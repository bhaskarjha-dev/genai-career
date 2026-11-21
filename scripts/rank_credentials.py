#!/usr/bin/env python3
"""Credential ranking and catalog generator: builds career/04-certifications/credential-catalog.md.

Implements Reduce Step R1 (decision D-026) over data/credentials.json:
  * Validates data/credentials.json against data/schemas/credentials.schema.json, checks every
    session line reference via common.ref_errors, checks score-triple ordering (lo <= mid <= hi),
    and confirms every credential ID in data/skills_ontology.json resolves.
  * Computes deterministic Monte Carlo value rankings (triangular draws across [lo, mid, hi]
    scores) for three channel lenses and eight role families, applying an explicit conservative
    prior UNMEASURED_HIRING_SIGNAL_PRIOR = (2.5, 4.0, 5.5) whenever hiring_signal is null so
    all credentials are evaluated on the full 1.0 weight vector and empirically measured
    credentials are never penalised relative to unmeasured peers (D-026 calibration, 2026-11-19).
  * Renders a cost- and hour-ordered collector's list (active, open-access exams) beside the
    stop-rule warning, followed by the full deduplicated census by issuer group.

Inputs (sources of truth):
  * data/credentials.json (+ data/schemas/credentials.schema.json)
  * data/skills_ontology.json (ID resolution check)

Usage:
    python3 -B scripts/rank_credentials.py            # print the rendered catalog
    python3 -B scripts/rank_credentials.py --update   # write career/04-certifications/credential-catalog.md
    python3 -B scripts/rank_credentials.py --check    # exit 1 if out of date or data are invalid
    python3 -B scripts/rank_credentials.py --json     # print computed rankings as JSON

Standard library only.
"""
import argparse
import datetime
import json
import math
import random
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import esc, ref_errors, schema_errors, session_line_counts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "credentials.json"
SCHEMA = ROOT / "data" / "schemas" / "credentials.schema.json"
ONTO = ROOT / "data" / "skills_ontology.json"
DOC = ROOT / "career" / "04-certifications" / "credential-catalog.md"

CRITERIA = ("hiring_signal", "channel_value", "rigour", "skill_alignment", "currency", "cost_efficiency")
TTL_DAYS = {"V0": 14, "V1": 30, "V2": 90, "V3": 180, "V4": 365}
MC_SEED = 20261119
MC_ITER = 4000
# Conservative prior for unmeasured (null) hiring_signal (D-026 calibration, 2026-11-19).
# Keeps hiring_signal: null in data/credentials.json (never inventing empirical measurements)
# while evaluating all credentials on the same 100% weight vector with wide ±1.5 uncertainty
# so empirically measured credentials are never penalised relative to zero-posting unmeasured peers.
UNMEASURED_HIRING_SIGNAL_PRIOR = (2.5, 4.0, 5.5)

GROUP_LABELS = OrderedDict([
    ("hyperscalers", "Hyperscalers (AWS, Google Cloud, Microsoft — provisional pending T0-28)"),
    ("frontier-labs", "Frontier Labs & AI-Native Vendors (T0-29)"),
    ("data-enterprise", "Data & Enterprise AI Platforms (T0-31)"),
    ("gpu-infra-oss", "GPU, Infrastructure & Open-Source (T0-32)"),
    ("dev-tools-agentic", "Developer Tools & Agentic Suites (provisional pending T0-33)"),
    ("governance-security-audit", "Governance, Security, Privacy & Audit (T0-34)"),
    ("courses-universities-india", "Courses, Universities, Private Bodies & Recognition (T0-30)"),
])

ACCESS_LABELS = {
    "open": "Open",
    "partner-gated": "Partner-gated",
    "employer-gated": "Employer-gated",
    "invite-only": "Invite-only",
    "nomination-only": "Nomination-only",
}

KIND_LABELS = {
    "proctored-exam": "Proctored exam",
    "hands-on-exam": "Hands-on exam",
    "hybrid-exam": "Hybrid exam",
    "assessed-cert": "Assessed cert",
    "completion-cert": "Completion cert",
    "accreditation": "Accreditation",
    "recognition": "Recognition",
    "graduate-cert": "Graduate cert",
}


