---
id: "T0-44"
title: "Pay Refresh: US, Canada, UK, Europe, Israel, Singapore, the Gulf, Japan and Australia"
date: "2026-11-11"
status: complete-with-gaps
topic: "pay-us-uk-europe-singapore-gulf"
tags: ["compensation", "pay-benchmarks", "negotiation", "equity", "lca", "frontier-labs", "pay-transparency"]
informs_decisions: ["D-003"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic) in Claude.ai with web search and page fetch. Conflict of interest: Anthropic, the developer, is an employer in scope; rows on Anthropic pay, equity and IPO are marked COI."
evidence_window: "2025-07-17 to 2026-11-12"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 25
---

# T0-44: Pay Refresh: US, Canada, UK, Europe, Israel, Singapore, the Gulf, Japan and Australia

This report tests 25 knowledge-base claims (K1–K25) and widens the pay evidence outside India. Sources are cited as S1, S2 and so on, from the ledger. Grades follow EGP-1.0: A is a primary page I opened, B a transparent dataset or established secondary source, C attributed third-party or single-source material, D memory or judgement, M my arithmetic from stated inputs, E absent or untraceable. The brief's anchor is 2026-11-11. Retrieval ran on 2026-11-13, and several Levels.fyi pages carry 2026-11-12 timestamps, so every figure carries its own "as of" date. Amounts are nominal local currency with no exchange rates applied, so cross-country comparisons use same-currency ratios. "TC" means base plus annualised stock plus bonus. Posted ranges and visa filings are base only.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | The US ML Engineer median TC on Levels.fyi is about $280K, with p25–p75 near $200K–$390K | 80% | D |
| P2 | The AI Engineer title earns about half the ML Engineer title in TC, but posted base ranges are close | 65% | D |
| P3 | Frontier labs pay 2–4× the US ML median, and 60–70% of that is equity | 70% | D |
| P4 | UK ML engineer TC is near £100K, and frontier-lab London base pay is above the UK p90 | 60% | D |
| P5 | Among Germany, the Netherlands, France and Switzerland, Switzerland pays most and France least | 65% | D |
| P6 | Posting transparency jumps only when a disclosure law takes effect (Ontario, Italy) | 60% | D |
| P7 | Gulf employers concede less in negotiation than US employers, because of expatriate labour supply | 50% | D |

## Research Question

**Decision.** What do GenAI roles pay in the listed places, by role, level, city and employer type, and what does the evidence say about negotiating pay by region? This informs D-003, `pay-benchmarks.md`, `negotiation-playbook.md` and `role_scores.json`.

**Reading applied.** "GenAI roles" means the 29 role IDs. Data exist only for a few title families (ML Engineer, AI Engineer, Forward Deployed Engineer, Applied AI Engineer, MLOps, Research Scientist and Research Engineer). The rest go under Absences. For each place I report the software-engineer (SWE) baseline plus an AI or ML title where one exists. India, freelance rates and EU-directive law are out of scope; for the directive I report only whether postings carry ranges.

**Method.** 33 searches and 31 pages opened; one further page was blocked by bot detection and I did not work around it. Levels.fyi's `.md` pages carry sample sizes and the HTML pages do not, so I used `.md` wherever the URL surfaced in search. Employer postings: five Anthropic London postings and one OpenAI posting were opened at the employer's own page, and further OpenAI postings were read as snippets on venture-capital job-board mirrors of its feed. Other sources: posted-range corpora, third-party LCA aggregators, recruiter guides, news and one field experiment.

**Falsification searches.**
- K3: I looked for evidence that AI Engineer posted pay equals ML Engineer pay, and found a 5–12% gap (S19, S20).
- K7: I looked for a systems premium inside OpenAI filings and found none between "AI Systems Engineer" and "Software Engineer" titles (S23).
- OpenAI equity: a relay attributes $865K per employee to The Information (period not stated) against the WSJ's $1.5M for 2025 (S28).
- UAE negotiation: relays conflict at 43%, 49% and 15% (S35).
- K9: I looked for evidence that salary-history bans are rare, and found 18–20 states plus DC with bans, no federal ban (S68).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | US ML Engineer TC median is $286,958 (p25 $200,000; p75 $389,850; p90 $497,500), 1.44× the US SWE median of $200,000 (M). The AI Engineer title sits at 0.54–0.56× ML at p25–p90 (M). FDE median is $205,000, Applied AI Engineer $250,000 and MLOps $145,200, all with wide spreads. | Levels.fyi 2026-11-11, n=1,027 (ML) and n=46,545 (SWE) [S1, S3, S16] | B |
| KF2 | Posted-range corpora report the top of the posted band, not base midpoints. ML ceilings: junior $180K, mid $211K, senior $241K, principal $300K. AI-engineering ceilings run 5–12% below ML (M). Equity is mentioned in 14% of AI and 26% of ML postings, but the source's level splits are internally inconsistent. | Axial Search, 13,776 and 43,480 US postings, Jan–Oct 2026 [S19, S20] | B (salary) / C (equity mentions) |
| KF3 | AI-focused engineers earn more than non-AI peers by 6.2% (Entry), 11.9%, 14.2% and 18.7% (Staff). Research roles had the fastest US pay growth in 2025 (+15.38%). The all-company SWE ladder is $155K, $226K, $312K, $457K, $551K, with steps ×1.46, ×1.38, ×1.46 and ×1.21 (M). | Levels.fyi blog 2025-07-17; 2025 pay report [S14, S15] | B |
| KF4 | Frontier-lab company medians are 2.1× (OpenAI $600K) to 3.1× (Anthropic leaderboard $882,500) the US ML median (M). OpenAI L5 is $932,917, with stock about 64%. New senior OpenAI offers median $730K against Microsoft's $280K, with stock 60%. | Levels.fyi OpenAI n=248, 2026-11-01; leaderboard 2026-11-11 [S3, S17, S62] | B/C (COI on Anthropic) |
| KF5 | The liquidity regime changed. OpenAI: average stock-based comp about $1.5M per employee in 2025, a $6.6B tender in Oct 2025, a $7B buyback at $852B in Aug 2026, and a confidential IPO filing in June 2026. Anthropic: public S-1 on 2026-10-26, roadshow from 2026-11-10 at $70–78 for 825M shares, lock-up up to 180 days and staged. Pricing is expected on 2026-11-18, which Anthropic has not confirmed. | [S27, S28, S29, S30, S31] | B/C (COI) |
| KF6 | LCA wages are filed base floors, not pay. OpenAI OpCo FY2025: 101 certified LCAs, median lower-bound wage $285,000. Title medians: Research Scientist $360K (n=188), Research Engineer $335K (n=84), SWE $255K (n=411). Anthropic MTS wages span $133,952 to $1,380,000 within one title. Market ML-engineer titles FY2025: median $179,982 (n=3,745). | Third-party aggregators of DOL data [S22–S26] | B |
| KF7 | UK ML TC median is £104,887 (n=114; p25 £80,210; p75 £156,733; p90 £213,619), 1.17× UK SWE (£90,039) (M). Robert Half London ML base median is £99,750. Anthropic London postings (COI; five opened): Research Engineer bands £260,000–£630,000 (three postings) and £375,000–£640,000, Applied AI Engineer £225,000–£240,000. The bands span internal levels, and the lowest floor is above the UK ML p90 TC. | [S2, S4, S38, S59] | B/A (COI) |
| KF8 | SWE TC medians, Nov 2026: Switzerland CHF 134,226, Ireland €105,072, Netherlands €95,634, Germany €85,121, France €61,045. ML-title medians are 1.24–1.34× the national SWE median (M). Poland: a Michael Page Warsaw ML-engineer posting lists PLN 263,000–329,000 a year, and a Devire report (relay) gives senior AI engineers PLN 25,000–35,000 gross a month. Sweden has no usable data. | Levels.fyi, n=617–2,947 [S5, S9–S12]; [S69, S70] | B/C |
| KF9 | Canada SWE CA$136,907 (Vancouver 186,120). Singapore SWE SGD 114,974, with ML-title SGD 151,000. Japan SWE ¥8,413,533, and Morgan McKinley Tokyo ML base ¥6.0M/8.0M/12.0M. Australia SWE A$152,290, Robert Half Sydney AI Engineer A$185,300 median, Hays A$145K–200K+. | [S6–S8, S13, S39–S41] | B/C |
| KF10 | Israel: GenAI developers averaged NIS 46,755 a month in H1 2025, and researcher offers reach NIS 50,000–90,000 a month plus options. UAE (Michael Page 2026): GenAI Engineer/MLOps AED 30–45K a month, Head/Director of AI AED 70–120K. Saudi figures are relay-only. | [S32, S33, S34, S37] | C |
| KF11 | Pay appears in postings at very different rates (Indeed Hiring Lab, mostly Q2 2026): UK 58–60%, Netherlands 49.5%, France 43%, Ireland 34–39%, Germany 12–14%, Italy 61% in July 2026, Ontario 71% (49% before its law), Canada 57%, US 49%, Japan 97% on Indeed but 14% on another feed, Australia 19%, Singapore 10%. Swedish ads often say pay is "according to agreement". | Indeed Hiring Lab [S43–S45]; [S70] | B/C |
| KF12 | In a field experiment on about 3,858 Levels.fyi tech job seekers, 61% of an encouraged group countered against 54% of controls. Those who countered gained 12.45% (about $27,000 a year). About 40% of offers were verbal. Levels.fyi coaching clients report +21–24%, but they are self-selected. The US has no federal salary-history ban, but 18–20 states plus DC bar the question and 13 states require ranges in postings as of 2026-07-01. Outside the US the evidence is thin and conflicting. | [S14, S35, S46, S57, S58, S68] | B/C |
| KF13 | Tool statuses: Forge closed into Schwab on 2026-03-02. EquityZen closed into Morgan Stanley on 2026-01-27. The Capbase exit calculator launched on 2026-04-08. Autograph Fair Offer is listed on Product Hunt. The "14% of 43,480 postings mention equity" figure belongs to Axial, not Comprehensive.io. | [S20, S47–S53] | B/C |
| KF14 | Gaps: relocation for GenAI hires has only generic US survey evidence plus a stated "relocation assistance" line in OpenAI postings. Six of the first twelve roles lack two US sources. AI-generated aggregator pages contaminate search results and were not used. | [S55, S61, S66] | C/E |
| KF15 | OpenAI San Francisco engineering and research postings (n=9, Jan–May 2026) list base bands from $230K to $460K, with a median band midpoint of $339K (M) and "offers equity" with no amounts. Its posting note says research and engineering hires share the internal title Member of Technical Staff. Aggregated OpenAI postings (n=570) have a median midpoint of $308K. | OpenAI careers page opened [S65]; mirrors [S66]; aggregate [S67] | A/B |

## Recommendation

| # | Decision rule | Failure mode | What would change it |
|---|---|---|---|
| R1 | Price offers against Levels.fyi percentiles for the exact title, level and country, using p25–p75 rather than the median. Cross-check with the country SWE median times the title ratio (US 1.44, CH 1.34, SG 1.31, NL 1.28, FR 1.24, UK 1.17, all M). | Title medians rest on unseen n and big-employer skew. | Published n per title, or a new dataset. |
| R2 | Read posted bands as base ranges that span levels. OpenAI lists $293K–$385K for one Staff/Senior Staff role, and Anthropic London lists £260K–£630K for research engineers. Ask which part of the band your level maps to, and ask in writing for equity form, vesting and refreshers, since only 14–26% of postings mention equity. | Bands are wide, and recruiter reposts may inflate samples. | Disclosure rules that cover equity or levels. |
| R3 | For frontier-lab offers value equity under three cases (last round, IPO range, 50% haircut). Ask about vesting, tender eligibility, hold periods and lock-up. Re-run after Anthropic prices. | Paper value is not liquid value, lock-ups run to 180 days or longer, and share-class terms vary. | IPO pricing and trading, or OpenAI's filing. |
| R4 | Get the offer in writing and counter once, naming components (level, base, sign-on, equity). Expect a gain near 12% (field experiment), not the 21–24% coaching headline. | "Best and final" markets, verbal offers, and a sample drawn from 2023–25 hiring. | A weaker or stronger market. |
| R5 | Match the tactic to the region. Gulf: ask for allowances, flights, schooling and end-of-service basis, since reported success on base is low. Israel: ask for sign-on and options. Japan: negotiate at offer stage. Germany and France: check the collective agreement and level first. UK, Ontario and BC: anchor on posted ranges. Sweden: expect no posted range. | Evidence is C/D and mostly relayed. | Michael Page's 2027 UAE guide, Hiring Lab updates, any outcome study. |
| R6 | For visa-dependent hires, treat an LCA wage as a floor. Ask which prevailing-wage level will be filed. | US visa rules may have changed; I did not verify them. | DOL or USCIS rule changes. |
| R7 | Ask for the relocation form (lump sum or managed move), tax gross-up and repayment terms in writing. Some postings state relocation assistance, but none gives amounts. | Evidence is generic US surveys. | Employer policy data. |
| R8 | Buy coaching only if you hold a competing offer. Prefer success-fee models. | Client results are self-selected, and discounting coaching by 80% did not raise negotiation attempts in the field experiment [S46]. | Independent outcome data. |

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| Use Levels.fyi alone | Rejected as sole source | Self-reported and skewed to large employers. Recruiter placements in London land close (£99,750 base against a £104,887 TC median), but Payscale-type sites differ widely. |
| Use posted ranges as base pay | Rejected | Axial reports the top of the band, and frontier-lab bands span several levels. |
| Use LCA as pay | Rejected | Base only, visa-sponsored only, and "Member of Technical Staff" hides seniority. |
| Use recruiter guides outside the US | Kept as cross-check | Undisclosed n, and several figures reach me through relays. |
| Value frontier equity at the last tender price | Rejected | IPO terms, lock-ups and conflicting averages ($1.5M against $865K) make the single price unsafe. |
| Skip negotiating in a weak market | Rejected | The field experiment found backlash rare, but it ran in 2023–25. Risk rises with "best and final" framing. |

## Detailed Findings

### 1. US pay by role and level

