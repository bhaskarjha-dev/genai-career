---
id: "T0-37"
title: "Visa and Work-Permit Dossier: United States"
date: "2026-11-13"
status: complete-with-gaps
topic: "visa-dossier-united-states"
tags: ["united-states", "work-visa", "h-1b", "o-1a", "eb-1a", "eb-2-niw", "opt", "india"]
informs_decisions: ["D-007"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and page fetch"
evidence_window: "2024-03-04 to 2026-11-11"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 7
---

# T0-37: Visa and Work-Permit Dossier: United States

S-numbers (S1, S2 and so on) point to rows in the Sources & Evidence Ledger. Grades follow EGP-1.0: A is a primary source I opened. B is a secondary source, or a primary page seen only as a search snippet. C is vendor or other third-party analysis, attributed, with conflicts of interest marked. D is recalled and unverified. M is my own arithmetic, which inherits the weakest input. The brief fixed the research date at 2026-11-11. Searches and page fetches ran on 2026-11-13, and each fact carries its own "as of" date. Pages on uscis.gov (HTML) and travel.state.gov refused automated access (bot detection), so figures that originate there come from snippets or summaries and are capped at B. This is a pointer to official sources, not legal advice.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | H-1B cap petitions are chosen by a purely random lottery, and a $100,000 payment applies to new petitions. | 0.6 | D |
| P2 | O-1A has no degree prerequisite, and USCIS approves about 94% of O petitions. | 0.7 | D |
| P3 | India's EB-2 backlog exceeds a decade; EB-1 India is under four years. | 0.7 | D |
| P4 | OPT (12 months) plus STEM OPT (24 months) is stable. | 0.6 | D |
| P5 | USCIS publishes O-1A approval rates separately from O-1B. | 0.3 | D |
| P6 | The "Gold Card" is a new statutory visa category. | 0.2 | D |

## Research Question

**Decision question.** Which legal routes let a foreign GenAI professional work in the United States as of 2026-11-13, what does each require, cost and take, how likely is an employer to use it for an AI role, and what leads to permanent residence?

**Sub-questions.**
1. Route census.
2. Employer reality.
3. Indian-national specifics.
4. Remote work while resident.
5. Status of pending and contested rules.
6. A comparison and reader recommendations.
7. The seven knowledge-base claims (K1–K7).

**Scope as applied.**
- United States only.
- I read "GenAI professional" as ML or software engineers, researchers and technical leaders.
- Indian nationals get the specific lens; E-3, TN and H-1B1 appear as the generic non-EU lens.
- Founder and remote-work routes are covered briefly.
- Where a source says "October 2026 Visa Bulletin" (K4), I also report the November 2026 bulletin, which is the one in force.
- USCIS reports the O classification as one line, so "O-1A approval" means the combined O line.

**Method.**
- About 40 searches (standard and extended) and 15 page-fetch attempts (9 opened, 6 blocked or refused), run in two passes. The second pass closed gaps flagged after the first: coverage of the $100,000 payment, founder routes, spouse work rights, the visa integrity fee, naturalisation and weighted-selection litigation.
- Opened (Read): the Federal Register NPRM on the $103,265 fee (S1), DOL FLAG processing times (S6), USCIS policy alert PA-2026-05 (S5), two USCIS Administrative Appeals Office (AAO) decisions (S7, S8), and a university tracker (S24). I also read three secondary pages in full: the Herman Legal Group explainer (S22), the SMA O-1 analysis (S30) and the F1Jobs rates article (S32).
- Blocked: uscis.gov HTML, travel.state.gov.
- Falsification searches:
  - Is the $100,000 payment collected? No, per two court orders.
  - Is O-1 approval about 94%? Stale; the figure is 91.0%.
  - Is vendor "99% NIW approval" comparable to USCIS data? No (see KF13).
  - Is India in the immigrant-visa pause or the travel ban? No.
  - Do all H-1B applicants need a police certificate (vendor claim)? Uncorroborated.
  - Does the $100,000 payment exempt cap-exempt employers? No (KF2).
  - Is the visa integrity fee being collected? Sources conflict (7.3).
- I drew no samples of my own.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | H-1B cap selection has been wage-weighted since 2026-02-27, with 4/3/2/1 entries for OEWS Levels IV/III/II/I. DHS estimated selection chances of 15.29% (Level I), 30.58% (II), 45.87% (III) and 61.16% (IV), against about 29.59% under the old random lottery. FY2027 registration ran 2026-03-04 to 2026-03-19 and petition filing ran 2026-04-01 to 2026-06-30. The cap was reached and there was no second round. Registrations were reported at 211,600, down 38.5% from 343,981 in FY2026 (M). One firm's own sample (n not stated, COI) shows selection of 24.5% at Level I and 69.2% at Level III. Selected beneficiaries with US advanced degrees rose to 71.5% from 57%. A law firm reports a D.D.C. suit against the rule (date and status not established). FY2028 dates were unpublished as of 2026-11-13. | [S1] [S26] [S27] [S28] [S29] [S56] [S71] [S72] | B |
| KF2 | The $100,000 payment (Proclamation 10973, effective 2025-09-21) was extended by Proclamation 11069 to 2027-09-21 [S1,S4]. USCIS guidance of 2025-10-20 applied it to new petitions, cap-subject and cap-exempt alike, for beneficiaries outside the US without a valid H-1B visa. It did not apply to granted changes of status, extensions or amendments inside the US [S61,S62]. As of 2026-11-11 USCIS is not collecting it, because the implementing agency policies were vacated by D. Mass. (2026-06-08) and blocked by N.D. Cal. (2026-09-30, covering the extension). D.D.C. upheld the payment on 2025-12-23, so the courts are split, with appeals pending in three circuits. The proclamation itself has not been struck down [S19–S23]. | [S1] [S4] [S19] [S20] [S21] [S22] [S23] [S61] [S62] | B |
| KF3 | DHS proposed on 2026-08-25 a $103,265 fee on every cap-subject H-1B petition, including the master's cap, payable at filing and additional to all other fees, including any proclamation payment. It excludes cap-exempt petitions. Comments closed 2026-09-24, and no final rule was found as of 2026-11-13. | [S1] | A |
| KF4 | Four further changes are proposed. Grace-period elimination (91 FR 57807, comments closed 2026-11-10). Removal of deference to prior approvals on extensions (comments due 2026-11-13). The DOL wage-level rise to the 34th/52nd/70th/88th percentiles (comments closed 2026-05-26). A school-paid OPT fee (comments closed 2026-11-09). In force: PA-2026-05 (denial without RFE, since 2026-08-05), the extension of the 9-11 biometric fee to all H-1B/L-1 extensions, and the adjustment-of-status discretion memo PM-602-0199 (since 2026-05-21). | [S1] [S2] [S3] [S5] [S9] [S10] [S22] [S46] | B |
| KF5 | O-1A has no degree, PhD or citation prerequisite: a major award or three of eight criteria, then a totality ("very top of the field") judgement. USCIS reports one O line. It shows 91.0% approved and a 24.2% RFE rate for FY2026 Q1–Q3 (23,417 decisions), against 93.9% approved in FY2025. A law firm reports that officers write out the second step in their decisions and that PA-2026-05 allows denial without an RFE. | [S5] [S8] [S30] [S31] [S32] | B |
| KF6 | The green-card analogues diverged from the O line. EB-1A approvals fell from 66.9% in FY2025 to 32.2% in FY2026 Q3. NIW approvals fell to a 35.7% trough in FY2025 Q4 and rose to 55.3% in FY2026 Q3. Standard I-140 times run 23.5 months (EB-1A, 2026-04) and 24–30 months (NIW). NIW filings nearly tripled between FY2022 and FY2025 and make up 46.9% of pending I-140s. All figures come from vendor and think-tank readings of USCIS data. | [S31] [S33] [S59] | C |
| KF7 | India's queue in the November 2026 Visa Bulletin (released 2026-10-22): EB-1 final action 2023-02-01, EB-2 2013-11-01, EB-3 2014-01-22. These lag the calendar by about 3.8, 13.0 and 12.8 years (M). USCIS directed employment-based I-485 filers to the Dates for Filing chart for November. India EB-2 was "unavailable" in July–September 2026. Approved EB-2 India petitions awaiting numbers: 356,360 (FY2026 Q3). | [S14] [S15] [S16] [S17] [S18] | B |
| KF8 | L-1A and L-1B were approved 91.2% and 91.3% (FY2026 Q1–Q3), with RFE rates of 25.9% and 29.4%. They require one continuous year abroad with a related entity in the prior three years. Maximum stays are 7 and 5 years. Covered employers owe a $4,500 fee, which since 2026-09-09 includes extensions (the rule expires 2027-09-30). L-2 and E spouses are work-authorised incident to status when their I-94 carries the spousal annotation; H-4 spouses are not. | [S1] [S32] [S66] | B |
| KF9 | OPT (12 months) and the STEM extension (24 months) remain in force. DHS proposed on 2026-10-08 that schools pay $70,000 for a first OPT recommendation and $30,000 for each later one, effective 60 days after a final rule. The D/S final rule (91 FR 44976) was postponed by D. Mass. on 2026-09-14. | [S3] [S22] [S49] | B |
| KF10 | FY2025: 406,348 H-1B approvals, 69.9% India-born, 62% in computer occupations, median pay $133,000 (initial approvals about $103,000). Amazon led initial approvals (4,644). The top seven India-based IT firms received 4,573 initial approvals, down 37% year on year. PERM analyst review averaged 300–360 days (DOL, 2026-10-31). 57.6% of FY2024 PERM filings were for workers already in H-1B status. | [S1] [S6] [S9] [S34] [S35] | B |
| KF11 | Since 2025-12-15 H-1B and H-4 applicants face an online-presence review, and interviews in India were mass-rescheduled. DoS wait times for H/L/O/P/Q on 2026-10-21 were: Kolkata 1 month, Mumbai 2, Chennai 2.5, New Delhi 3.5, Hyderabad 6.5. India is not in the 75-country immigrant-visa pause, which a court set aside in August 2026. | [S36] [S37] [S38] [S39] [S40] | B |
| KF12 | The Gold Card is operated under an executive order, not a statute. It uses Form I-140G within EB-1/EB-2 NIW, at a $1,000,000 gift ($2,000,000 corporate) plus a $15,000 fee. As of 2026-04-28 USCIS had 338 requests, 165 paid fees and 59 petitions. One approval was reported. AAUP v. DHS is pending. Indian applicants join the same per-country queue. | [S43] [S44] [S45] | B |
| KF13 | Vendor approval claims are self-reported and cohort-selected. WeGreened shows 98% overall, 99% NIW and 91% EB-1A under its refund policy, while USCIS-wide NIW and EB-1A rates are far lower. Beyond Border's comparison page itself says "98%, self-reported, denominator not disclosed". No independent audit was found. | [S31] [S41] [S42] [S60] | C |
| KF14 | No US job-seeker, points-based or digital-nomad visa was found. Schedule A lists only nurses, physical therapists and exceptional-ability workers, with no AI/ML occupation, and the 2023 STEM request for information produced no change in sources read. Founder routes exist but are narrow: the International Entrepreneur Rule is parole, not a visa, and EB-5 starts at $800,000 (see 7.7). | [S50] [S63] [S64] [S65] | B |

## Recommendation

Treat every row in the status table (Detailed Findings 7.2) as V0. Re-verify on the Federal Register, regulations.gov, court dockets, USCIS and State pages within 14 days of acting (D-007).

| Reader or situation | Decision rule | Failure mode | Re-check trigger |
|---|---|---|---|
| Mid-level engineer with an offer from a multinational with an affiliate abroad | If you worked at least one continuous year for the affiliate in the last three years, ask for L-1A or L-1B. There is no lottery and no $100,000 payment. | RFE rates of 25.9–29.4% and denial without RFE under PA-2026-05. "Specialised knowledge" is a judgement call. A $4,500 fee falls on covered employers. | PA-2026-05 ruling; USCIS FY2026 Q4 data |
| Mid-level engineer with a US employer offer | Ask the employer to register in the March 2027 cap round at the wage level the salary supports, and to state in writing who pays any fee that is finalised. | Non-selection (FY2027 had no second round). The $103,265 proposal, if finalised, falls on the employer. The employer may drop the role. | Final rule on $103,265; FY2028 registration notice |
| Offer from a university or non-profit research organisation | Prefer cap-exempt H-1B, which is outside the lottery and the $103,265 proposal. | Small employer pool. The $100,000 payment covers cap-exempt petitions for workers outside the US, if the court orders lift. | Court orders; USCIS guidance |
| Senior engineer or researcher, no offer, strong evidence | Pursue O-1A through a US employer or US agent. Consider NIW or EB-1A only with evidence that clears the "very top" test. | Final-merits denial. EB-1A approvals were 32.2% in FY2026 Q3. A thin filing may be denied with no RFE. Indian nationals then wait in a 13-year EB-2 queue (M). | USCIS Q4 data; PA-2026-05 ruling |
| Senior engineer or researcher, no offer, thinner evidence | Target cap-exempt employers or employers that file high wage-level H-1B cases (Level III–IV). Build O-1A evidence in parallel. | Lottery and time. Evidence-building may not change the outcome. | None specific |
| New graduate on F-1 in the US | Use OPT then STEM OPT (up to 36 months). Seek employers that offer Level II–IV wages, and consider the master's cap. Ask your designated school official (DSO) about the OPT fee NPRM. | OPT fee final rule. D/S rule revival. Level I entry has the lowest selection odds. | OPT fee final rule; D. Mass. D/S case |
| New graduate abroad | There is no direct work route. L-1 needs a prior year abroad with a multinational. An F-1 route costs tuition and passes through consular vetting. | Consular delays; the US may not fit. | DoS wait-time tool |
| Indian national planning permanent residence | Plan on six years of H-1B plus AC21 extensions. Start PERM early, and compare EB-3 with EB-2 each month (EB-3 India is ahead). Check how a three-year bachelor's is evaluated. | Retrogression or "unavailable" months; three-year degree rejected for EB-2. | Visa Bulletin each month |
| Anyone offered a vendor refund offer or "98% approval" | Treat as marketing. Ask for the denominator, the period and the cohort rule. | Paying for a claim that does not transfer to your case. | None |

**What would change these rules.**
- Appellate rulings on the $100,000 payment.
- A final rule on the $103,265 fee, the OPT fee, grace-period removal, deference removal or DOL wage levels.
- First post-PA-2026-05 USCIS data.
- Visa Bulletin movement in December 2026 and January 2027.
- A ruling in AAUP v. DHS or in the weighted-selection suit.

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| H-1B cap-subject | Preferred baseline | Largest employer use (62% of FY2025 approvals in computer occupations). Wage weighting rewards pay. Exposed to fee rules. |
| H-1B cap-exempt | Preferred where it fits | No lottery; outside the $103,265 proposal. Narrow employer pool, and the $100,000 payment reaches it for workers abroad if the court orders lift. |
| O-1A | Preferred for strong profiles | No cap or lottery. Approval is 91.0% for filed O cases, but the "very top" test is enforced more tightly. |
| L-1A/L-1B | Preferred for multinational staff | No lottery; one-year-abroad gate and high RFE rates. |
| EB-1A | Rejected as a default | Approval 32.2% in FY2026 Q3; India EB-1 queue about 3.8 years behind (M). |
| EB-2 NIW | Conditional | Approval 55.3% in FY2026 Q3, but 24–30 months standard; India EB-2 about 13 years behind (M). |
| PERM EB-2/EB-3 | Preferred settlement path via employer | Official DOL timings; India queue. |
| OPT/STEM OPT | Preferred for graduates | Up to 36 months of work; fee NPRM and D/S risk. |
| Gold Card | Rejected | $1,000,000 gift; executive order only; litigation; same India queue. |
| EB-5 | Rejected for most readers | $800,000 to $1,050,000 plus job creation; proposed rule adds a $1,400,000 tier. |
| International Entrepreneur Rule | Niche | Parole, not a visa; needs funding or grant thresholds; vendor-sourced. |
| E-3, H-1B1, TN | Not available to Indians | Nationality-specific (Australia; Chile and Singapore; Canada and Mexico). |
| Vendor-guided "easy route" | Rejected as a decision basis | Claims are self-reported (KF13). |

## Detailed Findings

### 7.1 Route table (United States)

| Route | Kind | Eligibility | Salary threshold and date | Processing | Fees | Dependants | Path to permanent residence | Source | Grade |
|---|---|---|---|---|---|---|---|---|---|
| H-1B cap-subject | employer-sponsored | US employer petition plus LCA; bachelor's or higher in the specialty (or equivalent); registration and weighted selection; 65,000 + 20,000 (US master's) per FY | No fixed amount; employer pays at least the prevailing or actual wage by SOC and area (as of 2026-11-13). DOL NPRM would lift levels to the 34th/52nd/70th/88th percentile. | FY2027: registration 2026-03-04 to -19; filing from 2026-04-01; start 2026-10-01. Premium service standard 15 business days. | $215 registration; $780/$460 I-129; $1,500/$750 ACWIA; $500 fraud; $600/$300/$0 Asylum Program Fee. Total $3,595 (large) or $2,225 (small), M, before premium $2,965 and the $4,000 PL 114-113 fee where it applies. $100,000 blocked; $103,265 proposed. | H-4; H-4 EAD only with an approved I-140 or an AC21 extension | Employer PERM to EB-2/EB-3; six-year limit with AC21 exceptions | S1 S22 S26 S52 S53 S55 | B |
| H-1B cap-exempt | employer-sponsored | University or affiliated non-profit; non-profit or government research organisation; workers already counted under the cap who change jobs or extend within six years | As above | No registration; same premium | As above; the $103,265 proposal excludes cap-exempt petitions; the $100,000 payment covers cap-exempt petitions for workers abroad (blocked as of 2026-11-11) | As above | As above | S1 S61 S62 | A |
| O-1A | talent | Major award or at least 3 of 8 criteria, then a totality judgement; petition by a US employer or US agent; no degree prerequisite | None (high pay is one criterion) | Standard 14.5 months for 80% of O petitions (tool read 2026-11-01); premium 15 business days | I-129 $1,055/$530 + asylum $600/$300 + premium $2,965 = $4,620 (M, large employer) | O-3 (no work; D) | EB-1A, NIW or PERM | S5 S8 S30 S32 S58 | B |
| L-1A / L-1B | intra-company | Employee of a qualifying foreign affiliate with one continuous year abroad in the prior three; L-1A manager or executive (7-year maximum), L-1B specialised knowledge (5-year maximum); new-office L-1A starts at one year | None | Standard 6.5 months (tool read 2026-11-01); premium 15 business days | I-129 $1,385/$695 + fraud $500 + asylum $600/$300; premium $2,965; PL 114-113 $4,500 for covered employers | L-2; spouse works incident to status with an annotated I-94 | EB-1C or PERM | S1 S32 S52 S58 S66 | B |
| EB-1A | talent | Major award or at least 3 of 10 criteria, then a final-merits test ("very top of the field"); no offer or PERM | None | Standard 23.5 months (2026-04); premium 15 business days | I-140 $715 + $300 (self-petitioner) + premium $2,965 | Derivative spouse and children | Direct; India final action 2023-02-01 | S7 S31 S57 S14 | B |
| EB-2 NIW | self-sponsored | Advanced degree or exceptional ability, plus the three Dhanasar prongs; no PERM | None | Standard 24–30 months; premium 45 business days | As EB-1A | Derivatives | Direct; India final action 2013-11-01 | S31 S59 S12 | B |
| EB-2/EB-3 via PERM | employer-sponsored | DOL prevailing-wage determination, recruitment test, then I-140 | DOL level by SOC and area | PWD queue on 2026-10-31: H-1B July 2026 receipts. PERM analyst review 300–360 days. End to end 16–20 months (vendor). | I-140 $715 + asylum $600; recruitment adverts (cost not verified) | Derivatives | India final action: EB-2 2013-11-01; EB-3 2014-01-22 | S6 S14 S54 S57 | B |
| F-1 OPT / STEM OPT | graduate | F-1 student; 12 months post-completion OPT; 24-month STEM extension | None | Premium I-765: 30 business days | I-765 premium $1,780 (B). Proposed school fee $70,000/$30,000 (not in force). | F-2 (no work; D) | None directly (H-1B or other) | S3 S12 S22 | B |
| E-3 / H-1B1 / TN | employer-sponsored | Australia (E-3); Chile and Singapore (H-1B1); Canada and Mexico (TN). Indians are ineligible. | LCA-based for E-3 and H-1B1 | TN: USCIS-filed 4.5 months | E and TN consular fee tiers not itemised here | E spouses work incident to status with an annotated I-94 | None direct | S1 S32 S66 | B |
| Gold Card (I-140G) | talent | $1,000,000 gift ($2,000,000 corporate), lawful funds, vetting; goes through EB-1A or EB-2 NIW | — | Not faster per DHS filing | $15,000 fee plus the gift | — | Same EB queue and caps | S43 S44 S45 | B |
| International Entrepreneur Rule | founder | Parole (not a visa) for founders of funded start-ups; Form I-941; thresholds of $311,071 in qualified investment or $124,429 in government grants (vendor); ownership floors recalled, not verified | — | Not retrieved | I-941 $1,200 (vendor) | Not verified | None direct; needs O-1A, EB-1A, NIW, EB-5 or PERM | S63 S67 | C |
| EB-5 investor | self-sponsored | $1,050,000 standard or $800,000 in a targeted employment area or infrastructure project; job creation required (10 full-time jobs, recalled); proposed rule adds $1,400,000 for high-employment areas | — | Not retrieved | USCIS fees not itemised | Derivatives | Direct; regional centre authority runs to 2027-09-30 | S64 S65 S76 | B |

