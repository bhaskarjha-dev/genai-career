---
id: T0-16
title: "Agentic Protocol Stack (MCP / A2A / ACP / AG-UI): Standardization Status and Enterprise Hiring Demand, October 2026"
date: 2026-10-21
status: complete
topic: agentic-protocol-standardization-and-enterprise-demand
tags:
  - mcp
  - a2a
  - acp
  - ag-ui
  - aaif
  - linux-foundation
  - agent-gateway
  - oauth
  - agent-security
  - hiring-demand
  - evidence-graded
informs_decisions:
  - adopt-mcp-2026-07-28-as-default-internal-tool-integration-standard
  - agent-gateway-build-vs-buy
  - dedicated-agent-gateway-engineer-requisitions-vs-fold-into-platform-security-roles
  - protocol-level-skill-requirements-in-agent-engineering-job-descriptions
confidence:
  overall: medium
  governance_and_spec_status: high
  gateway_and_security_patterns: medium-high
  adoption_metrics: medium-low        # mostly self-reported by project/vendors
  hiring_volume: low-medium           # keyword indexes only; no census exists in public sources
  enterprise_mandate_claim: low       # no public evidence found for "mandated for all internal SaaS"
---

# T0-16 — Agentic Protocol Stack: Standardization Status and Enterprise Hiring Demand (October 2026)

## Prior

*Written from memory before the searches in this session. Per the calibration rules these are Grade D hypotheses, not findings. Each is stated so that evidence can confirm, update, or contradict it.*

| # | Proposition (checkable) | How it was tested | What would falsify it |
|---|---|---|---|
| P1 | MCP is hosted by a Linux Foundation vehicle called the **Agentic AI Foundation (AAIF)** (not "Agentic AI Interoperability Framework"), launched Dec 2025 with MCP, goose, and AGENTS.md. A2A is a **separate** LF project. | Foundation press releases, AAIF project roster | A primary source using the brief's expansion; A2A listed as an AAIF project |
| P2 | The latest MCP specification revision is **2025-11-25** (async Tasks, Client ID Metadata Documents, extensions). | modelcontextprotocol.io spec/changelog/blog | Any later dated revision |
| P3 | IBM's **ACP** merged into A2A in 2025, so ACP is not an independent competing standard; "ACP" is an overloaded acronym. | LF AI & Data post; AAIF launch release | ACP shipping releases as a separate protocol in 2026 |
| P4 | **AG-UI** is CopilotKit-led, not foundation-hosted; adoption claims are largely vendor-reported; 1.0 status uncertain. | AG-UI repo, AAIF roster, funding coverage | AG-UI in a neutral foundation; independent adoption data |
| P5 | MCP appears in a **small but fast-growing** share of job postings; explicit protocol-level requirements (JSON-RPC, transport, tool-schema) are rarer than framework mentions (LangChain/LangGraph); "Agent Gateway Engineer" is not an established title; the claim that enterprises **mandate MCP servers for all internal SaaS** lacks public evidence. | Three job-index sources, sampled JDs, surveys | A census-grade source showing MCP as a majority requirement; postings with the literal title in volume; a traceable mandate source |

## Research Question

**Decision under test:** Has the agentic protocol stack (MCP under Linux Foundation / AAIF governance, A2A, ACP, AG-UI) matured into an industry-standard requirement that is driving *verified* engineering hiring volume in late 2026?

This is decomposed into four sub-questions:

- **RQ1 — Standardization.** What are the governance status, current specification version, and industry backing of MCP, A2A, ACP, and AG-UI?
- **RQ2 — Requirement.** Do enterprises actually *require* protocol-based integration, and what gateway/auth/rate-limit/audit patterns do they deploy? What are the security failure modes?
- **RQ3 — Hiring.** Is there verified hiring volume, and do job descriptions require protocol-level knowledge (JSON-RPC, SSE/WebSocket transport, tool-schema authoring) or mostly framework-level knowledge (LangGraph, CrewAI)?
- **RQ4 — Architecture.** How do protocol-native designs compare with proprietary-framework wrappers?

**Scope and method.** Temporal anchor: 21 Oct 2026. Evidence window ends at that date; the AGNTCon + MCPCon North America event (22–23 Oct 2026, San Jose, per the Linux Foundation event banner) is **not** reflected. In scope: open protocols, enterprise gateways, Python/TypeScript/Rust tool servers. Out of scope: closed single-vendor frameworks lacking open-protocol support (framework adapters that *consume* MCP, e.g. LangChain's, are in scope because they sit on the open protocol). Roughly 60 searches/fetches were run; primary sources (specs, foundation pages, government publications, vendors' own product documentation, repositories) were preferred over commentary.

**Terminology corrections to the brief** (each verified in §Detailed Findings):

