---
id: "T0-69"
title: "Skill and Tool Momentum: What Is Rising and Falling, as Dated Series"
date: "2026-11-14"
status: complete-with-gaps
topic: "skill-tool-momentum-dated-series"
tags: ["skills-radar", "momentum", "agent-protocols", "mcp", "deprecations", "providers", "india", "emerging-titles"]
informs_decisions: ["D-004"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-14"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), via Claude Code. Anthropic products (MCP, Agent Skills, Claude Code, Claude models) are in scope, so rows about their adoption carry COI."
evidence_window: "2024-09-01 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 37
---

# T0-69: Skill and Tool Momentum: What Is Rising and Falling, as Dated Series

S-numbers (S1, S2 and so on) point to rows of the Sources & Evidence Ledger. Grades follow the protocol: A (primary page opened), B (established secondary or platform data with a method), C (vendor, single-source or undisclosed-method analysis, attributed), D (recalled or judgement), M (my arithmetic, inputs shown), P (practice-curated). The research date is 2026-11-14; the brief's temporal anchor is 2026-11-11, and a few sources dated 2026-11-09 to 2026-11-13 are included. Coverage is incomplete: two rounds of parallel research agents stopped on the account's usage limit before saving anything, so this report rests on 51 web searches and 68 page-fetch attempts (9 failed or refused) made directly by one researcher. Areas where I could not obtain two dated signals are listed under Absences, not filled from memory.

## Prior

| # | Proposition (held before searching) | Confidence | Grade |
|---|---|---|---|
| P1 | LangChain and LangGraph usage fell after the 1.0 reset, and the frameworks are a weak career signal. | 40% | D |
| P2 | MCP is the dominant agent-tool protocol and sits under neutral (Linux Foundation) governance. | 85% | D |
| P3 | AutoGen is dormant and superseded by Microsoft Agent Framework. | 80% | D |
| P4 | Hugging Face TGI is archived and TensorRT-LLM engine builds were removed. | 70% | D |
| P5 | Dedicated vector-database brands lost relevance to pgvector and cloud-native search. | 50% | D |
| P6 | OpenAI's share of LLM traffic is falling as multi-model use becomes standard. | 75% | D |

## Research Question

**Decision question.** Which GenAI skills, tools, frameworks and protocols are rising, stable or falling in employer demand and practitioner use, as dated series, and what should a job seeker learn first, keep or drop? This informs D-004, the skills radar, emerging roles, the skills ontology and the posting-share data file.

**Sub-questions.** (1) Which skill areas have two dated points from at least two independent signal types? (2) Which devalued-skill claims (K1–K10) survive? (3) Which tools were acquired, renamed, deprecated or went dormant since 2025-01-01? (4) What is the adoption evidence for agent protocols? (5) What does India show? (6) Which candidate titles (K11–K34) have real postings? (7) What should each role family learn, keep and drop?

**Reading chosen.** A skill counts as rising or falling only when two independent signal types move the same way between two dates. A single-date posting share is a level, not momentum. Posting shares measure employer demand, surveys measure self-reported use, downloads and registry counts measure installs and supply (including automated installs), and stars measure attention.

**Method.** I searched and fetched primary pages first (vendor documentation, repositories where the session allowed, release notes, specification text), then labour-market and developer-survey data, then vendor reports (graded C). The session's URL allowlist refused GitHub repository pages for TGI and RAGAS and the RAGAS PyPI page, so those two verdicts rest on a documentation page plus a release aggregator. Falsification searches: (a) evidence that LangChain/LangGraph usage is rising (found: installs and posting presence); (b) evidence that vector-database brands still carry signal (found: DB-Engines scores); (c) evidence that RAGAS is dormant (found the opposite: a release candidate on 2026-11-13); (d) a trace of the K10 provider-share figures to their original report (found: Datadog, 2026-04-21); (e) a trace of the K1 and K2 counts to their original studies (found: two arXiv papers); (f) exact-title searches for each quarantined or never-measured title.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Five tool-status claims hold on primary pages: TGI is in maintenance mode (no date shown; Hugging Face recommends vLLM, SGLang and llama.cpp/MLX); TensorRT-LLM removed the TensorRT backend, `trtllm-build`, `trtllm-refit` and `trtllm-prune` and runs on PyTorch only (page updated 2026-11-03); `autogen-agentchat` last shipped on PyPI on 2025-09-30 (none in the 365 days to 2026-11-13); torchtune is "no longer actively maintained"; the OpenAI Assistants API was sunset on 2026-08-26. | [S38] [S23] [S36] [S57] [S44] | A |
| KF2 | RAGAS is not dormant: v0.4.3 (2026-01-13) was followed by v0.4.4rc1 on 2026-11-13 under the vibrantlabsai GitHub organisation (aggregator page; GitHub and PyPI pages were refused). The TGI archive date 2026-03-21 rests on one secondary source. | [S37] [S39] | B |
| KF3 | Eval and observability vendors are consolidating: seven tools were acquired or closed between 2025-05-05 and 2026-05-22 (W&B Weave, Humanloop, Langfuse, Helicone, Promptfoo, Traceloop, Galileo). OpenAI (2026-03-09) and Langfuse confirm two on their own pages; the other dates come from a secondary roundup. | [S25] [S26] [S28] | B |
| KF4 | Multi-provider use is the norm. Datadog telemetry: OpenAI share 75% to 63% and more than 70% of organisations using three or more models. Langfuse Cloud traces: OpenAI 82.7% (2024-10) to 55.3% (2025-09). A gateway: OpenAI used by 70 of 100 paid teams (2025-12) to 55 (2026-10), Anthropic 48 to 54. An a16z CIO survey (n=100): 81% use three or more model families, up from 68%. | [S15] [S13] [S14] [S12] | B |
| KF5 | MCP is rising on governance and supply, but its specification is volatile. The Agentic AI Foundation reported 146 members on 2026-02-24; the 2026-07-28 revision removes protocol sessions, deprecates Roots, Sampling, Logging, HTTP+SSE and Dynamic Client Registration; the official registry held 30,375 unique servers on 2026-09-10 (about 3x May 2026), of which 62% have one version and about 36% were not updated in three months. COI. | [S29] [S30] [S32] | B |
| KF6 | Agent frameworks as a class are rising, but production practice is split. Datadog: adopting organisations rose from more than 9% to almost 18% (early 2025 to early 2026). An arXiv study found 85% (17 of 20) of interviewed teams built custom loops, yet 61% of its surveyed deployed agents used frameworks. On one agentic job board LangChain is named in 34.3% and LangGraph in 22.1% of 534 listings (2026-04-19); AutoGen in 7.9%. | [S15] [S20] [S22] | B |
| KF7 | JobsPipe's AI Engineer shares are dated 2026-09-10 (the count date), not 2026-11-02: Python 78.4%, LLM 76.7%, agentic AI 59.3%, RAG 54.0%, vector databases 32.6%, prompt engineering 31.1%. The page was unchanged on 2026-11-14, so these are levels at one date, not a series. | [S1] [S2] | B |
| KF8 | India: Naukri's AI-ML index grew 49% YoY in February 2026, 22% in May, 25% in June and 20% in September, while IT and software services moved from +6% to −7%, −3% and −4%. Indeed India: AI mentions in postings 8.2% (2024-09), 10.6% (2025-06), 11.7% (2025-09); software-development postings −12.3% over three months to about May 2026. Two independent platforms agree: AI up, generic software down, demand skewed to experience. | [S7] [S8] [S9] [S10] [S61] [S62] | B |
| KF9 | Coding agents are rising as a class. JetBrains: Claude Code work adoption about 3% (2025 Q2) to 18% (2026-01), Copilot 29% and "stalled". Stack Overflow: agent use 30.9% (2025); 66% of AI users use coding agents (2026), with different denominators. COI for Claude Code. | [S65] [S3] [S5] | B |
| KF10 | TypeScript is the fastest-growing major language on GitHub (2,636,006 monthly contributors in 2025-08, +66.63% YoY, ranked first); Python grew 48.78% there yet is flat in Stack Overflow's survey (57.9% in 2025, 58% in 2026) and named in 78.4% of AI Engineer postings. | [S6] [S3] [S5] [S1] | B |
| KF11 | "Commoditised by brand" is not supported for vector databases by popularity data: DB-Engines scores (Dec 2024 to Dec 2025) rose from 3.24 to 7.95 (Pinecone), 1.84 to 4.39 (Qdrant), 1.70 to 4.18 (Weaviate), 2.81 to 5.00 (Milvus). Posting data name the category ("vector databases", 32.6% of AI Engineer postings), not brands. | [S40] [S1] | M |
| KF12 | Governance and security demand is single-date and regulation-timed. The EU omnibus moves Annex III high-risk obligations from 2026-08-02 to 2027-12-02 (provisional agreement 2026-05-07; final adoption not verified); BSI issued its 50th ISO/IEC 42001 certificate on 2026-10-21 (11 in 2025); SANS counted more than 850 AI/ML security-engineer postings and about 430 AI governance, risk and compliance leads in mid-September 2026. | [S45] [S63] [S64] | B |
| KF13 | Titles: exact-title postings exist for Agent Architect (2), Distributed Training Engineer (OpenAI, Periodic Labs), Edge AI Engineer (at least 9 listings on one aggregator) and AI developer advocate roles at 6 employers. None found for Prompt Wizard, AI Whisperer, Transformer Specialist, Neural Network Designer, Cognitive Architect or Context Architect. Title counts were unavailable, so no title passes the volume test on evidence. | [S49]–[S54] | C |
| KF14 | Voice is rising provisionally: voice-model use among paid gateway teams about 4% (2026-07) to about 11% (2026-10); LiveKit raised $100M at a $1B valuation (2026-01-22, company-stated). | [S14] [S59] | C |

## Recommendation

Decision rules for a job seeker (grades in Detailed Findings):

1. **Learn concepts first, one framework second.** Build one agent with no framework (custom loop, tool schemas, retries) and one with LangGraph or Microsoft Agent Framework; name the framework in the CV, show the loop in the repository. Failure mode: a concept-only CV can fail keyword filters, so name the tools.
2. **Learn the 2026-07-28 MCP specification, not the 2025 tutorials.** Stateless requests, `server/discover`, multi round-trip requests, and Client ID Metadata Documents for client registration. Avoid building on Roots, Sampling, Logging or HTTP+SSE (deprecated, 12-month minimum window). Failure mode: the specification keeps changing; pin a version and read the changelog.
3. **Make evaluation and tracing portable.** Practise offline and online evals, LLM-as-judge with human review, and OpenTelemetry/OTLP-based tracing; treat any single eval or observability brand as replaceable (seven tools changed hands or closed in 13 months). Failure mode: methodology is hard to prove without a platform; keep a public eval harness in a repository.
4. **Build provider independence into every project.** Two providers, a routing or fallback layer, cost accounting. Failure mode: abstraction layers add latency and lowest-common-denominator features.
5. **Drop or deprioritise** Assistants API, TGI, `trtllm-build` engine compilation, torchtune recipes, AutoGen-specific code, and framework syntax as a headline skill. Failure mode: legacy systems still run these, so keep them only for maintenance roles.
6. **India.** Aim at AI/ML roles with 8–16 years' experience or GCC employers if senior; if early-career or in generic IT services, add AI-specific proof, because Naukri and Indeed both show software and IT-services demand falling. Failure mode: Naukri's index counts postings and recruiter searches, not hires, and free listings inflate it.
7. **Judge titles by skills.** Search postings by skill set; do not rebuild a CV around quarantined labels (Prompt Wizard, AI Whisperer and similar had no exact postings in my searches).

What would change these rules: a second dated posting series for agentic AI, RAG or MCP (a fall of 25% or more would move them from rising to stable); an MCP and A2A convergence announcement; final EU adoption or further delay of the omnibus; a deprecation notice for LangGraph or Microsoft Agent Framework; a RAGAS or Promptfoo licence change.

## Alternatives Considered

| Option | Why preferred or rejected | Failure mode if chosen |
|---|---|---|
| Rank tools by GitHub stars or downloads | Rejected as a primary signal: stars measure attention, downloads include CI and mirrors. Used only as a second signal. | Over-weights hyped repositories. |
| Treat JobsPipe's 12 title pages as a time series | Rejected: the page date is 2026-09-10 and unchanged on 2026-11-14, so there is one date. | A false "surging" ring. |
| Lean on vendor surveys (LangChain, Datadog, Ramp) | Used, graded B or C, with COI noted. | Customer bases skew to the vendor's users. |
| Frameworks-first learning path | Rejected as default: class adoption is rising but 17 of 20 interviewed production teams used custom loops. | Framework churn (AutoGen, torchtune) strands skills. |
| Concepts-first, tool second (recommended) | Preferred: durable concepts (evaluation, retrieval quality, tool schemas) outlive tools. | Keyword-filter misses; mitigate by naming tools. |


## Detailed Findings

Section map: KF1–KF3 sit in sections 5 and 6; KF4 in 2.8; KF5 in 2.1 and 7; KF6 in 2.2; KF7 in 3; KF8 in 8; KF9 in 2.7; KF10 in 2.11; KF11 in 2.3; KF12 in 2.10; KF13 in 9; KF14 in 2.9. Section 4 holds the classification tables, section 10 the learn, keep and drop lists.

### 1. How the series and calls were built

Each series table has one row per dated data point: skill or tool, signal type, date, value, source and grade. Signal types are kept apart: posting share (employer demand), survey use share (self-reported use), telemetry share (use seen by an observability or gateway vendor), transactions (card and bill-pay spend), downloads (installs, including automated ones), stars and popularity scores (attention), registry counts (supply), and events (announcements, releases, deprecations). Pages marked Read in the ledger were opened with a fetch tool that returns a model-written summary of the page, so figures were checked against that summary and not against raw page text; maintainers should re-check load-bearing figures at the source.

**Call rule (grade D, my own).** A skill is *rising* or *falling* when two independent signal types move the same way between two dates by about 25% or more (about 3 percentage points or more for surveys), or when a deprecation is confirmed on a primary page and one more signal agrees. A call with one dated signal type is written *lean rising* or *lean falling* and should not move a skill between rings on its own. A level at one date is not momentum. A skill with no usable signal is *unclassified*.

### 2. Series by skill area

#### 2.1 Agent protocols (MCP, A2A, AG-UI)

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| MCP | governance | 2026-02-24 | Agentic AI Foundation (AAIF, Linux Foundation): 146 members, of which 97 are new Gold and Silver members since launch; eight Platinum founders; hosts MCP, goose and AGENTS.md | [S29] | A, COI |
| MCP | official announcement | 2026-01-26 | MCP Apps launched as the first official MCP extension; clients named: ChatGPT, Claude, goose, VS Code | [S29] | A, COI |
| MCP | specification | 2025-11-25 to 2026-07-28 | Revision 2026-07-28 removes protocol-level sessions and the `initialize` handshake; adds `server/discover`, `subscriptions/listen` and multi round-trip requests; moves tasks to an extension; deprecates Roots, Sampling, Logging, HTTP+SSE and Dynamic Client Registration; sets a 12-month minimum deprecation window | [S30] | A, COI |
| MCP | registry supply (unique servers) | 2026-05 (author's figure; day not stated) | about 9,650 | [S32] | C, COI |
| MCP | registry supply (unique servers) | 2026-09-10 | 30,375 unique servers from 99,114 server-version records; 62% have one version; about 36% not updated in three months or more; 1.1% (332) deprecated. One author's pull of the official registry API | [S32] | C, COI |
| MCP | registry supply (servers first published per month) | 2025-09; 2026-02; 2026-04; 2026-06; 2026-07; 2026-08 | 407; 1,081; 2,387; 3,662; 4,840; 6,265 | [S32] | C, COI |
| MCP | repository attention | window ending 2025-08 (report 2025-10-28) | GitHub states the MCP repository reached 37 thousand stars in eight months | [S6] | B, COI |
| MCP | posting mention | 2026-04-19 | named in 36 of 213 LangChain-ecosystem listings (16.9%) on one agentic job board; one date only | [S22] | C |
| A2A | adoption (supporting organisations) | 2025-04; 2026-04-09 | more than 50; more than 150 (stated by the Linux Foundation project) | [S33] | C |
| A2A | specification | 2026-04-09 | v1.0, described as the first stable specification; SDKs in Python, JavaScript, Java, Go and .NET | [S33] | A |
| A2A | vendor support | 2026-04-09; 2026-04-03 | Azure AI Foundry, Copilot Studio and AWS Bedrock AgentCore Runtime named in the press release; trade press reports Microsoft Agent Framework A2A 1.0 support as "coming soon" | [S33] [S35] | C; B |
| AG-UI | any | none | no source obtained (not searched) | none | see Absences |

Calls: MCP **rising** on supply and governance (registry counts and AAIF membership are different signal types, each with two dates); no employer-demand series exists for MCP. A2A **lean rising** (one signal type, stated by the project).

#### 2.2 Agent frameworks and SDKs

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Agent frameworks (class) | telemetry share of organisations | early 2025 to early 2026 (report 2026-04-21) | more than 9% to almost 18% of organisations; services using agentic frameworks more than doubled | [S15] | B |
| Agent frameworks (class) | survey of deployed agents | fieldwork 2025-07-28 to 2025-10-29 | 61% use frameworks; LangChain/LangGraph 25.0%, CrewAI 10.7%, LlamaIndex 3.6%, OpenAI Swarm 3.6% | [S20] | B |
| Custom loops | interviews | study April to November 2025 | 17 of 20 interviewed teams (85%) used custom in-house implementations; two teams moved from CrewAI to custom | [S20] | B |
| LangChain | posting share (agentic listings) | 2026-04-19 | 34.3% (183 of 534) | [S22] | C |
| LangGraph | posting share | 2026-04-19 | 22.1% (118 of 534) | [S22] | C |
| LlamaIndex; CrewAI; AutoGen | posting share | 2026-04-19 | 13.9% (74); 10.9% (58); 7.9% (42) | [S22] | C |
| n8n; Semantic Kernel; Pydantic AI | posting share | 2026-04-19 | 3.4% (18); 2.4% (13); 2.4% (13) | [S22] | C |
| LangChain | downloads (vendor statement) | 2025-10-22 | "90M monthly downloads" (month and counter not stated) | [S55] | C |
| LangChain | downloads (pepy.tech, last 30 days) | 2026-11-11 | 157,554,330 (all-time 3,484,648,401); counts installs including CI and mirrors | [S41] | B |
| LangGraph | downloads (pepy.tech, last 30 days) | 2026-11-11 | 58,965,017 (all-time 667,975,165) | [S42] | B |
| AutoGen (`autogen-agentchat`) | repository activity (PyPI releases) | 2025-09-30 to 2026-11-14 | last release 0.7.5 on 2025-09-30; 54 releases in all; none in the 12 months to 2026-11-13; 410 days to 2026-11-14 (my count) | [S36] | A |
| Microsoft Agent Framework | releases | 2026-02-19; 2026-04-03 | release candidate; 1.0 production-ready for .NET and Python, described as the successor to Semantic Kernel and AutoGen; AutoGen still receives bug and critical security fixes | [S34] [S35] | A; B |
| OpenAI Assistants API | status | 2026-08-26 | sunset; Responses API and Conversations API replace it | [S44] | A |
| LangChain 1.0 | release | 2025-10-22 | `create_agent` and middleware; legacy chains moved to `langchain-classic`; LangGraph prebuilt agents deprecated; no breaking changes promised before 2.0 | [S55] | A |

The two LangChain download figures come from different counters, so no change between them is computed. Calls: framework class **lean rising** (one dated signal type); AutoGen **falling**; Assistants API **gone**.

#### 2.3 Retrieval and vector stores

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| RAG | posting share (AI Engineer) | 2026-09-10 | 54.0% | [S1] | B |
| Vector databases (category) | posting share (AI Engineer) | 2026-09-10 | 32.6% | [S1] | B |
| Pinecone | popularity score (DB-Engines vector DBMS) | 2024-12 to 2025-12 | 3.24 to 7.95 (+145%) | [S40] | M |
| Weaviate | popularity score | 2024-12 to 2025-12 | 1.70 to 4.18 (+146%) | [S40] | M |
| Qdrant | popularity score | 2024-12 to 2025-12 | 1.84 to 4.39 (+139%) | [S40] | M |
| Milvus | popularity score | 2024-12 to 2025-12 | 2.81 to 5.00 (+78%) | [S40] | M |
| Chroma | popularity score | 2024-12 to 2025-12 | 1.87 to 2.57 (+37%) | [S40] | M |
| OpenSearch | popularity score | 2024-12 to 2025-12 | 17.19 to 19.79 (+15%) | [S40] | M |
| Couchbase | popularity score | 2024-12 to 2025-12 | 15.82 to 11.39 (−28%) | [S40] | M |
| Elasticsearch | popularity score | 2024-12 to 2025-12 | 132.32 to 109.83 (−17%) | [S40] | M |
| MongoDB | popularity score | 2024-12 to 2025-12 | 400.38 to 372.27 (−7%) | [S40] | M |

The December 2025 scores are read from the page; the December 2024 scores and the percentage changes are my arithmetic from the page's change columns (±0.01). The page I fetched on 2026-11-14 held the December 2025 ranking, not a later one. DB-Engines scores measure popularity (mentions, searches, job offers and similar), not usage. pgvector and Redis are not on the page. Call: dedicated vector-database brands **lean rising** on popularity; brand-level employer demand is unmeasured.

#### 2.4 Evaluation and observability

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Offline evals; online evals | survey (vendor-run, 1,340 responses) | fieldwork 2025-11-18 to 2025-12-02 | 52.4%; 37.3%; any observability 89%; detailed tracing 62% | [S21] | C |
| Human-in-the-loop evaluation; LLM-as-judge | survey of deployed agents | fieldwork 2025-07-28 to 2025-10-29 | 74.2% (N=31); 51.6%; 75% of interviewed teams evaluate without a formal benchmark set | [S20] | B |
| RAGAS | repository activity (releases, aggregator page) | 2025-10-14; 2026-01-13; 2026-11-13 | v0.3.7; v0.4.3; v0.4.4rc1 (release candidate); 304 days between the last two (my count) | [S37] | B |
| Eval and observability brands | events | 2025-05-05 to 2026-05-22 | seven tools acquired or closed (section 6) | [S25] [S26] [S28] | B |
| LLM observability (Datadog) | vendor report | 2026-04-21 | recommends online evaluations; gives no quantified evaluation results | [S15] | B |

Calls: evaluation as a practice **lean rising** (survey levels at one date each, plus market validation by deals); any single eval or observability brand is replaceable.

#### 2.5 Serving engines and inference optimisation

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| TGI | status notice | undated (page opened 2026-11-14) | Hugging Face documentation carries a maintenance-mode notice (pull requests only for minor fixes, documentation and lightweight maintenance) and recommends vLLM, SGLang and llama.cpp or MLX | [S38] | A |
| TGI | event | 2026-03-21 | read-only archive; maintenance mode dated 2025-12; one secondary source; GitHub banner not opened | [S39] | C |
| TensorRT-LLM | status | documentation page updated 2026-11-03 | TensorRT backend, `trtllm-build`, `trtllm-refit`, `trtllm-prune` and per-model `convert_checkpoint.py` removed; PyTorch is the sole backend; replacement is `tensorrt_llm.LLM(model=hf_model)` and `trtllm-serve` | [S23] | A |
| TensorRT-LLM | repository activity | release candidates 1.3.0rc26 to rc29 (month and day shown, year not) | rc28 notes list removal of deprecated TensorRT serve, evaluation, benchmark and stress paths (breaking); no stable 1.3.0 in the part of the page I read | [S24] | A (partial read) |
| vLLM | governance and attention | 2025-05-07 | joined the PyTorch Foundation; more than 46,500 GitHub stars and more than 1,000 contributors | [S43] | A |
| vLLM; SGLang | official recommendation | undated | named by Hugging Face as TGI replacements | [S38] | A |
| llama.cpp | stars | 2026-10-07 | about 130,500 | [S58] | C |
| Ollama | stars | 2026-10-07 | about 182,400; v0.40.0 released 2026-09-25 | [S58] | C |

No second dated star or download count was obtained for vLLM, SGLang, llama.cpp or Ollama, and no posting share for any serving engine. Calls: TGI **falling**; TensorRT-LLM engine compilation **gone**; vLLM and SGLang **lean rising**; llama.cpp and Ollama **unclassified**.

#### 2.6 Fine-tuning and post-training

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| TRL | release | 2026-03-31 | v1.0: more than 75 post-training methods; stable core for SFT, DPO, reward modelling, RLOO and GRPO | [S56] | A |
| TRL | downloads (vendor statement) | 2026-03-31 | "3 million times a month"; comparison table shows 3.0M PyPI downloads a month and 17.8 thousand stars | [S56] | C |
| torchtune | status | README, undated | no longer actively maintained; development wound down in 2025 | [S57] | A |
| Fine-tuning practice | survey (vendor-run) | fieldwork 2025-11-18 to 2025-12-02 | 57% of respondents not fine-tuning | [S21] | C |

Calls: TRL **lean rising** (a stable 1.0 API; no dated demand series); torchtune **falling**. No posting share for post-training skills was obtained.

#### 2.7 Coding agents

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Claude Code | survey, awareness (JetBrains AI Pulse) | 2025 Q2 (April to June); 2025-09; 2026-01 | 31%; 49%; 57% | [S65] | B, COI |
| Claude Code | survey, work adoption | 2025 Q2; 2026-01 | about 3%; 18% (1.5 times the September 2025 level; 24% in the US and Canada) | [S65] | B, COI |
| GitHub Copilot | survey, work adoption | 2026-01 | 29%; growth stalled since the previous year; 40% at companies with more than 5,000 employees | [S65] | B |
| Cursor; OpenAI Codex; Google Antigravity; JetBrains AI Assistant; Junie | survey, work adoption | 2026-01 | 18%; 3% (before the Codex desktop app launch); 6%; 9%; 5% | [S65] | B |
| AI coding tools (class) | survey | fieldwork April to June 2025 | 85% of 24,534 developers regularly use AI; 62% use at least one AI coding assistant, agent or editor | [S66] | B |
| AI tools (class) | survey | 2024; 2025 | use or plan to use: 76%; 84% (49,000+ respondents in 2025) | [S3] | B |
| AI agents | survey | 2025 | 30.9% use agents (14.1% daily); 17.4% plan to; 37.9% do not plan to | [S3] | B |
| Coding agents | survey | 2026 (published 2026-10-06) | 66% of AI users use coding agents and 63% chatbots; 73% of AI coding-assistant and agent users use them daily; the page also states Claude Code 66% and GitHub Copilot 59% without a clear denominator | [S5] | B; C for the tool figures; COI for Claude Code |
| GitHub Copilot coding agent | vendor statement | 2025-05 to 2025-09 | more than 1 million pull requests | [S6] | C |

Denominators differ between the 2025 and 2026 Stack Overflow figures, so no like-for-like change is computed. Calls: coding agents as a class **rising** (JetBrains adoption and Stack Overflow agent use, different denominators); Claude Code **rising** (COI); GitHub Copilot **stable** (growth stalled).

#### 2.8 Providers and models (K10)

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Provider mix | telemetry share (Datadog, more than 1,000 customers) | year to 2026-04-21 | OpenAI share 75% to 63% (the unit is not named in the text I read; OpenAI customers more than doubled); Anthropic +23 percentage points; Google Gemini +20 percentage points | [S15] | B |
| Multi-model use | telemetry | 2026-04-21 | more than 70% of organisations use three or more models; the share using more than six models nearly doubled | [S15] | B |
| Provider mix | traced traffic (Langfuse Cloud, more than 20,000 organisations, self-hosted excluded) | 2024-10 to 2025-09 | OpenAI 82.7% to 55.3%; Google 0.5% to 13.1%; Anthropic 6.8% to 7.3%; other 10.0% to 24.3% | [S13] | B |
| Provider mix | paid teams using each lab (Vercel AI Gateway) | 2025-12 to 2026-10 | OpenAI 70 to 55 of 100; Anthropic 48 to 54; OpenAI share of spend about 9 to about 15 cents per dollar | [S14] | B, COI |
| Model churn | gateway usage | 2026-10 | model half-life about six weeks; median model version replaced every 61 days; more than half of language-model requests went to models under 60 days old | [S14] | B |
| Multi-model use | survey of CIOs (a16z, n=100; undated) | a year apart | 81% use three or more model families, up from 68% | [S12] | C, COI |
| Business adoption | card and bill-pay transactions (Ramp, more than 85,000 US businesses) | 2026-01 to 2026-10 | any paid AI 46.8% to 56.8%; Anthropic 19.5% to 44.8% (16.7% in 2025-12); OpenAI 35.9% to 40.6% (36.8% in 2025-12) | [S16] [S17] [S18] | B, COI |
| Multi-vendor payers | transactions (Ramp) | 2025-01; 2026-01 | businesses paying for both OpenAI and Anthropic: 8%; 16% | [S17] | B, COI |
| Token spend share (weekly) | transactions (Ramp) | weeks ending 2026-10-04; 2026-11-01 | Anthropic 53.2% to 49.3%; OpenAI 42.3% to 46.1% | [S16] | B, COI |
| Models used | survey (Stack Overflow) | 2025 | OpenAI GPT 81.4%, Claude Sonnet 42.8%, Gemini Flash 35.3%, OpenAI reasoning 34.6%, Gemini reasoning 25.6%, DeepSeek reasoning 23.3%, Llama 17.8%, Mistral 10.4% | [S4] | B |

OpenAI's share of traffic falls in three sources while its share of businesses paying rises in Ramp's data. These are different measures (traffic share against the share of businesses with any spend), so they do not contradict each other. Calls: multi-provider use **rising** (survey, transactions and telemetry, each with two dates; B, COI for Ramp); single-provider chat wrappers remain **devalued**.

#### 2.9 Voice, multimodal and on-device

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Voice models | gateway usage (Vercel; figures begin 2026-06-22) | 2026-07; 2026-10 | share of paid teams using a voice model about 4%; about 11% (10.7% in the chart); among teams paying in both months 5% to 14% | [S14] | B |
| Voice AI | funding (company-stated) | 2026-01-22 | LiveKit $100M Series C at a $1B valuation; more than 200,000 developers and customers | [S59] | C |
| Voice AI engineers | job board | 2026-11-14 | a voice-AI engineering job board exists; no count obtained | [S68] | C |
| On-device and edge | listings seen | 2026-11-14 | at least 9 distinct "Edge AI Engineer" listings on one aggregator; Deepgram "Embedded AI Engineer, On-Device Models"; other on-device and edge-device engineer listings | [S52] | C |
| Multimodal (other than voice) | any | none | not searched | none | see Absences |

Calls: voice **lean rising** (one gateway's usage plus funding, which are different signal types but the usage series is short); on-device and edge **unclassified** (listings at one date).

#### 2.10 AI security and governance

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| AI/ML security engineers | posting count (SANS tracker) | mid-September 2026 (published 2026-10-20) | more than 850 postings | [S64] | B |
| AI red team | posting count | mid-September 2026 | about 100 postings; +13% week on week | [S64] | B |
| AI governance, risk and compliance leads | posting count | mid-September 2026 | about 430 postings | [S64] | B |
| AI supply-chain security; AI security specialists; AI SOC orchestrators | posting count | mid-September 2026 | 93; 48; 36 postings | [S64] | B |
| ISO/IEC 42001 | certificates (BSI) | 2025 (calendar year); 2026-10-21 | BSI issued 11 certificates in 2025; the 50th certificate was awarded on 2026-10-21; certified organisations in more than 16 countries, India among them | [S63] | A |
| EU AI Act (Annex III high-risk obligations) | rule timing | 2026-05-07 to 2026-06-22 | provisional agreement to move them from 2026-08-02 to 2027-12-02; Annex I systems to 2028-08-02; transparency and watermarking to 2026-12-02 for systems placed on the market before 2026-08-02; Parliament adopted on 2026-06-16; Council approval pending on 2026-06-22; final adoption not verified | [S45] | B |

Call: **lean rising** for AI security and governance demand (posting counts at one date, certificate counts with an uneven base); regulation timing moved out by 16 months for Annex III (my count). Not enough to classify momentum.

#### 2.11 Programming languages and clouds

| Skill | Signal type | Date | Value | Source | Grade |
|---|---|---|---|---|---|
| Python | survey use share (Stack Overflow, all respondents) | 2025; 2026 | 57.9% (+7 percentage points on 2024); 58% | [S3] [S5] | B |
| JavaScript | survey | 2025; 2026 | 66%; 62% | [S4] [S5] | B |
| SQL | survey | 2025; 2026 | 58.6%; 58% (second place in 2026, ahead of HTML/CSS) | [S3] [S5] | B |
| TypeScript | survey | 2025 | 43.6%; no 2026 figure on the page | [S4] | B |
| TypeScript | GitHub activity (Octoverse) | 2024-08 to 2025-08 | 2,636,006 monthly contributors, +66.63% year on year, ranked first | [S6] | B |
| Python; JavaScript | GitHub activity | 2024-08 to 2025-08 | monthly contributors +48.78%; +24.79% | [S6] | B |
| TypeScript | survey (JetBrains) | fieldwork April to June 2025 | largest five-year rise among languages | [S66] | B |
| Rust | survey | 2025; 2026 | 14.8%; twelfth most used (percentage not on the page) | [S4] [S5] | B |
| LLM SDK imports | GitHub activity | 2024-08 to 2025-08 | more than 1.1 million public repositories import an LLM SDK, +178% year on year; 693,867 created in the 12 months | [S6] | B |
| AWS; Azure; GCP | survey | 2025 | 43.3%; 26.3%; 24.6% | [S4] | B |
| Python | posting share (AI Engineer) | 2026-09-10 | 78.4% | [S1] | B |
| AWS; Azure | posting share (AI Engineer) | 2026-09-10 | 35.1% each | [S1] | B |

Stack Overflow's 2025 and 2026 samples differ in size (49,000+ and more than 30,000 respondents), and the 2026 figures are whole numbers, so differences of one point or less are within rounding. Calls: TypeScript **rising** (GitHub activity and JetBrains survey); Python **stable** (survey flat in 2026 after +7 points in 2025; GitHub contributors rose, partly because the contributor base grew); JavaScript **lean falling** (one survey pair, 4 points); clouds **unclassified** (no two-date series).

### 3. Posting shares at one date

JobsPipe AI Engineer page, as of 2026-09-10: active postings from ten job boards, deduplicated by posting ID, grouped by canonical title and counted on that date; a posting counts once for each skill it names, so shares overlap; skills are matched against a curated lexicon; the sample size is not stated. The page showed the same figures on 2026-11-14, so these are levels at one date, not a series. The page also lists 3,944 live AI Engineer postings across 30+ sources (undated).

| Skill | Share of AI Engineer postings (as of 2026-09-10) | Source | Grade |
|---|---|---|---|
| Python | 78.4% | [S1] | B |
| LLM | 76.7% | [S1] | B |
| Agentic AI | 59.3% | [S1] | B |
| RAG | 54.0% | [S1] | B |
| Machine learning | 39.8% | [S1] | B |
| AI | 37.8% | [S1] | B |
| Generative AI | 37.6% | [S1] | B |
| Azure; AWS | 35.1%; 35.1% | [S1] | B |
| CI/CD | 34.4% | [S1] | B |
| Vector databases | 32.6% | [S1] | B |
| Prompt engineering | 31.1% | [S1] | B |

Other shares on the page: remote 11.0%; pay disclosed 19.6%; senior 24.6%; entry 7.0%; mid 6.0%; lead or manager 5.6%; full-time 77.6% of postings that state a type. The 2026-04-19 framework shares (LangChain 34.3% and others) are in section 2.2 and come from a different, smaller source (534 listings on one agentic job board, tagging method not described).

### 4. Classification

Calls follow the rule in section 1. "Signals" names the signal types and dates behind the call.

#### 4.1 Durable concepts

| Concept | Call | Signals | Grade |
|---|---|---|---|
| Provider independence and routing | rising | survey of CIOs (68% to 81% on three or more model families); transactions (8% to 16% paying for both OpenAI and Anthropic, 2025-01 to 2026-01); telemetry (more than 70% of organisations on three or more models, share above six models nearly doubled) | B (COI for Ramp) |
| Evaluation methodology (offline and online evals, LLM-as-judge with human review) | lean rising | two surveys at one date each (52.4% offline and 37.3% online; 74.2% human-in-the-loop and 51.6% LLM-as-judge); seven eval and observability deals; no posting share | C |
| Tracing and observability (OpenTelemetry-compatible) | lean rising | 89% any observability and 62% detailed tracing (one date); MCP revision 2026-07-28 adds OpenTelemetry trace context to `_meta`; W&B Weave accepts OTLP | C |
| Retrieval quality and RAG | stable at a high level | RAG in 54.0% and vector databases in 32.6% of AI Engineer postings (one date); vector-store popularity up (see 2.3) | B; M |
| Tool schemas and tool calling | rising (carried by MCP) | registry supply and governance growth under MCP; A2A as a complement | B, COI |
| Agent loop design (custom loops, retries, human review) | lean stable | 17 of 20 interviewed production teams used custom loops; 68% of deployed agents run fewer than 10 steps before human intervention (N=60); one study | B |
| Prompt design as a baseline skill | stable as a skill; lean falling as a title | named in 31.1% of AI Engineer postings (2026-09-10); title evidence is 72 of 20,662 (0.35%) from a sample of 2024–25 vintage | B; M |
| AI security and governance (red teaming, supply chain, ISO/IEC 42001) | lean rising | posting counts at one date (SANS), certificate counts (BSI), regulation dates moved | B |

#### 4.2 Fast-moving tools and protocols

| Tool or protocol | Call | Signals | Grade |
|---|---|---|---|
| MCP | rising (supply and governance); specification volatile | registry 9,650 to 30,375 servers (2026-05 to 2026-09-10); AAIF 97 new Gold and Silver members to 146 (2026-02-24); 16.9% of LangChain-ecosystem listings (one date) | B for governance, C for registry; COI |
| A2A | lean rising | more than 50 to more than 150 organisations (2025-04 to 2026-04-09), project-stated | C |
| AG-UI | unclassified | none obtained | none |
| Agent frameworks (class) | lean rising | Datadog adoption more than 9% to almost 18%; survey and postings at one date | B |
| LangChain and LangGraph | unclassified at brand level (stable presence) | pepy.tech last-30-day installs at one date; 34.3% and 22.1% of one board's agentic listings; the vendor's 90M statement uses another counter | C |
| Microsoft Agent Framework | lean rising (new) | release candidate 2026-02-19, 1.0 on 2026-04-03; not among the frameworks counted on the job board | B |
| AutoGen | falling | no PyPI release since 2025-09-30 (410 days to 2026-11-14); named successor; 7.9% of one board's listings | A |
| CrewAI | unclassified | 10.9% of listings (one date); 10.7% of surveyed deployed agents; two interviewed teams moved to custom | C |
| OpenAI Assistants API | gone | sunset 2026-08-26 | A |
| Dedicated vector-database brands | lean rising | DB-Engines popularity up 37% to 146% (2024-12 to 2025-12), no brand-level posting share | M |
| Eval and observability brands | independence falling; replaceable | seven acquisitions or closures, 2025-05-05 to 2026-05-22 | B |
| RAGAS | stable (active) | release candidate 2026-11-13 after 304 days | B |
| TGI | falling | maintenance-mode notice on the vendor's page; archive 2026-03-21 from one secondary | A; C |
| TensorRT-LLM engine compilation | gone | removal documented, page updated 2026-11-03 | A |
| vLLM; SGLang | lean rising | PyTorch Foundation 2025-05-07; named as TGI replacements; no second dated count | A |
| TRL | lean rising | v1.0 on 2026-03-31; download figures vendor-stated | A; C |
| torchtune | falling | no longer actively maintained | A |
| Coding agents (class) | rising | JetBrains work adoption; Stack Overflow agent use; denominators differ | B |
| Claude Code | rising | work adoption about 3% to 18% (2025 Q2 to 2026-01); awareness 31% to 57% | B, COI |
| GitHub Copilot | stable | 29% in 2026-01, growth stalled | B |
| TypeScript | rising | GitHub contributors +66.63%; JetBrains largest five-year rise | B |
| Python | stable | survey 57.9% to 58%; AI Engineer postings 78.4% (one date) | B |
| Voice AI tooling | lean rising | gateway voice use about 4% to about 11% (2026-07 to 2026-10); LiveKit funding | C |
| India AI/ML demand | rising | Naukri AI/ML +49%, +22%, +25%, +20% year on year (2026-02, 05, 06, 09); Indeed India AI mentions 8.2% to 11.7% (2024-09 to 2025-09) | B |
| India IT and generic software demand | falling | Naukri IT and software services +6% to −4% (2026-02 to 2026-09); Indeed India software-development postings −12.3% over three months to about 2026-05 | B |

### 5. Devalued skills (K1–K10)

Verdict words here are *still devalued*, *recovered*, *gone* or *unresolved*; the Repository Deltas table uses the protocol's verdict words.

| K | Skill | Verdict | Evidence | Grade |
|---|---|---|---|---|
| K1 | Standalone prompt writing; Prompt Engineer title | still devalued as a title; baseline as a skill | 72 of 20,662 LinkedIn postings (0.35%, my arithmetic) from a 2024–25-vintage study; prompt engineering named in 31.1% of AI Engineer postings (2026-09-10) | B; M |
| K2 | Framework-specific syntax as a differentiator | recovered as a posting keyword; still not a differentiator | LangChain 34.3% and LangGraph 22.1% of 534 agentic listings (2026-04-19); 17 of 20 interviewed production teams used custom loops | C; B |
| K3 | Demo RAG pipelines | still devalued (table stakes) | RAG named in 54.0% of AI Engineer postings (2026-09-10); no evidence of a differentiator; the claim's 10.0% was not found | B |
| K4 | Vendor-specific vector-database fluency | unresolved | no brand-level posting share found; category 32.6%; brand popularity up (M) | M |
| K5 | Loyalty to one eval-platform brand | still devalued | seven eval and observability tools changed hands or closed in 13 months | B |
| K6 | Hugging Face TGI skills | gone | maintenance-mode notice on the vendor's page; archive date from one secondary | A; C |
| K7 | AutoGen-specific skills | gone on PyPI; successor named | no release for 410 days; Microsoft Agent Framework named as successor | A |
| K8 | RAGAS-based evaluation pipelines | recovered | release candidate v0.4.4rc1 on 2026-11-13 after v0.4.3 on 2026-01-13; commit history not opened | B |
| K9 | Static TensorRT-LLM engine compilation | gone | removal documented; page updated 2026-11-03 | A |
| K10 | Single-provider chat wrappers | still devalued | OpenAI share falling in three telemetry sources; multi-model use rising in three signal types | B |

### 6. Acquisitions, deprecations and dormancy

| Tool | Event | Date | Replacement or outcome | Source | Grade |
|---|---|---|---|---|---|
| OpenAI Assistants API | sunset | 2026-08-26 | Responses API; Conversations API replaces Threads | [S44] | A |
| AutoGen (`autogen-agentchat`) | last PyPI release 0.7.5 | 2025-09-30 | Microsoft Agent Framework (release candidate 2026-02-19; 1.0 about 2026-04-03) | [S36] [S34] [S35] | A |
| Semantic Kernel | folded into the same successor; still active | 2026-04-03 | Microsoft Agent Framework | [S35] | B |
| Hugging Face TGI | maintenance-mode notice (undated); read-only archive 2026-03-21 (one secondary) | 2025-12 to 2026-03-21 | vLLM, SGLang, llama.cpp and MLX | [S38] [S39] | A; C |
| TensorRT-LLM TensorRT backend and `trtllm-build` | removed | documentation page updated 2026-11-03 | PyTorch backend; `tensorrt_llm.LLM`, `trtllm-serve` | [S23] | A |
| torchtune | no longer actively maintained | wound down in 2025 | no successor named in the README lines I read | [S57] | A |
| LangChain legacy chains and agents; LangGraph prebuilt agents | moved or deprecated at 1.0 | 2025-10-22 | `create_agent` with middleware; `langchain-classic` | [S55] | A |
| MCP Roots, Sampling, Logging, HTTP+SSE, Dynamic Client Registration | deprecated, 12-month minimum window | 2026-07-28 | Client ID Metadata Documents replace Dynamic Client Registration; stateless transport | [S30] | A, COI |
| W&B Weave | acquired by CoreWeave (completed) | 2025-05-05 | Apache 2.0; accepts OTLP | [S28] | C |
| Humanloop | platform sunset; team joined Anthropic | 2025-09-08 | none (no live product); billing stopped 2025-07-30 | [S28] | C, COI |
| Langfuse | to ClickHouse (announced) | 2026-01-16 | stays open source and self-hostable per its own page | [S26] [S27] [S28] | A; B |
| Helicone | to Mintlify (announced); maintenance mode | 2026-03-03 | Apache 2.0, self-hostable | [S28] | C |
| Promptfoo | to OpenAI (announced; closing subject to customary conditions; closing not verified) | 2026-03-09 | OpenAI says the open-source project continues | [S25] | A |
| Traceloop (OpenLLMetry) | to ServiceNow (completed) | 2026-05-05 | Apache 2.0 | [S28] | C |
| Galileo | to Cisco (Splunk) (completed) | 2026-05-22 | commercial licence | [S28] | C |
| RAGAS | active: v0.4.4rc1 | 2026-11-13 | none needed | [S37] | B |

The roundup (S28) is a secondary source; two of its rows are corroborated by the issuers' own pages (Promptfoo, Langfuse). Search results also named OpenAI–Statsig (SiliconANGLE, dated 2025-09-02 in the result) and OpenAI–Neptune; neither page was opened, so neither is counted.

### 7. Protocols

| Dimension | MCP | A2A | AG-UI |
|---|---|---|---|
| Governance | AAIF under the Linux Foundation; 146 members on 2026-02-24 [S29] | Linux Foundation project; one-year mark 2026-04-09 [S33] | not obtained |
| Specification | revision 2026-07-28 (previous 2025-11-25) [S30] | v1.0 on 2026-04-09 [S33] | not obtained |
| Vendor support | ChatGPT, Claude, goose and VS Code clients for MCP Apps [S29]; supported in Microsoft Agent Framework [S35] | Azure AI Foundry, Copilot Studio, AWS Bedrock AgentCore Runtime [S33]; Agent Framework support "coming soon" as of 2026-04-03 [S35] | not obtained |
| Registry or adoption counts | 30,375 unique servers on 2026-09-10 [S32] | more than 150 supporting organisations on 2026-04-09 [S33] | not obtained |
| Posting mentions | 16.9% of 213 LangChain-ecosystem listings on 2026-04-19 [S22] | none obtained | none obtained |
| Grade; COI | A for governance and specification, C for counts; COI (Anthropic originated MCP) | A for release facts, C for adoption | none |

What changed in MCP revision 2026-07-28 (all from the changelog [S30], grade A, COI):

- Removed: protocol-level sessions and the `initialize` handshake, so requests are stateless.
- Added: `server/discover`, `subscriptions/listen`, multi round-trip requests, cacheable results (`ttlMs`, `cacheScope`), and OpenTelemetry trace context in `_meta`.
- Moved: tasks into the extension `io.modelcontextprotocol/tasks`.
- Deprecated: Roots, Sampling and Logging; the HTTP+SSE transport (deprecated since 2025-03-26, reclassified as Deprecated); OAuth Dynamic Client Registration (RFC 7591) in favour of Client ID Metadata Documents; the `includeContext` values `thisServer` and `allServers`.
- Policy: a feature lifecycle with a 12-month minimum deprecation window.

### 8. India

**Naukri JobSpeak** (index of new postings and recruiter searches on Naukri, base July 2008 = 1000; sample size not stated; free listings can inflate it). Year-on-year changes:

| Month covered (publication) | AI/ML | IT and software services | Overall index | Source | Grade |
|---|---|---|---|---|---|
| 2026-02 (2026-03-03) | +49% | +6% | 3,233 against 2,890 (+12%) | [S7] | B |
| 2026-05 | +22% (AI/ML above 30 LPA +27%) | −7% | 2,836 against 2,807 (about +1%) | [S8] | B |
| 2026-06 (2026-07-06, TechRepublic citing Reuters) | +25% across 14 sectors; +16% within IT | −3% (IT listings) | not stated in the article | [S9] | B |
| 2026-07 | +33% (Info Edge, search snippet) | not seen | +5% (snippet) | [S11] | C |
| 2026-09 (2026-10-06; the URL says october-2026) | +20%; +11% within IT | −4% | 3,053 against 3,002 (+2%) | [S10] | B |

Experience and city detail (Naukri): in 2026-09, AI/ML within IT rose 54% at 13–16 years, 28% at 8–12 years and 19% for freshers, and was stable at 4–7 years [S10]; in 2026-05, AI hiring rose 44% in Hyderabad, 34% in the National Capital Region and 31% in Chennai, and AI/ML at 13–16 years rose 32% [S8]. In 2026-09 the overall index moved +9% in Hyderabad, +6% in Chennai, +4% in Bengaluru and Kolkata, flat in Pune and −6% in the National Capital Region and Mumbai; freshers +1% [S10].

**Indeed India** (share of Indian postings that reference AI): 8.2% (2024-09), 10.6% (2025-06), 11.7% (2025-09) [S61, grade B]. Software-development postings fell 12.3% over three months to about 2026-05; IT infrastructure and operations −10.2%, IT systems −9.3%, data and analytics −6.7%; overall postings −0.7% in 2026-05 [S62, grade B]. Indeed's US figure, for context: 4.2% of all postings mentioned AI in late 2025 (a record, up 134% since 2020) [S46, grade B]. The AI-share series by country sits in Indeed's AI tracker repository (daily 7-day averages, refreshed monthly); the page I opened did not show the values [S47].

**Other India sources.** CIEL HR (job-posting data March 2024 to May 2026, 2026 against 2025, denominators not stated): agentic AI engineers +260%, GenAI solutions architects +120%, LLM engineers +86.5%, MLOps engineers +82.2% [S60, grade C]. GitHub: 21.9 million developers in India in 2025, up from 4.5 million in 2020, with more than 5 million added in 2025 [S6, grade B].

**Reading.** Two independent platforms with different methods agree on direction: AI-referencing demand up, generic software and IT-services demand down, and AI/ML growth concentrated in 8–16 years of experience. Early-career evidence is mixed (freshers in AI/ML within IT +19% against freshers overall +1%, 2026-09). The call for India AI/ML demand is **rising** (grade B) and for IT and generic software **falling** (grade B). No India skill-level posting series (for example RAG or MCP) was found. Naukri's AI/ML growth rates are year-on-year changes from an undisclosed base.

### 9. Emerging titles

All counts below are listings I saw in search snippets or aggregator pages on 2026-11-14 (access: Extract). They are not market counts: aggregators mirror each other and nothing was deduplicated. The seven graduation tests are volume (V), persistence (P), breadth across employers (B), a shared skill set (S), a seniority ladder (L), adoption by a lab or Big Tech employer (E) and not being an alias (A). Y means evidence supports it, N means evidence against, ? means not testable from what I saw. Persistence is untestable for every title because I have one observation date.

| Title (K) | Listings seen | Tests | Result | Grade |
|---|---|---|---|---|
| Agent Architect (K16) | two exact listings on one aggregator (IDs 3188493, 3188491); variants "AI Agent Architect" and "Agentic AI Architect"; many "AI Architect" | V N, P ?, B N, S ?, L ?, E ?, A N | not graduated; alias of AI Architect | C |
| Distributed Training Engineer (K17) | exact titles at Periodic Labs and OpenAI ("Distributed Training Engineer, Sora"); "distributed training and inference engineer" on WeAreDevelopers | V ?, P ?, B N (two named employers), S ?, L ?, E Y (OpenAI), A ? | not graduated; closest on employer adoption | C |
| Edge AI Engineer (K13) | at least 9 distinct listings on one aggregator; Deepgram "Embedded AI Engineer, On-Device Models"; "Applied ML Engineer, Edge Devices" | V Y (at least 9 on one aggregator), P ?, B ?, S ?, L ?, E ?, A ? | not graduated; candidate | C |
| AI Developer Advocate (K33) | Temporal "Principal Developer Advocate, AI"; MongoDB "AI Staff Developer Advocate"; Fireworks AI "Technical Developer Advocate"; Encord "Developer Advocate, AI/ML"; LlamaIndex "Developer Evangelist, Technical Content" (posted 2026-07-08); Apple "Sr Software Engineer (Developer Advocacy, GenAI)" | V ?, P ?, B Y (six employers), S ?, L Y (Principal, Staff, Senior), E Y (Apple), A ? (developer relations with an AI focus) | not graduated; closest to passing, needs dated counts | C |
| Context Engineer (K20–K22) | "Context Engineer" (Minneapolis), "Sr Staff AI Engineer, Context Engineering" (Chicago), "LLM/Prompt-Context Engineer, Fullstack Python" (Atlanta) on one search page; Novoflow "Founding Prompt/Context Engineer"; PostHog "Context Engineer"; no total shown | V ?, P ?, B ? (two named employers; others not read), S ?, L Y ("Sr Staff" appears), E ?, A ? | not graduated; count unavailable | C |
| AI Vibe Coding Engineer; Vibe Coder (K28) | Gruve "AI Vibe Coding Engineer", four listings on one aggregator; "Prompt Engineer / Vibecoder" and "AI Prompt Engineer / Vibe Coder" listings; no exact "Vibe Engineer" | V N, P ?, B N (one employer), S ?, L ?, E N, A ? | not graduated | C |
| Reasoning roles (K32) | xAI "Member of Technical Staff, Reasoning"; "AI Engineer - Reasoning"; Daivio "AI Engineer, Reasoning systems"; no exact "Reasoning Engineer" | V ?, P ?, B ? (titles differ), S ?, L ?, E Y (xAI), A N (Member of Technical Staff alias) | not graduated | C |
| Pre-training roles (K18, K19) | IFM "Machine Learning Engineer - Pre-training (LLM)"; Sciforium "Pre-training Research Engineer"; Reflection "Member of Technical Staff, Pre-training Infra"; Hyphen Connect "LLM Pre-training & Distributed Engineer"; no exact "Foundation Model Pre-Training Engineer" or "Foundation Model Engineer" | V ?, P ?, B ? (four employers, four different titles), S ?, L ?, E ?, A N | not graduated | C |

No exact-title hit in the combined searches: Prompt Wizard (K27), AI Whisperer (K29), Neural Network Designer (K30), Transformer Specialist (K31), Cognitive Architect (K26), Context Architect (K23), Technical Program Manager (AI) (K34) and Retrieval Engineer (K12). Not searched on their own: K11, K14, K21, K22, K24 and K25. No title graduates on this evidence.

New GenAI titles with real postings (from CIEL HR's India posting data, grade C, denominators not stated): agentic AI engineer (+260%), GenAI solutions architect (+120%), LLM engineer (+86.5%) and MLOps engineer (+82.2%), 2026 against 2025 [S60]. No dated posting counts or graduation tests were possible for them.

### 10. Learn, keep and drop by role family

Lists are graded B unless marked. Evidence is mostly single-date levels and primary-page tool statuses, so "learn first" means "supported by demand levels or by a primary page", not "measured as rising". Families with no usable evidence say so.

#### Applied AI Engineering

- **Learn first.** Python (78.4% of AI Engineer postings, 2026-09-10) [S1]. Calling and routing between at least two model providers [S15] [S13] [S14]. Agent patterns, built first as a custom loop and then in one framework (LangGraph or Microsoft Agent Framework); agentic AI is named in 59.3% of postings [S1] [S20]. RAG with a retrieval-quality test set (54.0%) [S1]. Offline and online evaluation with human review [S20] [S21] (C). The MCP revision 2026-07-28 [S30] (A, COI). TypeScript for the AI Product Engineer (AI Frontend) path [S6] [S66].
- **Keep.** Azure and AWS (35.1% each) and CI/CD (34.4%) [S1]. Vector databases as a category (32.6%) [S1]. Prompt design as a baseline skill (31.1%) [S1]. SQL (58.6% in 2025, 58% in 2026) [S3] [S5].
- **Drop or deprioritise.** The Assistants API [S44] (A). AutoGen-specific code [S36] (A). Framework syntax as a headline skill [S20]. Single-provider wrappers [S15].

#### ML Engineering & Applied Science

- **Learn first.** Post-training methods in TRL (SFT, DPO, reward modelling, RLOO, GRPO) [S56] (A for the library's status; demand is unmeasured). PyTorch-based training and serving stacks, since TensorRT-LLM runs on PyTorch only and vLLM sits in the PyTorch Foundation [S23] [S43] (A). Evaluation methodology [S20].
- **Keep.** Python and SQL (survey use 57.9% and 58.6% in 2025) [S3].
- **Drop or deprioritise.** torchtune recipes [S57], TGI [S38] and TensorRT engine building [S23] (A).
- Note: no Machine Learning Engineer or Applied Scientist posting page was opened, so no role-level shares support these lists.

#### Forward Deployment & Solutions

- **Learn first.** MCP and A2A integration patterns [S30] [S33] (A for the specifications). RAG architecture [S1]. AWS and Azure, the clouds named in 35.1% each of AI Engineer postings and in 43.3% and 26.3% of survey respondents [S1] [S4]. Demand signal: GenAI solutions architects +120% in India, 2026 against 2025, denominators not stated [S60] (C).
- **Keep and drop.** Insufficient evidence: no Forward Deployed Engineer or Solutions Architect posting page was opened.

#### AI Infrastructure & Platform

- **Learn first.** vLLM and SGLang serving [S38] [S43] (A). TensorRT-LLM through its PyTorch backend (`tensorrt_llm.LLM`, `trtllm-serve`) [S23] (A). Distributed training (exact-title postings at OpenAI and Periodic Labs) [S50] (C). MLOps (MLOps engineers +82.2% in India, 2026 against 2025) [S60] (C).
- **Keep.** Local serving with llama.cpp and Ollama (about 130,500 and 182,400 stars on 2026-10-07) [S58] (C). OpenTelemetry-compatible tracing [S28] [S30] (C).
- **Drop or deprioritise.** TGI [S38] and `trtllm-build` engine compilation [S23] (A).

#### Evaluation, Safety & Security

- **Learn first.** Offline and online evaluation, LLM-as-judge with human review [S20] [S21]. AI security: SANS counted more than 850 AI/ML security-engineer postings, about 100 AI red-team and 93 AI supply-chain security postings in mid-September 2026 [S64]. ISO/IEC 42001 for governance engineers [S63] (A).
- **Keep.** Eval harnesses that run on more than one platform: RAGAS (release candidate 2026-11-13), Promptfoo (OpenAI-owned; open source continues) and Langfuse (ClickHouse; open source continues) [S37] [S25] [S26]. COI: Promptfoo and Humanloop events involve OpenAI and Anthropic.
- **Drop or deprioritise.** Loyalty to one eval or observability brand [S28] (C). Humanloop, which was sunset on 2025-09-08 [S28] (C).

#### Research

- **Learn first.** Reinforcement-learning post-training methods in TRL (GRPO, RLOO) [S56] (A for status). Distributed training and pre-training infrastructure (variant titles at four employers) [S50] (C).
- **Keep.** PyTorch [S23] (A).
- **Drop or deprioritise.** torchtune [S57] (A).
- Frontier AI Safety and Alignment Researcher: insufficient evidence. No Research Scientist posting page was opened.

#### Governance, Risk & Assurance

- **Learn first.** ISO/IEC 42001 (BSI's 50th certificate on 2026-10-21) [S63] (A). The EU AI Act timetable as amended by the Digital Omnibus (provisional; final adoption not verified) [S45]. Demand signal: about 430 AI governance, risk and compliance lead postings in mid-September 2026 [S64].
- **Keep.** Insufficient evidence.
- **Drop or deprioritise.** Planning around 2026-08-02 as the Annex III high-risk date without checking final adoption of the omnibus [S45].

#### Product & Program

- Insufficient evidence for a graded list: no AI Product Manager series was obtained. Two judgements, grade D: build evaluation literacy [S20] [S21]; plan for model churn, because one gateway reports a model half-life of about six weeks [S14].

#### Human Data & Evaluation Operations

- Insufficient evidence: not searched.

#### Embodied & Physical AI

- Insufficient evidence: not searched. The edge-AI listings in section 9 are software roles, not robotics.

#### Leadership & Executive

- Insufficient evidence for lists. India context: AI/ML demand within IT is concentrated at 8–16 years of experience (+28% and +54%, 2026-09) [S10], and trade press reports demand shifting to senior and specialised talent [S9].

#### Independent & Fractional

- Insufficient evidence: not searched.


## Repository Deltas

Verdict words follow the protocol: confirmed, updated, contradicted, stale, unverifiable. Grade is the grade of the evidence for the verdict; unverifiable rows are graded E (nothing found after searching) and name the nearest datum where one exists.

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Prompt Engineer title is 72 of 20,662 LinkedIn AI postings (0.35%); standalone prompt writing devalued | updated | The 72 of 20,662 traces to arXiv 2506.00058 (submitted 2025-05-29, revised 2026-02-12; collection dates not stated in what I read), so the title count is of 2024–25 vintage and no newer title count was found. As a skill, prompt engineering is named in 31.1% of AI Engineer postings (2026-09-10). [S19] [S1] | B |
| K2 | LangChain named in 3.6% of postings and 0 of 10 top-lab job descriptions; 85% of 20 production teams built custom loops | updated | The 85% is 17 of 20 interviewed teams (arXiv 2512.04123v2), but the same paper's survey finds 61% of deployed agents use frameworks, and 3.6% appears there for LlamaIndex and for OpenAI Swarm, not LangChain. One agentic job board names LangChain in 34.3% and LangGraph in 22.1% of 534 listings (2026-04-19). The 0-of-10 claim was not tested. [S20] [S22] [S15] | B |
| K3 | RAG named in 10.0% of broad postings; demo RAG commoditised | unverifiable | The 10.0% was not found. Nearest datum: RAG in 54.0% of AI Engineer postings (2026-09-10), a different population. [S1] | E |
| K4 | Pinecone in 0.7% of postings against 9.8% for vector databases | unverifiable | Neither figure found. Nearest data: vector databases in 32.6% of AI Engineer postings (2026-09-10); Pinecone's DB-Engines score 3.24 to 7.95 (2024-12 to 2025-12, my arithmetic). [S1] [S40] | E |
| K5 | Eval-platform brands in under 3% of postings; vendors consolidating (OpenAI–Promptfoo, ClickHouse–Langfuse) | updated | Both deals confirmed: OpenAI's page (2026-03-09) and Langfuse's own page; the date 2026-01-16 comes from SiliconANGLE. Consolidation is wider: W&B Weave (2025-05-05), Humanloop (sunset 2025-09-08), Helicone (2026-03-03), Traceloop (2026-05-05), Galileo (2026-05-22), per a secondary roundup. The under-3% and 0-of-10 figures were not found. [S25] [S26] [S27] [S28] | B |
| K6 | Hugging Face archived the TGI repository on 2026-03-21 | confirmed | Hugging Face documentation carries a maintenance-mode notice and recommends vLLM, SGLang and llama.cpp or MLX (primary). The archive date 2026-03-21 and maintenance from 2025-12 rest on one secondary (Spheron); the GitHub banner could not be opened. [S38] [S39] | B |
| K7 | AutoGen: no PyPI release in 365 days; superseded by Microsoft Agent Framework | confirmed | `autogen-agentchat` last release 0.7.5 on 2025-09-30; none in the 12 months to 2026-11-13 (410 days to 2026-11-14, my count). Microsoft calls Agent Framework the successor to Semantic Kernel and AutoGen (release candidate 2026-02-19; 1.0 about 2026-04-03); trade press says AutoGen still receives bug and critical security fixes. The AG2 fork was not checked. [S36] [S34] [S35] | A |
| K8 | RAGAS: no release since 2026-01-13 and no commit on main since 2026-02-24 | updated | An aggregator lists v0.4.4rc1 on 2026-11-13, 304 days after v0.4.3, under the vibrantlabsai organisation. Commit history not opened (GitHub and PyPI pages refused). [S37] | B |
| K9 | TensorRT-LLM 1.3 removed `trtllm-build`; PyTorch is the only backend | confirmed | NVIDIA's migration guide (page updated 2026-11-03) lists removal of the TensorRT backend, `trtllm-build`, `trtllm-refit`, `trtllm-prune` and `convert_checkpoint.py`; PyTorch is the sole backend. The guide appears in documentation for 1.3.0rc21 to rc29; I saw no stable 1.3.0 in the part of the releases page I read. [S23] [S24] | A |
| K10 | OpenAI's share of traced traffic fell from 75% to 63%; more than 70% of organisations use three or more models | confirmed | Traced to Datadog's 2026 State of AI Engineering (2026-04-21): OpenAI 63% share, down from 75%; more than 70% of organisations use three or more models (vendor telemetry; the text I read does not name the unit of the share). Corroborated by Langfuse (82.7% to 55.3%, 2024-10 to 2025-09), a gateway (OpenAI 70 to 55 of 100 paid teams, 2025-12 to 2026-10) and a CIO survey (81% on three or more families). [S15] [S13] [S14] [S12] | B |
| K11 | "Vector Search & Retrieval Systems Engineer" is a candidate title, unmeasured | unverifiable | Not searched as an exact title; a combined "Retrieval Engineer" search returned no direct hit. No source. | E |
| K12 | "Retrieval / Search Engineer (LLM)" is a candidate title, unmeasured | unverifiable | No direct hit for "Retrieval Engineer" in one combined search; no title count. No source. | E |
| K13 | "On-Device / Edge AI Engineer": no posting evidence | contradicted | At least 9 distinct "Edge AI Engineer" listings on one aggregator; Deepgram "Embedded AI Engineer, On-Device Models"; other on-device and edge-device engineer listings (search snippets, 2026-11-14). [S52] | C |
| K14 | "On-Device & Edge SLM Engineer": unsourced label | unverifiable | No exact-title hit; related titles exist (K13). CoreML and ONNX claims not searched. [S52] | E |
| K15 | "Conversational & Voice AI Engineer": no title count | updated | A voice-AI engineering job board exists (title count not obtained); gateway voice-model use rose from about 4% to about 11% (2026-07 to 2026-10); LiveKit raised $100M on 2026-01-22 (company-stated). [S68] [S14] [S59] | C |
| K16 | "Agent Architect (exact)": about 2 postings; alias of AI/Solutions Architect | confirmed | Two exact "Agent Architect" listings on one aggregator, plus "AI Agent Architect" and "Agentic AI Architect" variants (2026-11-14); the alias reading was not disproved. [S49] | C |
| K17 | "Distributed Training Engineer": title not found | contradicted | Exact-title postings at Periodic Labs and at OpenAI ("Distributed Training Engineer, Sora"); WeAreDevelopers lists "distributed training and inference engineer". [S50] | C |
| K18 | "Foundation Model Pre-Training Engineer": unsourced label | updated | No exact title; pre-training variants exist at IFM, Sciforium, Reflection and Hyphen Connect. [S50] | C |
| K19 | "Foundation Model Engineer": never searched | updated | Searched on 2026-11-14 in a combined query: no exact hit; pre-training and distributed-training variants only. [S50] | C |
| K20 | "Context Engineer": 10–25 live globally, three archetypes | unverifiable | Real listings exist (a ZipRecruiter search page with salary data as of 2026-06-01; Novoflow; PostHog) in at least three archetypes, but no total count was shown. [S48] | C |
| K21 | "AI Context Engineer": Adobe title | unverifiable | Not searched separately; covered only by the Context Engineer searches. No source. | E |
| K22 | "Data / Context Engineer": staffing listing | unverifiable | Not searched separately. No source. | E |
| K23 | "Context Architect": 2–3 listings | confirmed | No hit for "Context Architect" in a combined search, consistent with a quarantined, low-volume title; the 2–3 listings were not reproduced (low weight). [S49] | C |
| K24 | "Context Harness Engineer": one aggregator count | unverifiable | Not searched. No source. | E |
| K25 | "Principal Agentic Context Engineer": single blog citation | unverifiable | Not searched. No source. | E |
| K26 | "Cognitive Architect": raw hits are false positives | confirmed | No hit for "Cognitive Architect" in a combined search (low weight). [S49] | C |
| K27 | "Prompt Wizard": 0 postings | confirmed | No exact-title hit (searched 2026-11-14). [S54] | C |
| K28 | "Vibe Engineer": not searched | updated | Searched: no exact "Vibe Engineer"; Gruve "AI Vibe Coding Engineer" has four listings on one aggregator and "Vibe Coder" roles exist. [S54] | C |
| K29 | "AI Whisperer": never measured | updated | Searched: no exact-title hit. [S54] | C |
| K30 | "Neural Network Designer": never measured | updated | Searched: no exact-title hit. [S51] | C |
| K31 | "Transformer Specialist": never measured | updated | Searched: no exact-title hit. [S51] | C |
| K32 | "Reasoning Engineer": never measured | updated | No exact title; xAI "Member of Technical Staff, Reasoning" and "AI Engineer - Reasoning" roles exist. [S51] | C |
| K33 | "AI Developer Advocate / DevRel (AI)": one Ollama opening | updated | AI developer-advocate roles at Temporal, MongoDB, Fireworks AI, Encord, LlamaIndex and Apple (2026-11-14). [S53] | C |
| K34 | "Technical Program Manager (AI)": only inside the FDE sample | unverifiable | No direct hit for "Technical Program Manager, AI" in a combined search. No source. | E |
| K35 | Agentic AI in 59.3% of AI Engineer postings; Agent Architect about 2; Context Engineer about 10–25 | confirmed | JobsPipe: agentic AI 59.3% (as of 2026-09-10; page unchanged on 2026-11-14); two exact Agent Architect listings; the Context Engineer count was not verified. [S1] [S49] [S48] | B |
| K36 | Evaluation in the postings of 68.2% of 198 companies (snapshot 2026-08-05) | unverifiable | No source found. Nearest datum: a vendor survey with offline evals at 52.4% of respondents (not a posting measure). [S21] | E |
| K37 | Thin-wrapper skills commoditised; Prompt Engineer a legacy title | updated | Single-provider wrappers: devalued status confirmed by the K10 evidence. Prompt Engineer: the title evidence is of 2024–25 vintage, and prompt engineering is still named in 31.1% of AI Engineer postings (2026-09-10). [S15] [S19] [S1] | B |

Verdict counts: 9 confirmed (K6, K7, K9, K10, K16, K23, K26, K27, K35), 14 updated, 2 contradicted (K13, K17), 0 stale, 12 unverifiable.

## Absences

| Item the brief asked for | Where I looked | Result |
|---|---|---|
| Posting-share series at two dates for any GenAI skill (RAG, MCP, LangGraph, evaluation) | JobsPipe AI Engineer page (one date, 2026-09-10, unchanged on 2026-11-14); one agentic job board (one date, 2026-04-19); Indeed Hiring Lab AI tracker repository (values not on the page; Hiring Lab blog pages refused by the fetch tool); Naukri JobSpeak (category level only) | Absent. This is the central gap: no skill's employer-demand momentum is measured. |
| JobsPipe series for the other eleven titles in the brief | Not opened | Absent; no second date for any title. |
| Europe (EU and UK) posting series | Indeed UK Hiring Lab page (redirect refused); no European labour-market source searched beyond the EU AI Act | Absent. |
| Package-download series for MCP SDKs, OpenAI Agents SDK, Claude Agent SDK and Google ADK; npm | Two searches (MCP package downloads on pypistats; a combined SDK downloads query) | No dated two-point series obtained. npm was not searched. |
| AG-UI adoption | No search run | Absent. |
| Second dated count for vLLM, SGLang, llama.cpp, Ollama | One search on vLLM and SGLang adoption; one on llama.cpp, Ollama and ExecuTorch | Only vLLM on 2025-05-07 and llama.cpp and Ollama on 2026-10-07. |
| On-device and small-model tool series (CoreML, ONNX, ExecuTorch, small language models) | Same search as above | No series; star counts at one date only. |
| Multimodal (other than voice) | No search run | Absent. |
| Posting shares for fine-tuning and post-training skills | Not found in any source opened | Absent. |
| Second dated count for LangChain and LangGraph downloads | pepy.tech (one snapshot, 2026-11-11); the vendor's statement of 2025-10-22 | Not comparable; no series. |
| Evaluation-platform share in postings (K5, K36); RAG and Pinecone shares (K3, K4); a newer Prompt Engineer title count (K1) | Searches for each figure's wording | Not found. |
| TGI archive banner and date on GitHub | GitHub repository page | Refused by the fetch tool (URL not on the allowlist); the date rests on one secondary source. |
| RAGAS commit history on main | GitHub and PyPI pages | Refused; K8's commit claim unverified. |
| Final adoption of the EU AI Act omnibus after 2026-06-22 | Sidley article only | Not verified; the Official Journal was not searched. |
| A stable TensorRT-LLM release carrying the removal | GitHub releases page, first 100,000 characters | Release candidates only in the part read. |
| Titles K11, K12, K14, K21, K22, K24, K25, K34; a Context Engineer count (K20) | Combined title searches on 2026-11-14 | No exact hit or not searched; no count. |
| Role families: Human Data & Evaluation Operations; Embodied & Physical AI; Independent & Fractional; parts of Research, Product & Program, Leadership | No search run | Learn, keep and drop lists marked "insufficient evidence". |
| India GCC and skill-level series (foundit, Quess, NASSCOM, IANS leads) | Surfaced in search results; the YourStory and TechRepublic GCC pages failed or were cut off by the usage limit | Not opened; no GCC skill series. |
| OpenAI–Statsig and OpenAI–Neptune | Search results only | Not opened; not counted. |

## Open Questions & Risks

**Open questions**

1. Did the EU AI Act omnibus complete adoption before 2026-08-02? The date has passed; the Official Journal text and the Council decision were not checked, so the 2027-12-02 date for Annex III is provisional.
2. Does any platform publish skill-level posting shares at two or more dates for GenAI skills? JobsPipe's page showed one date; the Hiring Lab tracker CSVs may hold category series but were not readable here.
3. Is RAGAS's move to the vibrantlabsai organisation a rename or a fork, and does the main branch show commits after 2026-02-24?
4. Did the Promptfoo acquisition close, and did its licence change after 2026-03-09?
5. Which stable TensorRT-LLM release first carries the TensorRT backend removal?
6. Has MCP demand in postings risen? Only one date (2026-04-19) and one narrow board were seen.
7. What do European and UK posting data show for the same skills?

**Risks to the evidence**

- Coverage is limited by two rounds of parallel research agents that stopped on the account's usage limit before saving anything, and by a further limit hit on the last fetch. The report rests on one researcher's 51 searches and 68 fetch attempts, with no second reader.
- Pages marked Read were opened through a fetch tool that summarises pages with a model, so a figure could be mis-stated or a caveat dropped; the figures that carry the Key Findings were cross-checked against a second source where one existed (provider shares, AutoGen, TGI, Naukri and Indeed direction).
- Conflict of interest: Anthropic originated MCP and makes Claude Code and the Claude models. Rows on MCP, Claude Code, Ramp's Anthropic share, the Vercel and a16z provider figures, and the Humanloop team's move to Anthropic are marked COI. Third-party or primary pages carry the MCP governance, specification and registry facts.
- Titles: counts come from aggregators that mirror each other, so a listing can appear several times.

**Strongest objections an expert would raise**

| Objection | Evidence for | Evidence against | Where it leaves the findings |
|---|---|---|---|
| A single-date posting share is a level, not momentum. | JobsPipe page dated 2026-09-10 and unchanged on 2026-11-14; the agentic board has one date. [S1] [S22] | None; the report treats them as levels. | No GenAI skill has a measured demand trend; calls rest on other signal types. |
| Downloads, stars and popularity scores do not measure use. | pepy.tech counts installs including CI and mirrors; DB-Engines scores popularity (mentions, searches, job offers). [S41] [S40] | Used only as second signals; no call rests on one alone. | Brand-level calls are "lean". |
| Vendor telemetry and surveys over-represent the vendor's own customers. | Datadog says its customers skew to cloud-mature organisations; the Vercel data are one gateway; Ramp covers businesses on its own platform and likely undercounts; LangChain's survey is vendor-run. [S15] [S14] [S16] [S21] | Datadog, Langfuse, Vercel and a16z agree on the direction of OpenAI's share and on multi-model use. | Direction credible; magnitudes less so. |
| An Anthropic-authored review will favour Anthropic products. | MCP, Claude Code and Claude-model rows are in scope. | Every such row is marked COI; MCP facts come from the specification, the Linux Foundation project and a third party's registry count; JetBrains and Stack Overflow are independent. [S29] [S30] [S32] [S65] | Treat Claude Code and MCP magnitudes with caution. |
| Aggregator title counts are unreliable. | Mirror sites repeat listings (Periodic Labs appeared on several boards); nothing was deduplicated. [S50] | Only listings seen are reported, never market counts; no title is called graduated. | Titles remain candidates. |
| India's year-on-year growth rates start from a low base, and Naukri's index includes recruiter searches and free listings. | Naukri's method note; overall index changes of +1% to +12%. [S7] [S8] [S10] | Indeed India, with a different method, shows AI mentions rising from 8.2% to 11.7% and software postings falling. [S61] [S62] | Direction credible; the size of AI/ML growth is uncertain. |
| Concepts-first advice will fail keyword filters. | Postings name tools: LangChain in 34.3% of the agentic board's listings. [S22] | Recommendation 1 says to name the tool; 17 of 20 interviewed production teams used custom loops. [S20] | Unresolved; no screening data were found. |
| A deprecated tool still runs in legacy systems. | AutoGen still receives security fixes; TGI is in maintenance, not removed. [S35] [S38] | Assistants API and the TensorRT backend are removed. [S44] [S23] | Keep only for maintenance roles. |

## Discovered Concerns

1. **Date labels on posting data.** The JobsPipe figures the brief labels "retrieved 2026-11-02" carry the page's count date 2026-09-10, and the page was unchanged on 2026-11-14. A retrieval date used as a data date would show a two-month-old count as new, and no second date exists to build a series. [S1]
2. **Naukri slug mismatch.** The page with "october-2026" in its URL covers September 2026 and was published on 2026-10-06. Dating the point as October would misplace it. [S10]
3. **Stale DB-Engines copy.** The vector DBMS page returned the December 2025 ranking on 2026-11-14. Any figure labelled with a later date needs a fresh check. [S40]
4. **K2's 3.6% figure.** In the arXiv survey, 3.6% belongs to LlamaIndex and to OpenAI Swarm; LangChain/LangGraph is 25.0%. A transcription slip is possible; I did not find the source of the "3.6% of postings" claim. [S20]
5. **RAGAS organisation name.** The aggregator lists the repository under vibrantlabsai; the page did not confirm a rename from the earlier organisation name. A tracker keyed to the old name could miss releases. [S37]
6. **Unsourced download figure.** An Ollama audit page quotes "52 million monthly downloads" without a source; I did not use it. [S58]
7. **Ambiguous Stack Overflow 2026 figure.** The statement that Claude Code is used by 66% and GitHub Copilot by 59% has no clear denominator, and Claude Code is an Anthropic product (COI). [S5]
8. **Indeed AI-share series sits behind a repository.** Hiring Lab blog pages were refused by the fetch tool, and the tracker repository page showed file names but no values; anyone building a country series needs the CSV files. [S47]
9. **Obsolete tutorials.** The Assistants API sunset date (2026-08-26) has passed, and the MCP revision of 2026-07-28 deprecates several features; learning material from 2025 may teach both. [S44] [S30]

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | LangChain and LangGraph usage fell after the 1.0 reset, and the frameworks are a weak career signal. | Contradicted | No fall is visible: pepy.tech last-30-day installs were 157,554,330 (LangChain) and 58,965,017 (LangGraph) on 2026-11-11 (installs include CI and mirrors, and the vendor's October 2025 "90M monthly" statement uses another counter, so no change can be computed); named in 34.3% and 22.1% of 534 agentic listings (2026-04-19); framework adoption rose from more than 9% to almost 18% of organisations (Datadog). The weak-differentiator half stands: 17 of 20 interviewed production teams built custom loops. [S41] [S42] [S55] [S22] [S15] [S20] | Name LangChain or LangGraph on a CV as a tool, not as a differentiator; do not advise avoiding them. |
| P2 | MCP is the dominant agent-tool protocol and sits under neutral (Linux Foundation) governance. | Updated | Governance confirmed on a primary page (AAIF, 146 members on 2026-02-24); registry supply about tripled from 2026-05 to 2026-09-10 (single-author count); "dominant" was not measured against alternatives; the 2026-07-28 revision removes sessions and deprecates five features, so 2025 tutorials are partly out of date. COI. [S29] [S30] [S32] | Teach the 2026-07-28 revision and pin a version. |
| P3 | AutoGen is dormant and superseded by Microsoft Agent Framework. | Confirmed | No PyPI release since 2025-09-30; Microsoft names Agent Framework as successor (release candidate 2026-02-19; 1.0 about 2026-04-03). [S36] [S34] [S35] | Drop AutoGen-specific skills except for maintenance roles. |
| P4 | Hugging Face TGI is archived and TensorRT-LLM engine builds were removed. | Confirmed | TGI: maintenance-mode notice on a primary page; archive date from one secondary. TensorRT-LLM: removal documented, page updated 2026-11-03. [S38] [S39] [S23] | Drop both from learn lists. |
| P5 | Dedicated vector-database brands lost relevance to pgvector and cloud-native search. | Contradicted | DB-Engines popularity rose 37% to 146% for dedicated brands from 2024-12 to 2025-12 (my arithmetic) while Elasticsearch fell 17% and MongoDB 7%; pgvector is not on the page; popularity is not usage or demand. [S40] | Keep vector databases as a category skill; make no brand call. |
| P6 | OpenAI's share of LLM traffic is falling as multi-model use becomes standard. | Confirmed | Three telemetry sources show OpenAI's share falling (Datadog 75% to 63%; Langfuse 82.7% to 55.3%; gateway paid-team use 70 to 55 of 100). Ramp shows OpenAI's share of businesses paying rising from 36.8% (2025-12) to 40.6% (2026-10) as overall adoption rises, which is a different measure. [S15] [S13] [S14] [S16] | Build provider independence into projects. |


## Sources & Evidence Ledger

Access: Read means the page was opened with the fetch tool, which returns a model-written summary; Extract means only a search-result snippet or a summary was seen; Blocked means the fetch tool refused the address or failed, and no workaround was tried. Retrieval dates are in India Standard Time. Rows S49–S54 and S68 are listings pages that mirror each other; no figure rests on one of them alone except where the text says "seen".

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | AI Engineer job description: skills and key shares, JobsPipe, https://jobspipe.dev/job-description/ai-engineer | as of 2026-09-10 | 2026-11-14 | B | Read | single-source; platform data; n not stated | AI Engineer skill shares; date of the brief's figures |
| S2 | AI Engineer jobs (live roles), JobsPipe, https://jobspipe.dev/jobs/ai-engineer.md | undated | 2026-11-14 | B | Read | single-source | 3,944 live postings across 30+ sources |
| S3 | Stack Overflow Developer Survey 2025, Stack Overflow, https://survey.stackoverflow.co/2025/ | 2025-07-29 | 2026-11-14 | B | Read | corroborated | AI tool and agent use; Python, SQL shares |
| S4 | Stack Overflow Developer Survey 2025, Technology, Stack Overflow, https://survey.stackoverflow.co/2025/technology/ | 2025-07-29 | 2026-11-14 | B | Read | | language, cloud, database and model shares |
| S5 | The results of the 2026 developer survey are here, Stack Overflow blog, https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/ | 2026-10-06 | 2026-11-14 | B | Read | COI (Claude Code figure) | 2026 language shares; coding-agent use |
| S6 | Octoverse 2025: a new developer joins GitHub every second as AI leads TypeScript to #1, GitHub blog, https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1 | 2025-10-28 (updated 2026-02-28) | 2026-11-14 | B | Read | COI (MCP stars); Copilot agent figure is vendor-stated | language contributors; LLM SDK repositories; India developers; MCP stars |
| S7 | Naukri JobSpeak, February 2026, Naukri (Info Edge), https://www.naukri.com/blog/naukri-jobspeak-it-hiring-shows-meaningful-recovery-and-ai-momentum-continues-white-collar-market-posts-12-yoy-growth-in-february-2026/ | 2026-03-03 | 2026-11-14 | B | Read | single-platform method | India AI/ML and IT series |
| S8 | Naukri JobSpeak, May 2026, Naukri (Info Edge), https://www.naukri.com/blog/naukri-jobspeak-may-2026-white-collar-hiring-remains-stable-in-may-ai-ml-roles-and-insurance-sector-continue-to-lead/ | undated (covers May 2026) | 2026-11-14 | B | Read | single-platform method | India AI/ML, IT, city and experience detail |
| S9 | India AI hiring outpaces IT recruitment (Naukri June data via Reuters), TechRepublic, https://techrepublic.com/article/news-india-ai-hiring-outpaces-it-recruitment-apac | 2026-07-06 | 2026-11-14 | B | Read | | India series for 2026-06; seniority shift |
| S10 | Naukri JobSpeak, September 2026 data (URL slug says october-2026), Naukri (Info Edge), https://www.naukri.com/blog/naukri-jobspeak-october-2026-white-collar-hiring-ai-ml-growth/ | 2026-10-06 | 2026-11-14 | B | Read | slug mismatch | India series for 2026-09; experience and city detail |
| S11 | Info Edge reports 5% July white-collar job growth driven by 33% AI/ML surge, sahi.com, https://www.sahi.com/news/info-edge-reports-5-july-white-collar-job-growth-driven-by-33-ai-ml-surge-3162-PE1_COR | undated (covers July 2026) | 2026-11-14 | C | Extract | single-source | India series for 2026-07 |
| S12 | OpenAI leads, Anthropic surges: enterprise AI shifts to a multi-model reality (a16z CIO survey, n=100), eMarketer, https://www.emarketer.com/content/openai-leads--anthropic-surges-enterprise-ai-shifts-multi-model-reality | undated | 2026-11-14 | C | Read | COI; single-source; survey date not stated | multi-model use among CIOs |
| S13 | State of LLMs (September 2025 data), Langfuse, https://langfuse.com/blog/2025-10-13-state-of-llms-september-2025 | 2025-10-13 | 2026-11-14 | B | Read | vendor data; self-hosted excluded | OpenAI, Google and Anthropic traced-traffic shares |
| S14 | AI Gateway Production Index (October 2026 data), Vercel, https://vercel.com/blog/ai-gateway-production-index-november-2026 | 2026-11-09 | 2026-11-14 | B | Read | COI (vendor data; includes Anthropic share); one gateway | provider use; model churn; voice-model use |
| S15 | 2026 State of AI Engineering, Datadog, https://datadoghq.com/state-of-ai-engineering/ | 2026-04-21 | 2026-11-14 | B | Read | vendor telemetry; customers skew cloud-mature | OpenAI share; multi-model use; framework adoption |
| S16 | AI Index (October 2026 data), Ramp, https://ramp.com/data/ai-index | undated page (October 2026 data) | 2026-11-14 | B | Read | COI (Anthropic share); likely undercounts | business adoption; token spend share |
| S17 | AI Index, February 2026 (January data), Ramp, https://ramp.com/velocity/ai-index-february-2026 | 2026-02-11 | 2026-11-14 | B | Read | COI | business adoption; multi-vendor payers |
| S18 | AI Index (August 2026 data), Ramp, https://ramp.com/data/ai-index-sept-2026 | undated (covers 2026-08) | 2026-11-14 | B | Read | COI | business adoption for 2026-08 |
| S19 | Prompt Engineer: analyzing skill requirements in the AI job market (arXiv 2506.00058), An Vu and Jonas Oppenlaender, https://arxiv.org/abs/2506.00058 | 2025-05-29 (v2 2026-02-12) | 2026-11-14 | B | Read | preprint; collection dates not stated in what was read | K1 title count |
| S20 | Measuring agents in production (arXiv 2512.04123v2), https://arxiv.org/pdf/2512.04123v2 | 2026-01-30 (v2) | 2026-11-14 | B | Read | preprint; small samples | custom loops; framework use; evaluation practice |
| S21 | State of Agent Engineering, LangChain, https://langchain.com/state-of-agent-engineering | 2026-06-12 (page header; fieldwork 2025-11-18 to 2025-12-02) | 2026-11-14 | C | Read | vendor-run survey | evaluation, tracing and fine-tuning practice |
| S22 | LangChain job market 2026, agentic-engineering-jobs.com, https://agentic-engineering-jobs.com/langchain-job-market-2026 | 2026-04-19 | 2026-11-14 | C | Read | single-source; own job board; tagging method not described | framework and MCP posting shares |
| S23 | TensorRT backend removal guide, NVIDIA TensorRT-LLM documentation, https://nvidia.github.io/TensorRT-LLM/latest/legacy/tensorrt-backend-removal.html | page updated 2026-11-03 | 2026-11-14 | A | Read | issuer page | K9; TensorRT-LLM removal |
| S24 | TensorRT-LLM releases, NVIDIA on GitHub, https://github.com/NVIDIA/TensorRT-LLM/releases | undated (release dates partly shown) | 2026-11-14 | A | Read (first 100,000 characters only) | partial read | release-candidate sequence |
| S25 | OpenAI to acquire Promptfoo, OpenAI, https://openai.com/blog/openai-to-acquire-promptfoo | 2026-03-09 | 2026-11-14 | A | Read | issuer page | K5; Promptfoo acquisition |
| S26 | Langfuse joins ClickHouse, Langfuse, https://langfuse.com/blog/joining-clickhouse | undated | 2026-11-14 | A | Read | issuer page | K5; Langfuse acquisition |
| S27 | ClickHouse raises $400M and acquires Langfuse, SiliconANGLE, https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/ | 2026-01-16 | 2026-11-14 | B | Extract | corroborated by a BusinessWire release seen in search (https://www.businesswire.com/news/home/20260116008883/en) | Langfuse announcement date |
| S28 | Who bought your LLM observability tool? (2025–2026 consolidation), Developers Digest, https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026 | undated (2026) | 2026-11-14 | C | Read | secondary roundup; two rows corroborated by S25 and S26 | Weave, Humanloop, Helicone, Traceloop and Galileo events |
| S29 | AAIF's first quarter: new members, technical wins and open governance, Agentic AI Foundation, https://aaif.io/blog/aaifs-first-quarter-success-story-new-members-technical-wins-and-open-governance | 2026-02-24 | 2026-11-14 | A | Read | COI (MCP) | AAIF membership; MCP Apps; MCP support |
| S30 | MCP specification 2026-07-28 changelog, Model Context Protocol project, https://modelcontextprotocol.io/specification/2026-07-28/changelog | 2026-07-28 | 2026-11-14 | A | Read | COI (MCP) | MCP revision, deprecations |
| S31 | MCP 2026 changes the rules (guest post by a WSO2 field CTO), Agentic AI Foundation, https://aaif.io/blog/mcp-2026-changes-the-rules | 2026-09-03 | 2026-11-14 | C | Read | COI (MCP); vendor author | cross-check of the 2026 specification changes; no adoption numbers |
| S32 | The MCP registry by the numbers, dev.to (amareswer), https://dev.to/amareswer/the-mcp-registry-by-the-numbers-38nc | data pull 2026-09-10 (post date not stated) | 2026-11-14 | C | Read | single-source; COI (MCP) | MCP registry counts |
| S33 | A2A protocol surpasses 150 organizations, lands in major cloud platforms and sees enterprise production use in first year, Linux Foundation, https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year | 2026-04-09 | 2026-11-14 | A for release facts; C for adoption | Read | vendor-stated adoption | A2A v1.0; organisations; vendor support |
| S34 | Migrate your Semantic Kernel and AutoGen projects to Microsoft Agent Framework (release candidate), Microsoft DevBlogs, https://devblogs.microsoft.com/agent-framework/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/ | 2026-02-19 | 2026-11-14 | A | Read | issuer page | Agent Framework as successor |
| S35 | Microsoft ships production-ready Agent Framework 1.0 for .NET and Python, Visual Studio Magazine, https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx | 2026-04-06 per URL (text dated April 3; year inferred from its references) | 2026-11-14 | B | Read | | Agent Framework 1.0; AutoGen fixes; A2A status |
| S36 | autogen-agentchat, Python Package Index, https://pypi.org/project/autogen-agentchat | last release 2025-09-30 | 2026-11-14 | A | Read | registry page | K7; AutoGen release gap |
| S37 | vibrantlabsai/ragas releases, releasealert.dev, https://releasealert.dev/github/vibrantlabsai/ragas | undated (release of 2026-11-13 listed) | 2026-11-14 | B | Read | single-source; aggregator | K8; RAGAS releases |
| S38 | Text Generation Inference documentation, Hugging Face, https://huggingface.co/docs/text-generation-inference/index | undated | 2026-11-14 | A | Read | issuer page | K6; TGI status |
| S39 | Migrate TGI to vLLM or SGLang (2026), Spheron, https://www.spheron.network/blog/migrate-tgi-to-vllm-sglang-2026/ | undated (2026) | 2026-11-14 | C | Read | single-source | TGI archive date |
| S40 | DB-Engines ranking of vector DBMS, DB-Engines, https://db-engines.com/en/ranking/vector+dbms | ranking month 2025-12 (page content on 2026-11-14) | 2026-11-14 | B | Read | stale copy; 2024-12 values and percentage changes are my arithmetic (M) | vector-store popularity |
| S41 | langchain downloads, pepy.tech, https://pepy.tech/projects/langchain | updated 2026-11-11 | 2026-11-14 | B | Read | counts include CI and mirrors | LangChain installs |
| S42 | langgraph downloads, pepy.tech, https://pepy.tech/project/langgraph | updated 2026-11-11 | 2026-11-14 | B | Read | counts include CI and mirrors | LangGraph installs |
| S43 | PyTorch Foundation welcomes vLLM, PyTorch Foundation, https://pytorch.org/blog/pytorch-foundation-welcomes-vllm/ | 2025-05-07 | 2026-11-14 | A | Read | issuer page | vLLM governance and stars |
| S44 | Assistants API migration guide, OpenAI, https://developers.openai.com/api/docs/assistants/migration | undated (states the sunset of 2026-08-26) | 2026-11-14 | A | Read | issuer page | Assistants API sunset |
| S45 | EU lawmakers reach provisional agreement to delay key EU AI Act obligations, Sidley Austin (Data Matters), https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ | 2026-06-22 | 2026-11-14 | B | Read | final adoption not verified | EU AI Act omnibus dates |
| S46 | Indeed AI language job postings, eWeek, https://www.eweek.com/news/indeed-ai-language-job-postings/ | 2026-01-23 | 2026-11-14 | B | Read | reports Indeed Hiring Lab data (late 2025) | US AI mention share |
| S47 | hiring-lab/ai-tracker, Indeed Hiring Lab on GitHub, https://github.com/hiring-lab/ai-tracker | undated | 2026-11-14 | A | Read | data values not on the page | existence and scope of Indeed's AI series |
| S48 | Context Engineering jobs, ZipRecruiter, https://www.ziprecruiter.com/Jobs/Context-Engineering | undated (salary data as of 2026-06-01) | 2026-11-14 | C | Read | listing total not shown | Context Engineer listings |
| S49 | Agent Architect listings, virtualvocations, https://www.virtualvocations.com/job/agent-architect-3188493-i.html ; https://www.virtualvocations.com/job/agent-architect-3188491-i.html ; https://www.virtualvocations.com/job/ai-agent-architect-3219768-i.html ; Agentic AI Architect, Teal, https://www.tealhq.com/job/agentic-ai-architect_7ea1a0f9e6726ab5b23133370229343ab3c70 | undated | 2026-11-14 | C | Extract | search snippets; aggregator listings | K16, K23, K26 |
| S50 | Distributed and pre-training engineer listings: Periodic Labs, https://swooped.co/job-postings/distributed-training-engineer-remote-periodic-labs-96ff6 ; OpenAI, https://inferencejobs.com/companies/openai/jobs/distributed-training-engineer-sora ; WeAreDevelopers, https://www.wearedevelopers.com/jobs/48399-distributed-training-and-inference-engineer.md ; Hyphen Connect, https://jobera.com/job/hyphenconnect-llm-pre-training-distributed-engineer-ai-infrastructure-51199870/ ; Sciforium, https://resumegeni.com/jobs/llm-training-engineer-at-sciforium-san-francisco | undated | 2026-11-14 | C | Extract | mirrors repeat listings | K17, K18, K19 |
| S51 | xAI "Member of Technical Staff, Reasoning", Greenhouse, https://job-boards.greenhouse.io/xai/jobs/5073866007 ; Daivio "AI Engineer, Reasoning systems", foundit, https://www.foundit.in/job/ai-engineer-reasoning-systems-beyond-standard-llm-use-daivio-india-51127818 | undated | 2026-11-14 | C | Extract | search snippets | K30, K31, K32 |
| S52 | Edge AI Engineer listings, virtualvocations, https://www.virtualvocations.com/job/edge-ai-engineer-3061908-i.html (eight more listing IDs appeared in the same search); Deepgram "Embedded AI Engineer, On-Device Models", Chopping Block, https://www.choppingblock.ai/jobs/embedded-ai-engineer-on-device-models-at-deepgram | undated | 2026-11-14 | C | Extract | search snippets; one aggregator | K13, K14 |
| S53 | AI developer-advocate listings: Temporal, https://job-boards.greenhouse.io/temporaltechnologies/jobs/4947867007 ; MongoDB, https://found.dev/job/mongodb-ai-staff-developer-advocate-b1tx ; Fireworks AI, https://www.indexventures.com/startup-jobs/fireworks-ai/technical-developer-advocate/ ; Encord, https://resumegeni.com/jobs/developer-advocate-aiml-at-encord-san-francisco ; LlamaIndex, https://csdsjobs.duckdns.org/job/developer-evangelist-technical-content-llamaindex-san-francisco-2aa41cfa119b ; Apple, https://jobs.anitab.org/companies/apple/jobs/97748980-sr-software-engineer-developer-advocacy-genai-ai-data-platforms | undated | 2026-11-14 | C | Extract | search snippets; aggregator mirrors | K33 |
| S54 | Gruve "AI Vibe Coding Engineer" listings, jobgether, https://jobgether.com/offer/6a56f0c1ac00a71a5a904a44-ai-vibe-coding-engineer ; vibehackers, https://vibehackers.io/jobs/ai-vibe-coding-engineer-gruve | undated | 2026-11-14 | C | Extract | search snippets; one employer | K27, K28, K29 |
| S55 | LangChain and LangGraph 1.0, LangChain, https://www.langchain.com/blog/langchain-langgraph-1dot0 | 2025-10-22 | 2026-11-14 | A for release facts; C for adoption | Read | vendor | LangChain 1.0 changes; vendor download statement |
| S56 | TRL v1.0, Hugging Face, https://huggingface.co/blog/trl-v1 | 2026-03-31 | 2026-11-14 | A for release facts; C for download figures | Read | vendor | TRL status and methods |
| S57 | torchtune README, Meta PyTorch on GitHub, https://raw.githubusercontent.com/meta-pytorch/torchtune/main/README.md | undated | 2026-11-14 | A | Read | issuer page | torchtune status |
| S58 | Ollama hits 52 million downloads (audit page), Vucense, https://vucense.com/ai-intelligence/local-llms/ollama-hits-52-million-downloads-local-ai/ | checked 2026-10-07 | 2026-11-14 | C | Read | single-source; the download figure is unsourced and not used | Ollama and llama.cpp stars |
| S59 | LiveKit raises $100M at a $1B valuation (press release), Fortune (EZ Newswire), https://fortune.com/press-releases/livekit-raises-100m-1b-valuation-voice-first-computing-2026-01-22 | 2026-01-22 | 2026-11-14 | C | Read | company-stated; paid content | voice-AI funding |
| S60 | AI job shift: agentic AI engineers the hottest tech hire, demand up 260% (CIEL HR data), BusinessToday.in, https://www.businesstoday.in/jobs/story/ai-job-shift-agentic-ai-engineers-emerge-as-the-hottest-tech-hire-demand-up-260-percent-553968-2026-09-08 | 2026-09-08 | 2026-11-14 | C | Read | denominators not stated; single-source | India title growth |
| S61 | AI job postings rise sharply to 11.7%: report (Indeed), indbiz.gov.in, https://indbiz.gov.in/ai-job-postings-rise-sharply-to-11-7-report | 2025-10-22 | 2026-11-14 | B | Read | | Indeed India AI mention share |
| S62 | Software job postings fall 12.3% as AI reshapes tech hiring in India: Indeed, People Matters, https://www.peoplematters.in/news/recruiting-and-onboarding/software-job-postings-fall-123percent-as-ai-reshapes-tech-hiring-in-india-indeed-50486 | 2026-06-24 | 2026-11-14 | B | Read | | Indeed India software postings |
| S63 | BSI awards its 50th ISO/IEC 42001 certificate, BSI, https://www.bsigroup.com/en-GB/insights-and-media/media-centre/press-releases/2026/november/bsi-awards-its-50th-iso-iec-42001-certificate/ | 2026-10-21 (award date; URL path says 2026/november) | 2026-11-14 | A | Read | issuer page | ISO/IEC 42001 certificates |
| S64 | AI security jobs hiring (SANS tracker), Cybersecurity Dive, https://www.cybersecuritydive.com/news/ai-security-jobs-hiring-sans-tracker/833465/ | 2026-10-20 | 2026-11-14 | B | Read | | AI security posting counts |
| S65 | Which AI coding tools do developers actually use at work? (AI Pulse), JetBrains Research, https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/ | 2026-04 per URL (fieldwork 2026-01) | 2026-11-14 | B | Read | COI (Claude Code figures) | coding-agent adoption |
| S66 | State of Developer Ecosystem 2025, JetBrains Research, https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/ | 2025-10 per URL (fieldwork April to June 2025) | 2026-11-14 | B | Read | | AI use among developers; TypeScript rise |
| S67 | The 2025 State of AI report, OpenRouter with a16z, https://openrouter.ai/blog/insights/the-2025-state-of-ai-report/ | 2025 (month not stated) | 2026-11-14 | C | Read | no provider shares in the text opened | disconfirming check for K10; no figure used |
| S68 | Voice AI engineering jobs, voiceaispace, https://www.voiceaispace.com/jobs/engineering | undated | 2026-11-14 | C | Extract | search snippet | existence of a voice-AI job board |
| S69 | Pages the fetch tool refused or could not open: https://github.com/huggingface/text-generation-inference ; https://pypi.org/project/ragas/ ; https://hiringlab.indeed.com/2026/01/22/january-labor-market-update-jobs-mentioning-ai-are-growing-amid-broader-hiring-weakness/ ; https://hiringlab.indeed.com/uk/blog/2026/03/30/uk-labour-market-is-cooling-but-ai-hiring-is-bucking-the-trend/ ; https://pub.towardsai.net/mcp-registries-in-mid-2026-one-upstream-won-2ce541b92036 ; https://yourstory.com/enterprise-story/2026/11/gccs-increase-hiring-of-techies-with-ai-data-cybersecurity-skills ; https://www.techrepublic.com/article/news-gcc-ai-cloud-hiring-apac-india/ | n/a | 2026-11-14 | E | Blocked | not on the fetch allowlist, failed to load, or cut off by the account's usage limit; no workaround tried | none; see Absences |


## Data Appendix

One JSON object per line, in three blocks. Conventions: `share` in `skill_signal` records is a fraction of postings (0.784 means 78.4%); percentages in `measure` records are in percent units, with the unit named in `unit`; event records use `unit` "date" and an ISO date in `value`; `as_of` for a monthly figure is the last day of the month covered, and is null where the source gives no date (the period is then in `note`); `n` is null where the source does not state it; skill IDs are written `new:<slug>` because the brief gives no skill IDs, and role names are the brief's role names. Rows about MCP, Claude Code and Ramp's Anthropic share carry COI in `note`.

**Skill signals**

```jsonl
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:python", "n": null, "source_kind": "platform", "share": 0.784, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:llm", "n": null, "source_kind": "platform", "share": 0.767, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:agentic-ai", "n": null, "source_kind": "platform", "share": 0.593, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:rag", "n": null, "source_kind": "platform", "share": 0.54, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:machine-learning", "n": null, "source_kind": "platform", "share": 0.398, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:ai", "n": null, "source_kind": "platform", "share": 0.378, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:generative-ai", "n": null, "source_kind": "platform", "share": 0.376, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:azure", "n": null, "source_kind": "platform", "share": 0.351, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:aws", "n": null, "source_kind": "platform", "share": 0.351, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:ci-cd", "n": null, "source_kind": "platform", "share": 0.344, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:vector-databases", "n": null, "source_kind": "platform", "share": 0.326, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": "AI Engineer", "skill": "new:prompt-engineering", "n": null, "source_kind": "platform", "share": 0.311, "as_of": "2026-09-10", "ttl": "V3", "grade": "B", "src": ["S1"], "note": "fraction of AI Engineer postings; n not stated; shares overlap"}
{"type": "skill_signal", "role": null, "skill": "new:langchain", "n": 534, "source_kind": "platform", "share": 0.343, "count": 183, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:langgraph", "n": 534, "source_kind": "platform", "share": 0.221, "count": 118, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:llamaindex", "n": 534, "source_kind": "platform", "share": 0.139, "count": 74, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:crewai", "n": 534, "source_kind": "platform", "share": 0.109, "count": 58, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:autogen", "n": 534, "source_kind": "platform", "share": 0.079, "count": 42, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:n8n", "n": 534, "source_kind": "platform", "share": 0.034, "count": 18, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:semantic-kernel", "n": 534, "source_kind": "platform", "share": 0.024, "count": 13, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:pydantic-ai", "n": 534, "source_kind": "platform", "share": 0.024, "count": 13, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "listings on one agentic job board; role titles not stated; tagging method not described"}
{"type": "skill_signal", "role": null, "skill": "new:mcp", "n": 213, "source_kind": "platform", "share": 0.169, "count": 36, "as_of": "2026-04-19", "ttl": "V3", "grade": "C", "src": ["S22"], "note": "denominator is the 213 LangChain- or LangGraph-tagged listings, not all 534; COI (MCP)"}
```

**Measures**

```jsonl
{"type": "measure", "subject": "skill:python", "measure": "survey_use_share", "unit": "percent of respondents", "value": 57.9, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S3"]}
{"type": "measure", "subject": "skill:typescript", "measure": "survey_use_share", "unit": "percent of respondents", "value": 43.6, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:javascript", "measure": "survey_use_share", "unit": "percent of respondents", "value": 66, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:sql", "measure": "survey_use_share", "unit": "percent of respondents", "value": 58.6, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S3"]}
{"type": "measure", "subject": "skill:rust", "measure": "survey_use_share", "unit": "percent of respondents", "value": 14.8, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:aws", "measure": "survey_use_share", "unit": "percent of respondents", "value": 43.3, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:azure", "measure": "survey_use_share", "unit": "percent of respondents", "value": 26.3, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:gcp", "measure": "survey_use_share", "unit": "percent of respondents", "value": 24.6, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S4"]}
{"type": "measure", "subject": "skill:python", "measure": "survey_use_change_vs_prior_year", "unit": "percentage points", "value": 7, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S3"], "note": "Python rose 7 points against the 2024 survey"}
{"type": "measure", "subject": "skill:ai-agents", "measure": "survey_use_share", "unit": "percent of respondents", "value": 30.9, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S3"], "note": "14.1% daily; 17.4% plan to use; 37.9% do not plan to"}
{"type": "measure", "subject": "skill:ai-tools", "measure": "survey_use_or_plan_share", "unit": "percent of respondents", "value": 84, "n": 49000, "method": "annual developer survey, all respondents; as_of is the publication date; n stated as 49,000+", "as_of": "2025-07-29", "ttl": "V3", "grade": "B", "src": ["S3"], "note": "76% in the 2024 survey"}
{"type": "measure", "subject": "skill:ai-tools", "measure": "survey_use_or_plan_share", "unit": "percent of respondents", "value": 76, "as_of": null, "ttl": "V3", "grade": "B", "src": ["S3"], "note": "2024 survey value as stated in the 2025 survey summary; the 2024 publication date was not seen"}
{"type": "measure", "subject": "skill:javascript", "measure": "survey_use_share", "unit": "percent of respondents", "value": 62, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"]}
{"type": "measure", "subject": "skill:sql", "measure": "survey_use_share", "unit": "percent of respondents", "value": 58, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"]}
{"type": "measure", "subject": "skill:python", "measure": "survey_use_share", "unit": "percent of respondents", "value": 58, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"]}
{"type": "measure", "subject": "skill:html-css", "measure": "survey_use_share", "unit": "percent of respondents", "value": 58, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"]}
{"type": "measure", "subject": "skill:coding-agents", "measure": "survey_use_share", "unit": "percent of AI users", "value": 66, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"], "note": "denominator differs from the 2025 agent figure; 63% of AI users use chatbots"}
{"type": "measure", "subject": "skill:ai-coding-tools", "measure": "survey_daily_use_share", "unit": "percent of AI coding-assistant and agent users", "value": 73, "n": 30000, "method": "annual developer survey; more than 30,000 respondents; as_of is the publication date", "as_of": "2026-10-06", "ttl": "V3", "grade": "B", "src": ["S5"]}
{"type": "measure", "subject": "skill:claude-code", "measure": "work_adoption_share", "unit": "percent of developers", "value": 3, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2025-06-30", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "about 3% (April to June 2025 wave); COI (Anthropic product)"}
{"type": "measure", "subject": "skill:claude-code", "measure": "work_adoption_share", "unit": "percent of developers", "value": 18, "n": 10000, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2026-01-31", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "January 2026 wave; 1.5 times the September 2025 level; COI (Anthropic product)"}
{"type": "measure", "subject": "skill:claude-code", "measure": "awareness_share", "unit": "percent of developers", "value": 31, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2025-06-30", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "COI (Anthropic product)"}
{"type": "measure", "subject": "skill:claude-code", "measure": "awareness_share", "unit": "percent of developers", "value": 49, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2025-09-30", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "COI (Anthropic product)"}
{"type": "measure", "subject": "skill:claude-code", "measure": "awareness_share", "unit": "percent of developers", "value": 57, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2026-01-31", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "COI (Anthropic product)"}
{"type": "measure", "subject": "skill:github-copilot", "measure": "work_adoption_share", "unit": "percent of developers", "value": 29, "n": 10000, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2026-01-31", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "growth stalled since the previous year"}
{"type": "measure", "subject": "skill:cursor", "measure": "work_adoption_share", "unit": "percent of developers", "value": 18, "n": 10000, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2026-01-31", "ttl": "V3", "grade": "B", "src": ["S65"]}
{"type": "measure", "subject": "skill:openai-codex", "measure": "work_adoption_share", "unit": "percent of developers", "value": 3, "n": 10000, "method": "JetBrains AI Pulse; professional developers worldwide; share using at work (adoption) or aware (awareness)", "as_of": "2026-01-31", "ttl": "V3", "grade": "B", "src": ["S65"], "note": "before the Codex desktop app launch"}
{"type": "measure", "subject": "skill:ai-tools", "measure": "regular_use_share", "unit": "percent of developers", "value": 85, "n": 24534, "method": "JetBrains State of Developer Ecosystem 2025; fieldwork April to June 2025", "as_of": "2025-06-30", "ttl": "V3", "grade": "B", "src": ["S66"], "note": "62% use at least one AI coding assistant, agent or editor"}
{"type": "measure", "subject": "skill:typescript", "measure": "github_monthly_contributors", "unit": "contributors", "value": 2636006, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"], "note": "ranked first among languages"}
{"type": "measure", "subject": "skill:typescript", "measure": "github_contributors_yoy_change", "unit": "percent", "value": 66.63, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"]}
{"type": "measure", "subject": "skill:python", "measure": "github_contributors_yoy_change", "unit": "percent", "value": 48.78, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"]}
{"type": "measure", "subject": "skill:javascript", "measure": "github_contributors_yoy_change", "unit": "percent", "value": 24.79, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"]}
{"type": "measure", "subject": "skill:llm-sdk-imports", "measure": "github_public_repositories", "unit": "repositories", "value": 1100000, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"], "note": "more than 1.1 million; 693,867 created in the 12 months to August 2025"}
{"type": "measure", "subject": "skill:llm-sdk-imports", "measure": "github_public_repositories_yoy_change", "unit": "percent", "value": 178, "method": "GitHub Octoverse 2025; monthly contributors; data to August 2025", "as_of": "2025-08-31", "ttl": "V4", "grade": "B", "src": ["S6"]}
{"type": "measure", "subject": "market:india", "measure": "github_developers", "unit": "developers", "value": 21900000, "region": "IN", "as_of": null, "ttl": "V4", "grade": "B", "src": ["S6"], "note": "stated as the 2025 figure; more than 5 million added in 2025"}
{"type": "measure", "subject": "market:india", "measure": "github_developers", "unit": "developers", "value": 4500000, "region": "IN", "as_of": null, "ttl": "V4", "grade": "B", "src": ["S6"], "note": "stated as the 2020 figure"}
{"type": "measure", "subject": "skill:mcp", "measure": "github_stars", "unit": "stars", "value": 37000, "as_of": null, "ttl": "V1", "grade": "B", "src": ["S6"], "note": "GitHub states 37 thousand stars in eight months (window ending 2025-08); COI (MCP)"}
{"type": "measure", "subject": "provider:openai", "measure": "usage_share", "unit": "percent", "value": 63, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": "2026-04-21", "ttl": "V3", "grade": "B", "src": ["S15"], "note": "unit of the share not named in the text read; OpenAI customer count more than doubled"}
{"type": "measure", "subject": "provider:openai", "measure": "usage_share", "unit": "percent", "value": 75, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": null, "ttl": "V3", "grade": "B", "src": ["S15"], "note": "a year before the report; the period is not dated on the page"}
{"type": "measure", "subject": "provider:anthropic", "measure": "usage_share_change", "unit": "percentage points", "value": 23, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": "2026-04-21", "ttl": "V3", "grade": "B", "src": ["S15"], "note": "gain over the year; the resulting share is not stated"}
{"type": "measure", "subject": "provider:google", "measure": "usage_share_change", "unit": "percentage points", "value": 20, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": "2026-04-21", "ttl": "V3", "grade": "B", "src": ["S15"], "note": "gain over the year; the resulting share is not stated"}
{"type": "measure", "subject": "skill:multi-model-use", "measure": "orgs_using_three_or_more_models", "unit": "percent of organisations", "value": 70, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": "2026-04-21", "ttl": "V3", "grade": "B", "src": ["S15"], "note": "more than 70%"}
{"type": "measure", "subject": "skill:agent-frameworks", "measure": "org_adoption_share", "unit": "percent of organisations", "value": 18, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": "2026-04-21", "ttl": "V3", "grade": "B", "src": ["S15"], "note": "almost 18% in early 2026"}
{"type": "measure", "subject": "skill:agent-frameworks", "measure": "org_adoption_share", "unit": "percent of organisations", "value": 9, "n": 1000, "method": "telemetry from more than 1,000 Datadog customers using LLM Observability; customers skew cloud-mature", "as_of": null, "ttl": "V3", "grade": "B", "src": ["S15"], "note": "more than 9% in early 2025; day not stated"}
{"type": "measure", "subject": "provider:openai", "measure": "traced_traffic_share", "unit": "percent", "value": 82.7, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2024-10-31", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "October 2024; month-level figure"}
{"type": "measure", "subject": "provider:openai", "measure": "traced_traffic_share", "unit": "percent", "value": 55.3, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2025-09-30", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "September 2025; month-level figure"}
{"type": "measure", "subject": "provider:google", "measure": "traced_traffic_share", "unit": "percent", "value": 0.5, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2024-10-31", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "October 2024; month-level figure"}
{"type": "measure", "subject": "provider:google", "measure": "traced_traffic_share", "unit": "percent", "value": 13.1, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2025-09-30", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "September 2025; month-level figure"}
{"type": "measure", "subject": "provider:anthropic", "measure": "traced_traffic_share", "unit": "percent", "value": 6.8, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2024-10-31", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "October 2024; month-level figure"}
{"type": "measure", "subject": "provider:anthropic", "measure": "traced_traffic_share", "unit": "percent", "value": 7.3, "n": 20000, "method": "Langfuse Cloud traced traffic; more than 20,000 organisations; self-hosted excluded", "as_of": "2025-09-30", "ttl": "V3", "grade": "B", "src": ["S13"], "note": "September 2025; month-level figure"}
{"type": "measure", "subject": "provider:openai", "measure": "paid_teams_using_per_100", "unit": "teams per 100 paid teams", "value": 70, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "December 2025; COI (vendor data; includes Anthropic share)"}
{"type": "measure", "subject": "provider:openai", "measure": "paid_teams_using_per_100", "unit": "teams per 100 paid teams", "value": 55, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "October 2026; COI (vendor data; includes Anthropic share)"}
{"type": "measure", "subject": "provider:anthropic", "measure": "paid_teams_using_per_100", "unit": "teams per 100 paid teams", "value": 48, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "December 2025; COI (vendor data; includes Anthropic share)"}
{"type": "measure", "subject": "provider:anthropic", "measure": "paid_teams_using_per_100", "unit": "teams per 100 paid teams", "value": 54, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "October 2026; COI (vendor data; includes Anthropic share)"}
{"type": "measure", "subject": "skill:llm-model-versions", "measure": "model_half_life", "unit": "weeks", "value": 6, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "about six weeks; report estimate"}
{"type": "measure", "subject": "skill:llm-model-versions", "measure": "median_version_replacement_interval", "unit": "days", "value": 61, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S14"]}
{"type": "measure", "subject": "skill:voice-models", "measure": "paid_teams_using_share", "unit": "percent of paid teams", "value": 4, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-07-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "about 4% in July 2026; voice figures begin 2026-06-22"}
{"type": "measure", "subject": "skill:voice-models", "measure": "paid_teams_using_share", "unit": "percent of paid teams", "value": 11, "method": "Vercel AI Gateway; anonymised traffic through the gateway; paid teams have at least one paid request in the month", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S14"], "note": "about 11% in October 2026 (10.7% in the chart)"}
{"type": "measure", "subject": "skill:multi-model-use", "measure": "cios_using_three_or_more_model_families", "unit": "percent of CIOs", "value": 81, "n": 100, "method": "a16z survey of Forbes Global 2000 CIOs reported by eMarketer", "as_of": null, "ttl": "V3", "grade": "C", "src": ["S12"], "note": "survey date not stated; COI"}
{"type": "measure", "subject": "skill:multi-model-use", "measure": "cios_using_three_or_more_model_families", "unit": "percent of CIOs", "value": 68, "n": 100, "method": "a16z survey of Forbes Global 2000 CIOs reported by eMarketer", "as_of": null, "ttl": "V3", "grade": "C", "src": ["S12"], "note": "a year earlier; COI"}
{"type": "measure", "subject": "provider:anthropic", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 16.7, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:anthropic", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 19.5, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-01-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:anthropic", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 43.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-08-31", "ttl": "V1", "grade": "B", "src": ["S18"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:anthropic", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 44.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:openai", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 36.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:openai", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 35.9, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-01-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "provider:openai", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 40.6, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "COI (Anthropic comparison)"}
{"type": "measure", "subject": "skill:paid-ai-adoption", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 46.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-01-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "any paid AI vendor; COI (Anthropic comparison)"}
{"type": "measure", "subject": "skill:paid-ai-adoption", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 55.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "any paid AI vendor; COI (Anthropic comparison)"}
{"type": "measure", "subject": "skill:paid-ai-adoption", "measure": "business_adoption_share", "unit": "percent of US businesses on Ramp", "value": 56.8, "n": 85000, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-10-31", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "any paid AI vendor; COI (Anthropic comparison)"}
{"type": "measure", "subject": "skill:multi-vendor-ai-payers", "measure": "share_paying_for_openai_and_anthropic", "unit": "percent of US businesses on Ramp", "value": 16, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-01-31", "ttl": "V1", "grade": "B", "src": ["S17"], "note": "COI"}
{"type": "measure", "subject": "skill:multi-vendor-ai-payers", "measure": "share_paying_for_openai_and_anthropic", "unit": "percent of US businesses on Ramp", "value": 8, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": null, "ttl": "V1", "grade": "B", "src": ["S17"], "note": "a year earlier than 2026-01; COI"}
{"type": "measure", "subject": "provider:anthropic", "measure": "weekly_token_spend_share", "unit": "percent", "value": 53.2, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-10-04", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "week ending 2026-10-04; COI"}
{"type": "measure", "subject": "provider:anthropic", "measure": "weekly_token_spend_share", "unit": "percent", "value": 49.3, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-11-01", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "week ending 2026-11-01; COI"}
{"type": "measure", "subject": "provider:openai", "measure": "weekly_token_spend_share", "unit": "percent", "value": 42.3, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-10-04", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "week ending 2026-10-04; COI"}
{"type": "measure", "subject": "provider:openai", "measure": "weekly_token_spend_share", "unit": "percent", "value": 46.1, "method": "Ramp card and bill-pay data; US businesses with a positive transaction in the month; likely undercounts", "as_of": "2026-11-01", "ttl": "V1", "grade": "B", "src": ["S16"], "note": "week ending 2026-11-01; COI"}
{"type": "measure", "subject": "market:india-ai-ml-hiring", "measure": "yoy_change", "unit": "percent", "value": 49, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-02-28", "ttl": "V1", "grade": "B", "src": ["S7"]}
{"type": "measure", "subject": "market:india-ai-ml-hiring", "measure": "yoy_change", "unit": "percent", "value": 22, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-05-31", "ttl": "V1", "grade": "B", "src": ["S8"]}
{"type": "measure", "subject": "market:india-ai-ml-hiring", "measure": "yoy_change", "unit": "percent", "value": 25, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-06-30", "ttl": "V1", "grade": "B", "src": ["S9"], "note": "across 14 sectors"}
{"type": "measure", "subject": "market:india-ai-ml-hiring", "measure": "yoy_change", "unit": "percent", "value": 33, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-07-31", "ttl": "V1", "grade": "C", "src": ["S11"], "note": "Info Edge figure seen in a search snippet"}
{"type": "measure", "subject": "market:india-ai-ml-hiring", "measure": "yoy_change", "unit": "percent", "value": 20, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"]}
{"type": "measure", "subject": "market:india-it-software-services-hiring", "measure": "yoy_change", "unit": "percent", "value": 6, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-02-28", "ttl": "V1", "grade": "B", "src": ["S7"]}
{"type": "measure", "subject": "market:india-it-software-services-hiring", "measure": "yoy_change", "unit": "percent", "value": -7, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-05-31", "ttl": "V1", "grade": "B", "src": ["S8"]}
{"type": "measure", "subject": "market:india-it-software-services-hiring", "measure": "yoy_change", "unit": "percent", "value": -3, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-06-30", "ttl": "V1", "grade": "B", "src": ["S9"], "note": "IT listings"}
{"type": "measure", "subject": "market:india-it-software-services-hiring", "measure": "yoy_change", "unit": "percent", "value": -4, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"]}
{"type": "measure", "subject": "market:india-ai-ml-hiring-within-it", "measure": "yoy_change", "unit": "percent", "value": 16, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-06-30", "ttl": "V1", "grade": "B", "src": ["S9"]}
{"type": "measure", "subject": "market:india-ai-ml-hiring-within-it", "measure": "yoy_change", "unit": "percent", "value": 11, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"]}
{"type": "measure", "subject": "market:india-white-collar-hiring", "measure": "jobspeak_index", "unit": "index points (base 2008-07 = 1000)", "value": 3233, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-02-28", "ttl": "V1", "grade": "B", "src": ["S7"]}
{"type": "measure", "subject": "market:india-white-collar-hiring", "measure": "jobspeak_index", "unit": "index points (base 2008-07 = 1000)", "value": 3053, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"]}
{"type": "measure", "subject": "market:india-ai-ml-in-it-13-16-years", "measure": "yoy_change", "unit": "percent", "value": 54, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"], "note": "AI/ML hiring within IT by experience band"}
{"type": "measure", "subject": "market:india-ai-ml-in-it-8-12-years", "measure": "yoy_change", "unit": "percent", "value": 28, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"], "note": "AI/ML hiring within IT by experience band"}
{"type": "measure", "subject": "market:india-ai-ml-in-it-freshers", "measure": "yoy_change", "unit": "percent", "value": 19, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-09-30", "ttl": "V1", "grade": "B", "src": ["S10"], "note": "AI/ML hiring within IT by experience band"}
{"type": "measure", "subject": "market:india-ai-hiring-hyderabad", "measure": "yoy_change", "unit": "percent", "value": 44, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-05-31", "ttl": "V1", "grade": "B", "src": ["S8"]}
{"type": "measure", "subject": "market:india-ai-hiring-ncr", "measure": "yoy_change", "unit": "percent", "value": 34, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-05-31", "ttl": "V1", "grade": "B", "src": ["S8"]}
{"type": "measure", "subject": "market:india-ai-hiring-chennai", "measure": "yoy_change", "unit": "percent", "value": 31, "method": "Naukri JobSpeak index of new postings and recruiter searches; sample size not stated; free listings can inflate it", "region": "IN", "as_of": "2026-05-31", "ttl": "V1", "grade": "B", "src": ["S8"]}
{"type": "measure", "subject": "market:india-job-postings", "measure": "ai_mention_share", "unit": "percent of postings", "value": 8.2, "method": "Indeed postings that reference AI", "region": "IN", "as_of": "2024-09-30", "ttl": "V3", "grade": "B", "src": ["S61"]}
{"type": "measure", "subject": "market:india-job-postings", "measure": "ai_mention_share", "unit": "percent of postings", "value": 10.6, "method": "Indeed postings that reference AI", "region": "IN", "as_of": "2025-06-30", "ttl": "V3", "grade": "B", "src": ["S61"]}
{"type": "measure", "subject": "market:india-job-postings", "measure": "ai_mention_share", "unit": "percent of postings", "value": 11.7, "method": "Indeed postings that reference AI", "region": "IN", "as_of": "2025-09-30", "ttl": "V3", "grade": "B", "src": ["S61"]}
{"type": "measure", "subject": "market:india-software-development-postings", "measure": "postings_change_three_months", "unit": "percent", "value": -12.3, "method": "Indeed postings", "region": "IN", "as_of": "2026-05-31", "ttl": "V3", "grade": "B", "src": ["S62"], "note": "over three months to about May 2026"}
{"type": "measure", "subject": "market:us-job-postings", "measure": "ai_mention_share", "unit": "percent of postings", "value": 4.2, "method": "Indeed Hiring Lab, as reported by eWeek", "region": "US", "as_of": null, "ttl": "V3", "grade": "B", "src": ["S46"], "note": "record; late 2025; up 134% since 2020; exact date not stated"}
{"type": "measure", "subject": "title:agentic-ai-engineer", "measure": "posting_growth_2026_vs_2025", "unit": "percent", "value": 260, "method": "CIEL HR job-posting data, March 2024 to May 2026", "region": "IN", "as_of": "2026-05-31", "ttl": "V3", "grade": "C", "src": ["S60"], "note": "denominators not stated"}
{"type": "measure", "subject": "title:genai-solutions-architect", "measure": "posting_growth_2026_vs_2025", "unit": "percent", "value": 120, "method": "CIEL HR job-posting data, March 2024 to May 2026", "region": "IN", "as_of": "2026-05-31", "ttl": "V3", "grade": "C", "src": ["S60"], "note": "denominators not stated"}
{"type": "measure", "subject": "title:llm-engineer", "measure": "posting_growth_2026_vs_2025", "unit": "percent", "value": 86.5, "method": "CIEL HR job-posting data, March 2024 to May 2026", "region": "IN", "as_of": "2026-05-31", "ttl": "V3", "grade": "C", "src": ["S60"], "note": "denominators not stated"}
{"type": "measure", "subject": "title:mlops-engineer", "measure": "posting_growth_2026_vs_2025", "unit": "percent", "value": 82.2, "method": "CIEL HR job-posting data, March 2024 to May 2026", "region": "IN", "as_of": "2026-05-31", "ttl": "V3", "grade": "C", "src": ["S60"], "note": "denominators not stated"}
{"type": "measure", "subject": "protocol:mcp", "measure": "aaif_members", "unit": "members", "value": 146, "as_of": "2026-02-24", "ttl": "V2", "grade": "A", "src": ["S29"], "note": "Agentic AI Foundation; 97 new Gold and Silver members since launch; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_unique_servers", "unit": "servers", "value": 9650, "method": "one author pull of the official MCP registry API", "as_of": "2026-05-31", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "about 9,650 (author's figure); month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_unique_servers", "unit": "servers", "value": 30375, "method": "one author pull of the official MCP registry API", "as_of": "2026-09-10", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "from 99,114 server-version records; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 407, "method": "one author pull of the official MCP registry API", "as_of": "2025-09-30", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 1081, "method": "one author pull of the official MCP registry API", "as_of": "2026-02-28", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 2387, "method": "one author pull of the official MCP registry API", "as_of": "2026-04-30", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 3662, "method": "one author pull of the official MCP registry API", "as_of": "2026-06-30", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 4840, "method": "one author pull of the official MCP registry API", "as_of": "2026-07-31", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_servers_first_published_in_month", "unit": "servers", "value": 6265, "method": "one author pull of the official MCP registry API", "as_of": "2026-08-31", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "month-level; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_share_not_updated_three_months", "unit": "percent", "value": 36, "method": "one author pull of the official MCP registry API", "as_of": "2026-09-10", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "about 36%; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "registry_share_single_version", "unit": "percent", "value": 62, "method": "one author pull of the official MCP registry API", "as_of": "2026-09-10", "ttl": "V1", "grade": "C", "src": ["S32"], "note": "COI (MCP)"}
{"type": "measure", "subject": "protocol:a2a", "measure": "supporting_organisations", "unit": "organisations", "value": 50, "as_of": "2025-04-30", "ttl": "V3", "grade": "C", "src": ["S33"], "note": "more than 50 in April 2025; project-stated"}
{"type": "measure", "subject": "protocol:a2a", "measure": "supporting_organisations", "unit": "organisations", "value": 150, "as_of": "2026-04-09", "ttl": "V3", "grade": "C", "src": ["S33"], "note": "more than 150; project-stated"}
{"type": "measure", "subject": "skill:langchain", "measure": "monthly_downloads", "unit": "downloads", "value": 157554330, "method": "pepy.tech last 30 days; includes CI and mirrors", "as_of": "2026-11-11", "ttl": "V1", "grade": "B", "src": ["S41"]}
{"type": "measure", "subject": "skill:langgraph", "measure": "monthly_downloads", "unit": "downloads", "value": 58965017, "method": "pepy.tech last 30 days; includes CI and mirrors", "as_of": "2026-11-11", "ttl": "V1", "grade": "B", "src": ["S42"]}
{"type": "measure", "subject": "skill:langchain", "measure": "monthly_downloads", "unit": "downloads", "value": 90000000, "method": "vendor statement \"90M monthly downloads\"", "as_of": "2025-10-22", "ttl": "V1", "grade": "C", "src": ["S55"], "note": "counter and month not stated; not comparable with pepy.tech"}
{"type": "measure", "subject": "skill:pinecone", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 3.24, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:pinecone", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 7.95, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "skill:milvus", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 2.81, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:milvus", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 5.0, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "skill:qdrant", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 1.84, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:qdrant", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 4.39, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "skill:weaviate", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 1.7, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:weaviate", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 4.18, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "skill:chroma", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 1.87, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:chroma", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 2.57, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "skill:elasticsearch", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 132.32, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2024-12-31", "ttl": "V1", "grade": "M", "src": ["S40"], "note": "my arithmetic from the change columns of the December 2025 page (plus or minus 0.01)"}
{"type": "measure", "subject": "skill:elasticsearch", "measure": "dbengines_vector_dbms_score", "unit": "score", "value": 109.83, "method": "DB-Engines vector DBMS popularity score (mentions, searches, job offers and similar)", "as_of": "2025-12-31", "ttl": "V1", "grade": "B", "src": ["S40"], "note": "December 2025 ranking, read from the page fetched on 2026-11-14"}
{"type": "measure", "subject": "tool:openai-assistants-api", "measure": "sunset_date", "unit": "date", "value": "2026-08-26", "as_of": "2026-08-26", "ttl": "V6", "grade": "A", "src": ["S44"], "note": "Responses API and Conversations API replace it"}
{"type": "measure", "subject": "tool:autogen-agentchat", "measure": "last_pypi_release_date", "unit": "date", "value": "2025-09-30", "as_of": "2025-09-30", "ttl": "V6", "grade": "A", "src": ["S36"], "note": "version 0.7.5; 54 releases in all; none in the 12 months to 2026-11-13"}
{"type": "measure", "subject": "tool:microsoft-agent-framework", "measure": "release_candidate_date", "unit": "date", "value": "2026-02-19", "as_of": "2026-02-19", "ttl": "V6", "grade": "A", "src": ["S34"], "note": "described as the successor to Semantic Kernel and AutoGen"}
{"type": "measure", "subject": "tool:microsoft-agent-framework", "measure": "general_availability_date", "unit": "date", "value": "2026-04-03", "as_of": "2026-04-03", "ttl": "V6", "grade": "B", "src": ["S35"], "note": "article dated April 3; year inferred from its references"}
{"type": "measure", "subject": "tool:text-generation-inference", "measure": "maintenance_mode_notice_date", "unit": "date", "value": null, "as_of": "2026-11-14", "ttl": "V2", "grade": "A", "src": ["S38"], "note": "documentation notice is undated; recommends vLLM, SGLang and llama.cpp or MLX"}
{"type": "measure", "subject": "tool:text-generation-inference", "measure": "archived_date", "unit": "date", "value": "2026-03-21", "as_of": "2026-03-21", "ttl": "V6", "grade": "C", "src": ["S39"], "note": "one secondary source; GitHub banner not opened"}
{"type": "measure", "subject": "tool:tensorrt-llm", "measure": "tensorrt_backend_removal_doc_updated", "unit": "date", "value": "2026-11-03", "as_of": "2026-11-03", "ttl": "V2", "grade": "A", "src": ["S23"], "note": "page lists removal of the TensorRT backend, trtllm-build, trtllm-refit, trtllm-prune and convert_checkpoint.py; PyTorch is the sole backend"}
{"type": "measure", "subject": "tool:torchtune", "measure": "maintenance_status_date", "unit": "date", "value": null, "as_of": "2026-11-14", "ttl": "V2", "grade": "A", "src": ["S57"], "note": "README says no longer actively maintained; development wound down in 2025"}
{"type": "measure", "subject": "tool:langfuse", "measure": "acquisition_announced_date", "unit": "date", "value": "2026-01-16", "as_of": "2026-01-16", "ttl": "V6", "grade": "B", "src": ["S26", "S27"], "note": "acquirer ClickHouse; the issuer page is undated"}
{"type": "measure", "subject": "tool:promptfoo", "measure": "acquisition_announced_date", "unit": "date", "value": "2026-03-09", "as_of": "2026-03-09", "ttl": "V6", "grade": "A", "src": ["S25"], "note": "acquirer OpenAI; closing subject to customary conditions; closing not verified"}
{"type": "measure", "subject": "tool:helicone", "measure": "acquisition_announced_date", "unit": "date", "value": "2026-03-03", "as_of": "2026-03-03", "ttl": "V6", "grade": "C", "src": ["S28"], "note": "acquirer Mintlify; maintenance mode"}
{"type": "measure", "subject": "tool:traceloop", "measure": "acquisition_completed_date", "unit": "date", "value": "2026-05-05", "as_of": "2026-05-05", "ttl": "V6", "grade": "C", "src": ["S28"], "note": "acquirer ServiceNow"}
{"type": "measure", "subject": "tool:galileo", "measure": "acquisition_completed_date", "unit": "date", "value": "2026-05-22", "as_of": "2026-05-22", "ttl": "V6", "grade": "C", "src": ["S28"], "note": "acquirer Cisco (Splunk)"}
{"type": "measure", "subject": "tool:wandb-weave", "measure": "acquisition_completed_date", "unit": "date", "value": "2025-05-05", "as_of": "2025-05-05", "ttl": "V6", "grade": "C", "src": ["S28"], "note": "acquirer CoreWeave"}
{"type": "measure", "subject": "tool:humanloop", "measure": "platform_sunset_date", "unit": "date", "value": "2025-09-08", "as_of": "2025-09-08", "ttl": "V6", "grade": "C", "src": ["S28"], "note": "team joined Anthropic (COI); billing stopped 2025-07-30"}
{"type": "measure", "subject": "protocol:mcp", "measure": "specification_revision_date", "unit": "date", "value": "2026-07-28", "as_of": "2026-07-28", "ttl": "V6", "grade": "A", "src": ["S30"], "note": "removes protocol-level sessions; deprecates Roots, Sampling, Logging, HTTP+SSE and Dynamic Client Registration; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp", "measure": "specification_revision_date", "unit": "date", "value": "2025-11-25", "as_of": "2025-11-25", "ttl": "V6", "grade": "A", "src": ["S30"], "note": "revision before 2026-07-28; COI (MCP)"}
{"type": "measure", "subject": "protocol:mcp-apps", "measure": "launch_date", "unit": "date", "value": "2026-01-26", "as_of": "2026-01-26", "ttl": "V6", "grade": "A", "src": ["S29"], "note": "first official MCP extension; COI (MCP)"}
{"type": "measure", "subject": "protocol:a2a", "measure": "v1_release_date", "unit": "date", "value": "2026-04-09", "as_of": "2026-04-09", "ttl": "V6", "grade": "A", "src": ["S33"], "note": "described as the first stable specification"}
{"type": "measure", "subject": "tool:langchain", "measure": "v1_release_date", "unit": "date", "value": "2025-10-22", "as_of": "2025-10-22", "ttl": "V6", "grade": "A", "src": ["S55"], "note": "create_agent and middleware; legacy chains moved to langchain-classic"}
{"type": "measure", "subject": "tool:trl", "measure": "v1_release_date", "unit": "date", "value": "2026-03-31", "as_of": "2026-03-31", "ttl": "V6", "grade": "A", "src": ["S56"], "note": "more than 75 post-training methods"}
{"type": "measure", "subject": "tool:ragas", "measure": "release_candidate_date", "unit": "date", "value": "2026-11-13", "as_of": "2026-11-13", "ttl": "V6", "grade": "B", "src": ["S37"], "note": "v0.4.4rc1; previous release v0.4.3 on 2026-01-13"}
{"type": "measure", "subject": "tool:vllm", "measure": "pytorch_foundation_join_date", "unit": "date", "value": "2025-05-07", "as_of": "2025-05-07", "ttl": "V6", "grade": "A", "src": ["S43"], "note": "more than 46,500 GitHub stars and more than 1,000 contributors on that date"}
{"type": "measure", "subject": "regulation:eu-ai-act-omnibus", "measure": "provisional_agreement_date", "unit": "date", "value": "2026-05-07", "as_of": "2026-05-07", "ttl": "V6", "grade": "B", "src": ["S45"], "note": "Parliament adopted on 2026-06-16; Council approval pending on 2026-06-22; final adoption not verified"}
{"type": "measure", "subject": "tool:autogen-agentchat", "measure": "days_since_last_pypi_release", "unit": "days", "value": 410, "as_of": "2026-11-14", "ttl": "V1", "grade": "M", "src": ["S36"], "note": "from 2025-09-30 to 2026-11-14; my count"}
{"type": "measure", "subject": "tool:ragas", "measure": "days_between_v0_4_3_and_v0_4_4rc1", "unit": "days", "value": 304, "as_of": "2026-11-13", "ttl": "V6", "grade": "M", "src": ["S37"], "note": "from 2026-01-13 to 2026-11-13; my count"}
{"type": "measure", "subject": "title:ai-ml-security-engineer", "measure": "posting_count", "unit": "postings", "value": 850, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated; more than 850"}
{"type": "measure", "subject": "title:ai-red-team", "measure": "posting_count", "unit": "postings", "value": 100, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated; about 100; +13% week on week"}
{"type": "measure", "subject": "title:ai-grc-lead", "measure": "posting_count", "unit": "postings", "value": 430, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated; about 430 AI governance, risk and compliance leads"}
{"type": "measure", "subject": "title:ai-supply-chain-security", "measure": "posting_count", "unit": "postings", "value": 93, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated"}
{"type": "measure", "subject": "title:ai-security-specialist", "measure": "posting_count", "unit": "postings", "value": 48, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated"}
{"type": "measure", "subject": "title:ai-soc-orchestrator", "measure": "posting_count", "unit": "postings", "value": 36, "method": "SANS AI security job tracker as reported by Cybersecurity Dive; postings analysed in mid-September 2026", "as_of": "2026-09-15", "ttl": "V1", "grade": "B", "src": ["S64"], "note": "mid-September 2026, day not stated"}
{"type": "measure", "subject": "standard:iso-iec-42001", "measure": "bsi_certificates_issued_in_year", "unit": "certificates", "value": 11, "as_of": "2025-12-31", "ttl": "V4", "grade": "A", "src": ["S63"], "note": "BSI issued 11 in 2025"}
{"type": "measure", "subject": "standard:iso-iec-42001", "measure": "bsi_certificates_cumulative", "unit": "certificates", "value": 50, "as_of": "2026-10-21", "ttl": "V4", "grade": "A", "src": ["S63"], "note": "the 50th certificate awarded on this date; certified organisations in more than 16 countries including India"}
{"type": "measure", "subject": "skill:livekit", "measure": "funding_raised", "unit": "USD", "value": 100000000, "as_of": "2026-01-22", "ttl": "V6", "grade": "C", "src": ["S59"], "note": "Series C at a $1B valuation; company-stated"}
{"type": "measure", "subject": "skill:livekit", "measure": "developers_and_customers", "unit": "developers and customers", "value": 200000, "as_of": "2026-01-22", "ttl": "V3", "grade": "C", "src": ["S59"], "note": "more than 200,000; company-stated"}
{"type": "measure", "subject": "title:agent-architect", "measure": "exact_title_listings_seen", "unit": "listings", "value": 2, "as_of": "2026-11-14", "ttl": "V1", "grade": "C", "src": ["S49"], "note": "two exact listings on one aggregator; not a market count"}
{"type": "measure", "subject": "title:edge-ai-engineer", "measure": "exact_title_listings_seen", "unit": "listings", "value": 9, "as_of": "2026-11-14", "ttl": "V1", "grade": "C", "src": ["S52"], "note": "at least 9 distinct listings on one aggregator; not a market count"}
{"type": "measure", "subject": "title:ai-vibe-coding-engineer", "measure": "exact_title_listings_seen", "unit": "listings", "value": 4, "as_of": "2026-11-14", "ttl": "V1", "grade": "C", "src": ["S54"], "note": "Gruve; four listings on one aggregator; not a market count"}
{"type": "measure", "subject": "title:ai-developer-advocate", "measure": "employers_with_listings_seen", "unit": "employers", "value": 6, "as_of": "2026-11-14", "ttl": "V1", "grade": "C", "src": ["S53"], "note": "Temporal, MongoDB, Fireworks AI, Encord, LlamaIndex, Apple; not a market count"}
{"type": "measure", "subject": "title:distributed-training-engineer", "measure": "employers_with_listings_seen", "unit": "employers", "value": 2, "as_of": "2026-11-14", "ttl": "V1", "grade": "C", "src": ["S50"], "note": "Periodic Labs and OpenAI; not a market count"}
```

**Absences and rule**

```jsonl
{"type": "absence", "item": "Posting-share series at two dates for any GenAI skill (RAG, MCP, LangGraph, evaluation)", "searched": "JobsPipe AI Engineer page (one date, 2026-09-10, unchanged on 2026-11-14); one agentic job board (one date, 2026-04-19); Indeed Hiring Lab AI tracker repository (values not on the page); Naukri JobSpeak (category level only)", "grade": "E", "src": ["S1", "S22", "S47", "S10"], "as_of": "2026-11-14", "note": "No skill has a measured employer-demand trend"}
{"type": "absence", "item": "JobsPipe series for the other eleven titles named in the brief", "searched": "Pages not opened", "grade": "E", "src": ["S1"], "as_of": "2026-11-14", "note": "No second date for any title"}
{"type": "absence", "item": "Europe (EU and UK) posting series", "searched": "Indeed UK Hiring Lab page (refused by the fetch tool); no European labour-market source searched beyond the EU AI Act", "grade": "E", "src": ["S69"], "as_of": "2026-11-14"}
{"type": "absence", "item": "Package-download series for MCP SDKs, OpenAI Agents SDK, Claude Agent SDK, Google ADK, and npm", "searched": "Two searches (MCP package downloads on pypistats; a combined SDK downloads query); npm not searched", "grade": "E", "src": [], "as_of": "2026-11-14", "note": "No dated two-point series obtained"}
{"type": "absence", "item": "AG-UI adoption", "searched": "No search run", "grade": "E", "src": [], "as_of": "2026-11-14"}
{"type": "absence", "item": "Second dated count for vLLM, SGLang, llama.cpp and Ollama", "searched": "One search on vLLM and SGLang adoption; one on llama.cpp, Ollama and ExecuTorch", "grade": "E", "src": ["S43", "S58"], "as_of": "2026-11-14", "note": "Only vLLM on 2025-05-07 and llama.cpp and Ollama on 2026-10-07 were found"}
{"type": "absence", "item": "On-device and small-model tool series (CoreML, ONNX, ExecuTorch, small language models)", "searched": "The llama.cpp, Ollama and ExecuTorch search", "grade": "E", "src": [], "as_of": "2026-11-14", "note": "Star counts at one date only"}
{"type": "absence", "item": "Multimodal (other than voice) series", "searched": "No search run", "grade": "E", "src": [], "as_of": "2026-11-14"}
{"type": "absence", "item": "Posting shares for fine-tuning and post-training skills", "searched": "Not found in any source opened", "grade": "E", "src": [], "as_of": "2026-11-14"}
{"type": "absence", "item": "Second dated count for LangChain and LangGraph downloads", "searched": "pepy.tech (one snapshot, 2026-11-11); the vendor statement of 2025-10-22 uses another counter", "grade": "E", "src": ["S41", "S42", "S55"], "as_of": "2026-11-14", "note": "Not comparable; no series"}
{"type": "absence", "item": "Evaluation-platform share in postings (K5, K36)", "searched": "Searches for each figure wording; a vendor survey and an arXiv study were opened", "grade": "E", "src": ["S20", "S21"], "as_of": "2026-11-14", "note": "Not found"}
{"type": "absence", "item": "RAG share of 10.0% and Pinecone share of 0.7% in postings (K3, K4)", "searched": "Searches for each figure wording", "grade": "E", "src": ["S1"], "as_of": "2026-11-14", "note": "Not found; nearest data are AI Engineer posting shares"}
{"type": "absence", "item": "A newer Prompt Engineer title count than the arXiv sample (K1)", "searched": "One search on the title count; the arXiv paper was opened", "grade": "E", "src": ["S19"], "as_of": "2026-11-14", "note": "Not found"}
{"type": "absence", "item": "TGI archive banner and date on GitHub (K6)", "searched": "GitHub repository page", "grade": "E", "src": ["S69", "S39"], "as_of": "2026-11-14", "note": "Refused by the fetch tool; the archive date rests on one secondary source"}
{"type": "absence", "item": "RAGAS commit history on main (K8)", "searched": "GitHub and PyPI pages", "grade": "E", "src": ["S69", "S37"], "as_of": "2026-11-14", "note": "Refused by the fetch tool; the commit claim is unverified"}
{"type": "absence", "item": "Final adoption of the EU AI Act omnibus after 2026-06-22", "searched": "Sidley article only", "grade": "E", "src": ["S45"], "as_of": "2026-11-14", "note": "The Official Journal was not searched"}
{"type": "absence", "item": "A stable TensorRT-LLM release carrying the removal (K9)", "searched": "GitHub releases page, first 100,000 characters", "grade": "E", "src": ["S24"], "as_of": "2026-11-14", "note": "Release candidates only in the part read"}
{"type": "absence", "item": "Exact-title postings for K11, K12, K14, K21, K22, K24, K25 and K34; a Context Engineer count (K20)", "searched": "Combined title searches on 2026-11-14", "grade": "E", "src": ["S48"], "as_of": "2026-11-14", "note": "No exact hit, not searched, or no count"}
{"type": "absence", "item": "Learn, keep and drop evidence for Human Data & Evaluation Operations, Embodied & Physical AI, Independent & Fractional", "searched": "No search run", "grade": "E", "src": [], "as_of": "2026-11-14", "note": "Lists marked insufficient evidence"}
{"type": "absence", "item": "India GCC and skill-level series", "searched": "Leads surfaced in search results; the YourStory and TechRepublic GCC pages failed or were cut off by the usage limit", "grade": "E", "src": ["S69"], "as_of": "2026-11-14", "note": "No GCC skill series"}
{"type": "absence", "item": "OpenAI-Statsig and OpenAI-Neptune acquisitions", "searched": "Search results only", "grade": "E", "src": [], "as_of": "2026-11-14", "note": "Not opened; not counted"}
{"type": "rule", "jurisdiction": "EU", "instrument": "EU AI Act, Digital Omnibus amendment (provisional agreement of 2026-05-07)", "requirement": "Application date for Annex III high-risk obligations moves from 2026-08-02 to 2027-12-02; Annex I systems to 2028-08-02; transparency and watermarking obligations to 2026-12-02 for systems placed on the market before 2026-08-02", "status": "pending", "url": "https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/", "applies_to": "providers and deployers of high-risk AI systems", "effective": "2027-12-02", "as_of": "2026-06-22", "ttl": "V0", "grade": "B", "src": ["S45"], "note": "Parliament adopted on 2026-06-16; Council approval pending on 2026-06-22; final adoption not verified; the source is a law-firm article, not the Official Journal"}
```
