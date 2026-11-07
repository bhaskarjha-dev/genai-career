# Roadmap

> **Updated:** 2026-11-07 · **Architecture:** decisions D-013 and D-015 to D-018 in [research/DECISIONS.md](research/DECISIONS.md) · **History:** [CHANGELOG.md](CHANGELOG.md)
> This page tracks what the repository covers, what is planned next, and the decisions that are still open. Evidence-grade conventions follow EGP-1.0.

---

## 1. Where the repository stands

**The question it answers:** is a person at point zero fully provided for? **Yes for every lifecycle stage, with named gaps.** Each stage has its core guides, and the gaps below are listed where readers meet them.

| Coverage | What |
|---|---|
| **Covered** | Every stage, 00 to 11: start-here tools (targeting workbook, glossary, tool catalog), the market and employers, the role universe with a role map and one hub per role, skills with a radar and learning roadmaps, credentials, proof of work with project cards, job search, networking, interviewing with prep packs, compensation, onboarding and growth, and six track playbooks |
| **Needs new research** | Measured tool tiers and skill momentum (job-description mining); India job platforms (FAD OQ2); research-backed routes for DevOps/SRE engineers, product managers and students (provisional [P] routes exist); live target-company lists; remote pay bands and Europe depth; burnout and sustainable pace |
| **Needs building** | The résumé generator (P0-1); a static site, if chosen |

**Quality caveat.** AI agents drafted the stage guides from the research sessions on 2026-11-05 and 2026-11-06. On 2026-11-06, 13 independent fact-checking agents checked 4,829 claims against the session lines they cite and made 234 fixes, and a script confirmed that the figures on each line appear near the line it cites. Before 1.0, CONTRIBUTING §7 requires an independent fact-check of the reference documents: the pages added on 2026-11-05 and 2026-11-06 had the agent fact-check above, and the v0.1.0 catalogs and skills references still need one (P1-5). No human domain expert has reviewed the guides yet; that is recommended before readers rely on the compensation, tax, visa and interviewing pages (P1-4). The work also logged errata U13–U26 against the Phase 0 records.

---

## 2. The complete flow: what exists at each stage

Stages follow D-001's 12-stage funnel, plus three stages D-001 lacks (marked +). [AGENTS.md](AGENTS.md) maps funnel stages to folders.

| # | Stage: the person's question | What exists | What's still missing | Folder |
|---|---|---|---|---|
| + | Start: "Where do I start, and what should I target?" | Targeting workbook (self-assessment, constraints, rings, 90-day plan), glossary, tool catalog, personal gap analysis (`scripts/gap_analysis.py`) | — | [00-start](career/00-start/README.md) |
| 1 | Awareness: "What does the market look like, globally and in India?" | Market overview, employer landscape, emerging roles | India job platforms; target-company lists | [01-landscape](career/01-landscape/README.md) |
| 2 | Exploration: "Which roles exist, and which are best?" | Role map, role hubs, master catalog, ranked catalog, GenAI target roles | — | [02-roles](career/02-roles/README.md) |
| 3 | Skills: "What do I lack, and in what order do I learn it?" | Skills radar, learning roadmaps, agentic protocols, typed role inventories, vocabulary, skill maps | Measured tool tiers and a "surging" ring (job-description mining) | [03-skills-and-tech](career/03-skills-and-tech/README.md) |
| 4 | Credentials: "Is a certificate worth it?" | Credential ROI, credentials by role | — | [04-certifications](career/04-certifications/README.md) |
| 5 | Portfolio: "What should I build to prove it?" | Proof-of-work standards, project archetype cards with minimal sets | — | [05-portfolio](career/05-portfolio/README.md) |
| 5+ | Online presence: "What do recruiters find?" | Online-presence guide | — | [07-networking](career/07-networking/README.md) |
| 6 | Discovery: "Where are the postings?" | Channels and boards, tool catalog | India platforms (stated as a gap in the guide) | [06-job-search](career/06-job-search/README.md) |
| 7 | Application: "How do I apply well?" | Job-search strategy, résumé strategy and matrix, ATS mechanics | The résumé generator (P0-1) | [06-job-search](career/06-job-search/README.md) |
| 8 | Networking: "How do I get referred?" | Referrals and outreach (with the open-source route), communities guide | — | [07-networking](career/07-networking/README.md) |
| 9 | Interview preparation: "How do I pass my track?" | System-design archetypes, behavioural calibration, coding rounds, prep packs | — | [08-interviewing](career/08-interviewing/README.md) |
| 10 | Execution: "How do I handle the day and the follow-up?" | Interview loops (classification, day-of, follow-up, debrief) | — | [08-interviewing](career/08-interviewing/README.md) |
| 11 | Negotiation: "Is this offer good, and how do I push?" | Pay benchmarks, offer evaluation, negotiation playbook, India remote tax | India and Europe negotiation evidence is thin (stated in the guide) | [09-compensation](career/09-compensation/README.md) |
| 12 | First 90 days | First-90-days playbook, growth and progression | — | [10-onboarding](career/10-onboarding/README.md) |
| + | Running the search: "Am I on track, and what's broken?" | Application operating system (tracker, rhythm, funnel thresholds) | — | [06-job-search](career/06-job-search/README.md) |
| Tracks | Backgrounds, locations, ways of working | Career transitions, PhD to industry, India remote playbook, visa and relocation, freelance and fractional, governance careers | Research for DevOps/SRE, PM and student routes | [11-tracks](career/11-tracks/README.md) |

