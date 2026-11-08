# Roadmap

> **Updated:** 2026-11-08 · **Architecture:** decisions D-013 and D-015 to D-021 in [research/DECISIONS.md](research/DECISIONS.md) · **History:** [CHANGELOG.md](CHANGELOG.md)
> This page tracks what the repository covers, what is planned next, and the decisions that are still open. Evidence-grade conventions follow EGP-1.0.

---

## 1. Where the repository stands

**The question it answers:** is a person at point zero fully provided for? **Yes for every lifecycle stage, with named gaps.** Each stage has its core guides, and the gaps below are listed where readers meet them.

| Coverage | What |
|---|---|
| **Covered** | Every stage, 00 to 11: start-here tools (targeting workbook, glossary, tool catalog), the market and employers, the role universe with a role map and one hub per role, skills with a radar and learning roadmaps, credentials, proof of work with project cards, job search, networking, interviewing with prep packs, compensation, onboarding and growth, and six track playbooks |
| **Needs new research** | Measured tool tiers and skill momentum (job-description mining); India job platforms (FAD OQ2); research-backed routes for DevOps/SRE engineers, product managers and students (provisional [P] routes exist); live target-company lists; remote pay bands and Europe depth; burnout and sustainable pace. All of these, plus a full certification census, networking, résumés, countries and visas, interviews and a dossier for every role, are planned as the 53 sessions of [research pipeline 2](research/pipeline-2/README.md) |
| **Needs building** | The résumé generator (P0-1); a static site, if chosen |

**Quality caveat.** AI agents drafted the stage guides from the research sessions on 2026-11-05 and 2026-11-06. On 2026-11-06, 13 independent fact-checking agents checked 4,829 claims against the session lines they cite and made 234 fixes, and a script confirmed that the figures on each line appear near the line it cites. Before 1.0, CONTRIBUTING §7 requires an independent fact-check of the reference documents: the pages added on 2026-11-05 and 2026-11-06 had the agent fact-check above, and the v0.1.0 catalogs and skills references still need one (P1-5). No human domain expert has reviewed the guides yet; that is recommended before readers rely on the compensation, tax, visa and interviewing pages (P1-4). The work also logged errata U13–U26 against the Phase 0 records.

