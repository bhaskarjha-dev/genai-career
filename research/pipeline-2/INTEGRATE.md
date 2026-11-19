# Integrating Research Pipeline 2

How to turn 51 saved research sessions into the knowledge base the [CHARTER](../../CHARTER.md) describes: "the most reliable source of career intelligence for professionals working in Generative AI." This document is written for the agent or person doing the integration and follows [AGENTS.md](../../AGENTS.md) §2 and §4.

## The vision: what the repository should become

The `career/` folder is the **product**. The `research/sessions/` folder is the **lab notebook**. The `data/` folder is the **database**.

A reader should get everything they need from `career/`. They should never need to open a research session to find the answer to a career question. If a career page cannot answer a question that a session covers, the page is incomplete — that is a gap to close, not a design choice.

The data files (`data/*.json`) power generated views: role rankings, skill inventories, the tool catalog, prep packs. These are structured, queryable, and updated by scripts. The career guides carry the **narrative intelligence**: decision rules, comparisons, anti-patterns, templates, employer-specific detail, regional nuance, and step-by-step guidance. Both layers must be fed by the research.

## Why this matters: the gap as of November 2026

The 48 hand-drafted career guides were written from Phase 0 sessions in a 2-day agent sprint on 2026-11-05/06. They are well-structured, well-graded, and internally consistent — but they draw on only the Phase 0 research base (~2 MB across 24 sessions). The 51 RP2 sessions (~8.2 MB) represent the deep, targeted, per-topic evidence that Phase 0 was never designed to provide. As of this writing, only 1 of 116 career pages cites any RP2 session.

The largest gaps, by ratio of session evidence to career page content:

| Career page | Current | RP2 session(s) | Session total | Gap |
|---|---|---|---|---|
| `visa-and-relocation.md` | 57 KB | T0-37 to T0-42 | 1,228 KB | 21× |
| `interview-loops.md` | 46 KB | T0-46 | 491 KB | 11× |
| 29 role hubs (total) | ~260 KB | T0-48 to T0-66 | ~2,750 KB | 11× |
| `online-presence.md` | 23 KB | T0-19 + T0-20 | 211 KB | 9× |
| Certifications (2 files) | 57 KB | T0-29 to T0-34 | 887 KB | 16× |
| `channels-and-boards.md` | 41 KB | T0-24 + T0-25 | 248 KB | 6× |
| `resume-strategy.md` | 42 KB | T0-23 | 228 KB | 5× |
| `pay-benchmarks.md` | 51 KB | T0-44 + T0-45 | 341 KB | 7× |

Closing these gaps is the purpose of integration.

## Two layers of integration

Each session carries two kinds of knowledge. Both must be integrated — the second is where most of the value lies.

### Layer 1: Structured records → data files

