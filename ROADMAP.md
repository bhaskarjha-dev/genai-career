# Roadmap

> **Updated:** 2026-11-19 · **Architecture:** decisions D-013 and D-015 to D-027 in [research/DECISIONS.md](research/DECISIONS.md) · **History:** [CHANGELOG.md](CHANGELOG.md)
> This page tracks what the repository covers, what is planned next, and the decisions that are still open. Evidence-grade conventions follow EGP-1.0.

---

## 1. Where the repository stands

**The question it answers:** is a person at point zero fully provided for? **Yes across every lifecycle stage (00 to 11), backed by 75 integrated research sessions (22 Phase 0, 2 Phase 3, 51 of 53 Research Pipeline 2), with named remaining gaps.** Every role has a hybrid hub combining generated scorecards with a full RP2 narrative dossier (D-023), the D-012 Hype Register checks 19 boom and doom claims against the evidence (`career/01-landscape/hype-register.md`), and four computed databases cover credentials (`data/credentials.json`), target employers (`data/target_employers.json`), countries (`data/countries.json`) and rated learning resources (`data/learning_resources.json`, D-027).

| Coverage | What |
|---|---|
| **Covered** | Every stage, 00 to 11: start-here tools (RP2-refreshed 9-route targeting workbook, glossary, **291-item tool catalog** with T0-10 4-Tier Data Hygiene policy), market/employer landscape, **95-employer target directory** + 7 sponsor registers & **D-012 Hype Register**, role universe (29 hybrid role hubs, **418 classified titles**, **4 E / 17 V / 7 W / 1 A**, role map, rankings, GenAI targets), skills (radar with 6th multi-signal momentum view, learning roadmaps, **60-item rated learning resources catalog D-027** [52 rated + 8 primary specs], agentic protocols, 29 typed inventories), credentials (**194-credential scored database** with remediated T0-34 hiring signals and `UNMEASURED_HIRING_SIGNAL_PRIOR = (2.5, 4.0, 5.5)` fix, ROI guide, credentials by role), portfolio standards (incl. T0-05 micro-audit OS & OSS commit map) & **21 archetypes**, job search (global & India boards, AI-mediated hiring & legal table, résumé strategy, ATS mechanics, operating system), networking (dedicated LinkedIn guide, online presence, communities, 17 fellowships & residencies, referrals & outreach), interviewing (**61-employer loop reference**, **161 practice prompts across 12 tracks** incl. `robot-learning`, multi-vendor API prices, behavioural calibration), compensation (global & India benchmarks incl. T0-65 leadership pay, negotiation, offer evaluation reflecting Anthropic `ANT` IPO, verified India remote tax), onboarding & growth, and 15 track playbooks including 33-country / **51-city** / 7-lens rankings (with Shanghai & harvested T0-36 Pass 1 Sydney/Numbeo data), remote/EOR guide, 6 regional visa dossiers and 9 researched transition routes |
| **Needs new research / deferred** | Deferred RP2 sessions **T0-28** (hyperscaler cloud exams) and **T0-33** (developer-tool & agentic-suite credentials), scheduled after 2026-12-05 (17 records in `data/credentials.json` carry `provisional_pending_rp2: true`); repeatable monthly job-description mining (INS-1) for two-date employer-demand skill series (JobsPipe's AI Engineer count date stayed at 2026-09-10 through 2026-11-14); logged-in India job-board counts (INS-5); role-specific India pay for 12 remaining IC Grade D placeholders; governance-track interview loops (Grade E); audited outcome data for GenAI courses/bootcamps (Grade E) |
| **Needs building** | Measurement instruments INS-1, INS-2, INS-4, INS-5; CI external link-check (`lychee`) & `markdownlint-cli2` wiring; 3-persona navigation pilot (`T1-01 O6`); a static site if chosen. Résumé building is out of scope: résumés are built in a personal career repository from this repository's inputs (D-022) |

**Quality caveat.** On 2026-11-06, 13 fact-checking agents audited 4,829 Phase 0 claims and logged errata U13–U26. On 2026-11-19, full sceptical integration of all 51 saved RP2 sessions (+ Phase 3 `T3-01`/`T3-02`) plus a 75-session end-to-end utilization audit audited every session for `Extract`-only Grade A violations (159 ledger rows / 55 JSONL records downgraded to Grade B unless live-verified), COI disclosures (792 rows), cross-session contradictions and downstream transcription defects, logging errata **U27–U60** in [research/ERRATA.md](research/ERRATA.md) and verifying load-bearing facts against primary government, issuer and employer pages. Before 1.0, CONTRIBUTING §7 requires an independent fact-check of the v0.1.0 reference documents (P1-5) and human domain-expert review of the compensation, tax, visa and interviewing guides (P1-4).

**Consolidation (2026-11-07 to 2026-11-19).** One owner per fact (D-019); generated `review_by` dates and weekly CI checks (D-020); generic scope (D-022); hybrid role hubs (D-023); computed target-employer, country, credential and learning-resource catalogs (D-024 to D-027); D-012 Hype Register & full T1-02 governance rubric in `CONTRIBUTING.md`; all **19 generators** wired into `scripts/build_all.py` with schema and regression tests in `scripts/tests/test_machinery.py`.

---

## 2. The complete flow: what exists at each stage

Stages follow D-001's 12-stage funnel, plus three stages D-001 lacks (marked +). [AGENTS.md](AGENTS.md) maps funnel stages to folders.

| # | Stage: the person's question | What exists | What's still missing | Folder |
|---|---|---|---|---|
| + | Start: "Where do I start, and what should I target?" | Targeting workbook (9 routes, RP2 worked example), glossary, **291-item tool catalog** (with 4-Tier Data Hygiene policy), personal gap analysis (`scripts/gap_analysis.py`) | — | [00-start](career/00-start/README.md) |
| 1 | Awareness: "What does the market look like, globally and in India?" | Market overview, employer landscape, **95-employer target directory** + 7 sponsor registers (`target-employers.md`), emerging roles, **Hype Register (`hype-register.md`, D-012)** | Monthly INS-1 refresh | [01-landscape](career/01-landscape/README.md) |
| 2 | Exploration: "Which roles exist, and which are best?" | Role map, 29 hybrid role hubs (scorecards + RP2 dossiers), master catalog (**418 titles**; 4 E / 17 V / 7 W / 1 A), ranked catalog, GenAI target roles | 2026-12-01 recount for quorum candidates | [02-roles](career/02-roles/README.md) |
| 3 | Skills: "What do I lack, and in what order do I learn it?" | Skills radar (5 computed rings + 6th multi-signal adoption/telemetry view), learning roadmaps, **60-item rated learning resources catalog (`learning-resources.md`, D-027)**, agentic protocols, 29 typed role inventories, vocabulary, skill maps | Two-date employer-demand JD series (INS-1; JobsPipe AI Engineer stayed at 2026-09-10) | [03-skills-and-tech](career/03-skills-and-tech/README.md) |
| 4 | Credentials: "Is a certificate worth it?" | **194-credential scored catalog (`credential-catalog.md`)**, credential ROI, credentials by role | Deferred sessions T0-28 (hyperscalers) and T0-33 (developer tools) after 2026-12-05 | [04-certifications](career/04-certifications/README.md) |
| 5 | Portfolio: "What should I build to prove it?" | Proof-of-work standards (GitHub, OSS map, micro-audit OS, writing, portfolio sites), **21 project archetype cards** | — | [05-portfolio](career/05-portfolio/README.md) |
| 5+ | Online presence: "What do recruiters find?" | Dedicated LinkedIn guide (`linkedin-guide.md`), online-presence guide | — | [07-networking](career/07-networking/README.md) |
| 6 | Discovery: "Where are the postings?" | Channels and boards (global + measured India boards, ghost jobs, pay transparency, scams), tool catalog | Logged-in India counts (INS-5) | [06-job-search](career/06-job-search/README.md) |
| 7 | Application: "How do I apply well?" | Job-search strategy, résumé strategy and matrix, ATS mechanics (AI-mediated hiring + anti-bot + V0 legal table) | — (résumés live in a personal career repository: D-022) | [06-job-search](career/06-job-search/README.md) |
| 8 | Networking: "How do I get referred?" | Referrals and outreach (outreach law, micro-audits, yield/hour), communities guide, **17 fellowships and residencies** (`fellowships-and-residencies.md`) | Community-to-job baseline (OQ4) | [07-networking](career/07-networking/README.md) |
| 9 | Interview preparation: "How do I pass my track?" | **61-employer loop reference (`employer-interview-loops.md`)**, system-design archetypes (5 Mermaid diagrams, calc equations, multi-vendor API pricing), behavioural calibration, coding rounds, prep packs (**161 prompts / 12 tracks**) | Governance-track employer loops (Grade E); remaining undocumented labs | [08-interviewing](career/08-interviewing/README.md) |
| 10 | Execution: "How do I handle the day and the follow-up?" | Interview loops (per-cell sourced, day-of, follow-up, debrief) | — | [08-interviewing](career/08-interviewing/README.md) |
| 11 | Negotiation: "Is this offer good, and how do I push?" | Pay benchmarks (global + India cities/GCC/startups + leadership), offer evaluation (Anthropic ANT IPO + equity risk), negotiation playbook, primary-verified India remote tax | 12 IC India Grade D pay placeholders; India/EU negotiation outcomes | [09-compensation](career/09-compensation/README.md) |
| 12 | First 90 days | First-90-days playbook (role-specific + country probation mechanics), growth and progression | Burnout/retention longitudinal data | [10-onboarding](career/10-onboarding/README.md) |
| + | Running the search: "Am I on track, and what's broken?" | Application operating system (tracker fields, Gem 14%–26% onsite conversion, thresholds) | — | [06-job-search](career/06-job-search/README.md) |
| Tracks | Backgrounds, locations, ways of working | 33-country / **51-city** / 7-lens rankings (`country-rankings.md`), remote & EOR guide (`remote-cross-border.md`), 6 regional visa dossiers (`visa/`), visa & relocation overview, 9 researched transition routes (`career-transitions.md`), PhD to industry, India remote playbook, freelance and fractional, governance careers | Continental Europe works-council negotiation data | [11-tracks](career/11-tracks/README.md) |

---

## 3. Phases

| Phase | Scope | Status |
|---|---|---|
| **1. Foundation** | Architecture v2 (D-013): stage spine, front matter, `data/`, `AGENTS.md`, `llms.txt`, manifest, findings registry, errata, CI | **Done** (2026-11-04) |
| **2. Knowledge** | Freshness tracking: page-level `review_by` dates and validator due report (D-017) | **Done** (2026-11-05) |
| **3. Guidance** | Core guides for every stage in the guide pattern (D-016) | **Done** (2026-11-05); human expert review pending |
| **4. Hubs and catalogs** | Role map (D-015), role hubs, skills radar, credentials by role, archetypes, prep packs, tool catalog | **Done** (2026-11-05) |
| **4b. Consolidation** | One owner per fact (D-019); generated review dates & weekly CI (D-020); schema/validator hardening; generic scope (D-022) | **Done** (2026-11-10) |
| **5. Research pipeline 2** | 53 targeted sessions (D-021), 9 reduce steps, Decisions D-023 to D-027, 4 new computed databases/generators, 29 hybrid role hubs, 15 new career pages (including `hype-register.md` and `learning-resources.md`), errata U27–U60 | **51 of 53 sessions integrated; 8 of 9 reduce steps done; 75-session utilization audit complete** (2026-11-19). Remaining: T0-28 & T0-33 (deferred past 2026-12-05) to complete R1 |
| **6. Release 1.0** | Independent fact-check of v0.1.0 reference documents (P1-5) and paths/IDs/schemas declared stable (CONTRIBUTING §7); human expert review recommended first (P1-4) | Next major milestone after T0-28/T0-33 and P1-5 |

---

## 4. Build plan

Ordered by impact on hiring odds, then by dependency:

| Priority | Deliverable | Status / Why | Depends on |
|---|---|---|---|
| **P0-2** | **Finish deferred RP2 sessions T0-28 & T0-33** ([tracker](research/pipeline-2/README.md)) | **51/53 integrated (2026-11-19).** Run T0-28 (AWS/GCP/Azure exams) and T0-33 (developer tools/agentic suites) after 2026-12-05 to resolve the 17 provisional records in `data/credentials.json` and close R1 | Vendor announcements (post-2026-12-05) |
| **P1-1** | **Job-description mining (two-date skill demand series):** 30+ dated full-text postings per role from public ATS boards; promote measured tools from [S]/[P] to [JD] and add a posting-demand momentum ring | **Partially done (2026-11-19):** role dossiers T0-48 to T0-66 integrated and T0-69 added a multi-signal adoption/telemetry/governance ring (Ring 6 on `skills-radar.md`), but **no two-date employer-posting-share series exists yet** (JobsPipe AI Engineer stayed at 2026-09-10) | P1-7 (INS-1) |
| **P1-2** | **India job platforms** (Naukri, Instahyre, Cutshort, Wellfound, Hirist; FAD OQ2) | **Done for RP2 scope (2026-11-19):** T0-25 and T0-45 integrated into `channels-and-boards.md` and `india-remote-playbook.md`. Remaining: owner's monthly logged-in counts (INS-5) | INS-5 |
| **P1-3** | **Four more starting backgrounds:** DevOps/SRE, product managers, IT-services engineers, students and new graduates | **Done (2026-11-19):** T0-67 integrated into `career/11-tracks/career-transitions.md` (9 researched routes total) | — |
| **P1-4** | **Human expert review** of the stage guides, starting with compensation, tax, visa and interviewing | Open — guides were agent-drafted and agent-verified (including live primary checks on 2026-11-19) | — |
| **P1-5** | **Independent fact-check of the v0.1.0 reference documents:** role catalog, rankings, skill maps and ontology links | Open — CONTRIBUTING §7 requires it before 1.0 | — |
| **P1-6** | **Integrate research pipeline 2 by reduce step** (R1–R9) | **8 of 9 reduce steps done (2026-11-19):** R2–R9 complete; R1 complete for 5/7 saved sessions + T3-01/T3-02 (pending T0-28 & T0-33 after 2026-12-05) | P0-2 (T0-28, T0-33) |
| **P1-7** | **Job-description collector** (instrument INS-1, planned `scripts/collect_jds.py`): monthly full-text ATS snapshots from `data/target_employers.json` (95 employers), skill extraction via ontology aliases, n>=60 per role | Open — turns small/excerpt-heavy RP2 samples (T0-48/50/51/53/57/60) into repeatable full-text measurement | `data/target_employers.json` (ready) |
| **P2** | **Official-register script** (instrument INS-2): AI-title filings from US DOL LCA, UK sponsor register and NL IND | Open — sponsorship counts for country rankings and target employers | — |
| **P2** | **Net-pay calculator** (instrument INS-4): effective tax and social contributions from official schedules across 33 countries | Open — removes recalled Grade D tax models in T0-35/T0-36 (FR, FI, SE, TW, NZ, MY, etc.) | `data/countries.json` (ready) |
| **P2** | **Logged-in platform counts** (instrument INS-5): monthly owner queries on Naukri, Instahyre, LinkedIn | Open — India demand evidence agents cannot fetch signed out | Owner runs monthly |
| **P2** | **Tool-choice cards** (stage 03): `compare` fields per choose-one class in `data/skills_ontology.json` | Open | Skills ontology |
| **P2** | **Research-track concept checklist** (stage 11) | Open | Skills ontology |
| **P2** | **Finish one owner per fact (D-019):** `targeting-workbook.md` refreshed against Nov 2026 hubs and 9 routes (**Done 2026-11-19**); remaining: trim copied prose in `role-rankings.md` §5.2–§5.3 | Partially done (2026-11-19) | — |
| **P2** | **Ontology clean-up (remainder):** Physical AI duplicates (`perception`→`computer_vision`, `vla_models`→`robot_learning`) **Done (2026-11-19)**; remaining: collapse AI Engineer's Optional tools into choose-one classes and deduplicate the three governance entries in skills-radar ring 2 | Partially done (2026-11-19) | Skills ontology |
| **P2** | **CI hygiene & navigation pilot (`T1-01 O6`, `T1-02 §10.12`):** wire weekly `lychee` external link-check (excluding banned `archive.today` hosts per `AC5`) and `markdownlint-cli2` in CI; run a 3-persona navigation pilot before 1.0 | Open | — |
| **P2** | **Leadership hubs & static site:** collapse empty sections on the 5 leadership hubs in `build_role_hubs.py`; evaluate static-site generator (see §6 item 3); claims registry if `review_by` exceeds 25 due pages | Open | Decisions in §6 |

---

## 5. Maintenance calendar

Every volatile page carries a `review_by` date under EGP-1.0 classes (V0 = 14d, V1 = 31d, V2 = 90d, V3 = 180d); `scripts/validate_docs.py` reports any due page and the weekly `due-report` CI workflow fails while any page is due (D-020).

| When | What |
|---|---|
| Every change | `python3 -B scripts/build_all.py` (all 19 generators + validator) and, after script changes, `python3 -B -m unittest discover -s scripts/tests` |
| Mondays (CI) | Weekly `due-report` workflow runs `validate_docs.py --strict` |
| Quarterly (EGP-1.0) | Stratified random audit of **n = 59** live claims (`T1-02 §10.13.3`, ≤4.95% 95% defect upper bound at 0 defects; widen to 299 on any defect) plus **n = 20** rejected/demoted claims (`CONTRIBUTING.md` §6) |
| By 2026-11-30 | OpenAI hosted Evals platform shutdown (confirmed 2026-11-19); check whether replacement eval tooling changes `tool-catalog.md` or `system-design-archetypes.md` |
| By 2026-12-01 to 2026-12-03 | **V0 14-day checks (2026-12-03):** `visa-and-relocation.md` + 6 regional visa dossiers (US $100k H-1B appeals, Dec 2026 Visa Bulletin, UK Earned Settlement Rules, NL 30% ruling floor €48,013 vs €46,107 `ERRATA U57` on `belastingdienst.nl` & *Belastingplan 2027* Senate, AU/NZ/SG/MY/DE 2027 rules), `ats-mechanics.md` (*Mobley v. Workday*, *Kistler v. Eightfold*, CO SB 26-189 / *xAI v. Weiser*), `governance-careers.md`, `hype-register.md` (HR-018, H-1B fee status), `offer-evaluation.md` (Anthropic `ANT` post-IPO lock-ups, OpenAI S-1), `credential-catalog.md` (NVIDIA NCP-GENL/AAI Certiverse booking, Anthropic DoW FASCSA rehearing). **2026-12-01 catalog recount:** check if JobsPipe title & skill-share pages refreshed past 2026-09-10 / 2026-10-19; test graduation candidates **Research Engineer** (V→E), **AI Security Engineer** (W→E/V), **AI PM**, **AI Solutions Architect**, **AI Developer Advocate**, **Edge AI Engineer**, **Distributed Training Engineer** |
| After 2026-12-05 | Run deferred RP2 sessions **T0-28** (hyperscaler cloud exams) and **T0-33** (developer tools/agentic suites), resolve 17 provisional records in `data/credentials.json`, mark R1 `done` |
| By 2026-12-06 to 2026-12-20 | **V1 31-day checks:** Skillenai-linked pages (`role-catalog.md`, `role-rankings.md`, `genai-target-roles.md`, `agentic-protocols.md`, `agentic-ai-engineer`, `ai-enablement-engineer`, `ai-security-engineer` hubs due 2026-12-06); Fast AI Jobs / JobsPipe-linked hubs and market/board pages due 2026-12-13 to 2026-12-20; `tool-catalog.md` due 2026-12-22 (its oldest tool reading is dated 2026-09-23) |
| By 2027-01-14 to 2027-02-17 | **Q1 2027 wave & V2 90-day refresh (2027-02-17):** AWS MLA-C02 GA (2027-01-14), AWS AIB-C01 early-adopter cut-off (`2027-02-15`), NL 30%→27% ruling & SG EP S$6,000 (`2027-01-01`), SG Tech.Pass close (`2027-01-27`) & ONE Pass AI/Tech track (`2027-01-28`), tool/credential/learning-resource/pay V2 re-verification (`data/skills_ontology.json`, `data/tools.json`, `data/credentials.json`, `data/learning_resources.json`, `pay-benchmarks.md`, `country-rankings.md`, `india-remote-tax.md`, `hype-register.md`); Phase 0 decisions review (`2027-01-31`, including `T0-01` Objection 7 share-of-corpus quorum floor for D-002) |
| By 2027-05-01 to 2027-05-13 | Posting-term shares (V3, 2027-05-01); India DPDP Rules Phase 3 full enforcement (2027-05-13); D-013 to D-027 scheduled reviews |

---

## 6. Open decisions

1. **Résumé generator (P0-1): closed on 2026-11-10 by D-022.** Résumés live in a personal career repository.
2. **Research pipeline 2 order: mostly closed (2026-11-19).** 51 of 53 sessions are integrated; only T0-28 and T0-33 remain after 2026-12-05.
3. **Static site:** stay GitHub-native Markdown (adopted choice) or publish via a static-site generator — note `T1-01 KF9`'s caveat on MkDocs Material maintenance overhead vs evaluating Astro Starlight in Q2 2027.
4. **Generic or personal: closed on 2026-11-10 by D-022.**
5. **Claims registry:** keep page-level `review_by` dates (D-017, D-020), or add per-claim IDs if weekly due reports exceed 25 pages at once.
6. **Upstream errata:** keep sealed Phase 0 / RP2 records immutable with [research/ERRATA.md](research/ERRATA.md) (adopted choice) rather than editing sessions.
7. **Human review of accepted decisions D-019 to D-027:** D-019 (one owner per fact), D-020 (generated review dates), D-021 (RP2), D-022 (generic scope), **D-023** (hybrid role hubs), **D-024** (`data/target_employers.json`), **D-025** (`data/countries.json` + 6 visa dossiers + `remote-cross-border.md`), **D-026** (`data/credentials.json` + `rank_credentials.py`) and **D-027** (`data/learning_resources.json` + `build_learning_resources.py`) all carry `status: accepted`, `human_reviewed: false`.
8. **A code licence for `scripts/`:** MIT or Apache-2.0 alongside CC BY-SA 4.0 for content.
9. **Data shapes for RP2 rankings: closed on 2026-11-19 by D-024, D-025, D-026 and D-027** (separate `data/target_employers.json`, `data/countries.json`, `data/credentials.json`, and `data/learning_resources.json`).

---

## 7. Known issues and follow-ups

Updated on 2026-11-19 after sceptical integration of all 51 saved RP2 sessions and the 75-session utilization audit. Confirmed errors from Phase 0, Phase 3 (`T3-02`) and RP2 are logged in [research/ERRATA.md](research/ERRATA.md) (`U1`–`U60`).

**Resolved items from the 2026-11-06 / 2026-11-07 list (closed 2026-11-19):**
- `T1-03 F4 vs L211` (Google behavioural veto): closed via T0-46 K3 (Google HC weighs variance and can downlevel; Amazon Bar Raiser and Anthropic values hold strict vetoes).
- `T0-14 L553 vs T1-03 F6` (Meta AI coding vs design round): closed via T0-46 K4 (Meta runs two distinct AI-enabled rounds: a 60-min CoderPad AI-assisted coding round piloted Oct 2025 AND a 2026 agentic design round).
- `interview-loops.md` umbrella C attribution: closed by per-cell sourcing across `interview-loops.md` and `employer-interview-loops.md`.
- `system-design-archetypes.md` unverified OpenAI/Google API prices: closed via T0-46 §7 multi-vendor API pricing table.
- `india-remote-tax.md` primary-source check of Income-tax Act 2025 sections & FEMA 2026 Regulations: closed via T0-43 + live verification (s.58, s.62(4), s.63, s.408, s.124, FEMA 2026 Reg. 3/4/5, EPFO S.O. 5109(E)).
- `OMB M-25-21` missing issue date: closed (issued 2025-04-03, primary White House PDF, Grade A; logged in ERRATA U43).
- `credential-roi.md` partner-credit wording: closed (T0-11 L435 + 2026 partner rules).
- Physical AI duplicate skills (`perception`, `vla_models`): closed (merged into `computer_vision` and `robot_learning`).
- `T2-01 L153` vs `T0-06 D2` gate-scaling reconciliation: closed on 2026-11-19 in `career/00-start/targeting-workbook.md` (adopts `T0-06 D2` effective-hours scaling for solo build gates while noting `T2-01`'s coarse ×1.5 / ×0.5 rule for externally gated steps).
- False missing-city claim in `T0-36`: closed on 2026-11-19 (ERRATA U58 — Pass 1 JSONL inside `T0-36` contained Greater Sydney ML pay `A$169,370` plus Numbeo rents for Abu Dhabi, Auckland, Melbourne and Manama; harvested into `data/countries.json`).

**Remaining unconfirmed candidate errata and cross-session conflicts:**

| Location | Reported conflict or issue | Where the guides stand |
|---|---|---|
| `T0-35 L268` vs `T0-39 L666, L1582` | Netherlands 2026 30%-ruling taxable-salary floor is **€48,013** (T0-35) vs **€46,107** (T0-39), both secondary [B] (ERRATA U57) | Flagged V0 in `country-rankings.md` and `glossary.md`; verify directly on `belastingdienst.nl` |
| `T0-53 L221` vs `T0-44 L113` | Applied AI Engineer US Levels.fyi P90 is **$505K** (T0-53, 2026-11-11) vs **$605K** (T0-44, 2026-11-13 extract) | `pay-benchmarks.md` and `data/role_scores.json` report the reconciled **$505,000–$605,000** spread |
| `T0-49 L239` vs `T0-02 L232` | Meta E6 MLE TC on Levels.fyi is **$660K** (T0-49 extract) vs **$782K** (T0-02) | `pay-benchmarks.md` and `ml-engineer` hub report the **$660K–$790K** band |
| `T0-34` ISACA AAIR fees & `T3-01` GitHub GH-300/600 validity | ISACA AAIR maintenance fee conflicts ($45/$85 vs $20/$35 across ISACA pages); GH-300/600 validity conflicts between annual free Microsoft Learn renewal and 2 years; GCP PMLE validity 2 vs 3 years | Flagged in `credential-catalog.md`; resolve in T0-28 / T0-33 |
| `T0-67 L59` & `T0-67` NACE | TCS FY26 fresher hiring (>25,000 offers on earnings call vs 44,000 onboarded in secondary press); NACE Class of 2026 AI-skill demand 10.5% vs 17.5% across chart/prose | Both ranges disclosed in `career-transitions.md` |
| `T0-02 F3/F5`, `T0-06 L130/L387`, `T0-03 KF2 vs L179`, `T0-18 F1 vs L196`, `T0-07 L229` | Minor Phase 0 internal discrepancies retained from 2026-11-06 fact-check | Pages already apply conservative/reconciled readings |

**RP2 low-Read-rate session caveats (re-verify via primary reads / INS-1 at next refresh):**
- Six RP2 sessions opened ≤12% of their cited sources in full: **T0-68** (2%, 2/98), **T0-43** (6%, 9/141), **T0-36** (9%, 19/218), **T0-67** (9%, 7/75), **T0-60** (10%, 10/98), **T0-57** (11%, 6/57), and **T0-47** (12%, 10/85). Load-bearing figures were live-verified on 2026-11-19 and all un-opened Extract-only Grade A claims were downgraded to Grade B (ERRATA U49), while small-`n` / excerpt-heavy JD counts (`n=10–36`) were held on the watchlist rather than overturning ontology tiers.

**Persistent Grade E evidence absences (after RP2):**
- **Skills & demand:** two-date employer-posting-share series for any GenAI skill (JobsPipe AI Engineer stayed at 2026-09-10); Big Tech direct ATS scrape (Google, Meta, Apple, Amazon, Microsoft blocked automated fetches in T0-48/49/57).
- **Compensation & negotiation:** 19 of 21 India role-level Grade D pay placeholders remain unmeasured; no US pay dataset for Inference, Agentic, AI PM or roles 13–24; zero measured India negotiation outcomes, switch-hike distributions or Continental Europe works-council negotiation data; no worker-side pay distribution for foreign-band remote roles paid into India.
- **Interviewing:** governance-track employer interview loops (0 retrieved sources); 7 frontier labs without documented loops (Mistral, Cohere, Microsoft AI, Thinking Machines, SSI, Sakana, Poolside).
- **Learning & credentials:** zero independent audited outcome studies for any GenAI-specific course or bootcamp (T0-68 KF1); deferred hyperscaler (T0-28) and developer-tool (T0-33) censuses.
- **Tax & visa primary gaps:** Income-tax Rules 2026 exact ITR/Form 67 numbers and bank step-by-step EDF workflows; Payoneer final RBI PA-CB CoA; bot-blocked primary texts in T0-39 (NL/FR), T0-40 (PT AIMA) and T0-41 (SA `pr.gov.sa`, QA Hukoomi, IL PIBA Procedure 5.3.0043 post-2026-03-01 spouse EAS); Numbeo post-2024 rents genuinely absent for **Boston, Pune, Delhi NCR, Chennai and Beijing** (Abu Dhabi, Auckland, Melbourne and Manama were harvested from `T0-36` Pass 1 JSONL per ERRATA U58); recalled Grade D tax schedules in T0-35/T0-36 (close via INS-4).

**Grading edge cases & remaining housekeeping:**
- **Other platform aggregates:** Decide whether Forge, Carta, Pave and Levels.fyi `.md` exports (which showed unit/currency glitches in Apr–Jul 2026 captures) should formally join D-018's Grade B list.
- **FAD open questions:** OQ3 (inter-rater EGP-1.0 reliability pilot on 50 claims), OQ4 (community-to-job conversion baseline), OQ6 (formal AI-contribution policy in CONTRIBUTING).
- **Session-ID namespace:** widen `T#-##` patterns across scripts and schemas before `T0-99`.
- **Tooling:** port the figure-to-citation verifier and `check_prose_refs.py` into `scripts/` (P2).
