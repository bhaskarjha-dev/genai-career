#!/usr/bin/env python3
"""Country and city ranking engine for GenAI careers (D-025).

Reads data/countries.json, validates it against data/schemas/countries.schema.json
and research-session line counts, runs deterministic triangular Monte Carlo
sampling over each country's [lo, mid, hi] pillar intervals across six lenses,
and generates career/11-tracks/country-rankings.md in full.

Usage:
    python3 -B scripts/rank_countries.py                # print generated Markdown
    python3 -B scripts/rank_countries.py --update       # rewrite career/11-tracks/country-rankings.md
    python3 -B scripts/rank_countries.py --check        # exit 1 if out of date or invalid
    python3 -B scripts/rank_countries.py --json out.json # write machine-readable rankings

Scores use 0-10 anchored pillar scales; composite = sum(weight * score * 10),
so a country scoring 10 on every active pillar reaches 100. Standard library only.
"""
import argparse
import json
import random
import statistics
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    RELATIVE_TIME,
    ROOT,
    esc,
    prose,
    ref_errors,
    schema_errors,
    session_line_counts,
)

DEFAULT_DATA = ROOT / "data" / "countries.json"
DEFAULT_SCHEMA = ROOT / "data" / "schemas" / "countries.schema.json"
DEFAULT_DOC = ROOT / "career" / "11-tracks" / "country-rankings.md"

PILLARS = [
    "demand",
    "pay_ppp",
    "net_pay",
    "access_india",
    "access_non_eu",
    "remote_reach",
    "ecosystem",
    "stability",
]
MC_ITER = 20000
MC_SEED = 20261119


def half_up(x, places):
    q = Decimal("1") if places == 0 else Decimal("0." + "0" * (places - 1) + "1")
    return Decimal(str(round(x, 6))).quantize(q, rounding=ROUND_HALF_UP)


def r1(x):
    return str(half_up(x, 1))


def r0(x):
    return str(half_up(x, 0))


def g(x):
    return "%g" % x


def fmt_usd_k(val):
    if val is None:
        return "—"
    return f"${r1(val)}k"


def fmt_usd_mo(val):
    if val is None:
        return "—"
    return f"${val:,}/mo"


def validate(data, schema):
    errs = schema_errors(data, schema, schema)
    counts = session_line_counts()

    errs += ref_errors(data.get("fx_note", ""), counts, "fx_note")
    errs += ref_errors(data.get("description", ""), counts, "description")
    errs += ref_errors(data.get("scoring_method", ""), counts, "scoring_method")

    seen_lenses = set()
    for lens in data.get("lenses", []):
        lid = lens.get("id", "?")
        if lid in seen_lenses:
            errs.append(f"duplicate lens id {lid!r}")
        seen_lenses.add(lid)
        wsum = sum(lens.get("weights", {}).values())
        if abs(wsum - 1.0) > 1e-6:
            errs.append(f"lens {lid!r}: weights sum to {wsum:.6f}, expected 1.0")

    seen_ids, seen_iso = set(), set()
    for c in data.get("countries", []):
        cid = c.get("id", "?")
        iso = c.get("iso2", "?")
        if cid in seen_ids:
            errs.append(f"duplicate country id {cid!r}")
        seen_ids.add(cid)
        if iso in seen_iso:
            errs.append(f"duplicate country iso2 {iso!r}")
        seen_iso.add(iso)

        tr = c.get("incoming_tax_regime", {})
        errs += ref_errors(tr.get("source", ""), counts, f"{cid}.incoming_tax_regime.source")
        errs += ref_errors(tr.get("summary", ""), counts, f"{cid}.incoming_tax_regime.summary")

        for city in c.get("cities", []):
            cname = city.get("name", "?")
            errs += ref_errors(city.get("source", ""), counts, f"{cid}.cities[{cname}].source")
            errs += ref_errors(city.get("basis_note", ""), counts, f"{cid}.cities[{cname}].basis_note")

        for pname in PILLARS:
            ps = c.get("pillars", {}).get(pname)
            if not ps:
                continue
            lo, mid, hi = ps["range"]
            if not (0 <= lo <= mid <= hi <= 10):
                errs.append(f"{cid}.pillars.{pname}: range [{lo}, {mid}, {hi}] violates 0 <= lo <= mid <= hi <= 10")
            errs += ref_errors(ps.get("basis", ""), counts, f"{cid}.pillars.{pname}.basis")

    return errs


