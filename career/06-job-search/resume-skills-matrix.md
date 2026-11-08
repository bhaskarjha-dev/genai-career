---
id: job-search.resume-matrix
title: "GenAI Resume Skills Matrix"
content_type: reference
stage: 6
status: published
last_verified: 2026-11-04
summary: "The concise skills section for every role (Must / Important / Should / Optional headline skills), shared skills across roles, and a skills-section blueprint per resume variant."
sources: [T0-03, T0-04, T0-10, T0-11, T0-13]
generated_by: "scripts/build_resume_matrix.py (generated blocks)"
---
# GenAI Resume Skills Matrix
## Must / Important / Should / Optional Skills for Every GenAI Role, With Resume-Variant Blueprints

> **Updated:** 2026-11-04 · **Scope:** Programmatic headline resume skills matrix generated from the typed skills ontology.
> **How to use it:** [resume-strategy.md](resume-strategy.md) explains the master → variant → per-posting system that these lists feed.
> **Role universe:** the individual-contributor roles of the [role catalog](../02-roles/role-catalog.md), in the order of the [GenAI target roles](../02-roles/genai-target-roles.md), plus the employed leadership tracks.
> **Sources:**
> - Tiers and evidence tags: [data/skills_ontology.json](../../data/skills_ontology.json), shown in full in the [role skill inventories](../03-skills-and-tech/role-skill-inventories.md).
> - JobsPipe job-description measurements, retrieved 2026-11-02 [B] ([data/posting_skill_shares.json](../../data/posting_skill_shares.json)).
> - Skill shares from T0-03, T0-15 and T0-16.
>
> **Concise layer of one ontology:** this file shows only the *headline* skills, the resume phrases that fit a skills section. The complete typed inventory for each role (every concept, method, tool, framework, platform and non-technical skill, with evidence) is in [role-skill-inventories.md](../03-skills-and-tech/role-skill-inventories.md); each role block below links to it.
>
> **Reproduce:** edit [data/skills_ontology.json](../../data/skills_ontology.json), the single source for skills, role tiers and variants. Then run `python3 scripts/build_resume_matrix.py --update`; it validates the ontology and rewrites every block between the `BEGIN/END GENERATED` markers in this file.
>
> **Honesty rule:** this matrix tells you what to *build and show*, not what to claim. List only what you can defend in an interview.

---

## 1. How the tiers are defined

| Tier | Meaning | Evidence rule used here | Where it goes on the resume |
|---|---|---|---|
| **Must** | The screen gate: what most postings put in *basic qualifications*, plus recruiter-search hooks (titles, languages, frameworks, LLM terms) | Role-defining, or named in roughly half or more of the title's postings | Skills section **and** an evidence line in a recent role or project |
| **Important** | The differentiators that win interviews and set your level (*preferred qualifications*) | Skills that set strong candidates apart in the evidence, or skills probed in the role's interview track (the older three-tier model of D-004 is not used: ERRATA U20) | A project or experience bullet with a metric; also the skills section |
| **Should** | Common supporting skills | Named in roughly 20–50% of postings, or standard hygiene | Skills section if true, in the posting's exact wording |
| **Optional** | Employer-specific or frontier skills | Under ~20% of postings, frontier tier, or named only by specific employers | Only when the posting names it |
| **Avoid** | Devalued, deprecated or counter-productive items | The ontology's register of devalued skills and its tool statuses ([skills radar](../03-skills-and-tech/skills-radar.md#4-replace-what-to-stop-investing-in)) | Leave out, or reframe |

**Prerequisites are not skills.** Years of experience, degree, PhD, credentials and work authorisation are facts. They cannot be tailored, so state them plainly; if you miss a hard requirement, route around it with a referral ([T0-04](../../research/sessions/T0-04-ats-filtering-funnel-conversion-math.md) R5).

**Ordering:** within a tier, skills are in priority order. That is posting share where postings were measured; otherwise the ontology's order.

**Evidence basis:** each role names one of three bases:
- *JD-measured* (JobsPipe posting shares, B).
- *Catalog tiers* (B–D, from the research sessions cited per skill in the ontology).
- *Practice-curated* (D; check it against 10–20 live postings before investing).

The tiers themselves are a model output (Grade M).

---

<a id="shared-layer"></a>
## 2. The shared layer is thin

How often each skill is Must or Important across the engineering roles (variants A–D):

<!-- BEGIN GENERATED: scripts/build_resume_matrix.py (shared layer) -->
| Skill | Must or Important in (of 19 engineering roles) | Listed at any tier from Must to Should |
|---|:---:|:---:|
| Python (production) | 18 (95%) | 19 (100%) |
| LLM APIs & tool calling | 10 (53%) | 10 (53%) |
| LLM evaluation (golden sets, calibrated judges, CI gates) | 9 (47%) | 11 (58%) |
| AWS / Azure / GCP | 7 (37%) | 12 (63%) |
| ML fundamentals | 7 (37%) | 7 (37%) |
| Git & CI/CD | 6 (32%) | 9 (47%) |
| Agents & tool use | 5 (26%) | 8 (42%) |
| PyTorch | 5 (26%) | 6 (32%) |
| OAuth/OIDC, RBAC, SSO | 5 (26%) | 5 (26%) |
| C++ | 4 (21%) | 6 (32%) |
| Deep learning & transformers | 4 (21%) | 6 (32%) |
| Data structures & algorithms | 4 (21%) | 4 (21%) |
| Retrieval quality (hybrid, reranking, recall@k) | 4 (21%) | 4 (21%) |
| Observability (OpenTelemetry traces, metrics) | 3 (16%) | 9 (47%) |
<!-- END GENERATED -->

Only Python is near-universal. LLM evaluation and LLM API work are shared by about half and a third of the engineering roles, respectively. Every other skill is family-specific, which is why resume variants are organised by role family (§3) rather than built from one universal list.

---

<a id="blueprints"></a>
## 3. Skills-section blueprints for each resume variant

Each variant is **anchored on its highest-ranked target role**: that role's Must and Important skills form the base skills section. For a posting from a sibling role, swap in the listed skills and drop the least relevant anchor items. "Hygiene" lists Should-tier skills shared by at least half of the variant's roles.

