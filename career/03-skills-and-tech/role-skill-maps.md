---
id: skills.role-maps
title: "GenAI Role Skills Catalog"
content_type: reference
stage: 3
status: published
last_verified: 2026-11-04
summary: "Narrative skill map for every role: table-stakes, differentiating and frontier skills, tools with their status, proof of work, interview track and typical gaps; the volatile tool and credential registry."
sources: [T0-03, T0-06, T0-13, T0-14, T0-15, T0-16, T1-03]
---
# GenAI Role Skills Catalog
## The Full Skill Stack for Every Canonical GenAI Role: Tiered, Evidence-Tagged, Interview- and Portfolio-Linked

> **Updated:** 2026-11-04 · **Temporal anchor:** October 2026
> **Role universe:** the 29 canonical roles in the [master catalog](../02-roles/role-catalog.md), in the order of the [ranked catalog](../02-roles/role-rankings.md)
> **Skill tiers:** Decision **D-004**, the three-tier competency model (T0-03 §6.4): **Table-stakes** (gets you screened), **Differentiating** (the main pay driver at Tier 2–4 per D-004) and **Frontier** (specialist employers, Tier 4–5)
> **Evidence standard:** EGP-1.0. A skill list is guidance, not a measurement. Measured prevalence carries a grade; everything else is tagged by where it came from (§0).
> **Complete typed inventories:** this file keeps the narrative skill maps. The complete inventory for each role (every concept, method, language, framework, library, model, platform, data store, infrastructure tool, specialised product, protocol, regulation and non-technical skill, each tiered and evidence-tagged) is generated from [data/skills_ontology.json](../../data/skills_ontology.json) into [role-skill-inventories.md](role-skill-inventories.md); [skills-vocabulary.md](skills-vocabulary.md) types every skill.

---

## 0. How to Read This File

| Tag | Meaning | Grade |
|---|---|---|
| **[JD x%]** | Share of live postings for that title that name the skill (JobsPipe job-description measurements, retrieved 2026-11-02) | B |
| **[S09 x%]** | Share of the 3,647-posting S09 corpus (198 companies, 2026-08-05; skews senior/infra) that names the skill ([T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) §6.3) | B |
| **[S]** | Named in research sessions or in real job descriptions cited there | B/C |
| **[P]** | Practice-curated: standard for the role, but **not** evidenced in the corpus. Check it against 10–20 live JDs before investing heavily | D |

**How to use it:**
1. Pick a role from the [ranked catalog](../02-roles/role-rankings.md).
2. Close the **table-stakes** gaps first; these get you through screens.
3. Build **2–3 differentiating** skills into proof of work; these win Tier 2–3 offers.
4. Add **frontier** skills only if you are targeting specialist employers or Tier 4–5.

Three facts from the evidence frame every list below:
- **Evaluation is the most consistent separator, but it is "common, not universal":** evals appear in 19.0% of S09 postings and at 68.2% of companies [T0-03], and in 59.7% of AI-first roles [T0-13].
- **Hiring signals reward practice, not brands.** Named eval frameworks barely register in postings, and framework-syntax mastery is devalued [T0-03 §4.3].
- **Tools churn fast.** Since late 2025: TGI was archived, RAGAS went dormant, AutoGen was superseded and `trtllm-build` was removed (§5). Learn the concepts first and the tools second.

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

- **C1:** pragmatism under ambiguity.
- **C2:** explaining probabilistic trade-offs.
- **C3:** ownership and incident response.
- **C4:** responsible AI.

Prepare four STAR-AI stories. A behavioural "No Hire" is a near-automatic veto at Anthropic and Google [B/C · T1-03].

### 1.3 Proof of work by tier (T2-01 KF9, T0-13)

| Target tier | Portfolio bar |
|---|---|
| T0–T1 | One evaluated end-to-end system over a non-generic corpus: metrics, cost accounting, and a README a stranger can reproduce in under 30 minutes |
| T2–T3 | Two systems with *different failure surfaces*, CI-gated evals, observability and cost-optimisation evidence; at T3, a serving or kernel study plus an upstream PR |
| T4–T5 | A methodology programme with external adopters, published research, industry-visible OSS, evidence at O-1A level |

**Anti-portfolio** (widely treated as low-signal): generic PDF-chat or RAG demos, Streamlit-over-API wrappers, tutorial clones, and toy chatbots without eval metrics [T0-13, FAD §9.1].

**Verifiability ladder (T0-13):**

| Level | Meaning | Example |
|---|---|---|
| V0 | Self-asserted | Screenshot, "achieves 95% accuracy" |
| V1 | Reproducible | One command regenerates the results table; pinned versions; CI run linked |
| V2 | Externally attested | Merged upstream PR; leaderboard row with commit hash; independent reproduction |
| V3 | Operationally evidenced | 30+ days of uptime and spend logs; an incident postmortem; real users |

Every headline README claim should be V1 or higher. Tier 3 portfolios need at least one V2 item; Tier 4 portfolios need V2 as the norm.

**Repository anatomy (T0-13 PA-01 to PA-12):**
- **Front matter:** evidence block (PA-01), `make repro` (PA-02), dataset card (PA-03).
- **Measurement:** eval harness (PA-04), CI gates (PA-05), latency benchmark (PA-06), cost accounting (PA-07), telemetry (PA-08).
- **Engineering hygiene:** abuse resistance (PA-09), architecture and ≥3 ADRs (PA-10), failure analysis (PA-11), AI-use disclosure in `docs/PROCESS.md` (PA-12).

**How T0-13's portfolio rubric weights shift by tier (T0–1 / T2 / T3 / T4):**

| Criterion | T0–1 | T2 | T3 | T4 |
|---|:---:|:---:|:---:|:---:|
| Eval | 20 | 20 | 15 | 15 |
| Perf/cost | 8 | 12 | 20 | 15 |
| Third-party verifiability | 5 | 5 | 10 | 15 |
| Depth/influence | 2 | 3 | 5 | 15 |

---

## 2. What Postings Actually Ask For

### 2.1 JobsPipe job-description measurements (live postings, retrieved 2026-11-02) [B]

| Title | Top skills named (share of postings) | Other signals |
|---|---|---|
| **AI Engineer** | Python 78.4 · LLM 76.7 · agentic AI 59.3 · RAG 54.0 · machine learning 39.8 · AI 37.8 · generative AI 37.6 · Azure 35.1 · AWS 35.1 · CI/CD 34.4 · vector DBs 32.6 · prompt engineering 31.1 | Remote 11.0%; pay disclosed 19.6%; senior 24.6%, entry 7.0% |
| **Machine Learning Engineer** | ML 98.6 · Python 71.3 · PyTorch 48.2 · LLM 45.0 · data structures 33.7 · deep learning 32.6 · TensorFlow 31.8 · communication 30.3 · AI 27.0 · A/B testing 23.5 · NLP 23.3 · C++ 23.3 | Remote 14.0%; pay disclosed 38.5%; entry 13.7%, senior 23.2% |
| **Research Scientist** (all fields) | Python 42.3 · communication 41.3 · ML 39.2 · data structures 26.0 · PyTorch 25.4 · AI 25.1 · LLM 24.4 · creativity 23.0 · deep learning 18.6 · C++ 17.4 · reinforcement learning 17.1 | Remote 3.3%; US 65.0% of postings |
| **Solutions Architect** | AWS 53.6 · leadership 43.0 · communication 42.9 · mentoring 35.1 · Azure 29.5 · adaptability 26.5 · compliance 25.3 · Python 23.6 · AI 23.2 · GCP 22.6 · DevOps 17.2 · generative AI 17.1 | Remote 16.2% |
| **Data Scientist** | data science 90.1 · Python 86.0 · ML 69.3 · SQL 63.8 · statistics 52.7 · communication 42.3 · data analysis 33.1 · LLM 30.1 · AI 27.2 · AWS 24.8 · generative AI 22.0 | Feeder for AI Engineer / Evals |
| **Product Manager** | product management 92.6 · communication 53.7 · leadership 40.1 · compliance 26.1 · time management 24.0 · agile 22.7 · roadmapping 18.4 · AI 15.4 · stakeholder management 14.2 · agentic AI 13.6 | Feeder for AI PM |
| **Software Engineer** | Python 44.4 · communication 44.2 · Java 32.4 · CI/CD 31.3 · AWS 30.8 · system design 28.3 · C++ 24.6 · AI 24.0 | — |
| **Backend Engineer** | communication 40.4 · AWS 39.7 · Python 38.4 · system design 37.0 · Kubernetes 31.2 · PostgreSQL 30.7 · Docker 28.0 · CI/CD 26.8 · observability 25.0 | Remote 31.6% |
| **Full-Stack Engineer** | React 69.4 · TypeScript 52.7 · Python 41.8 · AWS 41.3 · CI/CD 37.8 · Node.js 32.3 · REST API 27.6 | Remote 21.6% |
| **DevOps Engineer** | DevOps 99.0 · CI/CD 81.2 · Kubernetes 69.4 · Terraform 59.1 · Python 55.7 · Docker 53.4 · AWS 52.9 · Linux 45.1 | Feeder for ML Platform / AI Infra |
| **Security Engineer** | Python 45.7 · cybersecurity 42.3 · compliance 39.4 · AWS 38.8 · incident response 32.4 · application security 26.5 · IAM 21.6 | Feeder for AI Security |
| **Engineering Manager** | leadership 72.7 · communication 51.4 · mentoring 47.1 · compliance 30.9 · system design 25.3 · observability 18.0 · agentic AI 14.8 | Feeder for AI EM |

