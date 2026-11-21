---
id: roles.hub.inference-engineer
title: "Inference / LLM Serving Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "Inference / LLM Serving Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-56]
roles: [inference-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Inference / LLM Serving Engineer

> Owns the inference data path: batching, KV cache, scheduling, quantisation, speculative decoding, latency and cost.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| AI Infrastructure & Platform | L3 Inference and ML platforms; also L1 Compute and hardware | Verified (V) | #11 of 24 | #11 of 24 · band B · Monte Carlo rank 11 (P10–P90 8–15) | D1 Serving & kernels |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 4.5 (3.5–5.5) | C | Inference Jobs 341 'Inference Engineer' listings on 2026-11-13 (upper bound; page 1 ~40% aged <=3 months); 37 verified active postings across labs, inference clouds and hardware vendors [T0-56]. |
| Pay | 7.5 (6.5–8.5) | B | Date-clean US sample (n=14) posted base median midpoint $288K (IQR $261K–$344K, bounds $165K–$500K) plus equity at labs and inference platforms [T0-56]. |
| Durability | 7 (5.5–8.5) | D | Judgement. Strong latency/cost demand balances rapid engine churn (TGI archived, TensorRT-LLM static backend removed) and emerging automated kernel-optimisation tooling [T0-56, T0-69]. |
| Leverage | 8.5 (7.5–9.5) | D | Judgement. Direct GPU-cost and latency-SLO leverage (Anthropic Cloud Inference and Sarvam serving-efficiency scope [T0-56 L312]). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4 (3–5.5) | B | 9 of 37 core postings (24.3%) in India across Bengaluru, Hyderabad and Gurugram: AI startups (Sarvam, Gnani x2, PrimaLabs, AION), cloud hosts (DigitalOcean x2, Rackspace) and 1 Weekday recruiter client; 0 GCCs and 0 India silicon vendors found [T0-56]. |
| India pay | 6 (4.5–7.5) | C | 1 of 9 India postings discloses pay: Rs24–36L (5+ yrs, Weekday client, 2026, B) plus adjacent senior infra/ML Bengaluru bands [T0-56]. |

India rank (CCI with India inputs): #12 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 7 | ○ 2.5 | ○ 2.5 | ○ 1 | ◐ 4.5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), C++, GPU fundamentals (HBM, prefill vs decode), PyTorch internals, System design, vLLM / SGLang / TensorRT-LLM, Kubernetes, Continuous batching & KV cache.
- **Important (headline):** Speculative decoding, Quantisation (FP8/FP4, AWQ, GPTQ), TP/PP & MoE serving, Load testing & latency SLOs, Profiling & roofline (Nsight), Cost & latency engineering.
- **Full inventory:** 71 skills (Must 9 · Important 15 · Should 26 · Optional 20 · Avoid 1), each with its evidence and posting keywords: [inference-engineer.md](../../03-skills-and-tech/inventories/inference-engineer.md).
- **Prerequisites:** Backend → Staff-level inference takes ~10–14 months with infrastructure depth [D · T2-01]
- **Credentials (tie-breakers, not skills):** NVIDIA-Certified Professional: Generative AI LLMs (NCP-GENL) (Optional: announced (verify live Certiverse booking before prep); NCP-AIO targets live GPU serving/ops more directly); NVIDIA-Certified Professional: AI Operations (NCP-AIO) (Optional: $500, 30 MCQ + 3 live VM labs (only NVIDIA exam with confirmed live lab split); targets GPU cluster operations (T0-32:L599, T0-54:L259)); AMD ROCm Certified Associate (Optional: Free AMD ROCm GPU labs + exam; optional signal for AMD MI300X/ROCm inference teams (T0-32:L243, L857)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A single-GPU serving study (BF16 vs FP8/4-bit, prefix caching, chunked prefill, speculative decoding) with a roofline and $/M tokens at the SLO; a custom Triton kernel tested against a reference; an upstream PR to vLLM, SGLang or FlashInfer
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P5 Single-GPU serving and quantisation study](../../05-portfolio/project-archetypes.md#p5) (61%); [P6 Self-hosted LLM platform on Kubernetes](../../05-portfolio/project-archetypes.md#p6) (25%); [P21 Category-level public technical micro-audit or benchmark](../../05-portfolio/project-archetypes.md#p21) (25%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Infrastructure.** It tests sub-discipline specific: serving and inference (systems coding, distributed-systems design; KV-cache maths, decode roofline, continuous batching and prefill/decode disaggregation appear in prep guides [C]), GPU cluster ops (Slurm, InfiniBand/RDMA, NCCL debugging, bare-metal failure recovery, Kubernetes at scale), MLOps/ML platform (IaC, CI/CD, drift monitoring, feature stores, ML job schedulers) and GPU kernels (simulated-accelerator take-home [A, COI], profiler walkthrough, roofline analysis, numerics/dtype tolerances). Source: T0-14, T0-46, T0-54, T0-56, T0-58, T0-63, T1-03.
- **Practise:** the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** D1 Serving & kernels (AI Systems & Infrastructure); headline pattern: "Inference Engineer: LLM serving and GPU performance". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** inference, vLLM, SGLang, TensorRT-LLM, KV cache, latency, throughput, quantization, CUDA
- **Leave out or reframe:** TGI (archived 2026-03-21); the removed trtllm-build static engine path; single-process load generators
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-inference-engineer).

## Specialisations inside this role

- **Edge and on-device models** (L3 Inference and ML platforms): Candidate title: On-Device & Edge SLM Engineer, role catalog §5.3 (at least 9 live Edge AI Engineer aggregator listings plus Deepgram in Nov 2026 [C · T0-69 K13; ERRATA U38]; 0/16 in AI Product Engineer sample [T0-62]).
- **Quantisation and distillation** (L3 Inference and ML platforms): No title of its own in the catalog.
- **Disaggregated serving (prefill and decode)** (L3 Inference and ML platforms): No title of its own in the catalog.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [GPU Kernel / ML Compiler Engineer](gpu-kernel-engineer.md) (0.20); [Research Engineer / Member of Technical Staff](research-engineer.md) (0.18); [ML Platform / MLOps Engineer](ml-platform-engineer.md) (0.15).
- **Same family (AI Infrastructure & Platform):** [GPU Kernel / ML Compiler Engineer](gpu-kernel-engineer.md), [AI Infrastructure / GPU Platform Engineer](ai-infrastructure-engineer.md), [ML Platform / MLOps Engineer](ml-platform-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-inference-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-inference-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A November 2026 sample of 37 in-scope postings (from 56 examined; 8 opened in full on employer boards) shows that "Inference Engineer" covers **three distinct jobs** rather than one uniform C++/CUDA runtime profile [M · T0-56 L48–49, L62, L120–125]:

| Variant | Sample share | Typical employers | Distinguishing technical asks |
|---|---|---|---|
| **1. Engine and runtime performance** | 18/37 (49%) | OpenAI, xAI, NVIDIA, Amazon, Microsoft AI, Mistral, Sarvam AI, Baseten | Named serving engines (13/18), speculative decoding (10/18), CUDA/kernels (8/18), C++ (4/18), multi-node TP/PP/EP and disaggregated serving; **Kubernetes 0/18** |
| **2. Platform and serving fleet** | 9/37 (24%) | Anthropic (×3), Together AI, Red Hat, CoreWeave, Fluidstack, vCluster, General Compute | Large-scale distributed systems, KV-aware request routing (6/9), autoscaling (4/9), Kubernetes (6/9), Rust (5/9) or Go/Python |
| **3. Deployment and MLOps serving** | 10/37 (27%) | DigitalOcean, Gnani.ai, AION, Rackspace, Infosys, AIT Vienna, recruiter-posted | Production Kubernetes (6/10) with vLLM, SGLang, Dynamo or Triton operations, multi-tenant serving and latency/cost tuning |

**Skill shifts and tool churn that revise the Phase 0 scorecard:**
- **vLLM is the near-universal baseline; C++, PyTorch internals and Kubernetes are variant-specific:** Every posting that named a serving engine named **vLLM** (28/37, 76%), followed by **SGLang** (21/37, 57%) and **TensorRT-LLM** (15/37, 41%) [M · T0-56 L68, L196–199]. Distributed systems appears in 15/37 overall and **8 of 8 full-text reads** [M · T0-56 L68, L203]. By contrast, C++ appears in only 5/37 (14%; Anthropic, OpenAI and Together ask Python, Rust or Go), PyTorch internals in 4/37 (11%, mostly familiarity), and Kubernetes in 12/37 (32% overall, 0/18 in the runtime variant) [M · T0-56 L68, L205–208].
- **Core techniques and orchestration:** Continuous batching and KV-cache management is the most-named technique (18/37, 49%), ahead of speculative decoding (13/37, 35%; 10/18 runtime), quantisation (11/37, 30%), parallelism (9/37, 24%), KV-aware routing (8/37, 22%), disaggregated prefill/decode (6/37, 16%) and prefix caching (6/37, 16%) [M · T0-56 L69, L210–220]. Emerging multi-node orchestration layers **NVIDIA Dynamo** and **`llm-d`** appear in 8/37 postings (22%), and non-NVIDIA accelerators (AMD, TPU, Trainium, Gaudi, Cerebras, Groq) in 8/37 (22%) [M · T0-56 L69, L201, L224]. Specialisation shares across the sample: quantisation/distillation 32%, disaggregated serving 16%, edge/on-device 3% (Red Hat `llama.cpp`) [M · T0-56 L69, L319].
- **Confirmed tool retirements (live-verified 2026-11-19):** Hugging Face **TGI** entered maintenance mode and its GitHub repository was archived on 2026-03-21 (official recommendation: migrate to vLLM or SGLang), yet 4/37 postings (11%) still name it [A/B · T0-56 L72, L200]. **TensorRT-LLM** removed its legacy TensorRT `.engine` backend and `trtllm-build` workflow (PR #15767 merged 2026-07-02), leaving PyTorch as its sole execution backend [A/B · T0-56 L72, L199]. Never headline TGI or `trtllm-build` on a résumé [P · T0-56 L341–342].
- **Proof of work and résumé positioning:** Upstream open-source work is named in 11 of 37 postings (30%): NVIDIA asks for GitHub PR links, Sarvam asks for non-trivial code-path contributions, Inferact values public vLLM blogs or side projects, and Gnani treats upstream work as close to an expectation at senior level [B/M · T0-56 L70, L275]. Reviewers want concrete serving scoreboards — TTFT, TPOT, p99 latency with explicit request mix/load profile and cost per million tokens — rather than "deployed a model" or average latency [A/C/P · T0-56 L276, L333–345]. A standalone custom kernel without serving-system metrics is a weaker standalone proof than before given agentic kernel generation [C · T0-56 L278].

## Employer landscape and title confusion

**Employer mix and noisy counts (November 2026):** The 37-posting sample splits across AI-native and AI-cloud firms (14, 38%), frontier labs (7, 19%), Big Tech and silicon vendors (6, 16%), recruiter-posted listings (4, 11%), enterprise/open-source vendors (3, 8%), consultancies/managed services (2, 5%) and public research (1, 3%), with **0 GCC postings found** [M · T0-56 L64, L172–181]. Caution on aggregator volume: Inference Jobs displayed 341 "Inference Engineer" listings on 2026-11-13, but page 1 included postings up to two years old; only 5/20 (25%) were aged two months or less and 8/20 (40%) three months or less, implying roughly 65–210 active postings (wide 95% interval) [B/M · T0-56 L63, L151–153].

**Severe title noise and aliases:**
- **Classify by duties, never title:** On Together AI's Greenhouse board (78 open roles on 2026-11-13), at least 10 roles carried "Inference" in the title, yet **only 1 was an inference-engineering role** (4 were Kubernetes/compute provisioning, 2 reliability/SRE and 3 forward-deployed or support) [A/M · T0-56 L62, L154, L159]. Postings also drift under the same job ID: Anthropic job `5257650008` appeared as "Inference Runtime" in a search copy but read as "Inference Velocity" (developer productivity — excluded) when opened live on 2026-11-13 [A · T0-56 L432, L560].
- **Aliases to search (expanding K2):** Only 8 of 37 titles use "Inference Engineer" directly; 11 use `(Senior/Staff) Software Engineer, Inference / Model Inference / Inference Platform` [M · T0-56 L128–136]. Add *Performance Engineer, Inference* (Sarvam), *Research Engineer, Inference / Latency & Throughput* (Mistral), *Applied AI Engineer, Inference* (CoreWeave), *Forward Deployed Engineer (AI Inference)* (DigitalOcean), *LLMOps Engineer* (Gnani), *AI Model Serving Specialist* (Rackspace) and *Cloud Inference* (Anthropic) [M · T0-56 L137–145].
- **Boundary with GPU kernel engineering:** Although 11/37 postings (30%) mention CUDA or kernels (8/18 runtime), kernel authoring is a separate job family at Sarvam, Baseten, Together AI and Anthropic — Sarvam splits its vertical stack cleanly into Kernels (writes GPU code) and Inference (integrates it and owns system-level serving numbers) [A/B · T0-56 L116, L234].
- **Credentials:** **0 of 37 postings** name any certification [M · T0-56 L71, L285]. NVIDIA's `NCP-GENL` ($200, 120 min, 60–70 questions, 2-year validity) carried a "(Coming soon)" banner on its UK page as of 2026-10-30 alongside registration links, and its blueprint focuses predominantly on LLM design, training and fine-tuning rather than serving engines (Model Optimization 17%, GPU Acceleration 14%, Deployment 9%) [A · T0-56 L71, L282–284]. Skip certifications for this track; see [credential ROI](../../04-certifications/credential-roi.md).

## Career path, India demand and market signals

**Seniority and entry routes:** The role has **no direct entry-level track in the sample**: 0/37 postings are entry-level, 5 Staff+, 13 Senior and 19 level-unstated, with stated minimums of 3–6 years (median 5, `n = 9`) [M · T0-56 L66, L167]. Only 5/37 (14%) state a degree, all accepting equivalent experience, and 0 require a PhD [M · T0-56 L166]. The Phase 0 estimate that backend engineers reach Staff-level inference in 10–14 months (`K13`) is unverified — no transition-time source was found and postings ask for 5+ years [D · T0-56 L384].
- **Realistic routes:** Backend and platform engineers have the strongest path into platform/fleet and deployment variants (distributed systems appears in 8/8 full-text reads); DevOps/SRE engineers fit deployment/MLOps and reliability roles; PhDs fit research-engineer and runtime-performance tracks (Mistral) [M/D · T0-56 L291–293]. Candidates with under 3 years of experience should enter via backend/platform/SRE roles or customer-facing applied/forward-deployed inference roles (such as Baseten's Applied AI Inference listing) [C/D · T0-56 L82, L300].

**Progression, automation and durability:** IC ladders reach Staff+ (Anthropic) and Senior Principal (Red Hat), with exits into GPU kernel/performance engineering, research engineering, forward-deployed/solutions roles, engineering management (Baseten, Together) or founding (Inferact grew out of vLLM) [A/B · T0-56 L304–305]. On durability, **agentic kernel generation is moving into production**: Baseten's engineering blog reports latency cuts of 42.3% on Qwen-Image and 15.2% on FLUX.2 from its agentic kernel framework, Databricks reports its `Proteus` system generated kernels 1.8–5.2× faster than vLLM's best on a 122B model (while flagging reward-hacking risks), and FlashInfer-Bench provides a public benchmark [B for existence (live-confirmed 2026-11-19); C/COI for self-reported vendor outcomes · T0-56 L73, L308–311, L427]. Hand-writing routine kernels is the most exposed slice; system-level ownership (routing, scheduling, disaggregated serving, SLOs and correctness validation) remains the durable anchor [D · T0-56 L73, L88].

**Pay signals, geography and sponsorship:** Full pay tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). Across 14 date-clean US postings with disclosed bands, the median of posted base midpoints is **$288K** (IQR $261K–$344K; bounds $165K–$500K; sensitivity `n = 17` adding three ~3-month listings is $271K), led by frontier labs at **$388K** (`n = 4`: OpenAI $266K–$500K, Anthropic $300K–$485K and $320K–$485K [COI], xAI $180K–$440K), AI-native/cloud at $270K (`n = 7`) and Red Hat at $261K (`n = 2`) [M/A/B · T0-56 L67, L240–246, L254–255]. Europe shows wide employer-type dispersion: Anthropic London Staff posts £325K–£390K [A, COI], while AIT Vienna's public-research role starts at €66.6K gross [A] [T0-56 L247–248]. Levels.fyi carries no "Inference Engineer" title, and secondary blogs citing it conflict by over 2× and should be ignored [C · T0-56 L257]. Regionally, the sample is 54% US (20/37; 12 in California), 24% India (9/37), 14% Europe (5/37) and 8% remote/unknown, with only **4 of 37 (11%) remote-eligible** [M · T0-56 L65, L325–327]. On US sponsorship (pointers, not legal advice; verify in [visa and relocation](../../11-tracks/visa-and-relocation.md)): Anthropic explicitly sponsors (3 postings), General Compute explicitly does not (1), and 33 are silent; generic DOL LCA titles prevent isolating inference engineers [A/B · T0-56 L74, L328–329].

**India demand and nuance (revising Phase 0 "No India evidence"):** T0-56 finds **9 of 37 postings (24%) in India** (Bengaluru, Hyderabad, Gurugram) across AI startups (**Sarvam AI**, **Gnani.ai ×2**, **PrimaLabs**, **AION**), US cloud (**DigitalOcean ×2**), managed services (**Rackspace**) and a recruiter client (**Weekday**), all senior or 5+ years where stated [M/B · T0-56 L65, L361–362]. **No in-window GCC posting** was found (an NVIDIA India inference posting was removed on 2026-06-24; Together AI's India inference-titled role was Kubernetes provisioning) [A/B · T0-56 L187–188, L361, L396]. **Sarvam AI's `Performance Engineer, Inference`** (opened in full) is the clearest runtime-variant role in India, requiring source-level fluency in SGLang, vLLM, Dynamo or TensorRT-LLM, multi-node 100B+ serving, disaggregated prefill/decode, speculator training and on-call SLO ownership [A · T0-56 L366, L530]. India titles frequently surface as *LLMOps Engineer*, *AI Model Serving Specialist* or *Forward Deployed Engineer (AI Inference)* (with Indeed India reporting ~19× growth in forward-deployed postings from June 2025 to June 2026 — an adjacent competitor and on-ramp) [B · T0-56 L157, L363, L437]. Only 1 of 9 India postings discloses pay (₹24–36 LPA for 5+ years, dated 2026-07-29 [B]); for big-tech context, Levels.fyi Greater Bengaluru software-engineer medians at Google, NVIDIA and Qualcomm sit at ₹4.8M–₹6.9M TC [B] — see [pay benchmarks](../../09-compensation/pay-benchmarks.md) [T0-56 L249–252, L364].

## Interview themes and preparation notes

The generated card's **Infrastructure** track fits at Grade C with important additions by variant [C · T0-56 L271]:
- **Employer-reported stages and AI-tool rules:** Anthropic's live posting states that coding rounds mirror on-the-job work in the candidate's chosen language rather than LeetCode puzzles and requires acknowledging candidate AI-use guidance at application [A, COI · T0-56 L265]; one candidate recap describes a 4-round virtual onsite covering coding/optimisation, batching/KV-cache/scheduling design, and mission/safety [D · T0-56 L266]. Together AI prep guides report 4–5 rounds (algorithms coding, applied ML-systems coding, a 60-minute multi-model serving design round, and domain depth on batching, KV cache, speculative decoding and quantisation — note the guide states it is partly reasoned from postings) [C · T0-56 L267]. Baseten guides highlight designing a low-latency LLM API under bursty traffic with explicit batching, KV-cache and queueing trade-offs [C · T0-56 L268]. An older xAI copy notes technical-staff review without recruiters targeting a one-week process over Google Meet [B · T0-56 L269].
- **Track nuance by variant:** Evidence corroborates continuous batching, KV cache, disaggregated serving and request scheduling (including one AMD onsite report tracing a request through a paged-KV engine [D]), while no source directly named "decode roofline" or "KV-cache maths" as standalone prompts [C/D · T0-56 L271, L405]. Add **systems-language coding** (C++/Rust/Go and concurrency) for runtime roles and **distributed-systems design** (routing, autoscaling, multi-tenant traffic shaping) for platform roles [M/C · T0-56 L271]. Practise with the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack) and [interview loops](../../08-interviewing/interview-loops.md) (no model answers, per D-018). No India-specific interview evidence was found [E · T0-56 L365, L408].

## Dossier evidence and limits

- **Sample and access:** 37 in-scope postings (19 of 56 excluded), retrieved 2026-11-13 (anchor 2026-11-11, 90-day window from 2026-08-13). Only **8 of 37 (22%) were opened in full** on employer boards (Grade A); 29 were snippet-level (Grade B/C), so skill shares are lower bounds [M · T0-56 L48–49, L192]. Date evidence is mixed: 15 date-verified or opened live, 6 relative age only, 15 undated and 1 older than 90 days (Weekday client 2026-07-29, retained and flagged) [M · T0-56 L50, L163–164].
- **Classification, bias and COI:** Variant classification was single-rater; 4 borderline postings could shift variant shares by up to ~11 percentage points [T0-56 L425]. Search-surfaced English-only sampling under-samples hyperscaler internal boards and non-English markets [T0-56 L51, L424]. Anthropic is both model developer and employer in scope (3 included + 1 excluded posting, marked COI) [T0-56 L13, L438]. **Epistemic audit note:** T0-56 ledger rows S48 (Baseten blog) and S49 (Databricks blog) were graded A despite Extract-only access and vendor COI; live verification on 2026-11-19 confirms both posts exist (Grade B for existence) while keeping all speedup benchmarks at Grade C (COI, vendor self-reported).
- **Explicit absences (not measured as of 2026-11-13):** role-specific posting trend since January 2025; LinkedIn, Indeed, JobsPipe or Fast AI Jobs role-level aggregates; Levels.fyi inference-specific title; in-window India GCC postings and consultancies beyond Infosys; A-grade interview loops for OpenAI, NVIDIA, Baseten or Sarvam; Anthropic's full interview-time AI-policy page; exact-title LCA counts; named hiring-manager proof-of-work statements; published analyses of prior roles of hired engineers; RadixArk's posting from K3; transition-time data for K13; and India-specific interview loops [E · T0-56 L390–408].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