<!-- BEGIN GENERATED: scripts/build_resume_matrix.py (variant blueprints) -->
| Variant | Anchor role (base skills section = its Must + Important skills) | Swap in for sibling roles (their Must/Important skills the anchor lacks) | Hygiene: list if true |
|---|---|---|---|
| **A1** Builder | **[AI Engineer](#resume-ai-engineer):** Python (production), LLM APIs & tool calling, Agents & tool use, RAG, LLM evaluation (golden sets, calibrated judges, CI gates), Retrieval quality (hybrid, reranking, recall@k), Agent reliability (durable state, budgets, approvals), Cost & latency engineering, Observability (OpenTelemetry traces, metrics), LLM security (prompt injection, OWASP), Prompt & context design, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search | **[Agentic AI Engineer](#resume-agentic-ai-engineer):** MCP (Model Context Protocol), Containment (DLP, sandboxing, egress), Agent frameworks (LangGraph, Agents SDKs), Human-in-the-loop design; **[AI Evaluation Engineer](#resume-ai-evaluation-engineer):** Testing (pytest), Eval statistics (CIs, power, pass^k), Error analysis, Experiment design & A/B testing, Benchmark construction, Rubrics & inter-rater agreement; **[AI Enablement Engineer](#resume-ai-enablement-engineer):** Internal tooling & DevEx, OAuth/OIDC, RBAC, SSO, MCP (Model Context Protocol), Guardrails, Change management & adoption, LLM gateways, Coding-agent rollout, Pilots & adoption measurement; **[AI Product Engineer](#resume-ai-product-engineer):** React, TypeScript / JavaScript, APIs & integrations, Streaming & agent UX, Agent-UX telemetry, Human-in-the-loop design | Docker, SQL, TypeScript / JavaScript, Token & unit economics |
| **A2** Deployer | **[Forward Deployed Engineer (AI)](#resume-forward-deployed-engineer):** Python (production), APIs & integrations, LLM APIs & tool calling, RAG, Customer scoping & demos, Retrieval quality (hybrid, reranking, recall@k), OAuth/OIDC, RBAC, SSO, Agents & tool use, LLM evaluation (golden sets, calibrated judges, CI gates), Domain expertise, Stakeholder communication | **[Applied AI Engineer](#resume-applied-ai-engineer):** Guardrails, Prompt & context design, Technical writing, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search; **[AI / GenAI Solutions Architect](#resume-ai-solutions-architect):** AWS / Azure / GCP, GenAI reference architectures, Leadership & mentoring, GRC & risk assessment, Managed AI (Bedrock, Azure OpenAI, Vertex), Cost & latency engineering, Token & unit economics, Pre-sales | TypeScript / JavaScript, Docker |
| **B1** Engineer | **[Machine Learning Engineer (GenAI/LLM track)](#resume-ml-engineer):** ML fundamentals, Python (production), PyTorch, Deep learning & transformers, LLM APIs & tool calling, Data structures & algorithms, TensorFlow / JAX, Experiment design & A/B testing, C++, Fine-tuning (SFT, LoRA), LLM evaluation (golden sets, calibrated judges, CI gates), Serving literacy (vLLM, batching, quantisation), Embedding & reranker models, Data pipelines & quality, Eval statistics (CIs, power, pass^k) | — | SQL, Git & CI/CD, Docker, AWS / Azure / GCP, RAG, Stakeholder communication, APIs & integrations, Linear algebra, System design, Error analysis, Quantisation (FP8/FP4, AWQ, GPTQ) |
| **B2** Scientist | **[Applied Scientist (GenAI/LLM teams)](#resume-applied-scientist):** ML fundamentals, Python (production), PyTorch, Experiment design & A/B testing, Data structures & algorithms, SQL, LLM APIs & tool calling, Research-to-production, Eval statistics (CIs, power, pass^k), Fine-tuning (SFT, LoRA), Causal inference, Research methods & re-implementation, Deep learning & transformers | — | LLM evaluation (golden sets, calibrated judges, CI gates), Data pipelines & quality, Stakeholder communication, AWS / Azure / GCP, Testing (pytest), Git & CI/CD, Docker, Recommender systems |
| **B3** Robotics | **[Physical AI / Robotics AI Engineer](#resume-physical-ai-engineer):** Robotics fundamentals, C++, Python (production), Perception / computer vision, Simulation & sim-to-real, ROS, Robot learning & VLA models, Edge inference, Teleoperation data pipelines, Safety cases | — | PyTorch, Deep learning & transformers, Quantisation (FP8/FP4, AWQ, GPTQ), Reinforcement learning, Linux, Docker, Data pipelines & quality |
| **C1** Engineering | **[Research Engineer / Member of Technical Staff](#resume-research-engineer):** Python (production), PyTorch, PyTorch internals, ML fundamentals, Deep learning & transformers, Data structures & algorithms, Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), Training-run debugging, LLM evaluation (golden sets, calibrated judges, CI gates), Profiling & roofline (Nsight), Data pipelines & quality | — | Linux, C++, Continuous batching & KV cache, vLLM / SGLang / TensorRT-LLM, Reinforcement learning, Research methods & re-implementation |
| **C2** Science | **[Research Scientist (LLM research)](#resume-research-scientist):** ML fundamentals, Python (production), PyTorch, Deep learning & transformers, Research methods & re-implementation, Linear algebra, LLM APIs & tool calling, Data structures & algorithms, Novel research & publications, Clear writing & presenting, Reinforcement learning, Post-training (SFT, preference, RL), LLM evaluation (golden sets, calibrated judges, CI gates) | **[Frontier AI Safety / Alignment Researcher](#resume-ai-safety-researcher):** Safety & capability evals, Alignment methods, Interpretability, Red-teaming | Eval statistics (CIs, power, pass^k), C++, Distributed training (FSDP2, TP/PP, MoE) |
| **D1** Serving & kernels | **[Inference / LLM Serving Engineer](#resume-inference-engineer):** Python (production), C++, GPU fundamentals (HBM, prefill vs decode), PyTorch internals, System design, vLLM / SGLang / TensorRT-LLM, Kubernetes, Continuous batching & KV cache, Speculative decoding, Quantisation (FP8/FP4, AWQ, GPTQ), TP/PP & MoE serving, Load testing & latency SLOs, Profiling & roofline (Nsight), Cost & latency engineering | **[GPU Kernel / ML Compiler Engineer](#resume-gpu-kernel-engineer):** CUDA / Triton / CUTLASS, Linear algebra, Attention, GEMM & quantised kernels, GPU memory performance, Numerics validation, ML compilers (XLA, TorchInductor) | Linux, Model supply chain & CVEs, Observability (OpenTelemetry traces, metrics), Constrained decoding, Token & unit economics |
| **D2** Platform & infrastructure | **[AI Infrastructure / GPU Platform Engineer](#resume-ai-infrastructure-engineer):** Linux, Kubernetes, Networking, Terraform / IaC, Python (production), SRE (SLOs, on-call, incidents), Observability (OpenTelemetry traces, metrics), Git & CI/CD, Docker, AWS / Azure / GCP, GPU fleet ops & scheduling, System design, NCCL / RDMA / InfiniBand, Checkpointing & storage throughput, Hardware-fault reliability, Capacity & GPU/API cost governance | **[ML Platform / MLOps](#resume-ml-platform-engineer):** KServe / Ray Serve, LLM gateways, OAuth/OIDC, RBAC, SSO, MLOps lifecycle (model & prompt CI/CD), Model supply chain & CVEs, vLLM / SGLang / TensorRT-LLM | Go / Java, KServe / Ray Serve, vLLM / SGLang / TensorRT-LLM, MCP (Model Context Protocol) |
| **D3** Security | **[AI Security Engineer / AI Red Teamer](#resume-ai-security-engineer):** AppSec & threat modelling, Python (production), OAuth/OIDC, RBAC, SSO, Incident response & SIEM, LLM security (prompt injection, OWASP), Prompt-injection attack & defence, Agent abuse & MCP authorisation, Model supply chain & CVEs, Containment (DLP, sandboxing, egress), Red-teaming, GRC & risk assessment, AWS / Azure / GCP | — | MCP (Model Context Protocol), Observability (OpenTelemetry traces, metrics), Docker, Kubernetes |
| **E1** Product | **[AI Product Manager](#resume-ai-product-manager):** Product management, Stakeholder communication, AI literacy (tokens, RAG vs fine-tune, cost), Leadership & mentoring, GRC & risk assessment, Rubrics & inter-rater agreement, Metrics for non-deterministic systems, Token & unit economics, Pilots & adoption measurement, Python/SQL (notebook level), Risk & compliance docs (Annex IV, model cards) | — | Agents & tool use, Human-in-the-loop design, Domain expertise, Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **E2** Governance & assurance | **[AI Governance Programme Lead / Manager](#resume-ai-governance-lead):** GRC & risk assessment, EU AI Act / NIST AI RMF / ISO 42001, Stakeholder communication, AI inventory & risk register, Sector rules (SR 26-2, LL144, DPDP), Content provenance (EU AI Act Art. 50), Privacy law & DPO duties, Observability (OpenTelemetry traces, metrics), Python/SQL (notebook level), AI operating model & governance boards | **[AI Risk, Audit & Compliance Specialist](#resume-ai-risk-assurance-specialist):** Audit methodology, Model validation, Fairness & explainability tools, Risk & compliance docs (Annex IV, model cards), Technical writing; **[Responsible AI / AI Governance Engineer](#resume-responsible-ai-engineer):** Python (production), ML fundamentals, Risk & compliance docs (Annex IV, model cards), Guardrails, LLM evaluation (golden sets, calibrated judges, CI gates), Fairness & explainability tools | Technical writing |
| **E3** Domain evaluation | **[Domain Evaluation Specialist / AI Trainer](#resume-domain-evaluation-specialist):** Domain expertise, Clear writing & presenting, Rubrics & inter-rater agreement, Error analysis, Annotation workflows, Benchmark construction | — | AI literacy (tokens, RAG vs fine-tune, cost), Red-teaming, Eval statistics (CIs, power, pass^k), Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **L1** AI Engineering Manager / Director | **[AI Engineering Manager / Director](#resume-ai-engineering-manager):** Leadership & mentoring, Stakeholder communication, GRC & risk assessment, System design, LLM evaluation (golden sets, calibrated judges, CI gates), Observability (OpenTelemetry traces, metrics), Capacity & GPU/API cost governance, Guardrails, AI strategy & portfolio | — | Agents & tool use, Token & unit economics, AI literacy (tokens, RAG vs fine-tune, cost), MLOps lifecycle (model & prompt CI/CD), SRE (SLOs, on-call, incidents), Python (production) |
| **L2** VP / Head of AI / CAIO | **[VP / Head of AI / CAIO](#resume-vp-head-of-ai):** AI strategy & portfolio, Leadership & mentoring, Stakeholder communication, AI operating model & governance boards, EU AI Act / NIST AI RMF / ISO 42001, Token & unit economics, Capacity & GPU/API cost governance | — | GRC & risk assessment, Product management, AI literacy (tokens, RAG vs fine-tune, cost), LLM evaluation (golden sets, calibrated judges, CI gates), Change management & adoption, AI inventory & risk register |
<!-- END GENERATED -->

---

<a id="roles"></a>
## 4. Role-by-role matrix (sorted by GenAI target order; leadership last)

<!-- BEGIN GENERATED: scripts/build_resume_matrix.py (role blocks) -->
<a id="resume-ai-engineer"></a>
#### #1 · AI Engineer · variant A1
*Basis: JD-measured (JobsPipe 2026-11-02) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, Agents & tool use, RAG |
| **Important** | LLM evaluation (golden sets, calibrated judges, CI gates), Retrieval quality (hybrid, reranking, recall@k), Agent reliability (durable state, budgets, approvals), Cost & latency engineering, Observability (OpenTelemetry traces, metrics), LLM security (prompt injection, OWASP), Prompt & context design, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search |
| **Should** | APIs & integrations, Docker, SQL, Agent frameworks (LangGraph, Agents SDKs), TypeScript / JavaScript, System design, Guardrails, Embedding & reranker models, Error analysis, Human-in-the-loop design, Load testing & latency SLOs, Stakeholder communication, Token & unit economics |
| **Optional** | MCP (Model Context Protocol), Self-hosting open models, Fine-tuning (SFT, LoRA), Constrained decoding, Managed AI (Bedrock, Azure OpenAI, Vertex), Kubernetes, Domain expertise |
| **Avoid** | Wrapper-only demos; framework-syntax mastery as a headline; new RAGAS dependencies; "Prompt Engineer" as your title |

- **Prerequisites:** No formal gate. JD labels: senior 24.6%, entry 7.0%; T0-03 "Senior AI Engineer" cut assumes 5+ years [B]. 72% of AI-engineering postings state a degree requirement [C · T0-06].
- **Proof to show:** An evaluated end-to-end system over a real corpus (metrics table, cost/latency budget, reproducible README); for T2–T3, a second system with a different failure surface plus CI-gated evals, traces, a load test and a postmortem.
- **Posting terms to mirror:** Python (78.4%), LLM (76.7%), agentic AI (59.3%), RAG (54.0%), machine learning (39.8%), generative AI (37.6%), AWS / Azure (35.1% each), CI/CD (34.4%), vector databases (32.6%), prompt engineering (31.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-engineer.md)

<a id="resume-ml-engineer"></a>
#### #2 · Machine Learning Engineer (GenAI/LLM track) · variant B1
*Basis: JD-measured (JobsPipe 2026-11-02) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Deep learning & transformers |
| **Important** | LLM APIs & tool calling, Data structures & algorithms, TensorFlow / JAX, Experiment design & A/B testing, C++, Fine-tuning (SFT, LoRA), LLM evaluation (golden sets, calibrated judges, CI gates), Serving literacy (vLLM, batching, quantisation), Embedding & reranker models, Data pipelines & quality, Eval statistics (CIs, power, pass^k) |
| **Should** | SQL, Git & CI/CD, Docker, AWS / Azure / GCP, RAG, Stakeholder communication, APIs & integrations, Linear algebra, System design, Error analysis, Quantisation (FP8/FP4, AWQ, GPTQ) |
| **Optional** | Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), CUDA / Triton / CUTLASS, Recommender systems, MLOps lifecycle (model & prompt CI/CD), Kubernetes, Domain expertise |
| **Avoid** | Fine-tuning as the default answer (70% of 20 studied production systems used off-the-shelf models); tools you have only read about |

- **Prerequisites:** Degree common (72% of AI-engineering postings state one [C]). JD labels: entry 13.7%, senior 23.2%. DS → MLE 6–18 months; PhD → applied roles ~8 months [D · T0-06].
- **Proof to show:** A baseline-first model with measured lift and error analysis; a prompt vs RAG vs fine-tune comparison with cost and quality; a serving benchmark (tokens/s, p95, $/M tokens); small-budget training evidence (FSDP2 smoke tests, MFU).
- **Posting terms to mirror:** machine learning (98.6%), Python (71.3%), PyTorch (48.2%), LLM (45.0%), data structures (33.7%), deep learning (32.6%), TensorFlow (31.8%), A/B testing (23.5%), NLP (23.3%), C++ (23.3%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ml-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ml-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ml-engineer.md)

<a id="resume-research-engineer"></a>
#### #3 · Research Engineer / Member of Technical Staff · variant C1
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), PyTorch, PyTorch internals, ML fundamentals, Deep learning & transformers, Data structures & algorithms |
| **Important** | Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), Training-run debugging, LLM evaluation (golden sets, calibrated judges, CI gates), Profiling & roofline (Nsight), Data pipelines & quality |
| **Should** | Linux, C++, Continuous batching & KV cache, vLLM / SGLang / TensorRT-LLM, Reinforcement learning, Research methods & re-implementation |
| **Optional** | Pre-training at scale, CUDA / Triton / CUTLASS, TPU / Trainium / ROCm, Numerics validation, Kubernetes, Novel research & publications |
| **Avoid** | Listing frameworks without scale evidence; claiming research taste without artifacts |

- **Prerequisites:** PhD-level profile, a fellowship (Anthropic Fellows: no PhD required) or strong OSS (vLLM, SGLang).
- **Proof to show:** Paper re-implementations with rigorous evals; a nano-vLLM-style engine benchmarked against vLLM; DDP/FSDP2 smoke tests; upstream OSS contributions; fellowship projects.
- **Posting terms to mirror:** Member of Technical Staff, research engineer, PyTorch, distributed training, post-training, RL / RLHF, evals.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-research-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-research-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/research-engineer.md)

<a id="resume-forward-deployed-engineer"></a>
#### #4 · Forward Deployed Engineer (AI) · variant A2
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), APIs & integrations, LLM APIs & tool calling, RAG, Customer scoping & demos |
| **Important** | Retrieval quality (hybrid, reranking, recall@k), OAuth/OIDC, RBAC, SSO, Agents & tool use, LLM evaluation (golden sets, calibrated judges, CI gates), Domain expertise, Stakeholder communication |
| **Should** | TypeScript / JavaScript, AWS / Azure / GCP, Docker, SQL, Data pipelines & quality, Managed AI (Bedrock, Azure OpenAI, Vertex), Agent reliability (durable state, budgets, approvals), System design |
| **Optional** | Self-hosting open models, Product management, MCP (Model Context Protocol), Change management & adoption, AppSec & threat modelling, Pre-sales, Agent frameworks (LangGraph, Agents SDKs) |
| **Avoid** | A pre-sales-only story with no production code; vague "AI solutions" claims without customer outcomes |

- **Prerequisites:** One JD: 2–6 years and up to 50% travel [B · T0-01]. Only ~48% of the cluster is engineer-titled, so target those titles.
- **Proof to show:** A customer pilot case study with numbers; a demo on real data shown to at least two potential users; a deployment write-up that covers failure modes.
- **Posting terms to mirror:** forward deployed, FDE, customer-facing, deployment, integration, RAG, agents, travel.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-forward-deployed-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-forward-deployed-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/forward-deployed-engineer.md)

<a id="resume-applied-scientist"></a>
#### #5 · Applied Scientist (GenAI/LLM teams) · variant B2
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Experiment design & A/B testing, Data structures & algorithms |
| **Important** | SQL, LLM APIs & tool calling, Research-to-production, Eval statistics (CIs, power, pass^k), Fine-tuning (SFT, LoRA), Causal inference, Research methods & re-implementation, Deep learning & transformers |
| **Should** | LLM evaluation (golden sets, calibrated judges, CI gates), Data pipelines & quality, Stakeholder communication, AWS / Azure / GCP, Testing (pytest), Git & CI/CD, Docker, Recommender systems |
| **Optional** | Post-training (SFT, preference, RL), Distributed training (FSDP2, TP/PP, MoE), Novel research & publications, Domain expertise |
| **Avoid** | A publication list with no shipped systems; claims of "state of the art" without baselines |

- **Prerequisites:** Often a PhD (T2-01 names Applied Scientist as the main high-volume PhD corridor); coding/DSA is the usual gap for PhDs.
- **Proof to show:** Your own method turned into a service with tests and CI; at least three code reviews via OSS PRs; an eval-statistics write-up.
- **Posting terms to mirror:** applied scientist, machine learning, statistics, experimentation, A/B testing, LLM, PyTorch.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-applied-scientist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-applied-scientist) · [Complete typed inventory](../03-skills-and-tech/inventories/applied-scientist.md)

<a id="resume-applied-ai-engineer"></a>
#### #6 · Applied AI Engineer · variant A2
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, RAG, Agents & tool use |
| **Important** | Customer scoping & demos, LLM evaluation (golden sets, calibrated judges, CI gates), Guardrails, Prompt & context design, Technical writing, Retrieval quality (hybrid, reranking, recall@k), ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search |
| **Should** | APIs & integrations, Docker, Agent frameworks (LangGraph, Agents SDKs), Observability (OpenTelemetry traces, metrics), Cost & latency engineering, Stakeholder communication, TypeScript / JavaScript |
| **Optional** | Fine-tuning (SFT, LoRA), MCP (Model Context Protocol), Managed AI (Bedrock, Azure OpenAI, Vertex), Domain expertise |
| **Avoid** | Generic chatbot demos; no evidence of working with external users |

- **Prerequisites:** Lab-tier hiring bar on top of the AI Engineer stack; backend (~6 months) and PhD (~8 months) routes [D · T0-06].
- **Proof to show:** A customer-facing reference implementation with evals and a published write-up; the AI Engineer T2–T3 portfolio.
- **Posting terms to mirror:** applied AI, LLM, customers, evals, deployment, solutions, safety.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-applied-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-applied-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/applied-ai-engineer.md)

<a id="resume-ai-infrastructure-engineer"></a>
#### #7 · AI Infrastructure / GPU Platform Engineer · variant D2
*Basis: Catalog tiers + DevOps/SRE feeder JD shares.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Linux, Kubernetes, Networking, Terraform / IaC, Python (production), SRE (SLOs, on-call, incidents), Observability (OpenTelemetry traces, metrics) |
| **Important** | Git & CI/CD, Docker, AWS / Azure / GCP, GPU fleet ops & scheduling, System design, NCCL / RDMA / InfiniBand, Checkpointing & storage throughput, Hardware-fault reliability, Capacity & GPU/API cost governance |
| **Should** | Go / Java, KServe / Ray Serve, vLLM / SGLang / TensorRT-LLM |
| **Optional** | Prefill/decode disaggregation, TPU / Trainium / ROCm, Profiling & roofline (Nsight) |
| **Avoid** | Listing SLURM or storage products you have not run (not named in the research corpus); generic DevOps bullets with no GPU scale |

- **Prerequisites:** Infrastructure depth; best feeders are SRE, DevOps and backend infrastructure engineers.
- **Proof to show:** A self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem.
- **Posting terms to mirror:** GPU, Kubernetes, infrastructure, distributed systems, NCCL, InfiniBand, SRE, Terraform (DevOps JDs: Kubernetes 69.4%, Terraform 59.1%, Linux 45.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-infrastructure-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-infrastructure-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-infrastructure-engineer.md)

<a id="resume-research-scientist"></a>
#### #8 · Research Scientist (LLM research) · variant C2
*Basis: JD-measured (all-field research-scientist postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Deep learning & transformers, Research methods & re-implementation, Linear algebra |
| **Important** | LLM APIs & tool calling, Data structures & algorithms, Novel research & publications, Clear writing & presenting, Reinforcement learning, Post-training (SFT, preference, RL), LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Should** | C++, Distributed training (FSDP2, TP/PP, MoE), Eval statistics (CIs, power, pass^k) |
| **Optional** | Interpretability, Alignment methods, Pre-training at scale |
| **Avoid** | Unpublished claims of novelty; burying the publication list |

- **Prerequisites:** PhD plus publications; frontier offers are "not plannable" [D · T0-06].
- **Proof to show:** Papers, open research code, talks.
- **Posting terms to mirror:** Python (42.3%), communication (41.3%), machine learning (39.2%), PyTorch (25.4%), LLM (24.4%), deep learning (18.6%), C++ (17.4%), reinforcement learning (17.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-research-scientist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-research-scientist) · [Complete typed inventory](../03-skills-and-tech/inventories/research-scientist.md)

<a id="resume-inference-engineer"></a>
#### #9 · Inference / LLM Serving Engineer · variant D1
*Basis: Catalog tiers ([S]/[A]); named JDs at Anthropic, NVIDIA, Together AI, Baseten, Inferact.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), C++, GPU fundamentals (HBM, prefill vs decode), PyTorch internals, System design, vLLM / SGLang / TensorRT-LLM, Kubernetes |
| **Important** | Continuous batching & KV cache, Speculative decoding, Quantisation (FP8/FP4, AWQ, GPTQ), TP/PP & MoE serving, Load testing & latency SLOs, Profiling & roofline (Nsight), Cost & latency engineering |
| **Should** | Linux, Model supply chain & CVEs, Observability (OpenTelemetry traces, metrics), Constrained decoding, Token & unit economics |
| **Optional** | Prefill/decode disaggregation, CUDA / Triton / CUTLASS, NCCL / RDMA / InfiniBand, Engine internals & multi-LoRA, Numerics validation, Tile DSLs (Helion, CuteDSL) |
| **Avoid** | TGI (archived 2026-03-21); the removed trtllm-build static engine path; single-process load generators |

- **Prerequisites:** Backend → Staff-level inference takes ~10–14 months with infrastructure depth [D · T2-01].
- **Proof to show:** A single-GPU serving study (BF16 vs FP8/4-bit, prefix caching, chunked prefill, speculative decoding) with a roofline and $/M tokens at the SLO; a custom Triton kernel tested against a reference; an upstream PR to vLLM, SGLang or FlashInfer.
- **Posting terms to mirror:** inference, vLLM, SGLang, TensorRT-LLM, KV cache, latency, throughput, quantization, CUDA.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-inference-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-inference-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/inference-engineer.md)

<a id="resume-agentic-ai-engineer"></a>
#### #10 · Agentic AI Engineer · variant A1
*Basis: T0-16 title shares (LangGraph 35.8%, MCP 13.8%) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, Agents & tool use, Prompt & context design |
| **Important** | Agent reliability (durable state, budgets, approvals), MCP (Model Context Protocol), Containment (DLP, sandboxing, egress), LLM evaluation (golden sets, calibrated judges, CI gates), LLM security (prompt injection, OWASP), Agent frameworks (LangGraph, Agents SDKs), Human-in-the-loop design |
| **Should** | RAG, Observability (OpenTelemetry traces, metrics), AWS / Azure / GCP, TypeScript / JavaScript, Git & CI/CD, Kubernetes, SQL, Docker, Token & unit economics |
| **Optional** | Coding-agent rollout, Constrained decoding, Retrieval quality (hybrid, reranking, recall@k), Domain expertise |
| **Avoid** | AutoGen (dormant); CrewAI as a headline (absent from tier-1 lab postings); demo agents with no failure handling |

- **Prerequisites:** Usually an AI Engineer title in practice; the standalone title is small (~66 + 28 postings in 90 days).
- **Proof to show:** An agent with human approval, sandboxed tools, deterministic trace replay and failure-injection tests (timeouts, malformed arguments, prompt injection), reporting cost per task.
- **Posting terms to mirror:** agentic AI, agents, multi-agent, LangGraph (35.8% of Agentic AI Engineer postings), LangChain, MCP, tool calling.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-agentic-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-agentic-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/agentic-ai-engineer.md)

<a id="resume-ml-platform-engineer"></a>
#### #11 · ML Platform / MLOps (LLMOps) Engineer · variant D2
*Basis: Catalog tiers + DevOps feeder JD shares.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Kubernetes, Terraform / IaC, Git & CI/CD, Docker, Python (production), AWS / Azure / GCP, Observability (OpenTelemetry traces, metrics) |
| **Important** | Linux, KServe / Ray Serve, LLM gateways, OAuth/OIDC, RBAC, SSO, MLOps lifecycle (model & prompt CI/CD), Model supply chain & CVEs, SRE (SLOs, on-call, incidents), vLLM / SGLang / TensorRT-LLM |
| **Should** | MCP (Model Context Protocol), Capacity & GPU/API cost governance, Go / Java |
| **Optional** | Engine internals & multi-LoRA, Prefill/decode disaggregation, GPU fleet ops & scheduling |
| **Avoid** | Generic DevOps bullets with no model-serving scope |

- **Prerequisites:** Backend, DevOps or SRE background; India GCCs use the MLOps Engineer title (Taggd, C).
- **Proof to show:** A self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, dynamic LoRA routing and Grafana dashboards.
- **Posting terms to mirror:** MLOps, LLMOps, Kubernetes (69.4% of DevOps postings), Terraform (59.1%), CI/CD (81.2%), model serving, KServe, monitoring.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ml-platform-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ml-platform-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ml-platform-engineer.md)

<a id="resume-ai-product-manager"></a>
#### #12 · AI Product Manager · variant E1
*Basis: JD-measured (all PM postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Product management, Stakeholder communication, AI literacy (tokens, RAG vs fine-tune, cost) |
| **Important** | Leadership & mentoring, GRC & risk assessment, Rubrics & inter-rater agreement, Metrics for non-deterministic systems, Token & unit economics, Pilots & adoption measurement, Python/SQL (notebook level), Risk & compliance docs (Annex IV, model cards) |
| **Should** | Agents & tool use, Human-in-the-loop design, Domain expertise, Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Optional** | MCP (Model Context Protocol), AI strategy & portfolio |
| **Avoid** | "AI-powered" buzzwords without a shipped model feature or metrics |

- **Prerequisites:** 4+ years as a PM plus at least one shipped model-powered feature [D · T0-06]; T2-01 asks for 5+ years in product/ops plus notebook-level Python.
- **Proof to show:** A PRD plus eval rubric plus pilot metrics; a domain rubric with 50+ labelled cases; "10 failure modes ranked by business impact".
- **Posting terms to mirror:** product management (92.6%), communication (53.7%), leadership (40.1%), compliance (26.1%), agile (22.7%), roadmapping (18.4%), AI (15.4%), stakeholder management (14.2%), agentic AI (13.6%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-product-manager) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-product-manager) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-product-manager.md)

<a id="resume-ai-evaluation-engineer"></a>
#### #13 · AI Evaluation Engineer · variant A1
*Basis: Catalog tiers; evals in 19.0% of S09 postings (68.2% of companies).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM evaluation (golden sets, calibrated judges, CI gates), Testing (pytest), LLM APIs & tool calling |
| **Important** | Eval statistics (CIs, power, pass^k), Error analysis, Experiment design & A/B testing, Retrieval quality (hybrid, reranking, recall@k), Benchmark construction, Git & CI/CD, Rubrics & inter-rater agreement |
| **Should** | Observability (OpenTelemetry traces, metrics), SQL, RAG, Agents & tool use, Metrics for non-deterministic systems |
| **Optional** | Safety & capability evals, Red-teaming, Annotation workflows, Domain expertise |
| **Avoid** | New RAGAS dependencies (dormant since Feb 2026); storing master API keys in SaaS eval platforms; "accuracy" claims without CIs |

- **Prerequisites:** Best feeders: data scientists (error analysis), PhDs (measurement rigour), backend engineers (CI, observability) [D · T0-06].
- **Proof to show:** An eval harness with a kappa-calibrated judge validated on 100+ human labels, plus position and verbosity bias tests; a CI regression threshold and a cost–quality frontier chart.
- **Posting terms to mirror:** LLM evaluation, evals, benchmarking, LLM-as-a-judge, golden dataset, A/B testing, pytest.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-evaluation-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-evaluation-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-evaluation-engineer.md)

