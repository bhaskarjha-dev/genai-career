---
id: T0-06
title: "Career Transition Timelines, Skill Deltas and Quarterly Roadmaps: Five Starting Backgrounds into GenAI (Oct 2026)"
date: 2026-10-21
status: complete
topic: "GenAI career transitions for backend/systems, data science/BI, frontend/full-stack, non-technical, and academic/PhD starting points"
tags:
  - genai
  - ai-engineering
  - career-transition
  - upskilling
  - evals
  - hiring
  - roadmap
  - portfolio
  - labor-market
  - 2026
informs_decisions:
  - "Which archetype-specific pivot route to commit to: internal transfer, external search, or adjacent role"
  - "Weekly time budget (8-10, 15-20, or 35-40 h/week) and whether part-time is viable"
  - "Month 3/6/9/12 go/no-go gates and the artifacts that must exist at each gate"
  - "Role level and loop type to target: applied-AI startup, big-company loop, or frontier lab"
  - "Which learning platforms and GPU compute to budget for"
confidence: medium-low
confidence_notes: "Market-context findings rest on primary or well-corroborated sources (medium-high). Timeline, weekly-hours and per-archetype skill-delta claims rest on self-reports, vendor content and the author's own model (low). No longitudinal cohort study of GenAI career transitions was found."
evidence_scale: "A = primary/canonical source read this session; B = reputable secondary, or interested-but-disclosed primary, corroborated; C = single-source, vendor, aggregator or snippet-only; D = recalled from model memory, anecdotal, anonymous, or author-modeled"
author_note: "Written by Claude (Anthropic). Some cited sources are Anthropic-authored or use Anthropic data; they are flagged in the ledger and are not sole support for any headline conclusion."
---

# T0-06: Career Transition Timelines, Skill Deltas and Quarterly Roadmaps for Five Starting Backgrounds Pivoting into GenAI (October 2026)

