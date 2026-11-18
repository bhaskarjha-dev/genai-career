---
id: "T0-53"
title: "Role Dossier: Applied AI Engineer"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-applied-ai-engineer"
tags: ["applied-ai-engineer", "role-dossier", "job-postings", "forward-deployed", "pay", "india"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic) in claude.ai with web search and fetch. COI: Anthropic's own postings and candidate-guidance page are in the evidence and are marked COI."
evidence_window: "2024-05 to 2026-11-13 (items dated before 2025-01-01 are flagged where used)"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-53: Role Dossier: Applied AI Engineer

S-numbers (S1 onwards) point to rows in the Sources & Evidence Ledger. Grades follow the protocol: A is an employer's or issuer's own page that I opened; B is platform, aggregator or search-extract evidence; C is third-party analysis; D is memory, a single anecdote or judgement; M is my own calculation and inherits its weakest input; P is practice-curated. The brief anchors on 2026-11-11, so the 90-day posting window opens on 2026-08-13. I retrieved every source on 2026-11-13, which is also the "seen" date on every record. Freshness classes (V1 to V5) are on each data record.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | At labs and AI vendors the title means customer-embedded delivery (scoping, evaluation, production hand-off), not research. | 0.8 | D |
| P2 | Python appears in at least 75% of postings and RAG in at least 50%. | 0.6 | D |
| P3 | Posted US lab base ranges sit between $180K and $350K. | 0.7 | D |
| P4 | Lab postings ask for 3–5 years of experience; a bachelor's degree or equivalent suffices. | 0.7 | D |
| P5 | Lab pay for India-based Applied AI Engineer roles is not posted in INR. | 0.7 | D |
| P6 | The title is stable across employers. | 0.5 | D |

## Research Question

**Decision question.** What should the knowledge base say about what an Applied AI Engineer does, how much demand and pay the role carries, which skills, proof and credentials it needs, how candidates are interviewed, how careers progress, and where the jobs are? The answer feeds `role_scores.json`, `skills_ontology.json`, `role_titles.json` and `role-catalog.md`.

**Sub-questions.** Variants and aliases (item 1). Demand (2). Job-description sample (3). Skills (4). Pay (5). Loop (6). Proof (7). Credentials (8). Routes and prerequisites (9). Progression, durability, leverage (10). Footprint (11). Geography and sponsorship (12). Résumé signals (13). Misconceptions (14). India (15). Probes: how these postings differ from AI Engineer postings, and measured volume and pay.

**Scope as applied.**
- I treated the exact title "Applied AI Engineer", plus "Partner", "Architect" and Applied-AI-team variants, as in scope.
- I excluded two roles because of what they ask for: JPMorgan's "Applied AI ML Associate/Lead" posts (ML engineering and data science) and OpenAI's "Applied AI Engineer, Codex Core Agent" (product model-improvement engineering).
- A posting counts if I opened it live on 2026-11-13 or a listing dated it on or after 2026-08-13. Five further postings were search-indexed but undated and are flagged.
- Managers, directors and heads appear only as ladder evidence.

**Method.**
- Web searches against employers' own boards (Greenhouse, Lever, Ashby, openai.com/careers, Siemens, Google, Atomicwork).
- The Fast AI Jobs "AI Engineer" listing (352 rows, updated 2026-11-11), whose rows link to employers' ATS pages.
- Levels.fyi, JobsPipe, aggregators of Department of Labor LCA data, interview-prep pages, India pay pages, demand reports, the AWS exam guide, and Anthropic's candidate AI guidance page.
- Sample: 36 included postings, of which 10 were read in full, 8 as search extracts with body text and 18 as listing metadata only. Skill shares use only the 10 full reads.
- OpenAI's site and some Greenhouse boards refused automated fetches, so OpenAI rows rest on extracts.

**Falsification searches (disconfirming results documented).**
1. A JobsPipe page for Applied AI Engineer: none exists, and the knowledge base's shares match JobsPipe's "AI Engineer" page.
2. Liveness of search-indexed postings: 4 of 14 fetched were closed, including Google Cloud's FDE IV, Applied AI posting on 2026-11-13.
3. India INR pay for the title: none posted; proxies only.
4. LCA filings under the exact title at OpenAI or Anthropic: none found.
5. Role-specific interview evidence at Scale, Google Cloud and Indian GCCs: none found.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | The title is a family. At OpenAI, Anthropic, Mistral and Scale it names post-sales build-and-advise work for customers: scoping, prototypes, evaluation suites, workshops, product feedback. Sibling titles split pre-sales (Architect), ecosystem partners (Partner) and embedded delivery (FDE). At NVIDIA, Siemens, Atomicwork and Deloitte India the same title names internal or product AI engineering, and JPMorgan's "Applied AI ML" titles are ML engineering. | Ten bodies read in full; OpenAI Partner variants; Siemens and NVIDIA bodies [S1–S4, S7, S8, S11, S15, S17, S18, S24, S26, S50] | A/B |
| KF2 | Exact-title volume can be measured only at AI startups and labs. Fast AI Jobs lists 352 open AI Engineer rows (2026-11-11). Of the newest 50, 21 carry "Applied AI Engineer" in the title (9 employers; OpenAI 6, Scale 4) and 11 more are FDE or "Deployed AI Engineer" titles. No row is entry-level. | [S13] | B/M |
| KF3 | The knowledge base's skill shares (Python 78.4%, LLM 76.7%, agentic 59.3%, RAG 54.0%, ML 39.8%) are JobsPipe's "AI Engineer" page shares, not Applied AI Engineer shares. | [S21] | B |
| KF4 | In 10 postings read in full: Python 9, agents 9, customer scoping 9, evaluation 8, technical communication 7, LLM API 5, RAG 5 (none of Anthropic's four), ML fundamentals 5, cloud 3, vector search 3, guardrails 1, git/CI 1, retrieval quality 0. Uncertainty is about ±31 pp at p = 0.5. | [S1–S4, S7, S8, S11, S15, S17, S50] | M |
| KF5 | Levels.fyi gives a US median total compensation of $250K for the title (p25 $200K, p75 $475K, p90 $505K) as of 2026-11-11. Posted US lab ranges run $197K–$320K and London £225K–£240K, and some are OTE. Exact-title LCA offered wages have a median of $185,480 (n=6; offered, not paid). | [S19, S1–S4, S18, S40] | B/A/M |
| KF6 | Stated minimum experience is 2–4 years (median 3, n=8). A bachelor's degree or equivalent is stated in 7 of 10 reads, no degree requirement in 1, none stated in 1, and a PhD or master's is required in 1 (Mistral Palo Alto). None of the 36 sampled titles is entry-level; JobsPipe finds AI-titled roles are 16.4% entry level against 38.3% of all postings. | [S1–S4, S7, S8, S11, S15, S17, S50, S22] | M/B |
| KF7 | Demand growth is strong at the FDE-family level. Indeed US FDE postings went from 643 to 5,330 (Apr 2025 to Apr 2026); Lightcast reports above 1,000% year on year for Jan–Aug 2026; India FDE postings rose nearly 19× (Jun 2025 to Jun 2026) and moderated after the June peak. | [S29–S32] | B/C |
| KF8 | India: OpenAI posts Applied AI Engineer, Architect and Partner-AWS roles in Delhi, Mumbai and Bangalore (hybrid, 3 days in office, relocation assistance). Siemens Bangalore asks 3–5 years; Deloitte India and Hitachi Energy post the title. No INR range for lab roles was found; pay evidence is proxies only. | [S17, S18, S27, S28, S43, S44, S52] | B/C/D |
| KF9 | Titles and listings are unstable. Scale's "Applied AI Engineer, Enterprise" page now carries the title "Frontier Agents Engineer". OpenAI runs "AI Deployment Engineer" and "Applied AI Engineer" with near-identical team text. 4 of 14 fetched search-indexed postings were closed. | [S11, S18, S49, S5, S9, S23, S25] | A/M |
| KF10 | Interview evidence is mostly C-grade prep-vendor material. Anthropic's own policy (A, COI) says drafts are yours first, take-homes are without Claude unless indicated, and live interviews allow no AI unless indicated. Reports describe a build or take-home, system design and a customer-conversation round; Mistral reports show about five rounds including coding and customer success. | [S36, S34, S35, S37, S38, S51] | A/C/D |
| KF11 | Anthropic's four postings say it sponsors visas (not for every role). Mistral Palo Alto lists visa sponsorship. Exact-title LCAs are rare (six found). | [S1–S4, S8, S40] | A/B |
| KF12 | The posted ladder runs engineer, senior or staff, lead or technical lead, manager (7+ years at Anthropic, 8+ at OpenAI), then director or head. Success wording ties to production adoption and revenue follow-on. | [S6, S7, S10, S12, S16, S18] | A/B |
| KF13 | No posting read in full names a certification. The AWS Generative AI Developer – Professional (AIP-C01) is an active professional exam (65 scored plus 10 unscored questions, pass mark 750 of 1,000, target candidate with 2+ years building production applications); it is optional for this role. | [S45, S46] | A/C |
| KF14 | Variants differ by employer type. RAG, vector search, fine-tuning and named frameworks appear in 5 of 6 non-Anthropic reads and in none of Anthropic's four, which emphasise context engineering, evaluation, MCP, technical content and safety. | [S1–S4, S7, S8, S11, S15, S17, S50] | M |

## Recommendation

| Rule | Decision | Failure mode |
|---|---|---|
| R1 (about 3–6 years as a software, forward-deployed or solutions engineer or technical founder, with production LLM work that includes evaluation) | Apply first to lab and AI-vendor Applied AI Engineer postings. Lead with customer-facing delivery and an evaluation suite. | Hybrid office minimums (25% at Anthropic, 3 days at OpenAI India), travel (up to 25% at Snorkel) and pre-sales duties may not fit. Some ranges are OTE. |
| R2 (any level) | Search the family, not the title: AI Deployment Engineer, Forward Deployed (AI or ML) Engineer, Applied AI Architect, Partner Applied AI Engineer, Frontier Agents Engineer, Deployed AI Engineer. Confirm the posting is open on the employer's own board. | Title collisions (JPMorgan "Applied AI ML", OpenAI's "Applied AI Engineering" organisation, internal variants at NVIDIA, Siemens, Atomicwork) waste applications. Closed listings are common (4 of 14 fetched). |
| R3 (proof) | Build an evaluation suite plus a reference agent implementation for a realistic customer workflow, with a short write-up. Add an MCP server or a cookbook-style contribution where relevant. | No outcome data ranks proof types (P grade). Demos with no external users are the failure the knowledge base already names. |
| R4 (under about 2–3 years) | Target enterprise, consultancy or GCC "Applied AI Engineer" roles, or AI Engineer routes. Treat lab roles as a stretch that needs unusual proof. | Level labels can conflict with years (Siemens tags the role entry level but asks 3–5 years). None of 36 titles is entry level. |
| R5 (India) | Target OpenAI's Delhi, Mumbai and Bangalore postings, GCC and enterprise variants, and Google-style Applied AI FDE roles when open. Ask for the INR range at the first call. | INR figures found are estimates (D/E). Hybrid and relocation terms apply. |
| R6 (staff and above, 7+ years) | Look for Staff, Lead and Technical Lead variants (Mistral Lead asks 7–10+ years; Scale and Snorkel post Staff roles) before manager roles. | Manager postings ask for team-building and revenue accountability, which is a different job, and there are few of them. |
| R7 (credentials) | Do not buy a certificate for this role unless the target is a services firm that asks for one. | Services and consulting employers are thinly sampled and may screen on certificates. |

**What would change these rules.**
- A larger enterprise, consultancy and GCC sample read separately.
- Posted INR ranges for lab roles.
- Evidence that the FDE-family surge is fading (Indeed India already shows moderation after June 2026).
- Employers consolidating titles, as Scale's rename suggests.

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| A1. One role card with variant tags (customer-facing, pre-sales, partner, internal, ML-collision) | Preferred | Matches how the evidence splits and keeps one page for job seekers. |
| A2. Split into "customer-facing Applied AI Engineer" and "internal applied AI engineer" | Deferred | Bodies for 26 of 36 postings were not read in full, so variant shares are weak. |
| A3. Merge into an FDE family | Rejected for now | Anthropic and Mistral keep Applied AI Engineer distinct from FDE. Report demand at family level instead. |
| A4. Treat as an alias of AI Engineer | Rejected | Skill patterns differ by employer type, and labs post no "AI Engineer" title in my searches. |
| A5. Wait for a larger sample | Rejected | The door is two-way. Interim records are graded and dated. |

## Detailed Findings

### DF1 Definition, variants and aliases (items 1, 14)

At labs and AI vendors the title describes post-sales, build-and-advise work: scoping with a customer, prototypes, evaluation suites, workshops and product feedback, usually alongside account executives [S1, S2, S7, S8, S18]. Mistral's Prototyping team describes itself as the technical pre-sales arm of go-to-market [S7]. Anthropic separates Applied AI Engineer (4+ years) from Applied AI Architect (3+ years, pre-sales, "founder-led sales" or sales-engineering background) [S1–S4]. OpenAI's "Applied AI Engineer, Partner" postings serve cloud and ISV partners [S13].

| Variant (classified by what the posting asks for) | Examples | n of 36 |
|---|---|---|
| Customer-facing build and advise (post-sales or embedded) | OpenAI Enterprise, API Platform, Digital Natives, Large Enterprise, HLS, Delhi, Cyber; Anthropic Enterprise, London, Life Sciences; Mistral ×3; Scale ×4; Snorkel ×2; AssemblyAI ×2; Concurrence | 22 |
| Partner ecosystem | OpenAI Partner (Google Cloud; Oracle and Cloud ISV; AWS) | 3 |
| Pre-sales or architect | Anthropic Architect, Startups; Snorkel Staff Pre-Sales | 2 |
| Research engineer inside an Applied AI team | Anthropic Applied AI, Research Engineer | 1 |
| Internal or product build | NVIDIA, Siemens, Atomicwork, Deloitte India | 4 |
| Undetermined (listing metadata only) | Pika, Crusoe, General Matter, Flexport | 4 |

Ten of the 22 customer-facing rows are classified from title and listing text only. Thirty-two of the 36 titles contain "Applied AI Engineer", but I searched by that title, so this is not a measurement.

