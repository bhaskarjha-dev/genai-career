#!/usr/bin/env python3
"""Resume-layer and proof-of-work analysis for career/06-job-search/job-search-strategy.md.

Works on the concise resume layer of data/skills_ontology.json: the headline
skills and their per-role tiers, the same projection the resume matrix shows. With the
project archetypes in data/project_archetypes.json it computes:

  * universal-resume coverage: the share of each role's Must skills held by a universal
    resume (AI Engineer's Must + Important, plus ML Engineer's Must and top three Important)
  * role-resume necessity: within each resume variant (family), the anchor role's resume is
    the family resume; another role needs a dedicated resume when the family resume holds
    under 60% of its Must + Important skills or misses two or more of its Must skills
  * role similarity: weighted Jaccard over tiers (Must 3, Important 2, Should 1)
  * proof of work: greedy minimum sets of archetypes that bring every individual-contributor
    role, and the top-8 targets, to at least 60% of their weighted Must (3) + Important (2) skills

and writes the results into the GENERATED blocks of the blueprint.

Usage:
    python3 scripts/resume_layers.py              # print every generated block
    python3 scripts/resume_layers.py --update     # rewrite the GENERATED blocks in the blueprint
    python3 scripts/resume_layers.py --check      # exit 1 if they are out of date

Percentages are model outputs (EGP grade M) computed from judgement-graded tiers and archetypes.
Standard library only.
"""
import argparse
import itertools
import json
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_resume_matrix import project  # noqa: E402
from build_skills import load_ontology, validate_ontology  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "career" / "06-job-search" / "job-search-strategy.md"
ARCHETYPES = ROOT / "data" / "project_archetypes.json"
LABELS = OrderedDict([("summary", "key numbers"), ("universal", "universal coverage"), ("decisions", "role-resume decisions"),
                      ("pairs", "similar roles"), ("projects", "proof-of-work sets")])
END_MARKER = "\n<!-- END GENERATED -->"
WEIGHT = {"must": 3, "important": 2, "should": 1}
THRESHOLD = 0.6


def short(name):
    return name.split(" (")[0]


def tkey(r):
    return r["target"] if isinstance(r["target"], int) else 99


def analyse(data, archetypes):
    R = data["roles"]
    ic = sorted((k for k, r in R.items() if isinstance(r["target"], int)), key=lambda k: R[k]["target"])

    def wvec(r):
        v = {}
        for t, w in WEIGHT.items():
            for k in r[t]:
                v[k] = max(v.get(k, 0), w)
        return v

    def sim(a, b):
        va, vb = wvec(R[a]), wvec(R[b])
        keys = set(va) | set(vb)
        den = sum(max(va.get(k, 0), vb.get(k, 0)) for k in keys)
        return sum(min(va.get(k, 0), vb.get(k, 0)) for k in keys) / den if den else 0.0

    # universal resume
    ae, mle = R["ai-engineer"], R["ml-engineer"]
    uni = list(OrderedDict.fromkeys(ae["must"] + ae["important"] + mle["must"] + mle["important"][:3]))
    cov = OrderedDict()
    for k in ic:
        m = R[k]["must"]
        cov[k] = sum(1 for x in m if x in uni) / len(m)
    # families and role-resume decisions
    fam = OrderedDict()
    for k in sorted(R, key=lambda k: tkey(R[k])):
        fam.setdefault(R[k]["flavour"], []).append(k)
    decisions = OrderedDict()
    for f, members in fam.items():
        anchor = members[0]
        base = set(R[anchor]["must"] + R[anchor]["important"])
        for m in members:
            mi = R[m]["must"] + R[m]["important"]
            share = sum(1 for x in mi if x in base) / len(mi)
            must_missing = sum(1 for x in R[m]["must"] if x not in base)
            if m == anchor:
                dec = "anchor"
            elif must_missing >= 2 or share < THRESHOLD:
                dec = "dedicated"
            else:
                dec = "family"
            decisions[m] = (f, share, must_missing, dec)
    # similarity
    pairs = sorted(((sim(a, b), a, b) for a, b in itertools.combinations(ic, 2)), reverse=True)
    isolated = min(ic, key=lambda a: max(sim(a, b) for b in ic if b != a))
    iso_val = max(sim(isolated, b) for b in ic if b != isolated)
    # proof of work

    def role_cov(role, chosen):
        r = R[role]
        sk = set().union(*[set(archetypes[p]["skills"]) for p in chosen]) if chosen else set()
        w = {**{k: 2 for k in r["important"]}, **{k: 3 for k in r["must"]}}
        return sum(v for k, v in w.items() if k in sk) / sum(w.values())

    def greedy(pool):
        chosen, remaining = [], list(archetypes)
        while remaining:
            def score(ch):
                covs = [role_cov(k, ch) for k in pool]
                return (sum(c >= THRESHOLD - 1e-9 for c in covs), sum(covs))
            best = max(remaining, key=lambda p: (score(chosen + [p]), -int(p[1:])))
            if score(chosen + [best]) <= score(chosen):
                break
            chosen.append(best)
            remaining.remove(best)
            if score(chosen)[0] == len(pool):
                break
        return chosen

    top8 = [k for k in ic if R[k]["target"] <= 8]
    all_set, top8_set = greedy(ic), greedy(top8)
    return dict(R=R, ic=ic, uni=uni, cov=cov, fam=fam, decisions=decisions, pairs=pairs, isolated=(isolated, iso_val),
                all_set=all_set, top8=top8, top8_set=top8_set, role_cov=role_cov)