Not in the table: job-seeker, points-based, digital-nomad or bilateral Indian routes (none found). See Absences.

### 7.2 Status table (every pending, contested or changed rule since 2025-01-01)

| Item | Status | As of | Official source | Grade |
|---|---|---|---|---|
| Proclamation 10973 $100,000 payment | Litigated; not collected | 2026-11-11 | 90 FR 46027 (cited in S1) | B |
| Proclamation 11069 extension to 2027-09-21 | In force on paper; implementing policies blocked | 2026-11-11 | 91 FR 60497 | B |
| California v. Mullin (D. Mass. 25-13829) | Vacatur 2026-06-08; 1st Cir. 26-1699, stay denied 2026-07-24 | 2026-11-11 | S1; S20 | B |
| Global Nurse Force v. Trump (N.D. Cal.) | Relief 2026-09-30 covers the extension; 9th Cir. appeal filed 2026-10-09; relief type described inconsistently | 2026-11-11 | S21; S22 | B |
| Chamber of Commerce v. DHS (D.D.C.) | Upheld 2025-12-23; D.C. Cir. argued 2026-03-09, undecided | 2026-11-11 | S22 | B |
| $103,265 H-1B fee NPRM (91 FR 54817) | Proposed; comments closed 2026-09-24; no final rule found | 2026-11-13 | S1 | A |
| Weighted selection final rule (90 FR 60864) | In force from 2026-02-27 | 2026-11-13 | S1 | A |
| Suit against the weighted selection rule (D.D.C.) | Reported by a law firm; filing date and status not established | 2026-11-13 | S72 | C |
| DOL prevailing-wage NPRM (91 FR 15454) | Proposed; comments closed 2026-05-26; no final rule found | 2026-11-13 | S9; S10 | B |
| Grace-period elimination NPRM (91 FR 57807) | Proposed; comments closed 2026-11-10; 8 CFR 214.1(l)(2) still applies | 2026-11-13 | S2; S25 | B |
| Removal of deference (docket USCIS-2026-0529) | Proposed; comments due 2026-11-13 | 2026-11-11 | S22; S32 | B |
| PA-2026-05 evidence/RFE policy | In force from 2026-08-05; challenged (AAUP v. Mullin, no ruling reported) | 2026-11-01 | S5 (policy); S32 (challenge, C) | A |
| PM-602-0199 adjustment-of-status memo | In force from 2026-05-21; DHS said most applicants may still adjust | 2026-11-13 | S46 | B |
| Executive Order on H-1B program integrity | In force 2026-09-18; implementing guidance not seen | 2026-09-22 | S24 | B |
| 9-11 fee rule (91 FR 51360) | In force; extends the fee to all H-1B/L-1 extensions for covered employers; statutory fee ends 2027-09-30 | 2026-11-13 | S1 | A |
| Premium processing fee rule (FR 2026-00321) | In force from 2026-03-01 ($2,965) | 2026-11-13 | S11; S12 | B |
| Premium-processing timeframe amendment (RIN 1615-AD25) | Under OIRA review since 2026-10-13; text unpublished | 2026-11-01 | S59 | C |
| OPT Fees NPRM (91 FR 64566) | Proposed; comments closed 2026-11-09 | 2026-11-13 | S3; S22 | B |
| D/S final rule (91 FR 44976) | Final; effective date postponed 2026-09-14 | 2026-11-13 | S49 | B |
| EAD automatic-extension removal (90 FR 48799) | In force for renewals filed on or after 2025-10-30; challenged in C.D. Cal. (filed 2026-01-08) | 2026-11-13 | S48; S74 | C |
| Online-presence review for H-1B/H-4; expanded vetting | In force from 2025-12-15; expanded screening effective 2026-10-01 | 2026-11-13 | S24; S37 | B |
| Interview-waiver narrowing | In force from 2025-09-02 | 2026-11-13 | S24 | B |
| Visa integrity fee ($250 per visa issuance, P.L. 119-21) | Collection status contested: one source says collected since 2025-10-01, another said not collected as of 2026-06-15 | 2026-11-13 | S68; S69; S75 | C |
| Visa Bulletin November 2026 | In force; Dates for Filing chart for I-485; December bulletin not found | 2026-11-13 | S13–S18 | B |
| 75-country immigrant-visa pause | Set aside by a court in August 2026; India never listed | 2026-11-13 | S39; S40 | B |
| Gold Card (EO 14351; Form I-140G) | Operating by executive order; AAUP v. DHS pending | 2026-11-13 | S43; S44 | B |
| EB-5 proposed rule (published 2026-07-02) | Proposed; comments closed 2026-08-31; RIA grandfathering deadline 2026-09-30 passed; inflation adjustment due 2027-01-01 | 2026-11-13 | S64; S65; S76 | B |
| International Entrepreneur Rule | Operating per vendor pages; no rescission found in sources read | 2026-09 | S63; S67 | C |
| H-4 EAD rule | Stands (certiorari denied 2025-10-14) | 2025-10-14 | S47 | B |
| L-2 and E spouse work incident to status | In force (policy of 2021-11); needs an annotated I-94 | 2026-11-13 | S66 | B |
| Naturalisation 2025 civics test | In force for N-400 filed on or after 2025-10-20 | 2025-10-03 | S73 | B |
| Schedule A | Unchanged | 2025-10-08 | S50 | B |
| H.R. 1 fee IFR (91 FR 22952), naturalisation fee NPRM (91 FR 37500), biometrics NPRM (90 FR 49062), EB-5 fee NPRM (90 FR 48516) | Existence only; contents not read | 2026-08-25 | S1 | A |