| Role ID | Segment | Statistic | Value | Basis | n · date | Src · grade |
|---|---|---|---|---|---|---|
| ml-engineer | all levels | p25 / p50 / p75 / p90 | $200,000 / $286,958 / $389,850 / $497,500 | TC | 1,027 · 2026-11-11 | S1 · B |
| ml-engineer | IC junior / mid / senior / principal | median top of posted band | $180K / $211K / $241K / $300K | base ceiling | 13,776 postings · Jan–Oct 2026 | S19 · B |
| ml-engineer | manager / director | same | $234K / $279K | base ceiling | same | S19 · B |
| ml-engineer | LCA titles, FY2025 | p25 / p50 / p75 / p90 | $145,000 / $179,982 / $215,000 / $250,000 | base filed | 3,745 · FY2025 | S24 · B |
| ai-engineer | all levels | p25 / p50 / p75 / p90 | $110K / $155K / $212K / $280K | TC | n and date not shown | S16 · B |
| ai-engineer | SF Bay Area | p25 / p50 / p75 / p90 | $170K / $225K / $309K / $459,980 | TC | n/s · 2026-06-15 | S16 · B |
| ai-engineer | IC junior / mid / senior / principal | median top of band | $170K / $200K / $213K / $270K | base ceiling | 43,480 · Jan–Sep 2026 | S20 · B |
| ai-engineer | AI/ML-engineer LCA titles | median lower bound | $165,350 (FY2025); $169,000 (FY2026 Q1–Q3) | base filed | 3,816; 4,459 | S22 · B |
| forward-deployed-engineer | all levels | p25 / p50 / p75 / p90 | $172K / $205K / $277K / $350K | TC | page updated 2026-09-08 | S16 · B |
| forward-deployed-engineer | posted, AI startups | median (range) | $180,656 ($75K–$375K) | base | 164 | S21 · B |
| research-engineer | OpenAI MTS (Research Engineer), LCA | median (min–max) | $335K ($210K–$530K) | base filed | 84 | S23 · B |
| research-engineer | OpenAI SF postings titled Research Engineer (4) | band midpoints | $345K–$420K (median $391K, M) | base band | Jan–Mar 2026 | S66 · B |
| applied-ai-engineer | all levels | p25 / p50 / p75 / p90 | $200K / $250K / $475K / $605K | TC | date not shown | S16 · B |
| ai-infrastructure-engineer | OpenAI MTS (AI Systems Engineer), LCA | median (min–max) | $252,500 ($170K–$460K) | base filed | 187; title mapping uncertain | S23 · B |
| research-scientist | OpenAI MTS (Research Scientist), LCA | median (min–max) | $360K ($178,006–$685K) | base filed | 188 | S23 · B |
| research-scientist | OpenAI posting, Researcher, Agent Post-Training | band | $250K–$380K | base band | 2026-05-23 | S66 · B |
| research-scientist | "AI Researcher" title | p25 / p50 / p75 / p90 | $56K / $172K / $340K / $490K | TC | wide spread, small n | S16 · B |
| research-scientist | new-hire equity, P6 / M6 | median | $4.09M / $4.72M | equity grant | Aug 2026 | S49 · C |
| applied-scientist | Amazon Applied Scientist | L4 to L7; median package | $245K to $653K; $335K (median reported $306,000) | TC | date not shown | S18 · B |
| ml-platform-engineer | "Machine Learning Ops Engineer" title | p25 / p50 / p75 / p90 | $120K / $145,200 / $200K / $295K | TC | page updated 2026-10-11 | S16 · B |

One US source only for applied-scientist, ml-platform-engineer and applied-ai-engineer. No US pay records for inference-engineer, agentic-ai-engineer or ai-product-manager (see Absences).

**US cities (SWE TC medians, Levels.fyi 2026-11-11, S3):** SF Bay Area $300,000; Seattle $257,600; New York $215,900; Austin $200,000. Boston is not listed. Posted ML ceilings by state: California $257K, New York $245K, Washington $226K (S19). AI-engineering ceilings: California $240K, Washington $230K (S20). OpenAI postings: San Francisco median midpoint $308K (n=497) against New York $247K (n=22), all roles, base only (S67 · C).

### 2. Observed employer postings (base bands)

| Employer (type) | Title | Location | Posted | Band | Src · grade |
|---|---|---|---|---|---|
| OpenAI (frontier lab) | Staff / Senior Staff Backend Engineer, B2B Flywheel (7+ years) | San Francisco | 2026-05-15 | $293K–$385K, offers equity | S65 · A |
| OpenAI | Software Engineer, Core Science | San Francisco | 2026-05-23 | $293K–$385K | S66 · B |
| OpenAI | Software Engineer, Ad Formats | San Francisco | not shown | $230K–$385K | S66 · B |
| OpenAI | Research Engineer, Speech & Realtime Models | San Francisco | 2026-02-17 | $295K–$445K | S66 · B |
| OpenAI | Senior Research Engineer/Scientist, Edge, Consumer Products | San Francisco | 2026-01-23 | $380K–$460K | S66 · B |
| OpenAI | ML Research Engineer, Hardware Codesign | San Francisco | 2026-01-13 | $230K–$460K | S66 · B |
| OpenAI | Research Engineer/Scientist, Human Alignment, Consumer Devices | San Francisco | 2026-03-13 | $380K–$445K | S66 · B |
| OpenAI | Researcher, Context, Agent Post-Training | San Francisco | 2026-05-23 | $250K–$380K | S66 · B |
| OpenAI | Research Scientist / Research Engineer, Early Career Cohort | San Francisco | 2026-03-20 | $295K (single figure) | S66 · B |
| Anthropic (frontier lab, COI) | Research Engineer, Pretraining Scaling; Science of Scaling; Machine Learning (Reinforcement Learning) | London | not shown | £260,000–£630,000 each | S59 · A |
| Anthropic | Research Engineer, RL Scaling Science | London | not shown | £375,000–£640,000 | S59 · A |
| Anthropic | Applied AI Engineer (4+ years, customer-facing) | London | not shown | £225,000–£240,000 | S59 · A |
| Anthropic | Applied AI Engineer, Beneficial Deployments | London | 2026-07-15 | £240,000–£255,000 | S21 · B |
| Anthropic | Research Engineer, Post-Training | London | not shown | £270,000–£340,000 | S59 · B |

The median band midpoint across the nine OpenAI engineering and research postings is $339K (M), against a Levels.fyi OpenAI L5 base of $335,000 (S17). Non-engineering OpenAI postings (a recruiter at $216K–$240K and a compensation analyst at $234K–$260K) are excluded. The Anthropic bands are 2.4× wide, and the postings say required years of experience "will correlate with the internal job level", so one band covers several levels. OpenAI's postings say they offer equity without amounts. The opened Anthropic postings state only the base band, and one Anthropic posting seen as a snippet says the total package includes equity and may include incentive pay. OpenAI's posting note says research and engineering hires share the internal title Member of Technical Staff.

### 3. Employer-type packages

| Type | Employer | Package evidence | Equity form and liquidity | Src · grade |
|---|---|---|---|---|
| Frontier lab | OpenAI | SWE median $600K (n=248; 2026-11-01); L2 $249K (base $169K) to L7 $1.89M; L5 $932,917 (base $335,000, stock $597,917); leaderboard median $640K; new senior offers $730K (stock $435K, 60%); posted bases $230K–$460K | RSU with 4-year vesting on Levels.fyi (an older snapshot showed PPU); $6.6B tender in Oct 2025 (more than 600 sellers, about 75 at the $30M cap, two-year hold reported); $7B buyback at $852B in Aug 2026; average stock comp $1.5M per employee in 2025 | S3, S17, S27, S28, S62, S66 · B/C |
| Frontier lab | Anthropic (COI) | SWE median $570K–$582.5K (Apr 2026 snapshot) and $882,500 on the 2026-11-11 leaderboard; Senior $550K (base $318K, stock $233K); Lead $759K; Staff about $1.25M, about $843K of it equity (relay); London posted bases £225K–£640K | 4-year vesting; 10-for-1 split 2026-09-17; IPO range $70–78; lock-up up to 180 days, some staged to a year; April 2026 tender at $350B pre-money (low-grade relays) | S3, S17, S29–S31, S59, S62 · B/C |
| Frontier lab | xAI | ML L4 Palo Alto $690K (base $290K, stock $400K), one package, 2026-01-30 | not found | S18 · C |
| Big Tech | Nvidia | ML median $261K; IC1 $205K, IC3 $292K, IC4 $331K (2026-06-30); Germany SWE median €189,905 | RSU | S5, S18 · B |
| Big Tech | Meta, Amazon, Microsoft, Google | Meta ML E4 $303–331K, E5 $472–497K, E6 $660–790K (two snapshots, undated); Amazon ML L5 $270K, L6 $401K; Amazon Applied Scientist L4 $245K to L7 $653K; Microsoft levels 61–62 $216–229K; Google FDE median $292K | RSU | S18 · B |
| AI-native startup | Scale AI, Cohere, Mistral AI | Scale AI ML median TC $178,100, L3 $195K, L4 $254K (2026-07-01); Cohere top ML package CA$366,059; Mistral AI SWE median €110,643 | Startup equity grants for AI/ML engineers rose 59% between Jan 2024 and Feb 2026 (Carta, via relay); Pave: new-hire equity dominates, base compressed | S12, S18, S49 · B/C |
| Enterprise | Salesforce, LinkedIn, Pinterest, Bosch, TD | Salesforce Senior MTS ML $308K; LinkedIn ML IC2 $246K to IC5 $690K; Pinterest IC13–IC16 $226K–$686K (2026-05-16); Bosch ML Germany €85.6K; TD ML Toronto CA$135K (single) | Equity is mentioned in 26% of ML postings overall | S18, S19 · B/C |
| Consultancy | none found | | | Absence |

### 4. LCA filings (base wage filed; not what people earn)

| Employer or population | Scope | Certified LCAs | Wage statistic | Period | Src · grade |
|---|---|---|---|---|---|
| OpenAI OpCo, LLC | all titles | 101; 210 | median lower bound $285,000; $260,000 | FY2025; FY2026 to Q3 | S22 · B |
| OpenAI OpCo | MTS (Software Engineer) | 411 | $255,000 (min $170,000; max $490,000) | FY2023–FY2026 | S23 · B |
| OpenAI OpCo | MTS (Research Scientist) / (Research Engineer) | 188; 84 | $360,000; $335,000 | same | S23 · B |
| OpenAI OpCo | MTS (Research & AI Systems) / (AI Systems Engineer) / untitled MTS | 75; 187; 174 | $370,000; $252,500; $310,000 | same | S23 · B |
| OpenAI OpCo | one record, SOC 15-1221 | 1 | offered $400,000 (range $400K–$600K) against a prevailing wage of $179,837 | FY2025 | S25 · B |
| OpenAI, INC. (older entity) | MTS | 9 | median $120,000 | 2016–17 | S23 · B |
| Anthropic, PBC (COI) | all titles | 292 | MTS from $133,952 to $1,380,000 (two above $1M); average prevailing wage $167,564 | FY2025–FY2026 to Q3 | S22, S23, S26 · B/C |
| All employers | titles matching "machine learning engineer" | 3,745 | median $179,982; mean $182,461 | FY2025 | S24 · B |
| All employers | AI/ML engineer family | 3,816; 4,459 | median lower bound $165,350; $169,000 | FY2025; FY2026 to Q3 | S22 · B |

Reading rules: the wage is an offered base at or above the prevailing wage; the aggregators differ in statistic (lower bound against title median); "Member of Technical Staff" hides seniority. I did not open DOL files, so these are B, not A.

### 5. Pay by place (non-US)

#### Canada (Toronto, Vancouver, Montreal)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90) | CA$136,907 (102,914–185,466; 236,410) | 5,338 · 2026-11-03 | S7 · B |
| SWE city medians: Vancouver / Toronto / Montreal | CA$186,120 / 140,269 / 121,755 | 2026-11-03 | S7 · B |
| Title medians: FDE; Research Scientist | CA$186,280; CA$177,575 | 2026-11-03 | S7 · B |
| ML, company pages: Shopify; Layer 6 | CA$230K (2026-02-28); CA$208K (2026-07-22) | small n | S18 · B |

#### United Kingdom (London, Cambridge)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| ML engineer TC p25 / p50 / p75 / p90 | £80,210 / £104,887 / £156,733 / £213,619 | 114 · 2026-11-12 | S2 · B |
| SWE TC median; London; Cambridge | £90,039; £105,271; £117,192 | 4,743 · 2026-11-11 | S4 · B |
| ML base, London (placement-based): 25th / 50th / 75th | £79,750 / £99,750 / £126,250 | n and date not shown | S38 · C |
| Title medians: FDE; Research Scientist | £139,550; £129,774 | 2026-11-11 | S4 · B |
| Anthropic London posted bases (COI) | Research Engineer £260,000–£640,000 across four opened postings; Applied AI Engineer £225,000–£255,000 | postings, 2026 | S59, S21 · A/B |
| Advertised ML median, London (history: six months to 2025-05-05) | £97,500 | | S63 · C |

#### Ireland (Dublin)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Dublin | €105,072 (78,346–141,197; 169,145); €110,408 | 1,161 · 2026-11-11 | S10 · B |
| Company medians: Meta; Stripe | €191,627; €166,172 | 2026-11-11 | S10 · B |
| ML engineer | no figure found | | Absence |

#### Germany (Berlin, Munich)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90) | €85,121 (70,692–102,640; 126,054) | 2,947 · 2026-11-11 | S5 · B |
| Berlin; Munich | €93,539; €80,623 | 2026-11-11 | S5 · B |
| Nvidia SWE; HPC title | €189,905; €116,110 | 2026-11-11 | S5 · B |
| ML, Berlin metro (older snapshot; displayed in USD) | median $97,683 (p25 $86.7K; p75 $106K) | n/s · 2025-07-25 | S18 · B |

#### Netherlands (Amsterdam)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Amsterdam | €95,634 (73,898–131,136; 163,452); €105,747 | 1,403 · 2026-11-11 | S11 · B |
| Title medians: ML; FDE | €122,301; €135,510 | 2026-11-11 | S11 · B |
| Pay frequency | about 13 instalments a year | | S11 · B |

#### France (Paris)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Paris | €61,045 (47,046–77,325; 103,959); €90,546 | 1,106 · 2026-11-12 | S12 · B |
| Title median: ML; company: Mistral AI SWE | €75,458; €110,643 | 2026-11-12 | S12 · B |

