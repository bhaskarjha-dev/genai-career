---
id: skills.role-maps
title: "Role Skill Maps"
content_type: reference
stage: 3
status: published
last_verified: 2026-11-19
review_by: 2027-02-17
summary: "Narrative skill map for every role: practice notes from the evidence, tools in use with their November 2026 status, proof of work, interview track, typical gaps and entry routes. Each role's skills and tiers are in its generated inventory."
sources: [T0-03, T0-06, T0-13, T0-14, T0-15, T0-16, T0-20, T0-34, T0-46, T0-48, T0-49, T0-50, T0-51, T0-52, T0-53, T0-54, T0-55, T0-56, T0-57, T0-58, T0-59, T0-60, T0-61, T0-62, T0-63, T0-64, T0-65, T0-66, T0-68, T0-69, T1-03]
---
# Role Skill Maps
## What the Evidence Says About Each Canonical GenAI Role: Practice Notes, Tools, Proof of Work, Interviews and Gaps

> **Updated:** 2026-11-19 · **Temporal anchor:** November 2026
> **Role universe:** the 29 canonical roles in the [master catalog](../02-roles/role-catalog.md), in the order of the [ranked catalog](../02-roles/role-rankings.md)
> **Skills and tiers:** every role's skills, each with its tier (Must, Important, Should, Optional, Avoid) and evidence tag, are generated from [data/skills_ontology.json](../../data/skills_ontology.json) into the role's inventory, indexed in [role-skill-inventories.md](role-skill-inventories.md); [skills-vocabulary.md](skills-vocabulary.md) types every skill. This page keeps the narrative the inventories cannot show: practice notes, tools in use, proof of work, interview tracks, typical gaps and entry routes.
> **No D-004 tiers here.** This page no longer sorts skills into table-stakes, differentiating and frontier tiers. Erratum U20 finds the D-004 thresholds behind those tiers unsupported (posted pay tracks seniority and employer tier more than skill tier), and the labels contradicted the ontology's tiers, which are the source of truth for role skill tiers ([AGENTS.md §2](../../AGENTS.md#2-sources-of-truth)).
> **Evidence standard:** EGP-1.0. A skill list is guidance, not a measurement. Measured prevalence carries a grade; everything else is tagged by where it came from (§0).

---

## 0. How to Read This File

| Tag | Meaning | Grade |
|---|---|---|
| **[S09 x%]** | Share of the 3,647-posting S09 corpus (198 companies, 2026-08-05; skews senior/infra) that names the skill ([T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) §6.3) | B |
| **[S]** | Named in research sessions or in real job descriptions cited there | B/C |
| **[P]** | Practice-curated: standard for the role, but **not** evidenced in the corpus. Check it against 10–20 live JDs before investing heavily | D |

