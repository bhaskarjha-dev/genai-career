---
id: T1-02
title: "Epistemic Governance & Evidence-Grounding Protocol (EGP-1.0) for an AI-Careers Repository"
date: 2026-10-21
status: complete
topic: "Evidence hierarchy, citation mechanics, temporal recency and contradiction adjudication"
tags: [epistemics, evidence-grading, provenance, recency-ttl, citation, link-rot, contradiction-resolution, ci-linting, anti-hype, ai-careers]
informs_decisions:
  - "provisional:evidence-grade-rubric"
  - "provisional:recency-ttl-classes"
  - "provisional:citation-and-archive-standard"
  - "provisional:contradiction-adjudication"
  - "provisional:ci-lint-and-audit-gates"
confidence: 0.78
confidence_note: "High for the verified findings that motivate each rule (read at snippet depth or better). Medium for the specific TTL numbers and badge conventions, which are judgement calls not yet calibrated against this repository's own change logs."
temporal_anchor: "2026-10"
last_verified: 2026-10-21
session_type: "independent; run parallel to Layer 0; no upstream findings were injected or used"
protocol_version: EGP-1.0
author_disclosure: "Written by Claude (Anthropic). Several evidence items concern Anthropic (its API documentation, CEO statements, Economic Index data); they are flagged COI:anthropic in the ledger and treated as interested-party sources."
---

# T1-02 — Epistemic Governance & Evidence-Grounding Protocol

> **How to read this file.** `S##` is a row in the Sources & Evidence Ledger (§9). Depth codes: **F** = full text opened · **S** = snippet, abstract or summary opened · **M** = not opened (recalled, or known only second-hand). Grades **A–E** follow the rubric proposed here (§10.3). `◌` marks a statement recalled from memory and not verified this session; it is capped at Grade D until verified. "Not found after searching…" statements are findings, not omissions. Dates are ISO-8601 and the temporal anchor is 2026-10-21.

## 1. Prior

Beliefs held *before* searching, written as checkable propositions. Section 8 (Delta) reports what the evidence did to each.

| # | Proposition (from memory) | Credence | How it was tested |
|---|---|---|---|
| P1 | A source-type-only A–E ladder is not enough. Mature frameworks (GRADE, the Admiralty system, ICD 203) rate the *claim as phrased*, keep source reliability apart from information credibility, and have explicit downgrade rules. | 0.85 | Read GRADE and ICD 203 text; check the Admiralty structure |
| P2 | Frontier-AI product facts and immigration *status* go stale much faster than the brief's 3/12/36-month examples imply, because shelf-life depends on the volatility of the process producing the fact, not on its topic. | 0.70 | Vendor deprecation log, price history, H-1B event timeline, release cadences |
| P3 | About 25–40% of web pages disappear within a decade; archiving at citation time (Wayback Machine, Perma.cc) is the standard mitigation. | 0.80 (range) | Pew 2024 crawl study; archive-tool documentation |
| P4 | Some widely repeated AI-career statistics trace to one non-peer-reviewed report or to an executive *forecast*, and their scope drifts as they are repeated ("95% of AI pilots fail"; "AI will write 90% of code"). | 0.80 | Trace both claims to origin; compare wording across sources |
| P5 | Self-reported salary platforms and government LCA filings disagree mainly because they measure different constructs, so conflicts should be normalised before they are adjudicated. | 0.85 | DOL record layouts; Levels.fyi definitions |

## 2. Research Question

What evidence hierarchy, citation mechanics, temporal-recency rules and contradiction-resolution workflow must a repository about AI careers enforce so that every factual claim (salary figures, hiring volumes, technical specifications, policy status) is traceable to a primary source, fresh within a declared shelf-life, and resistant to hype in *either* direction (boom or doom)?

Sub-questions: (a) How should evidence be graded, and what is the unit being graded? (b) What shelf-life should each class of claim receive, and what should end it early? (c) How should citations be formatted and preserved against link rot and archive failure? (d) What is the step-by-step procedure when reputable sources conflict? (e) What can a CI pipeline enforce mechanically, and what must stay with humans?

## 3. Key Findings

Each finding carries a grade under the rubric of §10.3, the ledger rows that support it, and the depth at which they were read. Where a finding has sub-claims of different strength, the grade shown is the weakest link and the sub-grades are given.

**KF1 · Grade the claim as phrased, not the source alone.** GRADE rates certainty of evidence per outcome in four levels; randomised trials start high and observational studies start low; ratings move down for five named concerns (risk of bias, inconsistency, indirectness, imprecision, publication bias) and up for three, and the method is presented as a transparent judgement process (S01, S02). NHMRC guidance has two reviewers rate independently (S03). The Admiralty system rates source reliability (A–F) and information credibility (1–6) on separate axes (S05–S08). ICD 203 requires analysts to separate underlying information from assumptions and judgements and to disclose uncertainty drivers, including the currency of the information (S04). The brief's A–E ladder is a sound *starting tier* but needs claim-scoping, explicit downgrade flags and hard caps. **Grade A** for GRADE and ICD 203 (primary text, S); Admiralty structure is **B** (secondary and tertiary sources; the field manual S09 was not opened).

**KF2 · Link rot is fast, and the archive layer has its own failure modes.** Pew's crawl-based study found 38% of pages that existed in 2013 inaccessible by October 2023, about a quarter of all pages across the 2013–2023 vintages gone, and roughly one in five pages from 2021 gone within two years; 54% of sampled Wikipedia articles contained at least one dead reference link (S11). The planning number for a repository with 6–12-month claims is therefore the two-year figure (~20%), not the decade figure. Archive infrastructure fails too: the Internet Archive's October 2024 breach and DDoS took the Wayback Machine offline until a read-only restoration around 2024-10-14 (S20, S21); English Wikipedia deprecated archive.today in February 2026 after evidence that its operator altered archived content (S22, S23); Perma.cc's free-tier rules are described inconsistently across sources (S13–S16); a Fifth Circuit panel declined judicial notice of Wayback captures and required authentication (S24–S26). **Grade B** (Pew is a transparent-method study but not peer-reviewed; incident reports are secondary).

**KF3 · Decay is real but heterogeneous: separate a fact's *instance* from its *trend*.** Clinical systematic reviews show a median 5.5 years before a signal that an update is needed, with 23% signalled within two years (S12). AI-platform facts move faster. One vendor's official deprecation page lists seven model-deprecation notices between 2025-06-30 and 2026-06-05 (mean gap ≈ 57 days; a floor, since later notices exist) (S27). Secondary sources report a 67% Opus-tier list-price cut at the 2025-11 model transition ($15/$75 → $5/$25 per million tokens) (S30, S31). Epoch AI estimates the price of reaching a fixed capability falls 9–900× per year (median 50×) depending on threshold (S32, S33), while other analyses report different rates (S34, S35). The price *of model M* is stable until M is repriced or retired; the price *of capability L* decays continuously, and the two need different TTLs. **Grade B** (sub-grades: A for S12 and S27; C for the price-cut figure, primary not read; B for Epoch).

**KF4 · Policy *status* can change every few weeks while policy *text* sits still.** Proclamation 10973 (signed 2025-09-19; 90 FR 46027) imposed the $100,000 payment on certain new H-1B petitions with a 12-month term; Proclamation 11069 (2026-09-18; Federal Register public-inspection document 2026-19554) extended it (S36–S38). In the 123 days from 2026-06-08 to 2026-10-09, secondary legal sources record eight dated events: vacatur of the implementing policies (D. Mass., 06-08), notice of appeal (06-11), administrative stay (06-12), First Circuit stay denial (07-24), the extension proclamation (09-18), its Federal Register publication (09-23), a second district-court order (N.D. Cal., 09-30) and a Ninth Circuit appeal (10-09) (S39–S44). One secondary page, dated 2026-10-07 by its URL, places a ruling on "September 30, 2027", an impossible date for that page (S45). The courts acted on the agencies' implementing policies, not on the proclamation's existence, so "the fee was struck down" is wrong while "as of 2026-10-21, collection is blocked" is supportable, and both statements expire. **Grade B** (A for proclamation text; B for litigation status, because dockets were not retrieved).

**KF5 · Grade-A official statistics have gaps, vintages and definitional drift.** BLS collected no October 2025 household-survey data during the 43-day funding lapse, so no October 2025 unemployment rate exists, and BLS said it could not precisely quantify the effect on the November estimates (S46). DOL's LCA disclosure files are cumulative quarterly releases (the Q3 FY2026 file appeared 2026-08-14), the wage-field wording differs between the FY2019 and FY2020 record layouts, and DOL warns of data-entry anomalies (S47–S50). A certified LCA is an application for a position; the data do not show whether or how it was used (S49, restated by the secondary S51). A primary source is necessary for credibility, not sufficient for completeness. **Grade A** (BLS release and DOL layouts read at snippet depth; the "not a hire" nuance is B).

