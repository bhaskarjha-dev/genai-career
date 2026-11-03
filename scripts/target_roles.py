#!/usr/bin/env python3
"""GenAI-domain target-role analysis built on scripts/rank_roles.py and data/role_scores.json.

Two inputs are restricted to their GenAI subset (postings naming LLM, JobsPipe JD 2026-11-02):
  * AI Engineer: US 1,697 x 76.7% ~ 1,302 -> Demand band 9; India 398 x 76.7% ~ 305 -> India band 10
  * ML Engineer: US 1,084 x 45.0% ~ 488 -> Demand band 7; India 90 x 45.0% ~ 41 -> India band 5.5
Everything else is the catalog's data. Output: consensus rank across 8 lenses, with and without the
GenAI restriction, plus persona and India lenses, as a short text report (and JSON with --json).
This is the computation behind career/02-roles/genai-target-roles.md.

Usage:
    python3 scripts/target_roles.py                    # print the report
    python3 scripts/target_roles.py --json OUT.json    # also write machine-readable results

Standard library only; reuses scripts/rank_roles.py (fixed seed, so results are reproducible).
"""
import copy
import json
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import rank_roles as rr  # noqa: E402

JSON_OUT = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
data = json.loads((ROOT / 'data' / 'role_scores.json').read_text(encoding='utf-8'))

GENAI_ADJ = {
    'ai-engineer': {'demand': {'lo': 8.5, 'mid': 9, 'hi': 9.5}, 'india_demand': {'lo': 8.5, 'mid': 10, 'hi': 10}},
    'ml-engineer': {'demand': {'lo': 6.5, 'mid': 7, 'hi': 8}, 'india_demand': {'lo': 4, 'mid': 5.5, 'hi': 7}},
}
LENSES = ['base', 'equal', 'pay_max', 'hiring_safety', 'moat_first', 'switcher', 'india', 'mc']


def adjusted(d):
    d = copy.deepcopy(d)
    for r in d['roles']:
        a = GENAI_ADJ.get(r['id'])
        if a:
            r['demand'].update(a['demand'])
            r['india']['demand'].update(a['india_demand'])
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


raw = analyse(data)
gen = analyse(adjusted(data))
if JSON_OUT:
    Path(JSON_OUT).write_text(json.dumps({'catalog': raw, 'genai': gen}, indent=1, default=str), encoding='utf-8')

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
