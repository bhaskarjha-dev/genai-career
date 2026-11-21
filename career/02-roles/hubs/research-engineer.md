---
id: roles.hub.research-engineer
title: "Research Engineer / Member of Technical Staff: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "Research Engineer / Member of Technical Staff on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-50, T0-55]
roles: [research-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Research Engineer / Member of Technical Staff

> Engineering for frontier research: training runs, post-training and reinforcement learning, evaluations and research infrastructure; often titled Member of Technical Staff.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Research | L2 Foundation models and research; also L4 Post-training and adaptation, L3 Inference and ML platforms, L1 Compute and hardware; planes: Evaluation and quality | Verified (V) | #5 of 24 | #4 of 24 · band A · Monte Carlo rank 4 (P10–P90 2–6) | C1 Engineering |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 5.5 (4.5–7) | B | Fast AI Jobs 223 Research Engineer roles (2026-11-12, up from 171; quorum-crossing candidate flagged for 2026-12-01 recount); AI Pulse 569 category count (C); Anthropic 670–674 total listings (>=30 RE page 1), OpenAI 822 via Epoch AI (2026-11-06) [T0-50, T0-70]. |
| Pay | 9 (8–10) | B | Frontier US posted base bands (Nov 2026): Anthropic $315K–$850K, OpenAI $205K–$555K, xAI $180K–$600K, Thinking Machines $350K–$475K, DeepMind $166K–$244K, Microsoft AI IC4–IC5; equity lifts lab TC well above $500K–$1M+ [T0-44, T0-50]. |
| Durability | 7.5 (6–9) | D | Judgement. Frontier distributed-training and post-training infra scarcity [T0-03 Tier 3] and strong lab 2-yr retention (SignalFire: Anthropic 80%, DeepMind 78%, OpenAI 67%, B) balanced against task-automation signals (Anthropic Opus 4/4.5 take-home; METR 320-min 50% horizon, B) [T0-50 K7]. |
| Leverage | 8 (7–9) | D | Judgement. Frontier training-run reliability, post-training recipes and research velocity at AI labs [T0-50]. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 2 (1–3) | C | Two verified live India RE postings (Google DeepMind Bangalore, Sarvam Bengaluru); 0 RE titles on Anthropic page 1 and Microsoft AI Bengaluru (77 listings) [T0-50]. |
| India pay | 8 (6–9.5) | D | No India evidence: 0 of 2 live India RE postings disclose pay [T0-50 K6]; adjacent Bengaluru Principal MTS outlier $192.5K USD on Levels.fyi (n=1, B adjacent) [T0-45, T0-50]. |

India rank (CCI with India inputs): #10 of 24. One input (India comp) is a Grade D placeholder.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ○ 3 | ○ 3 | ○ 2 | ○ 1 | ● 7.5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), PyTorch, PyTorch internals, ML fundamentals, Deep learning & transformers, Data structures & algorithms.
- **Important (headline):** Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), Training-run debugging, LLM evaluation (golden sets, calibrated judges, CI gates), Profiling & roofline (Nsight), Data pipelines & quality.
- **Full inventory:** 59 skills (Must 6 · Important 14 · Should 18 · Optional 21), each with its evidence and posting keywords: [research-engineer.md](../../03-skills-and-tech/inventories/research-engineer.md).
- **Prerequisites:** Strong systems/ML engineering profile, fellowship (Anthropic Fellows: no PhD required) or OSS (vLLM, SGLang); only 1/18 JDs in T0-50 required a PhD [B/C · T0-50]
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** Paper re-implementations with rigorous evals; a nano-vLLM-style engine benchmarked against vLLM; DDP/FSDP2 smoke tests; upstream OSS contributions; fellowship projects
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P7 Small-scale distributed training / post-training study](../../05-portfolio/project-archetypes.md#p7) (70%); [P4 Prompt vs RAG vs fine-tune comparison](../../05-portfolio/project-archetypes.md#p4) (53%); [P8 Paper re-implementation with rigorous evals and a write-up](../../05-portfolio/project-archetypes.md#p8) (47%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Research.** It tests coding-led loops and paid work trials for Research Engineer and AI Safety roles (Anthropic Python-only coding with AI-partnership rules [A, COI], xAI 1-week loop [A], FAR.AI 72-min coding plus work trial [B]; research talk not confirmed for RE or safety), versus quiz, coding and research/past-work talk for Research Scientist (DeepMind [A], xAI [A]). Source: T0-14, T0-46, T0-50, T0-55, T0-60, T1-03.
- **Practise:** the [research prep pack](../../08-interviewing/prep-packs.md#research-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** C1 Engineering (Frontier Research); headline pattern: "Research Engineer: distributed training, post-training, evals at scale". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** Member of Technical Staff, research engineer, PyTorch, distributed training, post-training, RL / RLHF, evals
- **Leave out or reframe:** Listing frameworks without scale evidence; claiming research taste without artifacts
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-research-engineer).

## Specialisations inside this role

- **Post-training and reinforcement learning** (L4 Post-training and adaptation): Absorbed into Research Engineer (legacy title in the A–Z index; named in 55.6% of RE [T0-50], 41.7% of RS [T0-55] and 26% of AS postings [T0-52]).
- **Synthetic data** (L4 Post-training and adaptation): No title of its own in the catalog.
- **Pre-training at scale** (L2 Foundation models and research): Candidate title (ungraduated): live pre-training postings at 4 employers and Distributed Training Engineer at OpenAI/Periodic Labs in Nov 2026 [C · T0-69 K17–K18; ERRATA U38], role catalog §5.2.
- **Reasoning models and test-time compute** (L2 Foundation models and research): Unmeasured buzzword: Reasoning Engineer, role catalog §5.2.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Research Scientist (AI/ML)](research-scientist.md) (0.46); [Machine Learning Engineer](ml-engineer.md) (0.31); [Applied Scientist](applied-scientist.md) (0.29).
- **Same family (Research):** [Research Scientist (AI/ML)](research-scientist.md), [Frontier AI Safety / Alignment Researcher](ai-safety-researcher.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-research-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-research-engineer): narrative skills, tools, interview and typical gaps.
- [PhD to industry](../../11-tracks/phd-to-industry.md): the track playbook for this role.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

