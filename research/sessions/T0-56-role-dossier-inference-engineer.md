---
id: "T0-56"
title: "Role Dossier: Inference / LLM Serving Engineer"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-inference-engineer"
tags: ["role-dossier", "inference-engineer", "llm-serving", "job-postings", "india"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic, claude.ai chat with web search and fetch). Anthropic is also an employer in scope: ledger rows S1-S4 are marked COI."
evidence_window: "2025-06-01 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-56: Role Dossier: Inference / LLM Serving Engineer

S-numbers refer to rows in the Sources & Evidence Ledger. Grades follow EGP-1.0: A is a primary source I opened; B is a platform, mirror or snippet of a primary source; C is third-party analysis; D is memory, anecdote or judgement; M is my own calculation and inherits the weakest input; P is practice-curated. The brief fixes the research date at 2026-11-11, so the 90-day posting window opens 2026-08-13. Every source was retrieved on 2026-11-13, so every `seen` date is 2026-11-13. Requirement wording from postings is paraphrased, with at most one short quotation per source, to respect copyright limits.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | Most "inference engineer" postings are low-level GPU/runtime jobs where both Python and C++ are Must skills. | 70% | D |
| P2 | Posted US base for the role clusters around $250-300K, with frontier labs at $320-485K. | 65% | D |
| P3 | Entry-level postings under this title exist but are rare (under 10%). | 60% | D |
| P4 | vLLM is named in most postings and TGI is fading. | 75% | D |
| P5 | India has few inference-titled postings, concentrated in AI startups and multinational GCCs, and rarely posts pay. | 60% | D |
| P6 | Postings almost never name certifications. | 85% | D |

## Research Question

**Decision question.** What must the knowledge base say about the Inference / LLM Serving Engineer role so that a job seeker learns what the job is, what it pays, what skills and proof it needs, how it is interviewed, how careers progress, and where the jobs are? Door: two-way.

**Sub-questions.** Variants and aliases; demand and employer, seniority and remote mix; skills with shares; pay by region; interview loop; proof of work; credentials; entry routes; progression, durability and leverage; footprint and specialisations; geography and sponsorship; résumé signals; misconceptions; India.

**Reading of the brief.** "Inference engineer" is a noisy title, so I classified each posting by what it asks for.
- **Included:** the requirements centre on serving LLMs (or other generative models) in production. That covers engine/runtime performance, serving platform or fleet engineering, and deployment of serving stacks.
- **Excluded:** "inference" appears in the title but there is no serving content (provisioning, developer productivity, support, forward-deployed work without engine content), or the posting is outside the date window or not verifiably live.

**Method.**
- 26 web searches and 16 page fetches on 2026-11-13 (2 further fetches were refused because the URL had not appeared in results).
- The sample was drawn through a search engine and employer ATS boards (Greenhouse, Ashby, Lever, employer sites). Where a board page could not be fetched, I used aggregator mirrors.
- 56 postings were examined; 37 were included and 19 excluded (34%).
- **Access level:** 8 of the 37 were opened on the employer's own board (A). The other 29 are snippet-level (B or C).
- **Date evidence:** 15 have an explicit in-window date or were opened live, 6 carry only a relative age, 15 are undated, and 1 is older than 90 days but flagged.
- **Bias.** Search-engine sampling over-represents large English-language employers and aggregator-syndicated postings. It under-samples hyperscaler internal careers pages and all non-English markets, and it cannot reach LinkedIn or Indeed. Skill shares are lower bounds because absence from a snippet is not absence from the posting.
- **Falsification searches:**
  - C++ as a Must skill: disconfirmed.
  - Entry-level postings: none found.
  - TGI and `trtllm-build` as live practice: disconfirmed.
  - GCC postings: none found.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | "Inference" in a title covers three different jobs. Of 37 in-scope postings, 18 (49%) are engine/runtime-performance roles, 9 (24%) are platform/fleet roles and 10 (27%) are deployment/MLOps roles. At Together AI only 1 of at least 10 inference-titled postings is an inference-engineering job. | [S1][S5][S7][S8][S9][S61] | M |
| KF2 | One niche AI-infra board lists 341 "Inference Engineer" postings on 2026-11-13, but its page 1 includes postings up to two years old. About 40% of page-1 postings were 3 months old or less (n=20, wide interval). No role-specific time series was found. | [S18][S19] | B / M |
| KF3 | Employer mix (n=37): frontier labs 7, Big Tech/silicon 6, AI-native/AI-cloud 14, enterprise vendors 3, consultancy/managed services 2, recruiter-posted 4, public research 1. No GCC posting was found. | [S61] | M |
| KF4 | Regions (n=37): US 20 (12 list California), India 9, Europe 5, remote/unknown 3. Only 4 of 37 (11%) are remote-eligible. | [S61] | M |
| KF5 | No posting is explicitly entry-level. Staff or above 5, Senior 13, level unstated 19. Among 9 postings stating years, the minimum is 3-6 (median 5). | [S61] | M |
| KF6 | Posted US base: median of range midpoints $288K (IQR $261-344K, n=14). Adding three platform listings aged about three months gives $271K (n=17). Frontier-lab median is $388K (n=4). UK is £325-390K at Anthropic. An Austrian public research institute starts at €66.6K. India is posted at ₹24-36 LPA (n=1). | [S1][S2][S3][S5][S6][S13][S18][S38] | M (inputs A/B) |
| KF7 | Engines: vLLM is named in 28 of 37 (76%), SGLang 21 (57%), TensorRT-LLM 15 (41%), TGI 4 (11%). C++ appears in only 5 (14%), Python in 12 (32%) and distributed-systems experience in 15 (41%). Distributed systems appears in 8 of 8 full-text reads. Kubernetes appears in 12 (32%) but in 0 of 18 runtime-variant postings. | [S61] | M (lower bounds) |
| KF8 | Techniques: batching/KV cache 18 (49%), speculative decoding 13 (35%), quantisation 11 (30%), parallelism 9 (24%), disaggregated prefill/decode 6 (16%), prefix caching 6 (16%). Dynamo or llm-d is named in 8 (22%). Specialisation shares: quantisation/distillation 32%, disaggregated 16%, edge/on-device 3%. | [S61] | M (lower bounds) |
| KF9 | Upstream open-source work is named in 11 of 37 (30%). Postings ask for PR links, blogs and side projects, and outcome metrics (p99, tokens per day, cost per million tokens). | [S10][S26][S37][S61] | B / M |
| KF10 | No posting (0 of 37) names a certification. NVIDIA's NCP-GENL page exists but still carries a "(Coming soon)" label, and its blueprint centres on training and fine-tuning. | [S14][S61] | A / M |
| KF11 | TGI is in maintenance mode per Hugging Face docs, and the archive date comes from a single secondary source. TensorRT-LLM removed the TensorRT engine backend and `trtllm-build` (PR merged 2026-07-02). Postings still name TGI (11%) and TensorRT-LLM (41%). | [S15][S16][S17][S61] | B / C |
| KF12 | Employers report agents writing production kernels: Baseten latency -42.3% on one image model, Databricks kernels 1.8-5.2x faster than vLLM's best for a 122B model, and a public benchmark for AI-generated kernels. Hand kernel-writing is the most exposed task. System ownership (routing, scheduling, SLOs, validation) is less exposed. | [S48][S49][S50] | A (existence) / C (outcomes, COI) |
| KF13 | Anthropic states it sponsors visas. General Compute says sponsorship is not available. LCA filings cannot isolate the role because they use generic titles. | [S1][S2][S3][S30][S51] | A / B |
| KF14 | Employers describe the job as owning compute cost and speed. This is consistent with leverage 8.5 but is self-description. | [S2][S10] | C (COI for Anthropic) |

## Recommendation

| # | Decision rule for a job seeker | Why | Failure mode |
|---|---|---|---|
| R1 | Classify each posting before applying: runtime (C++/CUDA, speculative decoding, quantisation), platform/fleet (distributed systems, Rust/Go/Python, routing, autoscaling) or deployment/MLOps (Kubernetes plus vLLM operations). Keep one résumé variant per class. | KF1, KF7 | Single-rater classification may be wrong at the margins. A posting can change under the same job ID (see Discovered Concerns). |
| R2 | With under 3 years of relevant experience, do not expect an inference-titled posting. Build through backend/platform/SRE or ML-systems roles, or apply to applied, forward-deployed or research-engineer variants. | KF5: 0 of 37 entry-level, minimum years 3-6 | "Inference" in an adjacent title may mean fleet operations with little engine exposure. |
| R3 | Learn in this order: one engine to source level (vLLM first), KV-cache and batching accounting with SLO metrics, speculative decoding and quantisation. Then add the language for your variant (C++/CUDA/Triton, Rust/Go, or Python plus Kubernetes). Skip TGI and `trtllm-build`. | KF7, KF8, KF11 | Shares are lower bounds and engine popularity can shift. |
| R4 | Ship proof of work: a single-GPU serving study reporting percentile latency with load profile and cost per million tokens, plus a merged upstream PR on a non-trivial path. | KF9 | Typo-fix PRs read as noise. A study without a load profile reads as naive. |
| R5 | Anchor pay on posted ranges (US median about $270-290K; frontier labs about $390K). Treat Levels.fyi-citing blogs as unusable. | KF6, S57 | Posted ranges are not realised pay. Level and employer type are confounded. |
| R6 | For India, target AI startups, US cloud vendors and multinational engineering centres. Expect 5+ years and thin posted pay. Check remote eligibility. | KF4, KF5, India section | Many postings are anonymous recruiter listings or stale. |
| R7 | Skip certifications. | KF10 | A niche employer could value NVIDIA credentials. |
| R8 | Invest in system-level ownership and validation, not hand kernel-writing alone. | KF12 | Agent tooling could also automate more system work than the evidence shows. |

**What would change these rules.**
- A role-specific time series showing decline.
- An A-grade interview-loop source.
- Full-text reads that move skill shares by more than 15 points.
- LCA data by exact title.
- Evidence that agentic tooling changes headcount.

## Alternatives Considered

| Option | Verdict and reason |
|---|---|
| Use platform counts (341) as openings | Rejected. The page includes postings up to two years old. Used only as an upper bound. |
| Classify by title | Rejected. At Together AI only 1 of at least 10 inference-titled postings meets the definition. |
| Treat forward-deployed and support roles as the role | Rejected. They are adjacent routes, not the engineering role. |
| Compute shares only on the 8 full-text reads | Used as a cross-check only. n=8 is too small, but distributed systems appears in 8 of 8. |
| Use secondary blogs citing Levels.fyi for pay | Rejected. They disagree by more than 2x. Posted bands and Levels.fyi pages were used instead. |
| Use LCA data for sponsorship | Rejected for role-level use. Titles are generic. Used for employer-level context only. |
| Include a posting only if opened on the employer board | Rejected. It would leave n=8. The A/B split is reported instead. |

## Detailed Findings

### 1. Definition and variants

At 2026-11-13 the role is the job of making production generative-model serving fast, reliable and cost-efficient: scheduler, KV cache, batching, quantisation, speculative decoding, parallelism, routing and fleet efficiency.

Boundaries with adjacent roles:
- **Kernel work** is a separate family. Sarvam posts Inference and Kernels as a vertical stack: kernels authors the GPU code, inference integrates it and owns system-level numbers [S10]. Baseten, Together and Anthropic also list separate kernel or performance titles [S18][S20].
- **Research engineering** sits between inference and research at Mistral [S36].
- **SRE-type** "AI Inference Reliability Engineer" roles exist at Together AI [S8].

| Variant | n (share) | Typical employers | Distinguishing requirements |
|---|---|---|---|
| Engine/runtime-performance | 18 (49%) | OpenAI, xAI, NVIDIA, Amazon, Microsoft AI, Mistral, Sarvam, Baseten | Named engines in 13 of 18; speculative decoding in 10 of 18; CUDA/kernels in 8 of 18; C++ in 4 of 18; Kubernetes in 0 of 18 |
| Platform/fleet | 9 (24%) | Anthropic x3, Together, Red Hat, CoreWeave, Fluidstack, vCluster, General Compute | Distributed systems, routing, autoscaling; Kubernetes in 6 of 9; Rust in 5 of 9 |
| Deployment/MLOps | 10 (27%) | DigitalOcean, Gnani, AION, Rackspace, Infosys, AIT, recruiter-posted | Kubernetes plus vLLM or Triton operations; Kubernetes in 6 of 10 |

**Title groups in the sample (n=37).**

| Group | n | Examples |
|---|---|---|
| (Senior/Staff) Software Engineer, Inference / Model Inference / Inference Platform | 11 | Anthropic x3, OpenAI, Together, NVIDIA x2, Baseten, Fluidstack, DigitalOcean (Hyderabad), AION |
| Inference Engineer family (AI/LLM, Senior, Founding) | 8 | vCluster, General Compute, Zoox, Dice x2, FutureFit, Weekday client, PrimaLabs |
| Member of Technical Staff / Training-Inference | 4 | xAI, Inferact, Microsoft AI x2 |
| Machine Learning Engineer with inference focus | 4 | Red Hat x2, Amazon x2 |
| Performance / Research engineer | 3 | Sarvam, Mistral x2 |
| Applied, forward-deployed, LLMOps, platform | 7 | CoreWeave, DigitalOcean (Bengaluru), Gnani x2, Rackspace, Infosys, AIT |

The knowledge base's aliases mostly appear: "Inference Engineer", "Member of Technical Staff, Inference", "Model Performance Engineer" (Baseten), "Principal ML Engineer, llama.cpp" (Red Hat), and an "LLM Inference Optimization Engineer" title (Infosys). Aliases to add:
- Performance Engineer, Inference
- Research Engineer, Inference / Latency & Throughput
- Applied AI Engineer, Inference
- Forward Deployed Engineer (AI Inference)
- LLMOps Engineer
- AI Model Serving Specialist
- Software Engineer, Inference Platform
- Cloud Inference

