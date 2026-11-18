---
id: "T0-70"
title: "Market Pulse: Hiring Volume, Layoffs, Funding and Employer Mix"
date: "2026-11-13"
status: complete-with-gaps
topic: "market-pulse-hiring-layoffs-funding"
tags: ["market-pulse", "hiring-volume", "layoffs", "venture-funding", "entry-level", "india-gcc"]
informs_decisions: ["D-002", "D-003"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and page fetch. Anthropic is the author's developer, so rows about Anthropic are marked COI."
evidence_window: "2025-11-18 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 6
---

# T0-70: Market Pulse: Hiring Volume, Layoffs, Funding and Employer Mix

This session re-measures the knowledge base's (KB) October 2026 market signals. [S#] points to a row in the Sources & Evidence Ledger. Grades follow EGP-1.0: A primary source opened; B established secondary source or platform data; C third-party or single-source analysis; D memory or judgement; E unverifiable; M my own calculation, with inputs shown. The brief anchors the pulse at 2026-11-11. Searches and page fetches ran on 2026-11-13, which is the retrieval date for every ledger row. Posting counts are V1 (31 days). Rows about Anthropic, the author's developer, carry COI. The KB is not cited as evidence. URLs in the ledger are as returned by search or fetch on 2026-11-13.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | JobsPipe's AI Engineer counts (1,697 US; 398 India; 3,944 global) will differ by more than 10% from the KB reading, because the platform advertises daily updates. | 70% | D |
| P2 | Monthly AI-cited US layoff announcements kept rising after September 2026. | 60% | D |
| P3 | Q3 2026 venture funding fell below Q2 2026 but stayed above Q3 2025, with AI above 60% of dollars. | 75% | D |
| P4 | Entry-level share of AI postings is low, and applications per job exceed Greenhouse's 2025 figure of 244. | 65% | D |
| P5 | Indian AI/ML posting growth beat overall white-collar growth by double digits in October 2026. | 80% | D |
| P6 | Only AI Engineer, MLE and FDE exceed 50 postings, and no title crosses the quorum within a month. | 70% | D |

## Research Question

**Decision question.** Did hiring volume, layoffs, funding, employer mix, entry-level hiring or pay pressure change enough since the KB's October 2026 snapshot to alter D-002, D-003, `career/01-landscape/market-overview.md`, `career/01-landscape/employer-landscape.md` or `data/role_scores.json`? Which of K1–K6 still hold?

**Sub-questions.** The eight coverage items in the brief: recount, quorum changes, employer events, funding, applicant pressure, entry level, India, signals check.

**Scope as applied.**
- *Dates.* The brief's anchor is 2026-11-11 and the session ran on 2026-11-13. A JobsPipe count dated 2026-10-19 expires on 2026-11-19 under V1.
- *Same platform, same query.* Achieved for JobsPipe title-by-country pages (AI Engineer, MLE) and for Fast AI Jobs role pages. Not achieved for Skillenai (no page surfaced), for JobsPipe's FDE and Research Engineer pages (not retrievable), or for Go Fractional beyond one undated page.
- *"AI employers".* I read this as frontier labs, big tech, AI startups, and enterprises or consultancies that post AI titles.
- *Layoffs versus hiring.* Layoffs and buyouts are logged as events. Only posting counts, official statistics and platform indices are treated as measured change.
- *Pay.* Out of scope in detail. Posted-pay disclosure and the advertised-pay premium for AI-mentioning postings are noted as pay-pressure signals.
- *Nine signals.* The brief supplies six claims (K1–K6). The KB's nine-signal list was not supplied.

**Method.** About 55 searches and page fetches on 2026-11-13. Pages I opened are marked Read in the ledger. Pages seen only as search extracts are marked Extract. Corroboration pairs:
- Layoffs: Challenger via three outlets.
- Funding: Crunchbase and PitchBook-NVCA.
- Demand: Dice/Lightcast, JOLTS and BLS.
- India: Naukri, foundit and Zinnov–Nasscom.
- FDE: six counts.
- Research Engineer: Fast AI Jobs and AI Pulse.
- H-1B: two law-firm sources.

Falsification searches, each documented in Detailed Findings:
- Did JobsPipe refresh?
- Are AI-cited layoffs rising?
- Are AI roles closed to juniors beyond the tech-wide pattern?
- Is there a hiring bust?
- Did any AI employer announce a freeze in the window?
- Did funding collapse?
- Is the AI-mention share or pay premium for developer postings rising?

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | JobsPipe's AI Engineer title pages read 3,944 global, 1,697 US and 398 India on 2026-11-13, identical to the KB reading dated 2026-10-19. The MLE pages read 2,157 global (1,084 US; 90 India). JobsPipe's Labour Market Pulse carries a snapshot dated 2026-11-13 and is refreshed daily, so the frozen values are specific to the title pages. A JobsPipe salary page shows 1,850 AI Engineer postings (undated), against 1,697 on the US jobs page. JobsPipe's own method note says raw counts reflect the crawl as well as the market and recommends shares. Read JobsPipe counts as a cross-section, not a trend. | S1–S5, S63, S66; inference is M | B / M |
| KF2 | Fast AI Jobs (last updated 2026-11-11) lists 352 AI Engineer, 298 MLE, 1,007 FDE and 223 Research Engineer postings at AI startups. Cached extracts from 2026-07-30 to about 2026-08-03 gave 275, 227, 779 and 171. That is +28%, +31%, +29% and +30% (M). The near-uniform rise suggests partly platform coverage, not title-specific demand. | S9–S13 | B / M |
| KF3 | No title falls below the 50-posting quorum. AI Engineer, MLE and FDE remain far above it. Research Engineer is above it on two platforms: 223 on Fast AI Jobs (baseline 171) and 569 in AI Pulse's category count (2026-11-12). AI Pulse's category counts also exceed 50 for AI Product Manager (570), AI Safety (89) and AI Engineering Manager (68), but AI Pulse is outside the KB's platform set and its categories are not the KB's titles. Applied Scientist (23 on Fast AI Jobs) and the Fractional CAIO page (10 posts in a rolling 90 days) are below. Nineteen titles were not measured. | S12, S14, S58, S65 | B / C |
| KF4 | FDE counts range from 260 to 1,276 across six sources dated 2026-10-12 to 2026-11-11, because titles are defined differently. Plank counted 1,276 postings at 547 companies on 2026-10-30. fdejobslist shows 391. One analyst counted 260 distinct roles at 44 companies on 2026-10-12. Of the first 50 Fast AI Jobs rows (sorted by posting date), 23 are individual-contributor FDE titles, 5 are manager or leader titles and 22 are adjacent titles such as deployment strategist, GTM engineer or field engineer (M). Every definition is far above 50. | S9, S16–S20 | C / M |
| KF5 | Announced US job cuts fell to 43,994 in October 2026, down 71% on October 2025. AI was cited for 1,265 cuts (under 3% of the month) against a May peak of 38,579, and for 121,401 year-to-date (about 20% of 617,189). Market and economic conditions lead the stated reasons year-to-date (130,531). Technology-sector cuts of 5,576 were the lowest monthly figure of 2026. | S22, S23, S25 (corroborated) | B |
| KF6 | Company actions diverge from the aggregate. Microsoft offered voluntary exits to about 60,000 staff on 2026-10-26, which Challenger did not count in October. Canva announced a 22% cut (1,271 people) on 2026-11-04. Qualcomm began India cuts, with about 1,000 roles reported at risk. These are announcements, not measured changes in AI-role hiring. No hiring-freeze announcement at an AI employer dated 2026-10-01 to 2026-11-13 was found. | S24–S30, S62 | B / C |
| KF7 | Demand indicators rose. Dice/Lightcast report US tech postings +20% and AI/ML postings +91% year on year in October 2026. JOLTS openings were 7.5 million in September (7.19 million in August). BLS reports payrolls +165,000 in October, with unemployment at 4.1%. | S45–S47 | B |
| KF8 | Q3 2026 funding stayed high but cooled. Crunchbase counts USD 159bn globally (−25% on Q2's USD 212bn; +53% on Q3 2025), with AI at 64%. PitchBook-NVCA counts USD 98.4bn in the US (about 40% below Q2), with AI at 65.9% of Q3 and 82.7% of year-to-date value. A record 27 rounds of USD 1bn or more drove the total. Anthropic filed an updated S-1 on 2026-11-10 seeking up to USD 88.5bn across an IPO and a placement [COI]. | S31–S34 | B |
| KF9 | Applicant pressure is high, and no AI-specific series exists. Greenhouse measured 244 applications per job in 2025, up 111% from 116 in 2022. Ashby reports 291 applications per hire in Q1 2026 and an inbound-applicant offer rate near 0.2%, against 7.3% for referrals (secondary report). Technical roles take a median of 76 days to a first hire (Ashby, via a compilation). Pay pressure is flat to slightly lower on JobsPipe's advertised-pay measure: 39.5% of developer postings named AI in 2026-09-01 to 2026-09-18 against 39.1% in the 30 days to 2026-11-13, and the advertised premium was +28% then and +25% as of 2026-11-13 (not like-for-like; M). | S35–S38, S63, S64 | B / C / M |
| KF10 | The entry-level squeeze is tech-wide, not AI-specific. Entry-level roles were 4.5% of US software postings in Q1 2026 (Indeed Hiring Lab). JobsPipe finds 16.4% of AI-titled postings entry level against 38.3% of all postings (US 10.4% against 35.8%), yet within ICT occupations AI roles are 15.4% entry level against 12.5%. AI Pulse classifies 137 of 11,652 open AI roles (1.2%) as entry level. The NY Fed puts graduate unemployment at 5.2% in Q3 2026, its lowest in over a year. Anthropic reports junior staff fell from 27% to 9% of its technical hires [COI; a share, not a count]. | S8, S39–S44, S65 | B / C |
| KF11 | India shows faster AI/ML growth than the market. Naukri's October 2026 report has AI/ML +32% and GCC +18% year on year. Overall hiring rose +14%, which is flattered by a soft October 2025 base. September was AI/ML +20% and GCC +4%. foundit projects 510,452 GCC hires in 2026, 64% needing AI, data or automation skills. Zinnov–Nasscom count 2,117 GCCs with 2.36 million staff. JobsPipe's India counts did not change. | S3, S48–S53 | B / C |
| KF12 | Employer mix differs by title. AI Engineer postings on JobsPipe are led by consultancies and financial firms (PwC 67, Capital One 34, TCS 31, Deloitte 31 globally). MLE postings are led by consumer-tech and autonomy firms (TikTok 148, Waymo 53, Pinterest 33). FDE postings are led by AI platform vendors (Palantir 77 of 310 open roles and Databricks 94 of 870 on 2026-09-08). | S1, S2, S3, S4, S21 | B / C |
| KF13 | Two rule events bear on hiring. As of early November 2026 employers need not pay the USD 100,000 H-1B fee, because two federal courts blocked it. Appeals are pending, and a separate USD 103,265 DHS proposal is not final. The EU Digital Omnibus on AI was signed on 2026-07-08, deferring high-risk obligations to 2027-12-02 and 2028-08-02. Pointers only; confirm with the official sources. | S54–S56 | B (V0) |
| KF14 | Signals check: K1 updated, K2 stale, K3 unverifiable, K4 confirmed, K5 updated, K6 stale. The advice on AI Engineer, MLE and FDE does not change. There is one status candidate (Research Engineer), three category-level candidates on a non-KB platform, and one data-quality flag (JobsPipe title pages). | Repository Deltas | M |

## Recommendation

**Decision rules for job seekers**

1. **Start with AI Engineer, MLE and FDE titles.** Add Research Engineer if you can show research-engineering output (training code, evaluations, a paper).
   - *Failure mode:* AI Engineer counts include consultancy and bench postings, and FDE counts include sales-adjacent titles. A large count is not a low bar.
   - *Changes if:* a refreshed JobsPipe reading puts US AI Engineer below about 1,500, or Fast AI Jobs AI Engineer falls below 275.
2. **Treat layoff and buyout headlines as employer-specific.** Before treating Microsoft, Canva or Qualcomm news as a freeze, check the specific team's open requisitions on the employer's own careers page.
   - *Failure mode:* careers pages carry stale requisitions, and voluntary exits can change team capacity within weeks.
   - *Changes if:* an AI employer announces a named freeze (none found in the window).
3. **Do not rely on volume applications.** With about 291 applications per hire and about 0.2% inbound offer rate against 7.3% for referrals (C), spend effort on referrals and direct outreach to a list of 10–15 employers.
   - *Failure mode:* Ashby's customers skew to tech and startups, and referred candidates are self-selected.
   - *Changes if:* AI-role-specific funnel data appears (absent as of 2026-11-13).
4. **Entry-level, US.** Target structured new-graduate and early-career postings (for example, new-graduate FDE and MLE roles listed on Fast AI Jobs and JobsPipe) and do not read the squeeze as AI-specific.
   - *Failure mode:* entry-level postings are only 1–11% of the pool depending on the platform, and adding AI skills alone does not escape a tech-wide pattern.
   - *Changes if:* the NY Fed's Q4 2026 update (expected about February 2027 from its quarterly cadence) reverses the Q3 improvement.
5. **India-based seekers.** Weight GCC and AI/ML postings, and the GCC early-career intake (0–3 years is 30% of GCC hiring, +18% year on year, per foundit). Do not plan around either H-1B outcome.
   - *Failure mode:* Naukri's October growth has a base effect, platform indices are not hiring counts, and GCC layoffs (Qualcomm India) show exposure.
   - *Changes if:* the Naukri AI/ML series falls below +10% in a month without a base effect.
6. **FDE applicants.** Check the title and the duties. About half of the "FDE" rows in the sample are strategist, GTM or field roles with different skills.
   - *Failure mode:* time spent on roles that look like FDE but screen for sales skills.
   - *Changes if:* a title-exact recount shows a materially higher share of IC FDE roles.

**For the KB maintainers**
- Re-measure JobsPipe before 2026-11-19, and record counts as cross-sections (JobsPipe's own guidance) or use its Pulse shares.
- Mark `research-engineer` as a quorum-crossing candidate until a recount under the KB's own method. Treat `ai-product-manager`, `ai-engineering-manager` and `ai-safety-researcher` as category-level candidates (AI Pulse, C) that need a KB-method recount.
- Store Fast AI Jobs counts with the coverage caveat.
- Reword K5 (the ranking claim fails in the 15-country table).

## Alternatives Considered

| Option | Verdict | Reason | Failure mode |
|---|---|---|---|
| Wait for a better market | Rejected | Demand indicators (Dice, JOLTS, BLS) rose through October 2026 (S45–S47). | Indicators are aggregate, not AI-role hires. |
| Mass-apply | Rejected | About 291 applications per hire and 0.2% inbound offer rate (S37). | Only some employers ration applications this way. |
| Referral-led targeted search | Preferred | 7.3% against 0.2% offer rate (S37, C). | Slower; needs a network. |
| Pivot to FDE | Conditional | FDE is the largest title cluster (S9, S16). | Category includes adjacent roles. |
| GCC route (India) | Preferred for India | GCC hiring +18% year on year; fresher intake growing (S48, S52). | Layoff exposure; platform indices. |
| Read funding as a hiring signal | Rejected | AI is 82.7% of US deal value year-to-date, with exits weak (S32). | Funding and hiring are not linked one-to-one. |
| Read layoffs as a hiring signal | Rejected | Challenger counts stated reasons only, and buyouts are excluded (S22, S62). | None; it is a data-quality point. |
| Read JobsPipe counts as a trend | Rejected | JobsPipe's own note says counts reflect crawl mix, and title pages did not move (S1–S3, S63). | Shares move with the denominator. |

## Detailed Findings

### 1. Recount (item 1)

| Title (role ID) | Platform · query | Region | Previous count and date | New count and date | Change | Grade |
|---|---|---|---|---|---|---|
| AI Engineer (`ai-engineer`) | JobsPipe · `/jobs/ai-engineer` | Global | 3,944 · corpus 2026-10-19, page unchanged 2026-11-02 (brief) | 3,944 · page read 2026-11-13 | 0 | B |
| AI Engineer | JobsPipe · `/jobs/ai-engineer/usa` | US | 1,697 · 2026-10-19 | 1,697 · 2026-11-13 | 0 | B |
| AI Engineer | JobsPipe · `/jobs/ai-engineer/india` | India | 398 · 2026-10-19 | 398 · 2026-11-13 (search snapshot) | 0 | B |
| MLE (`ml-engineer`) | JobsPipe · `/jobs/machine-learning-engineer` | Global | not in brief | 2,157 · 2026-11-13 | baseline | B |
| MLE | JobsPipe · `/usa` | US | not in brief | 1,084 · 2026-11-13 | baseline | B |
| MLE | JobsPipe · `/india` | India | not in brief | 90 · 2026-11-13 | baseline | B |
| FDE (`forward-deployed-engineer`) | JobsPipe | all | not in brief | Gap: page not retrievable | n/a | n/a |
| AI Engineer | Fast AI Jobs · `/jobs/role/ai-engineer` | AI-startup boards, global | 275 · page dated 2026-07-30 | 352 · 2026-11-11 | +77 (+28%) | B / M |
| MLE | Fast AI Jobs · `/jobs/role/ml-engineer` | same | 227 · cached extract, postings to 2026-07-30 | 298 · 2026-11-11 | +71 (+31%) | B / M |
| FDE | Fast AI Jobs · `/jobs/role/forward-deployed-engineer` | same | 779 · cached extract, postings to 2026-07-31 | 1,007 · 2026-11-11 | +228 (+29%) | B / M |
| Research Engineer (`research-engineer`) | Fast AI Jobs · `/jobs/role/research-engineer` | same | 171 · cached extract, postings to 2026-07-31 | 223 · 2026-11-11 | +52 (+30%) | B / M |
| Applied Scientist (`applied-scientist`) | Fast AI Jobs | same | none | 23 · extract with postings to 2026-10-23 | n/a | B |
| Fractional AI Leader (`fractional-ai-leader`) | Go Fractional · Chief AI Officer page | global | none | 10 posts in a rolling 90 days; 4 open · undated extract | n/a | B |

Notes:
- **Query scope.** JobsPipe pages are title-by-country pages built from 30+ ATS feeds and boards, deduplicated. Fast AI Jobs role pages count roles on AI-startup career pages only. Fast AI Jobs has no US filter in this reading.
- **JobsPipe title pages cannot serve as a new measurement.** Values and sample listings match the KB reading. The JobsPipe Labour Market Pulse shows a snapshot dated 2026-11-13 and a cached extract of the same page shows 2026-10-16, so the platform's aggregate pages refresh while these title pages did not move (S63). A JobsPipe AI Engineer salary page reports 1,850 live postings (undated), which differs from the 1,697 on the US jobs page; page definitions or snapshot ages differ (S66).
- **JobsPipe's own method note.** Counts measure the crawl as much as the market, because the board mix changes week to week; JobsPipe recommends shares and asks readers to quote figures as a cross-section, not a trend (S63).
- **The highest LinkedIn job ID in the MLE sample (4451522517) exceeds that in the AI Engineer US sample (4451391326).** That is consistent with different snapshot ages, but it assumes ID order tracks posting order (D).
- **Fast AI Jobs baselines are undated cached extracts.** Treat the +28% to +31% changes as indicative.
- **Entry-level filter counts on JobsPipe (S6).** AI Engineer 275, which is 7.0% of 3,944; MLE 240, which is 11.1% of 2,157 (M).
- **Pay disclosure (S1, S4).** MLE median posted base is USD 211k (IQR 177k–257k) across 965 of 2,157 postings. 1,107 of 3,944 AI Engineer postings state pay.

### 2. Quorum changes (item 2)

| Role ID | Evidence | Versus 50 | Flag |
|---|---|---|---|
| `ai-engineer` | JobsPipe 3,944 / 1,697 US / 398 India; Fast AI Jobs 352 | above | none |
| `ml-engineer` | JobsPipe 2,157 / 1,084 / 90; Fast AI Jobs 298 | above | none |
| `forward-deployed-engineer` | Fast AI Jobs 1,007; five other counts 260–1,276 | above | none; definition caveat |
| `research-engineer` | Fast AI Jobs 223 (2026-11-11), baseline 171; AI Pulse category 569 (2026-11-12, C) | above on two platforms | **Candidate crossing (V to E)**; needs a recount under the KB's method. Fast AI Jobs covers AI startups only, and the page may fold in "Research Engineer / Scientist" titles. |
| `ai-product-manager` | AI Pulse category "AI Product Manager" 570 (2026-11-12, C) | above on a non-KB platform | Category-level candidate; needs a KB-method recount |
| `ai-engineering-manager` | AI Pulse category "AI Engineering Manager" 68 (2026-11-12, C) | above on a non-KB platform | Category-level candidate; needs a KB-method recount |
| `ai-safety-researcher` | AI Pulse category "AI Safety" 89 (2026-11-12, C) | above on a non-KB platform | Category-level candidate; the category may include trust-and-safety roles |
| `applied-scientist` | Fast AI Jobs 23 (extract, postings to 2026-10-23) | below | none (status V unchanged) |
| `fractional-ai-leader` | Go Fractional CAIO: 10 posts in a rolling 90 days | below | none |
| `agentic-ai-engineer` | Exact-title postings appear in JobsPipe samples (S7) but no count; agentic named in 59.3% of AI Engineer postings (counted 2026-09-10); agentic AI is 1.7% of salaried postings, ahead of machine learning at 1.5% (S64) | unknown | cannot confirm either way |
| 19 other titles | not retrieved | unknown | see Absences |

AI Pulse's categories are aggregator-defined and undisclosed; its "AI/ML Engineer" category alone is 8,787 of 11,652 roles (75%, M). Treat its counts as corroboration of direction, not as quorum evidence under the KB's rule.

### 3. Employer mix, announcements, freezes and layoffs (item 3)

**3a. Who posts (as of 2026-11-13)**

| Title · platform | Top employers by open postings | Reading |
|---|---|---|
| AI Engineer · JobsPipe global | PwC 67; Capital One 34; TCS 31; Deloitte 31; Jack & Jill 25; Mastercard 20; Infosys 20; American Express 19 | Consultancies, IT services and financial firms use the title heavily |
| AI Engineer · JobsPipe US | Capital One 33; TCS 22; American Express 16; Bristol Myers Squibb 14; Deloitte 13; Infosys 12 | Same pattern |
| AI Engineer · JobsPipe India | PwC 19; Deloitte 11; Teradata 9; Infosys 6; TCS 5; HCLTech 4; Barclays 4 | Services-led |
| MLE · JobsPipe global | TikTok 148; Waymo 53; Pinterest 33; Adobe 31; Apple 25; ByteDance 21 | Large consumer-tech and autonomy firms |
| FDE · employer boards, 2026-09-08 (S21) | Palantir 77 of 310 open roles (25%); Databricks 94 of 870 (11%) | Concentrated in a few platform vendors (C) |
| AI Engineer / FDE · Fast AI Jobs | OpenAI, Databricks, Scale AI, Snorkel AI, Turing and Celonis appear repeatedly in the first rows | AI-platform and startup employers |

**3b. Events table.** "Measured effect" means a change in posting counts or official statistics attributable to the event.

| Date | Employer | Event | Type | Measured effect | Source | Grade |
|---|---|---|---|---|---|---|
| 2026-10-16 | Anthropic [COI] | Own report: junior share of technical hires fell from 27% to 9%, and junior share of technical staff from 21% to 14%, while headcount grew | hiring composition | share, not count | S44 | C |
| 2026-10-22 | Barclays | About 5,000 job cuts tied to AI cost savings, plus over 200 in investment banking | layoff announcement | none | S59 | C |
| 2026-10-26 | Microsoft | Voluntary exit offer to about 60,000 eligible staff (about 27% of 223,000) in the US, UK, Canada and India, level 70 and below; excluded from Challenger's October total | buyout, not a layoff | none | S26, S62 | B |
| week to 2026-11-04 | Amazon | 250 devices-and-services roles and 95 software, product and operations roles, as reported in the tracker | layoff | none | S27 | B |
| 2026-11-04 | Canva | Global workforce cut of 22% (1,271 people), per Canva's own update | layoff | none | S27 | B |
| 2026-11-05 (listing) | Block, Fiserv, Circle, Angi, Axonius, Bria | Block second round of 2026 cuts; Fiserv 3,000; Circle 5%; Angi 300; Axonius 22% of Israeli developers (66) in an AI-driven restructuring; Bria 33% (20) | layoffs | none | S28 | C |
| 2026-11 (reported 11-11) | Qualcomm | India cuts in Bengaluru and Hyderabad after a global reduction announced in October; about 1,000 roles reported at risk, with extra pay for early exits | layoff | none | S29 | C |
| 2026-11-12 (report) | Zomato, Apple, Deloitte | Zomato about 250 roles and a Hyderabad support centre closure; Apple 147 permanent job losses in California (state filing, as reported); Deloitte cuts in Australia and the UK | layoffs | none | S30 | C |
| 2026-11-10 | Anthropic [COI] | Updated S-1: IPO plus private placement of up to USD 88.5bn at a valuation of up to USD 1.4tn; Nasdaq listing expected in November | funding / liquidity | none | S34 | B |
| 2026-10 (through 10-31) | US employers (non-AI) | Seasonal hiring plans of 470,400 through October, up 26% | hiring plans | none for AI roles | S23, S25 | B |

**Hiring freezes.** A search for freeze announcements at AI employers dated 2026-10-01 to 2026-11-13 found none. Older items exist but predate the window and were not verified to the primary source: Meta's AI-division pause (reported 2025-08-21), Salesforce's engineer-hiring pause (since 2025), and an SAP freeze reported with a 2 July date and an unconfirmed year. I report them as absences, not findings.

### 4. Funding (item 4)

| Period | Crunchbase global (USD bn) | AI share (Crunchbase) | PitchBook-NVCA US deal value (USD bn) |
|---|---|---|---|
| Q3 2025 | 104 | about 50% (64% less 14 points, M) | not retrieved |
| Q1 2026 | about 308 (679 − 212 − 159, M) | not retrieved | 267 as first published 2026-04-03 |
| Q2 2026 | 212 | not retrieved | H1 total 412.7 (AI 355.9, 86%) |
| Q3 2026 | 159 (−25% on Q2; +53% on Q3 2025) | 64% (USD 102bn) | 98.4 (about −40% on Q2); AI 65.9% of Q3 and 82.7% of year-to-date |

- **Method.** Crunchbase data are as of 2026-10-02 and early-stage figures lag. PitchBook-NVCA reports US deal value with an estimated 5,012 deals in Q3.
- **Concentration.** Crunchbase counts 27 rounds of USD 1bn or more in Q3 (14 in Q1, 16 in Q2); Databricks and Safe Superintelligence raised USD 5bn each. PitchBook reports that AI's share of each quarter's deal value has shrunk since January even though its year-to-date share is a record.
- **Exits and funds.** Per PitchBook as reported by SiliconANGLE, one deal (SpaceX's USD 60bn purchase of Anysphere, the maker of Cursor) made up 53.1% of Q3 exit value, and only 211 emerging managers closed a fund against 927 in 2022 (S32).
- **Q3 deals.** Nvidia's bid for Hugging Face (USD 12.9bn), AMD's intended World Labs purchase (USD 8.2bn) and Stripe–OpenRouter (USD 7.5bn) (S31).
- **Verdict.** P3 holds: Q3 fell from Q2 and stayed above Q3 2025, with AI above 60%. Two trackers agree on direction.

### 5. Applicant pressure and pay signals (item 5)

| Measure | Value | Source | Period · method | Grade |
|---|---|---|---|---|
| Applications per job | 244 (2025) vs 116 (2022), +111% | Greenhouse | 6,000+ companies, 640 million+ applications | B |
| Applications per recruiter | 746 (2025) vs 146 (2022) | Greenhouse | same | B |
| Greenhouse customer series | 95 (2025) vs 28 (2021) | Greenhouse via S36 | data pulled 2025-08; conflicts with 244 | C |
| Applications per hire | 291 (Q1 2026) vs about 100 (early 2021) | Ashby via S37 | 109 million applications, 247,000 jobs | C |
| Offer rate, inbound vs referred | about 0.2% vs 7.3% | Ashby Talent Trends via S37 | offer rate, not hire rate | C |
| Hire rate implied by 291 | 0.34% | M (1/291) | | M |
| Time to first hire, technical | median 76 days (business roles 56) | Ashby via S38 | Q1 2026 | C |
| Applicants per opening | about 30 (iCIMS, 2026-08) | via S38 | "per opening" differs from "per job" | C |
| AI-mention share of software-developer postings | 39.5% (2026-09-01 to 2026-09-18, salaried postings) vs 39.1% (rolling 30 days to 2026-11-13) | JobsPipe S64, S63 | different denominators | B / M |
| Advertised-pay premium, AI-mentioning vs other developer postings | +28% (median USD 169,538 for AI postings) vs +25% (USD 162,000 vs USD 129,234) | JobsPipe S64, S63 | not like-for-like; advertised, not paid | B / M |
| Whole-market AI-mention share | 6.7% of postings (2026-09-01 to 2026-09-18) | JobsPipe S64 | | B |
| AI Engineer advertised pay | median USD 181k (P25 144k; P75 215k) on 1,850 postings | JobsPipe S66 | undated | B |
| MLE advertised base | median USD 211k (IQR 177k–257k), 965 postings with pay | JobsPipe S4 | | B |

- **No AI-specific funnel series.** None of the applicant-pressure rows is specific to AI roles (Absences).
- **Pay pressure.** The two JobsPipe windows show a flat AI-mention share and a premium that is 3 points lower, but windows and denominators differ, and JobsPipe itself says a single month is a photograph, not a direction. I make no claim of tightening or easing beyond "no rise".
- **Posted-pay disclosure.** 45% of MLE postings on JobsPipe state pay (965 of 2,157), and 28% of AI Engineer postings (1,107 of 3,944).

### 6. Entry level (item 6)

| Signal | Value | Source | Grade |
|---|---|---|---|
| Entry-level share of US software postings, Q1 2026 | 4.5% (senior 69.3%) | Indeed Hiring Lab via S39, S43 | B |
| AI-titled postings, entry-level share, all countries | 16.4% vs 38.3% for all postings | JobsPipe, 2026-10-11 | B |
| Same, US | 10.4% vs 35.8% | JobsPipe | B |
| Same, inside ICT occupations | AI roles 15.4% vs 12.5% for tech | JobsPipe | B |
| JobsPipe entry-level filter counts | AI Engineer 275 (7.0%); MLE 240 (11.1%) | S6, M | B / M |
| AI Pulse seniority mix, 2026-11-12 | entry 137 (1.2%), mid 5,631 (48.3%), senior 4,231 (36.3%), leadership 1,653 (14.2%) of 11,652 (M) | AI Pulse S65 | C |
| Graduate unemployment (aged 22 to 27) | 5.2% in Q3 2026 (5.6% in Q2; 5.8% a year earlier); underemployment 42.5% | NY Fed via S41, S42, S43 | B |
| AI/ML engineer postings, 30 days to 2026-10-15 | 6% entry level, 63% senior (n = 2,698) | SimpleApply S61 | C |
| Early-career software developer employment (22–25) | down nearly 20% from the 2024 peak | Stanford AI Index 2026 via CNBC S40 | C |
| Anthropic technical hires | junior share 27% to 9% [COI] | Anthropic S44 | C |

- **Reading.** Postings tilt senior, but the AI-specific closure story is not supported. Within tech, AI roles are no more senior than other roles. The NY Fed attributes nearly two-thirds of the rise in young-graduate unemployment to remote-work exposure (S60).
- **Spread across platforms.** The entry-level share of AI roles runs from 1.2% (AI Pulse) to 6–7% (SimpleApply, JobsPipe filter) to 10.4% (JobsPipe, US AI-titled postings), so definitions drive the level. Compare direction, not level.
- **Limits.** Anthropic's figure is one employer's share of hires, not a count and not a market measure.

### 7. India (item 7)

| Item | Value | Source | Grade |
|---|---|---|---|
| Naukri JobSpeak index, October 2026 | 2,836 vs 2,480 (+14%); base effect noted | S48, S49 | B / C |
| AI/ML hiring, October / September | +32% / +20% year on year | S48, S50 | B |
| GCC hiring, October / September | +18% / +4% year on year | S48, S50 | B |
| IT/software services; software engineering and QA, October | +5%; +1% | S49 | C |
| Freshers, September | +1% overall; AI/ML freshers in IT +19% | S50 | C |
| GCC base, FY2026 | 2,117 GCCs, 3,728 units, 2.36 million staff, USD 98.4bn | Zinnov–Nasscom via S51 | B |
| GCC hires projected for 2026 | 510,452; 64% need AI/data/automation; 0–3 years 30% (+18%) | foundit via S52 | B |
| Greenfield GCCs, January–August 2026 | 111 vs 100 in all of 2025 | UnearthIQ via S53 | C |
| JobsPipe India counts | AI Engineer 398 (no change); MLE 90 | S3, S5 | B |
| India layoffs | Qualcomm India (about 1,000 at risk); Zomato about 250; Microsoft's offer covers India | S26, S29, S30 | B / C |

Indian AI-startup hiring: not found (Absences).

### 8. Signals check (item 8)

| K | Claim | Verdict | Evidence | Caveat |
|---|---|---|---|---|
| K1 | Only AI Engineer, MLE and FDE exceed the quorum; agentic, context and evaluation work are skills, not titles | updated | Research Engineer 223 on Fast AI Jobs (baseline 171) and 569 on AI Pulse; AI Product Manager 570, AI Safety 89 and AI Engineering Manager 68 on AI Pulse (C, category-level); agentic in 59.3% of AI Engineer postings (counted 2026-09-10) and 1.7% of salaried postings ahead of machine learning at 1.5% (S7, S12, S64, S65) | "Only" is not supported for Research Engineer; the skill clause holds on JobsPipe skill shares; the other candidates are outside the KB's platform set |
| K2 | JobsPipe: 1,697 US, 398 India, 3,944 global | stale | Identical values on 2026-11-13 (S1–S3); the Pulse page refreshes daily (S63); JobsPipe's method note warns that counts reflect crawl mix | Re-measure before 2026-11-19; title pages not refreshed |
| K3 | About 66% of US AI-engineering postings are IC; 35% mid-level; 31% senior | unverifiable | No source found. JobsPipe labels 24.6% of AI Engineer postings senior; SimpleApply reports 63% senior; AI Pulse shows 36.3% senior and 48.3% mid-level across all AI roles (S7, S61, S65) | Seniority definitions differ |
| K4 | Applications per job +110% (2022–2025); cold applications hire about 0.2% | confirmed | Greenhouse 116 to 244 (+111%); inbound offer rate about 0.2%; 291 per hire implies 0.34% (S35, S37) | 0.2% is an offer rate; other measures 0.3–0.5% |
| K5 | India highest AI-title share of five countries (3.0% vs 1.3% US); about twice US entry-level share (21.2% vs 10.4%) | updated | The India–US figures match JobsPipe's table of 2026-10-11. Singapore is 3.7% in a 15-country table, and five other countries have a higher entry-level share of AI roles than India (S8) | Ranking holds only within the KB's five-country set |
| K6 | Evaluation in 68.2% of 198 companies' postings; 52.4% of agent teams run offline evals | stale | LangChain survey: 52.4% offline, 37.3% online (n = 1,340; fielded 2025-11-18 to 2025-12-02) (S57); 68.2% not traced | Vendor survey with ecosystem skew |

### 9. Regulatory events (V0 unless stated)

| Instrument | Status as of 2026-11-13 | Hiring relevance | Source | Grade |
|---|---|---|---|---|
| H-1B USD 100,000 proclamation fee | Vacated by D. Mass. (2026-06-08); First Circuit denied a stay (2026-07-24); N.D. Cal. order of 2026-09-30 also covers the September 2026 extension. A D.D.C. ruling upheld the fee in December 2025 (appeal argued March 2026) | Removes a cost on new overseas H-1B hires, but appeals are pending | S54, S55 | B |
| DHS proposed USD 103,265 fee on cap-subject H-1B workers | Comment period closed 2026-09-24; no final rule as of 2026-11-13 | Separate from the proclamation fee | S55 | B |
| EU Digital Omnibus on AI | Final act signed 2026-07-08. High-risk obligations apply from 2027-12-02 (stand-alone) and 2028-08-02 (product-embedded) | Defers compliance-driven demand for governance and assurance roles (V4) | S56 | B |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Only three titles above quorum; skills not titles | updated | Research Engineer 223 (Fast AI Jobs) and 569 (AI Pulse); agentic 59.3% of AI Engineer postings [S7, S12, S64, S65] | B |
| K2 | JobsPipe 1,697 / 398 / 3,944 | stale | Same values on 2026-11-13; Pulse page refreshes while title pages do not [S1, S2, S3, S63] | B |
| K3 | 66% IC; 35% mid; 31% senior | unverifiable | No source found; platform seniority shares conflict [S7, S61, S65] | C |
| K4 | Applications per job +110%; 0.2% cold-apply hire | confirmed | Greenhouse 116 to 244; Ashby 0.2% offer rate, 291 per hire [S35, S37] | B |
| K5 | India AI-title share highest; 2x US entry share | updated | India 3.0% vs US 1.3% and 21.2% vs 10.4% hold; Singapore is higher on AI share [S8] | B |
| K6 | Evaluation in 68.2% of postings; 52.4% run offline evals | stale | LangChain 52.4%, fielded 2025-11-18 to 2025-12-02; 68.2% untraced [S57] | C |

## Absences

| Item | Where I looked | Note |
|---|---|---|
| JobsPipe FDE title page | Three searches; a direct fetch was refused because the URL was not in earlier results | Previous KB count for FDE and MLE not in the brief |
| JobsPipe Research Engineer page (same-platform recount) | One search; no JobsPipe page surfaced | The Research Engineer flag rests on Fast AI Jobs (B) and AI Pulse (C) |
| JobsPipe counts for other titles | Searches for the platform's role pages | Not surfaced |
| Skillenai counts (KB platform dated 2026-10-14) | Search for Skillenai roles and agentic AI engineer counts | No Skillenai page surfaced |
| Go Fractional beyond the CAIO page | Search; one page | Page undated |
| Fast AI Jobs reading dated 2026-10-19 | Cached search extracts only | Baselines are 2026-07-30 to 2026-08-03 |
| AI-role-specific applications per job and time to hire | Greenhouse, Ashby, Employ, SHRM and iCIMS compilations | Only all-role and technical-role figures exist |
| Source for K3 | Search on the shares and platform seniority labels | Not traced |
| Source for the 68.2% in K6 | Search on the figure and LangChain survey | Not traced |
| Hiring-freeze announcements at AI employers, 2026-10-01 to 2026-11-13 | One search | Only older items found, unverified to primary |
| Layoffs.fyi 2026 total | Search results; page not opened | Crunchbase tracker used instead |
| Stanford AI Index 2026 primary page (entry-level employment) | Not opened | Secondary summary only (S40) |
| Challenger October 2026 primary report | Not opened | Site listing and three corroborating outlets |
| Indian AI-startup hiring and funding in Q3 2026 | Naukri, foundit, Zinnov–Nasscom and UnearthIQ coverage | Crunchbase's Q3 Asia report not opened |
| Pay-pressure series longer than two JobsPipe windows | JobsPipe Pulse, the September blog; the July archive file returned an error | Only 2026-09-01 to 2026-09-18 and the 30 days to 2026-11-13 |
| KB's nine-signal list | Brief supplied six claims | Three signals untested |
| Counts for 19 titles | Fast AI Jobs, JobsPipe, AI Pulse, one fractional page | IDs: applied-ai-engineer, ai-infrastructure-engineer, research-scientist, inference-engineer, ml-platform-engineer, ai-evaluation-engineer, ai-solutions-architect, gpu-kernel-engineer, ai-security-engineer, ai-governance-lead, physical-ai-engineer, ai-enablement-engineer, ai-product-engineer, ai-risk-assurance-specialist, responsible-ai-engineer, domain-evaluation-specialist, chief-ai-officer, independent-ai-consultant, vp-head-of-ai |

## Open Questions & Risks

**Objections an expert would raise**

| Objection | Evidence for | Evidence against |
|---|---|---|
| Posting counts are not hiring | Greenhouse: 69.8% of jobs closed with a hire in 2025, so about 30% close without (S38). Aggregators duplicate postings, and consultancies post bench roles | JOLTS openings and hires rose in September and Dice/Lightcast postings rose, so direction agrees (S45, S46). No source measures AI-role hires |
| Counts are crawl artefacts, not market measures | JobsPipe's own note says counts move with board mix (S63); JobsPipe publishes 1,697 and 1,850 for AI Engineer on different pages (S2, S66) | Fast AI Jobs and AI Pulse, which crawl differently, also show large counts; shares on the Pulse page are stable (S63, S65) |
| Fast AI Jobs growth is coverage, not demand | Four titles rose +28% to +31%, which is near-uniform. Another board warns that coverage growth distorts series (not in ledger) | Dice AI/ML +91% and Naukri AI/ML +32% point the same way, but they are different series. Unresolved |
| Layoff headlines mislead (AI-washing; buyouts uncounted) | Challenger counts stated reasons only, and Microsoft's 60,000 offers are excluded (S22, S62) | AI-cited cuts fell to 1,265 in October. A Lightcast economist says labour data do not show mass replacement (S22) |
| Counts are not comparable across platforms | FDE ranges from 260 to 1,276 by definition; AI Pulse categories are undefined | Within-platform comparisons used; ranges reported |
| The entry-level squeeze is caused by AI | Anthropic 27% to 9% [COI]; Stanford AI Index software developers aged 22–25 fell nearly 20% from 2024 peak (S40, S44) | Within ICT, AI roles are 15.4% entry level against 12.5% (S8). NY Fed finds remote work explains about two-thirds of the rise (S60). Graduate unemployment fell to 5.2% (S42) |
| Funding headlines overstate hiring capacity | AI is 82.7% of US deal value year-to-date, with exits weak (S32) | Q3 deal count was near a record at about 5,012 (S32) |

**Open questions**
- When will JobsPipe refresh its title pages?
- Will Q4 funding hold after Q3's cooling?
- Will Anthropic's November IPO change hiring or pay in AI roles? [COI]
- When will the H-1B appeals resolve?
- Will any platform publish AI-role funnel data?
- Are Fast AI Jobs' increments coverage-driven?

**Risks**
- JobsPipe values expire (V1) on 2026-11-19.
- H-1B status is V0 and can change within 14 days.
- Platform indices (Naukri, foundit) carry commercial incentives.

## Discovered Concerns

1. **JobsPipe title pages appear frozen or cached.** The figures carry no date stamp, and the claim of daily updates is not met on these pages, although the Pulse page refreshes. JobsPipe publishes at least three AI Engineer counts (1,697 US jobs page; 1,850 salary page; 3,944 global) with undisclosed definitions. This affects every V1 role score that depends on it.
2. **Fast AI Jobs scope.** It covers AI startups only. Its category pages merge adjacent titles (FDE, Solutions Engineer), which inflates counts relative to exact-title definitions.
3. **AI Pulse is an aggregator with undisclosed category rules.** Its categories (AI Safety, AI Engineering Manager) are not the KB's titles, and 75% of its roles sit in one category.
4. **COI rows.** Anthropic's own report, its IPO filing and any Anthropic employer rows are marked COI. The author's developer is in scope, so treat those rows as employer self-reports.
5. **Source-vintage mismatch.** Two NY Fed URLs returned different quarters (Q2 and Q3). Cite the vintage, not the page.
6. **EU deferral.** The Omnibus pushes high-risk obligations out by 16 months, which weakens near-term demand drivers for `ai-governance-lead`, `ai-risk-assurance-specialist` and `responsible-ai-engineer`. Role scores that assumed 2026-08-02 deadlines need review.
7. **Untraced AI-washing claim.** One compilation says 80 of 119 cutting companies advertised marketing roles on 2026-11-05. I could not trace the method, so I grade it E and do not rely on it.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | JobsPipe counts differ by more than 10% | Contradicted | Identical on 2026-11-13 (S1–S3); the Pulse page refreshes, so the cause is page-level caching or definitions (S63) | `role_scores.json`: treat JobsPipe as one reading and re-measure |
| P2 | AI-cited layoffs kept rising after September | Contradicted | October 1,265, the lowest month of 2026 (S22, S23) | `market-overview.md`: soften any "AI layoff wave" wording |
| P3 | Q3 fell from Q2, stayed above Q3 2025, AI above 60% | Confirmed | Crunchbase and PitchBook (S31, S32) | `employer-landscape.md`: funding strong but cooling and concentrated |
| P4 | Entry-level share low; applications above 244 | Updated | Share low and tech-wide; no 2026 per-job series, only 291 per hire (S8, S37) | D-002: entry-level advice stays cautious but not AI-specific |
| P5 | India AI/ML growth beats overall by double digits | Confirmed | October +32% vs +14%; September +20% vs +2% (S48, S50) | D-003 (India depth): supports GCC emphasis |
| P6 | Only three titles above 50; no crossing | Updated | Research Engineer 223 (Fast AI Jobs) and 569 (AI Pulse); three more categories above 50 on AI Pulse (S12, S65) | `role_scores.json`: flag `research-engineer`; recount three category-level candidates |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | AI Engineer Jobs (global), JobsPipe, https://jobspipe.dev/jobs/ai-engineer | n/d | 2026-11-13 | B | Read | single-source; possible cache | 3,944; top employers; pay disclosure |
| S2 | AI Engineer Jobs United States, JobsPipe, https://jobspipe.dev/jobs/ai-engineer/usa.md | n/d | 2026-11-13 | B | Read | single-source | 1,697; employers |
| S3 | AI Engineer Jobs India, JobsPipe, https://jobspipe.dev/jobs/ai-engineer/india | n/d | 2026-11-13 | B | Extract | single-source | 398; employers |
| S4 | Machine Learning Engineer Jobs (global), JobsPipe, https://jobspipe.dev/jobs/machine-learning-engineer | n/d | 2026-11-13 | B | Read | single-source | 2,157; pay; employers |
| S5 | MLE US and India pages, JobsPipe, https://jobspipe.dev/jobs/machine-learning-engineer/usa.md and https://jobspipe.dev/jobs/machine-learning-engineer/india | n/d | 2026-11-13 | B | Extract | single-source | 1,084; 90 |
| S6 | AI Engineer and MLE entry-level pages, JobsPipe, https://jobspipe.dev/jobs/entry-level-ai-engineer.md and https://jobspipe.dev/jobs/entry-level-machine-learning-engineer.md | n/d | 2026-11-13 | B | Extract | single-source | 275; 240 |
| S7 | AI Engineer job description and AI Engineer Remote pages, JobsPipe, https://jobspipe.dev/job-description/ai-engineer and https://jobspipe.dev/jobs/ai-engineer/remote.md | counted 2026-09-10 | 2026-11-13 | B | Extract | single-source | skill shares; exact-title agentic postings; K1, K3 |
| S8 | AI jobs and entry-level hiring, October 2026, JobsPipe blog, https://jobspipe.dev/blog/ai-jobs-entry-level | 2026-10-11 | 2026-11-13 | B | Read | publisher is a platform | K5; entry-level shares |
| S9 | Forward Deployed Engineer Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/forward-deployed-engineer | 2026-11-11 (last updated) | 2026-11-13 | B | Read | startups only | FDE count; sample classification |
| S10 | AI Engineer Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/ai-engineer | 2026-11-11 (last updated) | 2026-11-13 | B | Read | startups only | 352 |
| S11 | Machine Learning Engineer Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/ml-engineer | 2026-11-11 (last updated) | 2026-11-13 | B | Read | startups only | 298 |
| S12 | Research Engineer Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/research-engineer | 2026-11-11 (last updated) | 2026-11-13 | B | Read | startups only | 223; quorum candidate |
| S13 | Cached extracts of the four Fast AI Jobs role pages (275; 227; 779; 171), https://www.fastaijobs.com/jobs/role/ai-engineer and sibling role pages | 2026-07-30 to about 2026-08-03 | 2026-11-13 | B | Extract | baseline dates uncertain | previous counts |
| S14 | Applied Scientist Jobs at AI Startups, Fast AI Jobs, https://www.fastaijobs.com/jobs/role/applied-scientist | n/d (postings to 2026-10-23) | 2026-11-13 | B | Extract | startups only | 23 |
| S15 | AI Startup Jobs directory, Fast AI Jobs, https://www.fastaijobs.com/jobs | 2026-11-12 | 2026-11-13 | B | Read | startups only | 41,330 total |
| S16 | FDE job market census, Plank Research, https://joinplank.com/fde-job-market | 2026-10-30 | 2026-11-13 | C | Extract | single-source | 1,276 |
| S17 | FDE Jobs List, https://fdejobslist.com/ | about 2026-11-11 | 2026-11-13 | C | Extract | single-source | 391 |
| S18 | Forward Deployed Engineer jobs, A10X, https://a10x.dev/jobs | 2026-11-05 | 2026-11-13 | C | Extract | single-source | 355 |
| S19 | FDE Jobs at Startups, The Anti Job Board, https://www.theantijobboard.com/startups/jobs/forward-deployed-engineer | 2026-10-30 | 2026-11-13 | C | Extract | single-source | 496 |
| S20 | Forward deployed engineer job market analysis, Ghanem Zadeh, https://ghanemzadeh.com/forward-deployed-engineer-job-market/ | 2026-10-12 | 2026-11-13 | C | Extract | single-source | 260 roles |
| S21 | FDE jobs: who is hiring, Valletta Software, https://vallettasoftware.com/blog/post/companies-hiring-forward-deployed-engineers | 2026-09-08 | 2026-11-13 | C | Extract | employer-board counts | Palantir, Databricks |
| S22 | AI blamed for 121,401 job cuts, HCAMag, https://www.hcamag.com/us/specialization/transformation/ai-blamed-for-121401-job-cuts-but-the-labor-data-isnt-buying-it/594129 | 2026-10-19, updated 2026-11-05 | 2026-11-13 | B | Read | corroborated | Challenger series |
| S23 | October job cuts at 3-year low, TheStreet Pro, https://pro.thestreet.com/market-commentary/october-job-cuts-at-3-year-low-as-focus-turns-to-economic-conditions | 2026-11-05 | 2026-11-13 | B | Extract | corroborated | October figures; hiring plans |
| S24 | Challenger Report listing, Challenger, Gray & Christmas, https://www.challengergray.com/blog/tag/job-cuts/ | 2026-11-05 | 2026-11-13 | A | Extract | headline only | report existence |
| S25 | US companies announce fewest October job cuts in three years, Bloomberg via CPA Practice Advisor, https://www.cpapracticeadvisor.com/?p=193395 | 2026-11-06 | 2026-11-13 | B | Extract | corroborated | October; hiring plans |
| S26 | Microsoft offers 60,000 employees voluntary buyouts, AP via WDBJ, https://www.wdbj7.com/2026/10/26/microsoft-offers-60000-employees-voluntary-buyouts-ai-spending-accelerates/ ; also Fox 6, https://www.fox6now.com/news/microsoft-offers-voluntary-buyouts-60000-employees-tech-giant-reshapes-its-workforce | 2026-10-26 | 2026-11-13 | B | Extract | corroborated | Microsoft event |
| S27 | The Crunchbase Tech Layoffs Tracker, Crunchbase News, https://news.crunchbase.com/startups/tech-layoffs/ | 2026-11-04 | 2026-11-13 | B | Read | method stated | Canva, Amazon, weekly count |
| S28 | Tech Layoffs Tracker 2026, TrueUp, https://www.trueup.io/layoffs | 2026-11-05 | 2026-11-13 | C | Extract | aggregator | small-company cuts |
| S29 | Qualcomm layoffs, American Bazaar, https://americanbazaaronline.com/2026/11/11/qualcomm-layoffs-us-chipmaker-offers-extra-salary-to-employees-who-quit-within-3-days-492089 | 2026-11-11 | 2026-11-13 | C | Extract | single-source | Qualcomm India |
| S30 | Apple, Canva, Microsoft, Zomato lay off workers, IBTimes India, https://www.ibtimes.co.in/apple-fires-hardware-programme-managers-canva-microsoft-zomato-lay-off-workers-ai-takes-over-908302 | 2026-11-12 | 2026-11-13 | C | Extract | single-source | Zomato, Apple |
| S31 | Q3 2026 global startup funding, Crunchbase News, https://news.crunchbase.com/venture/q3-2026-global-startup-funding-ai-billion-dollar-rounds-exits-data/ | 2026-10-05 | 2026-11-13 | B | Read | corroborated | funding |
| S32 | US venture deal value reaches record USD 515.8B (PitchBook-NVCA Q3 2026), SiliconANGLE, https://siliconangle.com/?p=849755 | 2026-10-08 | 2026-11-13 | B | Read | corroborated | PitchBook-NVCA Q3 |
| S33 | PitchBook-NVCA Venture Monitor, NVCA, https://nvca.org/pitchbook-nvca-venture-monitor/ | n/d | 2026-11-13 | B | Extract | none | AI share, Q3 value |
| S34 | Anthropic Seeks Record USD 88.5B Tied To Public Market Debut, Crunchbase News, https://news.crunchbase.com/ai/anthropic-record-ipo-ant-public-market-debut-spcx/ | 2026-11-10 | 2026-11-13 | B | Read | COI | Anthropic S-1 |
| S35 | The Hire Standard report preview, Greenhouse, https://www.greenhouse.com/recruiting-benchmarks | 2026-03 | 2026-11-13 | B | Extract | vendor benchmark | 116 to 244 |
| S36 | How many applicants per job, Noon.ai, https://www.noon.ai/blog/articles/353-how-many-applicants-per-job | n/d | 2026-11-13 | C | Extract | compilation | Greenhouse series |
| S37 | Recruitment statistics 2026, Pin, https://www.pin.com/blog/recruitment-statistics/ | n/d | 2026-11-13 | C | Extract | secondary | Ashby 291; 0.2%; 7.3% |
| S38 | Time-to-hire and funnel benchmarks, HeroHunt, https://www.herohunt.ai/blog/average-time-to-hire-2026-benchmarks-by-role-and-fixes/ and https://www.herohunt.ai/blog/recruiting-funnel-conversion-rates-2026-stage-benchmarks/ | n/d | 2026-11-13 | C | Extract | compilation | time to hire; iCIMS |
| S39 | Will AI replace software engineers, Extern, https://www.extern.com/post/will-ai-replace-software-engineers-guide | 2026-11 | 2026-11-13 | C | Extract | secondary for Indeed | 4.5%; 69.3% |
| S40 | AI is automating coding (software developer jobs), CNBC, https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html | 2026-10-11 | 2026-11-13 | B | Extract | secondary for Indeed and Stanford | postings rise; Stanford AI Index |
| S41 | NY Fed college labor market web feature (Q2 2026 highlights), https://www.newyorkfed.org/research/college-labor-market?stream=business | n/d | 2026-11-13 | A | Read | Q2 vintage | 5.6%; definitions |
| S42 | NY Fed college labor market web feature, search extract of the Q3 2026 update, https://www.newyorkfed.org/research/college-labor-market?stream=business | 2026-11-02 | 2026-11-13 | B | Extract | different vintage from S41 | 5.2%; 42.5% |
| S43 | Software Engineer Jobs in the AI era, MASEconomics, https://maseconomics.com/software-engineer-jobs-ai-era/ | 2026-11-10 | 2026-11-13 | C | Blocked | snippet only | Q3 date; Indeed index |
| S44 | How employment is changing at Anthropic, Anthropic Institute, https://www.anthropic.com/research/employment-at-anthropic | 2026-10-16 | 2026-11-13 | C | Extract | COI; single employer | 27% to 9% |
| S45 | October 2026 Jobs Report, Dice, https://www.dice.com/hiring/?p=999887277 | 2026-11 (data as of 2026-11-03) | 2026-11-13 | B | Extract | Lightcast data | tech and AI/ML postings |
| S46 | US job postings jumped sharply in September, AP via WRAL, https://www.wral.com/news/ap/4f6f0-us-job-postings-jumped-sharply-in-september-a-sign-hiring-could-pick-up/ | 2026-11-03 | 2026-11-13 | B | Read | reports BLS JOLTS | openings; layoffs |
| S47 | The Employment Situation, October 2026, BLS, https://www.bls.gov/news.release/empsit.nr0.htm | 2026-11-06 | 2026-11-13 | B | Extract | primary seen as extract; corroborated by wire reports | payrolls; unemployment |
| S48 | India's white-collar hiring jumps 14% in October, Staffing Industry Analysts, https://www.staffingindustry.com/news/global-daily-news/indias-white-collar-hiring-jumps-14-in-october-auto-sector-leads | 2026-11-03 | 2026-11-13 | B | Extract | reports Naukri | AI/ML, GCC |
| S49 | India's white-collar hiring rises 14% in October, SightsIn Plus, https://www.sightsinplus.com/news/survey-report/indias-white-collar-hiring-rises-14-in-october-manufacturing-auto-lead/ ; Lapaas Voice, https://lapaasvoice.com/indias-white-collar-hiring-rises-14-in-october-as-manufacturing-and-ai-jobs-drive-growth/ | 2026-11 | 2026-11-13 | C | Extract | secondary | index; base effect |
| S50 | AI/ML hiring jumps 20% in September, Angel One, https://www.angelone.in/news/stocks/india-s-white-collar-hiring-rise-2-in-september-as-ai-ml-hiring-jumps-20 ; Success CDS, https://www.successcds.net/?p=177078 | 2026-10-02 and 2026-10-06 | 2026-11-13 | C | Extract | secondary | September; freshers |
| S51 | GCC count nears 2,117, YourStory, https://yourstory.com/enterprise-story/2026/05/gccs-number-touch-2117-in-india-revenue-just-short-of-100-billion ; Business Today, https://www.businesstoday.in/amp/technology/news/story/the-big-boom-how-indias-gcc-story-hits-2030-target-4-years-early-530265-2026-05-07 | 2026-05 | 2026-11-13 | B | Extract | reports Zinnov–Nasscom | GCC base |
| S52 | India's GCC hiring boom, Business Today, https://www.businesstoday.in/jobs/story/at-5-1-lakh-jobs-indias-global-capability-centre-hiring-boom-scales-new-peak-540328-2026-07-01 | 2026-07-01 | 2026-11-13 | B | Extract | reports foundit | 510,452; 64%; 30% |
| S53 | India crosses 100 greenfield GCCs, Communications Today, https://www.communicationstoday.co.in/?p=423357 | 2026-09 | 2026-11-13 | C | Extract | reports UnearthIQ | 111 greenfield GCCs |
| S54 | What is happening to the USD 100,000 H-1B fee (November 2026), Ahluwalia Law, https://www.ahluwalialaw.com/?p=34775 | 2026-11 | 2026-11-13 | B | Extract | law firm | H-1B status |
| S55 | Federal court order blocking implementation of the USD 100,000 H-1B fee, Ogletree Deakins, https://ogletree.com/insights-resources/blog-posts/federal-court-issues-new-order-blocking-agency-implementation-of-100000-h-1b-fee | 2026-10 | 2026-11-13 | B | Extract | corroborates S54 | 2026-09-30 order; DHS proposal |
| S56 | Digital Omnibus on AI approved, dig.watch, https://dig.watch/?p=262657 | 2026-07 | 2026-11-13 | B | Extract | secondary to the Official Journal | signing date; deadlines |
| S57 | State of Agent Engineering, LangChain, https://langchain.com/state-of-agent-engineering | 2025-12 (fielded 2025-11-18 to 2025-12-02) | 2026-11-13 | C | Extract | vendor survey; COI | K6 |
| S58 | Fractional Chief AI Officer benchmarks, Go Fractional, https://www.gofractional.com/insights/rates/chief-ai-officer | n/d | 2026-11-13 | B | Extract | platform index; undated | 10 posts in 90 days |
| S59 | Barclays to cut 5K jobs because of AI, iHeart, https://www.iheart.com/content/2026-10-22-barclays-to-cut-5k-jobs-because-of-ai/ | 2026-10-22 | 2026-11-13 | C | Extract | single-source | Barclays |
| S60 | NPR via KPBS, remote work and graduate unemployment (title shortened), https://www.kpbs.org/news/economy/2026/06/01/remote-work-not-ai-has-sidelined-recent-college-graduates-research-finds | 2026-06-01 | 2026-11-13 | B | Extract | reports NY Fed research | objection evidence |
| S61 | AI and ML engineer job market 2026, SimpleApply, https://simpleapply.ai/blog/ai-ml-engineer-job-market-2026 | 2026-10 | 2026-11-13 | C | Extract | single-source | seniority split |
| S62 | Challenger October summary, Outsource Accelerator, https://news.outsourceaccelerator.com/?p=126943 | 2026-11-05 | 2026-11-13 | C | Extract | corroborates S22 | Microsoft exclusion |
| S63 | Labour Market Pulse (snapshot 2026-11-13), JobsPipe, https://jobspipe.dev/pulse.md | 2026-11-13 | 2026-11-13 | B | Read | rolling 30-day window; counts-versus-shares caveat | developer AI share and premium; method note; refresh evidence |
| S64 | The highest-paying AI jobs in September 2026, JobsPipe blog, https://jobspipe.dev/blog/highest-paying-ai-jobs-september-2026.md | 2026-09-18 | 2026-11-13 | B | Read | window 2026-09-01 to 2026-09-18 | AI-mention shares; premium; agentic share |
| S65 | AI and ML Engineer Salary Benchmarks 2026 (market overview), AI Pulse, https://theaimarketpulse-com.pages.dev/salaries/ | last refreshed 2026-11-12 | 2026-11-13 | C | Read | aggregator; category rules undisclosed | category counts; seniority mix |
| S66 | AI Engineer Salary page, JobsPipe, https://jobspipe.dev/salary/ai-engineer | n/d | 2026-11-13 | B | Extract | undated | 1,850 postings; median USD 181k |

## Data Appendix

```jsonl
{"type":"measure","grade":"B","src":["S1"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"global_postings","unit":"postings","value":3944,"method":"JobsPipe page /jobs/ai-engineer as read; same value as the KB reading with corpus 2026-10-19","region":"global","note":"No change; page may be a cached snapshot so the true count date is uncertain"}
{"type":"measure","grade":"B","src":["S2"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"us_postings","unit":"postings","value":1697,"method":"JobsPipe page /jobs/ai-engineer/usa","region":"US","note":"No change since the KB reading; a JobsPipe salary page shows 1,850 AI Engineer postings (undated)"}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-engineer","measure":"india_postings","unit":"postings","value":398,"method":"JobsPipe page /jobs/ai-engineer/india, search snapshot","region":"India","note":"No change since the KB reading"}
{"type":"measure","grade":"B","src":["S4"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-engineer","measure":"global_postings","unit":"postings","value":2157,"method":"JobsPipe page /jobs/machine-learning-engineer","region":"global","note":"Baseline; no KB figure in the brief"}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-engineer","measure":"us_postings","unit":"postings","value":1084,"method":"JobsPipe MLE US page","region":"US","note":"Baseline"}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-engineer","measure":"india_postings","unit":"postings","value":90,"method":"JobsPipe MLE India page","region":"India","note":"Baseline"}
{"type":"measure","grade":"B","src":["S10","S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ai-engineer","measure":"global_postings","unit":"postings","value":352,"method":"Fast AI Jobs role page; AI-startup boards only; 188 companies","region":"global","note":"Baseline 275 on 2026-07-30, +28% (M); uniform growth across four titles may reflect coverage"}
{"type":"measure","grade":"B","src":["S11","S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:ml-engineer","measure":"global_postings","unit":"postings","value":298,"method":"Fast AI Jobs role page; AI-startup boards only; 171 companies","region":"global","note":"Baseline 227 about 2026-07-30, +31% (M)"}
{"type":"measure","grade":"B","src":["S9","S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":1007,"method":"Fast AI Jobs role page; 353 companies","region":"global","note":"Baseline 779 about 2026-07-31, +29% (M); category includes deployment strategist, GTM and field-engineer titles; 23 of the first 50 rows are IC FDE titles (M)"}
{"type":"measure","grade":"B","src":["S12","S13"],"as_of":"2026-11-11","ttl":"V1","subject":"role:research-engineer","measure":"global_postings","unit":"postings","value":223,"method":"Fast AI Jobs role page; 103 companies","region":"global","note":"Candidate quorum crossing; baseline 171 with postings to 2026-07-31, +30% (M); needs recount under the KB method"}
{"type":"measure","grade":"C","src":["S65"],"as_of":"2026-11-12","ttl":"V1","subject":"role:research-engineer","measure":"global_postings","unit":"postings","value":569,"method":"AI Pulse category count; aggregator outside the KB platform set","region":"global","note":"Corroborates the Fast AI Jobs reading; category definition undisclosed"}
{"type":"measure","grade":"C","src":["S65"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ai-product-manager","measure":"global_postings","unit":"postings","value":570,"method":"AI Pulse category AI Product Manager","region":"global","note":"Category-level candidate; needs recount under the KB method"}
{"type":"measure","grade":"C","src":["S65"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ai-engineering-manager","measure":"global_postings","unit":"postings","value":68,"method":"AI Pulse category AI Engineering Manager","region":"global","note":"Category-level candidate; needs recount under the KB method"}
{"type":"measure","grade":"C","src":["S65"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ai-safety-researcher","measure":"global_postings","unit":"postings","value":89,"method":"AI Pulse category AI Safety","region":"global","note":"Category may include trust-and-safety roles; candidate only"}
{"type":"measure","grade":"B","src":["S14"],"as_of":"2026-10-23","ttl":"V1","subject":"role:applied-scientist","measure":"global_postings","unit":"postings","value":23,"method":"Fast AI Jobs role page extract; 15 companies","region":"global","note":"Below quorum; extract undated, latest listed posting 2026-10-23"}
{"type":"measure","grade":"C","src":["S16"],"as_of":"2026-10-30","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":1276,"method":"Plank census of ATS boards and aggregators; 547 companies","region":"global","note":"Single-source vendor census"}
{"type":"measure","grade":"C","src":["S19"],"as_of":"2026-10-30","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":496,"method":"Anti Job Board; startups; 337 companies","region":"global","note":"Single-source"}
{"type":"measure","grade":"C","src":["S17"],"as_of":"2026-11-11","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":391,"method":"Public Lever, Ashby and Greenhouse feeds","region":"global","note":"Single-source; date inferred from listing dates"}
{"type":"measure","grade":"C","src":["S18"],"as_of":"2026-11-05","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":355,"method":"A10X verified-live board; 96 companies; includes Applied AI roles","region":"global","note":"Single-source"}
{"type":"measure","grade":"C","src":["S20"],"as_of":"2026-10-12","ttl":"V1","subject":"role:forward-deployed-engineer","measure":"global_postings","unit":"postings","value":260,"method":"Distinct roles with forward deployed in the title; 382 postings; 44 companies","region":"global","note":"Strict title definition"}
{"type":"measure","grade":"B","src":["S58"],"as_of":"2026-11-13","ttl":"V1","subject":"role:fractional-ai-leader","measure":"global_postings","unit":"posts in rolling 90 days","value":10,"method":"Go Fractional Chief AI Officer benchmark page","region":"global","note":"Page undated, retrieval date used; 4 open jobs; average rate USD 190 per hour; below quorum"}
{"type":"measure","grade":"B","src":["S22","S23","S25"],"as_of":"2026-10-31","ttl":"V1","subject":"market:us-announced-job-cuts","measure":"monthly_total","unit":"announced job cuts","value":43994,"method":"Challenger, Gray and Christmas October 2026 report, published 2026-11-05","region":"US","note":"Down 71% on October 2025 (153,074); year-to-date 617,189, down 44%"}
{"type":"measure","grade":"B","src":["S22","S23"],"as_of":"2026-10-31","ttl":"V1","subject":"market:us-announced-job-cuts-ai-cited","measure":"monthly_total","unit":"announced job cuts","value":1265,"method":"Challenger; employer-stated reasons","region":"US","note":"Lowest month of 2026; May 2026 peak 38,579"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-10-31","ttl":"V1","subject":"market:us-announced-job-cuts-ai-cited","measure":"year_to_date","unit":"announced job cuts","value":121401,"method":"Challenger; employer-stated reasons","region":"US","note":"About 20% of the 617,189 year-to-date total"}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-09-30","ttl":"V3","subject":"market:global-venture-funding","measure":"quarterly_total","unit":"USD billion","value":159,"method":"Crunchbase, data as of 2026-10-02","region":"global","note":"Q3 2026; Q2 212; Q3 2025 104; Q1 to Q3 2026 679; Q1 about 308 by subtraction (M)"}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-09-30","ttl":"V3","subject":"market:global-venture-funding-ai-share","measure":"quarterly_share","unit":"share of dollars","value":0.64,"method":"Crunchbase; AI-driven startups USD 102bn","region":"global","note":"Down from the two previous quarters"}
{"type":"measure","grade":"B","src":["S32","S33"],"as_of":"2026-09-30","ttl":"V3","subject":"market:us-venture-deal-value","measure":"quarterly_total","unit":"USD billion","value":98.4,"method":"PitchBook-NVCA Venture Monitor Q3 2026","region":"US","note":"About 40% below Q2; about 5,012 deals; AI 65.9% of Q3 and 82.7% of year-to-date"}
{"type":"measure","grade":"B","src":["S35","S36"],"as_of":"2025-12-31","ttl":"V3","subject":"market:applications-per-job","measure":"annual_average","unit":"applications per job","value":244,"method":"Greenhouse Hire Standard; 6,000+ companies; 640 million+ applications","region":"global","note":"116 in 2022, +111%; Greenhouse customer series gives 95 for 2025"}
{"type":"measure","grade":"C","src":["S37"],"as_of":"2026-03-31","ttl":"V3","subject":"market:applications-per-hire","measure":"quarterly_average","unit":"applications per hire","value":291,"method":"Ashby Recruiter Productivity via secondary report; 109 million applications","region":"global","note":"About 100 in early 2021; Ashby customers skew to tech and startups"}
{"type":"measure","grade":"C","src":["S37"],"as_of":"2026-03-31","ttl":"V3","subject":"market:inbound-applicant-offer-rate","measure":"offer_rate","unit":"percent","value":0.2,"method":"Ashby Talent Trends via secondary report","region":"global","note":"Referred candidates 7.3%; offer rate, not hire rate"}
{"type":"measure","grade":"B","src":["S42","S43"],"as_of":"2026-09-30","ttl":"V3","subject":"market:graduate-unemployment-rate","measure":"quarterly_rate","unit":"percent","value":5.2,"method":"NY Fed, graduates aged 22 to 27; Q3 2026 update","region":"US","note":"5.6% in Q2 2026; underemployment 42.5%; Q3 vintage seen as extract"}
{"type":"measure","grade":"B","src":["S39","S43"],"as_of":"2026-03-31","ttl":"V3","subject":"market:software-postings-entry-level-share","measure":"quarterly_share","unit":"percent","value":4.5,"method":"Indeed Hiring Lab via secondary reports","region":"US","note":"Senior share 69.3%; lowest of any sector"}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-10-11","ttl":"V3","subject":"market:ai-title-entry-level-share","measure":"share_of_ai_titled_postings","unit":"percent","value":10.4,"method":"JobsPipe active postings with AI in the title; seniority stated or inferred","region":"US","note":"All US postings 35.8%; ICT-only comparison 15.4% vs 12.5%"}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-10-11","ttl":"V3","subject":"market:ai-title-entry-level-share","measure":"share_of_ai_titled_postings","unit":"percent","value":21.2,"method":"JobsPipe active postings with AI in the title; seniority stated or inferred","region":"India","note":"All India postings 31.9%; AI-title share of postings 3.0%; Singapore 3.7%"}
{"type":"measure","grade":"C","src":["S65"],"as_of":"2026-11-12","ttl":"V1","subject":"market:ai-roles-entry-level-share","measure":"share_of_open_ai_roles","unit":"percent","value":1.2,"method":"AI Pulse: 137 entry-level of 11,652 open AI roles (M)","region":"global","note":"Mid-level 48.3%, senior 36.3%, leadership 14.2% (M); classification undisclosed"}
{"type":"measure","grade":"B","src":["S63"],"as_of":"2026-11-13","ttl":"V1","subject":"market:ai-mention-share-software-developers","measure":"share_of_postings","unit":"percent","value":39.1,"method":"JobsPipe Labour Market Pulse; rolling 30 days; ISCO 2512","region":"global","note":"39.5% on 2026-09-01 to 2026-09-18 (S64); denominators differ; advertised premium +25% vs +28%"}
{"type":"measure","grade":"B","src":["S45"],"as_of":"2026-10-31","ttl":"V1","subject":"market:ai-ml-tech-postings-yoy","measure":"annual_change","unit":"percent","value":91,"method":"Dice with Lightcast data as of 2026-11-03","region":"US","note":"Tech postings overall +20% year on year, +4% on September"}
{"type":"measure","grade":"B","src":["S46"],"as_of":"2026-09-30","ttl":"V1","subject":"market:jolts-job-openings","measure":"monthly_level","unit":"million openings","value":7.5,"method":"BLS JOLTS reported by AP","region":"US","note":"7.19 million in August; layoffs 1.64 million"}
{"type":"measure","grade":"B","src":["S47"],"as_of":"2026-10-31","ttl":"V1","subject":"market:us-nonfarm-payroll-change","measure":"monthly_change","unit":"jobs","value":165000,"method":"BLS Employment Situation October 2026","region":"US","note":"Unemployment rate 4.1%; August and September revised up by 84,000"}
{"type":"measure","grade":"B","src":["S48"],"as_of":"2026-10-31","ttl":"V1","subject":"market:naukri-ai-ml-hiring-yoy","measure":"annual_change","unit":"percent","value":32,"method":"Naukri JobSpeak October 2026 via Staffing Industry Analysts","region":"India","note":"September +20%; overall index +14% with a soft October 2025 base"}
{"type":"measure","grade":"B","src":["S48"],"as_of":"2026-10-31","ttl":"V1","subject":"market:naukri-gcc-hiring-yoy","measure":"annual_change","unit":"percent","value":18,"method":"Naukri JobSpeak October 2026 via Staffing Industry Analysts","region":"India","note":"September +4%"}
{"type":"measure","grade":"B","src":["S51"],"as_of":"2026-03-31","ttl":"V4","subject":"market:india-gcc-count","measure":"fy2026_count","unit":"centres","value":2117,"method":"Zinnov-Nasscom GCC Landscape FY26 via press reports","region":"India","note":"3,728 units; 2.36 million staff; USD 98.4bn revenue"}
{"type":"measure","grade":"B","src":["S52"],"as_of":"2026-07-01","ttl":"V3","subject":"market:india-gcc-hires-projected-2026","measure":"annual_projection","unit":"hires","value":510452,"method":"foundit Insights Tracker via Business Today","region":"India","note":"64% of new roles need AI, data or automation skills; 0-3 years 30% of hiring"}
{"type":"company","grade":"B","src":["S26"],"as_of":"2026-10-26","ttl":"V6","name":"Microsoft","employer_type":"big-tech","hq":"Redmond, US","regions":["US","UK","CA","IN"],"note":"Voluntary exit offer to about 60,000 eligible staff on 2026-10-26; not a layoff; hq from memory"}
{"type":"company","grade":"C","src":["S44","S34"],"as_of":"2026-11-10","ttl":"V6","name":"Anthropic","employer_type":"frontier-lab","hq":"San Francisco, US","regions":["US","UK"],"note":"COI. Junior share of technical hires 27% to 9% (report of 2026-10-16); updated S-1 of 2026-11-10 seeking up to USD 88.5bn"}
{"type":"company","grade":"B","src":["S27"],"as_of":"2026-11-04","ttl":"V6","name":"Canva","employer_type":"other","hq":"Sydney, AU","regions":["AU","US"],"note":"Announced a 22% workforce cut (1,271 people) on 2026-11-04"}
{"type":"company","grade":"C","src":["S29"],"as_of":"2026-11-11","ttl":"V6","name":"Qualcomm","employer_type":"big-tech","hq":"San Diego, US","regions":["US","IN"],"note":"India cuts in Bengaluru and Hyderabad reported 2026-11-11, about 1,000 roles at risk; hq from memory"}
{"type":"company","grade":"C","src":["S30"],"as_of":"2026-11-12","ttl":"V6","name":"Zomato","employer_type":"other","hq":"Gurugram, IN","regions":["IN"],"note":"About 250 roles and a Hyderabad support centre closure reported 2026-11-12; hq from memory"}
{"type":"company","grade":"C","src":["S59"],"as_of":"2026-10-22","ttl":"V6","name":"Barclays","employer_type":"enterprise","hq":"London, UK","regions":["UK","US","IN"],"note":"About 5,000 job cuts tied to AI cost savings; hq from memory"}
{"type":"company","grade":"C","src":["S21"],"as_of":"2026-09-08","ttl":"V1","name":"Databricks","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US","UK","IN","SG"],"genai_open":94,"note":"94 of 870 open roles FDE-labelled on 2026-09-08; USD 5bn raise in Q3 2026 (S31); hq from memory"}
{"type":"company","grade":"C","src":["S21"],"as_of":"2026-09-08","ttl":"V1","name":"Palantir","employer_type":"enterprise","hq":"Denver, US","regions":["US","UK"],"genai_open":77,"note":"77 of 310 open roles FDE-labelled on 2026-09-08; hq from memory"}
{"type":"company","grade":"B","src":["S1","S3"],"as_of":"2026-11-13","ttl":"V1","name":"PwC","employer_type":"other","hq":"London, UK","regions":["US","IN","global"],"genai_open":67,"note":"Top AI Engineer poster on JobsPipe: 67 global, 19 India; professional-services firm; hq from memory"}
{"type":"company","grade":"B","src":["S1","S2"],"as_of":"2026-11-13","ttl":"V1","name":"Capital One","employer_type":"enterprise","hq":"McLean, US","regions":["US"],"genai_open":34,"note":"34 AI Engineer postings globally, 33 US; hq from memory"}
{"type":"company","grade":"B","src":["S1","S2","S3"],"as_of":"2026-11-13","ttl":"V1","name":"Tata Consultancy Services","employer_type":"it-services","hq":"Mumbai, IN","regions":["US","IN"],"genai_open":31,"note":"31 AI Engineer postings globally, 22 US, 5 India; hq from memory"}
{"type":"company","grade":"B","src":["S1","S2","S3"],"as_of":"2026-11-13","ttl":"V1","name":"Infosys","employer_type":"it-services","hq":"Bengaluru, IN","regions":["US","IN"],"genai_open":20,"note":"20 AI Engineer postings globally, 12 US, 6 India; hq from memory"}
{"type":"company","grade":"B","src":["S4"],"as_of":"2026-11-13","ttl":"V1","name":"Waymo","employer_type":"other","hq":"Mountain View, US","regions":["US"],"genai_open":53,"note":"53 MLE postings on JobsPipe; autonomy firm; hq from memory"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"JobsPipe Forward Deployed Engineer title page count","searched":"Three web searches for the JobsPipe FDE page; direct fetch refused because the URL was not in earlier results","note":"KB previous FDE and MLE counts are not in the brief"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"JobsPipe Research Engineer page count (same-platform recount)","searched":"One web search for the JobsPipe Research Engineer page","note":"No JobsPipe page surfaced; the Research Engineer flag rests on Fast AI Jobs and AI Pulse"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"JobsPipe counts for titles other than AI Engineer and MLE","searched":"Searches for platform role pages","note":"19 titles unmeasured on any platform; three more have category counts on AI Pulse only (C)"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Skillenai counts (KB platform dated 2026-10-14)","searched":"Search for Skillenai AI roles and agentic AI engineer counts","note":"No Skillenai page surfaced"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Go Fractional counts beyond the Chief AI Officer page","searched":"Search for Go Fractional AI roles","note":"CAIO page is undated"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Fast AI Jobs reading dated 2026-10-19","searched":"Cached search extracts of role pages","note":"Baselines used are 2026-07-30 to 2026-08-03"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"AI-role-specific applications per job and time to hire","searched":"Greenhouse, Ashby, Employ, SHRM and iCIMS compilations","note":"Only all-role and technical-role figures exist"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Source for K3 (66% IC, 35% mid-level, 31% senior)","searched":"Search on the shares and platform seniority labels","note":"Not traced; platform seniority shares conflict"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Source for the 68.2% of 198 companies in K6","searched":"Search on the figure and the LangChain survey","note":"Not traced"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Hiring-freeze announcements at AI employers dated 2026-10-01 to 2026-11-13","searched":"One search on hiring freezes and headcount plans","note":"Only older items found: Meta AI-division pause reported 2025-08-21; Salesforce engineer-hiring pause since 2025; SAP freeze with unconfirmed year"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Indian AI-startup hiring and funding in Q3 2026","searched":"Naukri, foundit, Zinnov-Nasscom and UnearthIQ coverage","note":"Crunchbase Q3 2026 Asia report not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Pay-pressure series longer than two JobsPipe windows","searched":"JobsPipe Pulse and the September blog; the July archive file returned an error","note":"Only 2026-09-01 to 2026-09-18 and the 30 days to 2026-11-13; windows and denominators differ"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Challenger October 2026 primary report and Stanford AI Index 2026 primary page","searched":"Opened HCAMag; saw Challenger's site listing and secondary summaries","note":"Primary documents not opened"}
```