### 2.2 Skill and tool mentions in the S09 corpus (T0-03 §6.3) [B]

Each figure is the share of postings, with the share of companies in brackets. Two caveats: S09 skews senior and infra-heavy, and the three corpora T0-03 compared disagree by up to 5× on some skills. Only the *ordering* "evals > fine-tuning" held across all three.

| Group | Skill (postings % / companies %) |
|---|---|
| Broad engineering | Agents/orchestration 37.0 (80.8) · observability/monitoring 28.5 (77.8) · distributed systems 19.1 (62.1) · evals/benchmarking 19.0 (68.2) · PyTorch 18.0 (54.0) · Kubernetes 15.5 (60.1) |
| Model work | Inference-optimisation concept 14.8 (57.1) · fine-tuning/SFT 13.0 (50.5) · RAG 10.0 (40.4) · prompt engineering 7.5 (38.4) |
| Specialist systems | CUDA/GPU kernels 6.6 (29.3) · MCP 4.3 (28.8) · vLLM 3.9 (19.2) · TensorRT 3.9 (19.2) · LangChain 3.6 (23.2) |
| Smaller | Ray 3.0 · Triton 2.8 · SGLang 2.6 · Temporal 2.3 · LangGraph 2.1 · TensorRT-LLM 2.0 · Grafana 2.9 · Datadog 2.4 · OpenTelemetry 1.3 · Pinecone 0.7 · LangSmith 0.7 · Arize 0.4 |

### 2.3 Agentic and protocol skills (T0-16) [C]

- **MCP's share of the market is small but growing.**
  - Skillenai: 1,747 postings in the 90 days to 2026-10-14 (~0.7% adjusted share), +9.7% vs the prior 4 weeks.
  - API Evangelist: 234 of 343,299 postings (0.068%), at 102 of 984 companies.
- **Role mix of MCP postings:** software engineer 21.0%, AI engineer 9.2%, product manager 8.0%.
- **MCP share by title** (the count in brackets is the number of postings that mention MCP, not the sample size): AI Enablement Engineer 30.2% (16, so n≈53), Frontier Agents Engineer 27.3% (6), AI Application Engineer 20.0% (6), AI Security Specialist 13.0% (3).
- **Frameworks still dominate agent-titled roles:** in Agentic AI Engineer postings LangGraph appears in 35.8%, MCP in 13.8%; in Agent Engineer postings LangChain 42.9%, LangGraph 39.3%.
- **Top co-skills in MCP postings:** Python 849 · TypeScript 476 · RAG 378 · CI/CD 362 · AWS 312 · LLMs 282 · SQL 273 · LangGraph 261 · Claude Code 258 · Kubernetes 254.
- **Protocol-level skills (JSON-RPC, transports, tool-schema authoring) are unmeasured:** no dataset found measures them.

### 2.4 What the market devalues (T0-03 §4.3)

1. **Framework-syntax memorisation.** In a study of 20 deployed systems, 85% ran custom loops [A]. Learn portable state-machine concepts instead.
2. **Loyalty to an eval-platform brand.** The vendors are consolidating: OpenAI bought Promptfoo, ClickHouse bought Langfuse. Learn the methodology.
3. **Legacy static engine compilation.** The static engine-build backend (`trtllm-build`) was removed from TensorRT-LLM v1.3 onward; PyTorch is the sole backend.
4. **Standalone prompt writing.** Without regression tests, evals or cost accounting, it is commoditised. The "prompt engineer" title is 0.35% of LinkedIn AI postings [B].

---

## 3. Skill Maps by Role

Roles appear in ranked-catalog order. Each map gives table-stakes, differentiating and frontier skills, tools with their October 2026 status, human skills, proof of work, the interview track, and typical gaps by background.

<a id="skills-ml-engineer"></a>
### 3.1 Machine Learning Engineer (`ml-engineer`) · Rank #1

*Complete typed inventory, with evidence for every skill: [role_inventories/ml-engineer.md](inventories/ml-engineer.md).*

**Measured:** ML 98.6 · Python 71.3 · PyTorch 48.2 · LLM 45.0 · data structures 33.7 · deep learning 32.6 · TensorFlow 31.8 · A/B testing 23.5 · NLP 23.3 · C++ 23.3 [JD].

- **Table-stakes:**
  - Python and PyTorch [JD].
  - ML fundamentals: supervised learning, loss functions, optimisation, regularisation, metrics [JD].
  - Data structures and algorithms [JD 33.7%].
  - SQL and data wrangling [P].
  - Experiment design and A/B testing [JD 23.5%].
  - Deployment basics: Docker, a REST service, CI [P].
- **Differentiating:**
  - Deep learning and transformers: attention, tokenisation, embeddings [JD].
  - **When *not* to fine-tune.** 70% of production LLM apps use off-the-shelf models [A · T0-03 S31]. Fine-tune or distil only for narrow, stable, high-volume tasks that have a golden set [D · T0-14].
  - Fine-tuning methods: SFT and LoRA [S09 13.0% for fine-tuning; LoRA named in a Baseten JD, S · T0-03]; QLoRA and PEFT [P].
  - Embedding and retrieval models.
  - LLM evals: offline and online metrics, CIs [S].
  - Serving literacy: vLLM/SGLang, batching, quantisation [S].
  - Recsys and ranking for recsys-heavy employers [S · T0-14].
  - Data-centric work: labelling and data quality [P].
- **Frontier:**
  - Distributed training: DDP/FSDP2 sharding, checkpoint and resume logic; memory and throughput arithmetic from the Ultra-Scale Playbook [S · T0-13 D8]; tensor/pipeline parallelism and MoE [S · T0-03 serving JD]; data-parallel wording [P].
  - Distributed post-training and RL infrastructure (verl, OpenRLHF) [S].
  - Custom kernels [S].
- **Tools (Oct 2026):**
  - PyTorch; Hugging Face Transformers/PEFT/TRL [P]; Ray Train/Serve [S09 3.0%]; W&B [S · T0-03 J9]; MLflow [P]; vLLM 0.32 / SGLang 0.5.22; TensorRT-LLM (stable 1.2.1 as of October 2026, v1.4.0rc1 tagged; static engine build removed from v1.3) [S · T0-03].
  - FSDP2/DDP [S · T0-13 D8]; Megatron [S · T0-05, RadixArk JD]; DeepSpeed and SLURM are not named in the sessions [P].
- **Human:** communication [JD 30.3%]; translating model metrics into business impact [P].
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
### 3.2 AI Engineer (`ai-engineer`) · Rank #2

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-engineer.md](inventories/ai-engineer.md).*

**Measured:** Python 78.4 · LLM 76.7 · agentic AI 59.3 · RAG 54.0 · ML 39.8 · generative AI 37.6 · Azure 35.1 · AWS 35.1 · CI/CD 34.4 · vector DBs 32.6 · prompt engineering 31.1 [JD].

- **Table-stakes** [S · T0-03 Tier 1]:
  - Production Python: typing, asyncio, Pydantic.
  - Provider SDKs: OpenAI, Anthropic, Google GenAI.
  - Structured outputs (JSON Schema); tool/function calling; streaming (SSE).
  - Embeddings and vector search; naive RAG.
  - Prompt versioning and few-shot design.
  - Docker and basic cloud on AWS/Azure/GCP [JD 35%].
  - FastAPI/REST; SQL; Git and CI/CD [JD 34.4%].
