---
id: tracks.remote-cross-border
title: Cross-Border Remote Work for GenAI Roles
content_type: guide
stage: 11
status: published
last_verified: 2026-11-19
review_by: 2027-02-17
sources: [T0-43, T0-07, T0-18, T0-35, T0-36]
roles: []
geos: [global, india, us, uk, eu]
tags: [remote, cross-border, eor, contracting, payment-rails, india]
summary: "Evidence-graded guide to finding, pricing and structuring cross-border remote GenAI roles across direct contracting, Contractor of Record, Employer of Record and local entities (T0-43)."
---

# Cross-Border Remote Work for GenAI Roles

> [!WARNING]
> **Dated pointers, not legal or tax advice.** Cross-border employment classification, permanent establishment (PE), intellectual-property assignment, foreign-exchange rules and Employer of Record (EOR) compliance vary by jurisdiction and change frequently. Confirm contract language and tax filings with a qualified lawyer and chartered accountant before signing.

## The short answer

Genuine cross-border remote GenAI jobs are scarce: roughly **11.0%** of AI Engineer postings carry a remote tag (`B · T0-43 L57, L109`), over **95%** of remote postings across general tech are single-country (`B · T0-43 L114`), and an order-of-magnitude **0.2–1.2%** of AI-engineer postings are both remote and open to residents of India (`M · T0-43 L58, L118`). Treat cross-border remote work as a targeted search aimed at three real channels — **foreign employers with a local entity**, **US/European startups willing to contract B2B or use an EOR/CoR**, and **distributed product companies whose time-zone window includes your country** — rather than mass-applying to "remote" board tags (`T0-43 L59–60, L111`).

Do not accept a foreign contract blindly on headline USD numbers. From India, breaking even against a Bengaluru senior software-engineer median total compensation of ₹55.4 lakh requires roughly **$39.4/hour** (and **$75.8/hour** against the ₹1.066 crore P90) at 1,500 billable hours before accounting for unpaid leave, hardware, FX spreads, insurance and compliance (`M · T0-43 L62, L200–204`). For employers worried about misclassification or local payroll, offer a concrete structure — **direct B2B contracting**, **Contractor of Record (CoR)** or **Employer of Record (EOR)** — while being candid that an EOR does not remove **permanent-establishment (PE)** risk if you negotiate or conclude contracts locally (`C · T0-43 L230`).

## At a glance

| Question | What the evidence shows (as of November 2026) | Grade · Source |
|---|---|---|
| Share of AI Engineer postings tagged remote | **11.0%** (JobsPipe, counted 2026-09-10; hybrid counted as on-site) | B · T0-43 L57, L109 |
| Share of remote postings open worldwide | **3.3%** (WFH.team, n=6,676) and **2.1–4.0%** (Jobgether, Sep 2026); **95.7%** single-country (SeekerScore, n=180,429) | B · T0-43 L58, L112–114 |
| AI Engineer postings remote and open to India | **0.2–1.2%** order-of-magnitude model estimate; 1 of 45 Fast AI Jobs remote AI postings was explicit worldwide | M · T0-43 L58, L110, L118 |
| Global EOR list pricing | **$599–$699/employee-month** at Deel, Remote and Oyster; CoR **$199–$325/mo**; India-specialist EORs **$99–$399/mo** (vendor quotes) | A/B/C · T0-43 L61, L219 |
| India senior break-even contract rate (1,500 h/yr) | **$39.4/h** vs Bengaluru senior SWE P50 (₹55.4L); **$75.8/h** vs P90 (₹1.066Cr) at ₹93.765/USD (2026-11-12), before overheads | M · T0-43 L62, L200–204 |
| India presumptive-tax ceiling (s.58(2) / old §44ADA) | ₹75 lakh (~**$79,987** at ₹93.765/USD), hit around $44/h × 1,800 h or $53/h × 1,500 h | M · T0-43 L336 |
| RBI cross-border PA-CB transaction cap | **₹25 lakh** (~$26.7k) per transaction under RBI Master Directions (2025-09-15); larger invoices need AD-bank SWIFT | A/B · T0-43 L245, L276 |

## Who actually hires cross-border remote for GenAI

