#!/usr/bin/env python3
"""Prep-pack generator: builds career/08-interviewing/prep-packs.md from the interview prompt bank.

One pack per interview track: the practice prompts the research reports for that track, each with what a strong
answer covers, the red flags interviewers note, the roles it applies to and the skills it probes. The packs give
practice prompts and answer criteria, not model answers: the repository curates and does not teach (CHARTER).

Inputs (sources of truth):
  * data/interview_prompts.json (+ data/schemas/interview_prompts.schema.json)   tracks, the T0-14 system-design
                                                                                 archetypes A1-A15, and the prompts
  * data/role_scores.json      each role's interview track
  * data/skills_ontology.json  skill names

Usage:
    python3 scripts/build_prompts.py            # print the page
    python3 scripts/build_prompts.py --update   # write career/08-interviewing/prep-packs.md
    python3 scripts/build_prompts.py --check    # exit 1 if it is out of date or the data are invalid

Standard library only.
"""
import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import stack_lib as sl  # noqa: E402
from build_skills import load_ontology  # noqa: E402
from common import ref_errors, schema_errors, session_line_counts  # noqa: E402
from common import esc  # noqa: E402  (shared helpers)

ROOT = sl.ROOT
DATA = ROOT / "data" / "interview_prompts.json"
SCHEMA = ROOT / "data" / "schemas" / "interview_prompts.schema.json"
DOC = ROOT / "career" / "08-interviewing" / "prep-packs.md"
ALL_ROLE_TRACKS = ("behavioural", "coding")


def validate(data, scores, onto):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errs = [f"interview_prompts.json {e[2:]}" for e in schema_errors(data, schema, schema)]
    if errs:
        return errs
    lines = session_line_counts()
    roles = {r["id"] for r in scores["roles"]}
    known = set(onto["skills"]) | set(onto["classes"])
    tracks, archetypes = data["tracks"], data["archetypes"]
    missing = [t for t in scores["interview_tracks"] if t not in tracks]
    if missing:
        errs.append(f"interview_prompts.json: tracks missing for role_scores interview tracks {missing}")
    seen = set()
    for p in data["prompts"]:
        pid = p["id"]
        if pid in seen:
            errs.append(f"interview_prompts.json: duplicate prompt id {pid}")
        seen.add(pid)
        if p["track"] not in tracks:
            errs.append(f"interview_prompts.json: {pid} has unknown track {p['track']!r}")
        if p.get("archetype") and p["archetype"] not in archetypes:
            errs.append(f"interview_prompts.json: {pid} has unknown archetype {p['archetype']!r}")
        errs += [f"interview_prompts.json: {pid} names unknown role {r}" for r in p.get("roles", []) if r not in roles]
        errs += [f"interview_prompts.json: {pid} names unknown skill {s}" for s in p.get("skills", []) if s not in known]
        if not 3 <= len(p["covers"]) <= 6:
            errs.append(f"interview_prompts.json: {pid} has {len(p['covers'])} covers items; the schema requires 3-6")
        if not 1 <= len(p["red_flags"]) <= 3:
            errs.append(f"interview_prompts.json: {pid} has {len(p['red_flags'])} red flags; the schema requires 1-3")
        errs += ref_errors(p["source"], lines, f"interview_prompts.json: {pid} source")
        errs += ref_errors(p["answer_source"], lines, f"interview_prompts.json: {pid} answer_source")
    used_tracks = {p["track"] for p in data["prompts"]}
    used_arch = {p.get("archetype") for p in data["prompts"]}
    errs += [f"interview_prompts.json: track {t} has no prompt" for t in tracks if t not in used_tracks]
    errs += [f"interview_prompts.json: archetype {a} has no prompt" for a in archetypes if a not in used_arch]
    return errs