---

## 3. Phases

| Phase | Scope | Status |
|---|---|---|
| **1. Foundation** | Architecture v2 (D-013): the stage spine and folder READMEs, the Start Here page, front matter and its schema, the root `data/` layer, `AGENTS.md`, `llms.txt` and the manifest, the findings registry, the research index and errata, CI validation | **Done** (2026-11-04) |
| **2. Knowledge** | Freshness tracking: page-level `review_by` dates and the validator's due report (D-017) replace the planned claims registry for now | **Done** (2026-11-05) |
| **3. Guidance** | The core guides for every stage, in the guide pattern (D-016) | **Done** (2026-11-05); human expert review pending |
| **4. Hubs and catalogs** | The role map (D-015) and one hub per role; the skills radar, credentials by role, project archetype cards, prep packs and the tool catalog, all generated from `data/` | **Done** (2026-11-05). Persona and situation routing lives in [Start Here](career/README.md) (§1 and §6), so no separate stage × persona index was built. A stage × tier index is deferred: the tier bands are contested ([ERRATA](research/ERRATA.md) U14) |
| **5. Research pipeline 2** | Job-description mining per role (30 or more dated postings; at least 95% recall); India job platforms; transitions for DevOps/SRE, PM and students; target-company lists; expiry re-verification | **Next** |
| **6. Release 1.0** | An independent fact-check of the reference documents (P1-5) and paths, IDs and schemas declared stable (CONTRIBUTING §7); a human expert review of the guides is recommended first (P1-4) | After phase 5, or earlier once the fact-check is done |

---

## 4. Build plan

Ordered by impact on hiring odds, then by dependency:

| Priority | Deliverable | Why | Depends on |
|---|---|---|---|
| **P0-1** | **Résumé generator:** build the universal, family and role résumés from one tagged personal inventory kept in `personal/` (git-ignored), following the layers in the [job-search strategy](career/06-job-search/job-search-strategy.md) §2.5. Include a section-order skeleton for a one- to two-page résumé, and a per-role bank of evidence lines keyed to each role's Must and Important skills, with the X-Y-Z pattern as an optional [P] form ([ATS mechanics](career/06-job-search/ats-mechanics.md)) | Makes a few dozen résumés maintainable | Résumé matrix and role inventories (exist) |
| **P1-1** | **Job-description mining:** 30 or more dated postings per role from public ATS boards; promote measured tools from [S] or [P] to [JD]; add a "surging" ring to the skills radar from dated series | Tool tiers outside a dozen measured titles rest on session mentions and practice curation | Research pipeline 2 |
| **P1-2** | **India job platforms** (Naukri, Instahyre and others; FAD OQ2) | The channels guide and the India playbook state the gap | A new session |
| **P1-3** | **Three more starting backgrounds:** DevOps/SRE, product managers, students and new graduates | Their routes in career transitions are provisional [P] | A new session |
| **P1-4** | **Human expert review** of the stage guides, starting with compensation, tax, visa and interviewing | The guides were agent-drafted and agent-checked | — |
| **P1-5** | **Independent fact-check of the v0.1.0 reference documents:** the role catalog, rankings and skill maps, and the 1,529 tiered skill links in the ontology. The planned agent check was blocked on 2026-11-04 ([role skill inventories §4](career/03-skills-and-tech/role-skill-inventories.md#4-verification)) | CONTRIBUTING §7 requires it before 1.0 | — |
| **P2** | **Tool-choice cards** (stage 03): for each choose-one class in the skills ontology (serving engines, eval runners, tracing and agent orchestration first), a sourced default and if → then rules, stored as `compare` fields and rendered in [skills vocabulary §2](career/03-skills-and-tech/skills-vocabulary.md#2-choose-one-classes). Start from T0-03's risk-aware tool selection policy (§4.2, L139–147) and its devaluation table (§6.8.2) | Readers choosing between interchangeable tools get a sourced default, not just a list | Skills ontology |
| **P2** | **Research-track concept checklist** (stage 11): the concepts research-engineer and research-scientist loops probe, as a self-check list built from the research family's Must and Important skills and T0-06 D8, pointing to primary references rather than teaching them. Until then, the research role inventories' self-assessment tables and the [skills radar](career/03-skills-and-tech/skills-radar.md) family C view cover it | Completes the PhD and research path | Skills ontology |
| **P2** | Migrate the three guides that predate the guide pattern (GenAI target roles, job-search strategy, résumé strategy); target-company lists; learning-resource curation with a rating method (no GenAI course or bootcamp has outcome data that is not vendor-reported, T0-06 L203); a claims registry if page-level `review_by` proves too coarse (D-017); a static site | Context and convenience | Decisions in §6 |

---

## 5. Maintenance calendar

| When | What |
|---|---|
| Every change | `python3 -B scripts/validate_docs.py` (CI runs it on every push); it lists pages past their `review_by` date |
| As listed by the validator | Re-verify each page whose `review_by` date has passed. On 2026-11-06 two pages are already due: visa and relocation (visa statuses, EGP-1.0 class V0) and the market overview (its S09 pay snapshot) |
| By 2026-11-14 to 2026-11-23 | Posting counts and indices taken in October 2026 pass their 31-day TTL (class V1): agentic protocols (2026-11-14), the employer landscape and channels and boards (2026-11-19); regulatory and tax statuses follow (2026-11-21 to 2026-11-23) |
| By 2026-11-21 | India remote tax: besides the statuses, check the export-of-services rules under FEMA and the Income-tax Act 2025 section numbers (s.58, s.62(4), s.63) against the primary texts, which T0-07 did not open (§7) |
| By 2026-12-01 | JobsPipe recount for the ranks most likely to move: Applied Scientist, Research Engineer, AI PM, AI Solutions Architect |
| By 2027-01-17 | Re-verify pay figures (90 days from the T0-02 measurement date of 2026-10-19) |
| By 2027-01-21 | Re-verify tool, protocol and credential statuses (EGP-1.0 class V2; 90 days from 2026-10-23), then regenerate the skills docs, the radar, credentials by role and the tool catalog |
| By 2027-01-31 | Scheduled review of the Phase 0 decisions (D-001 to D-012) |
| By 2027-05-04 | Scheduled review of D-013 to D-017 |
| By 2027-05-06 | Scheduled review of D-018 |
| Quarterly | Re-verify a sample of claims; refresh the findings registry after any new session |

---

## 6. Open decisions

1. **Résumé generator (P0-1):** build it now, with the personal inventory under `personal/` (git-ignored)?
2. **Research pipeline 2 scope:** which first: job-description mining, India platforms, or the three new backgrounds?
3. **Static site:** stay GitHub-native Markdown (the current choice), or publish with MkDocs Material (T1-01 KF9)? The front matter and folder indexes already support either.
4. **Generic or personal:** keep the system generic for anyone, or also build a personal instance from one person's background, targets and constraints? `scripts/gap_analysis.py` is the first personal tool.
5. **Claims registry:** keep page-level `review_by` dates (D-017), or add per-claim IDs with their own expiry once the guides stabilise?
6. **Upstream errata:** apply the [ERRATA.md](research/ERRATA.md) corrections inside FAD and DECISIONS, or keep those records as written (the current choice) with status notes?

---

## 7. Known issues and follow-ups

Found during the 2026-11-06 fact-check and not yet resolved. Line numbers are as of 2026-11-06.

**Candidate errata in the sealed records.** Reported by the fact-checkers but not yet confirmed. Verify each against the session, then log confirmed ones in [research/ERRATA.md](research/ERRATA.md):

| Location | Reported issue | Where the guides stand |
|---|---|---|
| T0-02 F3 and F5 | The findings say Grade A, but the session's source ledger grades the underlying sources (S13, S15, S49) as B search excerpts | Pages grade these figures B (D-018) |
| T0-06 L130 against L152 and L808 | L152 and L808 call data scientists a top-two feeder on both LinkedIn lists; L130 lists them third on the 2025 list | Not quoted as a ranking |
| T0-06 L387 | The 1.4–3.7-month range leaves out the zero-code route (4.6 months) | Not quoted |
| T0-03 KF2 against L179 and L419 | KF2 says the top-band job descriptions read were J1–J8; L179 and L419 say 0 of 10 top-band lab job descriptions | The market overview follows L179 |
| T0-18 F1 (L89) against L196 | The fractional CTO second-read ask is $209–212 in F1 and $210 in the table | The freelance guide follows F1 |
| T0-07 L229 | ₹49.91L ÷ ₹75L is 66.5%, printed as 66.6% | Immaterial; India remote tax copies the session |
| T1-03 F4 against L211 | F4 calls a Google behavioural No Hire a near-automatic veto; the firm table says the hiring committee may downlevel instead | Behavioural calibration reports both |
| T0-14 L553 and L826 against T1-03 F6 | T0-14 records Meta's spring 2026 AI-enabled round as a design round; T1-03 presents it as a coding round | Coding rounds flags the difference |

**Grading edge cases** (decide, then apply across pages):

- **Other platform aggregates.** The employer landscape keeps T0-17's Grade A for Forge secondary-market data (for example the −61% median for 2021-vintage names). D-018 names only Levels.fyi, JobsPipe and Fast AI Jobs. Decide whether Forge and Carta data are also B.
- **Credential ROI** grades two Microsoft facts A (the unverified partner-credit claim, and AI-103's beta label) where T0-11.F1 grades Microsoft facts B.
- **Interview loops:** grade-C claims inside the employer-loop tables rely on one umbrella attribution; name the source in each cell at the next revision.
- **Negotiation playbook:** one row keeps A/B because it combines Levels.fyi (B) with a Pave press release (A).

**Checks against primary sources:**

- **India remote tax:** the export-of-services rules under FEMA and the Income-tax Act 2025 section numbers rest on secondary sources; check them at the 2026-11-21 review (§5).
- **US federal AI governance:** OMB memo M-25-21's issue date is not in the corpus (the guides say "reported May 2025").
- **System design:** only Anthropic's model prices were fetched (2026-10-21); OpenAI and Google prices are unverified, and secondary sources disagree on batch-API size limits.

**Model consistency:** T2-01 L153 scales gate dates by ×1.5 at Tier A and ×0.5 at Tier C; the targeting workbook and learning roadmaps scale them by effective hours from T0-06 D2 (G1 near month 6 at Tier A). Both are model outputs. Reconcile the two, or explain the difference, when either page is revised.

**Data freshness:** the market overview's pay figures (the S09 snapshot of 2026-08-05 and the Q3 2025 AI premium by level) need a fresher pay corpus, and the visa statuses need re-verifying before anyone acts on them. Both pages are listed as due.

**Tooling:** the 2026-11-06 fact-check used a heuristic script that flags any figure that does not appear within a few lines of the session line it cites. Porting it into `scripts/` (standard library only) would speed up future re-verification (P2).