Research Engineer / Member of Technical Staff (MTS) is the engineering half of frontier-model research: turning research hypotheses into stable training runs, post-training pipelines, evaluation fleets and data infrastructure [A · T0-50 L61, L105]. In the November 2026 employer-page sample (n = 18 distinct postings), work clusters into five operational tracks (a posting may span several) [M · T0-50 L307–L322]:

- **Post-training and reinforcement learning (9/18, 50%):** reward modelling, RL environments, synthetic data and model-behaviour post-training (OpenAI, Microsoft AI, Anthropic Zurich, Google DeepMind Gemini) [A/M · T0-50 L105, L311].
- **Research infrastructure and distributed systems (6/18, 33%):** failure-tolerant RL distributed systems, multi-GPU training runtimes and inference-adjacent tooling — including roles that ask for systems-engineering depth (Python plus Rust, C++ or Go) and list ML experience only as preferred (Anthropic RL Distributed Systems; Thinking Machines Training Systems) [A/M · T0-50 L105, L312, L494, L503].
- **Pre-training at scale and training data (5/18, 28%; data 2/18):** scaling training across thousands of GPUs, optimiser development and petabyte-scale data curation in Python, Spark and Ray (Anthropic Pre-training, xAI Pre-training Data) [A/M · T0-50 L105, L313, L317, L491, L497].
- **Evaluation fleets (5/18, 28%):** designing, running and analysing large-scale evaluations during live training runs, sitting directly on the evaluation and quality plane [A/M · T0-50 L314, L495, L499].
- **Agents, multimodal and interpretability tooling (agents 5/18; multimodal 4/18; interpretability 1/18):** building tooling for researchers, including roles stating explicitly that no prior research experience is required (Anthropic Interpretability, asking for 5–10+ years of software engineering) [A/M · T0-50 L315–L319, L496].

**Footprint and skill nuance.** Revising Phase 0's L2/L4/L1 footprint (reflected in the expanded L2/L4/L3/L1 plus evaluation-plane scorecard above), T0-50 finds infrastructure (50% named anywhere; 22% primary) and evaluation/assurance (33% named; 11% primary) recurring across postings [M · T0-50 L324–L341]. On n = 18 (Wilson 95% intervals ±20–25 percentage points — a cross-check rather than a standalone tier override), Python (67%, 12/18) is the sole scorecard Must that appears in over half of postings; general software engineering (39%), cross-functional collaboration (39%), reinforcement learning (39%), ambiguity/pragmatism (33%), evaluations (33%), JAX/TPU (33%) and post-training (33%) outrank explicit PyTorch (28%, 5/18), deep learning (22%, 4/18), data structures and algorithms (6%, 1/18 — Google DeepMind Bangalore only), FSDP (0/18) and PyTorch internals (0/18) [M · T0-50 L64, L187–L232]. Treat DSA as an interview skill rather than a job-description keyword [M · T0-50 L84, L232].

