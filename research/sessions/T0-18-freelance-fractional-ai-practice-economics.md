---
id: T0-18
title: "Independent GenAI Consulting & Fractional Head-of-AI Practice Economics (October 2026)"
date: 2026-10-25
status: complete
topic: freelance-fractional-ai-practice-economics
tags: [fractional-head-of-ai, fractional-cto, genai-consulting, rate-cards, retainers, advisory-equity, msa-clauses, liability-caps, client-acquisition, solo-practice-model, us, europe, india]
informs_decisions:
  - "Go independent vs stay employed, and what must be true first"
  - "Hourly vs retainer vs fixed-fee pricing, and the rate card to publish"
  - "MSA template choice and clause positions (liability cap, pre-existing IP carve-outs, AI disclaimers, data privacy)"
  - "Acquisition channel mix (network and referral vs marketplaces)"
  - "Platform, invoicing and contract-tool selection"
  - "India-resident structuring questions to put to a chartered accountant"
confidence: medium
---

# T0-18 · Independent GenAI Consulting and Fractional Head-of-AI Practice Economics

*As of 2026-10-24. Claims are tagged **found** (read in a retrieved source, cited as [S##] to the ledger at the end), **recalled** (from model memory, Grade D at most), **modelled** (my Monte Carlo and tax arithmetic, Grade D) or **inferred** (design judgment, Grade D). Untagged sentences inside a finding are **found**. This is research, not legal or tax advice.*

## Prior

Five propositions held before the research. They come from the brief's "known (unverified)" list and from recall, so each is Grade D by rule. No numeric credences were recorded at the outset; the Delta section records the direction and size of each update.

| # | Proposition (checkable) | Origin | Test I applied |
|---|---|---|---|
| P1 | Experienced US independent AI engineers and consultants bill roughly **$150–$300 per hour**. | Brief; recall | Two or more independent sources quoting asked or offered rates; look for the upper tail ($300+) and for a lower bound |
| P2 | A **Fractional Head of AI retainer is about $10K per month**, for example 10 hours a week for $8,000 a month plus about 0.25% advisory equity. | Brief; recall | Published retainers or vendor benchmarks; arithmetic on hours; advisory-equity benchmarks |
| P3 | **Client acquisition (churn) and scope creep** are the dominant operating risks of an independent AI practice. | Brief; recall | Survey evidence on acquisition pain; evidence on scope creep and margin; contrary findings |
| P4 | **Many practitioners return to full-time employment.** | Brief; recall | Exit or return-to-employment data; intent surveys; survivorship bias |
| P5 | Standard MSAs **cap provider liability at fees paid in the preceding 3–6 months**, and pre-existing IP (agent harnesses, prompt templates) is carved out of the client's ownership. | Brief; recall | Primary template text for caps and IP; published statistics on cap multipliers |


## Research Question

**Decision.** What are the empirical market rates, client-acquisition funnels, contract structures and revenue distributions for independent GenAI consultants, Fractional Heads of AI and 1–5 person boutique AI engineering practices in late 2026, and therefore how should a practitioner price, contract, source clients and judge viability?

**Sub-questions** (each answered under Detailed Findings):

1. Rate cards (hourly, project, retainer) by experience tier and by geography: US, Europe, India.
2. How a Fractional Head of AI engagement is structured: hours, retainer, term, deliverables, decision rights, equity.
3. Which MSA protections matter: liability caps, pre-existing IP carve-outs, AI accuracy disclaimers, data privacy.
4. Which acquisition channels and playbooks work, and which commoditise.
5. The realistic P25/P50/P75/P90 of annual revenue after expenses and taxes for full-time independents.
6. Which platform, invoicing and contract-template tools exist and what they cost.

**Scope.** In scope: solo technical consultants, fractional engineering and AI leaders, and agencies of one to five people. Out of scope: TCS, Wipro and Infosys-scale outsourcers. "India" is covered as (a) India-based providers selling to US and European clients, which is what the sources describe, and (b) Indian domestic client rates, for which no dataset was found.

**Method.** Web searches and page fetches across this session (102 ledger rows: 78 read as page text, 20 seen only as search-result extracts, 2 blocked, 2 searched with nothing usable; grades A 17, B 18, C 62, ungraded 5). An attempt to run the research through parallel sub-agents failed on a rate limit and produced nothing usable, so all research was done directly; a later attempt to have two independent reviewers audit the finished report against its sources hit the same limit and returned nothing, so I ran that audit myself (next paragraph). Searches were deliberately aimed at failure modes and counter-evidence (Detailed Findings 9). The solo-practice model is a Monte Carlo of realised rate × paid hours with a US federal and an Indian tax engine, hand-checked against closed-form cases (Detailed Findings 7). Where a search found nothing, the ledger says so (Access = Gap) rather than filling the hole from memory.

**Second pass (2026-10-25).** After the report was assembled I re-fetched 39 of the 102 sources and compared the figures the report relies on. Most matched. These did not, and the report now reflects them: Go Fractional's live CAIO and CTO benchmarks had moved since my first read (the CAIO offer rate fell from $189 to $125 as postings rose from 6 to 10) and IT Jobs Watch's 2024 comparison moved from £613 to £625; my first paraphrase of Common Paper's PSA was loose on termination, refunds and the warranty remedy, and I had listed gross negligence as an example of unlimited claims when the template's help article lists it under increased claims; a Second Talent "$145 to $210" LLM-rate trend and a "$12,000" example from a CMO-focused article did not reproduce and were dropped; the 27.6M full-time-independents figure is MBO's 2025 count, not a 2026 one; the Fractional Jobs sample includes past and aspiring fractionals, not only current ones; and a few wordings were tightened (Delta rows R8 to R11). Sources whose pages the session could not reach the second time were not re-checked and rest on the first read (listed under Honest gaps).

**Evidence grades** (as set by the brief; recall caps at D):

| Grade | Meaning | Typical examples here |
|---|---|---|
| A | Canonical primary source, for the claim the page itself makes | A vendor's own fee page; Common Paper template text; Gartner's press release (for what Gartner forecasts) |
| B | Independent or transparent secondary | Law-firm commentary; large platform datasets with disclosed method; trade press |
| C | Directional: vendor, self-reported, small n or single source | Vendor rate guides; sponsor-run surveys; aggregator pages |
| D | Recalled, inferred, modelled or design judgment | Everything produced by my model; clause adaptations; funnel arithmetic |

Access labels in the ledger: **Read** (page text retrieved), **Extract** (seen only as a search-result text extract), **Blocked** (fetch refused), **Gap** (searched, nothing usable). A Grade A applies only to what the page says about itself: a vendor's price list is A for the price, not for whether anyone pays it.

**Confidence by claim type** (overall frontmatter confidence is *medium* because the structural and legal findings are firmer than the numerical ones):

| Claim type | Basis | Confidence |
|---|---|---|
| Asking rates (US, Europe, India) | Vendor guides, platform benchmarks, adverts; no transacted rates | Low to medium |
| Retainer structure and size | One firm's published package; vendor-computed ranges; sponsor surveys | Low to medium |
| MSA clause set and the cap norm | Primary template text and statistics; law-firm commentary | Medium to high for what is standard; low for what clients accept from a solo provider |
| Acquisition channels | Consistent direction across sponsor-run and independent surveys; no AI funnel data | Medium on direction; low on magnitudes |
| Income distribution | Modelled; no AI-specific data; proxies disagree with the model's upper tail | Low |
| Tax mechanics (US, India) | Secondary sources plus my simplifications | Low to medium; verify with a professional |
| Tool fees | Vendors' own pages (A) where retrievable; estimates elsewhere (C) | Medium |


## Key Findings

**Answer in brief.**

- **Rates.** US senior AI consultants *ask* $150–$250 an hour (middle 50% of Go Fractional's live CAIO and CTO benchmarks); employer-posted offers are lower (CAIO $125–$189, CTO $124–$129 across two reads of the live pages). The UK GenAI contract median is £550 a day; vendors quote $50–$100 an hour for India-based seniors. Grade C throughout: asked or advertised rates, not transacted ones.
- **Retainers.** About $8,000–$13,000 a month for 10–13 hours a week. "$8,000 for 10 hours a week" is $200 an hour only on a 4-week month; it is $185 on a 52/12-week month.
- **Contracts.** The primary-source norm is a cap of 1× fees over the prior 12 months. The brief's 3–6 months is contradicted. Carving pre-existing IP out of the assignment is standard template text.
- **Acquisition.** Referrals and networks dominate (92–94% in two sponsor-run surveys). Acquisition is the number-one challenge (90%). I found no AI-specific funnel benchmark.
- **Distribution.** No empirical AI-specific income distribution was found. Modelled US net after overhead, health insurance and federal tax: $83K / $105K / $130K / $160K (P25/P50/P75/P90) for practitioners who get traction. If 30%, 45% or 60% of entrants stall, P25 falls to $38K, $24K or $19K while P75 and P90 barely move. Grade D.

**F1. Posted rates are asking rates, and the little offer-side data sits below them. Grade C.**
Go Fractional's live benchmarks, read twice (about 2026-10-20 and again on 2026-10-25), show fractional Chief AI Officers asking $190–$208 an hour on average (P25–P75 $150–$250 both times) against employer-posted listings averaging $125–$189, so offers run at 0.66–0.91× of asks. For fractional CTOs, asks average $209–$212 against $124–$129 posted (0.59–0.61×). The samples are small and the CAIO figures moved most: 6 then 10 CAIO job posts and 19 then 17 CTO posts over 90 days, with 326 CAIO profiles on the first read (the CAIO page no longer states a count) and 1,042 then 1,116 CTO profiles [S01, S02]. Go Fractional's own survey (n=213, April 2026) reports a $153 average across fractional roles and $218 for CAIO [S03]; Fractional Jobs' larger report (n=1,733) gives mean hourly rates of $209–$229 by function and nothing AI-specific [S06]. *So what:* treat $150–$250 as the asking corridor and plan realised rates nearer its lower half (the model's median is $165).

**F2. US contractor cards cluster at $130–$235 for senior AI engineers; $300+ is marketing. Grade C.**
Senior AI-engineer contractor rates are quoted at $130 / $165 / $200 (low / mid / high, A.Team) and $155–$235 (Second Talent); architect or CTO-tier work at $200 / $220 / $240+ [S09, S11]. Junior and mid freelance bands are $95–$142 and $119–$185 [S11]. Second Talent's separate LLM-developer page gives the same $155–$235 for seniors and shows no rate trend [S12]. An "AI premium" is claimed at 10–25% (A.Team), 37% over a full-stack baseline (Second Talent) and 34% an hour for AI-work freelancers across Upwork [S09, S11, S56]; UK contract data show about 26% for software roles, yet the same platform says AI skills "do not yet create a significant rate premium" market-wide [S31]. Figures above $300 appear only in agency marketing ranges (Big-4 $300–$600; "fractional AI CTO $200–$500") [S14]. *So what:* P1's $150–$300 is right for asks but its centre of mass is $150–$250; $300 is a stretch tier.

**F3. Europe is lower and flatter, and the UK premium is not rising. Grade B for the UK data, C elsewhere.**
UK GenAI contract day rates quoted in job adverts (six months to 2026-10-20, 900 rates): median £550, P25 £463, P75 £675, P90 £788, roughly £58–£99 an hour at 8 hours a day; the same-period median was £550 in 2025 and £613–£625 in 2024 (two reads) [S30]. Germany's freelancermap survey (n=5,412) averages €103 an hour, €108 for data and analytics, with no AI cut [S27]. France's AI day rate is quoted at €600–€900, and €1,000–€1,500 for gen-AI and agent specialists, by a blog citing Malt, Hays and Free-Work [S32]; the Netherlands averages €83 an hour [S33]. *So what:* price European work from local data in local currency; converting a US card overstates what the market shows.

**F4. India-based providers are quoted at roughly a third to a half of US asks; no realised-rate dataset exists. Grade C, with modelled tax effects (D).**
Vendors quote $50–$75 an hour for senior India-based AI engineers working for international clients (Second Talent), $60–$100 (Navtechy) and $50–$90 for generative-AI work against $120–$200 in the US (Prakash); a payments vendor claims $120–$200 on premium platforms and $50–$80 mid-level direct [S13, S22, S23, S24]. Outliers ($12 an hour "market median" at Flexiple; $61–$85 for US seniors at Lemon.io) were disregarded [S18, S26]. I found no data on rates actually paid to India-based AI consultants by US or European startups, and none on Indian domestic client rates. Payment friction runs from about 1.2% to 5% on Payoneer's own schedule (1% to receive into a non-local-currency account, 1.2–4% to withdraw) to 8–9% on PayPal per a payments vendor [S24, S81]. *Modelled:* an India-resident individual on the presumptive scheme (section 58 of the Income-tax Act 2025, ₹75 lakh with at most 5% cash receipts) falls off it at about $79K of receipts, and net income drops by about $7K as receipts rise from $75K to $80K [S38, S39]. *So what:* plan on $70–$100 an hour for India-based providers until a higher realised rate is evidenced, and get structuring advice before receipts approach the ceiling.

**F5. Retainers are about $8–13K a month for 10–13 hours a week; the brief's example holds only on a 4-week month. Grade A for one published package, C for the rest.**
One firm publishes a Fractional AI Architect package: 8 / 16 / 32 hours a month for $1,800 / $3,400 / $6,400 ($225 / $212.50 / $200 an hour), 3-month minimum, billed monthly in advance, no rollover, with the client supplying a project owner for 2–4 hours a week [S17]. Go Fractional *computes* CAIO retainers of about $9,800 a month, from $7,800 (13 hours × 4 weeks; $13,000 at the P75 ask by my arithmetic), and CTO retainers of $9,000–$15,000 (15 hours × 4 weeks × $150–$250), which are arithmetic and not observed contracts [S01, S02]. Fractionus says US fractional-executive retainers "typically" run $8,000–$22,000 and engagements 6–18 months [S15]; Fractional Jobs' report has 46% of fractionals billing mainly on retainer, a typical posting of about 10 hours a week and engagements of 6–12 months [S06]. For advisory equity, the FAST tiers give a "Standard" advisor 0.25% / 0.20% / 0.15% (idea / startup / growth stage) and "Strategic" or "Expert" advisors 0.3–1.0% [S61]; a CMO-focused source says equity-only deals work only in a narrow band (a pre-revenue company, about four to eight advisory hours a month, an operator with cash flow elsewhere) and otherwise fail within six months [S60]. *So what:* P2 is confirmed in magnitude, but $8,000 for 10 hours a week is $200 an hour only if a month has four weeks; at 52/12 weeks it is $185, and at 12 hours of actual work a week it is $154 (Detailed Findings 2).

**F6. Clients come from networks and referrals; acquisition is the top pain; there is no AI funnel benchmark. Grade C.**
92% of Go Fractional's survey respondents find clients through networks (54% through LinkedIn, 29% through platforms) [S03]; 94% of Fractional Jobs respondents won clients through referrals and 72% found their first client through their personal network [S06]; all 80 consultants in Antenna's 2019 survey of $100K+ earners used their network and most won nothing through platforms [S47]; Consulting Success reports referrals (38%) and networking (18%) behind the highest incomes and 70% of consultants getting zero website leads [S48, S50]. Acquisition is the top challenge for 90% of Go Fractional respondents, 78% of Antenna's, 62% in freelancermap's survey (as compiled by 9am), and 43% of DACH freelancers have no secured workload [S03, S27, S47, S57]. One counter-signal: MBO says 42% of independents name online platforms as their primary way to find work, but that covers all independent work, not senior consulting [S53]. *Not found:* conversion rates by channel for AI work, and any quantified value of open-source or technical-content reputation. *Modelled (D):* two concurrent retainers with a nine-month average life need about 2.7 new retainers a year, which is 8–18 first calls a year at proposal close rates of 70% down to 30%, if half of first calls become proposals (all three inputs assumed; Detailed Findings 4). *So what:* P3's acquisition half is confirmed; build a referral-first funnel.

**F7. The contract norm is a 12-month, 1× fees cap with a higher cap for data; the 3–6 month prior is contradicted; IP carve-outs are standard. Grade A for template text, C for the statistic's scope.**
Common Paper's Professional Services Agreement v1.1 (CC BY 4.0) defaults the general cap to 1× fees paid or payable in the 12 months before the claim, offers an optional "Increased Cap" (default 5×) for privacy, security, confidentiality and similar claims, waives consequential damages (except for Increased Claims and confidentiality breaches), assigns deliverables to the client *excluding* provider pre-existing and third-party materials, and grants a non-exclusive, non-transferable, perpetual, irrevocable licence to use pre-existing materials only as necessary to use the deliverables [S89, S90, S91]. Common Paper's own dataset of more than 10,000 contracts finds 92% of *sales* contracts at 1.0× fees over twelve months and 4% at 0.5× [S92]. I found no source describing 3–6 months as standard. AI-specific commentary adds accuracy disclaimers, a human-oversight acknowledgement, no-training commitments, an AI-specific cap of 12 months' fees and flow-down of model-provider terms [S94, S95]. *So what:* P5 is half right. Use 1× over 12 months as the baseline and treat anything shorter as an opening position that a client may reject.

**F8. Output ownership, EU, Colorado and India rules moved in 2026; contracts should allocate roles, not assume them. Grade B.**
The US Supreme Court denied certiorari in *Thaler v. Perlmutter* on 2026-03-02, leaving the D.C. Circuit's human-authorship requirement in place; prompts alone are generally insufficient (Copyright Office, January 2025) [S98]. The EU Digital Omnibus took effect on 2026-07-27, delaying Annex III high-risk obligations to 2027-12-02 and Annex I to 2028-08-02 [S99]; Article 4 AI literacy remains mandatory in recalibrated form [S100]. Colorado's SB 26-189 (signed 2026-05-14, effective 2027-01-01) replaces SB 24-205, drops the reasonable-care duty and annual impact assessments, keeps developer documentation duties and voids indemnities for one's own discriminatory acts [S101, S102]. India's DPDP Rules were notified on 2025-11-13, with the main fiduciary obligations from 2027-05-13 [S41]. *So what (inferred):* assign "whatever rights exist" in outputs without warranting copyrightability, and state who is the deployer and who keeps documentation.

**F9. Insurance is cheap on paper, but AI-output cover is shrinking. Grade C for prices, B for the exclusions.**
Median annual premiums for small IT consultants are $899 for tech E&O, $1,540 for cyber, $369 for general liability and $638 for a business owner's policy, with typical $1M / $1M limits and a $2,500 deductible [S46] (broker quotes, not AI-specific). Fenwick (2026-06-15) reports the ISO generative-AI exclusion on commercial general liability (January 2026) and some carriers declining AI-output liability under tech E&O, with cyber the most stable line [S96]. *So what:* a liability cap is only as good as the cover behind it. Get AI-output coverage confirmed in writing and size any supercap to the policy limit.

**F10. There is no AI-specific income distribution; the modelled one describes the upper tail. Grade D.**
*Found:* no source gives percentiles for independent AI practitioners. Proxies cover all freelancers or all consultants: Upwork's median for full-time skilled freelancers is $85,000 (data year not stated by the aggregator, probably 2024) [S55]; Consulting Success's monthly gross bands imply roughly $29K (P25) and $84K (P50) a year for consultants in general, by my linear interpolation [S49]; MBO counts 5.8M of 74.9M independents earning $100K+, at most about 21% of the 27.6M full-time independents (MBO's 2025 count; I did not find a 2026 count) [S54, S55]. *Modelled:* for US practitioners with traction, net after overhead, health insurance and federal tax is $83K / $105K / $130K / $160K (P25/P50/P75/P90) on $135K / $167K / $205K / $245K revenue. Mixing in entrants who stall (30%, 45%, 60%) moves P25 to $38K, $24K and $19K and P50 to $87K, $68K and $39K, but P75 and P90 stay within $94–$130K and $131–$160K. The modelled share earning $120K a year or more is 47% at a 45% mix and 35% at a 60% mix, bracketing Consulting Success's 42% of specialists and 37% of all consultants earning $10K a month or more [S49]. India-resident base case ($70 an hour median): $38K / $53K / $64K / $85K. *So what:* the viable-only table overstates; use the planning range. P75 and P90 depend on rate and traction; P25 depends on whether you get traction at all.

**F11. Failure modes are real but thinly evidenced; return-to-employment is unresolved. Grade C.**
Gartner *forecasts* that over 40% of agentic-AI projects will be cancelled by the end of 2027 and that only about 130 of thousands of agentic vendors are real [S62]; the "95% of GenAI pilots fail" headline rests on a small sample and a narrow failure definition [S63]. Deloitte refunded over A$97,000 of a roughly A$440,000 Australian government contract after AI-generated errors [S64]. Scope creep is the top retainer-profitability problem for 59 of 115 agencies in an SE Ranking survey, seen only through an aggregator [S58]. AI efficiency threatens hourly billing: 98% of Fractional Jobs respondents say AI made them more efficient [S06], Upwork reports gen-AI and creative per-contract earnings down 13% even as contract starts rose 90% [S56], and the UK GenAI median fell from £613–£625 (2024, two reads) to £550 [S30]. Return to employment: no behavioural data found. Intent figures (90% not interested in returning, 84% would be self-employed again, 78% plan to continue) are intent, not behaviour: the first comes from a sponsor-run sample of 810 active, 235 past and 688 aspiring fractionals (the page does not say which group the 90% covers) and the others from current independents, so survivorship bias is likely [S06, S28, S54]; Consulting Success says over half of consultants regain their prior employee income within two years [S50], which is not the same as staying. Demand signals conflict: Go Fractional labels CAIO demand "falling sharply" and CTO demand "rising sharply", while Fractional Jobs' sponsor release claims hiring up 149% year on year [S01, S02, S07]. *So what:* P3's scope-creep half has only secondary support; P4 cannot be settled from what I found.

**F12. Platform fees that vendors publish are low; the costs that matter are markup, non-circumvention terms and rate suppression. Grade A for self-reported fees, C for estimates.**
Upwork's freelancer fee is a variable 0–15% per contract, shown before the proposal [S66] (it replaced the 20/10/5% tiers on 2025-05-01, per a third-party explainer [S67]). Toptal charges talent nothing and lets them set their rate, with client markup undisclosed [S68]. Braintrust lets talent keep 100% on their own clients [S71]. Go Fractional membership is free [S04]. Bonsai's plans are $9–$49 per user per month on annual billing, with contracts and invoicing from the Essentials plan up [S77]. Stripe Invoicing charges 0.4% or 0.5% per paid invoice plus processing [S79]. Estimates (C): Toptal client markup 30–50%, Braintrust client-side 10–15%, Catalant 20–30% of total fees (a 25–43% markup on the expert's fee), Contra 0% commission with Pro at $29 a month [S69, S72, S74, S75]. Not retrievable: fractionaljobs.io and contra.com/pricing (blocked), FSuite (searched, nothing found), and official Braintrust and Catalant fee statements. *So what:* use marketplaces as a supplementary channel and read non-circumvention terms before signing.


## Recommendation

Everything in this section is design judgment (Grade D) built on the cited evidence. None of it is an observed market practice unless an [S##] says so. It is written for a US-market practitioner, with the India-based variant in item 8.

**1. Lead with a capacity retainer, priced on 52/12 weeks.**
Sell the Fractional Head of AI role as a monthly retainer for 10–13 hours a week at $200–$225 an hour, which is **$8,700–$12,700 a month** (hours × 4.33 × rate; the matrix is in Detailed Findings 2). Pricing on a 4-week month, as vendor calculators do [S01], gives away about 8% of the fee. Anchors: Vantage Point's published tiers at $200–$225 an hour [S17], Go Fractional's asking corridor of $150–$250 [S01, S02] and Fractionus's $8–22K range [S15]. Terms: 3-month minimum, billed monthly in advance, an hours cap with a stated overage rate, no rollover, 30-day notice after the minimum, and a client project owner for 2–4 hours a week [S17, S60].

**2. Put a fixed-fee sprint at the front of the funnel.**
Offer a 2–6 week diagnostic or pilot at a fixed fee of estimated hours × list rate × 1.2–1.25. The multiplier covers the model's 20% unbilled-leakage case (1 + 0.20) with a margin. Convert the sprint to a retainer afterwards. A fixed fee keeps the benefit of AI-assisted delivery, which hourly billing hands to the client (item 7). The evidence for value-based pricing is weak: 51% of value-based pricers against 39% of hourly pricers report $10K+ average projects, self-reported by a coaching business [S50].

**3. Start from Common Paper PSA v1.1 and make nine changes.**
Base: [S89]. (a) General cap of 1× fees paid or payable under the SOW in the prior 12 months; open at 6 months only if you will concede to 12. (b) A supercap for confidentiality and data-security breaches at the lesser of 5× fees and your insurance limit [S91, S94]. (c) Keep the consequential-damages waiver (the template excepts Increased Claims and confidentiality breaches). (d) List your pre-existing materials (agent harnesses, orchestration code, prompt templates, evaluation suites) in a schedule with the embedded-use licence [S89]. (e) Assign deliverables on payment, not as work made for hire [S97]. (f) Add the AI clauses: accuracy disclaimer, human review, no training on client data, flow-down of model-provider terms [S94, S95]; and take AI Output out of the template's non-infringement warranty and indemnity [S89]. (g) Use change orders and the hours cap to contain scope creep [S89]. (h) Allocate the deployer role and compliance documentation to the client where EU or Colorado rules apply [S99, S101]. (i) Ask for permission to cite the client as a reference. (j) Write the retainer's 3-month minimum and 30-day notice into the SOW, because the template allows termination for any reason only when no SOW is active, and expect to refund unearned prepaid fees on termination [S89]. Sample wording is in Detailed Findings 5.

**4. Insure, and check the AI exclusion.**
Hold tech E&O and cyber (median quotes $899 and $1,540 a year [S46]) and ask the broker in writing whether claims arising from AI-generated output are covered [S96]. If they are not, keep the AI-output cap at 1× fees and refuse a supercap for output accuracy.

**5. Source clients referral-first.**
Spend the first 90 days on your own network (former employers, colleagues, founders you have worked with), the sprint offer and two or three proof engagements. Add Go Fractional (free membership [S04]) and one or two networks as secondary channels. Use bidding platforms only to fill utilisation: agency-sourced work paid about half in the one dataset that measured it (Antenna 2019: $113 against $223 an hour [S47]), and Upwork reports gen-AI and creative per-contract earnings down 13% [S56]. The modelled volume needed to sustain two retainers is low (8–18 first calls a year), so relationship quality matters more than lead volume.

**6. Set a viability gate before leaving employment.**
Go when (a) you can see about 900–1,000 paid hours of committed or highly likely work in year one (two retainers at 10 hours a week for 48 weeks is 960); (b) you hold at least six months of living costs, because the modelled first-year ramp (3 months at 10% utilisation, 3 at 40%, 6 at 60%) gives net $52K / $71K / $92K at P25 / P50 / P75 against $83K / $105K / $130K in a steady year; and (c) you can accept a P25 near $38K, or $19–24K if the outside view is right (Detailed Findings 7). If after 90 days you hold neither a signed retainer nor two outstanding sprint proposals, move to part-time consulting or back to employment.

**7. Do not sell hours as the unit of value.**
If AI cuts delivery time by 30%, an hourly biller needs a 43% higher rate to hold revenue; at 50% fewer hours the rate must double (Detailed Findings 2). Price capacity (retainer) or outcomes (sprint), and review rates every six months against the Go Fractional benchmarks [S01, S02].

**8. If you are India-based and selling to US or European clients.**
Quote in USD at $70–$100 an hour until you have evidence of a higher realised rate, then test $120 and above with a few clients (the model's upside case; no dataset supports it). Receive through Wise or Payoneer, not PayPal [S24, S80, S81]. Before receipts approach ₹75 lakh (about $79K) ask a chartered accountant whether your work qualifies for the presumptive scheme in section 58, what the tax is just above the ceiling, and how export-of-services GST applies (one accounting blog reports zero-rating under a Letter of Undertaking and a ₹20 lakh registration threshold, Grade C [S34]) [S38, S39]. Include data-protection terms that follow the DPDP timeline [S41].

**9. Tool stack.**
Contract: Common Paper PSA v1.1, free under CC BY 4.0 [S89]. Invoicing: Stripe Invoicing at 0.4% or 0.5% per paid invoice plus processing [S79], or Bonsai Essentials at $19–$25 per user per month for contracts and invoices [S77]. Foreign receipts: Wise or Payoneer. Profile and job board: Go Fractional. Skip Docracy, which is legacy [S82]. Treat Toptal, Braintrust and Catalant as optional, because their client-side fees are undisclosed or estimated [S68, S70, S73].

**What would change this recommendation.** (i) A transaction-level dataset, such as anonymised invoices from a billing platform, showing realised AI retainer rates well below $150 an hour. (ii) Evidence that AI-output claims are uninsurable for solo providers. (iii) Evidence that caps of 3–6 months are routinely accepted in consulting contracts. (iv) Tax advice that the Indian presumptive scheme does not apply to AI consultancy. (v) Behavioural data showing that most independents return to employment within two years.

## Alternatives Considered

| Alternative | Case for | Case against (evidence) | When I would choose it |
|---|---|---|---|
| Marketplace-first (Upwork, Toptal, Braintrust, Catalant) | Fast start, vetting, escrow and payments handled | Agency-sourced work paid about half [S47]; Upwork gen-AI per-contract earnings −13% [S56]; Toptal markup estimated at 30–50% and reported non-circumvention terms [S69]; most Go Fractional respondents (92%) win through networks [S03] | The first 90 days, to fill utilisation while the referral funnel builds |
| Pure hourly time-and-materials | Simple; hourly pricing dominates in Go Fractional's survey [S03]; 51% of Antenna's consultants used it [S47] | Penalises AI efficiency (30% fewer hours needs a 43% higher rate); overrun risk sits with you | Short or undefined work, at $200 an hour or more |
| Fixed-fee or value-based projects | 51% of value-based pricers report $10K+ projects against 39% of hourly pricers (self-reported) [S50] | Scope-creep exposure; needs estimating skill; modelled leakage of 5–20% cuts net income P50 from $119K to $98K across the no-leakage and 20%-leakage cases (Detailed Findings 7) | Well-scoped sprints with a change-order clause |
| Equity-heavy advisory | Upside: 0.25% of a $50M exit is $125K before dilution (modelled) | FAST tiers are 0.15–1.0% [S61]; equity-only deals fail within six months outside a narrow band [S60]; no outcome data found | Only alongside a cash retainer near market, with 2-year vesting and a 3-month cliff [S61] |
| Boutique agency (2–5 people) | Leverage beyond your own hours | Boutique gross margin averages 20–40% (self-reported) [S50]; adds payroll, bench and management risk; scope creep hits retainers hardest [S58] | After two or more retainers are stable and you can hire against signed work |
| Stay employed and consult part-time | Keeps salary and benefits; tests demand cheaply | Caps paid hours; some employment contracts restrict outside work (recalled, D) | The default if you cannot see 900 paid hours |
| Template choice: Common Paper vs Bonterms vs Freelancers Union vs bespoke | Common Paper is free, open (CC BY 4.0), has primary-source defaults and statistics [S89, S92] | Bonterms standard terms were not retrieved and its licence is shown inconsistently [S88]; the Freelancers Union tool is a beta generator with no IP clause mentioned [S83]; bespoke drafting costs legal fees | Common Paper as the base; a lawyer to review the schedule of pre-existing materials |


## Detailed Findings

### 1. Rate cards by geography and tier

All rates in this section are asked, advertised or computed rates (Grade C unless stated). None is a transacted rate. The recommended operating card at the end of the section is inferred (Grade D).

#### 1.1 United States

| Tier | Second Talent: US freelance AI engineer [S11] | A.Team: low / mid / high [S09] | Other sources |
|---|---|---|---|
| Junior | $95–$142 | n/a | n/a |
| Mid | $119–$185 | n/a | n/a |
| Senior (production LLM work) | $155–$235 | $130 / $165 / $200 | Second Talent's LLM page: senior US freelance $155–$235, no trend shown [S12]; Go Fractional survey average across fractional roles $153 [S03] |
| Architect, CTO-tier, fractional leader | n/a | $200 / $220 / $240+ | Go Fractional asks: CAIO $190–$208, CTO $209–$212 (two reads), P25–P75 $150–$250 [S01, S02]; Fractional Jobs mean hourly for all executives $223, engineering $229 [S06]; Go Fractional survey: CAIO $218, architect $217, CTO $211 [S03] |
| Boutique or agency | n/a | n/a | Boutique $150–$300; Big-4 $300–$600; offshore AI-first $22–$50 [S14] |

A.Team's "low / mid / high" labels are not stated percentiles; the model uses its mid ($165) and high ($200) as the median and P75 of realised rates. Lemon.io's $61–$85 for US senior LLM developers [S18] and Fiverr's $10–$125 for AI strategy consultants [S19] are commodity-marketplace outliers and were not used.

**Asking versus offered (Go Fractional live benchmarks, read about 2026-10-20 and again on 2026-10-25) [S01, S02]:**

| Role and read | Talent asks: average (P25–P75) | Employer offers: average (P25–P75) | Offers ÷ asks | Posts / profiles in 90 days | Typical hours a week | Demand label |
|---|---|---|---|---|---|---|
| Fractional CAIO, first read | $208 ($150–$250) | $189 ($130–$250) | 0.91× | 6 / 326 | 13 | "falling sharply" |
| Fractional CAIO, second read | $190 ($150–$250) | $125 ($93–$150) | 0.66× | 10 / not stated | 13 | "falling sharply" |
| Fractional CTO, first read | $212 ($160–$250) | $129 ($96–$145) | 0.61× | 19 / 1,042 | 15 | "rising sharply" |
| Fractional CTO, second read | $210 ($150–$250) | $124 ($90–$130) | 0.59× | 17 / 1,116 | 15 | "rising" |

"Employer offers" are rates in live listings; "talent asks" are rates candidates set on their profiles. On the second read the CAIO page gave one asking figure (average $190, median $180) without separating profile asks, and showed no update date; the CTO page was dated 2026-10-24. The CAIO offered rate moved from $189 to $125 as postings rose from six to ten, which shows how unstable a sample this small is: read the CAIO ratio as 0.66–0.91× and the CTO ratio as about 0.6×.

**The AI premium.** Claims: 10–25% on contractor hourly rates (A.Team's key takeaways; its body text says roughly 10–15% for senior contractors and 20–30% for architects [S09]), 37% for AI/ML engineers over a full-stack baseline (Second Talent [S11]), 34% an hour for AI-work freelancers (Upwork Future Workforce Index, platform-wide, n=2,400 US skilled workers [S56]), about 26% for UK software contractors and 17% for project management (YunoJuno [S31]). Against that, YunoJuno states that AI skills "do not yet create a significant rate premium" market-wide, and Upwork reports gen-AI and creative per-contract earnings down 13% even as contract starts rose 90% [S31, S56]. The premium is real in some segments and absent in others; it is not a uniform multiplier.

#### 1.2 Europe

**UK GenAI contract day rates**, quoted in job adverts over the six months to 2026-10-20 (900 rates) [S30]; hourly equivalents are my arithmetic at 8 hours a day:

| Percentile | Day rate | At 8 hours a day |
| --- | --- | --- |
| P10 | £400 | £50 |
| P25 | £463 | £58 |
| Median | £550 | £69 |
| P75 | £675 | £84 |
| P90 | £788 | £99 |

London median £575. The same-period median was £550 in 2025 and £613–£625 in 2024 (two reads of the live page). These are contract-role adverts, not signed contracts, and are not tiered by seniority; I treat the percentile ladder as a rough proxy for tiers (inferred, D). YunoJuno's booking data (more than 182,000 data points) put UK average day rates at £566 for cloud, £533 for software, £521 for product and £518 for strategy, with over 80% of bookings made directly rather than through agencies [S31].

**Other countries.** Germany: freelancermap's 2026 survey (n=5,412, DACH, fielded November 2025 to February 2026) gives an average of €103 an hour, €108 for data and analytics, a 42-hour working week, and 43% of respondents without secured workload; the income label (net or gross) is ambiguous, so I did not use its income figures [S27, S28]. The 2025 edition reported €104 [S29]. France: AI day rate (TJM) €600–€900 "confirmed", €1,000–€1,500 for generative-AI and agent specialists, IT average €520 [S32]. Netherlands: €83 an hour [S33]. No source separates Heads of AI or fractional leaders in any European country, and no European retainer data was found.

#### 1.3 India-based providers selling to international clients

| Tier | Second Talent [S11, S13] | Navtechy (freelance) [S22] | Other |
|---|---|---|---|
| Junior (0–2 years) | $25–$35 contract; $31–$44 freelance | $15–$25 | Upwork India beginners $10–$25 [S25] |
| Mid | $28–$72 (about $4,480–$11,520 a month at 160 hours) | $30–$50 | Mid-level direct $50–$80 [S24] |
| Senior | $50–$75 (international clients) | $60–$100 | Generative-AI work $50–$90 against USA $120–$200 [S23]; $120–$200 on premium platforms, unverified [S24] |

Second Talent adds that freelance rates run about 25% above contract rates [S13]. The model uses a median of $70 an hour (P75 $100) as the base case and a median of $120 (P75 $160) as an upside "US-positioned" case; the upside has no dataset behind it. Flexiple's $12 an hour "market median" is derived from salaries and was disregarded [S26].

**Not found:** rates paid to India-based AI consultants by US or European startups (no dataset), and rates paid by Indian domestic clients to AI consultants (no source at all). The figures above are what India-based talent is quoted at for foreign clients, mostly by vendors that sell that talent.

#### 1.4 Retainer cards that exist

| Source | Offer | Price | Effective rate | Grade |
|---|---|---|---|---|
| Vantage Point [S17] | Fractional AI Architect, 8 hours a month | $1,800 | $225 an hour | A (one firm's own price) |
| Vantage Point [S17] | 16 hours a month | $3,400 | $212.50 | A |
| Vantage Point [S17] | 32 hours a month | $6,400 | $200 | A |
| Go Fractional [S01] | Fractional CAIO, 13 hours a week | About $9,800 a month, from $7,800 (page); $13,000 at the P75 ask (my arithmetic) | $150–$250 | C |
| Go Fractional [S02] | Fractional CTO, 15 hours a week | $9,000–$15,000 a month (computed) | $150–$250 | C |
| Fractionus [S15] | US fractional executives, all roles | $8,000–$22,000 a month | not stated | C |
| Groovy Web [S14] | Fractional AI CTO, 1–3 days a week | $6,000–$20,000 a month | not stated | C (agency marketing) |
| A.Team [S10] | Fractional CTO, "10–15 hours" to "40+ hours" a month | $4,000–$40,000 a month | implies $250–$1,250 | Excluded: the monthly-hours units contradict every weekly-hours source |

A unit warning from an adjacent market: a CMO-focused source puts the median fractional retainer at $10,000–$12,000 a month for 15–25 hours a month, about $400–$800 an hour by my arithmetic, while the same site cites Go Fractional's typical scope in hours a week [S60]. Always ask whether hours are per week or per month.

#### 1.5 Project and billing-model evidence (weak)

| Source | Offer | Price | Grade |
|---|---|---|---|
| Softude [S21] | AI roadmap or strategy engagement | from about $15,000 | C (vendor marketing) |
| Alice Labs [S20] | Project pricing by tier | $20,000 to $2M+ | C (vendor marketing) |
| Fiverr [S19] | AI agent development, marketplace low end | about $295 per fixed project | C |
| Consulting Success [S50] | Most common average consulting project value | $5,000–$15,000 and $15,000–$50,000 (33% in the second band; 6% above $100,000) | C |

Billing mix: 51% time-and-materials, 30% fixed fee and 19% retainer among 80 consultants earning $100K+ (Antenna, 2019) [S47]; 46% of Fractional Jobs respondents bill mainly on a monthly retainer [S06]; Go Fractional's survey says hourly pricing dominates and that the best relationships are retainer-based, billed upfront, with a term of three months or more [S03]. 13% of consultants use monthly retainers according to an aggregator [S58]. No source gives AI-specific project price points from named, independently verified engagements.

#### 1.6 Recommended operating card (inferred, Grade D)

Built from the sourced bands above. It is a starting list price, not a market statistic.

| Offer | US-market clients | Europe | India-based provider selling to US or EU |
|---|---|---|---|
| Senior hands-on engineering, time-and-materials | $175–$225 an hour list; floor $150 (inside Second Talent's $155–$235 and Go Fractional's $150–$250 corridor) | UK £675–£790 a day (P75–P90 of adverts); Germany €100–€130 an hour (average €103); France €800–€1,200 a day (inside the quoted €600–€1,500) | $70–$100 an hour; test $120 and above only with evidence |
| Architect or fractional-leader hourly | $225–$275 an hour list | No source; do not extrapolate | $100–$150 an hour is a hypothesis with no data behind it |
| Fractional Head of AI retainer, 10–13 hours a week | $8,700–$12,700 a month (matrix below) | Price as local day rate × days a week × 4.33; no European retainer data found | At $70–$100 an hour, $3,000–$5,600 a month on the same formula |
| Advisory block | 8 / 16 / 32 hours a month at about $1,800 / $3,400 / $6,400 (Vantage Point's published tiers [S17]) | n/a | n/a |
| Fixed-fee sprint (2–6 weeks) | Estimated hours × list rate × 1.2–1.25 | Same formula in local rates | Same formula |

### 2. Retainer matrix, overruns, equity and AI-efficiency arithmetic

All arithmetic in this section is mine (Grade D) unless a source is cited.

**2.1 Matrix on the vendor convention** (monthly fee = hours a week × 4 × hourly rate, as Go Fractional computes it [S01, S02]):

| Hours per week | $150/h | $175/h | $200/h | $225/h | $250/h | $300/h |
|---|---|---|---|---|---|---|
| 5 | $3,000 | $3,500 | $4,000 | $4,500 | $5,000 | $6,000 |
| 8 | $4,800 | $5,600 | $6,400 | $7,200 | $8,000 | $9,600 |
| 10 | $6,000 | $7,000 | $8,000 | $9,000 | $10,000 | $12,000 |
| 13 | $7,800 | $9,100 | $10,400 | $11,700 | $13,000 | $15,600 |
| 15 | $9,000 | $10,500 | $12,000 | $13,500 | $15,000 | $18,000 |
| 20 | $12,000 | $14,000 | $16,000 | $18,000 | $20,000 | $24,000 |

**2.2 Recommended matrix on a 4.33-week month** (monthly fee = hours a week × 52/12 × hourly rate). A calendar month averages 4.33 weeks, so the 4-week convention delivers only 92.3% of the nominal hourly rate if the client expects the weekly hours every calendar week (a $200 rate becomes $184.62; $150 becomes $138.46):

| Hours per week | $175/h | $200/h | $225/h | $250/h |
| --- | --- | --- | --- | --- |
| 5 | $3,792 | $4,333 | $4,875 | $5,417 |
| 8 | $6,067 | $6,933 | $7,800 | $8,667 |
| 10 | $7,583 | $8,667 | $9,750 | $10,833 |
| 13 | $9,858 | $11,267 | $12,675 | $14,083 |
| 15 | $11,375 | $13,000 | $14,625 | $16,250 |
| 20 | $15,167 | $17,333 | $19,500 | $21,667 |

**2.3 Overrun.** The brief's example, $8,000 a month for a nominal 10 hours a week, depends on hours staying at the cap:

| Hours actually worked per week | Realised $/h (4-week month) | Realised $/h (52/12-week month) |
|---|---|---|
| 10 | $200 | $185 |
| 11 | $182 | $168 |
| 12 | $167 | $154 |
| 13 | $154 | $142 |
| 14 | $143 | $132 |

At 12 hours of actual work a week the same retainer earns $167 an hour on the 4-week convention and $154 on 52/12 weeks, a 17–23% cut to the nominal $200. This is the arithmetic behind the hours cap and overage clause.

**2.4 Advisory equity.** The FAST tiers [S61] (fully-diluted basis not confirmed; usual vesting is two years with a three-month cliff; Carta's observed grants are mostly 0.2–1.0%):

| Company stage | Standard | Strategic | Expert |
|---|---|---|---|
| Idea | 0.25% | 0.50% | 1.00% |
| Startup | 0.20% | 0.40% | 0.80% |
| Growth | 0.15% | 0.30% | 0.60% |

The brief's 0.25% therefore matches the idea-stage "Standard" tier. **Modelled arithmetic, no probabilities attached:** 0.25% of a $10M, $50M or $200M exit equity value is $25,000 / $125,000 / $500,000, before dilution, vesting, liquidation preferences and tax. A CMO-focused source reports that equity-only arrangements work only in a narrow band (a pre-revenue company, about four to eight advisory hours a month, an operator with cash flow elsewhere) and otherwise fail within six months [S60]; I found no outcome data on advisory equity for AI leaders.

**2.5 AI efficiency and hourly billing.** If AI cuts the hours needed to deliver a fixed outcome, an hourly biller must raise the rate by 1/(1 − s) − 1 to hold revenue, where s is the share of hours saved:

| If AI cuts delivery hours by | Hourly rate must rise by | …to hold revenue flat |
|---|---|---|
| 20% | +25% | e.g. $165 → $206 |
| 30% | +43% | e.g. $165 → $236 |
| 50% | +100% | e.g. $165 → $330 |
| 70% | +233% | e.g. $165 → $550 |

Fractional Jobs' respondents report 98% efficiency gains from AI (62% "substantial") and 30% say they serve more clients because of it [S06]. Hours saved can be re-sold to more clients (utilisation up) or discounted by clients (rate down); the evidence on which dominates is mixed (Finding 11).

**2.6 Hours a week.** Go Fractional's typical scope is 13 hours for a CAIO and 15 for a CTO [S01, S02]; a typical Fractional Jobs posting calls for about 10 hours a week, and the median fractional worker bills 21 client-facing hours a week with 64% serving two or more clients [S06]. 91% of Fractional Jobs respondents do hands-on execution rather than advice alone [S06].


### 3. Fractional Head of AI: engagement structure

#### 3.1 What the sources support

*Found.* One firm's published package is the only primary-source structure: hours blocks of 8, 16 or 32 a month, a 3-month minimum, billing monthly in advance, no rollover, acceptance by a monthly hours statement, a client-supplied project owner for 2–4 hours a week, and client approvals within 3 business days; it states no notice terms [S17]. Market patterns, all Grade C: typical scope 13 hours a week for a CAIO and 15 for a CTO [S01, S02]; a typical Fractional Jobs posting asks for about 10 hours a week, and engagements run mostly 6–12 months (60% last six months or longer) [S06]; Fractionus says 6–18 months [S15]; Go Fractional's survey says the best relationships are retainer-based, billed upfront, for three months or more [S03]; a CMO-focused source describes a six to 12 month initial term converting to month-to-month with 30 days' notice, with early exits driven by mismatches in scope, compensation and measurement [S60]. 91% of Fractional Jobs respondents do hands-on execution, so a "Head of AI" is usually also building something [S06]. Go Fractional's materials name weekly bandwidth, overage rates, 30/60/90 plans, decision rights and renewal triggers as the structuring items; I could not read its playbook, which returned only a script shell [S05]. I found no public Head-of-AI contract text and no equity terms specific to AI leaders.

#### 3.2 Proposed term sheet (inferred, Grade D)

| Term | Proposed position | Basis |
|---|---|---|
| Role | Owns AI strategy and the use-case portfolio; sets architecture and evaluation standards; advises on build, buy and vendors; coaches the team. Hands-on build work goes in a separate SOW | 91% do hands-on work [S06]; keeps scope and liability separable |
| Hours | Cap of 10–13 hours a week, tracked weekly; overage at list rate with written pre-approval; no rollover | Typical scope [S01]; Vantage Point [S17] |
| Fee | $8,700–$12,700 a month (Detailed Findings 2.2), billed monthly in advance | Matrix; Go Fractional and Vantage Point [S01, S17] |
| Term | 3-month minimum, then month-to-month on 30 days' notice; no automatic renewal inside the minimum | [S17, S60] |
| Client owner | Named project owner for 2–4 hours a week; approvals within 3 business days | [S17] |
| Acceptance | Monthly hours statement plus a deliverable and decision log | [S17] |
| Reporting | Weekly written update; monthly steering review; quarterly roadmap refresh | Design |
| Equity (optional) | Only on top of a near-market cash retainer; 0.15–0.25% (Standard tier); 2-year vesting, 3-month cliff | [S60, S61] |
| Exclusivity and conflicts | No exclusivity; disclose other clients in the same sector; accept at most a narrow employee non-solicit if asked (Common Paper's PSA has none) | [S89]; design |
| Termination | After the 3-month minimum, either side may end the SOW for convenience on 30 days' notice (write this into the SOW: the PSA lets either party end the agreement for any reason only when no SOW is active, §5.2(c)); for cause with a 30-day cure period (§5.2(a)); unearned prepaid fees are refunded pro rata unless you end the SOW for the client's uncured breach (§5.3(e)) | [S89]; [S17, S60]; design |
| Data and access | Client-issued accounts, least privilege; consultant holds no production credentials unless the SOW says so; AI tools used on client material must have no-training terms | [S95]; design |
| Insurance | Tech E&O and cyber held; certificate on request | [S46, S89] |

#### 3.3 Deliverables by phase (inferred, Grade D)

| Phase | Deliverables |
|---|---|
| Days 0–30: baseline | Inventory of AI use, data, tools and spend; stakeholder interviews; regulatory and privacy screen (EU AI Act role, Colorado where relevant, data protection); three to five use cases scored on value, feasibility and risk; quick-win recommendation; 30-day readout |
| Days 31–60: operating model | Acceptable-use and data-handling policy; evaluation and red-team standard for LLM features; build, buy or partner decisions and vendor shortlist; reference architecture with a model-provider and deprecation strategy; pilot selection and kickoff; hiring plan and role definitions |
| Days 61–90: delivery and hand-off | Pilot readout with KPIs and cost model; 12-month roadmap and budget; vendor-negotiation support; team enablement sessions; renewal decision memo |
| Standing | Weekly update; monthly hours statement; decision log; quarterly roadmap refresh; executive or board briefing on request |

#### 3.4 Decision rights (inferred, Grade D)

| Decision | Head of AI | Client executive | Client project owner |
|---|---|---|---|
| Use-case priority and AI strategy | Recommends | Approves | Consulted |
| Architecture and evaluation standards within budget | Decides | Informed | Consulted |
| Vendor and model selection | Recommends and shortlists | Approves and signs | Consulted |
| Budget and headcount | Advises | Decides | Informed |
| Risk acceptance and regulatory classification | Advises | Decides (the deployer) | Informed |
| Technical hiring | Runs the technical interview loop | Decides | Consulted |
| Production access and credentials | Not held by default | Grants | Administers |

#### 3.5 Renewal triggers at day 75 (inferred, Grade D)

Renew when (a) at least one pilot has a measured KPI against its baseline, (b) a named internal owner can run the roadmap, (c) a hiring plan or budget is approved, and (d) the client has used at least 70% of the contracted hours, because underuse is a churn signal. If (a) to (c) fail, offer a smaller advisory block (8–16 hours a month) or end the engagement; early exits in the one source that discusses them came from scope, compensation and measurement mismatches [S60].


### 4. Client acquisition: evidence, playbooks and the modelled funnel

#### 4.1 What the surveys say (all Grade C unless noted)

| Source | Sample | Finding |
|---|---|---|
| Go Fractional survey, April 2026 [S03] | n=213 fractionals; vendor-run | 92% find clients through networks, 54% through LinkedIn, 29% through platforms; 90% name acquisition the biggest challenge |
| Fractional Jobs report 2026 [S06] | n=1,733; sponsor sells fractional talent | 94% won clients through referrals; 72% found their first client through their network; 38% say AI expertise helped them win work |
| Antenna 2019 [S47] | 80 consultants earning $100K+; selected on success | All 80 use networking and 1-on-1 meetings for leads; 39 events, 30 speaking, 26 blogging, 7 SEO; most won nothing through online talent platforms; 60% have a website and only 14% of those get meaningful inquiries; 78% name business development a top-three pain |
| Consulting Success [S48, S50] | List of more than 50,000 consultants; responses unreported; sells coaching | Methods that win the *most clients*: phone 16%, direct mail 15%, networking 14%, joint ventures 12%, referrals 8%, blogging and SEO 7%, LinkedIn 4%. Method behind the *highest income* (2019 data): referrals 38%, networking 18%. 70% get zero website leads; 88% do not list fees on their site |
| Landenwitsch [S52] | Newsletter survey, n unstated; non-profit and social-impact consultants | About 80% of engagements from personal networks |
| MBO Partners 2025 [S53] | US independents (all kinds of work) | 42% name online platforms as their primary way to find work |
| 9am compilation [S57] | Compiles MBO, YunoJuno, freelance.de, freelancermap | Platform use rose from 37% to 63% of independents (2020–2025); more than 80% of YunoJuno bookings are direct; 26% need over three months to land a project and 3% within a week (freelance.de) |
| freelancermap Kompass 2026 [S27] | n=5,412, DACH, B | 43% have no secured workload; 85% use AI tools |

Volume and income point in different directions: the channels that produce the *most* clients (outbound phone, direct mail) are not the ones behind the *highest* income (referrals, networking). Platforms are the most used channel among independents generally (MBO) but not the best-paid one for senior consultants.

#### 4.2 Sustainable and high-margin versus commoditised

Direction of the evidence: the further the channel is from the end client, the lower the rate.

| Share of revenue from a staffing agency or consulting firm [S47] | 0% | 1–20% | 21–40% | 41–60% | 61–80% | 81–99% | 100% |
|---|---|---|---|---|---|---|---|
| Average hourly rate in the sample | $223 | $190 | $174 | $137 | $131 | $115 | $113 |

That is a 49% drop from fully direct to fully agency-sourced work (2019 data, n=80, selected on success; the model's "agency-dependent" stress uses ×0.51). Consistent signals: Upwork reports gen-AI and creative per-contract earnings down 13% [S56]; marketplace low-end AI agent builds list at about $295 per fixed project [S19]; Toptal's client markup is estimated at 30–50% and Catalant's fee at 20–30% of total fees [S69, S74], which sit between you and the client's budget. No source gives AI-specific win rates or margins by channel.

#### 4.3 Playbooks (inferred, Grade D)

These are syntheses of the evidence above and ordinary practice. None is a benchmarked playbook; the sources found no AI-specific conversion data.

**A. Warm-network retainer (primary).**
1. List about 100 contacts in four rings: former managers and colleagues now at director level or above, founders and investors you have worked with, peers at adjacent consultancies, and past clients.
2. Make two personal outreaches a week offering a 45-minute AI-readiness teardown, free or for a small fee, with a one-page written output.
3. Send a fixed-fee sprint proposal within 48 hours of any call that surfaces a concrete problem.
4. At day 60 of any engagement, ask for two introductions and for permission to cite the client.
5. Target (modelled): 8–18 first calls a year sustain two concurrent retainers (4.4); two a month leaves a buffer.
Anchor: referral and network dominance [S03, S06, S47].

**B. Productised ladder.** A 1–2 week diagnostic, then a 2–6 week pilot sprint at a fixed fee, then the retainer. The ladder shortens the trust gap for clients who have not bought from a solo provider; the sprint price is estimated hours × list rate × 1.2–1.25. Anchor: value-based pricers report larger projects (self-reported) [S50].

**C. Network and marketplace placement (secondary).** Go Fractional's free profile and job board [S04]; Fractionus accepts under 3% of applicants and quotes $8–22K retainers [S15]; Fractional Jobs is described by a competitor as free of platform fees [S16]; Toptal charges talent nothing [S68]; Braintrust lets talent keep 100% on clients they bring [S71] and, per directories, charges clients 10–15% [S72]; Catalant's winning experts typically have 10–20 years' experience [S73] and its fee is estimated at 20–30% of total fees [S74]. Use them to fill gaps, and read non-circumvention terms before accepting work [S69]. Expect rate compression against direct work (4.2).

**D. Agency and partner subcontracting (floor).** Subcontract to one or two boutiques to cover utilisation gaps; price assuming roughly half your direct rate if the agency owns the client relationship [S47], and negotiate the right to cite the work.

**E. Content and open-source reputation (slow, unquantified).** I found no source that quantifies open-source or technical-content reputation as a channel. The only adjacent figures are discouraging for the first year: 70% of consultants get zero website leads [S50] and 14% of Antenna's website owners get meaningful inquiries [S47]. Treat content as a compounding asset that supports referrals (the referrer needs something to forward), not as a funnel.

#### 4.4 Modelled funnel (assumptions, Grade D)

Inputs: two concurrent retainers, a nine-month average engagement (inside the 6–12 month norm [S06]), half of first calls becoming proposals (assumed), and proposal close rates of 30–70% (the range a coaching firm claims for its clients [S51]). Two retainers with a nine-month life need 2 × 12 ÷ 9 = 2.7 new retainers a year:

| Close rate on proposals (assumed) | New retainers needed per year | First calls needed per year | per month |
|---|---|---|---|
| 30% | 2.7 | 18 | 1.5 |
| 50% | 2.7 | 11 | 0.9 |
| 70% | 2.7 | 8 | 0.6 |

The funnel is a relationship funnel, not a volume funnel: fewer than two good first calls a month is enough. The binding constraint is trust and fit, which is why referrals dominate.

#### 4.5 Not found

AI-specific conversion rates by channel; cost per lead or per client by channel; marketplace win rates for AI consulting; any quantified value of open-source or technical-content reputation (searched, nothing quantified); and any dataset on how long it takes an AI consultant to land a first retainer. The only conversion figure is a coaching firm's claim that its clients' proposal close rates rise from about 30% to about 70% [S51], with no sample and no discovery-call conversion.


### 5. MSA protections for a solo AI provider

No source or statute makes any of these clauses "mandatory". The set below is what I judge necessary for a solo provider, anchored to a primary-source template (Common Paper's Professional Services Agreement v1.1, CC BY 4.0 [S89]) and to law-firm commentary. Section numbers are Common Paper's.

#### 5.1 Clause table

| Clause | Position for a solo AI provider | Anchor | Status of the anchor |
|---|---|---|---|
| General liability cap | 1× fees paid or payable under the SOW in the 12 months before the claim | §8.1; default General Cap [S89, S90]; 92% of sales contracts use 1.0× over twelve months and 4% use 0.5× [S92] | A for the default; the statistic covers *sales* contracts and its base is not spelled out. A 3–6 month cap is my opening-position adaptation, not a norm (D) |
| Consequential damages | Mutual waiver of lost profits and of indirect, special and consequential loss; expect clients to ask for carve-outs | §8.2 waiver; §8.3 says the waiver does not apply to Increased Claims or to a breach of confidentiality (§11) [S89] | A. The sample clause below leaves out the §8.3 carve-outs, which favours the provider (D) |
| Supercap | For confidentiality and data-security breaches: the lesser of 5× fees and your E&O and cyber limits. Exclude AI-output accuracy | Increased Cap, default 5×, typically for privacy, security, confidentiality [S91]; customers ask for supercaps on IP indemnity, confidentiality and data security [S94] | A for the default; B for the customer-side expectation; lesser-of formula is mine (D) |
| Unlimited claims | Keep the list short. The template treats a claim as Increased or Unlimited, never both; its help article gives no examples of Unlimited Claims and lists gross negligence and wilful misconduct among its Increased Claim examples | §8.3 and the Increased/Unlimited mechanism [S89, S91] | A for the mechanism. Recalled (D): caps for gross negligence or wilful misconduct are unenforceable in some jurisdictions |
| Indemnities | Limit your indemnity to third-party claims that a Deliverable, as you delivered it, infringes intellectual property; exclude AI Output, Customer Materials, Third-Party Materials and client changes; keep it inside the cap or supercap; give no unlimited AI-output indemnity | §9.1 and §9.2: each party defends and indemnifies the other against "Covered Claims"; §9.4 makes Section 9 the exclusive remedy for a Covered Claim. The standard-terms text I retrieved does not list the covered claims, which may be set on the cover page that I did not retrieve [S89]. Resist unlimited AI-output indemnities [S95]; customers expect an IP indemnity that covers outputs [S94] | A for the mechanism as retrieved; B for the commentary; the position is mine (D) |
| IP in deliverables | Assign deliverables to the client on payment, excluding Provider Materials and third-party materials | §2.1 [S89] | A |
| Pre-existing materials | Schedule your agent harnesses, orchestration code, prompt templates and libraries, evaluation suites, tooling and know-how as Provider Materials; the client gets a non-exclusive, non-transferable, perpetual, irrevocable licence to use them only as necessary to use the deliverables; you reserve all other rights | §2.3 licence and §2.6 reservation of rights [S89] | A for the mechanism; the named list is my adaptation (D) |
| Work made for hire | Do not use it with individual contractors | A work-made-for-hire clause can make the commissioning party a statutory employer for workers' compensation and unemployment insurance in California: Lab. Code §3351.5(c), Unemp. Ins. Code §§686 and 621(d) [S97] | B (2021, California-specific) |
| Third-party and open-source components | Exclude from the assignment; list licences | §2.1 [S89] | A |
| AI output ownership | Assign whatever rights exist in AI output; give no warranty that any copyright subsists | Human-authorship requirement left in place after cert denied 2026-03-02; prompts alone generally insufficient [S98] | B for the law; the clause is my adaptation (D) |
| Accuracy disclaimer and human review | No warranty of accuracy, completeness, currency or fitness of AI output; client has a qualified human review output before relying on it in consequential decisions | Commentary lists an accuracy disclaimer and a human-oversight acknowledgement [S95] | B |
| Warranty and remedy | Services performed in a timely, competent and professional manner; deliverables conform to the SOW; if they do not, you re-perform within 45 days and, failing that, the client may end the affected SOW for a prorated refund of prepaid fees, which are the client's only remedies for that warranty; all other warranties disclaimed. The template also warrants that deliverables do not infringe and that you have the rights to convey them (§6.3(b), (d)): carve AI Output and open-source components out of both | §6.3(a)–(d), §6.4, §7.1 [S89] | A for the template; the carve-outs are mine (D) |
| No training on client data | You will not train or fine-tune any model on client data except one delivered to the client; you will use model providers only under terms that bar training on client data; the client warrants its right to supply the data | [S95]; customers should not rely on NDAs alone to restrict training [S94] | B |
| Model-provider terms | Third-party model terms and availability flow down; you notify the client of deprecations you become aware of; no warranty of continued availability | Diligence on third-party models and a deprecation-notice requirement [S94, S95] | B |
| Data protection | A data-processing addendum wherever personal data is processed. EU: processor terms and transfer clauses (recalled, D). India: processors act on the fiduciary's directions; main obligations from 2027-05-13 [S41]. Colorado: developer documentation duties from 2027-01-01 [S101] | As cited | B for DPDP and Colorado; D for the EU point |
| Insurance | Maintain tech E&O and cyber; certificate on request | §10.1: each party carries commercial insurance for the term plus six months, at limits that meet any Insurance Minimums in the SOW; certificate on request; "date of occurrence form" with waiver of subrogation [S89]; AI exclusions [S96]. Recalled (D): professional-liability policies are commonly written claims-made, so check that the occurrence-form sentence matches your policy and edit it if not | A and B; the claims-made point is recalled (D) |
| Fees and payment | Fees are non-refundable apart from the prorated refund of prepaid fees that the template allows on specific terminations; bill monthly retainers in advance and expect to refund unearned prepaid fees on any termination except one you make for the client's uncured breach | §4.1 and §5.3(e) [S89]; [S17] | A and C |
| Term and termination | 30-day cure for breach. Put the 3-month minimum and the 30-day convenience notice into the retainer SOW, because the template lets either party end the agreement for any reason only when no SOW is active | §5.2(a) (30-day cure) and §5.2(c) (any reason only if there are no active SOWs) [S89]; [S17, S60] | A for the template; C for the retainer terms; the SOW wording is mine (D) |
| Change orders | Any scope change in writing; hours cap and overage rate in the SOW | §1.3 [S89] | A |
| Independent contractor, exclusivity | Independent-contractor status; no exclusivity; no non-solicit unless narrow | §12.9; no non-solicit appears in the text I retrieved [S89] | A |
| Subcontractors | If you use other people (most 1–5 person practices do), name them in the SOW or get blanket permission | §1.5: Provider may use Subcontractors only with Customer's prior permission and stays responsible for them [S89] | A for the template; the drafting advice is mine (D) |
| Reference rights | Permission to name the client as a reference or publish a case study | The template has a section headed "No Publicity" (§12.7; its text was not retrieved), so ask in the SOW [S89] | D (the heading is A; the advice is design) |
| Governing law and venue | Provider's home jurisdiction or a neutral one; arbitration optional | Not retrieved | D (recalled) |

#### 5.2 Sample drafting language (my wording, Grade D)

Illustrative only; it is not legal advice and is not tested in any jurisdiction. Have a lawyer in your jurisdiction review it, particularly the supercap, the work-made-for-hire point and the data terms. It is more provider-friendly than Common Paper's template in two places: the damages waiver has no carve-out for Increased Claims or confidentiality breaches (template §8.3), and the supercap is the lesser of 5× fees and your insurance limits.

```text
Liability cap. Each party's total aggregate liability arising out of or related to this
Agreement will not exceed the fees paid or payable by Customer under the applicable SOW in
the 12 months before the event giving rise to liability (the "General Cap").

Consequential damages. Neither party is liable for lost profits, loss of data or goodwill,
or any indirect, incidental, special, consequential or punitive damages, however caused.

Supercap. Provider's total liability for breach of the Confidentiality or Data Security
sections will not exceed the lesser of (i) five times the fees paid or payable in the 12
months before the claim and (ii) the limits of Provider's technology errors-and-omissions and
cyber insurance in effect at that time. This sentence does not apply to the accuracy of AI Output.

Provider Materials. "Provider Materials" means agent frameworks, orchestration code, prompt
templates and libraries, evaluation suites, tooling, scripts and know-how, and improvements to
them, that Provider owns or develops independently of the Services, including those listed in
Schedule B. Provider keeps all rights in Provider Materials. To the extent Provider Materials
are embedded in a Deliverable, Provider grants Customer a non-exclusive, non-transferable,
perpetual, irrevocable, worldwide licence to use them only as necessary to use that Deliverable.

Assignment. When Provider has received all fees due for a Deliverable, Provider assigns to
Customer all right, title and interest it holds in that Deliverable, excluding Provider
Materials and Third-Party Materials. No Deliverable is a work made for hire.

AI Output. Deliverables may include output generated by artificial-intelligence systems
("AI Output"). AI Output may be inaccurate, incomplete or out of date. Provider gives no
warranty as to the accuracy, completeness, timeliness or fitness for purpose of AI Output.
Customer will have a qualified person review AI Output before relying on it for any legal,
medical, financial, employment, credit or other consequential decision. Provider assigns
whatever rights it holds in AI Output but does not warrant that any right subsists in it.
Provider's warranties and indemnities do not extend to AI Output, except that Provider will not
knowingly deliver AI Output that it knows infringes a third party's rights.

Data and training. Provider will not use Customer Data to train or fine-tune any model other
than a model delivered to Customer. Provider will use third-party model providers only under
terms that prohibit training on Customer Data. Customer warrants that it has the right to
provide Customer Data to Provider.

Third-party models. Services that depend on third-party models are subject to those providers'
terms and availability. Provider will tell Customer of material changes or deprecations it
becomes aware of but does not warrant continued availability.

Retainer hours. Retainer Hours are capped at [10] per week and do not roll over. Work beyond
the cap needs Customer's written approval and is billed at [rate] per hour. Any change to
scope is recorded in a change order.

Retainer term. Each retainer SOW has a minimum term of three months. After the minimum, either
party may end the SOW for convenience on 30 days' written notice. Fees for hours worked and for
the notice period are payable; prepaid fees for hours not worked are refunded pro rata, except
where Provider ends the SOW for Customer's uncured breach.
```

### 6. Insurance, liability in practice and regulation

**Insurance.** Median annual premiums for small IT consultants: tech E&O $899, cyber $1,540, general liability $369, business owner's policy $638; tech E&O limits of $1M per occurrence and $1M aggregate with a $2,500 deductible, for the average policy the broker sells [S46]. These are broker quote medians, not AI-specific, and the page lists cyber separately while saying tech E&O can bundle it. Fenwick's June 2026 analysis reports that ISO introduced a generative-AI exclusion for commercial general liability in January 2026, that some carriers decline AI-output liability under tech E&O, that cyber is the most stable line, that D&O and employment-practices policies carry absolute AI exclusions, and that affirmative AI products are early-stage; it advises reviewing policies and seeking endorsements [S96]. Practical consequence (inferred): a cap is only as good as the cover behind it, so keep the AI-output cap at 1× fees unless an insurer confirms coverage in writing.

**Liability in practice.** The one worked example found is Deloitte's refund to the Australian government: the contract was about A$440,000 and the refund was over A$97,000 (about US$63,000, less than a quarter of the contract) after a report contained a fabricated court-judgment quote and non-existent references [S64]. It is a large-firm, public-sector case and not a template for solo claims, but it shows that the realised cost of an unverified AI error was a partial fee refund plus reputational damage, not unlimited damages. A Fast Company commentary says responsibility for AI errors rests with the professional who relies on the output and cites several cases, but offers no contract-term guidance [S65]. I searched for lawsuits against independent AI consultants and found only generic commentary, which I did not read in full; I make no claim about their frequency.

**Regulation that changes contract terms:**

| Instrument | What the sources say | What it changes for a consultant (inferred) |
|---|---|---|
| US copyright | Cert denied in *Thaler v. Perlmutter* on 2026-03-02; the D.C. Circuit's human-authorship rule stands; prompts alone are generally insufficient (Copyright Office, January 2025); *Allen v. Perlmutter* pending [S98] | Assign "whatever rights exist" in AI output, give no copyrightability warranty, and record the human contribution to deliverables |
| EU AI Act as amended by the Digital Omnibus | In force 2026-07-27; Annex III high-risk obligations from 2027-12-02, Annex I from 2028-08-02 [S99]; GPAI rules since 2025-08-02 and Article 4 AI literacy retained in recalibrated form [S100] | Decide in the contract who is provider and who is deployer, and who keeps technical documentation; dates moved, so 2025 explainers are stale |
| Colorado SB 26-189 | Signed 2026-05-14, effective 2027-01-01; replaces SB 24-205; drops the reasonable-care duty, risk programmes and annual impact assessments; developer documentation duties; indemnities for one's own discriminatory acts are void [S101, S102] | For automated-decision systems used in Colorado, include documentation deliverables and do not draft an indemnity for the client's own discriminatory acts |
| India DPDP Rules 2025 | Notified 2025-11-13 (G.S.R. 846(E)); consent-manager rule 2026-11-13; main fiduciary obligations 2027-05-13; processors act on fiduciary directions [S41] | A processor-style data addendum when handling Indian personal data; the law-firm summary does not describe processor-contract requirements |


### 7. Solo-practice model: effective rate, utilisation, overhead, tax and the distribution

Everything in this section is **modelled (Grade D at best)**. Sourced anchors are cited next to each input; assumptions are labelled. The model answers "what would net income look like if rates, hours and costs were roughly these?", not "what do AI practitioners actually earn?", which no source I found can answer.

#### 7.1 Structure

Revenue = realised hourly rate × paid hours. Paid hours = working hours × gross utilisation ÷ (1 + scope leakage), where gross utilisation is delivery hours as a share of working hours and leakage is the share of delivery hours that is never billed. Profit = revenue × (1 − 2% payment leakage) − business overhead. Net = profit − health insurance − self-employment and federal income tax. 400,000 Monte Carlo draws per scenario, seed 20261022, Python with NumPy. The tax engines were hand-checked against closed-form cases ($100,000 of Schedule C profit; the Social Security wage-base cap at $300,000; a round trip of the W-2 inverse; India's ₹12 lakh zero-tax point, the ₹24 lakh slab sum and marginal relief at ₹12.1 lakh). Full code is in the appendix at the end of this section.

#### 7.2 Inputs

| Input | Value | Basis |
|---|---|---|
| Working hours | 42 a week × 46 weeks = 1,932 hours a year | 42-hour week from freelancermap [S27]; 46 weeks is my assumption (about six weeks off) |
| Realised hourly rate (US) | Lognormal, median $165, P75 $200 (implied P25 $136, P90 $237) | A.Team senior mid and high bands [S09]; "low / mid / high" are not stated percentiles |
| Gross utilisation | Normal, mean 60%, sd 13%, clipped to 20–90% | Assumption. Consulting firms report about 68–71% billable utilisation; no solo benchmark [S59] |
| Scope leakage | Uniform 5–20% of delivery hours unbilled | Assumption; scope-creep evidence is secondary [S58] |
| Rate and utilisation correlation | −0.3 | Assumption (higher-rate niches fill less of the week) |
| Business overhead (US) | $15,308 a year: tech E&O $899, cyber $1,540, general liability $369 [S46]; software and AI tools $3,600, accounting and legal $3,900, equipment and office $2,000, business development $3,000 (assumed) | Table in 7.6 |
| Health insurance (US) | $7,500 a year ($625 a month, ACA benchmark silver plan, age 40, 2026) | Becker's citing KFF [S45] |
| Payment and platform leakage | 2% of revenue | Assumption |
| US tax, 2026, single filer | Self-employment tax 15.3% on 92.35% of net earnings (Social Security wage base $184,500; 0.9% additional Medicare above $200,000; half deductible); self-employed health-insurance deduction; standard deduction $16,100; brackets 10% to $12,400, 12% to $50,400, 22% to $105,700, 24% to $201,775, 32% to $256,225, 35% to $640,600, 37% above; QBI deduction of 20% with a specified-service-trade phase-in from $201,750 over $75,000; no state tax | [S42, S43, S44]. The phase-in is modelled as a (1 − p)² multiplier, a conservative simplification |
| India tax, new regime | Slabs nil to ₹4 lakh, 5% to ₹8 lakh, 10% to ₹12 lakh, 15% to ₹16 lakh, 20% to ₹20 lakh, 25% to ₹24 lakh, 30% above; section 87A rebate of ₹60,000 up to ₹12 lakh with marginal relief just above; surcharge 10% from ₹50 lakh, 15% from ₹1 crore, 25% from ₹2 crore; cess 4% | [S35, S36, S37]. Surcharge marginal relief is not modelled. BankBazaar lists a 5% surcharge for ₹50 lakh–₹1 crore; ICAI shows 10%, which I used |
| India presumptive scheme | 50% of receipts deemed profit up to ₹75 lakh (cash receipts at most 5%); above it, profit on actual books | Section 58 of the Income-tax Act 2025, consolidating the old 44ADA [S38, S39]. Eligibility of AI consultancy is uncertain: one source hedges that technical consultancy "may qualify" |
| India other | ₹94.716 per US dollar [S40]; 3% payment friction; overhead ₹6.5 lakh a year (assumed); GST ignored | [S24, S81] for friction |
| Weak-traction state (mixtures) | Gross utilisation mean 22% (sd 8%, bounded 5–50%), rate × 0.85; weights of 15%, 30%, 45% and 60% of entrants | Assumption. freelancermap reports 24% of respondents bill under 50 days a year and 38% under 100, including part-timers [S27] |

#### 7.3 United States: practitioners who get traction

| Metric (US, single filer, 2026 law) | P10 | P25 | P50 | P75 | P90 |
|---|---|---|---|---|---|
| Realised rate ($ per paid hour) | $114 | $136 | $165 | $200 | $237 |
| Paid hours per year | 742 | 878 | 1,030 | 1,184 | 1,324 |
| Paid utilisation (share of 1,932 working hours) | 38% | 45% | 53% | 61% | 69% |
| Gross revenue | $111k | $135k | $167k | $205k | $245k |
| Tax (self-employment + federal) | $19k | $26k | $36k | $47k | $57k |
| **Net after overhead, health insurance and tax** | $67k | $83k | $105k | $130k | $160k |
| Net per *working* hour (net ÷ 1,932) | $35 | $43 | $54 | $68 | $83 |
| Net per *paid* hour | $69 | $84 | $103 | $127 | $152 |
| W-2 salary with the same take-home (no benefits counted) | $83k | $106k | $137k | $174k | $215k |

*Reading it.* The median practitioner bills about 1,030 hours (53% of working hours) at $165, grosses $167K, and nets $105K, or $54 per working hour and $103 per paid hour. The same take-home from a W-2 job would need a salary of about $137K, with no value placed on employer benefits, paid leave or retirement matching, which a W-2 job adds and this comparison omits.

#### 7.4 The population view: entrants who stall

The table above conditions on getting traction. Mixing in a weak-traction state (7.2) gives the planning range:

| Weak-traction share of entrants | P10 | P25 | P50 | P75 | P90 |
| --- | --- | --- | --- | --- | --- |
| 0% (viable practitioners only; table above) | $67k | $83k | $105k | $130k | $160k |
| 15% | $29k | $70k | $97k | $125k | $155k |
| **30% (planning case)** | $15k | $38k | $87k | $118k | $149k |
| 45% | $10k | $24k | $68k | $109k | $141k |
| 60% (outside-view case) | $7k | $19k | $39k | $94k | $131k |

| Weak-traction share | Revenue P25 | Revenue P50 | Revenue P75 | Paid hours P25 | Paid hours P50 |
| --- | --- | --- | --- | --- | --- |
| 0% | $135k | $167k | $205k | 878 | 1,030 |
| 15% | $115k | $156k | $197k | 766 | 980 |
| 30% | $73k | $140k | $187k | 502 | 903 |
| 45% | $54k | $112k | $173k | 398 | 740 |
| 60% | $47k | $73k | $151k | 349 | 509 |

P75 and P90 barely move ($94–$130K and $131–$160K), because they are set by rate and traction. P25 and P50 are set by the weak-traction share, which nothing I found observes. The 30% row is my planning case for an AI specialist with a retained network; the outside view below points higher.

**Cross-checks against all-independent data.** Consulting Success's income bands (consultants in general, not AI; gross) put 37% of consultants at $10K a month or more, and 42% of specialists [S49]. MBO counts 5.8M of 74.9M independents at $100K or more [S54]. The modelled shares at or above $120K a year of revenue are:

| Weak-traction share (modelled) | Draws with revenue ≥ $120K | Draws with revenue ≥ $100K | Draws with revenue < $60K |
| --- | --- | --- | --- |
| 0% | 85% | 95% | 0% |
| 15% | 73% | 81% | 10% |
| 30% | 60% | 67% | 20% |
| 45% | 47% | 54% | 29% |
| 60% | 35% | 40% | 39% |
| Consulting Success, all consultants (≥ $10K a month) | 37% | n/a | n/a |
| Consulting Success, specialists (≥ $10K a month) | 42% | n/a | n/a |
| MBO Partners, all independents (≥ $100K) | n/a | 7.7% (5.8M of 74.9M) | n/a |

Matching the specialists' 42% needs a weak-traction share of roughly 51%, and matching all consultants' 37% roughly 57% (linear interpolation between the 45% and 60% rows). So the modelled viable-only distribution (85% of draws at $120K or more) is an upper-tail description, and a planning case of 30% is optimistic against the outside view. On time, freelancermap's billable-day distribution (DACH, n=5,412) has a median of about 138 days, roughly 1,100 hours at eight hours a day by my interpolation, close to the modelled viable median of 1,030 paid hours, with 38% of respondents under 100 days (about 800 hours) [S27].

| Lens | What it measures | Result | Grade |
| --- | --- | --- | --- |
| Model, viable practitioners | US net after overhead, health insurance, federal tax | P25 $83k / P50 $105k / P75 $130k / P90 $160k | D |
| Model, planning range (30–60% stall) | Same | P25 $19k–$38k; P50 $39k–$87k; P75 $94k–$118k; P90 $131k–$149k | D |
| Consulting Success bands [S49] | Gross monthly consulting income, consultants in general | 37% earn $10K a month or more (42% of specialists); interpolated gross P25 about $29K and P50 about $84K a year | C for the bands; D for the interpolation |
| Upwork [S55] | Median for full-time skilled freelancers (data year not stated; probably 2024) | $85,000 | C |
| MBO Partners [S54] | Independents earning $100K or more | 5.8M of 74.9M (7.7%); at most about 21% of the 27.6M full-time independents (MBO's 2025 count) | C |
| freelancermap Kompass [S27] | Billable days a year, DACH IT and consulting freelancers (n=5,412) | Median about 138 days (about 1,100 hours at 8 hours a day, my interpolation); 38% under 100 days | B |
| Antenna 2019 [S47] | Consultants earning $100K or more (selected sample) | Average rate $174, median $150; technology average $258 (garbled chart; mapping inferred) | C |

#### 7.5 Scenarios and sensitivities (US, net after overhead, health insurance and federal tax)

| # | Scenario (change vs base) | Revenue P50 | Net P25 | Net P50 | Net P75 | Net P90 |
|---|---|---|---|---|---|---|
| S0 | **Base**: rate median $165 (P25 $136, P75 $200), gross utilisation 60%, scope leakage 5–20% | $167k | $83k | $105k | $130k | $160k |
| S1 | No scope-creep leakage | $188k | $95k | $119k | $148k | $180k |
| S2 | Scope-creep leakage fixed at 20% | $156k | $78k | $98k | $122k | $148k |
| S3 | High utilisation (gross mean 75%) | $208k | $108k | $133k | $165k | $191k |
| S4 | Acquisition mode (gross mean 40%) | $110k | $48k | $66k | $87k | $108k |
| S5 | AI-efficiency compression: realised rates ×0.87 | $145k | $71k | $90k | $113k | $136k |
| S6 | Agency-dependent: rates ×0.51 | $85k | $35k | $47k | $62k | $77k |
| S7 | Rate median $200 (Go Fractional CTO asking median; CAIO $180–$200) | $202k | $103k | $129k | $162k | $190k |
| S8 | Rate median $140 (employer-offer style) | $142k | $69k | $88k | $110k | $133k |
| S9 | Add 5% flat state income tax | $167k | $79k | $99k | $123k | $151k |
| S10 | Drop the QBI deduction | $167k | $80k | $100k | $123k | $151k |
| S11 | Rate and utilisation independent (ρ = 0 instead of −0.3) | $168k | $80k | $105k | $136k | $173k |
| S12 | Year-1 ramp (3 mo @10%, 3 mo @40%, 6 mo @60% gross utilisation) | $117k | $52k | $71k | $92k | $115k |
| S13 | Overhead 30% of revenue instead of about 11% (implied margin about 68% before health and tax) | $167k | $66k | $81k | $99k | $118k |

Reading the scenarios: utilisation and traction matter most (S3 and S4 move the median by +$28K and −$39K); rate level is next (S7 and S8, +$24K and −$17K); scope leakage moves it by −$7K to +$14K; the AI-efficiency stress (S5) costs $15K; agency dependence (S6) more than halves it. The first-year ramp (S12) gives $71K at the median against $105K in a steady year. Overhead is not a big lever at $15K, but self-reported margins in the one source found (only 34% of consultants report margins above 70%, definition unstated [S49]) are lower than the 89% my overhead implies, so S13 stresses overhead at 30% of revenue (implied margin 68% before health and tax).

**Rate needed for a take-home target** (US, base overhead, health insurance and 2% leakage):

| Target take-home (after overhead, health, tax) | 800 paid h | 1,000 paid h | 1,200 paid h |
|---|---|---|---|
| $75,000 | $154/h | $123/h | $102/h |
| $100,000 | $199/h | $160/h | $133/h |
| $150,000 | $290/h | $232/h | $193/h |

**Net by rate and paid hours** (revenue → net after overhead, health insurance and tax):

| Paid hours / year | $125/h | $150/h | $175/h | $200/h | $250/h |
|---|---|---|---|---|---|
| 700 | $88k → **$49k** | $105k → **$62k** | $122k → **$75k** | $140k → **$87k** | $175k → **$111k** |
| 900 | $112k → **$68k** | $135k → **$83k** | $158k → **$99k** | $180k → **$114k** | $225k → **$145k** |
| 1,100 | $138k → **$85k** | $165k → **$104k** | $192k → **$122k** | $220k → **$141k** | $275k → **$180k** |
| 1,300 | $162k → **$102k** | $195k → **$124k** | $228k → **$146k** | $260k → **$171k** | $325k → **$203k** |

**What a W-2 job would have to pay** for the independent to need a given rate:

| If you would otherwise earn (W-2) | Take-home | Rate needed at 900 paid h | at 1,100 paid h | at 1,300 paid h |
|---|---|---|---|---|
| $120,000 | $93,250 | $166/h | $136/h | $115/h |
| $150,000 | $113,791 | $200/h | $163/h | $138/h |
| $200,000 | $148,927 | $256/h | $210/h | $177/h |

**Retainer portfolios** (deterministic, base overhead):

| Portfolio (US, base overhead) | Revenue | Net after tax | Equivalent W-2 salary |
|---|---|---|---|
| 1 retainer 10h/wk @ $8k x12 | $96,000 | $55,628 | $66,521 |
| 2 retainers @ $8k x12 | $192,000 | $122,019 | $162,038 |
| 2 retainers, one gap 3 months | $168,000 | $105,748 | $138,233 |
| 2 retainers @ $10.8k (Go Fractional CAIO avg) x12 | $259,200 | $170,664 | $230,933 |

Two retainers at $8,000 for 10 hours a week need 960 paid hours in a 48-week year (2.0 retainers); at 13 hours a week, 1.5 retainers cover the same hours. A three-month gap in one of two retainers costs about $16K of net income.

#### 7.6 US overhead assumptions

| Item (US) | $/year | Basis |
|---|---|---|
| Tech E&O (professional liability) | 899 | Insureon median, IT consultants (updated 2026-06-12) — sourced |
| Cyber liability | 1,540 | Insureon median — sourced (may overlap a bundled tech-E&O policy; kept to be conservative) |
| General liability | 369 | Insureon median — sourced |
| Software, AI tools, cloud | 3,600 | Assumption (Grade D) |
| Accounting, bookkeeping, legal review | 3,900 | Assumption (Grade D) |
| Equipment, office/coworking | 2,000 | Assumption (Grade D) |
| Business development, travel, events | 3,000 | Assumption (Grade D) |
| **Business overhead subtotal** | **15,308** | |
| Health insurance (not a Schedule C expense) | 7,500 | $625/month ACA benchmark silver, age 40, 2026 (Becker's citing KFF) — secondary |
| Payment/platform leakage | 2% of revenue | Assumption (Grade D) |

#### 7.7 India-resident individual selling to US or European clients

| India-resident, individual, new regime | P10 | P25 | P50 | P75 | P90 |
|---|---|---|---|---|---|
| Base (rate median $70) — realised rate | $36 | $49 | $70 | $100 | $138 |
| &nbsp;&nbsp;Revenue (USD) | $37k | $50k | $70k | $99k | $135k |
| &nbsp;&nbsp;Receipts (₹ lakh) | ₹34.6L | ₹47.2L | ₹66.7L | ₹94.0L | ₹128.0L |
| &nbsp;&nbsp;Income tax incl. cess (₹ lakh) | ₹1.5L | ₹3.0L | ₹6.0L | ₹24.3L | ₹37.2L |
| &nbsp;&nbsp;**Net after overhead, payment friction and tax (USD)** | $27k | $38k | $53k | $64k | $85k |
| &nbsp;&nbsp;**Net (₹ lakh)** | ₹25.5L | ₹36.3L | ₹50.2L | ₹60.5L | ₹80.4L |
| &nbsp;&nbsp;Share of draws above the ₹75 lakh presumptive-scheme ceiling | 41% | | | | |
| Upside: US-market positioning (rate median $120) — realised rate | $69 | $90 | $120 | $160 | $207 |
| &nbsp;&nbsp;Revenue (USD) | $70k | $91k | $121k | $160k | $206k |
| &nbsp;&nbsp;Receipts (₹ lakh) | ₹66.5L | ₹86.0L | ₹114.4L | ₹151.8L | ₹195.5L |
| &nbsp;&nbsp;Income tax incl. cess (₹ lakh) | ₹6.0L | ₹21.6L | ₹32.5L | ₹45.5L | ₹60.7L |
| &nbsp;&nbsp;**Net after overhead, payment friction and tax (USD)** | $52k | $60k | $76k | $101k | $129k |
| &nbsp;&nbsp;**Net (₹ lakh)** | ₹49.7L | ₹56.8L | ₹72.0L | ₹95.3L | ₹122.5L |
| &nbsp;&nbsp;Share of draws above the ₹75 lakh presumptive-scheme ceiling | 84% | | | | |

| India scenario | Revenue P50 | Net P25 | Net P50 | Net P75 | Net P90 |
|---|---|---|---|---|---|
| Base: rate median $70, gross util 60%, 3% payment friction | $70k | $38k | $53k | $64k | $85k |
| US-market positioning: rate median $120 | $121k | $60k | $76k | $101k | $129k |
| High utilisation (gross 75%) | $88k | $49k | $59k | $78k | $106k |
| Acquisition mode (gross 40%) | $46k | $23k | $35k | $51k | $61k |
| Base with 8.5% payment friction (PayPal-style) | $70k | $36k | $50k | $60k | $80k |
| Presumptive scheme unavailable (actual books throughout) | $70k | $33k | $45k | $64k | $85k |

*The ceiling.* Under the modelled presumptive scheme, tax rises sharply once receipts pass ₹75 lakh (about $79,184), because profit is then taxed on actual books and the surcharge starts at ₹50 lakh:

| Annual receipts (USD) | Receipts (₹ lakh) | Tax basis | Tax incl. cess (₹ lakh) | Net after tax (USD) | Net (₹ lakh) |
|---|---|---|---|---|---|
| $60,000 | 56.8 | 50% presumptive | 4.5 | $46,589 | 44.1 |
| $70,000 | 66.3 | 50% presumptive | 6.0 | $54,729 | 51.8 |
| $75,000 | 71.0 | 50% presumptive | 6.7 | $58,799 | 55.7 |
| $80,000 | 75.8 | actual profit | 18.2 | $51,533 | 48.8 |
| $85,000 | 80.5 | actual profit | 19.8 | $54,719 | 51.8 |
| $90,000 | 85.2 | actual profit | 21.3 | $57,904 | 54.8 |
| $95,000 | 90.0 | actual profit | 22.9 | $61,090 | 57.9 |
| $100,000 | 94.7 | actual profit | 24.5 | $64,275 | 60.9 |
| $110,000 | 104.2 | actual profit | 27.6 | $70,646 | 66.9 |
| $120,000 | 113.7 | actual profit | 32.2 | $75,539 | 71.5 |

Between $75,000 and $80,000 of receipts, net income *falls* by about $7,300 (from $58,799 to $51,533). In the base case 41% of draws sit above the ceiling, which is why India's P75 compresses ($64K) against its P50 ($53K); in the US-positioned case 84% do. Moving payments from a 3% rail to an 8.5% PayPal-style rail costs about $3,400 at the median. This is a model of the statute as I read it from secondary sources; whether AI consultancy qualifies for the scheme, how receipts are measured when payment arrives net of fees, and whether a different structure (for example a company) is better are questions for a chartered accountant.

#### 7.8 Limitations

- No input is calibrated to transacted AI-consultant data; the rate median and P75 come from one vendor's bands.
- The weak-traction weights (15–60%) are unobserved; the central percentiles are unstable with respect to them.
- US: single filer, federal tax only (5% state sensitivity is S9), no retirement contributions, no benefits value, simplified QBI phase-in, no bad debt, no seasonality, no sales tax or VAT.
- India: new regime only, no GST, no advance-tax timing, surcharge marginal relief not modelled, eligibility for the presumptive scheme uncertain, flat FX rate, overhead fixed at ₹6.5 lakh.
- The model describes people who bill. It does not include people who never launched or who stopped.
- All figures are rounded in tables; the underlying run is reproducible from the appendix.

<details>
<summary>Appendix: model code (Python 3 with NumPy; run as <code>python3 -I model.py &lt;outdir&gt;</code>)</summary>

```python
#!/usr/bin/env python3
"""Solo-practice economics model for research session T0-18.

Run with:  python3 -I model.py <outdir>
Everything here is MODELLED (Grade D at best). Sourced anchors are named next to
each constant; assumptions are marked ASSUMPTION. Nothing is downloaded.
"""
import json
import math
import sys

import numpy as np

SEED = 20261022
N = 400_000

# ----------------------------------------------------------------------------
# Time budget
# ----------------------------------------------------------------------------
HOURS_PER_WEEK = 42        # freelancermap Freelancer-Kompass 2026 average week
WEEKS_WORKED = 46          # ASSUMPTION: 52 weeks minus ~6 weeks off/sick/holidays
T_TOTAL = HOURS_PER_WEEK * WEEKS_WORKED  # 1,932 working hours per year

# ----------------------------------------------------------------------------
# US tax constants, tax year 2026, single filer
# (KPMG summary of Rev. Proc. 2025-32; SS wage base $184,500; QBI per secondary source)
# ----------------------------------------------------------------------------
STD_DED = 16_100
US_BRACKETS = [(12_400, .10), (50_400, .12), (105_700, .22), (201_775, .24),
               (256_225, .32), (640_600, .35), (math.inf, .37)]
SS_BASE = 184_500
SE_FRAC = 0.9235
QBI_THR = 201_750          # 2026 SSTB phase-in start, single (beancount.io, secondary)
QBI_RNG = 75_000           # widened from $50k by OBBBA (same source)

# ----------------------------------------------------------------------------
# US overhead
# SOURCED: Insureon medians for IT consultants (E&O $899, cyber $1,540, GL $369)
# SOURCED (secondary): ACA benchmark silver premium, 40-year-old, 2026 = $625/month
#   (Becker's citing KFF, 2025-11-20) -> $7,500/yr
# ASSUMPTION: everything else
# ----------------------------------------------------------------------------
US_BIZ_OVERHEAD = {
    "tech_eo_insurance": 899,
    "cyber_insurance": 1_540,
    "general_liability": 369,
    "software_ai_tools": 3_600,       # ASSUMPTION
    "accounting_legal": 3_900,        # ASSUMPTION
    "equipment_office": 2_000,        # ASSUMPTION
    "bd_marketing_travel": 3_000,     # ASSUMPTION
}
US_BIZ_OVERHEAD_TOTAL = sum(US_BIZ_OVERHEAD.values())
US_HEALTH = 625 * 12
US_LEAKAGE_PCT = 0.02   # ASSUMPTION: payment processing + occasional platform fees

# ----------------------------------------------------------------------------
# India constants (FY2026-27 / tax year 2026-27, new regime default)
# ----------------------------------------------------------------------------
FX = 94.716             # INR per USD, 2026-10-20 (valutafx)
IN_SLABS = [(4e5, 0.0), (8e5, .05), (12e5, .10), (16e5, .15), (20e5, .20),
            (24e5, .25), (math.inf, .30)]
IN_REBATE = 60_000      # s.87A, taxable income <= Rs 12 lakh
IN_CESS = 0.04
IN_PRESUMPTIVE_RATE = 0.50           # 44ADA / s.58 (Income-tax Act 2025)
IN_PRESUMPTIVE_LIMIT = 75e5          # Rs 75 lakh if cash receipts <= 5%
IN_PAY_FRICTION = 0.03               # Wise/Payoneer 2-4% (Winvesta, vendor)
IN_OVERHEAD_INR = 6.5e5              # ASSUMPTION (placeholder, Grade D)


def progressive(x, brackets):
    x = np.maximum(np.asarray(x, dtype=float), 0.0)
    tax = np.zeros_like(x)
    lo = 0.0
    for hi, r in brackets:
        tax += r * np.clip(x - lo, 0.0, hi - lo)
        lo = hi
    return tax


# ----------------------------------------------------------------------------
# US engines
# ----------------------------------------------------------------------------
def us_self_employed(profit, health, state_rate=0.0, qbi=True):
    """profit = Schedule C profit (revenue - business overhead), before health premiums."""
    profit = np.asarray(profit, dtype=float)
    pos = np.maximum(profit, 0.0)
    base = pos * SE_FRAC
    ss = 0.124 * np.minimum(base, SS_BASE)
    med = 0.029 * base
    addl = 0.009 * np.maximum(base - 200_000, 0.0)
    se_tax = ss + med + addl
    half = 0.5 * (ss + med)
    sehi = np.minimum(health, np.maximum(profit - half, 0.0))
    agi = profit - half - sehi
    ti0 = np.maximum(agi - STD_DED, 0.0)
    if qbi:
        qbi_income = np.maximum(agi, 0.0)
        pct = np.clip((ti0 - QBI_THR) / QBI_RNG, 0.0, 1.0)
        # SSTB with no W-2 wages: both the applicable-percentage cut and the
        # wage-limit phase-in bite -> (1 - pct)^2  (conservative simplification)
        qbi_ded = np.minimum(0.20 * qbi_income * (1.0 - pct) ** 2, 0.20 * ti0)
    else:
        qbi_ded = np.zeros_like(ti0)
    ti = np.maximum(ti0 - qbi_ded, 0.0)
    fed = progressive(ti, US_BRACKETS)
    state = state_rate * ti0
    net = profit - health - se_tax - fed - state
    return {"se_tax": se_tax, "fed": fed, "state": state, "ti": ti, "qbi_ded": qbi_ded,
            "sehi": sehi, "net": net}


def w2_net(salary):
    s = np.asarray(salary, dtype=float)
    fica = 0.062 * np.minimum(s, SS_BASE) + 0.0145 * s + 0.009 * np.maximum(s - 200_000, 0.0)
    fed = progressive(s - STD_DED, US_BRACKETS)
    return s - fica - fed


_W2_GRID = np.linspace(0, 1_500_000, 150_001)
_W2_NET = w2_net(_W2_GRID)


def w2_equivalent(net_target):
    """W-2 gross salary whose take-home equals net_target (employer pays health, no match)."""
    return np.interp(net_target, _W2_NET, _W2_GRID)


# ----------------------------------------------------------------------------
# India engine
# ----------------------------------------------------------------------------
def in_tax(ti):
    ti = np.maximum(np.asarray(ti, dtype=float), 0.0)
    t = progressive(ti, IN_SLABS)
    t = np.where(ti <= 12e5, np.maximum(t - IN_REBATE, 0.0), np.minimum(t, ti - 12e5))
    sur = np.where(ti > 2e7, 0.25, np.where(ti > 1e7, 0.15, np.where(ti > 5e6, 0.10, 0.0)))
    return t * (1.0 + sur) * (1.0 + IN_CESS)


def india_net(revenue_usd, overhead_inr=IN_OVERHEAD_INR, friction=IN_PAY_FRICTION,
              force_actual=False):
    rev = np.asarray(revenue_usd, dtype=float)
    receipts = rev * FX
    fric = friction * receipts
    eligible = (receipts <= IN_PRESUMPTIVE_LIMIT) & (not force_actual)
    taxable = np.where(eligible, IN_PRESUMPTIVE_RATE * receipts,
                       np.maximum(receipts - fric - overhead_inr, 0.0))
    tax = in_tax(taxable)
    net_inr = receipts - fric - overhead_inr - tax
    return {"receipts_inr": receipts, "taxable_inr": taxable, "tax_inr": tax,
            "net_inr": net_inr, "net_usd": net_inr / FX, "eligible_44ada": eligible}


# ----------------------------------------------------------------------------
# Monte Carlo draws
# ----------------------------------------------------------------------------
def draw(n, rate_med, rate_p75, u_mean, u_sd, rho=-0.3, leak=(0.05, 0.20),
         rate_mult=1.0, u_bounds=(0.20, 0.90), seed=SEED):
    """Correlated draw of realised rate and gross utilisation.

    rate ~ lognormal(median=rate_med, sigma chosen so P75 = rate_p75)
    u_gross = delivery hours / total working hours (paid or unpaid), clipped normal
    leak = unbilled share of delivery hours (scope creep), uniform
    paid_hours = T_TOTAL * u_gross / (1 + leak)
    """
    rng = np.random.default_rng(seed)
    z1 = rng.standard_normal(n)
    z2 = rng.standard_normal(n)
    sigma = math.log(rate_p75 / rate_med) / 0.6744897501960817
    rate = rate_med * np.exp(sigma * z1) * rate_mult
    zu = rho * z1 + math.sqrt(1 - rho ** 2) * z2
    u_gross = np.clip(u_mean + u_sd * zu, *u_bounds)
    lk = rng.uniform(leak[0], leak[1], n) if leak[0] != leak[1] else np.full(n, leak[0])
    paid = T_TOTAL * u_gross / (1.0 + lk)
    return {"rate": rate, "u_gross": u_gross, "leak": lk, "paid_hours": paid,
            "revenue": rate * paid}


BASE_KW = dict(rate_med=165, rate_p75=200, u_mean=0.60, u_sd=0.13, rho=-0.3)


def mixture(n, w_weak, seed=SEED):
    """Population-weighted stress: share w_weak of entrants are in a weak-traction state.

    ASSUMPTION (Grade D): weak-traction = gross utilisation mean 22% (sd 8%, bounded 5-50%),
    realised rate x0.85. Weight range 15-45% brackets freelancermap's 24% (<50 billable days)
    and 38% (<100 billable days) of respondents, which include part-timers.
    """
    rng = np.random.default_rng(seed + 7)
    base = draw(n, seed=seed, **BASE_KW)
    weak = draw(n, rate_med=165, rate_p75=200, u_mean=0.22, u_sd=0.08, rho=-0.3,
                rate_mult=0.85, u_bounds=(0.05, 0.50), seed=seed + 11)
    pick = rng.random(n) < w_weak
    return {k: np.where(pick, weak[k], base[k]) for k in base}


def pct(a, ps=(10, 25, 50, 75, 90)):
    return {f"P{p}": float(np.percentile(a, p)) for p in ps}


def run_us(label, d, overhead=US_BIZ_OVERHEAD_TOTAL, health=US_HEALTH, state_rate=0.0,
           qbi=True, leakage_pct=US_LEAKAGE_PCT):
    rev = d["revenue"]
    profit = rev * (1.0 - leakage_pct) - overhead
    r = us_self_employed(profit, health, state_rate=state_rate, qbi=qbi)
    net = r["net"]
    out = {
        "label": label,
        "paid_hours": pct(d["paid_hours"]),
        "paid_utilisation": pct(d["paid_hours"] / T_TOTAL),
        "rate": pct(d["rate"]),
        "revenue": pct(rev),
        "profit_before_tax_after_health": pct(profit - health),
        "tax_total": pct(r["se_tax"] + r["fed"] + r["state"]),
        "net_after_tax": pct(net),
        "net_per_working_hour": pct(net / T_TOTAL),
        "net_per_paid_hour": pct(net / np.maximum(d["paid_hours"], 1)),
        "w2_equivalent_salary": {k: float(w2_equivalent(v)) for k, v in pct(net).items()},
        "share_net_below_zero": float(np.mean(net < 0)),
        "net_over_revenue_median_ratio": float(np.median(net / np.maximum(rev, 1))),
    }
    return out, r


def run_in(label, d, overhead_inr=IN_OVERHEAD_INR, friction=IN_PAY_FRICTION):
    rev = d["revenue"]
    r = india_net(rev, overhead_inr=overhead_inr, friction=friction)
    out = {
        "label": label,
        "rate": pct(d["rate"]),
        "paid_hours": pct(d["paid_hours"]),
        "revenue_usd": pct(rev),
        "revenue_inr_lakh": {k: v * FX / 1e5 for k, v in pct(rev).items()},
        "net_after_tax_usd": pct(r["net_usd"]),
        "net_after_tax_inr_lakh": {k: v * FX / 1e5 for k, v in pct(r["net_usd"]).items()},
        "tax_inr_lakh": {k: v / 1e5 for k, v in pct(r["tax_inr"]).items()},
        "share_above_44ada_limit": float(np.mean(~r["eligible_44ada"])),
        "share_taxable_above_50L": float(np.mean(r["taxable_inr"] > 5e6)),
        "net_per_working_hour_usd": pct(r["net_usd"] / T_TOTAL),
    }
    return out, r


def tests():
    """Hand-checked cases for the tax engines."""
    # US: $100,000 Schedule C profit, no health, no state
    r = us_self_employed(np.array([100_000.0]), 0.0)
    se = 100_000 * 0.9235 * 0.153
    assert abs(float(r["se_tax"][0]) - se) < 0.01, (r["se_tax"], se)
    agi = 100_000 - se / 2
    ti0 = agi - STD_DED
    qbi_ded = min(0.2 * agi, 0.2 * ti0)
    ti = ti0 - qbi_ded
    fed = 1_240 + 4_560 + 0.22 * (ti - 50_400)
    assert abs(float(r["fed"][0]) - fed) < 0.01, (r["fed"], fed)
    # US: SS wage-base cap kicks in
    r = us_self_employed(np.array([300_000.0]), 0.0, qbi=False)
    base = 300_000 * 0.9235
    se = 0.124 * 184_500 + 0.029 * base + 0.009 * (base - 200_000)
    assert abs(float(r["se_tax"][0]) - se) < 0.01
    # W-2 inverse
    s = float(w2_equivalent(w2_net(120_000.0)))
    assert abs(s - 120_000) < 1.0, s
    # India: Rs 12 lakh taxable -> zero tax; Rs 24 lakh -> slab maths
    assert float(in_tax(np.array([12e5]))[0]) == 0.0
    t24 = (0.05 * 4e5 + 0.10 * 4e5 + 0.15 * 4e5 + 0.20 * 4e5 + 0.25 * 4e5) * 1.04
    assert abs(float(in_tax(np.array([24e5]))[0]) - t24) < 1e-6
    # marginal relief: Rs 12.1 lakh -> tax capped at Rs 10,000 (+ cess)
    assert abs(float(in_tax(np.array([12.1e5]))[0]) - 10_000 * 1.04) < 1e-6
    return True


def retainer_matrix():
    rates = [150, 175, 200, 225, 250, 300]
    hours_wk = [5, 8, 10, 13, 15, 20]
    rows = []
    for h in hours_wk:
        row = {"hours_per_week": h}
        for rt in rates:
            monthly = h * 4 * rt                 # Go Fractional formula (4-week month)
            eff_calendar = monthly / (h * 52 / 12)   # if client expects every calendar week
            row[f"{rt}"] = {"monthly": monthly, "annual": monthly * 12,
                            "eff_hourly_52_12": round(eff_calendar, 1)}
        rows.append(row)
    return rates, rows


def required_rate(target_net, paid_hours, overhead=US_BIZ_OVERHEAD_TOTAL, health=US_HEALTH):
    lo, hi = 20.0, 1_000.0
    for _ in range(80):
        mid = (lo + hi) / 2
        rev = mid * paid_hours
        profit = rev * (1 - US_LEAKAGE_PCT) - overhead
        n = float(us_self_employed(np.array([profit]), health)["net"][0])
        if n < target_net:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main(outdir):
    tests()
    res = {"meta": {"seed": SEED, "n": N, "T_total_hours": T_TOTAL, "fx_inr_per_usd": FX,
                    "us_biz_overhead": US_BIZ_OVERHEAD, "us_biz_overhead_total": US_BIZ_OVERHEAD_TOTAL,
                    "us_health": US_HEALTH, "us_leakage_pct": US_LEAKAGE_PCT,
                    "india_overhead_inr": IN_OVERHEAD_INR}}

    # ---- US base: rate P25/P50/P75 = 130/165/200 (A.Team senior mid/low/high); u_gross mean .60
    base_kw = BASE_KW
    scen = {}
    d0 = draw(N, **base_kw)
    scen["S0 base"], r0 = run_us("Base: rate med $165 (P25 $130-P75 $200), gross util 60%, leak 5-20%", d0)
    scen["S1 no leakage"], _ = run_us("No scope leakage", draw(N, leak=(0.0, 0.0), **base_kw))
    scen["S2 leak 20%"], _ = run_us("Leakage fixed at 20%", draw(N, leak=(0.20, 0.20), **base_kw))
    scen["S3 util high"], _ = run_us("High utilisation (gross mean 75%)", draw(N, **{**base_kw, "u_mean": 0.75}))
    scen["S4 util low"], _ = run_us("Acquisition mode (gross mean 40%)", draw(N, **{**base_kw, "u_mean": 0.40}))
    scen["S5 ai compression"], _ = run_us("AI-efficiency compression: realised rate x0.87", draw(N, rate_mult=0.87, **base_kw))
    scen["S6 agency dependent"], _ = run_us("Agency-dependent: rate x0.51 (Antenna 2019)", draw(N, rate_mult=0.51, **base_kw))
    scen["S7 rate 200"], _ = run_us("Rate median $200 (Go Fractional asked median)", draw(N, **{**base_kw, "rate_med": 200, "rate_p75": 242}))
    scen["S8 rate 140"], _ = run_us("Rate median $140 (employer-offered style)", draw(N, **{**base_kw, "rate_med": 140, "rate_p75": 170}))
    scen["S9 state 5%"], _ = run_us("Base + 5% flat state income tax", d0, state_rate=0.05)
    scen["S10 no QBI"], _ = run_us("Base without QBI deduction", d0, qbi=False)
    scen["S11 rho 0"], _ = run_us("Base with rate/utilisation independent (rho=0)", draw(N, **{**base_kw, "rho": 0.0}))
    scen["S12 seed2"], _ = run_us("Base, different seed (stability check)", draw(N, seed=SEED + 1, **base_kw))
    for w in (0.15, 0.30, 0.45):
        scen[f"S13 mix{int(w*100)}"], _ = run_us(
            f"Population-weighted: {int(w*100)}% weak-traction entrants", mixture(N, w))
    res["us"] = scen

    # ---- India
    in_kw = dict(rate_med=70, rate_p75=100, u_mean=0.60, u_sd=0.13, rho=-0.3)
    din = draw(N, **in_kw)
    ind = {}
    ind["I0 base"], rin = run_in("India base: rate med $70 (P25 ~$49, P75 $100), same utilisation", din)
    ind["I1 us-positioned"], _ = run_in("India upside: US-market positioning, rate med $120 / P75 $160", draw(N, **{**in_kw, "rate_med": 120, "rate_p75": 160}))
    ind["I2 util high"], _ = run_in("India, gross util 75%", draw(N, **{**in_kw, "u_mean": 0.75}))
    ind["I3 util low"], _ = run_in("India, gross util 40%", draw(N, **{**in_kw, "u_mean": 0.40}))
    ind["I4 paypal"], _ = run_in("India base with 8.5% payment friction (PayPal-style)", din, friction=0.085)
    res["india"] = ind

    # ---- India cliff table
    cliff = []
    for rev in range(50_000, 130_001, 5_000):
        a = india_net(np.array([float(rev)]))
        b = india_net(np.array([float(rev)]), force_actual=True)
        cliff.append({"revenue_usd": rev, "receipts_inr_lakh": float(a["receipts_inr"][0]) / 1e5,
                      "eligible_44ada": bool(a["eligible_44ada"][0]),
                      "net_usd_applied": float(a["net_usd"][0]),
                      "net_usd_if_actual_books": float(b["net_usd"][0]),
                      "tax_inr_lakh_applied": float(a["tax_inr"][0]) / 1e5})
    res["india_cliff"] = cliff
    res["india_cliff_threshold_usd"] = IN_PRESUMPTIVE_LIMIT / FX

    # ---- grids
    rates, rows = retainer_matrix()
    res["retainer_matrix"] = {"rates": rates, "rows": rows}
    grid = []
    for h in (700, 900, 1_100, 1_300):
        row = {"paid_hours": h}
        for rt in (125, 150, 175, 200, 250):
            rev = rt * h
            profit = rev * (1 - US_LEAKAGE_PCT) - US_BIZ_OVERHEAD_TOTAL
            rr = us_self_employed(np.array([profit]), US_HEALTH)
            row[str(rt)] = {"revenue": rev, "net": float(rr["net"][0]),
                            "tax": float(rr["se_tax"][0] + rr["fed"][0])}
        grid.append(row)
    res["us_grid"] = grid
    res["required_rate"] = {f"net{t}_hours{h}": required_rate(t, h)
                            for t in (75_000, 100_000, 150_000) for h in (800, 1_000, 1_200)}

    # ---- deterministic retainer portfolios
    port = {}
    for name, rev in (("1 retainer 10h/wk @ $8k x12", 96_000),
                      ("2 retainers @ $8k x12", 192_000),
                      ("2 retainers, one gap 3 months", 168_000),
                      ("2 retainers @ $10.8k (Go Fractional CAIO avg) x12", 259_200)):
        profit = rev * (1 - US_LEAKAGE_PCT) - US_BIZ_OVERHEAD_TOTAL
        rr = us_self_employed(np.array([profit]), US_HEALTH)
        port[name] = {"revenue": rev, "net": float(rr["net"][0]),
                      "tax": float(rr["se_tax"][0] + rr["fed"][0]),
                      "w2_equiv": float(w2_equivalent(float(rr["net"][0])))}
    res["portfolios"] = port

    # ---- external proxy comparison: Consulting Success monthly gross bands
    gross_m = d0["revenue"] / 12.0
    res["proxy_compare"] = {
        "modelled_cum_share_under_2k": float(np.mean(gross_m < 2_000)),
        "modelled_cum_share_under_5k": float(np.mean(gross_m < 5_000)),
        "modelled_cum_share_under_10k": float(np.mean(gross_m < 10_000)),
        "modelled_cum_share_under_45k": float(np.mean(gross_m < 45_000)),
        "modelled_share_over_100k_annual": float(np.mean(d0["revenue"] > 100_000)),
        "modelled_share_over_250k_annual": float(np.mean(d0["revenue"] > 250_000)),
    }
    # ---- equity arithmetic (no probabilities)
    res["equity_arithmetic"] = {f"exit_{x}M": 0.0025 * x * 1e6 for x in (10, 50, 200)}

    # ---- W-2 comparison: rate an independent needs to match a W-2 take-home
    w2cases = {}
    for sal in (120_000, 150_000, 200_000):
        tgt = float(w2_net(float(sal)))
        w2cases[str(sal)] = {"w2_take_home": tgt,
                             "required_rate": {str(h): required_rate(tgt, h) for h in (900, 1_100, 1_300)}}
    res["w2_cases"] = w2cases

    # ---- retainer overrun: $8,000/month for a nominal 10 h/week
    res["retainer_overrun"] = {str(h): 8_000 / (h * 4) for h in (10, 11, 12, 13, 14)}
    res["retainer_overrun_52_12"] = {str(h): 8_000 / (h * 52 / 12) for h in (10, 11, 12, 13, 14)}

    # ---- AI-efficiency arithmetic: rate uplift needed to hold revenue if hours fall
    res["ai_efficiency_breakeven_uplift"] = {f"{int(s*100)}% fewer hours": 1.0 / (1.0 - s) - 1.0
                                            for s in (0.2, 0.3, 0.5, 0.7)}

    # ---- retainers needed for a paid-hours target (48 billable weeks)
    res["retainers_needed"] = {f"{h} paid hours @ {hw} h/wk each": h / (hw * 48.0)
                               for h in (960, 1_100) for hw in (10, 13)}

    # ---- MODELLED funnel (assumptions, not evidence)
    avg_tenure_months = 9.0            # between Fractional Jobs' 6-12 month norm
    concurrent = 2
    new_per_year = concurrent * 12.0 / avg_tenure_months
    funnel = {}
    for close in (0.30, 0.50, 0.70):   # close rate on proposals (Consulting Success coaching claim 30-70%)
        for call_to_prop in (0.50,):
            calls = new_per_year / (close * call_to_prop)
            funnel[f"close{int(close*100)}"] = {"new_retainers_per_year": new_per_year,
                                                "first_calls_per_year": calls,
                                                "first_calls_per_month": calls / 12.0}
    res["funnel_model"] = funnel

    # ---- Year-1 ramp: months 1-3 at 10% gross utilisation, months 4-6 at 40%, months 7-12 at base
    ramp_months = [0.10] * 3 + [0.40] * 3 + [0.60] * 6
    mean_u = sum(ramp_months) / 12.0
    res["ramp_year1_mean_gross_util"] = mean_u
    res["ramp_year1"], _ = run_us("Year-1 ramp (3 mo @10%, 3 mo @40%, 6 mo @60% gross util)",
                                  draw(N, **{**base_kw, "u_mean": mean_u}))

    with open(f"{outdir}/results.json", "w") as f:
        json.dump(res, f, indent=1)
    print("ok; tests passed; wrote results.json")


if __name__ == "__main__":
    main(sys.argv[1])
```

The overhead and mixture cross-check sensitivities (S13 and the 60% mix) re-use `draw`, `mixture`, `us_self_employed` and `pct` from this file: S13 sets profit = revenue × (1 − 0.02) − 0.30 × revenue; the 60% mix is `mixture(N, 0.60)` passed through `run_us`.

</details>


### 8. Tool catalog

Fees are what each vendor says about itself (Grade A) unless marked C. "Fit" is my judgment (inferred). A fee quoted as a share of the client's total bill differs from a markup on the expert's fee: markup = 1 ÷ (1 − fee share) − 1, so a 20–30% share of total fees is a 25–43% markup.

#### 8.1 Marketplaces and networks

| Tool | What it is | Cost to the independent | Cost or markup to the client | Terms to watch | Fit |
|---|---|---|---|---|---|
| Go Fractional [S04] | Fractional job board, profile, rate tools; publishes the benchmarks used above | Free membership; contracts, invoicing and payouts handled; $500 referral programme | Not stated | Vendor-run data [S03] | Primary secondary channel for fractional leaders |
| Fractional Jobs [S06, S16] | Fractional job board; sponsor of the largest survey | Unverified: fractionaljobs.io was blocked; a competitor says "no platform fees or percentage markup" | Unverified | Confirm fees and any exclusivity directly | Check terms, then use as a lead source |
| Fractionus [S15] | Placement network | Not stated; accepts under 3% of applicants | Not stated | Competitor of Fractional Jobs | Optional |
| FSuite | Named in the brief | Two searches found no FSuite page [S78] | n/a | n/a | Not catalogued |
| Toptal [S68, S69] | Vetted freelance marketplace | Talent sets own rate; no fee to talent; availability 0–50 hours a week | Undisclosed; estimates 30–50% (C) | Contracts reportedly bar working directly with Toptal-sourced clients (competitor page, C); official FAQ is silent | Gap-filling after screening; read the terms |
| Braintrust [S70, S71, S72] | Talent network | 0% talent fee; talent keeps 100% on clients it brings | 10% (CoinMarketCap) to 15% (Flexiple) on top, plus a 15% conversion fee if hired full-time within six months (C); official FAQ gave no fee information | Directory and competitor sources disagree | Optional |
| Catalant [S73, S74] | Expert marketplace for consulting projects | Experts are paid whether or not the client pays Catalant; winning experts typically have 10–20 years' experience | 20–30% of total fees, about a 25–43% markup (C); another source says 20–35% | No official fee figure found | Senior consultants with enterprise-project credentials |
| Contra [S75, S76] | Commission-free freelancer platform | 0% commission; free tier; Pro $29 a month or $199 a year (C) | Some payment fees on free-plan transactions (C) | Official pricing page blocked | Portfolio and direct invoicing |
| Upwork [S66, S67] | Bidding marketplace | Variable 0–15% per contract, shown before the proposal and fixed for that contract | Client marketplace fee 5% (3% for eligible US clients), 8–10% for Business Plus; Connects $0.15; Freelancer Plus $14.99 or $19.99 (C) | Commodity pricing pressure (Finding 11) | Utilisation filler only |
| Fiverr [S19] | Commodity marketplace | n/a | AI strategy consultants listed at $10–$125 an hour (C) | n/a | Not for senior work |

#### 8.2 Contracts, invoicing and payments

| Tool | What it is | Pricing | Notes | Fit |
|---|---|---|---|---|
| Common Paper [S89, S93] | Open contract standards: Professional Services Agreement v1.1, NDAs, AI Addendum v1.0 | Free; CC BY 4.0 | AI Addendum clause text not retrieved | Base template |
| Bonterms [S88] | Open standard terms | Licence shown as both CC BY 4.0 and CC0 (conflict) | PSA v1.2 cover page has "Deliverables Type: licensed or assigned"; standard terms at bonterms.com not retrieved | Alternative; verify before use |
| Freelancers Union Contract Creator [S83] | Free beta contract generator | Free | Covers scope, payment terms and deadlines; no IP clause mentioned | Too thin for AI work |
| OpenAgreements [S86, S87] | Template catalogue (125 templates incl. Common Paper's) | Content CC BY 4.0; project code Apache-2.0 | Each template keeps its source licence; "legal research, not legal advice" | Browse and compare |
| GitHub: okfn/contracts, dxw/contracts [S84, S85] | Organisations' own contract documents | Free | Organisation-specific; no consulting template with AI terms confirmed; dxw's clause contents not visible | Reference only |
| Docracy [S82] | Legacy contract-sharing site | n/a | Shutdown announced 2018-02-27 for 2018-07-01; wiki lists it offline, but it was observed operating in 2021 | Skip |
| Bonsai [S77] | Contracts, proposals, invoices, time tracking | Per user per month, monthly / annual: Basic $15 / $9, Essentials $25 / $19, Premium $39 / $29, Elite $59 / $49 | Proposals, contracts and invoicing start at Essentials; processing fees vary by payment method and provider; template wording not reviewed | Reasonable all-in-one |
| Stripe Invoicing [S79] | Invoicing | Starter 0.4% and Plus 0.5% per paid invoice, plus processing | Bulgarian page; a US page was not fetched | Card and ACH invoicing |
| Wise Business [S24, S80] | Multi-currency receiving | Free to open; free local receipt for USD, GBP and EUR; SWIFT receipt fixed at USD 6.11, GBP 2.16, EUR 2.39 | INR conversion percentage not stated on the page; a payments vendor says about 2–2.5% (C) | Main rail for India-based providers |
| Payoneer [S81] | Cross-border receiving | Receive free into a local-currency account, 1% (minimum $1) into a non-local one; EU or UK bank transfer 1%; US ACH 1%; payer card up to 3.99% + $0.49; withdrawal 1.2–4%; conversion 1.2–4% | Fees vary by territory and account | Alternative rail |
| PayPal [S24] | Payments | About 8–9% friction for India-based freelancers (payments vendor, C) | | Avoid for large invoices |

### 9. Failure-mode and falsification log

Each row is a claim I tried to break, with what I searched for and what came back.

| # | Claim or failure mode | What I looked for | What I found | Verdict |
|---|---|---|---|---|
| 1 | Acquisition is the dominant risk | Surveys of independents and fractionals on challenges | 90% (Go Fractional), 78% (Antenna), 62% (freelancermap, via 9am), 43% with no secured workload [S03, S27, S47, S57] | Supported (C); nothing AI-specific |
| 2 | Scope creep wrecks retainer margins | Data on scope creep for consultants and agencies | An SE Ranking figure seen only through an aggregator (59 of 115 agencies) [S58]; a CMO-tenure blog on scope mismatches [S60] | Plausible; no primary evidence for solo AI work |
| 3 | Many practitioners return to full-time work | Exit and return-to-employment data | freelancermap's survey reports no such figure [S27]; intent only: 90% not interested in returning, 84% would be self-employed again, 78% plan to continue [S06, S28, S54]; over half of consultants regain prior employee income within two years [S50] | Unresolved; intent data are sponsor-run and may be survivorship-biased |
| 4 | AI efficiency erodes hourly billing | Rate trends over time | UK median £613–£625 (2024, two reads) to £550 (2025 and 2026) [S30]; Upwork per-contract earnings −13% [S56]; against that, +34% an hour for AI work on Upwork [S56] | Mixed |
| 5 | Demand for a "Head of AI" is thin | Posting counts and demand signals | CAIO: 6 then 10 posts in 90 days, demand "falling sharply"; CTO: 19 then 17 posts, "rising" [S01, S02]; Fractional Jobs hiring +149% year on year (sponsor release) [S07]; AI/ML is 5% in its top-industries list [S06] | Conflicting; sell outcomes, not the title |
| 6 | GenAI projects fail or get cancelled | Failure forecasts and rebuttals | Gartner forecast of over 40% of agentic projects cancelled by end-2027 [S62]; critique of the "95% fail" claim [S63] | Forecast, not observation; contested |
| 7 | Consultants are liable for AI errors | Cases and lawsuits | Deloitte's partial refund [S64]; commentary [S65]; no suits against independent AI consultants found | Plausible; no frequency data |
| 8 | Insurers exclude AI risk | Coverage changes | ISO generative-AI exclusion on CGL; some tech E&O carriers decline AI-output liability [S96] | Found (B) |
| 9 | 3–6 month liability caps are standard | Cap statistics and template defaults | 1× fees over 12 months is the template default; 92% of sales contracts [S90, S92]; no source for a 3–6 month norm | Contradicted |
| 10 | AI work commands a platform premium | Premium evidence | +34% (Upwork), +37% (Second Talent), 10–25% (A.Team), "not significant" market-wide (YunoJuno) [S09, S11, S31, S56] | Mixed |
| 11 | India-based consultants earn US-positioned rates | Rates actually paid | Vendor ranges of $50–$100 against $120–$200 from a payments vendor [S13, S22, S23, S24]; no dataset | Unverified |
| 12 | Advisory equity pays | Outcome data | FAST tiers; equity-only deals "fail within six months" outside a narrow band [S60, S61]; no outcome data | No evidence of payoff |
| 13 | Marketplaces trap you with non-circumvention terms | Official terms | Toptal's FAQ is silent; a competitor page reports bars [S68, S69] | Unverified |
| 14 | Docracy is a live template source | Current status | Offline or legacy; sources conflict [S82] | Contradicted |
| 15 | Open-source or content reputation drives inbound | Quantified channel evidence | Nothing quantified; adjacent figures are discouraging [S47, S50] | Not found |
| 16 | GitHub holds consulting MSA templates with AI clauses | Repository search | Two organisation-specific repositories; no AI terms confirmed [S84, S85, S87] | Not found |
| 17 | FSuite is a fractional network I can catalogue | Searches by name | No FSuite page in two searches [S78] | Not found |
| 18 | Indian domestic client rates | Rate cards for Indian clients | None | Not found |


## Open Questions & Risks

### What was found, recalled, modelled and inferred

| Category | What it covers | Grade ceiling |
|---|---|---|
| Found | Every claim with an [S##] cited to the ledger; Access = Read or Extract | A to C by source |
| Recalled | The EU processor-terms and transfer-clause point (5.1); caps for gross negligence being unenforceable in some jurisdictions (5.1, objection 11); the "Annex I" label for the EU's product-embedded high-risk category (Detailed Findings 6); employment contracts that restrict outside work (Alternatives Considered); governing-law guidance (5.1); the claims-made form of professional-liability policies (5.1, Insurance); the "before" values of dated items in the Delta table (EU, Colorado, *Thaler*, Upwork tiers) | D |
| Modelled | The solo-practice model and its tax engines (Detailed Findings 7); retainer, overrun, equity and AI-efficiency arithmetic (2); the funnel (4.4) | D |
| Inferred | The recommendation, term sheet, deliverables, decision rights, clause adaptations and operating card | D |

### The strongest expert objections, with evidence for and against

**1. "These are asking rates, not transacted rates."**
*For:* Go Fractional's own data show offers at 0.66–0.91× (CAIO, two reads) and about 0.6× (CTO) of asks [S01, S02]; every rate source is a vendor guide, a platform benchmark or a job advert; no invoice-level data was found; Go Fractional's retainers are computed as rate × hours × 4 [S01]. *Against:* four independent sources (A.Team, Second Talent, Go Fractional, Fractional Jobs) land on roughly $150–$250 for senior and executive work [S03, S06, S09, S11]; the UK figures are employer-quoted adverts [S30]; Vantage Point's tiers are prices one firm actually posts [S17]. *Conclusion:* treat $150–$250 as the asking corridor and plan below it. Scenario S8 (median $140) shows the cost of being wrong: net P50 falls $17K.

**2. "Sponsor-run surveys and survivorship bias make the acquisition and retention figures unreliable."**
*For:* a marketplace (Go Fractional) and a talent seller (Fractional Jobs) sponsor the two biggest surveys; Fractional Jobs' sample mixes 810 active, 235 past and 688 aspiring fractionals and the page does not say which group the "90% not interested in returning" covers, so leavers may be absent from it; Consulting Success sells coaching; Antenna's sample is selected on earning $100K or more [S03, S06, S47, S48]. *Against:* the referral-and-network finding replicates across sponsor-run, independent (freelancermap, Antenna) and platform sources (YunoJuno: over 80% of bookings are direct) [S27, S31, S47]. *Conclusion:* trust the direction, not the magnitudes.

**3. "Vendors have commercial reasons to inflate or deflate."**
*For:* offshore staffing vendors quote India rates [S13, S22, S23]; a payments vendor claims $120–$200 for India-based seniors on premium platforms [S24]; agencies publish marketing ranges up to $600 an hour [S14]. *Against:* the bands overlap across vendors with opposite incentives, and the two extremes (Lemon.io's $61–$85 for US seniors, Flexiple's $12) are visibly out of line. *Conclusion:* I used bands, excluded the outliers, and labelled the India upside case a hypothesis.

**4. "'Head of AI' is a re-labelled fractional CTO or ML engineer, and demand is thin."**
*For:* the CAIO benchmark rests on six to ten postings and Go Fractional labels CAIO demand "falling sharply" [S01]; AI/ML is 5% in Fractional Jobs' top-industries list [S06]. *Against:* CAIO asks ($190–$208) are within about 10% of CTO asks ($209–$212); 24% of Fractional Jobs' clients explicitly requested AI-native skills and 38% of respondents say AI expertise helped them win work [S06]; the same sponsor reports hiring up 149% year on year [S07]. *Conclusion:* sell the outcome (pilots, roadmap, governance) and keep fractional-CTO and architect positioning available.

**5. "AI efficiency will erode hourly billing, so rate levels will fall."**
*For:* UK GenAI day-rate medians fell from £613–£625 (2024, two reads) to £550 [S30]; Upwork per-contract earnings in gen-AI and creative work fell 13% [S56]; 98% of Fractional Jobs respondents are more efficient [S06]; a 30% cut in hours needs a 43% higher rate to hold revenue. *Against:* Upwork reports AI-work freelancers earning 34% more an hour and complex AI-augmented work earnings up 45% [S56]; 30% of Fractional Jobs respondents serve more clients because of AI [S06]. *Conclusion:* the evidence is mixed, so the recommendation avoids pure hourly billing; stress S5 (rates × 0.87) costs $15K of median net.

**6. "Source numbers are inconsistent in their units."**
*For:* A.Team's monthly-hours tiers imply $250–$1,250 an hour [S10]; a CMO-focused page pairs a $10,000–$12,000 monthly retainer with 15–25 hours a month (about $400–$800 an hour by my arithmetic) beside Go Fractional's hours-per-week scope [S60]; Go Fractional's retainers use 4-week months. *Against:* I excluded or recomputed each case. *Conclusion:* residual risk that other sources hide similar errors.

**7. "The tax and legal treatment is oversimplified, and this is not advice."**
*For:* the US model ignores state tax (S9 adds 5%), retirement contributions and benefits, and simplifies the QBI phase-in; the India model assumes the presumptive scheme applies to AI consultancy (one source hedges), takes the ₹75 lakh and 50% parameters from a slide deck that does not say they are unchanged from section 44ADA, omits surcharge marginal relief and GST [S37, S38, S39]; the sample clauses are my drafting, untested; the California note is a 2021 article [S97]; the AI-clause commentary is one practitioner's list [S95]. *Against:* hand-checked closed-form tests passed; sources for brackets and wage bases are consistent [S42, S43]. *Conclusion:* use the figures to size decisions, then confirm with a CPA, chartered accountant and lawyer.

**8. "You have no AI-specific income data, and your distribution is the upper tail."**
*For:* the modelled viable P25 revenue ($135K) exceeds what any all-independent proxy implies; 85% of viable draws earn $120K or more against 37–42% in Consulting Success's bands; the weak-traction weights are unobserved [S49, S54]. *Against:* AI specialists at a senior level plausibly sit above all-consultant averages; freelancermap's median of about 138 billable days is consistent with the viable paid-hours median [S27]. *Conclusion:* report the viable table only as a conditional, give the planning range of 30–60% stalled entrants, and treat P25 and P50 as scenario-dependent.

**9. "People who try this return to employment; your sources cannot see them."**
*For:* the 90%, 84% and 78% figures are intent, not behaviour, and come from sponsor-run or self-selected samples; freelancermap reports no return-to-employment figure [S06, S27, S28, S54]. *Against:* 87% of Fractional Jobs' respondents have 11+ years of experience, a population less likely to need to return; over half of consultants regain prior employee income within two years [S06, S50], which suggests income recovery, not a lasting return. *Conclusion:* unresolved; P4 stays open. The viability gate in the recommendation is the protection.

**10. "The cap statistic is for sales contracts, not consulting."**
*For:* Common Paper's 92% figure is for sales contracts and its base is not spelled out [S92]. *Against:* the PSA's own default is the same 1× over 12 months [S89, S90], and I found no source for a 3–6 month norm. *Conclusion:* the baseline stands. Small solo engagements may land at lower caps in practice; I could not test that.

**11. "Caps do not survive gross negligence or wilful misconduct in many places."**
*For (recalled, D):* enforceability of such caps varies by jurisdiction. *Against:* the template's help article lists gross negligence and wilful misconduct among its examples of Increased (supercap) claims [S91]. *Conclusion:* do not rely on a cap for those categories; take counsel's view in your jurisdiction.

**12. "The India presumptive scheme may not apply to AI consultancy."**
*For:* one source says technical consultancy "may qualify" depending on the nature of services [S39]. *Against:* the ICAI deck lists professionals under the consolidated section [S38]. *Effect (modelled):* if the scheme is unavailable, net income at $60,000 of receipts is $39,932 rather than $46,589, at $70,000 it is $45,162 rather than $54,729, and at $75,000 it is $48,348 rather than $58,799. The base-case India P50 would fall from $53K to $45K, with P25 at $33K instead of $38K.

### Open questions this research could not answer

1. What is the distribution of *realised* AI-retainer rates? Anonymised invoices from a billing platform would settle it.
2. What are first-call-to-retainer conversion rates for AI consultants specifically, by channel?
3. Do clients accept 12-month, 1× caps and insurance-limited supercaps from solo providers, or do they push for more?
4. Is affirmative AI-output cover available to solos, and at what price?
5. Do India-based providers realise US-positioned rates (above $100 an hour), and through which channels?
6. What fraction of independents return to employment within two to three years?
7. What does Common Paper's AI Addendum v1.0 say in clause text, and how does it compare with the commentary used here [S93]?
8. What do Indian domestic clients pay AI consultants?

### Risks to the recommendation

- **Concentration.** Two retainers means each client is half your revenue; losing one costs about $16K of net income for a three-month gap (Detailed Findings 7.5).
- **Rate deflation.** If AI-driven compression reaches senior consulting, the corridor falls below $150; mitigation is outcome-based pricing and six-monthly rate reviews.
- **Insurance gaps.** AI-output claims may be uncovered [S96]; mitigation is the lower AI-output cap and written confirmation.
- **Regulatory flux.** EU and Colorado dates moved in 2026 and may move again [S99, S101].
- **Platform and channel dependence.** Sponsor-run channels can change terms; the referral-first funnel limits exposure.
- **Model risk.** Every percentile in 7.3–7.7 is modelled; do not quote them as observed.

### What would change my conclusions

A transaction-level dataset on AI-retainer rates; evidence that 3–6 month caps are routinely agreed in consulting; behavioural data showing most independents return to employment; a tax opinion that the Indian presumptive scheme does not apply; or an insurer's confirmation that AI-output claims are routinely covered for small providers.

### Honest gaps (searched or attempted; nothing usable)

- **FSuite:** two searches, no FSuite page [S78].
- **Bonsai** contract-template wording: pricing was retrieved from the official page, but template text was not reviewed [S77].
- **Braintrust** and **Catalant:** no official fee statement found [S70, S73].
- **Contra** pricing page and **fractionaljobs.io:** fetch refused [S08, S76].
- **Go Fractional playbook:** returned a script shell only [S05].
- **Common Paper AI Addendum** clause text and **Bonterms** standard terms: not retrieved [S88, S93].
- **Common Paper PSA cover page** (Key Terms): not retrieved; the cap amounts, the claims covered by the indemnities and any Insurance Minimums may be set there [S89].
- **AI-specific funnel benchmarks**, **AI-specific income percentiles**, **longitudinal return-to-employment data**, and **quantified open-source or content reputation as a channel:** searched, none found.
- **Rates paid to India-based AI consultants** by US or EU startups, and **Indian domestic client rates:** no dataset.
- **Lawsuits against independent AI consultants:** results were generic commentary and were not read in full.
- **GitHub consulting MSA templates with AI terms:** none confirmed [S84, S85, S87].
- **Income-tax Act 2025** section values: the ICAI deck shows the 50% and ₹50 lakh / ₹75 lakh parameters under section 58 but does not state they are unchanged from 44ADA [S38].
- **Payoneer** legal fee page: failed to fetch; the main fees page was used [S81].
- **Second-pass re-verification (2026-10-25)** covered 39 of the 102 sources. Not re-checked (blocked on the second pass, or low-weight and not attempted), so they rest on the first read: A.Team's CTO page, Second Talent's India card, Groovy Web, Fractionus, the India tax-slab pages (BankBazaar, Tata Capital, ICAI Palakkad), the QBI, ACA-premium and Harvest utilisation pages, Gartner, Catalant, Braintrust, Bonsai, Koley Jessen, WCR Legal, and the Upwork-fee explainer and the Toptal, Braintrust, Catalant and Contra fee-estimate pages.


## Delta

Belief-change table: what I (or the brief) believed before, what the evidence showed, and how far the belief moved. "Before" values for P1–P5 are the Prior section; the later rows are recalled or first-reading items (Grade D) that sources updated.

| # | Belief | Before | After | Change | Evidence | Confidence now |
|---|---|---|---|---|---|---|
| P1 | US experienced AI consultants bill $150–$300 an hour | $150–$300 | Asks cluster at $150–$250; offers are lower (CAIO $125–$189, CTO $124–$129); $300+ appears only in marketing ranges; Europe and India are lower | Partly confirmed, narrowed | [S01, S02, S09, S11, S14] | Medium on asks, low on transacted rates |
| P2a | Head-of-AI retainer is about $10K a month | About $10K | $8–13K for 10–13 hours a week; Vantage Point's published tiers equal $200–$225 an hour | Confirmed in magnitude | [S01, S15, S17] | Medium |
| P2b | "$8,000 for 10 hours a week" is $200 an hour | $200 | $200 on a 4-week month, $185 on 52/12 weeks, $154 at 12 hours of actual work; Go Fractional's retainers are computed, not observed | Corrected | Arithmetic (Detailed Findings 2); [S01] | High (arithmetic) |
| P2c | About 0.25% advisory equity | 0.25% | Matches the FAST idea-stage "Standard" tier; stage tiers run 0.15–1.0%; equity-only deals fail within six months outside a narrow band (CMO source); no outcome data | Confirmed as a benchmark, not as a payoff | [S60, S61] | Medium on the benchmark, low on value |
| P3a | Acquisition and churn are a dominant risk | Dominant | Acquisition is the top challenge in every survey that asks (90%, 78%, 62%); no AI-specific funnel data | Confirmed | [S03, S27, S47, S57] | Medium |
| P3b | Scope creep is a dominant risk | Dominant | Supported only by an aggregator's figure and a blog; added two risks I had not weighed: AI-driven rate compression and AI-output liability or insurance gaps | Partly confirmed, extended | [S56, S58, S60, S96] | Low to medium |
| P4 | Many practitioners return to full-time work | Many | Intent surveys say 90% are not interested in returning (sponsor-run; possible survivorship bias); no behavioural data; freelancermap reports no figure | Unresolved; weakly contradicted by intent data | [S06, S27, S28, S50, S54] | Low |
| P5a | MSA caps are fees in the preceding 3–6 months | 3–6 months | 1× fees over 12 months is the template default and the figure for 92% of Common Paper's sales contracts | Contradicted | [S89, S90, S92] | High on the template, medium on consulting practice |
| P5b | Pre-existing IP (harnesses, prompt templates) is carved out | Carved out | Standard in Common Paper's PSA (exclusion from assignment plus an embedded-use licence); naming harnesses and prompt templates is a drafting adaptation | Confirmed | [S89] | High |
| R1 | Upwork's freelancer fee is a 20/10/5% sliding scale (recalled) | 20/10/5% | Variable 0–15% per contract since 2025-05-01 | Superseded | [S66, S67] | Medium |
| R2 | Toptal's client markup is documented (recalled expectation) | A published figure | Undisclosed; estimates 30–50% | Not available | [S68, S69] | Low |
| R3 | *Thaler v. Perlmutter* was pending (recalled) | Pending | Certiorari denied 2026-03-02; human-authorship rule stands | Updated | [S98] | High |
| R4 | Colorado's AI law takes effect in 2026 (recalled) | 2026 | SB 26-189 signed 2026-05-14, effective 2027-01-01, with a lighter duty set | Updated | [S101, S102] | High |
| R5 | EU high-risk obligations start in August 2026 (recalled) | 2026-08 | Digital Omnibus in force 2026-07-27: Annex III from 2027-12-02, Annex I from 2028-08-02 | Updated | [S99] | High |
| R6 | Docracy is a live template library (recalled) | Live | Legacy; sources conflict on whether it is offline | Contradicted | [S82] | Medium |
| R7 | The modelled distribution describes full-time AI independents | Representative | It describes the upper tail; outside-view calibration needs a 51–57% stalled share; planning range 30–60% | Narrowed | Detailed Findings 7.4; [S49] | Low |
| R8 | A retainer can be ended for convenience on 30 days' notice under Common Paper's PSA (my first reading of the template) | Allowed | §5.2(c) allows termination for any reason only when no SOW is active; §5.3(e) refunds unearned prepaid fees unless the provider ends the SOW for breach; §4.1 makes fees non-refundable only apart from that | Corrected | [S89] | High |
| R9 | Go Fractional's CAIO offers run at about 0.91× of asks (first read) | 0.91× | 0.66× on the second read as postings rose from 6 to 10; CTO about 0.6× on both reads | Revised | [S01, S02] | Medium on direction, low on size |
| R10 | Senior LLM rates rose from $145 (2023) to $210 (2026) with growth slowing (search extract) | Rising | Not reproduced: the current page gives $155–$235 and shows no trend | Withdrawn | [S12] | Low |
| R11 | 27.6M full-time independents is a 2026 MBO figure (first reading) | 2026 | It is MBO's 2025 count, described as stable; I found no 2026 count | Corrected | [S54, S55] | Medium |

## Sources & Evidence Ledger

Grades: A canonical primary for what the page itself says; B independent or transparent secondary; C directional (vendor, self-reported, small n, single source); D recalled, inferred or modelled (none appear here; those are tagged in the body). Access: Read = page text retrieved; Extract = seen only as a search-result text extract; Blocked = fetch refused; Gap = searched, nothing usable. Dates are publication or update dates where the page gave one, otherwise the year or the retrieval month. Rows marked Gap or Blocked are listed so the absence is on the record.

| ID | Source | Date | What it supports | Grade | Access | Caveat |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | [Go Fractional, Fractional Chief AI Officer cost & rates (live benchmark)](https://www.gofractional.com/insights/rates/chief-ai-officer) | first read about 2026-10-20 (page then said updated 2026-10-20); re-read 2026-10-25 (no date shown) | CAIO asks avg $208 / median $200 / P25-P75 $150-250; offers $189 ($130-250); 13 h/wk; $7.8-13k/mo computed as rate x hours x 4; 6 posts and 326 profiles in 90 days; demand 'falling sharply'. Re-read 2026-10-25: asks avg $190 / median $180 / P25-P75 $150-250; offers avg $125 (P25-P75 $93-150); 13 h/wk; about $9,800 a month, from $7,800; 10 posts in 90 days, no profile count; demand 'falling sharply' | C | Read | Vendor (talent marketplace); tiny n; retainer figures are computed, not observed contracts; figures moved between reads (offers $189 to $125 as posts rose from 6 to 10) |
| S02 | [Go Fractional, Fractional CTO cost & rates (live benchmark)](https://www.gofractional.com/insights/rates/cto) | first read about 2026-10-20 (page then said updated 2026-10-20); re-read 2026-10-25 (page dated 2026-10-24) | CTO asks avg $210 (P25-P75 $150-250; profile asks $212, $160-250); offers $129 ($96-145); 15 h/wk; $9-15k/mo computed; 19 posts and 1,042 profiles; demand 'rising sharply'; 32/32/37% remote/hybrid/on-site. Re-read 2026-10-25: asks avg $209 (profile asks avg $210, P25-P75 $150-250; FAQ median $200); offers avg $124 (P25-P75 $90-130); 15 h/wk; 17 posts and 1,116 profiles; demand rising (GF Demand Index +13%); $9-15k/mo computed (15 x 4 x rate) | C | Read | Vendor; computed retainers; figures drift between reads |
| S03 | [Go Fractional, 2026 State of Fractional Work (PDF; n=213 survey, April 2026)](https://www.gofractional.com/docs/2026_State_of_Fractional_Work-Go_Fractional.pdf) | 2026-06-09 | Avg fractional rate $153; CTO $211; CAIO $218; Architect $217; EM $185; Tech Lead $174; 92% networks / 54% LinkedIn / 29% platforms; 90% acquisition #1 challenge; hourly pricing dominates; best relationships retainer-based, billed upfront, 3+ months | C | Read | Vendor-run survey; self-selected respondents |
| S04 | [Go Fractional, membership page](https://www.gofractional.com/membership) | retrieved 2026-10 | Free membership; profile, job board, rate tools; contracts/invoicing/payouts handled; $500 referral programme | A | Read | Vendor describing its own product |
| S05 | [Go Fractional playbook site](https://playbook.gofractional.com) | n/a | Referenced for structuring items (weekly bandwidth, overage rates, 30/60/90, decision rights, renewal triggers) only via the PDF excerpt; the site itself returned no readable text | - | Gap | JavaScript shell; not used as evidence |
| S06 | [Fractional Jobs, The Fractional Work Report 2026](https://www.fractionaljobs.io/the-fractional-work-report) | 2026 | n=1,733 survey responses (810 active, 235 past, 688 aspiring fractionals) + 44,433 profiles + 1,447 postings; mean hourly: Finance/Engineering $229, Operations $215, Marketing $209, all executives $223 (n=546); 46% mainly retainer; 64% two or more clients; 94% won clients via referrals; 72% first client via network; 98% say AI made them more efficient (62% substantial gains), 30% serve more clients because of AI, 38% say AI expertise helped win work; 90% 'not interested in returning to full-time work' (intent, not behaviour); typical posting about 10 h/wk, median 21 client-facing h/wk; engagements mostly 6-12 months (60% six months or longer); 91% do hands-on execution, 83% Director-level or above, 87% have 11+ years' experience; AI/ML at 5% in its top-industries list (the page does not say whether of companies or postings); 24% of its clients explicitly asked for AI-native skills | C | Read | Commissioned by a company that sells fractional talent; third-party analysis claimed; no AI-specific or CTO-specific rates, no typical retainer, no churn; the page does not say which respondent group the 90% covers |
| S07 | [PRWeb press release on the Fractional Jobs report](https://www.prweb.com/releases/fractional-hiring-surges-149-as-businesses-rethink-the-full-time-standard-report-302852670.html) | 2026-08-18 | Hiring demand +149% YoY headline | C | Read | Press release by the report's sponsor |
| S08 | [fractionaljobs.io (homepage / fee terms)](https://www.fractionaljobs.io) | n/a | Intended to confirm placement-fee terms | - | Blocked | Fetch refused (provenance); fee terms rely on a competitor's claim ([S16]) |
| S09 | [A.Team, What an AI engineer costs in 2026](https://www.a.team/talent/guides/ai-engineer-rates) | 2026 | US senior AI engineer contractor $130/$165/$200 (low/mid/high); AI architect or CTO-tier $200/$220/$240+; Eastern Europe senior $80/$110/$140; LatAm senior $65/$95/$125; AI premium 10-25% on contractor hourly in the key takeaways (body text: roughly 10-15% for US senior contractors and 20-30% for the architect tier) | C | Read | Vendor selling engineers; 'low/mid/high' are not defined on the page, which says the ranges come from A.Team's engagement data tracking seller-quoted rates |
| S10 | [A.Team, What a fractional CTO costs in 2026](https://www.a.team/talent/guides/fractional-cto-rates) | 2026 | Advisory 10-15 h/month at $4-10k; active 20-40 h/month at $10-25k; interim 40+ h/month at $20-40k | C | Extract | Vendor; units are hours per MONTH and imply $250-1,250/h, inconsistent with hours-per-week sources; excluded from pricing |
| S11 | [Second Talent, Cost to hire a freelance AI engineer](https://www.secondtalent.com/cost-to-hire/ai-engineer/) | updated 2026-09-24 | US freelance AI engineer junior $95-142, mid $119-185, senior $155-235/h; India mid-level $28-72/h ($4,480-11,520/month at 160 h); AI/ML engineer +37% vs full-stack baseline | C | Read | Vendor (offshore staffing); modelled bands |
| S12 | [Second Talent, US freelance LLM developer hourly rate](https://www.secondtalent.com/resources/freelance-llm-developer-hourly-rate-us/) | October 2026 | Senior (7-10 years) US freelance or contract LLM developer $155-235/h (dated October 2026); employees $170-260/h; agencies $295-490/h; the page calls LLM pricing 'the least settled rate on this page' and shows no trend or 2023 figure. An earlier search extract showed $145 (2023) to $210 (2026) with slowing growth; that did not reproduce and is not used | C | Read | Vendor; modelled bands; the earlier extract's 2023 figure and 'median senior' figures ($210-$275) were not found on re-fetch |
| S13 | [Second Talent, AI engineer rate card India](https://www.secondtalent.com/developer-rate-card/ai-engineer-india/) | updated 2026-09-14 | International clients typically pay $50-75/h for senior India-based AI engineers; junior (0-2 y) $25-35 contract / $31-44 freelance; freelance ~25% above contract; senior salaries Rs 30-70 LPA | C | Extract | Vendor; table partly truncated in extract |
| S14 | Groovy Web, AI consulting rates 2026 and fractional AI CTO cost: [link 1](https://groovyweb.co/blog/ai-consulting-rates-2026) · [link 2](https://www.groovyweb.co/blog/fractional-ai-cto-cost-usa-2026) | 2026 | Boutique $150-300/h; Big 4 $300-600; offshore AI-first $22-50; fractional AI CTO $200-500/h or $6-20k/month (1-3 days/week); fractional CTO retainer $5-15k | C | Extract | Agency marketing |
| S15 | [Fractionus, FAQ](https://fractionus.com/faq) | 2026 | US fractional executive retainers 'typically' $8,000-22,000 per month; engagements 'most' run 6-18 months; fractionals are independent contractors | C | Extract | Placement vendor; generic across all executive roles, not AI-specific; no method stated |
| S16 | [Fractionus, Fractional Jobs vs Fractionus comparison](https://fractionus.com/compare/fractional-jobs-vs-fractionus) | 2026 | Claims Fractional Jobs has 'no platform fees or percentage markup; you contract and pay the fractional directly' | C | Read | A competitor describing Fractional Jobs; fractionaljobs.io itself was blocked, so the fee claim is unverified |
| S17 | [Vantage Point, Fractional AI Architect support package](https://vantagepoint.io/packages/support-fractional-ai-architect) | 2026 | 8/16/32 h per month for $1,800/$3,400/$6,400 ($225/$212.50/$200 per h); 3-month minimum; no rollover; billed monthly in advance; acceptance = monthly hours statement; client supplies project owner 2-4 h/week and approvals within 3 business days; no notice terms stated | A | Read | One firm's own published prices (Cockrum Consulting LLC, Dallas/Sofia); scoped to Salesforce, HubSpot and Claude work; n=1 |
| S18 | [Lemon.io, LLM developer rate calculator](https://lemon.io/rate-calculator/llm-developers/) | 2026 | US senior LLM developers $61-85/h (outlier low) | C | Extract | Vendor; inconsistent with every other source |
| S19 | [Fiverr, cost to hire AI experts](https://fiverr.com/resources/guides/costs/ai-expert) | 2026-05-21 | AI strategy consultants $10-125/h; AI agent development about $295 per fixed project (marketplace low end) | C | Extract | Commodity marketplace |
| S20 | [Alice Labs, AI consulting rates 2026](https://alicelabs.ai/en/insights/ai-consulting-rates-2026.md) | 2026 | Project pricing $20k to $2M+ by tier | C | Extract | Vendor marketing |
| S21 | [Softude, AI consulting cost in 2026](https://www.softude.com/?p=14220) | 2026-07-28 | AI roadmap/strategy engagements start around $15,000 | C | Extract | Vendor marketing |
| S22 | [Navtechy, hire an AI developer in India](https://navtechy.com/blog/hire-ai-developer-india) | 2026 | India freelance: junior $15-25, mid $30-50, senior (6+ y, production LLM) $60-100 per hour | C | Extract | Indian dev shop; self-reported |
| S23 | [Prakash Infotech, AI developer cost](https://prakashinfotech.com/?p=66581) | undated | Generative AI work: India $50-90/h vs USA $120-200/h | C | Extract | Vendor; undated |
| S24 | [Winvesta, AI freelancers earn $200/hr but lose 15% to payment fees](https://winvesta.in/blog/businesses/ai-freelancers-earn-200hr-but-lose-15-to-payment-fees) | 2026 | India-based AI freelancers: senior $120-200/h on premium platforms, mid-level $50-80 direct; payment friction PayPal ~8-9%, Payoneer ~3-4% (up to 6% direct), Wise ~2-2.5%, SWIFT 3-8% | C | Read | Payments vendor; no dataset behind rate claims |
| S25 | [Upwork, hire freelancers in India](https://www.upwork.com/hire/in/) | 2026 | India beginners $10-25/h; nothing AI-specific | C | Read | Marketplace page |
| S26 | [Flexiple, hire LLM engineers in Chennai](https://flexiple.com/hire/llm/chennai) | 2026 | 'Market median' about $12/h, derived from salary - a modelled figure, not a market rate | C | Extract | Disregarded |
| S27 | [freelancermap, Freelancer-Kompass 2026 (PDF)](https://www.freelancermap.de/files/survey/freelancer-kompass-2026.pdf) | survey 2025-11-17 to 2026-02-08 | n=5,412 (DACH); avg rate EUR 103; 42 h/week; billable days a year (24% under 50, 14% 50-100, 16% 101-150, 18% 151-200, 15% 201-250, 7% 251-300, 6% over 300); non-billable time (34% under 10%, 46% 10-20%, 20% over 20% of working time); 43% no secured workload; plans to return to employment not reported; gross profit 32% <EUR 25k and 13% >EUR 125k; 85% use AI tools; monthly project income EUR 6,653 | B | Read | Platform operator; self-reported; DACH; no AI-specific rate (data/analytics EUR 108); income label ambiguous (net vs gross) |
| S28 | [freelancermap, Freelancer-Kompass landing page](https://www.freelancermap.de/freelancer-kompass) | 2026 | EUR 103 average; 84% would become self-employed again (willingness to stay, not return-to-employment data) | B | Read | As above |
| S29 | [heise.de, Freelancers average 104 euros (2025 edition)](https://heise.de/-10325758) | 2025 | 2025 edition: EUR 104/h and EUR 8,022 gross per month - shows the income label differs by edition | C | Extract | Secondary coverage |
| S30 | [IT Jobs Watch, Generative AI contract rates (UK)](https://www.itjobswatch.co.uk/contracts/uk/generative%20ai.do) | 6 months to 2026-10-20 (first read); 6 months to 2026-10-24 (re-read) | Median day rate GBP 550 (900 rates quoted); P10 400 / P25 463 / P75 675 / P90 788; London median 575; same-period medians 550 (2025), 613 (2024). Re-read 2026-10-25: 908 rates, P10 401, P25 463, P75 675, P90 788, London 575; same-period medians 550 (2025) and 625 (2024) | B | Read | Job-advert quoted rates, not signed contracts; not tiered by seniority; live page, and the 2024 comparison moved from 613 to 625 between reads |
| S31 | [YunoJuno, Contractor rates in 2026](https://www.yunojuno.com/blogs/contractor-rates-in-2026-ai-cloud-and-product-skills-continue-to-command-premium-rates) | 2026 | >182,000 data points; UK avg day rates Cloud GBP 566, Software 533, Product 521, Strategy 518; AI premium ~26% (software) and ~17% (project management); 'AI skills do not yet create a significant rate premium' market-wide; >80% of bookings direct | B | Read | Platform operator; 2024-25 data |
| S32 | [Studeria, TJM consultant IA 2026 (France)](https://www.studeria.fr/articles-de-blog/tjm-consultant-ia-2026-tarifs-grille) | 2026 | France AI TJM EUR 600-900 (confirmed), EUR 1,000-1,500 (gen-AI / agent experts), IT average EUR 520 | C | Read | Blog citing Malt, Hays and Free-Work |
| S33 | [9am, freelance rates Europe 2026](https://www.9am.works/freelancer-academy/blog/freelance-rates-europe-2026) | 2026 | Netherlands avg EUR 83/h; UK GBP 385-566/day with 17-26% AI premium (recycles freelancermap and YunoJuno) | C | Extract | Platform with a commercial stake |
| S34 | [beancount.io, India freelancer tax: Section 44ADA, presumptive taxation, GST threshold](https://beancount.io/blog/2026/08/04/india-freelancer-tax-section-44ada-presumptive-taxation-gst-threshold-guide) | 2026-08-04 | 44ADA mechanics; GST registration threshold Rs 20 lakh; export of services zero-rated with LUT | C | Read | Accounting-software blog |
| S35 | [Tata Capital, personal income tax slabs](https://www.tatacapital.com/blog/wealth-services/personal-income-tax-slabs/) | 2026 | New-regime slabs and s.87A rebate | C | Read | Financial-services blog |
| S36 | [BankBazaar, income tax slabs FY2026-27](https://mobikwik.bankbazaar.com/tax/income-tax-slabs.html) | 2026 | New-regime slabs nil/5/10/15/20/25/30% at Rs 4/8/12/16/20/24 lakh; s.87A rebate Rs 60,000 up to Rs 12 lakh; cess 4%; salaried standard deduction Rs 75,000 | C | Read | Lists 5% surcharge for Rs 50L-1Cr, conflicting with the ICAI page (10%); its FAQ rebate threshold (Rs 7 lakh) conflicts with its own table |
| S37 | [ICAI Palakkad branch, Rates of income tax (AY 2026-27)](https://palakkad.icai.org/resources/Utilities/Rates_of_Income_Tax/Rates_of_Income_Tax.aspx) | page footer 2025-03-10 | Individual surcharge 10% (Rs 50L-1Cr), 15% (1-2Cr), 25% (>2Cr); cess 4% | B | Read | Does not split old/new regime or state the new-regime cap; page older than the figures it covers |
| S38 | [ICAI NIRC, The New Income Tax Act 2025 (presentation)](https://nirc.icai.org/wp-content/uploads/2026/05/The-New-Income-Tax-Act-2025-nanda-sir.pdf) | 2026-05 | Income-tax Act 2025 effective 2026-04-01 (repeals 1961 Act); s.58 consolidates old 44AD/44ADA/44AE; professionals 50% of gross receipts up to Rs 50 lakh, Rs 75 lakh if cash receipts <=5%; 'Tax Year' concept | B | Read | Slide deck; does not say the values are unchanged from 44ADA |
| S39 | [taxaj, Presumptive taxation 44ADA for professionals](https://www.taxaj.com/learn/presumptive-taxation-44ada-for-professionals-50-lakh-limit/) | 2026-08-22 | 50% deemed profit; Rs 50 lakh / Rs 75 lakh (cash <=5%); 'technical consultancy' may qualify, depends on nature of services; above limit regular books and audit | C | Read | Hedges on IT-consultant eligibility; cites the old section number |
| S40 | [ValutaFX, INR/USD history 2026](https://www.valutafx.com/history/inr-usd-2026) | 2026-10-20 | USD 1 = INR 94.716 on 2026-10-20; 2026 range 0.0103-0.0111 USD per INR | C | Read | Rate aggregator |
| S41 | [S.S. Rana, MeitY notifies final DPDP Rules 2025](https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/) | 2025-11 | Rules notified 2025-11-13 (G.S.R. 846(E)); Board rules at once; consent-manager rule 2026-11-13; main fiduciary obligations 2027-05-13; processors act on fiduciary directions | B | Read | Law-firm summary; processor-contract requirements not described |
| S42 | [KPMG, Rev. Proc. 2025-32 inflation adjustments for 2026](https://kpmg.com/us/en/taxnewsflash/news/2025/10/tnf-rev-proc-2025-32-inflation-adjustments-for-2026-individual-taxpayers.html) | 2025-10 | 2026 single brackets 10% to $12,400, 12% to $50,400, 22% to $105,700, 24% to $201,775, 32% to $256,225, 35% to $640,600, 37% above; standard deduction $16,100 | B | Read | Secondary summary of the Revenue Procedure; QBI thresholds not covered |
| S43 | [NerdWallet, self-employment tax](https://www.nerdwallet.com/taxes/learn/self-employment-tax) | 2026 | SE tax 15.3%; 92.35% base; Social Security wage base $184,500 for 2026; half deductible; 0.9% additional Medicare above $200,000 (single) | C | Read | Consumer finance site |
| S44 | [beancount.io, Section 199A QBI deduction after OBBBA](https://beancount.io/blog/2026/06/01/section-199a-qbi-deduction-pass-through-owners-obbba-permanent-2026-thresholds-sstb-phase-out-w2-wages-ubia-form-8995-aggregation-guide) | 2026-06-01 (updated 2026-08-14) | QBI deduction permanent; 2026 phase-in starts $201,750 (single), range $75,000; consulting is a specified service trade (SSTB) | C | Read | Blog; statute not read |
| S45 | [Becker's Payer, states ranked by average ACA benchmark premiums in 2026](https://www.beckerspayer.com/payer/aca/states-ranked-by-average-aca-benchmark-premiums-in-2026/) | 2025-11-20 | US average benchmark (second-lowest silver, age 40) $625, per KFF; range $401 (NH) to $1,299 (VT) | C | Read | Secondary report of KFF; article does not say 'monthly' explicitly |
| S46 | [Insureon, cost of insurance for IT consultants](https://www.insureon.com/technology-business-insurance/it-consultants/cost) | updated 2026-06-12 | Median annual premiums: tech E&O $899, cyber $1,540, general liability $369, BOP $638; tech E&O limits $1M per occurrence / $1M aggregate with a $2,500 deductible (general liability $1M / $2M, $500 deductible) | C | Read | Insurance broker; medians of quotes for small IT consultants; not AI-specific; page says tech E&O bundles cyber yet lists cyber separately; limits and deductible describe the average policy the broker sells |
| S47 | [Antenna, Independent consultant survey (2019 eBook)](https://www.lemonly.com/general-uploads/Work/191010_Antenna_ConsultantSurvey_eBook_Final.pdf) | 2019 | n=80 consultants earning $100k+; avg rate $174, median $150; Technology avg $258 (chart labels garbled; mapping inferred); agency-sourced share vs rate ($223 at 0% down to $113 at 100%); 100% network; most won nothing via platforms; 14% of those with a website get meaningful inquiries; 51% T&M, 30% fixed, 19% retainer; 78% name business development a top-three pain | C | Read | Old, small, selected on success (about 100 responded, 80 kept after a quality scrub); chart labels are garbled in the PDF text, so the technology average is an inferred mapping |
| S48 | [Consulting Success, consultant marketing study](https://www.consultingsuccess.com/consultant-marketing-study) | 2024 (year ambiguous) | List of >50,000 consultants, responses unreported; most-clients methods: phone 16%, direct mail 15%, networking 14%, joint ventures 12%, referrals 8%, blogging/SEO 7%, LinkedIn 4%; highest-income method (2019 data): referrals 38%, networking 18%; 70% get zero website leads | C | Read | Coaching business with a stake in the answer; respondent count unknown |
| S49 | [Consulting Success, how consultants get paid](https://www.consultingsuccess.com/how-consultants-get-paid) | published 2025-06-11, updated 2026-03-20 | Monthly income bands 22% <$2k / 20% $2-5k / 20% $5-10k / 32% $10-45k / 3% $45-100k / 2% >$100k; specialists 42% earn $10k+; 73% of non-specialists $5k or less; value-based pricers 51% vs hourly 39% with $10k+ projects; 34% of consultants report profit margins above 70% (specialists 54%, non-specialists 35%; margin definition not stated) | C | Read | Same publisher; survey year and n not stated; gross; not AI-specific |
| S50 | [Consulting Success, top consulting statistics](https://www.consultingsuccess.com/?p=78868) | undated | Over 50% of consultants reach their previous employee income level within 2 years of starting; boutique-firm average gross margin 20-40%; most common average project value $5k-$15k and $15k-$50k (33% in $15k-$50k, 6% over $100k); 79% are trying to raise fees and 25% will lower fees to win clients; 88% do not list fees on their website; 70% get zero website leads or calls per month | C | Read | Coaching business with a stake in the answer; undated; mostly management, strategy and operations consultants, not AI; response count not stated |
| S51 | [Consulting Success, consulting proposal close rate](https://www.consultingsuccess.com/consulting-proposal-close-rate) | 2026 | Claims coaching clients' close rates rise from ~30% to ~70% of proposals | C | Read | Author's coaching experience; no sample; no discovery-call conversion given |
| S52 | [Sam Landenwitsch, Report: the surprising truth about finding clients](https://samlandenwitsch.substack.com/p/report-the-surprising-truth-about) | undated | Nonprofit/social-impact consultants: about 80% of engagements from personal networks; cold outreach, platforms and referral programmes ranked lowest; open source not mentioned | C | Read | Newsletter survey, n unstated, different sector; author sells proposal templates |
| S53 | [MBO Partners, 2025 State of Independence press release](https://www.mbopartners.com/blog/press/2025-state-of-independence-reveals-growing-talent-strategy-for-businesses) | 2025-09-09 | 5.6M independents earn over $100k; 42% name online platforms as primary way to find work; 74% used generative AI | B | Extract | MBO is a Beeline (workforce software) company |
| S54 | Coverage of MBO Partners 16th State of Independence (2026): [link 1](https://www.selfemployed.com/news/mbo-partners-state-of-independence-2026/) · [link 2](https://www.staffingindustry.com/news/global-daily-news/more-independent-workers-go-full-time-plan-to-continue) | 2026-09-28 | 74.9M independents; 5.8M earn $100k+; n=4,557 US adults incl. 2,063 independents (April 2026); full-time independents are 22% of the full-time US workforce (10% in 2019), with no absolute count in either article; 74.9M total (about 72.9M a year earlier); 5.8M at $100k+ (3M in 2020); 78% plan to continue | C | Read | Secondary coverage. The 27.6M full-time count used in the body is MBO's 2025 figure from an aggregator ([S55]), not from these pages |
| S55 | [Digital Applied, gig economy and freelance statistics 2026](https://digitalapplied.com/blog/gig-economy-freelance-statistics-2026-data-points) | 2026-07-08 | Upwork: full-time skilled freelancers median $85,000 (attributed to Upwork's Future Workforce Index, April 2025; data year not stated, probably 2024); MBO's 2025 report (15th edition, 2025-09-09): full-time independents 'held stable' at 27.6M of 72.9M, 5.6M earning $100k+ | C | Read | Aggregator; originals not traced |
| S56 | Upwork Future Workforce Index 2026 (company release and finviz copy): [link 1](https://investors.upwork.com/news-releases/news-release-details/upworks-future-workforce-index-2026-how-ai-redefining-value-work) · [link 2](https://finviz.com/news/367958/upworks-future-workforce-index-2026-how-ai-is-redefining-the-value-of-work-as-skilled-freelancing-accelerates) | 2026-07-14 | AI-work freelancers earn 34% more per hour; gen-AI/creative contract starts +90% but per-contract earnings -13%; complex AI-augmented work earnings +45%; AI-augmented professional services volume +72%, earnings +22%; freelancing share 28% to 38%; n=2,400 US skilled workers, Mar-Apr 2026; 'AI Orchestrator' framing | C | Read | Marketplace with a stake; platform-wide averages, not consultant-specific; official press-release URL on upwork.com errored on fetch |
| S57 | [9am, platforms became the number one client channel for freelancers](https://www.9am.works/freelancer-academy/blog/platforms-number-one-client-channel-freelancers) | 2026 | Compiles MBO (42% platforms primary; platform use 37% to 63% 2020-2025), YunoJuno (>80% of bookings direct), freelance.de (26% need >3 months to land a project; 3% within a week), freelancermap (62% name acquisition biggest obstacle) | C | Read | Platform with a commercial stake; its own text says platforms are most used but not highest-converting |
| S58 | [shno.co, retainer pricing statistics](https://www.shno.co/marketing-statistics/retainer-pricing-statistics) | 2026 | 13% of consultants use monthly retainers; 59 of 115 agencies cite scope creep as top retainer profitability problem (SE Ranking survey); retainer-led agencies report 30-50% higher margins | C | Extract | Aggregator; originals not traced |
| S59 | [Harvest, average utilization rate for consulting](https://www.getharvest.com/calculators/average-utilization-rate-consulting) | 2026 | Consulting billable utilisation 67.7% worldwide (2023, unattributed); about 71% for consulting and professional services (SPI Research); no solo benchmark | C | Read | Software vendor; firms, not solos |
| S60 | Webtonic, fractional CMO tenure and churn (Fractional Pulse): [link 1](https://www.webtonic.io/blog/fractional-cmo-tenure-churn) · [link 2](https://www.webtonic.io/blog/fractional-cmo-benchmarks-kpis) | 2026 | Typical 6-12 month initial term then month-to-month with 30-day notice on either side; equity-only deals work only in a narrow band (pre-revenue company, about 4-8 advisory hours a month, an operator with cash flow elsewhere) and otherwise 'fail within six months'; early exits from scope, compensation and measurement mismatch. Sibling benchmarks page: median fractional retainer $10-12k a month for 15-25 hours a month (Fractional Pulse, updated Aug 2026); Go Fractional typical scope about 9 h/week; no hourly rate stated | C | Read | Agency blog; CMO-focused, not AI. A '$12,000 for 20 h/month = $600/h; 20 h/week = $150/h' example in my first read did not reproduce on 2026-10-25 and is no longer used |
| S61 | [Holloway, typical startup advisor equity levels (FAST tiers)](https://holloway.com/g/equity-compensation/sections/typical-startup-advisor-equity-levels) | 2026 | Standard/Strategic/Expert tiers: idea 0.25/0.50/1.00%, startup 0.20/0.40/0.80%, growth 0.15/0.30/0.60%; Carta: most grants 0.2-1.0%; usual vesting 2 years with 3-month cliff | B | Read | Fully-diluted basis not confirmed |
| S62 | [Gartner press release, over 40% of agentic AI projects will be cancelled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) | 2025-06-25 | Forecast (not an observation) that >40% of agentic AI projects are cancelled by end-2027; poll of 3,412 webinar attendees; 'only about 130 of thousands of agentic AI vendors are real' | A | Read | Primary for what Gartner says; it is a forecast |
| S63 | [CustomerThink, debunking the myth of 95% GenAI failure](https://customerthink.com/the-great-genai-divide-debunking-the-myth-of-95-failure/) | 2025-11-06 | Critique: MIT NANDA '95% fail' rests on ~150 surveys and 52 interviews with a narrow failure definition | C | Read | Opinion piece |
| S64 | [CFO Dive, Deloitte refunds Australian government over AI errors](https://www.cfodive.com/news/deloitte-refunds-60k-report-ai-errors-australian-government-accounting/803321/) | 2025-10-21 | Contract ~A$440,000 (AusTender, Dec 2024); refund over A$97,000 (~US$63,000), less than a quarter; fabricated court-judgment quote and non-existent references | B | Read | Trade press relaying AP and the department; article does not say whether Deloitte disclosed AI use |
| S65 | [Fast Company (republished from The Conversation), companies may be held liable when AI harms their clients](https://www.fastcompany.com/91623691/companies-liable-ai-errors) | 2026-10-17 | Commentary: responsibility for AI errors rests with the professional relying on the output; cites Deloitte, Air Canada tribunal, Walters v. OpenAI, Keene v. Google, Clinco v. Commissioner; no contract-term guidance | C | Read | Commentary; case details as summarised by the authors |
| S66 | [Upwork Help, freelancer service fees](https://support.upwork.com/hc/en-us/articles/211062538) | retrieved 2026-10 | Freelancer fee variable 0-15% per contract, shown before proposal and fixed for that contract; direct contracts lower; enterprise typically 10% | A | Read | Upwork describing its own fees |
| S67 | [Golance, Upwork fees explained 2026](https://golance.com/blogs/upwork-fees-explained-2026) | 2026-05 | Replaced the 20/10/5% tiers (2025-05-01); client marketplace fee 5% Basic (3% eligible US), 8-10% Business Plus; Connects $0.15; Freelancer Plus $14.99 or $19.99 depending on source | C | Extract | Third-party explainer; Freelancer Plus price conflicts across sources |
| S68 | [Toptal, freelance jobs FAQ](https://www.toptal.com/freelance-jobs/faq) | retrieved 2026-10 | Talent sets own rate; no fee charged to talent; availability 0-50 h/week | A | Read | Silent on client markup and on non-circumvention |
| S69 | aiproposer.com Toptal vs Upwork; thegtmdirectory.com Toptal; rapidevelopers.com Toptal: [link 1](https://aiproposer.com/comparisons/toptal-vs-upwork) · [link 2](https://thegtmdirectory.com/tools/toptal/md) · [link 3](https://rapidevelopers.com/clone/toptal) | 2025-2026 | Client markup undisclosed; estimates 30-40% (aiproposer) and ~50% (thegtmdirectory); contracts reportedly bar working directly with Toptal-sourced clients (rapidevelopers) | C | Extract | Secondary/competitor pages; markup is an estimate |
| S70 | [Braintrust, frequently asked questions](https://usebraintrust.com/frequently-asked-questions) | retrieved 2026-10 | Page contained no fee information | - | Read | Gap: no official fee statement found |
| S71 | [Braintrust, bring your own talent](https://usebraintrust.com/blog/bring-your-own-talent) | retrieved 2026-10 | Talent keeps 100% of earnings on their own clients | A | Read | Vendor describing its own programme |
| S72 | alignlist.com Braintrust; coinmarketcap.com academy; flexiple.com Braintrust review: [link 1](https://alignlist.com/companies/braintrust) · [link 2](https://coinmarketcap.com/academy/pt/article/what-is-braintrust-brtrst) · [link 3](https://flexiple.com/reviews/braintrust) | 2025-2026 | 0% talent fee; client-side 10% (CoinMarketCap) to 15% on top (Flexiple); 15% conversion fee if hired full-time within six months | C | Extract | Directories and a competitor; client fee conflicts (10% vs 15%) |
| S73 | [Catalant, is Catalant right for me](https://catalant.com/managing-your-practice/is-catalant-right-for-me) | retrieved 2026-10 | Winning experts typically 10-20 years' experience; experts are paid whether or not the client pays Catalant | A | Read | Official page gives no fee figure |
| S74 | fitgap.com Catalant; yespress.io Catalant: [link 1](https://us.fitgap.com/products/014434/catalant) · [link 2](https://yespress.io/catalant) | 2026 | Catalant fee 20-30% of total project fees (about 25-43% markup on expert fee); yespress cites a 20-35% range from Catalant's consultant guide | C | Extract | Secondary; range differs by source |
| S75 | yespress.io Contra; subscribed.fyi Contra review: [link 1](https://yespress.io/contra) · [link 2](https://subscribed.fyi/contra/reviews/contra-review-7667) | 2026 | 0% commission on freelancer earnings; free tier; Pro $29/month or $199/year; some client payment fees on free-plan transactions | C | Extract | Secondary; official pricing page blocked (see next row) |
| S76 | [Contra, pricing page](https://contra.com/pricing) | n/a | Intended to confirm pricing | - | Blocked | Fetch refused (provenance) |
| S77 | Bonsai, pricing page and help article: [link 1](https://www.hellobonsai.com/pricing) · [link 2](https://help.hellobonsai.com/en/articles/455542-bonsai-s-pricing-and-subscription-plans) | retrieved 2026-10-23 (help article dated 2026-07-13) | Per user per month, monthly / billed yearly: Basic $15/$9, Essentials $25/$19, Premium $39/$29, Elite $59/$49 (Elite minimum 3 users); proposals, contracts and invoicing from Essentials up; processing fees vary by payment method and provider, no amounts given; free trial; Bonsai Tax add-on | A | Read | Vendor describing its own product; pricing page undated; contract-template wording not reviewed |
| S78 | FSuite (searched, not found) (no URL) | n/a | Two searches ('FSuite fractional executives marketplace how it works fees fractional CTO'; 'FSuite fractional executive platform') returned no FSuite page; results were jobbers.io, Fractionus comparison pages and generic fractional-executive articles | - | Gap | Not catalogued; no fee or model claim is made about FSuite |
| S79 | [Stripe Invoicing pricing (Bulgaria English page)](https://stripe.com/en-bg/invoicing/pricing) | retrieved 2026-10-23 | Starter 0.4% per paid invoice; Plus 0.5% (adds quotes); card and bank-debit processing fees are charged separately under Stripe Payments pricing | A | Read | Vendor's own page; regional (Bulgaria) version, a US page was not fetched |
| S80 | [Wise Business pricing (India page)](https://wise.com/in/pricing/business) | retrieved 2026-10-23 | Free to open; receiving via local account details (USD ACH and wire, GBP, EUR) free; SWIFT receipt fixed fees USD 6.11, GBP 2.16, EUR 2.39; the page gives no INR conversion or withdrawal percentage | A | Read | Vendor's own page; INR conversion cost not retrievable, so the 2-2.5% Wise figure elsewhere rests on a payments vendor ([S24]) |
| S81 | [Payoneer, fees](https://www.payoneer.com/fees/) | retrieved 2026-10-23 | Receiving by bank transfer free into a local-currency receiving account, 1% (minimum $1) into a non-local-currency account; EU/UK bank transfers 1%; US ACH debit 1%; payer card up to 3.99% + $0.49; withdrawal to bank 1.2%-4% with or without conversion ($1.50 same-country); conversion 1.2%-4% by corridor; fees vary by territory and account | A | Read | Vendor's own page; region not stated for the general rows; https://www.payoneer.com/legal/fees/ failed to fetch |
| S82 | [Archive Team wiki, Docracy](https://wiki.archiveteam.org/index.php/Docracy) | retrieved 2026-10 | Shutdown announced 2018-02-27 for 2018-07-01; status 'Offline'; but the site was observed operating in 2021 | C | Read | Conflicting status; treat as legacy |
| S83 | [Freelancers Union, Contract Creator announcement](https://blog.freelancersunion.org/2024/05/14/introducing-the-freelancers-union-contract-creator/) | 2024-05-14 | Free beta contract generator for scope, payment terms and deadlines; no IP clause mentioned | A | Read | Publisher describing its own tool |
| S84 | [GitHub okfn/contracts](https://github.com/okfn/contracts) | retrieved 2026-10 | Open Knowledge Foundation's own contract documents; licence file unnamed; no consulting template or AI terms confirmed | C | Read | Organisation-specific |
| S85 | [GitHub dxw/contracts](https://github.com/dxw/contracts) | retrieved 2026-10 | UK agency dxw's own terms of service and agreements in Markdown (23 stars); LICENCE.md present but text not visible; clause contents not visible | C | Read | Agency-specific; could not confirm IP, liability or AI clauses |
| S86 | [OpenAgreements](https://openagreements.org) | retrieved 2026-10 | Free legal reference library; 125 templates incl. Common Paper Professional Services Agreement and Independent Contractor Agreement, Common Paper NDAs; page content CC BY 4.0; 'legal research, not legal advice' | C | Read | Template licences are source-specific |
| S87 | [GitHub open-agreements/open-agreements](https://github.com/open-agreements/open-agreements) | retrieved 2026-10 | Project code Apache-2.0; content keeps its source licence (check each template's metadata.yaml); 57 stars | C | Read | Catalogue not visible in extract |
| S88 | [OpenAgreements, Bonterms Professional Services Agreement entry](https://openagreements.org/templates/bonterms-professional-services-agreement) | retrieved 2026-10 | Bonterms PSA v1.2 cover page includes 'Deliverables Type: licensed or assigned'; licence shown as CC BY 4.0 and CC0 (conflict) | C | Read | Standard terms at bonterms.com were not retrieved |
| S89 | [Common Paper, Professional Services Agreement v1.1 (CC BY 4.0)](https://commonpaper.com/standards/professional-services-agreement/1.1/) | v1.1 | s8.1 caps (General Cap / Increased Cap; amounts set on the cover page); s8.2 damages waiver (lost profits, consequential and similar); s8.3 caps do not apply to Unlimited Claims and the waiver does not apply to Increased Claims or a confidentiality breach; s9.1-9.2 mutual defend-and-indemnify duties for Covered Claims, s9.4 exclusive remedy (covered claims not listed in the text retrieved); s2.1 deliverables assigned excluding pre-existing and third-party materials; s2.3 non-exclusive, non-transferable, perpetual, irrevocable licence to use pre-existing materials only as necessary to use the deliverables; s2.6 reservation of rights; s1.3 change orders not binding until agreed in writing; s1.5 subcontractors only with customer permission; s4.1 fees non-refundable except the prorated refund of prepaid fees on specific terminations; s5.2(a) 30-day cure, s5.2(c) termination for any reason only if no SOW is active, s5.3(e) refund of unearned prepaid fees unless the provider terminates under s5.2(a); s6.3(a)-(d) warranties (professional manner, non-infringement, conformity to the SOW, rights to convey); s6.4 re-performance within 45 days, else termination of the affected SOW with a prorated refund, the only remedies for the s6.3(c) warranty; s7.1 disclaimer; s10.1 each party carries insurance for the term plus six months, date-of-occurrence form; s12.7 headed 'No Publicity' (text not retrieved); s12.9 independent contractors; no non-solicit in the text retrieved | A | Read | Template; cap amounts and covered claims may be set on the cover page, which was not retrieved. A second fetch on 2026-10-25 corrected my first paraphrase of s4, s5 and s6.4 |
| S90 | [Common Paper help centre, General Cap Amount](https://help.commonpaper.com/en/articles/6901520-general-cap-amount) | retrieved 2026-10 | Default General Cap: 1x fees paid or payable in the 12 months before the claim | A | Read | Template default, not a market statistic |
| S91 | [Common Paper help centre, Increased and Unlimited Claims](https://help.commonpaper.com/en/articles/6901510-increased-and-unlimited-claims-optional) | retrieved 2026-10 | Increased Claims typically cover privacy, security, confidentiality, gross negligence and wilful misconduct; default Increased Cap 5x fees paid or payable in the 12 months before the claim; a claim is Increased or Unlimited, not both; the article gives no examples of Unlimited Claims | A | Read | Template default |
| S92 | [Common Paper, general cap clause statistics](https://commonpaper.com/clause/general-cap) | retrieved 2026-10 | >10,000 contracts: 98% of sales contracts use a multiplier; 92% use 1.0x fees over twelve months; 4% use 0.5x | A | Read | Vendor's own dataset; 'sales contracts', not consulting services; the base for the 92% is not spelled out and no breakdown by contract type is given; the page's example language comes from its Cloud Service Agreement |
| S93 | [Common Paper, AI Addendum v1.0 (overview)](https://commonpaper.com/standards/ai-addendum/) | 2025-08-07 | Topics: data usage, training rights, IP and liability; no clause text in the overview | A | Read | Clause text not retrieved |
| S94 | [Koley Jessen, AI contracting: practical legal guidance](https://www.koleyjessen.com/insights/publications/ai-contracting-practical-legal-guidance-for-growing-businesses) | 2026-02-24 | Secure a broad output licence; do not rely on NDAs to restrict training; IP indemnity must cover outputs and exclusions need scrutiny; super caps for IP indemnity, confidentiality, data security; diligence third-party models and require deprecation notice | B | Read | Law-firm marketing; written from the customer's side |
| S95 | [WCR Legal (Oleg Prosin), eight AI clauses for MSAs](https://wcr.legal/ai-msa-clauses-2026/) | 2026-05-19 | Outputs assigned to client; accuracy disclaimer ('does not warrant the accuracy, completeness, currency or fitness for purpose of AI-generated Outputs'); human-oversight acknowledgement; no training on client data without consent; AI-specific cap of 12 months' fees; resist unlimited AI-output indemnities; flow down model-provider terms | B | Read | Single practitioner's guidance |
| S96 | [Fenwick (Sarah Hopkins), emerging AI exclusions and coverage fragmentation](https://fenwick.com/insights/publications/end-silent-ai-emerging-ai-exclusions-coverage-fragmentation-and-practical-implications) | 2026-06-15 | ISO introduced a generative-AI exclusion for CGL policies in January 2026 (no separate effective date given); some carriers decline AI-output liability under tech E&O; cyber most stable; D&O/EPLI absolute AI exclusions; affirmative AI products early-stage; review policies and seek endorsements | B | Read | Law-firm commentary |
| S97 | [Farella Braun + Martel, work-made-for-hire clauses in contractor agreements (California)](https://www.fbm.com/employment/publications/employment-law-issues-to-consider-before-including-work-made-for-hire-clauses-in-contractor-agreements/) | 2021-04-29 | A work-made-for-hire clause with an individual contractor can make the commissioning party a statutory employer for workers' compensation and unemployment insurance; use assignment instead | B | Read | 2021; California-specific |
| S98 | [Mayer Brown, Supreme Court denies review in AI authorship case](https://www.mayerbrown.com/en/insights/publications/2026/03/supreme-court-denies-review-in-ai-authorship-case) | 2026-03-11 | Cert denied 2026-03-02 in Thaler v. Perlmutter (No. 25-449); D.C. Circuit human-authorship requirement stands; Allen v. Perlmutter pending; prompts alone generally insufficient (Copyright Office, January 2025) | B | Read | Law-firm summary (fetched with a space-separated path; canonical hyphenated URL confirmed by search) |
| S99 | [CMS, EU Digital Omnibus: streamlined AI Act compliance rules now in force](https://cms.law/en/gbr/publication/the-eu-s-digital-omnibus-streamlined-ai-act-compliance-rules-are-now-in-force) | 2026-07 | Published in the Official Journal 2026-07-24, in force 2026-07-27; Annex III high-risk obligations from 2027-12-02, Annex I from 2028-08-02 | B | Read | Law-firm summary; the page calls the second category high-risk AI embedded in regulated products (medical devices, machinery, toys) and does not use the label 'Annex I', which is my mapping (recalled) |
| S100 | [KI-Campus, AI Omnibus recalibrates Article 4 AI literacy](https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory) | 2026 | Article 4 AI literacy recalibrated but still mandatory; GPAI rules apply since 2025-08-02 | C | Read | Education-platform blog |
| S101 | [Holland & Knight, Colorado governor signs SB 26-189](https://www.hklaw.com/en/insights/publications/2026/05/colorado-governor-signs-sb-189) | 2026-05 | SB 26-189 signed 2026-05-14, effective 2027-01-01; repeals and reenacts SB 24-205 around automated decision-making technology; drops reasonable-care duty, risk programmes and annual impact assessments; developer documentation duties; indemnities for one's own discriminatory acts void | B | Read | Law-firm summary |
| S102 | [Checkr policy hub, Colorado AI Act effective date moved to 1 January 2027](https://checkr.com/policy-hub/colorado-updates-ai-act-moving-effective-date-to-jan-1-2027) | 2026 | Corroborates the 2027-01-01 effective date | C | Read | Vendor policy page |
