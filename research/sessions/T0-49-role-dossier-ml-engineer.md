---
id: "T0-49"
title: "Role Dossier: Machine Learning Engineer"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-ml-engineer"
tags: ["machine-learning-engineer", "role-dossier", "job-postings", "pay", "india", "skills"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai with web search and fetch. COI: one sampled posting (Anthropic) is the developer's own; it is marked COI."
evidence_window: "2025-12-02 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-49: Role Dossier: Machine Learning Engineer

S-numbers (S1, S2 …) refer to rows in the Sources & Evidence Ledger. Grades: A is a primary page I opened; B is an established secondary source, or a primary page seen only as a search extract; C is a mirror, a third-party analysis or a single practitioner; D is recall or judgement; M is my own calculation from the sampled records; P is practice-curated. I made all retrievals on 2026-11-13. The brief's anchor date is 2026-11-11, so I counted the 90-day window from that date (2026-08-13). KB claims appear only as K-numbers; the KB-session references inside them were not opened. Skill shares are computed only from the text captured in each `jd` record, so they are reproducible from the Data Appendix and are lower bounds.

## Prior

| # | Proposition (before searching) | Confidence | Grade |
|---|---|---|---|
| P1 | LLMs or GenAI feature in roughly 40–50% of MLE postings; the rest is classic ML (ranking, ads, vision). | medium | D |
| P2 | Levels.fyi US MLE median total compensation is about $270–290K. | medium | D |
| P3 | AWS ML Specialty is retired and MLA-C01 is the in-force AWS ML-engineer associate exam. | medium | D |
| P4 | A degree is stated in a majority of MLE postings. | low | D |
| P5 | Fine-tuning is named in fewer than 20% of MLE postings. | medium | D |
| P6 | Levels.fyi Bengaluru MLE pay (median near ₹44L) is well above broad-market samples. | low | D |

## Research Question

**Decision question.** What should the knowledge base say about the Machine Learning Engineer role: what the job is, how much demand and pay it carries, the skills, proof and credentials it needs, how candidates are interviewed and presented, how careers progress, and where the jobs are? I read "MLE" as the title as posted, then classified each posting by what it asks for. I kept LLM-centred and classic-ML work both in scope and report the split, because the KB restricts demand to GenAI work.

**Sub-questions.** The 15 coverage items in the brief, plus three probes: the LLM or GenAI share of MLE postings; classic ML system design against LLM work in interviews; and the pay premium of the title over AI Engineer.

**Method.**
- More than 40 searches and about 15 page fetches.
- Postings were found through employer- and ATS-targeted queries (Greenhouse, Lever, Workable, Ashby and employer career sites).
- Four employer pages were read in full (A). Twenty-three more were seen as employer-page extracts (B). Nine were reachable only as job-board mirrors (C).
- Platform counts came from JobsPipe and Fast AI Jobs. Pay and sponsorship data came from Levels.fyi and LCA aggregators.
- Certification, interview and durability sources are listed in the ledger.

**Falsification searches.**
- MLA-C01 currency: contradicted (item 8).
- India median cross-check: broad samples give about half the KB's Levels.fyi figure (item 5).
- Degree share: 39% in the sample, not a majority (item 9).
- Scope of the "70%" statistic: it covers 20 interviewed agent deployments (item 10).
- Big Tech boards: I looked for Apple, Meta, Google, Amazon and Microsoft pages and reached none; Netflix, Roblox, Waymo, Pinterest and TikTok were reached.

**What the sample biases.** The sample (n = 36) is search-engine-led, not random. It over-represents US (25), English-language, AI-native and Greenhouse-hosted employers, and under-represents Big Tech, consultancies and IT services (Europe 4, India 6, Latin America 1). OpenAI's employer pages block bots, so those records rest on extracts. Requirement text is full for 4 postings and partial for 32, so skill shares are lower bounds with about ±16 percentage points of sampling error at n = 36.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Volume is large: 2,157 live MLE postings globally, 1,084 in the US, 108 in the UK, 90 in India and 60 in Canada, as of 2026-11-13. Fast AI Jobs lists 298 roles at 171 AI startups, as of 2026-11-11. | [S1][S5] | B |
| KF2 | Platform counts are noisy. 12 of 50 Fast AI rows (24%) carry non-MLE titles (CV, perception, MLOps, solutions architect, manager) and 5 (10%) are internships. JobsPipe also lists staffing and recruiter posters. | [S5][S1] | M |
| KF3 | About half of MLE postings involve LLMs or GenAI: JobsPipe names LLM in 45.0% (counted 2026-09-10); my sample shows 47% (17/36, ±16 points). The split is 59% (13/22) at labs and AI-native firms against 29% (4/14) elsewhere. 53% (19/36) have no GenAI element. | [S2][S41] | B/M |
| KF4 | Python and PyTorch are the core (platform 71.3% and 48.2%; sample 33% and 28%). Evals (31%) and production ownership (28%) are the most common non-framework skills in the sample. Fine-tuning is 17%, RL or post-training 11%, serving 14%, C++ 6%. The platform's C++ share (23.3%) is inflated by AV, robotics and vision employers. | [S2][S41] | B/M |
| KF5 | US pay: Levels.fyi median TC $285,650 (P25 $200K, P75 $387K, P90 $498K; updated 2026-11-12). Posted-pay median is $224K (P25–P75 $183–268K, n = 582). The LCA median offered wage for the exact title is $172,900 (53 filings). | [S7][S3][S35] | B |
| KF6 | On one platform and method, the MLE posted-pay median is $224K against $181K for AI Engineer (+$43K, +24%). Employer mix confounds this; within-employer pairs were not measured. | [S3][S4] | M |
| KF7 | India: broad Bengaluru samples give a median near ₹19.9L (n = 422, IQR ₹9.2–35.6L). The KB's Levels.fyi ₹44.5L could not be verified. JobsPipe's India demand is internally inconsistent (90 live roles is 4.2% of 2,157, against 7.7% on its JD page). | [S10][S1][S2] | B/C |
| KF8 | Seniority: 17 sampled postings state years, with a median of 5 (range 2–10). Only 2 of 36 are entry or junior (a TikTok new-graduate PhD programme and a PhysicsX junior role). JobsPipe labels 13.7% entry and 23.2% senior (labelled share only). | [S41][S2] | M/B |
| KF9 | A degree is stated in 39% (14/36) of captured text, and 8 of those 14 accept equivalent experience. Labs and AI-native firms state one less often (5/22) than other employers (9/14). The KB's 72% for AI-engineering postings was not reproduced. | [S41] | M |
| KF10 | Credentials: 0 of 36 postings name any certification. AWS ML Specialty retired on 2026-03-31. AWS MLA-C01 took its last English exam on 2026-09-28, replaced by MLA-C02 (beta). PMLE costs $200 and NCP-GENL costs $200. | [S13][S14][S16][S18] | B |
| KF11 | No employer-published MLE loop was found. Employers do publish AI-use rules (Glean's AI exercise, Anthropic's AI guidance). Reports describe 4–6 rounds including ML system design on recommendation and ranking. | [S21][S20][S37] | A/C |
| KF12 | Employer-stated proof: a public open-source track record (Hugging Face), shipped production ownership (Glean; Scale AI via mirror), error analysis and regression tests (voize), and evidence for choosing training over prompt or tool changes (PhysicsX). A named practitioner who hires AI engineers asks for a baseline, a ground-truth set and compared approaches. | [S22][S21][S25][S33][S30][S45] | A/B/C |
| KF13 | Durability: 70% of 20 interviewed agent deployments used off-the-shelf models without weight tuning, which is narrower than "70% of production apps". Fine-tuning or RL still appears in 22% (8/36) of sampled postings, mostly at labs and AI-native firms. | [S34][S41] | B/M |
| KF14 | Geography (JobsPipe, counted 2026-09-10): US 50.3%, India 7.7%, UK 6.8%, Singapore 5.9%, Canada 3.6%, Germany 3.1%. LCA filings for the exact title: 53 in FY2026 to date (CA 25, WA 10, NY 7). | [S2][S35] | B |
| KF15 | The sample's gaps are Big Tech boards (Meta, Google, Amazon, Microsoft, Apple), consultancies beyond McKinsey, entry-level postings and Europe (n = 4). Findings that rest on the sample are directional. | [S41] | M |

## Recommendation

1. **Choose the flavour before applying.**
   - Close to half of postings are LLM-systems work (evals, post-training, serving, agents). The rest is classic ML (ranking, ads, risk, safety, simulation).
   - Target LLM-systems roles at labs and AI-native firms. Target ranking and large-scale ML at Big Tech and enterprises.
   - Failure mode: a generic profile matches neither keyword set.
   - Would change if: a measured Big Tech sample shows a different GenAI share.
2. **Build the core.**
   - Python plus PyTorch plus production ML, then one differentiator: evals, serving or post-training.
   - Failure mode: a long framework list with no evidence of shipped work.
   - Would change if: platform shares for evals or serving rise above 40%.
3. **Show proof.**
   - Use public merged pull requests, a system you owned after launch, error analysis with regression tests, and a measured choice between prompting, RAG and fine-tuning.
   - Do not present fine-tuning as the default answer, and do not list tools you have only read about.
   - Failure mode: proof tied to one employer's wording; most evidence here is posting language and one practitioner, not hiring-manager interviews.
4. **Entry.**
   - Expect a median ask of 5 years of experience. Entry roles are mostly new-grad, PhD or internship programmes.
   - Realistic routes are backend or data-science transitions and the PhD route to lab roles; the non-technical route is weak.
   - Failure mode: no 2025+ transition analysis was found, so route timings are unmeasured.
5. **Credentials.**
   - Skip the AWS ML Specialty (retired). If you work on AWS, use MLA-C02 once it is generally available.
   - Take PMLE only for GCP shops, and NCP-GENL only for inference-infrastructure roles.
   - Failure mode: IT-services and GCC employers (largely unsampled) may filter on certificates.
6. **Pay anchors.**
   - US: $224K posted base (platform median) and $285,650 Levels.fyi TC (self-reported, skewed high).
   - India: about ₹20L broad median, with product, GCC and lab roles far higher.
   - Failure mode: using Levels.fyi medians as a market average, especially in India.
7. **Sponsorship (US).**
   - Check each posting. Anthropic and Capital One state that sponsorship is possible.
   - Failure mode: exact-title LCA counts understate sponsorship because titles vary.
8. **Interview prep.**
   - Prepare coding, ML fundamentals, ML system design (ranking and recommendation), and an LLM-systems design question.
   - Expect AI-tool discussion or exercises at AI-forward employers.
   - Failure mode: loop evidence is grade C, from prep vendors and candidate reports.

## Alternatives Considered

| Option | Verdict | Why |
|---|---|---|
| Use platform shares only | Rejected as sole source | They carry no requirement-level detail and extraction is lexicon-based; I used them as the cross-check. |
| Treat classic-ML MLE as out of scope for the GenAI KB | Rejected | 53–55% of postings have no LLM element; keep one role with two tracks. |
| Split MLE into two roles in the KB | Not preferred | Titles and pay bands overlap; tags are cheaper and sturdier. |
| Headline pay from Levels.fyi TC | Used with care | Self-reported and skewed to big employers; shown beside posted base. |
| Count certifications as Must or Important | Rejected | 0 of 36 postings name one. |
| Wait for Big Tech board access before publishing | Rejected | Bot walls persist; publish with the gap flagged. |

## Detailed Findings

### 1. Definition, variants and aliases

- As of 2026-11-13 the MLE builds, evaluates, adapts and serves models. The sample shows three families:
  - **LLM-systems MLE:** Anthropic RL environments, Glean assistant quality, OpenAI API Multicloud.
  - **Classic-ML MLE:** ranking and pricing (Roblox), recommendation and ads (Pinterest, TikTok), growth optimisation (OpenAI), simulation (Waymo), physics surrogates (PhysicsX).
  - **Platform or open-source MLE:** library maintenance (Hugging Face), inference engine (Together AI).
- Adjacent roles: research engineer and research scientist (more research, often PhD); software engineer in ML or ML systems (infrastructure); MLOps or ML platform; forward-deployed ML engineer (customer-facing, excluded from the sample); AI engineer (application layer, lower posted pay).
- Title wording in the sample: "Machine Learning Engineer" appears in 31 of 36 titles (86%). Five are aliases:
  - "Software Engineer, Machine Learning (India)" (Glean).
  - "Staff, Software Engineer (Machine Learning)" and "(IND) Senior Software Engineer / Senior ML Engineer" (Walmart Global Tech India).
  - "Senior ML Engineer – NLP (m/f/d)" (voize).
  - "Machine Learning Software Engineer, Research" (PhysicsX).
- Other aliases seen in listings but not sampled: "Data Scientist (MLE)" (Walmart Global Tech India), "AI/ML Engineer" (Sanmina India), "Machine Learning Systems Engineer" (Anthropic), "Forward Deployed Machine Learning Engineer" (Mistral AI), and "Perception Engineer" and "Computer Vision Engineer" (Fast AI Jobs rows).
- Title noise on Fast AI Jobs: 12 of the 50 visible rows (24%) are outside the ML-engineer family and 5 (10%) are internships or new-graduate roles (M).

### 2. Demand

| Measure | Value | Source and date |
|---|---|---|
| Live MLE postings, global | 2,157 | S1, 2026-11-13 |
| US / UK / India / Canada | 1,084 / 108 / 90 / 60 | S1, 2026-11-13 |
| California; San Francisco; New York; Seattle | 532; 187; 140; 92 | S1, 2026-11-13 |
| Remote-flagged postings | 378 on the count page (17.5% of 2,157); 14.0% on the JD page | S1; S2 (counted 2026-09-10) |
| Seniority cuts (count page) | Senior 814; Lead 359; Entry 240 (cuts overlap) | S1 |
| Seniority labels (JD page) | Entry 13.7%; Mid 2.4%; Senior 23.2%; Lead or manager 9.2%; unlabelled about 51.5% | S2 |
| Employer mix (JobsPipe top employers) | TikTok 148; Waymo 53; Pinterest 33; Adobe 31; Apple 25; ByteDance 21; Capital One 20; Roblox 18 | S1 |
| Employer size | 1000+ employees 38.9%; 201–1000 9.2%; 51–200 3.0%; 1–50 2.2% (the rest unknown) | S2 |
| AI-startup postings (Fast AI Jobs) | 298 at 171 startups; 39% at Pre-Seed to Series B; Series A 49, C 40, B 39, D 33, E 30 | S5, 2026-11-11 |
| Trend since 2025-01-01 | No dated series found | Absences |

JobsPipe's top-employer list on its count page differs from the list on its salary page (Reddit, Airbnb, Roblox), so top-employer rankings vary with the cut. The top MLE employers by volume are consumer-tech and autonomy firms (TikTok, Waymo, Pinterest), not the AI labs; my sample over-represents labs relative to volume.

### 3. Job-description sample

The sample has 36 postings, one `jd` record each.

| Employer type | n | US | Europe | India | LatAm |
|---|---|---|---|---|---|
| Frontier lab (Anthropic 1, OpenAI 5) | 6 | 6 | 0 | 0 | 0 |
| AI-native or open-source lab (Hugging Face 2, Scale AI 2, Glean 4, Together AI 1, Lila Sciences 3, PhysicsX 3, voize 1) | 16 | 10 | 4 | 2 | 0 |
| Big Tech or large consumer tech (Netflix 1, Roblox 2, Waymo 1, Pinterest 2, TikTok 1) | 7 | 7 | 0 | 0 | 0 |
| Enterprise or consultancy (Capital One 2, McKinsey 1) | 3 | 2 | 0 | 0 | 1 |
| GCC (Walmart Global Tech India 2) | 2 | 0 | 0 | 2 | 0 |
| Indian employer (Flipkart, Specbee) | 2 | 0 | 0 | 2 | 0 |
| **Total** | **36** | **25** | **4** | **6** | **1** |

- **Evidence:** 4 pages read in full (A: Anthropic, Hugging Face US, Glean Assistant Quality, Netflix), 23 employer-page extracts (B), 9 mirror-only (C).
- **Window:** 16 are confirmed live at retrieval or dated inside the window. 20 are indexed pages without a verified date. Walmart Staff (2026-08-05) is 8 days outside the window. Hugging Face US (2026-05-29) is outside by date, but its page was live at retrieval.
- **Remote and pay:** 2 postings (6%) are fully remote; 13 (36%) disclose pay.
- **Seniority by title:** 7 staff or principal, 9 senior, lead or manager, 18 mid or unspecified, 2 entry or junior.
- **Concentration:** OpenAI 5, Glean 4, Lila Sciences 3 and PhysicsX 3. No other employer exceeds 2.
- **Exclusions** (named, not a full tally; the reasons were non-MLE work, closed or stale pages, or no requirement text):
  - Anthropic Research Engineer (pretraining) and ML Infrastructure Engineer (Safeguards).
  - OpenAI Training: ML Framework Engineer.
  - Together AI Research Engineer and Inference Frameworks and Optimization Engineer.
  - Scale AI ML Engineering Manager and forward-deployed engineer.
  - Greenhouse (the company) Engineering Manager, ML.
  - Mistral AI: the MLE (Paris/London) and open-source-software MLE postings were closed or 6+ months old; its forward-deployed ML engineer postings are customer-facing.
  - McKinsey QuantumBlack forward-deployed engineer, data scientist and data engineer roles.
  - Pinterest manager and applied-research roles, and an MLE II posting whose application window ended 2026-04-07.
  - Closed or stale pages: Shield Bengaluru (closed), EvenUp early-career MLE (closed), voize ML Engineer NLP (removed 2026-02-18), Netflix MLE (removed 2025-10-31).
  - Apple mirrors (outside the window, or without requirement text).

### 4. Skills

Sample share is count out of 36 and a lower bound. Platform share is JobsPipe (counted 2026-09-10).

| Skill [ID] | Sample share (n = 36); platform | Suggested tier | KB tier | Reason |
|---|---|---|---|---|
| ML fundamentals [ml_fundamentals] | 36/36 by title; 98.6% | Must | Must | Title-defined. |
| Python [python] | 12/36 (33.3%); 71.3% | Must | Must | Core everywhere; the sample share is a lower bound. |
| PyTorch [pytorch] | 10/36 (27.8%); 48.2% | Must | Must | Dominant framework in the sample. |
| Deep learning and transformers [deep_learning] | 9/36 (25.0%); 32.6% | Important | Must | At or below a third in both sources; treat as implicit baseline. |
| LLM involvement [llm_apis] | 17/36 (47.2%); 45.0% | Must for GenAI-targeted MLE | Important | The KB restricts demand to GenAI work; 13/22 at labs and AI-native, 4/14 elsewhere. |
| Data structures and algorithms [dsa] | 0/36; 33.7% | Important | Important | Not named in the sample; interview-driven. One unsampled TikTok graduate posting lists it. |
| TensorFlow or JAX [tensorflow_jax] | 7/36 (19.4%); 31.8% | Should | Important | Mostly "PyTorch or TensorFlow" lists. |
| Experiment design and A/B testing [experiment_design] | 4/36 (11.1%); 23.5% | Should (Important in ranking and growth) | Important | OpenAI (three postings) and Glean. |
| NLP [nlp] | 6/36 (16.7%); 23.3% | Should | Important | Folded into LLM work. |
| C++ [cpp] | 2/36 (5.6%); 23.3% | Optional (Important for AV, robotics, kernels) | Important | The platform share is inflated by AV and vision employers. |
| Communication [communication] | 5/36 (13.9%); 30.3% | Important | Important | Explicit communication or explaining language only. |
| Fine-tuning [finetuning] | 6/36 (16.7%); 13.0% | Should | Important | Under 20% in both sources. |
| LLM evaluation [evals] | 11/36 (30.6%); n/a | Important (Must in the LLM-systems track) | Important | Rising and distinctive. |
| Serving literacy [serving_literacy] | 5/36 (13.9%); n/a | Should (Important on inference teams) | Important | Core only on inference teams. |
| Embeddings and retrieval [embedding_models] | 3/36 (8.3%); n/a | Should | Important | Few postings. |
| Data pipelines [data_pipelines] | 5/36 (13.9%); n/a | Should | Important | Mentioned as support work. |
| Eval statistics [eval_stats] | 0/36; n/a | Should | Important | Not named; interview-level. |
| Adaptation choice [adaptation_choice] | not computed; n/a | Important | Important | PhysicsX wording supports it (one employer, outside the sample). |
| Pragmatism [c1_pragmatism] | 2/36 (5.6%); n/a | Should | Important | Anthropic and Glean wording. |
| Trade-off explanation [c2_tradeoffs] | 1/36 (2.8%); n/a | Should | Important | voize wording. |
| Ownership and incident response [c3_ownership] | 10/36 (27.8%); n/a | Important | Important | Production deployment and ownership language; incident response is not named. |
| Responsible-AI judgement [c4_responsible_ai] | 1/36 (2.8%); n/a | Should (Important in safety and finance) | Important | Capital One. |
| RL and post-training [new:post_training_rl] | 4/36 (11.1%); n/a | Should | not in KB | Anthropic, OpenAI, Glean (two postings). |
| Cloud platforms [new:cloud_platforms] | 2/36 (5.6%); n/a | Should | not in KB | Capital One and Specbee. |
| Open-source contributions [new:open_source_contributions] | 2/36 (5.6%); n/a | Should (Must for open-source library roles) | not in KB | Both Hugging Face postings. |
| Recommendation and ranking [new:recsys_ranking] | 5/36 (13.9%); n/a | Optional (track-specific) | not in KB | Pinterest (two), TikTok, Roblox, Glean India. |
| Distributed training [new:distributed_training] | 3/36 (8.3%); n/a | Optional | not in KB | Hugging Face (two) and PhysicsX. |

### 5. Pay

| Population | Statistic | Value | Basis, n | Source and date |
|---|---|---|---|---|
| US, Levels.fyi MLE | P25 / P50 / P75 / P90 | $200K / $285,650 / $387K / $498K | TC, self-reported, n not shown | S7, 2026-11-12 |
| Live postings with pay (platform) | P25 / P50 / P75 | $183K / $224K / $268K | posted pay, n = 582 | S3, retrieved 2026-11-13 |
| AI Engineer, same platform | P25 / P50 / P75 | $144K / $181K / $215K | posted pay, n = 568 | S4 |
| AI startups, Fast AI Jobs | median | $202,500 (range $128–400K) | posted pay, n = 61 | S6 |
| US exact-title H-1B LCAs, FY2026 to date | median, IQR | $172,900; $150,000–192,941 | offered wage, 53 filings, 28 employers | S35 |
| Sample (US), posted base midpoints | median | about $247K | base, n = 12, skewed to labs, AI-native and large consumer tech | S41 (M) |

By level in the sample, posted base:
- Mid: Glean $180–205K; Together AI $160–230K; Scale AI MLE, Public Sector (DC band) $196–245K; Pinterest Core Engineering $139–286K (wide, location-tiered).
- Senior: Roblox $243–295K; Capital One Senior Manager (MLE 5 band) $251–286K; Capital One Lead (location bands) $176–241K; Pinterest Monetization $163–286K.
- Staff and above: Anthropic $340–560K; Scale AI Staff (DC band) $260–327K; Waymo Senior Staff $281–356K.
- OpenAI Core Experimentation (Seattle): $437–485K. Netflix L4: $170–720K, salary-only.

Meta on Levels.fyi: the company page extract shows E3 $187K to E6 $660K, with the highest reported $789,812 (S8). K4's E6 $782K is probably a high percentile; not resolved. A secondary blog citing Levels.fyi gave a median of about $262K for 2025–2026 (S40), so the Levels.fyi median rose about 9% to $285,650 as of 2026-11-12 (C).

India (as labelled by each source):

| Population | Value | n, date, source |
|---|---|---|
| Bengaluru MLE, Flexiple | median ₹19.9L; IQR ₹9.2–35.6L; P90 ₹57.7L | n = 422, Aug 2026, S10 (C) |
| Bengaluru MLE, Hyring model | median ₹21.1L; IQR ₹14.3–35.9L | modelled, S11 (C) |
| Bangalore MLE, Interview Query | median TC $61K | n = 27, S12 (C) |
| Levels.fyi Greater Bengaluru, all SWE | median TC ₹55.4L | SWE family, 2026-07-18, S9 |

Only these India figures were found. Pay by employer type is not published at that cut (Absence).

### 6. Interview loop

| Employer | Stages and content | AI policy | Grade |
|---|---|---|---|
| Meta | Recruiter and phone screens; five-round onsite (two coding, system design, ML design, behavioural). ML design centres on ranking and recommendation. | Some candidates report a 45-minute AI-enabled coding round. | C |
| Glean | Not published beyond the AI element. | The interview includes a brief AI-focused exercise or discussion. The application asks which AI tools you use. | A |
| Anthropic | Not published for this role. | The application asks you to confirm AI partnership guidelines. A "Why Anthropic?" answer of 200–400 words is valued. | A |
| OpenAI | Multi-stage, with live pair coding and/or a take-home, plus ML system design. | Not published. | C |
| Google | ML system design and ML depth rounds replace some SWE rounds. | Not published. | C |
| Cross-employer | 4–6 stages over 3–6 weeks; take-homes are common. | A practitioner who hires AI engineers says AI-tool use is part of the interview and take-homes resemble small product features (C). | C |

The KB's track (classic ML system design) fits at grade C. Its extension "plus where an LLM would help" has no source. I did not run a search on Indian GCC loops.

### 7. Proof of work

Employers and one practitioner name the following:
- **Public open-source work:** "a public track record of open-source contributions, for example merged pull requests" (Hugging Face, read).
- **Shipped production ownership:** "a track record of shipping production systems, not just prototypes" (Glean, read). A Scale AI posting seen through a mirror asks for "a shipped project with real users behind it, where you owned it after launch" (C).
- **Evaluation discipline:** "building evaluations … using error analysis and regression tests" (voize, mirror).
- **Evidence-based adaptation:** a PhysicsX post-training posting asks you to use evidence to decide whether training is better than changes to prompts, tools or agent design.
- **Ship, measure, defend:** Louis-François Bouchard, a practitioner who hires AI engineers and writes in his own name (article updated 2026-08-28), asks for a small AI product shipped end to end, measured against a real baseline, with the choices defended. He lists a fine-tuned model without a serious baseline, imprecise technical claims and dead repositories as red flags (C; the role is AI engineer, not MLE).

These support K14 and K15. I found no hiring-manager interviews written for the MLE role (Absence); other results for this query were SEO blogs and were not used.

### 8. Credentials

| Credential | State at 2026-11-13 | Detail | Source |
|---|---|---|---|
| AWS Certified ML – Specialty (MLS-C01) | Retired | Last exam 2026-03-31; holders stay active 3 years from award. | S13 |
| AWS ML Engineer – Associate MLA-C01 | Retired (English) | Last English exam 2026-09-28. | S14, S15 |
| AWS ML Engineer – Associate MLA-C02 | Beta | Beta registration from 2026-09-01; covers GenAI, fine-tuning and RAG; standard availability early 2027 per third parties. Fee not confirmed. | S14, S15, S19 |
| Google Cloud Professional ML Engineer | Active | $200, 2 hours, 50–60 questions; guide dated 2026-06-01. Validity is "2 years" on Google's page extract; a third party says 3. | S16, S17, S19 |
| NVIDIA NCP-GENL | Active | $200, 120 minutes, 2-year validity; some localised NVIDIA pages still say "Coming soon". | S18 |

JD signal: 0 of 36 sampled postings name any certification (lower bound from partial text). K12's "tie-breaker in GCP shops" has no source.

### 9. Entry routes and prerequisites

- **Degree.** Stated in 14 of 36 postings (39%); 8 of those 14 accept equivalent experience (M). Labs and AI-native firms state one less often (5 of 22, 23%) than other employers (9 of 14, 64%).
- **Experience.** 17 postings state years; the median is 5 and the range is 2 to 10. Senior-titled postings ask 5–8+.
- **Entry roles.** Two of 36 in the sample: a TikTok new-graduate PhD programme (2027 start, Seattle) and a PhysicsX junior role. JobsPipe lists 240 entry-level roles, mostly new-graduate, PhD or recruiter-posted programmes. Fast AI Jobs shows 5 of 50 rows as internships or new-graduate roles.
- **Routes.** Backend-to-MLE and data-scientist-to-MLE are the routes visible in the postings' stated prior experience ("Software Engineer or Machine Learning Engineer in a product company", "Data Scientist, or in a comparable quantitative engineering role"). The PhD route leads to lab and research-leaning roles. Frontend, DevOps or SRE, product-management and non-technical routes are not evidenced.
- **Transition times.** The only source found (a 2026 blog with an undisclosed method) is graded D and not used. Pre-2025 analyses exist but are stale and not used (Absences).

### 10. Progression, durability, leverage

- **Ladders.** Netflix uses L4 and L5. Pinterest's own careers site describes MLEs at L13–L16 reporting to a Manager II (S43). Capital One's ladder runs from Machine Learning Engineer through Lead and Senior Lead to Senior Manager (its Senior Manager posting labels the band "Machine Learning Engineer 5"). Roblox and Anthropic use Senior, Staff and Principal.
- **Exits.** Research or applied scientist, ML platform and inference, forward-deployed ML, and ML management (Scale AI, Greenhouse and Pinterest post manager roles).
- **Commoditisation signals.**
  - 70% of 20 interviewed agent deployments used off-the-shelf models without weight tuning (S34).
  - Capital One asks for AI tooling "beyond basic code completion" (mirror of a Senior Lead posting, S32).
  - AWS rewrote its ML-engineer exam around GenAI and agentic work.
- **Growth signals.** Fine-tuning or RL appears in 22% (8/36) of sampled postings, and evals in 31%.
- **Leverage.** Sampled roles sit near revenue: paid-marketing optimisation (OpenAI), marketplace pricing and ranking (Roblox), ads ranking (Pinterest, TikTok) and risk (Capital One). This is judgement-grade (D), unmeasured.

### 11. Work footprint and specialisations

Categories overlap.

| Layer or specialisation | Sample share | Note |
|---|---|---|
| Post-training and adaptation (fine-tuning or RL) | 8/36 (22%) | L4 is real but a minority. |
| Evaluation plane | 11/36 (31%) | The largest GenAI-specific cluster. |
| Serving and inference | 5/36 (14%) | Concentrated on inference teams. |
| Retrieval, RAG or similarity search | 3/36 (8%) | |
| Non-GenAI classic ML | 19/36 (53%) | Ranking, ads, safety, simulation, physics, vision. |
| Fine-tuning and domain adaptation (KB specialisation) | 6/36 (16.7%) | |
| Synthetic data (KB specialisation) | 0/36 | One unsampled PhysicsX post-training posting mentions it. |

### 12. Geography and sponsorship

- **Concentration.**
  - By country (JobsPipe, counted 2026-09-10): US 50.3%, India 7.7%, UK 6.8%, Singapore 5.9%, Canada 3.6%, Germany 3.1%, France 2.4%, Brazil 1.8%.
  - Within the US, California holds 532 roles; San Francisco, New York and Seattle lead the cities. TikTok runs graduate programmes in San Jose and Seattle.
- **Remote.** About 14–17.5% remote-flagged on JobsPipe; 2 of 36 sampled postings are fully remote.
- **Sponsorship.** Anthropic's posting says it sponsors visas but cannot for every role. Capital One says it "will consider sponsoring". Glean's form asks about sponsorship.
- **LCA data.**
  - 53 certified LCAs for the exact title in FY2026 to date, from 28 employers. Meta and Apple filed 6 each and Block 5.
  - Filing states: CA 25, WA 10, NY 7, MA 3, TX 3.
  - A broader AI/ML role family shows 8,275 certified LCAs across FY2025 and FY2026 through Q3 (median $167,485).
  - These are filings, not workers or pay.

### 13. Résumé and profile signals

- **What postings reward.** Evidence of shipping and owning production systems; public open-source work; evaluation and error analysis; plain statements of what you decided and why.
- **Keywords.** PyTorch, LLM, fine-tuning, RL, evals, vLLM, TensorRT-LLM, Hugging Face Transformers, A/B testing, recommender systems, feature engineering.
- **Red flags.** Tool lists without use, fine-tuning presented as the default answer, no baseline, dead repositories, and ignoring application instructions. Hugging Face asks you to start your first answer with "GPU-poor and proud", which tests whether you read the posting.
- **Evidence-line patterns (P).** See the `practice` records. These are patterns only; no achievements are invented.

### 14. Misconceptions and risks

- **"MLE means LLM fine-tuning."** Fine-tuning is named in 17% of sampled postings (13.0% on the platform). 53% of sampled postings have no GenAI element.
- **Title inflation and mixing.** OpenAI "MLE" roles range from growth optimisation to cloud-platform engineering. Netflix's band is $170K–$720K. Capital One's "Senior Manager, MLE" carries an "MLE 5" band label.
- **Aggregator noise.** Recruiter posters, talent-pool listings, contract roles, and stale index pages. PitchMeAI, an aggregator, rates ghost-job risk at Pinterest as high (160 stale of 190 open; median 66 days open, by its own tracking; C). I treat this as an attributed claim, not a measurement.
- **Lexicon extraction.** JobsPipe skill shares count mentions, not requirements.

### 15. India

- **Volume.** 90 live roles (JobsPipe count page), or 7.7% on the JD page; treat the India share as 4–8%.
- **Employers seen.** Walmart Global Tech India, Glean Bangalore, Flipkart, Specbee, Chargebee, Skild AI and Cerebras (Bengaluru), and Sanmina (Chennai).
- **Aliases.** "Data Scientist (MLE)", "Software Engineer – ML", "AI/ML Engineer".
- **Experience asks.** 4+ years (Flipkart), 6+ (Glean India, Specbee, Walmart), 8–13 (Walmart Staff). All six Indian postings in the sample state years of experience, against 17 of 36 overall.
- **Pay.** Broad median about ₹20L; the KB's Levels.fyi figure is unverified. Interview differences were not found (Absence).

### Probes specific to this session

- **Share involving LLMs or GenAI.** 45.0% on the platform; 47% in the sample (±16 points). The sample splits 59% (13/22) at labs and AI-native firms against 29% (4/14) elsewhere.
- **Classic ML system design against LLM work.** Reports (C) centre on ranking and recommendation design plus coding; AI-forward employers add AI-use exercises. No loop evidence separates LLM-systems design from classic design.
- **Premium over AI Engineer.** +$43K, or +24%, at the median on one platform (M). Within-employer pairs were not completed.

### Strongest objections

| Objection | Evidence for | Evidence against |
|---|---|---|
| The sample is too small and skewed for skill shares. | n = 36, ±16 points; 32 postings with partial text. | The LLM share (47%) and fine-tuning share (17%) sit close to the platform values (45.0% and 13.0%). |
| Levels.fyi overstates market pay. | Self-reported and skewed to big employers; the posted-pay median is $224K and the LCA median $172,900. | LCA wages are offered wages for a narrow title set. |
| The India gap is a sample-composition artefact. | Levels.fyi favours product and GCC employers; broad samples give about half. | The Levels.fyi MLE Bengaluru page was not opened. |
| The "70% off-the-shelf" statistic overstates commoditisation. | It covers 20 interviewed agent deployments. | Fine-tuning or RL still appears in 22% of sampled postings. |
| Certification data from snippets may be wrong. | AWS and NVIDIA statements are extracts. | Several independent sources agree on dates and fees. |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Definition: builds, trains, adapts, serves; classic ML remains large | confirmed | Three families in the sample; 53% have no GenAI element [S41][S2] | B/M |
| K2 | Title aliases | updated | New aliases: ML Software Engineer, SWE–ML (India), Data Scientist (MLE), ML Systems Engineer, forward-deployed MLE; the "(GenAI MLE)" label was not seen [S41][S5] | M |
| K3 | Demand: JobsPipe 1,084 / 2,157 / 90; Fast AI 273 at 159; LLM 45.0%; TikTok 74 | updated | Fast AI is 298 at 171 (2026-11-11); TikTok 148; US 1,084, global 2,157 and India 90 match; the LLM share was counted 2026-09-10, not 2026-11-02 [S1][S2][S5] | B |
| K4 | US TC P50 $280K, P75 $385.5K, P90 $497.5K (n = 1,063); Meta and Google figures | updated | P50 $285,650, P75 $387K, P90 $498K (2026-11-12); Meta E6 figure unresolved [S7][S8] | B |
| K5 | India 90 live; India 7.7% against US 50.3% | updated | 90 is 4.2% of 2,157; the 7.7% is on a different snapshot (counted 2026-09-10) [S1][S2] | B |
| K6 | Bengaluru Levels.fyi P50 ₹44.5L, P90 ₹94.6L (n = 96) | unverifiable | Levels.fyi page not opened; Flexiple n = 422 gives a median of ₹19.9L [S10][S9] | C |
| K7 | Durability judgement; 70% off-the-shelf | updated | The 70% is of 20 interviewed agent cases (survey n = 306), not "production apps" [S34] | B |
| K8 | Footprint: L4 plus L2 and L3 | updated | Fine-tuning or RL 22%, evals 31%, serving 14%, non-GenAI 53% [S41] | M |
| K9 | Interview track: classic ML system design | confirmed | Reports and prep guides (C); the LLM extension is unsourced [S37] | C |
| K10 | Must skills and shares | confirmed | JobsPipe shares unchanged; deep learning is borderline (25% in the sample) [S2][S41] | B/M |
| K11 | Important skills and shares | confirmed | Shares unchanged; tier changes suggested in item 4 [S2][S41] | B/M |
| K12 | Credentials | updated | MLS-C01 retired; MLA-C01 ended 2026-09-28 (MLA-C02 in beta); PMLE and NCP-GENL active; 0/36 JD mentions [S13][S14][S16][S18] | B |
| K13 | Prerequisites and transition times | unverifiable | JD labels (entry 13.7%, senior 23.2%) match; the 72% degree share and transition times could not be reproduced (sample: degree stated in 39%) [S2][S41] | B/D |
| K14 | Proof of work | confirmed | Employer wording supports each element except serving benchmarks [S22][S21][S33][S30][S45] | B |
| K15 | Leave out fine-tuning as default; unread tools | confirmed | 70% of 20 case studies; fine-tuning named in 17% of sampled postings [S34][S41] | B |

## Absences

| Item | Where I looked | Note |
|---|---|---|
| Dated posting-count trend since 2025-01-01 | JobsPipe, Fast AI Jobs, general search | Only snapshots; K3's earlier figures have no date. |
| Employer-published MLE loop formats | Employer sites, posting text | Only AI-use policies (Glean, Anthropic). |
| Hiring-manager statements on proof of work written for the MLE role | One general search and one fetch | One named practitioner (Bouchard), writing about AI engineers; the other results were SEO blogs and were not used. |
| 2025+ analysis of prior roles of MLEs with a stated method | LinkedIn, Indeed and bootcamp analyses | Only pre-2025 pieces and an unsourced 2026 blog. |
| Levels.fyi Bengaluru MLE page (K6) | Two targeted searches | Not retrieved. |
| Levels.fyi Google L5 and L6 figures (K4) | Not re-verified | |
| Within-employer MLE against AI Engineer pay pairs | JobsPipe, JobsRadar | Aggregate comparison only. |
| Big Tech postings from employer boards (Meta, Google, Amazon, Microsoft, Apple) | Search and fetch | Not reached; Apple mirrors were outside the window. Netflix, Roblox, Waymo, Pinterest and TikTok were reached. |
| Consultancy and IT-services postings beyond McKinsey (Accenture, Deloitte, TCS, Infosys) | Not searched | Gap in employer-type coverage. |
| India interview differences; India pay by employer type | General search | Not found. |
| Mistral AI MLE postings inside the window | Lever page and mirrors | MLE and open-source-software MLE postings were closed or 6+ months old; forward-deployed ML engineer postings were excluded as customer-facing. |
| OpenAI employer pages | Fetch | Blocked by bot detection; search extracts only. |
| Entry-level postings in the sample | | Only 2 of 36. |
| Non-English and non-US postings | | One German mirror (voize); no French or other-language search. |
| Synthetic-data share | | 0/36 in captured text. |

## Open Questions & Risks

- Does a read of Meta, Google, Amazon and Microsoft boards shift the LLM share or the pay medians?
- Would a full-text pass lift the skill shares toward the platform values, given 32 postings with partial text?
- Which JobsPipe snapshot is right for India (90 roles against 7.7%)?
- Is Google's PMLE validity 2 or 3 years?
- When does MLA-C02 reach general availability, and at what fee?
- Does the posted-pay median (about $224K) hide a split between lab and enterprise bands?
- Do consultancies and IT-services employers (Accenture, Deloitte, TCS, Infosys) filter on certificates?
- Risk: mirror and extract evidence can be stale.
- Risk: platform extraction is lexicon-based, and ghost-job or re-posting effects can inflate counts.

## Discovered Concerns

- JobsPipe's JD page says "Counted on 2026-09-10", while K3 attributes the shares to 2026-11-02.
- JobsPipe's own India figures are inconsistent (90 roles is 4.2% of 2,157, against a 7.7% share).
- A Levels.fyi city-page markdown file labelled "United States" shows a $145,000 median (Miami); it is easy to mis-cite.
- AWS replaced MLA-C01 within weeks of the KB's note; treat certification statuses as V2.
- Greenhouse and Lever boards re-post old requisition IDs, so an old ID does not imply an old posting: Fast AI Jobs lists a Glean posting under an old ID with a 2026-11-04 date.
- Fast AI Jobs' ML Engineer role page includes CV, perception and MLOps titles.
- Graduate postings labelled "2026 Start" remain indexed in mirrors and are stale for application purposes.
- Aggregator ghost-job claims (PitchMeAI on Pinterest) are unmeasured.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | LLM share about 40–50% | Confirmed | 45.0% platform; 47% sample | Keep the two-track framing. |
| P2 | Levels.fyi US median about $270–290K | Confirmed | $285,650 (2026-11-12) | No change to the US pay anchor. |
| P3 | MLA-C01 is the in-force AWS exam | Contradicted | MLA-C01 ended 2026-09-28; MLA-C02 in beta | Update K12 and the credential records. |
| P4 | Degree stated in a majority | Contradicted | 39% in the sample | Soften the degree wording. |
| P5 | Fine-tuning in under 20% | Confirmed | 16.7% sample; 13.0% platform | Keep fine-tuning at Should. |
| P6 | India Levels.fyi median well above broad samples | Updated | Flexiple ₹19.9L against the KB's ₹44.5L (unverified) | Report India pay as a range. |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | JobsPipe, Machine Learning Engineer jobs: 2,157 live roles — https://jobspipe.dev/jobs/machine-learning-engineer | n/a (live) | 2026-11-13 | B | Read + Extract (filter counts from a search snippet of the same page) | single-source | Demand counts, top employers |
| S2 | JobsPipe, MLE job description page — https://jobspipe.dev/job-description/machine-learning-engineer | counted 2026-09-10 | 2026-11-13 | B | Read | single-source | Skill shares, seniority, geography |
| S3 | JobsPipe, MLE salary — https://jobspipe.dev/salary/machine-learning-engineer.md | n/a | 2026-11-13 | B | Extract | single-source | Posted-pay median |
| S4 | JobsPipe, AI Engineer salary — https://jobspipe.dev/salary/ai-engineer.md | n/a | 2026-11-13 | B | Extract | single-source | AI Engineer comparison |
| S5 | Fast AI Jobs, ML Engineer role page — https://www.fastaijobs.com/jobs/role/ml-engineer | 2026-11-11 | 2026-11-13 | B | Read | single-source | Startup demand, title noise |
| S6 | Fast AI Jobs job pages (Scale AI London; Together AI) — https://www.fastaijobs.com/job/greenhouse--4413274005 | n/a | 2026-11-13 | B | Extract | single-source | MLE salary median (n = 61) |
| S7 | Levels.fyi, Machine Learning Engineer salary — https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer | 2026-11-12 | 2026-11-13 | B | Read | self-reported | US TC percentiles |
| S8 | Levels.fyi, Meta MLE salaries — https://www.levels.fyi/companies/meta/salaries/software-engineer/title/machine-learning-engineer | n/a | 2026-11-13 | B | Extract | self-reported | Meta levels |
| S9 | Levels.fyi, software engineer in Greater Bengaluru (md) — https://www.levels.fyi/t/software-engineer/locations/greater-bengaluru | 2026-07-18 | 2026-11-13 | B | Extract | self-reported | India SWE benchmark |
| S10 | Flexiple, MLE salary in Bengaluru — https://www.flexiple.com/salary/machine-learning-engineer/bengaluru | 2026-08 | 2026-11-13 | C | Extract | single-source | India pay |
| S11 | Hyring, MLE salary in Bengaluru — https://www.hyring.com/jobseeker-toolkit/salary/machine-learning-engineer-salary-in-bengaluru | 2026 | 2026-11-13 | C | Extract | modelled | India pay |
| S12 | Interview Query, MLE salary in Bangalore — https://www.interviewquery.com/salaries/machine-learning-engineer-salary-in-bangalore-india | n/a | 2026-11-13 | C | Extract | small n | India pay |
| S13 | AWS, Certified Machine Learning – Specialty — https://aws.amazon.com/en/certification/certified-machine-learning-specialty | n/a | 2026-11-13 | B | Extract | corroborated | MLS-C01 retirement |
| S14 | AWS Training and Certification Blog, September 2026 new offerings — https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/ | 2026-09 | 2026-11-13 | B | Extract | corroborated | MLA-C01 end, MLA-C02 beta |
| S15 | AWS blog, Updates to the ML Engineer – Associate exam (MLA-C02); AWS Builder Center post (September 2026) — https://aws.amazon.com/blogs/training-and-certification/updates-to-aws-certified-machine-learning-engineer-associate-mla-c02/ | 2026 | 2026-11-13 | B | Extract | corroborated | Dates and scope |
| S16 | Google Cloud, Professional Machine Learning Engineer certification — https://cloud.google.com/certification/machine-learning-engineer | n/a | 2026-11-13 | B | Extract | single-source | Fee, duration, validity |
| S17 | Google, Professional ML Engineer exam guide (PDF) — https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf | 2026-06-01 | 2026-11-13 | B | Extract | single-source | Guide date |
| S18 | NVIDIA, NVIDIA-Certified Professional: Generative AI LLMs — https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/ | n/a | 2026-11-13 | B | Extract | single-source | Fee, duration, validity |
| S19 | Third-party certification explainers (k21academy, Tutorials Dojo, certcrush, Ascendient, certempire); URLs not retained individually | 2026 | 2026-11-13 | C | Extract | conflicting on PMLE validity | MLA-C02 timing, PMLE validity conflict |
| S20 | Anthropic, Staff Machine Learning Engineer, Virtual Collaborator — https://job-boards.greenhouse.io/anthropic/jobs/4946308008 | n/a | 2026-11-13 | A | Read | COI | JD; sponsorship; AI-use policy |
| S21 | Glean, Machine Learning Engineer, Assistant Quality — https://job-boards.greenhouse.io/gleanwork/jobs/4711484005 | 2026-10-20 (per mirror) | 2026-11-13 | A | Read | single-source | JD; AI exercise; proof wording |
| S22 | Hugging Face, Open-Source Machine Learning Engineer – US Remote — https://apply.workable.com/huggingface/jobs/view/19A136F8E2 | 2026-05-29 | 2026-11-13 | A | Read | single-source | JD; proof wording |
| S23 | Netflix, Machine Learning Engineer (L4) – Infrastructure Algorithms and ML — https://jobs.lever.co/netflix/94c7b46a-4fcb-4b3b-8260-8d43baee85ec | n/a | 2026-11-13 | A | Read | single-source | JD; pay |
| S24 | OpenAI careers pages (https://openai.com/careers/machine-learning-engineer-implicit-signals-san-francisco/ and four sibling pages) with a16z, thrivecap and resumegeni mirrors for dates and pay | 2026-08 to 2026-10 | 2026-11-13 | B | Extract (fetch blocked) | mirror dates and pay | OpenAI JDs |
| S25 | Scale AI Greenhouse pages (https://job-boards.greenhouse.io/scaleai/jobs/4631848005, .../4654382005) with Accel and Index mirrors | 2026-11-05 | 2026-11-13 | B | Extract | mirror | Scale AI JDs; proof wording |
| S26 | Glean Greenhouse pages (https://job-boards.greenhouse.io/gleanwork/jobs/4632997005, .../4712438005, https://boards.greenhouse.io/gleanwork/jobs/4012745005) | n/a | 2026-11-13 | B | Extract | single-source | Glean JDs |
| S27 | Hugging Face Workable page (https://apply.workable.com/huggingface/jobs/view/9E2A4C02C7) | n/a | 2026-11-13 | B | Extract | single-source | HF Voice Agents JD |
| S28 | Together AI Greenhouse page (https://job-boards.greenhouse.io/togetherai/jobs/4385540007) | 2026-11-02 (listing) | 2026-11-13 | B | Extract | mirror pay | Together AI JD |
| S29 | Lila Sciences Greenhouse pages (https://job-boards.greenhouse.io/lilasciences/jobs/4302917009, .../4116513009, .../4222224009) | 2026-11-04 (listing) | 2026-11-13 | B | Extract | single-source | Lila JDs |
| S30 | PhysicsX Greenhouse pages (https://job-boards.greenhouse.io/physicsx/jobs/4648881101, .../4652630101, https://job-boards.eu.greenhouse.io/physicsx/jobs/4880947101, .../5029174101) | n/a | 2026-11-13 | B | Extract | single-source | PhysicsX JDs; adaptation wording |
| S31 | Roblox careers pages (https://careers.roblox.com/jobs/7573319, .../7347389) | n/a | 2026-11-13 | B | Extract | mirror pay | Roblox JDs |
| S32 | Capital One careers site (https://www.capitalonecareers.com/en/job/mclean/senior-manager-machine-learning-engineer/1732/101273104112) and Built In and Anitab mirrors | 2026-09-28 | 2026-11-13 | B | Extract | mirror | Capital One JDs; sponsorship; AI-tooling wording |
| S33 | Job-board mirrors for Waymo (jobera), Walmart Global Tech India (aijobs.ai, jobs.anitab.org), Flipkart (gravityer), Specbee (career.io), voize (Arbeitnow, choppingblock); exact URLs in the `jd` records | 2026 | 2026-11-13 | C | Extract | mirror | Nine JDs; proof wording (voize) |
| S34 | Measuring Agents in Production, arXiv:2512.04123 — https://arxiv.org/abs/2512.04123 | 2025-12-02 (v1); 2026-02-03 (v3) | 2026-11-13 | B | Extract | single-source | 70% off-the-shelf statistic |
| S35 | visa-bulletin.us, Top H-1B sponsors for Machine Learning Engineer — https://visa-bulletin.us/h1b-sponsors/ml-engineer/ | FY2026 | 2026-11-13 | B | Extract | DOL data via aggregator | LCA counts and wages |
| S36 | careery.pro and h1bvisajobs.com LCA pages; URLs not retained individually | 2026 | 2026-11-13 | C | Extract | aggregator | Wider LCA context |
| S37 | Interview reports and prep guides (Glassdoor Meta MLE report 2026-03; Codemia; PracHub; Interview Query; Dataford; f1jobs); URLs not retained individually | 2026 | 2026-11-13 | C | Extract | vendor and candidate reports | Loop evidence |
| S38 | atr-blog.pages.dev, AI career switching guide 2026 | 2026 | 2026-11-13 | D | Extract | method unstated | Not used as evidence |
| S39 | JobsRadar, AI Engineer salaries — https://jobs-radar.com/salaries/ai-engineer | n/a | 2026-11-13 | C | Extract | single-source | AI Engineer pay cross-check |
| S40 | Secondary salary blogs citing Levels.fyi (KORE1 2026-07-02, Interview Kickstart, MentorCruise); URLs not retained individually | 2026 | 2026-11-13 | C | Extract | secondary | Earlier Levels.fyi median (about $262K) |
| S41 | Author's sample of 36 postings (URLs in the `jd` records) | 2026-11-13 | 2026-11-13 | M | Read + Extract | own calculation | Skill shares and sample measures |
| S42 | McKinsey & Company, Machine Learning Engineer – QuantumBlack Studio (job 112295) — https://www.mckinsey.com/careers/search-jobs/jobs/machinelearningengineer-quantumblackstudio-112295 | n/a | 2026-11-13 | B | Extract | single-source | McKinsey JD |
| S43 | Pinterest MLE postings: career.com and Arc mirrors (https://www.career.com/job/pinterest/machine-learning-engineer-core-engineering/j202504022224148877458), PitchMeAI summary, and pinterestcareers.com manager posting (https://www.pinterestcareers.com/jobs/7075176/manager-ii-machine-learning-engineering-core-engineering/) | 2026-05-31 and later | 2026-11-13 | C | Extract | mirror | Pinterest JDs; L13–L16 ladder; ghost-job claim |
| S44 | TikTok careers, MLE Graduate (E-Commerce Recommendation Mall) – 2027 Start (PhD) — https://lifeattiktok.com/search/7672883737036654853 | n/a | 2026-11-13 | B | Extract | single-source | TikTok JD; graduate programmes |
| S45 | Louis-François Bouchard, How to Get an AI Engineer Job in 2026 — https://www.louisbouchard.ai/what-i-look-for-when-hiring-ai-engineers/ | updated 2026-08-28 | 2026-11-13 | C | Read | named practitioner; AI-engineer role | Proof of work; AI-use in interviews |
| S46 | Mistral AI postings (https://jobs.lever.co/mistral/c7b7fdfe-a071-4d62-bc15-7bcdff8067e7 and mirrors) | 2026 | 2026-11-13 | C | Extract | mirror | Exclusion evidence |

## Data Appendix

```jsonl
{"type": "jd", "grade": "A", "src": ["S20"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Anthropic", "title": "Staff Machine Learning Engineer, Virtual Collaborator", "url": "https://job-boards.greenhouse.io/anthropic/jobs/4946308008", "job_id": "4946308008", "seen": "2026-11-13", "location": "San Francisco, CA", "remote": false, "seniority": "staff", "years": null, "degree": "Bachelor's degree in a related field or equivalent experience", "must": ["Are a very experienced Python programmer", "Have strong machine learning experience", "Thrive at the intersection of research and product, with a pragmatic approach to solving real-world problems"], "nice": ["Reward modeling and preventing reward hacking in RL systems", "Developing evaluation frameworks for open-ended tasks"], "pay": {"lo": 340000, "hi": 560000, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "COI: employer is the model developer. Read in full; posting date not shown; hybrid with 25% in office; posting says visas are sponsored; responsibilities include scalable data pipelines with quality control and rubric-based evaluation systems; boilerplate says communication skills are greatly valued"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "OpenAI", "title": "Machine Learning Engineer, Implicit Signals", "url": "https://openai.com/careers/machine-learning-engineer-implicit-signals-san-francisco/", "job_id": null, "seen": "2026-11-13", "location": "San Francisco, CA", "remote": null, "seniority": "unspecified", "years": null, "degree": null, "must": ["Experience taking ML projects from problem formulation and experimentation through production deployment", "Strong foundations in supervised learning, statistics, and experimental design"], "nice": ["Experience with model distillation, representation learning, calibration, or efficient inference"], "pay": null, "ats": "Ashby", "note": "Employer page fetch blocked by bot detection; text from search extract; posted 2026-10-13 per resumegeni mirror; owns classifiers through supervised fine-tuning, distillation, evaluation, deployment and production inference"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "OpenAI", "title": "Machine Learning Engineer, Growth", "url": "https://openai.com/careers/machine-learning-engineer-growth-san-francisco/", "job_id": null, "seen": "2026-11-13", "location": "San Francisco, CA", "remote": null, "seniority": "unspecified", "years": 5, "degree": null, "must": ["5+ years of experience as a Machine Learning Engineer, Applied Scientist, Data Scientist, or in a comparable quantitative engineering role, or an equivalent record of impact", "Strong foundations in machine learning and statistics, with experience applying optimization or control methods to decisions under uncertainty"], "nice": null, "pay": null, "ats": null, "note": "Extract only; date not shown; paid-marketing optimisation models; classic ML; team text names experimentation"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "OpenAI", "title": "Machine Learning Engineer, API Multicloud", "url": "https://openai.com/careers/machine-learning-engineer-api-multicloud/", "job_id": null, "seen": "2026-11-13", "location": "San Francisco, CA", "remote": null, "seniority": "unspecified", "years": 3, "degree": "Master's or PhD in Computer Science, Machine Learning, or a related field, or equivalent practical experience", "must": ["3+ years of professional engineering experience in relevant ML, infrastructure, or product-driven engineering roles", "Strong ML engineering experience building, training, fine-tuning, evaluating, or deploying production AI systems, with hands-on experience in deep learning, transformer models, and frameworks like PyTorch or TensorFlow", "Hands-on experience with training and fine-tuning large language models, including methods like supervised fine-tuning, distillation, preference optimization, reinforcement learning, or other post-training techniques"], "nice": null, "pay": null, "ats": null, "note": "Extract only; date not shown; platform-style MLE adapting OpenAI models for cloud partners, starting with AWS"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "OpenAI", "title": "Machine Learning Engineer, Core Experimentation", "url": "https://openai.com/careers/machine-learning-engineer-core-experimentation-seattle/", "job_id": null, "seen": "2026-11-13", "location": "Seattle, WA", "remote": false, "seniority": "unspecified", "years": null, "degree": null, "must": ["Have a strong grounding in machine learning, statistics, computer science, or a related field through formal study or equivalent practical experience"], "nice": null, "pay": {"lo": 437000, "hi": 485000, "currency": "USD", "period": "year"}, "ats": null, "note": "Posted 2026-09-24 and pay band from a16z jobs mirror; hybrid; Statsig team; responsibilities include cross-experiment learning systems and agent workflows; no named degree"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "OpenAI", "title": "Machine Learning Engineer, Multimodal Perception and Authentication", "url": "https://openai.com/careers/machine-learning-engineer-multimodal-perception-and-authentication-san-francisco/", "job_id": null, "seen": "2026-11-13", "location": "San Francisco, CA", "remote": null, "seniority": "unspecified", "years": null, "degree": null, "must": ["Have a strong background in computer vision, audio or speech machine learning, multimodal learning, or sensing", "Have experience developing specialized machine learning models, larger multimodal models, or both"], "nice": null, "pay": null, "ats": "Ashby", "note": "Posted 2026-08-21 per thrivecap mirror; extract only"}
{"type": "jd", "grade": "A", "src": ["S22"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Hugging Face", "title": "Open-Source Machine Learning Engineer - US Remote", "url": "https://apply.workable.com/huggingface/jobs/view/19A136F8E2", "job_id": "19A136F8E2", "seen": "2026-11-13", "location": "New York, US (Remote)", "remote": true, "seniority": "unspecified", "years": null, "degree": null, "must": ["Strong Python skills, with experience writing clean, well-tested, maintainable library code", "Deep hands-on experience with a modern deep-learning framework, especially PyTorch (JAX or TensorFlow a plus)", "A public track record of open-source contributions, for example merged pull requests to ML or data libraries, that we can review on GitHub"], "nice": ["Experience maintaining an open-source project", "Familiarity with distributed training, inference optimization, or GPU/accelerator performance work", "Experience training or fine-tuning models at scale"], "pay": null, "ats": "Workable", "note": "Read in full; posted 2026-05-29 (outside the 90-day window) but page live at retrieval; applicants must open the first answer with a stated phrase; also asks for fluent written English for asynchronous collaboration; role text names transformer architectures and vLLM"}
{"type": "jd", "grade": "B", "src": ["S27"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Hugging Face", "title": "Senior Machine Learning Engineer, Voice Agents - EMEA Remote", "url": "https://apply.workable.com/huggingface/jobs/view/9E2A4C02C7", "job_id": "9E2A4C02C7", "seen": "2026-11-13", "location": "EMEA (Remote)", "remote": true, "seniority": "senior", "years": null, "degree": null, "must": ["Senior engineer, able to own a substantial part of an architecture and drive it forward autonomously", "Substantial open-source contributions to a Python library. Comfortable with async Python and distributed systems, including their failure modes"], "nice": null, "pay": null, "ats": "Workable", "note": "Extract only; date not shown; open-source speech-to-speech and voice-agent library"}
{"type": "jd", "grade": "B", "src": ["S25"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Scale AI", "title": "Machine Learning Engineer, Public Sector", "url": "https://job-boards.greenhouse.io/scaleai/jobs/4631848005", "job_id": "4631848005", "seen": "2026-11-13", "location": "Denver, CO; Honolulu, HI; Washington, DC", "remote": false, "seniority": "unspecified", "years": null, "degree": null, "must": ["Experience in computer vision, deep learning, reinforcement learning, or NLP in production settings", "Strong programming skills in Python; experience with TensorFlow or PyTorch"], "nice": null, "pay": {"lo": 196000, "hi": 245000, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "Pay is the DC/CO/HI band shown on an Accel mirror; the Greenhouse extract shows the SF, NY and Seattle band 240450-300300; listed 2026-11-05 on Fast AI Jobs; role builds automated evaluation pipelines for defence and intelligence customers"}
{"type": "jd", "grade": "B", "src": ["S25"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Scale AI", "title": "Staff Machine Learning Engineer, Public Sector", "url": "https://job-boards.greenhouse.io/scaleai/jobs/4654382005", "job_id": "4654382005", "seen": "2026-11-13", "location": "San Francisco; St. Louis; New York; Washington, DC", "remote": false, "seniority": "staff", "years": null, "degree": null, "must": ["The goal of a Staff Machine Learning Engineer at Scale is to lead the design and deployment of agentic AI systems that operate in real-world, mission-critical government environments", "Required-skill tags on refresh.cv mirror (not verbatim posting text): Python, PyTorch, ML systems engineering, retrieval systems, embeddings"], "nice": null, "pay": {"lo": 260400, "hi": 326600, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "DC band; mirror shows up to 362250 across locations; listed 2026-11-05"}
{"type": "jd", "grade": "A", "src": ["S21"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Glean", "title": "Machine Learning Engineer, Assistant Quality", "url": "https://job-boards.greenhouse.io/gleanwork/jobs/4711484005", "job_id": "4711484005", "seen": "2026-11-13", "location": "San Francisco, CA", "remote": false, "seniority": "unspecified", "years": 2, "degree": null, "must": ["2+ years of industry experience in machine learning, applied AI, or software engineering with significant ML ownership", "Strong hands-on coding ability and a track record of shipping production systems, not just prototypes or research projects", "Proficiency in common ML tooling and strong software engineering fundamentals in languages such as Python, Go, Java, or C++"], "nice": null, "pay": {"lo": 180000, "hi": 205000, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "Read in full; posted 2026-10-20 per jobsbyculture; hybrid 4 days a week; interview includes a brief AI-focused exercise or discussion; role covers LLM assistant quality, evaluation, retrieval (RAG), post-training and reinforcement learning, experimentation and the data infrastructure behind it; asks for a pragmatic, product-minded approach"}
{"type": "jd", "grade": "B", "src": ["S26"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Glean", "title": "Machine Learning Engineer, Enterprise Brain", "url": "https://job-boards.greenhouse.io/gleanwork/jobs/4632997005", "job_id": "4632997005", "seen": "2026-11-13", "location": null, "remote": null, "seniority": "unspecified", "years": 3, "degree": "BA/BS in computer science, math, sciences, or a related field", "must": ["3+ years of industry experience in AI or Machine Learning Engineering", "BA/BS in computer science, math, sciences, or a related field"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Extract only; responsibilities include reinforcement learning and fine-tuning approaches for agentic systems and scalable evaluation and benchmarking loops; location not captured"}
{"type": "jd", "grade": "B", "src": ["S26"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Glean", "title": "Machine Learning Engineer, LLM Evals and Observability (Bangalore; title inferred from Glean board listing)", "url": "https://job-boards.greenhouse.io/gleanwork/jobs/4712438005", "job_id": "4712438005", "seen": "2026-11-13", "location": "Bangalore, India (in person)", "remote": false, "seniority": "unspecified", "years": null, "degree": null, "must": [], "nice": ["Experience with LLM applications, evals, tracing, data warehouses, workflow orchestration, or ML infrastructure is a strong plus"], "pay": null, "ats": "Greenhouse", "note": "Requirement list not captured; skill tags taken from role text (evaluation pipelines, quality evalsets, LLM-powered judges, agent observability)"}
{"type": "jd", "grade": "B", "src": ["S26"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Glean", "title": "Software Engineer, Machine Learning (India)", "url": "https://boards.greenhouse.io/gleanwork/jobs/4012745005", "job_id": "4012745005", "seen": "2026-11-13", "location": "Bangalore, India", "remote": false, "seniority": "senior", "years": 6, "degree": "BA/BS in computer science, math, sciences, or a related degree", "must": ["6+ years of experience", "Experience working with search, recommendation, natural language processing, or other large systems involving machine learning"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Alias title; date not shown; Jobgether mirror adds domain adaptation of language models"}
{"type": "jd", "grade": "B", "src": ["S28"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Together AI", "title": "Machine Learning Engineer - Inference", "url": "https://job-boards.greenhouse.io/togetherai/jobs/4385540007", "job_id": "4385540007", "seen": "2026-11-13", "location": "San Francisco, CA (on-site)", "remote": false, "seniority": "unspecified", "years": 3, "degree": null, "must": ["Design and build the production systems that power the Together AI inference engine", "Knowledge of existing AI inference systems such as TGI, vLLM, TensorRT-LLM, Optimum (jobera requirements summary)"], "nice": null, "pay": {"lo": 160000, "hi": 230000, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "Listed 2026-11-02 on Fast AI Jobs; years from weekday mirror; mirror skill tags: Python, PyTorch, CUDA, Rust; serving-flavoured MLE"}
{"type": "jd", "grade": "B", "src": ["S29"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Lila Sciences", "title": "Senior / Staff Machine Learning Engineer, Applied AI", "url": "https://job-boards.greenhouse.io/lilasciences/jobs/4302917009", "job_id": "4302917009", "seen": "2026-11-13", "location": "Cambridge, MA; San Francisco, CA", "remote": false, "seniority": "senior", "years": null, "degree": null, "must": ["Strong experience building, training, adapting, or evaluating machine learning models", "Strong software engineering skills in Python and modern ML frameworks such as PyTorch, JAX, or TensorFlow"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Listed 2026-11-04 on Fast AI Jobs; role text names expertise in LLM training, evaluation and production-oriented ML systems"}
{"type": "jd", "grade": "B", "src": ["S29"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Lila Sciences", "title": "Machine Learning Engineer II / Senior Machine Learning Engineer I, Physical Sciences", "url": "https://job-boards.greenhouse.io/lilasciences/jobs/4116513009", "job_id": "4116513009", "seen": "2026-11-13", "location": "Cambridge, MA", "remote": false, "seniority": "unspecified", "years": null, "degree": null, "must": ["Strong Python software engineering fundamentals (testing, packaging, typing); experience with machine learning frameworks (e.g., PyTorch, Huggingface, etc.)"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Listed 2026-11-04 on Fast AI Jobs"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "voize", "title": "Senior ML Engineer - NLP (m/f/d)", "url": "https://jobs.ashbyhq.com/voize/f4939c9a-041c-4383-80e0-1072c8f48241", "job_id": "f4939c9a-041c-4383-80e0-1072c8f48241", "seen": "2026-11-13", "location": "Berlin, Germany", "remote": null, "seniority": "senior", "years": null, "degree": null, "must": ["Experience training, evaluating and shipping ML or NLP models to production, and explaining the decisions and results behind your work", "Experience building evaluations for ML or LLM systems and using error analysis and regression tests"], "nice": null, "pay": null, "ats": "Ashby", "note": "Ashby page not opened; text from Arbeitnow and choppingblock mirrors; posted 2026-11-06; pay not stated; four ML engineers hired through one process"}
{"type": "jd", "grade": "B", "src": ["S30"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "PhysicsX", "title": "Senior Machine Learning Engineer", "url": "https://job-boards.greenhouse.io/physicsx/jobs/4648881101", "job_id": "4648881101", "seen": "2026-11-13", "location": "London, United Kingdom", "remote": false, "seniority": "senior", "years": null, "degree": null, "must": ["Own the deployment of ML models and engineering surrogates (e.g., deep learning on CAE/CFD/FEA data, time-series forecasting, anomaly detection, optimization and control) to customer production environments", "Own the scoping of new projects and work-streams with existing customers"], "nice": null, "pay": null, "ats": "Greenhouse (EU board)", "note": "Date not shown"}
{"type": "jd", "grade": "B", "src": ["S30"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "PhysicsX", "title": "Machine Learning Software Engineer, Research", "url": "https://job-boards.greenhouse.io/physicsx/jobs/4652630101", "job_id": "4652630101", "seen": "2026-11-13", "location": "London, United Kingdom", "remote": false, "seniority": "junior", "years": null, "degree": null, "must": ["building machine learning models and pipelines in Python, using common libraries and frameworks (e.g., NumPy, SciPy, Pandas, PyTorch, JAX), especially including deep learning applications"], "nice": null, "pay": null, "ats": "Greenhouse (EU board)", "note": "Alias title; junior label from Built In mirror, which showed it 8 days after posting; date not shown; Built In summary mentions implementing distributed training"}
{"type": "jd", "grade": "B", "src": ["S30"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "PhysicsX", "title": "Machine Learning Engineer (Delivery)", "url": "https://job-boards.eu.greenhouse.io/physicsx/jobs/4880947101", "job_id": "4880947101", "seen": "2026-11-13", "location": "San Francisco Bay Area (hybrid)", "remote": false, "seniority": "unspecified", "years": null, "degree": null, "must": ["Experience applying Machine learning methods (including 3D graph/point cloud deep learning methods) to real-world engineering applications, with a focus on driving measurable impact in industry settings"], "nice": null, "pay": null, "ats": "Greenhouse (EU board)", "note": "Date not shown; works with data scientists, simulation engineers and customers"}
{"type": "jd", "grade": "A", "src": ["S23"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Netflix", "title": "Machine Learning Engineer (L4) - Infrastructure Algorithms and ML", "url": "https://jobs.lever.co/netflix/94c7b46a-4fcb-4b3b-8260-8d43baee85ec", "job_id": "94c7b46a-4fcb-4b3b-8260-8d43baee85ec", "seen": "2026-11-13", "location": "Los Gatos, California", "remote": false, "seniority": "mid", "years": null, "degree": null, "must": ["A strong coder with experience in Python and standard ML frameworks like PyTorch and TensorFlow", "Familiarity with operational tooling for ML services (monitoring, alerting, etc.), and services for model hosting/serving", "Able to communicate your ideas clearly and succinctly with the right amount of detail to audiences with varying technical backgrounds"], "nice": ["Experience with languages like Java or C++ is a plus", "Some experience in implementing and productionizing models in large scale industrial settings is a plus"], "pay": {"lo": 170000, "hi": 720000, "currency": "USD", "period": "year"}, "ats": "Lever", "note": "Read in full; salary-only compensation; posting date not shown"}
{"type": "jd", "grade": "B", "src": ["S31"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Roblox", "title": "Senior Machine Learning Engineer, Dynamic Economics", "url": "https://careers.roblox.com/jobs/7573319", "job_id": "7573319", "seen": "2026-11-13", "location": "San Mateo, CA", "remote": false, "seniority": "senior", "years": null, "degree": "BS, MS, or Ph.D. in Computer Science, Machine Learning, Statistics, or a related technical field, or equivalent practical experience building ML systems", "must": ["you will build models that power ranking, personalization, pricing, and optimization across Roblox's economic surfaces"], "nice": null, "pay": {"lo": 243290, "hi": 295250, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "Pay from refresh.cv mirror (shown 1 week after posting); careers-site ID 5819"}
{"type": "jd", "grade": "B", "src": ["S31"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Roblox", "title": "Senior/Principal Machine Learning Engineer, Safety AI Systems", "url": "https://careers.roblox.com/jobs/7347389", "job_id": "7347389", "seen": "2026-11-13", "location": null, "remote": null, "seniority": "principal", "years": 8, "degree": null, "must": ["8+ years of experience designing, developing, and operating large-scale, high-impact machine learning systems in a production environment"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Date not shown; multimodal generative AI for proactive moderation"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Waymo", "title": "Senior Staff Machine Learning Engineer, Simulation", "url": "https://jobera.com/job/waymo-senior-staff-machine-learning-engineer-simulation-7430495/", "job_id": "7430495", "seen": "2026-11-13", "location": "Mountain View, CA; San Francisco, CA; New York, NY", "remote": false, "seniority": "staff", "years": 7, "degree": "PhD in Computer Science, Machine Learning, Artificial Intelligence, or a related technical field, or equivalent practical experience", "must": ["7+ years of hands-on experience in developing and deploying machine learning applications", "Scale the development of machine learning-based metrics and eval datasets"], "nice": null, "pay": {"lo": 281000, "hi": 356000, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "Mirror page; employer page not reached; hybrid"}
{"type": "jd", "grade": "B", "src": ["S32"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Capital One", "title": "Senior Manager, Machine Learning Engineer", "url": "https://www.capitalonecareers.com/en/job/mclean/senior-manager-machine-learning-engineer/1732/101273104112", "job_id": "R1001222", "seen": "2026-11-13", "location": "McLean, VA; San Francisco, CA; New York, NY; San Jose, CA; Cambridge, MA", "remote": false, "seniority": "senior manager", "years": 5, "degree": "Bachelor's Degree or higher in Computer Science, Machine Learning or a related quantitative field", "must": ["Bachelor's Degree or higher in Computer Science, Machine Learning or a related quantitative field (Statistics, Economics, Operations Research, Analytics, Mathematics, Engineering)"], "nice": ["5+ years of experience optimizing ML algorithms, configurations, and infrastructure", "5+ years of experience working with Machine Learning techniques (Supervised, semi-supervised, and unsupervised, reinforcement learning, etc.)", "Ability to communicate complex technical and machine learning concepts clearly to a variety of audiences"], "pay": {"lo": 250800, "hi": 286200, "currency": "USD", "period": "year"}, "ats": null, "note": "Posted 2026-09-28; pay is the Machine Learning Engineer 5 band for New York, San Francisco and San Jose; employer will consider sponsoring"}
{"type": "jd", "grade": "C", "src": ["S32"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Capital One", "title": "Lead Machine Learning Engineer - ML/AI", "url": "https://builtin.com/job/lead-machine-learning-engineer-ml-ai/7372673", "job_id": null, "seen": "2026-11-13", "location": "Cambridge, MA; McLean, VA; New York, NY; Richmond, VA", "remote": false, "seniority": "lead", "years": 3, "degree": "Bachelor's degree", "must": ["Bachelor's degree", "At Least 3 years of experience deploying scalable software solutions on cloud platforms (e.g. AWS, Google Cloud, Azure, or equivalent private cloud)"], "nice": null, "pay": {"lo": 175800, "hi": 240800, "currency": "USD", "period": "year"}, "ats": null, "note": "Built In mirror, reposted 4 days before its crawl; location bands run from Richmond 175800-200700 to New York 211000-240800; responsibilities include model evaluation and experimentation, LLM inference, similarity search, guardrails, governance and observability"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Walmart Global Tech India", "title": "(IND) Senior Software Engineer / Senior ML Engineer", "url": "https://aijobs.ai/job/ind-senior-software-engineer-senior-ml-engineer", "job_id": null, "seen": "2026-11-13", "location": "Bengaluru, India", "remote": false, "seniority": "senior", "years": 6, "degree": null, "must": ["6+ years of experience in machine learning engineering, with a 2+ years focus on Generative AI and NLP", "Proficiency in Python, ML frameworks (PyTorch, TensorFlow), and NLP libraries like Hugging Face Transformers"], "nice": ["Experience with multi-modal models and advanced optimization techniques"], "pay": null, "ats": null, "note": "Mirror shown 2 weeks after posting; date unknown"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Walmart Global Tech India", "title": "Staff, Software Engineer (Machine Learning)", "url": "https://jobs.anitab.org/companies/walmart/jobs/88809024-staff-software-engineer-machine-learning", "job_id": null, "seen": "2026-11-13", "location": "Bengaluru, Karnataka, India", "remote": false, "seniority": "staff", "years": 8, "degree": null, "must": ["Skill: Machine Learning Engineer; Exp range: 8 - 13 years"], "nice": null, "pay": null, "ats": null, "note": "Alias title; posted 2026-08-05, eight days outside the window; mirror"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Flipkart", "title": "Machine Learning Engineer", "url": "https://www.gravityer.com/jobs/machine-learning-engineer-flipkart", "job_id": null, "seen": "2026-11-13", "location": "Bengaluru, India", "remote": false, "seniority": "mid", "years": 4, "degree": "Bachelors or Masters in computer science", "must": ["Solid understanding of machine learning models and related mathematics", "Typical background: Bachelors or Masters in computer science with 4+ years of experience working as a Software Engineer or Machine Learning Engineer in a product company"], "nice": ["Familiarity with data engineering technologies (Kafka/Flink/Spark etc)"], "pay": null, "ats": null, "note": "Mirror; undated"}
{"type": "jd", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Specbee", "title": "Sr Machine Learning Engineer", "url": "https://career.io/job/sr-machine-learning-engineer-bengaluru-specbee-e6d58d657d6b30c7562424da31432409", "job_id": null, "seen": "2026-11-13", "location": "Bengaluru, Karnataka, India", "remote": false, "seniority": "senior", "years": 6, "degree": null, "must": ["6+ years of experience in machine learning engineering or related roles", "Experience in deploying and managing ML and LLM models in production", "Deep understanding of supervised and unsupervised learning, deep learning, and NLP techniques, and large language models (LLMs)"], "nice": null, "pay": null, "ats": null, "note": "Mirror shown 12 days after posting; date unknown; responsibilities include scalability, reliability and efficiency of ML pipelines across cloud and on-prem"}
{"type": "jd", "grade": "B", "src": ["S29"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Lila Sciences", "title": "Principal, Machine Learning Engineer", "url": "https://job-boards.greenhouse.io/lilasciences/jobs/4222224009", "job_id": "4222224009", "seen": "2026-11-13", "location": "San Francisco, CA", "remote": false, "seniority": "principal", "years": 10, "degree": "Master's degree or higher in Computer Science, Machine Learning, or a related quantitative field (or Bachelor's with equivalent professional experience)", "must": ["10+ years of hands-on experience building and operating production ML systems at scale"], "nice": null, "pay": null, "ats": "Greenhouse", "note": "Date not shown; ML infrastructure for biological models; defines ML engineering standards"}
{"type": "jd", "grade": "B", "src": ["S42"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "McKinsey & Company (QuantumBlack Studio)", "title": "Machine Learning Engineer - QuantumBlack Studio", "url": "https://www.mckinsey.com/careers/search-jobs/jobs/machinelearningengineer-quantumblackstudio-112295", "job_id": "112295", "seen": "2026-11-13", "location": "Sao Paulo, Brazil", "remote": null, "seniority": "mid", "years": 3, "degree": "Bachelor's degree in a relevant field (e.g., Computer Science, Engineering, Business) or equivalent experience", "must": ["Bachelor's degree in a relevant field (e.g., Computer Science, Engineering, Business) or equivalent experience", "3+ years of experience in Machine Learning or AI engineering"], "nice": ["Experience working in client-facing roles is a strong advantage"], "pay": null, "ats": null, "note": "Employer careers page extract; date not shown; consultancy MLE working with engineering and data science teams on client delivery"}
{"type": "jd", "grade": "C", "src": ["S43"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Pinterest", "title": "Machine Learning Engineer, Core Engineering", "url": "https://www.career.com/job/pinterest/machine-learning-engineer-core-engineering/j202504022224148877458", "job_id": null, "seen": "2026-11-13", "location": "Palo Alto, CA", "remote": null, "seniority": "mid", "years": 2, "degree": "Bachelor's degree in computer science, machine learning, statistics, a related field or equivalent experience (Arc mirror); career.com copy reads Degree in computer science, machine learning, statistics, or related field", "must": ["2 years of industry experience applying machine learning methods (e.g., user modeling, personalization, recommender systems, search, ranking, natural language processing, reinforcement learning, and graph representation learning)", "End-to-end hands-on experience with building data processing pipelines, large scale machine learning systems, and big data technologies (e.g., Hadoop/Spark)"], "nice": ["M.S. or PhD in Machine Learning or related areas", "Publications at top ML conferences", "Expertise in scalable realtime systems that process stream data"], "pay": {"lo": 138905, "hi": 285982, "currency": "USD", "period": "year"}, "ats": null, "note": "career.com mirror shows posted 2026-05-31 and available before 2026-11-20 (live by its stated expiry); Pinterest's own site posts MLE levels L13-L16 in a manager posting"}
{"type": "jd", "grade": "C", "src": ["S43"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "Pinterest", "title": "Machine Learning Engineer, Monetization Engineering", "url": "https://pitchmeai.com/companies/pinterest/jobs/machine-learning-engineer-monetization-engineering-san-francisco-ca-us-palo-alto-ca-us-106478", "job_id": null, "seen": "2026-11-13", "location": "San Francisco, CA; Palo Alto, CA; Seattle, WA", "remote": null, "seniority": "unspecified", "years": null, "degree": "Bachelor's degree in computer science, machine learning, statistics, a related field or equivalent experience", "must": ["Bachelor's degree in computer science, machine learning, statistics, a related field or equivalent experience"], "nice": null, "pay": {"lo": 163418, "hi": 285982, "currency": "USD", "period": "year"}, "ats": "Greenhouse", "note": "PitchMeAI summary of Pinterest's Greenhouse listing, last confirmed open 2026-10-08; role builds deep learning and ML systems to personalise Pinterest and improve candidate retrieval for Ads; PitchMeAI rates ghost-job risk at Pinterest as high (160 stale of 190 open; median 66 days open; its own tracking since 2026-08-03; C)"}
{"type": "jd", "grade": "B", "src": ["S44"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "employer": "TikTok", "title": "Machine Learning Engineer Graduate (E-Commerce Recommendation Mall) - 2027 Start (PhD)", "url": "https://lifeattiktok.com/search/7672883737036654853", "job_id": "A241638B", "seen": "2026-11-13", "location": "Seattle, WA", "remote": false, "seniority": "entry (new graduate)", "years": null, "degree": "PhD degree in Computer Science, Electrical Engineering, Mathematics, Statistics or a related discipline (new-graduate programme)", "must": ["PhD degree in Computer Science, Electrical Engineering, Mathematics, Statistics or a related discipline", "Solid foundation in machine learning and deep learning"], "nice": ["Experience in recommendation systems, especially in live commerce, e-commerce, search, ads, or other large-scale consumer products", "Experience with generative recommendation, large recommendation models, retrieval"], "pay": null, "ats": null, "note": "Employer careers page extract; date not shown; new-graduate programme; a separate TikTok graduate posting (mirror, not sampled) lists solid knowledge of data structures and algorithms"}
```

```jsonl
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "ml_fundamentals", "n": 36, "source_kind": "jd-sample", "count": 36, "share": 1.0, "tier_hint": "Must", "note": "title-defined; not informative"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "python", "n": 36, "source_kind": "jd-sample", "count": 12, "share": 0.333, "tier_hint": "Must", "note": "lower bound: requirement text only partly captured for 32 of 36 postings"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "pytorch", "n": 36, "source_kind": "jd-sample", "count": 10, "share": 0.278, "tier_hint": "Must"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "deep_learning", "n": 36, "source_kind": "jd-sample", "count": 9, "share": 0.25, "tier_hint": "Important", "note": "KB tier is Must"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "llm_apis", "n": 36, "source_kind": "jd-sample", "count": 17, "share": 0.472, "tier_hint": "Must", "note": "any LLM, GenAI, agent, RAG or language-model fine-tuning mention; 13/22 at labs and AI-native, 4/14 elsewhere; Must for GenAI-targeted MLE"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "dsa", "n": 36, "source_kind": "jd-sample", "count": 0, "share": 0.0, "tier_hint": "Important", "note": "0 of 36 name it; one unsampled TikTok graduate posting (mirror) lists solid knowledge of data structures and algorithms; interview-driven"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "tensorflow_jax", "n": 36, "source_kind": "jd-sample", "count": 7, "share": 0.194, "tier_hint": "Should"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "experiment_design", "n": 36, "source_kind": "jd-sample", "count": 4, "share": 0.111, "tier_hint": "Should", "note": "Important in ranking and growth tracks"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "nlp", "n": 36, "source_kind": "jd-sample", "count": 6, "share": 0.167, "tier_hint": "Should"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "cpp", "n": 36, "source_kind": "jd-sample", "count": 2, "share": 0.056, "tier_hint": "Optional", "note": "Important for AV, robotics and kernel roles"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "communication", "n": 36, "source_kind": "jd-sample", "count": 5, "share": 0.139, "tier_hint": "Important", "note": "explicit communication or explaining language only"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "finetuning", "n": 36, "source_kind": "jd-sample", "count": 6, "share": 0.167, "tier_hint": "Should"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "evals", "n": 36, "source_kind": "jd-sample", "count": 11, "share": 0.306, "tier_hint": "Important", "note": "Must in the LLM-systems track"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "serving_literacy", "n": 36, "source_kind": "jd-sample", "count": 5, "share": 0.139, "tier_hint": "Should", "note": "Important on inference teams"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "embedding_models", "n": 36, "source_kind": "jd-sample", "count": 3, "share": 0.083, "tier_hint": "Should", "note": "retrieval, RAG or similarity search"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "data_pipelines", "n": 36, "source_kind": "jd-sample", "count": 5, "share": 0.139, "tier_hint": "Should"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "eval_stats", "n": 36, "source_kind": "jd-sample", "count": 0, "share": 0.0, "tier_hint": "Should", "note": "not named in captured text"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "adaptation_choice", "n": 36, "source_kind": "jd-sample", "count": null, "share": null, "tier_hint": "Important", "note": "not computed; PhysicsX post-training posting (not in sample) asks for evidence on training versus prompt or tool changes"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "c1_pragmatism", "n": 36, "source_kind": "jd-sample", "count": 2, "share": 0.056, "tier_hint": "Should", "note": "Anthropic and Glean wording"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "c2_tradeoffs", "n": 36, "source_kind": "jd-sample", "count": 1, "share": 0.028, "tier_hint": "Should", "note": "explaining decisions and results (voize)"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "c3_ownership", "n": 36, "source_kind": "jd-sample", "count": 10, "share": 0.278, "tier_hint": "Important", "note": "production deployment and ownership language"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "c4_responsible_ai", "n": 36, "source_kind": "jd-sample", "count": 1, "share": 0.028, "tier_hint": "Should", "note": "Important in safety and finance roles"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "new:post_training_rl", "n": 36, "source_kind": "jd-sample", "count": 4, "share": 0.111, "tier_hint": "Should", "note": "post-training, preference optimisation, reward modelling or RL as an LLM or agent training method"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "new:cloud_platforms", "n": 36, "source_kind": "jd-sample", "count": 2, "share": 0.056, "tier_hint": "Should"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "new:open_source_contributions", "n": 36, "source_kind": "jd-sample", "count": 2, "share": 0.056, "tier_hint": "Should", "note": "Must for open-source library roles"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "new:recsys_ranking", "n": 36, "source_kind": "jd-sample", "count": 5, "share": 0.139, "tier_hint": "Optional", "note": "track-specific: ranking, recommendation, ads"}
{"type": "skill_signal", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "skill": "new:distributed_training", "n": 36, "source_kind": "jd-sample", "count": 3, "share": 0.083, "tier_hint": "Optional"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "ml_fundamentals", "n": null, "source_kind": "platform", "share": 0.986, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "python", "n": null, "source_kind": "platform", "share": 0.713, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "pytorch", "n": null, "source_kind": "platform", "share": 0.482, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "llm_apis", "n": null, "source_kind": "platform", "share": 0.45, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "dsa", "n": null, "source_kind": "platform", "share": 0.337, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "deep_learning", "n": null, "source_kind": "platform", "share": 0.326, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "tensorflow_jax", "n": null, "source_kind": "platform", "share": 0.318, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "communication", "n": null, "source_kind": "platform", "share": 0.303, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "experiment_design", "n": null, "source_kind": "platform", "share": 0.235, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "nlp", "n": null, "source_kind": "platform", "share": 0.233, "note": "JobsPipe lexicon share; denominator not published"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "cpp", "n": null, "source_kind": "platform", "share": 0.233, "note": "JobsPipe lexicon share; denominator not published; inflated by AV, robotics and vision employers"}
{"type": "skill_signal", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "role": "ml-engineer", "skill": "finetuning", "n": null, "source_kind": "platform", "share": 0.13, "note": "JobsPipe lexicon share; denominator not published; value as listed in K11; shares matched on the page"}
{"type": "pay", "grade": "B", "src": ["S7"], "as_of": "2026-11-12", "ttl": "V3", "role": "ml-engineer", "location": "United States", "stat": "p25", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 200000, "n": null, "note": "title page; n not displayed; self-reported"}
{"type": "pay", "grade": "B", "src": ["S7"], "as_of": "2026-11-12", "ttl": "V3", "role": "ml-engineer", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 285650, "n": null, "note": null}
{"type": "pay", "grade": "B", "src": ["S7"], "as_of": "2026-11-12", "ttl": "V3", "role": "ml-engineer", "location": "United States", "stat": "p75", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 387000, "n": null, "note": null}
{"type": "pay", "grade": "B", "src": ["S7"], "as_of": "2026-11-12", "ttl": "V3", "role": "ml-engineer", "location": "United States", "stat": "p90", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 498000, "n": null, "note": null}
{"type": "pay", "grade": "B", "src": ["S3"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "live postings with pay (jurisdiction not stated; US-dominated)", "stat": "p25", "currency": "USD", "period": "year", "basis": "base", "source_name": "JobsPipe", "value": 183000, "n": 582, "note": "posted pay; component not stated, treated as base"}
{"type": "pay", "grade": "B", "src": ["S3"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "live postings with pay (jurisdiction not stated; US-dominated)", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "JobsPipe", "value": 224000, "n": 582, "note": null}
{"type": "pay", "grade": "B", "src": ["S3"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "live postings with pay (jurisdiction not stated; US-dominated)", "stat": "p75", "currency": "USD", "period": "year", "basis": "base", "source_name": "JobsPipe", "value": 268000, "n": 582, "note": null}
{"type": "pay", "grade": "B", "src": ["S4"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "live postings with pay (jurisdiction not stated; US-dominated)", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "JobsPipe AI Engineer (comparator)", "value": 181000, "n": 568, "note": "P25 144000; P75 215000; comparator for the AI Engineer premium probe"}
{"type": "pay", "grade": "B", "src": ["S6"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "AI startups", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "Fast AI Jobs", "value": 202500, "n": 61, "note": "range 128000-400000"}
{"type": "pay", "grade": "B", "src": ["S35"], "as_of": "2026-11-13", "ttl": "V4", "role": "ml-engineer", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "H-1B LCA via visa-bulletin.us", "value": 172900, "n": 53, "note": "offered wage on filings, FY2026 to date; IQR 150000-192941; filings are not evidence of pay"}
{"type": "pay", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "author sample of posted bands", "value": 246600, "n": 12, "note": "median of band midpoints; Netflix excluded for its 170000-720000 band; skewed to labs, AI-native and large consumer tech"}
{"type": "pay", "grade": "A", "src": ["S20"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "San Francisco, CA", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Anthropic posting (COI)", "lo": 340000, "hi": 560000, "level": "staff", "employer_type": "frontier-lab", "n": 1}
{"type": "pay", "grade": "A", "src": ["S21"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "San Francisco, CA", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Glean posting", "lo": 180000, "hi": 205000, "level": "mid", "employer_type": "ai-startup", "n": 1}
{"type": "pay", "grade": "B", "src": ["S31"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "San Mateo, CA", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Roblox posting via mirror", "lo": 243290, "hi": 295250, "level": "senior", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "B", "src": ["S32"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "New York, NY; San Francisco, CA; San Jose, CA", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Capital One posting", "lo": 250800, "hi": 286200, "level": "senior manager (MLE 5 band)", "employer_type": "enterprise", "n": 1}
{"type": "pay", "grade": "C", "src": ["S43"], "as_of": "2026-11-13", "ttl": "V1", "role": "ml-engineer", "location": "San Francisco Bay Area; Seattle", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Pinterest posting via mirror", "lo": 138905, "hi": 285982, "level": "mid", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "C", "src": ["S10"], "as_of": "2026-08-01", "ttl": "V3", "role": "ml-engineer", "location": "Bengaluru, India", "stat": "p50", "currency": "INR", "period": "year", "basis": "tc", "source_name": "Flexiple", "value": 1990000, "n": 422, "note": "labelled all-in; IQR 920000-3560000; P90 5770000"}
{"type": "pay", "grade": "C", "src": ["S11"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "Bengaluru, India", "stat": "p50", "currency": "INR", "period": "year", "basis": "tc", "source_name": "Hyring India Salary Model 2026", "value": 2110000, "n": null, "note": "modelled CTC estimate; P25 1430000; P75 3590000"}
{"type": "pay", "grade": "C", "src": ["S12"], "as_of": "2026-11-13", "ttl": "V3", "role": "ml-engineer", "location": "Bangalore, India", "stat": "p50", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Interview Query", "value": 61000, "n": 27, "note": "small sample"}
{"type": "pay", "grade": "B", "src": ["S9"], "as_of": "2026-07-18", "ttl": "V3", "role": "ml-engineer", "location": "Greater Bengaluru, India", "stat": "p50", "currency": "INR", "period": "year", "basis": "tc", "source_name": "Levels.fyi, all software engineer titles", "value": 5540248, "n": null, "note": "SWE family, not MLE; benchmark only"}
```

```jsonl
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "live_postings", "unit": "postings", "value": 2157, "region": "global", "method": "JobsPipe live index, 30+ sources"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "live_postings", "unit": "postings", "value": 1084, "region": "US", "method": "JobsPipe filter count"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "live_postings", "unit": "postings", "value": 90, "region": "India", "note": "4.2% of 2157; JD page shows 7.7% on a 2026-09-10 snapshot"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "live_postings", "unit": "postings", "value": 108, "region": "UK"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "live_postings", "unit": "postings", "value": 60, "region": "Canada"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "remote_flagged_postings", "unit": "postings", "value": 378, "region": "global", "note": "17.5% of 2157"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "seniority_cut_postings", "unit": "postings", "value": 814, "region": "global", "note": "Senior 814; Lead 359; Entry 240; cuts overlap"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "city_postings", "unit": "postings", "value": 187, "region": "San Francisco", "note": "New York 140; Seattle 92; Austin 34; Boston 21; Los Angeles 16; California 532"}
{"type": "measure", "grade": "B", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "open_roles_top_employer", "unit": "postings", "value": 148, "region": "global", "note": "TikTok; Waymo 53; Pinterest 33; Adobe 31; Apple 25; ByteDance 21; Capital One 20; Roblox 18"}
{"type": "measure", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_remote", "unit": "fraction", "value": 0.14, "region": "global"}
{"type": "measure", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_pay_disclosed", "unit": "fraction", "value": 0.385, "region": "global"}
{"type": "measure", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_seniority_label", "unit": "fraction", "value": 0.232, "region": "global", "note": "Senior 0.232; Entry 0.137; Mid 0.024; Lead or manager 0.092; unlabelled about 0.515"}
{"type": "measure", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_country", "unit": "fraction", "value": 0.503, "region": "US", "note": "India 0.077; UK 0.068; Singapore 0.059; Canada 0.036; Germany 0.031; France 0.024; Brazil 0.018"}
{"type": "measure", "grade": "B", "src": ["S2"], "as_of": "2026-09-10", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_employer_size_1000_plus", "unit": "fraction", "value": 0.389, "region": "global", "note": "201-1000: 0.092; 51-200: 0.030; 1-50: 0.022"}
{"type": "measure", "grade": "B", "src": ["S5"], "as_of": "2026-11-11", "ttl": "V1", "subject": "role:ml-engineer", "measure": "open_roles_ai_startups", "unit": "postings", "value": 298, "region": "global", "note": "171 AI startups; 39% at Pre-Seed to Series B; Series A 49, C 40, B 39, D 33, E 30"}
{"type": "measure", "grade": "M", "src": ["S5"], "as_of": "2026-11-11", "ttl": "V1", "subject": "role:ml-engineer", "measure": "share_non_mle_titles_in_role_listing", "unit": "fraction", "value": 0.24, "n": 50, "method": "12 of the 50 rows visible on the page; 5 further rows are internships or new-grad", "note": "CV, perception, MLOps, solutions architect and manager titles"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_genai_involved", "unit": "fraction", "value": 0.472, "n": 36, "note": "17/36; 13/22 at labs and AI-native, 4/14 elsewhere; plus or minus 16 points"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_no_genai_element", "unit": "fraction", "value": 0.528, "n": 36}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_degree_stated", "unit": "fraction", "value": 0.389, "n": 36, "note": "8 of 14 accept equivalent experience; 5/22 at labs and AI-native, 9/14 elsewhere"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "median_years_required", "unit": "years", "value": 5, "n": 17, "note": "minimum stated; range 2 to 10"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_certification_named", "unit": "fraction", "value": 0.0, "n": 36, "note": "lower bound; partial text"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_pay_disclosed_in_sample", "unit": "fraction", "value": 0.361, "n": 36}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_remote_in_sample", "unit": "fraction", "value": 0.056, "n": 36}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_entry_or_junior_in_sample", "unit": "fraction", "value": 0.056, "n": 36, "note": "TikTok new-graduate PhD programme; PhysicsX junior"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:ml-engineer", "measure": "share_exact_title_phrase", "unit": "fraction", "value": 0.861, "n": 36, "note": "Machine Learning Engineer appears in the title of 31 of 36; 5 are aliases"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 6, "n": 36, "note": "frontier-lab"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 16, "n": 36, "note": "ai-startup"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 7, "n": 36, "note": "big-tech"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 3, "n": 36, "note": "enterprise"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 2, "n": 36, "note": "gcc"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_employer_type", "unit": "postings", "value": 2, "n": 36, "note": "indian-employer"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_region", "unit": "postings", "value": 25, "n": 36, "region": "US"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_region", "unit": "postings", "value": 4, "n": 36, "region": "Europe"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_region", "unit": "postings", "value": 6, "n": 36, "region": "India"}
{"type": "measure", "grade": "M", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ml-engineer", "measure": "sample_postings_by_region", "unit": "postings", "value": 1, "n": 36, "region": "LatAm"}
{"type": "measure", "grade": "B", "src": ["S35"], "as_of": "2026-11-13", "ttl": "V4", "subject": "role:ml-engineer", "measure": "h1b_lca_filings_exact_title", "unit": "filings", "value": 53, "region": "US", "method": "DOL disclosure data via aggregator, FY2026 to date", "note": "28 employers; CA 25, WA 10, NY 7, MA 3, TX 3"}
{"type": "measure", "grade": "B", "src": ["S34"], "as_of": "2026-02-03", "ttl": "V5", "subject": "role:ml-engineer", "measure": "share_off_the_shelf_models_in_agent_case_studies", "unit": "fraction", "value": 0.7, "n": 20, "method": "interview case studies of deployed agents; survey n = 306", "note": "scope is agents, not all production applications"}
{"type": "loop", "grade": "C", "src": ["S37"], "as_of": "2026-11-13", "ttl": "V3", "employer": "Meta", "track": "classic-ml-system-design", "stages": ["recruiter screen", "technical phone screen", "onsite: two coding rounds", "system design", "ML design", "behavioural"], "formats": ["live coding", "ML design on ranking and recommendation"], "ai_policy": "some 2026 candidates report a 45-minute AI-enabled coding round", "take_home": null, "duration": null, "note": "Glassdoor report (2026-03) and prep guides; method unstated"}
{"type": "loop", "grade": "A", "src": ["S21"], "as_of": "2026-11-13", "ttl": "V3", "employer": "Glean", "track": "classic-ml-system-design", "stages": ["not published"], "formats": null, "ai_policy": "interview includes a brief AI-focused exercise or discussion; application asks which AI tools you use", "take_home": null, "duration": null, "note": "policy only; round content not published"}
{"type": "loop", "grade": "A", "src": ["S20"], "as_of": "2026-11-13", "ttl": "V3", "employer": "Anthropic", "track": "classic-ml-system-design", "stages": ["not published"], "formats": null, "ai_policy": "candidates confirm AI partnership guidelines; a 200-400 word why-Anthropic answer is valued", "take_home": null, "duration": null, "note": "COI; policy only"}
{"type": "loop", "grade": "C", "src": ["S37"], "as_of": "2026-11-13", "ttl": "V3", "employer": "OpenAI", "track": "classic-ml-system-design", "stages": ["screen", "assessment (live pair coding and/or take-home)", "onsite with ML system design"], "formats": null, "ai_policy": null, "take_home": true, "duration": null, "note": "prep-vendor guide"}
{"type": "loop", "grade": "C", "src": ["S37"], "as_of": "2026-11-13", "ttl": "V3", "employer": "Google", "track": "classic-ml-system-design", "stages": ["coding rounds", "ML system design", "ML depth", "Googleyness"], "formats": null, "ai_policy": null, "take_home": null, "duration": null, "note": "prep-vendor guide"}
{"type": "loop", "grade": "C", "src": ["S37", "S45"], "as_of": "2026-11-13", "ttl": "V3", "employer": "cross-employer", "track": "classic-ml-system-design", "stages": ["recruiter screen", "one or two coding or ML fundamentals rounds", "ML system design", "take-home or case study"], "formats": null, "ai_policy": "practitioner writing in own name says AI-tool use is part of the interview and take-homes resemble small product features", "take_home": true, "duration": "4-6 stages over 3-6 weeks", "note": "f1jobs and Dataford role guide; Bouchard (AI engineer hiring, C)"}
{"type": "practice", "grade": "A", "src": ["S22"], "as_of": "2026-11-13", "ttl": "V3", "area": "proof-of-work", "tactic": "Merged pull requests to ML or data libraries", "claim": "Open-source employers ask for a public track record that reviewers can read on GitHub", "evidence": "Hugging Face posting wording (read)", "verdict": "use", "risk": "only fits open-source and infrastructure roles"}
{"type": "practice", "grade": "B", "src": ["S21", "S25"], "as_of": "2026-11-13", "ttl": "V3", "area": "proof-of-work", "tactic": "Ship a system with real users and own it after launch", "claim": "Employers separate production ownership from prototypes", "evidence": "Glean posting (read); Scale AI posting via Accel mirror", "verdict": "use", "risk": "unmeasured effect on callbacks"}
{"type": "practice", "grade": "B", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V3", "area": "proof-of-work", "tactic": "Baseline-first model with error analysis and regression tests", "claim": "Employers ask for evaluations, error analysis and regression tests", "evidence": "voize posting via mirror", "verdict": "use-with-care", "risk": "one employer; serving benchmarks have no employer wording"}
{"type": "practice", "grade": "C", "src": ["S45"], "as_of": "2026-11-13", "ttl": "V3", "area": "proof-of-work", "tactic": "Ship, measure, defend: baseline, ground-truth test set, two approaches compared, error analysis and cost", "claim": "A practitioner who hires AI engineers says a fine-tune without a serious baseline, no baseline, imprecise technical claims and dead repositories are red flags", "evidence": "Bouchard, article updated 2026-08-28 (AI engineer role, not MLE; named practitioner)", "verdict": "use-with-care", "risk": "role differs from MLE; single author"}
{"type": "practice", "grade": "B", "src": ["S30"], "as_of": "2026-11-13", "ttl": "V3", "area": "proof-of-work", "tactic": "Compare prompting, tools and fine-tuning with cost and quality", "claim": "Employers want evidence for choosing training over prompt or tool changes", "evidence": "PhysicsX post-training posting", "verdict": "use-with-care", "risk": "single employer"}
{"type": "practice", "grade": "P", "src": ["S41"], "as_of": "2026-11-13", "ttl": "V3", "area": "resume", "tactic": "Evidence-line pattern: verb, system, metric from baseline to result, measured by offline eval or A/B test", "claim": "Quantified, measured lines match employers' emphasis on production and evaluation", "evidence": "pattern only; no measurement of effect", "verdict": "use-with-care", "risk": "do not invent figures"}
{"type": "practice", "grade": "B", "src": ["S13", "S14"], "as_of": "2026-11-13", "ttl": "V2", "area": "credentials", "tactic": "Skip the AWS ML Specialty; consider MLA-C02 only for AWS-heavy roles", "claim": "The Specialty is retired and MLA-C01 has ended in English", "evidence": "AWS pages and blog", "verdict": "avoid", "risk": "IT-services and GCC employers were not sampled"}
{"type": "credential", "grade": "B", "src": ["S13"], "as_of": "2026-03-31", "ttl": "V2", "id": "aws_mls_c01", "name": "AWS Certified Machine Learning - Specialty", "issuer": "Amazon Web Services", "level": "specialty", "state": "retired", "url": "https://aws.amazon.com/en/certification/certified-machine-learning-specialty", "exam_code": "MLS-C01", "retires": "2026-03-31", "jd_signal": {"value": 0, "unit": "postings naming it", "n": 36, "region": "US, Europe, India, LatAm", "method": "author sample, partial text"}}
{"type": "credential", "grade": "B", "src": ["S14"], "as_of": "2026-09-28", "ttl": "V2", "id": "aws_mla_c01", "name": "AWS Certified Machine Learning Engineer - Associate (MLA-C01)", "issuer": "Amazon Web Services", "level": "associate", "state": "retired", "url": "https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/", "exam_code": "MLA-C01", "retires": "2026-09-28", "note": "last English exam date; replaced by MLA-C02", "jd_signal": {"value": 0, "unit": "postings naming it", "n": 36, "region": "US, Europe, India, LatAm", "method": "author sample, partial text"}}
{"type": "credential", "grade": "B", "src": ["S14", "S15", "S19"], "as_of": "2026-09-01", "ttl": "V2", "id": "aws_mla_c02", "name": "AWS Certified Machine Learning Engineer - Associate (MLA-C02)", "issuer": "Amazon Web Services", "level": "associate", "state": "beta", "url": "https://aws.amazon.com/blogs/training-and-certification/updates-to-aws-certified-machine-learning-engineer-associate-mla-c02/", "exam_code": "MLA-C02", "launched": "2026-09-01", "note": "beta registration from 2026-09-01; covers GenAI, fine-tuning and RAG; standard availability early 2027 per third parties; fee not confirmed"}
{"type": "credential", "grade": "B", "src": ["S16", "S17"], "as_of": "2026-06-01", "ttl": "V2", "id": "gcp_pmle", "name": "Google Cloud Professional Machine Learning Engineer", "issuer": "Google Cloud", "level": "professional", "state": "active", "url": "https://cloud.google.com/certification/machine-learning-engineer", "fee": {"amount": 200, "currency": "USD"}, "duration_min": 120, "items": "50-60 questions", "validity_months": 24, "note": "validity 2 years per Google page extract; one third party says 3 years; exam guide dated 2026-06-01", "jd_signal": {"value": 0, "unit": "postings naming it", "n": 36, "region": "US, Europe, India, LatAm", "method": "author sample, partial text"}}
{"type": "credential", "grade": "B", "src": ["S18"], "as_of": "2026-11-13", "ttl": "V2", "id": "nvidia_ncp_genl", "name": "NVIDIA-Certified Professional: Generative AI LLMs", "issuer": "NVIDIA", "level": "professional", "state": "active", "url": "https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/", "exam_code": "NCP-GENL", "fee": {"amount": 200, "currency": "USD"}, "duration_min": 120, "validity_months": 24, "note": "some localised NVIDIA pages still show Coming soon", "jd_signal": {"value": 0, "unit": "postings naming it", "n": 36, "region": "US, Europe, India, LatAm", "method": "author sample, partial text"}}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Dated posting-count trend for MLE since 2025-01-01", "searched": "JobsPipe, Fast AI Jobs, general web search", "note": "snapshots only"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Employer-published MLE interview loop formats", "searched": "employer careers pages and posting text", "note": "only AI-use policies found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Named hiring-manager statements on proof of work written for the MLE role", "searched": "one general search plus one fetch", "note": "one named practitioner found (Bouchard), writing about AI engineers; other results were SEO blogs and were not used"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "2025+ published analysis of prior roles of MLEs with a stated method", "searched": "LinkedIn, Indeed and bootcamp analyses", "note": "only pre-2025 pieces and an unsourced 2026 blog"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Levels.fyi Bengaluru MLE page (K6)", "searched": "two targeted searches", "note": "page not retrieved"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Within-employer MLE versus AI Engineer pay pairs", "searched": "JobsPipe and JobsRadar", "note": "aggregate comparison only"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Big Tech MLE postings read from employer boards (Meta, Google, Amazon, Microsoft, Apple)", "searched": "search and fetch", "note": "not reached; Apple mirrors were outside the window; Netflix, Pinterest, Roblox, Waymo and TikTok were reached"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Consultancy and IT-services MLE postings beyond McKinsey (Accenture, Deloitte, TCS, Infosys)", "searched": "not searched", "note": "gap in employer-type coverage"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "India interview differences and India pay by employer type", "searched": "general web search", "note": "not found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Mistral AI MLE postings inside the window", "searched": "Lever page and mirrors", "note": "MLE and open-source-software MLE postings were closed or 6+ months old; forward-deployed ML engineer postings excluded as customer-facing"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "OpenAI employer pages", "searched": "fetch", "note": "blocked by bot detection; search extracts only"}
```