- **Differentiating** [S · T0-03 Tier 2]:
  - **Evaluation harnesses:**
    - pytest regression in CI.
    - Golden sets: 20–50 seed tasks built from real failures, growing to 100+.
    - LLM-judge calibration with position swaps and Cohen's κ.
    - pass@k and pass^k metrics.
  - **Retrieval quality:**
    - Hybrid search: BM25 + dense vectors + cross-encoder reranking.
    - recall@k and MRR; citation faithfulness; abstention.
    - ACL-aware retrieval.
    - Treat ACL enforcement as a fail-closed, retrieval-time invariant [S · T0-14 A8].
    - Plan embedding-model migrations; they also invalidate semantic caches [C · T0-14].
    - Choose RAG vs long context vs fine-tuning deliberately [A/B · T0-14 T4]:
      - Accuracy drops for facts that sit mid-context.
      - Retrieve when the corpus exceeds the window, changes often or needs per-user ACLs.
      - Fine-tune for style or format, not for facts that change.
  - **Agent reliability:**
    - Durable state (LangGraph or Temporal) with checkpoints.
    - Loop limits and step/token budgets.
    - Idempotent tools; human approval for irreversible actions.
  - **Cost and latency engineering:**
    - Cache-aware prompt layout, stable prefix first. Only 28% of LLM spans on cache-capable models show cached reads, even though 69% of input tokens are system prompts [A · Datadog].
    - Model routing and multi-provider fallback. 60% of LLM errors in Feb 2026 were rate limits [A].
    - TTFT/TPOT budgets.
    - Token economics [A · T0-14]:
      - Cache pricing: reads bill at 0.1× base input (lower on some model tiers); writes at 1.25× (5-minute) or 2× (1-hour).
      - A cache breakpoint placed on changing content causes perpetual misses.
      - Batch APIs are 50% cheaper for up to 24-hour latency, so route evals, backfills and enrichment to batch.
      - Layer caches as prefix → exact → semantic; semantic goes last because of false hits.
  - **Observability:** OpenTelemetry GenAI traces, per-tenant cost attribution.
  - **Security basics:** prompt injection, OWASP LLM Top 10.
  - **Context management:** compaction, just-in-time retrieval [S · T0-14].
- **Frontier (role-relative):**
  - Self-hosting with vLLM/SGLang plus utilisation-aware cost models [S].
  - Structured generation with JSON-schema enforcement (constrained decoding) [S · T0-03 §4.1, T0-14 A13].
  - MCP server/client design to spec revision 2026-07-28 [S · T0-16].
  - Distillation or fine-tuning for narrow tasks [S].
- **Tools (Oct 2026)** [S · T0-03, T0-16]:
  - **Agent frameworks:** LangGraph 1.x, LlamaIndex Workflows, OpenAI Agents SDK (GA 2026-03-23, native Temporal), Claude Agent SDK, Pydantic AI 2.x, Microsoft Agent Framework 1.x, Google ADK 2.x.
  - **Evals:** DeepEval and Promptfoo (OpenAI-owned as of October 2026).
  - **Tracing:** Langfuse, Phoenix, LangSmith and Braintrust are listed interchangeably in JDs.
  - **Storage and gateways:** generic vector DBs (brand names devalued); LiteLLM gateway.
- **Human:** scoping with stakeholders; explaining probabilistic trade-offs; writing failure-mode docs; product sense [S · T0-06 S12].
- **Proof of work:**
  - **T0–T1:** an evaluated system over a real corpus. Include a metrics table (recall@k, rubric correctness, faithfulness), a cost/latency budget, and a reproducible README.
  - **T2–T3:** a second system with a different failure surface (an agent with approvals and budgets), plus CI-gated evals, traces, a load test and a postmortem [S · T0-06, T2-01].
  - **Specialisation option:** a "reliability layer for LLM apps": caching, backoff, budgets, fallbacks, trace replay, eval-regression CI [S · T0-06].
  - **If you host a live demo** [S · T0-13 H1–H12]:
    - Default to replay mode.
    - Use a dedicated key with a hard spend cap.
    - Add per-IP and global rate limits plus a daily budget counter.
    - Cap tokens and set timeouts.
    - Expose no side-effecting tools; keep secrets in a store.
    - Run injection tests in CI.
    - Add a kill switch and a visible budget meter (protects against denial-of-wallet).
- **Interview:** the application track: RAG with ACL enforcement, agent loop control, eval architecture, context management [B/C · T1-03]. Plus the 45-minute design blueprint (5 / 4 / 9 / 16 / 7 / 4 minutes) [S · T0-14].
- **Typical gaps:**
  - Backend: evals (the largest gap), LLM API fluency, retrieval, and Python if coming from Java/Go.
  - Data scientists: production hygiene, serving/ops, DSA and system design.
  - Frontend: evals, retrieval, a service layer.
  - PhDs: production craft and code review [D · T0-06].
- **Avoid:** wrapper-only demos; framework-syntax memorisation; new RAGAS dependencies.

<a id="skills-research-engineer"></a>
### 3.3 Research Engineer / Member of Technical Staff (`research-engineer`) · Rank #3

*Complete typed inventory, with evidence for every skill: [role_inventories/research-engineer.md](inventories/research-engineer.md).*

- **Table-stakes:** Python and PyTorch, including internals [S · Inferact JD]; DSA; Linux; ML fundamentals; experimenting at scale [P].
- **Differentiating:**
  - **Distributed training:** DDP/FSDP2 sharding, checkpoint and resume [S · T0-13 D8]; tensor/pipeline parallelism and MoE [S · T0-03]; Megatron [S · T0-05].
  - **Debugging training runs:** loss spikes and numerics [P].
  - **Post-training:** SFT, preference and RL methods [P; T0-03 lists distributed post-training and RL infrastructure as frontier].
  - **RL and fine-tuning tooling:** RL frameworks verl and OpenRLHF; fine-tuning tools Unsloth and LlamaFactory. All four appear as bonus vLLM integrations in an Inferact *inference* JD [S · T0-03 J8].
  - **Evals at scale; research data pipelines; profiling** [S].
- **Frontier:**
  - Pre-training at scale; custom kernels; accelerator ecosystems (TPU, Trainium) [S · T0-03 J2].
  - Numerics validation: exact vs approximate top-k, FP32 islands [S · Anthropic postmortem].
- **Human:** close collaboration with researchers; research taste [S · T0-06].
- **Proof of work:**
  - Paper re-implementations with rigorous evals [S · T2-01].
  - Compact reimplementations: a nano-vLLM-style engine (continuous batching, paged KV, prefix caching) in 1–2k lines, benchmarked against vLLM; distributed-training smoke tests with DDP/FSDP2 [S · T0-13 D8].
  - OSS contributions to training or serving stacks [S].
  - Fellowship projects; Anthropic Fellows does not require a PhD [B · T0-06].
- **Interview:** a research talk plus coding. Frontier labs add infrastructure research-engineering rounds (KV cache, batching, GPU scheduling); Tier 4 candidates face the full research loop [S · T2-01, T1-03].

<a id="skills-forward-deployed-engineer"></a>
### 3.4 Forward Deployed Engineer (`forward-deployed-engineer`) · Rank #4

*Complete typed inventory, with evidence for every skill: [role_inventories/forward-deployed-engineer.md](inventories/forward-deployed-engineer.md).*

- **Table-stakes:**
  - Production Python and/or TypeScript.
  - APIs and integrations: REST, webhooks, auth.
  - SQL and data pipelines.
  - LLM APIs plus RAG plus tool calling.
  - Docker and cloud deployment [S · T0-06 "coding, GenAI and infrastructure skills"].
- **Differentiating:**
  - **Discovery and scoping with customers**; demos and proofs of concept under time pressure; stakeholder communication [S · T0-06, T2-01].
  - **Enterprise integration:** ACL-enforced retrieval [S · T1-03 AI-FDE prep]; OAuth/OIDC and RBAC [S · T0-16 PTC JD]; SSO and customer data access in private networks [P].
  - **Agent design for customer workflows**; evals tied to customer KPIs [S].
  - **Vertical domain depth:** Databricks splits FDE work by manufacturing, public sector, financial services and retail [S · T0-01].
  - **Security reviews and change management** [P].
- **Frontier:**
  - On-prem or hybrid model deployment (self-hosted serving) [P].
  - Turning field patterns into product requirements [P].
- **Tools:** the AI Engineer stack, plus the customer's data platforms (Databricks is named) [S], cloud AI services (Bedrock, Azure OpenAI, Vertex) [P], and enterprise connectors [P].
- **Human:** customer empathy, executive communication, comfort with ambiguity, and willingness to travel (up to 50% in one JD) [S].
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
### 3.5 Applied AI Engineer (`applied-ai-engineer`) · Rank #5

*Complete typed inventory, with evidence for every skill: [role_inventories/applied-ai-engineer.md](inventories/applied-ai-engineer.md).*

