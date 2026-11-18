---
id: "T0-68"
title: "Learning Resources for GenAI Roles, Rated: Documentation, Courses, Books, Cohorts and Bootcamps"
date: "2026-11-13"
status: complete-with-gaps
topic: "learning-resources-rated"
tags: ["learning-resources", "courses", "bootcamps", "gpu-compute", "outcome-evidence", "india", "rating-rubric"]
informs_decisions: ["D-008", "D-005"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai with web search. Anthropic's own resources (Claude Academy, Anthropic documentation) and material by a researcher who joined Anthropic in 2026 are in scope; Anthropic is this model's developer, so those rows are marked COI."
evidence_window: "2018-03 to 2026-11"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 17
---

# T0-68: Learning Resources for GenAI Roles, Rated: Documentation, Courses, Books, Cohorts and Bootcamps

S-numbers (S1–S98) refer to rows in the Sources & Evidence Ledger. Grades follow the protocol: A is a primary source opened in full; B is an established secondary source, or a primary page seen only as a search extract (the protocol caps those at B); C is an attributed third-party or vendor claim; D is recalled or judgement; E is unverifiable; M is my own calculation; P is practice-curated. The brief anchors on 2026-11-11 and retrieval took place on 2026-11-13; sources dated up to 2026-11-11 are included. Only two pages were opened in full (S26, S44), so no row in this report exceeds B. Calculated rubric scores are M and inherit the weakest grade among their inputs.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | No GenAI-specific course or bootcamp has independent, audited outcome data; every figure is vendor-reported. | 85% | D |
| P2 | DeepLearning.AI short courses are free, including certificates. | 60% | D |
| P3 | Hugging Face courses are free and are the strongest free route into LLM and agent work. | 80% | D |
| P4 | Colab and Kaggle free tiers cover months 1–6 of application work, with Kaggle giving about 30 GPU hours a week. | 70% | D |
| P5 | Lambda H100 rents for about US$2.99–3.29 per hour and a RunPod RTX 4090 for about US$0.34–0.69 per hour. | 65% | D |
| P6 | Stanford CS336 is the best free LLM-systems course and Karpathy's Zero to Hero the best free introduction. | 75% | D |

## Research Question

**Decision question.** Which learning resources (documentation, free courses, lectures, books, paid cohorts, bootcamps) best build the skills of each GenAI role family, how should they be rated when almost none has independent outcome data, and which are poor value? The answer informs D-008, D-005, `career/03-skills-and-tech/learning-roadmaps.md` and `data/tools.json`.

**Sub-questions.**
1. What rubric, with weights, rates resources without outcome data?
2. What are the strongest 5–10 resources per role family?
3. What independent outcome evidence, regulator action or consumer-court record exists, including in India?
4. What do the main paid programmes cost, claim and refund?
5. Which popular resources are stale, and what replaced them?
6. What do free compute tiers, credit programmes and GPU rental cost?
7. What is the minimal free and paid set per family?
8. Do K1–K17 hold?

**Scope as applied.**
- The 12 role families are used as named in the brief. The knowledge base's Must/Important skill lists were not supplied, so role fit is scored against the brief's family descriptions.
- Certifications are excluded. They appear only as a property of a course (for example, whether a certificate is proctored).
- Degrees and executive programmes appear as price context only.
- Fast-moving topics use resources updated since 2024-01-01. Foundations use any date, with the edition stated.
- WIDEN to non-English resources was not achieved beyond incidental Japanese and Chinese pages (a gap, listed under Absences).

**Method.** 68 web searches and 2 full page fetches; two further fetch attempts were refused by the tool because the URLs had not yet appeared in search results, so the pages were reached through search extracts instead. Query groups covered regulator actions, ISA bootcamps, platform mergers and acquisitions, each K-tool, GPU price trackers, free LLM API tiers, Indian consumer-court and advertising-standards records, paid-programme pages and refund terms, and the primary pages of candidate free resources. Rated sample: 52 resource records and 88 resource-by-family rows (scored, or marked not scored).

**Falsification searches.**
- Independent or audited outcomes, which found the CIRR audit standard (partly contradicts K1).
- RAGAS dormancy, where an undated Snyk snapshot reports "healthy" against later 2026 analyses showing no release since 2026-01-13.
- RunPod and Lambda price pages, which contradicted the stored figures (K16, K17).
- DeepLearning.AI pricing, where sources conflict between US$15, US$25–30 and a draft US$30 per month or US$270 per year.
- NVIDIA DLI catalogue age, where 2019–2021 catalogues were replaced by October 2026 data.
- AI SDK release dates, where one secondary source (2026-05-04) contradicted other secondary sources dating AI SDK 6 to 2025-12-22, and the Vercel AI SDK 7 launch post (2026-06-25) contradicted the stored "AI SDK 6" framing (K5).
- Maven refund terms, where an older "14 days after the course ends" rule conflicts with the present "through week 2" refund policy.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | No independent outcome study of any GenAI-specific course or bootcamp was found. The only audit standard is CIRR, which had three publishing schools as of early 2026 (general software bootcamps). Codesmith's audited 2023 software cohort predates its AI/ML syllabus. | [S56] [S57] [S58] | C |
| KF2 | The only regulator action found on bootcamp outcome claims is CFPB v BloomTech (2024-04-17). It found ISAs were loans marketed as non-loans and hiring claims were false. California records BloomTech's last day of instruction as 2025-12-31. | [S1] [S2] [S3] [S5] | B |
| KF3 | The strongest free resources are primary or university material: Stanford CS336 (Spring 2026, five implementation-heavy assignments), Hugging Face courses, DataTalks.Club zoomcamps, GPU MODE lectures, ARENA, Inspect docs, OWASP GenAI Top 10 2026, NIST AI RMF and BlueDot courses. | [S22] [S33] [S59] [S61] [S62] [S64] [S65] [S90] | B |
| KF4 | The rubric (authority 20, currency 20, hands-on 20, role fit 25, cost 15, plus gates) puts free resources at 75–97 in every family where a free route exists. No paid programme reached "use": Maven AI Evals scores 75–80 and shows Maven's refund-policy badge, but its refund window (end of week 2 of a six-week course whose first week is listed as two days) was not confirmed as at least 14 days from the first session, and no other programme passed the refund and outcome-claim gates. | Section 1 | M |
| KF5 | DeepLearning.AI course videos are free. Labs, quizzes and certificates need Pro (US$25 per month billed annually, US$30 monthly). The Hugging Face Agents certificate is free. Certificates are unproctored completion records. | [S22] [S28] [S29] | B |
| KF6 | Paid price points: Maven AI Evals US$4,200 for the 2026-10-10 cohort, announced as the last of 2026 (about US$3,000 in 2025); Scaler ₹3,99,000; upGrad/IIIT-B ₹1,25,000–2,25,000; Great Learning ₹2.1–3.35 lakh plus GST (12-month track) or US$3,950 (23-week track); Simplilearn US$2,499–4,800 or ₹1.7–2.85 lakh (listings conflict); Codesmith US$22,500; Interview Kickstart not published. | [S49] [S52] [S53] [S55] [S57] [S84] [S85] [S87] [S98] | C |
| KF7 | Refund terms differ sharply. Maven gives a full refund through week 2 of courses of four weeks or more that carry its refund-policy badge. Scaler states 14 days from the first class. upGrad refunds before programme start. Simplilearn deducts an administration charge, and its Wharton-distributed programmes accept refund requests only within 7 days of purchase. Interview Kickstart gives a conditional 50% on some tracks and none on listed Indian tracks. NVIDIA DLI purchases are non-refundable. | [S30] [S49] [S52] [S53] [S84] [S86] [S97] | B |
| KF8 | In India no order against a GenAI or IT bootcamp was found. Adjacent records exist: CCPA coaching-sector penalties, consumer-commission refund orders (EduBridge, FIITJEE), 2018 ASCI findings that included Great Lakes advertising, and self-reported refund complaints about Great Learning on a complaints-handling site (13 complaints, 5 resolved; the site sells complaint-resolution services). | [S44] [S45] [S46] [S47] [S88] | B |
| KF9 | Staleness is concentrated in agent tooling and regulation. The OpenAI Assistants API retired on 2026-08-26. LangChain 1.0 and LangGraph 1.0 (2025-10-22) deprecated the old agent helpers. AI SDK 6 (2025-12-22) was superseded by AI SDK 7 on 2026-06-25 (one secondary source gave 2026-05-04 for AI SDK 6 and is contradicted [S19]). The OWASP LLM Top 10 2026 edition replaced earlier editions. The EU Digital Omnibus on AI (in force 2026-07-27) moved high-risk deadlines to 2027-12-02 and 2028-08-02. | [S17] [S64] [S69] [S70] [S80] [S89] | B |
| KF10 | Free GPU notebooks are narrower than the stored assumption. Colab Pro for Education and SageMaker Studio Lab are closed to new users. Kaggle's weekly quota is not in its docs. ZeroGPU gives a free account 5 minutes a day. Modal's US$30 monthly credit buys about 7.6 H100-hours. | [S26] [S37] | B |
| KF11 | Free LLM API tiers exist (Groq, OpenRouter, Google AI Studio, Cerebras) but limits are per-model or per-project and volatile, and flagship models were reported as paid-only from April 2026. "API credits cover months 1–6" therefore depends on the model needed. | [S83] | C |
| KF12 | GPU rental prices rose in 2026. Lambda H100 SXM went from US$2.99–3.29 in older cached snapshots (date not shown) to US$3.99–4.29 per GPU-hour, and a tracker shows US$4.59 in early November. RunPod repriced Secure Cloud twice in September–October 2026 (RTX 4090 US$0.89). The cheapest in-stock consumer GPU was US$0.29–0.41 per hour. | [S26] [S39] [S41] [S42] [S43] | B |
| KF13 | Governance, leadership, human-data and fractional families have no independently rated curriculum. Their best items are primary documents and BlueDot. Vendor-awarded "Certified AI Consultant / Fractional CAIO" titles have no independent assessment. Pre-July 2026 EU AI Act guides are stale. | [S62] [S63] [S73] [S74] [S89] | C |
| KF14 | Chip Huyen's *AI Engineering* (O'Reilly, 1st edition, 2025-01-07) is the strongest conceptual book on evaluation, RAG and inference but is about 22 months old. Two 2026 books overtake older editions on currency: Raschka's *Build a Reasoning Model* (2026-06-30) and *Programming Massively Parallel Processors*, 5th edition (2026-06-03). | [S60] [S92] [S93] | B |
| KF15 | COI: Anthropic's free Academy launched as Anthropic Academy on 2026-03-02 and was renamed Claude Academy on 2026-08-20 (22–26 courses; counts differ by source); its certificate is described as an attendance record. Andrej Karpathy joined Anthropic on 2026-05-19, so his materials are COI-adjacent. | [S68] [S72] [S82] | C |

## Recommendation

**Decision rules for a job seeker**

