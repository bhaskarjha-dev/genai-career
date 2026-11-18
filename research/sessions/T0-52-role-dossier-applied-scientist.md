---
id: "T0-52"
title: "Role Dossier: Applied Scientist"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-applied-scientist"
tags: ["applied-scientist", "role-dossier", "job-postings", "pay", "interview-loop", "india"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and page fetch; no Anthropic product is in scope for this role"
evidence_window: "2020-02-01 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 14
---

# T0-52: Role Dossier: Applied Scientist

S-numbers (S1, S2 …) point to rows in the Sources & Evidence Ledger. Grades follow the protocol: A is a primary source I opened, B a platform or secondary source, C third-party analysis, D memory or anecdote, E nothing found, M my own calculation (it takes the weakest input grade), P practice-curated. The research date is 2026-11-13, the day the sources were retrieved. The brief's anchor was 2026-11-11, so the 90-day window is applied from 2026-08-13. Evidence before 2025-01-01 is flagged stale. Postings are cited by employer and job ID, and the full records are in the Data Appendix.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| 1 | Amazon and Microsoft account for most Big Tech "Applied Scientist" postings, and frontier labs rarely use the title | 70% | D |
| 2 | Amazon's US Applied Scientist II (AS II) postings require a PhD, or a Master's plus several years of experience | 75% | D |
| 3 | Pay ranges appear in US postings but almost never in European or Indian ones | 70% | D |
| 4 | Amazon AS total compensation at the mid level (L5) is in the low-to-mid $300Ks, below Google or Meta ML-engineer pay at the same level | 60% | D |
| 5 | Amazon AS loops combine ML breadth and depth, coding, system design and Leadership Principles with a Bar Raiser | 80% | D |
| 6 | A PhD is a hard requirement in most AS postings outside Amazon | 50% | D |

## Research Question

**Decision question.** What does the knowledge base need to know about the Applied Scientist role to tell a job seeker accurately what the job is, how much demand and pay it carries, what skills, proof and credentials it needs, how candidates are interviewed, how careers progress, and where the jobs are?

**Sub-questions.**
1. Variants and aliases.
2. Demand, trend and mix.
3. A dated sample of at least 30 postings, and skill shares from it.
4. Pay in the US, Europe and India.
5. Interview loop.
6. Proof of work, credentials, entry routes.
7. Progression, durability, leverage.
8. Work footprint and specialisation.
9. Geography and sponsorship.
10. Résumé signals and misconceptions.
11. India.
12. Probes: Amazon's ladder against other employers, and the PhD share.

**Scope as applied.** The role is postings titled "Applied Scientist" at any level, at technology, AI-native and frontier-class employers, classified by what they ask for. The wider "Applied Scientist" keyword market (universities, hospitals, pharma) is reported only as a contrast.

**Method.**
- I ran 29 web searches and 17 page fetches; 2 further fetches were refused because the URL had not appeared in a prior result.
- Discovery was by employer, using search-engine queries per employer and per ATS domain. Employer-owned pages were opened wherever a URL surfaced.
- The sample has 33 postings. Of these, 23 are "read" postings: 22 on pages I opened (14 individual employer or board pages, plus 8 Amazon postings shown inside Amazon Science pages) and 1 requirement list from a mirror's search snippet. Sixteen of the 23 have full requirement text and 7 have the description only. The other 10 are search-snippet level and are used only for degree, years, pay and alias evidence.
- Skill tags were coded by me from posting text, and shares were computed in a local script. The two bases are n=23 (all read) and n=16 (full requirement text). Wilson 95% intervals are about ±20 percentage points.
- Because of copyright limits, the `must` and `nice` fields in the appendix are condensed paraphrases, not verbatim phrases.

**Sampling biases.** Search-engine discovery over-represents Amazon, Microsoft, Zalando, Uber and GenAI-themed postings. It under-represents Indian-headquartered employers, enterprises and consultancies, and non-English postings. LinkedIn and Indeed counts were not retrievable.

**Falsification searches.**
- Wider-market skill shares (InterviewStack, S34).
- Indian employer titles (Walmart Global Tech India uses "Data Scientist", S52).
- Frontier-lab titles (OpenAI, Anthropic and Cohere do not use the title; Mistral does, S17 and S53).
- Microsoft AS pay on Levels.fyi (not found).
- India AS pay from 2025 (only stale items found).
- JobsPipe role pages (Data Scientist and AI Engineer pages exist; no Applied Scientist page surfaced, S57).
- Level mapping behind the K4 pay proxy (checked against Levels.fyi's leveling comparison, S59).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | In tech-employer postings the title mostly means application-layer ML and experimentation (17 of 23 read postings), not post-training (primary in 1 of 23; named in 6 of 23). Variants: Big Tech product ML, measurement science (Uber), LLM post-training or agentic work (Hippocratic AI, Zalando, Amazon KDP), and customer-facing research engineering (Mistral). In the all-keyword market, 38% of 3,146 postings sit in healthcare, education, biotech or pharma. | [S3–S17, S34] | B (shares M) |
| KF2 | Amazon's careers site listed 642 open science roles on 2026-11-13, of which 451 were in Applied Science (US 465, India 90, Europe about 40 across all science categories). Fast AI Jobs shows 23 AS roles at 15 AI startups on 2026-10-28 (39% at Pre-Seed to Series B), against 14 at 12 in a June snapshot (+64%). Zalando alone surfaced at least 14 AS postings. | [S1, S32, S33, S60, S10–S12] | A / B |
| KF3 | Degree and experience rules differ by employer. Amazon uses "PhD, or Master's + 4 years" in 7 of the 9 postings with a stated rule. Microsoft AS II is Bachelor's + 2, Master's + 1, or PhD. Uber and Zalando accept Master's + 2. Mistral requires no degree. Only 1 of 19 postings with a degree rule needs a PhD alone, and that one has an equivalent-experience clause. | [S3–S9, S11–S14, S17, S21, S22, S27, S28] | M (inputs A/B) |
| KF4 | Skill shares in full-text postings (n=16): ML fundamentals 94%, Python 88%, production deployment 75%, LLM/GenAI 69%, PyTorch 44%, statistics 44%, experimentation 38%, SQL 25%, DSA 19% (but tested in interview reports). A 3,146-posting all-keyword set puts "Statistics & Experimentation" at 44.6% as a category, in line with the sample, but shows far lower LLM (4.5%) and PyTorch (5.4%) shares because the populations differ. | Sample, [S34, S37] | M (platform C) |
| KF5 | Levels.fyi Amazon AS (US), updated 2026-08-18: total compensation L4 $245K, L5 $324K, L6 $407K, L7 $653K, median $335K. Base is flat at $164–173K, so stock drives the level gradient. Posted base bands: Amazon $136,000–$223,400, Microsoft IC3 $102,100–$219,200, Uber AS II (New York) $161,000–$179,000. On Levels.fyi's level mapping Amazon L6 aligns with Google L5, so the K4 proxy range fits senior AS pay and overstates mid-level pay. | [S30, S3, S7, S14, S59, S69] | B |
| KF6 | Only 7 of 33 postings post a pay range, all in USD. None of the 8 European or 6 Indian postings do. LCA filings show Amazon.com Services LLC filed 312 AS II LCAs in FY2024 (mean offered wage $171,690); filings are not pay. | Sample, [S44–S48] | A / B |
| KF7 | India: Amazon India (4 postings) and Microsoft IDC (2) supply all six Indian postings in the sample. Amazon's site lists 90 India science roles (14% of 642). The all-keyword market has India at 3.9%. Walmart Global Tech India uses "Data Scientist" for comparable work. No AS-specific India pay from 2025 was found. | [S1, S5, S6, S8, S9, S34, S49–S52] | B / D |
| KF8 | Interview loops reported in 2026. Amazon: a technical phone screen, then 4–6 rounds (ML breadth, ML depth, coding, team-specific system design, a Bar Raiser on Leadership Principles; PhD candidates add a research talk). Microsoft: a screen, then 3–4 rounds with coding in almost every round, including ML coding such as K-means from scratch or self-attention. Zalando: HR screen, hiring manager, then rounds on science depth, science breadth (coding), scope and collaboration. Classic ML system design is at most one slot. Amazon reportedly bars GenAI tools in interviews unless explicitly permitted. | [S37–S39, S62–S67] | C |
| KF9 | Ladders: Amazon AS I → AS II → Senior → Principal (Levels.fyi L4–L7); Microsoft AS II is IC3 and a Senior AS is L63; Zalando adds Senior Principal; Uber has AS II → Sr. Title and content diverge: Zalando "Applied Scientist" postings ask for PhD + 4 years and roadmap ownership, while Uber's AS II (marketing measurement) names no ML at all. | [S2, S7, S10, S12, S14, S30, S63] | A / B |
| KF10 | Durability is two-sided. Amazon kept 451 Applied Science openings on 2026-11-13 while cutting about 14,000 corporate roles in 2025-10 (including applied scientists per one summary), about 16,000 in 2026-01 and an undisclosed number in its AGI organisation in 2026-07. Sources disagree on whether Amazon tied the 2025 cuts to AI. | [S1, S40–S43] | B / C |
| KF11 | Sponsorship and remote work: LCA volumes and Amazon's "multiple positions" AS II requisitions show US sponsorship; Zalando offers relocation assistance. Remote work is rare: 1 of 33 postings (Ukraine only), against 9.9% remote in the all-keyword set. Microsoft AI expects four office days a week from 2026-01-26. | [S2, S8, S11, S26, S34, S44] | B / A |
| KF12 | None of the 23 read postings names a certification. AWS, Kubernetes and CI/CD appear as tools. Employers name degrees, years, publications or patents (11 of 23), and evidence of shipped systems. | Sample [S3–S18] | M |
| KF13 | Proof of work, from employer wording: shipped models with online-experiment evidence (Microsoft, Uber, Amazon); top-venue publications or patents (Amazon basic qualifications, Zalando, Microsoft preferred); and large-codebase, test and CI practice at an AI-native lab (Mistral). Amazon's own guidance (2022-01-26, stale) adds Leadership Principles and a writing exercise at senior level. | [S2, S3–S9, S17] | A / C |
| KF14 | Primary layer of the work (n=23, my judgement): application and deployment 74%, orchestration and context 13%, models and research 9%, post-training 4%. Fine-tuning or post-training is named in 26% (95% interval 13–46%). | Sample | M |

## Recommendation

Decision rules for job seekers, with the failure mode of each:

1. **Pick a variant before tailoring.** The variants are Big Tech product ML (Amazon, Microsoft, Zalando, Uber), measurement and causal science (Uber AS II, Amazon ads and pricing), and LLM post-training or agentic work (Hippocratic AI, Zalando Agentic AI, Amazon KDP). A fourth, customer-facing research engineering (Mistral), is a single-employer variant. Failure mode: a résumé aimed at all of them reads as none, and a keyword search for the title returns university and pharma roles.
2. **Route by credential.**
   - A PhD new graduate has Amazon's no-experience route (AS II) and AI-native employers.
   - A Master's holder with under four years should look first at Microsoft AS II (Master's + 1), Zalando (MSc + 2), Uber (MS + 2), and Amazon AS I or requisitions that ask for Master's + 1.
   - A Bachelor's holder has routes at Microsoft (Bachelor's + 2) and Uber (Bachelor's + 3–4 years).
   - Failure mode: templates change, the sample is small, and Amazon's "Master's + 4" will screen out Master's new graduates.
3. **Prepare the loop in five parts:** ML breadth and depth; coding in every round (easy-to-medium problems plus ML coding such as computing AUC, K-means from scratch or self-attention); team-specific system design including agentic cases; product-scope and collaboration discussions (Zalando); and Leadership Principles stories for Amazon. Do not use GenAI tools in Amazon interviews unless explicitly permitted. Failure mode: loop evidence is anecdotal (about 6 Amazon reports, about 8 Microsoft reports, about 3 Zalando reports from 2025-10 to 2026-04), and none was found for Uber, Hippocratic AI or Mistral.
4. **Build proof.** Show one shipped model or service with offline-to-online evidence. List publications or patents if you have them. For AI-native roles add large-codebase contributions with tests and CI. Failure mode: a publication-only profile passes Amazon's basic-qualification screen but lacks the "work backwards from a customer problem" evidence that Amazon's guidance describes.
5. **Price on total compensation.** Use Levels.fyi for Amazon. Expect no posted band in Europe or India. Failure mode: Levels.fyi is self-reported, base is flat across levels, and stock value moves.
6. **Search employer boards.** Use Amazon Science's category and country filters rather than keyword aggregators. Failure mode: legacy Amazon requisition IDs (2.7M–3.0M) may be stale.
7. **Treat durability as employer-cycle risk.** Keep portable skills: production ML, experimentation, LLM adaptation. Failure mode: over-rotating to LLM skills when the all-keyword market names them in 4.5% of postings.

**What would change these rules:**
- Amazon's Applied Science count leaving 300–600.
- Amazon or Microsoft changing their AS II degree templates.
- Levels.fyi Amazon L5 AS leaving $290–360K.
- India AS pay data from 2025 onwards.
- Loop evidence for Uber, Hippocratic AI or Mistral.

## Alternatives Considered

| Option | Verdict | Why |
|---|---|---|
| Report platform-only skill shares (InterviewStack, n=3,146) | Rejected as primary | The all-keyword population includes 38% healthcare, education and pharma postings. The vendor has a conflict of interest and its extraction is opaque (S34). Kept as a contrast. |
| Report only my tech-employer sample | Preferred, with disclosure | It matches the role definition. It is Big Tech-heavy (73%) and GenAI-skewed. |
| Use ML-engineer proxies for AS pay | Rejected for mid-level pay | AS-specific Levels.fyi and posted bands exist (S30, S3, S7, S14). The proxies fit only senior level once levels are mapped (KF5). |
| Treat LCA wages as pay | Rejected for pay, kept for sponsorship | Filings show what an employer filed, not what people are paid. |
| Re-score the role | Not done | The rubric thresholds were not in the brief. Counts and bands are given instead. |
| Pull LinkedIn or Indeed counts | Not possible | Blocked or no usable counts returned. |
| Use JobsPipe for an AS count | Not possible | JobsPipe has Data Scientist (5,126 live roles) and AI Engineer (3,944) pages but no Applied Scientist page surfaced (S57). |

## Detailed Findings

### 1. Definition, variants and aliases

**Definition.** As at 2026-11-13 an Applied Scientist builds and ships models or measurement systems for a product, usually inside a large technology employer. Amazon's own pages describe the work as code built and deployed in production (S58). Amazon's science guidance says applied scientists must bring algorithms to production, with software skill as a core requirement (S2). Amazon separates Applied Science (451 open roles), Data Science (75), Research Science (66) and Economics (25) (S1). The guidance describes data scientists as generalists and research and applied scientists as depth specialists (S2).

| Variant | Employers in sample | What postings ask | Grade |
|---|---|---|---|
| Big Tech applied ML (search, ads, recommenders, Alexa/AGI, vision, forecasting) | Amazon, Microsoft, Zalando | Production models, A/B tests, Python, PhD or Master's + years | A |
| Measurement and causal science | Uber AS II, Amazon FAIM and Detail Page, Zalando marketing | SQL, Python, experimental design; ML optional (Uber AS II names none) | A |
| LLM post-training and agentic | Hippocratic AI, Zalando Agentic AI, Amazon KDP Bengaluru | PyTorch, RLHF/RLVR, RAG and agents, evaluation | A / B |
| Customer-facing research engineering | Mistral AI, Amazon GenAI Innovation Center | Pre/post-training at scale, client projects, no degree required at Mistral | B / A |
| Domain-applied ML at AI startups | KoBold Metals, PhysicsX, Moloco, Garner Health, Sprinter Health (Fast AI Jobs listings, not opened) | Mining, physics simulation, ads, healthcare delivery, logistics | B |
| Keyword noise (not this role) | Universities, hospitals, pharma | Clinical and lab science | C |

**Title forms in the sample (n=33):**

| Title form | Count | Notes |
|---|---|---|
| Applied Scientist II (AS II) | 14 | Amazon (L5), Microsoft (IC3), Uber |
| Applied Scientist, unlevelled | 9 | Several are senior in content |
| Senior / Sr Applied Scientist | 7 | |
| Staff or Principal Applied Scientist | 2 | Zalando Principal and Senior Principal appear outside the sample |
| Applied Scientist I | 1 | Amazon L4 |

**Aliases outside the sample:**
- "Applied Scientist / Research Engineer" and "AI Scientist" (Mistral, S53).
- "Applied Research Scientist" (Meta, ServiceNow, S56).
- "Associate Applied Scientist" and "Applied Scientist III" (Garner Health, S60).
- "AI Applied Scientist", "Applied AI Scientist" and "Staff Applied AI Scientist" (S61).
- "Data & Applied Scientist" (Microsoft), "Applied Data Scientist" (Cresta) and "Scientist I–III" (Amazon India listings).

Volumes by alias are not measurable beyond Amazon's category counts. Grade C for the aliases.

### 2. Demand

| Measure | Region | Value | Date | Source | Grade |
|---|---|---|---|---|---|
| Amazon open science roles, all categories | Global | 642 (607 full-time, 35 internships) | 2026-11-13 | S1 | A |
| Amazon Applied Science category | Global | 451 | 2026-11-13 | S1 | A |
| Amazon AS-titled roles (my estimate: 6 of 10 listed items carry the title) | Global | about 270 (141–375) | 2026-11-13 | S1 | M |
| Amazon open science roles by country (all categories) | US / India / Europe | 465 / 90 / about 40 | 2026-11-13 | S1 | A |
| Fast AI Jobs, AS roles at AI startups | Global | 23 roles at 15 companies | 2026-10-28 | S32 | B |
| Fast AI Jobs funding-stage mix of those 23 roles | Global | Series C 35%, B 17%, A 13%, E 13%, D 9%, Seed 9%, F 4%; 39% at Pre-Seed to Series B | 2026-10-28 | S32 | B |
| Fast AI Jobs, San Francisco and Bay Area | US | 8 roles at 6 startups | 2026-10-05 | S60 | B |
| Fast AI Jobs, Series D and later | Global | 7 roles at 3 companies | 2026-10-30 | S60 | B |
| Fast AI Jobs earlier snapshot (newest role dated 2026-06-09) | Global | 14 roles at 12 companies | 2026-06 | S33 | B |
| Change between the two Fast AI Jobs readings | Global | +64% roles, +25% companies | 2026-06 to 2026-10 | S32, S33 | M |
| InterviewStack all-keyword postings | Global | 3,146 (US 1,916 = 60.9%; Singapore 6.0%; UK 5.2%; Canada 4.8%; India 3.9%; Germany 2.0%) | 2026-05 | S34 | C |
| Zalando AS-titled postings surfaced by one search (lower bound) | Germany | at least 14 | 2026-11-13 | S10–S12, S19, S20 | A (extract) |
| JobsPipe adjacent roles (no AS page surfaced) | Global | Data Scientist 5,126 live roles; AI Engineer 3,944 | 2026-11-13 | S57 | B |
| Employer mix in sample | — | Big Tech 73% (24 of 33); Zalando 15%; AI-native and frontier-class 12% | 2026-11-13 | Sample | M |
| Seniority mix, sample | — | entry 3%, mid 70%, senior 21%, staff and above 6% | 2026-11-13 | Sample | M |
| Seniority mix, all-keyword | — | entry 14.2%, mid 60.6%, senior 16.1%, staff/lead 9.1% | 2026-05 | S34 | C |
| Remote share | — | Sample 1 of 33; all-keyword remote 9.9%, hybrid 19.4%, on-site 77.1% | 2026-05/11 | Sample, S34 | M / C |

Trend since 2025: the Fast AI Jobs startup count rose (+64%), and Amazon's open count was 451 on 2026-11-13 after three rounds of corporate cuts. The Levels.fyi median rose 19.8% between the 2025-06-06 and 2026-08-18 readings ($279,722 to $335K). Level averages rose only 2–5% (L4 +1.7%, L5 +5.2%, L6 +2.8%), so most of the change looks like a shift in who reported (M, B).

### 3. Job-description sample

**Sample summary (n=33; exclusions below).**

| Employer type | US | India | Europe | Unknown | Total |
|---|---|---|---|---|---|
| Big Tech (Amazon 16, Microsoft 4, Uber 4) | 14 | 6 | 2 | 2 | 24 |
| Enterprise / retail platform (Zalando) | 0 | 0 | 5 | 0 | 5 |
| AI-native startup or scale-up (Hippocratic AI, Outreach, Squad) | 1 | 0 | 1 | 1 | 3 |
| Frontier-lab-class (Mistral AI) | 1 | 0 | 0 | 0 | 1 |
| GCC or Indian-headquartered employer; consultancy | 0 | 0 | 0 | 0 | 0 (shortfall) |
| **Total** | **16** | **6** | **8** | **3** | **33** |

Basis (grade M): 16 postings with full requirement text, 7 with description only (Amazon Science pages), 10 at snippet level. Amazon is 48% of the sample, which reflects its dominance of the title but over-weights it for skill shares.

**Window status.**
- Dated in window: Amazon 10593286, 10588542, 10591721 and 10589082 (2026-10-23 to 2026-10-25); the Microsoft Turing mirror (2026-10-16); Mistral (2026-08-17).
- Live at retrieval with no date shown: the Amazon legacy-ID pages, Microsoft, Zalando and Uber pages, and the Amazon "Work with us" feed items with IDs above 10599900 (posted after 2026-10-26).
- Over 90 days by date: Hippocratic AI Staff AS RL (2026-07-29), listed with an Apply link at retrieval.
- Window unverified: the 10 snippet-level postings. Uber Sr AS dated 2026-08-04 (101 days old) is kept for its pay band.
- Caveat: the fetch tool may serve cached copies, so liveness of undated pages is an inference.

**Excluded after reading or seeing (12):**

| Excluded | Count | Reason |
|---|---|---|
| Amazon 10593555 | 1 | Duplicate text of 10593286 |
| Amazon 10592196 (hardware-embedded perception) | 1 | Employer cap (Amazon already 16 of 33), not a different role |
| Amazon 10599924 "Pricing Optimization Scientist" | 1 | Title is not AS, although the text asks for one |
| Hippocratic AI 76929926 and 87905062 | 2 | Near-identical siblings of the Staff posting |
| Microsoft "Data & Applied Scientist II" (Hyderabad) | 1 | Data-science analytics role (SQL, Kusto, Power BI) |
| Postings dated more than 90 days before retrieval and not verified live | 6 | Microsoft AS II-AI Redmond (2025-10-28), Amazon AERO Agentic AI (2026-03-26), Alexa Edge AI (2026-05-28), Amazon IN SPS Tech (2026-07-31), Amazon Berlin Community Data & Science (2026-07-13), Uber Sr AS SF (2026-03-26) |

### 4. Skills (grade M for every row; inputs A or B)

Shares are shown as k/n. The first share column is n=23 read postings; the second is n=16 postings with full requirement text. Requirement-type skills (Python, SQL, PyTorch, degrees) are lower bounds in the first column, because 7 Amazon Science pages did not display qualification lists. "Variant" means the tier changes by role variant.

| Skill (ID) | Share, n=23 | Share, n=16 | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| ml_fundamentals | 95.7% (22/23) | 93.8% (15/16) | Must | Must | Only Uber's measurement AS II lacks ML |
| python | 60.9% (14/23) | 87.5% (14/16) | Must | Must | The two Microsoft India postings name no language |
| statistics | 34.8% (8/23) | 43.8% (7/16) | Important (Must for measurement and search variants) | Must | Interval 23–67%; platform category "Statistics & Experimentation" is 44.6% (S34) |
| pytorch | 30.4% (7/23) | 43.8% (7/16) | Important (Must for LLM post-training variant) | Must | Named in both AI-native and frontier-class postings |
| experiment_design | 34.8% (8/23) | 37.5% (6/16) | Important (Must for ads, search, product science) | Must | Named in all 3 Microsoft AS II postings and in Uber |
| dsa | 13.0% (3/23) | 18.8% (3/16) | Must for interview preparation; Should in postings | Must | Only in Amazon legacy qualifications; coding rounds reported at Amazon, Microsoft and Zalando in 2026 (C) |
| sql | 17.4% (4/23) | 25.0% (4/16) | Should | Important | KB platform share 63.8% against 25% here; named by Microsoft Hyderabad, 2 Zalando, Uber NYC |
| data_science | not coded | not coded | — | Important | Too generic to code (unverifiable) |
| data_analysis | 8.7% (2/23) | 12.5% (2/16) | Should | Important | Named in Uber postings only |
| communication | 43.5% (10/23) | 43.8% (7/16) | Important | Important | Consistent with KB platform share |
| llm_apis (proxy: RAG, agents, prompting) | 30.4% (7/23) | 31.2% (5/16) | Important (Must on agentic teams) | Important | Zalando Agentic AI, Amazon KDP and FAIM, Microsoft |
| generative_ai | 69.6% (16/23) | 68.8% (11/16) | Important | Important | Sample skew; all-keyword set shows LLMs 4.5% and GenAI 3.6% (S34) |
| research_to_prod (production deployment) | 78.3% (18/23) | 75.0% (12/16) | Must | Important | Strongest signal after ML and Python |
| eval_stats (CIs, power, pass^k) | 0% (0/23) | 0% (0/16) | Should | Important | No explicit mention; evaluation wording is under new:llm_evaluation |
| finetuning | 26.1% (6/23) | 31.2% (5/16) | Important | Important | KB platform share 13.0%; higher in LLM variants |
| causal | 13.0% (3/23) | 6.2% (1/16) | Should (Must for measurement variants) | Important | Uber, Amazon ads and Detail Page |
| research_methods | 56.5% (13/23) research or novel-algorithm wording; publications or patents 47.8% | 62.5% (10/16); 43.8% | Important | Important | Amazon basic qualifications list publications or patents |
| deep_learning | 34.8% (8/23) | 43.8% (7/16) | Important | Important | |
| ablations | 4.3% (1/23) | 6.2% (1/16) | Optional | Important | One mention (Hippocratic AI) |
| c1_pragmatism | not coded | not coded | Important (judgement) | Important | Ambiguity wording at Zalando and Mistral |
| c2_tradeoffs | not coded | not coded | Important (judgement) | Important | Trade-off communication in Microsoft and Amazon GenAI Innovation Center |
| c3_ownership | not coded | not coded | Important | Important | End-to-end ownership wording in Microsoft, Zalando and Hippocratic AI (at least 3 of 23) |
| c4_responsible_ai (safety, reliability) | 8.7% (2/23) | 12.5% (2/16) | Should | Important | Uber and Hippocratic AI |
| new:publications_patents | 47.8% (11/23) | 43.8% (7/16) | Important | — | Basic qualification at Amazon |
| new:llm_evaluation | 43.5% (10/23) | 43.8% (7/16) | Important | — | Metrics, verifiers, LLM-as-judge |
| new:software_engineering | 30.4% (7/23) | 31.2% (5/16) | Important | — | Large-codebase and production-code wording |
| new:nlp_ir_recsys | 47.8% (11/23) | 50.0% (8/16) | Should (domain) | — | |
| new:java_cpp | 26.1% (6/23) | 37.5% (6/16) | Optional | — | Amazon template accepts Python alone |
| new:mentoring_leadership | 39.1% (9/23) | 25.0% (4/16) | Should | — | Rises with seniority |
| new:big_data_spark | 17.4% (4/23) | 25.0% (4/16) | Should | — | |
| new:cloud_aws | 17.4% (4/23) | 12.5% (2/16) | Should | — | |
| new:rl | 21.7% (5/23) | 18.8% (3/16) | Should (Must for post-training variant) | — | |

No skill met an Avoid threshold.

### 5. Pay

| Population | Statistic | Value | Basis | Source | Grade |
|---|---|---|---|---|---|
| Amazon US, AS II, posted | Range | $136,000–$223,400 and $136,000–$222,200 (lowest to highest geographic market) | Base | S3, S4 | A |
| Amazon Seattle AS II requisition | Range | $163,617–$193,200 | Base | S2 | A |
| Microsoft US AS II (IC3), typical | Range | $102,100–$202,200 | Base | S7 | A |
| Microsoft AS II, SF Bay Area and NYC | Range | $133,800–$219,200 | Base | S7 | A |
| Uber AS II, New York | Range | $161,000–$179,000 | Base | S14 | A |
| Uber Sr AS, SF/NYC (2026-08-04) | Range | $190,000–$211,000 plus equity | Base | S24 | B |
| Outreach Sr AS | Range | $140,000–$175,000 | Base | S25 | B |
| Levels.fyi Amazon AS US by level | Mean | L4 $245K; L5 $324K; L6 $407K; L7 $653K; median all levels $335K | Total compensation | S30 | B |
| Levels.fyi Amazon AS US base by level | Mean | $164K; $171K; $167K; $173K (L4–L7) | Base | S30 | B |
| Same page, FAQ block | Median | $306,000 | Total compensation | S30 | B (internal inconsistency noted) |
| Levels.fyi Amazon AS, New York area | Mean | L4 $260K; L5 $353K (update date not shown) | Total compensation | S30 | B |
| Levels.fyi snapshot 2025-06-06 | Mean | L4 $241K; L5 $308K; L6 $396K; median $279,722 | Total compensation | S31 | B |
| aijobs.net, US 2025 | Median | $199,250 (n=282; basis not stated) | Unstated | S35 | B |
| ZipRecruiter, as of 2026-06-07 | Mean | $173,084 | Unstated | S36 | C |
| InterviewStack, US postings with pay (n=878), all-keyword mix | Median | $110,000 | Base | S34 | C |
| LCA, Amazon.com Services AS II, FY2024 (n=312) | Mean offered wage | $171,690 (Amazon Development Center, n=44: $175,339) | Filed base | S44 | B (filings, not pay) |
| LCA, Amazon Development Center AS II, Santa Clara, filed 2025-12-16 | Offered wage | $171,600; prevailing wage $164,403 (level II) | Filed base | S45 | B |
| LCA, Microsoft "Applied Sciences" (n=12) | Median | $247,285 (range $132,440–$276,123; titles differ) | Filed base | S47 | B |
| India, Amazon AS II Bengaluru, offer 2020-02 | Offer | Base INR 2.8M; total about INR 4.3M | Mixed | S49 | D (stale) |
| India, Amazon "Scientist II", 4–9 years, n=4 (2022-04-30) | Range | INR 4.5M–7.0M (basis not stated) | Unstated | S50 | C (stale) |
| India, Amazon software engineers, Greater Bengaluru (adjacent role) | Median | INR 6.03M (2026-04-04) | Total compensation | S51 | B |
| Europe, any employer | — | No posted band in 8 European postings | — | Sample | A |

**Notes.**
- K4's proxies (Google L5 $393–445K, Meta E5 $458K) are the knowledge base's own figures, and I did not re-verify them. On Levels.fyi's leveling comparison and a design-guide mapping, Amazon L6 aligns with Google L5 and Meta E5, and Amazon L5 aligns with Google L4 and Meta E4 (S59, S69). Amazon L6 AS ($407K) therefore sits level with the Google range and about 11% below the Meta figure (M). Amazon L5 AS ($324K) corresponds to Google L4, for which the KB gives no figure. The proxies fit senior AS pay and overstate mid-level pay if read across the same level number.
- Two sources corroborate Amazon US base: the posted bands and the LCA filings both centre near $170K for AS II.
- Total compensation at Amazon is stock-driven: base moves by $9K across L4–L7 while stock moves by $210K.

### 6. Interview loop

| Employer | Stage | What it assesses | Source | Grade |
|---|---|---|---|---|
| Amazon (US, global) | Recruiter screen; technical phone screen of about 60 minutes | Science breadth or depth, live coding (one easy-to-medium problem), Leadership Principles | S37, S64 | C |
| Amazon | Virtual onsite, 4–6 rounds of about 60 minutes | ML breadth, ML depth, coding (easy-to-medium; ML coding such as AUC), team-specific system design (one 2026-07 report adds agentic product thinking), Bar Raiser or Leadership Principles round | S37, S38, S64 | C |
| Amazon | PhD candidates | Research talk (job talk) plus Q&A | S37, S64 | C |
| Amazon India (Bengaluru intern loops, 2026) | HackerRank assessment, then rounds on research depth and on coding | Transformer fundamentals, research depth | S64, S65 | C |
| Amazon | Senior levels | Writing exercise (2022 guidance, stale) | S2 | A (stale) |
| Amazon Lab126 | Recruiter screen → technical phone → onsite → research presentation, about 3–5 weeks | Research depth and Leadership Principles | S39 | C |
| Microsoft | Screen (30–60 minutes), then a 3–4 round loop | Resume deep dive; ML fundamentals plus ML coding (K-means from scratch, self-attention); LeetCode-medium DSA; data analysis (SQL, pandas) on some teams; ML case or system design (planned in some loops, absent in one 2026-04 report); behavioural or hiring-manager round | S62, S63 | C |
| Zalando | 30-minute HR screen → hiring manager → one-hour technical → four final rounds | Science depth; science breadth with coding; scope (product-focused); collaboration | S66 | C |
| Uber, Hippocratic AI, Mistral | — | Not found (Absences) | — | E |
| Amazon (policy) | All stages | Candidates must not use GenAI tools unless explicitly permitted and may be disqualified (reported from internal guidelines, 2025-02) | S67 | B |

Glassdoor's Amazon Applied Scientist page rates the process 3.3 of 5 for difficulty, with 77% of reports positive (S64; undated, C). The KB track "classic ML system design" (K9) is only partly right. System design is one round at Amazon, sometimes absent at Microsoft and not named at Zalando, while ML breadth, ML depth, coding in nearly every round and behavioural or product-scope rounds carry most of the loops. The employer-wide loop session owns general AI-tool policies, so the policy row is a pointer only.

### 7. Proof of work

- **Amazon (2022-01-26, stale).** A science leader and Bar Raiser lists functional competencies (science breadth and depth, experience developing science applications, scripting-language coding). She adds three Leadership Principles (Learn and Be Curious, Dive Deep, Invent and Simplify) and a writing exercise for senior roles. She states that for applied research the success criterion is positive customer impact (S2; A, stale).
- **Microsoft.** Preferred wording includes a record of shipping ML features that moved business metrics, and publications or patents (S7, S8; A).
- **Uber.** Wording asks for experimentation, evaluation and production ML (S13; A).
- **Hippocratic AI.** Asks for a shipped, rigorously evaluated post-training improvement within 90 days (S16; B).
- **Mistral.** Asks for a track record from personal, professional or academic projects, large-codebase contributions, and tests and CI (S17; B).
- **K13's specifics** (three OSS code reviews, an eval-statistics write-up) have no supporting source.

### 8. Credentials

None of the 23 read postings names a certification (M). AWS, Kubernetes and CI/CD appear as tools (Zalando S11). Employers instead state degrees, years of experience and publications or patents. No employer statement about certifications for this role was found.

### 9. Entry routes and prerequisites

**Degree rules among the 19 postings that state one (M; inputs A/B):**

| Rule | Count | Employers |
|---|---|---|
| "PhD, or Master's + N years" (N = 2 or 4) | 8 | Amazon |
| A Bachelor's route exists (Bachelor's + 2 to 5 years, or Master's + 1 to 2, or PhD) | 6 | Microsoft ×2, Uber ×3, Amazon requisition |
| Master's or PhD only | 3 | Microsoft Bengaluru, Zalando process intelligence, Hippocratic AI |
| PhD (or equivalent experience) | 1 | Zalando search |
| No degree required | 1 | Mistral |

- A PhD is named as preferred or nice-to-have in 6 postings.
- At Amazon US, 5 of 7 AS II postings seen say "PhD, or Master's + 4 years", 1 says "Master's + 2" and 1 requisition says "Master's + 1 or Bachelor's + 5".
- On the probe: a PhD is the only no-experience route at Amazon (the K12 corridor), but outside Amazon it is rarely the sole route.
- PhD share among hires was not found (Absences).

**Routes by background (author judgement from the rules above; grade D/M):**

| Background | Realistic route | Basis |
|---|---|---|
| PhD research | Amazon AS II direct; AI-native; Amazon PhD internships (35 internship postings) and the Postdoctoral Science Program (S1) | A |
| Data scientist | Uber and Zalando AS roles that sit in the data-science family (SQL, Python, experimentation) | M |
| Backend engineer | Microsoft AS II (Bachelor's + 2 "related experience") if ML evidence exists | D |
| New graduate with a Master's | Microsoft (+1), Zalando (+2), Amazon AS I | A |
| Front-end, non-technical, DevOps or SRE, product management | No direct route seen: ML modelling is named in 22 of 23 read postings | D |

### 10. Progression, durability and leverage

| Employer | Ladder seen | Evidence | Grade |
|---|---|---|---|
| Amazon | AS I (L4) → AS II (L5) → Senior (L6) → Principal (L7); manager exit via Applied Science Manager postings | S2, S30 | A / B |
| Microsoft | AS II sits at IC3 within the 59–70 numbering; a Senior AS is L63 in a 2026 loop report (community mapping: 59–62 entry/mid, 63–64 senior, 65–67 principal) | S7, S55, S63 | A / C |
| Zalando | AS → Senior → Principal → Senior Principal | S10, S12 | A |
| Uber | AS II → Sr | S13, S14 | A |

**Probe (Amazon against other employers).** Levels.fyi's leveling comparison aligns Amazon L4, L5 and L6 with Google L3, L4 and L5 (S59, S69). Microsoft AS II requires Bachelor's + 2, Master's + 1 or a doctorate, while Amazon US AS II mostly requires PhD or Master's + 4. Zalando's "Applied Scientist" can carry principal-level scope, and Uber places the title in its Data Science family. The title therefore does not map one-to-one across employers.

**Durability evidence (B/C).**
- Amazon reported about 14,000 corporate cuts in 2025-10 (one summary says they included applied scientists), about 16,000 in 2026-01, and an undisclosed number of AGI-organisation cuts in 2026-07 after the AGI organisation was placed under one executive in December and its leaders departed (S40–S43).
- Amazon states large AI models remain a priority, and a report puts 2026 capital expenditure near $200B (S41).
- Sources conflict on whether the 2025 cuts were tied to AI: one report says Amazon cited AI-driven transformation, another that leaders did not (S42, S43). I keep both readings.
- Amazon still listed 451 Applied Science roles on 2026-11-13 (S1).
- I found no direct evidence of AS tasks being automated.

**Leverage (employer claims are at most C).** Amazon's FAIM role says its models move advertiser return on ad spend, Uber's measurement role sets marketing allocation, and Hippocratic AI's post-training work determines model behaviour in clinical settings (S1, S14, S16).

### 11. Work footprint and specialisations (n=23, my judgement, grade M)

| Primary layer | Count | Share |
|---|---|---|
| Application and deployment | 17 | 74% |
| Orchestration and context (agents, RAG) | 3 | 13% |
| Models and research | 2 | 9% |
| Post-training | 1 | 4% |
| Serving; infrastructure | 0 | 0% |

Evaluation and quality work is named as a task in 10 of 23 (43%). The fine-tuning and domain-adaptation specialisation is named in 6 of 23 (26%, interval 13–46%) and is the primary layer in 1 of 23.

### 12. Geography and sponsorship

- **Amazon, all science categories (n=642):** US 465 (72%), India 90 (14%), Europe about 40 (6%): UK 14, Germany 7, Luxembourg 6, Spain 5, Romania 4, Switzerland 2, Italy 1, Poland 1 (S1, A). Aggregator listings also show Amazon AS roles in Israel (Tel Aviv, Haifa), Cambridge (UK) and Toronto (S61, C).
- **Sample:** US 16, Europe 8 (Germany 5, Netherlands 1, Ukraine-only remote 1, plus 1 Amazon Berlin), India 6, unknown 3.
- **Visa sponsorship:**
  - Amazon.com Services filed 312 AS II LCAs in FY2024, and Amazon Development Center filed 44 (S44).
  - Amazon posts AS II "multiple positions" requisitions in the offered-position style, with a stated salary range and minimum requirements (Amazon 10601059, S2; others seen on a third-party copy, S29).
  - Zalando states relocation assistance (S11).
  - LCA data is A for what was filed and never evidence of pay.
- **Remote and office policy:**
  - Microsoft AI expects four office days a week from 2026-01-26 (S8).
  - Uber expects at least 50% in office (S13).
  - Hippocratic AI expects five days in office (S16).
  - Zalando states hybrid with 60% or more remote per week, varying by team (S11).

### 13. Résumé and profile signals (practice-curated, grade P)

- **Keywords taken from postings, by variant:**
  - production deployment
  - A/B testing and offline and online evaluation
  - PyTorch
  - LLM, RAG, fine-tuning and post-training
  - publications or patents
  - mentoring (for senior roles)
- **Headline pattern:** "Applied Scientist, [domain: search, ads, LLM post-training, measurement], shipped to production and A/B tested". No achievement should be invented.
- **Evidence-line pattern:** method or model, then the system it served, then the offline metric, then the online experiment result, then the business metric moved. Fill each slot with your own results.
- **Red flags:**
  - A publication list with no shipped system (K14, partly supported).
  - Claims of state of the art without baselines (no source found).
  - A title that does not match the work: Uber's AS II is measurement science, and Zalando uses "Applied Scientist" for principal-level scope.

### 14. Misconceptions and risks

| Myth or risk | Evidence |
|---|---|
| "Applied Scientist means ML research-lite" | Amazon's guidance says success is customer impact and code is core (S2); Mistral's version is a research engineer with client work (S17) |
| "The title is one job" | Uber's AS II names no ML (S14); Hippocratic AI's is RL post-training (S16); startup listings span mining, physics simulation, ads and healthcare delivery (S32) |
| "Most postings are Big Tech" | In the all-keyword market the top employers are a university, a life-sciences firm and a hospital group (S34) |
| "A PhD is required" | 1 of 19 postings with a rule requires one alone (sample) |
| "Remote work is available" | 1 of 33 postings, Ukraine only (sample) |
| "AI-tool automation is shrinking the role" | Not evidenced either way; Amazon cut roles and still listed 451 openings (S1, S40–S43) |
| "Posted pay is available everywhere" | 0 of 14 European and Indian postings post pay (sample) |
| "AI tools are welcome in the interview" | Amazon reportedly bars GenAI tools unless explicitly permitted (S67) |

### 15. India

- **Volume.** Amazon's site lists 90 India science roles (14% of 642). The all-keyword market puts India at 3.9% of postings (123 of 3,146).
- **Employer mix.** Amazon India (Bengaluru and the Karnataka development centre) and Microsoft IDC (Hyderabad, Bengaluru) supply all six Indian postings in the sample. Walmart Global Tech India titles comparable work "Data Scientist" (15 postings seen, S52). Amazon India titles also appear as "Scientist I–III" on job-portal listings. Tekion lists a Lead Applied Scientist in Bengaluru (S33; not opened).
- **Requirements.** Amazon India uses the same degree template as the US (PhD or Master's + 4 years). Microsoft Hyderabad AS II asks for Bachelor's + 2 or Master's + 1, and Microsoft Bengaluru asks for a Master's or PhD with 3–6 years.
- **Pay.** No posted band in India. AS-specific pay evidence is stale (2020–2022, D/C). Amazon software-engineer pay in Greater Bengaluru (₹6.03M median, 2026-04-04) is an adjacent B proxy only.
- **Interview.** Bengaluru reports show the same components as the US loop. Intern loops in 2026 used a HackerRank assessment and then rounds on research depth and coding (S64, S65). One 2024-11 Bengaluru full-time report (stale) describes a phone screen, one coding round, two ML design rounds and two Leadership Principles rounds with practical, non-LeetCode questions (S64). Evidence is thin, and I found no systematic India-specific difference.

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Research-to-production scientist at large tech firms | updated | Same title also used by AI-native firms, measurement science and the all-keyword market [S34, S14, S16, S17] | B |
| K2 | Aliases: Applied Research Scientist; Applied Scientist (GenAI) | updated | Level-suffixed titles, "Applied Scientist / Research Engineer", "AI Scientist", "Associate Applied Scientist", "Data & Applied Scientist", "Applied Research Scientist"; "(GenAI)" not seen as a title [S53, S56, S60, S61] | C |
| K3 | Only count: 14 at 12 AI startups; Big Tech unmeasured; "~700" untraced | updated | Fast AI Jobs 23 at 15 on 2026-10-28; Amazon 451 Applied Science on 2026-11-13; "~700" still has no primary source; JobsPipe has no AS page [S1, S32, S33, S57, S60] | A / B |
| K4 | No corpus pay; ML-engineer proxy | updated | AS-specific pay is available as of 2026-11-13: Amazon L5 $324K, L6 $407K; posted base bands; proxies fit only senior level once levels are mapped [S30, S3, S7, S14, S59, S69] | B |
| K5 | No India demand evidence | updated | Amazon lists 90 India science roles; 6 Indian postings read; India is 3.9% of the all-keyword set [S1, S34] | B |
| K6 | India pay proxy: Google MLE Bengaluru | unverifiable | Only stale AS self-reports (2020–2022) and an adjacent Amazon software-engineer figure [S49–S51] | D |
| K7 | Durability (judgement) | updated | 451 open roles against three rounds of Amazon cuts; attribution to AI disputed [S1, S40–S43] | C |
| K8 | Footprint L4 post-training, L2 research, evaluation plane | updated | Application and deployment is primary in 74%; post-training primary in 4% and named in 26% [Sample] | M |
| K9 | Track: classic ML system design | updated | System design is one of about five components at Amazon, sometimes absent at Microsoft; coding appears in almost every Microsoft round; Zalando tests depth, breadth (coding), scope and collaboration [S37–S39, S62–S66] | C |
| K10 | Must skills and shares | updated | Shares consistent within the interval (category "Statistics & Experimentation" 44.6% on the platform); statistics, PyTorch and experiment design are Important overall and Must by variant [Sample, S34] | M |
| K11 | Important skills and shares | updated | SQL 25%, LLM/GenAI 69%, ablations 4%, production deployment 75% [Sample] | M |
| K12 | Often a PhD; DSA the usual PhD gap | updated | PhD is the only no-experience route at Amazon; 1 of 19 postings requires a PhD alone; coding rounds reported at three employers [Sample, S37, S62, S66] | M |
| K13 | Proof of work it needs | unverifiable | Tests and CI supported by one posting; the OSS review count and eval-statistics write-up have no source [S17, S2] | C |
| K14 | Leave out publication lists without shipped systems; unbaselined SOTA claims | updated | Publications are named qualifications at Amazon and Zalando, so keep them and pair them with shipped systems [S2, S3–S9] | C |

## Absences

| Item | Where I looked | Result |
|---|---|---|
| Postings at GCCs or Indian-headquartered employers | Walmart Global Tech India (15 postings, all Data Scientist); combined queries for Flipkart, Intuit, Adobe, Oracle, Salesforce | None with the exact title |
| Enterprise or consultancy AS postings | Same queries | None found |
| Pay bands in European postings | 8 European postings | None posted |
| AS pay in India from 2025 | Levels.fyi Greater Bengaluru, AmbitionBox, LeetCode | Stale items only |
| Microsoft AS pay on Levels.fyi | Levels.fyi searches | Mapped to "Data Scientist"; no AS figure |
| LinkedIn, Indeed, Glassdoor posting counts | Search snippets | Blocked or no counts |
| JobsPipe Applied Scientist count | JobsPipe role pages | Data Scientist (5,126 live roles) and AI Engineer (3,944) pages exist; no Applied Scientist page surfaced |
| Typical prior roles of people hired (published analyses) | Amazon Science, InterviewStack, general search | None found |
| PhD share among hires | Same | None found |
| Loops for Uber, Hippocratic AI, Mistral AS roles | General search | None retrieved (Amazon, Microsoft and Zalando found) |
| India-specific loop differences | Glassdoor, LeetCode Discuss | Thin: few Bengaluru reports; components match the US |
| Amazon interview AI-tool policy as an official page | Search | Only reporting on internal guidelines (B) |
| Employer statements about certifications | Sample, search | None |
| Frontier-lab AS postings (OpenAI, Anthropic, Cohere, DeepMind) | One search | None; Mistral is the exception |
| Hiring-manager proof-of-work statements from 2025 onwards | Amazon Science and employer pages | Only posting wording; Amazon's named guidance is from 2022 |
| Amazon levels above L7 | Levels.fyi pages | Not seen |

## Open Questions & Risks

| Objection an expert would raise | For | Against |
|---|---|---|
| The sample is Big Tech-heavy and GenAI-skewed | LLM share is 69% here against 4.5% in the all-keyword set | The populations differ (the all-keyword set includes pharma and universities); no classified larger sample exists |
| n=23 gives wide skill intervals | Intervals are about ±20 points | Core shares agree with the KB's platform shares within interval, and the platform's category share for statistics and experimentation (44.6%) matches |
| Posting dates and liveness are weak | Many pages show no date; fetches may be cached; Amazon IDs come in two series | Pages rendered with apply paths; the newest listing items are dated |
| Levels.fyi is self-reported | Two medians appear on one page ($335K and $306K); mix shift explains most of the 19.8% rise | Posted bands and LCA wages corroborate a base near $170K |
| Amazon generalises poorly | Microsoft and Uber ladders and degree rules differ | Microsoft, Uber and Zalando are in the sample |
| InterviewStack is a conflicted vendor with opaque extraction | Self-published | Only used as a contrast |
| Glassdoor and LeetCode interview reports are anecdotal | About 6 Amazon, 8 Microsoft and 3 Zalando reports from 2025-10 to 2026-04; one Zalando report alleges a mismatch between stated requirements and what was tested | They agree on round structure within each employer |
| Level mapping is approximate | Community sources disagree on Amazon-to-Google mapping at some levels | Levels.fyi's own comparison and a design-guide mapping agree (S59, S69) |
| Layoff attribution is contested | Reports conflict on AI as a cause | Both readings kept |

Open question: the sample cannot show whether the 451 Amazon roles are net new or a rolling refresh.

## Discovered Concerns

- Amazon "multiple positions" AS II requisitions (job numbers beginning AMZ) use an offered-position format with a salary range and minimum requirements (Master's + 1, or Bachelor's + 5). They differ from the general posting template and are probably filed for sponsored hires.
- Uber places "Applied Scientist" in its Data Science family, so measurement-science variants may map to the data-scientist role rather than ML engineering.
- Amazon runs two job-ID series (legacy 2.7M–3.0M and a newer 10.5M+ series). Anyone verifying postings by ID should expect both, and legacy IDs may be stale.
- Amazon's science careers page exposes category and country counts, which make a single-source monthly demand counter.
- Mistral's "Applied Scientist" is customer-facing research engineering and may belong with another KB role.
- Hippocratic AI's AS postings are RL post-training and may map to a post-training role variant.
- Fast AI Jobs startup listings are domain-heavy (mining, physics simulation, ads, healthcare delivery, logistics), so "applied" often means domain-applied ML.
- Microsoft's loop reports show prep material from recruiters differing from the rounds actually held (one 2026-04 report), so loop guidance for this employer is less reliable.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| 1 | Amazon and Microsoft dominate; frontier labs rarely use the title | Updated | Amazon dominates (451 roles); Mistral (frontier-class) and 15 AI startups also use the title [S1, S17, S32] | Add AI-native variants |
| 2 | Amazon US AS II needs PhD or Master's + several years | Confirmed | 7 of 9 Amazon postings with a rule use "PhD, or Master's + 4" [S3, S4, S21, S22, S27, S28] | Keep as an Amazon-specific note |
| 3 | Pay posted only in US postings | Confirmed | 7 of 33 post; none of 14 European and Indian | Pay page needs levels data |
| 4 | Amazon L5 is low-to-mid $300Ks, below Google or Meta | Updated | L5 $324K (confirmed); the level-aware comparison is parity at senior level [S30, S59, S69] | K4 proxy limited to senior level |
| 5 | Loop is breadth, depth, coding, design, Leadership Principles | Confirmed | Glassdoor 2026 reports [S37, S64]; Microsoft and Zalando loops differ in detail [S62, S66] | Track description needs update |
| 6 | PhD required in most non-Amazon postings | Contradicted | 1 of 19 requires a PhD alone | K12 wording |

## Sources & Evidence Ledger

All sources were retrieved 2026-11-13 unless noted. "Extract" means only a search snippet or summary was seen.

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Careers (page 7), Amazon Science, https://www.amazon.science/careers?p=7 | live listing; postings 2026-10-23 to 2026-10-26 | 2026-11-13 | A | Read | single-source | Counts; Amazon 10593286, 10588542, 10591721, 10589082 |
| S2 | How to build a successful career as a scientist at Amazon, Amazon Science, https://amazon.science/working-at-amazon/how-to-build-a-successful-career-as-a-scientist-at-amazon | 2022-01-26 (modified 2024-07-12); feed live at retrieval | 2026-11-13 | A | Read | stale (article) | Hiring criteria; Amazon 10601059, 10601943, 10602090, 10599900 |
| S3 | Applied Scientist II, AGI Intelligent Decisions (2906278), Amazon, https://amazon.jobs/en/jobs/2906278/applied-scientist-ii-agi-intelligent-decisions | not shown | 2026-11-13 | A | Read | undated | Posting; pay; degree |
| S4 | Applied Scientist II, Generative AI Innovation Center (2773329), Amazon, https://amazon.jobs/en/jobs/2773329/applied-scientist-ii-generative-ai-innovation-center | not shown | 2026-11-13 | A | Read | undated | Posting; pay |
| S5 | Applied Scientist II, CMT Systems (2757258), Amazon, https://amazon.jobs/en/jobs/2757258/applied-scientist-ii-5365-cmt-systems | not shown | 2026-11-13 | A | Read | undated | India posting |
| S6 | Applied Scientist (2720385), Amazon, https://amazon.jobs/en/jobs/2720385/applied-scientist-amazon | not shown | 2026-11-13 | A | Read | undated | India posting |
| S7 | Applied Scientist II (Bing Places) 200034701, Microsoft AI, https://microsoft.ai/job/applied-scientist-ii-bing-places-5/ | not shown | 2026-11-13 | A | Read | undated | Posting; pay |
| S8 | Applied Scientist II 200034207, Microsoft AI, https://microsoft.ai/job/applied-scientist-ii-9/ | not shown | 2026-11-13 | A | Read | undated; text post-dates 2026-01-26 | India posting; office policy |
| S9 | Applied Scientist II 200009039, Microsoft AI, https://microsoft.ai/job/applied-scientist-ii/ | not shown | 2026-11-13 | A | Read | undated | India posting |
| S10 | Applied Scientist, Search/NLP/IR (2719998), Zalando, https://jobs.zalando.com/en/jobs/2719998 | not shown | 2026-11-13 | A | Read | undated | Posting |
| S11 | Applied Scientist (2717524), Zalando, https://jobs.zalando.com/en/jobs/2717524 | not shown | 2026-11-13 | A | Read | undated | Posting; hybrid; relocation |
| S12 | Senior Applied Scientist, Agentic AI (2725217), Zalando, https://jobs.zalando.com/en/jobs/2725217 | not shown | 2026-11-13 | A | Read | undated | Posting |
| S13 | Sr Applied Scientist (159035), Uber, https://www.uber.com/careers/list/159035/ | 2026-06-18 (via S15) | 2026-11-13 | A | Read | | Posting; office policy |
| S14 | Applied Scientist II (144960), Uber, https://www.uber.com/global/hi/careers/list/144960 | 2026-06-19 (via S15) | 2026-11-13 | A | Read | | Posting; pay |
| S15 | Uber AS listings, The Muse, https://www.themuse.com/jobs/uber/sr-applied-scientist-1e5bd4 | 2026-06-18 | 2026-11-13 | B | Extract | | Posting dates |
| S16 | Staff Applied Scientist, RL, Hippocratic AI, General Catalyst job board, https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/87905065-staff-applied-scientist-reinforcement-learning | 2026-07-29 | 2026-11-13 | B | Read | third-party board; Ashby link | Posting |
| S17 | Applied Scientist, Mistral AI, General Catalyst job board, https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/90169240-applied-scientist | 2026-08-17 | 2026-11-13 | B | Read | third-party board | Posting; proof |
| S18 | Applied Scientist II (Turing, Redmond), resumegeni mirror, https://resumegeni.com/jobs/applied-scientist-ii-at-microsoft-united-states-washington-redmond | 2026-10-16 | 2026-11-13 | C | Extract | mirror | Posting |
| S19 | Applied Scientist, Search and Recommendation (2719994), Zalando, https://jobs.zalando.com/en/jobs/2719994 | not shown | 2026-11-13 | A | Extract | | Posting |
| S20 | Applied Scientist, ZEOS (2722729), Zalando, https://jobs.zalando.com/en/jobs/2722729 | not shown | 2026-11-13 | A | Extract | | Posting |
| S21 | Applied Scientist II (2875053), Amazon, https://amazon.jobs/zh/jobs/2875053/applied-scientist-ii | not shown | 2026-11-13 | A | Extract | | Degree |
| S22 | Applied Scientist II, Multimodal IR/Search (3031254), Amazon, https://www.amazon.jobs/en/jobs/3031254/applied-scientist-ii-multimodal-information-retrieval-search-agi-level-5 | not shown | 2026-11-13 | A | Extract | | Degree |
| S23 | Applied Scientist, Marketing Measurement (153133), Uber, https://www.uber.com/global/ja/careers/list/153133/ | not shown | 2026-11-13 | A | Extract | | Posting |
| S24 | Sr Applied Scientist (Uber), Sway board, https://talent.swayvc.com/companies/uber/jobs/88623872-sr-applied-scientist | 2026-08-04 | 2026-11-13 | B | Extract | outside 90 days | Pay |
| S25 | Senior Applied Scientist (Outreach), startup.jobs, https://startup.jobs/senior-applied-scientist-outreach_io-7996499 | not shown | 2026-11-13 | B | Extract | | Pay |
| S26 | Applied Scientist (LLM) (Squad), Employbl, https://www.employbl.com/jobs/applied-scientist-llm-squad-1440230 | 2026-06-03 | 2026-11-13 | B | Extract | outside 90 days | Remote example |
| S27 | Applied Scientist II (2773192), Amazon, https://amazon.jobs/en/jobs/2773192/applied-scientist-ii-amzl-learning-product | not shown | 2026-11-13 | A | Extract | | Degree |
| S28 | Applied Scientist II (2919860), Amazon, https://amazon.jobs/en/jobs/2919860/applied-scientist-ii-sponsored-products | not shown | 2026-11-13 | A | Extract | | Degree |
| S29 | Applied Scientist II, AMZ9890756, resumegeni, https://resumegeni.com/jobs/applied-scientist-ii-amz9890756-at-amazon-us-ca-san-diego | not shown | 2026-11-13 | C | Extract | mirror | Requisition template |
| S30 | Amazon Applied Scientist Salaries, Levels.fyi, https://www.levels.fyi/en-gb/companies/amazon/salaries/applied-scientist | 2026-08-18 | 2026-11-13 | B | Extract | self-reported | Pay |
| S31 | Amazon Applied Scientist Salaries (earlier snapshot), Levels.fyi, https://next.levels.fyi/companies/amazon/salaries/applied-scientist | 2025-06-06 | 2026-11-13 | B | Extract | self-reported | Pay trend |
| S32 | Applied Scientist Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/applied-scientist | 2026-10-28 | 2026-11-13 | B | Extract | | Demand; stage mix |
| S33 | Applied Scientist roles, Fast AI Jobs, https://www.fastaijobs.com/roles/applied-scientist | roles dated 2026-03-03 to 2026-06-09 | 2026-11-13 | B | Extract | | Demand baseline |
| S34 | Applied Scientist Skills Companies Want in 2026, InterviewStack.io via DEV, https://dev.to/gnana_6392e836fd500a957dc/applied-scientist-skills-companies-want-in-2026-a-comprehensive-analysis-on-3146-active-postings-3odp | 2026-05-15 | 2026-11-13 | C | Read | conflict of interest (interview-prep vendor); category share from a later search snippet of the same page | Platform shares |
| S35 | Applied Scientist Salary in United States 2025, aijobs.net, https://aijobs.net/salaries/applied-scientist-salary-in-united-states-during-2025 | 2025 | 2026-11-13 | B | Extract | | Pay |
| S36 | Applied Scientist Jobs, ZipRecruiter, https://www.ziprecruiter.com/Jobs/Applied-Scientist/3 | 2026-06-07 | 2026-11-13 | C | Extract | | Pay |
| S37 | Amazon Applied Scientist II interview reviews, Glassdoor, https://www.glassdoor.ie/Interview/Amazon-Interview-E6036-RVW102987402.htm | 2026-02-27 to 2026-07-21 | 2026-11-13 | C | Extract | anecdotal | Loop |
| S38 | Amazon AI Research Scientist guide, Interview Query, https://www.interviewquery.com/guides/amazon-ai-research-scientist?exp_page=3 | not dated | 2026-11-13 | C | Extract | conflict of interest | Loop |
| S39 | Amazon Lab126 Applied Scientist guide, Dataford, https://dataford.io/interview-guides/amazon-lab126/applied-scientist | 2026 | 2026-11-13 | C | Extract | conflict of interest | Loop |
| S40 | Amazon cuts jobs in AGI team, Business Today, https://www.businesstoday.in/amp/technology/news/story/amazon-cuts-jobs-in-agi-team-after-laying-off-16000-employees-544682-2026-07-23 | 2026-07-23 | 2026-11-13 | B | Extract | | Durability |
| S41 | Amazon Cuts AGI Jobs While AI Spending Keeps Climbing, eWeek, https://www.eweek.com/de/news/amazon-agi-layoffs-ai-spending/ | 2026-07-24 | 2026-11-13 | B | Extract | | Durability |
| S42 | Amazon confirms 16,000 layoffs, ChannelWeb, https://www.channelweb.co.uk/news/2026/amazon-layoffs | 2026-01 | 2026-11-13 | B | Extract | conflicts with S43 | Durability |
| S43 | Amazon Layoffs: 5 Key Takeaways (summarising CRN), McGraw Hill, https://www.mheducation.com/highered/blog/2026/03/amazon-layoffs-5-key-takeaways | 2026-03 | 2026-11-13 | C | Extract | | Durability |
| S44 | Applied Scientist II H-1B report, MyVisaJobs, https://myvisajobs.com/reports/h1b/job-title/applied-scientist-ii | FY2024 | 2026-11-13 | B | Extract | page title says 2025 | LCA counts |
| S45 | H-1B record I-200-25350-485628, h1bdata.net, https://h1bdata.net/record/I-200-25350-485628 | 2025-12-16 | 2026-11-13 | B | Extract | | LCA wage |
| S46 | Applied Scientist III H-1B salary, visa-bulletin.us, https://visa-bulletin.us/h1b-salary/amazoncom-services-llc/applied-scientist-iii/ | through FY2025 | 2026-11-13 | B | Extract | | LCA wage |
| S47 | Applied Sciences H-1B salary (Microsoft), visa-bulletin.us, https://visa-bulletin.us/h1b-salary/microsoft-corporation/applied-sciences/ | through FY2026 | 2026-11-13 | B | Extract | | LCA wage |
| S48 | Amazon.com Services LLC H-1B sponsorship, careery.pro, https://careery.pro/h1b-sponsors/amazoncom-services-llc | FY2025 to FY2026 Q3 | 2026-11-13 | B | Extract | | LCA volume |
| S49 | Amazon Applied Scientist 2 Bangalore, LeetCode Compensation, https://leetcode.com/discuss/compensation/520551/amazon-applied-scientist-2-bangalore | 2020-02 | 2026-11-13 | D | Extract | stale | India pay |
| S50 | Amazon Scientist II salaries in India, AmbitionBox, https://ambitionbox.com/salaries/amazon-salaries/scientist-ii | 2022-04-30 | 2026-11-13 | C | Extract | stale; low confidence | India pay |
| S51 | Amazon Software Engineer salaries, Greater Bengaluru, Levels.fyi, https://www.levels.fyi/en-gb/companies/amazon/salaries/software-engineer/locations/greater-bengaluru | 2026-04-04 | 2026-11-13 | B | Extract | adjacent role | India proxy |
| S52 | Walmart Global Tech India postings, AnitaB.org board, https://jobs.anitab.org/companies/walmart/jobs/92045488-staff-data-scientist | 2026-09 to 2026-10 | 2026-11-13 | B | Extract | | Title evidence |
| S53 | Research jobs, The Rundown (Mistral titles), https://jobs.therundown.ai/jobs/research?page=5 | 2026 | 2026-11-13 | C | Extract | | Aliases |
| S54 | Mistral and Hippocratic AI job pages, JobsByCulture, https://jobsbyculture.com/jobs/mistral/ai-scientist-e9p5d | 2026 | 2026-11-13 | C | Extract | | Frontier-lab titles |
| S55 | Microsoft Data Scientist levels, Interview Kickstart, https://interviewkickstart.com/blogs/companies/microsoft-data-scientist-salary | not dated | 2026-11-13 | C | Extract | | Microsoft levels |
| S56 | Applied Research Scientist listings, DEjobs, https://nationalmssociety.dejobs.org/applied-research-scientist/jobs-in/usa/jobs/ | 2026 | 2026-11-13 | C | Extract | | Aliases |
| S57 | Data Scientist Jobs: 5,126 live roles (2026), JobsPipe, https://jobspipe.dev/jobs/data-scientist | 2026 (updated daily per page) | 2026-11-13 | B | Extract | adjacent roles; no AS page surfaced | Adjacent-role counts; JobsPipe absence |
| S58 | Ops Tech Applied Science, Amazon, https://www.amazon.jobs/en/landing_pages/ops-tech-applied-science | not dated | 2026-11-13 | A | Extract | | Definition |
| S59 | Career Leveling Comparison (example report), Levels.fyi, https://www.levels.fyi/reports/examples/leveling-comparison-report.html | 2024 | 2026-11-13 | B | Extract | example report | Level mapping |
| S60 | Applied Scientist at Series D+ AI startups and in San Francisco, Fast AI Jobs, https://www.fastaijobs.com/jobs/stage/series-d-plus/applied-scientist ; https://www.fastaijobs.com/jobs/role/applied-scientist/san-francisco | 2026-10-30; 2026-10-05 | 2026-11-13 | B | Extract | | Startup counts; alias titles |
| S61 | Applied AI Scientist job listings, JobsGlitch, https://jobsglitch.com/jobs/title/applied-ai-scientist | 2026 | 2026-11-13 | C | Extract | aggregator | Aliases; Amazon AS locations |
| S62 | Microsoft Applied Scientist II interview reviews, Glassdoor, https://www.glassdoor.com.au/Interview/Microsoft-Interview-E1651-RVW102606651.htm | 2026-01 to 2026-07 | 2026-11-13 | C | Extract | anecdotal | Microsoft loop |
| S63 | Microsoft Senior Applied Scientist (L63) Interview Experience, LeetCode Discuss, https://leetcode.com/discuss/post/7791470/microsoft-senior-applied-scientist-l63-i-jvy4/ | 2026-04-06 | 2026-11-13 | C | Extract | single report | Microsoft loop; L63 |
| S64 | Amazon Applied Scientist interview reviews (Bengaluru, Tokyo, London, intern), Glassdoor, https://www.glassdoor.com/Interview/Amazon-Interview-E6036-RVW92578453.htm | 2024-11 to 2026-07 | 2026-11-13 | C | Extract | anecdotal; one report stale | Amazon and India loops; difficulty rating |
| S65 | Amazon Applied Scientist Intern (6 Months) Interview, LeetCode Discuss, https://leetcode.com/discuss/post/8530116/amazon-applied-scientist-intern-6-months-hdbp/ | 2026-09-19 | 2026-11-13 | C | Extract | single report | Intern loop |
| S66 | Zalando Applied Scientist interview reviews, Glassdoor, https://www.glassdoor.fr/Entretien/Zalando-Entretien-E613421-RVW54448840.htm | 2025-10 to 2026-04 | 2026-11-13 | C | Extract | anecdotal | Zalando loop |
| S67 | Is it cheating? AI use during job interviews, GeekWire (reporting Business Insider), https://www.geekwire.com/2025/is-it-cheating-ai-use-during-job-interviews-sparks-debate-over-whether-to-restrict-emerging-tools/ | 2025-03 | 2026-11-13 | B | Extract | reporting on internal guidelines | Amazon AI-tool policy |
| S68 | Applied scientist interview at Amazon, Blind, https://www.teamblind.com/post/applied-scientist-interview-amazon-4udsobcp | not dated | 2026-11-13 | D | Extract | anecdote | Context only (not relied on) |
| S69 | Amazon SDE levels mapped to internal levels, DesignGurus, https://www.designgurus.io/blog/amazon-sde-levels | not dated | 2026-11-13 | C | Extract | vendor blog | Level mapping |

## Data Appendix

Records are grouped by type. Each line is one JSON object.

```jsonl
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "AS-titled postings at GCC or Indian-headquartered employers", "searched": ["Walmart Global Tech India postings on the AnitaB board (15 seen, all Data Scientist titles)", "combined queries for Flipkart, Intuit, Adobe, Oracle, Salesforce with Bengaluru or Hyderabad"], "note": "Amazon India and Microsoft IDC supply all six Indian postings in the sample"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Enterprise or consultancy AS postings", "searched": ["combined queries for Uber, Oracle, Salesforce, Adobe, Zillow, Booking.com; Walmart, Flipkart, Intuit"], "note": "Only Uber and Walmart results surfaced"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Posted pay bands in European postings", "searched": ["8 European postings in the sample"], "note": "None posted a band"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "AS-specific India pay from 2025 onwards", "searched": ["Levels.fyi Greater Bengaluru pages", "AmbitionBox", "LeetCode Compensation"], "note": "Only 2020-2022 items found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Microsoft Applied Scientist pay on Levels.fyi", "searched": ["Levels.fyi Microsoft Applied Scientist searches"], "note": "Levels.fyi maps Microsoft to Data Scientist; no AS-specific US figure surfaced"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "LinkedIn, Indeed and Glassdoor posting counts for Applied Scientist", "searched": ["search snippets for open-job counts"], "note": "Only ZipRecruiter pay snippets and non-comparable counts"}
{"type": "absence", "grade": "E", "src": ["S57"], "as_of": "2026-11-13", "item": "JobsPipe Applied Scientist posting count", "searched": ["JobsPipe role pages: Data Scientist (5,126 live roles) and AI Engineer (3,944) found", "two queries for an Applied Scientist page"], "note": "No Applied Scientist page surfaced; adjacent-role counts recorded instead"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Published analyses of prior roles of people hired as Applied Scientists", "searched": ["Amazon Science", "InterviewStack", "general search"], "note": "None found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "PhD share among hires", "searched": ["Amazon Science", "general search"], "note": "Only posting-level degree rules found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Interview loops for Uber, Hippocratic AI and Mistral AS roles", "searched": ["general search"], "note": "None retrieved; Amazon, Microsoft and Zalando loops found"}
{"type": "absence", "grade": "E", "src": ["S64", "S65"], "as_of": "2026-11-13", "item": "India-specific interview differences", "searched": ["Glassdoor Bengaluru reports", "LeetCode Discuss intern report"], "note": "Thin evidence; components match the US loop; one full-time report is stale (2024-11)"}
{"type": "absence", "grade": "E", "src": ["S67"], "as_of": "2026-11-13", "item": "Amazon interview AI-tool policy as an official page", "searched": ["amazon.jobs interview tips", "news search"], "note": "Only reporting on internal guidelines (B)"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Employer statements on certifications for the role", "searched": ["23 read postings"], "note": "No certification named"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "AS-titled postings at OpenAI, Anthropic, Cohere, Google DeepMind", "searched": ["one title-and-employer search"], "note": "They use Research Scientist or Member of Technical Staff; Mistral AI is the exception"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Hiring-manager proof-of-work statements dated 2025 onwards", "searched": ["Amazon Science", "employer pages"], "note": "Only posting wording; the named Amazon guidance is from 2022"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Amazon applied-science levels above L7", "searched": ["Levels.fyi pages"], "note": "Not seen"}
```

```jsonl
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science open roles, all categories", "unit": "postings", "value": 642, "method": "careers-site result count", "region": "global", "note": "607 full-time, 35 internships"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science Applied Science category", "unit": "postings", "value": 451, "method": "careers-site category filter", "region": "global", "note": "Upper bound on AS-titled roles; includes internships and managers"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science Data Science category", "unit": "postings", "value": 75, "method": "careers-site category filter", "region": "global"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science Research Science category", "unit": "postings", "value": 66, "method": "careers-site category filter", "region": "global"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science open roles in the US, all categories", "unit": "postings", "value": 465, "method": "careers-site country filter", "region": "US"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science open roles in India, all categories", "unit": "postings", "value": 90, "method": "careers-site country filter", "region": "IN"}
{"type": "measure", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Amazon Science open roles in Europe, all categories (UK 14, DE 7, LU 6, ES 5, RO 4, CH 2, IT 1, PL 1)", "unit": "postings", "value": 40, "method": "sum of country filters", "region": "EU+UK+CH"}
{"type": "measure", "grade": "M", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Estimated Amazon AS-titled open roles", "unit": "postings", "lo": 141, "hi": 375, "n": 10, "method": "451 times Wilson interval of 6 of 10 listed items carrying the title", "region": "global", "note": "Central estimate about 270; one page of 10 listings"}
{"type": "measure", "grade": "B", "src": ["S32"], "as_of": "2026-10-28", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Fast AI Jobs open AS roles at AI startups", "unit": "postings", "value": 23, "method": "platform count", "region": "global", "note": "15 companies"}
{"type": "measure", "grade": "B", "src": ["S32"], "as_of": "2026-10-28", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Share of Fast AI Jobs AS roles at Pre-Seed to Series B startups", "unit": "percent", "value": 39, "n": 23, "method": "platform stage tags", "region": "global", "note": "Series C 35%, B 17%, A 13%, E 13%, D 9%, Seed 9%, F 4%"}
{"type": "measure", "grade": "B", "src": ["S60"], "as_of": "2026-10-05", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Fast AI Jobs AS roles in San Francisco and the Bay Area", "unit": "postings", "value": 8, "method": "platform location page", "region": "US", "note": "6 startups"}
{"type": "measure", "grade": "B", "src": ["S60"], "as_of": "2026-10-30", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Fast AI Jobs AS roles at Series D and later startups", "unit": "postings", "value": 7, "method": "platform stage page", "region": "global", "note": "3 companies"}
{"type": "measure", "grade": "B", "src": ["S33"], "as_of": "2026-06-09", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Fast AI Jobs AS roles snapshot at AI startups", "unit": "postings", "value": 14, "method": "count of listed roles", "region": "global", "note": "12 companies; newest role dated 2026-06-09"}
{"type": "measure", "grade": "M", "src": ["S32", "S33"], "as_of": "2026-10-28", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Change in Fast AI Jobs AS roles between the two readings", "unit": "percent", "value": 64, "method": "23 against 14", "region": "global", "note": "Companies 15 against 12 (+25%)"}
{"type": "measure", "grade": "B", "src": ["S57"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:data-scientist", "measure": "JobsPipe live Data Scientist roles (adjacent role)", "unit": "postings", "value": 5126, "method": "platform page count", "region": "global", "note": "No Applied Scientist page surfaced"}
{"type": "measure", "grade": "B", "src": ["S57"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:ai-engineer", "measure": "JobsPipe live AI Engineer roles (adjacent role)", "unit": "postings", "value": 3944, "method": "platform page count", "region": "global"}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V1", "subject": "role:applied-scientist", "measure": "InterviewStack active Applied Scientist postings (all-keyword)", "unit": "postings", "value": 3146, "method": "vendor job board count", "region": "global", "note": "US 1916 (60.9%); India 123 (3.9%); Singapore 188; UK 163; Canada 150; Germany 63"}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Share of all-keyword postings in healthcare, education, biotech or pharma", "unit": "percent", "value": 38, "n": 3146, "method": "vendor classification", "region": "global"}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Share of all-keyword postings that are remote", "unit": "percent", "value": 9.9, "n": 3146, "method": "vendor work-mode tags", "region": "global", "note": "Hybrid 19.4%; on-site 77.1%"}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Seniority mix of all-keyword postings (entry 14.2, mid 60.6, senior 16.1, staff or lead 9.1)", "unit": "percent", "value": 14.2, "n": 3146, "method": "title-keyword tagging", "region": "global", "note": "Value is the entry share"}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Share of all-keyword postings in the Statistics and Experimentation skill category", "unit": "percent", "value": 44.6, "n": 3146, "method": "vendor skill-category tagging", "region": "global", "note": "Category-level figure from a search snippet of the same analysis"}
{"type": "measure", "grade": "A", "src": ["S10", "S11", "S12", "S19", "S20"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Distinct Zalando AS-titled postings surfaced by one search", "unit": "postings", "value": 14, "method": "count of distinct job IDs", "region": "DE", "note": "Lower bound"}
{"type": "measure", "grade": "C", "src": ["S64"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Glassdoor interview difficulty rating for Amazon Applied Scientist (5 is hardest)", "unit": "rating out of 5", "value": 3.3, "method": "platform rating", "region": "global", "note": "77% of reports positive; undated page"}
{"type": "measure", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Share of sample from Big Tech (Amazon, Microsoft, Uber)", "unit": "percent", "value": 72.7, "n": 33, "method": "jd-sample count", "region": "global"}
{"type": "measure", "grade": "M", "src": ["S3", "S7", "S14"], "as_of": "2026-11-13", "ttl": "V1", "subject": "role:applied-scientist", "measure": "Share of sample postings that post a pay range", "unit": "percent", "value": 21.2, "n": 33, "method": "jd-sample count (7 of 33)", "region": "global", "note": "All in USD; none of 6 Indian or 8 European postings"}
{"type": "measure", "grade": "M", "src": ["S3", "S7", "S11"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Share of postings with a stated degree rule that require a PhD alone", "unit": "percent", "value": 5.3, "n": 19, "method": "jd-sample count (1 of 19)", "region": "global", "note": "The one case has an equivalent-experience clause"}
{"type": "measure", "grade": "M", "src": ["S3", "S5", "S6"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Share of read postings naming any certification", "unit": "percent", "value": 0, "n": 23, "method": "jd-sample count", "region": "global"}
{"type": "measure", "grade": "M", "src": ["S10", "S11", "S12", "S16"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Share of read postings whose primary layer is application and deployment", "unit": "percent", "value": 73.9, "n": 23, "method": "author judgement", "region": "global"}
{"type": "measure", "grade": "M", "src": ["S8", "S10", "S16", "S17"], "as_of": "2026-11-13", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Share of read postings naming fine-tuning or post-training (specialisation share)", "unit": "percent", "value": 26.1, "n": 23, "method": "jd-sample count (6 of 23)", "region": "global", "note": "Interval 13-46%"}
{"type": "measure", "grade": "M", "src": ["S30", "S31"], "as_of": "2026-08-18", "ttl": "V3", "subject": "role:applied-scientist", "measure": "Change in Levels.fyi Amazon AS US median total compensation, 2025-06-06 to 2026-08-18", "unit": "percent", "value": 19.8, "method": "335000 against 279722", "region": "US", "note": "Level averages rose 1.7-5.2%; mix shift likely"}
{"type": "measure", "grade": "B", "src": ["S44"], "as_of": "2024-09-30", "ttl": "V4", "subject": "role:applied-scientist", "measure": "Amazon.com Services AS II certified LCAs, FY2024", "unit": "filings", "value": 312, "method": "aggregated DOL disclosure data", "region": "US", "note": "Applications, not workers; Amazon Development Center adds 44"}
```

```jsonl
{"type": "pay", "grade": "A", "src": ["S3"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "United States (lowest to highest geographic market)", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Amazon posting 2906278", "lo": 136000, "hi": 223400, "level": "AS II", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "A", "src": ["S4"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "United States (lowest to highest geographic market)", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Amazon posting 2773329", "lo": 136000, "hi": 222200, "level": "AS II", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "A", "src": ["S2"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "Seattle, WA", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Amazon requisition 10601059", "lo": 163617, "hi": 193200, "level": "AS II", "employer_type": "big-tech", "n": 1, "note": "Offered-position style requisition"}
{"type": "pay", "grade": "A", "src": ["S7"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "United States (typical)", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Microsoft posting 200034701", "lo": 102100, "hi": 202200, "level": "IC3 (AS II)", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "A", "src": ["S7"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "SF Bay Area and New York City", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Microsoft posting 200034701", "lo": 133800, "hi": 219200, "level": "IC3 (AS II)", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "A", "src": ["S14"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "New York, NY", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Uber posting 144960", "lo": 161000, "hi": 179000, "level": "AS II", "employer_type": "big-tech", "n": 1}
{"type": "pay", "grade": "B", "src": ["S24"], "as_of": "2026-08-04", "ttl": "V3", "role": "applied-scientist", "location": "San Francisco, CA and New York, NY", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Uber Sr AS via Sway board", "lo": 190000, "hi": 211000, "level": "Senior", "employer_type": "big-tech", "n": 1, "note": "Plus equity; third-party copy"}
{"type": "pay", "grade": "B", "src": ["S25"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "United States (city not shown)", "stat": "range", "currency": "USD", "period": "year", "basis": "base", "source_name": "Outreach Sr AS via startup.jobs", "lo": 140000, "hi": 175000, "level": "Senior", "employer_type": "ai-startup", "n": 1}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-08-18", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 245000, "level": "L4", "employer_type": "big-tech", "note": "Amazon; base 164K, stock 48.6K, bonus 33.1K"}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-08-18", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 324000, "level": "L5", "employer_type": "big-tech", "note": "Amazon; base 171K, stock 118K, bonus 36K; aligns with Google L4 on Levels.fyi's level comparison"}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-08-18", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 407000, "level": "L6", "employer_type": "big-tech", "note": "Amazon; base 167K, stock 211K, bonus 28.9K; aligns with Google L5 and Meta E5"}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-08-18", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 653000, "level": "L7", "employer_type": "big-tech", "note": "Amazon; base 173K, stock 258K, bonus 223K"}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-08-18", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 335000, "employer_type": "big-tech", "note": "Amazon, all levels; FAQ block on the same page says 306000"}
{"type": "pay", "grade": "B", "src": ["S30"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "location": "New York City area", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 353000, "level": "L5", "employer_type": "big-tech", "note": "Amazon; L4 260000; update date not shown"}
{"type": "pay", "grade": "B", "src": ["S31"], "as_of": "2025-06-06", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "tc", "source_name": "Levels.fyi earlier snapshot", "value": 308000, "level": "L5", "employer_type": "big-tech", "note": "Amazon; L4 241000, L6 396000, median 279722"}
{"type": "pay", "grade": "B", "src": ["S35"], "as_of": "2025-12-31", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "aijobs.net", "value": 199250, "n": 282, "note": "Basis not stated; aggregator figure"}
{"type": "pay", "grade": "C", "src": ["S36"], "as_of": "2026-06-07", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "mean", "currency": "USD", "period": "year", "basis": "base", "source_name": "ZipRecruiter", "value": 173084, "note": "Basis not stated"}
{"type": "pay", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "InterviewStack", "value": 110000, "n": 878, "note": "All-keyword mix including lab and pharma postings"}
{"type": "pay", "grade": "B", "src": ["S44"], "as_of": "2024-09-30", "ttl": "V4", "role": "applied-scientist", "location": "United States", "stat": "offer", "currency": "USD", "period": "year", "basis": "base", "source_name": "LCA via MyVisaJobs", "value": 171690, "level": "AS II", "employer_type": "big-tech", "n": 312, "note": "Amazon.com Services mean offered wage; filings are not pay; Amazon Development Center n=44 mean 175339"}
{"type": "pay", "grade": "B", "src": ["S45"], "as_of": "2025-12-16", "ttl": "V4", "role": "applied-scientist", "location": "Santa Clara, CA", "stat": "offer", "currency": "USD", "period": "year", "basis": "base", "source_name": "LCA record I-200-25350-485628", "value": 171600, "level": "AS II", "employer_type": "big-tech", "n": 1, "note": "Prevailing wage 164403 (level II); filing, not pay"}
{"type": "pay", "grade": "B", "src": ["S47"], "as_of": "2026-11-13", "ttl": "V4", "role": "applied-scientist", "location": "United States", "stat": "p50", "currency": "USD", "period": "year", "basis": "base", "source_name": "LCA via visa-bulletin.us", "value": 247285, "employer_type": "big-tech", "n": 12, "note": "Microsoft Applied Sciences titles; range 132440-276123; filings, not pay"}
{"type": "pay", "grade": "D", "src": ["S49"], "as_of": "2020-02-01", "ttl": "V3", "role": "applied-scientist", "location": "Bengaluru, India", "stat": "offer", "currency": "INR", "period": "year", "basis": "base", "source_name": "LeetCode Compensation", "value": 2800000, "level": "AS II", "employer_type": "big-tech", "n": 1, "note": "Stale; signing bonus INR 1.2M in each of years 1 and 2; total about INR 4.3M"}
{"type": "pay", "grade": "C", "src": ["S50"], "as_of": "2022-04-30", "ttl": "V3", "role": "applied-scientist", "location": "India", "stat": "range", "currency": "INR", "period": "year", "basis": "tc", "source_name": "AmbitionBox", "lo": 4500000, "hi": 7000000, "level": "Scientist II", "employer_type": "big-tech", "n": 4, "note": "Stale; low confidence; basis not stated"}
{"type": "pay", "grade": "B", "src": ["S51"], "as_of": "2026-04-04", "ttl": "V3", "role": "applied-scientist", "location": "Greater Bengaluru, India", "stat": "p50", "currency": "INR", "period": "year", "basis": "tc", "source_name": "Levels.fyi", "value": 6030000, "employer_type": "big-tech", "note": "Amazon software engineers; adjacent-role proxy, not AS"}
```

```jsonl
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "ml_fundamentals", "n": 23, "source_kind": "jd-sample", "share": 0.957, "count": 22, "tier_hint": "Must", "note": "Full-text n=16: 0.938"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "python", "n": 23, "source_kind": "jd-sample", "share": 0.609, "count": 14, "tier_hint": "Must", "note": "Full-text n=16: 0.875"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "statistics", "n": 23, "source_kind": "jd-sample", "share": 0.348, "count": 8, "tier_hint": "Important", "note": "Full-text n=16: 0.438; Must for measurement and search variants"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "pytorch", "n": 23, "source_kind": "jd-sample", "share": 0.304, "count": 7, "tier_hint": "Important", "note": "Full-text n=16: 0.438; Must for LLM post-training variant"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "experiment_design", "n": 23, "source_kind": "jd-sample", "share": 0.348, "count": 8, "tier_hint": "Important", "note": "Full-text n=16: 0.375"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S37", "S62", "S66"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "dsa", "n": 23, "source_kind": "jd-sample", "share": 0.13, "count": 3, "tier_hint": "Must", "note": "Full-text n=16: 0.188; Must for interviews (coding rounds reported at Amazon, Microsoft, Zalando in 2026), Should in postings"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "sql", "n": 23, "source_kind": "jd-sample", "share": 0.174, "count": 4, "tier_hint": "Should", "note": "Full-text n=16: 0.25"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "data_analysis", "n": 23, "source_kind": "jd-sample", "share": 0.087, "count": 2, "tier_hint": "Should", "note": "Full-text n=16: 0.125"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "communication", "n": 23, "source_kind": "jd-sample", "share": 0.435, "count": 10, "tier_hint": "Important", "note": "Full-text n=16: 0.438"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "llm_apis", "n": 23, "source_kind": "jd-sample", "share": 0.304, "count": 7, "tier_hint": "Important", "note": "Proxy: RAG, agents, prompting; full-text n=16: 0.313"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "generative_ai", "n": 23, "source_kind": "jd-sample", "share": 0.696, "count": 16, "tier_hint": "Important", "note": "Full-text n=16: 0.688; sample skewed to GenAI themes"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "research_to_prod", "n": 23, "source_kind": "jd-sample", "share": 0.783, "count": 18, "tier_hint": "Must", "note": "Full-text n=16: 0.75"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "eval_stats", "n": 23, "source_kind": "jd-sample", "share": 0, "count": 0, "tier_hint": "Should", "note": "No explicit confidence-interval or power wording; see new:llm_evaluation"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "finetuning", "n": 23, "source_kind": "jd-sample", "share": 0.261, "count": 6, "tier_hint": "Important", "note": "Full-text n=16: 0.313"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "causal", "n": 23, "source_kind": "jd-sample", "share": 0.13, "count": 3, "tier_hint": "Should", "note": "Full-text n=16: 0.063; Must for measurement variants"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "research_methods", "n": 23, "source_kind": "jd-sample", "share": 0.565, "count": 13, "tier_hint": "Important", "note": "Research or novel-algorithm wording; full-text n=16: 0.625"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "deep_learning", "n": 23, "source_kind": "jd-sample", "share": 0.348, "count": 8, "tier_hint": "Important", "note": "Full-text n=16: 0.438"}
{"type": "skill_signal", "grade": "M", "src": ["S16"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "ablations", "n": 23, "source_kind": "jd-sample", "share": 0.043, "count": 1, "tier_hint": "Optional", "note": "Hippocratic AI only"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "c4_responsible_ai", "n": 23, "source_kind": "jd-sample", "share": 0.087, "count": 2, "tier_hint": "Should", "note": "Safety or reliability wording; Uber and Hippocratic AI"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:publications_patents", "n": 23, "source_kind": "jd-sample", "share": 0.478, "count": 11, "tier_hint": "Important", "note": "Basic qualification at Amazon; full-text n=16: 0.438"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:llm_evaluation", "n": 23, "source_kind": "jd-sample", "share": 0.435, "count": 10, "tier_hint": "Important", "note": "Metrics, verifiers, LLM-as-judge; full-text n=16: 0.438"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:software_engineering", "n": 23, "source_kind": "jd-sample", "share": 0.304, "count": 7, "tier_hint": "Important", "note": "Full-text n=16: 0.313"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:nlp_ir_recsys", "n": 23, "source_kind": "jd-sample", "share": 0.478, "count": 11, "tier_hint": "Should", "note": "Domain tag; full-text n=16: 0.5"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:java_cpp", "n": 23, "source_kind": "jd-sample", "share": 0.261, "count": 6, "tier_hint": "Optional", "note": "Amazon template accepts Python alone; full-text n=16: 0.375"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:mentoring_leadership", "n": 23, "source_kind": "jd-sample", "share": 0.391, "count": 9, "tier_hint": "Should", "note": "Rises with seniority; full-text n=16: 0.25"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:big_data_spark", "n": 23, "source_kind": "jd-sample", "share": 0.174, "count": 4, "tier_hint": "Should", "note": "Full-text n=16: 0.25"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:cloud_aws", "n": 23, "source_kind": "jd-sample", "share": 0.174, "count": 4, "tier_hint": "Should", "note": "Full-text n=16: 0.125"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:rl", "n": 23, "source_kind": "jd-sample", "share": 0.217, "count": 5, "tier_hint": "Should", "note": "Must for post-training variant; full-text n=16: 0.188"}
{"type": "skill_signal", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "ttl": "V3", "role": "applied-scientist", "skill": "new:cv_robotics", "n": 23, "source_kind": "jd-sample", "share": 0.087, "count": 2, "tier_hint": "Optional", "note": "Domain tag"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "experiment_design", "n": 3146, "source_kind": "platform", "share": 0.263, "tier_hint": null, "note": "A/B testing; all-keyword set; the Statistics and Experimentation category is 0.446"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "python", "n": 3146, "source_kind": "platform", "share": 0.254, "tier_hint": null, "note": "All-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "statistics", "n": 3146, "source_kind": "platform", "share": 0.246, "tier_hint": null, "note": "All-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "ml_fundamentals", "n": 3146, "source_kind": "platform", "share": 0.153, "tier_hint": null, "note": "Machine learning; all-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "sql", "n": 3146, "source_kind": "platform", "share": 0.057, "tier_hint": null, "note": "All-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "deep_learning", "n": 3146, "source_kind": "platform", "share": 0.056, "tier_hint": null, "note": "All-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "pytorch", "n": 3146, "source_kind": "platform", "share": 0.054, "tier_hint": null, "note": "All-keyword set"}
{"type": "skill_signal", "grade": "C", "src": ["S34"], "as_of": "2026-05-15", "ttl": "V3", "role": "applied-scientist", "skill": "generative_ai", "n": 3146, "source_kind": "platform", "share": 0.036, "tier_hint": null, "note": "LLMs alone 0.045; all-keyword set"}
```

```jsonl
{"type": "loop", "grade": "C", "src": ["S37", "S38", "S64", "S67"], "as_of": "2026-07-21", "ttl": "V3", "employer": "Amazon", "track": "classic-ml-system-design", "stages": ["recruiter screen", "technical phone screen of about 60 minutes: science breadth or depth plus one easy coding problem", "virtual onsite of 4-6 rounds: ML breadth, ML depth, coding, team-specific system design (one 2026-07 report adds agentic product thinking), Bar Raiser round on Leadership Principles", "PhD candidates: research talk with Q&A"], "formats": ["easy-to-medium LeetCode-style coding and ML coding such as computing AUC", "STAR behavioural stories against Leadership Principles"], "ai_policy": "Candidates must not use GenAI tools unless explicitly permitted and may be disqualified (reported from internal guidelines, 2025-02)", "take_home": null, "duration": "21 days average in one Glassdoor report", "note": "About 6 anecdotal 2026 reports; system design is one round among about five; employer-wide policy owned by another session"}
{"type": "loop", "grade": "C", "src": ["S64", "S65"], "as_of": "2026-04-17", "ttl": "V3", "employer": "Amazon India (Bengaluru)", "track": "classic-ml-system-design", "stages": ["HackerRank assessment (intern loop)", "further interviews on research depth and on coding (intern loop, 2026)", "full-time reports: phone screen, coding, ML design or depth rounds, Leadership Principles rounds"], "formats": ["transformer fundamentals and research depth questions", "practical, non-LeetCode implementation questions in one 2024-11 report (stale)"], "ai_policy": null, "take_home": "HackerRank assessment for interns", "duration": null, "note": "Few Bengaluru reports; components match the US loop"}
{"type": "loop", "grade": "C", "src": ["S39"], "as_of": "2026-11-13", "ttl": "V3", "employer": "Amazon Lab126", "track": "classic-ml-system-design", "stages": ["recruiter screen", "technical phone interviews", "onsite loop", "research presentation"], "formats": ["research presentation defended to a panel"], "ai_policy": null, "take_home": null, "duration": "3-5 weeks", "note": "Vendor guide with a conflict of interest"}
{"type": "loop", "grade": "C", "src": ["S62", "S63"], "as_of": "2026-07-30", "ttl": "V3", "employer": "Microsoft", "track": "classic-ml-system-design", "stages": ["screen of 30-60 minutes: resume deep dive plus coding or ML case questions", "loop of 3-4 rounds of about 45-60 minutes: ML fundamentals plus ML coding, DSA coding, data analysis on some teams, ML case or system design (planned in some loops, absent in one 2026-04 report), behavioural or hiring-manager round"], "formats": ["live coding in most rounds, including K-means from scratch and self-attention", "HackerRank used in one reported round", "SQL and pandas questions on some teams"], "ai_policy": null, "take_home": null, "duration": null, "note": "About 8 Glassdoor reports from 2026-01 to 2026-07 and one LeetCode Discuss report of a Senior Applied Scientist (L63) loop dated 2026-04-06 that ended in an offer; recruiter prep material differed from the rounds held"}
{"type": "loop", "grade": "C", "src": ["S66"], "as_of": "2025-10-17", "ttl": "V3", "employer": "Zalando", "track": "classic-ml-system-design", "stages": ["30-minute HR screening", "hiring-manager round", "one-hour technical interview", "four final rounds: science depth, science breadth with coding, scope (product-focused), collaboration"], "formats": ["coding inside the breadth round"], "ai_policy": null, "take_home": null, "duration": null, "note": "About 3 Berlin reports from 2025-10 to 2026-04; one reports five rounds and a mismatch between stated requirements and what was tested; older reports not used"}
```

```jsonl
{"type": "practice", "grade": "P", "src": ["S7", "S8", "S13", "S3"], "as_of": "2026-11-13", "ttl": "V3", "area": "resume", "tactic": "Write each project line as: method or model, system served, offline metric, online experiment result, business metric moved", "claim": "Microsoft, Uber and Amazon postings ask for offline and online experimentation and for shipped features that moved business metrics", "evidence": "Microsoft Bing Places and Hyderabad, Uber Amsterdam and Amazon AGI postings name online A/B testing or experimentation; pattern only, no outcomes invented", "verdict": "use", "risk": "Reads as boilerplate if the numbers are not your own"}
{"type": "practice", "grade": "P", "src": ["S3", "S4", "S10", "S7"], "as_of": "2026-11-13", "ttl": "V3", "area": "resume", "tactic": "Keep publications and patents listed, paired with a shipped system", "claim": "Publications or patents appear in 11 of 23 read postings and are a basic qualification in several Amazon postings", "evidence": "Amazon 2773329, 2757258, 2720385; Zalando 2719998; Microsoft 200034701 preferred", "verdict": "use", "risk": "A publication-only profile lacks the customer-impact evidence Amazon's guidance describes"}
{"type": "practice", "grade": "P", "src": ["S10", "S16", "S17"], "as_of": "2026-11-13", "ttl": "V3", "area": "resume", "tactic": "Choose one variant headline: product ML, measurement and causal science, or LLM post-training", "claim": "Postings differ sharply by variant in tools and evidence asked for", "evidence": "Uber AS II names no ML; Hippocratic AI asks for RL post-training; Zalando Agentic AI asks for agent orchestration", "verdict": "use", "risk": "A mixed headline can match none of the variants"}
{"type": "practice", "grade": "P", "src": ["S17"], "as_of": "2026-08-17", "ttl": "V3", "area": "portfolio", "tactic": "For AI-native and frontier-class roles show large-codebase contributions with tests and CI", "claim": "Mistral's posting asks for a record in a large codebase and for tests and CI practice", "evidence": "One posting only", "verdict": "use-with-care", "risk": "Single-source; other AI-native employers may weigh it differently"}
{"type": "practice", "grade": "P", "src": ["S37", "S38", "S64"], "as_of": "2026-07-21", "ttl": "V3", "area": "interview-prep", "tactic": "Prepare ML breadth and depth, easy-to-medium coding plus ML coding, system design with agentic cases, and Leadership Principles stories", "claim": "Amazon loops in 2026 reports combine these components", "evidence": "About 6 Glassdoor reports and 2 vendor guides", "verdict": "use-with-care", "risk": "Anecdotal; loops vary by team"}
{"type": "practice", "grade": "P", "src": ["S62", "S63"], "as_of": "2026-07-30", "ttl": "V3", "area": "interview-prep", "tactic": "For Microsoft practise ML coding from scratch (K-means, self-attention) alongside LeetCode-medium problems and ML fundamentals", "claim": "Microsoft AS loops reported in 2026 put coding in almost every round", "evidence": "One Senior AS (L63) report and about 8 Glassdoor reports", "verdict": "use-with-care", "risk": "Recruiter material differed from the rounds held in one report; team variation"}
{"type": "practice", "grade": "P", "src": ["S2"], "as_of": "2022-01-26", "ttl": "V3", "area": "interview-prep", "tactic": "Prepare Learn and Be Curious, Dive Deep and Invent and Simplify stories", "claim": "Amazon's science guidance names these three principles as standing out for scientists", "evidence": "One Bar Raiser's 2022 article, stale", "verdict": "use-with-care", "risk": "Four years old; principles and loops may have shifted"}
{"type": "practice", "grade": "P", "src": ["S67"], "as_of": "2025-03-01", "ttl": "V3", "area": "interview-prep", "tactic": "Do not use GenAI tools during Amazon interviews unless the recruiter says they are allowed", "claim": "Amazon reportedly treats unauthorised GenAI use as grounds for disqualification", "evidence": "Reporting on internal guidelines (Business Insider via GeekWire)", "verdict": "use", "risk": "Policy may change; confirm with the recruiter"}
{"type": "practice", "grade": "P", "src": ["S2", "S16"], "as_of": "2026-11-13", "ttl": "V3", "area": "resume", "tactic": "State 'state of the art' only with named baselines and an evaluation design", "claim": "Employers stress rigorous evaluation and customer impact over benchmark claims", "evidence": "Amazon guidance on customer-impact success; Hippocratic AI asks for rigorously evaluated gains", "verdict": "avoid", "risk": "Unbaselined claims invite probing in depth rounds"}
{"type": "practice", "grade": "P", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V3", "area": "job-search", "tactic": "Search employer boards and Amazon Science category and country filters instead of keyword aggregators", "claim": "The all-keyword market includes 38% healthcare, education and pharma postings", "evidence": "InterviewStack analysis and Amazon's filter counts", "verdict": "use", "risk": "Legacy Amazon requisition IDs may be stale"}
{"type": "practice", "grade": "P", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V3", "area": "portfolio", "tactic": "Complete at least three code reviews through open-source pull requests", "claim": "K13 recommends this", "evidence": "No source found for the number", "verdict": "untested", "risk": "Count is arbitrary", "note": "(source reference approximate)"}
```

```jsonl
{"type": "company", "grade": "A", "src": ["S1"], "as_of": "2026-11-13", "ttl": "V2", "name": "Amazon", "employer_type": "big-tech", "hq": "Seattle, WA", "regions": ["US", "IN", "DE", "LU", "UK", "ES"], "genai_open": true, "ats": "in-house (amazon.jobs)", "board_url": "https://www.amazon.science/careers", "sponsorship": "LCA volume: 312 AS II filings FY2024", "remote_policy": "mostly on-site", "india_presence": "90 science roles listed", "note": "451 Applied Science roles on 2026-11-13"}
{"type": "company", "grade": "A", "src": ["S7", "S8"], "as_of": "2026-11-13", "ttl": "V2", "name": "Microsoft", "employer_type": "big-tech", "hq": "Redmond, WA", "regions": ["US", "IN", "CN", "UK"], "genai_open": true, "ats": "in-house (microsoft.ai site)", "board_url": "https://microsoft.ai/", "sponsorship": null, "remote_policy": "Microsoft AI office at least 4 days a week from 2026-01-26", "india_presence": "Hyderabad and Bengaluru AS II postings", "note": "AS II at IC3; Senior AS at L63"}
{"type": "company", "grade": "A", "src": ["S13", "S14"], "as_of": "2026-11-13", "ttl": "V2", "name": "Uber", "employer_type": "big-tech", "hq": "San Francisco, CA", "regions": ["US", "NL"], "genai_open": true, "ats": "in-house (uber.com careers)", "board_url": "https://www.uber.com/careers", "sponsorship": null, "remote_policy": "at least 50% in office", "india_presence": null, "note": "AS roles sit in the Data Science family"}
{"type": "company", "grade": "A", "src": ["S10", "S11", "S12"], "as_of": "2026-11-13", "ttl": "V2", "name": "Zalando", "employer_type": "enterprise", "hq": "Berlin", "regions": ["DE"], "genai_open": true, "ats": "in-house (jobs.zalando.com)", "board_url": "https://jobs.zalando.com/en/what-we-do/applied-science-and-research", "sponsorship": "relocation assistance stated", "remote_policy": "hybrid, 60% or more remote per week, varies by team", "india_presence": null, "note": "Job category Applied Science & Research; at least 14 AS postings"}
{"type": "company", "grade": "B", "src": ["S16"], "as_of": "2026-07-29", "ttl": "V2", "name": "Hippocratic AI", "employer_type": "ai-startup", "hq": "Palo Alto, CA", "regions": ["US"], "genai_open": true, "ats": "Ashby", "board_url": "https://jobs.generalcatalyst.com/companies/hippocractic-ai", "sponsorship": null, "remote_policy": "in office five days a week", "india_presence": null, "note": "AS roles are LLM post-training"}
{"type": "company", "grade": "B", "src": ["S17"], "as_of": "2026-08-17", "ttl": "V2", "name": "Mistral AI", "employer_type": "frontier-lab", "hq": "US", "regions": ["US", "FR", "UK", "SG", "CH", "PL"], "genai_open": true, "ats": "Ashby", "board_url": "https://jobs.generalcatalyst.com/companies/mistral-ai-2", "sponsorship": null, "remote_policy": "not remote per aggregator", "india_presence": null, "note": "Customer-facing Applied Scientist and Research Engineer roles"}
{"type": "company", "grade": "B", "src": ["S25"], "as_of": "2026-11-13", "ttl": "V2", "name": "Outreach", "employer_type": "ai-startup", "hq": "US", "regions": ["US"], "genai_open": true, "ats": null, "board_url": null, "sponsorship": null, "remote_policy": null, "india_presence": null, "note": "Sales-engagement software company; Sr AS posting with pay band"}
{"type": "company", "grade": "B", "src": ["S26"], "as_of": "2026-06-03", "ttl": "V2", "name": "Squad", "employer_type": "ai-startup", "hq": "US", "regions": ["UA"], "genai_open": true, "ats": "Greenhouse", "board_url": null, "sponsorship": null, "remote_policy": "remote within Ukraine only", "india_presence": null, "note": "Applied Scientist (LLM)"}
```

```jsonl
{"type": "jd", "grade": "A", "src": ["S3"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, AGI Intelligent Decisions", "url": "https://amazon.jobs/en/jobs/2906278/applied-scientist-ii-agi-intelligent-decisions", "job_id": "2906278", "seen": "2026-11-13", "location": "US (city not shown)", "remote": null, "seniority": "mid (AS II)", "years": "2 with Master's; 0 with PhD", "degree": "PhD, or Master's + 2y", "must": ["PhD or Master's + 2y in CS or ML field", "Java, C++ or Python", "2y building business models", "2y deploying ML or DL in production", "ML fundamentals; LLM, NLP or IR focus"], "nice": ["5y spoken-language systems", "familiarity with state-of-the-art ML", "solid software development", "written and spoken communication"], "pay": {"lo": 136000, "hi": 223400, "currency": "USD", "period": "year"}, "ats": "Amazon in-house", "note": "type=big-tech; basis=full text; date not shown; live at retrieval"}
{"type": "jd", "grade": "A", "src": ["S4"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, Generative AI Innovation Center", "url": "https://amazon.jobs/en/jobs/2773329/applied-scientist-ii-generative-ai-innovation-center", "job_id": "2773329", "seen": "2026-11-13", "location": "US (city not shown)", "remote": null, "seniority": "mid (AS II)", "years": "4 with Master's", "degree": "PhD, or Master's + 4y", "must": ["PhD or Master's + 4y", "publications or patents at top venues", "Java, C++ or Python", "one of algorithms and data structures, optimisation, data mining, HPC", "neural deep learning and ML"], "nice": ["professional software development", "PhD in a quantitative field", "DL frameworks (MXNet, TensorFlow, PyTorch)", "communicating rigorous maths to non-experts"], "pay": {"lo": 136000, "hi": 222200, "currency": "USD", "period": "year"}, "ats": "Amazon in-house", "note": "type=big-tech; basis=full text; customer-facing AWS team"}
{"type": "jd", "grade": "A", "src": ["S5"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, 5365 - CMT Systems", "url": "https://amazon.jobs/en/jobs/2757258/applied-scientist-ii-5365-cmt-systems", "job_id": "2757258", "seen": "2026-11-13", "location": "Bengaluru, India", "remote": null, "seniority": "mid (AS II)", "years": "4 with Master's; 3 building models", "degree": "PhD, or Master's + 4y", "must": ["3y building business models", "PhD or Master's + 4y", "publications or patents at top venues", "Java, C++ or Python", "one of algorithms and data structures, optimisation, data mining"], "nice": ["Unix or Linux", "professional software development"], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=full text; pricing, NLP, LLM work"}
{"type": "jd", "grade": "A", "src": ["S6"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist, Amazon (International Machine Learning)", "url": "https://amazon.jobs/en/jobs/2720385/applied-scientist-amazon", "job_id": "2720385", "seen": "2026-11-13", "location": "Bengaluru, India", "remote": null, "seniority": "mid (unlevelled; 5y building models)", "years": "4 with Master's; 5 building models", "degree": "PhD, or Master's + 4y", "must": ["5y building business models", "PhD or Master's + 4y", "publications or patents", "Java, C++ or Python", "one of algorithms and data structures, optimisation"], "nice": ["large tech organisation", "PhD in CS or EE with ML specialisation"], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=full text"}
{"type": "jd", "grade": "A", "src": ["S7"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Microsoft", "title": "Applied Scientist II (Bing Places)", "url": "https://microsoft.ai/job/applied-scientist-ii-bing-places-5/", "job_id": "200034701", "seen": "2026-11-13", "location": "Redmond, WA", "remote": null, "seniority": "mid (IC3)", "years": "2 with Bachelor's; 1 with Master's", "degree": "Bachelor's + 2y, or Master's + 1y, or doctorate", "must": ["degree in stats, econometrics, CS or EE with 2y, 1y or none by level of degree"], "nice": ["Master's or PhD", "4y applying LLMs or AI (RAG, ranking, classification)", "Python with PyTorch, TensorFlow or JAX", "offline metrics and online A/B testing", "search or IR background", "publications or patents", "distributed training, production ML infrastructure"], "pay": {"lo": 102100, "hi": 202200, "currency": "USD", "period": "year"}, "ats": "Microsoft in-house", "note": "type=big-tech; basis=full text; Bay Area and NYC band 133800-219200"}
{"type": "jd", "grade": "A", "src": ["S8"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Microsoft", "title": "Applied Scientist II (search query understanding)", "url": "https://microsoft.ai/job/applied-scientist-ii-9/", "job_id": "200034207", "seen": "2026-11-13", "location": "Hyderabad, India", "remote": "no (office at least 4 days a week from 2026-01-26)", "seniority": "mid (AS II)", "years": "2 with Bachelor's; 1 with Master's", "degree": "Bachelor's + 2y, or Master's + 1y, or doctorate", "must": ["production NLP or LLM work (prompting, fine-tuning, RAG)", "statistical modelling and experiment design", "SQL and large-scale data tools (Spark, Databricks, Kusto)"], "nice": ["query understanding or recommenders", "multimodal or advanced RAG", "record of shipping ML features that moved KPIs", "communicating to senior stakeholders"], "pay": null, "ats": "Microsoft in-house", "note": "type=big-tech; basis=full text; no language named"}
{"type": "jd", "grade": "A", "src": ["S9"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Microsoft", "title": "Applied Scientist II (NLP grounding for AI search)", "url": "https://microsoft.ai/job/applied-scientist-ii/", "job_id": "200009039", "seen": "2026-11-13", "location": "Bengaluru, India", "remote": null, "seniority": "mid (AS II)", "years": "3-6", "degree": "Master's or PhD", "must": ["Master's or PhD in CS or EE with NLP, ML or data mining", "3-6y applying deep learning or ML", "communication and collaboration"], "nice": ["research or development depth in ML and NLP", "delivering advanced NLP projects", "record of shipping products"], "pay": null, "ats": "Microsoft in-house", "note": "type=big-tech; basis=full text"}
{"type": "jd", "grade": "A", "src": ["S10"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Zalando", "title": "Applied Scientist - Search/NLP/IR", "url": "https://jobs.zalando.com/en/jobs/2719998", "job_id": "2719998", "seen": "2026-11-13", "location": "Berlin, Germany", "remote": null, "seniority": "mid by title; principal-level content", "years": "4", "degree": "PhD in NLP, IR or ML, or equivalent experience", "must": ["PhD or equivalent + 4y industry", "leads multi-area scientific roadmap", "authority in deep learning; top-venue publications", "Python with PyTorch or TensorFlow; LLMs in IR", "AWS or equivalent cloud"], "nice": [], "pay": null, "ats": "Zalando in-house", "note": "type=enterprise; basis=full text"}
{"type": "jd", "grade": "A", "src": ["S11"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Zalando", "title": "Applied Scientist (Process Intelligence)", "url": "https://jobs.zalando.com/en/jobs/2717524", "job_id": "2717524", "seen": "2026-11-13", "location": "Berlin, Germany", "remote": "hybrid, 60% or more remote per week, varies by team", "seniority": "mid (unlevelled)", "years": "2", "degree": "Master's or PhD in a quantitative field", "must": ["Master's or PhD + 2y", "ML and statistics", "Python (numpy, pandas, scikit-learn)", "production deployment (AWS, Kubernetes, CI/CD, REST)", "Spark or Databricks and relational databases"], "nice": [], "pay": null, "ats": "Zalando in-house", "note": "type=enterprise; basis=full text; relocation assistance stated"}
{"type": "jd", "grade": "A", "src": ["S12"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Zalando", "title": "Senior Applied Scientist - Agentic AI", "url": "https://jobs.zalando.com/en/jobs/2725217", "job_id": "2725217", "seen": "2026-11-13", "location": "Berlin, Germany", "remote": null, "seniority": "senior", "years": null, "degree": null, "must": ["record of shipping production LLM and agentic systems", "ML, DL and NLP depth", "agent orchestration, RAG, hallucination mitigation", "Python (PyTorch, PydanticAI), SQL, Databricks", "strategic communication"], "nice": [], "pay": null, "ats": "Zalando in-house", "note": "type=enterprise; basis=full text; no degree or years stated"}
{"type": "jd", "grade": "A", "src": ["S13", "S15"], "as_of": "2026-06-18", "ttl": "V1", "role": "applied-scientist", "employer": "Uber", "title": "Sr Applied Scientist", "url": "https://www.uber.com/careers/list/159035/", "job_id": "159035", "seen": "2026-11-13", "location": "Amsterdam, Netherlands", "remote": "hybrid, at least 50% in office", "seniority": "senior", "years": "2 with PhD or Master's; 4 with Bachelor's", "degree": "PhD, MS or BS", "must": ["quantitative degree with 2y or 4y applied ML", "ML and statistics foundation", "production ML systems", "Python and large datasets", "experimentation, evaluation, data analysis"], "nice": ["LLMs: RAG, prompt design, evaluation", "fine-tuning, LoRA, adapters", "RL or feedback-driven optimisation", "Spark, Hive, Presto", "reliability or safety of AI systems", "fraud, risk or security domain"], "pay": null, "ats": "Uber in-house", "note": "type=big-tech; basis=full text; posted 2026-06-18 per The Muse; live at retrieval"}
{"type": "jd", "grade": "A", "src": ["S14", "S15"], "as_of": "2026-06-19", "ttl": "V1", "role": "applied-scientist", "employer": "Uber", "title": "Applied Scientist II (Brand Science, marketing measurement)", "url": "https://www.uber.com/global/hi/careers/list/144960", "job_id": "144960", "seen": "2026-11-13", "location": "New York, NY", "remote": "hybrid, at least 50% in office", "seniority": "mid (AS II)", "years": "2 with Master's; 3 with Bachelor's", "degree": "PhD, MS or BS", "must": ["quantitative degree with experience by level", "advanced SQL, Python and BI tools", "in-depth experimental design"], "nice": ["marketing or AdTech problems", "PhD in stats, economics or OR"], "pay": {"lo": 161000, "hi": 179000, "currency": "USD", "period": "year"}, "ats": "Uber in-house", "note": "type=big-tech; basis=full text; names no ML; posted 2026-06-19 per The Muse"}
{"type": "jd", "grade": "B", "src": ["S16"], "as_of": "2026-07-29", "ttl": "V1", "role": "applied-scientist", "employer": "Hippocratic AI", "title": "Staff Applied Scientist, Reinforcement Learning", "url": "https://jobs.generalcatalyst.com/companies/hippocractic-ai/jobs/87905065-staff-applied-scientist-reinforcement-learning", "job_id": "87905065", "seen": "2026-11-13", "location": "Menlo Park, CA", "remote": "no (office five days a week)", "seniority": "staff", "years": "5", "degree": "Master's in CS or ML", "must": ["Master's in CS, ML or related", "5y in NLP, LLM training or RL", "2y RL for LLM post-training", "Python and PyTorch for large-scale training", "RLHF, RLVR or LLM-as-judge experience", "training or fine-tuning at 50B+ parameters"], "nice": ["top-venue publications", "healthcare or regulated domain", "FSDP, DeepSpeed, vLLM", "safety alignment, interpretability"], "pay": null, "ats": "Ashby (via General Catalyst job board)", "note": "type=ai-startup; basis=full text; 107 days before retrieval but listed with Apply link"}
{"type": "jd", "grade": "A", "src": ["S1"], "as_of": "2026-10-23", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist (Kindle Direct Publishing science, Bengaluru)", "url": "https://www.amazon.jobs/jobs/10593286/applied-scientist", "job_id": "10593286", "seen": "2026-11-13", "location": "Bengaluru, India", "remote": null, "seniority": "mid (unlevelled)", "years": null, "degree": null, "must": ["description only: agentic LLM systems, multimodal models, post-training with SFT and RL", "offline and online experiments", "production deployment", "clear readouts with recommendations"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; posted 2026-10-23; twin requisition 10593555 excluded as duplicate"}
{"type": "jd", "grade": "A", "src": ["S1"], "as_of": "2026-10-23", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Senior Applied Scientist (Audible)", "url": "https://www.amazon.jobs/jobs/10588542/senior-applied-scientist", "job_id": "10588542", "seen": "2026-11-13", "location": "Berlin, Germany", "remote": null, "seniority": "senior", "years": null, "degree": null, "must": ["description only: ML, GenAI, NLP, RL", "end-to-end production solutions and critical-path code", "author peer-reviewed publications", "mentor scientists"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; posted 2026-10-23"}
{"type": "jd", "grade": "A", "src": ["S1"], "as_of": "2026-10-25", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Principal Applied Scientist, FAIM (Full Funnel Agentic Intelligence and Models)", "url": "https://www.amazon.jobs/jobs/10591721/principal-applied-scientist-faim-full-funnel-agentic-intelligence-and-models", "job_id": "10591721", "seen": "2026-11-13", "location": "New York, NY", "remote": null, "seniority": "principal", "years": null, "degree": null, "must": ["description only: agentic AI for advertising, evaluation of an ads agent", "incrementality measurement and long-term sales modelling", "large-scale experiments", "productionise ML and optimisation; mentor; publish"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; posted 2026-10-25"}
{"type": "jd", "grade": "A", "src": ["S1"], "as_of": "2026-10-23", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Sr. Applied Scientist - CV, Vulcan Stow", "url": "https://www.amazon.jobs/jobs/10589082/sr-applied-scientist--cv-vulcan-stow", "job_id": "10589082", "seen": "2026-11-13", "location": "Seattle, WA", "remote": null, "seniority": "senior", "years": null, "degree": null, "must": ["description only: 3D perception, transformers, deep learning", "deploy production models with edge inference on SageMaker", "mentoring and communication"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; posted 2026-10-23"}
{"type": "jd", "grade": "A", "src": ["S2"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II (AMZ1513176, multiple positions)", "url": "https://www.amazon.jobs/jobs/10601059/applied-scientist-ii-amz", "job_id": "10601059", "seen": "2026-11-13", "location": "Seattle, WA", "remote": null, "seniority": "mid (AS II)", "years": "1 with Master's; 5 with Bachelor's", "degree": "Master's + 1y, or Bachelor's + 5y", "must": ["Master's + 1y, or Bachelor's + 5y", "1y programming in Java, C++ or Python", "1y supervised and unsupervised ML modelling for moderately complex projects"], "nice": [], "pay": {"lo": 163617, "hi": 193200, "currency": "USD", "period": "year"}, "ats": "Amazon in-house", "note": "type=big-tech; basis=minimum requirements plus description; offered-position style; seen in the Amazon Science feed, listed after 10599924 (posted 2026-10-26)"}
{"type": "jd", "grade": "A", "src": ["S2"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist I, Tablet Product Software", "url": "https://www.amazon.jobs/jobs/10601943/applied-scientist-i-tablet-product-software", "job_id": "10601943", "seen": "2026-11-13", "location": "Seattle, WA", "remote": null, "seniority": "entry (AS I)", "years": null, "degree": null, "must": ["description only: recommendation models deployed to production", "mentor engineers in ML and generative AI"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; seen in the Amazon Science feed"}
{"type": "jd", "grade": "A", "src": ["S2"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, Detail Page", "url": "https://www.amazon.jobs/jobs/10602090/applied-scientist-ii-detail-page", "job_id": "10602090", "seen": "2026-11-13", "location": "Bengaluru, India", "remote": null, "seniority": "mid (AS II)", "years": null, "degree": null, "must": ["description only: econometric, ML and big-data methods for detail-page optimisation", "statistical modelling and simulation", "present results to executives"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; seen in the Amazon Science feed"}
{"type": "jd", "grade": "A", "src": ["S2"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Sr. Applied Scientist, APM Video Science", "url": "https://www.amazon.jobs/jobs/10599900/sr-applied-scientist-apm-video-science-", "job_id": "10599900", "seen": "2026-11-13", "location": "New York, NY", "remote": null, "seniority": "senior", "years": null, "degree": null, "must": ["description only: LLMs, VLMs and computer vision for Twitch creator tools", "research prototype to production", "evaluate first-party and third-party solutions", "mentor through code reviews; external publications"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=description only; seen in the Amazon Science feed"}
{"type": "jd", "grade": "C", "src": ["S18"], "as_of": "2026-10-16", "ttl": "V1", "role": "applied-scientist", "employer": "Microsoft", "title": "Applied Scientist II (Turing team)", "url": "https://resumegeni.com/jobs/applied-scientist-ii-at-microsoft-united-states-washington-redmond", "job_id": null, "seen": "2026-11-13", "location": "Redmond, WA", "remote": "hybrid, at least 3 days in office", "seniority": "mid (AS II)", "years": "2", "degree": null, "must": ["2y industrial coding in C++, C#, C, Java or Python", "2y deep learning in end-to-end AI products (search, recommendation, NLP, document understanding)", "2y PyTorch or TensorFlow"], "nice": [], "pay": null, "ats": "Eightfold (per mirror)", "note": "type=big-tech; basis=requirements list read in a third-party mirror's search snippet; employer page not opened"}
{"type": "jd", "grade": "B", "src": ["S17"], "as_of": "2026-08-17", "ttl": "V1", "role": "applied-scientist", "employer": "Mistral AI", "title": "Applied Scientist", "url": "https://jobs.generalcatalyst.com/companies/mistral-ai-2/jobs/90169240-applied-scientist", "job_id": "90169240", "seen": "2026-11-13", "location": "Palo Alto, CA and New York, NY", "remote": "no (per aggregator)", "seniority": "mid (unlevelled)", "years": null, "degree": "not required; PhD or master's is a plus", "must": ["strong communication to technical and non-technical audiences", "expert PyTorch or JAX", "clean fault-tolerant Python in large codebases", "track record from personal, professional or academic projects"], "nice": ["PhD or master's", "large-codebase contributions", "publications", "tests and CI practice"], "pay": null, "ats": "Ashby (via General Catalyst job board)", "note": "type=frontier-lab; basis=full text; pre/post-training on large GPU clusters and client research projects"}
{"type": "jd", "grade": "B", "src": ["S19"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Zalando", "title": "Applied Scientist - Search and Recommendation", "url": "https://jobs.zalando.com/en/jobs/2719994", "job_id": "2719994", "seen": "2026-11-13", "location": "Germany (city not shown in snippet)", "remote": null, "seniority": "mid (unlevelled)", "years": null, "degree": null, "must": ["ML and AI solutions built with AWS, Python and TensorFlow", "hypotheses and A/B tests", "deployment"], "nice": [], "pay": null, "ats": "Zalando in-house", "note": "type=enterprise; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S20"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Zalando", "title": "Applied Scientist - ZEOS Data Science and Algorithms", "url": "https://jobs.zalando.com/en/jobs/2722729", "job_id": "2722729", "seen": "2026-11-13", "location": "Germany (city not shown in snippet)", "remote": null, "seniority": "mid (unlevelled)", "years": "3", "degree": null, "must": ["3y as applied, data or research scientist", "time-series forecasting methods"], "nice": [], "pay": null, "ats": "Zalando in-house", "note": "type=enterprise; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S21"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II (multimodal learning, LLM, speech)", "url": "https://amazon.jobs/zh/jobs/2875053/applied-scientist-ii", "job_id": "2875053", "seen": "2026-11-13", "location": "US (Amazon Development Center U.S., Inc.)", "remote": null, "seniority": "mid (AS II)", "years": "4 with Master's; 3 building models", "degree": "PhD, or Master's + 4y", "must": ["PhD or Master's + 4y", "3y building business models"], "nice": ["domain knowledge in multimodal, speech or NLP", "statistics, ML and DL fundamentals"], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S22"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II - Multimodal Information Retrieval/Search, AGI (Level 5)", "url": "https://www.amazon.jobs/en/jobs/3031254/applied-scientist-ii-multimodal-information-retrieval-search-agi-level-5", "job_id": "3031254", "seen": "2026-11-13", "location": "not shown", "remote": null, "seniority": "mid (AS II, L5)", "years": "4 with Master's; 1 building models", "degree": "PhD, or Master's + 4y", "must": ["1y building business models", "PhD or Master's + 4y", "Java, C++ or Python"], "nice": ["PhD with IR, recommender or multimodal specialty", "hands-on visual LLMs"], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S23"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Uber", "title": "Applied Scientist, Marketing Measurement", "url": "https://www.uber.com/global/ja/careers/list/153133/", "job_id": "153133", "seen": "2026-11-13", "location": "New York, NY and San Francisco, CA", "remote": null, "seniority": "mid (unlevelled)", "years": "2", "degree": "Bachelor's, Master's or PhD, or equivalent applied experience", "must": ["2y statistical and causal inference methods in applied settings"], "nice": [], "pay": null, "ats": "Uber in-house", "note": "type=big-tech; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S24"], "as_of": "2026-08-04", "ttl": "V1", "role": "applied-scientist", "employer": "Uber", "title": "Sr Applied Scientist", "url": "https://talent.swayvc.com/companies/uber/jobs/88623872-sr-applied-scientist", "job_id": "88623872", "seen": "2026-11-13", "location": "San Francisco, CA and New York, NY", "remote": null, "seniority": "senior", "years": "4", "degree": null, "must": ["4y as ML scientist, research scientist or applied scientist"], "nice": [], "pay": {"lo": 190000, "hi": 211000, "currency": "USD", "period": "year"}, "ats": null, "note": "type=big-tech; basis=snippet; 101 days before retrieval, outside the window, kept for its pay band"}
{"type": "jd", "grade": "B", "src": ["S25"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Outreach", "title": "Senior Applied Scientist", "url": "https://startup.jobs/senior-applied-scientist-outreach_io-7996499", "job_id": "7996499", "seen": "2026-11-13", "location": "not shown", "remote": null, "seniority": "senior", "years": "2", "degree": null, "must": ["2y implementing ML and NLP systems incl. LLM architectures, classification, entity recognition, dialogue, agentic workflows"], "nice": [], "pay": {"lo": 140000, "hi": 175000, "currency": "USD", "period": "year"}, "ats": null, "note": "type=ai-startup; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S26"], "as_of": "2026-06-03", "ttl": "V1", "role": "applied-scientist", "employer": "Squad", "title": "Applied Scientist (LLM)", "url": "https://www.employbl.com/jobs/applied-scientist-llm-squad-1440230", "job_id": "1440230", "seen": "2026-11-13", "location": "Kyiv and Lviv, Ukraine", "remote": "remote within Ukraine only", "seniority": "mid (unlevelled)", "years": "3", "degree": null, "must": ["3y commercial ML with NLP or LLM focus"], "nice": [], "pay": null, "ats": "Greenhouse", "note": "type=ai-startup; basis=snippet; listing updated 2026-06-03, window unverified"}
{"type": "jd", "grade": "B", "src": ["S27"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, AMZL Learning Product", "url": "https://amazon.jobs/en/jobs/2773192/applied-scientist-ii-amzl-learning-product", "job_id": "2773192", "seen": "2026-11-13", "location": "US (Amazon.com Services LLC)", "remote": null, "seniority": "mid (AS II)", "years": "4 with Master's", "degree": "PhD, or Master's + 4y", "must": ["PhD or Master's + 4y", "publications or patents at top venues", "Java, C++ or Python"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=snippet; window unverified"}
{"type": "jd", "grade": "B", "src": ["S28"], "as_of": "2026-11-13", "ttl": "V1", "role": "applied-scientist", "employer": "Amazon", "title": "Applied Scientist II, Sponsored Products", "url": "https://amazon.jobs/en/jobs/2919860/applied-scientist-ii-sponsored-products", "job_id": "2919860", "seen": "2026-11-13", "location": "not shown", "remote": null, "seniority": "mid (AS II)", "years": "4 with Master's", "degree": "PhD, or Master's + 4y", "must": ["PhD or Master's + 4y"], "nice": [], "pay": null, "ats": "Amazon in-house", "note": "type=big-tech; basis=snippet; window unverified"}
```

```jsonl
{"type": "repo_delta", "grade": "B", "src": ["S34", "S14", "S16", "S17"], "as_of": "2026-11-13", "k": "K1", "verdict": "updated", "finding": "The title also covers AI-native post-training work, customer-facing research engineering and Uber's measurement science; the all-keyword market has 38% non-tech postings", "suggested": "Add variant notes to the role page"}
{"type": "repo_delta", "grade": "C", "src": ["S53", "S56", "S60", "S61"], "as_of": "2026-11-13", "k": "K2", "verdict": "updated", "finding": "Aliases seen: level-suffixed titles, Applied Scientist / Research Engineer, AI Scientist, Associate Applied Scientist, Data & Applied Scientist, Applied Research Scientist; Applied Scientist (GenAI) not seen as a title", "suggested": "Replace the alias list"}
{"type": "repo_delta", "grade": "B", "src": ["S1", "S32", "S33", "S57", "S60"], "as_of": "2026-11-13", "k": "K3", "verdict": "updated", "finding": "Fast AI Jobs 23 roles at 15 startups on 2026-10-28; Amazon 451 Applied Science roles on 2026-11-13; the ~700 figure remains untraced; JobsPipe has no AS page", "suggested": "Cite counts; no re-score without rubric thresholds"}
{"type": "repo_delta", "grade": "B", "src": ["S30", "S3", "S7", "S14", "S59", "S69"], "as_of": "2026-11-13", "k": "K4", "verdict": "updated", "finding": "AS-specific pay is available as of 2026-11-13: Amazon L5 $324K, L6 $407K; posted base bands; proxies fit only senior level once levels are mapped", "suggested": "Replace proxy with Levels.fyi Amazon AS and posted bands"}
{"type": "repo_delta", "grade": "B", "src": ["S1", "S34"], "as_of": "2026-11-13", "k": "K5", "verdict": "updated", "finding": "Amazon lists 90 India science roles; 6 Indian postings read; India is 3.9% of the all-keyword set", "suggested": "Add India counts"}
{"type": "repo_delta", "grade": "D", "src": ["S49", "S50", "S51"], "as_of": "2026-11-13", "k": "K6", "verdict": "unverifiable", "finding": "Only stale AS self-reports (2020-2022) and an adjacent Amazon software-engineer figure were found", "suggested": "Keep as low-confidence"}
{"type": "repo_delta", "grade": "C", "src": ["S1", "S40", "S41", "S42", "S43"], "as_of": "2026-11-13", "k": "K7", "verdict": "updated", "finding": "451 open roles against three rounds of Amazon cuts; attribution to AI disputed", "suggested": "Describe durability as employer-cycle risk"}
{"type": "repo_delta", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "k": "K8", "verdict": "updated", "finding": "Application and deployment is primary in 74%; post-training primary in 4% and named in 26%", "suggested": "Narrow the L4 footprint to AI-native and post-training variants"}
{"type": "repo_delta", "grade": "C", "src": ["S37", "S38", "S39", "S62", "S63", "S64", "S66"], "as_of": "2026-11-13", "k": "K9", "verdict": "updated", "finding": "System design is one of about five components at Amazon, sometimes absent at Microsoft; coding appears in almost every Microsoft round; Zalando tests depth, breadth with coding, scope and collaboration", "suggested": "Describe the track as a mix of ML depth, coding and behavioural rounds"}
{"type": "repo_delta", "grade": "M", "src": ["S3", "S18", "S34"], "as_of": "2026-11-13", "k": "K10", "verdict": "updated", "finding": "Shares consistent within interval (platform category Statistics and Experimentation 44.6%); statistics, PyTorch and experiment design are Important overall and Must by variant", "suggested": "Tier by variant"}
{"type": "repo_delta", "grade": "M", "src": ["S3", "S18"], "as_of": "2026-11-13", "k": "K11", "verdict": "updated", "finding": "SQL 25%, LLM/GenAI 69%, ablations 4%, production deployment 75%", "suggested": "Move research_to_prod to Must; ablations to Optional"}
{"type": "repo_delta", "grade": "M", "src": ["S3", "S4", "S21", "S22", "S27", "S28"], "as_of": "2026-11-13", "k": "K12", "verdict": "updated", "finding": "PhD is the only no-experience route at Amazon; 1 of 19 postings requires a PhD alone", "suggested": "Reword as an Amazon-specific corridor"}
{"type": "repo_delta", "grade": "C", "src": ["S17", "S2"], "as_of": "2026-11-13", "k": "K13", "verdict": "unverifiable", "finding": "Tests and CI supported by one posting; the OSS review count and eval-statistics write-up have no source", "suggested": "Mark the count as untested"}
{"type": "repo_delta", "grade": "C", "src": ["S2", "S3", "S4", "S10"], "as_of": "2026-11-13", "k": "K14", "verdict": "updated", "finding": "Publications are named qualifications at Amazon and Zalando; pair them with shipped systems", "suggested": "Reframe rather than omit"}
```
