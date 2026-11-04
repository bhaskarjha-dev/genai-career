# Roadmap

> **Updated:** 2026-11-04 · **Architecture:** decision D-013 in [research/DECISIONS.md](research/DECISIONS.md) · **History:** [CHANGELOG.md](CHANGELOG.md)
> This page tracks what the repository covers, what is planned next, and the decisions that are still open. Evidence-grade conventions follow EGP-1.0.

---

## 1. Where the repository stands

**The question it answers:** is a person at point zero fully provided for? **Not yet.**

| Coverage | Lifecycle stages |
|---|---|
| **Covered well** | Role universe, role ranking and target order (stages 1–2); skills per role, including tools, posting keywords and a self-assessment (stage 3) |
| **Covered in part** | Job search: strategy, resume layers, resume variants and the concise skills matrix exist; the resume generator does not (stages 6–7) |
| **Evidence only** (research exists, guides not yet written) | Landscape, certifications, portfolio, networking, interviewing, compensation, onboarding and the tracks. Each stage README links its research sessions and findings in the meantime |

**The research is mostly in place.** The 22 sessions hold the evidence for nearly every missing guide ([findings registry](research/findings.md)). What's missing is turning that research into user-facing guides and tools.

---

## 2. The complete flow: what exists and what's missing at each stage

Stages follow D-001's 12-stage funnel, plus three stages D-001 lacks (marked +). The last column links each stage's folder.

| # | Stage: the person's question | What exists | What's missing | Research ready to use | Folder |
|---|---|---|---|---|---|
| 1 | Awareness: "What does the GenAI job market look like, globally and in India?" | Partial: master catalog §7–§8, the ranked catalog's India lens | A market and employer guide: labs, Big Tech, AI startups, GCCs, IT services; India platforms; a target-company list | T0-01, T0-02, T0-09, T0-17 | [01-landscape](career/01-landscape/README.md) |
| 2 | Exploration: "Which roles exist, and which are best?" | **Complete:** master catalog, ranked catalog, GenAI target roles | — | T0-01, T0-15, T0-16 | [02-roles](career/02-roles/README.md) |
| 2+ | Self-assessment and targeting: "Where am I, and what should I target?" | Partial: persona lenses, the 12-skill readiness rubric, the per-role self-assessment tables | **A targeting workbook:** rubric scores, tier placement, constraints (location, visa, pay floor, hours per week) → primary, adjacent and stretch rings | T0-06, T2-01, T0-08, T0-07 | [career/README.md](career/README.md) (Start Here) |
| 3 | Skills: "What do I lack?" | **Complete per role:** skills catalog, typed role inventories (tools, keywords, 0–3 self-assessment), vocabulary, resume matrix | A learning roadmap per family with time estimates; a personal gap-analysis workflow across several target roles | T0-06, T0-10, T0-03 | [03-skills-and-tech](career/03-skills-and-tech/README.md) |
| 4 | Credentials: "Is a certificate worth it?" | Partial: master §6.2, the T0-11 decision rule, the credentials table in the vocabulary | A short credential decision guide | T0-11 | [04-certifications](career/04-certifications/README.md) |
| 5 | Portfolio: "What should I build to prove it?" | Partial: proof lines per role, T0-13 standards, the 20 project archetypes and their coverage ([job-search strategy §2.6](career/06-job-search/job-search-strategy.md)) | **A project archetype catalog:** specs, rubric, repository anatomy PA-01–PA-12, minimal project sets per ring | T0-13, T0-05, T0-12, T0-14 | [05-portfolio](career/05-portfolio/README.md) |
| 5+ | Online presence: "What do recruiters find when they search?" | Missing | LinkedIn profile (headline, About, skills), GitHub profile, a portfolio site or blog, kept consistent with the universal resume | T0-12, T0-11, T0-04 | [07-networking](career/07-networking/README.md) |
| 6 | Discovery: "Where are the postings?" | Missing | Boards, aggregators, ATS boards and India platforms; alerts; target-company lists by family and tier | T0-10, T0-01, T0-09 | [06-job-search](career/06-job-search/README.md) |
| 7 | Application: "How do I apply well?" | Partial: resume strategy, concise matrix, role inventories | The L1–L3 layer update and a resume generator; an **application operating system**: tracker fields, daily and weekly rhythm, the one-company-per-cycle rule, a knockout-answer bank, a cover-letter policy | T0-04, T0-10 | [06-job-search](career/06-job-search/README.md) |
| 8 | Networking and channels: "How do I get referred?" | Missing (the largest lever) | A referral-ask playbook; hiring-manager outreach (T0-05: managers under two years in role, work email, no attachment, common ground + proof + ask); recruiters; communities and their rules; the OSS-to-hire route | T0-04, T0-05, T0-12 | [06-job-search](career/06-job-search/README.md), [07-networking](career/07-networking/README.md) |
| 9 | Interview prep: "How do I pass my track?" | Partial: interview lines per role, master §8.2 | **Prep packs per family:** design archetypes, coding, four STAR-AI stories (competencies C1–C4), company loops, AI-tool policies, take-homes | T0-14, T1-03, T0-10 | [08-interviewing](career/08-interviewing/README.md) |
| 10 | Execution: "How do I handle the day and the follow-up?" | Missing | A day-of checklist, follow-up, using feedback | T1-03 | [08-interviewing](career/08-interviewing/README.md) |
| 11 | Negotiation: "Is this offer good, and how do I push?" | Partial: pay facts in the catalogs | A negotiation playbook: benchmarks by role, tier and region; equity risk adjustment; offer diligence (T0-17 R5); scripts; India ESOP tax; timing several offers | T0-02, T0-17, T1-03, T0-07 | [09-compensation](career/09-compensation/README.md) |
| 12 | First 90 days | Missing | An expectation-gap and probation playbook | T0-09 | [10-onboarding](career/10-onboarding/README.md) |
| + | Running the search: "Am I on track, and what's broken?" | Missing (not in FAD) | A **candidate workbook** (targets, gaps, projects, resumes, pipeline, prep, offers); a weekly review; funnel metrics with thresholds (for example, no screens after 15 targeted applications points to positioning [D · T0-06]) | T0-04, T0-06, T0-10 | [career/README.md](career/README.md) + templates |
| Tracks | India remote and contracting, visa and relocation, transitions, PhD to industry, freelance and fractional, governance careers | Partial: facts in the catalogs | Track playbooks | T0-07, T0-08, T0-06, T0-18, T0-15 | [11-tracks](career/11-tracks/README.md) |

