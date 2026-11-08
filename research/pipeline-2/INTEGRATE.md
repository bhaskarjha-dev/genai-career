# Integrating a Research Pipeline 2 Session

How to turn a saved, verified session report into data, pages and generated views. It is written for the agent or person doing the integration and follows [AGENTS.md](../../AGENTS.md) §2 and §4. Integration is where errors creep in, so take the steps in order and finish with a clean build.

## 0. Before you start

- [ ] The report passed `python3 -B scripts/research_pipeline.py --appendix <draft>` with `PROBLEMS: 0` before it was saved, so that the saved session never needs editing.
- [ ] It was verified as [VERIFY.md](VERIFY.md) describes (every A/B item for **required** sessions, a sample for **sample** sessions), and the verification summary is its last section, or the corrections are logged in [research/ERRATA.md](../ERRATA.md).
- [ ] It is saved as `research/sessions/<id>-<slug>.md`, with the ID and slug from [catalogue.json](catalogue.json).

## 1. Register the session

1. Add the session's lifecycle stages (the catalogue's `stages`) to `SESSION_STAGES` in [scripts/build_findings.py](../../scripts/build_findings.py).
2. Add a row under "Sessions by theme" in [research/README.md](../README.md).
3. Update the hand-written session counts: [README.md](../../README.md), [AGENTS.md](../../AGENTS.md) and [research/README.md](../README.md). Generated pages count sessions themselves.
4. Run `python3 -B scripts/build_all.py`. It registers the Key Findings in the findings registry and marks the session as saved in the tracker.

## 2. Map each record to its owner

One owner per fact (decision D-019; the owners table is in AGENTS.md §2). Cite every value with the session line it comes from, in the form `T0-27 L212` (the validator checks that the line exists). Keep the report's grade unless verification changed it, and apply decision D-018's conventions (platform aggregates B; LCA filings A for filings only).

| Record type | Goes to | Notes |
|---|---|---|
| `credential` | Until reduce step R1 exists: `credentials` in [data/skills_ontology.json](../../data/skills_ontology.json) (name, issuer, level, status with `as_of`, `src`), and the role links that tier it | R1 decides whether credentials move to their own data file with the richer fields (fees, format, signal, channel value) |
| `tool`, `board` | [data/tools.json](../../data/tools.json): `stage`, `category` (an existing category in its schema; add one only with a reason), `verdict`, `evidence` (the grade), `source` (`T0-xx Lnnn`), `as_of`, `url`, `status` | The tool catalog regenerates from it |
| `company` | The target-employer list decided at reduce step R6; examples in the employer landscape | Never personal data |
| `jd` | Not stored raw in `data/`: the URLs, job IDs and phrases stay in the session. Use them for aliases (data/role_titles.json), requirement wording, prerequisites and posted pay bands | A sample of 15–30 postings is too small for share-based tier changes on its own |
| `skill_signal` | Role links in the ontology (`share`, `n`, `src`) as corroboration. Change a tier only when the sample agrees with platform shares or the job-description collector (INS-1), and give the reason | Skills arrive as ontology IDs; a `new:` skill needs a vocabulary entry first |
| `pay` | [pay benchmarks](../../career/09-compensation/pay-benchmarks.md) (the owner of pay figures), then the `comp` and India `comp` bases in [data/role_scores.json](../../data/role_scores.json), re-scored on the anchored rubric in role rankings §1 | Independent rates go to the freelance page |
| `measure` with `subject` `role:…` | `demand`, `genai_demand` and India `demand` bases, and `count_sources`, in data/role_scores.json | Re-score on the rubric; the generators recompute ranks and the target order |
| `measure` with `subject` `country:…` or `city:…` | The country data created at reduce step R2 | |
| `measure` with `subject` `skill:…` | The skills radar's momentum ring (reduce step R9) | Needs two signal types per call |
| `visa_route` | [visa and relocation](../../career/11-tracks/visa-and-relocation.md) (the owner of visa rules): corridors and the dated status table, with class and expiry per row; then reduce step R2's access pillar | Pointers, not advice; keep the disclaimer |
| `rule` | The owner page's dated status table (for example the visa page, the channels guide for pay transparency and ghost jobs, ATS mechanics for AI-hiring law), with class and expiry per row | Pointers, not advice |
| `practice` | The owner guide's rules, templates and pitfalls, with the grade shown | Keep the guide pattern (CONTRIBUTING §4) |
| `community` | The directory in the [communities guide](../../career/07-networking/communities-guide.md) | |
| `resource` | [Learning roadmaps](../../career/03-skills-and-tech/learning-roadmaps.md) | |
| `loop` | [Interview loops](../../career/08-interviewing/interview-loops.md) (the owner of loop types) | |
| `prompt` | [data/interview_prompts.json](../../data/interview_prompts.json): track, archetype, prompt, what a strong answer covers, red flags, source line | Never model answers (D-018) |
| Repository Deltas table (and any `repo_delta` record) | The claim's owner. **confirmed:** refresh its date. **updated** or **contradicted:** correct the owner and say so in the changelog. **stale** or **unverifiable:** mark the claim. A contradicted Phase 0 record becomes a candidate erratum in ROADMAP §7 | |
| `absence` | The owner page's "Evidence and limits" section (what is not measured) | |

## 3. Dates and freshness

- Each record's `as_of` plus its `ttl` class sets when the fact expires (CONTRIBUTING §3). A page's `review_by` is the earliest expiry among the facts it owns (decision D-017; generated pages compute theirs, decision D-020).
- Pay is re-verified after 90 days in this repository, even though class V3 allows 180.

## 4. Conflicts

- **Session against session:** prefer the newer primary source; keep both readings with their dates where they genuinely differ; for a material conflict, write it up with [templates/CONFLICT-RESOLUTION.template.md](../templates/CONFLICT-RESOLUTION.template.md).
- **Session against a Phase 0 record:** never edit the old session. Log the disagreement as a candidate erratum in ROADMAP §7, then confirm it into [research/ERRATA.md](../ERRATA.md).
- **Session against the knowledge base's design** (a scoring rule, a data-file shape, a page's place): append a decision to [research/DECISIONS.md](../DECISIONS.md) before changing the design.

## 5. Reduce steps

A reduce step (R1–R9 in the [tracker](README.md#tracker)) runs when the sessions it needs are saved; R3 can run role by role. The ranking steps (R1 credentials, R2 countries) follow the method in the [README](README.md#reduce-steps-from-sessions-to-data-and-pages): the sessions supply graded attributes, a script computes the order (Grade M), and a generated page shows it. A new data file needs a schema in `data/schemas/`, a generator registered in `GENERATORS` in [scripts/build_all.py](../../scripts/build_all.py), and a decision record.

## 6. Finish

- [ ] `python3 -B scripts/build_all.py` prints `PROBLEMS: 0`.
- [ ] After any script change: `python3 -B -m unittest discover -s scripts/tests`.
- [ ] Set the session's `status` to `integrated` in [catalogue.json](catalogue.json), and a reduce step's to `done` when it is complete; run `build_all.py` again so the tracker shows it.
- [ ] Add an entry under `## [Unreleased]` in [CHANGELOG.md](../../CHANGELOG.md).
- [ ] Update [ROADMAP.md](../../ROADMAP.md) if the session closes a build item or opens a new one.
