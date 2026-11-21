---
id: job-search.resume-matrix
title: "GenAI Resume Skills Matrix"
content_type: reference
stage: 6
status: published
last_verified: 2026-11-19
review_by: 2027-02-17
summary: "The concise skills section for every role (Must / Important / Should / Optional headline skills), shared skills across roles, and a skills-section blueprint per resume variant."
sources: [T0-03, T0-04, T0-10, T0-11, T0-13, T0-48, T0-49, T0-50, T0-51, T0-52, T0-53, T0-54, T0-55, T0-56, T0-57, T0-58, T0-59, T0-60, T0-61, T0-62, T0-63, T0-64, T0-65, T0-66, T0-69]
generated_by: "scripts/build_resume_matrix.py (generated blocks)"
---
# GenAI Resume Skills Matrix
## Must / Important / Should / Optional Skills for Every GenAI Role, With Resume-Variant Blueprints

> **Updated:** 2026-11-19 · **Scope:** Programmatic headline resume skills matrix generated from the typed skills ontology.
> **How to use it:** [resume-strategy.md](resume-strategy.md) explains the master → variant → per-posting system that these lists feed.
> **Role universe:** all 29 canonical roles of the [role catalog](../02-roles/role-catalog.md): the 24 individual-contributor roles in the order of the [GenAI target roles](../02-roles/genai-target-roles.md), plus the 5 leadership and independent tracks.
> **Sources:**
> - Tiers and evidence tags: [data/skills_ontology.json](../../data/skills_ontology.json), shown in full in the [role skill inventories](../03-skills-and-tech/role-skill-inventories.md).
> - JobsPipe job-description measurements (count date 2026-09-10, retrieved 2026-11-02, unchanged 2026-11-14 [B · T0-69 KF7]; [data/posting_skill_shares.json](../../data/posting_skill_shares.json)).
> - Skill shares and role dossiers from T0-03, T0-15, T0-16, RP2 dossiers T0-48 to T0-66 and T0-69.
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
| LLM evaluation (golden sets, calibrated judges, CI gates) | 9 (47%) | 13 (68%) |
| LLM APIs & tool calling | 9 (47%) | 9 (47%) |
| AWS / Azure / GCP | 7 (37%) | 12 (63%) |
| ML fundamentals | 7 (37%) | 7 (37%) |
| Git & CI/CD | 6 (32%) | 9 (47%) |
| Agents & tool use | 6 (32%) | 8 (42%) |
| PyTorch | 6 (32%) | 6 (32%) |
| RAG | 4 (21%) | 9 (47%) |
| C++ | 4 (21%) | 6 (32%) |
| Deep learning & transformers | 4 (21%) | 6 (32%) |
| OAuth/OIDC, RBAC, SSO | 4 (21%) | 5 (26%) |
| Data structures & algorithms | 4 (21%) | 4 (21%) |
| Retrieval quality (hybrid, reranking, recall@k) | 4 (21%) | 4 (21%) |
<!-- END GENERATED -->

Only Python is near-universal. LLM evaluation and LLM API work are shared by about half and a third of the engineering roles, respectively. Every other skill is family-specific, which is why resume variants are organised by role family (§3) rather than built from one universal list.

---

<a id="blueprints"></a>
## 3. Skills-section blueprints for each resume variant

Each variant is **anchored on its highest-ranked target role**: that role's Must and Important skills form the base skills section. For a posting from a sibling role, swap in the listed skills and drop the least relevant anchor items. "Hygiene" lists Should-tier skills shared by at least half of the variant's roles.

