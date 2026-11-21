#!/usr/bin/env python3
"""Learning-resources catalogue generator: builds career/03-skills-and-tech/learning-resources.md from data/learning_resources.json.

Implements decision D-027: stores all 52 sceptically rated learning resources from T0-68 plus
verified primary technical specifications and engineering references from T0-13, T0-16 and T0-69
in one machine-readable catalogue, validates it against its schema, data/role_scores.json and
research session line counts, and renders the user-facing catalogue.

Inputs (sources of truth):
  * data/learning_resources.json (+ data/schemas/learning_resources.schema.json)
  * data/role_scores.json (canonical role slugs)

Usage:
    python3 -B scripts/build_learning_resources.py            # print the page
    python3 -B scripts/build_learning_resources.py --update   # write career/03-skills-and-tech/learning-resources.md
    python3 -B scripts/build_learning_resources.py --check    # exit 1 if out of date or data are invalid

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
from common import RELATIVE_TIME, esc, ref_errors, schema_errors, session_line_counts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "learning_resources.json"
SCHEMA = ROOT / "data" / "schemas" / "learning_resources.schema.json"
SCORES = ROOT / "data" / "role_scores.json"
DOC = ROOT / "career" / "03-skills-and-tech" / "learning-resources.md"

VERDICT_ORDER = {"use": 0, "use-with-care": 1, "watch": 2, "avoid": 3}
VERDICT_LABEL = {
    "use": "Use",
    "use-with-care": "Use with care",
    "watch": "Watch",
    "avoid": "Avoid",
}


def _check_date(value, where, errs):
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        errs.append(f"{where}: {value!r} is not a valid ISO date")
        return None


def validate(data):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errs = [f"learning_resources.json {e[2:]}" for e in schema_errors(data, schema, schema)]
    if errs:
        return errs

    lines = session_line_counts()
    as_of = _check_date(data["as_of"], "learning_resources.json as_of", errs)
    review_by = _check_date(data["review_by"], "learning_resources.json review_by", errs)
    if as_of and review_by and review_by < as_of:
        errs.append(f"learning_resources.json: review_by ({review_by}) precedes as_of ({as_of})")

    w_sum = sum(data["rubric"]["weights"].values())
    if w_sum != 100:
        errs.append(f"learning_resources.json: rubric weights sum to {w_sum}, expected 100")

    scores = json.loads(SCORES.read_text(encoding="utf-8"))
    valid_roles = {r["id"] for r in scores["roles"]}
    valid_families = set(data["families"].keys())
    covered_roles = set()
    for fid, fam in data["families"].items():
        for rid in fam["roles"]:
            if rid not in valid_roles:
                errs.append(f"learning_resources.json: family {fid} references unknown role {rid!r}")
            covered_roles.add(rid)
        for field in ("minimal_free", "minimal_paid"):
            if RELATIVE_TIME.search(fam[field]):
                errs.append(f"learning_resources.json: family {fid}.{field} contains relative-time wording")
    missing_roles = sorted(valid_roles - covered_roles)
    if missing_roles:
        errs.append(f"learning_resources.json: canonical roles not mapped to any family: {missing_roles}")

    seen_ids = set()
    for res in data["resources"]:
        rid = res["id"]
        if rid in seen_ids:
            errs.append(f"learning_resources.json: duplicate resource id {rid!r}")
        seen_ids.add(rid)
        _check_date(res["as_of"], f"learning_resources.json: {rid} as_of", errs)
        errs += ref_errors(res["source"], lines, f"learning_resources.json: {rid} source")
        for fid in res["families"]:
            if fid not in valid_families:
                errs.append(f"learning_resources.json: {rid} references unknown family {fid!r}")
        for field in ("name", "cost_display", "outcome_evidence", "refund_terms", "note"):
            val = res.get(field) or ""
            if RELATIVE_TIME.search(val):
                errs.append(f"learning_resources.json: {rid}.{field} contains relative-time wording")
    return errs


def _sort_key(res):
    return (
        VERDICT_ORDER[res["verdict"]],
        0 if res["is_free"] else 1,
        -(res["score"] if res["score"] is not None else -1),
        res["name"].lower(),
    )


def _fmt_score(res):
    gates = ", ".join(res["gates"])
    if res["score"] is None:
        return f"Not scored ({gates})" if gates else "Primary ref"
    return f"{res['score']}/100 ({gates})" if gates else f"{res['score']}/100"


def _fmt_flags(res):
    parts = []
    if res["coi"]:
        parts.append("COI")
    if res["read_depth"] != "full-read":
        parts.append(res["read_depth"])
    return " · ".join(parts) if parts else "Full read"


def render(data):
    resources = data["resources"]
    families = data["families"]
    rubric = data["rubric"]

    sources = sorted({
        m for item in resources
        for m in re.findall(r"T[0-3]-\d\d", item["source"])
    })

    n_total = len(resources)
    n_t068 = sum(1 for r in resources if "T0-68" in r["source"])
    n_primary = n_total - n_t068
    n_free = sum(1 for r in resources if r["is_free"])
    n_paid = n_total - n_free
    by_verdict = OrderedDict((v, [r for r in resources if r["verdict"] == v]) for v in VERDICT_ORDER)

    out = [
        "---",
        "id: skills.learning-resources",
        'title: "Rated GenAI Learning Resources Catalogue: Courses, Docs, Books and Paid Programmes"',
        "content_type: reference",
        "stage: 3",
        "status: published",
        f"last_verified: {data['as_of']}",
        f"review_by: {data['review_by']}",
        f'summary: "{n_total} sceptically rated GenAI learning resources ({n_t068} from T0-68 plus {n_primary} primary technical specifications) mapped to all {len(families)} role families with rubric scores, refund checks, COI flags and hard gates."',
        f"sources: [{', '.join(sources)}]",
        "roles: [all]",
        "geos: [global, india]",
        "tags: [learning, resources, courses, books, bootcamps, gpu-compute, evals]",
        "generated_by: scripts/build_learning_resources.py",
        "---",
        "",
        "<!-- Generated by scripts/build_learning_resources.py from data/learning_resources.json. Edit the data, not this page. -->",
        "",
        "# Rated GenAI Learning Resources Catalogue: Courses, Docs, Books and Paid Programmes",
        "",
        f"> {n_total} sceptically rated GenAI learning resources ({n_free} free or free-video, {n_paid} paid) mapped across all {len(families)} canonical role families, with rubric scores, refund checks, conflict-of-interest (COI) flags and hard gates (decision D-027).",
        "",
        "## How to read this catalogue",
        "",
        "- **Start with the free minimal set for your role family.** Free primary specifications, university courses and open project tracks reach 75–97/100 in every family where a free route exists [M · T0-68 L74]. Sequence your study using [learning roadmaps](learning-roadmaps.md) and target skills from [role skill inventories](role-skill-inventories.md).",
        "- **No independent outcome audit exists for any GenAI-specific course or bootcamp.** CIRR had three publishing general software schools in early 2026, and Codesmith's audited 2023 software cohort predates its AI/ML syllabus [C · T0-68 L71]. Treat unverified placement percentages as unverified claims.",
        f"- **Rubric formula (Grade M):** `{rubric['formula']}` — Authority ({rubric['weights']['authority']}%), Currency ({rubric['weights']['currency']}%), Hands-on depth ({rubric['weights']['hands_on']}%), Role fit ({rubric['weights']['role_fit']}%), Cost ({rubric['weights']['cost']}%). Scores are tie-breakers, not job-outcome predictors [M · T0-68 L91, L121].",
        "- **Hard gates override raw scores:**",
    ]
    for gk, gv in rubric["gates"].items():
        out.append(f"  - **{gk}:** {gv}")
    out += [
        "- **Read-depth and COI disclosures:** Most T0-68 rows were rated from search extracts (`extract-only`, capped at Grade B under EGP-1.0); primary specifications added from T0-13, T0-16 and T0-69 are marked `Primary ref` rather than assigned a T0-68 rubric score. Vendor- or lab-authored resources are flagged `COI` — cross-check them with one independent source [B/C · T0-68 L22, L98].",
        "- **Consumer-law and refund pointers** summarise documented terms and public commission/regulator records; they are pointers, not legal advice.",
        "",
        "## At a glance",
        "",
        "| Verdict | Count | Meaning |",
        "|---|:---:|---|",
        f"| **Use** | {len(by_verdict['use'])} | {esc(rubric['bands']['use'])} |",
        f"| **Use with care** | {len(by_verdict['use-with-care'])} | {esc(rubric['bands']['use_with_care'])} |",
        f"| **Watch** | {len(by_verdict['watch'])} | {esc(rubric['bands']['watch'])} |",
        f"| **Avoid** | {len(by_verdict['avoid'])} | {esc(rubric['bands']['avoid'])} |",
        f"| **Total** | **{n_total}** | {n_t068} rated in T0-68 + {n_primary} primary technical specs/references |",
        "",
        "## Minimal sets by role family",
        "",
        "| Role family | Roles covered | Minimal free set | Minimal paid set |",
        "|---|---|---|---|",
    ]
    for fid, fam in families.items():
        role_links = ", ".join(f"`{r}`" for r in fam["roles"])
        out.append(
            f"| [{esc(fam['label'])}](#{fid}) | {role_links} | {esc(fam['minimal_free'])} | {esc(fam['minimal_paid'])} |"
        )

    out += ["", "## Resources by role family", ""]
    for fid, fam in families.items():
        group = sorted([r for r in resources if fid in r["families"]], key=_sort_key)
        out += [
            f'<a id="{fid}"></a>',
            f"### {esc(fam['label'])}",
            "",
            f"Roles: {', '.join(f'`{r}`' for r in fam['roles'])}.",
            "",
            "| Resource | Kind | Cost | Last update | Score / gates | Verdict | Flags & evidence |",
            "|---|---|---|---|---|---|---|",
        ]
        for res in group:
            rlink = f"[**{esc(res['name'])}**]({res['url']}) ({esc(res['provider'])})"
            upd = esc(res["last_update"]) if res.get("last_update") else "Not determined"
            note = f" {esc(res['note'])}" if res.get("note") else ""
            ev = f"{_fmt_flags(res)} · [{res['grade']} · {esc(res['source'])}].{note}"
            out.append(
                f"| {rlink} | `{res['kind']}` | {esc(res['cost_display'])} | {upd} | "
                f"{_fmt_score(res)} | **{VERDICT_LABEL[res['verdict']]}** | {ev} |"
            )
        out.append("")

    paid_items = sorted([r for r in resources if not r["is_free"]], key=_sort_key)
    out += [
        "## Paid programmes, cohorts and refund checks",
        "",
        "Before paying more than US$100 / ₹8,000, confirm in writing: total cost including any NBFC/lender finance charge, a full-refund window of at least 14 days from the first session (Gate G2), and the denominator/method behind any outcome claim [B · T0-68 L94–L95]. Consumer-law and refund notes below are evidence pointers, not legal advice.",
        "",
        "| Programme / resource | Cost | Outcome evidence | Refund terms | Verdict | Evidence |",
        "|---|---|---|---|---|---|",
    ]
    for res in paid_items:
        rlink = f"[**{esc(res['name'])}**]({res['url']})"
        ref_t = esc(res["refund_terms"]) if res.get("refund_terms") else "Not stated / standard retail"
        out.append(
            f"| {rlink} | {esc(res['cost_display'])} | {esc(res['outcome_evidence'])} | "
            f"{ref_t} | **{VERDICT_LABEL[res['verdict']]}** | {res['grade']} · {esc(res['source'])} ({res['as_of']}) |"
        )
    out.append("")

    out += [
        "## Evidence and limits",
        "",
        f"- {data['basis']}",
        "- **Maven AI Evals price reconciliation:** T0-68 (read 2026-11-13 via search extracts) recorded US$4,200 for the 2026-10-10 cohort; T0-21 opened the primary Maven enrolment page on 2026-11-14 and recorded US$4,500 for the 2027-01-30 to 2027-03-27 cohort with a >=20% team discount for two or more enrolments [A/B · T0-21 L91, L191, L278; T0-68 L325].",
        "- **Non-English gap:** T0-68 did not achieve systematic coverage of non-English GenAI courses or documentation beyond incidental pages [E · T0-68 L54].",
        "- **Proctored certifications** are out of scope here and are ranked separately in the [credential catalog](../04-certifications/credential-catalog.md) and [credentials by role](../04-certifications/credentials-by-role.md) (decision D-019).",
        "- **Compute and GPU rental tools** (Modal, RunPod, Kaggle, Hugging Face Learn, DeepLearning.AI) also appear in the cross-stage [tool catalog](../00-start/tool-catalog.md).",
        "",
        "## Next steps",
        "",
        "- **Sequence these resources by gate and timeframe:** [learning roadmaps](learning-roadmaps.md).",
        "- **Pick the exact skills for your target role:** [role skill inventories](role-skill-inventories.md) and [skills radar](skills-radar.md).",
        "- **Check proctored certifications separately:** [credential catalog](../04-certifications/credential-catalog.md).",
        "- **Turn study into graded proof of work:** [proof-of-work standards](../05-portfolio/proof-of-work-standards.md) and [project archetypes](../05-portfolio/project-archetypes.md).",
        "- Back to [Stage 03 overview](README.md) or [Start Here](../README.md).",
        "",
    ]
    return "\n".join(out)


def build():
    data = json.loads(DATA.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    errs = validate(data)
    if errs:
        raise SystemExit("learning_resources data are invalid:\n  " + "\n  ".join(errs[:30]))
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
