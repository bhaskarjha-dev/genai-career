---
id: T0-02
title: "Global & Regional Compensation Benchmarks for GenAI Roles — US, Europe, India, GCC, Singapore, Remote (October 2026)"
date: 2026-10-21
status: partial
status_note: "DONE-criteria scorecard: 2 met (base/bonus/equity decoupling; equity discount model), 2 partial (multi-geo percentile tables; infra-vs-app premium), 1 unmet (primary-platform India contractor rates). See section 6.15."
topic: "Empirical distribution of GenAI/ML engineer compensation (base cash, bonus, liquid equity, paper equity) by geography and experience tier, as of October 2026"
tags: [compensation, genai, ml-engineer, ai-engineer, levels-fyi, h1b-lca, dol-oflc, india, us, europe, gcc, singapore, remote, equity, tender-offers, ppp, fx]
informs_decisions:
  - "Offer evaluation: India-based engineer comparing local, US-remote and relocation offers"
  - "Hiring budget bands for GenAI/ML roles by geography and level"
  - "Equity valuation: how much of a frontier-lab or startup package to count as cash"
  - "Which paid or primary datasets to acquire next (Radford McLagan, Levels.fyi API, Pave, DOL LCA processing)"
confidence: medium-low
confidence_notes: "High for Levels.fyi all-level percentile bands (US, London, Bengaluru, Hyderabad) and the OpenAI/Anthropic level tables as of the retrieval date; low for tier-conditional non-US values, GCC, contractor rates, the infra-vs-app premium, and every equity discount factor."
evidence_as_of: 2026-10-21
revision: "r2 (21 Oct 2026): second pass added Hyderabad, UK-wide, Dubai and Singapore Levels.fyi pages, Google, Meta and Nvidia ML ladders, and same-employer geography ratios"
data_attribution: "Data source: Levels.fyi (https://www.levels.fyi)"
---

# T0-02 — Global & Regional Compensation Benchmarks for GenAI Roles (October 2026)

