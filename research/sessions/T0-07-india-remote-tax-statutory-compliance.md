---
id: T0-07
title: "India-based software/AI engineers paid directly by US/EU/UK clients: optimal legal, statutory and tax structure (position as at 21 October 2026)"
date: 2026-10-21
status: complete-with-gaps
topic: india-remote-engineer-tax-statutory-compliance
tags:
  - india
  - income-tax-act-2025
  - section-58-presumptive
  - section-44ada
  - gst-export-of-services
  - lut-rfd-11
  - fema-2026-export-regulations
  - edf-edpms
  - firc-fira-ebrc
  - purpose-code-p0802
  - w-8ben
  - employer-of-record
  - deel-remote-oyster
  - llp
  - private-limited
  - advance-tax
  - msa-ip-assignment
informs_decisions:
  - entity-structure-choice (sole proprietorship under presumptive tax vs LLP vs Pvt Ltd vs EOR)
  - billing-ceiling-management-around-INR-75-lakh
  - gst-registration-and-annual-lut-routine
  - cross-border-payment-rail-and-fintech-selection
  - us-eu-uk-client-onboarding-documents (W-8BEN, invoices)
  - msa-ip-assignment-indemnity-and-misclassification-drafting
confidence: 0.62
confidence_note: "High on statutory mechanics where official text was seen (ITD, IRS, RBI, GSTN); medium on the 1 Oct 2026 FEMA regime (secondary sources only, primary RBI text not fetched); medium-low on take-home figures, which depend on stated cost assumptions (sensitivities provided)."
---

# T0-07 — India remote-engineer tax, statutory and payments structure (as at 21 Oct 2026)

> **Not professional advice.** This is a research synthesis by an AI assistant, not a Chartered Accountant, lawyer or financial adviser. It supplies facts, grades the evidence and models outcomes so you can decide; confirm anything you act on with a practising CA (income tax / GST / FEMA) and, for the MSA and US forms, a lawyer or US tax adviser.

**Evidence grades used throughout**

| Grade | Meaning |
|---|---|
| **A** | Official issuer text (IRS, Income Tax Department, RBI, GSTN) seen directly, canonical URL recorded |
| **B** | Two or more independent professional/secondary sources agree, or a Big-4 alert; primary text not fetched |
| **C** | Single secondary source, or vendor-sourced (commercial interest, may conflict with other vendors) |
| **D** | Recalled from model memory, or my own inference; **not verified** in this session |
| **M** | Model output (my Python calculation) — inherits the weakest grade among its inputs |

Bracketed tags like **[E17]** point to the Sources & Evidence Ledger at the end.

---

## 1. Prior (what I believed before searching — five checkable propositions)

| # | Proposition (recalled, not evidence) | Pre-search confidence | How it was tested |
|---|---|---|---|
| P1 | The Income-tax Act, 2025 replaces the 1961 Act from 1 Apr 2026, so the brief's premise ("Income Tax Act 1961, FY 2026-27 provisions") is outdated and §44ADA has a new section number | Medium | Searched commencement + section mapping; fetched ICAI NIRC deck |
| P2 | §44ADA: ₹75 lakh ceiling if cash receipts ≤5%, otherwise ₹50 lakh; 50% deemed profit; LLPs and companies excluded | High | ITD ITR-4 FAQ; practitioner sources |
| P3 | Software/IT work is an eligible "profession" because IT sits in **Rule 6F**, and ITAT rulings uphold it | Low–medium | Searched notification text; searched ITAT/HC rulings |
| P4 | FEMA: export proceeds must be realised within 9 months; SOFTEX is the declaration for software exports; **P0802** = software consultancy and **P0803** = hardware consultancy | Medium (P0803 weakest) | RBI purpose-code list; FEMA 2026 regulations |
| P5 | A Pvt Ltd overtakes §44ADA around the ₹75 lakh ceiling; EOR costs roughly $599/month; USD/INR is around ₹88–90 | Medium–low | Built a model; priced EOR vendors; checked FX |

Outcome of these tests is in the **Delta** table (section 8). Short version: P1 confirmed, P2 confirmed (with a nuance on the cash test), P3 half wrong (not Rule 6F; no ITAT ruling found), P4 outdated and half wrong, P5 contradicted on two of three counts (the Pvt Ltd crossover and the FX rate) and refined on the EOR price.

---

## 2. Research Question

**Under the law and regulatory practice in force on 21 October 2026, which structure — sole proprietorship under presumptive taxation, LLP / Pvt Ltd, or an Employer of Record — maximises net take-home and minimises legal risk for an India-resident software/AI engineer billing ₹30L / ₹50L / ₹75L / ₹1.2Cr a year to US/EU/UK entities, and what exact compliance stack (GST/LUT, FEMA/banking, W-8BEN, advance tax, MSA) goes with each?**

