---
id: roles.hub.gpu-kernel-engineer
title: "GPU Kernel / ML Compiler Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "GPU Kernel / ML Compiler Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-63]
roles: [gpu-kernel-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# GPU Kernel / ML Compiler Engineer

> Writes and tunes GPU kernels and compiler paths for training and inference, and validates their numerics.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| AI Infrastructure & Platform | L1 Compute and hardware; also L3 Inference and ML platforms | Verified (V) | #16 of 24 | #16 of 24 · band B · Monte Carlo rank 16 (P10–P90 13–18) | D1 Serving & kernels |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 4 (3–5.5) | C | CUDA/GPU kernels named in 6.6% of S09 postings (29.3% of companies) [T0-03 6.3]; River AI (GPU kernels) and AMD (Triton kernels) among T0-13's inference/kernel postings [T0-13:112, 737]. |
| Pay | 7.5 (6.5–8.5) | B | US core sample (n=17) median posted base band $190K–$287.5K (median midpoint $235.8K, IQR $217.5K–$275K); frontier labs and NVIDIA/AMD Staff/Principal reach $400K–$700K+ TC [T0-63]. |
| Durability | 6.5 (5–8) | D | Judgement. Frontier scarcity vs counter-evidence: tile DSLs (Helion, CuteDSL, CUDA Tile) and automated kernel agents abstract kernel writing [T0-03:L542, L101]; no labour data either way [T0-03:L571]. |
| Leverage | 8.5 (7.5–9.5) | D | Judgement. GPU efficiency moves a large cost line (8.5-9 anchor). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4 (3–5) | B | 8 of 41 core postings (19.5%) in India across Bengaluru and Hyderabad: NVIDIA, AMD, Qualcomm, Sarvam AI and silicon GCCs [T0-63]. |
| India pay | 6.5 (5–8) | C | No employer-posted India kernel band; one Bengaluru recruiter band Rs70–90L base (C) plus NVIDIA/AMD Bengaluru staff engineering bands [T0-63]. |

India rank (CCI with India inputs): #15 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 4 | ○ 2 | ○ 1.5 | ○ 1 | ◐ 4.5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** C++, CUDA / Triton / CUTLASS, GPU fundamentals (HBM, prefill vs decode), Linear algebra, Profiling & roofline (Nsight).
- **Important (headline):** Attention, GEMM & quantised kernels, GPU memory performance, Numerics validation, ML compilers (XLA, TorchInductor), Quantisation (FP8/FP4, AWQ, GPTQ).
- **Full inventory:** 45 skills (Must 7 · Important 14 · Should 11 · Optional 13), each with its evidence and posting keywords: [gpu-kernel-engineer.md](../../03-skills-and-tech/inventories/gpu-kernel-engineer.md).
- **Prerequisites:** Systems / C++ / CUDA background or a PhD
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** GPU MODE leaderboard submissions; kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware with correctness tests
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P9 Custom Triton kernel with benchmarks and correctness tests](../../05-portfolio/project-archetypes.md#p9) (80%); [P5 Single-GPU serving and quantisation study](../../05-portfolio/project-archetypes.md#p5) (32%); [P7 Small-scale distributed training / post-training study](../../05-portfolio/project-archetypes.md#p7) (12%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Infrastructure.** It tests KV-cache maths, decode roofline, continuous batching, prefill/decode disaggregation, GPU scheduling, p95 debugging. Source: T1-03, T0-14 (first collected in the role catalog §8.2; this file is the owner).
- **Practise:** the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** D1 Serving & kernels (AI Systems & Infrastructure); headline pattern: "Inference Engineer: LLM serving and GPU performance". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** CUDA, Triton, CUTLASS, kernels, GPU, compiler, XLA, performance
- **Leave out or reframe:** Raw-kernel claims without benchmarks and correctness tests
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-gpu-kernel-engineer).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Inference / LLM Serving Engineer](inference-engineer.md) (0.21); [Research Scientist (AI/ML)](research-scientist.md) (0.09); [Research Engineer / Member of Technical Staff](research-engineer.md) (0.09).
- **Same family (AI Infrastructure & Platform):** [Inference / LLM Serving Engineer](inference-engineer.md), [AI Infrastructure / GPU Platform Engineer](ai-infrastructure-engineer.md), [ML Platform / MLOps Engineer](ml-platform-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-gpu-kernel-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-gpu-kernel-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A November 2026 sample of 41 core postings across 30 employers (from 90 screened; 16 verified in-window or opened live) confirms the role spans **three distinct technical tracks** across hardware (L1) and serving platforms (L3) [M · T0-63 L50, L83, L142–146]:

| Variant | Sample share | Typical employers | Core technical scope |
|---|---|---|---|
| **1. Kernel authoring and optimisation** | 26/41 (63.4%) | Anthropic, xAI, OpenAI, Mistral, NVIDIA, AMD, River AI, RadixArk, Inferact, CoreWeave, Sarvam AI | Custom attention, GEMM, MoE and fused kernels in CUDA (85%, 22/26), Triton (69%, 18/26), CUTLASS/CuTe, HIP or Pallas; profiling and numerics |
| **2. Compiler or DSL engineering** | 10/41 (24.4%) | NVIDIA (Triton, CUDA Tile, HW-SW codesign), AMD (Triton/LLVM), Google (TPU compilers), Microsoft (Maia), Meta, SambaNova | MLIR/LLVM passes, XLA, TorchDynamo, Triton and CUDA Tile compilers; CUDA named in 40% (4/10), Triton in 40% (4/10) |
| **3. Custom-silicon enablement** | 5/41 (12.2%) | Amazon Annapurna (Trainium NKI), Cerebras, Graphcore, Intel | Kernel libraries, low-level assembly and Triton/runtime ports for non-NVIDIA accelerators; CUDA named in 0% (0/5), Triton in 20% (1/5) |

Workload focus confirms the L1 + L3 footprint: 43.9% (18/41) explicitly name inference or serving, 14.6% (6/41) name training, and 0% are training-only [M · T0-63 L83, L321].

**Skill shifts revising the Phase 0 scorecard (`K10`, `K11`):**
- **Promote Triton to Must; CUDA C++ remains dominant:** **CUDA or Triton** appears in 73.2% (30/41) of core postings — CUDA in 63.4% (26/41) and **Triton in 56.1%** (23/41; 69% of kernel-led postings) [M · T0-63 L76, L186–187, L197]. Profiling/performance analysis is the largest non-language ask at 46.3% (19/41; Nsight by name 12.2%) [M · T0-63 L191, L200]. Explicit C++ appears in 31.7% (13/41) because CUDA C++ is implied [M · T0-63 L188].
- **Skills over-tiered in Phase 0:** Linear algebra is named explicitly in only 4.9% (implicit in GEMM work); CUTLASS (14.6%), CuTe (12.2%), quantisation (9.8%), Hopper (4.9%) and Blackwell (4.9%) sit in the Should band rather than universal Important [M · T0-63 L190, L196–202].
- **Major skills missing from the Phase 0 headline card:** **TPU / Pallas / XLA** (26.8%, 11/41), **PTX / SASS / assembly** (22.0%, 9/41 — Important for NVIDIA targets), **MLIR / LLVM** (19.5%, 8/41 — Important on the compiler track), **Python** (19.5%, 8/41), **ROCm / HIP** (17.1%, 7/41), **NCCL / multi-GPU communication** (17.1%, 7/41) and **open-source kernel contributions** (17.1%, 7/41) [M · T0-63 L204–211]. Tile DSLs (CuTe, **CUDA Tile** launched with CUDA 13.1, TileLang — plus PyTorch **Helion** compiling to `tileir` and `CuTeDSL`, live-verified 2026-11-19) appear in 14.6% (6/41) and are generating compiler roles, yet have not made CUDA C++ optional [B/M · T0-63 L84, L212, L362].
- **Proof of work and résumé positioning:** Employers ask for hardware-measured proof rather than claims. **Sarvam AI** calls its GitHub filter its highest-yield signal and asks for production kernels that beat published baselines by a measurable margin [A · T0-63 L79, L270]; NVIDIA asks for FlashInfer, Triton or CUTLASS PRs, AMD asks for upstream Triton/LLVM/MLIR, and RadixArk asks for SGLang [B · T0-63 L271]. **GPU MODE** (>20,000 members per NVIDIA Technical Blog) runs public leaderboards across B200, H100, A100 and L4 and co-hosted the NVIDIA Blackwell NVFP4 four-problem hackathon (2025-11-10 to 2026-02-13), though hiring conversion from leaderboard placements is unreported [B · T0-63 L79, L274, L424]. Name the exact GPU (H100/H200/B200), baseline library (cuBLAS, FlashAttention), before/after metric and dtype numerical tolerance on every résumé line — unbenchmarked "optimised CUDA" claims destroy credibility [A/P · T0-63 L341–358, L408].

## Employer landscape and title confusion

**Employer mix (November 2026):** The 41 core postings span **30 distinct employers**, refuting the myth that only NVIDIA hires (NVIDIA accounts for 6 of 41 core postings and 11 of 59 retained postings including internships and adjacent roles) [M · T0-63 L85, L136, L367]. Core employer split: chip vendors and accelerator startups **34.1%** (14: NVIDIA, AMD, Intel, SambaNova, Graphcore, Cerebras), AI-native and inference clouds **24.4%** (10: River AI, Relace, Preference Model, Sciforium, RadixArk ×2, CoreWeave, Inferact, FriendliAI, Luma AI), frontier labs **12.2%** (5: Anthropic, xAI, OpenAI ×2, Mistral), Big Tech **12.2%** (5: Google ×2, Amazon Annapurna, Microsoft Maia, Meta), services/recruiters **7.3%** (3: Wipro, EPAM, Square Root Consulting), enterprise **4.9%** (2: Databricks, Waymo) and India-based employers **4.9%** (2: Sarvam AI, Taglynk client) [M · T0-63 L118–127, L175].

**Severe title noise and boundaries:**
- **Aggregator pollution:** Of 90 postings screened, **31 (34%) were excluded**: 9 NVIDIA OS-kernel/driver/firmware roles, 15 stale/expired roles, 3 non-ML CUDA application roles, and **4 hourly AI-trainer/evaluator gigs ($60–$100/h)** borrowing the "GPU Kernel Engineer" title (OpenTrain, Anyone AI, Gramian) [M/C · T0-63 L75, L130–134, L451]. On Inference Jobs' "GPU Kernel Development" tag (79 jobs), page 1 (`n = 20`) held 45% OS/driver roles, 30% stale kernel/compiler roles, 10% other stale roles and only **15% (3/20) fresh kernel/compiler postings** [B/M · T0-63 L75, L170–171].
- **Aliases to search (`K2` updated):** Among 41 core titles, 53.7% contain *Kernel*, 31.7% *Performance* or *Optimization* and 24.4% *Compiler* [M · T0-63 L157–162]. Add *Performance Engineer (GPU, Kernels)*, *Research Engineer, GPU Performance*, *ML Kernels & Runtime*, *ML Engineer, GPU Kernel and Runtime*, *Systems ML — Compilers / Backend* and *Neuron / NKI Kernel Engineer* [M · T0-63 L164, L396].
- **Boundary with Inference Engineering:** Anthropic's *Performance Engineer, Inference* explicitly states that reasoning about kernel concepts matters more than having written kernels yourself, and its Staff+ Inference Runtime ($405K–$485K) is Rust/Python serving work; Sarvam splits Kernels (writes GPU code) from Inference (integrates it and owns serving SLOs) [A/B · T0-63 L80, L149]. Qualcomm's *GPU Kernel Development Engineer* mixes mobile GPU driver work with ML kernels (adjacent) [B · T0-63 L153].
- **Credentials and degrees:** **0 of 41 core postings** name a certification; skip certifications and build public kernel proof [M · T0-63 L81, L280]. Across the 7 postings with visible degree text, a Bachelor's degree was accepted in **7 of 7** ("or equivalent experience" in 4/7), and a Master's or PhD was required in **0 of 7** [M · T0-63 L81, L282].

## Career path, India demand and market signals

**Seniority and entry routes:** The core track has **0 of 41 entry-level postings** (6 mid, 12 senior, 4 staff/principal, 19 unstated; stated minimum 2–8 years, median 5, `n = 10`) [M · T0-63 L74, L176]. Entry operates through three concrete gates: (1) **internships** (3 NVIDIA kernel/compiler internships in Austin, Zürich and Shanghai/Beijing), (2) **new-graduate programmes** (NVIDIA TensorRT Performance New College Grad 2027; 2026 sibling posted $124K–$241.5K), and (3) **merit-based take-homes** (Anthropic reports hiring several top performance engineers straight from undergraduate study via its take-home [A, COI]) [A/B · T0-63 L74, L79, L297, L564–566, L575]. Relace also explicitly prefers a strong low-level systems engineer with no GPU experience over an average CUDA programmer [B · T0-63 L273]. For experienced engineers without kernel PRs, entering via adjacent inference/performance or compiler roles is the highest-probability path [D · T0-63 L90, L105–107].

**Progression and durability (`K7` updated):** IC ladders run NVIDIA L3–L5, Google/Graphcore Staff, and SambaNova Principal, with exits into kernel engineering management (Cerebras, Amazon NKI, Meta MTIA, Baseten), technical PM for kernels/ROCm (Amazon, AMD) or founding kernel startups [B/C · T0-63 L301–305]. Durability shows an active tug-of-war as of November 2026:
- *Automation pressure:* Cursor and NVIDIA co-authors reported a multi-agent harness (SOL-ExecBench) optimising 235 CUDA kernels on 27 B200 GPUs over three weeks, beating single-agent-optimised PyTorch baselines on 149/235 (63%) with a 1.38× geomean speedup — **crucial caveats:** the baseline was single-agent-optimised PyTorch (not expert vendor libraries), median speed-of-light score was 0.56, and generated BF16 GEMM stayed at 86% of cuBLAS [A for post existence (live-confirmed 2026-11-19); C/COI for self-reported benchmarks · T0-63 L84, L308]. Anthropic likewise reported Claude Opus 4.5 matching top human scores on its 2-hour take-home [C, COI · T0-63 L79, L309].
- *Counter-forces:* Anthropic notes humans with unlimited time still beat models and that its performance engineers' work is shifting toward **debugging, verification, numerics and systems design** [C, COI · T0-63 L311]; NVIDIA, Waymo and Etched postings explicitly *add* agentic kernel-optimisation duties rather than cutting headcount [B · T0-63 L312]; and new abstractions (**CUDA Tile** in CUDA 13.1) plus custom silicon (TPU, Trainium, Maia, MTIA, Cerebras) are creating compiler and enablement demand [B · T0-63 L84, L313]. Hedge by pairing hand-written kernel skills with numerics verification and compiler/DSL depth [D · T0-63 L96].

**Pay signals, geography and sponsorship:** Full pay tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). Across 17 US core postings with disclosed bands, the median base band is **$190K–$287.5K** (median midpoint **$235.8K**, IQR $217.5K–$275K; W1-only `n = 8` midpoint $244.6K) [M · T0-63 L77, L226–227]. Frontier labs sit well above: Anthropic posts **$280K–$850K** across levels for `Performance Engineer, GPU` [A, COI] (separate from its $405K–$485K adjacent Staff+ Inference Runtime role [B, COI]) and OpenAI posts $325K–$490K for AMD GPU Enablement [B]; NVIDIA posts $152K–$356.5K across L3–L5, consistent with Levels.fyi NVIDIA US IC4 average base ($244K) and all-level median TC ($315K, `n = 2,369`) [B · T0-63 L77, L228–237]. Europe: Graphcore Gdańsk posts PLN 196.4K–474.4K (mid to staff) [B · T0-63 L244]. Geographically, **70.7% (29/41) are in the US**, 19.5% (8) India, 7.3% (3) Europe and 2.4% (1) China; only **12.2% (5/41)** offer a remote option [M · T0-63 L82, L325–329]. On US sponsorship (pointers, not legal advice; verify in [visa and relocation](../../11-tracks/visa-and-relocation.md)): Anthropic explicitly sponsors [A, COI], NVIDIA had 2,380 certified H-1B LCAs across all titles in FY2026 through Q3 (filings are not pay) [B], one aggregator lists Fireworks AI as not offering H-1B sponsorship [C], and the US $100,000 H-1B entry-fee proclamation remained actively contested in federal courts as of November 2026 (V0) [B · T0-63 L82, L330–337].