<a id="resume-ai-solutions-architect"></a>
#### #14 · AI / GenAI Solutions Architect · variant A2
*Basis: JD-measured (all Solutions Architect postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AWS / Azure / GCP, GenAI reference architectures, Stakeholder communication |
| **Important** | Leadership & mentoring, GRC & risk assessment, Python (production), Managed AI (Bedrock, Azure OpenAI, Vertex), Cost & latency engineering, Token & unit economics, OAuth/OIDC, RBAC, SSO, Pre-sales |
| **Should** | RAG, Agents & tool use, Terraform / IaC, Networking, Kubernetes, Customer scoping & demos |
| **Optional** | LLM gateways, Self-hosting open models, AI strategy & portfolio, Agent frameworks (LangGraph, Agents SDKs), MCP (Model Context Protocol), Domain expertise |
| **Avoid** | Certification lists in place of delivered architectures |

- **Prerequisites:** Senior engineer / cloud architect background. Certifications (AIP-C01, PMLE, AI-103) are tie-breakers mainly in IT-services, staffing and partner channels [B/C · T0-11].
- **Proof to show:** A reference architecture with a cost model and a working infrastructure-as-code deployment.
- **Posting terms to mirror:** solutions architect, AWS (53.6%), Azure (29.5%), GCP (22.6%), leadership (43.0%), communication (42.9%), mentoring (35.1%), compliance (25.3%), Python (23.6%), AI (23.2%), generative AI (17.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-solutions-architect) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-solutions-architect) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-solutions-architect.md)