#### Switzerland (Zurich)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Zurich | CHF 134,226 (106,969–192,643; 279,831); CHF 209,499 | 617 · 2026-11-11 | S9 · B |
| Title medians: ML; FDE | CHF 179,235; CHF 172,655 | 2026-11-11 | S9 · B |
| Pay frequency | usually 13 instalments a year | | S9 · B |

#### Sweden (Stockholm)
No usable pay record. A Stockholm Academic Work ad received through Arbetsförmedlingen gives pay as "enligt avtal" (according to agreement), so postings often carry no range (S70 · C). Modelled aggregator pages gave figures but are not traceable to data and were not used (S61).

#### Poland (Warsaw)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| ML engineer, Warsaw, permanent, posted by Michael Page | PLN 263,000–329,000 a year; gross or net not stated | one posting · 2026 (reference suggests June) | S69 · B |
| Senior AI engineer, employment contract, gross monthly (Devire report, relayed) | PLN 25,000–35,000; Lead/Principal PLN 32,000–45,000 | date not shown | S69 · C |
| Contract mix, Just Join IT offers | 62.1% B2B contracts, 32% employment contracts | date not shown | S69 · C |

Levels.fyi's AI Engineer Poland `.md` (2026-06-02) shows a PLN 49,505 median that cannot be annual pay, so I did not use it (S61).

#### Israel (Tel Aviv)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| GenAI developers, average monthly salary; algorithm experts without GenAI | NIS 46,755; NIS 42,255 (+10.6%, M) | GotFriends H1 2025 | S32 · C |
| AI researcher offers, monthly gross, plus options | NIS 50,000–90,000 | industry sources · 2026-09-17 | S33 · C |
| AI team management roles, monthly | NIS 60,000–80,000, often with sign-on | 2025 | S32 · C |
| Data scientists TC, Levels.fyi as read by Globes: Meta; Nvidia | about NIS 974,000; about NIS 945,000 a year | 2026-09-17 | S33 · C |

#### Singapore
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90) | SGD 114,974 (85,540–165,006; 216,301) | 1,360 · 2026-11-12 | S6 · B |
| ML engineer title median | SGD 151,000 (1.31× SWE, M) | 2026-11-12 | S6 · B |
| Pay frequency; top companies | usually 13 instalments; Meta SGD 256,240, Grab SGD 196,911 | 2026-11-12 | S6 · B |

#### UAE (Dubai, Abu Dhabi)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| GenAI Engineer / MLOps; AI Product Manager (per month, base) | AED 30,000–45,000 each | 2025-11-19 | S34 · C |
| Head / Director of AI (per month) | AED 70,000–120,000 | 2025-11-19 | S34 · C |
| AI engineering pay change in 2025 | +4–6% | | S34 · C |

The period is monthly, inferred from the USD equivalents in the relay. I did not open the Michael Page guide. A 2027 guide launched on 2026-10-27 (S36). I found no separate Abu Dhabi figures.

#### Saudi Arabia (Riyadh)
Cooper Fitch figures, relayed by an unverified site (S37): junior ML SAR 20,000–28,000 a month, senior SAR 42,000–62,000. Grade D, not traced to the guide.

#### Japan (Tokyo)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Tokyo | ¥8,413,533 (6,560,187–11,730,848; 16,868,633); ¥8,980,325 | 384 · 2026-11-05 | S13 · B |
| ML engineer, Tokyo, base (low / mid / high), excluding bonus | ¥6,000,000 / ¥8,000,000 / ¥12,000,000 | 2026 guide, placement-based | S41 · C |
| AI-related roles, candidate-reported | ¥6M and above | 4,548 respondents · Jun 2025–May 2026 | S42 · C |

#### Australia (Sydney)
| Item | Value | n · date | Src · grade |
|---|---|---|---|
| SWE TC median (p25–p75; p90); Sydney | A$152,290 (114,915–190,474; 243,743); A$162,228 | 1,590 · 2026-11-04 | S8 · B |
| Atlassian; Canva SWE medians | A$312,176; A$268,723 | 2026-11-04 | S8 · B |
| AI Engineer, Sydney, base (25th / 50th / 75th; order assumed) | A$163,500 / A$185,300 / A$212,550 | n not stated | S39 · C |
| AI Engineer, Australia, salary range | A$145,000–200,000+ | Hays, 2026-04-30 | S40 · C |
| ML engineer, Sydney, average base (broad crowdsourced) | A$93,528 | | S60 · C |

### 6. Best source per place and its bias

| Place | Best available source | Bias |
|---|---|---|
| US | Levels.fyi ML title (n=1,027); employer postings; LCA for floors | Self-reported, large-employer and senior skew; postings give bands across levels |
| Canada | Levels.fyi SWE (n=5,338) | No ML-title n; big-tech skew |
| UK | Levels.fyi ML (n=114) plus Robert Half placement base | Small n; Robert Half n undisclosed; base against TC |
| Ireland | Levels.fyi SWE (n=1,161) | Big-tech skew; no ML title |
| Germany | Levels.fyi SWE (n=2,947) | Nvidia and Google skew; collective-agreement pay under-represented |
| Netherlands | Levels.fyi SWE and ML title | Title n unseen |
| France | Levels.fyi SWE (n=1,106) | Tech-company skew |
| Switzerland | Levels.fyi SWE (n=617) | Small n; Meta and Google skew |
| Sweden | none | Ads often give no pay; modelled sites untraceable |
| Poland | Michael Page posting; Devire relay | Gross or net unstated; B2B and employment contracts are not comparable |
| Israel | GotFriends via Globes | One agency; monthly gross; no equity |
| Singapore | Levels.fyi SWE (n=1,360) | Big-tech skew; no negotiation data |
| UAE | Michael Page 2026 via Arabian Business | Relay; ranges; guide not opened |
| Saudi Arabia | none reliable | Relay of unverified origin |
| Japan | Morgan McKinley Tokyo base; Levels.fyi (n=384) | Base only against TC; foreign-firm skew |
| Australia | Levels.fyi SWE (n=1,590); Robert Half Sydney | Robert Half ordering assumed; Payscale is a different population |

### 7. Do postings carry ranges?

| Place | Share of postings with pay | Date · source |
|---|---|---|
| UK | 56% (Mar 2026), 58% (Q2), 60% (Jul); high of 64% in early 2025 | S43 · B |
| Netherlands; France; Ireland; Germany | 48–49.5%; 43%; 34–39%; 12–14% | S43 · B |
| Italy | 61% in Jul 2026, from 35% in Jan, after June implementation | S43 · B |
| Ontario; Canada; rest of Canada | 71% (49% before its law); 57%; 41% | Jun 2026 · S44 · B |
| US | 49%; 13 states require the range in the posting as of 2026-07-01 | Jun 2026 · S44, S68 · B/C |
| Japan | 97% (Indeed), against 14% (fantastic.jobs): sources conflict | S44, S45 · B/C |
| Australia; Singapore | 19%; 10% | Feb–Apr 2026 · S45 · C |
| Poland; Sweden | Polish boards show ranges on many postings (62.1% of Just Join IT offers are B2B); Swedish ads often say "according to agreement". Shares not measured. | S69, S70 · C |

### 8. Ladders and steps

- US SWE median TC by level, all companies (Levels.fyi 2025): Entry $155K, Engineer $226K, Senior $312K, Staff $457K, Principal $551K. Steps are ×1.46, ×1.38, ×1.46 and ×1.21 (M) [S14].
- AI premium over non-AI peers: 6.2%, 11.9%, 14.2% and 18.7%, Entry to Staff [S15].
- OpenAI runs L2 to L7: total $249K at L2, $336K at L3, $932,917 at L5, $1.89M at L7. L2 is typically 0–1 years and L3 2–3 years [S17]. OpenAI uses "Staff / Senior Staff" in postings as an external signal of seniority over the shared internal title Member of Technical Staff [S65].
- Anthropic ladder (relay of Levels.fyi): Entry about $367K, Senior $591K, Lead $780K, Staff about $1.25M [S62].
- Pave (relay): ML engineering median base $321K at P6 and $347K at M6; AI/ML turnover 21.8% against 16.8% for software engineering [S49]. Pave's H1 2026 promotion rate is 8.6% [S48].
- Anthropic postings say required years of experience "will correlate with the internal job level", so the title does not carry the level [S59]. I found no published map from GenAI titles to levels.

### 9. Negotiation by region

| Region | Norm | Evidence | Grade |
|---|---|---|---|
| US | Counter once. About 42% of candidates counter, and about 85% of those get something (Fidelity, cited in the paper). Counters gained 12.45% on average in a 3,858-person tech sample. About 40% of offers were verbal. "Best and final" framing rose from May 2025. No federal salary-history ban; 18–20 states plus DC bar the question for private employers (Virginia from 2026-07-01), and 13 states require ranges in postings. | NBER w33903 via UCLA Anderson [S46]; Levels.fyi coaching +21–24%, self-selected [S14]; law-firm and HR summaries [S68] | B / C |
| Canada | Employers are more open than candidates assume. Ontario and BC postings give anchors. | McGill, 2026-02-09 [S56]; Ontario 71% of postings [S44] | C |
| UK | No posting mandate, but 56–60% of postings show pay. 67% of HR directors report more willingness to negotiate. | Robert Half UK [S57]; Indeed [S43] | C |
| Continental Europe | In Germany, collective agreements keep posting transparency near 12–14%. 49% of European candidates negotiate (undated). Works councils, notice periods and counter-offers: not sourced. | [S43, S64] | C/D |
| Poland, Sweden | Polish ads commonly show ranges and a B2B or employment-contract choice; Swedish ads often say pay is by agreement. No outcome evidence. | [S69, S70] | C |
| Israel | AI offers exceed stated bands, with sign-on up to six salaries and options. | Globes, 2025-07-20 [S32] | C |
| Singapore | 13th-month pay is customary. No negotiation outcome evidence found. | [S6, S45] | C |
| Gulf | Michael Page 2026: 43% negotiated, against 49% a year earlier (Khaleej Times), or 49% attempted and 15% succeeded (The National, Arabian Business). The relays conflict. Employers hold leverage. | [S35] | C |
| Japan | 74.5% of 393 IT engineers negotiated at job change, and 90.8% of them got a raise. Vendor survey. | [S58] | C |
| Australia | 97% of 500 employers would offer perks if pay expectations fall outside range. Employers' stated maximum uplift: 5% or less 16%, 6–10% 40%, 11–15% 29%, 16–20% 12%, over 20% 2% (table heading truncated in the extract). | Robert Half AU, 2026-02-24 [S57] | C |

### 10. Relocation

The evidence is generic US corporate surveys plus employer posting text. Atlas Van Lines' 59th survey (549 decision-makers, fielded 2025-12-15 to 2026-01-16; published 2026-04-16) and NEI's 2026 lump-sum survey show lump sums as common for new hires, mostly paid after the start date, with tax assistance in 81–91% of partial lump-sum programmes [S55]. OpenAI's San Francisco postings say it offers "relocation assistance to new employees" or that it "may be available", without amounts [S66]. Anthropic's postings say it sponsors visas and retains an immigration lawyer, but cannot sponsor every role, and its application form asks about relocation [S59]. I found no GenAI-specific evidence on amounts, flights, temporary housing or tax equalisation. Grade C.

### 11. Local package conventions

| Place | Convention | Source · grade |
|---|---|---|
| Switzerland, Singapore | 13 instalments a year usual | Levels.fyi [S9, S6] · B |
| Netherlands | about 13.0 instalments a year | Levels.fyi [S11] · B |
| Poland | Employment contract (UoP) or B2B contract; 62.1% of Just Join IT offers are B2B | [S69] · C |
| UAE | End-of-service gratuity under Federal Decree-Law 33/2021: 21 days' basic wage per year for the first five years, 30 days after, capped at two years' wage. Verify at u.ae. | Memory · D |
| Saudi Arabia | End-of-service award under Labor Law art. 84: half a month per year for five years, a month per year after. Verify at hrsd.gov.sa. | Memory · D |
| Israel | Mandatory pension (employer about 6.5% plus 6% severance, employee 6%); study fund customary. Verify with the Ministry of Labor. | Memory · D |
| Australia | Superannuation guarantee 12% from 2025-07-01. Verify at ato.gov.au. | Memory · D |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | US ML engineer $280K median (n=1,063); posted base $213–288K | updated | Median as of 2026-11-11 is $286,958, n=1,027. The posted figure is not reproducible: Axial's overall ceiling median is $197K. LCA is a floor ($179,982). [S1, S19, S24] | B |
| K2 | AI Engineer is 0.55–0.56× ML at every percentile | confirmed | Ratios 0.54–0.56 (M) from $110K/$155K/$212K/$280K against $200K/$286,958/$389,850/$497,500. The Google employer-mix half is untested. [S1, S16] | B |
| K3 | Posted base nearly identical across AI, infra and ML; FDE $180–248K | updated | AI ceilings are 5–12% below ML (M). FDE median $180,656 (n=164). Infra and platform not found. [S19, S20, S21] | B |
| K4 | Frontier labs about 3× US ML; equity 60% (OpenAI L5), 72% (Anthropic Staff) | updated | Company medians are 2.1–3.1× (M); OpenAI L5 is 3.3×. OpenAI stock share is 60–64%; Anthropic Staff about 67% (relay). [S1, S3, S17, S62] | B/C |
| K5 | SWE ladder $155K to $551K; steps ×1.38–1.46 | confirmed | Matches the 2025 report. The last step is ×1.21 (M). [S14] | B |
| K6 | AI premium 6.2% to 18.7% | confirmed | Exact, dated 2025-07-17. No 2026 refresh found. [S15] | B |
| K7 | Systems premium +13% to +31% in base, uncontrolled | updated | Eleven title–country pairs show +20% to +50% in TC (M). Inside OpenAI filings, AI Systems $252,500 against SWE $255,000. The Zurich guide was not reopened. [S4–S13, S23] | M |
| K8 | 80–87% of negotiators gain; coaching +21–24% self-selected | confirmed | About 85% got something (Fidelity, cited in the paper); the field experiment gives +12.45% among counterers. [S14, S46] | B/C |
| K9 | Counter once, in writing, 10–20% up; salary-history bans | confirmed | The 12.45% average supports the magnitude. About 40% of offers are verbal. No federal salary-history ban, but 18–20 states plus DC bar the question. [S46, S68] | B |
| K10 | Levels.fyi salary database: use | confirmed | `.md` pages give n and percentiles. April–July 2026 location pages show unit anomalies. [S1–S13, S16] | B |
| K11 | Levels.fyi coaching: use-with-care; +21/23/24% | confirmed | Exact in the 2025 report. 650 negotiations, about $40M total, so about $61.5K each (M). [S14, S46] | B |
| K12 | Rora: percentage of increase; self-reported outcomes | confirmed | The site states a percentage fee. The $2,250+ figure was not found. [S53] | B (COI) |
| K13 | Candor: watch; status unverified | unverifiable | No primary page found. Only an affiliate blog claims a 10–20% fee. [S54] | E |
| K14 | Doody book: use-with-care; no outcome data | stale | Only an affiliate mention of a $19 book. No outcome data found. [S54] | E |
| K15 | Comprehensive.io: 14% of 43,480 postings mention equity | updated | The 14% and 43,480 are Axial Search's figures. Comprehensive.io status unverified. [S20] | B |
| K16 | DOL LCA files: floor, not pay | confirmed | One record: offered $400K against a prevailing wage of $179,837. Anthropic MTS spans $133,952 to $1,380,000. [S22, S23, S25, S26] | B |
| K17 | Third-party LCA browsers differ | confirmed | Entity split (OpenAI, INC. at $120,000 in 2016–17 against OpCo) and statistic split (lower bound against title median). Untitled MTS median is $310,000. [S22–S25] | B |
| K18 | Broad crowdsourced sites are a different population | confirmed | Payscale Sydney ML average A$93,528 against Robert Half Sydney AI A$185,300. Glassdoor Israel labels monthly figures as annual. [S39, S60] | C |
| K19 | Recruiter guides: cross-checks only | updated | Robert Half London is placement-based. Michael Page UAE still reaches me by relay, and a 2027 guide exists. [S34, S36, S38, S39] | C |
| K20 | Pave: 6.5% promoted raise; +39% equity at promotion | updated | A newer report exists, giving 4.4% non-promoted AI/ML raises against 3.7% for R&D. The 6.5% and +39% were not found. [S47, S48, S49] | C |
| K21 | Carta: candidate programme status unverified | unverifiable | Relays cite 396 tenders in 2025 and +59% startup equity grants. Programme status not found. [S49] | C |
| K22 | Forge acquisition agreed; closing unverified | updated | Schwab completed it on 2026-03-02. [S50] | B |
| K23 | EquityZen acquisition agreed 2025-10-29 | updated | Morgan Stanley closed it on 2026-01-27. [S51] | B |
| K24 | Capbase exit calculator launched April 2026 | confirmed | Product Hunt launch 2026-04-08, free. [S52] | B |
| K25 | Autograph Fair Offer: existence unconfirmed | updated | Product Hunt lists Fair Offer launches on 2024-01-15 and 2025-05-10. Accuracy unvalidated. [S52] | C |