def render(data, scores, onto):
    tracks, archetypes, prompts = data["tracks"], data["archetypes"], data["prompts"]
    roles = OrderedDict((r["id"], r) for r in scores["roles"])
    hub = lambda rid: f"[{roles[rid]['name']}](../02-roles/hubs/{rid}.md)"  # noqa: E731
    sname = lambda s: (onto["skills"].get(s) or onto["classes"].get(s) or {"name": s})["name"]  # noqa: E731
    by_track = OrderedDict((t, [p for p in prompts if p["track"] == t]) for t in tracks)
    by_arch = OrderedDict((a, [p["id"] for p in prompts if p.get("archetype") == a]) for a in archetypes)
    grades = sorted({p["grade"] for p in prompts})

    out = ["---", "id: interviewing.prep-packs", 'title: "Interview Prep Packs: Practice Prompts by Track"', "content_type: reference",
           "stage: 8", "status: published", f"last_verified: {data['as_of']}",
           f'summary: "{len(prompts)} practice prompts for the GenAI interview tracks, each with what a strong answer covers, the red flags '
           f'interviewers note, the roles it applies to and its source; plus the {len(archetypes)} system-design archetypes."',
           "sources: [T0-14, T1-03]", "tags: [interviewing, practice, system-design, behavioural]",
           "generated_by: scripts/build_prompts.py", "---", "",
           "<!-- Generated by scripts/build_prompts.py from data/interview_prompts.json. Edit the data, not this page. -->", "",
           "# Interview Prep Packs: Practice Prompts by Track", "",
           "> Practice prompts for every GenAI interview track, each with what a strong answer covers and the red flags interviewers "
           "note, keyed to roles and to the system-design archetypes.", "",
           "## How to use these packs", "",
           "1. **Find your track.** Your role's hub names it; the table below lists the roles on each track. Classify the actual loop "
           "with the recruiter first ([interview loops](interview-loops.md)).",
           "2. **Practise aloud and timed.** For design prompts, use the [45-minute blueprint](system-design-archetypes.md); for "
           "behavioural prompts, the STAR-AI story bank in [behavioural calibration](behavioral-calibration.md); for coding, "
           "the formats in [coding rounds](coding-rounds.md).",
           "3. **Score yourself** against \"a strong answer covers\", then check the red flags. Re-run the prompt a week later.",
           "4. **Expect variation.** These are prompts the research reports or synthesises; real loops differ by company and level.", "",
           "The packs give practice prompts and answer criteria, not model answers. Each prompt carries its source and grade"
           + (f" ({', '.join(grades)})" if grades else "") + "; prompts the research does not report directly are labelled.", "",
           "## Tracks at a glance", "",
           "| Track | What it tests | Roles on this track | Prompts |", "|---|---|---|:---:|"]
    for tid, t in tracks.items():
        if tid in ALL_ROLE_TRACKS:
            members = "every role"
        else:
            members = ", ".join(hub(r) for r in roles if roles[r].get("interview_track") == tid) or "—"
        out.append(f"| [{t['name']}](#{sl.gh_slug(t['name'] + ' pack')}) | {esc(t['tests'])} | {members} | {len(by_track[tid])} |")
    no_track = [r for r in roles if roles[r].get("interview_track") is None]
    if no_track:
        out += ["", "No interview-track evidence in the corpus for: " + ", ".join(hub(r) for r in no_track)
                + ". Use the closest track and the behavioural pack."]
    loops = data.get("loop_types") or {}
    if loops:
        out += ["", "## Which system-design archetypes to drill first", "",
                "Classify the loop before you prepare: the three loop types drill different archetypes "
                "([interview loops](interview-loops.md)).", "",
                "| Loop type | Typical employers | Drill first | Then | Advice | Source |", "|---|---|---|---|---|---|"]
        for lt in loops.values():
            out.append(f"| **{esc(lt['name'])}** | {esc(lt['employers'])} | {', '.join(lt['drill_first']) or '—'} | "
                       f"{', '.join(lt.get('drill_next', [])) or '—'} | {esc(lt['advice'])} | {lt['source']} |")
    out += ["", "## The packs", ""]
    for tid, t in tracks.items():
        out += [f"### {t['name']} pack", "", f"*What it tests:* {t['tests'].rstrip('.')}. *Source:* {t['source'].rstrip('.')}.", ""]
        if not by_track[tid]:
            out += ["No prompt is reported for this track in the corpus.", ""]
            continue
        for p in by_track[tid]:
            arch = f" · {p['archetype']} {archetypes[p['archetype']]['name']}" if p.get("archetype") else ""
            out += [f"#### {p['id']}{arch}", "", f"> {p['prompt']}", "",
                    f"- **Source:** {p['reported_by']} [{p['grade']} · {p['source']}]"]
            out.append("- **A strong answer covers**" + (f" (from {p['answer_source']}):" if p.get("answer_source") else ":"))
            out += [f"  - {c}" for c in p["covers"]]
            if p.get("red_flags"):
                out.append("- **Red flags:**")
                out += [f"  - {r}" for r in p["red_flags"]]
            if p.get("roles"):
                out.append("- **Roles:** " + ", ".join(roles[r]["name"] for r in p["roles"]))  # hub links: the track table above
            if p.get("skills"):
                out.append("- **Skills probed:** " + ", ".join(sname(s) for s in p["skills"]))
            out.append("")
    out += ["## System-design archetypes", "",
            f"The {len(archetypes)} recurring GenAI system-design archetypes ([T0-14](../../research/sessions/T0-14-ai-system-design-interview-patterns.md) §6.3). "
            "The [system-design guide](system-design-archetypes.md) has a case card for each.", "",
            "| ID | Archetype | Family | Core tension | Staff-level tell | Most reported at | Prompts here |", "|---|---|---|---|---|---|---|"]
    for aid, a in archetypes.items():
        rep = esc(a.get("most_reported_at", "—")) + (f"; {esc(a['report_evidence'])}" if a.get("report_evidence") else "")
        out.append(f"| {aid} | {esc(a['name'])} | {a['family']} | {esc(a['core_tension'])} | {esc(a['staff_tell'])} | {rep} | "
                   f"{', '.join(by_arch[aid]) or '—'} |")
    out += ["", "## Evidence and limits", "",
            f"- {data['basis']}",
            "- No session measures pass rates by prompt, and no prep platform has independent outcome evidence [T1-03; T0-10]. "
            "Use the packs to practise the criteria, not to predict a loop.",
            f"- Data as of {data['as_of']}. Loop formats and AI-tool policies change; re-check a company's current loop with its recruiter.", "",
            "## Next steps", "",
            "- [Interview loops](interview-loops.md): classify your loop and plan the day.",
            "- [System-design archetypes](system-design-archetypes.md), [behavioural calibration](behavioral-calibration.md) and "
            "[coding rounds](coding-rounds.md): the frameworks behind these prompts.",
            "- [Project archetypes](../05-portfolio/project-archetypes.md): projects that give you stories and design depth.",
            "- [Offer evaluation](../09-compensation/offer-evaluation.md): what to do when the offer arrives.", ""]
    return "\n".join(out)


def build():
    data = json.loads(DATA.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    scores, onto = sl.load(sl.SCORES), load_ontology()
    errs = validate(data, scores, onto)
    if errs:
        raise SystemExit("interview prompts are invalid:\n  " + "\n  ".join(errs[:30]))
    return render(data, scores, onto)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = build()
    if args.update:
        DOC.write_text(text, encoding="utf-8")
        print(f"wrote {DOC.relative_to(ROOT)}")
    elif args.check:
        if not DOC.exists() or DOC.read_text(encoding="utf-8") != text:
            print(f"out of date: {DOC.relative_to(ROOT)}")
            sys.exit(1)
        print("up to date")
    else:
        print(text)


if __name__ == "__main__":
    main()