Other claims carry an EGP-1.0 grade and their source, for example [A · T0-14]. The JobsPipe posting shares (count date 2026-09-10, retrieved 2026-11-02, unchanged 2026-11-14 [B · T0-69 KF7]) that the inventories tag [JD x%] are in [posting evidence](role-skill-inventories.md#posting-evidence).

**How to use it:**
1. Pick a role from the [ranked catalog](../02-roles/role-rankings.md) and open its map below.
2. Open the role's inventory for its skills and tiers: close Must gaps first, then build two or three Important skills into proof of work ([role skill inventories §0](role-skill-inventories.md#0-how-to-use-it)).
3. Use the map for what the inventory cannot show: practice notes, the tools in use, the proof of work, the interview track and the typical gaps.

Four facts from the evidence frame every map below:
- **Evaluation is the most consistent separator, but it is "common, not universal":** evals appear in 19.0% of S09 postings and at 68.2% of companies [B · T0-03 §6.3], and in 59.7% of AI-first roles [B · T0-13.F3]. Raw judge agreement overstates accuracy by **33–41 points** against chance-corrected Cohen's κ across 21 LLM judges (`arXiv:2606.19544`) [A/B · T0-03 L98].
- **Hiring signals reward practice, not brands.** Named eval frameworks barely register in postings, seven eval and observability vendors were acquired or sunset between May 2025 and May 2026 (W&B Weave, Humanloop, Langfuse, Helicone, Promptfoo, Traceloop, Galileo) [B · T0-69 L51, L370–L376], and model choice turns over fast (Vercel AI Gateway median model replacement **61 days** / ~6-week half-life) [B · T0-69 L221].
- **Tools churn fast.** Between late 2025 and November 2026: Hugging Face TGI entered maintenance/archive, OpenAI retired the Assistants API (2026-08-26), `torchtune` became dormant, AutoGen stalled (410 days without a PyPI release), Vercel shipped AI SDK 7 (2026-06-25) and TensorRT-LLM removed `trtllm-build` (PyTorch backend only). Conversely, **RAGAS is not dormant** — `vibrantlabsai/ragas` shipped v0.4.4rc1 on 2026-11-13 [B · T0-69 L49–L50, L362–L377] (see the [watch list](skills-vocabulary.md#5-watch-list-tools-with-a-notable-status)). Learn concepts first and tools second.
- **Operational tripwires to monitor on production stacks:** serving-engine CVEs (vLLM/SGLang), eval/tracing vendor lock-in (export OTLP), silent inference-provider routing bugs (e.g. Anthropic's September 2025 three-bug postmortem: context-routing truncation affecting up to 16% of Sonnet 4 requests, TPU token-corruption miscompilation and XLA:TPU approximate top-k errors [A, COI · T0-03 L104]) and runaway token cost multipliers [A/B · T0-03 §4.5 L161–L168].

---

## 1. The Universal GenAI Skill Spine

### 1.1 Twelve-skill readiness rubric (T0-06, target levels for an AI-engineer role)

The scale runs 0–3 (T0-06 D9): 0 = none, 1 = tutorial-level awareness, 2 = built and shipped something small with feedback, 3 = owns it in production or could teach it.

| # | Skill | Target | # | Skill | Target |
|---|---|:---:|---|---|:---:|
| S1 | Production Python / TypeScript | 3 | S7 | Production ops (CI/CD, deploy, observability, cost, security) | 2–3 |
| S2 | LLM API fluency (structured output, tool calling, streaming, token budgets) | 3 | S8 | System design for LLM applications | 2 |
| S3 | Retrieval and context engineering | 2–3 | S9 | Frontend and streaming UX | 1 (3 for frontend targets) |
| S4 | Evaluation design | 3 | S10 | Model and inference literacy | 1–2 |
| S5 | Error analysis and data literacy | 2–3 | S11 | Domain judgement and rubric writing | 2 |
| S6 | Agents and tool-use reliability | 2 | S12 | Product sense and stakeholder communication | 2 |

**"GenAI role-ready" means** you can build, evaluate, deploy and operate an LLM-backed system on your own, with a measured eval suite, traces, and a cost and latency budget [T0-06].

**Three fast self-tests (T0-06):**
1. Q&A over 50 documents, reporting recall@5 and faithfulness.
2. Explain the full request path of a system you built.
3. Design an eval: 30 cases, a rubric, and judge validation.

### 1.2 Behavioural competencies every GenAI loop probes (T1-03, T0-46)

The four competencies (C1–C4), the STAR-AI story bank and how hiring decisions differ across employers — Amazon's Bar Raiser veto and Anthropic's values screen versus Google Hiring Committee variance and downlevelling (not a simple single-interviewer behavioural veto) — are in [behavioural calibration](../08-interviewing/behavioral-calibration.md) [B/C · T1-03.F4, F5; T0-46].

### 1.3 Proof of work by tier (T2-01 KF9, T0-13)

The portfolio bar by target level, the verifiability ladder (V0–V3), the fifteen artefacts (PA-01 to PA-15), the anti-portfolio and the rubric weights are in [proof-of-work standards](../05-portfolio/proof-of-work-standards.md#the-verifiability-ladder-and-the-level-model).

---

## 2. What Postings Actually Ask For

### 2.1 JobsPipe job-description measurements (count date 2026-09-10; retrieved 2026-11-02, unchanged 2026-11-14) [B]

The per-title skill shares, remote shares and pay-disclosure shares from this JobsPipe pull (single-date snapshot as of 2026-09-10 [B · T0-69 KF7]) are kept in [data/posting_skill_shares.json](../../data/posting_skill_shares.json) and shown in [role skill inventories: posting evidence](role-skill-inventories.md#posting-evidence).

### 2.2 Skill and tool mentions in the S09 corpus (T0-03 §6.3) [B]

S09's posting and company shares are in [T0-03 §6.3](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md#63-skill-and-tool-mention-shares-s09-dataset-audit), and its comparison with two other corpora, which disagree by up to 5× (only "evals > fine-tuning" held in all three), is in [T0-03 §6.1.1](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md#611-corpora-comparison-same-skill-across-three-sampling-frames); the inventories tag each S09 share [S09 x%].

### 2.3 Agentic and protocol skills (T0-16) [C]

MCP's share in each postings index, the frameworks that lead inside agent-titled roles and the skills that co-occur with MCP are in [agentic protocols: how employers ask for it](agentic-protocols.md#how-employers-ask-for-it).

### 2.4 What the market devalues (T0-03 §4.3)

What to stop investing in (framework syntax, loyalty to one eval platform, static TensorRT-LLM engine builds, standalone prompt writing), and what to learn instead, is in the [skills radar](skills-radar.md#4-replace-what-to-stop-investing-in).

---

## 3. Skill Maps by Role

Roles appear in ranked-catalog order. Each map opens with the role's inventory, which lists every skill with its ontology tier and evidence. Below it come practice notes (graded points from the evidence, or a pointer to the page that works them through; they are not tiers), tools in use with their November 2026 status, proof of work, the interview track, and typical gaps or entry routes where the evidence has them.

<a id="skills-ml-engineer"></a>
### 3.1 Machine Learning Engineer (`ml-engineer`) · CCI rank #1

*Skills and tiers: [inventories/ml-engineer.md](inventories/ml-engineer.md). Posting shares for Machine Learning Engineer postings: [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Tools (Nov 2026):**
  - PyTorch; Hugging Face Transformers/PEFT/**TRL v1.0** (shipped 2026-03-31, 75+ post-training methods: SFT, DPO, reward modelling, RLOO, GRPO [A · T0-69 L190]); Ray Train/Serve [S09 3.0%]; W&B (CoreWeave-acquired 2025-05-05, Weave Apache 2.0 [C · T0-69 L370]); MLflow [P]; vLLM 0.32 / SGLang 0.5.22; TensorRT-LLM (PyTorch backend only; static `trtllm-build` removed [A · T0-69 L366]); **avoid `torchtune`** (dormant [A · T0-69 L367]).
  - FSDP2/DDP [S · T0-13 D8]; Megatron [S · T0-05, RadixArk JD]; DeepSpeed and Slurm appear on cluster-heavy variants [S · T0-54].
- **Practice note:** 70% (14 of 20) of interviewed production agent teams in `arXiv 2512.04123v2` used off-the-shelf models rather than fine-tuning (`B · T0-03`; ERRATA U36) — beat prompting and retrieval baselines before training weights.
- **Proof of work:**
  - A baseline-first model with measured lift and error analysis.
  - A prompt vs RAG vs fine-tune comparison with cost and quality numbers.
  - A serving benchmark covering tokens/s, p95 and $/M tokens [S · T0-06].
  - Training evidence on a small budget [S · T0-13 D8 M1–M5]:
    - Validate an Ultra-Scale-Playbook memory/throughput model against 1-GPU measurements.
    - Run CPU/gloo smoke tests of DDP/FSDP2 sharding, checkpointing and resume.
    - Run scaled-down nanochat jobs and report MFU and tokens/s.
- **Interview:** classic ML system design (recsys, fraud, ETA) plus coding, with a "where would an LLM help?" probe. Databricks MLE loops cover LLM training systems and RAG over millions of documents [C · T0-14].
- **Typical gaps:**
  - Backend engineers: ML maths and statistics.
  - Data scientists: production engineering and serving.
  - PhDs: production craft and shipping speed [D · T0-06].

<a id="skills-ai-engineer"></a>
### 3.2 AI Engineer (`ai-engineer`) · CCI rank #2

*Skills and tiers: [inventories/ai-engineer.md](inventories/ai-engineer.md). Posting shares for AI Engineer postings: [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Practice notes:**
  - **Cache-aware prompt layout, stable prefix first.** Datadog telemetry (>1,000 orgs) shows only **28%** of LLM spans on cache-capable models achieve cached reads even though **69%** of input tokens are system prompts; **59%** of requests are still single-call, overall error rate is **5%**, and **60%** of errors in Feb 2026 were rate limits [A/B · Datadog, T0-03 L102–L103, L467–L468].
  - **Real cost multipliers matter more than list price.** GEICO's production cost audit found effective prices spanning **$0.21–$15.25 per 1M tokens** with a **2.5×–24×** penalty from poorly structured multi-turn context, uncached prefixes and oversized models [B · T0-03 L103, L470–L471].
  - **Multi-provider routing and model half-life.** Over 70% of Datadog orgs use 3+ models, Langfuse Cloud OpenAI trace share fell 82.7% to 55.3%, and Vercel AI Gateway median model replacement is **61 days** (~6-week half-life) [B · T0-69 L52, L221]. Token economics and RAG vs long-context vs fine-tuning are worked through in [system-design archetypes](../08-interviewing/system-design-archetypes.md) [A/B · T0-14].
- **Tools (Nov 2026)** [S · T0-03, T0-16, T0-69]:
  - **Agent frameworks:** LangGraph 1.x (59.0M 30-day PyPI downloads via `pepy.tech`; LangChain 157.6M as of 2026-11-11 [B · T0-69 L132–L133]), LlamaIndex Workflows, OpenAI Agents SDK (GA 2026-03-23, native Temporal) & **Responses API** (replaced retired Assistants API on 2026-08-26 [A · T0-69 L362]), Claude Agent SDK, Pydantic AI 2.x, Microsoft Agent Framework 1.0 (GA 2026-04-03 [B · T0-69 L364]), Google ADK 2.x.
  - **Evals:** DeepEval, UK AISI Inspect AI, Promptfoo (OpenAI acquisition announced 2026-03-09 [A · T0-69 L374]) and RAGAS (active: v0.4.4rc1 shipped 2026-11-13 [B · T0-69 L50]). Avoid eval-brand lock-in — 7 eval/obs tools were acquired or sunset in 13 months [B · T0-69 L51].
  - **Tracing:** Langfuse (ClickHouse acquisition announced 2026-01-16, stays open source [A · T0-69 L372]), Phoenix, LangSmith, Braintrust and OpenTelemetry/Traceloop (ServiceNow-acquired 2026-05-05, Apache 2.0 [C · T0-69 L375]) are listed interchangeably in JDs.
  - **Storage and gateways:** Vector databases appear as a category in 32.6% of AI Engineer postings while brand popularity is **unresolved** (DB-Engines scores rose +37% to +146% across Pinecone, Qdrant, Weaviate and Milvus in 2025, so brand demand is not falling even though JDs name the category [M · T0-69 L59, L350]); LiteLLM gateway.
- **Proof of work:**
  - **T0–T1:** an evaluated system over a real corpus. Include a metrics table (recall@k, rubric correctness, faithfulness), a cost/latency budget, and a reproducible README.
  - **T2–T3:** a second system with a different failure surface (an agent with approvals and budgets), plus CI-gated evals, traces, a load test and a postmortem [S · T0-06, T2-01].
  - **Specialisation option:** a "reliability layer for LLM apps": caching, backoff, budgets, fallbacks, trace replay, eval-regression CI [S · T0-06].
  - **If you host a live demo,** default to replay mode and harden it with the H1–H14 checklist in [proof-of-work standards](../05-portfolio/proof-of-work-standards.md#checklist) [D · T0-13].
- **Interview:** the application track: RAG with ACL enforcement, agent loop control, eval architecture, context management [B/C · T1-03]. Plus the 45-minute design blueprint (5 / 4 / 9 / 16 / 7 / 4 minutes) [S · T0-14].
- **Typical gaps:**
  - Backend: evals (the largest gap), LLM API fluency, retrieval, and Python if coming from Java/Go.
  - Data scientists: production hygiene, serving/ops, DSA and system design.
  - Frontend: evals, retrieval, a service layer.
  - PhDs: production craft and code review [D · T0-06].
- **Avoid:** wrapper-only demos; framework-syntax memorisation; retired OpenAI Assistants API tutorials; single-provider chat wrappers.

<a id="skills-forward-deployed-engineer"></a>
### 3.3 Forward Deployed Engineer (`forward-deployed-engineer`) · CCI rank #3

*Skills and tiers: [inventories/forward-deployed-engineer.md](inventories/forward-deployed-engineer.md).*

- **Measured (`T0-51`, n=28 excerpts, lower bounds):** customer scoping (50.0%), Python (42.9%), LLM APIs (39.3%), agents (35.7%), APIs (32.1%), stakeholder management (25.0%), evals (21.4%) [C · T0-51 L782–L793].
- **Tools:** the AI Engineer stack, plus customer data platforms (Databricks, Palantir, Snowflake) [S], cloud AI services (Bedrock, Azure OpenAI, Vertex) [P], and enterprise connectors [P].
- **Proof of work:**
  - A customer pilot case study with numbers [S · T0-06].
  - A demo on a real data source shown to ≥2 potential users [S · T2-01].
  - A deployment write-up that covers failure modes.
- **Interview:** T1-03 and T0-51 file FDE under the customer-application track: scoping under ambiguity, production API/agent integration, eval architecture and live debugging/customer walkthroughs [B/C · T1-03; T0-51] (the older Databricks AI-FDE RAG/multi-agent loop claim in T0-14 was unconfirmed in T0-51; ERRATA U48 K9). Prepare a customer-scoping scenario as well [P].
- **Typical gaps:**
  - Backend engineers: customer-facing skills.
  - Frontend engineers: backend and infrastructure.
  - Non-technical candidates: coding plus infrastructure, roughly 10 months of work [D · T2-01].

<a id="skills-research-engineer"></a>
### 3.4 Research Engineer / Member of Technical Staff (`research-engineer`) · CCI rank #4

*Skills and tiers: [inventories/research-engineer.md](inventories/research-engineer.md).*

- **Proof of work:**
  - Paper re-implementations with rigorous evals [S · T2-01].
  - Compact reimplementations: a nano-vLLM-style engine (continuous batching, paged KV, prefix caching) in 1–2k lines, benchmarked against vLLM; distributed-training smoke tests with DDP/FSDP2 [S · T0-13 D8].
  - OSS contributions to training or serving stacks [S].
  - Fellowship projects; Anthropic Fellows does not require a PhD [B · T0-06].
- **Interview:** a research talk plus coding. Frontier labs add infrastructure research-engineering rounds (KV cache, batching, GPU scheduling); Tier 4 candidates face the full research loop [S · T2-01, T1-03].

<a id="skills-applied-scientist"></a>
### 3.5 Applied Scientist (`applied-scientist`) · CCI rank #5

*Skills and tiers: [inventories/applied-scientist.md](inventories/applied-scientist.md).*

- **Proof of work:**
  - Your own method turned into a service with tests and CI.
  - At least three code reviews via OSS pull requests.
  - An eval-statistics write-up [S · T0-06].
- **Interview:** ML design is usually a strength for PhDs; coding is the usual gap. Some loops include a research talk [S · T2-01].

<a id="skills-applied-ai-engineer"></a>
### 3.6 Applied AI Engineer (`applied-ai-engineer`) · CCI rank #6

*Skills and tiers: [inventories/applied-ai-engineer.md](inventories/applied-ai-engineer.md).*

- **Proof of work:** a customer-facing reference implementation with evals and a published write-up [P]; then the AI Engineer T2–T3 portfolio.
- **Interview:** the application track plus customer scenarios [S · T0-14 Applied-AI loop].

<a id="skills-research-scientist"></a>
### 3.7 Research Scientist (AI/ML) (`research-scientist`) · CCI rank #7

*Skills and tiers: [inventories/research-scientist.md](inventories/research-scientist.md). Posting shares for all-field Research Scientist postings: [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Proof of work:** papers, open research code, talks [S].
- **Interview:** a research talk, deep technical discussion and coding. Offers are "not plannable" [D · T0-06].

<a id="skills-ai-infrastructure-engineer"></a>
### 3.8 AI Infrastructure / GPU Platform Engineer (`ai-infrastructure-engineer`) · CCI rank #8

*Skills and tiers: [inventories/ai-infrastructure-engineer.md](inventories/ai-infrastructure-engineer.md). Posting shares for DevOps Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-54`, n=35 / 12 full-read):** GPU fleet ops and scheduling 94.3% (83.3% full-read), Kubernetes 80.0%, InfiniBand/RDMA networking 51.4% (83.3% full-read), Slurm 42.9% (62.5% in HPC/platform/neocloud variants, 0% in fleet-lifecycle variant A), SRE 37.1% (66.7% full-read), storage/checkpointing 22.9% [B · T0-54 L57, L98, L172–L181].
- **Tools (Nov 2026):**
  - **Cluster and serving:** Kubernetes GPU scheduling; **Slurm** [S · T0-54 L181]; Ray [S09 3.0%]; NVIDIA Dynamo [S]; parallel storage (Lustre/WEKA named in 8/35 T0-54 postings [S · T0-54 L361]).
  - **Monitoring:** Prometheus/Grafana [S].
- **Proof of work:** a self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem [S · T0-03].
- **Interview:** the infrastructure track. Anthropic prompts include GPU cluster design and mixed GPU allocation; strong infrastructure candidates without ML experience do well [B · T0-14].
- **Entry routes:** a paid residency: RadixArk AI Infra Resident, listed at $200K, SGLang experience not required. Caveats: the Accel listing showed "Posted 6+ months ago" and the Greenhouse copy lists no salary [B · T0-05].

<a id="skills-ml-platform-engineer"></a>
### 3.9 ML Platform / MLOps Engineer (`ml-platform-engineer`) · CCI rank #9

*Skills and tiers: [inventories/ml-platform-engineer.md](inventories/ml-platform-engineer.md). Posting shares for DevOps Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-58`, n=31 coded):** lifecycle tooling 67.7% (MLflow 45.2%, Kubeflow 41.9%; union 51.6%, especially in India GCCs/services), Kubernetes 61.3%, cloud 51.6%, Git/CI 45.2%, IaC 41.9%, observability 41.9%, Airflow 16.1%; LLM gateways and supply chain were 0/31 and remain differentiators [B · T0-58 L177–L200].
- **Tools (Nov 2026):**
  - **Lifecycle & tracking:** MLflow, Kubeflow, Airflow, feature stores [S · T0-58 L184–L192]; W&B (CoreWeave-acquired 2025-05-05 [C · T0-69 L370]).
  - **Serving and gateways:** KServe, Ray (Anyscale acquired by Nscale 2026-07-30 [B · T0-03 L340]), LiteLLM, Azure APIM MCP, Foundry AI Gateway, AgentCore Gateway, AAIF `agentgateway` / `Agent Router`, Cloudflare MCP server portals [S · T0-16].
  - **Observability:** Langfuse (ClickHouse acquisition announced 2026-01-16 [A · T0-69 L372]), Phoenix (ELv2 licence), Prometheus/Grafana/Datadog [S].
- **Proof of work:** a self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, MLflow/Kubeflow model registry, dynamic LoRA routing and Grafana dashboards [S · T0-03, T0-58].
- **Interview:** the infrastructure track plus platform design questions: gateway, playground, model distribution [S · T0-14].

<a id="skills-ai-security-engineer"></a>
### 3.10 AI Security Engineer / AI Red Teamer (`ai-security-engineer`) · CCI rank #10

*Skills and tiers: [inventories/ai-security-engineer.md](inventories/ai-security-engineer.md). Posting shares for Security Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-60`, n=18):** red-teaming 78% (14/18), prompt injection 44% (8/18), offensive security/VAPT 39% (7/18; e.g. Amazon 5+ yr), agent abuse 39% (7/18), MITRE ATLAS 11% (2/18); SANS counted >850 AI/ML security postings in mid-September 2026 [B/C · T0-60 L237–L250; T0-69 L60].
- **Proof of work:** a red-team suite in CI (custom, Promptfoo or Inspect AI) mapped to OWASP GenAI LLM Top 10 2026, OWASP Agentic Top 10 and MITRE ATLAS against a working agent, with measured attack-success rates before and after mitigation [S · T0-13 R2, T0-68 L606]; an own-instance MCP security audit [P].
- **Interview:** "design safeguards for an AI system that can take actions on behalf of a user" [S · T0-14 A15].
- **Programme:** Anthropic AI Security Fellow (requires US/UK/Canada work authorisation; Anthropic reports >40% of its first Fellows cohort joined full-time — vendor-reported with COI [C, COI · T0-06 L706; ERRATA U31]).

<a id="skills-inference-engineer"></a>
### 3.11 Inference / LLM Serving Engineer (`inference-engineer`) · CCI rank #11

*Skills and tiers: [inventories/inference-engineer.md](inventories/inference-engineer.md).*

- **Measured (`T0-56`, n=37):** vLLM 76% (28/37; 100% of engine-naming postings), SGLang 57% (21/37), TensorRT-LLM 41% (15/37), batching/KV cache 49% (18/37), speculative decoding 35% (13/37), quantisation 30% (11/37), parallelism 24% (9/37), disaggregated prefill/decode 16% (6/37) [B · T0-56 L68–L69, L197–L212].
- **Practice notes:**
  - **Speculative decoding:** measure acceptance rate and goodput before enabling it by default [A · T0-14]. T0-03 gives α < 0.6 as an example of where drafting overhead can cause a net regression; the threshold depends on draft cost, length and load.
  - **KV-cache and latency arithmetic** (bytes per token, the end-to-end latency budget) is in the formula kit of the [system-design archetypes](../08-interviewing/system-design-archetypes.md). Llama-3.1-70B needs about 320 KiB per token at BF16 [S · T0-14 F4]; T0-03 §6.10 mislabels that value as FP8, which is half (erratum U11).
- **Security:** patch serving-engine CVEs promptly [A/B · T0-03]:
  - SGLang had three critical CVEs in H1 2026: CVE-2026-5760 (GGUF template RCE) and CVE-2026-3059/3060 (pickle deserialisation).
  - vLLM CVE-2026-22778 (weight-loader RCE) and CVE-2026-27893 (`trust_remote_code`, fixed in v0.18.0).
  - Parse templates in a sandbox.
- **Tools (Nov 2026):** vLLM 0.32, SGLang 0.5.22, TensorRT-LLM (PyTorch backend only; NVIDIA migration guide updated 2026-11-03 documents removal of static `trtllm-build` [A · T0-69 L366]), NVIDIA Dynamo 1.6.0 (1.0 GA 2026-03-16), Dynamo Triton (the renamed Triton Inference Server), FlashInfer, LMCache, Mooncake, llm-d. **Hugging Face TGI entered maintenance mode / read-only archive (2026-03-21, secondary); do not use it for new work** [A/C · T0-03; T0-69 L365].
- **Proof of work** (T0-13 R3 specification):
  - **Benchmark scope:** a single-GPU study comparing BF16 vs FP8/4-bit, prefix caching, chunked prefill and speculative decoding.
  - **Kernel:** a custom Triton kernel tested against a reference implementation.
  - **Measurement:** a multi-process load generator; a quality gate with confidence intervals; $/M tokens at the SLO; a roofline analysis.
  - **Contribution:** an upstream PR to vLLM, SGLang or FlashInfer [S]. Know the house rules first [S · T0-05]:
    - vLLM requires DCO sign-off and AI-use disclosure, and rejects one-off typo PRs.
    - vLLM does not allow pure code-agent PRs; breaches can lead to automatic banning.
    - SGLang lets only top and trusted contributors trigger CI.
  - **Load-test method:** use multi-process generators (inference-perf, GuideLLM) with Poisson arrivals. Single-process Python clients can inflate TTFT/TPOT, and warm-up matters: one report shows 2,484 ms first-run vs ~73 ms steady-state TTFT [S · T0-13].
- **Interview:** the infrastructure track: KV-cache math, decode roofline, continuous batching, prefill/decode disaggregation, GPU scheduling. Anthropic has one reported p95-latency debugging prompt [C · T0-14, T1-03]; prepare by splitting latency into queue, prefill and decode. Anthropic details [B/C · T0-14, T0-13]:
  - A design-document review round (first observed April 2026, 3 reports).
  - The one-hour design round runs in a shared Google Doc, and live rounds default to no AI assistance.
  - The public performance take-home runs in a Python simulator and needs no GPU.
- **Typical gap:** backend engineers moving to Tier 3 need infrastructure depth; plan on roughly 10–14 months [D · T2-01].

<a id="skills-ai-solutions-architect"></a>
### 3.12 AI / GenAI Solutions Architect (`ai-solutions-architect`) · CCI rank #12

*Skills and tiers: [inventories/ai-solutions-architect.md](inventories/ai-solutions-architect.md). Posting shares for all Solutions Architect postings (adjacent): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-62`, n=23):** customer-facing technical experience 95.7% (22/23), pre-sales 60.9% (14/23), cloud 52.2% (12/23; split evenly across AWS 26.1%, Azure 30.4%, GCP 30.4%), agents 56.5%, RAG 26.1%, evals 17.4%; Axial US AI-architecture (n=16,927) shows cloud 62% and observability 39% [B · T0-62 L146–L155, L688–L690].
- **Credentials:** a tie-breaker only in IT services, staffing and partner firms:
  - Options as of November 2026: **Google Cloud PAA** (ranked #1, MCP + A2A + 2 labs, GA mid-Nov 2026), AWS `AIP-C01`, Google `PMLE`, Azure `AI-103` (status provisional pending T0-28) and partner-gated Anthropic `CCAR-P`/`CCAR-F`; statuses in [credentials by role](../04-certifications/credentials-by-role.md).
  - No certification is verified in more than 10% of GenAI JDs [B · T0-11, T0-62].
- **Proof of work:** an eval-backed customer reference architecture with a cost and latency walkthrough (IaC optional outside cloud-partner tracks; 0/23 in T0-62) [P · T0-62].

<a id="skills-ai-product-manager"></a>
### 3.13 AI Product Manager (`ai-product-manager`) · CCI rank #13

*Skills and tiers: [inventories/ai-product-manager.md](inventories/ai-product-manager.md). Posting shares for Product Manager postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-59`, n=41):** AI literacy ≥46% (19/41), eval rubrics ≥27% (11/41; 5 of 9 opened pages), success metrics ≥24%, AI-assisted prototyping ≥15% (Microsoft AI, OpenAI, Lovable, Sarvam), Python/SQL ≥10% [B · T0-59 L176–L185].
- **Proof of work:**
  - A PRD paired with a working AI-coded prototype, an eval rubric and pilot metrics [S · T0-06, T0-59 L181].
  - A domain rubric with 50+ labelled cases.
  - "10 failure modes ranked by business impact" [S · T2-01].
- **Interview:** AI product sense, evals/technical-depth round and, at AI-native firms, a live build round [B/S · T0-59 L61; T2-01].
- **Entry fee:** 4+ years as a PM (~3+ yr at mid-size/enterprise teams; 5–10+ yr at frontier labs) plus at least one shipped model-powered feature [B/D · T0-06, T0-67 L154–L155].

<a id="skills-agentic-ai-engineer"></a>
### 3.14 Agentic AI Engineer (`agentic-ai-engineer`) · CCI rank #14

*Skills and tiers: [inventories/agentic-ai-engineer.md](inventories/agentic-ai-engineer.md).*

- **Measured:** standalone "agentic"-titled volume is a niche (Skilark: 107 of 28,771 AI listings = 0.37%, Feb 2026 [C · T0-57 L118]); frameworks are named more often than MCP in agent-titled postings ([agentic protocols](agentic-protocols.md#inside-agent-titled-roles-frameworks-lead) [C · T0-16.F10]).
- **Protocols** [S · T0-16, T0-69] (protocol facts are kept in [agentic protocols](agentic-protocols.md)):
  - **MCP, spec revision 2026-07-28:**
    - Stateless core (`server/discover`, `subscriptions/listen`, OTel trace context in `_meta`); Client ID Metadata Documents replace dynamic client registration (DCR); 12-month minimum deprecation window.
    - Extensions: MCP Apps, Enterprise-Managed Authorization, `io.modelcontextprotocol/tasks`.
    - Deprecated: Roots, Sampling, Logging, HTTP+SSE, `includeContext` (`thisServer`/`allServers`) [A, COI · T0-69 L392–L398].
  - **A2A v1.0:** task states, contextId, signed Agent Cards. It has no consensus mechanism and no exactly-once delivery.
  - **AG-UI 1.0** (CopilotKit; not part of AAIF).
  - **MCP at scale** [S · T0-16]:
    - Progressive discovery / code mode: one illustrative task fell from ~150,000 to ~2,000 tokens when tools were presented as code APIs.
    - `Mcp-Method` / `Mcp-Name` routing headers for gateways.
    - Cacheable `tools/list` (`ttlMs`, `cacheScope`); never serve per-user tool visibility from a shared cache.
  - **SDK churn:** Python SDK v2 and FastMCP 4.x track the new spec; the TypeScript SDK v2 splits packages and removes server-side SSE. Pin major versions [S · T0-16].
- **Security** [S · T0-16, T0-14]:
  - Treat tool and peer outputs as untrusted.
  - Apply the Rule of Two (avoid the "lethal trifecta" of private data, untrusted input and outbound actions in one session).
  - Defend against prompt injection and session smuggling.
- **Tools (Nov 2026):**
  - Recommended: LangGraph 1.x, Temporal [S09 2.3%], OpenAI Agents SDK & Responses API, Claude Agent SDK, Pydantic AI 2.x, Microsoft Agent Framework 1.0 (GA 2026-04-03; MCP GA, A2A "coming soon" [B · T0-69 L387]), Google ADK 2.x, FastMCP 4.x, `langchain-mcp-adapters`, LiveKit (voice agents [C · T0-69 L62]).
  - **Avoid AutoGen** (stalled: no PyPI release for 410 days [A · T0-69 L363]) and retired OpenAI Assistants API. CrewAI is absent from tier-1 lab postings [S · T0-03].
- **Proof of work:** an agent with human approval, sandboxed tools, deterministic trace replay and failure-injection tests (practice-curated differentiators [P · T0-57 L233]), reporting cost per task [S · T0-06].
- **Interview:** agent loop control; tool-gateway design; workflow vs agent trade-offs [S · T1-03, T0-14].

<a id="skills-ai-evaluation-engineer"></a>
### 3.15 AI Evaluation Engineer (`ai-evaluation-engineer`) · CCI rank #15

*Skills and tiers: [inventories/ai-evaluation-engineer.md](inventories/ai-evaluation-engineer.md).*

**Measured:** evals/benchmarking appears in 19.0% of S09 postings and at 68.2% of companies [S09], and in 59.7% of AI-first roles [T0-13]. In `T0-60` (n=18), LLM judges appear in 8/13 non-lab postings (44% overall) and golden datasets in 7/13 (39% overall) [C · T0-60 L150–L151]. Only 52.4% of agent teams run offline evals and 37.3% online evals [B/C · LangChain survey].

- **Tools (Nov 2026):**
  - **Eval frameworks:** UK AISI Inspect AI (MIT licence, 200+ evals [B · T0-68 L605]), DeepEval, Promptfoo (OpenAI acquisition announced 2026-03-09 [A · T0-69 L374]), TruLens and **RAGAS** (active: `v0.4.4rc1` shipped 2026-11-13 under `vibrantlabsai`, lifting prior dormancy [B · T0-69 L50, L377]; still avoid eval-brand lock-in).
  - **Tracing platforms:** LangSmith, Langfuse (ClickHouse), Phoenix, Braintrust and OpenTelemetry/Traceloop (ServiceNow); JDs treat these as interchangeable; **Humanloop** sunset 2025-09-08 [C · T0-69 L371].
  - **Do not store master API keys in SaaS eval platforms** (Braintrust breach, 2026-05-04) [A/B · T0-03].
- **Proof of work:**
  - An eval harness with a κ-calibrated binary judge per failure mode validated on **100–200 human labels per failure mode** (starting from ~100 traces / 30+ manual labels [C · T0-20 L63, L196]), plus position and verbosity bias tests (`arXiv:2606.19544` shows raw agreement overstates κ by 33–41 points [A/B · T0-03 L98]).
  - A CI regression threshold and a cost–quality frontier chart [S · T0-06].
- **Interview:** eval design is the most frequent GenAI-engineer question in one aggregate ("Evaluate an LLM System", 19 guides) [C · T0-14]: golden sets, judge calibration, online sampling, A/B tests. T1-03's behavioural questions B11–B12 probe grader design and contamination [B/C · T1-03].
- **Best feeders:** data scientists (error analysis, judge validation), PhDs (measurement rigour), backend engineers (CI, observability) [D · T0-06].

<a id="skills-gpu-kernel-engineer"></a>
### 3.16 GPU Kernel / ML Compiler Engineer (`gpu-kernel-engineer`) · CCI rank #16

*Skills and tiers: [inventories/gpu-kernel-engineer.md](inventories/gpu-kernel-engineer.md).*

- **Measured (`T0-63`, n=41 core postings):** CUDA/Triton union 73.2% (CUDA 63.4%, Triton 56.1% / 69% of kernel-led postings), ML compilers 48.8%, profiling 46.3%, GPU fundamentals 36.6%, C++ 31.7%, TPU/Pallas/XLA 26.8%, PTX/SASS 22.0%, MLIR/LLVM 19.5%, NCCL 17.1%, ROCm/HIP 17.1%, open-source contributions 17.1% [B · T0-63 L186–L212].
- **Watch (Nov 2026):** **CUDA 13.1 Tile IR** (`cuda-tile` 1.7.0, COMPSAC 2026 ~60 lines Python on B200 [A/B · T0-03 L101, L180, L542]) and automated kernel agents (e.g. Cursor/NVIDIA multi-agent optimisation of 235 CUDA kernels [B · T0-63 L84]) are shifting raw kernel authoring toward tile DSLs and system-level roofline/numerics judgement.
- **Proof of work:**
  - GPU MODE leaderboard submissions (teams of up to 3) [S · T0-12]; AMD × GPU MODE kernel competitions run on organiser hardware [S · T0-13 M4].
  - Kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware and with correctness tests [S · T0-05, T0-13, T0-63 L209].
- **Interview:** kernel and system internals. Reported AMD kernel interviews overlap with GPU MODE material [C/D · T0-12].

<a id="skills-physical-ai-engineer"></a>
### 3.17 Physical AI / Robotics AI Engineer (`physical-ai-engineer`) · CCI rank #17

*Skills and tiers: [inventories/physical-ai-engineer.md](inventories/physical-ai-engineer.md).*

- **Measured (`T0-64`, n=48 / 12 full-text; ERRATA U38):** robot learning 79% (11/12 full-text), real-robot deployment 54% (11/12), simulation & sim-to-real 46% (10/12), imitation learning 42% (10/12), RL 42% (9/12), Python 38% (10/12), PyTorch 31% (8/12) and teleoperation data pipelines 27% (6/12). Hard-real-time C++ (19%) and ROS (15%) are variant-dependent (absent at Figure, Skild, Apptronik and 1X) [B · T0-64 L170–L192]. Note that "Helix" is a Figure AI department prefix, not a standalone role title [A · T0-64 L56].
- **Proof of work:** a sim-to-real or manipulation policy project (MuJoCo or NVIDIA Isaac Sim/Lab; PyTorch imitation/RL/VLA) deployed to real hardware with measured success rates, failure taxonomy and public code or publications (all 6 embodied-AI postings in T0-20 ask for publications or public OSS [B · T0-20 L70, L174]).

<a id="skills-ai-safety-researcher"></a>
### 3.18 Frontier AI Safety / Alignment Researcher (`ai-safety-researcher`) · CCI rank #18

*Skills and tiers: [inventories/ai-safety-researcher.md](inventories/ai-safety-researcher.md).*

- **Measured (`T0-60`, n=15):** alignment 53% (8/15), ML fundamentals (SFT/RLHF/RL) 27%, interpretability 27% (Must for interpretability variants) [C · T0-60 L682–L686].
- **Proof of work:** fellowship projects (Anthropic Fellows: ~4 months with stipend and compute; Anthropic reports >40% of its first cohort joined full-time — vendor-reported figure with COI [C, COI · T0-06 L706; ERRATA U31]); published empirical safety research; open eval contributions (e.g. UK AISI Inspect Evals) [P · T0-20 L82].
- **Market reality:** about 600 technical FTEs worldwide, growing about 21% a year; no pay data [C · T0-15].

<a id="skills-ai-governance-lead"></a>
### 3.19 AI Governance Programme Lead / Manager (`ai-governance-lead`) · CCI rank #19

*Skills and tiers: [inventories/ai-governance-lead.md](inventories/ai-governance-lead.md).*

**Measured (`T0-34`, `T0-61`):** Axial US AI-governance (n=1,997, C): Python 27.1%, observability/monitoring 42.3%, OneTrust 8.7–9.2%, Azure 11.1%, CISSP 10.4%, AIGP 8.9%, CIPP 8.2%, CISM 8.1%, CIPM 6.8%, CRISC 6.4%, CISA 5.9% [C · T0-34 L51–L52, L618–L624]. GRC Careers AI Governance board (n=76, B [COI]): **CISA 17.1% (#1)**, **CISM 13.2% (#2)**, **CRISC 11.8% (#3)**, CIPP 9.2%, CISSP 7.9%, **AIGP 6.6% (7.5% merged; 10.0% of 30 AI-Gov-tagged)**, CIPM 6.6% [B, COI · T0-34 L51–L52, L610–L616]. India purposive sample (n=9, B): CISA 6/9, CISSP 5/9, CRISC 5/9, ISO/IEC 42001 LI/LA 5/9, AIGP 3/9, DSCI DCPP/DCPLA 0/9 [B · T0-34 L54, L632–L639].

- **Practice notes:**
  - **The regulatory map (updated July 2026):** Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 2026-07-27) moved EU AI Act Annex III high-risk enforcement to **2027-12-02** and Annex I to **2028-08-02** (Art. 50 transparency applied 2026-08-02) [A/B · T0-61 L89, L369; T0-68 L367]. Colorado SB 24-205 was repealed and replaced by narrower SB 26-189 (effective 2027-01-01) [B/C · T0-61 L374]. Full map in [governance careers](../11-tracks/governance-careers.md).
  - **Transparency marking:** the voluntary transparency Code (final 10 Jun 2026, ~190 signatories) asks for at least two marking layers and does not name C2PA [A/B · T0-15].
- **Credentials:** established domain certifications lead in postings (CISA, CISM, CRISC, CISSP, CIPP/CIPM); AIGP ($649 member / $799 non-member, BoK v2.1 Feb 2026; no ISO/IEC 17024 listing found) is a secondary tie-breaker [B · T0-34 L50–L52, L269].
- **Tools:**
  - Seen in postings: OneTrust; IBM OpenPages (one analyst JD) [S].
  - Not named in Axial's lists or the T0-15/T0-61 JDs: Credo AI and Holistic AI [S].
- **Proof of work:** an AI inventory, use-case intake workflow, risk register and governance playbook mapped to the amended EU AI Act, NIST AI RMF and ISO/IEC 42001 [S · T0-06, T0-61].

<a id="skills-ai-product-engineer"></a>
### 3.20 AI Product Engineer (AI Frontend) (`ai-product-engineer`) · CCI rank #20

*Skills and tiers: [inventories/ai-product-engineer.md](inventories/ai-product-engineer.md). Posting shares for Full-Stack Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Measured (`T0-62`, n=16):** TypeScript 81.3%, product sense / ownership 50.0%, Next.js 43.8%, Python 18.8% [B · T0-62 L349–L353, L722–L725].
- **Tools (Nov 2026):** **Vercel AI SDK 7** (shipped 2026-06-25, ESM-only, Node.js 22+; replaces AI SDK 6 [B · T0-68 L79, L364]); AG-UI, MCP Apps and A2UI for agent UI. On-device and browser inference: WebGPU (in all major browsers), Transformers.js v4, Chrome built-in AI (Prompt API), WebMCP (draft API moved to `document.modelContext` [C · T0-68 L365]); treat these as a differentiator, not a job [S · T0-06, T2-01].
- **Proof of work:**
  - A full-stack app (frontend → API → LLM → eval) with streaming cancel/retry/error states, accessibility, 50 eval cases and UX metrics [S · T0-06, T0-62].
  - An on-device module benchmarked on ≥3 device/browser combinations, with feature detection and a fallback [S · T0-06].
- **Interview:** the **product-frontend** track (streaming agent UX, state management, product sense, live frontend/API build; ERRATA U48 [B · T0-62]), plus AI-enabled coding rounds [S · T2-01].

<a id="skills-ai-risk-assurance-specialist"></a>
### 3.21 AI Risk, Audit & Compliance Specialist (`ai-risk-assurance-specialist`) · CCI rank #21

*Skills and tiers: [inventories/ai-risk-assurance-specialist.md](inventories/ai-risk-assurance-specialist.md).*

- **Measured (`T0-61`, n=8):** compliance docs 38%, third-party AI risk 38%, controls testing 25%, AI inventory/registry 25% [C · T0-61 L684–L687]. Note that CISA/CIA/CPA/ACCA/ICAEW/CA ANZ is a prerequisite for the ISACA AAIA credential (`T0-34 K10`, excluding Indian CA), not a universal job gate [B · T0-34, T0-61].
- **Proof of work:** a reproducible model-validation or bias-audit harness and report on a public model, using documented methodology [P · T0-61].

<a id="skills-responsible-ai-engineer"></a>
### 3.22 Responsible AI / AI Governance Engineer (`responsible-ai-engineer`) · CCI rank #22

*Skills and tiers: [inventories/responsible-ai-engineer.md](inventories/responsible-ai-engineer.md).*

- **Measured (`T0-61`, n=8):** LLM evaluation pipelines 75% (6/8), fairness & bias 38% (3/8), Python 38% explicit (implied in eval pipeline work), guardrails 25%, EU AI Act / NIST / ISO 25%; Fairlearn/SHAP/LIME/Captum 0/8 and NeMo Guardrails/Giskard 1/8 (Cognizant nice-to-have only) — the evaluation/fairness practice matters far more than any single library [C · T0-61 L309–L320].
- **Tools (Nov 2026):**
  - Named in JDs: NeMo Guardrails, Giskard (v3) and Arize (optional/preferred in single JDs); Azure AI, Azure ML, AI Foundry, Microsoft Fabric and Purview [S · T0-15, T0-61].
  - Fairness and explainability: Fairlearn, SHAP, LIME, Captum; AIF360 (stale since Apr 2024; pin or fork); model cards [S · T0-15].
  - Absent from sampled JDs: Guardrails AI and C2PA (portfolio-only) [S · T0-15].
- **Proof of work:** a compliance packet mapped to NIST AI 600-1 and **OWASP GenAI LLM Top 10 2026**, with CI-tested runtime guardrails, structured tracing, subgroup evals and a binary judge calibrated on **100–200 human labels per failure mode** [S/C · T0-15, T0-20 L63, L196, T0-61, T0-68 L606].

<a id="skills-ai-enablement-engineer"></a>
### 3.23 AI Enablement Engineer (`ai-enablement-engineer`) · CCI rank #23

*Skills and tiers: [inventories/ai-enablement-engineer.md](inventories/ai-enablement-engineer.md).*

- **Measured (`T0-62`, n=15 + Skillenai n=42 as of 2026-11-05):** teaching/workshops 60.0% (9/15), internal tooling 46.7%, change management 46.7%, agents 33.3% (Skillenai 16.7%), coding agents 33.3%, prompt engineering 33.3% (Skillenai 35.7%), Python 26.7% (Skillenai 33.3%), MCP 26.7% (Skillenai **19.0% on 2026-11-05**, down from **30.2% on 2026-10-14** [B/C · T0-62 L261–L281; T0-16 L393]), GRC 26.7%, IAM/SSO 20.0% (Must inside platform variant only) [B · T0-62].
- **Proof of work:** an internal pilot with 5–10 colleagues measuring adoption and time saved, plus a sanitised MCP server with SSO/OAuth for platform-variant targets, a runbook and a risk register [S · T0-06, T0-62].

<a id="skills-domain-evaluation-specialist"></a>
### 3.24 Domain Evaluation Specialist / AI Trainer (`domain-evaluation-specialist`) · CCI rank #24

*Skills and tiers: [inventories/domain-evaluation-specialist.md](inventories/domain-evaluation-specialist.md).*

- **Measured (`T0-66`, n=18):** human evaluation 67% (12/18; 12/14 expert-grader postings), domain depth 61%, writing 44%, error analysis 39%, eval rubrics 33%, golden datasets 33% [C · T0-66 L630–L635].
- **Proof of work:** a domain gold standard: 100+ real tasks with rubrics, adjudication rules and two-reviewer agreement, comparing 2–3 models against the existing human baseline [S · T0-06, T0-66].
- **Next step:** this is "a bridge, not a destination". Move toward an in-house eval-lead, AI PM or governance role [S · T0-06].

<a id="skills-leadership"></a>

### 3.25 Leadership and independent tracks

*Skills and tiers: all five leadership and independent tracks now have dedicated inventories in [data/skills_ontology.json](../../data/skills_ontology.json) (indexed in [role-skill-inventories.md](role-skill-inventories.md)): [AI engineering manager](inventories/ai-engineering-manager.md), [VP / Head of AI](inventories/vp-head-of-ai.md), plus dedicated RP2-backed profiles for [Chief AI Officer](../02-roles/hubs/chief-ai-officer.md), [Independent AI Consultant](../02-roles/hubs/independent-ai-consultant.md) and [Fractional AI Leader](../02-roles/hubs/fractional-ai-leader.md).*

**AI Engineering Manager / Director (`T0-65`, n=8 text-visible):**
- **Measured:** leadership 100%, people management 100% (2–6 yr managing named in 5/8; 8+ yr total engineering), stakeholder alignment 75%, technical leadership 75%, roadmapping 38%, system design 38%, mentoring 38%, hiring 25% (Must at labs); GRC (0/8) and guardrails (1/8) dropped well below generic EM feeder shares [B/C · T0-65 L154–L168, L202]. (Do not rely on the unverified SignalFire "<3 years to management" claim; ERRATA U30.)
- **AI-specific skills:** making eval and observability a shared practice other teams consume (the "Staff scope" in T0-14) [S]; hiring senior AI ICs; managing the first 90 days (63% of organisations lack, or are unsure they have, data-management practices for AI, Gartner [A/B · T0-09]).

**VP / Head of AI (`T0-65`, n=11 text-visible):**
- **Two distinct variants:** **Player-coach** (5/11: first AI hire or small team, reports to CEO/CTO, ships production systems) vs **Enterprise strategy/operations lead** (portfolio scorecard, governance, build-vs-buy, vendor leadership without direct authority) [A/B · T0-65 L212–L214, L235–L248].
- **Measured:** strategy 91% (10/11), hands-on production AI 45% (5/11 — Must for player-coach, Optional for enterprise), leadership 45%, stakeholder 45%, hiring 27%, org design 27%; unit economics and capacity/cost were 0/11 explicit in extracts [B/C · T0-65 L235–L248]. Operating-model design: ~two-thirds of senior leaders prefer hub-and-spoke [C · T0-01 F12].

**Chief AI Officer (`T0-65`, n=7 text-visible):**
- **Measured:** strategy 100% (7/7), responsible AI / governance 86% (6/7), AI platform/systems technical depth 43% (3/7; SBI, Axial, Riverside), executive/board communication, hiring, build-vs-buy and business case [B/C · T0-65 L313–L320].
- **Federal mandate (strictly CAIO, not VP/Head of AI; ERRATA U43):** US federal agency CAIO designations are mandated by **OMB M-25-21** (dated 2025-04-03, Grade A [T0-65 L292]); private-sector CAIO seats are voluntary, often dual-hatted, and average ~2.2 years tenure (Avasant, C [T0-65 L302]).

**Independent AI Consultant / Contract Builder & Fractional AI Leader (`T0-66`):**
- **Separate the two markets:**
  - **Independent AI Consultant / Contract Builder** is hands-on delivery (`T0-66` UK IT Jobs Watch GenAI contract benchmark n=1,466 [B]: Python 34.6%, LLM apps 34.1%, Azure 29.7%, ML 28.5%, stakeholder management 27.4%, CI/CD 25.6%, RAG 23.7%, AWS 23.2%, SQL 17.7%, MLOps 13.5% [B · T0-66 L618–L629]; global direct n=17 adds agents/LangGraph/MCP 35% and evals 18% [C · T0-66 L601–L607]).
  - **Fractional AI Leader** (`T0-66` n=13 [C]): strategy 85%, governance/risk 77%, executive communication 77%, change/training 77%, use-case ROI 69%, prior Head/VP/CTO/C-suite seat 69%, hands-on LLM prototyping 46% [C · T0-66 L582–L592]. Avoid vendor-awarded "Certified AI Consultant / Fractional CAIO" short-course titles (`T0-68 G4`).
- **Contracting:** MSA + SOW; monthly advance billing; an explicit overage rate; no rollover; 30-day notice; IP carve-outs; liability capped at 1× fees [C · T0-18].
- **Client acquisition (ERRATA U47):** contrast Go Fractional's vendor-claimed **92%** referral figure with broader independent-freelancer surveys showing **53–75%** referral share; the model assumes 8–18 first calls a year to sustain two retainers [C/D · T0-18, T0-66].
- **India compliance (not tax advice):** the ₹75 lakh presumptive-tax ceiling, GST and the LUT, purpose codes (P0802; P1006 for advisory work), W-8BEN and FEMA's 9-month realisation rule are in [India remote tax](../09-compensation/india-remote-tax.md) [B · T0-07].
- **Insurance:** tech E&O (~$899/yr) and cyber (~$1,540/yr) [C · T0-18].

---

## 4. Skill × Role Matrices

<a id="41-engineering-roles"></a>
Each role's tier for every skill comes from the ontology: see the [role index](role-skill-inventories.md#1-role-index) and the [cross-role views](role-skill-inventories.md#2-cross-role-views-what-recurs-for-universal-and-family-resumes). The practice-judgement (Grade D) cluster matrices that stood here disagreed with the ontology's tiers and were removed; the ontology is the source of truth for role skill tiers (AGENTS.md §2).

---

## 5. Volatile Tool and Credential Registry (status as of November 2026)

Tool and protocol statuses live in the skills ontology and are shown, dated, in the [skills vocabulary watch list](skills-vocabulary.md#5-watch-list-tools-with-a-notable-status); credential statuses are in [credentials by role](../04-certifications/credentials-by-role.md#by-credential), and protocol facts are in [agentic protocols](agentic-protocols.md#at-a-glance).

---

## 6. Suggested Learning Order by Background

Learning order by role family and starting background is in [learning roadmaps](learning-roadmaps.md#adjust-for-your-starting-background), the 60-item rated catalogue is in [learning resources](learning-resources.md), and modelled timelines and the gates G1–G4 are in [career transitions](../11-tracks/career-transitions.md#the-shared-spine-four-gates-and-an-hours-budget).

---
*Role skill maps. [P] items are practice-curated (Grade D) and should be checked against live job descriptions. Tool and protocol statuses are class V2 under EGP-1.0 (90 days), refreshed on 2026-11-19 from RP2 sessions `T0-34`, `T0-48`–`T0-66`, `T0-68` and `T0-69`; next scheduled review by 2027-02-17.*