## Absences

| Item | Where I looked | Note |
|---|---|---|
| Two US sources by level for applied-scientist, inference-engineer, agentic-ai-engineer, ai-product-manager; a second source for applied-ai-engineer, ml-platform-engineer and ai-infrastructure-engineer | Levels.fyi title queries, Axial, Fast AI Jobs, Pave relays, LCA aggregators | Only Amazon Applied Scientist, Levels.fyi MLOps and Applied AI Engineer pages found; no inference, agentic or AI product manager dataset. |
| Roles 13–24 and leadership roles, US | Not searched individually | Only UAE AI Product Manager and Head of AI, and Axial manager and director ceilings. |
| ML-engineer city medians for Boston, Austin, Seattle, New York | Levels.fyi searches | Only SWE city medians surfaced. |
| US employer-posted ranges beyond OpenAI | Greenhouse and Ashby searches | One Anthropic page was blocked by bot detection and not retried; no Anthropic US posting was opened. Posting dates are not shown on the opened Anthropic pages. |
| LCA wage ranges for AI/ML titles at the top FY2025 filers (Amazon, Microsoft, Meta, Google, Apple) | Aggregator searches | DOL files not fetched; dol.gov is outside the session network allow-list. |
| ML or AI engineer pay with n for Ireland, Australia, Japan, Sweden, Saudi Arabia, Abu Dhabi; Poland beyond one posting and a relay | Levels.fyi, recruiter and news searches | Levels.fyi AI Engineer Poland `.md` median of PLN 49,505 cannot be annual pay and was not used. |
| Official statistics with an AI-specific occupation (ONS, MOM, ABS, MHLW, CBS Israel) | News and aggregator queries | MHLW information-and-communications average of about 6.3M JPY cited second-hand only. |
| Frontier-lab retention grants, refreshers and sign-on structures; Anthropic April 2026 tender details | News searches | Tender and IPO coverage only; April tender from low-grade relays. |
| Continental Europe negotiation norms: works councils, notice periods, counter-offers | One regional search | Only Hiring Lab and SHRM notes. |
| Singapore, Saudi and Australian negotiation outcomes; official Gulf end-of-service sources | Regional searches | None opened. |
| GenAI-specific relocation amounts (visa, flights, temporary housing, tax equalisation) | Relocation survey searches and posting text | Generic US surveys and "assistance offered" lines only. |
| Candor, Doody, Comprehensive.io, Carta candidate programme | Vendor searches | No primary page found or opened. |
| Robert Half Zurich guide; Michael Page UAE guides (2026, 2027) | Not reopened | K7 and K19 rest on relays. |

## Open Questions & Risks

- Anthropic's IPO pricing (expected 2026-11-18) and first trade (expected 2026-11-19) are unconfirmed by Anthropic; any change alters the equity rules (V0).
- Whether "Member of Technical Staff" filings map to role IDs is unresolved. My LCA-to-role mappings are labelled.
- The date and n of Levels.fyi's AI Engineer, FDE and Applied AI Engineer title pages are not shown in my extracts.
- The Axial pages contain internal inconsistencies, for example Principal IC equity at 33%, 45% and 35% on different lines. Use only the salary percentiles.
- I did not verify H-1B policy (fees, weighted selection). One aggregator claims 63.4% of LCAs are Level I–II.
- US state counts for salary-history bans differ between sources (18 or about 20 states plus DC), so treat the count as approximate.

**Strongest objections.**

| Objection | Evidence for and against |
|---|---|
| Levels.fyi overstates typical pay | For: Payscale and Glassdoor figures are far lower. Against: Robert Half London placement base (£99,750) sits near the Levels.fyi TC median (£104,887), and OpenAI posted bases (median midpoint $339K) sit near Levels.fyi L5 base ($335,000). Use percentiles. |
| Posted ranges overstate base | For: Axial states they are top-of-band, and Anthropic's bands span levels. Against: the ML mid ceiling of $211K sits above the LCA median of $180K, as a ceiling would. |
| LCA wages are floors | Supported by the prevailing-wage gap and by Anthropic's $134K–$1.38M span within one title. |
| Frontier equity averages are accounting, not cash | The $1.5M is stock-based compensation expense (a relay gives $865K). The S-1 coverage says its figures are not sums promised to employees. Tender caps and lock-ups limit liquidity. |
| Negotiation uplifts are survivor-biased | Coaching figures are self-selected. The field experiment (+12.45%) is less selected but ran in 2023–25. |
| Gulf and Israel figures are relays | Correct. Michael Page's guide was not opened and GotFriends data arrived through Globes. They stay at C. |

## Discovered Concerns