- **Table-stakes:** the full [AI Engineer](#skills-ai-engineer) table-stakes stack.
- **Differentiating:**
  - Customer delivery of LLM applications [S · T0-01 D3].
  - Evals defined per customer use case.
  - Safety in regulated settings: Anthropic's "Beneficial Deployments" team is an example [S].
  - Model-behaviour knowledge and prompting at scale [P].
  - Partner enablement and technical writing [P].
  - The context-retrieval specialisation (a Databricks posting) [S].
- **Frontier:** shaping lab products from field feedback [P].
- **Proof of work:** a customer-facing reference implementation with evals and a published write-up [P]; then the AI Engineer T2–T3 portfolio.
- **Interview:** the application track plus customer scenarios [S · T0-14 Applied-AI loop].

<a id="skills-research-scientist"></a>
### 3.6 Research Scientist (AI/ML) (`research-scientist`) · Rank #6

*Complete typed inventory, with evidence for every skill: [role_inventories/research-scientist.md](inventories/research-scientist.md).*

**Measured (all-field research-scientist postings):** Python 42.3 · communication 41.3 · ML 39.2 · PyTorch 25.4 · LLM 24.4 · creativity 23.0 · deep learning 18.6 · C++ 17.4 · reinforcement learning 17.1 [JD].

- **Table-stakes:** deep ML theory and maths (optimisation, probability, linear algebra); Python/PyTorch; experiment design; scientific writing [P/JD].
- **Differentiating:**
  - Research taste and novel method development [S · T0-06].
  - A publication record [S].
  - Reinforcement learning [JD 17.1%] and LLM research [JD 24.4%].
  - Communication [JD 41.3%].
- **Frontier:** field-defining work; leading research agendas [S · T0-17 Tier 5].
- **Proof of work:** papers, open research code, talks [S].
- **Interview:** a research talk, deep technical discussion and coding. Offers are "not plannable" [D · T0-06].

<a id="skills-applied-scientist"></a>
### 3.7 Applied Scientist (`applied-scientist`) · Rank #7

*Complete typed inventory, with evidence for every skill: [role_inventories/applied-scientist.md](inventories/applied-scientist.md).*

- **Table-stakes:** ML and statistics depth; Python and PyTorch; experiment design; coding and DSA for big-company loops [S · T0-06]; SQL [P].
- **Differentiating:**
  - **Research-to-production translation:** turning a method into a tested service [S · T0-06].
  - **Evaluation statistics:** confidence intervals, power analysis, judge-bias tests, drift detection [S · T0-06].
  - **Baseline-first discipline** and one-page decision memos [S].
  - **Causal inference and A/B testing** [P].
  - **LLM fine-tuning and alignment basics** [S09 13.0%].
  - **Reading papers and adapting them** to product constraints [P].
- **Frontier:** novel methods, publications and patents [P].
- **Human:** framing impact for business stakeholders; scoping [S · T0-06].
- **Proof of work:**
  - Your own method turned into a service with tests and CI.
  - At least three code reviews via OSS pull requests.
  - An eval-statistics write-up [S · T0-06].
- **Interview:** ML design is usually a strength for PhDs; coding is the usual gap. Some loops include a research talk [S · T2-01].

<a id="skills-ai-infrastructure-engineer"></a>
### 3.8 AI Infrastructure / GPU Platform Engineer (`ai-infrastructure-engineer`) · Rank #8

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-infrastructure-engineer.md](inventories/ai-infrastructure-engineer.md).*

- **Table-stakes:** Linux; Kubernetes; networking; IaC (Terraform); Python or Go; observability; SRE and on-call practice [JD for DevOps/SRE feeders].
- **Differentiating:**
  - **GPU fleet operations:** H100/H200/B200; reserved vs spot capacity; tensor-parallel groups [S · T0-14].
  - **GPU scheduling and allocation ledgers** (archetype A4); weight distribution and canary rollouts (A5) [S · T0-14].
  - **Distributed-systems depth**, the minimum in top-band JDs [S · T0-03 J1].
  - **Cluster interconnect basics:** NCCL / RDMA / InfiniBand [S].
  - **Checkpoint and storage throughput; failure recovery** [P].
  - **Reliability under hardware faults:** silent data corruption (Anthropic's postmortem describes TPU silent corruption) [S · T0-03].
  - **Capacity planning and GPU cost governance** [S].
- **Frontier:**
  - Multi-node interconnect optimisation [S].
  - Disaggregated serving fleets [S].
  - Mixed accelerator estates (CUDA, TPU, Trainium) [S · T0-03 J2].
  - Hardware CI with canary, shadow and rollback [S].
- **Tools:**
  - **Cluster and serving:** Kubernetes GPU scheduling; Ray [S09 3.0%]; Dynamo [S].
  - **Monitoring:** Prometheus/Grafana [S].
  - **Not named in the sessions:** SLURM, Lustre/WEKA [P].
- **Proof of work:** a self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem [S · T0-03].
- **Interview:** the infrastructure track. Anthropic prompts include GPU cluster design and mixed GPU allocation; strong infrastructure candidates without ML experience do well [B · T0-14].
- **Entry routes:** a paid residency: RadixArk AI Infra Resident, listed at $200K, SGLang experience not required. Caveats: the Accel listing showed "Posted 6+ months ago" and the Greenhouse copy lists no salary [B · T0-05].

<a id="skills-inference-engineer"></a>
### 3.9 Inference / LLM Serving Engineer (`inference-engineer`) · Rank #9

*Complete typed inventory, with evidence for every skill: [role_inventories/inference-engineer.md](inventories/inference-engineer.md).*

- **Table-stakes** [S · T0-03 J1–J8]:
  - Python plus C++ (or Rust).
  - Distributed-systems fundamentals [S]; Linux [P].
  - GPU basics: compute-bound prefill vs memory-bandwidth-bound decode [S · T0-03 §6.10]; HBM capacity and bandwidth [S · T0-14 §6.6]; SRAM/memory hierarchy [P].
  - PyTorch internals; Kubernetes.
- **Differentiating** [S · T0-03, T0-14]:
  - **Serving engines:** vLLM is the default; SGLang suits prefix-heavy and agentic workloads; TensorRT-LLM is NVIDIA-only.
  - **Batching and memory:** continuous batching, PagedAttention / KV-cache management, chunked prefill, prefix caching.
  - **Speculative decoding:** lossless; best for inter-token latency at low-to-medium QPS in memory-bound workloads; measure acceptance rate and goodput before enabling by default [A · T0-14]. T0-03 gives α < 0.6 as an example of where drafting overhead can cause a net regression; the threshold depends on draft cost, length and load.
  - **Quantisation:** FP8/FP4, AWQ, GPTQ, INT4/W4A16.
  - **Parallelism:** tensor and pipeline parallelism; MoE serving.
  - **Latency budgeting:**
    - Track TTFT, ITL/TPOT, goodput, p95 and p99.
    - `E2E = TTFT + (N_out − 1) × ITL`.
  - **KV-cache memory math:**
    - Bytes per token = `2 × L × H_kv × d_head × bytes`.
    - Llama-3.1-70B ≈ 320 KiB/token at BF16 [S · T0-14 F4] (T0-03 §6.10 mislabels this value as FP8; FP8 is half).
  - **Profiling:** roofline analysis with Nsight Systems and the PyTorch Profiler.
  - **Load testing:** `vllm bench serve`, AIPerf.
  - **Fleet control:** autoscaling on queue depth and KV utilisation; admission control; prefix-aware routing.
  - **Utilisation-aware cost models:** the GEICO study found a 2.5–24× cost penalty at 1–10 req/s on H100s.
- **Frontier** [S · T0-03 Tier 3]:
  - Engine internals: scheduler, KVBM.
  - Prefill/decode disaggregation: NVIDIA Dynamo, llm-d.
  - Custom kernels: Triton, CUDA, CUTLASS, tile DSLs.
  - Interconnect: NCCL / RDMA.
  - Numerics validation; multi-LoRA serving.
- **Security:** patch serving-engine CVEs promptly [A/B · T0-03]:
  - SGLang CVE-2026-5760 (GGUF template RCE).
  - vLLM CVE-2026-22778 (weight-loader RCE) and CVE-2026-27893 (`trust_remote_code`).
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
### 3.10 AI Product Manager (`ai-product-manager`) · Rank #10

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-product-manager.md](inventories/ai-product-manager.md).*

**Measured (PM postings):** product management 92.6 · communication 53.7 · leadership 40.1 · compliance 26.1 · agile 22.7 · roadmapping 18.4 · AI 15.4 · stakeholder management 14.2 · agentic AI 13.6 [JD].

- **Table-stakes:** PM fundamentals (discovery, prioritisation, roadmaps); metrics; stakeholder management [JD].
- **Differentiating:**
  - **AI literacy** [S · T0-06]: tokens, context windows, hallucination, RAG vs fine-tuning vs prompting, latency and cost.
  - **Eval fluency:** rubrics, golden sets, inter-rater agreement, the limits of LLM judges [S].
  - **Success metrics for non-deterministic systems**, and how to report them [S · T2-01].
  - **Token and unit economics** [S].
  - **Pilot execution and adoption measurement** [S].
  - **Risk and governance documentation** [S].
  - **Notebook-level SQL and Python** [S · T0-06]; hands-on prompting in a console or playground [S · T2-01].
  - **Human-in-the-loop design** [P].
