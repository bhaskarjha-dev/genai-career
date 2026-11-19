---
id: roles.hub.applied-scientist
title: "Applied Scientist: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "Applied Scientist on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-52]
roles: [applied-scientist]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Applied Scientist

> Research-to-production scientist at large technology firms: modelling, experimentation and shipping models.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| ML Engineering & Applied Science | L4 Post-training and adaptation; also L2 Foundation models and research; planes: Evaluation and quality | Verified (V) | #3 of 24 | #5 of 24 · band A · Monte Carlo rank 5 (P10–P90 3–7) | B2 Scientist |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 6.5 (5.5–8) | B | Amazon Science listed 451 Applied Science category openings on 2026-11-13 (central estimate ~270 literally AS-titled, Wilson range 141–375); Fast AI Jobs 23 AI-startup roles (confirming Big Tech concentration); active hiring at Microsoft, Uber, Zalando, Mistral [T0-52, T0-70]. |
| Pay | 7.75 (6.75–8.75) | B | Levels.fyi Amazon Applied Scientist US TC (2026-08-18): L4 $245K, L5 $324K, L6 $407K, L7 $653K (median $306K–$335K); corroborated by Microsoft/Uber posted US bands [T0-44, T0-52]. |
| Durability | 7.5 (6–9) | C | Amazon retained 451 Applied Science openings on 2026-11-13 despite corporate headcount reductions across Oct 2025–Jul 2026; subject to Big Tech employer-cycle risk [T0-52]. |
| Leverage | 7.5 (6.5–8.5) | D | Judgement. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 5 (4–6.5) | B | Amazon Science listed 90 India science roles (14% of 642 global) on 2026-11-13; verified postings across Amazon India and Microsoft IDC (Hyderabad/Bengaluru) [T0-52]. |
| India pay | 7.5 (6–9) | D | Proxy: Google MLE Bengaluru L4 Rs65.2L, L5 Rs168.3L (small n) [T0-02:254]. |

India rank (CCI with India inputs): #3 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ○ 3 | ◐ 4.5 | ○ 2 | ○ 1 | ● 8 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** ML fundamentals, Python (production), PyTorch, Experiment design & A/B testing, Data structures & algorithms, Research-to-production.
- **Important (headline):** SQL, LLM APIs & tool calling, Eval statistics (CIs, power, pass^k), Fine-tuning (SFT, LoRA), Causal inference, Research methods & re-implementation, Deep learning & transformers.
- **Full inventory:** 64 skills (Must 7 · Important 16 · Should 25 · Optional 16), each with its evidence and posting keywords: [applied-scientist.md](../../03-skills-and-tech/inventories/applied-scientist.md).
- **Prerequisites:** Amazon US uses PhD or Master's+4 (7/9), while Microsoft (BS+2/MS+1), Uber (BS+3–4/MS+2), Zalando (MS+2) and Mistral offer broader routes; coding/DSA is the usual gap for PhDs [A/C · T0-52]
- **Credentials (tie-breakers, not skills):** PyTorch Certified Associate (PTCA) (Optional: ). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** Your own method turned into a service with tests and CI; at least three code reviews via OSS PRs; an eval-statistics write-up
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P4 Prompt vs RAG vs fine-tune comparison](../../05-portfolio/project-archetypes.md#p4) (56%); [P8 Paper re-implementation with rigorous evals and a write-up](../../05-portfolio/project-archetypes.md#p8) (47%); [P3 Eval harness with a calibrated judge and statistics](../../05-portfolio/project-archetypes.md#p3) (31%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Classic ML system design.** It tests recommendation, fraud or ETA system design, plus where an LLM would help. Source: T1-03, T0-14 (first collected in the role catalog §8.2; this file is the owner).
- **Practise:** the [classic ml system design prep pack](../../08-interviewing/prep-packs.md#classic-ml-system-design-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** B2 Scientist (ML & Applied Science); headline pattern: "Applied Scientist: LLM evaluation, experimentation, research to production". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** applied scientist, machine learning, statistics, experimentation, A/B testing, LLM, PyTorch
- **Leave out or reframe:** A publication list uncoupled from shipped production impact (publications/patents appear in 11/23 JDs, so pair them with production code); claims of 'state of the art' without baselines
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-applied-scientist).

## Specialisations inside this role

- **Fine-tuning and domain adaptation** (L4 Post-training and adaptation): No title of its own in the catalog.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Machine Learning Engineer](ml-engineer.md) (0.49); [Research Scientist (AI/ML)](research-scientist.md) (0.30); [Research Engineer / Member of Technical Staff](research-engineer.md) (0.29).
- **Same family (ML Engineering & Applied Science):** [Machine Learning Engineer](ml-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-applied-scientist): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-applied-scientist): narrative skills, tools, interview and typical gaps.
- [PhD to industry](../../11-tracks/phd-to-industry.md): the track playbook for this role.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