**KF6 · Salary sources measure different constructs.** LCA fields record a from/to wage rate with a pay-unit field for a certified position (S47–S49). Levels.fyi defines total compensation as base plus annualised stock plus bonus, describes its data as self-reported and reviewed, and promotes itself with a verification superlative that cannot be checked from outside (S52). A "contradiction" between them is expected and is definitional until proven otherwise (P5 confirmed). **Grade B** (A for DOL definitions; B for Levels.fyi's definitions as self-description; E for its verification superlative).

**KF7 · One paper can carry three headline numbers; pin versions.** The Stanford "Canaries in the Coal Mine" working paper headlined a 13% relative employment decline for young workers in AI-exposed occupations in its August 2025 version, 16% in the November 2025 version, and in the August 2026 version (data through June 2026) leads with a *descriptive* 19% shortfall against less-exposed peers, restating the July-2025 vintage as 15% on the same measure; the 2026 text says it does not estimate a causal AI effect and reports attenuation when education is controlled (S53–S55). Secondary articles mix the versions. **Grade A** for the drift itself (primary read in full, F); the labour-market inference is **B**.

**KF8 · Productivity "contradictions" are mostly differences of scope.** Peng et al. report a 55.8% faster completion on one JavaScript HTTP-server task for 95 recruited developers (95% CI roughly 21–89%) using early Copilot, with GitHub/Microsoft-affiliated authors (S58). METR's July 2025 trial of 16 experienced open-source developers on their own repositories (246 tasks) found work 19% slower with early-2025 tools, although the developers had forecast a speed-up (S59, S61). METR's own 2026-02-24 update says its follow-up data are an unreliable signal because developers declined to work without AI and withheld tasks, calls them very weak evidence, and says late-2025 AI likely sped developers up (S60). The studies differ in task, population, tool generation and measurement, so no single "AI makes developers X% faster" figure is supported. **Grade B** (preprints plus a primary METR post; vendor COI noted).

**KF9 · "95% of AI pilots fail" is a case study in provenance decay.** The statistic comes from a July 2025 report by MIT's NANDA initiative that was not peer-reviewed. Fortune described 150 interviews, a 350-person survey and 300 deployments; three other sources, including a long-form podcast analysis, give the report's stated method as 52 structured interviews, 153 survey responses and 300+ public initiatives (S62–S65). The headline is tied to a narrow "measurable P&L impact within six months" threshold and is reworded in circulation as a share of pilots, companies or projects, or as pilots that "stall". The primary PDF could not be fetched (S66), so the sample-size conflict is unresolved at primary depth. **Grade C.**

**KF10 · "AI will write 90% of code" is three different claims.** (1) A hedged forecast by Anthropic's CEO at CFR on 2025-03-10 (S67, via S68). (2) A named analyst's October 2025 estimate that the company-wide share of merged code was far below 90% (about half), based partly on private discussions (S68). (3) A first-party figure published 2026-06-04: more than 80% of code merged into Anthropic's production codebase in May 2026 was authored by Claude, with the company calling its related 8× code-per-engineer figure likely an overstatement of productivity (S69–S71). Claim (3) is an interested-party measurement about one company, not an industry statistic. Searches found no independent industry-wide measurement of AI-authored code share (absence is not proof). **Grade B** for the chain (primary documents S67 and S69 not opened); COI:anthropic.

**KF11 · LLM-fabricated citations are measured, and LLM verifiers are unreliable.** GPTZero reported 100 hallucinated citations in 51–53 papers among 4,841 scanned NeurIPS 2025 papers (its own page uses both counts) (S72, S74); a third-party failure-mode study builds on that scan (S73); the July 2026 HALLMARK preprint finds LLM-based citation verifiers fail in specific ways, including over-flagging papers newer than the verifier's training data (S75). Existence and support checks must therefore be deterministic (resolver plus anchor-string match), not LLM judgement. **Grade B** (vendor-reported with disclosed method, COI:vendor; preprint).

**KF12 · Two caps are grounded in evidence and in law.** (a) *Single-study cap*: in the 2015 reproducibility project, 97% of original psychology findings were significant versus 36% of replications (S79). (b) *Vendor-claim cap*: the FTC's Operation AI Comply and its Workado order treat unsupported AI performance claims ("98% accurate") as deceptive and require competent and reliable evidence (S76–S78). Crossref exposes Retraction Watch data in its main API, making retraction checks scriptable (S80, S81). **Grade B** (law-firm alerts and an association summary; the FTC release and the Science paper were not opened).

## 4. Recommendation

Adopt **EGP-1.0**, a *claim-scoped evidence-grading and freshness protocol* enforced by a CI gate, with these non-negotiables (full text in §10):

1. **The grade attaches to the claim as written.** Attribution claims ("S reports X") and assertion claims ("X is so") are graded separately; writers must use attribution form whenever the assertion grade is below B (§10.3).
2. **Base tier by source type (A–E, per the brief), then flags and caps; weakest link governs;** independent corroboration can add at most one notch and never rescues a flagged or capped claim.
3. **Cite-or-Flag.** Every empirical sentence ends with `[grade][^cNNNN]` bound to the claim ledger, or with `[UNVERIFIED]` plus a task that expires in 30 days. Nothing graded D, E or unverified may appear in titles, summaries, recommendations or tables of figures (§10.4).
4. **Three dates and seven volatility classes.** `as_of`, `published`, `last_verified`; TTLs of 14/31/90/180/365/1095 days and none for history, shortened by event triggers and instrument sunsets (§10.6).
5. **Write volatile facts once.** Status-type claims live in a central facts registry and are transcluded, not retyped.
6. **Archive on cite.** Two institutional archives for A/B sources, a content hash, a ≤15-word anchor; archive.today-family domains are banned (§10.7).
7. **CAP-1 for conflicts.** Normalise definitions first, then trace provenance, grade, classify (R0–R5), and publish range-and-reasons. Never average, never silently pick (§10.8).
8. **Claim archaeology and a Hype Register for viral statistics,** with a *symmetric burden of proof* for boom and doom claims (§10.9).
9. **Mechanical CI** on every pull request, a weekly network sweep, and a quarterly sampled audit with a stated acceptance bound (§10.12–10.13).
10. **Pilot before enforcing:** two reviewers grade 50 claims independently; measure agreement; revise the rubric if agreement is poor (§10.13).

Suggested sequence: week 1 adopt schemas and run the linter in warn mode; weeks 1–2 pilot inter-rater agreement; weeks 2–4 backfill archives for A/B sources; week 5 switch EG001–EG004 and EG006–EG007 to blocking.

## 5. Alternatives Considered

| # | Alternative | Why not adopted as-is | What was borrowed |
|---|---|---|---|
| A1 | Adopt GRADE wholesale | Built for clinical guideline questions with systematic evidence profiles; too heavy per claim | Rate-down domains became the −M/−I/−V/−S/−D/−R/−P flags; "do not rate up after rating down" |
| A2 | Admiralty two-axis codes (A1…F6) | 36 combinations; illegible to casual readers | Independence of source and information assessment |
| A3 | Wikipedia-style reliable/unreliable binary plus a perennial-sources list | Too coarse; says nothing about fit between claim and source | `As of` stamps, ban on relative-time words, dated "citation needed" tags, a domain registry |
| A4 | Numeric credence per claim | False precision; no calibration data exists for this repository | ICD 203 verbal probability bands, used only for forecasts |
| A5 | One global TTL (for example six months) | Wrong for status claims (days) and for foundations (years); either floods maintainers or lets facts rot | Per-class TTLs with a trigger override |
| A6 | Full evidence vault (store every source copy) | Storage, licensing and drift of the copy itself | Hash, text extract and two archives instead |
| A7 | LLM as the fact-checking gate | Hallucinated citations and verifier failure modes (KF11) | LLMs allowed as lead generators only; never the verifier of record |
| A8 | Trust-by-reputation allowlist ("tier-1 blog = B") | Ignores interest and claim type; vendors are reliable about their own specs and unreliable about their own impact | Allowlist kept as the *starting tier*, with claim-type exceptions |

## 6. Detailed Findings

### D1 · Frameworks (KF1)

- **GRADE** (S01, S02): certainty is rated per outcome as high, moderate, low or very low. The BMJ Best Practice summary calls the method subjective but transparent and reproducible, which is the right framing for any rubric adopted here: the goal is auditable judgement, not mechanical truth.
- **Admiralty** (S05–S08): two letters-and-numbers axes, assessed independently. A machine-readable form exists as a MISP taxonomy (S08), which could be reused if the repository ever exchanges ratings with security tooling. One practitioner glossary says the NATO doctrine text is not public (S07), so the repository should cite the taxonomy or the U.S. field manual (S09, **not opened**) rather than attribute wording to NATO.
- **ICD 203** (S04), signed 2015-01-02 with a technical amendment on 2022-08-22: requires distinguishing information from assumptions and judgements, and lists the *currency* of information among uncertainty drivers. Its verbal likelihood bands (01–05% "almost no chance" through 95–99% "almost certain") are the only calibrated vocabulary adopted here, and only for forecasts.
- **Gap.** I did not search for inter-rater-reliability studies of the Admiralty scale; whether such ratings are reproducible in practice is open (see §7, objection O1).

### D2 · Link rot, archive failure modes and tool gotchas (KF2)

| Item | What was found | Consequence for the protocol |
|---|---|---|
| Pew (S11) | 38% of 2013 pages gone by 2023; ~25% across 2013–2023 vintages; ~1 in 5 gone after two years; 23% of news and 21% of government pages carry a broken link | Plan on ~20% loss in two years; weekly link checks |
| Internet Archive outage (S20, S21) | Breach and DDoS in October 2024; Wayback restored read-only about 2024-10-14, with Save Page Now unavailable for a time | Never depend on one archive; allow `archive_pending` status |
| archive.today (S22, S23) | Deprecated on English Wikipedia (~695,000 links) in February 2026 after a DDoS and evidence that archived content was altered | Ban the domain family; hash content at capture so alteration is detectable even in trusted archives |
| Perma.cc (S13–S16) | Links become permanent after 24 hours and are preserved by participating libraries; a 2019 post says individual accounts get 10 free links on registration and paid tiers beyond that; the Wikipedia article states both "10 per month" and that recurring free links stopped in 2019 | Pricing and quotas are **unverified for 2026**; confirm in the dashboard before relying on quota |
| Wayback APIs (S17; S18 and S19 **not opened**) | Availability API can return empty for URLs that do have captures; the CDX server is the reliable lookup; 429 responses carry Retry-After | Use CDX; back off on 429. No official numeric rate limit was found in the pages opened, so none is hard-coded |
| Courts (S24–S26) | Fifth Circuit (No. 20-30568, 2022) held Wayback captures are not a proper subject of judicial notice and need authentication; other courts have taken a more permissive line | Archives support *verifiability*, not legal admissibility; legal claims cite court-issued documents |
| Crossref (S80, S81) | Retraction Watch data merged into the main REST API; rate limits revised 2025-12-01; a Labs-API route was deprecated | Throttle from response headers rather than constants ◌ (header names recalled) |
| Semantic Scholar (S82–S84) | Overview page says unauthenticated users share 1,000 requests/second; tutorial says 5,000 requests per 5 minutes; keyed introductory rate 1 request/second; a third-party measurement (2026-08) found per-endpoint-class throttling | Official pages disagree with each other. Handle 429s; never hard-code |
| Google ClaimReview (S85–S87) | Search-result rich-result support phased out (announced 2025-06-12; Search Console reporting removed from 2025-09-09) | Do not depend on fact-check snippets as a discovery channel. Whether the Fact Check Explorer and API continue was **not verified** |
| lychee (S92–S94) | `--cache`, `--max-cache-age`, `--accept`, `--exclude`; in action v2.x an explicit `--accept 201` rejects plain 200 | Always list the full accepted range |
| GitHub rendering (S90, S91) | Five alert types only (NOTE, TIP, IMPORTANT, WARNING, CAUTION); extended title/fold syntaxes are not GitHub-compatible | Callouts use basic syntax only |

### D3 · Decay evidence and the brief's starting assumption (KF3)

- **Deprecation log (S27).** Notices dated 2025-06-30, 2025-08-13, 2025-10-28, 2025-12-19, 2026-02-19, 2026-04-14 and 2026-06-05: seven in 340 days, gaps of 44, 76, 52, 62, 54 and 52 days. Later notices almost certainly exist (a secondary guide, S29, lists retirement dates for newer models) but the full page was not read.
- **Policy-vintage conflict.** An older vintage of the same documentation (S28) states a notice period of at least six months for publicly released models; a secondary guide dated 2026-08-06 (S29) says at least 60 days. Either the policy changed or one source is wrong; the wording on the 2026-10-21 vintage of the page was **not read** in full. This is the protocol's pattern in miniature: cite the vintage, archive it, and re-verify on trigger.
- **Price.** The Opus-tier cut was 66.7% on both input and output ($15 → $5 and $75 → $25 per million tokens) (S30, S31, secondary only). A cloud-cost vendor notes that a tokeniser change can alter the effective bill at an unchanged list price (S30), and a third-party blog repeats a vendor claim of 76% fewer output tokens (S31), which is Grade E until independently measured. So "price" must name its measurand: per token, per task, or per capability.
- **Trend estimates differ because the baskets differ.** Epoch's 9–900×/year range (median 50×) (S32, S33) versus roughly 13×/year to reach a given performance level in a later Epoch analysis as summarised by a secondary outlet (S34, undated in the snippet) versus 5–10×/year for frontier models in a paper summary (S35). Different thresholds and model sets: a definitional split (R2), not a contradiction.
- **Clinical analogue (S12).** Median 5.5 years (CI 4.6–7.6); signals within one year in 15%, within two years in 23%, at publication in 7%; faster for fast-moving topics. If even clinical reviews need updates within two years about a quarter of the time, 36 months is a *ceiling for foundations only*.
- **Test of the brief's assumption** ("uncited technical claims decay into misinformation within 6–12 months"). Supported for status, price, specification and lineup claims; not supported as a blanket rule (foundational and historical claims persist). Note the evidence concerns *any* claim lacking an as-of date and trigger, cited or not.

### D4 · H-1B fee timeline as a volatility specimen (KF4)

| Date | Event | Sources | Grade |
|---|---|---|---|
| 2025-09-19 | Proclamation 10973 signed; effective 2025-09-21; 12-month term | S36, S37 | A |
| 2025-09-24 | Published at 90 FR 46027 (FR Doc. 2025-18601) | S36 | A |
| 2026-06-08 | D. Mass. vacates the implementing policies | S43 (and S41–S44) | B |
| 2026-06-11 | Notice of appeal | S41–S44 | B |
| 2026-06-12 | Administrative stay; collection briefly restored | S41–S44 | B |
| 2026-07-24 | First Circuit denies a stay pending appeal | S41, S42 | B |
| 2026-09-18 | Proclamation 11069 extends the restriction (to 2027-09-21 per secondary summaries); FR public-inspection doc 2026-19554; published 2026-09-23 | S38, S44 | A (text) / B |
| 2026-09-30 | N.D. Cal. order against the implementing memos (No. 4:25-cv-08454) | S39 | B |
| 2026-10-09 | Government appeals to the Ninth Circuit | S40 | B |

Event-level attribution to a specific alert was not recorded for 06-11, 06-12 and 07-24; re-verify against the dockets. Proclamation 11069 also recites the 2025-12-29 DHS weighted-selection final rule; the page citation in my snippet was garbled and is deliberately not reproduced. Law-firm alerts mention an earlier, contrary D.D.C. ruling; its date and docket were **not verified**. A university immigration-services page (S45) misdescribes the First Circuit's action as reinstating the vacatur and carries the impossible 2027 date. **Not found:** the primary court orders (PACER or CourtListener links did not appear in any result).

### D5 · What "primary" does not guarantee (KF5)

- BLS's 2025-12-16 release states that October 2025 household data were not collected and that composite-estimation adjustments were made; BLS could not quantify the effect on November (S46). A linter cannot see this kind of caveat, so the claim record needs a `caveat` field that a human fills from the release notes.
- LCA files: Q1 FY2026 appeared 2026-02-13 and Q3 FY2026 on 2026-08-14, each cumulative within the fiscal year (S49, S50). The wage-rate field description changes between record layouts (S47: "employer's proposed wage rate"; S48: "wage paid"), and the pay-unit field mixes hour, week, bi-week, month and year, so annualising is a transformation that must be recorded.
- **Not found:** DOL's own wording that a certified LCA does not establish a hire; only a secondary quotation (S51, a vendor blog, Grade D) was retrieved.

### D6 · Salary constructs (KF6)

| Source | Construct | Known limits | Use in the repository |
|---|---|---|---|
| DOL LCA disclosure (S47–S49) | Wage-rate range on certified applications, with pay unit | Position-level, not hires; base wage only; data-entry anomalies; layout wording varies by year | A for "what was filed"; never for "what workers earn" |
| Levels.fyi (S52) | Self-reported total compensation (base + annualised stock + bonus) | Self-selection; per-cell n varies; verification claim not checkable | B for "what the platform reports" **with n and date**; E for its verification superlative |

Presentation follows the range-and-reasons template (§10.8). Recommended, not evidenced: suppress any salary cell with fewer than five submissions.

### D7 · Version drift in one paper (KF7)

| Version | Data through | Headline | Basis | Causal claim? |
|---|---|---|---|---|
| Aug 2025 (S55) | 2025-07 | 13% relative decline, ages 22–25, most vs least exposed | Regression with firm-level controls | Not stated as established |
| Nov 2025 (S54) | 2025-09 | 16% | Regression with firm-level controls | Not stated as established |
| Aug 2026 (S53) | 2026-06 | 19% "kept-pace" shortfall (15% at the July-2025 vintage on the same measure) | Descriptive divergence | Explicitly **not** causal |

S53 reports that estimates attenuate when education is controlled, and that a survey benchmark (ACS) shows a smaller, statistically insignificant gap than ADP for 2022–2024 (as I read the table: −0.022 versus −0.132), with sector-level disagreement. ADP supplied the proprietary data and holds a right to review the paper to prevent disclosure of confidential information (S53). Yale Budget Lab (S56, S57) finds no discernible economy-wide disruption in the occupational mix; these are different outcomes and populations (R2). The paper cites other studies, including one finding attenuation when work-from-home is controlled; I did not open them.

### D8 · Productivity-study scope (KF8)

| Study | Design and n | Task and population | Tool era | Result | Flag |
|---|---|---|---|---|---|
| Peng et al. (S58) | Randomised, 95 recruited developers | One JavaScript HTTP-server task | Early Copilot | 55.8% faster (CI ≈ 21–89%) | COI:vendor |
| METR 2025 (S59, S61) | Within-developer randomised, 16 developers, 246 tasks | Own mature repositories | Early-2025 tools | 19% slower; forecast +24%; self-rated +20% | Later labelled historical by METR (per S61) |
| METR 2026 update (S60) | New experiment from 2025-08 | Developer-chosen tasks | Late-2025 tools | "Unreliable signal"; selection effects (refusals, withheld tasks, lower pay) | Author-declared weak evidence |

Classification under CAP-1: R2 (scope split) between the first two rows; R1 (superseded, as an estimate for tools released after early 2025) for METR's own 2025 result. Secondary snippets also mentioned a 2026 meta-analysis and an enterprise RCT at Google; neither was opened, so neither is used.

### D9 · Anatomy of "95%" (KF9)

| Source | Wording | Stated basis |
|---|---|---|
| Fortune, 2025-08-18 (S63) | Generative-AI pilots "failing"; elsewhere in the article, "95% of companies in the dataset" | 150 interviews, 350 employees surveyed, 300 deployments |
| aiwiki.ai and letsdatascience (S64, S65) | Pilots that stall or show no measurable P&L impact | 52 interviews, 153 survey responses, 300+ initiatives; Jan–Jun 2025; described as preliminary |
| 80,000 Hours analysis, 2026-04-28 (S62) | Report not peer-reviewed; small sample; the 5% is a share of the whole sample rather than of pilots; the authors' initiative has a commercial interest in the remedy it recommends | Host's own reading of the report |

Resolution: R0 (false conflict) *pending* the primary PDF for the sample-size discrepancy, plus R2 for the definitional variants. Action: obtain the PDF (S66, mirror) and record its stated method at F depth. Entered in the Hype Register (§10.9).

### D10 · The "90% of code" chain (KF10)

| Date | Statement | Source | Claim type | Grade as used |
|---|---|---|---|---|
| 2025-03-10 | Within 3–6 months AI could be writing 90% of code; "essentially all" within 12 months is possible | CFR event (S67, **not opened**; quoted in S68) | Forecast | C for attribution (via S68); E as evidence about the future |
| 2025-09/10 | Internal share said to be 70–90%; "absolutely true" for Anthropic and some customers, on many teams, not uniformly | Interview as reported in S68 | Self-report | C |
| 2025-10-22 | Company-wide merged share estimated near half; some teams near 90% | S68 (named analyst; partly private information) | Estimate | C |
| 2026-06-04 | More than 80% of merged production code in May 2026 authored by Claude; 8× code per engineer, which the company itself says likely overstates productivity | Anthropic Institute essay (S69, **not opened**; reported in S70, S71) | First-party measurement | B, COI:anthropic |
| Any date | Industry-wide share of AI-authored code | **Not found** after searching for first-party disclosures, the analyst post and press coverage | none | No claim permitted |

My own classification: the forecast is *unresolved by its own terms* (its metric was undefined when made); the later first-party figure answers a differently defined question for one company. Because the author of this file is built by the company in question, rows S67–S71 should be independently reviewed (§7).

### D11 · Fabricated citations (KF11)

GPTZero scanned 4,841 accepted papers and reports 100 confirmed hallucinated citations (its page gives the paper count as both 51 and 53); it sells detection tools, so its finding is Grade B with a vendor flag (S72, S74). A third-party study of failure modes used the scan (S73). HALLMARK (S75) shows LLM-based verifiers err, notably on references newer than the model's training data. **Not found:** any base rate for AI-careers content specifically. Mechanical checks that avoid LLM judgement are specified in §10.12: DOI resolution through Crossref, title and author match, HTTP status, and anchor-string presence in the archived page.

### D12 · Caps (KF12)

- **Single-study cap.** 97% versus 36% (S79) comes from psychology; it is an analogue for the risk that one significant result does not hold up, not a measured rate for AI research.
- **Vendor-claim cap.** Operation AI Comply began in September 2024; the Workado matter involved a "98% accurate" detector claim and an order requiring competent and reliable evidence, with a final order reported in August 2025 (S76, S77; FTC release S78 **not opened**).
- **Retraction hygiene.** Crossref exposes retraction and correction notices (including Retraction Watch data) on the work record, enabling a scripted check at citation and on a schedule (S80, S81).
- **Not found:** how often AI-career claims are retracted; not searched.

### 6.13 Falsification log

| Attempt | Outcome |
|---|---|
| Find a mature framework that grades *sources only* | None found beyond simple tiering and binary reliability lists; GRADE, Admiralty and ICD 203 all separate or qualify |
| Show a single TTL is adequate | Contradicted for status claims (eight events in 123 days) and for model lineups; partly supported for a given model's list price until repricing |
| Show archives are reliable enough to be a sole control | Contradicted (outage, altered snapshots, quota ambiguity, evidentiary limits) |
| Find an independent, industry-wide AI-authored-code statistic | **Not found** |
| Find validation of LLM-based citation verification | Not found in one search; found failure-mode evidence (S75) |
| Find validation data for inter-rater agreement on evidence ratings in this domain | Not searched; piloted in §10.13 instead |

## 7. Open Questions & Risks

### 7.1 Limits and disclosures of this session

- **Conflict of interest.** The author is Claude, built by Anthropic. Findings KF3 (price and deprecation facts), KF10 (the "90% of code" chain) and parts of KF7 (the Stanford paper uses Anthropic Economic Index exposure measures, as I read it) concern Anthropic. Those rows carry `COI:anthropic`; an independent human reviewer should re-verify S27–S31 and S67–S71 before the repository relies on them.
- **No upstream findings.** The session ran independently; no Layer 0 output was available, and none was assumed.
- **Decision IDs are provisional.** The repository's decision registry was not provided, so `informs_decisions` uses placeholder slugs.
- **Depth limits.** Rows marked **M** in the ledger were located but not opened; claims resting on them are capped at Grade D until opened. These include the NANDA report PDF (S66), the CFR event page (S67), Anthropic's June 2026 essay (S69), the FTC release (S78), the field manual (S09) and the Wayback API documents (S18, S19). The tool constraints of this session allowed fetching only URLs that had appeared in earlier results, and those fetches were refused.
- **No archive captures exist yet.** This session could not call archive services, so no ledger row has a Wayback or Perma.cc link. By the protocol's own rule (EG004) this file is non-conformant until a backfill job runs. That is a deliberate, disclosed gap and the first task in §4.
- **Recalled-only items (◌).** RFC 2119/8174 usage, WCAG success criterion 1.4.1, the Landis–Koch agreement bands, ALFRED, OpenAlex, the IFCN Code of Principles, the eCFR versioner, CourtListener/PACER, GitHub-flavoured footnote support and Crossref response-header names were recalled, not verified (S95). Treat them as Grade D.
- **Quotation and copyright.** All source material is paraphrased; no quotation exceeds a short phrase.

### 7.2 Strongest objections an expert would raise

| # | Objection | Evidence for | Evidence against or mitigation | Residual risk |
|---|---|---|---|---|
| O1 | Letter grades are false precision; two reviewers will not agree | GRADE itself is described as subjective (S02); no agreement data were collected here | Discrete scales with explicit downgrade rules are standard practice; caps and flags reduce discretion; a 50-claim pilot measures agreement before enforcement (§10.13) | Medium until the pilot runs |
| O2 | The TTL numbers are arbitrary | The class boundaries are judgement; no change-log data from this repository exist | Anchored in measured cadences: 7 deprecation notices in 340 days (S27), 8 legal events in 123 days (S39–S44), ~20% link loss in two years (S11); triggers can only shorten TTLs; calibrate after two quarters from the claim-reversal rate | Medium |
| O3 | Peer-reviewed work should be Grade A; demoting it is wrong | Peer review is a real filter | The protocol keeps A for what a study found in its own sample and caps only generalisation; 97% versus 36% replication (S79) is an analogue for the risk; retractions are scriptable (S80, S81) | Low |
| O4 | Anti-hype rules bias the repository toward scepticism and staleness | Caps and weakest-link grading penalise genuinely new, true claims | The symmetric-burden rule applies to boom and doom claims alike; "95% fail" (S62–S65) is itself a negative-hype statistic; attribution form lets new claims appear without being asserted; audit a sample of rejected claims for false rejection | Medium |
| O5 | Archives are not legal-grade and raise copyright questions | Fifth Circuit refused judicial notice (S24–S26); archive.today alterations (S22) | Archives serve verifiability only; legal claims cite court-issued documents; hash plus extract detect alteration; copyright review of the archiving policy is an open task | Needs legal review |
| O6 | CI cannot check semantic support; anchor strings can be gamed | LLM verifiers fail (S75); an anchor proves only that a string exists | Anchor plus numeric match catches fabricated or misattributed figures; the quarterly human audit is the real control | Medium-high |
| O7 | Marking vendors' statements about their own products as interested-party is over-cautious | First-party documentation is the authority on API behaviour (S27) | The protocol keeps A for first-party specifications and caps only impact and performance claims; yet even first-party pages show vintage conflict (S27 versus S28) | Low |
| O8 | The author is conflicted on the Anthropic-related findings | Author built by Anthropic; KF10 concerns Anthropic | Disclosed; primary documents left unopened and graded accordingly; independent review requested (§7.1) | Needs human review |
| O9 | Law-firm alerts are advocacy; litigation status needs dockets | No docket or order was retrieved; a date error was found in one secondary page (S45) | Multiple independent alerts agree on the event sequence; graded B; docket retrieval is a named follow-up | Medium |
| O10 | The maintenance burden will sink adoption | An illustrative 1,000-claim repository needs about 1,936 re-verifications per year (≈37 per week) under the §10.13 mix | A central facts registry removes duplicate claims; V6 costs nothing; automation covers links, hashes and retractions; apply the full protocol to decision-critical claims first | Medium; measure actual workload |

### 7.3 Open questions

1. Where does the repository's decision registry live, and what are its IDs?
2. What claim volume and type mix should the workload model assume? (Needed to calibrate TTLs.)
3. Does the repository's licence policy permit storing text extracts and hashes of third-party pages?
4. Which Perma.cc account and tier will be used, and what are the 2026 quotas? (Unverified.)
5. Should forecasts have a standing Prediction Register with scheduled resolution reviews? (Recommended: yes.)
6. What is the policy for paywalled sources (analyst reports, some salary data)? (Proposed: a source the reviewer cannot open is depth M, so the MEM ceiling of D applies unless a public page states the same figure.)
7. Should ledger entries adopt the MISP Admiralty tags for interoperability?

## 8. Delta

| Prior | Before | What the evidence showed | Direction | After |
|---|---|---|---|---|
| P1 Claim-scoped grading with separated axes | 0.85 | Confirmed by GRADE, Admiralty and ICD 203 (S01–S08). Refined: GRADE's "no rating up after rating down" became the fatal-cap logic; ICD 203 names *currency* as an uncertainty driver. **New:** the attribution-versus-assertion split came from the cases (KF7, KF9, KF10), not from the frameworks | Confirmed and extended | 0.93 |
| P2 Facts decay faster than 3/12/36 months imply | 0.70 | Directionally right but mis-specified. Three months holds for model lineup and list price (S27). Twelve months would have been unsafe for H-1B *status* (eight events in 123 days) though fine for *text*. Thirty-six months survives only as a ceiling for foundations (S12). **New:** instrument sunsets (a 12-month proclamation), event triggers, and vintage conflict inside first-party documentation (S27 versus S28) | Updated | 0.88 |
| P3 Link rot 25–40% per decade | 0.80 | Range confirmed (38% in ten years, ~25% across vintages) but I under-weighted the short horizon: ~20% within two years (S11). **New:** the archive layer itself fails (S20–S23) and Perma.cc terms are inconsistently reported | Confirmed; emphasis contradicted | 0.90 |
| P4 Viral statistics trace to weak provenance | 0.80 | Confirmed twice with specifics (S62–S71). **Surprises:** press and report disagreed about the sample size; the forecaster later published the metric (an interested-party correction chain); one working paper changed its headline across three versions (S53–S55); METR superseded its own result (S60) | Confirmed; surprises added | 0.92 |
| P5 Salary conflicts are mostly definitional | 0.85 | Confirmed (S47–S49, S52). **New:** DOL's own wage-field wording differs between record-layout years; Levels.fyi's verification superlative cannot be checked externally | Confirmed | 0.88 |
| Unstated: stable free-tier terms for Perma.cc | ~0.7 | Contradicted: sources disagree, including within one article (S13–S16) | Contradicted | 0.3 |
| Unstated: official documentation is internally consistent | ~0.8 | Contradicted: Semantic Scholar's pages disagree on shared limits (S82, S83); two vintages of one vendor's notice policy differ (S27, S28) | Contradicted | 0.4 |
| Unstated: "peer-reviewed = A" is defensible as written | ~0.6 | Refined: valid for what a study found in its sample, not for generalisation (S79) | Updated | 0.85 (with cap) |

## 9. Sources & Evidence Ledger

All rows retrieved 2026-10-21. **Depth:** F full text · S snippet or summary · M not opened. **Grade** is the grade *as used in this file* under §10.3. "A (attr.)" means the primary document supports an attribution claim ("it reports…"), not necessarily the underlying assertion. **Flags:** COI = interested party; ↻ = vintage or URL anomaly; ☐ = archive capture pending (all rows). URLs are canonicalised: default ports, locale and tracking parameters removed.

| ID | Source | Canonical URL | Type | Grade | Date | Depth | Flags |
|---|---|---|---|---|---|---|---|
| S01 | GRADE Handbook | https://gdt.gradepro.org/app/handbook/handbook.html | Method standard | A | n.d. | S | |
| S02 | BMJ Best Practice, "What is GRADE?" | https://bestpractice.bmj.com/info/toolkit/learn-ebm/what-is-grade | Secondary summary | B | n.d. | S | |
| S03 | NHMRC, assessing certainty of evidence | https://www.nhmrc.gov.au/guidelinesforguidelines/develop/assessing-certainty-evidence | Agency guidance | B | n.d. | S | |
| S04 | ICD 203, Analytic Standards | https://www.dni.gov/files/documents/ICD/ICD-203.pdf | Policy directive | A | 2015-01-02 (amended 2022-08-22) | S | |
| S05 | Admiralty code (Wikipedia) | https://en.wikipedia.org/wiki/Admiralty_code | Tertiary | C | n.d. | S | |
| S06 | Small Wars Journal, Admiralty article | https://smallwarsjournal.com/?p=154117 | Practitioner journal | C | n.d. | S | |
| S07 | Altss glossary, source reliability | https://altss.com/glossary/source-reliability | Vendor glossary | C | n.d. | S | |
| S08 | MISP taxonomies, admiralty-scale | https://eugit.opencloud.lu/MISP/misp-taxonomies/src/commit/70c298b53c3f3ef196555708b06995b24b944e79/admiralty-scale | Machine-readable taxonomy | B | n.d. | S | |
| S09 | US Army FM 2-22.3 | https://irp.fas.org/doddir/army/fm2-22-3.pdf | Primary (field manual) | A (unread) | n.d. | M | unread |
| S10 | Caulfield, SIFT (four moves) | https://hapgood.us/2019/06/19/sift-the-four-moves/ | Method (author's blog) | B | 2019-06-19 | S | |
| S11 | Pew Research, "When Online Content Disappears" | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | Study with public method | B | 2024-05-17 | S | |
| S12 | Shojania et al., Ann Intern Med (doi 10.7326/0003-4819-147-4-200708210-00179) | https://pubmed.ncbi.nlm.nih.gov/17638714/ | Peer-reviewed | A | 2007 | S | |
| S13 | Perma.cc FAQ | https://perma.cc/docs/faq | Maintainer docs | A | n.d. | S | ↻ quotas |
| S14 | Perma.cc About | https://perma.cc/about | Maintainer docs | A | n.d. | S | |
| S15 | Perma blog, individual-account tiers | https://archive.blogs.harvard.edu/perma/2019/01/07/introducing-individual-account-subscription-tiers-for-perma | Maintainer post | A (2019 vintage) | 2019-01-07 | S | ↻ pre-2026 |
| S16 | Perma.cc (Wikipedia) | https://en.wikipedia.org/wiki/Perma.cc | Tertiary | C | n.d. | S | ↻ self-inconsistent |
| S17 | DataImpulse, Wayback API guide | https://dataimpulse.com/blog/wayback-machine-api/ | Vendor blog | C | n.d. | S | |
| S18 | Internet Archive, Wayback Availability API | https://archive.org/help/wayback_api.php | Primary docs | A (unread) | n.d. | M | unread |
| S19 | Internet Archive, CDX server docs | https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server | Primary docs | A (unread) | n.d. | M | unread |
| S20 | Help Net Security, Internet Archive breach | https://www.helpnetsecurity.com/2024/10/10/internet-archive-data-breach/ | Trade press | B | 2024-10-10 | S | |
| S21 | Lowyat, Wayback back online | https://lowyat.net/2024/335016/wayback-machine-back-online-oct-2024 | News | C | 2024-10 | S | |
| S22 | Archive.today (Wikipedia) | https://en.wikipedia.org/wiki/Archive.today | Tertiary | C | n.d. | S | |
| S23 | TechCrunch, archive.today deprecation | https://techcrunch.com/?p=3095336 | Trade press | B | 2026-02 | S | |
| S24 | Fifth Circuit, No. 20-30568 (Weinhoffer v. Davie Shoring) | https://www.ca5.uscourts.gov/Opinions/pub/20/20-30568-CV0.pdf | Court opinion | A | 2022 | S | |
| S25 | MoloLamken, NLJ article on the Fifth Circuit ruling | https://www.mololamken.com/assets/htmldocuments/NLJ_5th%20Circuit%20Raises%20Bar%20for%20Website%20Snapshots_April%202022.pdf | Law-firm article | B | 2022-04 | S | |
| S26 | Michigan Bar Journal, Wayback evidence | https://michbar.org/journal/Details/ArticleID=4698 | Bar journal | B | n.d. | S | |
| S27 | Anthropic, model deprecations (2026-10-21 vintage) | https://platform.claude.com/docs/en/about-claude/model-deprecations | Vendor docs (first-party) | A | n.d. (read 2026-10-21) | S | COI:anthropic |
| S28 | Anthropic, model deprecations (older vintage) | https://docs.anthropic.com/en/docs/resources/model-deprecations | Vendor docs (superseded) | A (old vintage) | n.d. | S | COI:anthropic ↻ |
| S29 | Dev.to, "5 Claude API deadlines…" | https://dev.to/mr_manushukla/5-claude-api-deadlines-between-17-august-and-24-november-2026-and-the-400-errors-that-arrive-first-1daj | Community blog | D | 2026-08-06 | S | |
| S30 | CloudZero, Opus pricing explainer | https://www.cloudzero.com/blog/claude-opus-4-7-pricing | Vendor blog | C | n.d. | S | COI:vendor |
| S31 | claudefa.st, Opus 4.5 post | https://claudefa.st/blog/models/claude-opus-4-5 | Blog | D | n.d. | S | vendor claim relayed |
| S32 | Epoch AI, LLM inference price trends | https://epoch.ai/blog/llm-inference-price-trends | Research org | B | 2025-03 | S | |
| S33 | Epoch AI, data insight on price trends | https://epoch.ai/data-insights/llm-inference-price-trends | Research org | B | n.d. | S | |
| S34 | TechSpot, report on newer Epoch analysis | https://www.techspot.com/news/114055-cost-ai-performance-falling-fast-could-reshape-entire.html | News | C | n.d. | S | undated |
| S35 | Longterm Wiki, "Price of Progress" summary | https://www.longtermwiki.com/source/2255e8e1cf26d155 | Wiki summary | C | n.d. | S | |
| S36 | Proclamation 10973, 90 FR 46027 (FR Doc. 2025-18601) | https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18601.pdf | Presidential document | A | 2025-09-24 | S | |
| S37 | Proclamation 10973, DCPD-202500931 | https://www.govinfo.gov/app/details/DCPD-202500931/ | Presidential document | A | 2025-09 | S | |
| S38 | Proclamation 11069, FR public inspection 2026-19554 | https://public-inspection.federalregister.gov/2026-19554.pdf | Presidential document | A | 2026-09-23 | S | |
| S39 | Bloomberg Law, N.D. Cal. order on H-1B fee memos | https://news.bloomberglaw.com/daily-labor-report/judge-halts-memos-on-100-000-h-1b-worker-fee-in-blow-to-trump-17 | News | B | 2026-09 | S | |
| S40 | Bloomberg Government, appeal of the order | https://news.bgov.com/daily-labor-report/trump-appeals-court-loss-that-blocked-100-000-h-1b-fee-policies | News | B | 2026-10 | S | |
| S41 | Clark Hill, First Circuit and the H-1B fee | https://www.clarkhill.com/news-events/news/first-circuit-blocks-reinstatement-of-100k-h-1b-fee/ | Law-firm alert | B | 2026-07 | S | |
| S42 | Littler, appellate court pauses the policy | https://www.littler.com/news-analysis/asap/appellate-court-pauses-100000-h-1b-fee-policy-appeal-continues | Law-firm alert | B | 2026-07 | S | |
| S43 | BAL, district court vacates implementation | https://www.bal.com/immigration-news/united-states-federal-court-rules-h-1b-proclamation-implementation-unlawful-vacates-100000-h-1b-visa-fee-government-to-appeal/ | Law-firm alert | B | 2026-06 | S | |
| S44 | Fragomen, extension and vacatur | https://www.fragomen.com/insights/united-states-president-trump-extends-dollar100000-h-1b-fee-but-policy-currently-vacated-by-court-order.html | Law-firm alert | B | 2026-09 | S | |
| S45 | Univ. of Colorado ISSS, fee status | https://www.colorado.edu/isss/2026/10/07/100000-h-1b-fee-current-status | Institutional page | C | 2026-10-07 | S | ↻ date error |
| S46 | BLS, Employment Situation (archived 2025-12-16) | https://www.bls.gov/news.release/archives/empsit_12162025.htm | Agency release | A | 2025-12-16 | S | |
| S47 | DOL OFLC, H-1B FY2019 record layout | https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/H-1B_FY19_Record_Layout.pdf | Agency data layout | A | FY2019 | S | |
| S48 | DOL OFLC, LCA FY2020 record layout | https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Record_Layout_FY20.pdf | Agency data layout | A | FY2020 | S | |
| S49 | DOL OFLC, performance data page | https://www.dol.gov/node/138147 | Agency page | A | n.d. | S | ↻ non-canonical node URL |
| S50 | AILA, OFLC Q3 FY26 release notice | https://www.aila.org/library/oflc-releases-public-disclosure-data-and-selected-program-statistics-for-q3-of-fy26 | Association notice | B | 2026-08 | S | |
| S51 | JobsPipe, H-1B salary database | https://jobspipe.dev/blog/h1b-salary-database | Vendor blog | D | n.d. | S | COI:vendor |
| S52 | Levels.fyi, company salary page (Opensignal) | https://www.levels.fyi/companies/opensignal/salaries.md | Salary platform | B (definitions); E (verification claim) | n.d. | S | COI:vendor |
| S53 | Stanford Digital Economy Lab, Canaries (Aug 2026) | https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf | Working paper | A (attr.); B (inference) | 2026-08 | F | data partner ADP |
| S54 | Stanford, Canaries (Nov 2025 version) | https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf | Working paper | A (attr.) | 2025-11 | S | |
| S55 | SIEPR, Canaries (Aug 2025 version) | https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial | Working paper | A (attr.) | 2025-08-26 | S | |
| S56 | Yale Budget Lab, "Evaluating the Impact of AI…" | https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs | Think-tank analysis | B | 2025-10-01 | S | |
| S57 | Yale Budget Lab, tracking page | https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market | Think-tank dashboard | B | updated 2026-03 | S | |
| S58 | Peng et al., Copilot productivity (arXiv 2302.06590) | https://arxiv.org/abs/2302.06590v1 | Preprint | B | 2023-02-13 | S | COI:vendor |
| S59 | TechCrunch, METR study coverage | https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows | Trade press | B | 2025-07-11 | S | |
| S60 | METR, developer-productivity update | https://metr.org/blog/2026-02-24-uplift-update/ | Research org (primary) | A (attr.) | 2026-02-24 | S | |
| S61 | ScienceBlog, METR summary | https://scienceblog.com/?p=582102 | Science news | C | 2026 | S | |
| S62 | 80,000 Hours, analysis of the MIT study | https://80000hours.org/podcast/episodes/ai-workplace-mit-study/ | Podcast with transcript | C | 2026-04-28 | F | |
| S63 | Fortune, "MIT report: 95%…" | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | News | C | 2025-08-18 | S | sample-size conflict |
| S64 | aiwiki.ai, GenAI Divide entry | https://aiwiki.ai/wiki/mit_genai_divide_report/raw | Wiki | D | n.d. | S | |
| S65 | LetsDataScience, report summary | https://letsdatascience.com/news/mit-report-documents-genai-pilot-roi-gap-e0924d7d | News aggregator | D | n.d. | S | |
| S66 | NANDA, "State of AI in Business 2025" (mirror) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | Primary report | A (unread) | 2025-07 | M | fetch refused |
| S67 | CFR, Anthropic CEO speaker event | https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic | Primary event page | A (unread) | 2025-03-10 | M | COI:anthropic |
| S68 | LessWrong, "Is 90% of code at Anthropic being written by AIs?" | https://www.lesswrong.com/posts/prSnGGAgfWtZexYLp/is-90-of-code-at-anthropic-being-written-by-ais | Named-analyst post | C | 2025-10-22 | F | partly private sources |
| S69 | Anthropic Institute, "When AI builds itself" | https://www.anthropic.com/institute/recursive-self-improvement | First-party essay | A (unread) | 2026-06-04 | M | COI:anthropic; fetch refused |
| S70 | Fortune, report on the Anthropic essay | https://fortune.com/2026/06/05/anthropic-ai-pause-development-recursive-self-improvement | News | B | 2026-06-05 | S | |
| S71 | The State of AI, 80%-of-code item | https://www.thestateofai.com/news/anthropic-80-percent-code-not-engineers | Newsletter | C | 2026-06 | S | |
| S72 | GPTZero, NeurIPS hallucinated-citation scan | https://gptzero.me/news/neurips/ | Vendor report | C | 2026-01 | S | COI:vendor; 51 vs 53 |
| S73 | arXiv 2602.05930, citation failure modes | https://arxiv.org/pdf/2602.05930 | Preprint | B | 2026-02 | S | uses S72 data |
| S74 | TechCrunch, NeurIPS citations coverage | https://techcrunch.com/?p=3084660 | Trade press | B | 2026-01 | S | |
| S75 | HALLMARK, citation-verifier failure modes (arXiv 2607.18360) | https://www.alphaxiv.org/abs/2607.18360 | Preprint | B | 2026-07 | S | |
| S76 | Benesch, Operation AI Comply one year on | https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus.html | Law-firm alert | B | n.d. | S | |
| S77 | Crowell, FTC and AI-detection claims | https://www.crowell.com/en/insights/client-alerts/ftc-cracks-down-on-ai-models-ai-detection-claims | Law-firm alert | B | n.d. | S | |
| S78 | FTC, Workado order press release | https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-order-requires-workado-back-artificial-intelligence-detection-claims | Agency release | A (unread) | 2025-04 | M | unread |
| S79 | APS Observer, reproducibility report (OSC 2015; doi 10.1126/science.aac4716) | https://www.psychologicalscience.org/publications/observer/obsonline/report-demonstrates-need-for-improved-reproducibility-in-psychological-science.html | Association summary | B | 2015 | S | psychology analogue |
| S80 | Crossref Community, Labs-API deprecation post | https://community.crossref.org/t/deprecating-retraction-watch-annotations-in-the-labs-api/15884 | Maintainer post | A | n.d. | S | |
| S81 | Crossref staff page (Rittman), rate-limit and Retraction Watch posts | https://crossref.org/people/martyn-rittman | Maintainer index | A | 2025-12 | S | |
| S82 | Semantic Scholar API overview | https://semanticscholar.org/product/api | Vendor docs | A | n.d. | S | ↻ conflicts with S83 |
| S83 | Semantic Scholar API tutorial | https://webflow.semanticscholar.org/product/api/tutorial | Vendor docs | A | n.d. | S | ↻ staging-style host |
| S84 | CASRAI guide, Semantic Scholar API | https://casrai.org/guides/semantic-scholar-api | Third-party guide | C | 2026-08 | S | |
| S85 | Google Search Central blog, simplifying results | https://developers.google.com/search/blog/2025/06/simplifying-search-results | Vendor docs | A | 2025-06-12 | S | ↻ `?authuser=1` removed |
| S86 | Nieman Lab, fact-check snippet removal | https://www.niemanlab.org/2025/06/google-kills-the-fact-checking-snippet/ | Trade press | B | 2025-06 | S | |
| S87 | Poynter IFCN, ClaimReview snippets removed | https://www.poynter.org/ifcn/2025/google-claimreview-fact-checks-snippets-removed/ | Trade press | B | 2025-06 | S | |
| S88 | Wikipedia, Manual of Style: Dates and numbers | https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers | Project guideline | A (attr.) | n.d. | S | ↻ URL reconstructed; search returned a mirror |
| S89 | Wikipedia, Template:As of | https://en.wikipedia.org/wiki/Template:As_of | Project template | A (attr.) | n.d. | S | ↻ URL reconstructed; search returned a mirror |
| S90 | GitHub Docs, style guide (alerts) | https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide | Vendor docs | A | n.d. | S | |
| S91 | Hugo docs, blockquote render hooks | https://gohugo.io/render-hooks/blockquotes/ | Project docs | B | n.d. | S | |
| S92 | lychee (repository) | https://github.com/lycheeverse/lychee | Project docs | A | n.d. | S | |
| S93 | lychee-action releases | https://github.com/lycheeverse/lychee-action/releases | Project docs | A | n.d. | S | |
| S94 | adr.github.io pull request 93 | https://github.com/adr/adr.github.io/pull/93 | Community PR | C | n.d. | S | |
| S95 | Recalled-only references (◌): RFC 2119 and 8174; WCAG 2.x SC 1.4.1; Landis–Koch bands; ALFRED; OpenAlex; IFCN Code of Principles; eCFR versioner; CourtListener/PACER; GFM footnotes; Crossref header names | none | Memory | D | n.d. | M | unverified |

## 10. Formal Epistemic Protocol Specification (EGP-1.0)

### 10.0 Status, scope and language

- EGP-1.0 governs every repository file that states a fact about the world: salary and compensation figures, hiring and layoff counts, technical specifications, prices, policy and legal status, study findings, attributions and forecasts.
- Out of scope: subjective philosophical opinions. They MUST be labelled `[OPINION]` and MUST NOT be used as support for a factual claim.
- MUST, MUST NOT, SHOULD and MAY in capitals carry their RFC 2119/8174 meanings ◌.
- Session documents such as this one MAY use `S##` tags in place of inline markers. Repository content pages MUST use inline markers (§10.4).
- Where rules conflict, the more restrictive applies; the Evidence Steward breaks ties (§10.14).

### 10.1 Definitions

| Term | Meaning |
|---|---|
| Claim | One empirical statement about one measurand |
| Empirical sentence | A sentence that (i) contains a number, percentage, currency amount, date, version identifier or a quantifier or comparison about the world; (ii) attributes an action or status to a named entity (announced, raised, requires, supports, deprecated, banned, hired); (iii) makes a present-tense existence or capability claim about a product, policy or dataset; or (iv) asserts causation. Exempt: code blocks, front matter, definitions of the repository's own terms, labelled hypotheticals |
| Measurand | What is measured, fixed by population, unit, period, statistic and definition |
| Attribution claim | "Source S states or reports X" |
| Assertion claim | "X is the case in the world" |
| Anchor | A phrase of at most 15 words, or a numeric string, found on the source and evidencing the claim, with a locator |
| `as_of` | The date the described state of the world refers to ("data through 2026-06") |
| `published` | The date of the source or of its specific version |
| `last_verified` | The date a verifier last reopened the source and rechecked anchor, status and retraction state |
| TTL | Maximum days between verifications for the claim's volatility class |
| Trigger | An event that ends a claim's validity before its TTL |
| Interested party | A source that gains if the claim is believed (vendor, employer, advocate, the maker of a forecast) |
| Vintage | A specific release or version of a dataset, document or page |

### 10.2 Claim types

| `type` | What it asserts | Example from AI careers | Needed for grade A or B | Ceiling if missing |
|---|---|---|---|---|
| `fact_of_record` | Law, specification, price, lifecycle date or status | "Proclamation 10973 imposes a $100,000 payment on certain new H-1B petitions" | The issuing authority's own document, opened | Secondary only: B. Not opened: D |
| `measurement` | A statistic or estimate | "Median total compensation of X" | Instrument, population, period, n, vintage | No instrument: D |
| `performance` | A product's accuracy, speed or impact | "Tool X is 98% accurate" | Independent measurement with a stated protocol | Vendor-only: E |
| `causal` | One thing caused another | "AI reduced entry-level hiring" | An identification design (randomisation or credible quasi-experiment) or a systematic review | Descriptive evidence only: may be written as "associated with", never as cause |
| `forecast` | A future state | "AI will write 90% of code within six months" | A published model or assumptions, a horizon and a resolution criterion | Bare prediction: assertion grade E; attribution graded normally |
| `attribution` | Who said or reported what | "A CEO said X on date D" | The primary recording, transcript or document, with date and context | Secondary quotation: C |
| `opinion` | Evaluative or philosophical view | — | Out of scope | — |

### 10.3 Evidence grades

#### 10.3.1 Rubric

| Grade | Definition | Qualifying source types | Permitted phrasing | AI-career examples (this session) |
|---|---|---|---|---|
| **A** | Direct primary record, opened by the verifier | Statutes, regulations, Federal Register documents, court opinions and orders, official data releases with their record layouts, a vendor's own documentation *for facts about that vendor's product*, regulatory filings ◌, a peer-reviewed article *for its own sample and design*, a report or working paper *for what it states* | Plain assertion for `fact_of_record`, with a date for status; "Study X found…" for studies | Proclamation 10973 text (S36); BLS release on missing October 2025 data (S46); the Fifth Circuit's holding (S24); Anthropic's deprecation dates for Anthropic models (S27, COI); the Stanford PDF's statement that its 2026 analysis is descriptive (S53) |
| **B** | Authoritative secondary, or primary whose method must be taken on trust | Surveys and analyses with public methodology; reporting by established news and legal outlets that cites primary documents; preprints and working papers for their findings; platform aggregates with disclosed n and definitions; a tier-1 engineering blog *for how its own systems work* | Attribute, and give method: "According to…, n=…" | Pew link-rot figures (S11); law-firm alerts on the 2026-07-24 stay denial (S41); Peng et al.'s 55.8% as a finding of that study (S58); METR's 2025 result (S59) |
| **C** | Reputable practitioner reporting | Named-person conference talk, named-guest podcast, high-reputation newsletter, forum post with analysis by a named author, executive statements as quotations | "Name (role) said or estimated… (medium, date)". MUST NOT be sole support for a number or appear in a table of figures | 80,000 Hours analysis of the NANDA report (S62); a named analyst's ~50% estimate (S68) |
| **D** | Informal community signal, second-hand or unattributed material, or anything recalled from memory | Reddit, Blind, Discord threads; unattributed or unreviewed blogs; explainers summarising a primary; claims from model weights | Leads and sentiment colour in a labelled box. No numbers in tables, summaries or recommendations | A community guide's summary of notice policy (S29); every `◌` item (S95) |
| **E** | Speculative, unverifiable or promotional | Vendor marketing; unsupported superlatives; bare forecasts used as evidence about the future; untraceable viral statistics; model hallucinations | Only in the Hype Register, or as an attributed quotation with a warning. Never asserted | A salary platform's verification superlative (S52); "98% accurate" (S76–S78); "76% fewer tokens" (S31); "90% of all code is AI-written" as an industry statistic (no evidence found) |

#### 10.3.2 Attribution versus assertion

- An **attribution claim** is graded by access depth: A if the verifier opened the source itself; B if known through a reliable secondary that quotes or links it; C through a practitioner summary; D otherwise.
- An **assertion claim** is graded by source tier (§10.3.1), then flags and caps (§10.3.4).
- A claim MUST be phrased in the form its grade supports. If the assertion grade is below B, the writer MUST use attribution form.
- Repetition never raises a grade. "Widely reported" and "many sources say" are prohibited as support.

Worked pair from S53: the attribution claim "the August 2026 version reports a 19% shortfall in employment for 22–25-year-olds in the most AI-exposed occupations relative to less-exposed peers, as a descriptive measure" is **A**. The assertion "employment of young workers in AI-exposed occupations has fallen relative to peers in ADP data" is **B**. The causal sentence "AI cost young workers 19% of jobs" carries −D and −S, lands at D, and is **not permitted**.

#### 10.3.3 Assignment procedure

1. **G1 Access.** Did the verifier open the originating document, dataset or ruling? If not, the ceiling is B; if the claim is only recalled, the ceiling is D (MEM).
2. **G2 Interest.** Does the source benefit if the claim is believed? First-party specifications and status: no change. Performance or impact claims: ceiling C until independently corroborated. Promotional copy: E.
3. **G3 Method.** Are instrument, sample, period and definitions public and sufficient to assess? If not, apply −M.
4. **G4 Scope.** Is the claim phrased within the evidence's population, period and causal strength? If not, rewrite it, or apply −D (and −S for a general or causal claim from one study).
5. **G5 Retrievability.** Can a reviewer reach the source, and is it archived? If not, apply −P; after 14 days the ceiling is D (DEAD).
6. **G6 Currency.** Is the claim within TTL and not superseded? If not, apply −V; the claim shows ⏳ and leaves summaries.

#### 10.3.4 Flags, ceilings and corroboration

| Flag | Meaning | Effect |
|---|---|---|
| −M | No usable methodology or instrument | One notch down |
| −I | Interested party without independent corroboration | One notch down |
| −V | Past TTL, or superseded vintage | One notch down |
| −S | Single study or single source for a general or causal claim | One notch down |
| −D | Definition or scope mismatch between claim and evidence | One notch down |
| −R | Correction, retraction or expression of concern pending | One notch down; resolve within 14 days; if retracted: E and delete |
| −P | Paywalled, unreachable, or archive missing | One notch down |

| Ceiling | Trigger | Absolute cap |
|---|---|---|
| MEM | Recalled from memory or model output, or source not opened (depth M) | D |
| PROMO | Vendor marketing or promotional copy supporting a `performance` claim | E |
| DEAD | Source unreachable and unarchived for more than 14 days | D |
| UNDATED | No `as_of` date | D |
| HALLUC | Citation does not resolve or was fabricated | E, and delete |
| BAN | Source on the banned-archive list | Invalid; remove |

**Formula.** `grade = min( base_tier − flags + corroboration, ceilings )`, floored at E. **Corroboration** adds at most one notch and only when no flag and no ceiling applies. It requires two sources from different organisations, neither derived from the other, both opened by the verifier, each at least one notch below the target grade or better. It never lifts a claim above A.

#### 10.3.5 Worked grading examples

| Claim | Type | Source and facts | Result |
|---|---|---|---|
| "Proclamation 10973 imposed a $100,000 payment on certain new H-1B petitions" | `fact_of_record` | S36 opened; government source; archived | **A** |
| "As of 2026-10-21, collection of the payment is blocked" | `fact_of_record` (status, V0) | Law-firm alerts S39–S44 (B). Verified within 14 days: no flag. Verified 20 days ago: −V | **B**; **C** with ⏳ when stale |
| "AI will write 90% of code in six months" | `forecast` | S67 and S68; bare prediction | Assertion **E**; attribution **C** (via S68) |
| "More than 80% of code merged at Anthropic in May 2026 was authored by Claude" | `measurement` (first-party) | S69 not opened; reported by S70 (B); interested party, no independent corroboration (−I) | Attribution via S70: **B**. Assertion: **C** with `COI` badge. Any industry-wide version: **no claim permitted** |

#### 10.3.6 Where each grade may appear

| Zone | A | B | C | D | E or UNVERIFIED |
|---|---|---|---|---|---|
| Title, summary or TL;DR, recommendation | Yes | Yes (attribution, or with caveat) | No | No | No |
| Tables of figures | Yes | Yes, with n and as-of | No | No | No |
| Body prose | Yes | Yes | Attributed | Labelled box only | Hype Register only |
| Sole support for a decision-critical claim | Yes | Yes | No | No | No |

### 10.4 The Cite-or-Flag contract

**Rules**

| ID | Rule |
|---|---|
| C1 | Every empirical sentence MUST end with an inline evidence marker (IEM) or `[UNVERIFIED]` |
| C2 | IEM grammar: a grade letter in brackets followed by a footnote reference to a claim ID; optional status tags may follow (below) |
| C3 | `[UNVERIFIED]` MUST carry a task footnote `u####` with reason, owner, opening date and an expiry no more than 30 days away. Reason codes: MEM, PAYWALL, NO-METHOD, NO-PRIMARY, CONFLICT, OTHER. At expiry the claim is verified or deleted; CI fails otherwise |
| C4 | Forbidden zones: titles, summaries, recommendations, tables of figures and captions MUST NOT contain grade D, grade E, `[UNVERIFIED]`, stale or contested claims |
| C5 | A decision-critical claim MUST rest on at least one A or B claim within TTL, and the page MUST state the strongest counter-evidence with its grade |
| C6 | Interested-party performance or impact claims MUST use attribution form and carry the 🏷️ badge |
| C7 | Forecasts MUST carry `[FORECAST]`, the speaker, date, horizon and resolution criterion, and be listed in the Prediction Register |
| C8 | Relative-time words ("now", "currently", "recently", "latest", "so far") are prohibited; use ISO dates or "as of YYYY-MM-DD" (the same practice as S88, S89) |
| C9 | No orphan statistics: every number needs population, period, unit and source vintage in the ledger |
| C10 | Quotations MUST NOT exceed 15 words; paraphrase otherwise, with a locator |
| C11 | Symmetric burden: claims that raise or lower the apparent appeal or risk of AI careers meet identical evidence requirements |
| C12 | Claims first produced by a model carry `origin: model_memory`, are capped at D until externally verified, and MUST be disclosed in the pull request |

**Syntax**

```markdown
Proclamation 10973 imposed a $100,000 payment on certain new H-1B petitions. [A][^c0101]

[^c0101]: **A** · Proclamation 10973, 90 FR 46027 (2025-09-24), FR Doc. 2025-18601 · as of 2025-09-19 · verified 2026-10-21 · TTL V6 · [govinfo](https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18601.pdf) · [archive](https://web.archive.org/web/<timestamp>/<url>)
```

```markdown
Vendor X says its detector is 98% accurate. [UNVERIFIED][^u0007]

[^u0007]: reason=NO-METHOD · owner=@steward · opened=2026-10-21 · expires=2026-11-20
```

```markdown
In March 2025 a CEO predicted AI would write 90% of code within three to six months. [C][^c0102] [FORECAST]
```

Status tags that MAY follow the IEM: `[FORECAST]`, `[CONTESTED]`, `[HISTORICAL]`. The footnote body is generated from the claim ledger and MUST begin with the same grade letter as the inline marker; CI rejects a mismatch (EG002).

### 10.5 Ledgers and registries

All files live under `evidence/`. Field names below are the ones the reference linter reads (§10.12).

```yaml
# evidence/sources.yaml
- id: S36
  title: "Proclamation 10973, Restriction on Entry of Certain Nonimmigrant Workers"
  publisher: "Executive Office of the President"
  type: presidential_document          # see §10.7 for the type list
  citation: "90 FR 46027 (2025-09-24); FR Doc. 2025-18601"
  url_canonical: "https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18601.pdf"
  url_archive: "https://web.archive.org/web/<timestamp>/<url>"
  url_archive_secondary: "https://perma.cc/<guid>"
  published: 2025-09-24
  retrieved: 2026-10-21
  retrieval_depth: F                   # F full text, S snippet or abstract, M not opened
  content_sha256: "<64 hex characters>"
  interested_party: []                 # e.g. [vendor-name]
  paywalled: false
```

```yaml
# evidence/claims.yaml
- id: c0101
  text: "Proclamation 10973 imposed a $100,000 payment on certain new H-1B petitions."
  type: fact_of_record
  grade: A
  grade_trace: {base: A, flags: [], ceilings: [], corroboration: 0}
  source_ids: [S36]
  anchor: "Restriction on Entry of Certain Nonimmigrant Workers"   # at most 15 words
  locator: "Sec. 1, p. 46027"
  measurand_id: h1b-fee-instrument
  as_of: 2025-09-19
  last_verified: 2026-10-21
  ttl_class: V6
  triggers: []
  caveat: ""                           # human-written limits from the source's own notes
  origin: human                        # human | model_memory | import
  verifier: "@steward"
  status: live                         # live | stale | contested | historical | retracted
```

```yaml
# evidence/facts.yaml  (volatile facts, written once and transcluded)
h1b_fee_collection_status:
  claim_id: c0140
  ttl_class: V0
  render: "As of {last_verified}, collection of the $100,000 payment is blocked by court orders against the implementing policies; appeals are pending. {iem}"
  triggers: ["docket activity", "Federal Register notice", "new proclamation"]
```

Pages include a fact with `<!-- fact:h1b_fee_collection_status -->` and `<!-- /fact -->`; a build step regenerates the sentence from `facts.yaml`, adds ⏳ when stale, and fails the build if any fact is hard-expired. Other registries: `unverified.yaml` (C3 tasks), `hype_register.yaml` and `predictions.yaml` (§10.9), `contradictions/CON-YYYY-NNN.yaml` (§10.8).

### 10.6 Temporal recency protocol

| Class | Name | Default TTL | Typical content | Evidence basis | Early-expiry triggers |
|---|---|---|---|---|---|
| V0 | Live status | 14 days | Enforceability of contested policies; pending rulemaking; incident or outage status | Eight dated legal events in 123 days (S39–S44) | Docket activity; Federal Register notice; agency guidance; new proclamation |
| V1 | Monthly series | 31 days | Monthly employment and openings statistics; job-posting indices; layoff counts | Monthly release cadence; gaps and vintages (S46) | New release; revision; benchmark |
| V2 | Platform and product facts | 90 days | API prices, model IDs and lifecycle dates, rate limits, context windows, SDK behaviour, leaderboard ranks, plan terms | Seven deprecation notices in 340 days (S27); a 67% price cut (S30, S31) | Changelog or pricing-page hash change; deprecation notice; new model release |
| V3 | Market estimates and tool-generation findings | 180 days | Compensation medians; quarterly datasets; effect sizes of AI tools; skills-demand rankings | Quarterly LCA releases (S49, S50); METR's own result superseded in about seven months (S59, S60) | New quarterly release; new paper version; new tool generation |
| V4 | Annual and stable text | 365 days | Final-rule and statute text; annual datasets; durable empirical findings | A 364-day proclamation term (S36, S38) | Amendment; sunset date; erratum; retraction |
| V5 | Foundations | 1,095 days | Core engineering, statistics and evidence-synthesis principles; definitions | Clinical-review update signals (S12); a durable directive (S04) | New edition; major refutation |
| V6 | Historical record | none | Dated past events and publication facts, in past tense with an absolute date | — | Correction or retraction only |

**Reading the brief's probes against the table.** Model inference cost: list prices and lineups are V2 (90 days, the brief's three months), while a *trend* in price per capability is V3. Visa regulations: final-rule or proclamation *text* is V4 (365 days), but enforceability and litigation *status* is V0 (14 days); 12 months would have been unsafe (KF4). Core engineering principles: V5 (36 months) is a ceiling reserved for foundations, not for practice guidance on fast-moving AI tooling, which is V3.

