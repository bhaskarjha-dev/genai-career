---
id: "T0-26"
title: "Job-Search Tools: Trackers, Builders, Autofill, Auto-Apply, Agents, Open Source and MCP Servers"
date: "2026-11-11"
status: complete-with-gaps
topic: "job-search-tools-agents-oss-mcp"
tags: ["job-search-tools", "auto-apply", "autofill", "mcp", "open-source", "platform-terms", "india"]
informs_decisions: ["D-005"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic) in claude.ai with web search, page fetch and bash. COI: Anthropic products are in scope (Claude in Chrome; the Indeed connector listed in Claude's directory; Claude models appear in the salary-advice audits). Those rows are marked COI."
evidence_window: "2025-02-07 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 18
---

# T0-26: Job-Search Tools: Trackers, Builders, Autofill, Auto-Apply, Agents, Open Source and MCP Servers

Source numbers (S1, S2 …) refer to the Sources & Evidence Ledger. Grades follow EGP-1.0 (A primary and opened; B established secondary, platform data, or a primary page seen only as an extract; C vendor, practitioner or single-source; D memory; E unverifiable; M own calculation; P practice-curated). The brief anchors on 2026-11-11, but my tool clock read 2026-11-13 and every retrieval is dated 2026-11-13, so statuses are "as of 2026-11-13". Vendor outcome claims are grade C and marked COI. Many tool reviews are written by competing vendors (Scoutify, FastApply, LoopCV, Weekday, Resumly); I used them only for status, price or a stated vendor claim and say so. Repository figures come from github.com pages and commit feeds (the unauthenticated API was rate-limited). Stars measure attention, not quality or safety.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | No major job board permits third-party auto-apply bots; LinkedIn and Indeed prohibit them. | 85% | D |
| P2 | No independent study links ATS "score" checkers to interview outcomes. | 80% | D |
| P3 | LinkedIn offers no official MCP server for job search. | 60% | D |
| P4 | Greenhouse, Lever and Ashby expose public job-board APIs, and Adzuna, Reed and USAJOBS give free keys to individuals. | 85% | D |
| P5 | Job platforms do not run auto-apply for candidates themselves. | 65% | D |
| P6 | The large open-source auto-apply bots (tens of thousands of stars) are actively maintained. | 60% | D |

## Research Question

**Decision question:** which job-search tools help a GenAI job seeker, which carry account, legal, privacy or reputational risk, and what verdict does each get (informs D-005; `data/tools.json`; the tool catalog; the application operating system)?

**Sub-questions:** (1) are K1–K18 still true; (2) what do platform terms say; (3) what do employers' systems do with automated or duplicate applications; (4) which official APIs and MCP servers exist; (5) which open-source projects matter and how risky are they; (6) is there independent outcome evidence; (7) what privacy and security evidence exists; (8) what is the smallest useful stack.

**Scope as applied:** `tool` records use stage 6 for application tooling (trackers, autofill, auto-apply, checkers, builders, APIs, MCP, open source), stage 0 for general assistants and browser agents, and stage 1 for labour-market data. Boards, commercial résumé builders, contact finders and interview tools belong to other sessions; I recorded only those I met.

**Method:** about 45 web searches, 13 successful page fetches, and repository checks through bash. I read primary pages for Simplify, Teal, Greenhouse, Ashby, Indeed (MCP docs and newsroom), Adzuna terms, Remotive's README and Huntr's Q3 2026 report. LinkedIn's help pages block automated fetching (robots), so I saw them only as extracts. **Falsification searches:** independent evidence that auto-apply raises interviews (none found; only vendor claims); an official LinkedIn MCP server (none found); validation of ATS scores against outcomes (none); whether Sonara still operates (one competitor says no, one reading of Sonara's own footer says yes); whether any board explicitly permits third-party auto-apply (none found); whether LLM salary-advice bias persists in 2026-era models (it does, in one October 2026 preprint). A late verification round closed seven gaps (Simplify+ prices, Workable MCP, BLS and O*NET terms, Jooble documentation, the résumé-injection figures, the NCS fee advisory, Adzuna's India listing).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | LinkedIn and Indeed prohibit third-party automation of applying. LinkedIn's help page bars bots and extensions that automate activity on its site. Indeed's India help page lists third-party bots that apply for jobs as prohibited conduct, and its terms bar automating Indeed Apply outside its own tooling. | [S8][S9][S10][S11] | B |
| KF2 | Indeed tested its own "Apply For Me" from 2026-07-07, then on 2026-08-04 paused the automatic mode and kept a mode where the seeker reviews every draft. Trade press attributes the pause to employer pushback. | [S12][S13] | A (pause); C (reason) |
| KF3 | No independent controlled study of auto-apply outcomes was found. Huntr's correlational data (to 2026-10-01): 8.0% of applications led to interviews at 11–20 applications versus 2.4% at 100+, yet 72.0% of heavy appliers got at least one interview versus 47.8%. Of 68 survey users of send-for-you tools, 9% reported more interviews, 49% the same, 25% fewer. | [S16][S17] | B/C |
| KF4 | Employer systems have countermeasures. Greenhouse Real Talent flags bot and bulk-tool spam (phased in from Q3 2025). Ashby documents duplicate merging and Application Limits. About 1% of 196,682 résumés on one hiring platform carried hidden prompt injections. | [S14][S15][S25][S58] | A/B |
| KF5 | Simplify bundles two behaviours in one account. Copilot autofills and the user submits. Autopilot (20 credits a week) submits with no review step and stops rather than submit an answer it cannot determine. | [S1][S2][S3] | A |
| KF6 | Jobscan Auto Apply is real: review by default, optional auto-submit, Lever and Workable at launch, bundled in Premium ($49.95 a month). No outcome evidence. | [S41][S42][S43] | B/C |
| KF7 | Teal+ costs $13 a week, $29 a month or $79 a quarter (not $9 a week). Huntr Pro is $40 a month, $90 a quarter or $160 per six months. Two third parties report Simplify+ at $19.99 a week, $39.99 a month and $89.99 a quarter. Free tiers cover tracking. | [S18][S19][S20][S88][S89] | A/B/C |
| KF8 | Official MCP servers exist but mostly serve employers. Indeed's is a beta, Claude-only, read-only server for seekers. Greenhouse (open beta, July 2026) and Workable (94 tools by 2026-07-20) serve recruiters and admins. No official LinkedIn job-search MCP was found. | [S26][S23][S24][S31][S90][S29][S30] | A/B/C |
| KF9 | Community LinkedIn and Indeed MCP servers work through scraping or your logged-in session. The leading one (4,202 stars, Apache-2.0) can import browser session cookies and can message and connect on your behalf. | [S28][S86] | A/B |
| KF10 | Official job-data APIs for individuals exist: Adzuna, USAJOBS, Reed (UK only), Jooble, Remotive, Arbeitnow, Careerjet (publisher-oriented), and unauthenticated Greenhouse, Lever and Ashby board endpoints. Labour-market data is US-centred: BLS API v2 (500 queries a day), O*NET Web Services, and Indeed Hiring Lab data with no India series. Naukri has no public API. | [S32][S33][S34][S35][S36][S37][S39][S40][S67][S72][S91][S92][S93] | A/B/C |
| KF11 | Open-source leaders as of 2026-11-13: career-ops (82,242 stars, never submits), AIHawk (32,498, auto-applies), Reactive Resume (45,680), Resume-Matcher (29,270). OpenResume has had no commit since 2024-10-29. | [S73][S74][S77][S81][S79] | A |
| KF12 | ChatGPT Atlas was discontinued on 2026-08-09 and folded into ChatGPT. Comet and the Claude Chrome extension appear in HUMAN Security's May 2026 agent-traffic data. No board checked sanctions browser agents for applying, and trade press reports agent blocking rates rising. | [S68][S69][S47] | B/C |
| KF13 | Resume and applicant-data exposures from misconfigured cloud storage hit TalentHook (about 26M files), LiveCareer (5.1M) and HireClick (5.7M) in 2025. Naukri had an API bug exposing recruiter emails. | [S63][S64][S65][S66] | B |
| KF14 | Checker scores diverge by tool (one vendor test: 21% to 80% for the same résumé) and no outcome link exists; use them as gap lists. | [S43][S61][S62] | C |
| KF15 | Non-generative writing assistance raised hires by 8% and wages by 10% in a field experiment on one online labour market (abstract only; sample size not re-verified). LLM salary advice differs by persona, including in audits of 2026-era models. | [S54][S55][S56] | B |

## Recommendation

1. **Respect platform terms first.** Do not run bots, clicking extensions, scrapers or MCP servers that use your logged-in session on linkedin.com or indeed.com [S8][S10]. The cost is account restriction, and no benefit has been shown.
2. **Track for free.** Use Huntr's free tier, Teal's free tier, a spreadsheet, or MyGreenhouse for Greenhouse roles. Log every submission with date, CV version and source. If you pay, choose monthly or quarterly rather than weekly, and diarise the cancellation date.
3. **Autofill only on employer-hosted forms, and click Submit yourself.** Use Simplify Copilot or MyGreenhouse Quick Apply, read every answer, and leave Simplify Autopilot off.
4. **No unattended auto-apply.** If you experiment, use review-before-send modes (Jobscan's default; Indeed's draft mode) on a few targeted roles, and treat the result as unproven.
5. **Use a general LLM for drafting and rehearsal, not for salary targets.** Check every factual line, never add hidden text to a résumé, and take pay ranges from independent data.
6. **Treat checker scores as gap lists.** Free scans are enough; do not pay for a score.
7. **Technical readers: keep your CV as data.** RenderCV or Reactive Resume, plus a human-in-the-loop evaluator such as career-ops. Avoid open-source bots that submit, and scrapers aimed at LinkedIn or Indeed.
8. **Prefer official feeds.** Use the Indeed MCP in Claude for search (beta, read-only), the public Greenhouse, Lever and Ashby board endpoints for company watchlists, and Adzuna, Reed or USAJOBS for aggregate search. Never hand an agent your LinkedIn cookies or password, and treat posting text as untrusted input (P).
9. **India:** Naukri has no public API (one commercial source, C), so third-party scrapers rely on non-public endpoints; avoid them [S67]. Third-party listings of Adzuna's country set include India [S85][S100]. Indeed India's help bars bots [S10]. The NCS portal states that it charges jobseekers no fee at any stage, and the Labour Ministry repeated that warning on 2026-11-09 [S97][S98]. For labour-market context, BLS and O*NET describe US occupations only, and Indeed Hiring Lab's repository has no India folder [S72].

**What would change this:** an independent outcome study of any auto-apply category; a change in LinkedIn or Indeed terms or an Indeed return to automatic mode; an official LinkedIn MCP; a security incident at a listed tool; a Greenhouse, Ashby or Workday policy on automated applications.

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| Ban all automation | Partly adopted | Right for unattended submission and for LinkedIn and Indeed; autofill with human submit is documented practice [S1][S12]. |
| Allow supervised auto-apply | Rejected as default | Only vendor evidence; Indeed's own test paused the automatic mode [S12]. |
| Trust vendor success rates | Rejected | Grade C with COI; Huntr cannot observe auto-apply [S16]. |
| Treat open source as safer | Rejected | MIT-licensed bots still breach terms; stars show attention only [S74][S76]. |
| Pay for the full tool stack | Rejected | Jobscan Premium ($49.95) plus Teal+ ($29) plus Huntr Pro ($40) is $118.95 a month at monthly list prices (M; inputs S42, S18, S19), and free tiers cover the core jobs. |
| Wait for official agent integrations | Partly adopted | Indeed MCP exists but is read-only and Claude-only [S26]. |

## Detailed Findings

### DF1 Platform terms and employer treatment

LinkedIn's help page bars third-party software, including bots, plug-ins and extensions, that scrapes or automates activity; it was seen as an extract because the site blocks fetching [S8]. Secondary analysis of the User Agreement effective 2025-11-03 reports the same [S9]. Indeed's India help page lists third-party bots that apply for jobs as prohibited [S10]. A tracker of Indeed's terms (accessed 2026-07-28) quotes a clause barring automation of Indeed Apply outside its vendors and tooling, and a separate clause for its own Apply For Me tool [S11]. A competitor's survey of board terms found none that explicitly allows third-party auto-apply (COI) [S47].

On the employer side: Ashby's documentation covers duplicate-candidate merging and an Application Limits setting that can throttle or block repeat applications [S14][S15]. Greenhouse says spam comes from bulk automated tools and ships Real Talent to flag bots and fraud [S25]. A hidden-instruction study of 196,682 résumés found about 1% carrying hidden injections; over 90% of those used embedded data such as skill lists rather than explicit instructions. It did not measure effect on decisions, and a secondary summary reports the detector's precision as 86.1%, so some flags were false alarms [S58][S59][S99]. Press anecdotes report employers blocking reapplication by such candidates (C) [S60].

### DF2 Tool table by category

| Tool | Category | What | Price | Permissions and data | Status (date) | Verdict | Grade |
|---|---|---|---|---|---|---|---|
| Huntr | Tracker | Tracker, clipper, AI add-ons | Free (100 jobs per third party); Pro $40/mo, $90/qtr, $160/6 mo | Extension permissions not retrieved | Operating (2026-11-13) | use-with-care | B |
| Teal | Tracker | Tracker, builder, match score | Free; Teal+ $13/wk, $29/mo, $79/qtr | Not retrieved | Operating (2026-11-13) | use-with-care | A |
| MyGreenhouse | Autofill, tracker | Quick Apply on Greenhouse-hosted jobs | Free | Profile may be recommended to hiring teams; opt-out; says it never sells data (vendor claim) | Operating (2026-11-13) | use-with-care | A |
| Simplify Copilot | Autofill | Autofill and tracker | Free | Chrome store declares PII and location; Firefox listing asks for all-sites data access; about 500k Chrome users | Operating (2026-11-13) | use-with-care | B |
| Simplify Autopilot | Auto-apply | Credit-based submission | Simplify+ $19.99/wk, $39.99/mo, $89.99/qtr (two third parties); 20 credits/wk | No review step | Live (2026-11-13); homepage says "early access" | avoid | A |
| Jobscan Auto Apply | Auto-apply | Drafts, holds for review, optional auto-submit | Premium $49.95/mo | Lever and Workable at launch; review by default | Live (2026-11-13) | watch | B |
| LazyApply | Auto-apply | Extension bot for Easy Apply, Indeed | $99, $149, $999 per year (competitor-reported) | Runs in your LinkedIn session | Operating (2026-10, per competitor reviews) | avoid | C |
| FastApply, LoopCV, JobCopilot, AIApply, Massive | Auto-apply | Hosted cloud submission | $14/mo; €9.99/mo; about $0.93/day; $29/mo plus credits; Massive not priced | Not audited | Operating per vendor and roundup pages (2026-10) | avoid | C |
| Sonara | Auto-apply | Matching and submission | $2.95 trial renewing at $23.95 (competitor) | Operated by BOLD | Live under BOLD (2026-10) | avoid | C |
| Scoutify | Alerts, auto-apply | Alerts, Auto Apply and Sniper on employer ATS pages | $5/wk, $15/wk, $25/wk; weekly auto-renew | Applies on employer ATS, not LinkedIn (vendor claim) | Operating (2026-11-13) | avoid | B |
| Indeed Apply For Me | Auto-apply (first party) | Drafts and submits from Indeed profile | Free test | Uses your Indeed profile | Limited US test; automatic mode paused 2026-08-04 | watch | A |
| General LLMs (drafting) | AI assistant | Drafting and rehearsal | Varies | Do not paste ID documents | Operating (2026-11-13) | use-with-care | B |
| General LLMs (salary adviser) | AI assistant | Salary targets and negotiation advice | Varies | — | Operating (2026-11-13) | avoid | B |
| Jobscan checker, other checkers | Checker | Keyword match | $49.95/mo; 5 free scans/mo | Résumé upload | Operating (2026-11-13) | use-with-care | C |
| Indeed Hiring Lab data | Labour-market data | Postings index (CC-BY-4.0) | Free | No India series | Updated 2026-11-12 | use | A |
| BLS Public Data API | Labour-market data | US labour series, OEWS wages | Free; v2 key: 500 queries/day, 50 series/query | Registration renewed yearly; US only | Operating (2026-11-13) | use | B |
| O*NET Web Services | Labour-market data | US occupation skills and tasks | Free account | Attribution, register site URL, no alteration | Operating (2026-11-13) | use | B |

### DF3 Open-source table (retrieved 2026-11-13)

| Repository | Purpose | Licence | Stars | Last commit | Terms risk | Verdict |
|---|---|---|---|---|---|---|
| santifer/career-ops | Local scan, score, tailor; never submits | MIT | 82,242 | 2026-11-12 | Board scanning may breach site terms; includes contact discovery (out of scope) | use-with-care |
| feder-cr/Jobs_Applier_AI_Agent_AIHawk | Auto-apply bot | MIT | 32,498 | 2026-11-12 | Auto-submits; press cited LinkedIn risks | avoid |
| GodsScion/Auto_job_applier_linkedIn | LinkedIn auto-apply | MIT | 3,031 | 2026-09-10 | Core function breaches LinkedIn terms; dry-run option | avoid |
| speedyapply/JobSpy | Scraper: LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs, HelloWork | MIT | 4,709 | 2026-10-27 | Scrapes sites that forbid it | avoid |
| stickerdaniel/linkedin-mcp-server | LinkedIn MCP via your browser session | Apache-2.0 | 4,202 | 2026-11-13 | Platform does not permit; cookie import | avoid |
| AmruthPillai/Reactive-Resume | Résumé builder, self-hostable | MIT | 45,680 | 2026-11-12 | Hosted retention unverified | use-with-care |
| rendercv/rendercv | YAML to PDF résumé | MIT | 17,949 | 2026-03-25 | Slower maintenance | use-with-care |
| srbhr/Resume-Matcher | Local gap analysis and builder | Apache-2.0 | 29,270 | 2026-11-07 | None documented | use-with-care |
| xitanggg/open-resume | Builder and parser | AGPL-3.0 | 8,977 | 2024-10-29 | Stale for two years | watch |
| jsonresume/jsonresume.org | Résumé schema and registry (schema repo moved here) | MIT | 351 | 2026-11-07 | None | use-with-care |
| Gsync/jobsync | Self-hosted tracker | MIT | 1,525 | 2026-10-30 | Not assessed beyond metadata | watch |
| browser-use/browser-use | General browser-agent framework | MIT | 120,863 | 2026-11-12 | Depends on target site terms | watch |
| hiring-lab/job_postings_tracker | Indeed postings index | CC-BY-4.0 | 225 | 2026-11-12 | None; no India folder | use |

### DF4 Agent and API table

| Integration | Official? | Access | Platform permits? | Risks | Verdict |
|---|---|---|---|---|---|
| Indeed MCP (beta) | Yes | Sign-in; Claude connector only; search, detail, resume read and company data | Yes (its own) | Reads your Indeed profile; beta; COI; docs list four tools, a directory lists two | use-with-care |
| Greenhouse MCP | Yes | OAuth, admin scopes; open beta for Core, Plus, Pro (2026-07) | Employer-side | Not for seekers | watch |
| Workable MCP | Yes | OAuth2 custom connector; all customers; 94 tools by 2026-07-20, including a job-search tool over the account's job catalog | Employer-side | Read and write on employer data; not for seekers | watch |
| Get on Board MCP | Yes (board) | AI client connects to its Talent Database; candidate profiles readable from 2026-10 | Employer-side | Seeker use unverified | watch |
| LinkedIn job-search MCP | None found | — | — | — | Absence |
| stickerdaniel/linkedin-mcp-server | No | Your logged-in browser session; can import cookies from local browsers; can message and connect | No | Account restriction; credential exposure | avoid |
| Scraper-backed Indeed or LinkedIn MCP (HasData, Apify) | No | API key to vendor | No | Terms breach | avoid |
| adzuna-mcp (community) | No | Your Adzuna keys | Within Adzuna terms | Rate limits | use-with-care |
| Adzuna API | Yes | Free key; personal job search permitted; India (`in`) appears in third-party country lists (counts differ from 12 to 25) | Yes | Free tier for evaluation; official country page not opened | use-with-care |
| USAJOBS API | Yes | Free key plus email User-Agent | Yes | US federal only | use |
| Reed API | Yes | Free key, basic auth | Yes | UK only | use |
| Jooble API | Yes | Key on request via jooble.org/api/about; POST with key in URL | Terms on its about page, not read | Limits per key | use-with-care |
| Remotive API | Yes | No key; 24-hour delay; 4 calls a day advised | Yes, with attribution | Thin feed | use-with-care |
| Arbeitnow API | Yes | No key | Not read | Europe focus | use-with-care |
| Careerjet API | Yes | Key; real user IP and agent required | Publisher use | Not for personal scripts | use-with-care |
| Greenhouse, Lever, Ashby board APIs | Yes | Unauthenticated GET | Yes | Per-company only | use |

### DF5 Outcome evidence

Huntr's Q3 2026 report (platform data, B; vendor COI) states that it sees when a user marks a job applied, not how, so it cannot measure auto-apply tools. Its survey: of 329 respondents, 68 (21%) had used a send-for-you tool; 40 of those 68 had stopped [S16]. Volume raises total interviews while lowering yield per application, so "adverse" holds per application only. K6's figures (9.25% and 2.58%) match the Q1 2026 report as extracted [S17]. Indeed reports that Apply For Me applications were 3.5 times more likely to be a great fit (vendor, COI, C) [S12]. The peer-reviewed experiment [S54] concerns non-generative writing help on one online labour market and does not transfer to auto-apply.

### DF6 Privacy and security

Exposures: TalentHook (Azure container, about 26M files, CISA contacted 2025-04-09) [S64]; LiveCareer (5.1M files) [S63]; HireClick (5.7M files) [S65]. BOLD, which owns Sonara, is the company behind LiveCareer; I found no link between the exposed files and Sonara. Extensions: Simplify's Firefox listing requires access to data on all websites [S6]; Teal and Huntr permission lists were not retrieved. Agents: researchers demonstrated cross-site data extraction against Atlas, with similar conditions reported for Gemini in Chrome, Claude for Chrome and Comet [S68]. I found no job-posting-specific injection incident (see Absences).

### DF7 Minimal stack

| Job | Free choice | Paid (optional) | Failure mode |
|---|---|---|---|
| CV source of truth | RenderCV or Reactive Resume | — | Parse errors; RenderCV last commit 2026-03-25 |
| Tracker | Huntr free, Teal free, spreadsheet | Teal+ monthly or quarterly in a sprint | Huntr free cap; weekly auto-renew |
| Autofill | Simplify Copilot, MyGreenhouse | — | Misfilled fields; Autopilot sits in the same account |
| Drafting | General LLM | — | Fabricated details; persona-shaped advice |
| Gap check | Jobscan free scans, Resume-Matcher | Jobscan quarterly | Unvalidated scores |
| Discovery | ATS board APIs, Adzuna, Reed, USAJOBS, Indeed MCP | — | Coverage gaps; beta; read-only |
| Human-in-the-loop evaluator (technical readers) | career-ops with your own LLM | — | Board scanning may breach site terms; scoring errors; contact discovery is out of scope |

**Avoid:** LazyApply-type bots, Autopilot and Sniper-style unattended submission, hosted bulk services, scraper-backed MCP with your LinkedIn session, hidden prompts, LLM salary targets.

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Auto-apply at volume: weak, adverse evidence | updated | [S16][S12][S13][S25] | B |
| K2 | Autofill only with review and own Submit | confirmed | [S1][S21][S12] | B |
| K3 | ATSs keep history; Ashby matches by email | confirmed | [S14][S15] | A |
| K4 | LinkedIn bars automation tools | confirmed | [S8][S9] | B |
| K5 | No study links ATS scores to outcomes | confirmed | [S43][S61][S62] | C |
| K6 | Huntr 9.25% vs 2.58% | updated | [S16][S17] | B |
| K7 | LLM drafting: use-with-care; +8% hires | confirmed | [S54] | B |
| K8 | LLM career or salary adviser: avoid | confirmed | [S55][S56][S57] | B |
| K9 | Simplify Copilot use-with-care | confirmed | [S5][S6][S1] | B |
| K10 | MyGreenhouse use-with-care | confirmed | [S21][S22] | A |
| K11 | Huntr use-with-care | confirmed | [S19][S20] | B |
| K12 | Teal $9 a week | updated | [S18] | A |
| K13 | LazyApply avoid | confirmed | [S44][S45][S8][S10] | B |
| K14 | Simplify Autopilot beta, avoid | updated | [S1][S2][S3] | A |
| K15 | Jobscan Auto Apply unverified | updated | [S41][S42] | B |
| K16 | Hosted services avoid; 3 of 8 submit | confirmed | [S46][S53][S87] | C |
| K17 | Sonara relaunched under BOLD | confirmed | [S48][S49][S50] | C |
| K18 | Scoutify avoid, vendor-only | confirmed | [S51][S52][S4] | B |

## Absences

| Item | Where I looked |
|---|---|
| Independent outcome study of any auto-apply category | Huntr reports; academic phrasing; roundups |
| Official LinkedIn MCP or job-search API for individuals | Two secondary guides say none; no LinkedIn primary page opened |
| Workday, Lever and Ashby terms on automated applications | Not retrieved |
| Own-page pricing for LoopCV, JobCopilot, AIApply, Massive, FastApply | Competitor pages only |
| Simplify+ prices on Simplify's own help page | Extract did not show amounts; two third parties agree (C) |
| Teal, Huntr and Jobscan extension permissions and retention terms | Policies not opened |
| Jooble terms-of-use text and per-key limits | Documentation read as extract; terms live on its about page, not read |
| Job-posting prompt injection against applicant agents | One search; nothing job-specific |
| NCS (India) API for jobseekers | Advisory only |
| Naukri public API | One commercial source says none (C) |
| India series in Indeed Hiring Lab data | No IN folder in repository listing |
| Adzuna's official country list (India coverage) | Third-party listings only; counts differ (12 to 25) |
| Other labour-market tools (Lightcast, Levels.fyi data) | Not checked |
| Jobright and Careerflow status | Not verified |

## Open Questions & Risks

Strongest objections: (1) **Huntr data is self-selected and correlational.** Heavy appliers may be different people; I report the figures as B/C and note the contradiction between yield and totals. (2) **Auto-apply may help some users.** Six of 68 reported more interviews [S16]; I could not test for causation. (3) **Terms of service are not law.** A vendor guide argues automation is lawful and the risk is account restriction [S94]; I give pointers only and no legal advice. (4) **Competitor-authored sources dominate.** I used them for status and price only [S47]. (5) **Stars are attention.** (6) **COI:** I am an Anthropic model, and Claude in Chrome and the Indeed connector are Anthropic-related.

Open: Indeed's next step after the pause; whether Greenhouse Real Talent is switched on at specific employers; whether Simplify drops the "early access" label.

## Discovered Concerns

- Hidden prompts in résumés: a reputational and ethical risk [S58][S60].
- Agent-browser security: proof-of-concept data extraction [S68]; Amazon v. Perplexity injunction (2026-03) reported later reversed by one source, status unverified (V0) [S69].
- Weekly auto-renewing billing at Scoutify and Teal's weekly plan.
- Sonara's 2024 shutdown locked users out of their data; keep a local export.
- Greenhouse says weaker fraud signals are warnings, so false flags are possible.
- Indeed's terms were revised 2026-07-08 and 2026-09-29 [S11][S47].

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | No board permits third-party auto-apply | Confirmed | [S8][S10][S47] | Core of K13 |
| P2 | No study links checkers to outcomes | Confirmed | [S43][S61] | K5 stays |
| P3 | No official LinkedIn MCP | Confirmed (C) | [S29][S30] | Prefer Indeed MCP |
| P4 | Public ATS APIs and free keys | Updated | [S32][S36][S39] | Careerjet is publisher-only |
| P5 | Platforms do not run auto-apply | Contradicted | [S12] | Indeed tested and paused |
| P6 | Large OSS bots are maintained | Confirmed | [S74] | AIHawk active |

## Sources & Evidence Ledger

All retrieved 2026-11-13. "Undated" means no publication date was shown.

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Get started with Autopilot, Simplify, https://help.simplify.jobs/articles/1784339-get-started-with-autopilot | Undated | 2026-11-13 | A | Read | vendor facts | Autopilot, no review |
| S2 | Autopilot credits and failed applications, Simplify, https://help.simplify.jobs/articles/4455305-autopilot-credits-and-failed-applications | Undated | 2026-11-13 | A | Read | vendor facts | 20 credits |
| S3 | What's included in Simplify+, Simplify, https://help.simplify.jobs/articles/5623502-whats-included-in-simplify-features-and-pricing | Undated | 2026-11-13 | A | Read | vendor facts | Plan scope |
| S4 | Simplify vs Scoutify Sniper, Scoutify, https://scoutify.com/blog/scoutify-vs-simplify/ | 2026-09 | 2026-11-13 | C | Read | COI | Competitor view of Autopilot |
| S5 | Simplify Copilot, Chrome Web Store, https://chromewebstore.google.com/detail/pbanhockgagggenencehbnadejlgchfc | Undated | 2026-11-13 | B | Extract | | Users, rating, data |
| S6 | Simplify Copilot, Mozilla Add-ons, https://addons.mozilla.org/en-GB/firefox/addon/simplify-jobs | 2025-09-26 | 2026-11-13 | B | Extract | | Permissions |
| S7 | Privacy policy, Simplify, https://simplify.jobs/privacy.html | Undated | 2026-11-13 | B | Extract | | Data use |
| S8 | Prohibited software and extensions, LinkedIn Help, https://www.linkedin.com/help/linkedin/answer/a1341387 | Undated | 2026-11-13 | B | Extract | robots-blocked | K4 |
| S9 | LinkedIn User Agreement analysis, ConductAtlas, https://conductatlas.com/platform/linkedin/linkedin-user-agreement/linkedin-dos-and-donts-prohibited-conduct/ | 2025-11-03 | 2026-11-13 | C | Extract | secondary | K4 |
| S10 | Indeed Help (India), https://support.indeed.com/hc/en-in/articles/360028540531 | Undated | 2026-11-13 | B | Extract | | Bots prohibited |
| S11 | Indeed Terms provisions, ConductAtlas, https://conductatlas.com/platform/indeed/indeed-terms-of-service/provision/CA-P-028259/automation-of-indeed-apply-process-prohibited/ | 2026-07 (accessed 2026-07-28) | 2026-11-13 | C | Extract | secondary | Indeed Apply clause |
| S12 | Indeed's Apply For Me, Indeed Newsroom, https://www.indeed.com/news/releases/indeed-tests-apply-for-me-job-search | 2026-07-07 (upd. 2026-08-04) | 2026-11-13 | A | Read | COI on claims | K1, pause |
| S13 | Indeed Hits Pause on Apply for Me, HR Tech Feed, https://hrtechfeed.com/indeed-hits-pause-on-apply-for-me-ai-feature-after-employer-pushback/ | 2026-08 | 2026-11-13 | C | Extract | | Employer pushback |
| S14 | Handling multiple applications, Ashby Docs, https://docs.ashbyhq.com/handling-multiple-applications-from-one-candidate | Undated | 2026-11-13 | A | Read | | K3, limits |
| S15 | Merge duplicate profiles, Ashby Docs, https://docs.ashbyhq.com/how-do-i-merge-duplicate-candidate-profiles | Undated | 2026-11-13 | A | Read | | K3 |
| S16 | Q3 2026 Job Search Trends, Huntr, https://huntr.co/research/job-search-trends-q3-2026 | 2026-10-13 | 2026-11-13 | B | Read | platform data; COI | K1, K6 |
| S17 | Q1 2026 Job Search Trends, Huntr, https://huntr.co/research/job-search-trends-q1-2026 | 2026 | 2026-11-13 | B | Extract | | K6 figures |
| S18 | Teal vs. Teal+, Teal Help Centre, https://help.tealhq.com/en/articles/9530153-teal-vs-teal | Undated | 2026-11-13 | A | Read | vendor facts | K12 |
| S19 | Pricing, Huntr, https://api.huntr.co/pricing | Undated | 2026-11-13 | B | Extract | | Huntr prices |
| S20 | Hiretual vs Huntr, Pulse Signal, https://getpulsesignal.com/compare/hiretual-vs-huntr | 2026-10-06 | 2026-11-13 | C | Extract | | 100-job cap |
| S21 | MyGreenhouse for job seekers, Greenhouse, https://www.greenhouse.com/for-jobseekers | Undated | 2026-11-13 | A | Read | vendor claims C | K10 |
| S22 | MyGreenhouse Quick Apply, Greenhouse Support, https://support.greenhouse.io/hc/en-us/articles/35746094035099-MyGreenhouse-Quick-Apply | Undated | 2026-11-13 | B | Extract | | Quick Apply |
| S23 | Greenhouse Launches MCP, Greenhouse, https://www.greenhouse.com/newsroom/greenhouse-launches-mcp-giving-hiring-teams-a-governed-way-to-connect-ai-tools-to-greenhouse | 2026-05-07 | 2026-11-13 | B | Extract | | MCP launch |
| S24 | Release Notes July 2026, Greenhouse Support, https://support.greenhouse.io/hc/en-us/articles/53681385010331-Release-Notes-July-2026 | 2026-07 | 2026-11-13 | B | Extract | | Open beta |
| S25 | Real Talent launch, Greenhouse, https://www.greenhouse.com/newsroom/greenhouse-real-talent-tm-launches-to-fix-overwhelming-candidate-pipelines-while-combatting-fraud-and-spam-in-hiring | 2025 | 2026-11-13 | B | Extract | vendor | Spam detection |
| S26 | Indeed MCP, Indeed Docs, https://docs.indeed.com/mcp/ | Undated | 2026-11-13 | A | Read | COI (Claude connector) | Indeed MCP |
| S27 | Indeed MCP analysis, Agentman, https://agentman.ai/agentskills/connections/mcp-server/indeed | 2026-08-22 | 2026-11-13 | C | Extract | | Tool and scope conflict |
| S28 | linkedin-mcp-server, GitHub, https://github.com/stickerdaniel/linkedin-mcp-server | 2026-11-13 | 2026-11-13 | A | Read | | Cookie import |
| S29 | LinkedIn MCP: what's official, ContextBolt, https://contextbolt.com/blog/linkedin-mcp/ | 2026 | 2026-11-13 | C | Extract | | No official MCP |
| S30 | What is a LinkedIn MCP server, Contentin, https://contentin.io/glossary/linkedin-mcp/ | 2026 | 2026-11-13 | C | Extract | | No official MCP |
| S31 | Workable MCP Server, Workable, https://resources.workable.com/workable-mcp-server | 2026 | 2026-11-13 | B | Extract | vendor | Workable MCP |
| S32 | Adzuna API Terms of Service, https://developer.adzuna.com/docs/terms_of_service | Undated | 2026-11-13 | A | Read | | Adzuna terms |
| S33 | Authentication guide, USAJOBS Developer, https://developer.usajobs.gov/Guides/Authentication | Undated | 2026-11-13 | B | Extract | | USAJOBS |
| S34 | Jobseeker API, Reed, https://www.reed.co.uk/developers/jobseeker | Undated | 2026-11-13 | B | Extract | | Reed |
| S35 | remote-jobs-api README, Remotive, GitHub, https://github.com/remotive-com/remote-jobs-api | Undated | 2026-11-13 | A | Read | | Remotive |
| S36 | Careerjet partner API, https://www.careerjet.im/partners/api | Undated | 2026-11-13 | B | Extract | | Careerjet |
| S37 | Free Job Board API, Arbeitnow, https://arbeitnow.com/blog/job-board-api | 2026 | 2026-11-13 | B | Extract | | Arbeitnow |
| S38 | Free job APIs in 2026, JobsPipe, https://jobspipe.dev/blog/free-job-api | 2026 | 2026-11-13 | C | Extract | COI | Adzuna limits |
| S39 | Four job-board APIs verified live, DEV Community, https://dev.to/gettingtechnicl/the-public-api-behind-every-careers-page-and-how-to-pull-structured-job-data-from-any-of-them-2d80 | 2026-08-21 | 2026-11-13 | C | Extract | | ATS endpoints |
| S40 | Multi-ATS Jobs Feed, Apify, https://apify.com/hardwoodlogic/multi-ats-jobs-feed | 2026 | 2026-11-13 | C | Extract | quotes Greenhouse docs | Public GET |
| S41 | Auto Apply, Jobscan, https://www.jobscan.co/auto-apply | Undated | 2026-11-13 | B | Extract | vendor | K15 |
| S42 | Jobscan vs Simplify, Jobscan, https://www.jobscan.co/blog/jobscan-vs-simplify/ | 2026 | 2026-11-13 | B | Extract | vendor | Lever, Workable; $49.95 |
| S43 | Jobscan review, Careery, https://careery.pro/blog/is-jobscan-worth-it-2026 | 2026-10-09 | 2026-11-13 | C | Extract | | Quarterly price; no evidence |
| S44 | LazyApply review, Weekday, https://www.weekday.works/post/lazyapply-review | 2026-10 | 2026-11-13 | C | Extract | COI | Prices |
| S45 | LazyApply review, LoopCV, https://blog.loopcv.pro/lazyapply-review/ | 2026-07-03 | 2026-11-13 | C | Extract | COI | Trustpilot |
| S46 | Which bots actually submit, FastApply, https://blog.fastapply.co/ai-job-application-bots-which-actually-submit-2026 | 2026-05 | 2026-11-13 | C | Extract | COI | K16 claim origin |
| S47 | Which job boards allow auto apply, FastApply, https://blog.fastapply.co/which-job-boards-allow-auto-apply-2026 | 2026-10 | 2026-11-13 | C | Extract | COI | Board terms survey |
| S48 | Sonara, 6figr, https://6figr.com/blog/?p=780 | 2026-10 | 2026-11-13 | C | Extract | | Footer reads BOLD |
| S49 | Sonara review, Weekday, https://www.weekday.works/post/sonara-ai-review | 2026-10 | 2026-11-13 | C | Extract | COI | Relaunch |
| S50 | Sonara directory, LoopCV, https://www.loopcv.pro/directory/sonara/ | 2026 | 2026-11-13 | C | Extract | COI; dissent | Status conflict |
| S51 | Pricing, Scoutify, https://scoutify.com/pricing/ | Undated | 2026-11-13 | B | Extract | vendor | K18 |
| S52 | Scoutify, Apple App Store, https://apps.apple.com/app/id6756941343 | Undated | 2026-11-13 | B | Extract | vendor | App prices |
| S53 | Best auto-apply tools, Scoutify, https://scoutify.com/blog/best-auto-apply-tools/ | 2026 | 2026-11-13 | C | Extract | COI | Competitor prices |
| S54 | Algorithmic Writing Assistance on Jobseekers' Resumes Increases Hires, Management Science 71(12), https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2024.04528 | 2025 | 2026-11-13 | B | Extract | peer-reviewed | K7 |
| S55 | Asking an AI for salary negotiation advice, PLOS ONE, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11805401/ | 2025-02-07 | 2026-11-13 | B | Extract | peer-reviewed | K8 |
| S56 | AI Advice Reinforces Traditional Gender Roles, arXiv 2610.14036, https://arxiv.org/pdf/2610.14036 | 2026-10 | 2026-11-13 | C | Extract | preprint | K8, 2026 models |
| S57 | Surface Fairness, Deep Bias, arXiv 2506.10491, https://arxiv.org/html/2506.10491v1 | 2025 | 2026-11-13 | C | Extract | preprint | K8 |
| S58 | Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening, arXiv 2605.28999, https://arxiv.org/html/2605.28999v1 | 2026-05-27 | 2026-11-13 | B | Extract | USENIX Security 2026 | Hidden prompts |
| S59 | Thwarting Hidden Resume Hacks, Duke Pratt, https://pratt.duke.edu/news/thwarting-prompt-injection/ | 2026-07-22 | 2026-11-13 | B | Extract | | Study summary |
| S60 | Job seekers hide AI prompts, Herald Corp, https://biz.heraldcorp.com/article/10870662 | 2026-09-11 | 2026-11-13 | C | Extract | anecdotes | Employer reaction |
| S61 | Best resume checkers, Enhancv, https://enhancv.com/blog/best-resume-checkers/ | 2026 | 2026-11-13 | C | Extract | COI | Score spread |
| S62 | ATS checker test, ATS Verification, https://atsverification.com/blog/ats-checker-test-2026/ | 2026-10-28 | 2026-11-13 | C | Extract | COI | Checker test |
| S63 | LiveCareer exposure, SC World, https://www.scworld.com/brief/over-5m-job-seekers-data-accidentally-exposed-by-livecareer | 2025 | 2026-11-13 | B | Extract | | Exposure |
| S64 | TalentHook leak, TEISS, https://www.teiss.co.uk/news/millions-of-us-job-seekers-resumes-exposed-in-talenthook-data-leak-16044 | 2025 | 2026-11-13 | B | Extract | | Exposure |
| S65 | HireClick exposure, Daily Security Review, https://dailysecurityreview.com/security-spotlight/hireclick-exposes-5-7-million-resume-files-due-to-misconfigured-cloud-storage/ | 2025 | 2026-11-13 | C | Extract | | Exposure |
| S66 | Naukri recruiter email exposure, TechRadar, https://www.techradar.com/pro/security/another-top-employment-website-found-exposing-recruiter-email-addresses | 2025-05 | 2026-11-13 | B | Extract | headline and secondary | Naukri bug |
| S67 | Naukri API, JobsPipe, https://jobspipe.dev/sources/naukri | 2026 | 2026-11-13 | C | Extract | COI | No public API |
| S68 | OpenAI is shutting down ChatGPT Atlas, Business Standard, https://www.business-standard.com/technology/tech-news/openai-is-shutting-down-chatgpt-atlas-what-it-means-for-ai-browsing-126071000619_1.html | 2026-07-10 | 2026-11-13 | B | Extract | | Atlas end; PoC |
| S69 | AI agent traffic, PPC Land, https://ppc.land/ai-agent-traffic-dips-in-may-but-blocking-rates-keep-climbing/ | 2026-06 | 2026-11-13 | C | Extract | quotes HUMAN | Agent share; injunction |
| S70 | Indeed Career Scout suite, Indeed via BusinessWire, https://www.businesswire.com/news/home/20250910809034/en/Indeed-Introduces-New-Suite-of-Hiring-Products-Career-Scout-Talent-Scout-Premium-Sponsored-Jobs-and-Indeed-Connect | 2025-09-10 | 2026-11-13 | B | Extract | COI claims | Career Scout |
| S71 | Indeed AI agents, Social Samosa, https://www.socialsamosa.com/industry-updates/indeed-introduces-ai-powered-job-search-agents-10901796 | 2025 | 2026-11-13 | C | Extract | | India preview |
| S72 | job_postings_tracker, Indeed Hiring Lab, GitHub, https://github.com/hiring-lab/job_postings_tracker | 2026-11-12 | 2026-11-13 | A | Read | | Labour data; no IN |
| S73 | career-ops, GitHub, https://github.com/santifer/career-ops | 2026-11-12 | 2026-11-13 | A | Read | | OSS |
| S74 | AIHawk, GitHub, https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk | 2026-11-12 | 2026-11-13 | A | Read | | OSS |
| S75 | JobSpy, GitHub, https://github.com/speedyapply/JobSpy | 2026-10-27 | 2026-11-13 | A | Read | | OSS |
| S76 | Auto_job_applier_linkedIn, GitHub, https://github.com/GodsScion/Auto_job_applier_linkedIn | 2026-09-10 | 2026-11-13 | A | Read | | OSS |
| S77 | Reactive-Resume, GitHub, https://github.com/AmruthPillai/Reactive-Resume | 2026-11-12 | 2026-11-13 | A | Read | | OSS |
| S78 | rendercv, GitHub, https://github.com/rendercv/rendercv | 2026-03-25 | 2026-11-13 | A | Read | | OSS |
| S79 | open-resume, GitHub, https://github.com/xitanggg/open-resume | 2024-10-29 | 2026-11-13 | A | Read | | OSS |
| S80 | jsonresume.org, GitHub, https://github.com/jsonresume/jsonresume.org | 2026-11-07 | 2026-11-13 | A | Read | | OSS |
| S81 | Resume-Matcher, GitHub, https://github.com/srbhr/Resume-Matcher | 2026-11-07 | 2026-11-13 | A | Read | | OSS |
| S82 | jobsync, GitHub, https://github.com/Gsync/jobsync | 2026-10-30 | 2026-11-13 | A | Read | | OSS |
| S83 | browser-use, GitHub, https://github.com/browser-use/browser-use | 2026-11-12 | 2026-11-13 | A | Read | | OSS |
| S84 | BeamApply, Mozilla Add-ons, https://addons.mozilla.org/en-US/firefox/addon/beamapply/ | 2026-09-05 | 2026-11-13 | B | Extract | | Small OSS autofill |
| S85 | Adzuna Job Search MCP (Jayesh-Kr), Glama, https://glama.ai/mcp/servers/Jayesh-Kr/adzuna-mcp/tree | 2026 | 2026-11-13 | C | Extract | | Community MCP; India in country list |
| S86 | Indeed MCP Server, HasData, https://mcpservers.org/servers/hasdata/indeed-mcp | 2026 | 2026-11-13 | C | Extract | vendor | Scraper MCP |
| S87 | Auto-apply tool roundup, TheWearify, https://thewearify.com/?p=212101 | 2026 | 2026-11-13 | C | Extract | | LoopCV, AIApply prices |
| S88 | Simplify Jobs review, Weekday, https://www.weekday.works/post/simplify-jobs-review | 2026-10-27 | 2026-11-13 | C | Extract | COI | Simplify+ prices |
| S89 | Simplify Jobs review, Remote Job Assistant, https://www.remotejobassistant.com/blog/simplify-jobs-review | 2026-03-10 | 2026-11-13 | C | Extract | prices checked via upgrade flow | Simplify+ prices |
| S90 | Workable Expands MCP Server to 94 Tools, GlobeNewswire, https://www.globenewswire.com/news-release/2026/07/20/3329974/0/en/Workable-Expands-MCP-Server-to-94-Tools-Extending-AI-Assistant-Access-Across-the-Full-Hiring-and-HR-Lifecycle.html | 2026-07-20 | 2026-11-13 | B | Extract | vendor | Workable MCP |
| S91 | BLS Public Data API FAQs, US Bureau of Labor Statistics, https://www.bls.gov/developers/api_FAQs.htm | Undated | 2026-11-13 | B | Extract | | BLS limits |
| S92 | O*NET Web Services Data License, https://services.onetcenter.org/help/license_data | Undated | 2026-11-13 | B | Extract | | O*NET terms |
| S93 | REST API documentation, Jooble Help Center, https://jooblehelpcenter.freshdesk.com/en/support/solutions/articles/60001448238-rest-api-documentation | Undated | 2026-11-13 | B | Extract | | Jooble |
| S94 | Is it legal to automate job applications?, LoopCV, https://loopcv.pro/guides/is-it-legal-to-automate-job-applications | 2026 | 2026-11-13 | C | Extract | COI | Legality argument |
| S95 | Get on Board MCP Server and candidate profiles, Get on Board, https://www.getonbrd.com/product_updates/mejores-publicaciones-en-google-jobs-y-perfiles-en-el-servidor-mcp | 2026-10 | 2026-11-13 | B | Extract | vendor | Board MCP |
| S96 | Indeed MCP Connector, Skills Playground, https://skillsplayground.com/connectors/indeed/ | 2026 | 2026-11-13 | C | Extract | | Two-tool listing |
| S97 | National Career Service home page, Ministry of Labour and Employment (India), https://www.ncs.gov.in/ | Undated | 2026-11-13 | B | Extract | government site | No-fee statement |
| S98 | Labour Ministry warns jobseekers against fake 'National Career Service' job offers, IANS, https://ianslive.in/labour-ministry-warns-jobseekers-against-fake-ncs-job-offers--20261109161546 | 2026-11-09 | 2026-11-13 | B | Extract | | Ministry advisory |
| S99 | Resume prompt injection, Metaview, https://www.metaview.ai/resources/blog/resume-prompt-injection | 2026 | 2026-11-13 | C | Extract | COI (recruiting-AI vendor) | Detector precision; data vs instructions |
| S100 | Adzuna API, Jentic, https://jentic.com/apis/adzuna.com/adzuna | 2026 | 2026-11-13 | C | Extract | | Country list includes in |

## Data Appendix

```jsonl
{"type":"tool","id":"huntr","name":"Huntr","stage":6,"category":"Application tracker","what":"Job tracker, clipper, AI add-ons","verdict":"use-with-care","why":"Free tier (100 jobs per third party) suffices; log every submission; pay only for a short sprint","url":"https://huntr.co","status":"operating (as of 2026-11-13)","risk":"upfront multi-month billing","price":{"free":true,"plans":[{"amount":40,"currency":"USD","period":"month"},{"amount":90,"currency":"USD","period":"quarter"},{"amount":160,"currency":"USD","period":"half-year"}]},"open_source":false,"grade":"B","src":["S19","S20"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"teal","name":"Teal","stage":6,"category":"Application tracker","what":"Tracker, builder, match score, extension","verdict":"use-with-care","why":"Free tier covers tracking; Teal+ weekly is $13 not $9; avoid weekly auto-renew","url":"https://www.tealhq.com","status":"operating (as of 2026-11-13)","risk":"weekly billing; extension permissions not retrieved","price":{"free":true,"plans":[{"amount":13,"currency":"USD","period":"week"},{"amount":29,"currency":"USD","period":"month"},{"amount":79,"currency":"USD","period":"quarter"}]},"open_source":false,"grade":"A","src":["S18"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"mygreenhouse","name":"MyGreenhouse","stage":6,"category":"Application autofill","what":"Quick Apply autofill and tracker for Greenhouse-hosted jobs","verdict":"use-with-care","why":"Free, global; profile may be recommended to hiring teams (opt-out); submit yourself","url":"https://www.greenhouse.com/for-job-seekers","status":"operating (as of 2026-11-13)","risk":"profile sharing; vendor-only claims on hires","price":{"free":true,"plans":[]},"open_source":false,"grade":"A","src":["S21","S22"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"simplify-copilot","name":"Simplify Copilot","stage":6,"category":"Application autofill","what":"Browser autofill and tracker","verdict":"use-with-care","why":"Human-submit autofill on employer forms; broad site permissions; keep Autopilot off","url":"https://simplify.jobs","status":"operating (as of 2026-11-13)","risk":"all-sites data access on Firefox; misfilled fields","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S5","S6","S7"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"simplify-autopilot","name":"Simplify Autopilot","stage":6,"category":"Auto-apply agent","what":"Credit-based unattended submission","verdict":"avoid","why":"No review step; 20 credits a week; stops rather than submit an undeterminable answer","url":"https://simplify.jobs","status":"live; homepage says early access (as of 2026-11-13)","risk":"unreviewed screening answers","price":{"free":false,"plans":[{"amount":19.99,"currency":"USD","period":"week"},{"amount":39.99,"currency":"USD","period":"month"},{"amount":89.99,"currency":"USD","period":"quarter"}]},"open_source":false,"note":"Simplify+ prices come from two third parties (S88, S89); Simplify's own extract did not show amounts","grade":"A","src":["S1","S2","S3","S88","S89"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"jobscan-auto-apply","name":"Jobscan Auto Apply","stage":6,"category":"Auto-apply agent","what":"Drafts applications, holds for review, optional auto-submit","verdict":"watch","why":"Review by default; Lever and Workable at launch; no outcome evidence; avoid auto-submit setting","url":"https://www.jobscan.co/auto-apply","status":"live (as of 2026-11-13)","risk":"opt-in auto-submit; credits","price":{"free":false,"plans":[{"amount":49.95,"currency":"USD","period":"month"}]},"open_source":false,"grade":"B","src":["S41","S42","S43"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"lazyapply","name":"LazyApply","stage":6,"category":"Auto-apply agent","what":"Extension bot for LinkedIn Easy Apply, Indeed, ZipRecruiter","verdict":"avoid","why":"Core function automates applying on boards whose terms prohibit it; Trustpilot low 2s (competitor-reported)","url":"https://lazyapply.com","status":"operating (as of 2026-10)","risk":"account restriction; refund disputes","price":{"free":false,"plans":[{"amount":99,"currency":"USD","period":"year"},{"amount":149,"currency":"USD","period":"year"},{"amount":999,"currency":"USD","period":"year"}]},"open_source":false,"grade":"C","src":["S44","S45","S8","S10"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"fastapply","name":"FastApply","stage":6,"category":"Auto-apply agent","what":"Hosted cloud auto-apply","verdict":"avoid","why":"Unattended hosted submission; only vendor test evidence; board terms bar bots","url":"https://fastapply.co","status":"operating per vendor blog (2026-10)","risk":"unaudited; reputational","price":{"free":false,"plans":[{"amount":14,"currency":"USD","period":"month"}]},"open_source":false,"grade":"C","src":["S46","S47"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"loopcv","name":"LoopCV","stage":6,"category":"Auto-apply agent","what":"Hosted auto-apply campaigns and LinkedIn extension","verdict":"avoid","why":"Unattended submission; LinkedIn extension breaches terms; not audited","url":"https://www.loopcv.pro","status":"operating per roundups (2026)","risk":"account restriction","price":{"free":true,"plans":[{"amount":9.99,"currency":"EUR","period":"month"}]},"open_source":false,"grade":"C","src":["S87","S45"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"jobcopilot","name":"JobCopilot","stage":6,"category":"Auto-apply agent","what":"Hosted daily-batch auto-apply","verdict":"avoid","why":"Unattended submission; not audited; competitor-reported pricing","url":"https://jobcopilot.com","status":"operating per roundups (2026)","risk":"weekly billing; reputational","price":null,"open_source":false,"note":"competitor-reported about USD 0.93 a day","grade":"C","src":["S53"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"aiapply","name":"AIApply","stage":6,"category":"Auto-apply agent","what":"Auto-apply with credits plus resume and interview tools","verdict":"avoid","why":"Unattended submission; credits on top of subscription; not audited","url":"https://aiapply.co","status":"operating per roundups (2026)","risk":"layered billing","price":{"free":false,"plans":[{"amount":29,"currency":"USD","period":"month"}]},"open_source":false,"note":"plus credit packs per competitor","grade":"C","src":["S53","S87"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"massive","name":"Massive","stage":6,"category":"Auto-apply agent","what":"Recurring bulk applications","verdict":"avoid","why":"Bulk unattended submission; seen only in roundups; not audited","url":null,"status":"unverified beyond roundups","risk":"unknown terms","price":null,"open_source":false,"grade":"C","src":["S87"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"sonara","name":"Sonara","stage":6,"category":"Auto-apply agent","what":"AI matching and auto-apply","verdict":"avoid","why":"2024 shutdown locked users out; relaunched under BOLD; unattended submission","url":"https://sonara.ai","status":"live under BOLD (as of 2026-10); original service shut 2024-02-01","risk":"shutdown without export history; trial renews","price":null,"open_source":false,"note":"competitor-reported USD 2.95 trial renewing at 23.95","grade":"C","src":["S48","S49","S50"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"scoutify","name":"Scoutify","stage":6,"category":"Auto-apply agent","what":"Alerts, Auto Apply, Sniper on employer ATS","verdict":"avoid","why":"Unattended submission; vendor-only evidence; weekly auto-renew","url":"https://scoutify.com","status":"operating (as of 2026-11-13)","risk":"weekly billing","price":{"free":false,"plans":[{"amount":5,"currency":"USD","period":"week"},{"amount":15,"currency":"USD","period":"week"},{"amount":25,"currency":"USD","period":"week"}]},"open_source":false,"grade":"B","src":["S51","S52","S4"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"indeed-apply-for-me","name":"Indeed Apply For Me","stage":6,"category":"Auto-apply agent","what":"First-party drafting and submission from Indeed profile","verdict":"watch","why":"Limited US test; automatic mode paused 2026-08-04; review-all-drafts mode continues","url":"https://www.indeed.com/news/releases/indeed-tests-apply-for-me-job-search","status":"early test, automatic mode paused (2026-08-04)","risk":"changes without notice","price":null,"open_source":false,"grade":"A","src":["S12","S13"],"as_of":"2026-08-04","ttl":"V2"}
{"type":"tool","id":"indeed-career-scout","name":"Indeed Career Scout","stage":6,"category":"AI job-search agent","what":"First-party career coach and matcher","verdict":"watch","why":"Outcome claims are vendor-only; India availability unverified (preview announced)","url":"https://www.indeed.com","status":"launched US 2025-09; India preview announced","risk":"profile data use","price":null,"open_source":false,"grade":"C","src":["S70","S71"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"general-llm-drafting","name":"General LLM assistants (drafting and rehearsal)","stage":0,"category":"AI assistant","what":"ChatGPT, Claude, Gemini for drafting","verdict":"use-with-care","why":"Field evidence favours non-generative writing help; verify every claim; no hidden text","url":"https://pubsonline.informs.org/doi/fpi/10.1287/mnsc.2024.04528","status":"operating","risk":"fabricated details; COI","price":null,"open_source":false,"grade":"B","src":["S54","S16"],"as_of":"2026-11-13","ttl":"V5"}
{"type":"tool","id":"general-llm-salary-adviser","name":"General LLM assistants as career or salary adviser","stage":0,"category":"AI assistant","what":"Salary targets and negotiation advice","verdict":"avoid","why":"Audits show persona-dependent salary advice, including 2026-era models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11805401/","status":"operating","risk":"biased targets; COI","price":null,"open_source":false,"grade":"B","src":["S55","S56","S57"],"as_of":"2026-11-13","ttl":"V5"}
{"type":"tool","id":"general-browser-agents","name":"General browser agents (Comet, Claude in Chrome, ChatGPT agent, Gemini in Chrome)","stage":0,"category":"Browser agent","what":"Agents that click through sites","verdict":"avoid","why":"For unattended applying: no platform sanctions it, agent traffic is blocked, injection risk; COI for Claude","url":null,"status":"operating per HUMAN Security traffic data (2026-05)","risk":"account restriction; prompt injection","price":null,"open_source":false,"grade":"C","src":["S69","S68"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"chatgpt-atlas","name":"ChatGPT Atlas","stage":0,"category":"Browser agent","what":"OpenAI agentic browser","verdict":"avoid","why":"Discontinued 2026-08-09 and folded into ChatGPT","url":null,"status":"discontinued (2026-08-09)","risk":"product ended","price":null,"open_source":false,"grade":"B","src":["S68"],"as_of":"2026-08-09","ttl":"V2"}
{"type":"tool","id":"jobscan-checker","name":"Jobscan resume checker","stage":6,"category":"Parse and match checker","what":"Keyword match report against a posting","verdict":"use-with-care","why":"Use as a gap list; score not validated against outcomes; 5 free scans a month","url":"https://www.jobscan.co","status":"operating (as of 2026-11-13)","risk":"paid score unlock; billing","price":{"free":true,"plans":[{"amount":49.95,"currency":"USD","period":"month"},{"amount":89.95,"currency":"USD","period":"quarter"}]},"open_source":false,"grade":"C","src":["S42","S43"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"ats-score-checkers","name":"ATS score checkers (class)","stage":6,"category":"Parse and match checker","what":"Match scores from Teal, Resume Worded, Enhancv, others","verdict":"use-with-care","why":"Scores differ by tool and have no outcome link; use as gap lists","url":null,"status":"operating","risk":"false assurance","price":null,"open_source":false,"grade":"C","src":["S61","S62","S43"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"resume-matcher","name":"Resume-Matcher","stage":6,"category":"Parse and match checker","what":"Local gap analysis and builder with LLMs","verdict":"use-with-care","why":"Local; gap list only","url":"https://github.com/srbhr/Resume-Matcher","status":"active (2026-11-07)","risk":"LLM errors","price":{"free":true,"plans":[]},"open_source":true,"note":"Apache-2.0; 29270 stars; last commit 2026-11-07","grade":"A","src":["S81"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"reactive-resume","name":"Reactive Resume","stage":6,"category":"Resume builder (open source)","what":"Builder, self-hostable","verdict":"use-with-care","why":"Active; self-host to control data; hosted retention unverified","url":"https://github.com/AmruthPillai/Reactive-Resume","status":"active (2026-11-12)","risk":"hosted retention unverified","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 45680 stars; last commit 2026-11-12","grade":"A","src":["S77"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"rendercv","name":"RenderCV","stage":6,"category":"Resume builder (open source)","what":"YAML to PDF CV generator","verdict":"use-with-care","why":"Good CV-as-data default; slower maintenance","url":"https://github.com/rendercv/rendercv","status":"last commit 2026-03-25","risk":"slower maintenance","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 17949 stars","grade":"A","src":["S78"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"openresume","name":"OpenResume","stage":6,"category":"Resume builder (open source)","what":"Builder and parser","verdict":"watch","why":"No commit since 2024-10-29","url":"https://github.com/xitanggg/open-resume","status":"stale","risk":"unmaintained","price":{"free":true,"plans":[]},"open_source":true,"note":"AGPL-3.0; 8977 stars","grade":"A","src":["S79"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"json-resume","name":"JSON Resume","stage":6,"category":"Resume builder (open source)","what":"Résumé schema and registry; schema repo moved into monorepo","verdict":"use-with-care","why":"Portable data format; ecosystem uneven","url":"https://github.com/jsonresume/jsonresume.org","status":"active (2026-11-07)","risk":"ecosystem quality varies","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 351 stars in monorepo","grade":"A","src":["S80"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"career-ops","name":"career-ops","stage":6,"category":"Open-source job-search project","what":"Local scan, score, tailor; drafts forms; never submits","verdict":"use-with-care","why":"Human-in-the-loop by design; board scanning may breach site terms","url":"https://github.com/santifer/career-ops","status":"active (2026-11-12)","risk":"board terms; contact discovery out of scope","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 82242 stars","grade":"A","src":["S73"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"aihawk","name":"AIHawk","stage":6,"category":"Open-source job-search project","what":"Auto-apply bot","verdict":"avoid","why":"Auto-submits; unattended; LinkedIn risk","url":"https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk","status":"active (2026-11-12)","risk":"account restriction","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 32498 stars","grade":"A","src":["S74"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"auto-job-applier-linkedin","name":"Auto_job_applier_linkedIn","stage":6,"category":"Open-source job-search project","what":"LinkedIn auto-apply with dry-run option","verdict":"avoid","why":"Core function automates LinkedIn","url":"https://github.com/GodsScion/Auto_job_applier_linkedIn","status":"last commit 2026-09-10","risk":"account restriction","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 3031 stars","grade":"A","src":["S76"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"jobspy","name":"JobSpy","stage":6,"category":"Open-source job-search project","what":"Scraper for LinkedIn, Indeed, Glassdoor, ZipRecruiter, Bayt, Naukri, BDJobs, HelloWork","verdict":"avoid","why":"Scrapes sites whose terms forbid it","url":"https://github.com/speedyapply/JobSpy","status":"active (2026-10-27)","risk":"terms breach; blocks","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 4709 stars","grade":"A","src":["S75","S8","S10"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"jobsync","name":"JobSync","stage":6,"category":"Application tracker","what":"Self-hosted tracker","verdict":"watch","why":"Assessed on metadata only","url":"https://github.com/Gsync/jobsync","status":"active (2026-10-30)","risk":"not assessed","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 1525 stars","grade":"A","src":["S82"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"beamapply","name":"BeamApply","stage":6,"category":"Application autofill","what":"Open-source Greenhouse autofill for Firefox","verdict":"watch","why":"Small project; developer states no data collection; not audited","url":"https://addons.mozilla.org/en-US/firefox/addon/beamapply/","status":"v1.3.0 updated 2026-09-05","risk":"unaudited","price":{"free":true,"plans":[]},"open_source":true,"note":"GPL-3.0 per listing","grade":"B","src":["S84"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"browser-use","name":"browser-use","stage":0,"category":"Browser agent","what":"General browser-agent framework","verdict":"watch","why":"Generic; job use depends on each site's terms","url":"https://github.com/browser-use/browser-use","status":"active (2026-11-12)","risk":"terms; injection","price":{"free":true,"plans":[]},"open_source":true,"note":"MIT; 120863 stars","grade":"A","src":["S83"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"indeed-mcp","name":"Indeed MCP (official)","stage":6,"category":"MCP server","what":"Search, job detail, resume read and company data in Claude","verdict":"use-with-care","why":"Official, read-only, beta, Claude-only; reads your Indeed profile; COI","url":"https://docs.indeed.com/mcp/","status":"beta (as of 2026-11-13)","risk":"profile read; docs list four tools, a directory lists two","price":{"free":true,"plans":[]},"open_source":false,"grade":"A","src":["S26","S27","S96"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"greenhouse-mcp","name":"Greenhouse MCP","stage":6,"category":"MCP server","what":"Employer-side access to jobs, candidates, scorecards","verdict":"watch","why":"Open beta for admins; not for job seekers","url":"https://www.greenhouse.com/newsroom/greenhouse-launches-mcp-giving-hiring-teams-a-governed-way-to-connect-ai-tools-to-greenhouse","status":"open beta (2026-07)","risk":"employer data","price":null,"open_source":false,"grade":"B","src":["S23","S24"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"workable-mcp","name":"Workable MCP Server","stage":6,"category":"MCP server","what":"Employer-side recruiting and HR access; OAuth2 custom connector; 94 tools by 2026-07-20","verdict":"watch","why":"Employer-side read and write access; not for job seekers","url":"https://resources.workable.com/workable-mcp-server","status":"expanded to 94 tools (2026-07-20)","risk":"employer data","price":null,"open_source":false,"note":"vendor says available to all customers on all plans","grade":"B","src":["S31","S90"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"getonbrd-mcp","name":"Get on Board MCP Server","stage":6,"category":"MCP server","what":"Board-run MCP; candidate profiles readable from 2026-10","verdict":"watch","why":"Employer-side talent database; seeker use unverified","url":"https://www.getonbrd.com/product_updates/mejores-publicaciones-en-google-jobs-y-perfiles-en-el-servidor-mcp","status":"operating (2026-10)","risk":"profile data exposure","price":null,"open_source":false,"grade":"B","src":["S95"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"linkedin-mcp-server","name":"linkedin-mcp-server (stickerdaniel)","stage":6,"category":"MCP server","what":"LinkedIn profiles, jobs, messages through your browser session","verdict":"avoid","why":"Automates a logged-in LinkedIn session; imports browser cookies; platform does not permit","url":"https://github.com/stickerdaniel/linkedin-mcp-server","status":"active (2026-11-13)","risk":"account restriction; credential exposure; can message and connect","price":{"free":true,"plans":[]},"open_source":true,"note":"Apache-2.0; 4202 stars; sponsored by Unipile","grade":"A","src":["S28","S8"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"scraper-backed-job-mcp","name":"Scraper-backed Indeed and LinkedIn MCP servers (class)","stage":6,"category":"MCP server","what":"HasData, Apify and similar hosted scrapers exposed as MCP","verdict":"avoid","why":"Scrape sites whose terms bar it; vendor API keys","url":"https://mcpservers.org/servers/hasdata/indeed-mcp","status":"operating","risk":"terms breach","price":null,"open_source":false,"grade":"C","src":["S86","S11"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"adzuna-mcp","name":"adzuna-mcp (community, Jayesh-Kr)","stage":6,"category":"MCP server","what":"Adzuna search and salary data through your own keys","verdict":"use-with-care","why":"Uses an official API; within Adzuna terms; rate limits","url":"https://glama.ai/mcp/servers/Jayesh-Kr/adzuna-mcp/tree","status":"operating","risk":"free-tier limits","price":{"free":true,"plans":[]},"open_source":true,"note":"12 countries per listing, including India","grade":"C","src":["S85","S32"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"adzuna-api","name":"Adzuna API","stage":6,"category":"Job-data API","what":"Search, salary and histogram endpoints","verdict":"use-with-care","why":"Personal job search permitted; free tier for evaluation; commercial use needs agreement","url":"https://developer.adzuna.com","status":"operating","risk":"limits; one account only","price":{"free":true,"plans":[]},"open_source":false,"note":"India (in) appears in third-party country lists (S85, S100); counts differ and Adzuna's own country page was not opened","grade":"A","src":["S32","S38","S85","S100"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"usajobs-api","name":"USAJOBS API","stage":6,"category":"Job-data API","what":"US federal job announcements","verdict":"use","why":"Official; free key; email User-Agent","url":"https://developer.usajobs.gov","status":"operating","risk":"US federal only","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S33"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"reed-api","name":"Reed Jobseeker API","stage":6,"category":"Job-data API","what":"UK job search and details","verdict":"use","why":"Official; free key; basic auth","url":"https://www.reed.co.uk/developers/jobseeker","status":"operating","risk":"UK only","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S34"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"jooble-api","name":"Jooble REST API","stage":6,"category":"Job-data API","what":"POST search over aggregated listings; key issued on request","verdict":"use-with-care","why":"Official free key; terms of use on its about page not read; limits per key","url":"https://jooble.org/api/about","status":"operating (as of 2026-11-13)","risk":"terms unread; key sits in the URL path","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S93"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"remotive-api","name":"Remotive API","stage":6,"category":"Job-data API","what":"Remote job feed","verdict":"use-with-care","why":"24-hour delay; 4 calls a day advised; attribution; no resubmission","url":"https://github.com/remotive-com/remote-jobs-api","status":"operating","risk":"thin feed","price":{"free":true,"plans":[]},"open_source":false,"grade":"A","src":["S35"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"arbeitnow-api","name":"Arbeitnow API","stage":6,"category":"Job-data API","what":"Europe and remote feed, no key","verdict":"use-with-care","why":"Free; terms not read","url":"https://arbeitnow.com/blog/job-board-api","status":"operating","risk":"terms unread","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S37"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"careerjet-api","name":"Careerjet API","stage":6,"category":"Job-data API","what":"90-country search for publishers","verdict":"use-with-care","why":"Each call must carry a real visitor IP and user agent","url":"https://www.careerjet.im/partners/api","status":"operating","risk":"unsuitable for personal scripts","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S36"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"ats-board-apis","name":"Greenhouse, Lever and Ashby public board APIs","stage":6,"category":"Job-data API","what":"Unauthenticated GET endpoints per company board","verdict":"use","why":"Documented for job-board publishing; good for company watchlists","url":"https://developers.greenhouse.io/job-board.html","status":"operating (verified live 2026-08-21)","risk":"per-company only","price":{"free":true,"plans":[]},"open_source":false,"grade":"C","src":["S39","S40"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"indeed-hiring-lab-data","name":"Indeed Hiring Lab job postings index","stage":1,"category":"Labour-market data","what":"Daily postings index, refreshed weekly","verdict":"use","why":"Primary dataset, CC-BY-4.0; no India series","url":"https://github.com/hiring-lab/job_postings_tracker","status":"updated 2026-11-12","risk":"no India coverage","price":{"free":true,"plans":[]},"open_source":true,"note":"CC-BY-4.0; 225 stars","grade":"A","src":["S72"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"bls-public-data-api","name":"BLS Public Data API","stage":1,"category":"Labour-market data","what":"US labour series including OEWS wages, CPS and JOLTS","verdict":"use","why":"Official US source; free v2 key gives 500 queries a day, 50 series a query, 20 years; US only","url":"https://www.bls.gov/developers/api_FAQs.htm","status":"operating (as of 2026-11-13)","risk":"yearly key renewal; no postings data; no India coverage","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S91"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"tool","id":"onet-web-services","name":"O*NET Web Services","stage":1,"category":"Labour-market data","what":"US occupation skills, tasks and technologies via a free account","verdict":"use","why":"Official US source; publishable with attribution, site registration and unaltered data","url":"https://services.onetcenter.org/help/license_data","status":"operating (as of 2026-11-13)","risk":"attribution duties; US occupations only","price":{"free":true,"plans":[]},"open_source":false,"grade":"B","src":["S92"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"tracking","tactic":"Log every submission with date, CV version, ATS and source","claim":"A complete log is the only outcome data a job seeker controls","evidence":"Huntr's analyses rest on user logs; Huntr cannot observe how applications were sent","verdict":"use","risk":"time cost","grade":"P","src":["S16"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"autofill","tactic":"Autofill only on employer-hosted forms; read every answer; click Submit yourself","claim":"Human submission keeps accuracy and platform-terms risk low","evidence":"Simplify, Indeed and Jobscan all keep or return to a review step","verdict":"use-with-care","risk":"misfilled fields","grade":"B","src":["S1","S12","S41"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"platform-terms","tactic":"Do not run bots, clicking extensions or scrapers on linkedin.com or indeed.com","claim":"Both prohibit third-party automation","evidence":"LinkedIn help; Indeed India help","verdict":"avoid","risk":"account restriction","grade":"B","src":["S8","S10"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"volume","tactic":"Prefer fewer, targeted applications and avoid unattended modes","claim":"Per-application yield falls with volume; totals can rise","evidence":"Huntr: 8.0% vs 2.4% interview rate; 72.0% vs 47.8% with at least one interview","verdict":"use-with-care","risk":"correlational data","grade":"B","src":["S16"],"as_of":"2026-11-13","ttl":"V3"}
{"type":"practice","area":"accuracy","tactic":"Check every AI-drafted answer against your record","claim":"AI drafts can add false details","evidence":"Huntr reports that most surveyed AI users saw invented details","verdict":"use","risk":"time cost","grade":"C","src":["S16"],"as_of":"2026-11-13","ttl":"V3"}
{"type":"practice","area":"integrity","tactic":"Never hide instructions in a résumé","claim":"Hidden prompts are measurable and employers react","evidence":"About 1% of 196,682 résumés; employers report blocking reapplication","verdict":"avoid","risk":"rejection; reputation","grade":"B","src":["S58","S60"],"as_of":"2026-11-13","ttl":"V3"}
{"type":"practice","area":"checkers","tactic":"Use ATS checkers as gap lists and paste-test exported text","claim":"Scores are not validated against outcomes","evidence":"No independent study found; vendor tests disagree","verdict":"use-with-care","risk":"false assurance","grade":"C","src":["S43","S61","S62"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"data-portability","tactic":"Keep a local CV source file and export before any shutdown","claim":"Tool closures can lock out your data","evidence":"Sonara's 2024 shutdown","verdict":"use","risk":"none","grade":"C","src":["S48","S49"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"agents","tactic":"Never give an agent or MCP server your LinkedIn cookies or password; treat posting text as untrusted","claim":"Session-based servers import cookies; agentic browsers show injection weaknesses","evidence":"linkedin-mcp-server README; Atlas proof of concept","verdict":"avoid","risk":"credential exposure","grade":"B","src":["S28","S68"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"practice","area":"billing","tactic":"Choose monthly or quarterly plans, set a cancellation date, avoid weekly auto-renew","claim":"Weekly plans raise cost for long searches","evidence":"Teal $13 a week versus $29 a month; Scoutify weekly auto-renew","verdict":"use-with-care","risk":"charges after the sprint","grade":"B","src":["S18","S51"],"as_of":"2026-11-13","ttl":"V2"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Independent outcome study of any auto-apply category","searched":"Huntr reports; academic phrasing; roundups","note":"Only vendor claims found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Official LinkedIn MCP or job-search API for individuals","searched":"MCP directories; two secondary guides","note":"Secondary sources say none; LinkedIn primary not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Workday, Lever and Ashby terms on automated applications","searched":"Not retrieved","note":"Open item"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Own-page pricing for LoopCV, JobCopilot, AIApply, Massive, FastApply","searched":"Competitor pages only","note":"Prices are competitor-reported"}
{"type":"absence","grade":"E","src":["S88","S89"],"as_of":"2026-11-13","item":"Simplify+ prices on Simplify's own help page","searched":"Help article read; extract did not show amounts","note":"Two third parties agree on 19.99, 39.99 and 89.99 USD"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Teal, Huntr and Jobscan extension permissions and retention terms","searched":"Policies not opened","note":"Open item"}
{"type":"absence","grade":"E","src":["S93"],"as_of":"2026-11-13","item":"Jooble terms-of-use text and per-key limits","searched":"Help-centre documentation as extract","note":"Terms live on its about page, not read"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Job-posting prompt injection against applicant agents","searched":"One search","note":"Only résumé-side injection found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"NCS (India) API for jobseekers","searched":"One search","note":"Advisory only"}
{"type":"absence","grade":"E","src":["S67"],"as_of":"2026-11-13","item":"Naukri public API","searched":"One commercial source (C)","note":"Reported none"}
{"type":"absence","grade":"E","src":["S72"],"as_of":"2026-11-13","item":"India series in Indeed Hiring Lab data","searched":"Repository folder listing","note":"No IN folder"}
{"type":"absence","grade":"E","src":["S85","S100"],"as_of":"2026-11-13","item":"Adzuna official country list (India coverage)","searched":"Third-party listings only","note":"India appears in several listings; counts differ from 12 to 25"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Other labour-market tools (Lightcast, Levels.fyi data)","searched":"Not checked","note":"Open item"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Jobright and Careerflow status","searched":"Not verified","note":"Open item"}
{"type":"repo_delta","grade":"B","src":["S16","S12","S13","S25"],"as_of":"2026-11-13","k":"K1","verdict":"updated","finding":"Per-application yield falls with volume but totals can rise; Indeed paused its own automatic mode; no independent study","suggested":"Reword as: no independent evidence of benefit; yield per application falls with volume"}
{"type":"repo_delta","grade":"B","src":["S1","S12","S41"],"as_of":"2026-11-13","k":"K2","verdict":"confirmed","finding":"Review-and-submit remains the pattern; do not run autofill extensions on linkedin.com or indeed.com","suggested":"Add the platform exception"}
{"type":"repo_delta","grade":"A","src":["S14","S15"],"as_of":"2026-11-13","k":"K3","verdict":"confirmed","finding":"Ashby documents duplicate merging and Application Limits"}
{"type":"repo_delta","grade":"B","src":["S8","S9"],"as_of":"2026-11-13","k":"K4","verdict":"confirmed","finding":"LinkedIn help bars bots and extensions that automate; seen as extract"}
{"type":"repo_delta","grade":"C","src":["S43","S61","S62"],"as_of":"2026-11-13","k":"K5","verdict":"confirmed","finding":"No independent study; vendor tests show scores diverging"}
{"type":"repo_delta","grade":"B","src":["S16","S17"],"as_of":"2026-11-13","k":"K6","verdict":"updated","finding":"K6 figures match Q1 2026; Q3 2026 gives 8.0% vs 2.4%, plus at-least-one-interview 47.8% vs 72.0%","suggested":"Cite Q3 2026 with both measures"}
{"type":"repo_delta","grade":"B","src":["S54"],"as_of":"2026-11-13","k":"K7","verdict":"confirmed","finding":"Management Science 2025: 8% more hires for non-generative writing help; second half of K7 not verified"}
{"type":"repo_delta","grade":"B","src":["S55","S56","S57"],"as_of":"2026-11-13","k":"K8","verdict":"confirmed","finding":"Audits extend to 2026-era models; COI as Claude was audited"}
{"type":"repo_delta","grade":"B","src":["S5","S6","S1"],"as_of":"2026-11-13","k":"K9","verdict":"confirmed","finding":"Copilot human-submit; same account carries Autopilot"}
{"type":"repo_delta","grade":"A","src":["S21","S22"],"as_of":"2026-11-13","k":"K10","verdict":"confirmed","finding":"Free, global; profile can be recommended to employers"}
{"type":"repo_delta","grade":"B","src":["S19","S20"],"as_of":"2026-11-13","k":"K11","verdict":"confirmed","finding":"Free tier plus Pro $40, $90, $160"}
{"type":"repo_delta","grade":"A","src":["S18"],"as_of":"2026-11-13","k":"K12","verdict":"updated","finding":"Teal+ is $13 a week, $29 a month, $79 a quarter","suggested":"Replace $9 a week"}
{"type":"repo_delta","grade":"B","src":["S44","S45","S8","S10"],"as_of":"2026-11-13","k":"K13","verdict":"confirmed","finding":"Operating; Indeed also bars third-party bots"}
{"type":"repo_delta","grade":"A","src":["S1","S2","S3"],"as_of":"2026-11-13","k":"K14","verdict":"updated","finding":"Help centre no longer says beta; 20 credits a week; no review step; stops if an answer cannot be determined","suggested":"Drop the unverified failure-rate wording"}
{"type":"repo_delta","grade":"B","src":["S41","S42"],"as_of":"2026-11-13","k":"K15","verdict":"updated","finding":"Verified: review by default, optional auto-submit, Lever and Workable at launch","suggested":"Verdict watch"}
{"type":"repo_delta","grade":"C","src":["S46","S53","S87"],"as_of":"2026-11-13","k":"K16","verdict":"confirmed","finding":"The 3 of 8 claim is FastApply's own test; services operating"}
{"type":"repo_delta","grade":"C","src":["S48","S49","S50"],"as_of":"2026-11-13","k":"K17","verdict":"confirmed","finding":"Live under BOLD per a reading of Sonara's footer; one competitor dissents"}
{"type":"repo_delta","grade":"B","src":["S51","S52","S4"],"as_of":"2026-11-13","k":"K18","verdict":"confirmed","finding":"Operating; $5, $15, $25 weekly; evidence vendor-only"}
```
