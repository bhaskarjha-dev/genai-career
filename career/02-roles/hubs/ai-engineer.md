---
id: roles.hub.ai-engineer
title: "AI Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "AI Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-48, T0-01, T0-02, T0-03, T0-06, T0-11, T0-14, T0-17, T0-23]
roles: [ai-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# AI Engineer

> Builds LLM-powered product features: API orchestration, retrieval (RAG), agents, evaluation and deployment. The title is a broad umbrella that also covers non-GenAI variants.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Applied AI Engineering | L5 Orchestration and context; also L6 Applications and deployment; planes: Evaluation and quality | Established (E) | #1 of 24 | #2 of 24 · band S · Monte Carlo rank 2 (P10–P90 1–3) | A1 Builder |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 10 (9–10) | B | JobsPipe 3,944 global / 1,697 US / 398 India (re-checked 2026-11-13; static vs 2026-10-19 refresh caveat); Fast AI Jobs 352 open roles at 188 AI startups (2026-11-12, up from 326; 64% of newest 50 rows customer-facing); LinkedIn Jobs on the Rise 2026 #1 [T0-01, T0-24, T0-48, T0-70]. |
| Pay | 6.5 (5.75–7.25) | B | Levels.fyi US AI Engineer TC P25 $110K / P50 $155K / P75 $212K / P90 $280K (0.54–0.56x US ML; SF Bay P50 $225K / P90 $460K; 2026-11-11); Axial US AI engineering posted base ceilings $170K–$270K (senior $213K, n=43,480; 5–12% below ML); AI/ML LCA floor $169K (n=4,459); Google within-employer check shows 62–69% of log gap is employer/level mix [T0-44, T0-48]. |
| Durability | 6 (4.5–7.5) | D | Judgement. Title persists and leads growth, but the table-stakes layer (SDK calls, naive RAG, prompting) is commoditised [T0-03 6.4 Tier 1]; evals, agent reliability and cost engineering keep value [T0-03 Tier 2]. |
| Leverage | 7.5 (6.5–8.5) | D | Judgement. Ships the revenue-facing AI features; enterprise and services employer mix [T0-01 F2]. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 10 (9–10) | B | JobsPipe India 398 of 3,944 global (10.1% M — correcting Phase 0 13.6% erratum; static 2026-11-13 check; consulting-heavy coverage artefact); Indian boards show 10,953–55,203 GenAI/AI keyword listings; Naukri JobSpeak AI/ML YoY +20% to +49% across 2026 [T0-25, T0-48, T0-69]. |
| India pay | 5.25 (4.5–6.25) | B | Levels.fyi Greater Bengaluru AI Engineer TC (2026-11-12): P25 Rs13.8L / P50 Rs20.0L (variants Rs18.3L–Rs20.5L) / P75 Rs39.7L / P90 Rs60.6L; GCC 0–2 yr fixed Rs13.2L, senior Rs58–60L (C) [T0-45]. |

India rank (CCI with India inputs): #1 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ● 9 | ● 7.5 | ● 8 | ○ 2 | ◐ 7 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), LLM APIs & tool calling, Agents & tool use, RAG.
- **Important (headline):** LLM evaluation (golden sets, calibrated judges, CI gates), Retrieval quality (hybrid, reranking, recall@k), Agent reliability (durable state, budgets, approvals), Cost & latency engineering, Observability (OpenTelemetry traces, metrics), LLM security (prompt injection, OWASP), Prompt & context design, ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search.
- **Full inventory:** 149 skills (Must 4 · Important 20 · Should 60 · Optional 64 · Avoid 1), each with its evidence and posting keywords: [ai-engineer.md](../../03-skills-and-tech/inventories/ai-engineer.md).
- **Prerequisites:** No formal gate. JD labels: senior 24.6%, entry 7.0%; T0-03 "Senior AI Engineer" cut assumes 5+ years [B]. About 72% of US AI-engineering postings state a degree [C · T0-06] and 75% of 903 Glassdoor US postings mention one (24% bachelor's, 24% master's, 28% PhD; "mention", not "require") [C · T0-23], while nearly 25% of AI postings in Atlanta Fed Lightcast data list no education requirement [A · T0-23]
- **Credentials (tie-breakers, not skills):** AWS Certified Generative AI Developer – Professional (AIP-C01) (Optional: tie-breaker, mostly in services and GCC channels); Microsoft AI-103 (Azure AI apps and agents) (Optional: Azure shops; replaces AI-102 (retired 2026-06-30); status provisional pending T0-28); Databricks Certified Generative AI Engineer Associate (Optional: only if the team runs Databricks); AWS Certified Machine Learning – Specialty (Avoid: retired 2026-03-31); Microsoft Azure AI Engineer Associate (AI-102) (Avoid: retired 2026-06-30); LangChain Certified Agent Engineer (LCAE) (Optional: ); Model Context Protocol Associate (MCPA) (Optional: ). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** An evaluated end-to-end system over a real corpus (metrics table, cost/latency budget, reproducible README); for T2–T3, a second system with a different failure surface plus CI-gated evals, traces, a load test and a postmortem
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (68%); [P2 Reliable agent: approvals, sandboxed tools, replay, failure injection](../../05-portfolio/project-archetypes.md#p2) (50%); [P20 Responsible-AI compliance packet with runtime guardrails](../../05-portfolio/project-archetypes.md#p20) (32%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Application.** It tests Coding, RAG or agent system design, and evaluation (plus an emerging AI-assisted build variant at AI-native firms such as Sierra, OpenAI and Anthropic). Source: T0-14, T0-46, T0-53, T0-57.
- **Practise:** the [application prep pack](../../08-interviewing/prep-packs.md#application-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** A1 Builder (Applied GenAI Engineering); headline pattern: "AI Engineer: LLM systems, RAG, agents, evaluation". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** Python (78.4%), LLM (76.7%), agentic AI (59.3%), RAG (54.0%), machine learning (39.8%), generative AI (37.6%), AWS / Azure (35.1% each), CI/CD (34.4%), vector databases (32.6%), prompt engineering (31.1%)
- **Leave out or reframe:** Wrapper-only demos; framework-syntax mastery as a headline; new RAGAS dependencies; "Prompt Engineer" as your title
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ai-engineer).

## Specialisations inside this role

- **RAG and retrieval** (L5 Orchestration and context): Candidate title: Retrieval / Search Engineer (LLM), role catalog §5.3.
- **Graph RAG and knowledge graphs** (L5 Orchestration and context): No title of its own in the catalog.
- **Document parsing and multimodal ingestion** (L5 Orchestration and context): No title of its own in the catalog.
- **Vector search infrastructure** (L5 Orchestration and context): Candidate title: Vector Search & Retrieval Systems Engineer, role catalog §5.3.
- **Context engineering** (L5 Orchestration and context): Quarantined title on the watchlist (Context Engineer), role catalog §5.1 and §5.4.
- **Coding agents** (L5 Orchestration and context): No title of its own in the catalog.
- **Voice and conversational agents** (L6 Applications and deployment): Candidate title: Conversational & Voice AI Engineer, role catalog §5.3.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Applied AI Engineer](applied-ai-engineer.md) (0.62); [Agentic AI Engineer](agentic-ai-engineer.md) (0.50); [Forward Deployed Engineer](forward-deployed-engineer.md) (0.40).
- **Same family (Applied AI Engineering):** [Applied AI Engineer](applied-ai-engineer.md), [Agentic AI Engineer](agentic-ai-engineer.md), [AI Product Engineer (AI Frontend)](ai-product-engineer.md), [AI Enablement Engineer](ai-enablement-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ai-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ai-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (JobsPipe 2026-11-13; Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

Across the 14 full-text postings audited in the November 2026 dossier (as of 2026-11-13), AI Engineer work is application-layer software engineering around foundation models: LLM API integration (14/14), retrieval-augmented generation (12/14), evaluation harnesses (12/14), and tool-calling agents (11/14) [M · T0-48 L73]. Employers explicitly draw the boundary against model research on one side and thin prompt wrappers on the other: Indicium specifies "building reliable, scalable applications rather than model training or research", and GR8_TECH states "Not research. Not prompt-only." [A · T0-48 L140, L356]. Post-training and custom inference serving rarely appear in core AI Engineer duties [B/M · T0-48 L356].

In practice, the umbrella title covers four distinct day-to-day topologies in the full-text sample [A/B · T0-48 L131–L138]:

| Operating variant | Share of full reads (n = 14) | Typical deliverables and team topology |
|---|---|---|
| **Product-embedded LLM engineer** (OfferUp, Spektr, Showpad, Vercel, Microsoft, Guardz, GR8_TECH) | 7/14 | Owns user-facing RAG, assistant, or agent features inside a product engineering squad, with offline/online evaluation, observability, latency/cost budgets, and production incident ownership [A/B · T0-48 L135, L311] |
| **Consultancy delivery** (Robots & Pencils, Indicium, Talentica) | 3/14 | Builds client-facing LLM pipelines and knowledge-graph/document-ingestion systems across varied cloud stacks [A · T0-48 L136, L251–L252] |
| **Enterprise platform and internal automation** (Dun & Bradstreet ×2, Celonis) | 3/14 | Builds internal workflows, analytics/data-platform integrations, or marketing-ops agents; some enterprise roles mix LangChain with low-code tools such as Make and Zapier [A · T0-48 L137, L244, L602] |
| **Lab customer-facing builder** (Mistral Prototyping) | 1/14 | Rapidly builds customer prototypes and deployments beside go-to-market teams to unlock deals and follow-on revenue [A · T0-48 L138, L352] |

**Language and stack nuance.** Python is near-universal (12/14 full reads; 78.4% on JobsPipe as counted 2026-09-10), but not universal [B/M · T0-48 L73, L225]. TypeScript/JavaScript appears in 5/14 full reads: Showpad is TypeScript-led without Python, Spektr asks for "TypeScript and/or Python", Celonis accepts JavaScript as an alternative, and Vercel requires both [A · T0-48 L97, L240, L564–L565]. Orchestration frameworks (LangChain, LangGraph, or equivalent) appear in 10/14 full reads mostly as interchangeable examples, and MCP/A2A protocols appear in 4/14 (required at GR8_TECH; preferred at D&B Dublin, Microsoft, and Guardz) [A/M · T0-48 L241, L243].

**Mid-level versus senior and staff scope.** Mid-level postings (typically 2–4 years) focus on implementing RAG pipelines, structured outputs, and bounded tool-calling workflows inside an existing architecture [A · T0-48 L566, L569]. Senior, Staff, Lead, and Principal roles shift towards owning the end-to-end AI roadmap (Spektr), designing shared evaluation and observability practices, managing cost/latency and production incidents, and tying system metrics to business KPIs (OfferUp) [A · T0-48 L311, L350–L352]. At large enterprises and Big Tech (Workday Principal, Guardz), senior AI Engineer postings still screen for underlying ML fundamentals and PyTorch/TensorFlow fluency [A/B · T0-48 L95, L572, L601].

## Employer landscape and title confusion

Broad-market demand is enterprise- and services-heavy, whereas startup and lab demand is heavily customer-facing [B · T0-48 L72, L189]:

- **Broad market (JobsPipe, read 2026-11-13):** Live global volume remains 3,944 (1,697 US; 398 India), led globally by consultancies, banks, and IT-services firms — PwC (67), Capital One (34), TCS (31), Deloitte (31), Jack & Jill (25), Mastercard (20), Infosys (20), and Amex (19) [B · T0-48 L69, L189]. LinkedIn's Jobs on the Rise 2026 (2026-01-07) ranks AI Engineer #1 of 25 (median 3.7 years' experience; 26% remote, 27% hybrid), though LinkedIn pools AI engineers with ML engineers [B · T0-48 L71, L191].
- **AI startups (Fast AI Jobs, updated 2026-11-11):** 352 open roles across 188 startups (up from 326 at 183 on 2026-10-19; roughly +28% from 275 in an inferred August 2026 snapshot), with 44% at Pre-Seed to Series B [B/M · T0-48 L70, L183–L185].
- **Frontier labs almost never post the literal "AI Engineer" title:** Zero literal "AI Engineer" openings appeared on the first page of Anthropic's 670-job board (2026-11-13; COI), and OpenAI, Anthropic, and Mistral instead hire under [Applied AI Engineer](applied-ai-engineer.md) or [Forward Deployed Engineer](forward-deployed-engineer.md) [A/B · T0-48 L75, L162–L163].

**Title mix and false positives to screen out before applying:**

| Posting pattern | Evidence (November 2026) | How to read it |
|---|---|---|
| **Customer-facing startup rows under "AI Engineer"** | Of the 50 newest Fast AI Jobs "AI Engineer" rows (2026-11-02 to 2026-11-11), **42% (21/50)** are titled *Applied AI Engineer* and **22% (11/50)** are *Forward Deployed / Deployed*; only **26% (13/50)** are plain AI / Senior / Staff AI Engineer [B/M · T0-48 L72, L160–L165] | Search both plain and applied/FDE titles, then read the first responsibilities to check travel and customer-facing duties [P · T0-48 L90–L92] |
| **Off-role contamination in aggregators** | On JobsPipe, 5 of 56 sampled rows (9%) are clearly non-GenAI (*Site AI Engineer* in construction, *Power Platform & AI Engineer*, *Physical AI*) and up to 11 (20%) are ambiguous; Fast AI Jobs mixes in Figure AI robotics (*Helix AI Engineer*) and GTM AI Engineer [M · T0-48 L74, L165] | Filter by duties (LLM APIs + RAG/agents + evals), never by title string alone [P · T0-48 L90–L91] |
| **Title drift and internal level inflation** | Vercel job `5517523004` is titled "AI Engineer" on its careers URL and "Research Engineer" on Greenhouse; Dun & Bradstreet's Chennai "Senior Gen AI Engineer" (5–8 years) maps internally to "Senior Analyst" [A · T0-48 L83, L401, L561, L564] | Verify the internal band, reporting line, and job scope rather than trusting headline seniority [P] |
| **Closed listings in search indexes** | 7 of 21 employer ATS fetches (33%) redirected to the board index because the requisition had closed, and an expired April 2026 TIAA posting still surfaced in search [A/M · T0-48 L56, L83, L459] | Always open the employer's own Greenhouse/Lever/Ashby board to confirm liveness before tailoring an application [P · T0-48 L108] |

**Adjacent role boundaries:** Compared with [Machine Learning Engineer](ml-engineer.md), AI Engineer rarely trains models from scratch or runs large-scale ranking/recsys infrastructure [A/B · T0-48 L140, L356]. Compared with [Applied AI Engineer](applied-ai-engineer.md) and [Forward Deployed Engineer](forward-deployed-engineer.md), core product AI Engineers sit inside internal product squads rather than customer-delivery or go-to-market teams [A/B · T0-48 L135–L138].

## Career path, India demand and market signals

**Entry routes and prerequisites.** Across 21 postings stating minimum years, the median ask is **3 years** (range 0.5–10; senior postings often start at 3–5 years rather than a rigid 5+) [M · T0-48 L80, L337, L419]. Explicit entry-level openings remain thin — 1 of 42 sampled records and 275 of 3,944 (7.0%) on JobsPipe — and no full-read posting accepted a non-engineering transition [B/M · T0-48 L80, L177, L344–L345]. A degree was stated in only 5 of 14 full-text postings (below the broader 72% AI-engineering figure in T0-06) [M · T0-48 L80, L338]. Backend and full-stack software engineers match most directly; data scientists fit enterprise/ML-leaning variants (D&B, Workday, Guardz); frontend engineers fit TypeScript-heavy product teams (Vercel, Showpad, Spektr) [A/B · T0-48 L339–L343]. Progression runs AI Engineer II / L3 → Senior → Staff / Principal / Lead → Applied AI Engineering Manager, with lateral exits into FDE, Applied AI Engineer, or ML Engineer [A/B · T0-48 L350].

**Pay and channel dispersion.** Full percentile tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). The November 2026 dossier adds three role-specific pricing rules:
- **Employer and level mix explain most of the ML Engineer pay gap.** On Levels.fyi (updated 2026-11-12), US AI Engineer median total compensation is **$155K** (P25 $110K, P75 $211K, P90 $280K) against **$285,650** for ML Engineer — a **0.54×** market-wide ratio [B/M · T0-48 L77, L283–L288]. Inside Google, however, AI Engineer median total compensation is **$240K** (n = 38, 2026-10-19; L3 $196K, L5 $355K, L6 $583K) against roughly **$290K–$302K** for ML Engineer (ratio **0.79–0.83**, a +21–26% MLE premium), meaning **62–69% of the log market gap** reflects employer and level mix rather than the title alone [B/M · T0-48 L77, L270–L271, L289–L291].
- **US posted base dispersion is driven by hiring channel.** Across 18 pay-disclosing US postings (biased towards pay-transparent employers), median base midpoint is **$200.6K** (IQR $155K–$234K; senior+ median $231.5K, non-senior $195K) [M · T0-48 L76, L264–L266]. Staffing and IT-services postings pay starkly less for overlapping stacks — ApTask ($80K–$90K) and TCS Austin ($70K–$130K) versus OfferUp ($140K–$160K), Vercel ($192K–$288K), Scale AI ($216K–$270K), and Datadog Staff ($234K–$300K) [A/B · T0-48 L267, L389, L594].
- **Sponsorship is employer-specific.** Department of Labor H-1B LCA disclosures via careery.pro show 8,275 certified filings for the broader AI/ML engineer family (FY2025 to FY2026 Q3; 529 exact "AI ENGINEER"; median offered wage $165K rising to $169K; 46.6% in California — regulatory floors, not pay), yet individual postings explicitly restrict work authorisation (e.g., Microsoft Wellfound listing "Not Available", Inizio US citizen/green-card only, GR8_TECH B2B contractor engagement) [B · T0-48 L82, L362–L370]. Visa rules and contested H-1B fee status live in [visa and relocation](../../11-tracks/visa-and-relocation.md).

**India demand and hiring reality.** JobsPipe records **398 live India postings** on 2026-11-13, which is **10.1%** of the 3,944 global total (correcting the earlier 13.6% share in Phase 0) [B/M · T0-48 L69, L175–L176, L411]. Top measured India employers on JobsPipe are Teradata (9), Infosys (6), TCS (5), HCLTech (4), Barclays (4), and Target (4), with **Gen AI Engineer** (Infosys, Fractal, Talentica, D&B Chennai), **Applied AI Engineer** (Celonis Bangalore), and **Staff Cloud AI Engineer** (Teradata) as recurring aliases [B · T0-48 L190, L396–L397]. Broad-market India pay centres on **₹9L–₹25L** (Flexiple Bengaluru GenAI Engineer median ₹9.2L, n = 59, Aug 2026; Flexiple senior 6+ years ₹21.6L; AIM Research ₹12–15 LPA; Levels.fyi single-employer WCG Bengaluru ₹24.0L), while none of the four full-read India postings disclosed a salary band [B/C · T0-48 L78, L274–L278, L398]. Candidates in India should watch for **pedigree gates** (Talentica explicitly restricts to IIT, NIT, BITS, VJTI, COEP, and IIIT-H) and title-versus-grade compression (D&B Chennai's 5–8-year "Senior Gen AI Engineer" graded internally as Senior Analyst) [A · T0-48 L400–L401].

**Credentials update.** Zero of 14 full-text postings named a certification [M · T0-48 L79, L322]. AWS ML Specialty (MLS-C01, last exam 2026-03-31) and Microsoft AI-102 (retired 2026-06-30) are retired [B · T0-48 L327–L328; A · T0-11 L165–L167]. AWS AIP-C01 is active, Databricks Certified Generative AI Engineer Associate updated its blueprint on 2026-03-18 (45 scored items, 90 minutes, $200, 2-year validity; covers Agent Bricks, MCP servers, guardrails, and MLflow tracing) [A · T0-48 L79, L330], and Microsoft AI-103 reached general availability in June 2026 (live-verified on Microsoft Learn on 2026-11-19, resolving the beta-versus-GA extract conflict in T0-48 L329). Keep certifications strictly optional unless targeting an AWS/Azure services channel or a Databricks shop; see [credential ROI](../../04-certifications/credential-roi.md).

## Interview themes and preparation notes

Employer-published interview specifications remain sparse: Spektr publishes a compact three-stage loop (30-minute talent intro, 30-minute technical, 60-minute technical) [A · T0-48 L81, L297]. Across third-party hiring blogs and candidate syntheses (Grade C), AI Engineer loops concentrate on four recurring signals [C · T0-48 L81, L298–L302]:

1. **Evaluation-design take-homes (3–5 hours) or live builds:** Designing a rubric, golden set, and regression check for a non-deterministic workflow rather than building an unmeasured chatbot [C · T0-48 L299].
2. **RAG architecture and failure-mode deep dives:** Chunking, embedding/reranking trade-offs, latency and cost budgets, and diagnosing retrieval versus generation errors [C · T0-48 L299].
3. **Agent loop control and safety:** Explaining termination conditions, step budgets, and tool-failure handling — e.g., drawing a shipped agent and marking every place it could loop indefinitely [C · T0-48 L300, L302].
4. **AI-usage policy compliance:** Check every employer's written rules before using coding assistants. Anthropic's Greenhouse application explicitly links an AI-usage policy and asks applicants to confirm non-AI-assisted evaluation on communication (B, COI; full rules live-verified 2026-11-19) [B · T0-48 L81, L298].

**Calibration note on the Application track.** While RAG, agent loops, and evaluation architecture are corroborated, neither "context management" nor "RAG with access control" appeared in sampled interview reports (per-user data permissions appeared only in a Databricks certification sample question) [A/C · T0-48 L302, L433].

**Proof of work and common rejection signals.** Postings explicitly reward "shipped, not demoed" systems (NinjaTrader), "Evaluation Obsession" (Spektr), production incident ownership (GR8_TECH), and deep knowledge of LLM failure modes (Indicium); Mistral lists hackathons and open-source LLM contributions as nice-to-have [A/B · T0-48 L306–L312]. Hiring-side blogs flag tutorial/wrapper demos, framework-syntax headlines, certificate-led résumés, and inability to discuss a real production failure you owned [C · T0-48 L313–L317, L332, L375]. For structured practice prompts (without model answers), use the [application prep pack](../../08-interviewing/prep-packs.md#application-pack) and [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## Dossier evidence and limits

- **Primary dossier:** [T0-48](../../../research/sessions/T0-48-role-dossier-ai-engineer.md) (retrieved 2026-11-13; 72 sources: 23 Read, 49 Extract-only; 42 JD records, of which 14 are full-text reads used for skill shares and 28 are thin mirror/aggregator records) [T0-48 L51–L52, L481–L554].
- **Sampling and statistical limits:** Skill shares rest on n = 14 full-text postings (**±26 percentage points** margin of error) and are **upwardly biased by query terms** ("RAG", "agents", "evaluation", "LLM"), so they act only as directional cross-checks against platform shares (JobsPipe JD shares were counted on 2026-09-10) and do not justify standalone tier changes [M · T0-48 L52–L55, L83]. Google, Amazon, Meta, Apple, and NVIDIA direct career boards were not reached; no non-English searches were run [T0-48 L57, L430–L431].
- **Epistemic downgrades and COI applied:** Seven Extract-only ledger rows graded A in T0-48 (`S21`–`S24`, `S48`, `S51`, `S68`) are treated as Grade B (with AI-103 general availability independently verified on Microsoft Learn on 2026-11-19). Because T0-48 was authored by Claude Sonnet 5.5 (Anthropic), Anthropic's posting (`S47`) and Claude-mentioning postings (`S34`, `S65`, `S42`) carry a COI flag, as does LinkedIn's Davos press release (`S7`) [T0-48 L13, L466].
- **What would change this view:** A query-neutral full-text sample (n ≥ 60) establishing unbiased evaluation and MCP shares; direct employer-board reads from Big Tech and Indian GCCs; and live posted pay bands for India roles [T0-48 L111–L114, L443].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