**Rules**

| ID | Rule |
|---|---|
| T1 | TTL = min(class TTL, the source's `cadence_days`, days until the instrument's stated end date). A 12-month proclamation expires at its sunset |
| T2 | Triggers MAY shorten a TTL and MUST NOT lengthen it |
| T3 | Every claim carries three dates: `as_of`, `published`, `last_verified`. The linter requires `as_of` ≤ `last_verified` ≤ today |
| T4 | `last_verified` is set only by a human or CI job that reopened the source and rechecked anchor, status and retraction state. Prose edits MUST NOT change it. The verifier's ID is recorded |
| T5 | A page's "Evidence verified through" date is the *oldest* `last_verified` among its claims, never the file's modification date |
| T6 | **Staleness ladder, in age since verification:** over 1.0× TTL the claim is stale (⏳; error for V0–V2, warning for V3–V5; excluded from summaries and recommendations); over 1.5× TTL it is hard-expired (error for every class; delete or move to `stale/`) |
| T7 | Volatile facts are written once in `facts.yaml` and transcluded; pages MUST NOT retype status or price values |
| T8 | Events are written as dated events ("On 2026-09-30, a district court enjoined…"), which are V6. "Current status" appears only as a transcluded fact with a TTL |
| T9 | Versioned sources are pinned by version or vintage, and headline numbers are recorded per version (S53–S55) |
| T10 | When a source retracts, replaces or labels its own result historical (S60, S61), every claim depending on it takes −V until regraded |