<!-- BEGIN GENERATED: scripts/build_resume_matrix.py (variant blueprints) -->
| Variant | Anchor role (base skills section = its Must + Important skills) | Swap in for sibling roles (their Must/Important skills the anchor lacks) | Hygiene: list if true |
|---|---|---|---|
| **A1** Builder | **[AI Engineer](#resume-ai-engineer):** Python (production), LLM APIs & tool calling, Agents & tool use, RAG, LLM evaluation (golden sets, calibrated judges, CI gates), Retrieval quality (hybrid, reranking, recall@k), Agent reliability (durable state, budgets, approvals), Cost & latency engineering, Observability (OpenTelemetry traces, metrics), LLM security (prompt injection, OWASP), Prompt & context design, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search, Product sense | **[Agentic AI Engineer](#resume-agentic-ai-engineer):** MCP (Model Context Protocol), Containment (DLP, sandboxing, egress), Agent frameworks (LangGraph, Agents SDKs), Human-in-the-loop design; **[AI Evaluation Engineer](#resume-ai-evaluation-engineer):** Testing (pytest), Eval statistics (CIs, power, pass^k), Error analysis, Experiment design & A/B testing, Benchmark construction, Human evaluation programmes, Rubrics & inter-rater agreement; **[AI Product Engineer](#resume-ai-product-engineer):** React, TypeScript / JavaScript, APIs & integrations, Streaming & agent UX, Agent-UX telemetry, Human-in-the-loop design; **[AI Enablement Engineer](#resume-ai-enablement-engineer):** Internal tooling & DevEx, Change management & adoption, Teaching & workshop delivery, MCP (Model Context Protocol), Guardrails, Coding agents & AI-assisted engineering, Pilots & adoption measurement, GRC & risk assessment | Docker, SQL, TypeScript / JavaScript, Token & unit economics |
| **A2** Deployer | **[Forward Deployed Engineer (AI)](#resume-forward-deployed-engineer):** Python (production), APIs & integrations, LLM APIs & tool calling, RAG, Customer scoping & demos, Retrieval quality (hybrid, reranking, recall@k), OAuth/OIDC, RBAC, SSO, Agents & tool use, LLM evaluation (golden sets, calibrated judges, CI gates), Domain expertise, Stakeholder communication, Customer-facing communication | **[Applied AI Engineer](#resume-applied-ai-engineer):** Guardrails, Prompt & context design, Technical writing, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search; **[AI / GenAI Solutions Architect](#resume-ai-solutions-architect):** AWS / Azure / GCP, GenAI reference architectures, Pre-sales, Leadership & mentoring, GRC & risk assessment, Managed AI (Bedrock, Azure OpenAI, Vertex), Cost & latency engineering, Token & unit economics | TypeScript / JavaScript, Docker, Observability (OpenTelemetry traces, metrics) |
| **B1** Engineer | **[Machine Learning Engineer (GenAI/LLM track)](#resume-ml-engineer):** ML fundamentals, Python (production), PyTorch, Deep learning & transformers, LLM APIs & tool calling, Data structures & algorithms, TensorFlow / JAX, Experiment design & A/B testing, C++, Fine-tuning (SFT, LoRA), LLM evaluation (golden sets, calibrated judges, CI gates), Serving literacy (vLLM, batching, quantisation), Embedding & reranker models, Data pipelines & quality, Eval statistics (CIs, power, pass^k) | — | SQL, Git & CI/CD, Docker, AWS / Azure / GCP, RAG, Stakeholder communication, APIs & integrations, Linear algebra, System design, Error analysis, Quantisation (FP8/FP4, AWQ, GPTQ) |
| **B2** Scientist | **[Applied Scientist (GenAI/LLM teams)](#resume-applied-scientist):** ML fundamentals, Python (production), PyTorch, Experiment design & A/B testing, Data structures & algorithms, Research-to-production, SQL, LLM APIs & tool calling, Eval statistics (CIs, power, pass^k), Fine-tuning (SFT, LoRA), Causal inference, Research methods & re-implementation, Deep learning & transformers | — | LLM evaluation (golden sets, calibrated judges, CI gates), Data pipelines & quality, Stakeholder communication, AWS / Azure / GCP, Testing (pytest), Git & CI/CD, Docker, Recommender systems |
| **B3** Robotics | **[Physical AI / Robotics AI Engineer](#resume-physical-ai-engineer):** Robotics fundamentals, C++, Python (production), Simulation & sim-to-real, ROS, Robot learning & VLA models, PyTorch, Real-robot deployment & hardware bring-up, Edge inference, Teleoperation data pipelines, Safety cases, Imitation learning, Computer vision & robot perception, Reinforcement learning | — | Deep learning & transformers, Quantisation (FP8/FP4, AWQ, GPTQ), Linux, Docker, Data pipelines & quality |
| **C1** Engineering | **[Research Engineer / Member of Technical Staff](#resume-research-engineer):** Python (production), PyTorch, PyTorch internals, ML fundamentals, Deep learning & transformers, Data structures & algorithms, Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), Training-run debugging, LLM evaluation (golden sets, calibrated judges, CI gates), Profiling & roofline (Nsight), Data pipelines & quality | — | Linux, C++, Continuous batching & KV cache, vLLM / SGLang / TensorRT-LLM, Reinforcement learning, Research methods & re-implementation |
| **C2** Science | **[Research Scientist (LLM research)](#resume-research-scientist):** ML fundamentals, Python (production), PyTorch, Deep learning & transformers, Research methods & re-implementation, Linear algebra, Novel research & publications, Data structures & algorithms, Clear writing & presenting, Reinforcement learning, Post-training (SFT, preference, RL), LLM evaluation (golden sets, calibrated judges, CI gates) | **[Frontier AI Safety / Alignment Researcher](#resume-ai-safety-researcher):** Safety & capability evals, Alignment methods, Interpretability, Red-teaming | Eval statistics (CIs, power, pass^k), C++, Distributed training (FSDP2, TP/PP, MoE) |
| **D1** Serving & kernels | **[Inference / LLM Serving Engineer](#resume-inference-engineer):** Python (production), C++, GPU fundamentals (HBM, prefill vs decode), PyTorch internals, System design, vLLM / SGLang / TensorRT-LLM, Kubernetes, Continuous batching & KV cache, Speculative decoding, Quantisation (FP8/FP4, AWQ, GPTQ), TP/PP & MoE serving, Load testing & latency SLOs, Profiling & roofline (Nsight), Cost & latency engineering | **[GPU Kernel / ML Compiler Engineer](#resume-gpu-kernel-engineer):** CUDA / Triton / CUTLASS, Attention, GEMM & quantised kernels, GPU memory performance, Numerics validation, ML compilers (XLA, TorchInductor), Upstream open-source contributions | Linux, Model supply chain & CVEs, Observability (OpenTelemetry traces, metrics), Constrained decoding, Token & unit economics, Linear algebra |
| **D2** Platform & infrastructure | **[AI Infrastructure / GPU Platform Engineer](#resume-ai-infrastructure-engineer):** Linux, Kubernetes, Networking, Terraform / IaC, Python (production), SRE (SLOs, on-call, incidents), Observability (OpenTelemetry traces, metrics), GPU fleet ops & scheduling, Git & CI/CD, Docker, AWS / Azure / GCP, System design, NCCL / RDMA / InfiniBand, Checkpointing & storage throughput, Hardware-fault reliability, Capacity & GPU/API cost governance | **[ML Platform / MLOps](#resume-ml-platform-engineer):** MLOps lifecycle (model & prompt CI/CD), KServe / Ray Serve, LLM gateways, OAuth/OIDC, RBAC, SSO, Model supply chain & CVEs, vLLM / SGLang / TensorRT-LLM | Go / Java, KServe / Ray Serve, vLLM / SGLang / TensorRT-LLM, MCP (Model Context Protocol) |
| **D3** Security | **[AI Security Engineer / AI Red Teamer](#resume-ai-security-engineer):** AppSec & threat modelling, Python (production), OAuth/OIDC, RBAC, SSO, Incident response & SIEM, LLM security (prompt injection, OWASP), Prompt-injection attack & defence, Red-teaming, Agent abuse & MCP authorisation, Model supply chain & CVEs, Containment (DLP, sandboxing, egress), AWS / Azure / GCP | — | MCP (Model Context Protocol), Observability (OpenTelemetry traces, metrics), Docker, Kubernetes |
| **E1** Product | **[AI Product Manager](#resume-ai-product-manager):** Product management, Stakeholder communication, AI literacy (tokens, RAG vs fine-tune, cost), Rubrics & inter-rater agreement, Leadership & mentoring, GRC & risk assessment, Metrics for non-deterministic systems, Token & unit economics, Pilots & adoption measurement, Product sense | — | Python/SQL (notebook level), Agents & tool use, Human-in-the-loop design, Domain expertise, Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **E2** Governance & assurance | **[AI Governance Programme Lead / Manager](#resume-ai-governance-lead):** GRC & risk assessment, EU AI Act / NIST AI RMF / ISO 42001, Stakeholder communication, AI inventory & risk register, Sector rules (SR 26-2, LL144, DPDP), Content provenance (EU AI Act Art. 50), Privacy law & DPO duties, Observability (OpenTelemetry traces, metrics), Python/SQL (notebook level), AI operating model & governance boards | **[AI Risk, Audit & Compliance Specialist](#resume-ai-risk-assurance-specialist):** Audit methodology, Model validation, Fairness & explainability tools, Risk & compliance docs (Annex IV, model cards), Technical writing; **[Responsible AI / AI Governance Engineer](#resume-responsible-ai-engineer):** Python (production), ML fundamentals, Risk & compliance docs (Annex IV, model cards), LLM evaluation (golden sets, calibrated judges, CI gates), Guardrails, Fairness & explainability tools | Technical writing |
| **E3** Domain evaluation | **[Domain Evaluation Specialist / AI Trainer](#resume-domain-evaluation-specialist):** Domain expertise, Clear writing & presenting, Rubrics & inter-rater agreement, Human evaluation programmes, Error analysis, Annotation workflows, Benchmark construction | — | AI literacy (tokens, RAG vs fine-tune, cost), Red-teaming, Eval statistics (CIs, power, pass^k), Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **L1** AI Engineering Manager / Director | **[AI Engineering Manager / Director](#resume-ai-engineering-manager):** Leadership & mentoring, Stakeholder communication, Technical leadership, System design, LLM evaluation (golden sets, calibrated judges, CI gates), Observability (OpenTelemetry traces, metrics), AI strategy & portfolio | — | Capacity & GPU/API cost governance, Agents & tool use, Token & unit economics, AI literacy (tokens, RAG vs fine-tune, cost), MLOps lifecycle (model & prompt CI/CD), SRE (SLOs, on-call, incidents), Python (production) |
| **L2** VP / Head of AI | **[VP / Head of AI](#resume-vp-head-of-ai):** AI strategy & portfolio, Leadership & mentoring, Stakeholder communication, AI operating model & governance boards, EU AI Act / NIST AI RMF / ISO 42001 | — | GRC & risk assessment, Product management, AI literacy (tokens, RAG vs fine-tune, cost), LLM evaluation (golden sets, calibrated judges, CI gates), Technical leadership, Change management & adoption, AI inventory & risk register |
| **L3** Chief AI Officer (CAIO) | **[Chief AI Officer](#resume-chief-ai-officer):** AI strategy & portfolio, GRC & risk assessment, Leadership & mentoring, Stakeholder communication, AI operating model & governance boards, Change management & adoption, Domain expertise | — | EU AI Act / NIST AI RMF / ISO 42001, LLM evaluation (golden sets, calibrated judges, CI gates), Privacy law & DPO duties |
| **L4** Independent AI Consultant / Contract Builder | **[Independent AI Consultant / Contract Builder](#resume-independent-ai-consultant):** Python (production), LLM APIs & tool calling, Agents & tool use, AWS / Azure / GCP, RAG, ML fundamentals, Stakeholder communication, Git & CI/CD, LLM evaluation (golden sets, calibrated judges, CI gates), APIs & integrations, Domain expertise, Customer-facing communication, MCP (Model Context Protocol) | — | Docker, SQL, MLOps lifecycle (model & prompt CI/CD), AI strategy & portfolio, GRC & risk assessment, Data pipelines & quality, Leadership & mentoring, Privacy law & DPO duties |
| **L5** Fractional AI Leader | **[Fractional AI Leader](#resume-fractional-ai-leader):** AI strategy & portfolio, GRC & risk assessment, Change management & adoption, Leadership & mentoring, Stakeholder communication, Agents & tool use, Domain expertise, Teaching & workshop delivery, AI operating model & governance boards | — | MLOps lifecycle (model & prompt CI/CD), LLM evaluation (golden sets, calibrated judges, CI gates), AWS / Azure / GCP, Privacy law & DPO duties |
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
| **Important** | LLM evaluation (golden sets, calibrated judges, CI gates), Retrieval quality (hybrid, reranking, recall@k), Agent reliability (durable state, budgets, approvals), Cost & latency engineering, Observability (OpenTelemetry traces, metrics), LLM security (prompt injection, OWASP), Prompt & context design, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search, Product sense |
| **Should** | APIs & integrations, Docker, SQL, Agent frameworks (LangGraph, Agents SDKs), TypeScript / JavaScript, System design, Guardrails, Embedding & reranker models, Error analysis, Human-in-the-loop design, Load testing & latency SLOs, Stakeholder communication, Token & unit economics, Coding agents & AI-assisted engineering |
| **Optional** | MCP (Model Context Protocol), Self-hosting open models, Fine-tuning (SFT, LoRA), Constrained decoding, Managed AI (Bedrock, Azure OpenAI, Vertex), Kubernetes, Domain expertise |
| **Avoid** | Wrapper-only demos; framework-syntax mastery as a headline; OpenAI Assistants API (retired 2026-08-26); "Prompt Engineer" as your title |

- **Prerequisites:** No formal gate. JD labels: senior 24.6%, entry 7.0%; T0-03 "Senior AI Engineer" cut assumes 5+ years [B]. About 72% of US AI-engineering postings state a degree [C · T0-06] and 75% of 903 Glassdoor US postings mention one (24% bachelor's, 24% master's, 28% PhD; "mention", not "require") [C · T0-23], while nearly 25% of AI postings in Atlanta Fed Lightcast data list no education requirement [A · T0-23].
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
| **Avoid** | Fine-tuning as the default answer (70%, 14/20 interviewed production agent teams in arXiv 2512.04123v2 used off-the-shelf models, B · T0-03); dormant torchtune workflows; tools you have only read about |

- **Prerequisites:** Degree common (72% in Axial Search [C · T0-06]; 75% of 903 Glassdoor US postings mention a degree [C · T0-23]; nearly 25% in Atlanta Fed Lightcast data list none [A · T0-23]). JD labels: entry 13.7%, senior 23.2%. DS → MLE 6–18 months; PhD → applied roles ~8 months [D · T0-06].
- **Proof to show:** A baseline-first model with measured lift and error analysis; a prompt vs RAG vs fine-tune comparison with cost and quality; a serving benchmark (tokens/s, p95, $/M tokens); small-budget training evidence (FSDP2 smoke tests, MFU).
- **Posting terms to mirror:** machine learning (98.6%), Python (71.3%), PyTorch (48.2%), LLM (45.0%), data structures (33.7%), deep learning (32.6%), TensorFlow (31.8%), A/B testing (23.5%), NLP (23.3%), C++ (23.3%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ml-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ml-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ml-engineer.md)

<a id="resume-applied-scientist"></a>
#### #3 · Applied Scientist (GenAI/LLM teams) · variant B2
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Experiment design & A/B testing, Data structures & algorithms, Research-to-production |
| **Important** | SQL, LLM APIs & tool calling, Eval statistics (CIs, power, pass^k), Fine-tuning (SFT, LoRA), Causal inference, Research methods & re-implementation, Deep learning & transformers |
| **Should** | LLM evaluation (golden sets, calibrated judges, CI gates), Data pipelines & quality, Stakeholder communication, AWS / Azure / GCP, Testing (pytest), Git & CI/CD, Docker, Recommender systems |
| **Optional** | Post-training (SFT, preference, RL), Distributed training (FSDP2, TP/PP, MoE), Novel research & publications, Domain expertise |
| **Avoid** | A publication list uncoupled from shipped production impact (publications/patents appear in 11/23 JDs, so pair them with production code); claims of 'state of the art' without baselines |

- **Prerequisites:** Amazon US uses PhD or Master's+4 (7/9), while Microsoft (BS+2/MS+1), Uber (BS+3–4/MS+2), Zalando (MS+2) and Mistral offer broader routes; coding/DSA is the usual gap for PhDs [A/C · T0-52].
- **Proof to show:** Your own method turned into a service with tests and CI; at least three code reviews via OSS PRs; an eval-statistics write-up.
- **Posting terms to mirror:** applied scientist, machine learning, statistics, experimentation, A/B testing, LLM, PyTorch.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-applied-scientist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-applied-scientist) · [Complete typed inventory](../03-skills-and-tech/inventories/applied-scientist.md)

<a id="resume-forward-deployed-engineer"></a>
#### #4 · Forward Deployed Engineer (AI) · variant A2
*Basis: RP2 T0-51 (n=28 FDE postings; excerpt-based lower bounds) + catalog tiers ([S]/[P]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), APIs & integrations, LLM APIs & tool calling, RAG, Customer scoping & demos |
| **Important** | Retrieval quality (hybrid, reranking, recall@k), OAuth/OIDC, RBAC, SSO, Agents & tool use, LLM evaluation (golden sets, calibrated judges, CI gates), Domain expertise, Stakeholder communication, Customer-facing communication |
| **Should** | TypeScript / JavaScript, AWS / Azure / GCP, Docker, SQL, Data pipelines & quality, Managed AI (Bedrock, Azure OpenAI, Vertex), Agent reliability (durable state, budgets, approvals), System design, Coding agents & AI-assisted engineering |
| **Optional** | Self-hosting open models, Product management, MCP (Model Context Protocol), Change management & adoption, AppSec & threat modelling, Pre-sales, Agent frameworks (LangGraph, Agents SDKs) |
| **Avoid** | A pre-sales-only story with no production code; vague "AI solutions" claims without customer outcomes |

- **Prerequisites:** One JD: 2–6 years and up to 50% travel [B · T0-01]. Only ~48% of the cluster is engineer-titled, so target those titles.
- **Proof to show:** A customer pilot case study with numbers; a demo on real data shown to at least two potential users; a deployment write-up that covers failure modes.
- **Posting terms to mirror:** forward deployed, FDE, customer-facing, deployment, integration, RAG, agents, travel.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-forward-deployed-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-forward-deployed-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/forward-deployed-engineer.md)

<a id="resume-research-engineer"></a>
#### #5 · Research Engineer / Member of Technical Staff · variant C1
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), PyTorch, PyTorch internals, ML fundamentals, Deep learning & transformers, Data structures & algorithms |
| **Important** | Distributed training (FSDP2, TP/PP, MoE), Post-training (SFT, preference, RL), Training-run debugging, LLM evaluation (golden sets, calibrated judges, CI gates), Profiling & roofline (Nsight), Data pipelines & quality |
| **Should** | Linux, C++, Continuous batching & KV cache, vLLM / SGLang / TensorRT-LLM, Reinforcement learning, Research methods & re-implementation |
| **Optional** | Pre-training at scale, CUDA / Triton / CUTLASS, TPU / Trainium / ROCm, Numerics validation, Kubernetes, Novel research & publications |
| **Avoid** | Listing frameworks without scale evidence; claiming research taste without artifacts |

- **Prerequisites:** Strong systems/ML engineering profile, fellowship (Anthropic Fellows: no PhD required) or OSS (vLLM, SGLang); only 1/18 JDs in T0-50 required a PhD [B/C · T0-50].
- **Proof to show:** Paper re-implementations with rigorous evals; a nano-vLLM-style engine benchmarked against vLLM; DDP/FSDP2 smoke tests; upstream OSS contributions; fellowship projects.
- **Posting terms to mirror:** Member of Technical Staff, research engineer, PyTorch, distributed training, post-training, RL / RLHF, evals.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-research-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-research-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/research-engineer.md)

<a id="resume-applied-ai-engineer"></a>
#### #6 · Applied AI Engineer · variant A2
*Basis: Catalog tiers ([S]/[P]); no JD measurement.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, RAG, Agents & tool use, Customer scoping & demos, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Important** | Guardrails, Prompt & context design, Technical writing, Retrieval quality (hybrid, reranking, recall@k), ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search |
| **Should** | APIs & integrations, Docker, Agent frameworks (LangGraph, Agents SDKs), Observability (OpenTelemetry traces, metrics), Cost & latency engineering, Customer-facing communication, Stakeholder communication, TypeScript / JavaScript |
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
| **Must** | Linux, Kubernetes, Networking, Terraform / IaC, Python (production), SRE (SLOs, on-call, incidents), Observability (OpenTelemetry traces, metrics), GPU fleet ops & scheduling |
| **Important** | Git & CI/CD, Docker, AWS / Azure / GCP, System design, NCCL / RDMA / InfiniBand, Checkpointing & storage throughput, Hardware-fault reliability, Capacity & GPU/API cost governance |
| **Should** | Go / Java, KServe / Ray Serve, vLLM / SGLang / TensorRT-LLM |
| **Optional** | Prefill/decode disaggregation, TPU / Trainium / ROCm, Profiling & roofline (Nsight) |
| **Avoid** | Listing Slurm or parallel storage systems (Lustre, Weka) you have not operated at cluster scale (Slurm appears in 15/35 T0-54 postings); generic DevOps bullets with no GPU scale |

- **Prerequisites:** Infrastructure depth; best feeders are SRE, DevOps and backend infrastructure engineers.
- **Proof to show:** A self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem.
- **Posting terms to mirror:** GPU, Kubernetes, infrastructure, distributed systems, NCCL, InfiniBand, SRE, Terraform (DevOps JDs: Kubernetes 69.4%, Terraform 59.1%, Linux 45.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-infrastructure-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-infrastructure-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-infrastructure-engineer.md)

<a id="resume-research-scientist"></a>
#### #8 · Research Scientist (LLM research) · variant C2
*Basis: JD-measured (all-field research-scientist postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | ML fundamentals, Python (production), PyTorch, Deep learning & transformers, Research methods & re-implementation, Linear algebra, Novel research & publications |
| **Important** | Data structures & algorithms, Clear writing & presenting, Reinforcement learning, Post-training (SFT, preference, RL), LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Should** | C++, Distributed training (FSDP2, TP/PP, MoE), Eval statistics (CIs, power, pass^k) |
| **Optional** | LLM APIs & tool calling, Interpretability, Alignment methods, Pre-training at scale, Computer vision & robot perception, Technical leadership |
| **Avoid** | Unpublished claims of novelty; burying the publication list |

- **Prerequisites:** PhD plus publications; frontier offers are "not plannable" [D · T0-06].
- **Proof to show:** Papers, open research code, talks.
- **Posting terms to mirror:** Python (42.3%), communication (41.3%), machine learning (39.2%), PyTorch (25.4%), LLM (24.4%), deep learning (18.6%), C++ (17.4%), reinforcement learning (17.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-research-scientist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-research-scientist) · [Complete typed inventory](../03-skills-and-tech/inventories/research-scientist.md)

<a id="resume-ml-platform-engineer"></a>
#### #9 · ML Platform / MLOps (LLMOps) Engineer · variant D2
*Basis: Catalog tiers + DevOps feeder JD shares.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Kubernetes, Terraform / IaC, Git & CI/CD, Docker, Python (production), AWS / Azure / GCP, Observability (OpenTelemetry traces, metrics), MLOps lifecycle (model & prompt CI/CD) |
| **Important** | Linux, KServe / Ray Serve, LLM gateways, OAuth/OIDC, RBAC, SSO, Model supply chain & CVEs, SRE (SLOs, on-call, incidents), vLLM / SGLang / TensorRT-LLM |
| **Should** | MCP (Model Context Protocol), Capacity & GPU/API cost governance, Go / Java |
| **Optional** | Engine internals & multi-LoRA, Prefill/decode disaggregation, GPU fleet ops & scheduling |
| **Avoid** | Generic DevOps bullets with no model-serving scope |

- **Prerequisites:** Backend, DevOps or SRE background; India GCCs use the MLOps Engineer title (Taggd, C).
- **Proof to show:** A self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, dynamic LoRA routing and Grafana dashboards.
- **Posting terms to mirror:** MLOps, LLMOps, Kubernetes (69.4% of DevOps postings), Terraform (59.1%), CI/CD (81.2%), model serving, KServe, monitoring.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ml-platform-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ml-platform-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ml-platform-engineer.md)

<a id="resume-ai-security-engineer"></a>
#### #10 · AI Security Engineer / AI Red Teamer · variant D3
*Basis: Security Engineer feeder JD shares + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AppSec & threat modelling, Python (production), OAuth/OIDC, RBAC, SSO, Incident response & SIEM, LLM security (prompt injection, OWASP), Prompt-injection attack & defence, Red-teaming |
| **Important** | Agent abuse & MCP authorisation, Model supply chain & CVEs, Containment (DLP, sandboxing, egress), AWS / Azure / GCP |
| **Should** | MCP (Model Context Protocol), Observability (OpenTelemetry traces, metrics), Docker, Kubernetes |
| **Optional** | GRC & risk assessment, Safety & capability evals |
| **Avoid** | Classifier-only defences presented as complete (adaptive attacks beat 12 published defences) |

- **Prerequisites:** Application-security background; Anthropic AI Security Fellow requires US/UK/Canada work authorisation [A · T0-12].
- **Proof to show:** A red-team suite in CI against a working agent, with attack-success rates before and after mitigation; an MCP security audit.
- **Posting terms to mirror:** application security (26.5% of Security Engineer postings), cybersecurity (42.3%), Python (45.7%), IAM (21.6%), incident response (32.4%), AI security, prompt injection, red team, OWASP.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-security-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-security-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-security-engineer.md)

<a id="resume-inference-engineer"></a>
#### #11 · Inference / LLM Serving Engineer · variant D1
*Basis: Catalog tiers ([S]/[A]); named JDs at Anthropic, NVIDIA, Together AI, Baseten, Inferact.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), C++, GPU fundamentals (HBM, prefill vs decode), PyTorch internals, System design, vLLM / SGLang / TensorRT-LLM, Kubernetes, Continuous batching & KV cache |
| **Important** | Speculative decoding, Quantisation (FP8/FP4, AWQ, GPTQ), TP/PP & MoE serving, Load testing & latency SLOs, Profiling & roofline (Nsight), Cost & latency engineering |
| **Should** | Linux, Model supply chain & CVEs, Observability (OpenTelemetry traces, metrics), Constrained decoding, Token & unit economics |
| **Optional** | Prefill/decode disaggregation, CUDA / Triton / CUTLASS, NCCL / RDMA / InfiniBand, Engine internals & multi-LoRA, Numerics validation, Tile DSLs (Helion, CuteDSL) |
| **Avoid** | TGI (archived 2026-03-21); the removed trtllm-build static engine path; single-process load generators |

- **Prerequisites:** Backend → Staff-level inference takes ~10–14 months with infrastructure depth [D · T2-01].
- **Proof to show:** A single-GPU serving study (BF16 vs FP8/4-bit, prefix caching, chunked prefill, speculative decoding) with a roofline and $/M tokens at the SLO; a custom Triton kernel tested against a reference; an upstream PR to vLLM, SGLang or FlashInfer.
- **Posting terms to mirror:** inference, vLLM, SGLang, TensorRT-LLM, KV cache, latency, throughput, quantization, CUDA.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-inference-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-inference-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/inference-engineer.md)

<a id="resume-ai-solutions-architect"></a>
#### #12 · AI / GenAI Solutions Architect · variant A2
*Basis: JD-measured (all Solutions Architect postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AWS / Azure / GCP, GenAI reference architectures, Stakeholder communication, Pre-sales |
| **Important** | Leadership & mentoring, GRC & risk assessment, Python (production), Managed AI (Bedrock, Azure OpenAI, Vertex), Cost & latency engineering, Token & unit economics, OAuth/OIDC, RBAC, SSO, RAG, Agents & tool use |
| **Should** | Terraform / IaC, Networking, Kubernetes, Customer scoping & demos, Customer-facing communication, LLM evaluation (golden sets, calibrated judges, CI gates), Observability (OpenTelemetry traces, metrics) |
| **Optional** | LLM gateways, Self-hosting open models, AI strategy & portfolio, Agent frameworks (LangGraph, Agents SDKs), MCP (Model Context Protocol), Domain expertise |
| **Avoid** | Certification lists in place of delivered architectures |

- **Prerequisites:** Usually 5+ (10+ at frontier labs) years in customer-facing engineering or cloud architecture, though entry-level hyperscaler CSA programmes exist; certs matter mainly in partner/SI channels [B/C · T0-11, T0-62].
- **Proof to show:** A reference architecture with a cost/latency model, an eval-backed live demo and a customer-scenario discovery walkthrough (IaC optional outside cloud-delivery shops).
- **Posting terms to mirror:** solutions architect, AWS (53.6%), Azure (29.5%), GCP (22.6%), leadership (43.0%), communication (42.9%), mentoring (35.1%), compliance (25.3%), Python (23.6%), AI (23.2%), generative AI (17.1%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-solutions-architect) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-solutions-architect) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-solutions-architect.md)

<a id="resume-ai-product-manager"></a>
#### #13 · AI Product Manager · variant E1
*Basis: JD-measured (all PM postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Product management, Stakeholder communication, AI literacy (tokens, RAG vs fine-tune, cost), Rubrics & inter-rater agreement |
| **Important** | Leadership & mentoring, GRC & risk assessment, Metrics for non-deterministic systems, Token & unit economics, Pilots & adoption measurement, Product sense |
| **Should** | Python/SQL (notebook level), Agents & tool use, Human-in-the-loop design, Domain expertise, Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Optional** | Risk & compliance docs (Annex IV, model cards), MCP (Model Context Protocol), AI strategy & portfolio |
| **Avoid** | "AI-powered" buzzwords without a shipped model feature or metrics |

- **Prerequisites:** 4+ years as a PM plus at least one shipped model-powered feature [D · T0-06]; T2-01 asks for 5+ years in product/ops plus notebook-level Python.
- **Proof to show:** A shipped model/agent prototype with PRD, eval rubric (50+ labelled cases) and failure-mode ranking by business impact.
- **Posting terms to mirror:** product management (92.6%), communication (53.7%), leadership (40.1%), compliance (26.1%), agile (22.7%), roadmapping (18.4%), AI (15.4%), stakeholder management (14.2%), agentic AI (13.6%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-product-manager) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-product-manager) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-product-manager.md)

<a id="resume-agentic-ai-engineer"></a>
#### #14 · Agentic AI Engineer · variant A1
*Basis: T0-16 title shares (LangGraph 35.8%, MCP 13.8%) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, Agents & tool use, Prompt & context design |
| **Important** | Agent reliability (durable state, budgets, approvals), MCP (Model Context Protocol), Containment (DLP, sandboxing, egress), LLM evaluation (golden sets, calibrated judges, CI gates), LLM security (prompt injection, OWASP), Agent frameworks (LangGraph, Agents SDKs), Human-in-the-loop design |
| **Should** | RAG, Observability (OpenTelemetry traces, metrics), AWS / Azure / GCP, TypeScript / JavaScript, Git & CI/CD, Kubernetes, SQL, Docker, Product sense, Token & unit economics, Coding agents & AI-assisted engineering |
| **Optional** | Constrained decoding, Retrieval quality (hybrid, reranking, recall@k), Domain expertise |
| **Avoid** | AutoGen (dormant); CrewAI as a headline (absent from tier-1 lab postings); demo agents with no failure handling |

- **Prerequisites:** Usually an AI Engineer title in practice; standalone 'agentic' titles are a niche (Skilark: 107 of 28,771 AI listings = 0.37%, Feb 2026 [C · T0-57 L118]; IT Jobs Watch ~7 UK permanent in 6 mo).
- **Proof to show:** An agent with human approval, sandboxed tools, deterministic trace replay and failure-injection tests (timeouts, malformed arguments, prompt injection), reporting cost per task.
- **Posting terms to mirror:** agentic AI, agents, multi-agent, LangGraph (35.8% of Agentic AI Engineer postings), LangChain, MCP, tool calling.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-agentic-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-agentic-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/agentic-ai-engineer.md)

<a id="resume-ai-evaluation-engineer"></a>
#### #15 · AI Evaluation Engineer · variant A1
*Basis: Catalog tiers; evals in 19.0% of S09 postings (68.2% of companies).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM evaluation (golden sets, calibrated judges, CI gates), Testing (pytest), LLM APIs & tool calling |
| **Important** | Eval statistics (CIs, power, pass^k), Error analysis, Experiment design & A/B testing, Retrieval quality (hybrid, reranking, recall@k), Benchmark construction, Git & CI/CD, Human evaluation programmes, Rubrics & inter-rater agreement |
| **Should** | Observability (OpenTelemetry traces, metrics), SQL, RAG, Agents & tool use, Metrics for non-deterministic systems |
| **Optional** | Safety & capability evals, Red-teaming, Annotation workflows, Domain expertise |
| **Avoid** | Eval-platform brand lock-in (7 acquisitions/closures in 13 months; OpenAI hosted Evals shutdown 2026-11-30); storing master API keys in SaaS eval platforms; 'accuracy' claims without CIs |

- **Prerequisites:** Lead with 3+ years software/backend or data-science engineering (0/22 entry-level and 0/22 PhD required in T0-60); PhDs add measurement rigour [C · T0-60].
- **Proof to show:** An eval harness with a kappa-calibrated judge validated on 100+ human labels, plus position and verbosity bias tests; a CI regression threshold and a cost–quality frontier chart.
- **Posting terms to mirror:** LLM evaluation, evals, benchmarking, LLM-as-a-judge, golden dataset, A/B testing, pytest.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-evaluation-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-evaluation-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-evaluation-engineer.md)

<a id="resume-gpu-kernel-engineer"></a>
#### #16 · GPU Kernel / ML Compiler Engineer · variant D1
*Basis: Catalog tiers ([S]); kernels in 6.6% of S09 postings.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | C++, CUDA / Triton / CUTLASS, GPU fundamentals (HBM, prefill vs decode), Profiling & roofline (Nsight) |
| **Important** | Attention, GEMM & quantised kernels, GPU memory performance, Numerics validation, ML compilers (XLA, TorchInductor), Upstream open-source contributions |
| **Should** | Linear algebra, Quantisation (FP8/FP4, AWQ, GPTQ), Python (production), PyTorch internals |
| **Optional** | Tile DSLs (Helion, CuteDSL), TPU / Trainium / ROCm, NCCL / RDMA / InfiniBand |
| **Avoid** | Raw-kernel claims without benchmarks and correctness tests |

- **Prerequisites:** Systems / C++ / CUDA background or a PhD.
- **Proof to show:** GPU MODE leaderboard submissions; kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware with correctness tests.
- **Posting terms to mirror:** CUDA, Triton, CUTLASS, kernels, GPU, compiler, XLA, performance.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-gpu-kernel-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-gpu-kernel-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/gpu-kernel-engineer.md)

<a id="resume-physical-ai-engineer"></a>
#### #17 · Physical AI / Robotics AI Engineer · variant B3
*Basis: RP2 T0-64 (n=48 Physical AI postings, 12 full-text; lower bounds) + platform cross-check (n=4,875, Grade B) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Robotics fundamentals, C++, Python (production), Simulation & sim-to-real, ROS, Robot learning & VLA models, PyTorch, Real-robot deployment & hardware bring-up |
| **Important** | Edge inference, Teleoperation data pipelines, Safety cases, Imitation learning, Computer vision & robot perception, Reinforcement learning |
| **Should** | Deep learning & transformers, Quantisation (FP8/FP4, AWQ, GPTQ), Linux, Docker, Data pipelines & quality |
| **Optional** | CUDA / Triton / CUTLASS |
| **Avoid** | Simulation-only results presented as real-world performance |

- **Prerequisites:** Robotics or controls background with ML.
- **Proof to show:** A sim-to-real or manipulation project with measured success rates and failure analysis.
- **Posting terms to mirror:** robotics, VLA, imitation learning, reinforcement learning, sim-to-real, ROS, perception.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-physical-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-physical-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/physical-ai-engineer.md)

<a id="resume-ai-governance-lead"></a>
#### #18 · AI Governance Programme Lead / Manager · variant E2
*Basis: Axial shares (C) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | GRC & risk assessment, EU AI Act / NIST AI RMF / ISO 42001, Stakeholder communication, AI inventory & risk register |
| **Important** | Sector rules (SR 26-2, LL144, DPDP), Content provenance (EU AI Act Art. 50), Privacy law & DPO duties, Observability (OpenTelemetry traces, metrics), Python/SQL (notebook level), AI operating model & governance boards |
| **Should** | Technical writing, Risk & compliance docs (Annex IV, model cards), AI literacy (tokens, RAG vs fine-tune, cost), Leadership & mentoring |
| **Optional** | Audit methodology |
| **Avoid** | Listing AIGP as your main credential (domain certifications come first) |

- **Prerequisites:** About 5 years all-level (median 10 years stated minimum for manager/lead/director postings in T0-61) in GRC, privacy, audit or security; domain certs first, AIGP optional [B/C · T0-15, T0-61].
- **Proof to show:** An AI inventory, risk register and governance playbook mapped to the EU AI Act, NIST AI RMF and ISO 42001.
- **Posting terms to mirror:** AI governance, EU AI Act, NIST AI RMF, ISO 42001, risk management, compliance, privacy; Axial: observability/monitoring 42.3%, Python 27.1%.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-governance-lead) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-governance-lead) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-governance-lead.md)

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