Sub-questions (mapped to the brief's domain probes): Q1 profession eligibility and the 95%/5% test; Q2 zero-rated export prerequisites and the RFD-11 procedure; Q3 FIRC/FIRA/purpose-code/EDPMS mapping; Q4 where a Pvt Ltd becomes mathematically superior; Q5 EOR fee drag; Q6 MSA clauses for misclassification, IP and indemnity.

**Scope notes.** In scope: Income-tax law for FY/Tax Year 2026-27, CGST/IGST, RBI/FEMA. Out of scope: evasion, undisclosed offshore accounts. State-level items (professional tax, shops-and-establishments, Udyam) were not researched.

---

## 3. Key Findings (12, each with an evidence grade)

**KF1 — The statute changed under the brief's feet. [Grade B]**
The Income-tax Act, 2025 replaced the 1961 Act from 1 April 2026; FY 2026-27 is "Tax Year 2026-27". Presumptive taxation (old 44AD/44ADA/44AE) is consolidated in **s.58**; tax audit (old 44AB) is **s.63**; advance tax is **ss.404/408**; the employer-NPS deduction (old 80CCD(2)) is **s.124(2)**; and "information technology" is named among specified professions in **s.62(4)**. The substance of §44ADA carried over, but section numbers, forms and the Income-tax Rules 2026 differ. *Caveat:* I did not fetch the Act's own text, and sub-section numbering is inconsistent across commentaries (some cite "58(2) or 61(2)"). [E01, E02, E05, E07, E08]

**KF2 — §44ADA eligibility holds; the legal test is "cash ≤ 5%", not "95% digital". [A for limits; B for IT status]**
The Income Tax Department's own ITR-4 FAQ states: resident individual or partnership firm other than an LLP; ceiling ₹50 lakh, raised to ₹75 lakh where cash receipts do not exceed 5% of total gross receipts; deemed profit 50% [E03]. Companies and LLPs are out. The IT profession was notified for s.44AA(1) by **S.O. 385(E) dated 4 May 2001** — *not* via Rule 6F as I had recalled — and is now written into s.62(4) [E04, E05]. No ITAT/High Court ruling for or against IT freelancers was found. §44AD (6%/8% of turnover) is not a workaround for notified professions, and misfiling it draws notices [E06].

**KF3 — The ₹75 lakh line is a cliff, not a slope. [M; inputs B]**
At exactly ₹75L a sole proprietor pays ₹7.33L tax and keeps ₹62.77L. One rupee more and presumptive taxation is lost: tax becomes ₹19.1L (actual books + tax audit), net ₹50.55L — about **₹11.8L of extra tax for ₹1 of extra billing**. To merely match the ₹75L/44ADA take-home you must bill roughly ₹94.0L (sole-prop books), ₹92.4L (LLP), ₹93.9L (Pvt Ltd, full extraction) or ₹98.4L (EOR). Declaring below 50% deemed profit while above the basic exemption triggers a tax audit, and the professional audit threshold is ₹50 lakh [E07].

**KF4 — Up to ₹75L, §44ADA beats every alternative; Pvt Ltd offers no tax edge unless profits stay in the company. [M]**
Take-home under 44ADA is 83–84% of billing versus 67–73% under actual-books structures. The driver is the 50% deemed deduction against realistic costs of about ₹4–5L (44ADA only loses if true costs approach half of receipts). A Pvt Ltd that extracts everything ends up level with sole-prop books (and pays ~₹35k more compliance); retained profits face a second layer (~35.9% at top slab if later paid as dividends). An LLP beats sole-prop books by ₹1.7–2.9L from roughly ₹55L upward, but that result depends on a partner-remuneration cap I recalled and could not verify in the 2025 Act **[D]**, and on a genuine second partner.

**KF5 — EOR costs a 22–24% take-home haircut versus 44ADA at ≤₹75L and is near parity at ₹1.2Cr. [A for Remote's price; B for Deel; M]**
List prices: Deel $599/month; Remote $599/month paid annually or $699 monthly; Oyster about $699 [E31]. At ₹96/$ that is ₹6.9L a year — 23.0% / 13.8% / 9.2% / 5.8% of client spend at ₹30L / 50L / 75L / 1.2Cr — plus ~1% FX margin and a ~2.4% employer statutory load. EOR cash take-home is ₹19.4L / 32.9L / 47.9L / 75.0L. To match 44ADA the client would need to budget **+27% / +32% / +31%** more; at ₹1.2Cr the gap to sole-prop books is only ~4%. EOR's value is non-tax (statutory benefits, no GST/EDF/FIRC burden, lower misclassification and PE exposure for the client).

**KF6 — GST registration is mandatory at all four billing levels; zero-rating rests on an annual LUT and realisation within one year. [B]**
Exports count toward aggregate turnover; the service-provider threshold is ₹20 lakh (₹10 lakh special-category states), so registration is compulsory at ₹30L and above [E15]. The LUT (Form GST RFD-11) is filed per financial year under Rule 96A [E13, E14]. If consideration in convertible foreign exchange is not realised within one year (or an extension granted by the Commissioner), IGST plus interest falls due [E14]. A vendor claim of an automatic "15 months" is **not** supported by the rule text. Finance Act 2026 (assent 30 Mar 2026) omitted IGST s.13(8)(b), so intermediary-type services to overseas recipients can now qualify as exports [E16].

**KF7 — The FEMA export regime reset on 1 October 2026: EDF replaces SOFTEX, and realisation is nine months after a late amendment. [B]**
New Export/Import of Goods and Services Regulations took effect 1 Oct 2026 [E17]. For services, an Export Declaration Form (EDF) goes to the AD bank within 30 days of the end of the month of the invoice (one EDF per month can cover all service invoices); banks load data to EDPMS within five working days; invoices up to ₹10 lakh can be closed on a declaration [E17]. One CA source reports SOFTEX as withdrawn [E18; single source, grade C]. Sources disagreed on the realisation period (15/18 months in the January text vs 9/12); the timeline reconciles because a **22 Sept 2026 amendment** reset it to **9 months (12 for INR)** before commencement [E19]. *Primary RBI text not fetched.*

**KF8 — Purpose code and proof of receipt. [A for codes; C for platform claims]**
RBI's list: **P0802** software consultancy/implementation; **P0803** database/data-processing charges; P0801 hardware consultancy; P1006 business and management consultancy [E20]. For AI/ML engineering P0802 is the natural code; pure data-processing/labelling may fit P0803; advisory work P1006. Proof of receipt: e-FIRC from an AD bank, FIRA from many fintechs, eBRC from DGFT. Bank/fintech fees and PA-CB authorisation status come from competing vendors and conflict [E22–E24]. EEFC accounts allow 100% of export earnings to be credited [E21].

**KF9 — US side: no withholding on work performed in India; the W-8BEN is a status document. [A]**
US withholding bites on US-source income; compensation for services performed outside the US is foreign-source [E26]. A W-8BEN runs from signing to the end of the third following calendar year and must be replaced within 30 days of a change in circumstances; PAN serves as the foreign TIN; Line 10 is only for conditional treaty claims [E25]. Individuals use W-8BEN, entities W-8BEN-E [E25, E28]. An Indian LLP whose members all have limited liability is, by default, a **corporation** for US tax (Treas. Reg. §301.7701-3(b)(2)) — contradicting vendor guides that say "partnership" [E27, E29]. Confirm with US tax counsel before an LLP signs a W-8.

**KF10 — Advance tax and return plumbing. [B; A for the ITR-4 limit]**
Presumptive taxpayers pay 100% of advance tax in one instalment by 15 March (s.408(2), formerly 211(1)(b)); others pay 15/45/75/100% by 15 Jun/15 Sep/15 Dec/15 Mar [E08]. ITD guidance shows ITR-1/ITR-4 carry no Schedule FA/FSI/TR, so anyone with foreign assets or a foreign-tax-credit claim must use ITR-3 [E34]. The new regime is default; for 44ADA incomes the old regime only wins with deductions of ≥₹5.4L (₹30L billing) to ≥₹7.75L (₹50–75L) (model) [M].

**KF11 — IP ownership is the sleeper risk in the MSA. [B]**
Under Copyright Act s.17 a contractor (contract *for* services) is first owner of the code. Under s.19, an assignment must state the rights, duration and territory; if silent, it defaults to five years and India only. The Delhi High Court division bench applied exactly this in *Pine Labs v Gemalto* (2011) [E33]. Employment under an EOR flips the default to the employer (s.17(c)) absent a contrary agreement.

**KF12 — Labour Codes raise the cost floor of employment (EOR). [B/C]**
The four Labour Codes took effect 21 Nov 2025; the "50% wages" rule enlarges PF/gratuity bases and fixed-term employees get gratuity after one year [E32]. My model only uses a PF-ceiling and gratuity-accrual assumption, so EOR employer load may be understated if a vendor contributes PF on full wages.

---
## 4. Recommendation (provisional decision rule — validate with a CA before acting)

**Headline.** For an individual billing foreign clients directly, **up to ₹75L with cash receipts ≤5%: operate as a sole proprietor under presumptive taxation (s.58 / old §44ADA) in the new regime, with GST registration and an annual LUT, bank-channel receipts, monthly EDF, a W-8BEN, and an IP-explicit MSA.** On the model this keeps roughly 83–84% of billing against 64–73% under every alternative. Nothing in the research makes a company, LLP or EOR *mathematically* better below the ceiling.

| Expected annual billing | Provisional structure | Why (model + findings) | Main watch-outs |
|---|---|---|---|
| **≤ ₹75L**, cash ≤5% | Sole proprietor, s.58 presumptive, new regime | 83–84% take-home; no tax audit; single advance-tax instalment (KF2, KF4, KF10) | Hard ceiling; cash test; GST + LUT + EDF still apply; ITR-3 (not ITR-4) if foreign assets or FTC; work must genuinely fit the IT / technical-consultancy profession |
| **₹50–75L but cash receipts >5%** | Do not claim presumptive treatment (ceiling falls to ₹50L) | Statutory ceiling (KF2) | Domestic cash receipts count toward the 5%; foreign bank credits normally do not |
| **₹75L to roughly ₹92–98L** (the "dead zone") | Decide deliberately between (a) lawfully staying at or below ₹75L and (b) accepting actual-books taxation | You need ≈₹92–98L to match ₹75L take-home (KF3) | Receipt-timing, scope-splitting or family-splitting arrangements invite scrutiny; I did not research GAAR/sham-arrangement exposure — get a written CA opinion first |
| **≥ ₹1Cr** | LLP with a genuine second partner (slightly lower tax); or salaried Pvt Ltd with employer NPS if you value locked retirement savings; or Pvt Ltd retain-and-reinvest if you are building a company | Cash outcomes sit within ~₹3–10L of each other at ₹1.2Cr; the ordering turns on a recalled remuneration cap **[D]**, employer NPS (locked), and retention | LLP W-8 classification; ₹0.9–1.2L compliance; second-layer tax when retained profit is extracted |
| **Any level**, if the client mandates employment or you want statutory benefits | EOR | Fixed fee ≈₹6.9L; salary taxation (KF5) | Negotiate a budget uplift of about +27–32% at ≤₹75L to match 44ADA take-home (≈+4% at ₹1.2Cr) |

### Default compliance stack for the recommended path

1. **GST:** register once aggregate turnover (exports included) passes ₹20L; furnish the **LUT for each financial year before the first export of that year** (steps in D4).
2. **Receiving rail:** an AD-bank account (SBI/HDFC/ICICI) or an RBI-authorised cross-border provider; ask for an **e-FIRC/FIRA** quoting **P0802** per remittance or per month; avoid parking proceeds in an unrepatriated foreign balance (FEMA and Schedule FA exposure — D5).
3. **EDF:** from October 2026 an EDF per month through your AD bank/platform; the first one (October invoices) is due by **30 Nov 2026**; realise each invoice within **9 months**.
4. **Invoice** as a zero-rated export under LUT, quote the LUT ARN; add a reverse-charge note for EU/UK business customers (D4, D6).
5. **W-8BEN** to US clients (PAN as foreign TIN); re-issue every three years or within 30 days of a change.
6. **Books and reconciliation:** keep invoices, contract, bank advice, e-FIRC/FIRA, EDF acknowledgements, LUT ARN; make GST turnover, ITR gross receipts and bank credits tell the same story (AIS/TIS cross-checks).
7. **Advance tax:** one instalment by 15 March 2027 if presumptive; otherwise four instalments. File ITR-4, or ITR-3 if you hold foreign assets or claim a foreign tax credit.
8. **MSA:** explicit perpetual, worldwide assignment; independent-contractor substance; capped indemnities (D8).

### What would change this recommendation

- Primary text of s.58 / s.62 differs from the commentary I relied on, or an ITAT/High Court ruling excludes software development from the profession list (none found either way).
- RBI's operational circulars on EDF for individuals impose a burden that makes a platform/EOR route more attractive.
- Your deductions under the old regime exceed ≈₹5.4L–₹7.75L (rare at these incomes; model).
- You hold foreign assets or expect foreign withholding (moves you to ITR-3; not a structure change).
- You intend to scale into an agency (people, assets, investors, exit): non-tax factors then dominate and the Pvt Ltd case strengthens.
- A client's vendor policy refuses individual contractors (some require a company or an EOR).

---

## 5. Alternatives Considered

| # | Alternative | Verdict | Reason | Evidence |
|---|---|---|---|---|
| 1 | Sole proprietor, **actual books + tax audit** | Rejected ≤₹75L; the default above ₹75L | Loses the 50% deemed deduction; audit cost | M, E07 |
| 2 | **LLP** (2 partners) | Conditional above ~₹55L | ₹1.7–2.9L better than sole-prop books *only if* the recalled remuneration cap holds **[D]**; worse than sole-prop books at every level if no remuneration is deductible; 44ADA unavailable to LLPs; W-8 classification friction; LLP audit once turnover >₹40L | M, E03, E11, E12, E27 |
| 3 | **Pvt Ltd, extract everything** | Rejected | Equal to sole-prop books (≈₹0.03L difference at ₹75L) with higher compliance | M |
| 4 | **Pvt Ltd, retain and reinvest** | Conditional | Face-value wealth (cash + retained) beats sole-prop books from ~₹17L, and beats the ₹75L/44ADA outcome from ~₹85L, but only ₹12.75L is cash in hand (zero-tax salary band) and later extraction at top-slab dividend rates (~35.9%) erases the lead | M, E09, E11 |
| 5 | **EOR** (Deel / Remote / Oyster) | Conditional | 22–24% lower cash than 44ADA at ≤₹75L; value is employment protection and client-side risk transfer | E31, M |
| 6 | **Contractor-management / payment platforms** (Deel Contractor, Remote contractor tools) | Tax-neutral overlay | Does not change your tax position; check who the contractual counterparty is (GST export status depends on the recipient being outside India); I found no authoritative source on the Contractor-of-Record flow | E38 (C) |
| 7 | **Non-LLP partnership firm** under presumptive tax | Not researched in depth | ITD FAQ says such firms are eligible; each firm has its own ceiling; deductibility of partner remuneration inside the presumptive profit not verified | E03 |
| 8 | **§44AD** (6%/8% of turnover) | Not available | Specified professions are routed to 44ADA; misfiling draws notices | E06 (B) |
| 9 | **Old tax regime** | Rejected at these incomes | Needs deductions ≥₹5.4L (₹30L billing) to ≥₹7.75L (₹50–75L) | M |
| 10 | **Splitting receipts across years or family members** | Not modelled; flagged | Possible lawful planning when genuine, but legal exposure unresearched | — |

---
## 6. Detailed Findings

### D1. Statutory frame: old-to-new map (Income-tax Act 1961 → Income-tax Act 2025)

FY 2025-26 returns (assessment year 2026-27) are still governed by the 1961 Act and are being filed now. **FY 2026-27 is the first year under the 2025 Act** (returns in 2027, "Tax Year 2026-27"). Notifications and circulars under the old Act were reported as continuing to apply unless inconsistent [E01].

| Topic | 1961 Act | 2025 Act | Grade |
|---|---|---|---|
| Presumptive taxation (business and professions) | 44AD, 44ADA, 44AE | **s.58** (some commentary also cites 61(2) — numbering unresolved) | B |
| Specified-profession list | 44AA(1) + notifications (IT: S.O. 385(E), 4 May 2001) | **s.62(4)**, "information technology" named | B/C |
| Tax audit | 44AB | **s.63** | B |
| Advance tax / presumptive single instalment | 207–211 / 211(1)(b) | **ss.404 / 408(2)** | B/C |
| Employer NPS deduction | 80CCD(2) | **s.124(2)** (14% of basic + DA in the new regime) | C |
| Concessional company regime | 115BAA | **s.200** (reported by calculators; not verified) | C |
| Advance-tax default interest | 234B / 234C | ss.424 / 425 (single source) | C |
| Year concept | Previous year / assessment year | "Tax year" | B |
| Return forms, Form 67 | ITR-3/4, Form 67 | Renumbered under Income-tax Rules 2026 (not verified) | D |

### D2. §44ADA / s.58: eligibility and mechanics (answers Probe 1 and the 95%/5% question)

- **Who:** resident individual, or partnership firm other than an LLP **[A, E03]**. A company or LLP cannot use it, so choosing either structure forfeits the scheme.
- **Profession:** the s.44AA(1) list — legal, medical, engineering, architecture, accountancy, technical consultancy, interior decoration, authorised representative, film artist, company secretary and information technology **[B, E04, E05]**. Software/AI engineering falls under "information technology" (S.O. 385(E) of 2001; now s.62(4)); some practitioners also lean on "technical consultancy". I found no authority that excludes software development.
- **Ceiling:** ₹50 lakh of gross receipts, or ₹75 lakh if cash receipts do not exceed 5% of total gross receipts **[A, E03]**.
- **Deemed profit:** 50% of gross receipts, or a higher figure if declared; no further deductions are allowed on top **[A/B]**. Whether platform fees netted before payout form part of "gross receipts" is not verified **[D]**.
- **The "95% digital" claim in the brief:** correct in substance but framed the other way round in law. The test is *cash ≤5% of gross receipts*; receipts via account-payee cheque/draft or electronic modes through a bank are not cash (practitioner summaries) **[B/C]**. Foreign remittances arrive as bank credits, so cash share is effectively nil for exclusively foreign clients — but I could not confirm that the statute's list of "prescribed electronic modes" expressly names SWIFT/TT credits; that is an inference **[D]**.
- **Enforcement:** I found no CBDT circular or statistics on how strictly the 5% test is policed. The practical controls visible in the research are the receipts-by-mode disclosure in the return, AIS/TIS matching, and GST-turnover matching (an ITR-4 form excerpt asks for GST-return turnover **[C]**). Consequence of failing the test between ₹50L and ₹75L: the presumptive claim is unavailable and actual-books/audit rules apply (inference) **[D]**.
- **Opting out:** declaring less than 50% while income exceeds the basic exemption limit triggers books and a tax audit (old 44AB(d), now s.63); the general professional audit threshold is ₹50 lakh **[B, E07]**. One calculator site claims the 2025 Act now forces an audit for businesses declaring below the deemed rate even if they never opted in; that concerns the business scheme and is a single weak source **[C]**.
- **Return form:** ITR-4 (Sugam) is the presumptive-income return, but the ITD's own guidance shows ITR-1/ITR-4 contain no Schedule FA/FSI/TR; with foreign assets or a foreign-tax-credit claim you need **ITR-3** (presumptive income can still be declared there) **[A, E34]**.
- **ITAT/High Court rulings and classification codes:** searched for rulings on IT freelancers and §44ADA and on the "profession of information technology" notification; **nothing authoritative found**. Practitioner lists show ITR-4 profession codes for software development and other software consultancy **[C]**; confirm against the current return schema.
- **Failure modes seen:** filing under §44AD instead of §44ADA draws notices **[B, E06]**; GST turnover, bank credits and ITR gross receipts failing to reconcile; crossing ₹75L unnoticed in a year with a lumpy receipt.

### D3. Take-home model (answers Probes 4 and 5; all figures **M**, E39)

**Question asked:** if the client's all-in annual spend is ₹30L / ₹50L / ₹75L / ₹1.2Cr, how much cash does the engineer keep after tax, compliance, platform/FX costs and (for EOR) the EOR fee?

**Assumptions** (everything not marked with an evidence tag is mine and should be replaced with your numbers):

| Parameter | Value | Basis |
|---|---|---|
| Taxpayer | Resident individual < 60, TY 2026-27, **new regime** (default) | E10 |
| Slabs | 0–4L nil; 4–8L 5%; 8–12L 10%; 12–16L 15%; 16–20L 20%; 20–24L 25%; >24L 30% | E10 (C; unchanged for FY 2026-27 per multiple explainers) |
| Rebate / standard deduction | 87A rebate for income ≤₹12L (max ₹60k) with marginal relief; ₹75k standard deduction for salary only | E10 (C) |
| Surcharge | 10% >₹50L; 15% >₹1Cr; 25% >₹2Cr, with marginal relief; surcharge on dividends capped at 15%; cess 4% | **E09 (A)** |
| Company tax | 25.168% (22% + 10% surcharge + 4% cess) | E09, E11 |
| LLP tax | 30% + 12% above ₹1Cr + 4% cess; partner remuneration capped at 90% of first ₹6L of book profit (min ₹3L) + 60% of balance | rate E11 (C); **cap recalled [D]** |
| Own work costs | ₹3L fixed + 1% of receipts (equipment, internet, tools, co-working) | assumption |
| FX/platform cost on direct receipts | 1.0% of receipts (reported range 0.3–2%) | vendor ranges (C) |
| Compliance cost per year | 44ADA ₹40k; sole prop books + audit ₹85k; LLP ₹90k; Pvt Ltd ₹1.2L; EOR employee ₹5k | my estimates **[D]** |
| USD/INR | ₹96 | E35 (≈95.5 on 25 Aug, ≈96.8 on 10 Oct 2026) |
| EOR | $599/month; 1% FX margin; PF at the ₹15,000/month wage ceiling both sides; gratuity accrual 4.81% of wages with wages = 50% of gross; **client supplies the equipment** | E31, E32 |
| Comparison basis | The same all-in client spend under every structure | assumption |

**Result 1 — net cash in hand, ₹ lakh (% of billing)**

| Structure | ₹30L | ₹50L | ₹75L | ₹1.2Cr |
|---|---|---|---|---|
| Sole prop, **s.58 presumptive (44ADA)** | **24.91 (83.0%)** | **42.17 (84.3%)** | **62.77 (83.7%)** | not eligible |
| Sole prop, actual books + tax audit | 21.95 (73.2%) | 35.43 (70.9%) | 50.55 (67.4%) | 77.96 (65.0%) |
| LLP, 2 partners (1 working) | 21.40 (71.3%) | 35.40 (70.8%) | 52.25 (69.7%) | 80.85 (67.4%) |
| Pvt Ltd, all profit extracted (salary-optimised) | 21.94 (73.1%) | 35.42 (70.8%) | 50.58 (67.4%) | 78.00 (65.0%) |
| Pvt Ltd, retain-optimised — **cash in hand** | 12.75 (42.5%) | 12.75 (25.5%) | 12.75 (17.0%) | 12.75 (10.6%) |
| …plus retained after corporate tax (illiquid) | +9.32 | +23.98 | +42.32 | +75.32 |
| EOR — cash take-home | 19.42 (64.7%) | 32.86 (65.7%) | 47.90 (63.9%) | 75.01 (62.5%) |
| EOR — cash + employer-funded PF/gratuity (locked) | 20.38 (67.9%) | 34.29 (68.6%) | 49.91 (66.6%) | 78.06 (65.1%) |
| EOR + employer NPS 14% — cash | 18.67 | 31.88 | 46.62 | 74.35 |
| EOR + employer NPS 14% — cash + locked | 21.05 (70.2%) | 35.96 (71.9%) | 52.83 (70.4%) | 84.39 (70.3%) |
| Pvt Ltd extracted + company NPS 14% — cash / cash + locked | 20.39 / 23.48 | 33.36 / 38.86 | 47.97 / 56.48 | 75.18 / 89.10 |

Employer-NPS is only open to salaried structures (EOR employee, Pvt Ltd director); sole proprietors and LLP partners cannot use it. NPS money is locked until retirement, so "cash + locked" counts it at face value (withdrawal taxation not researched).

**Result 2 — total tax paid, ₹ lakh (% of billing)**

| Structure | ₹30L | ₹50L | ₹75L | ₹1.2Cr |
|---|---|---|---|---|
| 44ADA | 1.09 (3.6%) | 3.43 (6.9%) | 7.33 (9.8%) | — |
| Sole prop books | 3.60 (12.0%) | 9.72 (19.4%) | 19.10 (25.5%) | 35.79 (29.8%) |
| LLP (LLP + partner) | 4.10 (13.7%) | 9.70 (19.4%) | 17.35 (23.1%) | 32.85 (27.4%) |
| Pvt Ltd extracted | 3.26 (10.9%) | 9.38 (18.8%) | 18.72 (25.0%) | 35.40 (29.5%) |
| Pvt Ltd retained | 3.13 (10.4%) | 8.07 (16.1%) | 14.23 (19.0%) | 25.33 (21.1%) |
| EOR (employee tax only) | 2.44 (8.1%) | 8.33 (16.7%) | 17.46 (23.3%) | 33.87 (28.2%) |

**Result 3 — the cliff (sole proprietor, ₹ lakh)**

| Billing | Regime | Tax | Net cash |
|---|---|---|---|
| 75.00 | 44ADA | 7.33 | 62.77 |
| 76.00 | Actual books + audit | 19.44 | 51.19 |
| 80.00 | Actual books | 20.78 | 53.77 |
| 90.00 | Actual books | 24.14 | 60.21 |
| 100.00 | Actual books | 27.51 | 66.64 |
| 120.00 | Actual books | 35.79 | 77.96 |

Extra tax from one rupee more billing across the line: **≈₹11.77L**. Billing needed to recover the ₹62.77L take-home: sole-prop books ₹94.0L; LLP ₹92.4L; Pvt Ltd (all extracted) ₹93.9L; Pvt Ltd (retained, face value) ₹85.5L; EOR ₹98.4L. Above the line, each extra ₹100 billed yields roughly ₹62–67 after tax between ₹80L and ₹2Cr, and about ₹59–60 near ₹3Cr where the 25% surcharge tier applies; the LLP keeps the most (₹63–67) and EOR the least (₹59–63.5).

**Result 4 — EOR fee drag** (fee = $599 × 12 × ₹96 = ₹6.90L)

| Client spend | EOR fee | FX margin | Employer statutory load | Gross salary (share of spend) | Cash vs 44ADA | Client budget needed to match |
|---|---|---|---|---|---|---|
| ₹30L | ₹6.90L (23.0%) | ₹0.23L | ₹0.75L (2.5%) | ₹22.12L (73.7%) | −22.0% | ₹38.0L (+27%) |
| ₹50L | ₹6.90L (13.8%) | ₹0.43L | ₹1.21L (2.4%) | ₹41.46L (82.9%) | −22.1% | ₹66.0L (+32%) |
| ₹75L | ₹6.90L (9.2%) | ₹0.67L | ₹1.79L (2.4%) | ₹65.63L (87.5%) | −23.7% | ₹98.4L (+31%) |
| ₹1.2Cr | ₹6.90L (5.8%) | ₹1.12L | ₹2.84L (2.4%) | ₹109.14L (90.9%) | −3.8% vs sole-prop books (−7.2% vs LLP) | ₹124.8L (+4% vs sole-prop books) |

**Result 5 — Pvt Ltd: where is it "mathematically superior"? (Probe 4)**

| Comparison | Crossover billing | Reading |
|---|---|---|
| Pvt Ltd vs **44ADA** (≤₹75L) | **Never** | Even retained face-value wealth is lower (₹55.07L vs ₹62.77L at ₹75L) |
| Pvt Ltd vs sole-prop actual books, **everything extracted** | **Never** | Identical tax (salary is deductible); the company adds ~₹35k compliance |
| Pvt Ltd (retain, **face value**) vs sole-prop actual books | ≈₹17L | But only ₹12.75L is cash; the rest is locked in the company |
| Pvt Ltd (retain, face value) vs the ₹75L/44ADA outcome | ≈₹85.5L | Requires leaving ₹50L+ in the company indefinitely |
| Same, but retained profit later extracted as dividends (~35.9%) | **Not within the modelled range** | At ₹1.2Cr: ₹61.0L total vs ₹78.0L for sole-prop books |

Exit through a share sale (capital-gains treatment) and buy-back rules were not researched, so a growth company with a realistic exit can still favour a Pvt Ltd; this model measures tax drag only.

**Result 6 — regime choice for 44ADA incomes:** the old regime needs deductions of about **₹5.4L** (₹30L billing) or **₹7.75L** (₹50L and ₹75L) to beat the new regime; typical 80C/80CCD(1B)/80D totals are ~₹2.25–2.5L.

**Result 7 — sensitivities** (net cash, ₹ lakh)

| Scenario | 44ADA @ ₹50L | Sole-prop books @ ₹1.2Cr | EOR @ ₹50L | EOR @ ₹1.2Cr |
|---|---|---|---|---|
| Base | 42.2 | 78.0 | 32.9 | 75.0 |
| Direct FX/platform cost 0.3% / 2.0% | 42.5 / 41.7 | 78.5 / 77.2 | 32.9 | 75.0 |
| Own work costs ₹1.5L / ₹6L fixed | 43.7 / 39.2 | 78.9 / 76.0 | 32.9 | 75.0 |
| EOR employee bears the same work costs | 42.2 | 78.0 | 29.4 | 70.8 |
| EOR fee $699 (Remote monthly / Oyster) | 42.2 | 78.0 | 32.1 | 74.3 |
| USD/INR 90 / 100 | 42.2 | 78.0 | 33.1 / 32.7 | 75.3 / 74.8 |
| EOR FX margin 2% | 42.2 | 78.0 | 32.6 | 74.3 |
| Pvt Ltd compliance ₹2L (Pvt Ltd extracted) | — | 77.5 (Pvt Ltd) vs 78.0 | — | — |

The ranking is stable across these. The only judgement that matters is the top end: at ₹1.2Cr, EOR and the direct structures sit within about ₹1–5L of each other, and counting employer NPS or locked PF/gratuity at face value puts EOR or a salaried Pvt Ltd ahead.

**LLP caveat.** With *zero* deductible partner remuneration the LLP is worse than sole-prop books at every level (net ₹17.5L / 31.0L / 47.9L / 74.0L). The LLP's edge therefore rests on the unverified remuneration cap.

**Model revision note (for honesty).** My first run scaled own costs at 10% of receipts, implying ₹12L of tool spend at ₹1.2Cr. That made EOR look ₹2.1L *ahead* of sole-prop books at the top end. I replaced it with ₹3L fixed + 1% variable, which flips that comparison to EOR ₹3.0L *behind*. The ₹1.2Cr conclusion is therefore the most assumption-sensitive result in this file.

---
### D4. GST: zero-rated export of services, LUT (RFD-11), invoicing (answers Probe 2)

**Prerequisites for zero-rating without paying IGST**

1. **Export of services conditions (IGST s.2(6)), all five together:** supplier in India; recipient outside India; place of supply outside India; consideration received in convertible foreign exchange (or INR where RBI permits); supplier and recipient not merely establishments of one person **[B, E14, E15]**.
2. **Registration:** aggregate turnover includes exports; ₹20 lakh threshold (₹10 lakh special-category states) for service providers; below it, a small-supplier exemption for inter-state services is generally relied on, though practitioners flag interpretive caution **[B/C, E15]**. At ₹30L and above, **registration is mandatory**.
3. **Valid LUT for the financial year** (CGST Rule 96A; Form GST RFD-11) **[B, E13, E14]**. LUT is available to registered persons other than those prosecuted for tax evasion above a notified amount (Notification 37/2017-CT; the amount was not verified here) **[C/D]**.
4. **Realisation:** consideration must arrive within **one year** of the invoice date or any longer period the Commissioner allows; otherwise tax plus interest is payable within 15 days after expiry **[B, E14]**. The interest rate is the s.50 rate (18% p.a., recalled) **[D]**. FEMA's 9-month period (D5) is stricter and runs in parallel.
5. **Invoice endorsement and correct reporting** (below).

**Filing the LUT on the GST portal — procedure (GSTN user manual, as reproduced) [B, E13]**

1. Confirm an active GSTIN and an authorised signatory. Companies and LLPs can only sign with a **DSC**; proprietors may use **EVC (OTP)** or DSC.
2. Log in at gst.gov.in → **Services → User Services → Furnish Letter of Undertaking (LUT)**. Form GST RFD-11 opens.
3. Select **"LUT Applied for Financial Year"** (2026-27 now; 2027-28 before the first export after 1 April 2027).
4. Optionally upload the previous year's LUT with *Choose File*.
5. Tick the declaration check-boxes (GSTN notes three conditions). Older guides also mention witness details; the manual excerpt I saw does not — follow the on-screen form.
6. Preview, then **Sign and File with DSC / EVC** (OTP goes to the registered mobile/e-mail).
7. The portal issues an **ARN** by e-mail and SMS; download the acknowledgement. There is no separate LUT number; the ARN serves as the reference **[C]**.
8. Retrieve later via *Services → User Services → View My Submitted LUTs*; saved drafts sit in *My Saved Applications*.
9. **Renew every financial year, before the first export of that year**; an LUT lapses at year-end **[C]**. Without a valid LUT the supply should be treated as taxable (18% IGST, refundable later) — a cash-flow hit **[C]**.

*Practical gap to check today (21 Oct 2026):* if no LUT was filed for FY 2026-27, file immediately; how invoices raised earlier in the year without a valid LUT are treated is a point to settle with your CA **[D]**.

**Export invoice standard** (Rule 46-style content, partly recalled) **[B/C/D]**

- Supplier name, address, GSTIN; invoice number and date; recipient name, address and **country**; description of service and SAC (IT services sit in the 9983 group — e.g. 998313 IT consulting and support, 998314 IT design and development) **[D]**.
- Value in the invoice currency plus the INR equivalent for GST reporting **[C]**.
- **No IGST charged**, with the endorsement that the supply is meant for export under LUT without payment of integrated tax, and the LUT ARN **[B/C]**. Charging 18% "to be safe" breaks zero-rating and locks up cash **[C, E37]**.
- Reporting: export invoices in GSTR-1 (without payment of tax) and zero-rated outward supply in GSTR-3B, monthly or quarterly under QRMP; GSTR-9 optional up to ₹2Cr; e-invoicing not triggered below ₹5Cr — all recalled **[D]**.
- Bank and FX conversion charges carry 18% GST; as a registered person you can generally claim it as input credit, and zero-rated exporters can claim refunds of unutilised credit **[C, E37]**.

**Finance Act 2026 — IGST s.13(8)(b) omitted (effective 30 Mar 2026)** **[B, E16].** Intermediary services used to have their place of supply fixed at the supplier's location (India), which blocked export treatment. Place of supply is now the recipient's location, so an engineer who is characterised as an "intermediary" to an overseas client can qualify for zero-rating. The definition of "intermediary" is unchanged, and treatment of advances or invoices straddling 30 March 2026 is contested.

*Not researched:* GST on platform/marketplace fees paid to foreign platforms (import-of-service reverse charge), and the exact treatment of GST on EOR-style arrangements (an EOR employee makes no taxable supply).

### D5. FEMA and banking: regime, documents, rails (answers Probe 3)

**The 1 Oct 2026 regime [B, E17, E18, E19]**

- *Chronology as reported by secondary sources* (dates not independently confirmed): a Nov 2025 interim extension of the realisation period to 15 months; new Export/Import of Goods and Services Regulations notified in Jan 2026 (15/18 months, effective 1 Oct 2026); an interim reversion to 9 months in mid-2026; and a **22 Sept 2026 amendment** fixing **9 months (12 months for INR)** from the invoice date when the regulations commenced. The KPMG alert reflects the January text and is superseded on this one point.
- **Services:** an **Export Declaration Form (EDF)** to the AD bank within **30 days from the end of the month** of the invoice; one EDF per month may cover all service invoices; for services other than software, filing on or before the receipt date is an alternative **[B, E17]**. AD banks load the data to EDPMS within five working days; invoices up to **₹10 lakh** can be closed on a simple declaration **[B]**. SOFTEX is reported as withdrawn **[C, single CA source]**.
- **Dates that matter:** EDF for October 2026 invoices is due **30 Nov 2026**; each invoice needs realisation inside 9 months.
- **Gap:** I found **no published SBI/HDFC/ICICI procedure for EDF** (too new). Ask your AD bank or payment platform who files, in what format, and how closure is confirmed.

**Purpose codes (RBI list) [A, E20]**

| Code | RBI description | Use for an engineer |
|---|---|---|
| **P0802** | Software consultancy / implementation | Default for software and ML engineering |
| P0803 | Database, data-processing charges | Data processing / labelling-type services |
| P0801 | Hardware consultancy / implementation | Hardware work only |
| P1006 | Business and management consultancy | Advisory/strategy work |

The P0802 entry in RBI's list still refers to SOFTEX; its wording may have been updated after SOFTEX was withdrawn (not verified). Classifying AI/ML work between P0802 and P0803 is my inference **[D]** — align the code with the invoice description.

**Proof-of-receipt documents**

| Document | What it is | Who issues | Notes |
|---|---|---|---|
| **e-FIRC** | System-generated certificate (banks stopped physical FIRCs for export receipts around 2016) | AD bank, on request | Needed as evidence of realisation, GST refund claims, and income-tax records **[C]** |
| **FIRA** | Foreign Inward Remittance Advice — lighter proof | Many fintechs / partner banks | One guide says some GST officers may not accept FIRA for refunds **[C]**; obtain e-FIRC where a refund is claimed |
| **eBRC** | Electronic Bank Realisation Certificate on DGFT, linked to the inward remittance message | DGFT portal, from bank data | Mostly relevant to incentives; vendors say it is self-certified for services **[C]** |
| **"FIRS"** | Appears in one vendor-compiled bank guide for advance payments/other remittances | Bank-specific | Not an RBI-defined instrument as far as I saw; treated as bank terminology **[C]** |

**How to get an e-FIRC from a bank [C, E23, E24]:** net banking → Trade / Forex → Inward Remittance → *FIRC request* (menu names differ); attach the invoice, agreement or purpose declaration, PAN and the credit advice; pay the fee; allow roughly 4–7 business days (SBI reported slower). Fee and FX-markup figures from compilers **conflict** (HDFC FIRC reported anywhere from ₹200 + GST to ₹1,500; SBI from nil to ₹1,000; FX markups 0.5–3.5%), so ask each bank for its published schedule **[C/D]**.

**Fintech rails**

| Provider | What the research supports | Grade |
|---|---|---|
| **Payoneer** | Payoneer's investor release reports **in-principle** RBI authorisation for cross-border payment-aggregator activity; FIRA download is described by third parties | A (authorisation fact) / C |
| **Wise Business** | e-FIRC on request is described; sources conflict on its PA-CB status (final vs in-principle vs absent from a January 2026 list) | C |
| **Skydo** | Vendor and third-party lists report final PA-CB authorisation (Jan 2026) and auto-generated FIRA | C |
| **Deel / Remote payouts** | Not researched | — |

**Verify PA-CB status on RBI's own list of authorised payment aggregators** (a page referenced in RBI material); every status above is vendor-reported **[C]**.

**Holding proceeds.** EEFC accounts let you credit **100%** of export earnings and keep them in foreign currency **[A, E21]**. Receiving export proceeds into a foreign-held balance (a virtual USD account abroad) and leaving it there raises a FEMA repatriation question and brings **Schedule FA / ITR-3** into play **[C, inference]**; check the platform's resident-user terms.

### D6. US / EU / UK client onboarding (answers the W-8BEN and invoicing parts of the brief)

**US withholding logic [A, E25, E26].** US withholding applies to US-source fixed or determinable income; compensation for personal services performed *outside* the US is foreign-source, so an India-resident engineer working from India has no US withholding even without a treaty claim. The W-8BEN is the client's evidence of your foreign status.

**Completing Form W-8BEN (Rev. Oct 2021) — individual or sole proprietor [A, E25]**

1. **Part I, Line 1:** your name (match PAN/passport). **Line 2:** country of citizenship — India.
2. **Line 3:** permanent residence address in India (not a PO box or c/o). **Line 4:** mailing address if different.
3. **Line 5 (US TIN):** leave blank if you have no SSN/ITIN. **Line 6a (foreign TIN):** your **PAN**. **Line 8:** date of birth where the payer requires it.
4. **Part II (Lines 9–10):** only if claiming treaty benefits. For services performed in India no US-source income arises, so no rate claim is needed. If a payer insists, Line 10 must state the specific article and conditions; vendor guides split between business profits (Art. 7) and independent personal services (Art. 15), and none gave an authoritative India-specific template **[C]**. Avoid claiming Article 12 (royalties/fees) unless the income genuinely is royalties.
5. **Part III:** sign and date (an e-signature must show it was signed electronically; a typed name alone is not enough) **[A]**.
6. **Give the form to the client, never to the IRS.** It stays valid from signing to the end of the third following calendar year; replace it within 30 days of a change in circumstances **[A]**.
7. State "services performed entirely in India" in the MSA and on invoices to support the foreign-source position.

**Entities.** A Pvt Ltd uses **W-8BEN-E** (chapter 3 status "corporation"; chapter 4 status usually "active NFFE" per vendor guides **[C]**; PAN as FTIN). For an **LLP**, vendor guides say "partnership", but under Treas. Reg. §301.7701-3(b)(2) a foreign entity whose members all have limited liability is by default an *association taxable as a corporation* unless it elects otherwise **[A, E27]** — and the W-8BEN-E form itself directs foreign partnerships elsewhere (W-8IMY) unless claiming treaty benefits **[A, E28]**. Treat LLP documentation as a point for US tax counsel.

**EU / UK invoicing [C, E30].** For B2B services the place of supply is the customer's country, so the customer self-accounts for VAT (EU: Art. 44/196 reverse charge; UK: outside the scope of UK VAT for the supplier, with the customer accounting under its own rules). Practical invoice content: no VAT, both parties' VAT IDs where available, and a short "reverse charge — recipient accountable for VAT" note. On the Indian side the invoice is a zero-rated export under LUT. Country-specific withholding on service fees was **not researched**; if a client withholds anyway, relief is via the India foreign-tax-credit route (Form 67 before the return due date; ITR-3) with a Tax Residency Certificate and Form 10F to reduce withholding at source **[D]**.

---
### D7. EOR models and contractor platforms (answers Probe 5, qualitatively)

**What changes under an EOR.** The EOR's Indian entity becomes your employer; the client directs your work and funds the EOR's invoice (salary + employer contributions + fee). You are taxed as a salaried employee with tax deducted by the EOR, you make no taxable supply (no GST, no LUT), and the FIRC/EDF burden sits with the EOR/client rather than you. The brief's "fee drag" is therefore mostly borne by the client, but it shrinks the pot that funds your salary unless the client raises its budget (Result 4: +27–32% to match 44ADA at ≤₹75L).

| Vendor | Published price | Grade | Notes |
|---|---|---|---|
| **Remote** | EOR **$599/employee/month paid annually, $699 month-to-month**; contractor management $29/month; FX rate shown on invoices | A (vendor page) | Reconciles the $599-vs-$699 conflict seen in aggregators |
| **Deel** | EOR **$599/month** in several independent aggregators; Contractor management ~$49/month and Contractor-of-Record ~$325/month reported | B/C | Deel's own page was not fetched (an aggregator reports it blocks automated access); FX margin reported at roughly 0.6–2% **[C]**; some vendors take a refundable deposit **[C]** |
| **Oyster** | Mostly reported at **$699/month** (a few sources say $599) | C | Not verified on the vendor page |

**Employer-side load.** PF, gratuity and insurance sit on top of salary. The four Labour Codes (in force 21 Nov 2025) enlarge the wage base through the 50% rule and bring gratuity after one year for fixed-term staff **[B/C, E32]**; the model's 2.4% load assumes PF at the ₹15,000/month wage ceiling and may understate an EOR that contributes on full wages.

**Trade-offs beyond tax.** *Gains:* statutory benefits, provident fund and gratuity accrual, leave, employment-law protection, no GST/EDF/FIRC chores, and (for the client) lower misclassification and permanent-establishment exposure. *Costs:* 22–24% lower cash than 44ADA at ≤₹75L; you are an employee, so copyright in work made in the course of employment defaults to the employer (Copyright Act s.17(c)) **[B]**; employment contracts usually restrict outside work; notice periods apply.

**Contractor-management and Contractor-of-Record platforms.** These are payment/compliance overlays and do not change your income-tax position. What matters for GST is **who the contractual recipient of your service is**: zero-rating requires a recipient outside India. I found no authoritative source on the Contractor-of-Record flow or its GST consequences (one third-party page on Deel and GST is single-source) **[C]** — read the counterparty clause before invoicing without GST.

### D8. MSA provisions for misclassification, IP and indemnity (answers Probe 6)

Only the IP row below was verified against sources; the rest is drafting practice from my own knowledge **[D]** and should be reviewed by a lawyer.

| Clause | What to include | Why | Grade |
|---|---|---|---|
| **Status and substance** | Independent contractor; you control methods, hours and place of work; no exclusivity or minimum hours; own equipment; right to substitute or subcontract; deliverables-based fees; no employee benefits; no authority to bind the client | Labels do not decide status — conduct does — so the contract should mirror how work is actually done | D |
| **IP assignment** | Present assignment of all IP in deliverables, **perpetual, worldwide, all media and modes, irrevocable**, with consideration stated; separate licence for your background tools | Without stated duration/territory an assignment defaults to five years and India only; as a contractor you are first owner | **B (E33)** |
| **Moral rights, pre-existing IP** | Non-assertion/acknowledgement language; schedule listing background IP and open-source components | Moral rights under the Copyright Act are personal; enforceability of waivers is uncertain | D |
| **AI-specific** | Ownership of fine-tuned weights, prompts, evaluation sets and outputs; no training of third-party models on client data; training-data provenance warranties; open-source licence compliance | Where AI deliverables are involved, "who owns the weights and data" is the common dispute | D |
| **Fees and payment** | Currency, invoice cadence, 30–45-day terms, payer bears bank/intermediary charges, no set-off, late fees | Keeps realisation well inside the 9-month FEMA limit and protects net receipts | D |
| **Taxes and forms** | Fees exclusive of VAT/GST; you supply W-8BEN and are responsible for Indian taxes; client responsible for its own VAT/withholding; gross-up if withholding is imposed | Allocates tax risk explicitly | D |
| **Indemnity and cap** | Your indemnity limited to third-party IP infringement caused by your deliverables and breach of confidentiality; liability cap at fees paid in the prior 12 months with narrow carve-outs; consequential damages excluded; client indemnifies for its materials, data and instructions | Prevents uncapped exposure disproportionate to fees | D |
| **Insurance** | Professional-indemnity/cyber cover if the client requires it | Cost and availability for individuals vary | D |
| **Confidentiality and data** | Mutual NDA; security obligations; data-protection terms (DPDP Act for Indian personal data; SCCs where GDPR data is handled) | AI work often touches personal data | D (not researched) |
| **Termination and acceptance** | Notice, acceptance tests, payment for work done, survival of IP/confidentiality | Avoids disputes over unpaid work | D |
| **Dispute resolution** | Named governing law, institutional arbitration in a neutral seat, enforceability under the New York Convention (US and UK are parties; recalled) | Cross-border enforcement | D |
| **Restraints** | Resist broad non-competes; keep confidentiality and narrow non-solicit instead (Indian Contract Act s.27 voids post-termination restraints, recalled) | Limits ability to take other clients | D |
| **Client PE protection** | State that you work from your own premises, have no authority to conclude contracts, and are not a dependent agent | Helps the client avoid a permanent-establishment argument | D |

### D9. Tool catalog

| Tool | Category | Use in this workflow | Evidence | Caveats |
|---|---|---|---|---|
| **GST Portal (gst.gov.in)** | Statutory filing | Registration; **LUT / RFD-11**; GSTR-1/3B; refunds | A/B (GSTN manual, E13) | DSC mandatory for companies/LLPs; EVC for proprietors |
| **Income Tax e-filing portal** | Statutory filing | ITR-3/ITR-4; AIS/TIS; advance-tax challans; foreign-tax-credit form | A (existence/limits, E34) | Form numbers changed under the 2025 Act/Rules 2026 (not verified) |
| **DGFT portal** | Export proof | eBRC against inward remittance data | C | Mainly for incentives |
| **RBI list of authorised payment aggregators** | Regulatory check | Verify a fintech's PA-CB status | A (referenced) | I could not retrieve the current list |
| **AD-bank net banking (SBI CINB, HDFC, ICICI)** | Bank | e-FIRC request, EDF handling, FX conversion | C | Fees/TAT conflict across compilers |
| **Wise Business** | Remittance | Receive-and-convert; e-FIRC on request | C | PA-CB status conflicting; check resident-user terms and any foreign-balance holding |
| **Payoneer** | Remittance | Receiving accounts; FIRA | A (in-principle authorisation) / C | Confirm current authorisation status |
| **Skydo** | Remittance / invoicing | India-focused invoicing, FIRA, collection | C (vendor-reported) | Vendor claims only |
| **Deel** | EOR / contractor payments | EOR; contractor management; CoR | B/C | Pricing via aggregators; FX margin reported 0.6–2% |
| **Remote** | EOR / contractor payments | EOR; contractor management | A (price page) | $599 annual vs $699 monthly |
| **Oyster** | EOR | EOR | C | Price conflicts across sources |
| **ClearTax** | Tax filing | Consumer ITR/GST filing platform | D | Appeared as an explainer source only; features not assessed |
| **Winman (CA-ERP / GST / TDS)** | Practitioner software | Desktop suite your CA may use for ITR/GST/TDS | A (vendor self-description, E36) | Practitioner tool; Windows-oriented; not a consumer product |
| Others encountered | Remittance/payments | Xflow, PayGlocal, Razorpay, Cashfree, Playto, Seasaw | C | Vendor content; not assessed |

### D10. Direct answers to the six domain probes

1. **Does software/AI engineering qualify under §44AA/§44ADA, and what do ITAT rulings say?** Yes on the text: "information technology" was notified for s.44AA(1) by S.O. 385(E) (4 May 2001) and is named in s.62(4) of the 2025 Act **[B]**. **No ITAT/High Court ruling on IT freelancers was found** either way; practitioner lists show ITR-4 codes for software development and other software consultancy **[C]**.
2. **Prerequisites for zero-rated export and the RFD-11 steps?** Registration, a valid annual LUT, the five export conditions, realisation inside one year, correct invoice and returns — and the click-path in D4 **[B]**.
3. **Banking documentation for e-FIRC/FIRA with P0802 across SBI/HDFC/ICICI and fintechs?** Request via net banking with invoice, agreement or purpose declaration and PAN; ask the payer or platform to quote **P0802**; expect 4–7 business days at banks; fees and fintech authorisation status are vendor-sourced and conflicting; **no bank-published EDF procedure was found** (D5).
4. **How strictly is the 95%/5% test enforced, and when does a Pvt Ltd win?** The test is statutory (cash ≤5%); no CBDT enforcement circular or statistics were found; practical controls are return disclosures and AIS/GST matching **[D]**. A Pvt Ltd **never** beats 44ADA at ≤₹75L, never beats sole-prop books when profits are extracted, and wins only if profits are retained (face value ≈₹17L vs books; ≈₹85.5L vs the 44ADA outcome), a lead that extraction tax erases (Result 5).
5. **EOR versus 44ADA fee drag?** Fee ₹6.9L fixed = 23.0/13.8/9.2/5.8% of client spend; FX ≈1%; employer load ≈2.4%; EOR cash is 22–24% below 44ADA at ≤₹75L and ~4% below sole-prop books at ₹1.2Cr (Result 4).
6. **MSA provisions?** Status-and-substance, an explicit perpetual-worldwide assignment, capped and narrow indemnities, tax-and-forms allocation, and client-PE protections (D8).

---

## 7. Open Questions & Risks

### 7.1 Open questions (what I could not settle)

1. **Primary text of s.58 / s.62(4) / s.63** of the Income-tax Act 2025 was not fetched; sub-section numbering differs across commentaries (58(2) vs 61(2)). Confirm the exact provision, including how "gross receipts" and the cash test are drafted.
2. **RBI primary text** (the January 2026 regulations and the 22 Sept 2026 amendment) was not fetched; the 9/12-month realisation rule and EDF mechanics rest on secondary sources and a Big-4 alert that predates the amendment.
3. **EDF for individuals:** who files (you, the platform or the bank), through which portal, and what closure confirmation looks like — no bank-published procedure found.
4. **Whether SWIFT/TT credits count as "electronic modes"** in the cash test (inference only).
5. **PA-CB status** of Wise, Payoneer, Skydo and others — vendor-reported and conflicting.
6. **LLP partner-remuneration cap** in the 2025 Act (recalled, drives the LLP result) and the LLP's US classification for W-8 purposes.
7. **GST:** the LUT-ineligibility monetary threshold; treatment of invoices raised before an LUT is filed; GST on foreign-platform fees; small-supplier exemption below ₹20 lakh.
8. **Misclassification** under Indian labour and social-security law for long-term single-client contractors (including gig/aggregator provisions) was not researched in depth; neither was the foreign client's permanent-establishment exposure.
9. **Foreign withholding by EU/UK/other clients** and treaty relief by country.
10. **Exit and extraction taxes** for a Pvt Ltd (share sale, buy-back changes in the 2026 Budget) were not researched.
11. **Cost inputs** (compliance fees, own work costs, FX cost, employer-load assumptions) are my estimates; replace them with quotes.
12. **AI-work classification** between P0802 and P0803 for data-labelling or model-training services.
13. **State-level items** (professional tax, shops-and-establishments, Udyam) were not researched.

### 7.2 Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Crossing ₹75L (or ₹50L if cash >5%) without noticing — tax roughly triples at the line | Medium for fast-growing earners | Very high (≈₹11.8L at the line) | Track cumulative receipts monthly against ₹75L; plan decisions before Q4 |
| Filing under §44AD instead of §44ADA | Medium | Notices, tax recomputation | File under the profession scheme; CA review of business-code and section choice |
| No/lapsed LUT for the financial year | Medium | IGST demand or cash locked in refunds | Calendar the LUT every 1 April; file before the first export |
| Realisation beyond 9 months (FEMA) / one year (GST) | Low–medium (late-paying clients) | IGST + interest; FEMA contravention | Short payment terms; extension request via AD bank before expiry |
| Missing monthly EDF from Oct 2026 | Medium (new regime) | Reporting default flagged in EDPMS | Agree EDF responsibility with bank/platform now; first due 30 Nov 2026 |
| Parking proceeds abroad / foreign balances | Medium | FEMA exposure; ITR-3 and Schedule FA obligations | Repatriate to Indian account or EEFC; disclose foreign assets |
| IP default (5 years/India) in MSA | Medium | Loss or dispute over code ownership | Explicit perpetual-worldwide assignment |
| Misclassification (contractor treated like an employee) | Medium for single-client, full-time work | Reclassification, benefits claims | Substance-over-label drafting; or EOR |
| LLP/W-8 classification error | Medium if LLP used | Withholding or form rejection | US tax adviser sign-off |
| Rapid regulatory change (2025 Act, Rules 2026, FEMA 2026) | High | Outdated advice | Re-verify against primary text before filing |

### 7.3 Strongest objections an expert would raise, and what I found

| # | Objection | What the evidence shows | Net |
|---|---|---|---|
| 1 | "Software development is *business*, not a *profession*; presumptive treatment under 44ADA is vulnerable." | IT was notified as a profession in 2001 and is named in the 2025 Act (B); practitioner lists show 44ADA-compatible codes (C); **no ruling found either way**; misfiling under 44AD draws notices (B). | Moderate residual risk; get a written CA view and keep work documentation |
| 2 | "The 95% digital test is not what the law says, and foreign remittances may not be 'prescribed electronic modes'." | Test is cash ≤5% (A); foreign credits are bank credits (inference, D). | Objection partly right on framing; exposure small for exclusively foreign clients |
| 3 | "Your Pvt Ltd model ignores reinvestment, liability protection, ESOPs, investors and capital-gains exits." | Correct — the model measures tax drag only; exit/buy-back taxation not researched. | Valid; the company route is a business decision, not a tax one |
| 4 | "The EOR comparison is unfair: client budgets differ and EOR salaries include benefits." | I fixed client spend and counted locked benefits separately; parity budgets computed (+27–32%). | Fair as a like-for-like cost test; not proof that clients will fund parity |
| 5 | "FEMA 2026 details are moving and secondary blogs are unreliable." | Sources conflicted until reconciled by the 22 Sept 2026 amendment timeline; primary RBI text not fetched. | Agree — treat KF7 as B-grade and verify with your bank |
| 6 | "GST one-year and FEMA nine-month periods conflict." | They run in parallel; FEMA is stricter (B). | Practical rule: realise within 9 months |
| 7 | "Vendor guides say an LLP is a partnership for US forms." | Treasury regulation points to corporation by default (A); W-8BEN-E instructions route partnerships to W-8IMY (A). | Vendor guidance is doubtful; use US counsel |
| 8 | "Cost assumptions drive the answer." | Sensitivities show stable rankings except at ₹1.2Cr; first-run cost model flipped that comparison. | Agree; use your own costs |
| 9 | "ITR-4 is not usable if you hold foreign assets." | Confirmed by ITD guidance (A). | Use ITR-3 in those cases |

### 7.4 Searched and not found (honest gaps)

- ITAT/High Court rulings on IT/AI freelancers and §44ADA, and on the 2001 IT notification.
- Any CBDT circular or statistic on enforcing the 5% cash test.
- Bank-published (SBI/HDFC/ICICI) e-FIRC and EDF procedures; only vendor-compiled summaries with conflicting fees.
- An authoritative, current RBI PA-CB list confirming Wise, Payoneer and Skydo.
- Primary text of RBI's 22 Sept 2026 amendment and of Income-tax Act 2025 s.58/62.
- The Contractor-of-Record counterparty and GST treatment on Deel.
- A definition of "FIRS" beyond one vendor-compiled bank guide.
- India-specific W-8BEN Line 10 template from a primary source.

### 7.5 Falsification attempts

| Belief tested | Attempt | Result |
|---|---|---|
| IT is eligible under 44ADA | Searched for ITAT denials | None found; eligibility rests on notification + statute |
| LLPs are excluded | Checked the ITD FAQ | Confirmed |
| Realisation period is 15/18 months | Compared post-22-Sept sources | Superseded; 9/12 months |
| Vendor claim of an automatic "15 months" under GST | Read Rule 96A text | Not supported; one year, extendable by the Commissioner |
| P0803 = hardware | Read the RBI list | Wrong; P0803 is database/data processing |
| USD/INR ≈ ₹88–90 | Checked market data | Wrong; ≈₹95–97 |
| LLP is a partnership for US forms | Read the Treasury regulation | Default is corporation |
| A Pvt Ltd beats 44ADA near ₹75L | Built the model | Contradicted |

---

## 8. Delta (belief change table)

| # | Prior belief | What the evidence showed | Direction | Grade of update |
|---|---|---|---|---|
| 1 | Income-tax Act 2025 replaces the 1961 Act from 1 Apr 2026 (brief assumed 1961) | In force from 1 Apr 2026; s.58 / s.62(4) / s.63 / ss.404, 408 | **Confirmed**; brief's premise outdated | B |
| 2 | §44ADA ₹75L with cash ≤5%; 50%; LLP excluded; brief's "95% digital" | ITD FAQ confirms; test is cash ≤5%, "digital" is shorthand | **Confirmed**, nuance added | A |
| 3 | IT listed in Rule 6F | Notified for s.44AA(1) via S.O. 385(E) (4 May 2001); now s.62(4) | **Contradicted** | B |
| 4 | ITAT rulings uphold IT freelancers | None found | **Unsupported** (gap) | — |
| 5 | Realisation 9 months; SOFTEX applies | New regime 1 Oct 2026; SOFTEX withdrawn (single source); EDF monthly; 9/12 months after 22 Sept amendment | **Updated** | B |
| 6 | P0803 = hardware consultancy | P0801 hardware; P0803 database/data processing; P0802 software | **Contradicted** | A |
| 7 | W-8BEN valid 3 years; services outside the US are not US-source | Confirmed by IRS instructions and IRS source rules | **Confirmed** | A |
| 8 | Treaty Article 12/15 needed for 0% US withholding | Not needed for work performed in India; vendor guides diverge on the article | **Updated** | A/C |
| 9 | LLP is a corporation for US purposes by default | Treasury regulation supports; vendor guides say partnership | **Confirmed** against vendors | A |
| 10 | EOR ≈ $599/month | Deel $599; Remote $599 annual / $699 monthly; Oyster ≈ $699 | **Refined** | A/B/C |
| 11 | USD/INR ≈ ₹88–90 | ≈₹95–97 | **Contradicted** | C |
| 12 | Pvt Ltd overtakes 44ADA near the ceiling | Never ≤₹75L; above, only if profits are retained | **Contradicted** | M |
| 13 | §44AD as a possible alternative for IT freelancers | Notified professions go to 44ADA; misfiling draws notices | **Rejected** | B |
| 14 | GST-LUT "15 months" (vendor claim) | Rule 96A says one year, extendable by the Commissioner | **Contradicted** | B |
| 15 | Intermediary status blocks export zero-rating | s.13(8)(b) omitted from 30 Mar 2026 | **Updated** | B |
| 16 | Copyright assignments are simple | Duration/territory defaults (5 years/India) apply when silent | **Confirmed** as a risk | B |

---
## 9. Sources & Evidence Ledger

**"Seen via" key:** **F** = I opened the page; **S** = excerpt seen in a search result (page not opened); **N** = URL/title noted from a search listing and not re-verified at write-up. Grades follow the legend at the top. Research date: 21 Oct 2026; roughly 45 searches and fetches.

| ID | Supports | Source and URL | Seen via | Grade |
|---|---|---|---|---|
| E01 | Income-tax Act 2025 in force; s.58 presumptive; s.63 audit; old notifications continue | ICAI NIRC, *The New Income Tax Act 2025* deck — https://nirc.icai.org/wp-content/uploads/2026/05/The-New-Income-Tax-Act-2025-nanda-sir.pdf | F | B |
| E02 | Commencement 1 Apr 2026 (CBDT communication, reproduced) | TaxGuru, "Income-tax Act 2025 in force from 1 April 2026"; Outlook Money, "New I-T Act marks new chapter…CBDT" — https://www.outlookmoney.com/tax/new-i-t-act-marks-new-chapter-in-indias-tax-administration-step-towards-viksit-bharat-cbdt | S/N | B |
| E03 | 44ADA: resident individual or non-LLP firm; ₹50L/₹75L; cash ≤5%; 50% | Income Tax Department, ITR-4 (Sugam) FAQ — https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq | S | **A** |
| E04 | IT profession notified for s.44AA(1): S.O. 385(E), 4 May 2001 | TaxGuru, *Professionals eligible to opt Section 44ADA* — https://taxguru.in/income-tax/professionals-eligible-opt-section-44ada.html ; TaxTMI notification record — https://www.taxtmi.com/notifications?id=13571 | F/S | B |
| E05 | "Information technology" named in s.62(4); s.58 limits | Buildwright, freelancer guide to the 2025 Act — https://buildwright.co.in/freelancers/insights/freelancer-income-tax-2025-act ; Taxmann, Income-tax Rules 2026 guide — https://www.taxmann.com/post/blog/income-tax-rules-2026-master-guide-with-rule-wise-commentary ; CAalley, presumptive taxation for professionals — https://www.caalley.com/news-updates/indian-news/presumptive-taxation-for-professionals-the-50-rule-remains-but-what-changes-for-deductions-and-losses-under-the-new-tax-act | S | B/C |
| E06 | 44AD vs 44ADA misfiling draws notices | Business Standard explainer (Sep 2025) — https://www.business-standard.com/amp/economy/news/explainer-difference-between-section-44ad-and-section-44ada-of-i-t-act-125091601204_1.html | N | B |
| E07 | Tax audit: professional threshold ₹50L; opt-out below 50% triggers audit; s.63 | TaxGuru — https://taxguru.in/?p=1058959 and https://taxguru.in/?p=1034483 ; Qwikfilings — https://qwikfilings.com/?p=380062 ; CalcGuru — https://calcguru.in/?p=5850 ; Quicko tax-audit applicability tool | S | B/C |
| E08 | Advance tax: ss.404, 408(2); presumptive single instalment 15 March; instalment schedule | TaxGuru — https://taxguru.in/?p=1048485 ; Qwikfilings — https://qwikfilings.com/?p=379987 | N | B/C |
| E09 | Surcharge 10/15/25%; dividend surcharge cap 15%; 115BAA surcharge 10%; marginal relief | Income Tax Department, "What is surcharge and how is it computed" — https://www.incometaxindia.gov.in/w/what-is-surcharge-and-how-it-is-computed- ; ITD tax-rate tables — https://incometaxindia.gov.in/Documents/Left%20Menu/TAX%20RATES_Indvl.htm | S | **A** (pages predate the 2025 Act; carried-over rule assumed) |
| E10 | New-regime slabs unchanged; 87A rebate to ₹12L; ₹75k standard deduction; employer NPS s.124(2) 14% | Value Research — https://www.valueresearchonline.com/stories/229044/employer-nps-deduction-new-tax-regime/ ; CalcGuru — https://calcguru.in/?p=4211 ; several Budget-2026 explainers (not individually ledgered) | S | C |
| E11 | Company 25.168%; LLP 30% + 12% over ₹1Cr; dividends taxed in shareholders' hands | caakhilesh.in corporate-tax calculator; taxgarden.in corporate tax FY 2026-27; virtualauditor.in; taxclue.in | N | C |
| E12 | LLP audit if turnover >₹40L or contribution >₹25L; Forms 8 and 11; company audit mandatory | setindiabiz.com LLP annual compliance; incorpx.io LLP audit limit; patronaccounting.com statutory audit of LLP | N | C |
| E13 | RFD-11 click-path, DSC/EVC, ARN | GSTN user manual as reproduced — https://gstzen.in/a/gst-manuals-user-manuals-filing-of-letter-of-undertaking-form-gst-rfd-11.html ; https://taxguru.in/goods-and-service-tax/how-to-file-letter-of-undertaking-for-export-of-goods-or-services.html ; https://eximpe.com/blog/b2b/how-to-file-lut-in-gst-portal-online | S | B |
| E14 | Rule 96A(1)(b) text; export-of-services conditions; BRC/FIRC circulars | CAclubindia, *Export of services and receipt of consideration under GST* — https://www.caclubindia.com/articles/export-of-services-and-receipt-of-consideration-under-gst-50977.asp ; CA Sunil Kumar, refund clarifications — https://www.ca-sunilkumar.com/clarifications-refund-issues-exports-goods-services/ | N | B |
| E15 | Aggregate turnover includes exports; ₹20L / ₹10L thresholds | TaxGuru, GST for freelancers — https://taxguru.in/goods-and-service-tax/gst-freelancers-consultants-guide-domestic-foreign-clients.html ; TaxTMI forum — https://www.taxtmi.com/forum/issue?id=120746 ; SetIndiaBiz — https://www.setindiabiz.com/?p=15182 | N | B/C |
| E16 | IGST s.13(8)(b) omitted by Finance Act 2026 (assent 30 Mar 2026) | Grant Thornton Bharat — https://www.grantthornton.in/insights/articles/gst-on-intermediary-services/ ; TaxGuru — https://taxguru.in/goods-and-service-tax/intermediary-conundrum-omission-section-13-8-b-igst-act-finance-act-2026.html | S | B |
| E17 | FEMA 2026 regime effective 1 Oct 2026; EDF monthly for services; EDPMS upload; ₹10L small-value closure | KPMG India Flash News on the 2026 Regulations — https://www.in.kpmg.com/taxflashnews/KPMG-Flash-News-Foreign-Exchange-Management-Export-and-Import-of-Goods-and-Services-Regulations-2026.pdf | F | B (predates 22 Sept amendment) |
| E18 | EDF steps for freelancers; SOFTEX withdrawn; first EDF due 30 Nov 2026 | Startup Advisory, *Export of services reporting — RBI EDF, FEMA 2026* — https://www.startupadvisory.in/blog-export-of-services-reporting-rbi-edf-fema-2026.htm | F | C |
| E19 | 22 Sept 2026 amendment: 9 months (12 for INR) realisation from 1 Oct 2026 | taxupdate.in (FEMA export realisation period, 1 Oct 2026) — https://taxupdate.in/finance/983/fema-export-realisation-period-october-1-2026-nine-months-rbi-amendment/ ; lexcomply.com CXO guide — https://www.lexcomply.com/blog/fema-export-of-goods-services-rules-2026-cxo-guide-6ad59ef96d45e ; ymshah.com EDF rules — https://ymshah.com/edf-rules-export-declaration-form-2026/ ; plus corplawupdates, indiabizexperts, TaxGuru | N | B (primary RBI text not fetched) |
| E20 | Purpose codes P0801/P0802/P0803/P1006 | RBI purpose-code annexure — https://website.rbi.org.in/documents/87730/39710850/52220.pdf ; Wise purpose-code guide — https://wise.com/in/blog/purpose-code-for-inward-remittance ; Skydo P0802 page — https://www.skydo.com/rbi-purpose-codes/P0802-software-consultancy-and-implementation | S | **A** (RBI) |
| E21 | EEFC: 100% of export earnings may be credited | RBI EEFC FAQ — https://website.rbi.org.in/documents/d/rbi/exchange-earner-s-foreign-currency-eefc-account ; RBI circular — https://website.rbi.org.in/documents/87730/39016390/APD68120516_A.pdf | S | **A** |
| E22 | PA-CB status: Payoneer in-principle; Skydo/Wise claims conflicting | Payoneer investor release — https://investor.payoneer.com/news-releases/news-release-details/payoneer-receives-principle-authorization-cross-border-payment ; Skydo PA-CB list — https://www.skydo.com/blog/rbi-pa-cb-list ; Winvesta list — https://www.winvesta.in/blog/businesses/19-firms-got-rbis-pa-cb-license-who-won-and-why | S/N | A (Payoneer release) / C (lists) |
| E23 | FIRC vs FIRA vs eBRC; e-FIRC on request | Xflow — https://www.xflowpay.com/blog/brc-vs-firc ; Commenda — https://www.commenda.io/compliance/firc-global-transactions ; Skydo — https://www.skydo.com/blog/fira-vs-ebrc ; Wise — https://wise.com/in/blog/firc-certificate | S | C |
| E24 | Bank procedures/fees/FX markups (conflicting) | Skydo — https://www.skydo.com/blog/bank-charges-for-inward-remittance ; Razorpay — https://razorpay.com/blog/bank-charges-inward-remittance-india/ ; Seasaw — https://seasaw.ai/resources/fira-download/ ; Playto — https://playto.so/blogs/how-to-get-firc-from-hdfc-icici-kotak-and-sbi-for-international-payments-2026 ; Remitbee | S | C/D |
| E25 | W-8BEN validity, FTIN, Line 10, e-signature, 30-day rule | IRS, *Instructions for Form W-8BEN* (reviewed 30 Apr 2026) — https://www.irs.gov/instructions/iw8ben | F | **A** |
| E26 | Services performed outside the US are foreign-source (s.862(a)(3)) | IRS, *Persons employed by a foreign person* — https://www.irs.gov/individuals/international-taxpayers/persons-employed-by-a-foreign-person ; Tax Notes private-letter-ruling excerpt | S | A/B |
| E27 | Foreign eligible entity default classification (all-limited-liability → association) | 26 CFR §301.7701-3 — https://www.law.cornell.edu/cfr/text/26/301.7701-3 ; https://www.govinfo.gov/content/pkg/CFR-2014-title26-vol18/pdf/CFR-2014-title26-vol18-sec301-7701-3.pdf | S | **A** (application to Indian LLP is my inference) |
| E28 | W-8BEN-E form and instructions; partnerships routed to W-8IMY | IRS — https://www.irs.gov/pub/irs-pdf/iw8bene.pdf ; https://www.irs.gov/pub/irs-pdf/fw8bene.pdf | S | **A** |
| E29 | Vendor W-8 guides (Art. 7 vs Art. 15; LLP "partnership") | Xflow — https://www.xflowpay.com/blog/form-w-8-ben-and-w-8-ben-e ; Skydo — https://www.skydo.com/blog/form-w-8ben-e-guide ; Winvesta — https://www.winvesta.in/blog/investors/w-8ben-and-w-8ben-e-form-guide-for-indians-2025-winvesta ; Karbon — https://www.karboncard.com/blog/guide-to-w-8ben-and-w-8ben-e | S | C |
| E30 | EU/UK B2B reverse-charge logic | Solidgate — https://solidgate.com/glossary/reverse-charge/ ; ACCA — https://accaglobal.com/uk/en/technical-activities/uk-tech/in-practice/2022/september/vat-on-supply-of-services-to-customers-outside-uk.html | S | C |
| E31 | EOR prices | Remote pricing page — https://remote.com/en-in/pricing (**A**); Second Talent — https://www.secondtalent.com/resources/employer-of-record-cost/ ; HireInSouth — https://www.hireinsouth.com/post/deel-pricing ; Shorpay — https://shorpay.com/blog/compare/eor-pricing-comparison ; StratEdge — https://stratedgeglobal.com/oyster-vs-deel/ ; Conexo — https://conexo.ca/blog/deel-vs-remote-vs-oyster-vs-multiplier-vs-pebl-eor-pricing-compared | S/N | A (Remote) / B–C (Deel, Oyster) |
| E32 | Labour Codes in force 21 Nov 2025; 50% wages rule; gratuity | HRone — https://hrone.cloud/?p=56103 ; Embee — https://embee.co.in/?p=42368 ; Outlook Money gratuity explainer — https://www.outlookmoney.com/amp/story/retirement/pension/gratuity-under-new-labour-codes-rules-eligibility-and-impact-explained ; Suryoday Bank — https://suryoday.bank.in/blogs/new-labour-law-regime/ | N | B/C |
| E33 | Copyright Act ss.17/19; *Pine Labs v Gemalto* (Delhi HC DB, 2011) | BananaIP — https://www.bananaip.com/?p=83620 ; Vidhi Judicial (ss.17–21) — https://vidhijudicial.com/sec-17-to-21-chapter-iv-(ownership-of-copyright-and-the-rights-of-the-owner)-the-copyright-act,-1957.html ; Legitquest — https://www.legitquest.com/case/pine-labs-pvt-ltd-v-gemalto-terminals-india-pvt-ltd-others/74466 ; Khurana & Khurana — https://www.khuranaandkhurana.com/2011/05/25/pine-labs-pvt-ltd-vs-gemalto-terminals-india-pvt-ltd-others | S | B |
| E34 | ITR-1/ITR-4 lack Schedules FA/FSI/TR | Income Tax Department, *Enhancing Tax Transparency on Foreign Assets and Income* — https://www.incometax.gov.in/iec/foportal/sites/default/files/2024-11/Enhancing%20Tax%20Transparency%20on%20Foreign%20Assets%20and%20Income.pdf ; ITRNGST guide — https://itrngst.com/guides/income-tax/schedule-fa-freelancers-ay-2026-27/ | S | **A** |
| E35 | USD/INR ≈ 95.5 (25 Aug) to ≈ 96.8 (10 Oct 2026) | Banklive — https://banklive.net/en/convert/usd-to-inr ; HDFC Sky/PTI — https://hdfcsky.com/news/rupee-rises-24-paise-to-close-at-95-46-against-us-dollar ; Pound Sterling Live — https://www.poundsterlinglive.com/history/USD-INR-2026 | S | C |
| E36 | Winman product description | https://www.winmansoftware.com/ ; https://www.techjockey.com/detail/winman-ca-erp | S | A (vendor self-description) |
| E37 | GST practicalities (zero-rating, invoice, FX-fee GST) | Xflow — https://www.xflowpay.com/blog/export-of-services-under-gst ; PayGlocal — https://payglocal.in/blog/gst-on-export-of-services-impact ; Razorpay — https://razorpay.com/blog/gst-export-services-india-guide/ ; DisyTax — https://disytax.com/export-of-services-under-gst/ ; Incorpx — https://www.incorpx.io/blog/gst-export-of-services-freelancers-india | S | C |
| E38 | Deel platform and GST (single third-party page) | TaxTap — https://taxtap.in/platform/deel/gst ; Shorpay — https://shorpay.com/blog/indian-contractor-invoice-gst-lut | S | C |
| E39 | All take-home, cliff, break-even and sensitivity figures | My Python model (new-regime tax engine with surcharge/rebate marginal relief; structure models) — run in the working environment on 21 Oct 2026; inputs listed in D3 | — | **M** |

---

### Closing note on reliability

- **Strongest ground (A/B):** §44ADA parameters and eligibility; surcharge tiers; ITR-4 foreign-asset limit; RBI purpose codes and EEFC rule; W-8BEN mechanics and US sourcing rule; Remote's published price; the Rule 96A realisation condition; the omission of IGST s.13(8)(b); IP assignment defaults.
- **Moderate ground (B/C):** the Income-tax Act 2025 numbering; the 1 Oct 2026 FEMA/EDF details (primary RBI text unseen); GST registration threshold interplay; Labour Codes effects; Deel/Oyster prices.
- **Weak ground (C/D):** bank and fintech fees, PA-CB statuses, the LLP remuneration cap, GST return mechanics, MSA drafting practice, and all compliance-cost inputs.
- **Model outputs (M)** are only as good as these inputs. Replace the cost assumptions with real quotes, and have a practising CA reproduce the 44ADA and cliff arithmetic against the exact provision text before relying on them.