### 2. Demand

| Measure | Value | Source and date | Grade |
|---|---|---|---|
| "Inference Engineer" category listings on Inference Jobs | 341 postings; includes postings up to 2 years old | [S18], 2026-11-13 | B |
| Same category in a search-index snapshot (date unknown) | 233 postings; 11 with salary data, middle 50% $138-322K | [S19] | B |
| Page-1 postings aged 2 months or less / 3 months or less | 5 of 20 (25%) / 8 of 20 (40%); about 20-150 / 65-210 of 341 at 95% | [S18], own calculation | M |
| Together AI board open roles | 78; at least 10 inference-titled (page 1 of 2); 1 in scope | [S8][S7][S9] | A / M |
| Baseten open roles (platform mirror) | 93 | [S20] | B |
| Role-specific trend since 2025-01 | Not found | Absences | E |
| Broader AI-engineer demand | LinkedIn "AI Engineer" +143% in 2025 (secondary); Indeed India forward-deployed postings about 19x from 2025-06 to 2026-06 | [S53][S52] | C / B |

Seniority mix (n=37): Staff or above 5, Senior 13, unstated 19, entry-level 0. Remote-eligible: 4 of 37 (11%). Together AI's 10 inference-titled postings split as: 1 in scope, 4 infrastructure-provisioning family, 2 reliability (SRE-type), 3 forward-deployed or support.

### 3. Job-description sample

- Included postings are in the Data Appendix as `jd` records. The Weekday client posting is dated 2026-07-29, 105 days before the research date. It is retained and flagged. Removing it changes no skill share by more than 3 points.
- Date evidence for the 37: opened live or explicitly dated in window 15; relative age only 6; undated 15; older than 90 days 1.
- Pay is disclosed in 14 of 37 postings (38%): 10 of 20 US, 2 of 5 Europe, 1 of 9 India, 1 of 3 remote/unknown.
- Degree is stated in 5 of 37 (14%); all five accept equivalent experience and none requires a PhD.
- Years are stated numerically in 9 of 37; minimums range 3-6 with a median of 5.
- No posting names a certification.

**Sample summary: employer type by region (n=37).**

| Employer type | US | Europe | India | Remote/unknown | Total |
|---|---|---|---|---|---|
| Frontier lab | 4 | 3 | 0 | 0 | 7 |
| Big Tech / silicon | 5 | 1 | 0 | 0 | 6 |
| AI-native / AI-cloud | 5 | 0 | 7 | 2 | 14 |
| Enterprise / open-source vendor | 3 | 0 | 0 | 0 | 3 |
| Consultancy / managed services | 1 | 0 | 1 | 0 | 2 |
| Recruiter-posted | 2 | 0 | 1 | 1 | 4 |
| Public research | 0 | 1 | 0 | 0 | 1 |
| Total | 20 | 5 | 9 | 3 | 37 |

**Exclusions (19 of 56 examined).**

| Reason | n | Items |
|---|---|---|
| Not this role or unclear | 8 | Anthropic Inference Velocity (developer productivity) [S4]; Together AI Inference/Compute Infrastructure, India (Kubernetes provisioning control plane) [S9]; Mistral Software Engineer, Performance (API and database performance) [S12]; Meta posting with unclear title; GSSTech Technology Engineer; Together AI forward-deployed (strategic inference); Together AI support engineer (inference), India; Capital One Distinguished Engineer [S58] |
| Outside window or not verifiable | 11 | Google GDC LLM serving (2026-05-08); Microsoft CoreAI Workload Engines (2026-04-08); Perplexity AI Inference Engineer (copy dated 2026-05-27); Fireworks LLM Infrastructure (2026-07-15); Prime Intellect Inference (2026-07-08); Talentiser (2026-06-11); Zinnov (2026-04-22); Majestic Labs (2026-06-15); NVIDIA Senior SWE AI Inference (one copy shows removal on 2026-06-24) [S21]; Hippocratic AI (March 2026 posting; the in-window listing had no usable text) [S43]; Together AI LLM Inference Frameworks (closed, redirected to the board) [S8] |

### 4. Skills

Shares are the count named in the available text of 37 postings. For 29 snippet-level postings they are lower bounds. The full-text subset is n=8 (Anthropic x3, OpenAI, xAI, Together, AIT, Sarvam).

| Skill (ID) | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| serving_engines | 28 (76%) | 37 | Must | Must | Absent mainly in platform/fleet roles at frontier labs |
| vllm | 28 (76%) | 37 | Must | Important | Every posting naming an engine named vLLM. The 3.9% in K11 is a different population (all AI-engineering postings, unverifiable) |
| sglang | 21 (57%) | 37 | Important | Important | Usually listed as "vLLM, SGLang or TensorRT-LLM" |
| trt_llm | 15 (41%) | 37 | Important | Important | PyTorch backend only; engine-build path removed [S15] |
| new:tgi | 4 (11%) | 37 | Avoid | leave out (K15) | Maintenance mode [S16][S17] |
| new:dynamo_llm_d | 8 (22%) | 37 | Should | none | Emerging orchestration layer |
| new:triton_inference_server | 5 (14%) | 37 | Optional | none | Enterprise and consultancy postings |
| system_design | 15 (41%); 8 of 8 full-text | 37 | Must | Must | Common denominator across variants |
| python | 12 (32%); 5 of 8 full-text | 37 | Must | Must | Not named in OpenAI, xAI or Sarvam full texts, which name C++/CUDA |
| cpp | 5 (14%); 2 of 8; 4 of 18 runtime | 37 | Important | Must | Demote. Anthropic, OpenAI and Together ask Python, Rust or Go |
| new:cuda_kernels | 11 (30%); 8 of 18 runtime | 37 | Important | none | Must for kernel-adjacent runtime roles |
| pytorch_internals | 4 (11%) | 37 | Should | Must | Mostly "familiarity"; only Inferact says internals |
| kubernetes | 12 (32%); 0 of 18 runtime | 37 | Important | Must | Must for platform and deployment variants |
| gpu_fundamentals | 9 (24%) | 37 | Must | Must | Hard to separate in snippets |
| batching_kv | 18 (49%) | 37 | Must | Important | Most-named technique |
| spec_decoding | 13 (35%); 10 of 18 runtime | 37 | Important | Important | Must for runtime variant |
| quantization | 11 (30%) | 37 | Important | Important | Confirmed |
| parallel_serving | 9 (24%) | 37 | Important | Important | Confirmed |
| load_testing | 9 (24%) | 37 | Important | Important | Sarvam names TTFT/TPOT/p99 and cost per million tokens as its scoreboard |
| profiling | 8 (22%) | 37 | Important | Important | Nsight, PyTorch profiler |
| cost_latency | 12 (32%) | 37 | Important | Important | Confirmed |
| prefix_caching | 6 (16%) | 37 | Should | Important | Demote |
| inference_autoscaling | 5 (14%); 4 of 9 platform | 37 | Should | Important | Important for platform |
| kv_aware_routing | 8 (22%); 6 of 9 platform | 37 | Should | Important | Important for platform |
| new:disaggregated_serving | 6 (16%) | 37 | Should | none | Appears in 2026 postings (Mistral, Sarvam, Amazon, NVIDIA) |
| new:upstream_oss_contributions | 11 (30%) | 37 | Important | none | Proof signal |
| new:rust | 8 (22%); 5 of 9 platform | 37 | Should | none | Platform variant |
| new:go | 6 (16%) | 37 | Optional | none | Platform and deployment |
| new:non_nvidia_accelerators | 8 (22%) | 37 | Should | none | AMD, TPU, Trainium, Gaudi |
| new:distillation | 4 (11%) | 37 | Optional | none | Speculator and draft training |
| new:edge_on_device | 1 (3%) | 37 | Optional | none | Red Hat llama.cpp |
| c3_ownership | on-call named in 1 | 37 | Important | Important | Not measurable from snippets |

**Robustness.** In the 15 date-verified postings the main skill shares stay within 15 points of the full-sample shares, except distributed systems (67% against 41%). That subset over-represents frontier-lab infrastructure roles.

**Probe: engines, techniques and kernel overlap.**
- vLLM, SGLang and TensorRT-LLM are the named engines.
- Speculative decoding is mainly a runtime-variant skill (10 of 18).
- CUDA or kernel work appears in 11 of 37 postings but is a separate job family at Sarvam, Baseten and Together.

### 5. Pay

| Population | Statistic | Component | n | Value | Date | Grade |
|---|---|---|---|---|---|---|
| US posted ranges, date-clean | Median of range midpoints | Base | 14 | $288K | 2026-11-13 | M |
| Same | p25-p75 | Base | 14 | $261-344K | 2026-11-13 | M |
| Same | Lowest lower bound / highest upper bound | Base | 14 | $165K / $500K | 2026-11-13 | M |
| Sensitivity: adds NVIDIA x2 and d-Matrix (about 3 months old) | Median; p25-p75 | Base | 17 | $271K; $252-328K | 2026-11-13 | M |
| Frontier labs (Anthropic x2, OpenAI, xAI) | Median midpoint | Base | 4 | $388K | 2026-11-13 | M |
| AI-native / AI-cloud | Median midpoint | Base | 7 | $270K | 2026-11-13 | M |
| Red Hat | Median midpoint | Base | 2 | $261K | 2026-11-13 | M |
| Anthropic London, Staff | Posted range | Base | 1 | £325-390K | 2026-11-13 | A |
| AIT Vienna, Senior | Starting salary | Base | 1 | €66,598 | 2026-11-13 | A |
| India, Weekday client, 5+ years | Posted range | Unspecified | 1 | ₹24-36 LPA | 2026-07-29 | B |
| Google SWE, Greater Bengaluru | Median | Total comp | n/a | ₹6.62M (L3 ₹4.07M to L7 ₹32.4M) | 2026-05-23 | B |
| NVIDIA SWE, Greater Bengaluru | Median | Total comp | n/a | ₹6.89M or ₹6.33M (two figures on one page) | 2026-04-05 | B |
| Qualcomm SWE, Greater Bengaluru | Median | Total comp | n/a | ₹5.04M or ₹4.84M (two figures) | 2026-03-10 | B |

- OpenAI's own page shows $266-500K at retrieval, while aggregator copies show $325-490K [S5].
- Anthropic's Staff/Senior ranges are $300-485K (Cloud Inference) and $320-485K (Inference Infrastructure) [S1][S2].
- A level split was not computed because level and employer type are confounded.
- Levels.fyi has no "inference engineer" title. Secondary blogs citing it disagree by more than 2x and are unusable [S57].
- Anthropic's LCA median offered wage across all titles is $209K [S51]. That population differs from the Staff/Senior postings and cannot be compared with them.
- K4's note that systems and research-engineering titles pay 13-31% more in two datasets could not be tested.

### 6. Interview loop

| Employer | Stages and assessments | AI-tool policy | Grade |
|---|---|---|---|
| Anthropic | Application form with an AI-use acknowledgement. Posting says coding interviews mirror on-the-job work, not LeetCode-style, in the candidate's chosen language | Acknowledgement of candidate AI guidance at application; interview-time rules not retrieved | A [S2] |
| Anthropic (one candidate) | Four-round virtual onsite: coding and optimisation, design discussion on batching, KV cache and scheduling, mission and safety | Not stated | D [S46] |
| Together AI | 4-5 rounds: two coding (algorithms; applied ML-systems), one 60-minute system design, domain discussion. The guide says it is partly reasoned from postings | Not stated | C [S45] |
| Baseten | Serve an LLM behind a low-latency API under bursty traffic and justify batching, KV-cache and queueing | Not stated | C [S45] |
| xAI | No recruiters; technical staff review applications; process aimed at one week; Google Meet interviews (older posting copy) | Not stated | B [S59] |

Track fit: K9's Infrastructure track fits at grade C. Evidence supports batching, KV cache, disaggregation and scheduling (also one AMD onsite question tracing a request through a paged-KV engine [S60], grade D, and an Anthropic batching design prompt [S47], grade C). It does not directly support "decode roofline" or "KV-cache maths" as named topics. Add systems-language coding (C++/Rust/Go, concurrency) for runtime roles and distributed-systems design for platform roles.

### 7. Proof of work

- **Open source.** 11 of 37 postings name upstream contributions. NVIDIA asks for PR links [S37]. Sarvam wants contributions on non-trivial code paths [S10]. Inferact wants shared blogs or side projects on vLLM [S26]. Gnani calls upstream work close to an expectation at senior level [S40]. A practitioner newsletter makes the same case, and a free learning site verifies that PRs are merged and are not typo fixes [S54].
- **Outcome metrics.** Sarvam wants concrete outcomes (tokens per day, throughput wins, p99 reductions) rather than "deployed a model" [S10]. A practitioner guide says reviewers read benchmarks critically and want percentile latency with the request mix [S55].
- **Public examples.** No named hiring manager writing in their own name was found. Public examples are the postings themselves.
- **Kernel proof.** A weaker signal, given agentic kernel generation [S48][S49].

### 8. Credentials

- NVIDIA NCP-GENL: professional level, 120 minutes, $200, 60-70 questions, valid two years, remotely proctored [S14].
- The page carries "(Coming soon)" at the top yet shows a register link and full details. Its metadata is dated 2026-10-30.
- Its blueprint is about designing, training and fine-tuning LLMs. Model Optimization is 17%, GPU Acceleration 14%, Model Deployment 9% and Production Monitoring 7%.
- No posting in the sample names a certification, and no employer statement about credentials for this role was found.

### 9. Entry routes and prerequisites

