---
id: "T0-48"
title: "Role Dossier: AI Engineer"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-ai-engineer"
tags: ["ai-engineer", "role-dossier", "job-postings", "llm-applications", "india-lens"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai with web search and page fetch. Anthropic's own postings (JD36) and Claude-named tooling inside postings are in scope; those rows are marked COI."
evidence_window: "2025-07-11 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-48: Role Dossier: AI Engineer

S-numbers (S1 to S72) are rows in the Sources & Evidence Ledger. Grades follow EGP-1.0: A is an employer's or issuer's own page that I opened; B is a platform, aggregate or mirror; C is third-party analysis; D is recall, a model estimate or a single anecdote; M is my own calculation (it inherits the weakest input grade); P is practice-curated. The brief states 2026-11-11 as its anchor; I read every page on 2026-11-13, so postings are live at read or dated between 2026-08-13 and 2026-11-13. K1 to K15 are the knowledge base's claims, tested in Repository Deltas. This report consolidates two research passes (28 searches and 29 page fetches in total). The second pass raised the full-text posting sample from 11 to 14, opened the Levels.fyi US pages for AI Engineer and ML Engineer, read Databricks' own exam guide, and re-checked the Fast AI Jobs and credential claims. Skill shares come from a sample with a known selection bias, so they are cross-checks on platform shares and not measurements.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | "AI Engineer" postings are mostly GenAI application work (LLM APIs, RAG, agents) and name Python in nearly all of them. | 75% | D |
| P2 | US posted base for the title sits at roughly $150–250K, with senior postings at $180–260K. | 65% | D |
| P3 | Employers rarely name certifications for this role. | 80% | D |
| P4 | Frontier labs rarely use the literal title "AI Engineer". | 60% | D |
| P5 | India holds about 10–14% of postings, with pay centred on ₹10–25L. | 60% | D |
| P6 | Within one employer the AI Engineer title earns less than ML Engineer, but by less than the market-wide gap (about 0.55×). | 65% | D |

## Research Question

**Decision question.** What must the knowledge base know about the AI Engineer role to tell a job seeker accurately what the job is, how much demand and pay it carries, which skills, proof and credentials it needs, how candidates are interviewed and presented, how careers progress, and where the jobs are?

**Sub-questions.**
1. Do the platform counts and shares reproduce?
2. What do real postings ask for, by employer type and region?
3. What does the title pay, and how does that compare with ML Engineer inside one employer?
4. Which certifications are live or retired, and do employers name them?
5. How are candidates interviewed and what proof do hiring sources want?
6. What are the entry routes, sponsorship signals and India specifics?

**Reading chosen.** The role is the person who builds LLM-powered product features. Customer-facing "Applied AI Engineer" and "Forward Deployed AI Engineer" postings are kept in the sample but flagged as variants, because labs and startups use no other label. Postings whose work is robotics, construction site AI, Power Platform or pure data science are off-role.

**Method.**
- **Volume of work.** I ran 28 web searches and 29 page fetches on 2026-11-13. The fetch tool refused 5 further URLs because they had not appeared in earlier results.
- **Sample.** Thirteen postings were read in full on employers' own Lever, Greenhouse or careers pages (JD01–JD10, JD40–JD42). One more (Microsoft, JD11) was read in full through a Getro mirror that carries the employer's apply link. The other 28 records are thin: title, location, pay or snippet text read through mirrors or aggregator rows, with liveness unverified.
- **Denominators.** Skill shares use only the 14 full-text postings (n = 14, about ±26 percentage points). I cannot observe an absent term in a truncated snippet, so thin records are excluded.
- **Sampling bias.**
  - Queries contained "RAG", "agents", "evaluation" and "LLM", so shares for those terms are inflated by construction.
  - The search engine favours English-language pages and large employers.
  - It also returns closed postings: 7 of 21 ATS fetches (33%) landed on a board index because the job had closed, and one returned an error.
  - Google, Amazon, Meta, Apple and NVIDIA postings were not reached.
- **Falsification searches.**
  - Within-employer pay: Levels.fyi Google AI Engineer against Google ML Engineer.
  - Python universality: I looked for roles that do not name Python and found two.
  - Frontier-lab title use: Anthropic's and Mistral's boards, and OpenAI rows on Fast AI Jobs.
  - Posting liveness: I fetched postings that search or platform lists showed as live or "New".
  - Platform counts: I re-read Fast AI Jobs and JobsPipe against the KB's figures.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | JobsPipe counts reproduce: 3,944 live (global), 1,697 (US) and 398 (India) on 2026-11-13, identical to the KB's 2026-10-19 values. India's share is 398/3,944 = 10.1%, not 13.6%. | [S1][S2][S3] | B (share M) |
| KF2 | Fast AI Jobs lists 352 open AI Engineer jobs at 188 AI startups, last updated 2026-11-11 (the KB records 326 at 183). A search-index snapshot of the same page from about 2026-07-30 to 2026-08-03 showed 275 at 170, so the count rose about 28% in roughly three and a half months. In that August snapshot AI Engineer (275) also outnumbered ML Engineer (227). | [S70][S71] | B (growth M) |
| KF3 | LinkedIn Jobs on the Rise 2026 (2026-01-07) ranks AI Engineers #1 of 25, with median experience 3.7 years and 26% remote / 27% hybrid. LinkedIn groups AI engineers with ML engineers. | [S6][S7] | B |
| KF4 | At AI startups the "AI Engineer" label is mostly customer-facing. Of the 50 newest AI Engineer rows by posting date on Fast AI Jobs (2026-11-02 to 2026-11-11), 21 (42%) are titled "Applied AI Engineer", 11 (22%) forward-deployed, 13 (26%) plain AI / Senior / Staff AI Engineer and 5 (10%) other. Greenhouse hosts 64% of them and Ashby 36%. Indicium's board shows the same split (2 "AI Engineer" and 4 forward-deployed postings). | [S70][S65] | B (shares M) |
| KF5 | In 14 full-text postings: LLM building 14/14, RAG 12/14, evaluation 12/14, Python 12/14, agents 11/14. Showpad (TypeScript-led) and Talentica name no Python. Shares are query-biased (±26 pp). | [S27]–[S37][S62]–[S64] | M |
| KF6 | Off-role titles: on title alone, 5 of 56 JobsPipe sample rows (9%) are clearly off-role (Site AI ×2, Power Platform ×2, Physical AI ×1) and up to 11 (20%) are ambiguous. Fast AI Jobs' 50-row sample has 1 robotics row (Figure AI "Helix AI Engineer"). Celonis' internal Senior Applied AI Engineer lists Make and Zapier beside LangChain. This is a floor, not a content-based share. | [S1][S2][S5][S70][S64] | M |
| KF7 | Frontier labs use "Applied AI Engineer", which is customer-facing: 4+ years at Anthropic, 2+ at Mistral, and six OpenAI "Applied AI Engineer" or "Partner Applied AI Engineer" rows on Fast AI Jobs. No literal "AI Engineer" title appeared on the first page of Anthropic's 670-job board. | [S29][S47][S70] | A/B |
| KF8 | Posted US base midpoints (n = 18, mixed levels): median $200.6K, IQR $155K–$234K. Senior-or-higher titles (n = 7): median $231.5K. Non-senior titles (n = 11): median $195K. The sample is biased high because it favours pay-transparent, larger employers. | [S30][S32][S37][S38][S40][S45][S46][S48] | M |
| KF9 | Levels.fyi US pages opened 2026-11-13 (both updated 2026-11-12): AI Engineer median total compensation $155K (P25 $110K, P75 $211K, P90 $280K); ML Engineer $285,650 (P25 $200K, P75 $387K, P90 $498K). The ratio is 0.54 at the median and 0.55–0.56 elsewhere. At Google it is 0.79–0.83 (AI Engineer median $240K, n = 38, against ML Engineer about $290–302K), so roughly 62–69% of the log gap disappears inside one employer. | [S10][S66][S11][S12] | B/M |
| KF10 | India pay: sources centre on ₹9–25L (Flexiple GenAI Engineer Bengaluru median ₹9.2L, n = 59; AIM Research ₹12–15L; Levels.fyi WCG ₹24.0L). None of the four full-read India postings states pay. | [S15]–[S19][S27][S31][S36][S64] | C/B |
| KF11 | Certifications: 0 of 14 full-text postings name one. AWS ML Specialty is retired (last test 2026-03-31), AI-102 is retired (2026-06-30), and AWS AIP-C01 is live. Databricks' Generative AI Engineer Associate is live (guide version of 2026-03-18: 45 scored items, 90 minutes, USD 200, online proctored, 2-year validity). AI-103 is still labelled beta in Microsoft Learn extracts, while one vendor page claims general availability. | [S20]–[S26][S67][S68][S69] | A/B/C |
| KF12 | Prerequisites: the median stated minimum experience is 3 years (n = 21, range 0.5–10). Senior-or-higher titles are 17 of 42. Explicit entry roles are 1 of 42. A degree is stated in 5 of 14. Talentica restricts by institution tier. | [S27]–[S38][S62]–[S64] | M |
| KF13 | Interview loop: Spektr runs 30 min intro, 30 min technical and 60 min technical. Third-party sources describe an eval-design take-home and a RAG design round with failure-mode analysis. Anthropic's application asks for non-AI-assisted writing. | [S35][S47][S52][S56] | A/C |
| KF14 | US sponsorship: DOL data via an aggregator shows 8,275 certified H-1B LCAs for the AI/ML engineer family (FY2025 to FY2026 Q3), 529 titled "AI ENGINEER", median offered wage $165K then $169K, 46.6% in California. Postings restrict sponsorship (Microsoft "Not Available" on Wellfound; Inizio US citizens or green card only). Celonis asks about sponsorship need, Indicium Lisbon asks about the right to work in Portugal, and GR8_TECH collects B2B contractor rates. | [S20][S40][S41][S62][S64][S65] | B |
| KF15 | Staleness and title drift: 7 of 21 ATS fetches had closed (a Celonis page marked "New" redirected to the careers home). JobsPipe's skill shares were counted on 2026-09-10. Vercel's job 5517523004 is "AI Engineer" on one site and "Research Engineer" on another, and D&B's "Senior Gen AI Engineer" is internally "Senior Analyst". | [S50][S4][S30][S27] | A/B |

## Recommendation

**Decision rules for a job seeker**

1. **Search by content and by alias.**
   - Apply where the posting names LLM APIs plus RAG or agents. Search "Applied AI Engineer" and "Forward Deployed AI Engineer" as well as "AI Engineer", because at AI startups about two-thirds of the "AI Engineer" labelled rows use those forms. Decide in advance whether you want customer-facing work.
   - Skip postings that mention Power Platform, "Site AI", "Physical AI" or low-code only.
   - *Failure mode:* the alias searches pull in pre-sales roles that need travel and customer skills, and the title filter still hides GenAI roles titled "Research Engineer", "Agent Engineer" or "Software Engineer, AI".
2. **Prove one evaluated, deployed system.**
   - Show a metrics table, a cost and latency budget, and a reproducible README. Evaluation appears in 12 of 14 full-text postings (query-biased), and "shipped, not demoed" appears verbatim.
   - *Failure mode:* big-tech and large-enterprise postings also screen on ML fundamentals (Workday asks for PyTorch and TensorFlow years; Guardz asks for a machine-learning foundation), so a single app project may not clear them.
3. **Match the language to the stack.**
   - Python is near-universal (12/14) but not universal. Spektr says "TypeScript and/or Python", Showpad is TypeScript-led, Celonis accepts "Python or other scripting languages like Javascript", and Vercel names both.
   - *Failure mode:* a single-language profile can rule out roughly a third of postings.
4. **Treat certifications as optional.**
   - Take one only if the target stack matches: Databricks Generative AI Engineer Associate for Databricks shops, AWS AIP-C01 for AWS services shops, AI-103 for Azure shops (check its beta status first). Never start the retired AWS ML Specialty or AI-102.
   - *Failure mode:* services and GCC channels may screen on certificates; my sample cannot see that channel.
5. **Anchor pay on posted bands and level, not on the ML Engineer title.**
   - Use US base of about $155K–$234K (IQR) for mid-to-senior roles and about $230K for senior-or-higher. Market-wide the AI Engineer title earns about 0.54× ML Engineer; inside Google the gap is 17–21%. Negotiate by level and employer.
   - *Failure mode:* the sample over-represents pay-transparent employers, and Levels.fyi skews to big tech.
6. **In India, expect ₹9–25L for most roles.**
   - Pay is higher at product and global-tech centres. Check institution gates: Talentica lists IIT, NIT, BITS and similar institutes only.
   - *Failure mode:* India figures are mostly C-grade and employer-mix dependent.
7. **Confirm a posting is live on the employer's board before investing time.**
   - *Failure mode:* boards also close postings quickly, so a live board can still be too late.

**What would change these rules**
- An unbiased count (no query terms) that puts evaluation below 40% would demote it from "candidate Must".
- Evidence that services and GCC employers screen on certifications would change rule 4.
- A broader sample from non-startup employers that shows the "Applied" and forward-deployed share far below 64% would narrow rule 1 to startups and labs.

## Alternatives Considered

| Option | Verdict and reason |
|---|---|
| Compute skill shares on all 42 records | Rejected. 28 records are truncated, so absent terms are unobservable. |
| Use platform shares only (no sample shares) | Partly used. Platform shares set tiers; the sample is a cross-check. |
| Exclude customer-facing "Applied AI Engineer" roles | Rejected. They are kept and flagged because labs and startups use no other title. |
| Treat Vercel's retitled role as in-sample | Kept. It has the same job ID under the AI Engineer title and does LLM product work; flagged as title drift. |
| Use Levels.fyi alone for pay | Rejected. It is big-tech skewed. Posted bands and LCA wages are added to corroborate. |
| Use the Fast AI Jobs title mix as a proxy for the whole market | Rejected. It covers AI startups only (Greenhouse and Ashby), so it is used for the startup segment. |

## Detailed Findings

### 1. Definition and variants

The 14 full-text postings fall into four variants.

| Variant | Full-read examples | What distinguishes it | n (of 14) |
|---|---|---|---|
| Product-embedded LLM application engineer | OfferUp, Spektr, Showpad, Vercel, Microsoft, Guardz, GR8_TECH | Owns RAG, agent or assistant features inside a product, with evaluation and production support | 7 |
| Consultancy delivery | Robots & Pencils, Indicium, Talentica | Builds LLM systems for clients | 3 |
| Enterprise analytics, platform and internal automation | D&B ×2, Celonis | Data-platform or internal-process AI; Celonis names low-code tools | 3 |
| Customer-facing prototype builder at a lab | Mistral | Pre-sales prototypes and deployments for customers | 1 |

The boundary with ML Engineer is stated in Indicium's posting ("rather than model training or research") and in GR8_TECH's ("Not research. Not prompt-only."). The boundary with solutions and forward-deployed engineering is blurred at Mistral, Anthropic, Databricks, Indicium and NinjaTrader.

Alias counts across the 42 sample records:

| Alias form | n |
|---|---|
| AI Engineer (plain) | 16 |
| Staff / Principal / Lead AI Engineer | 6 |
| Applied AI Engineer (incl. Senior) | 6 |
| Senior AI Engineer | 5 |
| Gen AI / GenAI Engineer | 5 |
| AI Software Engineer | 1 |
| Sr. Software Engineer, AI | 1 |
| Frontier Agents Engineer | 1 |
| Senior AI Specialist (GR8_TECH) | 1 |

JobsPipe rows add Site AI Engineer, Power Platform & AI Engineer, Physical AI Engineer, Founding AI Engineer, Graduate AI Engineer and Full-Stack AI Engineer Intern [S1][S2][S5].

**Title families among the 50 newest AI Engineer rows by posting date on Fast AI Jobs (2026-11-02 to 2026-11-11, AI startups)** [S70]:

| Title family | Rows | Share | Examples |
|---|---|---|---|
| Applied AI Engineer (incl. Partner, Senior, Staff, Enterprise) | 21 | 42% | OpenAI ×6, Scale AI ×4, Snorkel AI ×2, AssemblyAI ×2, Flexport ×2, Concurrence ×2, General Matter, Pika, Crusoe |
| Forward-deployed or "Deployed" AI Engineer | 11 | 22% | Turing ×4, Databricks ×2, Toloka ×2 (freelance), Helsing, Avathon, Traversal |
| Plain AI / Senior / Staff AI Engineer | 13 | 26% | Metropolis ×3, Grammarly ×3, Grafana Labs ×2, Celonis, Fever, TRM Labs, Reducto, PhysicsX (post-training) |
| Other | 5 | 10% | Figure AI (robotics "Helix AI Engineer"), Everlaw (GTM AI Engineer), Perplexity (Member of Technical Staff), Profound (Agent Engineer), SendBird (AI Agent Engineer, Intern) |

Greenhouse hosts 32 of these 50 rows (64%, including company sites with a Greenhouse job ID) and Ashby hosts 18 (36%). The 50 rows are the most recent of 352, so they over-represent employers that post often (Turing, Scale AI, OpenAI).

### 2. Demand table (role:ai-engineer)

| Measure | Value | Source and date | Grade |
|---|---|---|---|
| Live postings, global | 3,944 | JobsPipe page, read 2026-11-13 [S1] | B |
| Live postings, US | 1,697 | JobsPipe [S2], 2026-11-13 | B |
| Live postings, India | 398 | JobsPipe [S3], 2026-11-13 | B |
| India share | 10.1% | 398/3,944 | M |
| Entry-level labelled | 275 (7.0%) | JobsPipe [S5] | B/M |
| Senior-titled query | 1,377 (34.9%) | JobsPipe [S5]; the label share is 24.6% [S4], a different measure | B/M |
| Freelance / contract / part-time | 197 / 197 / 21 | JobsPipe [S5] | B |
| Boston / Austin | 33 / 45 | JobsPipe [S5] | B |
| Remote share | 11.0% | JobsPipe JD page, counted 2026-09-10 [S4] | B |
| Pay disclosed | 19.6% [S4] or 28.1% (1,107/3,944) [S1] | Conflict: different dates and corpora | B/M |
| AI startups hiring AI Engineers | 352 roles at 188 startups; 44% at Pre-Seed to Series B | Fast AI Jobs, last updated 2026-11-11 [S70] | B |
| Same platform, earlier snapshot | 275 roles at 170 startups | Search-index copy, sibling pages updated 2026-07-27 to 2026-08-03 [S71] | B |
| Platform growth | +28% (352/275) | Snapshot date is inferred, so treat as indicative | M |
| ML Engineer at AI startups (August snapshot) | 227 (AI Engineer 275 is 1.21×) | Fast AI Jobs [S71] | B/M |
| Forward Deployed Engineer at AI startups (August snapshot) | 779 roles at 288 startups | Fast AI Jobs [S71] | B |
| San Francisco, AI Engineer (August snapshot) | 98 roles at 66 startups | Fast AI Jobs [S71] | B |
| Employer mix, global | PwC 67, Capital One 34, TCS 31, Deloitte 31, Jack & Jill 25, Mastercard 20, Infosys 20, Amex 19 | JobsPipe [S1] | B |
| Employer mix, India | Teradata 9, Infosys 6, TCS 5, HCLTech 4, Barclays 4, Target 4 | JobsPipe [S3] | B |
| LinkedIn rank | #1 of 25; median 3.7 years; 26% remote, 27% hybrid | [S6][S7], 2026-01-07 | B |
| LinkedIn volume | 75,000 AI-engineer postings 2023–2025 [S8, C]; +143% in 2025 [S9, D] | secondary | C/D |

LinkedIn and JobsPipe define remote differently (26% against 11%), so the figures are not comparable. The Fast AI Jobs and JobsPipe counts cover different employer sets (AI startups against all employers).

### 3. Sample summary

**n = 42 records.** Thirteen are full reads on employer pages (A), one is a full-text mirror (B), and 28 are thin (B).

| Employer type | US | Europe | India | LATAM | Other or unspecified | Total |
|---|---|---|---|---|---|---|
| Frontier lab | 1 | 1 | 0 | 0 | 0 | 2 |
| Big Tech | 2 | 0 | 0 | 0 | 0 | 2 |
| AI-native and product startups | 6 | 2 | 0 | 0 | 3 | 11 |
| Enterprise and product companies | 10 | 1 | 5 | 0 | 2 | 18 |
| IT services, consultancy, staffing | 3 | 1 | 3 | 1 | 0 | 8 |
| GCC | 0 | 0 | 1 | 0 | 0 | 1 |
| **Total** | 22 | 5 | 9 | 1 | 5 | 42 |

"Other or unspecified" holds Guardz (Israel), GR8_TECH (remote, no country), Safran, Apollo.io and Fieldguide Senior AI Engineer (location not shown in the extract).

- **Seniority by title:** entry 1 (2.4%), mid or unlabelled 24 (57.1%), senior 11 (26.2%), staff/principal/lead 6 (14.3%). Senior-or-higher is 17 of 42 (40.5%).
- **Exclusions (16):**
  - 7 closed on fetch: Anthropic 5073277008, Spektr 4855450101, EggAI 4772834101, Sweet Security 4801947101, LTS 4284737009, Indicium "AI Engineers – USA" 4889127101 and Celonis Applied AI Engineer 7681593003 (posted 2026-04-02 per The Muse, also outside the window).
  - 2 outside the window: TIAA Lead AI Engineer (ended 2026-04-22) and MX Technologies Staff AI Engineer (listed 2026-04-09).
  - 3 not the role: a Microsoft engineering-manager post, a Microsoft Cloud & AI Solution Engineer (pre-sales) and a Surf AI Senior Data Scientist.
  - 2 ML-titled mirrors: Workday Principal Machine Learning Engineer and Pennylane Senior Machine Learning Engineer.
  - 2 duplicate texts: Spektr Iași 5005904101 and Indicium Lisbon 4695065101 (read in full; same text as JD08 with a Portugal right-to-work question).
- **Off-role titles:** Site AI, Power Platform, Physical AI and robotics rows came only from JobsPipe and Fast AI Jobs lists and were never entered into the sample.

### 4. Skills table (full-text n = 14; platform shares from S4 where shown)

| Skill [ID] | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| Python [python] | 12/14 = 85.7% | 14 | Must | Must | Platform 78.4%. Showpad and Talentica name no Python; Celonis accepts JavaScript as an alternative. |
| LLM APIs [llm_apis] | 14/14 = 100% | 14 | Must | Must | Platform "Llm" 76.7%. Coded broadly as any LLM-application building. |
| Agents [agents] | 11/14 = 78.6% | 14 | Must | Must | Platform "Agentic ai" 59.3%. Vercel, Robots & Pencils and Talentica are not agent-oriented. |
| RAG [rag] | 12/14 = 85.7% | 14 | Must | Must | Platform 54.0%. Vercel and Celonis lack RAG. Query-biased. |
| Evals [evals] | 12/14 = 85.7% | 14 | Important (candidate Must) | Important | KB cites 19.0%; JobsPipe publishes only the top six skills, so I could not reproduce it. My queries contained "evaluation". Mistral and Celonis lack it. |
| Retrieval quality [retrieval_quality] | 4/14 = 28.6% | 14 | Important | Important | Rerankers, chunking or HyDE named by OfferUp, Spektr, Indicium and Robots & Pencils. |
| Observability [observability] | 8/14 = 57.1% | 14 | Important | Important | KB share 28.5%, not checked. Includes monitoring and tracing wording. |
| Cost and latency [cost_latency] | 6/14 = 42.9% | 14 | Important | Important | Showpad, Indicium, Spektr, Talentica, Microsoft, GR8_TECH. |
| Cloud [cloud] | 10/14 = 71.4% | 14 | Important (watch for Must) | Important | KB 35.1%. The sample names AWS, Azure or GCP in most enterprise postings. |
| Git and CI/CD [git_ci] | 7/14 = 50.0% | 14 | Important | Important | KB 34.4%. |
| Vector search [vector_search] | 8/14 = 57.1% | 14 | Important | Important | KB 32.6%. |
| Prompt engineering [prompt_engineering] | 9/14 = 64.3% | 14 | Important | Important | Widely named but treated as a baseline; GR8_TECH says "Not prompt-only". |
| ML fundamentals [ml_fundamentals] | 7/14 = 50.0% | 14 | Important | Important | Platform "Machine learning" 39.8%. |
| Responsible AI and guardrails [c4_responsible_ai] | 7/14 = 50.0% | 14 | Important | Important | D&B ×2, OfferUp, Robots & Pencils, Indicium, Microsoft, Guardz. |
| Communication [communication] | 8/14 = 57.1% | 14 | Important | Important | KB 44.2%. |
| TypeScript / JavaScript [new:typescript] | 5/14 = 35.7% | 14 | Should (Must at TypeScript-led employers) | not in KB | Vercel, Showpad, Spektr, Mistral (React/Next.js), Celonis (JavaScript as an alternative). |
| Orchestration frameworks [new:orchestration_frameworks] | 10/14 = 71.4% | 14 | Should | not in KB | LangChain, LangGraph or agent frameworks, mostly as examples ("or equivalent"). |
| Fine-tuning [new:fine_tuning] | 6/14 = 42.9% | 14 | Should | not in KB | Named as a mention, rarely as a hard requirement. |
| MCP / A2A [new:mcp_a2a] | 4/14 = 28.6% | 14 | Should (rising from Optional) | not in KB | D&B Dublin (desirable), Microsoft (preferred protocols), GR8_TECH (must-have: MCP or similar), Guardz (strong plus). |
| Low-code automation [new:low_code_automation] | 1/14 = 7.1% | 14 | Optional | not in KB | Celonis names Make and Zapier beside LangChain. |

Specialisation shares (n = 14):

| Specialisation | Share | Postings |
|---|---|---|
| RAG and retrieval | 12/14 = 85.7% | see RAG row |
| Graph RAG and knowledge graphs | 2/14 = 14.3% | D&B Dublin, Indicium |
| Document parsing and ingestion | 2/14 = 14.3% | Robots & Pencils, Indicium |
| Context engineering | 1/14 = 7.1% | D&B Chennai |
| Coding agents | 1/14 = 7.1% | Vercel (UI generation and code synthesis) |
| Voice and conversational agents | 1/14 = 7.1% | GR8_TECH (chatbots and conversational AI) |
| Vector search infrastructure | 0/14 | none (vector stores appear as stack, not as work) |

The agentic share is 11/14, the retrieval share 12/14 and the evaluation share 12/14 (all query-biased).

### 5. Pay table

| Population | Statistic | Component | n | Date | Source (grade) |
|---|---|---|---|---|---|
| US, sample midpoints, all levels | p50 $200,575; p25 $155,363; p75 $234,125 | base | 18 | 2026-11-13 | JD sample [S30][S32][S37][S38][S40][S45][S46][S48] (M) |
| US, senior/staff/principal/lead titles | p50 $231,500 | base | 7 | 2026-11-13 | JD sample (M) |
| US, non-senior titles | p50 $195,000 | base | 11 | 2026-11-13 | JD sample (M) |
| Posted bands | Vercel $192–288K; OfferUp $140–160K; Microsoft IC3 $102.1–202.2K; Workday Principal $188–282K; Datadog Staff $234–300K; Scale Senior $216–270K; Dynatrace Lead $150–180K; ApTask $80–90K | base | 1 each | 2026-11-13 | [S30][S32][S37][S38][S45][S46][S48] (A/B) |
| US AI Engineer | p25 $110K; p50 $155K; p75 $211K; p90 $280K | total compensation | n/s | 2026-11-12 | Levels.fyi, page opened [S10] (B) |
| US ML Engineer (adjacent title) | p25 $200K; p50 $285,650; p75 $387K; p90 $498K | total compensation | n/s | 2026-11-12 | Levels.fyi, page opened [S66] (B) |
| Google AI Engineer | p50 $240,000; L3 $196K; L5 $355K; L6 $583K (bases $157K, $191K, $255K) | total compensation | 38 | 2026-10-19 | Levels.fyi [S11] (B) |
| Google ML Engineer | p50 about $290K to $302K | total compensation | n/s | 2026-08-04 for $290K | Levels.fyi localised pages [S12] (B) |
| Amazon / Scale AI AI Engineer | medians about $200K / $124.8K | total compensation | n/s | 2026-05-07 for Amazon | Levels.fyi [S14] (B) |
| AI/ML engineer LCA wages | p50 $165,350 (FY2025); $169,000 (FY2026 Q1–Q3) | offered wage on filings, not pay | 3,816; 4,459 | to 2026-06 | careery.pro on DOL data [S20] (B) |
| India, WCG (Bengaluru) | p50 ₹2,399,179 | total compensation | n/s | n/d | Levels.fyi [S15] (B) |
| India, GenAI Engineer, Bengaluru | p50 ₹9.2L; middle half ₹6–22.3L | all-in | 59 | 2026-08 | Flexiple [S16] (C) |
| India, senior (6+ years) | p50 ₹21.6L | all-in | n/s | 2026-08 | Flexiple [S17] (C) |
| India, market | p50 ₹12–15 LPA | n/s | n/s | 2025 | AIM Research [S18] (C) |
| India, Bengaluru model | p50 ₹21.1L; p25 ₹14.3L; p75 ₹35.9L | CTC | model | 2026 | Hyring [S19] (D) |
| Paris AI Engineer / Senior | €54–66.1K / €65–75K | posted | 1 each | 2026-11-13 | WTTJ [S60] (B) |

**Pay-gap probe (AI Engineer against ML Engineer, total compensation).**

| Point | AI Engineer | ML Engineer | Ratio |
|---|---|---|---|
| US P25 | $110K | $200K | 0.55 |
| US P50 | $155K | $285,650 | 0.54 |
| US P75 | $211K | $387K | 0.55 |
| US P90 | $280K | $498K | 0.56 |
| Google P50 | $240K | about $290–302K | 0.79–0.83 |

The market-wide title discount is about 46% (1 − 0.54). Inside Google it is 17–21%. On a log scale 31–38% of the market-wide gap remains within Google, so roughly 62–69% reflects employer and level mix. The KB said "about half". Google's AI Engineer figure rests on 38 submissions, so this is one employer. An earlier secondary comparator of about $262K for the US ML Engineer median [S13, C] was superseded once the Levels.fyi ML Engineer page was opened [S66].

### 6. Interview loop table

| Employer | Track | Stages | AI policy | Grade |
|---|---|---|---|---|
| Spektr (Copenhagen, Iași) | Application | Intro with Talent team (30 min), Technical interview (30 min), Technical interview (60 min) | not stated | A [S35] |
| Anthropic (Applied AI Engineer) | Application, customer-facing | Recruiter screen, technical phone screen, take-home or live coding, customer-conversation simulation, onsite weighted to system design | The Greenhouse page links an AI-usage policy and asks applicants to confirm they want to be judged on non-AI-assisted communication | C [S56]; policy fact B [S47] |
| Generic AI-native startup | Application | Intro (30 min), eval-design take-home (3–5 h), technical deep-dive with RAG design and failure modes (90 min), product and mission (45 min) | not stated | C [S52] |
| PromptLayer (practitioner) | Application | Take-home build of a working agent, agentic system-design interview | not stated | C [S53] |

The KB's Application track fits on RAG design, agent loops and evaluation architecture. "Ask them to draw an agent they shipped and mark every place it could loop forever" is a reported question [S55]. "Context management" was not evidenced in any interview source. "RAG with access control" appears only in an issuer's exam material: a sample question in Databricks' own guide concerns an agent application that must respect each user's data permissions [S67]. That is certification content, not interview evidence.

### 7. Proof of work

- **Postings (A/B):**
  - NinjaTrader asks for "shipped, not demoed".
  - Mistral lists hackathons and open source as nice-to-have.
  - Spektr says "Evaluation Obsession".
  - OfferUp and Showpad name Ragas, DeepEval and Langfuse-type tooling as nice-to-have.
  - GR8_TECH says "Not research. Not prompt-only." and asks for production-incident ownership.
  - Indicium asks for "deep understanding of their capabilities, limitations, and failure modes" of LLM APIs.
- **Hiring blogs (C):**
  - "A failure they own" is called the most reliable senior signal [S54].
  - A portfolio of shipped evals is wanted [S52].
  - One to three polished projects with real evaluation sets, metrics, deployment and error handling [S58].
  - A portfolio you can narrate [S57].
- **Strongest public examples:** I did not identify named public repositories, so this stays an Absence.

### 8. Credentials

Zero of 14 full-text postings name a certification. The thin records could not show absence.

| Credential | Issuer | State as of 2026-11-13 | Key facts | Source (grade) |
|---|---|---|---|---|
| AWS Certified Generative AI Developer – Professional (AIP-C01) | AWS | active | Beta ended 2026-03-31; standard registration opened (blog edited 2026-03-17); fee USD 300 per a secondary source | [S22][S23] A (Extract); fee [S26] C |
| AWS Certified Machine Learning – Specialty (MLS-C01) | AWS | retired | Last test day 2026-03-31 | [S21] A (Extract) |
| Microsoft Azure AI Engineer Associate (AI-102) | Microsoft | retired | Retires 2026-06-30, 11:59 PM Central | [S24] A (Extract) |
| Microsoft Certified: Azure AI Apps and Agents Developer Associate (AI-103) | Microsoft | beta, with conflict | Microsoft Learn extracts label it "(beta)" with passing score 700; Microsoft TechCommunity (updated 2026-04-16) says the exam was in beta; one vendor page claims general availability at USD 165; duration 120 minutes per a third-party article; a July 2026 prep site also names AI-103 as the AI-102 replacement [S25, C] | [S68] A (Extract); [S69] C |
| Databricks Certified Generative AI Engineer Associate | Databricks | active | Guide version live as of 2026-03-18; 45 scored items; 90 minutes; USD 200; online proctored; no prerequisite (six months' hands-on recommended); valid 2 years; recertify by retaking the full live exam; blueprint covers Agent Bricks, MCP servers, guardrails and MLflow tracing; summaries dated 2026-03 to 2026-04 corroborate the 2026-03-18 change and the 2-year validity [S72, C] | [S67] A (Read) |

- **Employer statements:** "Everyone with a Coursera certificate is calling themselves an AI engineer" (a vendor blog, C) [S54].
- **Fit with the KB tiers:** Optional for AIP-C01, AI-103 and the Databricks exam, and Avoid for the two retired exams, is consistent with the evidence. The Databricks exam is tied to Databricks tooling, which matches the KB's "only if the team runs Databricks".

### 9. Entry routes and prerequisites

- **Experience:** the median stated minimum is 3 years (n = 21; range 0.5 at Talentica to 10 at Workday). Among the 12 full-read postings that state one, the median is also 3.
- **Degree:** 5 of 14 full-text postings state one. Microsoft prefers a Master's, and Workday prefers a Master's or PhD.
- **Realistic routes:**
  - Backend and full-stack engineers fit most directly. Mistral, Indicium, Robots & Pencils and GR8_TECH ask for software-engineering fundamentals.
  - Data scientists and ML engineers fit D&B, Workday and Guardz-style roles (Guardz asks for 5+ years as an ML engineer, data scientist or software engineer).
  - Front-end engineers fit TypeScript and React-heavy roles (Vercel, Mistral, Spektr).
  - DevOps and SRE experience helps where cloud and CI/CD are named (Showpad, Microsoft, GR8_TECH).
  - No full-read posting accepts a non-engineering route.
  - New graduates appear as explicit entry titles on aggregators (275 JobsPipe entry-level rows) and in Talentica's 0.5–3.5 year band.
- **Pools of hires:** backend, ML/data science and product engineers (one vendor blog, C) [S59]. Published analyses of prior roles were not found.

### 10. Progression, durability and leverage

- **Ladder in postings:** AI Engineer II or L3, Senior, Staff, Principal and Lead (Workday, Datadog, Dynatrace, Jeppesen, Celonis' Applied AI Engineer ladder), then Applied-AI engineering management (Anthropic and Microsoft manager posts). Adjacent exits are forward-deployed and applied roles, and ML engineering.
- **Durability:** I found no measurement of commoditisation. Postings ask for evaluation, tracing, cost and guardrails more than for prompt-writing alone. Employers also ask for AI-assisted coding (Indicium).
- **Leverage evidence (A):** Mistral's Proto role says to "unlock deals, and generate follow-on revenue", OfferUp's says "directly contribute to key business KPIs", and Spektr's says "own the end-to-end AI roadmap". These quotes support revenue-adjacent scope.

### 11. Work footprint

Postings sit in orchestration and context and in applications and deployment, with an evaluation plane named in 12 of 14. Post-training and serving rarely appear; PhysicsX's "AI Engineer: Post-Training" is the one post-training row among Fast AI Jobs' 50. GR8_TECH describes internal AI automation, chatbots, AI assistants and MCP-based services already in production. Indicium states "building reliable, scalable applications rather than model training or research".

### 12. Geography and sponsorship

- **Sample:** 22 US, 9 India, 5 Europe, 1 LATAM remote, 5 other or unspecified. US cities include Seattle, Redmond, Atlanta, Bellevue, Austin, Boston and New York.
- **Platforms:** JobsPipe US 1,697 (43.0% of global), India 398 (10.1%). Fast AI Jobs' August snapshot showed 98 of 275 AI-startup AI Engineer roles in San Francisco (36%).
- **LCA states:** CA 3,853, TX 793, WA 698, NY 665 and MA 281 [S20].
- **Sponsorship in postings:**
  - Microsoft Senior Applied AI Engineer: Wellfound lists sponsorship as "Not Available".
  - Inizio: US citizens or green card holders only.
  - Indicium: a right-to-work question for the UK (London) and for Portugal (Lisbon).
  - Pennylane: remote only from France, Germany, Ireland, Spain and the UK.
  - Celonis: the form asks whether the candidate will need immigration sponsorship, now or later.
  - GR8_TECH: collects gross monthly rates for B2B cooperation, which implies contractor engagement.
  - Mistral and Anthropic: no sponsorship statement was read.

### 13. Résumé and profile signals

- **Matching terms** from full-text postings: production, shipped, evaluation frameworks, RAG pipelines, agentic workflows, tool calling, LangGraph, FastAPI, observability, guardrails, MCP.
- **Red flags** from sources: tutorial-level projects, framework-syntax headlines, certificates presented as skill (C), and "prompt-only" profiles (GR8_TECH).
- **Evidence-line patterns (P):**
  - System, corpus size, retrieval metric before and after.
  - Cost per query and p95 latency.
  - Eval-set size and CI gate.
  - Incident or failure owned.
  - These are patterns only; numbers must be real.

### 14. Misconceptions and risks

- The title is not always GenAI (Power Platform, Site AI, Physical AI, robotics "Helix AI Engineer").
- At AI startups and labs the "AI Engineer" label often means customer-facing applied or forward-deployed work (64% of Fast AI Jobs' 50 most recent rows).
- Python is not universal.
- A degree is not always stated (5 of 14).
- Staffing postings can pay far less for similar stacks: ApTask at $80–90K against OfferUp at $140–160K.
- Level inflation: D&B's internal "Senior Analyst".
- Closed postings still surface in search and on platform lists.

### 15. India

- **Volume:** 398 live (JobsPipe, 10.1% of global). Wellfound shows 707 India results and Weekday about 1,088 Bangalore jobs [S61, C]. Two of Fast AI Jobs' 50 most recent rows are in India (Celonis Bangalore, Turing Hyderabad), and an August snapshot row listed TRM Labs "Senior AI Engineer (AI Automation) – India".
- **Employers:** Teradata 9, Infosys 6, TCS 5, HCLTech 4, Barclays 4, Target 4.
- **Aliases:** Gen AI Engineer (Infosys, Fractal, Talentica, D&B Chennai), Applied AI Engineer (Celonis, Cloutflow), Staff Cloud AI Engineer (Teradata).
- **Pay:** ₹9–25L for most roles (see Pay table). None of the four full-read India postings states pay; Celonis asks for a salary expectation.
- **Interview differences:** no source found.
- **Institution gate:** Talentica names IIT, NIT, BITS, VJTI, COEP and IIIT-H.
- **Years against title:** D&B Chennai asks for 5–8 years for a "Senior Gen AI Engineer" that is internally "Senior Analyst", and Celonis asks for 5–7 years for its Senior Applied AI Engineer.

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Definition: LLM product features; umbrella title with non-GenAI variants | confirmed | 14 full-text postings describe RAG, agents, LLM APIs, evals and deployment; Power Platform, Site AI, Physical AI and robotics rows exist [S27]–[S37][S62]–[S64][S1][S2][S70] | B |
| K2 | Alias list | updated | Absent from the list: "Applied AI Engineer" (6 of 42 records; 42% of Fast AI Jobs rows), "Forward Deployed AI Engineer" (22%), "Agent Engineer", "GTM AI Engineer", "Backend/AI Engineer", "Senior AI Specialist" and the Vercel "Research Engineer" retitle [S29][S30][S37][S48][S62][S70] | B |
| K3 | JobsPipe 3,944 / 1,697 / 398; Fast AI Jobs 326 at 183; LinkedIn #1 | updated | JobsPipe counts identical on 2026-11-13 [S1][S2][S3]; LinkedIn #1 confirmed [S6]; Fast AI Jobs now 352 at 188, updated 2026-11-11 [S70] | B |
| K4 | Pay: Levels.fyi P50 $154K / P75 $212.5K / P90 $280K; posted $200–275K; 0.55× MLE; Google gap 26–39% | updated | US $155K / $211K / $280K [S10]; ML Engineer $285,650 gives 0.54× [S66]; Google MLE premium is +21–26% (AI Engineer $240K against $290–302K) [S11][S12]; sample median midpoint $200.6K [S30]…[S48] | B/M |
| K5 | India 398 live; 13.6% share; GCC alias | updated | 398 confirmed; share is 10.1% on 398/3,944 [S1][S3]; Gen AI Engineer alias seen at Infosys, Fractal, Talentica and D&B Chennai; a GCC-specific count was not found | M |
| K6 | Bengaluru Levels.fyi P50 ₹21.4–24.5L; market ₹10–15L | confirmed | WCG ₹24.0L [S15]; AIM ₹12–15 LPA [S18]; Flexiple ₹9.2L and senior ₹21.6L [S16][S17]. P75 and P90 were not verified. | C |
| K7 | Durability judgement | unverifiable | No measurement of commoditisation found; sample mentions of evals, tracing and cost are directionally consistent but query-biased [S27]–[S37][S62]–[S64] | D |
| K8 | Footprint L5/L6 plus evaluation plane | confirmed | Orchestration, context and deployment dominate; evaluation named in 12 of 14 [S27]–[S37][S62]–[S64] | M |
| K9 | Application interview track | confirmed | Spektr loop; third-party RAG design and eval take-homes [S35][S52][S56]. "RAG with access control" appears only in an issuer exam sample [S67]. | C |
| K10 | Must skills and shares | confirmed | Python 78.4%, "Llm" 76.7%, "Agentic ai" 59.3%, RAG 54.0%, as read on JobsPipe (counted 2026-09-10) [S4]; sample Python 12/14 [S27]–[S37][S62]–[S64] | B |
| K11 | Important skills and shares | unverifiable | Only ML 39.8% and AI 37.8% (KB says 37.6%) are visible on the JobsPipe page; the other shares are not [S4] | B |
| K12 | Credentials and tiers | confirmed | AWS ML Specialty retired [S21]; AIP-C01 live [S22][S23]; AI-102 retired [S24]; Databricks live (guide 2026-03-18, USD 200, 45 items, 90 min, 2-year validity) [S67]; AI-103 beta label with a conflicting GA claim [S68][S69]; 0 of 14 postings name any | A/B |
| K13 | Prerequisites | updated | Senior label 24.6% and entry 275/3,944 = 7.0% reproduce [S4][S5]; the senior cut at 5+ years is 3–5 in postings [S27][S39][S40][S63]; degree stated in 5 of 14 against the KB's 72% | M |
| K14 | Proof of work | confirmed | "shipped, not demoed", hackathon and open-source nice-to-haves, eval emphasis, "Not prompt-only" [S29][S42][S35][S62]; hiring blogs [S52][S54][S58] | C |
| K15 | Leave out or reframe | unverifiable | No direct evidence on headline framing; Ragas is named only as a nice-to-have (2 of 14) [S31][S32] | D |

## Absences

| Item | Where I looked |
|---|---|
| AI-103 general-availability status | Microsoft Learn extracts say beta; a vendor page says GA (S68, S69); the primary pages were not opened. |
| Posting dates on Greenhouse and Lever pages | Thirteen employer pages read; none shows a date. Only a seen date is recorded. |
| Posting-count trend since 2025 | JobsPipe is a snapshot; Fast AI Jobs gives only an August to November 2026 comparison; LinkedIn growth is secondary. |
| Postings with the literal AI Engineer title at Google, Amazon, Meta, Apple, NVIDIA | 28 web searches; careers sites are JS-heavy and did not surface. |
| Non-English postings | No German, French, Spanish, Portuguese, Japanese or Korean queries run; only English WTTJ snippets seen. |
| Employer-run loops for this title at Big Tech and labs | Spektr posting; third-party hiring blogs. |
| "Context management" as an interview topic; "RAG with access control" as an interview topic | Hiring blogs S52–S56; only a certification sample question mentions per-user permissions. |
| India interview differences | Hiring and salary pages; none cover India loops. |
| Prior roles of people hired into AI Engineer roles | LinkedIn Jobs on the Rise coverage (only AI consultants' transitions shown); CallMissed (S59, C). |
| Named strongest public proof-of-work examples | Hiring blogs describe criteria but name no repositories. |
| India posted pay in the sample | Four full-read India postings (D&B Chennai, Showpad, Talentica, Celonis): none states pay. |
| Fast AI Jobs row postings (Celonis 7885808003, Fever, Metropolis, Grafana Labs and others) | The fetch tool refused links followed from the platform page, so these were not read in full. |
| Current Fast AI Jobs counts for ML Engineer, Forward Deployed Engineer and San Francisco | Only the August 2026 snapshot was seen. |

## Open Questions & Risks

- An unbiased count of evaluation, agent and RAG shares is needed; a query-neutral sample would resolve the 19% against 86% gap.
- Only 14 of 42 records are full reads; thin records carry location, title and pay only.
- Levels.fyi pages in snippets are location-scoped and sometimes mislabelled: one Miami ML Engineer page read $145K against the national $285,650.
- Mirror pages can lag employer pages. Liveness of 28 records is unverified.
- JobsPipe pages may not refresh daily. The US count matched across 2026-10-19 and 2026-11-13.
- The Fast AI Jobs August snapshot date is inferred from sibling pages, so the 28% growth figure is indicative only.
- **Strongest objections and evidence:**
  - *"The sample is search-engine biased."* True. Queries included the terms I then counted. Platform shares are used for tiers.
  - *"n = 14 is too small."* True. Intervals are about ±26 points; findings are directional.
  - *"Customer-facing roles are not AI Engineers."* Flagged and counted separately. Labs and startups use no other label, and they make up about two-thirds of the startup rows.
  - *"Levels.fyi skews to big tech."* True. Corroborated with posted bands and LCA wages.
  - *"The MLE gap is level mix."* Evidence agrees: 62–69% of the log gap disappears within Google.
  - *"Fast AI Jobs is a startup-only view."* True. It is used only for the startup segment.

## Discovered Concerns

- Search and platform lists return closed postings: 7 of 21 ATS fetches were closed, and a TIAA posting that ended 2026-04-22 still surfaced.
- Title drift at Vercel (same job ID: "AI Engineer" on one site, "Research Engineer" on another).
- Fast AI Jobs' "AI Engineer" category mixes applied, forward-deployed, GTM and robotics roles, so a platform count overstates GenAI application-engineering demand.
- Talentica's institution-tier gate is an India-specific access barrier.
- Staffing-channel pay (ApTask $80–90K) differs sharply from product-company pay for similar stacks.
- JobsPipe's JD page was counted 2026-09-10, so its skill shares are older than the live counts.
- Databricks' exam blueprint changed on 2026-03-18, and older study material may not match it.
- COI: Anthropic's own posting (JD36) is in the sample, and Claude-named tooling appears in Indicium and Robots & Pencils postings.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Mostly GenAI app work; Python near-universal | Confirmed | RAG 12/14, LLM 14/14, Python 12/14; two roles without Python [S27]–[S37][S62]–[S64] | Keep Python as Must; add TypeScript as Should |
| P2 | US base $150–250K; senior $180–260K | Updated | Median midpoint $200.6K, IQR $155–234K; senior-or-higher median $231.5K [S30]…[S48] | Lower the lower bound; sample biased high |
| P3 | Certifications rarely named | Confirmed | 0 of 14 postings [S27]–[S37][S62]–[S64] | Keep Optional/Avoid |
| P4 | Labs rarely use "AI Engineer" | Confirmed | Mistral, Anthropic and OpenAI use "Applied AI Engineer"; no literal title on Anthropic board page 1 [S29][S47][S70] | Add "Applied AI Engineer" alias |
| P5 | India 10–14%; ₹10–25L | Updated | Share 10.1%; Flexiple median ₹9.2L for GenAI Engineers [S3][S16] | Broaden low end to ₹9L |
| P6 | Within-employer gap smaller than 0.55× | Confirmed | Google ratio 0.79–0.83 against 0.54 market-wide [S11][S12][S10][S66] | Use the narrower within-employer figure |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | AI Engineer Jobs: 3,944 live roles, JobsPipe, https://jobspipe.dev/jobs/ai-engineer.md | n/d | 2026-11-13 | B | Read | single-source | Global count, industries, top companies |
| S2 | AI Engineer Jobs United States, JobsPipe, https://jobspipe.dev/jobs/ai-engineer/usa.md | n/d | 2026-11-13 | B | Extract | | US count, rows |
| S3 | AI Engineer Jobs India, JobsPipe, https://jobspipe.dev/jobs/ai-engineer/india | n/d | 2026-11-13 | B | Extract | | India count, employers |
| S4 | AI Engineer job description, JobsPipe, https://jobspipe.dev/job-description/ai-engineer | counted 2026-09-10 | 2026-11-13 | B | Extract | | Skill shares, remote, senior label |
| S5 | JobsPipe sub-pages (entry-level, senior, freelance, contract, part-time, Boston, Austin), https://jobspipe.dev/jobs/entry-level-ai-engineer.md and siblings | n/d | 2026-11-13 | B | Extract | | Counts, rows |
| S6 | LinkedIn Reveals 25 Fastest-Growing Jobs For 2026, Allwork.Space, https://allwork.space/2026/01/linkedin-reveals-25-fastest-growing-jobs-for-2026 | 2026-01-07 | 2026-11-13 | B | Extract | reports LinkedIn data | Rank, experience, remote |
| S7 | A New World of Work (Davos press release), LinkedIn News, https://news.linkedin.com/2026/2026-Davos-Press-Release | 2026-01 | 2026-11-13 | B | Extract | COI (LinkedIn's own data) | AI Engineer #1 second year |
| S8 | LinkedIn Identifies AI Engineer as Fastest-Growing Role, LetsDataScience, https://letsdatascience.com/news/linkedin-identifies-ai-engineer-as-fastest-growing-role-e82f85f1 | 2026 | 2026-11-13 | C | Extract | | 75,000 postings |
| S9 | AI engineers emerging roles, Outsource Accelerator, https://news.outsourceaccelerator.com/ai-engineers-emerging-roles/ | 2026 | 2026-11-13 | D | Extract | single-source | +143% YoY claim |
| S10 | AI Engineer Salary, Levels.fyi, https://www.levels.fyi/t/software-engineer/title/ai-engineer | 2026-11-12 (page "Updated") | 2026-11-13 | B | Read | | US percentiles and median |
| S11 | Google AI Engineer Salaries, Levels.fyi, https://www.levels.fyi/companies/google/salaries/software-engineer/title/ai-engineer | 2026-10-19 | 2026-11-13 | B | Read | | Google levels |
| S12 | Google Machine Learning Engineer Salaries (localised), Levels.fyi, https://www.levels.fyi/pt-br/companies/google/salaries/software-engineer/title/machine-learning-engineer | 2026-08-04 | 2026-11-13 | B | Extract | | $290–302K |
| S13 | Data Engineer vs Machine Learning Engineer Salary, Interview Kickstart, https://interviewkickstart.com/blogs/articles/data-engineer-vs-machine-learning-engineer-salary | 2026 | 2026-11-13 | C | Extract | quotes Levels.fyi; superseded by S66 | Earlier US ML Engineer comparator ($262K) |
| S14 | Levels.fyi AI Engineer pages for Amazon, Scale AI and Meta, https://www.levels.fyi/companies/amazon/salaries/software-engineer/title/ai-engineer | 2026-05-07 | 2026-11-13 | B | Extract | | Employer medians |
| S15 | WCG AI Engineer Salaries, Levels.fyi, https://www.levels.fyi/companies/wcg/salaries/software-engineer/title/ai-engineer | n/d | 2026-11-13 | B | Extract | single-employer | India figure |
| S16 | Generative AI Engineer Salary in Bengaluru, Flexiple, https://flexiple.com/salary/generative-ai-engineer/bengaluru | 2026-08 | 2026-11-13 | C | Extract | | n = 59 |
| S17 | AI Engineer Salary in Bengaluru, Flexiple, https://flexiple.com/salary/artificial-intelligence-engineer/bengaluru | 2026-08 | 2026-11-13 | C | Extract | | Senior median |
| S18 | AI Engineer Salary Study India 2025, AIM Research, https://reports.aimresearch.co/?p=15406 | 2025 | 2026-11-13 | C | Extract | | ₹12–15 LPA |
| S19 | AI Engineer Salary in Bengaluru, Hyring, https://hyring.com/jobseeker-toolkit/salary/ai-engineer-salary-in-bengaluru | 2026 | 2026-11-13 | D | Extract | model estimate | Percentiles |
| S20 | AI / ML engineer H-1B sponsorship, careery.pro (DOL LCA data), https://careery.pro/h1b-sponsors/role/ai-ml-engineer | to 2026-06 | 2026-11-13 | B | Extract | aggregator on filings | LCA counts, wages |
| S21 | AWS Certified Machine Learning – Specialty, AWS, https://aws.amazon.com/en/certification/certified-machine-learning-specialty | n/d | 2026-11-13 | A | Extract | | Retirement |
| S22 | Big news: AWS expands AI certification portfolio, AWS Training and Certification Blog, https://aws.amazon.com/blogs/training-and-certification/big-news-aws-expands-ai-certification-portfolio-and-updates-security-certification | edited 2026-03-17 | 2026-11-13 | A | Extract | | AIP-C01 registration |
| S23 | AWS Certification Exam Guides index, AWS, https://docs.aws.amazon.com/aws-certification/latest/examguides/aws-certification-exam-guides.html | n/d | 2026-11-13 | A | Extract | | AIP-C01 listed |
| S24 | Study guide for Exam AI-102, Microsoft Learn, https://learn.microsoft.com/certifications/resources/study-guides/ai-102 | n/d | 2026-11-13 | A | Extract | | Retirement notice |
| S25 | AI-102 vs AI-103, Open Exam Prep, https://open-exam-prep.com/blog/ai-102-vs-ai-103-which-exam-2026 | 2026-07-11 | 2026-11-13 | C | Extract | | AI-103 replacement |
| S26 | AWS ML Specialty retired, CertCrush, https://www.certcrush.app/blog/aws-machine-learning-specialty-retired-mls-c01-replacement | 2026-08-10 | 2026-11-13 | C | Extract | | AIP-C01 fee |
| S27 | Senior Gen AI Engineer (R-18860), Dun & Bradstreet, https://jobs.lever.co/dnb/187db64c-4590-4a9c-ae8b-91e27d793366 | n/d | 2026-11-13 | A | Read | | JD01 |
| S28 | AI Software Engineer II (R-18544), Dun & Bradstreet, https://jobs.lever.co/dnb/32695a2d-fdea-47fe-a3a6-400c3cbfd9a5 | n/d | 2026-11-13 | A | Read | | JD02 |
| S29 | Applied AI Engineer, Prototyping, Mistral AI, https://jobs.lever.co/mistral/ac195fdb-1731-4ce2-b47e-c1bb8c72c59d | n/d | 2026-11-13 | A | Read | | JD03 |
| S30 | Research Engineer / AI Engineer, Vercel, https://job-boards.greenhouse.io/vercel/jobs/5517523004 | n/d | 2026-11-13 | A | Read | | JD04 |
| S31 | AI Engineer, Showpad, https://job-boards.greenhouse.io/showpad/jobs/7920366 | n/d | 2026-11-13 | A | Read | | JD05 |
| S32 | AI Engineer, OfferUp, https://job-boards.greenhouse.io/offerup/jobs/7739995 | n/d | 2026-11-13 | A | Read | | JD06 |
| S33 | AI Engineer – L3, Robots & Pencils, https://job-boards.greenhouse.io/robotsandpencils/jobs/5152872008 | n/d | 2026-11-13 | A | Read | | JD07 |
| S34 | AI Engineers, Indicium AI, https://job-boards.greenhouse.io/indiciumai/jobs/4684638101 | n/d | 2026-11-13 | A | Read | COI (Claude named) | JD08 |
| S35 | AI Engineer, Spektr, https://job-boards.eu.greenhouse.io/spektr/jobs/5005915101 | n/d | 2026-11-13 | A | Read | | JD09, loop |
| S36 | Gen AI Engineer, Talentica Software, https://www.talentica.com/jobdescription/gen-ai-engineer | n/d | 2026-11-13 | A | Read | | JD10 |
| S37 | Applied AI Engineer, Microsoft (via AnitaB.org Getro mirror), https://jobs.anitab.org/companies/microsoft-2/jobs/97089626-applied-ai-engineer | 2026-10-15 | 2026-11-13 | B | Read | mirror of employer text | JD11 |
| S38 | Principal AI Engineer, Workday (startup.jobs and abilityjobs mirrors), https://startup.jobs/principal-ai-engineer-workday-8577132 | n/d | 2026-11-13 | B | Extract | mirror | JD12 |
| S39 | Senior AI Engineer, Employ (startup.jobs mirror), https://startup.jobs/ai-engineer-india-employ-7998354 | n/d | 2026-11-13 | B | Extract | mirror | JD13 |
| S40 | Senior Applied AI Engineer, Microsoft (Wellfound mirror), https://wellfound.com/jobs/4851468-senior-applied-ai-engineer | n/d | 2026-11-13 | B | Extract | mirror | JD14, visa field |
| S41 | AI Engineer Agentic & RAG Systems, Inizio Partners (Monster mirror), https://www.monster.com/job-openings/ai-engineer-ny--a95b66c7-5a28-4d12-89ea-6396ad0e7de3 | n/d | 2026-11-13 | B | Extract | mirror | JD15 |
| S42 | Sr Software Engineer, AI, NinjaTrader (startup.jobs mirror), https://startup.jobs/sr-software-engineer-ai-ninjatrader-7989072 | n/d | 2026-11-13 | B | Extract | mirror | JD16 |
| S43 | Senior AI Engineer, Pennylane (arc.dev mirror), https://arc.dev/remote-jobs/j/pennylane-senior-ai-engineer-plrdecdezz | n/d | 2026-11-13 | B | Extract | mirror | JD17 |
| S44 | Bayt India listings (Safran, Infosys, Fractal), https://www.bayt.com/en/india/jobs/genai-engineer-aws-75092004/ | n/d | 2026-11-13 | B | Extract | | JD18–JD20 |
| S45 | US pay-band mirrors (6sense, Apollo.io, Datadog, Distyl, Fieldguide, RealPage, ApTask, Ro, Bobsled), https://www.employbl.com/jobs/sr-ai-engineer-6sense-1813721 and siblings | n/d | 2026-11-13 | B | Extract | mirrors | JD21–JD29, JD39 |
| S46 | LinkedIn pages linked from JobsPipe rows (Jeppesen ForeFlight, Applied Materials, Dynatrace, Teradata, TCS, Haystack), https://www.linkedin.com/jobs/view/principal-ai-engineer-at-jeppesen-foreflight-4433279838 | n/d | 2026-11-13 | B | Extract | not opened | JD30–JD35 |
| S47 | Anthropic Greenhouse board and Applied AI Engineer postings, https://job-boards.greenhouse.io/anthropic/jobs/5111942008 | n/d | 2026-11-13 | A | Read (board) / Extract (postings) | COI (Anthropic) | JD36, board scan, AI-use policy |
| S48 | Senior Frontier Agents Engineer (Applied AI), Scale AI, https://scale.com/careers/4720478005 | n/d | 2026-11-13 | A | Extract | | JD37 |
| S49 | Senior AI Engineer – GTM, Allica Bank (RevOps Careers mirror), https://revopscareers.com/job/allica-bank-senior-ai-engineer-gtm | n/d | 2026-11-13 | B | Extract | mirror | JD38 |
| S50 | Greenhouse board indexes returned for closed jobs (Anthropic, Spektr, EggAI, Sweet Security, LTS, Indicium, Celonis), e.g. https://job-boards.eu.greenhouse.io/indiciumai?error=true | n/d | 2026-11-13 | A | Read | | Staleness |
| S51 | Lead AI Engineer, TIAA, https://careers.tiaa.org/lead-ai-engineer/job/81C04678D4A60E8E0C66BC78C5984AA5 | ended 2026-04-22 | 2026-11-13 | A | Extract | expired | Exclusion |
| S52 | How to Hire a Generative AI Engineer at a Startup, Recruiting from Scratch, https://www.recruitingfromscratch.com/blog/how-to-hire-a-generative-ai-engineer-at-a-startup-2026 | 2026-06-25 | 2026-11-13 | C | Extract | | Loop, proof |
| S53 | The Agentic System Design Interview, PromptLayer, https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/ | 2025-07-11 | 2026-11-13 | C | Extract | | Loop |
| S54 | Hiring for production AI, Alian Software, https://aliansoftware.com/en/blog/hiring-for-production-ai | n/d | 2026-11-13 | C | Extract | vendor | Proof, certificates |
| S55 | How to Hire AI Engineers, Second Talent, https://www.secondtalent.com/resources/how-to-hire-ai-engineers/ | 2026 | 2026-11-13 | C | Extract | vendor | Agent-loop question |
| S56 | What applied-AI engineer interviews test in 2026, techinterview.org, https://www.techinterview.org/post/3233476824/ai-engineer-interview-rag-agents-evals/ | 2026 | 2026-11-13 | C | Extract | | Anthropic-style loop |
| S57 | What Hiring Managers Actually Look for in AI Engineers, Gauntlet AI, https://gauntletai.com/night-school/what-hiring-managers-actually-look-for-in-ai-engineers | 2026-04-08 | 2026-11-13 | C | Extract | | Proof |
| S58 | What I look for when hiring AI engineers, Louis-François Bouchard, https://www.louisbouchard.ai/what-i-look-for-when-hiring-ai-engineers/ | 2026 | 2026-11-13 | C | Extract | | Portfolio criteria |
| S59 | Hiring AI Engineers in 2026, CallMissed, https://www.callmissed.com/blog/hiring-ai-engineers-2026 | 2026 | 2026-11-13 | C | Extract | | Pools |
| S60 | AI Engineer and Senior AI Engineer, Welcome to the Jungle (DejaBlue, Sweep), https://www.welcometothejungle.com/en/companies/dejablue/jobs/ai-engineer_paris | n/d | 2026-11-13 | B | Extract | | EU pay |
| S61 | AI Engineer Jobs in India, Wellfound and Weekday, https://wellfound.com/role/l/ai-engineer/india | n/d | 2026-11-13 | C | Extract | | India volume |
| S62 | Senior Artificial Intelligence Specialist, GR8_TECH, https://job-boards.eu.greenhouse.io/gr8tech/jobs/4784094101 | n/d | 2026-11-13 | A | Read | | JD40 |
| S63 | AI Engineer, Guardz, https://job-boards.eu.greenhouse.io/guardz/jobs/4488055101 | n/d | 2026-11-13 | A | Read | | JD41 |
| S64 | Senior Applied AI Engineer, Celonis, https://job-boards.greenhouse.io/celonis/jobs/7788209003 | n/d | 2026-11-13 | A | Read | | JD42 |
| S65 | Indicium AI jobs board (31 jobs) and AI Engineer, Lisbon, https://job-boards.eu.greenhouse.io/indiciumai/jobs/4695065101 | n/d | 2026-11-13 | A | Read | COI (Claude named) | Title mix, duplicate text, Portugal right-to-work |
| S66 | Machine Learning Engineer Salary, Levels.fyi, https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer | 2026-11-12 (page "Updated") | 2026-11-13 | B | Read | | US ML Engineer percentiles |
| S67 | Databricks Certified Generative AI Engineer Associate Exam Guide (Mar26), Databricks, https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf | live version as of 2026-03-18 | 2026-11-13 | A | Read | | Exam facts, blueprint, sample questions |
| S68 | Azure AI Apps and Agents Developer Associate (AI-103) certification and exam pages, Microsoft Learn, https://learn.microsoft.com/credentials/certifications/exams/ai-103/ ; announcement, Microsoft TechCommunity, https://techcommunity.microsoft.com/t5/the-skills-hub-blog/new-microsoft-certified-azure-ai-app-and-agent-developer/ba-p/4494126 | announcement updated 2026-04-16 | 2026-11-13 | A | Extract | crawl dates unknown | AI-103 beta label |
| S69 | AI-103 FAQ, MSCertQuiz, https://mscertquiz.com/certifications/ai-103 | 2026 | 2026-11-13 | C | Extract | vendor; conflicts with S68 | GA claim, USD 165 |
| S70 | AI Engineer Jobs at AI Startups (352 open), Fast AI Jobs, https://www.fastaijobs.com/jobs/role/ai-engineer | last updated 2026-11-11 | 2026-11-13 | B | Read | single-source | Count, title mix, ATS mix |
| S71 | Fast AI Jobs index-snapshot pages (AI Engineer 275 at 170; ML Engineer 227; Forward Deployed Engineer 779 at 288; San Francisco; new-grad), https://www.fastaijobs.com/jobs/role/ml-engineer and siblings | 2026-07-27 to 2026-08-03 | 2026-11-13 | B | Extract | search-index copies; dates inferred | Growth, comparators |
| S72 | Databricks Generative AI Engineer Associate summaries (Whizlabs, TechExamLexicon), https://www.whizlabs.com/blog/databricks-generative-ai-engineer-associate-exam-guide/ | 2026-03 to 2026-04 | 2026-11-13 | C | Extract | corroborates S67 | Blueprint change on 2026-03-18, validity |

## Data Appendix

One JSON object per line. JD01–JD11 and JD40–JD42 are the 14 full-text postings used for skill shares; the other 28 `jd` records are thin (title, location, pay or snippet text) and are excluded from share denominators. `credential` records are included for K12 (a protocol record type).

```jsonl
{"type":"jd","grade":"A","src":["S27"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Dun & Bradstreet","title":"Senior Gen AI Engineer (R-18860)","url":"https://jobs.lever.co/dnb/187db64c-4590-4a9c-ae8b-91e27d793366","job_id":"R-18860","seen":"2026-11-13","location":"Chennai, India","remote":"hybrid","seniority":"senior (internally Senior Analyst)","years":"5–8 years in AI/ML engineering, data science, or software engineering, with atleast 2 years focused on GenAI","degree":null,"must":["Strong programming expertise in Python, distributed computing using PySpark, and API development","Hands on experience with LLM frameworks (LangChain, LangGraph, Transformers, OpenAI/Vertex/Bedrock SDKs)","Experience developing AI agents, retrieval pipelines, tool calling structures, or autonomous task orchestration"],"nice":null,"pay":null,"ats":"Lever","note":"JD01. Posting date not shown on the page."}
{"type":"jd","grade":"A","src":["S28"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Dun & Bradstreet","title":"AI Software Engineer II (R-18544)","url":"https://jobs.lever.co/dnb/32695a2d-fdea-47fe-a3a6-400c3cbfd9a5","job_id":"R-18544","seen":"2026-11-13","location":"Dublin, Ireland","remote":"hybrid","seniority":"senior by years","years":"8+ years of software engineering experience, with at least 3 years in AI/Generative/Agentic systems","degree":"Bachelor’s or Master’s degree in Computer Science, AI, or related field","must":["Strong proficiency in Python and industry standard AI/ML frameworks (e.g., PyTorch, TensorFlow), LLM integration, and GenAI tooling","Proven experience with cloud-native development, especially GCP and Vertex AI","Familiarity with Kubernetes (GKE), Terraform, and CI/CD pipelines (GitHub Actions, Harness)"],"nice":["Familiarity with multi-agent ecosystems, GraphRAG architecture, knowledge graphs, context-aware retrieval systems for multi-hop reasoning, semantic enrichment","MCP (Model Context Protocol) and A2A"],"pay":null,"ats":"Lever","note":"JD02."}
{"type":"jd","grade":"A","src":["S29"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Mistral AI","title":"Applied AI Engineer, Prototyping","url":"https://jobs.lever.co/mistral/ac195fdb-1731-4ce2-b47e-c1bb8c72c59d","job_id":"ac195fdb-1731-4ce2-b47e-c1bb8c72c59d","seen":"2026-11-13","location":"Paris, France","remote":"on-site","seniority":"mid","years":"2+ years experience as a hands-on engineer shipping AI-powered products (ML, software, or full-stack)","degree":null,"must":["Strong software engineering fundamentals in Python, with experience building scalable backend systems (e.g., FastAPI, Pydantic)","Comfortable working across the modern AI stack: LLMs, RAG, agentic systems, and their deployment in real-world applications","Strong track record of building and deploying production systems end to end, not just prototypes"],"nice":["Built or won hackathons / AI competitions","Contributed to open-source projects, ideally in the LLM or applied AI space"],"pay":null,"ats":"Lever","note":"JD03. Variant: customer-facing builder in the GTM Proto Team; frontier-lab employer."}
{"type":"jd","grade":"A","src":["S30"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Vercel","title":"Research Engineer (Greenhouse); AI Engineer (vercel.com/careers/ai-engineer-5517523004)","url":"https://job-boards.greenhouse.io/vercel/jobs/5517523004","job_id":"5517523004","seen":"2026-11-13","location":"Hybrid - San Francisco, New York City","remote":"hybrid","seniority":"mid","years":"3+ years of experience in research engineering, applied ML, or related fields","degree":null,"must":["Strong programming skills in Python and JavaScript/TypeScript","Experience working with or fine-tuning LLMs (OpenAI, Hugging Face, etc.)","A solid understanding of modern frontend technologies (React, Tailwind, etc.)"],"nice":null,"pay":{"lo":192000,"hi":288000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD04. Same job ID carries two titles (title drift); labelled New; research-engineering flavour."}
{"type":"jd","grade":"A","src":["S31"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Showpad","title":"AI Engineer (Software Engineer – GenAI Focused)","url":"https://job-boards.greenhouse.io/showpad/jobs/7920366","job_id":"7920366","seen":"2026-11-13","location":"Pune, India","remote":null,"seniority":"mid","years":"3–6 years of professional software engineering experience","degree":null,"must":["Strong expertise in TypeScript/JavaScript","Experience building and supporting production-grade GenAI applications","Experience with vector databases, embeddings, and RAG architectures","Experience conducting LLM evaluations and measuring model performance"],"nice":["Experience with AI evaluation frameworks such as LangSmith, Ragas, DeepEval, or equivalent","Experience optimizing LLM cost, latency, and reliability"],"pay":null,"ats":"Greenhouse","note":"JD05. TypeScript-led; Python not named."}
{"type":"jd","grade":"A","src":["S32"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"OfferUp","title":"AI Engineer (Hybrid @ Bellevue, WA or Remote @ Florida)","url":"https://job-boards.greenhouse.io/offerup/jobs/7739995","job_id":"7739995","seen":"2026-11-13","location":"Bellevue, WA or Remote (Florida)","remote":"hybrid or remote","seniority":"mid","years":"2-4 years building and deploying AI/ML systems in production; 2+ years professional Python development","degree":"Bachelor's in CS, Math, Statistics, or related field (or equivalent experience)","must":["Hands-on experience with agentic frameworks (LangChain, LangGraph, or similar) including function calling and tool-use design","Practical experience building RAG systems (vector search, semantic chunking, rerankers)","Experience with LLM APIs, prompt engineering, and structured outputs"],"nice":["LLMOps tooling: evals (Ragas, DeepEval), observability (LangSmith, Arize Phoenix), guardrails (NeMo)","GraphRAG or knowledge graph integration (Neo4j/FalkorDB)"],"pay":{"lo":140000,"hi":160000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD06."}
{"type":"jd","grade":"A","src":["S33"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Robots & Pencils","title":"AI Engineer – L3","url":"https://job-boards.greenhouse.io/robotsandpencils/jobs/5152872008","job_id":"5152872008","seen":"2026-11-13","location":"Bogota, Colombia (Remote Friendly)","remote":"remote-friendly","seniority":"mid (L3)","years":"4+ years of professional software engineering experience; 1–3 years working with applied AI/ML or LLM-powered applications","degree":"Bachelor’s degree in Computer Science, Engineering, Data Science, or equivalent experience","must":["Strong experience building backend services using Python","Experience implementing RAG workflows, prompt engineering, or LLM integrations","Familiarity with embeddings, semantic search, or vector databases"],"nice":["Familiarity with LLM evaluation or monitoring tools such as Langfuse","Experience with Azure AI services or OpenAI APIs"],"pay":null,"ats":"Greenhouse","note":"JD07. Consultancy; labelled New; names Claude (Anthropic) in tech stack (COI marker)."}
{"type":"jd","grade":"A","src":["S34","S65"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Indicium AI","title":"AI Engineers","url":"https://job-boards.greenhouse.io/indiciumai/jobs/4684638101","job_id":"4684638101","seen":"2026-11-13","location":"London, UK","remote":null,"seniority":"experienced (level not stated)","years":null,"degree":null,"must":["Hands-on experience building applications with LLM APIs and deep understanding of their capabilities, limitations, and failure modes","Practical implementation of RAG architectures, vector databases, knowledge graphs and prompt engineering","Strong Python (or other modern programming language) proficiency with production API/service development experience and cloud platform knowledge (AWS, GCP, Azure)"],"nice":["Experience with AI-assisted coding using tools like Claude Code, OpenAI Codex, Github Copilot","Experience with fine-tuning LLMs for domain-specific applications"],"pay":null,"ats":"Greenhouse (EU board)","note":"JD08. Application form asks about UK right to work without sponsorship; names Claude tooling (COI marker). A duplicate-text posting for Lisbon (4695065101) asks about Portugal right to work. Indicium's board lists 31 jobs: 2 titled AI Engineer and 4 forward-deployed AI engineer variants."}
{"type":"jd","grade":"A","src":["S35"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Spektr","title":"AI Engineer","url":"https://job-boards.eu.greenhouse.io/spektr/jobs/5005915101","job_id":"5005915101","seen":"2026-11-13","location":"Copenhagen, Denmark (same text for Iasi, ID 5005904101)","remote":null,"seniority":"mid","years":"2+ years of experience in ML, AI, or Data/Backend roles","degree":null,"must":["Strong skills in TypeScript (our core) and/or Python, with hands-on experience in frameworks like LangChain or equivalent orchestration layers","You’ve built production-grade RAG pipelines and understand the nuances of embedding, retrieval strategy, and re-ranking","You have experience setting up evaluation frameworks to measure and improve model performance"],"nice":null,"pay":null,"ats":"Greenhouse (EU board)","note":"JD09. Labelled New; process: 30-min intro, 30-min technical, 60-min technical."}
{"type":"jd","grade":"A","src":["S36"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Talentica Software","title":"Gen AI Engineer","url":"https://www.talentica.com/jobdescription/gen-ai-engineer","job_id":null,"seen":"2026-11-13","location":"India (city not stated)","remote":"remote options mentioned","seniority":"entry to mid","years":"0.5 to 3.5 years","degree":"A Bachelor's degree in Computer Science, Data Science, Mathematics, or related fields from one of India's premier institutes (IITs, NITs, VJTI, BITS Pilani, BITS Ranchi, COEP, IIIT Hyderabad)","must":["Decent understanding of GenAI models and how it works","Good hands-on experience with GenAI frameworks","Basic understanding of machine learning algorithms","Capability to evaluate GenAI-based applications"],"nice":null,"pay":null,"ats":"employer site (lead form)","note":"JD10. Institution-tier gate; page undated."}
{"type":"jd","grade":"B","src":["S37"],"as_of":"2026-10-15","ttl":"V1","role":"role:ai-engineer","employer":"Microsoft","title":"Applied AI Engineer","url":"https://apply.careers.microsoft.com/careers/job/1970393557040326","job_id":"1970393557040326","seen":"2026-11-13","location":"Redmond, WA; Atlanta, GA","remote":"on-site","seniority":"IC3","years":"2+ years technical engineering experience (preferred: 4+ years in C# and/or Python)","degree":"Bachelor's Degree in Computer Science or related technical field","must":["Build agentic AI workflows using Azure AI Foundry Agent Service and Microsoft Agent Framework","Build evaluation systems including rubrics, golden datasets, and judge agents","Write production-quality C# and Python with test-driven development"],"nice":["Master's degree in Computer Science, AI, or related field","Experience with multi-agent orchestration and agent-to-agent communication protocols"],"pay":{"lo":102100,"hi":202200,"currency":"USD","period":"year"},"ats":"Microsoft careers (read via Getro mirror)","note":"JD11. Posted 2026-10-15; SF Bay and NYC band USD 133,800–219,200; employer page not opened."}
{"type":"jd","grade":"B","src":["S38"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Workday","title":"Principal AI Engineer","url":"https://startup.jobs/principal-ai-engineer-workday-8577132","job_id":null,"seen":"2026-11-13","location":"Seattle, WA","remote":"on-site","seniority":"principal","years":"10+ years","degree":"Bachelor's (Master's or PhD preferred)","must":["3+ years of demonstrated experience working with large language models (LLMs), text generation models, and/or graph neural network models for real-world use cases","4+ years of professional experience in machine learning and deep learning frameworks & toolkits such as Pytorch, TensorFlow","6+ years of proven experience with cloud computing platforms (e.g. AWS, GCP, etc.)"],"nice":null,"pay":{"lo":188000,"hi":282000,"currency":"USD","period":"year"},"ats":"Workday (mirror read)","note":"JD12. Agent Factory team; other US band USD 190,600–342,000."}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Employ Inc.","title":"Senior AI Engineer","url":"https://startup.jobs/ai-engineer-india-employ-7998354","job_id":null,"seen":"2026-11-13","location":"Bengaluru, India","remote":"hybrid","seniority":"senior","years":"4+ years","degree":null,"must":["4+ years building AI-augmented product capabilities (LLMs, RAG systems, agents, orchestration frameworks)","Lead the architecture and delivery of end-to-end AI-powered systems, including agents, RAG pipelines, orchestration layers, and reasoning workflows"],"nice":null,"pay":null,"ats":"mirror","note":"JD13. Snippet-level read."}
{"type":"jd","grade":"B","src":["S40"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Microsoft","title":"Senior Applied AI Engineer","url":"https://wellfound.com/jobs/4851468-senior-applied-ai-engineer","job_id":null,"seen":"2026-11-13","location":"Redmond, WA","remote":"in office","seniority":"senior","years":"4 years of exp","degree":null,"must":["Python","C#","RAG Pipelines","Agent Workflows","LLM Orchestration"],"nice":null,"pay":{"lo":119000,"hi":234000,"currency":"USD","period":"year"},"ats":"Microsoft careers (Wellfound mirror)","note":"JD14. Wellfound field: Visa Sponsorship Not Available; skills are listing tags."}
{"type":"jd","grade":"B","src":["S41"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Inizio Partners","title":"AI Engineer – Agentic & RAG Systems","url":"https://www.monster.com/job-openings/ai-engineer-ny--a95b66c7-5a28-4d12-89ea-6396ad0e7de3","job_id":null,"seen":"2026-11-13","location":"Remote (New York listed)","remote":"remote","seniority":"mid","years":null,"degree":null,"must":["Strong proficiency in Python (FastAPI, Flask, asyncio) and GCP experience is good to have","Demonstrated hands-on RAG implementation experience with specific tools, models, and evaluation metrics."],"nice":null,"pay":{"lo":null,"hi":160000,"currency":"USD","period":"year"},"ats":"mirror","note":"JD15. Up to USD 160k base plus 12% bonus; US citizens or green card holders only; listing 30+ days old; liveness unverified."}
{"type":"jd","grade":"B","src":["S42"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"NinjaTrader","title":"Sr. Software Engineer, AI (internal forward-deployed AI Engineer)","url":"https://startup.jobs/sr-software-engineer-ai-ninjatrader-7989072","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":"senior","years":null,"degree":null,"must":["Production LLM application experience with Anthropic or OpenAI SDKs — agents, structured outputs, tool use, RAG, evals, batch processing — shipped, not demoed"],"nice":null,"pay":null,"ats":"Greenhouse (mirror read)","note":"JD16. Snippet-level read; Anthropic SDK named (COI marker)."}
{"type":"jd","grade":"B","src":["S43"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Pennylane","title":"Senior AI Engineer","url":"https://arc.dev/remote-jobs/j/pennylane-senior-ai-engineer-plrdecdezz","job_id":null,"seen":"2026-11-13","location":"Remote (France, Germany, Ireland, Spain, UK)","remote":"remote with restrictions","seniority":"senior","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"Ashby (mirror read)","note":"JD17. Salary not provided; ML & AI teams of 25+ people."}
{"type":"jd","grade":"B","src":["S44"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Safran Group","title":"GenAI Engineer - AWS","url":"https://www.bayt.com/en/india/jobs/genai-engineer-aws-75092004/","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":null,"years":null,"degree":null,"must":["GenAI & LLMs: OpenAI, Anthropic, Amazon Bedrock, HuggingFace Transformers, LangChain, RAG architectures, prompt engineering, fine-tuning","Develop robust evaluation frameworks for LLM output (relevancy, faithfulness, summarization, contextual accuracy)"],"nice":null,"pay":null,"ats":"mirror","note":"JD18. Location not shown in extract."}
{"type":"jd","grade":"B","src":["S44"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Infosys","title":"Gen AI Engineer (Generative AI / LLMOps)","url":"https://www.bayt.com/en/india/jobs/gen-ai-engineer-74985155/","job_id":null,"seen":"2026-11-13","location":"Bengaluru, India","remote":null,"seniority":null,"years":null,"degree":null,"must":["hands-on experience in building, deploying, monitoring, and optimizing Large Language Model (LLM) applications in production environments"],"nice":null,"pay":null,"ats":"mirror","note":"JD19. Bayt shows 2026/09/30 beside the listing; likely closed; Monster mirror variant states 2-5 years."}
{"type":"jd","grade":"B","src":["S44"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Fractal Analytics","title":"Gen AI Engineer","url":"https://www.bayt.com/en/india/jobs/gen-ai-engineer-75168090/","job_id":null,"seen":"2026-11-13","location":"Bengaluru, India","remote":null,"seniority":null,"years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"mirror","note":"JD20. Title and location only."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"6sense","title":"Sr AI Engineer","url":"https://www.employbl.com/jobs/sr-ai-engineer-6sense-1813721","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":"senior","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":179400,"hi":248120,"currency":"USD","period":"year"},"ats":"mirror","note":"JD21. Location not shown; USD band."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Apollo.io","title":"Staff AI Engineer","url":"https://www.workingnomads.com/jobs/staff-ai-engineer-apolloio-1252328","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":"staff","years":null,"degree":null,"must":["responsible for building and productionizing advanced AI systems powered by Large Language Models (LLMs) and intelligent agents"],"nice":null,"pay":null,"ats":"mirror","note":"JD22. Snippet-level read."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Datadog","title":"Staff AI Engineer - Notebooks","url":"https://agentic-engineering-jobs.com/jobs/staff/us","job_id":null,"seen":"2026-11-13","location":"United States","remote":null,"seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":234000,"hi":300000,"currency":"USD","period":"year"},"ats":"aggregator row","note":"JD23. Title and pay only."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Distyl AI","title":"AI Engineer, Evaluation","url":"https://hotfix.jobs/jobs/ai-engineer-evaluation-at-distyl-ai-f6b322a2-816f-43c9-8487-e15edbac454c","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":null,"years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":150000,"hi":250000,"currency":"USD","period":"year"},"ats":"mirror","note":"JD24. Travel 10–50%; evaluation specialisation."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Fieldguide","title":"AI Engineer, Quality (Evals)","url":"https://hotfix.jobs/jobs/ai-engineer-quality-evals-at-fieldguide-54a01151-d1f8-4597-be26-69ae94139fb2","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA (remote listed)","remote":"remote","seniority":null,"years":"3+ YOE","degree":null,"must":["Built and deployed LLM-powered features serving production traffic","Implemented evaluation frameworks for model outputs and agent behaviors"],"nice":null,"pay":{"lo":170000,"hi":220000,"currency":"USD","period":"year"},"ats":"mirror","note":"JD25. Evaluation specialisation."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Fieldguide","title":"Senior AI Engineer","url":"https://hotfix.jobs/jobs/senior-ai-engineer-at-fieldguide-9151c56f-26b1-4aba-94d0-9285e9b42e65","job_id":null,"seen":"2026-11-13","location":null,"remote":null,"seniority":"senior","years":"3+ years experience with production LLM features","degree":null,"must":null,"nice":null,"pay":null,"ats":"mirror","note":"JD26. Snippet-level read."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"RealPage","title":"AI Engineer (DFW Hybrid)","url":"https://www.wearedevelopers.com/en/jobs/ext/6304089/ai-engineer-dfw-hybrid","job_id":null,"seen":"2026-11-13","location":"Dallas-Fort Worth, TX","remote":"hybrid","seniority":null,"years":null,"degree":"Degree in Computer Science, Machine Learning, Data Science, or related field, or equivalent practical experience","must":["Python for AI/ML, data pipelines, and back-end services"],"nice":["AI experiment tracking and evaluation frameworks (e.g., OpenAI Evals, Langsmith Evals, etc.)"],"pay":{"lo":85800,"hi":146200,"currency":"USD","period":"year"},"ats":"mirror","note":"JD27. Agentic AI team."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"ApTask (staffing; client not named)","title":"AI Engineer","url":"https://www.wearedevelopers.com/jobs/ext/1477808-ai-engineer","job_id":null,"seen":"2026-11-13","location":"Plano, TX","remote":null,"seniority":"mid","years":"2+ years of experience in AI/ML Engineering, Data Science, or related field","degree":null,"must":["Experience with Azure AI ecosystem, including Azure OpenAI models and Azure AI Search","Understanding of AI ML concepts, LLMs, vector databases, RAG, agents"],"nice":null,"pay":{"lo":80000,"hi":90000,"currency":"USD","period":"year"},"ats":"mirror (Indeed-hosted)","note":"JD28. Staffing channel; listing 13 days old at mirror crawl."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Ro","title":"AI Engineer","url":"https://jobs.lever.co/ro/0b6ded09-e358-4e39-a428-a2cbf6b15cda/apply","job_id":"0b6ded09-e358-4e39-a428-a2cbf6b15cda","seen":"2026-11-13","location":"New York, NY","remote":"hybrid","seniority":null,"years":"1 year minimum (aggregator field)","degree":null,"must":null,"nice":null,"pay":{"lo":182300,"hi":220000,"currency":"USD","period":"year"},"ats":"Lever","note":"JD29. Employer page fetch returned an error; listing about 2 months old at mirror crawl; liveness unverified."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Jeppesen ForeFlight","title":"Principal AI Engineer","url":"https://www.linkedin.com/jobs/view/principal-ai-engineer-at-jeppesen-foreflight-4433279838","job_id":"4433279838","seen":"2026-11-13","location":"Austin, TX","remote":null,"seniority":"principal","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":208000,"hi":255000,"currency":"USD","period":"year"},"ats":"LinkedIn row","note":"JD30. Title, location and pay only."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Applied Materials","title":"AI Engineer - (B5)","url":"https://www.linkedin.com/jobs/view/ai-engineer-b5-at-applied-materials-4439258189","job_id":"4439258189","seen":"2026-11-13","location":"Austin, TX","remote":null,"seniority":null,"years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":172000,"hi":236500,"currency":"USD","period":"year"},"ats":"LinkedIn row","note":"JD31. Title, location and pay only."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Dynatrace","title":"Lead AI Engineer","url":"https://www.linkedin.com/jobs/view/lead-ai-engineer-at-dynatrace-4380500952","job_id":"4380500952","seen":"2026-11-13","location":"Boston, MA","remote":null,"seniority":"lead","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":150000,"hi":180000,"currency":"USD","period":"year"},"ats":"LinkedIn row","note":"JD32. Older job ID; liveness unverified."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Teradata","title":"Staff Cloud AI Engineer","url":"https://in.linkedin.com/jobs/view/staff-cloud-ai-engineer-at-teradata-4382483924","job_id":"4382483924","seen":"2026-11-13","location":"Bengaluru, India","remote":null,"seniority":"staff","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"LinkedIn row","note":"JD33. Title and location only; Teradata has 9 India rows on JobsPipe."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Tata Consultancy Services","title":"Applied AI Engineer","url":"https://www.linkedin.com/jobs/view/applied-ai-engineer-at-tata-consultancy-services-4432915001","job_id":"4432915001","seen":"2026-11-13","location":"Austin, TX","remote":null,"seniority":null,"years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":70000,"hi":130000,"currency":"USD","period":"year"},"ats":"LinkedIn row","note":"JD34. Title, location and pay only."}
{"type":"jd","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Haystack","title":"AI Engineer","url":"https://www.linkedin.com/jobs/view/ai-engineer-at-haystack-4451187278","job_id":"4451187278","seen":"2026-11-13","location":"Greater Boston","remote":null,"seniority":null,"years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":228000,"hi":270000,"currency":"USD","period":"year"},"ats":"LinkedIn row","note":"JD35. Another Haystack row (Providence County, RI) shows USD 121,000–173,000."}
{"type":"jd","grade":"B","src":["S47"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Anthropic","title":"Applied AI Engineer, Life Sciences (Beneficial Deployments)","url":"https://job-boards.greenhouse.io/anthropic/jobs/5111942008","job_id":"5111942008","seen":"2026-11-13","location":"San Francisco, CA | New York City, NY","remote":null,"seniority":"mid to senior","years":"4+ years as a Software Engineer, Forward Deployed Engineer, or technical founder","degree":null,"must":["4+ years as a Software Engineer, Forward Deployed Engineer, or technical founder — with production experience shipping systems that real users depend on."],"nice":null,"pay":null,"ats":"Greenhouse","note":"JD36. Variant: customer-facing; snippet read; liveness unverified; COI (Anthropic)."}
{"type":"jd","grade":"B","src":["S48"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Scale AI","title":"Senior Frontier Agents Engineer (Applied AI)","url":"https://scale.com/careers/4720478005","job_id":"4720478005","seen":"2026-11-13","location":"San Francisco, New York, Seattle","remote":null,"seniority":"senior","years":null,"degree":null,"must":null,"nice":null,"pay":{"lo":216000,"hi":270000,"currency":"USD","period":"year"},"ats":"Greenhouse-backed careers page","note":"JD37. Variant: agent engineering; snippet read."}
{"type":"jd","grade":"B","src":["S49"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Allica Bank","title":"Senior AI Engineer – GTM","url":"https://revopscareers.com/job/allica-bank-senior-ai-engineer-gtm","job_id":null,"seen":"2026-11-13","location":"Bengaluru, India (remote)","remote":"remote","seniority":"senior","years":null,"degree":null,"must":null,"nice":null,"pay":null,"ats":"mirror","note":"JD38. Title and location only."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Bobsled","title":"AI Engineer","url":"https://www.builtinnyc.com/job/ai-engineer/7738766","job_id":"7738766","seen":"2026-11-13","location":"New York (Built In NYC listing)","remote":null,"seniority":null,"years":null,"degree":null,"must":["Demonstrated experience tuning LLM applications: prompt engineering, evals, retrieval, agent design, or similar"],"nice":null,"pay":null,"ats":"mirror","note":"JD39. Text-to-SQL accuracy focus."}
{"type":"jd","grade":"A","src":["S62"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"GR8_TECH","title":"Senior Artificial Intelligence Specialist (Senior AI / Generative AI Engineer)","url":"https://job-boards.eu.greenhouse.io/gr8tech/jobs/4784094101","job_id":"4784094101","seen":"2026-11-13","location":"Anywhere (remote-first)","remote":"remote","seniority":"senior","years":null,"degree":null,"must":["Proven experience building LLM-based systems in production.","Hands-on experience with: LLMs and RAG architectures, Chatbots or conversational AI systems, Tool/function calling and agent-style patterns.","Experience with context or tool-serving systems (MCP or similar)."],"nice":["Multi-agent or workflow-based systems.","Fine-tuning or adapting open-source LLMs.","Production incident ownership in AI systems."],"pay":null,"ats":"Greenhouse (EU board)","note":"JD40. Applied GenAI: 'Not research. Not prompt-only.' Application asks for gross monthly remuneration in EUR for B2B cooperation (contractor model). Stack: Python, SQL, LangChain, LangGraph, Pydantic, Langfuse, Qdrant/FAISS/OpenSearch/pgvector, AWS."}
{"type":"jd","grade":"A","src":["S63"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Guardz","title":"AI Engineer","url":"https://job-boards.eu.greenhouse.io/guardz/jobs/4488055101","job_id":"4488055101","seen":"2026-11-13","location":"Tel Aviv-Yafo, Israel","remote":null,"seniority":"senior by years","years":"5+ years of experience as a Machine Learning Engineer / Data Scientist / Software engineer or similar role, with a focus on production deployment","degree":null,"must":["1-2 years of hands-on experience working with LLMs (e.g., OpenAI GPT models, LLama, Gemini or other models).","Experience building production-grade LLM applications (e.g., RAG systems, AI agents, copilots, or chat-based workflows).","Proven ability to write and maintain production-level code in Python."],"nice":["Experience designing observability, evaluation, and monitoring for LLM agents (e.g., tracing, metrics, guardrails, offline/online evaluation).","Cybersecurity domain knowledge."],"pay":null,"ats":"Greenhouse (EU board)","note":"JD41. MCP named as a strong plus; page live at read; posting date not shown."}
{"type":"jd","grade":"A","src":["S64"],"as_of":"2026-11-13","ttl":"V1","role":"role:ai-engineer","employer":"Celonis","title":"Senior Applied AI Engineer","url":"https://job-boards.greenhouse.io/celonis/jobs/7788209003","job_id":"7788209003","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"senior","years":"5-7 years of experience in a development or engineering role, with hands-on experience in building and deploying production-level applications, bots, or automated workflows.","degree":null,"must":["Proficiency in Python or other scripting languages like Javascript and a strong understanding of its libraries for data manipulation (e.g., Pandas).","Hands-on experience with AI/automation frameworks and platforms such as Langchain, Make, Zapier, or similar tools.","A strong understanding of Large Language Models (LLMs) and a proven ability to apply advanced prompt engineering principles to solve business problems."],"nice":["Familiarity with marketing technology platforms (MarTech) such as Salesforce, HubSpot, or Marketo is a significant advantage.","Experience working in a B2B SaaS environment is a plus."],"pay":null,"ats":"Greenhouse","note":"JD42. Internal marketing-operations AI agents; low-code tools named (Make, Zapier); the application form asks for a salary expectation and whether the candidate will need immigration sponsorship."}
```

```jsonl
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S30","S32","S33","S34","S35","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"python","n":14,"count":12,"share":0.857,"source_kind":"jd-sample","tier_hint":"Must","note":"Showpad and Talentica name no Python; Celonis accepts JavaScript. Full-text postings only; query-biased sample, about ±26 pp."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S34","S35","S36","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"llm_apis","n":14,"count":14,"share":1.0,"source_kind":"jd-sample","tier_hint":"Must","note":"Coded broadly as any LLM-application building."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S31","S32","S34","S35","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"agents","n":14,"count":11,"share":0.786,"source_kind":"jd-sample","tier_hint":"Must","note":"Vercel, Robots & Pencils and Talentica are not agent-oriented."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S31","S32","S33","S34","S35","S36","S37","S62","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"rag","n":14,"count":12,"share":0.857,"source_kind":"jd-sample","tier_hint":"Must","note":"Vercel and Celonis lack RAG. Query-biased."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S30","S31","S32","S33","S34","S35","S36","S37","S62","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"evals","n":14,"count":12,"share":0.857,"source_kind":"jd-sample","tier_hint":"Important","note":"Queries contained 'evaluation'; KB platform share 19.0% not reproducible; keep Important (candidate Must) until an unbiased count."}
{"type":"skill_signal","grade":"M","src":["S32","S33","S34","S35"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"retrieval_quality","n":14,"count":4,"share":0.286,"source_kind":"jd-sample","tier_hint":"Important","note":"Rerankers, chunking or HyDE named."}
{"type":"skill_signal","grade":"M","src":["S27","S31","S32","S33","S34","S37","S62","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"observability","n":14,"count":8,"share":0.571,"source_kind":"jd-sample","tier_hint":"Important","note":"Includes monitoring and tracing wording."}
{"type":"skill_signal","grade":"M","src":["S31","S34","S35","S36","S37","S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"cost_latency","n":14,"count":6,"share":0.429,"source_kind":"jd-sample","tier_hint":"Important","note":null}
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S31","S32","S33","S34","S35","S37","S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"cloud","n":14,"count":10,"share":0.714,"source_kind":"jd-sample","tier_hint":"Important","note":"AWS, Azure or GCP named in most enterprise postings; consider Must for enterprise postings."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S31","S34","S35","S37","S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"git_ci","n":14,"count":7,"share":0.5,"source_kind":"jd-sample","tier_hint":"Important","note":null}
{"type":"skill_signal","grade":"M","src":["S27","S31","S32","S33","S34","S35","S37","S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"vector_search","n":14,"count":8,"share":0.571,"source_kind":"jd-sample","tier_hint":"Important","note":null}
{"type":"skill_signal","grade":"M","src":["S27","S28","S30","S31","S32","S33","S34","S37","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"prompt_engineering","n":14,"count":9,"share":0.643,"source_kind":"jd-sample","tier_hint":"Important","note":"GR8_TECH states 'Not prompt-only'."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S30","S32","S35","S36","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"ml_fundamentals","n":14,"count":7,"share":0.5,"source_kind":"jd-sample","tier_hint":"Important","note":"Platform 'Machine learning' 39.8% [S4]."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S32","S33","S34","S37","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"c4_responsible_ai","n":14,"count":7,"share":0.5,"source_kind":"jd-sample","tier_hint":"Important","note":"Guardrails or responsible-AI wording."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S29","S31","S32","S33","S35","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"communication","n":14,"count":8,"share":0.571,"source_kind":"jd-sample","tier_hint":"Important","note":null}
{"type":"skill_signal","grade":"M","src":["S29","S30","S31","S35","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"new:typescript","n":14,"count":5,"share":0.357,"source_kind":"jd-sample","tier_hint":"Should","note":"Must at TypeScript-led employers (Showpad, Spektr); Celonis names JavaScript as an alternative; generic language lists excluded."}
{"type":"skill_signal","grade":"M","src":["S27","S28","S31","S32","S34","S35","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"new:orchestration_frameworks","n":14,"count":10,"share":0.714,"source_kind":"jd-sample","tier_hint":"Should","note":"Mostly named as examples ('or equivalent')."}
{"type":"skill_signal","grade":"M","src":["S27","S30","S34","S35","S36","S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"new:fine_tuning","n":14,"count":6,"share":0.429,"source_kind":"jd-sample","tier_hint":"Should","note":null}
{"type":"skill_signal","grade":"M","src":["S28","S37","S62","S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"new:mcp_a2a","n":14,"count":4,"share":0.286,"source_kind":"jd-sample","tier_hint":"Should","note":"D&B Dublin (desirable), Microsoft (preferred protocols), GR8_TECH (must-have), Guardz (strong plus)."}
{"type":"skill_signal","grade":"M","src":["S64"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","skill":"new:low_code_automation","n":14,"count":1,"share":0.071,"source_kind":"jd-sample","tier_hint":"Optional","note":"Celonis names Make and Zapier beside LangChain."}
{"type":"skill_signal","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V3","role":"role:ai-engineer","skill":"python","n":null,"share":0.784,"source_kind":"platform","tier_hint":"Must","note":"JobsPipe publishes shares only; counts private."}
{"type":"skill_signal","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V3","role":"role:ai-engineer","skill":"llm_apis","n":null,"share":0.767,"source_kind":"platform","tier_hint":"Must","note":"Platform tag is 'Llm'."}
{"type":"skill_signal","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V3","role":"role:ai-engineer","skill":"agents","n":null,"share":0.593,"source_kind":"platform","tier_hint":"Must","note":"Platform tag is 'Agentic ai'."}
{"type":"skill_signal","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V3","role":"role:ai-engineer","skill":"rag","n":null,"share":0.54,"source_kind":"platform","tier_hint":"Must","note":null}
{"type":"skill_signal","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V3","role":"role:ai-engineer","skill":"ml_fundamentals","n":null,"share":0.398,"source_kind":"platform","tier_hint":"Important","note":"Platform tag 'Machine learning'; 'Artificial intelligence' is 37.8%, not 37.6% as in K11."}
{"type":"measure","grade":"B","src":["S1"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"live postings, global","unit":"postings","value":3944,"n":null,"method":"JobsPipe live index page","region":"global","note":"Identical to KB figure for 2026-10-19; page may not refresh daily."}
{"type":"measure","grade":"B","src":["S2"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"live postings, US","unit":"postings","value":1697,"n":null,"method":"JobsPipe live index page","region":"US","note":null}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"live postings, India","unit":"postings","value":398,"n":null,"method":"JobsPipe live index page","region":"India","note":null}
{"type":"measure","grade":"M","src":["S1","S3"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"India share of live postings","unit":"percent","value":10.1,"n":null,"method":"398/3,944","region":"India","note":"KB states 13.6%."}
{"type":"measure","grade":"M","src":["S1","S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"entry-level share","unit":"percent","value":7.0,"n":275,"method":"275/3,944","region":"global","note":"Matches KB 7.0%."}
{"type":"measure","grade":"M","src":["S1","S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"senior-titled query share","unit":"percent","value":34.9,"n":1377,"method":"1,377/3,944","region":"global","note":"Differs from the 24.6% senior label share in S4."}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"freelance and contract postings (each)","unit":"postings","value":197,"n":null,"method":"JobsPipe sub-pages","region":"global","note":"Part-time 21; Boston 33; Austin 45."}
{"type":"measure","grade":"B","src":["S4"],"as_of":"2026-09-10","ttl":"V1","subject":"role:ai-engineer","measure":"remote share of postings","unit":"percent","value":11.0,"n":null,"method":"JobsPipe JD page","region":"global","note":"LinkedIn reports 26% remote and 27% hybrid on a different definition [S6]."}
{"type":"measure","grade":"B","src":["S4","S1"],"as_of":"2026-09-10","ttl":"V1","subject":"role:ai-engineer","measure":"share of postings disclosing pay","unit":"percent","lo":19.6,"hi":28.1,"n":null,"method":"S4 states 19.6%; S1 states 1,107 of 3,944 publish a range (28.1%)","region":"global","note":"Different dates and corpora; conflict kept."}
{"type":"measure","grade":"B","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"open AI Engineer roles at AI startups (Fast AI Jobs)","unit":"postings","value":352,"n":null,"method":"Fast AI Jobs role page, last updated 2026-11-11","region":"global","note":"KB records 326. Category mixes applied, forward-deployed and plain AI Engineer titles."}
{"type":"measure","grade":"B","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"AI startups hiring AI Engineers (Fast AI Jobs)","unit":"companies","value":188,"n":null,"method":"Fast AI Jobs role page","region":"global","note":"KB records 183."}
{"type":"measure","grade":"B","src":["S71"],"as_of":"2026-08-03","ttl":"V1","subject":"role:ai-engineer","measure":"open AI Engineer roles at AI startups, earlier snapshot","unit":"postings","value":275,"n":null,"method":"search-index copy of the Fast AI Jobs role page (170 startups); date inferred from sibling pages updated 2026-07-27 to 2026-08-03","region":"global","note":"Snapshot date is inferred."}
{"type":"measure","grade":"M","src":["S70","S71"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"growth in AI-startup AI Engineer roles, August snapshot to 2026-11-11","unit":"percent","value":28.0,"n":null,"method":"352/275 - 1","region":"global","note":"Indicative only because the snapshot date is inferred."}
{"type":"measure","grade":"B","src":["S71"],"as_of":"2026-08-03","ttl":"V1","subject":"role:ml-engineer","measure":"open ML Engineer roles at AI startups, August snapshot","unit":"postings","value":227,"n":null,"method":"Fast AI Jobs role page copy","region":"global","note":"AI Engineer 275 is 1.21 times this figure (M)."}
{"type":"measure","grade":"B","src":["S71"],"as_of":"2026-08-03","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"open Forward Deployed Engineer roles at AI startups, August snapshot","unit":"postings","value":779,"n":null,"method":"Fast AI Jobs role page copy (288 startups)","region":"global","note":"Adjacent role."}
{"type":"measure","grade":"M","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"Applied AI Engineer family share of the 50 most recent Fast AI Jobs rows","unit":"percent","value":42.0,"n":50,"method":"title classification of 21 of 50 rows","region":"global","note":"Forward-deployed 22% (11); plain AI/Senior/Staff AI Engineer 26% (13); other 10% (5)."}
{"type":"measure","grade":"M","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"forward-deployed title share of the 50 most recent Fast AI Jobs rows","unit":"percent","value":22.0,"n":50,"method":"11 of 50 rows","region":"global","note":null}
{"type":"measure","grade":"M","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"plain AI Engineer title share of the 50 most recent Fast AI Jobs rows","unit":"percent","value":26.0,"n":50,"method":"13 of 50 rows","region":"global","note":null}
{"type":"measure","grade":"M","src":["S70"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"Greenhouse-hosted share of the 50 most recent Fast AI Jobs rows","unit":"percent","value":64.0,"n":50,"method":"32 of 50 rows; Ashby 36% (18)","region":"global","note":"Includes company sites carrying a Greenhouse job ID."}
{"type":"measure","grade":"B","src":["S6","S7"],"as_of":"2026-01-07","ttl":"V3","subject":"role:ai-engineer","measure":"LinkedIn Jobs on the Rise 2026 rank","unit":"rank of 25","value":1,"n":25,"method":"LinkedIn ranking of roles","region":"US","note":"Median experience 3.7 years; groups AI engineers with ML engineers."}
{"type":"measure","grade":"C","src":["S8"],"as_of":"2026-01-01","ttl":"V3","subject":"role:ai-engineer","measure":"LinkedIn AI-engineer postings added 2023–2025","unit":"postings","value":75000,"n":null,"method":"secondary summary of LinkedIn report","region":"US","note":"Of 639,000 AI-related postings."}
{"type":"measure","grade":"B","src":["S20"],"as_of":"2026-06-30","ttl":"V3","subject":"role:ai-engineer","measure":"certified H-1B LCAs, AI/ML engineer family","unit":"LCAs","value":8275,"n":8275,"method":"DOL LCA disclosure, FY2025 to FY2026 Q3, title match","region":"US","note":"529 titled AI ENGINEER; CA 3,853, TX 793, WA 698, NY 665, MA 281; applications, not workers."}
{"type":"measure","grade":"M","src":["S20"],"as_of":"2026-06-30","ttl":"V3","subject":"role:ai-engineer","measure":"California share of LCAs","unit":"percent","value":46.6,"n":8275,"method":"3,853/8,275","region":"US","note":null}
{"type":"measure","grade":"M","src":["S28","S32","S33","S36","S37"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer","measure":"full-text postings stating a degree","unit":"share","value":0.357,"n":14,"method":"5 of 14","region":"mixed","note":"KB cites 72% [T0-06]; not reproducible; about ±26 pp."}
{"type":"measure","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S35","S36","S37","S38","S39","S40","S45","S47","S63","S64"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer","measure":"stated minimum years of experience, median","unit":"years","value":3,"n":21,"method":"median of stated minimums across full-read and thin records; range 0.5 to 10","region":"mixed","note":"Twelve full-read postings that state a minimum have a median of 3."}
{"type":"measure","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S34","S35","S36","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer","measure":"postings naming a certification","unit":"share","value":0.0,"n":14,"method":"0 of 14","region":"mixed","note":"Thin records cannot show absence."}
{"type":"measure","grade":"M","src":["S50"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"ATS fetches that returned the board index (job closed)","unit":"percent","value":33.3,"n":21,"method":"7 of 21 fetches","region":"mixed","note":"One further fetch returned an error."}
{"type":"measure","grade":"M","src":["S1","S2","S5","S70"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"off-role titles among JobsPipe sample rows","unit":"percent","lo":8.9,"hi":19.6,"n":56,"method":"5 clearly off-role (Site AI x2, Power Platform x2, Physical AI x1) to 11 including ambiguous titles; title only","region":"mixed","note":"Floor and ceiling, not a content-based share. Fast AI Jobs' 50-row sample adds 1 robotics row (Figure AI)."}
{"type":"measure","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S34","S35","S36","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:rag-and-retrieval","measure":"share of full-text postings","unit":"share","value":0.857,"n":14,"method":"12 of 14","region":"mixed","note":"Query-biased."}
{"type":"measure","grade":"M","src":["S28","S34"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:graph-rag-and-knowledge-graphs","measure":"share of full-text postings","unit":"share","value":0.143,"n":14,"method":"2 of 14 (D&B Dublin, Indicium)","region":"mixed","note":null}
{"type":"measure","grade":"M","src":["S33","S34"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:document-parsing-and-ingestion","measure":"share of full-text postings","unit":"share","value":0.143,"n":14,"method":"2 of 14 (Robots & Pencils, Indicium)","region":"mixed","note":null}
{"type":"measure","grade":"M","src":["S27"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:context-engineering","measure":"share of full-text postings","unit":"share","value":0.071,"n":14,"method":"1 of 14 (D&B Chennai)","region":"mixed","note":null}
{"type":"measure","grade":"M","src":["S30"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:coding-agents","measure":"share of full-text postings","unit":"share","value":0.071,"n":14,"method":"1 of 14 (Vercel, UI generation and code synthesis)","region":"mixed","note":null}
{"type":"measure","grade":"M","src":["S62"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:voice-and-conversational-agents","measure":"share of full-text postings","unit":"share","value":0.071,"n":14,"method":"1 of 14 (GR8_TECH, chatbots and conversational AI)","region":"mixed","note":"No voice-specific posting in the full-text set."}
{"type":"measure","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S34","S35","S36","S37","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer:spec:vector-search-infrastructure","measure":"share of full-text postings","unit":"share","value":0.0,"n":14,"method":"0 of 14","region":"mixed","note":"Vector stores appear as stack, not as the work."}
{"type":"measure","grade":"M","src":["S27","S28","S29","S30","S31","S32","S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45","S46","S47","S48","S49","S62","S63","S64"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-engineer","measure":"senior, staff, principal or lead titles in the sample","unit":"share","value":0.405,"n":42,"method":"17 of 42 records by title","region":"mixed","note":"Explicit entry-level titles: 1 of 42 (2.4%)."}
{"type":"measure","grade":"M","src":["S10","S66"],"as_of":"2026-11-12","ttl":"V3","subject":"role:ai-engineer","measure":"AI Engineer to ML Engineer total-compensation ratio, US median","unit":"ratio","value":0.543,"n":null,"method":"155,000 / 285,650","region":"US","note":"P25 0.55 (110/200); P75 0.545 (211/387); P90 0.562 (280/498)."}
{"type":"measure","grade":"M","src":["S11","S12"],"as_of":"2026-10-19","ttl":"V3","subject":"role:ai-engineer","measure":"AI Engineer to ML Engineer total-compensation ratio, Google median","unit":"ratio","lo":0.79,"hi":0.83,"n":null,"method":"240,000 / (290,000 to 301,999)","region":"US","note":"On a log scale 31–38% of the market-wide gap remains within Google."}
```

```jsonl
{"type":"credential","grade":"A","src":["S67","S72"],"as_of":"2026-11-13","ttl":"V2","id":"databricks_genai_engineer_associate","name":"Databricks Certified Generative AI Engineer Associate","issuer":"Databricks","level":"Associate","state":"active","url":"https://www.databricks.com/sites/default/files/2026-03/Databricks-Certified-Generative-AI-Engineer-Associate-Exam-Guide-Mar26.pdf","format":"45 scored multiple-choice or multiple-selection items","proctored":true,"duration_min":90,"items":45,"fee":{"amount":200,"currency":"USD"},"validity_months":24,"renewal":"retake the full live exam","prerequisites":"none required; six months of hands-on experience recommended","families":["Applied AI Engineering"],"jd_signal":{"value":0,"unit":"postings naming it","n":14,"region":"mixed","method":"full-text JD sample"},"note":"Guide version live from 2026-03-18; blueprint covers Agent Bricks, MCP servers, guardrails and MLflow tracing; tied to Databricks tooling."}
{"type":"credential","grade":"B","src":["S22","S23","S26"],"as_of":"2026-11-13","ttl":"V2","id":"aws_aip_c01","name":"AWS Certified Generative AI Developer – Professional","issuer":"AWS","level":"Professional","state":"active","url":"https://aws.amazon.com/blogs/training-and-certification/big-news-aws-expands-ai-certification-portfolio-and-updates-security-certification","exam_code":"AIP-C01","fee":{"amount":300,"currency":"USD"},"families":["Applied AI Engineering"],"jd_signal":{"value":0,"unit":"postings naming it","n":14,"region":"mixed","method":"full-text JD sample"},"note":"Beta ended 2026-03-31; standard registration opened (blog edited 2026-03-17). Fee is from a secondary source (C)."}
{"type":"credential","grade":"B","src":["S21"],"as_of":"2026-11-13","ttl":"V2","id":"aws_mls_c01","name":"AWS Certified Machine Learning – Specialty","issuer":"AWS","level":"Specialty","state":"retired","url":"https://aws.amazon.com/en/certification/certified-machine-learning-specialty","exam_code":"MLS-C01","retires":"2026-03-31","families":["Applied AI Engineering"],"note":"Last test day 2026-03-31."}
{"type":"credential","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V2","id":"microsoft_ai_102","name":"Microsoft Certified: Azure AI Engineer Associate","issuer":"Microsoft","level":"Associate","state":"retired","url":"https://learn.microsoft.com/certifications/resources/study-guides/ai-102","exam_code":"AI-102","retires":"2026-06-30","families":["Applied AI Engineering"],"note":"Retires 2026-06-30, 11:59 PM Central."}
{"type":"credential","grade":"B","src":["S68","S69","S25"],"as_of":"2026-11-13","ttl":"V2","id":"microsoft_ai_103","name":"Microsoft Certified: Azure AI Apps and Agents Developer Associate","issuer":"Microsoft","level":"Associate","state":"beta","url":"https://learn.microsoft.com/credentials/certifications/exams/ai-103/","exam_code":"AI-103","passing":"700","duration_min":120,"fee":{"amount":165,"currency":"USD"},"launched":"2026-04","families":["Applied AI Engineering"],"jd_signal":{"value":0,"unit":"postings naming it","n":14,"region":"mixed","method":"full-text JD sample"},"note":"Microsoft Learn extracts label it beta; one vendor page claims general availability (conflict kept). Duration and fee are from third-party sources (C)."}
{"type":"pay","grade":"M","src":["S30","S32","S37","S38","S40","S45","S46","S48"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"T0-48 JD sample midpoints of posted ranges","value":200575,"n":18,"note":"Biased towards pay-transparent employers."}
{"type":"pay","grade":"M","src":["S30","S32","S37","S38","S40","S45","S46","S48"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p25","currency":"USD","period":"year","basis":"base","source_name":"T0-48 JD sample midpoints of posted ranges","value":155363,"n":18,"note":"Linear interpolation."}
{"type":"pay","grade":"M","src":["S30","S32","S37","S38","S40","S45","S46","S48"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p75","currency":"USD","period":"year","basis":"base","source_name":"T0-48 JD sample midpoints of posted ranges","value":234125,"n":18,"note":"Linear interpolation."}
{"type":"pay","grade":"M","src":["S38","S40","S45","S46","S48"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"T0-48 JD sample, senior/staff/principal/lead titles","value":231500,"level":"senior+","n":7,"note":null}
{"type":"pay","grade":"M","src":["S30","S32","S37","S45","S46"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"T0-48 JD sample, non-senior titles","value":195000,"level":"mid","n":11,"note":null}
{"type":"pay","grade":"A","src":["S30"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"San Francisco, CA","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Vercel Greenhouse posting","lo":192000,"hi":288000,"employer_type":"ai-startup","n":1,"note":null}
{"type":"pay","grade":"A","src":["S32"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Bellevue, WA / Remote FL","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OfferUp Greenhouse posting","lo":140000,"hi":160000,"level":"mid","employer_type":"enterprise","n":1,"note":null}
{"type":"pay","grade":"B","src":["S37"],"as_of":"2026-10-15","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Microsoft Applied AI Engineer (IC3)","lo":102100,"hi":202200,"level":"mid","employer_type":"big-tech","n":1,"note":"SF Bay and NYC band 133,800–219,200."}
{"type":"pay","grade":"B","src":["S38"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Seattle, WA","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Workday Principal AI Engineer","lo":188000,"hi":282000,"level":"principal","employer_type":"enterprise","n":1,"note":null}
{"type":"pay","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Datadog Staff AI Engineer - Notebooks","lo":234000,"hi":300000,"level":"staff","employer_type":"enterprise","n":1,"note":null}
{"type":"pay","grade":"B","src":["S48"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"San Francisco, New York, Seattle","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Scale AI Senior Frontier Agents Engineer","lo":216000,"hi":270000,"level":"senior","employer_type":"ai-startup","n":1,"note":null}
{"type":"pay","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Boston, MA","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Dynatrace Lead AI Engineer","lo":150000,"hi":180000,"level":"lead","employer_type":"enterprise","n":1,"note":"Older job ID; liveness unverified."}
{"type":"pay","grade":"B","src":["S45"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Plano, TX","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"ApTask AI Engineer (staffing)","lo":80000,"hi":90000,"level":"mid","employer_type":"it-services","n":1,"note":"Staffing channel."}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p25","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi AI Engineer","value":110000,"n":null,"note":"Page opened; n not shown."}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi AI Engineer","value":155000,"n":null,"note":"KB records 154,000."}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p75","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi AI Engineer","value":211000,"n":null,"note":"KB records 212,500."}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p90","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi AI Engineer","value":280000,"n":null,"note":"Matches KB 280,000."}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p25","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Machine Learning Engineer (adjacent title)","value":200000,"n":null,"note":"Comparator for the pay-gap probe."}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Machine Learning Engineer (adjacent title)","value":285650,"n":null,"note":"Comparator for the pay-gap probe."}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p75","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Machine Learning Engineer (adjacent title)","value":387000,"n":null,"note":"Comparator for the pay-gap probe."}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-11-12","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p90","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Machine Learning Engineer (adjacent title)","value":498000,"n":null,"note":"Comparator for the pay-gap probe."}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-10-19","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Google AI Engineer","value":240000,"employer_type":"big-tech","n":38,"note":"Bases: L3 157,000; L5 191,000; L6 255,000."}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-10-19","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Google AI Engineer, L3","value":196000,"level":"L3","employer_type":"big-tech","n":null,"note":null}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-10-19","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Google AI Engineer, L5","value":355000,"level":"L5","employer_type":"big-tech","n":null,"note":null}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-10-19","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Google AI Engineer, L6","value":583000,"level":"L6","employer_type":"big-tech","n":null,"note":null}
{"type":"pay","grade":"B","src":["S12"],"as_of":"2026-08-04","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Google Machine Learning Engineer (adjacent title)","lo":290000,"hi":301999,"employer_type":"big-tech","n":null,"note":"Two localised pages differ; comparator for the pay-gap probe."}
{"type":"pay","grade":"B","src":["S14"],"as_of":"2026-05-07","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Amazon AI Engineer","value":200000,"employer_type":"big-tech","n":null,"note":"Median package as shown in the page extract."}
{"type":"pay","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Scale AI AI Engineer","value":124800,"employer_type":"ai-startup","n":null,"note":"Page date not shown."}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-06-30","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"DOL LCA via careery.pro, AI/ML engineer family FY2026 Q1–Q3","value":169000,"n":4459,"note":"Offered wage on filings, not pay."}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2025-09-30","ttl":"V3","role":"role:ai-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"DOL LCA via careery.pro, AI/ML engineer family FY2025","value":165350,"n":3816,"note":"Offered wage on filings, not pay."}
{"type":"pay","grade":"B","src":["S15"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Bengaluru, India","stat":"p50","currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi WCG AI Engineer","value":2399179,"n":null,"note":"Single employer; about 2 years experience."}
{"type":"pay","grade":"C","src":["S16"],"as_of":"2026-08-31","ttl":"V3","role":"role:ai-engineer","location":"Bengaluru, India","stat":"p50","currency":"INR","period":"year","basis":"tc","source_name":"Flexiple Generative AI Engineer Bengaluru","value":920000,"n":59,"note":"Middle half 600,000–2,230,000; all levels."}
{"type":"pay","grade":"C","src":["S17"],"as_of":"2026-08-31","ttl":"V3","role":"role:ai-engineer","location":"Bengaluru, India","stat":"p50","currency":"INR","period":"year","basis":"tc","source_name":"Flexiple AI Engineer Bengaluru, 6+ years","value":2160000,"level":"senior","n":null,"note":null}
{"type":"pay","grade":"C","src":["S18"],"as_of":"2025-12-31","ttl":"V3","role":"role:ai-engineer","location":"India","stat":"p50","currency":"INR","period":"year","basis":"base","source_name":"AIM Research AI Engineer Salary Study India 2025","lo":1200000,"hi":1500000,"n":null,"note":"Median stated as INR 12–15 LPA."}
{"type":"pay","grade":"D","src":["S19"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Bengaluru, India","stat":"p50","currency":"INR","period":"year","basis":"base","source_name":"Hyring India Salary Model 2026","value":2110000,"n":null,"note":"Model estimate; p25 1,430,000; p75 3,590,000."}
{"type":"pay","grade":"B","src":["S60"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Paris, France","stat":"range","currency":"EUR","period":"year","basis":"base","source_name":"Welcome to the Jungle, DejaBlue AI Engineer (more than 3 years)","lo":54000,"hi":66100,"n":1,"note":"Posting date not shown."}
{"type":"pay","grade":"B","src":["S60"],"as_of":"2026-11-13","ttl":"V3","role":"role:ai-engineer","location":"Paris, France","stat":"range","currency":"EUR","period":"year","basis":"base","source_name":"Welcome to the Jungle, Sweep Senior AI Engineer","lo":65000,"hi":75000,"level":"senior","n":1,"note":"Posting date not shown."}
{"type":"loop","grade":"A","src":["S35"],"as_of":"2026-11-13","ttl":"V3","employer":"Spektr","track":"Application","stages":["Intro call with Talent team (30 min)","Technical interview (30 min)","Technical interview (60 min)"],"formats":null,"ai_policy":null,"take_home":null,"duration":"about 2 hours of interviews","note":"Stated on the posting."}
{"type":"loop","grade":"C","src":["S56","S47"],"as_of":"2026-11-13","ttl":"V3","employer":"Anthropic (Applied AI Engineer)","track":"Application","stages":["Recruiter screen","Technical phone screen","Take-home or live coding","Customer-conversation simulation","Onsite weighted to system design"],"formats":null,"ai_policy":"Greenhouse page links an AI-usage policy and asks applicants to confirm they want to be evaluated on non-AI-assisted communication.","take_home":"take-home or live coding","duration":null,"note":"Stage list is third-party (C); policy fact from the employer page (B); COI."}
{"type":"loop","grade":"C","src":["S52"],"as_of":"2026-06-25","ttl":"V3","employer":"Generic AI-native startup (recruiter playbook)","track":"Application","stages":["Intro call (30 min)","Take-home eval exercise (3–5 hours)","Technical deep-dive: RAG system design and failure-mode analysis (90 min)","Product and mission (45 min)"],"formats":null,"ai_policy":null,"take_home":"design an evaluation framework for a real problem","duration":null,"note":"Recruiter blog, not an employer's own loop."}
{"type":"loop","grade":"C","src":["S53"],"as_of":"2025-07-11","ttl":"V3","employer":"PromptLayer (practitioner)","track":"Application","stages":["Take-home build of a working agent","Agentic system-design interview"],"formats":null,"ai_policy":null,"take_home":"build a working agent","duration":null,"note":"Practitioner blog; not an employer-wide format."}
{"type":"practice","grade":"P","src":["S29","S42","S35","S58"],"as_of":"2026-11-13","ttl":"V3","area":"résumé","tactic":"Lead with one evaluated, deployed LLM system","claim":"Postings and hiring blogs ask for shipped work with evaluation, not demos","evidence":"'shipped, not demoed' (S42); hackathon and open-source nice-to-haves (S29); 'Evaluation Obsession' (S35); portfolio criteria (S58)","verdict":"use","risk":"Big-tech postings also screen on ML fundamentals","note":null}
{"type":"practice","grade":"P","src":["S52","S54"],"as_of":"2026-11-13","ttl":"V3","area":"résumé","tactic":"Evidence-line pattern: system, corpus size, retrieval metric before and after, cost per query, p95 latency, eval-set size","claim":"Quantified evaluation lines distinguish shipped systems from demos","evidence":"Hiring blogs ask for 'a portfolio of shipped evals' and 'a failure they own'","verdict":"use-with-care","risk":"Numbers must be real and reproducible","note":"Pattern only; no invented achievements."}
{"type":"practice","grade":"P","src":["S30","S31","S35","S64"],"as_of":"2026-11-13","ttl":"V3","area":"skills","tactic":"Match the primary language to the employer stack (Python or TypeScript)","claim":"Python is near-universal but not universal","evidence":"Showpad is TypeScript-led; Spektr says TypeScript and/or Python; Talentica names none; Celonis accepts JavaScript","verdict":"use","risk":"A single-language profile may be filtered out at some employers","note":null}
{"type":"practice","grade":"M","src":["S70","S65"],"as_of":"2026-11-13","ttl":"V1","area":"job search","tactic":"Search 'Applied AI Engineer' and 'Forward Deployed AI Engineer' as well as 'AI Engineer'","claim":"At AI startups most rows labelled AI Engineer use applied or forward-deployed titles","evidence":"21 of 50 recent Fast AI Jobs rows are 'Applied AI Engineer' and 11 are forward-deployed; Indicium lists 4 forward-deployed postings against 2 'AI Engineer'","verdict":"use","risk":"Pulls in customer-facing and pre-sales roles with travel","note":"Startup segment only."}
{"type":"practice","grade":"B","src":["S21","S24"],"as_of":"2026-11-13","ttl":"V2","area":"credentials","tactic":"Skip the AWS ML Specialty and AI-102","claim":"Both are retired and cannot be earned","evidence":"AWS: last test day 2026-03-31; Microsoft Learn: retired 2026-06-30","verdict":"avoid","risk":null,"note":null}
{"type":"practice","grade":"P","src":["S67"],"as_of":"2026-11-13","ttl":"V2","area":"credentials","tactic":"Take the Databricks Generative AI Engineer Associate only when the target team runs Databricks","claim":"The exam blueprint is tied to Databricks tooling","evidence":"Issuer guide covers Agent Bricks, MCP servers and MLflow tracing; 0 of 14 postings name it","verdict":"untested","risk":"No evidence on hiring outcomes","note":null}
{"type":"practice","grade":"P","src":["S50"],"as_of":"2026-11-13","ttl":"V1","area":"job search","tactic":"Open the employer's board to confirm a posting is live before applying","claim":"Search-surfaced postings are often closed","evidence":"7 of 21 ATS fetches returned the board index","verdict":"use","risk":"Live boards can still close quickly","note":null}
{"type":"practice","grade":"D","src":["S54"],"as_of":"2026-11-13","ttl":"V3","area":"title","tactic":"Avoid 'Prompt Engineer' as the headline title","claim":"Hiring sources treat prompting as a baseline skill","evidence":"Prompt engineering is named in 9 of 14 postings as a skill; no full-read posting uses it as the title","verdict":"untested","risk":null,"note":"KB advice K15; no direct evidence either way."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"AI-103 general-availability status on Microsoft Learn's primary page","searched":"Microsoft Learn extracts (beta label), Microsoft TechCommunity, one vendor page claiming GA (S68, S69); primary pages not opened","note":"Conflict kept."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posting dates on Greenhouse and Lever pages","searched":"Thirteen employer pages read; none shows a date","note":"Only a seen date is recorded."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posting-count trend since 2025","searched":"JobsPipe (snapshot only); Fast AI Jobs August to November 2026 comparison; LinkedIn secondary coverage","note":"No 2025 series found."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Postings with the literal AI Engineer title at Google, Amazon, Meta, Apple, NVIDIA","searched":"28 web searches; careers sites are JS-heavy and did not surface","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Non-English postings","searched":"No German, French, Spanish, Portuguese, Japanese or Korean queries run","note":"Only English WTTJ snippets seen."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Employer-run loops for this title at Big Tech and labs","searched":"Spektr posting; third-party hiring blogs","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"'Context management' and 'RAG with access control' as interview topics","searched":"Hiring blogs S52–S56; only a certification sample question mentions per-user permissions","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"India interview differences","searched":"Hiring and salary pages; none cover India loops","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Prior roles of people hired into AI Engineer roles","searched":"LinkedIn Jobs on the Rise coverage (only AI consultants' transitions shown); CallMissed (S59, C)","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Named strongest public proof-of-work examples","searched":"Hiring blogs describe criteria but name no repositories","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"India posted pay in the sample","searched":"Four full-read India postings (D&B Chennai, Showpad, Talentica, Celonis): none states pay","note":null}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Fast AI Jobs row postings (Celonis 7885808003, Fever, Metropolis, Grafana Labs and others)","searched":"The fetch tool refused links followed from the platform page","note":"Not read in full."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Current Fast AI Jobs counts for ML Engineer, Forward Deployed Engineer and San Francisco","searched":"Only the August 2026 snapshot pages were seen","note":null}
```
