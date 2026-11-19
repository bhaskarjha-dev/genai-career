---
id: tracks.country-rankings
title: GenAI Country and City Rankings
content_type: reference
stage: 11
status: published
last_verified: 2026-11-19
review_by: 2027-02-17
sources: [T0-35, T0-36, T0-43]
roles: []
geos: [global, india, us, eu, uk, sg, uae]
tags: [geography, relocation, country-rankings, cities, remote]
generated_by: scripts/rank_countries.py
summary: "Monte Carlo rankings of 33 GenAI destination countries and 50 city snapshots across six decision lenses, generated from data/countries.json (T0-35, T0-36, T0-43)."
---

# GenAI Country and City Rankings

Evidence-graded country and city comparisons across 33 jurisdictions and 50 cities from `T0-35` (Americas, Europe and Israel), `T0-36` (Gulf, India and Asia-Pacific) and `T0-43` (cross-border remote hiring), computed by `scripts/rank_countries.py` from `data/countries.json` (decision D-025). Do not hand-edit this file.

> [!WARNING]
> **Dated pointers, not legal, immigration or tax advice.** Visa thresholds, tax brackets, incoming-worker regimes and geopolitical conditions shift fast. Verify every statutory figure on the destination government's official portal on the day you act. All composite rankings and modelled net-pay figures on this page are **Grade M** (model outputs inheriting the weakest input, often Grade C Numbeo rents or Grade D recalled tax schedules).

> [!IMPORTANT]
> **Audit and volatility disclosures (as of 2026-11-19).**
> - **Extract-only audit downgrade (`T0-36`):** `T0-36` had a 9% full-page Read rate; every Extract-only Grade A claim in `T0-36` was downgraded to Grade B in `data/countries.json` unless verified directly at primary official sources on 2026-11-19.
> - **Active 2026 shocks:** Indian nationals face an approximately 13-year US EB-2/EB-3 green-card backlog (`T0-35 L55, L459`) plus H-1B litigation (`T0-35 L578-L579`); Gulf hubs (`AE`, `SA`, `QA`, `BH`) carry 2026 US-Iran regional conflict risk, November 2026 UAE flight disruptions and IMF growth downgrades (`T0-36 L627-L632, L1144`); the Netherlands 30% ruling steps down to 27% on 2027-01-01 (`T0-35 L589`); UK Earned Settlement shifts the baseline ILR track from 5 to 10 years outside high-earner and Global Talent tiers (`T0-35 L582`).

## Method and pillars

Each country is scored across eight anchored 0–10 pillars as a triangular interval `[lo, mid, hi]`. Wide intervals encode thin samples, conflicting data, Grade C/D inputs or policy shocks. `scripts/rank_countries.py` draws **20,000 deterministic Monte Carlo samples** (seed `20261119`) from each pillar's triangular distribution and computes composite 0–100 scores (`sum(weight * score * 10)`) across six lenses (all rankings **Grade M**).

**FX basis:** Americas, Europe and Israel net pay and rents are converted from T0-35 EUR figures to USD using T0-35's ECB reference rate of 2026-11-13 (1 EUR = 1.1052 USD; T0-35 L190). Gulf, India and Asia-Pacific figures use T0-36's USD figures derived from ECB cross rates around 2026-11-11 (INR 93.92, SGD 1.2816, JPY 158.33, KRW 1,358.7, AUD 1.4554, NZD 1.8039, CNY 6.6713, HKD 7.8374, MYR 4.059, TWD 31.522, AED 3.6725, SAR 3.75; treated as +/-2% error band; T0-36 L198).

| Pillar | What it measures | Scale |
|---|---|---|
| **Demand** (`demand`) | Volume and AI-skill share of GenAI/AI job postings across measured platforms. | 0 = negligible measured market; 5 = moderate regional hub; 10 = dominant global volume and share. |
| **Local purchasing power** (`pay_ppp`) | How far local tech net pay stretches against local rent and living costs (Numbeo LPP and post-rent share). | 0 = severe cost squeeze; 5 = moderate savings power; 10 = top global post-rent purchasing power. |
| **Net pay (USD)** (`net_pay`) | Absolute annual net take-home pay and post-rent disposable surplus in USD at reference tech salaries. | 0 = very low USD net surplus (<$15k); 5 = mid-tier ($50k-$65k net); 10 = global ceiling ($150k+ net). |
| **Access (Indian national)** (`access_india`) | Speed, predictability, salary-floor achievability and permanent-residency path for Indian citizens. | 0 = effectively closed; 5 = moderate employer sponsorship or slow/uncertain settlement; 10 = home market (zero visa friction). |
| **Access (non-EU national)** (`access_non_eu`) | Legal entry and settlement path for a generic non-EU national without India-specific backlogs or bilateral quotas. | 0 = effectively closed; 5 = moderate sponsorship with caps/waits; 10 = fast, predictable entry and settlement. |
| **Remote reach from India** (`remote_reach`) | Practical feasibility of working remotely from India for employers in that country (IST overlap, remote share, documented EOR/cross-border hiring). | 0 = closed or zero overlap with negligible hiring; 5 = moderate overlap or mixed local-entity/geo-gated hiring; 10 = strong overlap and open cross-border remote demand. |
| **AI ecosystem** (`ecosystem`) | Frontier AI labs, Big Tech and GCC R&D density, venture funding and public compute programmes. | 0 = minimal AI R&D presence; 5 = active regional startup/corporate hub; 10 = global frontier-lab and VC epicentre. |
| **Policy and macro stability** (`stability`) | Predictability of immigration, tax, AI regulation and regional geopolitical/security conditions as of November 2026. | 0 = severe active conflict or abrupt closure; 5 = material policy churn or regional risk; 10 = highly predictable legal and macro regime. |

**How to read the columns:** `Score` is the Monte Carlo mean composite (0–100) with the point estimate at `mid` in brackets where useful; `P10–P90` is the 80% Monte Carlo rank interval (narrow bands mean robust rank separation, wide bands mean overlapping tiers); `P(Top 5)` is the share of draws in which the country lands in the top five. In Indian-national lenses, **India** is included as the visa-free home baseline so foreign options can be judged against staying local.

## Lens comparison overview (all 33 countries)

Table of deterministic lens rank (`#`) and Monte Carlo 80% rank band (`P10–P90`) across all six lenses (**Grade M**). Countries are ordered by **Overall (Indian national)** rank.

| Country | Region | Overall (India) | Overall (non-EU) | Net pay | Fast access (IN) | Remote from IN | Settlement (IN) |
|---|---|---|---|---|---|---|---|
| **Singapore** (`SG`) | India & Asia-Pacific | #1 (1–1) | #2 (1–2) | #3 (3–3) | #7 (4–8) | #1 (1–3) | #4 (2–5) |
| **United Kingdom** (`GB`) | Europe & Israel | #2 (2–4) | #4 (3–5) | #7 (4–8) | #4 (3–6) | #3 (1–3) | #6 (5–7) |
| **Germany** (`DE`) | Europe & Israel | #3 (2–5) | #3 (3–4) | #11 (10–14) | #2 (2–2) | #5 (4–6) | #2 (1–3) |
| **India** (`IN`) | India & Asia-Pacific | #4 (3–7) | #12 (11–16) | #18 (14–22) | #1 (1–1) | #8 (6–10) | #1 (1–3) |
| **Ireland** (`IE`) | Europe & Israel | #5 (3–7) | #5 (4–7) | #9 (8–12) | #3 (3–4) | #4 (4–6) | #3 (2–5) |
| **United States** (`US`) | Americas | #6 (4–8) | #1 (1–2) | #1 (1–1) | #25 (24–27) | #2 (1–3) | #25 (22–25) |
| **Netherlands** (`NL`) | Europe & Israel | #7 (4–9) | #6 (5–8) | #4 (4–8) | #6 (4–8) | #6 (4–7) | #7 (5–8) |
| **Australia** (`AU`) | India & Asia-Pacific | #8 (5–9) | #8 (5–9) | #5 (4–8) | #5 (4–7) | #9 (8–12) | #5 (3–6) |
| **Canada** (`CA`) | Americas | #9 (7–10) | #7 (5–9) | #8 (4–8) | #8 (6–9) | #12 (9–15) | #8 (7–9) |
| **Switzerland** (`CH`) | Europe & Israel | #10 (9–10) | #9 (7–9) | #2 (2–2) | #24 (23–26) | #7 (6–8) | #18 (12–21) |
| **France** (`FR`) | Europe & Israel | #11 (11–12) | #10 (10–11) | #21 (17–23) | #9 (8–11) | #11 (9–14) | #9 (8–13) |
| **South Korea** (`KR`) | India & Asia-Pacific | #12 (12–16) | #11 (10–14) | #12 (10–15) | #14 (11–20) | #21 (19–24) | #15 (10–20) |
| **Denmark** (`DK`) | Europe & Israel | #13 (12–16) | #13 (11–16) | #10 (9–14) | #17 (11–21) | #17 (14–19) | #10 (9–17) |
| **United Arab Emirates** (`AE`) | Gulf | #14 (12–18) | #15 (12–21) | #14 (9–17) | #18 (12–21) | #10 (9–15) | #22 (19–25) |
| **Sweden** (`SE`) | Europe & Israel | #15 (13–19) | #16 (13–20) | #20 (16–22) | #19 (12–21) | #13 (10–15) | #19 (13–22) |
| **Hong Kong** (`HK`) | India & Asia-Pacific | #16 (13–20) | #17 (13–21) | #15 (11–18) | #12 (10–18) | #19 (17–22) | #17 (11–21) |
| **Spain** (`ES`) | Europe & Israel | #17 (14–20) | #14 (13–20) | #22 (20–26) | #10 (9–16) | #16 (13–18) | #12 (10–18) |
| **Finland** (`FI`) | Europe & Israel | #18 (15–22) | #19 (16–24) | #23 (21–26) | #13 (10–18) | #15 (12–18) | #11 (10–17) |
| **Japan** (`JP`) | India & Asia-Pacific | #19 (16–23) | #18 (14–22) | #27 (23–28) | #11 (10–18) | #25 (20–26) | #14 (10–20) |
| **Austria** (`AT`) | Europe & Israel | #20 (17–23) | #20 (16–24) | #17 (15–21) | #15 (11–20) | #20 (19–24) | #13 (10–19) |
| **Israel** (`IL`) | Europe & Israel | #21 (17–23) | #22 (17–25) | #6 (4–8) | #31 (28–32) | #14 (10–16) | #30 (28–31) |
| **Poland** (`PL`) | Europe & Israel | #22 (17–23) | #21 (17–24) | #26 (22–28) | #16 (11–20) | #18 (15–19) | #20 (13–22) |
| **Norway** (`NO`) | Europe & Israel | #23 (19–24) | #24 (19–25) | #16 (15–20) | #20 (15–22) | #24 (20–25) | #16 (12–21) |
| **Taiwan** (`TW`) | India & Asia-Pacific | #24 (22–27) | #25 (21–26) | #28 (23–28) | #22 (15–23) | #26 (24–27) | #23 (19–25) |
| **Saudi Arabia** (`SA`) | Gulf | #25 (23–28) | #26 (24–28) | #19 (14–23) | #26 (24–27) | #23 (20–25) | #26 (26–29) |
| **China** (`CN`) | India & Asia-Pacific | #26 (23–28) | #23 (17–25) | #13 (9–16) | #30 (28–32) | #28 (27–30) | #31 (28–31) |
| **Estonia** (`EE`) | Europe & Israel | #27 (24–28) | #27 (26–28) | #24 (22–27) | #23 (21–24) | #22 (20–25) | #24 (20–25) |
| **New Zealand** (`NZ`) | India & Asia-Pacific | #28 (25–28) | #28 (26–28) | #25 (21–28) | #21 (15–23) | #30 (28–31) | #21 (14–23) |
| **Portugal** (`PT`) | Europe & Israel | #29 (29–31) | #29 (29–31) | #32 (31–33) | #27 (25–28) | #29 (27–30) | #27 (26–28) |
| **Malaysia** (`MY`) | India & Asia-Pacific | #30 (29–31) | #31 (29–31) | #33 (31–33) | #28 (27–31) | #27 (26–29) | #29 (27–31) |
| **Italy** (`IT`) | Europe & Israel | #31 (29–31) | #30 (29–31) | #31 (30–33) | #29 (28–31) | #31 (29–31) | #28 (27–31) |
| **Qatar** (`QA`) | Gulf | #32 (31–32) | #32 (32–32) | #29 (29–30) | #32 (30–33) | #32 (32–32) | #32 (32–33) |
| **Bahrain** (`BH`) | Gulf | #33 (33–33) | #33 (33–33) | #30 (29–32) | #33 (32–33) | #33 (33–33) | #33 (32–33) |

## Detailed rankings by lens

### Overall (Indian national)

Balanced destination ranking for an Indian national weighing demand, net pay, local purchasing power, India-specific legal access, ecosystem, stability and remote reach. Weights: Demand 18%, Local purchasing power 12%, Net pay (USD) 16%, Access (Indian national) 18%, Remote reach from India 6%, AI ecosystem 16%, Policy and macro stability 14%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **Singapore** (`SG`) | India & Asia-Pacific | 79.4 | 79.8 | 1–1 | 100.0% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 2 | **United Kingdom** (`GB`) | Europe & Israel | 77.0 | 77.3 | 2–4 | 97.7% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 3 | **Germany** (`DE`) | Europe & Israel | 76.3 | 76.6 | 2–5 | 93.8% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 4 | **India** (`IN`) | India & Asia-Pacific | 75.3 | 75.6 | 3–7 | 69.0% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 5 | **Ireland** (`IE`) | Europe & Israel | 74.8 | 75.0 | 3–7 | 56.6% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 6 | **United States** (`US`) | Americas | 74.4 | 74.8 | 4–8 | 41.5% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 7 | **Netherlands** (`NL`) | Europe & Israel | 73.8 | 73.9 | 4–9 | 23.1% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 8 | **Australia** (`AU`) | India & Asia-Pacific | 73.5 | 73.6 | 5–9 | 16.3% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 9 | **Canada** (`CA`) | Americas | 72.1 | 72.4 | 7–10 | 1.8% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 10 | **Switzerland** (`CH`) | Europe & Israel | 70.9 | 70.9 | 9–10 | 0.2% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 11 | **France** (`FR`) | Europe & Israel | 67.8 | 67.9 | 11–12 | 0.0% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 12 | **South Korea** (`KR`) | India & Asia-Pacific | 65.3 | 65.3 | 12–16 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 13 | **Denmark** (`DK`) | Europe & Israel | 65.1 | 65.1 | 12–16 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 14 | **United Arab Emirates** (`AE`) | Gulf | 64.7 | 64.8 | 12–18 | 0.0% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 15 | **Sweden** (`SE`) | Europe & Israel | 63.7 | 63.8 | 13–19 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 16 | **Hong Kong** (`HK`) | India & Asia-Pacific | 63.4 | 63.4 | 13–20 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 17 | **Spain** (`ES`) | Europe & Israel | 63.4 | 63.5 | 14–20 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 18 | **Finland** (`FI`) | Europe & Israel | 62.3 | 62.3 | 15–22 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 19 | **Japan** (`JP`) | India & Asia-Pacific | 61.6 | 61.7 | 16–23 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 20 | **Austria** (`AT`) | Europe & Israel | 61.6 | 61.6 | 17–23 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 21 | **Israel** (`IL`) | Europe & Israel | 61.3 | 61.4 | 17–23 | 0.0% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 22 | **Poland** (`PL`) | Europe & Israel | 61.2 | 61.1 | 17–23 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 23 | **Norway** (`NO`) | Europe & Israel | 60.4 | 60.5 | 19–24 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 24 | **Taiwan** (`TW`) | India & Asia-Pacific | 58.5 | 58.6 | 22–27 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 25 | **Saudi Arabia** (`SA`) | Gulf | 57.5 | 57.6 | 23–28 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 26 | **China** (`CN`) | India & Asia-Pacific | 57.5 | 57.5 | 23–28 | 0.0% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 27 | **Estonia** (`EE`) | Europe & Israel | 57.0 | 57.0 | 24–28 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 28 | **New Zealand** (`NZ`) | India & Asia-Pacific | 55.9 | 56.1 | 25–28 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 29 | **Portugal** (`PT`) | Europe & Israel | 46.9 | 46.8 | 29–31 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 30 | **Malaysia** (`MY`) | India & Asia-Pacific | 45.7 | 45.6 | 29–31 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |
| 31 | **Italy** (`IT`) | Europe & Israel | 45.4 | 45.0 | 29–31 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 32 | **Qatar** (`QA`) | Gulf | 42.3 | 42.1 | 31–32 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 33 | **Bahrain** (`BH`) | Gulf | 38.4 | 38.1 | 33–33 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |

### Overall (generic non-EU national)