### 7.3 H-1B in full

- **Cap and selection.** The cap is 65,000 plus 20,000 for US master's or higher degrees. Registration is per beneficiary ($215). The weighted rule (published 2025-12-29, effective 2026-02-27) gives four entries at Level IV, three at III, two at II and one at I. DHS estimated selection chances of 15.29%, 30.58%, 45.87% and 61.16%, against about 29.59% for the old random lottery [S71]. A law firm reports a D.D.C. suit against the rule [S72].
- **FY2027 outcome.** The cap was reached. USCIS said no second round. The share of selected registrations at Level I was 17.7% [S29].
- **$100,000 payment.** See KF2. USCIS guidance of 2025-10-20 applied it to new petitions for beneficiaries outside the US without a valid H-1B visa, cap-exempt and cap-subject alike. It did not apply to granted changes of status, extensions or amendments inside the US, or to workers holding a valid H-1B visa [S61, S62]. Sources disagree on whether H-1B1 is covered, so I do not state it.
- **Cap-exempt employers.** Universities, affiliated non-profits, and non-profit or government research organisations are exempt from the cap. Workers already counted under the cap are exempt when changing jobs or extending within six years (S1, fn 23).
- **Costs.** See 7.1. Mandatory government fees for a large employer total $3,595 (M). Adding the proposed $103,265 would make $106,860 (M), before premium processing, attorney fees and any PL 114-113 fee.
- **Consular costs.** The MRV fee for H, L, O, P, Q and R visas is $205. Sources disagree on when that figure began (Alma says the 2023-06-17 schedule stood as of 2026-06; F1Jobs reports a rise from $190 on 2026-05-30), so I give it as $205 with that conflict [S69, S70]. A $250 visa integrity fee was enacted by P.L. 119-21 (signed 2025-07-04). It is charged per visa issuance, including dependants, and not on a change of status inside the US [S68]. Whether it is being collected is contested: F1Jobs states it has been collected since 2025-10-01, while another vendor page said it was not collected as of 2026-06-15 [S69, S75]. Verify at the consulate.
- **Timelines.** Registration in March, filing from 1 April, start on 1 October. Premium service standard 15 business days, restarting after an RFE response. Consular stamping for workers abroad adds appointment and administrative-processing time (7.9).
- **Portability.** A worker may change employer without re-entering the lottery (S1, fn 23). The 60-day grace period remains in force as of 2026-11-13, and the NPRM would remove it. Starting work on filing a transfer is recalled only (D).
- **H-4 EAD.** Spouses qualify only if the H-1B worker has an approved I-140 or an AC21 extension (S55, S74). Certiorari was denied on 2025-10-14 (S47). Renewals filed on or after 2025-10-30 get no automatic extension (S48).
- **Employer obligations.** A certified LCA with at least the prevailing wage is required (S1). Fees and any proclamation or biometric-fee exposure are in 7.1 and 7.2.
- **Language and degree.** No language test applies to the work routes I read (not verified; D). H-1B accepts a degree-plus-experience equivalence, while EB-2 needs a single-source four-year degree or a bachelor's plus five years [S51].

### 7.4 O-1A, EB-1A and NIW for AI researchers and engineers

- **O-1A.** The classification rests on INA 101(a)(15)(O)(i). Meeting the evidentiary criteria does not alone establish eligibility; officers weigh the totality (S8, 59 FR 41818, 41820). A petition must come from a US employer, a US agent, or a foreign employer through a US agent (S8, 8 CFR 214.2(o)(2)(i)). The eight O-1A criteria and the "small percentage" standard are described in S30.
- **EB-1A.** A major award or three of ten criteria, then a final-merits determination (S7).
- **NIW.** Governed by Matter of Dhanasar's three prongs (S59).
- **O approval and RFE.** FY2026 Q1–Q3: 23,417 decided, 91.0% approved, 24.2% with an RFE, 66.8% approved after an RFE, and 1,885 of 2,096 denials followed an RFE (S32).
- **Why O is not "easy".** O petitions are filed after attorney screening. The O line mixes O-1A, O-1B, O-2 and extensions. The final-merits test is enforced more tightly (S30).
- **Litigation reported by a law firm (S30).** Mukherji v. Miller (D. Neb., 2026-01-28) held the final-merits step unlawful. USCIS withdrew its appeal on 2026-06-10. The AAO rejected a Mukherji-based challenge on 2026-06-16.
- **AI-specific claims.** I found no USCIS data splitting NIW or EB-1A by field. A vendor claim of about 90% NIW approval for AI researchers against 61% overall (S60) is graded E.

### 7.5 L-1

L-1A and L-1B approval and RFE rates are in KF8 and 7.1. Blanket L petitions are on a separate USCIS tab and are not in those rows (S32). The one-year-abroad rule means a person who came to the US as a student and has only OPT employment rarely qualifies (S32). L-2 spouses work incident to status when the I-94 carries the "L-2S" annotation; a spouse whose I-94 lacks it relies on an EAD instead (S66).

### 7.6 Student routes

OPT is up to 12 months, with a 24-month STEM extension (S22). Premium I-765 costs $1,780 and has a 30-business-day service standard (S12). DHS estimated about 194,000 OPT and 95,000 STEM OPT participants in 2024 (S22). Under the OPT fee NPRM, the fee would apply to recommendations made on or after the effective date, and students already approved or recommended would not be charged, according to a law-firm reading of an AIP review (S22). Cap-gap regulations exist (S1, fn 31); I did not verify their details.

### 7.7 Gold Card, founders, job-seeker and points routes

- **Gold Card.** See KF12.
- **International Entrepreneur Rule.** It grants parole (not a visa) for 30 months, with a possible 30-month re-parole. The terms, the funding thresholds and the filing fee come from vendor and law-firm pages [S63, S67], so I grade them C. The ownership floors (10% initial, 5% on re-parole) and the limit of work authorisation to the start-up are recalled and unverified (D).
- **EB-5.** The statutory amounts are $1,050,000 and $800,000. DHS's proposed rule (published 2026-07-02, comments closed 2026-08-31) would add a $1,400,000 tier for high-employment areas and adjust amounts for inflation from 2027-01-01. The regional centre programme is authorised to 2027-09-30 [S64, S65, S76].
- **Job-seeker and points-based routes.** None found.

### 7.8 Employer reality

- **Volume.** FY2025: 406,348 H-1B approvals; 283,772 India-born; 252,088 in computer occupations (S35). Median pay was $133,000, with initial approvals about $103,000 and continuing about $141,000 (S35; the $133,000 is also cited in S1).
- **Who files.** Amazon, Meta, Microsoft and Google were the top four initial-approval employers (S34). 28,277 employers had at least one new approval, and 61% had one petition (S34, via a press summary).
- **Approval rates.** H-1B FY2026 Q1–Q3 was 97.0% (n=278,650, RFE 8.5%) (S32).
- **GenAI sponsorship.** No official statistic splits approvals by GenAI role (Absences).
- **Cost and effort.** Employer fees are in 7.1. PERM timing is in 7.1 (DOL page, S6). 57.6% of FY2024 PERM filings were for workers already in H-1B status (S9).

### 7.9 Indian nationals

- **Backlogs.** EB-1/EB-2/EB-3 India final action dates: 2023-02-01, 2013-11-01, 2014-01-22 (November 2026). Dates for Filing: 2024-07-01, 2015-01-15, 2015-01-15. EB-3 is ahead of EB-2. USCIS counted 356,360 approved EB-2 India petitions and 106,214 EB-3 India petitions awaiting numbers (FY2026 Q3, S18).
- **Consular waits.** DoS tool, 2026-10-21, next available (an estimate, not a promised wait): see KF11 and the measure records. F/M/J waits were 1 to 4 months (S36). An interview is expected for nearly every first-time applicant (S38).
- **Vetting.** Since 2025-12-15, public social-media settings are required for H-1B/H-4 (S37). Appointments were pushed from December 2025 into 2026 and later (S37).
- **Degrees.** H-1B allows a degree-plus-experience equivalence. EB-2 requires a single-source four-year degree or a bachelor's plus five years. USCIS relies on EDGE, which rates a three-year Indian bachelor's as two to three years of US study (S51).
- **No bilateral scheme** was found.
- **Not listed.** India is not in the 75-country immigrant-visa pause (S39) or in the sources I read on the travel ban (S40).
- **Document attestation and police certificates.** An official requirement was not verified (Absences).
- **Citizenship.** After a green card, naturalisation generally needs five years as a permanent resident (three if married to a US citizen), plus English and civics tests. N-400 filings on or after 2025-10-20 take the 2025 civics test [S73]. The naturalisation fee NPRM is 91 FR 37500 (S1).

### 7.10 Remote work while resident

- No US digital-nomad or remote-work visa was found.
- H-1B work is authorised for the petitioning employer. The petition must come from a US employer (S1, fn 22). Reading this as a bar on working for a foreign employer is my inference (D).
- O-1 can be petitioned by a foreign employer through a US agent (S8). Contractor work outside the petition is not authorised (D).
- L-1 covers the qualifying related entity only (D).
- Tax-residence pointer: the IRS substantial-presence and green-card tests (IRS Publication 519, not opened; D).

### 7.11 Comparison and reader recommendations

| Route | Eligibility | Time to start | Government cost (large employer, M) | Employer dependence | Settlement path |
|---|---|---|---|---|---|
| H-1B | Specialty degree; lottery | Next registration March 2027; start 2027-10-01 | $3,595 + premium $2,965; risks $103,265 | High | PERM or EB-1; India queue |
| O-1A | "Very top" evidence | Evidence preparation plus 15 business days (premium); consular wait if abroad | $4,620 | Medium (agent possible) | EB-1A, NIW, PERM |
| L-1 | One year abroad with an affiliate | 15 business days (premium); consular wait if abroad | $5,450 | High | EB-1C or PERM |

One-line recommendations:
- **Mid-level engineer with an offer:** L-1 if an affiliate exists, otherwise ask the employer to register for H-1B.
- **Senior engineer or researcher without an offer:** O-1A if the evidence is strong, otherwise target cap-exempt or high-wage H-1B employers.
- **New graduate:** OPT then STEM OPT, then H-1B at the highest honest wage level.

### 7.12 Vendor claims (K6, K7) and falsification

- WeGreened's own page shows 98% across 52,753 cases (2012-01 to 2025-12) under its refund policy: NIW 99% (42,047), EB-1A 91% (9,218), EB-1B 98% (1,488), and a 92% "refiling" cohort of 10,240 (S41). The same page states that USCIS EB-1A approval is about 60–70% and NIW about 50% generally.
- USCIS-wide EB-1A was 66.9% in FY2025 and 32.2% in FY2026 Q3 (S31). The firm's cohort is eligibility-screened.
- Beyond Border's comparison page says its 98% is self-reported with no disclosed denominator, and that it is not a law firm (S42).
- Beyond Border's cost table adds $100,000 to the H-1B total although the payment is not collected (S58).
- A vendor guide says every H-1B consular applicant needs a police certificate. I found no official corroboration (grade E).
- I relied on vendor-hosted digests of USCIS data in places (S28, S31, S32, S42, S56–S60, S63, S67, S69–S70). These are marked C or COI.
- K7: Federal Register, DOL and AAO pages opened without difficulty. uscis.gov HTML and travel.state.gov refused automated access.

### 7.13 Expert objections and evidence

