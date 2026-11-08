#!/usr/bin/env python3
"""GenAI target order: computes it, keeps its copies in sync, and prints the analysis.

The GenAI target order is computed here from data/role_scores.json (the source of truth) using
scripts/rank_roles.py. Where a role's demand is restricted to its GenAI subset (postings naming LLM, JobsPipe JD
2026-11-02), role_scores.json gives the restricted ranges as genai_demand and genai_india_demand (Grade M, with
their arithmetic as the basis); on 2026-11-07 that is AI Engineer and ML Engineer. Everything else is the catalog's data. The order is the consensus (mean) rank across 8 lenses.

Copies of the order live in two places, and this script keeps them honest:
  * data/skills_ontology.json  roles[*].target (used to order inventories and résumé blocks)
  * career/02-roles/genai-target-roles.md  §0 table: rank, consensus mean and lens range per row

Usage:
    python3 scripts/target_roles.py                    # print the report
    python3 scripts/target_roles.py --json OUT.json    # also write machine-readable results to OUT.json
    python3 scripts/target_roles.py --update           # write the computed ranks into skills_ontology.json roles[*].target
    python3 scripts/target_roles.py --check            # exit 1 if the ontology or the §0 table disagree with the computation

Standard library only; reuses scripts/rank_roles.py (fixed seed, so results are reproducible).
"""
import argparse
import copy
import json
import re
import statistics
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import rank_roles as rr  # noqa: E402

SCORES = ROOT / 'data' / 'role_scores.json'
ONTOLOGY = ROOT / 'data' / 'skills_ontology.json'
DOC = ROOT / 'career' / '02-roles' / 'genai-target-roles.md'
LENSES = ['base', 'equal', 'pay_max', 'hiring_safety', 'moat_first', 'switcher', 'india', 'mc']
ROW = re.compile(r"^\| (\d+) \| .*? \| (?:\d|—) \| ([0-9.]+) \| (\d+)–(\d+) \|", re.M)


def adjusted(d):
    """Restrict demand to its GenAI subset where data/role_scores.json gives one (genai_demand, genai_india_demand)."""
    d = copy.deepcopy(d)
    for r in d['roles']:
        if 'genai_demand' in r:
            r['demand'].update({k: r['genai_demand'][k] for k in ('lo', 'mid', 'hi')})
        if 'genai_india_demand' in r:
            r['india']['demand'].update({k: r['genai_india_demand'][k] for k in ('lo', 'mid', 'hi')})
    return d


def analyse(d):
    ic = [r for r in d['roles'] if r['track'] == 'ic']
    names = {r['id']: r['name'] for r in ic}
    out = {'names': names}
    base = rr.rank(ic, rr.PROFILES['base'])
    out['base'] = {x['role']['id']: {'rank': x['rank'], 'cci': x['cci'], 'scores': x['scores']} for x in base}
    out['mc'] = rr.monte_carlo(ic, rr.PROFILES['base'])
    out['profiles'] = {pn: {x['role']['id']: x['rank'] for x in rr.rank(ic, w)} for pn, w in rr.PROFILES.items()}
    ind = rr.rank(ic, rr.PROFILES['base'], india=True)
    out['india'] = {x['role']['id']: {'rank': x['rank'], 'cci': x['cci']} for x in ind}
    out['india_mc'] = rr.monte_carlo(ic, rr.PROFILES['base'], india=True)
    pers = {}
    for p in rr.PERSONAS:
        elig = [r for r in ic if r['persona_access'][p] >= rr.PERSONA_GATE]
        pers[p] = [(x['role']['id'], x['cci']) for x in rr.rank(elig, rr.PROFILES['switcher'], persona=p)]
    out['persona'] = pers
    cons = {}
    for rid in names:
        pos = {
            'base': out['profiles']['base'][rid], 'equal': out['profiles']['equal'][rid],
            'pay_max': out['profiles']['pay_max'][rid], 'hiring_safety': out['profiles']['hiring_safety'][rid],
            'moat_first': out['profiles']['moat_first'][rid], 'switcher': out['profiles']['switcher'][rid],
            'india': out['india'][rid]['rank'], 'mc': out['mc'][rid]['median'],
        }
        vals = [pos[k] for k in LENSES]
        cons[rid] = {'positions': pos, 'mean': statistics.mean(vals), 'best': min(vals), 'worst': max(vals),
                     'top5_lenses': sum(v <= 5 for v in vals), 'top10_lenses': sum(v <= 10 for v in vals),
                     'global_mean': statistics.mean([pos[k] for k in LENSES if k != 'india'])}
    order = sorted(cons, key=lambda k: (cons[k]['mean'], -out['base'][k]['cci']))
    for i, k in enumerate(order, 1):
        cons[k]['target_rank'] = i
    out['consensus'] = cons
    out['order'] = order
    return out


