#!/usr/bin/env python3
"""Composite Career Index (CCI) ranking engine for the GenAI role catalogs.

Reads data/role_scores.json and generates every scored table in
career/02-roles/role-rankings.md:

  * base leaderboard (weights 25/25/20/15/15, deterministic tie-breaks)
  * sensitivity ranks under six weight profiles
  * Monte Carlo rank distribution (triangular sampling inside each pillar's
    [lo, mid, hi] evidence range)
  * goal lenses, persona lenses (persona-specific Access, switcher weights,
    feasibility gate) and an India lens (India demand and pay)
  * Appendix A: score ledger, persona access table, India inputs, pillar leaders

Usage:
    python3 scripts/rank_roles.py                       # print all generated blocks
    python3 scripts/rank_roles.py --update              # rewrite the GENERATED blocks in the ranked catalog in place
    python3 scripts/rank_roles.py --check               # exit 1 if those blocks are out of date
    python3 scripts/rank_roles.py --markdown out.md     # write the blocks to a separate file
    python3 scripts/rank_roles.py --json out.json       # machine-readable results

Scores are on 0-10 anchored scales; composite = sum(weight * score / 10), so a
role scoring 10 on every pillar reaches 100. Standard library only.
"""
import argparse
import json
import random
import statistics
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = ROOT / "data" / "role_scores.json"
DEFAULT_DOC = ROOT / "career" / "02-roles" / "role-rankings.md"
# block key -> label used in the catalog's "<!-- BEGIN GENERATED: scripts/rank_roles.py (<label>) -->" markers
MARKER_LABEL = {"base": "base leaderboard", "sensitivity": "sensitivity", "leadership": "leadership",
                "goal": "goal lenses", "persona": "persona lenses", "india": "India lens", "appendix": "Appendix A"}
END_MARKER = "\n<!-- END GENERATED -->"

PILLARS = ["demand", "comp", "durability", "leverage", "access"]
PERSONAS = ["backend", "data_scientist", "frontend", "non_technical", "phd"]
PERSONA_LABEL = {"backend": "Backend / Systems SWE", "data_scientist": "Data Scientist / BI",
                 "frontend": "Frontend / Full-Stack", "non_technical": "Non-Technical (5+ yrs domain)",
                 "phd": "PhD / Academic Researcher"}
PROFILES = {
    "base":          {"demand": 25, "comp": 25, "durability": 20, "leverage": 15, "access": 15},
    "equal":         {"demand": 20, "comp": 20, "durability": 20, "leverage": 20, "access": 20},
    "pay_max":       {"demand": 15, "comp": 40, "durability": 20, "leverage": 10, "access": 15},
    "hiring_safety": {"demand": 40, "comp": 20, "durability": 15, "leverage": 10, "access": 15},
    "moat_first":    {"demand": 15, "comp": 20, "durability": 40, "leverage": 10, "access": 15},
    "switcher":      {"demand": 25, "comp": 15, "durability": 15, "leverage": 10, "access": 35},
}
PROFILE_LABEL = {"base": "Base", "equal": "Equal", "pay_max": "Pay-max", "hiring_safety": "Hiring-safety",
                 "moat_first": "Moat-first", "switcher": "Switcher"}
GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "M": 2, "D": 3}
MC_ITER = 20000
MC_SEED = 20261102
ACCESS_SPREAD = 1.0  # persona timelines are model outputs (Grade D): +/- 1 point
PERSONA_GATE = 4.0   # persona Access below this maps to T2-01's "implausible within 12 months" (○)


# ---------------------------------------------------------------- helpers
def half_up(x, places):
    q = Decimal("1") if places == 0 else Decimal("0." + "0" * (places - 1) + "1")
    return Decimal(str(round(x, 6))).quantize(q, rounding=ROUND_HALF_UP)


def r1(x):
    """Round half-up to one decimal (banker's rounding could hide a real ordering)."""
    return str(half_up(x, 1))


def r0(x):
    return str(half_up(x, 0))


def g(x):
    return "%g" % x


def clip(x, lo=0.0, hi=10.0):
    return max(lo, min(hi, x))