<a id="resume-gpu-kernel-engineer"></a>
#### #15 · GPU Kernel / ML Compiler Engineer · variant D1
*Basis: Catalog tiers ([S]); kernels in 6.6% of S09 postings.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | C++, CUDA / Triton / CUTLASS, GPU fundamentals (HBM, prefill vs decode), Linear algebra, Profiling & roofline (Nsight) |
| **Important** | Attention, GEMM & quantised kernels, GPU memory performance, Numerics validation, ML compilers (XLA, TorchInductor), Quantisation (FP8/FP4, AWQ, GPTQ) |
| **Should** | Python (production), PyTorch internals |
| **Optional** | Tile DSLs (Helion, CuteDSL), TPU / Trainium / ROCm, NCCL / RDMA / InfiniBand |
| **Avoid** | Raw-kernel claims without benchmarks and correctness tests |

- **Prerequisites:** Systems / C++ / CUDA background or a PhD.
- **Proof to show:** GPU MODE leaderboard submissions; kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware with correctness tests.
- **Posting terms to mirror:** CUDA, Triton, CUTLASS, kernels, GPU, compiler, XLA, performance.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-gpu-kernel-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-gpu-kernel-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/gpu-kernel-engineer.md)

<a id="resume-ai-security-engineer"></a>
#### #16 · AI Security Engineer / AI Red Teamer · variant D3
*Basis: Security Engineer feeder JD shares + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AppSec & threat modelling, Python (production), OAuth/OIDC, RBAC, SSO, Incident response & SIEM, LLM security (prompt injection, OWASP) |
| **Important** | Prompt-injection attack & defence, Agent abuse & MCP authorisation, Model supply chain & CVEs, Containment (DLP, sandboxing, egress), Red-teaming, GRC & risk assessment, AWS / Azure / GCP |
| **Should** | MCP (Model Context Protocol), Observability (OpenTelemetry traces, metrics), Docker, Kubernetes |
| **Optional** | Safety & capability evals |
| **Avoid** | Classifier-only defences presented as complete (adaptive attacks beat 12 published defences) |

