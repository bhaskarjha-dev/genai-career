---
id: roles.hub.ai-evaluation-engineer
title: "AI Evaluation Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "AI Evaluation Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-60]
roles: [ai-evaluation-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# AI Evaluation Engineer

> Designs evaluation harnesses, golden sets, LLM-judge calibration, regression gates and online monitoring.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Evaluation, Safety & Security | Evaluation and quality (plane); also L5 Orchestration and context, L4 Post-training and adaptation | Watch (W) | #15 of 24 | #15 of 24 · band B · Monte Carlo rank 13 (P10–P90 8–16) | A1 Builder |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 4 (3–5.5) | B | No platform title count yet, but T0-60 documented 22 named postings across frontier labs (5), Big Tech (Microsoft >=4), eval vendors/scale-ups (7) and enterprise/services [T0-60]. |
| Pay | 7 (5.5–9) | B | Bimodal US posted base bands: Microsoft AI IC4–IC5 $119.8K–$274.8K (NYC/SF to $304.2K, A), Scale AI $179.4K–$270K (B), Transluce $310K–$500K (B) and frontier labs above $300K base + equity [T0-60]. |
| Durability | 6.5 (5–8) | D | Judgement. Adoption gap (52.4% offline / 37.3% online evals among agent teams [T0-03 KF4]) and shift toward benchmark-saturation and agent evaluation [T0-60 K6] vs risk that evals stay a skill inside AI Engineer. |
| Leverage | 7.5 (6.5–8.5) | D | Judgement. Release-gating and model-quality ownership (Anthropic, Microsoft and Backbase evaluation teams [T0-60]). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4 (3–5) | B | Expanded beyond Backbase alone: 5 verified India postings (Glean, LogicMonitor, GlobalLogic Bengaluru; Backbase, HCLTech Hyderabad) plus 5 mirrored listings [T0-60]. |
| India pay | 5.5 (4–7) | C | One startup posted band Rs12–36L (Ressl AI founding role, B) plus C-grade adjacent AI/LLM engineer benchmarks [T0-60]. |

India rank (CCI with India inputs): #14 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 7 | ● 8 | ◐ 6.5 | ○ 3 | ● 7.5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), LLM evaluation (golden sets, calibrated judges, CI gates), Testing (pytest), LLM APIs & tool calling.
- **Important (headline):** Eval statistics (CIs, power, pass^k), Error analysis, Experiment design & A/B testing, Retrieval quality (hybrid, reranking, recall@k), Benchmark construction, Git & CI/CD, Human evaluation programmes, Rubrics & inter-rater agreement.
- **Full inventory:** 65 skills (Must 7 · Important 17 · Should 28 · Optional 13), each with its evidence and posting keywords: [ai-evaluation-engineer.md](../../03-skills-and-tech/inventories/ai-evaluation-engineer.md).
- **Prerequisites:** Lead with 3+ years software/backend or data-science engineering (0/22 entry-level and 0/22 PhD required in T0-60); PhDs add measurement rigour [C · T0-60]
- **Credentials (tie-breakers, not skills):** AWS Certified Generative AI Developer – Professional (AIP-C01) (Optional: weak signal; services channels only); LangChain Certified Agent Engineer (LCAE) (Optional: Open-access $99 (1 free resit), 40 MCQ in 120 min (pass 28/40), Talview proctored, 24-mo validity; hiring signal unmeasured (T0-29:L76)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** An eval harness with a kappa-calibrated judge validated on 100+ human labels, plus position and verbosity bias tests; a CI regression threshold and a cost–quality frontier chart
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P3 Eval harness with a calibrated judge and statistics](../../05-portfolio/project-archetypes.md#p3) (79%); [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (64%); [P4 Prompt vs RAG vs fine-tune comparison](../../05-portfolio/project-archetypes.md#p4) (36%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Evaluation design.** It tests golden sets, judge calibration, online sampling, A/B tests, plus 2–4 hour eval-harness take-homes and eval-system or eval-data design rounds (practitioner guides, C). Source: T0-14, T0-46, T0-60, T1-03.
- **Practise:** the [evaluation design prep pack](../../08-interviewing/prep-packs.md#evaluation-design-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** A1 Builder (Applied GenAI Engineering); headline pattern: "AI Engineer: LLM systems, RAG, agents, evaluation". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** LLM evaluation, evals, benchmarking, LLM-as-a-judge, golden dataset, A/B testing, pytest
- **Leave out or reframe:** Eval-platform brand lock-in (7 acquisitions/closures in 13 months; OpenAI hosted Evals shutdown 2026-11-30); storing master API keys in SaaS eval platforms; 'accuracy' claims without CIs
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ai-evaluation-engineer).

## Specialisations inside this role

- **Benchmark design and model evaluation** (Evaluation and quality): Alias of AI Evaluation Engineer in the A–Z index (also 27% floor in AI PM [T0-59] and 75% in Responsible AI Engineer [T0-61]).
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Applied AI Engineer](applied-ai-engineer.md) (0.27); [AI Engineer](ai-engineer.md) (0.26); [Machine Learning Engineer](ml-engineer.md) (0.24).
- **Same family (Evaluation, Safety & Security):** [AI Security Engineer / AI Red Teamer](ai-security-engineer.md), [Responsible AI / AI Governance Engineer](responsible-ai-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ai-evaluation-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ai-evaluation-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

Across T0-60's extended November 2026 sample (n = 22 postings: 18 first-pass base plus 4 supplementary — Transluce, Braintrust, Scale AI and Vals AI), AI Evaluation Engineer splits into **three distinct operating models** [A/B/M · T0-60 L68, L121–L122, L194]:

- **Applied and product evaluation engineering (majority of non-lab roles):** building production evaluation pipelines, golden reference datasets, LLM-as-a-judge graders calibrated against domain-expert labels, CI regression thresholds, online quality alerting and agent-trajectory observability (Microsoft Copilot and Health, Glean, LogicMonitor, Backbase, Harper, Sema4.ai, Judi Health, Geisinger, HCLTech, GlobalLogic) [A/B · T0-60 L68, L194, L568–L581].
- **Frontier-lab model evaluation (7/22, 32%; base 4/18):** building benchmark suites, monitoring live post-training runs and designing evaluations that resist superficial benchmark gaming (Anthropic Post-Training Evals and Evals Infrastructure, Cohere North Modelling, Mistral, xAI, Scale AI, Vals AI) [A/B/M · T0-60 L68, L136, L203, L564–L567, L584–L585].
- **Third-party and non-profit evaluators:** research-engineer-style teams building model-behaviour evaluations under government or frontier contracts — for example, Transluce's AI Behavior Engineer executing harmful-manipulation evaluations with the EU AI Office, alongside METR's evaluation-execution staff [B · T0-60 L68, L194, L582].

**Skills reality (base n = 18; lower bounds from mostly excerpted text; ±23–25 pp Wilson intervals — cross-check only).** In visible text, LLM-as-a-judge design (8/18, 44%; 8/13 non-lab), golden datasets (7/18, 39%), online monitoring and observability (7/18, 39%) and agent evaluations (6/18, 33%) lead, followed by CI regression gates (4/18), experiment design (4/18), named evaluation frameworks (4/18: LangSmith, Braintrust, DeepEval, Ragas, OpenAI Evals, LM Eval Harness), LLM tracing/OpenTelemetry (3/18) and human evaluation (3/18) [M · T0-60 L70, L144–L166, L660–L661]. By contrast, three scorecard Musts appear rarely verbatim: `pytest` (0/18; test design 1/18), explicit `statistics` (1/18, Anthropic nice-to-have only) and explicit `llm_apis` (1/18, though implied by agent evals), while Python appears in 4/18 overall and 3/3 A-read postings that state languages [M · T0-60 L70, L148–L159]. Note that Ragas still appears in two sampled postings (LogicMonitor, Ressl AI mirror); while T0-60 did not re-test Ragas maintenance directly, [ERRATA U37](../../../research/ERRATA.md) and [skills radar](../../03-skills-and-tech/skills-radar.md) lifted Phase 0's dormancy warning on 2026-11-13 after the `v0.4.4rc1` release [A · T0-69 L50, U37].

**Proof and credentials.** Zero of 18 base postings name any certification (AWS AIP-C01 was not re-checked) [M · T0-60 L79, L198, L395]. Employers explicitly ask for judge calibration aligned with human experts (LogicMonitor, Microsoft Health), a real regression caught by an eval suite (Harper), open-source evaluation-framework contributions (Mistral: LM Eval Harness, OpenAI Evals) and reusable open-source reference patterns (Braintrust) [B · T0-60 L197, L567, L572, L577, L583].

## Employer landscape and title confusion

| Employer group in T0-60 sample (n = 22) | Count | Sampled organisations | Grade |
|---|---|---|---|
| AI-native, scale-ups and eval vendors | 7/22 | Glean, LogicMonitor, Sema4.ai, Harper, Braintrust, Scale AI, Vals AI | B · T0-60 L122 |
| Frontier labs | 5/22 | Anthropic (×2), Cohere, Mistral AI, xAI (plus OpenAI eval roles cited in C commentary) | A/B/C · T0-60 L122, L138 |
| Big Tech | 3/22 | Microsoft AI and Microsoft Copilot (≥4 dated eval-focused postings Aug–Sep 2026) | A/B · T0-60 L68, L122, L137 |
| Enterprise, health, IT services, non-profit and contract | 7/22 | Backbase, Judi Health, Geisinger; HCLTech, GlobalLogic; Transluce; Dice healthcare contract | A/B · T0-60 L122 |

**Title fragmentation and absorption risk.** Across 22 postings, T0-60 observed more than 15 distinct titles — including `Software Engineer, Evals`, `Sr. Evaluation Engineer`, `Staff Engineer, AI Evals`, `Principal SWE for Copilot Evals`, `Principal Applied Scientist (LLM evals)`, `Senior MTS, AI Quality`, `AI Behavior Engineer`, `Eval Engineer`, `Evaluations Engineer`, `MTS, North Modelling (Evals)` and generic titles masking eval work (`Senior Technical Lead` at HCLTech) [A/B · T0-60 L195, L386, L564–L585]. At the same time, T0-60 excluded five postings where evaluations appeared merely as one bullet inside a broader AI Engineer or management role; whether dedicated eval titles persist or get absorbed into [AI Engineer](ai-engineer.md) remains unresolved without a title-level time series [D/M · T0-60 L61, L126, L391, L450].

**Posting-quality and mirror traps.** Backbase's Hyderabad Principal AI Evaluation Engineer requisition (first seen 2025-12-12) was still live more than 11 months later on 2026-11-13 and asked only for "familiarity" with agent-eval methods despite its Principal title [A · T0-60 L81, L203, L573]. Anthropic job ID 5198255008 changed both title and posted pay from USD 320K–485K (April 2026 mirrors) to USD 500K–850K (November 2026 live board, COI), and Scale AI's Applied AI Evals Engineer band conflicted across two mirrors (USD 216K–270K vs USD 179.4K–224.25K, filled by April 2026) [A/B · T0-60 L81, L172–L175, L564, L584].

## Career path, India demand and market signals

**Seniority gate and feeders (revising K12).** Dedicated evaluation engineering is **not an entry-level corridor**: **0 of 22 postings** are entry-level, and **12 of 22 (55%) are senior, staff, principal or lead** (7 principal/staff/lead, 5 senior), with mid/unspecified roles typically asking 3–7+ years of software engineering (Harper, Sema4.ai, Microsoft, Glean) [M · T0-60 L68, L124, L134, L199]. Software and backend engineers dominate over data scientists, and **PhD is required in 0 of 22 postings** [B/M · T0-60 L199, L396]. Data scientists appear in enterprise/health eval roles (Geisinger, Microsoft preferred), DevOps/SRE observability skills appear at GlobalLogic, Glean and Backbase, and regulated-domain expertise is preferred at Microsoft Health [B · T0-60 L199]. Candidates with under 3 years of experience generally enter through general AI engineering roles where evals is one duty [B/M · T0-60 L86]. Progression runs through IC4–IC5 ladders (Microsoft), Staff/Principal IC tracks (7/22) and management (`Evals Infrastructure Tech Lead / Manager` at Anthropic) [A/B · T0-60 L200].

**Demand signals, viral claims and bimodal pay.** No platform publishes a dedicated title count or 2025–2026 trend for AI Evaluation Engineer [E · T0-60 L140, L429]. Keyword aggregates provide rough context only (not title counts): ZeroG Talent shows 116 open "AI agent evaluation" positions (undated, C) and Fast AI Jobs shows 85 LLM/GenAI roles across 28 startups (2026-06-16, B) [B/C · T0-60 L68, L139]. Treat two widely repeated claims as untraceable (Grade E): "~500–800 evals roles in India" and "8% of postings mention evaluation skills", and ignore a contradictory aggregator claim of "56% remote-friendly" on a page with zero openings (sample remote share is 11%, 2/18 base) [D/E/M · T0-60 L135, L141–L142, L469–L470]. T0-60 replaced Phase 0's "no pay data" placeholder (reflected in the scorecard above) with **bimodal US posted base bands** (equity extra): Big Tech and applied scale-ups span USD 119.8K–274.8K at Microsoft AI (IC4–IC5; NYC/SF up to USD 304.2K, A) and USD 179.4K–270K at Scale AI (conflicting mirrors, B), whereas third-party evaluator Transluce posts USD 310K–500K (B) and Anthropic Post-Training Model Evaluations posts USD 500K–850K (A, COI) [A/B · T0-60 L69, L170–L178]. Full pay benchmarks live in [pay benchmarks](../../09-compensation/pay-benchmarks.md#pay-by-genai-role-what-the-corpus-measures).

**India demand and pay.** India volume is broader than the single Backbase role previously logged: **5 of 22 sampled postings** are in India (Bangalore 3: Glean Evals & Observability, LogicMonitor, GlobalLogic; Hyderabad 2: Backbase, HCLTech) plus 5 additional mirrored India listings (Cellular Vehicles, Brillio, BambooBox, Ressl AI, InRhythm), spanning IT services, product companies and startups asking for 4–15 years of experience [A/B · T0-60 L75, L204, L571–L575]. Posted India pay remains scarce: one startup listing states INR 12–36 lakh (Ressl AI founding role, B), alongside C-grade adjacent AI/LLM engineer benchmarks [B/C · T0-60 L69, L179–L180].

## Interview themes and preparation notes

Employer-authored interview documentation for evaluation roles is thin: Anthropic's posting specifies only its 200–400-word "Why Anthropic?" prompt and candidate AI-guidance confirmation without listing round structure [A, COI · T0-60 L186, L769]. One employer-agnostic practitioner guide (C, unclear authorship) matches the scorecard's evaluation-design track [C · T0-60 L80, L187, L392, L773]:

- **Reported loop pattern (C):** recruiter screen probing eval experience → technical phone screen combining Python coding and "design an eval" → 2–4 hour take-home building a small evaluation harness (typically LLM grading) → virtual onsite of two coding rounds, one eval-system design round, one eval-data design round and one behavioural round (3–5 weeks overall) [C · T0-60 L187, L773].

**Preparation rules (no model answers; see [interview loops](../../08-interviewing/interview-loops.md) and the [evaluation design prep pack](../../08-interviewing/prep-packs.md#evaluation-design-pack)):**
- **Anchor your portfolio in calibrated measurement, not bare accuracy.** Publish one working harness (using Promptfoo, Braintrust, LangSmith, DeepEval, Inspect or LM Eval Harness) that reports judge-versus-human agreement statistics, position and verbosity bias checks, a CI regression threshold and an error taxonomy [B/P · T0-60 L86, L202, L778–L779].
- **Bring one concrete regression story.** Employers explicitly probe for a real failure or regression your evaluation suite caught before production release [B · T0-60 L197, L779].

## Dossier evidence and limits

- **Low full-read rate (critical caveat):** Across T0-60 as a whole, only **7 of 70 ledger sources (10%)** were read in full; inside the evaluation subset, only **3 of 22 postings** were opened in full on employer pages (Anthropic, Microsoft AI, Backbase), while 18 came from ATS excerpts or aggregator mirrors (Grade B) and 1 (xAI) was downgraded to Grade C from a "similar jobs" sidebar [T0-60 L48, L67, L121, L580].
- **Lower-bound shares, freshness and COI:** Because 15 of the 18 skill-share postings were truncated excerpts, every skill percentage is a lower bound with ±23–25 percentage point Wilson intervals and serves only as a directional cross-check [T0-60 L48, L445]. Only 10 of 22 postings are verified live or dated within 90 days (3 older, 9 undated) [T0-60 L67, L125]. Anthropic sources carry model-author COI, and vendor blogs marketing "evals engineering" (S43) were excluded from reliance [T0-60 L13, L453, L468].
- **Key absences:** Platform title-level counts and 2025–2026 trends, Levels.fyi eval-engineer pay pages, US LCA counts, employer-specific eval interview loops, AWS AIP-C01 exam verification, and India GCC or services pay bands [T0-60 L429–L438].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