- **Prerequisites:** Research track record or fellowship (0/23 visible T0-60 postings required a PhD); Anthropic Fellows requires US, UK or Canada work authorisation with no visa sponsorship [A/C · T0-60].
- **Proof to show:** Fellowship projects; published safety research; open eval contributions.
- **Posting terms to mirror:** AI safety, alignment, interpretability, evaluations, red teaming.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-safety-researcher) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-safety-researcher) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-safety-researcher.md)

<a id="resume-ai-product-engineer"></a>
#### #20 · AI Product Engineer (AI Frontend) · variant A1
*Basis: JD-measured (Full-Stack Engineer postings) + catalog tiers.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | React, TypeScript / JavaScript, APIs & integrations, LLM APIs & tool calling, Product sense |
| **Important** | Python (production), AWS / Azure / GCP, Git & CI/CD, Streaming & agent UX, Agent-UX telemetry, LLM evaluation (golden sets, calibrated judges, CI gates), Human-in-the-loop design |
| **Should** | RAG, Agents & tool use, Docker |
| **Optional** | On-device / WebGPU inference, MCP (Model Context Protocol) |
| **Avoid** | Pure UI work with no model-facing evidence |

- **Prerequisites:** Median 2 years stated experience (n=6 in T0-62) for AI Product Engineer, rising to 6+ years for Staff AI Frontend; also search 'full-stack AI engineer' [C · T0-62].
- **Proof to show:** A deployed streaming chat or agent UI with cancel/retry/error states, accessibility and clean frontend–API–LLM integration (evals are a differentiator; on-device WebGPU optional).
- **Posting terms to mirror:** React (69.4%), TypeScript (52.7%), Python (41.8%), AWS (41.3%), CI/CD (37.8%), Node.js (32.3%), REST API (27.6%), streaming, LLM.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-product-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-product-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-product-engineer.md)