### 10.7 Citation and preservation standards

#### 10.7.1 Canonical URLs

| ID | Rule |
|---|---|
| U1 | https only; lowercase host; no default port (DOL links in this session carried `:443`, S47, S48) |
| U2 | Strip tracking, session and locale parameters: `utm_*`, `fbclid`, `gclid`, `authuser`, `lang` (the last two appeared in this session's results for S85 and S49) |
| U3 | Prefer persistent identifiers: DOI as `https://doi.org/…`; arXiv with a version (`/abs/2302.06590v1`); Federal Register citation plus govinfo URL; docket numbers; commit-SHA permalinks, never branch URLs |
| U4 | Pin versions: PDF vintage, the page's "last updated" text, dataset release plus record layout |
| U5 | If a page has no persistent identifier, record URL, retrieval timestamp, content hash and archive URL |
| U6 | Record both the original and the final URL after redirects |
| U7 | Prefer the publisher's host over mirrors; when only a mirror was reachable, say so (S66, S88) |
| U8 | No link shorteners, AMP or mobile variants |

#### 10.7.2 Citation templates by source type

| Source type | Required fields |
|---|---|
| Presidential document, regulation | Instrument number, Federal Register citation, date, FR Doc. number, govinfo URL. Status is a separate V0 claim |
| Court ruling | Court, caption, docket number, order date, link to the order. Cite the order itself only if opened; otherwise cite the secondary and say so. Appeal status is a separate V0 claim |
| Agency dataset | Agency, dataset, period, release date, vintage and record layout, file name, retrieval date, hash |
| Vendor documentation or pricing | Vendor, page title, section anchor, doc version if shown, retrieval date, archive snapshot, content hash |
| Paper | DOI, version, peer-review status, correction-check date. For a preprint, check Crossref and Semantic Scholar for a published version at each re-verification |
| Versioned working paper | Version label and date, data-through date, headline number per version |
| Dashboard | Dated snapshot with archive link; no "live" dashboards without one |
| Podcast or talk | Person, role, show or event, date, timestamp, transcript archive |
| Forum or social post | Archive link, permalink, handle, timestamp; grade D at most; no figures extracted |
| Model output | Not citable. Origin `model_memory` until externally verified |

#### 10.7.3 Archive-on-cite protocol

| Step | Action |
|---|---|
| AC1 | Resolve the URL; record final URL, HTTP status and a UTC timestamp |
| AC2 | Capture in the Wayback Machine (Save Page Now); record the snapshot URL. If unavailable, retry within 24 hours and set `archive_pending: true` (the October 2024 outage, S20, S21, shows this happens) |
| AC3 | For A or B sources behind decision-critical claims, also create a Perma.cc link after confirming account quota (S13–S16) |
| AC4 | Store a SHA-256 of the extracted main text, and of the raw file for PDFs and datasets, plus the anchor and locator. Store full copies only for public-domain government text or where the licence allows |
| AC5 | Banned: the archive.today family (`archive.today`, `.is`, `.ph`, `.fo`, `.li`, `.md`, `.vn`), because alteration of snapshots is documented (S22, S23) |
| AC6 | Weekly: link-check with lychee using its cache and explicit accepted status ranges (S92–S94). On failure, render the archive link and open an issue; 14 days to repair or apply −P |
| AC7 | Monthly: re-fetch A and B sources and compare hashes. A change sets `possible_silent_edit` and fires a trigger, because vendors edit pricing and policy pages in place |
| AC8 | Legal and regulatory claims cite court-issued or agency-issued documents; archive copies support verifiability, not admissibility (S24–S26) |

### 10.8 Contradiction Adjudication Protocol (CAP-1)

**Triggers.** Two live claims share a `measurand_id` and differ by more than 5% (relative) or categorically; a reviewer, reader or CI job flags a conflict, correction or retraction; a new vintage of a source disagrees with a live claim.

**Outcome classes**

| Code | Class | Meaning | Action |
|---|---|---|---|
| R0 | False conflict | Misquote, typo, or one origin counted twice | Fix or annotate; log the error pattern (for example the 2027 date in S45; the sample sizes in S63) |
| R1 | Superseded | One value is an older vintage or version of the same series or source | Adopt the newer; keep the older as V6 history; note the difference |
| R2 | Definitional split | Both are valid for different constructs | Present both with definitions; never merge |
| R3 | Method dominance | One is clearly stronger on pre-set criteria | Adopt it as primary; keep the weaker in a dissent log if widely believed |
| R4 | Irreducible | A credible same-construct conflict persists | Publish a range with reasons; review within 90 days; name the tie-breaking data |
| R5 | Rejected | Retracted, fabricated, hallucinated or unreachable | Remove; log |

**Steps**

| Step | Action |
|---|---|
| K0 | Open `contradictions/CON-YYYY-NNN.yaml`. Set both claims `status: contested`, show ⚖️, and freeze new citations of either |
| K1 | **Same-measurand test** across ten dimensions: population; geography; unit; currency and inflation base; time window and as-of; statistic (mean, median, percentile); definition of key terms ("AI job", "total compensation", "pilot"); data vintage; aggregation level; inclusion rules. Any difference makes it a definitional conflict (go to K2); none makes it an empirical conflict (go to K3) |
| K2 | **Normalise or split.** Convert only by a documented lossless transform (pay unit, currency, same vintage). Otherwise present both with their constructs. Outcome R2 |
| K3 | **Independence test.** Trace each value to its origin (the "trace claims to the original context" move, S10). If both derive from one origin, collapse them into one source (R0). Look for circular reporting |
| K4 | **Grade both** under §10.3 with flags and ceilings. A gap of two or more grades with no flag on the stronger side gives R3 |
| K5 | **Method audit** with a fixed checklist: design; sample and selection; measurement validity; time window; funding and conflicts; pre-registration; replication; corrections or retractions (S80, S81); version history |
| K6 | **Vintage rule.** Same series: the latest vintage, with revision notes. Studies: the later version by the same authors, recording differences (S53–S55). Status: the latest primary document outranks a law-firm alert |
| K7 | **Decide and classify** (R0–R5) with a rationale of at most 120 words |
| K8 | **Present** with the range-and-reasons template below. Never average. Never silently pick. If the losing view is widely believed, keep it in the dissent log with its grade |
| K9 | **Log** IDs, dates, outcome, reviewers and next review. SLA: decision-critical conflicts are resolved, or published as R4, within 14 days; others within 30. A conflict unresolved at the SLA is published as R4 automatically |
| K10 | **Escalate.** R3 and R5 need two reviewers; any conflict touching a headline recommendation gets a red-team review |

**Range-and-reasons template**

```markdown
> [!WARNING]
> **Sources disagree (CON-2026-014, class R2, reviewed 2026-10-21).** The figures below measure different things; do not compare them directly.

| Measure | Construct | Population and period | Value | Grade | As of | n |
|---|---|---|---|---|---|---|
| <source A> | <definition> | <who, when> | <value> [B][^c0301] | B | <date> | <n> |
| <source B> | <definition> | <who, when> | <value> [A][^c0302] | A | <date> | <n> |

**Why they differ:** <one to three sentences>. **What we use for decisions:** <choice and reason>. **What would resolve it:** <data>. Next review: <date>.
```

For salary conflicts the table MUST separate base pay from total compensation, offered from paid, and filed from self-reported; MUST state currency, year and n; and MUST NOT compute a "gap" across constructs. A filing-based wage (S47–S49) and a self-reported total-compensation figure (S52) are shown side by side as different things.

**Worked classifications**

| Conflict | Class | Reasoning |
|---|---|---|
| Peng +55.8% versus METR −19% | R2 | Task, population, tool era and measurement differ (S58–S60) |
| METR 2025 versus METR 2026 update | R1 | The author declared the follow-up unreliable and labelled the 2025 result historical (S60, S61); apply T10 |
| Stanford 19% versus Yale "no discernible disruption" | R2 | Different outcome (young workers in exposed occupations versus the economy-wide occupational mix) and different data (S53, S56, S57) |
| Stanford 13%, 16%, 19% | R1 | Versions of one paper; pin the version and record each (S53–S55) |
| Fortune's 150/350 versus the report's 52/153 | R0, pending primary | Open S66 and record the stated method |
| "September 30, 2027" versus 2026 | R0 | Typo in S45; the date is taken from other alerts (S39) |
| Epoch 9–900× versus ~13× versus 5–10× per year | R2 | Different thresholds and model baskets (S32–S35) |
| LCA wage versus Levels.fyi total compensation | R2 | Different constructs (S47–S49, S52) |

### 10.9 Claim archaeology and the Hype Register

**Trigger.** Any statistic that readers, press or contributors treat as common knowledge; any statistic in a headline or decision-critical claim; any statistic a reviewer flags.

**Protocol for a widely believed statistic traced to a vendor or PR survey without methodology**

| Step | Action |
|---|---|
| H0 | **Day 0, freeze.** Tag `[UNVERIFIED]` with a task; remove it from titles, summaries and recommendations |
| H1 | **Day 0–3, map the chain.** Record every wording variant and the earliest appearance found (archive timelines, scholarly citation graphs, press archives, fact-check indexes), with dates: origin, intermediaries, repeaters |
| H2 | **Find the originating instrument:** the report, survey, interview, filing or speech. Prefer the original to any description of it (S10) |
| H3 | **Day 3–10, obtain the methodology:** questionnaire or protocol, sample frame, n, dates, weighting, margin of error, sponsor, and the definition behind the headline number. Use at least three channels: the report's appendix or PDF; a written query to the author or publisher; the archive history of the page; the press office; independent re-analyses. Log each attempt with a date |
| H4 | **Check scope fidelity.** Does the number measure what the claim says (population, unit, definition, denominator)? Compare against every variant |
| H5 | **Day 14, decide.** O1: methodology found and adequate, so grade normally and correct scope drift. O2: methodology unavailable, so grade **E, "origin-untraceable"**, permitted only in the Hype Register or as an attributed quotation with a warning, never as fact. O3: found but defective (denominator, definition, tiny or non-random sample), so publish the corrected reading with the defect named. O4: misquoted or inflated downstream, so show the original statement beside the common version |
| H6 | **Interested-party check.** Who benefits? Apply −I and seek independent corroboration |
| H7 | **Recheck** quarterly or on trigger for newly published methodology; entries expire after 12 months unless renewed |
| H8 | **Phrase rule.** "Widely cited" is allowed only with a count of outlets and dates found; otherwise omit it |
| H9 | **Symmetry.** Run the same trace on doom claims and boom claims, and report the counts in the quarterly audit |

**Hype Register entries (verified facts only)**

```yaml
# evidence/hype_register.yaml
- id: HR-001
  claim_variants:
    - "95% of generative-AI pilots fail"
    - "95% of companies see no return on AI"
    - "only 5% of AI projects reach production with value"
  direction: negative
  origin: {source_id: S66, date: 2025-07, published_by: "MIT NANDA initiative", peer_reviewed: false}
  chain: [S66, S63, S64, S65]
  stated_method: "52 structured interviews, 153 survey responses, 300+ public initiatives (per S62, S64, S65; primary not yet opened)"
  conflicting_descriptions: ["150 interviews, 350-person survey, 300 deployments (S63)"]
  defects: ["not peer-reviewed", "small sample", "narrow success threshold (measurable P&L impact within six months)", "wording drifts between pilots, companies and projects"]
  interested_parties: ["authors' initiative sells a remedy (per S62)"]
  status: attributed-only            # never assert as fact
  grade_if_asserted: E
  next_review: 2027-01-21
  required_action: "Open S66; record its stated method at F depth; resolve 52/153 versus 150/350"
- id: HR-002
  claim_variants:
    - "AI will write 90% of code in three to six months"
    - "80-90% of code is now AI-written"
  direction: positive
  decomposition:
    - {claim: "forecast made 2025-03-10", type: forecast, grade: "C (attribution via S68); E (as evidence)"}
    - {claim: "more than 80% of merged code at Anthropic in May 2026 was authored by Claude", type: measurement, grade: "C (assertion; interested party)"}
    - {claim: "industry-wide share of AI-authored code", type: measurement, grade: "no claim permitted"}
  interested_parties: ["the forecaster and the measuring party are the same organisation"]
  status: decomposed
  next_review: 2027-01-21
```

```yaml
# evidence/predictions.yaml
- id: PR-2025-03-10-01
  speaker: "Anthropic CEO"
  venue: "CFR event (S67, not opened; quoted in S68)"
  statement_paraphrase: "AI could be writing 90% of code within three to six months, and essentially all within twelve"
  horizon: [2025-06-10, 2025-09-10]
  resolution_criterion: "none stated at the time"
  resolution_status: unresolved-ambiguous       # protocol classification; author judgement
  later_evidence: ["S68: 2025-10-22 third-party estimate, about half of merged code", "S69 via S70: 2026-06-04 first-party figure, more than 80% of merged code, one company"]
```

### 10.10 Badges and callouts

| Badge | Meaning | Note |
|---|---|---|
| 🟦 A | Direct primary record | Letter always shown with the glyph |
| 🟩 B | Authoritative secondary | |
| 🟨 C | Practitioner reporting | Not in tables of figures |
| 🟧 D | Informal or unverified signal | Labelled box only |
| 🟥 E | Speculative or promotional | Hype Register only |
| ⏳ | Past TTL | Added by the build |
| ⚖️ | Contested | CAP-1 record open |
| 🔮 | Forecast | `[FORECAST]` |
| 🕰️ | Historical, dated event | V6 |
| 🚩 | `[UNVERIFIED]` | Task and expiry required |
| 🏷️ | Interested-party source | Attribution form required |

- Source files keep the text tokens (`[A]`). A render step MAY replace them with glyph plus letter; glyphs never replace letters, and colour never carries meaning alone ◌ (WCAG 1.4.1).
- No external image-badge services: they add a render-time third-party dependency and a link-rot surface of their own (design reasoning, not evidence).
- Callouts use GitHub's five basic alert types only, in capitals (S90, S91): `> [!WARNING]` for contested, D, E or unverified blocks; `> [!CAUTION]` for stale or hard-expired claims; `> [!IMPORTANT]` for decision-critical constraints; `> [!NOTE]` for definitions and scope notes; `> [!TIP]` for how-to-verify hints.

Page header, generated by the build and never hand-edited:

```markdown
> [!NOTE]
> **Evidence panel** · EGP-1.0 · verified through 2026-10-21 · 🟦 12 · 🟩 9 · 🟨 3 · 🟧 1 · ⏳ 0 · ⚖️ 1 · 🚩 0 · ledger hash `abc1234`
```

### 10.11 Tool catalog

Verification: **V** verified in this session, **P** partly (some pages opened, key documents not), **M** recalled only (◌).

| Tool | Role in EGP | Facts found | Gotchas | Ver. |
|---|---|---|---|---|
| Wayback Machine: Save Page Now, CDX server, Availability API | AC2 capture; capture timelines for H1; AC6 fallback links | Three interfaces exist (S17–S19) | Availability API can return empty for captured URLs, so use CDX; 429 with Retry-After; October 2024 outage (S20, S21); no official numeric rate limit found; authentication details ◌ | P |
| Perma.cc | AC3 second archive | Maintained with partner libraries; links permanent after 24 hours; API exists; 2019 tiers and a 10-link trial (S13–S15) | Quotas inconsistent across sources (S16); confirm in the dashboard; preserves the target page only | P |
| archive.today family | Banned | Deprecated on English Wikipedia, February 2026 (S22, S23) | Altered snapshots | V |
| Crossref REST API | DOI resolution; retraction and correction status (`updated-by`, Retraction Watch source); preprint-to-published mapping | Retraction Watch data merged into the main API; limits revised 2025-12-01 (S80, S81) | Throttle from response headers, not constants ◌; identify your client with a contact address ◌ | P |
| Retraction Watch database | Source behind Crossref's retraction data; CSV distribution ◌ | Available through Crossref (S80, S81) | Coverage lag ◌ | P |
| Semantic Scholar Graph API | "Cited by" for archaeology; lookup by DOI or arXiv ID | Keyed introductory rate of 1 request per second; pages disagree on the shared unauthenticated limit (S82–S84) | Back off on 429; never hard-code limits | P |
| OpenAlex | Alternative scholarly graph | — | Access terms not verified | M |
| Google Fact Check Explorer and ClaimReview | Lead generator only | Search rich results phased out from 2025 (S85–S87) | Continued availability of the Explorer and API not verified | P |
| IFCN Code of Principles | Vetting fact-check publishers | IFCN sits within Poynter (S87) | Code text not opened | M |
| lychee and lychee-action | EG005 link checks | `--cache`, `--max-cache-age`, `--accept`, `--exclude`; action v2.x (S92–S94) | An explicit `--accept` replaces the default, so list the full range | V |
| GitHub Markdown | Alerts; footnotes ◌; permalinks ◌ | Five alert types (S90, S91) | Extended alert syntax is not GitHub-compatible | P |
| govinfo and Federal Register | Presidential documents, FR citations, public inspection | Stable PDF URL patterns (S36–S38) | Public-inspection PDFs precede official publication ◌; switch to the FR citation once published | P |
| CourtListener and PACER | Docket orders for V0 claims | — | Not seen in any result; a named follow-up for KF4 | M |
| eCFR versioner | Point-in-time regulation text | — | Not verified | M |
| ALFRED (archival FRED) | Data vintages for economic series | — | Not verified | M |
| MISP admiralty-scale taxonomy | Optional machine-readable source and information ratings | Exists (S08) | Not adopted by default | P |

### 10.12 CI linter and automation

| ID | Check | Severity | Runs in |
|---|---|---|---|
| EG001 | Empirical sentence without an IEM or `[UNVERIFIED]` | ERROR | PR (script) |
| EG002 | Marker–ledger integrity: unknown claim ID; missing footnote definition; inline grade differs from ledger grade; missing source IDs; grade outside A–E | ERROR | PR (script) |
| EG003 | Source hygiene: https only; banned archive domain; tracking parameter; malformed DOI; depth not F, S or M | ERROR | PR (script) |
| EG004 | Grade A or B without an archive URL | ERROR | PR (script) |
| EG005 | Link liveness (weekly): A or B dead more than 14 days is an error; others warn | ERROR/WARN | Scheduled (network); spec only |
| EG006 | Dates and TTL: `as_of` ≤ `last_verified` ≤ today; stale; hard-expired at 1.5× TTL; near-expiry notice within 14 days | ERROR/WARN/INFO | PR (script) |
| EG007 | Ceilings: memory-only source; `model_memory` origin; vendor marketing behind a performance claim | ERROR | PR (script) |
| EG008 | Retraction or correction found on any cited DOI | ERROR | Scheduled (network); spec only |
| EG009 | Forbidden zones: grade D, E or `[UNVERIFIED]` content, or stale or contested claims, under summary or recommendation headings | ERROR | PR (script) |
| EG010 | Forecast-like sentence without `[FORECAST]` | WARN | PR (script) |
| EG011 | Quotation or anchor over 15 words | WARN | PR (script) |
| EG012 | Conflicting values for one measurand without a resolution record | ERROR | PR (script) |
| EG013 | Relative-time wording without an as-of date | WARN | PR (script) |
| EG014 | Interested-party A or B claim without independent corroboration | WARN | PR (script) |
| EG015 | Monthly re-fetch: hash changed or anchor string absent, which opens a re-verify task | TASK | Scheduled (network); spec only |
| EG016 | `[UNVERIFIED]` task past its expiry date | ERROR | Spec only (needs `unverified.yaml`) |

The reference implementation below covers every rule marked "script". I ran it against a fixture seeded with one defect per rule and against a clean fixture: each implemented rule fired on its seeded defect, and the clean fixture exited 0. It is heuristic: the empirical-sentence test is a regular expression, so expect false positives (for example numbers in table headers) and tune rather than disable.

```python
#!/usr/bin/env python3
"""EGP-1.0 reference linter: offline checks only (network checks run as separate scheduled jobs).
Usage:  python tools/evidence_lint.py --docs docs --claims evidence/claims.yaml \
            --sources evidence/sources.yaml [--today 2026-10-21] [--strict]
Exit status 1 when any ERROR is found (or any WARN with --strict). Needs Python 3.9+ and PyYAML."""
import argparse, datetime as dt, pathlib, re, sys, urllib.parse
import yaml

TTL = {"V0": 14, "V1": 31, "V2": 90, "V3": 180, "V4": 365, "V5": 1095, "V6": None}   # days; None = no expiry
BLOCKED = {"archive.today", "archive.is", "archive.ph", "archive.fo", "archive.li", "archive.md", "archive.vn"}
TRACK = re.compile(r"^(utm_|fbclid$|gclid$|mc_eid$|ref_src$)")
DOI = re.compile(r"^10\.\d{4,9}/\S+$")
MARKER = re.compile(r"\s*(\[([A-E])\]\[\^(c\d{4})\]|\[UNVERIFIED\](?:\[\^(u\d{4})\])?|\[FORECAST\])")
EMPIRICAL = re.compile(r"(\d[\d,.]*\s?(%|percent|x|×|million|billion)|[$€£]\s?\d|\b(19|20)\d{2}\b|\bv?\d+\.\d+(\.\d+)?\b)", re.I)
RELTIME = re.compile(r"\b(now|today|currently|recently|latest|to date|so far|soon|upcoming|ongoing|this year|last year|next year)\b", re.I)
ASOF = re.compile(r"\bas of\b|\b\d{4}-\d{2}(-\d{2})?\b", re.I)
FORECAST = re.compile(r"\b(will|is expected to|are expected to|predict(s|ed)?|forecast(s|ed)?)\b", re.I)
SUMMARY_H = re.compile(r"^(summary|tl;?dr|key takeaways?|recommendation|executive summary)\b", re.I)
QUOTE = re.compile(r"“([^”]+)”|\"([^\"]+)\"")


def to_date(v):
    return v if isinstance(v, dt.date) else dt.date.fromisoformat(str(v))


def tokenise(m):                                    # replace a marker with a glued token, e.g. ⟦A:c0042⟧
    if m.group(2):
        return f"⟦{m.group(2)}:{m.group(3)}⟧"
    return f"⟦U:{m.group(4) or ''}⟧" if m.group(1).startswith("[UNVERIFIED") else "⟦F:⟧"


def lint_ledgers(claims, sources, today, out):
    sid = {s["id"]: s for s in sources}
    for s in sources:
        u = urllib.parse.urlparse(s.get("url_canonical", ""))
        if u.scheme != "https":
            out("ERROR", "EG003", s["id"], "canonical URL must use https")
        if (u.hostname or "").lower().removeprefix("www.") in BLOCKED:
            out("ERROR", "EG003", s["id"], "blocked archive domain")
        if any(TRACK.match(k) for k, _ in urllib.parse.parse_qsl(u.query)):
            out("ERROR", "EG003", s["id"], "tracking parameter in canonical URL")
        if s.get("doi") and not DOI.match(s["doi"]):
            out("ERROR", "EG003", s["id"], "malformed DOI")
        if s.get("retrieval_depth") not in ("F", "S", "M"):
            out("ERROR", "EG003", s["id"], "retrieval_depth must be F, S or M")
    groups = {}
    for c in claims:
        cid, g = c["id"], c.get("grade")
        if g not in list("ABCDE"):
            out("ERROR", "EG002", cid, "grade must be one of A-E"); continue
        src = [sid.get(x) for x in c.get("source_ids", [])]
        if not src or not all(src):
            out("ERROR", "EG002", cid, "missing or unknown source_ids"); continue
        if len(str(c.get("anchor", "")).split()) > 15:
            out("WARN", "EG011", cid, "anchor longer than 15 words")
        if g in "AB" and not any(s.get("url_archive") for s in src):
            out("ERROR", "EG004", cid, "grade A/B needs an archive URL on at least one source")
        if g in "ABC" and any(s.get("retrieval_depth") == "M" for s in src):
            out("ERROR", "EG007", cid, "memory-only source cannot support a grade above D")
        if c.get("origin") == "model_memory" and g in "ABC":
            out("ERROR", "EG007", cid, "model-memory claims are capped at D until externally verified")
        if g in "ABCD" and c.get("type") == "performance" and any(s.get("type") == "vendor_marketing" for s in src):
            out("ERROR", "EG007", cid, "vendor marketing cannot support a performance claim above E")
        if g in "AB" and any(s.get("interested_party") for s in src) and not c.get("independent_corroboration"):
            out("WARN", "EG014", cid, "interested-party source without independent corroboration")
        lv, asof = to_date(c["last_verified"]), to_date(c["as_of"])
        if not asof <= lv <= today:
            out("ERROR", "EG006", cid, "require as_of <= last_verified <= today")
        cls = c.get("ttl_class")
        if cls not in TTL:
            out("ERROR", "EG006", cid, "unknown ttl_class")
        elif TTL[cls] is not None:
            ttl, age = min(TTL[cls], c.get("ttl_days", TTL[cls])), (today - lv).days
            if age > 1.5 * ttl:
                out("ERROR", "EG006", cid, f"verified {age}d ago: hard-expired (TTL {ttl}d)")
            elif age > ttl:
                out("ERROR" if cls in ("V0", "V1", "V2") else "WARN", "EG006", cid, f"verified {age}d ago: stale (TTL {ttl}d)")
            elif age > ttl - 14:
                out("INFO", "EG006", cid, f"expires in {ttl - age}d")
        groups.setdefault(c.get("measurand_id"), []).append(c)
    for m, grp in groups.items():
        vals = [x["value"] for x in grp if isinstance(x.get("value"), (int, float))]
        if m and len(vals) > 1 and max(vals) - min(vals) > 0.05 * max(abs(v) for v in vals) \
                and not all(x.get("contradiction_id") for x in grp):
            out("ERROR", "EG012", m, "conflicting values for one measurand without a resolution record")


def lint_doc(path, by_id, out):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        text = text.split("---", 2)[2]
    defs = set(re.findall(r"^\[\^([cu]\d{4})\]:", text, re.M))
    in_code, heading = False, ""
    for n, line in enumerate(text.splitlines(), 1):
        where = f"{path}:{n}"
        if line.lstrip().startswith("```"):
            in_code = not in_code; continue
        h = re.match(r"^#{1,6}\s+(.*)", line)
        if in_code or re.match(r"^\s*(\[\^[cu]\d{4}\]:|<!--|>\s*\[!)", line):
            continue
        if h:
            heading = h.group(1).strip(); continue
        body = MARKER.sub(tokenise, line)
        for sent in re.split(r"(?<=[.!?⟧])\s+(?=[A-Z0-9\[(\"'*_`|])", body):
            marks = re.findall(r"⟦([^⟧]*)⟧", sent)
            plain = re.sub(r"⟦[^⟧]*⟧", "", sent)
            has = any(m[0] in "ABCDEU" for m in marks)
            if EMPIRICAL.search(plain) and not has:
                out("ERROR", "EG001", where, "empirical statement without evidence marker or [UNVERIFIED]")
            for m in marks:
                grade, _, cid = m.partition(":")
                if grade in "ABCDE":
                    c = by_id.get(cid)
                    if not c:
                        out("ERROR", "EG002", where, f"{cid} not in claims ledger")
                    elif c["grade"] != grade:
                        out("ERROR", "EG002", where, f"inline grade {grade} != ledger grade {c['grade']} for {cid}")
                    elif c.get("status") in ("stale", "contested") and SUMMARY_H.match(heading):
                        out("ERROR", "EG009", where, f"{c['status']} claim in summary/recommendation section")
                if cid and cid not in defs:
                    out("ERROR", "EG002", where, f"footnote definition [^{cid}] missing in this file")
                if SUMMARY_H.match(heading) and (grade in ("D", "E", "U")):
                    out("ERROR", "EG009", where, "grade D/E or [UNVERIFIED] content in summary/recommendation section")
            if RELTIME.search(plain) and not ASOF.search(plain):
                out("WARN", "EG013", where, "relative-time wording without an as-of date")
            if FORECAST.search(plain) and EMPIRICAL.search(plain) and not any(m.startswith("F") for m in marks):
                out("WARN", "EG010", where, "forecast-like sentence without [FORECAST] tag")
            for q in QUOTE.findall(plain):
                if len("".join(q).split()) > 15:
                    out("WARN", "EG011", where, "quotation longer than 15 words")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--claims", required=True)
    ap.add_argument("--sources", required=True)
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    today = to_date(a.today)
    claims = yaml.safe_load(pathlib.Path(a.claims).read_text(encoding="utf-8")) or []
    sources = yaml.safe_load(pathlib.Path(a.sources).read_text(encoding="utf-8")) or []
    msgs = []
    out = lambda sev, rule, where, msg: msgs.append((sev, rule, str(where), msg))
    lint_ledgers(claims, sources, today, out)
    by_id = {c["id"]: c for c in claims}
    for p in sorted(pathlib.Path(a.docs).rglob("*.md")):
        lint_doc(p, by_id, out)
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for sev, rule, where, msg in sorted(msgs, key=lambda m: (order[m[0]], m[1], m[2])):
        print(f"{sev:5} {rule} {where}: {msg}")
    blocking = sum(1 for m in msgs if m[0] == "ERROR" or (a.strict and m[0] == "WARN"))
    print(f"\n{len(msgs)} findings, {blocking} blocking")
    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
```

**Workflow** (not executed in this session; action versions are recalled ◌, so pin to commit SHAs and check `lychee --help` for the `--accept` range syntax at adoption):

```yaml
# .github/workflows/evidence.yml
name: evidence
on:
  pull_request:
  push:
    branches: [main]
  schedule:
    - cron: "17 5 * * 1"          # weekly sweep, Mondays 05:17 UTC
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install pyyaml
      - run: python tools/evidence_lint.py --docs docs --claims evidence/claims.yaml --sources evidence/sources.yaml
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v2
        with:
          args: >-
            --cache --max-cache-age 1d
            --accept '200..=299,429'
            --exclude 'archive\.(today|is|ph|fo|li|md|vn)'
            'docs/**/*.md' 'evidence/*.yaml'
          fail: true
```

**Scheduled network jobs** (specified, not implemented here):

| Job | Cadence | Action |
|---|---|---|
| J1 Link health | Weekly | lychee over documents and ledgers (EG005); open an issue per failure; render the archive link meanwhile |
| J2 Retraction sweep | Weekly | For every DOI and arXiv ID, query Crossref for update notices and Retraction Watch entries, and look for a published version of each preprint (EG008) |
| J3 Hash drift and anchors | Monthly | Re-fetch A and B sources; compare content hash; confirm the anchor string is still present (EG015); open a re-verify task on change |
| J4 Trigger watch | Daily | Poll the Federal Register, watched dockets and vendor changelog or pricing feeds for items listed in `facts.yaml` triggers; open a V0 or V2 re-verify task |
| J5 Expiry digest | Weekly | Post the linter's "expires in N days" lines as a single tracking issue |

**What CI cannot do.** It proves that a source exists, that a marker is wired to a ledger row, that a date is fresh and that a string is on a page. It cannot judge whether the source supports the claim, whether the scope is faithful, or whether a grade is fair. Those remain with the reviewer and the quarterly audit (§10.13), which is why O6 in §7.2 is rated medium-high.

### 10.13 Checklists and audits

#### 10.13.1 Contributor checklist (before opening a pull request)

1. Every empirical sentence ends with an IEM or with `[UNVERIFIED]` plus a task.
2. I opened every source myself (depth F or S). Nothing is cited from memory or from a model.
3. Each claim is phrased in the form its grade supports; I used attribution form wherever the assertion grade is below B.
4. Source IDs exist; URLs are canonical; DOI, arXiv, docket or Federal Register citations are included; versions are pinned.
5. Archives are captured (Wayback; Perma.cc for decision-critical A or B sources); the hash is stored; the anchor is 15 words or fewer, with a locator.
6. `as_of`, `published` and `last_verified` are set; the TTL class fits the volatility; any instrument sunset and the triggers are listed.
7. No relative-time words; status is written as dated events or as a transcluded fact.
8. Interested-party sources are flagged; independent corroboration was sought for performance and impact claims.
9. No D, E, unverified, stale or contested claim appears in a title, summary, recommendation or table of figures.
10. Conflicts have a CAP-1 record; nothing is averaged; range-and-reasons is used.
11. Viral statistics were traced to origin and the Hype Register was checked; boom and doom claims got equal scrutiny.
12. Model assistance is disclosed in the pull request; model-origin claims were verified externally.
13. Quotations are 15 words or fewer; everything else is paraphrased.

#### 10.13.2 Reviewer checklist

1. Reopen one randomly chosen source per page; confirm the anchor and the scope.
2. Regrade five claims blind to the author's grades; compare.
3. Confirm every decision-critical claim has an A or B support within TTL and a stated counter-evidence line.
4. Confirm the TTL class matches the claim's volatility (status is not text).
5. Open each archive link; confirm the hash matches.
6. Look for circular citation (two sources derived from one).
7. Confirm forecasts are tagged and registered.
8. Confirm population, period and unit match the source.
9. Check papers for retraction or correction.
10. Confirm CI is green and no waiver was granted without the Steward.

#### 10.13.3 Quarterly audit

- Draw a stratified random sample of **59** live claims (strata: TTL class and grade). Verify existence, support, scope, grade, currency and archive.
- Zero defects in 59 gives a 95% upper bound of about **4.95%** on the defect rate (computed as 1 − 0.05^(1/59) in this session); zero in 299 gives about 1.0%. Any defect widens the sample to 299 in the affected strata and triggers a root-cause review.
- Also sample **20** rejected or demoted claims to estimate false rejection (objection O4).
- Dashboard: stale ratio; claim debt (stale plus unverified plus contested); age of the oldest `[UNVERIFIED]` task; open conflicts older than 30 days; link-failure rate; archive coverage; hash-drift events; share of decision-critical claims backed by A or B; inter-rater agreement.
- Proposed thresholds (uncalibrated): stale ratio at or below 5%; no hard-expired claims; no `[UNVERIFIED]` task older than 30 days; 100% archive coverage for A and B; no conflict older than 30 days; sampled defect bound at or below 5%. A breach freezes publication of the affected pages until fixed.

#### 10.13.4 Pilot before enforcement

Two trained reviewers grade the same 50 claims independently. Compute Cohen's kappa; aim for 0.6 or higher (the "substantial" band in the Landis–Koch convention ◌). Read every disagreement, refine the rubric wording, and repeat until the target is met. Only then switch the blocking rules on.

#### 10.13.5 Workload estimate (illustrative)

For 1,000 claims in the mix V1 5%, V2 15%, V3 20%, V4 30%, V5 10%, V6 20%, the class TTLs imply about **1,936** re-verifications a year (about 161 a month, about 37 a week). This was computed from the TTLs in §10.6, not measured. Centralising volatile facts and automating link, hash and retraction checks should cut the human share; measure the real figure in the first quarter and recalibrate the classes.

### 10.14 Governance

| Item | Rule |
|---|---|
| Roles | **Evidence Steward** owns the rubric, ledgers, CI and tie-breaks. **Verifier**: any contributor who opens sources. **Reviewer**: independent of the author. **Red-team reviewer**: for headline claims, independent of any vendor named in the claim |
| Versioning | Semantic versions (EGP-1.0.0). Changes to grades, flags, ceilings or TTL classes need an issue-based proposal, a 7-day comment window and a changelog entry. Claims graded under an older version are regraded within one TTL cycle |
| Waivers | Time-boxed (30 days at most), recorded with a reason. No waivers for EG001–EG004 or EG007, and none for summary or recommendation zones |
| Appeals | A grade dispute goes to a second reviewer within 7 days; the outcome is logged |
| Protocol TTL | EGP is itself class V4: review annually, or sooner after any audit breach |
| Training | New contributors grade the examples in §10.3.5 and compare with the key |
| Disclosure | Conflicts are declared per contributor and per source (`interested_party`). The author-model disclosure in the frontmatter of this file is an instance |

### 10.15 End-to-end examples

**A. A volatile status fact (illustrative; the status will have changed by its expiry date).**

```markdown
<!-- fact:h1b_fee_collection_status -->
As of 2026-10-21, collection of the $100,000 payment is blocked by court orders against the implementing policies; appeals are pending. [B][^c0140] ⏳ re-verify by 2026-11-04
<!-- /fact -->
```

The sentence is generated from `facts.yaml` (§10.5). Its class is V0 (14 days), so it expires on 2026-11-04. After that date the build adds ⏳, drops it from summaries, and CI errors (stale V0–V2 claims block) until a verifier reopens the sources, checks the dockets and updates `last_verified`. At age 21 days (1.5× TTL, 2026-11-11) the claim is hard-expired and must be deleted or moved to `stale/`.

**B. A conflicted topic.**

```markdown
## Does AI make developers faster?

The studies measure different things. ⚖️

> [!WARNING]
> **Sources disagree (CON-2026-021, class R2, reviewed 2026-10-21).** Do not compare the figures directly.

| Study | Task and population | Tool era | Result |
|---|---|---|---|
| Peng et al. 🏷️ | One JavaScript task; 95 recruited developers | Early Copilot | 55.8% faster [B][^c0201] |
| METR (2025) | Own repositories; 16 experienced developers | Early-2025 tools | 19% slower [B][^c0202] |

METR later reported that its follow-up data were an unreliable signal because of selection effects, so its 2025 figure describes early-2025 tools only. [A][^c0203]

**What we use for decisions:** neither figure; plan on "uncertain, task-dependent". **What would resolve it:** a pre-registered study with matched tasks across tool generations. Next review: 2027-01-21.
```

**C. A decomposed hype statistic.** See HR-002 in §10.9: one sentence in circulation becomes three claims with three grades, and the industry-wide version is not permitted.

### 10.16 Change log

| Version | Date | Change |
|---|---|---|
| EGP-1.0.0 | 2026-10-21 | Initial specification: grade rubric, ceilings and flags; Cite-or-Flag contract; TTL classes V0–V6; archive-on-cite; CAP-1; claim archaeology; badges; tool catalog; reference linter; audit plan |