- **Prerequisites:** Application-security background; Anthropic AI Security Fellow requires US/UK/Canada work authorisation [A · T0-12].
- **Proof to show:** A red-team suite in CI against a working agent, with attack-success rates before and after mitigation; an MCP security audit.
- **Posting terms to mirror:** application security (26.5% of Security Engineer postings), cybersecurity (42.3%), Python (45.7%), IAM (21.6%), incident response (32.4%), AI security, prompt injection, red team, OWASP.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-security-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-security-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-security-engineer.md)

<a id="resume-ai-governance-lead"></a>
#### #17 · AI Governance Programme Lead / Manager · variant E2
*Basis: Axial shares (C) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | GRC & risk assessment, EU AI Act / NIST AI RMF / ISO 42001, Stakeholder communication, AI inventory & risk register |
| **Important** | Sector rules (SR 26-2, LL144, DPDP), Content provenance (EU AI Act Art. 50), Privacy law & DPO duties, Observability (OpenTelemetry traces, metrics), Python/SQL (notebook level), AI operating model & governance boards |
| **Should** | Technical writing, Risk & compliance docs (Annex IV, model cards), AI literacy (tokens, RAG vs fine-tune, cost), Leadership & mentoring |
| **Optional** | Audit methodology |
| **Avoid** | Listing AIGP as your main credential (domain certifications come first) |