| Background | Route | Evidence | KB access | Suggested |
|---|---|---|---|---|
| Backend / platform | Platform/fleet or deployment variants; runtime needs C++/CUDA | Distributed systems in 8 of 8 full-text reads; Rust/Go/Python | 7 | 7 |
| DevOps / SRE | Deployment/MLOps and platform | Kubernetes and GPU operations in 12 postings; Together reliability titles | not scored | 6 |
| PhD research | Research-engineer and runtime variants | Mistral research-engineer roles; Red Hat lists a PhD as a plus; no posting requires one | 4.5 | 5 |
| Data scientist | Deployment/MLOps only | 5+ years typical | 2.5 | 2.5 |
| Front-end | No route evidenced | none | 2.5 | 2 |
| Non-technical | No route evidenced | none | 1 | 1 |
| Product manager | Adjacent product roles (inference platform PM at Baseten), not the engineer role | [S20] | not scored | 1 |
| New graduate | None of 37 is entry-level | [S61] | not scored | 1.5 |

Suggested scores are judgement (D). No published analysis of prior roles of people hired into the role was found. Customer-facing applied roles are the nearest lower-experience on-ramp: a Baseten "Applied AI Inference Engineer" listing on an aggregator carries a "less than 5 years" label and $120-160K with an asterisk (probably an estimate), date not established [S62], grade C.

### 10. Progression, durability and leverage

- **Ladders.** Senior, Staff and Staff+ individual-contributor titles at Anthropic; Principal and Senior Principal at Red Hat; engineering-manager roles at Baseten and Together [S20][S8].
- **Exits.** Kernel or performance engineering, research engineering, forward-deployed or solutions roles, engineering management, and founding (Inferact grew out of vLLM).
- **Durability.** Tooling churn is documented: TGI is in maintenance mode and TensorRT-LLM removed its engine-build path [S15][S16].
- **Automation.**
  - Baseten reports its agentic kernel framework cut latency 42.3% on Qwen-Image and 15.2% on FLUX.2 [S48].
  - Databricks reports generated kernels for a 122B model were 1.8-5.2x faster than vLLM's best [S49].
  - FlashInfer-Bench provides a public benchmark for AI-generated kernels [S50].
  - Value claims are COI; Databricks also flags reward-hacking pitfalls.
- **Leverage.** Anthropic's Cloud Inference posting calls its engineers "extremely high leverage" and ties them to revenue streams and compute cost [S2]. Sarvam says the team owns the numbers the company plans against [S10]. Both are self-descriptions.

### 11. Work footprint and specialisations

- All 37 postings sit in serving and infrastructure (L3).
- 8 (22%) name non-NVIDIA accelerators, which links to L1 hardware. NVIDIA (x2) and Amazon roles add chip- and cloud-vendor context.
- 2 touch post-training or RL serving (xAI and Mistral Inference Foundation).
- Specialisation shares (n=37, lower bounds): quantisation and distillation 12 (32%), disaggregated prefill/decode 6 (16%), edge and on-device 1 (3%).

### 12. Geography and sponsorship

| Item | Evidence | Grade |
|---|---|---|
| US cities | California 12 of 20 US-located; Seattle/Bellevue 2; Boston 3; Charlotte 2; unknown 1 | M |
| Europe | London, Paris, Warsaw, Munich, Dublin, Vienna; UK remote for NVIDIA | B |
| India | Bengaluru, Hyderabad, Gurugram | B |
| Sponsorship statements | Anthropic yes (3); General Compute no (1); silent in the rest (33 of 37) | A / B |
| LCA aggregators | Anthropic 292 certified H-1B LCAs (FY2025 to FY2026 Q3); Together 45 total; Baseten 12-29 depending on source and window. Titles are generic, so the role cannot be isolated | B / C |

### 13. Résumé and profile signals (practice-curated, P)

- **Headline.** Pair one named engine with an SLO metric, for example "LLM serving engineer: vLLM, TTFT/p99, cost per million tokens".
- **Keywords to mirror.** Continuous batching, KV cache, prefix caching, speculative decoding, FP8/AWQ/GPTQ, tensor/pipeline/expert parallelism, disaggregated prefill/decode, Nsight, Kubernetes, Rust/Go/C++.
- **Evidence-line patterns (placeholders, not achievements).**
  - "Reduced p99 TTFT from X to Y at Z requests per second on <model> and <GPU> using <technique>."
  - "Raised throughput by X% at fixed SLO with <batching or KV-cache change>."
  - "Cut cost per million tokens by X% via <quantisation or speculation>."
  - "Merged upstream PR to <engine> changing <scheduler, allocator or routing path>."
  - "Owned on-call for <serving SLO> across N incidents; led <postmortem change>."
- **Red flags.**
  - TGI or `trtllm-build` as a headline skill.
  - "Deployed a model" with no numbers.
  - Average latency with no percentiles or load profile.
  - Calling hosted APIs presented as inference engineering.

### 14. Misconceptions and risks

| Myth or risk | Evidence |
|---|---|
| Inference engineer means CUDA kernel author | CUDA/kernels in 30% of postings; kernels is a separate family at Sarvam and Baseten |
| C++ is always required | 5 of 37; the Anthropic, OpenAI and Together postings ask Python, Rust or Go |
| An "inference" title means LLM serving | 1 of at least 10 at Together AI |
| Using vLLM makes you an inference engineer | Sarvam wants source-level changes to scheduler, KV allocator or disaggregation path |
| Pay is uniformly $400K+ | Median about $270-288K; frontier labs about $388K; Austria starts at €66.6K; India posted ₹24-36 LPA |
| Aggregator counts equal openings | Page 1 includes postings up to two years old |
| Posting red flags | No pay shown; recruiter-anonymous client; contract W2; title and content mismatch; mirrors that add invented salary estimates |

### 15. India

- **Volume.** 9 of 37 postings (24%) are in India, plus Together's India roles, which are not inference engineering. No in-window GCC posting was found.
- **Employer mix.** AI startups (Sarvam, Gnani x2, PrimaLabs, AION), US cloud (DigitalOcean x2), managed services (Rackspace), recruiter client (Weekday). All are senior or 5+ years where stated.
- **Aliases.** LLMOps Engineer, AI Model Serving Specialist, Senior Technology Engineer, Forward Deployed Engineer (AI Inference).
- **Pay.** Posted pay appears in 1 of 9 (₹24-36 LPA). Levels.fyi software-engineer medians at Google, NVIDIA and Qualcomm Bengaluru are ₹4.8-6.9M total compensation [S44]. Context only (C): Interview Query reports a Bangalore ML-engineer median total compensation of about $61K (n=27), and Instahyre lists NVIDIA India bands rising from ₹35-55 LPA to ₹1.6-2.6 Cr with level labels not visible in the snippet [S56].
- **Interview.** No India-specific loop evidence was found.
- **Sarvam** is the clearest runtime-variant posting in India: it asks for source-level engine fluency, speculator training and disaggregated serving [S10].

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Definition and family | updated | Runtime variant matches; add platform/fleet (24%) and deployment/MLOps (27%) variants; volume measured on a niche board [S10][S7][S61] | M |
| K2 | Aliases | updated | Most confirmed; add Performance Engineer, Research Engineer, Applied, LLMOps and Serving Specialist titles [S61] | M |
| K3 | Demand evidence | updated | Named JDs confirmed at Anthropic, NVIDIA, Together, Baseten, Inferact, Red Hat; RadixArk not retrieved; 341 listings on one board [S18][S61] | B / M |
| K4 | Pay about $270K, range $150-485K | confirmed | Median of midpoints $271-288K; bounds $165-500K; the knowledge base's family-level figure from its own posting corpus is unverifiable [S1][S5][S18] | M |
| K5 | No India demand evidence | updated | 9 India postings in sample; no GCC found [S61] | M |
| K6 | No India pay evidence | updated | ₹24-36 LPA posted (n=1); Levels.fyi medians [S38][S44] | B |
| K7 | Durability judgement | unverifiable | Cited economics and tripwire untestable; kernel automation evidence [S48][S49] | D |
| K8 | Footprint L3, also L1 | confirmed | All 37 serving; 22% name non-NVIDIA accelerators [S61] | M |
| K9 | Infrastructure track | confirmed | Batching, KV cache, disaggregation in reports; add coding rounds [S45][S46][S60] | C |
| K10 | Must skills | updated | Promote vLLM; demote C++, PyTorch internals, Kubernetes to variant-specific [S61] | M |
| K11 | Important skills and shares | updated | Shares are for a different population; promote batching_kv; demote prefix caching, autoscaling, routing [S61] | M |
| K12 | NCP-GENL optional | confirmed | Page exists; "(Coming soon)"; 0 of 37 name it [S14][S61] | A / M |
| K13 | Backend to Staff in 10-14 months | unverifiable | No transition-time source; postings need 5+ years [S61] | D |
| K14 | Proof of work | confirmed | Upstream PRs and outcome metrics asked for; kernel proof weaker [S10][S37][S48] | B |
| K15 | Leave out TGI, trtllm-build, single-process load generators | confirmed | TGI maintenance and archive; engine-build path removed; load-generator claim untested [S15][S16][S17] | B / C |

## Absences

| Item | Where I looked |
|---|---|
| Role-specific posting trend since 2025-01 | Search for LinkedIn, Indeed, Lightcast, Robert Half and platform data; only AI-engineer aggregates found |
| LinkedIn and Indeed live counts | Not surfaced by search; not attempted behind login |
| JobsPipe and Fast AI Jobs role-level aggregates | Only job pages and company medians found |
| Levels.fyi inference-specific title | None; software-engineer and ML-engineer titles only |
| GCC postings | NVIDIA, Qualcomm, AMD, Microsoft, Google India; one NVIDIA India posting removed 2026-06-24 |
| Consultancy postings beyond Infosys | Accenture, Deloitte, TCS, Wipro, Cognizant searched |
| A-grade loops for OpenAI, NVIDIA, Baseten, Sarvam | Employer pages carry no loop detail |
| Anthropic candidate AI-guidance policy page | Not retrievable (URL had not appeared in results) |
| LCA filings by exact title | Aggregator pages searched; titles are generic |
| Named hiring-manager statements on proof of work | Postings and C-grade guides only |
| Prior roles of people hired into the role | No published analysis found |
| RadixArk posting named in K3 | Not retrieved |
| Non-English postings | Not searched (limitation) |
| Decode-roofline and KV-cache maths as named interview topics | No source |
| Transition-time evidence for K13 | None |
| Employer statements on credentials | None |
| India interview differences | None |

## Open Questions & Risks

- Skill shares are lower bounds, and 29 postings are snippet-level.
- Classification was done by a single rater.
- Date evidence is mixed: 15 verified, 6 relative-age, 15 undated, 1 older.
- Search-engine sampling bias is as described under Research Question.
- Posted pay is not realised pay.
- The trajectory of agentic automation is uncertain.

**Strongest objections an expert would raise, with the evidence found.**

| Objection | Evidence for and against |
|---|---|
| Snippet tallies understate and are not comparable to the knowledge base's own posting-corpus shares | For: true. Against: the 8 full-text reads and the 15 date-verified postings give broadly consistent shares |
| Hyperscaler inference engineers hide under generic titles | For: Google and Microsoft postings found were out of window. Against: cannot be tested without internal careers pages |
| The platform versus runtime split is subjective | Four borderline postings (CoreWeave, vCluster, General Compute, Zoox) shift variant shares by at most about 11 points |
| Posted bands overstate pay | For: Anthropic's LCA median wage is $209K across all titles. Against: different populations |
| Agents will shrink demand more than implied | For: employer reports of agent-written kernels. Against: validation remains the bottleneck and Databricks flags reward-hacking |
| A niche-board count is inflated | For: stale postings. Used only as an upper bound |

## Discovered Concerns