**Aliases and neighbours seen (2026-11-13).**
- AI Deployment Engineer (OpenAI), a parallel title whose team text is near-identical to the Applied AI Engineer text [S18, S49].
- Frontier Agents Engineer and Senior Frontier Agents Engineer (Applied AI) (Scale) [S11, S12].
- Forward Deployed Machine Learning Engineer and Technical Lead, Forward Deployed (Mistral) [S9].
- Deployed AI Engineer (Helsing, listed 2026-11-11); Forward Deployed AI Engineer (Turing, Avathon, Toloka); AI Engineer – FDE (Databricks) [S13].
- Partner Applied AI Engineer (OpenAI, listed 2026-11-11) [S13].
- Applied AI Architect (Anthropic) [S4].
- Member of Applied AI – Architect (DevRev, Bangalore, listed 2026-06-04) and Senior Staff Applied AI Engineer – Context Retrieval (Databricks, listed 2026-07-24) [S14].
- Title collisions: JPMorgan "Applied AI ML Associate/Lead" [S26]; OpenAI's "Applied AI Engineering" organisation, which holds ordinary product-engineering roles [S14].

**Boundary with AI Engineer.** Secondary sources report that OpenAI and Anthropic post no "AI Engineer" title [S39]; I found none in my searches. The difference is therefore partly employer type. JobsPipe's AI Engineer shares describe a broader population (any employer), whereas the lab postings above describe customer-facing delivery [S21].

### DF2 Demand (items 2, 12)

| Metric | Value | Source | Date | Grade |
|---|---|---|---|---|
| AI Engineer category, open roles at AI startups | 352 across 188 startups | S13 | 2026-11-11 | B |
| Same page, earlier snapshot | 275 across 170 startups (newest row 2026-07-30) | S14 | about 2026-07-31 | B |
| Change between the two snapshots | +28% (352 / 275) | S13, S14 | n/a | M |
| First 50 rows: "Applied AI Engineer" in the title | 21 of 50 (42%); OpenAI 6, Scale 4, Snorkel 2, AssemblyAI 2, Flexport 2, Concurrence 2, General Matter 1, Pika 1, Crusoe 1 | S13 | 2026-11-11 | M |
| First 50 rows: FDE or Deployed AI Engineer titles | 11 of 50 (22%) | S13 | 2026-11-11 | M |
| Title level among those 21 | Staff 6 (one "Senior/Staff"), senior 4, unqualified 11, entry 0 | S13 | 2026-11-11 | M |
| OpenAI distinct "Applied AI Engineer" or "Partner Applied AI Engineer" titles seen (lower bound, not a census; liveness unverified outside the 2026-11-02 to 2026-11-11 listing) | at least 20 | S13, S18 | 2026-11-13 | M |
| Anthropic careers board, all roles | 670 jobs | S5 | 2026-11-13 | A |
| Anthropic Applied AI openings | about 20 in early August 2026 (single source) | S33 | 2026-08 | C |
| FDE-family postings, Indeed US | 643 (Apr 2025) to 5,330 (Apr 2026) | S31 | 2026-04 | C |
| FDE postings, Lightcast | above 1,000% year on year, Jan–Aug 2026 | S30 | 2026-09-03 | B |
| FDE postings, India (Indeed) | nearly 19× Jun 2025 to Jun 2026, then moderating | S29 | 2026-10-14 | B |
| FDE-type roles including "Applied AI Engineer" titles (LinkUp) | about 300 to over 5,000 in a year | S32 | n/s | C |

- **Not obtainable:** LinkedIn, Indeed and Glassdoor exact-title counts (login and bot walls) and any US, India or Europe split by exact title. Aggregator "Applied AI Engineering" category counts (about 3,400 at Inference Jobs) are keyword expansions and are not title counts [S49].
- **Employer mix (sample, n = 36):** frontier labs 18, AI startups 14, Big Tech 1, enterprise 1, GCC 1, IT services 1.
- **Seniority mix (title wording, n = 36):** staff or lead 7, senior 2, unqualified 27, entry 0.
- **Remote share:** 3 of 13 postings with a visible work mode offer a remote option (Snorkel; OpenAI Enterprise; OpenAI Partner-AWS Bangalore); none is fully remote worldwide. JobsPipe's remote flag on AI Engineer postings is 11.0% [S21].

### DF3 Sample summary (item 3)

| Dimension | Breakdown |
|---|---|
| Employer type | frontier-lab 18 (Anthropic 5, OpenAI 10, Mistral 3); ai-startup 14 (Scale 4, Snorkel 3, AssemblyAI 2, Concurrence, Pika, Crusoe, General Matter, Atomicwork 1 each); big-tech 1 (NVIDIA); enterprise 1 (Flexport); gcc 1 (Siemens Technology and Services); it-services 1 (Deloitte India) |
| Region | US 20; UK 5; Europe outside UK 2; India 4; APAC 1 (Seoul); Middle East and Israel 2; multiple or unspecified 2 |
| Evidence depth | Read in full 10; search extract with body text 8; listing metadata only 18 |
| Liveness | Verified live by fetch 10; dated 2026-08-13 or later 21; search-indexed but undated 5 (OpenAI Enterprise, API Platform, Delhi, Partner-AWS, Cyber-Government) |

**Excluded (16 seen).**

| Reason | Postings |
|---|---|
| Not this role (2) | JPMorgan Applied AI ML Lead (ML engineering) [S26]; OpenAI Applied AI Engineer, Codex Core Agent [S18] |
| Closed when fetched on 2026-11-13 (4) | EY London Consultant – Applied AI Engineer (dated 2026-04-09) [S25]; Anthropic Applied AI Engineer, Startups 5073277008 [S5]; Mistral Fullstack EMEA [S9]; Google Cloud Forward Deployed Engineer IV, Applied AI [S23] |
| Outside the window or unverified (10) | Hitachi Energy (2026-05-05) [S28]; Cohere ×3 (January 2026 listings) [S14, S48]; Titan AI (2026-05-28) and Apple (2026-05-13) [S48]; Google Senior Agent Engineer (2026-07-24) [S48]; Databricks Senior Staff Context Retrieval (2026-07-24) [S14]; OpenAI GTM Growth Engineering (2026-07-25) [S18]; Anthropic Beneficial Deployments 5068226008 (updated 2026-05-20) [S6] |

**Biases.**
- Search engines and the Fast AI Jobs listing over-represent labs and AI vendors (32 of 36) and English-language postings on Greenhouse, Ashby and Lever. Enterprise, consultancy and GCC rows number 4 of 36, below the target spread.
- Fast AI Jobs' newest 50 rows over-represent bulk posters (OpenAI and Scale supply 10 of the 21 exact-title rows).
- I ran no non-English searches.
- Skill shares rest on 10 full reads.

### DF4 Skills (item 4)

Shares are k of n = 10 postings read in full (Anthropic ×4, Mistral ×2, Scale, Snorkel, Siemens, Atomicwork). Uncertainty is about ±31 pp at p = 0.5. They are a cross-check on platform shares, not a measurement. "KB tier" is the knowledge base's current tier.

| Skill [ID] | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| Python [python] | 9 (90%) | 10 | Must | Must | Absent only in Anthropic Life Sciences text. |
| LLM APIs and tool calling [llm_apis] | 5 (50%) | 10 | Must | Must | Vendor API or platform named in 4, tool calling in 1; implied elsewhere. |
| RAG [rag] | 5 (50%) | 10 | Important (Must for vendor, startup and enterprise variants) | Must | Named in 5 of 6 non-Anthropic reads, in none of Anthropic's four. |
| Agents and tool use [agents] | 9 (90%) | 10 | Must | Must | Absent only in Anthropic Architect text. |
| Customer scoping and demos [customer_scoping] | 9 (90%) | 10 | Must | Important | Discovery or requirements language in every customer-facing read; absent only at Atomicwork. |
| LLM evaluation [evals] | 8 (80%) | 10 | Must | Important | Named in all four Anthropic texts, Mistral Palo Alto, Snorkel, Siemens, Atomicwork. |
| Guardrails [guardrails] | 1 (10%) | 10 | Should | Important | Siemens only. |
| Prompt and context design [prompt_context] | 4 (40%) | 10 | Important | Important | "Context engineering" at Anthropic ×3, plus Siemens. |
| Prompt engineering [prompt_engineering] | 6 (60%) | 10 | Important | Important | Union with prompt_context is 7 of 10. |
| Technical writing [tech_writing] | 4 (40%) | 10 | Important | Important | Content, documentation and white-paper duties at Anthropic ×3 and Siemens. |
| Retrieval quality [retrieval_quality] | 0 (0%) | 10 | Should | Important | No posting names hybrid search, reranking or recall. |
| ML fundamentals [ml_fundamentals] | 5 (50%) | 10 | Important | Important | Mistral Palo Alto, Scale, Snorkel, Siemens, Atomicwork; none at Anthropic. |
| Generative AI [generative_ai] | 10 (100%) | 10 | Must (definitional) | Important | True of every posting; does not discriminate between candidates. |
| AWS / Azure / GCP [cloud] | 3 (30%) | 10 | Should | Important | Nice-to-have at Mistral Prototyping; "AWS or GCP" at Scale; generic at Atomicwork. |
| Git and CI/CD [git_ci] | 1 (10%) | 10 | Optional | Important | Version control at Atomicwork only. |
| Embeddings and vector search [vector_search] | 3 (30%) | 10 | Should | Important | Mistral Palo Alto, Snorkel, Atomicwork. |
| Pragmatism under ambiguity [c1_pragmatism] | 4 (40%) | 10 | Important | Important | Explicit ambiguity wording at Anthropic ×2, Mistral Prototyping, Scale. |
| Explaining trade-offs [c2_tradeoffs] | 1 (10%) | 10 | Should | Important | Snorkel only; general communication is in 7 of 10. |
| Ownership and incident response [c3_ownership] | 3 (30%) | 10 | Should | Important | Ownership wording only; no incident or on-call wording. |
| Responsible-AI judgement [c4_responsible_ai] | 4 (40%) | 10 | Important | Important | Anthropic ×3 and Siemens. |
| new:technical_communication | 7 (70%) | 10 | Important | none | Explicit communication or presentation requirement. |
| new:customer_facing_experience | 3 (30%) | 10 | Important | none | Required at Anthropic London and Architect and at Snorkel; an alternative or nice-to-have in three more. |
| new:mcp | 2 (20%) | 10 | Should | none | Anthropic Enterprise and Life Sciences. |
| new:agent_frameworks_named | 3 (30%) | 10 | Should | none | LangChain, LlamaIndex, LangGraph, CrewAI, Semantic Kernel (Mistral Palo Alto, Snorkel, Siemens). |
| new:fine_tuning | 3 (30%) | 10 | Should | none | Mistral Palo Alto, Snorkel, Atomicwork. |

**Platform cross-check.** The knowledge base's shares come from JobsPipe's AI Engineer population, where Python is 78.4%, LLM 76.7%, agentic AI 59.3%, RAG 54.0%, machine learning 39.8% and remote 11.0% [S21]. My sample agrees on Python and agents, is lower on RAG, and adds customer scoping and evaluation as near-universal in customer-facing variants.

### DF5 Pay (item 5)

| Population | Statistic | Value | Component | n | Date | Grade |
|---|---|---|---|---|---|---|
| Levels.fyi, US, Applied AI Engineer [S19] | p25 / p50 / p75 / p90 | $200K / $250K / $475K / $505K | total compensation | not shown | 2026-11-11 | B |
| OpenAI Enterprise (US) [S18] | posted range | $197K–$278K plus equity | base | 1 | 2026-11-13 | B |
| OpenAI API Platform, Digital Natives (SF, Seattle) [S18] | posted range | $251K–$278K plus equity | base | 1 | 2026-11-13 | B |
| Anthropic Enterprise (SF, NYC) [S1] | posted range | $200K–$320K | not stated | 1 | 2026-11-13 | A (COI) |
| Anthropic Life Sciences [S3] | posted range | $280K–$320K | filed under Sales; may be OTE | 1 | 2026-11-13 | A (COI) |
| Anthropic Architect, Startups [S4] | posted range | $240K–$315K | not stated | 1 | 2026-11-13 | A (COI) |
| Anthropic London [S2] | posted range | £225K–£240K | not stated | 1 | 2026-11-13 | A (COI) |
| Snorkel Enterprise Solutions [S15] | posted range | $175K–$300K | OTE plus options | 1 | 2026-11-13 | A |
| Scale Enterprise GenAI (SF, NYC; listing 2026-02-23, outside the window) [S12] | posted range | $168.2K–$248.5K plus equity | base | 1 | 2026-02-23 | B |
| AssemblyAI (remote US, senior; posting ID not matched) [S47] | posted range | $195K–$250K | base | 1 | 2026-11-13 | B |
| NVIDIA Applied AI Engineer (US; other NVIDIA postings) [S24] | posted range | $152K–$287.5K plus equity | base | 1 | 2026-11-13 | B |
| US lab postings (OpenAI ×2, Anthropic ×3) [S1, S3, S4, S18] | median of range midpoints | $264,500 | base or OTE | 5 | 2026-11-13 | M |
| LCA filings, exact title (Scale ×2, Snorkel withdrawn, General Catalyst, loanDepot, one 2024 filing) [S40] | median offered wage | $185,480 | offered base wage | 6 | FY2024–FY2026 | M |

- **Corroboration.** The Levels.fyi median ($250K total compensation, all employers pooled) falls inside the spread of lab base midpoints ($237.5K–$300K). Because the pool also holds vendors and enterprises, and lab total compensation adds equity to base, lab total compensation is likely above the pooled median, but I found no lab-specific total-compensation figure for the title. The Levels.fyi p90 moved from $605K (snapshot of 2026-10-04) to $505K (2026-11-11), so the upper tail is unstable. Levels.fyi's OpenAI Software Engineer median is $600K (248 submissions, 2026-11-01) against $800K in a 2025-12-26 snapshot; that is the SWE family, not this title [S20].
- **Alias pay.** OpenAI "AI Deployment Engineer" listings show $176K–$224K for US remote (Inference Jobs, undated) [S49].
- **LCA caveat.** LCA wages are what employers filed, not what people are paid [S40, S41]. One of the six filings predates 2025-01-01 and one was withdrawn.
- **India proxies, not role-specific.** Levels.fyi Software Engineer, Greater Bengaluru: median total compensation ₹5,540,248 (p25 ₹3,781,292; p75 ₹7,954,873), generated 2026-07-18; the URL path suggests a senior-level page, so the level scope is unconfirmed (B) [S52]. Glassdoor-attributed AI Engineer average about ₹10–12 LPA (C). An aijobs.net model estimate for a mid-level Applied AI Engineer is ₹13.4–16.8 LPA (D). A salary-guide site gives ₹6–80 LPA with no traceable method (E). No posted INR range for a lab Applied AI Engineer was found [S44, S52].

