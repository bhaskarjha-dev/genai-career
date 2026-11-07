#!/usr/bin/env python3
"""Shared loading and validation for the stack model (decision D-015).

Used by scripts/build_role_map.py, scripts/build_role_hubs.py and scripts/validate_docs.py, so that the
footprint rules live in one place:

  * data/stack_model.json follows data/schemas/stack_model.schema.json;
  * every skills-ontology category is mapped exactly once (to a layer, a plane or the cross-cutting list);
  * every role in data/role_scores.json has a valid work footprint, definition and interview track;
  * every specialisation points at known roles, known skills and a known layer or plane.

Standard library only.
"""
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STACK = DATA / "stack_model.json"
STACK_SCHEMA = DATA / "schemas" / "stack_model.schema.json"
SCORES = DATA / "role_scores.json"
ONTOLOGY = DATA / "skills_ontology.json"
ARCHETYPES = DATA / "project_archetypes.json"
STATUS_LABEL = {"E": "Established", "V": "Verified", "W": "Watch", "A": "Absorbed"}
TIER_LABEL = {"M": "Must", "I": "Important", "S": "Should", "O": "Optional", "X": "Avoid"}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)


def areas(stack):
    """Every place a footprint can point to, in display order: layers L6..L1, then the planes."""
    out = OrderedDict()
    for k in sorted(stack["layers"], key=lambda k: -int(k[1:])):
        out[k] = stack["layers"][k]
    for k, v in stack["planes"].items():
        out[k] = v
    return out


def area_label(stack, code):
    a = areas(stack)[code]
    return f"{code} {a['name']}" if code in stack["layers"] else a["name"]


def category_area(stack):
    """Map each skills-ontology category to its layer or plane (cross-cutting categories map to None)."""
    out = {}
    for code, a in areas(stack).items():
        for c in a["categories"]:
            out[c] = code
    for c in stack["cross_cutting_categories"]:
        out[c] = None
    return out


def home(role):
    """The role's main place on the map: its primary layer, else its first plane."""
    st = role["stack"]
    return st["primary"] or st["planes"][0]


def gh_slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def errors(stack, scores, onto):
    """Return a list of problems; empty when the stack model, footprints and specialisations are consistent."""
    from build_skills import schema_errors  # local import keeps this module light for callers
    errs = []
    schema = load(STACK_SCHEMA)
    errs += [f"stack_model.json {e[2:]}" for e in schema_errors(stack, schema, schema)]
    if errs:
        return errs
    # categories: each ontology category exactly once
    placed = []
    for a in areas(stack).values():
        placed += a["categories"]
    placed += stack["cross_cutting_categories"]
    cats = list(onto["meta"]["categories"])
    dup = sorted({c for c in placed if placed.count(c) > 1})
    if dup:
        errs.append(f"stack_model.json: categories mapped more than once: {dup}")
    missing = [c for c in cats if c not in placed]
    unknown = [c for c in placed if c not in cats]
    if missing:
        errs.append(f"stack_model.json: ontology categories not mapped to a layer, plane or the cross-cutting list: {missing}")
    if unknown:
        errs.append(f"stack_model.json: categories not in the skills ontology: {unknown}")
    # footprints
    layers, planes = set(stack["layers"]), set(stack["planes"])
    tracks = scores.get("interview_tracks", {})
    for r in scores["roles"]:
        rid = r["id"]
        for f in ("definition", "stack", "interview_track"):
            if f not in r:
                errs.append(f"role_scores.json: {rid} has no '{f}'")
        if "stack" not in r:
            continue
        st = r["stack"]
        if set(st) != {"primary", "secondary", "planes", "basis", "grade"}:
            errs.append(f"role_scores.json: {rid} stack must have exactly primary, secondary, planes, basis, grade")
            continue
        if st["primary"] is not None and st["primary"] not in layers:
            errs.append(f"role_scores.json: {rid} primary layer {st['primary']!r} is not one of {sorted(layers)}")
        if st["primary"] is None and not st["planes"]:
            errs.append(f"role_scores.json: {rid} has no primary layer, so it needs at least one plane")
        bad = [x for x in st["secondary"] if x not in layers or x == st["primary"]]
        if bad:
            errs.append(f"role_scores.json: {rid} secondary layers invalid or repeat the primary: {bad}")
        badp = [x for x in st["planes"] if x not in planes]
        if badp:
            errs.append(f"role_scores.json: {rid} unknown planes {badp}")
        if st["grade"] != "D" or len(st["basis"]) < 20:
            errs.append(f"role_scores.json: {rid} footprint needs grade D and a basis of at least 20 characters")
        if not (20 <= len(r.get("definition", "")) <= 320):
            errs.append(f"role_scores.json: {rid} definition must be 20-320 characters")
        t = r.get("interview_track")
        if t is not None and t not in tracks:
            errs.append(f"role_scores.json: {rid} interview track {t!r} is not defined in interview_tracks")
    # specialisations
    ids = {r["id"] for r in scores["roles"]}
    known_skills = set(onto["skills"]) | set(onto["classes"])
    seen = set()
    for s in stack["specialisations"]:
        if s["id"] in seen:
            errs.append(f"stack_model.json: duplicate specialisation id {s['id']}")
        seen.add(s["id"])
        if s["where"] not in layers | planes:
            errs.append(f"stack_model.json: specialisation {s['id']} sits at unknown {s['where']!r}")
        for h in s["home"]:
            if h not in ids:
                errs.append(f"stack_model.json: specialisation {s['id']} names unknown role {h}")
        for k in s["skills"]:
            if k not in known_skills:
                errs.append(f"stack_model.json: specialisation {s['id']} names unknown skill {k}")
    return errs