- Levels.fyi `.md` pages from April–July 2026 show currency-converted values that do not parse as annual pay (for example Japan AI Engineer ¥40,682, and Istanbul and São Paulo ML pages). The UK ML `.md` header says "Location: United States" while the body is UK. Use the November 2026 `.md` pages, which carry n.
- AI-generated aggregators dominate searches for city salaries and were not used (S61).
- Levels.fyi lists OpenAI stock as RSU with 4-year vesting, while an older snapshot said PPU. I did not verify the legal form of OpenAI equity.
- Scale AI's Levels.fyi ML figure moved between snapshots ($181,250 earlier; $178,100 median TC and $215K median package on 2026-07-01), which shows how small-n company pages drift.
- EquityBee's free Benchmark tool compares startup equity grants by department, seniority and stage. It is a candidate for the equity-data tool list (S52).
- Hays's Tech Talent Explorer covers 34 countries (S40) and the Michael Page UAE 2027 guide exists (S36). Both merit a refresh.
- Venture-capital job boards mirror OpenAI's posting feed with dates and bands (S66). They are a cheap way to refresh frontier-lab posted ranges, with the caveat that they are mirrors.
- PwC's 2025 AI Jobs Barometer figure of a 56% wage premium for AI skills (relayed in a Polish article) is cross-occupation and not comparable with Levels.fyi's software-engineer premiums. I did not check for a later edition.
- Italy's posting share rose from 35% to 61% in 2026 (S43). Posting-share rows go stale quickly (V1).

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | US ML median about $280K | Confirmed | $286,958; p25 $200,000; p75 $389,850 [S1] | None |
| P2 | AI Engineer about half of ML in TC, close in posted base | Updated | TC ratio 0.54–0.56; posted ceilings 5–12% lower, not equal [S16, S19, S20] | Adjust `role_scores.json` pay weights |
| P3 | Frontier labs 2–4× US ML, 60–70% equity | Updated | 2.1–3.1× at company level, 3.3× at OpenAI L5; equity 60–67% [S3, S17, S62] | Rewrite the K4 line |
| P4 | UK ML TC about £100K; London frontier base above p90 | Confirmed | £104,887; £225K–£640K posted bases against p90 £213,619 [S2, S59] | None |
| P5 | Switzerland highest, France lowest | Confirmed | SWE: CH 134,226, NL 95,634, DE 85,121, FR 61,045 (unconverted) [S5, S9, S11, S12] | None |
| P6 | Transparency jumps when laws take effect | Confirmed | Ontario 49% to 71%; Italy 35% to 61% [S43, S44] | Note V1 decay |
| P7 | Gulf employers concede less | Confirmed (weak) | 15% success or 43% negotiating, by relay [S35] | Keep at C |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Levels.fyi ML Engineer, US `.md` — https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer.md | 2026-11-11 | 2026-11-13 | B | Read | self-reported | K1, KF1 |
| S2 | Levels.fyi ML Engineer, UK `.md` — https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/united-kingdom.md | 2026-11-12 | 2026-11-13 | B | Read | self-reported | UK ML |
| S3 | Levels.fyi SWE, US `.md` — https://www.levels.fyi/t/software-engineer.md | 2026-11-11 | 2026-11-13 | B | Read | self-reported | US SWE, cities, leaderboard |
| S4 | Levels.fyi SWE, UK `.md` — https://www.levels.fyi/t/software-engineer/locations/united-kingdom.md | 2026-11-11 | 2026-11-13 | B | Read | | UK SWE, titles |
| S5 | Levels.fyi SWE, Germany `.md` — https://www.levels.fyi/t/software-engineer/locations/germany.md | 2026-11-11 | 2026-11-13 | B | Read | | Germany |
| S6 | Levels.fyi SWE, Singapore `.md` — https://www.levels.fyi/t/software-engineer/locations/singapore.md | 2026-11-12 | 2026-11-13 | B | Read | | Singapore |
| S7 | Levels.fyi SWE, Canada `.md` — https://www.levels.fyi/t/software-engineer/locations/canada.md | 2026-11-03 | 2026-11-13 | B | Read | | Canada |
| S8 | Levels.fyi SWE, Australia `.md` — https://www.levels.fyi/t/software-engineer/locations/australia.md | 2026-11-04 | 2026-11-13 | B | Read | | Australia |
| S9 | Levels.fyi SWE, Switzerland `.md` — https://www.levels.fyi/t/software-engineer/locations/switzerland.md | 2026-11-11 | 2026-11-13 | B | Read | | Switzerland |
| S10 | Levels.fyi SWE, Ireland `.md` — https://www.levels.fyi/t/software-engineer/locations/ireland.md | 2026-11-11 | 2026-11-13 | B | Read | | Ireland |
| S11 | Levels.fyi SWE, Netherlands `.md` — https://www.levels.fyi/t/software-engineer/locations/netherlands.md | 2026-11-11 | 2026-11-13 | B | Read | | Netherlands |
| S12 | Levels.fyi SWE, France `.md` — https://www.levels.fyi/t/software-engineer/locations/france.md | 2026-11-12 | 2026-11-13 | B | Read | | France |
| S13 | Levels.fyi SWE, Japan `.md` — https://www.levels.fyi/t/software-engineer/locations/japan.md | 2026-11-05 | 2026-11-13 | B | Read | | Japan |
| S14 | Levels.fyi, End of Year Pay Report 2025 — https://www.levels.fyi/2025/ | n/a (2025 report) | 2026-11-13 | B | Read | vendor COI on coaching | K5, K8, K11 |
| S15 | Levels.fyi blog, AI Engineer Compensation Trends Q3 2025 — https://www.levels.fyi/blog/ai-engineer-compensation-trends-q3-2025.html | 2025-07-17 | 2026-11-13 | B | Read | | K6 |
| S16 | Levels.fyi title pages: AI Engineer (US; SF `.md`), FDE, Applied AI Engineer, AI Researcher, Machine Learning Ops Engineer — https://www.levels.fyi/t/software-engineer/title/ai-engineer ; https://www.levels.fyi/t/software-engineer/title/machine-learning-ops-engineer | various | 2026-11-13 | B | Extract | dates missing on some | K2, KF1 |
| S17 | Levels.fyi OpenAI and Anthropic company pages — https://www.levels.fyi/companies/openai/salaries/software-engineer | 2026-11-01; 2026-04-02 | 2026-11-13 | B | Extract | COI (Anthropic) | K4, KF4 |
| S18 | Levels.fyi company pages (Nvidia, Meta, Amazon incl. Applied Scientist, Salesforce, Pinterest, xAI, Scale AI, Shopify, Layer 6, Bosch; Berlin metro) — https://www.levels.fyi/companies/nvidia/salaries/software-engineer/title/machine-learning-engineer | various | 2026-11-13 | B | Extract | small n | employer table |
| S19 | Axial Search, ML Engineering Pay in 2026 — https://axialsearch.com/insights/ml-engineering-salaries | 2026-10-01 | 2026-11-13 | B | Read | recruiter COI; top-of-band | K1, K3 |
| S20 | Axial Search, What AI Engineering Roles Pay in 2026 — https://axialsearch.com/insights/ai-engineering-salaries | 2026-09-24 | 2026-11-13 | B | Read | recruiter COI; equity splits inconsistent | K3, K15 |
| S21 | Fast AI Jobs, FDE salaries and Anthropic job mirror — https://www.fastaijobs.com/salaries/forward-deployed-engineer | n/s | 2026-11-13 | B | Extract | aggregator | FDE posted |
| S22 | careery.pro LCA pages (OpenAI OpCo; Anthropic; AI/ML engineer role) — https://careery.pro/h1b-sponsors/openai-opco-llc | FY2025–FY2026 Q3 | 2026-11-13 | B | Extract | third-party of DOL data | LCA |
| S23 | Ellis LCA pages (OpenAI OpCo, OpenAI Inc, Anthropic) — https://www.ellis.com/visa-sponsors/openai-opco-llc | 2026-08 | 2026-11-13 | B | Extract | third-party of DOL data | LCA |
| S24 | h1bvisajobs.com, ML engineer FY2025; OpenAI SF SWE — https://h1bvisajobs.com/h1b-sponsorship-machine-learning-engineer | FY2025 | 2026-11-13 | B | Extract | third-party | LCA |
| S25 | h1bdata.net record I-200-25175-123570 — https://h1bdata.net/record/I-200-25175-123570 | 2025 | 2026-11-13 | B | Extract | | LCA example |
| S26 | BusinessToday.in (relaying Business Insider), Anthropic H-1B salaries — https://www.businesstoday.in/technology/news/story/from-engineers-to-product-managers-heres-how-much-anthropic-pays-with-salaries-up-to-rs13-02-crore-539575-2026-06-28 | 2026-06-28 | 2026-11-13 | C | Extract | relay; COI | Anthropic LCA |
| S27 | TechCrunch, OpenAI reportedly completed a $7 billion employee tender offer — https://techcrunch.com/2026/08/10/openai-reportedly-completed-a-7-billion-employee-tender-offer/ | 2026-08-10 | 2026-11-13 | B | Read | cites Bloomberg | KF5 |
| S28 | WSJ-derived coverage of OpenAI stock pay and the Oct 2025 tender (The Decoder; Implicator; SaaStr) — https://the-decoder.com/openais-stock-compensation-averages-1-5-million-per-employee-dwarfing-every-tech-startup-in-history/ | 2025-12-31; 2026-05 | 2026-11-13 | C | Extract | relay of WSJ; conflicting $865K figure | KF5 |
| S29 | Anthropic S-1 analyses (sec-api.io; IBTimes; VIP Wealth Advisors) — https://sec-api.io/insights/anthropic-ant-s-1-ipo-sec-filing-analysis | 2026-10-26 to 2026-10-27 | 2026-11-13 | C | Extract | COI; S-1 not opened | KF5 |
| S30 | Anthropic IPO roadshow coverage (ai-tldr citing anthropic.com; RTTNews; others) — https://ai-tldr.dev/releases/anthropic-ipo-price-range-roadshow/ | 2026-11-10 | 2026-11-13 | C | Extract | COI; dates unconfirmed | KF5 |
| S31 | Lock-up coverage (Augment citing Business Insider; Cryptopolitan) — https://augment.market/pulse/anthropics-lock-up-can-last-a-year-for-some-shareholders | 2026-10 | 2026-11-13 | C | Extract | COI; relay | KF5 |
| S32 | Globes, AI experts command the highest salaries in Israeli tech — https://en.globes.co.il/en/article-1001516449 | 2025-07-20 | 2026-11-13 | C | Read | recruiter data | Israel |
| S33 | Globes, AI researchers command lavish salaries — https://en.globes.co.il/en/article-ai-researchers-command-lavish-salaries-1001556738 | 2026-09-17 | 2026-11-13 | C | Read | industry sources | Israel |
| S34 | Arabian Business, UAE Salary Guide 2026 (Michael Page) — https://www.arabianbusiness.com/jobs/uae-salary-guide-2026-the-fastest-growing-sectors-top-paying-jobs-and-skills-employers-want-most | 2025-11-19 | 2026-11-13 | C | Read | relay of guide | UAE |
| S35 | UAE negotiation statistics (The National; Arabian Business; Khaleej Times) — https://www.thenationalnews.com/business/money/2025/10/20/fewer-uae-jobseekers-getting-desired-salary-amid-global-talent-influx | 2025-10-20 | 2026-11-13 | C | Extract | relays conflict | Gulf negotiation |
| S36 | Khaleej Times, Michael Page UAE Salary Guide 2027 — https://www.khaleejtimes.com/business/half-of-uae-workers-would-consider-quitting-if-asked-to-spend-more-time-in-office-report | 2026-10-27 | 2026-11-13 | C | Read | no AI pay tables | K19 |
| S37 | AI in Arabia (relay of Cooper Fitch) — https://ai-in-arabia-v2.pages.dev/careers/gulf-ai-jobs-boom-salaries-visas-upskilling-2026 | 2026 | 2026-11-13 | D | Extract | single-source; not traced | Saudi |
| S38 | Robert Half UK, ML Engineer, Greater London — https://www.roberthalf.com/gb/en/job-details/machine-learning-engineer/greater-london | n/s | 2026-11-13 | C | Extract | placement-based | UK |
| S39 | Robert Half Australia, AI Engineer and ML Engineer, Sydney — https://www.roberthalf.com/au/en/job-details/ai-engineer/sydney | n/s | 2026-11-13 | C | Extract | column order assumed | Australia |
| S40 | Hays Australia, AI elevates human expertise — https://www.hays.com.au/press-release/content/ai-elevates-human-expertise | 2026-04-30 | 2026-11-13 | C | Extract | | Australia |
| S41 | Morgan McKinley Japan, ML engineer, Tokyo — https://www.morganmckinley.com/jp-ja/salary-guide/data/機械学習エンジニア-事業法人/東京 | 2026 | 2026-11-13 | C | Extract | placement-based | Japan |
| S42 | Geekly, AI job type income — https://www.geekly.co.jp/column/cat-position/ai_job_type_income/ | 2026 | 2026-11-13 | C | Extract | candidate-reported | Japan |
| S43 | Indeed Hiring Lab Europe and UK transparency (with Euronews 2026-09-08, FE News) — https://www.hiringlab.org/uk/blog/2026/05/07/full-salary-transparency-in-europe-is-still-a-distant-prospect/ | 2026-05-07 | 2026-11-13 | B | Extract | | KF11 |
| S44 | HR Reporter, Indeed Pay Transparency Tracker, Canada — https://www.hrreporter.com/focus-areas/compensation-and-benefits/how-many-canadian-employers-include-salary-info-for-hr-jobs/394704 | 2026-06 | 2026-11-13 | B | Extract | relay of Indeed | KF11 |
| S45 | fantastic.jobs, Global Salary Transparency 2026 — https://fantastic.jobs/article/salary-transparency | 2026-04 | 2026-11-13 | C | Extract | job-feed method | KF11 |
| S46 | UCLA Anderson Review on NBER w33903 (Cullen, Perez-Truglia, Pakzad-Hurson) — https://anderson-review.ucla.edu/most-job-seekers-skip-negotiation-and-pay-a-high-price/ | 2025-10-15 | 2026-11-13 | B | Read | secondary; paper not opened | negotiation |
| S47 | Pave and Nua Group, The State of AI Talent — https://explore.pave.com/The-State-of-AI-Talent.html | 2026-08-24 | 2026-11-13 | C | Extract | vendor COI | K20 |
| S48 | Pave Merit Cycle 2026 (EIN Presswire) — https://www.einpresswire.com/article/915253089/2026-merit-cycle-report-ai-talent-premium-grows-as-raise-budgets-tighten | 2026-05-28 | 2026-11-13 | C | Extract | vendor COI | K20 |
| S49 | FutureProofing, AI compensation landscape (relays Pave, Carta, Levels.fyi) — https://www.futureproofing.dev/resources/hire-ai-engineer-hub/ai-engineer-salary-trends | 2026-09-22 | 2026-11-13 | C | Extract | relay | K20, K21 |
| S50 | Business Wire, Schwab completes acquisition of Forge Global — https://www.businesswire.com/news/home/20260302211827/en/Charles-Schwab-Completes-Acquisition-of-Forge-Global | 2026-03-02 | 2026-11-13 | B | Extract | issuer statement | K22 |
| S51 | Morgan Stanley, closes EquityZen acquisition — https://www.morganstanley.com/press-releases/morgan-stanley-closes-equityzen-acquisition | 2026-01-27 | 2026-11-13 | B | Extract | issuer statement | K23 |
| S52 | Product Hunt listings (Capbase exit calculator; Autograph Fair Offer); TNW on EquityBee Benchmark — https://www.producthunt.com/products/startup-exit-calculator-by-capbase-2 | 2024-01-15 to 2026-04-08 | 2026-11-13 | C | Extract | | K24, K25 |
| S53 | Rora website — https://www.teamrora.com | n/s | 2026-11-13 | B | Extract | COI (vendor) | K12 |
| S54 | Next Europa, How to Negotiate Salary in 2026 — https://all-blog-nexteuropa.pages.dev/career-advice/how-to-negotiate-salary-2026 | 2026-05-09 | 2026-11-13 | E | Extract | affiliate; single-source | K13, K14 |
| S55 | Atlas Van Lines 59th survey; NEI lump-sum survey — https://www.atlasvanlines.com/company-news/atlas-van-lines-59th-annual-corporate-relocation-survey-family-flexibility-and-the-economy-are-driving-relocation-decisions | 2026-04-16 | 2026-11-13 | C | Extract | generic US | relocation |
| S56 | McGill, employers more open to negotiating than Canadians assume — https://www.mcgill.ca/channels/node/215808 | 2026-02-09 | 2026-11-13 | C | Extract | snippet | Canada |
| S57 | Robert Half UK and Australia negotiation surveys (HR Review; IT Brief) — https://itbrief.com.au/story/australian-employers-brace-for-renewed-pay-negotiations | 2026-02-24 | 2026-11-13 | C | Extract | vendor survey | UK, Australia |
| S58 | Kikkake Creation survey of 393 IT engineers (PR Times, via aeo.washinmura.jp) — https://aeo.washinmura.jp/ai/kikkakecreation-com/en/news/2026-05-12-survey-on-the-reality-of-salary-negotiat | 2026-05-12 | 2026-11-13 | C | Extract | vendor survey; relay | Japan |
| S59 | Anthropic Greenhouse postings, London: five opened (jobs 4938436008, 5126127008, 5264619008, 5116274008, 5115935008) and one seen only in search results (4980460008) — https://job-boards.greenhouse.io/anthropic/jobs/4938436008 | not shown | 2026-11-13 | A | Read | COI; one further page blocked | UK frontier bands, visa text |
| S60 | Payscale AU, Indeed AU, Glassdoor Israel — https://www.payscale.com/research/AU/Job=Machine_Learning_Engineer/Salary/5735f513/Sydney | 2026 | 2026-11-13 | C | Extract | different population | K18 |
| S61 | choppingblock.ai, atr-blog.pages.dev, jobmentis.com, globalcostdata.com, orbytjobs.ai, comp-verdict.netlify.app, freenance.io | 2026 | 2026-11-13 | E | Extract | AI-generated or thin; not used | quality note |
| S62 | HeroHunt and FourWeekMBA relays of Levels.fyi OpenAI and Anthropic data — https://fourweekmba.com/ai-openai-offers-new-senior-engineers-2-6x-microsofts-pay/ | 2026-11-06 | 2026-11-13 | C | Extract | relay; COI (Anthropic) | K4 |
| S63 | ITJobsWatch, ML Engineer jobs in London — https://www.itjobswatch.co.uk/jobs/london/machine%20learning%20engineer.do | 2025-05-05 | 2026-11-13 | C | Extract | history, outside window | UK posted history |
| S64 | SHRM, negotiating points important to European job candidates — https://www.shrm.org/topics-tools/employment-law-compliance/negotiating-points-important-to-european-job-candidates | n/s | 2026-11-13 | C | Extract | undated | Europe |
| S65 | OpenAI Careers, Staff / Senior Staff Backend Engineer, B2B Flywheel — https://openai.com/careers/staff-senior-staff-backend-engineer-b2b-flywheel-san-francisco/ | 2026-05-15 (date from mirror) | 2026-11-13 | A | Read | employer's own page | KF15, title note |
| S66 | OpenAI postings on venture-capital job-board mirrors — https://jobs.stripes.co/companies/openai/jobs/65812394-senior-research-engineer-scientist-edge-consumer-products | 2026-01-13 to 2026-05-23 | 2026-11-13 | B | Extract | mirrors of the employer feed; snippets only | US posted bands, relocation text |
| S67 | Recruiting From Scratch, OpenAI Salary — https://www.recruitingfromscratch.com/roles/openai-salary | 2026-07-01 | 2026-11-13 | C | Extract | aggregator of 570 postings; midpoints; all roles | KF15 |
| S68 | Salary-history ban and pay-transparency law summaries (Foley; National Law Review; teamed.global; FirstHR; employsome) — https://www.teamed.global/pay-transparency-laws-by-state | 2026-05 to 2026-07 | 2026-11-13 | B | Extract | counts conflict (18 against about 20) | K9, US law |
| S69 | Poland: Michael Page posting; Egospodarka relaying Devire; itwiz relaying Just Join IT — https://michaelpage.pl/en/job-detail/machine-learning-engineer/ref/jn-062026-7034773 | 2025–2026 | 2026-11-13 | B | Extract | posting is B; relays are C | Poland |
| S70 | Academic Work ad received through Arbetsförmedlingen, via SweClockers jobs — https://jobb.sweclockers.com/jobb/8842 | 2026 | 2026-11-13 | C | Extract | single example | Sweden |

## Data Appendix

