#!/usr/bin/env python3
"""Skills-view generator: builds two decision views from the skills ontology.

Outputs (fully generated; edit the data, not the pages):
  * career/03-skills-and-tech/skills-radar.md         what to learn first, what sets each résumé family apart,
                                                      which skills only one or two roles demand, what to stop
                                                      investing in and what to watch
  * career/04-certifications/credentials-by-role.md   which credentials the evidence lists for each role, at
                                                      which tier, with each credential's dated status

Input (source of truth): data/skills_ontology.json — per-role tiered links with evidence, credentials with
statuses, résumé variants, and the register of devalued skills (T0-03 §4.3 and §6.8.2).

The radar's first five rings are computed (Grade M) from the tiers of the 24 individual-contributor roles, plus a sixth
multi-signal momentum view from T0-69 (adoption, telemetry, transaction and governance series across >=2 independent
signal types; NOT employer-posting-demand trends, because JobsPipe's AI Engineer page remained at count date 2026-09-10
on 2026-11-14). A tier is only as strong as the evidence behind its link (JD and S09 shares Grade B, session citations
A–C, practice-curated D), so the pages show the strongest evidence for each skill.

Usage:
    python3 scripts/build_skills_views.py            # list the outputs
    python3 scripts/build_skills_views.py --update   # write both pages
    python3 scripts/build_skills_views.py --check    # exit 1 if either page is out of date

Standard library only.
"""
import argparse
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_skills import load_ontology, validate_ontology  # noqa: E402
from common import esc, skill_name as name  # noqa: E402  (shared helpers)

ROOT = Path(__file__).resolve().parent.parent
RADAR = ROOT / "career" / "03-skills-and-tech" / "skills-radar.md"
CREDS = ROOT / "career" / "04-certifications" / "credentials-by-role.md"
CORE_MIN = 6            # Must or Important in at least this many of the 24 IC roles
FAMILY_IN = 0.5         # share of the family's roles with the skill at Must or Important
FAMILY_LIFT = 0.25      # ... and at least this much more often than in the other IC roles
FAMILY_TOP = 8
WATCH_STATES = ("acquired", "renamed", "beta", "development", "announced")
NOTICE = re.compile(r"\bCVE|breach|licen[cs]e", re.I)
GRADE_RANK = {"A": 0, "B": 1, "C": 2, "D": 3}
TIER_WORD = OrderedDict([("I", "Important"), ("O", "Optional"), ("X", "Avoid")])


def posting_date():
    """Retrieval date of the newest posting snapshot (data/posting_skill_shares.json)."""
    import json
    snaps = json.loads((ROOT / "data" / "posting_skill_shares.json").read_text(encoding="utf-8"))["snapshots"]
    return max(s["retrieved"] for s in snaps)


def type_label(o, sid):
    if sid in o["skills"]:
        t = o["skills"][sid]["type"]
    else:
        t = o["skills"][o["classes"][sid]["members"][0]]["type"]
    return o["meta"]["types"][t]["label"]


def nontech(o, sid):
    return type_label(o, sid) in {o["meta"]["types"][t]["label"] for t in
                                  ("communication", "behavioural", "business", "leadership", "domain", "research_craft")}


def ic_roles(o):
    """IC roles in GenAI target order."""
    return [rid for rid, _ in sorted(((k, r) for k, r in o["roles"].items() if isinstance(r["target"], int)),
                                     key=lambda kv: kv[1]["target"])]


def share_value(s):
    return float(s.rstrip("%"))


TITLE_KIND = re.compile(r"^(.*?)(?: \((closest measured title|adjacent|feeder)\))?$")
KIND_RANK = {None: 0, "closest measured title": 1, "adjacent": 2, "feeder": 3}
KIND_TEXT = {None: "", "closest measured title": " (closest measured title)", "adjacent": " (adjacent title)", "feeder": " (feeder title)"}