The Data Appendix of each session contains JSONL records (9,703 across 51 sessions). These map to data files per the [record-to-owner table](#2-map-each-record-to-its-owner) below. This is the mechanical layer: extract records, update JSON, run generators. It feeds the generated views (role hubs, inventories, rankings, catalogs, prep packs).

### Layer 2: Narrative intelligence → career guides

Everything between the front matter and the Data Appendix — the Key Findings, Detailed Findings, Recommendation, Alternatives Considered, Repository Deltas, Absences, Open Questions — contains the intelligence that JSON records cannot carry:

| Knowledge type | Example | Where it belongs |
|---|---|---|
| Decision rules | "Use Easy Apply only on LinkedIn for roles posted <48h" | Career guide, as a graded rule |
| Comparative analysis | "Wellfound vs AngelList vs Y Combinator boards: volume, quality, remote share" | Career guide, as a comparison table |
| Step-by-step templates | "Cold outreach email sequence: day 0, day 3, day 7" | Career guide, as a template block |
| Regional nuance | "Indian résumés still expect a photo and a declaration; US résumés penalise both" | Career guide, as a regional table |
| Anti-patterns | "Adding 500+ skills on LinkedIn triggers recruiter spam filters" | Career guide, as a pitfall callout |
| Employer-specific detail | "Google's L4 AI Engineer loop: 5 rounds, 45 min each" | Career guide, in the employer loop table |
| Cost-benefit reasoning | "AWS SAP-C02 at \$300 covers 60% overlap with AI Practitioner" | Career guide, in the credential sequencing |
| Process mechanics | "Canada Express Entry: 67-point grid, minimum CRS ~490 for AI" | Visa page or country sub-page |
| Absence documentation | "No measurable hiring signal for 'AI Ethics Officer'" | Owner page's "Evidence and limits" section |

**A session is not a data dump to be loaded. It is a research report to be read, evaluated, and synthesised into the pages that readers will use.**

## How to integrate a session

For each session in a reduce step:

### Read

1. **Read the entire narrative body** — not just the Data Appendix. The narrative contains the intelligence that makes the career guides actually useful.
2. **Read the Key Findings table** — these are the session's most important conclusions. Each finding graded B or above should inform a career page.
3. **Read the Repository Deltas table** — each K-number carries a verdict (confirmed, updated, contradicted, stale, unverifiable). Act on each per [§4 Conflicts](#4-conflicts).
4. **Read the Absences section** — what the brief asked for but was not found. These go into the career page's "Evidence and limits" section.

### Evaluate

Do not accept findings blindly. For each piece of evidence:

- **Is the grade earned?** Does the source support the claim at the stated confidence?
- **Does it conflict with Phase 0 or with another RP2 session?** If so, prefer the newer primary source and log the disagreement.
- **Is the coverage complete?** Does the session cover everything the career page needs, or are there gaps the page should acknowledge?
- **Is the recommendation sound?** Would a subject-matter expert give different advice?
- **Do the JSONL records match the narrative?** Sometimes the narrative says one thing and a record says another.

### Synthesise

Do not copy-paste from the session into the career page. Rewrite the page's sections with the deeper evidence, **in the page's own voice and structure**:

- Follow the guide pattern (CONTRIBUTING §4): Purpose and audience → Rules and decision table → How to do it → Evidence and limits.
- Grade every claim. Cite with `T0-XX LNNN` format (the validator checks that the line exists).
- Keep the page readable. A 491 KB session does not mean a 491 KB career page. The session is exhaustive research; the career page is **synthesised guidance**.
- Update the page's `sources`, `last_verified` and `review_by` front matter.

### Update data

Extract the JSONL records from the Data Appendix and map them to their owners per [§2](#2-map-each-record-to-its-owner). Run the generators.

## Role hubs: the generated-blocks approach

The 29 role hubs are (as of 2026-11-19) 9 KB generated summaries from `data/role_scores.json`. The 19 role dossier sessions average 145 KB of deep analysis each. The hubs serve as navigation — scores, skills, links — but a reader asking "What does an AI Engineer actually do, and how do I become one?" gets a score card, not an answer.

**Approach:** add hand-written sections below the generated block. The hub becomes a "(generated blocks)" file — part generated from data, part hand-written from the dossier narrative. The generated block gives the scores; the hand-written sections give the context: career path, employer landscape, interview themes, day-in-the-life, title confusion, India-specific demand. Update the `generated_by` front matter to `"build_role_hubs.py (generated blocks)"`. This follows the existing pattern used in `resume-strategy.md` and `job-search-strategy.md`.

## New pages to create where the evidence demands them

When a session's content exceeds what an existing page can absorb, or when the topic has no owner page, create one. Every new page under `career/` needs front matter that passes `data/schemas/frontmatter.schema.json` and must link to at least one other document. Add it to its folder's `README.md`.

Likely new pages based on the session sizes and the current structure:

| Potential page | Evidence from | Why |
|---|---|---|
| Country-specific visa sub-pages (6) in `career/11-tracks/visa/` | T0-37 to T0-42 (1,228 KB total) | 57 KB overview page cannot absorb 1.2 MB of procedural detail |
| Remote and cross-border work guide | T0-43 (135 KB) | No existing page owns EOR platforms, cross-border compliance, contractor-vs-employee analysis |
| LinkedIn guide | T0-19 (108 KB) | `online-presence.md` (23 KB) covers four surfaces; LinkedIn alone warrants a dedicated page |
| Fellowships and residencies | T0-21 (171 KB) | Distinct enough from communities; important for PhD and research transitions |
| Country ranking (generated) | T0-35 + T0-36 (880 KB) | A new data file, ranking script, and generated page — the R2 method in [README.md](README.md) |
| Credential catalog (generated) | T0-29 to T0-34 (887 KB) | A per-vendor encyclopaedic reference, generated from the credential data |
| Target-employer list | T0-27 (109 KB) | No existing page; open decision in ROADMAP §6.9 on data file vs page |

Create these only when the evidence justifies them — not to fill a template. If a session's content fits naturally in an existing page, expand that page instead.

## Registration

Before the first reduce step, register all saved RP2 sessions:

1. Add each session's lifecycle stages (from [catalogue.json](catalogue.json) `stages`) to `SESSION_STAGES` in [scripts/build_findings.py](../../scripts/build_findings.py). The stages, by session:

   | Sessions | Stages |
   |---|---|
   | T0-19 | [7] |
   | T0-20 | [5, 7] |
   | T0-21 | [7] |
   | T0-22 | [6, 7] |
   | T0-23 | [6] |
   | T0-24, T0-25 | [6] |
   | T0-26 | [0, 6] |
   | T0-27 | [1, 6] |
   | T0-29 to T0-32, T0-34 | [4] |
   | T0-35, T0-36 | [1, 11] |
   | T0-37 to T0-42 | [11] |
   | T0-43 | [9, 11] |
   | T0-44 | [9] |
   | T0-45 | [9, 11] |
   | T0-46 | [8] |
   | T0-47 | [6, 8] |
   | T0-48 to T0-65 | [2, 3] |
   | T0-66 | [2, 9, 11] |
   | T0-67 | [11] |
   | T0-68, T0-69 | [3] |
   | T0-70 | [1] |
   | T0-71 | [10] |

2. Add rows under "Sessions by theme" in [research/README.md](../README.md).
3. Update the hand-written session counts: [README.md](../../README.md), [AGENTS.md](../../AGENTS.md) and [research/README.md](../README.md).
4. Run `python3 -B scripts/build_all.py`.

## 0. Before you start

- [ ] The report passed `python3 -B scripts/research_pipeline.py --appendix <draft>` with `PROBLEMS: 0` before it was saved, so that the saved session never needs editing.
- [ ] It is saved as `research/sessions/<id>-<slug>.md`, with the ID and slug from [catalogue.json](catalogue.json).

## 1. Reduce steps and what each one feeds

A reduce step runs when the sessions it needs are saved; R3 can run role by role. Start with R5 (Résumé) as a pilot: one session, self-contained, validates the full workflow before scaling.

The `feeds` field in [catalogue.json](catalogue.json) lists the files each session was designed to change. Use it as a starting point, not a ceiling — if the session's narrative clearly belongs in a page not listed in `feeds`, update that page too.

### R5 Résumé (1 session — pilot)

**Session:** T0-23 (228 KB)

| Data file | From record types |
|---|---|
| `data/skills_ontology.json` | `skill_signal` |
| `data/tools.json` | `tool` |

| Career page | What the session's narrative adds |
|---|---|
| `career/06-job-search/resume-strategy.md` | 2026 format experiments (portal vs designed), ATS parse comparisons, before/after rewrites, keyword density, regional norms (US vs UK vs India vs EU), AI screening findings |
| `career/06-job-search/ats-mechanics.md` | ATS parsing data, format-specific parse failure rates, AI screening layer findings |

### R8 Interviewing (2 sessions)

**Sessions:** T0-46 (491 KB), T0-47 (118 KB)

| Data file | From record types |
|---|---|
| `data/interview_prompts.json` | `prompt` |
| `data/tools.json` | `tool` |
| `data/role_scores.json` | `measure` (demand corroboration) |

| Career page | What the sessions' narratives add |
|---|---|
| `career/08-interviewing/interview-loops.md` | Per-employer loop details for 20+ employers, AI-assistant policies, take-home formats, India-specific loops, debrief mechanics. At 46 KB vs 491 KB, this page may need restructuring |
| `career/08-interviewing/system-design-archetypes.md` | Model price tables, new archetypes from real interviews |
| `career/08-interviewing/coding-rounds.md` | Coding round formats, platform policies, time limits per employer |
| `career/08-interviewing/behavioral-calibration.md` | Employer-specific behavioural rubrics |
| `career/06-job-search/ats-mechanics.md` | AI-mediated hiring: AI interview platforms, proctoring, candidate-side AI, deepfake concerns, fraud detection |

### R4 Networking (4 sessions)

**Sessions:** T0-19 (108 KB), T0-20 (103 KB), T0-21 (171 KB), T0-22 (84 KB)

| Data file | From record types |
|---|---|
| `data/tools.json` | `tool`, `board` |
| `data/project_archetypes.json` | `practice` |

| Career page | What the sessions' narratives add |
|---|---|
| `career/07-networking/online-presence.md` | LinkedIn recruiter search mechanics, Open to Work effects, feed ranking, skill endorsements, Premium Career ROI, GitHub README templates, portfolio site patterns. The page is 23 KB for two 100+ KB sessions — may spawn a LinkedIn sub-page |
| `career/07-networking/communities-guide.md` | X/Twitter strategy, frontier communities, fellowship programmes, conference deep-dives, India event calendar, community-to-hire case studies. T0-21 at 171 KB is 5× the page |
| `career/07-networking/referrals-and-outreach.md` | Legal frameworks (CAN-SPAM, CASL, GDPR), deliverability mechanics, more templates |
| `career/05-portfolio/proof-of-work-standards.md` | GitHub-specific proof-of-work patterns, README writing standards |
| `career/11-tracks/phd-to-industry.md` | Fellowship and residency programmes for PhD transitions |

### R6 Job search (4 sessions)

**Sessions:** T0-24 (148 KB), T0-25 (94 KB), T0-26 (81 KB), T0-27 (109 KB)

| Data file | From record types |
|---|---|
| `data/tools.json` | `board`, `tool` |
| `data/role_scores.json` | `measure` |

| Career page | What the sessions' narratives add |
|---|---|
| `career/06-job-search/channels-and-boards.md` | Per-board audits, search syntax, ghost-job heuristics, pay transparency rules, scam patterns. T0-25 fills the **explicitly stated India gap**: Naukri, Instahyre, iimjobs |
| `career/06-job-search/application-operating-system.md` | Tool reviews (trackers, builders, auto-apply agents, risk analysis) |
| `career/06-job-search/job-search-strategy.md` | Target-employer methodology, employer-tier routing |
| `career/01-landscape/employer-landscape.md` | Employer data: ATS systems, sponsorship, board URLs, remote policies |
| `career/11-tracks/india-remote-playbook.md` | India-specific board analysis |

### R7 Pay (2 sessions)

**Sessions:** T0-44 (112 KB), T0-45 (229 KB)

| Data file | From record types |
|---|---|
| `data/role_scores.json` | `pay`, `measure` — comp bases re-scored on the rubric |

| Career page | What the sessions' narratives add |
|---|---|
| `career/09-compensation/pay-benchmarks.md` | 2026 US/UK/Europe/Singapore/Gulf detailed tables, India city-by-city and employer-by-employer breakdowns, equity patterns, GCC vs product vs startup pay |
| `career/09-compensation/negotiation-playbook.md` | Negotiation leverage data, India-specific patterns, equity valuation |
| `career/11-tracks/india-remote-playbook.md` | India pay benchmarks in the remote context |
| `career/11-tracks/freelance-fractional.md` | Independent rates (the owner of freelance pay — D-019) |

### R3 Roles (19 sessions — the bulk)

**Sessions:** T0-48 to T0-66 (~2,750 KB total). Can run role by role. Start with one (e.g. T0-48, AI Engineer) to validate the hub-expansion pattern.

| Data file | From record types |
|---|---|
| `data/role_scores.json` | `measure` (demand, genai_demand, india demand), `pay` |
| `data/skills_ontology.json` | `skill_signal` from JD samples — change tiers only with corroboration |
| `data/role_titles.json` | `jd` — title aliases from postings |
| `data/tools.json` | `tool` |

| Career page | What the sessions' narratives add |
|---|---|
| `career/02-roles/hubs/<role>.md` (29 files) | Career path, day-in-the-life, employer landscape, interview themes, title confusion, India demand — added as hand-written sections below the generated block |
| `career/09-compensation/pay-benchmarks.md` | Per-role pay data where the dossier has pay records |
| `career/01-landscape/emerging-roles.md` | T0-57 (Agentic AI Engineer) and others may update emerging-title verdicts |
| `career/11-tracks/phd-to-industry.md` | T0-50 (Research Engineer), T0-55 (Research Scientist) |
| `career/11-tracks/governance-careers.md` | T0-61 (Governance/Risk/Responsible AI) |
| `career/11-tracks/freelance-fractional.md` | T0-66 (Independent/Fractional/Contract) |

The session-to-role mapping:

| Session | Role(s) |
|---|---|
| T0-48 | AI Engineer |
| T0-49 | ML Engineer |
| T0-50 | Research Engineer |
| T0-51 | Forward-Deployed Engineer |
| T0-52 | Applied Scientist |
| T0-53 | Applied AI Engineer |
| T0-54 | AI Infrastructure Engineer |
| T0-55 | Research Scientist |
| T0-56 | Inference Engineer |
| T0-57 | Agentic AI Engineer |
| T0-58 | ML Platform Engineer |
| T0-59 | AI Product Manager |
| T0-60 | AI Evaluation Engineer, AI Security Engineer, AI Safety Researcher |
| T0-61 | AI Governance Lead, AI Risk Assurance Specialist, Responsible AI Engineer |
| T0-62 | AI Solutions Architect, AI Enablement Engineer, AI Product Engineer, Domain Evaluation Specialist |
| T0-63 | GPU Kernel Engineer |
| T0-64 | Physical AI Engineer |
| T0-65 | AI Engineering Manager, VP/Head of AI, Chief AI Officer, Fractional AI Leader |
| T0-66 | Independent AI Consultant, Fractional AI Leader |

### R9 Tracks, skills, market and onboarding (5 sessions)

**Sessions:** T0-67 (104 KB), T0-68 (126 KB), T0-69 (167 KB), T0-70 (77 KB), T0-71 (96 KB)

| Data file | From record types |
|---|---|
| `data/skills_ontology.json` | `skill_signal`, `measure` (momentum) |
| `data/posting_skill_shares.json` | New dated snapshot if T0-69 has posting-share measurements |
| `data/role_scores.json` | `measure` (demand from market pulse and transitions) |
| `data/tools.json` | `resource`, `tool` |

| Career page | What the sessions' narratives add |
|---|---|
| `career/11-tracks/career-transitions.md` | Routes for DevOps/SRE, PMs, IT-services engineers, students; week-by-week plans |
| `career/03-skills-and-tech/learning-roadmaps.md` | Course reviews, platform ratings, book recommendations, compute platforms |
| `career/03-skills-and-tech/skills-radar.md` | A measured "surging" ring from dated momentum series |
| `career/01-landscape/emerging-roles.md` | Emerging-title verdicts from momentum data |
| `career/01-landscape/market-overview.md` | 2026-11 market pulse: hiring trends, layoffs, funding |
| `career/01-landscape/employer-landscape.md` | Employer mix changes |
| `career/10-onboarding/first-90-days.md` | Role-specific onboarding, country-specific probation mechanics |
| `career/10-onboarding/growth-and-progression.md` | Growth and promotion paths |

### R2 Geography (11 sessions — highest infrastructure cost)

**Sessions:** T0-35 (609 KB), T0-36 (271 KB), T0-37 to T0-42 (6 visa dossiers, ~1,228 KB), T0-43 (135 KB), T0-44 (112 KB), T0-45 (229 KB)

R2 requires a **new data file** (`data/countries.json`), a schema, a ranking script and a generated country-ranking page. The method is described in the [README](README.md#reduce-steps-from-sessions-to-data-and-pages). File a decision record in [DECISIONS.md](../DECISIONS.md) before building (open decision in ROADMAP §6.9).

| Career page | What the sessions' narratives add |
|---|---|
| `career/11-tracks/visa-and-relocation.md` | The 6 visa dossiers total 1.2 MB. Create country sub-pages in `career/11-tracks/visa/` and keep the overview page for corridor comparison |
| `career/01-landscape/market-overview.md` | Country-level demand, city-tier analysis |
| `career/09-compensation/india-remote-tax.md` | Cross-border tax rules from T0-43 |
| `career/11-tracks/india-remote-playbook.md` | India city data, EOR analysis, cross-border compliance |
| `career/11-tracks/freelance-fractional.md` | Cross-border freelance compliance |

### R1 Credentials (5 of 7 sessions — partial)

**Sessions available:** T0-29, T0-30, T0-31, T0-32, T0-34 (~887 KB). **Deferred:** T0-28, T0-33 (run after 2026-12-05).

R1 has an **open decision** (ROADMAP §6.9): do credentials get their own data file or stay in the skills ontology? Read the R1 method in the [README](README.md#reduce-steps-from-sessions-to-data-and-pages). File a decision record before building.

| Career page | What the sessions' narratives add |
|---|---|
| `career/04-certifications/credential-roi.md` | Per-vendor deep dives, exam strategy, prep resources, renewal mechanics, overlap analysis, sequencing |
| `career/03-skills-and-tech/learning-roadmaps.md` | University programmes and India programmes as learning pathways |
| `career/11-tracks/governance-careers.md` | Governance/security/privacy credential paths |

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

## 5. Finish

- [ ] `python3 -B scripts/build_all.py` prints `PROBLEMS: 0`.
- [ ] After any script change: `python3 -B -m unittest discover -s scripts/tests`.
- [ ] Set the session's `status` to `integrated` in [catalogue.json](catalogue.json), and a reduce step's to `done` when it is complete; run `build_all.py` again so the tracker shows it.
- [ ] Add an entry under `## [Unreleased]` in [CHANGELOG.md](../../CHANGELOG.md).
- [ ] Update [ROADMAP.md](../../ROADMAP.md) if the session closes a build item or opens a new one.
