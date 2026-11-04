---
id: skills.vocabulary
title: "GenAI Skills Vocabulary"
content_type: reference
stage: 3
status: published
last_verified: 2026-11-04
summary: "Every skill in the ontology, typed (concept, method, language, framework, tool, platform, non-technical), with posting wording, relations, alternatives, status and corpus mentions."
sources: [T0-03, T0-11, T0-15, T0-16]
generated_by: "scripts/build_skills.py (generated blocks)"
---
# GenAI Skills Vocabulary
## Every Skill in the Ontology: Typed, With Posting Wording, Relations, Status and Corpus Evidence

> **Updated:** 2026-11-04 · **Scope:** Controlled vocabulary of 523 typed skills across 19 categories.
> **Source of truth:** [data/skills_ontology.json](../../data/skills_ontology.json), with its schema in [data/skills_ontology.schema.json](../../data/schemas/skills_ontology.schema.json).
> - Every table between the `BEGIN/END GENERATED` markers is produced by `python3 scripts/build_skills.py --update`, which validates the ontology first.
> - To add or change a skill, edit the ontology, never these tables.
>
> **Companions:**
> - [role-skill-inventories.md](role-skill-inventories.md): the complete typed inventory for each role.
> - [resume-skills-matrix.md](../06-job-search/resume-skills-matrix.md): the concise resume layer (headline skills only).
> - [role-skill-maps.md](role-skill-maps.md): narrative skill maps and the volatile tool registry.
> - [resume-strategy.md](../06-job-search/resume-strategy.md): how the lists feed master, variant and per-posting resumes.

---

## 0. How to Read This File

A resume needs three kinds of skill information:
- exact tool names, for recruiter keyword searches and AI screening;
- concept phrases, for human readers and screening rubrics;
- a proof pattern for each skill, because unbacked claims are discounted [A · T0-04; T0-13].

This vocabulary gives every skill a **type**, its **posting wording** and its **relations**, so that each role inventory can be complete and resume-ready.

**Types.** Each skill has exactly one type:

| Group | Types |
|---|---|
| Technical: knowledge | Concept / knowledge area · Method / practice |
| Technical: concrete | Programming language · Framework / SDK · Library / package · Model / model family · Platform / cloud service · Data store · Infrastructure / DevOps tool · Specialised product · Hardware / accelerator · Protocol / standard · Regulation / framework |
| Non-technical | Communication & collaboration · Behavioural competency · Business & product · Leadership & people · Domain knowledge · Research craft |

Credentials, prerequisites and proof artefacts are kept apart. They are facts and artefacts, not skills (§4 lists the credentials).

**Relations:**
- **Implements (→):** a tool realises a concept (vLLM → LLM serving; pgvector → vector search). On a resume, name the tool *and* the concept.
- **Part of:** a sub-concept sits under a broader one (hybrid search is part of retrieval quality).
- **Choose-one classes:** groups of interchangeable alternatives, such as vector stores or tracing products. Any member satisfies a role link to the class (§2).
- **Posting wording:** aliases that postings use for the same skill. Mirror them only when they are true for you.
- **Status:** the date-stamped state of a volatile tool:
  - the states are active, beta, development, acquired, renamed, dormant, archived and retired;
  - statuses come from the skills catalog's §5 registry and must be re-verified by 2027-01-21;
  - archived, dormant and retired items are always tiered Avoid.
- **Corpus mentions:** how often the 22 research sessions name a concrete technology, by name and alias matching.
  - A few ambiguous names (for example "R") are not counted.
  - Zero means practice-curated: standard in the field, but unmeasured in the research.
- **Roles listing it:** how many role inventories list the skill directly (the number at Must or Important in brackets), plus the roles that cover it only through a choose-one class link.

**Never list a model version as a skill.** Model families appear without version numbers: vendors deprecate models every few months, so the skill is the family and its trade-offs (T0-14; T1-02 KF3).

---

## 1. Summary

