#!/usr/bin/env python3
"""Role-hub generator: builds one page per canonical role in career/02-roles/hubs/ plus an index.

Each hub is a uniform card assembled from the sources of truth, so a role's key facts are on one page while
the evidence stays where it lives:
  * data/role_scores.json      definition, family, status, footprint, interview track, pillar scores with grades
  * scripts/rank_roles.py      CCI rank, band and Monte Carlo interval (computed, Grade M)
  * data/skills_ontology.json  target order, Must and Important skills, credentials, prerequisites, proof,
                               résumé variant, keywords to mirror, things to avoid
  * data/project_archetypes.json + scripts/resume_layers.py  archetype coverage and role similarity (Grade M)
  * data/stack_model.json      layer and plane names, specialisations

Usage:
    python3 scripts/build_role_hubs.py            # list what would be written
    python3 scripts/build_role_hubs.py --update   # write career/02-roles/hubs/*.md (removes stale hub files)
    python3 scripts/build_role_hubs.py --check    # exit 1 if any hub is out of date

Standard library only.
"""
import argparse
import datetime
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import rank_roles as rr  # noqa: E402
import stack_lib as sl  # noqa: E402
from build_resume_matrix import project  # noqa: E402
from build_skills import load_ontology  # noqa: E402
from resume_layers import analyse  # noqa: E402
from common import heading_slug, require_anchor  # noqa: E402  (shared helpers)

HUBS = sl.ROOT / "career" / "02-roles" / "hubs"
PILLARS = [("demand", "Demand"), ("comp", "Pay"), ("durability", "Durability"), ("leverage", "Leverage")]
PERSONA_LABEL = rr.PERSONA_LABEL
POSTING_TTL_DAYS = 31  # EGP-1.0 class V1: the demand scores rest on live posting counts
NO_INDIA = "No India evidence"


def review_by_for(scores, r):
    """31 days (EGP-1.0 class V1) after the oldest posting-count source this role's demand bases cite."""
    text = r["demand"]["basis"] + " " + r.get("india", {}).get("demand", {}).get("basis", "")
    dates = [d for src, d in scores["count_sources"].items() if src in text] or [scores["as_of"]]
    return (datetime.date.fromisoformat(min(dates)) + datetime.timedelta(days=POSTING_TTL_DAYS)).isoformat()


def counted_on(scores, r):
    text = r["demand"]["basis"] + " " + r.get("india", {}).get("demand", {}).get("basis", "")
    found = [f"{src} {d}" for src, d in scores["count_sources"].items() if src in text]
    return "; ".join(found) if found else f"as of {scores['as_of']}"


def num(x):
    return f"{x:g}"


def access_mark(v):
    return "●" if v >= 7.5 else "◐" if v >= 4 else "○"


def footprint(stack, st):
    main = sl.area_label(stack, st["primary"]) if st["primary"] else f"{stack['planes'][st['planes'][0]]['name']} (plane)"
    parts = [main]
    if st["secondary"]:
        parts.append("also " + ", ".join(sl.area_label(stack, x) for x in st["secondary"]))
    planes = [stack["planes"][p]["name"] for p in st["planes"] if not (st["primary"] is None and p == st["planes"][0])]
    if planes:
        parts.append("planes: " + ", ".join(planes))
    return "; ".join(parts)


def context():
    stack, scores = sl.load(sl.STACK), sl.load(sl.SCORES)
    onto = load_ontology()
    errs = sl.errors(stack, scores, onto)
    if errs:
        raise SystemExit("stack model or role footprints are invalid:\n  " + "\n  ".join(errs))
    archetypes = sl.load(sl.ARCHETYPES)["archetypes"]
    data = project(onto)
    an = analyse(data, archetypes)
    _, res = rr.tables(scores)
    covers = {}
    for oid, r in onto["roles"].items():
        for rid in r.get("covers", [oid]):
            covers[rid] = oid
    rnk, tgt = sl.ROOT / "career" / "02-roles" / "role-rankings.md", sl.ROOT / "career" / "02-roles" / "genai-target-roles.md"
    slugs = {"board": heading_slug(rnk, "2. Master Leaderboard"), "lead": heading_slug(rnk, "4. Leadership"),
             "appendix": heading_slug(rnk, "Appendix A"), "method": heading_slug(rnk, "1. Method"),
             "order": require_anchor(tgt, "at-a-glance-the-sorted-target-list"),
             "bg": require_anchor(tgt, "best-targets-by-background"),
             "tlead": require_anchor(tgt, "leadership-and-independent-tracks-when-to-target-them"),
             "months": require_anchor(sl.ROOT / "career" / "11-tracks" / "career-transitions.md", "modelled-months-to-a-first-offer")}
    n_ic = sum(1 for r in scores["roles"] if r["track"] == "ic")
    review_by = min(review_by_for(scores, r) for r in scores["roles"])
    playbooks = OrderedDict((f, (v["label"], set(v["roles"]))) for f, v in scores["track_playbooks"].items())
    return dict(stack=stack, scores=scores, onto=onto, archetypes=archetypes, data=data, an=an, res=res, covers=covers, slugs=slugs,
                n_ic=n_ic, n_lead=len(scores["roles"]) - n_ic, review_by=review_by, playbooks=playbooks)