**India demand — Phase 0 "No India evidence" contradicted (`K5`, live-verified 2026-11-19):** Contrary to the Grade D placeholder in the generated scorecard above, T0-63 documents **8 of 41 core postings (19.5%) in India** (Bengaluru and Hyderabad), corroborated by live web checks on 2026-11-19 [A/B · T0-63 L78, L373–388, L399]:
- **Indian AI lab:** **Sarvam AI** (`Performance Engineer, Kernels`, Bengaluru, on-site, opened live and live-verified 2026-11-19) — 5+ years ML systems, 2+ years authoring production CUDA kernels, CUTLASS/CuTe/PTX, Hopper/Blackwell (`TMA`, `tcgen05`, FP4), paired with a companion Inference role [A · T0-63 L78, L380–383, L562].
- **Chip-vendor R&D centres:** **AMD** (Hyderabad and Bengaluru — `ML GPU Kernel Development Engineer` from 2+ years, ROCm/HIP/Composable Kernel, Triton and AI/ML compilers; live-verified 2026-11-19) and **Intel** (Bengaluru — `AI Software Solutions Engineer, Kernel Dev`) [B · T0-63 L375, L535–537]. NVIDIA India postings in T0-63's window were GPU assembler, CUDA driver and system-software roles rather than ML-kernel roles; Qualcomm Bengaluru posted an adjacent Lead AI Compiler/Vulkan role [B · T0-63 L384–385].
- **Big Tech, services and startups:** **Google** (Bengaluru — `ML Compiler Engineer, TPU Performance Optimizations`; live-verified 2026-11-19), **EPAM** (Hyderabad and five other cities — GPU/TPU Pallas kernel optimisation), a **recruiter-listed senior kernel/inference role** (Bengaluru, 8–15 years, posted 2026-09-30) and an **Indian startup client** (Taglynk, Bengaluru, 2–5 years) [B/C · T0-63 L375–378].
- **India pay (`K6` updated):** No employer-posted kernel band was found. One recruiter listing (Bengaluru, 8–15 years) posts **₹70–90 LPA base** plus ESOPs and variable [C], while NVIDIA India software-engineer proxies conflict by method — crowd-sourced averages near ₹22.9 LPA [C, COI] versus Levels.fyi total-compensation medians of ₹6.0M India / ₹6.33M Greater Bengaluru [B] (see [pay benchmarks](../../09-compensation/pay-benchmarks.md)) [B/C · T0-63 L78, L238–242, L251, L387].