1. **AAIF = Agentic AI Foundation**, not "Agentic AI Interoperability Framework." (One LF-authored report once writes "Agentic AI Infrastructure Foundation" — an apparent slip; the foundation's own pages use "Agentic AI Foundation".)
2. **"ACP" is three different things**: IBM's Agent Communication Protocol (merged into A2A, Aug 2025); OpenAI/Stripe's Agentic Commerce Protocol (named in the AAIF launch release); and an editor-integration "Agent Client Protocol" seen in search results (not verified). The brief's "ACP" most plausibly means IBM's, which no longer exists as a separate standard.
3. **A2A is no longer outside AAIF**: the A2A project announced on 27 Aug 2026 that it is joining AAIF as a Growth Stage project.
4. **"Cloudflare Workers MCP Gateway"** is not the product name; the verified products are *MCP server portals* (in Cloudflare Access/Zero Trust) plus remote MCP servers built on Workers.
5. **"mcp-cli"** names several unrelated projects; none was verified as canonical.
6. **"Agent Gateway Engineer"** is not an established job title in any posting or index found (see KF-10).

## Key Findings

**Evidence grades.** **A** = canonical primary source (spec text, foundation/government publication, a vendor's own docs for its own product, the repository/registry itself) read this session. **B** = reputable secondary, vendor/self-reported data with disclosed method, a primary source seen only as an excerpt, or ≥2 independent corroborations. **C** = single secondary source, vendor marketing, or a measurement with material methodological limits. **D** = recalled from model memory, not verified (hypothesis only). **X** = contradicted/untraceable, rejected. Source IDs (S01…) refer to the Ledger at the end.

### KF-1 — Governance: MCP is hosted by the Agentic AI Foundation, a Linux Foundation fund — **Grade A**
The Linux Foundation announced AAIF on 9 Dec 2025 as a vehicle for neutral stewardship, with Anthropic's MCP, Block's goose, and OpenAI's AGENTS.md as founding projects; AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI are named as top-tier members in the launch release [S01]. By Aug 2026 AAIF reported 247 member organizations [S02] and its roster lists six projects: MCP, goose, AGENTS.md, agentgateway, A2A, and Agent Router [S04]. **Caveat:** foundation hosting settles IP/trademark neutrality, not who steers the spec. MCP's own contributor ladder reserves the Lead Maintainer role for the project's founders, with veto power and authority to appoint core maintainers, while core maintainers hold final technical authority and vote on SEPs [S09]. Neutral home ≠ distributed technical control.

### KF-2 — Specification: the current MCP revision is **2026-07-28**, not 2025-11-25 — **Grade A**
Released 28 Jul 2026 [S05, S06]. Headline changes: a **stateless core** (no required session handshake), request-level routing headers (`Mcp-Method`, `Mcp-Name`), cacheable list results with explicit TTL/scope, multi-round-trip requests, authorization hardening (RFC 9207 issuer identification; Client ID Metadata Documents replacing dynamic client registration), a formal extension mechanism (MCP Apps, Enterprise-Managed Authorization, Tasks), OpenTelemetry trace-context conventions, and deprecations (Roots, Sampling, Logging; the legacy HTTP+SSE transport). SDKs are formally tiered with conformance requirements; Tier 1 = TypeScript, Python, Go, C#, with Rust in beta at launch [S05, S08]. The 22 Aug 2026 roadmap names five priorities: agentic messaging primitives, HTTP-native transport unification, agent identity and enterprise security (DPoP, workload identity federation), progressive discovery, and SDK developer experience [S07]. **My recalled prior (2025-11-25 latest) was stale.**

### KF-3 — A2A: v1.0 shipped, backed by 150+ organizations, and has moved under AAIF — **Grade A (spec/governance); B (adoption count)**
A2A v1.0 shipped 12 Mar 2026 [S12]; the Linux Foundation reported 150+ participating organizations on 9 Apr 2026 [S15]; the project announced on 27 Aug 2026 that it is joining AAIF as a Growth Stage project [S13]. The v1.0 spec defines an explicit task lifecycle (submitted, working, completed, failed, canceled, rejected, plus interrupted states *input-required* and *auth-required*), `contextId` grouping across tasks, streaming and push-notification delivery, and capability/modality/version negotiation [S14]. It defines **no bid/price/auction-style negotiation**; "negotiation" is limited to discovery (Agent Card), accepted output modes, protocol-version and binding selection, and interrupt/reject states. The spec also warns that messages are not a reliable-delivery mechanism, so clients must be able to re-fetch task state [S14].

### KF-4 — ACP has been absorbed; AG-UI reached 1.0 but is single-steward — **Grade A (status); B (adoption claims)**
IBM's Agent Communication Protocol merged into A2A on 29 Aug 2025 [S16]. AG-UI declared 1.0 on 18 Sep 2026 [S17], is stewarded by CopilotKit's `ag-ui-protocol` GitHub organization, and is **not** in AAIF's project roster [S04]. CopilotKit's adoption claims (Google, Microsoft, Amazon, Oracle, LangChain, Mastra, Pydantic AI, Agno, AG2, LlamaIndex; "4M+ weekly downloads") are company-reported via its funding announcements [S18]; I could not independently verify how deep each vendor integration is.

### KF-5 — Adoption scale is large but almost entirely self-reported; the "78% in production" statistic is untraceable — **Grade B (scale) / X (78%)**
MCP maintainers report close to half a billion monthly downloads across Tier 1 SDKs and 1B+ cumulative downloads each for the TypeScript and Python SDKs [S05]; the reference-servers repo shows ~90k stars [S10]; AAIF's Momentum Report tracks 116 projects across five layers [S03]. These are project- or foundation-authored. The best-documented *independent-of-project* enterprise data point is the Stacklok survey (fielded Dec 2025; 100 senior technical leaders per sector across three sectors; vendor-run): nearly half of software-company respondents report MCP in some production use, 19% in broad production, and security is the top adoption obstacle (64%) [S45]. The widely repeated "78% of enterprise AI teams have MCP in production" figure has no traceable primary source; several analysts explicitly flag it as unsourced [S48]. I reject it.

### KF-6 — Production gateways have converged on one architecture (control plane + stateless data plane) — **Grade A per vendor; B for the synthesis**
Uber (1 Oct 2026) runs 800+ MCP servers exposing 5,000+ tools through a registry-driven control plane and a proxy data plane, with servers disabled by default, config-diff approval, tool-level authorization, PII redaction on responses, and token exchange for third-party servers [S27]. AWS AgentCore Gateway aggregates targets into one virtual MCP server with inbound JWT/IAM auth, request/response interceptors, and Cedar-based Policy (GA Mar 2026) [S28, S29]. Cloudflare MCP server portals sit in Access, route through Gateway for logging/DLP, and enable Code Mode by default [S30]. Microsoft's APIM/Foundry AI gateway (preview) federates MCP servers [S31]. Databricks exposes managed MCP servers that enforce Unity Catalog permissions with on-behalf-of-user auth [S32]. The AAIF-hosted agentgateway (Rust) provides RBAC (CEL), rate limiting, and budget controls [S33]. The common functional set — registry/allowlist, per-tool authN/Z, policy, response filtering, discovery scaling, audit — is my synthesis of these sources (§6).

### KF-7 — The spec is moving toward enterprise-grade auth; observed practice lags — **Grade A (spec) / B (practice)**
The standard now includes an OAuth resource-server model, Client ID Metadata Documents, an Enterprise-Managed Authorization extension described as stable on the roadmap, and planned DPoP and workload-identity work [S05–S07]. In practice, a 2025 Astrix scan of ~5,200 open-source MCP server implementations found 53% relying on static secrets and 8.5% using OAuth [S44] (sample skews to local/OSS servers; predates the 2026 changes). NSA's May 2026 guidance states that MCP-aware security proxies are still maturing and recommends controls — message signing, DLP on outputs, full tool-call logging — that are not part of the base protocol [S34].

### KF-8 — The vulnerability record is real, recurring, and partly disputed at the design level — **Grade A/B**
Documented 2026 classes: SSRF through OAuth discovery/registration (CVE-2026-45609, Spring AI community MCP security library) [S38]; unauthenticated RCE and SSRF in the popular mcp-atlassian server (CVE-2026-27825, CVE-2026-27826) [S37]; SSRF in a reference fetch server (CVE-2026-104120) [S39]; path traversal triggered via indirect prompt injection (CVE-2026-44192, Red Hat) [S40]. OX Security (Apr 2026) argues STDIO config-to-command execution is a systemic design flaw; Anthropic is reported to treat it as expected behavior — an unresolved dispute with a vendor-research conflict of interest [S41]. AAIF's own report finds unpatched CVEs across the projects it tracks grew ~2.6× between Dec 2025 and Jun 2026, while foundation-hosted protocol repos had the lowest per-repo average [S03]. For A2A, Unit 42 demonstrated *agent session smuggling* as an abuse of stateful trust, explicitly not a protocol flaw [S42].

### KF-9 — Hiring: three independent indexes agree on "small but fast-growing," none supports "mandated everywhere" — **Grade C**
(1) Fortune-1000 + API-provider postings, Q3 2026: 234 of 343,299 postings name "Model Context Protocol" (0.068%); 102 of 984 companies (10.4%) have at least one [S19]. (2) Skillenai broad index: 1,747 postings in the 90 days to 14 Oct 2026, ~0.7% adjusted share of all postings [S20]. (3) landed.jobs (AI-native-skewed): MCP rose from 1.2% of engineering postings in Jan 2026 to somewhere between 2.7% and 4% by mid-2026 (the report is internally inconsistent) [S23]. Universes, phrase rules, and denominators differ; the numbers cannot be averaged. All three show rapid growth from a small base; none shows ubiquity.

### KF-10 — No "Agent Gateway Engineer" title exists in volume; protocol-level skills are unmeasured; framework skills still dominate agent-titled roles — **Grade C**
I found no posting with that literal title. Equivalent work appears as "Senior Platform Engineer – Enterprise AI" (Boston Scientific) [S24], "Senior Enterprise AI Control Plane Engineer" (PTC; API-management background) [S25], and product roles such as Workato's Enterprise MCP/AI Control Plane PM [S26]. In the Skillenai index, "Agent Engineer" titles number only 28 in 90 days with LangChain (42.9%) and LangGraph (39.3%) leading and MCP outside the top 15 [S22]; for "Agentic AI Engineer," LangGraph appears in 35.8% vs MCP 13.8% [S20, S21]. **No dataset found measures JSON-RPC, SSE/WebSocket transport, or tool-schema authoring as separate requirements**; the only observable proxy is the keyword "MCP."

### KF-11 — Protocol-native vs framework-wrapper is a false dichotomy; the real choice is where governance and discovery live — **Grade B/C**
Frameworks wrap the open protocol (e.g., `langchain-mcp-adapters`; LangChain docs) [S51], so MCP-in-a-framework is the norm, not the alternative. The architectural questions are (a) in-process tool definitions vs protocol-aware gateway enforcement, and (b) how much tool schema the model sees. Anthropic's own engineering post illustrates a task dropping from ~150,000 to ~2,000 tokens when tools are presented as code APIs rather than loaded schemas (an illustrative example, not a benchmark) [S46]; Cloudflare enables Code Mode by default [S30]; Uber built a meta-tool layer and uses code-mode CLI as its default for coding agents [S27]; the MCP maintainers themselves list progressive discovery as a roadmap priority [S07].

### KF-12 — Credible falsifiers exist: context cost, auth friction, gateway bypass, spec churn — **Grade B/C**
A widely reported (second-hand, no transcript found) March 2026 remark attributed to Perplexity's CTO says the company was moving away from MCP internally for context-cost and auth reasons [S47]. The official reference servers are labeled not production-ready and many are archived [S10]. A Microsoft open-source ADR documents that server-side MCP invocation by some Foundry agent types can bypass a customer-operated gateway [S31]. The 2026-07-28 revision deprecates several features, and SDK v2 migrations produced ecosystem breakage reports and observability gaps [S50]. Net reading: MCP is **becoming governed infrastructure**, not a frictionless "HTTP of AI."

## Recommendation

### Verdict on the decision (three separable claims)

| Claim embedded in the decision | Verdict | Grade | Basis |
|---|---|---|---|
| The open protocol stack has matured into an **industry standard** | **Yes for MCP. Yes-with-caveats for A2A. Not yet for AG-UI. IBM's ACP no longer exists separately.** | A | MCP and A2A are both hosted by a neutral foundation; versioned spec (2026-07-28) with SDK tiers and conformance; multi-vendor participation; national-security guidance written specifically about MCP. Caveats: founder veto in MCP's technical governance; AG-UI single-steward; features still being deprecated. |
| It is an enterprise **requirement** | **Partly.** A de facto requirement for platform teams and tool vendors; **not shown** to be a universal mandate. | B/C | Uber-scale gateways and control-plane job postings exist; the only public survey shows security as the top blocker; no source evidences "mandated for all internal SaaS"; the 78% statistic is untraceable. |
| It is **driving verified hiring volume** | **Not verified at scale.** Measurable and rising fast, but small. | C | 0.07%–0.7% of postings depending on universe (up to ~3–4% of engineering postings in an AI-native-skewed index); no gateway-engineer title in volume; protocol-level skills unmeasured. |

**Suggested wording for planning documents:** *"MCP (and increasingly A2A) is the de facto open standard for agent–tool interoperability and is now under neutral foundation governance. Protocol and gateway literacy is a fast-growing but still minority hiring signal, concentrated in platform, API-management, identity, and security-adjacent roles."*

### Actions

1. **Standardize on MCP at the tool boundary and target the 2026-07-28 revision.** Pin SDK major versions (SDK v2 migrations broke downstream packages); plan to retire HTTP+SSE and any reliance on Sampling/Roots/Logging.
2. **Put a gateway in front of every non-local MCP server before scaling past a handful.** Adopt before building (cloud-native: AgentCore Gateway, Cloudflare portals, Azure APIM AI gateway [preview]; open source: agentgateway) unless regulatory or scale needs resemble Uber's. Minimum feature set: default-deny registry; per-tool authorization; identity propagation or token exchange; response DLP/projection; per-identity quotas; tool-definition drift detection; OTel/SIEM audit export. *(Build-vs-buy thresholds are my judgment; no source quantifies them.)*
3. **Adopt the control catalog in Detailed Findings §8** (SSRF-hardened discovery fetches, STDIO sandboxing, untrusted-output handling, no token passthrough, signed/pinned tool definitions).
4. **Hiring:** do not open a standalone "Agent Gateway Engineer" requisition on the strength of public demand data. Fold gateway work into platform / API-management / IAM / security roles (the pattern in the postings found) and specify what "MCP experience" means in the JD — *server authoring*, *gateway operation*, or *client integration* — because the keyword alone conflates them. Keep framework-and-evaluation skills as the primary filter for application-side agent engineers, where LangChain/LangGraph still dominate the listings.
5. **Measure, don't assert:** re-run the three-index measurement quarterly on a fixed universe with phrase variants ("MCP", "Model Context Protocol", "MCP server", "A2A"). Obtain a Lightcast/Indeed/LinkedIn pull if hiring volume is decision-critical.

### What would change the verdict *(heuristics — my judgment, not sourced thresholds)*
- **Toward "yes, verified demand":** Fortune-1000 posting share sustained above ~1% for two consecutive quarters (≈15× the Q3 2026 level); a census-grade source (Lightcast, Indeed Hiring Lab, LinkedIn Economic Graph) reporting MCP above ~2% of all tech postings; the literal gateway-engineer title appearing in dozens of postings; MCP Registry reaching GA with enterprise sub-registry adoption.
- **Toward "overstated":** share flat or falling for two quarters; a major MCP-attributed breach at a large enterprise; hyperscalers deprecating MCP gateways in favor of CLI/skills-first patterns; AAIF membership shrinking or A2A/MCP governance fracturing.

## Alternatives Considered

| # | Alternative framing or path | Evidence for | Evidence against | Verdict |
|---|---|---|---|---|
| A1 | **"MCP is the HTTP of generative-AI tooling"** (the brief's UNVERIFIED claim) | Neutral foundation; multi-vendor adoption; Tier 1 SDKs; stateless core arrived in 2026-07-28 | HTTP is a transport; MCP also carries tool contracts, auth, and discovery, and still has unsolved context-cost and security problems; reference servers not production-ready; spec still deprecating features | **Partly supported; rejected as stated.** Better analogy: an emerging *API-management-class* layer needing a gateway. |
| A2 | **"Enterprises mandate MCP servers for all internal SaaS"** | Uber's 800+ servers; hyperscaler gateways; control-plane job postings | No source evidences a mandate pattern; Stacklok shows security as top blocker; only ~8–11% of sampled companies (8.1% of API providers, 11.0% of the Fortune 1000) name MCP in any posting | **Not supported by public evidence.** |
| A3 | **Wait for MCP to stabilize** | Deprecations continue; SDK v2 churn | Stable dated revision with Tier 1 conformance; hyperscaler and government attention | **Rejected.** Adopt now, pin versions. |
| A4 | **Skills/CLI-first, MCP optional** | Context cost; Perplexity remark (second-hand); Uber's code-mode default | CLI/skills lack central governance, identity propagation, and audit; Uber and Cloudflare still run MCP gateways *under* code mode | **Hybrid:** MCP at the governed boundary, code-mode/CLI inside the agent. |
| A5 | **Framework-native tools only (no protocol)** | Simpler for one app, one framework | No portability; no central policy point; per-framework security posture; wrappers already speak MCP | **Acceptable for single-app prototypes; rejected for multi-team enterprise.** |
| A6 | **Build a custom gateway (Uber-style)** vs **adopt open source / cloud gateway** vs **vendor MCP gateway** | Uber's depth of integration with internal IAM/mesh | Uber's scale (800+ servers) is atypical; open-source (agentgateway, Agent Router) and cloud gateways now exist; two more AAIF-hosted gateway projects | **Adopt first; build only on demonstrated gaps.** |
| A7 | **Dedicated "Agent Gateway Engineer" role** vs **fold into platform/API/security roles** | Control-plane postings exist (PTC, Boston Scientific) | Title not found in volume; the postings found are API-management/platform hybrids | **Fold in** unless server count and compliance load justify a dedicated team. |
| A8 | **A2A-first** vs **MCP-first** | A2A v1.0; now under AAIF | No bid/negotiation semantics; reliability caveats; far thinner hiring signal | **MCP first for tools; adopt A2A only when crossing team/vendor boundaries with opaque agents.** |

## Detailed Findings

### 1. Protocol stack map (RQ1)

| Layer | Protocol | Steward / home | Version and status (Oct 2026) | In AAIF roster? | Grade |
|---|---|---|---|---|---|
| Agent ↔ tools/context | **MCP** | AAIF (Linux Foundation); project maintainer ladder | **2026-07-28** (dated, stable); prior baseline 2025-11-25 | Yes (founding project, Dec 2025) | A [S01, S05, S06] |
| Agent ↔ agent | **A2A** | LF project, then AAIF Growth Stage (announced 27 Aug 2026) | **v1.0** (12 Mar 2026) | Yes, per project announcement | A [S12–S14] |
| Agent ↔ user interface | **AG-UI** | CopilotKit-stewarded `ag-ui-protocol` GitHub org | **1.0** (18 Sep 2026) | **No** | A (status) / B (adoption) [S17, S18] |
| Agent communication (IBM) | **ACP** | Merged into A2A under LF AI & Data (29 Aug 2025) | n/a — absorbed | n/a | A [S16] |
| Agentic commerce | ACP (OpenAI/Stripe) | Named in the AAIF launch release | Not researched | Not on roster | A (existence only) [S01] |
| Gateways | **agentgateway**, **Agent Router** (Envoy-based) | AAIF-hosted projects | agentgateway announced joining AAIF 4 Jun 2026 | Yes | A (roster) / B (details) [S04, S33] |
| Instruction files | AGENTS.md | AAIF | Not researched | Yes | A [S01, S04] |
| Agent-generated UI | MCP Apps (MCP extension) · A2UI (Google) · AG-UI | Three approaches, per CopilotKit's own framing | — | MCP Apps lives inside MCP | B [S05, S18] |

### 2. MCP specification evolution and the 2026-07-28 revision (RQ1)

**Timeline.** Anthropic's engineering post confirms the Nov 2024 launch [S46]. Earlier-revision details below come from a secondary release-notes summary and are graded accordingly; they are consistent with, but not independently confirmed against, the spec archive in this session.

| Revision | Content (as sourced) | Grade |
|---|---|---|
| 2024-11-05 | Initial era; HTTP+SSE remote transport | B [S52 release notes] |
| 2025-03-26 | Streamable HTTP replaces HTTP+SSE (LangChain docs still link this transport spec) | B [S52, S51] |
| 2025-06-18 | Structured tool outputs; JSON-RPC batching removed; servers classified as OAuth resource servers; elicitation | B [S52] |
| 2025-11-25 | Baseline against which NSA's CSI and the 07-28 changelog are written. Feature list (Tasks, Client ID Metadata Documents, extensions, etc.) is **recalled, Grade D**, apart from items the 07-28 documents themselves reference | B (existence) / D (feature list) [S34, S06] |
| **2026-07-28** | See table below | **A** [S05, S06] |

**What 2026-07-28 changed, and what it means operationally.** The right-hand column is **my analysis**, not source text.

| Change (per blog/changelog) | Operational implication (analysis) |
|---|---|
| **Stateless core** — protocol no longer depends on server-held session state | Plain L7 load balancing without sticky sessions; serverless and horizontally scaled servers become straightforward; the "gateway as session-affinity problem" largely disappears |
| **Routing headers** `Mcp-Method`, `Mcp-Name`, plus custom `x-mcp-header` | Gateways/WAFs can route, authorize, and rate-limit by method and tool name without parsing JSON bodies. *Caveat:* ecosystem tooling is not uniformly reading these yet (see ecosystem lag, below) |
| **Cacheable list results** (`ttlMs`, `cacheScope`) | `tools/list` can be cached with explicit TTL. Gateways must honor `cacheScope` so per-user tool visibility is never served from a shared cache |
| **Multi-round-trip requests** (MRTR) | Server-initiated asks (e.g., user input) become explicit round trips, which fits stateless servers and human-approval flows without server→client push |
| **Authorization hardening** — RFC 9207 issuer (`iss`) identification; Client ID Metadata Documents replace dynamic client registration | Mix-up-attack mitigation. CIMD mechanics are recalled (D); note that any design in which an authorization server fetches a client-supplied metadata URL needs the same SSRF hardening as client-side discovery (see CVE-2026-45609 in §8) |
| **Formal extensions**: MCP Apps, Enterprise-Managed Authorization (EMA), Tasks | Enterprise IdP-governed access (EMA) and long-running work (Tasks) move out of core; capability negotiation by extension |
| **OpenTelemetry trace-context conventions** (SEP-414) | End-to-end tracing agent → gateway → server becomes standardized rather than bespoke |
| **Deprecations/removals**: Roots, Sampling, Logging deprecated; legacy HTTP+SSE deprecated; SSE stream resumability removed; formal feature-lifecycle policy; error-code allocation | Migration backlog for servers that use Sampling or SSE; evidence that the spec is still shedding features |
| **SDK tiers**: Tier 1 TypeScript, Python, Go, C#; Rust beta at launch | Conformance-gated SDK choice (Tier 1: 100% conformance suite pass, 2-business-day issue triage, 7-day critical-bug resolution; Tier 2: 80%) [S08] |

**Roadmap (22 Aug 2026)** [S07]: (1) agentic messaging primitives, (2) HTTP-native transport unification (including local servers speaking Streamable HTTP), (3) agent identity and enterprise security (DPoP, workload-identity federation, IETF OAuth/WIMSE alignment), (4) improved primitives with **progressive discovery** (the maintainers explicitly acknowledge that large tool lists degrade model tool selection and cost context), (5) SDK developer experience; plus a Server Card working group for `.well-known` server metadata. EMA is described there as stable.

**Ecosystem lag (the spec is stable; the toolchain is mid-migration)** — Grade B [S50, S51]:
- Python SDK v2 and community FastMCP 4.x track the new spec; the older standalone FastMCP 3.x line pinned the older SDK. A downstream package (jupyter-mcp-server) filed an import-breakage issue after the SDK v2 change.
- TypeScript SDK v2 splits packages (`@modelcontextprotocol/core|server|client`) and removes server-side SSE (client-side SSE remains for legacy servers).
- PostHog's MCP analytics docs describe SDK v2 as breaking session-ID–based analytics and note that header-based method/tool visibility is not yet read by all tooling.
- A FastMCP discussion on the RC notes session-backed context state does not round-trip across stateless requests.
- LangChain's MCP docs still link the 2025-03-26 transport spec.
- Rust SDK: the launch post said "beta"; the repository README later describes support for the stable revision (discrepancy noted; likely progressed since launch).

### 3. Governance detail (RQ1)

**AAIF (foundation layer)** [S01, S02, S04]: a directed fund under the Linux Foundation, launched 9 Dec 2025. Membership grew in waves (97 new members announced Feb 2026, 43 in May, 57 in Aug) to **247** organizations by Aug 2026. Leadership named on AAIF pages: Executive Director Mazin Gilbert; Governing Board chair David Nalley. Hosted projects: MCP, goose, AGENTS.md, agentgateway, A2A, Agent Router. Membership is not deployment — it is a signal of vendor alignment, not usage.

**MCP project governance (technical layer)** [S09]:
- *Lead Maintainers*: reserved for founders; veto authority; appoint/remove core maintainers; succession-only.
- *Core Maintainers*: final decision authority on technical direction; vote on SEPs (spec enhancement proposals).
- *Working Groups / Interest Groups*: make binding decisions within scope; chartered with sponsorship from at least two core maintainers or one lead maintainer. A Server Card working group is active [S07].
- **Interpretation (analysis):** the foundation neutralizes the IP and trademark question; it does not by itself distribute technical authority. Multi-company participation is nonetheless visible: the 07-28 announcement carries supportive statements from Google Cloud, Microsoft, AWS, Cloudflare, and OpenAI personnel, one identified as an MCP core maintainer [S05]. I did not independently verify each maintainer's employer.

**Comparative contributor health (LF-authored, so potentially favorable to its own model)** [S03]: AAIF's Momentum Report reports a lower per-repo CVE average in its Foundations & Protocols layer than other layers, a 53% contributor-health figure for that layer, and issue resolution in just under five weeks; it also flags single-organization-dominated, non-compliant projects (naming the OpenAI Agents SDK and LiteLLM among the highest-risk combinations). Treat the comparison as directional.

### 4. A2A, ACP, and AG-UI (RQ1)

**A2A v1.0 task model** [S14] — Grade A:

| State | Class | Meaning for handoff |
|---|---|---|
| SUBMITTED, WORKING | active | Accepted/in progress; clients can stream or poll |
| INPUT_REQUIRED | **interrupted** | Remote agent needs more input before continuing — the main "negotiation-like" turn |
| AUTH_REQUIRED | **interrupted** | Credentials/authorization needed mid-task |
| COMPLETED, FAILED, CANCELED, REJECTED | **terminal** | REJECTED = the agent declined the task |

- Operations include SendMessage, SendStreamingMessage, GetTask, ListTasks, CancelTask, SubscribeToTask, push-notification config management, and an authenticated extended Agent Card fetch.
- `contextId` ties multiple tasks into one conversation/workflow; task IDs are server-generated.
- **Opaque execution:** agents collaborate without exposing internal memory or tools. State handoff therefore means *task + artifacts + context ID*, not shared memory.
- **What "negotiation" actually covers:** discovery via the Agent Card (skills, supported interfaces, security schemes); accepted output modes (modality negotiation); protocol version and binding selection (an `A2A-Version` header; an empty header is treated as 0.3 — a silent-downgrade gotcha); and the interrupt/reject states above. **Not covered:** price/SLA bidding, multi-party consensus, transactional (exactly-once) handoff. Commerce-style negotiation lives in adjacent protocols (e.g., OpenAI/Stripe's Agentic Commerce Protocol), which I did not research.
- **Reliability caveats from the spec itself:** messages are not a reliable-delivery mechanism; send idempotency is permitted, not required; clients that reconnect must re-fetch task state.
- **Signed Agent Cards** are specified (v1.0 headline feature [S12]); whether verification is mandatory for clients is **not established** — one security-vendor analysis (grith.ai) claims it is optional [Grade C, S56; single vendor source]. Open question O-6.
- **Security evidence:** Unit 42's *agent session smuggling* PoC (built on Google ADK) shows that stateful multi-turn A2A sessions let a malicious remote agent inject instructions after trust is established; Unit 42 states this is not a protocol vulnerability, and press coverage reports no in-the-wild exploitation [S42, S43]. Defensive implications are in §8.
- **Gateway support:** AgentCore Gateway supports HTTP-type targets that proxy to agents; agentgateway federates both MCP and A2A [S28, S33]. (A job posting from a gateway vendor that mentions governing both protocols was seen in search results but its URL was not retained, so it is excluded from the evidence.)

**ACP** [S16]: IBM's ACP joined A2A on 29 Aug 2025; the brief's "emerging" ACP is therefore history, not a competitor. Keep the acronym disambiguated in all documents.

**AG-UI** [S17, S18]:
- 1.0 declared 18 Sep 2026; the repo showed ~16k stars and ~1.4k forks at retrieval (a direct count; popularity ≠ standardization).
- Stewarded by a startup (CopilotKit raised $27M in May 2026 — figures reported as $20M Series A + $7M seed by GeekWire/TechCrunch; Calcalist reports $20.5M + $6.5M); not in AAIF.
- Role: the agent-to-frontend event channel (streaming chat, frontend tool calls, shared state, human-in-the-loop UI), complementary to MCP (tools) and A2A (peers) per CopilotKit and its investor's framing. The transport and event-type details (SSE/HTTP, event taxonomy) are **recalled, Grade D**, not verified this session.
- CopilotKit itself frames agent-generated UI as three approaches: AG-UI (controlled), Google's A2UI (declarative), and MCP Apps (open-ended) [S18] — evidence that UI-layer standardization is **not** settled.

### 5. Adoption metrics audit (RQ1/RQ2)

| Metric | Value | Provenance | Grade | Note |
|---|---|---|---|---|
| Tier 1 SDK downloads | "close to half a billion" per month | MCP maintainers (07-28 post) | B | Self-reported; package-registry download counts include CI and mirrors |
| TypeScript and Python SDK cumulative downloads | each 1B+ | MCP maintainers | B | Same caveat |
| Earlier datapoint (Dec 2025) | ~97M monthly SDK downloads; 10,000+ servers | Recalled from launch coverage | **D** | Not re-verified; the LF page should be re-checked before citing |
| Reference-servers repo | ~90.0k stars, ~11.5k forks; README says reference servers are not production-ready; popular servers (GitHub, Slack, Google Drive, Postgres, etc.) listed as archived | GitHub (direct) | A | Stars measure attention, not deployment |
| AAIF membership | 247 orgs (Aug 2026) | AAIF | A | Membership ≠ usage |
| AAIF-tracked projects | 116 across five layers | AAIF Momentum Report | A/B | LF-authored |
| A2A participating orgs | 150+ (Apr 2026) | LF press release | A (as LF claim) | Counts supporters, not deployments |
| AG-UI downloads | "4M+ weekly" | CopilotKit | C | Company claim |
| MCP Registry size | Not obtainable | Live API returns *per-version* rows with an `isLatest` flag and no total count [S11]; one secondary source claims 9,652 listings (Apr 2026) [S48] | C | Counts of rows conflate versions; docs still carry a pre-GA caveat; **no evidence of GA found** |
| Enterprise "in production" share | "Nearly half" of surveyed software firms in some production use; 19% broad (Stacklok, n=100 software leaders; fielded Dec 2025) | Vendor survey | B/C | Vendor sells MCP governance; small n; US/UK large enterprises |
| "78% of enterprise AI teams in production" | — | Repeated by several blogs; analysts say unsourced | **X** | Rejected; DigitalApplied's own page carries a contradictory body |
| Gartner forecast (75% of API-gateway vendors with MCP features by 2026) | — | Via a vendor blog (K2View) [S49] | C | Analyst forecast, not an adoption measurement; original not read |
| Claim of 86% experimentation / 5% governed enterprise-wide ("July 2026 Stacklok/AAIF survey") | — | One secondary article | D | Could not find the primary; conflicts with the Dec 2025 fielding date of the report located |

### 6. Production gateway architecture — dissection (RQ2)

**6.1 Reference architecture (synthesis of the sources below; not any single vendor's diagram).**

```
  Agents / hosts (IDE, chat, autonomous agents)       identities: human | service | agent
        │   MCP over Streamable HTTP (2026-07-28 headers)   /   A2A (HTTP+JSON, gRPC, JSON-RPC)
        ▼
 ┌──────────────────────── DATA PLANE (stateless, horizontally scaled) ────────────────────────┐
 │ 1 Authenticate (OAuth/JWT; IdP federation)     2 Authorize (server → tool → argument level)    │
 │ 3 Rate-limit / quota / budget (identity × tool) 4 Aggregate + route (one virtual MCP server)    │
 │ 5 Discover (filtered tools/list; progressive discovery or code mode)  6 Cache (ttlMs/scope)    │
 │ 7 Transform (protocol translation; response projection; PII/DLP redaction)                     │
 │ 8 Broker credentials (token exchange / OBO / 3-legged consent)  9 Audit + trace (OTel)         │
 └──────────────────────────────────────────────────────────────────────────────────────────────┘
        ▲ policy, allowlist, config, analytics                │ upstream targets
 ┌───────────── CONTROL PLANE ─────────────┐          internal MCP servers · third-party MCP servers
 │ Registry / catalog (approved servers)    │          OpenAPI / Lambda / gRPC services (translated)
 │ Crawler + tool-definition drift detection│          A2A agents (HTTP-type targets)
 │ Approval workflow (config diff, HITL)    │
 │ Policy authoring (Cedar / CEL / RBAC)    │
 │ Inventory + shadow-MCP discovery         │
 └──────────────────────────────────────────┘
```

**6.2 How five production/vendor implementations map onto it.** "Not verified" means I did not find or did not capture the detail; it does not mean the feature is absent.

| Implementation | Registry / inventory | AuthN / AuthZ | Response handling | Discovery scaling | Audit / observability | Grade |
|---|---|---|---|---|---|---|
| **Uber** (self-reported, 1 Oct 2026) [S27] | MCP Registry plus a crawler that syncs tool definitions; servers **disabled by default**; changes surfaced as config diffs needing approval | Token relay; token exchange for third-party servers; tool-level authorization via the internal access-control system using policies for callers (humans, services, agents) | PII redaction on tool responses; "response projection" to trim fields | Meta-tool layer (discover server → discover tools → get schema → invoke); code-mode CLI is the default for coding agents | Not captured | A (own account) |
| **AWS AgentCore Gateway** [S28, S29] | Targets (APIs, Lambda, MCP servers, tool definitions) aggregated into one virtual MCP server; HTTP targets proxy to agents | Inbound: OAuth/JWT, IAM SigV4, authenticate-only, or none (dev). Outbound authorization per target. **Cedar-based Policy GA 3 Mar 2026**, evaluated at the gateway outside agent code | Request/response Lambda interceptors (one of each per gateway per the infrastructure schema) | Semantic tool search is configurable in the MCP protocol settings | CloudWatch/CloudTrail/X-Ray integration documented for gateway targets | A |
| **Cloudflare MCP server portals** [S30] | Portal in Access; servers re-synced every 24 h; Access policies show/hide servers and gate portals | Access as OAuth provider or third-party OAuth; managed OAuth for non-browser clients | Optional routing through Cloudflare Gateway for HTTP logging and DLP | **Code Mode on by default** (single `code` tool instead of every upstream tool; changelog 26 Mar 2026) | Per-tool request logging in Access; Logpush integration; Gateway rules for **shadow-MCP detection** | A |
| **Microsoft** (API Management AI gateway, Foundry; **preview**) [S31] | Federates remote MCP servers; can expose OpenAPI as MCP; built-in connectors | Entra ID; APIM policy | Content-safety and token/request rate limits | Not verified | Audit logging | A (docs) / B (ADR) |
| **Databricks managed MCP** [S32] | Managed servers (Genie, vector/AI search, SQL, Unity Catalog functions); custom servers on Databricks Apps | **On-behalf-of-user** auth; Unity Catalog permissions enforced | Not verified | Not verified | Gateway-level monitoring (secondary mention) | A |
| **agentgateway** (AAIF-hosted) [S33] | Federates MCP and A2A | RBAC with a CEL policy engine | Prompt guards | Not verified | Observability (details not verified) | B (project-authored) |

**6.3 Patterns that scale agent protocols (analysis, with evidence for each).**

1. **Aggregation into a virtual server.** AgentCore documents MCP-target aggregation into one consolidated `tools/list`; Cloudflare portals and Uber's proxy do the same. Benefit: one endpoint, one policy point. Cost: the aggregated tool list grows with every server.
2. **Progressive discovery / semantic routing / code mode.** Every large-scale implementation found has *some* answer to tool-list bloat: AgentCore's semantic search, Uber's four-step meta-tools, Cloudflare's single `code` tool, and the maintainers' roadmap item on progressive discovery. Anthropic's illustrative example (~150,000 → ~2,000 tokens) motivates this [S46]. Evidence that this is *required* at scale rather than optional rests mainly on Uber's experience (5,000+ tools) and the maintainers' own roadmap acknowledgement; no controlled benchmark was found.
3. **Caching.** The spec now defines list-result TTL and scope (§2). Separately, crawl-and-diff of upstream tool definitions (Uber) is the operational mirror: it detects definition drift ("rug pull") rather than caching responses. Vendor guides also advocate human approval on drift [S53, vendor claim, Grade C].
4. **Rate limiting, quotas, budgets.** Presence verified for agentgateway (rate limiting and budget controls), Microsoft's gateway (token and request limits), and as an explicit requirement in the PTC posting. **Honest gap: I found no verified numeric defaults, quotas, or throughput benchmarks for any platform**; do not quote rate-limit numbers from this session.
5. **Credential brokering.** Token exchange (Uber), outbound authorization per target (AgentCore), on-behalf-of-user (Databricks), and IdP-managed grants (EMA) all exist to prevent a shared bot identity from taking over the last hop. A vendor guide frames this as the key selection criterion [S53, Grade C].
6. **Audit and tracing.** OTel trace-context conventions are now in the spec; NSA recommends logging every tool/model invocation with identities and parameters (§8).
7. **Bypass and shadow controls.** A gateway only governs traffic that passes through it. Microsoft's ADR documents server-side invocation paths that can bypass a customer gateway; Cloudflare publishes shadow-MCP detection rules; NSA recommends scanning for unauthorized MCP servers.
8. **STDIO → remote.** Vendor guides describe gateways that wrap fleets of STDIO servers behind authenticated HTTP [S53, Grade C]; the 2026 roadmap's transport-unification priority points the same direction [S07].

**6.4 What Uber's design teaches (analysis).** Two choices stand out. First, **translation rather than rewrite**: a proxy that converts MCP into the company's internal protocols let existing services appear as MCP servers, which is plausibly why the count reached 800+. Second, **governance by default-deny plus diff approval** rather than after-the-fact review. Uber's later move to meta-tools and a code-mode default shows that raw MCP tool lists did not survive contact with 5,000 tools — a finding that cuts against the "MCP is just plug-and-play" narrative while still keeping MCP as the governed boundary.

### 7. Enterprise authentication, authorization, audit, and approvals (RQ2)

**Identity modes a gateway must support (synthesis from §6 sources):**

| Mode | Used when | Mechanism seen in sources |
|---|---|---|
| User-delegated | Agent acts as the human | On-behalf-of (Databricks); token exchange (Uber); OAuth pass-through with audience checks |
| Service/system identity | Background or system tools | IAM SigV4 / service principals / service tokens (AgentCore, Cloudflare) |
| Third-party SaaS consent | Vendor-hosted servers | Outbound OAuth per target; token relay |
| IdP-governed ("zero-touch") | Enterprise-managed access to many servers | **Enterprise-Managed Authorization** extension (stable per roadmap). Mechanism details (identity-assertion grant flow) are **recalled, Grade D**; the EMA blog was located but its body was not captured this session |

**Authorization granularity.** Server-level allow/deny is the floor; tool-level is what Uber and AgentCore Policy provide; argument-level is possible with Cedar/CEL but I found no verified production reporting of it.

**Audit.** NSA recommends logging all tool and model invocations with exact parameters, identities, and hashes, forwarded to a SIEM [S34]. Cloudflare logs per-tool requests [S30]. A reasonable minimum record (synthesis): timestamp; trace ID; principal and delegating principal; server and tool; argument hash plus redacted arguments; policy decision and rule ID; DLP actions; response size/hash; latency; outcome.

**Human-in-the-loop approvals.** Mechanisms that exist: protocol-level elicitation (introduced in 2025-06-18 per a secondary summary), multi-round-trip requests in 2026-07-28, gateway-level approval of server enablement and definition changes (Uber), and approval flows named in a platform-engineer posting (Boston Scientific). **Honest gap:** I found no published data on approval rates, latency, or UX outcomes at enterprise scale.

### 8. Security: vulnerabilities, structural issues, and defensive patterns (RQ2)

**8.1 Government and standards guidance.**
- **NSA AISC, "Model Context Protocol (MCP): Security Design Considerations for AI-Driven Automation"** (U/OO/6030316-26; 17 pp; announced 20 May 2026) [S34]. Written against the 2025-11-25 revision. Recommends: choose actively supported projects (noting many popular reference servers are archived); design trust boundaries and data-classification zones; filter outbound traffic with proxies/DLP; validate parameters; sandbox servers; sign and verify MCP messages with time-bound, replay-resistant signatures; treat tool outputs as untrusted and filter them; log every invocation; patch and track; scan for unauthorized servers. States that MCP-aware security proxies are still maturing.
- **Five Eyes "Careful Adoption of Agentic AI Services"** (30 Apr or 1 May 2026; secondary sources differ by a day): five risk categories (privilege compromise, design/configuration flaws, behavioral misalignment, cascading structural failures, supply-chain weaknesses); prompt injection called the most persistent and hard-to-fix threat. Evidence is via Cloud Security Alliance analyses [S35]; the primary advisory was not fetched.
- **OWASP Top 10 for Agentic Applications 2026** (9 Dec 2025; ASI01–ASI10) [S36]. A separate OWASP MCP-specific Top 10 is reported to be in beta by a secondary source only [Grade C].
- **Conflicting claim, not adopted:** one secondary article says NSA and CISA *jointly* published MCP guidance on 2 Jun 2026 [S54]. NSA's own document and announcement present the 20 May 2026 CSI as an NSA AISC publication; the claim is likely a conflation with the separate Five Eyes advisory.

**8.2 Vulnerability register (2026 unless stated).**

| Identifier | Component | Class | Disclosed | Source | Grade |
|---|---|---|---|---|---|
| CVE-2026-45609 (GHSA-qjp4-4jvr-xqg3) | Spring AI community `mcp-client-security` OAuth library | **SSRF via OAuth discovery with dynamic client registration** | 2026-05-29 | GitHub advisory / CVE record [S38] | A/B |
| CVE-2026-27825, CVE-2026-27826 | `mcp-atlassian` server | Unauthenticated RCE and SSRF (CVSS 9.1 and 8.2 as reported; per-ID class mapping not re-verified) | Feb 2026 | Pluto Security; Arctic Wolf [S37] | B |
| CVE-2026-104120 | `mcp-server-fetch` / `mcp-server-everything` reference servers (≤ 2026.6.4) | **SSRF** in the fetch-URL tool | 2026-10-02 | OpenCVE aggregator [S39] | B |
| CVE-2026-44192 | Red Hat Ansible Lightspeed MCP server | **Path traversal reachable through indirect prompt injection** | 2026 | Red Hat security advisory [S40] | A/B |
| (no CVE; design-level) | STDIO transport configuration → command execution; downstream CVEs in several host/framework projects | OX Security: systemic; ~7,400 publicly reachable servers confirmed, extrapolated "up to 200,000"; Anthropic reported to regard it as expected behavior | Apr 2026 | OX Security blog; secondary press [S41] | B/C (vendor research; dispute unresolved) |
| (no CVE) | A2A multi-agent systems | **Agent session smuggling** PoC (trust abuse in stateful sessions) | late 2025 | Unit 42 [S42, S43] | B |
| CVE-2025-6514; CVE-2025-49596; mcp-server-git CVE chain (Jan 2026) | `mcp-remote`; MCP Inspector; reference git server | RCE/command-injection class | 2025–Jan 2026 | **Recalled** | **D** |

Reading the register: all four verified CVE entries involve code that **fetches or resolves attacker-influenced URLs or paths** — SSRF appears in three of the four entries and path traversal in the fourth (the mcp-atlassian entry also includes RCE). That is a pattern addressable by library design and gateway egress control, not a mystery. Three of the four sit in *community or reference* components (a community OAuth library, a reference server, a community SaaS server), reinforcing the repository's not-production-ready warning. The AAIF Momentum Report's ~2.6× growth in unpatched CVEs (≈9,200 in the tracked set, Dec 2025 → Jun 2026) shows volume growing with ecosystem size [S03].

**8.3 Structural issues (not single bugs).**
- *STDIO and local trust.* Launching a subprocess from configuration is a code-execution primitive; OX says that is a protocol-level flaw, while the maintainers' position is reported as by-design. The 2026-07-28 roadmap's transport unification may change the local-server story but I found no spec text resolving the dispute [S07, S41].
- *Tool poisoning, rug pulls, injection via tool output.* Documented in vendor and academic write-ups (several recalled, Grade D); mitigations in the catalog below.
- *Static secrets.* 53% static secrets / 8.5% OAuth in Astrix's 2025 scan of OSS servers [S44]; sample skews local/OSS.
- *Gateway bypass.* Microsoft's ADR on server-side invocation [S31].

**8.4 Defensive control catalog.** "Basis" distinguishes what a source recommends from my own synthesis.

| Threat | Control | Enforced at | Basis |
|---|---|---|---|
| Unvetted or shadow servers | Default-deny registry and allowlist; discover unsanctioned servers on the network | Control plane; egress | Uber [S27]; Cloudflare [S30]; NSA [S34] |
| Tool poisoning / definition drift ("rug pull") | Pin and hash tool definitions; diff-and-approve changes; re-approve on drift | Control plane crawler | Uber [S27]; vendor claim [S53]; NSA [S34] |
| Indirect prompt injection via tool/peer output | Treat all tool and A2A outputs as untrusted; filter/DLP outputs; least-privilege tools; avoid combining untrusted-input reading with sensitive-write capability in one session | Data plane; agent design | NSA [S34]; Five Eyes [S35]; OWASP [S36] |
| Confused deputy / privilege escalation | Propagate the *user's* identity; token exchange/OBO; **no token pass-through**; per-tool authorization | Data plane | Uber [S27]; Databricks [S32]; AgentCore [S28] |
| SSRF (discovery, registration, fetch tools) | Block private/link-local/metadata ranges; HTTPS-only; egress allowlists; validate redirects; harden *both* client discovery and authorization-server metadata fetches | Libraries; egress proxy | CVE-2026-45609, CVE-2026-104120 [S38, S39]; analysis |
| Command injection / STDIO | Never build commands from untrusted configuration; sandbox local servers; prefer authenticated remote servers | Host; platform | OX [S41]; NSA [S34] |
| Static or long-lived secrets | Short-lived OAuth tokens; secret brokering; rotate | Data plane; IdP | Astrix [S44]; analysis |
| Replay / tampering | Time-bound message signing (not in base protocol); TLS everywhere | Gateway/host | NSA [S34] |
| Data exfiltration | Egress DLP; response projection; PII redaction | Data plane | Uber [S27]; Cloudflare [S30]; NSA [S34] |
| Insufficient audit | Log every call with identity, params/hash, decision; OTel trace IDs; SIEM export | Data plane | NSA [S34]; spec trace-context conventions [S06] |
| Runaway agents / abuse | Per-identity and per-tool quotas; budget caps | Data plane | agentgateway [S33]; Microsoft [S31] |
| Untrusted peer agents (A2A) | Verify Agent Cards (signatures where supported); allowlist peers; constrain multi-turn follow-ups; human approval for sensitive actions | A2A gateway; agent design | Unit 42 [S42]; spec [S14] |
| Supply chain / unmaintained servers | Pin versions; SBOM; prefer maintained servers; treat reference servers as examples only; track CVEs | Build pipeline | Servers repo README [S10]; AAIF report [S03]; NSA [S34] |

**8.5 Production postmortems — honest gap.** I searched for enterprise-authored incident postmortems of MCP/A2A deployments. I found vulnerability disclosures, vendor research, and design write-ups (Uber's article is a design account, not a postmortem), but **no end-user-company postmortem of a production MCP/A2A incident**. Absence of public postmortems is not evidence of absence of incidents.

### 9. Hiring demand — what is and is not verified (RQ3)

**"Verified hiring volume" in the strict sense (filled hires) is not available from any public source found.** What exists are postings indexes, which measure *intent*, not hires.

**9.1 Three independent keyword indexes (different universes — do not average).**

| Source | Universe | Window | Match rule | MCP result | Derived (my arithmetic) | Main limits | Grade |
|---|---|---|---|---|---|---|---|
| API Evangelist, Q3 2026 [S19] | 343,299 postings from 984 companies (775 Fortune 1000 + 209 API providers) | Q3 2026 (first quarter measured; no trend) | Full phrase "Model Context Protocol" (the abbreviation "MCP" alone is not counted, so this undercounts) | 234 postings; 102 companies | **0.068%** of postings (≈1 in 1,470); **10.4%** of companies; 11.0% of Fortune 1000 vs 8.1% of API providers | Intent only; sample is not the labor market; no trend; one analyst | C |
| Skillenai [S20–S22] | Index built from ~2.6k identified employers | 90 days to 14 Oct 2026 | Skill taxonomy entry "MCP" | **1,747 postings**; ~**0.7%** adjusted share; +9.7% share vs prior four weeks | Earlier snapshot (90 days to 2 Sep) showed 1,359 → +29% in ~6 weeks (windows overlap; coverage may shift) | Composition unaudited; measures posting mix | C |
| landed.jobs [S23] | 115,348 postings, 14,849 companies (5,849 AI-native); share of *engineering* postings; data to 2 Jul 2026 | Jan–Jun 2026 | "MCP" | 1.2% (Jan) → between **2.7%** and **4%** by mid-2026 (the text, a chart legend, and a forecast section disagree) | 2.3×–3.3× rise | AI-native skew; internal inconsistency | C |

*Reading across them (analysis):* (1) the figures are mutually plausible if engineering roles are a minority of all postings, but that is my inference, not a sourced reconciliation; (2) breadth is notable — about one in ten sampled Fortune-1000/API companies named MCP at least once — while per-company intensity is low; (3) all three show strong 2026 growth from a small base; (4) none shows MCP as a majority requirement. API Evangelist also reports that almost all (95 of 102) companies naming MCP also name a major AI vendor, and that postings split between builder roles and reviewer/security-governance roles [S19].

**9.2 Protocol vs framework on a single methodology (Skillenai).** Role percentages on this site run in two directions — *share of a role's postings that mention a skill* vs *share of a skill's postings that carry a role title* — so check the denominator before quoting any figure.

| Measure | MCP | LangGraph | Note |
|---|---|---|---|
| Postings, 90 days | 1,747 | 2,228 | MCP ≈ **0.78×** LangGraph (computed) |
| Adjusted share of index | ~0.7% | ~0.9% | |
| Share of "Agentic AI Engineer" postings mentioning the skill | **13.8%** (9) | **35.8%** (24) | Framework ≈ 2.6× MCP in agent-titled roles |
| "Agent Engineer" title (only 28 postings in 90 days) | outside the top 15 skills | 39.3% (LangChain 42.9%) | Tiny n |
| MCP postings that also mention LangGraph | 14.9% (261 of 1,747) | — | MCP appears mostly *outside* the LangGraph audience |
| Role mix of MCP postings | Software Engineer 21.0% (367); AI Engineer 9.2% (160); Product Manager 8.0% (140) | — | Spread across functions |
| Highest role-level MCP shares (small n) | AI Enablement Engineer 30.2% (16); Frontier Agents Engineer 27.3% (6); AI Application Engineer 20.0% (6); AI Security Specialist 13.0% (3) | — | Small samples |
| Top co-occurring skills in MCP postings | Python 849 · TypeScript 476 · RAG 378 · CI/CD 362 · AWS 312 · LLMs 282 · SQL 273 · LangGraph 261 · Claude Code 258 · Kubernetes 254 | — | |
| Top employers by MCP postings | MintMCP 40 · ServiceNow 24 · Cisco 23 · Ping Identity 22 · Anthropic 17 · NVIDIA 17 · Parloa 17 | — | Skews to gateway/identity/platform vendors (analysis) |

*Interpretation:* in raw volume MCP is already close to a leading agent framework in this index, yet **framework skills still dominate agent-titled roles**, and MCP is spread across software, AI, product, and security functions rather than concentrated in agent roles. Both are keyword counts, not requirement levels.

**9.3 Sampled job descriptions (paraphrased; excerpts only).**
- *Senior Platform Engineer – Enterprise AI* (Boston Scientific) [S24]: build and operate MCP platforms; establish gateway and control-plane capabilities (service discovery, authentication, authorization, routing, policy enforcement, observability); define secure integration patterns including identity propagation and human-in-the-loop approvals; MCP governance and service lifecycle; hands-on MCP client/server/gateway experience; API management, service mesh, and multi-cloud background.
- *Senior Enterprise AI Control Plane Engineer* (PTC; 5–8 years) [S25]: configure and operate MCP and LLM gateways, policies, access control, observability, and agent registries; "techno-functional" with an API-management/governance foundation; onboard internal and vendor MCP servers through a common gateway; OAuth/OIDC/JWT/RBAC/managed-identity patterns; preferred experience with Azure APIM MCP capabilities, Microsoft Foundry AI Gateway, LiteLLM, and iPaaS agent platforms; observability stacks (OpenTelemetry, Datadog, Splunk, Grafana).
- *Senior Product Manager, Enterprise MCP/AI Control Plane* (Workato) [S26]: roadmap for gateway pillars (OAuth, OIDC, DCR, M2M auth; policy; observability; runtime performance) and MCP server lifecycle (tiering, certification) across "hundreds of MCP servers and millions of tool invocations."
- *Pattern (analysis):* these roles are **API-gateway + IAM + AI-governance hybrids with MCP literacy**. In the excerpts seen, none lists JSON-RPC, SSE, or WebSocket as an explicit requirement; "protocol-level" appears as "MCP concepts, servers, clients, tools." Full postings may differ.
- Other postings (a financial-services ML platform role, a consumer-tech ML platform role, a gateway-vendor engineer role) were seen in search results but their URLs were not retained, so **they are excluded from the evidence**.
- A freelance-marketplace hiring guide lists JSON-RPC transport experience, OAuth 2.1, token scoping, audit logging, and an "enterprise MCP gateway" project tier as screening topics [S55] — marketing content showing how the skill is described, not data on demand.

**9.4 What the evidence establishes and what it does not.**
- *Established:* MCP appears across a broad set of large companies but thinly per company; mentions rose sharply within 2026; gateway/control-plane roles exist, under platform and API-management titles; framework skills still lead agent-titled roles.
- *Not established:* hires (as opposed to postings); required vs preferred status; any measure of JSON-RPC, SSE/WebSocket transport, or tool-schema authoring as separate skills (a targeted search returned only tutorials and a marketplace page); trend beyond 2026; whether the literal gateway-engineer title exists anywhere in volume.
- *What would settle it:* a Lightcast/Indeed/LinkedIn pull with a fixed phrase list ("MCP", "Model Context Protocol", "MCP server", "A2A", "agent gateway"); an ATS crawl with de-duplication; parsing of required vs preferred language; added keywords for JSON-RPC and transport terms.

### 10. Protocol-native architectures vs framework wrappers (RQ4)

The four patterns below are not mutually exclusive; the table compares their characteristic strengths and costs. **Basis legend:** [E] sourced evidence, [A] analysis.

| Dimension | A. Protocol-native (MCP server behind a gateway) | B. Framework-native tools (in-process) | C. Framework wrapper consuming MCP | D. Code-mode / CLI over MCP or APIs |
|---|---|---|---|---|
| Portability across agent hosts | High — any MCP client; vendor hosts connect [A] | Low — tied to one framework runtime [A] | Medium — server portable, client framework-specific [E: adapters exist, S51] | Medium — depends on sandbox/runtime [A] |
| Central policy and audit point | Yes — gateway [E: S27–S33] | No — per application [A] | Partial — only if routed via a gateway [A] | Via gateway in front of MCP/API; none for raw CLI [A] |
| Identity propagation | Standardizing: OAuth model, EMA; OBO/token exchange in gateways [E] | Ad hoc [A] | Inherits server/gateway auth; wrapper must pass tokens [A] | Depends on runtime [A] |
| Context/token cost | High if full schemas are loaded; mitigated by progressive discovery [E: S07, S27, S28] | Smaller toolsets typical, same per-tool cost [A] | Same as A [A] | Low — illustrative ~150,000 → ~2,000 tokens [E: S46] |
| Latency | Extra gateway hop [A] | Lowest [A] | Extra hop [A] | Extra execution/sandbox step [A] |
| Versioning churn | Spec and SDK churn (07-28; SDK v2) [E: S06, S50] | Framework churn [A] | Both [A] | Both [A] |
| Testing/conformance | Tiered SDK conformance suite exists [E: S08] | Framework-specific [A] | Adapter tests [A] | Sandbox testing [A] |
| Security surface | Server/gateway; known CVE classes [E: §8] | App-local [A] | Inherits MCP plus wrapper [A] | Code-execution sandbox risk [A] |
| Hiring signal | Platform/API/IAM roles; "MCP" keyword [E: §9] | Framework skills dominate agent-titled roles [E: S20–S22] | Both | Emerging; not measured |

**Evidence limits:** no controlled benchmark comparing these patterns on latency, reliability, or total cost was found; the only quantified comparison is Anthropic's illustrative token example, which the post presents as an example rather than a measurement across tasks [S46]. The LF-authored Momentum Report's contributor-health comparison favors foundation-hosted projects but is not independent [S03].

### 11. Tool catalog (production SDKs, gateways, testing)

Status key: **V** = verified this session (grade in the ledger); **R** = recalled, not verified (Grade D).

| Category | Tool | Status | Notes | Source |
|---|---|---|---|---|
| SDK | Python SDK (`mcp`, v2 line) | V | Tier 1; community FastMCP 4.x (v4.0.3 observed) depends on mcp 2.2.0; v2 migration breakage reported downstream | S05, S50 |
| SDK | TypeScript SDK (`@modelcontextprotocol/sdk` v1; v2 split into core/server/client packages) | V | Tier 1; v2 removes server-side SSE | S05, S50 |
| SDK | Go SDK; C# SDK | V | Tier 1 | S05 |
| SDK | Rust SDK (`rmcp`) | V | Beta at launch; README later describes stable-revision support | S05, S50 |
| SDK | Java, Kotlin, PHP, Ruby, Swift SDKs | V (listed) | Listed as official in the servers repo; tier not verified | S10 |
| Framework | FastMCP (PrefectHQ / community) 4.x | V | Tracks the new spec; session-state caveat in stateless mode | S50 |
| Adapter | `vercel/mcp-handler` | V | Next.js/Vercel adapter; present in repo results | S50 |
| Adapter | `langchain-mcp-adapters` (Python, JS; `MultiServerMCPClient`) | V | Docs still reference the 2025-03-26 transport spec | S51 |
| Hosting | Cloudflare Workers (remote MCP servers) + MCP server portals | V | Docs: build remote servers directly on Workers; portals govern them. *"Cloudflare Workers MCP Gateway" is not a verified product name* | S30 |
| Conformance | `modelcontextprotocol/conformance` suite | V | Basis for SDK tiering | S08 |
| Debug | MCP Inspector | R | Exists per general knowledge; not verified this session | — |
| CLI | "mcp-cli" | Ambiguous | Multiple unrelated projects share the name; none verified as canonical | — |
| CLI | A2A CLI | V (listed) | A2A project blog dated 1 Oct 2026; not read | S13 |
| Gateway | agentgateway (AAIF; Rust; Apache-2.0) | V | MCP + A2A federation, CEL RBAC, rate limits, budgets; 300+ contributors across 60+ orgs (project-reported) | S33 |
| Gateway | Agent Router (AAIF; Envoy-based) | V (roster) | No technical details retrieved | S04 |
| Gateway | AWS AgentCore Gateway | V | Aggregation, inbound/outbound auth, Cedar Policy, interceptors | S28, S29 |
| Gateway | Cloudflare MCP server portals + Code Mode | V | See §6.2 | S30 |
| Gateway | Azure API Management AI gateway; Foundry governance | V (preview) | Federates MCP servers; bypass gap documented | S31 |
| Managed servers | Databricks managed MCP | V | UC-enforced, OBO | S32 |
| Gateway | LiteLLM MCP gateway | V (mention) | Bring-your-own option in an AWS sample; named as preferred experience in a PTC posting | S25, S57 |
| Gateway | Vendor MCP gateways (Tyk, Obot, TrueFoundry, Speakeasy; MintMCP appears as a top MCP-hiring company) | V (marketing) | Vendor guides, Grade C | S53, S20 |
| Gateway | Kong, Docker MCP Gateway, IBM ContextForge | R | Not verified this session | — |
| Registry | Official MCP Registry | V | Preview; v0.1 API; per-version rows; no GA evidence | S11 |
| A2A | A2A spec/proto and multi-language SDKs | V | Spec is normative proto; SDK list not audited | S13, S14 |
| UI | AG-UI SDKs; CopilotKit; MCP Apps; A2UI | V | See §4 | S17, S18, S05 |

### 12. Falsification log (calibration rule 4)

| # | Claim tested for failure | What I searched or read | Result |
|---|---|---|---|
| 1 | Enterprises mandate MCP servers for all internal SaaS | Surveys, analyst pieces, postings | **No traceable mandate source.** Security is the top stated obstacle; posting shares are small. Not supported |
| 2 | "78% of enterprise AI teams have MCP in production" | Traced through repeating blogs | **No primary source**; analysts flag as unsourced. Rejected (X) |
| 3 | "Agent Gateway Engineer" is an established title | Literal-title searches; three job indexes | **Not found**; functional equivalents under other titles |
| 4 | NSA and CISA jointly issued MCP guidance on 2 Jun 2026 | NSA PDF and announcement vs one secondary article | NSA-only, 20 May 2026; the "joint" claim is uncorroborated (likely conflation with the Five Eyes advisory) |
| 5 | MCP is being displaced by CLIs/skills | Perplexity remark; Anthropic code-execution post; Uber and Cloudflare code-mode defaults | **Partial:** the invocation pattern is changing; MCP is retained at the governed boundary; the Perplexity remark is second-hand with no transcript found |
| 6 | The spec is settled | 2026-07-28 changelog | **No:** deprecations and removals continue |
| 7 | Reference servers are production-ready | Servers repo README | **No:** explicitly not; many archived |
| 8 | A gateway governs all agent traffic | Microsoft ADR; Cloudflare shadow-MCP rules | **No:** bypass paths and shadow servers exist |
| 9 | Protocol vulnerabilities are only implementation bugs | OX Security vs maintainers' reported position; CVEs | **Disputed,** unresolved |
| 10 | Public production postmortems exist | Incident/postmortem searches | **None found** |
| 11 | Gateway rate-limit numbers are published | Vendor doc excerpts | Capabilities yes; **numbers not verified** |
| 12 | Indeed / Lightcast / LinkedIn published MCP posting statistics | Queries naming those sources | **None surfaced** |
| 13 | JSON-RPC / SSE / WebSocket / tool-schema requirements are measured in postings | Targeted query | **No dataset;** tutorials and a marketplace page only |
| 14 | MCP Registry size is obtainable | Live API | **No total count;** rows are per version; secondary counts unverifiable |
| 15 | AG-UI is foundation-governed | AAIF roster; repo | **No** |
| 16 | A2A includes auction/bid negotiation | Spec | **No** such primitives |

### 13. DONE-criteria check

| Criterion | Status | Notes |
|---|---|---|
| Governance status, spec version, industry backing of MCP and related protocols verified | **Met** | MCP, A2A, AG-UI, ACP all placed with primary sources; spec = 2026-07-28; backing = AAIF members, partner statements; caveat on founder veto |
| Enterprise security and gateway patterns (auth, rate limiting, audit) codified | **Met, with gaps** | §6–§8 codify patterns and a control catalog; numeric rate-limit values and HITL outcome data not verified |
| Verified hiring volume and JD requirements for protocol skills documented | **Partly met** | Volume measured via three indexes (Grade C); JD requirements sampled (three postings); **protocol-level vs framework-level percentages cannot be computed** from any public data found |
| Protocol-native vs framework-wrapper comparisons established | **Met qualitatively (B/C)** | No controlled benchmark exists in sources found |
| Protocol security vulnerabilities and defensive patterns detailed | **Met** | §8 register and controls; recalled items flagged D |

## Open Questions & Risks

### Strongest objections an expert would raise (calibration rule 4)

| # | Objection | Evidence for | Evidence against | Net assessment |
|---|---|---|---|---|
| 1 | "Your hiring numbers are keyword counts in unrepresentative indexes; they cannot support any claim about *volume*, let alone *hires*." | All three are indexes with disclosed limits; no census; landed.jobs is internally inconsistent; postings ≠ hires | Three different universes agree on order of magnitude (small, rising) | **Largely valid.** The verdict is phrased "not verified at scale," and Action 5 prescribes a fixed-universe quarterly re-measure |
| 2 | "Foundation governance is a fig leaf: the founders keep a veto." | Contributor ladder reserves Lead Maintainer (veto, appoints core maintainers) for founders | Broad vendor membership (247 orgs); partner statements incl. an OpenAI-affiliated core maintainer; LF-reported contributor-health data (not independent) | **Partly valid.** Flagged in KF-1; I could not verify actual voting patterns or maintainer affiliations |
| 3 | "MCP is losing to CLI/skills; calling it a standard lags the market." | Perplexity remark (second-hand); context-cost evidence; Uber and Cloudflare default to code mode | Spec release, hyperscaler gateways, NSA guidance, AAIF growth, ~10% of sampled Fortune-1000 companies naming MCP; code mode runs *on top of* MCP at Uber and Cloudflare | **Valid for the invocation pattern, not for the governed integration boundary.** Watch for hyperscalers de-emphasizing MCP gateways |
| 4 | "No public mandate evidence ≠ no mandates; internal policies are rarely published." | True: internal policy is invisible | No source evidences the pattern either way | **Valid.** The claim stays *unverified*, not *falsified*; the report only says "not supported by public evidence" |
| 5 | "Adoption metrics (downloads, stars) are inflated by CI, mirrors, and hype." | Downloads and stars are self-reported attention proxies | I graded them B and did not rely on them as primary evidence; government guidance and CVE volume are independent signals of real deployment | **Valid;** mitigated by grading |
| 6 | "The security record is vendor-hyped: OX sells security; most CVEs are in community code, not the protocol." | OX has commercial incentive; three of four verified CVE entries are community/reference components | NSA and OWASP independently address MCP/agentic risk; AAIF's own report shows CVE growth; the maintainers' reported "by design" stance concedes the local-trust model | **Partly valid.** The design-level claim is unresolved; the SSRF/path-traversal pattern holds regardless |
| 7 | "Operational advice built on the stateless 2026-07-28 model is premature; the tooling lags." | SDK v2 breakage, observability gaps, docs pinned to older transport spec | Tier 1 SDKs with conformance gating; partner support statements | **Valid.** Recommendation 1 says pin versions and plan migration |
| 8 | "The A2A→AAIF move rests on the project's own announcement." | Single project-authored post for the move itself | The AAIF roster independently lists A2A | **Low risk;** corroborated by a second primary page |
| 9 | "The analyst is an Anthropic model reporting on an Anthropic-originated protocol." | MCP originated at Anthropic; I am Claude | Primary sources preferred; vendor/LF/project-authored sources flagged; counter-evidence (OX dispute, Perplexity, context cost, founder veto) deliberately included | **Disclosed.** Readers should weight Grade A items from non-Anthropic sources (NSA, hyperscaler docs, CVE records) most heavily |

### Open questions

- **O-1** What share of large enterprises runs *any* production MCP server, and how many internal SaaS systems does that cover? No census exists; Stacklok is n=100 per sector and vendor-run.
- **O-2** Does AAIF governance change A2A's spec process (SEP-style proposals, conformance suites)? Check outputs of AGNTCon + MCPCon (22–23 Oct 2026), which postdate this evidence.
- **O-3** Will AG-UI join a neutral foundation, and will MCP Apps / A2UI / AG-UI converge?
- **O-4** When does the MCP Registry reach general availability, and will enterprise private sub-registries emerge?
- **O-5** Will the spec address the STDIO command-execution dispute, e.g., via transport unification?
- **O-6** Is A2A Agent Card signature verification mandatory for clients, or optional (§4)?
- **O-7** What is the exact Enterprise-Managed Authorization flow and which IdPs support it? (Recalled; EMA post body not captured.)
- **O-8** What are the numeric rate-limit, quota, and throughput characteristics of AgentCore Gateway, Cloudflare portals, APIM, and agentgateway?
- **O-9** Hiring: required-vs-preferred parsing; JSON-RPC/transport keyword incidence; hires vs postings; Lightcast/Indeed/LinkedIn pulls.
- **O-10** Primary source for the March 2026 Perplexity remark (transcript or official statement).
- **O-11** Which gateways already implement the 2026-07-28 headers, caching, and stateless model?
- **O-12** Verify the recalled (Grade D) items listed in the Ledger addendum before any external citation.

### Risks

- **R-1 Timing.** AGNTCon + MCPCon North America (22–23 Oct 2026) falls one day after the evidence cutoff and may change governance, roadmap, or adoption claims.
- **R-2 Source interest.** The MCP blog, AAIF/LF reports, CopilotKit, Stacklok, OX, Astrix, and gateway vendors each have organizational or commercial interests; grades reflect this.
- **R-3 Author conflict.** See objection 9. The analysis was produced by an Anthropic model.
- **R-4 Index volatility.** Job indexes are keyword-based, change composition, and use different denominators.
- **R-5 Rapid change.** The spec/SDK ecosystem is mid-migration; operational notes may age within a quarter.
- **R-6 Memory-derived items.** Items marked D must not be cited externally without verification.
- **R-7 Small date conflicts.** Five Eyes advisory (30 Apr vs 1 May 2026) and CopilotKit funding split ($20M+$7M vs $20.5M+$6.5M) differ across secondary sources; immaterial to conclusions.
- **R-8 Evidence capture limits.** A few search results seen during the session were not retained with URLs; the corresponding facts were excluded rather than cited (e.g., other job postings).

## Delta

| # | Prior belief (Grade D) | What the evidence showed | Direction | Evidence grade |
|---|---|---|---|---|
| P1 | AAIF is the LF vehicle (not "Interoperability Framework"); A2A is separate | **Confirmed** name and founding projects (MCP, goose, AGENTS.md). **Updated:** A2A announced joining AAIF (27 Aug 2026); AAIF now hosts six projects incl. two gateways; 247 members; naming error in the brief confirmed | Confirmed + updated | A |
| P2 | Latest MCP spec is 2025-11-25 | **Contradicted.** Current is **2026-07-28**: stateless core, routing headers, cacheable lists, MRTR, auth hardening, formal extensions, deprecations, SDK tiers | Contradicted | A |
| P3 | IBM ACP merged into A2A; "ACP" is overloaded | **Confirmed** (29 Aug 2025). **Added:** OpenAI/Stripe's Agentic Commerce Protocol appears in the AAIF launch release | Confirmed | A |
| P4 | AG-UI is CopilotKit-led, not foundation-hosted; adoption vendor-reported; 1.0 uncertain | **Confirmed** not in AAIF; adoption claims are company-reported. **Updated:** 1.0 declared 18 Sep 2026 | Confirmed + updated | A / B |
| P5 | MCP mentions small but fast-growing; protocol-level < framework mentions; no gateway-engineer title; mandate claim unsupported | **Confirmed in direction and now quantified:** 0.068% / ~0.7% / 2.7–4% depending on universe; framework skills lead agent-titled roles; gateway work appears as platform/control-plane titles; protocol-level skills **unmeasured**; mandate claim unsupported | Confirmed + quantified | C |
| K1 | *(Brief, UNVERIFIED)* "MCP is the HTTP of generative-AI tooling" | **Partly supported** (neutral governance, multi-vendor, SDK conformance) but overstated: still shedding features, unresolved context-cost and security issues, reference servers not production-ready | Qualified | A/B |
| K2 | *(Brief)* "Enterprise teams mandate MCP servers for all internal SaaS" | **Not supported by public evidence;** survey shows security-limited adoption; posting shares small; "78%" statistic untraceable | Not supported | B/C, X |
| K3 | *(Brief)* "High demand for engineers who understand protocol-level agent integration" | **Demand is real but small and fast-growing;** concentrated in platform/API/IAM/security roles; *protocol-level* demand specifically is not measured by any dataset found | Partly supported | C |
| S1 | *(Surprise)* A2A under AAIF | New since my prior | Updated | A |
| S2 | *(Surprise)* Uber's evidence that raw MCP tool lists do not scale (meta-tools, code mode) | Challenges "plug-and-play" narrative while retaining MCP as the boundary | Updated | A |
| S3 | *(Surprise)* NSA published MCP-specific guidance; AAIF's own report shows ~2.6× unpatched-CVE growth | Raises the security bar for any enterprise claim of "mature" | Updated | A |
| S4 | *(Surprise)* Founder veto in MCP technical governance despite foundation hosting | Qualifies "neutral standard" | Updated | A |
| M1 | *(Memory check)* Anthropic's code-execution-with-MCP example (~150,000 → ~2,000 tokens) | **Verified** in the original post (98.7% reduction stated for the example) | Confirmed | A |
| M2 | *(Memory check)* Specific 2025 CVEs (mcp-remote, MCP Inspector, mcp-server-git chain) | **Not verified** this session | Unverified | D |

## Sources & Evidence Ledger

**Access key:** *Fetched* = page read in full or substantially; *Excerpt* = search-result excerpt only (primary content seen but page not opened); *Domain+title* = deep link not retained, so only the domain and document title are given (no URL is invented). Dates are as stated in or inferred from the source.

| ID | Source (title) | Locator | Type | Date | Access | Grade | Used for |
|---|---|---|---|---|---|---|---|
| S01 | Linux Foundation, "Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)…" | https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-Agentic-ai-foundation | Foundation press release | 2025-12-09 | Fetched | A | KF-1, §1, §3 |
| S02 | AAIF, "Agentic AI Foundation Welcomes 57 New Members" | https://aaif.io/news/agentic-ai-foundation-welcomes-57-new-members | Foundation news | 2026-08 | Fetched | A | KF-1, §3 |
| S03 | AAIF, "Agentic AI Momentum Report" | https://aaif.io/report/agentic-ai-momentum-report/ | Foundation (LF-authored) report | 2026 (undated in retrieved text) | Fetched | A/B | KF-5, KF-8, §3, §5, §8 |
| S04 | AAIF, Projects page | https://aaif.io/projects | Foundation roster | retrieved Oct 2026 | Fetched | A | KF-1, KF-4, §1 |
| S05 | MCP blog, "The 2026-07-28 Specification" | https://blog.modelcontextprotocol.io/posts/2026-07-28/ | Project blog | 2026-07-28 | Fetched | A | KF-2, KF-5, KF-7, §2, §3 |
| S06 | MCP specification, 2026-07-28 changelog | https://modelcontextprotocol.io/specification/2026-07-28/changelog | Specification | 2026-07-28 | Fetched | A | KF-2, §2, §8 |
| S07 | MCP blog, 2026 roadmap (and "Enterprise-Managed Authorization" post, title located, body not captured) | https://blog.modelcontextprotocol.io/posts/mcp-roadmap/ ; https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/ | Project blog | 2026-08-22 | Fetched (roadmap) | A | KF-2, KF-7, §2, §6, §7 |
| S08 | MCP docs, SDK tiers | https://modelcontextprotocol.io/community/sdk-tiers | Project docs | n.d. | Fetched | A | §2, §11 |
| S09 | MCP docs, contributor ladder; working and interest groups; governance working group | https://modelcontextprotocol.io/community/contributor-ladder ; https://modelcontextprotocol.io/community/working-interest-groups.md ; https://modelcontextprotocol.io/community/working-groups/governance | Project docs | n.d. | Excerpt | A (excerpt) | KF-1, §3 |
| S10 | GitHub, modelcontextprotocol/servers | https://github.com/modelcontextprotocol/servers | Repository | retrieved Oct 2026 | Fetched | A | KF-5, KF-12, §5, §11 |
| S11 | MCP Registry live API; Registry docs (aggregators page) | https://registry.modelcontextprotocol.io/v0.1/servers?limit=100 ; domain+title: modelcontextprotocol.io registry docs | Registry / docs | retrieved Oct 2026 | Fetched / excerpt | A | §5, §11 |
| S12 | A2A blog, "A2A Protocol Ships v1.0…" | https://a2a-protocol.org/latest/blog/2026/03/12/a2a-protocol-ships-v10-production-ready-standard-for-agent-to-agent-communication/ | Project blog | 2026-03-12 | Fetched | A | KF-3, §4 |
| S13 | A2A blog, "A New Chapter for A2A: Joining the Agentic AI Foundation" | https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ | Project blog | 2026-08-27 | Fetched | A | KF-3, §1, §11 |
| S14 | A2A Protocol Specification (latest) | https://a2a-protocol.org/latest/specification/ | Specification | v1.0.x | Fetched | A | KF-3, §4 |
| S15 | Linux Foundation, "A2A Protocol Surpasses 150 Organizations…" | https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year | Foundation press release | 2026-04-09 | Fetched | A (LF claim) | KF-3, §5 |
| S16 | LF AI & Data, "ACP Joins Forces with A2A…" | https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ | Foundation community blog | 2025-08-29 | Fetched | A | KF-4, §1, §4 |
| S17 | GitHub, ag-ui-protocol/ag-ui, discussion #2792 (1.0 release) | https://github.com/ag-ui-protocol/ag-ui/discussions/2792 | Repository discussion | 2026-09-18 | Fetched | A | KF-4, §4 |
| S18 | CopilotKit "Series A" post; TechCrunch; GeekWire; Glilot Capital | https://copilotkit.ai/blog/series-a ; https://techcrunch.com/2026/05/05/copilotkit-raises-27m-to-help-devs-deploy-app-native-ai-agents/ ; https://www.geekwire.com/2026/seattles-copilotkit-raises-27m-as-some-of-the-biggest-names-in-tech-adopt-its-ai-agent-protocol/ ; https://glilotcapital.com/?p=3213 | Vendor + press | 2026-05-05/06 | Excerpt | B (company claims) | KF-4, §4, §5 |
| S19 | API Evangelist, "One Hundred Two Companies Hiring for MCP and the Enterprises Are Ahead" | https://apievangelist.com/2026/10/14/one-hundred-two-companies-hiring-for-mcp-and-the-enterprises-are-ahead/ | Analyst blog (job index) | 2026-10-14 | Fetched | C | KF-9, §9 |
| S20 | Skillenai, skill page "MCP" | https://skillenai.com/data/skill/mcp | Job index | snapshot 2026-10-14 | Fetched | C | KF-9, KF-10, §9 |
| S21 | Skillenai, skill page "LangGraph" | https://skillenai.com/data/skill/langgraph | Job index | snapshot 2026-10-13 | Fetched | C | KF-10, §9 |
| S22 | Skillenai, role page "Agent Engineer" | https://skillenai.com/data/role/agent-engineer | Job index | Oct 2026 | Fetched | C | KF-10, §9 |
| S23 | landed.jobs, "The State of AI-Native Jobs 2026" | https://www.landed.jobs/reports/state-of-ai-native-jobs | Vendor report (job index) | data to 2026-07-02 | Fetched | C | KF-9, §9 |
| S24 | Job posting: Senior Platform Engineer – Enterprise AI (Boston Scientific), freehire.me copy | https://freehire.me/jobs/senior-platform-engineer-enterprise-ai-boston-scientific-eno7vkib | Job posting | n.d. | Excerpt | C | KF-10, §9 |
| S25 | Job posting: Senior Enterprise AI Control Plane Engineer (PTC), Dice and zapply.jobs copies | https://www.dice.com/job-detail/4c7924c5-2562-4841-b07b-0e1d95c74885 ; https://zapply.jobs/jobs/31cfdbf5-4fe8-4108-a333-6d54e678b0e9/ | Job posting | ~Sep 2026 | Excerpt | C | KF-10, §9, §11 |
| S26 | Job posting: Senior Product Manager, Enterprise MCP/AI Control Plane (Workato), aidevboard copy | https://aidevboard.com/job/senior-product-manager-enterprise-mcpai-control-plane-c695b425 | Job posting | n.d. | Excerpt | C | KF-10, §9 |
| S27 | Uber Engineering, "Designing MCP Gateway: Uber's MCP Management Platform" | https://www.uber.com/ca/en/blog/designing-mcp-gateway/ | Enterprise engineering blog | 2026-10-01 | Fetched | A (self-reported) | KF-6, KF-11, §6, §8 |
| S28 | AWS docs, Amazon Bedrock AgentCore Gateway: core concepts; Runtime targets. Two specific claims rest on secondary AWS-related pages: the one-request/one-response interceptor limit (AWS open-source MDAA infrastructure schema) and CloudWatch/CloudTrail/X-Ray integrations (a repost of an AWS blog on API Gateway targets) | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.md ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-http-runtime.html ; https://aws.github.io/modern-data-architecture-accelerator/typedocs/interfaces/_aws-mdaa_bedrock-builder-l3-construct.GatewayConfigProps.html ; https://aihub.hkuspace.hku.hk/?p=5403 | Vendor product docs; AWS open-source schema; blog repost | n.d. | Excerpt | A (core docs) / B (the two specific claims) | KF-6, §6 |
| S29 | AWS What's New, "Policy in Amazon Bedrock AgentCore is now generally available" (German-locale page as retrieved) | https://aws.amazon.com/de/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/ | Vendor announcement | 2026-03 (GA date 3 Mar 2026 per secondary guide) | Excerpt | A | KF-6, §6 |
| S30 | Cloudflare docs, MCP server portals; "Code mode for MCP server portals" changelog; Access changelog; Cloudflare blog on governing MCP (Code Mode, shadow-MCP detection) | https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/index.md ; https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/index.md ; https://developers.cloudflare.com/changelog/product/access/index.md ; https://blog.cloudflare.com/author/ivan-anguiano/rss | Vendor product docs / blog | 2025-08-26 (portals); 2026-03-26 (Code Mode) | Excerpt | A | KF-6, §6, §8, §11 |
| S31 | Microsoft: Learn, "AI Gateway tier (preview) overview" (API Management); Learn, "Govern MCP tools by using an AI gateway (preview)" (Foundry); microsoft.github.io/agent-governance-toolkit, ADR 0026 (Foundry AI gateway / functions PDP) | Domain+title (deep links not retained): learn.microsoft.com; microsoft.github.io/agent-governance-toolkit | Vendor docs; open-source ADR | 2026 | Excerpt | A (docs) / B (ADR) | KF-6, KF-12, §6, §8 |
| S32 | Databricks docs, "Managed MCP servers" | Domain+title: docs.databricks.com (agents / MCP tools) | Vendor product docs | 2026 | Excerpt | A | KF-6, §6 |
| S33 | agentgateway, "agentgateway Joins AAIF as an Open Gateway for Agentic AI Infrastructure"; docs | https://agentgateway.dev/blog/2026-06-04-agentgateway-joins-aaif/ ; https://agentgateway.dev/docs/kubernetes/main/ | Project blog / docs | 2026-06-04 | Excerpt | B | KF-6, §6, §11 |
| S34 | NSA AISC, "Model Context Protocol (MCP): Security Design Considerations for AI-Driven Automation" (U/OO/6030316-26) | https://www.nsa.gov/Portals/75/documents/Cybersecurity/CSI_MCP_SECURITY.pdf | Government guidance | 2026-05 (announced 2026-05-20) | Fetched | A | KF-7, §7, §8 |
| S35 | Cloud Security Alliance research notes on the Five Eyes "Careful Adoption of Agentic AI Services" advisory | https://labs.cloudsecurityalliance.org/research/csa-research-note-cisa-agentic-ai-security-guide-enterprise/ ; https://labs.cloudsecurityalliance.org/research/csa-whitepaper-five-eyes-agentic-ai-guidance-analysis-202605/ | Secondary analysis of government advisory | 2026-05 | Excerpt | B | §8 |
| S36 | OWASP GenAI Security Project, "OWASP Top 10 for Agentic Applications for 2026" (genai.owasp.org; canonical page not opened); BleepingComputer coverage; Teleport explainer | https://www.bleepingcomputer.com/news/security/the-real-world-attacks-behind-owasp-agentic-ai-top-10/amp ; https://goteleport.com/blog/owasp-top-10-agentic-applications | Standards body (via press/vendor coverage) | 2025-12-09 | Excerpt | B | §8 |
| S37 | Pluto Security and Arctic Wolf write-ups on mcp-atlassian CVE-2026-27825 / CVE-2026-27826 | Domain+title: pluto.security blog; arcticwolf.com blog | Researcher / MDR vendor | 2026-02 | Excerpt | B | KF-8, §8 |
| S38 | CVE-2026-45609 / GHSA-qjp4-4jvr-xqg3 (Spring AI community `mcp-client-security`) | Identifier anchors: cve.org record; GitHub Advisory Database | CVE record / advisory | 2026-05-29 | Excerpt | A/B | KF-8, §8 |
| S39 | CVE-2026-104120 (`mcp-server-fetch` / `mcp-server-everything` SSRF), OpenCVE | Identifier anchor: opencve.io record | CVE aggregator | 2026-10-02 | Excerpt | B | KF-8, §8 |
| S40 | CVE-2026-44192 (Ansible Lightspeed MCP server), Red Hat security page | Identifier anchor: access.redhat.com/security/cve | Vendor advisory | 2026 | Excerpt | A/B | KF-8, §8 |
| S41 | OX Security, "The Mother of All AI Supply Chains: Critical, Systemic Vulnerability at the Core of the MCP"; press and CSA coverage of Anthropic's reported response | Domain+title: ox.security blog; secondary: The Register; CSA research note | Vendor research; press | 2026-04 | Excerpt | B/C | KF-8, §8 |
| S42 | Palo Alto Networks Unit 42, "Agent Session Smuggling in Agent2Agent Systems" | https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/ | Vendor research | late 2025 | Excerpt | B | KF-8, §4, §8 |
| S43 | eSecurityPlanet, "When AI Agents Go Rogue: Inside the Agent Session Smuggling Attack" | https://www.esecurityplanet.com/threats/news-ai-session-smuggling-attack/ | Trade press | late 2025 | Excerpt | B | §4 |
| S44 | Astrix Security, "State of MCP Server Security 2025" | https://astrix.security/learn/blog/state-of-mcp-server-security-2025/ | Vendor research | 2025 | Excerpt | B | KF-7, §8 |
| S45 | Stacklok, "State of Model Context Protocol in Software 2026" (and PDF) | https://stacklok.com/resources/state-of-mcp-in-software-2026/ ; https://stacklok.com/wp-content/uploads/2026/01/State-of-MCP-in-Software-2026_FINAL.pdf | Vendor survey | fielded Dec 2025; published 2026-01 | Excerpt | B/C | KF-5, §5 |
| S46 | Anthropic Engineering, "Code execution with MCP: building more efficient AI agents" | https://www.anthropic.com/engineering/code-execution-with-mcp | Vendor engineering post | 2025-11-04 | Fetched | A | KF-11, §6, §10 |
| S47 | Coverage of the March 2026 Perplexity remark, e.g., Tyk learning-center article on whether MCP is "dead" | Domain+title: tyk.io learning center (primary transcript not found) | Secondary (second-hand) | 2026-03 | Excerpt | C | KF-12 |
| S48 | "78% in production" provenance trail: DigitalApplied; Colrows; Medium (chierhu); Forkast; baeseokjae; andrew.ooo; Bex | https://digitalapplied.com/mcp-adoption-statistics-2026/ ; https://colrows.com/blogs/mcp-enterprise-adoption/ ; https://chierhu.medium.com/the-mcp-server-ecosystem-a-rigorous-survey-for-builders-cbb15b98cd1e ; https://forkast.news/mcp-locked-in-its-architecture-today-now-the-hard-part-enterprise-adoption-at-scale/ ; https://baeseokjae.github.io/posts/mcp-enterprise-adoption-guide-2026/ ; https://andrew.ooo/answers/mcp-model-context-protocol-enterprise-adoption-july-2026/ ; https://bex.co/blog/2026/09/24/mcp-transition-technology-infrastructure-first-deploy-api | Secondary blogs | 2026 | Excerpt | C / X | KF-5, §5 |
| S49 | K2View, "MCP Gartner insights for 2025" | https://www.k2view.com/blog/mcp-gartner/ | Vendor blog summarizing analyst forecast | 2025 | Excerpt | C | §5 |
| S50 | SDK/ecosystem evidence: python-sdk v2.0.0a1 release; FastMCP changelog and discussion #4591; rust-sdk repo; vercel/mcp-handler; PostHog "MCP SDK v2" doc; jupyter-mcp-server issue #325; DEV post on Node.js MCP servers | https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0a1 ; https://gofastmcp.com/changelog ; https://github.com/PrefectHQ/fastmcp/discussions/4591 ; https://github.com/modelcontextprotocol/rust-sdk ; https://github.com/vercel/mcp-handler ; https://posthog.com/docs/mcp-analytics/sdk-v2 ; https://github.com/datalayer/jupyter-mcp-server/issues/325 ; https://dev.to/zsevic/building-an-mcp-server-with-nodejs-55b1 | Repos / docs / issues | 2026 | Excerpt | B | KF-12, §2, §11 |
| S51 | LangChain, langchain-mcp-adapters repo and MCP docs | https://github.com/langchain-ai/langchain-mcp-adapters ; https://docs.langchain.com/oss/python/langchain/mcp | Repository / vendor docs | 2026 | Excerpt | A/B | KF-11, §2, §10, §11 |
| S52 | Speakeasy, MCP release notes (revision summaries) | https://speakeasy.com/mcp/release-notes | Vendor summary | 2025–2026 | Excerpt | B | §2 |
| S53 | Vendor MCP-gateway guides: Tyk; Obot (two posts); TrueFoundry; Speakeasy | https://tyk.io/learning-center/mcp-gateway-architecture-technical-guide/ ; https://obot.ai/blog/the-13-best-mcp-gateways-for-enterprise-teams/ ; https://obot.ai/blog/mcp-gateway-the-solution-to-mcp-sprawl/ ; https://www.truefoundry.com/blog/what-is-mcp-gateway ; https://www.speakeasy.com/resources/mcp-gateway | Vendor marketing | 2026 | Excerpt | C | §6, §11 |
| S54 | tech-insider.org article claiming a joint NSA/CISA MCP publication on 2 Jun 2026 | Domain+title: tech-insider.org (MCP 2026 update article) | Secondary | 2026 | Excerpt | X (conflicts with S34) | §8, §12 |
| S55 | Upwork, "Hire the Best MCP Server Developers" | https://www.upwork.com/hire/mcp-server-developers/ | Marketplace marketing | Oct 2026 | Excerpt | C | §9 |
| S56 | grith.ai, "Google's A2A Protocol Has Zero Defenses Against Prompt Injection" | https://grith.ai/blog/a2a-protocol-zero-defenses-prompt-injection | Security-vendor blog | n.d. | Excerpt | C | §4 |
| S57 | AWS sample, "External MCP → AgentCore Gateway: authorization architecture" (LiteLLM bring-your-own gateway option) | https://aws-samples.github.io/sample-ai-agent-factory/projects/self-service/docs/mcp-gateway-integration/ | Vendor sample docs | n.d. | Excerpt | C | §11 |

### Ledger addendum — recalled claims (Grade D; not verified this session)

| # | Recalled claim | Where it appears | Status |
|---|---|---|---|
| D1 | Dec 2025 launch figures: ~97M monthly SDK downloads and 10,000+ MCP servers | §5 | Re-check against the LF launch page before citing |
| D2 | 2025-11-25 feature list (Tasks, Client ID Metadata Documents, extensions, etc.) and CIMD mechanics | §2 | Verify against the 2025-11-25 spec |
| D3 | Enterprise-Managed Authorization flow (identity-assertion grant / cross-app access) | §7 | Verify against the EMA post and extension spec |
| D4 | AG-UI transport (SSE/HTTP) and event taxonomy | §4 | Verify against AG-UI docs |
| D5 | CVE-2025-6514 (mcp-remote), CVE-2025-49596 (MCP Inspector), mcp-server-git CVE chain (Jan 2026) | §8.2 | Verify against NVD |
| D6 | MCP Inspector's role as the official debugging tool | §11 | Verify against the MCP docs |
| D7 | Tool-poisoning / rug-pull research attributions and the "untrusted input + sensitive write" risk framing | §8.3–8.4 | Verify before attributing to named researchers |
| D8 | Kong, Docker MCP Gateway, IBM ContextForge as MCP gateway options | §11 | Verify |