def best_evidence(o, sid, roles):
    """The strongest evidence behind a skill's links in the given roles, as a short tag.

    Posting shares measured on the role's own title beat borrowed ones (closest, adjacent, then feeder titles);
    then the higher share wins. S09 shares come next, then session citations by grade, then practice curation."""
    jd, s09, sess, practice = [], [], [], False
    for rid in roles:
        for l in o["roles"][rid]["links"]:
            if l["id"] != sid:
                continue
            if l["ev"] == "JD":
                title, kind = TITLE_KIND.match(l["src"][0].split(": ", 1)[1]).groups()
                jd.append((KIND_RANK[kind], -share_value(l["share"]), l["share"], title, kind))
            elif l["ev"] == "S09":
                s09.append((share_value(l["share"]), l["share"]))
            elif l["ev"] == "S":
                sess.append(l["grade"])
            else:
                practice = True
    if jd:
        _, _, share, title, kind = min(jd)
        return f"JD {share} of {title} postings{KIND_TEXT[kind]} [B]"
    if s09:
        return f"S09 {max(s09)[1]} [B]"
    if sess:
        g = min(sess, key=lambda x: GRADE_RANK.get(x[0], 9))
        return f"Session citation [{g}]"
    return "[P] practice-curated" if practice else "—"


def tier_counts(o, roles):
    """skill -> {tier: [role ids]} over the given roles."""
    out = OrderedDict()
    for rid in roles:
        for l in o["roles"][rid]["links"]:
            out.setdefault(l["id"], OrderedDict((t, []) for t in "MISOX"))[l["tier"]].append(rid)
    return out


def front(id_, title, stage, as_of, review_by, summary, sources, tags):
    assert 20 <= len(summary) <= 320, len(summary)
    return ["---", f"id: {id_}", f'title: "{title}"', "content_type: reference", f"stage: {stage}", "status: published",
            f"last_verified: {as_of}", f"review_by: {review_by}", f'summary: "{summary}"',
            f"sources: [{', '.join(sources)}]", f"tags: [{', '.join(tags)}]",
            "generated_by: scripts/build_skills_views.py", "---", "",
            "<!-- Generated by scripts/build_skills_views.py from data/skills_ontology.json. Edit the data, not this page. -->", ""]