<a id="resume-ai-risk-assurance-specialist"></a>
#### #21 · AI Risk, Audit & Compliance Specialist · variant E2
*Basis: Catalog tiers ([S]/[B]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Audit methodology, GRC & risk assessment, Model validation, Privacy law & DPO duties |
| **Important** | EU AI Act / NIST AI RMF / ISO 42001, Sector rules (SR 26-2, LL144, DPDP), Fairness & explainability tools, Risk & compliance docs (Annex IV, model cards), Technical writing |
| **Should** | Stakeholder communication, Python/SQL (notebook level), AI inventory & risk register |
| **Optional** | Content provenance (EU AI Act Art. 50) |
| **Avoid** | Claiming GenAI risk ownership as settled (SR 26-2 excludes generative and agentic AI) |

- **Prerequisites:** 4–10+ years in model risk management (MRM), IT audit, compliance or technology risk; CISA/CIA/CPA is required only for the ISACA AAIA credential, not as a universal job gate [B · T0-61].
- **Proof to show:** A model-validation or bias-audit report on a public model, using a documented methodology.
- **Posting terms to mirror:** audit, model risk, AI risk, compliance, ISO 42001, bias audit, privacy.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-risk-assurance-specialist) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-risk-assurance-specialist) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-risk-assurance-specialist.md)