- **Frontier:** platform and agent product strategy; MCP/AI control-plane products (e.g., Workato's Senior PM, Enterprise MCP posting) [S · T0-16].
- **Proof of work:**
  - A PRD plus eval rubric plus pilot metrics [S · T0-06].
  - A domain rubric with 50+ labelled cases.
  - "10 failure modes ranked by business impact" [S · T2-01].
- **Interview:** scoping and product sense rounds [S · T2-01].
- **Entry fee:** 4+ years as a PM plus at least one shipped model-powered feature [D · T0-06].

<a id="skills-ml-platform-engineer"></a>
### 3.11 ML Platform / MLOps Engineer (`ml-platform-engineer`) · Rank #11

*Complete typed inventory, with evidence for every skill: [role_inventories/ml-platform-engineer.md](inventories/ml-platform-engineer.md).*

- **Table-stakes:** Kubernetes [JD 69.4% of DevOps]; Terraform [JD 59.1%]; CI/CD [JD 81.2%]; Docker; Python; a major cloud; monitoring [JD].
- **Differentiating:**
  - **Model serving on Kubernetes:** vLLM/SGLang, KServe, Ray Serve, NVIDIA Dynamo / Dynamo Triton [S · T0-03 §4.1].
  - **LLM gateways** (archetype A6) [S · T0-14]: per-team budgets, PII redaction, routing, cache layers, usage ledgers.
  - **MCP gateways and tool registries** [S · T0-16]:
    - Identity: OAuth/OIDC/JWT, RBAC, identity propagation.
    - Governance: approvals, server tiering, drift detection.
  - **Observability:**
    - Prometheus/Grafana for TTFT, TPOT and KV saturation; per-tenant cost attribution.
    - OpenTelemetry: the GenAI semantic conventions are still in *Development*, so keep them behind adapters [S · T0-03].
  - **Lifecycle:** CI/CD for models and prompts; model and prompt registries [S].
  - **Supply chain:** model provenance, SBOMs, CVE patching [S].
  - **Operations:** SLOs, error budgets, cost governance [S · T0-14].
- **Frontier:** multi-LoRA serving, prefill/decode disaggregation, GPU autoscaling, supply-chain hardening [S · T0-03].
- **Tools (Oct 2026):**
  - **Serving and gateways:** KServe, Ray, LiteLLM, Azure APIM MCP, Foundry AI Gateway, AgentCore Gateway, agentgateway, Cloudflare MCP server portals [S].
  - **Observability:** Langfuse (ClickHouse-owned as of October 2026), Phoenix (ELv2 licence), Prometheus/Grafana/Datadog [S].
  - **Experiment tracking:** MLflow / W&B [P].
- **Proof of work:** a self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, dynamic LoRA routing and Grafana dashboards [S · T0-03].
- **Interview:** the infrastructure track plus platform design questions: gateway, playground, model distribution [S · T0-14].

<a id="skills-agentic-ai-engineer"></a>
### 3.12 Agentic AI Engineer (`agentic-ai-engineer`) · Rank #12

*Complete typed inventory, with evidence for every skill: [role_inventories/agentic-ai-engineer.md](inventories/agentic-ai-engineer.md).*

**Measured:** LangGraph is named in 35.8% of Agentic AI Engineer postings vs MCP in 13.8%; Agent Engineer postings name LangChain 42.9% and LangGraph 39.3% [C · T0-16].

- **Table-stakes:** tool/function calling with JSON-schema tools; state-machine basics; prompt and context design; Python [S].
- **Differentiating** [S · T0-03, T0-14 A11, T0-16]:
  - **Durable execution:** checkpoints, retries with jitter, idempotency keys, compensation where possible.
  - **Human approval** for irreversible actions.
  - **Budgets:** step, token and time limits; loop detection.
  - **Tool routers** with schema validation and authorisation.
  - **Sandboxes:** containers or microVMs with an egress policy.
  - **Replay and reliability:** append-only event logs and deterministic replay; pass^k reliability evals.
  - **Design choices:** workflow vs agent, and single vs multi-agent.
  - **Context handling:** compaction and just-in-time retrieval.
- **Protocols** [S · T0-16]:
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
### 3.13 AI / GenAI Solutions Architect (`ai-solutions-architect`) · Rank #13

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-solutions-architect.md](inventories/ai-solutions-architect.md).*

**Measured (all Solutions Architect postings):** AWS 53.6 · leadership 43.0 · communication 42.9 · mentoring 35.1 · Azure 29.5 · compliance 25.3 · Python 23.6 · AI 23.2 · GCP 22.6 · generative AI 17.1 [JD].

- **Table-stakes:** cloud architecture on AWS/Azure/GCP [JD]; networking and security basics; Python [JD 23.6%]; communication and leadership [JD].
- **Differentiating:**
  - Reference architectures for RAG and agents on managed services (Bedrock, Azure OpenAI, Vertex) [P; Amazon GenAI SA posting S].
  - Model routing and multi-model strategy. Over 70% of organisations use 3+ models [A · Datadog]; learned routing preserved about 95% of GPT-4 quality at 35–85% lower cost, depending on the benchmark [A · T0-14 T1].
  - Data governance and compliance architecture [JD 25.3%].
  - Cost modelling, including the self-host vs managed-API decision [S · T0-03].
  - Gateway and identity patterns [S · T0-16].
  - Pre-sales: demos and proposals [P].
- **Frontier:** enterprise AI platform strategy; multi-cloud AI governance [P].
- **Credentials:** a tie-breaker only in IT services, staffing and partner firms:
  - Current options: AIP-C01 (AWS Generative AI Developer – Professional), PMLE (Google), AI-103 (Azure AI Apps and Agents Developer Associate).
  - No certification is verified in more than 10% of GenAI JDs [B · T0-11].
- **Proof of work:** a reference architecture with a cost model and a working infrastructure-as-code deployment [P].

<a id="skills-ai-evaluation-engineer"></a>
### 3.14 AI Evaluation Engineer (`ai-evaluation-engineer`) · Rank #14

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-evaluation-engineer.md](inventories/ai-evaluation-engineer.md).*

**Measured:** evals/benchmarking appears in 19.0% of S09 postings and at 68.2% of companies [S09], and in 59.7% of AI-first roles [T0-13]. Only 52.4% of agent teams run offline evals and 37.3% online evals [B/C · LangChain survey].

- **Table-stakes:** Python; pytest; statistics fundamentals; data handling; LLM APIs [S].
- **Differentiating** [S · T0-03, T0-13, T0-14]:
  - **Eval design:** separate capability and regression suites; 20–50 seed tasks drawn from real failures; golden sets with adjudication rules.
  - **Graders, code-based first:**
    - Code checks wherever possible.
    - Model graders calibrated against ~50 passing and ~50 failing human labels (TPR/TNR).
    - Human graders where needed.
  - **Judge calibration:**
    - Position swaps; checks for verbosity, self-preference and anchoring bias.
    - Cohen's κ: raw agreement overstates quality by **33–41 points** [A/B].
  - **Statistics:** pass@k vs pass^k; confidence intervals and power analysis; contamination and saturation checks.
  - **Component evals:** recall@k, MRR, faithfulness, tool accuracy, router accuracy, cache false-hit rate, guardrail precision/recall.
  - **Online evals:** sampling, A/B tests, and an incident → golden-set loop.
  - **Error analysis:** taxonomies from ≥100 reviewed traces.
  - **Operations:** CI regression gates, judge-version pinning, flaky-task detection.
  - **Test the eval itself:** one reported benchmark score moved from 42% to 95% after grader bugs were fixed [A · T0-14 §6.7].
    - Give model judges an "Unknown" option and one dimension each.
    - Grade outcomes, not exact tool-call paths.
    - Run each trial in a clean, isolated environment.
- **Frontier:** benchmark construction; safety and capability evals; methodology programmes with external adopters [S · T0-13 R4].
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
### 3.15 GPU Kernel / ML Compiler Engineer (`gpu-kernel-engineer`) · Rank #15

*Complete typed inventory, with evidence for every skill: [role_inventories/gpu-kernel-engineer.md](inventories/gpu-kernel-engineer.md).*

- **Table-stakes:** C++; the CUDA programming model; GPU architecture (SMs, warps, memory hierarchy, tensor cores); linear algebra; profiling [S · T0-03 J3/J4].
- **Differentiating:**
  - **Kernel languages:** Triton, CUTLASS/CuTe [S].
  - **Core kernels:** fused attention; GEMM tuning; quantised kernels (FP8/FP4/INT4) [S].
  - **Memory performance:** coalescing, bank conflicts, occupancy [P].
  - **Analysis:** roofline (ridge ≈ 300 FLOP/byte on an H100 at BF16 dense, a calculated figure) [S · T0-14]; Nsight Systems [S · T0-03]; Nsight Compute [P].
  - **Numerics validation** [S].
  - **Compiler stacks:** XLA, the Triton compiler, TorchInductor, NeuronX [S · T0-03 J2].