> **Reading guide**
>
> - **Temporal anchor:** 21 Oct 2026. Evidence was retrieved this session through roughly 50 searches and page fetches. Source IDs like `[S04]` point to the ledger at the end.
> - **Provenance tags:** `[F]` = found and read this session (ledger ID given). `[M]` = the author's own model or synthesis, which caps at Grade D under the calibration rules. `[R]` = recalled from model memory before searching, also capped at Grade D.
> - **Grades:** A = primary or canonical source read this session. B = reputable secondary, or interested-but-disclosed primary, corroborated. C = single source, vendor content, aggregator, or search-snippet-only. D = recalled, anecdotal, anonymous, or author-modeled.
> - **Access marks in the ledger:** `fetched` = the page was opened in full. `extract` = substantive text from the canonical page came back inside search results. `snippet` = only a short excerpt or a secondary description was seen. Snippet-only sources are never graded above C.
> - **Disclosure:** this file was written by Claude, a model made by Anthropic. A few sources are Anthropic-authored or use Anthropic data (the Fellows Program; the Anthropic Economic Index, which the Stanford Canaries analysis uses for its automation-versus-augmentation split; and one unattributed blog claim about Anthropic's interview loop). They are flagged. The Stanford finding is also contested in the literature (see KF-2 and Open Questions). None of them carries a headline conclusion alone.
> - **Geography:** most quantitative evidence is US-centric (Axial, ATUS, Huntr, Stanford/ADP). Check local labour-market conditions before relying on any absolute number.
> - **What this file is not:** a promise of outcomes. The timeline tables are a transparent model, not measured cohort data. Every parameter is stated so you can change it.

---

## Prior

Five propositions I held **before** searching. All are recalled from model memory and therefore capped at Grade D. Each is written so that evidence could contradict it. Initial confidence is my subjective pre-search estimate.

| # | Proposition (recalled, pre-search) | Initial confidence | What would falsify it |
|---|---|---|---|
| **P1** | Backend/systems engineers with 5+ years (Java/Go) pivot fastest into GenAI engineering because distributed-systems literacy transfers, and a realistic median time to first offer while employed full-time is about 6-9 months. | 0.65 | Head-to-head data showing frontend/full-stack or data-science backgrounds equal or faster; or evidence that the binding skill is evaluation or domain judgment rather than systems skill. |
| **P2** | The main reason traditional Data Scientists fail production AI technical loops is software-engineering weakness (tests, packaging, deployment, system design), not statistics or ML knowledge. | 0.70 | Evidence that DS skills are specifically rewarded in GenAI loops, that DS are a top feeder population, or that rejections cluster elsewhere. |
| **P3** | Non-technical professionals cannot win a raw-coding competition; viable paths run through domain specialization in evaluation, product, operations or customer-facing roles. | 0.75 | Evidence that non-technical entrants fill coding-heavy roles at scale, or that domain-led roles are too few to matter. |
| **P4** | Part-time timelines are about 6-12 months for experienced engineers and 12-24 months for everyone else or the research track, and shipped artifacts matter more than hours logged. | 0.60 | Cohort data contradicting these ranges; evidence that credentials or hours dominate artifacts. |
| **P5** | Academic PhDs struggle less with knowledge than with engineering craft, product speed and communication; frontier-lab research slots are scarce, so most PhDs should target applied or research-engineer roles. | 0.60 | Evidence that PhD supply is absorbed easily into industry, or that the barrier is something else (visa, title inflation, hiring freezes). |

Side recalls that were also re-tested (AI-skill wage premium, WebGPU/Safari status, Transformers.js version, Kaggle GPU quota, the size of the entry-level squeeze) are reported in **Delta**.

---

## Research Question

**Decision.** For a professional starting from one of five backgrounds in October 2026, what is a *realistic* path (calendar time, weekly hours, deliverables) into a Junior, Mid-level or Senior GenAI role? Which knowledge gaps must be closed, which habits must be unlearned, and what should be shipped at months 3, 6, 9 and 12?

**Sub-questions** (mapped to the brief's domain probes)

1. **Market structure.** Where is hiring actually happening, at what seniority, and who is being hired from which backgrounds?
2. **Backend probe.** What is the median time to first offer for a 5+ year Java/Go engineer pivoting while employed?
3. **Data-science probe.** Which software-engineering deficiencies most often disqualify traditional Data Scientists in production AI loops?
4. **Frontend probe.** Can Frontend/Full-Stack engineers use client-side AI runtimes (WebGPU, Transformers.js, streaming UI, agent interfaces) to sidestep backend-heavy competition?
5. **Non-technical probe.** Which high-leverage niches exist for Product/Operations/Domain experts?
6. **PhD probe.** What translation barriers stop Quant PhDs from succeeding in commercial GenAI product engineering?
7. **Hours versus duration.** What weekly time budgets are realistic for an employed adult, and what pivot duration do they imply?
8. **Tooling.** Which self-paced platforms, GPU labs and diagnostic matrices are worth using, and at what verified cost?

**Working definitions**

- **GenAI role-ready** `[M]`: able to independently build, evaluate, deploy and operate an LLM-backed system (retrieval and/or tool-using agent) with a measured eval suite, traces, a cost and latency budget, and a data-backed explanation of its failure modes.
- **Level mapping** `[M]`: *Junior* = under about 2 years of relevant professional experience; *Mid* = about 3-7 years; *Senior* = 8+ years or clear ownership of production systems. Career-changers are modeled as moving **laterally** (same level as their prior experience) unless stated, for reasons developed in KF-2.

**Out of scope.** Thirty-day "zero-to-hero" claims; overnight transitions; planning around frontier-lab research-scientist offers as a base case (treated as a lottery-style upside, not a plan).

**Method.** Four search strategies, as briefed. (1) Archetype gaps. (2) Unlearning traps and failure modes. (3) Milestone modeling. (4) Empirical verification of weekly hours and search friction. Plus tool-catalog verification and falsification searches (slowdown, bubble, rejection reasons). Where the brief asked for longitudinal studies, verified retrospectives and hiring-manager feedback, I report what exists and, explicitly, what I searched for and did not find.

---

## Key Findings

Twelve substantive findings. Each carries an evidence grade and a pointer to the ledger. Detailed per-archetype material is in **Detailed Findings**.

| # | Finding (one line) | Grade |
|---|---|---|
| KF-1 | Demand is real, IC-heavy and mid/senior-weighted; the wage premium is large but correlational. | B |
| KF-2 | The junior door is the narrowest part of the market; prior tacit experience is the hedge. | A (facts) / B (implication) |
| KF-3 | The AI-engineer population is mostly experienced software engineers who pivoted; data scientists are a consistent second; "backend is fastest" is untestable with public data. | B (population) / D (speed ordering) |
| KF-4 | Evaluation is the cross-archetype bottleneck and the most consistent interview discriminator. | B (survey ranking) / C (hiring content) |
| KF-5 | The data-scientist "can't ship" trope is half right: real gaps in big-company loops, real advantage in evals. | C / D |
| KF-6 | Client-side AI platform facts are solid; demand for AI-frontend specialists is thin and senior-skewed. | A (platform) / C-D (demand) |
| KF-7 | Non-technical niches exist (AI PM, AI ops, domain evaluation, FDE-adjacent) but each has an entry fee in experience, credentials or coding. | C |
| KF-8 | PhD supply is up but industry absorption is flat; the barrier is craft translation and market structure more than knowledge. | B / C / D |
| KF-9 | No longitudinal timeline data exists; self-reports cluster at 4-9 months part-time for experienced engineers and are all survivor-biased. | D |
| KF-10 | Hours, not compute, are the binding constraint: 10-15 h/week is a large share of an employed adult's leisure. | A + [M] |
| KF-11 | Job-search friction adds roughly 2-4 months with a fat right tail. | C |
| KF-12 | Compute and course access are cheap relative to time; most GenAI application work needs no GPU. | A / B |

### KF-1. Demand is real, IC-heavy and mid/senior-weighted; the premium is correlational (Grade B)

**Evidence**
- Axial Search counted 43,480 US AI-engineering postings from January through July 2026, about 1,550 per week, peaking at 2,327 in one late-June week. About 66% are individual-contributor roles, reported as 35% mid-level and 31% senior, and about 10% are management; the part of the page I read gave no entry-level share. 72% state a degree requirement. The most common requirements are Python (62%), cloud (55%) and foundation-model experience (51%) `[F: S04, Grade C]`.
- LinkedIn's Jobs on the Rise 2026 (data Jan 2023 to Jul 2025) ranks AI Engineer first and AI Consultant/Strategist second. Reported median experience is 3.7 years for AI engineers and 8.2 years for AI consultants/strategists `[F: S06, secondary summaries, Grade C]`.
- PwC's 2026 AI Jobs Barometer (15 Jun 2026; over one billion job ads, 27 countries) reports a 62% average wage premium for jobs requiring AI skills, up from 57%, and 69% growth in AI-skill postings versus 9% for all postings `[F: S05, Grade B]`.

**Caveats.** All three are posting- or ad-based, not hire-based. The Stanford authors note that generative AI can induce employers to post roles they are less likely to fill `[F: S01]`. PwC's premium is correlational and covers AI-skill jobs broadly, not GenAI engineers specifically. Indeed Hiring Lab reported in late 2025 that overall tech postings remained about a third below pre-pandemic levels `[F: S45, 2025 vintage]`. LinkedIn's March 2026 workforce report puts US hiring 23% below its February 2020 pace, with technology, information and media 26% below `[F: S47b, Grade A]`. AI engineering is an exception inside a soft tech market, not a rising tide.

**Implication.** There is a growing pool of roles, weighted toward people who already have experience. That favors lateral pivots by experienced professionals and disfavors start-from-zero plans.

### KF-2. The junior door is narrowest; tacit experience is the hedge (Grade A facts, B implication)

**Evidence.** Stanford Digital Economy Lab's *Canaries in the Coal Mine?* (August 2026 version) reports that employment of workers aged 22-25 in the most AI-exposed occupations is 19% below where it would be had it kept pace with less-exposed peers. The gap has widened since it was first documented in August 2025. Experienced workers show no comparable gap. The effect operates through reduced hiring rather than increased separations. It is concentrated where AI substitutes for work rather than complements it, and the authors' reading is that AI replaces codified knowledge more readily than tacit knowledge `[F: S01, Grade A]`.

**Caveats.** Descriptive, not causal. Some divergent trends pre-date generative AI. Effects attenuate with education controls. The data are ADP payroll records and the pattern is more pronounced there than in national survey benchmarks `[F: S01]`.

**Corroboration and a counterweight.** PwC's 2026 barometer (2.4 million US entry-level jobs analysed) finds that AI-exposed entry-level roles are seven times more likely to require traditionally senior, human-intensive skills such as judgment and leadership. Those "seniorised" entry-level openings grew 35% since 2019 while other entry-level roles shrank 10% `[F: S05, Grade B]`. The Stanford group's own June 2026 indicators note that studies disagree: several find junior declines, while a Yale Budget Lab study is reported to find little relationship between AI exposure and employment (the snippet I saw was truncated, so I cannot state the exact outcome measure) `[F: S01b, snippet, Grade C]`. A commentator has also questioned the Canaries analysis's reliance on Anthropic Economic Index data `[F: S01c, commentary on the 2025 version, Grade D]`.

**Implication `[M]`.** "Junior GenAI role from scratch" is the hardest target on the map. Pivoters should convert prior tacit experience (systems, product, domain, research) into **lateral-level** AI roles. A true entry-level pivot is realistic mainly for BI analysts and new PhD graduates, and even there at lower odds.

### KF-3. Experienced software engineers dominate the AI-engineer population; backend-versus-frontend speed is unmeasured (Grade B / D)

**Evidence**
- The 2026 AI Engineering Survey (Notion × Amplify Partners × Vercel; 1,053 responses collected 16 May to 15 Jun 2026): among respondents with 10+ years of software experience, 51% have 3 or fewer years of AI experience. The share with under one year of AI experience fell from about 1 in 10 to roughly 1 in 34. Role mix: Founder/CTO 23%, AI Engineer 19%, Fullstack Engineer 12%, Eng Manager/Tech Lead 9%, Product Manager 9% `[F: S02, Grade B]`. The conference talk summarizing the same data reports a median of about 8 years writing code and 3 years in AI/ML, with 1,048 respondents `[F: S03, snippet, Grade C]`.
- LinkedIn 2026: AI Engineers most often come from Software Engineer, Data Scientist and Full Stack Engineer roles. AI Consultants/Strategists come from Founder, Software Engineer and Product Manager. AI/ML Researchers come from Data Scientist, Software Engineer and ML Engineer `[F: S06, Grade C]`. The 2025 list (Jan 2022 to Jul 2024) names full-stack engineers, research assistants and data scientists for AI engineers, and operations associates for AI consultants `[F: S07, Grade C]`.

**Caveats.** The survey is a convenience sample of conference, partner and community audiences, and its sponsors describe results as respondent shares rather than population estimates. LinkedIn titles do not separate backend from frontend ("Software Engineer" is the top feeder), and share of transitions is not speed or success rate. **No public dataset ranks archetypes by time to offer.**

**Implication.** P1's "backend is fastest" cannot be confirmed or refuted from public data. What is supported: experienced software engineers of any stack are the dominant feeder, data scientists a steady second, and full-stack engineers appear in both LinkedIn lists. This file treats backend as "plausibly fastest, unproven".

### KF-4. Evaluation is the cross-archetype bottleneck and interview discriminator (Grade B ranking / C hiring content)

**Evidence**
- In the 2026 survey, evaluation is the most-cited biggest challenge in the AI stack (20%), ahead of orchestration/agents (18%), inference cost and speed (16%) and security/guardrails (15%). Prompting is the most common adaptation method (80%), followed by tool-use tuning (59%), RAG (49%), fine-tuning (26%) and RL (22%) `[F: S02, Grade B]`.
- Pragmatic Engineer's reporting on companies that built AI features with existing software engineers quotes Wordsmith's CEO saying the hardest adjustment for most developers is getting comfortable with evaluations and iterating on non-deterministic output `[F: S08, Grade B]`.
- Hiring-side write-ups converge on eval design, error analysis, retrieval judgment, agent debugging and cost/latency reasoning as what applied-AI loops test, usually via a take-home and a scoping or customer-style round `[F: S11, S12, S13, S14; Grade C/D, unattributed or consultant content]`.
- The most detailed first-person retrospective found (React developer to AI engineer, 8 months, employed throughout) credits an eval harness as its highest-value early investment `[F: S10, Grade D]`.

**Caveats.** I found no systematic dataset of rejection reasons. Hiring content is blogger and consultant sourced.

**Implication `[M]`.** Make **evaluation the spine of every archetype's portfolio**. Each background has a different comparative advantage inside it: backend (regression CI and observability), frontend (UX and human-in-the-loop evals), DS (error analysis and judge validation), non-technical (domain rubrics and ground truth), PhD (measurement rigor).

### KF-5. The data-scientist "can't ship" trope is half right (Grade C / D)

**For the trope.** DataTalks.Club's wiki frames the data-scientist-to-ML-engineer move as keeping statistical judgment while changing what counts as proof: reviewable code, operational curiosity about monitoring and MLOps, and written design with baselines. It names Python, system design, deployment and monitoring as the gaps a project will expose `[F: S39, Grade C]`. A mentoring marketplace's guide for the same move gives a five-milestone roadmap and a 6-18 month timeline `[F: S39, Grade D]`. Candidate-reported rejections at large-company ML loops cite coding rounds and system design as the deciding rounds `[F: S40, Grade D, anecdotal]`.

**Against the trope.** Data scientists are a top-two feeder into AI engineer titles on both LinkedIn lists `[F: S06, S07]`. Hamel Husain's 2026 "Revenge of the Data Scientist" talk argues that the core eval loop *is* data science: trace review is exploratory analysis, aligning evals to outcomes is metric design, validating LLM judges is model evaluation, and curated test sets are experimental design. A companion Arize post adds that PMs and domain experts, not engineers, should label eval data `[F: S15, Grade C; a named-practitioner argument, not an empirical test]`.

**Caveats.** No frequency data on disqualifying deficiencies was found.

**Implication `[M]`.** P2 is **refined, not confirmed**. The DS gap is real in big-company loops (algorithmic coding, system design) and in "own it in production" signals. But DS have a genuine comparative advantage in the eval work KF-4 identifies as the bottleneck. The unlearning job is not "learn software engineering from scratch"; it is "make your analysis reproducible, tested, deployed and cheap".

### KF-6. Client-side AI platform facts are solid; AI-frontend demand is thin and senior-skewed (Grade A platform / C-D demand)

**Platform facts**
- WebGPU: Chrome and Edge, Firefox (141 on Windows, 145 on macOS Apple Silicon) and Safari 26. Google's note says Linux and Android coverage in some browsers was still in progress. Khronos' SIGGRAPH 2026 slides (22 Jul 2026) describe WebGPU as available in all major browsers `[F: S17, Grade A]`.
- Transformers.js v4 (Hugging Face blog, 9 Feb 2026) ships a new WebGPU runtime, with the same code running in browsers, Node, Bun and Deno. Point releases 4.1 and 4.2 added newer model families, KV-cache improvements and tool calling `[F: S18, Grade A]`.
- Chrome built-in AI: Translator, Language Detector and Summarizer are stable from Chrome 138. The Prompt API is stable for extensions from 138 and listed for web pages at Chrome 148. Writer, Rewriter and Proofreader remain trials. The page footer still shows a 2024 update date while its table references Chrome 148, so treat it as a living page and verify `[F: S19, Grade A]`.
- WebMCP (websites exposing tools to in-browser agents): early preview announced Feb 2026. Chrome's imperative-API documentation is dated 18 May 2026. Third-party coverage reports a 21 Jul 2026 draft spec, a Chrome origin trial from 149 and a rename from `navigator.modelContext` to `document.modelContext`. Treat the API surface as volatile `[F: S19 Grade A for Chrome docs; third-party details Grade C]`.
- Vercel's AI SDK 6 added an Agent abstraction, tool-execution approval, DevTools and full MCP support. Third-party sources disagree on its ship date (January versus May 2026), so verify against Vercel's changelog `[F: S20]`.

**Demand facts (thin).** Postings matching the "AI frontend" thesis exist, and the four I examined in detail were all Staff-level and asked for 5-6+ years: Productboard's frontend-heavy Staff roles (streaming responses, tool-use visualization, human-in-the-loop checkpoints, generative components), a recruiter-listed Staff AI Frontend Engineer role at USD 250-315k that appears under more than one company name (6+ years), and Artisan's Staff Frontend Engineer (AI transparency and human-in-the-loop controls). I also saw a forward-deployed "Frontend Engineer (AI)" listing. A vendor analysis describes a "barbell" market in which junior frontend is oversupplied and senior is tight `[F: S38, Grade C/D]`. I found **no census** of AI-frontend postings.

**Implication `[M]`.** The platform bet is sound. The claim that it lets you bypass backend-heavy competition is unproven, and the visible demand skews senior. Treat client-side AI as a **differentiator on top of full-stack AI competence**, not a substitute for it.

### KF-7. Non-technical niches exist, each with an entry fee (Grade C)

**Evidence**
- LinkedIn: AI consultants/strategists rank second on the 2026 list with reported median experience of 8.2 years. Data annotators rank fourth with 3.5 years `[F: S06, Grade C]`.
- Forward-deployed engineer postings rose more than 1,000% from January to August 2026 versus the same months of 2025 (Lightcast data reported by Fortune). Median advertised salary exceeds USD 188k versus about USD 145k for software engineers. The role still needs coding, GenAI and infrastructure skills plus customer-facing judgment `[F: S34, Grade B; large growth from a small base]`.
- A recruiting firm describes four AI PM archetypes: assistant/copilot PM, AI platform PM, ML-feature PM, and an AI-ops/internal-tools PM who deploys AI into a non-engineering team such as support or sales ops `[F: S35, Grade D, vendor]`.
- Expert-contract marketplaces hire domain specialists for evaluation and training data. A 2026 guide relaying TechCrunch says Mercor pays more than 30,000 experts an average of about USD 85+/hour. Bloomberg (16 Oct 2026), relayed by FourWeekMBA, puts Mercor's average at USD 110/hour, with recruiter postings ranging from up to about USD 120/hour for software engineers to USD 400/hour for civil-rights attorneys; those rates come from postings, not payroll data. Another relay reports thousands of roles open in mid-October 2026, concentrated in law, medicine and finance `[F: S33, Grade C/D as relayed]`. Mercor's own listings for senior domain experts ask for 4+ years of full-time experience, evidence of above-average performance, at least 10 hours per week and at-will contractor status, and a separate listing seeks degrees such as MA, JD, MD or PhD `[F: S33, Grade C, primary listings]`. Mercor also says the three-LLM judge panel that scores its APEX benchmark agrees with human raters about 89% of the time `[F: S33, Grade C]`. That is a benchmark-scoring statistic, not a labor-market measure, but it is a reminder that expert grading is increasingly mixed with LLM judges.

**Caveats.** These are mostly at-will, project-based contract roles with a minimum weekly commitment, and entry is credential- and experience-gated. They are a way to get paid AI-adjacent work quickly, not the equivalent of a career-grade GenAI role.

**Implication `[M]`.** P3 is **supported with an entry fee**: each niche asks for years of domain experience, credentials, or at least notebook-level coding.

### KF-8. PhD supply is up, industry absorption is flat, and craft translation is the recurring barrier (Grade B / C / D)

**Evidence**
- Stanford AI Index 2026: new AI PhDs in the US and Canada rose 22% from 2022 to 2024, and the increase went to academia rather than industry `[F: S31, Grade A for the headline]`. A secondary summary puts industry's share of new AI PhDs at 62.75% in 2024 versus a 2022 peak of 77% `[F: S31, Grade C]`. The 2024 AI Index had reported 70.7% for 2022, so the series has been revised or redefined. Treat levels as soft.
- **Derived `[M]`:** if both secondary figures hold, industry-bound new PhDs per 100 baseline 2022 graduates are about 77 in 2022 and about 77 in 2024 (122 × 62.75%), i.e. roughly flat. Supply growth went to academia; industry slots per PhD did not widen.
- Anthropic's Fellows Program (disclosed conflict of interest) says fellows work full-time for about four months with a stipend and compute, that applicants need not hold a PhD or have published, and that over 40% of the first cohort later joined Anthropic full-time `[F: S32, Grade B; self-reported by the program owner]`.
- Practitioner retrospectives from researchers who moved to industry stress code review, producing code with others and between meetings, reproducible end-to-end systems, and the gap between research code and production code. A PhD-to-industry write-up adds that engineering-track candidates face standard DSA and system-design loops and need visible testing, version-control and code-review practice `[F: S41, Grade D]`.
- LinkedIn's 2025 list shows research assistants among the most common prior roles of AI engineers `[F: S07, Grade C]`, so academic-adjacent people do make the move.

**Implication `[M]`.** The PhD barrier is mostly craft translation and market structure, not knowledge. Lab research slots are scarce, so the plannable path is applied AI engineering, applied science or research engineering.

### KF-9. No longitudinal timeline data exists; self-reports are survivor-biased (Grade D)

**Evidence**
- React developer to AI engineer in 8 months while employed full-time `[F: S10, Grade D]`. The author also completed a master's thesis in that window, which confounds the hours.
- A job-board playbook offers 4-6 months focused with one shipped project, 7-9 months part-time, and 12+ months self-paced without shipping `[F: S37, Grade D]`.
- A vendor reference class for **zero-experience** career changers: a 9-month part-time software-engineering bootcamp plus up to 10 months of job search, i.e. 14-19 months in total `[F: S36, Grade D]`.
- A mentoring marketplace estimates 6-18 months for a working data scientist with a Python foundation to move into ML engineering, and 12-24 months for career changers into ML engineering generally `[F: S39, Grade D, vendor; ML engineering rather than GenAI]`.
- A Big Tech engineer's first-person account planned 18 months and moved internally to an AI-building team first `[F: S50, Grade D]`.

**Searched and not found:** longitudinal cohort studies of GenAI career changers; any denominator of attempts versus successes; GenAI-specific course or bootcamp outcomes that are not vendor-reported; time-to-offer by background.

**What recurs.** Shipping a real, evaluated system beats credentials. Internal transfer to an AI-building team is repeatedly named as the fastest route (Janvi Kalra's account at Coda, the Amazon engineer account, an Instagram infrastructure engineer's move to AI/ML training infrastructure with no interview prep, and the job-board playbook) `[F: S09, S37, S50, S51]`. Internal moves are not automatic: the Amazon engineer was rejected by several internal teams before landing on an Ads GenAI team `[F: S50]`.

**Implication `[M]`.** Every timeline claim is a survivor-biased self-report. This file therefore **models** durations from explicit assumptions (Detailed Findings D2) instead of quoting a median it cannot support.

### KF-10. Hours, not compute, are the binding constraint (Grade A data + `[M]` derivation)

**Evidence.** BLS American Time Use Survey 2025 (released 25 Jun 2026): adults averaged 5.2 hours of leisure and sports per day, with television about half of that (2.6 hours). Employed adults in households without children under 18 averaged 4.5 hours per day, more than an hour above employed adults with a child under 18. Adults aged 35-44 averaged 3.9 hours. Full-time employed people worked 8.1 hours on days worked `[F: S28, Grade A]`. The survey was suspended during the Oct-Nov 2025 federal shutdown, which may affect estimates.

**Derived `[M]`.** 4.5 h/day is about 31.5 h/week, and roughly 3.4 h/day (about 24 h/week) is an upper bound for employed parents. A 9 h/week study plan consumes about 29% (no children) to 38% (children) of average leisure. A 17.5 h/week plan consumes about 56% to 74%. A 38 h/week plan exceeds all average leisure and implies a sabbatical, notice period or reduced work hours.

**Implication.** Three tiers are used throughout: **A** (8-10 h/week), **B** (15-20 h/week), **C** (35-40 h/week).

### KF-11. Job-search friction adds roughly 2-4 months with a fat right tail (Grade C)

**Evidence.** Huntr's Q2 2026 report: median 82 days from first saved job to first offer among searches that recorded an offer (108 days in Q1) `[F: S29, Grade C; survivorship, since only successful searches are counted]`. Ashby's 2026 trends, via secondary summaries, show a median time-to-hire of about 40 days for technical roles (per process, from the candidate's side), while another Ashby-derived summary puts median time to first fill near 75 days for technical roles (from job opening) `[F: S30, Grade C]`. LinkedIn's own research says US applicants per open role have doubled since spring 2022 `[F: S47a, Grade A]`, and its March 2026 workforce report puts US hiring 23% below its February 2020 pace `[F: S47b, Grade A]`.

**Implication `[M]`.** Budget 2-4 months of search on top of skill-building. Begin applying when roughly 70% of build gates are passed.

### KF-12. Compute and course access are cheap relative to time (Grade A / B)

**Evidence**
- Modal: the Starter plan includes USD 30 of monthly free credits. Per-second GPU prices are USD 0.000164 (T4, about 0.59/h), 0.000222 (L4, about 0.80/h) and 0.001097 (H100, about 3.95/h). Startup and academic credit programs exist, with amounts that vary across snapshots `[F: S21, Grade A]`.
- RunPod: per-minute billing and a credits program of up to USD 25K appear on the official page. Third-party trackers from Aug-Sep 2026 list RTX 4090 at about 0.34/h (community) to 0.69/h (secure) and H100 PCIe at about 1.99 to 2.89/h `[F: S22, Grade A for billing and credits, C for prices]`.
- Lambda: snapshots disagree (H100 SXM about 3.99-4.29 per GPU-hour on the instances page; older cached snapshots show 2.99-3.29), so verify live `[F: S23, Grade B/C]`.
- Kaggle: session limits are documented (12 h GPU/CPU, 9 h TPU, per a third-party read of the docs). The weekly GPU quota, commonly reported near 30 h, is not published in the docs I could see. Free GPUs are 16 GB-class `[F: S24, Grade C]`.
- Hugging Face Learn offers free LLM, Agents (with a free certificate), MCP and smol (post-training) courses `[F: S25, Grade A]`. DeepLearning.AI offers free short courses including *Evaluating AI Agents* `[F: S26, Grade B/C]`.
- Most teams adapt models by prompting, tool tuning and RAG; fine-tuning is 26% `[F: S02]`.

**Implication `[M]`.** API credits plus a free notebook tier are enough for months 1-6 of application-layer work. GPU spend matters mainly for inference-literacy and fine-tuning labs (DS, PhD, backend) and is small in absolute terms: 100 GPU-hours on a 24 GB card is roughly USD 35-70 at community or secure rates.

---

## Recommendation

### R0. Decision frame

Commit to **one archetype route and one hours tier for the next 90 days**. Judge progress by four pass/fail gates (G1-G4, defined in D3), not by hours logged or courses finished. At month 6, re-plan from your interview-funnel numbers rather than from optimism. `[M]`

### R1. Cross-cutting rules (all five archetypes)

1. **Build the eval harness before the second feature.** Evaluation is the survey's top-ranked stack challenge and the most consistent theme in hiring write-ups (KF-4).
2. **Try internal first.** Spend 6-8 weeks seeking a scoped AI assignment at your current employer, in parallel with any external search. It converts the tacit experience that KF-2 says is protected into AI credit. Evidence is four practitioner accounts (Grade D), and internal moves are not automatic, but the mechanism is consistent with the Stanford finding `[S01, S09, S37, S50, S51]`.
3. **Target lateral level and the right loop type.** Three loops need different preparation `[M, from S09, S11, S40]`:
   - *Applied-AI startups, dev-tool and vertical-AI companies:* take-homes (retrieval plus evals), agent debugging, a scoping or customer-style round.
   - *Big-company ML/AI loops:* algorithmic coding, system design and ML design.
   - *Frontier labs:* highly selective; an upside, not a base case.
4. **Choose the hours tier honestly** (KF-10). If your logged hours fall below 70% of plan for three consecutive weeks, move to the next-longer column in R2 instead of pushing harder.
5. **Make every artifact verifiable by a stranger:** a repo that runs, an eval table with numbers, a written failure analysis, a deployed endpoint or demo.
6. **Skip foundations-first sequencing for application roles.** The one detailed retrospective dropped a four-week theory block as low-yield `[S10]`, while SEO "roadmaps" are typically math-first. This is untested (Grade D). Reverse it for the PhD research-engineer track, where depth is the differentiator.
7. **Freeze stack choices for six weeks at a time.** Invest in durable concepts (context, retrieval, tool schemas, evals), not API surfaces: AI SDK 6 and WebMCP both changed shape within months `[S19, S20]`.
8. **Do not mix funnels.** Expert-contract work, AI PM, FDE and AI engineering have different gatekeepers and different proof.

### R2. Per-archetype recommendation and modeled time to first offer

"Range" means all-low versus all-high model parameters (D2), **not** a statistical interval. Months are calendar months from the start of the plan.

| Archetype | Recommended route | Target level | Tier A (8-10 h/wk) | Tier B (15-20 h/wk) | Tier C (35-40 h/wk) | Confidence |
|---|---|---|---|---|---|---|
| 1. Backend/Systems (5+ yrs) | Lateral move to applied AI engineer; specialize in reliability, evals-in-CI and cost control | Mid-Senior | ~10 mo (6-14) | **~6 mo (3.5-8)** | ~3 mo (2-4.5) | Medium-low |
| 2a. Data Scientist | Reposition as AI engineer with an evals/error-analysis edge; close the production gap in the first 90 days | Mid (watch for down-leveling) | ~13 mo (9-19) | **~8 mo (5-11)** | ~5 mo (3-6.5) | Low |
| 2b. BI Analyst | Analytics-AI engineer: text-to-SQL and analytics copilots with execution-accuracy evals; learn Python seriously | Junior-Mid | ~18 mo (12-26) | **~11 mo (7-15)** | ~6 mo (4-8) | Low |
| 3. Frontend/Full-Stack | AI product / full-stack engineer, with agent-UX and (optionally) on-device AI as differentiators | Mid | ~12 mo (8-18) | **~7 mo (5-11)** | ~4 mo (3-6) | Low |
| 4a. Non-technical, 5+ yrs domain/product/ops, targeting AI-adjacent roles | Choose one lane: AI PM, AI ops/enablement, domain-evaluation lead, solutions/FDE-adjacent | Senior in domain | ~10.5 mo (7-16) | **~7 mo (5-11)** | ~5 mo (3.5-8) | Low |
| 4b. Non-technical targeting an *engineering* role from zero code | Out of the 12-month horizon; treat as a 2-year plan | Junior | not meaningful (~39 mo) | **~22 mo (15-34)** | ~12 mo (8-18) | Low |
| 5. Academic/Quant PhD (can code) | Applied AI engineer, applied scientist or research engineer; research-scientist roles are upside only | Mid | ~13 mo (9-20) | **~8 mo (5-12.5)** | ~5 mo (3-8) | Low |

**Reading the table.**
- Internal transfers can beat these numbers, but there is no timing data (KF-9).
- Expert-contract evaluation gigs (Archetype 4) can start in weeks. That is paid AI-adjacent work, not the same outcome as the "first offer" modeled here.
- Tier B is the central planning case. Tier A roughly adds 4-6 months for most archetypes. Tier C removes about half the time but needs a sabbatical, notice period or reduced work hours.
- The model is anchored on the only calibrations available: an 8-month employed retrospective for a frontend developer (KF-9), a 14-19 month vendor reference class for zero-experience changers (KF-9), and Huntr's 82-108 day search medians (KF-11).

### R3. What to do in the next 14 days

1. Run the diagnostic in D9 (skills matrix plus three fast tests) and write down your score.
2. Pick an archetype route and an hours tier. Block the calendar and compare the hours against the ATUS-based budget in KF-10.
3. Choose one real corpus or task from your own domain and hand-write **30 evaluation cases** from real work. This is the prerequisite for G1.
4. Ship a v0 in two weeks using a hosted model API, logging every trace.
5. Identify an internal sponsor or AI initiative and ask for a scoped assignment.
6. Open free accounts only (Hugging Face, Modal credits, Kaggle). Do not pay for GPUs yet (KF-12).
7. Put G1-G4 on the calendar and schedule a monthly review that records funnel numbers: applications, screens, take-homes, onsite loops, offers.

---

## Alternatives Considered

| Alternative | What it offers | Why not the default | Evidence |
|---|---|---|---|
| **A1. Full-time immersion** (Tier C) | Fastest modeled path (3-5 months); structure; peer network. Examples: a selective 10-week fellowship advertised at 80-100 h/week; a four-month research residency with stipend (Anthropic Fellows, disclosed conflict of interest). | Selective, costly in opportunity terms, outcome claims are promotional and unverified, and 80-100 h/week is a regime this model does not cover. Best when you have 6+ months of runway and a strong skill base (backend, full-stack, DS). | `[S42 Grade C/D; S32 Grade B self-reported]` |
| **A2. Degree (online or part-time MS)** | A credential; 72% of AI-engineering postings state a degree requirement. | I found no evidence on degree versus portfolio effects for career changers, and recalled durations (2-3+ years part-time) exceed the 12-month horizon. Worth considering only for research-heavy targets where you lack a graduate degree. | `[S04 Grade C; duration recalled, Grade D]` |
| **A3. Stay and AI-augment the current role** | Lowest risk. Stanford finds employment flat or rising where AI complements work, especially for experienced workers. This is also step one of the internal-first route. | No title change, and no external signal unless you also ship and publish artifacts. | `[S01 Grade A]` |
| **A4. Adjacent roles** (ML/data platform, solutions engineering, FDE, AI PM) | May fit some archetypes better: backend to FDE or platform; non-technical to AI ops. FDE postings are growing fast from a small base. | Different proof requirements and gatekeepers; some require customer-facing skills. | `[S34 Grade B]` |
| **A5. Contract or freelance bridge** | Fast paid exposure: expert-evaluation marketplaces; AI consulting for seniors. | Volatile (at-will contracts), credential-gated, and increasingly mixed with LLM judges (Mercor reports 89% agreement between its benchmark judge panel and human raters, which does not measure demand). AI consulting skews to people with about 8 years of experience. | `[S33 Grade C/D; S06 Grade C]` |
| **A6. Wait** | Avoids chasing a possible bubble. | The artifacts this plan produces (evals, observability, reliability, domain rubrics) are valuable in your current role too, so the plan has low regret. The bubble argument I found was an opinion piece (Grade D). | `[M]` |

**Decision rules** `[M]`
- Employer has an AI initiative and a transfer is possible: go internal-first; Tier A can suffice.
- Runway of 6+ months and a strong base (backend, full-stack, DS): consider compressing with Tier C.
- Under 8 h/week available: plan a 12-18 month horizon, or pick an adjacent role.
- Non-technical with under 5 years of domain experience: build domain depth first; do not expect an AI-specific role inside 12 months.

---

## Detailed Findings

Sections D1-D3 cover shared structure (loop types, the time model, the milestone gates). D4-D8 are the five archetype roadmaps. D9-D11 hold the skills diagnostic, the tool catalog and cross-cutting cognitive traps.

### D1. Roles, levels and loop types

**"AI engineer" is a discipline more than a stable job spec.** A practitioner who interviewed with 46 companies while moving from software engineering to AI engineering reported no standard AI-engineer interview format `[F: S09, snippet, Grade C]`. Preparation therefore has to be matched to the *loop type*, not to the title. `[M]`

| Loop type | Reported content | Favors | Prep priorities | Evidence |
|---|---|---|---|---|
| **Applied-AI startup, dev-tool or vertical-AI company** | Four to five rounds. A take-home of the shape "answer questions over about 50 documents and report recall@5 and faithfulness on a 20-question set" is described in one write-up. Agent debugging, scoping and a customer-style conversation round. | Software engineers; DS with deploy skills; domain experts for vertical AI | Retrieval judgment, evals, error analysis, cost/latency, communication | `[S11, S12, S14 Grade C/D]` |
| **Big-company ML/AI loop** | Algorithmic coding, general system design, ML system design, behavioral. Candidates from ML/DS backgrounds report system design and coding as the deciding rounds. | Backend/systems engineers | DSA practice, distributed-systems design, ML design | `[S40 Grade D]` |
| **Frontier lab / research residency** | Highly selective. Fellowships and research-engineer tracks are an entry route; the lab's own fellowship page says no PhD or prior ML experience is required. | Strong engineers; PhDs | Research taste plus engineering depth; treat as upside | `[S32 Grade B, conflict of interest]` |

**Seniority.** Axial reports 35% of postings at mid-level and 31% at senior level (about 66% individual-contributor overall; the part of the page I read gave no entry-level share), and LinkedIn reports median experience of 3.7 years for AI engineers `[S04, S06 Grade C]`. Together these suggest a market weighted toward mid and senior hires that does not demand a decade of AI-specific experience. That is encouraging for lateral pivots. The Stanford evidence (KF-2) says the squeeze falls on people *without* prior experience, so lateral entry is the better-protected route.

### D2. Weekly hours versus pivot duration: the model

**What this is.** A transparent calculation, not data. Every number below is `[M]` (Grade D). It exists so that you can change the assumptions, and so that no unsupported "median" is presented as fact.

**Formula**

```
effective_hours_per_week = nominal_hours_per_week x adherence
build_weeks              = H_core / effective_hours_per_week
weeks_to_first_offer     = build_weeks + search_lag_weeks
months                   = weeks / 4.345
```

`search_lag` is the time after the build ends. It is shorter than the full search because applications begin at about 70% of the build. Calibration: Huntr's 82-108 day medians (about 12-15 weeks) run from the first saved job, minus roughly 3-4 weeks of overlap `[S29]`.

**Parameters**

| Tier | Nominal h/week | Adherence | Effective h/week | Who it fits |
|---|---|---|---|---|
| A | 9 | 0.75 | 6.75 | Employed, caregiving or heavy work load |
| B | 17.5 | 0.75 | 13.1 | Employed and disciplined (central planning case) |
| C | 38 | 0.85 | 32.3 | Sabbatical, notice period, bench time, full-time program |

| Archetype | H_core (hours): central (low-high) | Search lag (weeks): central (low-high) | Why |
|---|---|---|---|
| Backend/Systems 5+ yrs | 250 (150-350) | 6 (4-8) | Skips systems basics; mainly needs LLM patterns and evals |
| Frontend/Full-Stack | 300 (200-450) | 9 (6-12) | Adds a Python/service layer, retrieval and evals; demand is thinner |
| Data Scientist | 300 (200-450) | 11 (8-14) | Production hygiene plus loop-specific prep (coding, system design) |
| BI Analyst | 450 (300-650) | 12 (8-16) | Needs Python and ML-adjacent depth on top of the above |
| Non-technical, AI-adjacent roles | 200 (120-300) | 16 (12-24) | Fewer hours but a smaller, relationship-driven market |
| Non-technical, engineering from zero code | 1,000 (700-1,500) | 20 (12-32) | Includes learning to program; entry-level squeeze applies |
| PhD, applied roles | 300 (200-450) | 12 (8-20) | Strong on theory; needs engineering craft and loop prep |

**Results (months to first offer; central, with low-high range)**

| Archetype | Tier A | Tier B | Tier C |
|---|---|---|---|
| Backend/Systems | 9.9 (6.0-13.8) | 5.8 (3.6-8.0) | 3.2 (2.0-4.3) |
| Data Scientist | 12.8 (8.7-18.6) | 7.8 (5.3-11.1) | 4.7 (3.3-6.4) |
| BI Analyst | 18.1 (12.1-25.8) | 10.7 (7.1-15.1) | 6.0 (4.0-8.3) |
| Frontend/Full-Stack | 12.3 (8.2-18.1) | 7.3 (4.9-10.7) | 4.2 (2.8-6.0) |
| Non-technical, AI-adjacent | 10.5 (6.9-15.8) | 7.2 (4.9-10.8) | 5.1 (3.6-7.7) |
| Non-technical, engineering from zero code | 38.7 (26.6-58.5) | 22.1 (15.0-33.7) | 11.7 (7.7-18.1) |
| PhD, applied roles | 13.0 (8.7-19.9) | 8.0 (5.3-12.5) | 4.9 (3.3-7.8) |

R2 rounds these values. The "range" is all-low to all-high parameters, which is wider than a realistic interval.

**Checks against the few anchors available**
- *Frontend retrospective* `[S10]`: 8 months employed, with hours not stated. A 12 h/week nominal plan (9 effective) with the Frontend parameters gives about 9.7 months. That is within the modeled Tier A and B ranges, so the model is not obviously optimistic. One anecdote cannot validate it.
- *Zero-experience reference class* `[S36]`: the vendor's 14-19 months total compares with about 22 months (15-34) at Tier B for engineering from zero code. The model is somewhat more pessimistic, which is plausible because the vendor sells the program.
- *Data-scientist reference class* `[S39]`: a mentoring marketplace's 6-18 months for a working data scientist with a Python foundation moving into ML engineering overlaps the model's Data Scientist range (5.3-11.1 months at Tier B; 8.7-18.6 at Tier A). It is a vendor estimate for ML engineering, not GenAI engineering.
- *Conditioning.* All values are **conditional on persisting and eventually succeeding.** The probability of success is unknown because no denominators exist (KF-9). Survivorship bias runs through every self-report used as an anchor.

**Time budget against the ATUS data (KF-10)**

| Tier | Share of average leisure, employed adult with no child under 18 (about 31.5 h/week) | Share, employed adult with a child under 18 (about 24 h/week or less) |
|---|---|---|
| A (9 h) | 29% | 38% |
| B (17.5 h) | 56% | 74% |
| C (38 h) | 121% (not possible alongside full-time work) | 160% (not possible) |

These are averages, not personal capacity. The ATUS leisure category includes television (2.6 h/day on average) and socializing, so the figure is the maximum that can plausibly be traded, not a recommendation to trade all of it.

**Sensitivity `[M]`.** Adherence of 0.6 instead of 0.75 stretches the build phase by 25%. Doubling the search lag adds about 1.4-3.7 months depending on archetype. Doubling H_core roughly doubles the build phase. The model is most sensitive to H_core, the least-validated parameter. Hence the milestone gates in D3, which let you recalibrate H_core from your own progress by month 3.

### D3. The shared milestone spine (G1-G4)

Each archetype's roadmap in D4-D8 specializes this spine. Deliverables are `[M]` (author-designed), and each is mapped to a hiring signal that appears in the sources.

| Gate | Due (Tier B) | Required artifacts | How a stranger verifies it | Evidence anchor |
|---|---|---|---|---|
| **G1 Measured v0** | End of month 3 | A running LLM application (retrieval and/or tool use) over a real corpus or task from your domain. At least 50 labeled eval cases (at least 30 hand-written from real work), versioned with the code. At least 2 baselines compared (for example no retrieval, BM25 only, long-context stuffing). An error taxonomy from at least 100 reviewed traces, with counts. A written "what broke" memo of 500+ words with three specific failures. | Reproduces the headline eval numbers from the README in under 30 minutes. | Take-home shapes `[S11]`; eval-first lesson `[S10]` |
| **G2 Operable v1** | End of month 6 | Eval suite runs in CI on every prompt, model or retrieval change, with a regression threshold. If an LLM judge is used: validated on at least 100 human-labeled examples with agreement reported and at least one bias (position or verbosity) tested. Tracing plus a cost and latency view (p50/p95, cost per request). Deployed to at least one real user other than you. One postmortem of a real regression, with the test that now prevents it. | CI badge and log; judge-agreement table; a live URL or recorded demo; a postmortem document. | Generic-metric and unvalidated-judge pitfalls `[S15]`; cost shaping ambition for 40% `[S02]`; observability and in-house tooling `[S08]` |
| **G3 Second pattern and external proof** | End of month 9 | A second system with a *different failure surface* (tool-using agent with approvals and budgets; on-device or browser module; domain benchmark; serving lab). One public write-up with numbers and one external contribution (OSS PR, talk or community review). At least 5 mock loops of the target loop type. At least 15-20 *targeted* applications, not mass applications. | Public links; mock-loop feedback notes; a tracker of applications and outcomes. | Visibility mattered after five months of private work `[S10]` |
| **G4 Convert or re-plan** | End of month 12 | At least one offer or internal role change, **or** a written funnel diagnosis (where you lose between screen, take-home, onsite and offer) and a re-plan that changes loop type, level or tier. | Offer letter, or the diagnosis document reviewed by one practitioner. | Search friction `[S29, S47a, S47b]` |

**Gate failure rules `[M]`** (heuristics, Grade D)
- G1 not passed by the end of month 4 at Tier B: check adherence first. Then check for scope creep and for the absence of an eval set. Move to the next-longer tier before adding hours.
- G2 not passed by month 8: the system is probably over-scoped. Cut features and keep the eval and CI.
- No screens after 15 targeted applications: the problem is positioning or résumé signal, not skill. Get a practitioner review of the artifacts and the résumé.
- Three failed take-homes: invest in eval design and error analysis.
- Failed onsites at system design: practice system design and DSA for big-company loops, or retarget applied-AI loops.

---

### D4. Archetype 1: Backend / Systems Software Engineer (5+ years, Java/Go)

**Profile.** Owns services, concurrency, queues, observability and on-call. Likely gaps: the Python ecosystem (if Java/Go only), LLM API patterns, retrieval, evaluation and probabilistic thinking.

**What plausibly transfers `[M]`, with the evidence found.**
- Production habits (testing, CI/CD, observability, rate limiting, caching) transfer directly. Mature teams in Pragmatic Engineer's reporting built much of their AI tooling in-house. Examples include Sentry, which chose not to adopt LangChain, and incident.io, which used Postgres with pgvector alongside Go `[S08, Grade B]`.
- In one case, in-house developers with no prior AI experience built a feature in about two months after an agency had quoted six to nine months `[S08, Grade B, single case]`.
- A hiring-side post argues that LLM-engineering success rests on failure-mode intuition built by shipping systems that failed in production, and that years of classical ML work (fine-tuning classifiers, for example) are transferable but not equivalent `[S12, Grade D]`. If true, production scars matter more than model theory, which favors engineers who have run systems in production. Unverified.

**Mandatory skill deltas (ranked by size of gap) `[M]`**
1. **Evaluation design and error analysis.** The largest gap, and the one KF-4 identifies as the bottleneck.
2. **LLM API fluency and context engineering:** structured output, tool calling, streaming, token budgets.
3. **Retrieval:** hybrid (keyword plus dense) search, chunking, reranking, and knowing when not to retrieve.
4. **Python** (async, typing, pydantic) if coming from Java/Go.
5. **Agent reliability:** loop limits, budgets, approvals, replayable traces.
6. **A domain model of what "good" looks like** for your application. Systems engineers often skip this, and quality cannot be judged without it.

**Unlearning traps and biases**

| Trap | What it looks like | Evidence |
|---|---|---|
| Determinism assumption | Expecting 100% pass rates; treating a flaky eval as a bug in the test rather than a property of the system. Pass-rate thresholds are a product decision, not a correctness target. | Argument by Hamel Husain as relayed by Simon Willison `[S16, snippet, Grade C]`; Wordsmith CEO on non-determinism `[S08]` |
| "It's just an API call" | Underestimating the data and evaluation work behind a good answer. | `[M]` |
| Retrieval by default | Reaching for a vector database before measuring; skipping keyword search. The 8-month retrospective reports a large keyword-recall gain from hybrid retrieval plus a reranker. | `[S10, Grade D]` |
| Framework-first | Learning orchestration frameworks before the underlying patterns. Framework APIs churn. | `[S08, S20, S37]` Grade C/D |
| Infra-polish before measurement | Building a beautiful platform around a system whose quality has never been measured. | `[M]` |

*Cognitive biases:* competence-transfer overconfidence (assuming systems skill covers evaluation), infra bias (solving the problem you already know how to solve), and demo bias (judging quality from three examples).

**Quarterly roadmap (Tier B; add about 4 months at Tier A)**

| Months | Focus | Deliverables (code, eval, deployment) | Gate |
|---|---|---|---|
| **1-3** | Fluency plus a measured v0 | Week 1-2: Python fluency if needed. Hosted-model API with structured output, tool calling and streaming. v0 of a Q&A or task app over a corpus you know (company public docs, an open-source project's docs and issues, or a domain dataset). Week 3-6: 50 eval cases, harness with a metrics table (retrieval recall@k, answer correctness against a rubric, citation faithfulness), two baselines. Week 7-12: error analysis on 100+ traces, fix the top three failure classes, test hybrid retrieval and a reranker, log cost and latency, write the memo. | **G1** |
| **4-6** | Make it operable | CI job running the eval suite with a regression threshold. LLM-judge calibration against 100+ human labels. Tracing (any open-source or hosted tracer). Timeouts, retries, budgets and idempotent tool calls. Container deployment to any cloud or Modal. A real user. Load test. One postmortem. | **G2** |
| **7-9** | Second pattern and proof | Tool-using agent with human approval, per-run budget, sandboxed tools, deterministic replay of traces, and failure-injection tests (tool timeouts, malformed arguments, prompt-injection attempts). *Serving lab:* run an open-weight model on Modal, RunPod or Lambda and measure tokens/s, p95 latency and cost per million tokens against an API (cost and speed are the biggest challenge for 16% of survey respondents `[S02]`). Public write-up, one OSS contribution, 5+ mock loops, 15-20 targeted applications, an internal-role conversation. | **G3** |
| **10-12** | Convert | Run loops. Practice one eval-design round and one LLM system-design round. Prepare one failure story with data. Target applied AI engineer, AI platform/infrastructure and FDE-adjacent roles at your current level. | **G4** |

**Realistic state by checkpoint (Tier B) `[M]`**
- **Month 3:** G1 passed, one public artifact. Offers are unlikely unless the route is internal or FDE-adjacent.
- **Month 6:** G2 passed, interviews active. The modeled median first offer is here (range 3.6-8.0 months).
- **Month 9:** second pattern shipped. Most who persisted have an offer or decisive loop feedback.
- **Month 12:** offers for many who held to the gates; otherwise a funnel diagnosis (G4).

**Portfolio specialization.** A *reliability layer for LLM applications*: a small, well-tested gateway and harness with caching, backoff, budgets, fallbacks, trace replay, eval-regression CI and a public log of postmortems. It plays to your comparative advantage and differs from the RAG-chatbot portfolios that hiring write-ups describe as commonplace `[S11, S13, Grade D]`.

**Domain probe: median time to first offer for a 5+ year Java/Go engineer pivoting while employed full-time.**
- *Searched:* Pragmatic Engineer, MentorCruise and other retrospectives, LinkedIn Economic Graph and Jobs on the Rise summaries, Huntr and Ashby search benchmarks, job-board playbooks.
- *Found:* **no direct empirical median.** Anecdotal anchors are 8 months (a React developer, employed) and 4-9 months (a job-board playbook), plus a planned 18 months at one Big Tech engineer `[S10, S37, S50, Grade D]`.
- *Modeled:* about 6 months (3.6-8.0) at Tier B and about 10 months (6.0-13.8) at Tier A.
- *Verdict on P1's "6-9 months":* **plausible but unverified.** It spans the Tier B to Tier A boundary.

**Evidence summary for D4.** Transfer claims: Grade B for the in-house-build case, Grade D for the rest. Roadmap: `[M]`, anchored on `[S10, S11, S15]`.

---

### D5. Archetype 2: Data Scientist / BI Analyst

**Profile.**
- *Data Scientist:* statistics, ML, experimentation, SQL, notebooks. Likely gaps: production code, deployment, system design, on-call ownership.
- *BI Analyst:* SQL, metric definitions, dashboards, stakeholder communication. Likely gaps: Python, ML-adjacent skills, software engineering.

**What disqualifies Data Scientists in production AI loops: a ranked hypothesis list `[M]`.** I found **no frequency data**. The ranking below is built from guides and candidate-reported accounts (Grade D) and should be tested against your own funnel feedback.

| Rank | Deficiency | Evidence |
|---|---|---|
| 1 | Coding-round performance (algorithmic problems, clean code under time pressure) in big-company loops | Candidate reports `[S40, Grade D]` |
| 2 | System design (services, queues, scaling, LLM-app design) | A Glassdoor review says system design was emphasized and was the stated reason for rejection `[S40, Grade D]` |
| 3 | No production-ownership artifacts or stories: deployed, monitored, rolled back | Guides `[S39, Grade D/C]` |
| 4 | Operational thinking: latency, cost, failure modes | `[S39, S11, Grade D]` |
| 5 | Customer-facing scoping and communication | `[S11, Grade D]` |

*Absent from the evidence:* statistics or ML knowledge as the main disqualifier in GenAI *application* loops. No source I found cited it. That is an absence of evidence, not proof.

**Mandatory skill deltas (Data Scientist) `[M]`**
1. Production hygiene: typed, tested, installable Python; containers; CI/CD.
2. LLM application patterns: API fluency, structured outputs, tool use, retrieval.
3. Serving and operations: an API service with async handling, retries, auth, observability and cost tracking.
4. Loop preparation: DSA-style coding and system design for big-company loops.
5. Product scoping and communication.

*Strengths to leverage* (KF-5): error analysis, metric design, experimental design, judge validation `[S15]`.

**Unlearning traps and biases**

| Trap | What it looks like | Evidence |
|---|---|---|
| Train-first identity | Fine-tuning before establishing that prompting and retrieval fail. Only 26% of surveyed teams fine-tune, versus 80% prompting. | `[S02, Grade B]` |
| Notebook as deliverable | A notebook is not a service. | `[S39 Grade D]` |
| Generic and unvalidated metrics | Off-the-shelf "helpfulness" or "hallucination" scores, and LLM judges never checked against human labels. | `[S15, Grade C]` |
| Perfectionism and months on theory | Spending weeks on derivations before shipping an API. The 8-month retrospective dropped a four-week theory block as low-yield. | `[S10, Grade D]` |
| Undervaluing cost and latency | Ignoring that 40% of surveyed teams say cost shapes their ambition. | `[S02]` |
| *BI-specific:* dashboard thinking | A chat box bolted onto a dashboard with no evaluation of generated SQL or narrative. | `[M]` |

*Cognitive biases:* expertise anchoring (assuming statistical rigor automatically transfers; LLM judges still need validation), the streetlight effect (analysis where the tooling is comfortable) and the tool-hammer effect.

**Quarterly roadmap: Data Scientist (Tier B; add about 5 months at Tier A)**

| Months | Focus | Deliverables | Gate |
|---|---|---|---|
| **1-3** | Package discipline plus a measured v0 | Refactor one prior analysis into an installable package with tests, type checks, Docker and CI. Build the LLM application. For G1, use the DS edge: stratified sample of traces, an error taxonomy with agreement between two reviewers, confidence intervals on every eval metric. | **G1** |
| **4-6** | Serve it and calibrate the judge | FastAPI service (async, auth, retries, timeouts) deployed. Hybrid retrieval plus reranker. A **judge-calibration study**: 100+ human labels, agreement statistic, position and verbosity bias tests, published as a write-up. Eval-in-CI. A cost-quality frontier chart across models and prompts. | **G2** |
| **7-9** | Loop readiness and a second pattern | 4-6 weeks of DSA basics (arrays, hashing, graphs, basic DP) and LLM-app system design (RAG, agents, queues, caching, rate limits). Second pattern: a cost-reducing router (small model versus frontier model chosen by a classifier), or an embedding fine-tune as a GPU lab on Kaggle or Modal. Mock loops and targeted applications. | **G3** |
| **10-12** | Convert | Loops for applied AI engineer roles and roles that emphasize evaluation. Watch for down-leveling offers and decide your floor in advance. | **G4** |

**Quarterly roadmap: BI Analyst (Tier B; add about 7 months at Tier A) `[M]`**

| Months | Focus | Deliverables | Gate |
|---|---|---|---|
| **1-3** | Python plus a text-to-SQL v0 | pandas, typing, pytest, packaging; LLM API basics. A text-to-SQL copilot over a public schema with 50 questions and gold SQL, scored by **execution accuracy** (result-set comparison). | G1-lite |
| **4-6** | Governance and CI | Metric definitions as context (semantic layer), read-only access, row limits, eval in CI, deployed as an internal tool with at least one real user. | **G2** |
| **7-9** | Agentic analysis | A second pattern with human approvals and a documented business-impact case study. | **G3** |
| **10-12** | Convert | Target analytics-AI roles in your current industry. An analytics-engineering role with GenAI scope is a reasonable bridge. | **G4** |

**Realistic state by checkpoint (Tier B) `[M]`**
- *Data Scientist:* month 3, refactored package plus eval, no offers expected. Month 6, judge study published and loops starting. Month 9, the modeled median first offer is near month 8 (range 5.3-11.1). Month 12, offers likely if the loop type matches your prep; otherwise diagnose.
- *BI Analyst:* month 3, v0 and Python fluency. Month 6, G2-lite and applications. Month 9, early offers are rare. The modeled median is near month 11 (range 7.1-15.1), so month 12 is borderline.

**Portfolio specialization**
- *Data Scientist:* an **eval and error-analysis lab.** A public golden set, error taxonomy, judge calibration with bias tests and a cost-quality frontier. It makes the DS advantage visible and verifiable.
- *BI Analyst:* an **analytics copilot with execution-accuracy evals,** read-only guardrails and business-metric semantics.

**Domain probe: which software-engineering deficiencies most often disqualify Data Scientists?**
- *Searched:* Reddit, Blind, Glassdoor, Taro and LeetCode candidate reports; MentorCruise and DataTalks.Club guides; hiring write-ups.
- *Found:* anecdotal reports and guides, **no frequency data.** Coding and system-design rounds recur in big-company loops, and production-ownership evidence recurs in guides.
- *Answer, with its grade:* the ranked list above is a Grade D hypothesis. Validate it by asking recruiters for stage-level feedback and by tracking your own funnel.

**Evidence summary for D5.** DS advantage in evals: Grade C. Disqualifier ranking: Grade D. Roadmaps: `[M]`, anchored on `[S10, S11, S15, S39]`.

---

### D6. Archetype 3: Frontend / Full-Stack Engineer

**Profile.** Strong React and TypeScript, state management, streaming, design systems, accessibility and product sense. Likely gaps: retrieval and data work, evaluation, a service layer (Python or server-side TypeScript), system design for LLM applications and inference literacy.

**What transfers `[M]`.** UX for uncertainty, streaming interfaces and product intuition. The detailed 8-month retrospective is from a React developer who also had to do real backend work: hybrid retrieval, reranking, async and caching for latency, and an eval harness `[S10, Grade D]`.

**Mandatory skill deltas (ranked) `[M]`**
1. **Evaluation and error analysis** (the largest gap).
2. **Retrieval and data:** hybrid search, chunking, reranking. This is the "backend half" of most AI features.
3. **A service layer** with auth, queues, retries and observability, in Python (FastAPI) or server-side TypeScript.
4. **Agent reliability and human-in-the-loop design:** tool schemas, approvals, budgets.
5. **Inference literacy:** tokens, context windows, latency and throughput trade-offs, on-device constraints.
6. **System design for LLM applications** (interview-grade).

**Domain probe: can client-side AI runtimes help you bypass backend-heavy competition?** *Partly. The platform is real; the demand evidence is thin and senior-skewed.* Status as of October 2026:

| Runtime or framework | Verified status | Good for | Limits and risks | Grade |
|---|---|---|---|---|
| **WebGPU** | In current Chrome and Edge, Firefox 141 (Windows) and 145 (macOS Apple Silicon), and Safari 26. Linux and some Android combinations were still in progress in Google's note. | Any in-browser model inference | Coverage varies by OS and GPU. Feature-detect and fall back to WASM or a server. | A `[S17]` |
| **Transformers.js v4** | Released 9 Feb 2026 with a new WebGPU runtime. Same code in browsers, Node, Bun and Deno. 4.1 added newer model families and KV-cache work; 4.2 added tool calling. | Embeddings, semantic search, classification, speech, small language models | Model download size, memory, cold start. Check model support per release. | A `[S18]` |
| **Chrome built-in AI (Gemini Nano)** | Translator, Language Detector and Summarizer stable from Chrome 138. Prompt API listed for web at Chrome 148 and for extensions from 138. Writer, Rewriter and Proofreader are trials. | Private, offline-capable task features in Chrome | Chrome-specific. Hardware and storage requirements apply; check the docs' requirements page. The page footer shows a 2024 date, so verify. | A `[S19]` |
| **Vercel AI SDK 6** | Agent abstraction, tool-execution approval, DevTools, full MCP support. | Streaming UIs and agent loops in TypeScript | Breaking changes between major versions. Ship date reported inconsistently by third parties. | A `[S20]` |
| **WebMCP** | Early preview Feb 2026. Chrome imperative-API docs dated 18 May 2026. Third parties report a draft spec of 21 Jul 2026, a Chrome origin trial from 149 and an API rename. | Making your site callable by in-browser agents | Draft spec; API surface changing. Prototype only. | A (Chrome docs) / C (third-party detail) `[S19]` |

**Why "bypass" is overstated.** The visible demand is for Staff-level roles asking for 5-6+ years, and listings tend to be "full-stack product engineer" or forward-deployed rather than pure frontend `[S38, Grade C/D]`. A vendor analysis describes junior frontend as oversupplied and senior frontend as tight `[S38, Grade D]`. No census of AI-frontend postings exists in what I found. The real differentiators are `[M]`: (1) UX for uncertainty, citations, partial and streaming states, cancellation and approvals; (2) on-device AI where privacy, latency, offline use or cost matter; (3) agent-ready websites. **Test the bet in your own market:** count postings that name frontend-specific AI skills against postings for full-stack AI engineers. If the former are a small minority, apply as a full-stack AI engineer and use frontend as the differentiator.

**Unlearning traps and biases**

| Trap | What it looks like | Evidence |
|---|---|---|
| UI-wrapper plateau | A polished interface over a model whose quality is never measured. | Hiring write-ups on portfolios `[S11, S13, Grade D]` |
| Model output as trusted data | Unvalidated structured output crashing the UI; no error or partial-state design. | `[M]` |
| "Streaming means done" | Ignoring time to first token, cancellation, partial JSON and retry behavior. | `[M]` |
| UX judged by vibes | No telemetry on acceptance rate, edit rate or abandonment. | `[M]` |
| Client-side inference as a universal fix | Ignoring device variance, download size, memory and battery. | `[S17, S19]` |
| Chasing API surfaces | Rebuilding for each framework release. AI SDK 6 and WebMCP both shifted shape within months. | `[S19, S20]` |

*Cognitive biases:* comfort-zone bias (staying in the UI layer and avoiding retrieval and evals), the demo effect, and novelty bias toward shiny APIs such as WebMCP.

**Quarterly roadmap (Tier B; add about 5 months at Tier A) `[M]`**

| Months | Focus | Deliverables | Gate |
|---|---|---|---|
| **1-3** | Backend-capable measured v0 | Pick a service path: Python/FastAPI for the model and retrieval layer, or a TypeScript server with the AI SDK. Build a streaming chat or agent UI over an app with retrieval. 50 eval cases with task-success scoring plus UX metrics (time to first token p50/p95, abort handling, error states). Two baselines, error taxonomy, memo. | **G1** |
| **4-6** | Citations, tools and approvals | Retrieval with citations. Tool calling with a human-approval UI. Schema-validated structured output. Judge calibration, eval-in-CI, deployment, real users, acceptance and edit-rate telemetry. One postmortem. | **G2** |
| **7-9** | On-device module and proof | A Transformers.js v4 module for browser-side embeddings or a small model on a bounded task. Measure model size, load time, throughput and accuracy against the server version on at least 3 device and browser combinations. Feature detection and a fallback. Optional WebMCP prototype behind a flag, labeled experimental. Public write-up, an accessible open-source component, mock loops, 15-20 targeted applications. | **G3** |
| **10-12** | Convert | Loops for AI product or full-stack engineer, AI-frontend engineer and forward-deployed (frontend-heavy) roles. Prepare an LLM system-design answer and an agent-UX case study with numbers. | **G4** |

**Realistic state by checkpoint (Tier B) `[M]`.** Month 3: G1 with a streaming UI and evals; offers unlikely. Month 6: G2; interviews begin. Month 9: on-device module shipped. The modeled median first offer is near month 7 (range 4.9-10.7). Month 12: offers likely for most who held to the gates.

**Portfolio specialization.** An **agent-UX lab.** Measured UX outcomes (acceptance rate, edit distance, abandonment, time to first token), approval flows and failure states. Add a *private, browser-first semantic search* with measured latency and accuracy trade-offs, and accessible open-source components.

**Evidence summary for D6.** Platform facts: Grade A. Demand: Grade C/D. Roadmap: `[M]`.

---

### D7. Archetype 4: Non-Technical Professional (Product / Operations / Domain Expert)

**Core claim (P3).** Raw-coding competition is the wrong game. The leverage is domain judgment applied to evaluation, product, operations or customer implementation. Each lane has an entry fee.

**Lanes `[M]`, with evidence**

| Lane | What it is | Entry fee found in the sources | First proof | Main risk |
|---|---|---|---|---|
| **AI Product Manager** | Owns AI feature roadmap and quality bars. A recruiting firm names four types: copilot, platform, ML-feature and AI-ops/internal-tools PM `[S35, Grade D]`. | Product fundamentals first. One recruiter's job-description template asks for 4+ years of PM experience and at least one model-powered feature shipped and measured after launch `[S35, Grade D; the vendor discloses it is paid on placements]` | PRD plus eval rubric plus pilot metrics | Credibility with engineers; many roles ask for technical fluency |
| **AI ops / enablement / internal-tools PM** | Deploys AI into non-engineering teams such as support or sales ops `[S35 Grade D]` | Operations experience, process knowledge | Pilot with adoption and time-saved metrics, a runbook and a risk register | Title confusion; budget cycles |
| **Domain evaluation specialist** (in-house lead or contract expert) | Writes rubrics, labels golden sets, adjudicates disagreements. A Husain-linked Arize post argues PMs and domain experts, not engineers, should label eval data `[S15, Grade C]`. | Credentials and seniority. LinkedIn lists data annotators fourth, with median experience 3.5 years `[S06 Grade C]`. Expert marketplaces seek advanced degrees and years of experience `[S33]`. | Golden set, rubric, inter-rater agreement | At-will contract volatility, credential gating and growing use of LLM judges alongside human experts `[S33]` |
| **Solutions / FDE-adjacent / AI consultant** | Customer-facing implementation | AI consultants/strategists have median 8.2 years' experience `[S06]`. FDE postings need coding as well `[S34]`. | Customer pilot case study | Senior bar; FDE needs code |
| **Engineering from zero code** | Learn to program, then target junior roles | About 22 months (15-34) at Tier B in this model; vendor reference class 14-19 months `[S36]` | n/a | The entry-level squeeze `[S01]` |

**What AI-assisted building changes.** In the 2026 survey, under half of respondents say non-developers ship features (mostly internal) and 17% say they regularly ship full-size customer-facing ones. 59% agree that AI-generated code creates major liabilities `[S02, Grade B]`. Building internal tools with AI help is plausible for you, but **verification is the bottleneck, so your eval skill matters more than your prompting skill.**

**Mandatory skill deltas `[M]`**
1. AI literacy beyond tool use: tokens and context, hallucination, retrieval versus fine-tuning versus prompting, cost and latency.
2. **Evaluation fluency:** write rubrics, build golden sets, measure inter-rater agreement, read error analyses. A PM-oriented guide by Husain calls evals an emerging top skill for AI PMs `[S53, Grade D]`.
3. Notebook-level data skills: SQL and basic Python to analyze eval results and logs.
4. Pilot execution: scoping, adoption measurement, change management, risk and governance documents.
5. Technical communication with engineers.

**Unlearning traps and biases**

| Trap | What it looks like |
|---|---|
| Prompt-trick identity | Collecting prompts and tool demos instead of measuring outcomes. |
| Certificate collecting | Course completions without artifacts. No source found shows certificates carrying hiring signal; the artifact-first pattern recurs `[S10, S37]`. |
| Fluency mistaken for competence | Using an AI tool well is not the same as building and evaluating a system. |
| Automation bias | Trusting fluent outputs and LLM judges without calibrating them against human labels. |
| Gig-market mirage | Treating expert-contract work as a career track; it is volatile and credential-sensitive `[S33]`. |
| Coding avoidance or overreach | Refusing any code, or shipping AI-written code without tests. |

*Cognitive biases:* the Dunning-Kruger effect after early wins, the halo effect of fluent text, and sunk cost on credentials.

**Quarterly roadmap: AI-adjacent lane (Tier B; add about 3-4 months at Tier A) `[M]`**

| Months | Focus | Deliverables | Gate |
|---|---|---|---|
| **1-3** | Domain workflow plus a golden set | Choose one lane and one workflow you know deeply (claims triage, contract review, clinical-note QA, sales-ops enrichment). Build it with hosted or low-code tools. Create a **domain golden set**: 100+ real tasks, de-identified or synthetic with permission, with rubrics, adjudication rules and agreement between two reviewers. Compare 2-3 models or prompts. Baseline is today's human process. | **G1-domain** |
| **4-6** | Pilot and measurement | Pilot with 5-10 colleagues. Measure adoption, time saved and error rate. Check LLM-judge agreement with human labels. Write a PRD or runbook and a risk register. Learn SQL and notebook Python to analyze logs. | **G2-domain** |
| **7-9** | Scale and visibility | Extend the pilot. Build a cost-per-task model and a governance and guardrails document. Present internally. Publish a de-identified write-up. Ask leadership to define a role. Start targeted applications to vertical-AI companies where domain depth is valued. Apply to expert networks only once the golden-set artifact exists. | **G3** |
| **10-12** | Convert | Loops for AI PM, AI ops or solutions roles; negotiate scope. If none lands, plan the next six months explicitly. | **G4** |

**Realistic state by checkpoint (Tier B) `[M]`.** Month 3: golden set done and pilot starting; contract evaluation work is possible earlier. Month 6: pilot results and a PRD. Month 9: internal role redefinition or interviews. The modeled median for AI-adjacent roles is near month 7 (range 4.9-10.8), concentrated in internal moves and vertical-AI companies. Engineering-from-zero is **not** achievable within 12 months at Tier A or B.

**Portfolio specialization.** A **domain gold standard:** a de-identified benchmark with rubric and agreement statistics, pilot results, a governance playbook and an AI-ops runbook. It is the artifact engineers cannot produce without you.

**Domain probe: viable, high-leverage niches for non-technical professionals.**
1. **Domain evaluation lead** (in-house first): highest leverage because evaluation is the top stack challenge (KF-4) and domain experts should own the labels.
2. **AI ops / enablement PM:** deploying AI into an operating team you already understand.
3. **AI PM** (if you already have product fundamentals).
4. **Solutions / FDE-adjacent roles:** need seniority and, for FDE, some coding.
5. **Expert-contract evaluation:** a bridge, not a destination.

*Evidence grade:* Grade C (LinkedIn, Fortune/Lightcast, vendor and marketplace sources). *Searched and not found:* transition timelines or success rates for AI PM or AI-ops moves, and any systematic data on how long expert-contract demand will last.

---

### D8. Archetype 5: Academic Researcher / Quantitative PhD

**Profile.** Strong in mathematics and statistics, experimental design, literature reading and deep specialization. Likely gaps: production engineering craft, iteration speed, scoping for product value, communication with non-experts, baseline discipline, and an accurate picture of where roles exist.

**Two tracks `[M]`.** *T1:* applied AI engineer or applied scientist at a product company. *T2:* research engineer or scientist at a lab. This plan targets T1 and treats T2 as upside.

**Domain probe: what translation barriers stop PhDs succeeding in fast-paced commercial GenAI product engineering?**
*Searched:* DataTalks.Club interviews, Arize's physicist-to-ML-engineer retrospective, practitioner posts, and a PhD-to-industry write-up. *Not found:* systematic studies of PhD-to-industry AI transition outcomes. The barriers below are therefore Grade D, except where noted.

| # | Barrier | What it looks like | Evidence |
|---|---|---|---|
| 1 | Collaborative engineering craft | Research code does not survive review, tests or shared ownership. One researcher-turned-engineer says the hardest part was producing code with others, having never been through code review. | `[S41, Grade D]` |
| 2 | Shipping under constraints | Producing code between meetings and for shared systems, rather than at the pace of a research project. | `[S41, Grade D]` |
| 3 | Value framing | Optimizing a benchmark when the user's outcome is the metric. | `[M]`; no source verified in the final pass |
| 4 | Baseline discipline | Reaching for a sophisticated method before beating BM25 or a plain prompt. | `[M]`; compare `[S10]` |
| 5 | Scoping and communication | Weak performance in customer-style or scoping rounds. | `[S11, Grade D]` |
| 6 | Market structure | Supply of new AI PhDs rose 22% from 2022 to 2024 and the growth went to academia. The derived industry-bound count is roughly flat. | `[S31, Grade A headline; derivation M]` |
| 7 | Loop preparation | Big-company loops test DSA-style coding and system design, which a research career rarely exercises. A PhD-to-industry write-up says engineering-track candidates should expect standard DSA and system-design prep. | `[S40, S41, Grade D]` |

**Mandatory skill deltas `[M]`**
1. Production engineering: tests, packaging, CI, code review, containers.
2. LLM application patterns: API fluency, retrieval, tool use.
3. Evaluation at production fidelity: golden sets, judge calibration, drift monitoring. *This is a strength to lean on.*
4. Product scoping and communication.
5. Loop preparation (DSA, system design).
6. Inference economics (cost and latency).

**Unlearning traps and biases**

| Trap | What it looks like |
|---|---|
| Novelty bias | Using the newest method before establishing that a baseline fails. |
| Perfectionism and over-engineering | Slow iteration, delayed first release. |
| Publication mindset | Optimizing for paper-grade results rather than decision-useful ones. |
| Benchmark fixation | Treating leaderboard gains as product gains. |
| Solo-coding habits | No tests, no review, private repos. |
| Prestige signaling | A CV of papers where a repo of shipped, evaluated systems is wanted. |
| Over-targeting lab research slots | Survivorship bias in lab success stories; slots are scarce (KF-8). |

*Cognitive biases:* not-invented-here, survivorship bias, curse of knowledge when explaining to non-experts, and availability of papers over practitioner posts.

**Quarterly roadmap: applied track (Tier B; add about 5 months at Tier A) `[M]`**

| Months | Focus | Deliverables | Gate |
|---|---|---|---|
| **1-3** | Productionize and measure | Take your own method or a relevant technique and make it a reproducible service or library with tests, type checks and CI. Go through **code review at least three times** via open-source pull requests. Build the LLM application and pass G1 with baseline-first discipline: every sophisticated step must beat a simple baseline on the eval set. | **G1** |
| **4-6** | Product framing | Choose a business-framed problem and deliver to a real user. Write one-page decision memos (what was measured, what will be done). Cost and latency budget, eval-in-CI, judge calibration, deployment. | **G2** |
| **7-9** | Measurement-rigor artifact and applications | A statistical methodology for LLM evals published as a write-up and small open-source tool: confidence intervals, power analysis for eval-set size, judge-bias tests, drift detection. For the research track, apply to residency or fellowship cycles (see below); check dates for the next cohorts. Mock loops including DSA and system design. 15-20 targeted applications. | **G3** |
| **10-12** | Convert | Loops for applied AI engineer, applied scientist and research-engineer roles. Negotiate level. Plan the next six months if no offer lands. | **G4** |

**Research-track pathways.** The Anthropic Fellows Program describes a roughly four-month full-time fellowship with a stipend and compute, no PhD or prior ML requirement, and over 40% of the first cohort later joining Anthropic full-time `[S32, Grade B; disclosed conflict of interest; self-reported]`. Other labs run comparable programs; one roundup snippet lists an OpenAI safety fellowship `[S32 context, Grade C]`. Treat these as a competitive upside with unknown acceptance rates (not found).

**Realistic state by checkpoint (Tier B) `[M]`.** Month 3: productionized method and reviewed pull requests; offers unlikely. Month 6: applied project with a real user; interviews begin. Month 9: evaluation-rigor artifact published. The modeled median first offer for applied roles is near month 8 (range 5.3-12.5). Month 12: offers plausible for applied roles. **Frontier research roles are not plannable;** treat them as upside.

**Portfolio specialization.** *Rigorous evaluation and method-to-product translation:* a public eval methodology and tool, a reproduction of a method as a service with ablations against simple baselines, and decision memos.

**Evidence summary for D8.** Market structure: Grade A headline, Grade C/D for the derived and secondary numbers. Barriers: Grade D. Roadmap: `[M]`.

---

### D9. Skills diagnostic matrix and three fast tests

**Rubric.** 0 = none. 1 = tutorial-level awareness. 2 = built and shipped something small with feedback. 3 = owns it in production or could teach it.

**Starting levels are the author's hypotheses `[M]`, Grade D.** Individual variation is large. Score yourself honestly, then compare.

| Skill | Target for an AI-engineer role | Backend | Data Scientist | BI Analyst | Frontend/Full-Stack | Non-technical | PhD |
|---|---|---|---|---|---|---|---|
| S1 Production Python/TypeScript (typing, async, packaging, tests) | 3 | 2 (1 if no Python) | 1 | 1 | 2 | 0 | 1-2 |
| S2 LLM API fluency (structured output, tools, streaming, context) | 3 | 1 | 1 | 0-1 | 1 | 0-1 | 1 |
| S3 Retrieval and context engineering | 2-3 | 1 | 1-2 | 0 | 0-1 | 0 | 1 |
| S4 Evaluation design (golden sets, judge calibration, regression tests) | 3 | 0 | 2 | 1 | 0 | 0-1 (rubrics: 2) | 2 |
| S5 Error analysis and data literacy | 2-3 | 0-1 | 3 | 2 | 0 | 1 | 2-3 |
| S6 Agents and tool-use reliability | 2 | 1 | 0-1 | 0 | 0-1 | 0 | 0-1 |
| S7 Production ops (CI/CD, deploy, observability, cost, security) | 2-3 | 3 | 0-1 | 0 | 1-2 | 0 | 0 |
| S8 System design for LLM applications | 2 | 3 classical, 1 LLM | 0-1 | 0 | 1-2 | 0 | 0 |
| S9 Frontend and streaming UX for AI | 1 (3 for frontend targets) | 0-1 | 0 | 0-1 | 3 | 0 | 0 |
| S10 Model and inference literacy | 1-2 | 0 | 1-2 | 0 | 0-1 | 0 | 2-3 |
| S11 Domain judgment and rubric-writing | 2 | varies | 2 | 2-3 | varies | 3 | 3 in own field |
| S12 Product sense and stakeholder communication | 2 | 2 | 1-2 | 2-3 | 2-3 | 3 | 1 |

**Largest gaps by archetype `[M]`**
- *Backend:* S4, S2, S3 (and S1 if coming from Java/Go).
- *Data Scientist:* S1, S7, S8 (the production trio), then S2 and S6.
- *BI Analyst:* S1, S2, S3, S7.
- *Frontend/Full-Stack:* S4, S3, S5 and S7.
- *Non-technical:* S4 (as evaluation fluency), S5, S2 and basic S1.
- *PhD:* S1 and S7 (craft), S8 (loops), S12.

**Three fast tests (about one day each) `[M]`, with shapes drawn from hiring write-ups.**
1. **Q&A over 50 documents.** Given 50 documents and 20 questions with known answers, build a pipeline and report recall@5 and answer faithfulness. *Pass:* a reproducible script, a metrics table and two failure cases explained. Shape from `[S11, Grade D]`.
2. **Explain the request.** Explain what happens between a user pressing Enter and the answer appearing in an LLM app (context assembly, retrieval, tool calls, streaming, cost). *Pass:* failure modes and cost named at each stage. Shape from `[S11, Grade D]`.
3. **Design the eval.** For a task in your own domain, write 30 test cases, a rubric, and a plan to validate an LLM judge. *Pass:* two reviewers score a 20-case pilot and you report their agreement.

---

### D10. Tool catalog: platforms, GPU labs and assessments

Facts below were read this session unless marked. Prices drift; re-check before buying.

| Tool | Role in the plan | Verified facts (Oct 2026) | Best fit | Grade | Ledger |
|---|---|---|---|---|---|
| **Modal** | Serverless GPU for serving and fine-tune labs; small deployed endpoints | Starter plan with USD 30/month free credits. Per-second billing. T4 USD 0.000164/s (about 0.59/h), L4 0.000222/s (about 0.80/h), H100 0.001097/s (about 3.95/h). Startup and academic credit programs (amounts vary by snapshot). | Backend, DS, PhD | A | S21 |
| **RunPod** | Cheap pods for longer GPU experiments | Per-minute billing; a credits program of up to USD 25K on the official page. The official page rendered no numeric prices for me. Trackers (Aug-Sep 2026): RTX 4090 about 0.34/h community vs 0.69/h secure; H100 PCIe about 1.99 vs 2.89/h. | DS, PhD, Backend | A (billing, credits) / C (prices) | S22 |
| **Lambda** (lambda.ai; earlier lambdalabs.com) | On-demand H100/A100 for serving or fine-tune labs | Instances page lists H100 SXM at about USD 3.99-4.29 per GPU-hour and A100 40GB at about 1.99. Other cached snapshots show 2.99-3.29. **Verify live.** | DS, PhD | B/C | S23 |
| **Kaggle Notebooks** | Free GPU notebooks; Google's 5-Day GenAI Intensive codelabs (third-party description) | Session limits 12 h GPU/CPU and 9 h TPU. Weekly GPU quota commonly reported near 30 h but **not in the docs I could see.** 16 GB-class GPUs. | DS, PhD, literacy for non-technical | C | S24 |
| **Hugging Face Learn** | Free structured courses: LLM, Agents, MCP, smol (post-training), cookbook | Official catalog. The Agents Course certificate requires Unit 1, a use-case assignment and a final challenge. | All | A | S25 |
| **DeepLearning.AI short courses** | Free, focused 1-2 hour courses (for example *Evaluating AI Agents*) | Free, per Arize's course listing. Catalog size and prices are listicle-level information (Grade D); no recognized credential. | Backend, Frontend, all | B/C | S26 |
| **Coursera** | Structured specializations and certificates | Listicles cite about USD 49-59/month and free auditing; unverified. My view `[M]`: certificates carry weak hiring signal compared with shipped artifacts. | Non-technical, BI | D | S26 |
| **DataTalks.Club LLM Zoomcamp** | Free cohort-style RAG course with a portfolio project | A listing via Arize describes it as free and 10 weeks. | Backend, DS, BI | C | S27 |
| **Chrome built-in AI docs and demos** | Client-side AI labs | See KF-6. | Frontend | A | S19 |
| **Transformers.js v4** | Browser and Node WebGPU inference | See KF-6. | Frontend | A | S18 |
| **Vercel AI SDK 6** | Streaming and agent UIs | See KF-6. | Frontend | A | S20 |

**Not verified:** exact RunPod list prices from the official page, Kaggle's weekly GPU quota from official docs, DeepLearning.AI catalog counts and Coursera prices.

**GPU lab sequence `[M]`**
- *Lab 0 (everyone):* hosted-model API calls only. No GPU.
- *Lab 1 (Backend, DS, PhD):* serve an open-weight model on Modal or RunPod once. Measure tokens per second, p95 latency and cost per million tokens against an API.
- *Lab 2 (DS, PhD):* a small fine-tune or embedding fine-tune on a free 16 GB notebook GPU, or on a rented 24 GB card for larger models. A 24 GB card costs about USD 35-70 per 100 hours at the tracker prices above.
- *Frontend:* a browser-side lab needs no rented GPU, only a spread of test devices.

---

### D11. Cross-cutting cognitive traps and risks

All Grade D unless noted; they are `[M]` syntheses of the retrospectives and the standard planning literature (recalled).

| Trap | Why it matters here | Mitigation |
|---|---|---|
| **Planning fallacy** | The only detailed retrospective devotes much of its effort to evaluation, retrieval tuning and latency work, which tutorials rarely budget for `[S10]`. All timelines in this file are probably optimistic for people who do not log hours. | Log hours weekly; use the next-longer tier when adherence is below 70%. |
| **Survivorship bias** | Every retrospective and success rate comes from people who made it. No denominator exists (KF-9). | Treat all ranges as conditional on success. Track your own funnel. |
| **The month 4-5 trough** | The retrospective describes months four and five as feeling fraudulent in both directions `[S10, Grade D]`. | Pre-commit to G2 as the checkpoint rather than to a feeling. |
| **Tutorial hell and infinite preparation** | Foundations-first roadmaps dominate search results; building and evaluating is what hiring write-ups ask for. | Ship v0 in two weeks. |
| **Visibility neglect** | The retrospective built in private for five months and says visibility mattered `[S10]`. | Publish at G1. |
| **Title inflation and AI-washing** | "AI engineer" has no standard loop `[S09]`, and posting data can overstate real demand `[S01]`. | Read the job spec; match loop type to preparation. |
| **Burnout at Tier B** | 15-20 h/week is 56-74% of average leisure (KF-10). | Schedule recovery; accept Tier A and a longer horizon. |
| **Single-stack dependence** | AI SDK and WebMCP changed shape within months `[S19, S20]`. | Invest in concepts; freeze stack choices for six weeks. |

---

## Open Questions & Risks

### The strongest objections an expert would raise, and the evidence for and against each

| # | Objection | Evidence for | Evidence against | Verdict and effect on this file |
|---|---|---|---|---|
| 1 | "The hours and timeline numbers are invented." | They are modeled (Grade D). H_core, adherence and search lag are unvalidated judgment calls. No cohort data exists. | Parameters are explicit and changeable. The model was checked against the only available anchors: an 8-month retrospective `[S10]`, Huntr's 82-108 day search medians `[S29]` and a vendor reference class `[S36]`. Gates let you recalibrate H_core by month 3. | **Valid.** The file labels every timeline as a model and reports ranges, not a "median". |
| 2 | "Survivorship bias makes every anchor optimistic." | Every retrospective is from a success. Huntr counts only searches that ended in an offer `[S29]`. No denominators exist (KF-9). | Nothing found. | **Valid.** All durations are conditional on persisting and succeeding. |
| 3 | "Entry-level compression makes the non-technical, BI and junior routes too optimistic." | Stanford: 22-25-year-olds in AI-exposed jobs 19% below trend `[S01]`; PwC: entry-level roles in AI-exposed jobs now ask for senior-type skills `[S05]`. | One secondary summary of a LinkedIn graduate guide calls AI engineer a fast-growing title for young workers (source not retained, Grade D). It concerns title growth, while Stanford concerns employment levels in exposed occupations, so the two do not conflict. Other studies disagree with Stanford `[S01b]`. | **Partly valid.** The recommendation already favors lateral entry and lists the engineering-from-zero route as a 2-year plan. |
| 4 | "These skills will be obsolete within a year: models absorb RAG, frameworks churn." | AI SDK 6 introduced breaking changes `[S20]`; WebMCP changed API surface within months `[S19]`; interviews are changing `[S12]`. | Evaluation, error analysis, observability and cost control persisted across framework changes, and evaluation is the top stack challenge in 2026 `[S02]`. This is one year of survey data, not a long series. | **Valid.** Hence the rule to invest in concepts, not API surfaces. |
| 5 | "Posting data and wage premia overstate demand: ghost jobs, AI-washing, composition effects." | Stanford notes endogenous postings `[S01]`; PwC's premium is correlational `[S05]`; overall tech hiring is soft `[S45, S47b]`. | Several independent sources agree on direction (Axial, LinkedIn, PwC, Lightcast via Fortune), though they share a posting-based method `[S04, S06, S05, S34]`. | **Direction likely right; magnitudes soft.** |
| 6 | "Data scientists are not disadvantaged, and backend is not clearly fastest." | DS are a top-two feeder `[S06, S07]`; Husain argues the eval loop is data science `[S15]`. No speed data by archetype. | Candidate-reported rejections cite coding and system-design rounds `[S40]`. | **Largely accepted.** P2 was refined, P1 marked unproven. |
| 7 | "The frontend 'bypass' claim is speculative and AI-frontend roles are few and senior." | Visible postings are Staff-level with 6+ years `[S38]`; no census. | Platform facts are solid `[S17, S18, S19, S20]`. | **Valid.** Downgraded to "differentiator on top of full-stack competence". |
| 8 | "The PhD problem is market structure, not craft." | Derived industry-bound count is roughly flat while supply rose `[S31, M]`. | Only anecdotal evidence for craft barriers `[S41]`. The two cannot be separated with what I found. | **Open.** Both are listed. |
| 9 | "The author is an Anthropic model and several sources are Anthropic-linked." | The Fellows Program is Anthropic's `[S32]`. The Stanford analysis uses Anthropic Economic Index data, and a commentator criticized that reliance `[S01, S01c]`. One unattributed blog makes a claim about Anthropic's loop `[S11]`. | None of these is sole support for a headline conclusion. The Fellows Program is presented as one of several pathways. | **Disclosed.** Treat Anthropic-linked evidence with extra scrutiny. |
| 10 | "ATUS averages hide individual variation and are US-only." | True. | The averages are used only as a plausibility check on the hours tiers. | **Valid.** Check local conditions. |

### What I searched for and did not find (honest gaps)

1. **Median time to first offer for backend engineers pivoting while employed.** Searched Pragmatic Engineer, MentorCruise and other retrospectives, LinkedIn Economic Graph summaries, Huntr and Ashby benchmarks, and job-board playbooks. Found anecdotes and search-friction proxies only.
2. **Frequencies of rejection reasons for Data Scientists in AI loops.** Searched Reddit, Blind, Glassdoor, Taro and LeetCode reports plus guides. Found anecdotes only.
3. **A census of AI-frontend postings.** Searched job boards and vendor analyses. Found individual postings and one qualitative market commentary.
4. **Longitudinal cohort studies of GenAI career changers.** Searched LinkedIn Economic Graph, OECD.AI, Stanford, Lightcast, DataCamp. Found cross-sectional feeder-role summaries and posting counts, no cohorts.
5. **Non-vendor outcomes of GenAI bootcamps or courses.** Only vendor-reported figures.
6. **Time-to-offer or success rates for AI PM or AI-ops transitions.** Not found.
7. **Acceptance rates for research fellowships and residencies.** Not found.
8. **Degree-versus-portfolio effects for career changers.** Not found.
9. **Kaggle's official weekly GPU quota and RunPod's official price table.** Not retrievable from the official pages I could read.
10. **The durability of expert-contract demand** as LLM judges improve. Only a benchmark-specific agreement figure exists (Mercor's APEX judge panel, 89%), which does not measure demand `[S33]`.

### Conflicts and discrepancies between sources

- **PwC wage premium:** 56% (2025 edition, recalled), 57% (restated in 2026), 62% (2026). DataCamp's 2026 report still cites 56% `[S05, S43]`.
- **Survey size:** 1,053 responses (survey page) versus 1,048 (conference talk) `[S02, S03]`.
- **AI Index industry share for 2022:** 70.7% (2024 report) versus 77% (2026 secondary summary) `[S31]`.
- **Stanford estimate:** about 13% (2025 version, recalled), 16% (March 2026 version, secondary), 19% (August 2026 version). These are not strictly the same estimand `[S01, S01d]`.
- **AI SDK 6 ship date:** January 2026 versus 7 May 2026, depending on the third-party source `[S20]`.
- **Lambda H100 price:** 2.99-3.29 versus 3.99-4.29 per GPU-hour, depending on the snapshot `[S23]`.
- **Chrome built-in AI page:** footer dated 2024 while its table lists Chrome 148 `[S19]`.
- **Modal academic credits:** USD 10k versus 50k, depending on the snapshot `[S21]`.

### Risk register `[M]`

| Risk | Why it matters | Mitigation |
|---|---|---|
| Demand shock or hiring freeze | Overall tech hiring is soft `[S45, S47b]`. One opinion piece argues for an AI-talent bubble (Grade D, not cited as evidence). | Artifacts (evals, observability, reliability, domain rubrics) are valuable in your current role. Internal-first limits exposure. |
| AI-mediated screening | LinkedIn reports 66% of recruiters plan to increase AI pre-screening in 2026 `[S47a]`. | Targeted applications with role-specific artifacts rather than mass applying. |
| Interview inflation and loop churn | No standard AI-engineer loop `[S09]`. | Match preparation to loop type (D1); refresh mock loops quarterly. |
| Platform churn | `[S19, S20]` | Concepts over API surfaces; freeze stack choices six weeks at a time. |
| Burnout at Tier B | 56-74% of average leisure (KF-10). | Choose Tier A and a longer horizon when needed. |
| Contract risk (expert gigs) | At-will, project-based and credential-gated `[S33]`; check any IP and confidentiality terms yourself before accepting work. | Use as a bridge; do not rely on it as a primary income plan; never use an employer's or client's confidential data in portfolio artifacts. |
| Regional mismatch | Most data is US-centric. | Verify with local postings before committing. |

### Open research questions

1. What share of people who start each path reach an offer, and by when? (Needs cohort data.)
2. Does an evaluation-first portfolio outperform generic RAG-chatbot portfolios in screening? No controlled evidence exists.
3. Is AI-frontend a durable niche or a transitional layer that generative-UI frameworks will commoditize?
4. How durable is human domain-expert demand as AI graders improve?
5. Do certificates carry any signal for the non-technical lane? No evidence found either way.
6. How do the patterns differ outside the US?

### What would change this recommendation

- A cohort study showing different speeds by archetype would rewrite R2.
- Evidence that credentials outperform artifacts for career changers would revise the gates.
- A material change in screening (agent-conducted interviews, for example) would revise D1.
- A collapse in posting volumes would extend every horizon.

---

## Delta

How my beliefs changed. "Pre-search" entries are recalled (Grade D by rule).

| Pre-search belief | What the evidence showed | Direction | Updated belief and grade |
|---|---|---|---|
| **P1.** Backend engineers pivot fastest; median first offer 6-9 months while employed. | No head-to-head data. Software Engineer is the top feeder into AI-engineer titles, and Full Stack Engineer appears in both LinkedIn lists `[S06, S07]`. Experienced software engineers dominate the survey `[S02]`. Anecdotes run 4-9 months `[S10, S37]`. Evaluation, not systems skill, is the cited bottleneck `[S02, S08]`. | **Untested; plausibly supported** | Experienced software engineers of any stack are the dominant feeder. Speed ranking unproven. 6-9 months is plausible at the Tier A/B boundary. Grade B (population) / D (speed). |
| **P2.** The main DS disqualifier is production software engineering. | DS are a top-two feeder `[S06, S07]`. Husain/Arize argue the eval loop is DS work `[S15]`. Rejection anecdotes cite coding and system design in big-company loops `[S40]`. No frequency data. | **Refined (partly contradicted)** | The gap is real in big-company loops; DS hold a comparative advantage in evals. Grade C / D. |
| **P3.** Non-technical people need domain specialization, not coding competition. | AI consultants need about 8.2 years `[S06]`. FDE needs code `[S34]`. Domain experts should label evals `[S15]`. Expert marketplaces are credential-gated, at-will contract work with LLM judges increasingly in the loop `[S33]`. Non-developers do build internal tools, but 59% of surveyed respondents worry about AI-code liabilities `[S02]`. | **Confirmed, with an entry fee and a lower coding barrier than assumed** | Domain evaluation, AI ops and AI PM are the leverage points; verification is the bottleneck. Grade C. |
| **P4.** 6-12 months for experienced engineers, 12-24 for others. | Anecdotes of 4-9 months `[S10, S37]`. Modeled 6-10 months for backend and 7-13 for DS, frontend and PhD at Tiers B and A. About 22 months for engineering from zero code at Tier B. Search lag 82-108 days `[S29]`. | **Partly confirmed; refined into hours tiers** | Ranges depend on the hours tier and are conditional on success. Grade D. |
| **P5.** PhD barrier is craft; lab slots scarce. | New AI PhDs +22% with the growth going to academia `[S31]`. Derived industry-bound count roughly flat `[M]`. Craft barriers anecdotal `[S41]`. Fellowships state no PhD is required `[S32]`. | **Partly confirmed; strengthened on market structure** | Plan for applied roles; treat lab research roles as upside. Grade B (headline) / C-D (rest). |
| AI-skill wage premium about 56%. | PwC 2026: 62%, up from 57% `[S05]`. | **Updated** | Grade B. |
| WebGPU is not in Safari. | Safari 26 ships WebGPU; Khronos (Jul 2026) says all major browsers `[S17]`. | **Contradicted** | Grade A. |
| Transformers.js v3 is current. | v4 released 9 Feb 2026, with 4.1 and 4.2 `[S18]`. | **Updated** | Grade A. |
| Chrome's Prompt API is extension-only. | Listed for web at Chrome 148 `[S19]`. | **Updated** | Grade A. |
| Vercel AI SDK 5 is current. | AI SDK 6 exists with agents and tool approval `[S20]`. | **Updated** | Grade A. |
| Kaggle gives a documented 30 GPU hours per week. | Not in the docs I could read; commonly reported `[S24]`. | **Downgraded** | Grade C. |
| Lambda Labs prices are known. | Lambda (lambda.ai); snapshots conflict `[S23]`. | **Updated** | Grade B/C. |
| Entry-level squeeze is about 13%. | 16% (March 2026 version, secondary) and 19% (August 2026 version) `[S01, S01d]`. Contested `[S01b]`. | **Updated (not strictly comparable)** | Grade A (facts) / contested interpretation. |
| Foundations-first sequencing is required. | One detailed retrospective dropped it `[S10]`. Roadmaps are math-first; no controlled evidence. | **Untested** | Grade D. |
| AI engineer is the fastest-growing role. | LinkedIn ranks it first `[S06]`. | **Confirmed** | Grade C. |
| Time to offer depends mainly on skill. | Search friction of 82-108 days, applicants per role doubled, hiring 23% below pre-pandemic `[S29, S47a, S47b]`; hours constraint `[S28]`. | **Updated** | Hours and search friction matter as much as skill. Grade C / A. |

---

## Sources & Evidence Ledger

Access marks: **fetched** = opened in full; **extract** = substantive canonical text returned inside search results; **snippet** = short excerpt or secondary description only. IDs are stable across drafts; gaps (S44, S46, S48, S49, S52) are sources considered and dropped as redundant or unverifiable. URLs are as returned by search; where I could not retain a permalink, the entry says so. A final verification pass re-surfaced and re-read the entries for S01, S05, S12, S15, S16, S30, S33, S35, S38, S39, S41, S47a, S47b, S50, S51 and S53; other entries were retrieved earlier in the session and not re-opened in that pass.

| ID | Source (title, publisher, date) | URL | Access | Grade | Used for and caveats |
|---|---|---|---|---|---|
| S01 | Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence", Stanford Digital Economy Lab, revised 12 Aug 2026 | https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ ; PDF: https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf | fetched | A | KF-1, KF-2. Descriptive, not causal. ADP payroll data. Uses Anthropic Economic Index data (disclosed). |
| S01b | Stanford DEL, "AI Economic Indicators: June 2026 Update" | https://digitaleconomy.stanford.edu/app/uploads/2026/06/AIEI_RN01_Jun26.pdf | snippet | C | Notes that other studies disagree (Yale Budget Lab). Snippet truncated. |
| S01c | Casilli, "Young Workers Haven't Been Replaced by AI..." (commentary on the 2025 version), 29 Aug 2025 | https://www.casilli.fr/2025/08/29/young-workers-havent-been-replaced-by-ai-economists-are-just-looking-for-them-in-the-wrong-places/ | extract | D | Critique of reliance on Anthropic Economic Index data. Opinion. |
| S01d | The Futurist, summary of the March 2026 Canaries paper (16% relative decline), 10 Mar 2026 | https://futurist.com/2026/03/10/the-ceos-guide-to-ai-young-workers-as-the-canaries-in-the-coalmine/ | extract | C | Intermediate estimate in the Delta only. |
| S02 | Notion x Amplify Partners x Vercel, "2026 AI Engineering Survey" (1,053 responses, 16 May-15 Jun 2026) | https://www.notion.com/lp/ai-engineering-survey | fetched | B | KF-3, KF-4, KF-12. Convenience sample; sponsor-run. |
| S03 | Barr Yaron, "The 2026 State of AI Engineering", AI Engineer World's Fair, 2 Jul 2026 | https://www.ai.engineer/talks/RGe6EjucbzI-2026-state-ai-engineering ; https://ai.engineer/talks/the-2026-state-of-ai-engineering-barr-yaron-amplify-partners | snippet | C | Median 8 years coding / 3 years AI; n=1,048. |
| S04 | Axial Search, "Inside the AI Engineering Job Market: 43,500 Postings Analyzed", updated 13 Oct 2026 | https://axialsearch.com/insights/ai-ml-engineering-jobs/ | fetched | C | KF-1. Recruiter vendor; posting-based. |
| S05 | PwC, "2026 Global AI Jobs Barometer" press release, 15 Jun 2026 | https://pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html | extract | B | KF-1, KF-2. Interested primary; correlational. |
| S06 | LinkedIn "Jobs on the Rise 2026" (data Jan 2023-Jul 2025), via NewsNation, Allwork.Space and VnExpress | https://digital-release.wgnradio.com/?p=2781179 ; https://allwork.space/2026/01/linkedin-reveals-25-fastest-growing-jobs-for-2026 ; https://e.vnexpress.net/news/tech/tech-news/ai-roles-dominate-fastest-growing-jobs-in-us-5004966.html | extract | C | KF-1, KF-3, KF-7. Secondary reporting of LinkedIn's list. |
| S07 | SuperDataScience #856, "The Fastest-Growing Jobs Are AI Jobs" (LinkedIn 2025 list), Jan 2025 | https://superdatascience.com/podcast/856 | fetched | C | KF-3. Older edition. |
| S08 | Pragmatic Engineer, "AI Engineering in the real world", 25 Mar 2025 | https://newsletter.pragmaticengineer.com/p/ai-engineering-in-the-real-world | fetched (partial paywall) | B | KF-4, D4. Named practitioners; self-reports. |
| S09 | Pragmatic Engineer, "From Software Engineer to AI Engineer, with Janvi Kalra" | https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer | snippet | C | D1, KF-9. Single practitioner. |
| S10 | MentorCruise, "How I went from React developer to AI engineer in 8 months", 3 Aug 2026 | https://mentorcruise.com/blog/how-i-went-from-react-developer-to-ai-engineer-in-8-months-8b9e1/ | fetched | D | Timeline anchor. Single case; commercial context; also completed a thesis. |
| S11 | techinterview.org, "What applied-AI engineer interviews test in 2026", 23 Jul 2026 | https://www.techinterview.org/post/3233476824/ai-engineer-interview-rag-agents-evals/ | fetched | D | Loop content. Unattributed; makes an unverified claim about Anthropic's loop. |
| S12 | tianpan.co, "Hiring for LLM Engineering: What the Interview Actually Needs to Test" (16 Apr 2026) and related interview posts | https://tianpan.co/blog/2026/04/16/hiring-llm-engineers-interview-what-to-test ; https://tianpan.co/blog/tags/interviews | extract (first URL) / snippet (tag page) | D | KF-4, D4. Hiring-side opinion: failure-mode intuition from shipped systems; classical ML skills transferable but not equivalent. |
| S13 | Alpesh Nakrani, "AI engineer red flags" | https://alpeshnakrani.com/blog/ai-engineer-red-flags/ | snippet | D | Hiring-side opinion. |
| S14 | Eugene Yan & Jason Liu, "How to Interview and Hire ML/AI Engineers" | https://eugeneyan.com/writing/how-to-interview/ | snippet | C | Named practitioners. |
| S15 | Hamel Husain, "The Revenge of the Data Scientist" (blog post and PyAI 2026 slides); Arize recap of his Arize Observe 2026 talk; Vanishing Gradients episode | https://hamel.dev/blog/posts/revenge/ ; https://hamel.dev/blog/posts/revenge/images/The_Revenge_of_the_Data_Scientist.pdf ; https://arize.com/?p=29757 (permalink; title not shown in the extract) ; https://vanishinggradients.fireside.fm/60 | extract | C | KF-5, D5, D7. Named-practitioner argument, not an empirical test. Arize sells observability and evals tooling. |
| S16 | Simon Willison, link post on Hamel Husain's "Your AI Product Needs Evals", 31 Mar 2024 | https://simonwillison.net/2024/Mar/31/your-ai-product-needs-evals | extract | C | D4: the pass rate is a product decision, not a 100% target. |
| S17 | web.dev, "WebGPU is now supported in major browsers"; Khronos SIGGRAPH 2026 WebGPU slides (22 Jul 2026) | https://web.dev/blog/webgpu-supported-major-browsers ; https://www.khronos.org/developers/linkto/webgl-and-webgpu-sigg26 | extract | A | KF-6, D6. |
| S18 | Hugging Face, "Transformers.js v4: Now Available on NPM!", 9 Feb 2026; GitHub releases | https://huggingface.co/blog/transformersjs-v4 ; https://github.com/huggingface/transformers.js/releases | extract | A | KF-6, D6. |
| S19 | Chrome for Developers, "Built-in AI APIs" and "WebMCP imperative API" (18 May 2026); HackerNoon and Similarweb explainers on WebMCP | https://developer.chrome.com/docs/ai/built-in-apis ; https://developer.chrome.com/docs/ai/webmcp/imperative-api ; https://hackernoon.com/what-exactly-is-webmcp ; https://aisearch.similarweb.com/blog/webmcp/ | fetched (built-in APIs) / extract | A (Chrome docs) / C (third-party) | KF-6, D6. Footer date inconsistency noted. |
| S20 | Vercel, "AI SDK 6"; DEV Community migration guide | https://vercel.com/blog/ai-sdk-6 ; https://dev.to/rabinarayanpatra/how-to-migrate-vercel-ai-sdk-5-to-6-breaking-changes-guide-mcf | extract | A (features) / C (date) | KF-6, D6. Ship date disputed. |
| S21 | Modal, pricing | https://modal.com/pricing | extract | A | KF-12, D10. Credit amounts vary across snapshots. |
| S22 | RunPod, GPU instance pricing; price trackers (Spheron; Tech Insider) | https://www.runpod.io/gpu-instance/pricing ; https://www.spheron.network/blog/gpu-cloud-pricing-comparison-runpod-vs-vastai-2026/ ; https://tech-insider.org/runpod-vs-lambda-vs-vast-ai-2026/ | extract | A (billing, credits) / C (prices) | KF-12, D10. Official page showed no numeric prices. |
| S23 | Lambda, instances and pricing pages | https://lambda.ai/instances ; https://lambda.ai/pricing | extract | B/C | KF-12, D10. Snapshots conflict. |
| S24 | gpuperhour.com, free cloud GPUs and credits (read 21 Sep 2026); AIMultiple free cloud GPU roundup | https://gpuperhour.com/blog/free-cloud-gpus-and-credits ; https://aimultiple.com/free-cloud-gpu | extract | C | KF-12, D10. Weekly quota not in docs I could read. |
| S25 | Hugging Face Learn; Agents Course intro | https://huggingface.co/learn ; https://huggingface.co/learn/agents-course/en/unit0/introduction | extract | A | KF-12, D10. |
| S26 | DeepLearning.AI short courses (for example *Evaluating AI Agents*), as listed in an Arize course roundup (permalink not retained); aggregator listing | https://www.deeplearning.ai/short-courses/evaluating-ai-agents/ ; https://aiagentrank.io/learn/provider/deeplearning-ai | snippet | B/C (course existence) / D (catalog counts, Coursera prices) | KF-12, D10. |
| S27 | DataTalks.Club LLM Zoomcamp, as listed in an Arize course roundup (permalink not retained) | n/a | snippet | C | D10. |
| S28 | BLS, "American Time Use Survey: 2025 Results", 25 Jun 2026 | https://www.bls.gov/news.release/atus.nr0.htm ; https://www.bls.gov/news.release/archives/atus_06252026.htm | extract | A | KF-10, D2. US averages; suspension during the 2025 shutdown. |
| S29 | Huntr, "Job Search Trends Report Q2 2026" | https://huntr.co/research/job-search-trends-q2-2026 | extract | C | KF-11, D2. Searches with offers only. |
| S30 | Ashby 2026 Talent Trends via Leon Staff, Metaview and Pin summaries; Ashby-derived time-to-fill via TheHireHub | https://leonstaff.com/blogs/ashby-response-time/ ; https://content.metaview.ai/time-to-hire-by-role/ ; https://www.pin.com/blog/time-to-reply-interview-benchmarks ; https://www.thehirehub.ai/blog/time-to-hire-benchmarks | extract | C | KF-11. Secondary. Time-to-hire (about 40 days, technical) and time-to-fill (about 75 days) measure different things. Only the Leon Staff and TheHireHub pages were re-read in the final pass. |
| S31 | Stanford HAI, "AI Index Report 2026" (and 2024 education chapter); secondary summary | https://hai.stanford.edu/ai-index/2026-ai-index-report ; https://hai.stanford.edu/ai-index/2024-ai-index-report/education ; https://wallyboston.com/ai-in-academia/ | extract | A (headline) / C (secondary shares) | KF-8, D8. Series revisions noted. |
| S32 | Anthropic Alignment Science blog, "Anthropic Fellows Program 2026"; Techloy fellowships roundup | https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/ ; https://techloy.com/5-ai-fellowships-currently-open-for-applications-in-2026/ | extract / snippet | B (conflict of interest) / C | KF-8, D8. Self-reported by the program owner. |
| S33 | Expert-contract marketplaces: TechCrunch figures via a 2026 HeroHunt guide; Bloomberg (16 Oct 2026) via FourWeekMBA; CryptoBriefing; Mercor newsroom and listings; implicator.ai on the APEX benchmark | https://www.herohunt.ai/blog/mercor-2026-how-it-works-pay-alternatives/ ; https://fourweekmba.com/ai-doctors-and-lawyers-now-train-ai-for-up-to-400-an-hour/ ; https://cryptobriefing.com/gig-workers-advanced-degrees-ai-training-rates/ ; https://www.mercor.com/newsroom/ ; https://career.io/job/news-reporter-mercor-e9c349c81fd7ec5012da40ae09465592 ; https://work.mercor.com/jobs/list_AAABlRvLjyMZ_QjpNyhB6r5E/expert-model-trainer ; https://www.implicator.ai/mercors-apex-says-gpt-5-scores-64-on-real-work-still-not-production-ready/ | extract | C / D | KF-7, D7, Alternatives. Pay figures are secondary relays or company claims (Bloomberg's rates come from recruiter postings, not payroll). The 89% figure is specific to the APEX benchmark's judge panel. |
| S34 | Fortune, forward-deployed engineers (Lightcast data), 3 Sep 2026; Fast Company (FT 800% figure) | https://www.fortune.com/2026/09/03/forward-deployed-engineers-fast-growing-six-figure-silicon-valley-job-integrate-ai-with-customers-tech-careers-palantir/ ; https://www.fastcompany.com/91435680/postings-for-this-ai-job-are-up-800 | extract | B / C | KF-7. Large growth from a small base. |
| S35 | KORE1, "How to hire an AI product manager: 2026" and its AI PM job-description template; Product School commentary | https://www.kore1.com/how-to-hire-ai-product-manager-2026/ ; https://www.kore1.com/ai-product-manager-job-description-template/ ; https://productschool.com/blog/job-search/ai-product-management-careers | extract | D | KF-7, D7. Staffing-vendor content that discloses it is paid on placements. |
| S36 | TripleTen, "How long does a bootcamp take?" | https://tripleten.com/blog/posts/how-long-does-a-bootcamp-take | extract | D | KF-9, D2. Vendor reference class (zero experience). |
| S37 | JobsByCulture, "How to Transition Into AI Roles in 2026" | https://jobsbyculture.com/blog/how-to-transition-into-ai-roles-2026 | fetched | D | KF-9. Job-board playbook; unattributed ranges. |
| S38 | AI-frontend postings and commentary: Productboard Staff roles (Index Ventures; Built In); recruiter-listed Staff AI Frontend Engineer (Torre; Klarity listing); Artisan Staff Frontend Engineer (Y Combinator); JobStreet "Frontend Engineer (AI)"; GreatFrontEnd (27 Aug 2026) | https://www.indexventures.com/startup-jobs/productboard/staff-fullstack-product-engineer-frontend-heavy-praguebrnoremote-eu/ ; https://builtindublin.ie/job/staff-frontend-product-engineer-prague-brno-remote-eu/10828180 ; https://torre.ai/post/2wzYn5bW-yuvrolabs-seniorstaff-ai-frontend-engineer ; https://careers-page.com/transparent-search-group/job/8X9X4Y43 ; https://www.ycombinator.com/companies/artisan/jobs/ie5GSkZ-staff-frontend-engineer ; https://sg.jobstreet.com/job/94863897 ; https://www.greatfrontend.com/blog/frontend-developer-demand-a-job-market-reality-check | extract (postings) / snippet (JobStreet, GreatFrontEnd) | C / D | KF-6, D6. Individual postings. The JobStreet and GreatFrontEnd pages were not re-read in the final pass. |
| S39 | Data-scientist-to-ML-engineer guides: MentorCruise DS-to-MLE guide and its companion ML-engineer career-change guide; DataTalks.Club wiki | https://mentorcruise.com/blog/career-change-guide-how-to-transition-from-a-data-scientist-into-a-machine-learn/ ; https://mentorcruise.com/blog/career-change-guide-how-to-become-a-machine-learning-engineer-in-2026/ ; https://datatalks.club/podwiki/wiki/data-scientist-to-machine-learning-engineer/ | extract | D (MentorCruise, a mentoring marketplace) / C (DataTalks.Club) | KF-5, KF-9, D2, D5. MentorCruise: 6-18 months for a working data scientist with Python; 12-24 months for career changers into ML engineering. Targets ML engineering, not GenAI specifically. |
| S40 | Candidate-reported rejections: Glassdoor (Meta MLE), Blind, Taro, Taro (IBM India) | https://www.glassdoor.com.au/Interview/Meta-Interview-E40772-RVW30022540.htm ; https://www.teamblind.com/post/facebook-interview-experience-zmynvitf ; https://www.jointaro.com/question/Q2ivEz5ix5KtJyYmfSlU/i-keep-failing-my-mldata-science-interviews-and-i-dont-know-why/ ; https://www.jointaro.com/interviews/companies/ibm/work-experiences/ai-engineer-bengaluru-november-28-2025-5-e60d96a2 | extract | D | KF-5, D5. Anecdotal. |
| S41 | PhD-to-industry accounts: Arize, "From Physicist to Machine Learning Engineer"; DataTalks.Club, "From Research to Production" (Mihail Eric); techinterview.org, "PhD to Industry: Engineering and Research Roles" (updated 5 May 2026) | https://arize.com/blog/from-physicist-to-machine-learning-engineer/ ; https://datatalks.club/podcast/research-to-production-ml-systems-roadmap.html ; https://www.techinterview.org/post/3233475124/phd-to-industry-engineering-research/ | extract | D | KF-8, D8. Individual accounts; techinterview.org is unattributed. |
| S42 | Gauntlet AI fellowship (Crossover listing) | https://www.crossover.com/jobs/software-engineer/t-a0sfv000003W398AAC/gauntlet-ai-llm-engineer | snippet | C/D | Alternatives. Promotional; outcome claims unverified. |
| S43 | DataCamp, "State of AI Careers 2026" | https://www.datacamp.com/pt/resources/whitepapers/state-of-ai-careers-2026 | snippet | C | Delta: still cites the 56% premium. Vendor. |
| S45 | CIO Dive, Indeed Hiring Lab report on tech postings (2025) | https://www.ciodive.com/news/indeed-AI-jobs-report/806111/ | snippet | B/C | KF-1. 2025 vintage. |
| S47a | LinkedIn, "LinkedIn Research Talent 2026" | https://news.linkedin.com/2026/LinkedIn-Research-Talent-2026 | extract | A | KF-11, risk register: applicants per role doubled since spring 2022; 66% of recruiters plan more AI pre-screening. |
| S47b | LinkedIn Economic Graph, "LinkedIn Workforce Report, United States, March 2026" | https://economicgraph.linkedin.com/resources/linkedin-workforce-report-march-2026 | extract | A | KF-1, KF-11: US hiring 23% below Feb 2020; tech, information and media 26% below. |
| S50 | "Leaving Big Tech: How I Broke Into AI (Part 2)", Level Up Coding | https://levelup.gitconnected.com/leaving-big-tech-how-i-broke-into-ai-part-2-3eac4003c891 | extract | D | KF-9. Planned about 18 months; was rejected by several internal teams before landing on an Ads GenAI team. |
| S51 | Ryan, "Why I switched teams", Developing Dev newsletter | https://www.developing.dev/p/why-i-switched-teams | extract | D | KF-9. An Instagram infrastructure engineer's internal transfer to AI/ML training infrastructure: no interview prep, reused context, kept existing stock. |
| S53 | The Product Compass newsletter, "Mastering AI Evals: A Complete Guide for PMs" (guest post by Hamel Husain) | https://www.productcompass.pm/p/ai-evals | extract | D | D7. Describes evals as emerging as the top skill for AI PMs. Newsletter with a course tie-in. |

---
*End of file.*
