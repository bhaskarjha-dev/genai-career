---
id: "T0-55"
title: "Role Dossier: Research Scientist (AI/ML)"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-research-scientist"
tags: ["research-scientist", "role-dossier", "job-postings", "pay", "india"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and fetch. COI: Anthropic's own postings, pay data and candidate-AI guidance are in scope and are marked COI in the ledger."
evidence_window: "2025-06-25 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 14
---

# T0-55: Role Dossier: Research Scientist (AI/ML)

S-numbers refer to rows in the Sources & Evidence Ledger. Grades follow EGP-1.0: A (an employer's own page that I opened), B (platform data, or a snippet of a primary page), C (third-party analysis), D (memory or judgement), M (my calculation, inheriting the weakest input), P (practice-curated). The brief anchors the research on 2026-11-11. Every retrieval took place on 2026-11-13, which I use as the research date, so the 90-day window runs from 2026-08-15 to 2026-11-13. Access status is Read, Extract, Blocked or Gap. Posting identifiers such as JD01 refer to the order of the `jd` records in the Data Appendix.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | At frontier labs a PhD with first-author papers is a stated requirement in most Research Scientist postings. | 75% | D |
| P2 | "Research Scientist" is still the usual title for frontier-lab research roles. | 70% | D |
| P3 | Posted US base pay is roughly $250–450k at frontier labs and $150–250k at Big Tech. | 65% | D |
| P4 | India has few AI Research Scientist postings, and employers rarely post pay bands there. | 80% | D |
| P5 | Python, PyTorch and deep learning are near-universal in these postings. Data structures and algorithms are rarely named. | 60% | D |
| P6 | Labs publish little about their research loops. Coding plus a research discussion is typical. | 70% | D |

## Research Question

**Decision question.** What must the knowledge base tell a job seeker about the Research Scientist (AI/ML) role to describe it accurately? That covers the work, demand and pay, skills, proof and credentials, interviews, careers, geography and India. Each of the 14 K-claims gets a verdict.

**Sub-questions.**
1. Aliases and the boundary with Research Engineer, Member of Technical Staff and Applied Scientist.
2. Demand and trend.
3. A job-description sample.
4. Skill shares against the knowledge base's tiers.
5. Pay by region, employer type and level.
6. Loops.
7. Proof of work and credentials.
8. Entry routes.
9. Progression, durability and leverage.
10. Geography and sponsorship.
11. Résumé signals.
12. Misconceptions.
13. India.
14. Probes: PhD and publication requirements, research-taste interviews, industry against academic pay, and the measured-volume gap.

**Reading chosen.** The role is a posting that asks for original ML/AI method research. That means architectures, pre-training, RL, post-training, evaluation or alignment methods, or applied-domain ML research that also needs software engineering.
- Alias titles are included when the work matches: Member of Technical Staff (MTS), AI Scientist, Senior Researcher, ML Researcher and Applied Researcher.
- Combined Research Engineer / Research Scientist postings are included.
- Postings titled "research scientist" that are not ML method work are excluded.
- Amazon's ML research postings are titled Applied Scientist. I treat that as an adjacent role and did not count it, except one "MTS – Applied Science (New PhD)" posting that carries an RS-style brief.

**Method.** I ran 30 searches and made 19 fetch attempts. Of the fetches, 15 returned readable text, 2 were rejected as constructed URLs, 1 was blocked by bot detection (openai.com) and 1 returned only page chrome (hirist.tech). I read 13 postings in full (12 on employer boards, 1 on a mirror of the employer's text). Twelve of them feed the skill shares; the undated Mistral "AI scientist" text is left out. The other 32 sampled postings are known from snippets or mirrors.

**Exclusions (8).**
- Two People Research Scientist roles (Anthropic, OpenAI): people analytics.
- OpenAI's Learning & Cognitive Outcomes role: learning science.
- A DeepMind Philosophy and Human Values role: not ML method work.
- A Teva Clinical Research Scientist role: not AI.
- A JPMorgan internship: not a full-time role.
- Two Amazon postings, a Senior Research Scientist in AMX Research (operations research, people analytics) and a Research Scientist in AI & Customer Insights for Alexa (quantitative research).

One AI/ML posting was not counted: the JHU APL 2026 PhD Graduate role, which had expired (valid through 2026-09-20) and is limited to US citizens [S53].

**Sampling bias.** The sample was found through search engines and aggregator mirrors. This over-represents large employers, English-language postings and Greenhouse-hosted boards (DeepMind has 9 of 45 records). It under-represents Chinese, Japanese and Korean employers, Deloitte, TCS and Infosys-type consultancies, and non-indexed boards. The likely effect is towards higher pay and PhD-heavy postings.

**Falsification searches.**
- Searched for Research Scientist postings with no PhD requirement. Found 8 of 33 with visible degree wording.
- Searched for evidence that RS and RE are distinct ladders. Found convergence evidence instead.
- Searched for proof that sampled postings were open. Found expired deadlines on pages that still load.
- Searched for employer-board counts. Found none.
- Searched for employer-stated hire backgrounds. Found one DeepMind statement on an undated page.
- Cross-checked pay across posted bands, Levels.fyi, LCA aggregates and Pave.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | 30 of 45 sampled titles are a plain Research Scientist form (33 of 45 contain the phrase once the two combined RE/RS titles and Plaid's parenthetical are counted). The other 15 are Member of Technical Staff (Cohere; Amazon "MTS – Applied Science"), AI Scientist (Mistral), Senior Researcher (Microsoft), ML Researcher (ElevenLabs, Sarvam), AI Engineer & Researcher (xAI), combined RE/RS (OpenAI), "Research" (Thinking Machines), Staff MLE with Research Scientist in brackets (Plaid) and Applied Researcher (Accenture). In the Amazon postings I saw, ML research is titled Applied Scientist and "Research Scientist" is used for quantitative or operations-research roles. I searched for aliases on purpose, so these counts are not prevalence. | [S12][S14][S16][S17][S19][S21][S58][S59] | M |
| KF2 | The sample has 45 postings: 17 frontier lab, 14 Big Tech, 7 AI-native, 6 enterprise or consultancy, 1 agency. By region: US 23, Europe 12, India 9, Canada 1. Only 6 are verifiably live or dated inside the window, 16 are dated outside it and 23 are undated. Eight DeepMind Greenhouse pages in the search index carried application deadlines that had already passed. The one I fetched in full (7341608, deadline 2025-10-31) still returned complete content, so a page that loads is not proof of an open posting. | [S1][S6][S7][S11][S13][S26][S27][S29] | M/A |
| KF3 | Of 33 postings with degree wording, 19 (57.6%) require a PhD: 9 outright and 10 with an "or equivalent" or master's-plus-experience substitute. 3 prefer a PhD, 3 ask for an advanced degree and 8 (24.2%) name none. Big Tech is 10 of 10 PhD. Frontier labs are 4 of 13 PhD-or-equivalent, with 6 naming no degree (Anthropic Reward Models, DeepMind Deep Learning, OpenAI Research Scientist, xAI, Mistral ×2). DeepMind states that the majority of its research-scientist hires are post-PhD (undated page). | [S1]–[S6][S9]–[S12][S14][S16]–[S24][S55] | M/A |
| KF4 | Publications or a research track record appear in 11 of 12 fully read postings (9 in required lists). Open-source or code evidence appears in 6 of 12. xAI asks for a Google Scholar URL and a "statement of exceptional work". DeepMind asks candidates to link GitHub, side projects and open-source work, and says it looks for implementation and engineering ability as well as research. | [S1]–[S6][S9][S11][S16][S19]–[S22][S55] | M/A |
| KF5 | In the 12 fully read postings, ML is named in 12, Python in 8, PyTorch in 8, JAX in 5, deep learning in 8, research methods in 8 and large-scale training in 8. Data structures and algorithms, and creativity, are named in 0. LLM-API or tool-use skill is named in 1. JobsPipe's shares (Python 42.3%, DSA 26.0%, creativity 23.0%) come from research-scientist postings in all fields, not from AI. | [S30] plus the 12 postings | M/B |
| KF6 | The median of posted US base-range midpoints is $234k (n=18): frontier labs $329k (n=8), Big Tech $201k (n=8). Examples: OpenAI RS $250–445k, Anthropic $300–425k, DeepMind Deep Learning $174–252k, Meta FAIR $117–257k, NVIDIA $168–356.5k, Microsoft $119.8–258k. 22 of 45 postings (48.9%) show a range: 18 of 23 US and 0 of 9 India. | [S1][S2][S3][S9][S10][S11][S12][S14][S16] | A/M |
| KF7 | Total compensation at frontier labs is far above base. Levels.fyi reports an OpenAI RS US median of $1.25M (L4 $763K, L5 $1.39M) and an Anthropic median of $746K to $875K, depending on the snapshot. Pave and Nua report median new-hire equity of $4.09M (P6) and $4.72M (M6) for AI research scientists, as an intended annualised value at grant. Their 90th-percentile tail of about $45–60M is for private Bay Area firms that raised $1B–$5B or more. | [S32][S33][S47] | B |
| KF8 | Outside the US, posted pay is lower. UK bands are £60–90k (DeepL, ElevenLabs) and £120–160k (AIXI). Anthropic Zurich RE/RS is CHF 280–680k (secondary source). In India none of 9 postings states a band, and Levels.fyi lists Google RS India L3 at ₹3.05M with n not shown. | [S25][S27][S34][S52] | B/C |
| KF9 | No AI-specific posting count from employers' own boards exists in my evidence. JobsPipe (all fields, counted 2026-09-10) gives shares only: US 65.0%, DE 5.6%, UK 4.7%, SG 3.8%, IN 3.7%, remote 3.3%. Fast AI Jobs lists 333 open RS roles at 171 AI startups. OpenAI LCA filings run 28 (2023), 96 (2024), 165 (2025) and 165 (2026). | [S30][S31][S35] | B |
| KF10 | DeepMind's own page (undated, possibly older than 2025) describes four phases: recruiter chat, technical interviews (a breadth quiz plus coding), research interviews that include a talk on your research, and a culture interview, with a "relatively even split" between coding and research assessment. xAI states its stages: CV plus statement, 15-minute screen, coding, two post-training sessions and a presentation. Anthropic states that its RS Reward Models interviews are in Python and that live interviews allow no AI unless indicated. Other loop detail is candidate-reported. | [S2][S16][S39][S40][S41][S55][S56] | A/C |
| KF11 | RS, RE and MTS titles are converging at labs. Anthropic's own advice, as quoted by a practitioner, is to apply as an engineer if you have an engineering background. PhD new-graduate schemes exist at NVIDIA (L3), Meta FAIR and Amazon AGI. OpenAI runs an early-career RS/RE cohort at a $295k base. | [S42][S43][S48][S9][S11][S15][S59] | B/C |
| KF12 | Industry pays more than academia. An NBER working paper finds that AI researchers who move to industry earn 63% more than similar academic switchers. US professors average about $155k. By my arithmetic, posted industry base midpoints are about 1.5× that and frontier-lab total compensation about 5–8×. | [S45][S46] | B/M |
| KF13 | "Research Scientist" is an inflated title. Anthropic and OpenAI use "People Research Scientist" for people-analytics roles, DeepMind uses it for a philosophy role, Amazon uses it for quantitative and operations-research roles, and one Glassdoor listing pairs it with contract "Human Data LLM Research Scientist" work at $100–120 an hour. I excluded 8 postings on this basis. | [S49][S53][S59] | B/C |
| KF14 | India: 9 of 45 sampled postings, from DeepMind India, IBM Research India, GE Vernova, Sarvam, Accenture's Centre for Advanced AI and an agency client. All 9 name an advanced degree and 8 of 9 are PhD-led. No posted band was found, and employer-stated interview detail is a Gap. | [S8][S21][S22][S23][S26][S58] | M |

## Recommendation

**Decision rules**
1. **PhD finished or in the final year, with at least one first-author paper at a top venue.** Apply directly to RS, MTS or "Researcher" postings at frontier labs and Big Tech research. Prefer postings that accept a PhD or equivalent practical experience. Lead with papers and code, and prepare a talk on your research (DeepMind and xAI both include one).
   - Failure mode: the sample shows requirements, not hire rates. A PhD does not guarantee an offer.
2. **No PhD but strong research artefacts.** Target the 8 of 33 postings that name no PhD (Anthropic Reward Models, DeepMind Deep Learning, OpenAI, xAI, Mistral, Cohere, Plaid). Show reproduced results, open code and written experiments. Mistral asks for "first-author publications, open-source contributions, or impactful projects".
   - Failure mode: these postings still ask for research track records, so the artefact bar is high.
3. **Engineering background.** Apply to combined RE/RS or MTS postings first. Move to RS after research decisions you can defend.
   - Failure mode: the RE-to-RS path rests on practitioner statements (C).
4. **Domain expert** (biology, finance, energy). Use "Research Scientist, <domain>" roles. They still require ML and production software skills (Anthropic Life Sciences, Mistral Science).
   - Failure mode: few openings, and domain depth does not replace ML depth.
5. **India-based.** Look at DeepMind India, IBM Research India, Sarvam, GE Vernova and Accenture's Centre for Advanced AI. Expect PhD-led requirements and ask for the pay range early, because 0 of 9 postings state one.
   - Failure mode: India pay data is thin (grade C).
6. **Check dates.** Treat expired deadlines as closed. Do not infer that a page is open because it loads.
7. **Read pay as base or total compensation.** Posted bands are base. Levels.fyi and Pave are self-reported or vendor data weighted to equity.
8. **Interview preparation.** Practise Python live coding without AI tools, revise maths, statistics and ML breadth for a quiz-style round, and follow each employer's AI-use rule.

**What would change these rules.**
- Employer-board counts by ATS (Greenhouse, Ashby, Lever) for AI-classified RS roles.
- Hire-background data for people placed into the role.
- A fresh in-window sample with confirmed open status.

## Alternatives Considered

| Option | Verdict | Why |
|---|---|---|
| Platform shares only (JobsPipe, Fast AI Jobs) | Rejected as primary | JobsPipe covers all fields, and neither platform publishes counts for AI RS. Kept as a cross-check. |
| Only literal "Research Scientist" titles | Rejected | Misses MTS, AI Scientist and Senior Researcher postings at the labs that matter most. |
| Only postings verified inside 90 days | Rejected | Leaves n=6. All 45 kept, with window status flagged on every record. |
| Levels.fyi as the sole pay input | Rejected | Self-reported, small n, and non-English pages gave conflicting numbers. Paired with posted bands and LCA aggregates. |
| Pave equity as typical pay | Rejected | It is an intended annualised value at grant, vendor-published, and the headline tail applies to a narrow set of private firms. Reported as a range of evidence, not as a typical figure. |
| Treat Amazon "Applied Scientist" postings as RS | Rejected | Adjacent role; counting it would blur the boundary the knowledge base needs. One MTS posting with an RS-style brief is kept. |
| Add consultancies | Partly done | Accenture was sampled (2 records). No Deloitte, TCS or Infosys research-scientist postings surfaced. |

## Detailed Findings

### 1. Definition, variants and aliases

The definition holds at labs. OpenAI's posting describes the role as developing new ML techniques and advancing a team's research agenda [S14]. DeepMind's RS postings ask for publication and for leading research projects [S3][S4]. Four boundaries matter.
- **RS versus RE and MTS.** Several labs use combined or flat titles, so the line is blurred [S42][S43].
- **Domain research scientists.** Anthropic Life Sciences and Mistral Science need ML plus software engineering plus domain depth [S1][S19].
- **Applied scientist.** In the Amazon postings I saw, ML research is titled Applied Scientist (AGI) or "MTS – Applied Science". "Research Scientist" there appears on quantitative or operations-research roles [S59]. Accenture titles its applied roles "AI Applied Researcher" [S58].
- **The title in other senses.** People-analytics, philosophy and contract AI-trainer postings carry it [S49][S53].

| Alias pattern | Employers (sample) | n of 45 |
|---|---|---|
| Plain "Research Scientist" form in title (incl. Senior, AI, ML, Principal) | DeepMind, Anthropic, Meta, NVIDIA, Microsoft (Principal), OpenAI, Scale, DeepL, AIXI, JPMorgan, IBM, GE Vernova, Careernet | 30 |
| Research Engineer / Research Scientist (combined) | OpenAI | 2 |
| Member of Technical Staff (incl. "MTS – Applied Science") | Cohere, Amazon | 2 |
| AI Scientist / Lead AI Scientist | Mistral | 2 |
| Senior Researcher | Microsoft Research | 2 |
| ML Researcher / Machine Learning Researcher | ElevenLabs, Sarvam | 2 |
| AI Engineer & Researcher | xAI | 1 |
| "Research, Pre-Training Science" | Thinking Machines | 1 |
| Staff MLE (Research Scientist) | Plaid | 1 |
| Applied Researcher / Research & Innovation Lead | Accenture | 2 |

### 2. Demand

| Measure | Value | Scope and date | Source | Grade |
|---|---|---|---|---|
| Country shares | US 65.0%, DE 5.6%, UK 4.7%, SG 3.8%, IN 3.7%, FR 2.6%, CA 2.1%, NL 1.7% | All fields; JobsPipe, counted 2026-09-10; counts not published | [S30] | B |
| Remote flag, pay disclosed | 3.3%, 35.2% | Same | [S30] | B |
| Seniority label (labelled postings) | Entry 12.2%, mid 4.0%, senior 11.3%, lead or manager 4.5% | Same | [S30] | B |
| Industry mix | Software and IT 8.7%, publishing 6.8%, pharma 3.3%, scientific R&D 2.8% | Same; mostly not AI | [S30] | B |
| Open RS roles at AI startups | 333 across 171 startups; 54% Pre-Seed to Series B | Fast AI Jobs snapshot; newest listed role 2026-07-21 | [S31] | B |
| Remote ML-RS listings | 249 | Glassdoor page headed November 2026 | [S49] | C |
| OpenAI certified LCA positions, "MTS (Research Scientist)" | 188; median base filed $360,000 | ellis.com table headed 2026, aggregated 2026-08 | [S35] | B |
| OpenAI LCA filings by year | 28 (2023), 96 (2024), 165 (2025), 165 (2026) | ellis.com | [S35] | B |
| Anthropic certified H-1B LCAs | 292 (FY2025 to FY2026 Q3); about 80 in FY2026 H1 | careery.pro; Business Insider via secondary | [S37][S38] | B/C |

**Trend.** No posting-count series since 2025-01-01 was found (Absence). LCA filings are a proxy for MTS-type roles, not RS-only, and the OpenAI counts differ by cut. froghire reports 239 for FY2026 (+104%) and careery.pro reports 311 wage records (FY2025 to Q3 FY2026) [S37]. The differences come from fiscal against calendar years and quarter coverage.

**Employer mix and seniority in my sample.** Frontier labs 17, Big Tech 14, AI-native 7, enterprise or consultancy 6, agency 1. Senior, staff, principal or lead titles: 13 of 45 (28.9%). Early-career or new-graduate PhD: 4 (8.9%). Level not stated: 28 (62.2%) [M]. Remote-friendly or remote: 4 of 45 (8.9%), against JobsPipe's all-fields 3.3%.

### 3. Job-description sample (n = 45)

| Employer type | US | Europe | India | Canada | Total |
|---|---|---|---|---|---|
| Frontier lab | 8 | 5 | 3 | 1 | 17 |
| Big Tech | 11 | 1 | 2 | 0 | 14 |
| AI-native startup | 2 | 4 | 1 | 0 | 7 |
| Enterprise or consultancy | 2 | 2 | 2 | 0 | 6 |
| Agency or unnamed client | 0 | 0 | 1 | 0 | 1 |
| **Total** | **23** | **12** | **9** | **1** | **45** |

**Window status (2026-08-15 to 2026-11-13).** Six records are in-window: JD01 (board updated 2026-08-21), JD19 (posted 2026-10-30), JD22 (2026-11-05), JD34 (valid through 2026-12-01), JD35 (2026-11-02) and JD42 (2026-11-07). Sixteen are dated outside it: JD06–JD09, JD13, JD15–JD18, JD20, JD27, JD28, JD40 and JD43–JD45. They are flagged and kept as requirement-wording evidence from 2025-01-01 onwards. The other 23 are undated. They returned content on 2026-11-13, but their open status is unverified.

**Read depth.** I read 13 postings in full: JD01–JD06, JD12, JD16, JD26, JD29, JD30, JD40 and JD41. Twelve of them feed the skill shares; JD30 is left out because its text is undated. For the other 32, absence from a snippet is not absence from the posting.

**Quoting.** The brief asks for verbatim Must phrases. To stay within copyright limits, the `must` and `nice` fields in the Data Appendix are paraphrased, with at most one short verbatim phrase per source. Exact wording is at each URL.

### 4. Skills

n = 12 fully read postings (JD01–JD06, JD12, JD16, JD26, JD29, JD40, JD41). Three of the 12 are outside the window (JD06, JD16, JD40). At n=12 the interval is about ±28 pp, so shares are cross-checks. JD02 counts for Python because its posting says all interviews are in Python. Tier rule: Must ≥ 60%, Important 40–59%, Should 20–39%, Optional < 20%. Overrides are explained.

| Skill [id] | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| ML fundamentals [ml_fundamentals] | 100% (12/12) | 12 | Must | Must | Named in every posting. JobsPipe all-fields share is 39.2%. |
| Python [python] | 66.7% (8/12) | 12 | Must | Must | Named in 8. The other 4 name JAX or PyTorch instead, which implies Python. JobsPipe 42.3%. |
| PyTorch [pytorch] | 66.7% (8/12) | 12 | Must | Must | Write it as "PyTorch or JAX". JobsPipe 25.4%. |
| Deep learning and transformers [deep_learning] | 66.7% (8/12) | 12 | Must | Must | Confirmed. JobsPipe 18.6%. |
| Research methods [research_methods] | 66.7% (8/12) | 12 | Must | Must | Experiment design, ablations, full research lifecycle. |
| Novel research and publications [research_novelty] | 91.7% (11/12) | 12 | Must | Important | In the required list in 9 of 11. Promote. |
| Linear algebra [linear_algebra] | 16.7% (2/12) | 12 | Important | Must | Explicit in 2. Any maths foundation is named in 6 (50%). Demote. |
| Communication [communication] | 66.7% (8/12) | 12 | Important | Important | Cross-cutting, often preferred or boilerplate. JobsPipe 41.3%. |
| Creativity [creativity] | 0% (0/12) | 12 | Optional | Important | Not named. JobsPipe 23.0% is an all-fields figure. |
| LLM APIs and tool calling [llm_apis] | 8.3% (1/12) | 12 | Optional | Important | Only Anthropic Life Sciences. The KB pairs this tier with JobsPipe's "llm" 24.4%, which measures mention of LLMs, not API skill. |
| Data structures and algorithms [dsa] | 0% (0/12) | 12 | Should | Important | In no JD. Override to Should because coding rounds exist (xAI coding assessment; Anthropic Python interviews; DeepMind coding interview [S2][S16][S55]). JobsPipe 26.0%. |
| Scientific writing and writing [scientific_writing, writing] | 33.3% (4/12) | 12 | Should | Important | Named in 4. |
| Reinforcement learning [rl] | 25.0% (3/12) | 12 | Should | Important | 5 of 12 if RLHF and RLVR wording counts. Must on RL and post-training teams. JobsPipe 17.1%. |
| Post-training [post_training] | 41.7% (5/12) | 12 | Important | Important | Confirmed. Must on post-training teams. |
| LLM evaluation [evals] | 41.7% (5/12) | 12 | Important | Important | Confirmed. |
| Research taste [research_taste] | 16.7% (2/12) | 12 | Should | Important | Explicit in 2 of 12. Five postings in the wider sample name problem selection or taste (JD04, 23, 29, 34, 41). Interview evidence is C. |
| Statistics [statistics] | 25.0% (3/12) | 12 | Should | Important | Named in 3. |
| Behavioural c1–c4 | not testable | 12 | no evidence | Important | JDs do not state these (Absence). |
| JAX [new:jax] | 41.7% (5/12) | 12 | Important | not in card | Must at DeepMind and xAI. |
| Large-scale training [new:large_scale_training] | 66.7% (8/12) | 12 | Important | not in card | Often in preferred lists, so held at Important. |
| Open-source or code evidence [new:open_source_code] | 50.0% (6/12) | 12 | Important | not in card | Proof-of-work signal. |
| Mathematical foundations [new:mathematical_foundations] | 50.0% (6/12) | 12 | Important | not in card | Superset of linear algebra and statistics. |
| LLM research subject [new:llm_modelling] | 58.3% (7/12) | 12 | Important | not in card | Replaces the misplaced "llm" share on llm_apis. |
| TensorFlow [new:tensorflow] | 33.3% (4/12) | 12 | Optional | not in card | Only as one of "JAX, PyTorch or TensorFlow". |
| C++ or CUDA [new:cpp_cuda] | 16.7% (2/12) | 12 | Optional | not in card | JobsPipe C++ 17.4%. |
| Domain expertise [new:domain_expertise] | 25.0% (3/12) | 12 | Should | not in card | Life sciences, finance, energy. |

### 5. Pay

**Posted US base ranges** (grade A where the employer page was read; B for mirrors or snippets).

| Population | Statistic | Component | Value (USD/yr) | n | Source | Grade |
|---|---|---|---|---|---|---|
| OpenAI RS, SF (general posting) | range | base; equity extra | $250,000–$445,000 | 1 | [S14] | B |
| OpenAI RE/RS Post-Training, SF | range | base | $295,000–$555,000 | 1 | [S14] | B |
| Anthropic RS Life Sciences, SF | range | base | $300,000–$320,000 | 1 | [S1] | A |
| Anthropic Senior RS Reward Models | range | base | $340,000–$425,000 | 1 | [S2] | A |
| DeepMind RS Deep Learning, US | range | base | $174,000–$252,000 | 1 | [S3] | A |
| Meta FAIR RS (PhD) | range | base | $117,000–$173,000 | 1 | [S9] | A |
| Meta AI RS MSL FAIR Foundations | range | base | $184,000–$257,000 | 1 | [S10] | B |
| NVIDIA RS, levels L3 / L4 / L5 | range | base | $168,000–$264,500 / $192,000–$304,750 / $224,000–$356,500 | 3 | [S11] | B |
| Microsoft Senior Researcher IC4 (US typical; Bay Area and NYC) | range | base | $119,800–$234,700; $158,400–$258,000 | 2 | [S12] | B |
| xAI AI Engineer & Researcher | range | base | $180,000–$440,000 | 1 | [S16] | A |
| Thinking Machines "Research" | range | base | $350,000–$475,000 | 1 | [S18] | B |
| JPMorgan AI Research Scientist, Senior Associate, NYC | range | base | $128,250–$195,000 | 1 | [S24] | B |
| Amazon Applied Scientist, AGI, Sunnyvale (adjacent title) | range | base | $136,000–$223,400 | 1 | [S59] | B |

**Derived statistics** (M; inputs are the rows above, excluding the Amazon adjacent row).

| Population | Median of range midpoints | n |
|---|---|---|
| All US postings with a range | $234,438 | 18 |
| Frontier lab | $328,750 | 8 |
| Big Tech | $200,875 | 8 |

Some inputs fall outside the window, so read these as 2025–2026 bands.

**Elsewhere and as total compensation.**

| Population | Statistic | Component | Value | Source | Grade |
|---|---|---|---|---|---|
| UK: DeepL Senior RS Voice AI | range | base | £70,000–£90,000 | [S25] | B |
| UK: ElevenLabs ML Researcher | range | base | £60,000–£80,000 | [S25] | C |
| UK/US: AIXI Labs ML RS | range | base | £120,000–£160,000 | [S27] | B |
| Cohere MTS Multilingual | range | base | US $110,000–$370,000; Canada CAD 165,000–460,000 | [S17] | B |
| Anthropic RE/RS Pre-Training, Zurich | range | base | CHF 280,000–680,000 | [S52] | C |
| OpenAI RS, US (Levels.fyi) | p50 | total | $1.25M; L4 $763K; L5 $1.39M | [S32] | B |
| Anthropic RS, US (Levels.fyi) | p50 | total | $746,404 (snapshot 2025-12-11); $875K (other cache) | [S33] | B |
| AI RS, new-hire equity (Pave/Nua) | p50 | equity | $4.09M (P6); $4.72M (M6) | [S47] | B |
| AI RS (Pave/Nua) | p50 | base | $311,000 (P6); $340,000 (M6) | [S47] | B |
| OpenAI "MTS (Research Scientist)" LCA | p50 | base filed | $360,000 (min $178,006, max $685,000, 188 positions) | [S35] | B |
| Anthropic "MTS" LCA | p50 | base filed | $315,000 (223 positions) | [S36] | B |
| Fast AI Jobs disclosed RS salaries | p50 | posted | $216,750 (n=122; $112,320–$412,500) | [S31] | B |
| Google RS India, L3 (Levels.fyi) | p50 | total | ₹3,053,733 (updated 2026-07-20) | [S34] | B |

LCA wages are what an employer filed, not what people are paid. Levels.fyi pages in other languages returned conflicting INR figures (₹25–45M for L4–L5) that I did not use.

**Probe: industry against academic pay.**
- An NBER working paper finds that earnings rise 63% for AI researchers who move to industry, relative to similar switchers within academia [S45].
- Fortune quotes a Northwestern professor who puts average professorial salaries at $155,000 and says corporate-role PhDs can earn up to five times as much [S46].
- Dividing my numbers by that average: the $234k posted base midpoint is about 1.5×, the $746k Anthropic total about 4.8× and the $1.25M OpenAI total about 8.1× (M). The $155k average covers all CS professors, not new hires.

### 6. Interview loop

| Employer type | Track | Stages | Assesses | AI policy | Grade |
|---|---|---|---|---|---|
| Google DeepMind (frontier lab) | research | Recruiter chat; technical interviews (a breadth quiz on CS, statistics, maths and ML, plus a coding interview in a language of your choice); research interviews of about 30 minutes with researchers and leads, including a talk on your research; a culture interview | Breadth, coding and research skill, in a roughly even split between coding and research | Not stated | A for the page (undated, possibly older than 2025) [S55]; C for 2026 candidate reports of two research and two coding interviews [S56][S57] |
| xAI (frontier lab) | research | CV and statement of best work; 15-minute phone interview; coding assessment in a language of choice; 2 post-training technical sessions; a meet-the-team presentation of past work and vision; target about one week; Google Meet | Problem formulation in post-training, coding, a research talk | Not stated | A [S16] |
| Anthropic (frontier lab) | research | The posting states all interviews are in Python. Candidate reports: written responses, CodeSignal, phone screen, technical video interview, 15-minute research discussion | Python coding, research experience and thinking, mission fit | Take-homes without Claude unless indicated; live interviews no AI unless indicated; Claude allowed for preparation and for refining a self-written application | A (policy, posting); C (stages) [S2][S39][S40] |
| Anthropic RE (adjacent) | research | ML coding (attention, training loops), debugging, system design for large-model training, paper discussion, project deep dive, values round | Applied ML engineering | Same policy | C [S41] |
| Meta (Big Tech) | research | No employer-stated loop. One candidate reported a systems-research RS loop as a standard software-engineering interview. | Coding | Not stated | C [S42] |

The KB's "research talk plus coding" track fits DeepMind (a talk in the research phase), xAI (a presentation round) and Anthropic (a research discussion, per candidate reports). I found no employer-stated loops for OpenAI, Meta, NVIDIA, Microsoft, JPMorgan, Sarvam or IBM (Absence). NVIDIA and Mistral say they use AI tools in their own recruiting [S11][S19].

**Research-taste probe.** Posting language that names taste or problem choice:
- DeepMind RL asks for strong experimental taste [S4].
- Sarvam asks for strong intuition for experimental design [S21].
- AIXI asks candidates to find a worthwhile question and drive it to a concrete result with little oversight [S27].
- OpenAI asks for the ability to choose impactful problems and own a research agenda [S14].

How taste is tested is C-grade only: the research interviews at DeepMind, the research discussion at Anthropic and the vision presentation at xAI.

### 7. Proof of work

Employer text asks for:
- Peer-reviewed or first-author papers (DeepMind RL, Meta, Sarvam, OpenAI) [S4][S9][S14][S21].
- A portfolio of built software, tools or model releases (DeepMind Deep Learning) [S3].
- Reproducible open code (Meta) [S9].
- A training run you owned end to end, including what failed and how you debugged it (Sarvam) [S21].
- A Google Scholar link and a short statement of your best work (xAI) [S16].
- Work judged on the strength of your best output, not its volume (AIXI) [S27].
- GitHub, side projects or code linked from the CV, with weight on implementation and engineering ability as well as research (DeepMind's own page) [S55].

No named hiring-manager interviews were found (Absence). Practitioner guides are C-grade.

### 8. Credentials

0 of 12 fully read postings name any certification, and none appeared in the text or snippets of the other 33 (not exhaustive). The credential employers name is a PhD or equivalent practical experience (KF3). DeepMind's page says it has no specific marker for degree achievement or GPA [S55]. No employer statement on certifications for this role was found.

### 9. Entry routes and prerequisites

| Background | Evidenced route | Evidence | KB access (judgement) | View |
|---|---|---|---|---|
| PhD research | Direct RS; PhD new-grad schemes (NVIDIA L3, Meta FAIR PhD, Amazon AGI); OpenAI early-career cohort | JD12, JD18, JD19, JD45; [S15]; DeepMind says most RS hires are post-PhD [S55] | 4 | Consistent. Publications are the gate. |
| Backend engineering | RE/MTS or combined RE/RS first | Anthropic advice via [S48]; no-degree postings (JD02, JD03, JD26, JD29) | 1 | Likely 1–2 with research artefacts (D). No hire-rate data. |
| Data scientist | Applied scientist or RE; domain-RS postings | JD01, JD29, JD40, JD43 | 1.5 | Plausible (D). |
| Front-end | No evidenced route | none | 1 | Consistent (D). |
| Non-technical domain | "Research Scientist, <domain>" with ML and SWE skills | JD01, JD29 | 1 | Narrow route. |
| DevOps/SRE | ML-systems research | JD19 | not given | Adjacent only. |
| Product management | No evidence | none | not given | No route found. |
| New graduate (non-PhD) | No RS evidence | none | not given | Aim for RE or MTS. |

The one published statement on hires is DeepMind's: most of its research-scientist hires are post-PhD, and it does not over-weight publications [S55]. The page is undated, so treat it as possibly older than 2025. Otherwise published analyses of prior roles of hired people are not available (Absence). The NBER paper shows that conference publications predict moves to top firms more than to academia [S45]. K12's "not plannable" for frontier offers has no source in my evidence.

### 10. Progression, durability and leverage

- **Ladders.** Microsoft Research Sciences IC4 is Senior Researcher [S12]. NVIDIA has L3–L5 bands [S11]. OpenAI total compensation jumps from $763K (L4) to $1.39M (L5) per Levels.fyi [S32]. Anthropic posts no level names. Pave's P6 (individual contributor) and M6 (manager) show a $311k to $340k base step [S47].
- **Next roles.** Staff, principal or lead researcher (Mistral's Lead AI Scientist [S19]) and research manager. Exit evidence is thin (Absence).
- **Durability.** The evidence is mixed.
  - For: OpenAI LCA filings grew from 28 to 165 between 2023 and 2025 [S35].
  - Against: OpenAI's RSI team posting says the team builds AI systems that accelerate and eventually carry out research at the lab [S14]. RS and RE titles are converging [S42].
  - K7 stays unverifiable.
- **Leverage.** Postings describe scope. Sarvam's researcher takes architecture and training-recipe decisions on a frontier-scale run [S21]. xAI expects researchers to help drive the research agenda [S16]. Pave's $4.09M median equity suggests value capture within the population it measures [S47].

### 11. Work footprint and specialisations

Layer classification is my judgement (M) from title and description, n=45.

| Layer | n (share) | Records |
|---|---|---|
| Models and research (L2) | 27 (60.0%) | JD03, 05, 09, 10, 12–14, 16–18, 20–23, 25, 27, 28, 30, 32–34, 38, 39, 41, 42, 45 |
| Post-training and adaptation (L4) | 6 (13.3%) | JD01, 02, 04, 24, 26, 31 |
| Applied or domain research | 9 (20.0%) | JD08, 11, 29, 35–37, 40, 43, 44 |
| Evaluation, safety and assurance | 2 (4.4%) | JD06, 07 |
| ML systems research | 1 (2.2%) | JD19 |

Role-card specialisations in the sample:
- Multimodal wording (the word multimodal, or vision-language or audio-language models): 4 of 45 (8.9%) (JD12, 17, 18, 42). Including single-modality vision, video, speech or audio work: 7 (15.6%).
- Reasoning or test-time-compute wording: 3 of 45 (6.7%) (JD07, 18, 26).

### 12. Geography and sponsorship

- **Concentration.** Postings cluster in the SF Bay Area (Mountain View, Menlo Park, Santa Clara, San Francisco, Sunnyvale), Seattle and Redmond, New York, London, Paris, Dublin, Zurich, Bangalore and Montreal. JobsPipe's all-fields shares are US 65.0% and DE 5.6% [S30].
- **Remote.** 4 of 45 postings are remote-friendly or remote: Anthropic RS Reward Models, Cohere, ElevenLabs and Microsoft's Principal RS.
- **Sponsorship.** Anthropic states that it sponsors visas and retains an immigration lawyer [S1][S2]. Mistral lists visa sponsorship [S19]. Meta requires work authorisation at hire [S9]. LCA filings (A for what was filed) are in §2 and §5.

### 13. Résumé and profile signals

Reviewers' stated signals are papers (first-author, venue), open code, a Google Scholar profile, owned experiments and shipped training runs. DeepMind adds that it reads GitHub links and side projects and does not over-weight publications [S55]. Headline and keyword patterns that match postings are "PyTorch or JAX", "large-scale training", "post-training" or "RL", "evaluation" and the research area in the title (for example "Gemini Diffusion", "reward models"). Red flags are unpublished novelty claims without artefacts, and publications buried below the fold (K14). The patterns below are templates. Fill the brackets only with real work.

| Skill | Evidence-line pattern (P) |
|---|---|
| deep_learning / pytorch / jax | "Implemented [method] in [PyTorch/JAX]; trained at [scale] on [hardware]; [result] versus [named baseline]." |
| research_methods | "Designed [n] ablations on [factor]; the result changed [decision]." |
| research_novelty | "First author, [venue, year]: [one-line contribution]. [link]" |
| post_training / rl | "Trained [reward model or policy] with [method]; measured [metric] on [eval]." |
| evals | "Built [benchmark] covering [n] tasks; reported [reliability measure]." |
| communication | "Presented [work] at [venue]; wrote [blog or technical report]. [link]" |

### 14. Misconceptions and risks

| Myth or risk | Evidence |
|---|---|
| "A PhD is required." | Named as required in 19 of 33 postings with degree wording, yet 8 of 33 name none, and frontier-lab postings often accept an equivalent (KF3). DeepMind says most RS hires are post-PhD [S55], so the PhD is the norm even where it is not the stated rule. |
| "RS and RE are separate ladders." | Roles-continuum paper and Fast Company on MTS titles [S42][S43]. |
| "Levels.fyi numbers are typical pay." | Self-reported, small n and equity-heavy. Pave's figures are intended value at grant [S32][S47]. |
| "Any 'Research Scientist' posting is an AI research job." | People-analytics, philosophy, quantitative and contract AI-trainer postings carry the title [S49][S53][S59]. |
| "A live page means an open job." | 8 DeepMind pages in the index had passed their deadlines, and the one I fetched still loaded (KF2). |
| Title inflation at the entry level | JobsPipe labels 12.2% of all-fields RS postings entry level [S30]. |
| "Consultancies hire research scientists." | Accenture uses applied-researcher titles with prototyping duties [S58]. |

### 15. India

- **Volume.** JobsPipe gives India 3.7% of all-fields RS postings against US 65.0% [S30]. The sample holds 9 India postings.
- **Employers.** Google DeepMind India (JD09–JD11), IBM Research India (JD38, JD39), GE Vernova Bangalore (JD40), Sarvam (JD41), an agency client (JD42) and Accenture's Centre for Advanced AI (JD44).
- **Aliases.** "Research Scientist", "ML Researcher" (Sarvam), "Senior ML Research Scientist" (agency) and "AI Research & Innovation Lead" (Accenture).
- **Requirements.** All 9 name an advanced degree and 8 are PhD-led. Sarvam asks for 3+ years after the PhD and first-author papers at top venues. GE Vernova asks for a PhD with 2–5 years or a Master's with 5–7 years. IBM asks for a doctorate.
- **Pay.** No posted band in 9 of 9. Levels.fyi lists Google RS India L3 at ₹3.05M (updated 2026-07-20) [S34]. Vendor guides claim ₹80 LPA to ₹1.5 Cr for senior RS at top labs, with no method [S51] (C).
- **Interviews.** No India-specific loop evidence (Absence). The India aggregator I tried (Hirist) gave no loop detail.

**Notes on the KB's role scores (no verdict requested).**
- Pay 9.5 fits frontier total compensation. It overstates Big Tech base ($201k median midpoint), UK or European pay and India, where I found 0 of 9 bands.
- Demand 5 cannot be tested without an AI-specific count.
- Access "PhD 4" looks low next to Big Tech's 10 of 10 PhD requirement. This is judgement (D).

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Definition: originates methods, publishes, leads agendas in ML and LLMs | confirmed | Holds at labs; add the RS/RE/MTS blur, the domain-RS boundary and the Amazon and Accenture title boundaries [S3][S4][S14][S42][S58][S59] | B |
| K2 | Aliases: MTS–Research Scientist, AI Research Scientist, Senior RS, "Apex / Named Frontier Researcher" | updated | Add MTS, AI Scientist, Senior Researcher, ML Researcher, combined RE/RS, AI Engineer & Researcher, Applied Researcher. Amazon titles ML research Applied Scientist. "Apex" has no source [S12][S14][S16][S17][S19][S21][S25][S58][S59] | M |
| K3 | Demand: AI count unmeasured; OpenAI 68 LCA (2025); JobsPipe LLM 24.4%, RL 17.1%, US 65% (2026-11-02) | updated | Shares reproduce, but the page says counted 2026-09-10 and covers all fields. OpenAI LCA positions are 188 in the 2026 table. Fast AI Jobs lists 333 open roles [S30][S31][S35][S37] | B |
| K4 | Pay: OpenAI ~$1.25M; Anthropic $0.75–0.83M; Pave $4.09M / $4.72M | updated | OpenAI $1.25M confirmed. Anthropic $746K to $875K by snapshot. Pave figures confirmed, but vendor-published (B, not A) [S32][S33][S47] | B |
| K5 | India 3.7% vs US 65.0% (JobsPipe, all fields) | confirmed | Numbers match; scope mismatch persists; page date 2026-09-10 [S30] | B |
| K6 | India pay: no evidence | updated | Thin evidence exists (Levels.fyi Google L3 ₹3.05M; vendor guides); 0 of 9 India postings state a band [S34][S51] | C |
| K7 | Durability: judgement | unverifiable | Evidence points both ways (LCA growth; a research-automation posting; role convergence) [S14][S35][S42] | D |
| K8 | Footprint: L2 and L4 | confirmed | 60.0% and 13.3% of the sample (judgement) [S1][S2][S3] | M |
| K9 | Interview track: research talk plus coding | confirmed | DeepMind (undated) and xAI state stages that include a talk or presentation; Anthropic states Python interviews; others are candidate-reported [S2][S16][S39][S40][S55] | A/C |
| K10 | Must skills incl. Python 42.3%, PyTorch 25.4%, DL 18.6%, linear algebra | updated | AI sample: Python 66.7%, PyTorch 66.7%, DL 66.7%; linear algebra explicit 16.7% (demote) [S30] | M |
| K11 | Important skills incl. creativity, llm_apis, DSA | updated | creativity 0/12, llm_apis 1/12, DSA 0/12 (demote); research_novelty 91.7% (promote); add JAX, large-scale training, open-source code [S30] | M |
| K12 | PhD plus publications; frontier offers "not plannable" | updated | PhD required in 19 of 33 postings with degree wording, required or preferred in 22, none named in 8. DeepMind says most RS hires are post-PhD (undated page). "Not plannable" has no source [S1]–[S24][S55] | M |
| K13 | Proof of work: papers, open code, talks | confirmed | Publications 11/12; open code 6/12; DeepMind and xAI loops include a talk [S16][S21][S55] | M |
| K14 | Leave out unpublished novelty claims; do not bury the publication list | confirmed | Employers ask for first-author work and a Scholar URL; DeepMind says it does not over-weight publications. The "unpublished novelty" half is P-grade only [S16][S21][S55] | P |

## Absences

| Item | Where I looked | Note |
|---|---|---|
| AI-specific posting count from employers' own boards | JobsPipe, Fast AI Jobs, Glassdoor, ZeroG Talent | Platforms only: shares, startups-only counts, or other scopes. Board-listing URLs were refused. |
| Trend in volume since 2025-01-01 | JobsPipe, Fast AI Jobs, web search | No series. LCA filings are a proxy only. |
| Employer-stated loops for OpenAI, Meta, NVIDIA, Microsoft Research | Web search; openai.com (bot-blocked) | DeepMind (undated) and xAI found; Anthropic gave a Python statement and an AI-use policy. |
| Consultancy and IT-services RS postings beyond Accenture | One search covering Accenture, TCS, Deloitte, Capgemini and Infosys | Only Accenture applied-researcher postings surfaced. |
| India posted pay bands | 9 India postings, Levels.fyi, vendor guides | 0 of 9 state a band. |
| Published analyses of prior roles of people hired | NBER and BFI paper, roles-continuum paper, DeepMind page | Only one DeepMind statement (undated) and academia-to-industry flow data. |
| Certifications for this role | 12 full-text postings, snippets of the rest | None named. |
| Named hiring-manager statements on proof of work | Web search | Posting text, DeepMind's page and practitioner guides (C) only. |
| Behavioural skills c1–c4 in postings | 12 full-text postings | Not stated. |
| Chinese, Japanese and Korean employers' RS postings | Not sampled | Out of reach of the search method. |
| Apple, Samsung, Qualcomm, Adobe and Salesforce research postings | Not searched | Gap in Big Tech coverage. |
| "Apex / Named Frontier Researcher" alias or pay | Web search | No source. |

## Open Questions & Risks

**Open.** Programmatic board counts (Greenhouse, Ashby, Lever) for AI-classified RS roles. Hire-background data. A fresh in-window sample with confirmed open status. India pay by level. Whether DeepMind's description of its loop still holds, since the page is undated.

**Strongest objections and evidence.**

| Objection | For / against |
|---|---|
| The sample is search-index-biased and mostly out-of-window or undated. | For: only 6 of 45 are verifiably in-window. Against: the qualitative patterns (degree, publications, stack) are consistent across employers and regions. Treat volumes as unmeasured. |
| "Research Scientist" no longer names frontier research. MTS does. | For: xAI, Cohere, Amazon and LCA filings use MTS or similar titles [S16][S17][S35][S59]. Against: 30 of 45 titles are a plain RS form, including DeepMind, Meta and NVIDIA. The alias list is the fix. |
| Posted base understates pay. | For: Levels.fyi total compensation is $0.75–1.25M for OpenAI and Anthropic [S32][S33]. Against: equity values are self-reported or vendor-computed and weighted to private firms [S47]. |
| "Or equivalent" is boilerplate; hires are nearly all PhDs. | For: DeepMind says most RS hires are post-PhD [S55], and its own posting wording is a PhD or equivalent [S6]. Forum posters report the RS bar as a de facto PhD [S54] (D). Against: 8 of 33 postings name no PhD. I have no hire-rate data beyond DeepMind's statement. |
| JobsPipe shares are all-fields, so comparing them with n=12 is not like-for-like. | Agreed. n=12 has an interval of about ±28 pp; both numbers are cross-checks. |
| Interview evidence is partly candidate-reported. | For: only DeepMind, xAI and Anthropic publish any loop detail. Against: DeepMind's and xAI's stages and Anthropic's policy are employer text. |
| An undated DeepMind page may describe an older process. | For: no date on the page. Against: 2026 candidate reports describe a similar mix of research and coding interviews [S56]. |

## Discovered Concerns

- **Stale pages.** Search-based sampling returns cached or stale board pages. Eight DeepMind Greenhouse pages in the index had passed their deadlines. This affects every role dossier that samples postings this way.
- **Quoting limits.** The brief asks for verbatim Must phrases. I paraphrased and kept at most one short quotation per source, so maintainers need the URLs to check exact wording.
- **Levels.fyi language variants.** They carry inconsistent INR figures. Cite the English page only.
- **Contract "AI trainer" roles.** They use research-scientist titles ($100–120 an hour). This matters for job-board and scam guidance [S49].
- **Anthropic candidate-AI policy.** It sets different rules per stage and affects interview guidance [S39].
- **OpenAI blocks automated fetching.** Maintainers must verify OpenAI pay and requirements manually.
- **Pave's report.** It is vendor-published and its population is only partly documented, so it should not feed a general pay score.
- **JobsPipe's date.** Its page says counted 2026-09-10, which may differ from the date the KB recorded.
- **Amazon title usage.** Amazon uses Applied Scientist for ML research, so a KB that maps "research scientist" to Amazon postings will pick up non-ML roles.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | PhD with first-author papers required in most frontier-lab postings | Updated | 4 of 13 frontier postings with degree text require PhD-or-equivalent; 6 name none; Big Tech 10 of 10 | Split frontier labs from Big Tech in advice |
| P2 | "Research Scientist" is the usual title | Updated | 30 of 45 titles are a plain RS form (33 contain the phrase); the rest are MTS, AI Scientist, Senior Researcher, ML Researcher, combined RE/RS, Applied Researcher and similar | Extend the alias list |
| P3 | $250–450k frontier; $150–250k Big Tech | Confirmed | Median midpoints $329k and $201k | Keep pay split by employer type |
| P4 | India low volume, no posted pay | Confirmed | 3.7% share; 0 of 9 bands | Keep the India caveat |
| P5 | Python, PyTorch, DL near-universal; DSA rare | Confirmed | PyTorch 8/12, DL 8/12, DSA 0/12 | Demote DSA, creativity, llm_apis |
| P6 | Labs publish little about loops | Updated | DeepMind and xAI publish stages; Anthropic publishes a Python statement and an AI-use policy; others do not | Grade loops A for these three, C for the rest |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Anthropic, Research Scientist, Life Sciences (job 5239733008), Greenhouse API, https://boards-api.greenhouse.io/v1/boards/anthropic/jobs/5239733008 | 2026-06-02 (updated 2026-08-21) | 2026-11-13 | A | Read | COI, single-source | JD01, pay, sponsorship |
| S2 | Anthropic, Senior Research Scientist, Reward Models (5024835008), https://job-boards.greenhouse.io/anthropic/jobs/5024835008 | undated | 2026-11-13 | A | Read | COI | JD02, Python interviews, sponsorship |
| S3 | Google DeepMind, Research Scientist, Deep Learning (7648705), https://job-boards.greenhouse.io/deepmind/jobs/7648705 | undated | 2026-11-13 | A | Read | | JD03, pay |
| S4 | Google DeepMind, Research Scientist, Reinforcement Learning (7716037), https://job-boards.greenhouse.io/deepmind/jobs/7716037 | undated | 2026-11-13 | A | Read | | JD04 |
| S5 | Google DeepMind, Research Scientist, Gemini Diffusion (7700399), https://job-boards.greenhouse.io/deepmind/jobs/7700399 | undated | 2026-11-13 | A | Read | | JD05 |
| S6 | Google DeepMind, Research Scientist, AI safety, NYC (7341608), https://job-boards.greenhouse.io/deepmind/jobs/7341608 | deadline 2025-10-31 | 2026-11-13 | A | Read | stale | JD06 |
| S7 | Google DeepMind Greenhouse snippets (7627676, 7647558, 6890135, 7089682, 7515907, board indexes), https://job-boards.greenhouse.io/deepmind | various; deadlines 2026-01 to 2026-04 | 2026-11-13 | B | Extract | stale | JD07, JD08, JD10, stale-page finding |
| S8 | Google DeepMind India via AnitaB mirror: AQUA, AnthroKrishi, https://jobs.anitab.org/companies/google-24698/jobs/84035376-research-scientist-aqua-deepmind | 2026-06-25 | 2026-11-13 | B | Extract | mirror | JD09, JD11 |
| S9 | Meta, Fundamental AI Research Scientist, FAIR (PhD), https://metacareers.com/jobs/1088304552854840 | undated | 2026-11-13 | A | Read | | JD12, pay, work authorisation |
| S10 | Meta mirrors: Accel Consider (75351325, 81106449), The Muse Paris, https://jobs.accel.com/companies/facebook-2-07d2eb1b-d3ad-4084-93df-74a124ac9233/jobs/75351325-ai-research-scientist-msl-fair-foundations | 2026-04-18 to 2026-05-30 | 2026-11-13 | B | Extract | mirror | JD13–JD15 |
| S11 | NVIDIA via AnitaB, Zapply and Inference Jobs mirrors, https://inferencejobs.com/companies/nvidia/jobs/senior-research-scientist-fundamental-generative-ai | 2026-04-10 to 2026-10-30 | 2026-11-13 | B | Read/Extract | mirror; stale (JD16) | JD16–JD19, levels, AI in recruiting |
| S12 | Microsoft Research Senior Researcher postings via AnitaB, CareerBuilder, Dice mirrors, https://jobs.anitab.org/companies/microsoft/jobs/77547827-senior-researcher-agentic-ai-microsoft-research-ai-frontiers | 2026-05-06 | 2026-11-13 | B | Extract | mirror | JD20, JD21, IC4 band |
| S13 | Microsoft Research careers page, https://www.microsoft.com/en-us/research/careers/ | 2026-11-05 | 2026-11-13 | B | Extract | single-source | JD22 |
| S14 | OpenAI careers pages (Research Scientist; RE/RS Post-Training; RSI), https://openai.com/careers/research-scientist-san-francisco/ | undated | 2026-11-13 | B | Blocked (fetch); search extract | single-source | JD23, JD24, pay, RSI posting |
| S15 | OpenAI mirrors: Glynn Capital, Stripes, Fast AI Jobs, refer.me, https://jobs.glynncapital.com/companies/openai/jobs/71353880-research-scientist-research-engineer-early-career-cohort | 2026-02-26 to 2026-07-22 | 2026-11-13 | B | Extract | mirror | JD25, early-career cohort |
| S16 | xAI, AI Engineer & Researcher, Post-training (4374125007), https://job-boards.greenhouse.io/xai/jobs/4374125007 | undated | 2026-11-13 | A | Read | | JD26, loop, pay |
| S17 | Cohere, MTS Multilingual via ResumeGeni mirror, https://resumegeni.com/jobs/member-of-technical-staff-multilingual-at-cohere-london | 2026-06-02 | 2026-11-13 | B | Extract | mirror | JD27 |
| S18 | Thinking Machines Lab, Research, Pre-Training Science via Inference Jobs, https://inferencejobs.com/companies/thinking-machines-lab/jobs/research-pre-training-science | 2026-02-23 | 2026-11-13 | B | Extract | mirror | JD28 |
| S19 | Mistral AI, Lead AI Scientist, Finance, Lever, https://jobs.lever.co/mistral/96aff642-c48a-44ec-81d4-654d1dbc615a | undated | 2026-11-13 | A | Read | | JD29, sponsorship, AI in hiring |
| S20 | Mistral AI, AI scientist, Lever, https://jobs.lever.co/mistral/675b7f06-a76b-4144-af0c-4dd3282ef489 | undated | 2026-11-13 | A | Read | possibly older than 2025 | JD30 |
| S21 | Sarvam AI, ML Researcher, Foundational Models, https://www.sarvam.ai/careers/jobs/2dcb062d-e42b-408d-be15-59ddde900984 | undated | 2026-11-13 | A | Read | | JD41 |
| S22 | GE Vernova, Research Scientist – Machine Learning (R5022607), https://careers.gevernova.com/research-scientist-machine-learning/job/R5022607 | 2026-01-16 | 2026-11-13 | A | Read | stale | JD40 |
| S23 | IBM Research India via refresh.cv, Weekday, foundit mirrors, https://refresh.cv/jobs/ibm/ddbc05b2-dc5a-4bc4-afef-eda9965b0fd5 | undated | 2026-11-13 | B | Extract | mirror | JD38, JD39 |
| S24 | JPMorgan AI Research Scientist, Senior Associate via CareerBuilder, Dice, The Muse, https://www.careerbuilder.com/job-details/ai-research-scientist-sr-associate-new-york-ny--dc5600e4-c659-4ad5-b6f5-0cacb621b29c | undated | 2026-11-13 | B | Extract | mirror | JD36, JD37 |
| S25 | DeepL and ElevenLabs research postings via JobLeads, https://www.jobleads.com/gb/job/senior-research-scientist-voice-ai--city-of-london--e6671f8c18b92df2533288b20317eeaf6 | undated | 2026-11-13 | C | Extract | mirror | JD32, JD33, UK pay |
| S26 | Careernet client posting via Hirist, https://www.hirist.tech/j/senior-ml-research-scientist-speech-ai-1682825 | 2026-11-07 (read as DD/MM) | 2026-11-13 | C | Extract | page itself is JS-only | JD42 |
| S27 | AIXI Labs, Machine Learning Research Scientist, https://www.aixi.uk/team/opportunities/ml-research-scientist/ | 2026-07-01 | 2026-11-13 | B | Extract | single-source | JD34 |
| S28 | Scale AI, ML Research Scientist, Post-Training, https://scale.com/careers/4528009005 | undated | 2026-11-13 | B | Extract | single-source | JD31 |
| S29 | Plaid, Staff MLE (Research Scientist) via Physics Today jobs, https://jobs.physicstoday.org/job/42042931/staff-machine-learning-engineer-research-scientist-dfai/ | 2026-11-02 | 2026-11-13 | C | Extract | mirror | JD35 |
| S30 | JobsPipe, Research Scientist job description, https://jobspipe.dev/job-description/research-scientist | counted 2026-09-10 | 2026-11-13 | B | Read | single-source | Demand, platform skill shares |
| S31 | Fast AI Jobs, Research Scientist roles and salaries pages, https://www.fastaijobs.com/jobs/role/research-scientist | snapshot about 2026-07-21 | 2026-11-13 | B | Extract | single-source | Open-role count, posted pay |
| S32 | Levels.fyi, OpenAI Research Scientist (US), https://www.levels.fyi/companies/openai/salaries/software-engineer/title/research-scientist | undated | 2026-11-13 | B | Extract | self-reported | Total compensation |
| S33 | Levels.fyi, Anthropic Research Scientist (US), https://www.levels.fyi/companies/anthropic/salaries/software-engineer/title/research-scientist | 2025-12-11 | 2026-11-13 | B | Extract | self-reported, COI | Total compensation |
| S34 | Levels.fyi, Google Research Scientist (India), https://www.levels.fyi/companies/google/salaries/research-scientist | 2026-07-20 | 2026-11-13 | B | Extract | self-reported; language variants conflict | India pay |
| S35 | ellis.com, OpenAI OpCo LCA salaries and filings, https://www.ellis.com/visa-sponsors/openai-opco-llc/salaries | 2026-08 | 2026-11-13 | B | Extract | DOL data via aggregator | LCA counts and wages |
| S36 | ellis.com, Anthropic PBC H-1B salaries, https://www.ellis.com/visa-sponsors/anthropic-pbc/salaries | 2026-04 | 2026-11-13 | B | Extract | COI | LCA counts and wages |
| S37 | careery.pro and froghire LCA summaries, https://careery.pro/h1b-sponsors/anthropic-pbc | to 2026-06-23 | 2026-11-13 | B | Extract | DOL data via aggregator | LCA counts |
| S38 | Business Insider via Let's Data Science and BusinessToday, https://letsdatascience.com/news/anthropic-h-1b-filings-reveal-2026-salaries-d6bb32c6 | 2026-06-28 | 2026-11-13 | C | Extract | secondary | Anthropic H-1B volume |
| S39 | Anthropic, Guidance on Candidates' AI Usage, https://www.anthropic.com/candidate-ai-guidance, and Fortune 2025-07-21 | 2025-07-10 | 2026-11-13 | B | Extract | COI | AI policy |
| S40 | Interview Query, Anthropic AI Research Scientist interview, https://www.interviewquery.com/guides/anthropic-ai-research-scientist | undated | 2026-11-13 | C | Extract | candidate report | Loop stages |
| S41 | DataInterview, Anthropic research engineer interview, https://www.datainterview.com/blog/anthropic-research-engineer-interview | 2026-10-29 | 2026-11-13 | C | Extract | guide | RE loop |
| S42 | arXiv 2601.06087, AI Roles Continuum, https://arxiv.org/abs/2601.06087v1 | 2026-01 | 2026-11-13 | B | Extract | | RS/RE convergence |
| S43 | Fast Company, AI companies are banking on this job title, https://www.fastcompany.com/91615945/ai-companies-are-banking-on-this-job-title | undated | 2026-11-13 | B | Extract | | MTS titles |
| S44 | Analytics India Magazine, Why OpenAI calls everyone Member of Technical Staff, https://analyticsindiamag.com/global-tech/why-openai-calls-everyone-member-of-technical-staff | undated | 2026-11-13 | C | Extract | | Title context |
| S45 | NBER WP 34964 / Chicago BFI, Attention and Money Is All You Need, https://www.nber.org/system/files/working_papers/w34964.pdf | 2026-03 | 2026-11-13 | B | Extract | working paper | Industry premium |
| S46 | Fortune, AI companies court AI PhDs, https://fortune.com/2025/06/25/ai-companies-court-ai-phds-with-huge-pay-packages-raising-fears-of-an-academic-brain-drain/ | 2025-06-25 | 2026-11-13 | B | Extract | | Professor salaries |
| S47 | Pave and Nua Group, State of AI Talent (press release; summary at digidai.github.io), https://www.prnewswire.com/news-releases/new-report-from-pave-and-nua-group-ai-research-scientists-command-median-new-hire-equity-grants-above-4-million-as-the-ai-talent-market-splits-into-distinct-job-families-302857849.html | 2026-08-24 | 2026-11-13 | B | Extract | COI (vendor) | Equity, base |
| S48 | Sundeep Teki, AI Career Guides, https://www.sundeepteki.org/advice/archives/10-2026 | 2026-10 | 2026-11-13 | C | Extract | quotes Anthropic advice | Entry route |
| S49 | Glassdoor, remote ML research scientist listings, https://www.glassdoor.com/Job/remote-research-scientist-machine-learning-jobs-SRCH_IL.0,6_IS11047_KO7,42.htm | 2026-11 | 2026-11-13 | C | Extract | | Remote count, contract-role flag |
| S50 | Choppingblock salary page, https://www.choppingblock.ai/salaries/research-scientist | 2026-06-23 | 2026-11-13 | C | Extract | | Cross-check total compensation |
| S51 | India pay guides (Recrew, Futurense, Instahyre), https://www.recrew.ai/salary-guides/ai-research-engineer | 2026 | 2026-11-13 | C | Extract | no method | India pay claims |
| S52 | Lohncheck.ch, Anthropic Zurich RE/RS Pre-Training, https://lohncheck.ch/en/articles/bigtech-zurich-salaries-careers-2026 | 2026 | 2026-11-13 | C | Extract | secondary, COI | Swiss pay |
| S53 | Excluded or uncounted roles: Anthropic People RS (Greenhouse 5362838008), OpenAI People RS and Learning & Cognitive Outcomes, DeepMind Philosophy and Human Values, Teva, JPMorgan internship, JHU APL, https://www.fastaijobs.com/job/greenhouse--5362838008 | 2026 | 2026-11-13 | B | Extract | | Exclusions |
| S54 | Forum comments on DeepMind PhD requirement (EA Forum / greaterwrong), https://ea.greaterwrong.com/posts/JPqdgyjY9iNTGqjDD/are-there-any-ai-safety-labs-that-will-hire-self-taught-ml/answer/d7YeCuiyhM5sgXbHD | undated | 2026-11-13 | D | Extract | single anecdotes | Objection context |
| S55 | Google DeepMind, Applying for technical roles (blog), https://deepmind.google/discover/blog/applying-for-technical-roles/ | undated | 2026-11-13 | A | Read | possibly older than 2025; no date on page | DeepMind loop, hires, proof of work |
| S56 | Glassdoor, Google DeepMind interview reviews (Research Scientist), https://www.glassdoor.com/Interview/Google-DeepMind-Interview-E1596815-RVW30399372.htm | 2026-06 (one review dated 2026-06-09) | 2026-11-13 | C | Extract | anonymous; which review page carries the text was not recorded | 2026 loop corroboration |
| S57 | techinterview.org, Google DeepMind Interview Process 2026, https://www.techinterview.org/post/3233474918/deepmind-interview-process-2026/ | 2026-07 (per snippet) | 2026-11-13 | C | Extract | guide | DeepMind loop context |
| S58 | Accenture postings: AI Applied Researcher (ZipRecruiter Ireland), AI Research & Innovation Lead (Built In), https://www.ziprecruiter.ie/jobs/544672920-ai-applied-researcher-at-accenture | 2026-06-15; removed 2026-03-24 | 2026-11-13 | B | Extract | mirror; degree line for JD43 unconfirmed | JD43, JD44, consultancy titles |
| S59 | Amazon postings and mirrors: Applied Scientist AGI, MTS Applied Science (New PhD), Senior RS AMX Research, RS Alexa customer insights, https://amazon.jobs/en/jobs/2912776/member-of-technical-staff-applied-science-new-phd-agi-autonomy | 2025-12 to 2026-05 | 2026-11-13 | B | Extract | mirror dates | JD45, Amazon title boundary, adjacent pay |

## Data Appendix

Record notes: `must` and `nice` are paraphrased from each posting, with at most one short verbatim phrase per source in single quotation marks. Exact wording is at each URL. In `jd` records, `note` starts with the posting identifier used in the report (JD01 to JD45).

```jsonl
{"type":"jd","grade":"A","src":["S1"],"as_of":"2026-08-21","ttl":"V1","role":"role:research-scientist","employer":"Anthropic","title":"Research Scientist, Life Sciences","url":"https://job-boards.greenhouse.io/anthropic/jobs/5239733008","job_id":"5239733008","seen":"2026-11-13","location":"San Francisco, CA, US","remote":"on-site (offices at least 25% of the time)","seniority":"not stated (level set internally)","years":null,"degree":"Bachelor's or equivalent minimum; PhD preferred, with equivalent industry experience accepted","must":["Software engineering strength in Python ('production-quality Python')","Hands-on training or fine-tuning of ML models, including LLMs, protein language models or other deep learning architectures","Experience applying ML and software engineering to biological problems"],"nice":["LLM post-training experience (RLHF, RL from verifiable rewards, SFT data curation, eval-driven development)","Published ML-for-biology research or open-source computational-biology tools"],"pay":{"lo":300000,"hi":320000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD01; first_published 2026-06-02 and updated 2026-08-21 per board API; live at retrieval; domain variant (AI for biology) kept because the work is post-training, evals and RL environments; read in full; COI (Anthropic)"}
{"type":"jd","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Anthropic","title":"Senior Research Scientist, Reward Models","url":"https://job-boards.greenhouse.io/anthropic/jobs/5024835008","job_id":"5024835008","seen":"2026-11-13","location":"Remote-Friendly (Travel Required) | San Francisco, CA, US","remote":"remote-friendly with travel; offices at least 25% of the time","seniority":"Senior","years":null,"degree":"Bachelor's degree in a related field or equivalent experience","must":["Track record of research contributions in reward modelling, RLHF or closely related ML areas","Experience training and evaluating reward models for LLMs","Comfort designing and running large-scale experiments with substantial compute"],"nice":["Published research on reward modelling, preference learning or RLHF","LLM-as-judge experience, including calibration and reliability","Constitutional AI, debate or scalable-oversight experience"],"pay":{"lo":340000,"hi":425000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD02; undated page; the posting says 'we conduct all interviews in Python'; visa sponsorship offered; read in full; COI (Anthropic)"}
{"type":"jd","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, Deep Learning","url":"https://job-boards.greenhouse.io/deepmind/jobs/7648705","job_id":"7648705","seen":"2026-11-13","location":"Mountain View, CA, US; San Francisco, CA, US","remote":"on-site (Mountain View or San Francisco)","seniority":"not stated (technical leadership and mentoring expected)","years":null,"degree":"Bachelor's or Master's in CS, mathematics or a related field, or equivalent practical experience","must":["Extensive experience with JAX, PyTorch or TensorFlow","Expert grasp of ML basics: optimisation, linear algebra, statistical learning theory","Track record of 'leading research projects from ideation to deployment or publication'","Evidence of building significant software, tools or models, for example open-source contributions"],"nice":["Large-scale distributed training and performance profiling experience","Strong communication with internal stakeholders and the wider research community"],"pay":{"lo":174000,"hi":252000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD03; base only, bonus, equity and benefits extra; carries a 'New' tag with no date or deadline; read in full"}
{"type":"jd","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, Reinforcement Learning","url":"https://job-boards.greenhouse.io/deepmind/jobs/7716037","job_id":"7716037","seen":"2026-11-13","location":"London, UK","remote":null,"seniority":"not stated","years":null,"degree":"PhD in ML preferred, with equivalent practical experience accepted","must":["Research track record in RL, including peer-reviewed publications","Strong implementation ability in research codebases","Ownership of experiments end to end, including analysis and interpretation","Strong communication and honesty about results"],"nice":["RL for sequence models, post-training, preference-based learning or agentic systems","Modern research stacks (JAX/Flax or PyTorch) and scaling experiments","'Strong experimental taste': judgement on baselines, ablations and what is worth testing"],"pay":null,"ats":"Greenhouse","note":"JD04; no pay band on the UK posting; undated; read in full"}
{"type":"jd","grade":"A","src":["S5"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, Gemini Diffusion","url":"https://job-boards.greenhouse.io/deepmind/jobs/7700399","job_id":"7700399","seen":"2026-11-13","location":"London, UK","remote":null,"seniority":"not stated","years":null,"degree":"Advanced degree in CS, EE, science or mathematics, or equivalent experience","must":["Academic ML research experience, publications, or research in related fields","Experience with some of LLMs, Transformers, diffusion and text-diffusion models, and 'Large-scale distributed training'","Python-based scientific programming (NumPy, SciPy, JAX, PyTorch or TensorFlow)","Maths and statistics depth to follow research papers (linear algebra, calculus)"],"nice":["Track record of building software, in open source, products or research","C++ or broader programming experience"],"pay":null,"ats":"Greenhouse","note":"JD05; undated; carries a 'New' tag; read in full"}
{"type":"jd","grade":"A","src":["S6"],"as_of":"2025-10-31","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist (AI safety, alignment, interpretability)","url":"https://job-boards.greenhouse.io/deepmind/jobs/7341608","job_id":"7341608","seen":"2026-11-13","location":"New York City, NY, US","remote":null,"seniority":"not stated","years":null,"degree":"PhD in CS, ML or a related technical field, 'or equivalent practical experience'","must":["Designing and implementing ML algorithms in Python","Hands-on experience with a major deep learning framework (JAX, PyTorch or TensorFlow)","Strong mathematical background and ability to engage with theoretical ML research"],"nice":["Publications at top venues (NeurIPS, ICML, ICLR)","Expertise in AI safety, interpretability or alignment"],"pay":{"lo":166000,"hi":244000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD06; STALE: page states an application deadline of 2025-10-31 yet still loads; kept as requirement-wording evidence; read in full"}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-03-02","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, Autonomous Agents","url":"https://job-boards.greenhouse.io/deepmind/jobs/7627676","job_id":"7627676","seen":"2026-11-13","location":"London, UK","remote":null,"seniority":"not stated","years":null,"degree":null,"must":["Curiosity about or experience with research on personalisation, memory, reasoning, self-improvement and safety for agents"],"nice":[],"pay":null,"ats":"Greenhouse","note":"JD07; STALE: closing date 2026-03-02 in the snippet; snippet only"}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-03-07","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, AI-powered Scientific Discovery","url":"https://job-boards.greenhouse.io/deepmind/jobs/7647558","job_id":"7647558","seen":"2026-11-13","location":"Montreal, Canada","remote":null,"seniority":"not stated","years":null,"degree":null,"must":["Experience with LLMs, preferably for code synthesis","Experience with an ML framework such as JAX, TensorFlow or PyTorch"],"nice":[],"pay":null,"ats":"Greenhouse","note":"JD08; the date 2026-03-07 is a mirror index date, outside window; snippet only"}
{"type":"jd","grade":"B","src":["S8"],"as_of":"2026-06-25","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, AQUA, DeepMind","url":"https://jobs.anitab.org/companies/google-24698/jobs/84035376-research-scientist-aqua-deepmind","job_id":"84035376","seen":"2026-11-13","location":"Bengaluru, India","remote":null,"seniority":"not stated","years":"2 years with ML frameworks","degree":"PhD in CS, AI or a related field, or equivalent practical experience","must":["2 years of experience with ML frameworks (JAX, TensorFlow or PyTorch)","Experience with advanced deep learning and reinforcement learning","Publication record at ML conferences or journals (NeurIPS, ICML, ICLR, KDD, AAAI)"],"nice":[],"pay":null,"ats":"Google careers (via mirror)","note":"JD09; mirror of Google careers text; posted 2026-06-25, outside window; job_id is the mirror's ID"}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, Machine Learning Optimization","url":"https://job-boards.greenhouse.io/deepmind/jobs/6890135","job_id":"6890135","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"not stated","years":null,"degree":"PhD in a technical field, with equivalent practical experience accepted","must":["PhD in a technical field, with equivalent practical experience accepted"],"nice":["PhD in ML, computer vision or NLP"],"pay":null,"ats":"Greenhouse","note":"JD10; undated; aggregators show a Bangalore RS listing removed on 2025-05-21, so probably closed; flagged stale; snippet only"}
{"type":"jd","grade":"B","src":["S8"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Google DeepMind","title":"Research Scientist, AnthroKrishi","url":"https://jobs.anitab.org/companies/google-24698/jobs/86441679-research-scientist-anthrokrishi-deepmind","job_id":"86441679","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"not stated","years":null,"degree":"PhD or equivalent practical research experience in CS, AI or a related field, with a focus on computer vision or ML","must":["PhD or equivalent practical research experience in CS, AI or a related field, focused on computer vision or ML"],"nice":[],"pay":null,"ats":"Google careers (via mirror)","note":"JD11; undated mirror; snippet only; job_id is the mirror's ID"}
{"type":"jd","grade":"A","src":["S9"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Meta","title":"Fundamental AI Research Scientist, FAIR (PhD)","url":"https://metacareers.com/jobs/1088304552854840","job_id":"1088304552854840","seen":"2026-11-13","location":"Menlo Park, Seattle, Boston, New York, San Francisco and 4 more, US","remote":"on-site","seniority":"early career (PhD completed before joining)","years":null,"degree":"Has or is completing a PhD (finished before joining), or equivalent practical experience","must":["Research background in ML, AI, computational statistics, applied mathematics or related areas","Research publications showing theoretical or empirical work","Developing and debugging in Python or a similar language"],"nice":["First-authored publications at peer-reviewed venues (ICML, NeurIPS, ACL, EMNLP, ICLR)","Research and engineering experience shown through grants, fellowships, patents, internships or coding competitions"],"pay":{"lo":117000,"hi":173000,"currency":"USD","period":"year"},"ats":"Meta careers","note":"JD12; base only, bonus and equity extra; undated; responsibilities include open-sourcing code and 'reproducible research'; work authorisation needed at hire; read in full"}
{"type":"jd","grade":"B","src":["S10"],"as_of":"2026-04-18","ttl":"V1","role":"role:research-scientist","employer":"Meta","title":"AI Research Scientist - MSL FAIR Foundations","url":"https://jobs.accel.com/companies/facebook-2-07d2eb1b-d3ad-4084-93df-74a124ac9233/jobs/75351325-ai-research-scientist-msl-fair-foundations","job_id":"75351325","seen":"2026-11-13","location":"Menlo Park, CA, US","remote":null,"seniority":"not stated","years":"3+","degree":"PhD in CS, ML or a related technical field","must":["PhD in CS, ML or a related technical field","3+ years in ML engineering, ML research or a related technical role"],"nice":[],"pay":{"lo":184000,"hi":257000,"currency":"USD","period":"year"},"ats":"Meta careers (via Accel mirror)","note":"JD13; posted 2026-04-18, outside window; job_id is the mirror's ID; snippet only"}
{"type":"jd","grade":"B","src":["S10"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Meta","title":"Research Scientist (PhD), Foundational Agent, Superintelligence Labs","url":"https://www.themuse.com/jobs/meta/research-scientist-phd-67dbfe","job_id":null,"seen":"2026-11-13","location":"Paris, France","remote":null,"seniority":"not stated","years":null,"degree":"PhD (stated in the title)","must":[],"nice":["High-impact publications at peer-reviewed AI venues (ACL, EMNLP, NeurIPS, ICML, ICLR)","AI research experience beyond completing a PhD","Experience in an industry research environment"],"pay":null,"ats":"Meta careers (via The Muse)","note":"JD14; required list not visible in the snippet; date unverified (mirror gave a relative label from an unknown crawl)"}
{"type":"jd","grade":"B","src":["S10"],"as_of":"2026-05-30","ttl":"V1","role":"role:research-scientist","employer":"Meta","title":"Research Scientist, FAIR SGT - New York","url":"https://jobs.accel.com/companies/facebook-2-07d2eb1b-d3ad-4084-93df-74a124ac9233/jobs/81106449-research-scientist-fair-sgt-new-york","job_id":"81106449","seen":"2026-11-13","location":"New York, NY, US","remote":null,"seniority":"not stated","years":null,"degree":null,"must":[],"nice":[],"pay":{"lo":154000,"hi":217000,"currency":"USD","period":"year"},"ats":"Meta careers (via Accel mirror)","note":"JD15; posted 2026-05-30, outside window; the snippet shows responsibilities only (generative models, LLM data efficiency, continual learning)"}
{"type":"jd","grade":"B","src":["S11"],"as_of":"2026-04-06","ttl":"V1","role":"role:research-scientist","employer":"NVIDIA","title":"Senior Research Scientist, Fundamental Generative AI","url":"https://inferencejobs.com/companies/nvidia/jobs/senior-research-scientist-fundamental-generative-ai","job_id":null,"seen":"2026-11-13","location":"Santa Clara, CA, US","remote":"on-site","seniority":"Senior","years":"2+","degree":"PhD in CS, engineering, statistics or similar, or equivalent experience","must":["Strong knowledge of generative AI theory and practice","Programming in Python, C++ and parallel programming (CUDA)","Deep learning frameworks such as PyTorch","Outstanding research track record"],"nice":[],"pay":{"lo":192000,"hi":304750,"currency":"USD","period":"year"},"ats":null,"note":"JD16; STALE: applications accepted at least until 2026-04-06; the mirror shows the posting about 7 months old; mirror of employer text read in full"}
{"type":"jd","grade":"B","src":["S11"],"as_of":"2026-08-01","ttl":"V1","role":"role:research-scientist","employer":"NVIDIA","title":"Senior Research Scientist - Generative World Models for Autonomous Driving and Physical AI","url":"https://jobs.anitab.org/companies/nvidia/jobs/88342766-senior-research-scientist-generative-world-models-for-autonomous-driving-and-physical-ai","job_id":"88342766","seen":"2026-11-13","location":"Santa Clara, CA, US","remote":null,"seniority":"Senior (levels 4 and 5)","years":null,"degree":null,"must":["Hands-on software engineering of production-quality AI systems for autonomous vehicles, 3D vision, generative world models, video understanding or simulation"],"nice":[],"pay":{"lo":192000,"hi":356500,"currency":"USD","period":"year"},"ats":"NVIDIA careers (via AnitaB mirror)","note":"JD17; L4 $192,000-$304,750 and L5 $224,000-$356,500; posted 2026-08-01, 104 days before retrieval (outside window by 14 days); job_id is the mirror's ID"}
{"type":"jd","grade":"B","src":["S11"],"as_of":"2026-04-10","ttl":"V1","role":"role:research-scientist","employer":"NVIDIA","title":"Research Scientist, Generative AI for Physical AI - PhD New College Grad 2026","url":"https://jobs.anitab.org/companies/nvidia/jobs/73966949-research-scientist-generative-ai-for-physical-ai-phd-new-college-grad-2026","job_id":"73966949","seen":"2026-11-13","location":"Santa Clara, CA, US","remote":null,"seniority":"New graduate (PhD)","years":null,"degree":"PhD (stated in the title)","must":["Deep PyTorch expertise for generative and physical AI","Foundation in diffusion, vision-language and reasoning models","Proven experience with RL algorithms"],"nice":[],"pay":{"lo":168000,"hi":264500,"currency":"USD","period":"year"},"ats":"NVIDIA careers (via AnitaB mirror)","note":"JD18; posted 2026-04-10, outside window; bullets as listed in the snippet, section header not visible"}
{"type":"jd","grade":"B","src":["S11"],"as_of":"2026-10-30","ttl":"V1","role":"role:research-scientist","employer":"NVIDIA","title":"Research Scientist, ML Systems - PhD New College Grad 2026","url":"https://zapply.jobs/jobs/9b90c7d3-0e56-4ed9-8fdf-0dfcd75e27f7/","job_id":null,"seen":"2026-11-13","location":"Santa Clara, CA, US and 3 more","remote":null,"seniority":"New graduate (PhD)","years":null,"degree":"PhD (stated in the title)","must":["Proven track record of research excellence","Depth in one systems layer (AI/ML systems, operating systems, distributed systems, data management, cloud, architecture)"],"nice":["Publication, patent and research-collaboration history"],"pay":null,"ats":"NVIDIA careers (via Zapply)","note":"JD19; posted 2026-10-30, inside window; applications accepted at least until 2026-11-03; ML-systems variant"}
{"type":"jd","grade":"B","src":["S12"],"as_of":"2026-05-06","ttl":"V1","role":"role:research-scientist","employer":"Microsoft","title":"Senior Researcher - Agentic AI - Microsoft Research AI Frontiers","url":"https://jobs.anitab.org/companies/microsoft/jobs/77547827-senior-researcher-agentic-ai-microsoft-research-ai-frontiers","job_id":"77547827","seen":"2026-11-13","location":"New York, NY, US","remote":null,"seniority":"Senior (Research Sciences IC4)","years":null,"degree":null,"must":[],"nice":[],"pay":{"lo":119800,"hi":234700,"currency":"USD","period":"year"},"ats":"Microsoft careers (via AnitaB mirror)","note":"JD20; alias title Senior Researcher; posted 2026-05-06, outside window; the band is Microsoft's typical US base; snippet only"}
{"type":"jd","grade":"B","src":["S12"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Microsoft","title":"Senior Researcher - Artificial Intelligence - Microsoft Research","url":"https://www.careerbuilder.com/job-details/senior-researcher-artificial-intelligence-microsoft-research-redmond-wa--4007c2a5-aafe-4eb2-bdb9-5c933eefd81c","job_id":null,"seen":"2026-11-13","location":"Redmond, WA, US","remote":null,"seniority":"Senior (Research Sciences IC4)","years":"2+ (preferred, with PhD)","degree":"PhD in CS or a related field, completed or close to completion; PhD plus 2+ years research experience preferred","must":["PhD in CS or a related field","Ability to develop and shape original research agendas","Proficient oral and written communication"],"nice":["Established publication record at top venues (NeurIPS, COLM, ICLR)"],"pay":{"lo":119800,"hi":234700,"currency":"USD","period":"year"},"ats":"Microsoft careers (via CareerBuilder)","note":"JD21; the Bay Area and NYC band is $158,400-$258,000; date unverified (mirror gave a relative label from an unknown crawl); alias title"}
{"type":"jd","grade":"B","src":["S13"],"as_of":"2026-11-05","ttl":"V1","role":"role:research-scientist","employer":"Microsoft","title":"Principal Research Scientist - AI Transformation team","url":"https://www.microsoft.com/en-us/research/careers/","job_id":null,"seen":"2026-11-13","location":"Remote (US)","remote":"remote (US)","seniority":"Principal","years":null,"degree":null,"must":[],"nice":[],"pay":null,"ats":"Microsoft careers","note":"JD22; title and date only, from the employer's careers listing posted 2026-11-05; requirements not read; may not be ML method research"}
{"type":"jd","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"OpenAI","title":"Research Scientist","url":"https://openai.com/careers/research-scientist-san-francisco/","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA, US","remote":null,"seniority":"not stated","years":null,"degree":null,"must":["Track record of new or improved ML ideas, shown by 'first author publications or projects'","Ability to own a research agenda: choose impactful problems and run long projects autonomously","Enthusiasm for OpenAI's approach to research"],"nice":["Thoughtfulness about the impacts of AI","Experience building high-performance implementations of deep learning algorithms"],"pay":{"lo":250000,"hi":445000,"currency":"USD","period":"year"},"ats":"Ashby (inferred from mirror IDs)","note":"JD23; direct fetch blocked by bot detection; search extract of the employer page; undated; equity extra; a Feb 2026 mirror shows $250k-$380k for a separate Research Scientist, PhD posting"}
{"type":"jd","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"OpenAI","title":"Research Engineer / Research Scientist, Post-Training","url":"https://openai.com/careers/research-engineer-research-scientist-post-training-san-francisco/","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA, US","remote":null,"seniority":"not stated","years":null,"degree":null,"must":["Strong ML engineering skills and research experience, especially with novel and highly capable models"],"nice":[],"pay":{"lo":295000,"hi":555000,"currency":"USD","period":"year"},"ats":"Ashby (inferred)","note":"JD24; combined RE/RS posting; offers equity; undated; search extract only"}
{"type":"jd","grade":"B","src":["S15"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"OpenAI","title":"Research Engineer / Research Scientist - ChatGPT Agent","url":"https://www.refer.me/job/openai-research-engineer--research-scientist--chatgpt-agent___85361","job_id":"85361","seen":"2026-11-13","location":"San Francisco, CA, US","remote":null,"seniority":"Mid level (per mirror)","years":null,"degree":null,"must":[],"nice":[],"pay":{"lo":295000,"hi":530000,"currency":"USD","period":"year"},"ats":"Ashby (via mirror)","note":"JD25; job_id is the mirror's ID; undated; snippet only"}
{"type":"jd","grade":"A","src":["S16"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"xAI","title":"AI Engineer & Researcher - Post-training","url":"https://job-boards.greenhouse.io/xai/jobs/4374125007","job_id":"4374125007","seen":"2026-11-13","location":"San Francisco and Palo Alto, CA, US","remote":"on-site (Bay Area or relocation)","seniority":"not stated","years":null,"degree":null,"must":["Expertise in ML and fine-tuning LLMs","Track record of leading research with significant impact on AI","Experience with advanced RL or inference-time search"],"nice":["Benchmark development or large-scale distributed ML systems experience"],"pay":{"lo":180000,"hi":440000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"JD26; stack Python, JAX, Rust; asks for a Google Scholar URL; states interview stages; undated; alias title; read in full"}
{"type":"jd","grade":"B","src":["S17"],"as_of":"2026-06-02","ttl":"V1","role":"role:research-scientist","employer":"Cohere","title":"Member of Technical Staff, Multilingual","url":"https://resumegeni.com/jobs/member-of-technical-staff-multilingual-at-cohere-london","job_id":null,"seen":"2026-11-13","location":"London (remote)","remote":"remote","seniority":"not stated","years":null,"degree":null,"must":["'Strong publication record or demonstrated research potential'","Ability to communicate across technical and research communities","Interest in advancing language technology"],"nice":[],"pay":{"lo":110000,"hi":370000,"currency":"USD","period":"year"},"ats":"Ashby","note":"JD27; US band, Canada band CAD 165,000-460,000; mirror date 2026-06-02, outside window; alias MTS; the mirror also carries third-party advice text"}
{"type":"jd","grade":"B","src":["S18"],"as_of":"2026-02-23","ttl":"V1","role":"role:research-scientist","employer":"Thinking Machines Lab","title":"Research, Pre-Training Science","url":"https://inferencejobs.com/companies/thinking-machines-lab/jobs/research-pre-training-science","job_id":null,"seen":"2026-11-13","location":"San Francisco, CA, US","remote":"on-site","seniority":"not stated","years":null,"degree":null,"must":[],"nice":[],"pay":{"lo":350000,"hi":475000,"currency":"USD","period":"year"},"ats":null,"note":"JD28; posted 2026-02-23, outside window; alias title; requirements not visible"}
{"type":"jd","grade":"A","src":["S19"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Mistral AI","title":"Lead AI Scientist, Finance (Mistral Science)","url":"https://jobs.lever.co/mistral/96aff642-c48a-44ec-81d4-654d1dbc615a","job_id":"96aff642-c48a-44ec-81d4-654d1dbc615a","seen":"2026-11-13","location":"Paris, France","remote":"hybrid","seniority":"Lead","years":null,"degree":null,"must":["Strong understanding of at least one scientific or industrial domain (finance, material physics, biology)","Record of AI/ML innovation on hard real-world problems, shown by first-author papers, open-source work or impactful projects","Expertise in ML, deep learning or LLMs, with PyTorch or TensorFlow","Experience working with customers or end users to refine requirements"],"nice":[],"pay":null,"ats":"Lever","note":"JD29; visa sponsorship listed; the employer may use AI tools in screening; undated; alias AI Scientist; read in full"}
{"type":"jd","grade":"A","src":["S20"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Mistral AI","title":"AI scientist (pre-training and fine-tuning LLMs)","url":"https://jobs.lever.co/mistral/675b7f06-a76b-4144-af0c-4dd3282ef489","job_id":"675b7f06-a76b-4144-af0c-4dd3282ef489","seen":"2026-11-13","location":"Paris / London","remote":"hybrid","seniority":"not stated","years":null,"degree":null,"must":["Strong scientific understanding of generative AI","Engineering competence across the 'full MLOps technical stack'"],"nice":[],"pay":null,"ats":"Lever","note":"JD30; undated text that may pre-date 2025; excluded from skill shares; alias AI Scientist"}
{"type":"jd","grade":"B","src":["S28"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Scale AI","title":"Machine Learning Research Scientist, Post-Training","url":"https://scale.com/careers/4528009005","job_id":"4528009005","seen":"2026-11-13","location":"San Francisco, CA; Seattle, WA; New York, NY, US","remote":null,"seniority":"not stated","years":null,"degree":"Master's or higher in CS, ML, AI or a related field (snippet cut before the first clause)","must":["Deep understanding of deep learning, RL and large-scale fine-tuning","Published ML research at major conferences or journals (NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR)"],"nice":[],"pay":null,"ats":null,"note":"JD31; undated; combined RS/RE posting; snippet only"}
{"type":"jd","grade":"B","src":["S25"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"DeepL","title":"Senior Research Scientist | Voice AI","url":"https://www.jobleads.com/gb/job/senior-research-scientist-voice-ai--city-of-london--e6671f8c18b92df2533288b20317eeaf6","job_id":null,"seen":"2026-11-13","location":"London, UK","remote":"on-site","seniority":"Senior","years":null,"degree":"PhD in mathematics, physics, CS or a related field (or equivalent)","must":["PhD in mathematics, physics, CS or a related field","Experience with large-scale deep learning models","PyTorch, TensorFlow or JAX"],"nice":[],"pay":{"lo":70000,"hi":90000,"currency":"GBP","period":"year"},"ats":null,"note":"JD32; the pay is the aggregator's figure; date unverified"}
{"type":"jd","grade":"B","src":["S25"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"ElevenLabs","title":"Machine Learning Researcher","url":"https://www.jobleads.com/gb/job/machine-learning-researcher--london--e3fde7b527bf543af55ee4158352751d9","job_id":null,"seen":"2026-11-13","location":"London, UK (remote)","remote":"remote","seniority":"not stated","years":null,"degree":null,"must":[],"nice":[],"pay":{"lo":60000,"hi":80000,"currency":"GBP","period":"year"},"ats":null,"note":"JD33; alias title; aggregator figure and a 30+ days label; requirements not visible"}
{"type":"jd","grade":"B","src":["S27"],"as_of":"2026-07-01","ttl":"V1","role":"role:research-scientist","employer":"AIXI Labs","title":"Machine Learning Research Scientist","url":"https://www.aixi.uk/team/opportunities/ml-research-scientist/","job_id":null,"seen":"2026-11-13","location":"London, UK or Berkeley, US","remote":null,"seniority":"not stated","years":null,"degree":"PhD in CS, physics or a related field preferred","must":["Maths background to upskill quickly on algorithmic information theory, AIXI, Bayesian statistics and RL theory","Proven ability to design, build and run experiments with LLM-based agents independently","Ability to find a worthwhile question and drive it to a concrete result with minimal oversight","Strong verbal and written communication"],"nice":["Publications at top ML, AI or theory venues, though the posting values 'the strength of your best work over volume'"],"pay":{"lo":120000,"hi":160000,"currency":"GBP","period":"year"},"ats":null,"note":"JD34; JSON-LD datePosted 2026-07-01 and validThrough 2026-12-01, so live at retrieval; the posting has no job ID"}
{"type":"jd","grade":"B","src":["S29"],"as_of":"2026-11-02","ttl":"V1","role":"role:research-scientist","employer":"Plaid","title":"Staff Machine Learning Engineer (Research Scientist) - DFAI","url":"https://jobs.physicstoday.org/job/42042931/staff-machine-learning-engineer-research-scientist-dfai/","job_id":"42042931","seen":"2026-11-13","location":"San Francisco, CA, US","remote":"on-site","seniority":"Staff","years":null,"degree":"Bachelor's (per mirror)","must":["Deep expertise in transformers, LLMs and foundation models, including large-scale training or domain adaptation"],"nice":[],"pay":null,"ats":null,"note":"JD35; posted 2026-11-02 and closing 2026-11-10 per the mirror; job_id is the mirror's ID; alias title; pay stated as commensurate"}
{"type":"jd","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"JPMorgan Chase","title":"AI Research Scientist - Senior Associate","url":"https://www.careerbuilder.com/job-details/ai-research-scientist-sr-associate-new-york-ny--dc5600e4-c659-4ad5-b6f5-0cacb621b29c","job_id":null,"seen":"2026-11-13","location":"New York, NY, US","remote":"on-site or hybrid","seniority":"Senior Associate","years":"MS plus 3 years if no PhD","degree":"PhD in CS or a related field, or an MS with at least 3 years of experience","must":["PhD (or MS plus 3 years) in CS or a related field","Research publications in prominent AI venues","Python programming skills"],"nice":["Expertise in synthetic data, generative AI, or LLM alignment and behaviour modelling with RL"],"pay":{"lo":128250,"hi":195000,"currency":"USD","period":"year"},"ats":null,"note":"JD36; a Dice listing shows $137,750-$195,000; date unverified"}
{"type":"jd","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"JPMorgan Chase","title":"AI Research Scientist - Senior Associate (NLP)","url":"https://www.themuse.com/jobs/jpmorganchase/senior-associate-ai-researcher-natural-language-processing","job_id":null,"seen":"2026-11-13","location":"London, UK","remote":null,"seniority":"Senior Associate","years":null,"degree":null,"must":[],"nice":[],"pay":null,"ats":null,"note":"JD37; the snippet describes end-to-end research, typically in NLP; date unverified"}
{"type":"jd","grade":"B","src":["S23"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"IBM Research India","title":"Research Scientist","url":"https://refresh.cv/jobs/ibm/ddbc05b2-dc5a-4bc4-afef-eda9965b0fd5","job_id":"111792","seen":"2026-11-13","location":"Bangalore, India","remote":"hybrid","seniority":"Mid level (per mirror)","years":"2-4","degree":"Doctorate (required education)","must":["Doctorate degree"],"nice":[],"pay":null,"ats":"IBM careers","note":"JD38; the work spans foundation models, deep learning, reinforcement learning and generative computing; the mirror gave a relative date label from an unknown crawl"}
{"type":"jd","grade":"B","src":["S23"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"IBM Research India","title":"Research Scientist (AI agents)","url":"https://jobs.weekday.works/research-scientist-at-ibm-4364739540","job_id":"143126037","seen":"2026-11-13","location":"Bengaluru, India","remote":null,"seniority":"not stated","years":null,"degree":"PhD in CS, ML, AI, mathematics or a related field","must":["PhD in CS, ML, AI, mathematics or a related field","Expertise in ML and deep learning (transformers, representation learning, generative models)","Research track record with publications at top venues (NeurIPS, ICML, ICLR, CVPR, ACL)","Python and an ML framework (PyTorch or TensorFlow)"],"nice":["Foundations in linear algebra, probability, statistics, calculus and optimisation","LLM experience","Industry research experience in a corporate or applied setting"],"pay":null,"ats":"IBM careers","note":"JD39; job_id is the foundit listing ID; undated mirror"}
{"type":"jd","grade":"A","src":["S22"],"as_of":"2026-01-16","ttl":"V1","role":"role:research-scientist","employer":"GE Vernova","title":"Research Scientist - Machine Learning","url":"https://careers.gevernova.com/research-scientist-machine-learning/job/R5022607","job_id":"R5022607","seen":"2026-11-13","location":"Bangalore, India","remote":"on-site","seniority":"not stated","years":"PhD with 2-5 years, or Master's with 5-7 years","degree":"PhD with 2-5 years of experience, or Master's with 5-7 years, from a reputed institution","must":["Fundamentals of statistics, ML and AI","Programming in Python, PySpark, PyTorch, Pandas or similar","Ability to build prototypes and proofs of concept quickly"],"nice":[],"pay":null,"ats":"GE Vernova careers","note":"JD40; posting start 2026-01-16, outside window; applied time-series ML for energy equipment; duties include designing and running experiments (counted under research_methods); read in full"}
{"type":"jd","grade":"A","src":["S21"],"as_of":"2026-11-13","ttl":"V1","role":"role:research-scientist","employer":"Sarvam AI","title":"ML Researcher, Foundational Models","url":"https://www.sarvam.ai/careers/jobs/2dcb062d-e42b-408d-be15-59ddde900984","job_id":"2dcb062d-e42b-408d-be15-59ddde900984","seen":"2026-11-13","location":"Bengaluru, India","remote":"on-site","seniority":"post-PhD researcher","years":"3+ years post-PhD (or equivalent depth)","degree":"PhD in ML, CS or a closely related field (or in the final stages)","must":["First-author publications at top-tier ML venues (NeurIPS, ICML, ICLR, ACL, EMNLP, COLM)","Hands-on pre-training of transformer language models from scratch, ideally at 7B+ parameters","PyTorch fluency and comfort with distributed training","'Strong intuition for experimental design'"],"nice":["Novel architectures (mixture-of-experts, state-space, hybrid)","Post-training research (RLHF, RLVR, distillation, reasoning models)"],"pay":null,"ats":"Ashby","note":"JD41; undated; alias ML Researcher; read in full"}
{"type":"jd","grade":"B","src":["S26"],"as_of":"2026-11-07","ttl":"V1","role":"role:research-scientist","employer":"Careernet (client unnamed)","title":"Senior ML Research Scientist - Speech AI","url":"https://www.hirist.tech/j/senior-ml-research-scientist-speech-ai-1682825","job_id":"1682825","seen":"2026-11-13","location":"Bangalore, India","remote":null,"seniority":"Senior","years":"5-9 (3-6 in ML, with 2-3 in speech)","degree":"MS or PhD in CS, EE or a related field, or equivalent depth shown through shipped production models","must":["3-6 years in ML, of which 2-3 are focused on speech (ASR, TTS, speaker or voice, audio-language models)"],"nice":[],"pay":null,"ats":"Hirist","note":"JD42; recruiter listing; posted 07/11/2026, read as DD/MM; the page itself is JS-only so the text comes from a search snippet"}
{"type":"jd","grade":"B","src":["S58"],"as_of":"2026-06-15","ttl":"V1","role":"role:research-scientist","employer":"Accenture","title":"AI Applied Researcher","url":"https://www.ziprecruiter.ie/jobs/544672920-ai-applied-researcher-at-accenture","job_id":"544672920","seen":"2026-11-13","location":"Dublin, Ireland","remote":null,"seniority":"Applied scientist level","years":null,"degree":null,"must":["Applied AI research with hands-on prototype development","Ability to combine model reasoning, external knowledge and tools into reliable end-to-end systems"],"nice":["Prior experience in an AI research lab, an applied research group or an advanced R&D setting"],"pay":null,"ats":"Accenture careers (via ZipRecruiter mirror)","note":"JD43; posted 2026-06-15 per the mirror, outside window; job_id is the mirror's ID; an unlabelled SimplyHired Ireland snippet, believed but not confirmed to be this role, gives Master's plus 2-3 years or PhD plus 1-2 years, so the degree is left null; applied variant; alias AI Applied Researcher"}
{"type":"jd","grade":"B","src":["S58"],"as_of":"2026-03-24","ttl":"V1","role":"role:research-scientist","employer":"Accenture","title":"AI Research & Innovation Lead (Centre for Advanced AI)","url":"https://builtin.com/job/ai-ml-engineer/8474198","job_id":"8474198","seen":"2026-11-13","location":"India (several cities including Bangalore)","remote":null,"seniority":"Lead","years":null,"degree":"PhD in CS, EE, mathematics, AI, statistics or similar from a top-tier institute (IIT, IISc, ISI, IIIT)","must":["PhD in CS, EE, mathematics, AI, statistics or similar from a top-tier institute","Experience in AI/ML, NLP, computer vision, speech or multimodal work"],"nice":["Leading research and publishing at top-tier conferences","Mentoring AI talent"],"pay":null,"ats":"Accenture careers (via Built In mirror)","note":"JD44; STALE: removed from Built In on 2026-03-24; the posting phrases the PhD as a question, treated here as required; the mirror's title is AI / ML Engineer while the text names the AI Research & Innovation Lead role; job_id is the mirror's ID"}
{"type":"jd","grade":"B","src":["S59"],"as_of":"2025-12-17","ttl":"V1","role":"role:research-scientist","employer":"Amazon","title":"Member of Technical Staff - Applied Science (New PhD), AGI Autonomy","url":"https://amazon.jobs/en/jobs/2912776/member-of-technical-staff-applied-science-new-phd-agi-autonomy","job_id":"2912776","seen":"2026-11-13","location":"San Francisco, CA, US","remote":null,"seniority":"New graduate (PhD)","years":null,"degree":"PhD in CS or a related field","must":["PhD in CS or a related field","Experience with deep learning methods and tools, for example PyTorch or JAX"],"nice":[],"pay":null,"ats":"Amazon careers","note":"JD45; posted about 2025-12-17 per a mirror snippet (unverified), outside window; a programming-language line (Python, Java and a C-family language) is not reproduced; alias MTS - Applied Science; Amazon titles most ML research Applied Scientist"}
```

```jsonl
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"ml_fundamentals","n":12,"source_kind":"jd-sample","share":1.0,"count":12,"tier_hint":"Must","note":"ML named in every fully read posting (JD01-06, 12, 16, 26, 29, 40, 41)"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"python","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Must","note":"named in 8; the other 4 name JAX or PyTorch, implying Python; JD02 counted because the posting says interviews are in Python"}
{"type":"skill_signal","grade":"M","src":["S3","S4","S5","S6","S11","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"pytorch","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Must","note":"write as PyTorch or JAX"}
{"type":"skill_signal","grade":"M","src":["S1","S3","S5","S6","S9","S11","S19","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"deep_learning","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Must","note":"includes transformers and diffusion wording"}
{"type":"skill_signal","grade":"M","src":["S2","S3","S4","S5","S6","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"research_methods","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Must","note":"experiment design, ablations, full research lifecycle"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"research_novelty","n":12,"source_kind":"jd-sample","share":0.917,"count":11,"tier_hint":"Must","note":"9 of 11 in required lists, 2 preferred only"}
{"type":"skill_signal","grade":"M","src":["S3","S5"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"linear_algebra","n":12,"source_kind":"jd-sample","share":0.167,"count":2,"tier_hint":"Important","note":"explicit in 2; any maths foundation in 6 (see new:mathematical_foundations)"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S9","S16","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"communication","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Important","note":"Anthropic counts rely partly on boilerplate that values communication skills"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"creativity","n":12,"source_kind":"jd-sample","share":0.0,"count":0,"tier_hint":"Optional","note":"not named in any fully read posting"}
{"type":"skill_signal","grade":"M","src":["S1"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"llm_apis","n":12,"source_kind":"jd-sample","share":0.083,"count":1,"tier_hint":"Optional","note":"agentic tools and tool-use environments in Anthropic Life Sciences only"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"dsa","n":12,"source_kind":"jd-sample","share":0.0,"count":0,"tier_hint":"Should","note":"in no JD; held at Should because coding rounds exist (xAI coding assessment, Anthropic Python interviews, DeepMind coding interview)"}
{"type":"skill_signal","grade":"M","src":["S2","S4","S5","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"scientific_writing","n":12,"source_kind":"jd-sample","share":0.333,"count":4,"tier_hint":"Should","note":"writeups, research writing, blog posts, internal writing"}
{"type":"skill_signal","grade":"M","src":["S1","S4","S16"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"rl","n":12,"source_kind":"jd-sample","share":0.25,"count":3,"tier_hint":"Should","note":"explicit RL in 3; 5 of 12 if RLHF and RLVR wording counts; Must on RL teams"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S4","S16","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"post_training","n":12,"source_kind":"jd-sample","share":0.417,"count":5,"tier_hint":"Important","note":"SFT, RLHF, fine-tuning; Must on post-training teams"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S4","S6","S16"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"evals","n":12,"source_kind":"jd-sample","share":0.417,"count":5,"tier_hint":"Important","note":"benchmarks, LLM-based grading, ablations, red-teaming"}
{"type":"skill_signal","grade":"M","src":["S4","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"research_taste","n":12,"source_kind":"jd-sample","share":0.167,"count":2,"tier_hint":"Should","note":"explicit in DeepMind RL and Sarvam; five postings in the wider sample name problem selection or taste (JD04, 23, 29, 34, 41)"}
{"type":"skill_signal","grade":"M","src":["S5","S9","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"statistics","n":12,"source_kind":"jd-sample","share":0.25,"count":3,"tier_hint":"Should","note":"statistics named in 3"}
{"type":"skill_signal","grade":"M","src":["S3","S4","S5","S6","S16"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:jax","n":12,"source_kind":"jd-sample","share":0.417,"count":5,"tier_hint":"Important","note":"Must at DeepMind and xAI"}
{"type":"skill_signal","grade":"M","src":["S2","S3","S4","S5","S6","S11","S16","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:large_scale_training","n":12,"source_kind":"jd-sample","share":0.667,"count":8,"tier_hint":"Important","note":"large-scale training or experiments; often in preferred lists"}
{"type":"skill_signal","grade":"M","src":["S1","S3","S5","S9","S19","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:open_source_code","n":12,"source_kind":"jd-sample","share":0.5,"count":6,"tier_hint":"Important","note":"open-source contributions or reproducible code"}
{"type":"skill_signal","grade":"M","src":["S3","S5","S6","S9","S11","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:mathematical_foundations","n":12,"source_kind":"jd-sample","share":0.5,"count":6,"tier_hint":"Important","note":"superset of linear algebra and statistics"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S4","S5","S16","S19","S21"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:llm_modelling","n":12,"source_kind":"jd-sample","share":0.583,"count":7,"tier_hint":"Important","note":"LLMs as the research subject; replaces the misplaced llm share on llm_apis"}
{"type":"skill_signal","grade":"M","src":["S3","S5","S6","S19"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:tensorflow","n":12,"source_kind":"jd-sample","share":0.333,"count":4,"tier_hint":"Optional","note":"only as one of JAX, PyTorch or TensorFlow"}
{"type":"skill_signal","grade":"M","src":["S5","S11"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:cpp_cuda","n":12,"source_kind":"jd-sample","share":0.167,"count":2,"tier_hint":"Optional","note":"C++ or CUDA named in 2"}
{"type":"skill_signal","grade":"M","src":["S1","S19","S22"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","skill":"new:domain_expertise","n":12,"source_kind":"jd-sample","share":0.25,"count":3,"tier_hint":"Should","note":"biology, finance and materials, energy"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"python","n":null,"source_kind":"platform","share":0.423,"note":"JobsPipe, all fields of research scientist; n not published"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"communication","n":null,"source_kind":"platform","share":0.413,"note":"JobsPipe, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"ml_fundamentals","n":null,"source_kind":"platform","share":0.392,"note":"JobsPipe machine-learning, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"dsa","n":null,"source_kind":"platform","share":0.26,"note":"JobsPipe data-structures, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"pytorch","n":null,"source_kind":"platform","share":0.254,"note":"JobsPipe, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"new:llm_modelling","n":null,"source_kind":"platform","share":0.244,"note":"JobsPipe llm share; measures LLM mention, not API skill"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"creativity","n":null,"source_kind":"platform","share":0.23,"note":"JobsPipe, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"deep_learning","n":null,"source_kind":"platform","share":0.186,"note":"JobsPipe, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"new:cpp_cuda","n":null,"source_kind":"platform","share":0.174,"note":"JobsPipe C++, all fields"}
{"type":"skill_signal","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V3","role":"role:research-scientist","skill":"rl","n":null,"source_kind":"platform","share":0.171,"note":"JobsPipe reinforcement-learning, all fields"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of active postings located in the United States","unit":"percent","value":65.0,"method":"JobsPipe index, canonical title research scientist, all fields; counts unpublished","region":"US","note":"all-fields scope (software 8.7%, publishing 6.8%, pharma 3.3%); not AI-specific"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of active postings located in India","unit":"percent","value":3.7,"method":"JobsPipe, all fields","region":"IN","note":"scope mismatch with AI"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of active postings located in the United Kingdom","unit":"percent","value":4.7,"method":"JobsPipe, all fields","region":"UK"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of active postings located in Germany","unit":"percent","value":5.6,"method":"JobsPipe, all fields","region":"DE"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of active postings located in Singapore","unit":"percent","value":3.8,"method":"JobsPipe, all fields","region":"SG"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of postings carrying a remote flag","unit":"percent","value":3.3,"method":"JobsPipe, all fields"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of postings stating pay","unit":"percent","value":35.2,"method":"JobsPipe, all fields"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of postings labelled entry level","unit":"percent","value":12.2,"method":"JobsPipe; unlabelled postings stay in the denominator"}
{"type":"measure","grade":"B","src":["S30"],"as_of":"2026-09-10","ttl":"V1","subject":"role:research-scientist","measure":"share of postings labelled senior","unit":"percent","value":11.3,"method":"JobsPipe; unlabelled postings stay in the denominator"}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-07-21","ttl":"V1","subject":"role:research-scientist","measure":"open Research Scientist roles at AI startups","unit":"count","value":333,"method":"Fast AI Jobs role page; 171 startups; snapshot date inferred from the newest listed role","note":"54% at Pre-Seed to Series B"}
{"type":"measure","grade":"C","src":["S49"],"as_of":"2026-11-13","ttl":"V1","subject":"role:research-scientist","measure":"remote research scientist machine learning listings","unit":"count","value":249,"method":"Glassdoor page headed November 2026","region":"remote","note":"includes contract roles; scope loose"}
{"type":"measure","grade":"B","src":["S35"],"as_of":"2026-08-01","ttl":"V4","subject":"role:research-scientist","measure":"OpenAI certified LCA positions titled MTS (Research Scientist)","unit":"count","value":188,"method":"ellis.com table headed 2026 (DOL LCA data); month only known","region":"US","note":"positions, not workers; LCAs show filings, not pay"}
{"type":"measure","grade":"B","src":["S35"],"as_of":"2026-08-01","ttl":"V4","subject":"role:research-scientist","measure":"OpenAI OpCo LCA filings in 2025","unit":"count","value":165,"method":"ellis.com; 2023 28, 2024 96, 2026 165","region":"US","note":"other aggregators give 239 (froghire, FY2026) and 311 wage records (careery.pro); cuts differ"}
{"type":"measure","grade":"B","src":["S36"],"as_of":"2026-04-01","ttl":"V4","subject":"role:research-scientist","measure":"Anthropic certified LCA positions titled Member of Technical Staff","unit":"count","value":223,"method":"ellis.com, last updated April 2026","region":"US","note":"title is broader than research scientist; COI"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S9","S16"],"as_of":"2026-11-13","ttl":"V1","subject":"role:research-scientist","measure":"postings in the job-description sample","unit":"count","value":45,"method":"17 frontier lab, 14 Big Tech, 7 AI-native, 6 enterprise or consultancy, 1 agency; US 23, Europe 12, India 9, Canada 1","note":"6 inside the 90-day window, 16 outside, 23 undated; 8 postings excluded as not AI/ML research or not full-time"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S9","S16"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of sampled postings disclosing a base range","unit":"percent","value":48.9,"n":45,"method":"22 of 45","note":"US 18 of 23 (78.3%); India 0 of 9"}
{"type":"measure","grade":"M","src":["S1","S3","S5","S6","S9","S11","S12","S19","S22","S24"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of postings requiring a PhD (outright or with an equivalent substitute)","unit":"percent","value":57.6,"n":33,"method":"19 of 33 postings with visible degree wording; 9 outright, 10 with substitute","note":"PhD required or preferred 22 of 33 (66.7%); no PhD named 8 of 33 (24.2%); 12 postings had no visible degree wording"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S5","S6","S14","S16","S19","S20"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of frontier-lab postings requiring PhD or equivalent","unit":"percent","value":30.8,"n":13,"method":"4 of 13 with degree text; 6 name none; 3 prefer a PhD or ask for an advanced degree","note":"DeepMind states that most of its RS hires are post-PhD (undated page)"}
{"type":"measure","grade":"M","src":["S9","S10","S11","S12","S23","S59"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of Big Tech postings with visible degree text that require a PhD (outright or with substitute)","unit":"percent","value":100.0,"n":10,"method":"10 of 10; 4 further Big Tech postings had no visible degree wording"}
{"type":"measure","grade":"M","src":["S2","S13","S17","S25"],"as_of":"2026-11-13","ttl":"V1","subject":"role:research-scientist","measure":"share of sampled postings remote-friendly or remote","unit":"percent","value":8.9,"n":45,"method":"4 of 45","note":"JobsPipe all-fields remote flag is 3.3%"}
{"type":"measure","grade":"M","src":["S2","S11","S12","S13","S19","S24","S25","S26","S29","S58"],"as_of":"2026-11-13","ttl":"V1","subject":"role:research-scientist","measure":"share of sampled titles with senior, staff, principal or lead","unit":"percent","value":28.9,"n":45,"method":"13 of 45; early-career or new-graduate PhD 4 (8.9%); level not stated 28 (62.2%)"}
{"type":"measure","grade":"M","src":["S9","S11","S26"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of sampled postings with multimodal wording","unit":"percent","value":8.9,"n":45,"method":"4 of 45 (JD12, 17, 18, 42)","note":"modality-specific work including vision, video, speech and audio: 7 of 45 (15.6%)"}
{"type":"measure","grade":"M","src":["S7","S11","S16"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of sampled postings with reasoning or test-time compute wording","unit":"percent","value":6.7,"n":45,"method":"3 of 45 (JD07, 18, 26)"}
{"type":"measure","grade":"M","src":["S3","S5","S9","S11","S12","S14"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of sampled postings in models and research (L2)","unit":"percent","value":60.0,"n":45,"method":"27 of 45 by my classification of title and description","note":"post-training 6 (13.3%); applied or domain 9 (20.0%); assurance 2 (4.4%); ML systems 1 (2.2%)"}
{"type":"measure","grade":"M","src":["S1","S2","S3","S4","S5","S6","S9","S11","S16","S19","S21","S22"],"as_of":"2026-11-13","ttl":"V3","subject":"role:research-scientist","measure":"share of fully read postings naming any certification","unit":"percent","value":0.0,"n":12,"method":"0 of 12; none seen in the text or snippets of the other 33"}
{"type":"measure","grade":"B","src":["S45"],"as_of":"2026-03-01","ttl":"V5","subject":"role:research-scientist","measure":"earnings premium of AI researchers moving to industry versus similar academic switchers","unit":"percent","value":63.0,"method":"NBER WP 34964; career-history data on AI researchers","note":"working paper, not peer-reviewed"}
{"type":"measure","grade":"B","src":["S46"],"as_of":"2025-06-25","ttl":"V3","subject":"role:research-scientist","measure":"average professorial salary quoted for US computer science","unit":"USD per year","value":155000,"method":"quote from a Northwestern professor in Fortune","note":"all CS professors, not new hires; the same quote puts corporate-role PhDs at up to 5 times as much"}
{"type":"pay","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"San Francisco, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI careers (search extract)","lo":250000,"hi":445000,"employer_type":"frontier-lab","n":1,"note":"general Research Scientist posting; equity extra"}
{"type":"pay","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"San Francisco, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI careers (search extract)","lo":295000,"hi":555000,"employer_type":"frontier-lab","n":1,"note":"combined RE/RS post-training"}
{"type":"pay","grade":"A","src":["S1"],"as_of":"2026-08-21","ttl":"V3","role":"role:research-scientist","location":"San Francisco, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Anthropic Greenhouse API","lo":300000,"hi":320000,"employer_type":"frontier-lab","n":1,"note":"Research Scientist, Life Sciences; COI"}
{"type":"pay","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"San Francisco / remote-friendly, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Anthropic Greenhouse","lo":340000,"hi":425000,"level":"Senior","employer_type":"frontier-lab","n":1,"note":"COI"}
{"type":"pay","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"Mountain View / San Francisco, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Google DeepMind Greenhouse","lo":174000,"hi":252000,"employer_type":"frontier-lab","n":1,"note":"plus bonus, equity, benefits"}
{"type":"pay","grade":"A","src":["S9"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"US (multiple)","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Meta careers","lo":117000,"hi":173000,"level":"early career (PhD)","employer_type":"big-tech","n":1}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-04-18","ttl":"V3","role":"role:research-scientist","location":"Menlo Park, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Meta via Accel mirror","lo":184000,"hi":257000,"employer_type":"big-tech","n":1,"note":"MSL FAIR Foundations; outside window"}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-08-01","ttl":"V3","role":"role:research-scientist","location":"Santa Clara, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"NVIDIA via mirrors","lo":168000,"hi":356500,"level":"L3 to L5","employer_type":"big-tech","n":3,"note":"L3 $168,000-$264,500; L4 $192,000-$304,750; L5 $224,000-$356,500"}
{"type":"pay","grade":"B","src":["S12"],"as_of":"2026-05-06","ttl":"V3","role":"role:research-scientist","location":"US (typical); Bay Area and NYC higher","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Microsoft Research Senior Researcher IC4","lo":119800,"hi":234700,"level":"IC4","employer_type":"big-tech","n":2,"note":"Bay Area and NYC band $158,400-$258,000"}
{"type":"pay","grade":"A","src":["S16"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"San Francisco and Palo Alto, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"xAI Greenhouse","lo":180000,"hi":440000,"employer_type":"frontier-lab","n":1}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-02-23","ttl":"V3","role":"role:research-scientist","location":"San Francisco, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Thinking Machines Lab via Inference Jobs","lo":350000,"hi":475000,"employer_type":"ai-startup","n":1}
{"type":"pay","grade":"B","src":["S17"],"as_of":"2026-06-02","ttl":"V3","role":"role:research-scientist","location":"US (Cohere remote)","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Cohere via mirror","lo":110000,"hi":370000,"employer_type":"ai-startup","n":1,"note":"Canada CAD 165,000-460,000"}
{"type":"pay","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"New York, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"JPMorgan AI Research Scientist Senior Associate via CareerBuilder","lo":128250,"hi":195000,"level":"Senior Associate","employer_type":"enterprise","n":1}
{"type":"pay","grade":"B","src":["S59"],"as_of":"2026-01-05","ttl":"V3","role":"role:research-scientist","location":"Sunnyvale, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Amazon Applied Scientist, AGI (adjacent title) via aplyr mirror","lo":136000,"hi":223400,"employer_type":"big-tech","n":1,"note":"adjacent title, not counted in the sample; RSUs extra"}
{"type":"pay","grade":"B","src":["S25"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"London, UK","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"DeepL Senior RS via JobLeads","lo":70000,"hi":90000,"level":"Senior","employer_type":"ai-startup","n":1,"note":"aggregator figure"}
{"type":"pay","grade":"C","src":["S25"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"London, UK","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"ElevenLabs ML Researcher via JobLeads","lo":60000,"hi":80000,"employer_type":"ai-startup","n":1,"note":"aggregator figure; alias title"}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-07-01","ttl":"V3","role":"role:research-scientist","location":"London, UK","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"AIXI Labs","lo":120000,"hi":160000,"employer_type":"ai-startup","n":1}
{"type":"pay","grade":"C","src":["S52"],"as_of":"2026-04-01","ttl":"V3","role":"role:research-scientist","location":"Zurich, Switzerland","stat":"range","currency":"CHF","period":"year","basis":"base","source_name":"Lohncheck.ch quoting an Anthropic posting","lo":280000,"hi":680000,"employer_type":"frontier-lab","n":1,"note":"secondary source; combined RE/RS pre-training; COI"}
{"type":"pay","grade":"B","src":["S32"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi OpenAI Research Scientist","value":1250000,"employer_type":"frontier-lab","note":"L4 $763K and L5 $1.39M by level; another line on the page gives $1.26M; highest reported $1.9M; self-reported; equity is private-company valuation"}
{"type":"pay","grade":"B","src":["S33"],"as_of":"2025-12-11","ttl":"V3","role":"role:research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Anthropic Research Scientist","value":746404,"employer_type":"frontier-lab","note":"another cached page shows $875K; self-reported; COI"}
{"type":"pay","grade":"B","src":["S47"],"as_of":"2026-08-24","ttl":"V3","role":"role:research-scientist","location":"United States (Pave dataset)","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Pave and Nua Group State of AI Talent","value":4090000,"level":"P6","n":null,"note":"equity component only (basis tc is the closest allowed value): median new-hire equity as an intended annualised value at grant; M6 $4.72M; median base $311,000 (P6) and $340,000 (M6); the P90 tail of about $45-60M applies to private Bay Area firms with $1B-$5B+ raised; vendor data; COI"}
{"type":"pay","grade":"B","src":["S35"],"as_of":"2026-08-01","ttl":"V4","role":"role:research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"OpenAI OpCo LCA, MTS (Research Scientist)","value":360000,"employer_type":"frontier-lab","n":188,"note":"wage filed on LCAs, not evidence of pay; min $178,006, max $685,000"}
{"type":"pay","grade":"B","src":["S31"],"as_of":"2026-07-21","ttl":"V3","role":"role:research-scientist","location":"AI startups (posted)","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Fast AI Jobs disclosed Research Scientist salaries","value":216750,"employer_type":"ai-startup","n":122,"note":"range $112,320-$412,500; later snapshots show n 132-134"}
{"type":"pay","grade":"B","src":["S34"],"as_of":"2026-07-20","ttl":"V3","role":"role:research-scientist","location":"India","stat":"p50","currency":"INR","period":"year","basis":"tc","source_name":"Levels.fyi Google Research Scientist India","value":3053733,"level":"L3","employer_type":"big-tech","n":null,"note":"n not shown; language variants of the page conflict and were not used"}
{"type":"pay","grade":"C","src":["S50"],"as_of":"2026-06-23","ttl":"V3","role":"role:research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Choppingblock Research Scientist salaries","value":262800,"n":138,"note":"P25 $174,000; P75 $435,000; submission-based; cross-check only"}
{"type":"pay","grade":"M","src":["S1","S2","S3","S6","S9","S10","S11","S12","S14","S16","S18","S24"],"as_of":"2026-11-13","ttl":"V3","role":"role:research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"median of posted range midpoints, sample","value":234438,"n":18,"note":"frontier lab $328,750 (n=8); Big Tech $200,875 (n=8); some inputs outside the window"}
{"type":"loop","grade":"A","src":["S55"],"as_of":"2026-11-13","ttl":"V2","employer":"Google DeepMind","track":"research","stages":["recruiter chat","technical interviews: breadth quiz on CS, statistics, maths and ML, plus a coding interview in a language of choice","research interviews of about 30 minutes with researchers and leads, including a talk on your research","culture interview"],"formats":["roughly even split between coding and research assessment"],"ai_policy":null,"take_home":null,"duration":null,"note":"employer page with no date, possibly older than 2025; 2026 candidate reports (C) describe two research and two coding interviews [S56]"}
{"type":"loop","grade":"A","src":["S16"],"as_of":"2026-11-13","ttl":"V2","employer":"xAI","track":"research","stages":["CV and statement of best work","15-minute phone interview","coding assessment in a language of choice","2 post-training technical sessions (research or engineering depending on background)","meet-the-team presentation of past work and vision"],"formats":["Google Meet"],"ai_policy":null,"take_home":null,"duration":"main process targeted within one week","note":"employer-stated on the posting"}
{"type":"loop","grade":"C","src":["S2","S39","S40"],"as_of":"2026-11-13","ttl":"V2","employer":"Anthropic","track":"research","stages":["written application with a why-Anthropic question","CodeSignal assessment (candidate-reported)","phone screen","technical video interview","15-minute research discussion"],"formats":["all interviews in Python (employer-stated on the RS Reward Models posting)"],"ai_policy":"Take-homes without Claude unless indicated; live interviews no AI assistance unless indicated; Claude allowed for preparation and for refining a self-written application","take_home":"role-dependent","duration":null,"note":"stages are candidate-reported (C); the Python statement and the AI policy are employer text; COI"}
{"type":"loop","grade":"C","src":["S41"],"as_of":"2026-10-29","ttl":"V2","employer":"Anthropic","track":"research","stages":["recruiter screen","ML coding such as attention or training loops with debugging","system design for large-model training","paper discussion","project deep dive","values round"],"formats":["live Python"],"ai_policy":"Same published guidance","take_home":null,"duration":null,"note":"research-engineer loop from a guide; adjacent to the RS loop; COI (subject)"}
{"type":"practice","grade":"P","src":["S1","S3","S4","S9","S16"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Lead with first-author publications (venue, year, one-line contribution) and link code","claim":"Publications are named in 11 of 12 fully read postings","evidence":"jd-sample; employer text","verdict":"use"}
{"type":"practice","grade":"P","src":["S16","S55"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Include a Google Scholar profile and links to GitHub, side projects or code","claim":"xAI's form asks for a Scholar URL and DeepMind's page invites GitHub and side-project links","evidence":"employer application form and employer page","verdict":"use"}
{"type":"practice","grade":"P","src":["S3","S21"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Evidence-line pattern: Implemented [method] in [PyTorch/JAX]; trained at [scale]; [result] versus [named baseline]","claim":"Framework fluency and scale are named in 8 of 12 postings","evidence":"jd-sample; pattern only, fill with real work","verdict":"use"}
{"type":"practice","grade":"P","src":["S4","S21"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Show experimental design: ablations run, factors varied, decision changed","claim":"Research methods and experimental taste are named in postings","evidence":"jd-sample","verdict":"use"}
{"type":"practice","grade":"P","src":["S16","S27"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Do not claim novelty without a public artefact (paper, code or write-up)","claim":"Employers ask for demonstrated work, not claims","evidence":"employer text","verdict":"use","note":"no source for the claim that unpublished novelty claims are penalised"}
{"type":"practice","grade":"P","src":["S16","S55"],"as_of":"2026-11-13","ttl":"V2","area":"interview","tactic":"Prepare a talk on your research and your vision","claim":"DeepMind's research phase and xAI's final round each include a talk or presentation","evidence":"employer pages","verdict":"use"}
{"type":"practice","grade":"P","src":["S48","S42"],"as_of":"2026-10-01","ttl":"V3","area":"applying","tactic":"If your record is engineering-led, apply to combined RE/RS or MTS postings first","claim":"Anthropic's advice, as quoted by a practitioner, is to apply as an engineer with an engineering background","evidence":"practitioner quoting Anthropic (C); roles-continuum paper","verdict":"use-with-care"}
{"type":"practice","grade":"P","src":["S2","S39"],"as_of":"2026-11-13","ttl":"V2","area":"interview","tactic":"Practise Python live coding without AI tools; follow each employer's stated AI rule","claim":"Anthropic interviews in Python and allows no AI in live interviews unless indicated","evidence":"employer posting and guidance","verdict":"use"}
{"type":"practice","grade":"P","src":["S7"],"as_of":"2026-11-13","ttl":"V1","area":"job search","tactic":"Check the posting date and deadline before applying","claim":"Eight DeepMind Greenhouse pages in the index carried passed deadlines, and the one fetched still loaded","evidence":"sample","verdict":"use"}
{"type":"practice","grade":"P","src":["S49","S59"],"as_of":"2026-11-13","ttl":"V1","area":"job search","tactic":"Treat hourly contract roles, and Research Scientist roles in quantitative or operations research, as outside AI research until the posting shows ML method work","claim":"One listing pairs the title with $100-120 an hour contract terms, and Amazon uses the title for quantitative roles","evidence":"Glassdoor snippet; Amazon postings","verdict":"use-with-care"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"AI-specific live posting count for Research Scientist from employers' own boards","searched":["JobsPipe research-scientist page","Fast AI Jobs role page","Glassdoor remote listing","ZeroG Talent listings"],"note":"platforms give shares, startups-only counts or other scopes; board-listing URLs were refused"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posting-volume trend since 2025-01-01","searched":["JobsPipe","Fast AI Jobs","web search"],"note":"no series; LCA filings are a proxy only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Employer-stated interview loops for OpenAI, Meta, NVIDIA and Microsoft Research","searched":["web search","openai.com (bot-blocked)"],"note":"DeepMind (undated page) and xAI found; Anthropic gave a Python statement and an AI-use policy"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Consultancy and IT-services Research Scientist postings beyond Accenture","searched":["one search covering Accenture, TCS, Deloitte, Capgemini and Infosys"],"note":"only Accenture applied-researcher postings surfaced"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"India posted pay bands for Research Scientist","searched":["9 India postings","Levels.fyi","vendor guides"],"note":"0 of 9 postings state a band"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Published analyses of prior roles of people hired as Research Scientists","searched":["NBER and BFI paper","AI roles continuum paper","DeepMind page"],"note":"only one DeepMind statement on an undated page, and academia-to-industry flow data"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Employer statements on certifications for this role","searched":["12 full-text postings","snippets of 33 more"],"note":"none named"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Named hiring-manager statements on proof of work","searched":["web search"],"note":"posting text, DeepMind's page and practitioner guides only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Behavioural skills c1-c4 in postings","searched":["12 full-text postings"],"note":"not stated"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Chinese, Japanese and Korean employers' Research Scientist postings","searched":[],"note":"not sampled"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Apple, Samsung, Qualcomm, Adobe and Salesforce research postings","searched":[],"note":"not searched"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Apex / Named Frontier Researcher alias and pay","searched":["web search"],"note":"no source"}
```
