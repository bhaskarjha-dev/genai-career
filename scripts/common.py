#!/usr/bin/env python3
"""Shared helpers for the repository scripts.

* schema_errors(): validates data against the JSON Schema subset the schemas in
  data/schemas/ use, and rejects any keyword it does not implement, so a schema
  rule can never be ignored silently.
* RELATIVE_TIME and prose(): the writing rule against relative-time words, applied to prose only.
* session_line_counts() and ref_errors(): check that citations such as
  "T0-10 L74, L539" or "T0-14 L385–386" point at lines that exist.

Imported by the generators and the validator; it writes nothing. Standard library only.
"""
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESSIONS = ROOT / "research" / "sessions"

# Keywords schema_errors() enforces, and keywords that only annotate.
SUPPORTED = {"$ref", "const", "enum", "type", "required", "properties", "additionalProperties", "propertyNames",
             "items", "minItems", "maxItems", "uniqueItems", "minLength", "maxLength", "pattern", "minimum",
             "maximum", "exclusiveMinimum", "exclusiveMaximum"}
ANNOTATIONS = {"$schema", "$id", "$comment", "$defs", "title", "description", "examples", "default"}
SCHEMA_CONTAINERS = {"properties", "$defs"}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)


def _is(value, kind):
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }[kind]


def schema_keyword_errors(sch, path="#"):
    """Every keyword in the schema must be one schema_errors() implements or an annotation."""
    errs = []
    if not isinstance(sch, dict):
        return errs
    for key, value in sch.items():
        if key in SCHEMA_CONTAINERS:
            for name, sub in value.items():
                errs += schema_keyword_errors(sub, f"{path}/{key}/{name}")
        elif key in ("items", "additionalProperties") and isinstance(value, dict):
            errs += schema_keyword_errors(value, f"{path}/{key}")
        elif key == "propertyNames":
            if set(value) - {"pattern"}:
                errs.append(f"$ schema {path}/propertyNames: only \"pattern\" is supported")
        elif key not in SUPPORTED and key not in ANNOTATIONS:
            errs.append(f"$ schema {path}: unsupported keyword \"{key}\" (implement it in scripts/common.py or remove it)")
    return errs


def schema_errors(inst, sch, root=None, path="$"):
    """Validate inst against sch (a JSON Schema subset). Returns a list of error strings."""
    if root is None:
        root = sch
    errs = schema_keyword_errors(root) if path == "$" else []
    return errs + _validate(inst, sch, root, path)


def _validate(inst, sch, root, path):
    if "$ref" in sch:
        node = root
        for part in sch["$ref"][2:].split("/"):
            node = node[part]
        return _validate(inst, node, root, path)
    errs = []
    if "const" in sch and inst != sch["const"]:
        errs.append(f"{path}: must equal {sch['const']!r}")
    if "enum" in sch and inst not in sch["enum"]:
        errs.append(f"{path}: {inst!r} is not one of {sch['enum']}")
    if "type" in sch:
        kinds = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(_is(inst, k) for k in kinds):
            return errs + [f"{path}: expected {' or '.join(kinds)}"]
    if isinstance(inst, dict):
        errs += [f"{path}: missing \"{k}\"" for k in sch.get("required", []) if k not in inst]
        props, names, extra = sch.get("properties", {}), sch.get("propertyNames"), sch.get("additionalProperties", True)
        for k, v in inst.items():
            if names and not re.search(names["pattern"], k):
                errs.append(f"{path}: key {k!r} does not match {names['pattern']}")
            if k in props:
                errs += _validate(v, props[k], root, f"{path}.{k}")
            elif extra is False:
                errs.append(f"{path}: unexpected key \"{k}\"")
            elif isinstance(extra, dict):
                errs += _validate(v, extra, root, f"{path}.{k}")
    elif isinstance(inst, list):
        if len(inst) < sch.get("minItems", 0):
            errs.append(f"{path}: needs at least {sch['minItems']} items")
        if "maxItems" in sch and len(inst) > sch["maxItems"]:
            errs.append(f"{path}: allows at most {sch['maxItems']} items")
        if sch.get("uniqueItems"):
            seen = [json.dumps(v, sort_keys=True) for v in inst]
            if len(seen) != len(set(seen)):
                errs.append(f"{path}: items must be unique")
        if "items" in sch:
            for i, v in enumerate(inst):
                errs += _validate(v, sch["items"], root, f"{path}[{i}]")
    elif isinstance(inst, str):
        if len(inst) < sch.get("minLength", 0):
            errs.append(f"{path}: shorter than {sch['minLength']}")
        if "maxLength" in sch and len(inst) > sch["maxLength"]:
            errs.append(f"{path}: longer than {sch['maxLength']}")
        if "pattern" in sch and not re.search(sch["pattern"], inst):
            errs.append(f"{path}: {inst!r} does not match {sch['pattern']}")
    elif _is(inst, "number"):
        if "minimum" in sch and inst < sch["minimum"]:
            errs.append(f"{path}: below {sch['minimum']}")
        if "maximum" in sch and inst > sch["maximum"]:
            errs.append(f"{path}: above {sch['maximum']}")
        if "exclusiveMinimum" in sch and inst <= sch["exclusiveMinimum"]:
            errs.append(f"{path}: must be above {sch['exclusiveMinimum']}")
        if "exclusiveMaximum" in sch and inst >= sch["exclusiveMaximum"]:
            errs.append(f"{path}: must be below {sch['exclusiveMaximum']}")
    return errs