```jsonl
{"type":"pay","grade":"B","src":["S1"],"as_of":"2026-11-11","ttl":"V3","role":"ml-engineer","location":"United States","stat":"p25","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":200000,"n":1027}
{"type":"pay","grade":"B","src":["S1"],"as_of":"2026-11-11","ttl":"V3","role":"ml-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":286958,"n":1027,"note":"p90 497500; self-reported, large-employer skew; HTML page of 2026-11-12 shows 285650"}
{"type":"pay","grade":"B","src":["S1"],"as_of":"2026-11-11","ttl":"V3","role":"ml-engineer","location":"United States","stat":"p75","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":389850,"n":1027}
{"type":"pay","grade":"B","src":["S2"],"as_of":"2026-11-12","ttl":"V3","role":"ml-engineer","location":"United Kingdom","stat":"p25","currency":"GBP","period":"year","basis":"tc","source_name":"Levels.fyi","value":80210,"n":114}
{"type":"pay","grade":"B","src":["S2"],"as_of":"2026-11-12","ttl":"V3","role":"ml-engineer","location":"United Kingdom","stat":"p50","currency":"GBP","period":"year","basis":"tc","source_name":"Levels.fyi","value":104887,"n":114,"note":"p90 213619"}
{"type":"pay","grade":"B","src":["S2"],"as_of":"2026-11-12","ttl":"V3","role":"ml-engineer","location":"United Kingdom","stat":"p75","currency":"GBP","period":"year","basis":"tc","source_name":"Levels.fyi","value":156733,"n":114}
{"type":"pay","grade":"B","src":["S16"],"as_of":null,"ttl":"V3","role":"ai-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":155000,"note":"p25 110000; p75 212000; p90 280000; n and update date not shown in extract"}
{"type":"pay","grade":"B","src":["S16"],"as_of":"2026-06-15","ttl":"V3","role":"ai-engineer","location":"San Francisco Bay Area","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":225000,"note":"p25 170000; p75 309000; p90 459980; n not shown"}
{"type":"pay","grade":"B","src":["S16"],"as_of":"2026-09-08","ttl":"V3","role":"forward-deployed-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":205000,"note":"p25 172000; p75 277000; p90 350000"}
{"type":"pay","grade":"B","src":["S21"],"as_of":null,"ttl":"V3","role":"forward-deployed-engineer","location":"United States","employer_type":"ai-startup","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Fast AI Jobs","value":180656,"n":164,"note":"disclosed salaries in postings; range 75000-375000; page date not shown"}
{"type":"pay","grade":"B","src":["S16"],"as_of":null,"ttl":"V3","role":"applied-ai-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":250000,"note":"p25 200000; p75 475000; p90 605000; date not shown"}
{"type":"pay","grade":"B","src":["S16"],"as_of":null,"ttl":"V3","role":"research-scientist","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":172000,"note":"AI Researcher title; p25 56000; p75 340000; p90 490000; wide, small n"}
{"type":"pay","grade":"B","src":["S16"],"as_of":"2026-10-11","ttl":"V3","role":"ml-platform-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi","value":145200,"note":"Machine Learning Ops Engineer title; p25 120000; p75 200000; p90 295000; n not shown"}
{"type":"pay","grade":"B","src":["S18"],"as_of":null,"ttl":"V3","role":"applied-scientist","location":"United States","employer_type":"big-tech","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Amazon","value":306000,"note":"median reported TC; median package 335000; L4 245000; L7 653000; date not shown"}
{"type":"pay","grade":"B","src":["S23"],"as_of":null,"ttl":"V4","role":"research-scientist","location":"San Francisco Bay Area","employer_type":"frontier-lab","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Ellis LCA data, OpenAI OpCo","value":360000,"n":188,"note":"MTS (Research Scientist); filed wage, min 178006, max 685000; page dated Aug 2026"}
{"type":"pay","grade":"B","src":["S23"],"as_of":null,"ttl":"V4","role":"research-engineer","location":"San Francisco Bay Area","employer_type":"frontier-lab","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Ellis LCA data, OpenAI OpCo","value":335000,"n":84,"note":"MTS (Research Engineer); filed wage, min 210000, max 530000"}
{"type":"pay","grade":"B","src":["S23"],"as_of":null,"ttl":"V4","role":"ai-infrastructure-engineer","location":"San Francisco Bay Area","employer_type":"frontier-lab","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Ellis LCA data, OpenAI OpCo","value":252500,"n":187,"note":"MTS (AI Systems Engineer); title mapping uncertain; min 170000, max 460000"}
{"type":"pay","grade":"B","src":["S24"],"as_of":"2025-09-30","ttl":"V4","role":"ml-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"h1bvisajobs.com from DOL LCA","value":179982,"n":3745,"note":"filed wage floor; p25 145000; p75 215000; p90 250000; FY2025"}
{"type":"pay","grade":"B","src":["S22"],"as_of":"2025-09-30","ttl":"V4","role":"ai-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"careery.pro from DOL LCA","value":165350,"n":3816,"note":"AI/ML engineer family; annualised lower bound of filed range; FY2025"}
{"type":"pay","grade":"B","src":["S22"],"as_of":"2026-06-30","ttl":"V4","role":"ai-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"careery.pro from DOL LCA","value":169000,"n":4459,"note":"FY2026 Q1-Q3; lower bound"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-10-01","ttl":"V3","role":"ml-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":197000,"n":13776,"note":"median of the top of the posted band, all levels, Jan-Oct 2026 postings"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-10-01","ttl":"V3","role":"ml-engineer","location":"United States","level":"IC junior","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":180000,"note":"top of posted band; p25 137000; p75 213000"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-10-01","ttl":"V3","role":"ml-engineer","location":"United States","level":"IC mid","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":211000,"note":"top of posted band; p25 184000; p75 244000"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-10-01","ttl":"V3","role":"ml-engineer","location":"United States","level":"IC senior","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":241000,"note":"top of posted band; p25 212000; p75 261000"}
{"type":"pay","grade":"B","src":["S19"],"as_of":"2026-10-01","ttl":"V3","role":"ml-engineer","location":"United States","level":"IC principal","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":300000,"note":"top of posted band; p25 260000; p75 334000"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineer","location":"United States","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":176000,"n":43480,"note":"median of the top of the posted band, all levels, Jan-Sep 2026 postings"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineer","location":"United States","level":"IC junior","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":170000,"note":"top of posted band; p25 130000; p75 200000"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineer","location":"United States","level":"IC mid","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":200000,"note":"top of posted band; p25 163000; p75 250000"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineer","location":"United States","level":"IC senior","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":213000,"note":"top of posted band; p25 187000; p75 250000"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineer","location":"United States","level":"IC principal","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":270000,"note":"top of posted band; p25 232000; p75 309000"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineering-manager","location":"United States","level":"manager","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":262000,"note":"top of posted band, AI engineering postings"}
{"type":"pay","grade":"B","src":["S20"],"as_of":"2026-09-24","ttl":"V3","role":"ai-engineering-manager","location":"United States","level":"director","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search","value":290000,"note":"top of posted band, AI engineering postings"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-06-30","ttl":"V3","role":"ml-engineer","location":"United States","employer_type":"big-tech","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Nvidia","value":261000,"note":"IC1 205000; IC3 292000; IC4 331000"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2025-12-19","ttl":"V3","role":"ml-engineer","location":"United States","employer_type":"enterprise","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Salesforce","value":286000,"note":"page also states 268000; Senior MTS 308000"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-05-16","ttl":"V3","role":"ml-engineer","location":"United States","level":"IC15 senior","employer_type":"enterprise","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Pinterest","value":465000,"note":"IC13 226000; IC16 686000"}
{"type":"pay","grade":"C","src":["S18"],"as_of":"2026-01-30","ttl":"V3","role":"ml-engineer","location":"Palo Alto","level":"L4","employer_type":"frontier-lab","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi xAI","value":690000,"note":"single package: base 290000, stock 400000"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-07-01","ttl":"V3","role":"ml-engineer","location":"United States","employer_type":"ai-startup","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Scale AI","value":178100,"note":"median reported TC; median package 215000; L3 195000; L4 254000"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-02-17","ttl":"V3","role":"research-engineer","location":"San Francisco","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":295000,"hi":445000,"note":"Speech and Realtime Models; offers equity, amount not stated"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-01-23","ttl":"V3","role":"research-engineer","location":"San Francisco","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":380000,"hi":460000,"note":"Senior Research Engineer/Scientist, Edge, Consumer Products; offers equity"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-01-13","ttl":"V3","role":"research-engineer","location":"San Francisco","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":230000,"hi":460000,"note":"ML Research Engineer, Hardware Codesign; offers equity"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-03-13","ttl":"V3","role":"research-engineer","location":"San Francisco","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":380000,"hi":445000,"note":"Research Engineer/Scientist, Human Alignment, Consumer Devices; offers equity"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-05-23","ttl":"V3","role":"research-scientist","location":"San Francisco","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":250000,"hi":380000,"note":"Researcher, Context, Agent Post-Training"}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-03-20","ttl":"V3","role":"research-scientist","location":"San Francisco","employer_type":"frontier-lab","level":"early career","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI posting via venture job-board mirror","lo":295000,"hi":295000,"note":"Early Career Cohort; single figure; relocation assistance may be available"}
{"type":"pay","grade":"A","src":["S59"],"as_of":null,"ttl":"V3","role":"research-engineer","location":"London","employer_type":"frontier-lab","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"Anthropic postings 4938436008, 5126127008, 5115935008","lo":260000,"hi":630000,"note":"COI; three London postings with the same band; spans internal levels; posting dates not shown; equity not quantified"}
{"type":"pay","grade":"A","src":["S59"],"as_of":null,"ttl":"V3","role":"research-engineer","location":"London","employer_type":"frontier-lab","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"Anthropic posting 5264619008","lo":375000,"hi":640000,"note":"COI; RL Scaling Science; posting date not shown"}
{"type":"pay","grade":"B","src":["S59"],"as_of":null,"ttl":"V3","role":"research-engineer","location":"London","employer_type":"frontier-lab","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"Anthropic posting 4980460008","lo":270000,"hi":340000,"note":"COI; Post-Training; seen in search results only; total package adds equity"}
{"type":"pay","grade":"A","src":["S59"],"as_of":null,"ttl":"V3","role":"applied-ai-engineer","location":"London","employer_type":"frontier-lab","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"Anthropic posting 5116274008","lo":225000,"hi":240000,"note":"COI; 4+ years, customer-facing; posting date not shown"}
{"type":"pay","grade":"B","src":["S21"],"as_of":"2026-07-15","ttl":"V3","role":"applied-ai-engineer","location":"London","employer_type":"frontier-lab","stat":"range","currency":"GBP","period":"year","basis":"base","source_name":"Anthropic posting 5343697008 via Fast AI Jobs","lo":240000,"hi":255000,"note":"COI; Beneficial Deployments"}
{"type":"pay","grade":"B","src":["S4"],"as_of":"2026-11-11","ttl":"V3","role":"forward-deployed-engineer","location":"United Kingdom","stat":"p50","currency":"GBP","period":"year","basis":"tc","source_name":"Levels.fyi","value":139550,"note":"title median within UK SWE sample n=4743"}
{"type":"pay","grade":"B","src":["S4"],"as_of":"2026-11-11","ttl":"V3","role":"research-scientist","location":"United Kingdom","stat":"p50","currency":"GBP","period":"year","basis":"tc","source_name":"Levels.fyi","value":129774,"note":"title median within UK SWE sample n=4743"}
{"type":"pay","grade":"C","src":["S38"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"London","stat":"p50","currency":"GBP","period":"year","basis":"base","source_name":"Robert Half UK","value":99750,"note":"placement-based; p25 79750; p75 126250; n and date not shown"}
{"type":"pay","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","role":"forward-deployed-engineer","location":"Canada","stat":"p50","currency":"CAD","period":"year","basis":"tc","source_name":"Levels.fyi","value":186280,"note":"title median within Canada SWE sample n=5338"}
{"type":"pay","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","role":"research-scientist","location":"Canada","stat":"p50","currency":"CAD","period":"year","basis":"tc","source_name":"Levels.fyi","value":177575,"note":"title median within Canada SWE sample n=5338"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-02-28","ttl":"V3","role":"ml-engineer","location":"Toronto","employer_type":"enterprise","stat":"p50","currency":"CAD","period":"year","basis":"tc","source_name":"Levels.fyi Shopify","value":230000,"note":"company page; small n"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-07-22","ttl":"V3","role":"ml-engineer","location":"Toronto","employer_type":"enterprise","stat":"p50","currency":"CAD","period":"year","basis":"tc","source_name":"Levels.fyi Layer 6","value":208000,"note":"company page; small n"}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2025-07-25","ttl":"V3","role":"ml-engineer","location":"Berlin","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi Berlin metro","value":97683,"note":"older snapshot; USD display; p25 86700; p75 106000; n not shown"}
{"type":"pay","grade":"B","src":["S18"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Germany","employer_type":"enterprise","stat":"p50","currency":"EUR","period":"year","basis":"tc","source_name":"Levels.fyi Bosch Global","value":85600,"note":"EG15 82400; date not shown; small n"}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-11-11","ttl":"V3","role":"ml-engineer","location":"Netherlands","stat":"p50","currency":"EUR","period":"year","basis":"tc","source_name":"Levels.fyi","value":122301,"note":"title median within NL SWE sample n=1403"}
{"type":"pay","grade":"B","src":["S11"],"as_of":"2026-11-11","ttl":"V3","role":"forward-deployed-engineer","location":"Netherlands","stat":"p50","currency":"EUR","period":"year","basis":"tc","source_name":"Levels.fyi","value":135510,"note":"title median within NL SWE sample n=1403"}
{"type":"pay","grade":"B","src":["S12"],"as_of":"2026-11-12","ttl":"V3","role":"ml-engineer","location":"France","stat":"p50","currency":"EUR","period":"year","basis":"tc","source_name":"Levels.fyi","value":75458,"note":"title median within France SWE sample n=1106"}
{"type":"pay","grade":"B","src":["S9"],"as_of":"2026-11-11","ttl":"V3","role":"ml-engineer","location":"Switzerland","stat":"p50","currency":"CHF","period":"year","basis":"tc","source_name":"Levels.fyi","value":179235,"note":"title median within Swiss SWE sample n=617"}
{"type":"pay","grade":"B","src":["S9"],"as_of":"2026-11-11","ttl":"V3","role":"forward-deployed-engineer","location":"Switzerland","stat":"p50","currency":"CHF","period":"year","basis":"tc","source_name":"Levels.fyi","value":172655,"note":"title median within Swiss SWE sample n=617"}
{"type":"pay","grade":"B","src":["S69"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Warsaw","stat":"range","currency":"PLN","period":"year","basis":"base","source_name":"Michael Page Poland posting jn-062026-7034773","lo":263000,"hi":329000,"note":"permanent contract; gross or net not stated; reference suggests June 2026"}
{"type":"pay","grade":"C","src":["S69"],"as_of":null,"ttl":"V3","role":"ai-engineer","location":"Poland","level":"senior","stat":"range","currency":"PLN","period":"month","basis":"base","source_name":"Devire report via Egospodarka","lo":25000,"hi":35000,"note":"gross, employment contract; Lead/Principal 32000-45000; date not shown, after June 2025"}
{"type":"pay","grade":"B","src":["S6"],"as_of":"2026-11-12","ttl":"V3","role":"ml-engineer","location":"Singapore","stat":"p50","currency":"SGD","period":"year","basis":"tc","source_name":"Levels.fyi","value":151000,"note":"title median within Singapore SWE sample n=1360"}
{"type":"pay","grade":"C","src":["S32"],"as_of":"2025-06-30","ttl":"V3","role":"ai-engineer","location":"Israel","stat":"mean","currency":"ILS","period":"month","basis":"base","source_name":"GotFriends via Globes","value":46755,"note":"GenAI developers, H1 2025; algorithm experts without GenAI 42255; recruiter data"}
{"type":"pay","grade":"C","src":["S33"],"as_of":"2026-09-17","ttl":"V3","role":"research-scientist","location":"Israel","stat":"range","currency":"ILS","period":"month","basis":"base","source_name":"Globes industry sources","lo":50000,"hi":90000,"note":"AI researchers, gross, plus stock options; not a statistic"}
{"type":"pay","grade":"C","src":["S32","S33"],"as_of":"2025-07-20","ttl":"V3","role":"vp-head-of-ai","location":"Israel","stat":"range","currency":"ILS","period":"month","basis":"base","source_name":"GotFriends via Globes","lo":60000,"hi":80000,"note":"AI team and integration management roles, often with sign-on; role mapping approximate"}
{"type":"pay","grade":"C","src":["S34"],"as_of":"2025-11-19","ttl":"V3","role":"ai-engineer","location":"Dubai","stat":"range","currency":"AED","period":"month","basis":"base","source_name":"Michael Page UAE Salary Guide 2026 via Arabian Business","lo":30000,"hi":45000,"note":"GenAI Engineer / MLOps; monthly basis inferred from USD equivalents; guide not opened"}
{"type":"pay","grade":"C","src":["S34"],"as_of":"2025-11-19","ttl":"V3","role":"ai-product-manager","location":"Dubai","stat":"range","currency":"AED","period":"month","basis":"base","source_name":"Michael Page UAE Salary Guide 2026 via Arabian Business","lo":30000,"hi":45000,"note":"monthly basis inferred"}
{"type":"pay","grade":"C","src":["S34"],"as_of":"2025-11-19","ttl":"V3","role":"vp-head-of-ai","location":"Dubai","stat":"range","currency":"AED","period":"month","basis":"base","source_name":"Michael Page UAE Salary Guide 2026 via Arabian Business","lo":70000,"hi":120000,"note":"Head/Director of AI; monthly basis inferred"}
{"type":"pay","grade":"D","src":["S37"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Riyadh","level":"junior","stat":"range","currency":"SAR","period":"month","basis":"base","source_name":"Cooper Fitch Q1 2026 via unverified relay","lo":20000,"hi":28000,"note":"not traced to the guide"}
{"type":"pay","grade":"D","src":["S37"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Riyadh","level":"senior","stat":"range","currency":"SAR","period":"month","basis":"base","source_name":"Cooper Fitch Q1 2026 via unverified relay","lo":42000,"hi":62000,"note":"not traced to the guide"}
{"type":"pay","grade":"C","src":["S41"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Tokyo","stat":"range","currency":"JPY","period":"year","basis":"base","source_name":"Morgan McKinley Japan 2026 guide","lo":6000000,"hi":12000000,"note":"low to high, corporate employers; mid 8000000; excludes bonus; placement-based"}
{"type":"pay","grade":"C","src":["S39"],"as_of":null,"ttl":"V3","role":"ai-engineer","location":"Sydney","stat":"p50","currency":"AUD","period":"year","basis":"base","source_name":"Robert Half Australia","value":185300,"note":"25th 163500; 75th 212550; column order assumed from the London page layout"}
{"type":"pay","grade":"C","src":["S40"],"as_of":"2026-04-30","ttl":"V3","role":"ai-engineer","location":"Australia","stat":"range","currency":"AUD","period":"year","basis":"base","source_name":"Hays Australia","lo":145000,"hi":200000,"note":"upper end stated as 200000+; Tech Talent Explorer updated Dec 2025"}
{"type":"pay","grade":"C","src":["S60"],"as_of":null,"ttl":"V3","role":"ml-engineer","location":"Sydney","stat":"mean","currency":"AUD","period":"year","basis":"base","source_name":"Payscale","value":93528,"note":"broad crowdsourced population; differs from Levels.fyi and recruiter placement data"}
```