<a id="resume-responsible-ai-engineer"></a>
#### #22 · Responsible AI / AI Governance Engineer · variant E2
*Basis: Catalog tiers ([S]); 13 JDs in T0-15.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), ML fundamentals, Risk & compliance docs (Annex IV, model cards), LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Important** | Guardrails, EU AI Act / NIST AI RMF / ISO 42001, Fairness & explainability tools, Observability (OpenTelemetry traces, metrics) |
| **Should** | MLOps lifecycle (model & prompt CI/CD), Managed AI (Bedrock, Azure OpenAI, Vertex), Red-teaming, Prompt-injection attack & defence, AI inventory & risk register, Technical writing |
| **Optional** | Content provenance (EU AI Act Art. 50), Domain expertise |
| **Avoid** | Pre-1.0 tools (Guardrails AI, Giskard v3, c2pa-python) presented as production-hardened |

- **Prerequisites:** MLOps or security engineering background in a regulated firm.
- **Proof to show:** A compliance packet mapped to NIST AI 600-1 and OWASP GenAI LLM Top 10 2026, with runtime guardrails, subgroup evals and a calibrated judge on 100-200 human labels per failure mode (T0-20 L63, L196).
- **Posting terms to mirror:** responsible AI, AI governance, guardrails, fairness, explainability, EU AI Act, model cards.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-responsible-ai-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-responsible-ai-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/responsible-ai-engineer.md)