1. *"USCIS rates are for filed cases."* True. The O line mixes O-1A, O-1B, O-2 and extensions, and EB figures are vendor readings (S32, S33).
2. *"The $100,000 payment was struck down."* Agency policies were vacated or blocked, not the proclamation. D.D.C. upheld it. Three appeals are pending (S22).
3. *"Selection odds depend on sample size."* The 24.5% and 69.2% figures come from one firm and are graded C (S28). DHS's own estimates are in KF1 (S71).
4. *"Visa Bulletin figures should come from State."* travel.state.gov was blocked. Several secondary reports agree (S14–S18).
5. *"Processing times are service standards."* Premium times are service standards that restart after an RFE. DOL times are averages. USCIS tool times are 80%-completion measures (S6, S12, S32).
6. *"Weighted selection may be challenged."* A law firm reports a D.D.C. suit. I could not establish its date or status (S72).
7. *"Fee facts differ between sources."* The visa integrity fee and MRV dates conflict across vendor pages, so I report the conflict rather than pick one (7.3).

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | O-1A has no degree, PhD or citation prerequisite; major award or three of eight criteria, then final merits | confirmed | [S8] [S30] [S7]; the totality test is enforced more tightly (S30, S31) | B |
| K2 | O-1A premium processing $2,965 since 2026-03-01; 15 business days | confirmed | [S11] [S12]; the 15 days is a service standard that restarts after an RFE | B |
| K3 | USCIS publishes the combined O class only: 93.9% FY2025; 91.0% FY2026 Q1–Q3; RFE near 23% in Q3 | confirmed | [S31] [S32] [S30]; Q3 alone is also 91.0%; Q1–Q3 RFE is 24.2%; monthly Q3 RFE was 23.0–23.7% | B |
| K4 | October 2026 Visa Bulletin: India EB-1 2023-02-01, EB-2 2013-11-01, EB-3 2014-01-01 | updated | [S14] [S16] [S17]; October figures confirmed; the November bulletin moved EB-3 India to 2014-01-22 | B |
| K5 | $100,000 extended to 2027-09-21; "struck down" by two courts; $103,265 pending | updated | [S1] [S4] [S19] [S21] [S22]; agency policies were vacated or blocked, not the proclamation; D.D.C. upheld it; three appeals pending; N.D. Cal. scope is clear | B |
| K6 | Petition providers: use-with-care; approval claims self-reported; no audit | confirmed | [S41] [S42] [S31]; no independent audit found | C |
| K7 | Official portals: use | confirmed | [S1] [S6] [S5]; uscis.gov HTML and travel.state.gov blocked automated access | B |

## Absences

- **Blocked official pages.** uscis.gov HTML (H-1B, O-1, L-1, EB pages; processing-times tool) and travel.state.gov (Visa Bulletin, Global Visa Wait Times, MRV and visa integrity fee pages). Looked at: web_fetch on uscis.gov/forms/..., travel.state.gov bulletin HTML and PDF. Used Federal Register, DOL FLAG, AAO PDFs and summaries instead.
- **Official FY2027 H-1B registration chart** (counts by wage level). Not opened; 211,600 comes from media.
- **Standard H-1B I-129 and employment-based I-485 processing times.** Not found.
- **O-1A-only statistics.** Not published (S31, S32).
- **Official USCIS I-140 category tables.** Read only through summaries.
- **Job-seeker, points-based, digital-nomad routes.** None found in the route lists in sources read. B-1 visits not authorising work is recalled (D).
- **Bilateral or special schemes for Indian nationals.** None found.
- **Founder routes, official sources.** The International Entrepreneur Rule and EB-5 details rest on law-firm and vendor pages. I did not open the USCIS I-941 page or the EB-5 Federal Register notice, and I did not confirm the International Entrepreneur Rule's status in an official source. E-2 being unavailable to Indian nationals is recalled (D).
- **Police certificates and document attestation.** An official requirement was not verified; the vendor claim is graded E.
- **GenAI-specific sponsorship statistics.** None found. LCA disclosure files were not queried.
- **Independent audit of provider approval rates.** None found.
- **Spouse work rights for O-3, F-2 and J-2.** Recalled only (D). L-2 and E rights are covered (B).
- **Visa integrity fee and MRV fee.** Official pages not opened; vendor sources conflict on collection status and on the MRV effective date.
- **Weighted-selection suit.** A law firm reports a D.D.C. filing; its date, case name and status were not established.
- **Whether H-1B1 is covered by the $100,000 payment.** Sources disagree; I do not state it.
- **Cap-gap details.** Not verified.
- **December 2026 Visa Bulletin.** Not published as of the last search.

## Open Questions & Risks

- Outcomes in the First, Ninth and D.C. Circuits on the $100,000 payment, and a possible Supreme Court petition.
- Whether the $103,265 fee, the OPT fee, grace-period removal, deference removal and the DOL wage rule are finalised, and whether they are challenged.
- First USCIS data after PA-2026-05 (FY2026 Q4).
- FY2028 registration dates and whether the $103,265 fee would apply to them.
- Outcome of the weighted-selection suit, if it is live.
- Whether the visa integrity fee is being collected at consulates.
- India EB-2 availability when a new fiscal year's numbers run out.
- EB-5 final rule and the 2027-09-30 sunset of the regional centre programme.
- Reliability of vendor-derived USCIS figures.

## Discovered Concerns