**Proof and credentials.** Zero of 18 postings name any certification [M · T0-50 L289]. Instead, application forms ask for an achievement statement ("the technical achievement you're most proud of" at Anthropic; a 100-word "statement of exceptional work" at xAI), a team-specific motivation essay (200–400 words at Anthropic) and optional Google Scholar or GitHub links (5/18 postings) [A · T0-50 L183, L285, L352]. Preferred qualifications name upstream open-source ML infrastructure (PyTorch, XLA, Megatron-LM, DeepSpeed; plus SGLang and vLLM in Thinking Machines' uncoded Inference posting) [A · T0-50 L285, L503, L661].

## Employer landscape and title confusion

Title choice reflects employer convention rather than work content [A/B · T0-50 L62, L115]. Searching only for "Research Engineer" misses a large share of identical roles posted under MTS or dual titles:

| Title family in T0-50 sample (n = 18) | Share | Typical employers and usage | Grade |
|---|---|---|---|
| Research Engineer | 50% (9/18) | Anthropic, OpenAI, Google DeepMind, Thinking Machines Lab | A/M · T0-50 L107–L109 |
| Member of Technical Staff (MTS) + team suffix | 22% (4/18) | xAI (Pre-training Data, Model Training, Macrohard), Microsoft AI (Post Training) | A/M · T0-50 L110 |
| Research Engineer / Scientist (dual title) | 17% (3/18) | OpenAI Post-Training, Anthropic Pre-training, Sarvam AI, Mistral | A/M · T0-50 L111, L507–L508 |
| Adjacent engineering titles | 11% (2/18) | OpenAI Training Performance Engineer; Amazon Sr. ML Engineer, AGI Foundations | A/M · T0-50 L112–L113, L500, L505 |

- **Employer board conventions diverge.** On 2026-11-13, Microsoft AI's careers board listed 54 of 84 titles as "Member of Technical Staff" and zero as "Research Engineer" (though the page simultaneously printed a filter mismatch warning, so exact totals are uncertain) [A · T0-50 L62, L125, L415]. By contrast, page 1 of 14 on Anthropic's Greenhouse board contained at least 30 "Research Engineer" titles (29 excluding one expression-of-interest row) [A · T0-50 L66, L124].
- **Visa filings mask function behind plain MTS.** On aggregated FY2025–FY2026 Q3 certified H-1B LCAs (`careery.pro`), Anthropic filed 115 of 292 under plain "Member of Technical Staff" against 7 under "(Research Engineer)"; OpenAI filed 50 of 311 under "(Software Engineer)", 14 under "(AI Systems Engineer)" and 13 under "(Research Engineer)" [B · T0-50 L62, L129–L130, L635, L642].
- **Boundary and evergreen traps.** Amazon uses "Member of Technical Staff (Research Director)" for research leadership, not IC engineering [A · T0-50 L55, L115, L360], and posts multimodal pre-training engineering under "Sr. Machine Learning Engineer, AGI Foundations" [A · T0-50 L505]. Thinking Machines keeps infrastructure listings open as evergreen expressions of interest (asking applicants not to reapply within six months) and Anthropic lists `[Expression of Interest]` rows [A · T0-50 L71, L503]. Third-party "ghost job" counts on Anthropic's board (PitchMeAI, vendor COI) contradicted each other in two same-day readings (449 vs 603 stale; 62 vs 97 median days open) with no disclosed threshold [C · T0-50 L71, L128, L417].

## Career path, India demand and market signals

**Entry routes and the PhD misconception.** A PhD is not a stated minimum in T0-50's sample: 1 of 18 qualification lists names MS or PhD (Anthropic Pre-training, whose logistics block still accepts a bachelor's degree or equivalent experience), 9/18 state a bachelor's or equivalent, and 8/18 state no degree [A/M · T0-50 L63, L177–L181, L414]. However, postings are not hiring bars — no published analysis of actual hire degrees or prior roles was found, so real hire cohorts may still skew heavily towards PhDs [E · T0-50 L403, L619]. Two concrete routes stand out:

