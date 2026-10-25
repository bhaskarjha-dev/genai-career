---
id: T0-17
title: "GenAI engineering career economics (Oct 2026): promotion velocity, compensation inflections, equity risk-discounting, and liquidity realities"
date: 2026-10-23
status: complete-with-gaps
topic: compensation-progression-plateaus-equity
tags: [genai, compensation, promotion-velocity, job-hopping, tier-jumps, private-equity-valuation, liquidation-preference, tender-offers, secondary-markets, 83b, dilution, levels-fyi, india, europe, us]
informs_decisions:
  - "Lateral move vs. internal promotion vs. tier jump (Big Tech -> frontier lab) for a given engineer"
  - "How heavily to discount private AI-company equity when comparing an offer against liquid public RSUs"
  - "Whether and when to sell in tender offers / secondaries; 83(b) and early-exercise decisions"
  - "India-based senior engineers: routes past the local salary ceiling without physical relocation"
confidence: medium
temporal_anchor: 2026-10
---

# T0-17 — GenAI Engineering Career Economics, October 2026

> **Provenance and disclosure (read first).**
> 1. This note was produced by an AI model (Claude) made by Anthropic, and Anthropic is one of the companies analysed (valuation, tender offers, IPO timing). Every Anthropic-related fact below comes from third-party reporting, counsel announcements or data-vendor pages retrieved during this session, and was graded with the same rubric as every other company. Readers with a stake in any named company should re-verify against primary filings (SEC EDGAR once public).
> 2. Nothing here is legal, tax or investment advice. I am not a lawyer, tax adviser or financial adviser; the tax and election mechanics are summarised from IRS material and law-firm alerts and should be confirmed with a qualified professional before acting.
> 3. Model parameters in §6.3 are **assumptions**, not findings. The robust outputs are the ranking and the sensitivity structure, not the point estimates.

**Evidence-grade rubric (used throughout).**