# ---------------------------------------------------------------- the radar
def radar(o):
    meta, ic = o["meta"], ic_roles(o)
    n_ic = len(ic)
    counts = tier_counts(o, ic)
    rname = {rid: o["roles"][rid]["name"] for rid in o["roles"]}
    hub = lambda rid: f"[{rname[rid]}](../02-roles/hubs/{rid}.md)"  # noqa: E731
    mi = {sid: c["M"] + c["I"] for sid, c in counts.items()}

    core = [sid for sid in counts if len(mi[sid]) >= CORE_MIN]
    core.sort(key=lambda s: (-len(mi[s]), -len(counts[s]["M"]), name(o, s)))
    core_tech = [s for s in core if not nontech(o, s)]
    core_soft = [s for s in core if nontech(o, s)]

    variants = o["resume_variants"]
    families = OrderedDict()
    for rid in ic:
        families.setdefault(o["roles"][rid]["variant"], []).append(rid)
    fam_rows = OrderedDict()
    for v, members in families.items():
        others = [r for r in ic if r not in members]
        rows = []
        for sid in counts:
            inn = [r for r in mi[sid] if r in members]
            out = [r for r in mi[sid] if r in others]
            f_in, f_out = len(inn) / len(members), (len(out) / len(others) if others else 0)
            if f_in >= FAMILY_IN and f_in - f_out >= FAMILY_LIFT and (len(members) == 1 or len(inn) >= 2):
                rows.append((f_in - f_out, f_in, sid, inn, out))
        rows.sort(key=lambda x: (-x[0], -x[1], name(o, x[2])))
        fam_rows[v] = rows[:FAMILY_TOP]

    defining = OrderedDict()
    for rid in ic:
        items = []
        for l in o["roles"][rid]["links"]:
            musts = counts[l["id"]]["M"]
            if l["tier"] == "M" and len(musts) <= 2:
                other = [r for r in musts if r != rid]
                items.append(name(o, l["id"]) + (f" (also Must for {rname[other[0]]})" if other else ""))
        defining[rid] = items

    devalued = o.get("devalued", [])
    x_roles = OrderedDict()
    for rid in ic:
        for l in o["roles"][rid]["links"]:
            if l["tier"] == "X":
                x_roles.setdefault(l["id"], []).append(rid)

    watch = []
    for sid, e in o["skills"].items():
        st = e.get("status")
        if not st:
            continue
        if st["state"] in WATCH_STATES or (st["state"] == "active" and NOTICE.search(st.get("note", ""))):
            label = st["state"] if st["state"] != "active" else "active, with a security or licence notice"
            watch.append((st["state"] == "active", e["name"], label, st["as_of"], st.get("note", "")))
    watch.sort()

    n_def = sum(1 for v in defining.values() if v)
    momentum = o.get("momentum", [])
    review_by = meta["ttl"]["tool_status_reverify_by"]
    out = front("skills.radar", "GenAI Skills Radar: Learn First, Differentiate, Specialise, Replace", 3, meta["as_of"], review_by,
                "What to learn first, what sets each résumé family apart, which skills only one or two roles demand, what to "
                f"stop investing in, and multi-signal adoption momentum, built from the skills ontology for the {len(ic)} IC roles.",
                ["T0-03", "T0-06", "T0-14", "T0-15", "T0-16", "T0-69", "T0-71", "T1-03"], ["skills", "learning", "radar"])
    out += ["# GenAI Skills Radar: Learn First, Differentiate, Specialise, Replace", "",
            f"> Five rings computed from the skill tiers of the {len(ic)} individual-contributor roles, plus a sixth multi-signal "
            "momentum view (adoption, telemetry, transaction and governance signals — not two-date job-posting demand).", "",
            "## How to read this radar", "",
            "- **Rings 1–5 are computed** (Grade M) from the tiers in [data/skills_ontology.json](../../data/skills_ontology.json): "
            "Must, Important, Should, Optional and Avoid. A computed ring is only as strong as the links behind it, so each table shows "
            "the strongest evidence for the skill: a share of live postings [JD, Grade B], a share of the S09 corpus [S09, Grade B], "
            "a session citation [A–C] or practice curation [P, Grade D]. A skill backed only by [P] is a hypothesis to check against "
            "10–20 live postings.",
            "- **No two-date job-posting demand trend exists yet.** JobsPipe's AI Engineer skill-share page remained frozen at "
            "count date 2026-09-10 when re-checked on 2026-11-14 ([T0-69](../../research/sessions/T0-69-skill-tool-momentum-dated-series.md)). "
            "Ring 6 (**Multi-signal rising**) therefore reports only items backed by two or more independent adoption, telemetry, "
            "transaction or governance signal types across two or more dates — never employer-posting-demand trends.",
            "- **Leadership tracks are left out**: their inventories rest mostly on practice curation.",
            "- **Résumé families** are the five skill-based groupings behind the résumé variants (A–E); "
            "see the [résumé skills matrix](../06-job-search/resume-skills-matrix.md).", "",
            "## At a glance", "",
            "| Ring | Rule | Skills | What to do |", "|---|---|:---:|---|",
            f"| **1. Core** | Must or Important in at least {CORE_MIN} of the {n_ic} roles | {len(core)} | Learn first: they transfer across families |",
            f"| **2. Family differentiators** | Must or Important in at least half of a family's roles, and at least "
            f"{int(FAMILY_LIFT * 100)} percentage points more often than in the other roles | {sum(len(v) for v in fam_rows.values())} | "
            "Choose a family, then learn these |",
            f"| **3. Role-defining** | Must in only one or two roles | {sum(len(v) for v in defining.values())} across {n_def} roles | "
            "Learn when you commit to the role |",
            f"| **4. Replace** | Devalued in the research, or archived, dormant or retired | {len(devalued)} | Stop investing; learn the replacement |",
            f"| **5. Watch** | Acquired, renamed, beta, announced or carrying a security or licence notice | {len(watch)} | "
            f"Use with care; re-check by {review_by} |",
            f"| **6. Multi-signal rising** | >=2 independent adoption, telemetry, transaction or governance signal types across >=2 dates (not JD-share trends) | {len(momentum)} | "
            "Track closely; check COI and specification churn before over-investing |", "",
            "```mermaid", "flowchart LR",
            '  core["1. Core: learn first"] --> fam["2. Family differentiators"] --> role["3. Role-defining skills"]',
            '  replace["4. Replace: stop investing"] -.-> core',
            '  watch["5. Watch: use with care"] -.-> fam',
            '  mom["6. Multi-signal rising (adoption/telemetry)"] -.-> fam',
            "```", "",
            "## 1. Core: learn first", "",
            f"Skills at Must or Important in at least {CORE_MIN} of the {n_ic} roles, most widely required first.", "",
            "**Technical:**", "",
            "| Skill | Type | Must in | Important in | Families | Strongest evidence |", "|---|---|:---:|:---:|---|---|"]
    fam_of = {rid: o["roles"][rid]["variant"] for rid in ic}

    def core_row(sid):
        fams = "".join(sorted({fam_of[r] for r in mi[sid]}))
        return (f"| **{esc(name(o, sid))}** | {type_label(o, sid)} | {len(counts[sid]['M'])} | {len(counts[sid]['I'])} | {fams} | "
                f"{esc(best_evidence(o, sid, ic))} |")
    out += [core_row(s) for s in core_tech]
    out += ["", "**Non-technical:**", "",
            "| Skill | Type | Must in | Important in | Families | Strongest evidence |", "|---|---|:---:|:---:|---|---|"]
    out += [core_row(s) for s in core_soft]
    out += ["", "The behavioural competencies C1–C4 are the four that GenAI behavioural rounds score "
            "([behavioural calibration](../08-interviewing/behavioral-calibration.md)). The fuller cross-role tables, with every skill's "
            "count at any tier, are in [role skill inventories §2](role-skill-inventories.md#2-cross-role-views-what-recurs-for-universal-and-family-resumes).", "",
            "## 2. What sets each résumé family apart", "",
            "Skills that a family's roles require far more often than the other roles do. \"In family\" and \"elsewhere\" count the roles "
            "with the skill at Must or Important; \"(core)\" marks skills that are also in ring 1.", ""]
    for v, members in families.items():
        out += [f"### {v} · {variants[v]['name']}", "",
                f"Roles ({len(members)}): " + ", ".join(hub(r) for r in members) + ".", ""]
        rows = fam_rows[v]
        if not rows:
            out += ["No skill passes the rule: this family's roles share few requirements beyond the core.", ""]
            continue
        out += ["| Skill | Type | In family | Elsewhere | Strongest evidence |", "|---|---|:---:|:---:|---|"]
        for _, _, sid, inn, outs in rows:
            mark = " (core)" if sid in core else ""
            out.append(f"| **{esc(name(o, sid))}**{mark} | {type_label(o, sid)} | {len(inn)} of {len(members)} | "
                       f"{len(outs)} of {n_ic - len(members)} | {esc(best_evidence(o, sid, members))} |")
        if len(rows) < 3:
            out += ["", "Few skills pass the rule because this family's roles differ a lot from one another; "
                    "their role-defining skills (§3) matter more than the shared ones."]
        out.append("")
    out += ["## 3. Role-defining skills", "",
            "Skills at Must for a role and for at most one other: learn them when you commit to that role. "
            "Each role's full inventory is linked from its hub.", "",
            "| Role | Variant | Role-defining skills |", "|---|:---:|---|"]
    for rid in ic:
        items = defining[rid]
        out.append(f"| {hub(rid)} | {o['roles'][rid]['flavour']} | {esc('; '.join(items)) if items else '— (its Must skills are shared with three or more roles)'} |")
    out += ["", "## 4. Replace: what to stop investing in", "",
            "The research names these as devalued, or their projects are archived, dormant or retired. Each row says what still has value "
            "and what to learn instead. Facts reconciled through November 2026 ([T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) "
            "§4.3 and §6.8.2; [T0-69](../../research/sessions/T0-69-skill-tool-momentum-dated-series.md); "
            "[T0-71](../../research/sessions/T0-71-onboarding-growth-ai-roles.md)). RAGAS was removed from this ring "
            "after v0.4.4rc1 shipped on 2026-11-13 (304 days after v0.4.3), though eval-platform brand replaceability still applies.", "",
            "| Stop investing in | Evidence | Still useful | Do instead | Learn instead | Grade · source |", "|---|---|---|---|---|---|"]
    for d in devalued:
        inst = ", ".join(name(o, k) for k in d["instead"]) or "—"
        src = ", ".join(s.replace(":", " ") for s in d["src"])
        out.append(f"| **{esc(d['name'])}** ({esc(d['verdict'])}) | {esc(d['evidence'])} | {esc(d.get('residual', '—'))} | "
                   f"{esc(d['action'])} | {esc(inst)} | {d['grade']} · {src} |")
    if x_roles:
        out += ["", "Roles whose inventories tier these items Avoid: " + "; ".join(
            f"{name(o, sid)} ({', '.join(rname[r] for r in rs)})" for sid, rs in x_roles.items()) + "."]
    out += ["", "## 5. Watch: use with care", "",
            f"Tools and standards whose status changed or that carry a notice. Statuses are class V2 facts: re-verify by {review_by}.", "",
            "| Item | Status | As of | What it means |", "|---|---|---|---|"]
    for _, nm, label, as_of, note in watch:
        out.append(f"| **{esc(nm)}** | {label} | {as_of} | {esc(note)} |")
    out += ["", "Every tool with a status record, including those that are simply active, is in the "
            "[skills vocabulary watch list](skills-vocabulary.md#5-watch-list-tools-with-a-notable-status). "
            "Credential statuses are in [credentials by role](../04-certifications/credentials-by-role.md).", ""]
    if momentum:
        out += ["## 6. Multi-signal rising (adoption, telemetry & governance — not JD-share trends)", "",
                "Items corroborated by at least two independent signal types across two or more dates in "
                "[T0-69](../../research/sessions/T0-69-skill-tool-momentum-dated-series.md) (as of 2026-11-14). "
                "None of these has a two-date employer-posting-demand share series yet (JobsPipe's AI Engineer count date "
                "remained 2026-09-10 on 2026-11-14). Single-signal items (A2A, LangGraph, vLLM, SGLang, TRL, evals, OTel, "
                "voice AI, AI security, vector-DB popularity) are deliberately excluded from this table until a second dated "
                "signal corroborates them.", "",
                "| Skill or capability | Signal types | Dated multi-signal series | Caveats & COI | Grade · source |",
                "|---|---|---|---|---|"]
        for m in momentum:
            src = ", ".join(s.replace(":", " ") for s in m["src"])
            sigs = ", ".join(s.replace("_", " ") for s in m["signals"])
            coi_tag = " [COI]" if m.get("coi") else ""
            out.append(f"| **{esc(m['name'])}**{coi_tag} | {esc(sigs)} | {esc(m['evidence'])} | "
                       f"{esc(m['caveat'])} | {esc(m['grade'])} · {src} |")
        out.append("")
    out += ["## Evidence and limits", "",
            f"- Rings 1–5 are computed from {sum(len(r['links']) for r in o['roles'].values())} tiered links in the ontology (as of {meta['as_of']}); "
            f"their evidence mix is in [role skill inventories §4](role-skill-inventories.md#4-verification). The rules and thresholds "
            f"(at least {CORE_MIN} roles for the core; half the family and {int(FAMILY_LIFT * 100)} points of lift for differentiators; "
            "at most two roles for role-defining skills) are judgement (Grade D).",
            f"- Posting shares come from JobsPipe (retrieved {posting_date()}, underlying AI Engineer count date 2026-09-10; "
            "[data](../../data/posting_skill_shares.json)). Several roles borrow a feeder or adjacent title's shares; "
            "the evidence column names the title.",
            "- The replace ring reproduces the research's verdicts with their grades; it does not add new ones.",
            "- Ring 6 measures multi-signal adoption, telemetry, transaction and governance movement as of 2026-11-14, NOT employer-posting "
            f"demand over time. Treat rings 1–5 as a snapshot, and re-check tools and statuses by {review_by}.", "",
            "## Next steps", "",
            "- [Learning roadmaps](learning-roadmaps.md): the order to learn in, by family and background.",
            "- [Role skill inventories](role-skill-inventories.md) and the [role hubs](../02-roles/hubs/README.md): every skill for one role.",
            "- [Project archetypes](../05-portfolio/project-archetypes.md): projects that prove the core and family skills.",
            "- [Agentic protocols](agentic-protocols.md): MCP, A2A and AG-UI in depth.", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- credentials by role
def credentials(o):
    meta = o["meta"]
    review_by = meta["ttl"]["tool_status_reverify_by"]
    roles = ic_roles(o) + [rid for rid, r in o["roles"].items() if not isinstance(r["target"], int)]
    rname = {rid: o["roles"][rid]["name"] for rid in o["roles"]}
    hub = lambda rid: f"[{rname[rid]}](../02-roles/hubs/{rid}.md)"  # noqa: E731
    cr = o["credentials"]
    listed = OrderedDict((cid, []) for cid in cr)
    for rid in roles:
        for cl in o["roles"][rid]["credentials"]:
            listed[cl["id"]].append((rid, cl["tier"]))
    with_any = [rid for rid in roles if o["roles"][rid]["credentials"]]
    without = [rid for rid in roles if not o["roles"][rid]["credentials"]]
    dates = sorted({c["status"]["as_of"] for c in cr.values() if c.get("status")})

    def status(c):
        st = c.get("status")
        if not st:
            return "not assessed in the research corpus (practice-curated)"
        return f"{st['state']} ({st['as_of']}): {st.get('note', '')}".rstrip(": ")

    out = front("certifications.by-role", "Credentials by Role", 4, meta["as_of"], review_by,
                "Which certifications the evidence lists for each GenAI role, at which tier, and each credential's dated status, "
                "generated from the skills ontology.",
                ["T0-11", "T0-15", "T0-29", "T0-30", "T0-31", "T0-32", "T0-34", "T0-54", "T0-59", "T0-60", "T0-61", "T0-62", "T3-01", "T3-02"],
                ["certifications", "credentials"])
    n_ret = sum(1 for c in cr.values() if c.get("status", {}).get("state") == "retired")
    n_beta = sum(1 for c in cr.values() if c.get("status", {}).get("state") == "beta")
    n_ann = sum(1 for c in cr.values() if c.get("status", {}).get("state") == "announced")
    out += ["# Credentials by Role", "",
            "> Which certifications the evidence lists for each role, at which tier, and each credential's status, "
            f"as of {dates[-1] if dates else meta['as_of']}.", "",
            "## How to read this page", "",
            "- **Credentials are tie-breakers, not skills.** Their signal depends on the hiring channel [B/C · T0-11, T0-31, T0-34]. "
            "Decide whether to sit one with the [credential ROI guide](credential-roi.md) and compare all 150 evaluated credentials "
            "in the [credential catalog](credential-catalog.md) before using this role map.",
            "- **Tiers:** *Important* means the evidence treats it as a differentiator for the role; *Optional* means it helps only "
            "where the channel or the posting rewards it; *Avoid* means retired, so new candidates should not pursue it "
            "(holders may still list it with its date).",
            f"- **Statuses** are class V2 facts, as of the dates shown; re-verify by {review_by}.", "",
            "## At a glance", "",
            f"- {len(with_any)} of {len(roles)} roles list at least one credential; {len(without)} list none, so proof of work decides.",
            f"- Across {len(cr)} role-mapped credentials: {n_ret} retired, {n_beta} in beta, and {n_ann} announced/booking-ambiguous (verify live portal before scheduling).", "",
            "## By role", "",
            "| Role | Variant | Important | Optional | Avoid (retired) |", "|---|:---:|---|---|---|"]
    for rid in roles:
        cells = OrderedDict((t, []) for t in TIER_WORD)
        for cl in o["roles"][rid]["credentials"]:
            cells.setdefault(cl["tier"], []).append(f"{cr[cl['id']]['name']}" + (f" ({cl['note']})" if cl.get("note") else ""))
        if not o["roles"][rid]["credentials"]:
            out.append(f"| {hub(rid)} | {o['roles'][rid]['flavour']} | — | — | — |")
            continue
        out.append(f"| {hub(rid)} | {o['roles'][rid]['flavour']} | " +
                   " | ".join(esc("; ".join(cells[t])) or "—" for t in TIER_WORD) + " |")
    out += ["", "## By credential", "",
            "| Credential | Issuer | Level | Status | Listed for |", "|---|---|---|---|---|"]
    for cid, c in cr.items():
        who = "; ".join(f"{rname[r]} ({TIER_WORD.get(t, t)})" for r, t in listed[cid]) or "no role (listed for reference)"
        out.append(f"| **{esc(c['name'])}** | {esc(c['issuer'])} | {c['level']} | {esc(status(c))} | {esc(who)} |")
    out += ["", "## Roles with no credential in the evidence", "",
            "For these roles the research names no credential that changes hiring outcomes; publications, merged contributions, "
            "shipped systems or case studies carry the signal instead:", "",
            ", ".join(hub(r) for r in without) + ".", "",
            "## Evidence and limits", "",
            "- Tiers and notes come from the role inventories in [data/skills_ontology.json](../../data/skills_ontology.json), which cite "
            "Phase 0 ([T0-11](../../research/sessions/T0-11-certification-cloud-credential-roi.md), "
            "[T0-15](../../research/sessions/T0-15-regulatory-ai-governance-career-families.md)), Phase 3 ([T3-01](../../research/sessions/T3-01-genai-certification-stack-ranking-sequencing.md), "
            "[T3-02](../../research/sessions/T3-02-genai-certification-stack-ranking-sequencing.md)) and RP2 certification and role dossiers "
            "([T0-29](../../research/sessions/T0-29-certifications-frontier-labs-ai-native-vendors.md), "
            "[T0-31](../../research/sessions/T0-31-certifications-data-enterprise-ai-platforms.md), "
            "[T0-32](../../research/sessions/T0-32-certifications-gpu-infrastructure-open-source.md), "
            "[T0-34](../../research/sessions/T0-34-certifications-governance-security-privacy-audit.md)). "
            "Hyperscaler cloud exams (T0-28) and vendor learning paths (T0-33) are deferred past 2026-12-05.",
            "- For the full 150-credential scored database (fees, proctoring, channel weights and pass/skip verdicts), see the "
            "[credential catalog](credential-catalog.md).",
            "- Credentials without a status are not assessed in the research corpus; their tiers are practice-curated (Grade D).",
            "- No session measures a credential's effect on pay or offers. The evidence is about screening signal by channel.", "",
            "## Next steps", "",
            "- [Credential catalog](credential-catalog.md): full 150-credential scored database and channel tables.",
            "- [Credential ROI](credential-roi.md): whether to get one, which one, and how to show it.",
            "- [Skills radar](../03-skills-and-tech/skills-radar.md): the skills that matter more than any credential.",
            "- [Proof-of-work standards](../05-portfolio/proof-of-work-standards.md): what to build instead.", ""]
    return "\n".join(out)


def build():
    o = load_ontology()
    errs = validate_ontology(o)
    if errs:
        raise SystemExit("skills ontology is invalid:\n  " + "\n  ".join(errs[:20]))
    return OrderedDict([(RADAR, radar(o)), (CREDS, credentials(o))])


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    pages = build()
    stale = [p for p, text in pages.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if args.update:
        for p in stale:
            p.write_text(pages[p], encoding="utf-8")
            print(f"wrote {p.relative_to(ROOT)}")
        if not stale:
            print("up to date")
    elif args.check:
        if stale:
            print("out of date: " + ", ".join(str(p.relative_to(ROOT)) for p in stale))
            sys.exit(1)
        print("up to date")
    else:
        for p in pages:
            print(p.relative_to(ROOT), "(stale)" if p in stale else "(current)")


if __name__ == "__main__":
    main()