def ranks(ctx):
    res = ctx["res"]
    base = {x["id"]: x for x in res["base"]}
    lead = {x["id"]: x for x in res["leadership"]}
    return base, lead, res["monte_carlo"], {x["id"]: x for x in res["india"]}


def target_label(ctx, rid, lead):
    oid = ctx["covers"].get(rid)
    if oid and isinstance(ctx["onto"]["roles"][oid]["target"], int) and oid == rid:
        return f"#{ctx['onto']['roles'][oid]['target']} of {ctx['n_ic']}"
    return f"Leadership #{lead[rid]['rank']} (ranked separately)" if rid in lead else "—"


def hub(ctx, r):
    stack, onto, data, an, slugs = ctx["stack"], ctx["onto"], ctx["data"], ctx["an"], ctx["slugs"]
    base, lead, mc, india = ranks(ctx)
    rid, name = r["id"], r["name"]
    oid = ctx["covers"].get(rid)
    orole = onto["roles"].get(oid) if oid else None
    ic = r["track"] == "ic"
    tracks = ctx["scores"]["interview_tracks"]
    variant = onto["resume_variants"].get(orole["variant"]) if orole else None
    as_of = max(ctx["scores"]["as_of"], onto["meta"]["as_of"], stack["as_of"])
    if ic:
        b, m = base[rid], mc[rid]
        cci = f"#{b['rank']} of {ctx['n_ic']} · band {b['band']} · Monte Carlo rank {m['median']} (P10–P90 {m['p10']}–{m['p90']})"
    else:
        cci = f"Leadership #{lead[rid]['rank']} of {ctx['n_lead']} (ranked separately)"
    flav = f"{orole['flavour']} {variant['flavours'][orole['flavour']].split(':')[0]}" if orole else "— (no résumé variant: case studies and referrals instead)"
    status = f"{sl.STATUS_LABEL[r['status']]} ({r['status']})"
    summary = (f"{name} on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof "
               f"it needs, how it is interviewed and how to present for it, with links to the full evidence.")
    if len(summary) > 320:
        summary = summary[:317] + "..."
    out = ["---", f"id: roles.hub.{rid}", f'title: "{name.replace(chr(34), chr(39))}: Role Hub"', "content_type: reference", "stage: 2",
           "status: published", f"last_verified: {as_of}", f"review_by: {review_by_for(ctx['scores'], r)}",
           f'summary: "{summary.replace(chr(34), chr(39))}"', f"roles: [{rid}]",
           "generated_by: scripts/build_role_hubs.py", "---", "",
           "<!-- Generated by scripts/build_role_hubs.py from data/. Edit the data or the generator, not this page. -->", "",
           f"# {name}", "", f"> {r['definition']}", "",
           "| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |",
           "|---|---|---|---|---|---|",
           f"| {r['family']} | {footprint(stack, r['stack'])} | {status} | {target_label(ctx, rid, lead)} | {cci} | {flav} |", "",
           "Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). "
           "The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; "
           "the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).", ""]
    if not ic:
        books = [(f, label) for f, (label, ids) in ctx["playbooks"].items() if rid in ids]
        start = (f"[{books[0][1]}](../../11-tracks/{books[0][0]})" if books
                 else "[growth and progression](../../10-onboarding/growth-and-progression.md) (the IC-versus-manager decision)")
        out += [f"> **Start with the track playbook:** {start}. Most of the evidence for leadership and independent tracks lives there; "
                "this hub keeps the scores and pointers.", ""]
    out += [
           "## The numbers", "",
           "| Pillar | Score (0–10: mid, range) | Grade | Basis |", "|---|---|:---:|---|"]
    for key, label in PILLARS:
        p = r[key]
        out.append(f"| {label} | {num(p['mid'])} ({num(p['lo'])}–{num(p['hi'])}) | {p['grade']} | {p['basis']} |")
    if not ic and "access" in r:
        a = r["access"]
        out.append(f"| Access (experience gate) | {num(a['mid'])} ({num(a['lo'])}–{num(a['hi'])}) | {a['grade']} | {a['basis']} |")
    out += ["", f"Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#{slugs['method']}); the composite (CCI) is a model output (Grade M). "
            f"The same inputs, with every source, are in [Appendix A](../role-rankings.md#{slugs['appendix']}). "
            "Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).", ""]
    if ic and "india" in r:
        out += ["**India lens:**", "", "| Pillar | Score (0–10: mid, range) | Grade | Basis |", "|---|---|:---:|---|"]
        for key, label in (("demand", "India demand"), ("comp", "India pay")):
            p = r["india"][key]
            out.append(f"| {label} | {num(p['mid'])} ({num(p['lo'])}–{num(p['hi'])}) | {p['grade']} | {p['basis']} |")
        placeholders = [k for k in ("demand", "comp") if r["india"][k]["basis"].startswith(NO_INDIA)]
        if len(placeholders) == 2:
            out += ["", "India rank: not shown. Neither India input has evidence for this role (both are Grade D placeholders), "
                    "so a rank would only restate the defaults.", ""]
        else:
            note = f" One input ({'India ' + placeholders[0]}) is a Grade D placeholder." if placeholders else ""
            out += ["", f"India rank (CCI with India inputs): #{india[rid]['rank']} of {ctx['n_ic']}.{note}", ""]
    out += ["## Who it suits", ""]
    if ic:
        pa = r["persona_access"]
        out += ["| " + " | ".join(PERSONA_LABEL[p] for p in rr.PERSONAS) + " |", "|" + "|".join(":---:" for _ in rr.PERSONAS) + "|",
                "| " + " | ".join(f"{access_mark(pa[p])} {num(pa[p])}" for p in rr.PERSONAS) + " |", "",
                "Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), "
                "◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). "
                f"The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#{slugs['months']}); "
                f"the best targets by background are in [GenAI target roles](../genai-target-roles.md#{slugs['bg']}).", ""]
    else:
        out += [f"A leadership or independent track: people reach it after years of experience. When to target it: "
                f"[GenAI target roles: leadership and independent tracks](../genai-target-roles.md#{slugs['tlead']}).", ""]
    out += ["## What you need", ""]
    if orole:
        drole = data["roles"][oid]
        sk = data["skills"]
        tiers = OrderedDict()
        for l in orole["links"]:
            tiers[l["tier"]] = tiers.get(l["tier"], 0) + 1
        counts = " · ".join(f"{sl.TIER_LABEL[t]} {tiers[t]}" for t in "MISOX" if t in tiers)
        out += [f"- **Must (headline):** {', '.join(sk[k]['name'] for k in drole['must'])}.",
                f"- **Important (headline):** {', '.join(sk[k]['name'] for k in drole['important'])}.",
                f"- **Full inventory:** {len(orole['links'])} skills ({counts}), each with its evidence and posting keywords: "
                f"[{oid}.md](../../03-skills-and-tech/inventories/{oid}.md).",
                f"- **Prerequisites:** {orole.get('prereq') or '—'}"]
        creds = orole.get("credentials", [])
        if creds:
            cred_txt = "; ".join(f"{onto['credentials'][c['id']]['name']} ({sl.TIER_LABEL[c['tier']]}: {c.get('note', '')})" for c in creds)
            out.append(f"- **Credentials (tie-breakers, not skills):** {cred_txt}. Whether one is worth it: "
                       "[credential ROI](../../04-certifications/credential-roi.md).")
        if oid != rid:
            out.append(f"- These skills come from the shared inventory for {orole['name']}, which covers this role.")
        out.append("- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); "
                   "in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).")
    else:
        out += ["- No skill inventory of its own: the catalog maps independent and fractional practice to the "
                "[leadership skill map](../../03-skills-and-tech/role-skill-maps.md#skills-leadership)."]
    out += ["", "## How to prove it", ""]
    if orole:
        out.append(f"- **What the evidence asks for:** {orole.get('proof') or '—'}")
        covs = sorted(((an["role_cov"](oid, [pid]), pid) for pid in ctx["archetypes"]), reverse=True)[:3]
        if ic and covs and covs[0][0] > 0:
            items = "; ".join(f"[{pid} {ctx['archetypes'][pid]['name']}](../../05-portfolio/project-archetypes.md#{pid.lower()}) ({round(100 * c)}%)"
                              for c, pid in covs if c > 0)
            out.append(f"- **Project archetypes that cover the most of its Must and Important skills** (Grade M): {items}. "
                       "One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) "
                       "computes the smallest sets that do.")
        out.append("- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).")
    else:
        out.append("- Case studies, client outcomes and referrals carry this track, not portfolio projects; see the [catalog profile](../role-catalog.md#profile-"
                   f"{rid}).")
    out += ["", "## How you are interviewed", ""]
    t = r["interview_track"]
    if t:
        pack = sl.gh_slug(f"{tracks[t]['name']} pack")
        out.append(f"- **Track: {tracks[t]['name']}.** It tests {tracks[t]['tests']}. Source: {tracks[t]['source']}.")
        out.append(f"- **Practise:** the [{tracks[t]['name'].lower()} prep pack](../../08-interviewing/prep-packs.md#{pack}), "
                   "plus the behavioural and coding packs.")
    else:
        out.append("- No interview-track evidence in the corpus for this role. Practise with the closest track's "
                   "[prep pack](../../08-interviewing/prep-packs.md) and the behavioural pack.")
    out += ["- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).", "", "## Résumé", ""]
    if orole:
        fh = variant["flavour_headlines"].get(orole["flavour"], variant["headline"])
        note = fh[1:-1]
        first = note.split()[0]
        note = note if (first.isupper() and len(first) > 1) else note[0].lower() + note[1:]
        head = f"headline: {note}" if fh.startswith("(") else f"headline pattern: \"{fh}\""
        out += [f"- **Variant:** {orole['flavour']} {variant['flavours'][orole['flavour']].split(':')[0]} ({variant['name']}); {head}. "
                "How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).",
                f"- **Keywords to mirror, only when true:** {orole.get('mirror') or '—'}",
                f"- **Leave out or reframe:** {orole.get('avoid') or '—'}",
                f"- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-{oid})."]
    else:
        out.append("- Independent and fractional work runs on case studies and referrals rather than portal résumés, so it has no variant.")
    specs = [s for s in stack["specialisations"] if rid in s["home"]]
    if specs:
        out += ["", "## Specialisations inside this role", ""]
        for s in specs:
            out.append(f"- **{s['name']}** ({sl.area_label(stack, s['where'])}): {s['catalog']}.")
        out.append("- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).")
    out += ["", "## Related roles", ""]
    names = {x["id"]: x["name"] for x in ctx["scores"]["roles"]}
    if oid and oid in an["ic"]:
        near = [(s, a if b == oid else b) for s, a, b in an["pairs"] if oid in (a, b)][:3]
        out.append("- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): "
                   + "; ".join(f"[{names[o]}]({o}.md) ({s:.2f})" for s, o in near) + ".")
    fam = [x for x in ctx["scores"]["roles"] if x["family"] == r["family"] and x["id"] != rid]
    if fam:
        out.append(f"- **Same family ({r['family']}):** " + ", ".join(f"[{x['name']}]({x['id']}.md)" for x in fam) + ".")
    out += ["", "## Go deeper", "",
            f"- [Catalog profile](../role-catalog.md#profile-{rid}): definition, demand, pay, who hires, entry routes, aliases and watch items.",
            (f"- [Role rankings](../role-rankings.md#{slugs['board']}): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#{slugs['appendix']})."
             if ic else f"- [Role rankings, leadership tracks](../role-rankings.md#{slugs['lead']})."),
            f"- [GenAI target roles](../genai-target-roles.md#{slugs['order']}): where this role sits in the GenAI target order and why.",
            f"- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-{rid if (orole and orole['variant'] != 'L' and oid == rid) else 'leadership'}): narrative skills, tools, interview and typical gaps."]
    out += [f"- [{label}](../../11-tracks/{f}): the track playbook for this role." for f, (label, ids) in ctx["playbooks"].items() if rid in ids]
    out += ["", "## Evidence and dates", "",
            f"- Pillar scores as of {ctx['scores']['as_of']}; skills ontology as of {onto['meta']['as_of']}; tool and credential statuses are due for re-verification by {onto['meta']['ttl']['tool_status_reverify_by']}.",
            f"- The demand scores rest on posting counts ({counted_on(ctx['scores'], r)}), which expire {POSTING_TTL_DAYS} days after they were counted "
            f"(EGP-1.0 class V1), so this page is due for re-verification by {review_by_for(ctx['scores'], r)}.",
            "- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).", "",
            "## Next steps", "",
            "- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)", ""]
    return "\n".join(out)