- **Prerequisites:** About 5 years in GRC, privacy, audit or security; domain certifications first (CIPP/CIPM, CISSP/CISA/CRISC); AIGP optional [B · T0-15].
- **Proof to show:** An AI inventory, risk register and governance playbook mapped to the EU AI Act, NIST AI RMF and ISO 42001.
- **Posting terms to mirror:** AI governance, EU AI Act, NIST AI RMF, ISO 42001, risk management, compliance, privacy; Axial: observability/monitoring 42.3%, Python 27.1%.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-governance-lead) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-governance-lead) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-governance-lead.md)

<a id="resume-physical-ai-engineer"></a>
#### #18 · Physical AI / Robotics AI Engineer · variant B3
*Basis: Practice-curated ([P]); no skill measurements in the corpus.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Robotics fundamentals, C++, Python (production), Perception / computer vision, Simulation & sim-to-real, ROS |
| **Important** | Robot learning & VLA models, Edge inference, Teleoperation data pipelines, Safety cases |
| **Should** | PyTorch, Deep learning & transformers, Quantisation (FP8/FP4, AWQ, GPTQ), Reinforcement learning, Linux, Docker, Data pipelines & quality |
| **Optional** | CUDA / Triton / CUTLASS |
| **Avoid** | Simulation-only results presented as real-world performance |

