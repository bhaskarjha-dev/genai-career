---
id: skills.role-maps
title: "Role Skill Maps"
content_type: reference
stage: 3
status: published
last_verified: 2026-11-04
review_by: 2027-01-19
summary: "Narrative skill map for every role: practice notes from the evidence, tools in use with their October 2026 status, proof of work, interview track, typical gaps and entry routes. Each role's skills and tiers are in its generated inventory."
sources: [T0-03, T0-06, T0-13, T0-14, T0-15, T0-16, T1-03]
---
# Role Skill Maps
## What the Evidence Says About Each Canonical GenAI Role: Practice Notes, Tools, Proof of Work, Interviews and Gaps

> **Updated:** 2026-11-04 · **Temporal anchor:** October 2026
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

Other claims carry an EGP-1.0 grade and their source, for example [A · T0-14]. The JobsPipe posting shares (retrieved 2026-11-02) that the inventories tag [JD x%] are in [posting evidence](role-skill-inventories.md#posting-evidence).

**How to use it:**
1. Pick a role from the [ranked catalog](../02-roles/role-rankings.md) and open its map below.
2. Open the role's inventory for its skills and tiers: close Must gaps first, then build two or three Important skills into proof of work ([role skill inventories §0](role-skill-inventories.md#0-how-to-use-it)).
3. Use the map for what the inventory cannot show: practice notes, the tools in use, the proof of work, the interview track and the typical gaps.

Three facts from the evidence frame every map below:
- **Evaluation is the most consistent separator, but it is "common, not universal":** evals appear in 19.0% of S09 postings and at 68.2% of companies [B · T0-03 §6.3], and in 59.7% of AI-first roles [B · T0-13.F3].
- **Hiring signals reward practice, not brands.** Named eval frameworks barely register in postings, and framework-syntax mastery is devalued [T0-03 §4.3].
- **Tools churn fast.** Since late 2025: TGI was archived, RAGAS went dormant, AutoGen was superseded and `trtllm-build` was removed (the [watch list](skills-vocabulary.md#5-watch-list-tools-with-a-notable-status) has the dates). Learn the concepts first and the tools second.

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

### 1.2 Behavioural competencies every GenAI loop probes (T1-03)

The four competencies (C1–C4), the STAR-AI story bank and the behavioural veto at Anthropic and Google are in [behavioural calibration](../08-interviewing/behavioral-calibration.md) [B/C · T1-03.F4, F5].

### 1.3 Proof of work by tier (T2-01 KF9, T0-13)

The portfolio bar by target level, the verifiability ladder (V0–V3), the fifteen artefacts (PA-01 to PA-15), the anti-portfolio and the rubric weights are in [proof-of-work standards](../05-portfolio/proof-of-work-standards.md#the-verifiability-ladder-and-the-level-model).

---

## 2. What Postings Actually Ask For

### 2.1 JobsPipe job-description measurements (live postings, retrieved 2026-11-02) [B]

The per-title skill shares, remote shares and pay-disclosure shares from this JobsPipe pull are kept in [data/posting_skill_shares.json](../../data/posting_skill_shares.json) and shown in [role skill inventories: posting evidence](role-skill-inventories.md#posting-evidence).

### 2.2 Skill and tool mentions in the S09 corpus (T0-03 §6.3) [B]

S09's posting and company shares are in [T0-03 §6.3](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md#63-skill-and-tool-mention-shares-s09-dataset-audit), and its comparison with two other corpora, which disagree by up to 5× (only "evals > fine-tuning" held in all three), is in [T0-03 §6.1.1](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md#611-corpora-comparison-same-skill-across-three-sampling-frames); the inventories tag each S09 share [S09 x%].

### 2.3 Agentic and protocol skills (T0-16) [C]

MCP's share in each postings index, the frameworks that lead inside agent-titled roles and the skills that co-occur with MCP are in [agentic protocols: how employers ask for it](agentic-protocols.md#how-employers-ask-for-it).

### 2.4 What the market devalues (T0-03 §4.3)

What to stop investing in (framework syntax, loyalty to one eval platform, static TensorRT-LLM engine builds, standalone prompt writing), and what to learn instead, is in the [skills radar](skills-radar.md#4-replace-what-to-stop-investing-in).

---

## 3. Skill Maps by Role

Roles appear in ranked-catalog order. Each map opens with the role's inventory, which lists every skill with its ontology tier and evidence. Below it come practice notes (graded points from the evidence, or a pointer to the page that works them through; they are not tiers), tools in use with their October 2026 status, proof of work, the interview track, and typical gaps or entry routes where the evidence has them.

<a id="skills-ml-engineer"></a>
### 3.1 Machine Learning Engineer (`ml-engineer`) · CCI rank #1

*Skills and tiers: [inventories/ml-engineer.md](inventories/ml-engineer.md). Posting shares for Machine Learning Engineer postings: [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Tools (Oct 2026):**
  - PyTorch; Hugging Face Transformers/PEFT/TRL [P]; Ray Train/Serve [S09 3.0%]; W&B [S · T0-03 J9]; MLflow [P]; vLLM 0.32 / SGLang 0.5.22; TensorRT-LLM (stable 1.2.1 as of October 2026, v1.4.0rc1 tagged; static engine build removed from v1.3) [S · T0-03].
  - FSDP2/DDP [S · T0-13 D8]; Megatron [S · T0-05, RadixArk JD]; DeepSpeed and SLURM are not named in the sessions [P].
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
  - **Cache-aware prompt layout, stable prefix first.** Only 28% of LLM spans on cache-capable models show cached reads, even though 69% of input tokens are system prompts [A · Datadog, T0-03 §6.10].
  - **Model routing and multi-provider fallback.** 60% of LLM errors in Feb 2026 were rate limits [A · Datadog, T0-03 §6.10].
  - **Token economics** (cache pricing, batch discounts, cache layering) and the RAG vs long-context vs fine-tuning decision are worked through in [system-design archetypes](../08-interviewing/system-design-archetypes.md) [A/B · T0-14].
- **Tools (Oct 2026)** [S · T0-03, T0-16]:
  - **Agent frameworks:** LangGraph 1.x, LlamaIndex Workflows, OpenAI Agents SDK (GA 2026-03-23, native Temporal), Claude Agent SDK, Pydantic AI 2.x, Microsoft Agent Framework 1.x, Google ADK 2.x.
  - **Evals:** DeepEval and Promptfoo (OpenAI-owned as of October 2026).
  - **Tracing:** Langfuse, Phoenix, LangSmith and Braintrust are listed interchangeably in JDs.
  - **Storage and gateways:** generic vector DBs (brand names devalued); LiteLLM gateway.
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
- **Avoid:** wrapper-only demos; framework-syntax memorisation; new RAGAS dependencies.

<a id="skills-research-engineer"></a>
### 3.3 Research Engineer / Member of Technical Staff (`research-engineer`) · CCI rank #3

*Skills and tiers: [inventories/research-engineer.md](inventories/research-engineer.md).*

- **Proof of work:**
  - Paper re-implementations with rigorous evals [S · T2-01].
  - Compact reimplementations: a nano-vLLM-style engine (continuous batching, paged KV, prefix caching) in 1–2k lines, benchmarked against vLLM; distributed-training smoke tests with DDP/FSDP2 [S · T0-13 D8].
  - OSS contributions to training or serving stacks [S].
  - Fellowship projects; Anthropic Fellows does not require a PhD [B · T0-06].
- **Interview:** a research talk plus coding. Frontier labs add infrastructure research-engineering rounds (KV cache, batching, GPU scheduling); Tier 4 candidates face the full research loop [S · T2-01, T1-03].

<a id="skills-forward-deployed-engineer"></a>
### 3.4 Forward Deployed Engineer (`forward-deployed-engineer`) · CCI rank #4

*Skills and tiers: [inventories/forward-deployed-engineer.md](inventories/forward-deployed-engineer.md).*

- **Tools:** the AI Engineer stack, plus the customer's data platforms (Databricks is named) [S], cloud AI services (Bedrock, Azure OpenAI, Vertex) [P], and enterprise connectors [P].
- **Proof of work:**
  - A customer pilot case study with numbers [S · T0-06].
  - A demo on a real data source shown to ≥2 potential users [S · T2-01].
  - A deployment write-up that covers failure modes.
- **Interview:** Databricks' AI-FDE loop covers RAG over sensitive, fast-changing documents and evaluating a multi-agent system [C · T0-14]. T1-03 files it under the Application track (RAG with ACL enforcement, agent loop control, eval architecture, context management) [B/C · T1-03]. Prepare a customer-scoping scenario as well [P].
- **Typical gaps:**
  - Backend engineers: customer-facing skills.
  - Frontend engineers: backend and infrastructure.
  - Non-technical candidates: coding plus infrastructure, roughly 10 months of work [D · T2-01].

<a id="skills-applied-ai-engineer"></a>
### 3.5 Applied AI Engineer (`applied-ai-engineer`) · CCI rank #5

*Skills and tiers: [inventories/applied-ai-engineer.md](inventories/applied-ai-engineer.md).*

- **Proof of work:** a customer-facing reference implementation with evals and a published write-up [P]; then the AI Engineer T2–T3 portfolio.
- **Interview:** the application track plus customer scenarios [S · T0-14 Applied-AI loop].

<a id="skills-research-scientist"></a>
### 3.6 Research Scientist (AI/ML) (`research-scientist`) · CCI rank #6

*Skills and tiers: [inventories/research-scientist.md](inventories/research-scientist.md). Posting shares for all-field Research Scientist postings: [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Proof of work:** papers, open research code, talks [S].
- **Interview:** a research talk, deep technical discussion and coding. Offers are "not plannable" [D · T0-06].

<a id="skills-applied-scientist"></a>
### 3.7 Applied Scientist (`applied-scientist`) · CCI rank #7

*Skills and tiers: [inventories/applied-scientist.md](inventories/applied-scientist.md).*

- **Proof of work:**
  - Your own method turned into a service with tests and CI.
  - At least three code reviews via OSS pull requests.
  - An eval-statistics write-up [S · T0-06].
- **Interview:** ML design is usually a strength for PhDs; coding is the usual gap. Some loops include a research talk [S · T2-01].

<a id="skills-ai-infrastructure-engineer"></a>
### 3.8 AI Infrastructure / GPU Platform Engineer (`ai-infrastructure-engineer`) · CCI rank #8

*Skills and tiers: [inventories/ai-infrastructure-engineer.md](inventories/ai-infrastructure-engineer.md). Posting shares for DevOps Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Tools:**
  - **Cluster and serving:** Kubernetes GPU scheduling; Ray [S09 3.0%]; Dynamo [S].
  - **Monitoring:** Prometheus/Grafana [S].
  - **Not named in the sessions:** SLURM, Lustre/WEKA [P].
- **Proof of work:** a self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem [S · T0-03].
- **Interview:** the infrastructure track. Anthropic prompts include GPU cluster design and mixed GPU allocation; strong infrastructure candidates without ML experience do well [B · T0-14].
- **Entry routes:** a paid residency: RadixArk AI Infra Resident, listed at $200K, SGLang experience not required. Caveats: the Accel listing showed "Posted 6+ months ago" and the Greenhouse copy lists no salary [B · T0-05].

<a id="skills-inference-engineer"></a>
### 3.9 Inference / LLM Serving Engineer (`inference-engineer`) · CCI rank #9

*Skills and tiers: [inventories/inference-engineer.md](inventories/inference-engineer.md).*

- **Practice notes:**
  - **Speculative decoding:** measure acceptance rate and goodput before enabling it by default [A · T0-14]. T0-03 gives α < 0.6 as an example of where drafting overhead can cause a net regression; the threshold depends on draft cost, length and load.
  - **KV-cache and latency arithmetic** (bytes per token, the end-to-end latency budget) is in the formula kit of the [system-design archetypes](../08-interviewing/system-design-archetypes.md). Llama-3.1-70B needs about 320 KiB per token at BF16 [S · T0-14 F4]; T0-03 §6.10 mislabels that value as FP8, which is half (erratum U11).
- **Security:** patch serving-engine CVEs promptly [A/B · T0-03]:
  - SGLang had three critical CVEs in H1 2026: CVE-2026-5760 (GGUF template RCE) and CVE-2026-3059/3060 (pickle deserialisation).
  - vLLM CVE-2026-22778 (weight-loader RCE) and CVE-2026-27893 (`trust_remote_code`, fixed in v0.18.0).
  - Parse templates in a sandbox.
- **Tools (Oct 2026):** vLLM 0.32, SGLang 0.5.22, TensorRT-LLM (stable 1.2.1 as of October 2026; static engine build removed from v1.3), NVIDIA Dynamo 1.6.0 (1.0 GA 2026-03-16), Dynamo Triton (the renamed Triton Inference Server), FlashInfer, LMCache, Mooncake, llm-d. **TGI was archived on 2026-03-21; do not use it for new work** [A/B · T0-03].
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

<a id="skills-ai-product-manager"></a>
### 3.10 AI Product Manager (`ai-product-manager`) · CCI rank #10

*Skills and tiers: [inventories/ai-product-manager.md](inventories/ai-product-manager.md). Posting shares for Product Manager postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Proof of work:**
  - A PRD plus eval rubric plus pilot metrics [S · T0-06].
  - A domain rubric with 50+ labelled cases.
  - "10 failure modes ranked by business impact" [S · T2-01].
- **Interview:** scoping and product sense rounds [S · T2-01].
- **Entry fee:** 4+ years as a PM plus at least one shipped model-powered feature [D · T0-06].

<a id="skills-ml-platform-engineer"></a>
### 3.11 ML Platform / MLOps Engineer (`ml-platform-engineer`) · CCI rank #11

*Skills and tiers: [inventories/ml-platform-engineer.md](inventories/ml-platform-engineer.md). Posting shares for DevOps Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Tools (Oct 2026):**
  - **Serving and gateways:** KServe, Ray, LiteLLM, Azure APIM MCP, Foundry AI Gateway, AgentCore Gateway, agentgateway, Cloudflare MCP server portals [S].
  - **Observability:** Langfuse (ClickHouse-owned as of October 2026), Phoenix (ELv2 licence), Prometheus/Grafana/Datadog [S].
  - **Experiment tracking:** MLflow / W&B [P].
- **Proof of work:** a self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, dynamic LoRA routing and Grafana dashboards [S · T0-03].
- **Interview:** the infrastructure track plus platform design questions: gateway, playground, model distribution [S · T0-14].

<a id="skills-agentic-ai-engineer"></a>
### 3.12 Agentic AI Engineer (`agentic-ai-engineer`) · CCI rank #12

*Skills and tiers: [inventories/agentic-ai-engineer.md](inventories/agentic-ai-engineer.md).*

- **Measured:** frameworks are named more often than MCP in agent-titled postings; the shares are in [agentic protocols](agentic-protocols.md#inside-agent-titled-roles-frameworks-lead) [C · T0-16.F10].
- **Protocols** [S · T0-16] (protocol facts are kept in [agentic protocols](agentic-protocols.md)):
  - **MCP, spec revision 2026-07-28:**
    - Stateless core; Client ID Metadata Documents replace dynamic client registration (DCR).
    - Extensions: MCP Apps, Enterprise-Managed Authorization, Tasks.
    - Deprecated: Roots, Sampling, Logging, HTTP+SSE.
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
- **Tools (Oct 2026):**
  - Recommended: LangGraph 1.x, Temporal [S09 2.3%], OpenAI Agents SDK, Claude Agent SDK, Pydantic AI 2.x, Microsoft Agent Framework 1.x, Google ADK 2.x, FastMCP 4.x, langchain-mcp-adapters.
  - **Avoid AutoGen** (dormant). CrewAI is absent from tier-1 lab postings [S · T0-03].
- **Proof of work:** an agent with human approval, sandboxed tools, deterministic trace replay and failure-injection tests (timeouts, malformed arguments, prompt injection), reporting cost per task [S · T0-06].
- **Interview:** agent loop control; tool-gateway design; workflow vs agent trade-offs [S · T1-03, T0-14].

<a id="skills-ai-solutions-architect"></a>
### 3.13 AI / GenAI Solutions Architect (`ai-solutions-architect`) · CCI rank #13

*Skills and tiers: [inventories/ai-solutions-architect.md](inventories/ai-solutions-architect.md). Posting shares for all Solutions Architect postings (adjacent): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Credentials:** a tie-breaker only in IT services, staffing and partner firms:
  - Current options: AIP-C01 (AWS Generative AI Developer – Professional), PMLE (Google), AI-103 (Azure AI Apps and Agents Developer Associate); statuses in [credentials by role](../04-certifications/credentials-by-role.md).
  - No certification is verified in more than 10% of GenAI JDs [B · T0-11].
- **Proof of work:** a reference architecture with a cost model and a working infrastructure-as-code deployment [P].

<a id="skills-ai-evaluation-engineer"></a>
### 3.14 AI Evaluation Engineer (`ai-evaluation-engineer`) · CCI rank #14

*Skills and tiers: [inventories/ai-evaluation-engineer.md](inventories/ai-evaluation-engineer.md).*

**Measured:** evals/benchmarking appears in 19.0% of S09 postings and at 68.2% of companies [S09], and in 59.7% of AI-first roles [T0-13]. Only 52.4% of agent teams run offline evals and 37.3% online evals [B/C · LangChain survey].

- **Tools (Oct 2026):**
  - **Eval frameworks:** DeepEval (active), Promptfoo (OpenAI-owned), TruLens.
  - **Tracing platforms:** LangSmith, Langfuse, Phoenix, Braintrust; JDs treat these as interchangeable.
  - **Avoid new RAGAS dependencies** (dormant since Feb 2026).
  - **Do not store master API keys in SaaS eval platforms** (Braintrust breach, 2026-05-04) [A/B · T0-03].
- **Proof of work:**
  - An eval harness with a κ-calibrated judge validated on ≥100 human labels, plus position and verbosity bias tests.
  - A CI regression threshold and a cost–quality frontier chart [S · T0-06].
- **Interview:** eval design is the most frequent GenAI-engineer question in one aggregate ("Evaluate an LLM System", 19 guides) [C · T0-14]: golden sets, judge calibration, online sampling, A/B tests. T1-03's behavioural questions B11–B12 probe grader design and contamination [B/C · T1-03].
- **Best feeders:** data scientists (error analysis, judge validation), PhDs (measurement rigour), backend engineers (CI, observability) [D · T0-06].

<a id="skills-gpu-kernel-engineer"></a>
### 3.15 GPU Kernel / ML Compiler Engineer (`gpu-kernel-engineer`) · CCI rank #15

*Skills and tiers: [inventories/gpu-kernel-engineer.md](inventories/gpu-kernel-engineer.md).*

- **Watch:** DSLs and automated kernel agents are abstracting raw kernel writing. Pair kernel skills with system-level judgement [S · T0-03].
- **Proof of work:**
  - GPU MODE leaderboard submissions (teams of up to 3) [S · T0-12]; AMD × GPU MODE kernel competitions run on organiser hardware [S · T0-13 M4].
  - Kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware and with correctness tests [S · T0-05, T0-13].
- **Interview:** kernel and system internals. Reported AMD kernel interviews overlap with GPU MODE material [C/D · T0-12].

<a id="skills-ai-governance-lead"></a>
### 3.16 AI Governance Programme Lead / Manager (`ai-governance-lead`) · CCI rank #16

*Skills and tiers: [inventories/ai-governance-lead.md](inventories/ai-governance-lead.md).*

**Measured (Axial, US AI-governance postings) [C]:** Python 27.1% · observability/monitoring 42.3% · OneTrust 8.7–9.2% · Azure 11.1% · AIGP 8.9% (CISSP 10.4%, CIPP 8.2%, CISA 5.9%).

- **Practice notes:**
  - **The regulatory map** (EU AI Act dates and the Annex III internal-control route, US, EU and India sector rules, transparency duties) is laid out against the work in [governance careers](../11-tracks/governance-careers.md) [A/B · T0-15].
  - **Transparency marking:** the voluntary transparency Code (final 10 Jun 2026, ~190 signatories) asks for at least two marking layers and does not name C2PA [A/B · T0-15].
- **Credentials:** domain certifications first (CIPP/CIPM, CISSP/CISA/CRISC); AIGP optional ($649 for IAPP members, $799 otherwise) [B · T0-15].
- **Tools:**
  - Seen in postings: OneTrust; IBM OpenPages (one analyst JD) [S].
  - Not named in Axial's lists or the 13 JDs: Credo AI and Holistic AI [S].
- **Proof of work:** an AI inventory, risk register and governance playbook mapped to the EU AI Act, NIST and ISO 42001 [S · T0-06 non-technical lane].

<a id="skills-physical-ai-engineer"></a>
### 3.17 Physical AI / Robotics AI Engineer (`physical-ai-engineer`) · CCI rank #17

*Skills and tiers: [inventories/physical-ai-engineer.md](inventories/physical-ai-engineer.md).*

*The corpus has no skill measurements for this role, so its inventory is almost entirely practice-curated [P]. Check it against current postings such as Figure AI's "Helix AI Engineer".*

- **Proof of work:** a sim-to-real or manipulation project with measured success rates and failure analysis [P].

<a id="skills-ai-safety-researcher"></a>
### 3.18 Frontier AI Safety / Alignment Researcher (`ai-safety-researcher`) · CCI rank #18

*Skills and tiers: [inventories/ai-safety-researcher.md](inventories/ai-safety-researcher.md).*

- **Proof of work:** fellowship projects (Anthropic Fellows: about 4 months with stipend and compute; Anthropic reports that >40% of the first cohort later joined it full-time 🏷️, a self-reported figure) [B · T0-06]; published safety research; open eval contributions [P].
- **Market reality:** about 600 technical FTEs worldwide, growing about 21% a year; no pay data [C · T0-15].

<a id="skills-ai-security-engineer"></a>
### 3.19 AI Security Engineer / AI Red Teamer (`ai-security-engineer`) · CCI rank #19

*Skills and tiers: [inventories/ai-security-engineer.md](inventories/ai-security-engineer.md). Posting shares for Security Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Proof of work:** a red-team suite in CI (custom or Promptfoo) against a working agent, with measured attack-success rates before and after mitigation [S · T0-13 R2]; an MCP security audit [P].
- **Interview:** "design safeguards for an AI system that can take actions on behalf of a user" [S · T0-14 A15].
- **Programme:** Anthropic AI Security Fellow (requires US/UK/Canada work authorisation; >40% of fellows got full-time offers) [A · T0-12].

<a id="skills-ai-enablement-engineer"></a>
### 3.20 AI Enablement Engineer (`ai-enablement-engineer`) · CCI rank #20

*Skills and tiers: [inventories/ai-enablement-engineer.md](inventories/ai-enablement-engineer.md).*

- **Practice notes:** AI Enablement Engineer has the highest title-level MCP share in T0-16's postings index; the figures are in [agentic protocols](agentic-protocols.md#inside-agent-titled-roles-frameworks-lead) [C · T0-16].
- **Proof of work:** an internal pilot with 5–10 colleagues, measuring adoption and time saved, with a runbook and a risk register [S · T0-06].

<a id="skills-ai-product-engineer"></a>
### 3.21 AI Product Engineer (AI Frontend) (`ai-product-engineer`) · CCI rank #21

*Skills and tiers: [inventories/ai-product-engineer.md](inventories/ai-product-engineer.md). Posting shares for Full-Stack Engineer postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).*

- **Tools (Oct 2026):** Vercel AI SDK 6; AG-UI, MCP Apps and A2UI for agent UI. On-device and browser inference: WebGPU (in all major browsers), Transformers.js v4, Chrome built-in AI (Prompt API), WebMCP (volatile); treat these as a differentiator, not a job [S · T0-06, T2-01].
- **Proof of work:**
  - A full-stack app (frontend → API → LLM → eval) with 50 eval cases and UX metrics.
  - An on-device module benchmarked on ≥3 device/browser combinations, with feature detection and a fallback [S · T0-06].
- **Interview:** the application track (agent UX), and AI-enabled coding rounds in the Meta format [S · T2-01].

<a id="skills-ai-risk-assurance-specialist"></a>
### 3.22 AI Risk, Audit & Compliance Specialist (`ai-risk-assurance-specialist`) · CCI rank #22

*Skills and tiers: [inventories/ai-risk-assurance-specialist.md](inventories/ai-risk-assurance-specialist.md).*

- **Proof of work:** a model-validation or bias-audit report on a public model, using documented methodology [P].

<a id="skills-responsible-ai-engineer"></a>
### 3.23 Responsible AI / AI Governance Engineer (`responsible-ai-engineer`) · CCI rank #23

*Skills and tiers: [inventories/responsible-ai-engineer.md](inventories/responsible-ai-engineer.md).*

- **Tools:**
  - Named in JDs: NeMo Guardrails, Giskard (v3) and Arize (preferred in the Cognizant JD).
  - Fairness and explainability: Fairlearn (0.15.0, Oct 2026), SHAP, LIME, Captum; AIF360 (stale since Apr 2024; pin or fork); model cards [S · T0-15].
  - Cloud AI governance tooling: Azure AI, Azure ML, AI Foundry, Microsoft Fabric and Purview (Beacon Hill, Tampa JD) [S · T0-15].
  - Absent from the 13 JDs: Guardrails AI and C2PA (portfolio-only) [S · T0-15].
  - Component maturity [S · T0-15]:
    - c2pa-python 0.38.0 (pre-1.0; pin versions).
    - Guardrails AI 0.11.0 (breaking changes).
    - Giskard v3 (pre-release; no tabular testing).
- **Proof of work:** a compliance packet mapped to NIST AI 600-1 and the OWASP LLM Top 10, with runtime guardrails, subgroup evals, and a calibrated judge on ~100 traces [S · T0-09, T0-15].

<a id="skills-domain-evaluation-specialist"></a>
### 3.24 Domain Evaluation Specialist / AI Trainer (`domain-evaluation-specialist`) · CCI rank #24

*Skills and tiers: [inventories/domain-evaluation-specialist.md](inventories/domain-evaluation-specialist.md).*

- **Proof of work:** a domain gold standard: 100+ real tasks with rubrics, adjudication rules and two-reviewer agreement, comparing 2–3 models against today's human baseline [S · T0-06].
- **Next step:** this is "a bridge, not a destination". Move toward an in-house eval-lead, AI PM or governance role [S · T0-06].

<a id="skills-leadership"></a>
### 3.25 Leadership and independent tracks

*Skills and tiers: [AI engineering manager](inventories/ai-engineering-manager.md) · [VP / Head of AI and Chief AI Officer](inventories/vp-head-of-ai.md). The Chief AI Officer, fractional and independent tracks have no inventory of their own; see the hubs for [Chief AI Officer](../02-roles/hubs/chief-ai-officer.md), [fractional AI leader](../02-roles/hubs/fractional-ai-leader.md) and [independent AI consultant](../02-roles/hubs/independent-ai-consultant.md).*

**AI Engineering Manager / Director:**
- **Measured:** posting shares for Engineering Manager postings (feeder): [posting evidence](role-skill-inventories.md#posting-evidence).
- **AI-specific skills:**
  - Making eval and observability a shared practice other teams consume (the "Staff scope" in T0-14) [S].
  - Hiring for AI roles; AI roadmaps; GPU and API cost governance; responsible-AI processes [P].
  - Managing the first 90 days: 43% of job seekers in a 2018 Jobvite survey said the role was not what hiring led them to expect, and 63% of organisations lack, or are unsure they have, data-management practices for AI (Gartner) [B/A · T0-09].

**VP / Head of AI and CAIO:**
- AI strategy and portfolio management; build-vs-buy and vendor decisions; budgets; governance boards [P].
- Regulatory accountability, such as US federal CAIO duties under OMB M-25-21 [B · T0-15].
- Operating-model design: about two-thirds of senior leaders prefer hub-and-spoke [C · T0-01 F12].

**Fractional Head of AI / Independent consultant:**
- **Mandate:** own AI strategy, architecture and eval standards, vendor decisions and the hiring plan, with 30/60/90-day deliverables [C · T0-18].
- **Contracting:** MSA + SOW; monthly advance billing; an explicit overage rate; no rollover; 30-day notice; IP carve-outs; liability capped at 1× fees [C · T0-18].
- **Client acquisition:** 92% find clients through networks; the model assumes 8–18 first calls a year to sustain two retainers [C/D · T0-18].
- **India compliance (not tax advice):** the ₹75 lakh presumptive-tax ceiling, GST and the LUT, purpose codes (P0802; P1006 for advisory work), W-8BEN and FEMA's 9-month realisation rule are in [India remote tax](../09-compensation/india-remote-tax.md) [B · T0-07].
- **Insurance:** tech E&O (~$899/yr) and cyber (~$1,540/yr) [C · T0-18].

---

## 4. Skill × Role Matrices

<a id="41-engineering-roles"></a>
Each role's tier for every skill comes from the ontology: see the [role index](role-skill-inventories.md#1-role-index) and the [cross-role views](role-skill-inventories.md#2-cross-role-views-what-recurs-for-universal-and-family-resumes). The practice-judgement (Grade D) cluster matrices that stood here disagreed with the ontology's tiers and were removed; the ontology is the source of truth for role skill tiers (AGENTS.md §2).

---

## 5. Volatile Tool and Credential Registry (status as of October 2026)

Tool and protocol statuses live in the skills ontology and are shown, dated, in the [skills vocabulary watch list](skills-vocabulary.md#5-watch-list-tools-with-a-notable-status); credential statuses are in [credentials by role](../04-certifications/credentials-by-role.md#by-credential), and protocol facts are in [agentic protocols](agentic-protocols.md#at-a-glance).

---

## 6. Suggested Learning Order by Background

Learning order by role family and starting background is in [learning roadmaps](learning-roadmaps.md#adjust-for-your-starting-background); modelled timelines and the gates G1–G4 are in [career transitions](../11-tracks/career-transitions.md#the-shared-spine-four-gates-and-an-hours-budget).

---
*Role skill maps. [P] items are practice-curated (Grade D) and should be checked against live job descriptions. Tool and protocol statuses are class V2 under EGP-1.0 (90 days). The earliest checks quoted here are dated 2026-10-21 (T0-13, T0-14, T0-16), so the next review is due by 2027-01-19.*
