---
id: "T0-62"
title: "Role Group Dossier: Solutions, Enablement and AI Product Engineering"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-group-solutions-enablement-product-engineering"
tags: ["role-dossier", "ai-solutions-architect", "ai-enablement-engineer", "ai-product-engineer", "job-postings", "india", "pay", "skills"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and page fetch. Anthropic's own postings and Claude products appear in the sample and are marked COI."
evidence_window: "2025-01-10 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 43
---

# T0-62: Role Group Dossier: Solutions, Enablement and AI Product Engineering

S-numbers (S1–S58) point to the Sources & Evidence Ledger. Grades follow the protocol: A is a primary page I opened; B is platform data, an aggregator mirror, or a search extract of a primary page; C is third-party analysis or a prep vendor; D is recalled or a single anecdote; M is my own calculation (it inherits the weakest input); P is practice-curated; E is an absence. The brief anchors the research at 2026-11-11. My retrieval clock read 2026-11-13, which is the date on every `seen` and `retrieved` field. I applied the 90-day posting window from the anchor (postings dated on or after 2026-08-13), and accepted an older posting only where the page was demonstrably live on 2026-11-13. `must` and `nice` entries in `jd` records are condensed paraphrases, not verbatim text, because of quotation limits. Every skill share is a floor: for most postings I saw an extract, not the full page. Anthropic is the developer of the model that wrote this dossier, so its postings are marked COI.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | AI Solutions Architect jobs are mostly pre-sales roles at AI vendors and delivery-architecture roles at consultancies; US posted base pay sits between $150K and $250K | 0.70 | D |
| P2 | "AI Enablement Engineer" is a small title (under 100 postings per 90 days) that mostly means internal adoption and training, not engineering | 0.55 | D |
| P3 | "AI Product Engineer" postings are mostly full-stack roles at startups, and visible AI-frontend roles skew senior | 0.60 | D |
| P4 | Certifications appear in under 10% of postings for these roles, mainly in cloud-partner channels | 0.70 | D |
| P5 | India pay for AI solutions architects runs ₹25–60 lakh a year, well below US pay | 0.60 | D |
| P6 | Frontier labs have renamed pre-sales solutions architects "Applied AI Architect" | 0.65 | D |

## Research Question

**Decision question.** What must the knowledge base record about AI / GenAI Solutions Architect, AI Enablement Engineer and AI Product Engineer (AI Frontend) so that it can tell a job seeker what the job is, what it pays, what it demands, how it is interviewed, how it progresses and where it is?

**Sub-questions.**
- Q1: Definition, variants and aliases.
- Q2: Demand, trend and mix.
- Q3: Skills, with shares and suggested tiers.
- Q4: Pay, including India.
- Q5: Loop, proof of work, credentials, entry routes and progression.
- Q6: Geography, sponsorship, résumé signals and India.

**Reading chosen for ambiguity.**
- "AI Product Engineer (AI Frontend)" is read as the product-engineering family: Product Engineer with AI features, AI Frontend Engineer, Frontend Engineer (AI). The exact AI-frontend title is rare.
- "AI Enablement Engineer" is read as the exact title plus close variants (Lead, Specialist, Platform Engineer Lead – AI Enablement).

**Method.**
- 33 web searches (extended mode for posting discovery) and 11 page-fetch attempts. 8 fetches were read in full: Anthropic London, Fabletics, Xensam, Within (YC page), Sofi (via mirror), Skillenai ×2 and Axial. 3 failed: Amazon jobs (client error), a second Greenhouse page (bot block) and an Ashby page (client error).
- Sample: search-indexed postings from employer boards (Greenhouse, Ashby, Workday, Teamtailor, Google, Accenture and Databricks careers, YC), mirrors (zapply, freehire, jobfound, Built In) and Hacker News threads. Included postings: 23 Solutions Architect, 15 Enablement, 16 Product Engineer.
- Each posting is classified by what it asks for, not by its title.
- Exclusions (counts in each role's sample summary): SA 8 of 31 candidates; Enablement 9 of 24; Product Engineer 16 of 32.
- Bias: search engines favour large employers and English-language pages. Greenhouse, Ashby and YC boards are over-represented; Workday, Taleo and Indian ATS boards are under-represented. A query for "Agentic AI Architect" inflates the agentic share for SA. Shares carry roughly ±20–25 percentage points at n = 15–23, so they are a cross-check on platform shares, not a measurement.
- Falsification searches:
  - Evidence that Enablement is a growing title (found a decline).
  - Evidence that Big Tech or frontier labs post the Enablement title (found none).
  - Evidence that certifications are demanded (found 1 of 23 SA postings).
  - Evidence that AI-frontend demand is senior-only (found mid-level Product Engineer roles).
  - Evidence that SA titles persist unchanged at labs (found renaming).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | The SA job splits into pre-sales/field work (15 of 23 sampled postings, 65.2%) and delivery, customer-success or consulting architecture (8, 34.8%). Frontier labs use "Applied AI Architect" in 4 of their 7 sampled postings. | Sample n = 23 [S1, S3, S5, S7–S15]. OpenAI's Applied AI Architect owns the customer's technical path from pre-sales discovery to production adoption while delivery teams implement [S3]. Microsoft's agentic CSA role sits in a customer-success unit [S8]. | M (inputs A/B) |
| KF2 | Experience gate: median stated minimum is 6.5 years (n = 10, range 3–10). Anthropic asks 5+ years (10+ in India). Microsoft posted an entry-level CSA on 2026-11-10. EY France labels 3–7-year engineering work "architect". | Anthropic London and India postings [S1]; Microsoft entry-level CSA [S8]; EY France [S13]. | M |
| KF3 | SA pay: US posted ranges $152K–$248K (Google $152–221K plus a 42.86% bonus target; Databricks $180–247.5K; AWS $153.6–239K). Anthropic London £165–190K OTE. Axial median posted pay $189K. Levels.fyi US median total compensation $220K (n = 1,200). Databricks L3→L6 total compensation $218K→$359K. OpenAI: one reported $418K. | [S1, S6, S7, S10, S18, S27] | B |
| KF4 | SA demand has no exact "AI Solutions Architect" count. Proxies: 16,927 US "AI architecture" postings since January 2026 (+24% quarter on quarter, Axial) and JobsPipe's 1,515 live US SA postings against 64 in India. | [S18, S24]. The Axial class is broader than the role; the JobsPipe SA count is not AI-specific. | B |
| KF5 | SA skills: customer-facing technical experience in 22 of 23 postings, pre-sales in 14, cloud in 12 (52.2%), AWS in only 6. Certifications are named in 1 of 23 (3 of 25 in-window postings read). Axial: AWS Solutions Architect certification in 1.7% of US AI-architecture postings. | Sample [S1–S15]; Axial [S18]. | M/B |
| KF6 | "AI Enablement Engineer" is a small and falling exact title: 57 postings in the 90 days to 2026-09-03 (down 35% on the prior four weeks), then 42 in the 90 days to 2026-11-05. 26 "AI Enablement Lead" postings (to 2026-09-02). No employer holds more than 3. About 1.0% of Skillenai's "AI Engineer" count (4,139). | [S20, S21, S22] | B (ratio M) |
| KF7 | Enablement has three variants: adoption/training lead (3 of 15, 20%), builder-enabler (9, 60%) and platform/MCP/context engineering (3, 20%). MCP is named in 4 of 15 (26.7%; platform 19.0%). Searches found no frontier-lab or Big Tech posting under the title; enterprises, public-sector bodies and contract trainer roles dominate. | Sample [S33–S45]; [S20]; [S58]. | M/B |
| KF8 | Enablement pay is bimodal: $160,378–$180,000 base for a builder role (5 years) against $120–140K for a bank adoption role (mirror); a London platform lead is offered up to £130K plus about 20% bonus; an India junior role pays ₹8–14 LPA. | [S33, S36, S44, S42] | A/B |
| KF9 | "AI Product Engineer" is not one title. Of 16 sampled postings, 7 are Product Engineer roles shipping AI features, 5 are AI-facing UI specialists, 2 are AI-native design/frontend roles and 2 are full-stack roles with AI-chat experience. React 93.8% (floor), TypeScript 81.3%, LLM-API integration 68.8%, streaming UX 25.0%, evals 0 of 16. | Sample [S1, S4, S49–S53] | M |
| KF10 | AI-frontend seniority is mixed. Median stated minimum is 2 years (n = 6). Within's Staff AI Frontend role asks 6+ years, pays $235–315K and requires US work authorisation. Junior India roles pay ₹4–18 LPA. | [S49, S51, S53] | A/M |
| KF11 | Certifications are a weak hiring signal in all three roles: 1 of 23 SA, 1 of 15 Enablement (generic "related certifications"), 0 of 16 Product Engineer. AWS AIP-C01 ($300, 75 questions, 180 minutes), Microsoft AI-103 (replaces AI-102, retired 2026-06-30) and Google PMLE ($200, 2 hours, 50–60 questions) exist. | [S31, S32, S37, S57] | B/M |
| KF12 | SA loops add a customer-scenario or presentation round (Anthropic, OpenAI, Databricks). AI-frontend loops ask candidates to build streaming chat UIs or complete take-homes. No Enablement loop reports were found. | [S30, S54]. Prep-vendor sources; COI. | C |
| KF13 | Sponsorship and geography: Anthropic states it sponsors visas; Within is US citizen/visa only; Google Singapore prioritises candidates with an existing right to work. Databricks' FY2026 LCA snapshot lists 145 SA, Specialist SA and Senior SA positions (plus 46 Resident and 37 Delivery SA). OpenAI shows certified SA LCAs at $278–290K. Axial: California 19% and Texas 13% of US AI-architecture postings. India's SA live count is about 4% of the US count. | [S1, S7, S49, S56, S18, S24]. LCA wages are filed wages, not pay. | A/B |
| KF14 | India SA pay is ₹31.9–49.2L across 6–12+ years (AmbitionBox via upGrad), with ₹55–80L+ at top GCC and product employers. A Cognizant AIML SA posting shows ₹39–56 LPA. | [S14, S29] | C |

## Recommendation

| Rule | Action | Failure mode | What would change it |
|---|---|---|---|
| R1 | With 5+ years in customer-facing technical roles (SA, SE, TAM, FDE) or consulting plus hands-on LLM delivery, apply to pre-sales SA / Applied AI Architect roles at labs, hyperscalers and data platforms. Prepare an eval-backed demo and a customer-scenario walkthrough. | OTE ranges overstate base. Posting dates are unverified for 13 of 23 sampled postings. Labs gate at 5+/10+ years and expect office presence. | An exact-title count showing under 100 postings; LCA data showing few sponsored filings. |
| R2 | With under 5 years, target Microsoft's entry-level CSA, consultancy architect/engineer roles (EY France 3–7 years), builder-enabler roles or Product Engineer roles. | Title inflation ("architect" for engineer work) and low pay (Microsoft Belgium €55.4–93.7K base). | Entry-level SA postings appearing at labs. |
| R3 | A backend, DevEx or SRE candidate with IAM and API-gateway skills should target the Enablement platform variant (MCP gateway, SSO/OAuth). Show a shipped MCP server or gateway pilot with usage numbers. | The exact title is tiny and falling (42 postings per 90 days). Employers are regulated and few. | Skillenai count above 60 per 90 days; frontier-lab postings appearing. |
| R4 | A non-technical operations candidate can pursue the adoption variant (about $120–140K in the one priced posting). Keep a route to the builder variant. | Likely transitional: it follows vendor copilot rollouts. | Adoption-lead postings with budgets above $140K. |
| R5 | A frontend or full-stack candidate should headline as "Product Engineer / Full-stack AI engineer" (React, TypeScript, LLM APIs). Show streaming UI with cancel, retry and error states, plus accessibility. | "AI Frontend" can mean a design-engineer role (Within). Generic UI is exposed to code generation. Work authorisation can block US roles. | A title-level count showing AI-frontend postings growing. |
| R6 | India-based: SA at Google, Anthropic India or Databricks needs about 10+ years. Otherwise target consultancies and GCCs (₹30–56L). Product Engineer: ₹4–18L early career. | Low volume (JobsPipe 64 SA live). IT-services pay is lower. | A posting pull showing more senior openings in India. |
| R7 | Skip certifications unless targeting Microsoft, AWS or Google partner channels. | Cost ($300 AIP-C01; $200 PMLE) for a signal present in about 4% of SA postings. | Employers listing certifications as requirements. |

## Alternatives Considered

| Option | Verdict |
|---|---|
| Use platform title counts (Axial, Skillenai) as the demand measure | Rejected as sole source: class definitions differ and coverage changes (Skillenai "Solutions Architect" 1,684 → 3,430 reflects coverage, not trend). Kept as proxies. |
| Sample through public ATS board endpoints | Preferred but unavailable here: Amazon, Greenhouse and Ashby fetches failed. Used search-indexed extracts instead. |
| Merge the three roles into FDE / Applied AI | Rejected. FDE is an adjacent role (Skillenai FDE 1,734 per 90 days) that deserves its own page. |
| Treat AI Product Engineer as AI-frontend only | Rejected: the exact title is too rare; the product-engineering family is the usable unit. |
| Use LCA filings as pay evidence | Rejected by protocol rule 2 (filings are not pay). Used only for sponsorship signals. |
| Use Levels.fyi as primary pay | Kept as secondary: AI-specific titles are not tracked and n is small. |

## Detailed Findings

### A. AI / GenAI Solutions Architect (`ai-solutions-architect`)

**A1. Definition, variants, aliases (probe: pre-sales vs delivery).** Two jobs share the title. The pre-sales job sells and de-risks a vendor's models or platform through technical discovery, demos and evaluations. The delivery job designs and governs a customer's AI solution inside an integrator or a vendor's customer-success unit.

| Employer family | Title in sample | Orientation | Evidence |
|---|---|---|---|
| Anthropic | Applied AI Architect; Solutions Architect, Applied AI | Pre-sales; partner and public-sector variants; manager track | S1 |
| OpenAI | Applied AI Architect; Solutions Architect; AI Deployment Engineer | Pre-sales to production ownership; delivery teams implement | S3, S16 |
| AWS | (Sr.) GenAI Specialist Solutions Architect | Pre-sales specialist, go-to-market | S5 |
| Google Cloud | (AI) Customer Engineer | Pre-sales with technical sales teams | S7 |
| Microsoft | Cloud Solution Architect (AI, Agentic, Copilot) | Post-sales customer success; an entry-level version exists | S8 |
| Databricks | (Sr.) Specialist Solutions Architect AI/ML | Field-engineering specialist | S9, S10 |
| Consultancies | AI Architect (Accenture, Capgemini, EY, PwC); AIML SA (Cognizant) | Delivery architecture | S11–S14 |
| AI-native services | AI Solutions Architect (Tribe AI) | Pre-sales to delivery handoff | S15 |

Alias counts in the sample (n = 23): Applied AI Architect 4; Solutions Architect (Applied AI / Technical Success) 3; Specialist SA 4; Customer Engineer 3; Cloud Solution Architect 3; (Agentic / GenAI / Enterprise) AI Architect 4; AIML Solution Architect 1; AI Solutions Architect 1. "Agent Architect (exact)" was not found in the window. "Principal AI Architect – Agentic" appears only in an expired Accenture Poland posting (S17).

Boundary with the Forward Deployed Engineer: Anthropic's Startups role lists FDE as a qualifying background, and Skillenai counts 1,734 FDE postings per 90 days (S22). FDE belongs on its own page.

**A2. Demand.**

| Measure | Value | Source and date | Grade |
|---|---|---|---|
| US "AI architecture" postings since 2026-01 | 16,927; +24% quarter on quarter | Axial, updated 2026-08-25 [S18] | B (proxy) |
| Employer mix (Axial, US) | IT services 23%, technology 22%, professional services 22%; 44% from firms above 10,000 staff; contract 15% | S18 | B |
| JobsPipe live SA postings | US 1,515; India 64; global 2,718; senior 1,125 | Retrieved 2026-11-13, page undated; the US figure equals the KB's 2026-11-02 value [S24] | B |
| Skillenai "Solutions Architect" per 90 days | 3,430 (roles page, retrieved 2026-11-13); 1,684 (90 days to 2026-08-01, +25% on the prior four weeks); "Solution Architect" 2,335 | S22, S23 | B (coverage changed; not a trend) |
| corvi SA category (snapshot 2026-07-05) | US 1,347; India 761; Bengaluru 325; London 162 | S25 | C |
| Exact "AI Solutions Architect" count | Not found | Absence | E |
| Employer mix, sample n = 23 | frontier labs 7; Big Tech 8; AI/data platform 2; consultancies 5; AI-native 1 | Sample | M |
| Seniority | Axial: 45% mid-level IC, 9% Principal, about 5% Director+. Sample: title or level flags senior seniority in 8 (Sr., Senior, level III, Advanced, Associate Director), entry in 1, nothing in 14; median stated minimum 6.5 years | S18; sample | M |
| Remote share | Axial: mostly hybrid, no share given. Sample: not measurable (Anthropic expects office ≥25%; Public Sector is on-site) | S1, S18 | B |
| Trend | Axial +24% quarter on quarter (US AI architecture); no exact-title series | S18 | B |

**A3. Skills (n = 23; shares are floors from extracts; ±20 points).**

| Skill | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| new:customer_facing_technical | 95.7% (22) | 23 | Must (new) | none | The explicit gate at labs and vendors (5+ or 10+ years). |
| presales | 60.9% (14) | 23 | Must | Important | Defines 65% of postings; delivery variants differ. |
| cloud | 52.2% (12) | 23 | Must | Must | Named in hyperscaler and consultancy postings, not in lab extracts. |
| agents | 56.5% (13) | 23 | Important | none | Mechanical Must; held at Important because my "agentic" queries inflate it. |
| azure | 30.4% (7) | 23 | Important | Important | KB platform share 29.5%. |
| gcp | 30.4% (7) | 23 | Important | Important | KB platform share 22.6%. |
| aws | 26.1% (6) | 23 | Important | Must | KB share 53.6% not replicated; generic cloud is the Must. |
| new:rag | 26.1% (6) | 23 | Important | none | In the interview track but not on the skill card. |
| managed_ai | 21.7% (5) | 23 | Should | Important | Named platforms only (Vertex, Foundry, Copilot Studio). |
| evals | 17.4% (4) | 23 | Should | none | Anthropic, OpenAI, Databricks, Tribe AI. |
| grc | 17.4% (4) | 23 | Should | Important | OpenAI, Capgemini, PwC. |
| guardrails | 8.7% (2) | 23 | Optional | none | Databricks only. |
| mcp | 4.3% (1) | 23 | Optional | none | Accenture only. |
| iam; model_selection; cost_latency | 4.3% each (1) | 23 | Should (floor) | Important | PwC only; keep the KB tier until a full-text read. |
| new:certification_named | 4.3% (1) | 23 | Optional | Optional | 3 of 25 in-window postings read. |

Python, communication, leadership and mentoring are not measurable from truncated extracts. Platform cross-check (Axial, n = 16,927 US postings): cloud 62%, Python 44%, observability 39%, foundation models 38% [S18].

**A4. Pay.**

| Population | Statistic | Component | n | Date | Source |
|---|---|---|---|---|---|
| Google CE III Cloud AI, US | $152,000–$221,000 range, plus 42.86% bonus target and equity | base | 1 | 2026-11-13 | S7 |
| Databricks SSA AI/ML, US | $180,000–$247,500 range ("Local Pay Range"; OTE not stated) | base | 1 | 2026-08-14 | S10 |
| AWS GenAI SSA, Seattle/Dallas and Santa Clara | $153,600–$207,800; $176,600–$239,000 | base | 1 | 2026-11-13 | S6 |
| Anthropic Startups, London | £165,000–£190,000 | OTE (includes commission) | 1 | 2026-11-13 | S1 |
| Microsoft CSA IC3, Belgium | €55,400–€93,700 | base | 1 | 2026-10-11 | S8 |
| AI architecture, US | p50 $189,000 | posted bands | 16,927 postings | 2026-08-25 | S18 |
| Solution Architect, US (Levels.fyi) | p50 $220,000 (p25 $170K, p75 $280K, p90 $347K); median base $180,000 | total compensation | 1,200 | undated page | S27 |
| Databricks L3 / L5 / L6 | $218K / $349K / $359K average (base $134K / $172K / $197K) | total compensation | not stated | 2026-01-13 | S27 |
| OpenAI SA, US | $418K (base $218K; stock $200K a year) | total compensation | 1 | undated | S27 |
| Anthropic SA, France | €154K–€218K average | total compensation | not stated | 2026-02-27 | S27 |
| Anthropic Solutions Architecture, US | $241.2K–$272.6K average of posted ranges | posted ranges | 15 postings | undated | S28 (C) |
| India AI SA, 6–9 / 9–12 / 12+ years | ₹31.9–35.3L / ₹41.8–46.2L / ₹44.5–49.2L; top 10% ₹40.5L / ₹60L / ₹65L | CTC (AmbitionBox) | not stated | 2026 | S29 |
| India AI SA (Glassdoor) | ₹24L average (₹14.25–37.5L) | CTC | not stated | 2026 | S29 |
| Cognizant AIML SA, Bengaluru | ₹39–56 LPA | posted (aggregator) | 1 | 2026-11-13 | S14 |
| Bengaluru Solution Architect (Levels.fyi) | $56,221 median (p25 $40.8K, p75 $76.9K) | total compensation | not stated | 2025-11-07 (stale flag) | S27 |

Score inputs (M/D). Demand 5.5 (4–7) on proxies, grade C. Pay 7 (5.5–8.5), grade B. Durability unchanged (D). Leverage 8.5 is consistent with A-grade text: OpenAI frames the architect as the "CTO" of a customer book, and Anthropic's manager role expects executive engagement in $10M+ evaluations [S1, S3].

**A5. Loop.**

| Employer type | Rounds reported | Assesses | AI-tool policy | Fit with KB track | Grade |
|---|---|---|---|---|---|
| Anthropic | Recruiter; technical conversation; take-home with live demo (Dataford) or customer-scenario presentation (CleverPrep); safety and judgement; cross-functional (4–6 rounds, 3–6 weeks) | Architecture, not coding; responsible deployment | The application form asks candidates to confirm Anthropic's AI-use guidance, and its "why Anthropic" answer is meant to be written without AI mediation [S1] | Fits | C (A for policy) |
| OpenAI | Recruiter; technical assessments; final loop of system design, customer role-play, pair programming, behavioural (3 rounds, 3–5 weeks) | AI system design; customer scenario | Not found | Fits | C |
| Databricks | Recruiter; technical discovery; customer scenario; architecture demo or panel presentation; take-home reported | Pre-sales depth and executive presence | Not found | Partly: the "AI-FDE loop" in K9 was not verified | C |
| Hyperscalers, consultancies | No role-specific reports found | none | none | Unverifiable | E |

**A6. Sample summary (n = 23).**
- Employer type: frontier labs 7 (Anthropic 4, OpenAI 3); Big Tech 8 (AWS 2, Google 3, Microsoft 3); AI/data platform 2 (Databricks); consultancy or IT services 5 (Accenture, Capgemini, EY, PwC, Cognizant); AI-native 1 (Tribe AI).
- Region: US 5; UK 4; Europe excluding UK 3; India 4; other APAC 2; not shown 5.
- Dating: 8 dated in the window, 1 read live, 1 aggregator-relative (same-day label), 13 with the date not shown (live status unverified).
- Excluded 8 of 31 candidates read: Anthropic Partner SA 4491240008 (datePosted 2025-01-10); OpenAI SA, Gov (2025-09-18); Wipro Senior Gen AI Architect (2026-01-16); Wipro Senior AI Architect (2025-05-07); Accenture Poland GenAI Architect (valid to 2026-09-10); PwC India Manager (2026-08-03); Anthropic Manager of Applied AI Architecture 5222289008 (people manager; used for progression); AWS AI Infrastructure SSA 10435350 (HPC and infrastructure specialist).
- Two in-window postings outside the sample (Microsoft Singapore Sr CSA; Databricks Seoul) are used only for the certification count.

**A7. Other coverage.**
- **Proof of work.** Anthropic's Startups posting asks for evals, production LLM apps and a record of selling technical products [S1]. Prep sources report a take-home plus live demo [S30]. The KB's "reference architecture + cost model + IaC" is only partly echoed: reference architectures appear at Accenture [S11], cost and latency constraints at PwC [S13], and IaC in 0 of 23. Suggest adding "eval harness and a customer-scenario walkthrough".
- **Credentials.**
  - One of 23 sampled postings names a certification (Microsoft Belgium prefers a technical certification in AI, cloud, developer or agents) [S8].
  - Two more in-window postings name them: Microsoft Singapore Sr CSA lists Azure certifications; Databricks Seoul lists a Databricks certification as nice-to-have [S8, S9]. That is 3 of 25 (12%).
  - Axial finds the AWS Solutions Architect certification in 1.7% of US AI-architecture postings and concludes that no credential opens the door alone [S18].
  - AWS AIP-C01: exam offered from about 2026-03, $300, 75 questions (65 scored), 180 minutes, 750/1000 pass mark (B; the AWS page was not opened) [S31].
  - Microsoft AI-103 (Azure AI Apps and Agents Developer Associate) replaces AI-102 (retired 2026-06-30). One tracker lists AI-103 as live and others as beta [S32].
  - Google PMLE: $200, 2 hours, 50–60 questions, 3+ years of Google Cloud experience recommended, exam guide dated 2026-06-01 with generative-AI tasks [S57].
- **Entry routes and prerequisites.**
  - Degree: bachelor's or equivalent is named in 3 of 23 postings; Microsoft Belgium prefers a master's.
  - Years: see the median above.
  - Typical prior roles named: SA, SE, TAM or FDE (Anthropic), DS/ML engineer (Databricks), cloud-native architect (Google). Published analyses of prior roles of people hired were not found.
  - Backend or cloud engineer: direct route via SE or SA roles. Data scientist: Databricks (hands-on ML, 5–10+ years). Frontend: Anthropic accepts software-engineer or technical-founder backgrounds. PhD: only as "graduate degree or equivalent". Non-technical: none seen. New graduate: Microsoft entry-level CSA.
- **Progression.** Databricks ladder L3–L6 (total compensation $218K→$359K) [S27]. An AWS Principal WW Specialist SA (AI, Bedrock go-to-market) listing shows $182K–$284K [S6]. Anthropic runs a manager track (7+ years) [S1]. Axial: Principal IC is 9% of postings and Director+ about 5% [S18]. Exits to FDE, product or sales-engineering leadership are not evidenced (D).
- **Work footprint.** L6 (all postings), L5 (agents 56.5%, RAG 26.1%) and L3 (Databricks and platform specialists): K8 holds.
- **Geography and sponsorship.**
  - Axial: California 19%, Texas 13%; San Francisco about 5% of cities, Dallas and Austin about 4% each [S18].
  - Skillenai generic-SA metros as of 2026-08-01: New York, Singapore, San Francisco, London, Bengaluru [S23].
  - Anthropic states it sponsors visas but cannot do so for every role or candidate [S1]. Google Singapore prioritises candidates who already have the right to work [S7].
  - LCA data, read through aggregators of Department of Labor disclosures (B) [S56]: Databricks' FY2026 snapshot lists 90 Solutions Architect, 28 Specialist SA and 27 Senior SA positions (medians $139,059, $155,491 and $164,403), plus 46 Resident SA and 37 Delivery SA. OpenAI OpCo shows two certified "Solutions Architect" go-to-market LCAs ($290,000 San Francisco; $278,000 New York; filed 2026-04-21 and 2026-04-20). Anthropic's displayed filings are Applied AI and Forward Deployed titles, with no SA row in the extract. One tracker reports no FY2026 OpenAI LCAs, which conflicts (entity naming). Filed wages are not pay.
- **Résumé and profile signals.** Lead with named customer deployments, technical wins and the scale of evaluations influenced; show production LLM apps with evals; state the customer-facing role explicitly. Avoid a certification list as the headline.
- **Misconceptions and red flags.**
  - "Architect" in a title can mean engineer work (EY France, 3–7 years).
  - OTE ranges are not base.
  - Search indexes still return a 2025-01-10 Anthropic posting.
  - Microsoft's CSA is post-sales, not pre-sales.
- **India.** Google CE roles (Bengaluru, Gurugram or Mumbai), Anthropic India (10+ years), OpenAI AI Deployment Engineer (Delhi, aggregator), Cognizant AIML SA, Databricks India SSA roles (listed only as similar jobs; details not extracted) [S1, S7, S14, S16]. JobsPipe shows 64 live SA postings in India against 761 in corvi's snapshot category (coverage conflict) [S24, S25]. No India-specific interview evidence.

### B. AI Enablement Engineer (`ai-enablement-engineer`)

**B1. Definition and variants (n = 15).**
- **Adoption or training lead (3):** Scotiabank, Liquidity Services, Jorie AI. Often non-coding or low-code.
- **Builder-enabler (9):** Revalize, Coder, Fabletics, LocalStack, CivicPlus, Mentor Collective, Ather, Phorest, Xensam. They build internal AI tools and agents and also teach.
- **Platform, MCP and context engineering (3):** Sofi, Siemens, the London platform lead.
- Fabletics adds a "last mile" variant: hardening apps that non-engineers build so they reach production [S33].
- Aliases seen: AI Enablement Lead; AI Enablement Specialist (Allspring, outside the window); Enterprise AI Enablement Lead; AI Enablement & Process Automation Lead; Platform Engineer Lead – AI Enablement; Senior Staff AI Enablement Engineer; Staff Software Engineer – AI Enablement (Phorest); AI Adoption & Enablement Lead (title-only listings). A public-sector "NCDOT – AI Enablement Engineer" and contract "Microsoft 365 Copilot Trainer" roles also surface under the same keywords [S58]. "AI Product Ops" was not found.
- Preset's own blog describes the role as the person who accelerates AI adoption across a company; it makes value claims about leverage (COI) [S46].

Probe answer: a distinct but small and falling title, which also works as an alias for internal platform/DevEx work and for training roles. No sampled posting sits at a frontier lab or Big Tech.

**B2. Demand.**

| Measure | Value | Source and date | Grade |
|---|---|---|---|
| "AI Enablement Engineer" postings, 90 days | 42 (to 2026-11-05); 57 (to 2026-09-03, −35% vs prior four weeks) | S20, S21 | B |
| "AI Enablement Lead" postings, 90 days | 26 (to 2026-09-02) | S21 | B |
| Ratio to Skillenai "AI Engineer" (4,139 per 90 days; roles page read 2026-11-13) | about 1.0% (42 / 4,139) | S20, S22 | M |
| Employer concentration | At most 3 postings per employer (CloudZero 3; Coder, INSPYR, Socure, ID.me and others 2 each) | S20 | B |
| Metros (2026-11-05) | San Francisco 4 (9.5%), Boston 3, Barcelona 2, Dallas 2, New York 2, Singapore 2; no Indian metro in the top nine | S20 | B |
| Employer-type mix, sample n = 15 | enterprise 6; software/SaaS 7; GCC 1; Indian product company 1; frontier lab or Big Tech 0 | Sample | M |
| Seniority | Median stated minimum 4.5 years (n = 8, range 0–10); Staff-level titles 2 (Sofi, Phorest) | Sample | M |
| Remote share, sample | Explicitly remote 6 of 15 (40%); hybrid 4; unspecified 5 | Sample | M |
| Trend | 57 → 42 (−26% across 63 days); "down 35% on the prior four weeks" at 2026-09-03 | S20, S21 | B |

**B3. Skills (n = 15; floors; ±25 points).**

| Skill | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| teaching | 60.0% (9) | 15 | Must | Important | Training, workshops or enablement sessions in 9 postings. Platform shares not available. |
| internal_tooling | 46.7% (7) | 15 | Must | Must | Builder and platform variants. |
| change_mgmt | 46.7% (7) | 15 | Must | Important | Adoption and rollout language; role-defining for the adoption variant. |
| agents | 33.3% (5) | 15 | Important | Important | Platform: 16.7% (n = 42). |
| coding_agents | 33.3% (5) | 15 | Important | Important | Claude, Cursor and Copilot rollouts. |
| pilots | 33.3% (5) | 15 | Important | Important | Adoption metrics, pilots, productivity measurement. |
| new:prompt_engineering | 33.3% (5) | 15 | Important | none | Platform: 35.7% (n = 42). |
| python | 26.7% (4) | 15 | Important | Must | Platform: 33.3%. KB claim of 78.4% not replicated. |
| llm_apis | 26.7% (4) | 15 | Important | Must | KB claim of 76.7% not replicated; platform "LLMs" 16.7%. |
| mcp | 26.7% (4) | 15 | Important | Important | Platform: 19.0%. Core in one posting (Sofi). |
| grc | 26.7% (4) | 15 | Important | none | Governance, audit and compliance (Sofi, Jorie, Phorest, Fabletics). |
| new:low_code_automation | 26.7% (4) | 15 | Important | none | n8n, Make, Zapier, Power Automate, Power Platform. |
| new:rag | 20.0% (3) | 15 | Should | none | Platform: 19.0%. |
| evals | 20.0% (3) | 15 | Should | none | Revalize, Fabletics, Ather. |
| iam | 20.0% (3) | 15 | Should | Must | Platform SSO 11.9%, OAuth 9.5%. Must inside the platform variant only. |
| claude_code | 13.3% (2) | 15 | Should | Important | Platform: 14.3%. |
| guardrails | 13.3% (2) | 15 | Should | Important | |
| typescript | 13.3% (2) | 15 | Should | none | Platform: 28.6%. |
| llm_gateways | 6.7% (1) | 15 | Optional | Important | Sofi only. |

Platform cross-check, Skillenai, n = 42 postings, 2026-11-05: prompt engineering 35.7%, Python 33.3%, TypeScript 28.6%, MCP 19.0%, RAG 19.0%, LLMs 16.7%, agents 16.7%, CI/CD 14.3%, AWS 14.3%, Claude Code 14.3%, SSO 11.9%, Azure 11.9%, OAuth 9.5% [S20].

**B4. Pay.**

| Population | Statistic | Component | n | Date | Source |
|---|---|---|---|---|---|
| Fabletics, El Segundo CA (builder; 5 years) | $160,378–$180,000 range | base | 1 | 2026-08-23 | S33 |
| Scotiabank, Dallas (adoption; recruiter mirror) | $120,000–$140,000 range | base (direct hire) | 1 | 2026-08-25 | S36 |
| London platform lead (fintech, via recruiter) | up to £130,000, plus about 20% bonus | base | 1 | 2026-11-02 | S44 |
| Ather Energy, Bengaluru (0–2 years) | ₹8–14 LPA | aggregator-stated | 1 | 2026-10-28 | S42 (C) |
| Sofi Senior Staff, Seattle/San Francisco | Not shown in the extract | none | 0 | 2026-11-09 | S35 |
| Levels.fyi or equivalent | Title not tracked | none | 0 | none | Absence |

Score inputs (M/C). Demand 2.5 (1.5–3.5), grade B for the count. Pay 5.5 (4–7.5), grade C. Durability 4.5 (3–6). Leverage 6.5 unchanged.

**B5. Loop.** No role-specific loop reports, AI-tool policies or round structures were found for the title (Absence). The KB track ("Application; RAG with access control, agent loop control, evaluation architecture, context management") cannot be verified. Posting text points to a different emphasis: adoption measurement (LocalStack, Sofi, Mentor Collective), IAM and API-gateway design (Sofi, Revalize), teaching ability, and portfolio evidence (Ather, Xensam).

**B6. Sample summary (n = 15).**
- Employer type: enterprise 6 (Scotiabank, Fabletics, Sofi, Jorie AI, Liquidity Services, London fintech); software/SaaS 7 (Revalize, Coder, LocalStack, CivicPlus, Mentor Collective, Phorest, Xensam); GCC 1 (Siemens); Indian product company 1 (Ather).
- Region: US 10; Europe 3 (London, Ireland/UK remote, Stockholm); India 2.
- Dating: 8 dated in the window (Revalize 2026-11-04 on one mirror and 2026-11-07 on another; Scotiabank through its recruiter mirror, 2026-08-25); 4 aggregator-relative ages (LocalStack about 71 days, CivicPlus about 53, Mentor Collective about 75, Jorie AI about 33); 2 undated (Liquidity Services; Siemens, listed 4 days before its snapshot, closing 2027-01-27); 1 posted 2026-07-20 and read live on 2026-11-13 (Xensam).
- Excluded 9 of 24 candidates: Brooks Automation R9154 (2026-05-29), Allspring (107 days), Extend Greenhouse 5989772004 (about 178 days), DigiRecruitx (2026-02-23; customer-facing product enablement), Stride Build (about 245 days), an intern posting (about 171 days), Bentley Systems and Autodesk (title-only, no posting URL) and OpenAI "Enablement Lead – Knowledge Work" (customer enablement, a different role).

**B7. Other coverage.**
- **Proof of work.** LocalStack asks for a workflow rebuilt around AI with before-and-after evidence; Mentor Collective for built internal agents and MCP servers; Sofi for adoption metrics, runbooks and a regulated-environment record; Ather and Xensam for portfolios of AI experiments [S35, S39, S40, S42, S34]. K28 and K29 hold.
- **Credentials.** One of 15 names certifications, generically ("related certifications" preferred, Revalize) [S37]. None names a specific certification.
- **Entry routes.**
  - Stated minimum years run from 0 to 10. Only Sofi names a degree (bachelor's plus 4 years or master's plus 3).
  - Backgrounds named: backend or DevEx (Mentor Collective, Fabletics), consulting, PM or business operations (LocalStack), IT platform adoption (Scotiabank), IAM and API gateways (Sofi), low-code (Liquidity Services).
  - The non-technical lane is real: 3 of 15 postings are adoption roles. An aggregator labels Revalize "Fresher" although it asks for 1+ years.
  - Published analyses of prior roles of hires were not found.
- **Progression and durability.** Staff and Senior Staff versions exist (Sofi, Phorest), and "AI Enablement Lead" has 26 postings. The count fell from 57 to 42. Adoption variants follow vendor copilot rollouts and look transitional. The platform and governance variant (MCP gateway, SSO, audit controls at Sofi) looks more durable (C). No evidence that the work itself is being automated (D).
- **Work footprint and specialisation.** L6 plus L5 (agents 33.3%; context engineering at Siemens); the platform variant adds an identity and security plane. MCP and agent protocols: named in 4 of 15 (26.7%), core in 1 (6.7%); platform 19.0% [S20].
- **Geography and sponsorship.** US 10 of 15. The Dallas mirror requires US work authorisation. Sponsorship is not stated elsewhere. LCA data for the exact title was not queried.
- **Résumé signals.** Adoption numbers (active users, time saved); a shipped MCP server or internal agent with a usage log; runbook and risk register; SSO/OAuth scoping; a training curriculum with champion-network metrics for the adoption variant.
- **Misconceptions and red flags.** The title is not always engineering (3 of 15 are training or adoption leads). "Highest-leverage role" articles are COI or anecdote [S46, S47]. "No experience required" copy sits beside 1+ years. Keyword searches mix in contract trainers and sales enablement.
- **India.** Ather (0–2 years, portfolio of AI experiments, ₹8–14 LPA) and Siemens (Bengaluru GCC; context packers for AI developer tools) [S42, S43]. India is 2 of 15 postings. No senior India pay found.

### C. AI Product Engineer, AI Frontend (`ai-product-engineer`)

**C1. Definition and variants (n = 16).**
- **AI-facing UI specialists (5):** Taktile (chat components, streaming, human-in-the-loop approvals), Pebl (AI UX, generative UI), Dash0 (agent interface), Prime Video (AI-integrated editor), Lucid (streaming AI SDK layer).
- **AI-native design or frontend engineers (2):** Within, Alpha.
- **Product Engineers shipping AI features (7):** Arlo, humans&, Anthropic, OpenAI, Clera, The Flex, myDataValue.
- **Full-stack roles with AI-chat experience (2):** CirrusLabs, eventfirst.
- Aliases with counts: "Product Engineer" 5; "Founding Product Engineer" 1; one each of AI Frontend Engineer (Within), Senior Frontend Software Engineer – AI UX (Pebl), Frontend Engineer – AI Business Automation (Prime Video), Senior Product Engineer – Frontend (Dash0), Senior Full-Stack Engineer – Team Agent (Taktile), AI Engineer (Lucid), Software Engineer – ChatGPT Shopping (OpenAI), Software Engineer – AI Product Engineering (CirrusLabs), Senior Full-Stack Engineer (eventfirst), Frontend Design Engineer (Alpha). "Agent Interface Architect", "Client-Side AI Specialist" and the on-device titles were not found.
- Specialisations in the card's context: conversational or chat UI appears in 4 of 16 (25%: Taktile, Pebl, Arlo, eventfirst); voice agents 0 of 16; edge or on-device 0 of 16.

Probe answer: an alias family for full-stack product engineering with AI features, not a distinct title. No title-level count exists, so growth cannot be measured.

**C2. Demand.**

| Measure | Value | Source and date | Grade |
|---|---|---|---|
| "AI Product Engineer" or "AI Frontend Engineer" count | Not found | Absence | E |
| Context counts | Skillenai "AI Engineer" 4,139 per 90 days; JobsPipe "AI Engineer" 3,944 live; Fast AI Jobs 497 full-stack jobs at 313 AI startups (undated); TealHQ "Product Engineer" 1,187 found (undated) | S22, S26, S53 | B/C |
| Employer mix, sample n = 16 | lab or lab-adjacent 3; Big Tech 1; AI-native startups and scale-ups 11; IT services 1 | Sample | M |
| Seniority | Senior or Staff in the title: 5 of 16 (31.3%); median stated minimum 2 years (n = 6, range 0.5–10) | Sample | M |
| Region | US 4; Europe 3; India 2; not shown 7 | Sample | M |
| Remote share, trend | Not measurable | none | none |

**C3. Skills (n = 16; floors; ±25 points).**

| Skill | Share | n | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| react | 93.8% (15) | 16 | Must | Must | KB platform share 69.4%. |
| typescript | 81.3% (13) | 16 | Must | Must | KB platform share 52.7%. |
| llm_apis | 68.8% (11) | 16 | Must | Must | AI features are the point of the role. |
| product_sense | 50.0% (8) | 16 | Must | Important | Product ownership language in 8 postings. |
| nextjs | 43.8% (7) | 16 | Important | Important | |
| new:design_craft | 37.5% (6) | 16 | Important | none | Design sensibility (Within, Pebl, Dash0, Anthropic, Alpha, Arlo). |
| streaming_ux | 25.0% (4) | 16 | Important | Important | Taktile, Pebl, Arlo, Lucid. |
| python | 18.8% (3) | 16 | Should | Important | KB platform share 41.8%. |
| cloud | 12.5% (2) | 16 | Should | Important | KB platform share 41.3%. |
| nodejs | 12.5% (2) | 16 | Should | Important | KB platform share 32.3%. |
| new:ai_coding_tools | 12.5% (2) | 16 | Should | none | Cursor, Claude Code, Copilot, v0. |
| hitl_design | 6.3% (1) | 16 | Optional | Important | Taktile. |
| generative_ui | 6.3% (1) | 16 | Optional | Important | Pebl. |
| vercel_ai_sdk | 6.3% (1) | 16 | Optional | Important | Lucid. |
| evals | 0% (0) | 16 | Optional | Important | Not named in any extract. |
| ux_telemetry; sse | 0% (0) | 16 | Optional | Important | Not named in any extract. |

The `apis`, `frontend_engineering` and `git_ci` skills could not be measured from the extracts.

**C4. Pay.**

| Population | Statistic | Component | n | Date | Source |
|---|---|---|---|---|---|
| Within, Staff AI Frontend, San Francisco | $235,000–$315,000 range | base | 1 | 2026-11-06 | S49 |
| Within on Indeed: Senior/Staff; AI Frontend Engineer | $185,000–$315,000; $140,000–$205,000 | posted ranges | 2 | 2026-11-13 | S53 (B/C) |
| ZipRecruiter listing, Senior Staff AI Frontend | $250,000–$315,000 range | posted | 1 | 2026-11-13 | S53 (B) |
| OpenAI Software Engineer, ChatGPT Shopping, San Francisco | $230,000–$385,000 range | posted (aggregator) | 1 | 2026-11-13 | S4 |
| ZipRecruiter listings: Staff AI Product Engineer NYC; Camber | $200,000–$300,000; $190,000–$230,000 | posted | 2 | 2026-11-13 | S53 (C) |
| myDataValue, London | up to £90,000, plus up to 1% equity | posted | 1 | 2026-11 | S52 |
| CirrusLabs, Bengaluru (2–4 years) | ₹10–18 LPA | aggregator-stated | 1 | 2026-10-06 | S51 |
| Alpha, remote India (0.5–3 years) | ₹4–8 LPA plus ESOPs | aggregator-stated | 1 | 2026-11-13 | S53 |

Score inputs (M/D). Demand 3.5 (2.5–5.5), no title count. Pay 6.5 (4–8.5): US labs and staff roles $230–385K against India ₹4–18 LPA. Durability and leverage unchanged.

**C5. Loop (prep-vendor and candidate reports; C).**

| Employer type | Rounds reported | Assesses | AI-tool policy | Fit with KB track | Grade |
|---|---|---|---|---|---|
| OpenAI (frontend) | Recruiter; phone screen; take-home; onsite including a live build of a streaming chat UI; frontend system design that increasingly covers the API behind the interface; behavioural | Streaming UI, async rendering, state, accessibility | Not found | Does not fit: frontend-heavy, not RAG or agent-loop control | C |
| Vercel (frontend, product) | Take-home (3–8 hours); React deep-dive; frontend system design; product and craft; culture | Next.js fluency, craft | Not found | Partly | C |
| Cursor (software engineer) | Recruiter; phone; take-home on the real codebase; onsite coding, system design, ML/AI deep-dive, product and craft, behavioural | Product intuition, autonomy | Not found | Partly | C |
| AI-wrapper Series A companies | Founder screen; product-flavoured coding (Python or TypeScript); take-home or paired build of a small AI feature | Shipping a working AI feature | Not found | Partly | C |

**C6. Sample summary (n = 16).**
- Dating: 3 dated (Within 2026-09-24; CirrusLabs 2026-10-06; eventfirst 2026-10-02) plus myDataValue in the November 2026 thread; 4 aggregator-relative (Taktile about 71 days, Clera about 74, Lucid about 79, Prime Video about 14); Anthropic's Product Engineer, Computer Use listed as open on its careers index about 17 days before retrieval; 7 not dated (Pebl, Arlo, humans&, Dash0, The Flex, OpenAI, Alpha).
- Excluded 16 of 32 candidates read.
  - 11 for date: Tribe AI Forward Deployed AI Product Engineer (2026-06-19); phData (2026-08-03); Kloud Hire (2026-07-25); Sekai (2026-05); Airwallex Staff Frontend Engineer, AI (about 297 days); Perplexity Frontend (2025-08-20); Close (about 283 days); Recruiting Bond Staff Frontend, AI Agents (2026-05-22); byrecruiting AI Product Engineer (2026-08-11, 92 days); Metrics Recruitment (about 228 days); Anthropic Staff Software Engineer, Product (about 277 days).
  - 5 for role: SCAYLE "Senior Frontend Engineer (AI)" (marketing-site replatform; AI only in the title), David AI (data-tooling UI), Perplexity MTS – Agents (agent backend), Anthropic Front End Engineer – Marketing, Anthropic Staff Software Engineer – Web Platform (platform and design system).

**C7. Other coverage.**
- **Proof of work.**
  - Within asks for a portfolio or GitHub of shipped work, design sensibility and accessibility (WCAG) [S49].
  - Anthropic's Product Engineer role asks for zero-to-one ownership and strong product design instincts [S1].
  - Taktile and Pebl ask for experience building conversational or agentic interfaces [S50].
  - The KB's "50 eval cases and UX metrics" is not echoed (evals 0 of 16); on-device modules are absent.
- **Credentials.** None of 16 names a certification.
- **Entry routes.** Frontend or full-stack engineers with 2+ years (Prime Video, Clera, CirrusLabs); Python backend plus React (Taktile); junior routes in India (Alpha 0.5–3 years). Within explicitly waives a CS degree; no posting requires one. No data-scientist, PhD, SRE, PM or non-technical routes seen.
- **Progression and durability.** Staff AI Frontend (Within) and founding roles are the top rungs seen. Within's emphasis on design craft and AI tooling suggests generic UI work is the exposed part (D). No growth or commoditisation data.
- **Work footprint.** L6 for all; L5 where the posting covers agent runtime or orchestration (Anthropic, Taktile, Dash0).
- **Geography and sponsorship.** US 4 (San Francisco, New York, Seattle); Europe 3 (Berlin ×2, London); India 2. Within is US citizen/visa only. Anthropic sponsors visas. eventfirst is remote CET. LCA data for these titles was not queried.
- **Résumé signals.** Headline as "Product Engineer" or "Full-stack AI engineer" with React, TypeScript and LLM-integration keywords; deployed app link; streaming, cancel, retry and error states; accessibility evidence.
- **Misconceptions and red flags.**
  - "AI frontend" can mean a design-engineer role (Within) or a marketing-site job (SCAYLE).
  - Axial's "AI product" dataset of 12,397 postings is product management, not engineering [S19].
  - Pay dispersion is extreme.
- **India.** CirrusLabs (₹10–18 LPA, 2–4 years, MERN plus LLMs) and Alpha (₹4–8 LPA). An out-of-window cutshort listing asks 3–10 years at ₹10–55 LPA [S53, S51]. India is 2 of 16 postings.

### D. Cross-role notes

- **Adjacency.** SA overlaps with FDE, Sales Engineer and TAM; Enablement with DevEx, platform engineering and IT adoption; Product Engineer with full-stack, design engineering and applied AI engineering.
- **Data quality.** Platform counts differ in method: Skillenai counts canonical titles per 90 days; JobsPipe counts live postings; Axial classifies functions; corvi snapshots categories. They are not interchangeable.
- **Score inputs summary (M/D, for maintainers).**

| Role | Demand | Pay | Durability | Leverage |
|---|---|---|---|---|
| ai-solutions-architect | 5.5 (4–7) | 7 (5.5–8.5) | 6 (4.5–7.5), no new evidence | 8.5 (7.5–9.5), supported |
| ai-enablement-engineer | 2.5 (1.5–3.5) | 5.5 (4–7.5) | 4.5 (3–6) | 6.5 (5.5–7.5) |
| ai-product-engineer | 3.5 (2.5–5.5) | 6.5 (4–8.5) | 5.5 (4–7), no new evidence | 6.5 (5.5–7.5) |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | SA definition; Forward Deployment & Solutions; status V | confirmed | 15 of 23 postings pre-sales or field, 8 of 23 delivery [S1–S15] | M |
| K2 | SA aliases | updated | Adds Applied AI Architect (4 of 23), Specialist SA, Customer Engineer – AI, Cloud Solution Architect (AI, Agentic), AI Deployment Engineer; "Agent Architect (exact)" not found; "Principal AI Architect – Agentic" only in an expired posting [S1, S3, S5, S7–S9, S17] | M |
| K3 | SA demand unmeasured; JobsPipe 1,515 US as upper bound | updated | Axial: 16,927 US AI-architecture postings, +24% quarter on quarter; JobsPipe US 1,515 unchanged on 2026-11-13; AI share not re-verified; exact-title count still absent [S18, S24] | B |
| K4 | SA pay: no data; prior 6.5 | updated | Posted US $152–248K; Anthropic London £165–190K OTE; Levels.fyi median total compensation $220K (n = 1,200); lab and vendor totals up to $418K; 6.5 is a floor for labs and vendors [S1, S6, S7, S10, S27] | B |
| K5 | SA India demand: JobsPipe 64 live | updated | JobsPipe India 64 still shown; corvi shows 761 in India for the category (2026-07-05); AI-architect postings exist at Google, Anthropic and Cognizant [S1, S7, S14, S24, S25] | B |
| K6 | SA India pay: GCC and top product ₹55–80L+ (C) | confirmed | upGrad (Glassdoor figures) and other guides corroborate the top tier; mid-level ₹31.9–49.2L (AmbitionBox) added [S29] | C |
| K7 | SA durability: enterprise integration and vendor ecosystems | unverifiable | Judgement. Growth proxy only (Axial +24% quarter on quarter); no durability evidence [S18] | D |
| K8 | SA footprint L6, L5, L3 | confirmed | Agents 56.5% and RAG 26.1% (L5); Databricks and platform specialists (L3) [S1–S15] | M |
| K9 | SA interview track: application plus customer scoping | confirmed | Customer-scenario round reported at Anthropic, OpenAI and Databricks; the "AI-FDE loop" itself not verified [S30] | C |
| K10 | SA Must skills (cloud 53.6%, AWS 53.6%, communication 42.9%) | updated | Cloud 52.2% replicates; AWS 26.1% does not; add customer-facing technical experience (95.7%) and pre-sales (60.9%); communication, reference architecture and stakeholder not measurable [S1–S15] | M |
| K11 | SA Important skills | updated | Azure 30.4% and GCP 30.4% hold; managed_ai 21.7%; grc 17.4%; iam, model_selection and cost_latency 4.3% each (floors) [S1–S15] | M |
| K12 | SA credentials: AIP-C01, PMLE, AI-103 (Optional) | updated | AIP-C01: about 2026-03 launch, $300, 75 questions, 180 minutes, 750/1000; AI-102 retired 2026-06-30 and AI-103 is live or beta (sources conflict); PMLE confirmed ($200, 2 hours, 50–60 questions, guide dated 2026-06-01) [S31, S32, S57] | B |
| K13 | SA prerequisites: senior engineer or cloud architect; certifications as tie-breakers | updated | Labs gate on 5+ or 10+ years customer-facing; EY France 3–7 years; Microsoft entry-level CSA exists; certifications rarely named [S1, S8, S13] | M |
| K14 | SA proof: reference architecture with cost model and IaC | updated | Postings stress evals, production LLM apps and sold technical products; reference architectures (Accenture) and cost constraints (PwC) appear; IaC 0 of 23 [S1, S11, S13] | M/C |
| K15 | SA leave out: certification lists in place of delivered architectures | confirmed | Certifications named in 1 of 23; AWS SA certification 1.7% in Axial's set [S18] | M/B |
| K16 | Enablement definition; Applied AI Engineering family; status W | updated | Three variants: adoption lead 20%, builder-enabler 60%, platform 20%; only the last two fit an engineering family [S33–S45] | M |
| K17 | Enablement aliases | updated | AI Enablement Lead (26 postings), Specialist, Enterprise AI Enablement Lead, Platform Engineer Lead – AI Enablement, Senior Staff AI Enablement Engineer; "AI Product Ops" not found [S21, S35, S41, S44] | B/M |
| K18 | Enablement demand about 53 per 90 days (from MCP 30.2%) | updated | Direct counts: 57 (to 2026-09-03), 42 (to 2026-11-05); MCP share 19.0% (8 of 42) [S20, S21] | B |
| K19 | Enablement pay: no data; prior 6.5 | updated | $160,378–$180,000 (builder), $120–140K (adoption), up to £130K plus bonus (London platform lead) [S33, S36, S44] | A/B |
| K20 | Enablement India demand: none | updated | Ather and Siemens (2 of 15); no Indian metro in Skillenai's top nine [S20, S42, S43] | B |
| K21 | Enablement India pay: none | updated | Ather ₹8–14 LPA (0–2 years; aggregator) [S42] | C |
| K22 | Enablement durability: adoption roles may be transitional | confirmed | Count fell 57 to 42; adoption variants follow vendor rollouts; platform variant (Sofi) looks more durable [S20, S21, S35] | C |
| K23 | Enablement footprint L6, L5 | confirmed | Agents 33.3%, MCP 26.7%, context engineering at Siemens [S33–S45] | M |
| K24 | Enablement interview track | unverifiable | No role-specific loop evidence found; posting text points to adoption measurement, IAM and teaching [S35, S39, S40] | E |
| K25 | Enablement Must skills (Python 78.4%, LLM APIs 76.7%) | contradicted | Python 26.7% (platform 33.3%), LLM APIs 26.7%; internal_tooling 46.7% holds; iam 20.0% [S20, S33–S45] | M/B |
| K26 | Enablement Important skills | updated | MCP 26.7%, agents 33.3%, coding_agents 33.3%, pilots 33.3%, change_mgmt 46.7%, teaching 60.0%; llm_gateways 6.7%; guardrails and claude_code 13.3% [S33–S45] | M |
| K27 | Enablement prerequisites: backend or DevEx; ops lane about 7 months | updated | 3 of 15 are non-coding adoption roles; entry at 0–2 years (Ather) and 1+ (Revalize); 7+ at Mentor Collective and LocalStack; median 4.5 [S37, S39, S40, S42] | M |
| K28 | Enablement proof: pilot with 5–10 colleagues, runbook, risk register | confirmed | Before-and-after workflow (LocalStack), adoption metrics and runbooks (Sofi), pilots (Mentor Collective) [S35, S39, S40] | B |
| K29 | Enablement leave out: adoption claims without numbers | confirmed | Same postings ask for measured adoption [S35, S39, S40] | B |
| K30 | AI PE definition: AI-native frontend and full-stack; status W | updated | Most "Product Engineer" postings are full-stack with AI features; the AI-facing UI subset is 5 of 16 [S1, S4, S49–S53] | M |
| K31 | AI PE aliases | updated | Found AI Frontend Engineer, Frontend Engineer – AI, Product Engineer (6), Founding Product Engineer, Software Engineer – AI Product Engineering; "Agent Interface Architect", "Client-Side AI Specialist" and on-device titles not found [S49–S53] | M |
| K32 | AI PE demand: thin and senior-skewed | updated | No title-level count; median stated minimum 2 years (n = 6); 5 of 16 Senior or Staff titles; exact AI-frontend titles 1–2 of 16 [S49–S53] | M |
| K33 | AI PE pay: one Staff AI Frontend at $250–315K | updated | Within $235–315K (A); OpenAI product role $230–385K (B); India ₹4–18 LPA [S4, S49, S51, S53] | A/B |
| K34 | AI PE India demand: none | updated | CirrusLabs and Alpha (2 of 16) [S51, S53] | B |
| K35 | AI PE India pay: none | updated | ₹4–8 LPA (0.5–3 years); ₹10–18 LPA (2–4 years) [S51, S53] | B/C |
| K36 | AI PE durability: agent UX differentiated, generic UI exposed | unverifiable | Judgement. Within hires on design craft plus AI tooling; no exposure data [S49] | D |
| K37 | AI PE footprint L6, L5 | confirmed | All L6; agent runtime or orchestration at Anthropic, Taktile and Dash0 [S1, S50] | M |
| K38 | AI PE interview track (RAG, agent loop, evals) | contradicted | Reports show streaming-UI builds, frontend system design, take-homes and product-craft rounds [S54] | C |
| K39 | AI PE Must skills (React 69.4%, TypeScript 52.7%) | updated | React 93.8%, TypeScript 81.3%, LLM APIs 68.8%; apis and frontend_engineering not measured [S1, S4, S49–S53] | M |
| K40 | AI PE Important skills | updated | Next.js 43.8%; product_sense 50.0%; python 18.8%; cloud 12.5%; nodejs 12.5%; streaming_ux 25.0%; evals, ux_telemetry and sse 0; hitl, generative_ui and vercel_ai_sdk 6.3% each [S49–S53] | M |
| K41 | AI PE prerequisites: Staff-level 5–6+ years; apply as full-stack AI engineer | updated | Within 6+ years confirms it for AI-frontend titles; Product Engineer roles ask 2+; the full-stack alias is supported [S49–S51] | A/M |
| K42 | AI PE proof: full-stack app with 50 evals and UX metrics; on-device module | updated | Shipped portfolio supported (Within); evals named in 0 of 16; on-device absent [S49–S53] | A/M |
| K43 | AI PE leave out: pure UI work with no model-facing evidence | confirmed | Postings ask for chat, streaming and agent-status interfaces [S50] | C |

## Absences

- **Exact-title counts.** No count for "AI Solutions Architect" and none for "AI Product Engineer" or "AI Frontend Engineer". Searched: Skillenai, JobsPipe, Fast AI Jobs, Axial, TealHQ, ZipRecruiter, Wellfound listings.
- **Pay for the small roles.** No Levels.fyi figures for AI Enablement Engineer or AI Product Engineer (titles not tracked); no senior India pay for either role; Sofi's pay band is not in the extract; Anthropic's Product Engineer pay not extracted.
- **Interview evidence.** No Enablement loop reports or AI-tool policies; no loop reports for SA at hyperscalers or consultancies; no AI-tool policies for OpenAI or Databricks. Searched prep sites (Dataford, CleverPrep, DesignGurus, techinterview.org) and employer pages.
- **Visa filings.** The Department of Labor LCA disclosure file was not queried for the exact titles. Only aggregators for SA-family employers (S56) were read.
- **Specialisations.** No voice-agent or on-device/edge postings in the Product Engineer sample (0 of 16).
- **Prior roles of hires.** No published analyses for any of the three roles (searched Skillenai and Axial).
- **Hiring-manager statements on proof of work.** Only posting text and one employer blog (Preset). No named hiring-manager interviews found.
- **Non-English postings.** Only EY France and an Anthropic Paris posting; German and Japanese postings not searched.
- **Posting dates.** 13 of 23 SA postings and 7 of 16 Product Engineer postings carry no date on the page extracts read.
- **Workday, Taleo and Indian ATS pages.** Not fetched, apart from Fabletics. Amazon jobs, a Greenhouse page and an Ashby page failed to load.
- **Databricks India and NTT Senior AI SA (Bangalore).** Listed as similar jobs only; details not extracted.

## Open Questions & Risks

- **Pre-sales share.** My queries targeted AI vendors and consultancies. Axial's employer mix (IT services 23%, technology 22%, professional services 22%) suggests a similar balance, but a title-level count would settle it.
- **Skill shares.** Floors from extracts at n = 15–23. A full-text read of 30+ postings per role would tighten them to about ±18 points.
- **Platform comparability.** Skillenai, JobsPipe, Axial and corvi use different classes and windows. The Skillenai SA count doubled between two reads because coverage changed.
- **Mirror dating.** Aggregator mirrors (zapply, freehire, jobfound) can re-publish with new dates and may outlive the employer's posting.
- **Posted pay is not pay.** OTE ranges (Anthropic) and "Local Pay Range" labels (Databricks) mix components.
- **Alias or title.** A small sample cannot settle whether the Enablement and Product Engineer titles are growing.

**Strongest objections an expert would raise.**

| Objection | Evidence for | Evidence against |
|---|---|---|
| The sample is search-engine biased and skews to labs, so skill shares are unreliable | Greenhouse, Ashby and YC boards dominate; extracts are truncated | Shares are used only as a cross-check; platform data agree directionally (Skillenai 42 Enablement postings; Axial 16,927 AI-architecture postings) |
| Consultancy "architect" postings mix titles with engineer jobs | EY France asks 3–7 years for "architect" | Each posting is classified by what it asks for; the title mismatch is flagged in the record |
| Levels.fyi and AmbitionBox are self-reported and not AI-specific | Small n for OpenAI and Anthropic SA | Employer-posted bands corroborate the US range ($152–248K) |
| The Enablement decline from 57 to 42 may be noise | Rolling 90-day windows from one platform | Both readings fall; no growth evidence in three falsification searches |
| Product Engineer cannot be assessed without a title count | The exact title count is absent | Content, seniority and pay evidence from 16 postings is still informative |
| The "agentic" share for SA is query-induced | Queries named "Agentic AI Architect" | Tier held at Important rather than Must for this reason |

## Discovered Concerns

- **Axial "AI product" dataset.** Its 12,397 postings are product management, not engineering. Do not use it for the AI Product Engineer page [S19].
- **Skillenai "Solutions Architect" counts.** They are generic, not AI-specific, and coverage changed between reads [S22, S23].
- **Stale and mirrored postings.** Search indexes return a 2025-01-10 Anthropic posting [S1]. Built In shows a repost date different from the schema date for a Databricks posting [S10].
- **Pay components.** Databricks' "Local Pay Range" does not say whether it is OTE for field roles. Anthropic's London range is OTE [S1, S10].
- **Certification retirements.** Microsoft retired AI-102 on 2026-06-30 and scheduled AZ-204 for retirement on 2026-07-31 (replacement AI-200), which affects the KB's credential pages beyond this role group [S32].
- **FDE adjacency.** Google lists a Forward Deployed Engineer, GenAI role, and Skillenai counts 1,734 FDE postings per 90 days. An FDE role page is a candidate [S22].
- **Entity naming in LCA data.** One tracker reports no FY2026 OpenAI LCAs while another lists 454 for "OpenAI OpCo, LLC" [S56].
- **Emerging titles.** "Context Engineer" appears in a trade article as a 2025 title (C). It is a candidate ontology entry [S58].
- **Keyword noise.** "AI enablement" keyword searches mix contract Copilot trainers, sales enablement and public-sector roles, so keyword counts overstate the Enablement Engineer title [S58].

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | SA is mostly pre-sales at vendors and delivery at consultancies; US base $150–250K | Updated | 15 of 23 pre-sales or field and 8 of 23 delivery; posted US $152–248K; lab and vendor totals $224–418K [S6, S7, S10, S27] | Add the pre-sales/delivery split to the role page; widen the pay range upward for labs and vendors |
| P2 | Enablement is small and mostly adoption | Updated | Small and falling (57 to 42), but builder-enabler is 60% and adoption 20% [S20, S21, S33–S45] | Rewrite the definition around three variants; lower demand |
| P3 | AI PE is mostly full-stack and skews senior | Updated | Full-stack confirmed; median stated minimum 2 years; 31.3% Senior or Staff titles [S49–S53] | Drop "senior-skewed"; widen the pay range |
| P4 | Certifications appear in under 10% of postings | Confirmed | SA 1 of 23 (4.3%; 3 of 25 in-window); Enablement 1 of 15 generic; Product Engineer 0 of 16; Axial 1.7% [S18, S37] | Keep certifications Optional |
| P5 | India SA pay ₹25–60L | Updated | ₹31.9–49.2L in the 6–12+ year bands; ₹55–80L+ at top GCC and product employers [S29] | Add experience-banded India pay |
| P6 | Labs renamed SA to Applied AI Architect | Confirmed | 4 of 7 lab postings use "Applied AI Architect"; the rest keep "Solutions Architect" [S1, S3] | Add the alias |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Anthropic Greenhouse postings: Applied AI Architect, Startups (5432573008); Solutions Architect, Applied AI, Seoul (5390735008) and India (5117581008); Applied AI Architect, Public Sector (5382518008); Manager of Applied AI Architecture (5222289008); Solutions Architect, Applied AI (Industries), Paris (4977626008); Partner SA (4491240008); Product Engineer, Computer Use (5238637008). Anthropic. https://job-boards.greenhouse.io/anthropic/jobs/ID | n/s (4491240008: 2025-01-10) | 2026-11-13 | A (extracts B) | Read (5432573008); Extract (rest) | COI | SA and PE jd records; pay; visa and AI policy; manager track |
| S2 | Anthropic careers index ("Jobs"). Anthropic. https://www.anthropic.com/ (path not retained) | n/s (about 17 days before retrieval per search metadata) | 2026-11-13 | B | Extract | COI | Liveness of the Product Engineer posting |
| S3 | OpenAI Ashby postings: Applied AI Architect, Large Enterprise (557dd2ec-db6c-49b1-a0aa-193007ebd5b6; c00094f9-e071-4870-afec-104beb3ce499); Applied AI Architect, Partner (0916f210-e851-493c-b8ec-51cf00152be1); Applied AI Architect (28cd6fe2-4096-426b-8b08-52a66458e2c6); Solutions Architect, Tokyo (4762783e-61e1-4d36-af1d-8dee3c5f70e2); Partner AI Deployment Engineer – AWS (87989505-81e5-4513-bba0-5f00bb064216). OpenAI. https://jobs.ashbyhq.com/openai/UUID | n/s | 2026-11-13 | B | Extract | none | SA jd records; loop; leverage |
| S4 | OpenAI, Software Engineer, ChatGPT Shopping (ca54cd23-2bcc-4327-bcb6-46d81ed414a8), with pay from an Ashby board aggregator listing. https://jobs.ashbyhq.com/openai/ca54cd23-2bcc-4327-bcb6-46d81ed414a8/application ; ashbyhq-scraper.vercel.app (domain only) | n/s | 2026-11-13 | B | Extract | pay from aggregator | PE jd and pay |
| S5 | Amazon jobs: 10477876, 10486724, 10435350, 10431946. Amazon. https://www.amazon.jobs/en/jobs/ID | n/s | 2026-11-13 | B | Extract (fetch of 10486724 failed: client error) | none | SA jd records |
| S6 | AWS pay mirrors: Dreamwork mirror of Sr. GenAI SSA, Agentic AI, Seattle (https://www.dreamworkhq.com/job/4b039d36-0866-4f8d-a814-a092b9fa12b2); aiengineerjobs.com similar-jobs list (domain only). | n/s | 2026-11-13 | B | Extract | mirror | AWS pay ranges; Principal WW Specialist SA range |
| S7 | Google Careers postings: 111789275959173830 (CE III, Cloud AI); 125989501649461958 (AI CE, Developer AI, Bengaluru); 73144135992648390 (AI CE, Conglomerates); 106309273499116230 (AI CE, Singapore). Google. https://www.google.com/about/careers/applications/jobs/results/ID | n/s | 2026-11-13 | B | Extract | none | SA jd records; pay; visa priority |
| S8 | Microsoft Cloud Solution Architect postings mirrored by zapply.jobs: 59fd8cc7-9ad6-4483-b8fc-eeae063379a0 (New York); 9d958776-bc16-45f8-9f9e-75406f27a34c (Belgium); c80ebfab-8359-4bd7-bced-e3bf683f1058 (entry level); a Singapore Sr CSA listing (ID not retained). https://zapply.jobs/jobs/UUID/ | 2026-09-25; 2026-10-11; 2026-11-10; 2026-10-18 | 2026-11-13 | B | Extract | mirror | SA jd records; certification count; entry route |
| S9 | Databricks careers postings: Senior Specialist SA AI/ML, London (8615245002) https://www.databricks.com/company/careers/field-engineering---other/senior-specialist-solutions-architect-ai-ml-8615245002 ; Specialist SA AI/ML, Seoul (8785057002); Sr Specialist SA AI&ML Engineer, Israel (8784103002). databricks.com | n/s | 2026-11-13 | B | Extract | none | SA jd; certification count |
| S10 | Databricks US postings: FEQ427R382 via zapply https://zapply.jobs/jobs/3bcd43d6-5ad4-4782-b3c4-abdc6b133926/ ; FEQ227R247 via Built In (domain builtin.com) | 2026-08-14; 2026-05-18 (schema date) | 2026-11-13 | B | Extract | mirror | SA jd; pay |
| S11 | Accenture careers: Agentic AI & Commerce Architect R00347820 https://www.accenture.com/gb-en/careers/jobdetails?id=R00347820_en ; AI LLM Technology Architecture Manager (AIOC-S01660661). Accenture | 2026-10-01 | 2026-11-13 | B | Extract | none | SA jd; reference architectures |
| S12 | Capgemini Agentic AI Architect: US https://workopia.io/jobs/5adffb1dd0243320543dcdbbcdb40d57 ; GCP variant via freehire.me (path not retained) | 2026-09-11; 2026-10-31 | 2026-11-13 | B | Extract | mirror; H-1B flag unverified | SA jd |
| S13 | EY France GenAI & Agentic AI Architect H/F https://freehire.me/jobs/genai-agentic-ai-architect-h-f-careers-ey-com-kqkpl564 ; PwC Enterprise AI Architect https://freehire.me/jobs/enterprise-ai-architect-pwc-fpmve5vf | 2026-10-17; 2026-09-23 | 2026-11-13 | B | Extract | mirror | SA jd; title inflation |
| S14 | Cognizant AIML Solution Architect via topgenaijobs.com https://www.topgenaijobs.com/jobs/aiml-solution-architect-at-cognizant-in-bengaluru-qzaika (apply link: careers.cognizant.com, job 00067490711) | same-day label per aggregator | 2026-11-13 | B | Extract | mirror | SA jd; India pay |
| S15 | Tribe AI, AI Solutions Architect https://jobs.ashbyhq.com/tribe-ai/c40506b1-4d60-44e2-bc11-2f71e6f17833 ; OpenRouter, Solutions Architect (Ashby; not in sample) | n/s | 2026-11-13 | B | Extract | none | SA jd |
| S16 | OpenAI AI Deployment Engineer, Delhi, via Authentic Jobs (domain only: https://authenticjobs.com/) | about 69 days before snapshot | 2026-11-13 | B | Extract | mirror | Alias; India context |
| S17 | Out-of-window SA postings: Wipro Senior Gen AI Architect https://careers.wipro.com/job/Bengaluru-Integration-Architect-L2-IND-560035/117288-en_US/ ; Wipro Senior AI Architect (The Muse); Accenture Poland GenAI Architect (justjoin.it); PwC India Manager Enterprise AI Architect (freehire); OpenAI SA, Gov | 2026-01-16; 2025-05-07; 2026-06-12; 2026-08-03; 2025-09-18 | 2026-11-13 | A/B | Extract | none | Exclusions; alias evidence |
| S18 | Axial Search, AI Architecture Jobs in 2026 (insight on 16,927 US postings). https://axialsearch.com/insights/ai-architecture-jobs | updated 2026-08-25 | 2026-11-13 | B | Read | recruiter-authored; method disclosed | SA demand, mix, pay, certifications, geography |
| S19 | Axial Search, AI Product Jobs in 2026 (product-management postings). https://axialsearch.com/insights/ai-product-jobs | 2026 | 2026-11-13 | B | Extract | misfit: product management | Discovered concern |
| S20 | Skillenai, AI Enablement Engineer role page. https://skillenai.com/data/role/ai-enablement-engineer | data as of 2026-11-05 | 2026-11-13 | B | Read | none | Enablement demand, skills, metros |
| S21 | Skillenai role snippets: AI Enablement Engineer (data to 2026-09-03) and AI Enablement Lead (to 2026-09-02). skillenai.com/data/role (slug paths as returned by search) | 2026-09-03; 2026-09-02 | 2026-11-13 | B | Extract | none | Enablement trend; Lead count |
| S22 | Skillenai, roles by demand. https://skillenai.com/data/role | undated | 2026-11-13 | B | Read | none | Solutions Architect, AI Engineer and FDE counts |
| S23 | Skillenai Solutions Architect via talents.vaia.com mirror (domain only: https://talents.vaia.com/) | data to 2026-08-01 | 2026-11-13 | B | Extract | mirror | SA generic count and metros |
| S24 | JobsPipe, Solutions Architect pages (US, India, global). https://jobspipe.dev/jobs/solutions-architect.md (US and India sub-pages under the same path) | undated | 2026-11-13 | B | Extract | none | SA live counts |
| S25 | corvi.careers, solution architecture jobs by location (domain only: https://corvi.careers/) | snapshot 2026-07-05 | 2026-11-13 | C | Extract | none | SA India and US snapshot |
| S26 | JobsPipe AI Engineer https://jobspipe.dev/jobs/ai-engineer.md ; Fast AI Jobs, full-stack engineer roles https://www.fastaijobs.com/jobs/role/fullstack-engineer | undated | 2026-11-13 | B | Extract | none | PE context counts |
| S27 | Levels.fyi Solution Architect pages: US overall; Databricks (updated 2026-01-13); OpenAI; Anthropic (updated 2026-02-27); Bengaluru (updated 2025-11-07). https://www.levels.fyi/ (paths not retained) | dates in column | 2026-11-13 | B | Extract | self-reported; small n for labs | SA pay |
| S28 | Inference Jobs, Anthropic Solutions Architecture salaries (domain only: https://inferencejobs.com/) | undated | 2026-11-13 | C | Extract | none | Anthropic SA posted-range average |
| S29 | India SA pay sources: upGrad AI Solutions Architect salary article; futurense AI SA salary in India; AmbitionBox AI Architect salary; alp.consulting AI/ML architect salary; IANS report on AI job salaries (2026-09-02). Domain-level: upgrad.com, futurense.com, ambitionbox.com, alp.consulting, ianslive.in | 2026 | 2026-11-13 | C | Extract | none | India SA pay |
| S30 | SA interview-prep sources: Dataford guides (OpenAI SA; Anthropic AI Architect; Databricks SA), CleverPrep Anthropic SA, a GitHub compilation of company loops. dataford.io, cleverprep.com, github.com | 2026 | 2026-11-13 | C | Extract | COI (prep vendors) | SA loop |
| S31 | AWS AIP-C01 third-party sources: CBT Nuggets https://www.cbtnuggets.com/blog/training/certification-paths/tech-news-generative-ai-developer-cert ; Lumify Work; Tutorials Dojo; a candidate's public blog (codedchords.dev, 2026-08) | 2026 | 2026-11-13 | B | Extract | corroborated; AWS page not opened | AIP-C01 facts |
| S32 | Microsoft AI-103 and AI-102: Pearson VUE Microsoft updates https://www.pearsonvue.com/us/en/microsoft/updates.html ; vladtalkstech https://vladtalkstech.com/microsoft-learning-and-credential-news/microsoft-certification-retirements-2026/ ; TrainingCamp https://trainingcamp.com/what-is-ai-103/ ; Open Exam Prep https://open-exam-prep.com/blog/ai-102-vs-ai-103-which-exam-2026 | 2026 | 2026-11-13 | B | Extract | conflicting on beta or live | AI-103 and retirements |
| S33 | Fabletics, AI Enablement Engineer R8529 (Workday). https://fabletics.wd1.myworkdayjobs.com/en-US/fabletics/job/AI-Enablement-Engineer_R8529 | 2026-08-23 | 2026-11-13 | A | Read | none | Enablement jd; pay |
| S34 | Xensam, AI Enablement Engineer 8096505 (Teamtailor). https://careers.xensam.com/jobs/8096505-ai-enablement-engineer | 2026-07-20 (modified 2026-10-14) | 2026-11-13 | A | Read | none | Enablement jd (Europe) |
| S35 | Sofi, Senior Staff AI Enablement Engineer (Greenhouse 8196294003) via zapply. https://zapply.jobs/jobs/3c04c190-7158-42c0-9001-4e9b7654bb14/ | 2026-11-09 | 2026-11-13 | B | Read (mirror) | mirror | Enablement jd; platform variant |
| S36 | Scotiabank, AI Enablement Engineer, Dallas https://jobs.scotiabank.com/job/Dallas-AI-Enablement-Engineer-TX-75219/604986617/ ; Inspyr Solutions mirror (job 26-158990; domain inspyrsolutions.com) | 2026-08-25 (mirror) | 2026-11-13 | B | Extract | mirror pay | Enablement jd; adoption variant pay |
| S37 | Revalize, AI Enablement Engineer. https://jobfound.org/job/revalize-is-hiring-for-ai-enablement-engineer-united-states-remote-usa-7-november-2026 ; https://www.virtualvocations.com/job/ai-enablement-engineer-3331177-i.html | 2026-11-04 and 2026-11-07 | 2026-11-13 | B | Extract | mirror | Enablement jd; certification count |
| S38 | Coder, AI Enablement Engineer. https://careers.redpoint.com/companies/coder/jobs/91812892-ai-enablement-engineer | 2026-09-01 | 2026-11-13 | B | Extract | none | Enablement jd |
| S39 | LocalStack AI Enablement Engineer (TealHQ https://www.tealhq.com/job/ai-enablement-engineer_7ea1aca5cc41c2543a4f68ee08850439db1ca ); CivicPlus and Liquidity Services (JobLeads, domain jobleads.com) | relative ages | 2026-11-13 | B | Extract | mirror | Enablement jd |
| S40 | Mentor Collective, AI Enablement Engineer. https://builtin.com/job/ai-enablement-engineer-remote/11054298 ; Techstars job board | about 75 days before snapshot | 2026-11-13 | B | Extract | none | Enablement jd |
| S41 | Jorie AI, Enterprise AI Enablement Lead. https://www.builtinchicago.org/job/enterprise-ai-enablement-lead/10024617 | about 33 days before snapshot | 2026-11-13 | B | Extract | none | Enablement jd |
| S42 | Ather Energy, AI Enablement Engineer. https://www.dreamworkhq.com/job/456e67af-56b0-44b8-b0d7-be27fbf88a16 ; ClassicJobs summary (classicjobs.in) | 2026-10-28 | 2026-11-13 | B | Extract | mirror | Enablement jd; India |
| S43 | Siemens, AI Enablement Engineer (Architect). https://www.bayt.com/en/india/jobs/ai-enablement-engineer-architect-75250366/ ; Indeed India listing | n/s | 2026-11-13 | B | Extract | none | Enablement jd; GCC |
| S44 | Platform Engineer Lead – AI Enablement, London. https://www.itjobboard.co.uk/job/16937486/platform-engineer-lead-ai-enablement/ | 2026-11-02 | 2026-11-13 | B | Extract | recruiter listing | Enablement jd; pay |
| S45 | Phorest, AI Enablement Engineer. https://remowork.life/jobs/6aaa7e825d989acfeaf035d5/ai-enablement-engineer ; dynamitejobs.com | 2026-09-16 | 2026-11-13 | B | Extract | none | Enablement jd |
| S46 | Preset, AI Enablement Engineer: The Highest-Leverage Role in Tech (blog). https://preset.io/blog/ai-enablement-engineer/ | n/s (about 227 days before retrieval) | 2026-11-13 | A (role description); C (value claims) | Extract | COI | Role description |
| S47 | The Broken Telephone, The AI Enablement Engineer: The Highest-Leverage Role Nobody Is Hiring For Yet. https://thebrokentelephone.com/articles/ai-enablement-engineer/ | n/s (about 209 days) | 2026-11-13 | D | Extract | single source | Misconceptions |
| S48 | Out-of-window or adjacent Enablement items: Brooks Automation R9154; Allspring; Extend (Greenhouse 5989772004); DigiRecruitx; Stride Build; Indeed IE and Glassdoor India lists | 2026-05-29; 2026-02-23; others n/s | 2026-11-13 | B/C | Extract | none | Exclusions |
| S49 | Within, Staff AI Frontend Engineer. https://www.ycombinator.com/companies/within/jobs/Am14EFK-staff-ai-frontend-engineer ; zapply mirror https://zapply.jobs/jobs/699df32e-992a-4daa-8442-512bf998ce7a/ | 2026-09-24 (mirror) | 2026-11-13 | A (YC page read); B (mirror) | Read | none | PE jd; pay; sponsorship |
| S50 | Ashby postings: Taktile c9d47dd2-3252-4266-a581-b9d1b46e9297; Pebl e7f04c03-619d-420c-9201-d2a2e2ec0d84; Arlo 1429423a-a98b-459d-8d89-b80e0862ab8c; humans& c3a7fce6-0bb5-43c6-a2a7-01c63e4b1401; Dash0 bb433d72-7241-49b4-acfb-a6a403f9422c; Clera 48f5376d-0222-4b2e-bf43-4d68d0ece121; The Flex 8c9ad50d-0f19-48cb-a7d0-03906f774729. https://jobs.ashbyhq.com/company/UUID | n/s | 2026-11-13 | B | Extract (Pebl fetch failed) | none | PE jd |
| S51 | Prime Video https://devsunite.com/jobs/prime-video-amazon-mgm-studios-frontend-engineer-ai-business-automation-prime-video-seattle-oct2026-141927 ; CirrusLabs https://jobfound.org/job/cirruslabs-is-hiring-for-software-engineer-ai-product-engineering-bengaluru-karnataka-india-6-october-2026 ; Lucid https://www.wearedevelopers.com/jobs/ext/2239710-ai-engineer | 2026-10-06 (CirrusLabs); others relative | 2026-11-13 | B | Extract | mirror | PE jd; India pay |
| S52 | Hacker News "Who is hiring?" threads, October and November 2026: eventfirst; myDataValue https://www.mydatavalue.com/founding-product-engineer/ . Via https://hnhiring.com/technologies/react and https://nchelluri.github.io/hnjobs/ | 2026-10-02; 2026-11 | 2026-11-13 | C | Extract | none | PE jd (Europe) |
| S53 | Alpha, Frontend Design Engineer https://www.productbased.in/jobs/frontend ; ZipRecruiter AI product and AI front-end listings https://www.ziprecruiter.com/Jobs/Ai-Product-Engineer/2 ; Indeed and cutshort listings | n/s | 2026-11-13 | B/C | Extract | none | PE jd; pay; India |
| S54 | AI frontend and product interview reports: Educative https://www.educative.io/guide/openai-frontend-engineer-interview ; DesignGurus https://www.designgurus.io/blog/openai-frontend-engineer-interview ; techinterview.org https://www.techinterview.org/post/3233475314/ai-product-engineer-interview-2026-hybrid-role/ and https://www.techinterview.org/companies/vercel/ ; Codemia https://codemia.io/guides/cursor-software-engineer ; CleverPrep https://www.cleverprep.com/companies/openai/frontend-engineer | 2026 | 2026-11-13 | C | Extract | COI (prep vendors) | PE loop |
| S55 | Out-of-window or off-role Product Engineer candidates: Tribe AI, phData, Kloud Hire, Sekai, Airwallex, Perplexity, Close, Recruiting Bond, byrecruiting, SCAYLE, David AI, Metrics Recruitment, Anthropic (Staff SWE Product; Web Platform; Front End – Marketing) | various | 2026-11-13 | A/B | Extract | none | Exclusions |
| S56 | LCA aggregators of Department of Labor disclosures: Ellis https://www.ellis.com/visa-sponsors/databricks-inc ; https://www.ellis.com/visa-sponsors/openai-opco-llc/h1b ; https://www.ellis.com/visa-sponsors/anthropic-pbc/h1b ; h1bgrader https://h1bgrader.com/h1b-sponsors/databricks-inc-nokpn1vn04/lca/2026 ; MyVisaJobs https://www.myvisajobs.com/employer/openai/ | FY2026 (OpenAI note 2026-10-07) | 2026-11-13 | B | Extract | conflicting on OpenAI | Sponsorship signals |
| S57 | Google Cloud, Professional Machine Learning Engineer certification page and exam guide. https://cloud.google.com/learn/certification/machine-learning-engineer ; https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf | guide dated 2026-06-01 | 2026-11-13 | B | Extract (issuer page excerpts) | none | PMLE facts |
| S58 | Enablement falsification listings: ZipRecruiter https://www.ziprecruiter.com/Jobs/Ai-Enablement-Engineer and https://www.ziprecruiter.com/Jobs/Ai-Enablement ; Dice https://www.dice.com/jobs/q-ai+enablement+specialist-jobs ; StepStone https://www.stepstone.de/results/ai-expert ; UltraTalent https://ultratalent.com/blog/new-ai-roles-reshaping-the-workforce/ | 2026-11 | 2026-11-13 | B/C | Extract | none | Absence of Big Tech and lab postings; variants |

## Data Appendix

Records are JSON Lines, grouped by type. `must` entries are condensed paraphrases, not verbatim text. `seen` is the retrieval date. `as_of` is the posting date where one is shown, otherwise the retrieval date. Postings with no date on the page extract are flagged in `note`. `seniority` is my reading of the title and body; the seniority counts in the narrative use title or level flags only.

### jd records: ai-solutions-architect (23)

```jsonl
{"type":"jd","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Anthropic","title":"Applied AI Architect, Startups","url":"https://job-boards.greenhouse.io/anthropic/jobs/5432573008","job_id":"5432573008","seen":"2026-11-13","location":"London, UK","remote":"hybrid, office at least 25% of the time","seniority":"mid-senior IC, pre-sales","years":5,"degree":"bachelor's or equivalent experience","must":["5+ yrs technical customer-facing (SA, SE, FDE or technical founder)","production LLM apps: context engineering, evals","Python and LLM frameworks","sold technical products"],"nice":["startup or high-growth background"],"pay":{"lo":165000,"hi":190000,"currency":"GBP","period":"year"},"ats":"Greenhouse","note":"Read in full and live. Pay is OTE (base plus commission). Employer states it sponsors visas. COI: developer's own posting."}
{"type":"jd","grade":"B","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Anthropic","title":"Solutions Architect, Applied AI","url":"https://job-boards.greenhouse.io/anthropic/jobs/5390735008","job_id":"5390735008","seen":"2026-11-13","location":"Seoul, South Korea","seniority":"mid-senior IC, pre-sales","years":5,"must":["5+ yrs customer-facing technical (SA, SE, TAM)","partner with account executives","architect enterprise LLM solutions"],"ats":"Greenhouse","note":"Extract; posting date not shown; liveness not re-verified. COI."}
{"type":"jd","grade":"B","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Anthropic","title":"Applied AI Architect, Public Sector","url":"https://job-boards.greenhouse.io/anthropic/jobs/5382518008","job_id":"5382518008","seen":"2026-11-13","location":"Washington, DC, US","remote":"on-site in secure government facilities","seniority":"mid-senior IC","years":5,"must":["5+ yrs SA, SE or TAM","cyber domain expertise","support Claude Code, API and Enterprise"],"ats":"Greenhouse","note":"Extract; posting date not shown; liveness not re-verified. COI."}
{"type":"jd","grade":"B","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Anthropic","title":"Solutions Architect, Applied AI","url":"https://job-boards.greenhouse.io/anthropic/jobs/5117581008","job_id":"5117581008","seen":"2026-11-13","location":"India (Anthropic India; an Indeed listing shows Bengaluru)","seniority":"senior IC, pre-sales","years":10,"must":["10+ yrs technical customer-facing","enterprise LLM integration across India and APAC","pre-sales architecture"],"ats":"Greenhouse","note":"Extract; fetch was bot-blocked; date not shown and may pre-date the window. COI."}
{"type":"jd","grade":"B","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"OpenAI","title":"Applied AI Architect, Large Enterprise","url":"https://jobs.ashbyhq.com/openai/557dd2ec-db6c-49b1-a0aa-193007ebd5b6/application","job_id":"557dd2ec-db6c-49b1-a0aa-193007ebd5b6","seen":"2026-11-13","location":"London, UK","seniority":"senior technical owner of a customer portfolio","must":["significant customer-facing technical experience (SA, SE, TAM, AI deployment)","Applied AI architectures across models, data, security, governance, evaluation","CTO, CIO and CISO engagement"],"ats":"Ashby","note":"Extract; date not shown."}
{"type":"jd","grade":"B","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"OpenAI","title":"Applied AI Architect, Partner","url":"https://jobs.ashbyhq.com/openai/0916f210-e851-493c-b8ec-51cf00152be1","job_id":"0916f210-e851-493c-b8ec-51cf00152be1","seen":"2026-11-13","location":null,"seniority":"senior partner-facing architect","must":["significant senior customer or partner-facing technical experience","architecture across ChatGPT Enterprise, API and Codex with GSI and RSI partners","credibility with CTOs and partner executives"],"ats":"Ashby","note":"Extract; location and date not shown."}
{"type":"jd","grade":"B","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"OpenAI","title":"Solutions Architect","url":"https://jobs.ashbyhq.com/openai/4762783e-61e1-4d36-af1d-8dee3c5f70e2","job_id":"4762783e-61e1-4d36-af1d-8dee3c5f70e2","seen":"2026-11-13","location":"Tokyo, Japan","seniority":"mid-senior, technical success","must":["business-minded SA for strategic API-platform customers","prototype with customers","share best practice through notebooks"],"ats":"Ashby","note":"Extract; date not shown; technical-success (post-sales) orientation."}
{"type":"jd","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Amazon Web Services","title":"Sr. GenAI Specialist Solutions Architect, Agentic AI, WWSO Generative AI","url":"https://www.amazon.jobs/en/jobs/10477876","job_id":"10477876","seen":"2026-11-13","location":null,"seniority":"senior specialist","must":["subject-matter expert on GenAI application modernisation (AWS Transform custom, Kiro)","customer briefings and deep dives","GenAI adoption patterns"],"ats":"Amazon (in-house)","note":"Extract; location and date not shown; URL is the job-ID form (slug omitted)."}
{"type":"jd","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Amazon Web Services","title":"Sr. GenAI & ML Specialist Solutions Architect, ASPI Auto & Manufacturing","url":"https://www.amazon.jobs/en/jobs/10486724/sr-genai-ml-specialist-solutions-architect-aspi-auto-manufacturing","job_id":"10486724","seen":"2026-11-13","location":null,"seniority":"senior specialist","must":["deep technical expertise plus executive-level customer engagement","pre-sales architecture for GenAI and ML on AWS"],"ats":"Amazon (in-house)","note":"Extract; fetch failed (client error); location and date not shown."}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Google Cloud","title":"Customer Engineer III, Cloud AI","url":"https://www.google.com/about/careers/applications/jobs/results/111789275959173830","job_id":"111789275959173830","seen":"2026-11-13","location":"US (Atlanta, Austin and other cities)","seniority":"level III","must":["GenAI apps: RAG pipelines, vector databases, LLM orchestration via APIs","partner with technical sales teams"],"pay":{"lo":152000,"hi":221000,"currency":"USD","period":"year"},"ats":"Google (in-house)","note":"Extract; date not shown; pay plus 42.86% bonus target and equity; URL is the job-ID form."}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Google Cloud","title":"AI Customer Engineer, Developer AI","url":"https://www.google.com/about/careers/applications/jobs/results/125989501649461958","job_id":"125989501649461958","seen":"2026-11-13","location":"Bengaluru, India","seniority":"advanced","years":10,"degree":"bachelor's in a technical field or equivalent practical experience","must":["10 yrs cloud-native architecture, customer-facing or support","architect AI agents with enterprise data via RAG, text-to-SQL, semantic search","Vertex AI platform"],"ats":"Google (in-house)","note":"Extract; date not shown; URL is the job-ID form."}
{"type":"jd","grade":"B","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Google Cloud","title":"AI Customer Engineer, Conglomerates","url":"https://www.google.com/about/careers/applications/jobs/results/73144135992648390","job_id":"73144135992648390","seen":"2026-11-13","location":"Gurugram or Mumbai, India","seniority":"advanced","must":["practice customer engineer with an AI specialty","accelerate technical wins on complex workloads"],"ats":"Google (in-house)","note":"Extract; date not shown; URL is the job-ID form."}
{"type":"jd","grade":"B","src":["S8"],"as_of":"2026-09-25","ttl":"V1","role":"ai-solutions-architect","employer":"Microsoft","title":"Senior Cloud Solution Architect, Agentic AI and Copilot Studio","url":"https://zapply.jobs/jobs/59fd8cc7-9ad6-4483-b8fc-eeae063379a0/","seen":"2026-11-13","location":"New York, US","seniority":"senior, customer-success unit","must":["senior technical authority for Copilot Studio and agents","build agents integrating Microsoft 365, SharePoint, Teams and Power Platform","Azure AI Foundry"],"ats":"Microsoft careers (zapply mirror)","note":"Extract from an aggregator mirror; posted 2026-09-25."}
{"type":"jd","grade":"B","src":["S8"],"as_of":"2026-10-11","ttl":"V1","role":"ai-solutions-architect","employer":"Microsoft","title":"Cloud Solution Architect, Copilot and AI","url":"https://zapply.jobs/jobs/9d958776-bc16-45f8-9f9e-75406f27a34c/","seen":"2026-11-13","location":"Belgium (from the pay band; the aggregator header says United States)","seniority":"IC3","must":["technical engagements from architecture and PoC to production","Dutch or French fluency","Azure AI and agent development"],"nice":["master's degree","technical certification in AI, cloud, developer or agents"],"pay":{"lo":55400,"hi":93700,"currency":"EUR","period":"year"},"ats":"Microsoft careers (zapply mirror)","note":"Extract from an aggregator mirror; posted 2026-10-11; pay is base."}
{"type":"jd","grade":"B","src":["S10"],"as_of":"2026-08-14","ttl":"V1","role":"ai-solutions-architect","employer":"Databricks","title":"Specialist Solutions Architect, AI/ML","url":"https://zapply.jobs/jobs/3bcd43d6-5ad4-4782-b3c4-abdc6b133926/","job_id":"FEQ427R382","seen":"2026-11-13","location":"US (Central and West Coast)","seniority":"senior specialist","must":["own AI/ML technical strategy for accounts","RAG, tool calling, multi-agent orchestration, guardrails, evals, observability","technical wins in competitive deals"],"pay":{"lo":180000,"hi":247500,"currency":"USD","period":"year"},"ats":"Greenhouse (zapply mirror)","note":"Extract from a mirror; posted 2026-08-14. 'Local Pay Range' (OTE not stated). A sister requisition (FEQ227R247) lists 5+ yrs ML, 2+ yrs customer-facing and a graduate degree or equivalent."}
{"type":"jd","grade":"B","src":["S9"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Databricks","title":"Senior Specialist Solutions Architect (AI/ML)","url":"https://www.databricks.com/company/careers/field-engineering---other/senior-specialist-solutions-architect-ai-ml-8615245002","job_id":"8615245002","seen":"2026-11-13","location":"London, UK","seniority":"senior specialist","years":10,"must":["10+ yrs hands-on data science or ML engineering","cloud infrastructure (AWS, Azure, GCP) for ML deployment","RAG, agentic systems, guardrails, AI observability"],"ats":"Greenhouse","note":"Extract; date not shown."}
{"type":"jd","grade":"B","src":["S11"],"as_of":"2026-10-01","ttl":"V1","role":"ai-solutions-architect","employer":"Accenture","title":"Agentic AI & Commerce Architect","url":"https://www.accenture.com/gb-en/careers/jobdetails?id=R00347820_en","job_id":"R00347820","seen":"2026-11-13","location":"UK careers site (location not stated)","seniority":"associate director level","years":8,"must":["8+ yrs AI and ML systems, with GenAI and agentic in production","agent integration with the commerce stack via MCP and A2A","hyperscaler agentic platforms (Vertex AI and ADK, Azure AI Foundry, Bedrock Agents)"],"ats":"Accenture careers","note":"Extract; posted 2026-10-01; mentions reference architectures and standards."}
{"type":"jd","grade":"B","src":["S12"],"as_of":"2026-09-11","ttl":"V1","role":"ai-solutions-architect","employer":"Capgemini","title":"Agentic AI Architect","url":"https://workopia.io/jobs/5adffb1dd0243320543dcdbbcdb40d57","seen":"2026-11-13","location":"Charlotte, New York, Atlanta or Chicago, US","seniority":"architect","must":["enterprise agentic architecture: multi-agent systems, orchestration, integrations","risk management practices and Responsible AI principles"],"ats":"Capgemini (workopia mirror)","note":"Extract; posted 2026-09-11; the aggregator shows an H-1B data flag that I did not verify."}
{"type":"jd","grade":"B","src":["S13"],"as_of":"2026-10-17","ttl":"V1","role":"ai-solutions-architect","employer":"EY","title":"GenAI & Agentic AI Architect H/F","url":"https://freehire.me/jobs/genai-agentic-ai-architect-h-f-careers-ey-com-kqkpl564","seen":"2026-11-13","location":"France","seniority":"consultant-level (3-7 years)","years":3,"must":["3-7 yrs in software, data or ML engineering, then GenAI applications","has built a GenAI application used by real users"],"ats":"EY careers (freehire mirror)","note":"Extract; posted 2026-10-17. Title says architect while the body describes AI engineer work. Years given as a 3-7 range."}
{"type":"jd","grade":"B","src":["S13"],"as_of":"2026-09-23","ttl":"V1","role":"ai-solutions-architect","employer":"PwC","title":"Enterprise AI Architect","url":"https://freehire.me/jobs/enterprise-ai-architect-pwc-fpmve5vf","seen":"2026-11-13","location":null,"seniority":"architect","must":["design end-to-end client AI architectures: agents, RAG, model routing, identity, human-in-the-loop","hybrid deployment: residency, latency, cost","work with Responsible AI, cyber and privacy specialists"],"ats":"PwC careers (freehire mirror)","note":"Extract; posted 2026-09-23; location not shown."}
{"type":"jd","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Cognizant","title":"AIML Solution Architect","url":"https://www.topgenaijobs.com/jobs/aiml-solution-architect-at-cognizant-in-bengaluru-qzaika","job_id":"00067490711","seen":"2026-11-13","location":"Bengaluru, India","remote":"hybrid","seniority":"architect","years":8,"must":["solution architect for AIML applications","hands-on agentic and GenAI applications with LLMs","GenAI on at least one major cloud"],"pay":{"lo":3900000,"hi":5600000,"currency":"INR","period":"year"},"ats":"Cognizant careers (topgenaijobs mirror)","note":"Extract; aggregator shows a same-day label and 8-12 years; pay is aggregator-stated."}
{"type":"jd","grade":"B","src":["S15"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","employer":"Tribe AI","title":"AI Solutions Architect","url":"https://jobs.ashbyhq.com/tribe-ai/c40506b1-4d60-44e2-bc11-2f71e6f17833","job_id":"c40506b1-4d60-44e2-bc11-2f71e6f17833","seen":"2026-11-13","location":null,"seniority":"senior","years":5,"must":["5+ yrs leading technical workstreams as SA or similar","GenAI in production","AWS, Azure and/or GCP production infrastructure"],"ats":"Ashby","note":"Extract; location and date not shown."}
{"type":"jd","grade":"B","src":["S8"],"as_of":"2026-11-10","ttl":"V1","role":"ai-solutions-architect","employer":"Microsoft","title":"Cloud Solution Architect, Entry Level","url":"https://zapply.jobs/jobs/c80ebfab-8359-4bd7-bced-e3bf683f1058/","seen":"2026-11-13","location":"Romania (from the pay-page link)","seniority":"entry level","must":["design and build AI and agentic solutions","Copilot Studio, Foundry, Fabric, Azure AI and GitHub"],"ats":"Microsoft careers (zapply mirror)","note":"Extract from an aggregator mirror; posted 2026-11-10."}
```

### jd records: ai-enablement-engineer (15)

```jsonl
{"type":"jd","grade":"B","src":["S36"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"Scotiabank","title":"AI Enablement Engineer","url":"https://jobs.scotiabank.com/job/Dallas-AI-Enablement-Engineer-TX-75219/604986617/","job_id":"604986617","seen":"2026-11-13","location":"Dallas, TX, US","remote":"hybrid (per recruiter mirror)","seniority":"mid","must":["technical enablement, platform adoption or systems analysis experience","conceptual GenAI, LLM and copilot understanding","AI champions network, training and documentation"],"pay":{"lo":120000,"hi":140000,"currency":"USD","period":"year"},"note":"Adoption variant. Pay and the US work-authorisation line come from the Inspyr mirror (job 26-158990, 2026-08-25), which does not name the employer."}
{"type":"jd","grade":"B","src":["S37"],"as_of":"2026-11-07","ttl":"V1","role":"ai-enablement-engineer","employer":"Revalize","title":"AI Enablement Engineer","url":"https://jobfound.org/job/revalize-is-hiring-for-ai-enablement-engineer-united-states-remote-usa-7-november-2026","seen":"2026-11-13","location":"United States (remote)","remote":"remote","seniority":"junior-mid (aggregator label: Fresher)","years":1,"must":["1+ yrs software development with LLM exposure","Python, REST APIs, React and TypeScript","build and support AI tools, agents and workflows; CRM and Microsoft 365 integrations"],"nice":["MCP servers and the Claude ecosystem","related certifications","Entra ID or Microsoft Graph"],"note":"Builder variant. Posted 2026-11-04 on one mirror and 2026-11-07 on another."}
{"type":"jd","grade":"B","src":["S38"],"as_of":"2026-09-01","ttl":"V1","role":"ai-enablement-engineer","employer":"Coder","title":"AI Enablement Engineer","url":"https://careers.redpoint.com/companies/coder/jobs/91812892-ai-enablement-engineer","job_id":"91812892","seen":"2026-11-13","location":"United States","seniority":null,"must":["execute the AI roadmap and internal AI infrastructure improvements","cross-functional enablement of AI use"],"nice":["business analysis, L&D or developer relations","internal developer platform or AI enablement programme","MCP and API integrations (Slack, GitHub, Salesforce)"],"note":"Builder variant. Redpoint portfolio board; years not shown."}
{"type":"jd","grade":"A","src":["S33"],"as_of":"2026-08-23","ttl":"V1","role":"ai-enablement-engineer","employer":"Fabletics","title":"AI Enablement Engineer","url":"https://fabletics.wd1.myworkdayjobs.com/en-US/fabletics/job/AI-Enablement-Engineer_R8529","job_id":"R8529","seen":"2026-11-13","location":"El Segundo, CA, US","remote":"hybrid or on-site","seniority":"senior-staff judgement","years":5,"must":["5 yrs software development","production path: auth, secrets, data governance, testing, CI/CD, monitoring","LLM APIs, prompt engineering, agents, RAG and evals","teach and unblock non-engineers"],"nice":["internal platform or paved-road tooling","coaching low-code builders"],"pay":{"lo":160378,"hi":180000,"currency":"USD","period":"year"},"ats":"Workday","note":"Read in full. Builder variant (last-mile production hardening)."}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"LocalStack","title":"AI Enablement Engineer","url":"https://www.tealhq.com/job/ai-enablement-engineer_7ea1aca5cc41c2543a4f68ee08850439db1ca","seen":"2026-11-13","location":"United States (remote)","remote":"remote","seniority":"senior","years":7,"must":["7+ yrs combined software engineering plus consulting, PM or business operations in B2B SaaS","broad AI understanding","before-and-after evidence of a workflow rebuilt around AI"],"note":"Builder variant. Age is relative: about 71 days before the aggregator snapshot."}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"CivicPlus","title":"AI Enablement Engineer for Automation & Impact","url":"https://www.jobleads.com/us/job/ai-enablement-engineer-for-automation-impact--united-states--e13dbf7a8830e3d923bd9a34944cd4452","seen":"2026-11-13","location":"United States","seniority":null,"must":["AI-enabled workflows, automations and integrations","AI and ML model or service integration familiarity","documentation, standards and reusable patterns"],"note":"Builder variant. Age is relative: about 53 days before the aggregator snapshot."}
{"type":"jd","grade":"B","src":["S40"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"Mentor Collective","title":"AI Enablement Engineer","url":"https://builtin.com/job/ai-enablement-engineer-remote/11054298","job_id":"11054298","seen":"2026-11-13","location":"United States (remote)","remote":"remote","seniority":"senior","years":7,"must":["7+ yrs software engineering, developer productivity or technical enablement","internal AI agents, MCP servers and Claude or Cursor integrations","hands-on daily use of Claude and Cursor","train non-engineering teams"],"note":"Builder variant. Age is relative: about 75 days before the Techstars board snapshot."}
{"type":"jd","grade":"B","src":["S35"],"as_of":"2026-11-09","ttl":"V1","role":"ai-enablement-engineer","employer":"Sofi","title":"Senior Staff AI Enablement Engineer","url":"https://zapply.jobs/jobs/3c04c190-7158-42c0-9001-4e9b7654bb14/","job_id":"8196294003","seen":"2026-11-13","location":"Seattle, WA or San Francisco, CA, US","seniority":"senior staff","years":4,"degree":"bachelor's plus 4 years or master's plus 3","must":["MCP servers and clients, API gateways, Claude Code, Cursor and Copilot","SSO, SAML, OAuth, OIDC, SCIM, Okta, RBAC","regulated-environment experience","adoption metrics"],"nice":["AI or API gateway experience","NIST AI RMF and OWASP LLM Top 10"],"pay":null,"ats":"Greenhouse (zapply mirror)","note":"Platform variant. Read from a mirror; pay not in the extract."}
{"type":"jd","grade":"B","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"Liquidity Services","title":"AI Enablement & Process Automation Lead","url":"https://www.jobleads.com/us/job/remote-ai-enablement-automation-lead--united-states--e13f37a4db303bd667066174ccbfb4842","seen":"2026-11-13","location":"United States (remote)","remote":"remote","seniority":"lead","must":["Copilot, Copilot Studio and Power Platform adoption","training programmes and prompt engineering","measure productivity gains"],"note":"Adoption variant. Date not shown."}
{"type":"jd","grade":"B","src":["S41"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"Jorie AI","title":"Enterprise AI Enablement Lead","url":"https://www.builtinchicago.org/job/enterprise-ai-enablement-lead/10024617","seen":"2026-11-13","location":"United States (remote)","remote":"remote","seniority":"lead","must":["lead enterprise AI adoption and assess processes","implementation playbooks and workshops","security, compliance and human oversight"],"note":"Adoption variant. Age is relative: about 33 days before the aggregator snapshot."}
{"type":"jd","grade":"B","src":["S42"],"as_of":"2026-10-28","ttl":"V1","role":"ai-enablement-engineer","employer":"Ather Energy","title":"AI Enablement Engineer","url":"https://www.dreamworkhq.com/job/456e67af-56b0-44b8-b0d7-be27fbf88a16","seen":"2026-11-13","location":"Bengaluru, India","seniority":"junior","years":0,"must":["0-2 yrs with a portfolio of AI experiments or automations","foundational Python automations","testing and evaluation (DeepEval or Promptfoo per an aggregator summary)"],"pay":{"lo":800000,"hi":1400000,"currency":"INR","period":"year"},"note":"Builder variant. Pay is aggregator-stated; another mirror shows 8.5-14 lakh. Years given as 0-2."}
{"type":"jd","grade":"B","src":["S43"],"as_of":"2026-11-13","ttl":"V1","role":"ai-enablement-engineer","employer":"Siemens","title":"AI Enablement Engineer (Architect)","url":"https://www.bayt.com/en/india/jobs/ai-enablement-engineer-architect-75250366/","job_id":"75250366","seen":"2026-11-13","location":"India (an Indeed listing shows Bengaluru)","seniority":"architect","must":["context packers assembling repo, doc and ticket context for AI tools (under 200 ms)","retrieval and context engineering"],"note":"Platform variant at a GCC. Application closes 2027-01-27; listed 4 days before its snapshot."}
{"type":"jd","grade":"B","src":["S44"],"as_of":"2026-11-02","ttl":"V1","role":"ai-enablement-engineer","employer":"Fintech (name withheld by recruiter)","title":"Platform Engineer Lead - AI Enablement","url":"https://www.itjobboard.co.uk/job/16937486/platform-engineer-lead-ai-enablement/","job_id":"16937486","seen":"2026-11-13","location":"London, UK","remote":"hybrid, 3 days in office","seniority":"lead","must":["platform engineering with AI enablement scope"],"pay":null,"note":"Platform variant. Recruiter listing: up to GBP 130,000 plus about 20% bonus (see pay records)."}
{"type":"jd","grade":"B","src":["S45"],"as_of":"2026-09-16","ttl":"V1","role":"ai-enablement-engineer","employer":"Phorest","title":"AI Enablement Engineer","url":"https://remowork.life/jobs/6aaa7e825d989acfeaf035d5/ai-enablement-engineer","seen":"2026-11-13","location":"Ireland or UK (remote)","remote":"remote","seniority":"staff","years":10,"must":["staff-level production software engineering","practical AI: AI-powered products, internal tooling or production LLM apps","multiplier: mentoring, governance of AI tooling, security and spend"],"note":"Builder variant. The body reads Staff Software Engineer, AI Enablement; 10+ years preferred."}
{"type":"jd","grade":"A","src":["S34"],"as_of":"2026-07-20","ttl":"V1","role":"ai-enablement-engineer","employer":"Xensam","title":"AI Enablement Engineer","url":"https://careers.xensam.com/jobs/8096505-ai-enablement-engineer","job_id":"8096505","seen":"2026-11-13","location":"Stockholm, Sweden","remote":"hybrid","seniority":"mid","years":3,"must":["3+ yrs software development","Python and API integrations","LLMs, RAG, vector databases and agent frameworks","open-source models, Linux and Docker"],"nice":["n8n, Make or Temporal","Bedrock, Azure AI or Vertex","portfolio of AI side projects"],"ats":"Teamtailor","note":"Read in full. Published 2026-07-20, modified 2026-10-14, live on 2026-11-13. Builder variant."}
```

### jd records: ai-product-engineer (16)

```jsonl
{"type":"jd","grade":"A","src":["S49"],"as_of":"2026-09-24","ttl":"V1","role":"ai-product-engineer","employer":"Within","title":"Senior/Staff AI Frontend Engineer","url":"https://www.ycombinator.com/companies/within/jobs/Am14EFK-staff-ai-frontend-engineer","job_id":"Am14EFK","seen":"2026-11-13","location":"San Francisco, CA, US","seniority":"staff","years":6,"degree":"not required","must":["React, Next.js, TypeScript and Tailwind","6+ yrs production frontend","AI-native tools (Cursor, Claude Code, v0, Lovable)","design sensibility and accessibility"],"nice":["portfolio or GitHub"],"pay":{"lo":235000,"hi":315000,"currency":"USD","period":"year"},"ats":"YC Work at a Startup","note":"Read in full. US citizen or visa holder only. Posted 2026-09-24 on a mirror. Indeed shows a second AI Frontend Engineer listing at $140,000-205,000."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Taktile","title":"Senior Full-Stack Engineer - Team Agent","url":"https://jobs.ashbyhq.com/taktile/c9d47dd2-3252-4266-a581-b9d1b46e9297","job_id":"c9d47dd2-3252-4266-a581-b9d1b46e9297","seen":"2026-11-13","location":null,"seniority":"senior","must":["React and TypeScript for rich interactive UIs","chat UI components, streaming responses and human-in-the-loop approvals","Python or FastAPI backend"],"ats":"Ashby","note":"Extract; age is relative: about 71 days before the aggregator snapshot; location not shown."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Pebl","title":"Senior Frontend Software Engineer, AI UX","url":"https://jobs.ashbyhq.com/pebl/e7f04c03-619d-420c-9201-d2a2e2ec0d84","job_id":"e7f04c03-619d-420c-9201-d2a2e2ec0d84","seen":"2026-11-13","location":null,"seniority":"senior","must":["React and TypeScript","interfaces for AI and agentic products, including generative UI","real-time and streaming integration"],"ats":"Ashby","note":"Extract; fetch failed; date and location not shown."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Arlo","title":"Product Engineer","url":"https://jobs.ashbyhq.com/arlo/1429423a-a98b-459d-8d89-b80e0862ab8c","job_id":"1429423a-a98b-459d-8d89-b80e0862ab8c","seen":"2026-11-13","location":null,"seniority":"unlabelled","must":["full-stack consumer apps (Python, Postgres, TypeScript, React, React Native)","streaming-response chat UI for an AI care partner","AI-assisted tools (Cursor, Copilot)"],"ats":"Ashby","note":"Extract; date and location not shown."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"humans&","title":"Product Engineer (Member of Technical Staff)","url":"https://jobs.ashbyhq.com/humans-and/c3a7fce6-0bb5-43c6-a2a7-01c63e4b1401","job_id":"c3a7fce6-0bb5-43c6-a2a7-01c63e4b1401","seen":"2026-11-13","location":null,"seniority":"unlabelled","must":["TypeScript with Convex, Next.js, React Native and Tailwind","product-builder ownership"],"ats":"Ashby","note":"Extract; date and location not shown. Frontier-lab-style startup."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Dash0","title":"Senior Product Engineer, Frontend (React, TypeScript)","url":"https://jobs.ashbyhq.com/dash0/bb433d72-7241-49b4-acfb-a6a403f9422c","job_id":"bb433d72-7241-49b4-acfb-a6a403f9422c","seen":"2026-11-13","location":null,"seniority":"senior","must":["React and TypeScript","data-intensive agent interface (Agent0)","product ownership"],"ats":"Ashby","note":"Extract; date and location not shown."}
{"type":"jd","grade":"B","src":["S1","S2"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Anthropic","title":"Product Engineer, Computer Use","url":"https://job-boards.greenhouse.io/anthropic/jobs/5238637008","job_id":"5238637008","seen":"2026-11-13","location":"San Francisco, New York or Seattle, US","seniority":"unlabelled, zero-to-one ownership","must":["zero-to-one product ownership as an early engineer","strong full-stack: production web frontend and backend","product design instincts"],"ats":"Greenhouse","note":"Extract; listed as open on Anthropic's careers index about 17 days before retrieval; posting date not shown. COI."}
{"type":"jd","grade":"B","src":["S4"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"OpenAI","title":"Software Engineer, ChatGPT Shopping","url":"https://jobs.ashbyhq.com/openai/ca54cd23-2bcc-4327-bcb6-46d81ed414a8/application","job_id":"ca54cd23-2bcc-4327-bcb6-46d81ed414a8","seen":"2026-11-13","location":"San Francisco, CA, US","seniority":"unlabelled","must":["end-to-end product experiences across web services, APIs and frontend","React, TypeScript, Next.js (preferred)"],"pay":{"lo":230000,"hi":385000,"currency":"USD","period":"year"},"ats":"Ashby","note":"Extract; date not shown; pay from an Ashby aggregator listing."}
{"type":"jd","grade":"B","src":["S51"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Amazon (Prime Video and Amazon MGM Studios)","title":"Frontend Engineer, AI Business Automation, Prime Video","url":"https://devsunite.com/jobs/prime-video-amazon-mgm-studios-frontend-engineer-ai-business-automation-prime-video-seattle-oct2026-141927","seen":"2026-11-13","location":"Seattle, WA, US","seniority":"mid","years":2,"must":["2+ yrs frontend (JavaScript, HTML, CSS, React)","browser-based creative editor with canvas compositing","integrate AI and ML outputs into interactive UI"],"ats":"Amazon (devsunite mirror)","note":"Extract; age is relative: about 14 days before the aggregator snapshot."}
{"type":"jd","grade":"B","src":["S51"],"as_of":"2026-10-06","ttl":"V1","role":"ai-product-engineer","employer":"CirrusLabs","title":"Software Engineer - AI Product Engineering","url":"https://jobfound.org/job/cirruslabs-is-hiring-for-software-engineer-ai-product-engineering-bengaluru-karnataka-india-6-october-2026","seen":"2026-11-13","location":"Bengaluru, India","seniority":"mid","years":2,"must":["MERN stack","practical AI-powered app experience","LLM and GenAI concepts"],"pay":{"lo":1000000,"hi":1800000,"currency":"INR","period":"year"},"ats":"CirrusLabs (jobfound mirror)","note":"Extract; posted 2026-10-06; stated 2-4 years; pay is aggregator-stated."}
{"type":"jd","grade":"B","src":["S51"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Lucid","title":"AI Engineer","url":"https://www.wearedevelopers.com/jobs/ext/2239710-ai-engineer","seen":"2026-11-13","location":"Berlin, Germany","seniority":"unlabelled","must":["production AI SDK layer (Vercel AI SDK) with streaming across providers","Next.js, React, TypeScript, Tailwind and shadcn"],"ats":"WeAreDevelopers listing","note":"Extract; age is relative: about 79 days before the aggregator snapshot. Title says AI Engineer; the work is full-stack AI web."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Clera","title":"Product Engineer (Full-Stack)","url":"https://jobs.ashbyhq.com/Clera/48f5376d-0222-4b2e-bf43-4d68d0ece121","job_id":"48f5376d-0222-4b2e-bf43-4d68d0ece121","seen":"2026-11-13","location":null,"seniority":"mid","years":2,"must":["Next.js, TypeScript and Node","AI-powered features in enterprise apps","product direction"],"ats":"Ashby","note":"Extract; age is relative: about 74 days before the aggregator snapshot."}
{"type":"jd","grade":"B","src":["S50"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"The Flex","title":"Product Engineer","url":"https://jobs.ashbyhq.com/The-Flex/8c9ad50d-0f19-48cb-a7d0-03906f774729","job_id":"8c9ad50d-0f19-48cb-a7d0-03906f774729","seen":"2026-11-13","location":null,"seniority":"unlabelled","must":["Python or FastAPI, React, TypeScript and Supabase","OpenAI APIs and LLM agents","product mindset"],"ats":"Ashby","note":"Extract; date and location not shown."}
{"type":"jd","grade":"C","src":["S52"],"as_of":"2026-10-02","ttl":"V1","role":"ai-product-engineer","employer":"eventfirst","title":"Senior Full-Stack Engineer","url":"https://hnhiring.com/technologies/react","seen":"2026-11-13","location":"Berlin, Germany (remote, CET)","remote":"remote","seniority":"senior","years":10,"must":["10+ yrs full-stack","some experience building an AI chat product","TypeScript, React, Next.js and Tailwind"],"ats":"none (Hacker News comment)","note":"Extract from an aggregator of the October 2026 thread; posted 2026-10-02."}
{"type":"jd","grade":"C","src":["S52"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"myDataValue","title":"Founding Product Engineer","url":"https://www.mydatavalue.com/founding-product-engineer/","seen":"2026-11-13","location":"London (Canary Wharf), UK","remote":"hybrid, 2 days a week","seniority":"founding","must":["Next.js, React, TypeScript and Tailwind","product ownership"],"pay":null,"ats":"none (Hacker News comment)","note":"Extract from the November 2026 thread. Stated: up to GBP 90,000 plus up to 1% equity (see pay records)."}
{"type":"jd","grade":"B","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","employer":"Alpha","title":"Frontend Design Engineer (Figma, React, TypeScript)","url":"https://www.productbased.in/jobs/frontend","seen":"2026-11-13","location":"India (remote)","remote":"remote","seniority":"junior","years":0.5,"must":["React and TypeScript","Figma design craft","AI-native go-to-market workspace"],"pay":{"lo":400000,"hi":800000,"currency":"INR","period":"year"},"ats":"none (aggregator)","note":"Extract; date not shown; stated 0.5-3 years; pay plus ESOPs."}
```

### skill_signal records

Sample shares are floors from extracts (grade M); platform shares are grade B. Suggested tiers apply the rule set out in the skills tables (Must at 45% or more, Important 25–44%, Should 10–24%, Optional below 10%), with the exceptions noted.

```jsonl
{"type":"skill_signal","grade":"M","src":["S1","S3","S5","S7","S8","S9","S10","S11","S12","S13","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"new:customer_facing_technical","n":23,"source_kind":"jd-sample","count":22,"share":0.957,"tier_hint":"Must","note":"Explicit customer-facing technical experience (SA, SE, TAM, FDE, consulting). Floor from extracts."}
{"type":"skill_signal","grade":"M","src":["S1","S3","S5","S7","S8","S9","S10","S11","S12","S13","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"presales","n":23,"source_kind":"jd-sample","count":14,"share":0.609,"tier_hint":"Must","note":"Explicit pre-sales, technical sales or go-to-market partnership. Pre-sales or field-aligned postings overall: 15 of 23."}
{"type":"skill_signal","grade":"M","src":["S5","S7","S8","S9","S10","S11","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"cloud","n":23,"source_kind":"jd-sample","count":12,"share":0.522,"tier_hint":"Must","note":"Named in hyperscaler and consultancy postings; not in lab extracts."}
{"type":"skill_signal","grade":"M","src":["S3","S5","S7","S8","S9","S10","S11","S12","S13","S14"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"agents","n":23,"source_kind":"jd-sample","count":13,"share":0.565,"tier_hint":"Important","note":"Mechanical Must; held at Important because queries named agentic titles."}
{"type":"skill_signal","grade":"M","src":["S8","S9","S11","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"azure","n":23,"source_kind":"jd-sample","count":7,"share":0.304,"tier_hint":"Important","note":"KB platform share 29.5%."}
{"type":"skill_signal","grade":"M","src":["S7","S9","S11","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"gcp","n":23,"source_kind":"jd-sample","count":7,"share":0.304,"tier_hint":"Important","note":"Google Customer Engineer postings count as Google Cloud. KB platform share 22.6%."}
{"type":"skill_signal","grade":"M","src":["S5","S9","S11","S14","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"aws","n":23,"source_kind":"jd-sample","count":6,"share":0.261,"tier_hint":"Important","note":"KB share 53.6% not replicated."}
{"type":"skill_signal","grade":"M","src":["S7","S9","S10","S13","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"new:rag","n":23,"source_kind":"jd-sample","count":6,"share":0.261,"tier_hint":"Important","note":"Appears in the interview track, not on the skill card."}
{"type":"skill_signal","grade":"M","src":["S7","S8","S11"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"managed_ai","n":23,"source_kind":"jd-sample","count":5,"share":0.217,"tier_hint":"Should","note":"Named platforms only (Vertex AI, Foundry, Copilot Studio, Bedrock Agents)."}
{"type":"skill_signal","grade":"M","src":["S1","S3","S10","S15"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"evals","n":23,"source_kind":"jd-sample","count":4,"share":0.174,"tier_hint":"Should","note":"Anthropic, OpenAI, Databricks, Tribe AI."}
{"type":"skill_signal","grade":"M","src":["S3","S12","S13"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"grc","n":23,"source_kind":"jd-sample","count":4,"share":0.174,"tier_hint":"Should","note":"Governance, Responsible AI and risk language."}
{"type":"skill_signal","grade":"M","src":["S9","S10"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"guardrails","n":23,"source_kind":"jd-sample","count":2,"share":0.087,"tier_hint":"Optional","note":"Databricks only."}
{"type":"skill_signal","grade":"M","src":["S11"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"mcp","n":23,"source_kind":"jd-sample","count":1,"share":0.043,"tier_hint":"Optional","note":"Accenture only."}
{"type":"skill_signal","grade":"M","src":["S13"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"iam","n":23,"source_kind":"jd-sample","count":1,"share":0.043,"tier_hint":"Should","note":"PwC only. Floor; keep the KB tier until a full-text read."}
{"type":"skill_signal","grade":"M","src":["S13"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"model_selection","n":23,"source_kind":"jd-sample","count":1,"share":0.043,"tier_hint":"Should","note":"PwC model routing. Floor; keep the KB tier until a full-text read."}
{"type":"skill_signal","grade":"M","src":["S13"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"cost_latency","n":23,"source_kind":"jd-sample","count":1,"share":0.043,"tier_hint":"Should","note":"PwC cost and latency constraints. Floor; keep the KB tier until a full-text read."}
{"type":"skill_signal","grade":"M","src":["S8"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","skill":"new:certification_named","n":23,"source_kind":"jd-sample","count":1,"share":0.043,"tier_hint":"Optional","note":"Microsoft Belgium prefers a technical certification. Two more in-window postings outside the sample name certifications (3 of 25 = 12%)."}
{"type":"skill_signal","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","role":"ai-solutions-architect","skill":"cloud","n":16927,"source_kind":"platform","share":0.62,"tier_hint":"Must","note":"Axial, US AI-architecture postings."}
{"type":"skill_signal","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","role":"ai-solutions-architect","skill":"python","n":16927,"source_kind":"platform","share":0.44,"tier_hint":"Important","note":"Axial, US AI-architecture postings."}
{"type":"skill_signal","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","role":"ai-solutions-architect","skill":"new:observability","n":16927,"source_kind":"platform","share":0.39,"tier_hint":"Important","note":"Axial; not on the KB card."}
{"type":"skill_signal","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","role":"ai-solutions-architect","skill":"new:foundation_models","n":16927,"source_kind":"platform","share":0.38,"tier_hint":"Important","note":"Axial; not on the KB card."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"teaching","n":15,"source_kind":"jd-sample","count":9,"share":0.6,"tier_hint":"Must","note":"Training, workshops or enablement sessions. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S33","S37","S38","S40","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"internal_tooling","n":15,"source_kind":"jd-sample","count":7,"share":0.467,"tier_hint":"Must","note":"Builder and platform variants. KB tier Must."}
{"type":"skill_signal","grade":"M","src":["S35","S36","S39","S40","S41","S34"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"change_mgmt","n":15,"source_kind":"jd-sample","count":7,"share":0.467,"tier_hint":"Must","note":"Adoption and rollout language. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S37","S40","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"agents","n":15,"source_kind":"jd-sample","count":5,"share":0.333,"tier_hint":"Important","note":"Platform share 16.7% (n = 42)."}
{"type":"skill_signal","grade":"M","src":["S33","S35","S37","S38","S40"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"coding_agents","n":15,"source_kind":"jd-sample","count":5,"share":0.333,"tier_hint":"Important","note":"Claude, Cursor and Copilot rollouts; AI coding tools as a working method."}
{"type":"skill_signal","grade":"M","src":["S35","S36","S39","S40","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"pilots","n":15,"source_kind":"jd-sample","count":5,"share":0.333,"tier_hint":"Important","note":"Pilots, adoption metrics, productivity measurement."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S39","S40","S42"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"new:prompt_engineering","n":15,"source_kind":"jd-sample","count":5,"share":0.333,"tier_hint":"Important","note":"Platform share 35.7% (n = 42). Not on the KB card."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S35","S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"python","n":15,"source_kind":"jd-sample","count":4,"share":0.267,"tier_hint":"Important","note":"KB tier Must; KB share 78.4% not replicated. Platform share 33.3%."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S37","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"llm_apis","n":15,"source_kind":"jd-sample","count":4,"share":0.267,"tier_hint":"Important","note":"KB tier Must; KB share 76.7% not replicated."}
{"type":"skill_signal","grade":"M","src":["S35","S37","S38","S40"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"mcp","n":15,"source_kind":"jd-sample","count":4,"share":0.267,"tier_hint":"Important","note":"Core in one posting (Sofi). Platform share 19.0%."}
{"type":"skill_signal","grade":"M","src":["S33","S35","S41","S45"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"grc","n":15,"source_kind":"jd-sample","count":4,"share":0.267,"tier_hint":"Important","note":"Governance, audit, compliance. Not on the KB card."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S37","S39"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"new:low_code_automation","n":15,"source_kind":"jd-sample","count":4,"share":0.267,"tier_hint":"Important","note":"n8n, Make, Zapier, Power Automate, Power Platform."}
{"type":"skill_signal","grade":"M","src":["S33","S34","S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"new:rag","n":15,"source_kind":"jd-sample","count":3,"share":0.2,"tier_hint":"Should","note":"Platform share 19.0%."}
{"type":"skill_signal","grade":"M","src":["S33","S37","S42"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"evals","n":15,"source_kind":"jd-sample","count":3,"share":0.2,"tier_hint":"Should","note":"Revalize, Fabletics, Ather."}
{"type":"skill_signal","grade":"M","src":["S33","S35","S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"iam","n":15,"source_kind":"jd-sample","count":3,"share":0.2,"tier_hint":"Should","note":"KB tier Must. Must inside the platform variant only. Platform SSO 11.9%, OAuth 9.5%."}
{"type":"skill_signal","grade":"M","src":["S35","S40"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"claude_code","n":15,"source_kind":"jd-sample","count":2,"share":0.133,"tier_hint":"Should","note":"Platform share 14.3%."}
{"type":"skill_signal","grade":"M","src":["S33","S35"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"guardrails","n":15,"source_kind":"jd-sample","count":2,"share":0.133,"tier_hint":"Should","note":"KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S35","S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"typescript","n":15,"source_kind":"jd-sample","count":2,"share":0.133,"tier_hint":"Should","note":"Platform share 28.6%."}
{"type":"skill_signal","grade":"M","src":["S35"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"llm_gateways","n":15,"source_kind":"jd-sample","count":1,"share":0.067,"tier_hint":"Optional","note":"Sofi only. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","skill":"new:certification_named","n":15,"source_kind":"jd-sample","count":1,"share":0.067,"tier_hint":"Optional","note":"Revalize prefers unspecified 'related certifications'."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"new:prompt_engineering","n":42,"source_kind":"platform","count":15,"share":0.357,"tier_hint":"Important","note":"Skillenai, 90 days to 2026-11-05."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"python","n":42,"source_kind":"platform","count":14,"share":0.333,"tier_hint":"Important","note":"Skillenai."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"typescript","n":42,"source_kind":"platform","count":12,"share":0.286,"tier_hint":"Important","note":"Skillenai."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"mcp","n":42,"source_kind":"platform","count":8,"share":0.19,"tier_hint":"Should","note":"Skillenai. KB derived 30.2% (16 of 53) is not replicated."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"new:rag","n":42,"source_kind":"platform","count":8,"share":0.19,"tier_hint":"Should","note":"Skillenai lists a second RAG entry at 11.9%; the two may overlap."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"agents","n":42,"source_kind":"platform","count":7,"share":0.167,"tier_hint":"Should","note":"Skillenai."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"claude_code","n":42,"source_kind":"platform","count":6,"share":0.143,"tier_hint":"Should","note":"Skillenai."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"aws","n":42,"source_kind":"platform","count":6,"share":0.143,"tier_hint":"Should","note":"Skillenai."}
{"type":"skill_signal","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V3","role":"ai-enablement-engineer","skill":"iam","n":42,"source_kind":"platform","count":5,"share":0.119,"tier_hint":"Should","note":"Skillenai SSO share; OAuth 9.5% (4 of 42)."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"react","n":16,"source_kind":"jd-sample","count":15,"share":0.938,"tier_hint":"Must","note":"Next.js counted as React. Anthropic extract does not name it. KB platform share 69.4%."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"typescript","n":16,"source_kind":"jd-sample","count":13,"share":0.813,"tier_hint":"Must","note":"KB platform share 52.7%."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S50","S51","S52"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"llm_apis","n":16,"source_kind":"jd-sample","count":11,"share":0.688,"tier_hint":"Must","note":"LLM integration, agents, AI SDK work."}
{"type":"skill_signal","grade":"M","src":["S1","S49","S50","S52"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"product_sense","n":16,"source_kind":"jd-sample","count":8,"share":0.5,"tier_hint":"Must","note":"Product ownership language. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S4","S49","S50","S51","S52"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"nextjs","n":16,"source_kind":"jd-sample","count":7,"share":0.438,"tier_hint":"Important","note":"Within, humans&, OpenAI, Lucid, Clera, eventfirst, myDataValue."}
{"type":"skill_signal","grade":"M","src":["S1","S49","S50","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"new:design_craft","n":16,"source_kind":"jd-sample","count":6,"share":0.375,"tier_hint":"Important","note":"Design sensibility. Accessibility named explicitly only by Within."}
{"type":"skill_signal","grade":"M","src":["S50","S51"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"streaming_ux","n":16,"source_kind":"jd-sample","count":4,"share":0.25,"tier_hint":"Important","note":"Taktile, Pebl, Arlo, Lucid."}
{"type":"skill_signal","grade":"M","src":["S50"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"python","n":16,"source_kind":"jd-sample","count":3,"share":0.188,"tier_hint":"Should","note":"KB platform share 41.8%."}
{"type":"skill_signal","grade":"M","src":["S50","S51"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"cloud","n":16,"source_kind":"jd-sample","count":2,"share":0.125,"tier_hint":"Should","note":"KB platform share 41.3%."}
{"type":"skill_signal","grade":"M","src":["S50","S51"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"nodejs","n":16,"source_kind":"jd-sample","count":2,"share":0.125,"tier_hint":"Should","note":"KB platform share 32.3%."}
{"type":"skill_signal","grade":"M","src":["S49","S50"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"new:ai_coding_tools","n":16,"source_kind":"jd-sample","count":2,"share":0.125,"tier_hint":"Should","note":"Within (Cursor, Claude Code, v0, Lovable) and Arlo."}
{"type":"skill_signal","grade":"M","src":["S50"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"hitl_design","n":16,"source_kind":"jd-sample","count":1,"share":0.063,"tier_hint":"Optional","note":"Taktile."}
{"type":"skill_signal","grade":"M","src":["S50"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"generative_ui","n":16,"source_kind":"jd-sample","count":1,"share":0.063,"tier_hint":"Optional","note":"Pebl."}
{"type":"skill_signal","grade":"M","src":["S51"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"vercel_ai_sdk","n":16,"source_kind":"jd-sample","count":1,"share":0.063,"tier_hint":"Optional","note":"Lucid."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"evals","n":16,"source_kind":"jd-sample","count":0,"share":0.0,"tier_hint":"Optional","note":"Not named in any extract. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"ux_telemetry","n":16,"source_kind":"jd-sample","count":0,"share":0.0,"tier_hint":"Optional","note":"Not named in any extract. KB tier Important."}
{"type":"skill_signal","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","skill":"sse","n":16,"source_kind":"jd-sample","count":0,"share":0.0,"tier_hint":"Optional","note":"Not named in any extract. KB tier Important."}
```

### pay records

```jsonl
{"type":"pay","grade":"B","src":["S7"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Google Careers, Customer Engineer III Cloud AI","lo":152000,"hi":221000,"level":"CE III","employer_type":"big-tech","n":1,"note":"Plus 42.86% bonus target and equity."}
{"type":"pay","grade":"B","src":["S10"],"as_of":"2026-08-14","ttl":"V1","role":"ai-solutions-architect","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Databricks, Specialist Solutions Architect AI/ML (FEQ427R382)","lo":180000,"hi":247500,"level":"senior specialist","employer_type":"other","n":1,"note":"'Local Pay Range'; OTE not stated."}
{"type":"pay","grade":"B","src":["S6"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","location":"US (Seattle, Dallas)","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Amazon, Sr. GenAI Specialist SA, Agentic AI (Dreamwork mirror)","lo":153600,"hi":207800,"level":"senior specialist","employer_type":"big-tech","n":1}
{"type":"pay","grade":"B","src":["S6"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","location":"US (Santa Clara)","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Amazon, Sr. GenAI Specialist SA, Agentic AI (Dreamwork mirror)","lo":176600,"hi":239000,"level":"senior specialist","employer_type":"big-tech","n":1}
{"type":"pay","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","location":"London, UK","stat":"range","currency":"GBP","period":"year","basis":"tc","source_name":"Anthropic, Applied AI Architect, Startups (5432573008)","lo":165000,"hi":190000,"level":"mid-senior","employer_type":"frontier-lab","n":1,"note":"OTE: base plus commission; equity not included. COI."}
{"type":"pay","grade":"B","src":["S8"],"as_of":"2026-10-11","ttl":"V1","role":"ai-solutions-architect","location":"Belgium","stat":"range","currency":"EUR","period":"year","basis":"base","source_name":"Microsoft, Cloud Solution Architect Copilot and AI (mirror)","lo":55400,"hi":93700,"level":"IC3","employer_type":"big-tech","n":1}
{"type":"pay","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Axial Search, AI architecture postings","value":189000,"n":16927,"note":"Median of posted bands across the class. Axial does not say base or OTE."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Solution Architect (all companies)","value":220000,"n":1200,"note":"p25 170,000; p75 280,000; p90 347,000. Page undated. Another snapshot shows 218,500."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Levels.fyi, Solution Architect (all companies)","value":180000,"n":1200,"note":"Median base. Page undated."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-01-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Databricks Solution Architect","value":218000,"level":"L3","employer_type":"other","note":"Base about 134,000."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-01-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Databricks Solution Architect","value":349000,"level":"L5 (Senior SA)","employer_type":"other","note":"Base about 172,000."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-01-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"mean","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Databricks Solution Architect","value":359000,"level":"L6 (Staff SA)","employer_type":"other","note":"Base about 197,000."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"offer","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, OpenAI Solution Architect","value":418000,"n":1,"employer_type":"frontier-lab","note":"Base about 218,000; stock about 200,000 a year. Single report; page undated."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2026-02-27","ttl":"V3","role":"ai-solutions-architect","location":"France","stat":"range","currency":"EUR","period":"year","basis":"tc","source_name":"Levels.fyi, Anthropic Solution Architect","lo":154000,"hi":218000,"employer_type":"frontier-lab","note":"Average total compensation range on the page. COI."}
{"type":"pay","grade":"C","src":["S28"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Inference Jobs, Anthropic Solutions Architecture","lo":241200,"hi":272600,"n":15,"employer_type":"frontier-lab","note":"Average of posted ranges across 15 postings; basis not stated. COI."}
{"type":"pay","grade":"C","src":["S29"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"AmbitionBox via upGrad, AI Solutions Architect","lo":3190000,"hi":3530000,"level":"6-9 years","note":"Top 10% about 4,050,000."}
{"type":"pay","grade":"C","src":["S29"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"AmbitionBox via upGrad, AI Solutions Architect","lo":4180000,"hi":4620000,"level":"9-12 years","note":"Top 10% about 6,000,000."}
{"type":"pay","grade":"C","src":["S29"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"AmbitionBox via upGrad, AI Solutions Architect","lo":4450000,"hi":4920000,"level":"12+ years","note":"Top 10% about 6,500,000."}
{"type":"pay","grade":"C","src":["S29"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"Glassdoor India via futurense, AI Solutions Architect","lo":1425000,"hi":3750000,"note":"Average about 2,400,000."}
{"type":"pay","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V1","role":"ai-solutions-architect","location":"Bengaluru, India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"Cognizant, AIML Solution Architect (aggregator)","lo":3900000,"hi":5600000,"level":"8-12 years","employer_type":"it-services","n":1,"note":"Aggregator-stated; component not stated."}
{"type":"pay","grade":"B","src":["S27"],"as_of":"2025-11-07","ttl":"V3","role":"ai-solutions-architect","location":"Bengaluru, India","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Solution Architect, Bengaluru","value":56221,"note":"p25 40,800; p75 76,900. Predates 2026; stale flag."}
{"type":"pay","grade":"A","src":["S33"],"as_of":"2026-08-23","ttl":"V1","role":"ai-enablement-engineer","location":"El Segundo, CA, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Fabletics, AI Enablement Engineer (R8529)","lo":160378,"hi":180000,"level":"5 years","employer_type":"enterprise","n":1}
{"type":"pay","grade":"B","src":["S36"],"as_of":"2026-08-25","ttl":"V1","role":"ai-enablement-engineer","location":"Dallas, TX, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Inspyr mirror of the Scotiabank-text posting (26-158990)","lo":120000,"hi":140000,"level":"mid","employer_type":"enterprise","n":1,"note":"Direct hire; the mirror does not name the employer."}
{"type":"pay","grade":"B","src":["S44"],"as_of":"2026-11-02","ttl":"V1","role":"ai-enablement-engineer","location":"London, UK","stat":"offer","currency":"GBP","period":"year","basis":"base","source_name":"Client-Server listing, Platform Engineer Lead - AI Enablement","value":130000,"level":"lead","employer_type":"enterprise","n":1,"note":"Stated as up to 130,000 plus about 20% bonus."}
{"type":"pay","grade":"B","src":["S42"],"as_of":"2026-10-28","ttl":"V1","role":"ai-enablement-engineer","location":"Bengaluru, India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"Ather Energy, AI Enablement Engineer (aggregator)","lo":800000,"hi":1400000,"level":"0-2 years","employer_type":"other","n":1,"note":"Aggregator-stated; another mirror shows 8.5-14 lakh."}
{"type":"pay","grade":"A","src":["S49"],"as_of":"2026-11-06","ttl":"V1","role":"ai-product-engineer","location":"San Francisco, CA, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Within, Staff AI Frontend Engineer (YC page)","lo":235000,"hi":315000,"level":"staff","employer_type":"ai-startup","n":1}
{"type":"pay","grade":"B","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Indeed listing, Within Senior/Staff AI Frontend Engineer","lo":185000,"hi":315000,"level":"senior-staff","employer_type":"ai-startup","n":1}
{"type":"pay","grade":"B","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Indeed listing, Within AI Frontend Engineer","lo":140000,"hi":205000,"level":"mid","employer_type":"ai-startup","n":1}
{"type":"pay","grade":"B","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"ZipRecruiter listing, Senior Staff AI Frontend Engineer","lo":250000,"hi":315000,"level":"senior-staff","n":1,"note":"Likely the same employer as the Within posting; not confirmed."}
{"type":"pay","grade":"B","src":["S4"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"San Francisco, CA, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"OpenAI, Software Engineer ChatGPT Shopping (Ashby aggregator)","lo":230000,"hi":385000,"employer_type":"frontier-lab","n":1,"note":"Aggregator listing; base versus total not stated."}
{"type":"pay","grade":"C","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"New York, US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"ZipRecruiter listing, Staff AI Product Engineer","lo":200000,"hi":300000,"level":"staff","n":1}
{"type":"pay","grade":"C","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"ZipRecruiter listing, Camber AI Product Engineer","lo":190000,"hi":230000,"n":1}
{"type":"pay","grade":"C","src":["S52"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"London, UK","stat":"offer","currency":"GBP","period":"year","basis":"base","source_name":"myDataValue, Founding Product Engineer (Hacker News)","value":90000,"level":"founding","employer_type":"ai-startup","n":1,"note":"Stated as up to 90,000 plus up to 1% equity."}
{"type":"pay","grade":"B","src":["S51"],"as_of":"2026-10-06","ttl":"V1","role":"ai-product-engineer","location":"Bengaluru, India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"CirrusLabs, Software Engineer AI Product Engineering (aggregator)","lo":1000000,"hi":1800000,"level":"2-4 years","employer_type":"it-services","n":1}
{"type":"pay","grade":"B","src":["S53"],"as_of":"2026-11-13","ttl":"V1","role":"ai-product-engineer","location":"India (remote)","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"Alpha, Frontend Design Engineer (aggregator)","lo":400000,"hi":800000,"level":"0.5-3 years","employer_type":"ai-startup","n":1,"note":"Plus ESOPs."}
```

### measure records

```jsonl
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V1","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_postings_since_2026_01","unit":"postings","value":16927,"n":16927,"method":"Axial Search classified function 'AI Architecture', US postings since January 2026","region":"US","note":"Proxy: the class is broader than the AI Solutions Architect title."}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V1","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_postings_qoq_change","unit":"percent","value":24,"method":"last quarter against the prior quarter, same tracked terms","region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_mid_level_ic","unit":"percent","value":45,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_principal_ic","unit":"percent","value":9,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_director_plus","unit":"percent","value":5,"region":"US","note":"Stated as about 5%."}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_firms_over_10000_staff","unit":"percent","value":44,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_it_services","unit":"percent","value":23,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_technology","unit":"percent","value":22,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_professional_services","unit":"percent","value":22,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_contract","unit":"percent","value":15,"region":"US"}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_median_years_required","unit":"years","value":7,"region":"US","note":"Principal IC about 10."}
{"type":"measure","grade":"B","src":["S18"],"as_of":"2026-08-25","ttl":"V3","subject":"role:ai-solutions-architect","measure":"us_ai_architecture_share_aws_solutions_architect_certification","unit":"percent","value":1.7,"region":"US"}
{"type":"measure","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"jobspipe_live_solutions_architect_us","unit":"live postings","value":1515,"region":"US","method":"JobsPipe live count across ATS sources; page undated","note":"Equals the KB's K3 figure dated 2026-11-02. Not AI-specific; AI share not re-verified."}
{"type":"measure","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"jobspipe_live_solutions_architect_india","unit":"live postings","value":64,"region":"India","method":"JobsPipe live count; page undated"}
{"type":"measure","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"jobspipe_live_solutions_architect_global","unit":"live postings","value":2718,"region":"global","method":"JobsPipe live count; page undated"}
{"type":"measure","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"jobspipe_live_senior_solutions_architect_global","unit":"live postings","value":1125,"region":"global","method":"JobsPipe live count; page undated"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"skillenai_solutions_architect_postings_90d","unit":"postings","value":3430,"region":"global","method":"Skillenai roles page, 90-day window; page undated","note":"Generic SA, not AI-specific. Coverage changed between reads; not a trend."}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"skillenai_solution_architect_postings_90d","unit":"postings","value":2335,"region":"global","method":"Skillenai roles page, variant spelling"}
{"type":"measure","grade":"B","src":["S23"],"as_of":"2026-08-01","ttl":"V1","subject":"role:ai-solutions-architect","measure":"skillenai_solutions_architect_postings_90d","unit":"postings","value":1684,"region":"global","method":"90 days to 2026-08-01, via a talents.vaia.com mirror"}
{"type":"measure","grade":"B","src":["S23"],"as_of":"2026-08-01","ttl":"V1","subject":"role:ai-solutions-architect","measure":"skillenai_solutions_architect_change_vs_prior_4_weeks","unit":"percent","value":25,"region":"global"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-solutions-architect","measure":"skillenai_forward_deployed_engineer_postings_90d","unit":"postings","value":1734,"region":"global","note":"Adjacent role; context only."}
{"type":"measure","grade":"C","src":["S25"],"as_of":"2026-07-05","ttl":"V1","subject":"role:ai-solutions-architect","measure":"corvi_solution_architecture_jobs_us","unit":"jobs","value":1347,"region":"US","note":"Category snapshot; not AI-specific."}
{"type":"measure","grade":"C","src":["S25"],"as_of":"2026-07-05","ttl":"V1","subject":"role:ai-solutions-architect","measure":"corvi_solution_architecture_jobs_india","unit":"jobs","value":761,"region":"India","note":"Conflicts with JobsPipe India 64; coverage differs."}
{"type":"measure","grade":"C","src":["S25"],"as_of":"2026-07-05","ttl":"V1","subject":"role:ai-solutions-architect","measure":"corvi_solution_architecture_jobs_bengaluru","unit":"jobs","value":325,"region":"Bengaluru"}
{"type":"measure","grade":"M","src":["S1","S3","S5","S7","S8","S9","S10","S11","S12","S13","S14","S15"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-solutions-architect","measure":"sample_presales_or_field_share","unit":"percent","value":65.2,"n":23,"method":"15 of 23 sampled postings classified pre-sales or field-aligned"}
{"type":"measure","grade":"M","src":["S1","S9","S7","S11","S13","S14","S15"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-solutions-architect","measure":"sample_median_stated_minimum_years","unit":"years","value":6.5,"n":10,"method":"Median of stated minimums among 10 postings that state years; range 3 to 10"}
{"type":"measure","grade":"M","src":["S8"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-solutions-architect","measure":"sample_certification_named_share","unit":"percent","value":4.3,"n":23,"note":"1 of 23. Adding two in-window postings outside the sample gives 3 of 25 (12.0%)."}
{"type":"measure","grade":"M","src":["S1","S3"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-solutions-architect","measure":"sample_lab_postings_using_applied_ai_architect_title","unit":"percent","value":57.1,"n":7,"method":"4 of 7 frontier-lab postings"}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"databricks_lca_solutions_architect_positions_fy2026","unit":"positions","value":90,"region":"US","method":"Aggregator of Department of Labor LCA disclosure data","note":"Median filed wage $139,059. Filed wages are not pay."}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"databricks_lca_specialist_sa_positions_fy2026","unit":"positions","value":28,"region":"US","note":"Median filed wage $155,491. Filed wages are not pay."}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"databricks_lca_senior_sa_positions_fy2026","unit":"positions","value":27,"region":"US","note":"Median filed wage $164,403. Filed wages are not pay."}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"databricks_lca_resident_sa_positions_fy2026","unit":"positions","value":46,"region":"US"}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"databricks_lca_delivery_sa_positions_fy2026","unit":"positions","value":37,"region":"US"}
{"type":"measure","grade":"B","src":["S56"],"as_of":"2026-11-13","ttl":"V4","subject":"role:ai-solutions-architect","measure":"openai_lca_solutions_architect_certified_seen","unit":"filings","value":2,"region":"US","note":"Go-to-market Solutions Architect filings seen: $290,000 San Francisco (2026-04-21) and $278,000 New York (2026-04-20). One tracker reports no FY2026 OpenAI filings (entity naming conflict). Filed wages are not pay."}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"aws_aip_c01_exam_fee","unit":"USD","value":300,"note":"Third-party sources agree; AWS page not opened. Pass mark 750 of 1000."}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"aws_aip_c01_exam_duration","unit":"minutes","value":180,"note":"One source lists 205 minutes; the majority list 180."}
{"type":"measure","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"aws_aip_c01_exam_questions","unit":"questions","value":75,"note":"65 scored plus 10 unscored; one source lists 85."}
{"type":"measure","grade":"B","src":["S57"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"gcp_pmle_exam_fee","unit":"USD","value":200,"note":"Issuer page excerpt; exam guide dated 2026-06-01."}
{"type":"measure","grade":"B","src":["S57"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"gcp_pmle_exam_duration","unit":"minutes","value":120}
{"type":"measure","grade":"B","src":["S57"],"as_of":"2026-11-13","ttl":"V2","subject":"role:ai-solutions-architect","measure":"gcp_pmle_exam_questions","unit":"questions","lo":50,"hi":60}
{"type":"measure","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"skillenai_ai_enablement_engineer_postings_90d","unit":"postings","value":42,"region":"global","method":"Skillenai role page, 90 days to 2026-11-05"}
{"type":"measure","grade":"B","src":["S21"],"as_of":"2026-09-03","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"skillenai_ai_enablement_engineer_postings_90d","unit":"postings","value":57,"region":"global","method":"Skillenai, 90 days to 2026-09-03","note":"KB's K18 estimated about 53 from an MCP share."}
{"type":"measure","grade":"B","src":["S21"],"as_of":"2026-09-03","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"skillenai_ai_enablement_engineer_change_vs_prior_4_weeks","unit":"percent","value":-35,"region":"global"}
{"type":"measure","grade":"B","src":["S21"],"as_of":"2026-09-02","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"skillenai_ai_enablement_lead_postings_90d","unit":"postings","value":26,"region":"global","method":"Skillenai, 90 days to 2026-09-02"}
{"type":"measure","grade":"M","src":["S20","S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"enablement_share_of_skillenai_ai_engineer_count","unit":"percent","value":1.0,"n":42,"method":"42 of 4,139 postings per 90 days; the two readings differ by a few days"}
{"type":"measure","grade":"B","src":["S20"],"as_of":"2026-11-05","ttl":"V1","subject":"role:ai-enablement-engineer","measure":"skillenai_enablement_max_postings_per_employer","unit":"postings","value":3,"region":"global","note":"CloudZero 3; Coder, INSPYR, Socure, ID.me and others 2 each."}
{"type":"measure","grade":"M","src":["S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_variant_share_adoption_or_training_lead","unit":"percent","value":20,"n":15,"method":"3 of 15: Scotiabank, Liquidity Services, Jorie AI"}
{"type":"measure","grade":"M","src":["S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_variant_share_builder_enabler","unit":"percent","value":60,"n":15,"method":"9 of 15"}
{"type":"measure","grade":"M","src":["S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_variant_share_platform_mcp_context","unit":"percent","value":20,"n":15,"method":"3 of 15: Sofi, Siemens, London platform lead"}
{"type":"measure","grade":"M","src":["S33","S34","S35","S36","S37","S38","S39","S40","S41","S42","S43","S44","S45"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_explicitly_remote_share","unit":"percent","value":40,"n":15,"method":"6 of 15; hybrid 4; unspecified 5"}
{"type":"measure","grade":"M","src":["S33","S34","S35","S37","S39","S40","S42","S45"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_median_stated_minimum_years","unit":"years","value":4.5,"n":8,"method":"Median of stated minimums among 8 postings; range 0 to 10"}
{"type":"measure","grade":"M","src":["S35","S37","S38","S40"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_specialisation_mcp_and_agent_protocols_named_share","unit":"percent","value":26.7,"n":15,"method":"MCP named in 4 of 15; core to the role in 1 (Sofi); platform share 19.0%"}
{"type":"measure","grade":"M","src":["S37"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-enablement-engineer","measure":"sample_certification_named_share","unit":"percent","value":6.7,"n":15,"note":"1 of 15, generic 'related certifications'."}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-product-engineer","measure":"skillenai_ai_engineer_postings_90d","unit":"postings","value":4139,"region":"global","note":"Context for the family; not the AI Product Engineer title."}
{"type":"measure","grade":"B","src":["S26"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-product-engineer","measure":"jobspipe_ai_engineer_live","unit":"live postings","value":3944,"region":"global","note":"Context only; page undated."}
{"type":"measure","grade":"B","src":["S26"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ai-product-engineer","measure":"fastaijobs_fullstack_engineer_open_roles","unit":"roles","value":497,"n":313,"method":"Open full-stack roles across 313 AI startups; page undated","note":"Context only."}
{"type":"measure","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_ai_facing_ui_specialist_share","unit":"percent","value":31.3,"n":16,"method":"5 of 16: Taktile, Pebl, Dash0, Prime Video, Lucid"}
{"type":"measure","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_product_engineer_shipping_ai_features_share","unit":"percent","value":43.8,"n":16,"method":"7 of 16"}
{"type":"measure","grade":"M","src":["S49","S50","S52"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_senior_or_staff_title_share","unit":"percent","value":31.3,"n":16,"method":"5 of 16: Within, Taktile, Pebl, Dash0, eventfirst"}
{"type":"measure","grade":"M","src":["S49","S51","S50","S52","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_median_stated_minimum_years","unit":"years","value":2,"n":6,"method":"Median of stated minimums among 6 postings; range 0.5 to 10"}
{"type":"measure","grade":"M","src":["S50","S52"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_specialisation_conversational_ui_share","unit":"percent","value":25.0,"n":16,"method":"4 of 16: Taktile, Pebl, Arlo, eventfirst"}
{"type":"measure","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_specialisation_voice_agents_share","unit":"percent","value":0,"n":16}
{"type":"measure","grade":"M","src":["S1","S4","S49","S50","S51","S52","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_specialisation_edge_on_device_share","unit":"percent","value":0,"n":16}
{"type":"measure","grade":"M","src":["S51","S53"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ai-product-engineer","measure":"sample_india_share","unit":"percent","value":12.5,"n":16,"method":"2 of 16: CirrusLabs, Alpha"}
```

### loop records

```jsonl
{"type":"loop","grade":"C","src":["S30","S1"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","employer":"Anthropic","track":"application","stages":["recruiter screen","technical conversation on architecture","take-home with live demo, or customer-scenario presentation","safety and judgement conversation","cross-functional and behavioural"],"formats":["4-6 rounds over 3-6 weeks (prep-vendor reports)"],"ai_policy":"The application form asks candidates to confirm Anthropic's AI-use guidance and to write the 'why Anthropic' answer without AI mediation (employer page).","take_home":true,"duration":"3-6 weeks","note":"Customer-scoping variant of the application track. Two prep vendors differ on the take-home. COI: developer's own process."}
{"type":"loop","grade":"C","src":["S30"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","employer":"OpenAI","track":"application","stages":["recruiter screen","technical assessments","final loop: system design, customer role-play, pair programming, behavioural"],"formats":["3 rounds (prep-vendor report)"],"ai_policy":null,"take_home":null,"duration":"3-5 weeks","note":"Customer scenario included."}
{"type":"loop","grade":"C","src":["S30"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","employer":"Databricks","track":"application","stages":["recruiter screen","technical discovery or architecture","customer scenario","architecture demo or panel presentation","behavioural and hiring manager"],"formats":["panel presentation"],"ai_policy":null,"take_home":null,"duration":null,"note":"A take-home is reported by some candidates. The AI-FDE loop cited in the KB was not verified."}
{"type":"loop","grade":"C","src":["S54"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","employer":"OpenAI (frontend)","track":"application","stages":["recruiter","phone screen","take-home","onsite: live build of a streaming chat UI","frontend system design that increasingly covers the API behind the interface","behavioural"],"formats":["live coding of a ChatGPT-style interface around a supplied streaming function"],"ai_policy":null,"take_home":true,"duration":null,"note":"Frontend-heavy variant; does not match the KB's RAG and agent-loop track."}
{"type":"loop","grade":"C","src":["S54"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","employer":"Vercel","track":"application","stages":["take-home (3-8 hours)","React deep-dive","frontend system design","product and craft","culture"],"formats":["take-home plus 3-4 onsite rounds"],"ai_policy":null,"take_home":true,"duration":null,"note":"Prep-vendor report."}
{"type":"loop","grade":"C","src":["S54"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","employer":"Cursor","track":"application","stages":["recruiter","phone","take-home on the real codebase","onsite: coding, system design, ML or AI deep-dive, product and craft, behavioural"],"formats":["take-home on a real codebase"],"ai_policy":null,"take_home":true,"duration":null,"note":"Prep-vendor report."}
{"type":"loop","grade":"C","src":["S54"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","employer":"AI-wrapper Series A companies","track":"application","stages":["founder or recruiter screen","product-flavoured coding in Python or TypeScript","take-home or paired build of a small AI feature"],"formats":["build a working AI feature"],"ai_policy":null,"take_home":true,"duration":null,"note":"Prep-vendor synthesis; low reliability."}
```

### practice records

```jsonl
{"type":"practice","grade":"P","src":["S1","S18"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","area":"resume","tactic":"Lead the profile with named customer deployments, technical wins and the scale of evaluations influenced, and state the customer-facing role explicitly","claim":"Postings gate on customer-facing technical experience (22 of 23) and on a record of selling technical products","evidence":"Sample shares; the Anthropic Startups posting; the Anthropic manager posting asks for experience with $10M+ evaluations","verdict":"use","risk":"Unverifiable revenue claims invite scrutiny; state scope and ranges."}
{"type":"practice","grade":"P","src":["S18","S8"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","area":"resume","tactic":"Headline the profile with a list of certifications","claim":"Certifications open doors in SA hiring","evidence":"Named in 1 of 23 sampled postings and in 1.7% of US AI-architecture postings (AWS Solutions Architect certification)","verdict":"avoid","risk":"Signals a services-channel profile at labs and vendors.","note":"Acceptable as a supporting line for Microsoft, AWS or Google partner roles."}
{"type":"practice","grade":"P","src":["S1","S13","S30"],"as_of":"2026-11-13","ttl":"V3","role":"ai-solutions-architect","area":"proof","tactic":"Build an eval-backed reference architecture with a cost and latency note, plus a 10-minute customer-scenario walkthrough","claim":"Postings ask for production LLM apps with evals; loops include a customer-scenario round","evidence":"Anthropic Startups posting; PwC cost and latency constraints; prep-vendor loop reports (C); IaC named in 0 of 23","verdict":"use-with-care","risk":"Loop evidence comes from prep vendors."}
{"type":"practice","grade":"P","src":["S35","S39","S40"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","area":"proof","tactic":"Run a pilot with named colleagues and report active use and time saved, with a runbook and a risk register","claim":"Employers ask for measured adoption and before-and-after evidence","evidence":"LocalStack asks for a before-and-after workflow; Sofi for adoption metrics and runbooks; Mentor Collective for pilots","verdict":"use","risk":"Small pilots give noisy numbers; state n and method."}
{"type":"practice","grade":"P","src":["S35","S37","S38","S40","S46"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","area":"proof","tactic":"Ship an MCP server or internal agent that colleagues use, and show the repository plus a usage log","claim":"Builder and platform variants ask for MCP servers, agents and integrations","evidence":"Mentor Collective, Coder, Sofi and Revalize postings; Preset's blog (COI)","verdict":"use","risk":"Do not publish confidential integrations; use a sanitised repo."}
{"type":"practice","grade":"P","src":["S36","S39","S41"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","area":"proof","tactic":"Present a training curriculum and champion-network metrics for the adoption variant","claim":"Adoption-lead postings ask for training, champions and playbooks","evidence":"Scotiabank, Liquidity Services and Jorie AI postings","verdict":"use-with-care","risk":"The variant may be transitional and pays less (about $120-140K in the one priced posting)."}
{"type":"practice","grade":"P","src":["S35","S37"],"as_of":"2026-11-13","ttl":"V3","role":"ai-enablement-engineer","area":"resume","tactic":"For the platform variant, show SSO, OAuth or Entra ID scoping work and an access-review or audit record","claim":"Platform postings ask for identity design in regulated settings","evidence":"Sofi (SSO, SAML, OAuth, OIDC, SCIM, audit); Revalize (Entra ID, permission models)","verdict":"use-with-care","risk":"Only 3 of 15 postings name identity skills."}
{"type":"practice","grade":"P","src":["S49","S50","S54"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","area":"proof","tactic":"Deploy a streaming chat or agent UI with cancel, retry and error states and an accessibility check, and link it","claim":"Postings and interview reports centre on AI-facing interfaces","evidence":"Taktile and Pebl posting text; Within asks for accessibility and shipped work; interview reports (C) describe live streaming-UI builds","verdict":"use","risk":"Evals were named in 0 of 16 postings; add them only as a differentiator."}
{"type":"practice","grade":"P","src":["S49","S50","S51"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","area":"resume","tactic":"Headline as Product Engineer or Full-stack AI engineer with React, TypeScript and LLM-integration keywords, and link a portfolio or GitHub","claim":"Most matching postings carry the Product Engineer or full-stack framing","evidence":"Alias counts: Product Engineer 6 of 16; React 93.8%, TypeScript 81.3%, LLM APIs 68.8%; Within asks for a portfolio or GitHub","verdict":"use","risk":"Generic full-stack framing can dilute AI-specific signals; keep the AI project first."}
{"type":"practice","grade":"P","src":["S49","S55"],"as_of":"2026-11-13","ttl":"V3","role":"ai-product-engineer","area":"resume","tactic":"Headline as 'AI Frontend Engineer' only","claim":"The AI-frontend title is the main way hiring teams search","evidence":"The exact title appears in 1 to 2 of 16 postings; Within uses it for a design-engineer role; SCAYLE uses 'AI' for a marketing-site role","verdict":"use-with-care","risk":"Narrows matches and invites mismatched roles."}
```

### absence records

```jsonl
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Exact-title posting count for AI Solutions Architect","searched":"Skillenai, JobsPipe, Fast AI Jobs, Axial Search, choppingblock.ai","note":"Only proxies found (Axial AI architecture class; generic SA counts)."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Title-level posting count for AI Product Engineer or AI Frontend Engineer","searched":"Skillenai, JobsPipe, Fast AI Jobs, TealHQ, ZipRecruiter, Wellfound listings","note":"Only adjacent counts (AI Engineer, full-stack, Product Engineer)."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Levels.fyi or equivalent pay for AI Enablement Engineer and AI Product Engineer","searched":"Levels.fyi via web search, ZipRecruiter, Glassdoor","note":"Titles not tracked."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Senior India pay for AI Enablement Engineer and AI Product Engineer","searched":"AmbitionBox, Glassdoor India, cutshort, Wellfound listings","note":"Only junior and early-career bands found."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Role-specific interview loop and AI-tool policy for AI Enablement Engineer","searched":"Dataford, CleverPrep, DesignGurus, techinterview.org, employer pages","note":"None found."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"SA interview loops at hyperscalers and consultancies; AI-tool policies at OpenAI and Databricks","searched":"Prep-vendor sites and employer careers pages","note":"Only Anthropic's application-form policy found."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"LCA filings for the exact titles AI Enablement Engineer and AI Product Engineer; the Department of Labor disclosure file itself","searched":"Ellis, h1bgrader and MyVisaJobs aggregators","note":"Aggregators only; the Department of Labor file was not queried."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Voice-agent and on-device or edge specialisations in the AI Product Engineer sample","searched":"Ashby, Greenhouse, YC and Hacker News extracts","note":"0 of 16 postings."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Published analyses of prior roles of people hired into the three roles","searched":"Skillenai role pages, Axial Search","note":"None found."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Hiring-manager statements on proof of work for the three roles","searched":"Employer blogs and posting text","note":"Only posting text and one employer blog (Preset, COI)."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Non-English postings beyond French (EY, Anthropic Paris)","searched":"Not searched in German, Japanese or Hindi","note":"Coverage limitation."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Posting dates for 13 of 23 SA and 7 of 16 Product Engineer postings","searched":"Page extracts of employer boards","note":"No date field in the extracts."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Workday, Taleo and Indian ATS hosted SA postings; Amazon, Greenhouse and Ashby page fetches","searched":"Fetch attempts","note":"Amazon (client error), Greenhouse (bot block) and Ashby (client error) failed."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Anthropic Product Engineer pay and Sofi pay band","searched":"Posting extracts","note":"Not shown in the extracts."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Details of Databricks India SSA postings and the NTT Senior AI SA (Bangalore) posting","searched":"Aggregator similar-jobs lists","note":"Listed only; no requirements extracted."}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Aliases 'Agent Architect (exact)', 'Agent Interface Architect', 'Client-Side AI Specialist', 'On-Device AI Engineer' and 'AI Product Ops' in the window","searched":"ATS board extracts and aggregator searches","note":"Not found."}
```