Balanced destination ranking for a generic non-EU national without India's US EB-2/EB-3 green-card backlog, India-specific bilateral quotas (MATES, India-NZ FTA) or IST remote-overlap weighting. Weights: Demand 20%, Local purchasing power 12%, Net pay (USD) 16%, Access (non-EU national) 18%, AI ecosystem 18%, Policy and macro stability 16%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **United States** (`US`) | Americas | 80.2 | 80.8 | 1–2 | 100.0% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 2 | **Singapore** (`SG`) | India & Asia-Pacific | 80.2 | 80.6 | 1–2 | 100.0% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 3 | **Germany** (`DE`) | Europe & Israel | 77.2 | 77.5 | 3–4 | 98.3% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 4 | **United Kingdom** (`GB`) | Europe & Israel | 76.9 | 77.1 | 3–5 | 95.8% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 5 | **Ireland** (`IE`) | Europe & Israel | 75.0 | 75.1 | 4–7 | 59.0% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 6 | **Netherlands** (`NL`) | Europe & Israel | 73.7 | 73.8 | 5–8 | 16.5% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 7 | **Canada** (`CA`) | Americas | 73.6 | 74.0 | 5–9 | 15.7% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 8 | **Australia** (`AU`) | India & Asia-Pacific | 73.5 | 73.6 | 5–9 | 13.6% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 9 | **Switzerland** (`CH`) | Europe & Israel | 71.8 | 71.9 | 7–9 | 1.1% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 10 | **France** (`FR`) | Europe & Israel | 69.0 | 69.2 | 10–11 | 0.0% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 11 | **South Korea** (`KR`) | India & Asia-Pacific | 67.0 | 67.1 | 10–14 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 12 | **India** (`IN`) | India & Asia-Pacific | 66.2 | 66.3 | 11–16 | 0.0% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 13 | **Denmark** (`DK`) | Europe & Israel | 65.7 | 65.7 | 11–16 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 14 | **Spain** (`ES`) | Europe & Israel | 64.0 | 64.1 | 13–20 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 15 | **United Arab Emirates** (`AE`) | Gulf | 64.0 | 64.1 | 12–21 | 0.0% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 16 | **Sweden** (`SE`) | Europe & Israel | 63.8 | 63.9 | 13–20 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 17 | **Hong Kong** (`HK`) | India & Asia-Pacific | 63.6 | 63.7 | 13–21 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 18 | **Japan** (`JP`) | India & Asia-Pacific | 63.3 | 63.4 | 14–22 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 19 | **Finland** (`FI`) | Europe & Israel | 62.1 | 62.1 | 16–24 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 20 | **Austria** (`AT`) | Europe & Israel | 62.1 | 62.2 | 16–24 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 21 | **Poland** (`PL`) | Europe & Israel | 61.7 | 61.6 | 17–24 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 22 | **Israel** (`IL`) | Europe & Israel | 61.5 | 61.6 | 17–25 | 0.0% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 23 | **China** (`CN`) | India & Asia-Pacific | 61.4 | 61.4 | 17–25 | 0.0% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 24 | **Norway** (`NO`) | Europe & Israel | 60.8 | 60.9 | 19–25 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 25 | **Taiwan** (`TW`) | India & Asia-Pacific | 59.7 | 59.8 | 21–26 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 26 | **Saudi Arabia** (`SA`) | Gulf | 57.8 | 57.9 | 24–28 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 27 | **Estonia** (`EE`) | Europe & Israel | 56.6 | 56.7 | 26–28 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 28 | **New Zealand** (`NZ`) | India & Asia-Pacific | 56.0 | 56.2 | 26–28 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 29 | **Portugal** (`PT`) | Europe & Israel | 46.7 | 46.6 | 29–31 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 30 | **Italy** (`IT`) | Europe & Israel | 46.5 | 46.1 | 29–31 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 31 | **Malaysia** (`MY`) | India & Asia-Pacific | 45.7 | 45.6 | 29–31 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |
| 32 | **Qatar** (`QA`) | Gulf | 42.0 | 41.9 | 32–32 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 33 | **Bahrain** (`BH`) | Gulf | 38.2 | 38.0 | 33–33 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |

### Highest net pay and disposable income

Prioritises USD net take-home pay and post-rent purchasing power, with secondary weight on job demand, stability and ecosystem. Weights: Demand 10%, Local purchasing power 30%, Net pay (USD) 45%, AI ecosystem 5%, Policy and macro stability 10%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **United States** (`US`) | Americas | 90.8 | 91.5 | 1–1 | 100.0% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 2 | **Switzerland** (`CH`) | Europe & Israel | 87.8 | 88.2 | 2–2 | 100.0% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 3 | **Singapore** (`SG`) | India & Asia-Pacific | 84.4 | 84.9 | 3–3 | 100.0% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 4 | **Netherlands** (`NL`) | Europe & Israel | 75.7 | 75.9 | 4–8 | 56.3% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 5 | **Australia** (`AU`) | India & Asia-Pacific | 75.3 | 75.5 | 4–8 | 45.1% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 6 | **Israel** (`IL`) | Europe & Israel | 74.8 | 75.1 | 4–8 | 33.9% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 7 | **United Kingdom** (`GB`) | Europe & Israel | 74.7 | 74.8 | 4–8 | 33.2% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 8 | **Canada** (`CA`) | Americas | 74.6 | 74.9 | 4–8 | 30.8% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 9 | **Ireland** (`IE`) | Europe & Israel | 70.4 | 70.5 | 8–12 | 0.3% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 10 | **Denmark** (`DK`) | Europe & Israel | 69.4 | 69.4 | 9–14 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 11 | **Germany** (`DE`) | Europe & Israel | 68.4 | 68.6 | 10–14 | 0.0% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 12 | **South Korea** (`KR`) | India & Asia-Pacific | 68.3 | 68.3 | 10–15 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 13 | **China** (`CN`) | India & Asia-Pacific | 67.9 | 68.0 | 9–16 | 0.1% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 14 | **United Arab Emirates** (`AE`) | Gulf | 67.3 | 67.5 | 9–17 | 0.3% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 15 | **Hong Kong** (`HK`) | India & Asia-Pacific | 65.8 | 65.8 | 11–18 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 16 | **Norway** (`NO`) | Europe & Israel | 63.1 | 63.1 | 15–20 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 17 | **Austria** (`AT`) | Europe & Israel | 62.8 | 62.8 | 15–21 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 18 | **India** (`IN`) | India & Asia-Pacific | 62.6 | 62.5 | 14–22 | 0.0% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 19 | **Saudi Arabia** (`SA`) | Gulf | 62.4 | 62.7 | 14–23 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 20 | **Sweden** (`SE`) | Europe & Israel | 61.9 | 61.9 | 16–22 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 21 | **France** (`FR`) | Europe & Israel | 61.0 | 61.1 | 17–23 | 0.0% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 22 | **Spain** (`ES`) | Europe & Israel | 58.5 | 58.6 | 20–26 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 23 | **Finland** (`FI`) | Europe & Israel | 57.9 | 57.9 | 21–26 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 24 | **Estonia** (`EE`) | Europe & Israel | 57.2 | 57.2 | 22–27 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 25 | **New Zealand** (`NZ`) | India & Asia-Pacific | 57.0 | 57.0 | 21–28 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 26 | **Poland** (`PL`) | Europe & Israel | 56.3 | 55.9 | 22–28 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 27 | **Japan** (`JP`) | India & Asia-Pacific | 55.3 | 55.0 | 23–28 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 28 | **Taiwan** (`TW`) | India & Asia-Pacific | 55.2 | 55.3 | 23–28 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 29 | **Qatar** (`QA`) | Gulf | 48.6 | 48.6 | 29–30 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 30 | **Bahrain** (`BH`) | Gulf | 43.2 | 43.1 | 29–32 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |
| 31 | **Italy** (`IT`) | Europe & Israel | 39.5 | 38.5 | 30–33 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 32 | **Portugal** (`PT`) | Europe & Israel | 39.2 | 39.0 | 31–33 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 33 | **Malaysia** (`MY`) | India & Asia-Pacific | 38.1 | 37.8 | 31–33 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |

### Fastest legal access (Indian nationals)

Prioritises speed and predictability of legal entry for Indian nationals alongside job demand and policy stability. India sits at #1 as the visa-free home baseline. Weights: Demand 20%, Net pay (USD) 10%, Access (Indian national) 45%, AI ecosystem 10%, Policy and macro stability 15%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **India** (`IN`) | India & Asia-Pacific | 85.3 | 85.9 | 1–1 | 100.0% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 2 | **Germany** (`DE`) | Europe & Israel | 81.3 | 81.7 | 2–2 | 100.0% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 3 | **Ireland** (`IE`) | Europe & Israel | 78.4 | 78.7 | 3–4 | 98.5% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 4 | **United Kingdom** (`GB`) | Europe & Israel | 76.6 | 77.0 | 3–6 | 81.1% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 5 | **Australia** (`AU`) | India & Asia-Pacific | 75.3 | 75.4 | 4–7 | 55.0% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 6 | **Netherlands** (`NL`) | Europe & Israel | 74.4 | 74.6 | 4–8 | 31.0% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 7 | **Singapore** (`SG`) | India & Asia-Pacific | 74.3 | 74.6 | 4–8 | 29.9% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 8 | **Canada** (`CA`) | Americas | 72.1 | 72.6 | 6–9 | 4.4% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 9 | **France** (`FR`) | Europe & Israel | 69.9 | 70.2 | 8–11 | 0.1% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 10 | **Spain** (`ES`) | Europe & Israel | 67.5 | 67.8 | 9–16 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 11 | **Japan** (`JP`) | India & Asia-Pacific | 66.5 | 66.8 | 10–18 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 12 | **Hong Kong** (`HK`) | India & Asia-Pacific | 66.4 | 66.5 | 10–18 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 13 | **Finland** (`FI`) | Europe & Israel | 66.3 | 66.3 | 10–18 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 14 | **South Korea** (`KR`) | India & Asia-Pacific | 65.5 | 65.6 | 11–20 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 15 | **Austria** (`AT`) | Europe & Israel | 65.1 | 65.2 | 11–20 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 16 | **Poland** (`PL`) | Europe & Israel | 65.1 | 65.2 | 11–20 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 17 | **Denmark** (`DK`) | Europe & Israel | 65.0 | 65.1 | 11–21 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 18 | **United Arab Emirates** (`AE`) | Gulf | 64.4 | 64.5 | 12–21 | 0.0% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 19 | **Sweden** (`SE`) | Europe & Israel | 64.4 | 64.7 | 12–21 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 20 | **Norway** (`NO`) | Europe & Israel | 63.4 | 63.6 | 15–22 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 21 | **New Zealand** (`NZ`) | India & Asia-Pacific | 62.8 | 63.2 | 15–23 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 22 | **Taiwan** (`TW`) | India & Asia-Pacific | 62.8 | 63.0 | 15–23 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 23 | **Estonia** (`EE`) | Europe & Israel | 59.8 | 60.0 | 21–24 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 24 | **Switzerland** (`CH`) | Europe & Israel | 57.2 | 57.0 | 23–26 | 0.0% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 25 | **United States** (`US`) | Americas | 55.7 | 55.8 | 24–27 | 0.0% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 26 | **Saudi Arabia** (`SA`) | Gulf | 55.1 | 55.1 | 24–27 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 27 | **Portugal** (`PT`) | Europe & Israel | 53.9 | 54.0 | 25–28 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 28 | **Malaysia** (`MY`) | India & Asia-Pacific | 50.0 | 50.0 | 27–31 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |
| 29 | **Italy** (`IT`) | Europe & Israel | 49.2 | 49.0 | 28–31 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 30 | **China** (`CN`) | India & Asia-Pacific | 48.8 | 48.6 | 28–32 | 0.0% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 31 | **Israel** (`IL`) | Europe & Israel | 48.5 | 48.6 | 28–32 | 0.0% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 32 | **Qatar** (`QA`) | Gulf | 45.6 | 45.5 | 30–33 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 33 | **Bahrain** (`BH`) | Gulf | 42.8 | 42.6 | 32–33 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |

### Remote work from India (employer markets)

Ranks employer jurisdictions by feasibility of remote employment or contracting from India: IST overlap, documented cross-border hiring, demand and pay. Weights: Demand 25%, Local purchasing power 15%, Remote reach from India 40%, AI ecosystem 10%, Policy and macro stability 10%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **Singapore** (`SG`) | India & Asia-Pacific | 78.3 | 78.6 | 1–3 | 100.0% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 2 | **United States** (`US`) | Americas | 78.2 | 78.7 | 1–3 | 99.8% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 3 | **United Kingdom** (`GB`) | Europe & Israel | 78.0 | 78.4 | 1–3 | 100.0% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 4 | **Ireland** (`IE`) | Europe & Israel | 73.5 | 73.8 | 4–6 | 76.8% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 5 | **Germany** (`DE`) | Europe & Israel | 73.2 | 73.5 | 4–6 | 69.2% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 6 | **Netherlands** (`NL`) | Europe & Israel | 72.1 | 72.2 | 4–7 | 40.4% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 7 | **Switzerland** (`CH`) | Europe & Israel | 70.0 | 70.2 | 6–8 | 9.4% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 8 | **India** (`IN`) | India & Asia-Pacific | 68.5 | 69.0 | 6–10 | 4.3% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 9 | **Australia** (`AU`) | India & Asia-Pacific | 66.8 | 66.9 | 8–12 | 0.1% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 10 | **United Arab Emirates** (`AE`) | Gulf | 64.6 | 64.9 | 9–15 | 0.0% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 11 | **France** (`FR`) | Europe & Israel | 64.4 | 64.6 | 9–14 | 0.0% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 12 | **Canada** (`CA`) | Americas | 64.1 | 64.3 | 9–15 | 0.0% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 13 | **Sweden** (`SE`) | Europe & Israel | 63.9 | 64.0 | 10–15 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 14 | **Israel** (`IL`) | Europe & Israel | 63.2 | 63.3 | 10–16 | 0.0% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 15 | **Finland** (`FI`) | Europe & Israel | 61.5 | 61.5 | 12–18 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 16 | **Spain** (`ES`) | Europe & Israel | 60.7 | 60.7 | 13–18 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 17 | **Denmark** (`DK`) | Europe & Israel | 60.4 | 60.4 | 14–19 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 18 | **Poland** (`PL`) | Europe & Israel | 59.6 | 59.5 | 15–19 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 19 | **Hong Kong** (`HK`) | India & Asia-Pacific | 57.6 | 57.5 | 17–22 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 20 | **Austria** (`AT`) | Europe & Israel | 55.6 | 55.5 | 19–24 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 21 | **South Korea** (`KR`) | India & Asia-Pacific | 55.5 | 55.5 | 19–24 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 22 | **Estonia** (`EE`) | Europe & Israel | 54.6 | 54.6 | 20–25 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 23 | **Saudi Arabia** (`SA`) | Gulf | 54.5 | 54.7 | 20–25 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 24 | **Norway** (`NO`) | Europe & Israel | 54.3 | 54.3 | 20–25 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 25 | **Japan** (`JP`) | India & Asia-Pacific | 53.9 | 54.0 | 20–26 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 26 | **Taiwan** (`TW`) | India & Asia-Pacific | 51.0 | 51.1 | 24–27 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 27 | **Malaysia** (`MY`) | India & Asia-Pacific | 47.6 | 47.5 | 26–29 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |
| 28 | **China** (`CN`) | India & Asia-Pacific | 46.2 | 46.2 | 27–30 | 0.0% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 29 | **Portugal** (`PT`) | Europe & Israel | 45.3 | 45.2 | 27–30 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 30 | **New Zealand** (`NZ`) | India & Asia-Pacific | 43.7 | 43.6 | 28–31 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 31 | **Italy** (`IT`) | Europe & Israel | 42.1 | 41.7 | 29–31 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 32 | **Qatar** (`QA`) | Gulf | 35.0 | 34.9 | 32–32 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 33 | **Bahrain** (`BH`) | Gulf | 30.7 | 30.4 | 33–33 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |

### Long-term settlement (Indian nationals)

Weights permanent-residency viability for Indian nationals and policy/macro stability alongside net pay, demand and AI ecosystem. Weights: Demand 14%, Net pay (USD) 14%, Access (Indian national) 32%, AI ecosystem 12%, Policy and macro stability 28%. **Grade M** (20,000 Monte Carlo draws).