- The KB's K5 wording "struck down" overstates the legal position (agency policies, not the proclamation; a split among courts).
- The KB's visa audit excluded H-1B, EB-2, L-1 and student routes, which carry the largest pending changes (KF3, KF4, KF9).
- Several rules stack on the same worker. A graduate could face the OPT fee, the $103,265 fee, loss of the grace period and loss of deference (arithmetic in S22 puts the two fees at $203,265).
- PA-2026-05 applies to all benefit requests, not only O-1.
- The most readable USCIS-data digests come from vendors with commercial interests (S28, S31, S32).
- Vendor pages disagree with each other on the visa integrity fee and on the MRV effective date, so a fee table built from vendors needs a consulate check.
- USCIS and State pages block automated checks, so the 14-day re-verification rule in D-007 must be done in a browser.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Random lottery; $100,000 applies | Updated | Weighted since 2026-02-27 [S1]; $100,000 extended but blocked [S4] [S22] | High: selection rewards wage level |
| P2 | No degree prerequisite; about 94% approval | Updated | Prerequisite confirmed [S8] [S30]; 91.0% [S32] | Medium |
| P3 | EB-2 India over a decade; EB-1 India under four years | Confirmed | 2013-11-01 and 2023-02-01 [S14] | High |
| P4 | OPT 12 + 24 months stable | Updated | In force [S22]; fee NPRM and D/S postponement [S3] [S49] | High for graduates |
| P5 | O-1A reported separately | Contradicted | One O line [S31] [S32] | Low |
| P6 | Gold Card is a statutory visa | Contradicted | Executive order; I-140G in EB-1/EB-2 [S43] [S44] | Low |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Fee for Certain H-1B Petitions (NPRM), 91 FR 54817, DHS/USCIS, https://www.govinfo.gov/content/pkg/FR-2026-08-25/html/2026-17324.htm | 2026-08-25 | 2026-11-13 | A | Read | none | $103,265; weighted selection; proclamation status; 9-11 fee; footnotes |
| S2 | Eliminating the Discretionary 60-day Grace Period (NPRM), 91 FR 57807, https://www.govinfo.gov/content/pkg/FR-2026-09-11/html/2026-18631.htm | 2026-09-11 | 2026-11-13 | B | Extract | single-source | Grace-period NPRM |
| S3 | Optional Practical Training Fees (NPRM), FR Doc 2026-20660, ICE, https://public-inspection.federalregister.gov/2026-20660.pdf | 2026-10-08 | 2026-11-13 | B | Extract | none | OPT fee NPRM |
| S4 | Proclamation 11069, 91 FR 60497, American Presidency Project, https://www.presidency.ucsb.edu/documents/proclamation-11069-restriction-entry-certain-nonimmigrant-workers | 2026-09-18 | 2026-11-13 | B | Extract | none | Extension to 2027-09-21 |
| S5 | USCIS Policy Alert PA-2026-05 (hosted copy), https://www.envoyglobal.com/wp-content/uploads/2026/08/20260805-EvidentiaryStandards.pdf | 2026-08-05 | 2026-11-13 | A | Read | third-party host | Denial without RFE |
| S6 | Processing Times, DOL OFLC FLAG, https://www.flag.dol.gov/processingtimes | 2026-10-31 | 2026-11-13 | A | Read | none | PERM and PWD timings |
| S7 | AAO non-precedent decision (EB-1A), USCIS, https://uscis.gov/sites/default/files/err/B2%20-%20Aliens%20with%20Extraordinary%20Ability/Decisions_Issued_in_2024/MAR042024_03B2203.pdf | 2024-03-04 | 2026-11-13 | A | Read | none | EB-1A framework |
| S8 | AAO non-precedent decision (O-1), USCIS, https://www.uscis.gov/sites/default/files/err/D8%20-%20Aliens%20of%20Extraordinary%20Ability%20or%20Achievement%20%28O-1%2C%20O-2%2C%20and%20O-3%29/Decisions_Issued_in_2024/APR252024_01D8101.pdf | 2024-04-25 | 2026-11-13 | A | Read | none | O-1 structure; petitioner rule |
| S9 | Improving Wage Protections (NPRM), 91 FR 15454, DOL, https://www.federalregister.gov/documents/2026/03/27/2026-06017/improving-wage-protections-for-the-temporary-and-permanent-employment-of-certain-foreign-nationals | 2026-03-27 | 2026-11-13 | B | Extract | none | Wage NPRM; PERM/H-1B overlap |
| S10 | Workplace compliance news, KPA, https://www.kpa.io/workplace-compliance-news-resources | 2026 | 2026-11-13 | B | Extract | single-source | Proposed percentiles |
| S11 | Premium processing fee rule, FR 2026-00321 (mirror), https://policyrisk.com/behind-the-curtain/federal-register/2026-00321 | 2026-01-12 | 2026-11-13 | B | Extract | mirror | $2,965 |
| S12 | How Do I Request Premium Processing?, USCIS, https://uscis.gov/forms/how-do-i-request-premium-processing | 2026 | 2026-11-13 | B | Extract | fetch blocked | Service standards |
| S13 | Visa Bulletin for November 2026, U.S. Department of State, https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2027/visa-bulletin-for-november-2026.html | 2026-10-22 | 2026-11-13 | B | Blocked | not opened | Origin of S14–S18 |
| S14 | US Visa Bulletin November 2026, BusinessToday, https://www.businesstoday.in/nri/visa/story/us-visa-bulletin-november-2026-india-eb-3-advances-eb-1-and-eb-2-remain-unchanged-563281-2026-10-23 | 2026-10-23 | 2026-11-13 | B | Extract | corroborated | India dates |
| S15 | November 2026 Visa Bulletin, CI Law Group, https://cilawgroup.com/?p=16977 | 2026-10 | 2026-11-13 | B | Extract | corroborated | Dates for Filing |
| S16 | US Visa Bulletin October 2026, BusinessToday, https://www.businesstoday.in/nri/visa/story/us-visa-bulletin-october-2026-eb-1-india-moves-forward-eb-2-becomes-available-again-559114-2026-10-01 | 2026-10-01 | 2026-11-13 | B | Extract | none | October figures |
| S17 | August 2026 Visa Bulletin, BAL, https://bal.com/immigration-news/united-states-august-2026-visa-bulletin-china-eb-3-advances-india-eb-2-remains-unavailable | 2026-07 | 2026-11-13 | B | Extract | none | India EB-2 unavailable |
| S18 | November 2026 Visa Bulletin Explained, F1Jobs, https://www.f1jobs.io/resources/blog/november-2026-visa-bulletin-explained-eb2-eb3-india | 2026-11 | 2026-11-13 | C | Extract | COI-light | Approved petitions awaiting numbers |
| S19 | Federal Court Vacates $100,000 H-1B Visa Fee, Clark Hill, https://www.clarkhill.com/news-events/news/h1b-fee-struck-down-massachusetts-court-2026/ | 2026-06 | 2026-11-13 | B | Extract | none | D. Mass. ruling |
| S20 | First Circuit order, No. 26-1699, https://www.ca1.uscourts.gov/sites/ca1/files/opnfiles/26-1699O-01A.pdf | 2026-07 | 2026-11-13 | B | Extract | court record | Stay denied |
| S21 | Second Federal Court Blocks the $100,000 Fee, Democracy Forward, https://democracyforward.org/news/press-releases/second-federal-court-blocks-trump-vance-administrations-unlawful-innovation-ban/ | 2026-10 | 2026-11-13 | C | Extract | party press release | N.D. Cal. ruling |
| S22 | A $100,000 Path to a U.S. Career, Herman Legal Group, https://www.lawfirm4immigrants.com/opt-fee-70000-h1b-cost-foreign-graduates/ | 2026-11-11 | 2026-11-13 | B | Read | COI | Litigation; OPT; deference; fees |
| S23 | Where Things Stand in November 2026, Ahluwalia Law, https://www.ahluwalialaw.com/what-is-happening-to-the-100000-h-1b-fee-where-things-stand-in-november-2026/ | 2026-11 | 2026-11-13 | B | Extract | COI; corroborated | Litigation status |
| S24 | Tracking Immigration Changes, Caltech International Offices, https://international.caltech.edu/maintainstatus/tracking-immigration-changes | 2026-11 | 2026-11-13 | B | Read | university summary | Status list |
| S25 | DHS proposes rule to end 60-day H-1B grace period, immpolicytracking.org, https://immpolicytracking.org/policies/dhs-proposes-rule-to-end-60-day-h-1b-grace-period/ | 2026-09-11 | 2026-11-13 | B | Extract | none | Comment deadline |
| S26 | USCIS Completes FY 2027 H-1B Cap Selection, Fragomen, https://www.fragomen.com/insights/united-states-uscis-completes-fy-2027-h-1b-cap-selection-process.html | 2026-03-31 | 2026-11-13 | B | Extract | none | FY2027 selection |
| S27 | H-1B FY2027 cap reached, Outlook Business, https://www.outlookbusiness.com/amp/story/news/h-1b-fy2027-cap-reached-what-it-means-for-applicants-and-employers | 2026 | 2026-11-13 | B | Extract | none | 211,600; 343,981 |
| S28 | Analyzing our H-1B selection results FY2027, Manifest Law, https://manifestlaw.com/blog/immigration/news/analyzing-our-h1b-selection-results-fy2027/ | 2026 | 2026-11-13 | C | Extract | COI; single-source | Selection rates |
| S29 | USCIS reaches FY 2027 H-1B cap, Staffing Industry Analysts, https://www.staffingindustry.com/editorial/cws-30-contingent-workforce-strategies/uscis-reaches-fy-2027-h-1b-cap- | 2026-07-22 | 2026-11-13 | B | Extract | none | 71.5%; 17.7% |
| S30 | Your O-1 Petition Meets Three Criteria, SMA Law Firm, https://smaimmigration.com/your-o-1-petition-meets-three-criteria-that-is-no-longer-enough/ | 2026-09 | 2026-11-13 | B | Read | COI | O-1A criteria; denial trends |
| S31 | USCIS Q3 FY2026 approval data, Manifest Law, https://manifestlaw.com/news/uscis-q3-fy2026-approval-data-09-09-2026 | 2026-09-09 | 2026-11-13 | C | Extract | COI | O, EB-1A, NIW rates |
| S32 | O-1, L-1 and TN approval and RFE rates, F1Jobs, https://www.f1jobs.io/resources/blog/o1-l1-tn-approval-and-rfe-rates-2026 | 2026-11-01 | 2026-11-13 | B | Read | COI-light | I-129 rates; processing tool; policy status |
| S33 | USCIS Report: Employment-Based Immigration Petitions, American Immigration Council, https://www.americanimmigrationcouncil.org/wp-content/uploads/2026/08/USCIS-Report_Employment-Based-Immigration-Petitions.pdf | 2026-08 | 2026-11-13 | B | Extract | none | NIW filings; backlog |
| S34 | H-1B Petitions and Denial Rates FY 2025, NFAP, https://nfap.com/wp-content/uploads/2025/11/H-1B-Petitions-and-Denial-Rates-For-FY-2025.NFAP-Policy-Brief.2025.pdf | 2025-11 | 2026-11-13 | B | Extract | advocacy | Top employers |
| S35 | H-1B Approvals Hit 406,348 in FY 2025, Visaverge, https://www.visaverge.com/news/h-1b-approvals-hit-406348-in-fy-2025-uscis-data-reveals-wage-weighted-system-impact/ | 2026 | 2026-11-13 | B | Extract | none | FY2025 report figures |
| S36 | US visa wait times October 2026, BusinessToday, https://www.businesstoday.in/nri/visa/story/us-visa-wait-times-october-2026-check-tourist-student-and-work-visa-timelines-in-india-563154-2026-10-23 | 2026-10-23 | 2026-11-13 | B | Extract | secondary | DoS wait times |
| S37 | H-1B, H-4 Appointments Rescheduling, Mondaq, https://www.mondaq.com/unitedstates/work-visas/1726436/h1b-h4-visa-appointments-rescheduling-begins-amid-expanded-social-media-vetting-policies | 2025-12 | 2026-11-13 | B | Extract | none | Vetting; rescheduling |
| S38 | H-1B Visa Stamping in India, Berardi Immigration Law, https://berardiimmigrationlaw.com/h-1b-visa-stamping-in-india-current-rules-wait-times-and-what-to-expect-in-2026/ | 2026-07 | 2026-11-13 | C | Extract | COI | In-person interview |
| S39 | US halts immigration visas for 75 countries, Business Standard, https://www.business-standard.com/immigration/us-halts-immigration-visas-for-75-countries-full-list-and-impact-explained-126011500190_1.html | 2026-01-15 | 2026-11-13 | B | Extract | none | India not listed |
| S40 | A Guide to Trump's Travel Ban and Visa Pause, Council on Foreign Relations, https://www.cfr.org/articles/guide-countries-trumps-travel-ban-list | 2026 | 2026-11-13 | B | Extract | none | Pause set aside |
| S41 | WeGreened.com, North America Immigration Law Group, https://www.wegreened.com/ | 2026 | 2026-11-13 | A | Extract | COI | Own claims (A); outcomes (C) |
| S42 | Beyond Border vs. WeGreened, Beyond Border Global, https://www.beyondborderglobal.com/resources/beyond-border-vs-wegreened | 2026 | 2026-11-13 | C | Extract | COI | Self-reported claims |
| S43 | Trump's $1 million Gold Card fails to catch on, CNBC, https://www.cnbc.com/2026/05/08/trump-gold-card-wealth.html | 2026-05-08 | 2026-11-13 | B | Extract | none | Gold Card uptake |
| S44 | AAUP v. DHS, 1:26-cv-00300, Civil Rights Litigation Clearinghouse, https://clearinghouse.net/case/47793/ | 2026-02-03 (filing) | 2026-11-13 | B | Extract | none | Litigation |
| S45 | Gold Card visa is processing applications, EB5Investors, https://www.eb5investors.com/blog/gold-card-visa-is-processing-applications-but-legal-challenges-mount/ | 2026 | 2026-11-13 | C | Extract | COI | 338/165/59 |
| S46 | USCIS Issues New Policy Memo on Adjustment of Status, Brown Immigration Law, https://brownimmigrationlaw.com/?p=4462 | 2026-05 | 2026-11-13 | B | Extract | none | PM-602-0199 |
| S47 | H-4 spouses topic, JD Supra (Jackson Lewis), https://www.jdsupra.com/topics/h-4-spouses | 2025-10 | 2026-11-13 | B | Extract | none | Certiorari denial |
| S48 | H-4 EAD 2026 auto extension ended, F1Jobs, https://www.f1jobs.io/resources/blog/h4-ead-2026-auto-extension-ended | 2026 | 2026-11-13 | C | Extract | COI-light | EAD rule |
| S49 | 2026 F-1 and J-1 Rule Change, Mondaq, https://www.mondaq.com/unitedstates/work-visas/1845774/2026-f-1-and-j-1-rule-change-employer-and-talent-pipeline-impact-report | 2026-09 | 2026-11-13 | B | Extract | none | D/S rule postponed |
| S50 | Schedule A, Group II, Fragomen, https://www.fragomen.com/insights/beyond-perm-leveraging-schedule-a-group-ii-for-exceptional-ability-in-the-sciences-arts-and-performing-arts.html | 2025-10-08 | 2026-11-13 | B | Extract | none | Schedule A |
| S51 | Insightful Immigration Blog (India), Cyrus Mehta, https://blog.cyrusmehta.com/tag/india-inc | 2026 | 2026-11-13 | B | Extract | practitioner | EDGE; degree equivalence |
| S52 | Cost to sponsor a work visa, Rippling, https://www.rippling.com/blog/how-much-does-it-cost-to-sponsor-a-work-visa | 2026 | 2026-11-13 | C | Extract | COI | L-1 and H-1B fees |
| S53 | H-1B fees, Ellis, https://www.ellis.com/resources/h1b-fees | 2026 | 2026-11-13 | C | Extract | COI | H-1B fee list |
| S54 | PERM processing times, CI Law Group, https://cilawgroup.com/news/2026/11/04/perm-labor-certification-processing-times/ | 2026-11-04 | 2026-11-13 | C | Extract | COI | 16–20 months |
| S55 | H-4 EAD 2026 guide, visa-pros.com, https://visa-pros.com/?p=5275 | 2026 | 2026-11-13 | C | Extract | single-source | H-4 EAD eligibility |
| S56 | FY2027 H-1B registration timeline, Alma, https://tryalma.com/learn/fy2027-h1b-registration-dates-timeline | 2026 | 2026-11-13 | C | Extract | COI | Weighted rule dates |
| S57 | NIW guide, Beyond Border Global, https://www.beyondborderglobal.com/resources/how-policy-analysts-can-strengthen-their-niw-case | date not shown | 2026-11-13 | C | Extract | COI | I-140 $715; $300 |
| S58 | US visa types explained, Beyond Border Global, https://www.beyondborderglobal.com/resources/us-visa-types-explained | 2026 | 2026-11-13 | C | Extract | COI | O-1 and L-1 fees; stale $100,000 |
| S59 | EB-2 NIW for AI and ML engineers, F1Jobs, https://www.f1jobs.io/resources/blog/eb2-niw-for-ai-machine-learning-engineers | 2026-11 | 2026-11-13 | C | Extract | COI-light | NIW 30 months; RIN 1615-AD25 |
| S60 | EB-2 NIW requirements for AI researchers, Beyond Border Global, https://www.beyondborderglobal.com/resources/eb-2-niw-requirements-for-ai-researchers-in-germany | 2025-11-27 | 2026-11-13 | C | Extract | COI; single-source | 90% vs 61% claim (E) |
| S61 | USCIS Issues Additional Guidance on the Proclamation Imposing $100,000 Payment, Ogletree Deakins, https://ogletree.com/insights-resources/blog-posts/uscis-issues-additional-guidance-on-the-proclamation-imposing-100000-payment-for-h-1b-petitions/ | 2025-10 | 2026-11-13 | B | Extract | corroborated | Cap-exempt coverage; beneficiaries abroad |
| S62 | Updated Guidance on Presidential Proclamation Imposing $100,000 Fee, Herbert Smith Freehills Kramer via JD Supra, https://www.jdsupra.com/legalnews/updated-guidance-on-presidential-1397258/ | 2025-10 | 2026-11-13 | B | Extract | corroborated | Exemptions for granted changes of status |
| S63 | International Entrepreneur Rule (IER): Parole for Startup Founders in 2026, Headman Law Group, https://headmanlaw.com/insights/international-entrepreneur-rule-ier-parole-2026/ | 2026-07-22 | 2026-11-13 | C | Extract | COI; single-source | IER parameters |
| S64 | Proposed EB-5 Changes, Fennemore, https://www.fennemorelaw.com/proposed-eb-5-changes-what-investors-and-regional-centers-should-know-now/ | 2026-07 | 2026-11-13 | B | Extract | none | $1,400,000 tier; thresholds; inflation |
| S65 | DHS Proposes Major Overhaul of EB-5 Program Regulations, EIG Law, https://eiglaw.com/dhs-proposes-major-overhaul-of-eb-5-program-regulations/ | 2026-07 | 2026-11-13 | B | Extract | corroborated | EB-5 proposed rule |
| S66 | USCIS Issues Further Guidance on Employment Authorization for E and L Spouses, Fragomen, https://www.fragomen.com/insights/united-states-uscis-issues-further-guidance-on-employment-authorization-for-e-and-l-spouses.html | date not shown | 2026-11-13 | B | Extract | none | L-2 and E spouse work incident to status |
| S67 | Entrepreneur visa guide, Lighthouse HQ, https://www.lighthousehq.com/blog/entrepreneur-visa | 2026-09 | 2026-11-13 | C | Extract | COI | IER thresholds; EB-5 amounts |
| S68 | New visa integrity fee, Greenberg Traurig, https://www.gtlaw-insidebusinessimmigration.com/?p=10280 | 2025 | 2026-11-13 | B | Extract | none | $250 per issuance; dependants; no fee on change of status |
| S69 | New $250 Visa Integrity Fee for H-1B, L-1, O-1 and TN, F1Jobs, https://www.f1jobs.io/resources/blog/visa-integrity-fee-250-work-visas-2026 | 2026-09-13 | 2026-11-13 | C | Extract | COI-light; conflicts with S75 | Collection claim; MRV $190 to $205 |
| S70 | DS-160 form, Alma, https://www.tryalma.com/learn/ds-160-form | 2026-06 | 2026-11-13 | C | Extract | COI | MRV $205 since 2023-06-17 |
| S71 | H-1B Program Update: DC Court Upholds Proclamation as DHS Finalizes Wage-Weighted Lottery, National Law Review, https://natlawreview.com/article/h-1b-program-update-dc-court-upholds-presidential-proclamation-dhs-finalizes-wage | 2026-01-05 | 2026-11-13 | B | Extract | none | DHS selection estimates |
| S72 | Lawsuit Challenges Using Wages as an H-1B Selection Factor, Berardi Immigration Law, https://berardiimmigrationlaw.com/?p=12734 | date not shown | 2026-11-13 | C | Extract | COI; single-source | Weighted-selection suit |
| S73 | Changes in the U.S. naturalization process, DeWitt LLP, https://dewittllp.com/news/2025/10/03/changes-in-the-u.s.-naturalization-process-for-permanent-residents-applying-for-u.s.-citizenship | 2025-10-03 | 2026-11-13 | B | Extract | none | Five-year rule; 2025 civics test |
| S74 | H-4 EAD 2026 eligibility, Ahluwalia Law, https://www.ahluwalialaw.com/?p=34299 | 2026 | 2026-11-13 | B | Extract | COI | H-4 pathways; EAD suit 2026-01-08 |
| S75 | Nonimmigrant visa (MRV) fees explained, VisaLedger, https://visa-fees.pages.dev/blog/nonimmigrant-visa-mrv-fees-explained/ | 2026-06-15 | 2026-11-13 | C | Extract | single-source; low provenance | Fee not collected as of mid-2026 |
| S76 | DHS proposes sweeping EB-5 overhaul, Outbound Investment, https://outboundinvestment.com/dhs-proposes-sweeping-eb-5-overhaul-with-new-investor-protections-stronger-oversight-and-higher-investment-thresholds/ | 2026-07 | 2026-11-13 | C | Extract | single-source | Comment deadline; sunset date |