- **Frontier:**
  - **Tile DSLs:** CUDA Tile IR, Helion, CuteDSL. With these DSLs, fused attention can be written in about 60 lines of Python on B200 (2026) [S · T0-03].
  - **Other platforms:** AMD ROCm [S · T0-05]; HIP [P].
  - **New hardware and collectives:** new-architecture bring-up; custom collectives [P].
- **Watch:** DSLs and automated kernel agents are abstracting raw kernel writing. Pair kernel skills with system-level judgement [S · T0-03].
- **Proof of work:**
  - GPU MODE leaderboard submissions (teams of up to 3) [S · T0-12]; AMD × GPU MODE kernel competitions run on organiser hardware [S · T0-13 M4].
  - Kernel PRs to vLLM, SGLang, FlashInfer or Triton, benchmarked on the target hardware and with correctness tests [S · T0-05, T0-13].
- **Interview:** kernel and system internals. Reported AMD kernel interviews overlap with GPU MODE material [C/D · T0-12].

<a id="skills-ai-governance-lead"></a>
### 3.16 AI Governance Programme Lead / Manager (`ai-governance-lead`) · Rank #16

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-governance-lead.md](inventories/ai-governance-lead.md).*

**Measured (Axial, US AI-governance postings) [C]:** Python 27.1% · observability/monitoring 42.3% · OneTrust 8.7–9.2% · Azure 11.1% · AIGP 8.9% (CISSP 10.4%, CIPP 8.2%, CISA 5.9%).

- **Table-stakes:** about 5 years in GRC, privacy, audit or security; risk assessment methods; policy writing; running committees; stakeholder management [S · T0-15].
- **Differentiating:**
  - **EU AI Act literacy** [A · T0-15]:
    - Timeline: GPAI duties since 2 Aug 2025; Annex III high-risk duties from 2 Dec 2027; Annex I from 2 Aug 2028.
    - Annex VI internal-control route for Annex III points 2–8.
    - Art. 101 fines up to EUR 15m or 3%.
  - **Other frameworks:** NIST AI RMF (voluntary, under revision); ISO/IEC 42001 (gives no Art. 40 presumption of conformity) [A/B].
  - **Sector rules:**
    - US: SR 26-2 (model risk; excludes GenAI and agentic AI), NYC LL144, OMB M-25-21.
    - EU: EIOPA.
    - India: RBI FREE-AI; DPDP (main obligations from 13 May 2027) [B].
    - **Transparency and provenance** [A/B · T0-15]:
      - EU AI Act Art. 50 duties apply from 2 Aug 2026 (machine-readable marking of synthetic content). 2 Dec 2026 only ends the grace period for older generative systems.
      - The voluntary transparency Code (final 10 Jun 2026, ~190 signatories) asks for at least two marking layers and does not name C2PA.
      - India's IT Rules amendment on synthetic content took effect 20 Feb 2026: permanent metadata or provenance markers, and 3-hour takedowns.
    - **US state and sector drivers:**
      - The NAIC bulletin covers 29 jurisdictions.
      - Colorado SB 24-205 never took effect; SB26-189 (notice, disclosure and human review) applies from 1 Jan 2027 [B · T0-15].
  - **Programme operations:** the AI inventory/registry, approvals before go-live, vendor risk, monitoring dashboards [S].
  - **Technical literacy:** observability and Python basics [C].
- **Credentials:** domain certifications first (CIPP/CIPM, CISSP/CISA/CRISC); AIGP optional ($649 for IAPP members, $799 otherwise) [B · T0-15].
- **Tools:**
  - Seen in postings: OneTrust; IBM OpenPages (one analyst JD) [S].
  - Not named in Axial's lists or the 13 JDs: Credo AI and Holistic AI [S].
- **Proof of work:** an AI inventory, risk register and governance playbook mapped to the EU AI Act, NIST and ISO 42001 [S · T0-06 non-technical lane].

<a id="skills-physical-ai-engineer"></a>
### 3.17 Physical AI / Robotics AI Engineer (`physical-ai-engineer`) · Rank #17

*Complete typed inventory, with evidence for every skill: [role_inventories/physical-ai-engineer.md](inventories/physical-ai-engineer.md).*

*The corpus has no skill measurements for this role; everything below is [P]. Check it against current postings such as Figure AI's "Helix AI Engineer".*

- **Table-stakes:** robotics fundamentals (kinematics, dynamics, control); C++ and Python; perception (computer vision); simulation; ROS-style middleware.
- **Differentiating:** robot learning (imitation learning, RL); vision-language-action models; sim-to-real transfer; real-time inference on edge hardware; teleoperation data pipelines; safety cases.
- **Proof of work:** a sim-to-real or manipulation project with measured success rates and failure analysis.

<a id="skills-ai-safety-researcher"></a>
### 3.18 Frontier AI Safety / Alignment Researcher (`ai-safety-researcher`) · Rank #18

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-safety-researcher.md](inventories/ai-safety-researcher.md).*

- **Table-stakes:** strong ML research foundations; Python/PyTorch; experiment design [P].
- **Differentiating:**
  - Dangerous-capability and safety evals; adversarial testing; red-teaming [S · EU AI Act Art. 55 duties, T0-15].
  - Alignment methods: preference learning, scalable oversight [P].
  - Interpretability, including mechanistic approaches (probing, circuits, sparse dictionary methods) [P; no headcount evidence].
  - Incident analysis [S].
- **Proof of work:** fellowship projects (Anthropic Fellows: about 4 months with stipend and compute; Anthropic reports that >40% of the first cohort later joined it full-time 🏷️, a self-reported figure) [B · T0-06]; published safety research; open eval contributions [P].
- **Market reality:** about 600 technical FTEs worldwide, growing about 21% a year; no pay data [C · T0-15].

<a id="skills-ai-security-engineer"></a>
### 3.19 AI Security Engineer / AI Red Teamer (`ai-security-engineer`) · Rank #19

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-security-engineer.md](inventories/ai-security-engineer.md).*

- **Table-stakes:** application-security fundamentals; threat modelling; Python [JD 45.7%]; cloud IAM [JD 21.6%]; incident response [JD 32.4%].
- **Differentiating** [S · T0-14 §6.8, T0-16 §8, T0-03]:
  - **Frameworks:** OWASP LLM Top 10 and OWASP Agentic Top 10.
  - **Prompt injection, direct and indirect.** Adaptive attacks beat 12 published defences, with >90% success against most of them [A · T0-14].
  - **Tool and agent abuse:** confused deputy, rug pulls, SSRF/RCE/path-traversal CVEs in MCP servers.
  - **MCP authorisation:**
    - Use token exchange / on-behalf-of flows; never pass tokens through.
    - Static secrets are used in 53% of ~5,200 OSS MCP servers, and OAuth in only 8.5% (2025 scan; skews to local/OSS servers; predates the 2026-07-28 spec) [B · T0-16].
  - **Supply chain:** model provenance, `trust_remote_code` hygiene, serving-engine CVEs.
  - **Containment:** output DLP; sandboxing and egress control; kill switches.
  - **Real attack chains pass classifiers.** EchoLeak (CVE-2025-32711) chained bypasses of an injection classifier, link redaction and a CSP to exfiltrate data with no user click [A/B · T0-14].
    - Controls: treat model output as untrusted (OWASP LLM05): schema validation, stripping auto-rendered markdown images and links, sandboxed code, PII and secret filters.
    - Enforce egress through a domain allowlist and proxy.
  - **Assurance:** adaptive red-team evals; logging and SIEM export.
  - **MCP estate hygiene:** shadow-MCP scanning; signed Agent Cards.
  - **Guidance:** NSA and Five Eyes advisories.
- **Frontier:** automated red-teaming systems; model-level attacks (jailbreak research, backdoors) [P].
- **Proof of work:** a red-team suite in CI (custom or Promptfoo) against a working agent, with measured attack-success rates before and after mitigation [S · T0-13 R2]; an MCP security audit [P].
- **Interview:** "design safeguards for an AI system that can take actions on behalf of a user" [S · T0-14 A15].
- **Programme:** Anthropic AI Security Fellow (requires US/UK/Canada work authorisation; >40% of fellows got full-time offers) [A · T0-12].

<a id="skills-ai-enablement-engineer"></a>
### 3.20 AI Enablement Engineer (`ai-enablement-engineer`) · Rank #20

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-enablement-engineer.md](inventories/ai-enablement-engineer.md).*