def score_point(country, weights):
    return sum(weights[p] * country["pillars"][p]["range"][1] * 10.0 for p in PILLARS)


def run_monte_carlo(data, n_iter=MC_ITER, seed=MC_SEED):
    """Draw triangular samples once per (country, pillar), then evaluate all lenses."""
    countries = data["countries"]
    lenses = data["lenses"]
    n_c = len(countries)
    rng = random.Random(seed)

    # Pre-extract (lo, mid, hi) tuples for fast inner loop
    ranges = [
        [tuple(c["pillars"][p]["range"]) for p in PILLARS]
        for c in countries
    ]
    lens_weights = [
        [lens["weights"][p] * 10.0 for p in PILLARS]
        for lens in lenses
    ]

    # Collect per-lens rank arrays and score sums
    rank_samples = [[[] for _ in range(n_c)] for _ in lenses]
    score_sums = [[0.0] * n_c for _ in lenses]
    top5_counts = [[0] * n_c for _ in lenses]

    for _ in range(n_iter):
        draws = [
            [
                mid if lo == hi else rng.triangular(lo, hi, mid)
                for (lo, mid, hi) in c_ranges
            ]
            for c_ranges in ranges
        ]
        for li, wvec in enumerate(lens_weights):
            scores = [
                sum(wvec[pi] * draws[ci][pi] for pi in range(len(PILLARS)))
                for ci in range(n_c)
            ]
            # Sort indices descending by score, deterministic tie-break by id
            order = sorted(range(n_c), key=lambda ci: (-scores[ci], countries[ci]["id"]))
            for rank_pos, ci in enumerate(order, 1):
                rank_samples[li][ci].append(rank_pos)
                score_sums[li][ci] += scores[ci]
                if rank_pos <= 5:
                    top5_counts[li][ci] += 1

    results = {}
    p10_idx = int(0.10 * (n_iter - 1))
    p90_idx = int(0.90 * (n_iter - 1))

    for li, lens in enumerate(lenses):
        rows = []
        for ci, c in enumerate(countries):
            rs = sorted(rank_samples[li][ci])
            pt = score_point(c, lens["weights"])
            mc_mean = score_sums[li][ci] / n_iter
            med_rank = statistics.median(rs)
            p10 = rs[p10_idx]
            p90 = rs[p90_idx]
            p_top5 = 100.0 * top5_counts[li][ci] / n_iter
            rows.append({
                "id": c["id"],
                "iso2": c["iso2"],
                "name": c["name"],
                "region": c["region"],
                "point_score": round(pt, 3),
                "mc_mean_score": round(mc_mean, 3),
                "median_rank": med_rank,
                "p10_rank": p10,
                "p90_rank": p90,
                "p_top5": round(p_top5, 1),
            })
        # Deterministic ordering: MC mean score desc, point score desc, median rank asc, id asc
        rows.sort(key=lambda r: (-r["mc_mean_score"], -r["point_score"], r["median_rank"], r["id"]))
        for idx, row in enumerate(rows, 1):
            row["rank"] = idx
        results[lens["id"]] = rows

    return results