def load_inputs():
    data = json.loads(DATA.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    onto = json.loads(ONTO.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    return data, schema, onto


def validate(data, schema, onto):
    errs = [f"credentials.json {e[2:]}" for e in schema_errors(data, schema, schema)]
    if errs:
        return errs

    # Check weight sums
    base_sum = sum(data["criteria"][k]["weight"] for k in CRITERIA)
    if abs(base_sum - 1.0) > 1e-6:
        errs.append(f"credentials.json: criteria weights sum to {base_sum:.4f}, expected 1.0")
    for lens in data["channel_lenses"]:
        lsum = sum(lens["weights"][k] for k in CRITERIA)
        if abs(lsum - 1.0) > 1e-6:
            errs.append(f"credentials.json: lens {lens['id']} weights sum to {lsum:.4f}, expected 1.0")

    seen = set()
    lines = session_line_counts()
    for cred in data["credentials"]:
        cid = cred["id"]
        if cid in seen:
            errs.append(f"credentials.json: duplicate id {cid}")
        seen.add(cid)
        try:
            datetime.date.fromisoformat(cred["as_of"])
        except ValueError:
            errs.append(f"credentials.json: {cid} as_of {cred['as_of']!r} is not an ISO date")
        for k in CRITERIA:
            triple = cred["scores"][k]
            if triple is not None and not (triple[0] <= triple[1] <= triple[2]):
                errs.append(f"credentials.json: {cid}.scores.{k} not ordered lo<=mid<=hi: {triple}")
        ph = cred["prep_hours"]
        if ph is not None and ph[0] > ph[1]:
            errs.append(f"credentials.json: {cid}.prep_hours not ordered lo<=hi: {ph}")
        errs += ref_errors(cred["source"], lines, f"credentials.json: {cid} source")

    # Every credential ID in data/skills_ontology.json must resolve in data/credentials.json
    for oid in onto.get("credentials", {}):
        if oid not in seen:
            errs.append(f"credentials.json: missing skills_ontology.json credential id {oid!r}")
    return errs


def effective_triple(cred, criterion):
    """Return [lo, mid, hi] for criterion, using UNMEASURED_HIRING_SIGNAL_PRIOR for null hiring_signal."""
    val = cred["scores"][criterion]
    if val is None and criterion == "hiring_signal":
        return UNMEASURED_HIRING_SIGNAL_PRIOR
    return val


def point_score(cred, weights):
    """Weighted mid-point score on 0–10 scale using the full weight vector and unmeasured hiring_signal prior."""
    total = 0.0
    wsum = 0.0
    for k in CRITERIA:
        val = effective_triple(cred, k)
        if val is None:
            continue
        w = weights[k]
        total += w * val[1]
        wsum += w
    return (total / wsum) if wsum > 0 else 0.0


def rank_subset(creds, weights, seed, n_iter=MC_ITER):
    """Deterministic Monte Carlo ranking over triangular [lo, mid, hi] draws."""
    if not creds:
        return []
    rng = random.Random(seed)
    n = len(creds)
    # Precompute active criteria and weights per credential (null hiring_signal uses conservative prior)
    specs = []
    for c in creds:
        active = []
        wsum = 0.0
        for k in CRITERIA:
            triple = effective_triple(c, k)
            if triple is not None and weights[k] > 0:
                active.append((triple[0], triple[1], triple[2], weights[k]))
                wsum += weights[k]
        norm = [(lo, mid, hi, w / wsum) for (lo, mid, hi, w) in active] if wsum > 0 else []
        specs.append(norm)

    rank_hist = [[] for _ in range(n)]
    score_sum = [0.0] * n
    score_samples = [[] for _ in range(n)]

    for _ in range(n_iter):
        draws = []
        for idx, norm in enumerate(specs):
            s = 0.0
            for lo, mid, hi, nw in norm:
                val = lo if lo == hi else rng.triangular(lo, hi, mid)
                s += nw * val
            draws.append((s, idx))
            score_sum[idx] += s
            score_samples[idx].append(s)
        draws.sort(key=lambda x: (-x[0], creds[x[1]]["id"]))
        for r_pos, (_, idx) in enumerate(draws, 1):
            rank_hist[idx].append(r_pos)

    rows = []
    p10_i = max(0, int(0.10 * n_iter) - 1)
    p90_i = min(n_iter - 1, int(0.90 * n_iter) - 1)
    for idx, c in enumerate(creds):
        rh = sorted(rank_hist[idx])
        ss = sorted(score_samples[idx])
        rows.append({
            "cred": c,
            "id": c["id"],
            "point": round(point_score(c, weights), 2),
            "mc_mean": round(score_sum[idx] / n_iter, 2),
            "score_p10": round(ss[p10_i], 2),
            "score_p90": round(ss[p90_i], 2),
            "rank_p10": rh[p10_i],
            "rank_p90": rh[p90_i],
            "measured_signal": c["scores"]["hiring_signal"] is not None,
        })
    rows.sort(key=lambda r: (-r["point"], -r["mc_mean"], r["id"]))
    for pos, r in enumerate(rows, 1):
        r["rank"] = pos
    return rows


def filter_for_lens(creds, lens):
    out = []
    for c in creds:
        if c["state"] != "active":
            continue
        if lens["access_filter"] is not None and c["access"] not in lens["access_filter"]:
            continue
        if lens["group_filter"] is not None and c["group"] not in lens["group_filter"]:
            continue
        if lens["kind_filter"] is not None and c["kind"] not in lens["kind_filter"]:
            continue
        if lens["channel_filter"] is not None and not any(ch in lens["channel_filter"] for ch in c["channels"]):
            continue
        out.append(c)
    return out


def compute_all(data):
    creds = data["credentials"]
    base_weights = {k: data["criteria"][k]["weight"] for k in CRITERIA}

    lenses_out = OrderedDict()
    for idx, lens in enumerate(data["channel_lenses"]):
        sub = filter_for_lens(creds, lens)
        lenses_out[lens["id"]] = {
            "lens": lens,
            "rows": rank_subset(sub, lens["weights"], MC_SEED + idx * 101),
        }

    # Role-family rankings over active exams/assessed certs (excludes completion-only & recognition)
    exam_kinds = {"proctored-exam", "hands-on-exam", "hybrid-exam", "assessed-cert", "accreditation"}
    families_out = OrderedDict()
    for idx, fam in enumerate(data["role_families"]):
        fid = fam["id"]
        sub = [c for c in creds if c["state"] == "active" and c["kind"] in exam_kinds and fid in c["families"]]
        watch = [c for c in creds if c["state"] in ("beta", "announced") and c["kind"] in exam_kinds and fid in c["families"]]
        families_out[fid] = {
            "family": fam,
            "rows": rank_subset(sub, base_weights, MC_SEED + 500 + idx * 37),
            "watch": sorted(watch, key=lambda x: x["name"]),
        }

    # Collector's list: active, open-access proctored/hands-on/hybrid exams with published fee_usd and prep_hours
    collector_pool = [
        c for c in creds
        if c["state"] == "active"
        and c["access"] == "open"
        and c["kind"] in ("proctored-exam", "hands-on-exam", "hybrid-exam")
        and c["fee_usd"] is not None
        and c["prep_hours"] is not None
        and c["group"] != "courses-universities-india"
    ]
    ranked_pool = rank_subset(collector_pool, base_weights, MC_SEED + 999)
    collector_rows = []
    for r in ranked_pool:
        c = r["cred"]
        fee = float(c["fee_usd"])
        h_mid = 0.5 * (c["prep_hours"][0] + c["prep_hours"][1])
        # Effort index combines prep hours and fee scaled to equivalent hours (USD 25 ~= 1h reference)
        effort = max(8.0, h_mid + fee / 25.0)
        efficiency = r["point"] / math.log2(effort + 2.0)
        collector_rows.append({
            "cred": c,
            "point": r["point"],
            "fee_usd": fee,
            "hours_mid": round(h_mid, 1),
            "efficiency": round(efficiency, 3),
        })
    collector_rows.sort(key=lambda x: (-x["efficiency"], x["fee_usd"], x["hours_mid"], x["cred"]["id"]))
    return lenses_out, families_out, collector_rows


def fmt_fee(c):
    if c["fee_local"] and c["fee_usd"] is not None and c["fee_usd"] > 0:
        return f"{esc(c['fee_local'])} (~${int(c['fee_usd']):,})"
    if c["fee_local"]:
        return esc(c["fee_local"])
    if c["fee_usd"] is None:
        return "Unpublished"
    if c["fee_usd"] == 0:
        return "Free"
    return f"${int(c['fee_usd']):,}"


def fmt_val(c):
    v = c["validity_months"]
    if v is None:
        return "No expiry / n.s."
    return f"{v} mo"


def fmt_hours(c):
    ph = c["prep_hours"]
    if ph is None:
        return "n.s."
    if ph[0] == ph[1]:
        return f"{int(ph[0])} h"
    return f"{int(ph[0])}–{int(ph[1])} h"


def fmt_name(c):
    label = esc(c["name"])
    if c["exam_code"] and c["exam_code"] not in c["name"]:
        label = f"{label} (`{esc(c['exam_code'])}`)"
    tag = " *(provisional)*" if c["provisional_pending_rp2"] else ""
    coi = " *(COI)*" if c["coi"] else ""
    return f"**{label}**{tag}{coi}"


def compute_review_by(data):
    dates = []
    for c in data["credentials"]:
        base = datetime.date.fromisoformat(c["as_of"])
        days = TTL_DAYS.get(c["ttl"], 90)
        dates.append(base + datetime.timedelta(days=days))
    return min(dates).isoformat()


def render(data, lenses_out, families_out, collector_rows):
    creds = data["credentials"]
    review_by = compute_review_by(data)
    sources = sorted({m for c in creds for m in re.findall(r"T[0-3]-\d\d", c["source"])})
    n_total = len(creds)
    n_active = sum(1 for c in creds if c["state"] == "active")
    n_prov = sum(1 for c in creds if c["provisional_pending_rp2"])
    n_measured = sum(1 for c in creds if c["scores"]["hiring_signal"] is not None)
    n_unmeasured = n_total - n_measured

    out = [
        "---",
        "id: certifications.catalog",
        'title: "GenAI Certification Catalog and Value Order"',
        "content_type: reference",
        "stage: 4",
        "status: published",
        f"last_verified: {data['as_of']}",
        f"review_by: {review_by}",
        (
            f'summary: "{n_total} vetted GenAI, ML, infrastructure, enterprise-platform and governance credentials '
            f'({n_active} active), ranked across three channel lenses, eight role families and a cost/hour collector '
            'list with Monte Carlo intervals."'
        ),
        f"sources: [{', '.join(sources)}]",
        "tags: [certifications, credentials, catalog, rankings, roi]",
        "generated_by: scripts/rank_credentials.py",
        "---",
        "",
        "<!-- Generated by scripts/rank_credentials.py from data/credentials.json. Edit the data, not this page. -->",
        "",
        "# GenAI Certification Catalog and Value Order",
        "",
        (
            f"> {n_total} deduplicated credentials ({n_active} active, "
            f"{sum(1 for c in creds if c['state'] == 'beta')} beta, "
            f"{sum(1 for c in creds if c['state'] == 'announced')} announced, "
            f"{sum(1 for c in creds if c['state'] == 'retired')} retired) reconciled across "
            "T0-29, T0-30, T0-31, T0-32, T0-34, T0-58, T3-01, T3-02 and T0-11."
        ),
        "",
        "> [!IMPORTANT]",
        (
            "> **Partial Reduce Step R1 release (as of "
            f"{data['as_of']}):** Research pipeline 2 sessions **T0-28** (AWS, Google Cloud, Microsoft hyperscalers) "
            "and **T0-33** (developer tools, agentic suites and GitHub) are deferred past **2026-12-05**. "
            f"The **{n_prov} entries** in those two groups are tagged *(provisional)* using T0-11, T3-01 and T3-02 "
            "and will be refreshed once T0-28 and T0-33 complete."
        ),
        "",
        "## How the value order works",
        "",
        (
            "Every credential in `data/credentials.json` is scored on six criteria as `[lo, mid, hi]` intervals "
            "(0–10) and ranked via deterministic Monte Carlo simulation "
            f"({MC_ITER:,} triangular draws, seed `{MC_SEED}`) [M · decision D-026]. "
            "Read rank intervals (`P10–P90`) rather than point ranks: overlapping intervals mean two credentials are "
            "indistinguishable given current evidence."
        ),
        "",
        "| Criterion | Base weight | Meaning |",
        "|---|:---:|---|",
    ]
    for k in CRITERIA:
        cdef = data["criteria"][k]
        out.append(f"| `{k}` | {int(round(cdef['weight'] * 100))}% | {esc(cdef['description'])} |")

    out += [
        "",
        (
            f"- **Conservative unmeasured hiring-signal prior (`[{UNMEASURED_HIRING_SIGNAL_PRIOR[0]:.1f}, "
            f"{UNMEASURED_HIRING_SIGNAL_PRIOR[1]:.1f}, {UNMEASURED_HIRING_SIGNAL_PRIOR[2]:.1f}]`):** Only "
            f"**{n_measured} of {n_total}** credentials have a systematic large-sample posting measurement "
            "(seven governance/security credentials from Axial Search's n = 1,997 US AI-governance dataset "
            "[C · T0-34 L51] corroborated with GRC Careers n = 76 [B COI · T0-34 L52], plus CKA and CKAD from "
            "LinuxCareers' n = 1,675 Linux posting audit [B · T0-32 L395]). For the remaining "
            f"**{n_unmeasured} credentials**, `hiring_signal` remains `null` in `data/credentials.json` and the "
            f"ranking model draws from the conservative triangular prior `[{UNMEASURED_HIRING_SIGNAL_PRIOR[0]:.1f}, "
            f"{UNMEASURED_HIRING_SIGNAL_PRIOR[1]:.1f}, {UNMEASURED_HIRING_SIGNAL_PRIOR[2]:.1f}]` on the full 100% "
            "weight vector (D-026 calibration, 2026-11-19). Keeping the full weight vector avoids the anti-measurement "
            "bias of five-criterion re-normalisation (which previously imputed each unmeasured credential's five-criterion "
            "mean as a phantom hiring signal and penalised empirically measured workhorses such as CKA, CISA and CISM) "
            "while widening `P10–P90` intervals to show epistemic uncertainty."
        ),
        (
            "- **Decision rule first:** Rankings show relative quality *conditional on deciding to certify*. "
            "Before paying for any exam, apply the three-condition filter and stop-loss in "
            "[credential-roi.md](credential-roi.md)."
        ),
        (
            "- **Conflict-of-interest (COI) tags (uniform EGP-1.0 rule):** Entries tagged *(COI)* either carry "
            "authoring-model issuer COI (Anthropic/Claude in T0-29 and Claude-branded Udacity in T0-30; Anthropic exam "
            "logistics and US Department of War FASCSA litigation at T0-29 L83 were independently live-verified on "
            "2026-11-19) or rely on commercial seller/reseller/owner-survey value or pricing claims (unverified private "
            "bodies, commercial MOOC/ed-tech/EU AI Act course sellers, self-certifying audit schemes, and IAPP AIGP's "
            "owner salary survey / GRC Careers board). Standard factual exam logistics from primary issuer pages are "
            "not tagged COI individually; all issuers have commercial stakes in value claims."
        ),
        "",
        "## Channel lenses",
        "",
        (
            "Value depends heavily on employer channel. A credential that unlocks partner tiers in an SI practice "
            "may be inaccessible or ignored at a product startup."
        ),
        "",
    ]

    # Render each of the 3 channel lenses
    lens_limits = {"product-frontier": 20, "services-partners-gcc": 25, "governance-assurance": 25}
    for lid, payload in lenses_out.items():
        lens = payload["lens"]
        rows = payload["rows"]
        limit = lens_limits.get(lid, 20)
        w = lens["weights"]
        w_str = ", ".join(f"`{k}` {int(round(w[k] * 100))}%" for k in CRITERIA)
        out += [
            f"### {lens['name']}",
            "",
            f"{lens['description']} Weights: {w_str} (conservative `[{UNMEASURED_HIRING_SIGNAL_PRIOR[0]:.1f}, "
            f"{UNMEASURED_HIRING_SIGNAL_PRIOR[1]:.1f}, {UNMEASURED_HIRING_SIGNAL_PRIOR[2]:.1f}]` prior where "
            "`hiring_signal` is unmeasured).",
            "",
            "| Rank | P10–P90 | Score | Credential | Issuer | Access | Fee | Validity | Signal measured? | Grade & source |",
            "|:---:|:---:|:---:|---|---|---|---|---|:---:|---|",
        ]
        for r in rows[:limit]:
            c = r["cred"]
            sig = "Yes" if r["measured_signal"] else "Prior (2.5–5.5)"
            out.append(
                f"| {r['rank']} | {r['rank_p10']}–{r['rank_p90']} | {r['point']:.2f} | "
                f"{fmt_name(c)} | {esc(c['issuer'])} | {ACCESS_LABELS[c['access']]} | "
                f"{fmt_fee(c)} | {fmt_val(c)} | {sig} | {c['grade']} · {esc(c['source'])} |"
            )
        if len(rows) > limit:
            out.append("")
            out.append(f"*Showing top {limit} of {len(rows)} eligible active credentials; all {n_total} entries appear in the full census below.*")
        out.append("")

    # Role-family views
    out += [
        "## Role-family views",
        "",
        (
            "Top active exams and assessed credentials per role family using the base R1 weights (conservative "
            f"`[{UNMEASURED_HIRING_SIGNAL_PRIOR[0]:.1f}, {UNMEASURED_HIRING_SIGNAL_PRIOR[1]:.1f}, "
            f"{UNMEASURED_HIRING_SIGNAL_PRIOR[2]:.1f}]` prior where `hiring_signal` is unmeasured). Completion-only "
            "MOOCs and recognition programmes are excluded from exam rankings and listed in the full census below."
        ),
        "",
    ]
    for fid, payload in families_out.items():
        fam = payload["family"]
        rows = payload["rows"]
        watch = payload["watch"]
        out += [
            f"### {fam['name']}",
            "",
            "| Rank | P10–P90 | Score | Credential | Access | Kind | Fee | Validity | Grade & source |",
            "|:---:|:---:|:---:|---|---|---|---|---|---|",
        ]
        for r in rows[:10]:
            c = r["cred"]
            out.append(
                f"| {r['rank']} | {r['rank_p10']}–{r['rank_p90']} | {r['point']:.2f} | "
                f"{fmt_name(c)} | {ACCESS_LABELS[c['access']]} | {KIND_LABELS[c['kind']]} | "
                f"{fmt_fee(c)} | {fmt_val(c)} | {c['grade']} · {esc(c['source'])} |"
            )
        if watch:
            w_list = "; ".join(f"{esc(x['name'])} ({x['state']})" for x in watch[:6])
            out += ["", f"- **Beta / announced watch:** {w_list}."]
        out.append("")

    # Cost- and hour-ordered collector's list
    out += [
        "## Cost- and hour-ordered collector's list",
        "",
        "> [!WARNING]",
        (
            "> **Stop-rule warning (T0-11, T3-01):** Most practitioners should earn **zero or one** certification, "
            "not work down a collector's list. Across 24 credentials in T3-01, knowledge overlap saves ~45% of "
            "standalone study hours while clever ordering saves only ~4% [M · T3-01 L133–L135]; past one "
            "employer-matched credential, additional badges displace inspectable portfolio work and add annual "
            "renewal debt (6–24 month cycles). Use this table only to compare marginal cash and time cost among "
            "active, **open-access** proctored/hands-on exams."
        ),
        "",
        "| Order | Credential | Issuer | Kind | Score | Fee (USD) | Prep (mid) | Cumul. fee | Cumul. hours | Validity |",
        "|:---:|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|",
    ]
    cum_fee = 0.0
    cum_h = 0.0
    for pos, item in enumerate(collector_rows[:20], 1):
        c = item["cred"]
        cum_fee += item["fee_usd"]
        cum_h += item["hours_mid"]
        fee_s = "Free" if item["fee_usd"] == 0 else f"${int(item['fee_usd']):,}"
        out.append(
            f"| {pos} | {fmt_name(c)} | {esc(c['issuer'])} | {KIND_LABELS[c['kind']]} | "
            f"{item['point']:.2f} | {fee_s} | {item['hours_mid']:.0f} h | "
            f"${int(round(cum_fee)):,} | {int(round(cum_h)):,} h | {fmt_val(c)} |"
        )
    out += [
        "",
        (
            "*Note: Prep hours are midpoints of published or estimated ranges (`data/credentials.json`) before "
            "cross-exam knowledge overlap; overlapping two exams in the same cluster (for example AWS + Google "
            "agentic, or Databricks GenAI + Context Engineer at ~35–42% overlap) reduces marginal hours "
            "[M · T3-01 L121, L133].*"
        ),
        "",
        "## Full deduplicated census by issuer group",
        "",
        (
            f"All **{n_total}** credentials in `data/credentials.json`, including retired exams, beta/announced "
            "releases, completion certificates, unverified private bodies and recognition programmes."
        ),
        "",
    ]

    for gid, glabel in GROUP_LABELS.items():
        gcreds = [c for c in creds if c["group"] == gid]
        if not gcreds:
            continue
        out += [
            f"### {glabel}",
            "",
            "| Credential | Issuer | State | Access | Kind | Fee | Prep | Validity | Grade & source | Notes |",
            "|---|---|---|---|---|---|---|---|---|---|",
        ]
        for c in gcreds:
            link_name = f"[{esc(c['name'])}]({c['url']})" if c.get("url") else esc(c["name"])
            if c["exam_code"] and c["exam_code"] not in c["name"]:
                link_name = f"{link_name} (`{esc(c['exam_code'])}`)"
            if c["provisional_pending_rp2"]:
                link_name += " *(prov.)*"
            out.append(
                f"| {link_name} | {esc(c['issuer'])} | {c['state']} | {ACCESS_LABELS[c['access']]} | "
                f"{KIND_LABELS[c['kind']]} | {fmt_fee(c)} | {fmt_hours(c)} | {fmt_val(c)} | "
                f"{c['grade']} · {esc(c['source'])} | {esc(c['note'])} |"
            )
        out.append("")

    out += [
        "## Evidence and limits",
        "",
        (
            f"- **Provisional hyperscaler and dev-tool rows ({n_prov} entries):** AWS, Google Cloud, Microsoft "
            "and GitHub records carry `provisional_pending_rp2: true` and draw on T0-11, T3-01 and T3-02 until "
            "RP2 sessions T0-28 and T0-33 run after 2026-12-05."
        ),
        (
            f"- **Sparse hiring-signal denominators:** Only {n_measured} of {n_total} credentials have systematic "
            "large-sample posting rates (Axial Search US AI-governance n = 1,997, unstable snapshots across 2026 "
            "[C · T0-34 L51, L61], corroborated with GRC Careers n = 76 [B COI · T0-34 L52]; LinuxCareers n = 1,675 "
            "Linux-focused postings [B · T0-32 L395]). Every other credential keeps `hiring_signal: null` in "
            f"`data/credentials.json` and uses the conservative `[{UNMEASURED_HIRING_SIGNAL_PRIOR[0]:.1f}, "
            f"{UNMEASURED_HIRING_SIGNAL_PRIOR[1]:.1f}, {UNMEASURED_HIRING_SIGNAL_PRIOR[2]:.1f}]` Monte Carlo prior in "
            "ranking; convenience-sample counts (such as Salesforce 7/17 US, 12/17 India or Palantir 8/14 US in T0-31) "
            "are documented in notes rather than converted into synthetic hiring-signal scores."
        ),
        (
            "- **NVIDIA `NCP-GENL` and `NCP-AAI` registration conflict:** Recorded as `announced` (V0) following "
            "T0-32 K2 (exam pages displayed `(Coming soon)` beside Register on 2026-10-30 while the hub listed "
            "USD 200 [A · T0-32 L74, L631, L841–L842]) and a 2026-11-19 live check confirming mixed portal status "
            "alongside rolling Certiverse scheduling. Verify live Certiverse availability before paying for prep."
        ),
        (
            "- **Anthropic COI and US defence exclusion (V0):** T0-29 carried model-issuer COI on Anthropic's "
            "four Claude exams; partner gating, fees, December 2026 refresh dates and the exclusion of CCAO-F "
            "from partner tiers were independently live-verified on 2026-11-19, alongside the split US litigation "
            "over the Department of War FASCSA supply-chain designation (D.C. Circuit 2–1 panel ruling 2026-09-25, "
            "rehearing en banc petition filed 2026-10-13 [A · T0-29 L83])."
        ),
        (
            "- **Unverified private credential bodies and Indian ed-tech programmes:** ARTiBA, GSDC (unverified "
            "ISO 17024 PCB-168 claim), Blockchain Council and IABAC had zero verified accreditation and 0/29 posting "
            "hits in T0-30 [A · T0-30 L71, L74]. Indian institute CEP/ed-tech bundles (₹1.3–2.3L) issue "
            "non-refundable certificates of participation with 0/14 India posting hits [A · T0-30 L71, L78]."
        ),
        (
            f"- **Freshness:** Data as of {data['as_of']}; earliest expiry is {review_by} (driven by V0 items "
            "including beta exams, NVIDIA registration status and pending US litigation)."
        ),
        "",
        "## Next steps",
        "",
        "- [Credential ROI guide](credential-roi.md): the three-condition decision rule, stop-loss, sequencing rules and per-issuer deep dives.",
        "- [Credentials by role](credentials-by-role.md): which credentials map onto each individual-contributor role.",
        "- [Proof-of-work standards](../05-portfolio/proof-of-work-standards.md): when to build inspectable artifacts instead of studying for an exam.",
        "- [Learning roadmaps](../03-skills-and-tech/learning-roadmaps.md): structured learning paths without ₹2 lakh certificate traps.",
        "- [Governance careers](../11-tracks/governance-careers.md): domain-first certification pathways for governance, privacy and audit.",
        "- [Certifications stage overview](README.md)",
        "",
    ]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    g.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data, schema, onto = load_inputs()
    errs = validate(data, schema, onto)
    if errs:
        raise SystemExit("credentials data are invalid:\n  " + "\n  ".join(errs[:30]))

    lenses_out, families_out, collector_rows = compute_all(data)
    if args.json:
        payload = {
            "as_of": data["as_of"],
            "review_by": compute_review_by(data),
            "lenses": {
                lid: [
                    {k: v for k, v in r.items() if k != "cred"}
                    for r in p["rows"]
                ]
                for lid, p in lenses_out.items()
            },
            "role_families": {
                fid: [
                    {k: v for k, v in r.items() if k != "cred"}
                    for r in p["rows"]
                ]
                for fid, p in families_out.items()
            },
            "collector_order": [
                {
                    "id": item["cred"]["id"],
                    "point": item["point"],
                    "fee_usd": item["fee_usd"],
                    "hours_mid": item["hours_mid"],
                    "efficiency": item["efficiency"],
                }
                for item in collector_rows
            ],
        }
        print(json.dumps(payload, indent=2))
        return

    text = render(data, lenses_out, families_out, collector_rows)
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