- **Prerequisites:** Robotics or controls background with ML.
- **Proof to show:** A sim-to-real or manipulation project with measured success rates and failure analysis.
- **Posting terms to mirror:** robotics, VLA, imitation learning, reinforcement learning, sim-to-real, ROS, perception.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-physical-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-physical-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/physical-ai-engineer.md)

<a id="resume-ai-safety-researcher"></a>
#### #19 · Frontier AI Safety / Alignment Researcher · variant C2
*Basis: Catalog tiers ([S]/[P]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Research methods & re-implementation |
| **Important** | Safety & capability evals, Alignment methods, Interpretability, Red-teaming, Novel research & publications |
| **Should** | Deep learning & transformers, LLM evaluation (golden sets, calibrated judges, CI gates), Reinforcement learning, Eval statistics (CIs, power, pass^k) |
| **Optional** | Post-training (SFT, preference, RL) |
| **Avoid** | Opinion pieces in place of experiments |

- **Prerequisites:** PhD or a fellowship is typical; ~600 technical FTEs worldwide (single-author estimate, C).
- **Proof to show:** Fellowship projects; published safety research; open eval contributions.
- **Posting terms to mirror:** AI safety, alignment, interpretability, evaluations, red teaming.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-safety-researcher) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-safety-researcher) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-safety-researcher.md)

<a id="resume-ai-enablement-engineer"></a>
#### #20 · AI Enablement Engineer · variant A1
*Basis: Catalog tiers; MCP named in 30.2% of these postings (T0-16).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, Internal tooling & DevEx, OAuth/OIDC, RBAC, SSO |
| **Important** | MCP (Model Context Protocol), Agents & tool use, Guardrails, Change management & adoption, LLM gateways, Coding-agent rollout, Pilots & adoption measurement |
| **Should** | RAG, Observability (OpenTelemetry traces, metrics), AWS / Azure / GCP, TypeScript / JavaScript, Token & unit economics, Metrics for non-deterministic systems, Technical writing, Stakeholder communication, AI inventory & risk register |
| **Optional** | Kubernetes, Docker, Agent frameworks (LangGraph, Agents SDKs), Domain expertise |
| **Avoid** | Adoption claims without usage or time-saved numbers |

- **Prerequisites:** Backend/DevEx engineers; a non-technical ops lane exists (~7 months) [D · T0-06].
- **Proof to show:** An internal pilot with 5–10 colleagues measuring adoption and time saved, with a runbook and a risk register.
- **Posting terms to mirror:** AI enablement, MCP, internal tools, copilot, developer productivity, adoption.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-enablement-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-enablement-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-enablement-engineer.md)

<a id="resume-ai-product-engineer"></a>
#### #21 · AI Product Engineer (AI Frontend) · variant A1
*Basis: JD-measured (Full-Stack Engineer postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | React, TypeScript / JavaScript, APIs & integrations, LLM APIs & tool calling |
| **Important** | Python (production), AWS / Azure / GCP, Git & CI/CD, Streaming & agent UX, Agent-UX telemetry, LLM evaluation (golden sets, calibrated judges, CI gates), Human-in-the-loop design |
| **Should** | RAG, Agents & tool use, Docker |
| **Optional** | On-device / WebGPU inference, MCP (Model Context Protocol) |
| **Avoid** | Pure UI work with no model-facing evidence |

- **Prerequisites:** Visible AI-frontend roles are Staff-level asking 5–6+ years [C/D · T0-06]; apply as "full-stack AI engineer".
- **Proof to show:** A full-stack app (frontend → API → LLM → eval) with 50 eval cases and UX metrics; an on-device module benchmarked on 3+ device/browser combinations.
- **Posting terms to mirror:** React (69.4%), TypeScript (52.7%), Python (41.8%), AWS (41.3%), CI/CD (37.8%), Node.js (32.3%), REST API (27.6%), streaming, LLM.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-product-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-product-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-product-engineer.md)