---

## 3. Phases

| Phase | Scope | Status |
|---|---|---|
| **1. Foundation** | Architecture v2 (D-013): the stage spine and folder READMEs, the Start Here page, front matter and its schema, the root `data/` layer, `AGENTS.md`, `llms.txt` and the manifest, the findings registry, the research index and errata, CI validation | **Done** (2026-11-04) |
| **2. Knowledge** | A knowledge page per stage, distilled from the findings and the sessions' detailed sections:<br>• a claims registry (`cNNNN` IDs, grade, three dates, expiry class, session line);<br>• guides cite claims by ID;<br>• an expiry scanner (tool statuses fall due 2027-01-21) | Next |
| **3. Guidance** | The FAD Milestone 1–3 guides, plus the P0 items in §4 | After phase 2 |
| **4. Hubs and catalogs** | One hub page per role (profile, rank, skills, resume block, interview track, pay); the ecosystem tool catalog (at least 35 tools; FAD gap A6); stage × persona and stage × tier indices | After phase 3 |
| **5. Research pipeline 2** | Job-description mining per role (30 or more dated postings; at least 95% recall), India job platforms, target-company lists, expiry re-verification; per-role deep dives only where gaps remain | When gaps demand it |

---

## 4. Build plan

Ordered by impact on hiring odds, then by dependency:

| Priority | Deliverable | Why | Depends on |
|---|---|---|---|
| **P0-1** | **Resume layer system:**<br>• add the L1 universal, L2 family and L3 role layers to the strategy and the data, with the decision table in the [job-search strategy](career/06-job-search/job-search-strategy.md) §2.5;<br>• write a generator that builds every layer from one tagged master inventory.<br>The per-role tools and keywords layer already exists in the role inventories | Makes a few dozen resumes maintainable | Resume matrix and role inventories (exist) |
| **P0-2** | **Proof-of-work plan:** the 20 project archetypes with specs and rubrics, the coverage map and the minimal project set per ring | Proof of work is the binding constraint | Project archetypes (exist as data), T0-13 |
| **P0-3** | **Channels and outreach playbook:** referrals, hiring-manager outreach, recruiters, communities, the OSS route | The largest measured lever (11–36×) | T0-04, T0-05, T0-12 |
| **P0-4** | **Targeting workbook and application operating system:** templates linked from the [Start Here](career/README.md) page, which exists | Gives the person a path and a daily rhythm | Target roles, resume system |
| **P1** | Interview prep packs per family; online-presence guide; discovery guide; learning roadmaps; negotiation playbook; visa constraints on targeting | Next most decision-relevant | P0 items |
| **P2** | Market and employer guide; credential guide; first-90-days playbook; track playbooks; a tool catalog | Context and later stages | — |

All P0 and P1 items synthesise existing sessions. Only three areas need new data:
- India job platforms (Naukri, Instahyre), which FAD lists as open question OQ2.
- Live target-company lists.
- Job-description mining per role, which would measure tool tiers (see [role-skill-inventories.md](career/03-skills-and-tech/role-skill-inventories.md) §5).

---

## 5. Maintenance calendar

| When | What |
|---|---|
| Every change | `python3 scripts/validate_docs.py` (CI runs it on every push) |
| By 2026-12-01 | JobsPipe recount for the ranks most likely to move: Applied Scientist, Research Engineer, AI PM, AI Solutions Architect |
| By 2027-01-21 | Re-verify tool and credential statuses (EGP-1.0 class V2; 90 days from 2026-10-23), then regenerate the skills docs |
| By 2027-01-31 | Scheduled review of the Phase 0 decisions (D-001 to D-012) |
| Quarterly | Expiry audit; re-verify a sample of claims; refresh the findings registry after any new session |

---

## 6. Open decisions

1. **Resume layers:** adopt the refined model (the counts in the [job-search strategy](career/06-job-search/job-search-strategy.md)) and build the generator? This is P0-1.
2. **Build order:** P0-1 → P0-2 → P0-3 → P0-4, or a different order?
3. **Static site:** stay GitHub-native Markdown (the current choice), or publish with MkDocs Material (T1-01 KF9) once the stage guides exist? The front matter and folder indexes already support either.
4. **Generic or personal:** keep the system generic for anyone, or also build a personal instance from one person's background, targets and constraints?
5. **Upstream errata:** apply the [ERRATA.md](research/ERRATA.md) corrections inside FAD and DECISIONS, or keep those records as written (the current choice) with status notes?