def leadership_ranks(d):
    _, res = rr.tables(d)
    return {x['id']: x['rank'] for x in res['leadership']}


def expected_targets(d, gen, onto):
    """The target value every ontology role should carry: an integer for IC roles, 'Ln' or 'La–Lb' for leadership."""
    lead = leadership_ranks(d)
    want = {}
    for oid, r in onto['roles'].items():
        if oid in gen['consensus']:
            want[oid] = gen['consensus'][oid]['target_rank']
        else:
            ranks = sorted(lead[c] for c in r.get('covers', [oid]) if c in lead)
            if ranks:
                want[oid] = f"L{ranks[0]}" if len(ranks) == 1 else f"L{ranks[0]}–L{ranks[-1]}"
    return want


def check(d, gen, onto):
    problems = []
    want = expected_targets(d, gen, onto)
    for oid, t in want.items():
        if onto['roles'][oid]['target'] != t:
            problems.append(f"skills_ontology.json: {oid} target is {onto['roles'][oid]['target']!r}, computed {t!r}")
    rows = ROW.findall(DOC.read_text(encoding='utf-8'))
    if len(rows) != len(gen['order']):
        problems.append(f"genai-target-roles.md §0: {len(rows)} rows, computed {len(gen['order'])}")
    for (n, mean, best, worst), rid in zip(rows, gen['order']):
        c = gen['consensus'][rid]
        exp = (str(c['target_rank']), f"{rr.half_up(c['mean'], 1):.1f}", str(c['best']), str(c['worst']))
        if (n, mean, best, worst) != exp:
            problems.append(f"genai-target-roles.md §0 row {n} ({gen['names'][rid]}): has rank/mean/range "
                            f"{n}/{mean}/{best}–{worst}, computed {exp[0]}/{exp[1]}/{exp[2]}–{exp[3]}")
    return problems


def report(raw, gen):
    print('GenAI-domain consensus order (8 lenses) vs catalog consensus')
    print(f"{'#':>2} {'role':45s} {'mean':>5} {'best-worst':>10} {'top10':>5} {'CCI-G':>6} {'MC':>9} {'top1':>5} | cat#  catmean")
    for k in gen['order']:
        c, m, b = gen['consensus'][k], gen['mc'][k], gen['base'][k]
        rc = raw['consensus'][k]
        print(f"{c['target_rank']:>2} {gen['names'][k][:45]:45s} {c['mean']:5.2f} {c['best']:>4}-{c['worst']:<5} {c['top10_lenses']:>5} "
              f"{b['cci']:6.2f} {m['median']:>3}({m['p10']}-{m['p90']}) {m['top1']:5.2f} | {rc['target_rank']:>3}  {rc['mean']:5.2f}")
    print()
    print('GenAI base top 5 MC top1/top3/top5:')
    for k in gen['order'][:6]:
        m = gen['mc'][k]
        print(f"  {gen['names'][k]:45s} top1 {m['top1']:.3f} top3 {m['top3']:.3f} top5 {m['top5']:.3f}")
    print()
    print('GenAI India lens top 12:')
    for k, v in sorted(gen['india'].items(), key=lambda kv: kv[1]['rank'])[:12]:
        m = gen['india_mc'][k]
        print(f"  {v['rank']:>2} {gen['names'][k]:45s} {v['cci']:6.2f} MC {m['median']}({m['p10']}-{m['p90']}) top1 {m['top1']:.3f}")
    print()
    print('GenAI persona lenses (top 6):')
    for p, lst in gen['persona'].items():
        print(' ', p, ' | '.join(f"{gen['names'][k]} ({v:.0f})" for k, v in lst[:6]))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--update', action='store_true')
    g.add_argument('--check', action='store_true')
    ap.add_argument('--json', metavar='OUT')
    args = ap.parse_args()
    data = json.loads(SCORES.read_text(encoding='utf-8'))
    raw, gen = analyse(data), analyse(adjusted(data))
    if args.json:
        Path(args.json).write_text(json.dumps({'catalog': raw, 'genai': gen}, indent=1, default=str), encoding='utf-8')
    if args.check or args.update:
        text = ONTOLOGY.read_text(encoding='utf-8')
        onto = json.loads(text, object_pairs_hook=OrderedDict)
        if args.update:
            for oid, t in expected_targets(data, gen, onto).items():
                onto['roles'][oid]['target'] = t
            new = json.dumps(onto, indent=1, ensure_ascii=False) + '\n'
            if new != text:
                ONTOLOGY.write_text(new, encoding='utf-8')
                print('updated roles[*].target in data/skills_ontology.json')
            else:
                print('targets already up to date')
        problems = check(data, gen, onto)
        if problems:
            print('out of date:\n  ' + '\n  '.join(problems))
            sys.exit(1)
        if args.check:
            print('up to date')
        return
    report(raw, gen)


if __name__ == '__main__':
    main()