1. **Start with the free minimal set for your family** (Section 3). Use the rubric score as a tie-breaker. It is not an outcome predictor.
2. **For fast-moving topics, use material updated within about 12 months.** Check the version before following a tutorial: AI SDK 7, LangChain 1.x, the Responses API, OWASP 2026 and the EU AI Act as amended in 2026 are the present references (Section 6). Pin tool versions (K5).
3. **Do not buy on placement or salary statistics.** K1 holds for GenAI-specific courses: no independent audit exists. Treat "X% placed" as E unless the programme gives the denominator, the definition, the period and an independent auditor.
4. **Pay only for something free cannot give**, namely live feedback on a graded project from named practitioners. Before paying, get in writing: the total price including any lender interest, a full-refund window of at least 14 days from the first session (Maven's refund policy covers the first two weeks only where its badge is shown), and, for any outcome claim, its method. If any item is missing, rate the programme "watch".
5. **Treat ISA, pay-after-placement and EMI as loans.** Read the lender's terms separately from the course contract. The BloomTech findings rest on US law. The structural risks (finance charge, contested placement claims, a lender holding the receivable) can apply elsewhere.
6. **Compute:** use free notebooks and free LLM API tiers first, but expect limits to move. Rent consumer GPUs (US$0.29–0.91 per hour) for fine-tuning labs. Use H100s (US$3.99–4.59 per hour) only for short labs. Recheck prices monthly, because they moved twice in six weeks.
7. **In India:** the free route covers every family. If you pay, keep screenshots of the claims made at sale, because refund disputes have succeeded before consumer commissions on service-failure grounds (not legal advice).
8. **Vendor-authored material (NVIDIA, OpenAI, Anthropic) is good for that vendor's stack.** Cross-check it with one independent source.

**What would change these rules:** independent audited outcomes for a GenAI-specific course; a change in refund terms or price; a resource going stale; a regulator finding against a named programme.

## Alternatives Considered

| Option | Verdict | Reason | Failure mode |
|---|---|---|---|
| Rank by learner outcomes | Rejected | No independent GenAI outcome data (KF1). | Not applicable. |
| Rank by stars, enrolment, affiliate "best course" lists | Rejected | Popularity is not evidence. Several price figures came from affiliate pages. | Rewards marketing. |
| Link only primary docs (the knowledge base's present stance) | Kept as the default for tools | Durable and checkable. | Learners still lack a curriculum order, so it is paired with the census. |
| Rubric-rated census (this report) | Preferred | Transparent weights; flags COI; separates quality from outcome claims. | False precision, since scores are M and role fit is judgement. |
| Free minimal sets first | Preferred | Free items score 75–97 where they exist. | Drop-off without feedback. Mitigate with cohort-style courses (LLM Zoomcamp, ARENA-style study groups). |
| Selective paid cohort (for example Maven AI Evals) | Allowed with gates | Quality scores 75–80 before gates. | Price volatility (US$3,000 to US$4,200); the October 2026 cohort was announced as the last of 2026; the week-2 refund end date may fall under 14 days. |
| India paid bootcamps and executive programmes | Use-with-care or watch | Documented refund terms exist for Scaler and upGrad. | Pre-start-only refunds; lender lock-in; vendor-commissioned outcome reports. |
| ISA or pay-after-placement bootcamps | Avoid unless audited and refundable | CFPB findings on BloomTech; no audit found for Indian ISA providers. | Loan-like obligation; unaudited claims. |
| Certificate-first path | Out of scope | Certificates are unproctored completion records (KF5). | Signals completion only. |
| Degree programmes | Context only | Another session covers credentials. | Not applicable. |

## Detailed Findings

### 1. Rating method

Each resource is scored 0–5 on five criteria. Weights multiply the score, so the total is out of 100: **T = 4A + 4C + 4H + 5R + 3$**. Outcome adjustments and gates are applied afterwards. Grade M throughout.

| Criterion | Weight | Scoring rule (0–5) |
|---|---|---|
| A: Authority | 20 | 5 maintainer, primary specification or university course by recognised researchers. 4 practitioner or author with a public record. 3 vendor or lab (COI-flagged). 2 transparent unknown, or a seller of the credential. 1 affiliate or anonymous. 0 untraceable. |
| C: Currency | 20 | Fast topics (LLM apps, agents, evaluation, serving): age of last update ≤6 months = 5, ≤12 = 4, ≤18 = 3, ≤24 = 2, ≤36 = 1, older or retired API = 0. Medium topics (post-training, systems, governance frameworks): thresholds doubled. Foundations: current edition = 5, superseded but durable = 3–4, obsolete = 0. |
| H: Hands-on depth | 20 | 5 graded or autograded assignments or a reviewed capstone. 4 projects with feedback or runnable labs. 3 unreviewed notebooks or exercises. 2 demos or quizzes. 1 reference or video only. 0 none. |
| R: Role fit | 25 | 5 covers most Must and Important skills for the family. 3 covers a core module. 1 tangential. |
| $: Cost (money and hours) | 15 | 5 free and ≤40 h. 4 free and >40 h, or ≤US$100 / ₹8,000. 3 ≤US$500 / ₹40,000. 2 ≤US$2,000 / ₹1.5 lakh. 1 ≤US$5,000 / ₹4 lakh. 0 above, or price not published. |

**Outcome adjustment.** Default 0. Up to +3 for independent audited outcomes (only Codesmith received +2; no GenAI-specific resource qualifies). −10 for untraceable placement or recognition claims. −25 for a regulator or court adverse finding.

**Gates.**
- **G1 Currency:** a fast-topic resource more than 18 months old, or built on a retired API, is capped at use-with-care (retired API: avoid).
- **G2 Paid:** above US$100 / ₹8,000, "use" needs a confirmed full-refund window of at least 14 days from the first session and traceable (or no) outcome claims.
- **G3 COI:** marked, with no score change.
- **G4:** a vendor-awarded title with no independent assessment is capped at watch. A regulator or court adverse finding, or closure, means avoid.
- **G5:** a partial or unfinished course is capped at use-with-care.

**Bands.** ≥75 use; 55–74 use-with-care; 40–54 watch; <40 watch (avoid where G4 applies).

**Limits.** Role-fit scores are judgement. A numerical weight-sensitivity run was not performed; I made only spot checks in which the top item in each family stayed on top.

### 2. Census by role family

Columns: resource · kind · cost · hours · last update · A/C/H/R/$ → score · verdict · grade. "n/d" means not determined.

#### 2.1 Applied AI Engineering

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| DataTalks.Club LLM Zoomcamp | cohort course | free | 10 wk, 5–15 h/wk (C) | cohort 2026-06-08 | 4/5/4/5/4 → 89 | use | B |
| Model-provider API docs (OpenAI Responses; Anthropic COI; Google) | docs | free | n/a | continuous; Assistants API retired 2026-08-26 | 5/5/1/5/5 → 84 | use | D |
| Hugging Face Agents Course | course | free | n/d | n/d; certificate rules live | 5/3/4/4/5 → 83 | use | B |
| Vercel AI SDK docs | docs | free | n/a | AI SDK 7, 2026-06-25 | 4/5/3/4/5 → 83 | use (pin 7.x; v6 code needs the v7 codemod) | B |
| Hugging Face LLM Course | course | free | ~15–20 h (C) | relaunched 2025-04-03 | 5/4/3/4/5 → 83 | use | B |
| DeepLearning.AI Agentic AI (Ng) | course | videos free; Pro US$25–30/mo | n/d | 2026 | 5/4/3/4/4 → 80 | use (skip paid certificate) | B |
| Maven AI Evals | paid cohort | US$4,200 (cohort 2026-10-10 to 11-21; last of 2026) | 33 live sessions over 6 weeks (3–5 h/wk per a third party) | cohort 2026-10 | 4/5/4/4/1 → 75, G2 | use-with-care | C |
| LangChain / LangGraph docs | docs | free | n/a | 1.0 GA 2025-10-22 | 4/4/3/3/5 → 74 | use-with-care (≥1.0 only) | B |
| Claude Academy (COI) | free courses | free | 22–26 courses | renamed 2026-08-20 | 3/5/2/3/5 → 70 | use-with-care | C |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h (M) | 1st ed. 2025-01-07 | 5/2/1/5/4 → 69, G1 | use-with-care | B |

#### 2.2 ML Engineering & Applied Science

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Hugging Face LLM Course | course | free | ~15–20 h (C) | 2025-04-03 relaunch | 5/4/3/5/5 → 88 | use | B |
| Stanford CS336 | university course | free | 17–18 lectures + 5 assignments | Spring 2026 (2026-03-30 to 06-03) | 5/5/5/3/4 → 87 | use (optional depth) | B |
| Raschka, *Build a Reasoning Model (From Scratch)* (Manning) | book | ~US$60 print | 440 pp (~11 h listed) | 2026-06-30 | 5/5/3/4/4 → 84 | use | B |
| Karpathy, Zero to Hero | lectures | free | ~19 h (C) | n/d | 5/4/3/4/5 → 83 | use | C |
| Raschka, *Build a Large Language Model (From Scratch)* (Manning) | book | CA$67.99 on one listing | 368 pp | 2024-10-29 | 5/4/3/4/4 → 80 | use | B |
| Hugging Face smol course | course | free | ~4 h/wk (C) | n/d | 5/3/3/4/5 → 79 | use | C |
| DataTalks.Club ML Zoomcamp | cohort course | free | 4 months | 2026 cohort not verified | 4/3/4/4/4 → 76 | use | C |
| DataTalks.Club MLOps Zoomcamp | course | free | self-paced; no 2026 live cohort (C) | n/d | 4/3/4/4/4 → 76 | use | C |
| freeCodeCamp ML with Python | course | free | ~300 h (C) | 2025–26 curriculum | 4/3/4/2/4 → 66 | use-with-care (TensorFlow-based) | C |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h (M) | 2025-01-07 | 5/2/1/4/4 → 64 | use-with-care | B |

#### 2.3 Forward Deployment & Solutions

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| DataTalks.Club LLM Zoomcamp | cohort course | free | 10 wk | 2026-06-08 | 4/5/4/4/4 → 84 | use | B |
| Provider API docs | docs | free | n/a | continuous | 5/5/1/4/5 → 79 | use | D |
| Hugging Face Agents Course | course | free | n/d | n/d | 5/3/4/3/5 → 78 | use | B |
| Claude Academy (COI) | courses | free | 22–26 courses | 2026-08-20 | 3/5/2/3/5 → 70 | use-with-care | C |
| NVIDIA DLI self-paced | courses | US$30 or 90 | per course | catalogue Oct 2026 | 4/2/4/3/4 → 67 | use-with-care | B |
| Scaler AI & ML with Agentic AI (FDE specialisation 2026-07-14) | paid programme | ₹3,99,000 | ~11 months (third party) | 2026 | 3/4/4/4/1 → 67 | use-with-care | B |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h | 2025-01-07 | 5/2/1/4/4 → 64 | use-with-care | B |
| roadmap.sh FDE roadmap | checklist | free | n/a | site updated 2026-09-17 | 3/4/0/3/5 → 58 | use-with-care | B |
| Interview Kickstart | paid cohort | not published | 66 wk (ML track, third party) | n/d | 2/3/3/3/0, −10 → 37 | watch | C |

#### 2.4 AI Infrastructure & Platform

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Stanford CS336 (GPU, parallelism, inference lectures) | university course | free | 17–18 lectures | Spring 2026 | 5/5/5/4/4 → 92 | use | B |
| *Programming Massively Parallel Processors*, 5th ed. (Hwu, Kirk, El Hajj; authors NVIDIA-affiliated) | book | ~€66 e-book, ~€74 paperback | 680 pp | 2026-06-03 | 5/5/3/5/4 → 89 | use | B |
| GPU MODE lectures | lecture series | free | 79+ lectures | n/d; repo created 2024-01-20 | 4/4/3/5/5 → 84 | use | B |
| DataTalks.Club MLOps Zoomcamp | course | free | self-paced | n/d | 4/3/4/4/4 → 76 | use | C |
| NVIDIA DLI self-paced | courses | US$30 or 90 | per course | Oct 2026 | 4/2/4/3/4 → 67 | use-with-care | B |
| Huyen, *AI Engineering* (inference chapter only) | book | ~US$55–80 | n/a | 2025-01-07 | 5/2/1/2/4 → 54 | watch | B |

#### 2.5 Evaluation, Safety & Security

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Inspect AI docs (UK AISI / Meridian Labs) | docs and framework | free | n/a | releases to 0.3.224 | 5/5/3/5/5 → 92 | use | B |
| Hamel Husain's blog | articles | free | n/a | post 2026-09-30 | 4/5/2/5/5 → 84 | use | B |
| BlueDot Technical AI Safety | cohort course | free | 30 h | 2026 | 4/5/3/4/5 → 83 | use | B |
| OWASP GenAI LLM Top 10 2026 and Agentic Top 10 | guidance | free | n/a | 2026-08-03/04; Dec 2025 | 4/5/1/5/5 → 80 | use | B |
| DataTalks.Club LLM Zoomcamp (evaluation, monitoring modules) | cohort course | free | 10 wk | 2026-06-08 | 4/5/4/3/4 → 79 | use | B |
| Maven AI Evals | paid cohort | US$4,200 (2026-10 cohort) | 33 live sessions over 6 weeks | 2026-10 | 4/5/4/5/1 → 80, G2 | use-with-care | C |
| NIST AI RMF 1.0 and AI 600-1 | framework | free | n/a | Jan 2023 / Jul 2024; revision pending | 5/3/1/3/5 → 66 | use-with-care | B |
| Huyen, *AI Engineering* (evaluation chapters) | book | ~US$55–80 | n/a | 2025-01-07 | 5/2/1/4/4 → 64 | use-with-care | B |
| roadmap.sh AI Red Teaming | checklist | free | n/a | site 2026-09-17 | 3/4/0/3/5 → 58 | use-with-care | B |

#### 2.6 Research

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Stanford CS336 | university course | free | 17–18 lectures + 5 assignments | Spring 2026 | 5/5/5/5/4 → 97 | use | B |
| Raschka, *Build a Reasoning Model (From Scratch)* | book | ~US$60 print | 440 pp | 2026-06-30 | 5/5/3/4/4 → 84 | use | B |
| Karpathy, Zero to Hero | lectures | free | ~19 h (C) | n/d | 5/4/3/4/5 → 83 | use | C |
| BlueDot Technical AI Safety | cohort course | free | 30 h | 2026 | 4/5/3/4/5 → 83 | use | B |
| ARENA curriculum (public; cohorts at LISA, London) | self-study curriculum | free | 4–5 weeks full-time | ARENA 9.0, 2026-10-05 to 11-06 | 4/4/4/4/4 → 80 | use | B |
| BlueDot AGI Strategy | cohort course | free | 25 h | 2026 | 4/5/3/3/5 → 78 | use | B |
| Hugging Face LLM Course | course | free | ~15–20 h | 2025-04-03 | 5/4/3/3/5 → 78 | use | B |
| Hugging Face smol course | course | free | ~4 h/wk | n/d | 5/3/3/3/5 → 74 | use-with-care | C |
| GPU MODE lectures | lectures | free | 79+ | n/d | 4/4/3/3/5 → 74 | use-with-care | B |
| UC Berkeley Agentic AI MOOC | lectures | free | ~12 × 2 h | Fall 2025 | 5/4/1/3/5 → 70 | use-with-care | B |

MATS is a selective fellowship rather than a learning resource and is not rated.

#### 2.7 Governance, Risk & Assurance

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| BlueDot Frontier AI Governance | cohort course | free | 25 h | 2026 | 4/5/3/3/5 → 78 | use | B |
| NIST AI RMF 1.0 and Generative AI Profile (AI 600-1) | framework | free | n/a | Jan 2023 / Jul 2024; revision in progress | 5/3/1/5/5 → 76 | use | B |
| EU AI Act explorer with the Digital Omnibus text (artificialintelligenceact.eu; official text on EUR-Lex not opened) | legal text and guide | free | n/a | Omnibus in force 2026-07-27 | 3/5/1/5/5 → 76 | use (verify dates against EUR-Lex) | B |
| BlueDot AGI Strategy | cohort course | free | 25 h | 2026 | 4/5/3/2/5 → 73 | use-with-care | B |
| OWASP GenAI LLM Top 10 2026 | guidance | free | n/a | 2026-08 | 4/5/1/3/5 → 70 | use-with-care | B |
| Claude Academy AI Fluency track (COI) | courses | free | n/d | 2026-08-20 | 3/5/2/2/5 → 65 | use-with-care | C |

Chicago Booth's ten-month Chief AI Officer programme (US$28,000, per press reports [S77]) is price context and is not rated. No independently rated syllabus for audit and compliance practice was found.

#### 2.8 Product & Program

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Hamel Husain's blog | articles | free | n/a | 2026-09-30 | 4/5/2/4/5 → 79 | use | B |
| Maven AI Evals | paid cohort | US$4,200 (2026-10 cohort) | 33 live sessions over 6 weeks | 2026-10 | 4/5/4/4/1 → 75, G2 | use-with-care | C |
| Hugging Face LLM Course (literacy) | course | free | ~15–20 h | 2025-04-03 | 5/4/3/2/5 → 73 | use-with-care | B |
| Claude Academy (COI) | courses | free | 22–26 | 2026-08-20 | 3/5/2/3/5 → 70 | use-with-care | C |
| Maven AI Product Management Certification | paid cohort | US$2,500 list | n/d | 2026 | 3/4/3/5/1 → 68 | use-with-care | C |
| BlueDot Future of AI | self-paced | free | 2 h | 2026 | 4/5/1/2/5 → 65 | use-with-care | B |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h | 2025-01-07 | 5/2/1/3/4 → 59 | use-with-care | B |

#### 2.9 Human Data & Evaluation Operations

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Inspect AI docs (for a move into evaluation harness work) | docs | free | n/a | 2026 | 5/5/3/2/5 → 77 | use | B |
| Hamel Husain's blog (error analysis, rubrics) | articles | free | n/a | 2026-09-30 | 4/5/2/3/5 → 74 | use-with-care | B |
| aitrainer.work Academy (platform-run, COI) | free courses | free | 15+ h | 2026-04-21 | 2/5/2/4/5 → 71 | use-with-care | C |
| Annotation Academy AI Evaluator Certification | paid | ~US$249 (M, 4 × US$62.25) | 30+ h | 2026 | 2/4/3/4/3, −10 → 55, G4 | watch | C |

No curriculum with independent evidence of employer recognition was found. Platforms gate entry with their own qualification tests (C) [S74].

#### 2.10 Embodied & Physical AI

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| NVIDIA Physical AI learning (Isaac Sim, Isaac Lab, GR00T) | free courses | free | 2–20+ h each | 2026 | 4/5/4/4/5 → 87 | use | B |
| Tedrake, Underactuated Robotics (MIT 6.832 / 6.8210; fundamentals) | open notes and lectures | free | semester course | notes © 2024 | 5/3/4/3/4 → 75 | use | B |
| Hugging Face Robotics Course (LeRobot) | course | free | units of 30–45 min | partial release; later units "coming soon" in one snapshot | 5/2/3/4/5 → 75, G5 | use-with-care | B |
| Karpathy, Zero to Hero (foundations) | lectures | free | ~19 h | n/d | 5/4/3/2/5 → 73 | use-with-care | C |

Modern Robotics (Lynch and Park) is cited only as a reference in a university syllabus and was not rated.

#### 2.11 Leadership & Executive

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| BlueDot AGI Strategy | cohort course | free | 25 h | 2026 | 4/5/3/3/5 → 78 | use | B |
| DataTalks.Club LLM Zoomcamp (to see what teams build) | cohort course | free | 10 wk | 2026-06-08 | 4/5/4/2/4 → 74 | use-with-care | B |
| NIST AI RMF and AI 600-1 | framework | free | n/a | Jan 2023 / Jul 2024 | 5/3/1/3/5 → 66 | use-with-care | B |
| Claude Academy (COI) | courses | free | 22–26 | 2026-08-20 | 3/5/2/2/5 → 65 | use-with-care | C |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h | 2025-01-07 | 5/2/1/3/4 → 59 | use-with-care | B |
| upGrad × IIIT-B Executive Programme in GenAI for Leaders | paid programme | ₹2,25,000 incl. GST | 5 months | 2026 listing | 3/4/3/3/1 → 58, G2 | use-with-care | C |
| roadmap.sh Engineering Manager roadmap | checklist | free | n/a | site 2026-09-17 | 3/4/0/2/5 → 53 | watch | B |

#### 2.12 Independent & Fractional

| Resource | Kind | Cost | Hours | Last update | Score | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Hamel Husain's blog | articles | free | n/a | 2026-09-30 | 4/5/2/3/5 → 74 | use-with-care | B |
| Provider API docs | docs | free | n/a | continuous | 5/5/1/3/5 → 74 | use-with-care | D |
| Maven AI Evals | paid cohort | US$4,200 | 33 live sessions over 6 weeks | 2026-10 | 4/5/4/3/1 → 70 | use-with-care | C |
| NIST AI RMF and AI 600-1 | framework | free | n/a | 2023 / 2024 | 5/3/1/3/5 → 66 | use-with-care | B |
| Huyen, *AI Engineering* | book | ~US$55–80 | ~25–30 h | 2025-01-07 | 5/2/1/4/4 → 64 | use-with-care | B |
| Vendor-awarded "Certified AI Consultant / Fractional CAIO" (chiefaiofficer.com; 3-day and 10-week tracks) | paid certification | price not seen | 3 days / 10 weeks | 2025–26 | not scored (G4) | avoid | C |

### 3. Minimal sets

| Family | Minimal free set (reason) | Minimal paid set (reason) | Grade |
|---|---|---|---|
| Applied AI Engineering | LLM Zoomcamp (graded project, evaluation module); provider docs plus pinned SDK docs (AI SDK 7 or LangChain 1.x); HF Agents Course (agent loop, free certificate) | None needed. Optional: Maven AI Evals (US$4,200) only if employer-funded, after a harness v0 exists; the October 2026 cohort was announced as the last of 2026 | M |
| ML Engineering & Applied Science | Zero to Hero → HF LLM Course → ML or MLOps Zoomcamp (fundamentals to fine-tuning to serving); CS336 optional | Raschka's reasoning-model book (~US$60) if post-training is the target; otherwise none | M |
| Forward Deployment & Solutions | LLM Zoomcamp; provider and cloud docs; HF Agents (customer-facing prototypes) | Huyen book for architecture vocabulary. Scaler FDE only after written refund terms | M |
| AI Infrastructure & Platform | CS336 systems lectures; GPU MODE lectures; MLOps Zoomcamp | PMPP 5th ed. (~€66–74) and rented GPUs at US$0.29–0.91/h for labs | M |
| Evaluation, Safety & Security | Inspect docs; Hamel's blog; OWASP 2026; BlueDot Technical AI Safety | Maven AI Evals if funded | M |
| Research | CS336; Zero to Hero; BlueDot Technical AI Safety or the public ARENA curriculum | Raschka's reasoning-model book (optional) | M |
| Governance, Risk & Assurance | NIST AI RMF plus AI 600-1; EU AI Act explorer (check EUR-Lex); OWASP 2026; BlueDot Frontier AI Governance | None verified; certifications are another session | M |
| Product & Program | HF LLM Course; Hamel's blog; BlueDot Future of AI (2 h) | Maven AI PM (US$2,500 list) or Evals (US$4,200), employer-funded | M |
| Human Data & Evaluation Operations | aitrainer.work Academy; Hamel's blog (rubrics, error analysis) | None recommended; the certification title lacks independent standing | M |
| Embodied & Physical AI | NVIDIA Physical AI courses; Tedrake's Underactuated Robotics (fundamentals); HF Robotics Course; Zero to Hero | Hardware or GPU rental only (24 GB+ GPU for Isaac Sim per a third-party guide, C) | M |
| Leadership & Executive | BlueDot AGI Strategy; NIST AI RMF; EU AI Act explorer; LLM Zoomcamp (to see what teams build) | Huyen book; executive programmes are context only | M |
| Independent & Fractional | NIST AI RMF; Hamel's blog; provider docs | Huyen book; Maven Evals. Avoid vendor-awarded CAIO titles | M |

### 4. Paid programmes

| Programme | Price | Duration | Syllabus currency | Instructors | Outcome claims and status | Refund | Verdict | Grade |
|---|---|---|---|---|---|---|---|---|
| Maven AI Evals for Engineers & PMs (Parlance Labs) | US$4,200 for the 2026-10-10 to 2026-11-21 cohort on Maven's page (one promo-code variant shows US$4,400); US$5,000 list in a 2026-03 affiliate list; about US$3,000 in 2025 (attendee review) | 6 weeks on Maven's page (33 live sessions, 11 lessons); third-party listings say 4 weeks at 3–5 h/wk | material refreshed for the 2026 cohorts; agent-centred; the October cohort is announced as the last of 2026 | Hamel Husain, Shreya Shankar | No job claims. "5,000+ engineers and PMs" is enrolment (vendor, COI); 4.7★ from 1,012 self-collected platform ratings (C) | Refund-policy badge shown on the page. Maven's policy gives a full refund through the Week 2 end date in the syllabus for courses of four weeks or more; week 1 is listed as Oct 10–11, so the window may be shorter than 14 days from the first session (not confirmed). An older rule allowed 14 days after the course ends | use-with-care | C |
| Maven AI Product Management Certification | US$2,500 list (US$2,000 with a discount) | n/d | n/d | Rohan Varma, Henry Shi | 4.8★ from 1,000+ platform reviews (affiliate-sourced) | as Maven policy, badge unconfirmed | use-with-care | C |
| Scaler AI & ML with Agentic AI | ₹3,99,000 total; EMI from ₹9,791/month with ₹20,000 upfront (listed on the sibling DSML page) | ~11 months (third party) | renamed; FDE specialisation added 2026-07-14 | n/d | 89% placed (11,444 of 12,851 completers, 2024–25 cohorts); KPMG-commissioned mean ₹21.6 LPA, median ₹17.5 LPA. Vendor-published (COI), traceable only to the vendor | 14 days from first class | use-with-care | B |
| upGrad × IIIT-B Applied AI & Agentic AI Executive Program | ₹1,25,000; EMI ₹5,631 | n/d | n/d | IIIT-B faculty | placement assistance; no placement promise (third party) | before programme start (GenAI certificate page); 30 working days to process | use-with-care | B |
| upGrad × IIIT-B Executive Programme in GenAI for Leaders | ₹2,25,000 incl. GST | 5 months | n/d | IIIT-B and Microsoft | dual certificate; no outcome claim found | as above | use-with-care | C |
| Great Learning × UT Austin McCombs PGP-AIML | US$3,950 for the 23-week track (programme page, read 2026-10-08 by a directory); ₹2.1–3.35 lakh plus GST in India listings (12-month track) | 23 weeks or 12 months (two tracks on the McCombs page) | not opened; page lists AI agents and GenAI | UT Austin McCombs faculty plus Great Learning mentors | No traceable outcome data; an unsourced ₹16 lakh median on an aggregator (E); ASCI upheld complaints on Great Lakes ads in 2018; platform reviews are high (4.93/5 from 505 reviews, self-selected) and a complaints site lists 13 complaints with 5 resolved (C) | For the MIT IDSS variant: US$250 fee more than 7 days after acceptance, rising to 100% near commencement; the UT Austin variant has a three-instalment fee table and its cancellation terms were not opened | watch | C |
| Simplilearn AI/ML programmes (Purdue × IBM and other partner variants) | PG Program in AI & ML US$4,800 on the programme page (US$4,300 in a Feb 2026 snapshot); ₹1,89,999 (aggregator) or ₹2,85,000 (a vendor city page); Applied GenAI Specialization US$2,995 (16 weeks); Generative AI for Business Transformation US$2,499 (12 weeks) | 12 weeks to 11 months | 2025–26 snapshots; currency unverified | Purdue faculty, IBM and Simplilearn trainers | Vendor ranking claims; an advocacy group alleges inflated ratings and career claims; ~100 BBB complaints (C); no regulator finding found; no ISA and no job-placement promise per a directory | Purdue/IBM page: withdrawal allowed with an administration charge deducted. Wharton-distributed programmes: requests only within 7 days of purchase (vendor policy page). Directory says terms are not stated on the public Purdue pages (C) | watch | C |
| Interview Kickstart (ML with Agentic AI; Gen AI India) | not published; India tracks from ₹1,10,000+ or ₹1,30,000+; US third-party US$4,900–9,600 | ML track 66 weeks (third party) | not opened | n/d | "average salary hike 53%" (2021 alumni) and a staff claim of 8,241 placed; unaudited; vendor says it is not a placement service | 50% only if tests passed within 5 attempts, ≥80% attendance and documented claim; listed India tracks: none; BBB 1/5 from 5 reviews | watch | B/C |
| Codesmith Software Engineering + AI/ML Immersive | US$22,500 | 14 wk full-time / 39 wk part-time | AI/ML added 2024 | n/d | CIRR-audited, general software cohort: 43.6% in-field at 180 days (2023, 865 graduates, directory summary); school reports 70.1% within 12 months | n/d | use-with-care | C |
| Springboard ML Engineering Career Track | US$11,990 up front | ~9 months | not opened | n/d | tuition-back offer if not placed; terms not opened | not opened | watch | C |
| Masai / Newton School ISA (India) | ₹2.5–4.5 lakh paid after placement (tiered), NBFC-financed | n/d | n/d | n/d | 94% placed (vendor, unverified) | ISA pause and withdrawal terms differ by unit | watch | C |
| NVIDIA DLI self-paced / workshops | US$30 or 90; workshops from US$500; private from US$10,000 | per course | catalogue of 52 courses, Oct 2026 | NVIDIA | certificate of competency after an assessment | none (non-refundable) | use-with-care | B |
| BloomTech (ISA, closed) | n/a | n/a | n/a | n/a | CFPB found false hiring-rate claims and mis-described ISAs | n/a | avoid | B |
| Vendor-awarded CAIO / AI Consultant titles | not seen | 3 days / 10 weeks | n/d | n/d | no independent assessment or outcome evidence | n/d | avoid | C |

### 5. Outcome evidence

| Evidence | Date | Finding | Grade |
|---|---|---|---|
| CFPB consent order, BloomTech (2024-CFPB-0001) | 2024-04-17 | ISAs (17% of pre-tax income above US$50,000, capped at 24 payments or US$30,000) were loans described as non-loans. At least 11,000 were originated since 2017. Hiring-rate claims were false. Permanent lending ban; 10-year student-lending ban on the CEO. | B [S1–S4] |
| Earlier CFPB ISA orders | 2021, 2023 | Better Future Forward (2021) and Prehired (2023) are earlier actions on ISAs treated as credit. | B [S6] |
| California BPPE closure notice | n/d | BloomTech closed; last day of instruction 2025-12-31; Student Tuition Recovery Fund noted. | B [S5] |
| CIRR (industry audit body) | early 2026 | Three schools publish CIRR data (Code Platoon, Codesmith, Hacktiv8). | C [S56] |
| Codesmith CIRR | 2023 cohort | 865 graduates; 43.6% in-field at 180 days (directory summary). School blog: 70.1% in-field within 12 months and US$110,000 median (2023–24 report). | C [S57] [S58] |
| India, CCPA coaching sector | 2025-04-17 | 49 notices; ₹77.60 lakh in penalties on 24 coaching centres; National Consumer Helpline secured ₹1.56 crore of refunds for 600+ students. No order on a GenAI bootcamp found. | C [S45] |
| Hyderabad District Commission-I, *Sai Kumar v EduBridge Learning* (CC 580/2023) | 2024-06-14 | Training firm facilitated a lender loan; refusing a refund after two classes was deficiency in service and unfair trade practice. Full refund, ₹10,000 compensation, ₹5,000 costs. Course was accounting/GST. | B [S44] |
| Delhi State Commission, FIITJEE | reported 2025-11-20 | Upheld a refund despite a no-refund clause (coaching, not IT). | B [S46] |
| ASCI Consumer Complaints Council | 2018 | Unsubstantiated "100% placement" and rank claims upheld across 201 education ads (Aug–Sept 2018); Great Lakes (Great Learning) advertising upheld in March 2018. Stale. | B [S47] |
| Truth in Advertising on Simplilearn | ~2025-12 | Alleges rating inflation and restrictive refunds; advocacy source. | C [S48] |
| Consumer complaints about Great Learning refunds | 2024-07 to 2026-04 | Voxya, a paid complaint-resolution service, lists 13 complaints against Great Learning with 5 resolved (38.46%), including a 2025-09-14 complaint about a refused refund after same-month cancellation. Self-reported, unverified, and the site has a commercial interest. | C [S88] |
| Vendor outcome reports (Scaler, Interview Kickstart, Masai) and platform ratings (Maven) | 2021–2026 | Self-published, commissioned or self-collected; denominators and audit not shown. Ratings are satisfaction, not outcomes. | C/E [S49] [S52] [S76] [S87] |

### 6. Staleness

| Resource | Status as of 2026-11-13 | Superseded by | Grade |
|---|---|---|---|
| OpenAI Assistants API tutorials | API retired 2026-08-26 | Responses API | B [S69] |
| LangChain pre-1.0 chains, `AgentExecutor`; LangGraph `create_react_agent` | deprecated at 1.0 GA (2025-10-22) | LangChain `create_agent`; a 2026-04 analysis found most top-ranked tutorials still used old patterns | B [S70] |
| Ragas 0.1–0.2 tutorials | API changed twice; last release 0.4.3 on 2026-01-13; no commits to main after 2026-02-24; SSRF CVE-2026-6587 (2026-04-20) | DeepEval or Inspect for harnesses; plan to patch Ragas yourself | C [S14] [S15] [S16] |
| Vercel AI SDK 5 and 6 tutorials | AI SDK 6 shipped 2025-12-22; AI SDK 7 shipped 2026-06-25 (ESM-only, Node.js 22 or later, `npx @ai-sdk/codemod v7`); an unpinned install pulls v7 (C) | AI SDK 7 (7.0.x) | B [S17] [S80] [S81] |
| WebMCP early tutorials using `navigator.modelContext` | API moved to `document.modelContext` (Chrome 149 origin trial; 150 deprecation) | current WebMCP draft (a W3C community-group report, not a standard) | C [S20] [S21] |
| OWASP LLM Top 10 2023 v1.1 and 2025 | 2026 edition published 2026-08-03/04 | OWASP GenAI LLM Top 10 2026 plus Agentic Top 10 | B [S64] |
| EU AI Act guides centred on a 2026-08-02 high-risk deadline | Digital Omnibus on AI, Regulation (EU) 2026/1744, in force 2026-07-27: Annex III high-risk moved to 2027-12-02, Annex I to 2028-08-02; Article 50 transparency applied from 2026-08-02 (watermark grace to 2026-12-02 for systems already on the market) | AI Act as amended in 2026 | B [S89] |
| Hugging Face NLP Course | relaunched as the LLM Course 2025-04-03 | HF LLM Course | B [S23] |
| DeepLearning.AI "short courses are free" | videos free; labs, quizzes, certificates need Pro | Pro US$25–30/mo; a third-party Dec 2025 article reported US$15 | B [S28] [S29] |
| NVIDIA "Building RAG Agents with LLMs" as free | listed at US$90 in the Oct 2026 catalogue | catalogue price at checkout | C [S32] |
| Colab Pro for Education; SageMaker Studio Lab | closed to new users | Kaggle, Colab free, paid rental | B [S26] |
| Free LLM API limits quoted in older posts | limits are per model or per project and change; flagship models reported as paid-only from April 2026 | check each provider's rate-limit page | C [S83] |
| Lambda H100 at US$2.99 | older cached snapshot (date not shown) | US$3.99–4.59 (Sept–Nov 2026) | C [S41] [S43] |
| *Programming Massively Parallel Processors*, 4th edition | 5th edition published 2026-06-03 (680 pp; new filtering, wavefront, multi-GPU and advanced matrix-multiplication material) | 5th edition | B [S93] |
| Karpathy LLM101n | announced 2024; not shipped; Eureka Labs set aside after Karpathy joined Anthropic (2026-05-19); do not plan around it | Zero to Hero, nanochat, CS336 | B/C [S72] [S82] |
| Huyen, *AI Engineering* (Jan 2025) | predates much of the 2025–26 agent tooling | use for concepts only | B [S60] |
| NIST AI RMF | 1.0 remains the published core; revision in progress. One source claims "1.1 released" and conflicts with the others. | check nist.gov before using templates | C [S63] |

### 7. Compute

| Option | Allowance, limit or price | As of | Verdict | Grade |
|---|---|---|---|---|
| Google Colab free | "very limited" GPUs; sessions ≤12 h; no published quota. Pro US$9.99/month (100 units); Pro+ US$49.99/month (600 units) | 2026-09-21 | use | B [S26] [S27] |
| Kaggle Notebooks | T4/P100-class; 12 h CPU/GPU and 9 h TPU sessions; weekly GPU quota set in the account (commonly reported ~30 h, not in docs). Colab Pro/Pro+ linked users get +15/+30 GPU h per week | 2026-09-21 | use | B [S26] |
| Hugging Face ZeroGPU | free account 5 min/day; PRO US$9/month gives 40 min; demos only | 2026-09-21 | use-with-care | B [S26] |
| Lightning AI free plan | 1 free Studio (4-hour restarts), 50 GB; credit amount unconfirmed | 2026-09-21 | watch | B [S26] |
| Free LLM API tiers | A docs-reading tracker found standing free tiers at 8 of 17 providers on 2026-10-18 (Gemini API, Mistral, Groq, OpenRouter, Z.ai, Cloudflare Workers AI, NVIDIA API Catalog, Cohere). Anthropic, Alibaba and Cerebras gave credits that run out (a November 2026 comparison still lists Cerebras at about 1M tokens/day, so sources conflict). OpenAI, DeepSeek, Moonshot, xAI, Hugging Face Inference Providers and GitHub Models had no free tier. Typical limits: Groq 30 requests/min and ~1,000/day on some models (14,400/day on an 8B model); OpenRouter `:free` models 20/min and 50/day (1,000/day after a US$10 credit purchase); Google AI Studio limits shown per project only; flagship models reported as paid-only from April 2026 | 2026-10-18 | use-with-care | C [S83] |
| Modal Starter | US$30/month credit; T4 US$0.59/h, L4 US$0.80/h, A100 40GB US$2.10/h, H100 US$3.95/h; US$30 buys ~7.6 H100-hours (M); academic grants up to US$10k by application | 2026-07 | use | B/C [S37] [S38] |
| RunPod | Community RTX 4090 from US$0.34/h (2026-08-04); Secure RTX 4090 US$0.89, H100 PCIe US$2.89, H100 SXM US$3.99, A100 PCIe US$1.79 (2026-10-15); Community prices unchanged | 2026-10-15 | use-with-care | B [S39] [S40] |
| Lambda | H100 SXM US$3.99 (8×) to US$4.29 (1×); A100 80GB US$2.79; B200 US$6.69; tracker shows H100 US$4.59 in a Nov capture; no spot | 2026-09-19 to 2026-11-09 | use-with-care | C [S41] [S42] [S43] |
| Cheapest in-stock rental (aggregator) | RTX 3090 US$0.29 (LeaderGPU); RTX 4090 US$0.41 (Vast.ai); L4 US$0.93 (Ori); A100 US$0.68 (LeaderGPU); T4 none in stock | 2026-11-11 | use | B [S26] |
| Hyperscaler trials | Google Cloud US$300/90 days (no GPUs in trial); AWS up to US$200/6 months (select services); Azure US$200/30 days | 2026-09-21 | watch | B [S26] |
| Student programmes | GitHub pack US$100 Azure credit plus 5 GPU hours (Camber); Azure for Students US$100/12 months; Studio Lab and Colab Pro for Education closed to new users | 2026-09-21 | use-with-care | B [S26] |
| Startup programmes | Google for Startups up to US$200,000 (US$350,000 AI-first); AWS Activate up to US$200,000 (portfolio); Microsoft up to US$150,000; NVIDIA Inception (no amount, no fee or equity) | 2026-09-21 | use | B [S26] |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | No GenAI course or bootcamp has outcome data beyond vendor figures | updated | [S1] [S5] [S56] [S57] [S58]. CIRR audits exist for general bootcamps. Codesmith's audited 2023 cohort predates its AI/ML syllabus. No GenAI-specific audit found. | C |
| K2 | Learn by building toward a gate | unverifiable | [S22] [S33]. The best-rated application resources are project-first. No controlled evidence found. | P |
| K3 | Put evaluation first; 30 cases in two weeks | unverifiable | [S33] [S65] [S66] [S67]. Top resources agree on practice. No outcome evidence found. | P |
| K4 | API credits plus free notebooks cover months 1–6; rent GPUs for serving or fine-tuning | updated | [S26] [S27] [S37] [S83]. Free notebook tiers are narrower (two programmes closed; opaque quotas). Free LLM API tiers exist at some providers but are volatile; a docs-reading tracker (2026-10-18) found OpenAI with no free tier and Anthropic offering credits (COI-adjacent), and flagship models were reported as paid-only from April 2026. | C |
| K5 | Tools change shape; pin versions (AI SDK 6, WebMCP, Promptfoo, Langfuse, RAGAS) | updated | [S10] [S11] [S12] [S13] [S14] [S17] [S20] [S21] [S80] [S81]. The pattern holds, but AI SDK 6 shipped on 2025-12-22 and was superseded by AI SDK 7 on 2026-06-25. Also LangChain 1.0, Assistants API retirement and OWASP 2026 [S64] [S69] [S70]. | B |
| K6 | roadmap.sh: use-with-care; viable from recall only | updated | [S35]. Currency verified (changelog 2026-09-17). Role roadmaps exist for FDE, AI Agents, AI Red Teaming and MLOps. A paid Roadmap Pro and courses exist. | B |
| K7 | Coursera and Udemy merged May 2026; catalogue may shift | confirmed | [S7] [S8] [S95] [S96]. Completed 2026-05-11. SEC filings show two restructurings: 2026-07-06 and a roughly 10% global workforce reduction on 2026-11-09. | B |
| K8 | freeCodeCamp: free; viable from recall only | updated | [S36]. Nonprofit and free. The 2025–26 curriculum added exam-based certificates. ML with Python is TensorFlow-based. LLM tutorials are posted (2026-10-08). | C |
| K9 | HF Learn free; Agents certificate needs Unit 1, assignment, final challenge | confirmed | [S22] [S24] [S25]. Fundamentals certificate needs Unit 1 and an 80% quiz. Final needs >30% on the GAIA subset. Certificate free. | B |
| K10 | Kaggle: 12 h GPU/CPU, 9 h TPU; ~30 h quota not in docs | confirmed | [S26]. The quota floats and appears only in the account. | B |
| K11 | DeepLearning.AI: free short courses; Pro US$30–50, sources conflict | updated | [S28] [S29]. Videos free; Pro US$25/month annual or US$30 monthly with a 7-day trial; labs and certificates behind Pro. | B |
| K12 | NVIDIA DLI price and format unverified; catalogues from 2019–2021 | updated | [S30] [S31] [S32]. Self-paced US$30 or 90; public workshops from US$500; certificates of competency after assessment; non-refundable. | B |
| K13 | LLM Zoomcamp: free, 10 weeks, project-based | updated | [S33] [S34]. 2026 cohort began 2026-06-08. Certificate only in a live cohort. An optional paid membership exists. | B |
| K14 | ISA bootcamps (BloomTech model): avoid; closed | confirmed | [S1] [S2] [S3] [S5] [S6]. | B |
| K15 | Modal US$30 credit; T4 0.59, L4 0.80, H100 3.95 per hour; ~7.6 H100-hours | confirmed | [S37] [S38]. US$30 ÷ US$3.95 = 7.59 h (M). | B |
| K16 | RunPod RTX 4090 ~US$0.34 (community) to ~0.69 (secure); credits up to US$25K | updated | [S39] [S40]. Secure RTX 4090 US$0.89 after the 2026-10-15 repricing. The credits programme was not verified. | B |
| K17 | Lambda H100 SXM ~US$3.99–4.29; other snapshots US$2.99–3.29 | updated | [S41] [S42] [S43]. The US$2.99–3.29 snapshots are stale. A tracker shows US$4.59 in early November (single source). | C |

## Absences

| Item | Where I looked | Result |
|---|---|---|
| Independent outcome study for a GenAI-specific course or bootcamp | CIRR coverage; Codesmith; regulator and consumer-court searches; Course Report and survey aggregators | None. Only general-bootcamp CIRR data and regulator findings on BloomTech |
| Indian regulator or court finding against upGrad, Great Learning, Simplilearn, Scaler or Interview Kickstart | CCPA, ASCI, district and state commissions | None found. Adjacent coaching and EduBridge records only. District orders are scattered, so absence is weak evidence |
| Refund detail: Great Learning UT Austin variant, the exact Simplilearn administration charge for the Purdue variants, and the Week 2 end date of the Maven AI Evals syllabus | Vendor pages, directory summaries, Maven help centre | Maven badge confirmed; window length versus the first session, and the other two items, not confirmed |
| Free LLM API tier terms from the providers' own pages | Tracker and community comparisons only (one tracker says it read provider docs on 2026-10-18) | Provider pages not opened |
| RunPod credits programme "up to US$25K" | Tracker pages and reviews | Only a referral bonus (US$5–500) found |
| CS336 primary site contents (assignment details and hours) | Page capture, schedule wiki, lecture listings | Primary site not opened |
| Modern Robotics course; MATS programme detail | University syllabus mention; ARENA directory | Not verified; MATS is a fellowship and not rated |
| ISO/IEC 42001 text; EUR-Lex text of Regulations (EU) 2024/1689 and 2026/1744 | Secondary explorers and law-firm notes | Official texts not opened |
| Alammar's *Hands-On Large Language Models*; *Designing Data-Intensive Applications* 2nd edition; Stanford CS224N and CS25 | Not searched | Gap |
| Independent evidence for K2 (build-first) and K3 (evaluation-first) | Search for learning-order and evaluation-practice evidence | None |
| Human-data training curriculum with evidence of employer recognition | AI-trainer guides, certification and platform sites | None found; seller claims only |
| Hugging Face course-level update dates | Learn index and blog | Not determined |
| Current Simplilearn price | 2024–25 snapshots and an aggregator | Snapshots only |
| Non-English resources (WIDEN move) | Incidental Japanese and Chinese pages only | Gap |

## Open Questions & Risks

**Strongest objections an expert would raise.**

| Objection | Evidence for or against |
|---|---|
| The weights and role-fit scores are arbitrary. | For: role fit is judgement and the skill lists were not supplied; no numerical sensitivity run. Against: the top item per family is strong on all five criteria. |
| Cost weighting favours free material, so a good paid cohort could be undervalued. | Cost is 15 of 100. Maven AI Evals scores 75–80 before gates. Its cap comes from an unconfirmed refund-window length, not from quality. |
| Most facts rest on search extracts, vendor pages and affiliate-linked aggregators. | True: ceiling B; affiliate and vendor items are marked in the ledger. |
| Absence of Indian regulator findings is not evidence of absence. | Agreed. Orders sit in many district commissions, and I did not search state portals directly. |
| CIRR is a member-funded industry body and covers software immersives, not GenAI roles. | True; it is the only audit standard found. |
| K2 and K3 concern learning order and cannot be tested by rating resources. | Agreed. They are recorded as untested. |
| An Anthropic model rating Anthropic's own materials, and a researcher who joined Anthropic in 2026, is conflicted. | Claude Academy, Anthropic docs and Karpathy's materials are marked COI or COI-adjacent. Authority is scored 3 for the Academy and no favourable adjustment was applied. |
| Free tiers and prices move faster than a dated report. | Agreed. Compute rows carry dates and a 31–90 day recheck; AI SDK 6 became AI SDK 7 within six months. |

**Risks.** Prices moved twice in six weeks (RunPod, Lambda). The NIST RMF revision could date governance templates. Coursera's integration could change catalogue and pricing. One in-session source claims an "AI RMF 1.1" release that others contradict. The EU AI Act implementation dates are a V0-class fact: re-check before publishing governance pages.

## Discovered Concerns

- Coursera filed two restructuring notices after the Udemy merger: 2026-07-06 and a roughly 10% global workforce reduction on 2026-11-09 with an estimated US$14–17 million in costs (SEC Form 8-K) [S95] [S96]; an earlier press report of the same cut is S9. This may affect catalogue and pricing and reinforces K7's caution.
- The stored K5 wording ("AI SDK 6 changed in 2026") is itself stale: AI SDK 7 shipped on 2026-06-25 [S80]. `data/tools.json` entries for the AI SDK should name v7 and carry a V2 recheck.
- GPU rental price volatility means `data/tools.json` entries need dated prices and a 31–90 day recheck [S39] [S43].
- Karpathy joined Anthropic on 2026-05-19 [S82], which makes his materials COI-adjacent for this report and leaves Eureka Labs' LLM101n unavailable [S72]. Do not list LLM101n as an available course.
- The EU Digital Omnibus on AI (Regulation (EU) 2026/1744, in force 2026-07-27) moved the high-risk dates [S89]. Any governance learning page that quotes 2026-08-02 as the high-risk deadline needs correction.
- Vendor-awarded "Certified AI Consultant / Fractional CAIO" titles are sold on short courses [S73]. The session covering certifications should check them.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | No audited GenAI outcome data | Confirmed (with update) | [S56] [S57] [S58]: CIRR exists for general bootcamps; no GenAI-specific audit | Keep "vendor-reported" wording. Name CIRR as the audit to ask for |
| P2 | DeepLearning.AI short courses free with certificates | Contradicted | [S28] [S29]: videos free; labs and certificates need Pro | Fix tool note and price |
| P3 | Hugging Face courses free with certificates | Confirmed | [S22] [S24] | Keep as default free route |
| P4 | Free notebooks cover months 1–6; Kaggle ~30 h/week | Updated | [S26] [S83]: quota not in docs; two programmes closed; LLM API free tiers volatile | Soften K4 wording |
| P5 | Lambda H100 ~US$2.99–3.29; RunPod 4090 ~US$0.34–0.69 | Updated | [S39] [S41] [S42] | Update prices and dates |
| P6 | CS336 and Zero to Hero are the best free picks | Updated | [S59] confirms CS336 (Spring 2026). [S72] [S82]: LLM101n not shipped; Karpathy joined Anthropic | Drop LLM101n references; mark COI-adjacent |


## Sources & Evidence Ledger

All retrieval dates are 2026-11-13. "Extract" means seen as a search snippet or summary.

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | CFPB consent order, BloomTech, File 2024-CFPB-0001, https://files.consumerfinance.gov/f/documents/cfpb_bloomtech-inc-consent-order_2024-04.pdf | 2024-04-17 | 2026-11-13 | B | Extract | primary page extract; corroborated | K14, KF2 |
| S2 | Goodwin Procter, "CFPB Enters Into Consent Order With For-Profit Coding School", Mondaq, https://www.mondaq.com/unitedstates/financial-services/1456308/cfpb-enters-into-consent-order-with-for-profit-coding-school | 2024-04-25 | 2026-11-13 | B | Extract | corroborated | BloomTech terms |
| S3 | TechCrunch, CFPB fines BloomTech, https://techcrunch.com/2024/04/17/consumer-financial-protection-bureau-fines-bloomtech-for-false-claims | 2024-04-17 | 2026-11-13 | B | Extract | corroborated | ISA terms, 11,000 loans |
| S4 | CU Insight, CFPB release text, https://www.cuinsight.com/?p=62363 | 2024-04 | 2026-11-13 | B | Extract | quotes regulator | finance charge, ban |
| S5 | California BPPE OSAR, BloomTech closure notice, https://www.osar.bppe.ca.gov/closures/informational_bloom.shtml | n/d | 2026-11-13 | B | Extract | regulator page | closure 2025-12-31 |
| S6 | Saul Ewing / Law360, "CFPB's Expanding Scope Evident In Coding Bootcamp Fine", https://www.saul.com/sites/default/files/documents/2024-05/Law360%20-%20CFPB%27s%20Expanding%20Scope%20Evident%20In%20Coding%20Bootcamp%20Fine.pdf | 2024-05 | 2026-11-13 | B | Extract | | earlier ISA orders |
| S7 | Coursera Form 10-Q, period ended 2026-09-30, SEC, https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000072/cour-20260930.htm | 2026 | 2026-11-13 | B | Extract | primary filing | merger completion |
| S8 | EdTech Innovation Hub, Coursera and Udemy merger, https://www.edtechinnovationhub.com/news/coursera-and-udemy-complete-merger-but-platform-integration-still-lies-ahead | 2026-05 | 2026-11-13 | C | Extract | | pricing unchanged at closing |
| S9 | Rallies.ai, Coursera 10% workforce cut, https://rallies.ai/news/coursera-plans-to-cut-about-10-of-global-workforce-26768c50ffb0298e | 2026-11 | 2026-11-13 | C | Extract | superseded by S95 | earlier report of the cut |
| S10 | OpenAI, "OpenAI to acquire Promptfoo", https://openai.com/blog/openai-to-acquire-promptfoo | 2026-03-09 | 2026-11-13 | B | Extract | primary page extract | K5 |
| S11 | SecurityBrief UK, OpenAI buys Promptfoo, https://securitybrief.co.uk/story/openai-buys-promptfoo-to-bolster-frontier-ai-security | 2026-03-12 | 2026-11-13 | C | Extract | | open-source continuity |
| S12 | Langfuse, "Langfuse joins ClickHouse", https://langfuse.com/blog/joining-clickhouse.md | 2026-01-16 | 2026-11-13 | B | Extract | primary page extract | K5 |
| S13 | BusinessWire, ClickHouse series D and Langfuse, https://www.businesswire.com/news/home/20260116008883/en | 2026-01-16 | 2026-11-13 | B | Extract | | K5 date |
| S14 | ecorpit.com, RAG evaluation tools 2026, https://ecorpit.com/rag-evaluation-tools-ragas-deepeval-braintrust-giskard-2026/ | 2026 | 2026-11-13 | C | Extract | analysis of PyPI and GitHub | Ragas dormancy |
| S15 | testmuai.com, Ragas metrics explained, https://www.testmuai.com/learning-hub/ragas-metrics/ | 2026-10-20 | 2026-11-13 | C | Extract | corroborates S14 | Ragas release date |
| S16 | DataCamp, RAG evaluation with Ragas, https://www.datacamp.com/tutorial/rag-evaluation-with-ragas | 2026-10-19 | 2026-11-13 | C | Extract | | 0.4.3 as the Oct 2026 release |
| S17 | Vercel, "AI SDK 6", https://vercel.com/blog/ai-sdk-6 | n/d (release 2025-12-22 per S81) | 2026-11-13 | B | Extract | page date not shown | AI SDK 6 content |
| S18 | ai-sdk.dev agents docs, https://ai-sdk.dev/docs/ai-sdk-core/agents | 2026 | 2026-11-13 | B | Extract | | AI SDK docs |
| S19 | doolpa.com, AI SDK 6 (claims 2026-05-04), https://doolpa.com/news/vercel-ai-sdk-6-agents-mcp-devtools-may-4-2026 | 2026-05 | 2026-11-13 | D | Extract | contradicted by S80 and S81 | rejected release date |
| S20 | W3C community-group technical notes on WebMCP, https://w3c-cg.github.io/aikr/webMCP/webmcp-technical-notes.html | 2026 | 2026-11-13 | B | Extract | | draft status |
| S21 | mcpbundles.com, "What Is WebMCP", https://www.mcpbundles.com/guides/what-is-webmcp | 2026-10-20 | 2026-11-13 | C | Extract | | API rename |
| S22 | Hugging Face Agents Course pages (unit0, unit1, unit4), https://huggingface.co/learn/agents-course/unit0/introduction | n/d | 2026-11-13 | B | Extract | primary page extract | K9, certificate rules |
| S23 | Hugging Face blog, NLP Course becoming LLM Course, https://huggingface.co/blog/llm-course | 2025-04-03 | 2026-11-13 | B | Extract | | LLM Course dates |
| S24 | Hugging Face Learn index and Robotics Course, https://huggingface.co/learn | n/d | 2026-11-13 | B | Extract | | course list, robotics |
| S25 | spectrumailab, Hugging Face free courses ranked 2026, https://spectrumailab.com/blog/hugging-face-free-courses-ranked-2026 | 2026-07-14 | 2026-11-13 | C | Extract | | 12 courses, certificates |
| S26 | GPUPerHour, "Free Cloud GPUs in 2026: What Works and What Closed", https://gpuperhour.com/blog/free-cloud-gpus-and-credits | 2026-09-21 | 2026-11-13 | B | Read | affiliate links | free tiers, credits, rental prices |
| S27 | GPUPerHour, Google Colab alternatives, https://gpuperhour.com/blog/google-colab-alternatives | 2026 | 2026-11-13 | B | Extract | affiliate links | Colab plan prices |
| S28 | DeepLearning.AI, Agentic AI course FAQ, https://learn.deeplearning.ai/courses/agentic-ai/information | 2026 | 2026-11-13 | B | Extract | vendor page | Pro price |
| S29 | DeepLearning.AI Pro letter, https://charonhub.deeplearning.ai/p/e6dd11e3-8fb9-4564-9bd1-9791b6b304ae | n/d | 2026-11-13 | B | Extract | vendor; a draft page and a Dec 2025 third party gave other prices | videos free; paid labs |
| S30 | NVIDIA Training support, https://www.nvidia.com/en-gb/learn/training/support | n/d | 2026-11-13 | B | Extract | vendor page | DLI prices, refunds |
| S31 | NVIDIA Training FAQ, https://learn.nvidia.com/faq-content.html | n/d | 2026-11-13 | B | Extract | vendor page | workshops, certificates |
| S32 | pasqualepillitteri.it, NVIDIA DLI guide, https://pasqualepillitteri.it/en/news/25084/nvidia-ai-courses-certifications-dli-guide | 2026-10 | 2026-11-13 | C | Extract | | catalogue counts |
| S33 | DataTalksClub/llm-zoomcamp README, https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/README.md | 2026 | 2026-11-13 | B | Extract | primary page extract | cohort, certificate rules |
| S34 | beri.net LLM Zoomcamp listing; KDnuggets, 5 free zoomcamps, https://www.beri.net/learning/llm-zoomcamp | 2026-08-04 | 2026-11-13 | C | Extract | | hours; no live MLOps cohort |
| S35 | roadmap.sh changelog and home, https://roadmap.sh/changelog | 2026-09-17 | 2026-11-13 | B | Extract | self-reported usage figures | K6 |
| S36 | freeCodeCamp news article (2026-10-08) and review, https://www.freecodecamp.org/news/build-and-train-a-25m-parameter-llm-from-scratch-on-your-cpu | 2026-10-08 | 2026-11-13 | C | Extract | review is affiliate-linked | K8 |
| S37 | Modal pricing page, https://modal.com/pricing?trk=public_post-text | n/d | 2026-11-13 | B | Extract | vendor page | credit, academic grant |
| S38 | UsagePricing, Modal calculator, https://usagepricing.com/tools/pricing-calculator/modal | 2026-07 | 2026-11-13 | C | Extract | | per-second rates |
| S39 | UsagePricing, RunPod Secure Cloud repricing, https://www.usagepricing.com/blueprint/activity/runpod-2026-10-15-secure-cloud-second-hike | 2026-10-15 | 2026-11-13 | B | Extract | tracker | K16 |
| S40 | ComputePrices, RunPod RTX 4090, https://computeprices.com/providers/runpod/gpus/rtx4090 | 2026-08-04 | 2026-11-13 | B | Extract | tracker | community price |
| S41 | Orb, Lambda pricing atlas, https://www.withorb.com/pricing-atlas/lambdalabs | 2026-09-19 | 2026-11-13 | C | Extract | page capture | K17 |
| S42 | Spheron, Lambda pricing (checked 2026-10-23), https://www.spheron.network/blog/lambda-labs-pricing-2026-gpu-cost-vs-spheron/ | 2026-10-23 | 2026-11-13 | C | Extract | competitor COI | Lambda tiers |
| S43 | PricingSaaS, Lambda diff week 46, https://pricingsaas.com/companies/lambdalabs/diffs/2026W46 | 2026-11-09 | 2026-11-13 | C | Extract | single-source | Nov increase |
| S44 | LiveLaw, EduBridge Learning (CC 580/2023), https://www.livelaw.in/consumer-cases/hyderabad-district-commission-edubridge-learning-refund-fee-dissatisfied-student-262340 | 2024-07-05 | 2026-11-13 | B | Read | reputable reporting | consumer-court record |
| S45 | Business news on CCPA coaching notices (webindia123; SocialNews.XYZ), https://news.webindia123.com/news/Articles/Business/20250417/4308265.html | 2025-04-17 | 2026-11-13 | C | Extract | | CCPA coaching actions |
| S46 | LiveLaw, Delhi State Commission on FIITJEE, https://www.livelaw.in/consumer-cases/delhi-state-commission-upholds-order-against-fiitjee-student-gets-refund-310550 | 2025-11-20 | 2026-11-13 | B | Extract | | refund order |
| S47 | ASCI CCC recommendations Sept 2018, https://www.ascionline.in/wp-content/uploads/2022/09/asci_sept18_ccc_recom.pdf; afaqs March 2018 | 2018 | 2026-11-13 | B | Extract | stale | advertising findings |
| S48 | Truth in Advertising, Simplilearn, https://truthinadvertising.org/articles/simplilearn/ | ~2025-12 | 2026-11-13 | C | Extract | advocacy source | refund, complaints |
| S49 | Interview Kickstart terms (India and global), https://interviewkickstart.com/in/terms-conditions | n/d | 2026-11-13 | B | Extract | vendor page | refund terms, India prices |
| S50 | techinterview.org, Interview Kickstart entries, https://www.techinterview.org/bootcamp_directory/p/interview-kickstart-ml/ | 2026-10-08 | 2026-11-13 | C | Extract | directory | claims, price opacity |
| S51 | BBB and Trustpilot, Interview Kickstart, https://prod.bbb.org/us/ca/santa-clara/profile/training-program/interview-kickstart-1216-1641366/customer-reviews | n/d | 2026-11-13 | C | Extract | self-selected reviews | ratings |
| S52 | Scaler fee, placement and programme pages, https://www.scaler.com/topics/scaler-aiml-course-fees/ | 2026-10 | 2026-11-13 | B | Extract | vendor; outcome claims COI | price, refund, claims |
| S53 | upGrad GenAI certificate page; IIIT-B CPE admissions, https://cpe.iiitb.ac.in/admissions | n/d | 2026-11-13 | B | Extract | vendor pages | prices, refund |
| S54 | Careers360 listings (upGrad leaders programme; Great Learning), https://www.careers360.com/courses-certifications/upgrad-executive-programme-in-generative-ai-for-leaders-course | n/d | 2026-11-13 | C | Extract | aggregator | prices |
| S55 | Great Learning fee pages and listings; UT Austin McCombs online programme page, https://onlineexeced.mccombs.utexas.edu/ut-ai-programs-dom; SwitchUp, https://www.switchup.org/bootcamps/great-learning?page=4 | n/d | 2026-11-13 | B | Extract | fees conflict by variant; reviews self-selected | price range, 23-week and 12-month tracks |
| S56 | InterviewPal, how to choose a coding bootcamp 2026, https://www.interviewpal.com/blog/how-to-choose-a-coding-bootcamp-in-2026 | 2026 | 2026-11-13 | C | Extract | | CIRR membership |
| S57 | Codesmith immersive page and blog, https://codesmith.io/immersive-program | 2025-04-09 | 2026-11-13 | B | Extract | vendor; COI on outcomes | tuition, CIRR link |
| S58 | techinterview.org, Codesmith entries, https://www.techinterview.org/bootcamp_directory/p/codesmith/ | 2026-10-08 | 2026-11-13 | C | Extract | directory summary of CIRR | audited figures |
| S59 | Stanford CS336 page capture and schedule listings, https://cs336.stanford.edu/ | 2026-06-02 | 2026-11-13 | B | Extract | several consistent listings; primary site not opened | CS336 Spring 2026 |
| S60 | *AI Engineering* (Huyen), library and publisher listings, https://bookshop.org/p/books/ai-engineering-building-applications-with-foundation-models-chip-huyen/d1a4892f5eb5134f | 2025-01-07 | 2026-11-13 | B | Extract | | edition, date |
| S61 | gpu-mode/lectures, https://github.com/gpu-mode/lectures | n/d | 2026-11-13 | B | Extract | primary page extract | lecture list |
| S62 | BlueDot Impact, https://bluedot.org/llms.txt | 2026 | 2026-11-13 | B | Extract | alumni claim COI | course list |
| S63 | NIST AI RMF page; secondary summaries (docs.modulos.ai), https://www.nist.gov/itl/ai-risk-management-framework | 2026 | 2026-11-13 | B | Extract | one source conflicts | status |
| S64 | OWASP GenAI Security Project announcement, https://genai.owasp.org/announcement/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/ | 2026-09-02 | 2026-11-13 | B | Extract | primary page extract | OWASP 2026 |
| S65 | Inspect AI docs and PyPI, https://inspect.aisi.org.uk/llms-guide.txt | 2026 | 2026-11-13 | B | Extract | | Inspect |
| S66 | Maven, "AI Evals For Engineers & PMs" course page, https://maven.com/parlance-labs/evals; beri.net review, https://www.beri.net/learning/maven-ai-evals-for-engineers-and-pms | 2026-10 | 2026-11-13 | B | Extract | vendor page; COI on claims | price US$4,200, dates, refund-policy badge, 33 live sessions |
| S67 | Hamel Husain, blog post, https://hamel.dev/blog/posts/claude-auto-evals | 2026-09-30 | 2026-11-13 | B | Extract | | currency |
| S68 | Claude Academy coverage (vanja.io; pasqualepillitteri.it), https://vanja.io/claude-academy/ | 2026-08 | 2026-11-13 | C | Extract | COI (Anthropic); not checked on Anthropic's own pages | launch, rebuild |
| S69 | OpenAI Assistants API retirement notice (Zoho forum) and eesel.ai, https://help.zoho.com/portal/en/community/topic/deprecation-notice-openai-assistants-api-will-be-shut-down-on-august-26-2026 | 2025–2026-09-08 | 2026-11-13 | B | Extract | | retirement |
| S70 | LangChain and LangGraph 1.0, https://www.langchain.com/blog/langchain-langgraph-1dot0 | 2025-10 | 2026-11-13 | B | Extract | primary page extract | agent API change |
| S71 | NVIDIA Physical AI learning, https://docs.nvidia.com/learning/physical-ai/index.md | n/d | 2026-11-13 | B | Extract | vendor | embodied courses |
| S72 | Karpathy and Eureka Labs status (layer3labs.io; techi.com), https://www.layer3labs.io/guides/who-is-andrej-karpathy | 2026-10-05 | 2026-11-13 | C | Extract | COI-adjacent | LLM101n status |
| S73 | CAIO programmes (chiefaiofficer.com; Gadget Review), https://www.chiefaiofficer.com/ai-consulting-certification-2025 | 2025–2026 | 2026-11-13 | C | Extract | promotional | CAIO titles, Booth price |
| S74 | Annotation Academy; aitrainer.work Academy, https://annotation.academy/llms.txt | 2026 | 2026-11-13 | C | Extract | sellers (COI) | human-data courses |
| S75 | GPTPrompts, best AI bootcamps in the US 2026, https://gptprompts.ai/best-ai-bootcamps-in-us-2026; techinterview.org bootcamp guide, https://www.techinterview.org/post/3233477782/choose-ai-ml-bootcamp/ | 2026-05; 2026-10-17 | 2026-11-13 | C | Extract | list sites | Springboard |
| S76 | Masai and Indian ISA coverage, https://www.indianstartuptimes.com/?p=26135 | 2026-10 | 2026-11-13 | C | Extract | | ISA terms |
| S77 | Chicago Booth CAIO price, Gadget Review, https://www.gadgetreview.com/?p=404899 | n/d | 2026-11-13 | C | Extract | | price context |
| S78 | Product Compass, AI PM courses (affiliate), https://www.productcompass.pm/p/best-ai-product-management-courses | 2026-03-12 | 2026-11-13 | C | Extract | affiliate COI | Maven PM price |
| S79 | Mondaq, RBI Digital Lending Directions 2025, https://www.mondaq.com/pdf/1660150.pdf | 2025 | 2026-11-13 | C | Extract | | lender rules context |
| S80 | Vercel, AI SDK 7 launch post (changelog), https://vercel.com/changelog/ai-sdk-7 | 2026-06-25 | 2026-11-13 | B | Extract | primary page extract | AI SDK 7 date, breaking requirements |
| S81 | Refonte Learning, Vercel AI SDK and AI-native development, https://www.refontelearning.com/blog/vercel-ai-sdk-ai-native-full-stack-development; DevelopersDigest, AI SDK 7 changelog digest, https://www.developersdigest.tech/blog/vercel-ai-sdk-whats-new-2026 | 2026-08-15; 2026-10-17 | 2026-11-13 | C | Extract | secondary | AI SDK 5, 6 and 7 dates; Node.js 22+, ESM-only; 7.0.143 |
| S82 | TechCrunch, "OpenAI co-founder Andrej Karpathy joins Anthropic's pre-training team", https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/ | 2026-05-19 | 2026-11-13 | B | Extract | COI-adjacent (Anthropic is the model's developer) | Karpathy move |
| S83 | DevelopersDigest, free LLM API tiers (docs read 2026-10-18), https://www.developersdigest.tech/models/free-api; Requesty, https://www.requesty.ai/blog/free-llm-apis; GitHub wiki, https://github.com/ShaikhWarsi/free-ai-tools | 2026-04 to 2026-11 | 2026-11-13 | C | Extract | trackers; Requesty is a gateway vendor; includes Anthropic's own offer (COI-adjacent) | K4 API-tier half |
| S84 | Simplilearn programme pages (Purdue courses; city pages), https://www.simplilearn.com/certifications/purdue-courses | 2025–2026 | 2026-11-13 | B | Extract | vendor pages | prices, durations, refund wording |
| S85 | Careers360, Simplilearn PG Program in AI and ML, https://www.careers360.com/college/31233/certificate/324303 | n/d | 2026-11-13 | C | Extract | aggregator | INR price, 11 months |
| S86 | Maven help centre, "Maven's Satisfaction Guarantee", https://help.maven.com/en/articles/8705540-maven-s-satisfaction-guarantee | n/d | 2026-11-13 | B | Extract | vendor policy page | refund windows |
| S87 | techinterview.org directory entries for Maven AI cohorts and Great Learning, https://www.techinterview.org/bootcamp_directory/p/maven-ai-engineering-cohorts/; https://www.techinterview.org/bootcamp_directory/p/great-learning-ai-ml/ | 2026-10-08 | 2026-11-13 | C | Extract | directory | prices, cancellation terms |
| S88 | Voxya, Great Learning complaints, https://voxya.com/company/great-learning-complaints/1229587 | 2024-07 to 2026-04 | 2026-11-13 | C | Extract | self-reported; site sells complaint resolution (COI) | refund complaints |
| S89 | artificialintelligenceact.eu, Digital Omnibus on AI, https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/; CSA research note, https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/ | 2026-07 | 2026-11-13 | B | Extract | non-official explorer; EUR-Lex not opened | Omnibus dates |
| S90 | ARENA 9.0 call for applicants, LessWrong, https://lesswrong.com/posts/y795kpdRqC3uRmhtt/arena-9-0-call-for-applicants | 2026 | 2026-11-13 | B | Extract | alumni claims COI | ARENA curriculum and cohorts |
| S91 | UC Berkeley RDI, Agentic AI MOOC (Fall 2025), https://rdi.berkeley.edu/agentic-ai/f25 | 2025 | 2026-11-13 | B | Extract | learner count self-reported | Berkeley MOOC |
| S92 | Raschka books: O'Reilly listing, https://www.oreilly.com/library/view/-/9781633434677/; Apple Books listing, https://books.apple.com/ca/book/build-a-large-language-model-from-scratch/id6673919337 | 2024-10-29; 2026-06-30 | 2026-11-13 | B | Extract | retailer listings | editions, page counts |
| S93 | Elsevier, *Programming Massively Parallel Processors*, 5th ed., https://shop.elsevier.com/books/catalog/isbn/9780443439001 | 2026-06-03 | 2026-11-13 | B | Extract | authors NVIDIA-affiliated | PMPP 5th edition |
| S94 | MIT, Underactuated Robotics course notes, https://underactuated.mit.edu/ | 2024 | 2026-11-13 | B | Extract | | Tedrake course |
| S95 | Coursera Form 8-K, event 2026-11-09, https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000075/cour-20261109.htm | 2026-11-10 | 2026-11-13 | B | Extract | primary filing | workforce reduction |
| S96 | Coursera Form 8-K, 2026-07-06, https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000055/cour-20260706.htm | 2026-07-06 | 2026-11-13 | B | Extract | primary filing | first restructuring, merger closing |
| S97 | Wharton Online x Simplilearn, refund policy, https://sl-onlinetraining.wharton.upenn.edu/terms-conditions | n/d | 2026-11-13 | B | Extract | vendor policy page | 7-day refund rule |
| S98 | techinterview.org, Simplilearn AI/ML entry, https://www.techinterview.org/bootcamp_directory/p/simplilearn-ai-ml/ | 2026-10-08 | 2026-11-13 | C | Extract | directory | Feb 2026 price snapshot |

## Data Appendix

Records use three extension fields on `resource` beyond the table in the protocol: `last_update`, `families` and `score`. `score` is the total for the first-listed family; scores for the other families are in Section 2. Tool records carry `stage` 3 for compute and `null` elsewhere because the brief gave a stage only for compute.

```jsonl
{"type": "resource", "grade": "B", "src": ["S33", "S34"], "as_of": "2026-06-08", "ttl": "V2", "name": "DataTalks.Club LLM Zoomcamp", "provider": "DataTalks.Club", "url": "https://datatalks.club/courses/llm-zoomcamp", "kind": "free cohort course", "verdict": "use", "cost": "free", "hours": "10 wk, ~5-15 h/wk (C)", "level": "intermediate", "outcome_evidence": "none independent", "last_update": "cohort 2026-06-08", "families": ["Applied AI Engineering", "Forward Deployment & Solutions", "Evaluation, Safety & Security"], "score": 89, "note": "graded homework and peer review; certificate only via cohort"}
{"type": "resource", "grade": "D", "src": ["S69"], "as_of": "2026-08-26", "ttl": "V2", "name": "OpenAI API documentation (Responses API)", "provider": "OpenAI", "url": "https://platform.openai.com/docs", "kind": "documentation", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "continuous", "families": ["Applied AI Engineering", "Forward Deployment & Solutions", "Independent & Fractional"], "score": 84, "note": "URL recalled, not opened; Assistants API retired 2026-08-26; equivalent Anthropic (COI) and Google docs not opened"}
{"type": "resource", "grade": "B", "src": ["S22"], "as_of": "2026-11-13", "ttl": "V2", "name": "Hugging Face Agents Course", "provider": "Hugging Face", "url": "https://huggingface.co/learn/agents-course", "kind": "free course", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "none; certificate is completion-based", "last_update": null, "families": ["Applied AI Engineering", "Forward Deployment & Solutions"], "score": 83, "note": "fundamentals certificate: Unit 1 plus 80% quiz; full: use-case assignment plus GAIA subset above 30%"}
{"type": "resource", "grade": "B", "src": ["S17", "S18", "S80", "S81"], "as_of": "2026-06-25", "ttl": "V2", "name": "Vercel AI SDK documentation", "provider": "Vercel", "url": "https://ai-sdk.dev/docs/ai-sdk-core/agents", "kind": "documentation", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "AI SDK 7, 2026-06-25", "families": ["Applied AI Engineering"], "score": 83, "note": "pin 7.x; v6 code needs the v7 codemod; AI SDK 7 is ESM-only and needs Node.js 22 or later; AI SDK 6 shipped 2025-12-22"}
{"type": "resource", "grade": "B", "src": ["S23", "S25"], "as_of": "2025-04-03", "ttl": "V2", "name": "Hugging Face LLM Course", "provider": "Hugging Face", "url": "https://huggingface.co/learn/llm-course", "kind": "free course", "verdict": "use", "cost": "free", "hours": "~15-20 h (C)", "level": "intermediate", "outcome_evidence": "none; chapter certificates only", "last_update": "relaunched 2025-04-03", "families": ["ML Engineering & Applied Science", "Applied AI Engineering", "Research", "Product & Program"], "score": 88, "note": "12 chapters; fine-tuning and reasoning models"}
{"type": "resource", "grade": "B", "src": ["S28", "S29"], "as_of": "2026-11-13", "ttl": "V2", "name": "DeepLearning.AI Agentic AI (Andrew Ng)", "provider": "DeepLearning.AI", "url": "https://learn.deeplearning.ai/courses/agentic-ai/information", "kind": "course", "verdict": "use", "cost": "videos free; Pro US$25/mo annual or US$30/mo", "hours": null, "level": "intermediate", "outcome_evidence": "none; unproctored completion certificate", "last_update": "2026", "families": ["Applied AI Engineering"], "score": 80, "note": "labs, quizzes and certificate need Pro; skip the certificate"}
{"type": "resource", "grade": "C", "src": ["S66", "S86", "S87", "S78"], "as_of": "2026-10-08", "ttl": "V2", "name": "AI Evals for Engineers & PMs", "provider": "Parlance Labs on Maven (Hamel Husain, Shreya Shankar)", "url": "https://maven.com/parlance-labs/evals", "kind": "paid cohort", "verdict": "use-with-care", "cost": {"amount": 4200, "currency": "USD"}, "hours": "6 weeks, 33 live sessions (third parties say 4 weeks at 3-5 h/wk)", "level": "intermediate", "outcome_evidence": "none on jobs; 5,000+ enrolled (vendor); ratings self-collected", "last_update": "cohort 2026-10-10 to 2026-11-21, announced as the last of 2026", "families": ["Evaluation, Safety & Security", "Applied AI Engineering", "Product & Program", "Independent & Fractional"], "score": 80, "note": "refund-policy badge shown; refund through the Week 2 end date may be under 14 days from the first session (not confirmed); about US$3,000 in 2025; US$5,000 in a 2026-03 affiliate list"}
{"type": "resource", "grade": "B", "src": ["S70"], "as_of": "2025-10-22", "ttl": "V2", "name": "LangChain and LangGraph documentation (1.x)", "provider": "LangChain", "url": "https://docs.langchain.com/oss/python/releases/langgraph-v1/index.html", "kind": "documentation", "verdict": "use-with-care", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "1.0 GA 2025-10-22", "families": ["Applied AI Engineering"], "score": 74, "note": "use only 1.x material; create_react_agent deprecated"}
{"type": "resource", "grade": "C", "src": ["S68"], "as_of": "2026-08-20", "ttl": "V2", "name": "Claude Academy (formerly Anthropic Academy)", "provider": "Anthropic", "url": "https://academy.claude.com", "kind": "free courses", "verdict": "use-with-care", "cost": "free", "hours": "22-26 courses (counts differ)", "level": "beginner to intermediate", "outcome_evidence": "none; certificate described as attendance", "last_update": "renamed 2026-08-20", "families": ["Applied AI Engineering", "Forward Deployment & Solutions", "Product & Program", "Leadership & Executive"], "score": 70, "note": "COI: Anthropic is this model's developer; launched 2026-03-02; facts from third-party coverage"}
{"type": "resource", "grade": "B", "src": ["S60"], "as_of": "2025-01-07", "ttl": "V2", "name": "AI Engineering: Building Applications with Foundation Models (Chip Huyen)", "provider": "O'Reilly Media", "url": "https://bookshop.org/p/books/ai-engineering-building-applications-with-foundation-models-chip-huyen/d1a4892f5eb5134f", "kind": "book", "verdict": "use-with-care", "cost": "~US$55-80", "hours": "~25-30 h (M)", "level": "intermediate", "outcome_evidence": "none", "last_update": "1st edition 2025-01-07", "families": ["Applied AI Engineering", "Evaluation, Safety & Security", "Forward Deployment & Solutions", "Leadership & Executive"], "score": 69, "note": "strong on evaluation, RAG, finetuning, inference; tooling detail ages"}
{"type": "resource", "grade": "B", "src": ["S59"], "as_of": "2026-06-02", "ttl": "V2", "name": "Stanford CS336 Language Modeling from Scratch", "provider": "Stanford University (Hashimoto, Liang)", "url": "https://cs336.stanford.edu/", "kind": "university course", "verdict": "use", "cost": "free", "hours": "17-18 lectures + 5 assignments", "level": "advanced", "outcome_evidence": "none", "last_update": "Spring 2026 (2026-03-30 to 2026-06-03)", "families": ["Research", "ML Engineering & Applied Science", "AI Infrastructure & Platform"], "score": 97, "note": "primary site not opened; assignments include FlashAttention2 with Triton"}
{"type": "resource", "grade": "C", "src": ["S72", "S82"], "as_of": "2026-10-05", "ttl": "V2", "name": "Neural Networks: Zero to Hero (Andrej Karpathy)", "provider": "Andrej Karpathy", "url": "https://karpathy.ai/zero-to-hero.html", "kind": "lecture series", "verdict": "use", "cost": "free", "hours": "~19 h (C)", "level": "intermediate", "outcome_evidence": "none", "last_update": null, "families": ["Research", "ML Engineering & Applied Science", "Embodied & Physical AI"], "score": 83, "note": "LLM101n not shipped; Eureka Labs set aside; Karpathy joined Anthropic 2026-05-19 (COI-adjacent)"}
{"type": "resource", "grade": "C", "src": ["S24", "S25"], "as_of": "2026-11-13", "ttl": "V2", "name": "Hugging Face smol course (post-training)", "provider": "Hugging Face", "url": "https://huggingface.co/learn", "kind": "free course", "verdict": "use", "cost": "free", "hours": "~4 h/wk (C)", "level": "intermediate", "outcome_evidence": "none", "last_update": null, "families": ["ML Engineering & Applied Science", "Research"], "score": 79, "note": "listed in the Learn index; syllabus not opened"}
{"type": "resource", "grade": "B", "src": ["S61"], "as_of": "2026-11-13", "ttl": "V2", "name": "GPU MODE lectures", "provider": "GPU MODE", "url": "https://github.com/gpu-mode/lectures", "kind": "lecture series", "verdict": "use", "cost": "free", "hours": "79+ lectures", "level": "advanced", "outcome_evidence": "none", "last_update": null, "families": ["AI Infrastructure & Platform", "Research"], "score": 84, "note": "CUDA, Triton, CUTLASS, NCCL, FlashAttention, quantisation; repo created 2024-01-20"}
{"type": "resource", "grade": "B", "src": ["S61", "S93"], "as_of": "2026-06-03", "ttl": "V2", "name": "Programming Massively Parallel Processors, 5th edition", "provider": "Hwu, Kirk, El Hajj (Elsevier / Morgan Kaufmann)", "url": "https://shop.elsevier.com/books/catalog/isbn/9780443439001", "kind": "book", "verdict": "use", "cost": "about EUR 66 e-book; EUR 74 paperback", "hours": "680 pages", "level": "advanced", "outcome_evidence": "none", "last_update": "5th edition 2026-06-03", "families": ["AI Infrastructure & Platform"], "score": 89, "note": "authors NVIDIA-affiliated (COI-adjacent); named as the companion book in the GPU MODE README"}
{"type": "resource", "grade": "C", "src": ["S34"], "as_of": "2026-11-13", "ttl": "V2", "name": "DataTalks.Club MLOps Zoomcamp", "provider": "DataTalks.Club", "url": "https://github.com/DataTalksClub", "kind": "free course", "verdict": "use", "cost": "free", "hours": "self-paced", "level": "intermediate", "outcome_evidence": "none", "last_update": "no live cohort in 2026 (C)", "families": ["AI Infrastructure & Platform", "ML Engineering & Applied Science"], "score": 76, "note": "README and organisation page only"}
{"type": "resource", "grade": "C", "src": ["S33"], "as_of": "2026-11-13", "ttl": "V2", "name": "DataTalks.Club ML Zoomcamp", "provider": "DataTalks.Club", "url": "https://github.com/DataTalksClub", "kind": "free cohort course", "verdict": "use", "cost": "free", "hours": "4 months", "level": "intermediate", "outcome_evidence": "none", "last_update": null, "families": ["ML Engineering & Applied Science"], "score": 76, "note": "2026 cohort not verified"}
{"type": "resource", "grade": "B", "src": ["S30", "S31", "S32"], "as_of": "2026-10-31", "ttl": "V2", "name": "NVIDIA Deep Learning Institute courses and workshops", "provider": "NVIDIA", "url": "https://www.nvidia.com/en-us/training/instructor-led-workshops/", "kind": "paid courses", "verdict": "use-with-care", "cost": "US$30 or 90 self-paced; workshops from US$500", "hours": "per course", "level": "intermediate", "outcome_evidence": "certificate of competency after assessment; no outcome claims", "last_update": "catalogue Oct 2026", "families": ["AI Infrastructure & Platform", "Forward Deployment & Solutions"], "score": 67, "note": "vendor stack (COI-adjacent); non-refundable"}
{"type": "resource", "grade": "B", "src": ["S71"], "as_of": "2026-11-13", "ttl": "V2", "name": "NVIDIA Physical AI learning (Isaac Sim, Isaac Lab, GR00T)", "provider": "NVIDIA", "url": "https://docs.nvidia.com/learning/physical-ai/index.md", "kind": "free courses", "verdict": "use", "cost": "free", "hours": "2-20+ h per course", "level": "beginner to intermediate", "outcome_evidence": "none", "last_update": "2026", "families": ["Embodied & Physical AI"], "score": 87, "note": "Isaac Sim may need a 24 GB+ GPU (third party, C); cloud launchable offered"}
{"type": "resource", "grade": "B", "src": ["S24"], "as_of": "2026-11-13", "ttl": "V2", "name": "Hugging Face Robotics Course (LeRobot)", "provider": "Hugging Face", "url": "https://huggingface.co/learn/robotics-course", "kind": "free course", "verdict": "use-with-care", "cost": "free", "hours": "30-45 min per unit", "level": "beginner to intermediate", "outcome_evidence": "none", "last_update": "partial release", "families": ["Embodied & Physical AI"], "score": 75, "note": "gate G5: later units listed as 'coming soon' in one snapshot; completion status not verified"}
{"type": "resource", "grade": "B", "src": ["S65"], "as_of": "2026-11-13", "ttl": "V2", "name": "Inspect AI documentation", "provider": "UK AI Security Institute and Meridian Labs", "url": "https://inspect.aisi.org.uk/", "kind": "documentation", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "PyPI releases to 0.3.224", "families": ["Evaluation, Safety & Security", "Human Data & Evaluation Operations"], "score": 92, "note": "MIT licence; over 200 pre-built evals"}
{"type": "resource", "grade": "B", "src": ["S64"], "as_of": "2026-08-04", "ttl": "V2", "name": "OWASP GenAI LLM Top 10 2026 and Top 10 for Agentic Applications", "provider": "OWASP GenAI Security Project", "url": "https://genai.owasp.org/home/resources/owasp-genai-llm-top-10-2026/", "kind": "guidance", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "2026-08-03/04; Agentic Top 10 Dec 2025", "families": ["Evaluation, Safety & Security", "Governance, Risk & Assurance"], "score": 80, "note": "replaces the 2023 and 2025 editions"}
{"type": "resource", "grade": "B", "src": ["S67"], "as_of": "2026-09-30", "ttl": "V2", "name": "Hamel Husain's blog (evaluation practice)", "provider": "Hamel Husain", "url": "https://hamel.dev/", "kind": "articles", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "none", "last_update": "post 2026-09-30", "families": ["Evaluation, Safety & Security", "Product & Program", "Human Data & Evaluation Operations", "Independent & Fractional"], "score": 84, "note": "page also advertises the paid cohort (COI)"}
{"type": "resource", "grade": "B", "src": ["S63"], "as_of": "2026-11-13", "ttl": "V2", "name": "NIST AI RMF 1.0 and Generative AI Profile (AI 600-1)", "provider": "NIST", "url": "https://www.nist.gov/itl/ai-risk-management-framework", "kind": "framework", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "Jan 2023 / Jul 2024; revision in progress", "families": ["Governance, Risk & Assurance", "Evaluation, Safety & Security", "Leadership & Executive", "Independent & Fractional"], "score": 76, "note": "one source claims a 1.1 release; others contradict it"}
{"type": "resource", "grade": "B", "src": ["S62"], "as_of": "2026-11-13", "ttl": "V2", "name": "BlueDot Technical AI Safety course", "provider": "BlueDot Impact", "url": "https://bluedot.org/courses/technical-ai-safety", "kind": "free cohort course", "verdict": "use", "cost": "free", "hours": "30 h", "level": "intermediate", "outcome_evidence": "vendor alumni claim (COI)", "last_update": "2026", "families": ["Research", "Evaluation, Safety & Security"], "score": 83, "note": "2-3 h reading plus 2 h live discussion weekly"}
{"type": "resource", "grade": "B", "src": ["S62"], "as_of": "2026-11-13", "ttl": "V2", "name": "BlueDot AGI Strategy course", "provider": "BlueDot Impact", "url": "https://bluedot.org/courses/agi-strategy", "kind": "free cohort course", "verdict": "use", "cost": "free", "hours": "25 h", "level": "beginner", "outcome_evidence": "vendor alumni claim (COI)", "last_update": "2026", "families": ["Leadership & Executive", "Research", "Governance, Risk & Assurance"], "score": 78, "note": "suggested first before specialist courses"}
{"type": "resource", "grade": "B", "src": ["S62"], "as_of": "2026-11-13", "ttl": "V2", "name": "BlueDot Frontier AI Governance course", "provider": "BlueDot Impact", "url": "https://bluedot.org/courses/ai-governance", "kind": "free cohort course", "verdict": "use", "cost": "free", "hours": "25 h", "level": "intermediate", "outcome_evidence": "vendor alumni claim (COI)", "last_update": "2026", "families": ["Governance, Risk & Assurance"], "score": 78, "note": "frontier-policy focus, not enterprise compliance practice"}
{"type": "resource", "grade": "B", "src": ["S62"], "as_of": "2026-11-13", "ttl": "V2", "name": "BlueDot The Future of AI", "provider": "BlueDot Impact", "url": "https://bluedot.org/courses/future-of-ai", "kind": "free self-paced course", "verdict": "use-with-care", "cost": "free", "hours": "2 h", "level": "beginner", "outcome_evidence": "none", "last_update": "2026", "families": ["Product & Program"], "score": 65, "note": "orientation only"}
{"type": "resource", "grade": "B", "src": ["S35"], "as_of": "2026-09-17", "ttl": "V2", "name": "roadmap.sh role roadmaps (AI Engineer, AI Agents, FDE, MLOps, AI Red Teaming)", "provider": "roadmap.sh", "url": "https://roadmap.sh/ai-engineer", "kind": "checklist", "verdict": "use-with-care", "cost": "free (paid Roadmap Pro and courses exist)", "hours": null, "level": "beginner", "outcome_evidence": "none", "last_update": "site changelog 2026-09-17", "families": ["Forward Deployment & Solutions", "Evaluation, Safety & Security", "Leadership & Executive"], "score": 58, "note": "community checklist, not a curriculum; usage figures are self-reported"}
{"type": "resource", "grade": "C", "src": ["S36"], "as_of": "2026-10-08", "ttl": "V2", "name": "freeCodeCamp Machine Learning with Python certification", "provider": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn", "kind": "free course", "verdict": "use-with-care", "cost": "free", "hours": "~300 h (C)", "level": "beginner", "outcome_evidence": "none", "last_update": "2025-26 curriculum", "families": ["ML Engineering & Applied Science"], "score": 66, "note": "TensorFlow-based; five projects"}
{"type": "resource", "grade": "B", "src": ["S52"], "as_of": "2026-10-31", "ttl": "V2", "name": "Scaler AI & Machine Learning with Agentic AI", "provider": "Scaler", "url": "https://www.scaler.com/topics/scaler-aiml-course-fees/", "kind": "paid programme", "verdict": "use-with-care", "cost": {"amount": 399000, "currency": "INR"}, "hours": "~11 months (third party)", "level": "intermediate", "outcome_evidence": "vendor report: 89% placed (11,444 of 12,851, 2024-25); KPMG-commissioned; not independently audited", "last_update": "2026; FDE specialisation 2026-07-14", "families": ["Forward Deployment & Solutions"], "score": 67, "note": "14-day refund from first class; COI on outcome claims"}
{"type": "resource", "grade": "B", "src": ["S53"], "as_of": "2026-11-13", "ttl": "V2", "name": "upGrad x IIIT-B Applied AI and Agentic AI Executive Program", "provider": "upGrad / IIIT Bangalore", "url": "https://cpe.iiitb.ac.in/admissions", "kind": "paid programme", "verdict": "use-with-care", "cost": {"amount": 125000, "currency": "INR"}, "hours": null, "level": "intermediate", "outcome_evidence": "placement assistance; no placement promise (third party)", "last_update": null, "families": ["Applied AI Engineering"], "score": 61, "note": "refund before programme start on the GenAI certificate page"}
{"type": "resource", "grade": "C", "src": ["S54"], "as_of": "2026-11-13", "ttl": "V2", "name": "upGrad x IIIT-B Executive Programme in Generative AI for Leaders", "provider": "upGrad / IIIT Bangalore", "url": "https://www.careers360.com/courses-certifications/upgrad-executive-programme-in-generative-ai-for-leaders-course", "kind": "paid programme", "verdict": "use-with-care", "cost": {"amount": 225000, "currency": "INR"}, "hours": "5 months", "level": "executive", "outcome_evidence": "none found", "last_update": null, "families": ["Leadership & Executive"], "score": 58, "note": "fee incl. GST per aggregator listing"}
{"type": "resource", "grade": "C", "src": ["S54", "S55", "S47", "S87", "S88"], "as_of": "2026-10-08", "ttl": "V2", "name": "Great Learning PGP in AI and Machine Learning (UT Austin McCombs)", "provider": "Great Learning with UT Austin McCombs", "url": "https://onlineexeced.mccombs.utexas.edu/ut-ai-programs-dom", "kind": "paid programme", "verdict": "watch", "cost": {"lo": 210000, "hi": 335000, "currency": "INR"}, "hours": "23 weeks or 12 months (two tracks)", "level": "intermediate", "outcome_evidence": "no traceable data; ASCI upheld Great Lakes ad complaints in 2018; a complaints site lists 13 complaints with 5 resolved", "last_update": null, "families": ["ML Engineering & Applied Science"], "score": null, "note": "India fee plus GST; US$3,950 for the 23-week track (international listing); not scored; UT Austin cancellation terms not opened"}
{"type": "resource", "grade": "B", "src": ["S49", "S50", "S51"], "as_of": "2026-11-13", "ttl": "V2", "name": "Interview Kickstart ML and Gen AI programmes", "provider": "Interview Kickstart", "url": "https://interviewkickstart.com/in/terms-conditions", "kind": "paid cohort", "verdict": "watch", "cost": "not published; India tracks from INR 110,000+", "hours": "66 weeks (ML track, third party)", "level": "intermediate", "outcome_evidence": "unaudited vendor claims (53% salary hike, 2021 alumni)", "last_update": null, "families": ["Forward Deployment & Solutions"], "score": 37, "note": "50% refund conditional; none on listed India tracks; BBB 1/5 from 5 reviews"}
{"type": "resource", "grade": "C", "src": ["S48", "S84", "S85", "S97", "S98"], "as_of": "2026-10-08", "ttl": "V2", "name": "Simplilearn AI and ML programmes (Purdue x IBM and partner variants)", "provider": "Simplilearn", "url": "https://www.simplilearn.com/certifications/purdue-courses", "kind": "paid programme", "verdict": "watch", "cost": "US$2,499-4,800; INR 1,89,999-2,85,000 (listings conflict)", "hours": "12 weeks to 11 months", "level": "intermediate", "outcome_evidence": "vendor ranking claims; advocacy allegations; no regulator finding found", "last_update": "2025-26 snapshots", "families": ["ML Engineering & Applied Science"], "score": null, "note": "withdrawal with administration charge; Wharton-distributed programmes: 7-day refund rule; not scored"}
{"type": "resource", "grade": "C", "src": ["S57", "S58", "S56"], "as_of": "2026-10-08", "ttl": "V2", "name": "Codesmith Software Engineering + AI/ML Immersive", "provider": "Codesmith", "url": "https://codesmith.io/immersive-program", "kind": "paid bootcamp", "verdict": "use-with-care", "cost": {"amount": 22500, "currency": "USD"}, "hours": "14 wk full-time / 39 wk part-time", "level": "intermediate", "outcome_evidence": "CIRR-audited general software cohort 2023: 43.6% in-field at 180 days (directory summary); school reports 70.1% within 12 months", "last_update": "AI/ML added 2024", "families": ["Applied AI Engineering"], "score": 61, "note": "only audited example found; audit covers a pre-AI/ML cohort"}
{"type": "resource", "grade": "C", "src": ["S75"], "as_of": "2026-05-31", "ttl": "V2", "name": "Springboard Machine Learning Engineering Career Track", "provider": "Springboard", "url": "https://gptprompts.ai/best-ai-bootcamps-in-us-2026", "kind": "paid bootcamp", "verdict": "watch", "cost": {"amount": 11990, "currency": "USD"}, "hours": "~9 months", "level": "intermediate", "outcome_evidence": "tuition-back offer if not placed; terms not opened", "last_update": null, "families": ["ML Engineering & Applied Science"], "score": null, "note": "list-site source only"}
{"type": "resource", "grade": "C", "src": ["S76", "S79"], "as_of": "2026-10-31", "ttl": "V2", "name": "Masai School and Newton School ISA / pay-after-placement programmes", "provider": "Masai School; Newton School", "url": "https://www.masaischool.com/blog/are-income-share-agreements-legal", "kind": "ISA bootcamp", "verdict": "watch", "cost": {"lo": 250000, "hi": 450000, "currency": "INR"}, "hours": null, "level": "beginner", "outcome_evidence": "94% placed (vendor, unverified)", "last_update": null, "families": ["Applied AI Engineering"], "score": null, "note": "NBFC-financed; read lender terms; no Indian regulator finding found"}
{"type": "resource", "grade": "C", "src": ["S78"], "as_of": "2026-03-12", "ttl": "V2", "name": "Maven AI Product Management Certification", "provider": "Maven (Rohan Varma, Henry Shi)", "url": "https://www.productcompass.pm/p/best-ai-product-management-courses", "kind": "paid cohort", "verdict": "use-with-care", "cost": {"amount": 2500, "currency": "USD"}, "hours": null, "level": "beginner to intermediate", "outcome_evidence": "4.8 stars from 1,000+ platform reviews", "last_update": "2026", "families": ["Product & Program"], "score": 68, "note": "price from an affiliate list (COI); Maven page not opened"}
{"type": "resource", "grade": "C", "src": ["S74"], "as_of": "2026-04-21", "ttl": "V2", "name": "aitrainer.work AI Trainer Academy", "provider": "aitrainer.work", "url": "https://aitrainer.work/guides/introducing-ai-trainer-academy", "kind": "free courses", "verdict": "use-with-care", "cost": "free", "hours": "15+ h", "level": "beginner", "outcome_evidence": "none", "last_update": "2026-04-21", "families": ["Human Data & Evaluation Operations"], "score": 71, "note": "run by a job platform (COI); nine courses"}
{"type": "resource", "grade": "C", "src": ["S74"], "as_of": "2026-11-13", "ttl": "V2", "name": "Annotation Academy AI Evaluator Certification", "provider": "Annotation Academy", "url": "https://annotation.academy/ai-evaluation-certification", "kind": "paid certification", "verdict": "watch", "cost": "4 x US$62.25 instalments (about US$249, M)", "hours": "30+ h; 24 modules", "level": "beginner", "outcome_evidence": "no evidence of employer or platform recognition", "last_update": "2026", "families": ["Human Data & Evaluation Operations"], "score": 55, "note": "gate G4; seller-awarded title"}
{"type": "resource", "grade": "C", "src": ["S73"], "as_of": "2026-11-13", "ttl": "V2", "name": "Certified AI Consultant / Fractional CAIO certification (chiefaiofficer.com)", "provider": "chiefaiofficer.com", "url": "https://www.chiefaiofficer.com/ai-consulting-certification-2025", "kind": "paid certification", "verdict": "avoid", "cost": null, "hours": "3 days (consultant); 10 weeks (CAIO)", "level": "executive", "outcome_evidence": "none; title awarded by the seller", "last_update": "2025-26", "families": ["Independent & Fractional"], "score": null, "note": "gate G4; price not seen"}
{"type": "resource", "grade": "B", "src": ["S1", "S5"], "as_of": "2025-12-31", "ttl": "V6", "name": "BloomTech (formerly Lambda School) ISA bootcamp", "provider": "BloomTech", "url": "https://www.osar.bppe.ca.gov/closures/informational_bloom.shtml", "kind": "ISA bootcamp (closed)", "verdict": "avoid", "cost": null, "hours": null, "level": "beginner", "outcome_evidence": "CFPB 2024: false hiring-rate claims; ISAs were loans", "last_update": "closed 2025-12-31", "families": ["Applied AI Engineering"], "score": null, "note": "closed; CFPB order and BPPE closure notice"}
{"type": "resource", "grade": "B", "src": ["S7", "S8", "S95", "S96"], "as_of": "2026-11-09", "ttl": "V2", "name": "Coursera (including Udemy after the merger)", "provider": "Coursera, Inc.", "url": "https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000072/cour-20260930.htm", "kind": "learning platform", "verdict": "use-with-care", "cost": "varies", "hours": null, "level": "all", "outcome_evidence": "none found for any MOOC", "last_update": "merger completed 2026-05-11", "families": ["ML Engineering & Applied Science"], "score": null, "note": "integration ongoing; restructurings on 2026-07-06 and 2026-11-09 (about 10% of global workforce)"}
{"type": "resource", "grade": "C", "src": ["S73", "S77"], "as_of": "2026-11-13", "ttl": "V2", "name": "Chicago Booth Chief AI Officer programme", "provider": "University of Chicago Booth", "url": "https://www.gadgetreview.com/?p=404899", "kind": "executive programme (context only)", "verdict": "watch", "cost": {"amount": 28000, "currency": "USD"}, "hours": "10 months", "level": "executive", "outcome_evidence": "none found", "last_update": null, "families": ["Leadership & Executive"], "score": null, "note": "price context from press; not rated"}
{"type": "resource", "grade": "B", "src": ["S92"], "as_of": "2026-06-30", "ttl": "V2", "name": "Build a Reasoning Model (From Scratch) (Sebastian Raschka)", "provider": "Manning Publications", "url": "https://www.oreilly.com/library/view/-/9781633434677/", "kind": "book", "verdict": "use", "cost": "about US$60 print (retail dates vary)", "hours": "440 pages (~11 h listed)", "level": "intermediate", "outcome_evidence": "none", "last_update": "ebook 2026-06-30", "families": ["ML Engineering & Applied Science", "Research"], "score": 84, "note": "print release dates differ by retailer"}
{"type": "resource", "grade": "B", "src": ["S92"], "as_of": "2024-10-29", "ttl": "V2", "name": "Build a Large Language Model (From Scratch) (Sebastian Raschka)", "provider": "Manning Publications", "url": "https://books.apple.com/ca/book/build-a-large-language-model-from-scratch/id6673919337", "kind": "book", "verdict": "use", "cost": "CA$67.99 on one listing", "hours": "368 pages", "level": "intermediate", "outcome_evidence": "none", "last_update": "2024-10-29", "families": ["ML Engineering & Applied Science"], "score": 80, "note": "foundations; code-along"}
{"type": "resource", "grade": "B", "src": ["S90"], "as_of": "2026-10-05", "ttl": "V2", "name": "ARENA curriculum and cohorts", "provider": "ARENA (Alignment Research Engineer Accelerator)", "url": "https://lesswrong.com/posts/y795kpdRqC3uRmhtt/arena-9-0-call-for-applicants", "kind": "self-study curriculum with in-person cohorts", "verdict": "use", "cost": "free", "hours": "4-5 weeks full-time", "level": "intermediate to advanced", "outcome_evidence": "alumni claims (vendor, COI)", "last_update": "ARENA 9.0, 2026-10-05 to 2026-11-06", "families": ["Research"], "score": 80, "note": "URL is the 9.0 call for applicants; the public curriculum site was not opened"}
{"type": "resource", "grade": "B", "src": ["S91"], "as_of": "2026-11-13", "ttl": "V2", "name": "UC Berkeley Agentic AI MOOC", "provider": "UC Berkeley RDI", "url": "https://rdi.berkeley.edu/agentic-ai/f25", "kind": "free lecture series", "verdict": "use-with-care", "cost": "free", "hours": "about 12 weekly lectures of 2 h", "level": "intermediate", "outcome_evidence": "none; 32,000+ registrants (self-reported)", "last_update": "Fall 2025", "families": ["Research"], "score": 70, "note": "lectures only; no graded hands-on per a directory"}
{"type": "resource", "grade": "B", "src": ["S94"], "as_of": "2026-11-13", "ttl": "V2", "name": "Underactuated Robotics (Russ Tedrake)", "provider": "MIT", "url": "https://underactuated.mit.edu/", "kind": "open course notes and lectures", "verdict": "use", "cost": "free", "hours": "semester course", "level": "advanced", "outcome_evidence": "none", "last_update": "notes copyright 2024", "families": ["Embodied & Physical AI"], "score": 75, "note": "classical and learning-based control fundamentals; less on VLA models"}
{"type": "resource", "grade": "B", "src": ["S89"], "as_of": "2026-07-27", "ttl": "V4", "name": "EU AI Act explorer with the Digital Omnibus on AI text", "provider": "artificialintelligenceact.eu (non-profit; not the official journal)", "url": "https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/", "kind": "legal text and guide", "verdict": "use", "cost": "free", "hours": null, "level": "intermediate", "outcome_evidence": "n/a", "last_update": "Omnibus in force 2026-07-27", "families": ["Governance, Risk & Assurance", "Leadership & Executive"], "score": 76, "note": "Annex III high-risk moved to 2027-12-02 and Annex I to 2028-08-02; verify against EUR-Lex (not opened)"}
```

```jsonl
{"type": "tool", "grade": "B", "src": ["S35"], "as_of": "2026-09-17", "ttl": "V2", "id": "roadmap-sh", "name": "roadmap.sh", "stage": 3, "category": "Career planning", "what": "Community role and skill roadmaps", "verdict": "use-with-care", "why": "Currency verified, but it is a checklist, not a curriculum; paid tier and courses exist", "url": "https://roadmap.sh/ai-engineer", "status": "active", "open_source": true, "note": "stage not given in the brief for this category"}
{"type": "tool", "grade": "B", "src": ["S7", "S8", "S95", "S96"], "as_of": "2026-11-09", "ttl": "V2", "id": "coursera", "name": "Coursera (including Udemy)", "stage": 3, "category": "Learning platform", "what": "MOOC and marketplace platform", "verdict": "use-with-care", "why": "Merger completed 2026-05-11; restructurings on 2026-07-06 and 2026-11-09; no ROI evidence for any MOOC", "url": "https://www.sec.gov/Archives/edgar/data/0001651562/000165156226000072/cour-20260930.htm", "status": "merged", "note": "stage not given in the brief"}
{"type": "tool", "grade": "C", "src": ["S36"], "as_of": "2026-10-08", "ttl": "V2", "id": "freecodecamp", "name": "freeCodeCamp", "stage": 3, "category": "Learning platform", "what": "Free project and exam-based curriculum", "verdict": "use-with-care", "why": "Free and active; ML track is TensorFlow-based; no ROI evidence", "url": "https://www.freecodecamp.org/learn", "status": "active", "open_source": true, "note": "stage not given in the brief"}
{"type": "tool", "grade": "B", "src": ["S22", "S24"], "as_of": "2026-11-13", "ttl": "V2", "id": "huggingface-learn", "name": "Hugging Face Learn", "stage": 3, "category": "Learning platform", "what": "About 12 free open courses (LLM, Agents, MCP, smol, Robotics)", "verdict": "use", "why": "Free; Agents certificate needs Unit 1, an assignment and a final challenge above 30%", "url": "https://huggingface.co/learn", "status": "active", "note": "certificates are completion-based"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "kaggle", "name": "Kaggle Notebooks and Learn", "stage": 3, "category": "Learning platform", "what": "Free T4/P100-class notebooks", "verdict": "use", "why": "12 h CPU/GPU and 9 h TPU sessions; weekly GPU quota set in the account, not in docs", "url": "https://www.kaggle.com/docs/notebooks", "status": "active", "note": "quota commonly reported about 30 h"}
{"type": "tool", "grade": "B", "src": ["S28", "S29"], "as_of": "2026-11-13", "ttl": "V2", "id": "deeplearning-ai", "name": "DeepLearning.AI", "stage": 3, "category": "Learning platform", "what": "Short courses and professional certificates", "verdict": "use-with-care", "why": "Videos free; labs, quizzes and certificates need Pro at US$25/month annual or US$30 monthly", "url": "https://learn.deeplearning.ai/courses/agentic-ai/information", "status": "active", "price": "US$25-30 per month (Pro)", "note": "certificates are unproctored"}
{"type": "tool", "grade": "B", "src": ["S30", "S31", "S32"], "as_of": "2026-10-31", "ttl": "V2", "id": "nvidia-dli", "name": "NVIDIA Deep Learning Institute", "stage": 3, "category": "Learning platform", "what": "Self-paced and instructor-led GPU courses", "verdict": "use-with-care", "why": "Self-paced US$30 or 90; workshops from US$500; non-refundable; stack-specific", "url": "https://www.nvidia.com/en-gb/learn/training/support", "status": "active", "price": "US$30-90 self-paced; US$500+ workshop", "note": "2019-2021 catalogues are stale"}
{"type": "tool", "grade": "B", "src": ["S33", "S34"], "as_of": "2026-06-08", "ttl": "V2", "id": "datatalks-llm-zoomcamp", "name": "DataTalks.Club LLM Zoomcamp", "stage": 3, "category": "Learning platform", "what": "Free 10-week RAG, evaluation and agents course", "verdict": "use", "why": "2026 cohort began 2026-06-08; graded homework and peer review; certificate only in a live cohort", "url": "https://datatalks.club/courses/llm-zoomcamp", "status": "active", "price": "free", "note": "optional paid membership exists"}
{"type": "tool", "grade": "B", "src": ["S1", "S5"], "as_of": "2025-12-31", "ttl": "V6", "id": "isa-bootcamps-bloomtech", "name": "ISA bootcamps (BloomTech model)", "stage": 3, "category": "Paid bootcamp", "what": "Income-share-financed coding bootcamps", "verdict": "avoid", "why": "CFPB found ISAs were loans and hiring claims false; BloomTech closed 2025-12-31", "url": "https://www.osar.bppe.ca.gov/closures/informational_bloom.shtml", "status": "closed", "risk": "loan-like obligation with unaudited outcome claims"}
{"type": "tool", "grade": "B", "src": ["S37", "S38"], "as_of": "2026-07-31", "ttl": "V2", "id": "modal", "name": "Modal", "stage": 3, "category": "GPU compute", "what": "Serverless GPU platform billed per second", "verdict": "use", "why": "US$30/month Starter credit (about 7.6 H100-hours); T4 US$0.59/h, L4 US$0.80/h, H100 US$3.95/h; academic grants up to US$10k", "url": "https://modal.com/pricing", "status": "active", "price": "US$0 plus usage"}
{"type": "tool", "grade": "B", "src": ["S39", "S40"], "as_of": "2026-10-15", "ttl": "V2", "id": "runpod", "name": "RunPod", "stage": 3, "category": "GPU compute", "what": "Community and Secure Cloud GPU rental", "verdict": "use-with-care", "why": "Community RTX 4090 from US$0.34/h; Secure RTX 4090 US$0.89/h and H100 SXM US$3.99/h after two repricings in Sept-Oct 2026", "url": "https://www.runpod.io/pricing", "status": "active", "price": "US$0.34-3.99 per GPU-hour (listed GPUs)", "risk": "price volatility; credits programme not verified"}
{"type": "tool", "grade": "C", "src": ["S41", "S42", "S43"], "as_of": "2026-11-09", "ttl": "V2", "id": "lambda", "name": "Lambda (lambda.ai)", "stage": 3, "category": "GPU compute", "what": "On-demand GPU instances", "verdict": "use-with-care", "why": "H100 SXM US$3.99-4.29 per GPU-hour in Sept-Oct 2026; tracker shows US$4.59 in a Nov capture; no spot", "url": "https://lambda.ai/service/gpu-cloud/pricing", "status": "active", "price": "US$3.99-4.59 per H100 SXM GPU-hour", "risk": "older snapshots at US$2.99-3.29 are stale"}
{"type": "tool", "grade": "B", "src": ["S26", "S27"], "as_of": "2026-09-21", "ttl": "V2", "id": "google-colab", "name": "Google Colab", "stage": 3, "category": "GPU compute", "what": "Hosted notebooks", "verdict": "use", "why": "Free tier gives limited GPUs and sessions up to 12 h with no published quota; Pro US$9.99/month, Pro+ US$49.99/month", "url": "https://research.google.com/colaboratory/faq.html", "status": "active", "price": "free; US$9.99 or 49.99 per month"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "hf-zerogpu", "name": "Hugging Face ZeroGPU", "stage": 3, "category": "GPU compute", "what": "Shared GPU for Gradio Spaces", "verdict": "use-with-care", "why": "Free account 5 min/day; PRO US$9/month for 40 min; demos only", "url": "https://huggingface.co/docs/hub/spaces-zerogpu", "status": "active", "price": "free; US$9 per month (PRO)"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "lightning-ai", "name": "Lightning AI free plan", "stage": 3, "category": "GPU compute", "what": "Studios with persistent storage", "verdict": "watch", "why": "1 free Studio with 4-hour restarts and 50 GB; credit amount unconfirmed", "url": "https://lightning.ai/pricing", "status": "active"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-11-11", "ttl": "V1", "id": "gpu-marketplaces", "name": "Marketplace GPU rental (Vast.ai, LeaderGPU, Ori)", "stage": 3, "category": "GPU compute", "what": "Cheapest in-stock on-demand consumer and datacentre GPUs", "verdict": "use", "why": "RTX 3090 US$0.29/h; RTX 4090 US$0.41/h; L4 US$0.93/h; A100 US$0.68/h; T4 none in stock", "url": "https://gpuperhour.com/providers/vastai", "status": "active", "price": "US$0.29-0.93 per GPU-hour", "risk": "stock and prices change daily; affiliate aggregator"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "hyperscaler-trials", "name": "Hyperscaler free trials (Google Cloud, AWS, Azure)", "stage": 3, "category": "GPU compute", "what": "Sign-up credits", "verdict": "watch", "why": "Google US$300/90 days with no GPUs in the trial; AWS up to US$200/6 months on select services; Azure US$200/30 days", "url": "https://docs.cloud.google.com/free/docs/free-cloud-features", "status": "active", "price": "credits only"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "student-compute-credits", "name": "Student compute programmes (GitHub Student Developer Pack, Azure for Students)", "stage": 3, "category": "GPU compute", "what": "US$100 Azure credit; Camber 5 GPU hours; Modal academic grants", "verdict": "use-with-care", "why": "Colab Pro for Education and SageMaker Studio Lab are closed to new users", "url": "https://education.github.com/pack", "status": "changed"}
{"type": "tool", "grade": "B", "src": ["S26"], "as_of": "2026-09-21", "ttl": "V2", "id": "startup-compute-credits", "name": "Startup credit programmes (Google for Startups, AWS Activate, Microsoft, NVIDIA Inception)", "stage": 3, "category": "GPU compute", "what": "Credits up to US$150,000-350,000 by stage", "verdict": "use", "why": "Apply early if eligible; NVIDIA Inception states no amount, fee or equity", "url": "https://www.nvidia.com/en-us/startups/", "status": "active", "note": "amounts as published; eligibility varies"}
{"type": "tool", "grade": "C", "src": ["S83"], "as_of": "2026-10-18", "ttl": "V2", "id": "free-llm-api-tiers", "name": "Free LLM API tiers (Gemini API, Groq, OpenRouter, Cloudflare, Mistral, Cohere)", "stage": 3, "category": "GPU compute", "what": "Rate-limited free inference APIs used instead of renting GPUs for application work", "verdict": "use-with-care", "why": "8 of 17 providers had a standing free tier on 2026-10-18; OpenAI had none and Anthropic gave credits; limits are per model or project and change; flagship models reported as paid-only from April 2026", "url": "https://www.developersdigest.tech/models/free-api", "status": "active", "risk": "limits and model IDs disappear without notice; some free tiers may train on prompts", "note": "category chosen because the brief lists no API-credit category; Anthropic row is COI-adjacent"}
{"type": "practice", "grade": "P", "src": ["S22", "S33"], "as_of": "2026-11-13", "ttl": "V3", "area": "learning-order", "tactic": "Ship a hosted-model v0 in two weeks; learn theory when the build needs it", "claim": "K2: build toward a gate, not a syllabus (reverse only for research engineering)", "evidence": "Best-rated application resources are project-first; no controlled evidence found", "verdict": "untested"}
{"type": "practice", "grade": "P", "src": ["S33", "S65", "S66", "S67"], "as_of": "2026-11-13", "ttl": "V3", "area": "evaluation", "tactic": "Hand-write 30 evaluation cases early and build the harness before the second feature", "claim": "K3: evaluation first in every family", "evidence": "Top resources teach this; no outcome evidence", "verdict": "untested"}
{"type": "practice", "grade": "C", "src": ["S26", "S27", "S37", "S83"], "as_of": "2026-10-18", "ttl": "V2", "area": "compute", "tactic": "Use free notebooks and free LLM API tiers first; rent consumer GPUs for fine-tuning labs", "claim": "K4: months 1-6 need no GPU rental", "evidence": "Notebook quotas are opaque and two programmes closed; free API tiers are volatile and exclude flagship models", "verdict": "use-with-care", "risk": "quota or model loss mid-project"}
{"type": "practice", "grade": "B", "src": ["S69", "S70", "S64", "S80"], "as_of": "2026-11-13", "ttl": "V2", "area": "currency", "tactic": "Pin tool versions; reject fast-topic tutorials older than about 12 months or built on retired APIs", "claim": "K5: most hours on durable concepts", "evidence": "Assistants API retired; LangChain 1.0; OWASP 2026; AI SDK 6 superseded by 7 within six months", "verdict": "use"}
{"type": "practice", "grade": "B", "src": ["S1", "S49", "S52", "S86"], "as_of": "2026-11-13", "ttl": "V3", "area": "purchase-diligence", "tactic": "Before paying, get in writing the total price including lender interest, a full-refund window of 14+ days from the first session, and any outcome-claim method", "claim": "Paid programmes differ sharply on refunds and price transparency", "evidence": "Scaler states 14 days; Maven refunds through week 2 on badged courses; Interview Kickstart price unpublished and refund conditional; CFPB BloomTech findings", "verdict": "use"}
{"type": "practice", "grade": "B", "src": ["S1", "S56", "S58"], "as_of": "2026-11-13", "ttl": "V3", "area": "outcome-claims", "tactic": "Treat 'X% placed' as E unless a method, denominator and independent audit are shown", "claim": "K1: no independent GenAI outcome data", "evidence": "CIRR is the only audit standard found; three schools published", "verdict": "use"}
{"type": "practice", "grade": "C", "src": ["S44", "S79"], "as_of": "2026-11-13", "ttl": "V3", "area": "india-financing", "tactic": "Treat EMI and NBFC course finance as a loan; read lender terms and keep screenshots of sale-time claims", "claim": "Refund disputes can succeed on service-failure grounds", "evidence": "Hyderabad commission ordered a full refund in the EduBridge case; not legal advice", "verdict": "use-with-care", "risk": "loan stays payable if the course contract and loan are separate"}
{"type": "practice", "grade": "M", "src": ["S26", "S37"], "as_of": "2026-11-13", "ttl": "V2", "area": "compute-budget", "tactic": "Convert credits to GPU-hours by dividing by the hourly price at the vendor where the credit is spendable", "claim": "US$30 Modal credit buys about 7.6 H100-hours at US$3.95 per hour", "evidence": "Calculation from published rates", "verdict": "use"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Independent outcome study of a GenAI-specific course or bootcamp", "searched": "CIRR coverage; Codesmith; regulator and consumer-court searches; survey aggregators", "note": "only general-bootcamp CIRR data and the CFPB BloomTech findings"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Indian regulator or court finding against upGrad, Great Learning, Simplilearn, Scaler or Interview Kickstart", "searched": "CCPA, ASCI, district and state consumer commissions", "note": "adjacent coaching, EduBridge and 2018 ASCI records only; state portals not searched directly"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Refund detail: Great Learning UT Austin variant; exact Simplilearn administration charge for Purdue variants; Week 2 end date of the Maven AI Evals syllabus", "searched": "vendor pages, directory summaries, Maven help centre", "note": "Maven badge confirmed; window length versus first session not confirmed"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Free LLM API tier terms from the providers' own pages", "searched": "tracker and community comparisons only", "note": "one tracker says it read provider docs on 2026-10-18"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "RunPod credits programme of up to US$25K", "searched": "tracker pages and reviews", "note": "only a referral bonus of US$5-500 found"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "CS336 primary site contents (assignment details and hours)", "searched": "page capture, schedule listings and lecture listings", "note": "primary site not opened"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Modern Robotics course; MATS programme detail", "searched": "university syllabus mention; ARENA directory", "note": "not verified; MATS is a fellowship and not rated"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "ISO/IEC 42001 text; EUR-Lex text of Regulations (EU) 2024/1689 and 2026/1744", "searched": "secondary explorers and law-firm notes", "note": "official texts not opened"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Alammar's Hands-On Large Language Models; Designing Data-Intensive Applications 2nd edition; Stanford CS224N and CS25", "searched": "not searched", "note": "gap"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Independent evidence for K2 (build-first) and K3 (evaluation-first)", "searched": "learning-order and evaluation-practice searches", "note": "practice claims remain untested"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Human-data training curriculum with evidence of employer recognition", "searched": "AI-trainer guides, certification and platform sites", "note": "seller claims only"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Hugging Face course-level update dates", "searched": "Learn index and blog", "note": "not determined"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Current Simplilearn price", "searched": "2024-26 snapshots and an aggregator", "note": "snapshots only; listings conflict"}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-13", "item": "Non-English resources (WIDEN move)", "searched": "incidental Japanese and Chinese pages only", "note": "gap"}
```
