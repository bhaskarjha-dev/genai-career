#!/usr/bin/env python3
"""Target-employers directory generator: builds career/01-landscape/target-employers.md from data/target_employers.json.

Implements decision D-024: stores vetted target employers (ATS vendor, public board URL, regions,
sponsorship evidence, remote policy, India presence, evidence grades and source lines) alongside
official sponsor-register pointers in one machine-readable file, validates it against its schema
and session line counts, and generates the user-facing directory with a computed review_by date.

Inputs (sources of truth):
  * data/target_employers.json (+ data/schemas/target_employers.schema.json)

Usage:
    python3 -B scripts/build_employers.py            # print the page
    python3 -B scripts/build_employers.py --update   # write career/01-landscape/target-employers.md
    python3 -B scripts/build_employers.py --check    # exit 1 if out of date or data are invalid

Standard library only.
"""
import argparse
import datetime
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import esc, ref_errors, schema_errors, session_line_counts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "target_employers.json"
SCHEMA = ROOT / "data" / "schemas" / "target_employers.schema.json"
DOC = ROOT / "career" / "01-landscape" / "target-employers.md"

# EGP-1.0 expiry classes in days (T1-02 §10.6; D-018). V6 has no expiry.
TTL_DAYS = {"V0": 14, "V1": 31, "V2": 90, "V3": 180, "V4": 365, "V5": 1095}


def _check_date(value, where, errs):
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        errs.append(f"{where}: {value!r} is not a valid ISO date")
        return None


def validate(data):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errs = [f"target_employers.json {e[2:]}" for e in schema_errors(data, schema, schema)]
    if errs:
        return errs
    lines = session_line_counts()
    _check_date(data["as_of"], "target_employers.json as_of", errs)

    seen_reg = set()
    for reg in data["sponsor_registers"]:
        rid = reg["id"]
        if rid in seen_reg:
            errs.append(f"target_employers.json: duplicate sponsor_register id {rid}")
        seen_reg.add(rid)
        _check_date(reg["as_of"], f"target_employers.json: register {rid} as_of", errs)
        errs += ref_errors(reg["source"], lines, f"target_employers.json: register {rid} source")

    seen_emp = set()
    valid_types = set(data["employer_types"].keys())
    for emp in data["employers"]:
        eid = emp["id"]
        if eid in seen_emp:
            errs.append(f"target_employers.json: duplicate employer id {eid}")
        seen_emp.add(eid)
        if emp["employer_type"] not in valid_types:
            errs.append(f"target_employers.json: {eid} unknown employer_type {emp['employer_type']!r}")
        _check_date(emp["as_of"], f"target_employers.json: {eid} as_of", errs)
        errs += ref_errors(emp["source"], lines, f"target_employers.json: {eid} source")
        op = emp.get("open_roles")
        if op is not None:
            _check_date(op["date"], f"target_employers.json: {eid} open_roles.date", errs)
            has_count = op.get("count") is not None
            has_range = op.get("lo") is not None and op.get("hi") is not None
            if not has_count and not has_range:
                errs.append(f"target_employers.json: {eid} open_roles needs count or lo/hi")
            if has_range and op["lo"] > op["hi"]:
                errs.append(f"target_employers.json: {eid} open_roles lo ({op['lo']}) > hi ({op['hi']})")
    return errs


def _expiry(item):
    days = TTL_DAYS.get(item["ttl"])
    if days is None:
        return None
    return datetime.date.fromisoformat(item["as_of"]) + datetime.timedelta(days=days)


def _fmt_open_roles(op):
    if not op:
        return "Not read"
    if op.get("count") is not None:
        num = f"{op['count']:,}"
    else:
        num = f"{op['lo']:,}–{op['hi']:,}"
    return f"{num} ({op['date']}; {esc(op['filter'])})"


def _fmt_hq_regions(emp):
    hq = esc(emp["hq"]) if emp.get("hq") else "Unverified"
    regs = ", ".join(emp["regions"]) if emp.get("regions") else "—"
    return f"{hq} ({regs})"


def _fmt_ats(emp):
    ats = esc(emp["ats"]) if emp.get("ats") else "Unestablished"
    slug = emp.get("ats_slug")
    if slug and emp.get("ats"):
        return f"{ats} (`{esc(slug)}`)"
    if slug:
        return f"Conflict / unverified (`{esc(slug)}`)"
    return ats