## Interview themes and preparation notes

The generated card's **Infrastructure** track label fits, but its topic list misses core kernel-loop exercises (`K9` updated) [C · T0-63 L264–265, L403]:
- **Employer loops and AI policies:** **Anthropic** uses a performance-engineering take-home on a simulated accelerator (originally 4 hours, then 2 hours, then redesigned into a constrained-ISA puzzle after Opus 4.5 matched top human 2-hour results; over 1,000 candidates completed since early 2024; AI tools allowed by design on the take-home, while general live-interview rules bar AI unless stated; the historical take-home is open-sourced) alongside recruiter, coding and ~5-session virtual onsite rounds [A for take-home, COI; C for stages · T0-63 L79, L259]. **NVIDIA** guides report 4–6 rounds over 4–8 weeks covering CUDA/systems coding, GPU performance reasoning, team-sized design and behavioural rounds (one guide states unapproved outside tools disqualify candidates, unverified on NVIDIA's page) [C · T0-63 L260]. **xAI** screens with CV plus a "statement of exceptional work" [B · T0-63 L261]; **Sarvam AI** screens heavily on GitHub/open-source kernel history [A · T0-63 L262].
- **Kernel-specific themes to add to prep (no model answers, per D-018):** Time-boxed kernel optimisation, roofline diagnosis (compute-bound vs memory-bandwidth-bound), Nsight Compute / Nsight Systems profiler walkthroughs, floating-point numerics and dtype tolerances (FP8/FP4/BF16), and hardware architecture mechanics (warps, SMs, shared memory, tensor cores, async copies) [C · T0-63 L93, L265]. Practise on Anthropic's open-sourced performance take-home alongside the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack) and [interview loops](../../08-interviewing/interview-loops.md). Confirm AI-tool permissions in writing before each stage [P · T0-63 L93].

## Dossier evidence and limits

- **Sample and access:** 41 core postings (plus 3 internships and 15 adjacent; 31 of 90 excluded), retrieved 2026-11-13 (anchor 2026-11-11, 90-day window from 2026-08-13). Only **16 of 41 core postings (39%) are W1** (dated on or after 2026-08-13 or opened live), and only **3 core postings** were opened on employers' own domains (Anthropic Greenhouse API, Sarvam Ashby page, NVIDIA careers meta); OpenAI and xAI refused automated fetches, and NVIDIA Workday was not indexed [M · T0-63 L49–52, L135, L416]. Only W1 records support recency claims [T0-63 L45, L435].
- **Sampling bias and COI:** Search keywords ("kernels", "CUDA", "Triton") inflate those skill shares while partial-text mirrors make all shares lower bounds (±15 pp at `n = 41`), and mirror dates drift (e.g., NVIDIA and Sciforium) [T0-63 L57–60, L435–436]. COI disclosures apply to Anthropic (model developer; S1, S2, S4), Cursor and NVIDIA co-authored kernel-agent benchmarks (S6), HeroHunt recruiting content (S7) and upGrad course-seller salary pages (S37) [T0-63 L13, L438–439, L455–457]. Modelled aggregator pay estimates (Glich, Ladders, Salary.com) were graded E and excluded [T0-63 L252, L452].
- **Explicit absences (not measured as of 2026-11-13):** monthly posting-count trend since January 2025; employer-posted India kernel pay bands; kernel-specific Levels.fyi titles and H-1B LCA counts; named hiring-manager proof statements beyond Anthropic and Sarvam; India-specific interview loops and kernel loops at AMD, Google, Meta and Microsoft; NVIDIA India ML-kernel postings within the 90-day window; hiring conversion outcomes for GPU MODE/hackathon placements; non-English postings; LinkedIn/Indeed live counts; and official USCIS reads on the contested $100,000 H-1B fee [E · T0-63 L414–428].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