Most postings labelled "Remote" are country-locked for tax, payroll, export-control or data-residency reasons. Across 6,676 remote listings on WFH.team, **67.4%** were US-only, **7.8%** multi-country and **3.3%** worldwide (`B · T0-43 L112`). In a November 2026 sample of 45 remote AI-engineer roles on Fast AI Jobs, 10 (22.2%) were explicitly US-only, 1 (2.2%) was explicitly worldwide and 0 named India (`M · T0-43 L110`). Frontier labs remain overwhelmingly on-site or region-locked: OpenAI had roughly **4%** remote openings (28 of 699 in April 2026, `C · T0-43 L116`), and Anthropic Fellows required work authorisation and physical location in the US, UK or Canada (`B · T0-43 L71`).

Even distributed-first companies draw hard geographic fences:

- **Time-zone fenced distributed firms:** PostHog's published handbook (opened directly) restricts hiring strictly to people physically located between **GMT+2 and GMT−8**, excluding India even if a candidate offers to shift hours; it employs via its own entities in the US, UK and Germany and via Deel EOR or contracting elsewhere (`A · T0-43 L59–60, L127, L602`).
- **Country-banded global remote firms:** GitLab dropped its legacy location-factor calculator on **2026-02-19** in favour of country-specific Radford local-currency pay ranges; its handbook table lists India under a PEO arrangement (Global Upside, select roles only) whereas 2026 job boilerplate lists India among legal-entity countries (`B · T0-43 L60, L126, L208`).
- **Foreign-HQ companies hiring via Indian entities or intermediaries:** Filtering Jobgether for India-reachable remote AI roles on 2026-11-13 returned 416 listings — **209 India-located**, 5 Asia-wide and **202 "anywhere"** postings inflated by all-open ATS feeds (`B · T0-43 L59, L111`). Most India-reachable roles at US-headquartered firms (Databricks, Twilio, Zoom, Skyflow, H2O.ai) hire into Indian payroll bands rather than US bands (`C · T0-43 L139, L184`).
- **AI-training and expert-data platforms (supplemental only):** Platforms such as Mercor, Scale and Surge offer fast remote onboarding, but provide weak worker protections and face active misclassification litigation (including a Mercor class action covering roughly 30,000 workers alongside April 2026 breach reports; Handshake AI roles are US-only) (`B/C · T0-43 L69, L293`). Upwork reported an AI-skill gross services volume run-rate near **$450 million** (+55% year on year in Q3 2026) even as total volume fell roughly 10% to $914.1 million, with effective take rates near 20% (`B/C · T0-43 L70, L561`). Treat marketplaces as utilisation fillers or portfolio cashflow, not primary senior employment.

## Pay localisation models and India break-even economics

Foreign employers price cross-border GenAI talent using one of three models (`T0-43 L64, L207–208`):

