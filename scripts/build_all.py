#!/usr/bin/env python3
"""Run every generator in dependency order, then the validator.

GENERATORS below is the single registry of generators: scripts/validate_docs.py imports it, and fails if a
script that supports --check is missing from it.

Usage:
    python3 -B scripts/build_all.py            # --update every generator in order, then validate
    python3 -B scripts/build_all.py --check    # --check every generator (as CI does), then validate

After an --update run it prints `git diff --stat`, so you can see every file the generators rewrote.
Standard library only.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

# Dependency order: each generator runs after the generators whose output it reads.
GENERATORS = [
    "build_findings.py",       # research sessions -> research/findings.md, data/findings.json
    "build_index.py",          # data/role_titles.json -> A–Z index block in the role catalog
    "rank_roles.py",           # data/role_scores.json -> role-rankings blocks
    "target_roles.py",         # role scores -> each role's `target` in data/skills_ontology.json
    "build_skills.py",         # skills ontology -> vocabulary, inventories index, per-role inventories
    "build_resume_matrix.py",  # skills ontology -> résumé skills matrix
    "resume_layers.py",        # ontology, archetypes -> computed résumé-layer blocks
    "build_skills_views.py",   # ontology -> skills radar, credentials by role
    "build_archetypes.py",     # project archetypes -> project-archetypes page
    "build_role_map.py",       # stack model, scores, ontology -> role map
    "build_role_hubs.py",      # everything above -> 29 role hubs and their index
    "build_prompts.py",        # interview prompts -> prep packs
    "build_tool_catalog.py",   # tools -> tool catalog
    "research_pipeline.py",    # research pipeline 2 catalogue, briefs, data -> tracker in research/pipeline-2/README.md
    "build_manifest.py",       # last: front matter of every document -> llms.txt, data/manifest.json
]


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="check every generator instead of updating")
    args = ap.parse_args()
    mode = "--check" if args.check else "--update"
    for script in GENERATORS:
        res = run([sys.executable, "-B", str(SCRIPTS / script), mode])
        out = (res.stdout + res.stderr).strip().splitlines()
        print(f"{script:24s} {'ok' if res.returncode == 0 else 'FAILED'}  {out[-1] if out else ''}")
        if res.returncode != 0:
            print("\n".join(out[-20:]))
            return 1
    val = run([sys.executable, "-B", str(SCRIPTS / "validate_docs.py")])
    print(val.stdout.strip())
    if not args.check:
        diff = run(["git", "diff", "--stat"])
        if diff.returncode == 0 and diff.stdout.strip():
            print("\nFiles changed in the working tree:\n" + diff.stdout.rstrip())
    return val.returncode


if __name__ == "__main__":
    sys.exit(main())