<a id="resume-ai-enablement-engineer"></a>
#### #23 · AI Enablement Engineer · variant A1
*Basis: Catalog tiers; MCP named in 30.2% of these postings (T0-16).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Internal tooling & DevEx, Change management & adoption, Teaching & workshop delivery |
| **Important** | Python (production), LLM APIs & tool calling, MCP (Model Context Protocol), Agents & tool use, Guardrails, Coding agents & AI-assisted engineering, Pilots & adoption measurement, GRC & risk assessment |
| **Should** | OAuth/OIDC, RBAC, SSO, RAG, Observability (OpenTelemetry traces, metrics), AWS / Azure / GCP, TypeScript / JavaScript, Token & unit economics, Metrics for non-deterministic systems, Technical writing, Stakeholder communication, AI inventory & risk register, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Optional** | LLM gateways, Kubernetes, Docker, Agent frameworks (LangGraph, Agents SDKs), Domain expertise |
| **Avoid** | Adoption claims without usage or time-saved numbers |

- **Prerequisites:** Splits into builder/platform (DevEx/backend) and ops/adoption (internal ops, L&D, RevOps) lanes; 26.7%–33.3% require Python [B/C · T0-62].
- **Proof to show:** An internal pilot with 5–10 colleagues measuring adoption and time saved, with a runbook and a risk register.
- **Posting terms to mirror:** AI enablement, MCP, internal tools, copilot, developer productivity, adoption.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-enablement-engineer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-ai-enablement-engineer) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-enablement-engineer.md)

