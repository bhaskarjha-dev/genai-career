#!/usr/bin/env python3
"""Personal gap analysis: compare your skill levels with one or more target roles.

You rate yourself 0-3 on the skills your target roles need (the T0-06 D9 scale stored in the ontology:
0 none, 1 tutorial-level, 2 built and shipped something small with feedback, 3 owns it in production).
The script compares your levels with the target level for each skill's tier (Must 3, or 2 at entry level;
Important 2; Should 1; Optional 0) and prints, to standard output only:

  * per target role: coverage of its Must and Important skills, and every gap;
  * across all targets: the skills to close first, weighted by tier and by how many targets need them;
  * the project archetypes that would evidence the most of your gaps.

Target levels are judgement (Grade D, anchored on T0-06); the tiers come from data/skills_ontology.json.
Keep your self-assessment outside the repository or under personal/ (git-ignored): it is personal data.

Usage:
    python3 -B scripts/gap_analysis.py --template ai-engineer applied-ai-engineer > personal/me.json
    # edit personal/me.json: set each level from 0 to 3
    python3 -B scripts/gap_analysis.py personal/me.json
    python3 -B scripts/gap_analysis.py personal/me.json --entry     # accept 2 for Must skills (entry level)

Self-assessment format: {"targets": ["<role id>", ...], "levels": {"<skill or class id>": 0-3, ...}}
A choose-one class (for example "cloud") counts at the best level among its members if the class itself is not rated.

Standard library only.
"""
import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_skills import load_ontology  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ARCHETYPES = ROOT / "data" / "project_archetypes.json"
TARGET = {"M": 3, "I": 2, "S": 1, "O": 0}
WEIGHT = {"M": 3, "I": 2, "S": 1, "O": 0}
TIER_NAME = {"M": "Must", "I": "Important", "S": "Should", "O": "Optional"}


def name(o, sid):
    e = o["skills"].get(sid) or o["classes"].get(sid)
    return e["name"] if e else sid


def level(o, levels, sid):
    if sid in levels:
        return levels[sid]
    if sid in o["classes"]:
        rated = [levels[m] for m in o["classes"][sid]["members"] if m in levels]
        if rated:
            return max(rated)
    return None


def template(o, targets):
    links = OrderedDict()
    for rid in targets:
        for l in o["roles"][rid]["links"]:
            if l["tier"] in ("M", "I", "S"):
                links.setdefault(l["id"], 0)
    return json.dumps(OrderedDict([("targets", targets), ("scale", o["meta"]["proficiency"]), ("levels", links)]),
                      indent=1, ensure_ascii=False)


def analyse(o, me, entry, archetypes):
    levels, targets = me["levels"], me["targets"]
    out = ["# Personal gap analysis", "",
           f"Targets: {', '.join(o['roles'][t]['name'] for t in targets)}. Scale: 0 none, 1 tutorial-level, 2 shipped something small, "
           f"3 owns it in production (T0-06 D9). Target levels per tier: Must {2 if entry else 3}, Important 2, Should 1 "
           "(judgement, Grade D).", ""]
    total = OrderedDict()
    unrated = set()
    for rid in targets:
        role = o["roles"][rid]
        rows, met, needed = [], 0, 0
        for l in role["links"]:
            tier = l["tier"]
            if tier not in ("M", "I", "S"):
                continue
            want = 2 if (entry and tier == "M") else TARGET[tier]
            have = level(o, levels, l["id"])
            if have is None:
                unrated.add(l["id"])
                have = 0
            if tier in ("M", "I"):
                needed += 1
                met += have >= want
            if have < want:
                rows.append((-WEIGHT[tier], -(want - have), name(o, l["id"]), tier, have, want))
                t = total.setdefault(l["id"], [0, []])
                t[0] += WEIGHT[tier] * (want - have)
                t[1].append(role["name"])
        rows.sort()
        out += [f"## {role['name']}", "",
                f"Must and Important skills at target level: {met} of {needed} ({round(100 * met / needed) if needed else 0}%). "
                f"Inventory: career/03-skills-and-tech/inventories/{rid}.md", ""]
        if rows:
            out += ["| Skill | Tier | You | Target | Gap |", "|---|---|:---:|:---:|:---:|"]
            out += [f"| {n} | {TIER_NAME[t]} | {h} | {w} | {w - h} |" for _, _, n, t, h, w in rows]
        else:
            out.append("No gaps at Must, Important or Should.")
        out.append("")
    ranked = sorted(total.items(), key=lambda kv: (-kv[1][0], name(o, kv[0])))
    out += ["## Close these first (across all targets)", "",
            "Score = tier weight (Must 3, Important 2, Should 1) × levels missing, summed over the targets that need the skill.", "",
            "| Skill | Score | Needed by |", "|---|:---:|---|"]
    out += [f"| {name(o, sid)} | {score} | {', '.join(roles)} |" for sid, (score, roles) in ranked[:15]]
    out.append("")
    if archetypes:
        gaps = {sid for sid, _ in ranked}
        scored = []
        for pid, p in archetypes.items():
            hit = [s for s in p["skills"] if s in gaps]
            if hit:
                scored.append((-sum(total[s][0] for s in hit), pid, p["name"], hit))
        scored.sort()
        out += ["## Projects that would evidence the most gaps", "",
                "From data/project_archetypes.json; the full cards are in career/05-portfolio/project-archetypes.md.", "",
                "| Archetype | Gap skills it evidences | Weighted gap covered |", "|---|---|:---:|"]
        out += [f"| {pid} {n} | {', '.join(name(o, s) for s in hit)} | {-sc} |" for sc, pid, n, hit in scored[:5]]
        out.append("")
    if unrated:
        out += [f"Unrated skills counted as 0: {', '.join(sorted(name(o, s) for s in unrated))}.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("assessment", nargs="?", help="your self-assessment JSON")
    ap.add_argument("--template", nargs="+", metavar="ROLE", help="print a blank self-assessment for these target roles")
    ap.add_argument("--entry", action="store_true", help="accept level 2 for Must skills (entry-level targets)")
    args = ap.parse_args()
    o = load_ontology()
    if args.template:
        bad = [r for r in args.template if r not in o["roles"]]
        if bad:
            raise SystemExit(f"unknown role ids {bad}; choose from: {', '.join(o['roles'])}")
        print(template(o, args.template))
        return
    if not args.assessment:
        ap.error("give a self-assessment file, or --template ROLE ...")
    me = json.loads(Path(args.assessment).read_text(encoding="utf-8"))
    bad = [r for r in me.get("targets", []) if r not in o["roles"]]
    if bad or not me.get("targets"):
        raise SystemExit(f"targets must be role ids from the ontology; unknown: {bad}")
    wrong = {k: v for k, v in me.get("levels", {}).items() if not (isinstance(v, int) and 0 <= v <= 3)}
    if wrong:
        raise SystemExit(f"levels must be integers 0-3: {wrong}")
    unknown = [k for k in me["levels"] if k not in o["skills"] and k not in o["classes"]]
    if unknown:
        raise SystemExit(f"unknown skill ids: {unknown}")
    archetypes = json.loads(ARCHETYPES.read_text(encoding="utf-8"))["archetypes"] if ARCHETYPES.exists() else {}
    print(analyse(o, me, args.entry, archetypes))


if __name__ == "__main__":
    main()