| Rank | Country | Region | MC Score | Mid Score | P10–P90 Rank | P(Top 5) | Key trade-off or caveat |
|---|---|---|---|---|---|---|---|
| 1 | **India** (`IN`) | India & Asia-Pacific | 80.1 | 80.4 | 1–3 | 100.0% | Sharp 2x-4x pay stratification between Levels.fyi product/GCC tier (BLR ML p50 INR 44.4L) and broad market (INR 10-20L); domestic remote-tagged share only 0.8%. |
| 2 | **Germany** (`DE`) | Europe & Israel | 79.8 | 80.1 | 1–3 | 99.8% | High effective tax/social wedge (~41.8%); local German still helps outside international hubs and speeds PR from 27 to 21 months. |
| 3 | **Ireland** (`IE`) | Europe & Israel | 77.9 | 78.1 | 2–5 | 95.6% | Acute Dublin housing shortage pushes 1-bed centre rent to ~$2,425/mo; small domestic market heavily reliant on US MNC EMEA headquarters. |
| 4 | **Singapore** (`SG`) | India & Asia-Pacific | 77.6 | 77.9 | 2–5 | 93.0% | High 1-bed city-centre rent (S$3,419-S$4,094/mo across Jun/Nov 2026 Numbeo captures); PR approval is discretionary with no published wait time. |
| 5 | **Australia** (`AU`) | India & Asia-Pacific | 76.3 | 76.4 | 3–6 | 72.9% | Core Skills 482 processing spans 7-10 months; Sydney 2025 Numbeo rent (~$2,159/mo) is one year old; no city-level Levels.fyi ML pages in T0-36. |
| 6 | **United Kingdom** (`GB`) | Europe & Israel | 74.7 | 75.0 | 5–7 | 27.1% | Earned Settlement policy shift creates ILR-timeline uncertainty for sub-GBP 50.3k earners; London 1-bed centre rent ~$2,906/mo compresses savings. |
| 7 | **Netherlands** (`NL`) | Europe & Israel | 73.8 | 73.9 | 5–8 | 10.7% | 30% ruling steps down to 27% on 2027-01-01; Amsterdam housing shortage pushes 1-bed centre rent to ~$2,635/mo; mandatory private health insurance excluded. |
| 8 | **Canada** (`CA`) | Americas | 71.9 | 72.2 | 7–9 | 1.0% | GTS Category A referral partners cut from 58 to 41 in Sep 2026; zero 09:00-18:00 IST overlap; BC/QC tax models low confidence in T0-35. |
| 9 | **France** (`FR`) | Europe & Israel | 69.2 | 69.4 | 8–13 | 0.0% | Lower headline tech pay than UK/DE/NL/CH; French tax/social model in T0-35 used recalled 2025 parameters (Grade D inputs); French language required for many firms. |
| 10 | **Denmark** (`DK`) | Europe & Israel | 67.6 | 67.7 | 9–17 | 0.0% | Small Levels.fyi senior sample (n=52); strict Danish permanent-residency integration rules outside initial Pay Limit entry. |
| 11 | **Finland** (`FI`) | Europe & Israel | 67.4 | 67.4 | 10–17 | 0.0% | Small AI hiring market; Finnish tax model in T0-35 is low confidence (2025 recalled scale); all-level pay reference only. |
| 12 | **Spain** (`ES`) | Europe & Israel | 67.3 | 67.6 | 10–18 | 0.0% | Lower headline tech pay than Northern Europe; Madrid Numbeo rent page dated June 2024 (possibly stale); Spanish language needed outside international hubs. |
| 13 | **Austria** (`AT`) | Europe & Israel | 66.5 | 66.6 | 10–19 | 0.0% | Small senior Levels.fyi sample (n=45 in Vienna); smaller AI job volume than Germany. |
| 14 | **Japan** (`JP`) | India & Asia-Pacific | 66.4 | 66.5 | 10–20 | 0.0% | Weak JPY depresses USD net pay ($38.0k at Tokyo R1); Japanese required for most local employers; PR guidelines tightening from 2027-04-01. |
| 15 | **South Korea** (`KR`) | India & Asia-Pacific | 66.3 | 66.4 | 10–20 | 0.0% | Korean language required outside foreign firms; 19% flat tax option scheduled to expire 2026-12-31; AI Basic Act in force Jan 2026 (1-yr penalty grace). |
| 16 | **Norway** (`NO`) | Europe & Israel | 65.8 | 66.0 | 12–21 | 0.0% | Small AI market (PwC 0.8-0.9% AI posting share) and small Oslo pay sample (n=82); high non-rent living costs. |
| 17 | **Hong Kong** (`HK`) | India & Asia-Pacific | 65.7 | 65.8 | 11–21 | 0.0% | Levels.fyi ML page is degenerate/very thin (use SWE R1 HK$570k / R2 HK$800k baseline); high housing costs (~$2,200/mo); small non-finance AI volume. |
| 18 | **Switzerland** (`CH`) | Europe & Israel | 65.5 | 65.4 | 12–21 | 0.0% | Very tight non-EU quota and employer burden of proof; privately bought mandatory health insurance is excluded from T0-35 net pay. |
| 19 | **Sweden** (`SE`) | Europe & Israel | 65.2 | 65.3 | 13–22 | 0.0% | Work-permit salary threshold rose to 90% median in 2026; Swedish tax model in T0-35 is low confidence. |
| 20 | **Poland** (`PL`) | Europe & Israel | 64.8 | 64.8 | 13–22 | 0.0% | All-level pay reference only in T0-35; employee tax model understates net take-home for B2B-contracted senior engineers. |
| 21 | **New Zealand** (`NZ`) | India & Asia-Pacific | 64.6 | 64.9 | 14–23 | 0.0% | Very small AI job market; Levels.fyi NZ ML page is degenerate/very thin; Auckland rent not retrieved in T0-36; NZ tax schedule recalled (Grade D). |
| 22 | **United Arab Emirates** (`AE`) | Gulf | 62.1 | 62.2 | 19–25 | 0.0% | 2026 US-Iran regional conflict triggered EASA aviation bulletins, UAE flight disruptions (Nov 2026) and threats to Gulf data centres; Dubai pay is noisy and Numbeo rent may understate asking rents by 25-40%. |
| 23 | **Taiwan** (`TW`) | India & Asia-Pacific | 62.1 | 62.2 | 19–25 | 0.0% | Moderate software/ML pay ($43.5k R1) relative to hardware/semiconductor prominence; Mandarin needed outside multinationals; tax schedule recalled (Grade D). |
| 24 | **Estonia** (`EE`) | Europe & Israel | 61.9 | 62.0 | 20–25 | 0.0% | Very small domestic market (n=107 all-level SWE); limited local AI job volume outside a handful of startups. |
| 25 | **United States** (`US`) | Americas | 60.6 | 60.8 | 22–25 | 0.0% | Severe India green-card backlog (~13 yrs EB-2/EB-3); H-1B $100k fee proclamation barred by courts 2026-09-30 with appeals pending; zero 09:00-18:00 IST overlap. |
| 26 | **Saudi Arabia** (`SA`) | Gulf | 54.1 | 54.1 | 26–29 | 0.0% | All Riyadh AI pay figures are Grade C; 2026 regional conflict risk plus 30% engineering Saudization and Qiwa work-permit tightening. |
| 27 | **Portugal** (`PT`) | Europe & Israel | 54.1 | 54.1 | 26–28 | 0.0% | Low local pay relative to Lisbon rent (Numbeo LPP 65.3, lowest in T0-35); Lisbon rent page dated June 2023 (stale). |
| 28 | **Italy** (`IT`) | Europe & Israel | 50.5 | 50.3 | 27–31 | 0.0% | Milan Levels.fyi sample is tiny (n=18, EUR 35.4k) and too thin to rank reliably; lowest EU WFH share in T0-35 (2.7%). |
| 29 | **Malaysia** (`MY`) | India & Asia-Pacific | 50.5 | 50.4 | 27–31 | 0.0% | Low local ML pay ($20k R1 / $34.9k R2) sits well below the new RM 20,000/mo (~$59k/yr) Cat I EP floor; tax schedule recalled (Grade D). |
| 30 | **Israel** (`IL`) | Europe & Israel | 50.2 | 50.3 | 28–31 | 0.0% | Active regional security/conflict risk; 63-month expert-permit cap prevents long-term settlement for non-citizen/non-aliyah nationals. |
| 31 | **China** (`CN`) | India & Asia-Pacific | 50.0 | 49.9 | 28–31 | 0.0% | Practically closed to foreign remote hiring (T0-36 L33, L91); Beijing rent absent (Shanghai 2025 rent used as proxy); tax schedule recalled (Grade D). |
| 32 | **Qatar** (`QA`) | Gulf | 43.8 | 43.7 | 32–33 | 0.0% | Very thin AI market and C-grade pay data only; IMF projected -8.6% 2026 GDP contraction amid 2026 US-Iran regional conflict (T0-36 L627-L630). |
| 33 | **Bahrain** (`BH`) | Gulf | 41.3 | 41.1 | 32–33 | 0.0% | No measured AI pay or Manama rent retrieved in T0-36 (very wide uncertainty bands); IMF projected -0.5% 2026 GDP amid Gulf conflict. |

## City pay, rent and disposable income snapshots

All city rows use reference total compensation from `T0-35` (converted from EUR at 1 EUR = 1.1052 USD) or `T0-36` (USD cross-rates), less modelled single-person income tax and employee social contributions, less 12 months of Numbeo 1-bedroom city-centre rent (**Grade M**; Numbeo rents are Grade C crowd-sourced averages; health insurance excluded for US, Switzerland and the Netherlands). For deeper pay negotiation and role-level bands, see [pay-benchmarks.md](../09-compensation/pay-benchmarks.md).

| Country | City | Reference gross (local) | Net pay (USD/yr) | 1-BR centre rent (USD/mo) | Disposable after rent (USD/yr) | Basis and caveats | Grade | Source |
|---|---|---|---|---|---|---|---|---|
| United States (`US`) | **San Francisco Bay Area** | USD 255,000 (US sr SWE; Bay all-lvl $281.8k) | $163.6k | $3,792/mo | $118.1k | US sr SWE ref; CA tax; Numbeo rent | M | T0-35 L143-L144, L197, L319 |
| United States (`US`) | **Seattle** | USD 255,000 (US sr SWE; SEA all-lvl $255k) | $184.8k | $2,543/mo | $154.3k | US sr SWE ref; 0% WA income tax | M | T0-35 L145, L195, L317 |
| United States (`US`) | **New York** | USD 255,000 (US sr SWE; NYC all-lvl $200k) | $161.9k | $4,529/mo | $107.5k | US sr SWE ref; NY+NYC tax; highest rent | M | T0-35 L146, L198, L320 |
| United States (`US`) | **Austin** | USD 255,000 (US sr SWE; AUS all-lvl $192.5k) | $186.3k | $2,188/mo | $160.0k | US sr SWE ref; 0% TX tax; #1 disp. surplus | M | T0-35 L148, L194, L316 |
| United States (`US`) | **Boston** | USD 255,000 (US sr SWE; BOS all-lvl $182k) | $173.7k | — | — | US sr SWE ref; MA tax; rent absent | M | T0-35 L147, L196, L312 |
| Canada (`CA`) | **Vancouver** | CAD 213,279 (sr SWE, n=463) | $99.8k | $1,999/mo | $75.8k | Sr SWE ref; BC tax low-conf; Apr 2025 rent | M | T0-35 L151, L201, L322 |
| Canada (`CA`) | **Toronto** | CAD 181,038 (sr SWE, n=1,031) | $84.1k | $1,593/mo | $65.0k | Sr SWE ref; Ontario tax; Nov 2026 rent | M | T0-35 L149, L204, L323 |
| Canada (`CA`) | **Montreal** | CAD 143,778 (sr SWE, n=247) | $65.2k | $1,277/mo | $49.9k | Sr SWE ref; QC tax low-conf; French factor | M | T0-35 L150, L209, L328 |
| United Kingdom (`GB`) | **London** | GBP 104,240 (all-lvl SWE, n=3,491; UK ML GBP 104.5k) | $92.8k | $2,906/mo | $57.9k | All-lvl ref (conservative vs sr); high rent | M | T0-35 L152, L183, L202, L324 |
| United Kingdom (`GB`) | **Cambridge** | GBP 84,375 (all-lvl SWE, n=165) | $78.7k | $1,808/mo | $57.0k | All-lvl ref; Apr 2025 rent | M | T0-35 L153, L205, L325 |
| Switzerland (`CH`) | **Zurich** | CHF 180,462 (sr SWE, n=229) | $156.0k | $2,845/mo | $121.8k | Sr SWE ref; #1 EU net & disp; health ins excl. | M | T0-35 L159, L199, L318 |
| Germany (`DE`) | **Berlin** | EUR 99,888 (sr SWE, n=872) | $64.3k | $1,459/mo | $46.7k | Sr SWE ref; 41.8% tax+social; Nov 2026 rent | M | T0-35 L155, L210, L331 |
| Germany (`DE`) | **Munich** | EUR 98,407 (sr SWE, n=323) | $63.4k | $1,656/mo | $43.5k | Sr SWE ref; Anthropic Munich; Jan 2026 rent | M | T0-35 L156, L211, L334 |
| Netherlands (`NL`) | **Amsterdam** | EUR 124,584 (sr SWE, n=645) | $87.0k | $2,635/mo | $55.4k | Sr SWE std net ($107.4k w/ 30% ruling) | M | T0-35 L157, L203, L254, L326 |
| Ireland (`IE`) | **Dublin** | EUR 110,371 (all-lvl SWE, n=987) | $76.8k | $2,425/mo | $47.7k | All-lvl ref (conservative vs sr); high rent | M | T0-35 L154, L206, L330 |
| France (`FR`) | **Paris** | EUR 81,333 (sr SWE, n=292) | $56.6k | $1,599/mo | $37.4k | Sr SWE std net ($63.8k w/ impatriate); Nov 2026 rent | M | T0-35 L158, L215, L255, L339 |
| Israel (`IL`) | **Tel Aviv** | ILS 553,971 (sr SWE, n=606) | $110.3k | $2,205/mo | $83.9k | Sr SWE ref; #3 pay outside US; Nov 2026 rent | M | T0-35 L172, L200, L321 |
| Sweden (`SE`) | **Stockholm** | SEK 872,504 (sr SWE, n=154) | $61.6k | $1,580/mo | $42.6k | Sr SWE ref; SE tax low-conf; Nov 2026 rent | M | T0-35 L160, L213, L335 |
| Denmark (`DK`) | **Copenhagen** | DKK 802,126 (sr SWE, n=52) | $74.5k | $1,954/mo | $51.0k | Sr SWE (small n=52); $79.5k net w/ 27% scheme | M | T0-35 L161, L207, L256, L327 |
| Finland (`FI`) | **Helsinki** | EUR 74,890 (all-lvl SWE, n=137) | $52.0k | $1,164/mo | $38.0k | All-lvl ref; low-conf tax; 25% regime $55.7k net | M | T0-35 L162, L218, L257, L336 |
| Norway (`NO`) | **Oslo** | NOK 918,643 (all-lvl SWE, n=82) | $67.8k | $1,563/mo | $49.1k | All-lvl ref (small n=82); Apr 2025 rent | M | T0-35 L163, L208, L329 |
| Spain (`ES`) | **Barcelona** | EUR 77,097 (sr SWE, n=304) | $56.7k | $1,557/mo | $38.0k | Sr SWE ref; Feb 2026 rent | M | T0-35 L165, L214, L337 |
| Spain (`ES`) | **Madrid** | EUR 74,568 (sr SWE, n=249) | $55.1k | $1,449/mo | $37.7k | Sr SWE ref; Jun 2024 rent (stale) | M | T0-35 L164, L217, L338 |
| Poland (`PL`) | **Warsaw** | PLN 290,538 (all-lvl SWE, n=841) | $44.3k | $1,152/mo | $30.5k | All-lvl employee ref; Nov 2026 rent | M | T0-35 L168, L219, L340 |
| Poland (`PL`) | **Krakow** | PLN 260,265 (all-lvl SWE, n=367) | $40.4k | $906/mo | $29.5k | All-lvl employee ref; low rent; Nov 2026 | M | T0-35 L169, L220, L341 |
| Austria (`AT`) | **Vienna** | EUR 89,500 (sr SWE, n=45) | $62.0k | $1,307/mo | $46.3k | Sr SWE (small n=45); moderate rent; Nov 2026 | M | T0-35 L171, L212, L332 |
| Estonia (`EE`) | **Tallinn** | EUR 63,900 (all-lvl SWE, n=107) | $55.1k | $789/mo | $45.7k | All-lvl ref; 21.9% tax; low rent (Dec 2025) | M | T0-35 L170, L216, L333 |
| Portugal (`PT`) | **Lisbon** | EUR 51,163 (all-lvl SWE, n=292) | $37.2k | $1,321/mo | $21.3k | All-lvl ref; Jun 2023 rent (stale); IFICI $39.0k net | M | T0-35 L166, L221, L259, L342 |
| Italy (`IT`) | **Milan** | EUR 35,449 (all-lvl SWE, n=18, very thin) | $27.7k | $1,716/mo | $7.1k | Very thin n=18; inpatriate $34.4k net | M | T0-35 L167, L222, L260, L343 |
| Singapore (`SG`) | **Singapore** | SGD 162,502 (ML p50; AI Eng SGD 89.8k) | $115.7k | $2,668/mo | $83.7k | R1 ML p50 (R2 disp $107.8k; Nov rent disp $77.0k) | M | T0-36 L160-L161, L208-L209, L276, L1168 |
| India (`IN`) | **Bengaluru** | INR 44.4L ML p50 (AI Eng 20.4-21.4L; sr SWE 55.4-56.1L) | $37.2k | $335/mo | $33.2k | Levels.fyi R1 ML (R2 disp $47.1k; broad mkt 11-20L) | M | T0-36 L153-L155, L204-L205, L293; T0-43 L179 |
| India (`IN`) | **Hyderabad** | INR 30.3L ML p50 (Glassdoor base 12.5L) | $26.8k | $390/mo | — | Levels.fyi R1 ML; rent INR 22k-54k wide range | M | T0-36 L156-L157, L206, L294 |
| India (`IN`) | **Pune** | INR 20.6L ML p50 (Payscale avg 10.2L) | $19.5k | — | — | Levels.fyi R1 ML; rent absent in T0-36 | M | T0-36 L158-L159, L207, L297 |
| India (`IN`) | **Delhi NCR** | No ML page in T0-36 (91 aimlroles postings) | — | — | — | Strong GCC/startup hub; T0-36 pay/rent absent | C | T0-36 L106, L297 |
| India (`IN`) | **Mumbai** | No ML page in T0-36 (41 aimlroles postings) | — | $650/mo | — | Finance/enterprise hub; Numbeo 2025 rent ~$650 | C | T0-36 L108, L295 |
| India (`IN`) | **Chennai** | No ML page in T0-36 (65 aimlroles postings) | — | — | — | SaaS/GCC hub; T0-36 pay/rent absent | C | T0-36 L107, L297 |
| Australia (`AU`) | **Sydney** | A$177,892 (AU ML p50; Indeed base A$135.1k) | $87.6k | $2,159/mo | $61.7k | National ML R1 + Sydney 2025 rent; 43 aimlroles | M | T0-36 L115, L182-L184, L226, L289 |
| Australia (`AU`) | **Melbourne** | A$177,892 (AU ML p50 national proxy) | $87.6k | — | — | 23 aimlroles postings; city rent absent in T0-36 | M | T0-36 L115, L182, L297 |
| United Arab Emirates (`AE`) | **Dubai** | AED 242,002 UAE ML p50 (Dubai p50 AED 154.3k; UAE p75 AED 360k) | $65.9k | $2,342/mo | $37.8k | R1 UAE ML + Dubai rent (R2 disp $69.9k; noisy pay) | M | T0-36 L162-L166, L210-L211, L278-L280 |
| United Arab Emirates (`AE`) | **Abu Dhabi** | US$100.5k modelled (ZeroTaxJobs; G42 AED 369.6k) | $100.5k | — | — | C-grade modelled pay; rent absent; sovereign hub | C | T0-36 L165, L297 |
| Saudi Arabia (`SA`) | **Riyadh** | SAR 215k-270k (Glassdoor/SalaryExpert C-grade) | $64.7k | $870/mo | $54.2k | Midpoint of C-grade range ($57.3k-$72.0k); 0% PIT | M | T0-36 L167, L212, L291 |
| Japan (`JP`) | **Tokyo** | JPY 8.12M ML p50 (p75 JPY 14.66M; SWE 8.37M) | $38.0k | $1,249/mo | $23.0k | R1 ML ($48.5k disp at R2); JPY weakness hurts USD | M | T0-36 L173-L175, L215-L216, L283 |
| South Korea (`KR`) | **Seoul** | KRW 117.6M ML p50 (p75 KRW 143.6M) | $66.6k | $1,290/mo | $51.2k | R1 ML (R2 disp $62.3k); moderate Seoul rent | M | T0-36 L176, L217-L218, L285 |
| Hong Kong (`HK`) | **Hong Kong** | HK$569,854 SWE p50 (SWE p75 HK$800k; ML page degenerate) | $63.9k | $2,200/mo | $37.6k | SWE R1 baseline (R2 disp $62.0k); 12.1% tax | M | T0-36 L179-L181, L221-L223, L281 |
| New Zealand (`NZ`) | **Auckland** | NZ$147,566 ML p50 (thin; Glassdoor base NZ$95k) | $59.4k | — | — | Very thin Levels.fyi ML R1; rent absent in T0-36 | M | T0-36 L185-L187, L227, L297 |
| Taiwan (`TW`) | **Taipei** | NT$1.37M ML p50 (p75 NT$1.97M; SWE NT$1.56M) | $40.2k | $816/mo | $30.4k | R1 ML (R2 disp $46.3k); low tax/rent; schedule D | M | T0-36 L177-L178, L219-L220, L287 |
| Malaysia (`MY`) | **Kuala Lumpur** | MYR 81,204 ML p50 (p75 MYR 141.5k) | $19.0k | $688/mo | $10.7k | R1 ML (R2 disp $22.3k); low USD pay; schedule D | M | T0-36 L170-L172, L224-L225, L290 |
| China (`CN`) | **Beijing** | CNY 657,542 ML p50 (p75 CNY 1.03M) | $69.7k | $924/mo | $58.6k | R1 ML + Shanghai 2025 rent proxy (R2 disp $95.8k) | M | T0-36 L188-L189, L229-L230, L296 |
| Qatar (`QA`) | **Doha** | QAR 197k avg (Paylab C-grade; Naukrigulf n=5) | $54.1k | $1,679/mo | $34.0k | C-grade aggregator pay + modelled rent; 0% PIT | M | T0-36 L168, L213, L292 |
| Bahrain (`BH`) | **Manama** | Not measured in T0-36 | — | — | — | Pay and rent absent in T0-36; 0% PIT + 1% UI | D | T0-36 L169, L214, L297 |