- **Table-stakes:** internal tooling in Python or TypeScript; LLM APIs; SSO/identity basics [P].
- **Differentiating:**
  - **MCP servers for internal systems.** This title has the highest MCP share of any (30.2%) [C · T0-16].
  - **Internal copilots and agent platforms** [P].
  - **Guardrails:** PII redaction and access controls [S · T0-14 A6].
  - **Adoption metrics:** usage, time saved [S · T0-06].
  - **Change management and training** [S].
  - **Per-team budgets** through a gateway [S].
  - **Coding-agent rollout:** Claude Code appears 258 times among the co-skills of MCP postings [C · T0-16].
- **Proof of work:** an internal pilot with 5–10 colleagues, measuring adoption and time saved, with a runbook and a risk register [S · T0-06].

<a id="skills-ai-product-engineer"></a>
### 3.21 AI Product Engineer (AI Frontend) (`ai-product-engineer`) · Rank #21

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-product-engineer.md](inventories/ai-product-engineer.md).*

**Measured (full-stack postings):** React 69.4 · TypeScript 52.7 · Python 41.8 · AWS 41.3 · CI/CD 37.8 · Node.js 32.3 · REST API 27.6 [JD].

- **Table-stakes:** React/TypeScript; a Node or Python service layer; REST/SSE/WebSocket; auth [JD].
- **Differentiating** [S · T0-06, T2-01]:
  - **Streaming UI:** partial states, cancellation, error states.
  - **Showing agent work:** tool-use visualisation; human-in-the-loop approval UX; citations and provenance; generative UI components.
  - **UX for uncertainty and transparency.**
  - **Agent-UX telemetry:** acceptance rate, edit distance, abandonment, TTFT p50/p95.
  - **Human-in-the-loop evals.**
  - **Libraries and protocols:** Vercel AI SDK 6; AG-UI, MCP Apps, A2UI.
- **Frontier:** on-device and browser inference: WebGPU (in all major browsers), Transformers.js v4, Chrome built-in AI (Prompt API), WebMCP (volatile). Treat these as a differentiator, not a job [S · T0-06, T2-01].
- **Proof of work:**
  - A full-stack app (frontend → API → LLM → eval) with 50 eval cases and UX metrics.
  - An on-device module benchmarked on ≥3 device/browser combinations, with feature detection and a fallback [S · T0-06].
- **Interview:** the application track (agent UX), and AI-enabled coding rounds in the Meta format [S · T2-01].

<a id="skills-ai-risk-assurance-specialist"></a>
### 3.22 AI Risk, Audit & Compliance Specialist (`ai-risk-assurance-specialist`) · Rank #22

*Complete typed inventory, with evidence for every skill: [role_inventories/ai-risk-assurance-specialist.md](inventories/ai-risk-assurance-specialist.md).*

- **Table-stakes:** audit methodology; CISA, CIA or CPA (required for the AAIA credential) [B · T0-15]; model-risk management; privacy law [S].
- **Differentiating:**
  - **Algorithmic bias audits:** NYC LL144 impact-ratio audits (only 18 of 391 employers had posted one) [A/B].
  - **EU-side assurance:** DSA audits; ISO/IEC 42001 audit or implementation; conformity assessment (notified bodies apply by 28 Jan 2028) [S].
  - **Model validation for predictive AI** under SR 26-2 [S].
  - **GenAI risk controls,** which have no settled owner [S].
  - **DPO duties** for India DPDP Significant Data Fiduciaries [S].
- **Proof of work:** a model-validation or bias-audit report on a public model, using documented methodology [P].

<a id="skills-responsible-ai-engineer"></a>
### 3.23 Responsible AI / AI Governance Engineer (`responsible-ai-engineer`) · Rank #23

*Complete typed inventory, with evidence for every skill: [role_inventories/responsible-ai-engineer.md](inventories/responsible-ai-engineer.md).*

- **Table-stakes:** Python; ML/MLOps basics; documentation discipline [S · T0-15].
- **Differentiating** [S · T0-15]:
  - **Guardrails:** prompt-injection detection; red-teaming.
  - **Eval pipelines:** hallucination, groundedness, subgroup fairness; observability.
  - **Turning regulation into engineering controls:** EU AI Act Annex IV documentation and Art. 12 logging; mappings to NIST AI RMF and ISO 42001.
  - **Fairness and explainability tooling:** Fairlearn (0.15.0, Oct 2026), SHAP, LIME, Captum; AIF360 (stale since Apr 2024; pin or fork); model cards [S · T0-15].
  - **Cloud AI governance tooling:** Azure AI, Azure ML, AI Foundry, Microsoft Fabric and Purview (Beacon Hill, Tampa JD) [S · T0-15].
- **Tools:**
  - Named in JDs: NeMo Guardrails, Giskard (v3) and Arize (preferred in the Cognizant JD).
  - Absent from the 13 JDs: Guardrails AI and C2PA (portfolio-only) [S · T0-15].
  - Component maturity [S · T0-15]:
    - c2pa-python 0.38.0 (pre-1.0; pin versions).
    - Guardrails AI 0.11.0 (breaking changes).
    - Giskard v3 (pre-release; no tabular testing).
- **Proof of work:** a compliance packet mapped to NIST AI 600-1 and the OWASP LLM Top 10, with runtime guardrails, subgroup evals, and a calibrated judge on ~100 traces [S · T0-09, T0-15].

<a id="skills-domain-evaluation-specialist"></a>
### 3.24 Domain Evaluation Specialist / AI Trainer (`domain-evaluation-specialist`) · Rank #24

*Complete typed inventory, with evidence for every skill: [role_inventories/domain-evaluation-specialist.md](inventories/domain-evaluation-specialist.md).*

