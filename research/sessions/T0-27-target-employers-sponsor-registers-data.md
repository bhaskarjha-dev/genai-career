---
id: "T0-27"
title: "Target Employers, Sponsor Registers and Hiring Data Corpora"
date: "2026-11-13"
status: complete-with-gaps
topic: "target-employers-sponsor-registers-data"
tags: ["employers", "sponsor-registers", "ats", "hiring-data", "india", "visa", "datasets", "terms-of-service"]
informs_decisions: ["D-003", "D-005"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and fetch. Anthropic, the developer, is an employer in scope; its self-published rows are tagged COI."
evidence_window: "2024-12-05 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 9
---

# T0-27: Target Employers, Sponsor Registers and Hiring Data Corpora

Evidence is cited as [S#] and keyed to the ledger near the end. Grades: A primary source opened; B established secondary source or sizeable dataset; C attributed third-party or vendor claim; D recalled or judgement; M my calculation (weakest input); P practice-curated. The research date is 2026-11-13 by the session clock. The brief's anchor of 2026-11-11 closes the evidence window for hiring and sponsorship data, so only live pages read on the retrieval date fall after it. Anthropic is an employer in scope. Its self-published figures are used only for counts and dates it publishes itself, and they are tagged COI.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | Big Tech and a handful of labs and data platforms hold most open AI roles, but aggregator counts for the same employer disagree widely. | 75% | D |
| P2 | Most AI-native startups hire through Greenhouse, Lever or Ashby, each with a public JSON endpoint. | 80% | D |
| P3 | The US USD 100,000 H-1B payment is being collected on new petitions. | 55% | D |
| P4 | The UK and Dutch sponsor registers are free downloads or lookups, and the USCIS H-1B Employer Data Hub is online and searchable. | 75% | D |
| P5 | Crunchbase has withdrawn free API access, and its terms bar scraping. | 60% | D |
| P6 | In India, GCCs and IT services supply most GenAI hiring volume. Frontier labs hire few people locally. | 70% | D |

## Research Question

**Decision.** Which employers should a GenAI job seeker put on a target list, in which locations, through which applicant-tracking systems (ATS), with what sponsorship and remote evidence? Which public datasets let them build and maintain that list lawfully?

**Sub-questions.** These follow the brief: (1) a census of at least 40 employers; (2) India; (3) sponsor registers and AI/ML LCA filers; (4) curated lists; (5) hiring signals and layoffs; (6) datasets and their terms; (7) a target-list method. I also tested K1–K9.

**Readings chosen.**
- "Open GenAI roles" means roles on an employer's board whose title or department indicates AI, ML, LLM or applied AI. I could open only one board directly (Anthropic), so every other count is a third-party reading of a board. Each count carries its filter and date.
- "Last complete fiscal year" means US FY2025 (2024-10-01 to 2025-09-30).
- Remote and sponsorship fields are null where I found nothing.

**Method.**
- About 45 searches and 8 page opens. The USCIS page was bot-blocked. The sandbox could not resolve dol.gov, so I did not process raw LCA files.
- The census has 46 company records. One was opened on the employer's own board (A). The others rest on aggregator panels or documents.
- FALSIFY searches: (a) whether the USD 100,000 payment is being collected (it is not, S16–S19); (b) counter-evidence to "nearly 70% of GCCs at pilot stage" (found different framings, S61); (c) whether Crunchbase still offers a free API (it does not, S86–S87); (d) enforcement against Apollo, ZoomInfo, Lusha and RocketReach (none found beyond S91 and S94).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Live counts for one employer disagree by source and date. Anthropic's own Greenhouse board listed 682 jobs on 2026-11-13 (all departments, 14 pages). Third-party readings were 400 (2026-07), 622 (2026-09-25), 603 (2026-10-08) and 675 (2026-11-01). Applied AI held 28 of the roles on the page read, so "all roles" overstates GenAI roles. | [S27] [S30]–[S33] | A |
| KF2 | US AI-role volume sits with Big Tech and large enterprises. Chopping Block (page dated 2026-11-11) shows open AI jobs in the US: Google 451–632, Amazon 388–477, Apple 287–310, NVIDIA 178–220, Capital One 173–187, Booz Allen 186–187, Meta 144–165, JPMorgan 81, GM 57. Two panels on one page disagree. The site's AI-job total fell from 37,286 of 109,767 (about 2026-10-20) to 7,555 of 70,864 (2026-11-11), a definition or coverage change. | [S35] [S36] | B |
| KF3 | Among AI labs and AI-native firms, total open roles (all functions) on 2026-11-01 were Databricks 904, OpenAI 810, Anthropic 675. The index covers 155 companies with at least 16,160 roles. TrueUp (2026-07) lists OpenAI 714, Anthropic 400, Harvey 333, xAI 210, Prolific 174, Mistral 172, ElevenLabs 171, Sierra 158, Glean 131, Cohere 130, Cursor 113. | [S32] [S33] | B |
| KF4 | Greenhouse, Lever and Ashby publish documented, unauthenticated JSON job-board endpoints, and Workable has a widget feed. ATS attribution for AI firms conflicts between sources: Cursor appears under Ashby in two sources and Lever in one, and Cohere and Perplexity appear under Ashby in one source and Lever in another. Vendor mix is moving. Among Huntr users' applications through ATS pages, Ashby rose from 14.1% to 19.1%, Greenhouse fell from 27.4% to 21.8% and Lever from 10.6% to 5.3% (Q3 2025 to Q3 2026). A script must detect the vendor at run time. | [S42]–[S49] [S50] | B |
| KF5 | Official sponsor sources: DOL LCA files (FY2025 complete; FY2026 to 2026-06-30 published), the UK register (page updated 2026-11-10, about 10.4 MB CSV), the NL IND register, the Canada positive-LMIA list (quarterly), the Denmark SIRI list (982 firms reported) and an Australian FOI list (January 2024, point-in-time). I found no public Irish list. The USCIS Employer Data Hub had a reported outage in March 2026 and bot-blocked my fetch. | [S1]–[S14] | A |
| KF6 | AI/ML LCA counts depend on the title filter. Exact title "Machine Learning Engineer" gives 1,053–1,071 FY2025 LCAs across two aggregators. A vendor AI/ML keyword set gives thousands per employer over several years (Amazon entities 4,252 + 437 + 430; Apple 2,115; Microsoft 1,989; Meta 522). All-title FY2025 certified LCAs: Amazon 21,585, Google 8,161, Microsoft 8,065, Apple 6,723, Meta 5,824 (Amazon about 15,500 in another count). OpenAI and Anthropic appear in none of the top lists I read. I could not run the DOL file; the sandbox could not resolve dol.gov. | [S2] [S20]–[S26] | B |
| KF7 | US sponsorship rules are unsettled (V0). The weighted-selection rule (90 FR 60864) took effect 2026-02-27 for the FY2027 cap. The USD 100,000 payment (Proclamation 10973) is not being collected as of 2026-11-13: D. Mass. vacated the implementing policy on 2026-06-08, and the First Circuit refused a stay on 2026-07-24. A second court ruled against the September 2026 extension (reported 2026-09-30), and appeals are pending. An executive order of 2026-09-18 asks agencies to weigh employer layoffs in H-1B decisions. | [S15]–[S19] [S105] | A |
| KF8 | India: 2,117 GCCs, 2.36 million staff and USD 98.4 billion FY26 revenue (NASSCOM–Zinnov). AI, data and cyber were 30.3% of GCC tech hiring demand in Q2 FY27. Five large IT firms added 13,918 net heads in Q2 FY27, and Wipro shrank by 6,716. Frontier labs entered with sales-first local hiring (Anthropic Bengaluru opened 2026-02-16). Sarvam listed 46 roles on 2026-11-02. | [S28] [S62]–[S75] | B |
| KF9 | Curated lists are discovery aids, not volume measures. Forbes AI 50 (2026-04-16) covers private firms only, with OpenAI and Anthropic about 80% of USD 305.6 billion raised. CB Insights AI 100 (May 2026) screened over 40,000 firms and uses "hiring momentum" as one input. No published overlap with observed hiring was found. Big Tech, GCCs and IT services are outside these lists. | [S53]–[S58] | B |
| KF10 | Layoffs.fyi counted 135,446 tech layoffs at 334 companies in 2026 (reading dated November 2026), against 122,606 at 278 in 2025. Meta cut about 10% and froze 6,000 open roles. Oracle cut about 21,000. TCS opened FY27 with 25,000 fresher offers, its lowest start since FY20. I found no study validating funding, headcount or launches as predictors of GenAI hiring. | [S72] [S73] [S82]–[S85] | C |
| KF11 | LinkedIn enforces by contract. Proxycurl shut in July 2025, and a consent judgment against ProAPIs and Netswift followed on 2026-09-16. CNIL fined KASPR EUR 240,000 (decision 2024-12-05; about 160 million contacts). ATS public endpoints are documented for public consumption. Crunchbase API access is by quote and its Basic API is retired. | [S42] [S86] [S91]–[S94] | A |
| KF12 | Of nine knowledge-base claims: confirmed K1, K4, K6; updated K2, K3, K7, K9; stale K8; unverifiable K5. | Repository Deltas | B |

## Recommendation

**Decision rules**
1. Use each employer's own board as the system of record. Use aggregators to discover and rank, and re-count on the board. Store snapshot date and filter with every count. Expect 10–40% disagreement between sources. [KF1–KF3]
2. In the planned script, detect the ATS from the careers URL and confirm it against the vendor endpoint. Cover Greenhouse, Lever, Ashby and Workable first. Treat Workday and custom sites as manual. Identify the client, rate-limit, honour robots.txt, link back to the posting and store no personal data. Re-detect vendors monthly. [KF4]
3. Treat registers as a screen, not a promise. A licence or filing shows an employer has sponsored, not that it will sponsor your role. For the US, rank employers by LCA filings in your SOC codes and titles for FY2025 plus the FY2026 file. Check USCIS pages before acting on fee or lottery rules, because the V0 status can change within days. [KF5–KF7]
4. India-based readers targeting India: Tier 1 is GCCs of banks and global tech, Sarvam, and Bengaluru or New Delhi offices of frontier labs (applied AI, FDE and engineering roles after the sales-first wave). Use IT services for volume but test each firm's GenAI role evidence. Add NL, UK, Denmark and Canada registers only for relocation. [KF8]
5. Avoid LinkedIn-derived scrapers and extension-based contact harvesting. Use Crunchbase Pro for funding lookups, without bulk extraction. [KF11]
6. Cadence: Tier 1 weekly, Tier 2 fortnightly, Tier 3 monthly. Register refresh monthly (UK file changes most working days). LCA refresh when DOL posts a quarter.

**Failure modes**
- Own-board counting: it misses employers on custom or Workday sites, and board totals include non-GenAI roles.
- Register screening: filings can lag a policy change, and entity names fragment (Amazon.com Services LLC vs AWS).
- India GCC focus: GCC hiring volumes come from recruiter indices with differing city shares, and GenAI roles may be fewer than headline totals.
- Avoiding scrapers: it costs speed, and manual lists go stale.

**What would change this:** a USCIS data release for FY2026, appellate rulings on the USD 100,000 payment, a final DOL wage rule, an ATS vendor restricting its public endpoint, or a regulator or court decision on job-board data or contact data.

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| Build the list from Forbes AI 50, CB Insights AI 100 or YC | Discovery only | No hiring-volume validation. They exclude Big Tech, GCCs and IT services. [KF9] |
| Use aggregator job counts as the list | Discovery only | Definitions drift (Chopping Block cut its AI-job total by about 80% between two snapshots). Boards disagree by source. [KF2] |
| Buy PitchBook or Dealroom | Rejected for individuals | PitchBook's typical contract is about USD 31,750 a year (reported). Dealroom Premium is about EUR 12,500 a year. [S89] [S90] |
| Crunchbase Pro | Accepted for lookups | USD 49–99 a month. API and bulk need a licence. [S86] |
| Scrape LinkedIn or use contact-data extensions | Rejected | Contract enforcement and a GDPR fine. [S91]–[S94] |
| Rely on sponsor registers alone | Rejected | Registers carry no role-level information. [S1] [S3] |
| ATS public endpoints plus employer boards | Chosen | Documented for public use. They give A-grade counts. [S42] |

## Detailed Findings

### 1. Employer census

Conventions:
- "AI jobs US" means Chopping Block's open AI jobs in the US on 2026-11-11 [S35] [S36]. Ranges reflect two panels on that page.
- TrueUp figures are labelled July 2026 with no day given [S33].
- "Own custom site" and Workday entries are recalled (D).
- Anthropic is the only board I opened.
- Records for Anduril, Palantir, Booz Allen and GM are included for volume context, not GenAI specificity.
- A record for Hyro (Israel) was drafted and withdrawn because the posting could not be re-checked. The census therefore has 46 employers.

| Employer | Type | Regions | Open GenAI roles (date; filter) | ATS | Sponsorship evidence | Remote / India | Grade |
|---|---|---|---|---|---|---|---|
| Anthropic | frontier lab | US, UK, FR, DE, JP, KR, IN | 682 all roles (2026-11-13; own board; Applied AI 28 on page 3) | Greenhouse | H-1B filings reported (C); no register lookup | Some Remote-Friendly (United States); Bengaluru office 2026-02-16 | A (COI) |
| OpenAI | lab | US, IN | 810 all roles (2026-11-01); 714 (2026-07) | Ashby | H-1B filings reported (C) | Delhi office, sales first (C) | B |
| Google DeepMind | lab | UK, US (D) | not read | Greenhouse (C) | Alphabet FY2025 LCAs 8,161 (B) | — | C |
| xAI | lab | US | 210 (2026-07) | unresolved | — | Reported absorbed into SpaceX (C) | C |
| Mistral AI | lab | FR | 172 (2026-07) | Lever (C) | — | — | C |
| Cohere | lab | CA | 130 (2026-07) | Ashby or Lever (conflict) | — | — | C |
| Perplexity | lab/product | US, IN | rank 16, count not captured | Ashby or Lever (conflict) | — | India BD and partnerships (C) | C |
| Sakana AI | lab | JP | not read; careers page only | not established | Visa assistance stated in postings (2026-05-31) | Tokyo-based | B |
| Sarvam AI | AI startup | IN | 46 (2026-11-02; 37 Bengaluru) | Ashby (C) | n/a | Bengaluru | C |
| G42 | other (sovereign-linked) | AE | not read; posting 2026-09-02 | not established | UAE route not assessed | — | C |
| Google | Big Tech | US | 451–632 AI jobs US | own site (D) | FY2025 LCAs 8,161 (B) | — | B |
| Amazon | Big Tech | US | 388–477 AI jobs US | own site (D) | DOL FY2026 YTD 45,025 positions (A); FY2025 LCAs 21,585 (B) | 16,000 cuts January 2026 (B) | B |
| Microsoft | Big Tech | US | not read | own site (D) | FY2025 LCAs 8,065 (B) | — | C |
| Meta | Big Tech | US | 144–165 AI jobs US | own site (D) | FY2025 LCAs 5,824 (B); DOL top-10 (A) | 10% cut; 6,000-role freeze (B) | B |
| Apple | Big Tech | US | 287–310 AI jobs US | own site (D) | FY2025 LCAs 6,723 (B); DOL top-10 (A) | — | B |
| NVIDIA | Big Tech | US | 178–220 AI jobs US; 2,000 all (2026-07) | Workday (D) | 980 SWE LCAs 2025-10 to 2026-06 (C) | — | B |
| Cisco | Big Tech | US | not read | — | DOL FY2026 YTD 15,786 positions (A) | — | A |
| JPMorgan Chase | enterprise | US, IN | 81 AI jobs US | own site (D) | 1,183 SWE LCAs (C) | India GCC 60,000+ staff; about 1,000 tech hires planned | B |
| Goldman Sachs | enterprise | US, IN | not read | — | DOL top-10 (A) | India GCC larger than any site outside US | B |
| Capital One | enterprise | US | 173–187 AI jobs US | Workday (D) | — | — | B |
| Walmart | enterprise | US | not read | — | 1,257 SWE LCAs (C) | — | C |
| Booz Allen Hamilton | enterprise (federal contractor) | US | 186–187 AI jobs US | — | clearance likely (D) | — | B |
| General Motors | enterprise | US | 57 AI jobs US | — | — | — | B |
| Qualcomm | enterprise | US | not read | — | DOL FY2026 YTD 71,203 positions (A; unusually large) | — | A |
| CGI | IT services | CA, US | not read | — | DOL FY2026 YTD 16,996 positions (A) | — | A |
| Deloitte | IT services | US | not read | — | 1,682 SWE LCAs (C) | — | C |
| Databricks | AI startup | US | 734–904 all roles | Greenhouse (token seen) | — | — | B |
| Harvey | AI startup | US | 333 (2026-07) | Ashby (vendor list) | — | — | B |
| ElevenLabs | AI startup | — | 171 (2026-07) | Ashby (slug seen) | — | — | B |
| Sierra | AI startup | US | 158 (2026-07) | Ashby (vendor list) | — | — | B |
| Glean | AI startup | US | 131 (2026-07) | not established | — | — | B |
| Cursor (Anysphere) | AI startup | US | 113 (2026-07) | Ashby or Lever (conflict) | — | — | B |
| Anduril | AI startup (defence) | US | 522 AI jobs (2026-10-20/28) to 2,165 all (2026-07) | — | citizenship likely (D) | — | B |
| Prolific | AI startup | — | 174 (2026-07) | not established | — | — | B |
| LangChain | AI startup | — | 97 (2026-07) | Ashby (slug seen) | — | — | B |
| Etched | AI startup | US | 99 (2026-07) | not established | — | — | B |
| Hugging Face | AI startup | — | not read | Workable | — | — | C |
| Palantir | other | US | not read | Lever | — | — | C |
| Grab | other | SG | not read; on 2026-07-28 list | not established | — | — | C |
| TCS | IT services | IN | not read; AI revenue above USD 3 billion annualised | not established | n/a | HQ India | B |
| Infosys | IT services | IN | not read; AI 8.2% of revenue (Q1 FY27) | not established | n/a | HQ India | B |
| HCLTech | IT services | IN | not read; 6,136 freshers in Q2 FY27 | not established | n/a | HQ India | B |
| Wipro | IT services | IN | not read; −6,716 net in Q2 FY27 | not established | n/a | HQ India | B |
| Tech Mahindra | IT services | IN | not read; +5,446 net in Q2 FY27 | not established | n/a | HQ India | B |
| Cognizant | IT services | US, IN | not read; 12,000–15,000 cuts planned (C) | not established | n/a | — | C |
| US Tech Force (OPM) | public sector | US | 1,000 early-career places, two years | not established | federal roles, citizenship likely (D) | — | B |

### 2. India

| Segment | Names and cities | Volume evidence | How they hire |
|---|---|---|---|
| GCCs | JPMorgan (Bengaluru, Hyderabad, Mumbai), Goldman Sachs (Bengaluru, Hyderabad), Capital One, Walmart, Google, Microsoft, Amazon (D for the last four) | GCC hiring projected at 510,452 in 2026 [S63] (C). City shares are Bengaluru 30%, Hyderabad 15%, Pune 12%, Mumbai 11%, Chennai 9%, NCR 8% in that source, and Bengaluru 22.6% in Q2 FY27 [S64]. AI, data and cyber were 30.3% of GCC tech hiring demand in Q2 FY27 [S64]. JPMorgan has over 60,000 staff in India and plans about 1,000 tech hires [S65] [S66]. | Parent-company career portals, mostly Workday or custom (D). Banks automate entry-level tasks [S66]. |
| Indian AI startups | Sarvam (Bengaluru), Krutrim, Gnani.ai, Soket | Sarvam raised USD 346 million of USD 399 million Indic-AI funding in 2026 [S75]. It listed 46 roles on 2026-11-02 [S74]. | Sarvam careers page routes via Ashby (C). |
| IT services | TCS (598,056 staff), Infosys, HCLTech (230,339), Wipro, Tech Mahindra | Five firms added 13,918 net in Q2 FY27, and Wipro fell by 6,716 [S69]. TCS AI revenue is above USD 3 billion annualised [S70]. Infosys AI is 8.2% of revenue [S71]. TCS FY27 began with 25,000 fresher offers [S72]. | Campus and lateral hiring. Firms disclose AI revenue and trained-staff counts, not GenAI role counts. |
| Global firms' offices | Anthropic (Bengaluru, 2026-02-16), OpenAI (New Delhi), Perplexity | Anthropic's office was announced by the employer [S28]. India is reported as Claude's second-largest market (C) [S104]. | Sales, partnerships and applied AI first; engineering later [S29] [S67]. |

### 3. Sponsorship registers

| Register | Holds | Update cadence | Access | Limits |
|---|---|---|---|---|
| US DOL LCA disclosure data | Employer-filed LCAs (H-1B, H-1B1, E-3): employer, SOC code and title, job title, worksite, offered wage, wage level, status (field list D) | Quarterly files per fiscal year. FY2025 is the last complete year. FY2026 to 2026-06-30 is published. | [S1]; Selected Statistics [S2] | Filings are not hires. Positions are not LCAs. Entities fragment. Wages are offered, with no equity. |
| USCIS H-1B Employer Data Hub | Employer-level petition decisions by fiscal year (snippet: FY2009 to FY2026 Q4) | Unverified | [S12] bot-blocked | Outage reported March 2026 [S13] [S14]. Employers identified by partial tax ID (D). |
| UK Register of Licensed Sponsors: Workers | Sponsor name, town, county, rating, route (D) | Page updated 2026-11-10; revised on most working days | [S3] CSV about 10.4 MB | A licence is not a vacancy. |
| NL IND public register | Recognised sponsors (labour, highly skilled migrants, research, education, exchange) | Monthly (IND snippet) | [S4] | Recognition is not a vacancy. |
| Canada positive LMIA list | Employers with positive LMIAs | Quarterly | [S5]; Global Talent Stream partner list trimmed September 2026 [S6] | An LMIA is not a job offer. |
| Denmark SIRI Fast-track list | Company name and CVR number; 982 firms reported | "Last updated" at foot of page | [S7] [S8]; a work route from 2027-01-01 covers India and 15 other countries [S9] | Salary-limited tracks only. |
| Australia accredited sponsors | FOI release as at January 2024 | Point-in-time | [S10] | Stale. |
| Ireland | No public list found (C) | — | — | — |

The OECD describes the general design of recognised-employer mechanisms (pre-approved employers that give a faster channel) [S11].

**AI/ML LCA filers.** I could not run the DOL files, so these are aggregator results with their filters.

| Filter and source | Result | Grade |
|---|---|---|
| Exact title "Machine Learning Engineer", FY2025 [S20] [S22] | 1,071 entries; 1,053 filed, 1,040 certified | B |
| Same title, FY2025 top filers [S23] (year label uncertain) | Adobe 114, Apple 108, TikTok 79, ByteDance 57, Meta 32 | B |
| Vendor AI/ML set, FY2021–FY2026 partial [S21] | Amazon.com Services 4,252; Apple 2,115; Microsoft 1,989; Meta 522; Amazon Development Center US 437; AWS 430 | B |
| All titles, FY2025 certified [S24] | Amazon 21,585; Google 8,161; Microsoft 8,065; Apple 6,723; Meta 5,824 | B |
| All titles, Amazon, FY2025 [S26] | About 15,500 | C |
| DOL positions certified, FY2026 to 2026-06-30 [S2] | Grandison Management 79,121; Qualcomm 71,203; Amazon 45,025; CGI 16,996; Cisco 15,786; then Goldman Sachs, Apple, Meta | A |

The DOL figures were transcribed at first read and the PDF could not be re-opened.

Reproducible filter [P]: `visa_class = H-1B`, status certified, and (`soc_code` in 15-1221 or 15-2051, or `job_title` matches `machine learning|ML engineer|AI engineer|applied scientist|research scientist|data scientist|LLM|generative|NLP`). Count LCAs and positions separately, and merge entity names.

### 4. Curated lists

| List | Publisher, date | Method | Overlap with hiring |
|---|---|---|---|
| Forbes AI 50 | Forbes with Sequoia and Meritech, 2026-04-16 | Unranked, private firms, nominations plus algorithm; Mayfield sponsor [S53] | Not computed. OpenAI and Anthropic hold about 80% of USD 305.6 billion raised [S54]. |
| CB Insights AI 100 | CB Insights, May 2026 | More than 40,000 screened; deal activity, investors, hiring momentum, Mosaic and Commercial Maturity [S56] | Not computed. Vendor claims 64% of winners closed follow-on rounds against 31% (COI) [S57]. |
| TrueUp Generative AI 50 | TrueUp, July 2026 | Editorial; names visible in the snippet run A–R only | Computed (M): 10 of TrueUp's top-15 hirers appear in the A–R part of its own list; Prolific, Cursor and LangChain are absent; xAI and Sierra unknown. Same publisher, so not independent. [S33] |
| YC batches | YC directory | S26 about 235 companies (largest) [S58] | Not computed. |
| NASSCOM–Zinnov GCC | May 2026 | 2,117 GCCs, 2.36 million staff, USD 98.4 billion FY26 [S62] | Press coverage only. |

### 5. Hiring signals and layoffs

- Open roles on the employer's board are the only direct measure (A). Role age is a weak ghost-job proxy: one aggregator reports a 62-day median at Anthropic and 449 of 603 roles as stale (C, method not shown) [S30].
- Funding: Sarvam's April 2026 round was followed by 46 listed roles, which is an anecdote [S74] [S75].
- Product and office launches: Anthropic's Bengaluru office was announced with local hiring [S28].
- Headcount: IT services publish quarterly net adds, which are not GenAI-specific [S69].
- I found no study validating any signal as a predictor.
- Layoffs: Layoffs.fyi 135,446 at 334 companies for 2026 [S82]; 128,536 at 299 on 2026-09-10 [S83]. AI attribution disagrees: 36% [S82] against 72% from an unnamed tracker [S85]. Meta froze 6,000 open roles [S84]. Cognizant planned 12,000–15,000 cuts (C) [S73].
- startup.jobs reports AI/ML at 1.6% of postings at established startups, with postings down 9.7% year on year (2026-10-27) [S40].
- BLS projects data scientists +34.6% and computer and information research scientists +21.8% for 2025–35 [S95].

### 6. Datasets and terms

| Dataset | What | Price | Terms | Legal risk | Verdict |
|---|---|---|---|---|---|
| DOL LCA data | Employer filings | Free | US federal data; licence not checked | Low | use |
| USCIS H-1B Hub | Petition outcomes | Free | Site terms not read | Low; availability risk (outage March 2026) | use-with-care |
| UK sponsor register | Licensed sponsors | Free | GOV.UK; licence not checked | Low | use |
| IND register | Recognised sponsors | Free | Public register | Low | use |
| Canada LMIA list | Positive-LMIA employers | Free | Open Government Licence (D) | Low | use-with-care |
| Denmark SIRI list | Certified firms | Free | Public | Low | use |
| Greenhouse, Lever, Ashby, Workable endpoints | Open postings JSON | Free | Greenhouse says GET endpoints need no authentication; Lever's README says postings may be scraped by third parties (both as quoted in S42); Ashby's API host robots.txt returned 401 on 2026-11-02 per one tool author [S43]; employer owns the content; ToS texts not opened | Low to medium | use-with-care |
| Crunchbase | Companies, funding | Pro USD 49 a month on annual billing in year one, USD 79 list after, USD 99 monthly; Business from USD 199; exports 2,000 or 5,000 rows a month; API and bulk by quote, reported to start around USD 50,000 a year [S86] [S87] | Basic API retired; ToS reportedly bars automated collection (C; not opened) | Contract | use-with-care |
| Dealroom | EU-strong startup data | Premium about EUR 12,500 a year, with 10,000 export credits per user [S89] | T&Cs (October 2026): separate API licence; personal data must be deleted when the licence ends [S88] | Personal-data duties | use-with-care |
| Tracxn | Startup and funding data; its reports supply Indian funding figures quoted by the press [S75] | Not retrieved in this session | Not retrieved | — | watch |
| PitchBook | Deal data | Typical contract about USD 31,750 a year, with deals from USD 20,000 to 122,500 (reported) [S90] | Licensed | — | watch |
| TrueUp, Fast AI Jobs, FourWeekMBA, Chopping Block | Job and company trackers | Free | ToS not read | Drift; own-board claims are vendor claims | use-with-care |
| startup.jobs stats | Posting statistics | Free | Invites citation with attribution [S40] | Low | use-with-care |
| Layoffs.fyi | Tech layoff tracker | Free | Third party | Conflicting totals | use-with-care |
| Huntr research | Applicant-tracker user data | Free | Self-tracked, skewed [S50] | — | use-with-care |
| Forbes AI 50, CB AI 100, YC directory | Curated lists | Free | Publisher terms not read | — | use-with-care |
| LinkedIn-derived scrapers and fake-account APIs | Profile data | Various | Breach LinkedIn's agreement; Proxycurl shut; consent judgment 2026-09-16 [S92] [S93] | High | avoid |
| Contact-data products (Apollo, RocketReach, Hunter, ZoomInfo, Lusha) | Contacts | Outreach session | Terms not assessed. LinkedIn removed Apollo and Seamless company pages in March 2025; Apollo's page was back by 2026-07-28 [S94]. CNIL fined KASPR [S91]. | Medium to high | watch |
| BLS EP and OOH; O*NET | Official labour data | Free | Official | Low | use |

### 7. Target-list method (50–100 employers)

1. **Frame** a matrix of role family × geography × visa need. [P]
2. **Seed** from four universes: own-board volume leaders (S27, S32); curated lists for discovery (S53–S58); register-filtered sponsors (S1, S3, S4, S7); India GCC and IT lists (S62). [A/B]
3. **Resolve the board.** Detect the ATS from the careers URL and confirm it against the public endpoint. Re-detect monthly. [B] [S42] [S50]
4. **Count and filter.** Use a keyword filter on title and department, and record date and filter. Expect ±10% movement within weeks. [P] [S27] [S30]–[S33]
5. **Screen visas and location** with register evidence, then recheck V0 policy status. [A] [S3] [S15]–[S19]
6. **Tier.** Tier 1 (≤15): at least 10 matching open roles on the own board, or at least 1 in your location, plus register evidence. Tier 2 (≤35): matching roles but weaker register evidence. Tier 3 (≤50 watchlist): signals such as an office opening or funding. [P]
7. **Review.** Tier 1 weekly, Tier 2 fortnightly, Tier 3 monthly, register refresh monthly, LCA refresh quarterly, tier moves quarterly. [P] [S3] [S4]
8. **Hygiene.** Keep no personal data on employees or recruiters, use public role pages only, and avoid scraped contacts. [A] [S91]–[S93]

### 8. Knowledge-base claims tested

- **K2:** Levels.fyi-based pulls dated 2026-08-15 give a US ML Engineer median total compensation of USD 278,000 and AI Engineer USD 159,430, a ratio of 0.57 (M) [S97]. The employer-mix share is unverified.
- **K3:** OpenAI's median is about USD 795,000–800,000 against USD 265,000–278,000 (2.9–3.0×, M). Anthropic's is USD 600,000–710,000 (2.2–2.7×, M) [S97] [S99] [S100] [S103]. Filed base pay at the labs is about USD 310,000–315,000 against typical MLE base of USD 160,000–190,000 [S98] [S101]. Base is therefore also higher, and "almost entirely equity" is not supported. The filed bases cover H-1B filers only.
- **K4:** Traces to a Dell–Zinnov report released at Dell Technologies Forum 2026 (vendor-sponsored, published 2026-09-25) [S59] [S60]. Infosys's 500-GCC index reports 27% with meaningful business impact [S61].
- **K5:** Fast AI Jobs pages show 275 AI Engineer postings at 170 startups (newest posting 2026-07-30) [S37] and 28,414 postings at 1,824 startups (2026-08-03) [S38]. I could not open a 2026-10-19 snapshot.
- **K7, K8:** BLS released 2025–35 projections on 2026-08-27, and the OOH features them [S95]. I found no O*NET page evidence.
- **K9:** Huntr's Q1 2026 report matches (139,927 applications, 25,635 job seekers) [S52]. Q2 and Q3 2026 reports exist [S50] [S51], and Q3 restates Q2's median time to first offer (91 against 82 days).

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Six employer types; evidence thinnest for IT services and public sector | confirmed | [S27] [S32] [S68]–[S72] [S80] | C |
| K2 | AI Engineer title pays 0.55–0.56× ML Engineer; half is employer mix | updated | [S97] (ratio 0.57, M) | C |
| K3 | Frontier labs about 3× ML Engineer median, almost entirely equity | updated | [S97]–[S101] [S103] | C |
| K4 | Nearly 70% of India GCCs at pilot stage | confirmed | [S59] [S60] [S61] | B |
| K5 | 326 AI Engineer postings at 183 startups on 2026-10-19 | unverifiable | [S37] [S38] | B |
| K6 | LCA wage filings are what was filed, not what people earn | confirmed | [S1] [S2] [S98] | A |
| K7 | BLS OOH: use | updated | [S95] | A |
| K8 | O*NET: use; sources cite BLS 2024–34 | stale | [S95] | C |
| K9 | Huntr reports: use-with-care | updated | [S50] [S51] [S52] | B |

## Absences

| Item | Where I looked |
|---|---|
| Raw LCA FY2025 ranking by AI/ML titles | The sandbox could not resolve dol.gov. Web search returned aggregator tables only. |
| USCIS Employer Data Hub employer-level data | The page was bot-blocked. Only snippets and outage reports were read. |
| UK and NL register lookups for the 46 employers | The 10.4 MB UK CSV and the IND register were not opened. |
| Equivalent registers in Germany, Japan, Singapore, Gulf states, Switzerland, Israel | Not searched individually. One combined search covered Ireland (no public list found), Denmark, Australia, Canada and New Zealand. |
| Own-site open-role counts for 45 of 46 employers | ATS boards are fetchable only after a search returns their URL. Other sites were JS-rendered, blocked or not reached. |
| GenAI-only counts | I found only all-role totals and vendor AI-job definitions. |
| Employers in Korea, Israel, Australia, Switzerland, EU (Aleph Alpha, DeepL, Black Forest Labs, Helsing) and Gulf (HUMAIN, MBZUAI) | Searches returned no usable employer-level evidence. A Korea listicle was too weak to use. A Hyro (Israel) record was withdrawn. |
| Public sector beyond US Tech Force (UK AI Security Institute, GovTech Singapore, India) | One combined search; only US Tech Force coverage retrieved. |
| NASSCOM–Zinnov and Dell–Zinnov full reports and methods | Press coverage only. |
| Overlap of Forbes AI 50 and CB Insights AI 100 with hiring | Full lists not retrieved; only a partial TrueUp overlap computed. |
| Predictive validity of hiring signals | Searched. No study found. |
| Vendor ToS texts (Crunchbase, Tracxn, TrueUp, Fast AI Jobs, Greenhouse, Lever, Ashby, Workable) | Not opened. Secondary summaries only (Dealroom T&Cs and pricing were read). |
| Enforcement against Apollo, ZoomInfo, Lusha, RocketReach, Hunter | Searched. None found beyond KASPR and LinkedIn's litigation. |
| O*NET OnLine page status (K8) | Not opened. The BLS 2025–35 release was read instead. |
| UK Skilled Worker rule changes in 2025–2026 | Not researched. |
| Remote-hiring policy for most employers | Only Anthropic's board (Remote-Friendly flags) and Sakana's posting text were read. |

## Open Questions & Risks

- Which taxonomy should define "GenAI role" for the script? Title keywords and department filters disagree by at least a factor of two on Anthropic's board.
- US sponsorship status is V0 (pending appeals, a proposed fee rule and a DOL wage proposal). Recheck before advising.
- Aggregators show definition drift, and ATS attribution conflicts. Both affect a script seeded from them.
- Regional coverage is thin outside the US and India.

| Objection | For | Against |
|---|---|---|
| Counts are not GenAI-specific. | Anthropic's board includes compute, comms and finance roles. | I labelled every count with its filter and flagged all-role totals. |
| LCAs show filings, not hires. | The DOL data are employer attestations. Big Tech counts include continuing staff. | I reported them as filings only (K6). |
| Aggregator numbers are unreliable. | Chopping Block's AI-job total fell about 80% between two snapshots; Anthropic readings span 400–682. | Ranges and dates are shown, and the own board is the system of record. |
| ATS public endpoints may breach terms. | Ashby's API robots.txt returned 401 on 2026-11-02 [S43]. | Greenhouse and Lever document public use. I did not open the ToS texts. |
| K3 base-pay comparison suffers survivor bias. | Filed bases cover H-1B filers only. | Levels.fyi totals show the same 2.9–3.0× for OpenAI. |

## Discovered Concerns

1. The executive order of 2026-09-18 directs agencies to weigh employer layoffs in H-1B decisions. This links the layoff signal to sponsorship risk. [S17]
2. xAI is reported absorbed into SpaceX (closed February 2026), so employer identity changes affect lists. [S55]
3. Denmark opens a work route on 2027-01-01 that includes India among 16 countries. [S9]
4. Canada trimmed Global Talent Stream referral partners in September 2026. [S6]
5. LinkedIn consent judgments (2026-09-16) tighten the scraping environment. [S93]
6. TCS's lowest fresher start since FY20 and Bloomberg's report of GCC automation of entry-level tasks matter for India-based juniors. [S66] [S72]

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Big Tech and a few labs hold most open AI roles; sources disagree | Confirmed | S32, S35, S36 | Rank with ranges. Re-count on own boards. |
| P2 | Greenhouse, Lever and Ashby with public endpoints | Updated | S42–S50 | Endpoints confirmed, but vendor attribution conflicts and shifts. |
| P3 | USD 100,000 payment collected | Contradicted | S16–S19, S105 | Not collected as of 2026-11-13, but extended on paper and litigated. |
| P4 | UK and NL registers free; USCIS hub online | Updated | S3, S4, S12–S14 | UK and NL confirmed. The USCIS hub had an outage and bot-blocked my fetch. |
| P5 | Crunchbase free API gone; scraping barred | Confirmed | S86, S87 | Pro for lookups only (C-grade sources; ToS not opened). |
| P6 | GCCs and IT services supply most India volume | Confirmed | S62–S66, S28 | Labs hire sales-first locally. |

## Sources & Evidence Ledger

All sources were retrieved 2026-11-13. "n/d" means no publication date was shown.

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | OFLC Performance Data, US DOL — https://www.dol.gov/agencies/eta/foreign-labor/performance | n/d | 2026-11-13 | A | Read | — | LCA files, FY coverage |
| S2 | LCA Selected Statistics FY2026 Q3, US DOL — https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/FY26Q3/LCA_Selected_Statistics_FY2026_Q3.pdf | 2026 Q3 | 2026-11-13 | A | Read | single read | Top employers by positions |
| S3 | Register of licensed sponsors: workers, GOV.UK — https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers | page updated 2026-11-10 | 2026-11-13 | A | Read | — | UK register |
| S4 | Public register recognised sponsors, IND — https://ind.nl/en/public-register-recognised-sponsors | n/d | 2026-11-13 | A | Extract | — | NL register |
| S5 | Positive LMIA Employers List, Open Government Portal — https://open.canada.ca/data/en/dataset/90fed587-1364-4f33-a9ee-208181dc0b97 | n/d | 2026-11-13 | A | Extract | — | Canada list |
| S6 | Canada trims Global Talent Stream partners, CIC News — https://www.cicnews.com/2026/09/canada-trims-list-of-partners-providing-access-to-fast-track-hiring-under-global-talent-stream-of-tfwp-0980494.html | 2026-09 | 2026-11-13 | C | Extract | — | GTS partners |
| S7 | Certified companies, SIRI (nyidanmark.dk) — https://www.nyidanmark.dk/en-GB/Words-and-concepts/SIRI/Certified-companies | n/d | 2026-11-13 | A | Extract | — | Denmark list |
| S8 | Denmark lists 982 firms, YEN.com.gh — https://yen.com.gh/world/313014-denmark-lists-982-companies-approved-hire-foreign-workers-fast-track-scheme/ | n/d | 2026-11-13 | C | Extract | — | Denmark count |
| S9 | Denmark new work route 2027, Business Standard — https://www.business-standard.com/immigration/denmark-to-open-new-work-route-in-2027-eligibility-and-key-rules-explained-126090800852_1.html | 2026-09-08 | 2026-11-13 | B | Extract | — | Denmark 2027 |
| S10 | Australia sponsor list, YEN.com.gh — https://yen.com.gh/world/315411-australia-publishes-list-1000-approved-sponsors-foreign-workers/ | n/d | 2026-11-13 | C | Extract | — | FOI list |
| S11 | Recognised employer mechanisms, OECD — https://www.oecd.org/en/publications/admitting-labour-migrants_03b9965e-en/full-report/how-do-recognised-employer-mechanisms-work_fa929f9b.html | n/d | 2026-11-13 | B | Extract | — | Register concept |
| S12 | H-1B Employer Data Hub, USCIS — https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub | n/d | 2026-11-13 | A | Blocked | snippet only | Hub scope |
| S13 | USCIS hub returns after five-day outage, Dallas Express — https://dallasexpress.com/business-markets/uscis-h-1b-employer-data-hub-returns-online-after-five-day-outage/ | 2026-03 | 2026-11-13 | C | Extract | — | Outage |
| S14 | H-1B hub offline, American Bazaar — https://americanbazaaronline.com/2026/03/12/h-1b-employer-data-hub-goes-offline-key-data-missing-476704/ | 2026-03-12 | 2026-11-13 | C | Extract | — | Missing data |
| S15 | Weighted Selection Final Rule, 90 FR 60864, GovInfo — https://www.govinfo.gov/content/pkg/FR-2025-12-29/html/2025-23853.htm | 2025-12-29 | 2026-11-13 | A | Extract | — | Cap rule |
| S16 | September 2026 H-1B changes, National Law Review — https://natlawreview.com/article/september-2026-h-1b-changes-new-compliance-scrutiny-and-extension-100000-entry | 2026-09 | 2026-11-13 | B | Extract | — | Fee status |
| S17 | USD 100,000 H-1B extended, Klasko — https://www.klaskolaw.com/h-1b-100000-fee-extended-one-year/ | 2026-09-23 | 2026-11-13 | B | Extract | — | Proclamation, EO |
| S18 | Judge strikes down fee, Forbes (S. Anderson) — https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/ | 2026-10-01 | 2026-11-13 | B | Extract | — | Second ruling |
| S19 | H-1B fee status, InterviewerSignal — https://interviewersignal.com/blog/h-1b-100000-fee | 2026-11 | 2026-11-13 | C | Extract | single-source | Collection status |
| S20 | ML Engineer H-1B sponsors, VisaPulse — https://visapulseusa.com/jobs/machine-learning-engineer | n/d | 2026-11-13 | B | Extract | — | Exact-title count |
| S21 | AI and ML H-1B data, VisaPulse — https://visapulseusa.com/ai-jobs | n/d | 2026-11-13 | B | Extract | — | AI/ML set |
| S22 | ML Engineer LCA FY2025, H1BGrader — https://h1bgrader.com/job-titles/machine-learning-engineer-370oqexvkz/lca/2025 | n/d | 2026-11-13 | B | Extract | — | Exact-title count |
| S23 | ML Engineer H-1B, MyVisaJobs — https://www.myvisajobs.com/reports/h1b/job-title/machine-learning-engineer/ | n/d | 2026-11-13 | B | Extract | year label uncertain | Top filers |
| S24 | H1B Database, H1BVisaJobs — https://h1bvisajobs.com/h1b-database | 2026 | 2026-11-13 | B | Extract | — | FY2025 LCA totals |
| S25 | H-1B SWE sponsors, Scoutify — https://scoutify.com/blog/h1b-software-engineer-jobs/ | 2026-10 | 2026-11-13 | C | Extract | — | SWE LCAs |
| S26 | Does Amazon sponsor H-1B, F1Jobs — https://www.f1jobs.io/resources/blog/amazon-h1b-sponsorship-international-candidate-guide-2026 | 2026 | 2026-11-13 | C | Extract | — | Amazon LCA range |
| S27 | Anthropic jobs board (page 3 of 14), Greenhouse — https://job-boards.greenhouse.io/anthropic?page=3 | live | 2026-11-13 | A | Read | COI | 682 jobs, ATS |
| S28 | Anthropic opens Bengaluru office, Anthropic — https://www.anthropic.com/news/bengaluru-office-partnerships-across-india | 2026-02-16 | 2026-11-13 | A | Extract | COI | India presence |
| S29 | Anthropic taps ex-Microsoft India MD, TechCrunch — https://techcrunch.com/2026/01/15/anthropic-taps-former-microsoft-india-md-to-lead-bengaluru-expansion/ | 2026-01-15 | 2026-11-13 | B | Extract | — | India hiring |
| S30 | Anthropic jobs, PitchMeAI — https://pitchmeai.com/companies/anthropic | checked 2026-10-08 | 2026-11-13 | C | Extract | single-source | 603; staleness |
| S31 | Hiring Signals scorecard, Apify — https://apify.com/nexgendata/hiring-signals-notion | 2026-09-25 | 2026-11-13 | C | Extract | — | 622 |
| S32 | AI Company Index, FourWeekMBA — https://fourweekmba.com/ai-company-index/ | 2026-11-01 | 2026-11-13 | B | Extract | — | Volumes |
| S33 | Generative AI report, TrueUp — https://trueup.io/generative-ai/reports | 2026-07 | 2026-11-13 | B | Extract | — | GenAI volumes |
| S34 | AI report, TrueUp — https://trueup.io/ai/reports | 2026-07 | 2026-11-13 | B | Extract | — | NVIDIA, Anduril |
| S35 | AI Chopping Block home (AI jobs) — https://www.choppingblock.ai/?jobs=ai | snapshot 2026-11-11 | 2026-11-13 | B | Read | — | US AI jobs |
| S36 | AI Chopping Block (earlier snapshots) — https://www.choppingblock.ai/?jobs=ai&roles=all | about 2026-10-20 to 10-28 | 2026-11-13 | B | Extract | — | Definition drift |
| S37 | AI Engineer jobs, Fast AI Jobs — https://www.fastaijobs.com/jobs/role/ai-engineer | about 2026-08 | 2026-11-13 | B | Extract | — | K5 |
| S38 | Entry-level AI startup jobs, Fast AI Jobs — https://www.fastaijobs.com/career-hacks/entry-level-ai-jobs-august-2026 | 2026-08-03 | 2026-11-13 | B | Extract | — | Database size |
| S39 | Top AI startups hiring, Fast AI Jobs — https://www.fastaijobs.com/collections/top-ai-startups-hiring | n/d | 2026-11-13 | B | Extract | — | Databricks, Anduril |
| S40 | Startup hiring statistics, Startup Jobs — https://startup.jobs/startup-hiring-statistics | 2026-10-27 | 2026-11-13 | B | Extract | — | AI share |
| S41 | Three AI labs, 708 open roles, newsletter — https://lindsaysnewsletter.substack.com/p/three-ai-labs-708-open-roles-and | n/d | 2026-11-13 | C | Extract | — | Board URLs |
| S42 | Company Jobs Feed (quotes vendor docs), Apify — https://apify.com/fairquery/company-jobs-feed | 2026 | 2026-11-13 | C | Extract | — | ATS endpoints |
| S43 | ATS Jobs (robots notes), Apify — https://apify.com/staticxviper/ats-jobs | 2026-11-02 | 2026-11-13 | C | Extract | single-source | Ashby robots; Workable |
| S44 | Public ATS APIs, DEV Community — https://dev.to/glitchbound/indeed-403s-you-with-zero-bytes-the-companies-it-aggregates-publish-free-apis-2k46 | n/d | 2026-11-13 | C | Extract | — | OpenAI Ashby 753 |
| S45 | Multi-ATS feed, Apify — https://apify.com/bikram07/multi-ats-jobs-feed | 2026 | 2026-11-13 | C | Extract | — | Mistral Lever |
| S46 | ATS Jobs Scraper, Apify — https://apify.com/mukeshrana90/ats-jobs-scraper | 2026 | 2026-11-13 | C | Extract | — | Ashby list |
| S47 | Companies using each ATS, JobsPipe — https://jobspipe.dev/companies-using.md | 2026-07 | 2026-11-13 | C | Extract | — | Ashby customers |
| S48 | State of ATS 2026, ResumeAI — https://withresumeai.com/reports/state-of-ats-2026 | 2026 | 2026-11-13 | C | Extract | conflicts S46, S47 | Lever claims |
| S49 | Ashby llms.txt, Ashby — https://www.ashbyhq.com/llms.txt | n/d | 2026-11-13 | A | Extract | COI | Customer list |
| S50 | Q3 2026 Job Search Trends, Huntr — https://huntr.co/research/job-search-trends-q3-2026 | 2026 Q3 | 2026-11-13 | B | Extract | COI | K9, ATS shares |
| S51 | Q2 2026 Job Search Trends, Huntr — https://huntr.co/research/job-search-trends-q2-2026 | 2026-08 | 2026-11-13 | B | Extract | COI | K9 |
| S52 | Q1 2026 Job Search Trends, Huntr — https://huntr.co/research/job-search-trends-q1-2026 | 2026 Q2 | 2026-11-13 | B | Extract | COI | K9 |
| S53 | Forbes AI 50 profile, Superscout — https://superscout.co/rankings/forbes-ai-50 | 2026 | 2026-11-13 | C | Extract | — | Forbes method |
| S54 | Forbes 2026 AI 50, MarketScale — https://www.marketscale.com/industries/software-and-technology/the-2026-forbes-ai-50-reveals-3056-billion-raised-consolidating-fast-around-a-handful-of-giants | 2026-08-01 | 2026-11-13 | C | Extract | — | Totals |
| S55 | Forbes AI 50 concentration, CloudTweaks — https://cloudtweaks.com/2026/07/forbes-ai-50-more-concentrated-than-appears/ | 2026-07 | 2026-11-13 | C | Extract | single-source | xAI in SpaceX |
| S56 | CB Insights AI 100 (press boilerplate), Business Wire — https://www.businesswire.com/news/home/20260513962615/en/ | 2026-05-13 | 2026-11-13 | B | Extract | — | AI 100 method |
| S57 | AI 100 listing, Neura — https://www.neura.market/ai-tools-directory/all/cb-insights-ai-100-the-most-promising-artificial-intelligence-startups-of-2026-may-2026 | 2026-05 | 2026-11-13 | C | Extract | COI | 64% claim |
| S58 | YC S26 Demo Day, Foundra — https://www.foundra.ai/key-reads/yc-s26-demo-day-agent-infrastructure-founder-strategy-2026 | 2026-09 | 2026-11-13 | C | Extract | — | S26 size |
| S59 | Dell–Zinnov GCC report, Entrepreneur India — https://india.entrepreneur.com/business-news/indias-gccs-to-become-ai-transformation-engines-by-2030-dell-zinnov | 2026-09-25 | 2026-11-13 | B | Extract | COI (sponsor) | K4 |
| S60 | GCCs stuck at pilot stage, Analytics India Magazine — https://analyticsindiamag.com/ai-news/indias-gccs-face-ai-shift-as-nearly-70-remain-stuck-at-pilot-stage-report | 2026-10-18 | 2026-11-13 | C | Extract | — | K4 |
| S61 | AI-First GCC Index 2026, Infosys — https://www.infosys.com/newsroom/features/2026/ai-first-gcc-index2026.html | 2026 | 2026-11-13 | B | Extract | COI | Counter-framing |
| S62 | NASSCOM–Zinnov 2,117 GCCs, YourStory — https://yourstory.com/enterprise-story/2026/05/gccs-number-touch-2117-in-india-revenue-just-short-of-100-billion | 2026-05 | 2026-11-13 | B | Extract | — | GCC scale |
| S63 | GCC hiring 5.1 lakh, Business Today — https://www.businesstoday.in/jobs/story/at-5-1-lakh-jobs-indias-global-capability-centre-hiring-boom-scales-new-peak-540328-2026-07-01 | 2026-07-01 | 2026-11-13 | C | Extract | — | Hiring, cities |
| S64 | GCC tech hiring Q2 FY27, Business Standard — https://www.business-standard.com/industry/news/ai-data-and-cybersecurity-drive-3-in-10-gcc-tech-hiring-demand-report-126110501019_1.html | 2026-11-05 | 2026-11-13 | C | Extract | — | AI share |
| S65 | JPMorgan 1,000 GCC hires, Business Standard — https://www.business-standard.com/world-news/jpmorgan-plans-1-000-india-gcc-hires-despite-ai-driven-workforce-cuts-126072300511_1.html | 2026-07-23 | 2026-11-13 | B | Extract | — | JPMorgan India |
| S66 | AI and entry-level tech jobs, Business Standard (Bloomberg) — https://www.business-standard.com/industry/news/ai-eats-into-entry-level-tech-jobs-as-india-s-graduates-seek-work-126100800232_1.html | 2026-10-08 | 2026-11-13 | B | Extract | — | GCC headcounts |
| S67 | OpenAI and Anthropic India strategy, AIM — https://analyticsindiamag.com/global-tech/the-indian-dream-of-american-ai-companies | 2025 | 2026-11-13 | C | Extract | — | Delhi, sales-first |
| S68 | HCLTech Q2 FY27 headcount, People Matters — https://www.peoplematters.in/news/recruiting-and-onboarding/hcltech-attrition-rises-to-128percent-as-headcount-grows-by-6450-in-q2-52678 | 2026-10 | 2026-11-13 | B | Extract | — | HCLTech |
| S69 | Indian IT giants add 14,000, Free Press Journal — https://www.freepressjournal.in/business/indian-it-giants-add-14000-employees-in-q2 | 2026-10 | 2026-11-13 | C | Extract | — | Net adds |
| S70 | TCS Q2 FY27, YourStory — https://yourstory.com/enterprise-story/2026/10/tcs-reports-15-rise-in-net-profit-in-q2-of-fy27 | 2026-10 | 2026-11-13 | B | Extract | — | TCS |
| S71 | IT Q2 FY27 preview, Bajaj Broking — https://www.bajajbroking.in/share-market-news/it-q2-fy27-preview-tcs-infosys-growth-seen-as-muted | 2026-10 | 2026-11-13 | C | Extract | — | Infosys 8.2% |
| S72 | TCS FY27 hiring plan, Business Standard — https://www.business-standard.com/companies/news/what-tcs-s-fy27-hiring-plan-tells-about-fresher-model-in-indian-it-sector-126041400641_1.html | 2026-04-14 | 2026-11-13 | B | Extract | — | Fresher offers |
| S73 | Global tech layoffs, Angel One — https://www.angelone.in/news/market-updates/global-tech-layoffs-crosses-93-000-so-far-in-2026-amid-ai-driven-restructuring | 2026-05-08 | 2026-11-13 | C | Extract | — | Cognizant |
| S74 | Sarvam AI careers, CareerIndia — https://www.careerindia.com/news/sarvam-ai-careers-2026-open-engineering-roles-bengaluru-application-guide-011-68035.html | 2026-11 | 2026-11-13 | C | Extract | — | Sarvam roles |
| S75 | Sarvam and Indic AI funding, Business Standard — https://www.business-standard.com/companies/news/sarvam-dominates-indic-ai-funding-in-2026-with-87-share-tracxn-report-126102801327_1.html | 2026-10-28 | 2026-11-13 | B | Extract | — | Funding |
| S76 | Applied Scientist posting, G42 — https://jobs.g42.ai/Inception42/job/Abu-Dhabi-Applied-Scientist-Abu/732148722/ | 2026-09-02 | 2026-11-13 | A | Extract | — | G42 |
| S77 | Career opportunities, Sakana AI — https://sakana.ai/careers | n/d | 2026-11-13 | A | Extract | — | Sakana |
| S78 | Sakana AI posting, Khosla Ventures job board — https://jobs.khoslaventures.com/companies/sakana-ai-2/jobs/81153321-software-engineer-product | 2026-05-31 | 2026-11-13 | B | Extract | — | Visa assistance |
| S79 | Companies hiring AI engineers in Singapore, Built In — https://builtin.com/articles/companies-hiring-ai-engineers-singapore | 2026-07-28 | 2026-11-13 | C | Extract | — | Grab |
| S80 | OPM unveils US Tech Force, ExecutiveGov — https://executivegov.com/articles/opm-us-tech-force-ai-adoption | 2026-03-05 | 2026-11-13 | B | Extract | — | Tech Force |
| S81 | OPM recruits Scale AI and eight firms, ClearanceJobs — https://news.clearancejobs.com/2026/06/09/opm-recruits-scale-ai-and-eight-tech-firms-to-help-modernize-the-federal-government/ | 2026-06-09 | 2026-11-13 | B | Extract | — | Tech Force partners |
| S82 | Startup layoffs news Nov 2026, Mean CEO — https://blog.mean.ceo/startup-layoffs-news-november-2026/ | 2026-11 | 2026-11-13 | C | Extract | cites Layoffs.fyi | 135,446 |
| S83 | Global tech layoffs 2026, Business Standard — https://www.business-standard.com/industry/news/global-tech-layoffs-2026-oracle-amazon-dell-uber-paypal-it-sector-job-cuts-126091100188_1.html | 2026-09-11 | 2026-11-13 | B | Extract | — | Oracle, Amazon |
| S84 | AI push deepens layoffs, Business Standard — https://www.business-standard.com/industry/news/ai-push-deepens-layoffs-as-big-tech-cuts-workforce-trims-hiring-globally-126042401011_1.html | 2026-04-24 | 2026-11-13 | B | Extract | — | Meta freeze |
| S85 | Layoffs and AI attribution, Crunchbase News — https://news.crunchbase.com/?p=94113 | 2026 | 2026-11-13 | B | Extract | tracker unnamed | 72% claim |
| S86 | Crunchbase pricing, Private Equity List — https://privateequitylist.com/intelligence/crunchbase-pricing | checked 2026-11-09 | 2026-11-13 | C | Extract | — | Pricing |
| S87 | Crunchbase API alternatives, Multiples — https://multiples.vc/compare/crunchbase-api-alternatives/md | 2026-08 | 2026-11-13 | C | Extract | — | API retired |
| S88 | Terms & Conditions, Dealroom — https://dealroom.co/terms-and-conditions | 2026-10 | 2026-11-13 | A | Extract | self-published | Dealroom terms |
| S89 | Pricing, Dealroom — https://content.dealroom.co/pricing | n/d | 2026-11-13 | A | Extract | self-published | Dealroom price |
| S90 | PitchBook and Crunchbase API pricing, Private Equity List — https://privateequitylist.com/intelligence/pitchbook-crunchbase-api-pricing | 2026-10-31 | 2026-11-13 | C | Extract | — | PitchBook price |
| S91 | Data scraping: CNIL fined KASPR EUR 240,000, EDPB — https://www.edpb.europa.eu/news/data-scraping-french-supervisory-authority-fined-kaspr-eu240-000_en | decision 2024-12-05 | 2026-11-13 | A | Extract | — | KASPR |
| S92 | LinkedIn battles scrapers, Bloomberg Law — https://news.bloomberglaw.com/ip-law/linkedin-battles-online-scrapers-in-perpetual-struggle-over-data | 2025 | 2026-11-13 | B | Extract | — | Proxycurl, hiQ |
| S93 | LinkedIn v ProAPIs final judgment, Digital Policy Alert — https://digitalpolicyalert.org/event/43954-us-district-court-issued-final-judgment-in-linkedin-v-proapis-data-scraping-lawsuit | 2026-09 | 2026-11-13 | B | Extract | — | Consent judgment |
| S94 | LinkedIn B2B data crackdown, LeadGenius — https://www.leadgenius.com/resources/linkedins-b2b-data-crackdown-what-changed-by-2026 | 2026-07-28 | 2026-11-13 | C | Extract | COI | Apollo page |
| S95 | Employment Projections 2025–35, BLS USDL-26-1422 — https://www.bls.gov/news.release/archives/ecopro_08272026.htm | 2026-08-27 | 2026-11-13 | A | Extract | — | K7, K8 |
| S96 | BLS AI exposure, AI2Work — https://ai2.work/blog/bls-ranks-831-jobs-by-ai-exposure-alongside-its-decade-outlook | 2026-09-05 | 2026-11-13 | C | Extract | — | AI exposure |
| S97 | AI salaries (Levels.fyi pull 2026-08-15), The AI Rankings — https://theairankings.com/ai-jobs/salaries/ | 2026-08-15 | 2026-11-13 | C | Extract | — | K2, K3 |
| S98 | Highest-paying AI jobs, AI Business Weekly — https://aibusinessweekly.net/p/highest-paying-ai-jobs | 2026-10-04 | 2026-11-13 | C | Extract | — | Filed base |
| S99 | What ML engineers make, TechInterview — https://www.techinterview.org/post/3233476387/what-ml-engineers-actually-make/ | 2026 | 2026-11-13 | C | Extract | — | OpenAI vs Amazon |
| S100 | AI compensation guide, Pin — https://www.pin.com/blog/ai-compensation-salary-guide | 2026 | 2026-11-13 | C | Extract | — | Anthropic median |
| S101 | MLE vs SWE salary, Interview Kickstart — https://interviewkickstart.com/blogs/articles/machine-learning-engineer-vs-software-engineer-salary | 2026 | 2026-11-13 | C | Extract | — | MLE base range |
| S102 | India emerges as talent hub for global AI giants, Communications Today (Business Standard item) — https://www.communicationstoday.co.in/?p=378238 | n/d | 2026-11-13 | C | Extract | single-source | Perplexity India roles |
| S103 | Prompt engineer salary guide, Kore1 — https://www.kore1.com/prompt-engineer-salary-guide/ | 2026 | 2026-11-13 | C | Extract | single-source | Anthropic median USD 710,000 (K3) |
| S104 | Anthropic opens India office as revenue doubles, CRN Asia — https://www.crnasia.com/india/news/2026/anthropic-opens-india-office-as-revenue-doubles-enterprise-adoption-of-claude-accelerates | 2026-02 | 2026-11-13 | C | Extract | single-source | India as second-largest market |
| S105 | The USD 100K H-1B fee is blocked, extended and still confusing, Silicon Path Law — https://siliconpathlaw.com/h1b-100k-fee-lawsuit-update-2026 | 2026-10 | 2026-11-13 | C | Extract | single-source | Second court ruling (N.D. Cal., 2026-09-30) |

## Data Appendix

Conventions:
- The record grade is the grade of the headline field (the count, or the ATS or identity where no count exists). Weaker fields are named in `note`.
- In company records, null means not established in this session.
- Board URLs appear only where a source showed the URL.
- Company records follow first, then tool, measure and absence records.

```jsonl
{"type":"company","grade":"A","src":["S27","S28","S30","S31","S32","S33","S98"],"as_of":"2026-11-13","ttl":"V1","name":"Anthropic","employer_type":"frontier-lab","hq":"San Francisco, US","regions":["US","UK","FR","DE","JP","KR","IN"],"genai_open":{"count":682,"date":"2026-11-13","filter":"none: all departments on own Greenhouse board; Applied AI group lists 28 on page 3 of 14"},"ats":"Greenhouse","board_url":"https://job-boards.greenhouse.io/anthropic","sponsorship":"No register lookup run; H-1B filings reported (median filed base about USD 315000 in 2025 filings; C)","remote_policy":"Some roles marked Remote-Friendly (United States); most hub-based","india_presence":"Bengaluru office opened 2026-02-16; hiring sales, partnerships, applied AI","note":"COI: developer of this model. Regions seen in postings on the board page read: UK, FR, DE, JP, KR, US; India from the office announcement. Ireland and Canada recalled only (D). Other readings of this board: 400 (2026-07), 622 (2026-09-25), 603 (2026-10-08), 675 (2026-11-01). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S32","S33","S41","S44","S47","S67","S98"],"as_of":"2026-11-01","ttl":"V1","name":"OpenAI","employer_type":"frontier-lab","hq":"San Francisco, US","regions":["US","IN"],"genai_open":{"count":810,"date":"2026-11-01","filter":"all roles on own careers feed per FourWeekMBA; not GenAI-only"},"ats":"Ashby","board_url":"https://jobs.ashbyhq.com/openai","sponsorship":"H-1B filings reported (median filed base about USD 310000 in 2025 filings; C)","remote_policy":null,"india_presence":"New Delhi office planned from late 2025; sales and strategy roles first (C)","note":"Other readings: 714 (2026-07, TrueUp), 753 (undated, public Ashby endpoint). Other regions not established."}
{"type":"company","grade":"C","src":["S41","S24"],"as_of":"2026-11-13","ttl":"V2","name":"Google DeepMind","employer_type":"frontier-lab","hq":"London, UK","regions":["UK","US"],"genai_open":null,"ats":"Greenhouse","board_url":"https://job-boards.greenhouse.io/deepmind","sponsorship":"Alphabet/Google FY2025 all-title certified LCAs 8161 (B)","remote_policy":null,"india_presence":null,"note":"HQ and regions recalled (D). Board URL from a newsletter that sampled three labs; count not read."}
{"type":"company","grade":"C","src":["S33","S55","S48"],"as_of":"2026-07-01","ttl":"V1","name":"xAI","employer_type":"frontier-lab","hq":"San Francisco Bay Area, US","regions":["US"],"genai_open":{"count":210,"date":"2026-07-01","filter":"company's open jobs per TrueUp Generative AI list; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Reported absorbed into SpaceX, closed 2026-02 (C). ATS unresolved: ResumeAI lists Lever. HQ recalled (D)."}
{"type":"company","grade":"C","src":["S33","S45"],"as_of":"2026-07-01","ttl":"V1","name":"Mistral AI","employer_type":"frontier-lab","hq":"Paris, FR","regions":["FR"],"genai_open":{"count":172,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":"Lever","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Lever slug 'mistral' per an Apify actor example (C); board not opened. HQ recalled (D)."}
{"type":"company","grade":"C","src":["S33","S46","S48"],"as_of":"2026-07-01","ttl":"V1","name":"Cohere","employer_type":"frontier-lab","hq":"Toronto, CA","regions":["CA"],"genai_open":{"count":130,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"ATS conflict: Ashby in an Apify actor list, Lever in ResumeAI State of ATS 2026; probe both public endpoints. HQ recalled (D)."}
{"type":"company","grade":"C","src":["S33","S46","S48","S67","S102"],"as_of":"2026-07-01","ttl":"V2","name":"Perplexity","employer_type":"frontier-lab","hq":"San Francisco, US","regions":["US","IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":"Business development and partnership roles planned (C); office plans reported","note":"Ranked 16th by open jobs in TrueUp Generative AI list; count not captured. ATS conflict: Ashby (slug 'perplexity') vs Lever. HQ recalled (D)."}
{"type":"company","grade":"B","src":["S77","S78"],"as_of":"2026-11-13","ttl":"V2","name":"Sakana AI","employer_type":"frontier-lab","hq":"Tokyo, JP","regions":["JP"],"genai_open":null,"ats":null,"board_url":"https://sakana.ai/careers","sponsorship":"Postings state assistance with visa applications for Tokyo-based hires (posting dated 2026-05-31; B)","remote_policy":"Candidates expected to be physically based in Tokyo (posting text)","india_presence":null,"note":"Open-role count not read; ATS not established."}
{"type":"company","grade":"C","src":["S74","S75"],"as_of":"2026-11-02","ttl":"V1","name":"Sarvam AI","employer_type":"ai-startup","hq":"Bengaluru, IN","regions":["IN"],"genai_open":{"count":46,"date":"2026-11-02","filter":"all roles listed on sarvam.ai/careers per CareerIndia; 37 in Bengaluru"},"ats":"Ashby","board_url":"https://sarvam.ai/careers","sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Headquartered in Bengaluru","note":"Secondary source for count and ATS (C). Funding USD 346M of 399M Indic-AI funding in 2026 per Tracxn (B)."}
{"type":"company","grade":"C","src":["S76"],"as_of":"2026-09-02","ttl":"V2","name":"G42","employer_type":"other","hq":"Abu Dhabi, AE","regions":["AE"],"genai_open":null,"ats":null,"board_url":"https://jobs.g42.ai","sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Applied Scientist posting (Inception42) dated 2026-09-02 seen; volume and ATS not established. UAE visa routes not assessed."}
{"type":"company","grade":"B","src":["S35","S36","S24"],"as_of":"2026-11-11","ttl":"V1","name":"Google","employer_type":"big-tech","hq":"Mountain View, US","regions":["US"],"genai_open":{"lo":451,"hi":632,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels on one page disagree"},"ats":null,"board_url":null,"sponsorship":"FY2025 certified LCAs 8161, all titles (B)","remote_policy":null,"india_presence":null,"note":"Own careers site (D). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S35","S36","S2","S24","S26","S83"],"as_of":"2026-11-11","ttl":"V1","name":"Amazon","employer_type":"big-tech","hq":"Seattle, US","regions":["US"],"genai_open":{"lo":388,"hi":477,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels disagree"},"ats":null,"board_url":null,"sponsorship":"DOL FY2026 YTD to 2026-06-30: 45025 positions certified (A); FY2025 certified LCAs 21585 (B) vs about 15500 (C)","remote_policy":null,"india_presence":null,"note":"Layoffs: 16000 announced January 2026 plus other events (B). Own careers site (D)."}
{"type":"company","grade":"C","src":["S24","S21"],"as_of":"2026-11-13","ttl":"V2","name":"Microsoft","employer_type":"big-tech","hq":"Redmond, US","regions":["US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"FY2025 certified LCAs 8065, all titles (B); AI/ML keyword-set LCAs 1989 across FY2021-FY2026 partial (B)","remote_policy":null,"india_presence":null,"note":"Open-role count not read."}
{"type":"company","grade":"B","src":["S35","S36","S24","S2","S84"],"as_of":"2026-11-11","ttl":"V1","name":"Meta","employer_type":"big-tech","hq":"Menlo Park, US","regions":["US"],"genai_open":{"lo":144,"hi":165,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels disagree"},"ats":null,"board_url":null,"sponsorship":"FY2025 certified LCAs 5824 (B); listed in DOL FY2026 Q3 top-10 by positions (A, count not transcribed)","remote_policy":null,"india_presence":null,"note":"About 10% workforce cut from 2026-05-20 and freeze on 6000 open roles reported 2026-04-24 (B)."}
{"type":"company","grade":"B","src":["S35","S36","S24","S2","S23"],"as_of":"2026-11-11","ttl":"V1","name":"Apple","employer_type":"big-tech","hq":"Cupertino, US","regions":["US"],"genai_open":{"lo":287,"hi":310,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels disagree"},"ats":null,"board_url":null,"sponsorship":"FY2025 certified LCAs 6723 (B); DOL FY2026 Q3 top-10 (A); exact-title ML Engineer LCAs 108 (B, year label uncertain)","remote_policy":null,"india_presence":null,"note":"Own careers site (D)."}
{"type":"company","grade":"B","src":["S35","S36","S34","S25"],"as_of":"2026-11-11","ttl":"V1","name":"NVIDIA","employer_type":"big-tech","hq":"Santa Clara, US","regions":["US"],"genai_open":{"lo":178,"hi":220,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels disagree"},"ats":"Workday","board_url":null,"sponsorship":"980 certified SWE LCAs 2025-10 to 2026-06 (C)","remote_policy":null,"india_presence":null,"note":"Workday recalled (D). TrueUp 2026-07: about 2000 open jobs, all roles."}
{"type":"company","grade":"A","src":["S2"],"as_of":"2026-06-30","ttl":"V4","name":"Cisco","employer_type":"big-tech","hq":"San Jose, US","regions":["US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"DOL FY2026 YTD to 2026-06-30: 15786 positions certified (A)","remote_policy":null,"india_presence":null,"note":"Open-role count not read. HQ recalled (D)."}
{"type":"company","grade":"B","src":["S35","S25","S65","S66"],"as_of":"2026-11-11","ttl":"V1","name":"JPMorgan Chase","employer_type":"enterprise","hq":"New York, US","regions":["US","IN"],"genai_open":{"count":81,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block"},"ats":null,"board_url":null,"sponsorship":"1183 certified SWE LCAs 2025-10 to 2026-06 (C)","remote_policy":null,"india_presence":"India GCC with 60000+ staff; about 1000 technology hires planned (Business Standard 2026-07-23)","note":"Own portal (D)."}
{"type":"company","grade":"B","src":["S2","S66"],"as_of":"2026-06-30","ttl":"V4","name":"Goldman Sachs","employer_type":"enterprise","hq":"New York, US","regions":["US","IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Listed in DOL FY2026 Q3 top-10 by positions certified (A; count not transcribed)","remote_policy":null,"india_presence":"Bengaluru and Hyderabad GCCs; more staff in India than anywhere outside the US per Bloomberg","note":"Open-role count not read. HQ and cities recalled (D)."}
{"type":"company","grade":"B","src":["S35","S36"],"as_of":"2026-11-11","ttl":"V1","name":"Capital One","employer_type":"enterprise","hq":"McLean, US","regions":["US"],"genai_open":{"lo":173,"hi":187,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels disagree"},"ats":"Workday","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Workday recalled (D)."}
{"type":"company","grade":"C","src":["S25"],"as_of":"2026-06-30","ttl":"V1","name":"Walmart","employer_type":"enterprise","hq":"Bentonville, US","regions":["US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"1257 certified SWE LCAs 2025-10 to 2026-06 (C)","remote_policy":null,"india_presence":null,"note":"Walmart Global Tech India not evidenced in this session."}
{"type":"company","grade":"B","src":["S35","S36"],"as_of":"2026-11-11","ttl":"V1","name":"Booz Allen Hamilton","employer_type":"enterprise","hq":"McLean, US","regions":["US"],"genai_open":{"lo":186,"hi":187,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block; two panels"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Federal contractor; citizenship or clearance requirements likely (D)."}
{"type":"company","grade":"B","src":["S35"],"as_of":"2026-11-11","ttl":"V1","name":"General Motors","employer_type":"enterprise","hq":"Detroit, US","regions":["US"],"genai_open":{"count":57,"date":"2026-11-11","filter":"open AI jobs in the US per Chopping Block"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Volume context only."}
{"type":"company","grade":"A","src":["S2"],"as_of":"2026-06-30","ttl":"V4","name":"Qualcomm","employer_type":"enterprise","hq":"San Diego, US","regions":["US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"DOL FY2026 YTD to 2026-06-30: 71203 positions certified (A); unusually large, likely multi-position LCAs","remote_policy":null,"india_presence":null,"note":"Figure transcribed at first read. Open-role count not read."}
{"type":"company","grade":"A","src":["S2"],"as_of":"2026-06-30","ttl":"V4","name":"CGI","employer_type":"it-services","hq":"Montreal, CA","regions":["CA","US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"DOL FY2026 YTD to 2026-06-30: 16996 positions certified (A)","remote_policy":null,"india_presence":null,"note":"HQ recalled (D)."}
{"type":"company","grade":"C","src":["S25"],"as_of":"2026-06-30","ttl":"V1","name":"Deloitte","employer_type":"it-services","hq":"London, UK","regions":["US"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"1682 certified SWE LCAs 2025-10 to 2026-06 (C)","remote_policy":null,"india_presence":null,"note":"Consulting; HQ recalled (D)."}
{"type":"company","grade":"B","src":["S32","S33","S39","S42"],"as_of":"2026-11-01","ttl":"V1","name":"Databricks","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US"],"genai_open":{"lo":734,"hi":904,"date":"2026-11-01","filter":"all roles; FourWeekMBA 904 (2026-11-01), TrueUp 787 (2026-07), Fast AI Jobs 734 (undated)"},"ats":"Greenhouse","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Greenhouse token 'databricks' appears in an Apify actor example (C). HQ recalled (D); other regions not established."}
{"type":"company","grade":"B","src":["S33","S49"],"as_of":"2026-07-01","ttl":"V1","name":"Harvey","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US"],"genai_open":{"count":333,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":"Ashby","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Ashby per the vendor's own customer list (COI). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S33","S46","S47"],"as_of":"2026-07-01","ttl":"V1","name":"ElevenLabs","employer_type":"ai-startup","hq":null,"regions":[],"genai_open":{"count":171,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":"Ashby","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Ashby slug 'elevenlabs' in Apify actor list and JobsPipe July 2026 check (C). HQ and regions not established."}
{"type":"company","grade":"B","src":["S33","S49"],"as_of":"2026-07-01","ttl":"V1","name":"Sierra","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US"],"genai_open":{"count":158,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":"Ashby","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Ashby per the vendor's own customer list (COI). HQ recalled (D); other regions not established."}
{"type":"company","grade":"B","src":["S33"],"as_of":"2026-07-01","ttl":"V1","name":"Glean","employer_type":"ai-startup","hq":"Palo Alto, US","regions":["US"],"genai_open":{"count":131,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"HQ recalled (D); ATS not established."}
{"type":"company","grade":"B","src":["S33","S47","S48"],"as_of":"2026-07-01","ttl":"V1","name":"Cursor (Anysphere)","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US"],"genai_open":{"count":113,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"ATS conflict: Ashby (JobsPipe July 2026) vs Lever (ResumeAI). Absent from the visible part of TrueUp Generative AI 50."}
{"type":"company","grade":"B","src":["S33","S36","S39"],"as_of":"2026-10-28","ttl":"V1","name":"Anduril","employer_type":"ai-startup","hq":"Costa Mesa, US","regions":["US"],"genai_open":{"lo":522,"hi":2165,"date":"2026-10-28","filter":"522 AI jobs (Chopping Block, about 2026-10-20 to 10-28); 961 all roles (Fast AI Jobs, undated); 2165 all roles (TrueUp, 2026-07)"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Defence AI; citizenship likely required (D). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S33"],"as_of":"2026-07-01","ttl":"V1","name":"Prolific","employer_type":"ai-startup","hq":"London, UK","regions":["UK"],"genai_open":{"count":174,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"HQ recalled (D); ATS not established."}
{"type":"company","grade":"B","src":["S33","S46"],"as_of":"2026-07-01","ttl":"V1","name":"LangChain","employer_type":"ai-startup","hq":"San Francisco, US","regions":["US"],"genai_open":{"count":97,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":"Ashby","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Ashby slug 'langchain' in an Apify actor list (C). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S33"],"as_of":"2026-07-01","ttl":"V1","name":"Etched","employer_type":"ai-startup","hq":"Cupertino, US","regions":["US"],"genai_open":{"count":99,"date":"2026-07-01","filter":"all open jobs per TrueUp; month-level date"},"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"AI chip company; HQ recalled (D)."}
{"type":"company","grade":"C","src":["S43"],"as_of":"2026-11-02","ttl":"V2","name":"Hugging Face","employer_type":"ai-startup","hq":"New York, US","regions":["US","FR"],"genai_open":null,"ats":"Workable","board_url":"https://apply.workable.com/huggingface","sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Board URL seen in an Apify actor example; count not read. HQ and regions recalled (D)."}
{"type":"company","grade":"C","src":["S44","S47"],"as_of":"2026-11-13","ttl":"V2","name":"Palantir","employer_type":"other","hq":"Denver, US","regions":["US"],"genai_open":null,"ats":"Lever","board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Lever slug 'palantir' (302 jobs in an undated DEV snapshot); count not dated. HQ recalled (D)."}
{"type":"company","grade":"C","src":["S79"],"as_of":"2026-07-28","ttl":"V2","name":"Grab","employer_type":"other","hq":"Singapore, SG","regions":["SG"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":null,"note":"Named among employers of AI engineers in Singapore (2026-07-28). No count."}
{"type":"company","grade":"B","src":["S69","S70","S71","S72"],"as_of":"2026-09-30","ttl":"V1","name":"TCS","employer_type":"it-services","hq":"Mumbai, IN","regions":["IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Headcount 598056 at 2026-09-30 (+4258 in Q2 FY27); AI revenue above USD 3 billion annualised; FY27 opened with 25000 fresher offers","note":"GenAI role counts not published. Global delivery recalled (D)."}
{"type":"company","grade":"B","src":["S69","S71"],"as_of":"2026-09-30","ttl":"V1","name":"Infosys","employer_type":"it-services","hq":"Bengaluru, IN","regions":["IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Net +4480 in Q2 FY27; AI 8.2% of revenue (Q1 FY27)","note":"GenAI role counts not published."}
{"type":"company","grade":"B","src":["S68","S69"],"as_of":"2026-09-30","ttl":"V1","name":"HCLTech","employer_type":"it-services","hq":"Noida, IN","regions":["IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Headcount 230339 at 2026-09-30 (+6450); 6136 freshers in Q2 FY27","note":"GenAI role counts not published. HQ recalled (D)."}
{"type":"company","grade":"B","src":["S69"],"as_of":"2026-09-30","ttl":"V1","name":"Wipro","employer_type":"it-services","hq":"Bengaluru, IN","regions":["IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Net headcount -6716 in Q2 FY27","note":"Only one of five large Indian IT firms to shrink in the quarter."}
{"type":"company","grade":"B","src":["S69"],"as_of":"2026-09-30","ttl":"V1","name":"Tech Mahindra","employer_type":"it-services","hq":"Pune, IN","regions":["IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":"Not applicable to India-based roles","remote_policy":null,"india_presence":"Net +5446 in Q2 FY27","note":"HQ recalled (D)."}
{"type":"company","grade":"C","src":["S73","S81"],"as_of":"2026-05-08","ttl":"V1","name":"Cognizant","employer_type":"it-services","hq":"Teaneck, US","regions":["US","IN"],"genai_open":null,"ats":null,"board_url":null,"sponsorship":null,"remote_policy":null,"india_presence":"Plan to cut 12000-15000 jobs reported 2026-05-08 (C); Indian staff most affected (C)","note":"Also a named US Tech Force partner (2026-06-09). HQ recalled (D)."}
{"type":"company","grade":"B","src":["S80","S81"],"as_of":"2026-06-09","ttl":"V2","name":"US Tech Force (OPM)","employer_type":"public-sector","hq":"Washington DC, US","regions":["US"],"genai_open":{"count":1000,"date":"2026-03-05","filter":"planned places in the first cohort of early-career engineers, data scientists, AI specialists; two-year terms"},"ats":null,"board_url":null,"sponsorship":"Federal civil roles generally require US citizenship (D)","remote_policy":null,"india_presence":null,"note":"Partners include Scale AI, Cisco, Cognition, Cognizant and Wiz (S81). Application portal not opened."}
```


```jsonl
{"type":"tool","grade":"A","src":["S1","S2"],"as_of":"2026-11-13","ttl":"V2","id":"dol-oflc-lca","name":"DOL OFLC LCA disclosure data","stage":1,"category":"sponsor-register","what":"Employer-filed Labor Condition Applications by quarter; Selected Statistics PDF","verdict":"use","why":"Official, free, employer-level, with job titles and offered wages; filings only","url":"https://www.dol.gov/agencies/eta/foreign-labor/performance","price":"free","note":"FY2025 is the last complete year; FY2026 to 2026-06-30 published. Disclosure tables are script-rendered."}
{"type":"tool","grade":"C","src":["S12","S13","S14"],"as_of":"2026-11-13","ttl":"V2","id":"uscis-h1b-employer-data-hub","name":"USCIS H-1B Employer Data Hub","stage":1,"category":"sponsor-register","what":"Employer-level H-1B petition decisions by fiscal year","verdict":"use-with-care","why":"Official, but an outage and missing data were reported in March 2026 and my fetch was bot-blocked","url":"https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub","price":"free","risk":"availability and completeness"}
{"type":"tool","grade":"A","src":["S3"],"as_of":"2026-11-10","ttl":"V2","id":"uk-register-licensed-sponsors-workers","name":"UK Register of Licensed Sponsors: Workers","stage":1,"category":"sponsor-register","what":"CSV of licensed sponsors with route and rating","verdict":"use","why":"Official, free, updated on most working days; licence is not a vacancy","url":"https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers","price":"free","note":"About 10.4 MB; page updated 2026-11-10."}
{"type":"tool","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V2","id":"ind-public-register-recognised-sponsors","name":"IND Public Register of Recognised Sponsors","stage":1,"category":"sponsor-register","what":"Recognised sponsors in the Netherlands by category","verdict":"use","why":"Official, free, monthly per IND snippet","url":"https://ind.nl/en/public-register-recognised-sponsors","price":"free"}
{"type":"tool","grade":"A","src":["S5","S6"],"as_of":"2026-11-13","ttl":"V2","id":"canada-positive-lmia-list","name":"Canada Positive LMIA Employers List","stage":1,"category":"sponsor-register","what":"Employers with positive LMIAs","verdict":"use-with-care","why":"Official and quarterly, but an LMIA is not a job offer; Global Talent Stream partners trimmed in September 2026","url":"https://open.canada.ca/data/en/dataset/90fed587-1364-4f33-a9ee-208181dc0b97","price":"free"}
{"type":"tool","grade":"A","src":["S7","S8"],"as_of":"2026-11-13","ttl":"V2","id":"denmark-siri-certified-companies","name":"SIRI Certified companies (Fast-track)","stage":1,"category":"sponsor-register","what":"Names and CVR numbers of certified companies; 982 reported","verdict":"use","why":"Official public list for the Danish Fast-track scheme","url":"https://www.nyidanmark.dk/en-GB/Words-and-concepts/SIRI/Certified-companies","price":"free"}
{"type":"tool","grade":"C","src":["S10"],"as_of":"2024-01-31","ttl":"V4","id":"australia-accredited-sponsors-foi","name":"Australia accredited sponsors FOI list","stage":1,"category":"sponsor-register","what":"Accredited Standard Business Sponsors as at January 2024","verdict":"watch","why":"Point-in-time release, not a live register","url":"https://yen.com.gh/world/315411-australia-publishes-list-1000-approved-sponsors-foreign-workers/","price":"free"}
{"type":"tool","grade":"B","src":["S42","S43"],"as_of":"2026-11-02","ttl":"V2","id":"greenhouse-job-board-api","name":"Greenhouse Job Board API","stage":1,"category":"ats-public-api","what":"Public unauthenticated GET endpoint for a company's open jobs","verdict":"use","why":"Documented for public use; employer owns the content; link back to the posting","url":"https://developers.greenhouse.io/job-board.html","price":"free","note":"URL as named in third-party documentation; vendor page not opened."}
{"type":"tool","grade":"C","src":["S42","S43"],"as_of":"2026-11-02","ttl":"V2","id":"lever-postings-api","name":"Lever Postings API","stage":1,"category":"ats-public-api","what":"Public postings feed; EU instance exists","verdict":"use","why":"Documented in the vendor repository; README permits third-party scraping per a secondary summary","url":"https://github.com/lever/postings-api","price":"free","note":"Vendor README not opened."}
{"type":"tool","grade":"C","src":["S42","S43"],"as_of":"2026-11-02","ttl":"V2","id":"ashby-public-job-posting-api","name":"Ashby public Job Posting API","stage":1,"category":"ats-public-api","what":"Public job-board feed with optional compensation","verdict":"use-with-care","why":"Documented, but one tool author recorded a 401 on the API host's robots.txt on 2026-11-02; ToS not opened","url":"https://developers.ashbyhq.com/docs/public-job-posting-api","price":"free"}
{"type":"tool","grade":"C","src":["S43"],"as_of":"2026-11-02","ttl":"V2","id":"workable-widget-api","name":"Workable account widget feed","stage":1,"category":"ats-public-api","what":"Public jobs feed per account","verdict":"use-with-care","why":"Appears in tool documentation; vendor terms not opened","url":"https://apply.workable.com/huggingface","price":"free"}
{"type":"tool","grade":"C","src":["S86","S87"],"as_of":"2026-11-09","ttl":"V2","id":"crunchbase","name":"Crunchbase","stage":1,"category":"company-funding-database","what":"Company, funding and people data","verdict":"use-with-care","why":"Pro suits lookups; API and bulk by quote; Basic API retired; scraping reportedly barred by ToS","url":"https://www.crunchbase.com","price":"Pro USD 49/month on annual billing in year one, USD 79 list, USD 99 monthly; Business from USD 199/month; API by quote, reported to start around USD 50000/year","risk":"contract breach if scraped","note":"ToS not opened."}
{"type":"tool","grade":"A","src":["S88","S89"],"as_of":"2026-10-31","ttl":"V2","id":"dealroom","name":"Dealroom","stage":1,"category":"company-funding-database","what":"EU-strong startup and investor data","verdict":"use-with-care","why":"Paid annual plans; API needs a separate licence; personal data must be deleted when the licence ends","url":"https://dealroom.co","price":"Premium about EUR 12500 per year","risk":"personal-data duties","note":"Self-published terms and pricing (COI-neutral for a third-party vendor)."}
{"type":"tool","grade":"D","src":["S75"],"as_of":"2026-10-28","ttl":"V2","id":"tracxn","name":"Tracxn","stage":1,"category":"company-funding-database","what":"Startup and funding data; its reports are the source of Indian press funding figures (S75)","verdict":"watch","why":"Pricing and terms were not retrieved in this session; a free tier and sales-quoted plans are recalled only (D)","url":"https://tracxn.com","price":null,"note":"Price null: not established."}
{"type":"tool","grade":"C","src":["S90"],"as_of":"2026-10-31","ttl":"V2","id":"pitchbook","name":"PitchBook","stage":1,"category":"company-funding-database","what":"Private-market deal data","verdict":"watch","why":"Priced for institutions; typical contract about USD 31750 a year (reported)","url":"https://pitchbook.com","price":"Quote; deals from USD 20000 to 122500 a year (reported)"}
{"type":"tool","grade":"B","src":["S33","S34"],"as_of":"2026-07-01","ttl":"V2","id":"trueup","name":"TrueUp","stage":1,"category":"job-aggregator","what":"Company and job trackers, including a Generative AI 50 and open-job rankings","verdict":"use-with-care","why":"Useful for discovery; method not stated; ToS not read","url":"https://trueup.io","price":"free"}
{"type":"tool","grade":"B","src":["S37","S38","S39"],"as_of":"2026-08-03","ttl":"V2","id":"fast-ai-jobs","name":"Fast AI Jobs","stage":1,"category":"job-aggregator","what":"AI-startup postings; 28414 at 1824 startups on 2026-08-03","verdict":"use-with-care","why":"Discovery aid; verify on the employer board","url":"https://www.fastaijobs.com","price":"free"}
{"type":"tool","grade":"B","src":["S35","S36"],"as_of":"2026-11-11","ttl":"V2","id":"chopping-block","name":"AI Chopping Block","stage":1,"category":"job-aggregator","what":"AI job counts by company and role, with pay","verdict":"use-with-care","why":"Definition drift: AI-job total fell from 37286 to 7555 between snapshots","url":"https://www.choppingblock.ai","price":"free"}
{"type":"tool","grade":"B","src":["S32"],"as_of":"2026-11-01","ttl":"V2","id":"fourweekmba-ai-company-index","name":"FourWeekMBA AI Company Index","stage":1,"category":"job-aggregator","what":"Open roles across 155 AI companies, rebuilt weekly","verdict":"use-with-care","why":"All roles, not GenAI-only","url":"https://fourweekmba.com/ai-company-index/","price":"free"}
{"type":"tool","grade":"B","src":["S40"],"as_of":"2026-10-27","ttl":"V2","id":"startup-jobs-statistics","name":"Startup Jobs hiring statistics","stage":1,"category":"job-aggregator","what":"273773 live startup openings; AI/ML 1.6% of postings","verdict":"use-with-care","why":"Vendor method; invites citation with attribution","url":"https://startup.jobs/startup-hiring-statistics","price":"free"}
{"type":"tool","grade":"C","src":["S82","S83"],"as_of":"2026-11-01","ttl":"V1","id":"layoffs-fyi","name":"Layoffs.fyi","stage":1,"category":"layoffs-tracker","what":"Tech layoff tracker: 135446 in 2026 at 334 companies per a November 2026 report","verdict":"use-with-care","why":"Third-party tracker; AI-attribution shares conflict across sources","url":"https://layoffs.fyi","price":"free"}
{"type":"tool","grade":"B","src":["S50","S51","S52"],"as_of":"2026-11-13","ttl":"V2","id":"huntr-research","name":"Huntr Job Search Trends reports","stage":1,"category":"labour-market-data","what":"Self-tracked applicant data; Q3 2026: 152742 jobs saved, 84753 applications, 4796 users with logged applications","verdict":"use-with-care","why":"Vendor-run, self-tracked, correlational; medians restated between reports","url":"https://huntr.co/research/job-search-trends-q3-2026","price":"free"}
{"type":"tool","grade":"A","src":["S95"],"as_of":"2026-08-27","ttl":"V4","id":"bls-employment-projections-ooh","name":"BLS Employment Projections and Occupational Outlook Handbook","stage":1,"category":"labour-market-data","what":"2025-35 projections released 2026-08-27 (USDL-26-1422); the OOH features them; includes AI exposure categories","verdict":"use","why":"Official and free; data scientists +34.6% and computer and information research scientists +21.8% for 2025-35","url":"https://www.bls.gov/emp","price":"free","note":"K7: the knowledge base's 2024-34 reference is superseded. AI exposure categories for 831 occupations per a secondary summary (C, S96)."}
{"type":"tool","grade":"D","src":["S95"],"as_of":"2026-11-13","ttl":"V2","id":"onet-online","name":"O*NET OnLine and My Next Move","stage":1,"category":"labour-market-data","what":"Occupation descriptors and skills; projections drawn from BLS and state data","verdict":"use","why":"Official and free (recalled); not opened in this session","url":"https://www.onetonline.org","price":"free","note":"K8: no O*NET page evidence newer than 2026-10-21. BLS released 2025-35 projections on 2026-08-27, so a 2024-34 citation is likely behind. URL recalled (D)."}
{"type":"tool","grade":"B","src":["S91","S92","S93"],"as_of":"2026-09-16","ttl":"V2","id":"linkedin-derived-scrapers","name":"LinkedIn-derived scraping and enrichment (fake-account APIs, browser extensions)","stage":1,"category":"contact-data","what":"Profile and contact data collected from LinkedIn at scale","verdict":"avoid","why":"LinkedIn enforces by contract: Proxycurl shut in July 2025; a consent judgment against ProAPIs and Netswift on 2026-09-16 bars scraping and selling LinkedIn data; CNIL fined KASPR EUR 240000","url":"https://digitalpolicyalert.org/event/43954-us-district-court-issued-final-judgment-in-linkedin-v-proapis-data-scraping-lawsuit","risk":"contract, GDPR and injunction exposure","note":"Applies to harvesting personal data of individuals."}
{"type":"tool","grade":"C","src":["S91","S94"],"as_of":"2026-07-28","ttl":"V2","id":"contact-data-products","name":"Contact-data products (Apollo, RocketReach, Hunter, ZoomInfo, Lusha)","stage":1,"category":"contact-data","what":"B2B contact databases and enrichment","verdict":"watch","why":"Belongs to the outreach session. For a target list use company-level data only. LinkedIn removed Apollo and Seamless company pages in March 2025 and Apollo's page was back by 2026-07-28; no enforcement against these vendors found beyond KASPR","url":"https://www.leadgenius.com/resources/linkedins-b2b-data-crackdown-what-changed-by-2026","risk":"personal-data and platform-terms exposure","note":"Vendor terms, accuracy and complaints not assessed here."}
{"type":"tool","grade":"C","src":["S53","S54","S55"],"as_of":"2026-04-16","ttl":"V3","id":"forbes-ai-50","name":"Forbes AI 50","stage":1,"category":"curated-list","what":"Unranked list of 50 private AI companies with Sequoia and Meritech, plus a 20-company Brink List","verdict":"use-with-care","why":"Private companies only; USD 305.6 billion raised, about 80% by OpenAI and Anthropic; no hiring-volume validation","url":"https://superscout.co/rankings/forbes-ai-50","price":"free","note":"Publisher page not opened; descriptions are secondary."}
{"type":"tool","grade":"B","src":["S56","S57"],"as_of":"2026-05-13","ttl":"V3","id":"cb-insights-ai-100","name":"CB Insights AI 100","stage":1,"category":"curated-list","what":"Annual list of 100 private AI companies selected from more than 40000","verdict":"use-with-care","why":"Inputs include hiring momentum, deal activity, investors, Mosaic and Commercial Maturity scores; the 64% follow-on claim is a vendor claim (COI)","url":"https://www.businesswire.com/news/home/20260513962615/en/","price":"free list and report; platform paid","note":"Overlap with hiring volume not computed."}
{"type":"tool","grade":"C","src":["S58"],"as_of":"2026-09-10","ttl":"V3","id":"yc-directory","name":"Y Combinator company directory and batches","stage":1,"category":"curated-list","what":"Public directory by batch; S26 batch about 235 companies, the largest","verdict":"use","why":"Official public directory; strong for early-stage AI discovery","url":"https://www.ycombinator.com/companies","price":"free","note":"URL recalled (D); batch size from a secondary report (C). Directory terms not read."}
{"type":"tool","grade":"B","src":["S59","S61","S62"],"as_of":"2026-03-31","ttl":"V3","id":"nasscom-zinnov-gcc-reports","name":"NASSCOM-Zinnov and Dell-Zinnov GCC reports","stage":1,"category":"curated-list","what":"India GCC counts, headcount and AI maturity","verdict":"use-with-care","why":"NASSCOM-Zinnov: 2117 GCCs, 2.36 million staff, USD 98.4 billion FY26. Dell-Zinnov is vendor-sponsored; Infosys's index frames impact differently","url":"https://yourstory.com/enterprise-story/2026/05/gccs-number-touch-2117-in-india-revenue-just-short-of-100-billion","price":"free summaries","note":"Full reports and methods not opened; press coverage only."}
```


```jsonl
{"type":"measure","grade":"A","src":["S27"],"as_of":"2026-11-13","ttl":"V1","subject":"Anthropic","measure":"open roles on own Greenhouse board","unit":"roles","value":682,"method":"board header count; all departments; 14 pages","region":"global","note":"COI. Applied AI group lists 28 roles on page 3."}
{"type":"measure","grade":"C","src":["S30","S31","S32","S33"],"as_of":"2026-11-01","ttl":"V1","subject":"Anthropic","measure":"open roles, third-party readings 2026-07 to 2026-11-01","unit":"roles","lo":400,"hi":675,"method":"readings 400 (2026-07), 622 (2026-09-25), 603 (2026-10-08), 675 (2026-11-01)","region":"global","note":"All roles; sources differ in method."}
{"type":"measure","grade":"B","src":["S32"],"as_of":"2026-11-01","ttl":"V1","subject":"OpenAI","measure":"open roles, all functions","unit":"roles","value":810,"method":"FourWeekMBA AI Company Index","region":"global","note":"Other readings: 714 (2026-07), 753 (undated)."}
{"type":"measure","grade":"B","src":["S32","S33","S39"],"as_of":"2026-11-01","ttl":"V1","subject":"Databricks","measure":"open roles, all functions","unit":"roles","lo":734,"hi":904,"method":"Fast AI Jobs 734 (undated), TrueUp 787 (2026-07), FourWeekMBA 904 (2026-11-01)","region":"global"}
{"type":"measure","grade":"B","src":["S32"],"as_of":"2026-11-01","ttl":"V1","subject":"AI Company Index (FourWeekMBA)","measure":"open roles across tracked AI companies (at least)","unit":"roles","value":16160,"n":155,"method":"155 companies; top 25 hold at least 12153","region":"global","note":"All roles, not GenAI-only."}
{"type":"measure","grade":"B","src":["S36"],"as_of":"2026-10-20","ttl":"V1","subject":"Chopping Block AI-job tracker","measure":"AI jobs of all jobs tracked","unit":"jobs","value":37286,"n":109767,"method":"vendor definition at about 2026-10-20 to 10-28","region":"global","note":"Snippets showed 37286 to 38034 across two dates."}
{"type":"measure","grade":"B","src":["S35"],"as_of":"2026-11-11","ttl":"V1","subject":"Chopping Block AI-job tracker","measure":"AI jobs of all jobs tracked","unit":"jobs","value":7555,"n":70864,"method":"vendor definition on page dated 2026-11-11","region":"global","note":"About 80% below the earlier reading; definition or coverage changed."}
{"type":"measure","grade":"B","src":["S38"],"as_of":"2026-08-03","ttl":"V1","subject":"Fast AI Jobs","measure":"open postings at tracked AI startups","unit":"postings","value":28414,"n":1824,"method":"vendor count; n is startups","region":"global"}
{"type":"measure","grade":"B","src":["S37"],"as_of":"2026-07-30","ttl":"V1","subject":"Fast AI Jobs","measure":"AI Engineer postings","unit":"postings","value":275,"n":170,"method":"page snapshot; n is startups; date inferred from newest posting shown","region":"global","note":"Test of K5 (326 at 183 on 2026-10-19): unverifiable."}
{"type":"measure","grade":"B","src":["S40"],"as_of":"2026-10-27","ttl":"V1","subject":"Established startups","measure":"AI/ML share of postings","unit":"percent","value":1.6,"method":"startup.jobs statistics; postings down 9.7% year on year; 273773 live openings","region":"global"}
{"type":"measure","grade":"C","src":["S82"],"as_of":"2026-11-01","ttl":"V1","subject":"Layoffs.fyi","measure":"tech employees laid off in 2026 to date","unit":"employees","value":135446,"n":334,"method":"tracker total quoted in a November 2026 report; n is companies; day not stated","region":"global","note":"128536 at 299 companies on 2026-09-10 (S83)."}
{"type":"measure","grade":"C","src":["S82"],"as_of":"2025-12-31","ttl":"V6","subject":"Layoffs.fyi","measure":"tech employees laid off in 2025","unit":"employees","value":122606,"n":278,"method":"tracker total; n is companies","region":"global"}
{"type":"measure","grade":"B","src":["S20","S22"],"as_of":"2025-09-30","ttl":"V4","subject":"US LCAs, exact title Machine Learning Engineer","measure":"LCAs filed in FY2025","unit":"LCAs","lo":1053,"hi":1071,"method":"VisaPulse 1053 filed (1040 certified); H1BGrader 1071 entries","region":"US","note":"Title filter undercounts AI/ML roles filed under other titles."}
{"type":"measure","grade":"C","src":["S24","S26"],"as_of":"2025-09-30","ttl":"V4","subject":"Amazon","measure":"certified LCAs in FY2025, all titles","unit":"LCAs","lo":15500,"hi":21585,"method":"H1BVisaJobs 21585; F1Jobs about 15500","region":"US","note":"Differences arise from entity merging and positions versus LCAs."}
{"type":"measure","grade":"A","src":["S2"],"as_of":"2026-06-30","ttl":"V4","subject":"Amazon","measure":"positions certified, FY2026 to 2026-06-30","unit":"positions","value":45025,"method":"DOL LCA Selected Statistics; unique FEIN","region":"US","note":"Transcribed at first read; PDF not re-opened. Positions, not workers."}
{"type":"measure","grade":"B","src":["S62"],"as_of":"2026-03-31","ttl":"V3","subject":"India GCCs","measure":"number of centres, FY26","unit":"centres","value":2117,"method":"NASSCOM-Zinnov; 2.36 million staff; USD 98.4 billion revenue","region":"IN"}
{"type":"measure","grade":"C","src":["S63"],"as_of":"2026-07-01","ttl":"V3","subject":"India GCCs","measure":"projected hires in 2026","unit":"jobs","value":510452,"method":"recruiter-index projection quoted by Business Today","region":"IN","note":"City shares: Bengaluru 30%, Hyderabad 15%, Pune 12%, Mumbai 11%, Chennai 9%, NCR 8%."}
{"type":"measure","grade":"C","src":["S64"],"as_of":"2026-09-30","ttl":"V3","subject":"India GCC tech hiring demand, Q2 FY27","measure":"share from AI, data and cybersecurity","unit":"percent","value":30.3,"method":"Business Standard report of a recruiter index","region":"IN","note":"Bengaluru 22.6% of demand in the same report."}
{"type":"measure","grade":"B","src":["S59","S60"],"as_of":"2026-09-25","ttl":"V3","subject":"India GCCs","measure":"share stuck at AI pilot stage (nearly)","unit":"percent","value":70,"method":"Dell-Zinnov report at Dell Technologies Forum 2026; method not seen","region":"IN","note":"COI: sponsor is a vendor. Infosys index: 27% report meaningful business impact (S61)."}
{"type":"measure","grade":"C","src":["S69"],"as_of":"2026-09-30","ttl":"V1","subject":"TCS, Infosys, HCLTech, Wipro, Tech Mahindra","measure":"net headcount change in Q2 FY27","unit":"employees","value":13918,"method":"sum reported by Moneycontrol via Free Press Journal","region":"IN","note":"HCLTech +6450, Tech Mahindra +5446, Infosys +4480, TCS +4258, Wipro -6716."}
{"type":"measure","grade":"B","src":["S70"],"as_of":"2026-09-30","ttl":"V3","subject":"TCS","measure":"annualised AI revenue (reported as crossing)","unit":"USD billion","value":3,"method":"company-reported","region":"IN","note":"COI: company self-report. Headcount 598056."}
{"type":"measure","grade":"C","src":["S71"],"as_of":"2026-06-30","ttl":"V3","subject":"Infosys","measure":"AI-related share of revenue, Q1 FY27","unit":"percent","value":8.2,"method":"company-reported, quoted in a broker preview","region":"IN","note":"COI: company self-report."}
{"type":"measure","grade":"B","src":["S50"],"as_of":"2026-09-30","ttl":"V3","subject":"Huntr users","measure":"median days from search start to first offer, Q3 2026","unit":"days","value":102,"method":"self-tracked; users with a logged first offer","region":"global","note":"The Q2 report gave 82 days for Q2; the Q3 report restates Q2 at 91."}
{"type":"measure","grade":"B","src":["S50"],"as_of":"2026-09-30","ttl":"V3","subject":"Greenhouse","measure":"share of Huntr users' applications through ATS pages, Q3 2026","unit":"percent","value":21.8,"method":"self-tracked; a year earlier 27.4%","region":"global"}
{"type":"measure","grade":"B","src":["S50"],"as_of":"2026-09-30","ttl":"V3","subject":"Workday","measure":"share of Huntr users' applications through ATS pages, Q3 2026","unit":"percent","value":19.9,"method":"self-tracked","region":"global"}
{"type":"measure","grade":"B","src":["S50"],"as_of":"2026-09-30","ttl":"V3","subject":"Ashby","measure":"share of Huntr users' applications through ATS pages, Q3 2026","unit":"percent","value":19.1,"method":"self-tracked; a year earlier 14.1%","region":"global"}
{"type":"measure","grade":"B","src":["S50"],"as_of":"2026-09-30","ttl":"V3","subject":"Lever","measure":"share of Huntr users' applications through ATS pages, Q3 2026","unit":"percent","value":5.3,"method":"self-tracked; a year earlier 10.6%","region":"global"}
{"type":"measure","grade":"C","src":["S54"],"as_of":"2026-04-16","ttl":"V3","subject":"Forbes AI 50 (2026)","measure":"total venture funding raised by the 50 honorees","unit":"USD billion","value":305.6,"method":"Forbes figure as reported by MarketScale","region":"global","note":"OpenAI and Anthropic account for 242.6, about 80%."}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-05-13","ttl":"V3","subject":"CB Insights AI 100 (2026)","measure":"companies screened (more than)","unit":"companies","value":40000,"method":"vendor statement in press boilerplate","region":"global","note":"COI: vendor's own list."}
{"type":"measure","grade":"A","src":["S95"],"as_of":"2026-08-27","ttl":"V4","subject":"Data scientists (US)","measure":"projected employment change 2025-35","unit":"percent","value":34.6,"method":"BLS Employment Projections","region":"US","note":"Computer and information research scientists +21.8%."}
{"type":"measure","grade":"M","src":["S97"],"as_of":"2026-08-15","ttl":"V3","subject":"US AI Engineer title vs ML Engineer title","measure":"median total compensation ratio","unit":"ratio","value":0.57,"method":"159430 / 278000 from a Levels.fyi-based pull dated 2026-08-15","region":"US","note":"Knowledge base claimed 0.55-0.56. Self-reported data; employer-mix share not tested."}
{"type":"measure","grade":"M","src":["S97","S99"],"as_of":"2026-08-15","ttl":"V3","subject":"OpenAI vs US ML Engineer median","measure":"total compensation ratio","unit":"ratio","lo":2.9,"hi":3.0,"method":"795000-800000 over 265000-278000","region":"US","note":"Self-reported Levels.fyi-derived figures from secondary pages."}
{"type":"measure","grade":"M","src":["S97","S99","S100","S103"],"as_of":"2026-08-15","ttl":"V3","subject":"Anthropic vs US ML Engineer median","measure":"total compensation ratio","unit":"ratio","lo":2.2,"hi":2.7,"method":"600000-710000 over 265000-278000","region":"US","note":"Software engineer medians used for Anthropic."}
{"type":"measure","grade":"C","src":["S98"],"as_of":"2025-12-31","ttl":"V3","subject":"OpenAI and Anthropic","measure":"median base pay in 2025 H-1B filings","unit":"USD per year","lo":310000,"hi":315000,"method":"JobsByCulture compilation quoted by AI Business Weekly; OpenAI about 310000, Anthropic about 315000; excludes equity","region":"US","note":"H-1B filers only; survivor bias."}
{"type":"measure","grade":"M","src":["S33"],"as_of":"2026-07-01","ttl":"V3","subject":"TrueUp top-15 hirers vs TrueUp Generative AI 50","measure":"top-15 hirers present in the visible A-R part of the 50","unit":"companies","value":10,"n":15,"method":"name matching on snippets; xAI and Sierra unknown (beyond R); Prolific, Cursor and LangChain absent","region":"global","note":"Same publisher, so not independent."}
{"type":"measure","grade":"C","src":["S8"],"as_of":"2026-11-13","ttl":"V2","subject":"Denmark SIRI Fast-track list","measure":"certified companies","unit":"companies","value":982,"method":"news report of the official list; list date not shown","region":"DK"}
{"type":"measure","grade":"A","src":["S91"],"as_of":"2024-12-05","ttl":"V6","subject":"KASPR (CNIL decision)","measure":"administrative fine","unit":"EUR","value":240000,"method":"EDPB summary of the CNIL decision; database about 160 million contacts","region":"FR"}
{"type":"measure","grade":"B","src":["S16","S17","S18","S19","S105"],"as_of":"2026-11-13","ttl":"V0","subject":"USD 100,000 H-1B payment (Proclamation 10973, extended to 2027-09-21)","measure":"collected by USCIS (1 yes, 0 no)","unit":"flag","value":0,"method":"law-firm and press summaries; D. Mass. vacatur 2026-06-08; First Circuit stay denied 2026-07-24; second court ruling 2026-09-30","region":"US","note":"Appeals pending; check USCIS before acting."}
{"type":"measure","grade":"B","src":["S65","S66"],"as_of":"2026-10-08","ttl":"V3","subject":"JPMorgan Chase India","measure":"employees in India (more than)","unit":"employees","value":60000,"method":"Bloomberg via Business Standard; about 1000 technology hires planned (2026-07-23)","region":"IN"}
```


```jsonl
{"type":"absence","grade":"E","src":["S20","S21","S22","S23","S24"],"as_of":"2026-11-13","item":"Employer ranking by AI/ML-title LCAs from the raw DOL FY2025 files","searched":"Sandbox DNS failed for dol.gov; web search returned aggregator tables only","note":"Run the reproducible filter in Detailed Findings section 3 on the DOL file."}
{"type":"absence","grade":"E","src":["S12","S13","S14"],"as_of":"2026-11-13","item":"USCIS Employer Data Hub employer-level data","searched":"Fetch of the USCIS page was bot-blocked; outage reports read instead"}
{"type":"absence","grade":"E","src":["S3","S4"],"as_of":"2026-11-13","item":"UK and NL register lookups for the 46 census employers","searched":"Register pages read; the 10.4 MB UK CSV and the IND register were not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Public sponsor registers in Germany, Japan, Singapore, Gulf states, Switzerland, Israel","searched":"One combined search covering Ireland, Denmark, Australia, Canada, New Zealand; the others were not searched individually. Ireland: no public list found (secondary)"}
{"type":"absence","grade":"E","src":["S27"],"as_of":"2026-11-13","item":"Own-site open-role counts for 45 of 46 employers","searched":"Anthropic's Greenhouse board opened; other boards need a search-result URL before a fetch, and custom sites were not reached"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"GenAI-only open-role counts (title and department filter)","searched":"Aggregator pages and the one board opened; only all-role totals and vendor AI-job definitions found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Employer-level evidence for Korea, Israel, Australia, Switzerland, EU labs (Aleph Alpha, DeepL, Black Forest Labs, Helsing) and Gulf (HUMAIN, MBZUAI)","searched":"Combined searches on Gulf, Japan, Korea and Singapore hiring; results were guides or listicles of low reliability. A Hyro (Israel) record was drafted and withdrawn because detail could not be re-checked"}
{"type":"absence","grade":"E","src":["S80","S81"],"as_of":"2026-11-13","item":"Public-sector hiring beyond US Tech Force (UK AI Security Institute, GovTech Singapore, India)","searched":"One combined search; only US Tech Force coverage retrieved"}
{"type":"absence","grade":"E","src":["S62"],"as_of":"2026-11-13","item":"NASSCOM-Zinnov and Dell-Zinnov full reports and methods","searched":"Press coverage only"}
{"type":"absence","grade":"E","src":["S53","S56"],"as_of":"2026-11-13","item":"Overlap of Forbes AI 50 and CB Insights AI 100 with observed hiring volume","searched":"Full lists not retrieved; only a partial TrueUp overlap computed"}
{"type":"absence","grade":"E","src":["S56","S57"],"as_of":"2026-11-13","item":"Evidence that funding, headcount growth or product launches predict GenAI hiring","searched":"Searches on hiring signals and list methods; only vendor claims found"}
{"type":"absence","grade":"E","src":["S88","S89"],"as_of":"2026-11-13","item":"Vendor terms of service: Crunchbase, Tracxn, TrueUp, Fast AI Jobs, Greenhouse, Lever, Ashby, Workable","searched":"Secondary summaries only; ToS pages not opened (Dealroom T&Cs and pricing were read)"}
{"type":"absence","grade":"E","src":["S91","S92","S93"],"as_of":"2026-11-13","item":"Enforcement and complaints against Apollo, ZoomInfo, Lusha, RocketReach, Hunter","searched":"Search on CNIL and other regulator decisions; only KASPR and LinkedIn litigation found"}
{"type":"absence","grade":"E","src":["S95"],"as_of":"2026-11-13","item":"O*NET OnLine page status for K8","searched":"Not opened; the BLS 2025-35 release was read instead"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"UK Skilled Worker rule changes in 2025-2026","searched":"Not researched in this session"}
{"type":"absence","grade":"E","src":["S27","S78"],"as_of":"2026-11-13","item":"Remote-hiring policy for most census employers","searched":"Only Anthropic's board (Remote-Friendly flags) and Sakana's posting text read"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Tracxn pricing and terms","searched":"Not retrieved in this session; Tracxn appears only as the source of funding figures quoted by the press (S75)"}
```