## Data Appendix

```jsonl
{"type":"visa_route","country":"US","route":"H-1B specialty occupation (cap-subject, incl. US master's exemption)","kind":"employer-sponsored","eligibility":"US employer files I-129 with certified LCA; bachelor's or higher in the specialty or equivalent; registration and weighted selection; 65,000 + 20,000 numbers per FY","url":"https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations","salary_threshold":null,"quota":"85,000 per FY; FY2027 cap reached, no second round; entries 4/3/2/1 by OEWS level since 2026-02-27","processing":{"lo":15,"hi":15,"unit":"business days"},"fees":"$215 registration; I-129 $780 ($460); ACWIA $1,500 ($750); fraud $500; asylum $600 ($300/$0); PL 114-113 $4,000 for covered employers; premium $2,965; $100,000 blocked; $103,265 proposed","validity":"Six-year limit with AC21 exceptions; initial grant length not verified","dependants":"H-4; H-4 EAD only with approved I-140 or AC21 extension","pr_path":"Employer PERM to EB-2/EB-3 (or EB-1); India queue per Visa Bulletin","language":"None found","changes":"2025-01-17 modernisation rule; 2026-02-27 weighted selection; 2025-09-21 payment (blocked); 2026-08-25 $103,265 NPRM","india_note":"69.9% of FY2025 approvals India-born; consular waits 1 to 6.5 months","note":"No fixed salary threshold; premium time is a service standard","grade":"B","src":["S1","S22","S26","S52","S53","S55"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"H-1B cap-exempt employer","kind":"employer-sponsored","eligibility":"University or affiliated non-profit; non-profit or government research organisation; workers already counted who change jobs or extend within six years","url":"https://www.uscis.gov/working-in-the-united-states/h-1b-specialty-occupations","salary_threshold":null,"quota":"Exempt from the cap","processing":{"lo":15,"hi":15,"unit":"business days"},"fees":"As H-1B; outside the $103,265 proposal","validity":"As H-1B","dependants":"As H-1B","pr_path":"As H-1B","language":"None found","changes":"$103,265 NPRM excludes cap-exempt; $100,000 payment covers cap-exempt petitions for workers abroad (blocked)","india_note":"Not specific","note":"Payment coverage from USCIS guidance of 2025-10-20 as reported by law firms","grade":"B","src":["S1","S61","S62"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"O-1A extraordinary ability (sciences, education, business, athletics)","kind":"talent","eligibility":"Major award or 3 of 8 criteria, then totality judgement; petition by US employer or US agent; no degree prerequisite","url":"https://www.uscis.gov/working-in-the-united-states/temporary-workers/o-1-visa-individuals-with-extraordinary-ability-or-achievement","salary_threshold":null,"quota":"None","processing":{"lo":14.5,"hi":14.5,"unit":"months"},"fees":"I-129 $1,055 ($530); asylum $600 ($300); premium $2,965","validity":"Not verified","dependants":"O-3 (no work; recalled)","pr_path":"EB-1A, NIW or PERM","language":"None found","changes":"2025-01-08 PA-2025-02; 2026-08-05 PA-2026-05","india_note":"Not lottery-bound; consular wait applies if abroad","note":"Processing is the 80% standard figure","grade":"B","src":["S5","S8","S30","S32","S58"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"L-1A manager or executive","kind":"intra-company","eligibility":"One continuous year abroad with a qualifying related entity in prior three years; 7-year maximum; new office starts at one year","url":"https://www.uscis.gov/working-in-the-united-states/temporary-workers/l-1a-intracompany-transferee-executive-or-manager","salary_threshold":null,"quota":"None","processing":{"lo":6.5,"hi":6.5,"unit":"months"},"fees":"I-129 $1,385 ($695); fraud $500; asylum $600 ($300); premium $2,965; PL 114-113 $4,500 for covered employers","validity":"7 years maximum","dependants":"L-2; spouse works incident to status with an annotated I-94","pr_path":"EB-1C or PERM","language":"None found","changes":"2026-08-10 9-11 fee rule extends to all extensions","india_note":"Named in the brief as common for IT services and GCCs; not measured","note":"Approval 91.2%; RFE 25.9%","grade":"B","src":["S1","S32","S52","S58","S66"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"L-1B specialised knowledge","kind":"intra-company","eligibility":"As L-1A with specialised knowledge; 5-year maximum","url":"https://www.uscis.gov/working-in-the-united-states/temporary-workers/l-1a-intracompany-transferee-executive-or-manager","salary_threshold":null,"quota":"None","processing":{"lo":6.5,"hi":6.5,"unit":"months"},"fees":"As L-1A","validity":"5 years maximum","dependants":"L-2; spouse works incident to status with an annotated I-94","pr_path":"PERM","language":"None found","changes":"As L-1A","india_note":"As L-1A","note":"Approval 91.3%; RFE 29.4%","grade":"B","src":["S32","S52","S66"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"EB-1A extraordinary ability","kind":"talent","eligibility":"Major award or 3 of 10 criteria, then final merits; no offer or PERM","url":"https://uscis.gov/sites/default/files/err/B2%20-%20Aliens%20with%20Extraordinary%20Ability/Decisions_Issued_in_2024/MAR042024_03B2203.pdf","salary_threshold":null,"quota":"Annual EB-1 limit; India dated queue","processing":{"lo":23.5,"hi":23.5,"unit":"months"},"fees":"I-140 $715 + $300 self-petitioner + premium $2,965","validity":"Permanent residence","dependants":"Derivatives","pr_path":"Direct; India final action 2023-02-01","language":"None found","changes":"Approval 66.9% FY2025; 32.2% FY2026 Q3","india_note":"EB-1 India about 3.8 years behind the calendar (M)","note":"Standard time as of 2026-04","grade":"B","src":["S7","S31","S57","S14"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"EB-2 national interest waiver","kind":"self-sponsored","eligibility":"Advanced degree or exceptional ability; Dhanasar three prongs; no PERM","url":"https://www.uscis.gov/policy-manual","salary_threshold":null,"quota":"Annual EB-2 limit; India dated queue","processing":{"lo":24,"hi":30,"unit":"months"},"fees":"I-140 $715 + $300 + premium $2,965 (45 business days)","validity":"Permanent residence","dependants":"Derivatives","pr_path":"Direct; India final action 2013-11-01","language":"None found","changes":"Approval 55.2% FY2025; 35.7% FY2025 Q4; 55.3% FY2026 Q3","india_note":"EB-2 India about 13.0 years behind the calendar (M)","note":"Approval and time from vendor readings","grade":"C","src":["S31","S59","S12","S57"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"EB-2/EB-3 via PERM","kind":"employer-sponsored","eligibility":"DOL prevailing-wage determination, recruitment, then I-140","url":"https://flag.dol.gov/programs/perm","salary_threshold":null,"quota":"Annual limits; India dated queue","processing":{"lo":16,"hi":20,"unit":"months"},"fees":"I-140 $715 + asylum $600; recruitment adverts not verified","validity":"Permanent residence","dependants":"Derivatives","pr_path":"India final action: EB-2 2013-11-01; EB-3 2014-01-22","language":"None found","changes":"DOL wage NPRM (proposed)","india_note":"EB-3 ahead of EB-2; three-year degree issue","note":"Official analyst review 300-360 days; end-to-end figure from a law firm","grade":"B","src":["S6","S14","S54","S57"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"F-1 OPT and STEM OPT","kind":"graduate","eligibility":"F-1 student; 12 months OPT; 24-month STEM extension","url":"https://www.ice.gov/sevis","salary_threshold":null,"quota":"None","processing":{"lo":30,"hi":30,"unit":"business days"},"fees":"Premium I-765 $1,780; proposed school fee $70,000/$30,000 (not in force)","validity":"12 + 24 months","dependants":"F-2 (recalled)","pr_path":"None directly","language":"None found","changes":"2026-07-17 D/S rule (postponed); 2026-10-08 OPT fee NPRM","india_note":"Large student flow; not measured","note":"Premium time is a service standard","grade":"B","src":["S3","S12","S22","S49"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"E-3 / H-1B1 / TN (treaty categories)","kind":"employer-sponsored","eligibility":"Australia (E-3); Chile and Singapore (H-1B1); Canada and Mexico (TN)","url":"https://travel.state.gov/content/travel/en/us-visas/employment/temporary-worker-visas.html","salary_threshold":null,"quota":"Not verified","processing":null,"fees":"Not verified","validity":"Not verified","dependants":"E spouses work incident to status with an annotated I-94","pr_path":"None direct","language":"None found","changes":"TN screening expanded 2026-09-18","india_note":"Indian nationals ineligible","note":"Page not opened","grade":"B","src":["S1","S32","S66"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"Gold Card (Form I-140G via EB-1A or EB-2 NIW)","kind":"talent","eligibility":"$1,000,000 gift ($2,000,000 corporate); lawful funds; vetting","url":"https://trumpcard.gov","salary_threshold":null,"quota":"Within EB-1/EB-2 numbers","processing":null,"fees":"$15,000 fee plus the gift","validity":"Permanent residence","dependants":"Not verified","pr_path":"Same EB queue and per-country caps","language":"None found","changes":"Executive order 2025-09-19; AAUP v. DHS filed 2026-02-03","india_note":"Same India queue","note":"Executive order only; litigation pending","grade":"B","src":["S43","S44","S45"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"visa_route","country":"US","route":"International Entrepreneur Rule (parole for start-up founders)","kind":"founder","eligibility":"Founder of a funded start-up; Form I-941; $311,071 qualified investment or $124,429 government grants; ownership floors of 10% initial and 5% re-parole (recalled, unverified)","url":null,"salary_threshold":null,"quota":"Up to three entrepreneurs per start-up (recalled)","processing":null,"fees":"I-941 $1,200 (vendor)","validity":"30 months plus 30-month re-parole","dependants":"Not verified","pr_path":"None direct; O-1A, EB-1A, NIW, EB-5 or PERM","language":"None found","changes":"No rescission found in sources read","india_note":"Not specific","note":"Parole, not a visa; official page not opened","grade":"C","src":["S63","S67"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"visa_route","country":"US","route":"EB-5 immigrant investor","kind":"self-sponsored","eligibility":"$1,050,000 standard or $800,000 in a targeted employment area or infrastructure project; job creation required (10 full-time jobs, recalled); proposed $1,400,000 tier for high-employment areas","url":null,"salary_threshold":null,"quota":"Annual EB-5 limit; regional centre authority to 2027-09-30","processing":null,"fees":"Not itemised","validity":"Permanent residence","dependants":"Derivatives","pr_path":"Direct","language":"None found","changes":"Proposed rule published 2026-07-02; inflation adjustment due 2027-01-01","india_note":"Not specific","note":"Official notice not opened","grade":"B","src":["S64","S65","S76"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"measure","subject":"H-1B cap registrations FY2027","measure":"registrations","unit":"count","value":211600,"region":"US","method":"Reported from USCIS data; chart not opened","note":"FY2026: 343,981; fall 38.5% (M)","grade":"B","src":["S27"],"as_of":"2026-03-19","ttl":"V4"}
{"type":"measure","subject":"H-1B FY2027 selection rate by wage level (one firm's registrants)","measure":"selection rate","unit":"percent","lo":24.5,"hi":69.2,"method":"Level I 24.5%, II 50.0%, III 69.2%, IV 65.2%; sample size not disclosed; COI","region":"US","grade":"C","src":["S28"],"as_of":"2026-03-31","ttl":"V4"}
{"type":"measure","subject":"DHS estimated H-1B selection chance by wage level","measure":"estimated selection rate","unit":"percent","lo":15.29,"hi":61.16,"method":"Level I 15.29%, II 30.58%, III 45.87%, IV 61.16%","region":"US","note":"Old random lottery averaged about 29.59%","grade":"B","src":["S71"],"as_of":"2026-02-27","ttl":"V4"}
{"type":"measure","subject":"USCIS I-129 H-1B approval rate","measure":"approval rate","unit":"percent","value":97.0,"n":278650,"region":"US","method":"FY2026 Q1-Q3 decisions; RFE rate 8.5%","grade":"B","src":["S32"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"USCIS I-129 O classification approval rate","measure":"approval rate","unit":"percent","value":91.0,"n":23417,"region":"US","method":"FY2026 Q1-Q3 decisions; RFE rate 24.2%; combines O-1A, O-1B, O-2","note":"FY2025: 93.9%","grade":"B","src":["S32","S31","S30"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"USCIS I-129 L-1A approval rate","measure":"approval rate","unit":"percent","value":91.2,"n":18553,"region":"US","method":"FY2026 Q1-Q3; RFE rate 25.9%","grade":"B","src":["S32"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"USCIS I-129 L-1B approval rate","measure":"approval rate","unit":"percent","value":91.3,"n":10263,"region":"US","method":"FY2026 Q1-Q3; RFE rate 29.4%","grade":"B","src":["S32"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"USCIS I-140 EB-1A approval rate","measure":"approval rate","unit":"percent","value":32.2,"region":"US","method":"FY2026 Q3; FY2025 66.9%; vendor reading of USCIS data","grade":"C","src":["S31"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"USCIS I-140 EB-2 NIW approval rate","measure":"approval rate","unit":"percent","value":55.3,"region":"US","method":"FY2026 Q3; FY2025 55.2%; FY2025 Q4 trough 35.7%; vendor reading","grade":"C","src":["S31"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"DOL PERM analyst review average","measure":"processing time","unit":"calendar days","lo":300,"hi":360,"method":"Last 30, 90 and 180 days: 300, 315, 360","region":"US","grade":"A","src":["S6"],"as_of":"2026-10-31","ttl":"V1"}
{"type":"measure","subject":"DOL H-1B prevailing wage queue","measure":"receipt month being processed","unit":"month","value":"2026-07","region":"US","method":"OEWS and non-OEWS","note":"PERM: 2026-08 (OEWS), 2026-07 (non-OEWS)","grade":"A","src":["S6"],"as_of":"2026-10-31","ttl":"V1"}
{"type":"measure","subject":"Visa Bulletin India EB-1 final action date","measure":"priority-date cutoff","unit":"ISO date","value":"2023-02-01","region":"India","note":"About 3.8 years behind the calendar (M)","grade":"B","src":["S14","S15"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"Visa Bulletin India EB-2 final action date","measure":"priority-date cutoff","unit":"ISO date","value":"2013-11-01","region":"India","note":"Unavailable July-September 2026; about 13.0 years behind (M)","grade":"B","src":["S14","S17"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"Visa Bulletin India EB-3 final action date","measure":"priority-date cutoff","unit":"ISO date","value":"2014-01-22","region":"India","note":"October 2026 was 2014-01-01; about 12.8 years behind (M)","grade":"B","src":["S14","S16"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"Visa Bulletin India EB-1 dates for filing","measure":"priority-date cutoff","unit":"ISO date","value":"2024-07-01","region":"India","note":"USCIS directed I-485 filers to this chart for November 2026","grade":"B","src":["S15"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"Visa Bulletin India EB-2 and EB-3 dates for filing","measure":"priority-date cutoff","unit":"ISO date","value":"2015-01-15","region":"India","note":"Same date for both categories","grade":"B","src":["S15"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"Approved EB-2 India petitions awaiting numbers","measure":"backlog","unit":"count","value":356360,"region":"India","note":"EB-3 India: 106,214; FY2026 Q3","grade":"C","src":["S18"],"as_of":"2026-06-30","ttl":"V1"}
{"type":"measure","subject":"DoS next-available wait, H/L/O/P/Q, Mumbai","measure":"consular wait","unit":"months","value":2,"region":"India","note":"Estimate, not a promised wait","grade":"B","src":["S36"],"as_of":"2026-10-21","ttl":"V1"}
{"type":"measure","subject":"DoS next-available wait, H/L/O/P/Q, New Delhi","measure":"consular wait","unit":"months","value":3.5,"region":"India","grade":"B","src":["S36"],"as_of":"2026-10-21","ttl":"V1"}
{"type":"measure","subject":"DoS next-available wait, H/L/O/P/Q, Hyderabad","measure":"consular wait","unit":"months","value":6.5,"region":"India","grade":"B","src":["S36"],"as_of":"2026-10-21","ttl":"V1"}
{"type":"measure","subject":"DoS next-available wait, H/L/O/P/Q, Chennai","measure":"consular wait","unit":"months","value":2.5,"region":"India","grade":"B","src":["S36"],"as_of":"2026-10-21","ttl":"V1"}
{"type":"measure","subject":"DoS next-available wait, H/L/O/P/Q, Kolkata","measure":"consular wait","unit":"months","value":1,"region":"India","grade":"B","src":["S36"],"as_of":"2026-10-21","ttl":"V1"}
{"type":"measure","subject":"H-1B approvals FY2025","measure":"approvals","unit":"count","value":406348,"region":"US","note":"India-born 283,772 (69.9%); computer occupations 252,088 (62%)","grade":"B","src":["S35"],"as_of":"2025-09-30","ttl":"V4"}
{"type":"measure","subject":"Median annual compensation, approved H-1B beneficiaries FY2025","measure":"median compensation","unit":"USD per year","value":133000,"region":"US","note":"Initial about 103,000; continuing about 141,000; not a salary threshold","grade":"A","src":["S1","S35"],"as_of":"2025-09-30","ttl":"V4"}
{"type":"measure","subject":"Amazon H-1B initial-employment approvals FY2025","measure":"approvals","unit":"count","value":4644,"region":"US","note":"Meta 1,555; Microsoft 1,394; Google 1,050","grade":"B","src":["S34"],"as_of":"2025-09-30","ttl":"V4"}
{"type":"measure","subject":"Top seven India-based IT firms, initial H-1B approvals FY2025","measure":"approvals","unit":"count","value":4573,"region":"India","note":"Down 37% on FY2024","grade":"B","src":["S34"],"as_of":"2025-09-30","ttl":"V4"}
{"type":"measure","subject":"PERM filings for workers already in H-1B status, FY2024","measure":"share","unit":"percent","value":57.6,"region":"US","grade":"B","src":["S9"],"as_of":"2024-09-30","ttl":"V4"}
{"type":"measure","subject":"Gold Card requests received by USCIS","measure":"requests","unit":"count","value":338,"region":"US","note":"165 fees paid; 59 I-140G petitions; one approval reported","grade":"C","src":["S45","S43"],"as_of":"2026-04-28","ttl":"V0"}
{"type":"measure","subject":"Premium processing fee, I-129 and I-140","measure":"fee","unit":"USD per request","value":2965,"region":"US","note":"Service standard 15 business days; 45 for NIW and EB-1C I-140","grade":"B","src":["S11","S12"],"as_of":"2026-03-01","ttl":"V4"}
{"type":"measure","subject":"Proposed H-1B cap-subject fee","measure":"fee","unit":"USD per petition","value":103265,"region":"US","note":"Proposed 2026-08-25; not in force","grade":"A","src":["S1"],"as_of":"2026-08-25","ttl":"V0"}
{"type":"measure","subject":"Proposed OPT fees paid by schools","measure":"fee","unit":"USD per recommendation","lo":30000,"hi":70000,"note":"$70,000 first; $30,000 each later; not in force","region":"US","grade":"B","src":["S3","S22"],"as_of":"2026-10-08","ttl":"V0"}
{"type":"measure","subject":"USCIS standard processing, I-129 O petitions","measure":"processing time","unit":"months","value":14.5,"region":"US","method":"80% completed within; tool read 2026-11-01; L 6.5; TN 4.5","grade":"B","src":["S32"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"USCIS standard processing, I-140 EB-2 NIW","measure":"processing time","unit":"months","lo":24,"hi":30,"method":"24 (2026-04, vendor); 30 (tool read 2026-11-01, vendor); EB-1A 23.5 (2026-04)","region":"US","grade":"C","src":["S31","S59"],"as_of":"2026-11-01","ttl":"V1"}
{"type":"measure","subject":"MRV fee, petition-based work visas (H, L, O, P, Q, R)","measure":"fee","unit":"USD per applicant","value":205,"region":"US","note":"Vendors disagree on when it began: schedule of 2023-06-17 (S70) or rise from $190 on 2026-05-30 (S69)","grade":"C","src":["S69","S70","S75"],"as_of":"2026-06-15","ttl":"V2"}
{"type":"measure","subject":"Visa integrity fee per nonimmigrant visa issuance","measure":"fee","unit":"USD per issuance","value":250,"region":"US","note":"Includes dependants; not charged on a change of status inside the US; collection status contested (S69 collected since 2025-10-01; S75 not collected as of 2026-06-15)","grade":"B","src":["S68","S69","S75"],"as_of":"2026-09-13","ttl":"V0"}
{"type":"measure","subject":"EB-5 minimum investment","measure":"investment threshold","unit":"USD","lo":800000,"hi":1050000,"note":"$800,000 in a targeted employment area or infrastructure project; $1,050,000 standard; $1,400,000 tier proposed","region":"US","grade":"B","src":["S64","S65"],"as_of":"2026-07-02","ttl":"V0"}
{"type":"measure","subject":"International Entrepreneur Rule qualified investment","measure":"threshold","unit":"USD","value":311071,"region":"US","note":"Alternative: $124,429 in government grants; vendor figures","grade":"C","src":["S67"],"as_of":"2026-09-01","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Proclamation 10973 payment (90 FR 46027)","requirement":"$100,000 payment with new H-1B petitions for workers outside the US, cap-subject and cap-exempt","status":"litigated","url":"https://www.presidency.ucsb.edu/documents/proclamation-restriction-entry-certain-nonimmigrant-workers","applies_to":"H-1B","effective":"2025-09-21","note":"Not collected; agency policies vacated or blocked","grade":"B","src":["S1","S22","S61","S62"],"as_of":"2026-11-11","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Proclamation 11069 (91 FR 60497)","requirement":"Extends the payment restriction to 2027-09-21","status":"litigated","url":"https://www.presidency.ucsb.edu/documents/proclamation-11069-restriction-entry-certain-nonimmigrant-workers","applies_to":"H-1B","effective":"2026-09-21","note":"N.D. Cal. relief covers the extension","grade":"B","src":["S4","S21","S22"],"as_of":"2026-11-11","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Fee for Certain H-1B Petitions NPRM (91 FR 54817)","requirement":"$103,265 on all cap-subject petitions","status":"proposed","url":"https://www.govinfo.gov/content/pkg/FR-2026-08-25/html/2026-17324.htm","applies_to":"H-1B cap-subject","effective":null,"note":"Comments closed 2026-09-24","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Weighted Selection final rule (90 FR 60864)","requirement":"Wage-weighted selection among H-1B registrations","status":"in-force","url":"https://www.govinfo.gov/content/pkg/FR-2026-08-25/html/2026-17324.htm","applies_to":"H-1B cap","effective":"2026-02-27","note":"Cited in S1 footnote 24; a D.D.C. suit is reported by a law firm, status not established","grade":"A","src":["S1","S56","S72"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"H-1B Modernization final rule (89 FR 103058)","requirement":"Revised specialty occupation and cap-exempt provisions","status":"in-force","url":"https://www.ahluwalialaw.com/?p=34299","applies_to":"H-1B","effective":"2025-01-17","note":"Effective date from a law-firm page; rule text not opened","grade":"B","src":["S74"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"DOL prevailing-wage NPRM (91 FR 15454)","requirement":"Raise wage levels to the 34th/52nd/70th/88th percentile","status":"proposed","url":"https://www.federalregister.gov/documents/2026/03/27/2026-06017/improving-wage-protections-for-the-temporary-and-permanent-employment-of-certain-foreign-nationals","applies_to":"H-1B, H-1B1, E-3, PERM","effective":null,"note":"Comments closed 2026-05-26","grade":"B","src":["S9","S10"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Eliminating the Discretionary 60-day Grace Period NPRM (91 FR 57807)","requirement":"Remove 8 CFR 214.1(l)(2)","status":"proposed","url":"https://www.govinfo.gov/content/pkg/FR-2026-09-11/html/2026-18631.htm","applies_to":"E-1, E-2, E-3, H-1B, H-1B1, L-1, O-1, TN and dependants","effective":null,"note":"Comments closed 2026-11-10","grade":"B","src":["S2","S25"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Removing Deference to Prior Determinations NPRM (docket USCIS-2026-0529)","requirement":"Delete 8 CFR 214.1(c)(5)","status":"proposed","url":"https://www.regulations.gov/docket/USCIS-2026-0529","applies_to":"I-129 extensions","effective":null,"note":"Comments due 2026-11-13","grade":"B","src":["S22","S32"],"as_of":"2026-11-11","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"USCIS Policy Alert PA-2026-05","requirement":"Officers may deny without RFE or NOID; RFE up to 12 weeks; no extra 14 days for foreign mail","status":"in-force","url":"https://www.envoyglobal.com/wp-content/uploads/2026/08/20260805-EvidentiaryStandards.pdf","applies_to":"All benefit requests","effective":"2026-08-05","note":"Challenge reported; no ruling","grade":"A","src":["S5","S32"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"USCIS memo PM-602-0199","requirement":"Adjustment of status treated as extraordinary discretionary relief","status":"in-force","url":"https://brownimmigrationlaw.com/?p=4462","applies_to":"I-485","effective":"2026-05-21","note":"DHS later said most applicants may still adjust","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Executive Order on H-1B program integrity","requirement":"Interagency coordination and compliance scrutiny","status":"in-force","url":"https://international.caltech.edu/maintainstatus/tracking-immigration-changes","applies_to":"H-1B employers","effective":"2026-09-18","note":"Implementing guidance not seen","grade":"B","src":["S24"],"as_of":"2026-09-22","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"CBP 9-11 Response and Biometric Entry-Exit Fee final rule (91 FR 51360)","requirement":"Covered employers pay the fee on all H-1B and L-1 extensions","status":"in-force","url":"https://www.govinfo.gov/content/pkg/FR-2026-08-25/html/2026-17324.htm","applies_to":"Employers with 50+ staff and over 50% in H-1B or L-1","effective":"2026-09-09","note":"Rule published 2026-08-10; effective date from S32; statutory fee ends 2027-09-30","grade":"A","src":["S1","S32"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Adjustment to Premium Processing Fees (FR 2026-00321)","requirement":"$2,965 for most I-129 and I-140; $1,780 for OPT I-765","status":"in-force","url":"https://policyrisk.com/behind-the-curtain/federal-register/2026-00321","applies_to":"Requests postmarked on or after 2026-03-01","effective":"2026-03-01","note":"Mirror of the Federal Register","grade":"B","src":["S11","S12"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Optional Practical Training Fees NPRM (91 FR 64566)","requirement":"Schools pay $70,000 then $30,000 per OPT recommendation","status":"proposed","url":"https://public-inspection.federalregister.gov/2026-20660.pdf","applies_to":"F-1 OPT and STEM OPT","effective":null,"note":"Effective 60 days after a final rule; comments closed 2026-11-09","grade":"B","src":["S3","S22"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Fixed period of admission final rule (91 FR 44976)","requirement":"Replace duration of status with fixed admission for F, J and I","status":"litigated","url":"https://www.mondaq.com/unitedstates/work-visas/1845774/2026-f-1-and-j-1-rule-change-employer-and-talent-pipeline-impact-report","applies_to":"F-1, J-1, I","effective":"2026-09-15","note":"Effective date postponed 2026-09-14 by D. Mass.","grade":"B","src":["S49"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"EAD automatic-extension removal (90 FR 48799)","requirement":"No automatic extension for renewals filed on or after 2025-10-30","status":"in-force","url":"https://www.f1jobs.io/resources/blog/h4-ead-2026-auto-extension-ended","applies_to":"EAD renewals incl. H-4","effective":"2025-10-30","note":"Challenge filed 2026-01-08 in C.D. Cal.","grade":"C","src":["S48","S74"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"H-4 EAD rule (8 CFR 274a.12(c)(26))","requirement":"EAD for H-4 spouses of H-1B workers with an approved I-140 or an AC21 extension","status":"in-force","url":"https://www.jdsupra.com/topics/h-4-spouses","applies_to":"H-4 spouses","effective":"2015-05-26","note":"Certiorari denied 2025-10-14; effective date recalled","grade":"B","src":["S47","S55","S74"],"as_of":"2025-10-14","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"L-2 and E spouse employment incident to status (USCIS policy, 2021-11)","requirement":"Work authorised with an I-94 carrying the spousal annotation; H-4 spouses excluded","status":"in-force","url":"https://www.fragomen.com/insights/united-states-uscis-issues-further-guidance-on-employment-authorization-for-e-and-l-spouses.html","applies_to":"L-2 and E spouses","effective":"2021-11-12","note":"Effective date from a law-firm summary","grade":"B","src":["S66"],"as_of":"2026-11-13","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Online presence review for H-1B and H-4","requirement":"Public social-media settings; review before visa issue","status":"in-force","url":"https://www.mondaq.com/unitedstates/work-visas/1726436/h1b-h4-visa-appointments-rescheduling-begins-amid-expanded-social-media-vetting-policies","applies_to":"H-1B and H-4 applicants","effective":"2025-12-15","note":"Expanded screening announced 2026-09-18, effective 2026-10-01","grade":"B","src":["S24","S37"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Interview waiver update","requirement":"Most nonimmigrant applicants interviewed in person","status":"in-force","url":"https://international.caltech.edu/maintainstatus/tracking-immigration-changes","applies_to":"Nonimmigrant visa applicants","effective":"2025-09-02","note":"First-time applicants expect an interview","grade":"B","src":["S24","S38"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Visa integrity fee (Public Law 119-21)","requirement":"$250 per nonimmigrant visa issuance, including dependants","status":"enacted","url":"https://www.gtlaw-insidebusinessimmigration.com/?p=10280","applies_to":"Most nonimmigrant visas","effective":"2025-10-01","note":"Collection status contested between S69 and S75","grade":"C","src":["S68","S69","S75"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"75-country immigrant-visa pause","requirement":"Pause on immigrant visa issuance for listed nationalities; India not listed","status":"litigated","url":"https://www.cfr.org/articles/guide-countries-trumps-travel-ban-list","applies_to":"Nationals of 75 listed countries","effective":"2026-01-21","note":"Set aside by a court in August 2026","grade":"B","src":["S39","S40"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Gold Card, EO 14351, Form I-140G","requirement":"$1,000,000 gift routed through EB-1A or EB-2 NIW","status":"litigated","url":"https://clearinghouse.net/case/47793/","applies_to":"Gold Card applicants","effective":"2025-12-10","note":"AAUP v. DHS pending; motion to dismiss on standing","grade":"B","src":["S43","S44"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"EB-5 proposed rule (published 2026-07-02)","requirement":"Codify $1,050,000 and $800,000; add $1,400,000 tier; inflation adjustment from 2027-01-01","status":"proposed","url":"https://eiglaw.com/dhs-proposes-major-overhaul-of-eb-5-program-regulations/","applies_to":"EB-5 investors","effective":null,"note":"Comments closed 2026-08-31; regional centre authority to 2027-09-30","grade":"B","src":["S64","S65","S76"],"as_of":"2026-11-13","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"International Entrepreneur Rule (8 CFR 212.19)","requirement":"Parole for qualifying start-up founders","status":"in-force","url":"https://headmanlaw.com/insights/international-entrepreneur-rule-ier-parole-2026/","applies_to":"Start-up founders","effective":null,"note":"Operating per vendor pages; no rescission found; regulation citation recalled","grade":"C","src":["S63","S67"],"as_of":"2026-09-01","ttl":"V0"}
{"type":"rule","jurisdiction":"US","instrument":"Naturalisation civics test (2025 version)","requirement":"N-400 filed on or after 2025-10-20 takes the 2025 civics test; five-year permanent residence rule (three if married to a citizen)","status":"in-force","url":"https://dewittllp.com/news/2025/10/03/changes-in-the-u.s.-naturalization-process-for-permanent-residents-applying-for-u.s.-citizenship","applies_to":"Naturalisation applicants","effective":"2025-10-20","note":"Fee NPRM 91 FR 37500 (2026-06-23) proposed","grade":"B","src":["S73","S1"],"as_of":"2025-10-03","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Schedule A (20 CFR 656)","requirement":"Pre-certified: nurses, physical therapists, exceptional-ability workers","status":"in-force","url":"https://www.fragomen.com/insights/beyond-perm-leveraging-schedule-a-group-ii-for-exceptional-ability-in-the-sciences-arts-and-performing-arts.html","applies_to":"PERM","effective":null,"note":"No AI or ML occupation","grade":"B","src":["S50"],"as_of":"2025-10-08","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"Premium-processing timeframe amendment (RIN 1615-AD25)","requirement":"Text unpublished","status":"pending","url":"https://www.f1jobs.io/resources/blog/eb2-niw-for-ai-machine-learning-engineers","applies_to":"Premium processing","effective":null,"note":"OIRA review since 2026-10-13","grade":"C","src":["S59"],"as_of":"2026-11-01","ttl":"V0"}
{"type":"absence","item":"Official USCIS HTML and State Department pages","searched":"web_fetch on uscis.gov/forms/..., travel.state.gov bulletin HTML and PDF","note":"Bot detection; used Federal Register, DOL, AAO and summaries","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Official FY2027 H-1B registration chart by wage level","searched":"USCIS registration page via search; media and law-firm summaries","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Standard processing time for H-1B I-129 and employment-based I-485","searched":"Search results and secondary summaries","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"O-1A-only approval statistics","searched":"USCIS data summaries from S31 and S32","note":"USCIS publishes one O line","grade":"E","src":["S31","S32"],"as_of":"2026-11-13"}
{"type":"absence","item":"US job-seeker, points-based or digital-nomad visa","searched":"Route lists in sources read","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Bilateral or special scheme for Indian nationals","searched":"US-India searches across consular, DHS and law-firm sources","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Official sources for International Entrepreneur Rule and EB-5 (USCIS and Federal Register pages)","searched":"Law-firm and vendor pages only; official pages not opened","grade":"E","src":["S63","S64","S65"],"as_of":"2026-11-13"}
{"type":"absence","item":"Official police-certificate and attestation rules for Indian applicants","searched":"Vendor guide only","note":"Vendor claim that every H-1B consular applicant needs a certificate is uncorroborated","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"GenAI-specific sponsorship statistics","searched":"USCIS and DOL summaries; LCA files not queried","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Independent audit of provider approval rates","searched":"Searches on WeGreened, Beyond Border and Manifest claims","grade":"E","src":["S41","S42"],"as_of":"2026-11-13"}
{"type":"absence","item":"Spouse work rights for O-3, F-2 and J-2","searched":"Not verified; recalled only","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"absence","item":"Official pages for the visa integrity fee and MRV fee","searched":"Vendor and law-firm pages only; sources conflict on collection status and MRV effective date","grade":"E","src":["S68","S69","S70","S75"],"as_of":"2026-11-13"}
{"type":"absence","item":"Date, case name and status of the suit against weighted selection","searched":"One law-firm page found; no docket located","grade":"E","src":["S72"],"as_of":"2026-11-13"}
{"type":"absence","item":"Whether H-1B1 is covered by the $100,000 payment","searched":"Law-firm guidance summaries disagree","grade":"E","src":["S61","S62"],"as_of":"2026-11-13"}
{"type":"absence","item":"H-1B cap-gap details","searched":"Regulation existence only (S1 footnote 31)","grade":"E","src":["S1"],"as_of":"2026-11-13"}
{"type":"absence","item":"December 2026 Visa Bulletin","searched":"Searches on 2026-11-13 found forecasts only","grade":"E","src":[],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K1","verdict":"confirmed","finding":"No degree, PhD or citation prerequisite; major award or 3 of 8 criteria; totality step enforced more tightly","suggested":"Add the totality step and the 2026 enforcement trend","grade":"B","src":["S8","S30"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K2","verdict":"confirmed","finding":"$2,965 from 2026-03-01; 15 business days is a service standard that restarts after an RFE","suggested":"Note 45 business days for NIW and EB-1C","grade":"B","src":["S11","S12"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K3","verdict":"confirmed","finding":"O line 91.0% for FY2026 Q1-Q3 and Q3 alone; RFE 24.2% cumulative, 23.0-23.7% monthly in Q3","suggested":"State the cumulative RFE rate","grade":"B","src":["S31","S32"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K4","verdict":"updated","finding":"October figures correct; November 2026 bulletin moved EB-3 India to 2014-01-22","suggested":"Replace with November 2026 and add Dates for Filing","grade":"B","src":["S14","S16"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K5","verdict":"updated","finding":"Agency policies vacated or blocked, not the proclamation; D.D.C. upheld; three appeals pending; $103,265 still proposed","suggested":"Reword 'struck down' and add the appeal status","grade":"B","src":["S1","S4","S22"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K6","verdict":"confirmed","finding":"Claims are self-reported and cohort-selected; no independent audit","suggested":"Keep use-with-care","grade":"C","src":["S41","S42"],"as_of":"2026-11-13"}
{"type":"repo_delta","k":"K7","verdict":"confirmed","finding":"Official sources remain primary; uscis.gov HTML and travel.state.gov block automated checks","suggested":"Note the access limit in D-007","grade":"B","src":["S1","S6"],"as_of":"2026-11-13"}
```