def tri(lo, mid, hi):
    return {"lo": float(lo), "mid": float(mid), "hi": float(hi)}


# ---------------------------------------------------------------- scoring
def derived_access(role, persona=None):
    """Access pillar: persona-specific score, or 0.5*max + 0.5*mean over the five personas."""
    if "access" in role:  # leadership / independent tracks carry an explicit score
        a = role["access"]
        return tri(a["lo"], a["mid"], a["hi"])
    pa = role["persona_access"]
    if persona:
        m = pa[persona]
    else:
        vals = [pa[p] for p in PERSONAS]
        m = 0.5 * max(vals) + 0.5 * statistics.mean(vals)
    return tri(clip(m - ACCESS_SPREAD), m, clip(m + ACCESS_SPREAD))


def pillar_ranges(role, persona=None, india=False):
    out = {}
    for p in ["demand", "comp", "durability", "leverage"]:
        src = role[p]
        if india and p in ("demand", "comp") and "india" in role:
            src = role["india"][p]
        out[p] = tri(src["lo"], src["mid"], src["hi"])
    out["access"] = derived_access(role, persona)
    return out


def composite(scores, weights):
    return sum(weights[p] * scores[p] / 10.0 for p in PILLARS)


def rank(roles, weights, persona=None, india=False):
    rows = []
    for r in roles:
        pr = pillar_ranges(r, persona, india)
        s = {p: pr[p]["mid"] for p in PILLARS}
        rows.append({"role": r, "scores": s, "cci": composite(s, weights)})
    # Deterministic tie-break cascade: CCI, Demand, Durability, Pay, then name.
    rows.sort(key=lambda t: (-round(t["cci"], 6), -t["scores"]["demand"], -t["scores"]["durability"],
                             -t["scores"]["comp"], t["role"]["name"]))
    for i, t in enumerate(rows, 1):
        t["rank"] = i
    return rows


def monte_carlo(roles, weights, persona=None, india=False, n=MC_ITER, seed=MC_SEED):
    rnd = random.Random(seed)
    ranges = {r["id"]: pillar_ranges(r, persona, india) for r in roles}
    ranks = {r["id"]: [] for r in roles}
    first = {r["id"]: 0 for r in roles}
    for _ in range(n):
        draw = []
        for r in roles:
            pr = ranges[r["id"]]
            s = {p: rnd.triangular(pr[p]["lo"], pr[p]["hi"], pr[p]["mid"]) for p in PILLARS}
            draw.append((composite(s, weights), r["id"]))
        draw.sort(key=lambda t: -t[0])
        first[draw[0][1]] += 1
        for i, (_, rid) in enumerate(draw, 1):
            ranks[rid].append(i)
    res = {}
    for rid, rs in ranks.items():
        rs.sort()
        res[rid] = {"median": int(half_up(statistics.median(rs), 0)), "p10": rs[int(0.10 * n)],
                    "p90": rs[int(0.90 * n) - 1], "top1": first[rid] / n,
                    "top3": sum(x <= 3 for x in rs) / n, "top5": sum(x <= 5 for x in rs) / n,
                    "top10": sum(x <= 10 for x in rs) / n}
    return res


def confidence(role):
    """High: demand and pay both rest on A/B evidence. Medium: worst of the two is C/M. Low: any D."""
    worst = max(GRADE_ORDER[role["demand"]["grade"]], GRADE_ORDER[role["comp"]["grade"]])
    return {0: "High", 1: "High", 2: "Medium", 3: "Low"}[worst]


def band(cci):
    return "S" if cci >= 75 else "A" if cci >= 65 else "B" if cci >= 55 else "C"