```jsonl
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"US SWE total comp","measure":"median","unit":"USD/year","value":200000,"n":46545,"region":"US","note":"p25 140000; p75 287333; p90 395000; median base 163000"}
{"type":"measure","grade":"B","src":["S4"],"as_of":"2026-11-11","ttl":"V3","subject":"UK SWE total comp","measure":"median","unit":"GBP/year","value":90039,"n":4743,"region":"UK","note":"p25 60168; p75 130019; p90 176609"}
{"type":"measure","grade":"B","src":["S10"],"as_of":"2026-11-11","ttl":"V3","subject":"Ireland SWE total comp","measure":"median","unit":"EUR/year","value":105072,"n":1161,"region":"Ireland","note":"p25 78346; p75 141197; p90 169145"}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-11","ttl":"V3","subject":"Germany SWE total comp","measure":"median","unit":"EUR/year","value":85121,"n":2947,"region":"Germany","note":"p25 70692; p75 102640; p90 126054"}
{"type":"measure","grade":"B","src":["S11"],"as_of":"2026-11-11","ttl":"V3","subject":"Netherlands SWE total comp","measure":"median","unit":"EUR/year","value":95634,"n":1403,"region":"Netherlands","note":"p25 73898; p75 131136; p90 163452"}
{"type":"measure","grade":"B","src":["S12"],"as_of":"2026-11-12","ttl":"V3","subject":"France SWE total comp","measure":"median","unit":"EUR/year","value":61045,"n":1106,"region":"France","note":"p25 47046; p75 77325; p90 103959"}
{"type":"measure","grade":"B","src":["S9"],"as_of":"2026-11-11","ttl":"V3","subject":"Switzerland SWE total comp","measure":"median","unit":"CHF/year","value":134226,"n":617,"region":"Switzerland","note":"p25 106969; p75 192643; p90 279831; 13 instalments usual"}
{"type":"measure","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","subject":"Canada SWE total comp","measure":"median","unit":"CAD/year","value":136907,"n":5338,"region":"Canada","note":"p25 102914; p75 185466; p90 236410"}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-11-12","ttl":"V3","subject":"Singapore SWE total comp","measure":"median","unit":"SGD/year","value":114974,"n":1360,"region":"Singapore","note":"p25 85540; p75 165006; p90 216301; 13 instalments usual"}
{"type":"measure","grade":"B","src":["S13"],"as_of":"2026-11-05","ttl":"V3","subject":"Japan SWE total comp","measure":"median","unit":"JPY/year","value":8413533,"n":384,"region":"Japan","note":"p25 6560187; p75 11730848; p90 16868633"}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-11-04","ttl":"V3","subject":"Australia SWE total comp","measure":"median","unit":"AUD/year","value":152290,"n":1590,"region":"Australia","note":"p25 114915; p75 190474; p90 243743"}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, San Francisco Bay Area","measure":"median","unit":"USD/year","value":300000}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Seattle","measure":"median","unit":"USD/year","value":257600}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, New York","measure":"median","unit":"USD/year","value":215900}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Austin","measure":"median","unit":"USD/year","value":200000}
{"type":"measure","grade":"B","src":["S4"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, London","measure":"median","unit":"GBP/year","value":105271}
{"type":"measure","grade":"B","src":["S4"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Cambridge","measure":"median","unit":"GBP/year","value":117192}
{"type":"measure","grade":"B","src":["S10"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Dublin","measure":"median","unit":"EUR/year","value":110408}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Berlin","measure":"median","unit":"EUR/year","value":93539}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Munich","measure":"median","unit":"EUR/year","value":80623}
{"type":"measure","grade":"B","src":["S11"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Amsterdam","measure":"median","unit":"EUR/year","value":105747}
{"type":"measure","grade":"B","src":["S12"],"as_of":"2026-11-12","ttl":"V3","subject":"SWE total comp, Paris","measure":"median","unit":"EUR/year","value":90546}
{"type":"measure","grade":"B","src":["S9"],"as_of":"2026-11-11","ttl":"V3","subject":"SWE total comp, Zurich","measure":"median","unit":"CHF/year","value":209499}
{"type":"measure","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","subject":"SWE total comp, Toronto","measure":"median","unit":"CAD/year","value":140269}
{"type":"measure","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","subject":"SWE total comp, Vancouver","measure":"median","unit":"CAD/year","value":186120}
{"type":"measure","grade":"B","src":["S7"],"as_of":"2026-11-03","ttl":"V3","subject":"SWE total comp, Montreal","measure":"median","unit":"CAD/year","value":121755}
{"type":"measure","grade":"B","src":["S13"],"as_of":"2026-11-05","ttl":"V3","subject":"SWE total comp, Tokyo","measure":"median","unit":"JPY/year","value":8980325}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-11-04","ttl":"V3","subject":"SWE total comp, Sydney","measure":"median","unit":"AUD/year","value":162228}
{"type":"measure","grade":"B","src":["S17"],"as_of":"2026-11-01","ttl":"V3","subject":"OpenAI software engineers, all levels, total comp","measure":"median","unit":"USD/year","value":600000,"n":248,"note":"L2 249000 to L7 1890000; leaderboard median 640000 on 2026-11-11"}
{"type":"measure","grade":"B","src":["S17"],"as_of":"2026-11-01","ttl":"V3","subject":"OpenAI L5 software engineer, average total comp","measure":"mean","unit":"USD/year","value":932917,"note":"base 335000; stock 597917, about 64 percent"}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-11","ttl":"V3","subject":"Anthropic software engineers, leaderboard median total comp","measure":"median","unit":"USD/year","value":882500,"note":"COI; company page snapshot of 2026-04-02 shows 570000 to 582500"}
{"type":"measure","grade":"B","src":["S15"],"as_of":"2025-07-17","ttl":"V3","subject":"AI premium over non-AI SWE total comp, Entry to Staff","measure":"difference","unit":"percent","lo":6.2,"hi":18.7,"note":"Entry 6.2; Engineer 11.9; Senior 14.2; Staff 18.7; 2024: 10.74, 11.6, 14.3, 15.8"}
{"type":"measure","grade":"B","src":["S14"],"as_of":"2025-12-31","ttl":"V3","subject":"US SWE median total comp by level, all companies, 2025","measure":"median","unit":"USD/year","lo":155000,"hi":551000,"note":"Entry 155000; Engineer 226000; Senior 312000; Staff 457000; Principal 551000"}
{"type":"measure","grade":"B","src":["S14"],"as_of":"2025-12-31","ttl":"V3","subject":"Levels.fyi coaching clients, engineers: median TC increase","measure":"median uplift","unit":"percent","lo":21,"hi":24,"note":"mid 21; senior 23; staff 24; self-selected; 650+ negotiations; about 40M total"}
{"type":"measure","grade":"B","src":["S46"],"as_of":"2025-02-10","ttl":"V5","subject":"Tech job seekers who countered an offer, encouraged group against control","measure":"share countering","unit":"percent","value":61,"n":3858,"note":"control 54; field experiment May 2023 to Feb 2025"}
{"type":"measure","grade":"B","src":["S46"],"as_of":"2025-02-10","ttl":"V5","subject":"Average compensation gain among those who countered","measure":"mean","unit":"percent","value":12.45,"note":"about 27000 USD a year; about 40 percent of offers were verbal"}
{"type":"measure","grade":"C","src":["S35"],"as_of":"2025-10-20","ttl":"V3","subject":"UAE professionals who negotiated pay in the 12 months to the Michael Page 2026 guide","measure":"share","unit":"percent","lo":43,"hi":49,"note":"relays conflict: 43 (Khaleej Times) against 49 attempted with 15 succeeded (The National, Arabian Business)"}
{"type":"measure","grade":"C","src":["S58"],"as_of":"2026-05-12","ttl":"V3","subject":"Japan IT engineers who negotiated pay at job change","measure":"share","unit":"percent","value":74.5,"n":393,"note":"90.8 percent of them received a raise; vendor survey"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-07-31","ttl":"V1","subject":"Share of UK postings with pay information","measure":"share","unit":"percent","lo":56,"hi":60,"region":"UK","note":"56 Mar 2026; 58 Q2; 60 Jul 2026"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-07-31","ttl":"V1","subject":"Share of postings with pay information, Netherlands","measure":"share","unit":"percent","value":49.5,"region":"Netherlands"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-07-31","ttl":"V1","subject":"Share of postings with pay information, France","measure":"share","unit":"percent","value":43,"region":"France"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-03-31","ttl":"V1","subject":"Share of postings with pay information, Ireland","measure":"share","unit":"percent","lo":34,"hi":39,"region":"Ireland","note":"34 Jan 2026; 39 Mar 2026"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-07-31","ttl":"V1","subject":"Share of postings with pay information, Germany","measure":"share","unit":"percent","lo":12,"hi":14,"region":"Germany"}
{"type":"measure","grade":"B","src":["S43"],"as_of":"2026-07-31","ttl":"V1","subject":"Share of postings with pay information, Italy","measure":"share","unit":"percent","value":61,"region":"Italy","note":"35 in Jan 2026"}
{"type":"measure","grade":"B","src":["S44"],"as_of":"2026-06-30","ttl":"V1","subject":"Share of postings with pay information, Ontario","measure":"share","unit":"percent","value":71,"region":"Ontario","note":"49 before its disclosure law; Canada 57; rest of Canada 41"}
{"type":"measure","grade":"B","src":["S44"],"as_of":"2026-06-30","ttl":"V1","subject":"Share of postings with pay information, US","measure":"share","unit":"percent","value":49,"region":"US"}
{"type":"measure","grade":"C","src":["S44","S45"],"as_of":"2026-06-30","ttl":"V1","subject":"Share of postings with pay information, Japan","measure":"share","unit":"percent","lo":14,"hi":97,"region":"Japan","note":"Indeed 97; fantastic.jobs 14; sources conflict"}
{"type":"measure","grade":"C","src":["S45"],"as_of":"2026-04-30","ttl":"V1","subject":"Share of postings with pay information, Australia and Singapore","measure":"share","unit":"percent","lo":10,"hi":19,"note":"Australia 19; Singapore 10"}
{"type":"measure","grade":"C","src":["S68"],"as_of":"2026-07-01","ttl":"V1","subject":"US states plus DC that bar private employers from asking about pay history","measure":"count","unit":"states","lo":18,"hi":20,"region":"US","note":"no federal ban; summaries differ on the count; Virginia effective 2026-07-01"}
{"type":"measure","grade":"C","src":["S68"],"as_of":"2026-07-01","ttl":"V1","subject":"US states requiring the pay range in the posting itself","measure":"count","unit":"states","value":13,"region":"US","note":"18 of 51 jurisdictions have a statewide pay-transparency law"}
{"type":"measure","grade":"C","src":["S69"],"as_of":null,"ttl":"V3","subject":"Share of Just Join IT offers that are B2B contracts, Poland","measure":"share","unit":"percent","value":62.1,"region":"Poland","note":"employment contracts 32 percent; date not shown"}
{"type":"measure","grade":"C","src":["S48"],"as_of":"2026-05-28","ttl":"V3","subject":"Median non-promoted raise, AI/ML engineers, H1 2026","measure":"median","unit":"percent","value":4.4,"note":"R&D median 3.7; all employees 3.4; promotion rate 8.6"}
{"type":"measure","grade":"C","src":["S28"],"as_of":"2025-12-31","ttl":"V3","subject":"OpenAI stock-based compensation per employee, 2025, about 4000 staff","measure":"average","unit":"USD/year","value":1500000,"note":"accounting expense from WSJ data shared with investors; a relay cites 865000 from The Information, period not stated"}
{"type":"measure","grade":"C","src":["S28"],"as_of":"2025-10-01","ttl":"V3","subject":"OpenAI employee tender, Oct 2025","measure":"size","unit":"USD","value":6600000000,"note":"over 600 sellers; about 75 at the 30M cap; month only"}
{"type":"measure","grade":"B","src":["S27"],"as_of":"2026-08-10","ttl":"V3","subject":"OpenAI employee share buyback valuation","measure":"valuation","unit":"USD","value":852000000000,"note":"buyback 7B; confidential IPO filing June 2026"}
{"type":"measure","grade":"C","src":["S30"],"as_of":"2026-11-10","ttl":"V0","subject":"Anthropic IPO price range per Class A share","measure":"range","unit":"USD","lo":70,"hi":78,"note":"COI; 825M shares; pricing expected 2026-11-18, trading 2026-11-19, per CNBC via relays; not confirmed by Anthropic"}
{"type":"measure","grade":"C","src":["S29"],"as_of":"2026-10-26","ttl":"V0","subject":"Anthropic unrecognised RSU expense to begin at IPO","measure":"expense","unit":"USD","value":23700000000,"note":"COI; over about 2.1 years plus 2.9B catch-up at IPO; SBC 1.17B FY2025, 2.19B 6M 2026; relays differ (32.3B all awards); 10-for-1 split 2026-09-17"}
{"type":"measure","grade":"C","src":["S31"],"as_of":"2026-10-26","ttl":"V0","subject":"Anthropic lock-up: share of locked-up shares certain holders may sell on day one","measure":"share","unit":"percent","value":10,"note":"COI; lock-up up to 180 days, staged, some up to a year; S-1 not final"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2025-09-30","ttl":"V4","subject":"OpenAI OpCo certified H-1B LCAs, median annualised lower-bound wage, FY2025","measure":"median","unit":"USD/year","value":285000,"n":101,"note":"FY2026 to Q3: 260000, n=210"}
{"type":"measure","grade":"B","src":["S22","S26"],"as_of":"2026-06-30","ttl":"V4","subject":"Anthropic certified H-1B LCAs in included files; MTS filed base range","measure":"count","unit":"LCAs","value":292,"note":"COI; MTS 133952 to 1380000 per Business Insider via BusinessToday.in"}
{"type":"measure","grade":"A","src":["S65"],"as_of":"2026-05-15","ttl":"V3","subject":"OpenAI posted base band, Staff / Senior Staff Backend Engineer, San Francisco","measure":"posted band","unit":"USD/year","lo":293000,"hi":385000,"note":"employer page opened; offers equity; 7+ years; Member of Technical Staff is the shared internal title"}
{"type":"measure","grade":"M","src":["S65","S66"],"as_of":"2026-05-23","ttl":"V3","subject":"OpenAI San Francisco engineering and research postings, median band midpoint","measure":"median","unit":"USD/year","value":339000,"n":9,"note":"Jan-May 2026; base only; compare Levels.fyi OpenAI L5 base 335000"}
{"type":"measure","grade":"C","src":["S67"],"as_of":"2026-07-01","ttl":"V3","subject":"OpenAI public postings, median midpoint of posted range, all roles","measure":"median","unit":"USD/year","value":308000,"n":570,"note":"aggregator; San Francisco 308000 (n=497); New York 247000 (n=22); base only"}
{"type":"measure","grade":"M","src":["S4","S5","S7","S8","S9","S10","S11","S12","S13"],"as_of":"2026-11-12","ttl":"V3","subject":"Systems titles (HPC, compiler, distributed) TC median over country SWE median, 11 title-country pairs","measure":"premium","unit":"percent","lo":20,"hi":50,"note":"all levels; seniority uncontrolled; inside OpenAI LCA, AI Systems 252500 against SWE 255000"}
{"type":"measure","grade":"M","src":["S1","S3"],"as_of":"2026-11-11","ttl":"V3","subject":"ML title TC median over SWE median: US 1.44; UK 1.17; CH 1.34; SG 1.31; NL 1.28; FR 1.24","measure":"ratio","unit":"multiple","lo":1.17,"hi":1.44,"note":"same-source, same-currency ratios; ML title n unseen outside US and UK"}
{"type":"measure","grade":"M","src":["S1","S16"],"as_of":"2026-11-11","ttl":"V3","subject":"AI Engineer title TC over ML Engineer title TC, p25 to p90","measure":"ratio","unit":"multiple","lo":0.54,"hi":0.56}
{"type":"measure","grade":"M","src":["S1","S3","S17"],"as_of":"2026-11-11","ttl":"V3","subject":"Frontier-lab TC over US ML median","measure":"ratio","unit":"multiple","lo":2.1,"hi":4.4,"note":"OpenAI company median 2.1; Anthropic leaderboard 3.1; OpenAI L5 3.3; Anthropic Staff about 4.4"}
{"type":"measure","grade":"C","src":["S55"],"as_of":"2026-04-16","ttl":"V3","subject":"Atlas Van Lines 59th corporate relocation survey, decision-makers","measure":"sample size","unit":"respondents","value":549,"note":"fielded 2025-12-15 to 2026-01-16; generic US, not GenAI-specific"}
```