1. **Direct lateral entry (4–10+ years of production engineering):** distributed-systems and backend engineers fit infrastructure, RL systems and evaluation postings directly, even with limited prior ML research [A/D · T0-50 L79, L293].
2. **Fellowship and residency entry:** the Anthropic Fellows Program accepts candidates "regardless of previous experience" for 4 months full-time (stipend USD 3,850/week, GBP 2,310/week or CAD 4,300/week, plus roughly USD 15k/month compute on the RL track) [A, COI · T0-50 L69, L666; verified 2026-11-19]. Employer postings state 25–50% of prior fellows received full-time offers (RL listing) and over 80% produced papers in one earlier cohort, but those outcome figures are self-reported employer claims with no disclosed denominators or acceptance rates (COI) [C, COI · T0-50 L69, L664–L665]. Eligibility requires existing US, UK or Canada work authorisation and in-country presence with no visa sponsorship; also verify cohort dates before applying, because the RL listing still named a "late September" cohort on 2026-11-13 [A, COI · T0-50 L69, L422, L667]. See [PhD to industry](../../11-tracks/phd-to-industry.md#fellowships-and-residencies) for how fellowships compare across labs.

**Market signals, pay dispersion and durability.** All-function employer-board volume was 670–674 open roles at Anthropic (2026-11-06 to 2026-11-13) and 822 at OpenAI (Epoch AI, 2026-11-06); no national role-specific count or dated series exists [A/B · T0-50 L66, L121–L123, L131]. Posted US base ranges (equity extra) span USD 119.8K–304.2K at Microsoft AI (IC4–IC5) and USD 151.3K–261.5K at Amazon up to USD 180K–600K at xAI, USD 205K–555K at OpenAI, USD 350K–475K at Thinking Machines Lab and USD 315K–850K at Anthropic (London £260K–630K) [A · T0-50 L65, L238–L255]. Platform medians are unreliable for senior bands: Fast AI Jobs' Anthropic Research Engineer median (USD 300K, undated) sits below Anthropic's own posted bands, and Levels.fyi adjacent-title OpenAI Research Scientist medians drift widely across snapshots (USD 800K, n = 16, updated 2026-08-01 in T0-50 L73, L260 versus USD 1.25M in an undated cache in T0-55 L93, L266), with private stock accounting for 62.6%–73.5% of total packages [B · T0-50 L72–L73, L259–L264; T0-55 L266]. Full compensation tables and equity discounting live in [pay benchmarks](../../09-compensation/pay-benchmarks.md#the-level-ladder). On durability, SignalFire (May 2025, LinkedIn-based) reports two-year retention of 2023–2024 hires at 80% (Anthropic), 78% (DeepMind) and 67% (OpenAI) versus 64% across Meta, with 8× engineer flow from OpenAI to Anthropic and ~11:1 from DeepMind to Anthropic [B · T0-50 L75, L300, L675–L680]. Counter-signal: Anthropic reported pre-release Claude Opus 4.5 matching its strongest human applicants in 2 hours on its performance-engineering take-home (forcing redesign; COI), and METR measured a 320-minute 50%-completion horizon (95% CI 170–729; 88.6-day doubling time since 2024) on software and ML-research tasks as of January 2026 — both track task automation, not headcount contraction [A COI / B · T0-50 L75, L298–L299, L654, L683–L685].

**India demand and US sponsorship.** India-located openings are scarce: 2 of 18 postings (Google DeepMind Bangalore "Research Engineer, India" on MLO model efficiency/adaptivity, asking for Python or C++ and algorithm design; Sarvam AI Bengaluru autonomous-agent research), neither disclosing INR pay [A · T0-50 L70, L365, L508–L509]. Page 1 of Anthropic's board and Microsoft AI's Bengaluru board (77 listings) listed zero Research Engineer titles on 2026-11-13 [A · T0-50 L70, L126, L365]. Anthropic opened a Bengaluru office in February 2026 announcing "technical, research and business" hiring without naming titles or headcount, and its Fellows programme does not operate in India [B, COI · T0-50 L70, L365; verified 2026-11-19]. For US roles, sponsorship is per-role (6 of 18 postings carry a sponsorship sentence; Anthropic states it sponsors visas though not for every role or candidate; Thinking Machines states "We sponsor visas.") [A · T0-50 L67]. Under the DHS final rule effective 2026-02-27 (FR Doc 2025-23853, verified against primary Federal Register and USCIS records on 2026-11-19), cap-subject FY2027 H-1B selection weights entries 4/3/2/1 across OEWS wage levels IV–I [A · T0-50 L67, L346, L630]; the separate US$100,000 H-1B entry-restriction proclamation (extended 2026-09-18 to 2027-09-21) remained barred from collection following the June 2026 D. Mass. vacatur (*State of California v. Mullin*) and July 2026 First Circuit stay denial [B/C · T0-50 L67, L347–L348, L646–L647; verified 2026-11-19]. *Pointers only, not legal or immigration advice:* verify live V0 status in [visa and relocation](../../11-tracks/visa-and-relocation.md#status-table).

## Interview themes and preparation notes

Employer-authored process descriptions for Research Engineer roles are **coding- and applied-problem-solving-led**, revising Phase 0's narrower "research talk plus coding" summary [A/C · T0-50 L68, L281]. A formal short research talk is documented only for Google DeepMind Research Scientist loops in an undated blog post (likely pre-2023) [A, old · T0-50 L68, L274, L475].

| Employer | Reported rounds and focus | Candidate AI-tool policy | Grade |
|---|---|---|---|
| xAI (Pre-training Data, Search Post Training, Macrohard) | 15-min call; coding assessment (language of choice); two real-world LLM problem-formulation sessions (Macrohard lists three onsite technical rounds); "meet the team" presentation of past work and vision; 1-week target | Not stated | A · T0-50 L270, L610, L656 |
| OpenAI (engineering and research guide) | Résumé review (~1 wk); intro call; skills assessment (pair coding, take-home or test); 4–6 hours of finals with 4–6 people over 1–2 days; no research-talk round named | Silent; ask the recruiter | A · T0-50 L271, L653 |
| Anthropic (policy, Zurich RE, performance take-home) | Zurich post-training RE states "all interviews in Python"; performance team redesigned its simulated-accelerator take-home from 4 hours to 2 hours; Fellows runs assessments, interviews and a research discussion | Refine self-drafted applications only (no invented work); no AI in take-homes or live rounds unless explicitly permitted (allowed on the performance take-home) | A, COI · T0-50 L272–L273, L652, L654–L655, L667 |
| Google DeepMind (candidate reports, n = 5, 2025-12-16) | Recruiter screen; 2–3 technical rounds: two LeetCode-medium coding problems, ML fundamentals (optimisation, regularisation, losses, transformers), maths and system-design-style questions; no research talk reported | Not stated | C · T0-50 L275, L660 |

**Preparation rules (no model answers; see [interview loops](../../08-interviewing/interview-loops.md) and the [research prep pack](../../08-interviewing/prep-packs.md#research-pack)):**
- **Drill unaided Python coding and codebase debugging first.** Even research-titled roles screen heavily on live Python, systems debugging and ML fundamentals; confirm each employer's AI-tool rule in writing before any screen (Meta piloted AI-enabled SWE coding interviews in July 2025, whereas Anthropic bars live AI by default) [A/B · T0-50 L83, L272, L276, L658].
- **Match round emphasis to the team's layer.** Distributed-systems and performance postings probe multi-host failure debugging, profiling and communication libraries; post-training and eval postings probe experimental design, failure diagnosis and measurement quality [A · T0-50 L105, L494–L495, L500].
- **Keep a tight past-work walkthrough ready.** Both xAI's "meet the team" presentation and Anthropic Fellows' research discussion expect a defended technical narrative of work you owned end to end [A · T0-50 L270, L273, L281].

## Dossier evidence and limits

- **Sample and access:** T0-50 is **complete with gaps** — 18 distinct coded employer-page postings (plus 1 London duplicate for pay and 4 opened uncoded) against a 30-posting target, because HTTP 429 limits terminated 23 of 25 subagent launches [T0-50 L24, L51, L141]. In the source ledger, 26 of 47 sources (55%) were read in full, 14 were Extract-only and 12 carry Anthropic conflict of interest (model developer's own postings and blogs) [T0-50 L13, L438–L486].
- **Sampling bias and uncertainty:** Frontier labs supply 15 of 18 postings (Anthropic alone 5 of 18, colouring degree, pay, hybrid and visa findings); enterprises, consultancies, Indian GCCs and Europe beyond Zurich, Paris and London are missing [T0-50 L53, L143–L153]. Twelve of 19 coded records were subagent-extracted without a second line-by-line audit, and skill shares carry ±20–25 percentage point Wilson intervals [T0-50 L45, L53, L406].
- **Verification and data anomalies:** T0-50's three Extract-only Grade A rule records (S18, S19, S21) were independently verified against primary US government records on 2026-11-19. OpenAI, Microsoft AI and Amazon pages showed full descriptions without a visible Apply button in fetched text [T0-50 L183, L405]. Aggregated `careery.pro` LCA counts (showing an unexplained coincidence of exactly 101 FY2025 LCAs for both OpenAI and Anthropic, and 1.9–9.0× lower figures than prior position counts because one LCA can cover multiple positions) remain unreconciled against raw DOL OFLC files [T0-50 L133–L135, L418–L420].
- **Key absences:** Exact-title Levels.fyi pages for Research Engineer or MTS, India INR pay, official OFLC disclosure files, hiring-manager screening criteria, empirical education/background shares of actual hires, and career-ladder exit paths [T0-50 L388–L397].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