<a id="resume-ai-risk-assurance-specialist"></a>
#### #22 · AI Risk, Audit & Compliance Specialist · variant E2
*Basis: Catalog tiers ([S]/[B]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Audit methodology, GRC & risk assessment, Model validation, Privacy law & DPO duties |
| **Important** | EU AI Act / NIST AI RMF / ISO 42001, Sector rules (SR 26-2, LL144, DPDP), Fairness & explainability tools, Risk & compliance docs (Annex IV, model cards), Technical writing |
| **Should** | Stakeholder communication, Python/SQL (notebook level), AI inventory & risk register |
| **Optional** | Content provenance (EU AI Act Art. 50) |
| **Avoid** | Claiming GenAI risk ownership as settled (SR 26-2 excludes generative and agentic AI) |

- **Prerequisites:** CISA, CIA or CPA (required for the AAIA credential) [B · T0-15].
- **Proof to show:** A model-validation or bias-audit report on a public model, using a documented methodology.
- **Posting terms to mirror:** audit, model risk, AI risk, compliance, ISO 42001, bias audit, privacy.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-risk-assurance-specialist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-risk-assurance-specialist) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-risk-assurance-specialist.md)

<a id="resume-responsible-ai-engineer"></a>
#### #23 · Responsible AI / AI Governance Engineer · variant E2
*Basis: Catalog tiers ([S]); 13 JDs in T0-15.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), ML fundamentals, Risk & compliance docs (Annex IV, model cards) |
| **Important** | Guardrails, LLM evaluation (golden sets, calibrated judges, CI gates), EU AI Act / NIST AI RMF / ISO 42001, Fairness & explainability tools, Observability (OpenTelemetry traces, metrics) |
| **Should** | MLOps lifecycle (model & prompt CI/CD), Managed AI (Bedrock, Azure OpenAI, Vertex), Red-teaming, Prompt-injection attack & defence, AI inventory & risk register, Technical writing |
| **Optional** | Content provenance (EU AI Act Art. 50), Domain expertise |
| **Avoid** | Pre-1.0 tools (Guardrails AI, Giskard v3, c2pa-python) presented as production-hardened |

- **Prerequisites:** MLOps or security engineering background in a regulated firm.
- **Proof to show:** A compliance packet mapped to NIST AI 600-1 and the OWASP LLM Top 10, with runtime guardrails, subgroup evals and a calibrated judge on ~100 traces.
- **Posting terms to mirror:** responsible AI, AI governance, guardrails, fairness, explainability, EU AI Act, model cards.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-responsible-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-responsible-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/responsible-ai-engineer.md)

<a id="resume-domain-evaluation-specialist"></a>
#### #24 · Domain Evaluation Specialist / AI Trainer · variant E3
*Basis: Catalog tiers ([C]/[S]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Domain expertise, Clear writing & presenting, Rubrics & inter-rater agreement |
| **Important** | Error analysis, Annotation workflows, Benchmark construction |
| **Should** | AI literacy (tokens, RAG vs fine-tune, cost), Red-teaming, Eval statistics (CIs, power, pass^k), Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Optional** | Python/SQL (notebook level), GRC & risk assessment |
| **Avoid** | Generic "AI trainer" claims without domain credentials |

- **Prerequisites:** 4+ years in the domain; MA/JD/MD/PhD for premium rates [C · T0-06].
- **Proof to show:** A domain gold standard: 100+ real tasks with rubrics, adjudication rules and two-reviewer agreement, comparing 2–3 models with the human baseline.
- **Posting terms to mirror:** AI trainer, evaluation, rubric, annotation, RLHF, plus your domain terms.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-domain-evaluation-specialist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-domain-evaluation-specialist) · [Complete typed inventory](../03-skills-and-tech/inventories/domain-evaluation-specialist.md)

<a id="resume-ai-engineering-manager"></a>
#### L1 · AI Engineering Manager / Director · variant L1
*Basis: JD-measured (Engineering Manager postings) + catalog.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Leadership & mentoring, Stakeholder communication |
| **Important** | GRC & risk assessment, System design, LLM evaluation (golden sets, calibrated judges, CI gates), Observability (OpenTelemetry traces, metrics), Capacity & GPU/API cost governance, Guardrails, AI strategy & portfolio |
| **Should** | Agents & tool use, Token & unit economics, AI literacy (tokens, RAG vs fine-tune, cost), MLOps lifecycle (model & prompt CI/CD), SRE (SLOs, on-call, incidents), Python (production) |
| **Optional** | EU AI Act / NIST AI RMF / ISO 42001, Agent frameworks (LangGraph, Agents SDKs), AWS / Azure / GCP, Domain expertise |
| **Avoid** | Team-size bragging without delivery or quality metrics |

- **Prerequisites:** Senior/Staff IC first; AI engineers move into management in under 3 years on average (SignalFire, C).
- **Proof to show:** Delivery record: AI systems shipped, eval/observability practices adopted across teams, cost governance results.
- **Posting terms to mirror:** leadership (72.7%), communication (51.4%), mentoring (47.1%), compliance (30.9%), system design (25.3%), observability (18.0%), agentic AI (14.8%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-engineering-manager) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-engineering-manager.md)

<a id="resume-vp-head-of-ai"></a>
#### L2–L3 · VP / Head of AI / CAIO · variant L2
*Basis: Catalog ([P]/[B]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AI strategy & portfolio, Leadership & mentoring, Stakeholder communication |
| **Important** | AI operating model & governance boards, EU AI Act / NIST AI RMF / ISO 42001, Token & unit economics, Capacity & GPU/API cost governance |
| **Should** | GRC & risk assessment, Product management, AI literacy (tokens, RAG vs fine-tune, cost), LLM evaluation (golden sets, calibrated judges, CI gates), Change management & adoption, AI inventory & risk register |
| **Optional** | Sector rules (SR 26-2, LL144, DPDP), AWS / Azure / GCP |
| **Avoid** | Technology lists in place of business outcomes |

- **Prerequisites:** EM/Director track record; US federal CAIOs are required by OMB M-25-21 [B · T0-15].
- **Proof to show:** Portfolio outcomes: revenue or cost impact, governance boards stood up, vendor decisions.
- **Posting terms to mirror:** AI strategy, roadmap, governance, operating model, budget, build vs buy.
- **Links:** [Role profile: vp-head-of-ai](../02-roles/role-catalog.md#profile-vp-head-of-ai) · [Role profile: chief-ai-officer](../02-roles/role-catalog.md#profile-chief-ai-officer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/vp-head-of-ai.md)
<!-- END GENERATED -->

---
*Posting shares are JobsPipe measurements retrieved 2026-11-02 [B]. Practice-curated items are Grade D. Re-check against live postings at each recount; the next is due by 2026-12-01.*