# ---------------------------------------------------------------- small text helpers shared by the generators
def esc(text):
    """Make text safe inside a Markdown table cell."""
    return str(text).replace("|", "\\|").replace("\n", " ")


def short(name):
    """A name without its parenthetical qualifier: "PyTorch (2.x)" -> "PyTorch"."""
    return name.split(" (")[0]


def skill_name(onto, sid):
    """Display name of a skill or choose-one class ID in the skills ontology (the ID itself if unknown)."""
    e = onto["skills"].get(sid) or onto["classes"].get(sid)
    return e["name"] if e else sid


def gh_slug(heading):
    """The anchor GitHub gives a heading."""
    s = heading.strip().lower()
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def heading_slug(path, prefix, anchor=None):
    """Slug of the first H2 in path starting with prefix; else the explicit <a id="anchor"> kept when a heading was renamed."""
    text = Path(path).read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("## ") and line[3:].startswith(prefix):
            return gh_slug(line[3:])
    if anchor and f'<a id="{anchor}"></a>' in text:
        return anchor
    raise SystemExit(f"no heading starting {prefix!r} (or anchor {anchor!r}) in {Path(path).name}")


def require_anchor(path, slug):
    """Return slug if path has a heading (any level) with that slug or an explicit <a id="slug">; otherwise exit."""
    text = Path(path).read_text(encoding="utf-8")
    slugs = {gh_slug(m) for m in re.findall(r"^#{1,6}\s+(.+?)\s*$", re.sub(r"(?ms)^```.*?^```", "", text), re.M)}
    if slug in slugs or f'<a id="{slug}"></a>' in text:
        return slug
    raise SystemExit(f"no heading or anchor #{slug} in {Path(path).name}")


# ---------------------------------------------------------------- writing rules (EGP-1.0), shared by the validator and
# scripts/research_pipeline.py's report check
RELATIVE_TIME = re.compile(r"\b(currently|recently|nowadays|these days|as of now|right now|at present|at the moment)\b"
                           r"|\blatest\b(?![^\n]{0,40}\d{4}(-\d{2}){0,2})", re.I)


def prose(text):
    """Text with fenced code, inline code, HTML comments, link targets and quoted strings removed."""
    out, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    t = "\n".join(out)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"`[^`\n]*`", " ", t)
    t = re.sub(r"\]\([^)\s]*\)", "]", t)
    t = re.sub(r'"[^"\n]*"', " ", t)
    t = re.sub(r"\u201c[^\u201d\n]*\u201d", " ", t)
    return t


# ---------------------------------------------------------------- session line references
def session_line_counts():
    """{"T0-01": number of lines, ...} for every research session."""
    return OrderedDict((p.name[:5], len(p.read_text(encoding="utf-8").splitlines()))
                       for p in sorted(SESSIONS.glob("T*.md")))


CITE = re.compile(r"\b(T\d-\d\d)((?:[ ,;]*L\d+(?:\s*[–-]\s*L?\d+)?)+)")
LINE = re.compile(r"L(\d+)(?:\s*[–-]\s*L?(\d+))?")


def ref_errors(text, counts, where):
    """Errors for session line references in text that point past the end of the session, or at no session."""
    errs = []
    for sid, refs in CITE.findall(text or ""):
        if sid not in counts:
            errs.append(f"{where}: cites {sid}, which is not a session")
            continue
        for a, b in LINE.findall(refs):
            for n in (int(a), int(b or a)):
                if not 1 <= n <= counts[sid]:
                    errs.append(f"{where}: {sid} L{n} is past the end of the session ({counts[sid]} lines)")
            if b and int(b) < int(a):
                errs.append(f"{where}: {sid} L{a}–{b} is a reversed range")
    return errs