```jsonl
{"type":"practice","grade":"B","src":["S46"],"as_of":"2025-02-10","ttl":"V5","area":"negotiation","tactic":"Counter the first offer once","claim":"Counters gained about 12.45% on average","evidence":"Field experiment on about 3,858 tech job seekers; 61% of an encouraged group countered against 54% of controls","verdict":"use","risk":"Ran in 2023-25; best-and-final framing has risen since May 2025"}
{"type":"practice","grade":"C","src":["S46"],"as_of":"2025-02-10","ttl":"V5","area":"negotiation","tactic":"Ask for the offer in writing","claim":"About 40% of offers were verbal and could be withheld","evidence":"Same experiment","verdict":"use-with-care"}
{"type":"practice","grade":"P","src":["S46"],"as_of":"2025-02-10","ttl":"V5","area":"negotiation","tactic":"Ask 10-20% above the offer","claim":"Ask size is untested; outcome average is 12.45%","evidence":"Outcome data only","verdict":"untested"}
{"type":"practice","grade":"C","src":["S14","S46"],"as_of":"2025-12-31","ttl":"V3","area":"negotiation","tactic":"Buy paid coaching","claim":"Clients report +21% to +24% median TC","evidence":"Self-selected clients; an 80% discount did not raise negotiation attempts","verdict":"use-with-care","risk":"Selection bias; vendor COI"}
{"type":"practice","grade":"C","src":["S68"],"as_of":"2026-07-01","ttl":"V1","area":"negotiation","tactic":"Where pay-history questions are banned, give a target range instead of current pay","claim":"No federal ban; about 18-20 states plus DC bar the question for private employers","evidence":"Law-firm and HR summaries that differ on the count","verdict":"use","risk":"Rules vary by state; confirm the jurisdiction of the role"}
{"type":"practice","grade":"P","src":["S59","S65"],"as_of":"2026-11-13","ttl":"V3","area":"negotiation","tactic":"Ask which part of a posted band maps to your level","claim":"Posted bands span levels, for example 260000-630000 GBP at Anthropic London","evidence":"Opened postings say required years of experience correlate with the internal level","verdict":"untested","risk":"COI on Anthropic rows"}
{"type":"practice","grade":"C","src":["S35"],"as_of":"2025-10-20","ttl":"V3","area":"negotiation","tactic":"Gulf: negotiate allowances, flights, schooling and end-of-service basis, not only base","claim":"Reported success rates on pay are low","evidence":"Michael Page 2026 guide via relays: 43% negotiated; 15% succeeded","verdict":"use-with-care","risk":"Relays conflict"}
{"type":"practice","grade":"C","src":["S32"],"as_of":"2025-07-20","ttl":"V3","area":"negotiation","tactic":"Israel: ask for sign-on and options","claim":"AI offers exceed stated salary caps; sign-on up to six salaries","evidence":"GotFriends quotes in Globes","verdict":"use-with-care","risk":"One recruiter source"}
{"type":"practice","grade":"C","src":["S58"],"as_of":"2026-05-12","ttl":"V3","area":"negotiation","tactic":"Japan: negotiate at offer stage","claim":"74.5% negotiated and 90.8% of them got a raise","evidence":"Vendor survey of 393 IT engineers","verdict":"use-with-care","risk":"Small, vendor-run, relayed"}
{"type":"practice","grade":"B","src":["S43"],"as_of":"2026-05-07","ttl":"V1","area":"negotiation","tactic":"Germany: check the collective agreement and level before pay","claim":"Collective agreements keep posting transparency at 12-14%","evidence":"Indeed Hiring Lab","verdict":"use-with-care"}
{"type":"practice","grade":"C","src":["S27","S28","S30"],"as_of":"2026-11-10","ttl":"V0","area":"equity","tactic":"Value frontier-lab equity under last-round, IPO-range and haircut cases; ask about tender eligibility, hold period and lock-up","claim":"Paper value differs from liquid value","evidence":"Two-year hold reported at OpenAI; Anthropic lock-up up to 180 days or longer, staged","verdict":"use-with-care","risk":"Pending IPO pricing; COI"}
{"type":"practice","grade":"C","src":["S22","S23"],"as_of":"2026-06-30","ttl":"V4","area":"visa","tactic":"Treat an LCA wage as a floor and ask which wage level will be filed","claim":"Filed wages are base-only offers at or above prevailing wage","evidence":"One OpenAI record: offered 400000 against prevailing wage 179837","verdict":"use-with-care","risk":"Visa rules not verified"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"US pay by level from two sources for applied-scientist, inference-engineer, agentic-ai-engineer, ai-product-manager; a second source for applied-ai-engineer, ml-platform-engineer and ai-infrastructure-engineer","searched":"Levels.fyi title queries, Axial, Fast AI Jobs, Pave relays, LCA aggregators","note":"only Amazon Applied Scientist, Levels.fyi MLOps and Applied AI Engineer pages found; no inference, agentic or AI product manager dataset"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"US pay records for roles 13-24 and leadership roles","searched":"not searched individually","note":"only UAE AI Product Manager and Head of AI, and Axial manager and director ceilings"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"ML-engineer city medians for Boston, Austin, Seattle, New York","searched":"Levels.fyi searches","note":"only SWE city medians surfaced"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"US employer-posted ranges beyond OpenAI","searched":"Greenhouse and Ashby searches","note":"one Anthropic page blocked by bot detection and not retried; no Anthropic US posting opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"LCA wage ranges for AI/ML titles at the top FY2025 filers (Amazon, Microsoft, Meta, Google, Apple)","searched":"aggregator searches","note":"DOL files not fetched; dol.gov is outside the session network allow-list"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"ML or AI engineer pay with n for Ireland, Australia, Japan, Sweden, Saudi Arabia, Abu Dhabi; Poland beyond one posting and a relay","searched":"Levels.fyi, recruiter and news searches","note":"Levels.fyi AI Engineer Poland .md median of PLN 49,505 cannot be annual pay and was not used; Swedish ads often say pay is by agreement"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Official statistics with an AI-specific occupation (ONS, MOM, ABS, MHLW, CBS Israel)","searched":"news and aggregator queries","note":"MHLW information-and-communications average of about 6.3M JPY cited second-hand only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Frontier-lab retention grants, refreshers and sign-on structures; Anthropic April 2026 tender details","searched":"news searches","note":"tender and IPO coverage only; April tender from low-grade relays"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Continental Europe negotiation norms: works councils, notice periods, counter-offers","searched":"one regional search","note":"only Hiring Lab and SHRM notes"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Singapore, Saudi and Australian negotiation outcomes; official Gulf end-of-service sources; salary-history rules in Canada","searched":"regional searches","note":"none opened or searched"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"GenAI-specific relocation amounts (visa, flights, temporary housing, tax equalisation)","searched":"relocation survey searches and posting text","note":"generic US surveys and assistance-offered lines only"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Candor, Doody, Comprehensive.io and Carta candidate-programme primary pages","searched":"vendor searches","note":"no primary page found or opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Robert Half Zurich guide; Michael Page UAE guides (2026, 2027)","searched":"not reopened","note":"K7 and K19 rest on relays"}
```