**Consolidation (2026-11-07 to 2026-11-08).** An audit of every file found the structure sound but facts copied by hand across pages, some of them contradictory. In response:
- each shared fact now has one owner (D-019): the v0.1.0 references were slimmed, the role skill maps are narrative only, the résumé guidance is one guide, and the posting-term shares moved into `data/posting_skill_shares.json`;
- the three older guides follow the guide pattern, so every guide is checked;
- generated pages carry `review_by` dates and a weekly run fails while any page is due (D-020);
- the validator rejects schema rules it cannot enforce, checks session line references in the data, and runs every generator from one registry (`scripts/build_all.py`); machinery tests run in CI.

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
| **4b. Consolidation** | One owner per fact (D-019); generated review dates and a weekly reminder (D-020); schema and validator hardening; facts moved out of scripts into `data/`; the three older guides migrated | **Done** (2026-11-08) |
| **5. Research pipeline 2** | 53 targeted sessions designed backwards from the data and pages they feed (D-021): networking, résumés, job search with India platforms measured, a seven-part certification census, countries, visas and remote work, pay, interviews and AI-mediated hiring, a dossier for every role (job-description samples), transitions for DevOps/SRE, PMs, IT-services engineers and students, learning resources, skill momentum and emerging titles, the market pulse and onboarding; nine reduce steps; five measurement instruments | **Designed** (2026-11-08). Next: the owner runs wave 1 ([tracker](research/pipeline-2/README.md#tracker)) |
| **6. Release 1.0** | An independent fact-check of the reference documents (P1-5) and paths, IDs and schemas declared stable (CONTRIBUTING §7); a human expert review of the guides is recommended first (P1-4) | After phase 5, or earlier once the fact-check is done |

---

## 4. Build plan

Ordered by impact on hiring odds, then by dependency:

| Priority | Deliverable | Why | Depends on |
|---|---|---|---|
| **P0-1** | **Résumé generator:** build the universal, family and role résumés from one tagged personal inventory kept in `personal/` (git-ignored), following the layers in the [résumé strategy](career/06-job-search/resume-strategy.md#the-five-layers-and-their-jobs). Include a section-order skeleton for a one- to two-page résumé, and a per-role bank of evidence lines keyed to each role's Must and Important skills, with the X-Y-Z pattern as an optional [P] form ([ATS mechanics](career/06-job-search/ats-mechanics.md)) | Makes a few dozen résumés maintainable | Résumé matrix and role inventories (exist) |
| **P0-2** | **Run research pipeline 2, wave 1:** 18 sessions (networking, the résumé, job search, the certification census, the country scan), prompts from `scripts/research_pipeline.py --prompt <id>`; then waves 2 and 3 ([order](research/pipeline-2/README.md#waves-and-the-recommended-order)) | The largest gaps by effect on a job search, and the catalogues the owner asked for | — (the owner runs them) |
| **P1-1** | **Job-description mining:** 30 or more dated postings per role from public ATS boards; promote measured tools from [S] or [P] to [JD]; add a "surging" ring to the skills radar from dated series | Tool tiers outside a dozen measured titles rest on session mentions and practice curation | The role dossiers T0-48 to T0-66 (samples of 15–30 postings per role: aliases, wording and pay bands) and T0-69 (dated series); P1-7 for measured shares |
| **P1-2** | **India job platforms** (Naukri, Instahyre and others; FAD OQ2) | The channels guide and the India playbook state the gap | Session T0-25 (and T0-45 for India pay); the owner's logged-in counts (INS-5) |
| **P1-3** | **Four more starting backgrounds:** DevOps/SRE, product managers, IT-services engineers, students and new graduates | Their routes in career transitions are provisional [P] or missing | Session T0-67 |
| **P1-4** | **Human expert review** of the stage guides, starting with compensation, tax, visa and interviewing | The guides were agent-drafted and agent-checked | — |
| **P1-5** | **Independent fact-check of the v0.1.0 reference documents:** the role catalog, rankings and skill maps, and the 1,529 tiered skill links in the ontology. The planned agent check was blocked on 2026-11-04 ([role skill inventories §4](career/03-skills-and-tech/role-skill-inventories.md#4-verification)) | CONTRIBUTING §7 requires it before 1.0 | — |
| **P1-6** | **Integrate research pipeline 2 by reduce step** (R1–R9): new data files with schemas where the decision records choose them, the computed credential value order (R1) and country ranking (R2) with their scripts and generated pages, and the owner pages each step names ([reduce steps](research/pipeline-2/README.md#reduce-steps-from-sessions-to-data-and-pages); [INTEGRATE.md](research/pipeline-2/INTEGRATE.md)) | Research changes nothing until it is integrated and verified | The sessions each step needs |
| **P1-7** | **Job-description collector** (instrument INS-1, planned `scripts/collect_jds.py`): postings from employers' public job-board endpoints for the T0-27 employer list, classified by title, skills extracted with the ontology's aliases, a dated snapshot with n per title; recall measured on a labelled sample | Turns samples of about 30 postings per role into repeatable monthly measurement | Session T0-27 (employers with their job-board URLs); build it before wave 2 if possible |
| **P2** | **Official-register script** (instrument INS-2): AI-title filings by employer and city from US LCA disclosure data and the UK and Dutch sponsor registers (A for filings, never for pay) | Sponsorship signals for the country ranking and the target-employer list | — |
| **P2** | **Net-pay calculator** (instrument INS-4): effective tax and social contributions at reference salaries per country from official schedules, with incoming-worker regimes | The country ranking's net-pay pillar | Sessions T0-35, T0-36 |
| **P2** | **Logged-in platform counts** (instrument INS-5): a fixed query list the owner runs monthly on platforms that hide counts from signed-out users (Naukri, Instahyre, LinkedIn), recorded as a dated table | India demand evidence agents cannot collect | — (the owner runs them) |
| **P2** | **Tool-choice cards** (stage 03): for each choose-one class in the skills ontology (serving engines, eval runners, tracing and agent orchestration first), a sourced default and if → then rules, stored as `compare` fields and rendered in [skills vocabulary §2](career/03-skills-and-tech/skills-vocabulary.md#2-choose-one-classes). Start from T0-03's risk-aware tool selection policy (§4.2, L139–147) and its devaluation table (§6.8.2) | Readers choosing between interchangeable tools get a sourced default, not just a list | Skills ontology |
| **P2** | **Research-track concept checklist** (stage 11): the concepts research-engineer and research-scientist loops probe, as a self-check list built from the research family's Must and Important skills and T0-06 D8, pointing to primary references rather than teaching them. Until then, the research role inventories' self-assessment tables and the [skills radar](career/03-skills-and-tech/skills-radar.md) family C view cover it | Completes the PhD and research path | Skills ontology |
| **P2** | **Finish one owner per fact (D-019):** the role rankings §5.2 and §5.3 still copy timelines, India pay, remote shares and tax facts (link career transitions, pay benchmarks, the market overview and India remote tax instead); the targeting workbook keeps T0-06 working tables (it names career transitions as their owner); refresh the workbook's worked example (access scores, India ranks, coverage, dated 2026-11-04) against the regenerated hubs | Fewer copies to refresh | — |
| **P2** | **Ontology clean-up:** collapse AI Engineer's 63 Optional tools into their choose-one classes (148 skills, next largest 84); merge the duplicate Physical AI entries ("Perception / computer vision" and "Computer vision"; two VLA entries) and the three governance entries in skills-radar ring 2 (EU AI Act, the combined EU AI Act/NIST/ISO entry, ISO/IEC 42001) | Cleaner inventories and radar | Skills ontology |
| **P2** | **Leadership hubs:** the five leadership and independent hubs are mostly "no evidence" sections; have `build_role_hubs.py` collapse empty sections (they already open with their track playbook) | Shorter pages | — |
| **P2** | Target-company lists (session T0-27, reduce step R6); learning-resource curation with a rating method (session T0-68; no GenAI course or bootcamp has outcome data that is not vendor-reported, T0-06 L203); a claims registry if page-level `review_by` proves too coarse (D-017, D-020); a static site | Context and convenience | Decisions in §6 |

---

## 5. Maintenance calendar

99 pages carry a `review_by` date (2026-11-08); the validator lists the ones that are due, and the weekly `due-report` workflow fails while any page is due (D-020).

| When | What |
|---|---|
| Every change | `python3 -B scripts/build_all.py` (every generator in order, then the validator) and, after a script change, `python3 -B -m unittest discover -s scripts/tests`. CI runs both on every push |
| Mondays (CI) | The `due-report` workflow runs the validator with `--strict`; a failure means a page is due |
| Overdue | Visa and relocation: its status table of contested and pending rules (class V0, 14 days) is past expiry. Re-verify each row against the official source the table names, then reset `review_by`. The visa dossiers T0-37 to T0-42 of research pipeline 2 will replace the table's content |
| After each research pipeline 2 session | Check the report with `scripts/research_pipeline.py --appendix` before saving it; verify it ([VERIFY.md](research/pipeline-2/VERIFY.md)); integrate it ([INTEGRATE.md](research/pipeline-2/INTEGRATE.md)). Re-runs follow the pipeline's [refresh cadence](research/pipeline-2/README.md#refresh-cadence) |
| By 2026-11-14 | Skillenai 90-day counts (window ending 2026-10-14, class V1): the role catalog, the role rankings, emerging roles, agentic protocols and four role hubs (agentic AI, AI enablement, AI security and the hubs index) |
| By 2026-11-19 | Fast AI Jobs counts (2026-10-19): the market overview, the employer landscape, channels and boards and five role hubs |
| By 2026-11-21 to 2026-11-25 | Regulatory and tax statuses: the glossary, India remote tax (also check the FEMA export-of-services rules and the Income-tax Act 2025 section numbers s.58, s.62(4), s.63 against the primary texts, which T0-07 did not open, §7), governance careers, the India playbook, PhD to industry, first 90 days (2026-11-23); Go Fractional counts on the fractional AI leader hub (2026-11-25) |
| By 2026-12-01 to 2026-12-03 | JobsPipe recount (T0-01 recount protocol), starting with the ranks most likely to move: Applied Scientist, Research Engineer, AI PM, AI Solutions Architect. It refreshes `data/role_scores.json`, then `build_all.py` regenerates the rankings, the target order and 20 hubs; the GenAI target roles, the résumé strategy, the job-search strategy and career transitions fall due on 2026-12-03 |
| By 2027-01-10 to 2027-01-23 | Pay figures (re-verified after 90 days) and tool, protocol and credential statuses (class V2): the targeting workbook (2027-01-10), freelance and fractional (2027-01-18), pay benchmarks and 12 other guides (2027-01-19), the 26 inventories, the skills radar and vocabulary, credentials pages, ATS mechanics, the application operating system and growth (2027-01-21), behavioural calibration and coding rounds (2027-01-23). Regenerate after editing the data |
| By 2027-01-31 | Scheduled review of the Phase 0 decisions (D-001 to D-012) |
| By 2027-05-01 | Posting-term shares (class V3, 180 days): add a new dated JobsPipe snapshot to `data/posting_skill_shares.json` and re-tier the links it changes |
| By 2027-05-04 to 2027-05-07 | Scheduled reviews: D-013 to D-017 (2027-05-04), D-018 (2027-05-06), D-019 and D-020 (2027-05-07) |
| Quarterly | Re-verify a sample of claims; refresh the findings registry after any new session |

---

## 6. Open decisions

1. **Résumé generator (P0-1):** build it now, with the personal inventory under `personal/` (git-ignored)?
2. **Research pipeline 2 order:** the pipeline recommends wave 1 first (networking, the résumé, job search, the certification census and the country scan) and names a ten-session minimum ([waves](research/pipeline-2/README.md#waves-and-the-recommended-order)). Confirm or reorder.
3. **Static site:** stay GitHub-native Markdown (the current choice), or publish with MkDocs Material (T1-01 KF9)? The front matter and folder indexes already support either.
4. **Generic or personal:** keep the system generic for anyone, or also build a personal instance from one person's background, targets and constraints? `scripts/gap_analysis.py` is the first personal tool.
5. **Claims registry:** keep page-level `review_by` dates (D-017, D-020), or add per-claim IDs with their own expiry? D-020's trigger: agents need claim-level expiry, or the weekly reminder lists more than 25 pages due at once.
6. **Upstream errata:** apply the [ERRATA.md](research/ERRATA.md) corrections inside FAD and DECISIONS, or keep those records as written (the current choice) with status notes?
7. **Confirm D-019, D-020 and D-021** (one owner per fact; generated review dates and the weekly reminder; research pipeline 2): appended on 2026-11-07 and 2026-11-08 as accepted, not yet reviewed by the owner (`human_reviewed: false`).
8. **A licence for `scripts/`:** CC BY-SA 4.0 covers the whole repository, but Creative Commons licences are not designed for code. The usual choice is a code licence (MIT or Apache-2.0) for `scripts/` alongside CC BY-SA 4.0 for the content; the owner decides.
9. **Data shapes for the research pipeline 2 rankings** (decide at each reduce step, with a decision record): credentials in their own data file or in the skills ontology (R1); where the country ranking page lives, stage 01 or stage 11 (R2); the target-employer list as a data file or a page (R6).

---

## 7. Known issues and follow-ups

Found during the 2026-11-06 fact-check and the 2026-11-07 repository audit, and not yet resolved. Line numbers are as of those dates.

**Candidate errata in the sealed records.** Reported by the fact-checkers but not yet confirmed. Verify each against the session, then log confirmed ones in [research/ERRATA.md](research/ERRATA.md):

| Location | Reported issue | Where the guides stand |
|---|---|---|
| T0-02 F3 and F5 | The findings say Grade A, but the session's source ledger grades the underlying sources (S13, S15, S49) as B search excerpts | Pages grade these figures B (D-018) |
| T0-06 L130 against L152 and L808 | L152 and L808 call data scientists a top-two feeder on both LinkedIn lists; L130 lists them third on the 2025 list | Not quoted as a ranking |
| T0-06 L387 | The 1.4–3.7-month range leaves out the zero-code route (4.6 months) | Not quoted |
| T0-03 KF2 against L179 and L420 (and L59 for evaluation platforms) | KF2 says the top-band job descriptions read were J1–J8; L179 and L420 say 0 of 10 top-band lab job descriptions | The market overview follows L179; coding rounds states both readings |
| T0-18 F1 (L89) against L196 | The fractional CTO second-read ask is $209–212 in F1 and $210 in the table | The freelance guide follows F1 |
| T0-07 L229 | ₹49.91L ÷ ₹75L is 66.5%, printed as 66.6% | Immaterial; India remote tax copies the session |
| T1-03 F4 against L211 | F4 calls a Google behavioural No Hire a near-automatic veto; the firm table says the hiring committee may downlevel instead | Behavioural calibration reports both |
| T0-14 L553 and L826 against T1-03 F6 | T0-14 records Meta's spring 2026 AI-enabled round as a design round; T1-03 presents it as a coding round | Coding rounds flags the difference |

**Grading edge cases** (decide, then apply across pages):

- **Other platform aggregates.** The employer landscape keeps T0-17's Grade A for Forge secondary-market data (for example the −61% median for 2021-vintage names). D-018 names only Levels.fyi, JobsPipe and Fast AI Jobs. Decide whether Forge and Carta data are also B.
- **Credential ROI** grades two Microsoft facts A where T0-11.F1 grades Microsoft facts B. Checked on 2026-11-07: AI-103's beta label rests on the Microsoft Learn exam page (S15), which T0-11's source ledger grades A (L512), so A stands; F1's B covers the AI-102, AI-300 and AI-200 facts (S16, C). The partner-credit sentence says only the 2022 AWS counts were verified, but T0-11 L435 adds "and older Microsoft lists": fix the wording at the next revision.
- **Interview loops:** grade-C claims inside the employer-loop tables rely on one umbrella attribution; name the source in each cell at the next revision.
- **Negotiation playbook:** one row keeps A/B because it combines Levels.fyi (B) with a Pave press release (A).

**Checks against primary sources:**

- **India remote tax:** the export-of-services rules under FEMA and the Income-tax Act 2025 section numbers rest on secondary sources; check them at the 2026-11-21 review (§5).
- **US federal AI governance:** OMB memo M-25-21's issue date is not in the corpus (the guides say "reported May 2025").
- **System design:** only Anthropic's model prices were fetched (2026-10-21); OpenAI and Google prices are unverified, and secondary sources disagree on batch-API size limits.

**Model consistency:** T2-01 L153 scales gate dates by ×1.5 at Tier A and ×0.5 at Tier C; the targeting workbook and learning roadmaps scale them by effective hours from T0-06 D2 (G1 near month 6 at Tier A). Both are model outputs. Reconcile the two, or explain the difference, when either page is revised.

**Data freshness:** the visa page's status table needs re-verifying against the official sources it names before anyone acts on it (it is due). The market overview no longer copies pay figures; pay lives in [pay benchmarks](career/09-compensation/pay-benchmarks.md), whose rows are dated by dataset (the S09 snapshot is dated 2026-08-05). The posting counts behind the role pages expire between 2026-11-14 and 2026-12-03 (§5).

**Review dates to recompute at the next edit** (they predate D-018's classes): the glossary (2026-11-21) states a V0 status (NIST AI RMF "being revised") and V1-derived quorum statements; governance careers (2026-11-21), first 90 days (2026-11-23) and India remote tax (2026-11-21) still use the old "14–31 days for policy" reading, although contested items such as "no federal preemption as of 22 Jun 2026" are V0 (14 days). Under D-018 each would already be due; recount them at those reviews, and consider a dated status table like the visa page's.

**FAD open questions tracked here** (FAD §19; they were tracked nowhere else):
- **OQ3 (High):** how consistently do different reviewers assign EGP-1.0 grades? Run the planned pilot (50 claims, two reviewers) before 1.0; research pipeline 2's quality gate 5 proposes drawing the 50 claims from its first sessions.
- **OQ4 (Low):** how to measure community-to-job conversion, given no baseline.
- **OQ6 (Medium):** how the repository handles AI-generated contributions. Current practice: agents draft, an independent check verifies every figure against its cited line (D-018 rule 6), and decisions record `authored_by` and `human_reviewed`; write it down as a contribution policy in CONTRIBUTING.

**Session-ID namespace:** the scripts read session IDs as five characters (T#-##). Research pipeline 2 reserves T0-19 to T0-71, which leaves T0-72 to T0-99 for re-runs and new foundational sessions (about two years at the pipeline's refresh cadence). Before T0-99, widen the ID patterns in `build_findings.py`, `build_skills.py`, `build_tool_catalog.py`, `common.py`, `research_pipeline.py` and the data schemas.

**Tooling:** the 2026-11-06 fact-check used a heuristic script that flags any figure that does not appear within a few lines of the session line it cites. Porting it into `scripts/` (standard library only) would speed up future re-verification (P2).