- **Table-stakes:** deep domain expertise (4+ years; MA/JD/MD/PhD for premium rates); clear writing; attention to detail [C · T0-06].
- **Differentiating:**
  - **Evaluation craft:** rubric design; golden-set construction with adjudication rules; inter-rater agreement (Cohen's κ) [S · T0-06].
  - **Benchmarking:** comparing models against today's human process; failure taxonomies [S].
  - **Working tools:** basic spreadsheets/SQL and hands-on prompting [S · T2-01].
- **Proof of work:** a domain gold standard: 100+ real tasks with rubrics, adjudication rules and two-reviewer agreement, comparing 2–3 models against today's human baseline [S · T0-06].
- **Next step:** this is "a bridge, not a destination". Move toward an in-house eval-lead, AI PM or governance role [S · T0-06].

<a id="skills-leadership"></a>
### 3.25 Leadership and independent tracks

*Complete typed inventories, with evidence for every skill: [AI engineering manager](inventories/ai-engineering-manager.md) · [VP / Head of AI and Chief AI Officer](inventories/vp-head-of-ai.md).*

**AI Engineering Manager / Director:**
- **Measured (EM postings):** leadership 72.7 · communication 51.4 · mentoring 47.1 · compliance 30.9 · system design 25.3 · observability 18.0 · agentic AI 14.8 [JD].
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
- **India compliance (not tax advice) [B · T0-07]:**
  - s.58 / old §44ADA presumptive taxation up to ₹75L (cash receipts ≤5%).
  - GST LUT; RBI purpose code P0802 (P1006 for advisory work); W-8BEN.
  - FEMA requires export proceeds to be realised within 9 months.
- **Insurance:** tech E&O (~$899/yr) and cyber (~$1,540/yr) [C · T0-18].

---

## 4. Skill × Role Matrices

Legend: **●●** core (the role is defined by it) · **●** important · **○** useful · blank = rarely needed. Cells are practice judgements (Grade D) that summarise the role maps in §3; check them against live JDs.

### 4.1 Engineering roles

| Skill cluster | AI Eng | Applied AI | Agentic | FDE | MLE | Applied Sci | Inference | Kernel | AI Infra | ML Platform | Evals | AI Security | AI Product Eng | AI Enablement | Physical AI |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Production Python / TypeScript | ●● | ●● | ●● | ●● | ●● | ● | ● | ○ | ● | ●● | ●● | ● | ●● | ●● | ● |
| C++ / Rust / systems languages | | | | | ○ | ○ | ●● | ●● | ● | ○ | | ○ | | | ●● |
| LLM APIs, structured output, tool calling | ●● | ●● | ●● | ●● | ● | ○ | ○ | | | ○ | ● | ● | ●● | ●● | ○ |
| Retrieval / RAG quality | ●● | ●● | ● | ●● | ● | ○ | | | | | ● | ○ | ○ | ● | |
| Evaluation and judge calibration | ●● | ●● | ●● | ● | ● | ●● | ○ | | | ● | ●● | ● | ● | ○ | ● |
| Agent runtimes and reliability | ● | ● | ●● | ● | | | | | | ○ | ● | ● | ● | ● | |
| Observability and cost engineering | ●● | ● | ●● | ● | ○ | | ● | | ● | ●● | ● | ○ | ● | ● | |
| Serving engines, batching, KV cache | ○ | ○ | | ○ | ● | | ●● | ● | ● | ●● | | ○ | | | ○ |
| Quantisation, speculative decoding | | | | | ○ | | ●● | ●● | | ● | | | ○ | | ● |
| GPU kernels and compilers | | | | | | | ● | ●● | ○ | | | | | | |
| Distributed training / post-training | | | | | ● | ● | ○ | ● | ● | ○ | | | | | ● |
| ML and statistics depth | ○ | ○ | | | ●● | ●● | ○ | ○ | | ○ | ●● | | | | ●● |
| Kubernetes, IaC, platform | ○ | ○ | ○ | ● | ○ | | ● | | ●● | ●● | | ○ | | ○ | |
| Gateways, identity, MCP | ○ | ○ | ●● | ● | | | | | ○ | ●● | | ●● | ○ | ●● | |
| AI security (OWASP LLM / Agentic) | ● | ● | ●● | ● | | | ○ | | ○ | ● | ○ | ●● | ○ | ● | |
| Customer scoping and communication | ○ | ●● | ○ | ●● | ○ | ● | | | | ○ | ○ | ○ | ○ | ● | |
| Frontend and agent UX (streaming, HITL approval, citations) | ○ | ○ | ○ | ● | | | | | | | | | ●● | ○ | |
| Robotics, control, simulation, sim-to-real | | | | | ○ | | | | | | | | | | ●● |

### 4.2 Research, product, governance and human-data roles

| Skill cluster | Research Eng | Research Sci | Safety Research | AI PM | Solutions Arch | Governance Lead | Risk & Audit | Responsible AI Eng | Domain Eval |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Production coding | ●● | ● | ● | ○ | ● | | | ●● | |
| ML and statistics depth | ●● | ●● | ●● | ○ | ○ | | ● | ● | |
| Research methods and publishing | ● | ●● | ●● | | | | | | |
| Distributed training / post-training | ●● | ● | ● | | | | | | |
| Evaluation and rubric design | ●● | ● | ●● | ● | ○ | ○ | ● | ●● | ●● |
| Cloud and solution architecture | ○ | | | ○ | ●● | | | ● | |
| Regulation (EU AI Act, NIST, ISO 42001) | | | ● | ○ | ● | ●● | ●● | ●● | |
| Audit and risk methodology | | | | | | ● | ●● | ● | |
| Product sense and metrics | ○ | ○ | | ●● | ● | ○ | | | ○ |
| Stakeholder communication | ● | ● | ● | ●● | ●● | ●● | ● | ● | ● |
| Deep domain expertise | | ● | ● | ● | ● | ● | ● | ○ | ●● |

---

## 5. Volatile Tool and Credential Registry (status as of October 2026)

The tool facts come from T0-03 (PyPI/GitHub checks on 2026-10-23/24), T0-16 and T0-11. They are class V2 (platform and product facts) under EGP-1.0: re-verify within 90 days of 2026-10-23, i.e. by 2027-01-21.

| Item | Status | Implication |
|---|---|---|
| Hugging Face TGI | **Archived 2026-03-21** | Do not use for new deployments |
| Triton Inference Server | Renamed **Dynamo Triton**; NVIDIA **Dynamo** (1.0 GA 2026-03-16; 1.6.0 on 2026-10-22) fronts vLLM, SGLang and TRT-LLM | Update stacks and résumés |
| TensorRT-LLM | Latest stable 1.2.1 (2026-04-20), v1.4.0rc1 tagged; static engine-build backend removed from v1.3 (PyTorch sole backend) | Drop static engine-compilation skills |
| vLLM | 0.32.0 (2026-10-18), pre-1.0; default open serving engine; CVE-2026-22778 (weight-loader RCE), CVE-2026-27893 (`trust_remote_code`, fixed in v0.18.0) | Pin versions; patch quickly |
| SGLang | 0.5.22 (2026-10-16); challenger for prefix-heavy and agentic serving; three critical CVEs in H1 2026: CVE-2026-5760 (GGUF template RCE), CVE-2026-3059/3060 (pickle deserialisation) | Sandbox template parsing; patch quickly |
| RAGAS | **Dormant**: no release since Jan 2026, no commit since Feb 2026 | Avoid new dependencies |
| DeepEval | Active (64 releases a year) | Safe default CI eval runner |
| Promptfoo | Acquired by OpenAI (2026-03-09) | Watch roadmap alignment |
| Langfuse | Acquired by ClickHouse (2026-01-16); MIT core | Still viable |
| Arize Phoenix | Elastic License 2.0 (source-available, not OSI) | Check licence fit |
| Braintrust | Breach 2026-05-04: customers had to rotate provider keys | Keep master keys out of SaaS eval tools |
| AutoGen | **Dormant**; superseded by **Microsoft Agent Framework 1.0** (2026-04-02) | Migrate |
| LangChain / LangGraph | 1.0 released 2025-10-17; legacy chains moved to a classic package | Learn LangGraph concepts, not chain syntax |
| OpenAI Agents SDK | GA 2026-03-23, native Temporal integration | Durable agents |
| MCP | Spec revision **2026-07-28** (stateless core; extensions; OTel trace context) | Re-check auth and transport assumptions |
| A2A | v1.0 (2026-03-12); joining the Linux Foundation AAIF (announced 2026-08-27) | Interop literacy |
| AG-UI | 1.0 (2026-09-18), CopilotKit; not in AAIF | Agent-UX protocol |
| OTel GenAI semantic conventions | Still in *Development* | Isolate behind adapters |
| AWS ML – Specialty certification | **Retired** (last exam 2026-03-31); successor MLA-C01; AIP-C01 (GenAI Developer – Professional) generally available | Update certification plans |
| Azure AI-102 | **Retired 2026-06-30**; replaced by AI-103 (Apps and Agents); DP-100 → AI-300; AZ-204 → AI-200 | AI-103 is still marked beta |
| Google PMLE | Active; refreshed for GenAI | Tie-breaker in GCP shops |

**Model names:** avoid hard-coding a model version as a skill. T0-14 anchors its cost and latency maths to the October 2026 model generation, and at one vendor, model-deprecation notices arrived about every 57 days in 2025–26 (T1-02 KF3).

---

## 6. Suggested Learning Order by Background

These are planning models (T0-06 and T2-01) at 15–20 hours a week. They are Grade D and conditional on success.

| Background | Weeks 1–8 | Months 3–6 | Months 6–9 | Target |
|---|---|---|---|---|
| **Backend / Systems** | LLM API fluency, retrieval, evals (the largest gap), Python if coming from Java/Go | System 1: evaluated RAG/agent with CI evals and traces | System 2 (different failure surface); serving lab | AI Engineer / Applied AI / FDE in ~6 months; infra roles at T3 in 10–14 months |
| **Data Scientist / BI** | Packaging, tests, CI, Docker; then RAG/tools/agents | Eval-and-error-analysis lab; FastAPI service | Judge-calibration study; DSA practice (≥3 weeks) | AI Engineer with an evals edge (DS ~8 months; BI ~11) |
| **Frontend / Full-Stack** | Evals; retrieval; FastAPI or server-side TypeScript | Full-stack app with 50 eval cases and UX metrics | On-device module; agent-UX case study | Full-stack AI Engineer / AI Product Engineer (~7 months) |
| **Non-Technical (5+ yrs domain)** | AI literacy; eval fluency; notebook-level SQL/Python | Domain golden set (100+ tasks) or a pilot with metrics | Governance playbook / PRD + rubric | AI PM, AI ops, domain-eval lead (~7 months) |
| **PhD** | Production Python; serving, batching, cost; eval pipelines | Method → service with tests and CI; ≥3 OSS code reviews | Eval-statistics write-up; fellowship applications | Applied Scientist / Research Engineer (~8 months) |

Milestone gates (T0-06 G1–G4):
- **G1, end of month 3:** a measured v0: ≥50 labelled eval cases, ≥2 baselines, an error taxonomy from ≥100 traces.
- **G2, month 6:** CI evals, a judge validated on ≥100 labels, tracing, ≥1 real user, a postmortem.
- **G3, month 9:** a second system, a public write-up, one external contribution, ≥5 mock interview loops, 15–20 targeted applications.
- **G4, month 12:** an offer, or a written diagnosis of your hiring funnel and a revised plan.

---
*Skills catalog maintained under the Vivechak research governance framework. [P] items are practice-curated (Grade D) and should be checked against live job descriptions. Tool status has a 90-day TTL (EGP class V2); next review by 2027-01-21.*