# ---------------------------------------------------------------- tables
def tables(data):
    roles = data["roles"]
    ic = [r for r in roles if r["track"] == "ic"]
    lead = [r for r in roles if r["track"] == "leadership"]
    base = rank(ic, PROFILES["base"])
    mc = monte_carlo(ic, PROFILES["base"])
    blocks = {}

    t = ["| Rank | Role | CCI /100 | Band | Demand | Pay | Durability | Leverage | Access | Evidence confidence | Monte Carlo rank (P10–P90) | P(top 5) |",
         "|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for x in base:
        r, s, m = x["role"], x["scores"], mc[x["role"]["id"]]
        t.append(f"| {x['rank']} | {r['name']} | **{r1(x['cci'])}** | {band(x['cci'])} | {g(s['demand'])} | {g(s['comp'])} | "
                 f"{g(s['durability'])} | {g(s['leverage'])} | {r1(s['access'])} | {confidence(r)} | "
                 f"{m['median']} ({m['p10']}–{m['p90']}) | {r0(100 * m['top5'])}% |")
    blocks["base"] = "\n".join(t)

    prof = {pn: {x["role"]["id"]: x["rank"] for x in rank(ic, w)} for pn, w in PROFILES.items()}
    t = ["| Role | " + " | ".join(PROFILE_LABEL[p] for p in PROFILES) + " | Best–worst |",
         "|---|" + "|".join(":---:" for _ in PROFILES) + "|:---:|"]
    for x in base:
        rs = [prof[p][x["role"]["id"]] for p in PROFILES]
        t.append(f"| {x['role']['name']} | " + " | ".join(str(v) for v in rs) + f" | {min(rs)}–{max(rs)} |")
    blocks["sensitivity"] = "\n".join(t)

    lb = rank(lead, PROFILES["base"])
    t = ["| Rank | Role | CCI /100 | Demand | Pay | Durability | Leverage | Access | Evidence confidence |",
         "|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for x in lb:
        r, s = x["role"], x["scores"]
        t.append(f"| L{x['rank']} | {r['name']} | **{r1(x['cci'])}** | {g(s['demand'])} | {g(s['comp'])} | "
                 f"{g(s['durability'])} | {g(s['leverage'])} | {g(s['access'])} | {confidence(r)} |")
    blocks["leadership"] = "\n".join(t)

    goal = {}
    t = ["| Goal (profile) | #1 | #2 | #3 | #4 | #5 |", "|---|---|---|---|---|---|"]
    for pn in ["hiring_safety", "pay_max", "moat_first", "switcher", "equal"]:
        rr = rank(ic, PROFILES[pn])[:5]
        goal[pn] = [x["role"]["id"] for x in rr]
        t.append(f"| {PROFILE_LABEL[pn]} | " + " | ".join(f"{x['role']['name']} ({r0(x['cci'])})" for x in rr) + " |")
    blocks["goal"] = "\n".join(t)

    persona_res = {}
    t = ["| Persona | #1 | #2 | #3 | #4 | #5 | Next best |", "|---|---|---|---|---|---|---|"]
    for p in PERSONAS:
        eligible = [r for r in ic if r["persona_access"][p] >= PERSONA_GATE]
        rr = rank(eligible, PROFILES["switcher"], persona=p)
        persona_res[p] = [x["role"]["id"] for x in rr]
        nxt = ", ".join(x["role"]["name"] for x in rr[5:7])
        t.append(f"| {PERSONA_LABEL[p]} | " + " | ".join(f"{x['role']['name']} ({r0(x['cci'])})" for x in rr[:5]) + f" | {nxt} |")
    blocks["persona"] = "\n".join(t)

    ib = rank(ic, PROFILES["base"], india=True)
    imc = monte_carlo(ic, PROFILES["base"], india=True)
    grank = {x["role"]["id"]: x["rank"] for x in base}
    t = ["| India rank | Role | CCI (India) | India Demand | India Pay | Global rank | Monte Carlo rank (P10–P90) |",
         "|:---:|---|:---:|:---:|:---:|:---:|:---:|"]
    for x in ib[:12]:
        r, s, m = x["role"], x["scores"], imc[x["role"]["id"]]
        t.append(f"| {x['rank']} | {r['name']} | {r1(x['cci'])} | {g(s['demand'])} | {g(s['comp'])} | {grank[r['id']]} | "
                 f"{m['median']} ({m['p10']}–{m['p90']}) |")
    blocks["india"] = "\n".join(t)

    blocks["appendix"] = appendix(data, base, lb)
    results = {
        "base": [{"rank": x["rank"], "id": x["role"]["id"], "cci": round(x["cci"], 3), "scores": x["scores"],
                  "band": band(x["cci"]), "confidence": confidence(x["role"])} for x in base],
        "monte_carlo": mc, "profiles": prof, "goal_lenses": goal, "persona_lenses": persona_res,
        "leadership": [{"rank": x["rank"], "id": x["role"]["id"], "cci": round(x["cci"], 3)} for x in lb],
        "india": [{"rank": x["rank"], "id": x["role"]["id"], "cci": round(x["cci"], 3)} for x in ib],
        "india_monte_carlo": imc,
    }
    return blocks, results


def appendix(data, base, lb):
    order = [x["role"] for x in base] + [x["role"] for x in lb]
    out = ["### A.1 Score justification ledger\n",
           "Format: `mid [lo–hi] · grade`. Durability and Leverage are labelled judgements (Grade D) with uniform ±1.5 / ±1.0 bands. "
           "Access is computed from A.2.\n"]

    def rng(v):
        return f"{g(v['mid'])} [{g(v['lo'])}–{g(v['hi'])}] · {v['grade']}"

    for i, r in enumerate(order, 1):
        tag = f"#{i}" if r["track"] == "ic" else f"L{i - len(base)}"
        out.append(f"<a id=\"ledger-{r['id']}\"></a>\n**{tag} · {r['name']}** (`{r['id']}`)\n")
        out += ["| Pillar | Score | Basis |", "|---|---|---|"]
        for p, lab in (("demand", "Demand"), ("comp", "Pay"), ("durability", "Durability"), ("leverage", "Leverage")):
            out.append(f"| {lab} | {rng(r[p])} | {r[p]['basis']} |")
        if r["track"] == "ic":
            acc = derived_access(r)["mid"]
            out.append(f"| Access | {r1(acc)} [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |")
        else:
            out.append(f"| Access | {rng(r['access'])} | {r['access']['basis']} |")
        out.append("")

    out += ["### A.2 Persona access scores (inputs to the Access pillar and the persona lenses)\n",
            "Scale: ≥7.5 ≈ a T2-01 ● corridor (about 6–8 months at 15–20 h/week); 4–7 ≈ ◐ (plausible but extended); "
            "<4 ≈ ○ (not plausible within 12 months; excluded from that persona's lens). Timelines come from T0-06 R2 and T2-01 §4.1 "
            "(Grade D models, conditional on success); cells without a modelled corridor are inferred from skill adjacency (Grade D).\n",
            "| Role | Backend SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Researcher | Access pillar |",
            "|---|:---:|:---:|:---:|:---:|:---:|:---:|"]
    for x in base:
        r = x["role"]
        pa = r["persona_access"]
        out.append(f"| {r['name']} | " + " | ".join(g(pa[k]) for k in PERSONAS) + f" | {r1(derived_access(r)['mid'])} |")
    out.append("")

    out += ["### A.3 India-lens inputs\n",
            "India Demand bands (live India postings): ≥300 → 10 · 150–299 → 8.5 · 75–149 → 7 · 30–74 → 5.5 · 10–29 → 4 · 1–9 → 2.5 · ≈0 → 1. "
            "India Pay anchors (TC): P50 ≥ ₹60L → 9.5 · ₹40–60L → 8 · ₹25–40L → 6.5 · ₹15–25L → 5 · < ₹15L → 3, adjusted for the P90 ceiling. "
            "Roles without India data carry wide ranges and Grade D.\n",
            "| Role | India Demand | India Pay | Basis |", "|---|---|---|---|"]
    for x in base:
        r = x["role"]
        i = r["india"]
        out.append(f"| {r['name']} | {rng(i['demand'])} | {rng(i['comp'])} | {i['demand']['basis']} / {i['comp']['basis']} |")
    out.append("")

    out.append("### A.4 Single-pillar leaders (IC roles, mid scores; ties shown)\n")
    ic = [x["role"] for x in base]
    for p, lab in (("comp", "Pay ceiling"), ("demand", "Demand"), ("durability", "Durability (judgement)")):
        srt = sorted(ic, key=lambda r: (-r[p]["mid"], r["name"]))
        cutoff = srt[min(5, len(srt) - 1)][p]["mid"]
        lead = [r for r in srt if r[p]["mid"] >= cutoff]
        out.append(f"- **{lab}:** " + "; ".join(f"{r['name']} {g(r[p]['mid'])}" for r in lead))
    return "\n".join(out)


def render(blocks):
    names = [("base", "Base leaderboard (individual-contributor roles)"), ("sensitivity", "Sensitivity: rank under each weight profile"),
             ("leadership", "Leadership & independent tracks (ranked among themselves)"), ("goal", "Goal lenses (top 5 under each alternative weight profile)"),
             ("persona", f"Persona lenses (switcher weights; roles with persona Access < {PERSONA_GATE:g} excluded)"),
             ("india", "India lens (India Demand and Pay, base weights)"), ("appendix", "Appendix A")]
    return "\n\n".join(f"### {title}\n\n{blocks[k]}" if k != "appendix" else blocks[k] for k, title in names) + "\n"


def block_spans(path, text):
    """(start, end) of the content between each BEGIN/END GENERATED marker pair, by block key."""
    spans = {}
    for key, label in MARKER_LABEL.items():
        begin = f"<!-- BEGIN GENERATED: scripts/rank_roles.py ({label}) -->\n"
        if text.count(begin) != 1:
            raise SystemExit(f"{path}: expected exactly one marker {begin.strip()!r}")
        i = text.index(begin) + len(begin)
        j = text.find(END_MARKER, i)
        if j < 0:
            raise SystemExit(f"{path}: no END marker after {begin.strip()!r}")
        spans[key] = (i, j)
    return spans


def update_doc(path, blocks):
    """Replace the content between each BEGIN/END GENERATED marker pair in `path` with fresh blocks."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    for key in MARKER_LABEL:
        i, j = block_spans(path, text)[key]
        text = text[:i] + blocks[key] + text[j:]
    path.write_text(text, encoding="utf-8")


def stale_blocks(path, blocks):
    """Labels of the generated blocks in `path` that differ from fresh output."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    return [MARKER_LABEL[k] for k, (i, j) in block_spans(path, text).items() if text[i:j] != blocks[k]]


def validate(data):
    for r in data["roles"]:
        checks = [(p, r[p]) for p in ["demand", "comp", "durability", "leverage"]]
        if r["track"] == "ic":
            assert set(r["persona_access"]) == set(PERSONAS), r["id"]
            assert all(0 <= v <= 10 for v in r["persona_access"].values()), r["id"]
            checks += [("india." + p, r["india"][p]) for p in ("demand", "comp")]
        else:
            checks.append(("access", r["access"]))
        for name, v in checks:
            assert 0 <= v["lo"] <= v["mid"] <= v["hi"] <= 10, (r["id"], name, v)
            assert v["grade"] in GRADE_ORDER, (r["id"], name, v["grade"])
            assert v.get("basis"), (r["id"], name, "missing basis")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data", default=str(DEFAULT_DATA))
    ap.add_argument("--markdown", help="write all generated markdown blocks to this path")
    ap.add_argument("--json", help="write machine-readable results to this path")
    ap.add_argument("--update", nargs="?", const=str(DEFAULT_DOC), metavar="DOC",
                    help="rewrite the GENERATED blocks of the ranked catalog in place (default: %(const)s)")
    ap.add_argument("--check", nargs="?", const=str(DEFAULT_DOC), metavar="DOC",
                    help="exit 1 if the GENERATED blocks of the ranked catalog are out of date (default: %(const)s)")
    args = ap.parse_args()
    data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    validate(data)
    blocks, results = tables(data)
    md = render(blocks)
    if args.check:
        stale = stale_blocks(args.check, blocks)
        if stale:
            print("out of date: " + ", ".join(stale))
            raise SystemExit(1)
        print("up to date")
    elif args.update:
        update_doc(args.update, blocks)
        print(f"updated {len(MARKER_LABEL)} generated blocks in {args.update}")
    else:
        print(md)
    if args.markdown:
        Path(args.markdown).write_text(md, encoding="utf-8")
    if args.json:
        Path(args.json).write_text(json.dumps(results, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