- **Posting volatility.** Anthropic job 5257650008 appeared as "Inference Runtime" in a search-index copy but as "Inference Velocity" (developer productivity) when opened on 2026-11-13 [S4]. The xAI board is branded SpaceXSI and retitled the posting [S6]. Store aliases with dates.
- **Aggregator staleness.** Inference Jobs lists postings up to two years old [S18].
- **NCP-GENL state.** It shows "(Coming soon)" yet publishes details [S14]. Recheck on a V2 cycle.
- **Content farms.** Some interview and salary sites mix speculation (one guide says it reasons from postings) or conflict on pay [S45][S57]. Do not use as loop evidence.
- **Invented estimates.** Some mirrors add invented salary estimates or misattribute employers (a Red Hat posting shown under "Red River").
- **Forward-deployed postings** are surging in India (Indeed, via IANS) and are an adjacent route and competitor [S52].
- **Anthropic is both author-developer and employer** in this dossier. COI is marked.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Low-level GPU/runtime jobs, C++ Must | Updated | Runtime variant is 49%; C++ named in 14% and Python in 32% | Demote C++ and PyTorch internals; classify by variant |
| P2 | Posted US base about $250-300K | Confirmed | Median $271-288K; frontier labs $388K | K4 stands |
| P3 | Entry-level rare | Updated | 0 of 37 entry-level; minimum years 3-6 | Early-career advice changes |
| P4 | vLLM majority; TGI fading | Confirmed | vLLM 76%; TGI 11%; TGI in maintenance mode | Promote vLLM; avoid TGI |
| P5 | India few, mostly startups and GCCs | Updated | 9 India postings (24%); startups and US cloud; no GCC found; pay posted in 1 of 9 | Fill K5 and K6 |
| P6 | Certifications unnamed | Confirmed | 0 of 37 | K12 Optional stands |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Staff + Senior SWE, Inference Infrastructure, Anthropic (Greenhouse API) https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5245851008 | 2026-06-08 (updated 2026-09-03) | 2026-11-13 | A | Read | COI | JD, pay, sponsorship |
| S2 | Staff / Senior SWE, Cloud Inference, Anthropic https://job-boards.greenhouse.io/anthropic/jobs/5107466008 | n/d | 2026-11-13 | A | Read | COI | JD, pay, interview, leverage |
| S3 | Staff SWE, Inference (London), Anthropic https://job-boards.greenhouse.io/anthropic/jobs/5097742008 | n/d | 2026-11-13 | A | Read | COI | JD, UK pay |
| S4 | Staff+ SWE, Inference Velocity, Anthropic https://job-boards.greenhouse.io/anthropic/jobs/5257650008 | n/d | 2026-11-13 | A | Read | COI | Exclusion, posting drift |
| S5 | SWE, Model Inference, OpenAI https://openai.com/careers/software-engineer-model-inference-san-francisco/ | n/d | 2026-11-13 | A | Read | | JD, pay |
| S6 | SWE Training/Inference (C++), xAI (SpaceXSI) https://job-boards.greenhouse.io/xai/jobs/4533894007 | n/d | 2026-11-13 | A | Read | | JD, pay, title drift |
| S7 | Senior Backend Engineer, Inference Platform, Together AI https://job-boards.greenhouse.io/togetherai/jobs/4835763007 | n/d | 2026-11-13 | A | Read | | JD, pay |
| S8 | Together AI board listing, 78 jobs https://job-boards.greenhouse.io/togetherai?error=true | 2026-11-13 | 2026-11-13 | A | Read | | Demand, title noise |
| S9 | Inference/Compute Infrastructure, India, Together AI https://job-boards.greenhouse.io/togetherai/jobs/5213325007 | n/d | 2026-11-13 | A | Read | | Exclusion |
| S10 | Performance Engineer, Inference, Sarvam AI https://www.sarvam.ai/careers/jobs/7d2faba2-21a1-4a8a-aff5-f708a6959195 | 2026-08-10 | 2026-11-13 | A | Read | | JD, India, proof |
| S11 | Sarvam posting copy, Khosla Ventures board https://jobs.khoslaventures.com/companies/sarvam-ai-2/jobs/89399732-performance-engineer-inference | 2026-08-10 | 2026-11-13 | B | Extract | | Posted date |
| S12 | Software Engineer, Performance, Mistral (Lever) https://jobs.lever.co/mistral/45e3045f-95d7-4200-bad5-3da0ad4b45d7 | n/d | 2026-11-13 | A | Read | | Exclusion |
| S13 | Senior AI Platform Engineer, AIT (Vienna) https://jobs.ait.ac.at/Job/273043 | n/d | 2026-11-13 | A | Read | | JD, EU pay |
| S14 | NVIDIA Generative AI LLMs Certification (NCP-GENL) https://www.nvidia.com/en-gb/learn/certification/generative-ai-llm-professional/ | 2026-10-30 (page metadata) | 2026-11-13 | A | Read | | Credential |
| S15 | TensorRT-LLM migration guide: TensorRT backend removed https://nvidia.github.io/TensorRT-LLM/legacy/tensorrt-backend-removal.html ; https://github.com/NVIDIA/TensorRT-LLM/pull/15767 | 2026-07-02 | 2026-11-13 | B | Extract | corroborated | K15 |
| S16 | Text Generation Inference docs, Hugging Face https://huggingface.co/docs/text-generation-inference/en/index.md | n/d | 2026-11-13 | B | Extract | | K15 |
| S17 | TGI vs vLLM benchmark (archive date 2026-03-21), markaicode https://markaicode.com/benchmarks/hugging-face-llama-33-a100-80gb-latency-benchmark/ | 2026 | 2026-11-13 | C | Extract | single-source | K15 |
| S18 | "Inference Engineer" jobs, Inference Jobs https://www.inferencejobs.com/jobs/inference-engineer | 2026-11-13 | 2026-11-13 | B | Read | | Demand, platform pay |
| S19 | Same page, search-index snapshot https://www.inferencejobs.com/jobs/inference-engineer | n/d | 2026-11-13 | B | Extract | | Count 233, pay summary |
| S20 | Baseten company page, Inference Jobs https://www.inferencejobs.com/companies/baseten | 2026-11-13 | 2026-11-13 | B | Read | | Demand |
| S21 | NVIDIA Senior SWE, AI Inference (JR2016392), Built In https://builtin.com/job/senior-software-engineer-ai-inference/9050456 | n/d | 2026-11-13 | B | Extract | | Exclusion (one copy shows removal 2026-06-24) |
| S22 | NVIDIA Agentic Inference, Dynamo, RemoWork https://remowork.life/jobs/6a684b42e681430a6b604edf/senior-system-software-engineer-agentic-inference-dynamo | 2026-07-27 (reposted 2026-10-31) | 2026-11-13 | B | Extract | | JD |
| S23 | Baseten SWE Inference Performance, Built In Seattle https://www.builtinseattle.com/job/software-engineer-inference-performance/11515772 | n/d | 2026-11-13 | B | Extract | | JD |
| S24 | Red Hat Distributed vLLM; llama.cpp, Built In https://builtin.com/job/principal-machine-learning-engineer/8257026 ; https://builtin.com/job/principal-senior-principal-machine-learning-engineer-llama-cpp/7149298 | n/d | 2026-11-13 | B | Extract | | JD |
| S25 | Amazon MLE II and SageMaker AI Inference, AnitaB boards https://jobs.anitab.org/companies/amazon-3-60ad394d-c673-4474-9694-344b0cae748f/jobs/98033381-machine-learning-engineer-ii-aws-inference-optimization | 2026-10-25; 2026-10-29 | 2026-11-13 | B | Extract | | JD |
| S26 | Inferact MTS Inference, startup.jobs https://startup.jobs/member-of-technical-staff-inference-inferact-8280046 | n/d | 2026-11-13 | B | Extract | | JD, proof |
| S27 | CoreWeave Applied AI Engineer, Inference, Teal https://www.tealhq.com/job/applied-ai-engineer-inference_7ea1aee85e9e6a26c816f9ff9d17641495a36 | n/d | 2026-11-13 | B | Extract | | JD |
| S28 | Fluidstack SWE Inference Platform, jobboardly https://it-jobs-near-me.jobboardly.com/jobs/software-engineer-inference-platform-a8fea23e | n/d | 2026-11-13 | B | Extract | | JD |
| S29 | vCluster Senior Inference Engineer, Built In https://www.builtinboston.com/job/senior-inference-engineer/10631066 | n/d | 2026-11-13 | B | Extract | | JD |
| S30 | General Compute Founding Inference Engineer, Wellfound https://wellfound.com/jobs/4817884-inference-engineer | n/d | 2026-11-13 | B | Extract | | JD, sponsorship |
| S31 | Microsoft AI MTS LLM Inference; Senior ML Engineer https://microsoft.ai/job/member-of-technical-staff-llm-inference | n/d | 2026-11-13 | B | Extract | | JD |
| S32 | Zoox AI Inference Engineer, hotfix.jobs https://hotfix.jobs/jobs/ai-inference-engineer-model-optimization-deployment-at-zoox-98f84382-a376-49eb-ab15-fc95bdd56e3f | n/d | 2026-11-13 | B | Extract | | JD |
| S33 | Infosys LLM Inference Optimization Engineer, The Ladders https://www.theladders.com/job/genai-platform-llm-inference-optimization-engineer-cloud-infosyslimiteddigital-charlotte-nc_87331729 | n/d | 2026-11-13 | C | Extract | | JD |
| S34 | Dice contract postings (San Jose; Charlotte) https://www.dice.com/job-detail/e4872a74-a68b-49a0-9c67-0e9d12cc5126 ; https://dice.com/job-detail/cd8d5273-a49c-4d0a-941b-42963aac15a5 | n/d | 2026-11-13 | B | Extract | | JD |
| S35 | FutureFit AI Inference Engineer, remotejobs.org https://remotejobs.org/remote-jobs/ai-inference-engineer-futurefit-ai | n/d | 2026-11-13 | C | Extract | | JD |
| S36 | Mistral Research Engineer postings, General Catalyst board https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/96101264-research-engineer-inference-foundation ; https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/97523312-research-engineer-latency-throughput | 2026-10-06; 2026-10-20 | 2026-11-13 | B | Extract | | JD |
| S37 | NVIDIA Senior SWE AI Inference Systems (UK/Dublin), Built In https://builtinbristol.uk/job/senior-software-engineer-ai-inference-systems/9221782 | n/d | 2026-11-13 | B | Extract | | JD, proof |
| S38 | Weekday client Inference Engineer, Workable https://apply.workable.com/weekday-1/jobs/view/A44098974C.md | 2026-07-29 | 2026-11-13 | B | Extract | | JD, India pay |
| S39 | DigitalOcean forward-deployed and inference services (India), Built In https://builtinbengaluru.in/job/senior-forward-deployed-engineer-i-ai-inference/10521962 ; https://builtinpune.in/job/senior-engineer-i-inference-services/8570880 | n/d | 2026-11-13 | B | Extract | | JD |
| S40 | Gnani.ai LLMOps postings, hirist https://www.hirist.tech/j/gnani-ai-llmops-engineer-1677460 ; https://www.hirist.tech/j/gnaniai-senior-llmops-engineer-1672372 | 2026-09-17; 2026-10-08 | 2026-11-13 | B | Extract | | JD, proof |
| S41 | PrimaLabs and AION postings, Weekday board and echojobs https://jobs.weekday.works/sr-inference-engineer-llm-at-primalabs-4416492368 ; https://echojobs.io/job/aion-senior-software-engineer-inference-platform-56bbr | n/d | 2026-11-13 | B | Extract | | JD |
| S42 | Rackspace AI Model Serving Specialist, resumegeni mirror https://resumegeni.com/jobs/ai-model-serving-specialist-at-rackspace-india-remote | n/d | 2026-11-13 | C | Extract | | JD |
| S43 | Hippocratic AI LLM Inference Engineer, General Catalyst board https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/70320201-llm-inference-engineer | 2026-03-13 | 2026-11-13 | B | Extract | | Exclusion |
| S44 | Levels.fyi software-engineer salaries, Greater Bengaluru (Google, NVIDIA, Qualcomm) https://www.levels.fyi/companies/google/salaries/software-engineer/locations/greater-bengaluru.md ; https://www.levels.fyi/en-gb/companies/nvidia/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/no-no/companies/qualcomm/salaries/software-engineer/locations/greater-bengaluru | 2026-03-10 to 2026-05-23 | 2026-11-13 | B | Extract | | India pay |
| S45 | Interview guides, techinterview.org https://www.techinterview.org/companies/together-ai/ ; https://www.techinterview.org/companies/baseten-interview-guide/ | 2026 | 2026-11-13 | C | Extract | | Loops |
| S46 | Anthropic interview recaps, dev.to https://dev.to/interview-aid/anthropic-sde-interview-recap-2026-hiring-process-real-experience-offer-received-431 | 2026 | 2026-11-13 | D | Extract | single-source | Loops |
| S47 | AI engineer interview questions, Exponent https://www.tryexponent.com/blog/ai-engineer-interview-questions | 2026 | 2026-11-13 | C | Extract | | Loops |
| S48 | Agentic kernels in production, Baseten blog https://www.baseten.co/blog/agentic-kernels-in-production/ | 2026 | 2026-11-13 | A | Extract | COI | Durability |
| S49 | Specialised GPU kernel generation, Databricks blog https://www.databricks.com/en/blog/achieving-extreme-efficiency-through-specialized-gpu-kernel-generation | 2026 | 2026-11-13 | A | Extract | COI | Durability |
| S50 | FlashInfer-Bench, arXiv 2601.00227 https://arxiv.org/html/2601.00227 | 2026-01 | 2026-11-13 | B | Extract | | Durability |
| S51 | LCA aggregator pages (careery.pro, froghire, Ellis, myvisajobs) https://careery.pro/h1b-sponsors/anthropic-pbc ; https://www.froghire.ai/company/together ; https://www.ellis.com/visa-sponsors/baseten-labs-inc/h1b ; https://www.myvisajobs.com/employer/baseten-labs/ | 2026 | 2026-11-13 | B | Extract | single-source | Sponsorship |
| S52 | India forward-deployed postings, Indeed via IANS https://ianslive.in/indias-forward-deployed-engineer-job-postings-surge-19-fold-report--20261014115304 | 2026-10-14 | 2026-11-13 | B | Extract | | Discovered concerns |
| S53 | Fastest growing AI roles, HeroHunt https://herohunt.ai/blog/fastest-growing-ai-roles-in-2026-data-and-rankings | 2026 | 2026-11-13 | C | Extract | | Trend (broad) |
| S54 | Open-source route, Machine Learning At Scale; InferQuest https://machinelearningatscale.substack.com/p/how-to-break-into-mlsys-through-open ; https://inferquest.org/ | 2026 | 2026-11-13 | C | Extract | | Proof |
| S55 | AI Inference Engineer guide, Second Talent https://www.secondtalent.com/occupations/ai-inference-engineer/ | 2026 | 2026-11-13 | C | Extract | | Résumé, proof |
| S56 | India salary pages, Instahyre and Interview Query https://resources.instahyre.com/blog/ai-engineer-salary-in-india/ ; https://interviewquery.com/salaries/machine-learning-engineer-salary-in-bangalore-india | 2026 | 2026-11-13 | C | Extract | | India pay (context) |
| S57 | Secondary blogs citing Levels.fyi https://letsdatascience.com/blog/the-56-premium-what-ai-skills-actually-pay-in-2026 | 2026 | 2026-11-13 | C | Extract | conflicting | Pay (rejected) |
| S58 | Excluded-posting evidence (Capital One, Meta, GSSTech) https://www.tealhq.com/job/distinguished-engineer_7ea1aeeac2da5157c900fabc0321670c3d0b1 ; https://www.choppingblock.ai/jobs/software-engineer-llvm-compiler-mtia-at-meta ; https://apply.workable.com/gsstech-group/jobs/view/B75CDB70DD.md | n/d | 2026-11-13 | B | Extract | | Exclusions |
| S59 | xAI posting copy with process statement, Built In https://builtin.com/job/ai-engineer-researcher-inference/3365055 | n/d | 2026-11-13 | B | Extract | | Loop |
| S60 | AMD interview question, PracHub https://prachub.com/interview-questions/trace-an-llm-request-through-a-paged-kv-inference-engine | 2026-09-14 | 2026-11-13 | D | Extract | single-source | Loop |
| S61 | Own JD sample, n=37 (compiled from S1-S3, S5-S7, S10, S13, S22-S42) | 2026-11-13 | 2026-11-13 | M | n/a | own calculation | All shares and sample tables |
| S62 | Applied AI Inference Engineer, Baseten, The Ladders https://www.theladders.com/job/applied-ai-inference-engineer-baseten-san-francisco-ca_83163754 | n/d | 2026-11-13 | C | Extract | | Entry-route context |