In technology-employer postings as of November 2026, an Applied Scientist builds, evaluates and ships models or measurement systems directly into production products — writing production code is core, not optional [A · T0-52 L131]. T0-52's sample of 23 read postings (16 full requirement text, 7 Amazon Science description-only) revises the scorecard's L4-primary work footprint: **application and deployment is the primary layer in 74% (17/23)**, orchestration and context in 13% (3/23), models and research in 9% (2/23), and post-training in only 4% (1/23) — although fine-tuning or post-training is named anywhere in 26% (6/23; 95% CI 13%–46%) and evaluation or quality work in 43% (10/23) [M · T0-52 L77, L90, L368–L378].

Four distinct role variants sit under the same title; tailor your positioning to one before applying [A/B · T0-52 L77, L96, L133–L139]:

| Variant | Sampled employers | Core work and stack | Grade |
|---|---|---|---|
| Big Tech applied ML (search, ads, recommenders, forecasting, vision, Alexa/AGI) | Amazon, Microsoft, Zalando | Production ML models, online A/B tests, Python, PhD or Master's + years | A · T0-52 L135 |
| Measurement and causal science | Uber AS II, Amazon FAIM and Detail Page, Zalando marketing | SQL, Python, experimental design and econometrics; Uber's marketing-measurement AS II names no ML at all | A · T0-52 L85, L136, L755 |
| LLM post-training and agentic systems | Hippocratic AI, Zalando Agentic AI, Amazon KDP Bengaluru | PyTorch, SFT/RLHF/RLVR (50B+ parameters at Hippocratic AI), RAG, agent orchestration and LLM evaluation | A/B · T0-52 L137, L753, L756–L757 |
| Customer-facing research engineering and domain-applied startup ML | Mistral AI, Amazon GenAI Innovation Center; startup listings (KoBold Metals, PhysicsX, Moloco, Garner Health) | Large-cluster pre/post-training plus client delivery (Mistral, no degree required); domain simulation, ads or healthcare delivery | A/B · T0-52 L138–L139, L766 |

