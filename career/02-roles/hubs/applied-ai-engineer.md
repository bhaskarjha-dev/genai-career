---
id: roles.hub.applied-ai-engineer
title: "Applied AI Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "Applied AI Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-53, T0-01, T0-02, T0-06, T0-14, T0-48, T0-51]
roles: [applied-ai-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Applied AI Engineer

> Customer- and solutions-facing LLM engineering at labs, AI vendors and product firms: reference architectures, production prototypes, evaluation harnesses and production deployment.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Applied AI Engineering | L6 Applications and deployment; also L5 Orchestration and context; planes: Evaluation and quality | Verified (V) | #6 of 24 | #6 of 24 · band A · Monte Carlo rank 6 (P10–P90 4–10) | A2 Deployer |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 5 (4–6.5) | C | 21 of newest 50 Fast AI Jobs AI-Engineer rows (42%) on 2026-11-11 carry 'Applied AI' titles; JobsPipe has no standalone Applied AI Engineer page; strong lab/scale-up cluster (Anthropic, OpenAI, Mistral, Snorkel, Scale) [T0-53]. |
| Pay | 7.75 (6.5–8.75) | B | Levels.fyi US Applied AI Engineer TC (Nov 2026): P25 $165K / P50 $232K / P75 $340K / P90 $505K–$605K (reconciling T0-53 2026-11-11 $505K vs T0-44 2026-11-13 extract $605K); lab posted base bands $210K–$440K+ [T0-44, T0-53]. |
| Durability | 6.5 (5–8) | D | Judgement. Customer-facing technical delivery at labs and vendors. |
| Leverage | 8.5 (7.5–9.5) | D | Judgement. Customer deployment and go-to-market at labs and vendors (8.5-9 anchor: directly moves revenue). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4 (2.5–5.5) | C | Verified active India hiring at OpenAI (Bengaluru Applied AI Engineer/Architect), Anthropic India partner/field roles and funded AI startups; no platform title count [T0-53]. |
| India pay | 6 (4–8) | D | No India evidence. |

India rank (CCI with India inputs): #6 of 24. One input (India comp) is a Grade D placeholder.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ● 8.5 | ◐ 6.5 | ◐ 6.5 | ○ 2 | ◐ 7 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), LLM APIs & tool calling, RAG, Agents & tool use, Customer scoping & demos, LLM evaluation (golden sets, calibrated judges, CI gates).
- **Important (headline):** Guardrails, Prompt & context design, Technical writing, Retrieval quality (hybrid, reranking, recall@k), ML fundamentals, AWS / Azure / GCP, Git & CI/CD, Embeddings & vector search.
- **Full inventory:** 46 skills (Must 6 · Important 14 · Should 14 · Optional 12), each with its evidence and posting keywords: [applied-ai-engineer.md](../../03-skills-and-tech/inventories/applied-ai-engineer.md).
- **Prerequisites:** Lab-tier hiring bar on top of the AI Engineer stack; backend (~6 months) and PhD (~8 months) routes [D · T0-06]
- **Credentials (tie-breakers, not skills):** AWS Certified Generative AI Developer – Professional (AIP-C01) (Optional: services channels); LangChain Certified Agent Engineer (LCAE) (Optional: ). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A customer-facing reference implementation with evals and a published write-up; the AI Engineer T2–T3 portfolio
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (59%); [P2 Reliable agent: approvals, sandboxed tools, replay, failure injection](../../05-portfolio/project-archetypes.md#p2) (35%); [P3 Eval harness with a calibrated judge and statistics](../../05-portfolio/project-archetypes.md#p3) (32%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Application.** It tests Coding, RAG or agent system design, and evaluation (plus an emerging AI-assisted build variant at AI-native firms such as Sierra, OpenAI and Anthropic). Source: T0-14, T0-46, T0-53, T0-57.
- **Practise:** the [application prep pack](../../08-interviewing/prep-packs.md#application-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** A2 Deployer (Applied GenAI Engineering); headline pattern: "Forward Deployed / Applied AI Engineer: customer-facing LLM systems". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** applied AI, LLM, customers, evals, deployment, solutions, safety
- **Leave out or reframe:** Generic chatbot demos; no evidence of working with external users
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-applied-ai-engineer).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [AI Engineer](ai-engineer.md) (0.62); [Forward Deployed Engineer](forward-deployed-engineer.md) (0.43); [Agentic AI Engineer](agentic-ai-engineer.md) (0.35).
- **Same family (Applied AI Engineering):** [AI Engineer](ai-engineer.md), [Agentic AI Engineer](agentic-ai-engineer.md), [AI Product Engineer (AI Frontend)](ai-product-engineer.md), [AI Enablement Engineer](ai-enablement-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-applied-ai-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-applied-ai-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (JobsPipe 2026-11-13; Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

At frontier labs and AI vendors (OpenAI, Anthropic, Mistral, Scale AI, Snorkel AI, AssemblyAI — 32 of 36 sampled postings as of 2026-11-13), **Applied AI Engineer** names a **post-sales, customer-facing build-and-advise engineering role** sitting beside account executives and product teams [A/B · T0-53 L65, L112]. Typical deliverables include scoping enterprise AI use cases, taking prototypes into production, building systematic evaluation suites with representative data and graders, running customer workshops and public technical content (cookbooks, reference architectures), and feeding product gaps back to core research and engineering [A/B · T0-53 L65, L112, L254–L255]. Regulated or sensitive-sector variants (Healthcare/Life Sciences, Cyber/Government) account for only **3 of 36 (8%)** sampled postings — a real niche, though narrower than the Phase 0 definition implies [M · T0-53 L303, L351].

**The technical stack diverges sharply between frontier labs and AI vendors/enterprises.** Across the 10 postings read in full (Anthropic ×4, Mistral ×2, Scale AI, Snorkel AI, Siemens, Atomicwork; ±31 pp), Python (9/10), agents (9/10), customer scoping (9/10), evaluation (8/10), and technical communication (7/10) are near-universal [M · T0-53 L68, L189–L209]. By contrast, **RAG, vector search, fine-tuning, and named orchestration frameworks** (LangChain, LlamaIndex, LangGraph, Semantic Kernel) appeared in **5 of 6 non-Anthropic reads** and **0 of 4 Anthropic reads**, which instead emphasised context engineering, evaluation frameworks, MCP, technical writing, and safety [M · T0-53 L78, L191, L196–L213].

**Important provenance note on skill shares.** The November 2026 dossier confirmed that JobsPipe has no `Applied AI Engineer` page; the posting-term shares previously shown on Phase 0 role cards (Python 78.4%, LLM 76.7%, agentic AI 59.3%, RAG 54.0%, ML 39.8%) came from JobsPipe's broader `AI Engineer` population [B · T0-53 L67, L215, L360].

**Mid-level versus senior, staff, and lead scope.** Mid-level/unqualified lab postings (typically 2–4 years) pair directly with customer engineering teams to ship production integrations and evaluation harnesses [A · T0-53 L268, L489–L490]. Staff and Lead variants (e.g., Mistral Lead asking 7–10+ years; Scale, Snorkel, Flexport, Concurrence, and Crusoe Staff roles) lead multi-quarter customer architectures, work directly with customer CTOs and AI product leaders, and set cross-account deployment patterns [A/B · T0-53 L76, L286, L495, L506].

## Employer landscape and title confusion

Exact-title demand is measurable only in the AI-startup and lab segment because LinkedIn, Indeed, and Glassdoor block exact-title censuses and JobsPipe lacks an Applied AI Engineer page [T0-53 L66, L155]. On Fast AI Jobs' `AI Engineer` board (352 open roles across 188 startups, updated 2026-11-11, up +28% from 275 on ~2026-07-30), **21 of the newest 50 rows (42%)** carry "Applied AI Engineer" across 9 employers — led by OpenAI (6) and Scale AI (4), plus Snorkel (2), AssemblyAI (2), Flexport (2), Concurrence (2), General Matter, Pika, and Crusoe — with **zero entry-level rows** (6 Staff, 4 Senior, 11 unqualified) [B/M · T0-53 L66, L141–L146]. Extrapolating from 21/50 to ~150 total openings is weak because the newest rows over-represent bulk posters, though OpenAI alone had at least **20 distinct** Applied AI / Partner Applied AI titles observed [M · T0-53 L147, L353]. Neither OpenAI nor Anthropic posted any literal `AI Engineer` title in T0-53's searches [B/C · T0-53 L135].

**Five distinct jobs hide under "Applied AI Engineer" — screen the duties before applying [A/B · T0-53 L65, L114–L133, L321–L329]:**

| Variant or collision | Examples in T0-53 (n = 36 + exclusions) | What differs and how to handle it |
|---|---|---|
| **Customer-facing build & advise (core)** | OpenAI Enterprise / Digital Natives / HLS / Delhi; Anthropic Enterprise / London / Life Sciences; Mistral ×3; Scale ×4; Snorkel ×2; AssemblyAI ×2 | 22/36 sample rows; post-sales prototyping, production deployment, evals, workshops, and customer discovery [A/B · T0-53 L116] |
| **Partner ecosystem & pre-sales variants** | OpenAI `Partner Applied AI Engineer` (GCP, Oracle, AWS; 3/36); Anthropic `Applied AI Architect` (pre-sales, 3+ yrs); Snorkel `Staff Pre-Sales` (2/36) | Partner roles build reference architectures with cloud/ISV partners; Architect/Pre-Sales roles ask for technical selling [A/B · T0-53 L112, L117–L118] |
| **Internal / product AI engineering** | NVIDIA (engineering productivity), Siemens Bangalore, Atomicwork, Deloitte India (`Applied AI Engineer II` = full-stack product) | 4/36 sample rows; no external customer delivery — closer to [AI Engineer](ai-engineer.md) [A/B/C · T0-53 L65, L120, L322, L329] |
| **Organisation-name collision** | OpenAI's "Applied AI Engineering" *organisation* (e.g., `Applied AI Engineer, Codex Core Agent`, excluded) | Standard product/model-improvement engineering housed inside a division named Applied AI [B · T0-53 L43, L133, L321] |
| **Classic ML title collision** | JPMorgan `Applied AI ML Associate / Lead` (excluded) | Traditional ML engineering and data science; not customer-facing LLM delivery [B · T0-53 L43, L133, L323] |

**Title churn and stale listings:** Search the entire sibling family — `AI Deployment Engineer` (OpenAI uses near-identical team text to Applied AI Engineer), `Forward Deployed Engineer` / `Forward Deployed ML Engineer` (Mistral, Anthropic, Databricks), `Deployed AI Engineer` (Helsing), `Frontier Agents Engineer` (Scale AI's "Applied AI Engineer, Enterprise" posting now carries this headline), `Partner Applied AI Engineer`, and `Applied AI Architect` [A/B · T0-53 L73, L125–L132]. Always check live status on the employer's ATS board: **4 of 14 (29%)** fetched search-indexed postings were closed (including Google Cloud `FDE IV, Applied AI` and EY London) [A/M · T0-53 L56, L73, L174].

## Career path, India demand and market signals

**Prerequisites and backgrounds.** Stated minimum experience across 8 full-read postings ranges **2–4 years (median 3)** — 2+ at Mistral, 3+ at Snorkel and Anthropic Architect, 4+ at Anthropic Applied AI Engineer — while **0 of 36** sampled titles are entry-level (JobsPipe similarly finds AI-titled roles are 16.4% entry-level versus 38.3% across all postings) [A/B/M · T0-53 L70, L268, L280]. A bachelor's degree or equivalent appears in 7 of 10 full reads, and **a PhD or master's is required in only 1 of 10** (Mistral Palo Alto, while Mistral's Lead posting accepts "self-made") [A/B · T0-53 L70, L268]. Employers name broad engineering feeder backgrounds: software engineering, FDE, technical founder, solutions architect, customer/sales engineering, product engineering, TPM, data science, and (at Mistral) DevOps/SRE — with no evidence of a non-technical entry path [A/B · T0-53 L269–L280]. Watch for ATS label mismatches: Siemens tags its Bangalore role "entry level" while requiring 3–5 years of ML/AI engineering [A · T0-53 L325, L523].

**Progression ladder:** Applied AI Engineer → Senior / Staff → Lead / Technical Lead (7–10+ years at Mistral) → Manager (7+ years at Anthropic, 8+ at OpenAI) → Director / Head of Applied AI (Scale AI, Snorkel AI), alongside lateral moves into Applied AI Architect, Staff FDE, or Applied AI Research Engineer (6+ years at Anthropic) [A/B · T0-53 L76, L286–L287].

**Pay and OTE nuance (newly evidenced).** Full pay tables are owned by [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). The November 2026 dossier replaces Phase 0's "no role-specific pay" gap with direct title benchmarks:
- **Levels.fyi US Applied AI Engineer title page** (read 2026-11-13, updated 2026-11-11): **P25 $200K / P50 $250K / P75 $475K / P90 $505K** total compensation across pooled employers (n not displayed; P90 shifted from $605K on 2026-10-04, indicating an unstable upper tail) [B · T0-53 L69, L221, L235].
- **US and UK frontier-lab posted bands:** Across 5 US lab postings (OpenAI ×2, Anthropic ×3), median range midpoint is **$264,500** — OpenAI Enterprise **$197K–$278K + equity**, OpenAI API Platform Digital Natives **$251K–$278K + equity**, Anthropic Enterprise **$200K–$320K**, Anthropic Life Sciences **$280K–$320K**, Anthropic Architect Startups **$240K–$315K** (COI), plus Anthropic London **£225K–£240K** (COI) [A/B/M · T0-53 L222–L227, L232]. Vendor/Big Tech comparators include Snorkel (**$175K–$300K OTE + options**; Staff Pre-Sales $230K–$360K), AssemblyAI remote senior ($195K–$250K base), and NVIDIA internal ($152K–$287.5K + equity) [A/B · T0-53 L228–L231, L512].
- **Verify base versus OTE and lab-equity volatility:** Snorkel explicitly posts On-Target Earnings (OTE), and Anthropic Life Sciences sits inside the Sales department where posted ranges may be OTE rather than pure base [A · T0-53 L225, L228, L326]. Meanwhile, Levels.fyi's OpenAI SWE TC median stood at $600K (n = 248, 2026-11-01) versus $800K (2025-12-26) and Phase 0's $875K — underscoring high volatility in lab equity valuations [B · T0-53 L235, L354].
- **Sponsorship and remote limits:** Lab postings are mostly hybrid or on-site (25%–3 days/week in office; only 3 of 13 postings with visible work mode offered a US or India remote option, none globally remote) [A/B/M · T0-53 L158, L308]. Anthropic (4 postings) and Mistral Palo Alto state visa sponsorship availability, while exact-title H-1B LCAs remain scarce (6 filings, median offered wage $185,480; OpenAI's 311 LCAs sit under other titles) [A/B/M · T0-53 L75, L233, L309–L310]. See [visa and relocation](../../11-tracks/visa-and-relocation.md).

**India demand and pay reality (newly evidenced).** Replacing Phase 0's "no India evidence" gap, **OpenAI** actively hires `Applied AI Engineer`, `Applied AI Architect`, and `Applied AI Engineer, Partner – AWS` across **Delhi, Mumbai, and Bengaluru** (hybrid 3 days/week with relocation assistance; remote option noted for Partner-AWS Bangalore; live-verified 2026-11-19) [B · T0-53 L72, L333–L334]. GCC, enterprise, and consultancy postings also appear at Siemens Technology and Services (Bengaluru, 3–5 years), Deloitte India (Bengaluru), DevRev (`Member of Applied AI – Architect`, Bengaluru), and Hitachi Energy (out of window), alongside Indeed India's nearly 19× FDE-family surge in June 2026 (moderating afterwards) [A/B/C · T0-53 L71–L72, L333, L337]. **No posted INR range for lab Applied AI Engineer roles was found** — candidates must ask for the INR band and equity structure at the first recruiter call; available India figures remain proxies (Levels.fyi Greater Bengaluru SWE ₹55.4L [B, level unconfirmed]; Glassdoor AI Engineer ~₹10–12 LPA [C]; aijobs.net model ₹13.4–16.8 LPA [D]) [B/C/D · T0-53 L88, L238, L356].

**Credentials:** Zero of 10 full-read postings named a certification [M · T0-53 L77, L261]. T0-53 opened the official AWS AIP-C01 exam guide (Grade A: 65 scored + 10 unscored items, pass mark 750/1,000, five domains weighted 31/26/20/12/11%, targeting 2+ years' production app experience); keep it strictly optional unless targeting services channels; see [credential ROI](../../04-certifications/credential-roi.md) [A · T0-53 L77, L262].

## Interview themes and preparation notes

Role-specific employer loop specifications remain unpublished outside AI-usage policies; stage descriptions come from prep vendors (Grade C, COI) and single candidate reports (Grade D) [A/C/D · T0-53 L74, L242–L249]:

- **Two stages missing from Phase 0's generic Application track:** Across Anthropic, OpenAI (SA/FDE/GenAI Engineer guides), and Mistral reports, loops consistently add (1) a **practical build or take-home** (or solution design) and (2) a **customer-conversation / customer-scenario simulation** alongside coding, system design, and values/behavioural rounds (4–6 rounds over 3–6 weeks; Mistral ~5 rounds including LeetCode-medium coding, deep technical use-case, and customer-success rounds) [C/D · T0-53 L74, L244–L246, L359]. No direct loop evidence confirmed Phase 0's "RAG with access control" prompt [T0-53 L359].
- **Anthropic's candidate AI-usage policy (primary page read, Grade A, COI; live-verified 2026-11-19):** Write application drafts yourself before refining with AI; complete take-homes **without** AI unless explicitly told otherwise; use **no AI** in live interviews unless indicated; AI is encouraged for interview preparation [A · T0-53 L74, L244, L464]. Always verify each employer's rules in writing before each stage.
- **Proof of work that aligns with postings:** Employers explicitly ask for **shipped production systems real users depend on** ("not just prototypes" — Mistral; "builder credibility" — Anthropic), **evaluation suites** (8/10 full reads), **public technical writing / cookbooks** (OpenAI Codex Applied AI names OpenAI Cookbook contributions; Anthropic names public technical content, MCP servers, benchmarks, and agent skills), and at Mistral **hackathons and open-source LLM contributions** [A/B · T0-53 L253–L259]. Weak signals are unmeasured chatbot demos with no external users and certificate-led headlines [P · T0-53 L316, L365]. Practise with the [application prep pack](../../08-interviewing/prep-packs.md#application-pack) and [application plus customer scoping prep pack](../../08-interviewing/prep-packs.md#application-plus-customer-scoping-pack) (no model answers).

## Dossier evidence and limits

- **Primary dossier:** [T0-53](../../../research/sessions/T0-53-role-dossier-applied-ai-engineer.md) (retrieved 2026-11-13; 52 sources: 17 Read, 35 Extract-only; 36 included JD records: 10 read in full, 8 body extracts, 18 listing-level rows) [T0-53 L51, L166, L427–L480].
- **Sampling and statistical limits:** Skill shares rest on **n = 10 full reads (±31 percentage points)**, heavily skewed towards frontier labs and AI startups (32 of 36 records; only 4 from Big Tech, enterprise, GCC, and IT services), with **4 of 10 full reads from Anthropic alone** [T0-53 L68, L178–L181, L392]. Accordingly, T0-53's suggested demotions of `rag`, `guardrails`, `cloud`, `git_ci`, and `vector_search` are **not** generalised to the full role without a broader enterprise/GCC full-text sample (n ≥ 30); `customer_scoping` and `evals` are flagged as strong promotion candidates corroborated across T0-48 and T0-51. OpenAI and AssemblyAI pages blocked automated fetches; no non-English searches were run; three OpenAI extract rows lacked retained posting-specific URLs [T0-53 L373–L384].
- **COI and provenance transparency:** Ten ledger entries (`S1`–`S6`, `S34`–`S36`, `S38`) carry COI flags (Anthropic pages authored by Claude Sonnet 5.5, plus interview-prep vendors) [T0-53 L13, L410, L425]. One vendor's untraceable claim that customer rounds "filter out about 60%" and an untraceable India ₹6–80 LPA range are excluded as Grade E [T0-53 L238, L249].
- **What would change this view:** A larger enterprise, consultancy, and GCC full-text sample; posted INR ranges for India lab roles; role-specific interview evidence at Scale AI, Google Cloud, and Indian GCCs; and tracking whether OpenAI and Scale consolidate parallel titles [T0-53 L93–L96, L376–L377].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