def render_markdown(data, results):
    countries = data["countries"]
    by_id = {c["id"]: c for c in countries}
    lenses = data["lenses"]
    n_c = len(countries)
    n_cities = sum(len(c["cities"]) for c in countries)

    lines = [
        "---",
        "id: tracks.country-rankings",
        "title: GenAI Country and City Rankings",
        "content_type: reference",
        "stage: 11",
        "status: published",
        f"last_verified: {data['as_of']}",
        f"review_by: {data['review_by']}",
        "sources: [T0-35, T0-36, T0-43]",
        "roles: []",
        "geos: [global, india, us, eu, uk, sg, uae]",
        "tags: [geography, relocation, country-rankings, cities, remote]",
        "generated_by: scripts/rank_countries.py",
        f'summary: "Monte Carlo rankings of {n_c} GenAI destination countries and {n_cities} city snapshots across six decision lenses, generated from data/countries.json (T0-35, T0-36, T0-43)."',
        "---",
        "",
        "# GenAI Country and City Rankings",
        "",
        f"Evidence-graded country and city comparisons across {n_c} jurisdictions and {n_cities} cities from `T0-35` (Americas, Europe and Israel), `T0-36` (Gulf, India and Asia-Pacific) and `T0-43` (cross-border remote hiring), computed by `scripts/rank_countries.py` from `data/countries.json` (decision D-025). Do not hand-edit this file.",
        "",
        "> [!WARNING]",
        "> **Dated pointers, not legal, immigration or tax advice.** Visa thresholds, tax brackets, incoming-worker regimes and geopolitical conditions shift fast. Verify every statutory figure on the destination government's official portal on the day you act. All composite rankings and modelled net-pay figures on this page are **Grade M** (model outputs inheriting the weakest input, often Grade C Numbeo rents or Grade D recalled tax schedules).",
        "",
        "> [!IMPORTANT]",
        "> **Audit and volatility disclosures (as of 2026-11-19).**",
        "> - **Extract-only audit downgrade (`T0-36`):** `T0-36` had a 9% full-page Read rate; every Extract-only Grade A claim in `T0-36` was downgraded to Grade B in `data/countries.json` unless verified directly at primary official sources on 2026-11-19.",
        "> - **Active 2026 shocks:** Indian nationals face an approximately 13-year US EB-2/EB-3 green-card backlog (`T0-35 L55, L459`) plus H-1B litigation (`T0-35 L578-L579`); Gulf hubs (`AE`, `SA`, `QA`, `BH`) carry 2026 US-Iran regional conflict risk, November 2026 UAE flight disruptions and IMF growth downgrades (`T0-36 L627-L632, L1144`); the Netherlands 30% ruling steps down to 27% on 2027-01-01 (`T0-35 L589`); UK Earned Settlement shifts the baseline ILR track from 5 to 10 years outside high-earner and Global Talent tiers (`T0-35 L582`).",
        "",
        "## Method and pillars",
        "",
        f"Each country is scored across eight anchored 0–10 pillars as a triangular interval `[lo, mid, hi]`. Wide intervals encode thin samples, conflicting data, Grade C/D inputs or policy shocks. `scripts/rank_countries.py` draws **{MC_ITER:,} deterministic Monte Carlo samples** (seed `{MC_SEED}`) from each pillar's triangular distribution and computes composite 0–100 scores (`sum(weight * score * 10)`) across six lenses (all rankings **Grade M**).",
        "",
        f"**FX basis:** {data['fx_note']}",
        "",
        "| Pillar | What it measures | Scale |",
        "|---|---|---|",
    ]

    for pid in PILLARS:
        pm = data["pillars"][pid]
        lines.append(f"| **{esc(pm['label'])}** (`{pid}`) | {esc(pm['description'])} | {esc(pm['scale'])} |")

    lines += [
        "",
        "**How to read the columns:** `Score` is the Monte Carlo mean composite (0–100) with the point estimate at `mid` in brackets where useful; `P10–P90` is the 80% Monte Carlo rank interval (narrow bands mean robust rank separation, wide bands mean overlapping tiers); `P(Top 5)` is the share of draws in which the country lands in the top five. In Indian-national lenses, **India** is included as the visa-free home baseline so foreign options can be judged against staying local.",
        "",
        "## Lens comparison overview (all 33 countries)",
        "",
        "Table of deterministic lens rank (`#`) and Monte Carlo 80% rank band (`P10–P90`) across all six lenses (**Grade M**). Countries are ordered by **Overall (Indian national)** rank.",
        "",
    ]

    lens_ids = [lens["id"] for lens in lenses]
    short_labels = {
        "overall_india": "Overall (India)",
        "overall_non_eu": "Overall (non-EU)",
        "net_pay": "Net pay",
        "fast_access_india": "Fast access (IN)",
        "remote_from_india": "Remote from IN",
        "long_term_settlement": "Settlement (IN)",
    }
    lookup = {lid: {r["id"]: r for r in results[lid]} for lid in lens_ids}

    header = "| Country | Region | " + " | ".join(short_labels.get(lid, lid) for lid in lens_ids) + " |"
    sep = "|---|---|" + "|".join(["---"] * len(lens_ids)) + "|"
    lines += [header, sep]

    for row in results["overall_india"]:
        cid = row["id"]
        c = by_id[cid]
        cells = []
        for lid in lens_ids:
            r = lookup[lid][cid]
            cells.append(f"#{r['rank']} ({r['p10_rank']}–{r['p90_rank']})")
        lines.append(f"| **{esc(c['name'])}** (`{c['iso2']}`) | {esc(c['region'])} | " + " | ".join(cells) + " |")

    lines += ["", "## Detailed rankings by lens", ""]

    for lens in lenses:
        lid = lens["id"]
        w_parts = [
            f"{data['pillars'][p]['label']} {int(round(lens['weights'][p] * 100))}%"
            for p in PILLARS
            if lens["weights"][p] > 0
        ]
        lines += [
            f"### {esc(lens['name'])}",
            "",
            f"{esc(lens['description'])} Weights: {', '.join(w_parts)}. **Grade M** ({MC_ITER:,} Monte Carlo draws).",
            "",
            "| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for r in results[lid]:
            c = by_id[r["id"]]
            lines.append(
                f"| {r['rank']} | **{esc(c['name'])}** (`{c['iso2']}`) | {esc(c['region'])} | "
                f"{r1(r['mc_mean_score'])} | {r1(r['point_score'])} | "
                f"{r['p10_rank']}–{r['p90_rank']} | {r1(r['p_top5'])}% | {esc(c['caveat'])} |"
            )
        lines.append("")

    # City Snapshots
    lines += [
        "## City pay, rent and disposable income snapshots",
        "",
        "All city rows use reference total compensation from `T0-35` (converted from EUR at 1 EUR = 1.1052 USD) or `T0-36` (USD cross-rates), less modelled single-person income tax and employee social contributions, less 12 months of Numbeo 1-bedroom city-centre rent (**Grade M**; Numbeo rents are Grade C crowd-sourced averages; health insurance excluded for US, Switzerland and the Netherlands). For deeper pay negotiation and role-level bands, see [pay-benchmarks.md](../09-compensation/pay-benchmarks.md).",
        "",
        "| Country | City | Reference gross (local) | Net pay (USD/yr) | 1-BR centre rent (USD/mo) | Disposable after rent (USD/yr) | Basis and caveats | Grade | Source |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for c in countries:
        for ct in c["cities"]:
            lines.append(
                f"| {esc(c['name'])} (`{c['iso2']}`) | **{esc(ct['name'])}** | {esc(ct['ref_gross_local'])} | "
                f"{fmt_usd_k(ct['net_annual_usd_k'])} | {fmt_usd_mo(ct['rent_1br_centre_usd_mo'])} | "
                f"{fmt_usd_k(ct['disposable_annual_usd_k'])} | {esc(ct['basis_note'])} | "
                f"{ct['grade']} | {esc(ct['source'])} |"
            )

    # Incoming-worker tax, language, TZ overlap, access summary
    lines += [
        "",
        "## Access, language, time-zone overlap and incoming-worker tax regimes",
        "",
        "Summary of working language, hours overlapping a 09:00–18:00 IST workday (standard / summer time), incoming-worker tax rules and primary skilled entry pathways. For full visa criteria, processing windows and country playbooks, see [visa-and-relocation.md](visa-and-relocation.md).",
        "",
        "| Country | Working language | IST overlap (std / DST) | Incoming-worker tax regime | Main skilled route and settlement | Source |",
        "|---|---|---|---|---|---|",
    ]
    for c in countries:
        tr = c["incoming_tax_regime"]
        tz = f"{g(c['tz_overlap_india_std_h'])} h / {g(c['tz_overlap_india_dst_h'])} h"
        tax_cell = f"**{esc(tr['name'])}** ({tr['grade']}): {esc(tr['summary'])}"
        lines.append(
            f"| **{esc(c['name'])}** (`{c['iso2']}`) | {esc(c['working_language'])} | {tz} | "
            f"{tax_cell} | {esc(c['access_summary'])} | {esc(tr['source'])} |"
        )

    # Appendix A: full score ledger
    lines += [
        "",
        "## Appendix A: pillar score ledger",
        "",
        "Every country's `[lo, mid, hi]` pillar interval, evidence grade and line-verified basis from `data/countries.json`.",
        "",
        "| Country | Pillar | Interval [lo, mid, hi] | Grade | Basis and citations |",
        "|---|---|---|---|---|",
    ]
    for c in countries:
        for pid in PILLARS:
            ps = c["pillars"][pid]
            lo, mid, hi = ps["range"]
            lines.append(
                f"| {esc(c['name'])} (`{c['iso2']}`) | `{pid}` | "
                f"[{g(lo)}, {g(mid)}, {g(hi)}] | {ps['grade']} | {esc(ps['basis'])} |"
            )

    lines += [
        "",
        "## Next steps",
        "",
        "- **Relocation pathways and visa execution:** [visa-and-relocation.md](visa-and-relocation.md)",
        "- **Working cross-border remote without relocating:** [remote-cross-border.md](remote-cross-border.md)",
        "- **India remote career playbook and city comparison:** [india-remote-playbook.md](india-remote-playbook.md)",
        "- **India cross-border tax, FEMA, GST and payment rails:** [india-remote-tax.md](../09-compensation/india-remote-tax.md)",
        "- **Role-level compensation benchmarks:** [pay-benchmarks.md](../09-compensation/pay-benchmarks.md)",
        "- **Global GenAI hiring landscape:** [market-overview.md](../01-landscape/market-overview.md)",
        "",
    ]

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA, help="path to countries.json")
    ap.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="path to countries.schema.json")
    ap.add_argument("--doc", type=Path, default=DEFAULT_DOC, help="target Markdown output")
    ap.add_argument("--update", action="store_true", help="write generated Markdown to --doc")
    ap.add_argument("--check", action="store_true", help="validate data and check --doc is up to date")
    ap.add_argument("--json", type=Path, default=None, help="optional path for machine-readable JSON output")
    args = ap.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    errs = validate(data, schema)
    if errs:
        print(f"VALIDATION FAILED ({len(errs)} error(s)):", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    results = run_monte_carlo(data)
    md = render_markdown(data, results)

    # Guard against accidental relative-time words in generated prose
    rel = RELATIVE_TIME.search(prose(md))
    if rel:
        print(f"ERROR: relative-time word {rel.group(0)!r} found in generated prose", file=sys.stderr)
        return 1

    if args.json:
        payload = {
            "schema": data["schema"],
            "as_of": data["as_of"],
            "mc_iterations": MC_ITER,
            "mc_seed": MC_SEED,
            "lenses": results,
        }
        args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if args.update:
        args.doc.parent.mkdir(parents=True, exist_ok=True)
        args.doc.write_text(md, encoding="utf-8")
        print(f"updated {args.doc.relative_to(ROOT)} ({len(data['countries'])} countries, {len(data['lenses'])} lenses)")
        return 0

    if args.check:
        if not args.doc.exists():
            print(f"{args.doc.relative_to(ROOT)} does not exist; run --update", file=sys.stderr)
            return 1
        existing = args.doc.read_text(encoding="utf-8")
        if existing != md:
            print(f"{args.doc.relative_to(ROOT)} is out of date; run --update", file=sys.stderr)
            return 1
        print(f"{args.doc.relative_to(ROOT)} is up to date")
        return 0

    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