<!-- BEGIN GENERATED: scripts/build_skills.py (summary) -->
| Group | Type | Entries | Named in the research corpus | Linked by at least one role | Where it goes on a resume |
|---|---|:---:|:---:|:---:|---|
| Technical: knowledge | [Concept / knowledge area](#type-concept) | 134 | n/a | 134 | Name it in the summary or a core-competencies line; prove it with a bullet that shows the system and a measured outcome |
| Technical: knowledge | [Method / practice](#type-method) | 64 | n/a | 64 | Use it as the verb of a bullet: what you did, on what, with what measured result |
| Technical: concrete | [Programming language](#type-language) | 16 | 12 | 16 | Skills section (Languages); back it with shipped or public code |
| Technical: concrete | [Framework / SDK](#type-framework) | 54 | 45 | 52 | Skills section (Frameworks) in the posting's wording; one bullet showing what you built with it |
| Technical: concrete | [Library / package](#type-library) | 45 | 26 | 45 | Skills section when the posting names it; otherwise inside a bullet |
| Technical: concrete | [Model / model family](#type-model) | 11 | 8 | 11 | Bullets (compared, fine-tuned, served); never a version number |
| Technical: concrete | [Platform / cloud service](#type-platform) | 31 | 22 | 31 | Skills section (Cloud & platforms); match the posting's cloud |
| Technical: concrete | [Data store](#type-data-store) | 14 | 5 | 14 | Skills section (Data); show scale or design choice in a bullet |
| Technical: concrete | [Infrastructure / DevOps tool](#type-infra-tool) | 18 | 14 | 18 | Skills section (Infrastructure); show what you ran and at what scale |
| Technical: concrete | [Specialised product](#type-product) | 38 | 35 | 37 | Skills section (Evaluation, observability, security or governance tools); show the practice, not just the tool |
| Technical: concrete | [Hardware / accelerator](#type-hardware) | 9 | 6 | 9 | Bullets with scale (for example "on 8×H100"), disclosed honestly |
| Technical: concrete | [Protocol / standard](#type-protocol) | 20 | 18 | 20 | Skills section or a bullet showing an integration (for example "MCP server with OAuth") |
| Technical: concrete | [Regulation / framework](#type-regulation) | 18 | 14 | 18 | Skills section for governance, risk and security roles; show an assessment, control or document you produced |
| Non-technical | [Communication & collaboration](#type-communication) | 11 | n/a | 11 | Show, don't list: a bullet with the artefact and its effect ("wrote the design doc adopted by 3 teams") |
| Non-technical | [Behavioural competency](#type-behavioural) | 9 | n/a | 9 | Show in bullets; prepare a STAR-AI story for the interview loop |
| Non-technical | [Business & product](#type-business) | 13 | n/a | 13 | Summary and bullets with business outcomes (cost, revenue, adoption) |
| Non-technical | [Leadership & people](#type-leadership) | 8 | n/a | 8 | Bullets with scope: team size, hires, mentees, decisions owned |
| Non-technical | [Domain knowledge](#type-domain) | 6 | n/a | 6 | Summary line plus bullets with domain outcomes |
| Non-technical | [Research craft](#type-research-craft) | 4 | n/a | 4 | Publications section and bullets (venues, citations, reproductions) |
| **Total** | | **523** | **205 of 274 concrete** | **520** | |
<!-- END GENERATED -->

---

## 2. Choose-One Classes

<!-- BEGIN GENERATED: scripts/build_skills.py (classes) -->
| Class | Members (any one satisfies a choose-1 link) | Note |
|---|---|---|
| **AWS / Azure / GCP** (`cloud`) | Amazon Web Services (AWS), Microsoft Azure, Google Cloud (GCP) | One major cloud (AWS, Azure or GCP) |
| **Managed AI** (`managed_ai`) | Amazon Bedrock, Azure AI Foundry / Azure OpenAI, Google Vertex AI | Managed AI services (Bedrock, Azure OpenAI / AI Foundry, Vertex AI) |
| **KServe / Ray Serve** (`kserve_ray`) | KServe, Ray Serve, BentoML, NVIDIA Dynamo Triton, NVIDIA NIM | Model serving on Kubernetes (KServe, Ray Serve) |
| **vLLM / SGLang / TensorRT-LLM** (`serving_engines`) | vLLM, SGLang, TensorRT-LLM | Serving engines (vLLM, SGLang, TensorRT-LLM) |
| **TPU / Trainium / ROCm** (`accelerators`) | Google TPU, AWS Trainium / Inferentia, AMD ROCm | Accelerator ecosystems (TPU, Trainium, ROCm) |
| **Tile DSLs** (`tile_dsls`) | Helion, CuTe DSL | Tile DSLs (CUDA Tile IR, Helion, CuteDSL) |
| **Agent frameworks** (`agent_frameworks`) | LangGraph, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, Microsoft Agent Framework, Google Agent Development Kit (ADK), LlamaIndex, CrewAI, Mastra | Agent frameworks (LangGraph, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI) |
| **TensorFlow / JAX** (`tensorflow_jax`) | TensorFlow, JAX |  |
| **Fairness & explainability tools** (`fairness_tools`) | Fairlearn, AI Fairness 360, SHAP, LIME, Captum, Microsoft Responsible AI Toolbox | Fairness & explainability tooling (Fairlearn, SHAP, LIME) |
| **Go / Java** (`go_java`) | Go, Java | Go or Java |
| **Vector stores** (`vector_dbs`) | pgvector, Pinecone, Weaviate, Qdrant, Milvus / Zilliz, Chroma, OpenSearch, Elasticsearch | Postings often add "or similar"; one is enough if you can explain the trade-offs |
| **LLM tracing and observability products** (`llm_tracing`) | Langfuse, Arize Phoenix, LangSmith, Braintrust, Helicone, Arize AX, Datadog (incl. LLM Observability) | T0-03 found tracing tools listed interchangeably |
| **Evaluation runners and platforms** (`eval_runners`) | DeepEval, Promptfoo, Inspect (UK AISI), TruLens, Giskard, Braintrust | Named eval frameworks barely register in postings; the practice matters more (T0-03 §4.3) |
| **LLM API providers** (`llm_api_providers`) | OpenAI API platform, Anthropic API, Gemini API (Google AI Studio) | Know at least two; switching cost is part of the design |
| **Frontier model families** (`frontier_models`) | Claude (Anthropic), GPT and o-series (OpenAI), Gemini (Google) | Capabilities, limits and pricing; never a version number |
| **Open-weight model families** (`open_weight_models`) | Llama (Meta), Qwen, Mistral and Mixtral, DeepSeek | For self-hosting, fine-tuning and cost work |
| **Experiment trackers** (`experiment_trackers`) | Weights & Biases (incl. Weave), MLflow | One is enough |
| **LLM gateway tools** (`gateway_tools`) | LiteLLM, Azure API Management (AI gateway), agentgateway, Helicone, Amazon Bedrock AgentCore | Match the employer's cloud |
| **Guardrail tools** (`guardrail_tools`) | NeMo Guardrails, Guardrails AI, Llama Guard | Layered with policy and evals |
| **AI red-teaming tools** (`red_team_tools`) | garak, PyRIT, Promptfoo, Giskard | Tools support, but do not replace, manual adversarial testing |
| **AI governance platforms** (`governance_platforms`) | OneTrust (AI governance), Credo AI, Holistic AI, IBM OpenPages / watsonx.governance | Employer-specific; list only when named |
| **Distributed-training frameworks** (`dist_training_frameworks`) | PyTorch FSDP2, DeepSpeed, Megatron-LM / Megatron Core | FSDP2 is the PyTorch-native default |
| **Post-training frameworks** (`posttraining_frameworks`) | TRL, verl, OpenRLHF, Unsloth, Axolotl, LLaMA-Factory | Choose by method (SFT, preference, RL) and scale |
| **Local inference runtimes** (`local_runtimes`) | llama.cpp, Ollama | Laptop and edge serving |
| **Distributed-inference frameworks** (`distributed_inference`) | NVIDIA Dynamo, llm-d | Disaggregated, KV-aware serving above the engines |
| **Inference benchmarking tools** (`inference_benchmarks`) | GuideLLM, inference-perf, AIPerf / GenAI-Perf | Report the method with the numbers |
| **General load-testing tools** (`load_test_tools`) | Locust, k6 | For API-level load tests |
| **Annotation platforms** (`annotation_platforms`) | Label Studio, Labelbox, Argilla | Employer-specific |
| **Coding-agent tools** (`coding_agent_tools`) | GitHub Copilot, Cursor, Claude Code, OpenAI Codex | Rollout skill matters more than the brand |
| **Python web frameworks** (`py_web_frameworks`) | FastAPI, Flask, Django | FastAPI is the common default for LLM services |
| **Demo UI frameworks** (`demo_ui`) | Streamlit, Gradio | For demos and internal tools |
| **Serverless GPU and inference clouds** (`serverless_gpu`) | Modal, Replicate, Together AI, Fireworks AI, Baseten | Cost-capped experiments and demos |
| **Data platforms and warehouses** (`data_platforms`) | Databricks (incl. Mosaic AI), Snowflake (incl. Cortex), Google BigQuery | Match the employer's stack |
| **Cluster schedulers** (`hpc_schedulers`) | Slurm, Kubernetes | SLURM for HPC-style training; Kubernetes for platform-style |
| **Robot simulators** (`robot_simulators`) | NVIDIA Isaac Sim / Isaac Lab, MuJoCo, Gazebo | Practice-curated |
<!-- END GENERATED -->

---

## 3. Vocabulary by Type

Within each type, rows are sorted by category, then name.

<!-- BEGIN GENERATED: scripts/build_skills.py (vocabulary) -->
<a id="type-concept"></a>
#### Concept / knowledge area (134)

*Technical: knowledge. On a resume: Name it in the summary or a core-competencies line; prove it with a bullet that shows the system and a measured outcome.*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Agent interoperability (tool and agent protocols)** (`agent_interop`) | Agents | agent protocols | part of Agents & tool use | 1 (0 M/I) |
| **Agent memory & state** (`agent_memory`) | Agents | long-term memory; conversation state | part of Agents & tool use | 1 (0 M/I) |
| **Agent reliability (durable state, budgets, approvals)** (`agent_reliability`) | Agents | reliable agents; agent budgets; human approval | part of Agents & tool use | 3 (2 M/I) |
| **Agents & tool use** (`agents`) | Agents | agentic AI; AI agents; tool use; agentic workflows | — | 10 (5 M/I) |
| **Computer-use & browser agents** (`computer_use`) | Agents | browser agents; GUI agents | part of Agents & tool use | 2 (0 M/I) |
| **Durable execution & workflow state** (`durable_execution`) | Agents | checkpointing; resumable workflows | part of Agent reliability (durable state, budgets, approvals) | 2 (1 M/I) |
| **Multi-agent orchestration** (`multi_agent`) | Agents | multi-agent systems; agent orchestration | part of Agents & tool use | 1 (1 M/I) |
| **GenAI reference architectures** (`ref_architecture`) | Cloud & platforms | reference architectures; solution architecture | part of System design | 1 (1 M/I) |
| **Serverless deployment** (`serverless`) | Cloud & platforms | serverless functions; FaaS | — | 2 (0 M/I) |
| **Data governance & lineage** (`data_governance`) | Data engineering | data lineage; data catalogue | — | 3 (0 M/I) |
| **Data pipelines & quality** (`data_pipelines`) | Data engineering | ETL; data engineering; data quality | — | 5 (2 M/I) |
| **LLM evaluation (golden sets, calibrated judges, CI gates)** (`evals`) | Evaluation | LLM evaluation; evals; evaluation harness; golden sets | — | 16 (11 M/I) |
| **Frontend engineering** (`frontend_engineering`) | Frontend & UX | frontend development; web development | — | 1 (1 M/I) |
| **Generative UI** (`generative_ui`) | Frontend & UX | — | part of Streaming & agent UX | 1 (1 M/I) |
| **On-device / WebGPU inference** (`on_device`) | Frontend & UX | on-device AI; in-browser inference | — | 1 (0 M/I) |
| **Streaming & agent UX** (`streaming_ux`) | Frontend & UX | streaming UI; agent UX | — | 1 (1 M/I) |
| **Attention, GEMM & quantised kernels** (`kernel_core`) | GPU & kernels | attention kernels; GEMM; quantised kernels | — | 1 (1 M/I) |
| **CUDA / Triton / CUTLASS** (`cuda_triton`) | GPU & kernels | GPU kernel programming; CUDA kernels; Triton kernels | — | 5 (1 M/I) |
| **GPU fundamentals (HBM, prefill vs decode)** (`gpu_fundamentals`) | GPU & kernels | GPU architecture; HBM; memory bandwidth; prefill vs decode | — | 2 (2 M/I) |
| **GPU memory performance** (`memory_perf`) | GPU & kernels | memory coalescing; shared memory; tensor cores; occupancy | — | 1 (1 M/I) |
| **ML compilers (XLA, TorchInductor)** (`compilers`) | GPU & kernels | ML compilers; graph compilers; kernel fusion | — | 1 (1 M/I) |
| **PTX / SASS-level optimisation** (`ptx_sass`) | GPU & kernels | PTX; SASS | part of Attention, GEMM & quantised kernels | 1 (0 M/I) |
| **Content provenance (EU AI Act Art. 50)** (`provenance`) | Governance, risk & compliance | content provenance; watermarking; AI labelling | — | 3 (1 M/I) |
| **EU AI Act / NIST AI RMF / ISO 42001** (`regulation`) | Governance, risk & compliance | AI regulation; AI standards; AI governance frameworks | — | 5 (4 M/I) |
| **Explainability (XAI)** (`explainability`) | Governance, risk & compliance | XAI; feature attribution | — | 3 (1 M/I) |
| **Fairness & bias assessment** (`bias_fairness`) | Governance, risk & compliance | algorithmic fairness; bias testing | — | 3 (2 M/I) |
| **Model risk management** (`model_risk_mgmt`) | Governance, risk & compliance | MRM; model risk | — | 2 (1 M/I) |
| **Privacy law & DPO duties** (`privacy`) | Governance, risk & compliance | privacy law; data protection; DPIA; DPO | — | 2 (2 M/I) |
| **Sector rules (SR 26-2, LL144, DPDP)** (`sector_rules`) | Governance, risk & compliance | sector AI rules; financial-services AI rules; hiring-AI rules | — | 3 (2 M/I) |
| **Constrained decoding** (`structured_generation`) | Inference & serving | constrained decoding; grammar-constrained generation; guided decoding | — | 3 (0 M/I) |
| **Continuous batching & KV cache** (`batching_kv`) | Inference & serving | continuous batching; KV cache; PagedAttention | part of Serving literacy (vLLM, batching, quantisation) | 2 (1 M/I) |
| **Engine internals & multi-LoRA** (`engine_internals`) | Inference & serving | multi-LoRA serving; scheduler internals | part of Serving literacy (vLLM, batching, quantisation) | 2 (0 M/I) |
| **Inference autoscaling** (`inference_autoscaling`) | Inference & serving | GPU autoscaling; KEDA | part of Serving literacy (vLLM, batching, quantisation) | 3 (1 M/I) |
| **KV-aware routing & load balancing** (`kv_aware_routing`) | Inference & serving | cache-aware routing | part of Prefill/decode disaggregation | 1 (1 M/I) |
| **KV-cache offload & tiering** (`kv_offload`) | Inference & serving | KV-cache offloading | part of Continuous batching & KV cache | 1 (0 M/I) |
| **Prefill/decode disaggregation** (`pd_disagg`) | Inference & serving | disaggregated serving; prefill/decode disaggregation | part of Serving literacy (vLLM, batching, quantisation) | 3 (0 M/I) |
| **Prefix caching & KV reuse** (`prefix_caching`) | Inference & serving | KV-cache reuse; RadixAttention | part of Continuous batching & KV cache | 1 (1 M/I) |
| **Quantisation (FP8/FP4, AWQ, GPTQ)** (`quantization`) | Inference & serving | quantisation; quantization; FP8; INT4; AWQ; GPTQ | — | 4 (2 M/I) |
| **Self-hosting open models** (`self_hosting`) | Inference & serving | open-weight models; self-hosted LLMs; local models | — | 3 (0 M/I) |
| **Serving literacy (vLLM, batching, quantisation)** (`serving_literacy`) | Inference & serving | LLM serving; LLM inference; inference optimisation | — | 1 (1 M/I) |
| **Speculative decoding** (`spec_decoding`) | Inference & serving | speculative decoding; EAGLE; draft models | part of Serving literacy (vLLM, batching, quantisation) | 1 (1 M/I) |
| **TP/PP & MoE serving** (`parallel_serving`) | Inference & serving | tensor-parallel serving; expert parallelism; MoE serving | part of Serving literacy (vLLM, batching, quantisation) | 1 (1 M/I) |
| **DevOps** (`devops`) | Infrastructure & DevOps | DevOps practices | — | 3 (2 M/I) |
| **Capacity & GPU/API cost governance** (`capacity_cost`) | Infrastructure & HPC | capacity planning; FinOps; GPU cost governance | — | 4 (3 M/I) |
| **Checkpointing & storage throughput** (`storage_checkpoint`) | Infrastructure & HPC | checkpointing; distributed storage; I/O throughput | — | 1 (1 M/I) |
| **GPU fleet ops & scheduling** (`gpu_fleet`) | Infrastructure & HPC | GPU cluster operations; cluster scheduling; GPU scheduling | — | 2 (1 M/I) |
| **Hardware-fault reliability** (`hw_reliability`) | Infrastructure & HPC | hardware failures; GPU fault tolerance; silent data corruption | — | 1 (1 M/I) |
| **NCCL / RDMA / InfiniBand** (`interconnect`) | Infrastructure & HPC | collective communication; interconnects | — | 3 (1 M/I) |
| **Networking** (`networking`) | Infrastructure & HPC | TCP/IP; load balancing; VPC; DNS | — | 2 (1 M/I) |
| **Choosing RAG vs long context vs fine-tuning** (`adaptation_choice`) | LLM applications | — | part of LLM fundamentals (tokens, context windows, sampling, hallucination) | 2 (1 M/I) |
| **Context engineering** (`context_engineering`) | LLM applications | context management; context-window management | part of Prompt & context design | 2 (1 M/I) |
| **Generative AI** (`generative_ai`) | LLM applications | GenAI; generative AI | — | 4 (3 M/I) |
| **LLM APIs & tool calling** (`llm_apis`) | LLM applications | LLM; LLM APIs; LLM integration; large language models | — | 10 (10 M/I) |
| **LLM fundamentals (tokens, context windows, sampling, hallucination)** (`llm_fundamentals`) | LLM applications | how LLMs work; tokenisation; sampling | — | 5 (0 M/I) |
| **Model selection & routing** (`model_selection`) | LLM applications | model routing; LLM routing | part of Cost & latency engineering | 2 (1 M/I) |
| **Multimodal AI (vision, documents, audio)** (`multimodal`) | LLM applications | vision-language models; VLMs | — | 3 (0 M/I) |
| **Prompt & context design** (`prompt_context`) | LLM applications | prompt and context design | — | 3 (3 M/I) |
| **Reasoning models & test-time compute** (`reasoning_models`) | LLM applications | thinking models; reasoning effort | part of LLM fundamentals (tokens, context windows, sampling, hallucination) | 1 (0 M/I) |
| **Speech & voice AI (ASR, TTS, realtime voice agents)** (`speech_voice`) | LLM applications | voice agents; ASR; TTS | part of Multimodal AI (vision, documents, audio) | 2 (0 M/I) |
| **Structured output & tool schemas** (`structured_output`) | LLM applications | JSON mode; structured outputs; function schemas | part of LLM APIs & tool calling | 1 (0 M/I) |
| **Tool and function calling** (`tool_calling`) | LLM applications | function calling | part of LLM APIs & tool calling | 3 (1 M/I) |
| **Causal inference** (`causal`) | ML & deep learning | causal inference; uplift modelling; counterfactuals | — | 1 (1 M/I) |
| **Computer vision** (`computer_vision`) | ML & deep learning | CV; image models | — | 2 (1 M/I) |
| **Data science** (`data_science`) | ML & deep learning | — | — | 1 (1 M/I) |
| **Deep learning & transformers** (`deep_learning`) | ML & deep learning | neural networks; transformers; transformer architecture | — | 6 (4 M/I) |
| **Diffusion & image/video generation models** (`diffusion_models`) | ML & deep learning | diffusion models | part of Deep learning & transformers | 1 (0 M/I) |
| **Linear algebra** (`linear_algebra`) | ML & deep learning | matrix calculus; maths for ML | — | 3 (2 M/I) |
| **Mixture of Experts (MoE)** (`moe`) | ML & deep learning | MoE | part of Deep learning & transformers | 1 (0 M/I) |
| **ML fundamentals** (`ml_fundamentals`) | ML & deep learning | machine learning; AI/ML; artificial intelligence; supervised learning | — | 8 (8 M/I) |
| **Natural language processing (NLP)** (`nlp`) | ML & deep learning | NLP | — | 3 (1 M/I) |
| **PyTorch internals** (`pytorch_internals`) | ML & deep learning | autograd internals; PyTorch dispatcher | — | 3 (2 M/I) |
| **Recommender systems** (`recsys`) | ML & deep learning | recommender systems; recommendations; personalisation | — | 2 (0 M/I) |
| **Reinforcement learning** (`rl`) | ML & deep learning | reinforcement learning; RL; policy optimisation | — | 4 (1 M/I) |
| **Search & ranking (learning to rank)** (`ranking_search`) | ML & deep learning | learning to rank; search relevance | — | 1 (0 M/I) |
| **Statistics (inference, hypothesis tests, regression)** (`statistics`) | ML & deep learning | statistical analysis; probability | — | 7 (3 M/I) |
| **Feature stores** (`feature_store`) | MLOps & platform | feature store | part of MLOps lifecycle (model & prompt CI/CD) | 2 (0 M/I) |
| **MLOps lifecycle (model & prompt CI/CD)** (`mlops_lifecycle`) | MLOps & platform | MLOps; LLMOps; model CI/CD; model registry; prompt CI/CD | — | 4 (1 M/I) |
| **Cost & latency engineering** (`cost_latency`) | Observability & LLMOps | cost optimisation; latency optimisation; token budgets | — | 4 (3 M/I) |
| **LLM gateways** (`llm_gateways`) | Observability & LLMOps | AI gateway; LLM proxy; model gateway | — | 3 (2 M/I) |
| **Observability (OpenTelemetry traces, metrics)** (`observability`) | Observability & LLMOps | LLM observability; monitoring; telemetry | — | 12 (6 M/I) |
| **Semantic & prompt caching** (`semantic_caching`) | Observability & LLMOps | prompt caching; response caching | part of Cost & latency engineering | 1 (0 M/I) |
| **AI literacy (tokens, RAG vs fine-tune, cost)** (`ai_literacy`) | Product & business | AI fluency; LLM literacy | — | 5 (1 M/I) |
| **Internal tooling & DevEx** (`internal_tooling`) | Product & business | developer experience; DevEx; internal platforms | — | 1 (1 M/I) |
| **APIs & integrations** (`apis`) | Programming | REST APIs; API design; integrations; backend services | — | 5 (2 M/I) |
| **Data structures & algorithms** (`dsa`) | Programming | data structures; algorithms; coding interviews | — | 4 (4 M/I) |
| **System design** (`system_design`) | Programming | distributed systems design; system design for LLM applications | — | 6 (3 M/I) |
| **Alignment methods** (`alignment`) | Research | AI alignment; scalable oversight | — | 2 (1 M/I) |
| **Interpretability** (`interpretability`) | Research | mechanistic interpretability; probing; sparse autoencoders | — | 2 (1 M/I) |
| **Agentic RAG** (`agentic_rag`) | Retrieval & RAG | — | part of RAG | 1 (0 M/I) |
| **ANN indexes (HNSW, IVF, PQ)** (`ann_indexes`) | Retrieval & RAG | HNSW; approximate nearest neighbour | part of Embeddings & vector search | 2 (0 M/I) |
| **Document ingestion, parsing & chunking** (`document_ingestion`) | Retrieval & RAG | chunking; PDF parsing; OCR | part of RAG | 1 (0 M/I) |
| **Embedding & reranker models** (`embedding_models`) | Retrieval & RAG | embedding models; rerankers; cross-encoders; bi-encoders | part of Embeddings & vector search | 2 (1 M/I) |
| **Embeddings & vector search** (`vector_search`) | Retrieval & RAG | embeddings; vector databases; semantic search; vector DB | part of RAG | 2 (2 M/I) |
| **GraphRAG & knowledge graphs** (`graphrag`) | Retrieval & RAG | knowledge graphs; graph RAG | part of RAG | 1 (0 M/I) |
| **Grounding & citations (hallucination control)** (`grounding_citations`) | Retrieval & RAG | hallucination mitigation; attribution | part of RAG | 2 (0 M/I) |
| **Hybrid search (BM25 + dense)** (`hybrid_search`) | Retrieval & RAG | BM25; lexical search; keyword search | part of Retrieval quality (hybrid, reranking, recall@k) | 1 (0 M/I) |
| **Permission-aware retrieval (ACLs, tenancy)** (`access_controlled_retrieval`) | Retrieval & RAG | document-level security; multi-tenant retrieval | part of Retrieval quality (hybrid, reranking, recall@k) | 2 (1 M/I) |
| **RAG** (`rag`) | Retrieval & RAG | RAG; retrieval-augmented generation; RAG pipelines | — | 9 (3 M/I) |
| **Reranking** (`reranking`) | Retrieval & RAG | cross-encoder reranking | part of Retrieval quality (hybrid, reranking, recall@k) | 1 (0 M/I) |
| **Retrieval quality (hybrid, reranking, recall@k)** (`retrieval_quality`) | Retrieval & RAG | retrieval evaluation; search relevance | part of RAG | 5 (4 M/I) |
| **Control systems** (`control_systems`) | Robotics & physical AI | control theory; MPC; PID | part of Robotics fundamentals | 1 (1 M/I) |
| **Edge inference** (`edge_inference`) | Robotics & physical AI | edge deployment; embedded inference | — | 1 (1 M/I) |
| **Imitation learning** (`imitation_learning`) | Robotics & physical AI | behaviour cloning; diffusion policy | part of Robot learning & VLA models | 1 (1 M/I) |
| **Motion planning** (`motion_planning`) | Robotics & physical AI | trajectory planning | part of Robotics fundamentals | 1 (1 M/I) |
| **Perception / computer vision** (`perception`) | Robotics & physical AI | 3D vision; robot perception | part of Computer vision | 1 (1 M/I) |
| **Robot learning & VLA models** (`robot_learning`) | Robotics & physical AI | robot foundation models; robot policy learning | — | 1 (1 M/I) |
| **Robotics fundamentals** (`robotics_fund`) | Robotics & physical AI | kinematics; dynamics; robotics | — | 1 (1 M/I) |
| **Sensor fusion** (`sensor_fusion`) | Robotics & physical AI | Kalman filters | part of Perception / computer vision | 1 (0 M/I) |
| **Simulation & sim-to-real** (`simulation`) | Robotics & physical AI | sim-to-real; simulation; digital twins | — | 1 (1 M/I) |
| **SLAM & state estimation** (`slam`) | Robotics & physical AI | localisation; mapping | part of Robotics fundamentals | 1 (0 M/I) |
| **Vision-language-action (VLA) models** (`vla_models`) | Robotics & physical AI | VLA | part of Robot learning & VLA models | 1 (1 M/I) |
| **World models** (`world_models`) | Robotics & physical AI | — | part of Robot learning & VLA models | 1 (0 M/I) |
| **Agent abuse & MCP authorisation** (`agent_abuse`) | Security & safety | excessive agency; tool abuse; MCP authorisation | part of LLM security (prompt injection, OWASP) | 1 (1 M/I) |
| **Containment (DLP, sandboxing, egress)** (`containment`) | Security & safety | sandboxing; DLP; egress control | part of LLM security (prompt injection, OWASP) | 2 (2 M/I) |
| **Cybersecurity fundamentals** (`cybersecurity`) | Security & safety | security; information security; infosec | — | 2 (1 M/I) |
| **Data & model poisoning** (`data_poisoning`) | Security & safety | backdoors; poisoning attacks | part of LLM security (prompt injection, OWASP) | 2 (0 M/I) |
| **Guardrails** (`guardrails`) | Security & safety | content filtering; safety filters; input and output validation | part of LLM security (prompt injection, OWASP) | 5 (4 M/I) |
| **LLM security (prompt injection, OWASP)** (`llm_security`) | Security & safety | AI security; LLM security; GenAI security | — | 3 (3 M/I) |
| **Model supply chain & CVEs** (`supply_chain`) | Security & safety | model supply chain; SBOM; model provenance; CVE patching | part of LLM security (prompt injection, OWASP) | 3 (2 M/I) |
| **OAuth/OIDC, RBAC, SSO** (`iam`) | Security & safety | identity and access management; RBAC; SSO | — | 5 (5 M/I) |
| **PII detection & redaction** (`pii_protection`) | Security & safety | PII redaction; data masking | part of Privacy law & DPO duties | 4 (0 M/I) |
| **Prompt-injection attack & defence** (`prompt_injection`) | Security & safety | prompt injection; indirect prompt injection; jailbreaks | part of LLM security (prompt injection, OWASP) | 2 (1 M/I) |
| **Distillation** (`distillation`) | Training & post-training | knowledge distillation; model distillation | part of Fine-tuning (SFT, LoRA) | 2 (0 M/I) |
| **Distributed training (FSDP2, TP/PP, MoE)** (`distributed_training`) | Training & post-training | tensor parallelism; pipeline parallelism; data parallelism; multi-node training | — | 4 (1 M/I) |
| **Fine-tuning (SFT, LoRA)** (`finetuning`) | Training & post-training | fine-tuning; SFT; supervised fine-tuning | — | 4 (2 M/I) |
| **Mixed-precision training (BF16, FP8)** (`mixed_precision`) | Training & post-training | BF16; FP8 training | part of Distributed training (FSDP2, TP/PP, MoE) | 3 (0 M/I) |
| **Parameter-efficient fine-tuning (LoRA, QLoRA)** (`peft_methods`) | Training & post-training | LoRA; QLoRA; adapters | part of Fine-tuning (SFT, LoRA) | 1 (0 M/I) |
| **Post-training (SFT, preference, RL)** (`post_training`) | Training & post-training | post-training; preference optimisation; RL fine-tuning | — | 5 (2 M/I) |
| **Pre-training at scale** (`pretraining`) | Training & post-training | pre-training; foundation-model training | — | 2 (0 M/I) |
| **Preference optimisation (DPO and variants)** (`preference_optimization`) | Training & post-training | DPO; ORPO; KTO; SimPO | part of Post-training (SFT, preference, RL) | 4 (0 M/I) |
| **Reward modelling** (`reward_modeling`) | Training & post-training | reward models | part of Post-training (SFT, preference, RL) | 2 (0 M/I) |
| **RL with verifiable rewards (GRPO)** (`rlvr`) | Training & post-training | GRPO; RLVR; reasoning RL | part of Post-training (SFT, preference, RL) | 2 (0 M/I) |
| **RLHF (reward models, PPO)** (`rlhf`) | Training & post-training | PPO | part of Post-training (SFT, preference, RL) | 2 (0 M/I) |
| **Scaling laws & compute-optimal training** (`scaling_laws`) | Training & post-training | compute-optimal scaling | part of Pre-training at scale | 2 (0 M/I) |

<a id="type-method"></a>
#### Method / practice (64)

*Technical: knowledge. On a resume: Use it as the verb of a bullet: what you did, on what, with what measured result.*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Coding-agent rollout** (`coding_agents`) | Agents | coding agents; AI coding assistants | — | 2 (1 M/I) |
| **Human-in-the-loop design** (`hitl_design`) | Agents | human-in-the-loop; human review; approval workflows | — | 4 (2 M/I) |
| **Data analysis** (`data_analysis`) | Data engineering | exploratory data analysis; EDA; analytics | — | 3 (2 M/I) |
| **Agent evaluation (trajectories, task success)** (`agent_evals`) | Evaluation | trajectory evaluation; agent benchmarks | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 4 (2 M/I) |
| **Benchmark construction** (`benchmark_design`) | Evaluation | benchmark construction; dataset curation; leaderboards | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 2 (2 M/I) |
| **Error analysis** (`error_analysis`) | Evaluation | failure analysis; trace review; error taxonomy | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 4 (2 M/I) |
| **Eval regression gates in CI** (`eval_ci_gates`) | Evaluation | regression testing; CI evals | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 2 (1 M/I) |
| **Eval statistics (CIs, power, pass^k)** (`eval_stats`) | Evaluation | confidence intervals; statistical power; pass^k; significance testing | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 6 (3 M/I) |
| **Experiment design & A/B testing** (`experiment_design`) | Evaluation | A/B testing; experimentation; online experiments | — | 3 (3 M/I) |
| **Golden datasets & test-set curation** (`golden_datasets`) | Evaluation | test sets; eval datasets | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 4 (2 M/I) |
| **Human evaluation programmes** (`human_evaluation`) | Evaluation | human raters; side-by-side evaluation | part of Rubrics & inter-rater agreement | 2 (2 M/I) |
| **LLM-as-judge design & calibration** (`llm_judges`) | Evaluation | LLM-as-a-judge; judge calibration | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 7 (1 M/I) |
| **Online evaluation & production monitoring** (`online_evals`) | Evaluation | production evals; online metrics | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 2 (1 M/I) |
| **Rubrics & inter-rater agreement** (`eval_rubrics`) | Evaluation | rubric design; inter-rater agreement; Cohen's kappa | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 3 (3 M/I) |
| **Safety & capability evals** (`safety_evals`) | Evaluation | dangerous-capability evals; frontier safety evaluations | part of LLM evaluation (golden sets, calibrated judges, CI gates) | 3 (1 M/I) |
| **Synthetic data generation** (`synthetic_data`) | Evaluation | synthetic datasets | — | 2 (0 M/I) |
| **Agent-UX telemetry** (`ux_telemetry`) | Frontend & UX | UX telemetry; feedback capture; AI feature analytics | — | 1 (1 M/I) |
| **Numerics validation** (`numerics`) | GPU & kernels | numerical accuracy; low-precision numerics validation | — | 3 (1 M/I) |
| **Profiling & roofline (Nsight)** (`profiling`) | GPU & kernels | roofline analysis; performance profiling | — | 4 (3 M/I) |
| **AI impact & risk assessment** (`ai_impact_assessment`) | Governance, risk & compliance | AI impact assessment; FRIA; algorithmic impact assessment | part of GRC & risk assessment | 3 (2 M/I) |
| **AI incident management & reporting** (`ai_incident_mgmt`) | Governance, risk & compliance | serious-incident reporting; AI incident response | — | 2 (1 M/I) |
| **AI inventory & risk register** (`ai_inventory`) | Governance, risk & compliance | AI inventory; AI risk register; AI system register | — | 5 (1 M/I) |
| **AI policy & standards writing** (`policy_writing`) | Governance, risk & compliance | AI policies; acceptable-use policy | — | 1 (1 M/I) |
| **Audit methodology** (`audit_method`) | Governance, risk & compliance | internal audit; audit methodology | — | 2 (1 M/I) |
| **Controls design & testing** (`controls_testing`) | Governance, risk & compliance | control testing | part of Audit methodology | 1 (1 M/I) |
| **GRC & risk assessment** (`grc`) | Governance, risk & compliance | GRC; risk assessment; risk management | — | 8 (6 M/I) |
| **Model validation** (`model_validation`) | Governance, risk & compliance | model validation; effective challenge | — | 1 (1 M/I) |
| **Risk & compliance docs (Annex IV, model cards)** (`compliance_docs`) | Governance, risk & compliance | technical documentation; Annex IV; model cards; system cards | — | 4 (3 M/I) |
| **Third-party and vendor AI risk** (`third_party_risk`) | Governance, risk & compliance | vendor risk; TPRM | part of GRC & risk assessment | 3 (1 M/I) |
| **Annotation guidelines & task design** (`annotation_guidelines`) | Human data & annotation | labelling guidelines | part of Annotation workflows | 1 (1 M/I) |
| **Annotation workflows** (`annotation`) | Human data & annotation | data annotation; data labelling; human feedback data | — | 2 (1 M/I) |
| **Fact-checking & output verification** (`output_verification`) | Human data & annotation | fact-checking; response grading | — | 1 (1 M/I) |
| **Preference & comparison data collection** (`preference_data`) | Human data & annotation | pairwise comparisons; RLHF data | part of Annotation workflows | 1 (0 M/I) |
| **Load testing & latency SLOs** (`load_testing`) | Inference & serving | latency SLOs; TTFT; throughput benchmarking | — | 2 (1 M/I) |
| **Git & CI/CD** (`git_ci`) | Infrastructure & DevOps | CI/CD; continuous integration; version control | — | 9 (6 M/I) |
| **SRE (SLOs, on-call, incidents)** (`sre`) | Infrastructure & DevOps | SLOs; on-call; site reliability engineering | — | 3 (2 M/I) |
| **Terraform / IaC** (`iac`) | Infrastructure & DevOps | infrastructure as code; IaC | — | 3 (2 M/I) |
| **Prompt engineering** (`prompt_engineering`) | LLM applications | prompt design; prompting | part of Prompt & context design | 6 (2 M/I) |
| **Experiment tracking & reproducibility** (`experiment_tracking`) | MLOps & platform | experiment management | part of MLOps lifecycle (model & prompt CI/CD) | 5 (0 M/I) |
| **Model & data drift monitoring** (`drift_monitoring`) | MLOps & platform | drift detection; model monitoring | part of Observability (OpenTelemetry traces, metrics) | 1 (0 M/I) |
| **Incident postmortems** (`postmortems`) | Observability & LLMOps | blameless postmortems; root-cause analysis | part of SRE (SLOs, on-call, incidents) | 3 (1 M/I) |
| **LLM tracing** (`tracing`) | Observability & LLMOps | traces; spans | part of Observability (OpenTelemetry traces, metrics) | 2 (0 M/I) |
| **Production hardening (rate limits, spend caps, kill switches)** (`production_hardening`) | Observability & LLMOps | rate limiting; spend caps | — | 1 (0 M/I) |
| **Progressive delivery (canary, shadow, feature flags)** (`progressive_delivery`) | Observability & LLMOps | canary releases; shadow deployment; feature flags | part of MLOps lifecycle (model & prompt CI/CD) | 2 (1 M/I) |
| **Prompt & model versioning** (`prompt_versioning`) | Observability & LLMOps | prompt management; prompt registry | part of MLOps lifecycle (model & prompt CI/CD) | 2 (0 M/I) |
| **Agile delivery (Scrum, Kanban)** (`agile`) | Product & business | agile; Scrum; Kanban | — | 1 (1 M/I) |
| **Change management & adoption** (`change_mgmt`) | Product & business | change management; adoption programmes | — | 3 (1 M/I) |
| **Pilots & adoption measurement** (`pilots`) | Product & business | pilots; POCs; proofs of concept; adoption metrics | — | 2 (2 M/I) |
| **Product analytics** (`product_analytics`) | Product & business | funnel analysis; cohort analysis | — | 1 (0 M/I) |
| **Rapid prototyping** (`rapid_prototyping`) | Product & business | prototyping; proofs of concept | — | 3 (1 M/I) |
| **User research & discovery** (`user_research`) | Product & business | customer interviews; user interviews | — | 1 (0 M/I) |
| **Testing (pytest)** (`testing`) | Programming | unit testing; integration testing; test automation | — | 2 (1 M/I) |
| **Ablations & controlled experiments** (`ablations`) | Research | ablation studies | part of Research methods & re-implementation | 2 (1 M/I) |
| **Research methods & re-implementation** (`research_methods`) | Research | paper reproduction; re-implementation | — | 4 (3 M/I) |
| **Research-to-production** (`research_to_prod`) | Research | productionising research; tech transfer | — | 1 (1 M/I) |
| **Retrieval metrics (recall@k, MRR, nDCG)** (`retrieval_evaluation`) | Retrieval & RAG | recall@k; MRR; nDCG | part of Retrieval quality (hybrid, reranking, recall@k) | 2 (0 M/I) |
| **Safety cases** (`safety_cases`) | Robotics & physical AI | safety cases; hazard analysis | — | 1 (1 M/I) |
| **Teleoperation data pipelines** (`teleop_data`) | Robotics & physical AI | teleoperation; robot data collection | — | 1 (1 M/I) |
| **AppSec & threat modelling** (`appsec`) | Security & safety | application security; secure design review | — | 2 (1 M/I) |
| **Incident response & SIEM** (`incident_response`) | Security & safety | SIEM; SOC; detection engineering | — | 1 (1 M/I) |
| **Red-teaming** (`red_teaming`) | Security & safety | AI red teaming; adversarial testing; jailbreak testing | — | 5 (2 M/I) |
| **Threat modelling for AI systems** (`threat_modeling`) | Security & safety | threat modelling; STRIDE; attack trees | part of AppSec & threat modelling | 1 (1 M/I) |
| **Training-data curation (filtering, dedup, mixtures)** (`data_curation`) | Training & post-training | data mixtures; deduplication; data filtering | part of Pre-training at scale | 2 (0 M/I) |
| **Training-run debugging** (`training_debug`) | Training & post-training | loss spikes; training instability; divergence debugging | — | 1 (1 M/I) |

<a id="type-language"></a>
#### Programming language (16)

*Technical: concrete. On a resume: Skills section (Languages); back it with shipped or public code.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **CUDA C++** (`cuda_cpp`) | GPU & kernels | CUDA; CUDA programming | → CUDA / Triton / CUTLASS | 45 in 5: T0-03 ×36, T0-12 ×3, T0-02 ×2 … | 1 (1 M/I) |
| **CuTe DSL** (`cutedsl`) | GPU & kernels | CuteDSL | → CUDA / Triton / CUTLASS; in: Tile DSLs | 3 in 1: T0-03 ×3 | 1 (0 M/I) + 1 via class |
| **Helion** (`helion`) | GPU & kernels | Helion DSL | → CUDA / Triton / CUTLASS; in: Tile DSLs | 2 in 1: T0-03 ×2 | 1 (0 M/I) + 1 via class |
| **HIP** (`hip`) | GPU & kernels | AMD HIP | → CUDA / Triton / CUTLASS | 0 (practice-curated) | 1 (0 M/I) |
| **Triton (kernel language)** (`triton_lang`) | GPU & kernels | OpenAI Triton; Triton kernels | → CUDA / Triton / CUTLASS | 39 in 4: T0-03 ×30, T0-02 ×4, T0-13 ×4 … | 3 (1 M/I) |
| **R** (`r_lang`) | ML & deep learning | R language; tidyverse | → Statistics | not counted (ambiguous name) | 1 (0 M/I) |
| **Bash / shell scripting** (`bash`) | Programming | shell scripting | — | 0 (practice-curated) | 3 (0 M/I) |
| **C++** (`cpp`) | Programming | modern C++; C++17; C++20 | — | 6 in 3: T0-03 ×3, T0-05 ×2, T2-01 ×1 | 6 (4 M/I) |
| **Go** (`go`) | Programming | Golang | in: Go / Java | 10 in 3: T0-06 ×7, T0-16 ×2, T2-01 ×1 | 2 via class |
| **Java** (`java`) | Programming | JVM | in: Go / Java | 10 in 4: T0-06 ×7, T0-11 ×1, T0-16 ×1 … | 2 via class |
| **Python (production)** (`python`) | Programming | Python 3; production Python; asyncio | — | 107 in 17: T0-15 ×25, T0-06 ×22, T0-03 ×13 … | 21 (19 M/I) |
| **Python/SQL (notebook level)** (`python_basic`) | Programming | notebook Python; Jupyter; Python for analysis | — | 1 in 1: T0-06 ×1 | 4 (2 M/I) |
| **Rust** (`rust`) | Programming | — | — | 10 in 2: T0-16 ×7, T0-03 ×3 | 1 (0 M/I) |
| **Scala** (`scala`) | Programming | — | — | 0 (practice-curated) | 1 (0 M/I) |
| **SQL** (`sql`) | Programming | SQL queries; analytical SQL | — | 15 in 4: T0-06 ×9, T2-01 ×3, T0-16 ×2 … | 6 (1 M/I) |
| **TypeScript / JavaScript** (`typescript`) | Programming | TypeScript; JavaScript; TS; JS | — | 21 in 6: T0-16 ×8, T0-06 ×6, T1-02 ×3 … | 6 (1 M/I) |

<a id="type-framework"></a>
#### Framework / SDK (54)

*Technical: concrete. On a resume: Skills section (Frameworks) in the posting's wording; one bullet showing what you built with it.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **AutoGen** (`autogen`) · *dormant 2026-10-23* | Agents | — | → Agents & tool use | 10 in 2: T0-03 ×9, T0-01 ×1 | — |
| **Claude Agent SDK** (`claude_agent_sdk`) | Agents | Anthropic Agent SDK | → Agents & tool use; in: Agent frameworks | 2 in 1: T0-03 ×2 | 2 (0 M/I) + 5 via class |
| **CrewAI** (`crewai`) | Agents | — | → Agents & tool use; in: Agent frameworks | 5 in 3: T0-03 ×3, T0-01 ×1, T0-16 ×1 | 1 (0 M/I) + 6 via class |
| **Google Agent Development Kit (ADK)** (`google_adk`) | Agents | ADK; Agent Development Kit | → Agents & tool use; in: Agent frameworks | 4 in 2: T0-03 ×3, T0-16 ×1 | 2 (0 M/I) + 5 via class |
| **LangChain** (`langchain`) · *active 2025-10-17* | Agents | LangChain 1.x | → Agents & tool use, RAG | 49 in 6: T0-03 ×33, T0-16 ×10, T0-13 ×2 … | 2 (1 M/I) |
| **LangGraph** (`langgraph`) · *active 2025-10-17* | Agents | LangGraph 1.x | → Agents & tool use, Agent reliability; in: Agent frameworks | 33 in 4: T0-03 ×20, T0-16 ×11, T0-01 ×1 … | 2 (1 M/I) + 5 via class |
| **Mastra** (`mastra`) | Agents | — | → Agents & tool use; in: Agent frameworks | 1 in 1: T0-16 ×1 | 1 (0 M/I) + 6 via class |
| **Microsoft Agent Framework** (`ms_agent_framework`) · *active 2026-04-02* | Agents | MAF | → Agents & tool use; in: Agent frameworks | 8 in 1: T0-03 ×8 | 2 (0 M/I) + 5 via class |
| **OpenAI Agents SDK** (`openai_agents_sdk`) · *active 2026-03-23* | Agents | Agents SDK | → Agents & tool use, Durable execution & workflow state; in: Agent frameworks | 4 in 2: T0-03 ×3, T0-16 ×1 | 2 (0 M/I) + 5 via class |
| **Pydantic AI** (`pydantic_ai`) | Agents | PydanticAI | → Agents & tool use, Structured output & tool schemas; in: Agent frameworks | 5 in 2: T0-03 ×4, T0-16 ×1 | 2 (0 M/I) + 5 via class |
| **Semantic Kernel** (`semantic_kernel`) | Agents | — | → Agents & tool use | 2 in 1: T0-03 ×2 | 1 (0 M/I) |
| **smolagents** (`smolagents`) | Agents | — | → Agents & tool use | 0 (practice-curated) | 2 (0 M/I) |
| **Apache Spark** (`spark`) | Data engineering | Spark; PySpark | → Data pipelines & quality | 0 (practice-curated) | 2 (0 M/I) |
| **CopilotKit** (`copilotkit`) | Frontend & UX | — | → Streaming & agent UX, Generative UI | 14 in 1: T0-16 ×14 | 1 (0 M/I) |
| **Gradio** (`gradio`) | Frontend & UX | — | → Rapid prototyping; in: Demo UI frameworks | 9 in 1: T0-13 ×9 | 1 (0 M/I) |
| **Next.js** (`nextjs`) | Frontend & UX | NextJS | → Frontend engineering | 1 in 1: T0-16 ×1 | 1 (1 M/I) |
| **React** (`react`) | Frontend & UX | React.js; ReactJS | → Frontend engineering | 10 in 2: T0-06 ×6, T1-01 ×4 | 1 (1 M/I) |
| **Streamlit** (`streamlit`) | Frontend & UX | — | → Rapid prototyping; in: Demo UI frameworks | 3 in 1: T0-13 ×3 | 1 (0 M/I) |
| **Vercel AI SDK** (`vercel_ai_sdk`) | Frontend & UX | AI SDK | → Streaming & agent UX, LLM APIs & tool calling | 13 in 2: T0-06 ×12, T2-01 ×1 | 2 (1 M/I) |
| **MLIR** (`mlir`) | GPU & kernels | — | → ML compilers | 0 (practice-curated) | 1 (0 M/I) |
| **TorchInductor (torch.compile)** (`torchinductor`) | GPU & kernels | torch.compile; Inductor | → ML compilers | 2 in 1: T0-03 ×2 | 1 (0 M/I) |
| **XLA** (`xla`) | GPU & kernels | OpenXLA | → ML compilers | 3 in 1: T0-03 ×3 | 1 (0 M/I) |
| **BentoML** (`bentoml`) | Inference & serving | — | → Serving literacy; in: KServe / Ray Serve | 2 in 2: T0-13 ×1, T0-14 ×1 | 2 via class |
| **Hugging Face TGI** (`tgi`) · *archived 2026-03-21* | Inference & serving | Text Generation Inference; TGI | → Serving literacy | 17 in 2: T0-03 ×16, T0-05 ×1 | — |
| **llama.cpp** (`llama_cpp`) | Inference & serving | GGML | → Self-hosting open models, Edge inference; in: Local inference runtimes | 32 in 2: T0-05 ×29, T0-03 ×3 | 2 via class |
| **llm-d** (`llm_d`) | Inference & serving | — | → Prefill/decode disaggregation, KV-aware routing & load balancing; in: Distributed-inference frameworks | 10 in 2: T0-13 ×8, T0-03 ×2 | 1 (0 M/I) |
| **Mooncake** (`mooncake`) | Inference & serving | Mooncake Transfer Engine | → Prefill/decode disaggregation, KV-cache offload & tiering | 1 in 1: T0-03 ×1 | 1 (0 M/I) |
| **NVIDIA Dynamo** (`dynamo`) · *active 2026-10-22* | Inference & serving | — | → Prefill/decode disaggregation, KV-aware routing & load balancing; in: Distributed-inference frameworks | 13 in 1: T0-03 ×13 | 3 (0 M/I) |
| **NVIDIA Dynamo Triton** (`dynamo_triton`) · *renamed 2026-10-23* | Inference & serving | Triton Inference Server | → Serving literacy; in: KServe / Ray Serve | 6 in 1: T0-03 ×6 | 2 (0 M/I) + 1 via class |
| **Ollama** (`ollama`) | Inference & serving | — | → Self-hosting open models; in: Local inference runtimes | 30 in 2: T0-05 ×27, T0-03 ×3 | 2 via class |
| **Ray Serve** (`ray_serve`) | Inference & serving | — | → Serving literacy; in: KServe / Ray Serve | 4 in 1: T0-03 ×4 | 2 via class |
| **SGLang** (`sglang`) · *active 2026-10-16* | Inference & serving | — | → Serving literacy, Continuous batching & KV cache; in: vLLM / SGLang / TensorRT-LLM | 83 in 4: T0-03 ×44, T0-05 ×33, T0-13 ×5 … | 4 (1 M/I) + 2 via class |
| **TensorRT-LLM** (`trt_llm`) · *active 2026-04-20* | Inference & serving | TRT-LLM | → Serving literacy; in: vLLM / SGLang / TensorRT-LLM | 39 in 4: T0-03 ×30, T0-02 ×6, T0-05 ×2 … | 2 (1 M/I) + 3 via class |
| **vLLM** (`vllm`) · *active 2026-10-18* | Inference & serving | — | → Serving literacy, Continuous batching & KV cache; in: vLLM / SGLang / TensorRT-LLM | 169 in 8: T0-05 ×69, T0-03 ×53, T0-12 ×13 … | 4 (1 M/I) + 2 via class |
| **DSPy** (`dspy`) | LLM applications | — | → Prompt & context design | 1 in 1: T0-03 ×1 | 1 (0 M/I) |
| **JAX** (`jax`) | ML & deep learning | Flax | → Deep learning & transformers; in: TensorFlow / JAX | 3 in 2: T0-11 ×2, T0-05 ×1 | 3 (0 M/I) + 1 via class |
| **Keras** (`keras`) | ML & deep learning | — | → Deep learning & transformers | 0 (practice-curated) | 1 (0 M/I) |
| **PyTorch** (`pytorch`) | ML & deep learning | PyTorch 2.x; torch | → Deep learning & transformers | 36 in 8: T0-03 ×18, T0-13 ×4, T0-04 ×3 … | 6 (5 M/I) |
| **TensorFlow** (`tensorflow`) | ML & deep learning | TF | → Deep learning & transformers; in: TensorFlow / JAX | 4 in 2: T0-11 ×2, T0-15 ×2 | 1 via class |
| **Ray** (`ray`) | MLOps & platform | Ray Train; Ray Data; Ray Core | → Distributed training, Data pipelines & quality | 12 in 2: T0-03 ×10, T0-16 ×2 | 4 (0 M/I) |
| **Django** (`django`) | Programming | — | → APIs & integrations; in: Python web frameworks | 6 in 2: T1-01 ×5, T0-12 ×1 | 1 via class |
| **FastAPI** (`fastapi`) | Programming | — | → APIs & integrations; in: Python web frameworks | 5 in 3: T0-06 ×3, T0-13 ×1, T2-01 ×1 | 3 (0 M/I) |
| **Flask** (`flask`) | Programming | — | → APIs & integrations; in: Python web frameworks | 0 (practice-curated) | 1 via class |
| **Node.js** (`nodejs`) | Programming | Node; NodeJS | → APIs & integrations | 1 in 1: T0-16 ×1 | 1 (1 M/I) |
| **Haystack** (`haystack`) | Retrieval & RAG | deepset Haystack | → RAG | 0 (practice-curated) | 1 (0 M/I) |
| **LlamaIndex** (`llamaindex`) | Retrieval & RAG | LlamaIndex Workflows | → RAG, Agents & tool use; in: Agent frameworks | 9 in 3: T0-03 ×7, T0-13 ×1, T0-16 ×1 | 2 (0 M/I) + 5 via class |
| **LeRobot** (`lerobot`) | Robotics & physical AI | Hugging Face LeRobot | → Robot learning & VLA models | 0 (practice-curated) | 1 (0 M/I) |
| **ROS** (`ros`) | Robotics & physical AI | ROS 2; Robot Operating System | → Robotics fundamentals | 0 (practice-curated) | 1 (1 M/I) |
| **Axolotl** (`axolotl`) | Training & post-training | — | → Fine-tuning; in: Post-training frameworks | 25 in 1: T0-05 ×25 | 2 (0 M/I) |
| **DeepSpeed** (`deepspeed`) | Training & post-training | ZeRO | → Distributed training; in: Distributed-training frameworks | 0 (practice-curated) | 2 (0 M/I) |
| **LLaMA-Factory** (`llamafactory`) | Training & post-training | LlamaFactory | → Fine-tuning; in: Post-training frameworks | 2 in 2: T0-03 ×1, T0-05 ×1 | 1 (0 M/I) |
| **Megatron-LM / Megatron Core** (`megatron`) | Training & post-training | Megatron; Megatron-Core | → Distributed training; in: Distributed-training frameworks | 1 in 1: T0-05 ×1 | 2 (1 M/I) |
| **OpenRLHF** (`openrlhf`) | Training & post-training | — | → Post-training; in: Post-training frameworks | 2 in 2: T0-03 ×1, T0-05 ×1 | 2 (0 M/I) |
| **verl** (`verl`) | Training & post-training | — | → Post-training; in: Post-training frameworks | 2 in 2: T0-03 ×1, T0-05 ×1 | 2 (0 M/I) |

<a id="type-library"></a>
#### Library / package (45)

*Technical: concrete. On a resume: Skills section when the posting names it; otherwise inside a bullet.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **FastMCP** (`fastmcp`) | Agents | — | → Agent interoperability | 6 in 1: T0-16 ×6 | 2 (0 M/I) |
| **langchain-mcp-adapters** (`langchain_mcp_adapters`) | Agents | — | → Agent interoperability | 4 in 1: T0-16 ×4 | 2 (0 M/I) |
| **NumPy** (`numpy`) | Data engineering | — | → Data analysis | 2 in 1: T0-18 ×2 | 3 (0 M/I) |
| **pandas** (`pandas`) | Data engineering | — | → Data analysis | 1 in 1: T0-06 ×1 | 3 (0 M/I) |
| **Polars** (`polars`) | Data engineering | — | → Data analysis | 0 (practice-curated) | 2 (0 M/I) |
| **lm-evaluation-harness** (`lm_eval_harness`) | Evaluation | lm-eval | → Benchmark construction | 2 in 2: T0-01 ×1, T0-13 ×1 | 1 (0 M/I) |
| **Transformers.js** (`transformers_js`) | Frontend & UX | — | → On-device / WebGPU inference | 11 in 2: T0-06 ×8, T2-01 ×3 | 1 (0 M/I) |
| **CuTe** (`cute`) | GPU & kernels | — | → CUDA / Triton / CUTLASS | 0 (practice-curated) | 1 (1 M/I) |
| **CUTLASS** (`cutlass`) | GPU & kernels | — | → CUDA / Triton / CUTLASS, Attention, GEMM & quantised kernels | 4 in 1: T0-03 ×4 | 2 (1 M/I) |
| **FlashAttention** (`flash_attention`) | GPU & kernels | — | → Attention, GEMM & quantised kernels | 0 (practice-curated) | 1 (0 M/I) |
| **FlashInfer** (`flashinfer`) | GPU & kernels | — | → Attention, GEMM & quantised kernels | 3 in 1: T0-03 ×3 | 2 (0 M/I) |
| **AI Fairness 360** (`aif360`) | Governance, risk & compliance | AIF360 | → Fairness & bias assessment; in: Fairness & explainability tools | 12 in 1: T0-15 ×12 | 2 (0 M/I) |
| **Captum** (`captum`) | Governance, risk & compliance | — | → Explainability, Interpretability; in: Fairness & explainability tools | 3 in 1: T0-15 ×3 | 1 (1 M/I) + 1 via class |
| **Fairlearn** (`fairlearn`) | Governance, risk & compliance | — | → Fairness & bias assessment; in: Fairness & explainability tools | 12 in 1: T0-15 ×12 | 2 (1 M/I) |
| **LIME** (`lime`) | Governance, risk & compliance | — | → Explainability; in: Fairness & explainability tools | 3 in 1: T0-15 ×3 | 1 (1 M/I) + 1 via class |
| **Microsoft Responsible AI Toolbox** (`ms_rai_toolbox`) | Governance, risk & compliance | RAI Toolbox | → Fairness & bias assessment, Explainability; in: Fairness & explainability tools | 3 in 1: T0-15 ×3 | 1 (0 M/I) + 1 via class |
| **SHAP** (`shap`) | Governance, risk & compliance | — | → Explainability; in: Fairness & explainability tools | 4 in 1: T0-15 ×4 | 2 (1 M/I) |
| **LMCache** (`lmcache`) | Inference & serving | — | → KV-cache offload & tiering | 2 in 2: T0-03 ×1, T0-14 ×1 | 1 (0 M/I) |
| **ONNX Runtime** (`onnx_runtime`) | Inference & serving | ORT | → Edge inference | 0 (practice-curated) | 1 (0 M/I) |
| **TensorRT** (`tensorrt`) | Inference & serving | — | → Edge inference | 6 in 1: T0-03 ×6 | 2 (0 M/I) |
| **NCCL** (`nccl`) | Infrastructure & HPC | — | → NCCL / RDMA / InfiniBand | 6 in 2: T0-03 ×5, T0-13 ×1 | 2 (0 M/I) |
| **Instructor** (`instructor`) | LLM applications | — | → Structured output & tool schemas | 0 (practice-curated) | 1 (0 M/I) |
| **Outlines** (`outlines`) | LLM applications | — | → Constrained decoding | 0 (practice-curated) | 1 (0 M/I) |
| **Hugging Face Transformers** (`transformers`) | ML & deep learning | transformers library | → Deep learning & transformers, Fine-tuning | 2 in 1: T0-15 ×2 | 4 (0 M/I) |
| **scikit-learn** (`scikit_learn`) | ML & deep learning | sklearn | → ML fundamentals | 1 in 1: T0-15 ×1 | 2 (0 M/I) |
| **SciPy** (`scipy`) | ML & deep learning | — | → Statistics | 0 (practice-curated) | 2 (0 M/I) |
| **spaCy** (`spacy`) | ML & deep learning | — | → Natural language processing | 0 (practice-curated) | 2 (0 M/I) |
| **XGBoost** (`xgboost`) | ML & deep learning | gradient-boosted trees | → ML fundamentals | 0 (practice-curated) | 2 (0 M/I) |
| **LiteLLM** (`litellm`) | Observability & LLMOps | LiteLLM proxy | → LLM gateways, Model selection & routing; in: LLM gateway tools | 40 in 3: T0-05 ×32, T0-09 ×4, T0-16 ×4 | 5 (0 M/I) |
| **Celery** (`celery`) | Programming | — | — | 1 in 1: T0-03 ×1 | 2 (0 M/I) |
| **Pydantic** (`pydantic`) | Programming | Pydantic v2 | → Structured output & tool schemas | 3 in 1: T0-03 ×3 | 4 (0 M/I) |
| **pytest** (`pytest`) | Programming | — | → Testing | 4 in 2: T0-03 ×3, T0-06 ×1 | 2 (0 M/I) |
| **TransformerLens** (`transformerlens`) | Research | — | → Interpretability | 0 (practice-curated) | 1 (0 M/I) |
| **FAISS** (`faiss`) | Retrieval & RAG | — | → ANN indexes | 0 (practice-curated) | 1 (0 M/I) |
| **sentence-transformers** (`sentence_transformers`) | Retrieval & RAG | SBERT | → Embedding & reranker models | 0 (practice-curated) | 1 (0 M/I) |
| **Unstructured** (`unstructured`) | Retrieval & RAG | unstructured.io | → Document ingestion, parsing & chunking | 0 (practice-curated) | 1 (0 M/I) |
| **MuJoCo** (`mujoco`) | Robotics & physical AI | — | → Simulation & sim-to-real; in: Robot simulators | 0 (practice-curated) | 1 via class |
| **OpenCV** (`opencv`) | Robotics & physical AI | — | → Computer vision | 0 (practice-curated) | 1 (0 M/I) |
| **Guardrails AI** (`guardrails_ai`) | Security & safety | — | → Guardrails; in: Guardrail tools | 11 in 1: T0-15 ×11 | 2 (0 M/I) + 1 via class |
| **Microsoft Presidio** (`presidio`) | Security & safety | Presidio | → PII detection & redaction | 0 (practice-curated) | 2 (0 M/I) |
| **Hugging Face Accelerate** (`accelerate`) | Training & post-training | — | → Distributed training | 0 (practice-curated) | 2 (0 M/I) |
| **PEFT** (`peft`) | Training & post-training | — | → Parameter-efficient fine-tuning | 0 (practice-curated) | 1 (0 M/I) |
| **PyTorch FSDP2** (`fsdp`) | Training & post-training | FSDP; FSDP2; Fully Sharded Data Parallel | → Distributed training; in: Distributed-training frameworks | 5 in 2: T0-13 ×4, T0-04 ×1 | 2 (1 M/I) |
| **TRL** (`trl`) | Training & post-training | — | → Post-training, Fine-tuning; in: Post-training frameworks | 0 (practice-curated) | 1 (0 M/I) |
| **Unsloth** (`unsloth`) | Training & post-training | — | → Fine-tuning, Parameter-efficient fine-tuning; in: Post-training frameworks | 18 in 3: T0-12 ×16, T0-03 ×1, T0-05 ×1 | 1 (0 M/I) |

<a id="type-model"></a>
#### Model / model family (11)

*Technical: concrete. On a resume: Bullets (compared, fine-tuned, served); never a version number.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **Claude (Anthropic)** (`claude`) | Models | Claude models | → LLM APIs & tool calling; in: Frontier model families | 40 in 12: T0-12 ×9, T0-14 ×6, T1-02 ×6 … | 15 via class |
| **CLIP / SigLIP** (`clip`) | Models | SigLIP | → Multimodal AI | 0 (practice-curated) | 1 (0 M/I) |
| **Cohere Command, Embed and Rerank** (`cohere_models`) | Models | Cohere Rerank; Cohere Embed | → Embedding & reranker models, Reranking | 0 (practice-curated) | 1 (0 M/I) |
| **DeepSeek** (`deepseek`) | Models | DeepSeek models | → Self-hosting open models; in: Open-weight model families | 5 in 1: T0-14 ×5 | 8 via class |
| **Gemini (Google)** (`gemini`) | Models | Gemini models | → LLM APIs & tool calling; in: Frontier model families | 3 in 3: T0-06 ×1, T0-09 ×1, T0-10 ×1 | 15 via class |
| **GPT and o-series (OpenAI)** (`gpt`) | Models | GPT; OpenAI models | → LLM APIs & tool calling; in: Frontier model families | 6 in 4: T0-13 ×2, T0-14 ×2, T0-03 ×1 … | 15 via class |
| **Llama (Meta)** (`llama`) | Models | Llama models | → Self-hosting open models; in: Open-weight model families | 11 in 3: T0-14 ×7, T0-03 ×2, T0-05 ×2 | 8 via class |
| **Mistral and Mixtral** (`mistral_models`) | Models | Mistral AI models | → Self-hosting open models; in: Open-weight model families | 1 in 1: T0-14 ×1 | 8 via class |
| **Qwen** (`qwen`) | Models | Qwen models | → Self-hosting open models; in: Open-weight model families | 1 in 1: T0-14 ×1 | 8 via class |
| **Whisper** (`whisper`) | Models | — | → Speech & voice AI | 0 (practice-curated) | 2 (0 M/I) |
| **Llama Guard** (`llama_guard`) | Security & safety | — | → Guardrails; in: Guardrail tools | 3 in 1: T0-15 ×3 | 2 (0 M/I) + 1 via class |

<a id="type-platform"></a>
#### Platform / cloud service (31)

*Technical: concrete. On a resume: Skills section (Cloud & platforms); match the posting's cloud.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **Amazon Bedrock AgentCore** (`bedrock_agentcore`) | Agents | AgentCore | → Agents & tool use, LLM gateways; in: LLM gateway tools | 15 in 1: T0-16 ×15 | 2 (0 M/I) |
| **Amazon Bedrock** (`aws_bedrock`) | Cloud & platforms | AWS Bedrock; Bedrock | → LLM APIs & tool calling; in: Managed AI | 9 in 2: T0-09 ×6, T0-11 ×3 | 5 via class |
| **Amazon Web Services (AWS)** (`aws`) | Cloud & platforms | AWS; Amazon Web Services | in: AWS / Azure / GCP | 167 in 9: T0-11 ×130, T0-16 ×14, T0-09 ×10 … | 7 (2 M/I) + 7 via class |
| **AWS Lambda** (`aws_lambda`) | Cloud & platforms | — | → Serverless deployment | 0 (practice-curated) | 2 (0 M/I) |
| **Azure AI Foundry / Azure OpenAI** (`azure_ai_foundry`) | Cloud & platforms | Azure OpenAI; AI Foundry; Microsoft Foundry | → LLM APIs & tool calling; in: Managed AI | 8 in 3: T0-09 ×4, T0-15 ×3, T0-16 ×1 | 1 (0 M/I) + 4 via class |
| **Fireworks AI** (`fireworks`) | Cloud & platforms | Fireworks | → Self-hosting open models; in: Serverless GPU and inference clouds | 0 (practice-curated) | 2 via class |
| **Google Cloud (GCP)** (`gcp`) | Cloud & platforms | GCP; Google Cloud Platform | in: AWS / Azure / GCP | 30 in 8: T0-11 ×20, T0-14 ×3, T0-15 ×2 … | 2 (1 M/I) + 12 via class |
| **Google Cloud Run** (`cloud_run`) | Cloud & platforms | Cloud Run | → Serverless deployment | 0 (practice-curated) | 2 (0 M/I) |
| **Google Vertex AI** (`vertex_ai`) | Cloud & platforms | Vertex AI; Vertex AI Agent Builder | → LLM APIs & tool calling; in: Managed AI | 1 in 1: T0-11 ×1 | 1 (0 M/I) + 5 via class |
| **Microsoft Azure** (`azure`) | Cloud & platforms | Azure | in: AWS / Azure / GCP | 50 in 7: T0-11 ×30, T0-15 ×8, T0-09 ×5 … | 4 (1 M/I) + 12 via class |
| **Modal** (`modal`) | Cloud & platforms | Modal Labs | → Self-hosting open models; in: Serverless GPU and inference clouds | 16 in 3: T0-06 ×9, T0-13 ×5, T2-01 ×2 | 1 (0 M/I) + 1 via class |
| **Replicate** (`replicate`) | Cloud & platforms | — | → Self-hosting open models; in: Serverless GPU and inference clouds | 4 in 1: T0-13 ×4 | 2 via class |
| **Together AI** (`together_ai`) | Cloud & platforms | — | → Self-hosting open models; in: Serverless GPU and inference clouds | 7 in 3: T0-03 ×4, T0-13 ×2, T0-14 ×1 | 2 via class |
| **Databricks (incl. Mosaic AI)** (`databricks`) | Data engineering | Mosaic AI | → Data pipelines & quality, MLOps lifecycle; in: Data platforms and warehouses | 83 in 9: T0-11 ×34, T0-14 ×17, T0-17 ×13 … | 3 (0 M/I) + 1 via class |
| **Google BigQuery** (`bigquery`) | Data engineering | BigQuery | → Data pipelines & quality; in: Data platforms and warehouses | 0 (practice-curated) | 3 via class |
| **Snowflake (incl. Cortex)** (`snowflake`) | Data engineering | Snowflake Cortex | → Data pipelines & quality; in: Data platforms and warehouses | 1 in 1: T0-13 ×1 | 3 via class |
| **AMD ROCm** (`rocm`) | GPU & kernels | ROCm | in: TPU / Trainium / ROCm | 1 in 1: T0-05 ×1 | 2 (0 M/I) + 2 via class |
| **Baseten** (`baseten`) | Inference & serving | — | → Self-hosting open models; in: Serverless GPU and inference clouds | 8 in 1: T0-03 ×8 | 1 (0 M/I) + 1 via class |
| **KServe** (`kserve`) | Inference & serving | — | → Serving literacy; in: KServe / Ray Serve | 1 in 1: T0-03 ×1 | 2 (0 M/I) + 1 via class |
| **CoreWeave** (`coreweave`) | Infrastructure & HPC | — | → GPU fleet ops & scheduling | 0 (practice-curated) | 1 (0 M/I) |
| **Lambda (GPU cloud)** (`lambda_cloud`) | Infrastructure & HPC | Lambda Labs | — | 1 in 1: T0-06 ×1 | 1 (0 M/I) |
| **Anthropic API** (`anthropic_platform`) | LLM applications | Claude API | → LLM APIs & tool calling; in: LLM API providers | 7 in 3: T0-09 ×5, T0-13 ×1, T1-02 ×1 | 6 via class |
| **Gemini API (Google AI Studio)** (`gemini_api`) | LLM applications | Google AI Studio | → LLM APIs & tool calling; in: LLM API providers | 0 (practice-curated) | 6 via class |
| **OpenAI API platform** (`openai_platform`) | LLM applications | OpenAI API | → LLM APIs & tool calling; in: LLM API providers | 2 in 1: T0-09 ×2 | 6 via class |
| **Hugging Face Hub** (`hugging_face`) | ML & deep learning | Hugging Face; HF Hub; Inference Endpoints | — | 68 in 10: T0-12 ×21, T0-05 ×14, T0-13 ×11 … | 7 (0 M/I) |
| **Amazon SageMaker** (`sagemaker`) | MLOps & platform | SageMaker | → MLOps lifecycle | 1 in 1: T0-11 ×1 | 2 (0 M/I) |
| **Anyscale** (`anyscale`) | MLOps & platform | — | — | 4 in 3: T0-05 ×2, T0-03 ×1, T0-12 ×1 | 2 (0 M/I) |
| **Azure Machine Learning** (`azure_ml`) | MLOps & platform | Azure ML | → MLOps lifecycle | 1 in 1: T0-15 ×1 | 2 (0 M/I) |
| **Kubeflow** (`kubeflow`) | MLOps & platform | Kubeflow Pipelines | → MLOps lifecycle | 0 (practice-curated) | 1 (0 M/I) |
| **Gazebo** (`gazebo`) | Robotics & physical AI | — | → Simulation & sim-to-real; in: Robot simulators | 0 (practice-curated) | 1 via class |
| **NVIDIA Isaac Sim / Isaac Lab** (`isaac`) | Robotics & physical AI | Isaac Sim; Isaac Lab | → Simulation & sim-to-real; in: Robot simulators | 0 (practice-curated) | 1 via class |

<a id="type-data-store"></a>
#### Data store (14)

*Technical: concrete. On a resume: Skills section (Data); show scale or design choice in a bullet.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **MongoDB** (`mongodb`) | Data engineering | — | — | 0 (practice-curated) | 2 (0 M/I) |
| **PostgreSQL** (`postgresql`) | Data engineering | Postgres | — | 3 in 3: T0-03 ×1, T0-06 ×1, T0-16 ×1 | 4 (0 M/I) |
| **Redis** (`redis`) | Data engineering | — | → Semantic & prompt caching | 1 in 1: T0-03 ×1 | 2 (0 M/I) |
| **Object storage (S3, GCS, Azure Blob)** (`object_storage`) | Infrastructure & HPC | Amazon S3; GCS; Blob Storage | → Checkpointing & storage throughput | 0 (practice-curated) | 1 (0 M/I) |
| **Feast** (`feast`) | MLOps & platform | — | → Feature stores | 0 (practice-curated) | 2 (0 M/I) |
| **Chroma** (`chroma`) | Retrieval & RAG | ChromaDB | → Embeddings & vector search; in: Vector stores | 0 (practice-curated) | 4 via class |
| **Elasticsearch** (`elasticsearch`) | Retrieval & RAG | Elastic | → Hybrid search, Embeddings & vector search; in: Vector stores | 0 (practice-curated) | 4 via class |
| **Milvus / Zilliz** (`milvus`) | Retrieval & RAG | Zilliz | → Embeddings & vector search; in: Vector stores | 0 (practice-curated) | 4 via class |
| **Neo4j** (`neo4j`) | Retrieval & RAG | — | → GraphRAG & knowledge graphs | 0 (practice-curated) | 1 (0 M/I) |
| **OpenSearch** (`opensearch`) | Retrieval & RAG | — | → Hybrid search, Embeddings & vector search; in: Vector stores | 1 in 1: T0-12 ×1 | 4 via class |
| **pgvector** (`pgvector`) | Retrieval & RAG | — | → Embeddings & vector search; in: Vector stores | 2 in 2: T0-03 ×1, T0-06 ×1 | 1 (0 M/I) + 3 via class |
| **Pinecone** (`pinecone`) | Retrieval & RAG | — | → Embeddings & vector search; in: Vector stores | 2 in 1: T0-03 ×2 | 1 (0 M/I) + 3 via class |
| **Qdrant** (`qdrant`) | Retrieval & RAG | — | → Embeddings & vector search; in: Vector stores | 0 (practice-curated) | 4 via class |
| **Weaviate** (`weaviate`) | Retrieval & RAG | — | → Embeddings & vector search; in: Vector stores | 0 (practice-curated) | 4 via class |

<a id="type-infra-tool"></a>
#### Infrastructure / DevOps tool (18)

*Technical: concrete. On a resume: Skills section (Infrastructure); show what you ran and at what scale.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **Temporal** (`temporal`) | Agents | Temporal.io | → Durable execution & workflow state | 23 in 10: T0-03 ×13, T0-12 ×2, T0-04 ×1 … | 1 (0 M/I) |
| **Apache Airflow** (`airflow`) | Data engineering | Airflow | → Data pipelines & quality | 2 in 2: T0-03 ×1, T0-12 ×1 | 2 (0 M/I) |
| **Apache Kafka** (`kafka`) | Data engineering | Kafka | → Data pipelines & quality | 2 in 1: T0-14 ×2 | 2 (0 M/I) |
| **NVIDIA Nsight (Systems / Compute)** (`nsight`) | GPU & kernels | Nsight Compute; Nsight Systems; ncu; nsys | → Profiling & roofline | 2 in 1: T0-03 ×2 | 2 (1 M/I) |
| **k6** (`k6`) | Inference & serving | Grafana k6 | → Load testing & latency SLOs; in: General load-testing tools | 8 in 1: T0-13 ×8 | 3 via class |
| **Locust** (`locust`) | Inference & serving | — | → Load testing & latency SLOs; in: General load-testing tools | 4 in 1: T0-13 ×4 | 3 via class |
| **Docker** (`docker`) | Infrastructure & DevOps | containers; containerisation; Dockerfile | — | 19 in 6: T0-13 ×10, T0-06 ×3, T0-03 ×2 … | 12 (2 M/I) |
| **Git** (`git`) | Infrastructure & DevOps | — | → Git & CI/CD | 3 in 2: T1-01 ×2, T0-09 ×1 | 2 (0 M/I) |
| **GitHub Actions** (`github_actions`) | Infrastructure & DevOps | — | → Git & CI/CD | 8 in 2: T0-13 ×6, T1-01 ×2 | 3 (0 M/I) |
| **Helm** (`helm`) | Infrastructure & DevOps | Helm charts | → Terraform / IaC | 0 (practice-curated) | 2 (0 M/I) |
| **Kubernetes** (`kubernetes`) | Infrastructure & DevOps | K8s; EKS; GKE; AKS | in: Cluster schedulers | 15 in 5: T0-03 ×9, T0-12 ×3, T0-11 ×1 … | 10 (3 M/I) |
| **Linux** (`linux`) | Infrastructure & DevOps | Unix; shell | — | 15 in 4: T0-16 ×11, T0-06 ×2, T0-09 ×1 … | 5 (2 M/I) |
| **Terraform** (`terraform`) | Infrastructure & DevOps | OpenTofu | → Terraform / IaC | 2 in 2: T0-11 ×1, T0-13 ×1 | 4 (2 M/I) |
| **Lustre** (`lustre`) | Infrastructure & HPC | — | → Checkpointing & storage throughput | 0 (practice-curated) | 1 (0 M/I) |
| **Slurm** (`slurm`) | Infrastructure & HPC | SLURM | → GPU fleet ops & scheduling; in: Cluster schedulers | 0 (practice-curated) | 4 (0 M/I) |
| **WEKA** (`weka`) | Infrastructure & HPC | WekaFS | → Checkpointing & storage throughput | 0 (practice-curated) | 1 (0 M/I) |
| **Grafana** (`grafana`) | Observability & LLMOps | — | → Observability | 6 in 3: T0-03 ×3, T0-13 ×2, T0-16 ×1 | 3 (0 M/I) |
| **Prometheus** (`prometheus`) | Observability & LLMOps | — | → Observability | 2 in 1: T0-03 ×2 | 3 (0 M/I) |

<a id="type-product"></a>
#### Specialised product (38)

*Technical: concrete. On a resume: Skills section (Evaluation, observability, security or governance tools); show the practice, not just the tool.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **Claude Code** (`claude_code`) | Agents | — | → Coding-agent rollout; in: Coding-agent tools | 4 in 3: T0-09 ×2, T0-05 ×1, T0-16 ×1 | 1 (1 M/I) |
| **Cursor** (`cursor`) | Agents | — | → Coding-agent rollout; in: Coding-agent tools | 18 in 3: T0-12 ×16, T0-05 ×1, T0-09 ×1 | 1 (0 M/I) |
| **GitHub Copilot** (`github_copilot`) | Agents | Copilot | → Coding-agent rollout; in: Coding-agent tools | 17 in 6: T0-10 ×8, T1-02 ×4, T0-15 ×2 … | 1 (0 M/I) |
| **OpenAI Codex** (`openai_codex`) | Agents | Codex | → Coding-agent rollout; in: Coding-agent tools | 6 in 4: T0-12 ×3, T0-01 ×1, T0-05 ×1 … | 1 (0 M/I) |
| **Braintrust** (`braintrust`) · *active 2026-05-04* | Evaluation | — | → LLM evaluation, LLM tracing; in: LLM tracing and observability products, Evaluation runners and platforms | 35 in 4: T0-03 ×18, T0-18 ×14, T0-13 ×2 … | 2 (0 M/I) + 7 via class |
| **DeepEval** (`deepeval`) · *active 2026-10-23* | Evaluation | Confident AI | → LLM evaluation, Eval regression gates in CI; in: Evaluation runners and platforms | 12 in 2: T0-03 ×10, T0-13 ×2 | 2 (0 M/I) + 4 via class |
| **Giskard** (`giskard`) | Evaluation | — | → LLM evaluation, Red-teaming; in: Evaluation runners and platforms, AI red-teaming tools | 13 in 1: T0-15 ×13 | 2 (1 M/I) + 7 via class |
| **Inspect (UK AISI)** (`inspect_ai`) | Evaluation | Inspect AI; inspect_ai | → Safety & capability evals, LLM evaluation; in: Evaluation runners and platforms | 3 in 1: T0-15 ×3 | 3 (0 M/I) + 5 via class |
| **Promptfoo** (`promptfoo`) · *acquired 2026-03-09* | Evaluation | — | → LLM evaluation, Red-teaming; in: Evaluation runners and platforms, AI red-teaming tools | 36 in 4: T0-03 ×18, T0-09 ×8, T0-13 ×7 … | 4 (0 M/I) + 5 via class |
| **RAGAS** (`ragas`) · *dormant 2026-10-23* | Evaluation | Ragas | → LLM evaluation | 16 in 2: T0-03 ×14, T0-13 ×2 | — |
| **TruLens** (`trulens`) | Evaluation | — | → LLM evaluation; in: Evaluation runners and platforms | 6 in 2: T0-03 ×3, T0-13 ×3 | 1 (0 M/I) + 5 via class |
| **Figma** (`figma`) | Frontend & UX | — | → Rapid prototyping | 1 in 1: T0-14 ×1 | 2 (0 M/I) |
| **Credo AI** (`credo_ai`) | Governance, risk & compliance | — | → AI inventory & risk register, GRC & risk assessment; in: AI governance platforms | 8 in 1: T0-15 ×8 | 1 (0 M/I) + 1 via class |
| **Holistic AI** (`holistic_ai`) | Governance, risk & compliance | — | → AI inventory & risk register, Fairness & bias assessment; in: AI governance platforms | 4 in 1: T0-15 ×4 | 1 (0 M/I) + 1 via class |
| **IBM OpenPages / watsonx.governance** (`ibm_openpages`) | Governance, risk & compliance | OpenPages; watsonx.governance | → GRC & risk assessment, Model risk management; in: AI governance platforms | 8 in 1: T0-15 ×8 | 2 (0 M/I) + 1 via class |
| **OneTrust (AI governance)** (`onetrust`) | Governance, risk & compliance | — | → AI inventory & risk register, GRC & risk assessment; in: AI governance platforms | 6 in 1: T0-15 ×6 | 2 (0 M/I) + 1 via class |
| **SynthID** (`synthid`) | Governance, risk & compliance | — | → Content provenance | 3 in 1: T0-15 ×3 | 1 (0 M/I) |
| **Argilla** (`argilla`) | Human data & annotation | — | → Annotation workflows, Preference & comparison data collection; in: Annotation platforms | 0 (practice-curated) | 2 via class |
| **Label Studio** (`label_studio`) | Human data & annotation | — | → Annotation workflows; in: Annotation platforms | 0 (practice-curated) | 2 via class |
| **Labelbox** (`labelbox`) | Human data & annotation | — | → Annotation workflows; in: Annotation platforms | 0 (practice-curated) | 2 via class |
| **AIPerf / GenAI-Perf** (`aiperf`) | Inference & serving | GenAI-Perf | → Load testing & latency SLOs; in: Inference benchmarking tools | 9 in 2: T0-14 ×5, T0-13 ×4 | 1 (0 M/I) |
| **GuideLLM** (`guidellm`) | Inference & serving | — | → Load testing & latency SLOs; in: Inference benchmarking tools | 8 in 1: T0-13 ×8 | 1 (0 M/I) |
| **inference-perf** (`inference_perf`) | Inference & serving | — | → Load testing & latency SLOs; in: Inference benchmarking tools | 8 in 1: T0-13 ×8 | 1 (0 M/I) |
| **NVIDIA NIM** (`nim`) | Inference & serving | NIM microservices | → Serving literacy; in: KServe / Ray Serve | 1 in 1: T0-14 ×1 | 2 via class |
| **MLflow** (`mlflow`) | MLOps & platform | — | → Experiment tracking & reproducibility, MLOps lifecycle; in: Experiment trackers | 4 in 1: T0-15 ×4 | 3 (0 M/I) |
| **Weights & Biases (incl. Weave)** (`wandb`) | MLOps & platform | W&B; Weave; wandb | → Experiment tracking & reproducibility, LLM tracing; in: Experiment trackers | 1 in 1: T0-03 ×1 | 5 (0 M/I) |
| **agentgateway** (`agentgateway`) | Observability & LLMOps | — | → LLM gateways, Agent interoperability; in: LLM gateway tools | 18 in 1: T0-16 ×18 | 3 (0 M/I) |
| **Arize AX** (`arize`) | Observability & LLMOps | Arize | → Observability, Online evaluation & production monitoring; in: LLM tracing and observability products | 19 in 4: T0-06 ×12, T0-15 ×5, T0-03 ×1 … | 2 (0 M/I) + 8 via class |
| **Arize Phoenix** (`phoenix`) · *active 2026-10-23* | Observability & LLMOps | Phoenix | → LLM tracing, LLM evaluation; in: LLM tracing and observability products | 21 in 3: T0-03 ×11, T0-13 ×9, T0-14 ×1 | 3 (0 M/I) + 7 via class |
| **Azure API Management (AI gateway)** (`azure_apim`) | Observability & LLMOps | APIM | → LLM gateways; in: LLM gateway tools | 8 in 1: T0-16 ×8 | 2 (0 M/I) |
| **Datadog (incl. LLM Observability)** (`datadog`) | Observability & LLMOps | — | → Observability; in: LLM tracing and observability products | 20 in 2: T0-03 ×19, T0-16 ×1 | 2 (0 M/I) + 9 via class |
| **Helicone** (`helicone`) | Observability & LLMOps | — | → LLM tracing, LLM gateways; in: LLM tracing and observability products, LLM gateway tools | 2 in 1: T0-03 ×2 | 9 via class |
| **Langfuse** (`langfuse`) · *acquired 2026-01-16* | Observability & LLMOps | — | → LLM tracing, LLM evaluation; in: LLM tracing and observability products | 63 in 6: T0-05 ×28, T0-03 ×14, T0-13 ×13 … | 3 (0 M/I) + 7 via class |
| **LangSmith** (`langsmith`) | Observability & LLMOps | — | → LLM tracing, LLM evaluation; in: LLM tracing and observability products | 14 in 3: T0-03 ×7, T0-13 ×6, T0-14 ×1 | 2 (0 M/I) + 7 via class |
| **Jira** (`jira`) | Product & business | — | → Agile delivery | 3 in 1: T0-09 ×3 | 1 (0 M/I) |
| **garak** (`garak`) | Security & safety | — | → Red-teaming; in: AI red-teaming tools | 3 in 1: T0-15 ×3 | 3 (0 M/I) + 2 via class |
| **NeMo Guardrails** (`nemo_guardrails`) | Security & safety | — | → Guardrails; in: Guardrail tools | 8 in 1: T0-15 ×8 | 2 (1 M/I) + 1 via class |
| **PyRIT** (`pyrit`) | Security & safety | — | → Red-teaming; in: AI red-teaming tools | 3 in 1: T0-15 ×3 | 3 (0 M/I) + 2 via class |

<a id="type-hardware"></a>
#### Hardware / accelerator (9)

*Technical: concrete. On a resume: Bullets with scale (for example "on 8×H100"), disclosed honestly.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **AMD Instinct (MI300 series)** (`amd_instinct`) | GPU & kernels | MI300X; MI325X; MI355X | — | 0 (practice-curated) | 3 (0 M/I) |
| **AWS Trainium / Inferentia** (`trainium`) | GPU & kernels | Trainium; Inferentia; Neuron SDK | in: TPU / Trainium / ROCm | 1 in 1: T0-03 ×1 | 3 (0 M/I) |
| **Google TPU** (`tpu`) | GPU & kernels | TPU; TPUs | in: TPU / Trainium / ROCm | 11 in 3: T0-03 ×8, T0-06 ×2, T0-05 ×1 | 5 (0 M/I) |
| **NVIDIA Ampere (A100)** (`nvidia_ampere`) | GPU & kernels | A100 | → GPU fundamentals | 6 in 3: T0-13 ×3, T0-06 ×2, T0-03 ×1 | 2 (0 M/I) |
| **NVIDIA Blackwell (B200 / GB200 / GB300)** (`nvidia_blackwell`) | GPU & kernels | B200; GB200; GB300; Blackwell | → GPU fundamentals | 14 in 4: T0-12 ×5, T0-14 ×4, T0-03 ×3 … | 3 (1 M/I) |
| **NVIDIA Hopper (H100 / H200)** (`nvidia_hopper`) | GPU & kernels | H100; H200 | → GPU fundamentals | 29 in 6: T0-14 ×12, T0-06 ×8, T0-13 ×4 … | 7 (1 M/I) |
| **InfiniBand** (`infiniband`) | Infrastructure & HPC | IB | → NCCL / RDMA / InfiniBand | 1 in 1: T0-03 ×1 | 1 (0 M/I) |
| **NVLink / NVSwitch** (`nvlink`) | Infrastructure & HPC | NVSwitch | → NCCL / RDMA / InfiniBand | 0 (practice-curated) | 1 (0 M/I) |
| **NVIDIA Jetson** (`jetson`) | Robotics & physical AI | Jetson Orin; Jetson Thor | → Edge inference | 0 (practice-curated) | 1 (0 M/I) |

<a id="type-protocol"></a>
#### Protocol / standard (20)

*Technical: concrete. On a resume: Skills section or a bullet showing an integration (for example "MCP server with OAuth").*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **A2A (Agent2Agent)** (`a2a`) · *active 2026-03-12* | Agents | Agent2Agent | → Agent interoperability | 66 in 1: T0-16 ×66 | 3 (0 M/I) |
| **MCP (Model Context Protocol)** (`mcp`) | Agents | MCP; Model Context Protocol; MCP servers | → Agent interoperability | 269 in 6: T0-16 ×252, T0-03 ×9, T0-06 ×4 … | 10 (2 M/I) |
| **OpenLineage** (`openlineage`) | Data engineering | — | → Data governance & lineage | 3 in 1: T0-15 ×3 | 2 (0 M/I) |
| **AG-UI** (`ag_ui`) · *active 2026-09-18* | Frontend & UX | Agent-User Interaction protocol | → Streaming & agent UX, Agent interoperability | 24 in 1: T0-16 ×24 | 2 (0 M/I) |
| **Server-Sent Events (SSE)** (`sse`) | Frontend & UX | SSE; streaming HTTP | → Streaming & agent UX | 20 in 2: T0-16 ×17, T0-14 ×3 | 2 (1 M/I) |
| **WebGPU** (`webgpu`) | Frontend & UX | — | → On-device / WebGPU inference | 15 in 2: T0-06 ×12, T2-01 ×3 | 1 (0 M/I) |
| **WebMCP** (`webmcp`) | Frontend & UX | — | → Agent interoperability | 10 in 1: T0-06 ×10 | 2 (0 M/I) |
| **WebSockets** (`websockets`) | Frontend & UX | WebSocket | → Streaming & agent UX | 7 in 2: T0-16 ×5, T0-14 ×2 | 1 (0 M/I) |
| **C2PA** (`c2pa`) | Governance, risk & compliance | Content Credentials | → Content provenance | 43 in 1: T0-15 ×43 | 3 (0 M/I) |
| **GGUF** (`gguf`) | Inference & serving | — | → Self-hosting open models | 2 in 1: T0-03 ×2 | 1 (0 M/I) |
| **ONNX** (`onnx`) | Inference & serving | — | → Edge inference | 0 (practice-curated) | 2 (0 M/I) |
| **RDMA (incl. RoCE)** (`rdma`) | Infrastructure & HPC | RoCE; GPUDirect RDMA | → NCCL / RDMA / InfiniBand | 3 in 1: T0-03 ×3 | 1 (0 M/I) |
| **JSON Schema** (`json_schema`) | LLM applications | — | → Structured output & tool schemas | 1 in 1: T0-03 ×1 | 3 (0 M/I) |
| **OpenTelemetry** (`opentelemetry`) | Observability & LLMOps | OTel | → Observability, LLM tracing | 49 in 4: T0-03 ×26, T0-13 ×13, T0-16 ×7 … | 3 (0 M/I) |
| **OTel GenAI semantic conventions** (`otel_genai`) · *development 2026-10-23* | Observability & LLMOps | GenAI semantic conventions | → Observability | 12 in 3: T0-03 ×8, T0-13 ×3, T0-15 ×1 | 2 (0 M/I) |
| **gRPC** (`grpc`) | Programming | — | → APIs & integrations | 6 in 2: T0-13 ×4, T0-16 ×2 | 2 (0 M/I) |
| **OpenAPI** (`openapi`) | Programming | Swagger | → APIs & integrations | 2 in 1: T0-16 ×2 | 3 (0 M/I) |
| **OAuth 2.x** (`oauth`) | Security & safety | OAuth; OAuth 2.1 | → OAuth/OIDC, RBAC, SSO | 21 in 1: T0-16 ×21 | 9 (1 M/I) |
| **OpenID Connect (OIDC)** (`oidc`) | Security & safety | OIDC | → OAuth/OIDC, RBAC, SSO | 2 in 1: T0-16 ×2 | 3 (0 M/I) |
| **safetensors** (`safetensors`) | Security & safety | — | → Model supply chain & CVEs | 0 (practice-curated) | 3 (0 M/I) |

<a id="type-regulation"></a>
#### Regulation / framework (18)

*Technical: concrete. On a resume: Skills section for governance, risk and security roles; show an assessment, control or document you produced.*

| Skill | Category | Posting wording (aliases) | Relations | Corpus mentions | Roles listing it |
|---|---|---|---|---|:---:|
| **California SB 53** (`ca_sb53`) | Governance, risk & compliance | SB 53 | → EU AI Act / NIST AI RMF / ISO 42001 | 2 in 1: T0-15 ×2 | 2 (0 M/I) |
| **Colorado AI Act** (`colorado_ai_act`) | Governance, risk & compliance | — | → EU AI Act / NIST AI RMF / ISO 42001 | 28 in 3: T0-15 ×14, T0-18 ×13, T1-02 ×1 | 2 (1 M/I) |
| **EU AI Act** (`eu_ai_act`) | Governance, risk & compliance | AI Act | → EU AI Act / NIST AI RMF / ISO 42001 | 71 in 5: T0-15 ×63, T0-18 ×4, T0-09 ×2 … | 14 (3 M/I) |
| **EU GPAI Code of Practice** (`eu_gpai_code`) | Governance, risk & compliance | GPAI Code of Practice | → EU AI Act / NIST AI RMF / ISO 42001 | 8 in 1: T0-15 ×8 | 2 (0 M/I) |
| **GDPR** (`gdpr`) | Governance, risk & compliance | — | → Privacy law & DPO duties | 10 in 3: T0-15 ×8, T0-05 ×1, T0-07 ×1 | 3 (0 M/I) |
| **HIPAA** (`hipaa`) | Governance, risk & compliance | — | → Privacy law & DPO duties | 1 in 1: T0-15 ×1 | 2 (0 M/I) |
| **India DPDP Act** (`dpdp`) | Governance, risk & compliance | DPDP; Digital Personal Data Protection Act | → Sector rules, Privacy law & DPO duties | 48 in 5: T0-15 ×31, T0-09 ×10, T0-18 ×5 … | 2 (2 M/I) |
| **ISO/IEC 42001** (`iso_42001`) | Governance, risk & compliance | ISO 42001; AIMS | → EU AI Act / NIST AI RMF / ISO 42001 | 25 in 1: T0-15 ×25 | 4 (3 M/I) |
| **NAIC AI model bulletin (insurance)** (`naic_bulletin`) | Governance, risk & compliance | NAIC bulletin | → Sector rules | 12 in 1: T0-15 ×12 | 2 (1 M/I) |
| **NIST AI RMF** (`nist_ai_rmf`) | Governance, risk & compliance | AI Risk Management Framework; NIST AI 600-1 | → EU AI Act / NIST AI RMF / ISO 42001 | 21 in 2: T0-15 ×15, T0-09 ×6 | 8 (2 M/I) |
| **NYC Local Law 144** (`nyc_ll144`) | Governance, risk & compliance | LL144; AEDT law | → Sector rules | 7 in 2: T0-15 ×6, T0-04 ×1 | 2 (2 M/I) |
| **SR 26-2 (US banking model-risk guidance)** (`sr_26_2`) | Governance, risk & compliance | — | → Sector rules, Model risk management | 26 in 2: T0-15 ×17, T0-09 ×9 | 2 (2 M/I) |
| **Functional-safety standards (IEC 61508, ISO 26262, ISO 10218)** (`functional_safety`) | Robotics & physical AI | ISO 26262; IEC 61508; ISO 10218 | → Safety cases | 0 (practice-curated) | 1 (0 M/I) |
| **ISO/IEC 27001** (`iso_27001`) | Security & safety | ISO 27001 | — | 0 (practice-curated) | 3 (0 M/I) |
| **MITRE ATLAS** (`mitre_atlas`) | Security & safety | ATLAS | → Red-teaming | 0 (practice-curated) | 2 (0 M/I) |
| **OWASP agentic AI threat guidance** (`owasp_agentic`) | Security & safety | OWASP Top 10 for Agentic Applications | → Agent abuse & MCP authorisation | 2 in 1: T0-16 ×2 | 2 (1 M/I) |
| **OWASP Top 10 for LLM Applications** (`owasp_llm_top10`) | Security & safety | OWASP LLM Top 10 | → LLM security | 14 in 3: T0-09 ×7, T0-14 ×5, T0-05 ×2 | 9 (1 M/I) |
| **SOC 2** (`soc2`) | Security & safety | — | — | 0 (practice-curated) | 3 (0 M/I) |

<a id="type-communication"></a>
#### Communication & collaboration (11)

*Non-technical. On a resume: Show, don't list: a bullet with the artefact and its effect ("wrote the design doc adopted by 3 teams").*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Clear writing & presenting** (`writing`) | Communication & collaboration | clear writing; presentations | — | 2 (2 M/I) |
| **Communication (written & verbal)** (`communication`) | Communication & collaboration | communication skills; verbal communication; written communication | — | 26 (15 M/I) |
| **Cross-functional collaboration** (`cross_functional`) | Communication & collaboration | collaboration; teamwork | — | 9 (1 M/I) |
| **Customer-facing communication** (`customer_communication`) | Communication & collaboration | client communication; customer workshops | — | 3 (1 M/I) |
| **Design docs & RFCs** (`design_docs`) | Communication & collaboration | design documents; RFCs; technical specs | — | 11 (0 M/I) |
| **Executive & board communication** (`executive_communication`) | Communication & collaboration | executive briefings; board reporting | — | 6 (4 M/I) |
| **PRDs & product specs** (`prd_writing`) | Communication & collaboration | product requirements documents; specs | — | 1 (1 M/I) |
| **Presenting & live demos** (`presenting`) | Communication & collaboration | presentations; public speaking; demos | — | 7 (1 M/I) |
| **Stakeholder communication** (`stakeholder`) | Communication & collaboration | stakeholder management; stakeholder communication | — | 12 (6 M/I) |
| **Teaching & workshop delivery** (`teaching`) | Communication & collaboration | training delivery; workshops | — | 1 (1 M/I) |
| **Technical writing** (`tech_writing`) | Communication & collaboration | technical writing; documentation | — | 7 (2 M/I) |

<a id="type-behavioural"></a>
#### Behavioural competency (9)

*Non-technical. On a resume: Show in bullets; prepare a STAR-AI story for the interview loop.*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Adaptability & learning agility** (`adaptability`) | Behavioural | adaptability; continuous learning | — | 3 (1 M/I) |
| **Attention to detail** (`attention_to_detail`) | Behavioural | rigour; precision | — | 1 (1 M/I) |
| **Creativity** (`creativity`) | Behavioural | innovation | — | 1 (1 M/I) |
| **Explaining probabilistic trade-offs (C2)** (`c2_tradeoffs`) | Behavioural | trade-off communication | — | 25 (25 M/I) |
| **Ownership & incident response (C3)** (`c3_ownership`) | Behavioural | ownership; accountability | — | 25 (25 M/I) |
| **Pragmatism under ambiguity (C1)** (`c1_pragmatism`) | Behavioural | ambiguity; bias for action | — | 26 (25 M/I) |
| **Problem solving** (`problem_solving`) | Behavioural | analytical thinking; critical thinking | — | 1 (0 M/I) |
| **Responsible-AI judgement (C4)** (`c4_responsible_ai`) | Behavioural | responsible AI; AI ethics | — | 26 (25 M/I) |
| **Time management & prioritisation** (`time_management`) | Behavioural | prioritisation; organisation | — | 2 (1 M/I) |

<a id="type-business"></a>
#### Business & product (13)

*Non-technical. On a resume: Summary and bullets with business outcomes (cost, revenue, adoption).*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **AI operating model & governance boards** (`operating_model`) | Governance, risk & compliance | AI operating model; AI governance board; AI CoE | — | 2 (2 M/I) |
| **AI strategy & portfolio** (`strategy`) | Product & business | AI strategy; portfolio management | — | 4 (2 M/I) |
| **Build-vs-buy & vendor evaluation** (`build_vs_buy`) | Product & business | vendor selection; procurement | — | 4 (1 M/I) |
| **Customer scoping & demos** (`customer_scoping`) | Product & business | discovery; requirements gathering; solution scoping; demos | — | 3 (2 M/I) |
| **Go-to-market & pricing** (`go_to_market`) | Product & business | GTM; packaging | — | 2 (0 M/I) |
| **Metrics for non-deterministic systems** (`success_metrics`) | Product & business | KPIs; north-star metrics; product metrics for AI | — | 3 (1 M/I) |
| **Pre-sales** (`presales`) | Product & business | pre-sales; solution selling; RFPs; technical sales | — | 2 (1 M/I) |
| **Product management** (`product_mgmt`) | Product & business | product management; product strategy | — | 3 (1 M/I) |
| **Product sense** (`product_sense`) | Product & business | product thinking; user empathy | — | 5 (3 M/I) |
| **Programme & project management** (`program_management`) | Product & business | project management; programme management; delivery management | — | 3 (0 M/I) |
| **Roadmapping & prioritisation** (`roadmapping`) | Product & business | roadmaps; product roadmap | — | 2 (1 M/I) |
| **ROI & business cases** (`business_case`) | Product & business | ROI; business value; value realisation | — | 6 (1 M/I) |
| **Token & unit economics** (`unit_economics`) | Product & business | token economics; cost per task; AI pricing | — | 8 (3 M/I) |

<a id="type-leadership"></a>
#### Leadership & people (8)

*Non-technical. On a resume: Bullets with scope: team size, hires, mentees, decisions owned.*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Budget & P&L ownership** (`budget_ownership`) | Leadership | budget; P&L | — | 2 (1 M/I) |
| **Hiring & interviewing** (`hiring`) | Leadership | recruiting; interviewing; hiring bar | — | 3 (2 M/I) |
| **Influence without authority** (`influence`) | Leadership | leading without authority | — | 4 (0 M/I) |
| **Leadership & mentoring** (`leadership`) | Leadership | leadership; technical leadership | — | 5 (4 M/I) |
| **Mentoring** (`mentoring`) | Leadership | mentorship; coaching | — | 23 (2 M/I) |
| **Organisation design** (`org_design`) | Leadership | org design; team topology | — | 2 (1 M/I) |
| **People management** (`people_management`) | Leadership | line management; performance management | — | 2 (1 M/I) |
| **Technical leadership** (`technical_leadership`) | Leadership | tech lead; technical direction | — | 3 (1 M/I) |

<a id="type-domain"></a>
#### Domain knowledge (6)

*Non-technical. On a resume: Summary line plus bullets with domain outcomes.*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Domain expertise** (`domain_depth`) | Domain | domain expertise; subject-matter expertise; SME | — | 13 (2 M/I) |
| **Financial services** (`domain_finance`) | Domain | banking; insurance; fintech | — | 5 (0 M/I) |
| **Healthcare & life sciences** (`domain_healthcare`) | Domain | healthcare; pharma; clinical | — | 1 (0 M/I) |
| **Legal** (`domain_legal`) | Domain | legal tech | — | 1 (0 M/I) |
| **Manufacturing & industrial** (`domain_industrial`) | Domain | manufacturing; automotive; industrial | — | 2 (0 M/I) |
| **Public sector & government** (`domain_public_sector`) | Domain | government | — | 3 (0 M/I) |

<a id="type-research-craft"></a>
#### Research craft (4)

*Non-technical. On a resume: Publications section and bullets (venues, citations, reproductions).*

| Skill | Category | Posting wording (aliases) | Relations | Roles listing it |
|---|---|---|---|:---:|
| **Novel research & publications** (`research_novelty`) | Research | publications; first-author papers; NeurIPS; ICML; ICLR | — | 4 (2 M/I) |
| **Peer review** (`peer_review`) | Research | reviewing; programme committee | — | 3 (0 M/I) |
| **Research taste & problem selection** (`research_taste`) | Research | problem selection | — | 3 (3 M/I) |
| **Scientific writing** (`scientific_writing`) | Research | paper writing; technical reports | — | 6 (2 M/I) |
<!-- END GENERATED -->

---

## 4. Credentials

Credentials are tie-breakers, not skills. Their signal depends on the hiring channel [B/C · T0-11]. Retired credentials are tiered Avoid for new candidates; holders may still list them with the date.

<!-- BEGIN GENERATED: scripts/build_skills.py (credentials) -->
| Credential | Issuer | Level | Status | Roles that list it |
|---|---|---|---|:---:|
| **AWS Certified AI Practitioner (AIF-C01)** (`aws_aif_c01`) | AWS | foundational | active 2026-10-23: foundational; for people who work with AI rather than build it | 1 |
| **AWS Certified Machine Learning Engineer – Associate (MLA-C01)** (`aws_mla_c01`) | AWS | associate | active 2026-10-23: successor to the retired ML – Specialty | 2 |
| **AWS Certified Generative AI Developer – Professional (AIP-C01)** (`aws_aip_c01`) | AWS | professional | active 2026-10-23: generally available | 6 |
| **AWS Certified Machine Learning – Specialty** (`aws_mls_c01`) | AWS | specialty | retired 2026-03-31: last exam 2026-03-31; holders may list it with the date | 2 |
| **Microsoft AI-103 (Azure AI apps and agents)** (`ms_ai_103`) | Microsoft | associate | beta 2026-10-23: replaces AI-102; still marked beta | 3 |
| **Microsoft Azure AI Engineer Associate (AI-102)** (`ms_ai_102`) | Microsoft | associate | retired 2026-06-30: replaced by AI-103 | 1 |
| **Google Cloud Professional Machine Learning Engineer (PMLE)** (`gcp_pmle`) | Google Cloud | professional | active 2026-10-23: refreshed for generative AI; tie-breaker in GCP shops | 2 |
| **Google Cloud Generative AI Leader** (`gcp_genai_leader`) | Google Cloud | foundational | active 2026-10-23: non-technical literacy credential | 1 |
| **Databricks Certified Generative AI Engineer Associate** (`databricks_genai`) | Databricks | associate | active 2026-10-23: only if the target team runs Databricks | 1 |
| **NVIDIA-Certified Associate: Generative AI LLMs (NCA-GENL)** (`nvidia_nca_genl`) | NVIDIA | associate | active 2026-10-23: a cheap structured syllabus | — |
| **NVIDIA-Certified Professional: Generative AI LLMs (NCP-GENL)** (`nvidia_ncp_genl`) | NVIDIA | professional | active 2026-10-23: for LLM training or inference-infrastructure roles | 3 |
| **IAPP Artificial Intelligence Governance Professional (AIGP)** (`iapp_aigp`) | IAPP | professional | active 2026-10-23: the most-named AI-governance credential in T0-15 | 3 |
| **IAPP CIPP (privacy law, regional variants)** (`iapp_cipp`) | IAPP | professional | active 2026-10-23: privacy-law credential | 2 |
| **IAPP CIPM (privacy programme management)** (`iapp_cipm`) | IAPP | professional | active 2026-10-23: privacy-programme credential | 1 |
| **IAPP CIPT (privacy technologist)** (`iapp_cipt`) | IAPP | professional | active 2026-10-23: privacy-engineering credential | — |
| **ISACA CISA** (`isaca_cisa`) | ISACA | professional | active 2026-10-23: IT-audit credential; prerequisite route for AAIA | 2 |
| **ISACA Advanced in AI Audit (AAIA)** (`isaca_aaia`) | ISACA | advanced | active 2026-10-23: requires CISA, CIA or CPA | 1 |
| **ISACA CRISC** (`isaca_crisc`) | ISACA | professional | active 2026-10-23: IT-risk credential | 2 |
| **ISC2 CISSP** (`isc2_cissp`) | ISC2 | professional | active 2026-10-23: security credential | 2 |
| **Certified Kubernetes Administrator (CKA)** (`cka`) | CNCF / Linux Foundation | professional | not in the research corpus (practice-curated) | 2 |
<!-- END GENERATED -->

---

## 5. Watch List: Tools With a Notable Status

<!-- BEGIN GENERATED: scripts/build_skills.py (watch list) -->
| Item | Type | Status | As of | What it means for a resume |
|---|---|---|---|---|
| **Hugging Face TGI** | Framework / SDK | archived | 2026-03-21 | do not use for new deployments |
| **AutoGen** | Framework / SDK | dormant | 2026-10-23 | superseded by Microsoft Agent Framework 1.0 |
| **RAGAS** | Specialised product | dormant | 2026-10-23 | no release since Jan 2026, no commit since Feb 2026 — avoid new dependencies |
| **NVIDIA Dynamo Triton** | Framework / SDK | renamed | 2026-10-23 | formerly Triton Inference Server |
| **Langfuse** | Specialised product | acquired | 2026-01-16 | acquired by ClickHouse; MIT core, still viable |
| **Promptfoo** | Specialised product | acquired | 2026-03-09 | acquired by OpenAI — watch roadmap alignment |
| **OTel GenAI semantic conventions** | Protocol / standard | development | 2026-10-23 | still in Development — isolate behind adapters |
| **A2A (Agent2Agent)** | Protocol / standard | active | 2026-03-12 | v1.0; joining the Linux Foundation AAIF (announced 2026-08-27) |
| **AG-UI** | Protocol / standard | active | 2026-09-18 | 1.0 (CopilotKit); not in AAIF |
| **Arize Phoenix** | Specialised product | active | 2026-10-23 | Elastic License 2.0 (source-available, not OSI) — check licence fit |
| **Braintrust** | Specialised product | active | 2026-05-04 | breach on 2026-05-04 forced provider-key rotation — keep master keys out of SaaS eval tools |
| **DeepEval** | Specialised product | active | 2026-10-23 | active (64 releases a year); safe default CI eval runner |
| **LangChain** | Framework / SDK | active | 2025-10-17 | 1.0; legacy chains moved to a classic package |
| **LangGraph** | Framework / SDK | active | 2025-10-17 | 1.0 released; learn graph concepts, not chain syntax |
| **Microsoft Agent Framework** | Framework / SDK | active | 2026-04-02 | 1.0; supersedes AutoGen |
| **NVIDIA Dynamo** | Framework / SDK | active | 2026-10-22 | 1.6.0 (1.0 GA 2026-03-16); fronts vLLM, SGLang and TRT-LLM |
| **OpenAI Agents SDK** | Framework / SDK | active | 2026-03-23 | GA, native Temporal integration |
| **SGLang** | Framework / SDK | active | 2026-10-16 | 0.5.22; three critical CVEs in H1 2026 — sandbox template parsing |
| **TensorRT-LLM** | Framework / SDK | active | 2026-04-20 | 1.2.1 stable; static engine-build backend removed from v1.3 |
| **vLLM** | Framework / SDK | active | 2026-10-18 | 0.32.0, pre-1.0; CVE-2026-22778 and CVE-2026-27893 — pin and patch |
<!-- END GENERATED -->

---

## 6. Limits

- **Corpus counts are name matches, not demand.** They show where the research names a technology, not how often employers ask for it.
- **Most tool tiers are not measured.** Measured posting shares exist for only a few titles (JobsPipe) and for the senior- and infra-skewed S09 corpus. Job-description mining is the planned next step:
  - a dated sample of 30 or more postings per role;
  - it will give tools measured shares;
  - it will test completeness at 95% or more recall.
- **Statuses expire.** Tool statuses are class V2 facts under EGP-1.0 and must be re-verified within 90 days of 2026-10-23.
