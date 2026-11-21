---
id: roles.hub.ml-engineer
title: "Machine Learning Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "Machine Learning Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-49, T0-01, T0-02, T0-03, T0-06, T0-11, T0-14, T0-23]
roles: [ml-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Machine Learning Engineer

> Builds, trains, adapts and serves models: training pipelines, fine-tuning and inference, increasingly for LLM systems; much of the title is still classic ML such as recommendation, ads and vision.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| ML Engineering & Applied Science | L4 Post-training and adaptation; also L2 Foundation models and research, L3 Inference and ML platforms; planes: Evaluation and quality | Established (E) | #2 of 24 | #1 of 24 · band S · Monte Carlo rank 1 (P10–P90 1–2) | B1 Engineer |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 9 (8–9.5) | B | JobsPipe 2,157 global / 1,084 US / 108 UK / 90 India (re-checked 2026-11-13; static refresh caveat); Fast AI Jobs 298 at AI startups (2026-11-12, up from 227); Axial H1 2026 US 13,776 (~490/wk, C); FY2025 DOL exact-title LCAs 1,053–1,071 [T0-24, T0-27, T0-49, T0-70]. |
| Pay | 8.5 (7.5–9) | B | Levels.fyi US ML Engineer TC P25 $200K / P50 $286,958 / P75 $389,850 / P90 $497,500 (n=1,027, 2026-11-11; 1.44x US SWE); Axial posted base ceilings $180K–$300K (senior $241K, n=13,776); Meta E5 $472–497K / E6 $660–790K, Amazon L6 $401K; FY2025 LCA floor $179,982 (n=3,745) [T0-44, T0-49]. |
| Durability | 7 (5.5–8.5) | D | Judgement. Broad ML engineering spans recommendation, ranking, forecasting and LLM training/serving; API-first adoption shifts routine application work toward AI Engineer while leaving model-training, fine-tuning and scale optimisation intact [T0-49]. |
| Leverage | 7.5 (6.5–8.5) | D | Judgement. Owns revenue-adjacent models behind ranking, recsys, pricing, ads and risk (OpenAI paid marketing, Roblox pricing/ranking, Pinterest/TikTok ads, Capital One risk [T0-49:L305]). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 7 (6–7.5) | B | JobsPipe India 90 live of 2,157 global (4.2% live vs 7.7% JD-page share, 4–8% range; static 2026-11-13 check); heavy GCC and big-tech presence in Bengaluru and Hyderabad [T0-49, T0-69]. |
| India pay | 8 (6.75–8.5) | B | Levels.fyi Greater Bengaluru ML Engineer TC (2026-11-12, n=97): P25 Rs30.3L / P50 Rs44.4L–Rs44.7L / P75 Rs65.7L / P90 Rs80.7L (down from Oct Rs94.6L); India ML/AI-focus SWE P50 Rs28.7L; Flexiple Bengaluru CTC P50 Rs19.9L (n=422, C) [T0-45]. |

India rank (CCI with India inputs): #2 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 5.5 | ◐ 7 | ○ 3.5 | ○ 1.5 | ◐ 7 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** ML fundamentals, Python (production), PyTorch, Deep learning & transformers.
- **Important (headline):** LLM APIs & tool calling, Data structures & algorithms, TensorFlow / JAX, Experiment design & A/B testing, C++, Fine-tuning (SFT, LoRA), LLM evaluation (golden sets, calibrated judges, CI gates), Serving literacy (vLLM, batching, quantisation), Embedding & reranker models, Data pipelines & quality, Eval statistics (CIs, power, pass^k).
- **Full inventory:** 85 skills (Must 4 · Important 18 · Should 28 · Optional 34 · Avoid 1), each with its evidence and posting keywords: [ml-engineer.md](../../03-skills-and-tech/inventories/ml-engineer.md).
- **Prerequisites:** Degree common (72% in Axial Search [C · T0-06]; 75% of 903 Glassdoor US postings mention a degree [C · T0-23]; nearly 25% in Atlanta Fed Lightcast data list none [A · T0-23]). JD labels: entry 13.7%, senior 23.2%. DS → MLE 6–18 months; PhD → applied roles ~8 months [D · T0-06]
- **Credentials (tie-breakers, not skills):** Google Cloud Professional Machine Learning Engineer (PMLE) (Optional: tie-breaker in GCP shops; refreshed for GenAI); AWS Certified Machine Learning Engineer – Associate (MLA-C01) (Avoid: retired in English 2026-09-28; replaced by AWS MLA-C02); NVIDIA-Certified Professional: Generative AI LLMs (NCP-GENL) (Optional: announced (verify live Certiverse booking before prep); LLM training/serving roles only); AWS Certified Machine Learning – Specialty (Avoid: retired 2026-03-31); AWS Certified ML Engineer – Associate (MLA-C02) (Optional: replaces MLA-C01; beta, GA 2027-01-14; adds GenAI and agentic workloads); PyTorch Certified Associate (PTCA) (Optional: Linux Foundation PyTorch Certified Associate ($250, 15-17h prep pathway); optional PyTorch baseline (T0-32:L499)); Databricks Certified Machine Learning Associate (Optional: $200, 48 Q, 90 min, 2-yr validity; associate baseline for Databricks ML shops (T3-01)); Databricks Certified Machine Learning Professional (Optional: $200, 59 Q, 120 min, 2-yr validity; hardest Databricks ML exam for production ML/MLOps shops (T3-01)); NVIDIA-Certified Associate: Generative AI LLMs (NCA-GENL) (Optional: $125 associate exam; cheap structured LLM syllabus only, low senior hiring lift (T0-11, T0-32:L489)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A baseline-first model with measured lift and error analysis; a prompt vs RAG vs fine-tune comparison with cost and quality; a serving benchmark (tokens/s, p95, $/M tokens); small-budget training evidence (FSDP2 smoke tests, MFU)
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P4 Prompt vs RAG vs fine-tune comparison](../../05-portfolio/project-archetypes.md#p4) (76%); [P8 Paper re-implementation with rigorous evals and a write-up](../../05-portfolio/project-archetypes.md#p8) (47%); [P3 Eval harness with a calibrated judge and statistics](../../05-portfolio/project-archetypes.md#p3) (32%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Classic ML system design.** It tests ML depth and breadth, coding (including ML-from-scratch or AI-assisted coding at AI-native firms), behavioural and leadership rounds, plus at most one classic ML system design round (recommendation, ranking, fraud or ETA; absent in some Microsoft loops). Source: T0-14, T0-46, T0-49, T0-52, T1-03.
- **Practise:** the [classic ml system design prep pack](../../08-interviewing/prep-packs.md#classic-ml-system-design-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** B1 Engineer (ML & Applied Science); headline pattern: "Machine Learning Engineer: LLM fine-tuning, evaluation, serving". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** machine learning (98.6%), Python (71.3%), PyTorch (48.2%), LLM (45.0%), data structures (33.7%), deep learning (32.6%), TensorFlow (31.8%), A/B testing (23.5%), NLP (23.3%), C++ (23.3%)
- **Leave out or reframe:** Fine-tuning as the default answer (70%, 14/20 interviewed production agent teams in arXiv 2512.04123v2 used off-the-shelf models, B · T0-03); dormant torchtune workflows; tools you have only read about
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ml-engineer).

## Specialisations inside this role

- **Fine-tuning and domain adaptation** (L4 Post-training and adaptation): No title of its own in the catalog.
- **Synthetic data** (L4 Post-training and adaptation): No title of its own in the catalog.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Applied Scientist](applied-scientist.md) (0.49); [Research Scientist (AI/ML)](research-scientist.md) (0.32); [Research Engineer / Member of Technical Staff](research-engineer.md) (0.31).
- **Same family (ML Engineering & Applied Science):** [Applied Scientist](applied-scientist.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ml-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ml-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (JobsPipe 2026-11-13; Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

Machine Learning Engineer is a two-track role, not a pure LLM fine-tuning job. In both JobsPipe's corpus (45.0% naming LLM, counted 2026-09-10) and the November 2026 dossier sample (17 of 36 postings, 47.2%, ±16 percentage points), **roughly half of MLE postings have no generative-AI component at all** (53% in the sample) [B/M · T0-49 L63, L358]. The split tracks employer type sharply: **59% (13/22)** of sampled postings at frontier labs and AI-native firms involve LLMs or GenAI, compared with **29% (4/14)** across consumer tech, enterprises, GCCs, and Indian product companies [M · T0-49 L63, L358].

Across the 36 sampled postings (as of 2026-11-13), the work falls into three operating families [B/M · T0-49 L127–L130, L311–L319]:

| MLE operating family | Representative employers in sample | Core deliverables and stack footprint |
|---|---|---|
| **LLM-systems MLE** | Anthropic (Virtual Collaborator RL), Glean (Assistant Quality, Enterprise Brain, LLM Evals), OpenAI (API Multicloud, Implicit Signals), Lila Sciences, voize | Evaluation pipelines and LLM-as-judge systems (**31%**, 11/36), post-training / SFT / RL (**22%**, 8/36 — fine-tuning 17%, RL/post-training 11%), retrieval/RAG (8%), and production quality ownership [A/B/M · T0-49 L64, L128, L313–L316] |
| **Classic-ML MLE** | Roblox (Dynamic Economics, Safety AI), Pinterest (Core, Monetization), TikTok (E-Commerce Recs), OpenAI (Growth), Waymo (Simulation), PhysicsX (CAE/CFD surrogates), Capital One | Ranking, recommendation, pricing, ads, fraud/risk, simulation, and physics surrogates; experiment design, feature pipelines, and offline-to-online model ownership (**53%**, 19/36 non-GenAI) [A/B/M · T0-49 L129, L317] |
| **Platform and open-source MLE** | Hugging Face (Transformers/voice-agent libraries), Together AI (inference engine), Netflix (Infrastructure Algorithms & ML) | Maintainable Python/PyTorch libraries, distributed training, serving and inference optimisation (**14%**, 5/36), operational monitoring and alerting [A/B/M · T0-49 L130, L315, L506, L514, L521] |

**Correcting the "70% off-the-shelf" durability caveat.** Phase 0 records summarised a study as showing that "70% of production apps" use off-the-shelf models without fine-tuning. Verification against the primary preprint (*Measuring Agents in Production*, arXiv:2512.04123; live-verified 2026-11-19) confirms the 70% figure covers **20 interviewed production agent deployments** (from a survey of n = 306), not all production ML applications [B · T0-49 L73, L301, L382]. Fine-tuning remains a minority task (13.0% on JobsPipe; 16.7% in the sample), while evaluation (31%) and post-launch production ownership (28%) are the most frequently cited non-framework signals [B/M · T0-49 L64, L205–L206, L214]. Likewise, JobsPipe's 23.3% C++ share is inflated by autonomous-vehicle, robotics, and vision employers; C++ appeared in only 2 of 36 (5.6%) sampled postings [B/M · T0-49 L64, L203].

**Mid-level versus senior and staff scope.** Mid-level postings (2–4 years, e.g., Glean Assistant Quality, Netflix L4, Pinterest Core) centre on building, evaluating, and shipping models into production services [A/B/C · T0-49 L510, L521, L533]. Senior, Staff, and Principal postings (5–10+ years, e.g., Anthropic Staff, Waymo Senior Staff, Lila Sciences Principal, Roblox Principal) own cross-system ML standards, reward modelling and open-ended evaluation frameworks, large-scale data quality pipelines, and ambiguous architecture trade-offs across research and product [A/B/C · T0-49 L291, L500, L523–L524, L531].

## Employer landscape and title confusion

**Volume is anchored by large consumer tech and autonomy employers, not frontier labs.** On JobsPipe (retrieved 2026-11-13), live global volume is 2,157 (US 1,084; UK 108; India 90; Canada 60; California 532), with 38.9% at 1,000+ employee firms and top hiring volume at **TikTok (148), Waymo (53), Pinterest (33), Adobe (31), Apple (25), ByteDance (21), Capital One (20), and Roblox (18)** [B · T0-49 L61, L144–L151, L155]. On Fast AI Jobs (updated 2026-11-11), AI startups list **298 roles at 171 startups** (up from 273 at 159 in October 2026; 39% Pre-Seed to Series B) [B · T0-49 L61, L152, L378].

**Title aliases and screening traps:**
- **Exact title dominates (86% / 31 of 36),** but five regional and company-specific aliases recur in postings: `Software Engineer, Machine Learning` (Glean India), `Staff, Software Engineer (Machine Learning)` and `Senior Software Engineer / Senior ML Engineer` (Walmart Global Tech India), `Machine Learning Software Engineer, Research` (PhysicsX), `Data Scientist (MLE)` (Walmart India), `AI/ML Engineer` (Sanmina India), and `Machine Learning Systems Engineer` (Anthropic) [B/M · T0-49 L132–L137]. The label `GenAI MLE` was not observed in any sampled posting [M · T0-49 L377].
- **Wide scope under one title:** OpenAI's "Machine Learning Engineer" postings span classic paid-marketing growth optimisation, multimodal perception, Statsig experimentation, and multi-cloud AWS post-training [B · T0-49 L344, L502–L505]. Capital One's "Senior Manager, Machine Learning Engineer" carries an individual-contributor band label (`MLE 5`) [B · T0-49 L344, L525].
- **Aggregator noise and stale requisitions:** Of the 50 visible Fast AI Jobs "ML Engineer" rows, **24% (12/50)** are non-MLE titles (computer vision, perception, MLOps, solutions architect, manager) and **10% (5/50)** are internships or new-graduate roles [M · T0-49 L62, L138]. Greenhouse and Lever boards re-post old requisition IDs, graduate "2026 Start" mirrors remain indexed after closing, and PitchMeAI flags high stale-listing counts on Pinterest (160 stale of 190 open, median 66 days; attributed aggregator claim, Grade C) [C · T0-49 L345, L430–L432].
- **Adjacent boundaries:** Exclude `Forward Deployed Machine Learning Engineer` (Mistral — customer-facing delivery), pure MLOps/platform, Research Scientist (publication-led), and [AI Engineer](ai-engineer.md) (application-layer API/RAG/agent work without model training or ranking ownership) [B · T0-49 L131, L182].

## Career path, India demand and market signals

**Prerequisites and realistic routes.** Across 17 sampled postings stating minimum years, the median ask is **5 years** (range 2–10; senior roles typically ask 5–8+) [M · T0-49 L68, L291]. Explicit entry-level openings are rare outside structured graduate pipelines: only **2 of 36** sampled postings were entry/junior (TikTok 2027 PhD new-graduate programme and PhysicsX junior role), and JobsPipe's 13.7% entry label (240 listings) concentrates heavily in new-grad, PhD, and recruiter programmes [B/M · T0-49 L68, L292]. A degree was stated in **39% (14/36)** of captured text — and 8 of those 14 accept equivalent experience — with labs and AI-native firms stating a degree far less often (5/22, 23%) than enterprises and consumer tech (9/14, 64%) [M · T0-49 L69, L290]. Realistic entry routes evidenced in postings are backend/product software engineering, quantitative data science, and PhD research into lab roles; frontend, SRE, PM, and non-technical routes are not evidenced in MLE postings [B/M · T0-49 L293].

**Ladders and progression.** Observed ladders include Netflix L4/L5, Pinterest L13–L16 (reporting to Manager II), Capital One MLE → Lead → Senior Lead → Senior Manager (`MLE 5`), and Senior → Staff → Principal at Roblox, Waymo, Lila Sciences, and Anthropic [A/B/C · T0-49 L298]. Common exits are Research/Applied Scientist, ML Platform/Inference Engineer, Forward Deployed ML, and ML Engineering Management [B · T0-49 L299].

**Pay nuance and the AI Engineer premium.** Full pay distributions are owned by [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). Key November 2026 role-specific signals:
- **US total compensation and posted base:** Levels.fyi US MLE median TC reached **$285,650** on 2026-11-12 (P25 $200K, P75 $387K, P90 $498K; n not displayed) [B · T0-49 L65, L226]. On JobsPipe's posted-pay dataset, MLE median posted pay is **$224K** (IQR $183K–$268K, n = 582) versus **$181K** for AI Engineer (n = 568) — a **+$43K (+24%)** aggregate premium, though confounded by employer mix [B/M · T0-49 L65–L66, L227–L228]. Fast AI Jobs startup median posted base is **$202,500** (n = 61, range $128K–$400K) [B · T0-49 L229].
- **Wide level and employer spreads in posted base:** Sample US bands run from **$160K–$245K** at mid-level (Together AI, Glean, Scale AI DC) and **$243K–$295K** at senior (Roblox, Capital One `MLE 5`) up to **$260K–$356K** at Staff/Senior Staff (Scale AI, Waymo) and **$340K–$560K** at frontier labs (Anthropic Staff COI; OpenAI Core Experimentation Seattle $437K–$485K); Netflix posts a single salary-only L4 band of **$170K–$720K** [A/B/C · T0-49 L233–L237]. Meta's Phase 0 E6 figure ($782K) remains unresolved against a Meta Levels.fyi extract showing E6 at $660K (highest reported $789.8K) [B · T0-49 L239]. Watch for location-scoped Levels.fyi pages (a Miami page labelled "United States" prints $145K) [T0-49 L428].
- **Sponsorship (US):** Exact-title FY2026 H-1B LCAs number 53 across 28 employers (Meta 6, Apple 6, Block 5; median offered wage $172,900 — a regulatory floor, not pay; exact-title counts understate sponsorship because titles vary); Anthropic and Capital One state sponsorship availability in postings [A/B · T0-49 L65, L104–L106, L327–L332]. See [visa and relocation](../../11-tracks/visa-and-relocation.md).

**India demand, pay split, and hiring bar.** JobsPipe's India figures are internally inconsistent across snapshots — **90 live India roles** on 2026-11-13 is **4.2%** of 2,157 global listings, whereas JobsPipe's 2026-09-10 JD snapshot reports **7.7%** — so treat India's share as **4–8%** [B/M · T0-49 L67, L350, L380]. Sampled and observed India employers include Walmart Global Tech India, Glean (Bengaluru), Flipkart, Specbee, Chargebee, Skild AI, Cerebras, and Sanmina [B/C · T0-49 L351]. Every India posting in the sample (6 of 6) stated explicit experience floors: 4+ years at Flipkart, 6+ at Glean India, Specbee, and Walmart Senior, and 8–13 years at Walmart Staff [B/C · T0-49 L353]. **India pay splits cleanly into two populations:** broad Bengaluru market samples centre near **₹20L** (Flexiple median **₹19.9L**, n = 422, IQR ₹9.2L–₹35.6L, P90 ₹57.7L, Aug 2026; Hyring model ₹21.1L) [C · T0-49 L67, L245–L246], roughly half of Phase 0's Levels.fyi Bengaluru MLE median of ₹44.5L (which could not be re-opened in T0-49; Interview Query n = 27 reports $61K) [C · T0-49 L247, L381].

**Credentials status (as of November 2026).** Zero of 36 sampled postings named any certification [M · T0-49 L70, L286]. AWS ML Specialty (MLS-C01) retired on 2026-03-31, and **AWS MLA-C01 took its last English exam on 2026-09-28**, replaced by **MLA-C02 (beta)** (registration opened 2026-09-01; adds GenAI, Bedrock, RAG, and agentic workloads; live-verified 2026-11-19) [B · T0-49 L70, L280–L282]. Google Cloud PMLE ($200, 2 hours, guide 2026-06-01; 2-year vs 3-year validity conflict) and NVIDIA NCP-GENL ($200, 120 minutes, 2-year validity) are active [B · T0-49 L283–L284]. See [credential ROI](../../04-certifications/credential-roi.md).

## Interview themes and preparation notes

No employer-published full MLE loop specification was found; loop structure rests on Grade C candidate reports and prep guides (4–6 rounds over 3–6 weeks across coding, ML fundamentals, ML system design, and behavioural) [C · T0-49 L71, L254–L263]:

- **Classic ML system design remains the anchor at Big Tech:** Meta and Google reports centre on ranking, recommendation, and large-scale ML architecture alongside live coding; some 2026 Meta candidates also report a 45-minute AI-enabled coding round [C · T0-49 L256, L260]. Note that the Phase 0 track extension "plus where an LLM would help" had no direct loop evidence in T0-49 [T0-49 L263].
- **AI-tool exercises and written policies at AI-native firms and labs:** Glean's posting explicitly states that its interview includes a brief AI-focused exercise or discussion and asks on the application which AI tools you use [A · T0-49 L257]. Anthropic requires confirming AI partnership guidelines and highlights a 200–400 word "Why Anthropic?" response (COI) [A · T0-49 L258]. OpenAI reports combine live pair coding and/or a take-home with ML system design [C · T0-49 L259].
- **What moves the needle in screening and proof of work:** Employer postings explicitly ask for **public merged pull requests** to ML/data libraries (Hugging Face — which also embeds a "GPU-poor and proud" reading check in its application!), **shipped production systems owned after launch** rather than prototypes (Glean, Scale AI mirror), **error analysis and regression tests** (voize), and **evidence-based adaptation decisions** proving why fine-tuning/training beats prompting or tool changes (PhysicsX) [A/B/C · T0-49 L72, L267–L273, L338]. Common rejection red flags include fine-tuning without a serious baseline, listing unread tools, dead repositories, and ignoring application instructions [C · T0-49 L272, L338]. Use the [classic ML system design prep pack](../../08-interviewing/prep-packs.md#classic-ml-system-design-pack) (no model answers).

## Dossier evidence and limits

- **Primary dossier:** [T0-49](../../../research/sessions/T0-49-role-dossier-ml-engineer.md) (retrieved 2026-11-13; 46 sources: 10 Read, 36 Extract-only; 36 JD records across US 25, India 6, Europe 4, LatAm 1) [T0-49 L44, L55, L161–L171].
- **Sampling and text-depth limits:** Only **4 of 36** postings were read in full (`Anthropic`, `Hugging Face`, `Glean`, `Netflix`); 32 rest on partial extracts or mirrors, so sample skill shares are **strict lower bounds** with ±16 percentage points error and cannot overturn platform tiers alone [M · T0-49 L55, L171, L190]. The sample over-represents frontier labs and AI-native firms (22/36) relative to hiring volume and missed direct employer boards at **Meta, Google, Amazon, Microsoft, and Apple**, as well as IT-services firms and consultancies beyond McKinsey [T0-49 L55, L75, L403–L404].
- **Known absences and COI:** No dated posting-count trend since 2025-01-01; no Levels.fyi Bengaluru MLE re-verification; no within-employer MLE-versus-AI-Engineer pay pairs; no India interview-loop evidence; OpenAI career pages blocked automated fetches [T0-49 L394–L410]. One posting (`S20`, Anthropic Staff MLE) is flagged COI because the dossier was authored by Claude Sonnet 5.5 (Anthropic) [T0-49 L13, L469]. Seven secondary ledger rows (`S19`, `S36`, `S37`, `S38`, `S40`, etc.) did not retain individual URLs [T0-49 L468–L489].
- **What would change this view:** Direct Big Tech board reads (Google, Meta, Amazon, Microsoft, Apple) and IT-services/GCC sampling to test the GenAI share and certification screening; opening the Levels.fyi Bengaluru MLE page; and full-text reads across all 36+ postings [T0-49 L83, L414–L420].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