| Grade | Meaning |
|---|---|
| **A** | Primary or canonical source retrieved in this session (statute/IRS form; the data owner's own published dataset or report; counsel's or company's own announcement). URL and title are in the ledger (§9). |
| **B** | Reputable secondary reporting or law-firm/analyst summary retrieved in this session; **or** a primary dataset with a small or self-selected sample (caveat stated). |
| **C** | Single aggregator, vendor, recruiter or community source; **or** a calculation derived from A/B inputs with stated assumptions. |
| **D** | Recalled from model weights, assumed, or unverified. A hypothesis, not evidence. |
| **G** | Gap: searched and not found (search terms recorded in §6.11). |

Citations like **[S12]** point to the ledger in §9. Items tagged **(R)** are recalled from memory and not verified this session.

**Overall confidence: medium.** *Higher:* IRS/83(b) mechanics, market-wide preference terms, tender-market statistics, the India Senior distribution, secondary-market percentiles. *Medium:* US ladder multiples, AI premium by level, frontier-lab tender facts, dilution arithmetic. *Lower:* AI-specific promotion velocity, frontier-lab level mapping, equity-model point estimates (assumption-driven), Anthropic/OpenAI IPO timing, India Staff-level pay and remote-band compression.

---

## 1. Prior (checkable propositions held *before* searching)

| # | Proposition (my initial belief, Grade D) | What would falsify it |
|---|---|---|
| **P1** | **Hop premium.** Same-tier job changes yield roughly +15–30% total compensation (TC) at the median; the "+35–50%" figure only appears when the move also crosses a level or a tier (e.g. Big Tech → frontier lab). Internal promotions raise base ~8–10% but TC ~15–25% once equity is counted; "5–10% internal raises" conflates annual merit cycles with promotion events. | Tech-specific data showing median same-tier lateral TC jumps ≥ 35%. |
| **P2** | **Promotion velocity.** Big-Tech ladders move ~1.5–2.5 years/level up to Senior, then 3–5+ years to Staff (many never); Senior is reached at ~6–9 years of experience (YOE). No public dataset shows AI engineers promoted materially faster. | Published time-in-level data split AI vs non-AI showing a material difference. |
| **P3** | **AI premium and tier step.** The AI premium is positive and grows with level (~5–20%); frontier-lab *headline* TC is ~1.5–2.5× Big Tech at the same nominal level, mostly paper equity. | Levels.fyi-type data showing a flat premium or a <1.3× frontier-lab multiple. |
| **P4** | **Preference overhang.** Market-wide terms are plain vanilla (1×, non-participating). Overhang is a *tail/cliff* risk concentrated in stale-vintage, capital-hungry or acqui-hire situations; hot AI names trade at or above their last round on secondaries, so "severe overhang" as a general description is overstated. | Term data showing widespread participating/senior/multiple preferences, or AI names broadly trading below primary. |
| **P5** | **Liquidity mechanics.** Tender offers cap sales at roughly 10–25% of holdings or a dollar cap, require 1–2 years' tenure and often exclude ex-employees; an IPO is not immediate liquidity (staged lock-ups); the 83(b) election has a hard 30-day deadline with no extension and does not apply to RSUs. | Evidence of uncapped sales, or an IRS extension mechanism. |

**The brief's "KNOWN: UNVERIFIED" claims** are tested directly: (i) "switching every 18–24 months yields 35–50% jumps vs 5–10% internal raises" → KF1 (promotion velocity in KF2); (ii) "AI unicorn paper equity often suffers severe liquidation-preference overhang" → KF6/KF7/KF11.

---

## 2. Research Question

**Decision.** What are the empirical promotion timelines, compensation inflections, equity-dilution mechanics and liquidity realities across GenAI engineering careers as of October 2026 — and how should an engineer (US, Europe, India) use them to choose between staying, lateral hops, tier jumps and private-equity-heavy offers?

**Sub-questions.**
1. Progression velocity: years of experience / months-in-level between T0→T5.
2. Internal vs external delta: TC gap between promotion and external move.
3. Equity: dilution, preference stack, secondary pricing, tender terms (OpenAI, Anthropic, Databricks, Cohere), 83(b).
4. Plateaus: where compensation stalls (Senior; India/Europe local ceilings) and what unblocks it.
5. Levers: negotiation levers for high-velocity moves.

**Tier definitions used in this note** (my operationalisation; cross-company mapping is approximate).

| Tier | Label | Big-Tech analogue | Frontier-lab analogue (Levels.fyi labels) | US all-company median TC, 2025 [S2] | Bengaluru anchor, Oct 2026 [S5] |
|---|---|---|---|---|---|
| T0 | Entry | L3 / E3 / SDE I | OpenAI L2–L3; Anthropic "Entry" | ≈ $155K | Entry median ≈ ₹18.9L (P90 ≈ ₹33.3L)* |
| T1 | Mid | L4 / E4 / SDE II | OpenAI L3–L4 | ≈ $226K | not retrieved |
| T2 | Senior | L5 / E5 / SDE III | OpenAI L4–L5; Anthropic "Senior" | ≈ $312K | Senior median ≈ ₹56.0L; P75 ≈ ₹79.9L; P90 ≈ ₹1.07Cr |
| T3 | Staff | L6 / E6 | OpenAI L5–L6; Anthropic "Lead"/"Staff" | ≈ $457K | not retrieved (see §6.8) |
| T4 | Principal / Sr Staff | L7 / E7 | OpenAI L6–L7 | ≈ $551K | not retrieved |
| T5 | Apex | Distinguished / Fellow / named frontier researcher | OpenAI L7+ and negotiated packages | not observable in medians | not observable |

\*Entry figure from a search-result snapshot of Levels.fyi (updated 4/5/2026), not a fetched page [S5 note].

The brief's INR bands: T2 ₹60L–1.2Cr; T3 ₹1.2Cr–2.5Cr (US-remote). At roughly ₹85–90 per USD (assumption; FX not verified this session) ₹2.5Cr ≈ $280–295K, i.e. *below* the Levels.fyi US all-company Senior median of ≈ $312K.

**Method.** On the order of 90 searches and page fetches across Levels.fyi, Pave, ADP, Carta, Cooley, Forge, IRS/law-firm alerts, company/counsel announcements and press. Recalled beliefs were recorded first (§1) and compared against evidence (§8). Failure modes were searched deliberately (§6.11).

**Completion status against the brief's DONE criteria.**

| DONE criterion | Status | Where |
|---|---|---|
| Empirical timeline benchmarks between each of the six tiers | **Partially met** — C/D-grade ranges only; no AI-specific series exists in the sources reached (G) | §6.1 |
| Financial differential, internal promotion vs external move | **Met** — triangulated (C), anchored on ADP, Bidwell, Pave, Levels.fyi | §6.2 |
| Concrete equity risk-discount model (valuation overhang, preference stack, liquidity) | **Met** — reproducible code; parameters are assumptions (D) | §6.3 |
| Plateau points and unblocking strategies | **Met** for US/India (Europe evidence thin, G) | §6.8 |
| Negotiation levers for high-velocity moves | **Met** | §6.9 |

---

## 3. Key Findings (12, with evidence grades)

| # | Finding (one line) | Grade | Verdict vs prior / brief |
|---|---|---|---|
| KF1 | The "35–50% per hop vs 5–10% internal" claim is **not a general rule**. Economy-wide switch premium ≈ 2–3 pp; same-tier lateral in tech ≈ +15–25% TC (triangulated); +35–50% appears when a move crosses a level or tier. | A / B / C | Brief claim **contradicted as stated**; conditionally supported |
| KF2 | **No public AI-vs-non-AI months-per-level dataset exists** (searched). Proxies: avg. Senior at ~8.6 YOE; annual promotion rate 8.6%; AI/ML promotion raises are *smaller* than average (6.5%). | G + B/C | P2 partly confirmed; AI-specific velocity unverified |
| KF3 | US ladder steps ×1.2–1.5 per tier; **AI premium rises with level (6.2% → 18.7%)**; frontier-lab headline TC ×2.0–3.1 vs all-company medians (≈ ×1.7–2.4 after equity risk-adjustment); Apex is unobservable. | A / B / C | P3 confirmed, headline multiple higher than prior |
| KF4 | **India ceiling is quantifiable:** Senior median ≈ ₹56L, P90 ≈ ₹1.07Cr, best local employers' senior medians ≈ ₹1.06–1.22Cr; the T3 band (₹1.2Cr+) starts above the local senior ceiling. | A | Confirmed |
| KF5 | Europe: medians far below US; London Senior ≈ £122K (P90 ≈ £221K); plateau evidence is indirect; UK EMI limits widened from 6 Apr 2026. | A / B / C / G | Partly confirmed |
| KF6 | **Preference overhang is not the market norm** (95.8% of Q2-2026 deals 1×; 96.4% non-participating) but is a **cliff** in tail outcomes: common ≈ a call option struck at the preference stack. | A | Brief claim contradicted as a generalisation; valid as tail risk |
| KF7 | Secondary pricing is **bimodal**: median Forge trade −3% to −7% vs last primary; top AI names at/above primary; 2021-vintage cohort at median −61%. | A / B | P4 confirmed |
| KF8 | Tender offers 2025–26: Carta median cap 20%, ~58% seller participation, ~0% median discount; frontier-lab caps are dollar-denominated ($30M OpenAI 2025; $2M Anthropic 2025) with 1–2-year tenure gates. | A / B | P5 confirmed |
| KF9 | **IPO ≠ liquidity:** OpenAI says no IPO in 2026; Anthropic timing reports conflict; SpaceX (incl. xAI) fell below its IPO price within ~5 weeks under a staged, price-triggered lock-up. | B / C | Confirmed; new evidence |
| KF10 | **Mega-round dilution is small** (≈ 3–14% per round) vs Carta medians (19.5% seed → 7.5% Series D) because valuations outrun capital raised; dilution is second-order when marks rise and first-order when they fall. | A / B | Updated |
| KF11 | Equity risk-discount model (assumption-driven): risk-adjusted value (RAV) ≈ 0.7 for lab-like and Series-C archetypes, ≈ 0.24 for a stale-vintage unicorn; **discount rate and bust probability dominate; preference structure is second-order (3–12%)**. | C / D | Model output, not measurement |
| KF12 | Hidden-trap register: verified items (83(b) 30-day rule, tenure/cap gates, vesting-cliff changes, acqui-hire carve-outs, QSBS tiers) vs recalled/unverified items; **systems-expertise premium has no controlled evidence (G)**. | A–D, G | Mixed |

### KF1 — The hop-premium claim fails as a general rule (A / B / C)
- **Economy-wide:** ADP's September 2026 release puts job-changers at +4.8% base / +7.3% gross pay growth versus job-stayers at +3.0% / +4.4% [S11] (A; all industries, not tech). The Atlanta Fed tracker had switchers at 4.8% versus stayers at 4.6% in early 2025, the narrowest gap in about a decade [S12] (B).
- **Peer-reviewed:** a study of roughly 5,000 investment-bank employees found externally hired people were paid about 18% more than internal promotees in comparable jobs, but they performed worse early and left sooner [S13, S83] (A; non-tech, older).
- **Tech-specific:** the only quantified uplift I could retrieve is Levels.fyi's coaching cohort: median comp improvement of about 21% (mid), 23% (senior) and 24% (staff) [S2] (B; self-selected buyers; includes negotiation of any offer, not only job changes).
- **Triangulation (C):** the Senior→Staff step between level medians is ×1.46 [S2], but a promotion delivers only about 16–24% TC (Pave: promoted base raise 6.5% for AI/ML, 7.7% R&D, 8.6% all; +39% in ongoing equity; equity at 30–50% of TC) [S14, S15, S17]. The gap — ≈ 22–30 pp for Senior→Staff (≈ 14–22 pp for Engineer→Senior) — is the ceiling an external move can capture, consistent with ~18% (Bidwell) and 21–24% (coaching).
- **Compounding test (C):** +35–50% every two years compounds to ×4.5–7.6 over ten years (16–22% a year). Levels.fyi medians rise only ×3.6 from Entry to Principal and ×2.0 from Entry to Senior (≈ 8.5% a year over the average 8.6 YOE to Senior) [S2, S10]. That cannot be the *median* experience; it describes tier-crossers and outliers (selection).
- **The "5–10% internal" half:** right for *base per promotion event*, wrong for TC and for annual cadence. Median merit is 3.4% (AI/ML non-promoted 4.4%), and only 8.6% of employees are promoted per year [S14–S16]. The median stayer's TC growth ≈ 3.4% + 0.086 × ~20% ≈ 5% a year; promotion-track performers reach ~9–12%.

**Verdict:** same-tier lateral ≈ **+15–25% TC**; a level-up hop **+35–50%** is plausible; tier jumps see KF3.

### KF2 — Promotion velocity: no AI-specific dataset; proxies only (G, B/C)
- Searched Levels.fyi, Pave, SignalFire, community/SEO sources for months-in-level split by AI vs non-AI: **none found** (G).
- Levels.fyi's cofounder reported that the average software engineer in its database reaches Senior at about **8.6 YOE**, with Google and Apple at ~7–9 and Netflix mostly 10+ [S10] (C; seen as a search snippet, page not fetchable). Anthropic's Levels.fyi page lists Senior at 6–8 YOE and Lead at 7–8 [S3] (B; n = 49).
- Community timelines (C/D): L3→L4 ≈ 1–2 years; L4→L5 ≈ 2–4; L5→L6 ≈ 3–5+ or never; Meta E5 treated as a de-facto terminal level by many [S20–S25].
- Pave: promotion rate **8.6%** of employees per year (flat year over year); AI/ML engineers get the *highest* non-promoted raise in R&D (4.4%) but near-bottom promoted raises (6.5%) — employers reward AI talent through annual raises and equity rather than promotion jumps [S15, S16] (B). AI/ML annual attrition was reported at ~28% vs ~17% for software engineers (2025 data) [S18] (B).
- SignalFire reports AI engineers move into management in under three years on average [S19] (C) — a different measure from IC promotion velocity.

### KF3 — Tier multipliers, AI premium and the frontier-lab step (A / B / C)
- **US ladder (Levels.fyi 2025):** medians ≈ $155K (Entry) → $226K → $312K → $457K → $551K (Principal); steps ×1.46, ×1.38, ×1.46, ×1.21. Principal fell ≈ 6.6% YoY while Staff rose ≈ 7.5% [S2] (A).
- **AI premium over non-AI engineers rises with level:** 6.2% (Entry), 11.9% (Engineer), 14.2% (Senior), 18.7% (Staff) [S1] (A).
- **Frontier labs (small samples):** OpenAI L2 ≈ $249K → L3 $346K → L4 $769K → L5 $918K → L6 $1.28M → L7 $1.89M (largest step L3→L4, ×2.2) [S4]; Anthropic Entry $483K, Senior $621K, Lead $865K, Staff $1.41M (n = 49) [S3] (B). Snippets of the same OpenAI pages at different dates show L3 between ≈ $272K and ≈ $436K and L4 between ≈ $576K and ≈ $769K — treat frontier-lab medians as **±30–50%** (C).
- **Tier-jump multiples vs US all-company medians (headline):** Senior ×2.0 (Anthropic) to ×2.9 (OpenAI L5); Staff ×2.8 (OpenAI L6) to ×3.1 (Anthropic Staff). All-company medians understate Big-Tech baselines, so the true Big-Tech→lab multiple is lower (C).
- **After equity risk-adjustment** (equity RAV 0.5–0.9, §6.3) an OpenAI-L6-like package (base ≈ $404K + stock ≈ $786K/yr, older snapshot) is ≈ ×1.7–2.4 of the US all-company Staff median (C, derived).
- **Apex (T5):** reporting says Meta offered some AI researchers up to $300M over four years and >$100M in year one, in ≥10 cases; Meta disputes characterisations [S78, S79] (C; anonymous sourcing). Not visible in medians; Levels.fyi cannot resolve it.

### KF4 — India: the local ceiling is quantifiable (A)
- Levels.fyi Greater Bengaluru, Senior SWE (n = 4,836): median ≈ ₹56.0L; P25 ≈ ₹38.4L; P75 ≈ ₹79.9L; **P90 ≈ ₹1.07Cr**. Highest senior medians by employer: Broadcom ≈ ₹1.22Cr, LinkedIn ≈ ₹1.09Cr, Rippling ≈ ₹1.08Cr, Atlassian ≈ ₹1.06Cr, Rubrik ≈ ₹1.06Cr [S5].
- The brief's **T2 band (₹60L–1.2Cr)** runs from just above the local Senior median to above the 90th percentile; the **T3 floor (₹1.2Cr)** exceeds every top-employer *senior* median listed. A local Staff role typically does not reach ₹1.2Cr; Levels.fyi job-board estimates for Broadcom Staff roles in Bengaluru show base salary of only ≈ $39–77K [S7] (C).
- "AI Engineer" in Bengaluru: median ≈ ₹24.5L, P75 ≈ ₹40.4L, P90 ≈ ₹62.6L on the page as fetched [S6]; a search snapshot of the same URL showed ≈ ₹21.4L — small-sample instability (B).
- All-level SWE medians (Levels.fyi 2025): India ≈ $33.8K vs US ≈ $192.5K [S2] (A).

### KF5 — Europe (A / B / C / G)
- Levels.fyi 2025: Europe-wide SWE median ≈ $73.6K; Switzerland ≈ $148.3K [S2] (A). London Senior median ≈ £122–123K, P75 ≈ £170K, P90 ≈ £221–226K; London Entry ≈ £57–60K [S8] (C; snippet).
- UK EMI options: from 6 April 2026 the company limits rise to 500 employees, £120M gross assets and £6M unexercised-option cap, with option life up to 15 years [S68] (B) — materially better for UK AI start-ups than the prior regime.
- **No retrievable Europe-specific time-in-level or "plateau" data (G).** The plateau inference rests on level distributions (London Senior P90/median ≈ 1.8×) and the absolute pay gap — treat as D.

### KF6 — Preference overhang: not the norm, but a cliff (A)
- Cooley's Q2 2026 report (166 financings): **95.8%** carried a 1× liquidation preference and **96.4%** were non-participating; down rounds were **12.1%** [S26] (A; deals Cooley handled — under-represents bespoke mega-round structures, see §7). Carta's Q1 2026 report says preference and participation terms sit near multi-year lows and the down-round rate was 11.4% [S27] (A).
- Why overhang still matters: common is economically a **call option struck at the preference stack**. In my archetypes, common receives nothing when exit equity ≤ stack (13% of last mark for a lab-like company; 21% for a Series-C app company); the preference "tax" is material only in a band just above the stack (§6.3).
- Real 2026 cases: Airtable (peak ≈ $11–11.7B; raised > $1.4B; sold at ≈ $1.285B EV / ≈ $2.25B equity incl. cash) [S57, S58] (C); Forge counts Airtable −88% and Miro −92% versus last round; the ten highest-valued unmatched 2021–Q1 2022 rounds average −73% [S34] (A).

### KF7 — Secondary pricing is bimodal (A / B)
- Forge: the median trade was **−7%** vs last primary in July 2026 (par in June; ≈ −50% in late 2022–2023); P10 −57%, P25 −34%, P75 +7%, P90 +27% [S33]. For August trades: median −3%, P10 −87%, P25 −30%, P75 +11%, P90 +58% [S34] (A). Of 497 companies last priced in 2021/Q1 2022, 112 traded on Forge at an average −49% (median −61%) [S34] (A).
- Hot names: OpenAI's Forge Price implied ≈ $894B on 21 Sept 2026 vs the $852B August tender (≈ 5% below market) [S36, S40] (B). Anthropic's April 2026 tender priced at $350B pre-money while secondary indications were far higher and the May 2026 primary set $965B post-money — ≈ 2.5–2.8× the tender/Series-G price [S46, S48, S49] (B/C). **For top AI names the hidden cost is selling early at the tender price, not a discount.**
- Demand is thinning: buy-side indications of interest fell to 43.5% in September, a two-year low [S35] (A).

### KF8 — Tender offers 2025–26 (A / B)
- **Generic (Carta):** H1 2026 saw 71 tenders worth ≈ $3B (count +34%, value +200% YoY); Q2 median subscription 93.1%; median seller participation 57.9%; median discount 0% (P75 ≈ 10%); in the median tender over 3.5 years *no ex-employees were eligible*; median cap 20% of holdings (Q2 2025) [S28, S29] (A). A record 16,538 employees sold in Carta tenders in 2025 [S30] (A).
- **OpenAI:** Oct 2025 — $6.6B sold of ≈ $10.3B authorised at $500B; per-person cap raised from $10M to $30M; two-year holding requirement; ~75 sellers hit the cap [S38, S39] (B). Aug 2026 — ≈ $7B at $852B, company-funded; participation and caps undisclosed in what I retrieved (G) [S40, S41] (B).
- **Anthropic:** May 2025 buyback at $61.5B — up to 20% of holdings, $2M cap, ≥2 years' tenure [S50] (B). 2026 tender at $350B pre-money — ≥1 year tenure; investor demand of ≈ $5–6B exceeded what employees chose to sell [S48] (C).
- **Databricks:** employee liquidity is bundled into primary rounds (Series L, > $4B at $134B, Dec 2025) [S59] (A); a further $5B at $190B closed Aug 2026 [S60] (B). **Cohere:** an employee secondary sale in Oct 2025 [S61] (B).

### KF9 — IPO is not liquidity (B / C)
- OpenAI confidentially filed in mid-2026, but its CEO said in September it will not go public in 2026 [S42, S43] (B). Anthropic is reported to have filed confidentially in June 2026; reports of a public filing, roadshow and listing in Oct–Nov 2026 **conflict on timing** (pre-midterms vs pre-Thanksgiving) and I could not confirm a public S-1 [S51, S52] (C).
- **SpaceX (including xAI) is the live precedent:** IPO priced mid-June 2026 at $135, peaked at $225.64 on 16 June, traded below the IPO price by mid-July and was roughly 40–50% below peak in early August, under a **nine-stage lock-up with a price-triggered tranche** (455.8M shares unlock only above $175.50) [S53, S54] (B).
- Forge's Q4 2026 outlook says IPO momentum is fading; Databricks' CEO called 2026 a poor year to list, with ≈ $200B of listing capital already queued [S35, S60] (A/B).

### KF10 — Dilution arithmetic (A / B)
- New-money dilution = raise ÷ post-money. OpenAI Mar 2026 ($122B committed at $852B post-money; part of it contingent) ≈ **14.3%** as a ceiling [S82]; Anthropic Series H ($65B at $965B) ≈ **6.7%** [S46] (A); Databricks ≈ **3.7%** (Series L ≈ $5B/$134B) and **2.6%** ($5B/$190B) [S37, S59, S60].
- Carta medians for software rounds: Seed **19.5%**, A **18%**, B **14%**, C **10%**, D **7.5%** [S31] (A); founders + option pool hold ≈ 55% after seed, 36.6% after A, 23.5% after B, 17.5% after C, 10.9% after D [S32] (A).
- OpenAI's recapitalisation left the Foundation with ≈ 26%, Microsoft ≈ 27%, and employees plus other investors ≈ 47% [S44] (B).
- Anthropic illustration (E and F inputs are D-grade): valuation ×15.7 from $61.5B to $965B, while three later rounds diluted holders by ≈ 20% in aggregate → per-share price ×≈12.5 (§6.5).

### KF11 — Equity risk-discount model: what drives the haircut (C / D)
- Stylised RAV (expected value ÷ headline value, pre-tax, pre-vesting): lab-like **0.72** (0.48–0.89 for discount rate 25%→10%); Series-C app **0.70** (0.41–0.92); stale-vintage unicorn **0.24** (0.15–0.29); seed/A **1.18** (0.59–1.68, extremely assumption-sensitive).
- For the Series-C archetype: doubling bust probability cuts RAV by 28%; moving the discount rate 15%→25% cuts it by 41%; **structure traps cut it only 3–12%** (1.5× multiple −3%; uncapped participation −5%; senior claim equal to 20% of mark −12%).
- Expected vested fraction of a 4-year grant: **0.56** at 28% annual attrition, **0.71** at 17% [S18 for rates].

### KF12 — Hidden traps and the systems-expertise gap (A–D, G)
- **Verified:** 83(b) must be filed within 30 days of transfer with no extension, now e-fileable via an IRS online account, and does not cover RSUs [S62–S65] (A/B); OpenAI removed its vesting cliff for new hires (Dec 2025) [S45] (B); tender gates on tenure/caps/ex-employee exclusion [S28, S38, S50] (A/B); acqui-hire carve-outs: in the 2025 Windsurf deal, employees hired within the prior year reportedly received no payout while Cognition's buy of the remainder waived cliffs [S55, S56] (B); QSBS for stock issued after 4 July 2025: 50/75/100% exclusion at 3/4/5 years, $15M cap, $75M asset test [S66, S67] (B).
- **Recalled/unverified (D):** 90-day post-termination exercise default; ROFR/repurchase mechanics; single- vs double-trigger acceleration; clawback language.
- **Specialised systems expertise (training/inference/kernels):** only recruiter blogs and job postings (e.g. OpenAI GPU-infrastructure base ranges ≈ $230–490K in postings) [S80, S81] (C); **no controlled premium estimate found (G).**

---

## 4. Recommendation

*Decision rules derived from the findings above. They are conditional on the stated evidence grades and are not personalised advice.*

**R1 — Replace "hop every 18–24 months" with a four-way menu of moves, each with its own expected jump.**

| Move | Expected TC change | Basis | Grade |
|---|---|---|---|
| Stay, merit only | +3.4% a year (AI/ML ≈ +4.4%) | Pave H1 2026 [S14, S16] | B |
| Stay + promotion event | ≈ +16–24% TC at the event (base +6.5–8.6%, equity grant +39%) | Pave + derived [S14, S15, S17] | C |
| Same-tier lateral | ≈ **+15–25%** TC | ADP/Bidwell/coaching triangulation [S2, S11, S13] | C |
| Level-up lateral (e.g. Senior → Staff elsewhere) | ≈ **+35–50%** (level-median step ×1.38–1.46) | Levels.fyi medians [S2] | B/C |
| Tier jump (Big Tech → frontier lab) | headline ×1.6–2.9; ≈ ×1.7–2.4 after equity risk-adjustment vs *all-company* medians | [S3, S4] + model | C |

Annualised, a +15% / +20% / +25% hop every two years is ≈ 7% / 9.5% / 11.8% a year — about the same as a promotion-track stayer (≈ 9–12%). **A hop beats staying only when the premium exceeds roughly 25% or when promotion is blocked** (§6.2).

**R2 — Price the forfeited unvested equity before every hop.** Fraction of a new-hire grant vested if you leave at 18 / 24 / 36 months (computed from published schedule shapes [S9]):

| Schedule | 18 mo | 24 mo | 36 mo |
|---|---|---|---|
| Flat 25/25/25/25 (monthly, no cliff) | 37.5% | 50% | 75% |
| Amazon-style 5/15/40/40 | 12.5% | 20% | 60% |
| Google-style 33/33/22/12 | 49.5% | 66% | 88% |
| Google-style 38/32/20/10 | 54% | 70% | 90% |

Forfeited value = grant × (1 − vested). Ask for a sign-on bonus or equity at least that large. Under a 28% annual-attrition assumption the expected vested fraction of a 4-year grant is only ≈ 0.56 (0.71 at 17%) (§6.3).

**R3 — Discount private AI equity with a stage-specific haircut before comparing it to liquid RSUs.** Defaults from the model (pre-tax, pre-vesting, assumption-driven; use the band, not the point):

| Archetype | Base RAV | Sensitivity band | Default haircut band to use |
|---|---|---|---|
| Frontier-lab-like ($100B+ mark; tender/IPO path) | 0.72 | 0.48–0.89 (discount rate 25%→10%); 0.61–0.81 (bust ×2 → ×0.5) | **0.5–0.8** |
| Series C–D AI application company ($1–5B mark) | 0.70 | 0.41–0.92; 0.51–0.88 | **0.4–0.8** |
| Stale-vintage unicorn (last priced ≥ 2021, mark far above exit multiple) | 0.24 | 0.15–0.29 | **0.15–0.3** |
| Seed / Series A | 1.18 | 0.59–1.68 | Do not underwrite; treat as option value and ask for cash |

Healthy late-stage non-frontier names (Databricks-class) sit between the first two rows by interpolation (D). If you may not complete the vest, apply the expected vested fraction separately.

**R4 — Plan liquidity as three separate events, not one.** (i) A tender (needs tenure ≥ 1–2 years, caps of ~20% of holdings or a dollar limit, often no ex-employee eligibility); (ii) an IPO (then a lock-up, possibly staged and price-triggered); (iii) the sale itself. Assume **no cash for 12–24 months** unless a tender is scheduled and you are eligible. Treat post-IPO price swings of ±50% around the lock-up as plausible (SpaceX precedent). When a tender is priced far below secondary or the next primary (Anthropic 2026: 2.5–2.8×), selling in it crystallises that gap; weigh diversification and tax needs against it.

**R5 — Run an offer-letter diligence checklist (ask in writing).** Fully diluted share count (to convert shares → ownership %); last preferred price and last 409A value (common-vs-preferred gap); total preference stack, seniority and any participation/multiple/senior debt; last tender: date, price, cap, tenure gate, ex-employee eligibility, participation rate; vesting schedule and cliff; RSU vs option (strike, exercise cost, tax at exercise); post-termination exercise window (R: default is often 90 days — verify); acceleration on change of control; early-exercise and 83(b) availability; repurchase/ROFR rights; how recent hires were treated in prior acquisitions (Windsurf precedent).

**R6 — Persona rules.**
- **India-based Senior (T2) → T3 without relocating.** (1) First exhaust T2: the top-paying local employers cluster at senior medians of ≈ ₹1.06–1.22Cr [S5]. (2) For T3, the realistic routes are Staff scope at those employers (band not verified, G) or a US-band remote contract; prefer **cash-heavy** packages, because unlisted foreign shares are reported to be taxed as a perquisite at vest/exercise and again as capital gains on sale (24-month threshold for long-term, 12.5% rate), creating a cash crunch before liquidity [S71, S72] (C — confirm with a chartered accountant). (3) Relocation routes are in legal flux (see §6.8). (4) Training/inference-systems depth is a plausible differentiator but has no controlled premium estimate (G).
- **US Big-Tech Senior weighing a frontier lab.** Proceed if the *risk-adjusted* package still clears roughly ×1.5 of the Big-Tech offer, you can hold through a lock-up, and you have negotiated no cliff, tender eligibility and a sign-on that covers forfeited vest. Do not treat headline paper at a ~$1T mark as cash.
- **Europe-based Senior.** The binding constraints are the absolute pay ceiling and equity tax treatment, not promotion speed; UK EMI reform (from 6 Apr 2026) improves option economics; evidence for remote/US-band routes from Europe is thin (G).

**R7 — Re-run this note when any of these fire:** public S-1 for Anthropic or OpenAI (lock-up terms); Forge median trade ≤ −15% for two consecutive months or P25 ≤ −40%; buy-side IOI share < 40%; H-1B litigation outcomes; Levels.fyi's end-of-year 2026 report (December); Pave H2 2026 data; Cooley Q3 2026 terms.

---

## 5. Alternatives Considered

| Path | What the evidence says | Main failure mode | Wins when |
|---|---|---|---|
| **A. Stay + promote (liquid Big-Tech RSUs)** | Median stayer ≈ +5%/yr TC; promotion-track ≈ +9–12%/yr; fully liquid; community timelines suggest many stall at Senior (C/D) | Plateau at T2; slower than market; promotion budgets compressing in R&D (7.7% vs 9.9%) [S15] | You are on a promotion track and value liquidity |
| **B. Same-tier hops every 18–24 months** | ≈ +15–25% per hop → 7–12%/yr; external hires underperform early and exit sooner in the one rigorous study [S13] | Forfeited unvested equity; no promotion credit; attrition-driven resume risk | Blocked promotion, or ≥ 25% premium |
| **C. Level-up hop** | +35–50% plausible (level-median step ×1.38–1.46) | Interview bar; down-levelling; ~2–5-year cadence only | You are demonstrably at the next level |
| **D. Tier jump to a frontier lab** | Headline ×1.6–2.9; risk-adjusted ≈ ×1.7–2.4 vs all-company medians; AI/ML attrition ≈ 28% (B) | Paper-equity concentration; no/late liquidity; IPO and lock-up price risk; selection | You can absorb equity volatility and hold ≥ 3–4 years |
| **E. Series B–D AI start-up** | RAV ≈ 0.4–0.8; cash comp usually lower (D); tenders ≈ 71 per half-year on Carta, mostly Series C+ [S28] | Down round (≈ 11–12% of rounds), acqui-hire carve-outs, preference cliff in tails | Equity discounted to ≤ 0.5 still beats the alternative |
| **F. Founding/early employee (seed–A) with 83(b)/early exercise** | Power-law outcomes; RAV 0.6–1.7 and extremely assumption-sensitive; possible QSBS | 30-day 83(b) deadline; cash at risk; wipe-out probability high | Cash needs are covered and you can file correctly |
| **G. India-remote for a US employer** | Avoids relocation; local senior ceiling ≈ ₹1.07–1.22Cr; US senior median ≈ $312K | Location-based pay compression (no controlled data, G); Indian perquisite tax on private shares (C); contractor/EOR constraints | Cash-heavy offer; employer with listed stock |
| **H. Relocate to the US** | H-1B $100K-fee policy extended but blocked/struck down in court (Sept–Oct 2026); weighted lottery from Feb 2026 [S69, S70] | Legal flux; cost; timing | Employer will sponsor and absorb costs |

**Rejected as a default:** "hop every 18–24 months regardless." The compounding arithmetic shows it only beats staying when the premium is ≥ ~25% or promotion is blocked; the vest-schedule table shows it can forfeit 30–80% of a new-hire grant; and the only rigorous study of external hiring found early underperformance and higher exit [S13].

---

## 6. Detailed Findings

### 6.1 Progression velocity: benchmarks between tiers

| Transition | Benchmark (time in level / YOE) | Evidence | Grade | AI-specific data? |
|---|---|---|---|---|
| **T0 → T1** | ≈ 12–24 months in level (L3→L4 about 1–2 years) | Community/SEO level guides [S20, S22] | C/D | None (G) |
| **T1 → T2** | A further ≈ 2–4 years (L4→L5). Senior is reached at an **average of ~8.6 YOE** across all companies; Google/Apple ≈ 7–9; Netflix mostly 10+. Anthropic Senior: 6–8 YOE | Levels.fyi cofounder post [S10] (snippet); Levels.fyi Anthropic page [S3]; guides [S20, S21] | C / B | None (G) |
| **T2 → T3** | ≈ 3–5+ years; many never. One Blind thread reports ~3 years median among those who did get L5→L6 at Google, with many stuck 4+ years. Anthropic: Lead 7–8 YOE vs Senior 6–8 (very small n) | [S24] (D); [S3] (B) | D / B | None (G) |
| **T3 → T4** | Not published; assume ≥ 3–5 years | — | D | G |
| **T4 → T5** | Not a ladder — negotiated, individual packages | [S78] | C | G |
| *Population check* | Annual promotion rate **8.6%** (all levels, flat YoY) ⇒ naive mean wait 11.6 years, inflated by terminal levels | Pave [S16] (derived) | B → C | n/a |

Notes. (i) Meta's E5 is widely described as a practical terminal level and Google's L5 as the "career level" for many [S21, S23] (C). (ii) Levels.fyi's 8.6-year figure is *higher* than the "5–8 years to Senior" common in SEO guides, which suggests textbook timelines are optimistic for the median engineer (C). (iii) AI/ML engineers' promotion *raises* are near the bottom of R&D (6.5%) while their annual raises lead (4.4%) [S15] — retention is being delivered through merit and equity rather than promotion events (B). (iv) **DONE-criterion status:** benchmarks between all six tiers exist only as C/D ranges; an AI-vs-non-AI months-per-level series was not found.

### 6.2 Internal vs external: quantifying the gap

| Source | Scope | Measure | Value | Grade |
|---|---|---|---|---|
| ADP Pay Insights, Sept 2026 [S11] | US private-sector payroll | Changers vs stayers, YoY | base 4.8% vs 3.0%; gross 7.3% vs 4.4% | A |
| Atlanta Fed via Fortune [S12] | US workers | Median raise, switchers vs stayers | 4.8% vs 4.6% (early 2025) | B |
| Bidwell 2011 [S13, S83] | ~5,000 investment-bank employees | External-hire pay vs internal promotee | ≈ +18%; weaker early performance; higher exit | A (non-tech) |
| Pave H1 2026 [S14–S16] | Comp-platform customers | Merit / promotion / AI-ML | 3.4% median merit; promoted +8.6% (R&D 7.7%, AI/ML 6.5%); AI/ML non-promoted 4.4%; promotion rate 8.6% | B |
| Pave 2025 [S17] | 26K US employees with equity | Equity step at promotion | +39% median ongoing equity (vs +20% above-expectations, +16% meets); base +9.7% | B |
| Levels.fyi coaching [S2] | Coaching clients (self-selected) | Median comp improvement | +21% mid, +23% senior, +24% staff | B |
| Community threads (Blind/Reddit; individual threads not retained) | Anecdotal | Described lateral jumps | ~15–25% at the same level is the commonly described range; I found no verifiable source for 35–50% | D |

**Derived promotion TC step.** TC step ≈ (1 − s)·base_step + s·equity_step, with equity share of TC *s* = 30–50%, base_step 6.5–8.6%, equity_step 39%:

| Equity share *s* | base 6.5% | base 8.6% |
|---|---|---|
| 30% | 16.3% | 17.7% |
| 40% | 19.5% | 20.8% |
| 50% | 22.8% | 23.8% |

So **≈ 16–24% TC at a promotion** (C; assumes the 2025 equity step still holds in 2026).

**External-capture ceiling.** Level-median steps (×1.381 Engineer→Senior; ×1.465 Senior→Staff [S2]) minus the promotion TC step leave ≈ 14–22 pp (Engineer→Senior) and ≈ 22–30 pp (Senior→Staff). Cross-sectional medians mix companies and cohorts, so this is an upper-bound heuristic (C).

**Growth-rate comparison (TC CAGR; computed).**

| Strategy | Assumptions | TC CAGR |
|---|---|---|
| Median stayer | merit 3.4% + 8.6% promotion probability × ~20% step | ≈ 5% |
| Promotion-track stayer | promotion every 3 years, step 17–24%, merit 3.4–4.4% | ≈ 9.0–12.2% (every 2.5 years: 10.1–13.8%; every 4 years: 7.5–10.2%) |
| Hop every 2 years | +15% / +20% / +25% / +35% / +50% | 7.2% / 9.5% / 11.8% / 16.2% / 22.5% |
| Hop every 1.5 years | same premia | 9.8% / 12.9% / 16.0% / 22.1% / 31.0% |
| Levels.fyi ladder-implied (Entry → Senior ×2.0) | over 7 / 8.6 / 10 years | 10.5% / 8.5% / 7.2% |

**Reading the table.** A same-tier hop at +15–25% every two years roughly equals a promotion-track stayer (≈ 9–12%); hopping dominates only at premia ≥ ~25–35% or when promotion is blocked. A sustained 35–50% every 18–24 months implies 16–31% a year — about twice the ladder-implied growth — so it describes outliers, not the median (C, derived; individual trajectories are not observed here).

### 6.3 Equity valuation model (ERDM): discounting paper equity by stage and preference stack

**Purpose.** Convert a headline private-equity grant (valued at the last-round preferred price) into a *risk-adjusted* value comparable with a liquid public RSU of the same headline value. **All scenario probabilities and discount rates below are assumptions (Grade D)**; only the structure of the model and its sensitivities are meant to be reusable.

**Notation.** `V0` last post-money valuation; `P0` last preferred price per share (normalised to 1.00 so outputs are multiples of headline value); `N` shares in the grant; `G0 = N·P0` headline value. Preferred class *i* has invested capital `I_i`, liquidation multiple `ℓ_i` (preference `LP_i = ℓ_i·I_i`), as-converted units `n_i`, optional participation (cap `κ_i·I_i`), and seniority rank. `S` = senior claims (debt, compute-financing obligations) ranking ahead of all equity. `n_c` = common units (founders, employees, pool).

**Layer 1 — liquidation waterfall (per scenario).** Let `E` be exit equity value and `E_net = max(E − S, 0)`.
1. If `E_net ≤ ΣLP_i`: preferred are paid by seniority (equal rank = pari passu, pro rata to `LP_i`); **common receives 0**.
2. Otherwise find the common per-unit value `p` that solves `n_c·p + Σ payout_i(p) = E_net`, where a non-participating class takes `max(LP_i, n_i·p)` (take the preference or convert); a participating class takes `LP_i + n_i·p`, bounded by its cap unless converting is better. `p` is found by bisection.

*Insight.* For a single 1× non-participating class owning fraction φ of the fully diluted shares, common value per unit is 0 for `E ≤ L`, `(E − L)/n_c` for `L < E < L/φ`, and `E/FD` for `E ≥ L/φ`: **common is a call option struck at the preference stack** with a kink at `L/φ`. The "overhang" is therefore a cliff near `E ≈ L`, not a uniform tax. (This is the intuition behind option-pricing-method common-stock valuations used for 409A work — recalled, D.)

**Layer 2 — scenario expectation.**
`RAV = Σ_s p_s · e^(−r·T_s) · (1 − h_s) · c_s / P0`, with `c_s` the common per-unit value from Layer 1 at `E_s = m_s·V0`, `r` a private-equity discount rate that includes illiquidity (base 15%), `T_s` the time to liquidity, and `h_s` a post-IPO/lock-up haircut (10% in IPO scenarios, 0 otherwise). `RAV` is pre-tax and pre-vesting.

**Layer 3 — vesting/attrition.** With a 4-year even vest and constant annual attrition `a` (hazard `λ = −ln(1 − a)`), the expected vested fraction is `F_v = (1 − e^(−4λ)) / (4λ)`: **0.82 / 0.71 / 0.63 / 0.56 for a = 10% / 17% / 22% / 28%.** (Attrition inputs: ≈ 28% AI/ML vs ≈ 17% software engineers [S18].)

**Layer 4 — tax and exercise cost (not in the numbers).** RSUs: ordinary income at settlement; options: exercise cost `K` and possible AMT; early-exercise with 83(b) shifts gain to capital-gains treatment (§6.7). Apply after the pre-tax haircut.

#### Archetypes (stylised; **not** any real company's cap table)

| Archetype | Mark `V0` | Preferred (units; invested) | Stack as % of `V0` | Common units |
|---|---|---|---|---|
| **L** frontier-lab-like | $900B | one 1× non-participating class: 630 units (70%); $120B | 13.3% | 270 |
| **M** Series-C AI application company | $3,000M | A: 600 u/$40M; B: 600 u/$200M; C: 400 u/$400M; standard seniority C > B > A | 21.3% | 1,400 |
| **Z** stale-vintage unicorn (Airtable-*shaped*) | $11,000M | one class: 6,600 units (60%); $1,400M | 12.7% | 4,400 |
| **S** seed/Series-A AI start-up | $60M | Seed 6 u/$3M; A 15 u/$15M (A senior) | 30.0% | 39 |

Scenario sets (`m` = exit equity ÷ `V0`; `T` years; probability) — **assumptions chosen to be loosely consistent with the evidence ranges** (Forge percentiles, Airtable/Miro cases, Cooley/Carta terms):

| Archetype | Scenarios (m / T / p) |
|---|---|
| L | bust/forced sale 0.25/4/0.10 · derating 0.60/5/0.20 · flat IPO 1.0/3/0.30 · growth IPO 2.0/4/0.28 · breakout IPO 4.0/5/0.12 |
| M | shutdown/acqui-hire 0.10/3/0.25 · soft-landing M&A 0.40/4/0.20 · flat 1.0/5/0.25 · growth 3.0/5/0.20 · breakout 8.0/6/0.10 |
| Z | fire sale 0.10/3/0.20 · deep reset 0.25/3/0.35 · moderate reset 0.50/4/0.25 · back to mark 1.0/5/0.15 · 2× 2.0/6/0.05 |
| S | wipeout 0/2/0.40 · acqui-hire 0.30/3/0.20 · flat 1.0/5/0.12 · 4× 4/6/0.15 · 15× 15/7/0.10 · 50× 50/8/0.03 |

#### Results

**(a) Waterfall — common value per unit (last-round price = 1.00), Archetype M.**

| `m = E/V0` | pro-rata (no pref) | plain 1× non-part. | Series C 1× participating, 3× cap | Series C 1.5× | plain + $300M senior claim |
|---|---|---|---|---|---|
| 0.20 | 0.20 | **0.000** | 0.000 | 0.000 | 0.000 |
| 0.25 | 0.25 | 0.075 | 0.061 | 0.000 | 0.000 |
| 0.40 | 0.40 | 0.300 | 0.250 | 0.200 | 0.150 |
| 0.50 | 0.50 | 0.423 | 0.367 | 0.346 | 0.300 |
| 0.75 | 0.75 | 0.712 | 0.617 | 0.635 | 0.596 |
| 1.00 | 1.00 | 1.000 | 0.867 | 0.923 | 0.885 |
| 2.00 | 2.00 | 2.000 | 1.867 | 2.000 | 1.900 |
| 3.00 | 3.00 | 3.000 | 3.000 | 3.000 | 2.900 |
| 10.00 | 10.00 | 10.000 | 10.000 | 10.000 | 9.900 |

Reading: with plain terms the preference matters only below `m ≈ 1.0` (Series C's conversion point); common is wiped out below `m ≈ 0.21`. A participating class keeps taking value until `m ≈ 3`. A **senior claim is a flat tax at every exit size** (here $300M ≈ 10% of `V0` ⇒ −0.10 per unit even at `m = 10`).

**(b) Archetype L.** Common receives nothing for `E ≤ $120B` (13.3% of the mark); at `m = 0.15` it receives 0.056 (a 63% shortfall vs pro rata); from `m ≥ 0.20` (an 80% drawdown) there is **no preference shortfall**. For a lab-like company the stack is irrelevant unless the mark falls by ~80%+.

**(c) Archetype Z (Airtable-shaped; illustrative only).** Exit equity $2.25B vs a $11B mark: pro-rata common value 0.205 vs waterfall 0.193 — the preference costs common only ≈ 5.6%; the **mark-down (≈ −80%) is the loss, not the stack**. At `E = $1.8B` the shortfall is 44%; at `E ≤ $1.4B` common gets nothing.

**(d) Risk-adjusted value (RAV) — base and sensitivities.**

| Archetype | E[m] | Base RAV | r = 10% | r = 25% | bust ×2 | bust ×0.5 | no IPO haircut |
|---|---|---|---|---|---|---|---|
| L | 1.49 | **0.72** | 0.89 | 0.48 | 0.61 | 0.81 | 0.80 |
| M | 1.76 | **0.70** | 0.92 | 0.41 | 0.51 | 0.88 | 0.76 |
| Z | 0.48 | **0.24** | 0.29 | 0.15 | 0.20 | 0.29 | 0.24 |
| S | 3.78 | **1.18** | 1.68 | 0.59 | 0.74 | 1.69 | 1.28 |

**(e) Structure traps on Archetype M (RAV, base scenarios).** Plain 1×: 0.699 · Series C 1.5×: 0.679 (−2.9%) · Series C 1× participating, 3× cap: 0.678 (−3.0%) · uncapped participation: 0.661 (−5.4%) · $300M senior claim (10% of mark): 0.657 (−6.0%) · $600M senior claim (20%): 0.614 (−12.2%).

**(f) Break-even.** For Archetype M, the probability of a ≥ 3× outcome needed for RAV = 0.50 / 0.60 / 0.75 / 0.90 is ≈ **0.18 / 0.24 / 0.33 / 0.42** (base assumption 0.30).

**(g) What the model says (robust to the assumptions).**
1. **Discount rate and the probability of sub-mark outcomes dominate** (−41% and −28% in Archetype M); **preference structure is second-order for healthy marks** (−3% to −12%) and first-order only when exit value is near the stack.
2. The brief's "severe overhang" is real in two places: (i) **stale-vintage names** (Z: RAV ≈ 0.24, driven mainly by the mark-down) and (ii) **bespoke structures** — senior claims scale with the mark and bite at every outcome.
3. For the lab-like archetype, RAV reaches 1.0 only if the expected exit multiple is ≈ 2.05× the current mark (base set: 1.49×); at RAV 0.5–0.8, treat headline paper as 50–80 cents of liquid RSU per dollar, before vesting and tax.

#### Reference implementation (reproduces every number in this section)

```python
import math

def waterfall(E, classes, n_common, senior=0.0):
    """classes: dicts(name, units, invest, lp_mult=1, participating=False, cap_mult=None, rank=1);
    rank 1 = most senior; equal rank = pari passu. Returns (common_value_per_unit, payouts)."""
    E_net = max(E - senior, 0.0)
    lp = {c['name']: c.get('lp_mult', 1.0) * c['invest'] for c in classes}
    pay = {c['name']: 0.0 for c in classes}
    if E_net <= sum(lp.values()):                      # preferences not covered -> common = 0
        remaining = E_net
        for r in sorted({c.get('rank', 1) for c in classes}):
            grp = [c for c in classes if c.get('rank', 1) == r]
            need = sum(lp[c['name']] for c in grp)
            x = min(remaining, need)
            for c in grp:
                pay[c['name']] = x * lp[c['name']] / need if need else 0.0
            remaining -= x
            if remaining <= 1e-12:
                break
        return 0.0, pay
    def class_payout(c, p):
        L, n = lp[c['name']], c['units']
        if not c.get('participating', False):
            return max(L, n * p)                       # take preference or convert
        part = L + n * p                               # preference + participation
        if c.get('cap_mult') is not None:
            part = max(min(part, c['cap_mult'] * c['invest']), n * p)
        return part
    total = lambda p: n_common * p + sum(class_payout(c, p) for c in classes)
    lo, hi = 0.0, E_net / n_common
    for _ in range(200):                               # bisection on common per-unit value
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if total(mid) > E_net else (mid, hi)
    p = (lo + hi) / 2
    return p, {c['name']: class_payout(c, p) for c in classes}

def expected_vested_fraction(a, years=4.0):            # constant hazard, even vesting
    lam = -math.log(1 - a)
    return (1 - math.exp(-lam * years)) / (lam * years)

def rav(scenarios, V0, classes, n_common, senior=0.0, r=0.15, ipo_haircut=0.10):
    """scenarios: (label, m=E/V0, T_years, prob, is_ipo). Returns EV as a multiple of headline value."""
    return sum(p * math.exp(-r * T) * (1 - (ipo_haircut if ipo else 0.0))
               * waterfall(m * V0, classes, n_common, senior)[0]
               for _, m, T, p, ipo in scenarios)
```

### 6.4 Private AI scale-ups: liquidity ledger (2025–Oct 2026)

| Company | Latest primary mark | Employee-liquidity events | Terms observed | Secondary / market indicator | Other relevant facts |
|---|---|---|---|---|---|
| **OpenAI** | ≈ $852B post-money (closed 31 Mar 2026; $122B committed, part contingent) [S82] (B) | Oct 2025 tender: $6.6B sold of ≈ $10.3B authorised at $500B; Aug 2026: ≈ $7B at $852B, company-funded [S38–S41] (B) | Cap raised from $10M to $30M; ≥ 2-year holding; ~75 sellers hit the cap; Aug 2026 participation/caps undisclosed (G) | Forge Price ≈ $894B on 21 Sept 2026 [S36] (B) | Recapitalisation (Oct 2025): Foundation ≈ 26%, Microsoft ≈ 27%, employees + other investors ≈ 47% [S44]; vesting cliff removed Dec 2025 [S45]; CEO: no IPO in 2026 [S42, S43] |
| **Anthropic** | $965B post-money (Series H, $65B, May 2026) [S46, S47] (A/B); Series G ≈ $380B (Feb 2026) [S47] | May 2025 buyback at $61.5B; 2026 tender at $350B pre-money [S48, S50] (B/C) | 2025: ≤ 20% of holdings, $2M cap, ≥ 2 years' tenure; 2026: ≥ 1 year tenure, investor demand ≈ $5–6B above what employees sold | Secondary indications far above the tender price [S49] (C) | Confidential filing reported June 2026; public-filing/roadshow timing reports conflict [S51, S52] (C) |
| **Databricks** | $190B (Aug 2026; $5B raise) [S60] (B) | Liquidity bundled into primary rounds (Series L, > $4B at $134B, Dec 2025; ≈ $5B equity after Feb 2026 follow-on) [S59, S37] (A/B) | Caps/tenure not disclosed (G) | Forge Price ≈ $242 (≈ $170.7B) in June 2026 [S37] (B) | CEO calls 2026 a poor IPO year [S60] |
| **Cohere** | Reported ≈ US$7B around its Oct 2025 employee sale [S61] (B) | Oct 2025 employee secondary [S61] | Not retrieved (G) | n/a | — |
| **SpaceX incl. xAI (public)** | IPO mid-June 2026 at $135 [S53, S54] (B) | Staged nine-stage lock-up; 455.8M-share tranche unlocks only above $175.50 | Price-triggered release | ≈ 40–50% below peak by early Aug [S53, S54] | Shows IPO ≠ liquid, de-risked equity |
| **Typical Carta tender (H1 2026)** | n/a | 71 tenders, ≈ $3B; ~70% at Series C+ [S28] (A) | Median cap 20% (Q2 2025); median subscription 93.1%; seller participation 57.9%; median discount 0%; no ex-employees in median tender [S28, S29] | Forge median trade −3% to −7% [S33, S34] (A) | 16,538 employees sold in 2025 [S30] |

**How to read it.** (1) Dollar caps at labs ($30M; $2M in 2025) are rarely binding for engineers below the apex; the binding constraints are **tenure gates, the company's choice of timing and price, and eligibility of ex-employees**. (2) Issuer discretion is structural: Morgan Stanley's announcement describes an issuer-centred model in which companies keep discretion over when and how their shares trade [S75] (B; announcement snippet). (3) Tender price discipline matters: when the tender prices off the last primary and the next primary reprices 2.5× (Anthropic 2026), sellers lock in the old price.

### 6.5 Dilution models

**Formulas.** New-money dilution `d_k = R_k / V_post,k`. Cumulative ownership factor `Π(1 − d_k)`. Price-per-share ratio between rounds `j → k`: `(V_k / V_j) · Π_{i=j+1..k}(1 − d_i)` (all share growth assumed to come from new-money issuance; option-pool top-ups add further dilution). An employee's *share count* is unchanged by a round; the *percentage* falls by `d_k`, while the *value* moves with price.

| Round | Raise | Post-money | New-money dilution | Source / grade |
|---|---|---|---|---|
| OpenAI, Mar 2026 | $122B committed (part contingent) | $852B | **14.3%** (ceiling; funded share is lower) | [S82] B |
| Anthropic Series E, Mar 2025 | $3.5B (recalled) | $61.5B | 5.7% | valuation [S50] B; raise (R) D |
| Anthropic Series F, Sep 2025 | $13B (recalled) | $183B | 7.1% | (R) D |
| Anthropic Series G, Feb 2026 | $30B | $380B | 7.9% | [S47] B |
| Anthropic Series H, May 2026 | $65B | $965B | **6.7%** | [S46] A |
| Databricks Series L (equity ≈ $5B after follow-on) | ≈ $5B | $134B | 3.7% | [S59, S37] A/B |
| Databricks, Aug 2026 | $5B | $190B | **2.6%** | [S60] B |
| Carta median path, seed → C (software) | — | — | 19.5% → 18% → 14% → 10% = **48.9% cumulative** | [S31] A |

**Anthropic illustration (E and F inputs are D-grade).** Valuation ×15.7 ($61.5B → $965B); three later rounds (F, G, H) diluted holders by ≈ 20.2% in aggregate; implied per-share price ≈ ×12.5. From F to H: valuation ×5.3; dilution from G and H ≈ 14.1%; price ≈ ×4.5. **Dilution is second-order while marks rise; it becomes first-order in down rounds**, where anti-dilution terms can shift value from common to preferred (broad-based weighted-average vs full-ratchet adjustment — recalled, D) and where the preference stack grows relative to equity value.

**Carta ownership context.** Founders plus option pool hold ≈ 55.1% after seed, 36.6% after A, 23.5% after B, 17.5% after C, 10.9% after D [S32] — a late joiner's pool slice is a small fraction of that common block.

### 6.6 Hidden-trap register for AI start-up offers

| # | Trap | Mechanism | Evidence | Status | What to ask / do |
|---|---|---|---|---|---|
| 1 | Tender tenure gate | Cannot sell until 1–2 years' tenure | OpenAI ≥ 2 yrs; Anthropic ≥ 2 yrs (2025), ≥ 1 yr (2026) [S38, S48, S50] | Verified (B) | Negotiate eligibility from day 1 or a first-tender guarantee |
| 2 | Percentage/dollar cap | ≈ 20% of holdings (median) or $2M–$30M | [S29, S38, S50] | Verified (A/B) | Ask for last three tenders' caps and fill rates |
| 3 | Ex-employee exclusion | Leavers cannot sell in the median tender | [S28] | Verified (A) | Ask for post-departure eligibility and exercise terms |
| 4 | Vest shape / cliff | Back-loaded schedules forfeit most of a grant at a 24-month hop | [S9, S45] | Verified (B) | See §4 R2 |
| 5 | Acqui-hire carve-out | Recent hires receive nothing in licence-and-hire deals | Windsurf, 2025 [S55, S56] | Verified (B) | Seek acceleration/protection language |
| 6 | Preference cliff | Common = 0 when exit ≤ stack | Model §6.3; terms [S26] | Verified as mechanism (A/C) | Ask total stack, seniority, last 409A |
| 7 | Participation / > 1× / senior debt | Takes value at every exit size | 3.6% of Q2-2026 deals participating; 4.2% not at 1× [S26] | Rare (A); bespoke mega-round terms unobserved (G) | Request the term summary |
| 8 | Tender priced below market | Seller locks in old price | Anthropic 2026 [S48, S49] | Reported (C) | Sell only what you need; compare with secondary |
| 9 | Issuer control of secondary trading | Company approves timing/price | [S75] | Reported (B) | Ask about ROFR and transfer approvals |
| 10 | Lock-up and price triggers | IPO shares locked in stages; some tranches only unlock above a price | SpaceX [S53, S54] | Verified (B) | Ask for lock-up and early-release terms when filed |
| 11 | 83(b) 30-day cliff | Missed deadline = default taxation at vest | [S62–S65] | Verified (A/B) | Calendar day 30 from the transfer date |
| 12 | Post-termination exercise window | Options may expire ~90 days after leaving | (R) | Unverified (D) | Ask for the window; seek extension |
| 13 | RSU tax before liquidity | Tax at settlement on unlisted stock | (R) | Unverified (D) | Ask whether RSUs are double-trigger |
| 14 | India perquisite-tax cash crunch | Tax at vest/exercise on unlisted foreign shares, then capital gains | [S71, S72] | Reported (C) | Prefer cash-heavy pay; plan funding |
| 15 | Non-disparagement / clawback language | Vested equity put at risk by exit terms | (R: a 2024 controversy) | Unverified (D) | Read exit agreements |

### 6.7 Tax and election mechanics (summaries; confirm with a professional)

**US §83(b) election.** The election must be filed no later than 30 days after the transfer of the restricted property; the deadline cannot be extended, and revocation requires IRS consent (IRC §83(b)(2); Treas. Reg. §1.83-2(b); Form 15620 instructions) [S62] (A). The IRS form is Form 15620 (Rev. 10-2024) [S62]; since mid-2025 it can also be filed online through an IRS online account (ID.me) per several law-firm alerts; file one way only, keep proof, and give the employer a copy [S63–S65] (B). It applies to restricted stock and early-exercised options, **not RSUs** (R, D).

*Illustration (assumptions: 100,000 shares bought at FMV $0.50 = $50K; 25,000 vest each year at FMV $1.50 / $4 / $9 / $20; all sold at $20; illustrative top federal rates 37% ordinary and 23.8% long-term incl. NIIT (R); state tax ignored):* without an election, ordinary income at vest ≈ $812.5K and later capital gain ≈ $1,137.5K ⇒ tax ≈ $571K; with an election at FMV (zero income at grant) the whole $1.95M gain is long-term ⇒ tax ≈ $464K; saving ≈ $107K. If the company fails, the cost is the $50K purchase price (a capital loss) and no tax is paid either way. Where shares are *granted* (not purchased) with FMV above zero, the election creates income at grant that is not recovered if the shares are forfeited (R).

**QSBS (§1202), stock issued after 4 July 2025.** Exclusion of 50% / 75% / 100% of gain after 3 / 4 / 5 years; per-issuer cap $15M; issuer gross-assets threshold $75M [S66, S67] (B). Relevant to genuinely early-stage grants; mega-cap AI labs exceed the asset test.

**UK EMI (from 6 April 2026).** Up to 500 employees; £120M gross assets; £6M company-wide unexercised-option limit; option life up to 15 years [S68] (B).

**India (foreign RSUs/ESOPs; advisory-blog level).** Perquisite taxed as salary at vest/exercise on the FMV of unlisted foreign shares; capital gains on sale, long-term after 24 months at 12.5% (no indexation); Schedule FA disclosure and Form 67 for foreign tax credit; remittance limits under the LRS for exercise costs [S71, S72] (C).

### 6.8 Plateau traps and how to unblock them

| Plateau | Where it bites | Evidence | Unblockers (grade) |
|---|---|---|---|
| **P1. US Senior (T2) plateau** | L5/E5-type levels | Many reported stuck 4+ years at Google L5 (D) [S24]; Meta E5 a practical terminal level for many (C) [S23]; Senior→Staff median step ×1.46 [S2]; in 2025 Staff medians rose ≈ 7.5% while Principal fell ≈ 6.6% [S2] | (i) Level-up lateral (+35–50%, C); (ii) AI specialisation — premium is larger at Staff (18.7%) than Senior (14.2%) [S1] (A); (iii) tier jump to a frontier lab (risk-adjusted ≈ ×1.7–2.4, C); (iv) documented cross-team scope for Staff promotion (D) |
| **P2. AI/ML promotion compression** | Any level in R&D | AI/ML promoted raise 6.5% vs 8.6% all functions; R&D promoted raise fell 9.9% → 7.7% (2025 → H1 2026) [S15] | Pull value through annual raises and equity; negotiate refresh cadence (promoted employees get ≈ +39% ongoing equity) [S17] (B) |
| **P3. India local ceiling (T2 → T3)** | Bengaluru Senior P90 ≈ ₹1.07Cr; top-employer senior medians ≈ ₹1.06–1.22Cr [S5] | Levels.fyi (A) | (a) Move into the top-paying employer cluster (A); (b) Staff scope at those employers — band not verified (G); (c) US-band remote role, cash-heavy — pay-band compression unquantified (G); (d) AI employers hiring in India — not verified (G); (e) relocation — volatile (below); (f) note the local escalator: India's median non-promoted raise was 9.9% vs ≈ 3.4% in the US [S16] (B), which erodes the gap slowly for those who stay |
| **P4. Europe pay ceiling** | London Senior median ≈ £122K, P90 ≈ £221K [S8]; Europe-wide median ≈ $73.6K vs US ≈ $192.5K [S2] | A / C | US-band remote or Swiss employers (Swiss median ≈ 2× Europe) (C, thin); EMI-eligible start-ups [S68] (B) |
| **P5. Golden handcuffs** | Unvested paper at a lab or start-up | §4 R2 table; §6.3 `F_v` | Sign-on covering forfeited vest; early tender eligibility; early exercise where cash risk is acceptable |
| **P6. Equity-rich, cash-poor** | Pre-IPO lab employees | Tender gates; staged lock-ups [S53, S54] | Plan 12–24 months without liquidity; fund taxes separately |

**Relocation route (US) — volatile as of Oct 2026 (B).** Yale's international-office summary reports that the $100,000 H-1B fee proclamation (Sept 2025) was extended for a further year while the fee remains blocked by a court order, and Forbes reported on 1 Oct 2026 that another judge struck down the latest version [S69, S70]. Reports also describe a wage-weighted selection rule for the cap lottery (higher wage levels receive more entries) and a proposed rule to codify a similar fee. Treat all of this as unsettled and re-check before planning.

### 6.9 Negotiation levers, codified

| # | Lever | Mechanism | Evidence | Expected effect | Grade |
|---|---|---|---|---|---|
| 1 | Parallel offers and timing | Create competing processes at the same level | Levels.fyi coaching cohort +21% / +23% / +24% (mid/senior/staff) [S2] | ≈ +20% (selection-biased) | B |
| 2 | Negotiate **level**, not just comp | Level-median step ×1.38–1.46 per level | [S2] | up to +38–46% | B/C |
| 3 | Sign-on = forfeited unvested | Use §4 R2 table | Computed from schedule shapes [S9] | Recovers 30–80% of a new-hire grant | C |
| 4 | Vest shape / cliff | Ask for no cliff or front-loading | OpenAI removed its cliff [S45]; Google-style vs Amazon-style [S9] | At 24 months: 66% vs 20% vested | B/C |
| 5 | Cash vs paper at risk-adjusted parity | Swap $1 of paper for RAV dollars of cash | Model §6.3 | $100K lab paper ≈ $50–80K liquid | C/D |
| 6 | Tender eligibility / first-sale rights | Ask for eligibility from day 1 or a guaranteed first tender | Tenure gates [S28, S38, S50] | Converts paper to cash 1–2 years earlier | B |
| 7 | Promotion / refresh commitments | Target-level date; refresh cadence | Pave: ≈ +39% ongoing equity at promotion [S17] | Larger post-promotion equity | B |
| 8 | Exercise terms | Early exercise + 83(b); longer exercise window | [S62–S65] (83(b)); window (R) | Tax-timing benefit; avoids expiry | B / D |
| 9 | Information rights | Fully diluted count, stack, last 409A, tender history | Enables the model | Makes RAV computable | D |
| 10 | M&A protections | Double-trigger acceleration; no recent-hire carve-out | Windsurf [S55, S56] | Protects against acqui-hire loss | B/D |
| 11 | India pay structure | Cash-heavy; plan perquisite tax; ask which pay band applies to remote roles | [S5, S71, S72] | Avoids dry tax; clarifies ceiling | C/G |
| 12 | Signal systems depth | Verifiable training/inference/kernel work | Recruiter/job-post evidence only [S80, S81] | Unquantified | G |

### 6.10 Tool catalog (secondary marketplaces, valuation aggregators, cap-table modelling)

| Tool | Category | What it gives you | Evidence status |
|---|---|---|---|
| **Forge Global** | Secondary marketplace + data | Forge Price (indicative price for ~200 pre-IPO companies), Forge Private Market Index, monthly "Private Market Update", liquidity programs for tenders | Verified [S33–S37]. Schwab agreed in Nov 2025 to acquire it for ≈ $660M; closing not verified [S74] |
| **Carta** | Cap table, 409A, tender administration, benchmarking | State of Private Markets and tender-offer datasets; Total Compensation benchmarks; QSBS tooling | Verified [S27, S28, S31]. Lists AngelList as a competitor on its site (not independently verified) |
| **EquityZen** | Secondary marketplace | Employee/investor secondary access | Morgan Stanley agreed to acquire it on 29 Oct 2025 (> 800K registered users; > 450 companies) [S75] (A) |
| **Hiive / Augment / Caplight / Nasdaq Private Market** | Marketplaces and pricing | Secondary quotes, tender administration (NPM), pricing + cap-table analytics (Caplight), market commentary (Augment) | Augment and Caplight/NPM pages seen [S49, S76] (C); Hiive named only in aggregator content (D) |
| **PitchBook** | Valuation / VC data | Private-company valuations and deal data | Vendor page only [S77] (C) |
| **AngelList** | Cap table / fund administration | — | Seen only as a competitor reference on Carta's site (D) |
| **Capbase – Startup Exit Calculator** | Waterfall / dilution modelling | Free tool (launched Apr 2026) modelling liquidation preferences, participation and dilution | [S73] (C) |
| **Levels.fyi** | Comp benchmarking, coaching | Level/company/location medians; negotiation coaching | [S1–S6] (A/B) |
| **Pave** | Comp-planning data | Merit, promotion, AI/ML raise benchmarks | [S14–S18] (B) |
| **ERDM (this note)** | Equity risk-discount model | Reproducible waterfall + scenario valuation (§6.3) | Self-contained; assumptions are D |

*Pulley, Ledgy and Cake Equity were not independently verified in this session and are omitted from the evidence-backed list.*

### 6.11 Falsification log and search record

**Searched and not found (G).**
- AI-vs-non-AI months-per-level or time-in-level data (Levels.fyi, Pave, SignalFire, community/SEO).
- A published source for the "35–50% per hop" statistic; the nearest items are coaching medians and anecdotes.
- A tech-specific job-changer vs stayer pay study (only economy-wide ADP/Atlanta Fed and a non-tech academic study).
- Evidence of participating/senior preferences in AI mega-rounds (terms are undisclosed).
- OpenAI's Aug 2026 tender caps and participation; Databricks/Cohere tender caps and tenure.
- Levels.fyi Staff-level TC for Bengaluru (only job-board base estimates); Europe time-in-level or plateau data; pay-band compression for India-based remote hires; a controlled systems-expertise premium; frontier-lab promotion timelines; a public Anthropic S-1 (none found as of the last sources checked).

**Failure modes found (falsification attempts that succeeded).** Windsurf (2025): recent hires reportedly paid nothing in a licence-and-hire deal [S55]. Airtable (−88% EV vs peak) and Miro (−92%); 2021-vintage cohort at median −61% [S34]. SpaceX post-IPO drawdown under a staged lock-up [S53, S54]. Anthropic's 2026 tender priced far below secondary indications [S48, S49]. OpenAI deferring its IPO [S42]. Buy-side IOIs at a two-year low [S35].

**Data-quality notes.** (1) Levels.fyi OpenAI level medians differ by 30–60% between dated snapshots; Anthropic's page has n = 49. (2) The Bengaluru "AI Engineer" median read ≈ ₹21.4L in a search snapshot and ≈ ₹24.5L on the fetched page. (3) Conflicting claims about whether 83(b) can be e-filed: the printed form says mail; law-firm alerts say online filing is available since mid-2025 — resolved toward the law-firm alerts, but confirm on IRS.gov. (4) Anthropic IPO timing reports conflict. (5) Airtable's peak valuation is quoted as ≈ $11B to $11.7B. (6) Two unrelated "19%" figures appear in the sources — Pave's AI/ML raise (4.4% vs 3.7% R&D = 19% higher) and Levels.fyi's Staff AI premium (18.7%) — and must not be conflated.

---

## 7. Open Questions & Risks

### 7.1 Open questions (what would resolve each)

1. **AI vs non-AI months-per-level** — needs time-in-level data split by specialisation (Levels.fyi, Pave or payroll-linked sources). Without it, T0→T5 timelines remain C/D ranges.
2. **Frontier-lab leveling and equity terms** — level mapping to Big Tech, RSU vesting/cliff, exercise or settlement mechanics, acceleration, and post-termination terms (offer letters, not public pages).
3. **OpenAI's Aug 2026 tender** — eligibility, caps and participation were not in the sources I could retrieve.
4. **Anthropic's IPO** — whether a public S-1 is filed, lock-up length and early-release triggers; timing reports conflict.
5. **India Staff-level TC and remote pay bands** — Levels.fyi Staff-level Greater Bengaluru data and any controlled evidence on location-based compression for India-based remote hires.
6. **Europe time-in-level / plateau evidence** — only distributional proxies were found.
7. **Preference stacks and senior claims in AI mega-rounds** — compute-for-equity, strategic-investor and debt structures are largely undisclosed.
8. **Systems-expertise premium (training, inference, kernels)** — needs a controlled title/skill comparison; recruiter blogs and postings are not evidence of a causal premium.
9. **Post-IPO behaviour of AI listings** — one detailed precedent (SpaceX incl. xAI); too thin to generalise.
10. **Employees' true cap-table share at the labs** — OpenAI's 47% figure bundles employees with other investors.

### 7.2 Risks to the recommendations

- **Valuation-regime risk.** Marks near $1T leave little room for multiple expansion; secondary demand is thinning (buy-side IOIs 43.5%, a two-year low) [S35]. A regime change moves headline paper far more than preference mechanics do (KF11).
- **Concentration risk.** Salary, unvested equity and career capital sit with one employer; AI/ML attrition (~28%) means many will not complete a 4-year vest (F_v ≈ 0.56).
- **Liquidity-timing risk.** Tenders are discretionary; IPOs can be deferred (OpenAI) or re-timed (Anthropic reports); lock-ups can be staged and price-triggered (SpaceX).
- **Legal and tax flux.** H-1B fee litigation and rules; QSBS/EMI changes; India perquisite-tax treatment of unlisted foreign shares.
- **Data-quality risk.** Self-reported compensation, small frontier-lab samples (n = 49) and snapshot volatility (±30–60%).
- **Model risk.** Scenario probabilities and discount rates are assumptions (D); stylised archetypes are not real cap tables.
- **Staleness risk.** This note is dated 23 Oct 2026; IPO filings, tender announcements or court rulings may land within weeks and would change KF7–KF9.
- **Conflict-of-interest risk.** The author is an AI model from a company analysed here; mitigated by external sourcing and grading, not eliminated.

### 7.3 Strongest objections an expert would raise — and what the evidence says

| # | Objection | Evidence for the objection | Evidence against | Net |
|---|---|---|---|---|
| O1 | "Levels.fyi is self-reported and skews to high payers; frontier-lab medians (n = 49) are unreliable." | n = 49 for Anthropic [S3]; OpenAI L3/L4 read ≈ $272K–$436K / $576K–$769K across snapshots [S4 + snippets] | Large samples elsewhere (Bengaluru Senior n = 4,836 [S5]); Pave payroll-linked data agree on direction [S14–S16] | Use ratios and ranges; treat lab levels as ±30–50% |
| O2 | "ADP/Atlanta Fed are economy-wide; the AI hop premium could be far larger." | True; I found no tech-specific rigorous study; AI/ML attrition ≈ 28% suggests an active market [S18] | Coaching medians +21–24% [S2]; compounding test (35–50% every 2 years ⇒ 16–22% a year vs ≈ 8.5% ladder-implied); Pave shows AI/ML rewarded via raises, not promotion jumps [S15] | 35–50% plausible for tier-crossers; unproven for the median |
| O3 | "Scenario probabilities are arbitrary — RAV is false precision." | Agreed (D); the seed/A archetype swings 0.59–1.68 | Sensitivities and break-evens reported; shape anchored to Forge percentiles, the 2021-vintage cohort and Cooley terms [S26, S33, S34] | Use bands; trust ranking and sensitivity structure |
| O4 | "Cooley/Carta terms under-represent bespoke AI mega-round structures." | Valid — such terms are undisclosed (G); Cooley covers deals it handled [S26] | Senior-claim sensitivity (−6% to −12% RAV); lab-like archetype is insensitive to the stack unless the mark falls ~80% | Unresolved but bounded under stated assumptions |
| O5 | "Forge medians reflect thin, selected trading." | Only 112 of 497 stale-vintage companies traded [S34] | Carta tender discounts also centre on 0% [S28]; the bimodal picture is consistent | Directionally robust; levels uncertain |
| O6 | "After an IPO the haircut disappears." | A listing plus lock-up expiry would convert paper to liquid stock | OpenAI deferral [S42]; SpaceX −40–50% from peak under staged lock-ups [S53, S54] | Illiquidity risk converts into market risk; it does not vanish |
| O7 | "The 16–24% promotion TC step mixes populations and years." | Built from Pave 2026 base steps and a 2025 equity step with an assumed equity share | Consistent with Bidwell (~18%) and coaching (+21–24%) [S2, S13] | C-grade; ±5 pp |
| O8 | "Survivorship bias: successful hoppers are who post." | Plausible for Blind/LinkedIn anecdotes | ADP and Atlanta Fed are not self-selected [S11, S12] | Reinforces that 35–50% is not typical |
| O9 | "India ESOP-tax summaries come from advisory blogs and may be outdated." | C-grade sources [S71, S72] | Multiple sources agree on perquisite-then-capital-gains structure | Confirm with a chartered accountant |
| O10 | "An Anthropic model analysing Anthropic's equity is conflicted." | True | Anthropic facts were sourced from third parties and graded identically; disclosure at top | Residual risk; verify against the S-1 when public |

---

## 8. Delta (belief change)

| # | Belief | Prior (memory, D) | What the evidence showed | Updated belief | Change |
|---|---|---|---|---|---|
| 1 | Same-tier hop premium | +15–30% TC | ADP +2.9 pp gross (economy); Bidwell +18%; coaching +21–24%; triangulated gap ≈ 22–30 pp for Senior→Staff [S2, S11, S13] | **+15–25%** | Refined (narrower) |
| 2 | "35–50% per hop" (brief) | True only at extremes | Compounding test fails for the median; only level/tier crossers reach it | Conditional on level-up or tier jump | **Contradicted as general** |
| 3 | Internal "5–10%" | Base 8–10%; TC 15–25% | Pave: promoted base 8.6% (R&D 7.7%, AI/ML 6.5%); merit 3.4%; TC step ≈ 16–24% [S14–S17] | Base right; TC larger; AI/ML promotion raises *lower* | Confirmed / refined |
| 4 | Promotion velocity | 1.5–2.5 y/level; Senior 6–9 YOE | Avg Senior at 8.6 YOE; Anthropic Senior 6–8; no AI-specific data [S3, S10] | Upper end of my range; AI-specific unverified | Partly confirmed |
| 5 | AI premium | +5–20%, rising with level | 6.2% / 11.9% / 14.2% / 18.7% (Entry→Staff) [S1] | Confirmed | Confirmed |
| 6 | Frontier-lab multiple | ×1.5–2.5 headline | ×2.0–3.1 headline vs all-company medians; ≈ ×1.7–2.4 risk-adjusted [S3, S4] | Higher headline than prior | Updated up |
| 7 | Preference overhang | Tail risk, plain terms | 95.8% 1×; 96.4% non-participating; cliff mechanism; stale cohort −61% median [S26, S34] | Not the market norm; a cliff in tails | Confirmed; brief's claim **contradicted as generalisation** |
| 8 | Hot AI names vs last round | At/above primary | Forge median −3% to −7%; OpenAI Forge Price > tender; Anthropic tender ≪ secondary [S33, S36, S49] | At/above for top names; new insight: **tender-price regret** | Confirmed + extended |
| 9 | Tender gates | 10–25% or $ cap; 1–2 yrs tenure | Carta median 20%; OpenAI $30M; Anthropic 20%/$2M; tenure 1–2 yrs [S28, S29, S38, S50] | Confirmed; frontier labs use dollar caps that are rising | Confirmed |
| 10 | IPO ≠ liquidity | Yes | SpaceX −40–50% from peak under staged lock-up; OpenAI no IPO in 2026 [S42, S53, S54] | Confirmed and strengthened | Confirmed |
| 11 | 83(b) | 30 days, no extension, not RSUs | IRS form + law firms; e-filing available since mid-2025 [S62–S65] | Confirmed; e-filing is new to me | Confirmed + updated |
| 12 | Dilution per round | 15–25% | Carta medians 19.5/18/14/10/7.5%; mega-rounds ≈ 3–14% [S31, S46, S60, S82] | Mega-round dilution far smaller | Refined |
| 13 | QSBS | Recalled pre-2025 rule (5-year, lower cap) | OBBBA: 3/4/5-year tiers, $15M cap, $75M assets [S66, S67] | Superseded | Updated |
| 14 | H-1B route | $100K fee in force | Extended but blocked/struck down in court; rules in flux [S69, S70] | Volatile | Updated |
| 15 | India Senior ceiling | ≈ ₹1Cr | P90 ≈ ₹1.07Cr; top employers ≈ ₹1.06–1.22Cr [S5] | Quantified | Confirmed |
| 16 | Equity haircut | ~50% for private AI equity | RAV 0.5–0.8 (labs), 0.4–0.8 (Series C–D), 0.15–0.3 (stale) | Stage-specific bands | Refined |
| 17 | Systems-expertise premium | Large and positive | No controlled evidence | Unresolved | **Unresolved (G)** |

---

## 9. Sources & Evidence Ledger

Grades follow the rubric in the preamble. "Snippet" means the page was seen as a search-result excerpt and not fetched in full. URLs are exactly as retrieved. Grade A rows are primary/canonical sources; a **claim-level** grade for each finding is given in §3.

| ID | Source (title / owner) | URL | Type · retrieval | Used for | Grade |
|---|---|---|---|---|---|
| S1 | Levels.fyi — "AI Engineer Compensation Trends (Q3 2025)" | https://www.levels.fyi/blog/ai-engineer-compensation-trends-q3-2025.html | Data owner · fetched | AI premium by level | A |
| S2 | Levels.fyi — "2025 End of Year Pay Report" | https://www.levels.fyi/2025/ · https://www.levels.fyi/2025/report.md | Data owner · fetched | Ladder medians; India/Europe/US medians; coaching uplift; YoY by level | A |
| S3 | Levels.fyi — Anthropic software-engineer salaries (snapshot 24 Sep 2026; n = 49) | https://www.levels.fyi/companies/anthropic/salaries/software-engineer | Data owner, small n · fetched | Anthropic levels, YOE | B |
| S4 | Levels.fyi — OpenAI salaries (updated 20 Oct 2026) | https://www.levels.fyi/companies/openai/salaries | Data owner, small n · fetched | OpenAI L2–L7; snapshot volatility (other dated snippets) | B |
| S5 | Levels.fyi — Senior Software Engineer, Greater Bengaluru (generated 21 Oct 2026; n = 4,836) | https://www.levels.fyi/t/software-engineer/levels/senior/locations/greater-bengaluru.md | Data owner · fetched | India senior distribution; top employers (entry-level figures from a search snapshot) | A |
| S6 | Levels.fyi — AI Engineer, Bengaluru | https://www.levels.fyi/t/software-engineer/title/ai-engineer/locations/bengaluru-ind | Data owner · fetched (unstable snapshot) | AI Engineer median/percentiles | B |
| S7 | Levels.fyi — job board, Software Engineer, Greater Bengaluru | https://www.levels.fyi/en-gb/jobs/title/software-engineer/location/greater-bengaluru | Job-board estimates · fetched | Staff base-salary estimates | C |
| S8 | Levels.fyi — Senior Software Engineer, London | https://www.levels.fyi/t/software-engineer/levels/senior/locations/london-metro-area | Data owner · snippet | London Senior/Entry | C |
| S9 | Levels.fyi blog — unique vesting schedules | https://www.levels.fyi/blog/unique-vesting-schedules.html | Blog · snippet | Schedule shapes (Amazon, Google) | B |
| S10 | LinkedIn post by Levels.fyi cofounder — YOE by level | https://www.linkedin.com/posts/zuhayeer_years-of-experience-level-something-weve-activity-7363288694377631744-dRz2 | Social post · snippet (page blocked to automation) | ~8.6 YOE to Senior; Google/Apple/Netflix ranges | C |
| S11 | ADP National Employment Report, Sept 2026 (PR syndication) and ADP Media Center, Aug 2026 | https://finviz.com/news/397020/adp-national-employment-report-private-sector-employment-increased-by-90000-jobs-in-september · https://mediacenter.adp.com/2026-09-02-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-38,000-Jobs-in-August | Data owner, via syndication · retrieved | Changers vs stayers | A |
| S12 | Fortune — "The demise of the job-hopping economy…" (citing Atlanta Fed) | https://www.fortune.com/2025/03/18/the-demise-of-the-job-hopping-economy-gen-zs-big-career-strategy-is-hitting-a-wall/ | Press · retrieved | Switchers vs stayers | B |
| S13 | Bidwell (2011), "Paying More to Get Less", Administrative Science Quarterly 56(3) | https://repository.upenn.edu/mgmt_papers/65/ | Peer-reviewed · retrieved | External-hire premium (~18%) | A |
| S14 | Pave — H1 2026 merit-increase benchmarks | https://www.pave.com/blog-posts/merit-increase | Vendor data · retrieved | Merit 3.4%; promoted +8.6% | B |
| S15 | Pave — "How the AI era is reshaping merit cycles" | https://pave.com/blog-posts/how-the-ai-era-is-reshaping-merit-cycles | Vendor data · retrieved | R&D 7.7%; AI/ML 4.4% / 6.5% | B |
| S16 | Pave 2026 Merit Cycle report press release (EIN Presswire, 28 May 2026) | https://norfolkdailynews.com/online_features/press_releases/2026-merit-cycle-report-ai-talent-premium-grows-as-raise-budgets-tighten/article_7de885ec-ae0f-50cc-8329-c06a9b6e613c.html | Press release · retrieved | Promotion rate 8.6%; India raise 9.9% | B |
| S17 | Pave — key insights, 2025 Merit Cycle webinar | https://www.pave.com/blog-posts/key-insights-from-paves-merit-cycle-state-of-the-union-webinar | Vendor data · retrieved | Promoted +9.7% base; +39% ongoing equity (n = 26K) | B |
| S18 | Pave — AI/ML talent insights (2025 report) | https://pave.com/blog-posts/ai-ml-talent-insights-4-key-takeaways-from-our-2025-report | Vendor data · snippet | Attrition ≈ 28% vs ≈ 17% | B |
| S19 | CIO Dive — SignalFire AI-talent report | https://www.ciodive.com/news/signalfire-AI-talent-engineering/732847/ | Press · snippet | AI engineers to management in < 3 years | C |
| S20 | DesignGurus — Google software engineer levels | https://www.designgurus.io/blog/google-software-engineer-levels | Blog · snippet | Community timelines | C |
| S21 | DesignGurus — FAANG job levels | https://www.designgurus.io/blog/understanding-faang-software-engineer-job-levels | Blog · snippet | Community timelines | C |
| S22 | The Interview Guys — Google salary levels | https://blog.theinterviewguys.com/google-salary-levels/ | Blog · snippet | L3→L4 timeline | C |
| S23 | ResumeAdapter — Meta levels | https://www.resumeadapter.com/companies/meta/levels | Blog · snippet | E5 as terminal level | C |
| S24 | Blind — L5→L6 promotion at Google/Facebook | https://www.teamblind.com/post/l5-to-l6-promo-at-google-facebook-dvkmmtdu | Community · snippet | L5→L6 anecdotes | D |
| S25 | Blind — time to reach level 65 at Microsoft | https://www.teamblind.com/post/how-long-to-reach-65-at-microsoft-from-high-62-jxujhcke | Community · snippet | Read; not used for numbers | D |
| S26 | Cooley — "Q2 2026 Venture Financing Report" | https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report | Law-firm dataset · retrieved | 95.8% 1×; 96.4% non-participating; 12.1% down rounds | A |
| S27 | Carta — "State of Private Markets: Q1 2026" | https://carta.com/data/state-of-private-markets-q1-2026/ | Data owner · fetched | Terms near lows; down rounds 11.4%; AI foundational valuations | A |
| S28 | Carta — "Tender Offer Update H1 2026" | https://carta.com/data/tender-offer-update-h1-2026/ | Data owner · fetched | Tender counts, participation, pricing, eligibility | A |
| S29 | Carta — tender offers, Q2 2025 | https://carta.com/data/tender-offers-q2-2025 | Data owner · snippet | Median 20% cap | B |
| S30 | Carta — startup tender offers and employee liquidity, 2025 | https://carta.com/data/linkedin-startup-tender-offers-employee-liquidity-2025/ | Data owner · snippet | 16,538 employee sellers | B |
| S31 | Carta — dilution by venture round (medians) | https://carta.com/data/linkedin-dilution-by-venture-round-medians/ | Data owner · snippet | 19.5 / 18 / 14 / 10 / 7.5% | B |
| S32 | Carta — founders rarely hold a majority after Series A | https://carta.com/data/linkedin-founders-rarely-majority-after-series-a/ | Data owner · snippet | Founders + pool ownership by round | B |
| S33 | Forge Global — Private Market Update, Aug 2026 | https://forgeglobal.com/insights/private-market-updates/100-billion-is-the-new-10-billion-august-2026/ | Data owner · fetched | July trade percentiles; −50% history | A |
| S34 | Forge Global — Private Market Update, Sept 2026 ("Great Reset…") | https://forgeglobal.com/insights/private-market-updates/great-reset-new-phase-discounted-acquisitions-september-2026/ | Data owner · fetched | Aug trade percentiles; Airtable/Miro; 2021 cohort | A |
| S35 | Forge Global — Q4 2026 Investment Outlook | https://forgeglobal.com/insights/forge-investment-outlook/q4-2026-investment-outlook/ | Data owner · fetched | IPO momentum; IOI 43.5% | A |
| S36 | Forge Global — OpenAI upcoming IPO news | https://forgeglobal.com/insights/openai-upcoming-ipo-news/ | Data owner · retrieved | Forge Price ≈ $894B | B |
| S37 | Forge Global — Databricks upcoming IPO news | https://forgeglobal.com/insights/databricks-upcoming-ipo-news/ | Data owner · retrieved | Forge Price ≈ $242; Series L follow-on | B |
| S38 | Yahoo Finance (WSJ summary) — OpenAI employees' Oct 2025 sale | https://finance.yahoo.com/markets/stocks/articles/600-openai-employees-scored-6-162500548.html | Press · retrieved | $6.6B sold; $30M cap; 2-year holding | B |
| S39 | The Decoder — OpenAI share sale and the $30M cap | https://the-decoder.com/openais-internal-share-sale-minted-roughly-75-multimillionaires-who-each-cashed-out-the-30-million-cap/ | Press · retrieved | ~75 sellers at cap | B |
| S40 | Calcalist (Bloomberg-sourced) — OpenAI $7B employee buyback | https://www.calcalistech.com/ctechnews/article/156mfxjli | Press · retrieved | Aug 2026 tender at $852B | B |
| S41 | People Matters — OpenAI buys back $7B in employee shares | https://www.peoplematters.in/news/ai-and-emerging-tech/openai-buys-back-dollar7-billion-in-employee-shares-ahead-of-potential-ipo-51379 | Press · retrieved | Corroboration | C |
| S42 | Fortune — Altman on IPO timing (12 Sep 2026) | https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/ | Press · retrieved | No OpenAI IPO in 2026 | B |
| S43 | TechCrunch — Altman: ill-advised to go public in 2026 | https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/ | Press · retrieved | Corroboration | B |
| S44 | TechCrunch — OpenAI completes its for-profit recapitalisation | https://techcrunch.com/2025/10/28/openai-completes-its-for-profit-recapitalization | Press · retrieved | 26% / 27% / 47% split | B |
| S45 | Bloomberg Law (summarising WSJ) — OpenAI to end equity vesting period | https://news.bloomberglaw.com/insurance/openai-to-end-equity-vesting-period-for-employees-wsj-says | Press · retrieved | Vesting-cliff removal | B |
| S46 | Orrick — Anthropic raises $65B Series H at $965B post-money | https://www.orrick.com/en/News/2026/05/Anthropic-Raises-65B-Series-H-at-965B-Post-Money-Valuation | Counsel announcement · retrieved | Series H terms | A |
| S47 | GV Wire (Reuters) — Anthropic Series H | https://gvwire.com/?p=249698 | Press · retrieved | Series G ≈ $380B; H corroboration | B |
| S48 | TipRanks — Anthropic wraps up tender offer as employees resist selling | https://www.tipranks.com/news/anthropic-wraps-up-tender-offer-as-employees-resist-selling-shares-ahead-of-ipo | Aggregator · retrieved | 2026 tender terms | C |
| S49 | Augment — "Anthropic's tender priced at $350B; the market said $1T" | https://augment.market/pulse/anthropics-tender-priced-at-350b-the-market-said-1t | Marketplace commentary · retrieved | Tender vs secondary gap | C |
| S50 | Maginative — Anthropic's first employee share buyback at $61.5B | https://www.maginative.com/article/anthropic-launches-first-employee-share-buyback-at-61-5-billion-valuation/ | Press · retrieved | 20% / $2M / ≥ 2 years | B |
| S51 | Gulf Times (Reuters) — Anthropic IPO launch said to shift to mid-October | https://www.gulf-times.com/article/732616/business/anthropic-ipo-launch-said-to-shift-towards-mid-october | Press · retrieved | IPO timing reports | C |
| S52 | INSIDE (Bloomberg-based) — Anthropic pre-IPO investor day | https://www.inside.com.tw/article/42543-anthropic-pre-ipo-investor-day-october-14 | Press · retrieved | IPO timing reports (conflicting) | C |
| S53 | Axios — SpaceX falls under IPO price as lock-up expirations loom (17 Jul 2026) | https://www.axios.com/2026/07/17/spacex-lockup-stock-selloff | Press · retrieved | IPO price; lock-up structure | B |
| S54 | Advisor Perspectives (Bloomberg) — SpaceX's $101B unlock pressure | https://www.advisorperspectives.com/articles/2026/08/05/spacexs-101-billion-unlock-pressure-shares | Press · retrieved | Staged lock-up; drawdown | B |
| S55 | TechCrunch — how Windsurf's VCs and founders got paid | https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal | Press · retrieved | Recent hires without payout | B |
| S56 | TechCrunch — Cognition acquires Windsurf | https://www.techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/ | Press · retrieved | Cliff waivers / acceleration | B |
| S57 | SaaStr — Airtable sold for $2.25B | https://www.saastr.com/airtable-just-sold-for-2-25b-at-2-7x-arr-it-raised-1-4b-and-was-once-worth-11-7b/ | Blog · retrieved | Airtable raise/peak/equity value | C |
| S58 | Reworked — Bending Spoons acquires Airtable | https://www.reworked.co/digital-workplace/bending-spoons-acquires-airtable-for-1285b/ | Trade press · retrieved | $1.285B EV | C |
| S59 | Fenwick — Databricks $4B+ Series L at $134B | https://www.fenwick.com/insights/experience/fenwick-represents-databricks-in-4b-series-l-funding-at-134b-valuation | Counsel announcement · retrieved | Series L incl. employee liquidity | A |
| S60 | The Next Web — Databricks closes $5B at $190B | https://thenextweb.com/news/databricks-closes-5-billion-round-at-190-billion-valuation | Press · retrieved | Aug 2026 round; CEO IPO comment | B |
| S61 | Bloomberg Law — Cohere to offer secondary sale of employee shares | https://news.bloomberglaw.com/private-equity/nvidia-backed-cohere-to-offer-secondary-sale-of-employee-shares | Press · retrieved | Cohere Oct 2025 secondary | B |
| S62 | IRS — Form 15620, Section 83(b) Election (Rev. 10-2024) | https://irs.gov/pub/irs-pdf/f15620.pdf | Agency form · fetched | 30-day rule; revocation | A |
| S63 | Morrison Foerster — Section 83(b) elections may now be filed online | https://www.mofo.com/pdf/resources/insights/250724-say-goodbye-to-paper-cuts-section-83-b | Law-firm alert · retrieved | Online filing | B |
| S64 | Goodwin — Online filing of Section 83(b) elections | https://www.goodwinlaw.com/en/insights/publications/2025/07/alerts-practices-erisa-online-filing-of-section-83b-elections | Law-firm alert · retrieved | Online filing | B |
| S65 | Snell & Wilmer — Electronic filing now available for 83(b) elections | https://www.swlaw.com/blogs/employee-benefits/2025/08/13/electronic-filing-now-available-for-section-83b-elections/ | Law-firm alert · retrieved | Online filing | B |
| S66 | Cooley — OBBBA expands QSBS benefits | https://www.cooley.com/news/insight/2025/2025-07-11-the-one-big-beautiful-bill-act-expands-qsbs-benefits | Law-firm alert · retrieved | QSBS tiers, caps | B |
| S67 | Wiggin and Dana — OBBBA client alert | https://www.wiggin.com/wp-content/uploads/2025/07/7.14.25_OBBBA-Client-Alert.pdf | Law-firm alert · retrieved | QSBS corroboration | B |
| S68 | Birketts — Autumn Budget 2025: changes to EMI | https://www.birketts.co.uk/legal-update/autumn-budget-2025-changes-to-enterprise-management-incentives/ | Law-firm alert · retrieved | EMI limits from 6 Apr 2026 | B |
| S69 | Yale OISS — proclamation extends H-1B $100,000 fee; fee remains blocked | https://oiss.yale.edu/news/presidential-proclamation-extends-h-1b-100000-fee-policy-fee-remains-blocked-by-court-order | University office · retrieved | H-1B status | B |
| S70 | Forbes — judge strikes down latest version of the $100,000 H-1B fee | https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/ | Press · retrieved | H-1B status | B |
| S71 | Wisemonk — ESOPs via EOR employment (India) | https://www.wisemonk.io/blogs/esops-via-eor-employment | Advisory blog · retrieved | Perquisite/capital-gains treatment | C |
| S72 | Treelife — ESOP taxation (India) | https://treelife.in/?p=16299 | Advisory blog · retrieved | Corroboration | C |
| S73 | Product Hunt — Startup Exit Calculator by Capbase | https://www.producthunt.com/products/startup-exit-calculator-by-capbase-2/launches/startup-exit-calculator-by-capbase-3 | Product listing · retrieved | Tool catalog | C |
| S74 | WealthManagement — Schwab agrees to buy Forge (≈ $660M) | https://www.wealthmanagement.com/alternative-investments/schwab-agrees-to-buy-private-share-platform-for-660m | Trade press · retrieved | Forge ownership; Forge Price scope | B |
| S75 | Morgan Stanley — acquisition of EquityZen (press release) | https://www.morganstanley.com/press-releases/leading-private-shares-platform-equityzen | Company announcement · snippet | EquityZen; issuer-centred model | A |
| S76 | Nasdaq Private Market — Caplight | https://www.nasdaqprivatemarket.com/company/caplight/ | Company page · retrieved | Tool catalog | C |
| S77 | PitchBook (vendor page) | https://pitchbook.com/PitchBookTV.html | Vendor page · retrieved | Tool catalog | C |
| S78 | TipRanks/TheFly — Wired: Meta offered AI talent up to $300M over 4 years | https://www.tipranks.com/news/the-fly/meta-has-offered-ai-research-talent-up-to-300m-over-4-years-wired-reports-thefly | Aggregator of a Wired report · retrieved | Apex-tier packages | C |
| S79 | TechCrunch — Meta response on AI pay packages | https://techcrunch.com/?p=3022848 | Press · retrieved | Meta's dispute | C |
| S80 | Acceler8Talent — GPU engineer recruitment 2026 | https://www.acceler8talent.com/resources/blog/gpu-engineer-recruitment--bay-area-and-boston-2026/ | Recruiter blog · retrieved | Systems-skill pay (non-causal) | C |
| S81 | Rockstar Developer University — AI infrastructure engineer | https://rockstardeveloperuniversity.com/ai-infrastructure-engineer/ | SEO/blog · retrieved | Job-posting ranges | C |
| S82 | Yahoo Finance (Verdict) — OpenAI closes $122bn funding round at $852bn valuation | https://finance.yahoo.com/markets/stocks/articles/openai-closes-122bn-funding-round-093126735.html | Press · retrieved | OpenAI Mar 2026 round; contingent capital | B |
| S83 | INSEAD Knowledge — "Transfer, promote or hire? It depends…" (summary of Bidwell) | https://knowledge.insead.edu/entrepreneurship/transfer-promote-or-hire-it-depends-whether-you-need-performance-soon | University magazine · retrieved | Early underperformance / exit of external hires | B |

**Not found / not retrievable (explicit gaps):** an AI-vs-non-AI time-in-level dataset; any source for a "35–50% per job change" statistic; tech-specific job-changer vs stayer study; OpenAI Aug 2026 tender caps/participation; Databricks/Cohere tender caps and tenure; Levels.fyi Staff-level Bengaluru medians; Europe time-in-level data; controlled evidence on India-remote pay-band compression; a controlled systems-expertise premium; a public Anthropic S-1.

*Recalled (unverified, Grade D) items used in this note and marked (R) where they appear:* equity-grant step size staying at +39% in 2026; illustrative top federal tax rates (37% / 23.8%); 83(b) inapplicability to RSUs; default 90-day post-termination exercise window; anti-dilution mechanics; 2024 non-disparagement controversy; Anthropic Series E raise ($3.5B) and Series F ($13B at $183B); OPM/409A common-valuation methodology.