def _fmt_remote_india(emp):
    parts = []
    if emp.get("remote_policy"):
        parts.append(f"**Remote:** {esc(emp['remote_policy'])}")
    if emp.get("india_presence"):
        parts.append(f"**India:** {esc(emp['india_presence'])}")
    return "<br>".join(parts) if parts else "—"


def render(data):
    employers = data["employers"]
    registers = data["sponsor_registers"]
    type_meta = data["employer_types"]

    expiries = [d for d in (_expiry(x) for x in employers + registers) if d is not None]
    review_by = min(expiries).isoformat()
    oldest_check = min(datetime.date.fromisoformat(x["as_of"]) for x in employers + registers if x["ttl"] != "V6")

    sources = sorted({
        m for item in employers + registers
        for m in re.findall(r"T[0-3]-\d\d", item["source"])
    })

    by_type = OrderedDict((k, [e for e in employers if e["employer_type"] == k]) for k in type_meta)
    n_boards = sum(1 for e in employers if e.get("board_url"))
    n_india = sum(1 for e in employers if e.get("india_presence"))

    out = [
        "---",
        "id: landscape.target-employers",
        'title: "Target GenAI Employers Directory: ATS Boards, Sponsorship Registers and India Presence"',
        "content_type: reference",
        "stage: 1",
        "status: published",
        f"last_verified: {data['as_of']}",
        f"review_by: {review_by}",
        f'summary: "{len(employers)} vetted GenAI target employers grouped by employer type with ATS platforms, '
        f'public board URLs, sponsorship evidence, India presence and {len(registers)} official sponsor registers."',
        f"sources: [{', '.join(sources)}]",
        "roles: [all]",
        "geos: [global, us, uk, europe, canada, india, apac, gulf]",
        "tags: [employers, target-list, ats, sponsor-registers, visa, india]",
        "generated_by: scripts/build_employers.py",
        "---",
        "",
        "<!-- Generated by scripts/build_employers.py from data/target_employers.json. Edit the data, not this page. -->",
        "",
        "# Target GenAI Employers Directory: ATS Boards, Sponsorship Registers and India Presence",
        "",
        f"> {len(employers)} vetted GenAI target employers grouped by employer type with ATS platforms, public board URLs, "
        f"sponsorship evidence, India presence and {len(registers)} official sponsor registers.",
        "",
        "## How to read this directory",
        "",
        "- **System of record:** use each employer's own board for live role counts. Third-party counts disagree by 10–40% or more across dates and definitions [B · T0-27 L71].",
        "- **ATS routing shifts:** employer ATS attribution conflicts across trackers and moves over time (for example Ashby grew from 14.1% to 19.1% of Huntr ATS-routed applications between Q3 2025 and Q3 2026 while Lever fell from 10.6% to 5.3%) [B · T0-27 L58]. Confirm the live board URL before applying or running watchlists.",
        "- **Registers screen; they do not promise sponsorship.** A licence or historical filing proves prior sponsorship capacity, not an open visa-eligible role [A · T0-27 L73]. For contested V0 visa rules (including US H-1B weighted selection and fee litigation), see [visa and relocation](../11-tracks/visa-and-relocation.md).",
        "- **Evidence grades** follow EGP-1.0: A primary source opened directly, B established secondary source or platform display (including Extract-only government pages downgraded from T0-27), C third-party or single source, D recalled or judgement.",
        f"- **Freshness:** directory as of {data['as_of']}; earliest expiry among live V1/V2 records sets `review_by: {review_by}`. Historical July 2026 TrueUp snapshots are kept as dated baselines, not live counts.",
        "",
        "## At a glance",
        "",
        "| Employer type | Tracked employers | Verified board URLs | Named India presence |",
        "|---|:---:|:---:|:---:|",
    ]
    for slug, meta in type_meta.items():
        group = by_type[slug]
        urls = sum(1 for e in group if e.get("board_url"))
        ind = sum(1 for e in group if e.get("india_presence"))
        out.append(f"| [{esc(meta['label'])}](#{slug}) | {len(group)} | {urls} | {ind} |")
    out.append(f"| **Total** | **{len(employers)}** | **{n_boards}** | **{n_india}** |")

    out += ["", "## Employers by type", ""]
    for slug, meta in type_meta.items():
        group = by_type[slug]
        if not group:
            continue
        out += [
            f'<a id="{slug}"></a>',
            f"### {esc(meta['label'])}",
            "",
            meta["description"],
            "",
            "| Employer | HQ (regions) | ATS | Open-role snapshot | Sponsorship evidence | Remote and India presence | Evidence & notes |",
            "|---|---|---|---|---|---|---|",
        ]
        for emp in group:
            name = f"[**{esc(emp['name'])}**]({emp['board_url']})" if emp.get("board_url") else f"**{esc(emp['name'])}**"
            spons = esc(emp["sponsorship"]) if emp.get("sponsorship") else "—"
            note_txt = f" {esc(emp['note'])}" if emp.get("note") else ""
            ev = f"{emp['grade']} · {esc(emp['source'])} (as of {emp['as_of']}, {emp['ttl']}).{note_txt}"
            out.append(
                f"| {name} | {_fmt_hq_regions(emp)} | {_fmt_ats(emp)} | {_fmt_open_roles(emp.get('open_roles'))} | "
                f"{spons} | {_fmt_remote_india(emp)} | {ev} |"
            )
        out.append("")

    out += [
        "## Official sponsor registers",
        "",
        "Use these primary registers to verify sponsorship eligibility before investing time in relocation-dependent targets. No public employer sponsor list was located for Ireland in T0-27 [C · T0-27 L179]; registers for Germany, Japan, Singapore, Switzerland, Israel and Gulf states were not individually audited in T0-27 [E · T0-27 L284].",
        "",
        "| Jurisdiction | Register | Update cadence | What it holds | Limits | Evidence & as of |",
        "|---|---|---|---|---|---|",
    ]
    for reg in registers:
        rname = f"[**{esc(reg['name'])}**]({reg['url']})"
        out.append(
            f"| {esc(reg['jurisdiction'])} | {rname} | {esc(reg['cadence'])} | {esc(reg['holds'])} | "
            f"{esc(reg['limits'])} | {reg['grade']} · {esc(reg['source'])} ({reg['as_of']}, {reg['ttl']}) |"
        )
    out.append("")

    out += [
        "## Evidence and limits",
        "",
        f"- {data['basis']}",
        f"- Oldest active non-V6 record date: {oldest_check.isoformat()}; earliest computed expiry: {review_by}.",
        "- Coverage is thickest for US frontier labs, Big Tech, AI-native startups and large India GCCs/IT services, and thin for European labs (Aleph Alpha, DeepL, Black Forest Labs, Helsing), Gulf labs beyond G42, Korea, Israel, Australia and public-sector bodies beyond US Tech Force and UK AISI [E · T0-27 L287–L288].",
        "- Structural employer-type comparisons (pay structures, equity risk adjustment, interview loops, onboarding and credentials) live in [employer landscape](employer-landscape.md) (decision D-019).",
        "- Target-list building, tiering and review cadence live in [job-search strategy](../06-job-search/job-search-strategy.md).",
        "",
        "## Next steps",
        "",
        "- **Understand each employer type:** [employer landscape](employer-landscape.md) and [market overview](market-overview.md).",
        "- **Turn this directory into a tiered watchlist:** [job-search strategy](../06-job-search/job-search-strategy.md).",
        "- **Find postings and set up ATS alerts:** [channels and boards](../06-job-search/channels-and-boards.md).",
        "- **Track outreach and applications:** [application operating system](../06-job-search/application-operating-system.md).",
        "- **Check live visa and sponsorship rules:** [visa and relocation](../11-tracks/visa-and-relocation.md) and the [India remote playbook](../11-tracks/india-remote-playbook.md).",
        "- **Check external datasets and job-search tools:** [tool catalog](../00-start/tool-catalog.md).",
        "- Back to [Start Here](../README.md).",
        "",
    ]
    return "\n".join(out)


def build():
    data = json.loads(DATA.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    errs = validate(data)
    if errs:
        raise SystemExit("target_employers data are invalid:\n  " + "\n  ".join(errs[:30]))
    return render(data)


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