## Data Appendix

Block 1 holds the `jd` records: 37 included postings followed by 3 excluded postings that I opened (marked `role: null`). Block 2 holds all other record types.

```jsonl
{"type":"jd","grade":"A","src":["S1"],"as_of":"2026-09-03","ttl":"V1","role":"inference-engineer","employer":"Anthropic","title":"Staff + Senior Software Engineer, Inference Infrastructure","url":"https://job-boards.greenhouse.io/anthropic/jobs/5245851008","job_id":"5245851008","seen":"2026-11-13","location":"San Francisco, CA; New York City, NY; Seattle, WA","remote":"hybrid (office at least 25% of time)","seniority":"Senior/Staff","degree":"Bachelor's or equivalent experience","must":["significant software engineering experience, particularly distributed systems","bias towards flexibility and impact","desire to learn ML systems and infrastructure"],"nice":["high-performance distributed systems","ML systems at scale","request routing and load balancing","LLM inference batching and caching","Kubernetes and cloud","Python or Rust"],"pay":{"lo":320000,"hi":485000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"req PIP-262856; first published 2026-06-08; updated 2026-09-03; title differed in an earlier index copy; COI; duties include autoscaling, capacity management and compute-efficiency work"}
{"type":"jd","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Anthropic","title":"Staff / Senior Software Engineer, Cloud Inference","url":"https://job-boards.greenhouse.io/anthropic/jobs/5107466008","job_id":"5107466008","seen":"2026-11-13","location":"San Francisco, CA; Seattle, WA","remote":"hybrid (office at least 25% of time)","seniority":"Senior/Staff","degree":"Bachelor's in a related field or equivalent experience","must":["significant experience in high-performance, large-scale distributed systems","services on AWS, GCP or Azure with Kubernetes or IaC exposure","“strong interest in inference”"],"nice":["LLM inference optimisation, batching, caching and serving strategies","GPUs, TPUs or Trainium","cost optimisation and capacity management","CI/CD for deployment and validation","Python or Rust"],"pay":{"lo":300000,"hi":485000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"posting date not shown; live when opened; states coding interviews are not LeetCode-style; COI; duties include request routing, autoscaling and capacity planning"}
{"type":"jd","grade":"A","src":["S5"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"OpenAI","title":"Software Engineer, Model Inference","url":"https://openai.com/careers/software-engineer-model-inference-san-francisco/","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA","remote":null,"seniority":"unstated (mid/senior)","years":5,"degree":null,"must":["at least 5 years professional software engineering","understanding of ML architectures and inference optimisation","production distributed systems experience","PyTorch, NVIDIA GPUs, NCCL/CUDA and HPC networking (InfiniBand, MPI, NVLink), or quick ramp-up"],"nice":["performance-critical distributed systems"],"pay":{"lo":266000,"hi":500000,"currency":"USD","period":"year"},"ats":"Ashby (per aggregator)","note":"employer page shows $266K-$500K plus equity; aggregator copies show $325K-$490K; no posting date on page; duties centre on performance, latency and throughput efficiency of inference"}
{"type":"jd","grade":"A","src":["S6"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"xAI (board branded SpaceXSI)","title":"Software Engineer - Training/Inference (C++)","url":"https://job-boards.greenhouse.io/xai/jobs/4533894007","job_id":"4533894007","seen":"2026-11-13","location":"Palo Alto, CA; Seattle, WA","remote":null,"seniority":"unstated","must":["low-level systems programming in C/C++ or Rust","large-scale high-concurrency production serving","GPU inference engines (vLLM, SGLang, Triton, TensorRT-LLM)","batching, caching, load balancing, parallelism","GPU kernels and code generation","quantisation, speculative decoding, distillation, low-precision numerics","benchmarking and reliability testing; CI/CD for inference"],"nice":[],"pay":{"lo":180000,"hi":440000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"aggregator copies carry the title Member of Technical Staff - Inference; title rewritten after board rebrand; skills list also names auto-scaling and latency and throughput targets; distributed inference infrastructure"}
{"type":"jd","grade":"A","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Together AI","title":"Senior Backend Engineer, Inference Platform","url":"https://job-boards.greenhouse.io/togetherai/jobs/4835763007","job_id":"4835763007","seen":"2026-11-13","location":"San Francisco, CA","remote":"hybrid (three days a week in office)","seniority":"Senior","years":5,"degree":"Bachelor's or Master's in CS/CE or equivalent practical experience","must":["5+ years building large-scale fault-tolerant distributed systems and API microservices","low-level OS concepts: threads, memory, networking, storage","expert Rust, Go, Python or TypeScript"],"nice":["LLM serving knowledge","SGLang, vLLM or NVIDIA Dynamo","Kubernetes","CUDA, Triton, NCCL, InfiniBand, NVLink, MPI"],"pay":{"lo":200000,"hi":290000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"duties: request routing, autoscaling, multi-tenant traffic shaping, prefix caching; valued: profiling system-level performance, latency and throughput trade-offs, open-source inference ecosystem"}
{"type":"jd","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Anthropic","title":"Staff Software Engineer, Inference","url":"https://job-boards.greenhouse.io/anthropic/jobs/5097742008","job_id":"5097742008","seen":"2026-11-13","location":"London, UK","remote":"hybrid (office at least 25% of time)","seniority":"Staff","degree":"Bachelor's or equivalent experience","must":["Python or Rust","building and operating distributed systems in production","Kubernetes and one major cloud"],"nice":["high-performance distributed systems","ML systems at scale","load balancing and request routing","LLM inference optimisation, batching, caching","AI accelerators (GPUs, TPUs, emerging hardware)"],"pay":{"lo":325000,"hi":390000,"currency":"GBP","period":"year"},"ats":"Greenhouse","note":"states visa sponsorship is offered; COI; duties include autoscaling and compute-efficiency work"}
{"type":"jd","grade":"A","src":["S13"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"AIT Austrian Institute of Technology (AI Factory Austria)","title":"Senior AI Platform Engineer (f/m/d)","url":"https://jobs.ait.ac.at/Job/273043","job_id":"273043","seen":"2026-11-13","location":"Vienna, Austria","remote":"flexible on-site and remote","seniority":"Senior","years":"5-7 (at least 2 on ML/AI platforms)","degree":"CS or related, or equivalent professional experience","must":["Kubernetes in production and scalable distributed systems and APIs","LLM and model serving with inference optimisation (e.g. vLLM, Triton)","strong Python","GPU workloads, IaC, GitOps, CI/CD"],"nice":["HPC and SLURM","PEFT and distributed training","multi-tenant platforms with metering","Go"],"pay":{"lo":66598,"hi":null,"currency":"EUR","period":"year"},"note":"annual gross starting salary under the non-university research collective agreement; fixed term to June 2028; deployment variant"}
{"type":"jd","grade":"A","src":["S10","S11"],"as_of":"2026-08-10","ttl":"V1","role":"inference-engineer","employer":"Sarvam AI","title":"Performance Engineer, Inference","url":"https://www.sarvam.ai/careers/jobs/7d2faba2-21a1-4a8a-aff5-f708a6959195","job_id":"7d2faba2-21a1-4a8a-aff5-f708a6959195","seen":"2026-11-13","location":"Bengaluru; Chennai","remote":"on-site","seniority":"Senior","years":5,"degree":null,"must":["5+ years ML systems, 2+ on production inference serving","100B+ parameter serving with multi-node TP/PP/EP","source-level fluency in SGLang, vLLM, Dynamo or TensorRT-LLM","disaggregated prefill-decode, distributed KV transfer, cross-node routing","building and training speculators","KV cache internals; NCCL; MIG/MPS","Nsight Systems profiling; C++ and CUDA at read-and-modify level","on-call ownership of an inference SLO","scoreboard of TTFT, TPOT and cost per million tokens; prefix sharing"],"nice":["upstream contributions on non-trivial paths","Dynamo or llm-d at scale","forked runtime in production","MoE, long-context, Indic workloads"],"ats":"Ashby","note":"no pay shown; paired with a separate Kernels posting; posted date from S11"}
{"type":"jd","grade":"B","src":["S22"],"as_of":"2026-10-31","ttl":"V1","role":"inference-engineer","employer":"NVIDIA","title":"Senior System Software Engineer, Agentic Inference - Dynamo","url":"https://remowork.life/jobs/6a684b42e681430a6b604edf/senior-system-software-engineer-agentic-inference-dynamo","job_id":null,"seen":"2026-11-13","location":"United States","remote":null,"seniority":"Senior","must":["open-source software serving inference of trained models on GPUs","disaggregated serving across Dynamo-supported engines (vLLM, SGLang, TRT-LLM)","distributed inference frontend with day-0 model support"],"nice":["contributions to open-source inference frameworks","GPU memory, KV and prefix cache optimisation for long-context reasoning"],"pay":{"lo":224000,"hi":431250,"currency":"USD","period":"year"},"ats":"Workday (per aggregator link)","note":"posted 2026-07-27, reposted 2026-10-31 per aggregator; employer page not opened"}
{"type":"jd","grade":"B","src":["S23"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Baseten","title":"Software Engineer - Inference Performance","url":"https://www.builtinseattle.com/job/software-engineer-inference-performance/11515772","job_id":null,"seen":"2026-11-13","location":"Seattle, WA","remote":"hybrid","seniority":"unstated (aggregator label entry level is unreliable)","must":["implement and productionise inference techniques working in runtime internals"],"nice":["project examples: agentic kernels, draft-model training for speculative decoding"],"pay":{"lo":180000,"hi":360000,"currency":"USD","period":"year"},"ats":"Ashby (per aggregators)","note":"listed as six days old on an undated snapshot"}
{"type":"jd","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Red Hat (IBM)","title":"Principal Machine Learning Engineer, Distributed vLLM","url":"https://builtin.com/job/principal-machine-learning-engineer/8257026","job_id":null,"seen":"2026-11-13","location":"Boston, MA","remote":"in-office (one copy lists remote)","seniority":"Principal","must":["Python, Go and Rust or C","Kubernetes APIs, operators and Gateway API inference extension (request routing)","gRPC and HTTP/2"],"nice":["llm-d","leading an upstream open-source community"],"pay":{"lo":190000,"hi":313000,"currency":"USD","period":"year"},"note":"listed as reposted hours earlier on an undated snapshot"}
{"type":"jd","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Red Hat (IBM)","title":"Principal/Senior Principal Machine Learning Engineer, llama.cpp","url":"https://builtin.com/job/principal-senior-principal-machine-learning-engineer-llama-cpp/7149298","job_id":null,"seen":"2026-11-13","location":"Boston, MA","remote":"in-office","seniority":"Principal/Senior Principal","must":["strong ML fundamentals and transformer/LLM inference understanding","performance profiling, benchmarking and optimisation","Python"],"nice":["C++ with CUDA, Metal, SYCL, Vulkan backends","quantisation"],"pay":{"lo":190000,"hi":351000,"currency":"USD","period":"year"},"note":"edge/local-inference specialisation; listed as reposted days earlier on an undated snapshot; upstream llama.cpp community work"}
{"type":"jd","grade":"B","src":["S25"],"as_of":"2026-10-25","ttl":"V1","role":"inference-engineer","employer":"Amazon (AWS)","title":"Machine Learning Engineer II, AWS Inference Optimization","url":"https://jobs.anitab.org/companies/amazon-3-60ad394d-c673-4474-9694-344b0cae748f/jobs/98033381-machine-learning-engineer-ii-aws-inference-optimization","job_id":null,"seen":"2026-11-13","location":"Santa Clara, CA","remote":null,"seniority":"Mid (MLE II)","must":["inference stacks such as vLLM and SGLang","speculative decoding, disaggregated inference, CUDA kernel tuning","price-performance of LLM inference on SageMaker, HyperPod, Bedrock"],"nice":[],"note":"mirror of employer posting; mirror id 98033381; pay not shown"}
{"type":"jd","grade":"B","src":["S25"],"as_of":"2026-10-29","ttl":"V1","role":"inference-engineer","employer":"Amazon (SageMaker AI)","title":"Machine Learning Engineer, SageMaker AI Inference","url":"https://jobs.anitab.org/companies/amazon-3-60ad394d-c673-4474-9694-344b0cae748f/jobs/98367335-machine-learning-engineer-sagemaker-ai-inference","job_id":null,"seen":"2026-11-13","location":"Bellevue, WA","remote":null,"seniority":"unstated","must":["kernel-level optimisation and inference pipeline improvements for LLM serving latency and throughput"],"nice":[],"note":"mirror id 98367335; pay not shown"}
{"type":"jd","grade":"B","src":["S26"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Inferact","title":"Member of Technical Staff, Inference","url":"https://startup.jobs/member-of-technical-staff-inference-inferact-8280046","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA (also a Singapore listing)","remote":null,"seniority":"unstated","must":["strong Python with PyTorch internals","LLM inference systems (vLLM, TensorRT-LLM, SGLang, TGI)","read and implement architectures from papers"],"nice":["vLLM integrations (verl, OpenRLHF, Unsloth, LlamaFactory)","widely shared technical blogs or side projects on vLLM"],"pay":{"lo":200000,"hi":400000,"currency":"USD","period":"year"},"note":"date not established; live status unverified"}
{"type":"jd","grade":"B","src":["S27"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"CoreWeave","title":"Applied AI Engineer, Inference","url":"https://www.tealhq.com/job/applied-ai-engineer-inference_7ea1aee85e9e6a26c816f9ff9d17641495a36","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA","remote":"on-site","seniority":"unstated","must":["familiarity with LLM inference systems such as vLLM, SGLang, TensorRT-LLM","measure and improve real-world inference performance"],"nice":[],"note":"date not established; live status unverified"}
{"type":"jd","grade":"B","src":["S28"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Fluidstack","title":"Software Engineer, Inference Platform","url":"https://it-jobs-near-me.jobboardly.com/jobs/software-engineer-inference-platform-a8fea23e","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":"unstated","must":["KV cache, prefix sharing and scheduling infrastructure","disaggregated prefill/decode on Kubernetes","speculative decoding (Medusa, EAGLE-3, draft models)","non-NVIDIA accelerators (AMD, TPU, Trainium, Cerebras, Groq)"],"nice":[],"pay":{"lo":165000,"hi":350000,"currency":"USD","period":"year"},"note":"location and date not established; live status unverified"}
{"type":"jd","grade":"B","src":["S29"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"vCluster Labs","title":"Senior Inference Engineer","url":"https://www.builtinboston.com/job/senior-inference-engineer/10631066","job_id":"10631066","seen":"2026-11-13","location":"Boston, MA (syndicated to Colorado and Dublin boards)","remote":null,"seniority":"Senior","must":["production LLM serving with vLLM, SGLang or TensorRT-LLM","quantisation, batching, caching and routing for latency and cost"],"nice":[],"note":"first inference hire; job_id is the Built In id; date not established"}
{"type":"jd","grade":"B","src":["S30"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"General Compute","title":"Founding Inference Engineer","url":"https://wellfound.com/jobs/4817884-inference-engineer","job_id":"4817884","seen":"2026-11-13","location":"remote or on-site","remote":"onsite or remote","seniority":"Founding","must":["production LLM serving: request batching, KV-cache management, continuous batching","vLLM, TGI, TensorRT-LLM or SGLang with a view on shortcomings","serving on non-NVIDIA accelerators"],"nice":[],"note":"visa sponsorship stated as not available; relocation not allowed; job_id is the Wellfound id; date not established"}
{"type":"jd","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Microsoft AI","title":"Member of Technical Staff, LLM Inference (MAI Superintelligence Team)","url":"https://microsoft.ai/job/member-of-technical-staff-llm-inference","job_id":"200009235-en-1","seen":"2026-11-13","location":"Mountain View, CA (multiple US locations)","remote":"office four days a week within commuting distance (MAI policy)","seniority":"unstated","must":["understand generative AI architectures and optimise them for inference","internals of vLLM and SGLang","benchmarking, profiling and optimising PyTorch models"],"nice":["JAX scaling book"],"note":"job number may belong to a sibling listing; date not established"}
{"type":"jd","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Microsoft AI","title":"Member of Technical Staff, Senior ML Engineer (MAI Superintelligence Team)","url":"https://microsoft.ai/job/member-of-technical-staff-senior-ml-engineer-mai-super-intelligence-team/","job_id":null,"seen":"2026-11-13","location":"United States","remote":null,"seniority":"Senior","must":["serving layers on SGLang and vLLM with non-standard decoding","models on NVIDIA H100 and AMD MI300X","quantisation, distillation, memory management"],"nice":[],"note":"date not established"}
{"type":"jd","grade":"B","src":["S32"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Zoox","title":"AI Inference Engineer, Model Optimization & Deployment","url":"https://hotfix.jobs/jobs/ai-inference-engineer-model-optimization-deployment-at-zoox-98f84382-a376-49eb-ab15-fc95bdd56e3f","job_id":null,"seen":"2026-11-13","location":"United States","remote":null,"seniority":"unstated","must":["optimising LLMs, VLMs or VLAs with KV-cache optimisation (PagedAttention), speculative decoding and efficient attention (FlashAttention)"],"nice":[],"note":"date not established"}
{"type":"jd","grade":"C","src":["S33"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Infosys Limited Digital","title":"GenAI Platform / LLM Inference Optimization Engineer (Cloud)","url":"https://www.theladders.com/job/genai-platform-llm-inference-optimization-engineer-cloud-infosyslimiteddigital-charlotte-nc_87331729","job_id":null,"seen":"2026-11-13","location":"Charlotte, NC","remote":null,"seniority":"under 5 years (aggregator label)","must":["vLLM, TensorRT-LLM, Triton Inference Server, SGLang","continuous batching, speculative decoding, KV and prefix caching","FP8/AWQ/GPTQ quantisation and GPU-utilisation tuning"],"nice":[],"pay":{"lo":100000,"hi":130000,"currency":"USD","period":"year"},"note":"pay shown with an asterisk, probably the aggregator's estimate; consultancy"}
{"type":"jd","grade":"B","src":["S34"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"unnamed end client via Dice","title":"AI Inference Engineer (contract W2, 6 months)","url":"https://www.dice.com/job-detail/e4872a74-a68b-49a0-9c67-0e9d12cc5126","job_id":null,"seen":"2026-11-13","location":"San Jose, CA","remote":"on-site","seniority":"unstated","must":["production serving with vLLM, SGLang, Triton Inference Server, TensorRT-LLM, TorchServe or KServe","inference internals: attention, KV cache, continuous batching, quantisation","multi-node multi-GPU serving; tensor and pipeline parallelism","C++, Python and Rust microservices; custom GPU kernels (CUDA, ROCm, Triton)","distributed multi-node serving platform (NVIDIA Dynamo); benchmarking and profiling"],"nice":[],"note":"recruiter-posted contract; listed as three days old on an undated snapshot"}
{"type":"jd","grade":"B","src":["S34"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"unnamed end client via Dice","title":"LLM Inference / AI Infrastructure Engineer (contract W2, 12 months)","url":"https://dice.com/job-detail/cd8d5273-a49c-4d0a-941b-42963aac15a5","job_id":null,"seen":"2026-11-13","location":"Charlotte, NC","remote":"on-site","seniority":"unstated","must":["vLLM, TensorRT-LLM, Triton Inference Server, SGLang","continuous batching, speculative decoding, KV and prefix caching","FP8/AWQ/GPTQ; tensor parallelism","Kubernetes, KServe, OpenShift AI, Helm"],"nice":[],"note":"recruiter-posted contract; listed as 22 days old on an undated snapshot"}
{"type":"jd","grade":"C","src":["S35"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"FutureFit AI (recruiting platform; end client unnamed)","title":"AI Inference Engineer (vLLM and Kubernetes)","url":"https://remotejobs.org/remote-jobs/ai-inference-engineer-futurefit-ai","job_id":null,"seen":"2026-11-13","location":"remote","remote":"remote","seniority":"Senior","years":5,"must":["5+ years systems or DevOps","vLLM and Kubernetes/OpenShift on RHEL with NVIDIA GPU Operator","Portuguese and English"],"nice":[],"note":"pay not listed; date not established"}
{"type":"jd","grade":"B","src":["S36"],"as_of":"2026-10-06","ttl":"V1","role":"inference-engineer","employer":"Mistral AI","title":"Research Engineer, Inference Foundation","url":"https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/96101264-research-engineer-inference-foundation","job_id":"96101264","seen":"2026-11-13","location":"Warsaw; London; Paris; Munich","remote":"hybrid","seniority":"unstated","must":["building and running ML/LLM services with latency and availability targets","hands-on vLLM, SGLang, TensorRT-LLM or other engines","prefill vs decode, KV cache, batching, scheduling, speculative decoding, parallelism","distributed and disaggregated serving"],"nice":[],"note":"job_id is the General Catalyst board id; posted 2026-10-06 or 2026-10-07 per two boards"}
{"type":"jd","grade":"B","src":["S36"],"as_of":"2026-10-20","ttl":"V1","role":"inference-engineer","employer":"Mistral AI","title":"Research Engineer, Latency & Throughput","url":"https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/97523312-research-engineer-latency-throughput","job_id":"97523312","seen":"2026-11-13","location":"London; Paris","remote":"hybrid","seniority":"unstated","must":["familiarity with state-of-the-art LLM inference"],"nice":["vLLM or production LLM deployments (inference experience is a plus, not required)"],"note":"research-engineer variant: speculative decoding, quantisation, KV compression"}
{"type":"jd","grade":"B","src":["S37"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"NVIDIA","title":"Senior Software Engineer, AI Inference Systems","url":"https://builtinbristol.uk/job/senior-software-engineer-ai-inference-systems/9221782","job_id":"9221782","seen":"2026-11-13","location":"UK (remote); Dublin listing","remote":"remote (UK)","seniority":"Senior","must":["performance engineering in ML frameworks (PyTorch) and engines (vLLM, SGLang)","contribute vLLM features; speculative decoding and DP/TP/EP/PP","benchmarking methodology including MLPerf Inference"],"nice":["open-source contributions with links to GitHub pull requests"],"ats":"Workday (NVIDIA)","note":"job_id is the Built In id; listed as posted one day earlier on an undated snapshot; efficiency at scale"}
{"type":"jd","grade":"B","src":["S38"],"as_of":"2026-07-29","ttl":"V1","role":"inference-engineer","employer":"Weekday client (unnamed)","title":"Inference Engineer","url":"https://apply.workable.com/weekday-1/jobs/view/A44098974C.md","job_id":"A44098974C","seen":"2026-11-13","location":"Bengaluru, India","remote":"on-site","seniority":"Senior","years":5,"must":["5+ years","LLMs and vLLM for production inference","transformer deployment with modern inference frameworks","distributed inference systems; benchmarking and profiling; latency, throughput and memory efficiency"],"nice":[],"pay":{"lo":2400000,"hi":3600000,"currency":"INR","period":"year"},"ats":"Workable","note":"105 days old on the research date; retained and flagged; a re-listing showed an application close of 2026-11-27"}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"DigitalOcean","title":"Senior Forward Deployed Engineer I (AI Inference)","url":"https://builtinbengaluru.in/job/senior-forward-deployed-engineer-i-ai-inference/10521962","job_id":"JR 2026-7939","seen":"2026-11-13","location":"Bengaluru, India","remote":"hybrid/in-office","seniority":"Senior","must":["vLLM, llm-d, SGLang, TensorRT-LLM or Modular MAX including continuous batching and paged attention","Kubernetes-native multi-tenant serving (llm-d, Dynamo, Ray Serve)","FP4/FP8 quantisation; distributed systems"],"nice":["open-source contributions to vLLM and llm-d","Python and Go (skills tags)"],"note":"listed as 21 days old on an undated snapshot"}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"DigitalOcean","title":"Senior Engineer I (Inference Services)","url":"https://builtinpune.in/job/senior-engineer-i-inference-services/8570880","job_id":null,"seen":"2026-11-13","location":"Hyderabad, India","remote":"hybrid","seniority":"Senior","must":["LLM inference platform across NVIDIA and AMD GPUs","CUDA or ROCm exposure; Go and Python"],"nice":["inference engines such as vLLM, SGLang, Modular MAX","contributions to open-source inference engines"],"note":"listed as reposted four days earlier on an undated snapshot"}
{"type":"jd","grade":"B","src":["S40"],"as_of":"2026-09-17","ttl":"V1","role":"inference-engineer","employer":"Gnani.ai","title":"Senior LLMOps Engineer","url":"https://www.hirist.tech/j/gnaniai-senior-llmops-engineer-1672372","job_id":"1672372","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"Senior","years":"6-10","must":["own the production LLM serving stack across vLLM, SGLang and NVIDIA Dynamo","engine selection per workload justified with benchmark evidence"],"nice":[],"note":"job_id is the hirist id; posted 17/09/2026 (dd/mm/yyyy)"}
{"type":"jd","grade":"B","src":["S40"],"as_of":"2026-10-08","ttl":"V1","role":"inference-engineer","employer":"Gnani.ai","title":"LLMOps Engineer","url":"https://www.hirist.tech/j/gnani-ai-llmops-engineer-1677460","job_id":"1677460","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"unstated (6-10 years)","years":"6-10","must":["depth in at least two of: serving engine (vLLM, SGLang, Dynamo), model optimisation (quantisation, distillation, speculative decoding, pruning), kernels (CUDA/Triton)","TensorRT-LLM engine building, NIM or Triton in production","serving hybrid state-space and attention models","profiling and bottleneck analysis"],"nice":["upstream contributions to serving or kernel projects (described as close to an expectation)"],"note":"job_id is the hirist id; posted 08/10/2026 (dd/mm/yyyy)"}
{"type":"jd","grade":"B","src":["S41"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"PrimaLabs","title":"Sr. Inference Engineer (LLM)","url":"https://jobs.weekday.works/sr-inference-engineer-llm-at-primalabs-4416492368","job_id":"4416492368","seen":"2026-11-13","location":"Gurugram, India","remote":null,"seniority":"Senior","years":"3-5+","must":["serving infrastructure: batching, KV-cache management, speculative decoding, quantisation, TP/PP","inference engines vLLM, TensorRT-LLM, SGLang or TGI","profiling with Nsight, nvprof or PyTorch Profiler"],"nice":["disaggregated serving","non-NVIDIA accelerators (AMD, Trainium/Inferentia, TPU, Gaudi)"],"note":"job_id is the id in the board URL; date not established; asks for contributions to open-source inference engines"}
{"type":"jd","grade":"B","src":["S41"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"AION","title":"Senior Software Engineer, Inference Platform","url":"https://echojobs.io/job/aion-senior-software-engineer-inference-platform-56bbr","job_id":null,"seen":"2026-11-13","location":"Bengaluru, India","remote":"hybrid","seniority":"Senior","must":["inference engines (vLLM, TGI, TensorRT-LLM or similar)","distributed systems, microservices and API gateway patterns"],"nice":["Golang strongly preferred"],"note":"skills tags list Python, Go, C++, Rust, Kubernetes; date not established"}
{"type":"jd","grade":"C","src":["S42"],"as_of":"2026-11-13","ttl":"V1","role":"inference-engineer","employer":"Rackspace Technology","title":"AI Model Serving Specialist","url":"https://resumegeni.com/jobs/ai-model-serving-specialist-at-rackspace-india-remote","job_id":null,"seen":"2026-11-13","location":"India (remote)","remote":"remote","seniority":"unstated","must":["deploying ML/LLM models on Triton, vLLM or KServe within Kubernetes","tuning batching, KV-cache and TensorRT optimisations for latency and throughput SLAs","Kubernetes, GPU scheduling, CUDA/MIG"],"nice":[],"note":"mirror of employer posting; managed-services employer; date not established"}
{"type":"jd","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V1","role":null,"employer":"Anthropic","title":"Staff+ Software Engineer, Inference Velocity","url":"https://job-boards.greenhouse.io/anthropic/jobs/5257650008","job_id":"5257650008","seen":"2026-11-13","location":"San Francisco, CA","remote":null,"seniority":"Staff+","must":["developer-productivity and CI work for inference engineers; no LLM serving requirement"],"nice":[],"pay":{"lo":405000,"hi":485000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"excluded: not this role; the same job ID appeared as Inference Runtime in a search-index copy; COI"}
{"type":"jd","grade":"A","src":["S9"],"as_of":"2026-11-13","ttl":"V1","role":null,"employer":"Together AI","title":"Senior or Staff Software Engineer, Inference / Compute Infrastructure Engineering (India)","url":"https://job-boards.greenhouse.io/togetherai/jobs/5213325007","job_id":"5213325007","seen":"2026-11-13","location":"India","remote":null,"seniority":"Senior/Staff","must":["Kubernetes control plane and GPU fleet provisioning; no LLM serving requirement"],"nice":[],"ats":"Greenhouse","note":"excluded: not this role; sibling postings exist for SF, Amsterdam and London"}
{"type":"jd","grade":"A","src":["S12"],"as_of":"2026-11-13","ttl":"V1","role":null,"employer":"Mistral AI","title":"Software Engineer, Performance","url":"https://jobs.lever.co/mistral/45e3045f-95d7-4200-bad5-3da0ad4b45d7","job_id":"45e3045f-95d7-4200-bad5-3da0ad4b45d7","seen":"2026-11-13","location":null,"remote":null,"seniority":"unstated","must":["backend, API and database performance engineering; no LLM serving requirement"],"nice":[],"ats":"Lever","note":"excluded: not this role"}
```

