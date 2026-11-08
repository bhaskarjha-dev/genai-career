#!/usr/bin/env python3
"""A-Z title index generator for career/02-roles/role-catalog.md.

Every title string the catalogs classify lives in data/role_titles.json (title, type,
maps-to role id, evidence or note; schema data/schemas/role_titles.schema.json). The
script checks it, sorts it and renders the table between the <!-- BEGIN GENERATED INDEX -->
and <!-- END GENERATED INDEX --> markers, so the order and the counts are computed, not
typed by hand. Canonical titles must match the role ids in data/role_scores.json.

Usage:
    python3 scripts/build_index.py              # print the table and the type counts
    python3 scripts/build_index.py --update     # rewrite the index block in the role catalog
    python3 scripts/build_index.py --check      # exit 1 if the index block is out of date

Standard library only.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common import schema_errors  # noqa: E402
DOC = ROOT / "career" / "02-roles" / "role-catalog.md"
BEGIN, END = "<!-- BEGIN GENERATED INDEX -->\n", "\n<!-- END GENERATED INDEX -->"

DATA = ROOT / "data" / "role_titles.json"
SCHEMA = ROOT / "data" / "schemas" / "role_titles.schema.json"
SCORES = ROOT / "data" / "role_scores.json"


def load():
    """[(title, type, maps_to, note)] from data/role_titles.json, after schema and cross-file checks."""
    data = json.loads(DATA.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errs = [f"role_titles.json {e[2:]}" for e in schema_errors(data, schema, schema)]
    if not errs:
        ids = {r["id"] for r in json.loads(SCORES.read_text(encoding="utf-8"))["roles"]}
        canon = {e["maps_to"] for e in data["titles"] if e["type"] == "Canonical"}
        if canon != ids:
            errs.append(f"role_titles.json: canonical titles {sorted(canon ^ ids)} differ from the role ids in data/role_scores.json")
        errs += [f"role_titles.json: {e['title']!r} has type {e['type']!r}, which is not in types"
                 for e in data["titles"] if e["type"] not in data["types"]]
    if errs:
        raise SystemExit("data/role_titles.json is invalid:\n  " + "\n  ".join(errs))
    return [(e["title"], e["type"], e["maps_to"], e["note"]) for e in data["titles"]]


def sort_key(title):
    # Case-insensitive; ignore punctuation and leading articles for a natural A-Z order.
    t = title.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def table(E):
    titles = [e[0] for e in E]
    dup = [t for t, c in Counter(titles).items() if c > 1]
    if dup:
        raise SystemExit(f"duplicate titles: {dup}")
    canon = {e[2] for e in E if e[1] == "Canonical"}
    mapped = {e[2] for e in E if e[2] not in ("—",) and not e[2].startswith("feeder")}
    if mapped - canon:
        raise SystemExit(f"titles map to non-canonical slugs: {sorted(mapped - canon)}")
    rows = sorted(E, key=lambda e: sort_key(e[0]))
    out = ["| # | Title (as seen) | Type | Maps to | Evidence / note |", "|:---:|---|---|---|---|"]
    for i, (t, ty, m, ev) in enumerate(rows, 1):
        mm = f"`{m}`" if m not in ("—",) and not m.startswith("feeder") else m
        out.append(f"| {i} | {t} | {ty} | {mm} | {ev} |")
    return "\n".join(out)


def block_span(text):
    if text.count(BEGIN) != 1:
        raise SystemExit("expected exactly one BEGIN GENERATED INDEX marker")
    i = text.index(BEGIN) + len(BEGIN)
    j = text.find(END, i - 1)
    if j < 0:
        raise SystemExit("no END GENERATED INDEX marker")
    return i, j


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true", help="rewrite the index block in the role catalog")
    g.add_argument("--check", action="store_true", help="exit 1 if the index block is out of date")
    args = ap.parse_args()
    E = load()
    tbl = table(E)
    if args.update or args.check:
        text = DOC.read_text(encoding="utf-8")
        i, j = block_span(text)
        if args.check:
            if text[i:j] != tbl:
                print("out of date: career/02-roles/role-catalog.md (A-Z index)")
                sys.exit(1)
            print("up to date")
            return
        DOC.write_text(text[:i] + tbl + text[j:], encoding="utf-8")
        print(f"updated the A-Z index ({len(E)} titles)")
        return
    print(tbl)
    print()
    print("TOTAL", len(E))
    for k, v in sorted(Counter(e[1] for e in E).items(), key=lambda kv: -kv[1]):
        print(k, v)


if __name__ == "__main__":
    main()