> **Evidence date.** Everything below was retrieved on 21 Oct 2026. The Levels.fyi pages for the US, SF Bay, London, Bengaluru, Singapore and OpenAI carry "last updated" stamps between 12 and 20 Oct 2026; the Anthropic page is stamped 24 Sep 2026 and the Google excerpt 4 Aug 2026. Items marked *cached* are search-engine copies with no visible date. The second-pass pages are stamped 12 Oct 2026 (Hyderabad), 15 Sep 2026 (UK-wide), 1–2 Apr 2026 (Singapore senior-level SWE) and 2 Nov 2025 (ByteDance Singapore); the Meta, Google and Dubai pages carry no visible date.
> **Attribution.** Data source: Levels.fyi (https://www.levels.fyi). The pages state that derived work must carry this credit; check the Levels.fyi Data License before redistributing derived tables.
> **Status: PARTIAL.** The brief's completion criteria are only partly met; the scorecard is in section 6.15 and the gaps are listed in section 7. Nothing in a gap cell has been filled with a guess presented as fact.

**Evidence grades (used throughout)**

| Grade | Meaning |
|---|---|
| **A** | Primary source opened this session at its canonical URL (Levels.fyi page or .md export, DOL/OFLC page, WTW/Pave/Aon press release, Carta Insights post, ECB rates). |
| **B** | Primary-derived: third-party processing of primary data, a named survey relayed by a reputable outlet, search-result excerpts of a canonical page that I did not open in full, or valuation literature. |
| **C** | Vendor, recruiter, aggregator, job-board or blog material with opaque or marketing-driven methodology. |
| **D** | Recalled from model memory before searching, or my own arithmetic/assumption. Capped at D by the calibration rules. |

Markers in the text: **[FOUND]** retrieved this session; **[RECALLED]** from memory, untested; **[MODEL]** my arithmetic or assumption; **†** the URL was not retained, or only an excerpt was seen in search results, so re-locate the source before relying on it.

---

## 1. Prior

Written before searching. Each proposition is checkable and graded D until tested (see the Delta table in section 8).

1. **[RECALLED]** On Levels.fyi, US all-level total compensation for the *Machine Learning Engineer* title has P50 around $250–300K and P90 near $500K; the newer *AI Engineer* title sits lower.
2. **[RECALLED]** OpenAI and Anthropic engineer medians on Levels.fyi are roughly $700–900K, with stock at least half of total compensation from the senior levels upward.
3. **[RECALLED]** Bengaluru ML Engineer P50 on Levels.fyi is ₹35–50L, while broad-market sources (Glassdoor, AmbitionBox) sit far lower at ₹10–25L, so the population sampled matters more than the city.
4. **[RECALLED]** At P50 in USD terms London is about 0.5–0.6× the US, Zurich 0.55–0.7×, and Bengaluru 0.12–0.2×.
5. **[RECALLED]** Inference/infrastructure specialists (vLLM, TensorRT-LLM, Triton) earn a 15–35% premium over application-layer AI engineers (RAG, agents), mostly through equity.

## 2. Research Question

**Decision question.** What is the empirical distribution of GenAI-role compensation — base cash, performance bonus, liquid equity and paper equity — across the US (SF Bay, NYC, remote), Europe (London, Berlin, Zurich), India (Bengaluru, Hyderabad, remote), the GCC (Dubai, Abu Dhabi), Singapore and international remote, as of October 2026, by experience tier (Tier 0 Entry to Tier 5 Apex)?

**Sub-questions (the five domain probes).**
1. Verified P25/P50/P75/P90 total compensation for AI engineers in Bengaluru/Hyderabad vs SF Bay vs London.
2. Share of pay delivered as illiquid paper equity at Series A/B AI startups vs liquid public stock at Big Tech.
3. Actual USD contract rates for India-based AI engineers on W-8BEN/contractor terms.
4. Infra/inference engineers (vLLM, TensorRT-LLM, Triton) vs application-layer AI engineers.
5. Frontier-lab premium (OpenAI, Anthropic, Google DeepMind, Meta FAIR) over market median for post-training and pre-training talent.

**Scoping notes.** No public source publishes a "GenAI engineer" percentile series. The closest primary proxies are Levels.fyi's *ML Engineer* and *AI Engineer* titles plus frontier-lab *Software Engineer* and *Research Scientist* pages. The tier definitions in section 6.1 are my operationalisation, not an industry standard.

---

## 3. Key Findings

**F1 — US distribution. [Grade A]** Levels.fyi US *ML Engineer* (n = 1,063; 19 Oct 2026): P25/P50/P75/P90 = **$200,000 / $280,000 / $385,500 / $497,500**. US *AI Engineer* (n = 335; 18–19 Oct 2026): **$110,000 / $154,000 / $212,500 / $280,000**. The AI Engineer title sits at 0.55–0.56× the ML Engineer title at every percentile; that is a title and employer-mix gap (ML Engineer skews to Big Tech with equity), not a measured skill premium. Blog claims of a Levels.fyi "AI Engineer average" of $242–245K do not match the primary page's percentiles (P75 $212.5K, P90 $280K); a mean-versus-median difference or an older vintage may explain part of the gap (Grade C). On these pages $300K is about P55 for ML Engineer and above P90 for AI Engineer. [S01, S02, S43]

**F2 — Geography. [Grade A/B; ratios Grade D arithmetic]** P50 total compensation, Levels.fyi *ML Engineer*: SF Bay **$327,860** (1.17× US), NYC **$264,509** (0.95×), London **£112,641 ≈ $149K** (0.53×), Greater Bengaluru **₹44.5L ≈ $46.7K** (0.17×), Zurich **CHF 134,196 ≈ $161K** (0.58×; excerpt whose URL I did not retain, Grade C; Robert Half's placement-based Zurich guide gives a lower base-only P50 of CHF 121.9K). Berlin ($97.7K) comes from a stale, thin page (25 Jul 2025; Grade C). London and Bengaluru ratios stay in a band across percentiles (0.53–0.59 and 0.15–0.20); SF's premium compresses from 1.25× at P25 to 1.03× at P90. Hyderabad ML (12 Oct 2026) is **₹30.3L ≈ $31.8K** (0.11× US, 0.68× Bengaluru), which replaces my earlier SWE-based proxy of 0.89× Bengaluru. Within one employer the gaps are narrower than the all-company ratios: Google's UK software-engineer pay is 0.66–0.76× its US pay at L3–L5, and Google Bengaluru ML pay is 0.22–0.45× Google US ML pay, against 0.53× (London) and 0.17× (Bengaluru) for all-company medians, so employer mix, not only geography, drives the all-company gaps. [S02–S08, S30, S39, S48–S50, S52]

**F3 — The India claim, tested. [Grade A for Levels.fyi; C for broad market]** Greater Bengaluru ML Engineer (n = 96; 12 Oct 2026): **₹28.9L / ₹44.5L / ₹68.6L / ₹94.6L** at P25/P50/P75/P90. The claim "₹50L–₹1Cr" therefore describes roughly **P56 to just above P90 of a self-selected, MNC/product-heavy sample**, not the market. Broad-market sources put the centre at ₹10–15L: Glassdoor India "AI Engineer" base about ₹10L (₹6–15L range, Aug 2026), "AI Developer" ₹6.95L (n = 167, Jun 2026), Indeed ₹10.5L (n = 79, Apr 2026), Payscale ₹4.5L, AIM Research median ₹12–15L (2025): a 3–4× gap. The gap is employer type: Levels.fyi Bengaluru SWE medians run from ₹13.1L (Fidelity) to ₹47.0L (LinkedIn) at entry level and from ₹24.9L (Sony) to ₹121.9L (X) at senior level. Hyderabad ML Engineer (12 Oct 2026) is **₹23.4L / ₹30.3L / ₹45.8L / ₹84.7L**, with a ₹26.9L median base. Google Bengaluru ML runs ₹45.2L (L3), ₹65.2L (L4) and ₹168.3L (L5). Treat India as two populations (MNC/GCC/product vs the rest). [S03, S10, S15, S33, S34, S48, S49]

**F4 — Frontier-lab level (Levels.fyi, US). [Grade A, small n]** OpenAI SWE (n = 242; 20 Oct 2026): median **$875,000**, mean $840,800. Anthropic SWE (n = 49; 24 Sep 2026): median **$882,500**, mean $816,227. By level: OpenAI L2 $249K → L5 $911K; Anthropic entry $483K → Staff $1.41M. Research Scientist medians are higher at OpenAI (about $1.25M, cached) and lower at Anthropic ($0.75–0.83M, cached). Premium: 3.1× the US ML Engineer median, 2.7× the SF Bay ML median, 1.8× the US ML Engineer P90. Medians are unstable: cached copies of the OpenAI SWE page show US medians from $555K to $875K. [S02, S05, S11, S12, S14]

**F5 — Base vs equity decoupled. [Grade A]** Base is compressed while stock scales with level. OpenAI: base $170K (L2) → $361K (L5), 2.1×; stock $79K → $550K, 7.0×. Anthropic: base $266K (entry) → $403K (Staff), 1.5×; stock $216K → $1.01M, 4.7×. Base share of total falls from 68% to 40% (OpenAI L2→L5), 55% to 29% (Anthropic entry→Staff), and 77% to 64% (Google ML L3→L4). Pave's August 2026 report (Grade A press release) shows the same pattern across job families: ML Engineering median base is $321K at P6 and $347K at M6, while median new-hire equity for AI Research Scientists is $4.09M at P6 and $4.72M at M6, more than double ML/AI Engineering. [S11–S13, S23]

**F6 — H-1B LCA evidence. [Grade B; raw DOL files not processed]** OpenAI: 311 certified LCAs across FY2025 and FY2026-to-Q3; median offered wage (lower bound of the stated range) **$270K** (FY2025 $285K; FY2026 YTD $260K, middle half $245–325K); position-level 2025 median **$310K** against an average prevailing wage of $162K. OpenAI by title (2025 positions): MTS-Software Engineer $255K, MTS-Research Engineer $335K, MTS-AI Systems Engineer $335K, MTS-Research Scientist $360K. Anthropic: 292 certified LCAs; lower-bound median **$209K** (FY2025 $300K; FY2026 YTD $189.6K, middle half $169.5–213.5K); position-level 2025 MTS median $315K. The FY2025-to-FY2026 drop reflects range floors set at the legal minimum (one Anthropic Research Engineer LCA lists a base of $138,445 equal to its prevailing wage, with a range up to $500,000). LCA wages are floors, not pay. [S16–S20]

**F7 — Frontier equity is semi-liquid, not Series-A paper. [Grade B]** OpenAI: $6.6B tender at $500B (Oct 2025); a roughly $7B company-funded buyback at $852B completed around 10 Aug 2026 (the same valuation as its March 2026 round); confidential IPO filing in June 2026 (the NYT reportedly later flagged possible delay). Anthropic: a tender for current and former staff with at least 12 months of tenure, with outside investors buying at $350B pre-money (the same price as its February Series G), completed around early April 2026 below the $5–6B investors had lined up because employees sold less than expected. Both priced at the last round (no visible discount); per-person caps and the share of vested stock that could be sold are not reported. [S28, S29]

**F8 — Equity discount model. [Inputs Grade B; outputs Grade D]** DF = value to the employee ÷ grant-date paper mark. Public RSU **0.95–1.00**; frontier lab with tenders **0.64–0.88**; late-stage private **0.42–0.61**; Series A/B **0.09–0.21** (haircut view) or **0.21–0.53** (upside credited). Cash-equivalent total: Anthropic Staff $1.04–1.29M vs $1.41M headline (74–91%); OpenAI L5 $710–844K vs $911K (78–93%). Inputs: DLOM 34–47% (restricted-stock and pre-IPO studies; 5–50% overall range, higher for common than preferred); Carta Series A→B two-year graduation of about 9–15% (2022 cohorts) to about 40% (2020 cohorts), about 28% in 2018, "about half" in a strong cohort; per-round dilution roughly 18–23% (Carta medians as relayed by secondary sites; URLs not retained†). Startup structure: Carta puts P80–95 AI/ML engineers at AI-native startups valued above $500M at about $320K salary + 0.146% equity; only 14% of 43,480 US AI-engineering postings mention equity and 31% a bonus, so posted ranges are base-only. [S11, S12, S25–S27, S36]

**F9 — PPP vs nominal FX for Indian engineers. [FX Grade A/B; PPP Grade C]** USD/INR is about 95.2 (19 Oct 2026), with the rupee about 8.3% weaker year on year. The World Bank ICP PPP factor is about ₹22–23 per international dollar (relayed by secondary sites), a price-level ratio near 0.24. The US ML P50 ($280K) is **6.0×** the Bengaluru P50 at market FX but **1.44×** at PPP; the PPP-equivalent of the US P50 in India is about ₹64L (≈ P70 of Bengaluru ML). Market FX is the right lens for savings and remittances, PPP for local consumption; tax and cost of living were not researched. [S30–S32]

**F10 — GCC. [Grade C]** Aggregators citing Michael Page's 2026 UAE guide put mid-level AI/ML engineers in Dubai at about AED 25–45K per month (average 35K ≈ $114K a year; the UAE levies no personal income tax **[RECALLED, Grade D]**); an independent aggregator quotes AED 25–40K for mid-level and 40–65K+ for senior. One aggregator's Abu Dhabi band is exactly 0.95× each Dubai figure, so it is derived, not independent; another shows Abu Dhabi at about 0.98× Dubai. Arabian Business reports that Michael Page's guide found UAE pay rises of 4–6% in 2025, sharpest in AI engineering and product management. A lower-paid broad market sits well below those bands: Glassdoor Dubai (n = 19) shows a median of about AED 15K a month, Naukrigulf (n = 32) about AED 7.6K and Indeed UAE about AED 6.2K. Levels.fyi's Dubai software-engineer page (all levels, not ML; undated) shows AED 240K / 300K / 430K / 546K at P25/P50/P75/P90, about AED 25K a month at the median, which matches the low end of the recruiter band; its Dubai ML/AI page is about two years old and is not used. [S37, S38, S54]

**F11 — India-based contractor rates. [Grade C; criterion unmet]** Marketplace-listed ranges (as relayed by one vendor, Sep–Oct 2026): Upwork $25–150/h, Toptal $70–200/h, Arc $61–100/h. The same vendor reports India mid-level AI/ML engineers at $28–72/h overall, with a rate card of $35–50/h (international-client contract) and $44–63/h (freelance). At 160 h/month, $35–63/h is $5.6–10.1K a month, or ₹64–115L a year at ₹95.25, about P70 to above P90 of Levels.fyi Bengaluru full-time pay, before benefits, tax and bench time. No platform-native percentile data was found. [S35]

**F12 — Infra/systems vs application premium: partially supported, not validated. [Grade B/C/D]** Two independent base-pay datasets show a systems premium: OpenAI's 2025 LCAs put MTS-AI Systems Engineer at $335K vs MTS-Software Engineer $255K (+31%), and Robert Half's 2026 Zurich guide (placement-based starting base) puts AI/ML System Performance Specialist at CHF 137.8K vs AI Developer CHF 116.6K (+18%) and ML Engineer CHF 121.9K (+13%). Elsewhere: Pave P4 senior ML median base $210K vs software-engineering generalist $196K (+7%); Comprehensive.io's 2023 posted-pay finding of +19% for ML Engineer over Software Engineer; the US ML-vs-AI Engineer title gap of 1.8× (about half of it is employer mix: at Google alone the ML Engineer median is 26–39% above the AI Engineer median); vendor guides claiming 20–35% for vLLM/TensorRT-LLM/CUDA skills without a stated source (Grade C). Caveats: base only, one employer or one city each, seniority not controlled, no dataset separates vLLM/TensorRT-LLM/Triton skills from application-layer AI work. [S01, S02, S17–S19, S24, S39, S41, S43, S45, S49]

---

## 4. Recommendation

1. **Anchor on Levels.fyi percentile bands by title and city, and treat them as the large-employer, equity-bearing reference.** Use the *ML Engineer* bands (US $200K / $280K / $385.5K / $497.5K; SF Bay $250K / $327.9K / $413K / $512K; NYC $196K / $264.5K / $346.8K / $460K; London £89.5K / £112.6K / £163K / £221K; Greater Bengaluru ₹28.9L / ₹44.5L / ₹68.6L / ₹94.6L; Greater Hyderabad ₹23.4L / ₹30.3L / ₹45.8L / ₹84.7L at P25/P50/P75/P90). For India always carry a second reference population (broad-market centre of ₹10–15L) and the employer-type dispersion in section 6.5.
2. **Judge every offer on a cash-equivalent basis, not the headline.** Count base + bonus + DF × equity, with DF from section 6.12: 0.95–1.00 for public RSUs, 0.64–0.88 for OpenAI/Anthropic-style tender-backed stock, 0.42–0.61 for late-stage private, 0.09–0.21 for Series A/B (0.21–0.53 only if you credit upside). These are model outputs (Grade D); the inputs are sourced.
3. **Restate the two headline claims.** India "₹50L–₹1Cr" is roughly P56 to just above P90 of Levels.fyi Bengaluru ML Engineer, not the market median. US "$300K–$1M+" starts at about P55 of ML Engineer and above P90 of the AI Engineer title; the $1M+ end is frontier-lab L5+ territory (OpenAI L5 $911K average, Anthropic Staff $1.41M), not a general GenAI figure.
4. **For an Indian engineer weighing foreign offers, compute both lenses and decide which applies to the goal.** At market FX the US ML P50 is 6.0× Bengaluru P50; at PPP it is 1.44× (PPP-equivalent ≈ ₹64L ≈ P70). The rupee is about 8.3% weaker year on year, which lifts the rupee value of any USD offer. Tax, cost of living, visa cost and savings rate were not modelled and decide the answer.
5. **Do not use these for binding decisions until primary data replace them:** GCC bands (Grade C), contractor rates (Grade C), the non-US tier-conditional grid (Grade D), Zurich/Berlin Levels.fyi rows (Grade C), and any discount factor outside the stated ranges. The infra/systems premium can be quoted only as "+13% to +31% in base at two datasets", with the caveats in F12.
6. **Close the gaps in this order (value per hour):** (a) pull Levels.fyi per-level × per-location pages or the Levels.fyi API/MCP (the site advertises both) to fill the tier grid; (b) download and process the DOL FY2026 Q3 LCA file locally for AI-related titles (my sandbox cannot resolve dol.gov); (c) obtain Radford McLagan AI job-family cuts for UK, Germany, India, UAE and Singapore (Aon announced AI job families on 31 Mar 2026; data is paywalled); (d) collect platform-native rate cards (Arc, Toptal, Turing, Upwork) and a chartered-accountant view of W-8BEN and contractor taxation; (e) obtain the Michael Page and Cooper Fitch UAE guides directly.

## 5. Alternatives Considered

| Alternative | Why considered | Verdict |
|---|---|---|
| H-1B LCA wages as the main anchor | Government-filed, employer-attested, large counts | **Rejected as anchor.** Base only; "Member of Technical Staff" hides seniority; range floors set at prevailing wage (Anthropic FY2026); only visa-sponsored roles. Kept as a base-wage floor and a within-employer title comparison. |
| Job-posting ranges (Comprehensive.io, Axial, recruiter scrapes) | Large n, current | **Cross-check only.** Base only; 14% of AI-engineering postings mention equity; posted is not paid. No public Comprehensive.io AI-engineer percentile page was found. |
| Broad crowdsourced sites (Glassdoor, Payscale, Indeed, AmbitionBox) | Broad population; a realistic lower bound for India | **Used as population contrast**, not for equity-bearing roles. |
| Vendor and recruiter "salary guides" (Instahyre, Second Talent, aggregator pages) | Only source for India GenAI bands, contractor rates and GCC | **Shown at Grade C**, never used for percentiles. One GCC band shown to be mechanically derived. |
| Option-pricing (Black-Scholes) valuation of equity | Standard for options | **Not used.** RSU-like units and tender liquidity dominate here; I used DLOM + graduation + dilution + tender mix instead. |
| Scaling the US tier ladder by geography ratios | The brief asks for all tiers × geographies | **Illustrative only** (section 6.5, Grade D). |
| PPP only, or market FX only | The two lenses differ by a factor of 4 | **Present both**; the right one depends on whether the goal is savings or local consumption. |
| Drop the "GenAI" label and use title proxies | No public "GenAI engineer" series exists | **Adopted**: ML Engineer, AI Engineer, frontier-lab SWE and Research Scientist. |

---

## 6. Detailed Findings

### 6.1 Tier definitions (operational; Grade D)

The brief names six tiers without defining them. This mapping is mine, built from the level and years-of-experience labels Levels.fyi shows (OpenAI L2 about 0–1 years, L3 about 2–3 years; Anthropic Senior about 6–8 years and Lead about 7–8 years).

| Tier | Label | Working definition | Big Tech ladder (Google) | Frontier-lab analogue |
|---|---|---|---|---|
| 0 | Entry | 0–2 years | L3 | OpenAI L2; Anthropic entry "Software Engineer" |
| 1 | Growth | 2–5 years | L4 | OpenAI L3 |
| 2 | Breakout | 5–8 years | L5 | OpenAI L4; Anthropic Senior |
| 3 | Premium | 8–12 years | L6 | OpenAI L5; Anthropic Lead |
| 4 | Elite | Principal / frontier research | L7 | OpenAI L6–L7 and Research Scientist; Anthropic Staff and Research Scientist |
| 5 | Apex | Bespoke packages for a few hundred researchers | n/a | Indirect only: Pave reports 90th-percentile new-hire equity of $45–60M at the most senior levels at private SF Bay companies that have raised $1B–$5B+ |

Frontier-lab titles are compressed ("Member of Technical Staff"), so mapping by years is approximate. Anthropic "Senior" (6–8 years) pays like OpenAI L4–L5.

### 6.2 Verified all-level distributions by geography (local currency)

| Geography | Title | Ccy | P25 | P50 | P75 | P90 | n | As of | Grade | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| United States | ML Engineer | USD | 200,000 | 280,000 | 385,500 | 497,500 | 1,063 | 19 Oct 2026 | A | S02 |
| United States | AI Engineer | USD | 110,000 | 154,000 | 212,500 | 280,000 | 335 | 18–19 Oct 2026 | A | S01 |
| SF Bay Area | ML Engineer | USD | 250,000 | 327,860 | 413,000 | 512,000 | not shown | 14 Oct 2026 | B | S05 |
| NYC area | ML Engineer | USD | 196,000 | 264,509 | 346,800 | 460,000 | not shown | cached | B | S06 |
| Greater London | ML Engineer | GBP | 89,500 | 112,641 | 163,000 | 221,000 | not shown | 15 Oct 2026 | A | S04 |
| Zurich | ML Engineer | CHF | 108,263 | 134,196 | 211,453 | 294,803 | not shown | cached | C† | S07 |
| Berlin | ML Engineer | USD | 86,700 | 97,683 | 106,000 | 114,000 | small | 25 Jul 2025 | C | S08 |
| Greater Bengaluru | ML Engineer | INR | 2,892,490 | 4,451,537 | 6,859,324 | 9,463,746 | 96 | 12 Oct 2026 | A | S03 |
| Greater Bengaluru | AI Engineer | INR | not shown | 2,139,582 | not shown | not shown | not shown | 18 Oct 2026 | B | S10 |
| Greater Bengaluru | ML Ops Engineer | INR | not shown | 2,363,338 | 4,105,587 | 6,352,858 | not shown | cached | C† | S10 |
| Singapore | Software Engineer (all levels, not ML) | SGD | 84,852 | 114,754 | 163,032 | 214,982 | 1,362 | 18 Oct 2026 | A (proxy) | S09 |
| Greater Hyderabad | ML Engineer | INR | 2,338,335 | 3,027,841 | 4,575,081 | 8,465,516 | not shown | 12 Oct 2026 | B | S48 |
| United Kingdom (all) | ML Engineer | GBP | 76,611 | 102,971 | 150,133 | 214,191 | not shown | 15 Sep 2026 | B | S52 |
| Singapore | Senior Software Engineer (not ML) | SGD | 129,000 | 180,537 | 234,000 | 298,000 | not shown | 2 Apr 2026 | B (proxy) | S53 |
| Dubai | Software Engineer (all levels, not ML) | AED | 240,000 | 300,041 | 430,000 | 546,000 | not shown | undated | B (proxy) | S54 |
| Greater Dubai | ML / AI Software Engineer | AED | 199,992 | 320,004 | 390,054 | 584,744 | not shown | stale (page about 2 years old) | C | S54 |
| Abu Dhabi | not found | | | | | | | | | |
| US Remote, Indian Remote, International Remote | no percentile source located | | | | | | | | | |

Notes on Table A:
- London P75/P90 are the page's rounded figures (£163K, £221K); the structured data gives £162,784 and £221,261.
- The SF Bay row comes from a search-result excerpt of the canonical page; the page was not opened in full. † means the URL was not retained and the figure should be re-pulled before use.
- **Data-hygiene warnings.** The Levels.fyi `.md` export for Greater Bengaluru labels its location "United States" although every value is in rupees. A search returned a Miami ML page (cached 3 Aug 2026, median $145K) whose header also read "United States". A Hong Kong ML export carries the same mislabel (HKD figures under a "United States" header). Validate currency, location and n before ingesting these exports programmatically.
- **Hyderabad.** Direct Levels.fyi data (12 Oct 2026) replaced my earlier SWE-based proxy: the measured P50 is 0.68× Bengaluru (₹30.3L), not the 0.89× (₹39.6L) that the Levels.fyi software-engineer city table implied. Hyderabad's median base is ₹26.9L (about 89% of total), and its all-levels software-engineer median (₹30.7L) is within 2% of its ML Engineer median, so no ML premium is visible there.

### 6.3 USD conversions and ratios to the US ML Engineer distribution

FX used: ECB reference rates of 13 Oct 2026 (EUR/USD 1.1188; per euro: 0.84460 GBP, 0.9312 CHF, 1.4319 SGD, 106.60 INR) give USD 1.3247 per GBP, USD 1.2015 per CHF and USD 0.7813 per SGD; the ECB cross for INR is 95.28 per USD and Investing.com shows about 95.24 on 19 Oct, so I used 95.25. The AED/USD peg of 3.6725 is **[RECALLED, Grade D]**.

| Geography (title) | P25 (USD) | P50 (USD) | P75 (USD) | P90 (USD) | Ratio to US ML Engineer, P25 / P50 / P75 / P90 |
|---|---|---|---|---|---|
| US ML Engineer | 200.0K | 280.0K | 385.5K | 497.5K | 1.00 |
| US AI Engineer | 110.0K | 154.0K | 212.5K | 280.0K | 0.55 / 0.55 / 0.55 / 0.56 |
| SF Bay ML Engineer | 250.0K | 327.9K | 413.0K | 512.0K | 1.25 / 1.17 / 1.07 / 1.03 |
| NYC ML Engineer | 196.0K | 264.5K | 346.8K | 460.0K | 0.98 / 0.95 / 0.90 / 0.92 |
| London ML Engineer | 118.6K | 149.2K | 215.6K | 293.1K | 0.59 / 0.53 / 0.56 / 0.59 |
| Zurich ML Engineer (C†) | 130.1K | 161.2K | 254.1K | 354.2K | 0.65 / 0.58 / 0.66 / 0.71 |
| Berlin ML Engineer (stale, C) | 86.7K | 97.7K | 106.0K | 114.0K | 0.43 / 0.35 / 0.27 / 0.23 (not reliable) |
| Bengaluru ML Engineer | 30.4K | 46.7K | 72.0K | 99.4K | 0.15 / 0.17 / 0.19 / 0.20 |
| Hyderabad ML Engineer | 24.5K | 31.8K | 48.0K | 88.9K | 0.12 / 0.11 / 0.12 / 0.18 |
| UK-wide ML Engineer (B) | 101.5K | 136.4K | 198.9K | 283.7K | 0.51 / 0.49 / 0.52 / 0.57 |
| Singapore Software Engineer (not ML) | 66.3K | 89.7K | 127.4K | 168.0K | not comparable |
| Singapore Senior Software Engineer (not ML) | 100.8K | 141.1K | 182.8K | 232.8K | not comparable |
| Dubai Software Engineer (not ML) | 65.4K | 81.7K | 117.1K | 148.7K | not comparable |

Cross-check (Grade B, press release): WTW's 2026 survey of mid-level technical-expert ML roles across ten countries reports median total compensation above $170K in the US, about $122K in Germany and just under $100K in the UK, ratios of at most about 0.72 and 0.59, because the US figure is reported only as above $170K. That is a broad corporate sample, yet the UK ratio sits next to the Levels.fyi London ratio (0.53–0.59). WTW also reports average year-on-year growth of 2% in base and 6% in total compensation for these roles, so recent growth is mostly non-cash. [S22]

### 6.4 Decoupling base, bonus and equity

**Table C1 — ladder-level components (US, Levels.fyi).**

| Employer / level | Total | Base | Stock per year | Bonus | Base % | Stock % | Bonus % |
|---|---|---|---|---|---|---|---|
| Google ML Engineer L3 | $199K | $154K | $35.1K | $9.8K | 77% | 18% | 5% |
| Google ML Engineer L4 | $294K | $189K | $88.6K | about $16K (residual) | 64% | 30% | 6% |
| OpenAI L2 | $249K | $170K | $78.8K | $0.6K | 68% | 32% | 0% |
| OpenAI L3 | $346K | $220K | $126K | $0 | 64% | 36% | 0% |
| OpenAI L4 | $769K | $311K | $457K | $0 | 40% | 59% | 0% |
| OpenAI L5 | $911K | $361K | $550K | $0 | 40% | 60% | 0% |
| Anthropic entry | $483K | $266K | $216K | $0 | 55% | 45% | 0% |
| Anthropic Senior | $621K | $316K | $305K | $0 | 51% | 49% | 0% |
| Anthropic Lead | $865K | $336K | $527K | $2K | 39% | 61% | 0% |
| Anthropic Staff | $1.41M | $403K | $1.01M | $0 | 29% | 72% | 0% |

Shares are computed from component averages and can total slightly more or less than 100% (Anthropic Staff sums to 101%). Levels.fyi lists 4-year vesting for both labs; Anthropic's page shows a 25% one-year cliff then monthly vesting. [S11–S13]

**Table C2 — geography medians (component medians are not additive).**

| Geography | Total (median) | Base | Equity | Bonus | Base share of total |
|---|---|---|---|---|---|
| NYC ML Engineer (B, cached) | $264.5K | $200K (P25 $170K, P75 $226K, P90 $280K) | median $25K (P75 $100K, P90 $192K) | P75 $25K, P90 $52K | about 76% |
| London ML Engineer (B excerpt, cached) | £112.6K | £95.2K (P75 £118.5K, P90 £134.3K) | not split | not split | about 84% |
| Bengaluru ML Engineer, city page (B, cached) | ₹45.3L | ₹38.3L | ₹2.06L | ₹2.44L | about 85% (equity 4.5%, bonus 5.4%) |
| Zurich ML Engineer (C†) | CHF 134.2K | CHF 122.1K (P25 105.8K, P75 165.6K, P90 176.9K) | not split | not split | about 91% |

Outside the large US employers, pay is overwhelmingly cash: equity is 5–10% of the median package in Bengaluru and NYC, and the base-to-total ratio is 84–91% in London, Bengaluru and Zurich.

**Table C3 — the four-component schema by employer archetype.** "Liquid" means sellable at vest on a public market; "paper" means not freely sellable.

| Archetype | Base cash | Performance bonus | Liquid equity | Paper equity | Basis |
|---|---|---|---|---|---|
| Public Big Tech (Google ML L3) | 77% | 5% | 18% | 0% | Levels.fyi; public RSUs |
| Public Big Tech (Google ML L4) | 64% | 6% | 30% | 0% | Levels.fyi |
| Frontier lab (OpenAI L5) | 40% | about 0% | 0% by default | 60%, semi-liquid through tenders (DF 0.64–0.88) | Levels.fyi; tender sources S28 |
| Frontier lab (Anthropic Staff) | 29% | about 0% | 0% by default | 72%, semi-liquid through tenders | Levels.fyi; S29 |
| AI-native startup valued above $500M (Carta P80–95 AI/ML engineer) | 64% of paper TC | not reported | 0% | 36% of paper TC (lower bound at the $500M floor); about 20–26% of cash-equivalent TC at late-stage DF 0.42–0.61 | Carta S25; [MODEL] |
| Indian employer, all-company (Levels.fyi Bengaluru city page) | about 85% | about 5% | about 4.5% (type not shown) | not shown | S10; ESOP data not found |

### 6.5 Tier ladder anchors and India employer dispersion

**Table D — US tier anchors (Levels.fyi; total, with base / stock per year / bonus in $K).**

| Tier | Google ML Engineer (two snapshots) | Meta ML Engineer | Nvidia ML Engineer | OpenAI SWE | Anthropic SWE |
|---|---|---|---|---|---|
| 0 Entry | L3 $199–205K (154 / 35–38 / 10–13) | E3 $187K (138 / 33 / 17) | IC1 $205K (168 / 38 / 0) | L2 $249K (170 / 79 / 0.6) | entry $483K (266 / 216 / 0) |
| 1 Growth | L4 $294–312K (189 / 89–104 / 16–19) | E4 $310K (186 / 101 / 23) | IC2 $208K (164 / 37 / 7) | L3 $346K (220 / 126 / 0) | no separate level |
| 2 Breakout | L5 $393–445K (214–216 / 151–194 / 27–35) | E5 $458K (230 / 198 / 31) | IC3 $315K (203 / 96 / 16) | L4 $769K (311 / 457 / 0) | Senior $621K (316 / 305 / 0) |
| 3 Premium | L6 $607–646K (272 / 304–335 / 32–39) | E6 $782K (261 / 481 / 39) | IC4 $340K (231 / 97 / 12) | L5 $911K (361 / 550 / 0) | Lead $865K (336 / 527 / 2) |
| 4 Elite | L7 $743K (page-level figure) | E7 not shown | not shown | L6 about $1.19–1.35M (cached copies); L7 packages up to about $1.9M (live-page maximum $1,942,125); Research Scientist median about $1.25M (cached) | Staff $1.41M (403 / 1,010 / 0); Research Scientist median $0.75–0.83M (cached, C†) |
| 5 Apex | n/a | n/a | n/a | n/a | n/a; indirect evidence only (Pave, section 6.1) |

Gaps: OpenAI L6/L7 current values were not captured (the OpenAI page hides the top two levels behind a prompt), Meta E7 and Nvidia IC5+ are not shown, and the two Google snapshots (undated) differ by up to 13% at L5. Tier-conditional P25/P75/P90 per geography are **not available** for ML Engineer; the closest are the senior-level software-engineer pages for Singapore (Table A) and Bengaluru (Table D2). Sources: S49, S51.

**Table D2 — India employer dispersion for software engineers (Levels.fyi, Greater Bengaluru; not ML-specific).** Medians of total compensation.

| Employer | Entry level | Senior level |
|---|---|---|
| X | ₹40.5L (SWE) | ₹121.9L (Senior SWE) |
| LinkedIn | ₹47.0L (IC1) | ₹109.6L (IC3) |
| Microsoft | ₹27.1L (SDE 59) | ₹71.5L (Senior SDE 63) |
| SAP | ₹14.4L (T1) | ₹43.2L (T3) |
| Fidelity Investments | ₹13.1L (L3) | ₹28.9L (L5) |
| Sony | ₹13.5L (L3) | ₹24.9L (L6) |

The spread between employers is 3.6× at entry level and 4.9× at senior level. Aggregated Levels.fyi Bengaluru SWE pages (URLs not retained†): entry level P25/P50/P75/P90 = ₹11.3L / ₹18.9L / ₹26.4L / ₹33.3L (updated 5 Apr 2026); a page whose URL path indicates senior level = ₹37.8L / ₹55.4L / ₹79.5L / ₹106.6L (updated 18 Jul 2026; the page title does not state the level, so treat the label as unconfirmed). [S10, S15]

**Google ML Engineer, Greater Bengaluru (Levels.fyi; small samples).** L3 ₹45.2L (base ₹23.9L; stock ₹19.7L a year; bonus ₹1.6L), L4 ₹65.2L (₹38.1L / ₹21.5L / ₹5.6L), L5 ₹168.3L (₹69.3L / ₹82.8L / ₹16.2L); highest reported ₹215.4L. Against the all-company Bengaluru ML distribution, Google L3 sits at about P51, L4 at about P71 and L5 above P90. ServiceNow's Hyderabad ML median is about ₹41.9–42.9L (P25 ₹30.8L, P90 ₹62.0L), roughly 1.4× the Hyderabad all-company median. [S48, S49]

**Table D3 — same-employer geography ratios (Google; Levels.fyi).**

| Level | Google US ML Engineer | Google Bengaluru ML Engineer | Ratio | Google US software engineer | Google UK software engineer | Ratio |
|---|---|---|---|---|---|---|
| L3 | $199–205K | ₹45.2L ≈ $47.5K | 0.23–0.24 | $214K | £123K ≈ $162.9K | 0.76 |
| L4 | $294–312K | ₹65.2L ≈ $68.5K | 0.22–0.23 | $315K | £164K ≈ $217.3K | 0.69 |
| L5 | $393–445K | ₹168.3L ≈ $176.7K | 0.40–0.45 | $448K | £224K ≈ $296.7K | 0.66 |
| L6 | $607–646K | not shown | n/a | not shown | £377K ≈ $499.4K | 0.77–0.82 against the US ML figure (title mismatch) |

Same-employer ratios (0.66–0.76 for the UK, 0.22–0.45 for Bengaluru) are higher than the all-company ratios (0.53 for London, 0.17 for Bengaluru), so a Big Tech or MNC offer should be benchmarked against this table rather than Table B. Caveats: the Google US software-engineer figures come from an index page about three months old; the UK figures are country-wide, not London; the Bengaluru samples are small (the L5 stock figure suggests few submissions); the Google US ML snapshots are undated. Anecdotal Blind posts (Grade D) put Google Zurich L5 total pay near CHF 360K and say Zurich stock grants run about half of US amounts; I did not find a Levels.fyi Google Zurich page. [S49, S50, S55]

**Table E — illustrative non-US P50 ranges for three Google-ladder anchors [MODEL, Grade D].** Method: the US anchor × the range of geography/US ratios at the percentiles the tier plausibly occupies (L3: P25–P50 ratios; L4: P50–P75; L7: P75–P90). Not for offers.

| Anchor (US total) | London | Zurich (C†) | Bengaluru (market-wide, not MNC-specific) |
|---|---|---|---|
| L3 $199K | $106–118K | $115–129K | $30–33K |
| L4 $294K | $157–164K | $169–194K | $49–55K |
| L7 $743K | $415–438K | $490–529K | $139–149K |

The Bengaluru column is a market-wide central estimate. Table D2 shows employer-level Bengaluru pay spanning ₹13L to ₹122L, so a product MNC will sit well above these values; Table D3 gives measured same-employer ratios that are higher (UK 0.66–0.76, Bengaluru 0.22–0.45).

### 6.6 Frontier-lab premium

| Comparison | Numerator | Denominator | Ratio |
|---|---|---|---|
| OpenAI SWE median vs US ML Engineer P50 | $875K | $280K | 3.1× |
| OpenAI SWE median vs SF Bay ML Engineer P50 | $875K | $327.9K | 2.7× |
| OpenAI SWE median vs US ML Engineer P90 | $875K | $497.5K | 1.8× |
| Anthropic SWE median vs US ML Engineer P50 | $882.5K | $280K | 3.2× |
| OpenAI Research Scientist median (cached) vs OpenAI SWE median | about $1.25M | $875K | 1.4× |
| OpenAI SWE median vs Google ML Engineer median across levels (cached, about $290–302K) | $875K | about $296K | about 3.0× |

**The premium is almost entirely equity.** Pave's P6 ML Engineering median base is $321K. OpenAI L5 base is $361K (+12%), Anthropic Lead $336K (+5%) and Anthropic Staff $403K (+26%). The mapping from Pave's P6 to lab levels is my assumption, but the order of magnitude is clear: frontier labs pay about 3× at total compensation and roughly 5–26% above the market in base for comparable senior roles. Pave's research-scientist finding points the same way (new-hire equity above $4M, base near ML Engineering). [S11, S12, S23]

**Gaps.** Levels.fyi has no pre-training or post-training specialisation, so "Research Scientist" is the only proxy. I read the OpenAI and Anthropic pages and the Google, Meta and Nvidia ML Engineer ladders (Table D); I did **not** retrieve Google DeepMind- or Meta FAIR-specific pages, so no verified premium is reported for them. Meta's ML Engineer median is $465K (n = 380, cached about five months), roughly 1.7× the US ML Engineer median and about half of the OpenAI figure. A secondary site's estimate built on Levels.fyi self-reports puts DeepMind London pay 30–40% below Mountain View in USD terms, with an L5 research scientist in London at £210–290K (Grade C). [S51, S55] Press reports of very large individual offers at Meta and elsewhere are **[RECALLED]** and were not re-verified in this session.

### 6.7 H-1B LCA evidence (regulatory strategy)

**What the primary source is.** The US Department of Labor's Office of Foreign Labor Certification publishes quarterly LCA disclosure files on its Performance Data page. The Q3 FY2026 release (decisions through 30 Jun 2026) appeared on 14 Aug 2026 according to an AILA practice alert. **I could not process the raw files**: the sandbox has no route to dol.gov (`Could not resolve host` for both dol.gov and flcdatacenter.com, and neither is on the egress allowlist), and I did not try to work around that. Everything below is third-party processing of the DOL data (Grade B). [S16]

| Employer | Source | Scope and method | Median offered wage | Notes |
|---|---|---|---|---|
| OpenAI OpCo, LLC | careery.pro [S17] | 311 certified H-1B LCAs, FY2025 + FY2026 through Q3; lower bound of wage range, annualised | **$270K** (FY2025 $285K, n = 101; FY2026 YTD $260K, n = 210) | Built from five DOL disclosure files |
| OpenAI OpCo, LLC | Visaverge [S18] | 210 certified LCAs, FY2026 YTD | $260K; middle half $245–325K | Most-filed title MTS-Software Engineer, median $255K |
| OpenAI OpCo, LLC | Ellis [S19] | 2025 positions (not filings) | **$310K** (average $307K) | Average prevailing wage $162K, so offered wages average about 1.9× the legal minimum |
| Anthropic PBC | careery.pro [S17] | 292 certified LCAs, FY2025 + FY2026 through Q3; lower bound | **$209K** (FY2025 $300K, n = 101; FY2026 YTD $190K, n = 191) | The FY2025→FY2026 drop is a filing-practice artefact, see below |
| Anthropic PBC | Visaverge [S18] | 191 certified LCAs, FY2026 YTD | $189.6K; middle half $169.5–213.5K | |
| Anthropic PBC | Ellis [S19] | 2025 positions | $280K overall (average $257.6K; average prevailing wage $167.6K) | MTS: 223 positions, median $315K; Research Engineer: 63 positions, median $215K; MTS (Manager): median $405K |

**OpenAI by title (Ellis, 2025 positions).**

| Title | Positions | Min | Median | Max |
|---|---|---|---|---|
| MTS (Software Engineer) | 107 | $170K | $255K | $490K |
| MTS (Research Engineer) | 84 | $210K | $335K | $530K |
| MTS (unspecified) | 83 | $200K | $310K | $650K |
| MTS (Research Scientist) | 68 | $245K | $360K | $685K |
| MTS (AI Systems Engineer) | 67 | $245K | $335K | $460K |
| MTS (Research & AI Systems) | 17 | $295K | $360K | $530K |
| MTS (Hardware Engineering) | 9 | $250K | $380K | $555K |
| MTS (Data Science) | 9 | $255K | $255K | $490K |

**How to read it.**
- **LCA wages are floors, and filing style moves the median.** Anthropic's lower-bound median fell from $300K (FY2025) to $190K (FY2026 YTD). A single Anthropic Research Engineer LCA (case I-200-25266-329882, submitted 23 Sep 2025) lists a base equal to its prevailing wage ($138,445) with a range up to $500,000. [S20] Lower-bound medians therefore understate pay whenever the floor is set at the legal minimum.
- **Cross-check against Levels.fyi base.** OpenAI Levels.fyi base runs $170K (L2) to $361K (L5), and the LCA title medians ($255–360K) fall inside that range. Anthropic's FY2026 lower-bound median ($190K) is below even the Levels.fyi entry-level base ($266K), which fits the floor artefact.
- **Aggregators disagree with themselves.** Ellis's two OpenAI pages give San Francisco medians of $180K and $310K. Treat all processed-LCA output as indicative until the raw file is reproduced.
- **Coverage.** LCAs cover visa-sponsored workers only, exclude bonus and equity, and Anthropic's titles are almost entirely "Member of Technical Staff". Seniority cannot be recovered.
- **Method for the local re-run [MODEL; field names recalled, Grade D, so check them against the file layout].** Filter VISA_CLASS = H-1B and CASE_STATUS = Certified; annualise wage units; take both the lower and upper bound; weight by worker positions; group by employer and a title regex (machine learning, AI, research, member of technical staff); report P25/P50/P75/P90 per employer and fiscal year.

### 6.8 India: Levels.fyi vs the broad market, and PPP vs nominal FX

**The spectrum of Indian sources (ML/AI engineer, annual total, ₹ lakh).**

| Source | Population | Figure | Grade |
|---|---|---|---|
| Levels.fyi Greater Bengaluru, ML Engineer | Self-reported, large-employer skew (n = 96) | P25 28.9 / P50 44.5 / P75 68.6 / P90 94.6 | A |
| Levels.fyi Greater Bengaluru, AI Engineer title | Same | P50 21.4 (base 20.3) | B |
| Levels.fyi Greater Hyderabad, ML Engineer | Self-reported, large-employer skew | P25 23.4 / P50 30.3 / P75 45.8 / P90 84.7 (base median 26.9) | B |
| AIM Research (2025) | Headline of a paywalled study | Median 12–15 | B |
| Glassdoor India, AI Engineer (Aug 2026, relayed) | Employee-reported, broad | Average base about 10 (range 6–15); average total about 12 | C |
| Glassdoor India, AI Developer (Jun 2026, n = 167, relayed) | Employee-reported | Average 6.95 | C |
| Indeed India, AI developer (Apr 2026, n = 79, relayed) | Job-posting weighted | Average 10.48 | C |
| Payscale, AI developer (relayed) | Employee-reported | Average base 4.5 | C |
| AmbitionBox via Codegnan, ML Engineer in Hyderabad (2026, about 7.1k records) | Employee-reported, broad | Average 11; senior about 20; lead about 25.5 | C |
| Recruiter and ed-tech guides (Weekday, Taggd) | Marketing-driven | Experienced at product companies and GCCs 38–65 (Weekday); senior at GCCs and top product companies 55–80+ (Taggd) | C |
| Flexiple (Aug 2026, URL not retained†) | Freelance and hiring platform pool | ML Engineer Bengaluru median 19.9 (n = 422) | C† |

**Reading.** The broad market (Glassdoor, Indeed, Payscale, AIM) centres on ₹10–15L, Levels.fyi ML Engineer on ₹44.5L, and recruiter-quoted senior product/GCC roles on ₹55–120L. The explanation is employer type, shown directly in Table D2 (Bengaluru senior SWE medians from ₹24.9L at Sony to ₹121.9L at X). The "₹50L–₹1Cr" claim is true for senior engineers at the top product MNCs and GCCs, and false as a statement about the median Indian AI engineer. Hyderabad shows the same shape: a Levels.fyi P50 of ₹30.3L against an AmbitionBox-based average near ₹11L.

**PPP vs nominal FX.**

| Bengaluru ML Engineer percentile | INR (lakh) | Nominal USD at ₹95.25 | PPP international dollars at ₹22.9 |
|---|---|---|---|
| P25 | 28.9 | $30.4K | Int'l$126K |
| P50 | 44.5 | $46.7K | Int'l$194K |
| P75 | 68.6 | $72.0K | Int'l$300K |
| P90 | 94.6 | $99.4K | Int'l$413K |

- **Two lenses on the US P50 ($280K).** At market FX it is ₹2.67 crore, 6.0× the Bengaluru P50. At PPP, the US P50 is 1.44× the Bengaluru P50, and its PPP-equivalent in India is about ₹64L, roughly P70 of the Bengaluru ML distribution. If the PPP factor is 15% lower or higher, that equivalent is ₹54–74L (about P60–P78).
- **Which lens applies.** Market FX governs savings in dollars, remittances, foreign education, imported goods and anything priced globally. PPP governs local consumption of non-tradables (housing, services, food). A real decision needs after-tax pay in both countries, US cost of living by city and visa constraints; none of that was researched.
- **Currency drift.** USD/INR was about 95.2 on 19 Oct 2026, with the rupee roughly 8.3% weaker than a year earlier (Trading Economics) and a record-low close near 96.8–96.9 on 8 Oct (Investing.com history and a trading blog). A fixed-USD offer is worth about 8–9% more in rupees than a year ago, which flatters foreign offers in rupee terms but not in PPP terms. [S30, S31]
- **PPP data quality.** The World Bank WDI indicator page (PA.NUS.PPP) was reached but its values were not read. The ₹22.9 figure comes from a study-notes site describing an extrapolated 2021 ICP round; another aggregator shows 22.0 for 2020 on the older 2011 round. PPP factors drift with relative inflation, and the 2026 value was not retrieved (Grade C). [S32]

### 6.9 India-based contractor rates

**What was found (all Grade C; no platform-native percentile data).**

| Source (Sep–Oct 2026) | Quote |
|---|---|
| Second Talent cost-to-hire pages | Mid-level India AI/ML engineer "observed" freelance rate $28–72/h ($4,480–11,520 per month at 160 billable hours). Platform ranges as relayed: Upwork $25–150/h, Toptal $70–200/h, Arc $61–100/h |
| Second Talent India rate card | AI Engineer: junior $25–35/h (international client) or $31–44/h (freelance); mid-level (3–6 years) $35–50/h or $44–63/h; senior $50–75/h from international clients. ML Engineer mid-level $32–45/h or $40–56/h. Freelance rates run about 25% above equivalent contract rates, per the vendor (no reason given) |
| Opsio rate-card blog | India AI/ML engineers at mid-level $35–50/h |
| PerfectionGeeks guide | India or Eastern Europe $30–80/h for skilled ML engineers |

**Conversion to annual rupee terms and position against Levels.fyi Bengaluru ML full-time pay.**

| Hourly (USD) | Monthly at 160 h | Annual (USD) | Annual (₹ lakh, ₹95.25) | Position at 160 h/month | Position at 120 h/month |
|---|---|---|---|---|---|
| $28 | $4,480 | $53,760 | 51.2 | about P57 | about P44 |
| $35 | $5,600 | $67,200 | 64.0 | about P70 | about P54 |
| $50 | $8,000 | $96,000 | 91.4 | about P88 | about P75 |
| $63 | $10,080 | $120,960 | 115.2 | above P90 | about P85 |
| $72 | $11,520 | $138,240 | 131.7 | above P90 | above P90 |

The 120 h/month column approximates 75% billable utilisation. Contract income carries no benefits, paid leave or employer provident-fund contribution, so a contractor needs a materially higher gross than a full-time employee to match the same take-home.

**Not researched.** W-8BEN is the form a foreign payee gives a US client to certify foreign status and claim treaty benefits **[RECALLED, Grade D]**; Indian tax treatment of such receipts, FEMA/FIRC mechanics and GST were not researched. Get a chartered-accountant opinion before relying on any net figure. Remotive and Wellfound were not retrieved at primary level, and Turing and Toptal rates are known only through vendor relays.

### 6.10 GCC (Dubai, Abu Dhabi)

| Source | Role and level | Monthly (AED) | Annual USD at 3.6725 | Grade |
|---|---|---|---|---|
| Aggregator citing Michael Page UAE guide 2026 (URL not retained†) | Mid-level AI/ML engineer, Dubai | 25,000–45,000 (average 35,000) | $81.7–147.0K (average $114.4K) | C† |
| Same aggregator, Abu Dhabi | Mid-level AI/ML engineer | 23,750–42,750 (average 33,250) | $77.6–139.7K | C† (exactly 0.95× Dubai) |
| Edoxi (12 Aug 2026) | Entry | 15,000–25,000 | $49.0–81.7K | C |
| Edoxi | Mid | 25,000–40,000 | $81.7–130.7K | C |
| Edoxi | Senior / lead | 40,000–65,000+ | $130.7–212.4K+ | C |
| Levels.fyi, Dubai Software Engineer (all levels, not ML; undated) | P25 / P50 / P75 / P90 | 20,000 / 25,003 / 35,838 / 45,500 | $65.4K / $81.7K / $117.1K / $148.7K | B (proxy) |
| Glassdoor Dubai, ML Engineer (n = 19), relayed | P25 / median / P75 | 10,400 / 15,400 / 20,400 | $34.0K / $50.4K / $66.8K | C |
| Naukrigulf Dubai, ML Engineer (n = 32), relayed | Average | 7,618 | $24.9K | C |
| Indeed UAE, all levels, relayed | Average | 6,195 | $20.2K | C |

- **Two populations again.** Levels.fyi's Dubai software-engineer median (about AED 25K a month) matches the low end of the recruiter band for mid-level AI/ML (AED 25–45K), while the broad market sits at about AED 6–15K a month, a 2–4× gap like those in India and NYC.
- Edoxi also cites SalaryExpert at about AED 309K a year for Dubai and about AED 304K for Abu Dhabi (ratio 0.98), which contradicts the mechanical 0.95 pattern above.
- Arabian Business reports that Michael Page's 2026 UAE guide found pay rises of 4–6% in 2025, sharpest in AI engineering and product management. A lifestyle site cites Korn Ferry for 8–15% AI/ML pay rises in 2026 (Grade C, unverified).
- **Unknowns.** Whether quoted monthly figures are basic salary or total package (housing and transport allowances are common in the region **[RECALLED, Grade D]**); employer type; nationality-linked pay differences. No current Levels.fyi UAE ML page (the Dubai ML/AI page is about two years old), Cooper Fitch or Korn Ferry document was read. I first rejected the Indeed UAE and Glassdoor Dubai pages as implausible; on a second look they describe a lower-paid broad market (about AED 6–15K a month), and the Glassdoor Dubai pages label a monthly figure as annual, so the fault was in the page labels, not the population.

### 6.11 Europe and Singapore

- **London.** Levels.fyi ML Engineer (A): £89.5K / £112.6K / £163K / £221K at P25/P50/P75/P90, with a base median of £95.2K. WTW's broad mid-level sample puts the UK just under $100K (about £75K), which is plausible as a broad-market figure beside a self-selected Levels.fyi P50 of $149K.
- **Berlin and Germany.** The only Levels.fyi Berlin ML page found is stale (25 Jul 2025; $86.7K / $97.7K / $106K / $114K). WTW gives Germany about $122K for mid-level ML roles, which is above that stale Berlin P50, so the Berlin row should not be used.
- **Zurich.** Levels.fyi excerpt (C†): CHF 108K / 134K / 211K / 295K. Robert Half Switzerland's 2026 guide (Grade B/C; starting salaries of candidates it placed, base only, excluding bonus, currency not printed in the excerpt and presumed CHF): ML Engineer P25/P50/P75 = 106,000 / 121,900 / about 140,450; AI Engineer 106,000 / 132,500 / 159,000; AI/ML System Performance Specialist 106,000 / 137,800 / 159,000; MLOps 95,400 / 116,600 / 137,800; AI Developer 90,100 / 116,600 / 137,800. The Levels.fyi P25 (CHF 108K) and the Robert Half P25 (CHF 106K) agree; the gap opens above the median because Big Tech equity is absent from a base-only placement guide. [S39]
- **Singapore.** Levels.fyi Software Engineer, all levels (A, proxy, not ML): SGD 84.9K / 114.8K / 163.0K / 215.0K (n = 1,362). The senior-level page (2 Apr 2026, Grade B proxy) shows SGD 129K / 180.5K / 234K / 298K, about 0.47–0.50× the US ML Engineer distribution in USD. One employer's ML ladder: ByteDance ML Engineer (Levels.fyi, last updated 2 Nov 2025, Grade B) has total compensation of SGD 126.8K / 201.4K / 230.5K / 242.1K at P25/P50/P75/P90 (median about $157K), with a median split of base SGD 145.1K (72%), bonus SGD 36.3K (18%) and equity SGD 20.0K (10%), so it is mostly cash. Cash-market cross-checks (Grade C): Indeed Singapore reports an average ML Engineer base of S$8,648 a month (n = 157; 21 Sep 2026; P10 S$4,247, P90 S$17,613), about S$104K a year, and a job-ad-based JobStreet Singapore page (URL not retained†) shows S$9,000 a month at the median. The ML premium over software engineers in Singapore was not measured. [S09, S53]
- **NYC contrast (Grade C).** Payscale's New York ML Engineer page puts base median at about $135K and total pay from about $92K (P10) to $189K (P90), against Levels.fyi NYC P90 of $460K, a 2.4× gap of the same type as in India. [S06, S21]

### 6.12 Equity: liquid vs paper, and the discount model

**Definition.** DF = value to the employee ÷ grant-date paper mark. The model values only the equity term; base and bonus pass through at par.

**Parameters and provenance.**

| Parameter | Value used | Source | Grade |
|---|---|---|---|
| DLOM, restricted-stock studies | About 34% (Silber: 69 placements, 1981–88, average 33.75%); aggregate about 35% | Acquiry; Damodaran (NYU Stern) | B |
| DLOM, pre-IPO studies | 46% mean, 47% median (Emory, 1980–2000) | Acquiry | B |
| DLOM overall range | 5–50%; BDO notes a higher DLOM can apply to common than preferred (employees hold common) | BDO | B |
| Tender price vs last round | 0% observed: OpenAI's Aug 2026 tender at $852B equals its March round; Anthropic's at $350B pre-money equals the Series G price. 5% friction assumed | Tender sources | B observed; D assumed |
| Sellable fraction of frontier-lab stock | 25–75% (per-person caps and share of vested stock sold are not reported) | none | D |
| P(liquidity), Series A/B | 0.25–0.50, anchored on Carta Series A→B graduation: about 28% within 2 years in a normal cohort (2018), about 40% within 3 years, "about half" in a strong cohort. Downside cohorts (2022) saw 9–15% within 2 years | Carta Insights | B anchor; D mapping |
| Retention after dilution | 0.60–0.75 (Series A/B hire); 0.85–0.95 (late stage). Per-round dilution about 18–23% | Carta medians via secondary relays† | C/D |
| Upside multiple m, conditional on liquidity | 1.0 (haircut view) or 2.5 (illustrative upside view) | none | D |
| Time value | 12% a year over 5 years (factor 0.567) for Series A/B; over 3 years (0.712) for late stage | none | D |

DLOM is not applied on the startup hold-to-exit path (liquidity arrives at exit) so it is not double-counted with P(liquidity).

**Discount factors.**

| Archetype | Construction | DF |
|---|---|---|
| Public RSU | Price volatility only | **0.95–1.00** |
| Frontier lab with tenders | s × (1 − 5%) + (1 − s) × (1 − DLOM 34–47%), s = sellable fraction | **0.64–0.88** (s = 25%: 0.64–0.73; 50%: 0.74–0.81; 75%: 0.85–0.88) |
| Late-stage private (Series C+) | P 0.70–0.90 × retention 0.85–0.95 × 0.712 × m | m = 1: **0.42–0.61**; m = 1.5: 0.64–0.91 |
| Series A/B startup | P 0.25–0.50 × retention 0.60–0.75 × 0.567 × m | m = 1: **0.09–0.21**; m = 2.5: **0.21–0.53** |
| Series A/B, downside cohort | P = 0.12 | m = 1: about 0.04–0.05 |

**Cash-equivalent examples (frontier DF 0.635–0.878; stock term only discounted).**

| Package (Levels.fyi, US) | Headline TC | Cash-equivalent TC | Share of headline |
|---|---|---|---|
| Anthropic Staff | $1.41M | $1.04–1.29M | 74–91% |
| Anthropic Lead | $865K | $673–801K | 78–93% |
| Anthropic Senior | $621K | $510–584K | 82–94% |
| OpenAI L5 | $911K | $710–844K | 78–93% |
| OpenAI L4 | $768K | $601–712K | 78–93% |
| Google ML L4 (public RSU, DF 0.95–1.00) | $294K | $290–294K | 98–100% |
| Carta AI-native example: $320K salary + 0.146% of a $500M floor valuation over 4 years (late-stage DF 0.42–0.61, m = 1) | $502.5K paper TC | $397–431K | 79–86%; equity is 20–26% of cash-equivalent TC |

**Per $100K a year of paper equity at a Series A/B AI startup:** about $9–21K of cash-equivalent value in the haircut view and $21–53K if upside is credited.

**Observations behind the numbers.**
- *Frontier labs.* OpenAI completed a $6.6B tender at $500B in Oct 2025 and a roughly $7B company-funded buyback at $852B around 10 Aug 2026; Anthropic completed a tender at $350B pre-money in early April 2026 for current and former staff with at least 12 months of tenure, with outside investors buying. At Anthropic employees sold less than investors wanted, which suggests access to liquidity was not the binding constraint for those who wanted it. Reporting does not say how much of an employee's vested stock could be sold. OpenAI filed confidentially for an IPO in June 2026; the NYT later reported it was weighing a delay. [S28, S29]
- *Where the "paper" label misleads.* At these two labs the stock has been repriced several times upward in two years, and sale prices have matched the last round, so grant-date marks understate or overstate value depending on grant timing. Levels.fyi's stock-per-year figures do not state whether they use grant-date or current valuation.
- *Startups.* Carta (Feb 2026): median equity grants for AI/ML engineers rose 59% at startups valued $1–10M and 30% at $25–50M between Jan 2024 and Feb 2026; at AI-native startups above $500M the P80–95 AI/ML engineer receives about $320K salary and 0.146% equity, against $285K and 0.10% at non-AI-native peers. A secondary relay of Carta puts initial AI/ML equity up 31% against salary up 9.1% over the same period (Grade C). Axial's 43,480 US postings mention equity in 14% and a bonus in 31%, and the firm notes these rates are floors. [S25, S36]
- *Pave's reading.* Median base is similar across AI job families at the same level, recent hires receive up to about 10% more base than incumbents, and the 90th-percentile new-hire equity package is $45–60M at the most senior levels at private SF Bay companies that raised $1B–$5B+. [S23]

**Limits.** Every DF above is a model output. The three sourced inputs (DLOM, graduation, dilution) are real but proxy for an employee's actual outcome; P(liquidity), sellable fraction, upside multiple and discount rate are assumptions. Treat the table as a way to compare packages on a common footing, not as a valuation.

### 6.13 Infrastructure/systems vs application-layer premium

| Evidence | Systems/infra side | Generic or application side | Premium | Scope | Grade |
|---|---|---|---|---|---|
| OpenAI LCAs, 2025 | MTS-AI Systems Engineer median $335K (67 positions) | MTS-Software Engineer $255K (107) | +31% | Base; one employer | B |
| OpenAI LCAs, 2025 | MTS-Research Engineer $335K (84) | MTS-Software Engineer $255K | +31% | Base; one employer | B |
| Robert Half Zurich, 2026 | AI/ML System Performance Specialist P50 CHF 137.8K | AI Developer CHF 116.6K | +18% (P25 +18%, P75 +15%) | Starting base; one city | B/C |
| Robert Half Zurich, 2026 | Same | ML Engineer CHF 121.9K | +13% | Starting base; one city | B/C |
| Robert Half Zurich, 2026 | AI Engineer CHF 132.5K | AI Developer CHF 116.6K | +14% | Starting base | B/C |
| Robert Half Zurich, 2026 | MLOps CHF 116.6K | AI Developer CHF 116.6K | 0% | Starting base | B/C |
| Pave, 2026 (US, $200–500M raised) | Senior (P4) ML median base $210K | Software-engineering generalist $196K | +7% | Base | A/B |
| Levels.fyi US titles | ML Engineer P50 $280K | AI Engineer P50 $154K | +82% | Total comp; composition effect | A |
| Google (Levels.fyi, US, same employer) | ML Engineer median $302–333K (two snapshots) | AI Engineer median $240K (n = 38; page about 13 months old) | +26% to +39% | Total comp; title premium within one employer | B |
| Levels.fyi Bengaluru titles | ML Ops P50 ₹23.6L† | AI Engineer P50 ₹21.4L | +10% | Total comp | C† |
| Levels.fyi analysis relayed by Pin (Q3 2025) | AI-skill premium over non-AI peers: +6.2% entry, +11.9% mid, +14.2% senior, +18.7% staff | | | Relay | C |
| Vendor guides (Leon Staff, Neuronify, Ayautomate, Recruitslab, Creww) | Claimed 20–35% for vLLM/TensorRT-LLM/CUDA | | unsourced | | C/D |

**Verdict.** A base-pay premium of roughly 13–31% for systems and research-engineering titles over generic software or "AI developer" titles shows up in two independent datasets, and a 7–19% ML-over-generic-SWE premium shows up in two more. That supports the vendor range qualitatively but not as a validated 20–35% for inference skills. What would validate it: total compensation (not base) by sub-specialty with seniority controlled. What blocks it: no public dataset isolates vLLM, TensorRT-LLM or Triton skills from application-layer AI work, "Member of Technical Staff (AI Systems Engineer)" may be more senior than the software-engineer title, and LCA wages are floors. At frontier labs the research-vs-engineering gap sits in equity (Pave), not base. Within one employer (Google), the ML Engineer title earns 26–39% more than the AI Engineer title, so about half of the US 1.8× title gap is employer mix.

### 6.14 Tool catalogue

| Tool | What it is | Verified this session | Role here |
|---|---|---|---|
| Levels.fyi | Crowdsourced total-comp percentile pages; `.md` structured exports; API, MCP and CLI advertised on the site; attribution required | Yes (pages opened) | Primary anchor |
| DOL OFLC LCA disclosure data | Official quarterly wage-filing files | Page confirmed; files unreachable from my sandbox | Base-wage floor; process locally |
| Third-party LCA browsers (Ellis, careery.pro, Visaverge, h1bdata.net, MyVisaJobs) | Processed DOL data; methods differ | Pages opened or excerpted | Cross-check only |
| Pave (with Nua Group) | Compensation platform; 9,000+ companies including 80% of the Forbes AI 50 | Press release | Base and equity by job family |
| Carta | Cap-table-derived startup compensation, equity and funding-stage data | Insights posts opened | Startup equity, graduation, dilution |
| Radford McLagan (Aon) | Paid global survey; added AI job families (Head of AI, Applied Research Scientist, ML Engineer, AI Ethics) on 31 Mar 2026; about 30M employees, 115 countries per Aon | Announcements only; data paywalled | Recommended purchase |
| WTW AI and Digital Talent Salary Survey | Ten-country survey, press summary | Press release | Cross-country mid-level medians |
| Comprehensive.io | Pay-transparency crawler of US tech job postings (base ranges); Mercer partnership for global coverage | Methodology only (URLs not retained†); no AI percentile page found | Not used for numbers |
| Candor | Named in the brief | Searched; nothing located | Unverified |
| Autograph "Fair Offer" | Algorithmic compensation range and equity valuation tool (v3 handles bonuses and price per share) | Listing only | Equity calculator; accuracy unvalidated |
| Carta Startup Equity Calculator, Cake Equity Benchmark Calculator, Equitybee Benchmark (9,000+ verified joining grants, 2,500+ US startups) | Equity calculators and benchmarks | Listings only | Equity cross-checks |
| Recruiter guides (Michael Page, Cooper Fitch, Robert Half, Hays) | Placement-based or survey salary guides | Robert Half Zurich page read; Michael Page UAE only through relays | Regional cross-checks |
| Glassdoor, Payscale, Indeed, AmbitionBox | Broad crowdsourced | Relays only | Population contrast |
| Arc, Upwork, Toptal, Turing | Contractor marketplaces | Vendor relays only | Not primary |

### 6.15 DONE-criteria scorecard

| Criterion | Status | What exists | What is missing |
|---|---|---|---|
| Multi-geo tables (US, UK, EU, India, Singapore) across all six tiers with P25/P50/P75/P90 | **Partial** | All-level P25–P90 for US (two titles), SF Bay, NYC, London, UK-wide, Bengaluru and Hyderabad (A/B); Zurich and Berlin at Grade C; Singapore and Dubai as software-engineer proxies; tier anchors for Google, Meta, Nvidia, OpenAI and Anthropic; senior-level software-engineer percentiles for Singapore and Bengaluru; same-employer geography ratios (Table D3) | Tier-conditional ML percentiles for every geography; a current Dubai/Abu Dhabi ML series; OpenAI L6/L7 values |
| Base decoupled from bonus and equity for all roles | **Met where the sources expose components** | Ladder-level splits (Google, OpenAI, Anthropic); medians for NYC, London, Bengaluru, Zurich; four-component archetype table | Splits for GCC, Singapore, contractors, Indian ESOPs |
| Contractor hourly and monthly USD rates for India-based talent from primary platform data | **Unmet** | Vendor-relayed ranges and conversions (Grade C) | Platform-native rate distributions; tax treatment |
| Equity discount factor modelled quantitatively | **Met (model)** | Parametric DF with sourced inputs and four archetypes; cash-equivalent examples | Calibration of P(liquidity), sellable fraction, upside multiple |
| Infra/systems vs application premium empirically validated | **Partial** | +13% to +31% base premia in OpenAI LCAs and Robert Half Zurich; +7% to +19% ML over generic SWE | Total-comp evidence; skill-level isolation; market-wide data |

---

## 7. Open Questions & Risks

### 7.1 Open questions

1. **Tier-conditional distributions per geography.** Levels.fyi exposes level-by-location pages (the path pattern exists), but I did not retrieve them for ML/AI titles. This is the main blocker for the six-tier grid.
2. **Raw DOL reproduction.** Process the FY2026 Q3 LCA file locally (method in section 6.7) and compare against the third-party figures; the sandbox could not reach dol.gov.
3. **Platform-native contractor data and tax.** Arc, Toptal, Turing and Upwork rate distributions for India-based AI engineers; W-8BEN, Indian income tax, FEMA/FIRC and GST treatment (none researched).
4. **GCC primary data.** The Michael Page UAE and Cooper Fitch guides themselves; whether monthly figures are basic or total package; a current Levels.fyi or equivalent ML-specific Dubai and Abu Dhabi series (the Dubai ML/AI page found is about two years old; only an all-levels software-engineer page is current).
5. **Singapore ML-specific percentiles** (Levels.fyi city page, MOM, MyCareersFuture); only software-engineer proxies and one employer's ML ladder were found.
6. **Germany.** A current Berlin/Munich ML series; the Berlin page found is from July 2025.
7. **Remote markets.** Percentile sources for US Remote, Indian Remote and International Remote; Remotive and Wellfound were not retrieved at primary level; Cutshort and the Michael Page India technology salary report were not retrieved.
8. **Equity calibration.** Carta exit-outcome distributions, secondary-market discounts for common stock, tender caps and participation, and the legal mechanics of OpenAI and Anthropic equity (Levels.fyi labels OpenAI stock as RSUs now; older cached copies of the page said PPUs, and I did not verify the conversion).
9. **Meta FAIR and Google DeepMind.** Meta, Google and Nvidia ML Engineer ladders were read, but no FAIR- or DeepMind-specific pages, so no verified premium is reported for them.
10. **Hyderabad by level.** All-level ML percentiles were found in the second pass; per-level Hyderabad data was not.
11. **Radford McLagan** AI job-family cuts (paywalled).
12. **Drift.** Levels.fyi pages update continuously. Re-pull the anchors in about 30 days.
13. **Licence.** Confirm the Levels.fyi Data License permits redistributing the derived tables in this file.

### 7.2 Strongest objections an expert would raise, and what the evidence says

| # | Objection | Evidence for | Evidence against or mitigation | Net |
|---|---|---|---|---|
| 1 | "Levels.fyi is self-reported and skews high; its India figures describe MNCs, not the market." | Bengaluru ML P50 ₹44.5L vs ₹4.5–15L in Glassdoor, Indeed, Payscale and AIM; NYC Levels.fyi P90 $460K vs Payscale P90 $189K; anecdotal Blind critiques (Grade D) | US ML P50 ($280K) sits near Pave's P6 ML base ($321K) for large-company customers; Levels.fyi Zurich P25 (CHF 108K) matches Robert Half's P25 (CHF 106K); no quantitative bias study was found | **Valid for India and for any "market median" claim.** Both populations are shown side by side |
| 2 | "Titles are not comparable and 'GenAI' is not 'ML'." | The AI Engineer title sits at a constant 0.55× of ML Engineer across percentiles, which signals composition; Anthropic titles are flattened to "Member of Technical Staff"; Levels.fyi has no GenAI title | None | **Valid.** All findings are title-proxy findings and are labelled so |
| 3 | "Frontier-lab medians come from small, drifting samples." | OpenAI n = 242, Anthropic n = 49; cached OpenAI SWE medians range $555K–$875K; wide within-lab dispersion (cached P10 $380K to P90 $1.585M) | OpenAI and Anthropic pages agree with each other ($875K, $882.5K) and with the LCA base scale; a roughly 3× ratio to the ML Engineer median survives ±25% noise | **Valid for point estimates; the order of magnitude holds** |
| 4 | "LCA wages understate pay." | Anthropic lower-bound median fell $300K → $190K; a record with base equal to prevailing wage and a $500K upper range; Ellis's two OpenAI pages disagree on San Francisco | OpenAI LCA title medians sit inside the Levels.fyi base range; offered wages average 1.9× prevailing wage at OpenAI | **Valid.** LCA is used only as a floor and for within-employer comparison |
| 5 | "Stock per year may reflect grant-date or current marks; repricing makes frontier TC unstable." | Levels.fyi does not state its basis; OpenAI's mark moved from $500B (Oct 2025 tender) to $852B (Mar 2026 round and Aug 2026 tender) | Tender prices equalled the last round, with no visible discount | **Valid and unresolved** |
| 6 | "PPP is the wrong lens for engineers who save in dollars." | Both lenses are shown; the rupee is about 8.3% weaker year on year | None | **Valid.** After-tax and cost-of-living analysis is still needed |
| 7 | "The discount model invents parameters." | P(liquidity), sellable fraction, upside multiple and discount rate are assumptions; DF ranges are wide (0.09–0.53 for startups) | DLOM, graduation and dilution inputs are sourced; DLOM is not double-counted on the hold-to-exit path; a downside cohort is shown (0.04–0.05) | **Valid.** Outputs are Grade D and meant for comparison, not valuation |
| 8 | "The infra premium is confounded by seniority and by who gets a systems title." | AI Systems Engineer titles at OpenAI may be more senior than "Software Engineer"; the Zurich guide is placement-based starting pay | Two independent datasets agree in sign and rough size (+13% to +31%); Pave shows +7% for ML over generic SWE | **Partly valid.** Reported as partially supported |
| 9 | "GCC figures are SEO aggregators." | One Abu Dhabi band is exactly 0.95× Dubai; broad-market pages (Indeed, Glassdoor, Naukrigulf) sit 2–4× below the recruiter bands | A second aggregator shows Abu Dhabi at 0.98× Dubai from a different source; Arabian Business corroborates the Michael Page guide's existence and AI-engineering pay growth; Levels.fyi's Dubai software-engineer median (about AED 25K a month) matches the low end of the recruiter band | **Valid.** Grade C |
| 10 | "These numbers will move." | The Bengaluru ML median differed between a cached copy (₹42.5L) and the live page (₹44.5L); the OpenAI stock-type label differed between copies | None | **Valid.** Re-pull in 30 days |

### 7.3 Risks

- **Mis-ingestion.** The Levels.fyi `.md` exports mislabel location for non-US pages, and a Miami page returned under a "United States" header; validate currency and location before loading them.
- **Over-reading Grade C rows.** The GCC, contractor, Zurich and Berlin rows are indicative only.
- **Frontier-lab valuation and liquidity risk.** The NYT reportedly flagged a possible OpenAI IPO delay; a relay described the August 2026 tender as the first flat valuation print in its run (Grade C). Tender caps and eligibility can change.
- **FX.** The rupee is volatile (record low near 96.8–96.9 on 8 Oct 2026), which moves every rupee-denominated comparison.
- **US immigration policy.** One news relay mentions a $100,000 H-1B fee; I did not verify its scope or status, and it matters for any Indian engineer evaluating a US offer.

---

## 8. Delta (belief change)

| # | Prior (recalled, Grade D) | What the evidence says | Verdict | Evidence grade |
|---|---|---|---|---|
| 1 | US ML Engineer P50 $250–300K, P90 about $500K; AI Engineer lower | ML Engineer $280K / $497.5K; AI Engineer $154K / $280K, a constant 0.55× | **Confirmed**; the title gap is larger than expected | A |
| 2 | OpenAI and Anthropic medians $700–900K; stock at least half of TC from senior levels | $875K and $882.5K; stock is 59–60% at OpenAI L4–L5, 49% at Anthropic Senior and 61–72% at Lead/Staff | **Confirmed**, with Anthropic Senior just under half | A |
| 3 | Bengaluru ML P50 ₹35–50L; broad market ₹10–25L | ₹44.5L; broad market ₹4.5–15L (AIM ₹12–15L; Flexiple ₹19.9L†) | **Confirmed**; the broad-market centre is at the low end | A/C |
| 4 | London 0.5–0.6×, Zurich 0.55–0.7×, Bengaluru 0.12–0.2× of US at P50 | 0.53, 0.58 (C†), 0.17 | **Confirmed**; Bengaluru's ratio understates product-MNC pay (Table D2) | A/C |
| 5 | Infra/inference premium 15–35%, mostly in equity | Base-only premia of +13% to +31% in two datasets and +7% to +19% for ML over generic SWE; no equity or skill-level evidence | **Partly supported, not validated**; "mostly equity" is untested | B/C |
| 6 | (Half-expected from blogs) Levels.fyi "AI Engineer" around $245K | Primary page P50 $154K, P90 $280K; the blogs' figure may be a mean or an older vintage | **Contradicted as a median; unresolved as a mean** | A vs C |
| 7 | OpenAI equity is illiquid paper | Two employee tenders ($500B in Oct 2025; $852B in Aug 2026, the latter company-funded), priced at the last round; Anthropic tender at $350B; Levels.fyi now labels OpenAI stock as RSUs | **Updated:** semi-liquid; modelled DF 0.64–0.88 | B |
| 8 | Employees at frontier labs sell eagerly into tenders | Anthropic employees sold less than investors wanted | **Updated** | B |
| 9 | LCA medians for both labs near $300K | OpenAI $260–310K; Anthropic FY2026 lower-bound median $190K because floors equal prevailing wage | **Updated:** filing practice dominates | B |
| 10 | (Self-correction) My first-pass note had OpenAI AI Systems Engineer LCA median at $252.5K | The opened Ellis page shows $335K | **Corrected**; this moved my provisional infra-premium read from "none" to "partly supported" | B |
| 11 | Hyderabad ML is about 0.89× Bengaluru (my software-engineer-based proxy) | Measured Levels.fyi Hyderabad ML P50 ₹30.3L is 0.68× Bengaluru (P25 0.81, P75 0.67, P90 0.89) | **Contradicted** (my proxy); direct data now used | B |
| 12 | Glassdoor, Indeed and Naukrigulf Dubai figures are implausible | They describe a lower-paid broad market (about AED 6–15K a month) and the Glassdoor pages label a monthly figure as annual | **Corrected** | C |
| 13 | All-company geography ratios (London 0.53, Bengaluru 0.17) describe what a given employer pays abroad | Same-employer ratios are higher: Google UK 0.66–0.76× its US pay, Google Bengaluru 0.22–0.45× | **Updated:** employer mix explains much of the all-company gap | B |

---

## 9. Sources & Evidence Ledger

† = URL not retained or only an excerpt seen in search results on 21 Oct 2026; re-locate before relying on it. Levels.fyi data requires attribution: Data source: Levels.fyi (https://www.levels.fyi).

| ID | Source | URL(s) | As of / type | Used for | Grade |
|---|---|---|---|---|---|
| S01 | Levels.fyi, AI Engineer (US) | https://www.levels.fyi/t/software-engineer/title/ai-engineer ; https://www.levels.fyi/t/software-engineer/title/ai-engineer.md | Opened; updated 18–19 Oct 2026; n = 335 | F1, Tables A–B, 6.13 | A |
| S02 | Levels.fyi, Machine Learning Engineer (US) | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer ; https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer.md | Opened; updated 19 Oct 2026; n = 1,063 | F1–F4, Tables A–B | A |
| S03 | Levels.fyi, ML Engineer, Greater Bengaluru | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/greater-bengaluru ; https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/greater-bengaluru.md | Opened; updated 12 Oct 2026; n = 96 | F3, Tables A–B, 6.8 | A |
| S04 | Levels.fyi, ML Engineer, Greater London | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/london-metro-area | Opened; updated 15 Oct 2026; base figures from a cached excerpt | F2, Tables A–C | A (totals), B (base) |
| S05 | Levels.fyi, ML Engineer, SF Bay Area | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/san-francisco-bay-area | Search excerpt, 14 Oct 2026; page not opened in full | F2, F4, Tables A–B | B |
| S06 | Levels.fyi, ML Engineer, NYC area | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/new-york-city-area | Structured-data excerpt; undated | F2, Tables A–C | B |
| S07 | Levels.fyi, ML Engineer, Zurich | URL not retained† | Structured-data excerpt; undated | F2, Tables A–B, C2 | C† |
| S08 | Levels.fyi, ML Engineer, Berlin | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/berlin-metropolitan-region | Excerpt dated 25 Jul 2025 | Table A (stale) | C |
| S09 | Levels.fyi, Software Engineer, Singapore (all levels) | https://www.levels.fyi/t/software-engineer/locations/singapore.md | Opened; 18 Oct 2026; n = 1,362 | Tables A–B, 6.11 | A (proxy) |
| S10 | Levels.fyi, Bengaluru: AI Engineer page; ML Ops, aggregated entry and senior SWE pages, and top-paying-locations table | https://www.levels.fyi/t/software-engineer/title/ai-engineer/locations/greater-bengaluru ; other URLs not retained† | Excerpts; AI Engineer 18 Oct 2026; others cached | F3, Tables A, D2, 6.2, 6.13 | B / C† |
| S11 | Levels.fyi, OpenAI Software Engineer (US) | https://www.levels.fyi/companies/openai/salaries/software-engineer | Opened; updated 20 Oct 2026; n = 242 | F4, F5, F8, Tables C1, D | A |
| S12 | Levels.fyi, Anthropic Software Engineer (US) | https://www.levels.fyi/companies/anthropic/salaries/software-engineer (opened via https://levels.fyi/company/anthropic/salaries/software-engineer) | Opened; updated 24 Sep 2026; n = 49 | F4, F5, F8, Tables C1, D | A |
| S13 | Levels.fyi, Google ML Engineer (US) | https://www.levels.fyi/hi-in/companies/google/salaries/software-engineer/title/machine-learning-engineer | Excerpt; updated 4 Aug 2026 | F5, Tables C1, D | B |
| S14 | Levels.fyi, Research Scientist pages | https://www.levels.fyi/companies/openai/salaries/software-engineer/title/research-scientist ; Anthropic page URL not retained† | Cached excerpts, undated | F4, 6.5, 6.6 | B / C† |
| S15 | Levels.fyi, Bengaluru company pages (X, LinkedIn, Microsoft, SAP, Fidelity Investments, Sony) | https://www.levels.fyi/companies/x/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/linkedin/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/microsoft/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/sap/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/fidelity-investments/salaries/software-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/sony/salaries/software-engineer/locations/greater-bengaluru | Excerpts seen in search results | F3, Table D2 | B |
| S16 | US DOL, Office of Foreign Labor Certification, Performance Data (LCA disclosure files); AILA practice alert on the Q3 FY26 release (title: "OFLC releases public disclosure data and selected program statistics for Q3 of FY26"; URL not retained†) | https://www.dol.gov/agencies/eta/foreign-labor/performance | Page confirmed; Q3 FY26 files released 14 Aug 2026; files not downloaded | 6.7 | A (page) |
| S17 | careery.pro, H-1B sponsor pages (DOL files FY2025 Q1–Q4 and FY2026 Q3) | https://careery.pro/h1b-sponsors/openai-opco-llc ; https://careery.pro/h1b-sponsors/anthropic-pbc | Search excerpts, Oct 2026 | F6, 6.7 | B |
| S18 | Visaverge, H-1B sponsor pages | https://www.visaverge.com/h1b-sponsors/openai-opco/ ; https://www.visaverge.com/h1b-sponsors/anthropic-pbc/ | Search excerpts (decisions through 30 Jun 2026) | F6, 6.7 | B |
| S19 | Ellis, H-1B sponsor pages (2025 positions) | https://www.ellis.com/visa-sponsors/openai-opco-llc ; https://www.ellis.com/visa-sponsors/openai-opco-llc/salaries ; https://www.ellis.com/visa-sponsors/anthropic-pbc/salaries | Search excerpts | F6, 6.7, 6.13 | B |
| S20 | h1bdata.net, record I-200-25266-329882 (Anthropic Research Engineer) | https://h1bdata.net/record/I-200-25266-329882 | Single DOL-derived record | F6, 6.7 | B |
| S21 | Payscale, Machine Learning Engineer, New York | https://www.payscale.com/research/US/Job=Machine_Learning_Engineer/Salary/51da40cd/New-York-NY | Excerpt | 6.11 | C |
| S22 | WTW, AI and Digital Talent Salary Survey press release (6 May 2026) and relays | https://www.wtwco.com/en-us/news/2026/05/us-pulls-further-ahead-on-ai-pay-as-europe-reshuffles-and-emerging-markets-accelerate ; https://www.hrgrapevine.com/us/content/article/2026-05-05-us-leads-the-way-as-incentives-reshape-rewards ; https://hrexecutive.com/where-ai-pay-is-heating-up-in-2026-global-shifts-and-emerging-markets/ (paywalled shell) | Press release | 6.3, 6.11 | A (press release) |
| S23 | Pave and Nua Group, "State of AI Talent" press release (24 Aug 2026); secondary relay | https://www.prnewswire.com/news-releases/new-report-from-pave-and-nua-group-ai-research-scientists-command-median-new-hire-equity-grants-above-4-million-as-the-ai-talent-market-splits-into-distinct-job-families-302857849.html ; https://genedai.me/2026/08/30/ai-research-equity-grants-base-pay/ | Press release (A); relay (C) | F5, 6.6, 6.12 | A / C |
| S24 | Pave, "How Expensive is AI Talent?" | https://www.pave.com/blog-posts/how-expensive-is-ai-talent | Excerpt | F12, 6.13 | A/B |
| S25 | Carta, AI-shifts-in-compensation data page | https://carta.com/data/AI-shifts-in-compensation/ | Seen in search results | F8, 6.12 | A |
| S26 | Carta Insights (Peter Walker), graduation-rate posts | https://carta.com/data/linkedin-series-a-to-series-b-graduation-hard/ ; https://carta.com/data/linkedin-series-a-to-series-b-harder-now/ ; https://carta.com/data/linkedin-series-a-to-b-hardest-in-six-years/ ; https://carta.com/data/linkedin-series-a-to-b-graduation-history/ ; https://carta.com/data/linkedin-seed-series-a-b-failure-rates-similar/ | Opened; Feb–Mar 2026 | F8, 6.12 | A |
| S27 | DLOM literature: Acquiry research summary; BDO "Demystifying Valuation Methodologies Part 3"; ABI Journal (Willamette update); Damodaran (NYU Stern) slides | https://www.acquiry.com/sector-multiples/dlom-research/ ; https://www.bdo.com/getmedia/63b38418-e0a7-47ce-8db2-eb262849ed4d/FS_AM_Valuation-Methodologies_Pt3_8-20_WEB.pdf?ext=.pdf ; https://www.abi.org/abi-journal/update-on-study-of-discount-for-lack-of-marketability ; https://pages.stern.nyu.edu/~adamodar/podcasts/valUGspr17/session22.pdf | Excerpts | F8, 6.12 | B |
| S28 | OpenAI employee tender, Aug 2026 (relays of CNBC and Bloomberg) | https://dealroom.co/news/144253-openai-closes-7b-share-sale-at-852b-valuation-ahead-of-ipo/ ; https://www.calcalistech.com/ctechnews/article/156mfxjli ; https://letsdatascience.com/news/openai-completes-7-billion-employee-share-buyback-52502325 ; https://aiweekly.co/alerts/openai-buys-7b-in-employee-stock-holds-valuation-at-852b | Relays; CNBC and Bloomberg originals not opened | F7, 6.12 | B |
| S29 | Anthropic employee tender, Feb–Apr 2026 (Bloomberg and relays) | https://bloomberg.com/news/articles/2026-02-04/anthropic-plans-employee-tender-offer-at-350-billion-valuation ; https://storyboard18.com/amp/brand-makers/anthropic-allows-employees-to-sell-shares-at-350-billion-valuation-90566.htm ; https://www.shopifreaks.com/anthropic-closes-tender-offer-below-its-6b-target-as-employees-hold-shares-ahead-of-an-anticipated-ipo-this-year/ ; https://www.tipranks.com/news/anthropic-wraps-up-tender-offer-as-employees-resist-selling-shares-ahead-of-ipo | Bloomberg paywalled; completion via relays | F7, 6.12, 7.2 | B |
| S30 | ECB euro foreign exchange reference rates | https://www.ecb.europa.eu/stats/shared/pdf/eurofxref.pdf | 13 Oct 2026 | 6.3, F9 | A |
| S31 | USD/INR history and currency pages | https://www.investing.com/currencies/usd-inr-historical-data ; https://tradingeconomics.com/india/currency ; https://insightfultrade.com/usd-inr-outlook | Excerpts, 8–19 Oct 2026 | F9, 6.8 | B |
| S32 | PPP: World Bank WDI indicator page; secondary summaries | https://data.worldbank.org/indicator/PA.NUS.PPP?t=0 ; https://bharatnotes.com/resources/key-terms/purchasing-power-parity--01-indian-economy-overview/ ; https://www.indexmundi.com/facts/india/ppp-conversion-factor | World Bank page reached, values not read; figures from secondary sites | F9, 6.8 | C |
| S33 | AIM Research, AI Engineer Salary Study, India 2025 | https://reports.aimresearch.co/?p=15406 ; https://aimresearch.co/?p=15406 | Headline of a paywalled study | F3, 6.8 | B |
| S34 | India broad-market relays (Glassdoor, Indeed, Payscale; recruiter guides) | https://www.itm.edu/blog/ai-engineer-salary-in-india/ ; https://www.weekday.works/post/ai-engineer-salary-in-india-2026 ; https://futurense.com/blog/ai-developer-salary-in-india ; https://taggd.in/?p=1011215 ; https://fueler.io/blog/ai-engineer-salary-in-india-skills-experience-and-career-path ; Flexiple (URL not retained†) | Excerpts, May–Oct 2026 | F3, 6.8 | C |
| S35 | Contractor-rate vendors | https://www.secondtalent.com/cost-to-hire/ai-engineer/ ; https://www.secondtalent.com/cost-to-hire/ml-engineer/ ; https://www.secondtalent.com/developer-rate-card/ai-engineer-india/ ; https://www.secondtalent.com/developer-rate-card/machine-learning-engineer-india/ ; https://opsiocloud.com/in/blogs/it-outsourcing-pricing-india-rate-cards/ ; https://www.perfectiongeeks.com/hire-developers/machine-learning-engineers-salary-guide | Excerpts, Sep–Oct 2026 | F11, 6.9 | C |
| S36 | Axial Search, AI engineering pay report (43,480 US postings) | https://axialsearch.com/insights/ai-engineering-salaries | Excerpt; postings since Jan 2026 | F8, 6.12 | B/C |
| S37 | GCC relays: Edoxi; Arabian Business (on the Michael Page UAE Salary Guide 2026); a lifestyle site citing Korn Ferry | https://www.edoxi.com/studyhub/average-ai-engineer-salary-dubai ; https://www.arabianbusiness.com/jobs/uae-salary-guide-2026-the-fastest-growing-sectors-top-paying-jobs-and-skills-employers-want-most ; https://careerpulses.lovable.app/article/high-income-skills-dubai-salary-guide-2026 | Excerpts, Aug–Oct 2026 | F10, 6.10 | C (Arabian Business B for the guide's existence) |
| S38 | Aggregator relay of the Michael Page UAE guide (jobxdubai pages; URLs not retained†); Michael Page UAE job listings | https://www.michaelpage.ae/jobs/ai (listings only; guide not read) | Excerpts | F10, 6.10 | C† |
| S39 | Robert Half Switzerland, Machine Learning Engineer in Zurich (2026 guide); JobStreet Singapore (URL not retained†) | https://roberthalf.com/ch/en/job-details/machine-learning-engineer/zurich | Excerpt; placement-based starting salaries, excluding bonus | F2, F12, 6.11, 6.13 | B/C |
| S40 | Aon Radford McLagan AI job-family announcements (31 Mar 2026; Aon Germany release) | https://www.aon.com/germany/ueber-aon/presse/ki-veraendert-skills-und-verguetung ; https://coverager.com/aon-updates-compensation-database-for-ai-roles/ | Announcements only | 4, 6.14 | A (existence only) |
| S41 | Comprehensive.io methodology and 2023 finding (ML Engineer posted pay about 19% above Software Engineer), via press and newsletter coverage | URLs not retained† | Excerpts | F12, 6.14 | B† |
| S42 | Equity tools: Autograph Fair Offer listing; Cake Equity; Equitybee Benchmark; a newsletter listing Carta's calculator | https://hunted.space/product/autograph-fair-offer ; https://www.cakeequity.com/equity-benchmarks-calculator ; https://thenextweb.com/news/equitybee-benchmark-startup-equity-data-employees ; https://startupnash.substack.com/p/the-highlights-how-to-evaluate-equity | Listings | 6.14 | C |
| S43 | Pin.com, AI compensation salary guide (relays Levels.fyi, PwC, Robert Half and others) | https://pin.com/blog/ai-compensation-salary-guide | Oct 2026 blog | F1, 6.13 | C |
| S44 | Blind thread on Levels.fyi bias | https://www.teamblind.com/post/how-much-bias-if-any-in-levelsfyi-numbers-hrv2rr7n | Anecdotal | 7.2 | D |
| S45 | Vendor guides claiming an infra premium | https://leonstaff.com/blogs/llm-engineer-salary-2026/ ; https://neuronify.com/ai-engineer-salary ; https://www.ayautomate.com/blog/ai-engineer-salary-guide-2026 ; https://recruitslab.com/compensation-guide/ai-engineer ; https://creww.dev/blog/ai-llm-engineer-compensation-bengaluru/ | Excerpts | F12, 6.13 | C/D |
| S46 | Carta dilution medians as relayed by secondary sites | URLs not retained† | Excerpts | F8, 6.12 | C† |
| S47 | News relay mentioning a $100,000 H-1B fee | https://letsdatascience.com/news/openai-discloses-h1b-base-salary-ranges-5d4e9276 | Excerpt; scope and status not verified | 7.3 | C |
| S48 | Levels.fyi, ML Engineer, Greater Hyderabad; ServiceNow ML Engineer, Greater Hyderabad; AmbitionBox figures via Codegnan | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/hyderabad-ind ; https://www.levels.fyi/companies/servicenow/salaries/software-engineer/title/machine-learning-engineer/locations/greater-hyderabad-area ; https://codegnan.com/machine-learning-engineer-salary-in-hyderabad/ | Search excerpts; Levels.fyi page stamped 12 Oct 2026 | F2, F3, Tables A–B, D2, 6.8 | B / C |
| S49 | Levels.fyi, Google ML Engineer (US, two snapshots; Greater Bengaluru) and Google AI Engineer (US) | https://www.levels.fyi/companies/google/salaries/software-engineer/title/machine-learning-engineer ; https://www.levels.fyi/companies/google/salaries/software-engineer/title/machine-learning-engineer?country=254 ; https://www.levels.fyi/companies/google/salaries/software-engineer/title/machine-learning-engineer/locations/greater-bengaluru ; https://www.levels.fyi/companies/google/salaries/software-engineer/title/ai-engineer | Search excerpts, undated (AI Engineer page about 13 months old) | F2, F3, F12, Tables D, D3, 6.13 | B |
| S50 | Levels.fyi, Google software engineer in the UK; Google salary index; Greater London senior-engineer leaderboard | https://www.levels.fyi/en-gb/companies/google/salaries/software-engineer/locations/united-kingdom ; https://www.levels.fyi/companies/google/salaries ; https://www.levels.fyi/leaderboard/Software-Engineer/Senior-Engineer/region/Greater-London-Area/ | Search excerpts; index page about 3 months old | F2, Table D3 | B |
| S51 | Levels.fyi, Meta and Nvidia ML Engineer | https://www.levels.fyi/companies/meta/salaries/software-engineer/title/machine-learning-engineer ; https://www.levels.fyi/companies/nvidia/salaries/software-engineer/title/machine-learning-engineer | Search excerpts (Meta n = 380; Nvidia n = 35) | Table D, 6.6 | B |
| S52 | Levels.fyi, ML Engineer, United Kingdom (all) | https://www.levels.fyi/t/software-engineer/title/machine-learning-engineer/locations/united-kingdom | Search excerpt, stamped 15 Sep 2026 | F2, Tables A–B | B |
| S53 | Levels.fyi, Singapore senior-level software engineer and ByteDance ML Engineer Singapore; Indeed Singapore | https://www.levels.fyi/t/software-engineer/levels/senior/locations/singapore ; https://www.levels.fyi/t/software-engineer/levels/senior/locations/singapore-sgp ; https://www.levels.fyi/companies/bytedance/salaries/software-engineer/title/machine-learning-engineer/locations/singapore ; https://sg.indeed.com/career/machine-learning-engineer/salaries | Search excerpts (1–2 Apr 2026; ByteDance 2 Nov 2025; Indeed 21 Sep 2026) | Tables A–B, 6.11 | B / C |
| S54 | Levels.fyi, Dubai software engineer, Dubai data engineer and the stale Greater Dubai ML/AI page; Gulf broad-market relays (Glassdoor Dubai, Arab1, Leap Scholar, ZeroTaxJobs) | https://www.levels.fyi/t/software-engineer/locations/dubai-are ; https://www.levels.fyi/t/software-engineer/title/data-engineer/locations/dubai-are ; https://www.levels.fyi/t/software-engineer/focus/ml-ai/locations/greater-dubai-area ; https://www.glassdoor.com/Salaries/dubai-united-arab-emirates-machine-learning-engineer-salary-SRCH_IL.0,26_IM954_KO27,52.htm ; https://arab1.ae/machine-learning-engineer-salary-in-uae ; https://leapscholar.com/blog/software-engineer-salary-in-uae/ ; https://zerotaxjobs.com/salaries/machine-learning-engineer/dubai | Search excerpts; the Greater Dubai ML/AI page is about two years old | F10, Tables A–B, 6.10 | B (Levels.fyi software engineer) / C |
| S55 | DeepMind estimate (CTAIO site) and Blind posts on Google Zurich and London pay | https://ctaio.dev/en/salary/google-deepmind-salary/ ; https://www.teamblind.com/post/fb-zurich-comp-4tzp4qpo ; https://www.teamblind.com/post/switching-from-amazon-to-google-hr4nxghd ; https://www.teamblind.com/post/google-london-comp-expectations-m2vys4gj | Secondary estimate and anecdotes | 6.5 (Table D3 caveats), 6.6 | C / D |

**Negative results (searched, not found or not retrieved).** Levels.fyi ML pages for Abu Dhabi, a current Dubai ML series, a Singapore city-level ML page and a Google Zurich page (Hyderabad was found in the second pass); any Levels.fyi remote-market page; a public Comprehensive.io AI-engineer percentile page; Radford McLagan AI percentiles (paywalled); Candor; Cutshort; the Michael Page India technology salary report; Remotive and Wellfound primary pages; platform-native India contractor distributions; a quantitative study of Levels.fyi selection bias; Google DeepMind- and Meta FAIR-specific Levels.fyi pages; the raw DOL LCA files (unreachable from the sandbox).

**Recalled, not found (Grade D, flagged where used).** The AED/USD peg of 3.6725; zero UAE personal income tax; the purpose of Form W-8BEN; housing allowances being common in Gulf packages; press reports of very large individual offers at Meta and elsewhere (not used).