**Skills reality (n = 16 full-text; ±20 pp Wilson intervals — cross-check only).** ML fundamentals (94%, 15/16), Python (88%, 14/16) and **production deployment (`research_to_prod`, 75%, 12/16; 78% of n = 23)** dominate [M · T0-52 L80, L224–L236]. LLM/GenAI appears in 69% (11/16, skewed by tech/GenAI sampling versus 4.5% LLMs in InterviewStack's all-keyword set of 3,146 postings) [M/C · T0-52 L80, L235]. Research methods (63%), publications or patents (44%; 48% of n = 23), LLM evaluation (44%), PyTorch (44%), statistics (44%, matching InterviewStack's 44.6% "Statistics & Experimentation" category), deep learning (44%) and experiment design (38%) sit next, while SQL (25%, below the scorecard's 63.8% platform share), DSA (19% in postings, though tested across loops), ablations (6%) and explicit eval-statistics terms (0%) appear less often verbatim [M/C · T0-52 L80, L222–L255].

**Proof and credentials.** Zero of 23 read postings name any certification [M · T0-52 L88, L319]. Employers ask for shipped models with offline-to-online A/B evidence (Microsoft, Uber, Amazon), top-venue publications or patents (11/23 read postings, including Amazon basic qualifications), and large-codebase tests and CI at Mistral [A/B · T0-52 L88–L89, L310–L314]. **Revision to scorecard K14:** do not omit publications — pair them with shipped production impact, because Amazon and Zalando list publications or patents as qualifications [A/C · T0-52 L103, L449]. Conversely, the scorecard's specific "at least three OSS code reviews" and "eval-statistics write-up" have no supporting source in T0-52 [C · T0-52 L315, L448].

## Employer landscape and title confusion

**Amazon anchors the verified market.** On 2026-11-13, Amazon Science listed **642 open science roles** globally (607 full-time, 35 internships), of which **451 sat in the Applied Science category** (central estimate ~270 literally AS-titled, Wilson range 141–375 based on 6 of 10 on page 7), far ahead of Data Science (75), Research Science (66) and Economics (25) [A/M · T0-52 L78, L131, L165–L167, L610–L617]. Note two Amazon board mechanics: Amazon runs two requisition ID series (legacy 2.7M–3.0M, which may be stale, and newer 10.5M+) and posts "multiple positions" `AMZ` requisitions with lower experience minimums (likely for sponsored hires) [A · T0-52 L105, L490, L492].

**Startups, Europe and frontier labs.** Fast AI Jobs tracked **23 Applied Scientist roles at 15 AI startups** on 2026-10-28 (39% at Pre-Seed to Series B), up 64% from 14 at 12 startups in June 2026 [B/M · T0-52 L78, L169–L174]. Zalando surfaced at least 14 AS-titled postings in Germany (snippet-level records downgraded to Grade B) [B · T0-52 L78, L176]. OpenAI, Anthropic, Cohere and Google DeepMind do not use the title; Mistral AI is the lone frontier-class exception [A/B/E · T0-52 L67, L153, L468]. The legacy "~700" count in earlier records remains untraced, and JobsPipe has no Applied Scientist role page [B/E · T0-52 L70, L177, L438].

**Title confusion and keyword noise.** Generic board searches for "Applied Scientist" are heavily polluted: in InterviewStack's 3,146-posting all-keyword analysis (May 2026, vendor COI), **38% sit in healthcare, education, biotech or pharma** (top employers: a university, a life-sciences company and a hospital group) [C · T0-52 L77, L140, L417]. Even inside tech, scope and family vary sharply: Uber places Applied Scientist in its Data Science family; Zalando's unlevelled "Applied Scientist" can require a PhD + 4 years and multi-area roadmap ownership (principal scope); Microsoft's "Data & Applied Scientist" in Hyderabad can be pure analytics (SQL, Kusto, Power BI) [A · T0-52 L85, L215, L357, L491]. Aliases observed outside the sample include `Applied Scientist / Research Engineer` and `AI Scientist` (Mistral), `Applied Research Scientist` (Meta, ServiceNow), `Associate Applied Scientist` and `Applied Scientist III` (Garner Health), `Applied AI Scientist`, and `Scientist I–III` (Amazon India listings); `Applied Scientist (GenAI)` was not seen [C · T0-52 L152–L159, L437].

## Career path, India demand and market signals

**Entry routes and the Amazon-specific PhD corridor.** Among 19 sampled postings stating a degree rule, **only 1 of 19 requires a PhD alone** (Zalando search, which still accepts equivalent experience) [M · T0-52 L79, L323–L335]. The "PhD corridor" is specifically Amazon's no-experience path: 7 of 9 Amazon postings with a stated rule ask for "PhD, or Master's + 4 years" (one asks Master's + 2; one `AMZ` offered-position requisition accepts Master's + 1 or Bachelor's + 5) [A/B/M · T0-52 L79, L327–L335]. Non-PhD routes are wider elsewhere:
- **Master's with <4 years:** Microsoft AS II (Master's + 1), Zalando (Master's + 2), Uber (Master's + 2), Amazon AS I [A · T0-52 L99, L328, L345].
- **Bachelor's with industry ML/data experience:** Microsoft AS II (Bachelor's + 2), Uber (Bachelor's + 3–4), Mistral (no degree required) [A/B · T0-52 L100, L328–L331].
- **No direct route observed** for frontend, DevOps/SRE, product management or non-technical backgrounds without ML modelling proof (ML modelling is named in 22 of 23 read postings) [D/M · T0-52 L346]. Actual PhD share among hires is unmeasured [E · T0-52 L336, L463].

**Ladders, level-aware pay pointers and durability.** Amazon runs AS I (L4) → AS II (L5) → Senior (L6) → Principal (L7), with manager exit via Applied Science Manager; Microsoft AS II sits at IC3 and Senior AS at L63; Zalando runs AS → Senior → Principal → Senior Principal; Uber runs AS II → Sr [A/B/C · T0-52 L85, L350–L356]. Crucially, Levels.fyi's levelling comparison aligns **Amazon L6 with Google L5 and Meta E5** (and Amazon L5 with Google L4 / Meta E4), so the scorecard's ML Engineer proxy fits senior AS pay and overstates mid-level L5 [B/M · T0-52 L81, L287, L357]. T0-52 captures AS-specific US data: Levels.fyi Amazon AS (updated 2026-08-18) shows mean total compensation L4 $245K, L5 $324K, L6 $407K, L7 $653K (all-level median $335K in header vs $306K in the same page's FAQ; base flat at $164K–$173K across L4–L7, so stock drives progression), corroborated by Amazon posted US bases ($136K–$223.4K) and FY2024 AS II LCA filings (mean $171,690, n = 312 — filings, not pay); Microsoft US IC3 base posts $102.1K–$202.2K (Bay Area/NYC $133.8K–$219.2K) and Uber NYC AS II $161K–$179K [A/B · T0-52 L81–L82, L261–L289]. Zero of 8 European and zero of 6 Indian postings state pay [A/B · T0-52 L82, L284]. See [pay benchmarks](../../09-compensation/pay-benchmarks.md#the-level-ladder) for the canonical benchmark tables. On durability, Amazon maintained 451 Applied Science openings on 2026-11-13 despite ~14,000 corporate cuts in October 2025, ~16,000 in January 2026 and July 2026 cuts in its AGI organisation (confirmed 2026-07-22 as a strategic refocus; verified 2026-11-19); sources conflict on whether 2025 cuts were AI-attributed [A/B/C · T0-52 L86, L359–L363]. Remote roles are scarce (1 of 33 postings, Ukraine-only, vs 9.9% all-keyword); Microsoft AI mandates ≥4 office days/week from 2026-01-26, Uber ≥50%, Hippocratic AI 5 days, while Zalando offers hybrid ≥60% remote [A/B/C · T0-52 L87, L389–L393].

**India demand and sponsorship.** Amazon Science listed **90 India science roles** (14% of 642 global) on 2026-11-13; India represents 3.9% (123/3,146) of the all-keyword market [A/C · T0-52 L83, L426]. Amazon India (4 Bengaluru postings, same PhD or Master's + 4 template) and Microsoft IDC (Hyderabad Bachelor's + 2 / Master's + 1; Bengaluru Master's/PhD + 3–6 years) supply all six India postings in T0-52 [A · T0-52 L83, L427–L428]. Other large India employers often use alternate titles: Walmart Global Tech India posted 15 comparable roles as "Data Scientist", and Amazon India roles also surface as "Scientist I–III" on portals [B · T0-52 L83, L427]. No 2025–2026 India AS pay was found (only stale 2020–2022 self-reports and an adjacent Amazon Bengaluru SWE median of ₹6.03M as of April 2026) [B/C/D · T0-52 L83, L281–L283, L429]. US sponsorship is evidenced by Amazon's 312 AS II LCAs in FY2024 (+44 at Amazon Development Center), and Zalando offers Berlin relocation assistance [A/B · T0-52 L87, L384–L387].

## Interview themes and preparation notes

T0-52 revises the scorecard's "classic ML system design" summary: across 2026 candidate reports, system design occupies **at most one round** at Amazon, is sometimes omitted at Microsoft and is not named at Zalando, while **ML breadth, ML depth, live coding (including ML algorithms from scratch) and behavioural or product-scope rounds** carry most of the loop [C · T0-52 L84, L306, L444].

| Employer | Reported loop structure (2025–2026 reports) | Key assessment themes and caveats | Grade |
|---|---|---|---|
| Amazon (US and India) | Recruiter screen → ~60-min technical phone (science + easy/medium coding + LPs) → 4–6 virtual onsite rounds (ML breadth, ML depth, coding, team-specific system design, Bar Raiser / LPs); PhDs add a research talk; Bengaluru interns use HackerRank first | Easy-to-medium DSA plus ML coding (e.g. AUC); one July 2026 report adds agentic product thinking; Glassdoor rates difficulty 3.3/5 (77% positive); internal guidelines reportedly bar GenAI tools unless permitted (disqualification risk) | C (loop) / B (AI policy) · T0-52 L295–L298, L304–L306, L711–L712 |
| Amazon Lab126 | Recruiter screen → technical phone → onsite → research presentation (3–5 weeks) | Research presentation defended to a panel; Leadership Principles (vendor guide, COI) | C · T0-52 L300, L713 |
| Microsoft | 30–60-min screen → 3–4 rounds (45–60 min each) with coding in nearly every round | Résumé deep dive; ML fundamentals + ML coding from scratch (K-means, self-attention); LeetCode-medium DSA; SQL/pandas on some teams; recruiter prep material differed from actual rounds in one April 2026 L63 report | C · T0-52 L301, L497, L714 |
| Zalando (Berlin) | 30-min HR → hiring manager → 1-hr technical → 4 finals | Science depth, science breadth with coding, product-focused scope and collaboration (n ≈ 3 reports) | C · T0-52 L302, L715 |

**Preparation rules (no model answers; see [interview loops](../../08-interviewing/interview-loops.md) and the [classic ML system design prep pack](../../08-interviewing/prep-packs.md#classic-ml-system-design-pack)):**
- **Practise both DSA and ML coding from scratch.** Coding appears across nearly every Microsoft round and in Amazon and Zalando loops; PhDs who neglect algorithmic and ML-implementation coding fail screens despite strong publications [C · T0-52 L102, L295–L302].
- **Frame every project around offline-to-online customer lift.** Pair method depth with baselines, online A/B experimentation and business metrics moved; prepare STAR Leadership Principles stories for Amazon and verify GenAI-tool rules before any screen [A/B/C/P · T0-52 L102–L103, L310, L719, L726].

## Dossier evidence and limits

- **Sample and access:** 33 postings (23 read: 16 full requirement text, 7 Amazon Science description-only; 10 search-snippet level used only for degree, years, pay and aliases) [T0-52 L58, L198]. Only 17 of 69 ledger sources (25%) were read in full; 52 were Extract-only. Eight Extract-only ledger rows (S19–S23, S27–S28, S58) were graded A in T0-52's ledger and are treated strictly as **Grade B** here (matching T0-52's own JSONL downgrades for those JDs) [T0-52 L534–L543, L573, L767–L776].
- **Sampling bias and uncertainty:** Big Tech makes up 73% of the sample (24/33; Amazon alone 16/33 = 48%), skewing skill shares towards Amazon templates and GenAI postings (69% GenAI vs 4.5% LLMs in InterviewStack's all-keyword set); Indian GCCs, consultancies and Indian-headquartered firms are absent (0/33) [T0-52 L62, L191–L198, L476]. Skill shares carry ~±20 percentage point Wilson intervals [T0-52 L59, L477].
- **Freshness and platform anomalies:** Only 6 of 33 postings carry verified in-window dates (2026-08-17 to 2026-10-25), and undated pages may be cached [T0-52 L201–L205, L478]. Levels.fyi Amazon AS shows two different medians on one page ($335K header vs $306K FAQ), and its 19.8% median rise from June 2025 to August 2026 against 1.7%–5.2% per-level increases indicates reporter-mix shift [T0-52 L183, L272, L479]. Loop evidence rests on small anecdotal samples (~6 Amazon, ~8 Microsoft, ~3 Zalando reports) with none retrieved for Uber, Hippocratic AI or Mistral [T0-52 L102, L303, L482].
- **Key absences:** 2025–2026 India AS pay, European posted pay (0/8), Microsoft AS pay on Levels.fyi (mapped to Data Scientist), a JobsPipe AS page, actual PhD share of hires, and post-2022 official hiring-manager proof guidance [T0-52 L453–L470].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