### DF6 Interview loop (item 6)

| Employer type | Stages reported | AI-tool policy | Source and grade | Fit with the KB "Application" track |
|---|---|---|---|---|
| Anthropic | Application with a "Why Anthropic" essay; recruiter screen; hiring-manager call; take-home, online assessment or live build; customer-conversation simulation (one vendor's claim); virtual onsite with system design; values round; 4–6 weeks | Drafts yours first, then refine with Claude. Take-homes without Claude unless indicated. Live interviews: no AI unless indicated. Interview preparation with AI is encouraged. | Policy: A, COI [S36]. Stages: C, prep vendors with COI [S34, S35] | Partial. RAG, agent and evaluation design fit; a customer-scenario round is missing from the track. |
| OpenAI | Recruiter or manager screen; coding and system-design screens; take-home or solution design for FDE-type roles; virtual onsite of 4–6 rounds with project walkthrough, behavioural and customer-scenario rounds (Solutions Architect and FDE guides); 3–6 weeks | Varies by team; applied loops resemble standard senior engineering loops | C [S37, S38]; guides cover SWE, SA, FDE and "GenAI Engineer (often Applied AI Engineer)" | Partial, same gap |
| Mistral | HR or talent-partner call (already technical); LeetCode-medium coding round; team-lead or senior AI engineer round; deep technical use-case round; customer-success round; about 5 rounds; take-home for many senior roles | Not reported | D (single candidate reports, Aug and Oct 2025; one report from 2024 is flagged as older) and C [S51] | Partial |
| Scale, Google Cloud, Indian GCCs and consultancies | No role-specific loop evidence found | n/a | Absence | n/a |

One prep vendor's claim that a customer round "filters out about 60%" is untraceable and graded E. I did not use it.

### DF7 Proof of work and credentials (items 7, 8)

- **Proof asked for in postings (A).**
  - OpenAI's Codex Applied AI posting names contributions to resources such as the OpenAI Cookbook and active use of AI coding tools [S18].
  - Anthropic asks for shipped systems that real users depend on, builder credibility and public technical content [S1–S3].
  - Mistral lists hackathons, AI competitions and open-source LLM contributions as nice-to-haves, and "production systems end to end, not just prototypes" as a requirement [S7, S8].
  - Snorkel's application form has an optional GitHub field [S15].
- **Hiring-manager statements in a named, first-person source:** none found. Rankings of proof types are therefore P at best.
- **Strongest public examples of the proof type.** Anthropic's Life Sciences posting names MCP servers, benchmarks and agent skills as artefacts [S3]. I did not verify individual public repositories.
- **Credentials.**
  - No posting read in full names a certification. JPMorgan's India boilerplate says "formal training or certification" generically [S26].
  - The AWS Certified Generative AI Developer – Professional (AIP-C01) guide, which I opened, describes a target candidate with 2+ years building production applications and 1 year of hands-on GenAI work. The exam has 65 scored and 10 unscored questions, a scaled score of 100–1,000 and a pass mark of 750. Domains are: foundation-model integration, data management and compliance 31%; implementation and integration 26%; AI safety, security and governance 20%; operational efficiency 12%; testing, validation and troubleshooting 11% [S45].
  - The guide page shows no fee or duration. Third-party guides report a fee of about $300 and a duration of 170–180 minutes (C) [S46].
  - Employer statements about credentials for this role: none found.

### DF8 Entry routes and prerequisites (item 9)

- **Years and degree.** Stated minimum years run 2, 2, 3, 3, 3, 4, 4, 4 (median 3, n = 8; Scale and Atomicwork state none). Degree: bachelor's or equivalent in 7 of 10; "no specific degree" in 1 (Atomicwork); none stated in 1 (Mistral Prototyping); PhD or master's required in 1 (Mistral Palo Alto), while Mistral's Lead posting accepts "self-made" [S10].
- **Backgrounds named by employers.** OpenAI lists applied AI or ML engineering, FDE, software engineering, customer engineering, solutions architecture and technical consulting [S18]. Anthropic lists software engineer, FDE, technical founder, product engineer, TPM, sales engineer and solutions architect [S1–S4]. Mistral adds data scientist and has DevOps/SRE and ML-infrastructure variants (extracts) [S9].

| Background | Route evidence in postings | Fit with KB access score (judgement) |
|---|---|---|
| Backend or software engineer | Named by every lab and vendor posting | Supported |
| Data scientist | Mistral names it; Snorkel and Scale ask for AI/ML solution delivery | Supported |
| Front-end engineer | Mistral Prototyping wants working frontend knowledge; Deloitte India's variant is full-stack | Weakly supported |
| DevOps or SRE | Explicit Mistral variants (extracts) | Not in the KB list; evidence exists |
| Product or technical programme manager | TPM named by Anthropic and Mistral | Not in the KB list |
| PhD researcher | Required in 1 of 10; Mistral Lead accepts "self-made" | Partly supported |
| Non-technical domain worker | No evidence of a route | Supported (low) |
| New graduate | None of 36 titles is entry level; AI-titled roles are 16.4% entry level [S22] | Supported (low) |

- **Typical prior roles of people hired:** no published analysis found (Absence).

### DF9 Progression, durability and leverage (item 10)

- **Ladder in postings (A/B).** Applied AI Engineer, then Senior or Staff (Scale Senior Frontier Agents asks 5+ years; Scale, Snorkel, Crusoe, Flexport and Concurrence post Staff rows). Next comes Lead or Technical Lead (Mistral Lead asks 7–10+ years). Manager postings exist at Anthropic (Life Sciences) and OpenAI (Digital Natives), and Scale and Snorkel post Director and Head-of-Applied-AI roles [S6, S9, S10, S12, S16, S18].
- **Exits and adjacent roles seen in postings.** Applied AI Architect and other pre-sales roles, FDE and Staff FDE, and a research-engineer variant (Anthropic Applied AI Research Engineer, 6+ years) [S4, S6, S13]. I found no published analysis of where people go after the role.
- **Durability.**
  - Supporting: family-level demand growth (KF7); lab expansion into India and EMEA (OpenAI Delhi, Mumbai, Bangalore, Munich, London); spread of the title into enterprises and GCCs (Siemens, Deloitte India, NVIDIA, Flexport).
  - Against: title instability (Scale's rename; OpenAI's parallel titles) and the Indeed India moderation after June 2026.
  - Missing: no evidence on tasks within the role being automated. OpenAI's Codex Applied AI posting asks for fluent use of AI coding tools rather than warning of displacement [S18].
- **Leverage (A).** Mistral's Prototyping posting describes technical pre-sales work: prototypes that help win deals and lead to follow-on work [S7]. OpenAI's API Platform posting asks for leadership of production-scale systems through adoption to "measurable business impact" [S18]. Anthropic's Life Sciences posting sits in the Sales department [S3].

### DF10 Work footprint and specialisations (item 11)

Layers named in duties or requirements of the 10 full reads: L6 applications and deployment 10; L5 orchestration and context (agent architectures, agentic workflows, context engineering, RAG) 10; evaluation plane 8; assurance (safety, security, governance) 4; post-training or fine-tuning 3; serving or infrastructure 2 (Mistral Prototyping, Atomicwork); models and research 0.

| Specialisation (role-card context) | Share of the 36 | Note |
|---|---|---|
| Partner Applied AI Engineer | 3 (8%) | OpenAI Google Cloud, Oracle and Cloud ISV, AWS |
| Context Retrieval | 0 | One Databricks posting (2026-07-24) is outside the window [S14] |
| Segment-named (Enterprise, Large Enterprise, Digital Natives, Startups, Healthcare and Life Sciences, Life Sciences, Cyber and Government) | 9 (25%) | Anthropic and OpenAI |
| Regulated or sensitive-sector variants (HLS, Life Sciences, Cyber and Government) | 3 (8%) | The knowledge base's "regulated settings" wording applies to a minority |

### DF11 Geography and sponsorship (item 12)

- **Locations in the sample.** San Francisco Bay Area, New York, Seattle, Washington DC, Los Angeles; London; Paris, Munich; Delhi, Mumbai, Bengaluru; Seoul; Kuwait City, Tel Aviv. OpenAI search extracts add Tokyo, Singapore, Sydney, Abu Dhabi and São Paulo (not among the 36) [S18].
- **Remote.** Lab postings are hybrid or on-site. Remote options appear at OpenAI Enterprise (US), OpenAI Partner-AWS (Bangalore) and Snorkel (US).
- **Sponsorship (A).** Anthropic's four postings say it sponsors visas but cannot do so for every role and candidate [S1–S4]. Mistral Palo Alto lists visa sponsorship among benefits [S8].
- **LCA filings (B, derived from DOL data).** Exact-title filings are few: Scale (including "Applied AI Engineer, Autonomous Agents" at $295,000, certified 2026-01-05), Snorkel (withdrawn), General Catalyst, loanDepot and one 2024 filing [S40]. OpenAI's 311 certified LCAs (FY2025 to Q3 FY2026, median $270,000) are mostly other titles, and the AI/ML engineer family shows 8,275 certified LCAs at a median of $167,485 across 2,693 employers [S41]. Business Insider reports about 80 certified Anthropic H-1B roles in the first half of fiscal 2026 (C) [S42]. For the exact title, sponsorship evidence therefore rests on posting wording, not on filing volume.

### DF12 Résumé and profile signals (item 13)

- **What postings reward:** named customer-facing delivery; production LLM systems with evaluation; context and agent design; MCP; technical writing; and, at Mistral, hackathons and open-source contributions [S1–S4, S7, S8].
- **Headline and keyword patterns matching the postings:** "Applied AI Engineer / forward-deployed", "prototype to production", "evaluation frameworks", "context engineering", "agent architectures", "customer-facing", "scoping", "workshops", "MCP", "Python or TypeScript".
- **Red flags (P):** demos with no external users, no evaluation evidence, and certificate-led profiles.
- **Evidence-line patterns** for the Must and Important skills are in the `practice` records. They are patterns, not claimed achievements.

### DF13 Misconceptions and red flags (item 14)

1. "Applied AI" at OpenAI is also the name of an organisation of ordinary product-engineering roles; it is not the customer-facing title [S14].
2. NVIDIA, Siemens, Atomicwork and Deloitte India use the title for internal or product engineering [S24, S17, S50, S27].
3. JPMorgan's "Applied AI ML" titles are ML engineering and data-science roles [S26].
4. A PhD is rarely required (1 of 10 reads).
5. Level labels can conflict with years (Siemens tags the role entry level and asks 3–5 years) [S17].
6. Posted ranges may be OTE (Anthropic Sales-department postings; Snorkel) [S3, S15].
7. Federal variants may carry clearance requirements (a Snorkel Federal listing in search extracts) [S16].
8. Nearly three in ten fetched search-indexed postings were closed (4 of 14) [S5, S9, S23, S25].
9. Title inflation is possible: "Applied AI Engineer II" at Deloitte India describes full-stack product engineering [S27].

### DF14 India (item 15)

- **Employers.** OpenAI (Delhi, Mumbai, Bangalore: Applied AI Engineer, Architect, Partner-AWS); Siemens Technology and Services (Bangalore); Deloitte (Bengaluru); Hitachi Energy (Bengaluru, outside the window); DevRev (Bangalore); Turing (Hyderabad FDE); JPMorgan (title collision) [S13, S14, S17, S18, S26–S28, S43].
- **OpenAI India terms.** Hybrid with 3 days in the office per week and relocation assistance [S18].
- **Pay.** No lab INR range found; proxies in DF5 [S44, S52].
- **Interview differences.** None found.
- **Demand.** India FDE postings rose nearly 19× year on year to June 2026 and moderated afterwards [S29]. AIM reports OpenAI hiring in Delhi and Mumbai [S43].
- **Aliases.** Applied AI Engineer, Applied AI Architect, Member of Applied AI, Forward Deployed Engineer, Applied AI ML (JPMorgan, collision).

### DF15 Implications for knowledge-base outputs (non-binding)

- **role_scores.json.** Demand 5 (4–6.5): keep the range, because exact-title demand is concentrated at labs and startups while family-level growth is strong. The evidence grade can move from C to B for the US lab and startup segment (KF2) but stays C overall. Pay 7.5 (6–9): supported at US and UK labs; the India lens needs a separate D-graded entry. Durability 6.5 (5.0–8.0): consider widening the title-level lower bound (KF9). Leverage 8.5 (7.5–9.5): supported by posting wording (DF9).
- **skills_ontology.json.** Move customer_scoping and evals to Must; move retrieval_quality, guardrails, cloud, git_ci, vector_search and c2/c3 down; carry the new skills with n = 10 caveats.
- **role_titles.json.** Add the aliases and the negative aliases from KF1 and KF9.
- **role-catalog.md.** State that the previous skill shares were AI Engineer shares.

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Customer- and solutions-facing LLM engineering at labs and vendors, with evaluation and safety in regulated settings | updated | Holds at labs and vendors. Pre-sales, partner, internal and ML-collision variants exist. Regulated-sector variants are a minority (3 of 36) [S1–S4, S17, S18, S24, S26, S50] | A/B |
| K2 | Aliases: Context Retrieval Engineer; Partner Applied AI Engineer | updated | Partner confirmed (OpenAI, listed 2026-11-11); Context Retrieval confirmed (Databricks, 2026-07-24); many further aliases found [S13, S14, S18] | B |
| K3 | 16 of newest 50 Fast AI Jobs AI-Engineer rows (2026-10-19); about 100 of 326 | updated | 21 of the newest 50 on 2026-11-11; category now 352 rows. An extrapolation of about 150 is weak because the newest rows are bulk postings [S13] | B/M |
| K4 | No role-specific pay; lab SWE total-compensation medians $875K–$882.5K | updated | Levels.fyi title page exists (median $250K); OpenAI SWE median $600K (2026-11-01) and $800K (US page, 2025-12-26); the $875K figure was not reproduced; Anthropic SWE not checked [S19, S20] | B |
| K5 | No India demand evidence | updated | OpenAI India postings; Indeed India FDE growth; GCC and consultancy postings [S17, S18, S27, S29, S43] | B |
| K6 | No India pay evidence | confirmed | The gap persists for the title; only software-engineer and AI-engineer proxies and estimates exist [S44, S52] | C/D |
| K7 | Durability is judgement: customer-facing delivery at labs and vendors | updated | Family-level demand supports it; title instability weakens the title; no automation evidence found [S29–S32, S11, S18] | B/C |
| K8 | Footprint L6, L5; evaluation plane | confirmed | L6 10 of 10, L5 10 of 10, evaluation 8 of 10 in full reads [S1–S4, S7, S8, S11, S15, S17, S50] | M |
| K9 | Interview track Application (RAG with access control, agent loop control, evaluation architecture, context management) | updated | Reports add a build or take-home and a customer-conversation round; no access-control or RAG-specific evidence [S34–S38, S51] | C/D |
| K10 | Must skills Python, LLM APIs, RAG, Agents, with 78.4/76.7/54.0/59.3% | updated | Shares are the AI Engineer population's; sample 9/10, 5/10, 5/10, 9/10; RAG is variant-dependent [S21, S1–S4, S7, S8, S11, S15, S17, S50] | B/M |
| K11 | Important skills with platform shares | updated | Customer scoping and evaluation belong in Must; retrieval quality, guardrails, cloud, git/CI and vector search fit Should or Optional [S1–S4, S7, S8, S11, S15, S17, S50] | M |
| K12 | AWS AIP-C01 (Optional; services channels) | confirmed | Exam guide opened and the exam is active; 0 of 10 postings name it [S45, S46] | A/C |
| K13 | Lab-tier bar on top of the AI Engineer stack; backend about 6 months, PhD about 8 months | updated | The lab bar is 3–4+ years including customer-facing work; PhD required in 1 of 10; the month estimates have no source in postings [S1–S4, S8] | A/M |
| K14 | Proof: customer-facing reference implementation with evals and a write-up | confirmed | Postings name evaluation, public content, shipped systems and open source [S1–S3, S7, S8, S18] | A |
| K15 | Reframe generic chatbot demos and work with no external users | confirmed | Anthropic asks for systems that real users depend on; Mistral asks for more than prototypes [S1, S3, S7] | A/P |

## Absences

| Item | Where I looked | Result |
|---|---|---|
| Exact-title posting counts on LinkedIn, Indeed and Glassdoor | Search extracts; login and bot walls | Not obtainable. Fast AI Jobs (AI startups) is the only exact-title count |
| A JobsPipe page for "Applied AI Engineer" | JobsPipe search | None exists; only the AI Engineer page |
| OpenAI posting bodies | openai.com careers and Ashby pages | Bot detection blocked fetches; extracts only |
| AssemblyAI posting bodies | Greenhouse | Blocked; listing and aggregator copies only |
| Enterprise, consultancy and GCC bodies on Workday and SuccessFactors | Searches; EY fetch | Thin; EY closed |
| Role-specific loops at Scale, Google Cloud, Indian GCCs and consultancies | Search | Not found |
| Posted INR ranges for lab Applied AI Engineer roles | Search | Not found |
| LCA filings for the exact title at OpenAI and Anthropic | LCA aggregators | Not found; OpenAI filings are mostly other titles |
| Hiring-manager statements on proof of work in a named first-person source | Search | Not found; postings only |
| Published analyses of prior roles of people hired | Search | Not found |
| Non-English postings | Not searched | Gap (WIDEN not done) |
| Evidence on tasks within the role being automated by AI tools | Search | Not found |
| DOL LCA primary files | Not opened | Aggregators used (B) |
| Posting-specific URLs for three OpenAI rows (API Platform, Partner-AWS, Cyber-Government) | openai.com search extracts | URLs not retained; the Ashby board root is given in those `jd` records |

## Open Questions & Risks

**Strongest objections an expert would raise**

| Objection | Evidence for | Evidence against |
|---|---|---|
| The sample is lab-heavy and mostly snippet-based, so shares are unreliable | 32 of 36 rows are labs or AI vendors; only 10 full reads (about ±31 pp) | Shares are labelled as a cross-check; Fast AI Jobs gives an independent exact-title share |
| "Applied AI Engineer" is just FDE or AI Engineer relabelled | OpenAI runs parallel titles; Scale renamed its page | Anthropic and Mistral keep Engineer, Architect and FDE as separate titles; skill patterns differ from the AI Engineer shares |
| Posted ranges may be OTE, not base | Anthropic's Sales-department postings; Snorkel wording | Flagged in the pay table; Levels.fyi gives a second reading |
| Levels.fyi is self-reported and skewed | No n shown; p90 moved by $100K between snapshots | The median agrees with posted ranges |
| Demand growth figures describe FDE, not this title | Indeed, Lightcast and LinkedIn describe FDE | The Fast AI Jobs exact-title count measures the title directly (21 of 50) |
| The newest 50 rows over-represent bulk posters | OpenAI and Scale supply 10 of 21 | Counts are reported with employer splits and an explicit weak-extrapolation caveat |

- **Unknowns.** Variant shares for the 26 postings without full reads. India pay. Whether the FDE-family boom persists after India's moderation. Whether OpenAI keeps two parallel titles.
- **Risks.** Closed listings in search indexes (4 of 14 fetched). Title churn (Scale, OpenAI).

## Discovered Concerns

1. The knowledge base's skill shares for this role came from the AI Engineer population. Other role cards built on feeder titles may share the problem.
2. Posted ranges mix base and OTE, which affects any pay anchor in `role_scores.json`.
3. `role_titles.json` needs negative aliases for OpenAI's "Applied AI Engineering" organisation and JPMorgan's "Applied AI ML" titles.
4. Fast AI Jobs rows link to employers' own ATS pages, so an exact-title count could be repeated in future sessions.
5. Anthropic's Applied AI department holds Engineer, Architect, FDE, Manager and Research Engineer titles that need mapping to role IDs.
6. Search-indexed postings were closed about three times in ten; future sessions should verify liveness by fetching.
7. COI: the author model is Anthropic's, and five Anthropic rows plus Anthropic's candidate-guidance page are in the evidence.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Customer-embedded delivery at labs and vendors | Updated | True there; internal and ML-engineering variants carry the same title | `role_titles.json` variants |
| P2 | Python at least 75%; RAG at least 50% | Updated | Python 9 of 10; RAG 5 of 10 (0 of 4 at Anthropic) | `skills_ontology.json` RAG tier |
| P3 | US lab base $180K–$350K | Confirmed | $197K–$320K posted | `role_scores.json` pay |
| P4 | 3–5 years; bachelor's or equivalent | Confirmed | Median 3 years; labs 3–4+; bachelor's or equivalent in 7 of 10 | Access scores unchanged |
| P5 | India lab pay unposted in INR | Confirmed | No INR range found | Keep D grade |
| P6 | Title stable | Contradicted | Scale rename; OpenAI parallel titles; title collisions | Aliases and negative aliases |

## Sources & Evidence Ledger

All sources were retrieved on 2026-11-13. "n/s" means the page showed no publication date. COI marks Anthropic's own pages, because the author model is Anthropic's.

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Applied AI Engineer, Enterprise, Anthropic (Greenhouse 5057647008) https://job-boards.greenhouse.io/anthropic/jobs/5057647008 | n/s | 2026-11-13 | A | Read | COI | JD, pay, visa wording |
| S2 | Applied AI Engineer, London, Anthropic (5116274008) https://job-boards.greenhouse.io/anthropic/jobs/5116274008 | n/s | 2026-11-13 | A | Read | COI | JD, GBP pay |
| S3 | Applied AI Engineer, Life Sciences, Anthropic (boards-api 5111942008) https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5111942008 | 2026-02-06 | 2026-11-13 | A | Read | COI | JD, pay, Sales department |
| S4 | Applied AI Architect, Startups, Anthropic (boards-api 5406982008) https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5406982008 | 2026-08-28 | 2026-11-13 | A | Read | COI | Pre-sales variant |
| S5 | Anthropic Greenhouse board index (670 jobs; redirect for closed posting 5073277008) https://job-boards.greenhouse.io/anthropic?error=true | 2026-11-13 | 2026-11-13 | A | Read | COI | Board size; closed posting |
| S6 | Anthropic extracts: Applied AI Research Engineer 5390811008; Beneficial Deployments 5068226008; FDE 4985877008; manager roles https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5390811008 | 2026-09-04 (5390811008) | 2026-11-13 | B | Extract | COI | Variants, ladder |
| S7 | Applied AI Engineer, Prototyping, Mistral (Lever) https://jobs.lever.co/mistral/ac195fdb-1731-4ce2-b47e-c1bb8c72c59d | 2025-10-10 (first listing per Fast AI Jobs) | 2026-11-13 | A | Read | none | JD, leverage |
| S8 | Applied AI, Forward Deployed Machine Learning Engineer, Palo Alto, Mistral (Lever) https://jobs.lever.co/mistral/0b476d3a-5f0c-4dda-9a5e-bd5ed8515328 | n/s | 2026-11-13 | A | Read | none | JD, visa benefit |
| S9 | Mistral Lever extracts: Technical Lead, Forward Deployed (e2cf255f); Fullstack EMEA (aceffeba, client error on fetch) https://jobs.lever.co/mistral/e2cf255f-49c8-4630-afe0-7f665f51f01f ; https://jobs.lever.co/mistral/aceffeba-c4e9-4b3b-adff-e7e78b986c5c | n/s | 2026-11-13 | B | Extract | none | Variants; closed posting |
| S10 | Lead Applied AI Engineer, Seoul, Mistral (General Catalyst jobs board copy) https://jobs.headline.com/companies/mistral-ai-2/jobs/90169162-lead-applied-ai-engineer | 2026-08-17 | 2026-11-13 | B | Extract | none | Lead rung, degree wording |
| S11 | Frontier Agents Engineer, London, Scale AI (Greenhouse 4536659005) https://job-boards.greenhouse.io/scaleai/jobs/4536659005 | n/s | 2026-11-13 | A | Read | none | JD, rename |
| S12 | Scale extracts: Senior Frontier Agents Engineer (Applied AI) 4720478005; Accel listing for Enterprise GenAI https://job-boards.greenhouse.io/scaleai/jobs/4720478005 ; https://jobs.accel.com/companies/scale-ai/jobs/44524550-applied-ai-engineer-enterprise-genai | 2026-02-23 (Accel) | 2026-11-13 | B | Extract | none | Pay, ladder |
| S13 | AI Engineer Jobs at AI Startups, Fast AI Jobs (352 roles; newest 50 rows with ATS links) https://www.fastaijobs.com/jobs/role/ai-engineer | 2026-11-11 | 2026-11-13 | B | Read | none | Demand, aliases, listing-level JDs |
| S14 | Fast AI Jobs earlier snapshot (275 roles) and company pages (Mistral, OpenAI team labels, Databricks, DevRev) https://www.fastaijobs.com/companies/mistral/ai-engineer | 2026-07-30 | 2026-11-13 | B | Extract | none | Trend, aliases, OpenAI organisation labels |
| S15 | Applied AI Engineer - Enterprise Solutions, Snorkel AI (Greenhouse 5709067004) https://job-boards.greenhouse.io/snorkelai/jobs/5709067004 | 2026-06-26 (per Fast AI Jobs) | 2026-11-13 | A | Read | none | JD, OTE pay |
| S16 | Snorkel extracts: Pre-Sales 5831080004; Staff and Federal variants; Built In copy https://job-boards.greenhouse.io/snorkelai/jobs/5831080004 | n/s | 2026-11-13 | B | Extract | none | Pay, ladder, clearance wording |
| S17 | Applied AI Engineer, Siemens Technology and Services Private Limited (501447) https://jobs.siemens.com/fr_FR/externaljobs/JobDetail/501447 | 2026-04-03 | 2026-11-13 | A | Read | none | India enterprise variant |
| S18 | OpenAI careers pages for Applied AI Engineer variants (search extracts; fetch blocked) https://openai.com/careers/applied-ai-engineer-enterprise-san-francisco/ ; https://openai.com/careers/applied-ai-engineer-delhi-india/ | n/s | 2026-11-13 | B | Extract | fetch blocked | JD, pay, India terms, ladder |
| S19 | Applied AI Engineer Salary, Levels.fyi https://www.levels.fyi/t/software-engineer/title/applied-ai-engineer | 2026-11-11 | 2026-11-13 | B | Read | self-reported | Pay |
| S20 | OpenAI Software Engineer salaries, Levels.fyi https://www.levels.fyi/companies/openai/salaries/software-engineer | 2026-11-01 | 2026-11-13 | B | Extract | self-reported | K4 test |
| S21 | AI Engineer job description, JobsPipe https://jobspipe.dev/job-description/ai-engineer | n/s | 2026-11-13 | B | Extract | shares only | Provenance of the KB's skill shares |
| S22 | AI jobs and entry-level hiring, JobsPipe https://jobspipe.dev/blog/ai-jobs-entry-level | 2026-10-11 | 2026-11-13 | B | Extract | shares only | Entry-level share |
| S23 | Forward Deployed Engineer IV, Applied AI, Google Cloud, Google Careers ("job not found" on retrieval) https://google.com/about/careers/applications/jobs/results/125981803457454790-forward-deployed-engineer-iv | n/s | 2026-11-13 | A | Read | closed | Liveness test (exclusion) |
| S24 | Senior Applied AI Engineer, NVIDIA (Talentify copy; Built In and other NVIDIA postings) https://www.talentify.io/senior-applied-ai-engineer-santa-clara-california-us-nvidia | 2026-09-14 | 2026-11-13 | B | Extract | aggregator | Internal variant, pay |
| S25 | Consultant – Applied AI Engineer, TC, EY London ("no longer available") https://careers.ey.com/ey/job/London-Consultant-Applied-AI-Engineer%2C-TC-E14-5EY/1382111233/ | 2026-04-09 | 2026-11-13 | A | Read | closed | Liveness test (exclusion) |
| S26 | JPMorgan Applied AI ML Lead listings https://www.themuse.com/jobs/jpmorganchase/applied-ai-ml-lead-1288d4 | n/s | 2026-11-13 | B | Extract | none | Title collision |
| S27 | Applied AI Engineer II, Deloitte Bengaluru (aggregator copy) https://www.airtribe.live/jobs/software-developer/applied-ai-engineer-software-engineer-ii-at-deloitte-XM2UXHZA3XUO | 2026-10 | 2026-11-13 | C | Extract | aggregator | India consultancy variant |
| S28 | Applied AI Engineer, Hitachi Energy Technology Services, Bengaluru (aggregator copy) https://apna.co/job/bengaluru/applied-ai-engineer-1592588882 | 2026-05-05 | 2026-11-13 | B | Extract | out of window | India enterprise variant |
| S29 | India FDE postings surge nearly 19-fold, Indeed Hiring Lab via IANS https://ianslive.in/indias-forward-deployed-engineer-job-postings-surge-19-fold-report--20261014115304 | 2026-10-14 | 2026-11-13 | B | Extract | corroborated (People Matters, Deccan Chronicle) | India trend |
| S30 | Forward-deployed engineers, Fortune, citing Lightcast https://fortune.com/2026/09/03/forward-deployed-engineers-fast-growing-six-figure-silicon-valley-job-integrate-ai-with-customers-tech-careers-palantir/ | 2026-09-03 | 2026-11-13 | B | Extract | none | US trend |
| S31 | Why forward deployed engineers are enterprise AI's fastest-growing role, skai.io (cites Indeed) https://skai.io/blog/why-forward-deployed-engineers-are-enterprise-ais-newest-fastest-growing-role/ | 2026 | 2026-11-13 | C | Extract | secondary | Indeed US counts |
| S32 | Inside the AI Revolution, LinkUp https://www.linkup.com/insights/blog/inside-the-ai-revolution-linkup-job-data-shows-steady-hiring | n/s | 2026-11-13 | C | Extract | vendor | Title list, growth |
| S33 | Why forward deployed engineers are becoming the delivery layer, techscoop Substack https://techscoop.substack.com/p/why-forward-deployed-engineers-are | 2026 | 2026-11-13 | C | Extract | single-source | Anthropic about 20 openings; LinkedIn comparison |
| S34 | Anthropic Applied AI Engineer interview, Perspective AI; 2026 FDE hiring trends https://getperspective.ai/blog/anthropic-applied-ai-engineer-interview-process-frontier-lab-2026 ; https://getperspective.ai/blog/2026-fde-hiring-trends-what-1000-job-posts-reveal | 2026-05-29 | 2026-11-13 | C | Extract | COI (vendor) | Loop; one untraceable statistic graded E |
| S35 | Anthropic interview guides, Educative and DataInterview https://www.educative.io/guide/anthropic-interview-process ; https://www.datainterview.com/blog/anthropic-forward-deployed-engineer-interview | 2026-10-28 (DataInterview) | 2026-11-13 | C | Extract | COI (prep vendors) | Loop stages |
| S36 | Guidance on Candidates' AI Usage, Anthropic https://www.anthropic.com/candidate-ai-guidance | 2025-07-10 | 2026-11-13 | A | Read | COI | AI-tool policy |
| S37 | OpenAI interview process 2026, team by team, techinterview.org https://www.techinterview.org/post/3233474915/openai-interview-process-2026-team-by-team/?format=md | 2026-07-13 | 2026-11-13 | C | Extract | none | OpenAI loop |
| S38 | OpenAI Solutions Architect and GenAI Engineer guides, CleverPrep and Dataford https://www.cleverprep.com/companies/openai/solutions-architect | 2026 | 2026-11-13 | C | Extract | COI (prep vendors) | Customer-scenario round |
| S39 | So You Want to Be an AI Engineer, Heavybit; Anthropic AI Engineer, DesignGurus https://heavybit.com/library/article/so-you-want-to-be-an-ai-engineer | n/s | 2026-11-13 | C | Extract | none | Boundary with AI Engineer |
| S40 | LCA aggregators: Scale, Snorkel, General Catalyst, loanDepot https://visapulseusa.com/employers/scale-ai-inc | 2026-04 | 2026-11-13 | B | Extract | derived from DOL data | LCA wages |
| S41 | OpenAI OpCo LCAs; AI/ML engineer LCAs, careery.pro https://careery.pro/h1b-sponsors/openai-opco-llc | FY2025 to Q3 FY2026 | 2026-11-13 | B | Extract | derived from DOL data | LCA context |
| S42 | Why AI firms file more H-1B visas, Business Insider via BusinessToday https://www.businesstoday.in/nri/visa/story/why-ai-firms-like-anthropic-openai-are-filing-for-more-h-1b-visas-even-while-big-tech-cos-pulled-back-535816-2026-06-10 | 2026-06-10 | 2026-11-13 | C | Extract | secondary | Sponsorship context |
| S43 | OpenAI is hiring AI engineers in Delhi and Mumbai, Analytics India Magazine https://analyticsindiamag.com/ai-news/openai-is-hiring-ai-engineers-in-delhi-mumbai/ | 2026 | 2026-11-13 | B | Extract | none | India demand |
| S44 | India pay pages: Weekday; Recrew; aijobs.net estimates https://www.weekday.works/post/ai-engineer-salary-in-india-2026 ; https://www.recrew.ai/salary-guides/applied-ai-engineer-in-india | 2026-10 | 2026-11-13 | C | Extract | model estimates; untraceable method | India pay proxies |
| S45 | AWS Certified Generative AI Developer – Professional (AIP-C01) exam guide, AWS https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html | n/s | 2026-11-13 | A | Read | none | Credential facts |
| S46 | AIP-C01 guides, Tutorials Dojo and MindMesh https://tutorialsdojo.com/aws-certified-generative-ai-developer-professional-certification-aip-c01-exam-guide-and-aip-c01-exam-topics-list/ | 2025-12-23 | 2026-11-13 | C | Extract | third-party | Fee and duration reports |
| S47 | AssemblyAI Applied AI Engineer, Built In and JustRemote copies https://www.builtinaustin.com/job/applied-ai-engineer/8228578 | n/s | 2026-11-13 | B | Extract | posting ID not matched | Pay, remote |
| S48 | Cohere, Titan AI, Apple and Google Senior Agent Engineer listings (out of window) https://www.fastaijobs.com/companies/cohere/ai-engineer | 2026-01 to 2026-07 | 2026-11-13 | B | Extract | out of window | Exclusions |
| S49 | Applied AI Engineering category, Inference Jobs https://inferencejobs.com/jobs/applied-ai-engineering | n/s | 2026-11-13 | B | Extract | category, not a title count | OpenAI parallel titles; keyword expansion |
| S50 | Applied AI Engineer, Atomicwork (employer careers page) https://www.atomicwork.com/career/4405099008 | n/s | 2026-11-13 | A | Read | none | JD (internal variant) |
| S51 | Mistral Applied AI interview reports: Taro (2025-08-01, 2025-10-01), Glassdoor (2024), techinterview.org, DataInterview https://www.jointaro.com/interviews/companies/mistral-ai/experiences/applied-ai-engineer-london-england-august-1-2025-declined-offer-negative-61fa1c00 ; https://www.techinterview.org/companies/mistral/?format=md | 2024-05 to 2026 | 2026-11-13 | D | Extract | single anecdotes; one pre-2025 | Mistral loop |
| S52 | Software Engineer salary, Greater Bengaluru, Levels.fyi https://www.levels.fyi/t/software-engineer/levels/senior/locations/greater-bengaluru.md | 2026-07-18 | 2026-11-13 | B | Extract | self-reported; level scope unconfirmed | India proxy |

## Data Appendix

Fragments in single quotes are verbatim phrases from the posting; other requirement text is paraphrase. `as_of` is the listing date where a listing dated the posting, otherwise 2026-11-13. Pay amounts are as posted; basis (base or OTE) is in the note when the posting states it.

### Job-description records (36 included postings)

```jsonl
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V1","employer":"Anthropic","title":"Applied AI Engineer, Enterprise","url":"https://job-boards.greenhouse.io/anthropic/jobs/5057647008","job_id":"5057647008","seen":"2026-11-13","location":"San Francisco, CA; New York City, NY","remote":"hybrid; 3 days in office per week","seniority":"mid-senior","years":"4+","degree":"bachelor's or equivalent experience","must":["'Production experience with LLMs'","agent development, evaluation frameworks, MCP and deployment at scale (paraphrase)","Python or TypeScript production applications (paraphrase)"],"nice":null,"pay":{"lo":200000,"hi":320000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Read in full; open 2026-11-13; says it sponsors visas; COI; base or OTE not stated"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V1","employer":"Anthropic","title":"Applied AI Engineer","url":"https://job-boards.greenhouse.io/anthropic/jobs/5116274008","job_id":"5116274008","seen":"2026-11-13","location":"London, UK","remote":"hybrid; at least 25% in office","seniority":"mid-senior","years":"4+","degree":"bachelor's or equivalent experience","must":["'Production experience building LLM-powered applications'","customer-facing or pre-sales technical role (paraphrase)","Python production applications (paraphrase)"],"nice":["workshops, hackathons and developer events (paraphrase)"],"pay":{"lo":225000,"hi":240000,"currency":"GBP","period":"year"},"ats":"Greenhouse","note":"Read in full; open 2026-11-13; says it sponsors visas; COI"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V1","employer":"Anthropic","title":"Applied AI Engineer, Life Sciences (Beneficial Deployments)","url":"https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5111942008","job_id":"5111942008","seen":"2026-11-13","location":"San Francisco, CA; New York City, NY","remote":"hybrid; at least 25% in office","seniority":"mid-senior","years":"4+","degree":"bachelor's or equivalent experience","must":["'Builder credibility'","prompting, context engineering, agent architectures, evaluation frameworks (paraphrase)","life-sciences or scientific-computing research experience (paraphrase)"],"nice":["MCP servers, benchmarks and agent skills for science (paraphrase)"],"pay":{"lo":280000,"hi":320000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Read via boards-api; first published 2026-02-06, updated 2026-04-01; department Sales so the range may be OTE; COI"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V1","employer":"Anthropic","title":"Applied AI Architect, Startups","url":"https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5406982008","job_id":"5406982008","seen":"2026-11-13","location":"San Francisco, CA; New York City, NY","remote":"hybrid; at least 25% in office","seniority":"mid-senior","years":"3+","degree":"bachelor's or equivalent experience","must":["'Comfortable with Python'","technical customer-facing experience (paraphrase)","LLM applications in production with context engineering and evaluation (paraphrase)","track record of technical selling (paraphrase)"],"nice":null,"pay":{"lo":240000,"hi":315000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Read via boards-api; first published 2026-08-28; pre-sales variant; COI"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S6"],"as_of":"2026-09-04","ttl":"V1","employer":"Anthropic","title":"Applied AI, Research Engineer","url":"https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5390811008","job_id":"5390811008","seen":"2026-11-13","location":"on-site; cities not seen","remote":"on-site","seniority":"senior","years":"6+","degree":null,"must":["6+ years as an engineer, TPM, FDE or founder (paraphrase)","customer exposure (paraphrase)"],"nice":null,"pay":null,"ats":"Greenhouse","note":"Search extract; updated 2026-09-04; research-engineer variant; liveness not verified; COI"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Enterprise","url":"https://openai.com/careers/applied-ai-engineer-enterprise-san-francisco/","job_id":null,"seen":"2026-11-13","location":"San Francisco; New York City; US remote","remote":"remote option listed","seniority":"unspecified","years":null,"degree":null,"must":["'highly proficient in Python'","enterprise AI systems taken from prototype to production (paraphrase)","systematic evaluation with representative data, graders and production signals (paraphrase)"],"nice":["JavaScript or TypeScript (paraphrase)"],"pay":{"lo":197000,"hi":278000,"currency":"USD","period":"year"},"ats":"Ashby","note":"Search extract; fetch blocked; an aggregator dated the posting 2026-07-09; undated-indexed; plus equity"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, API Platform, Digital Natives","url":"https://jobs.ashbyhq.com/openai","job_id":null,"seen":"2026-11-13","location":"San Francisco; Seattle","remote":"unknown","seniority":"senior","years":null,"degree":null,"must":["'personally leading complex, production-scale AI/ML systems'","relationships with customer CTOs and AI product leaders (paraphrase)"],"nice":null,"pay":{"lo":251000,"hi":278000,"currency":"USD","period":"year"},"ats":"Ashby","note":"Search extract of the openai.com page; posting-specific URL not retained, so the board root is given; undated-indexed; plus equity"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13","S18"],"as_of":"2026-11-03","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Digital Natives","url":"https://jobs.ashbyhq.com/openai/7be58f3a-6005-42ed-86fa-77773ebfb294","job_id":"7be58f3a-6005-42ed-86fa-77773ebfb294","seen":"2026-11-13","location":"London, UK","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (Fast AI Jobs, listed 2026-11-03); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-09","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Large Enterprise","url":"https://jobs.ashbyhq.com/openai/0cbc002e-bd6e-4aa3-9dbc-ed7fe59511ea","job_id":"0cbc002e-bd6e-4aa3-9dbc-ed7fe59511ea","seen":"2026-11-13","location":"Munich, Germany","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-09); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-06","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Enterprise - Healthcare and Life Sciences (HLS)","url":"https://jobs.ashbyhq.com/openai/6fc25168-bc4c-47a0-8601-583dfaf7fcbd","job_id":"6fc25168-bc4c-47a0-8601-583dfaf7fcbd","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-06); industry variant; body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-11","ttl":"V1","employer":"OpenAI","title":"Partner Applied AI Engineer, Google Cloud","url":"https://jobs.ashbyhq.com/openai/9a57d693-24ad-4457-a408-50617551ea5e","job_id":"9a57d693-24ad-4457-a408-50617551ea5e","seen":"2026-11-13","location":"San Francisco, CA","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-11); partner variant; body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-11","ttl":"V1","employer":"OpenAI","title":"Partner Applied AI Engineer, Oracle and Cloud ISV","url":"https://jobs.ashbyhq.com/openai/edfaa3d2-3434-4e51-af74-3945d63ad871","job_id":"edfaa3d2-3434-4e51-af74-3945d63ad871","seen":"2026-11-13","location":"San Francisco, CA","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-11); partner variant; body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S18","S43"],"as_of":"2026-11-13","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer","url":"https://openai.com/careers/applied-ai-engineer-delhi-india/","job_id":null,"seen":"2026-11-13","location":"Delhi, India (also Mumbai or Bangalore)","remote":"hybrid; 3 days in office per week; relocation assistance","seniority":"unspecified","years":null,"degree":null,"must":["backgrounds named: applied AI or ML engineering, FDE, software engineering, customer engineering, solutions architecture, technical consulting (paraphrase)"],"nice":null,"pay":null,"ats":"Ashby","note":"Search extract; fetch blocked; an Employbl brief dated 2026-08-22 listed it as posted about 3 weeks earlier; undated-indexed; no INR range"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Partner - AWS","url":"https://jobs.ashbyhq.com/openai","job_id":null,"seen":"2026-11-13","location":"Bangalore (remote), Mumbai, Delhi","remote":"remote option for Bangalore","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Search extract of the openai.com page; posting-specific URL not retained, so the board root is given; partner variant; undated-indexed"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V1","employer":"OpenAI","title":"Applied AI Engineer, Cyber, Government","url":"https://jobs.ashbyhq.com/openai","job_id":null,"seen":"2026-11-13","location":"Washington, DC","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":["deep cybersecurity experience with a product mindset (paraphrase)","secure cyber prototypes, agentic workflows and reference architectures (paraphrase)"],"nice":null,"pay":null,"ats":"Ashby","note":"Search extract of the openai.com page; posting-specific URL not retained, so the board root is given; government and national-security customers; undated-indexed"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S7"],"as_of":"2026-11-13","ttl":"V1","employer":"Mistral AI","title":"Applied AI Engineer, Prototyping","url":"https://jobs.lever.co/mistral/ac195fdb-1731-4ce2-b47e-c1bb8c72c59d","job_id":"ac195fdb-1731-4ce2-b47e-c1bb8c72c59d","seen":"2026-11-13","location":"Paris, France","remote":"on-site","seniority":"mid","years":"2+","degree":null,"must":["'hands-on engineer shipping AI-powered products'","LLMs, RAG and agentic systems in real deployments (paraphrase)","Python with FastAPI and Pydantic; working frontend knowledge (paraphrase)"],"nice":["hackathons or AI competitions","Docker, Kubernetes, AWS or GCP, Terraform","open-source contributions"],"pay":null,"ats":"Lever","note":"Read in full; open 2026-11-13; technical pre-sales team; first listed 2025-10-10"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S8"],"as_of":"2026-11-13","ttl":"V1","employer":"Mistral AI","title":"Applied AI, Forward Deployed Machine Learning Engineer - Palo Alto","url":"https://jobs.lever.co/mistral/0b476d3a-5f0c-4dda-9a5e-bd5ed8515328","job_id":"0b476d3a-5f0c-4dda-9a5e-bd5ed8515328","seen":"2026-11-13","location":"Palo Alto, CA","remote":"on-site","seniority":"mid-senior","years":"2+","degree":"PhD or master's in AI or data science","must":["'PhD / master in AI / data science'","LLM fine-tuning, advanced RAG or agentic use cases (paraphrase)","Python, PyTorch, LangChain-style frameworks and vector databases (paraphrase)"],"nice":["open-source LLM contributions","customer engineer, FDE, sales engineer, solutions architect or TPM background"],"pay":null,"ats":"Lever","note":"Read in full; open 2026-11-13; includes pre-sales calls; benefits list visa sponsorship"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S10"],"as_of":"2026-08-17","ttl":"V1","employer":"Mistral AI","title":"Lead Applied AI Engineer","url":"https://jobs.headline.com/companies/mistral-ai-2/jobs/90169162-lead-applied-ai-engineer","job_id":"90169162","seen":"2026-11-13","location":"Seoul, South Korea","remote":"unknown","seniority":"lead","years":"7-10+","degree":"PhD or master's, or 'self-made'","must":["7-10+ years as a technical individual contributor on AI products (paraphrase)","FDE, staff ML engineer or staff data scientist experience (paraphrase)"],"nice":null,"pay":null,"ats":"Lever","note":"Aggregator extract; posted 2026-08-17; liveness not verified"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S11"],"as_of":"2026-11-13","ttl":"V1","employer":"Scale AI","title":"Frontier Agents Engineer (page body: Applied AI Engineer, Enterprise)","url":"https://job-boards.greenhouse.io/scaleai/jobs/4536659005","job_id":"4536659005","seen":"2026-11-13","location":"London, UK","remote":"office 2-3 days per week","seniority":"mid","years":null,"degree":"bachelor's in computer science, maths or a quantitative field, or equivalent engineering background","must":["'gathering business requirements'","Python with numpy and pandas (paraphrase)","AWS or GCP and ML in cloud environments (paraphrase)"],"nice":["production GenAI applications","knowledge of LLM strengths and weaknesses"],"pay":null,"ats":"Greenhouse","note":"Read in full; open 2026-11-13; page title differs from body (rename)"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-05","ttl":"V1","employer":"Scale AI","title":"Senior Applied AI Engineer","url":"https://job-boards.greenhouse.io/scaleai/jobs/4751081005","job_id":"4751081005","seen":"2026-11-13","location":"London, UK","remote":"unknown","seniority":"senior","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-05); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-05","ttl":"V1","employer":"Scale AI","title":"Staff Applied AI Engineer","url":"https://job-boards.greenhouse.io/scaleai/jobs/4720050005","job_id":"4720050005","seen":"2026-11-13","location":"London, UK","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-05); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-06","ttl":"V1","employer":"Scale AI","title":"Applied AI Engineer","url":"https://job-boards.greenhouse.io/scaleai/jobs/4751059005","job_id":"4751059005","seen":"2026-11-13","location":"Kuwait City, Kuwait","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-06); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S15"],"as_of":"2026-11-13","ttl":"V1","employer":"Snorkel AI","title":"Applied AI Engineer - Enterprise Solutions","url":"https://job-boards.greenhouse.io/snorkelai/jobs/5709067004","job_id":"5709067004","seen":"2026-11-13","location":"New York City, NY; San Francisco, CA; US remote","remote":"hybrid, with a remote option","seniority":"mid","years":"3+ (stated as customer-facing experience)","degree":"B.S. in a quantitative field or comparable degree or experience","must":["'customer-facing experience in the design and implementation of AI/ML solutions'","RAG, fine-tuning, prompt recipes, agentic workflows and evaluation workflows (paraphrase)","Python with FastAPI, pydantic and pytest (paraphrase)"],"nice":null,"pay":{"lo":175000,"hi":300000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Read in full; open 2026-11-13; listed 2026-06-26; OTE plus options; travel up to 25%"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13","S16"],"as_of":"2026-11-11","ttl":"V1","employer":"Snorkel AI","title":"Staff Applied AI Engineer - Pre-Sales","url":"https://job-boards.greenhouse.io/snorkelai/jobs/6255083004","job_id":"6255083004","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":230000,"hi":360000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Listing-level (listed 2026-11-11); pre-sales variant; pay from a Built In copy of the Staff Pre-Sales posting, ID match unverified"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13","S16"],"as_of":"2026-11-11","ttl":"V1","employer":"Snorkel AI","title":"Senior/Staff Applied AI Engineer - Enterprise AI Solutions","url":"https://job-boards.greenhouse.io/snorkelai/jobs/6204368004","job_id":"6204368004","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-11); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-09","ttl":"V1","employer":"AssemblyAI","title":"Applied AI Engineer","url":"https://job-boards.greenhouse.io/assemblyai/jobs/4752669005","job_id":"4752669005","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-09); fetch blocked; a separate AssemblyAI copy shows remote US, senior, $195K-$250K but its ID is unmatched [S47]"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-09","ttl":"V1","employer":"AssemblyAI","title":"Enterprise Applied AI Engineer","url":"https://job-boards.greenhouse.io/assemblyai/jobs/4752670005","job_id":"4752670005","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-09); body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-03","ttl":"V1","employer":"Concurrence","title":"Staff Applied AI Engineer (Forward Deployed) [NYC or SF]","url":"https://jobs.ashbyhq.com/concurrence/66758675-0c38-4b68-a1f1-1ca0fbbcc289","job_id":"66758675-0c38-4b68-a1f1-1ca0fbbcc289","seen":"2026-11-13","location":"New York City or San Francisco","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-03); a Senior variant is also listed; body not opened"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-10","ttl":"V1","employer":"Pika","title":"Applied AI Engineer, Creative Experiences","url":"https://jobs.ashbyhq.com/pika/b075e6fb-df01-4eac-9437-1c1db97ea881","job_id":"b075e6fb-df01-4eac-9437-1c1db97ea881","seen":"2026-11-13","location":"Palo Alto, CA","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-10); variant not determinable"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-09","ttl":"V1","employer":"Crusoe","title":"Staff Applied AI Engineer","url":"https://jobs.ashbyhq.com/Crusoe/6d02f4e8-7320-42e1-9b6b-cc1b436604b7","job_id":"6d02f4e8-7320-42e1-9b6b-cc1b436604b7","seen":"2026-11-13","location":"Tel Aviv, Israel","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby","note":"Listing-level (listed 2026-11-09); variant not determinable"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-11","ttl":"V1","employer":"General Matter","title":"Applied AI Engineer","url":"https://job-boards.greenhouse.io/generalmatter/jobs/5190258008","job_id":"5190258008","seen":"2026-11-13","location":"Los Angeles, CA","remote":"unknown","seniority":"unspecified","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-11); variant not determinable"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S13"],"as_of":"2026-11-10","ttl":"V1","employer":"Flexport","title":"Staff Applied AI Engineer, Autonomous Supply Chains","url":"https://job-boards.greenhouse.io/flexport/jobs/7311883","job_id":"7311883","seen":"2026-11-13","location":"multiple locations","remote":"unknown","seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Greenhouse","note":"Listing-level (listed 2026-11-10); a Senior variant is also listed; variant not determinable"}
{"type":"jd","role":"applied-ai-engineer","grade":"B","src":["S24"],"as_of":"2026-09-14","ttl":"V1","employer":"NVIDIA","title":"Senior Applied AI Engineer","url":"https://www.talentify.io/senior-applied-ai-engineer-santa-clara-california-us-nvidia","job_id":null,"seen":"2026-11-13","location":"Santa Clara, CA","remote":"unknown","seniority":"senior","years":null,"degree":null,"must":["builds AI systems that improve engineering productivity and software quality (paraphrase)"],"nice":null,"pay":null,"ats":"Workday","note":"Aggregator extract; posted 2026-09-14; internal-productivity variant; other NVIDIA Applied AI Engineer postings show $152K-$287.5K"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S50"],"as_of":"2026-11-13","ttl":"V1","employer":"Atomicwork","title":"Applied AI Engineer","url":"https://www.atomicwork.com/career/4405099008","job_id":"4405099008","seen":"2026-11-13","location":"United States (US office; city not stated)","remote":"office-based","seniority":"mid","years":null,"degree":"no specific degree required (paraphrase)","must":["Python with PyTorch or TensorFlow (paraphrase)","semantic search, RAG or multi-agent workflows (paraphrase)","evaluation pipelines and metrics (paraphrase)"],"nice":null,"pay":null,"ats":"Greenhouse","note":"Read in full on the employer's own page; open 2026-11-13; no posting date shown; internal product variant; a Greenhouse board copy exists under ID 5073381008"}
{"type":"jd","role":"applied-ai-engineer","grade":"A","src":["S17"],"as_of":"2026-11-13","ttl":"V1","employer":"Siemens Technology and Services Private Limited","title":"Applied AI Engineer","url":"https://jobs.siemens.com/fr_FR/externaljobs/JobDetail/501447","job_id":"501447","seen":"2026-11-13","location":"Bangalore, Karnataka, India","remote":"on-site only","seniority":"mid (system label: entry)","years":"3-5; 1-2 with LLMs in production","degree":"bachelor's or master's in computer science or engineering (paraphrase)","must":["3-5 years in ML/AI engineering (paraphrase)","LLM applications with RAG, prompt engineering and evaluation (paraphrase)","LangChain, LlamaIndex or Semantic Kernel; hallucination mitigation (paraphrase)"],"nice":null,"pay":null,"ats":null,"note":"Read in full; open 2026-11-13; posted 2026-04-03; the level label conflicts with the years asked"}
{"type":"jd","role":"applied-ai-engineer","grade":"C","src":["S27"],"as_of":"2026-10-15","ttl":"V1","employer":"Deloitte","title":"Applied AI Engineer II","url":"https://www.airtribe.live/jobs/software-developer/applied-ai-engineer-software-engineer-ii-at-deloitte-XM2UXHZA3XUO","job_id":"372354","seen":"2026-11-13","location":"Bengaluru, India","remote":"unknown","seniority":"mid","years":null,"degree":null,"must":["full-stack product engineering with GenAI and agentic features (paraphrase)"],"nice":null,"pay":null,"ats":null,"note":"Aggregator copy; requisition 372354; the snapshot is dated only to October 2026 (as_of is approximate); body not opened"}
```

### Skill-signal records (n = 10 full reads; grade M)

```jsonl
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"python","n":10,"source_kind":"jd-sample","count":9,"share":0.9,"tier_hint":"Must","note":"Absent only in the Anthropic Life Sciences text"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"llm_apis","n":10,"source_kind":"jd-sample","count":5,"share":0.5,"tier_hint":"Must","note":"Vendor API or platform named in 4, tool calling in 1; implied in the rest"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"rag","n":10,"source_kind":"jd-sample","count":5,"share":0.5,"tier_hint":"Important","note":"5 of 6 non-Anthropic reads, 0 of 4 Anthropic; Must for vendor, startup and enterprise variants"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"agents","n":10,"source_kind":"jd-sample","count":9,"share":0.9,"tier_hint":"Must","note":"Absent only in the Anthropic Architect text"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"customer_scoping","n":10,"source_kind":"jd-sample","count":9,"share":0.9,"tier_hint":"Must","note":"Absent only at Atomicwork (internal product variant)"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"evals","n":10,"source_kind":"jd-sample","count":8,"share":0.8,"tier_hint":"Must","note":"Absent in Mistral Prototyping and Scale"}
{"type":"skill_signal","grade":"M","src":["S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"guardrails","n":10,"source_kind":"jd-sample","count":1,"share":0.1,"tier_hint":"Should","note":"Siemens only"}
{"type":"skill_signal","grade":"M","src":["S2","S3","S4","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"prompt_context","n":10,"source_kind":"jd-sample","count":4,"share":0.4,"tier_hint":"Important","note":"Context engineering at Anthropic x3; prompt design at Siemens"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S8","S15","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"prompt_engineering","n":10,"source_kind":"jd-sample","count":6,"share":0.6,"tier_hint":"Important","note":"Union with prompt_context is 7 of 10"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"tech_writing","n":10,"source_kind":"jd-sample","count":4,"share":0.4,"tier_hint":"Important","note":"Content, documentation and white-paper duties at Anthropic x3 and Siemens"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"retrieval_quality","n":10,"source_kind":"jd-sample","count":0,"share":0.0,"tier_hint":"Should","note":"No hybrid search, reranking or recall wording; may still be tested in interviews"}
{"type":"skill_signal","grade":"M","src":["S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"ml_fundamentals","n":10,"source_kind":"jd-sample","count":5,"share":0.5,"tier_hint":"Important","note":"Mistral Palo Alto, Scale, Snorkel, Siemens, Atomicwork; none at Anthropic"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"generative_ai","n":10,"source_kind":"jd-sample","count":10,"share":1.0,"tier_hint":"Must","note":"Definitional; does not discriminate between candidates"}
{"type":"skill_signal","grade":"M","src":["S7","S11","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"cloud","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Should","note":"Nice-to-have at Mistral Prototyping; AWS or GCP at Scale; generic at Atomicwork"}
{"type":"skill_signal","grade":"M","src":["S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"git_ci","n":10,"source_kind":"jd-sample","count":1,"share":0.1,"tier_hint":"Optional","note":"Version control at Atomicwork only"}
{"type":"skill_signal","grade":"M","src":["S8","S15","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"vector_search","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Should","note":"Mistral Palo Alto, Snorkel, Atomicwork"}
{"type":"skill_signal","grade":"M","src":["S1","S3","S7","S11"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"c1_pragmatism","n":10,"source_kind":"jd-sample","count":4,"share":0.4,"tier_hint":"Important","note":"Ambiguity wording at Anthropic Enterprise and Life Sciences, Mistral Prototyping, Scale"}
{"type":"skill_signal","grade":"M","src":["S15"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"c2_tradeoffs","n":10,"source_kind":"jd-sample","count":1,"share":0.1,"tier_hint":"Should","note":"Snorkel names strengths and weaknesses of approaches; general communication is in 7 of 10"}
{"type":"skill_signal","grade":"M","src":["S7","S11","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"c3_ownership","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Should","note":"Ownership wording only; no incident or on-call wording"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S4","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"c4_responsible_ai","n":10,"source_kind":"jd-sample","count":4,"share":0.4,"tier_hint":"Important","note":"Anthropic x3 (safe and beneficial AI wording) and Siemens (compliance and governance)"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S4","S7","S8","S15","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"new:technical_communication","n":10,"source_kind":"jd-sample","count":7,"share":0.7,"tier_hint":"Important","note":"Explicit communication or presentation requirement"}
{"type":"skill_signal","grade":"M","src":["S2","S4","S15"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"new:customer_facing_experience","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Important","note":"Required at 3; an alternative or nice-to-have at 3 more"}
{"type":"skill_signal","grade":"M","src":["S1","S3"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"new:mcp","n":10,"source_kind":"jd-sample","count":2,"share":0.2,"tier_hint":"Should","note":"Anthropic only"}
{"type":"skill_signal","grade":"M","src":["S8","S15","S17"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"new:agent_frameworks_named","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Should","note":"LangChain, LlamaIndex, LangGraph, CrewAI, Semantic Kernel"}
{"type":"skill_signal","grade":"M","src":["S8","S15","S50"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","skill":"new:fine_tuning","n":10,"source_kind":"jd-sample","count":3,"share":0.3,"tier_hint":"Should","note":"Mistral Palo Alto, Snorkel, Atomicwork"}
```

### Pay records

```jsonl
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-11","ttl":"V3","role":"applied-ai-engineer","location":"US","stat":"p25","value":200000,"currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Applied AI Engineer title page","n":null,"note":"n not shown; self-reported"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-11","ttl":"V3","role":"applied-ai-engineer","location":"US","stat":"p50","value":250000,"currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Applied AI Engineer title page","n":null,"note":"n not shown; self-reported; pooled across employers"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-11","ttl":"V3","role":"applied-ai-engineer","location":"US","stat":"p75","value":475000,"currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Applied AI Engineer title page","n":null,"note":"n not shown; self-reported"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-11-11","ttl":"V3","role":"applied-ai-engineer","location":"US","stat":"p90","value":505000,"currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Applied AI Engineer title page","n":null,"note":"The same page showed $605K in a snapshot dated 2026-10-04, so the upper tail is unstable"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, New York, remote)","stat":"range","lo":197000,"hi":278000,"currency":"USD","period":"year","basis":"base","source_name":"OpenAI Applied AI Engineer, Enterprise","employer_type":"frontier-lab","n":1,"note":"Plus equity; undated-indexed"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, Seattle)","stat":"range","lo":251000,"hi":278000,"currency":"USD","period":"year","basis":"base","source_name":"OpenAI Applied AI Engineer, API Platform, Digital Natives","employer_type":"frontier-lab","level":"senior","n":1,"note":"Plus equity; undated-indexed"}
{"type":"pay","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, New York)","stat":"range","lo":200000,"hi":320000,"currency":"USD","period":"year","basis":"base","source_name":"Anthropic Applied AI Engineer, Enterprise","employer_type":"frontier-lab","n":1,"note":"Basis not stated and may be OTE; COI"}
{"type":"pay","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, New York)","stat":"range","lo":280000,"hi":320000,"currency":"USD","period":"year","basis":"base","source_name":"Anthropic Applied AI Engineer, Life Sciences","employer_type":"frontier-lab","n":1,"note":"Department is Sales so the range may be OTE; COI"}
{"type":"pay","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, New York)","stat":"range","lo":240000,"hi":315000,"currency":"USD","period":"year","basis":"base","source_name":"Anthropic Applied AI Architect, Startups","employer_type":"frontier-lab","n":1,"note":"Pre-sales variant; basis not stated; COI"}
{"type":"pay","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"UK (London)","stat":"range","lo":225000,"hi":240000,"currency":"GBP","period":"year","basis":"base","source_name":"Anthropic Applied AI Engineer, London","employer_type":"frontier-lab","n":1,"note":"COI"}
{"type":"pay","grade":"A","src":["S15"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (New York, San Francisco, remote)","stat":"range","lo":175000,"hi":300000,"currency":"USD","period":"year","basis":"tc","source_name":"Snorkel Applied AI Engineer - Enterprise Solutions","employer_type":"ai-startup","n":1,"note":"Posting states OTE plus options"}
{"type":"pay","grade":"B","src":["S12"],"as_of":"2026-02-23","ttl":"V3","role":"applied-ai-engineer","location":"US (San Francisco, New York)","stat":"range","lo":168200,"hi":248500,"currency":"USD","period":"year","basis":"base","source_name":"Scale AI Applied AI Engineer, Enterprise GenAI (Accel listing)","employer_type":"ai-startup","n":1,"note":"Listing dated 2026-02-23, outside the window; plus equity"}
{"type":"pay","grade":"B","src":["S47"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (remote)","stat":"range","lo":195000,"hi":250000,"currency":"USD","period":"year","basis":"base","source_name":"AssemblyAI Applied AI Engineer (Built In copy)","employer_type":"ai-startup","level":"senior","n":1,"note":"Posting ID not matched to the listing-level record"}
{"type":"pay","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US","stat":"range","lo":152000,"hi":287500,"currency":"USD","period":"year","basis":"base","source_name":"NVIDIA Applied AI Engineer postings (aggregator copies)","employer_type":"big-tech","n":1,"note":"Internal variant; plus equity"}
{"type":"pay","grade":"B","src":["S49"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US (remote)","stat":"range","lo":176000,"hi":224000,"currency":"USD","period":"year","basis":"base","source_name":"OpenAI AI Deployment Engineer (alias title; Inference Jobs listing)","employer_type":"frontier-lab","n":1,"note":"Undated listing; alias title, not the exact title"}
{"type":"pay","grade":"M","src":["S1","S3","S4","S18"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"US labs","stat":"p50","value":264500,"currency":"USD","period":"year","basis":"base","source_name":"Median of posted-range midpoints: OpenAI x2 and Anthropic x3","employer_type":"frontier-lab","n":5,"note":"Midpoints 237.5K, 260K, 264.5K, 277.5K, 300K; Anthropic ranges may be OTE"}
{"type":"pay","grade":"M","src":["S40"],"as_of":"2026-03-31","ttl":"V4","role":"applied-ai-engineer","location":"US","stat":"p50","value":185480,"currency":"USD","period":"year","basis":"base","source_name":"LCA offered wages, exact title, via aggregators of DOL data","n":6,"note":"Offered wage, not pay; values 172,000; 175,000; 180,960; 190,000; 214,000; 295,000; includes one withdrawn filing and one filed in 2024"}
{"type":"pay","grade":"C","src":["S44"],"as_of":"2026-10-01","ttl":"V3","role":"applied-ai-engineer","location":"India","stat":"mean","value":1200000,"currency":"INR","period":"year","basis":"tc","source_name":"Weekday, citing Glassdoor India, AI Engineer (feeder title)","n":null,"note":"About 12 LPA; other pages cite about 10 LPA; title is AI Engineer, not Applied AI Engineer"}
{"type":"pay","grade":"D","src":["S44"],"as_of":"2026-11-13","ttl":"V3","role":"applied-ai-engineer","location":"India","stat":"range","lo":1340000,"hi":1680000,"currency":"INR","period":"year","basis":"base","source_name":"aijobs.net model estimate, mid-level Applied AI Engineer","level":"mid","n":0,"note":"Estimate, not a posted range"}
{"type":"pay","grade":"B","src":["S52"],"as_of":"2026-07-18","ttl":"V3","role":"applied-ai-engineer","location":"India (Greater Bengaluru)","stat":"p25","value":3781292,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi Software Engineer, Greater Bengaluru (proxy)","n":null,"note":"Proxy for the software-engineer family; the URL path suggests a senior-level page and the level scope is unconfirmed"}
{"type":"pay","grade":"B","src":["S52"],"as_of":"2026-07-18","ttl":"V3","role":"applied-ai-engineer","location":"India (Greater Bengaluru)","stat":"p50","value":5540248,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi Software Engineer, Greater Bengaluru (proxy)","n":null,"note":"Proxy; self-reported; skewed to premium employers"}
{"type":"pay","grade":"B","src":["S52"],"as_of":"2026-07-18","ttl":"V3","role":"applied-ai-engineer","location":"India (Greater Bengaluru)","stat":"p75","value":7954873,"currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi Software Engineer, Greater Bengaluru (proxy)","n":null,"note":"Proxy; level scope unconfirmed"}
```

### Measure records

```jsonl
{"type":"measure","grade":"B","src":["S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:applied-ai-engineer","measure":"open AI Engineer roles at AI startups (category)","unit":"postings","value":352,"n":352,"method":"Fast AI Jobs role page, deduplicated from company career pages","region":"global","note":"188 companies; category count, not an exact-title count"}
{"type":"measure","grade":"B","src":["S14"],"as_of":"2026-07-30","ttl":"V1","subject":"role:applied-ai-engineer","measure":"open AI Engineer roles at AI startups (earlier snapshot)","unit":"postings","value":275,"n":275,"method":"Fast AI Jobs role page snapshot","region":"global","note":"170 companies; newest row dated 2026-07-30"}
{"type":"measure","grade":"M","src":["S13","S14"],"as_of":"2026-11-11","ttl":"V1","subject":"role:applied-ai-engineer","measure":"change in category count between the two snapshots","unit":"percent","value":28,"method":"352 divided by 275, minus 1","region":"global","note":"About 3.5 months apart; snapshot dates are approximate"}
{"type":"measure","grade":"M","src":["S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:applied-ai-engineer","measure":"share of the newest 50 AI Engineer rows with 'Applied AI Engineer' in the title","unit":"share of rows","value":0.42,"n":50,"method":"manual count of the first 50 rows (21)","region":"global","note":"OpenAI 6, Scale 4, Snorkel 2, AssemblyAI 2, Flexport 2, Concurrence 2, General Matter 1, Pika 1, Crusoe 1; newest rows over-represent bulk posters"}
{"type":"measure","grade":"M","src":["S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:applied-ai-engineer","measure":"share of the newest 50 rows with FDE or Deployed AI Engineer titles","unit":"share of rows","value":0.22,"n":50,"method":"manual count (11)","region":"global","note":"Turing 4, Databricks 2, Toloka 2, Helsing, Avathon, Traversal"}
{"type":"measure","grade":"M","src":["S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:applied-ai-engineer","measure":"entry-level share among the 21 exact-title rows","unit":"share of rows","value":0,"n":21,"method":"title wording: staff 6, senior 4, unqualified 11, entry 0","region":"global","note":"Unqualified titles may still be mid level"}
{"type":"measure","grade":"M","src":["S13","S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"OpenAI distinct 'Applied AI Engineer' or 'Partner Applied AI Engineer' titles seen","unit":"titles (lower bound)","value":20,"method":"Fast AI Jobs listing plus openai.com search extracts; not a census","region":"global","note":"Liveness unverified outside the 2026-11-02 to 2026-11-11 listing; excludes Codex Core Agent"}
{"type":"measure","grade":"A","src":["S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"Anthropic careers board, all roles","unit":"jobs","value":670,"n":670,"method":"Greenhouse board index","region":"global","note":"All departments; COI"}
{"type":"measure","grade":"C","src":["S33"],"as_of":"2026-08-01","ttl":"V1","subject":"role:applied-ai-engineer","measure":"Anthropic Applied AI openings (approximate)","unit":"openings","value":20,"method":"single-source report","region":"global","note":"Reported for early August 2026; not verified"}
{"type":"measure","grade":"C","src":["S31"],"as_of":"2025-04-30","ttl":"V1","subject":"role:applied-ai-engineer","measure":"FDE-family postings on Indeed, US","unit":"postings","value":643,"method":"skai.io citing Indeed","region":"US","note":"Family-level, not the exact title"}
{"type":"measure","grade":"C","src":["S31"],"as_of":"2026-04-30","ttl":"V1","subject":"role:applied-ai-engineer","measure":"FDE-family postings on Indeed, US","unit":"postings","value":5330,"method":"skai.io citing Indeed","region":"US","note":"Family-level; about +729% on April 2025"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-03","ttl":"V1","subject":"role:applied-ai-engineer","measure":"growth in forward-deployed engineer postings, Jan-Aug 2026 against the same period of 2025","unit":"percent (reported as more than 1,000%)","value":1000,"method":"Lightcast via Fortune","region":"US (as reported)","note":"Family-level; Fortune also cites more than 4,600% against 2023"}
{"type":"measure","grade":"B","src":["S29"],"as_of":"2026-06-30","ttl":"V1","subject":"role:applied-ai-engineer","measure":"India FDE postings, June 2026 against June 2025","unit":"multiple","value":19,"method":"Indeed Hiring Lab via IANS","region":"India","note":"Reported as nearly 19x; moderating in later months; family-level"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-10-11","ttl":"V3","subject":"role:applied-ai-engineer","measure":"entry-level share of AI-titled postings","unit":"share","value":0.164,"method":"JobsPipe aggregate","region":"global","note":"Against 38.3% across all postings; population is AI-titled roles, not this title"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-10-11","ttl":"V3","subject":"role:applied-ai-engineer","measure":"entry-level share of all postings (JobsPipe)","unit":"share","value":0.383,"method":"JobsPipe aggregate","region":"global","note":"Comparison base"}
{"type":"measure","grade":"B","src":["S21"],"as_of":"2026-11-13","ttl":"V3","subject":"role:applied-ai-engineer","measure":"remote share of AI Engineer postings (JobsPipe)","unit":"share","value":0.11,"method":"JobsPipe AI Engineer job-description page","region":"global","note":"AI Engineer population, not the exact title"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S18","S50"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"share of postings with a visible work mode that offer a remote option","unit":"share","value":0.23,"n":13,"method":"10 full reads plus OpenAI Enterprise, Delhi and Partner-AWS extracts; 3 offer remote (Snorkel, OpenAI Enterprise, OpenAI Partner-AWS)","region":"global","note":"None is fully remote worldwide"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S5","S7","S8","S9","S11","S15","S17","S23","S25","S50"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"share of fetched search-indexed postings that were closed","unit":"share","value":0.29,"n":14,"method":"fetched each page on 2026-11-13: 10 live, 4 closed (EY London, Anthropic 5073277008, Mistral Fullstack EMEA, Google Cloud FDE IV)","region":"global","note":"Not a random sample of postings"}
{"type":"measure","grade":"M","src":["S13","S18","S10","S12","S16"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"sample share with staff or lead in the title","unit":"share","value":0.19,"n":36,"method":"title wording: staff or lead 7, senior 2, unqualified 27, entry 0","region":"global","note":"Entry-level share is 0 of 36"}
{"type":"measure","grade":"M","src":["S1","S13","S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"sample share at frontier labs","unit":"share","value":0.5,"n":36,"method":"Anthropic 5, OpenAI 10, Mistral 3","region":"global","note":"AI startups 14 (0.39); big-tech, enterprise, GCC and IT services 4 (0.11)"}
{"type":"measure","grade":"M","src":["S1","S13","S18"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"sample share located in the US","unit":"share","value":0.56,"n":36,"method":"20 US; UK 5; Europe outside UK 2; India 4; APAC 1; Middle East and Israel 2; unspecified 2","region":"global","note":"UK 0.14; India 0.11"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S7","S8","S15","S17"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"median stated minimum years of experience","unit":"years","value":3,"n":8,"method":"values 2, 2, 3, 3, 3, 4, 4, 4; Scale and Atomicwork state none","region":"global","note":"Labs 3-4+; Mistral 2+"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"full reads stating a bachelor's degree or equivalent","unit":"share","value":0.7,"n":10,"method":"7 of 10; no degree requirement 1; none stated 1; PhD or master's required 1 (Mistral Palo Alto)","region":"global","note":"None requires a PhD except Mistral Palo Alto"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S7","S8","S11","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V1","subject":"role:applied-ai-engineer","measure":"full reads naming any certification","unit":"postings","value":0,"n":10,"method":"manual read of requirements and nice-to-haves","region":"global","note":"JPMorgan boilerplate mentions 'formal training or certification' generically and is outside the sample"}
{"type":"measure","grade":"B","src":["S41"],"as_of":"2026-06-30","ttl":"V4","subject":"role:applied-ai-engineer","measure":"certified H-1B LCAs for the AI/ML engineer family","unit":"certified LCAs","value":8275,"method":"careery.pro aggregation of DOL data, FY2025 to Q3 FY2026","region":"US","note":"Median offered wage $167,485 across 2,693 employers; feeder family, not the exact title"}
{"type":"measure","grade":"B","src":["S41"],"as_of":"2026-06-30","ttl":"V4","subject":"role:applied-ai-engineer","measure":"certified LCAs for OpenAI OpCo","unit":"certified LCAs","value":311,"method":"careery.pro aggregation of DOL data","region":"US","note":"Median offered wage $270,000; titles are mostly other than Applied AI Engineer"}
{"type":"measure","grade":"C","src":["S42"],"as_of":"2026-06-10","ttl":"V3","subject":"role:applied-ai-engineer","measure":"Anthropic certified H-1B roles in the first half of fiscal 2026 (as reported)","unit":"roles","value":80,"method":"Business Insider via BusinessToday","region":"US","note":"All titles; not the exact title"}
```

### Interview-loop records

```jsonl
{"type":"loop","grade":"C","src":["S34","S35","S36"],"as_of":"2026-11-13","ttl":"V3","employer":"Anthropic","track":"application","stages":["application with a 'Why Anthropic' essay","recruiter screen","hiring-manager call","take-home, online assessment or live build","customer-conversation simulation (single-vendor claim)","virtual onsite with system design","values round"],"formats":["video calls","online coding platform or notebook (reported)"],"ai_policy":"Anthropic's own page: write application drafts yourself before refining with Claude; take-homes without Claude unless indicated; live interviews with no AI unless indicated; AI is encouraged for interview preparation","take_home":"reported for some roles","duration":"4-6 weeks (guides)","note":"Policy is from Anthropic's page (A, COI); stages are from prep vendors (C, COI)"}
{"type":"loop","grade":"C","src":["S37","S38"],"as_of":"2026-11-13","ttl":"V3","employer":"OpenAI","track":"application","stages":["recruiter or hiring-manager screen","coding and system-design screens","take-home or solution design for FDE-type roles","virtual onsite of 4-6 rounds with project walkthrough, behavioural and customer-scenario rounds","leadership conversations"],"formats":["video calls"],"ai_policy":"varies by team; applied loops resemble standard senior engineering loops","take_home":"reported for FDE-type roles","duration":"3-6 weeks (guides)","note":"Guides cover SWE, Solutions Architect, FDE and 'GenAI Engineer' loops, not the exact title; prep vendors carry COI"}
{"type":"loop","grade":"D","src":["S51"],"as_of":"2025-10-01","ttl":"V3","employer":"Mistral AI","track":"application","stages":["HR or talent-partner call (already technical)","coding round (LeetCode-medium reported)","team-lead or senior AI engineer round","deep technical use-case round","customer-success round"],"formats":null,"ai_policy":null,"take_home":"reported for many senior roles in a guide (C)","duration":"about 5 rounds","note":"Single candidate reports dated 2025-08-01 and 2025-10-01; one 2024 report is older than the window"}
```

### Practice records

```jsonl
{"type":"practice","grade":"P","src":["S2","S4","S15"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Lead each role entry with a customer-facing delivery line","claim":"Postings require or prefer customer-facing delivery experience","evidence":"Required in 3 of 10 full reads; scoping or requirements work named in 9 of 10","verdict":"use","risk":"Padding with pre-sales claims you cannot discuss in an interview","note":"Pattern, not an achievement"}
{"type":"practice","grade":"P","src":["S1","S2","S3","S4","S8","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Evidence line for evaluation: built <suite type> (golden set, graders, CI gate) for <system> that caught <n> regressions before release","claim":"Evaluation is named in 8 of 10 full reads","evidence":"Anthropic x4, Mistral Palo Alto, Snorkel, Siemens, Atomicwork","verdict":"use-with-care","risk":"Invented metrics; use only figures you can defend","note":"Pattern with placeholders"}
{"type":"practice","grade":"P","src":["S1","S2","S7"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Evidence line for production delivery: shipped <LLM feature> to <N> users and tracked latency, cost and quality against <target>","claim":"Postings ask for production experience, not prototypes","evidence":"Anthropic 'Production experience' wording; Mistral asks for systems built end to end, not just prototypes","verdict":"use","risk":"Listing demos as production","note":"Pattern with placeholders"}
{"type":"practice","grade":"P","src":["S1","S2","S3","S7","S8","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Evidence line for agents and tool use: designed an agent loop with tool permissions, step limits and failure handling for <workflow>","claim":"Agents appear in 9 of 10 full reads","evidence":"All except Anthropic Architect","verdict":"use-with-care","risk":"Framework name-dropping without design decisions to discuss","note":"Pattern with placeholders"}
{"type":"practice","grade":"P","src":["S7","S8","S15","S17","S50"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Evidence line for RAG when targeting vendor, startup or enterprise postings: built retrieval over <corpus> and measured answer quality on a <n>-item test set","claim":"RAG is named in 5 of 6 non-Anthropic reads and in none of Anthropic's four","evidence":"Mistral x2, Snorkel, Siemens, Atomicwork","verdict":"use-with-care","risk":"Over-weighting RAG for lab postings that stress context engineering and evaluation","note":"Pattern with placeholders"}
{"type":"practice","grade":"P","src":["S1","S3","S7","S8","S18"],"as_of":"2026-11-13","ttl":"V3","area":"portfolio","tactic":"Reference implementation with an evaluation suite and a short write-up for a realistic customer workflow","claim":"Postings ask for shipped systems, evaluation and public technical content","evidence":"Anthropic builder-credibility and content duties; Mistral open-source nice-to-haves; OpenAI Cookbook mention","verdict":"use","risk":"Chatbot demos with no external users; no outcome data ranks proof types"}
{"type":"practice","grade":"P","src":["S1","S3","S18"],"as_of":"2026-11-13","ttl":"V3","area":"portfolio","tactic":"Publish an MCP server or cookbook-style contribution for a domain data source","claim":"MCP appears in 2 of 10 reads (Anthropic); OpenAI names Cookbook contributions","evidence":"Anthropic Enterprise and Life Sciences; OpenAI Codex Applied AI posting","verdict":"use-with-care","risk":"Employer-specific signal; may not transfer"}
{"type":"practice","grade":"P","src":["S7","S8"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"List hackathons, AI competitions and open-source LLM contributions","claim":"Mistral lists them as nice-to-haves","evidence":"Mistral Prototyping and Palo Alto postings","verdict":"use-with-care","risk":"Weak signal outside Mistral-style postings"}
{"type":"practice","grade":"P","src":["S45"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Lead the headline with a cloud certificate","claim":"No full read names a certificate and the AWS exam is optional for this role","evidence":"0 of 10 postings; AWS guide describes a target candidate with production experience","verdict":"untested","risk":"May read as a tutorial-led profile for lab postings; may help at services firms"}
{"type":"practice","grade":"P","src":["S5","S9","S13","S23","S25"],"as_of":"2026-11-13","ttl":"V3","area":"job search","tactic":"Search the title family and confirm the posting is open on the employer's own board before applying","claim":"Aliases are many and 4 of 14 fetched search-indexed postings were closed","evidence":"Closed: EY, Anthropic 5073277008, Mistral Fullstack EMEA, Google Cloud FDE IV","verdict":"use","risk":"Time spent on listings that look live in search results"}
{"type":"practice","grade":"P","src":["S34","S35","S38"],"as_of":"2026-11-13","ttl":"V3","area":"interview","tactic":"Prepare a customer-discovery and scoping walkthrough as well as coding and system design","claim":"Guides report a customer-conversation round at Anthropic and a customer-scenario round in OpenAI SA and FDE loops","evidence":"Prep-vendor guides","verdict":"use-with-care","risk":"Guides are vendor-written (COI) and cover neighbouring titles"}
{"type":"practice","grade":"P","src":["S36"],"as_of":"2026-11-13","ttl":"V3","area":"interview","tactic":"Do not use AI assistants in Anthropic live rounds or take-homes unless the instructions say so","claim":"Anthropic's candidate guidance bars AI in live interviews unless indicated and in take-homes without Claude unless indicated","evidence":"Anthropic's own page","verdict":"use","risk":"Policies differ by employer and role; confirm in writing before each stage"}
```

### Credential record

```jsonl
{"type":"credential","grade":"A","src":["S45","S46"],"as_of":"2026-11-13","ttl":"V2","id":"aws_aip_c01","name":"AWS Certified Generative AI Developer - Professional","issuer":"Amazon Web Services","level":"professional","state":"active","url":"https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html","exam_code":"AIP-C01","format":"multiple choice and multiple response","items":75,"passing":"750 on a scaled 100-1,000 score","prerequisites":"none formal; the guide describes a target candidate with 2+ years building production applications on AWS or open source and 1 year of hands-on GenAI work","domains":[{"name":"Foundation-model integration, data management and compliance","weight":0.31},{"name":"Implementation and integration","weight":0.26},{"name":"AI safety, security and governance","weight":0.20},{"name":"Operational efficiency","weight":0.12},{"name":"Testing, validation and troubleshooting","weight":0.11}],"channels":["services"],"families":["Applied AI Engineering"],"jd_signal":{"value":0,"unit":"postings naming it","n":10,"region":"global","method":"full reads of the jd-sample"},"note":"75 items are 65 scored plus 10 unscored. The guide page shows no fee or duration; third-party guides report about USD 300 and 170-180 minutes (C). Domain names are paraphrased. Launch date not on the guide page."}
```

### Absence records

```jsonl
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Exact-title posting counts on LinkedIn, Indeed and Glassdoor","searched":"Search extracts and aggregator pages; login and bot walls","note":"Fast AI Jobs (AI startups only) is the only exact-title count obtained"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"A JobsPipe job-description page for Applied AI Engineer","searched":"JobsPipe search and title pages","note":"Only the AI Engineer page exists; its shares match the KB's skill shares"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"OpenAI posting bodies","searched":"openai.com careers pages and Ashby listings","note":"Bot detection blocked fetches; extracts only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"AssemblyAI posting bodies","searched":"Greenhouse and aggregator copies","note":"Fetch blocked; listing-level and aggregator copies only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Enterprise, consultancy and GCC posting bodies on Workday and SuccessFactors","searched":"Searches and one EY fetch","note":"Thin; the EY posting was closed"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Role-specific interview loops at Scale, Google Cloud, Indian GCCs and consultancies","searched":"Interview-prep and candidate-report searches","note":"Not found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posted INR ranges for lab Applied AI Engineer roles","searched":"OpenAI India postings, salary pages, Levels.fyi, aggregators","note":"Not found; only proxies and estimates"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"LCA filings for the exact title at OpenAI and Anthropic","searched":"LCA aggregators","note":"Not found; OpenAI filings are mostly other titles"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Hiring-manager statements on proof of work in a named first-person source","searched":"Search for hiring-manager posts and interviews about the role","note":"Not found; postings only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Published analyses of prior roles of people hired into the role","searched":"Search for career-path analyses","note":"Not found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Non-English postings","searched":"Not searched","note":"WIDEN move not done"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Evidence on tasks within the role being automated by AI tools","searched":"Demand and trend searches","note":"Not found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"DOL LCA primary files","searched":"Not opened","note":"Aggregators used (B)"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posting-specific URLs for three OpenAI rows (API Platform, Partner-AWS, Cyber-Government)","searched":"openai.com search extracts","note":"URLs not retained; the Ashby board root is given in those jd records"}
```