<a id="resume-domain-evaluation-specialist"></a>
#### #24 · Domain Evaluation Specialist / AI Trainer · variant E3
*Basis: Catalog tiers ([C]/[S]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Domain expertise, Clear writing & presenting, Rubrics & inter-rater agreement, Human evaluation programmes |
| **Important** | Error analysis, Annotation workflows, Benchmark construction |
| **Should** | AI literacy (tokens, RAG vs fine-tune, cost), Red-teaming, Eval statistics (CIs, power, pass^k), Technical writing, LLM evaluation (golden sets, calibrated judges, CI gates) |
| **Optional** | Python/SQL (notebook level), Product sense, GRC & risk assessment |
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
| **Must** | Leadership & mentoring, Stakeholder communication, Technical leadership |
| **Important** | System design, LLM evaluation (golden sets, calibrated judges, CI gates), Observability (OpenTelemetry traces, metrics), AI strategy & portfolio |
| **Should** | Capacity & GPU/API cost governance, Agents & tool use, Token & unit economics, AI literacy (tokens, RAG vs fine-tune, cost), MLOps lifecycle (model & prompt CI/CD), SRE (SLOs, on-call, incidents), Python (production) |
| **Optional** | GRC & risk assessment, Guardrails, EU AI Act / NIST AI RMF / ISO 42001, Agent frameworks (LangGraph, Agents SDKs), AWS / Azure / GCP, Domain expertise |
| **Avoid** | Team-size bragging without delivery or quality metrics |

- **Prerequisites:** 8+ years engineering plus 2-6 years managing (Anthropic accepts technical leadership for the 2+ years); backend, SRE and devtools managers can cross; PhD not required [A/M · T0-65 L202].
- **Proof to show:** Delivery record: AI systems shipped, eval/observability practices adopted across teams, cost governance results.
- **Posting terms to mirror:** leadership (72.7%), communication (51.4%), mentoring (47.1%), compliance (30.9%), system design (25.3%), observability (18.0%), agentic AI (14.8%).
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-ai-engineering-manager) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/ai-engineering-manager.md)