```jsonl
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"serving_engines","n":37,"source_kind":"jd-sample","count":28,"share":0.757,"tier_hint":"Must","note":"any named engine (vLLM, SGLang, TensorRT-LLM, TGI, Dynamo, llm-d, Triton server); lower bound, 29 snippet-level postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"vllm","n":37,"source_kind":"jd-sample","count":28,"share":0.757,"tier_hint":"Must","note":"every posting naming an engine named vLLM; promote from Important"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"sglang","n":37,"source_kind":"jd-sample","count":21,"share":0.568,"tier_hint":"Important","note":"usually listed as one of several engines"}
{"type":"skill_signal","grade":"M","src":["S61","S15"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"trt_llm","n":37,"source_kind":"jd-sample","count":15,"share":0.405,"tier_hint":"Important","note":"engine-build path removed from TensorRT-LLM; PyTorch backend only"}
{"type":"skill_signal","grade":"M","src":["S61","S16"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:tgi","n":37,"source_kind":"jd-sample","count":4,"share":0.108,"tier_hint":"Avoid","note":"maintenance mode; recognise, do not invest"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:dynamo_llm_d","n":37,"source_kind":"jd-sample","count":8,"share":0.216,"tier_hint":"Should","note":"NVIDIA Dynamo or llm-d named; emerging orchestration layer"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:triton_inference_server","n":37,"source_kind":"jd-sample","count":5,"share":0.135,"tier_hint":"Optional","note":"mainly enterprise, consultancy and contract postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"system_design","n":37,"source_kind":"jd-sample","count":15,"share":0.405,"tier_hint":"Must","note":"distributed systems or system design named; 8 of 8 in the full-text subset"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"python","n":37,"source_kind":"jd-sample","count":12,"share":0.324,"tier_hint":"Must","note":"5 of 8 full-text; not named in OpenAI, xAI or Sarvam texts"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"cpp","n":37,"source_kind":"jd-sample","count":5,"share":0.135,"tier_hint":"Important","note":"2 of 8 full-text; 4 of 18 runtime-variant postings; demote from Must"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:cuda_kernels","n":37,"source_kind":"jd-sample","count":11,"share":0.297,"tier_hint":"Important","note":"CUDA, Triton or kernel work named; 8 of 18 runtime-variant postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"pytorch_internals","n":37,"source_kind":"jd-sample","count":4,"share":0.108,"tier_hint":"Should","note":"PyTorch named, mostly as familiarity; demote from Must"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"kubernetes","n":37,"source_kind":"jd-sample","count":12,"share":0.324,"tier_hint":"Important","note":"0 of 18 runtime; 6 of 9 platform; 6 of 10 deployment"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"gpu_fundamentals","n":37,"source_kind":"jd-sample","count":9,"share":0.243,"tier_hint":"Must","note":"GPU architecture, memory or utilisation named; hard to separate in snippets"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"batching_kv","n":37,"source_kind":"jd-sample","count":18,"share":0.486,"tier_hint":"Must","note":"most-named technique; promote from Important"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"spec_decoding","n":37,"source_kind":"jd-sample","count":13,"share":0.351,"tier_hint":"Important","note":"10 of 18 runtime-variant postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"quantization","n":37,"source_kind":"jd-sample","count":11,"share":0.297,"tier_hint":"Important","note":"FP8, AWQ, GPTQ, low-precision numerics"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"parallel_serving","n":37,"source_kind":"jd-sample","count":9,"share":0.243,"tier_hint":"Important","note":"tensor, pipeline, expert parallelism or MoE serving"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"load_testing","n":37,"source_kind":"jd-sample","count":9,"share":0.243,"tier_hint":"Important","note":"benchmarking, load testing or latency SLOs named"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"profiling","n":37,"source_kind":"jd-sample","count":8,"share":0.216,"tier_hint":"Important","note":"Nsight, PyTorch profiler, py-spy, perf"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"cost_latency","n":37,"source_kind":"jd-sample","count":12,"share":0.324,"tier_hint":"Important","note":"cost, latency, throughput or price-performance named as the objective"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"prefix_caching","n":37,"source_kind":"jd-sample","count":6,"share":0.162,"tier_hint":"Should","note":"demote from Important"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"inference_autoscaling","n":37,"source_kind":"jd-sample","count":5,"share":0.135,"tier_hint":"Should","note":"4 of 9 platform-variant postings; Important for platform"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"kv_aware_routing","n":37,"source_kind":"jd-sample","count":8,"share":0.216,"tier_hint":"Should","note":"routing or load balancing; 6 of 9 platform-variant postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:disaggregated_serving","n":37,"source_kind":"jd-sample","count":6,"share":0.162,"tier_hint":"Should","note":"prefill/decode disaggregation; appears in 2026 postings (Mistral, Sarvam, Amazon, NVIDIA)"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:upstream_oss_contributions","n":37,"source_kind":"jd-sample","count":11,"share":0.297,"tier_hint":"Important","note":"upstream contributions, PR links or blogs requested; a proof signal"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:rust","n":37,"source_kind":"jd-sample","count":8,"share":0.216,"tier_hint":"Should","note":"5 of 9 platform-variant postings"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:go","n":37,"source_kind":"jd-sample","count":6,"share":0.162,"tier_hint":"Optional","note":"platform and deployment variants"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:non_nvidia_accelerators","n":37,"source_kind":"jd-sample","count":8,"share":0.216,"tier_hint":"Should","note":"AMD, TPU, Trainium, Gaudi, Cerebras, Groq"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:distillation","n":37,"source_kind":"jd-sample","count":4,"share":0.108,"tier_hint":"Optional","note":"draft-model or speculator training and model distillation"}
{"type":"skill_signal","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"new:edge_on_device","n":37,"source_kind":"jd-sample","count":1,"share":0.027,"tier_hint":"Optional","note":"Red Hat llama.cpp only; specialisation share"}
{"type":"skill_signal","grade":"M","src":["S61","S10"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","skill":"c3_ownership","n":37,"source_kind":"jd-sample","count":1,"share":0.027,"tier_hint":"Important","note":"explicit on-call SLO ownership named in one posting; behavioural skills not measurable from snippets"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"posting_count_inference_jobs_category","unit":"postings","value":341,"region":"global","method":"platform category listing","note":"includes postings up to about 2 years old; upper bound on openings"}
{"type":"measure","grade":"M","src":["S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"share_page1_listings_age_le_2_months","unit":"share","value":0.25,"n":20,"method":"age labels on relevance-sorted page 1","region":"global","note":"95% interval about 6-44%"}
{"type":"measure","grade":"M","src":["S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"share_page1_listings_age_le_3_months","unit":"share","value":0.4,"n":20,"method":"age labels on relevance-sorted page 1","region":"global","note":"95% interval about 19-61%; implies roughly 65-210 of 341"}
{"type":"measure","grade":"A","src":["S8"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"together_ai_board_open_roles","unit":"roles","value":78,"region":"global","method":"Greenhouse board listing"}
{"type":"measure","grade":"A","src":["S8"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"together_ai_inference_titled_roles","unit":"roles","value":10,"region":"global","method":"titles containing Inference on page 1 of 2","note":"lower bound"}
{"type":"measure","grade":"M","src":["S7","S8","S9"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"together_ai_inference_titled_roles_in_scope","unit":"roles","value":1,"n":10,"method":"classified by posting content","note":"4 provisioning family, 2 reliability, 3 forward-deployed or support"}
{"type":"measure","grade":"B","src":["S20"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"baseten_open_roles_platform_mirror","unit":"roles","value":93,"region":"global","method":"company page on a niche board"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"sample_included_postings","unit":"postings","value":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"sample_examined_postings","unit":"postings","value":56,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"sample_excluded_postings","unit":"postings","value":19,"method":"8 not this role or unclear; 11 outside window or not verifiable"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"india_postings_in_sample","unit":"postings","value":9,"n":37,"region":"India","method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_variant_runtime_performance","unit":"share","value":0.486,"n":37,"method":"classified by posting content"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_variant_platform_fleet","unit":"share","value":0.243,"n":37,"method":"classified by posting content"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_variant_deployment_mlops","unit":"share","value":0.27,"n":37,"method":"classified by posting content"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_frontier_lab","unit":"share","value":0.189,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_big_tech_silicon","unit":"share","value":0.162,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_ai_native_cloud","unit":"share","value":0.378,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_enterprise_vendor","unit":"share","value":0.081,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_consultancy_managed","unit":"share","value":0.054,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_recruiter_posted","unit":"share","value":0.108,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_employer_public_research","unit":"share","value":0.027,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_region_us","unit":"share","value":0.541,"n":37,"region":"US","method":"own JD sample; 12 of 20 list California"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_region_europe","unit":"share","value":0.135,"n":37,"region":"Europe","method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_region_india","unit":"share","value":0.243,"n":37,"region":"India","method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_region_remote_or_unknown","unit":"share","value":0.081,"n":37,"method":"own JD sample"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_seniority_staff_plus","unit":"share","value":0.135,"n":37,"method":"level in title or posting"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_seniority_senior","unit":"share","value":0.351,"n":37,"method":"level in title or posting"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_seniority_unstated","unit":"share","value":0.514,"n":37,"method":"level in title or posting"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_seniority_entry_level","unit":"share","value":0,"n":37,"method":"level in title or posting","note":"no explicit entry-level or new-graduate posting"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_remote_eligible","unit":"share","value":0.108,"n":37,"method":"explicit remote eligibility"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_pay_range_posted","unit":"share","value":0.378,"n":37,"method":"employer-posted range present","note":"US 10 of 20; Europe 2 of 5; India 1 of 9; remote or unknown 1 of 3"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_degree_stated","unit":"share","value":0.135,"n":37,"method":"degree requirement present","note":"all five accept equivalent experience; none requires a PhD"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"median_minimum_years_stated","unit":"years","value":5,"n":9,"method":"minimum years among postings stating years","note":"range 3-6"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_certification_named","unit":"share","value":0,"n":37,"method":"own JD sample; lower bound for snippet-level postings"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","subject":"role:inference-engineer","measure":"share_visa_statement_present","unit":"share","value":0.108,"n":37,"method":"explicit sponsorship statement","note":"3 yes (Anthropic), 1 no (General Compute)"}
{"type":"measure","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V1","subject":"role:inference-engineer","measure":"share_date_verified_in_window","unit":"share","value":0.405,"n":37,"method":"opened live or explicit in-window date","note":"6 relative-age only; 15 undated; 1 older than 90 days"}
{"type":"pay","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p50","value":287500,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","n":14,"note":"median of range midpoints, date-clean set"}
{"type":"pay","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p25","value":260600,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","n":14,"note":"25th percentile of range midpoints"}
{"type":"pay","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p75","value":344400,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","n":14,"note":"75th percentile of range midpoints"}
{"type":"pay","grade":"M","src":["S61","S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p50","value":270500,"currency":"USD","period":"year","basis":"base","source_name":"own sample plus three platform listings about 3 months old","n":17,"note":"sensitivity; p25-p75 about 251500-327600"}
{"type":"pay","grade":"M","src":["S61"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":165000,"hi":500000,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","n":14,"note":"lowest lower bound and highest upper bound"}
{"type":"pay","grade":"M","src":["S1","S2","S5","S6"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p50","value":387750,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","employer_type":"frontier-lab","n":4,"note":"Anthropic x2, OpenAI, xAI; median of range midpoints"}
{"type":"pay","grade":"M","src":["S7","S18","S23","S26","S28"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p50","value":270000,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","employer_type":"ai-startup","n":7,"note":"Together, Baseten, Inferact, Fluidstack, Thinking Machines, Crusoe x2"}
{"type":"pay","grade":"M","src":["S24"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"p50","value":261000,"currency":"USD","period":"year","basis":"base","source_name":"own sample of posted ranges","employer_type":"enterprise","n":2,"note":"Red Hat Boston postings"}
{"type":"pay","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"San Francisco, New York, Seattle","stat":"range","lo":320000,"hi":485000,"currency":"USD","period":"year","basis":"base","source_name":"Anthropic posting","level":"Senior/Staff","employer_type":"frontier-lab","n":1,"note":"COI"}
{"type":"pay","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"San Francisco, Seattle","stat":"range","lo":300000,"hi":485000,"currency":"USD","period":"year","basis":"base","source_name":"Anthropic posting","level":"Senior/Staff","employer_type":"frontier-lab","n":1,"note":"COI"}
{"type":"pay","grade":"A","src":["S5"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"San Francisco","stat":"range","lo":266000,"hi":500000,"currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting","employer_type":"frontier-lab","n":1,"note":"plus equity; aggregator copies show 325000-490000"}
{"type":"pay","grade":"A","src":["S6"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"Palo Alto, Seattle","stat":"range","lo":180000,"hi":440000,"currency":"USD","period":"year","basis":"base","source_name":"xAI posting","employer_type":"frontier-lab","n":1}
{"type":"pay","grade":"A","src":["S7"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"San Francisco","stat":"range","lo":200000,"hi":290000,"currency":"USD","period":"year","basis":"base","source_name":"Together AI posting","level":"Senior","employer_type":"ai-startup","n":1,"note":"plus equity"}
{"type":"pay","grade":"B","src":["S22"],"as_of":"2026-10-31","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":224000,"hi":431250,"currency":"USD","period":"year","basis":"base","source_name":"RemoWork copy of NVIDIA posting","level":"Senior","employer_type":"big-tech","n":1}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"San Francisco","stat":"range","lo":300000,"hi":400000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, Thinking Machines Lab","employer_type":"ai-startup","n":1,"note":"listing aged about 1 month on 2026-11-13"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":215000,"hi":260000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, Crusoe Staff Applied AI Inference Engineer","level":"Staff","employer_type":"ai-startup","n":1,"note":"listing aged about 2 months"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":250000,"hi":300000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, Crusoe Senior Staff Applied AI Inference Engineer","level":"Senior Staff","employer_type":"ai-startup","n":1,"note":"listing aged about 2 months"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":184000,"hi":356500,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, NVIDIA Senior SWE AI Inference Performance","level":"Senior","employer_type":"big-tech","n":1,"note":"listing aged about 3 months; excluded from primary statistics"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":124000,"hi":241500,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, NVIDIA Inference Performance Engineer","employer_type":"big-tech","n":1,"note":"listing aged about 3 months; excluded from primary statistics"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"US","stat":"range","lo":195000,"hi":285000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs listing, d-Matrix Principal LLM Inference Engineer","level":"Principal","employer_type":"ai-startup","n":1,"note":"listing aged about 3 months; excluded from primary statistics"}
{"type":"pay","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"London, UK","stat":"range","lo":325000,"hi":390000,"currency":"GBP","period":"year","basis":"base","source_name":"Anthropic posting","level":"Staff","employer_type":"frontier-lab","n":1,"note":"COI"}
{"type":"pay","grade":"A","src":["S13"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"Vienna, Austria","stat":"offer","value":66598,"currency":"EUR","period":"year","basis":"base","source_name":"AIT posting","level":"Senior","employer_type":"public-sector","n":1,"note":"starting gross salary under the non-university research collective agreement"}
{"type":"pay","grade":"B","src":["S38"],"as_of":"2026-07-29","ttl":"V3","role":"inference-engineer","location":"Bengaluru, India","stat":"range","lo":2400000,"hi":3600000,"currency":"INR","period":"year","basis":"tc","source_name":"Weekday client posting","level":"Senior (5+ years)","n":1,"note":"posted as 24-36 LPA; component not specified"}
{"type":"pay","grade":"B","src":["S44"],"as_of":"2026-05-23","ttl":"V3","role":"inference-engineer","location":"Greater Bengaluru, India","stat":"p50","value":6623336,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi, Google software engineer","employer_type":"big-tech","note":"software-engineer title, not inference-specific; L3 4.07M to L7 32.43M"}
{"type":"pay","grade":"B","src":["S44"],"as_of":"2026-04-05","ttl":"V3","role":"inference-engineer","location":"Greater Bengaluru, India","stat":"p50","value":6890000,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi, NVIDIA software engineer","employer_type":"big-tech","note":"software-engineer title; a second figure on the same page is 6334100"}
{"type":"pay","grade":"B","src":["S44"],"as_of":"2026-03-10","ttl":"V3","role":"inference-engineer","location":"Greater Bengaluru, India","stat":"p50","value":5040000,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi, Qualcomm software engineer","employer_type":"big-tech","note":"software-engineer title; a second figure on the same page is 4840363"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"global","stat":"p25","value":138000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs category summary","n":11,"note":"platform statistic from 11 postings; snapshot date unknown"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-13","ttl":"V3","role":"inference-engineer","location":"global","stat":"p75","value":322000,"currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs category summary","n":11,"note":"platform statistic from 11 postings; snapshot date unknown"}
{"type":"loop","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V3","employer":"Anthropic","track":"infrastructure","stages":["application form with acknowledgement of candidate AI-use guidance","coding interviews based on on-the-job work, language of the candidate's choice"],"ai_policy":"acknowledgement of AI guidance required at application; interview-time rules not retrieved","note":"posting states interviews are not LeetCode-style; COI"}
{"type":"loop","grade":"D","src":["S46"],"as_of":"2026-11-13","ttl":"V3","employer":"Anthropic","track":"infrastructure","stages":["virtual onsite of four rounds reported by one candidate","coding and optimisation task","design discussion on batching, KV cache and request scheduling","mission and safety discussion"],"note":"single anecdote; not for load-bearing use"}
{"type":"loop","grade":"C","src":["S45"],"as_of":"2026-11-13","ttl":"V3","employer":"Together AI","track":"infrastructure","stages":["four to five rounds","two coding rounds (algorithms; applied ML systems)","one 60-minute system design on multi-model inference serving","domain discussion on batching, KV cache, speculative decoding, quantisation"],"note":"guide says it is partly reasoned from postings"}
{"type":"loop","grade":"C","src":["S45"],"as_of":"2026-11-13","ttl":"V3","employer":"Baseten","track":"infrastructure","stages":["serve an LLM behind a low-latency API under bursty traffic","justify batching, KV-cache and queueing choices"],"note":"guide, not an employer statement"}
{"type":"loop","grade":"B","src":["S59"],"as_of":"2026-11-13","ttl":"V3","employer":"xAI","track":"infrastructure","stages":["application reviewed by technical staff, no recruiters","main process targeted within one week","interviews over Google Meet"],"formats":["video"],"note":"older posting copy; date not established"}
{"type":"practice","grade":"P","src":["S61","S10"],"as_of":"2026-11-13","ttl":"V3","area":"résumé headline","tactic":"Pair one named engine with an SLO metric in the headline","claim":"A headline such as engine plus TTFT/p99 plus cost per million tokens matches how postings are written","evidence":"named engine in 28 of 37 postings; Sarvam lists TTFT, TPOT, p99 and cost per million tokens as its scoreboard","verdict":"use"}
{"type":"practice","grade":"P","src":["S10","S55"],"as_of":"2026-11-13","ttl":"V3","area":"evidence lines","tactic":"Quantify with percentile latency and the load profile, not averages","claim":"Percentile latency with request mix reads as credible; averages read as naive","evidence":"Sarvam asks for concrete outcomes rather than deployed a model; practitioner guide says reviewers read benchmarks critically","verdict":"use"}
{"type":"practice","grade":"P","src":["S61","S37","S10","S54"],"as_of":"2026-11-13","ttl":"V3","area":"proof of work","tactic":"Merge an upstream PR on a non-trivial path of vLLM, SGLang or FlashInfer","claim":"Upstream contributions are named in 11 of 37 postings and NVIDIA asks for PR links","evidence":"Sarvam wants non-trivial paths; InferQuest-style programmes exclude typo fixes","verdict":"use-with-care","risk":"typo-fix PRs read as noise; maintainer review capacity limits throughput"}
{"type":"practice","grade":"P","src":["S61"],"as_of":"2026-11-13","ttl":"V3","area":"keywords","tactic":"Mirror posting vocabulary: continuous batching, KV cache, prefix caching, speculative decoding, FP8/AWQ/GPTQ, TP/PP/EP, disaggregated prefill/decode","claim":"These terms recur across variants","evidence":"counts of 6 to 18 of 37 postings per term","verdict":"use"}
{"type":"practice","grade":"P","src":["S15","S16","S17","S61"],"as_of":"2026-11-13","ttl":"V3","area":"red flags","tactic":"Do not headline TGI or the trtllm-build engine path","claim":"Both are retired or in maintenance mode","evidence":"TGI maintenance mode; TensorRT backend and trtllm-build removed","verdict":"avoid"}
{"type":"practice","grade":"P","src":["S61"],"as_of":"2026-11-13","ttl":"V3","area":"résumé variants","tactic":"Keep three variants: runtime, platform/fleet, deployment/MLOps","claim":"Requirements differ sharply by variant (Kubernetes 0 of 18 runtime versus 6 of 9 platform)","evidence":"variant mix 18/9/10 of 37","verdict":"untested"}
{"type":"practice","grade":"P","src":["S14","S61"],"as_of":"2026-11-13","ttl":"V3","area":"certifications","tactic":"Do not lead with NCP-GENL for inference roles","claim":"No posting names it and its blueprint centres on training and fine-tuning","evidence":"0 of 37 postings; NVIDIA exam page","verdict":"avoid"}
{"type":"credential","grade":"A","src":["S14","S61"],"as_of":"2026-11-13","ttl":"V2","id":"nvidia_ncp_genl","name":"NVIDIA-Certified Professional: Generative AI LLMs","issuer":"NVIDIA","level":"Professional","state":"announced","url":"https://www.nvidia.com/en-gb/learn/certification/generative-ai-llm-professional/","exam_code":"NCP-GENL","format":"online","proctored":true,"duration_min":120,"items":"60-70","fee":{"amount":200,"currency":"USD"},"validity_months":24,"renewal":"retake the exam","domains":[{"name":"LLM Architecture","weight":0.06},{"name":"Prompt Engineering","weight":0.13},{"name":"Data Preparation","weight":0.09},{"name":"Model Optimization","weight":0.17},{"name":"Fine-Tuning","weight":0.13},{"name":"Evaluation","weight":0.07},{"name":"GPU Acceleration and Optimization","weight":0.14},{"name":"Model Deployment","weight":0.09},{"name":"Production Monitoring and Reliability","weight":0.07},{"name":"Safety, Ethics, and Compliance","weight":0.05}],"families":["AI Infrastructure & Platform"],"jd_signal":{"value":0,"unit":"postings naming it","n":37,"region":"global","method":"own JD sample; 29 of 37 snippet-level"},"note":"page shows (Coming soon) at the top yet lists registration and full details; page metadata dated 2026-10-30"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"role-specific posting trend since 2025-01","searched":"web search for LinkedIn, Indeed, Lightcast, Robert Half and platform series; only AI-engineer aggregates found","note":"S53 and S52 are broader"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"LinkedIn and Indeed live counts for inference-engineer queries","searched":"not surfaced by search; not attempted behind login"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"JobsPipe and Fast AI Jobs role-level aggregates","searched":"web search; only job pages and company medians found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Levels.fyi inference-specific title data","searched":"web search and Levels.fyi pages; software-engineer and ML-engineer titles only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"in-window GCC postings (NVIDIA, Qualcomm, AMD, Microsoft, Google India)","searched":"web search for India inference roles; one NVIDIA India posting removed 2026-06-24"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"consultancy postings beyond Infosys","searched":"web search for Accenture, Deloitte, TCS, Wipro, Cognizant and similar"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"A-grade interview loops for OpenAI, NVIDIA, Baseten, Sarvam","searched":"employer pages and web search; no loop detail"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Anthropic candidate AI-guidance policy page","searched":"fetch refused because the URL had not appeared in results"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"LCA filings by exact title Inference Engineer","searched":"LCA aggregator pages for Anthropic, Together, Fireworks, Baseten; titles are generic"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"named hiring-manager statements on proof of work","searched":"web search; only postings and C-grade guides found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"typical prior roles of people hired into the role","searched":"web search for published analyses; none found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"RadixArk posting named in K3","searched":"not retrieved"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"non-English postings (French, German, Chinese, Japanese, Korean)","searched":"not searched","note":"limitation of the sample"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"decode roofline and KV-cache maths as named interview topics","searched":"interview guides and recaps; no source names them"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"transition-time evidence for backend to Staff-level inference (K13)","searched":"web search; none found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"employer statements on credentials for this role","searched":"postings and web search; none found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"India-specific interview differences","searched":"web search; none found"}
```