def blocks(data, archetypes):
    a = analyse(data, archetypes)
    R, ic, cov, dec = a["R"], a["ic"], a["cov"], a["decisions"]
    S = data["skills"]
    out = OrderedDict()
    strong = [k for k in ic if cov[k] >= 0.75 - 1e-9]
    zero = [k for k in ic if cov[k] == 0]
    n_family = len(a["fam"])
    dedicated = [k for k, v in dec.items() if v[3] == "dedicated"]
    family_ok = [k for k, v in dec.items() if v[3] == "family"]
    all_ok = sum(a["role_cov"](k, a["all_set"]) >= THRESHOLD - 1e-9 for k in ic)
    out["summary"] = "\n".join([
        f"- **Universal resume:** {len(a['uni'])} headline skills. It holds at least 75% of the Must skills of "
        f"{len(strong)} of the {len(ic)} roles and none of the Must skills of {len(zero)} roles (§2.4).",
        f"- **Resumes for a person targeting every role:** 1 universal + {n_family} family + {len(dedicated)} dedicated role "
        f"resumes = **{1 + n_family + len(dedicated)}**. {len(family_ok)} roles are served by their family resume plus tailoring (§2.5).",
        f"- **Proof of work:** {len(a['all_set'])} project archetypes bring {all_ok} of the {len(ic)} roles to at least "
        f"{THRESHOLD:.0%} coverage of their Must and Important skills; {len(a['top8_set'])} cover the top 8 targets (§2.6).",
    ])
    bands = [("**Strong (≥75%)**", lambda c: c >= 0.75 - 1e-9), ("**Partial (50–74%)**", lambda c: 0.5 - 1e-9 <= c < 0.75 - 1e-9),
             ("**Weak (<50%)**", lambda c: c < 0.5 - 1e-9)]
    rows = [f"The universal resume holds these {len(a['uni'])} headline skills: "
            + ", ".join(short(S[k]["name"]) if k in S else short(data["classes"][k]["name"]) for k in a["uni"]) + ".", "",
            "| Coverage | Roles (share of their Must skills the universal resume holds) |", "|---|---|"]
    for label, test in bands:
        members = [k for k in sorted(ic, key=lambda k: -cov[k]) if test(cov[k])]
        rows.append(f"| {label} | " + (", ".join(f"{short(R[k]['name'])} {cov[k]:.0%}" for k in members) or "—") + " |")
    out["universal"] = "\n".join(rows)
    rows = ["| Variant | Anchor (role resume = family resume) | Family resume + tailoring is enough | "
            "Needs a dedicated role resume (share of its Must + Important the family resume holds) |", "|---|---|---|---|"]
    for f, members in a["fam"].items():
        anchor = members[0]
        fam_ok = [f"{short(R[m]['name'])} ({dec[m][1]:.0%})" for m in members if dec[m][3] == "family"]
        ded = [f"{short(R[m]['name'])} ({dec[m][1]:.0%})" for m in members if dec[m][3] == "dedicated"]
        rows.append(f"| {f} | {short(R[anchor]['name'])} | {', '.join(fam_ok) or '—'} | {', '.join(ded) or '—'} |")
    out["decisions"] = "\n".join(rows)
    rows = ["| Pair | Similarity |", "|---|:---:|"]
    for s, x, y in a["pairs"][:8]:
        rows.append(f"| {short(R[x]['name'])} – {short(R[y]['name'])} | {s:.2f} |")
    iso, val = a["isolated"]
    rows += ["", f"The most isolated role is {short(R[iso]['name'])}: its closest neighbour scores {val:.2f}."]
    out["pairs"] = "\n".join(rows)
    A = archetypes
    rows = [f"**Every individual-contributor role at ≥{THRESHOLD:.0%}: {len(a['all_set'])} projects, chosen greedily:**", ""]
    rows += [f"{i}. {A[p]['name']} ({p})" for i, p in enumerate(a["all_set"], 1)]
    rows += ["", f"**The top 8 targets at ≥{THRESHOLD:.0%}: {len(a['top8_set'])} projects:**", ""]
    rows += [f"{i}. {A[p]['name']} ({p})" for i, p in enumerate(a["top8_set"], 1)]
    rows += ["", "Coverage of the top 8 with that set: " + ", ".join(
        f"{short(R[k]['name'])} {a['role_cov'](k, a['top8_set']):.0%}" for k in sorted(a["top8"], key=lambda k: -a['role_cov'](k, a['top8_set']))) + "."]
    out["projects"] = "\n".join(rows)
    return out


