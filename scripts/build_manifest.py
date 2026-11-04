#!/usr/bin/env python3
"""Manifest generator: builds llms.txt and data/manifest.json from document front matter.

Every document under career/ and the research index pages carry YAML front matter
(schema: data/schemas/frontmatter.schema.json). This script reads it and writes:

  * data/manifest.json  one record per document (path, id, title, type, stage, status,
                        version, last_verified, summary, sources, roles, generator,
                        section headings) for agents and tools
  * llms.txt            an index of the repository for language models (llmstxt.org
                        format): what the repo is, how to use it, and every document
                        with its one-line summary, grouped by stage

Usage:
    python3 scripts/build_manifest.py            # print the llms.txt text
    python3 scripts/build_manifest.py --update   # write llms.txt and data/manifest.json
    python3 scripts/build_manifest.py --check    # exit 1 if either is out of date

Standard library only.
"""
import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LLMS = ROOT / "llms.txt"
MANIFEST = ROOT / "data" / "manifest.json"
RESEARCH_PAGES = ["research/README.md", "research/findings.md", "research/ERRATA.md"]
STAGE_NAMES = OrderedDict([(1, "Landscape"), (2, "Roles"), (3, "Skills and technology"), (4, "Certifications"), (5, "Portfolio"),
                           (6, "Job search"), (7, "Networking"), (8, "Interviewing"), (9, "Compensation"), (10, "Onboarding"),
                           (11, "Tracks and transitions")])
DATA_FILES = OrderedDict([
    ("data/role_scores.json", "Scoring inputs for the role rankings: every pillar score with its [lo, mid, hi] range, evidence grade and sourced basis"),
    ("data/skills_ontology.json", "The skills ontology: 523 typed skills, choose-one classes, credentials, resume variants and every role's tiered, evidence-tagged skill links"),
    ("data/project_archetypes.json", "Proof-of-work project archetypes and the headline skills each one evidences"),
    ("data/findings.json", "Key findings of every research session, with grade, exact line and lifecycle stages"),
    ("data/manifest.json", "This manifest: every document with its front matter and section headings"),
    ("data/schemas/", "JSON Schemas for the skills ontology and for document front matter"),
])


def parse_front_matter(text):
    """Parse the flat YAML front matter used in this repository: scalars, quoted strings and inline lists."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = OrderedDict()
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"front matter line without a key: {line!r}")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",")]
            out[key.strip()] = [v for v in items if v]
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            out[key.strip()] = value[1:-1]
        elif re.fullmatch(r"-?\d+", value):
            out[key.strip()] = int(value)
        else:
            out[key.strip()] = value
    return out


def documents():
    paths = sorted((ROOT / "career").rglob("*.md")) + [ROOT / p for p in RESEARCH_PAGES if (ROOT / p).exists()]
    docs = []
    for p in paths:
        text = p.read_text(encoding="utf-8")
        fm = parse_front_matter(text)
        if fm is None:
            continue
        rel = p.relative_to(ROOT).as_posix()
        heads = [h.strip() for h in re.findall(r"^## (.+)$", text, re.M)]
        rec = OrderedDict([("path", rel)])
        rec.update(fm)
        rec["headings"] = heads
        docs.append(rec)
    return docs


def manifest_text(docs):
    order = sorted(docs, key=lambda d: (d.get("stage", 0) if d["path"].startswith("career/") else 99, d["path"]))
    return json.dumps(OrderedDict([("schema", "manifest/1.0"), ("generated_by", "scripts/build_manifest.py"),
                                   ("documents", order)]), indent=1, ensure_ascii=False) + "\n"


def llms_text(docs):
    by_path = {d["path"]: d for d in docs}

    def item(d):
        return f"- [{d['title']}]({d['path']}): {d['summary']}"

    out = ["# GenAI Career Intelligence System", "",
           "> Evidence-graded knowledge and guidance for GenAI careers: which roles exist and which are best, what each role needs "
           "(every concept, tool and soft skill, tiered and evidence-tagged), how to run a job search, and the 22 research sessions "
           "behind it all. Every empirical claim carries an EGP-1.0 grade (A/B measured, C small-sample or vendor, D judgement, "
           "M model output) and a date.", "",
           "How to use this repository:",
           "",
           "- Start at career/README.md (Start Here) or a stage README; each stage README links its guides and its graded research findings.",
           "- Facts live once: machine-readable sources of truth are in data/, and the generated documents are rebuilt from them by scripts/.",
           "- Research sessions are dated snapshots (October 2026): check research/ERRATA.md and each claim's date before relying on a figure.",
           "- Rules for agents that edit or answer from this repository are in AGENTS.md.", ""]
    out += ["## Start here", ""]
    for p in ["career/README.md", "research/README.md"]:
        if p in by_path:
            out.append(item(by_path[p]))
    out += ["- [ROADMAP.md](ROADMAP.md): What is covered, what is planned next, and the open decisions.",
            "- [AGENTS.md](AGENTS.md): Rules for AI agents: sources of truth, evidence standard, generators and validation.", ""]
    inventories = [d for d in docs if d["path"].startswith("career/03-skills-and-tech/inventories/")]
    for n, name in STAGE_NAMES.items():
        stage_docs = [d for d in docs if d["path"].startswith("career/") and d.get("stage") == n
                      and d not in inventories and d["path"] != "career/README.md"]
        if not stage_docs:
            continue
        stage_docs.sort(key=lambda d: (0 if d["path"].endswith("README.md") else 1, d["path"]))
        out += [f"## Stage {n:02d}: {name}", ""] + [item(d) for d in stage_docs] + [""]
    out += ["## Research", ""] + [item(by_path[p]) for p in RESEARCH_PAGES[1:] if p in by_path]
    out += ["- [research/sessions/](research/sessions/): The 22 Phase 0 research sessions (dated evidence reports with source ledgers).",
            "- [research/DECISIONS.md](research/DECISIONS.md): Architecture decision registry (D-001 to D-013).", ""]
    out += ["## Data", ""] + [f"- [{p}]({p}): {desc}" for p, desc in DATA_FILES.items()] + [""]
    out += ["## Optional", ""] + [item(d) for d in sorted(inventories, key=lambda d: d["path"])]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    docs = documents()
    outputs = {MANIFEST: manifest_text(docs), LLMS: llms_text(docs)}
    if args.update:
        for path, text in outputs.items():
            path.write_text(text, encoding="utf-8")
        print(f"wrote llms.txt and data/manifest.json ({len(docs)} documents)")
    elif args.check:
        stale = [str(p.relative_to(ROOT)) for p, t in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("out of date: " + ", ".join(stale))
            sys.exit(1)
        print("up to date")
    else:
        print(outputs[LLMS])


if __name__ == "__main__":
    main()