1. **Formulaic location factor:** Benchmark city pay × level × step × location multiplier. PostHog publishes its San Francisco benchmark multiplied by a location factor with a **0.60 floor outside the US** (`A · T0-43 L64, L207`).
2. **Local-market survey bands:** Country-specific Radford/Pave bands paid in local currency (GitLab's post-February 2026 model; standard at foreign-HQ firms with Indian entities) (`B · T0-43 L60, L208`).
3. **Direct global/US-adjacent contracting:** Negotiated hourly or monthly retainers billed directly to a foreign startup or enterprise without a local entity. Vendor rate cards quote India LLM developers at **$19–$33/h** (junior), **$28–$72/h** (mid) and **$42–$100/h** (senior), and India EOR fully loaded mid-level AI engineers at **$35k–$55k/year** (`C, COI · T0-43 L63, L186, L189`). For cross-region context, vendor reports place Latin America senior AI/ML near $103k (Revelo), Poland B2B AI engineers at $74k–$92k (No Fluff Jobs relay), and Lemon.io senior SWE hourly rates at $64 (North America), $39–$42 (Latin America / Eastern Europe / Asia) (`C, COI · T0-43 L305–311`).

Because top Indian product and GCC packages have risen, cross-border offers must be benchmarked against **your real local alternative**, not the broad IT-services average. Full role and employer pay bands live in [pay-benchmarks.md](../09-compensation/pay-benchmarks.md) (D-019); the break-even reference below shows why senior engineers in India should reject low-rate foreign contracts:

| Local Bengaluru benchmark (Levels.fyi, 2026-07-18) | Annual INR | USD equiv. (₹93.765/$, 2026-11-12) | Break-even at 1,500 billable h/yr | Break-even at 1,800 billable h/yr | Grade · Source |
|---|---|---|---|---|---|
| Senior SWE P50 total comp | ₹55.4 lakh | $59.2k | **$39.4/h** | **$32.9/h** | B/M · T0-43 L62, L179, L200 |
| Senior SWE P75 total comp | ₹79.5 lakh | $84.8k | **$56.5/h** | **$47.1/h** | B/M · T0-43 L179, L200 |
| Senior SWE P90 total comp | ₹1.066 crore | $113.7k | **$75.8/h** | **$63.2/h** | B/M · T0-43 L62, L179, L200 |
| Top-employer all-level medians (Broadcom, Rippling, Rubrik, Airbnb, Stripe) | ₹99.4L–₹1.22Cr | $106k–$130k | **$70.7–$86.7/h** | **$58.9–$72.3/h** | B/M · T0-43 L181 |

> [!NOTE]
> Break-even figures above divide annual total compensation by billable hours only (`M · T0-43 L200–204`). Independent contractors must also add **15–25%** (`[P]`) for health insurance, unpaid leave, bench time, hardware, accounting fees and FX/rail spreads — though Indian residents billing up to ₹75 lakh (~$80k) may offset part of this through presumptive taxation under Income-tax Act 2025 s.58(2) (see [india-remote-tax.md](../09-compensation/india-remote-tax.md)).

## Choosing a legal structure: direct contracting, CoR, EOR or local entity

When a foreign company wants to hire you from another country, the hiring friction is almost always **legal and compliance risk**, not technical fit (`T0-43 L68, L226–238`). Notice how contractor vs FTE norms vary sharply by geography in Deel's 2026 client mix: India runs roughly **70% FTE / 30% contractor**, whereas Poland runs 20/80, Brazil 16/84 and Argentina 4/96 (`C, COI · T0-43 L309`).

| Structure | Who employs you | Typical employer platform fee | Misclassification & payroll risk | Tax, IP & PE notes | Grade · Source |
|---|---|---|---|---|---|
| **Direct B2B contractor** | Self / sole prop / OPC / Pvt Ltd | **$0–$49/mo** (e.g., Deel $49, Remote/Oyster $29) | Employer bears misclassification risk if managing you like a full-time employee | Lowest employer cost; best India tax up to ₹75L (s.58(2)); contractor is first owner of IP under Indian Copyright Act s.17 unless explicitly assigned with worldwide/perpetual scope | A/B · T0-43 L219, L256–258 |
| **Contractor of Record (CoR / Shield)** | Platform contracts with you and indemnifies client | **$199–$325/mo** (Deel/Remote $325; Papaya ~$199; Remote Plus $99 w/ $100k indemnity) | Platform assumes or insures misclassification indemnity | Faster than EOR, keeps contractor tax status in India, still does **not** remove PE risk if you close commercial deals | A/B/C · T0-43 L219, L230 |
| **Employer of Record (EOR)** | EOR's local legal entity (e.g., Indian Pvt Ltd) | **$399–$699/mo** global; **$99–$399/mo** India-specialist + 1-mo salary deposit | Removes direct misclassification risk; handles EPF, gratuity, TDS and Four Labour Codes | Salaried tax treatment in India (22–24% lower take-home vs presumptive tax up to ₹75L, near parity at ₹1.2Cr; `T0-07 L92–93`); **does not eliminate dependent-agent PE risk** | A/B/C · T0-43 L61, L219, L230 |
| **Employer's own local entity (GCC / subsidiary)** | Foreign firm's local subsidiary | Internal entity overhead | Employer manages full local compliance | Simplest route for equity/RSUs and mobility, but typically pays local survey bands rather than US bands | B · T0-43 L59, L126, L139 |

### EOR platform landscape (verified November 2026)

| Platform | Published EOR fee | Contractor / CoR fees | Key trade-offs and status (as of 2026-11-19) | Grade · Source |
|---|---|---|---|---|
| **Deel** | From **$599/employee-mo** | Contractor $49/mo; CoR from $325/mo | Pricing read directly on Deel's page; 1-mo salary deposit typical; third-party FX margin 0.6–2% (`C`); **Rippling v. Deel** litigation proceeding (Feb & Sep 2026 rulings, `B`) | A (price) / B (litigation) · T0-43 L61, L219, L293, L341 |
| **Remote** | **$599/mo** (annual) / **$699/mo** (monthly) | Contractor $29/mo; Plus $99/mo; CoR from $325/mo | Owned-entity model across supported countries (appeals to IP-sensitive employers); verify India deposit terms | B · T0-43 L219, L340 |
| **Oyster** | **$699/mo** ($599 in some third-party tables) | Contractor $29/mo | Distributed-team focus; statutory India costs (EPF, professional tax, gratuity) pass through on top | B/C · T0-43 L219, L342 |
| **Pebl** (formerly Velocity Global) | Reported from **$399/mo** | Quote-based | Rebranded from Velocity Global to Pebl; enterprise compliance focus; verify quote directly | C · T0-43 L219 |
| **Multiplier** | Reported **$450–$500/mo** | Contractor ~$40/mo (secondary) | APAC focus, flat standalone EOR fee without core HRIS base fee; figures from third-party/vendor guides | C · T0-43 L219, L341 |
| **Rippling** | Quote-based, reported **$499+/mo** | Requires core platform base fee ($8+/user-mo) | Best only if employer already runs Rippling HR/IT; active litigation with Deel | C (price) / B (litigation) · T0-43 L219, L293 |
| **Papaya Global** | Reported from **$499/mo** | CoR reported ~$199/mo; global payroll ~$29/mo | Fintech-heavy owned payment rails; verify standalone EOR quote directly | C · T0-43 L219 |
| **India-specialist EORs** (e.g., Wisemonk, Remunance, Gloroots) | Reported **$99–$399/mo** | Varies by vendor | Lower monthly wrapper for India-only hiring, but pricing comes solely from vendor marketing (`COI`); vet financial stability and escrow practices | C (COI) · T0-43 L219 |

### Permanent establishment (PE) and Indian contract defaults

Two legal misconceptions kill cross-border offers late in negotiation:

1. **PE risk survives an EOR:** Even Deel's own guidance notes that hiring through an EOR does **not** eliminate dependent-agent permanent-establishment risk if the worker habitually concludes contracts or plays the principal role leading to contract conclusion in-country (`C · T0-43 L230`). The OECD's **November 2025** home-office PE commentary update introduced a **50% working-time threshold** paired with a **commercial-reason test** — and **India recorded formal reservations** (`B · T0-43 L68, L230, L673`). Pure engineering/R&D roles (writing code, training/evaluating models, no local sales authority or Indian client contracting) carry substantially lower PE exposure than sales or Forward Deployed Engineer roles closing local deals.
2. **Indian contract defaults differ from US templates:** Under India's **Copyright Act 1957**, an independent contractor is the first owner of software code (`s.17`), and an IP assignment that omits duration and territory defaults under **s.19(5) and s.19(6)** to **five years and India only** (reinforced by *Gemalto v Pine Labs*, Delhi High Court) (`B · T0-43 L67, L256–257`). Conversely, under **Indian Contract Act 1872 s.27**, post-termination non-compete clauses are generally void in India (`B · T0-43 L258`). Always state worldwide, perpetual IP assignment explicitly (tied to receipt of payment) so a foreign client's legal team does not block onboarding.

## Time-zone overlap economics and payment rails

Time-zone overlap heavily filters which remote markets are realistic without wrecking your health. For a 09:00–18:00 IST workday, **UAE (7.5 h)**, **Singapore (6.5 h)**, **Israel/Finland/Estonia (5.5–6.5 h)**, **Germany/Netherlands/France/Switzerland/Poland (4.5–5.5 h)** and **UK/Ireland (3.5–4.5 h)** offer comfortable daily synchronous overlap, whereas **US and Canada have 0.0 h** of overlap with standard IST daytime hours (`B · T0-35 L57, L485–515; T0-36 L320–332`). See [country-rankings.md](country-rankings.md) for the full 33-country Remote-from-India lens and time-zone table.

For India-based contractors billing foreign clients directly, payment rails and export compliance are owned in full by [india-remote-tax.md](../09-compensation/india-remote-tax.md) (D-019). The key operational gates from `T0-43` and November 2026 verification are:

- **₹25 lakh per-transaction PA-CB cap:** Under the RBI Master Directions on Payment Aggregators (2025-09-15), non-bank Cross-Border Payment Aggregators (PA-CB) are capped at **₹25 lakh (~$26.7k) per transaction** (`A/B · T0-43 L245, L276`). Larger invoices must travel via an Authorised Dealer Category-I (AD-I) bank SWIFT wire.
- **Rail trade-offs:** **Wise Business India** (terms 2026-07-24 read directly, `A · T0-43 L66, L269`) states RBI PA-CB authorisation, restricts receipts to export payments with proof of business, auto-remits in INR (no balance holding), applies ₹25L per-tx cap, and charges currency-dependent FX fees + 18% GST (eFIRC listed free on fee page vs $2.50 in older help docs; new USD details unavailable for some accounts). **Skydo** received final RBI PA-CB-I authorisation in January 2026 (press/vendor reported, `B/C · T0-43 L271`) with vendor-claimed flat fees ($19–$29) and instant FIRA. **Payoneer** received **in-principle** RBI PA-CB authorisation on 2026-01-22 (final not verified as of November 2026; charges up to 3% INR withdrawal; `B · T0-43 L270`). **Avoid PayPal** (~7.4–8.4% + $0.30 friction; `C · T0-43 L272`).
- **FEMA 2026 and IGST updates:** FEMA (Export and Import of Goods and Services) Regulations, 2026 (effective 2026-10-01, amended 2026-09-22) set export realisation at **9 months** (12 months for INR-invoiced exports) and introduce monthly Export Declaration Form (EDF) reporting (`A/B · T0-43 L65, L243`). Finance Act 2026 omitted IGST s.13(8)(b) from 2026-03-30, allowing qualifying intermediary services to export zero-rated under LUT (`A/B · T0-43 L246`).

## How to do it

1. **Filter by geography and overlap first (`[P]`):** Pick two target corridors — for example UK/EU/Singapore for 3.5–6.5 h IST daytime overlap, plus US async-friendly Series A–C AI startups if you can tolerate late-evening syncs (19:00–22:00 IST). Check [country-rankings.md](country-rankings.md) for employer-market density.
2. **Qualify hiring structure before investing interview hours (`[P]`):** On the first recruiter or founder screen, ask directly: *"Are you open to hiring someone resident in [Country] via direct B2B contract, CoR, EOR or your local entity, and is the pay band local or global?"* Do not spend 15 hours on take-homes before confirming location eligibility (PostHog-style hard time-zone walls reject automatically).
3. **Price against your local senior opportunity cost (`M · T0-43 L200–204`):** Compute your floor rate from your realistic local offer (`annual local TC ÷ 1,500 h × 1.20` for contractor overheads) and check whether staying below India's ₹75L presumptive ceiling or clearing it decisively (>₹1.1Cr) yields higher net cash (see [india-remote-tax.md](../09-compensation/india-remote-tax.md)).
4. **Bring the compliance answer to small startups (`[P]`):** Founders often refuse foreign hires simply because they do not know how to run payroll abroad. Present a crisp two-option proposal: Option A — direct B2B services agreement (Common Paper PSA + explicit worldwide/perpetual IP assignment + no local sales authority to limit PE risk); Option B — CoR ($199–$325/mo) or EOR ($399–$699/mo) if their counsel requires employment indemnity.
5. **Audit the employer and rail before starting work (`B/C · T0-43 L280–291`):** Verify corporate registration, LinkedIn history of the hiring manager and corporate domain email. Never run untrusted take-home code outside a disposable VM/container, never buy equipment from a "designated vendor" using an upfront cheque, and verify your chosen payment rail on RBI's authorised payment-system operator list.

## Templates and examples

### Script: de-risking cross-border hiring for a US/EU startup founder

> "I am based in Bengaluru (IST) and can guarantee [3–4 hours of daily overlap, e.g., 08:30–12:00 EST / 09:00–13:30 GMT]. Most foreign teams I work with choose one of two clean setups:
> 1. **Direct B2B contractor** under a standard services agreement (for example Common Paper PSA) with explicit worldwide, perpetual IP assignment on payment and a pure engineering scope (no local contracting or sales authority). Zero platform overhead for you; I handle local GST LUT, invoicing and tax filings.
> 2. **Contractor of Record or EOR** (such as Remote, Deel or Pebl, typically ~$325/mo for CoR or ~$399–$699/mo for EOR) if your counsel prefers third-party classification indemnity or local payroll.
> Which structure fits your finance and legal team best?"

## Checklist

- [ ] Confirmed in writing that the employer can legally engage a resident of your country (not merely a generic "Remote" ATS tag).
- [ ] Confirmed whether compensation uses a **global rate**, a **location-factor formula** or a **local-entity survey band**.
- [ ] Benchmarked the offer against your realistic local total compensation at 1,500 billable hours plus 15–25% contractor overhead (`[P]`).
- [ ] Verified contract clauses: explicit worldwide, perpetual IP assignment upon payment (overriding India Copyright Act s.19(5)/(6) defaults), net-15/net-30 payment terms, currency, governing law and pure R&D/engineering scope (no local sales/contracting authority).
- [ ] Verified payment rail limits (₹25L per-tx PA-CB cap in India), FX spread, e-FIRC/FIRA issuance and RBI authorisation status.
- [ ] Ran the employer fraud check (domain match, corporate registry, no upfront hardware cheque, disposable VM for any coding repository).

## Pitfalls

- **Treating "Anywhere" job-board filters as real eligibility:** Roughly half of Jobgether's India-filtered remote AI postings (202 of 416) came from unvetted "anywhere" ATS feeds (`B · T0-43 L111`). Always confirm on the company's own careers page.
- **Assuming an EOR solves PE risk:** An EOR handles local statutory payroll and misclassification, not dependent-agent PE if you negotiate local contracts (`C · T0-43 L230`).
- **Using US template IP clauses untouched under Indian law:** Omitting explicit duration and territory defaults Indian contractor assignments to 5 years and India only (`B · T0-43 L256–257`).
- **Ignoring remote hiring scams and malware:** FTC job-scam losses jumped from $90M (2020) to $501M (2024), with $150.4M in Q4 2025 alone (`C · T0-43 L282`), DOJ prosecutions documented DPRK remote-IT laptop-farm schemes (`B · T0-43 L285`), and Gartner forecast 1 in 4 candidate profiles worldwide could be fake by 2028 (`C · T0-43 L287`). Expect stricter identity checks (ID/video verification via known ATS links only) and apply equally strict due diligence to unverified remote recruiters.
- **Using PayPal or consumer accounts for B2B export invoices:** PayPal's ~7.4–8.4% friction destroys margin (`C · T0-43 L272`), and consumer transfer accounts risk freezes and missing e-FIRC/FIRA export proof.

## Evidence and limits

- **Primary session audit (`T0-43`):** `T0-43` opened 9 of 141 sources in full (6% Read rate: JobsPipe, Fast AI Jobs, Jobgether India filter, PostHog handbook/hiring, RBI FX rate, Deel pricing, Wise India fees and 2026-07-24 ToU); the remaining 131 sources were Extract-only (`T0-43 L402–547`). Under repository convention D-018, all platform tallies (JobsPipe, Fast AI Jobs, Jobgether, Levels.fyi) are graded **B** rather than A.
- **Live primary-source verification (2026-11-19):** RBI's ₹25L PA-CB cap (2025-09-15 Master Directions), FEMA 2026 Regulations & September 22, 2026 amendment (9/12 months, unified EDF), Income-tax Act 2025 s.58(2)/s.62(4)/s.63, Finance Act 2026 IGST s.13(8)(b) omission, and 2026 EOR pricing ranges (including Velocity Global's rebrand to Pebl) were cross-checked directly against live sources on 2026-11-19.
- **Evidence gaps:** Independent worker-side pay datasets for foreign-band remote roles paid into India do not exist (vendor quotes are Grade C with COI); conversion rates from remote contracting to sponsored relocation are unmeasured (`T0-43 L295–301`); and EOR pricing for Rippling, Multiplier, Pebl and Papaya relies on third-party/vendor guides rather than audited quotes.
- **Freshness:** Posting-share snapshots (JobsPipe 2026-09-10, Jobgether Sep/Nov 2026) are volatile (31-day expiry class); EOR fees, RBI PA-CB statuses and tax rules should be re-verified by **2027-02-17**.

## Next steps

- **India-specific remote strategy and city comparison:** [india-remote-playbook.md](india-remote-playbook.md)
- **India tax, FEMA, GST LUT, invoicing and payment rails:** [india-remote-tax.md](../09-compensation/india-remote-tax.md)
- **Compare 33 countries on remote reach, pay and visas:** [country-rankings.md](country-rankings.md)
- **Independent consulting, retainers and fractional positioning:** [freelance-fractional.md](freelance-fractional.md)
- **Relocating abroad instead of staying remote:** [visa-and-relocation.md](visa-and-relocation.md)
- **Local vs global compensation bands:** [pay-benchmarks.md](../09-compensation/pay-benchmarks.md)