<a id="resume-vp-head-of-ai"></a>
#### L2 · VP / Head of AI · variant L2
*Basis: RP2 T0-65 (n=11 text-visible Head/VP of AI postings, lower bounds) + catalog tiers ([S]/[P]).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AI strategy & portfolio, Leadership & mentoring, Stakeholder communication |
| **Important** | AI operating model & governance boards, EU AI Act / NIST AI RMF / ISO 42001 |
| **Should** | GRC & risk assessment, Product management, AI literacy (tokens, RAG vs fine-tune, cost), LLM evaluation (golden sets, calibrated judges, CI gates), Technical leadership, Change management & adoption, AI inventory & risk register |
| **Optional** | Token & unit economics, Capacity & GPU/API cost governance, Sector rules (SR 26-2, LL144, DPDP), AWS / Azure / GCP |
| **Avoid** | Technology lists in place of business outcomes |

- **Prerequisites:** 5-15+ years (median 10, n=7 in T0-65; 12-18+ in India); player-coach seats accept senior AI engineer or AI PM step-ups while enterprise seats ask for prior EM/Director delivery [B · T0-65 L250, L273, L279].
- **Proof to show:** Portfolio outcomes: revenue or cost impact, governance boards stood up, vendor decisions.
- **Posting terms to mirror:** AI strategy, roadmap, governance, operating model, budget, build vs buy.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-vp-head-of-ai) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/vp-head-of-ai.md)

<a id="resume-chief-ai-officer"></a>
#### L3 · Chief AI Officer · variant L3
*Basis: RP2 T0-65 (n=7 text-visible CAIO postings, including SBI GM & CAIO and Axial full reads; lower bounds) + federal mandate OMB M-25-21 (A).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AI strategy & portfolio, GRC & risk assessment, Leadership & mentoring, Stakeholder communication |
| **Important** | AI operating model & governance boards, Change management & adoption, Domain expertise |
| **Should** | EU AI Act / NIST AI RMF / ISO 42001, LLM evaluation (golden sets, calibrated judges, CI gates), Privacy law & DPO duties |
| **Optional** | AWS / Azure / GCP |
| **Avoid** | Treating vendor-awarded 'Certified CAIO' titles as executive credentials (no independent assessment, T0-68 G4); applying to junior 'Director, CAIO' posts expecting C-suite scope |

- **Prerequisites:** 12-15+ years total experience with 3-5+ years in director/VP/C-level AI or data leadership (Axial/SBI, T0-65 L323); US federal agency CAIOs are mandated by OMB M-25-21 (2025-04-03, Grade A, T0-65 L292) — private-sector CAIOs are voluntary and often dual-hatted.
- **Proof to show:** Enterprise AI delivery at scale (e.g. 100,000+ users in SBI), governance forums and independent model-validation oversight stood up, board-level vendor/build-vs-buy decisions and regulatory alignment (RBI/DPDP, GDPR, HIPAA, EU AI Act).
- **Posting terms to mirror:** AI strategy, AI governance, responsible AI, executive leadership, model validation, regulatory compliance, board reporting, build vs buy, enterprise transformation.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-chief-ai-officer) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/chief-ai-officer.md)

<a id="resume-independent-ai-consultant"></a>
#### L4 · Independent AI Consultant / Contract Builder · variant L4
*Basis: RP2 T0-66: UK IT Jobs Watch GenAI contract benchmark (n=1,466, Grade B) + global direct sample (n=17, lower bounds); delivery-heavy builder role.*

| Tier | Skills, in priority order |
|---|---|
| **Must** | Python (production), LLM APIs & tool calling, Agents & tool use, AWS / Azure / GCP, RAG |
| **Important** | ML fundamentals, Stakeholder communication, Git & CI/CD, LLM evaluation (golden sets, calibrated judges, CI gates), APIs & integrations, Domain expertise, Customer-facing communication, MCP (Model Context Protocol) |
| **Should** | Docker, SQL, MLOps lifecycle (model & prompt CI/CD), AI strategy & portfolio, GRC & risk assessment, Data pipelines & quality, Leadership & mentoring, Privacy law & DPO duties |
| **Optional** | PyTorch |
| **Avoid** | Buying vendor-awarded 'Certified AI Consultant' certificates (avoid per T0-68 G4); competing solely on generic marketplace race-to-the-bottom hourly rates without a vertical case study |

- **Prerequisites:** Proven production shipping record (typically 5+ years engineering/ML) plus client acquisition channel (warm network, specialist staffing or referral; avoid relying on unverified 92% referral claims — independent surveys show 53-75%, T0-66).
- **Proof to show:** Two to three anonymised client case studies with before/after latency, cost or workflow-time metrics, clean handover docs, and one public category-level evaluation or agent blueprint.
- **Posting terms to mirror:** Python, LLM, RAG, AI agents, Azure, AWS, GCP, LangGraph, MCP, MLOps, CI/CD, evaluations, stakeholder management, production delivery.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-independent-ai-consultant) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/independent-ai-consultant.md)

<a id="resume-fractional-ai-leader"></a>
#### L5 · Fractional AI Leader · variant L5
*Basis: RP2 T0-66 (n=13 fractional AI leadership postings/briefs; lower bounds; 4 Axial template pages noted).*

| Tier | Skills, in priority order |
|---|---|
| **Must** | AI strategy & portfolio, GRC & risk assessment, Change management & adoption, Leadership & mentoring, Stakeholder communication |
| **Important** | Agents & tool use, Domain expertise, Teaching & workshop delivery, AI operating model & governance boards |
| **Should** | MLOps lifecycle (model & prompt CI/CD), LLM evaluation (golden sets, calibrated judges, CI gates), AWS / Azure / GCP, Privacy law & DPO duties |
| **Optional** | Python (production) |
| **Avoid** | Vendor-awarded 'Fractional CAIO' certificates (avoid per T0-68 G4; 0 independent employer standing); over-promising full-time build output on a 1-day/week retainer |

- **Prerequisites:** Prior Head of AI, VP, CTO or C-suite leadership seat (explicit in 9/13 T0-66 postings, L588); client pipeline via executive network or PE/VC operating-partner referrals (53-75% referral share in independent surveys vs 92% Go Fractional vendor claim, T0-66).
- **Proof to show:** 2-3 anonymised executive case studies showing AI strategy -> shipped pilot -> measurable ROI, governance policy templates deployed, and permanent hires or vendor contracts structured.
- **Posting terms to mirror:** Fractional CAIO, Fractional Head of AI, AI strategy, AI governance, ROI, executive communication, change management, vendor selection, PE/SMB AI transformation.
- **Links:** [Role profile](../02-roles/role-catalog.md#profile-fractional-ai-leader) · [Narrative skill map](../03-skills-and-tech/role-skill-maps.md#skills-leadership) · [Complete typed inventory](../03-skills-and-tech/inventories/fractional-ai-leader.md)
<!-- END GENERATED -->

---
*Posting shares are JobsPipe measurements (count date 2026-09-10, retrieved 2026-11-02, unchanged 2026-11-14 [B · T0-69 KF7]) supplemented by RP2 role dossiers (`T0-48` to `T0-66`, verified 2026-11-19). Practice-curated items are Grade D. Next scheduled review by 2027-02-17.*