## Access, language, time-zone overlap and incoming-worker tax regimes

Summary of working language, hours overlapping a 09:00–18:00 IST workday (standard / summer time), incoming-worker tax rules and primary skilled entry pathways. For full visa criteria, processing windows and country playbooks, see [visa-and-relocation.md](visa-and-relocation.md).

| Country | Working language | IST overlap (std / DST) | Incoming-worker tax regime | Main skilled route and settlement | Source |
|---|---|---|---|---|---|
| **United States** (`US`) | English (native) | 0 h / 0 h | **None (state-tax arbitrage)** (B): No special incoming-worker income-tax relief; federal top rate 37% plus state tax (0% TX/WA vs 13.3% CA / 10.9% NY + ~3.88% NYC). | H-1B wage-weighted lottery (1x-4x by wage level, effective 2026-02-27) or O-1A / L-1A; Nov 2026 Visa Bulletin India EB-2 2013-11-01 (~13 yrs), EB-3 2014-01-22 (~12.8 yrs). | T0-35 L194-L198, L288 |
| **Canada** (`CA`) | English (French in Quebec) | 0 h / 0 h | **None** (B): No general incoming-worker tax relief; 2026 combined top marginal rates reach 53.53% (Ontario incl. surtax) and 53.50% (BC). | GTS Category B (9-day LMIA average, C$1,000; realistic India offer-to-start 1-3 months due to 10-week work-permit wait) & ICT C12; Express Entry 2026-11-03 adds high-wage LMIA-free points (NOC 21231/21211 +70 offer / +40 Canadian exp), zero STEM draws in 2025-2026; Start-Up Visa paused 2026-06-30. | T0-35 L201, L204, L209, L289 |
| **United Kingdom** (`GB`) | English (native) | 3.5 h / 4.5 h | **4-year FIG regime** (B): Non-dom remittance basis abolished from April 2025; replaced by 4-year Foreign Income and Gains (FIG) relief for arrivals with 10 consecutive non-resident tax years (does not exempt UK work income). | Skilled Worker (>=GBP 41,700 or SOC going rate: SOC 2134 GBP 54,700; SOC 3544 data analysts ineligible) or Global Talent (Tech Nation, unsponsored); Nov 2026 Earned Settlement policy sets 10-yr default / 5-yr >=GBP 50,271 / 3-yr >=GBP 125,141 (awaiting Rules); B2 English eff 2027-03-26; Graduate 18m from 2027-01-01. | T0-35 L202, L233, L290 |
| **Switzerland** (`CH`) | German/French/Italian; English common in Zurich AI/tech (EF EPI 564) | 4.5 h / 5.5 h | **Low standard tax (Zurich)** (B): No special employee incoming-worker tax relief; standard three-tier federal/cantonal/municipal rate is lowest in Europe at EUR 100k (22.4% deductions). | Quota of 8,500 third-country permits in 2026 (4,500 B + 4,000 L) with strict Swiss/EU/EFTA labour-market precedence. | T0-35 L199, L230, L295 |
| **Germany** (`DE`) | German; English widespread in Berlin/Munich tech (EF EPI 615) | 4.5 h / 5.5 h | **None** (B): No special incoming-worker tax relief; ~41.8% combined income tax and social contributions at reference salary. | EU Blue Card EUR 50,700 std / EUR 45,934.20 shortage (2027 draft EUR 53,100 / 48,108.60 pending Bundesrat); two degree-free IT paths (3y in 7 / 2y in 5); Opportunity Card 1y search; PR in 21m (B1 German) or 27m (A1). | T0-35 L210-L211, L246, L292 |
| **Netherlands** (`NL`) | Dutch; English #1 non-native worldwide (EF EPI 624) | 4.5 h / 5.5 h | **30% ruling (drops to 27% in 2027)** (B): 30% of salary tax-free up to EUR 262k cap in 2026 (adds +EUR 18,501/yr at Amsterdam sr ref); drops to flat 27% from 2027-01-01 with higher salary floor. | HSM 2026 (excl 8% holiday, recognised sponsor): EUR 5,942/mo (>=30), EUR 4,357 (<30), EUR 3,122 (zoekjaar), 2-week IND target; EU Blue Card EUR 5,942 / 4,754 (no sponsor recognition); 30%->27% ruling confirmed via Belastingplan 2027 (passed Tweede Kamer 2026-11-12, eff 2027-01-01); PR 5y. | T0-35 L60, L254, L268, L589 |
| **Ireland** (`IE`) | English (native) | 3.5 h / 4.5 h | **SARP (narrow)** (B): No broad incoming-worker relief modelled in T0-35; standard Dublin deductions ~37.0% at EUR 110.4k. | Critical Skills Employment Permit from EUR 40,904 (from 2026-03-01, phased rises to 2030), ~3-week backlog, 5 years to long-term residency/citizenship. | T0-35 L206, L239, L291 |
| **France** (`FR`) | French; English in Paris AI labs/startups (EF EPI 539) | 4.5 h / 5.5 h | **Impatriate regime** (M): Exemption of impatriation bonus / 30% flat option up to 8 years; adds +EUR 6,588/yr at Paris sr ref (net EUR 51.2k -> EUR 57.8k). | Talent Passport (qualified employee ~EUR 39.6k / 2x SMIC) or EU Blue Card (EUR 59,373); French language matters outside frontier startups. | T0-35 L60, L255, L274 |
| **Israel** (`IL`) | Hebrew; English standard in R&D/tech (EF EPI 524) | 5.5 h / 6.5 h | **None for B/1 expert** (B): Standard progressive bands (36.1% deductions at Tel Aviv sr ref); 10-year foreign-income exemption applies to new immigrants (olim), not temporary B/1 experts. | B/1 foreign-expert permit requiring 2x national average wage; cumulative stay capped at 63 months with no general permanent-residency path read. | T0-35 L200, L234, L306 |
| **Sweden** (`SE`) | Swedish; high English proficiency (EF EPI 609) | 4.5 h / 5.5 h | **Expert tax relief (25% exempt)** (B): 75% of pay taxed for qualifying experts/high earners (threshold SEK 88,200/mo or specialist); not modelled in T0-35 baseline. | Work permit floor SEK 34,470/mo (90% median, eff 2026-06-16; extensions >=2026-12-02) and EU Blue Card SEK 53,625/mo; 30-day service promise (>80% met); 4-year work-permit PR (asylum PR repeal excludes work permits); 8y citizenship (2026-06-06). | T0-35 L275 |
| **Denmark** (`DK`) | Danish; high English proficiency (EF EPI 611) | 4.5 h / 5.5 h | **Researcher & key-employee (27% + 8% AM)** (M): 27% flat tax plus 8% labour-market contribution for up to 7 years (adds +EUR 4,521/yr at Copenhagen sr ref). | Pay Limit Scheme at DKK 552,000/yr (~1-month target); small sample (n=52 sr SWE) in Copenhagen. | T0-35 L256, L269 |
| **Finland** (`FI`) | Finnish/Swedish; high English proficiency (EF EPI 603) | 5.5 h / 6.5 h | **Key-employee 25% flat tax** (M): Key-employee tax at source cut from 32% to 25% in 2026 (adds +EUR 3,339/yr at Helsinki ref; EUR 5,800/mo threshold). | Specialist residence permit (EUR 3,937/mo) with 2-week fast-track service target. | T0-35 L257, L270, L587 |
| **Norway** (`NO`) | Norwegian; high English proficiency (EF EPI 613) | 4.5 h / 5.5 h | **None** (B): No special incoming-worker tax relief; standard Oslo deductions ~29.4% at ref salary. | Skilled Worker NOK 599,200/yr (Master's) / NOK 522,600/yr (Bachelor's) without collective agreement; 3-year permanent-residence path requiring oral A2 Norwegian + social-studies test (2025-09-01). | T0-35 L208, L235, L299 |
| **Spain** (`ES`) | Spanish; moderate English (EF EPI 540) | 4.5 h / 5.5 h | **Beckham Law (24% flat)** (M): Special regime for displaced workers: flat 24% up to EUR 600k for up to 6 years (adds +EUR 2,816/yr at Madrid ref). | Highly Qualified Professional authorisation (20-working-day decision target) or EU Blue Card (1.4x average wage); digital-nomad visa also available. | T0-35 L258, L271 |
| **Poland** (`PL`) | Polish; high English in tech (EF EPI 600) | 4.5 h / 5.5 h | **B2B lump-sum (ryczalt) for contractors** (C): Standard employee deductions ~39.1% at Warsaw ref; 80% of local tech/AI contractors use B2B structures (not modelled in T0-35). | EU Blue Card at PLN 13,355.34/mo in 2026; minimum contract duration cut from 12 to 6 months in 2025-2026. | T0-35 L219, L245, L303; T0-43 L309 |
| **Austria** (`AT`) | German; high English proficiency (EF EPI 616 #2) | 4.5 h / 5.5 h | **None** (B): No general incoming-worker tax relief; 13th/14th month salary favourable tax built into standard 37.3% effective wedge. | Red-White-Red Card (70 points + job offer); Red-White-Red Card plus (unrestricted labour-market access) after 21 of 24 months. | T0-35 L212, L242, L305 |
| **Estonia** (`EE`) | Estonian; good English in tech (EF EPI 561) | 5.5 h / 6.5 h | **Flat 22% income tax** (B): Flat 22% income tax held in 2026 (planned 24% cancelled); #2 highest net pay in Europe at EUR 100k gross (EUR 77.0k). | Employment residence permit at national average gross salary (top-specialist route exempt from quota). | T0-35 L216, L231, L304, L588 |
| **Portugal** (`PT`) | Portuguese; high English proficiency (EF EPI 612) | 3.5 h / 4.5 h | **IFICI (20% flat)** (M): Incentive for Scientific Research and Innovation: 20% flat tax on qualifying Portuguese employment income for 10 years (+EUR 1,650/yr at Lisbon ref). | EU Blue Card (reported around EUR 21,030/yr via secondary source) and D3 highly qualified visa; AIMA immigration backlogs. | T0-35 L259, L272 |
| **Italy** (`IT`) | Italian; lower English proficiency (EF EPI 513) | 4.5 h / 5.5 h | **Inpatriate regime (50% exempt)** (M): 50% of employment income exempt up to EUR 600k for 5 years (+EUR 5,982/yr at Milan ref). | EU Blue Card outside annual decreto flussi quota (~EUR 36k raised threshold), but only 633 Blue Cards issued in 2024. | T0-35 L260, L273 |
| **Singapore** (`SG`) | English (official and primary) | 6.5 h / 6.5 h | **Low standard progressive tax (0-24%)** (B): No special expat tax break; resident rates 0-24% (24% above S$1m) and zero CPF for EP holders yield 8.8% effective tax at ML p50 (7.0% at US$100k). | EP S$5,600 (S$6,200 fin) rising 2027-01-01 to S$6,000 / S$6,600 + COMPASS >=40 pts (SOL names AI Engineer/Researcher for 5y EP); ONE Pass S$30k fixed + AI & Tech track 2027-01-28 (S$22.5k fixed + vested ESOP); Tech.Pass closes 2027-01-27; discretionary PR. | T0-36 L208, L238, L251, L268 |
| **India** (`IN`) | English in tech/GCCs (EF EPI 484 national) | 8 h / 8 h | **FY 2026-27 new regime (default)** (B): Income-tax Act 2025 effective 2026-04-01; slabs 0-30% (rebate to INR 12L, INR 75k std ded); contractors <=INR 75L may use s.58(2) presumptive 50% (see india-remote-tax.md). | Indian citizens need zero work authorisation (home market); foreign nationals require an Employment Visa with USD 25,000 minimum gross annual salary. | T0-36 L252, L374; T0-43 L247 |
| **Australia** (`AU`) | English (native) | 3.5 h / 4.5 h | **None** (B): Standard 2026-27 resident brackets 0-45% plus 2% Medicare levy (~28.4% effective at ML R1; employer superannuation excluded). | SID 482 (2026-07-01 to 2027-06-30, confirmed homeaffairs.gov.au): Specialist Skills AUD 146,576 (no occupation list, 37-78d) / Core Skills AUD 79,423 (CSOL, 4-9m); ENS 186 TRT PR after 2y; National Innovation Visa 858 (invitation-only); India-exclusive MATES 403 ballot (3,000/yr, 18-30). | T0-36 L226, L243, L257, L268 |
| **United Arab Emirates** (`AE`) | Arabic; English standard in international & sovereign AI firms | 7.5 h / 7.5 h | **0% personal income tax** (B): Zero federal or emirate personal income tax on employment income (verified 2026-11-19); 9% corporate tax applies only to business profits above AED 375k. | MoHRE employer permit (2d); Golden Visa 10y (>=AED 30,000/mo — basic-vs-gross contested V0); Green Visa 5y (>=AED 15k/mo); Virtual Working USD 3,500/mo; 0% tax, no standard PR/citizenship. | T0-36 L236, L253, L264 |
| **Saudi Arabia** (`SA`) | Arabic; English in sovereign/international AI employers | 6.5 h / 6.5 h | **0% personal income tax** (B): Zero personal income tax on employment income; expatriates generally exempt from pension contributions. | Employer-sponsored work visa (iqama); Premium Residency holders require Qiwa work permits from June 2026; 30% engineering Saudization effective 2026-06-30. | T0-36 L236, L253, L264 |
| **Japan** (`JP`) | Japanese; English roles exist at foreign firms and select AI labs | 5.5 h / 5.5 h | **None** (B): Standard progressive tax + 10% resident tax + social insurance (~25.9% at Tokyo R1; 32.6% at US$100k). | Engineer visa (CoE 1-3m), HSP (70 pts -> 3y PR, 80 pts -> 1y PR; JPY 3m floor rising by 2027-03-31) & J-Skip (Master's/10y + JPY 20m -> 1y PR); PR fee JPY 200,000 (2026-10-01); B1 Japanese PR rules 2027-04-01. | T0-36 L215, L247, L254, L268 |
| **South Korea** (`KR`) | Korean; English roles mainly at foreign firms and select AI labs | 5.5 h / 5.5 h | **K-Tech Pass 50% tax cut (10 yrs) / 19% flat** (C): K-Tech Pass (widened 2026-07-02) grants 50% income-tax cut for 10 years; legacy 19% flat foreigner rate sunsets for starts after 2026-12-31. | E-7 special-occupation visa or K-Tech Pass (widened July 2026, 3-year path to F-5 permanent residency). | T0-36 L265-L266, L370 |
| **Hong Kong** (`HK`) | Cantonese/English (English standard at international & finance firms) | 6.5 h / 6.5 h | **Low standard salaries tax (15% cap)** (B): No special expat break; 2-17% progressive or 15% standard cap (16% above HK$5m) yields 12.1%-13.5% effective deductions. | Top Talent Pass Scheme (HK$2.5M prior income or top-200 university, no offer needed) and General Employment Policy (~4-6 wks); 7 years ordinary residence for PR. | T0-36 L221-L222, L239, L256 |
| **New Zealand** (`NZ`) | English (native) | 1.5 h / 2.5 h | **4-year transitional foreign-income exemption** (D): Standard 10.5-39% income tax + 1.67% ACC levy (~27.9% at NZ R1; recalled schedule D); transitional exemption covers foreign passive income only. | AEWV (median-wage floor removed, 5.5-7w, NZ$1,540); Green List Tier 1 Software Engineer Straight to Residence at NZ$72.80/h (~NZ$151,424/yr, confirmed immigration.govt.nz); India-NZ FTA (eff 2026-10-20) adds 5,000-holder 3y cap with NO direct PR (prefer Green List Tier 1). | T0-36 L227, L244, L258, L268 |
| **Taiwan** (`TW`) | Mandarin; English roles at multinationals only | 6.5 h / 6.5 h | **50% exemption above NT$3M (5 yrs)** (D): Foreign special professionals (Gold Card) receive 50% exemption on salary exceeding NT$3M for 5 years (recalled D; standard R1 tax ~7.6%). | Employment Gold Card (open 4-in-1 work/residence permit, NT$160,000/mo salary threshold, verified 2026-11-19); path to APRC permanent residency. | T0-36 L219, L258, L267 |
| **Malaysia** (`MY`) | Malay/English (English widespread at international employers) | 6.5 h / 6.5 h | **None** (D): Resident rates 0-30% (~5.1% at KL R1, 20.6% at $100k; recalled schedule D, excl. EPF/SOCSO). | Employment Pass basic salary doubled 2026-06-01 (Cat I MYR 20,000+, Cat II MYR 10k-19,999); DE Rantau (AI/ML/data Tech Talent) reopens 2026-12-01 at USD 36,000/yr up to 4y (open to Indian citizens, no PR, taxable day 61). | T0-36 L224, L241, L258, L268 |
| **China** (`CN`) | Mandarin (English at select multinationals only) | 6.5 h / 6.5 h | **Expat allowance exemptions (temporary)** (D): Comprehensive income bands 3-45% plus ~20.5% social/housing fund (~29.3% at Beijing R1; recalled schedule D). | Z visa with Foreigner Work Permit (Cat A/B/C) and new K visa created for STEM talent, but language, regulatory and geopolitical barriers keep practical access tight. | T0-36 L229, L246, L258, L268 |
| **Qatar** (`QA`) | Arabic; English at international & sovereign employers | 6.5 h / 6.5 h | **0% personal income tax** (B): Zero personal income tax on employment income (PwC reviewed 2025-03-06); social insurance applies to nationals only. | Employer-only Law 21/2015 permit (Law 9/2026 freelance & 5y talent visa rules unconfirmed); 0% tax; PR capped at 100/yr after 20y + fluent Arabic. | T0-36 L236, L253, L264 |
| **Bahrain** (`BH`) | Arabic; English at international/finance employers | 6.5 h / 6.5 h | **0% personal income tax (1% UI)** (B): Zero personal income tax (PwC reviewed 2026-01-11); 1% expatriate unemployment insurance (older EY guide, C). | Employer-sponsored LMRA work permit; 10-year renewable Golden Residency for residents with 5 yrs work history and BHD 2,000/mo basic salary (verified 2026-11-19). | T0-36 L237, L253, L264 |

## Appendix A: pillar score ledger

Every country's `[lo, mid, hi]` pillar interval, evidence grade and line-verified basis from `data/countries.json`.

| Country | Pillar | Interval [lo, mid, hi] | Grade | Basis and citations |
|---|---|---|---|---|
| United States (`US`) | `demand` | [9.3, 9.8, 10] | B | 1.12M PwC AI postings (2.8% share), 7.34% Indeed AI share, 1,697 JobsPipe AI Eng postings (T0-35 L58, L106, L122). |
| United States (`US`) | `pay_ppp` | [8.2, 9, 9.6] | M | Numbeo LPP 144.5 (Austin 158.8, Seattle 165.0, SF 151.0); post-rent surplus $107.5k-$160.0k USD (T0-35 L316-L320, L356, L375-L379). |
| United States (`US`) | `net_pay` | [9.4, 9.8, 10] | M | Highest global net pay: $161.9k (NYC) to $186.3k (Austin) on $255k sr SWE; ML p50 $285.7k (T0-35 L182, L194-L198). |
| United States (`US`) | `access_india` | [1, 1.8, 2.8] | B | Weighted H-1B lottery (2026-02-27), $100k fee litigation, and ~13-yr India EB-2/EB-3 backlog; O-1A/EB-1A narrow bypass (T0-35 L55, L413, L459, L578-L579). |
| United States (`US`) | `access_non_eu` | [3.2, 4.4, 5.6] | B | No India per-country green-card cap, but still gated by H-1B weighted lottery and policy litigation (T0-35 L413, L437, L578-L579). |
| United States (`US`) | `remote_reach` | [5, 6.3, 7.6] | B | 0 h 09:00-18:00 IST overlap and 67.4% US-only on WFH.team, yet US generates the largest pool of worldwide/EOR remote contracts for India (T0-35 L511-L515; T0-43 L58, L112, L186). |
| United States (`US`) | `ecosystem` | [9.6, 9.9, 10] | B | Dominant global hub: US+Canada $280B+ 2025 VC, OpenAI, Anthropic, Google, Meta, NVIDIA HQs (T0-35 L59, L544). |
| United States (`US`) | `stability` | [4.5, 5.6, 6.6] | B | Active immigration-policy volatility: weighted H-1B rule (Feb 2026) and $100k proclamation appeals pending (T0-35 L61, L578-L579). |
| Canada (`CA`) | `demand` | [7, 7.8, 8.4] | B | 18.97% Indeed AI share (#1 in T0-35), 3.5% PwC AI share (~129k postings), 124 JobsPipe AI Eng (T0-35 L58, L103, L118). |
| Canada (`CA`) | `pay_ppp` | [6.6, 7.4, 8.2] | M | Numbeo LPP 114.8 (Toronto 121.2, Montreal 126.7); post-rent disp. $49.9k-$75.8k USD (T0-35 L322-L323, L328, L361). |
| Canada (`CA`) | `net_pay` | [6.8, 7.6, 8.3] | M | Vancouver $99.8k and Toronto $84.1k USD net on sr SWE; EUR 100k net EUR 67.9k (T0-35 L201, L204, L236). |
| Canada (`CA`) | `access_india` | [6, 7, 7.8] | B | Fast GTS LMIA (10-12 bus days + 2 wks) and points-based PR, tempered by referral-partner cuts (58->41) and Express Entry STEM pause (T0-35 L414, L438, L580-L581). Realistic India GTS offer-to-start is 1-3 months (10-week IRCC India work-permit wait); H-1B pathway not launched as of 2026-11-19 (T0-38). |
| Canada (`CA`) | `access_non_eu` | [6, 7, 7.8] | B | Same GTS and Express Entry framework for non-EU nationals (T0-35 L414, L438, L580-L581). |
| Canada (`CA`) | `remote_reach` | [3.8, 4.8, 5.8] | C | 0 h 09:00-18:00 IST overlap; smaller cross-border remote hiring pool for India than US/UK (T0-35 L508-L510; T0-43 L112). |
| Canada (`CA`) | `ecosystem` | [7, 7.7, 8.3] | B | Deep-learning hubs in Toronto and Montreal, strong North American AI startup/lab links (T0-35 L544-L545). |
| Canada (`CA`) | `stability` | [6, 6.8, 7.6] | B | Stable rule of law, but immigration levers actively tightened in 2026 (GTS partners, Express Entry categories; T0-35 L580-L581). |
| United Kingdom (`GB`) | `demand` | [8, 8.6, 9.1] | B | 9.92% Indeed AI share, 2.2% PwC AI share, 224 JobsPipe AI Eng postings (#1 Europe; T0-35 L58, L105, L123). |
| United Kingdom (`GB`) | `pay_ppp` | [6, 6.8, 7.6] | M | Numbeo LPP 118.2; London post-rent disp. $57.9k USD on all-level ref (higher for senior/frontier labs; T0-35 L324, L358). |
| United Kingdom (`GB`) | `net_pay` | [7, 7.8, 8.6] | M | London $92.8k USD net on all-level ref (senior higher); EUR 100k gross yields EUR 70.6k net (T0-35 L202, L233). |
| United Kingdom (`GB`) | `access_india` | [6.6, 7.5, 8.2] | B | Fast Skilled Worker (~3 wks, GBP 41,700) + Global Talent (3-yr ILR) + UK-India social-security pact; Earned Settlement raises standard ILR baseline to 10 yrs unless GBP 50.3k+/125.1k+ (T0-35 L415, L461, L582-L583). UK-India CETA & Double Contribution Convention (60m detachment) in force 2026-07-15; HPI 2026 list (82) has zero Indian universities (T0-39). |
| United Kingdom (`GB`) | `access_non_eu` | [6.5, 7.4, 8.1] | B | Same Skilled Worker, Global Talent and Earned Settlement framework without UK-India secondment pact (T0-35 L415, L439, L461, L582). |
| United Kingdom (`GB`) | `remote_reach` | [7, 7.9, 8.6] | B | 3.5-4.5 h IST overlap, English, active UK-to-India remote/EOR hiring (PostHog UK entity, distributed tech firms; T0-35 L504-L505; T0-43 L112, L127). |
| United Kingdom (`GB`) | `ecosystem` | [8.3, 8.9, 9.4] | B | #1 European VC ($17.0B in 2025), OpenAI London hub, Anthropic London, DeepMind London, Cambridge research (T0-35 L59, L536, L556-L557). |
| United Kingdom (`GB`) | `stability` | [5.2, 6.2, 7.2] | B | Strong institutions, but Earned Settlement reform and recent non-dom/threshold churn raise immigration-rule risk (T0-35 L582). |
| Switzerland (`CH`) | `demand` | [5.6, 6.4, 7.2] | B | 1.8% PwC AI posting share; smaller absolute volume than UK/DE/FR, high quality concentration in Zurich (T0-35 L125, L159). |
| Switzerland (`CH`) | `pay_ppp` | [8.6, 9.3, 9.8] | M | #1 Numbeo LPP in Europe (165.7; Zurich 164.4) and $121.8k USD post-rent disp. surplus (T0-35 L318, L351, L390). |
| Switzerland (`CH`) | `net_pay` | [8.6, 9.2, 9.7] | M | #2 globally after US: Zurich $156.0k USD net; #1 at EUR 100k gross (EUR 77.6k net; T0-35 L199, L230). |
| Switzerland (`CH`) | `access_india` | [2.2, 3.2, 4.4] | B | Strict 8,500 third-country quota and Swiss/EU precedence test make non-EU sponsorship hard outside top MNCs/labs (T0-35 L420, L444, L593). |
| Switzerland (`CH`) | `access_non_eu` | [2.2, 3.2, 4.4] | B | Same 8,500 third-country quota and EU precedence applies to all non-EU/EFTA nationals (T0-35 L420, L444, L593). |
| Switzerland (`CH`) | `remote_reach` | [5, 6, 7] | C | 4.5-5.5 h IST overlap and strong pay, but small documented remote cross-border hiring volume from India (T0-35 L491; T0-43 L112). |
| Switzerland (`CH`) | `ecosystem` | [6.8, 7.5, 8.2] | B | $3.6B 2025 VC, Anthropic Zurich, ETH/EPFL talent pipeline and major US Big Tech R&D offices (T0-35 L59, L539, L560). |
| Switzerland (`CH`) | `stability` | [8, 8.7, 9.3] | B | 2026 quota held steady at 8,500; 10m population-cap referendum rejected 54.8% in June 2026 (T0-35 L593). |
| Germany (`DE`) | `demand` | [7.4, 8.1, 8.7] | B | 125k PwC AI postings (1.3% share), 5.74% Indeed AI share, largest EU Blue Card volume (56,300; T0-35 L58, L107, L127). |
| Germany (`DE`) | `pay_ppp` | [6.4, 7.1, 7.8] | M | Numbeo LPP 130.0 (Munich 142.7, Berlin 126.1); post-rent disp. $43.5k-$46.7k USD (T0-35 L331, L334, L360, L386-L387). |
| Germany (`DE`) | `net_pay` | [5.2, 6, 6.7] | M | Berlin $64.3k and Munich $63.4k USD net after 41.8% deductions; EUR 100k yields EUR 58.2k (T0-35 L210-L211, L246). |
| Germany (`DE`) | `access_india` | [8, 8.7, 9.3] | B | Clear, uncapped EU Blue Card (EUR 45,934.20 IT/shortage), Opportunity Card, and fast 21-27 mo PR (T0-35 L54, L417, L441, L463). Germany objects to Indian Hague Apostilles, requiring New Delhi digitised Urkundenueberpruefung (~8 wks, EUR 400-500) (T0-39). |
| Germany (`DE`) | `access_non_eu` | [8, 8.7, 9.3] | B | Same uncapped EU Blue Card, Opportunity Card and 21-27 mo PR path for all non-EU nationals (T0-35 L417, L441, L463). |
| Germany (`DE`) | `remote_reach` | [5.6, 6.6, 7.5] | B | 4.5-5.5 h IST overlap, large tech base, documented cross-border EOR/remote hiring (PostHog DE entity; T0-35 L492-L493; T0-43 L127). |
| Germany (`DE`) | `ecosystem` | [7.4, 8, 8.6] | B | $8.4B 2025 VC (#3 Europe), Anthropic Munich, EuroHPC AI Gigafactories participation, industrial AI base (T0-35 L59, L538, L558, L568). |
| Germany (`DE`) | `stability` | [7.4, 8.2, 8.8] | B | Predictable statutory Blue Card indexing and strong rule of law; EU Digital Omnibus clarifies AI Act timelines (T0-35 L417, L594). |
| Netherlands (`NL`) | `demand` | [6.3, 7, 7.7] | B | 57k PwC AI postings (2.1% share), 3.63% Indeed AI share, strong Amsterdam international tech market (T0-35 L110, L124, L157). |
| Netherlands (`NL`) | `pay_ppp` | [6.8, 7.6, 8.4] | M | Numbeo LPP 124.3 (Amsterdam 129.9); post-rent disp. $55.3k std or ~$75.8k with 30% ruling (T0-35 L254, L326, L355, L388). |
| Netherlands (`NL`) | `net_pay` | [7, 7.9, 8.7] | M | Amsterdam $87.0k USD net standard, rising to $107.4k under 30% ruling (27% from 2027; T0-35 L203, L254, L589). |
| Netherlands (`NL`) | `access_india` | [7, 7.8, 8.5] | B | Fast 2-week IND target via recognised sponsors (EUR 5,942/mo 30+, EUR 4,357 <30), English-first workplace (T0-35 L54, L418, L442). MVV sticker collected in New Delhi/Mumbai/Bengaluru in <=10 working days; non-EU HSM volume eased 16,100 (2024) to 13,900 (2025) (T0-39). |
| Netherlands (`NL`) | `access_non_eu` | [7, 7.8, 8.5] | B | Same recognised-sponsor HSRM route for all non-EU nationals (T0-35 L418, L442). |
| Netherlands (`NL`) | `remote_reach` | [6.4, 7.3, 8.1] | B | 4.5-5.5 h IST overlap, 16.4% Eurostat WFH (#3 EU), EF EPI #1 English, distributed EU tech employers (T0-35 L499, L523, L605). |
| Netherlands (`NL`) | `ecosystem` | [6.4, 7.1, 7.8] | B | $3.4B 2025 VC, deep European product/fintech/AI ecosystem in Amsterdam (T0-35 L59, L540). |
| Netherlands (`NL`) | `stability` | [6.2, 7, 7.8] | B | Strong institutions, tempered by 30%->27% expat-ruling reduction effective 2027-01-01 (T0-35 L589). |
| Ireland (`IE`) | `demand` | [7, 7.7, 8.3] | B | 15.02% Indeed AI share (#2 in T0-35) and 3.7% PwC AI share (#2 Europe), concentrated in Dublin (T0-35 L104, L117). |
| Ireland (`IE`) | `pay_ppp` | [5.6, 6.4, 7.2] | M | Numbeo LPP 113.0; Dublin post-rent disp. $47.7k USD on all-level ref due to ~$2,425/mo rent (T0-35 L330, L354). |
| Ireland (`IE`) | `net_pay` | [6.3, 7.1, 7.9] | M | Dublin $76.8k USD net on all-level ref (senior higher); EUR 100k yields EUR 64.5k (T0-35 L206, L239). |
| Ireland (`IE`) | `access_india` | [7.5, 8.2, 8.8] | B | Critical Skills from EUR 40,904 (Mar 2026), ~3-week backlog, English-speaking, 5-year settlement path (T0-35 L54, L416, L462, L584). |
| Ireland (`IE`) | `access_non_eu` | [7.5, 8.2, 8.8] | B | Same Critical Skills and 5-year settlement route for all non-EU nationals (T0-35 L416, L440, L462). |
| Ireland (`IE`) | `remote_reach` | [6.5, 7.4, 8.2] | B | 3.5-4.5 h IST overlap, 19.2% Eurostat WFH (#2 EU), English, US hyperscaler EMEA hubs (T0-35 L506, L522). |
| Ireland (`IE`) | `ecosystem` | [6.6, 7.3, 8] | B | Anthropic Dublin office plus EMEA HQs of major US cloud and AI employers (T0-35 L554). |
| Ireland (`IE`) | `stability` | [7.2, 8, 8.7] | B | Published phased Critical Skills salary schedule to 2030 gives transparent predictability (T0-35 L584). |
| France (`FR`) | `demand` | [6.8, 7.5, 8.1] | B | ~178k PwC AI postings (1.3% share) and 4.53% Indeed AI share, anchored in Paris (T0-35 L109, L128). |
| France (`FR`) | `pay_ppp` | [5, 5.8, 6.6] | M | Numbeo LPP 113.3; Paris post-rent disp. $37.4k USD std (~$44.6k impatriate; T0-35 L255, L339, L363). |
| France (`FR`) | `net_pay` | [4.8, 5.6, 6.4] | M | Paris $56.6k USD net std ($63.8k impatriate); EUR 100k yields EUR 61.5k (T0-35 L215, L243, L255). |
| France (`FR`) | `access_india` | [6, 6.9, 7.7] | B | Talent Passport (~EUR 39.6k) and EU Blue Card (EUR 59,373) provide structured routes; French language slows broader mobility (T0-35 L419, L443, L617). |
| France (`FR`) | `access_non_eu` | [6, 6.9, 7.7] | B | Same Talent Passport and Blue Card framework for non-EU nationals (T0-35 L419, L443). |
| France (`FR`) | `remote_reach` | [4.6, 5.5, 6.4] | C | 4.5-5.5 h IST overlap, but lower English score (EF EPI 539) limits remote-from-India demand outside Paris AI labs (T0-35 L497, L617). |
| France (`FR`) | `ecosystem` | [7.6, 8.3, 8.9] | B | $8.5B 2025 VC (#2 Europe), Anthropic Paris (announced Nov 2025), major sovereign and open-weights AI startup hub (T0-35 L59, L537, L559). |
| France (`FR`) | `stability` | [6, 6.8, 7.6] | B | Stable Talent Passport and impatriate framework; EU AI Act Digital Omnibus eases near-term compliance (T0-35 L419, L594). |
| Israel (`IL`) | `demand` | [5.8, 6.7, 7.6] | C | Dense AI startup and MNC R&D hiring in Tel Aviv, though excluded from PwC/Indeed share tables (T0-35 L172, L546). |
| Israel (`IL`) | `pay_ppp` | [7, 7.8, 8.5] | M | Numbeo LPP 115.0; Tel Aviv post-rent disp. $83.9k USD (#4 globally after US/CH/SG; T0-35 L321, L352). |
| Israel (`IL`) | `net_pay` | [7.6, 8.3, 8.9] | M | Tel Aviv $110.3k USD net (#3 outside US); EUR 100k yields EUR 70.2k (T0-35 L200, L234). |
| Israel (`IL`) | `access_india` | [2, 3, 4] | B | B/1 expert permit at 2x avg wage, 63-month hard cumulative cap, no non-aliyah settlement route read (T0-35 L431, L455, L477). |
| Israel (`IL`) | `access_non_eu` | [2, 3, 4] | B | Same B/1 2x avg-wage test and 63-month cap for generic non-EU nationals (T0-35 L431, L455, L477). |
| Israel (`IL`) | `remote_reach` | [4.8, 5.8, 6.8] | C | Strong 5.5-6.5 h IST overlap and English R&D culture, but thin documented cross-border hiring from India (T0-35 L489). |
| Israel (`IL`) | `ecosystem` | [7.2, 8, 8.7] | C | High AI startup density (~$11.8B broad AI VC definition in T0-35) and major MNC R&D centres (T0-35 L546). |
| Israel (`IL`) | `stability` | [2.4, 3.6, 4.8] | C | Ongoing regional security and geopolitical conflict risk plus 63-month stay cap (T0-35 L477, L767). |
| Sweden (`SE`) | `demand` | [5.5, 6.3, 7] | B | 3.1% PwC AI posting share; active Stockholm tech hub, moderate absolute volume (T0-35 L121, L160). |
| Sweden (`SE`) | `pay_ppp` | [5.6, 6.4, 7.2] | M | Numbeo LPP 128.6; Stockholm post-rent disp. $42.6k USD (T0-35 L335, L364). |
| Sweden (`SE`) | `net_pay` | [5, 5.8, 6.6] | M | Stockholm $61.6k USD net (low-conf model); EUR 100k yields EUR 66.3k (T0-35 L213, L237). |
| Sweden (`SE`) | `access_india` | [5.6, 6.5, 7.3] | B | Employer work permit at 90% median wage (~4 mo); settlement path not collected in T0-35 (T0-35 L421, L445, L467, L585). |
| Sweden (`SE`) | `access_non_eu` | [5.6, 6.5, 7.3] | B | Same employer work-permit regime for non-EU nationals (T0-35 L421, L445, L585). |
| Sweden (`SE`) | `remote_reach` | [5.4, 6.3, 7.2] | B | 4.5-5.5 h IST overlap, 15.6% Eurostat WFH (#4 EU), strong English (EF EPI 609; T0-35 L503, L524, L611). |
| Sweden (`SE`) | `ecosystem` | [5.4, 6.2, 7] | C | Strong Nordic consumer/product tech hub in Stockholm, moderate AI VC scale (T0-35 L160, L543). |
| Sweden (`SE`) | `stability` | [6.4, 7.2, 8] | B | Strong institutions; work-permit threshold rose from 80% to 90% of median salary in 2026 (T0-35 L585). |
| Denmark (`DK`) | `demand` | [4.8, 5.6, 6.4] | B | 3.2% PwC AI posting share; small total market volume (T0-35 L120, L161). |
| Denmark (`DK`) | `pay_ppp` | [6.6, 7.4, 8.2] | M | Numbeo LPP 141.2 (#2 in Europe after CH); Copenhagen post-rent disp. $51.0k USD (T0-35 L327, L357). |
| Denmark (`DK`) | `net_pay` | [6, 6.8, 7.6] | M | Copenhagen $74.5k USD net std ($79.5k key-employee scheme); small n=52 (T0-35 L207, L256). |
| Denmark (`DK`) | `access_india` | [5.6, 6.5, 7.4] | B | Pay Limit Scheme (DKK 552,000/yr, ~1 mo) is fast for entry; settlement path not collected (T0-35 L422, L446, L468). |
| Denmark (`DK`) | `access_non_eu` | [5.6, 6.5, 7.4] | B | Same Pay Limit Scheme for non-EU nationals (T0-35 L422, L446). |
| Denmark (`DK`) | `remote_reach` | [4.5, 5.4, 6.3] | C | 4.5-5.5 h IST overlap and high English (EF EPI 611), small remote-hiring volume from India (T0-35 L494, L610). |
| Denmark (`DK`) | `ecosystem` | [4.8, 5.5, 6.3] | C | Strong life-sciences/compute research niche, modest AI startup volume (T0-35 L120, L543). |
| Denmark (`DK`) | `stability` | [7.4, 8.2, 8.9] | B | High institutional stability and clear Pay Limit indexing (T0-35 L422). |
| Finland (`FI`) | `demand` | [4.2, 5, 5.8] | C | Small Nordic market; $2.2B all-sector 2025 VC, excluded from PwC/Indeed AI share tables (T0-35 L162, L542). |
| Finland (`FI`) | `pay_ppp` | [5.4, 6.2, 7] | M | Numbeo LPP 119.8; Helsinki post-rent disp. $38.0k USD on all-level ref (T0-35 L336, L362). |
| Finland (`FI`) | `net_pay` | [4.4, 5.2, 6] | M | Helsinki $52.0k USD net std ($55.7k key-employee 25%); low-conf tax model (T0-35 L218, L257). |
| Finland (`FI`) | `access_india` | [6.6, 7.4, 8.2] | B | Fast-track Specialist permit (2-week target, EUR 3,937/mo); settlement not collected in T0-35 (T0-35 L56, L423, L447, L469). |
| Finland (`FI`) | `access_non_eu` | [6.6, 7.4, 8.2] | B | Same 2-week fast-track Specialist route for non-EU nationals (T0-35 L423, L447). |
| Finland (`FI`) | `remote_reach` | [5.6, 6.5, 7.4] | B | 5.5-6.5 h IST overlap and #1 EU Eurostat WFH share (20.5%), tempered by small volume (T0-35 L488, L521). |
| Finland (`FI`) | `ecosystem` | [4.8, 5.6, 6.4] | B | $2.2B 2025 VC, LUMI/EuroHPC supercomputing footprint, strong engineering culture (T0-35 L542, L568). |
| Finland (`FI`) | `stability` | [7.4, 8.1, 8.8] | B | Key-employee tax improved (32%->25%) and stable fast-track permit regime (T0-35 L587). |
| Norway (`NO`) | `demand` | [3.8, 4.6, 5.4] | B | 0.8-0.9% PwC AI posting share (lowest measured in Europe) and small Oslo tech volume (T0-35 L129, L163). |
| Norway (`NO`) | `pay_ppp` | [5.6, 6.4, 7.2] | M | Numbeo LPP 123.2; Oslo post-rent disp. $49.1k USD despite high non-rent costs (T0-35 L329, L353). |
| Norway (`NO`) | `net_pay` | [5.6, 6.4, 7.2] | M | Oslo $67.8k USD net on all-level ref; EUR 100k yields EUR 68.6k (T0-35 L208, L235). |
| Norway (`NO`) | `access_india` | [6, 6.9, 7.7] | B | Skilled-worker permit with no fixed statutory floor and 3-year PR path (tightened simultaneous checks 2025-09-01; T0-35 L424, L470, L586). |
| Norway (`NO`) | `access_non_eu` | [6, 6.9, 7.7] | B | Same skilled-worker and 3-year PR rules for non-EU nationals (T0-35 L424, L470). |
| Norway (`NO`) | `remote_reach` | [4.2, 5.1, 6] | C | 4.5-5.5 h IST overlap and high English (EF EPI 613), very small remote cross-border market (T0-35 L500, L608). |
| Norway (`NO`) | `ecosystem` | [3.8, 4.6, 5.4] | C | Small AI startup/lab ecosystem relative to neighbouring Nordics and Western Europe (T0-35 L129, L543). |
| Norway (`NO`) | `stability` | [7.4, 8.2, 8.9] | B | Very high macro and institutional stability; minor PR verification tightening in Sep 2025 (T0-35 L586). |
| Spain (`ES`) | `demand` | [5.8, 6.6, 7.3] | B | 4.0% PwC AI posting share (#1 in Europe) and growing Barcelona/Madrid tech hubs (T0-35 L116, L164-L165). |
| Spain (`ES`) | `pay_ppp` | [4.8, 5.6, 6.4] | M | Numbeo LPP 96.8; post-rent disp. $37.7k-$38.0k USD (T0-35 L337-L338, L367). |
| Spain (`ES`) | `net_pay` | [4.8, 5.5, 6.2] | M | Barcelona $56.7k and Madrid $55.1k USD net std ($58.2k Beckham Law; T0-35 L214, L217, L258). |
| Spain (`ES`) | `access_india` | [6.2, 7.1, 7.9] | B | 20-day target Highly Qualified Professional permit and updated EU Blue Card; settlement not collected in T0-35 (T0-35 L425, L449, L592). |
| Spain (`ES`) | `access_non_eu` | [6.2, 7.1, 7.9] | B | Same HQA and EU Blue Card access for non-EU nationals (T0-35 L425, L449, L592). |
| Spain (`ES`) | `remote_reach` | [4.8, 5.6, 6.5] | C | 4.5-5.5 h IST overlap, international Barcelona hubs, moderate English (EF EPI 540; T0-35 L495-L496, L616). |
| Spain (`ES`) | `ecosystem` | [5.2, 6, 6.8] | B | $2.9B 2025 VC, Barcelona Supercomputing Center / EU AI hub presence (T0-35 L541, L568). |
| Spain (`ES`) | `stability` | [6.6, 7.4, 8.1] | B | Stable Beckham Law and HQA framework; Blue Card indexed at 1.4x avg wage (T0-35 L592). |
| Poland (`PL`) | `demand` | [5.6, 6.4, 7.2] | B | 3.5% PwC AI posting share (#3 Europe) and major Warsaw/Krakow MNC engineering hubs (T0-35 L119, L168-L169). |
| Poland (`PL`) | `pay_ppp` | [5, 5.8, 6.7] | M | Lowest living-cost index in T0-35 (32.6); post-rent disp. $29.5k-$30.5k employee ref, higher on B2B (T0-35 L340-L341, L369; T0-43 L307). |
| Poland (`PL`) | `net_pay` | [4, 4.9, 6] | M | Warsaw $44.3k USD employee net on all-level ref; senior B2B AI roles quoted $74k-$92k gross (T0-35 L219; T0-43 L307). |
| Poland (`PL`) | `access_india` | [6, 6.9, 7.7] | B | EU Blue Card (PLN 13,355/mo) with min contract cut to 6 months; settlement not collected (T0-35 L428, L452, L590). |
| Poland (`PL`) | `access_non_eu` | [6, 6.9, 7.7] | B | Same Blue Card rules for non-EU nationals (T0-35 L428, L452, L590). |
| Poland (`PL`) | `remote_reach` | [4.6, 5.5, 6.4] | C | 4.5-5.5 h IST overlap and high English (EF EPI 600), though Poland itself competes as a nearshore hub rather than hiring India remotely (T0-35 L501-L502, L613; T0-43 L307). |
| Poland (`PL`) | `ecosystem` | [4.8, 5.6, 6.4] | C | Strong MNC R&D and applied-AI engineering hubs in Warsaw and Krakow (T0-35 L119, L168-L169). |
| Poland (`PL`) | `stability` | [6.4, 7.2, 8] | B | EU/Schengen framework with streamlined 6-month Blue Card contract rule (T0-35 L590). |
| Austria (`AT`) | `demand` | [4.2, 5, 5.8] | C | Smaller Central European tech market centred on Vienna; excluded from PwC/Indeed AI share tables (T0-35 L171). |
| Austria (`AT`) | `pay_ppp` | [6, 6.8, 7.6] | M | Numbeo LPP 114.2 (Vienna 133.5); post-rent disp. $46.3k USD (T0-35 L332, L359, L402). |
| Austria (`AT`) | `net_pay` | [5.2, 6, 6.8] | M | Vienna $62.0k USD net (small n=45); EUR 100k yields EUR 62.7k (T0-35 L212, L242). |
| Austria (`AT`) | `access_india` | [6.4, 7.2, 8] | B | Red-White-Red Card (70 pts) leading to RWR+ after 21 of 24 months (T0-35 L430, L454, L476). |
| Austria (`AT`) | `access_non_eu` | [6.4, 7.2, 8] | B | Same RWR Card and 21-month RWR+ path for non-EU nationals (T0-35 L430, L476). |
| Austria (`AT`) | `remote_reach` | [4.2, 5, 5.9] | C | 4.5-5.5 h IST overlap and #2 EF EPI English (616), limited cross-border remote volume (T0-35 L490, L606). |
| Austria (`AT`) | `ecosystem` | [4, 4.8, 5.6] | C | Research/corporate hub in Vienna without major frontier-lab offices (T0-35 L171, L543). |
| Austria (`AT`) | `stability` | [7.2, 8, 8.7] | B | High institutional stability and clear RWR points rules (T0-35 L430, L476). |
| Estonia (`EE`) | `demand` | [2.8, 3.6, 4.5] | C | Very small national market (Tallinn n=107 SWE), not in PwC/Indeed AI share tables (T0-35 L170). |
| Estonia (`EE`) | `pay_ppp` | [5.6, 6.4, 7.2] | M | Low rent ($789/mo) and 21.9% tax yield $45.7k USD post-rent disp. despite moderate gross (T0-35 L333, L366). |
| Estonia (`EE`) | `net_pay` | [4.6, 5.4, 6.2] | M | Tallinn $55.1k USD net on all-level ref; #2 in Europe at EUR 100k gross (EUR 77.0k; T0-35 L216, L231). |
| Estonia (`EE`) | `access_india` | [6, 6.9, 7.7] | B | Straightforward digital employment permit at national average salary; top-specialist quota exemption (T0-35 L429, L453). |
| Estonia (`EE`) | `access_non_eu` | [6, 6.9, 7.7] | B | Same employment-permit regime for non-EU nationals (T0-35 L429, L453). |
| Estonia (`EE`) | `remote_reach` | [5, 5.9, 6.8] | C | 5.5-6.5 h IST overlap and digital-first startup culture, constrained by tiny employer count (T0-35 L487, L615). |
| Estonia (`EE`) | `ecosystem` | [3.8, 4.6, 5.4] | C | High startup density per capita in Tallinn, tiny absolute AI scale (T0-35 L170). |
| Estonia (`EE`) | `stability` | [7, 7.8, 8.5] | B | Digital-government predictability; 22% flat income tax retained for 2026 (T0-35 L588). |
| Portugal (`PT`) | `demand` | [3, 3.8, 4.6] | C | Small Lisbon tech/nearshore hub; excluded from PwC/Indeed AI share tables (T0-35 L166). |
| Portugal (`PT`) | `pay_ppp` | [2.4, 3.2, 4.2] | M | Lowest Numbeo LPP in T0-35 (65.3; Lisbon 60.9); post-rent disp. only $21.3k USD (T0-35 L342, L368, L397). |
| Portugal (`PT`) | `net_pay` | [3, 3.8, 4.6] | M | Lisbon $37.2k USD net std ($39.0k IFICI); EUR 100k yields EUR 57.4k (T0-35 L221, L247, L259). |
| Portugal (`PT`) | `access_india` | [5.4, 6.4, 7.4] | C | Low nominal Blue Card threshold (~EUR 21k secondary source), offset by AIMA processing delays (T0-35 L426, L450). |
| Portugal (`PT`) | `access_non_eu` | [5.4, 6.4, 7.4] | C | Same Blue Card / D3 framework for non-EU nationals (T0-35 L426, L450). |
| Portugal (`PT`) | `remote_reach` | [4.2, 5.1, 6] | C | 3.5-4.5 h IST overlap and strong English (EF EPI 612), small domestic remote-hiring employer base (T0-35 L507, L609). |
| Portugal (`PT`) | `ecosystem` | [3.2, 4, 4.8] | C | Small European startup/remote-worker hub without frontier AI lab offices (T0-35 L166). |
| Portugal (`PT`) | `stability` | [5.6, 6.5, 7.4] | C | Stable EU framework, tempered by NHR->IFICI transition and AIMA administrative delays (T0-35 L272, L426). |
| Italy (`IT`) | `demand` | [4.2, 5, 5.8] | B | 4.76% Indeed AI share and 1.7% PwC AI share, moderate tech hiring in Milan (T0-35 L108, L126). |
| Italy (`IT`) | `pay_ppp` | [2, 3.2, 4.8] | M | Numbeo LPP 85.5; Milan disp. $7.1k on n=18 is distorted by tiny sample, hence wide band (T0-35 L224, L343, L365). |
| Italy (`IT`) | `net_pay` | [2.2, 3.4, 5] | M | Milan $27.7k USD net on n=18 (unreliable); EUR 100k yields EUR 57.3k std (lowest in Europe; T0-35 L222, L248). |
| Italy (`IT`) | `access_india` | [3.8, 4.8, 5.8] | B | Blue Card outside quota (~EUR 36k), but only 633 Blue Cards issued in 2024 signals high friction (T0-35 L427, L451, L473, L591). |
| Italy (`IT`) | `access_non_eu` | [3.8, 4.8, 5.8] | B | Same Blue Card friction (633 issued in 2024) for non-EU nationals (T0-35 L427, L473). |
| Italy (`IT`) | `remote_reach` | [2.5, 3.4, 4.4] | B | 4.5-5.5 h IST overlap, but lowest Eurostat WFH share (2.7%) and lower English (EF EPI 513; T0-35 L498, L525, L619). |
| Italy (`IT`) | `ecosystem` | [3.6, 4.4, 5.2] | C | Enterprise/industrial AI adoption in Milan/Turin; limited frontier-lab or AI VC density (T0-35 L126, L543). |
| Italy (`IT`) | `stability` | [5.6, 6.4, 7.2] | B | EU framework; Blue Card floor raised and inpatriate rules tightened in 2024-2026 (T0-35 L273, L591). |
| Singapore (`SG`) | `demand` | [7.6, 8.3, 8.9] | B | 340 aimlroles, #1 JobsPipe AI share (3.7%), #1 Lightcast AI share (4.69%), 1.82% LinkedIn AI talent conc. (T0-36 L58-L60, L109, L141-L142). |
| Singapore (`SG`) | `pay_ppp` | [7.4, 8.2, 8.9] | M | 66.0% of gross kept after tax and rent at ML R1 ($77.0k-$83.7k disp. across Jun/Nov rent; T0-36 L208, L276, L1168). |
| Singapore (`SG`) | `net_pay` | [8, 8.7, 9.2] | M | $115.7k USD net at ML R1 ($139.8k R2); only 7.0% tax at $100k gross (T0-36 L208-L209, L238). |
| Singapore (`SG`) | `access_india` | [5.4, 6.2, 7] | B | Fast EP + COMPASS (S$6,000 from 2027-01-01) and ONE Pass AI & Tech track (2027-01-28), but discretionary PR with no published timeline caps settlement certainty (T0-36 L56, L305, L360-L361, L556). COMPASS C3 awards 0 diversity pts if one nationality >=25% of firm's PMETs (exempt at >=S$22.5k fixed) (T0-42). |
| Singapore (`SG`) | `access_non_eu` | [5.4, 6.2, 7] | B | Same fast EP/COMPASS, ONE Pass and opaque discretionary PR rules for non-EU nationals (T0-36 L305, L360-L361). |
| Singapore (`SG`) | `remote_reach` | [6.2, 7.1, 8] | B | 6.5 h IST overlap, English, APAC HQs hiring remote/GCC India teams (local remote share 1.6% JobRise Oct 2026; T0-36 L325, L382). |
| Singapore (`SG`) | `ecosystem` | [7.8, 8.5, 9.1] | B | OpenAI Asia HQ, Anthropic (opened 2026-10-14), Google DeepMind, $1.82B AI VC, sovereign AI strategy (T0-36 L66, L343). |
| Singapore (`SG`) | `stability` | [7.8, 8.6, 9.2] | B | High institutional predictability; 2027 EP and ONE Pass AI/Tech changes announced well in advance (T0-36 L360-L361). |
| India (`IN`) | `demand` | [8.2, 8.8, 9.3] | B | 1,558 aimlroles postings (#1 APAC; BLR 575, HYD 163, Pune 151), 398 JobsPipe AI Eng (3.0%, 21.2% entry), 2,117 GCCs (T0-36 L58-L59, L102-L108, L126-L134). |
| India (`IN`) | `pay_ppp` | [5.6, 7, 8.2] | M | 70.2% of gross kept after tax & rent at BLR Levels.fyi R1 ($33.2k disp. on $335/mo rent), but wide 2x-4x gap to broad market (T0-36 L57, L204, L1261). |
| India (`IN`) | `net_pay` | [3.6, 4.8, 6.2] | M | BLR Levels.fyi ML R1 $37.2k net / R2 $51.1k (top Big Tech/product sr >$100k, broad market <$15k; T0-36 L204-L205; T0-43 L179-L181). |
| India (`IN`) | `access_india` | [9.6, 10, 10] | A | Home market for Indian citizens: zero visa friction or sponsorship dependency (T0-36 L310). |
| India (`IN`) | `access_non_eu` | [2.5, 4, 5.5] | B | Foreign Employment Visa requires USD 25,000 gross minimum and lacks a standard PR route for non-OCI foreigners (T0-36 L310, L1231). |
| India (`IN`) | `remote_reach` | [4, 5.4, 6.6] | B | Home base (8 h IST), but domestic remote-tagged tech share is only 0.8% (Oct 2026); remote roles exist via GCCs/foreign entities (T0-36 L324; T0-43 L59, L111). |
| India (`IN`) | `ecosystem` | [7, 7.7, 8.4] | B | $4.09B AI VC (108 new AI cos), 2,117 GCCs, IndiaAI Mission GPU build-out, strong talent base (T0-36 L129-L134, L342, L1143). |
| India (`IN`) | `stability` | [6.4, 7.2, 8] | B | Income-tax Act 2025 took effect smoothly with unchanged slabs; Four Labour Codes (Nov 2025) and FEMA 2026 regs settling in (T0-36 L374; T0-43 L243-L248). |
| Australia (`AU`) | `demand` | [6.4, 7.1, 7.8] | B | 87 aimlroles (Sydney 43, Melbourne 23), 1.78% Lightcast AI posting share, positive LinkedIn AI migration (T0-36 L115, L141, L144). |
| Australia (`AU`) | `pay_ppp` | [6.4, 7.2, 8] | M | 50.4% of gross kept after tax & Sydney rent ($61.7k USD disp. at R1; T0-36 L226, L289). |
| Australia (`AU`) | `net_pay` | [7, 7.8, 8.5] | M | $87.6k USD net at ML R1 (28.4% tax); $74.0k net at $100k gross (T0-36 L226, L243). |
| Australia (`AU`) | `access_india` | [6.8, 7.6, 8.4] | B | Skills in Demand 482 (Specialist 53-57 d), clear 186/189/190 PR and India-specific MATES (3,000/yr); Core Skills slow (7-10 mo; T0-36 L316, L364). |
| Australia (`AU`) | `access_non_eu` | [6.2, 7.1, 7.9] | B | Same 482 and 186/189/190 PR framework without India MATES allocation (T0-36 L316, L364). |
| Australia (`AU`) | `remote_reach` | [4.8, 5.8, 6.8] | C | 3.5-4.5 h IST overlap and English, though cross-border remote share from India is unmeasured (T0-36 L331, L382). |
| Australia (`AU`) | `ecosystem` | [6.2, 6.9, 7.6] | B | $2.52B AI VC, Anthropic Sydney (COI, downgraded from A to B on Extract), strong enterprise/SaaS AI hub (T0-36 L130, L352, L1033). |
| Australia (`AU`) | `stability` | [7.4, 8.2, 8.9] | B | Predictable annual threshold indexing, mandatory AI guardrails dropped, stable PR institutions (T0-36 L364-L365). |
| United Arab Emirates (`AE`) | `demand` | [5, 6, 7] | B | 32 aimlroles (Dubai 21, Abu Dhabi 19), 2.87% Lightcast AI share, #1 LinkedIn net AI migration (4.40/10k), 64% GenAI adoption (T0-36 L118, L141-L145). |
| United Arab Emirates (`AE`) | `pay_ppp` | [5.6, 7, 8.2] | M | 0% PIT yields 57%-71% kept after rent ($37.8k R1 / $69.9k R2), but Dubai rent may be understated 25-40% and pay swings widely (T0-36 L210-L211, L278-L280). |
| United Arab Emirates (`AE`) | `net_pay` | [5.8, 7.2, 8.6] | M | 0% PIT ($100k gross = $100k net); ML R1 $65.9k / R2 $98.0k, sovereign/senior higher, Dubai median lower ($42k; T0-36 L162-L165, L210-L211, L236). |
| United Arab Emirates (`AE`) | `access_india` | [6.2, 7, 7.8] | B | Fast employer-sponsored permit and 10-yr Golden Visa (AED 30k/mo), tempered by absence of permanent residency or citizenship path (T0-36 L306, L362). UAE is NOT a Hague Apostille member (requires MEA + UAE Embassy + MOFA legalisation chain) (T0-41). |
| United Arab Emirates (`AE`) | `access_non_eu` | [6.2, 7, 7.8] | B | Same fast employer permit and 10-yr Golden Visa with no permanent residency for non-EU nationals (T0-36 L306). |
| United Arab Emirates (`AE`) | `remote_reach` | [6, 7, 7.9] | C | 7.5 h IST overlap (#1 outside India), English business culture, active India-Gulf contractor corridor (remote share unmeasured; T0-36 L326, L384). |
| United Arab Emirates (`AE`) | `ecosystem` | [5.6, 6.6, 7.6] | C | G42, MBZUAI, TII, sovereign AI push; Stargate UAE 200MW energisation not confirmed as of Oct 2026 (T0-36 L344, L632). |
| United Arab Emirates (`AE`) | `stability` | [3.5, 4.8, 6] | C | 0% PIT stable, but 2026 US-Iran conflict brought EASA conflict bulletins, Nov 2026 flight disruptions and threats to Gulf data centres (T0-36 L627-L632, L1144). |
| Saudi Arabia (`SA`) | `demand` | [4.5, 5.5, 6.5] | C | 23 aimlroles postings, fast AI-talent growth and net migration, driven by sovereign build-out (T0-36 L119, L143-L144). |
| Saudi Arabia (`SA`) | `pay_ppp` | [5.4, 6.8, 8] | M | 0% PIT and modest Riyadh rent ($870/mo) leave $46.9k-$61.5k disp. (82%-86% of gross), on C-grade pay inputs (T0-36 L212, L291). |
| Saudi Arabia (`SA`) | `net_pay` | [5, 6.5, 8] | M | 0% PIT ($100k gross = $100k net); Riyadh pay estimated $57.3k-$88.8k across C-grade sources (T0-36 L167, L212, L236). |
| Saudi Arabia (`SA`) | `access_india` | [4.4, 5.5, 6.6] | C | Employer iqama available, but 30% engineering Saudization (Jun 2026) and Qiwa permits for Premium Residency raise friction; no PR (T0-36 L307, L586-L588). |
| Saudi Arabia (`SA`) | `access_non_eu` | [4.4, 5.5, 6.6] | C | Same iqama, Saudization and Qiwa rules for non-EU nationals (T0-36 L307, L586-L588). |
| Saudi Arabia (`SA`) | `remote_reach` | [4, 5, 6] | C | 6.5 h IST overlap, but sovereign/localisation policies favour on-site presence; remote share unmeasured (T0-36 L327, L384). |
| Saudi Arabia (`SA`) | `ecosystem` | [5.4, 6.4, 7.4] | C | HUMAIN sovereign AI company and $2.03B AI VC (ahead of Singapore in T0-36 Quid tally; T0-36 L135, L345). |
| Saudi Arabia (`SA`) | `stability` | [3, 4.3, 5.6] | C | 0% PIT intact, but 2026 US-Iran regional conflict risk plus Saudization/Qiwa labour-rule changes (T0-36 L375, L586-L588, L627-L632). |
| Japan (`JP`) | `demand` | [5.6, 6.4, 7.2] | B | 27.2% entry-level AI share on JobsPipe (#1 measured), solid Tokyo corporate/foreign hiring (T0-36 L58, L111, L127). |
| Japan (`JP`) | `pay_ppp` | [4.4, 5.3, 6.3] | M | 44.8%-52.4% of gross kept after tax & rent ($23.0k R1 / $48.5k R2; moderate Tokyo rent; T0-36 L215-L216, L283). |
| Japan (`JP`) | `net_pay` | [3.8, 4.9, 6.2] | M | Tokyo $38.0k net at R1 / $63.5k at R2; 32.6% tax at $100k (highest in T0-36; T0-36 L215-L216, L247). |
| Japan (`JP`) | `access_india` | [6, 7, 7.8] | B | HSP 70/80-point fast-track to 1-3 yr PR, tempered by reported minimum-income rise and Apr 2027 PR tightening (T0-36 L312, L368, L599). Japan Digital Nomad Visa excludes Indian citizens (T0-42). |
| Japan (`JP`) | `access_non_eu` | [6, 7, 7.8] | B | Same HSP points and 1-3 yr PR route for non-EU nationals (T0-36 L312, L368). |
| Japan (`JP`) | `remote_reach` | [3, 4, 5] | C | 5.5 h IST overlap, but strong Japanese-language and on-site culture limit remote-from-India hiring (T0-36 L330, L385). |
| Japan (`JP`) | `ecosystem` | [6, 6.8, 7.5] | C | Anthropic Tokyo, robotics/industrial AI leaders, light-touch AI Promotion Act (T0-36 L348, L369). |
| Japan (`JP`) | `stability` | [6.4, 7.2, 8] | B | Very safe macro environment; light-touch AI law; PR rules tightening in 2027 (T0-36 L368-L369, L599). |
| South Korea (`KR`) | `demand` | [5.6, 6.4, 7.2] | B | Strong LinkedIn AI talent concentration, high GenAI adoption, solid Seoul tech hiring (T0-36 L112, L142, L145). |
| South Korea (`KR`) | `pay_ppp` | [6.2, 7, 7.8] | M | 59% of gross kept after tax & rent ($51.2k R1 / $62.3k R2 on ~$1,290/mo rent; T0-36 L217-L218, L285). |
| South Korea (`KR`) | `net_pay` | [6, 6.8, 7.6] | M | Seoul $66.6k net at R1 / $77.7k at R2; 25.6% tax at $100k (T0-36 L217-L218, L242). |
| South Korea (`KR`) | `access_india` | [5.4, 6.4, 7.3] | C | K-Tech Pass widens 3-yr PR path for top tech talent alongside E-7, though Korean language narrows roles (T0-36 L313, L370, L386). |
| South Korea (`KR`) | `access_non_eu` | [5.4, 6.4, 7.3] | C | Same E-7 and K-Tech Pass pathways for non-EU nationals (T0-36 L313, L370). |
| South Korea (`KR`) | `remote_reach` | [2.8, 3.8, 4.8] | C | 5.5 h IST overlap, but Korean language and on-site employer culture restrict remote-from-India roles (T0-36 L330, L386). |
| South Korea (`KR`) | `ecosystem` | [6.2, 7, 7.8] | C | Naver, Kakao, HBM/AI semiconductor leaders, Anthropic Seoul (COI, downgraded from A to B; T0-36 L349, L1141). |
| South Korea (`KR`) | `stability` | [6, 6.8, 7.6] | C | AI Basic Act live Jan 2026 (1-yr grace) and 19% flat tax sunsetting Dec 2026; K-Tech Pass expanded (T0-36 L370-L371). |
| Hong Kong (`HK`) | `demand` | [4.8, 5.7, 6.6] | B | 3.48% Lightcast AI posting share (#2 APAC) and positive AI migration, concentrated in finance/quant (T0-36 L114, L141, L144, L351). |
| Hong Kong (`HK`) | `pay_ppp` | [5.2, 6.2, 7.2] | M | 52%-61% kept after tax & rent ($37.6k SWE R1 / $62.0k R2) on ~$2,200/mo rent (T0-36 L221-L222, L281). |
| Hong Kong (`HK`) | `net_pay` | [6, 7.2, 8.4] | M | Low 12-15% tax ($86.5k net at $100k gross); SWE R1 $63.9k / R2 $88.3k (quant/ML higher; T0-36 L221-L223, L239). |
| Hong Kong (`HK`) | `access_india` | [6.4, 7.3, 8.1] | B | TTPS (HK$2.5m or top-200 universities, verified 2026-11-19) & GEP fast (~4-6 wks), clear 7-year PR (T0-36 L315, L372, L1063, L1230). |
| Hong Kong (`HK`) | `access_non_eu` | [6.4, 7.3, 8.1] | B | Same TTPS, GEP and 7-year PR framework for non-EU nationals (T0-36 L315, L372). |
| Hong Kong (`HK`) | `remote_reach` | [4.6, 5.5, 6.5] | C | 6.5 h IST overlap and English finance sector, but thin cross-border remote hiring from India (T0-36 L329, L383). |
| Hong Kong (`HK`) | `ecosystem` | [4.8, 5.6, 6.4] | C | Strong quant/fintech AI demand, no major frontier AI lab offices documented in T0-36 (T0-36 L351). |
| Hong Kong (`HK`) | `stability` | [5.4, 6.3, 7.2] | C | Stable tax and expanded TTPS rules, weighed against broader political/regulatory alignment risk (T0-36 L372). |
| New Zealand (`NZ`) | `demand` | [3.2, 4, 4.8] | B | Small national market; high GenAI adoption, small absolute AI job postings (T0-36 L116, L141, L145). |
| New Zealand (`NZ`) | `pay_ppp` | [4.6, 5.6, 6.6] | D | Net pay $59.4k-$82.1k on thin sample; Auckland rent not retrieved in T0-36 (T0-36 L227-L228, L297). |
| New Zealand (`NZ`) | `net_pay` | [4.6, 5.8, 7] | M | NZ $59.4k net at thin R1 / $82.1k at R2 (Glassdoor base NZ$95k much lower; T0-36 L185-L187, L227-L228). |
| New Zealand (`NZ`) | `access_india` | [6.4, 7.4, 8.2] | B | AEWV relaxed, clear SMC/Green List PR (NZ$35/hr verified), plus India-NZ FTA (2026-10-20) adding 5,000 work slots for Indians (T0-36 L317, L366-L367, L621-L622). |
| New Zealand (`NZ`) | `access_non_eu` | [5.8, 6.8, 7.6] | B | Same AEWV and SMC/Green List settlement routes without the India-NZ FTA quota (T0-36 L317, L366-L367). |
| New Zealand (`NZ`) | `remote_reach` | [2.4, 3.3, 4.3] | C | Only 1.5-2.5 h IST overlap and tiny employer pool (T0-36 L332, L382). |
| New Zealand (`NZ`) | `ecosystem` | [3, 3.8, 4.6] | C | Small English-speaking startup ecosystem, no frontier AI lab presence found (T0-36 L353). |
| New Zealand (`NZ`) | `stability` | [7.4, 8.2, 8.9] | B | Very high institutional stability and welcoming skilled-migration reforms in 2026 (T0-36 L366-L367, L621-L622). |
| Taiwan (`TW`) | `demand` | [4.4, 5.2, 6] | C | Strong AI hardware/semiconductor base, smaller English-accessible GenAI software posting volume (T0-36 L113, L350). |
| Taiwan (`TW`) | `pay_ppp` | [5.4, 6.3, 7.2] | M | 70%-74% kept after tax & rent ($30.4k R1 / $46.3k R2) due to low rent ($816/mo) and low tax (T0-36 L219-L220, L287). |
| Taiwan (`TW`) | `net_pay` | [3.8, 4.8, 5.8] | M | Taipei $40.2k net at R1 / $56.1k at R2; 14.6% tax at $100k (schedule D; T0-36 L219-L220, L240). |
| Taiwan (`TW`) | `access_india` | [6.2, 7.1, 7.9] | B | Open 4-in-1 Employment Gold Card (NT$160k/mo verified 2026-11-19, no employer tie) and APRC route (T0-36 L314, L1229). |
| Taiwan (`TW`) | `access_non_eu` | [6.2, 7.1, 7.9] | B | Same open Employment Gold Card route for non-EU nationals (T0-36 L314, L1229). |
| Taiwan (`TW`) | `remote_reach` | [3, 4, 5] | C | 6.5 h IST overlap, but Mandarin-first domestic market limits cross-border remote roles (T0-36 L329, L387). |
| Taiwan (`TW`) | `ecosystem` | [5.2, 6.1, 7] | C | Global AI silicon/supply-chain leader, though no frontier-AI software lab offices found in T0-36 (T0-36 L350). |
| Taiwan (`TW`) | `stability` | [5.4, 6.5, 7.6] | C | Stable domestic visa/tax framework offset by cross-strait geopolitical tail risk (T0-36 L376). |
| Malaysia (`MY`) | `demand` | [3.8, 4.6, 5.4] | C | Growing Southeast Asian data-centre/delivery hub in KL, modest AI engineering posting volume (T0-36 L110). |
| Malaysia (`MY`) | `pay_ppp` | [2.8, 3.8, 4.8] | M | Low KL rent ($688/mo), but $10.7k R1 / $22.3k R2 post-rent disp. trails peer hubs (T0-36 L224-L225, L290). |
| Malaysia (`MY`) | `net_pay` | [2, 3, 4.2] | M | KL $19.0k net at R1 / $30.5k at R2 (far below India BLR Levels.fyi median; T0-36 L204, L224-L225). |
| Malaysia (`MY`) | `access_india` | [4.4, 5.4, 6.4] | B | EP floors raised sharply on 2026-06-01 (Cat I RM 20k/mo verified; Cat II/III require local succession plans; T0-36 L311, L363, L1051-L1053). |
| Malaysia (`MY`) | `access_non_eu` | [4.4, 5.4, 6.4] | B | Same June 2026 EP salary-floor and succession-plan rules for non-EU nationals (T0-36 L311, L363). |
| Malaysia (`MY`) | `remote_reach` | [4.2, 5, 5.9] | C | 6.5 h IST overlap and English at MNCs, low pay reduces pull for India-based remote engineers (T0-36 L328, L383). |
| Malaysia (`MY`) | `ecosystem` | [3.2, 4, 4.8] | C | Growing cloud/data-centre infrastructure, no frontier AI lab offices documented (T0-36 L347). |
| Malaysia (`MY`) | `stability` | [5.4, 6.3, 7.2] | B | Abrupt June 2026 doubling of EP salary minimums increases expatriate-hiring policy risk (T0-36 L363). |
| China (`CN`) | `demand` | [6.6, 7.5, 8.4] | C | 125 aimlroles postings on English boards, plus vast domestic AI labour market largely invisible in Western feeds (T0-36 L117). |
| China (`CN`) | `pay_ppp` | [5.8, 7, 8.2] | M | Beijing R1 disp. $58.6k / R2 $95.8k (using Shanghai 2025 rent proxy; schedule D; T0-36 L229-L230, L296). |
| China (`CN`) | `net_pay` | [5.8, 7, 8.2] | M | Beijing $69.7k net at R1 / $106.9k at R2; 29.3% tax at $100k (schedule D; T0-36 L229-L230, L246). |
| China (`CN`) | `access_india` | [1.8, 2.8, 4] | C | Z visa and new K visa exist, but Mandarin barrier, tight work-permit controls and bilateral friction limit Indian access (T0-36 L91, L318, L373, L387). |
| China (`CN`) | `access_non_eu` | [2.2, 3.2, 4.4] | C | Z/K visa accessible mainly to Mandarin-fluent or niche researchers; tight foreign-hire barriers (T0-36 L91, L318, L373). |
| China (`CN`) | `remote_reach` | [0.5, 1.2, 2] | C | Practically closed to cross-border foreign remote hiring despite 6.5 h IST overlap (T0-36 L33, L91, L329). |
| China (`CN`) | `ecosystem` | [7.4, 8.3, 9] | C | Major domestic frontier-AI labs and massive capital/engineering scale, separated from Western lab ecosystem (T0-36 L91, L117, L354). |
| China (`CN`) | `stability` | [2.6, 3.8, 5] | C | High geopolitical, export-control and regulatory uncertainty for foreign AI engineers (T0-36 L91, L373). |
| Qatar (`QA`) | `demand` | [2, 2.9, 3.9] | C | Tiny measured AI posting volume in Doha alongside high GenAI user adoption (T0-36 L120, L145). |
| Qatar (`QA`) | `pay_ppp` | [4, 5.2, 6.4] | M | 0% PIT yields $34.0k post-rent disp. (63% of gross) on C-grade pay and modelled rent (T0-36 L213, L292). |
| Qatar (`QA`) | `net_pay` | [4.2, 5.6, 7] | M | 0% PIT ($100k gross = $100k net); C-grade Doha pay around $54.1k (T0-36 L168, L213, L236). |
| Qatar (`QA`) | `access_india` | [4.8, 5.8, 6.8] | C | Employer-sponsored residence permit accessible with an offer, no PR path (T0-36 L308). Qatar is NOT a Hague Apostille member (requires MEA + Embassy + MOFA legalisation) (T0-41). |
| Qatar (`QA`) | `access_non_eu` | [4.8, 5.8, 6.8] | C | Same employer-sponsored permit rules for non-EU nationals (T0-36 L308). |
| Qatar (`QA`) | `remote_reach` | [2.4, 3.4, 4.4] | C | 6.5 h IST overlap, but negligible documented remote-from-India AI hiring (T0-36 L327, L384). |
| Qatar (`QA`) | `ecosystem` | [1.8, 2.6, 3.6] | C | No frontier AI labs documented; tiny AI startup/R&D base (T0-36 L346). |
| Qatar (`QA`) | `stability` | [2.4, 3.6, 4.8] | C | IMF projected -8.6% 2026 contraction amid 2026 US-Iran conflict and regional security shock (T0-36 L627-L630, L1144). |
| Bahrain (`BH`) | `demand` | [1.5, 2.3, 3.3] | C | Very thin measured AI posting volume in Manama (T0-36 L120). |
| Bahrain (`BH`) | `pay_ppp` | [2.5, 4.5, 6.5] | D | No pay or rent reference retrieved in T0-36; wide uncertainty around 0% PIT advantage (T0-36 L169, L214, L297). |
| Bahrain (`BH`) | `net_pay` | [3.5, 5, 6.5] | D | 0% PIT + 1% UI ($99k net at $100k gross), but local AI pay unmeasured (T0-36 L169, L214, L237). |
| Bahrain (`BH`) | `access_india` | [4.6, 5.6, 6.6] | B | LMRA employer permit plus 10-yr Golden Residency (5 yrs + BHD 2,000/mo basic verified 2026-11-19; no PR; T0-36 L309, L1226). |
| Bahrain (`BH`) | `access_non_eu` | [4.6, 5.6, 6.6] | B | Same LMRA and Golden Residency rules for non-EU nationals (T0-36 L309, L1226). |
| Bahrain (`BH`) | `remote_reach` | [2, 3, 4] | C | 6.5 h IST overlap, negligible documented remote AI hiring (T0-36 L327, L384). |
| Bahrain (`BH`) | `ecosystem` | [1.4, 2.2, 3.2] | C | No frontier AI labs or major AI clusters documented in T0-36 (T0-36 L346). |
| Bahrain (`BH`) | `stability` | [2.5, 3.7, 4.9] | C | IMF projected -0.5% 2026 growth amid 2026 US-Iran regional conflict (T0-36 L627-L630, L1144). |

## Next steps

- **Relocation pathways and visa execution:** [visa-and-relocation.md](visa-and-relocation.md)
- **Working cross-border remote without relocating:** [remote-cross-border.md](remote-cross-border.md)
- **India remote career playbook and city comparison:** [india-remote-playbook.md](india-remote-playbook.md)
- **India cross-border tax, FEMA, GST and payment rails:** [india-remote-tax.md](../09-compensation/india-remote-tax.md)
- **Role-level compensation benchmarks:** [pay-benchmarks.md](../09-compensation/pay-benchmarks.md)
- **Global GenAI hiring landscape:** [market-overview.md](../01-landscape/market-overview.md)