def spans(text):
    found = OrderedDict()
    for key, label in LABELS.items():
        begin = f"<!-- BEGIN GENERATED: scripts/resume_layers.py ({label}) -->\n"
        if text.count(begin) != 1:
            raise SystemExit(f"expected exactly one marker {begin.strip()!r}")
        i = text.index(begin) + len(begin)
        j = text.find(END_MARKER, i - 1)
        if j < 0 or "<!-- BEGIN GENERATED" in text[i:j]:
            raise SystemExit(f"no END marker after {begin.strip()!r}")
        found[key] = (i, j)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true", help="rewrite the GENERATED blocks in the blueprint")
    g.add_argument("--check", action="store_true", help="exit 1 if the GENERATED blocks are out of date")
    args = ap.parse_args()
    onto = load_ontology()
    problems = validate_ontology(onto)
    if problems:
        raise SystemExit("skills_ontology.json is invalid (run scripts/build_skills.py for details)")
    data = project(onto)
    archetypes = json.loads(ARCHETYPES.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)["archetypes"]
    bad = sorted({k for p in archetypes.values() for k in p["skills"] if k not in data["skills"]})
    if bad:
        raise SystemExit(f"project_archetypes.json uses IDs that are not headline skills: {bad}")
    out = blocks(data, archetypes)
    if not (args.update or args.check):
        for key, label in LABELS.items():
            print(f"### {label}\n\n{out[key]}\n")
        return
    text = DOC.read_text(encoding="utf-8")
    if args.check:
        stale = [LABELS[k] for k, (i, j) in spans(text).items() if text[i:j] != out[k]]
        if stale:
            print("out of date: " + ", ".join(stale))
            sys.exit(1)
        print("up to date")
        return
    for key in reversed(list(LABELS)):
        i, j = spans(text)[key]
        text = text[:i] + out[key] + text[j:]
    DOC.write_text(text, encoding="utf-8")
    print(f"updated {len(LABELS)} generated blocks in {DOC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