def index(ctx):
    base, lead, mc, _ = ranks(ctx)
    stack, onto = ctx["stack"], ctx["onto"]
    roles = ctx["scores"]["roles"]

    def tkey(r):
        o = onto["roles"].get(r["id"])
        if r["track"] == "ic":
            return (0, o["target"])
        return (1, lead[r["id"]]["rank"])
    as_of = max(ctx["scores"]["as_of"], onto["meta"]["as_of"], stack["as_of"])
    out = ["---", "id: roles.hubs", 'title: "Role Hubs: One Page per Role"', "content_type: index", "stage: 2", "status: published",
           f"last_verified: {as_of}", f"review_by: {ctx['review_by']}",
           f'summary: "Index of the {len(roles)} role hubs: one generated page per canonical role with its definition, footprint, graded scores, skills, proof, interview track and résumé pointers."',
           "generated_by: scripts/build_role_hubs.py", "---", "",
           "<!-- Generated by scripts/build_role_hubs.py from data/. Edit the data or the generator, not this page. -->", "",
           "# Role Hubs: One Page per Role", "",
           "> Every canonical role on one page: what it is, where the work sits, how it scores and on what evidence, who it suits, "
           "what it needs, how to prove it and how it is interviewed. Each hub links to the full evidence in the catalogs.", "",
           "## All roles, in GenAI target order", "",
           "| GenAI target | Role | Family | Main place | Status | CCI rank |", "|:---:|---|---|---|:---:|:---:|"]
    for r in sorted(roles, key=tkey):
        st = r["stack"]
        main = sl.area_label(stack, st["primary"]) if st["primary"] else stack["planes"][st["planes"][0]]["name"]
        tg = f"#{onto['roles'][r['id']]['target']}" if r["track"] == "ic" else f"Leadership #{lead[r['id']]['rank']}"
        rank = f"#{base[r['id']]['rank']}" if r["track"] == "ic" else f"Leadership #{lead[r['id']]['rank']}"
        out.append(f"| {tg} | [{r['name']}]({r['id']}.md) | {r['family']} | {main} | {r['status']} | {rank} |")
    out += ["", "Status: E established, V verified, W watch, A absorbed (see the [catalog's status classes](../role-catalog.md#12-status-classes-for-canonical-roles)). "
            f"Leadership and independent tracks are ranked separately (Leadership #1–#{ctx['n_lead']}). "
            "Codes L1–L6 elsewhere on the role map are work layers, not ranks.", "",
            "## How hubs are built", "",
            "- Generated by `scripts/build_role_hubs.py` from `data/role_scores.json`, `data/skills_ontology.json`, `data/project_archetypes.json` "
            "and `data/stack_model.json`, with ranks from `scripts/rank_roles.py`. Nothing on a hub is typed by hand.",
            "- Every score keeps its evidence grade and basis; computed values (CCI, coverage, similarity) are Grade M; work footprints are Grade D.", "",
            "## Next steps", "", "- [The role map](../role-map.md) · [Role catalog](../role-catalog.md) · [Start Here](../../README.md)", ""]
    return "\n".join(out)


def outputs():
    ctx = context()
    files = OrderedDict([(HUBS / "README.md", index(ctx))])
    for r in ctx["scores"]["roles"]:
        files[HUBS / f"{r['id']}.md"] = hub(ctx, r)
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    files = outputs()
    if args.update:
        HUBS.mkdir(parents=True, exist_ok=True)
        stale = [p for p in HUBS.glob("*.md") if p not in files]
        for p in stale:
            p.unlink()
        for p, text in files.items():
            p.write_text(text, encoding="utf-8")
        print(f"wrote {len(files)} hub files" + (f"; removed {len(stale)} stale" if stale else ""))
    elif args.check:
        stale = [str(p.relative_to(sl.ROOT)) for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        extra = [str(p.relative_to(sl.ROOT)) for p in HUBS.glob("*.md") if p not in files] if HUBS.exists() else []
        if stale or extra:
            print("out of date: " + ", ".join(stale + extra))
            sys.exit(1)
        print("up to date")
    else:
        for p in files:
            print(p.relative_to(sl.ROOT))


if __name__ == "__main__":
    main()
