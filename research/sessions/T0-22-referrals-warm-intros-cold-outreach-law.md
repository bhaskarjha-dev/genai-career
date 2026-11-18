---
id: "T0-22"
title: "Referrals, Warm Introductions and Cold Outreach, Including the Law"
date: "2026-11-11"
status: complete-with-gaps
topic: "referrals-warm-intros-cold-outreach-law"
tags: ["referrals", "cold-outreach", "networking", "outreach-law", "contact-data", "recruiters", "india"]
informs_decisions: ["D-011"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-11"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and fetch; no Anthropic product is in scope"
evidence_window: "2002-07-12 to 2026-11-09"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-22: Referrals, Warm Introductions and Cold Outreach, Including the Law

S-numbers point to rows in the Sources & Evidence Ledger. Grades A, B, C, D, E, M and P follow the protocol. "Read" means I opened the page; "Extract" means I saw only a search extract or summary, which caps the grade at B. The research date is 2026-11-11, the brief's anchor, and every retrieval date in the ledger follows it. Calculations are marked M and show their inputs. Sales-email and recruiter-message benchmarks are labelled proxies, not measurements of candidate outreach.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | Referred candidates reach interview at roughly 10× the inbound rate per application, mostly through selection rather than any tactic. | 0.8 | D |
| P2 | The "70–85% hidden job market" figure has no traceable measurement behind it. | 0.8 | D |
| P3 | No public dataset measures candidate-initiated cold-outreach reply rates. | 0.7 | D |
| P4 | A job seeker's personal message to a named person is mostly outside anti-spam statutes, which target commercial messages, but regulators have not said so. | 0.6 | D |
| P5 | Contact-finder tools find far fewer addresses than their vendors claim. | 0.8 | D |
| P6 | Referral hires quit less and are paid slightly more in peer-reviewed studies. | 0.7 | D |

## Research Question

**Decision (D-011).** How should a GenAI job seeker get referred, get introduced and reach hiring managers, founders and engineers directly, within the law and platform rules, and what does the evidence say about the yield of each route?

**Sub-questions.**
1. What does the referral literature show, with selection separated from information and from any tactic?
2. What does a referral do in an applicant-tracking system (ATS), and how do employers treat strangers and paid referrals?
3. What is measured for warm introductions, alumni networks and cold outreach?
4. How reliable are contact finders, and what are their terms and enforcement history?
5. What do the laws of the EU, UK, US, Canada, India, Singapore and Australia say about a job seeker's unsolicited message?
6. How do recruiters and recruiter-fee scams work, with depth for India?
7. What is the yield per hour by channel?

**Reading applied.**
- "Job seeker" means an individual acting for themselves, not a freelancer pitching services.
- "Referral" means an employee submitting a candidate.
- "Cold outreach" means an unsolicited message to a named person.
- Law items are pointers, not advice.
- Evidence is mostly sector-general; GenAI-specific evidence is thin.

**Method.**
- About 45 searches and 9 page fetches, run 2026-11-11 in English. The CNIL decision was searched in French.
- DEEPEN: Ashby, Gem, Instantly and Pin figures were traced to the vendor pages.
- WIDEN: I added labour-economics journals and regulator or statute pages for seven jurisdictions.
- FALSIFY searches:
  1. The origin of the hidden-market statistic.
  2. Selection in network effects (Mouw).
  3. The "ask before applying" rule against employer documents (GitLab, Greenhouse, Lever).
  4. Cold referrals to strangers.
  5. Any public candidate-to-hiring-manager reply dataset (none found).
  6. Wage penalties for contact-found jobs.
- Sample sizes of the datasets I cite are given in the findings.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Per application, vouched referrals convert far better than inbound: 40% vs 3% to interview and 16% vs 6% from interview to offer. By my arithmetic that is about 6.4 offers per 100 referred applications vs 0.18 per 100 inbound (≈36×); sourced is 1.5 per 100 (≈8×). Gem reports referrals at 11× inbound. The data is descriptive, not causal. | Ashby: 38M applications, 2021–2024 [S1]; Gem: 165M applications, 2021–2025 [S4]; M ratios | B (M) |
| KF2 | Referrals are about 18% of hires from about 1% of applications; inbound is 43–52% of hires; technical roles skew to sourced hires (24% vs 18%). The 70–85% "hidden market" traces to a 1966 claim and a 2016 self-selected poll. Household surveys of contact use (one-third to two-thirds of jobs) measure a different thing. | [S1][S2][S20][S21][S22][S23] | B/C/E |
| KF3 | Peer-reviewed work splits what vendor data merges. (a) Selection: who gets referred. (b) Information: referrals reveal performance and persistence not visible on a CV. (c) Team effects: referrals do better working with their referrer. Lower quit rates recur. Wage premia fade with tenure, and jobs found through family and friends carry a 5–7% wage discount in two datasets. The causal effect of "contacts" is contested. | [S10]–[S13][S17][S18] | A/B |
| KF4 | Incentives shape who is referred. With flat pay, referrers named closer and weaker people (Kolkata lab-in-field). Larger bonuses raised referral volume but lowered quality in an RCT, while the programme cut attrition by 15%. Bonus-driven referrals of strangers deserve a discount. | [S14][S15] | B |
| KF5 | Weak ties matter causally in tech. Randomised experiments on about 20M LinkedIn users (2015–2019) found most job mobility came from moderately weak ties (about 10 mutual connections), with larger effects in digital industries. The authors are LinkedIn-affiliated. | [S16] | B |
| KF6 | In an ATS a referral is a source or origin tag plus referrer attribution. Treatment of someone who already applied is employer-specific. GitLab downgrades a referral to an endorsement, with no bonus, once talent acquisition has progressed the application. Same-function referrals interview more (37% vs 26%) and are hired more (5.2% vs 3.1%) in business roles. | [S3][S24]–[S28] | A/B |
| KF7 | Strangers: GitLab tells employees to decline cold referral requests and excludes strangers from referral status. A self-selected survey (n≈500) rated cold referrals net negative at FAANG-type firms and small startups. Paid referral markets exist, with no outcome evidence. | [S9][S24][S30][S31] | A/C |
| KF8 | No measured candidate-initiated reply or interview rate exists in anything I could open. Proxies: Instantly 3.43% average, 5.5% top quartile, 10.7% top decile (sales email); Pin 4.96% automated and 6.31% recruiter-written email, and 17.08% LinkedIn (recruiter-to-candidate); Huntr trackers 1.95% of 1.24M applications reached interview. Claims of 15–50% for job-seeker cold email trace to vendor blogs. | [S5][S6][S8] | B/C/E |
| KF9 | The 60-send stop rule: 0 replies in 60 bounds the true rate below 4.9% (one-sided 95%). At a true 3% there is still a 16% chance of zero replies in 60. At 3.43% there is an 88% chance of at least one reply. So 60 sends detects rates of 5% or more but cannot separate 0–3%. | M | M |
| KF10 | The statutes reviewed regulate "direct marketing" (EU, UK), "commercial advertisement or promotion" (US), "commercial activity" (Canada), "commercial electronic messages" (Australia) or bulk commercial messages (Singapore). A personal request for work probably falls outside by definition, but no regulator says so. The GDPR household exemption is read narrowly. Canada exempts the first message after a named referral. India's DPDP core duties start on 2027-05-13 or 14. I found no Indian email anti-spam statute. | [S35]–[S47][S60][S61] | A/B (reading: D) |
| KF11 | Contact data: hit rates were 29.8–55.2% in a vendor-run audit of 1.3M lookups, against vendor claims of 92–99%, and a hit is not a deliverable address. CNIL fined Kaspr €240,000 for collecting LinkedIn contact details users had restricted. LinkedIn bans bots and scrapers and has sued ProAPIs and Proxycurl. | [S7][S48][S49][S50] | C/B |
| KF12 | Recruiters are paid by employers (contingency 15–25% of base; retained 25–35% of total compensation); candidates never pay. A payment demand is a scam marker. FTC-reported losses rose from $90M to $501M (2020–2024). India's NCS advisory is dated 2026-11-09. | [S55][S56][S58][S59] | B/C |
| KF13 | India: services firms pay referral bonuses (TCS ₹40,000; Infosys ₹10,000–50,000 by level). GCC hiring is projected at 510,452 jobs in 2026, with 64% needing AI or data skills. No measured Indian referral share exists. Paid referral groups and fraud alerts both exist. | [S31]–[S34][S55][S57] | B/C |
| KF14 | Yield per hour is unmeasured. Illustratively, referral beats cold applying if you can secure a vouched referral in under about 12 hours (about 6 hours if half the lift is selection). Artefact outreach, community and writing are unmeasured. | M from [S1] | M |

## Recommendation

**Decision rules.**

1. **Map vouchable ties first.** List people at each target employer, or one hop away, who have worked with you or seen your work. Ask the closest first, for a named requisition, with a forwardable paragraph (templates in Detailed Findings 12). Prefer a referrer in the same function [S3][S12][S24].
   *Failure mode:* the referrer declines or their credibility is spent; the funnel advantage may be selection rather than effect.
2. **Ask the referrer how their ATS and policy treat someone who has already applied.** Apply first only if told it is fine. If you have already applied, tell the referrer at once and ask for an endorsement [S24]–[S28].
   *Failure mode:* the referral is credited as an endorsement without a bonus, or a duplicate rule locks the source.
3. **Use double opt-in introductions for moderate ties** (about ten mutual connections) [S16].
   *Failure mode:* it burdens the mutual contact, and no yield is measured.
4. **With no tie, apply through the normal channel and send artefact-led notes** to hiring managers or engineers. Keep them to about 90 words, with one link and one ask. Plan on single-digit reply rates, treat that as an unmeasured proxy [S5][S6], and review at 60 sends. Change the targeting or the artefact before raising volume, and send one follow-up only.
   *Failure mode:* the reply rate is unknown and may be near zero; a sloppy note can harm your reputation.
5. **Do not do any of these.**
   - Ask strangers or pay anyone for referrals.
   - Run LinkedIn bots or scraping extensions.
   - Buy HR contact lists.
   - Pay any recruiter or "placement" fee.

   *Failure mode of avoiding them:* you give up cheap-looking reach, which the evidence says is low-value at best [S9][S24][S49][S55].
6. **Find work emails by pattern guessing plus verification on a free tier.** Log every send, source and consent signal [S51].
   *Failure mode:* hit rate is below vendor claims; the address may be personal data held without a notice.
7. **Law pointer.** Keep messages individual, role-relevant and one-to-one. Honour any opt-out. In Canada, name the referrer in a first message. Treat sole-trader recipients in the UK and EU, and any bulk or automated sending, as higher risk. If you sell services, the commercial-message rules apply [S36]–[S47].
   *Failure mode:* the definitional reading is untested by any regulator.
8. **Recruiters.** Use employer-paid agency recruiters as a secondary channel and never pay. India: avoid paid referral groups, Telegram HR sheets and any fee demand; report fraud to 1930 [S55].
   *Failure mode:* the evidence on agency conversion is thin.

**What would change this.**
- A measured candidate-initiated reply or interview rate by channel.
- ATS data that separates vouched from submit-only referrals.
- Regulator statements on job-seeker outreach.
- Employer policy pages from frontier labs.
- DPDP Rules in force on 2027-05-13 or 14.

## Alternatives Considered

| Option | Verdict | Reason and failure mode |
|---|---|---|
| Referral-first from every tie | Preferred for vouchable ties only | Information effect is real [S12]; fails for weak or no ties and burns referrer credit. |
| Ask strangers for referrals | Rejected | Policies decline and a survey rates it net negative [S9][S24]; low information value. |
| Pay for referrals | Rejected | Underground market with employer warnings and no outcome data [S30][S31]. |
| Portal applications only | Baseline | About 0.18 offers per 100 applications [S1][M]; large time cost. |
| Artefact-led cold outreach | Preferred when no tie | Cheap to test; reply rate unmeasured and the artefact takes time. |
| Double opt-in introductions | Preferred for moderate ties | Weak-tie evidence [S16]; no yield data. |
| Alumni or former-employer groups | Acceptable | Only bibliographic evidence [S19]; homophily limits reach. |
| Agency recruiters | Conditional | Employer-paid and non-exclusive; a survey rates agency contacts net negative [S9][S59]. |
| Bots, scrapers, bought lists | Rejected | Account restriction, enforcement and legal exposure [S48]–[S50]. |

## Detailed Findings

### 1. Economics of referrals

| Study | Sample | Setting | Finding | Grade |
|---|---|---|---|---|
| Burks, Cowgill, Hoffman, Housman, QJE 2015 [S10] | Nine large firms | Call centres, trucking, high-tech | Referred applicants are more likely to be hired and to accept; productivity is similar on most measures, with lower accident rates in trucking and more patents in high-tech. Referred workers quit less and earn slightly more. Profit gains come mostly from lower turnover and recruiting costs. | B |
| Brown, Setren, Topa, JOLE 2016 [S11] | One large US corporation | Employee referral system | Referred candidates are more likely to be hired. They start with a wage advantage that dissipates and stay longer. | B |
| Pallais and Sands, JPE 2016 [S12] | Three field experiments | Online labour market | Referrals carry performance and persistence information absent from observable characteristics. They do especially well when working with their referrer. No evidence that effort rises from worry about the referrer relationship. | A |
| Dustmann et al., REStud 2016 [S13] | German matched employer–employee data (as summarised in the abstract extract) | Referral networks | Referral hires show a wage premium and lower exit that fade with tenure, read as an information mechanism. | B |
| Friebel, Heinz, Hoffman, Zubanov, JPE 2023 [S14] | RCT, retail chain | Referral bonus | Larger bonuses raise referral volume but lower quality. The programme cut attrition by 15%. | B |
| Beaman and Magruder, AER 2012 [S15] | 562 original participants, 407 referrals | Kolkata lab-in-field | Performance-paid referrers recommend higher-ability people; flat pay shifts to closer ties. | B |
| Mouw, ASR 2003 [S17] | US survey data (NLSY) | Contacts and wages | Standard caution that observed contact premia may reflect who has contacts. I read only the abstract extract. | B |
| CEMFI working paper 0406 [S18] | US and EU household panels | Occupational choice | Jobs found through family and friends carry a 5–7% wage discount. | B |
| Rajkumar et al., Science 2022 [S16] | About 20M LinkedIn users, 2015–2019 | Randomised network suggestions | Moderately weak ties (about 10 mutual connections) drive most job mobility, with larger effects in digital industries. LinkedIn-affiliated authors. | B |

**How much is selection?** No source I found quantifies the selection share for vouched referrals in tech hiring. What the literature supports is:
- *Selection:* referrers choose whom to refer, and incentives change that choice [S15].
- *Information:* referrals add information beyond the CV [S12].
- *Gating:* referrals reach reviewers quickly. GitLab reviews them within five business days and says it interviews referred and other candidates identically [S24].

Ashby's per-application ratios blend all three. They are also computed on about 1% of applications [S1].

### 2. Referral mechanics by employer type

| Employer type | What is documented | Source | Grade |
|---|---|---|---|
| ATS: Lever | A "Referral" source tag attaches a referral form and a referred-by field. The first-ranked source tag drives reporting. Duplicate referrals to one posting can be blocked, and internal-only postings cannot be referred to. | [S26][S27] | B |
| ATS: Greenhouse | A "Who gets credit" field names the referrer, and recruiters can edit the source. Referrals can be added in the system or tracked through a unique link. | [S25] | B |
| ATS: Ashby, Workday | An Ashby secondary summary says admins can block referrals for existing candidates. Workday documentation was not accessible. | [S28] | C |
| Public-handbook software employer (GitLab) | Referral means someone you have worked with or know closely. An endorsement is a recommendation after the candidate applied, with no bonus. Referral status lasts six months within a job family. | [S24] | A |
| Frontier labs and Big Tech | No official referral-policy page found. Practitioner pages claim separate queues (unverified). | Absence | E |
| IT services (India) | TCS Bring Your Buddy bonus ₹40,000 for mid-level hires. Infosys ₹10,000–50,000 by job level (aggregator quoting ET). | [S32][S33] | C |
| GCCs | Hiring volume data only; no referral policies found. | [S34] | B |

Larger bonuses lowered referral quality in an RCT [S14]. The ATS data does not show vouched against submit-only referrals; I found no vendor split.

### 3. Asking for a referral

- **Strong ties** (worked together, saw your work): ask for a named requisition with a forwardable paragraph. Offer an easy decline. Ask how their process treats existing applicants [S24].
- **Weak or moderate ties:** ask for an introduction, not a referral, and give the contact a reason to look at an artefact [S16].
- **No tie:** do not ask for a referral. GitLab instructs its employees to decline and redirect to the jobs page [S24].
- **Success rates:** I found no data on how often referral requests succeed.
- **Paid referral services:**
  - Bloomberg, via LinkedIn News, describes an "underground market" in which workers charge strangers. App operators say it is legal and employers warn it could end referral programmes [S30].
  - A Topmate seller page lists a paid "referral jobs" group at ₹299 for three months [S31].
  - I found no statute or employer code of conduct on selling referrals, and no outcome evidence.

### 4. Warm introductions and alumni networks

- Double opt-in means the mutual contact asks the target first, then connects you.
- No yield data exists for double opt-in introductions or for alumni networks in GenAI hiring (Absences).
- A study of Dartmouth seniors' use of peer and alumni networks exists [S19], but I saw only its bibliographic record.
- In Canada, the first message after a referral can be sent without prior consent if it names the referrer and says it is sent because of the referral [S41].

### 5. Cold outreach

- **Structure:** the only measured guidance is proxy data. Instantly (vendor) reports the best email length under 80 words, 4–7 sequence steps as optimal, and 58% of replies from the first email [S5].
- **Recipient:** in a self-selected survey (n≈500, mean 8 years' experience), cold outreach to hiring managers was net positive at FAANG-type firms and neutral elsewhere. Cold outreach to recruiters was net negative at FAANG-type firms and small startups [S9]. This is a ranking, not a reply rate.
- **Channel:** Pin's LinkedIn rate (17.08%) is recruiter-to-candidate and does not transfer to candidate-initiated messages [S6]. I found no X direct-message data and no LinkedIn InMail data for candidates.
- **Timing:** no measured evidence for the 24–48 hour rule or for the day 5–7 follow-up (K4, K6).

### 6. Routes

| Route | Measured yield | Source | Grade |
|---|---|---|---|
| Inbound application | 3% reach interview; 6% of interviews reach offer (about 0.18 offers per 100 applications, M). Huntr trackers: 1.95% of 1.24M applications reached interview. | [S1][S8] | B/C |
| Vouched referral | 40% reach interview; 16% of interviews reach offer. Referred candidates pass initial screens at 52% vs 35%. | [S1][S3] | B |
| Sourced (recruiter-initiated) | 25% reach interview; 6% of interviews reach offer. Not a candidate action. | [S1] | B |
| Stranger or paid referral | No measured yield; employer policy declines; survey net negative. | [S9][S24] | C/A |
| Double opt-in introduction | Unmeasured | Absence | E |
| Alumni networks | Unmeasured | Absence | E |
| Cold outreach to manager, founder or engineer | No measured candidate rate. Proxies: sales email 3.43% average, 5.5% top quartile; recruiter email 4.96–6.31%. | [S5][S6] | B/C |
| Artefact-led outreach | Unmeasured | Absence | E |
| Agency recruiters | Agency interview-to-offer 8% (Ashby); survey net negative. | [S1][S9] | B/C |

### 7. Contact details

- Pattern guessing (first name, initial plus surname, and so on) is the common free method [S62]. I found no accuracy data for it.
- Pin's vendor-run audit (1.3M+ lookups, March–May 2026) found hit rates of Wiza 55.2%, ContactOut 48.2%, Forager 45.9% and RocketReach 29.8%, against claims of 92–99% [S7]. A hit means an address was returned, not that it works. Pin sells a competing product, and the population was recruiter candidate lists, not hiring managers.
- LinkedIn's help page bars crawlers, bots, plug-ins and extensions that scrape or automate, and says accounts may be restricted or shut down [S49]. LinkedIn v. ProAPIs (N.D. Cal. 3:25-cv-8393) was filed in October 2025; a Bloomberg Law report cites a 2025-12-08 filing saying the parties were exploring early resolution. LinkedIn's suit against Proxycurl (filed January 2025) was reported resolved in July 2025 [S50].
- CNIL decision SAN-2024-020 of 2024-12-05 fined Kaspr €240,000 for collecting LinkedIn contact details from users who had restricted visibility, and for retention, transparency and access failures [S48].
- "HR contact" spreadsheets sold to Indian job seekers: I found no verifiable listing and no regulator statement. India's DPDP Act excludes personal data made public by the data principal herself, so a sheet compiled from other sources is not obviously excluded. The Act's core duties do not apply until 2027-05-13 or 14 [S42][S43]. This is my reading, not advice (D).

### 8. The law

| Jurisdiction | Rule | Applies to job-seeker outreach? | Official source | Date | Grade |
|---|---|---|---|---|---|
| EU | ePrivacy Directive art 13: prior consent for e-mail "direct marketing" to natural-person subscribers; soft opt-in for a seller's own similar products; Member States protect legal-person subscribers (art 13(5)). GDPR art 2(2)(c): household exemption, read narrowly by the CJEU (C-25/17). | Probably not "direct marketing"; no regulator statement. Systematic collection may leave the household exemption. Member State rules not researched. | legislation.gov.uk copy of the Directive; CJEU judgment | 2002-07-12 (revised 2009-12-19); 2018-07-10 | A (art 13); B (GDPR) |
| UK | PECR reg 22 and ICO guide: consent or soft opt-in for direct marketing e-mail to individual subscribers (sole traders, some partnerships); no consent rule for corporate subscribers. DUAA 2025: maximum PECR fine aligned to GBP 17.5m or 4% from 2026-02-05. | Unclear, probably not marketing; no ICO statement found. | ICO PECR guidance; ICO DUAA blog | n/d; 2026-06-23 | B |
| US | CAN-SPAM covers e-mail whose primary purpose is commercial advertisement or promotion of a commercial product or service; no B2B exemption; opt-out model. | A request for employment is not obviously within it; no FTC statement. Freelance service pitches are. | FTC compliance guide | n/d | B |
| Canada | CASL: consent for commercial electronic messages (those encouraging commercial activity); implied consent from a conspicuously published address if the message is relevant to the role. SOR/2013-221 s 4: first message after a referral exempt if the referrer is named. | Unclear; no CRTC statement on job seekers found. | ISED consent page; Justice Laws | 2019-04-01; regulations consolidated to 2026-05-26 | A/B |
| India | DPDP Act 2023 s 3(c): excludes personal or domestic processing and data made public by the data principal. Rules notified 2025-11-13 (some sources say 14 November); Rule 4 from 2026-11-13/14; core duties from 2027-05-13/14. No email anti-spam statute found. TCCCPR 2018 covers commercial voice and SMS. | Core duties not in force as of 2026-11-11; a personal message is probably not commercial communication. | DPDP Act text (TRAI-hosted); TRAI paper | 2023-08-11; 2024-08-28 | B |
| Singapore | Spam Control Act 2007: unsolicited commercial messages sent in bulk (more than 100 similar messages in the s 6(1)(a) period; further thresholds in s 6(1)(b)–(c), not read). PDPA Do Not Call provisions cover marketing messages to Singapore phone numbers; messages outside s 37(1) are not specified messages. | One-to-one personal messages are not bulk commercial messages. | SSO; PDPC guidelines | 2007; 2017-07-27 | B |
| Australia | Spam Act 2003: commercial electronic messages need consent (express or inferred), sender identification and unsubscribe. Consent can be inferred from a conspicuously published work address if the message is relevant to the role. | A job application is not clearly a commercial message; no ACMA statement found. | legislation.gov.au | 2003-12-12 | B |

### 9. Recruiters and agencies

- Contingency fees run about 15–25% of first-year base and are paid only on placement; retained search runs about 25–35% of first-year total compensation in instalments. Both are employer-paid [S59].
- For leadership roles, retained search firms work by invitation. I found no conversion data for GenAI or leadership roles.
- Red flags: any registration, training, equipment, "biometric verification" or placement fee, and recruiters who contact you only on WhatsApp or Telegram [S55][S57][S58].
- FTC-reported job-scam losses rose from $90M (2020) to $501M (2024) [S58].

### 10. India

- Bonuses and hiring growth (KF13) mean employee referrals matter at services firms and GCCs. I found no measured referral share of hires for India.
- Official advisories:
  - The Ministry of Labour and Employment said on 2026-11-09 that all NCS services are free and that nobody should pay for registration, applications or interviews. Helplines: NCS 1514, cybercrime 1930 [S55].
  - The MEA's December 2023 advisory cites overcharging of ₹2–5 lakh by unregistered overseas recruitment agents and a service-charge ceiling of ₹30,000 plus 18% GST for registered agents [S56].
  - I4C's alert of 2026-05-29 covers fake online interviews and biometric-data scams [S57].
- Referral requests in WhatsApp or Telegram groups follow the same cold-referral logic as KF7. Payment-first "referral" or "job" groups are a scam marker [S31][S55][S57].

### 11. Yield per hour

Inputs: Ashby per-application rates [S1]; an assumption (D) of 3 cold applications per hour; H = hours to secure one vouched referral for a named requisition (unknown).

| Route | Offers per hour (M) | Reading |
|---|---|---|
| Cold applying | 0.0018 × 3 = 0.0054 (about 1 offer per 185 hours) | Population average. |
| Vouched referral | 0.064 ÷ H | Beats cold applying when H is under about 11.9 hours. |
| Vouched referral, lift halved for selection | 0.032 ÷ H | Beats cold applying when H is under about 5.9 hours. |
| Artefact outreach, community, public writing | Unmeasured | No data. |

Networking is the highest-yield activity per application for a vouched referral. It is not shown per hour, and not for stranger referrals. Measuring it would take ATS source tags on candidate-initiated referrals plus time logs, or randomised hours across channels.

### 12. Templates

These are formats with evidence tags, not ghost-written messages. Replace every bracket yourself.

**A. Referral request (to someone who has seen your work)** [S12][S24]
```
Subject: [Role], [Req ID] at [Company]: would you be willing to refer me?   [P]
Hi [Name], I'm applying for [role, req link] on [team].                      [S24: named requisition]
You've seen my work on [project], so I'm asking if you'd be comfortable      [S12: referrer's information; P: easy decline]
referring me; no problem if not.
Two lines you can reuse: [one-sentence fit]; [artefact: what it shows,       [P]
one command to reproduce].
How does [Company] treat someone who has already applied? I'll hold off      [S24][S25]-[S27]
applying until you say so.
Thanks, [Name] [CV link]
```

**B. Warm-introduction request (double opt-in)** [P][S16][S41]
```
Subject: Could you ask [Target] if they'd be open to hearing from me?
Hi [Mutual], I'd value a short introduction to [Target], [role] at [Company], because [specific reason].
Please ask them first; I'll write only if they say yes.                       [P: double opt-in]
Forwardable blurb: "[Name] is a [role] who [one-line evidence]. Their [artefact link] shows [what].
They'd like 15 minutes to ask about [topic]; no referral is requested."       [P; S41: name the referrer]
Thanks either way.
```

**C. Cold note to a hiring manager, engineer or founder, with an artefact (about 90 words)**
```
Subject: [Specific thing about their work]: [my artefact in five words]
Hi [Name], I read [post, PR or paper] and tried [what you did]. Result: [one sentence]; [link; reproduce with one command].   [P: verifiable artefact; S9]
I've applied for [role, req ID] through the careers page.                      [D: apply first, unmeasured]
Are you the right person to ask [one specific question], or can you point me to who is?   [P: one ask]
If it's not relevant, ignore this; I won't follow up more than once.            [P]
[Name] | [link]
```
Length guide: under 90 words (proxy: Instantly's under-80-word finding [S5]).

**D. Follow-up (day 5–7, about 40 words)** [P][S5]
```
Hi [Name], one addition since my note: [new evidence, such as a result or merged PR, with link].
No reply needed if the timing is wrong. [Name]
```
One follow-up, then stop [D]. In Instantly's vendor sequences 58% of replies came from the first email [S5].

### 13. Tools

| Tool | Stage | Verdict | Why |
|---|---|---|---|
| Hunter.io | 7 | use-with-care | Free plan 50 credits per month; Starter $49 monthly or $34 per month billed yearly. At up to about 130 new contacts per month at 30 sends a week, 50 credits cover roughly a third unless you find many addresses manually. [S51] |
| Apollo.io | 7 | use-with-care | Free plan 900 credits per year (75 per month) as captured 2026-09-28 and November 2026, down from 100 per month in an August 2026 capture; some pages still report unlimited email credits. [S52] |
| RocketReach | 7 | avoid | Lowest hit rate (29.8%); annual-only billing at about $396–399 a year. [S7][S54] |
| Clay | 7 | avoid | Built for go-to-market teams; Launch $185 per month on monthly billing, $167 on annual. [S53] |
| Wiza, ContactOut, Forager | 7 | avoid | Hit rates 45.9–55.2% (vendor-run audit); terms not reviewed this session. [S7] |
| LinkedIn automation bots | 7 | avoid | Barred by LinkedIn's rules; restriction named as the consequence. [S49][S50] |
| Huntr (tracker) | 7 | watch | Published aggregate data only; a spreadsheet does the same job. [S8] |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Ashby 3%/25%/40%; Gem about 11× and 8× | confirmed | [S1][S4]; Gem's sourced multiple is 4–8× inside its own article | B |
| K2 | Referrals 15–18% of hires, inbound about half; 70–85% unsupported | confirmed | [S2][S21][S22]; Ashby: referral 18%, inbound 43–52% | B/E |
| K3 | Ask before applying; a cold application may block the referral | updated | [S24]–[S28]; employer and ATS dependent, so "block" is too strong | B |
| K4 | Apply, then note within 24–48 hours; unmeasured | unverifiable | No data found | E |
| K5 | One verifiable artefact per message | unverifiable | Practitioner advice only [S62]; no measured effect | E |
| K6 | 30 per week; 80–90 words; one follow-up day 5–7 | unverifiable | Proxy: Instantly under 80 words; 58% of replies from first email [S5]; no candidate data | B (proxy) |
| K7 | Plan 3–8%; decide at 60; 4.9% bound | confirmed | M: 4.87% bound; no candidate rate found | M/E |
| K8 | Instantly 3.43%/5.5%; Pin 17.08% recruiter-to-candidate | confirmed | [S5][S6]; Instantly top decile 10.7% | B/C |
| K9 | Referred pass screens 52% vs 35% | confirmed | [S3] is the primary vendor source, not a secondary summary | B |
| K10 | LinkedIn automation: avoid | confirmed | [S49][S50] | B |
| K11 | Apollo free tier 1,200 credits a year | updated | [S52]: 900 per year as captured 2026-09-28; sources conflict | C |
| K12 | Hunter free 50 credits plus manual verification is enough | updated | [S51]: 50 credits stand; they cover about a third of a 30-sends-a-week cadence | B/M |
| K13 | RocketReach 29.8% find rate; $329 a year | updated | [S7] confirms 29.8%; [S54]: $396–399 annual-only | C |
| K14 | Clay Launch $185 a month on annual billing | updated | [S53]: $185 is monthly billing, $167 annual | C |
| K15 | Wiza 55.2%, ContactOut 48.2%, Forager 45.9% | confirmed | [S7]; vendor-run audit, hit rate not deliverability | C |

## Absences

- **Candidate-initiated reply or interview rates, by channel and message type.** Searched Instantly, Pin, Huntr, interviewing.io and vendor and practitioner posts. Only vendor claims and a ranking survey exist.
- **Success rate of referral requests** (asks to referrals). Not found.
- **Yield of warm introductions and alumni networks in GenAI hiring.** Not found.
- **Vouched vs submit-only referral split in ATS vendor data.** Not found.
- **Official referral-policy pages at frontier labs and Big Tech.** Not found; GitLab is the only public handbook found.
- **Workday referral mechanics.** Documentation is behind login.
- **Topmate policy on selling referrals; law or employer codes on selling referrals.** Not found.
- **Regulator statements on job-seeker outreach** under CAN-SPAM, PECR, CASL, the Spam Act or the PDPA. Not found.
- **EU Member State rules on B2B and individual e-mail.** Not researched.
- **Indian regulator statement on HR contact spreadsheets; Indian measured referral share.** Not found.
- **Accuracy data for email pattern guessing; standalone verifiers (NeverBounce, ZeroBounce).** Not researched.
- **Terms of service for Wiza, ContactOut, Forager, Apollo, Hunter.** Not opened.
- **X direct-message and LinkedIn InMail data for candidates.** Not found.
- **Literature not retrieved:** Facebook strong-tie study (Gee et al.), Fernandez–Weinberg, Hensvik–Skans, Kramarz–Skans, Zottoli–Wanous.

## Open Questions & Risks

**Open questions.** Does a candidate's artefact lift reply rates? Do ATS vendors treat vouched referrals differently from submit-only ones? Will DPDP Rules change how contact lists are treated after 2027-05-13 or 14?

**Strongest objections an expert would raise.**

1. *"Referral advantage is selection, so asking cannot change your odds."* For: Ashby cannot separate selection; Mouw warns of selection; incentives change who is referred [S15][S17]. Against: Pallais and Sands show a real information effect [S12]. Net: a vouched referral carries information; a stranger's does not [S24].
2. *"Vendor data is biased by ATS adoption and self-reported source labels."* For: all four datasets are vendor-owned, and Ashby's referral figure rests on about 1% of applications [S1]. Against: the direction agrees across Ashby and Gem. Net: use ratios as direction, not size.
3. *"Job-seeker outreach is clearly lawful (or clearly unlawful)."* For lawful: definitions target commerce [S39][S36]. Against: no regulator has said so, and the GDPR household exemption is narrow [S35]. Net: moderate-low confidence that personal one-to-one notes are outside scope; scraping and bulk send raise risk.
4. *"Candidate cold email gets 5–15% or more."* For: vendor posts. Against: none traceable; survey shows cold outreach net positive only at FAANG-type firms [S9]. Net: unknown in both directions.
5. *"The weak-ties result is LinkedIn's own and measures LinkedIn-mediated hiring."* True [S16]; applies most to LinkedIn-mediated routes, with the larger effect in digital industries.
6. *"The contact-finder audit is vendor-run and measures hit rate."* True [S7]; verdicts on RocketReach also rest on price and annual-only billing [S54].
7. *"GitLab is not representative."* True; it is the only public employer policy I found.

**Risks.**
- Retrieval dates follow the session anchor.
- URLs for S10, S11, S14, S21, S30 and S31 were not retained, and the DOI for S16 is recalled; maintainers should verify these.
- Source dates differ by one day for the DPDP Rules (13 vs 14 November 2025).
- Apollo credits conflict across sources.
- The EDPB summary page headline says €200,000 while its body and CNIL say €240,000.

## Discovered Concerns

- DPDP Rule 4 (consent managers) takes effect on 2026-11-13 or 14, two days after the anchor date [S43].
- UK PECR maximum fines rose to GBP 17.5m or 4% of turnover from 2026-02-05 [S38], which raises the stakes for any bulk send.
- AI-assisted recruiter impersonation and fake online interviews are rising in the FTC and I4C material [S57][S58].
- Many "data-backed" blog posts repeat 40% vs 3% without noting that it is per application and from about 1% of applications [S1].
- The employee side was not researched: whether employers restrict staff from accepting payment for referrals.

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | About 10× interview rate, mostly selection | Updated | 13× to interview and about 36× offers per application [S1][M]; part is information and gating, not only selection [S12] | Keeps the per-application caution; adds the information effect. |
| P2 | No traceable source for 70–85% | Confirmed | Trail ends at a 1966 claim and a 2016 poll [S21][S22] | Keeps the E grade. |
| P3 | No public candidate reply dataset | Confirmed | Only proxies and surveys [S5][S6][S9] | Keeps K7's "unverified" framing. |
| P4 | Personal messages mostly outside anti-spam law | Updated | Definitional reading supports it, but no regulator statement [S36]–[S47] | Moderate-low confidence; scraping and bulk are riskier. |
| P5 | Finder rates well below vendor claims | Confirmed | 29.8–55.2% vs 92–99% [S7] | Vendor-run, so cap at C. |
| P6 | Lower quits and slightly higher wages | Updated | Lower quits recur [S10][S14]; wage premium fades [S11][S13]; 5–7% discount for family and friends [S18] | Wage evidence is mixed. |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Ashby, Talent Trends: referrals report, https://www.ashbyhq.com/talent-trends-report/reports/referrals | 2025-05-16 | 2026-11-11 | B | Read | single-source | Funnel rates, referral share of applications |
| S2 | Ashby, Talent Trends: inbound and hire sources, https://www.ashbyhq.com/talent-trends-report/reports/inbound | 2025 (Q2 data) | 2026-11-11 | B | Read | single-source | Hire shares by source |
| S3 | Ashby, Recruiting Operations Benchmarks, https://www.ashbyhq.com/talent-trends-report/reports/recruiting-operations-benchmarks-talent-trends | 2026-05-07 | 2026-11-11 | B | Read | single-source | 52% vs 35%; same-function referrals |
| S4 | Gem, 2026 Recruiting Benchmarks key takeaways, https://vercel.gem.com/blog/key-takeaways-from-the-2026-recruiting-benchmarks-report | 2026 (n/d) | 2026-11-11 | B | Read | COI | 11× referrals; sourced 4–8× |
| S5 | Instantly, Cold Email Benchmark Report 2026, https://instantly.ai/cold-email-benchmark-report-2026 and https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/ | 2026-01-12 | 2026-11-11 | B | Extract | COI | Sales-email proxy rates, length, follow-up share |
| S6 | Pin, Recruiting Outreach Benchmarks 2026, https://www.pin.com/blog/recruiting-outreach-benchmark-report/ | 2026 (n/d) | 2026-11-11 | C | Extract | COI | Recruiter-to-candidate proxy rates |
| S7 | Pin, email finder vendor audit, https://www.pin.com/blog/email-finder-vendor-audit/ | 2026 (n/d; data window 2026-03 to 2026-05) | 2026-11-11 | C | Extract | COI | Hit rates by finder |
| S8 | Lumyhired summary of Huntr data, https://www.lumyhired.com/blog/job-search-strategies-2026 | 2026 (n/d) | 2026-11-11 | C | Extract | secondary | Tracker interview rate |
| S9 | interviewing.io, How to get in the door at top companies, part 1, https://interviewing.io/blog/how-to-get-in-the-door-at-top-companies-part-1 | n/d | 2026-11-11 | C | Read | self-selected survey | Channel ranking; cold referrals |
| S10 | Burks, Cowgill, Hoffman, Housman, "The Value of Hiring through Employee Referrals", QJE 2015 (URL not retained) | 2015 | 2026-11-11 | B | Extract | single-source | Referral literature |
| S11 | Brown, Setren, Topa, "Do Informal Referrals Lead to Better Matches?", JOLE 2016 (URL not retained) | 2016 | 2026-11-11 | B | Extract | | Referral literature |
| S12 | Pallais and Sands, "Why the Referential Treatment?", JPE 2016, https://econpapers.repec.org/RePEc:ucp:jpolec:doi:10.1086/688850 | 2016 | 2026-11-11 | A | Read | | Information effect |
| S13 | Dustmann et al., "Referral-based job search networks", REStud 2016, https://econpapers.repec.org/RePEc:oup:restud:v:83:y:2016:i:2:p:514-546 and https://iab.de/en/publications/publication/?id=5456851 | 2016 | 2026-11-11 | B | Extract | | Wage and exit effects |
| S14 | Friebel, Heinz, Hoffman, Zubanov, "What Do Employee Referral Programs Do?", JPE 2023 (URL not retained) | 2023 | 2026-11-11 | B | Extract | | Bonus quantity and quality |
| S15 | Beaman and Magruder, "Who Gets the Job Referral?", AER 2012, https://econpapers.repec.org/RePEc:aea:aecrev:v:102:y:2012:i:7:p:3574-93 | 2012 | 2026-11-11 | B | Extract | | Incentives and who is referred |
| S16 | Rajkumar et al., "A causal test of the strength of weak ties", Science 2022, https://www.science.org/doi/10.1126/science.abl4476 | 2022 | 2026-11-11 | B | Extract | URL from memory, verify; LinkedIn-affiliated authors | Weak ties |
| S17 | Mouw, "Social Capital and Finding a Job: Do Contacts Matter?", ASR 2003, https://www.citedrive.com/en/discovery/social-capital-and-finding-a-job-do-contacts-matter | 2003 | 2026-11-11 | B | Extract | | Selection caution |
| S18 | CEMFI working paper 0406, "Social Contacts and Occupational Choice", https://www.cemfi.es/ftp/wp/0406.pdf | 2004 | 2026-11-11 | B | Extract | | Wage discount via family and friends |
| S19 | Marmaros and Sacerdote, "Peer and social networks in job search", EER 2002, https://econbiz.de/Record/peer-and-social-networks-in-job-search-marmaros-david/10001668898 | 2002 | 2026-11-11 | C | Extract | bibliographic only | Alumni and peer networks |
| S20 | NY Fed (Topa), How do people find jobs, https://www.newyorkfed.org/medialibrary/media/aboutthefed/pdf/HowDoPeopleFindJobs_Topa_June2017.pdf | 2017-06 | 2026-11-11 | C | Extract | | Contact use in job finding |
| S21 | Learning Curves, "Hidden Origins of the Hidden Job Market Pt. 2", https://learningcurves.org/ (full post URL not retained) | c. 2023 | 2026-11-11 | C | Extract | | 1966 origin trail |
| S22 | On The Move Canada, https://onthemovecanada.com/work/find-job/job-networking-statistics/ ; Brock University, https://brocku.ca/chyds/2023/03/06/communicating-the-importance-of-networking | 2023-03-06 | 2026-11-11 | C | Extract | | 2016 poll origin |
| S23 | College Recruiter, https://www.collegerecruiter.com/blog/2024/07/09/is-it-true-that-80-of-job-openings-are-not-advertised | 2024-07-09 | 2026-11-11 | C | Extract | | Untraceable origin |
| S24 | GitLab Handbook, Referral Program and Process, https://handbook.gitlab.com/handbook/hiring/referral-process | 2025-10-14 | 2026-11-11 | A | Read | single employer | Referral vs endorsement; strangers |
| S25 | Greenhouse support articles on referral credit, editing a referral and candidate source, https://support.greenhouse.io/hc/en-us/articles/20713686421147 ; https://support.greenhouse.io/hc/en-us/articles/10953909383707 ; https://support.greenhouse.io/hc/en-us/articles/115003931231 | n/d | 2026-11-11 | B | Extract | | ATS mechanics |
| S26 | Lever Help, Creating and using tags, https://help.lever.co/hc/en-us/articles/20087333719965 | n/d | 2026-11-11 | B | Extract | | Referral source tag |
| S27 | Lever Help, Setting up a referral form, https://help.lever.co/hc/en-us/articles/21450491074461 | n/d | 2026-11-11 | B | Extract | COI on speed claim | Direct referrals; duplicates |
| S28 | Work-club summary of Ashby referral docs, https://work-club.com/ats-referral-hiring-software-questions/amp/ ; Ashby, https://ashbyhq.notion.site/Referrals-and-Referral-Links-9418282762224481bd30861997baaf07 | n/d | 2026-11-11 | C | Extract | secondary | Ashby referral blocking |
| S29 | Refer.me blog, "Do job referrals actually work? Data behind response rates", https://refer.me/blog/do-job-referrals-actually-work-data-behind-response-rates | c. 2026-04 | 2026-11-11 | C | Extract | COI (sells referrals); not relied on | Surfaced in the reply-rate search; vendor claims left untraced |
| S30 | LinkedIn News summarising Bloomberg, "Refer a stranger, collect cash" (URL not retained; Bloomberg original not opened) | c. 2025-01 | 2026-11-11 | C | Extract | | Paid referral market |
| S31 | Topmate seller page "SDE Jobs and Internships" (URL not retained); Topmate, https://topmate.io/ | n/d | 2026-11-11 | B | Extract | | Paid referral groups |
| S32 | People Matters, TCS referral incentive, https://www.peoplematters.in/news/talent-management/tcs-increases-referral-incentives-to-indian-rupee40000-to-secure-mid-level-tech-experts-48616 | n/d | 2026-11-11 | C | Extract | | TCS bonus |
| S33 | Aggregator quoting ET on Infosys referral bonuses, https://news.visitinrajasthan.com/?p=31022 | n/d | 2026-11-11 | C | Extract | secondary aggregator | Infosys bonus ranges |
| S34 | Business Today on foundit Insights Tracker, https://www.businesstoday.in/amp/jobs/story/at-5-1-lakh-jobs-indias-global-capability-centre-hiring-boom-scales-new-peak-540328-2026-07-01 | 2026-07-01 | 2026-11-11 | B | Extract | | GCC hiring |
| S35 | CJEU C-25/17 Jehovan todistajat (mirror of CELEX 62017CJ0025), https://pub-a0410b6281c64831b9c9612cf6920e67.r2.dev/celex-62017CJ0025.pdf | 2018-07-10 | 2026-11-11 | B | Extract | mirror | Household exemption |
| S36 | Directive 2002/58/EC art 13, legislation.gov.uk, https://www.legislation.gov.uk/eudr/2002/58/article/13/data.htm | 2002-07-12 (rev. 2009-12-19) | 2026-11-11 | A | Read | | ePrivacy rule |
| S37 | ICO, Electronic mail marketing; Choosing your lawful basis, https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/ ; https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/sending-direct-marketing-choosing-your-lawful-basis/ | n/d | 2026-11-11 | B | Extract | | PECR |
| S38 | ICO, One year on (DUAA), https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/one-year-on-marking-the-12-month-commencement-of-the-data-use-and-access-act/ ; DLA Piper, https://privacymatters.dlapiper.com/2026/02/uk-commencement-of-the-data-protection-provisions-in-the-data-use-and-access-act/ | 2026-06-23; 2026-02 | 2026-11-11 | B | Extract | | PECR fines; commencement |
| S39 | FTC, CAN-SPAM Act compliance guide, https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business | n/d | 2026-11-11 | B | Extract | | CAN-SPAM scope |
| S40 | ISED Canada, Getting consent to send email, https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/node/7 (also listed as .../en/getting-consent-send-email) | 2019-04-01 | 2026-11-11 | A | Read | possibly unchanged | CASL |
| S41 | Electronic Commerce Protection Regulations SOR/2013-221, https://laws-lois.justice.gc.ca/eng/regulations/SOR-2013-221/FullText.html | 2013-12-04 | 2026-11-11 | B | Extract | | Referral exemption |
| S42 | Digital Personal Data Protection Act 2023 (TRAI-hosted gazette text), https://www.trai.gov.in/sites/default/files/2024-09/DPDT_11082024.pdf | 2023-08-11 | 2026-11-11 | B | Extract | | s 3(c) exclusions |
| S43 | Mondaq (MeitY notifies DPDP Rules), https://www.mondaq.com/india/privacy-protection/1728232/update-meity-notifies-rules-operationalising-the-dpdp-framework-in-india ; SCC Online, https://www.scconline.com/blog/?p=371058 | 2025-11/12 | 2026-11-11 | B | Extract | secondary; dates differ by a day | DPDP commencement |
| S44 | TRAI consultation paper on TCCCPR review, https://trai.gov.in/sites/default/files/CP_28082024.pdf | 2024-08-28 | 2026-11-11 | B | Extract | | Telecom spam rules |
| S45 | Spam Control Act 2007, Singapore Statutes Online, https://sso.agc.gov.sg/Act/SCA2007 | 2007 | 2026-11-11 | B | Extract | | SCA bulk rule |
| S46 | PDPC, Advisory Guidelines on the DNC Provisions, https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/advisory-guidelines-on-the-dnc-provisions-(270717).pdf | 2017-07-27 | 2026-11-11 | B | Extract | | DNC scope |
| S47 | Spam Act 2003, legislation.gov.au, https://www.legislation.gov.au/C2004A01214/latest/text ; Mondaq summary, https://www.mondaq.com/australia/consumer-law/996226/spamming-and-the-spam-act | 2003-12-12 | 2026-11-11 | B | Extract | | Spam Act scope |
| S48 | CNIL, KASPR sanction, https://www.cnil.fr/fr/aspiration-de-donnees-sanction-de-240-000-euros-lencontre-de-la-societe-kaspr ; EDPB, https://www.edpb.europa.eu/news/data-scraping-french-supervisory-authority-fined-kaspr-eu240-000_en | 2024-12-19 | 2026-11-11 | B | Extract | EDPB title shows €200,000 | Enforcement vs contact-data vendor |
| S49 | LinkedIn Help, Prohibited software and extensions, https://www.linkedin.com/help/linkedin/answer/a1341387 | n/d (updated about 2 years before retrieval) | 2026-11-11 | B | Extract | | Platform rule |
| S50 | Bloomberg Law, LinkedIn v. ProAPIs, https://news.bloomberglaw.com/artificial-intelligence/linkedins-war-against-bot-scrapers-ramps-up-as-ai-gets-smarter ; Unipile timeline, https://www.unipile.com/br/?p=279858 | 2025-12 | 2026-11-11 | B | Extract | litigation may have moved | Scraper suits |
| S51 | Hunter.io pricing, https://hunter.io/pricing | n/d | 2026-11-11 | B | Extract | monthly prices from secondary snapshots | Free tier |
| S52 | FullEnrich Apollo pricing, https://fullenrich.com/content/apollo-pricing ; Snov.io, https://snov.io/blog/?p=62273 | 2026-09-28; 2026-11 | 2026-11-11 | C | Extract | official page not opened | Apollo credits |
| S53 | Crustdata Clay review, https://crustdata.com/reviews/clay | 2026-10-16 | 2026-11-11 | C | Extract | secondary | Clay prices |
| S54 | Hackceleration, https://hackceleration.com/labs/compare/rocketreach-vs-clay ; Noon, https://www.noon.ai/blog/articles/451-hunter-io-pricing-2026 | 2026-06; 2026-11-01 | 2026-11-11 | C | Extract | secondary | RocketReach prices |
| S55 | IANS, Labour Ministry warns on fake NCS offers, https://ianslive.in/labour-ministry-warns-jobseekers-against-fake-ncs-job-offers--20261109161546 | 2026-11-09 | 2026-11-11 | B | Extract | | NCS advisory |
| S56 | MEA advisory on overcharging by recruitment agents, https://www.eoivilnius.gov.in/pdf/Advisory%20circular-19-12-23.pdf | 2023-12-19 | 2026-11-11 | B | Extract | | Overseas recruitment fees |
| S57 | Asianet Newsable, MHA/I4C alert, https://newsable.asianetnews.com/amp/india/mha-warns-job-seekers-of-fake-online-interviews-ai-biometric-scams-articleshow-gy3y9qr | 2026-05-29 | 2026-11-11 | C | Extract | | Fake interview scams |
| S58 | CPA Practice Advisor on FTC job-scam data, https://www.cpapracticeadvisor.com/2026/04/23/with-job-scams-on-the-rise-heres-how-to-identify-fake-posts/182123/ | 2026-04-23 | 2026-11-11 | B | Extract | secondary | FTC losses |
| S59 | RecruitBPM, https://recruitbpm.com/blog/retained-search-vs-contingency-recruitment ; ZRG, https://www.zrgpartners.com/insights/differences-between-search-firms-part-2-3 | n/d | 2026-11-11 | C | Extract | practitioner | Recruiter fee structures |
| S60 | Law & Religion UK on C-25/17, https://lawandreligionuk.com/2018/07/10/jehovahs-witnesses-and-data-collection-cjeu/ | 2018-07-10 | 2026-11-11 | B | Extract | | Holding summary |
| S61 | Mondaq, One-man controller, https://www.mondaq.com/data-protection/1773198/one-man-controller-the-responsibility-of-individuals-under-the-gdpr | n/d | 2026-11-11 | C | Extract | | Art 2(2)(c) wording |
| S62 | interviewing.io, Cold outreach to hiring managers, part 2, https://interviewing.io/blog/how-to-get-in-the-door-at-top-companies-cold-out-reach-to-hiring-managers-part-2 | n/d | 2026-11-11 | C | Extract | practitioner | Pattern guessing; outreach advice |

## Data Appendix

```jsonl
{"type":"practice","area":"referral","tactic":"Ask a person who has worked with you or seen your work to refer you to a named requisition, with a forwardable paragraph","claim":"A vouched referral carries information not on a CV and sits in a higher-converting funnel","evidence":"Ashby 38M applications: 40% referred vs 3% inbound reach interview (descriptive); Pallais and Sands: referrals carry performance and persistence information; GitLab requires a specific requisition and candidate approval","verdict":"use","risk":"Referrer credibility at stake; causal share of the funnel gap unknown","grade":"B","src":["S1","S12","S24"],"as_of":"2026-11-11","ttl":"V5"}
{"type":"practice","area":"referral","tactic":"Prefer a referrer in the same function as the target role","claim":"Same-function referrals interview and convert more often in business roles","evidence":"Ashby 2026: 37% vs 26% interviewed and 5.2% vs 3.1% hired","verdict":"use","risk":"Business-role split only; descriptive","grade":"B","src":["S3"],"as_of":"2026-05-07","ttl":"V3"}
{"type":"practice","area":"referral","tactic":"Ask the referrer how their ATS and policy treat someone who already applied; apply first only if told it is fine","claim":"Treatment of existing applicants is employer and ATS specific, so a prior application does not always block a referral","evidence":"GitLab converts a progressed application into an endorsement; Greenhouse and Lever allow source edits or duplicate rules","verdict":"use-with-care","risk":"Credit lost or source locked","grade":"B","src":["S24","S25","S26","S27","S28"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"practice","area":"referral","tactic":"Ask a stranger for a referral","claim":"Cold referral requests have low value","evidence":"GitLab tells employees to decline; survey (n about 500) net negative at FAANG-type firms and small startups","verdict":"avoid","risk":"Wasted effort; reputational cost","grade":"C","src":["S9","S24"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"referral","tactic":"Pay a person or marketplace for a referral","claim":"Paid referrals add no vouching information and breach some employers' norms","evidence":"Bloomberg via LinkedIn News describes an underground market; GitLab bonuses only for referrals the employee can vouch for; paid referral group listed on Topmate","verdict":"avoid","risk":"Money lost; policy breach; no outcome evidence","grade":"C","src":["S24","S30","S31"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"warm-intro","tactic":"Double opt-in introduction through a mutual contact","claim":"Moderately weak ties transmit jobs most often","evidence":"Randomised LinkedIn experiments; Canada exempts a first message after a named referral; no yield measured","verdict":"use","risk":"Burdens the mutual contact","grade":"P","src":["S16","S41"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"alumni","tactic":"Use alumni or former-employer groups for introductions","claim":"Alumni ties are a source of introductions","evidence":"No yield data; only a bibliographic record of a peer-network study","verdict":"use-with-care","risk":"Homophily limits reach","grade":"P","src":["S19"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"cold-outreach","tactic":"Artefact-led note to a hiring manager, engineer or founder: about 90 words, one link, one ask","claim":"A verifiable artefact substitutes for the information a referral carries","evidence":"No measured effect of artefacts; sales proxy says under 80 words; survey net positive for manager outreach at FAANG-type firms","verdict":"use-with-care","risk":"Reply rate unmeasured; time cost; reputational harm if sloppy","grade":"P","src":["S5","S9","S62"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"cold-outreach","tactic":"Apply through the normal channel, then send a note within 24-48 hours","claim":"Sequence improves response","evidence":"Nothing measured","verdict":"untested","risk":"Looks like bypassing the process","grade":"P","src":["S9"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"cold-outreach","tactic":"One follow-up on day 5-7, then stop","claim":"One follow-up balances reply gain and annoyance","evidence":"Vendor sequences: 58% of replies from first email; no candidate data","verdict":"untested","risk":"Lost replies from later steps; annoyance","grade":"P","src":["S5"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"cold-outreach","tactic":"Cap at 30 messages a week and review at 60 sends","claim":"Zero replies in 60 sends bounds the true rate below 4.9%","evidence":"Binomial calculation; at a true 3% zero in 60 has 16% probability","verdict":"use-with-care","risk":"Cannot separate 0-3%","grade":"M","src":["S5","S6"],"as_of":"2026-11-11","ttl":"V5","note":"Inputs: n=60, alpha=0.05; proxy rates from S5 and S6"}
{"type":"practice","area":"cold-outreach","tactic":"Automate LinkedIn outreach or scrape profiles with bots or extensions","claim":"Third-party automation is barred and can lead to account restriction","evidence":"LinkedIn help page; LinkedIn v. ProAPIs","verdict":"avoid","risk":"Account restriction; legal exposure","grade":"B","src":["S49","S50"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"practice","area":"contact-details","tactic":"Pattern-guess work emails and verify on a free tier","claim":"Free tiers cover part of job-seeker volume; finders return fewer addresses than claimed","evidence":"Hunter free 50 credits; Pin audit hit rates 29.8-55.2%; no pattern-guess accuracy data","verdict":"use-with-care","risk":"Wrong or personal addresses; hit rate below claims","grade":"C","src":["S7","S51","S62"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"practice","area":"contact-details","tactic":"Buy HR contact lists or spreadsheets","claim":"Sourcing of such lists is unverified","evidence":"No quality data; Kaspr enforcement precedent; DPDP duties from 2027","verdict":"avoid","risk":"Data-protection complaints; fraud","grade":"C","src":["S42","S48"],"as_of":"2026-11-11","ttl":"V4"}
{"type":"practice","area":"recruiters","tactic":"Pay a recruiter, registration or placement fee","claim":"Legitimate recruiters are employer-paid","evidence":"NCS advisory; MEA advisory; FTC loss data","verdict":"avoid","risk":"Fraud; money lost","grade":"B","src":["S55","S56","S58"],"as_of":"2026-11-09","ttl":"V3"}
{"type":"practice","area":"recruiters","tactic":"Use employer-paid agency recruiters as a secondary channel","claim":"Agencies are one source among several","evidence":"Ashby agency interview-to-offer 8%; survey net negative; fee structures","verdict":"use-with-care","risk":"Incentive mismatch; poor fit","grade":"C","src":["S1","S9","S59"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"practice","area":"india","tactic":"Join paid referral or job-lead groups on Telegram or WhatsApp","claim":"Payment-first groups are a fraud marker","evidence":"Paid referral group listed on Topmate; official fraud alerts","verdict":"avoid","risk":"Fraud; identity data loss","grade":"C","src":["S31","S55","S57"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"tool","id":"hunter-io","name":"Hunter.io","stage":7,"category":"Contact finder","what":"Email finder, verifier, domain search and outreach sequences","verdict":"use-with-care","why":"Free plan 50 credits a month covers about a third of a 30-sends-a-week cadence; verify every address","url":"https://hunter.io/pricing","status":"active","risk":"Contact-data provenance unaudited","price":{"free":"50 credits/month","starter_monthly_usd":49,"starter_annual_usd_per_month":34},"open_source":false,"grade":"B","src":["S51"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"tool","id":"apollo-io","name":"Apollo.io","stage":7,"category":"Contact finder","what":"B2B contact database and sequencing","verdict":"use-with-care","why":"Free credits 900 a year (75 a month) in September to November 2026 captures; earlier 100 a month; sources conflict","url":"https://www.apollo.io/pricing","status":"active","risk":"LinkedIn removed Apollo's company page in March 2025 (secondary)","price":{"free":"900 credits/year"},"open_source":false,"grade":"C","src":["S52","S50"],"as_of":"2026-11-11","ttl":"V2","note":"Official page not opened"}
{"type":"tool","id":"rocketreach","name":"RocketReach","stage":7,"category":"Contact finder","what":"Contact lookup database","verdict":"avoid","why":"Lowest hit rate (29.8%) in a vendor-run audit; annual-only paid plans","url":"https://rocketreach.co/pricing","status":"active","risk":"Annual lock-in","price":{"annual_usd":[396,399]},"open_source":false,"grade":"C","src":["S7","S54"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"tool","id":"clay","name":"Clay","stage":7,"category":"Contact finder","what":"Go-to-market data enrichment workflows","verdict":"avoid","why":"Built for sales teams; Launch is 185 USD a month on monthly billing, 167 on annual","url":"https://www.clay.com/pricing","status":"active","risk":"Credit metering","price":{"launch_monthly_usd":185,"launch_annual_usd_per_month":167},"open_source":false,"grade":"C","src":["S53"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"tool","id":"paid-email-finders","name":"Wiza, ContactOut, Forager","stage":7,"category":"Contact finder","what":"Paid email finders","verdict":"avoid","why":"Hit rates 45.9-55.2% in a vendor-run audit; terms not reviewed","url":"https://www.pin.com/blog/email-finder-vendor-audit/","status":"active","risk":"Hit is not deliverability","open_source":false,"grade":"C","src":["S7"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"tool","id":"linkedin-automation-bots","name":"PhantomBuster and similar LinkedIn bots and extensions","stage":7,"category":"Outreach automation","what":"Third-party automation and scraping of LinkedIn","verdict":"avoid","why":"LinkedIn bars such tools and names account restriction as the consequence","url":"https://www.linkedin.com/help/linkedin/answer/a1341387","status":"active","risk":"Account restriction; litigation against scrapers","open_source":false,"grade":"B","src":["S49","S50"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"tool","id":"huntr","name":"Huntr","stage":7,"category":"Outreach tracking","what":"Job application tracker","verdict":"watch","why":"Only aggregate published data seen; a spreadsheet does the same job","url":"https://huntr.co","status":"active","open_source":false,"grade":"C","src":["S8"],"as_of":"2026-07-01","ttl":"V2"}
```

```jsonl
{"type":"rule","jurisdiction":"EU","instrument":"Directive 2002/58/EC art 13 (ePrivacy)","requirement":"Prior consent for e-mail used for direct marketing to subscribers who are natural persons; soft opt-in for a seller's own similar products to customers; Member States protect legal-person subscribers","status":"in-force","url":"https://www.legislation.gov.uk/eudr/2002/58/article/13/data.htm","applies_to":"Direct marketing e-mail; a job seeker's request for work is not clearly direct marketing; no regulator statement found","effective":"2009-12-19","grade":"A","src":["S36"],"as_of":"2009-12-19","ttl":"V4"}
{"type":"rule","jurisdiction":"EU","instrument":"GDPR art 2(2)(c) household exemption","requirement":"Regulation does not apply to processing by a natural person in the course of a purely personal or household activity; the CJEU read the equivalent exemption narrowly in C-25/17","status":"in-force","url":"https://pub-a0410b6281c64831b9c9612cf6920e67.r2.dev/celex-62017CJ0025.pdf","applies_to":"Systematic collection of third-party contact data may leave the exemption","grade":"B","src":["S35","S60","S61"],"as_of":"2018-07-10","ttl":"V4"}
{"type":"rule","jurisdiction":"UK","instrument":"PECR reg 22 and ICO electronic mail marketing guidance","requirement":"Consent or soft opt-in for direct marketing e-mail to individual subscribers including sole traders; no consent rule for corporate subscribers; sender identification and opt-out","status":"in-force","url":"https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/","applies_to":"Direct marketing; job-seeker message unclear","effective":null,"grade":"B","src":["S37"],"as_of":"2026-11-11","ttl":"V4","note":"Effective date not retained from extract"}
{"type":"rule","jurisdiction":"UK","instrument":"Data (Use and Access) Act 2025, PECR penalties","requirement":"Maximum PECR fine aligned with UK GDPR at GBP 17.5m or 4% of turnover; remaining provisions commenced 2026-06-19","status":"in-force","url":"https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/one-year-on-marking-the-12-month-commencement-of-the-data-use-and-access-act/","effective":"2026-02-05","grade":"B","src":["S38"],"as_of":"2026-06-19","ttl":"V4"}
{"type":"rule","jurisdiction":"US","instrument":"CAN-SPAM Act","requirement":"Covers e-mail whose primary purpose is commercial advertisement or promotion of a commercial product or service; no B2B exemption; opt-out model","status":"in-force","url":"https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business","applies_to":"Employment request not obviously covered; freelance service pitches are","effective":null,"grade":"B","src":["S39"],"as_of":"2026-11-11","ttl":"V4","note":"Effective date not retained"}
{"type":"rule","jurisdiction":"Canada","instrument":"CASL (S.C. 2010, c. 23)","requirement":"Consent for commercial electronic messages; implied consent where a conspicuously published address and a message relevant to the recipient's role","status":"in-force","url":"https://ised-isde.canada.ca/site/canada-anti-spam-legislation/en/node/7","applies_to":"Job-seeker message unclear; no CRTC statement found","effective":null,"grade":"A","src":["S40"],"as_of":"2019-04-01","ttl":"V4","note":"Page dated 2019-04-01, outside the evidence window"}
{"type":"rule","jurisdiction":"Canada","instrument":"Electronic Commerce Protection Regulations SOR/2013-221 s 4","requirement":"First commercial electronic message after a referral by someone with a relationship to both parties is exempt from consent if it names the referrer and says it is sent because of the referral","status":"in-force","url":"https://laws-lois.justice.gc.ca/eng/regulations/SOR-2013-221/FullText.html","effective":"2014-07-01","grade":"B","src":["S41"],"as_of":"2026-05-26","ttl":"V4"}
{"type":"rule","jurisdiction":"India","instrument":"Digital Personal Data Protection Act 2023 s 3(c)","requirement":"Act does not apply to personal data processed by an individual for personal or domestic purposes or made public by the data principal or under a legal obligation","status":"enacted","url":"https://www.trai.gov.in/sites/default/files/2024-09/DPDT_11082024.pdf","applies_to":"Core duties not in force until 2027-05-13 or 14","effective":"2027-05-13","grade":"B","src":["S42","S43"],"as_of":"2026-11-11","ttl":"V4","note":"Sources differ by a day"}
{"type":"rule","jurisdiction":"India","instrument":"DPDP Rules 2025 commencement","requirement":"Rules 1, 2, 17-21 from notification; Rule 4 after 12 months; Rules 3, 5-16, 22-23 after 18 months","status":"enacted","url":"https://www.mondaq.com/india/privacy-protection/1728232/update-meity-notifies-rules-operationalising-the-dpdp-framework-in-india","effective":"2027-05-13","grade":"B","src":["S43"],"as_of":"2025-11-13","ttl":"V4","note":"Notified 2025-11-13 per Gazette; some sources say 14 November"}
{"type":"rule","jurisdiction":"India","instrument":"TRAI TCCCPR 2018 (amended 2025-02-12)","requirement":"Commercial voice calls and SMS using telecom resources follow sender registration, consent and preference rules; email not covered","status":"in-force","url":"https://trai.gov.in/sites/default/files/CP_28082024.pdf","applies_to":"Personal message not obviously commercial communication","effective":"2019-02-28","grade":"B","src":["S44"],"as_of":"2024-08-28","ttl":"V4"}
{"type":"rule","jurisdiction":"Singapore","instrument":"Spam Control Act 2007","requirement":"Unsolicited commercial electronic messages sent in bulk (more than 100 similar messages in the s 6(1)(a) period; further thresholds not read) need an unsubscribe facility","status":"in-force","url":"https://sso.agc.gov.sg/Act/SCA2007","applies_to":"One-to-one personal messages are not bulk commercial messages","effective":"2007-06-15","grade":"B","src":["S45"],"as_of":"2026-11-11","ttl":"V4"}
{"type":"rule","jurisdiction":"Singapore","instrument":"PDPA Do Not Call provisions","requirement":"Specified marketing messages to Singapore telephone numbers need registry checks and sender identification; B2B marketing excluded; messages outside s 37(1) are not specified messages","status":"in-force","url":"https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/advisory-guidelines-on-the-dnc-provisions-(270717).pdf","effective":null,"grade":"B","src":["S46"],"as_of":"2017-07-27","ttl":"V4"}
{"type":"rule","jurisdiction":"Australia","instrument":"Spam Act 2003","requirement":"Commercial electronic messages need consent (express or inferred), sender identification and unsubscribe; consent may be inferred from a conspicuously published work address if the message is relevant to the role","status":"in-force","url":"https://www.legislation.gov.au/C2004A01214/latest/text","applies_to":"Job application not clearly a commercial message; no ACMA statement found","effective":null,"grade":"B","src":["S47"],"as_of":"2026-11-11","ttl":"V4"}
{"type":"rule","jurisdiction":"platform:LinkedIn","instrument":"LinkedIn Help: Prohibited software and extensions","requirement":"No third-party crawlers, bots, plug-ins or extensions that scrape, modify the appearance of or automate activity; accounts may be restricted or shut down","status":"in-force","url":"https://www.linkedin.com/help/linkedin/answer/a1341387","effective":null,"grade":"B","src":["S49"],"as_of":"2026-11-11","ttl":"V2"}
{"type":"measure","subject":"Ashby referred applications","measure":"application to interview rate","unit":"percent","value":40,"n":38000000,"method":"ATS source labels, 2021-01 to 2024-12; descriptive","region":"global","grade":"B","src":["S1"],"as_of":"2025-05-16","ttl":"V3"}
{"type":"measure","subject":"Ashby sourced applications","measure":"application to interview rate","unit":"percent","value":25,"n":38000000,"method":"ATS source labels; descriptive","grade":"B","src":["S1"],"as_of":"2025-05-16","ttl":"V3"}
{"type":"measure","subject":"Ashby inbound applications","measure":"application to interview rate","unit":"percent","value":3,"n":38000000,"method":"ATS source labels; descriptive","grade":"B","src":["S1"],"as_of":"2025-05-16","ttl":"V3"}
{"type":"measure","subject":"Ashby referred interviews","measure":"interview to offer rate","unit":"percent","value":16,"method":"ATS source labels; inbound and sourced were 6%","grade":"B","src":["S1"],"as_of":"2025-05-16","ttl":"V3"}
{"type":"measure","subject":"Offers per 100 referred applications","measure":"40% x 16%","unit":"offers per 100 applications","value":6.4,"method":"Calculation from Ashby rates","grade":"M","src":["S1"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"measure","subject":"Offers per 100 inbound applications","measure":"3% x 6%","unit":"offers per 100 applications","value":0.18,"method":"Calculation from Ashby rates; referral about 36x inbound","grade":"M","src":["S1"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"measure","subject":"Referrals share of hires","measure":"share of hires","unit":"percent","value":18,"method":"Ashby hire-source data; about 1% of applications","grade":"B","src":["S1","S2"],"as_of":"2025-05-16","ttl":"V3"}
{"type":"measure","subject":"Inbound share of hires","measure":"share of hires","unit":"percent","lo":43,"hi":52,"method":"Ashby quarterly range; Q2 2025 52%","grade":"B","src":["S2"],"as_of":"2025-06-30","ttl":"V3"}
{"type":"measure","subject":"Referred candidates passing initial screen","measure":"pass rate vs 35% for non-referred","unit":"percent","value":52,"n":54000000,"method":"Ashby 2021-01 to 2026-03","grade":"B","src":["S3"],"as_of":"2026-05-07","ttl":"V3"}
{"type":"measure","subject":"Same-function referrals, business roles","measure":"interview rate vs 26% for other referrals","unit":"percent","value":37,"method":"Ashby 2026 benchmarks","grade":"B","src":["S3"],"as_of":"2026-05-07","ttl":"V3"}
{"type":"measure","subject":"Gem referrals vs inbound","measure":"hire-rate multiple","unit":"multiple","value":11,"n":165000000,"method":"Gem 2021-06 to 2025-05 applications","grade":"B","src":["S4"],"as_of":null,"ttl":"V3","note":"Publication date not shown on the page"}
{"type":"measure","subject":"Gem sourced vs inbound","measure":"hire-rate multiple","unit":"multiple","lo":4,"hi":8,"method":"Gem reports nearly 8x in one passage and about 4x yield (11% of hires from 2.6% of applications) in another","grade":"B","src":["S4"],"as_of":null,"ttl":"V3","note":"Publication date not shown on the page"}
{"type":"measure","subject":"Instantly cold email platform average","measure":"reply rate","unit":"percent","value":3.43,"method":"Billions of interactions, 2025-01-01 to 2025-12-18; sales email proxy; top quartile 5.5%, top decile 10.7%","grade":"B","src":["S5"],"as_of":"2026-01-12","ttl":"V3"}
{"type":"measure","subject":"Pin LinkedIn messages (recruiter to candidate)","measure":"reply rate","unit":"percent","value":17.08,"n":4000000,"method":"Messages sent through Pin by 1,500+ organisations; proxy","grade":"C","src":["S6"],"as_of":null,"ttl":"V3","note":"Publication date not shown"}
{"type":"measure","subject":"Pin automated recruiting email","measure":"reply rate, delivered basis","unit":"percent","value":4.96,"method":"As above; recruiter-written email 6.31%","grade":"C","src":["S6"],"as_of":null,"ttl":"V3","note":"Publication date not shown"}
{"type":"measure","subject":"Huntr tracked applications","measure":"share reaching interview","unit":"percent","value":1.95,"n":1244654,"method":"User-tracked applications 2024-10-01 to 2026-07-01, via secondary summary","grade":"C","src":["S8"],"as_of":"2026-07-01","ttl":"V3"}
{"type":"measure","subject":"Wiza","measure":"email find rate","unit":"percent","value":55.2,"n":1300000,"method":"Pin vendor-run audit; data window March-May 2026; hit is not deliverability","grade":"C","src":["S7"],"as_of":"2026-05-31","ttl":"V2"}
{"type":"measure","subject":"ContactOut","measure":"email find rate","unit":"percent","value":48.2,"n":1300000,"method":"Pin vendor-run audit; data window March-May 2026","grade":"C","src":["S7"],"as_of":"2026-05-31","ttl":"V2"}
{"type":"measure","subject":"Forager","measure":"email find rate","unit":"percent","value":45.9,"n":1300000,"method":"Pin vendor-run audit; data window March-May 2026","grade":"C","src":["S7"],"as_of":"2026-05-31","ttl":"V2"}
{"type":"measure","subject":"RocketReach","measure":"email find rate","unit":"percent","value":29.8,"n":1300000,"method":"Pin vendor-run audit; data window March-May 2026","grade":"C","src":["S7"],"as_of":"2026-05-31","ttl":"V2"}
{"type":"measure","subject":"Zero replies in 60 sends","measure":"one-sided 95% upper bound on true reply rate","unit":"percent","value":4.87,"n":60,"method":"1 - 0.05^(1/60)","grade":"M","src":["S5"],"as_of":"2026-11-11","ttl":"V5"}
{"type":"measure","subject":"Zero replies in 60 sends if true rate is 3%","measure":"probability","unit":"percent","value":16.1,"n":60,"method":"0.97^60","grade":"M","src":["S5"],"as_of":"2026-11-11","ttl":"V5"}
{"type":"measure","subject":"Break-even hours to secure one vouched referral","measure":"hours per referral at which referral matches cold applying","unit":"hours","value":11.9,"method":"6.4% per referred application vs 0.18% x 3 applications per hour (assumed, D); 5.9 hours if lift halved","grade":"M","src":["S1"],"as_of":"2026-11-11","ttl":"V5"}
{"type":"measure","subject":"Friebel et al. referral programme","measure":"attrition reduction","unit":"percent","value":15,"method":"RCT in a retail chain","grade":"B","src":["S14"],"as_of":null,"ttl":"V5","note":"Published 2023; month not retained"}
{"type":"measure","subject":"Jobs found through family and friends","measure":"wage discount","unit":"percent","lo":5,"hi":7,"method":"US and EU household panels","grade":"B","src":["S18"],"as_of":null,"ttl":"V5","note":"Working paper dated 2004; month not retained"}
{"type":"measure","subject":"Beaman and Magruder Kolkata experiment","measure":"original participants","unit":"people","value":562,"n":562,"method":"Lab-in-field; 407 referrals","region":"India","grade":"B","src":["S15"],"as_of":null,"ttl":"V5","note":"Published 2012; month not retained"}
{"type":"measure","subject":"CNIL fine on KASPR","measure":"administrative fine","unit":"EUR","value":240000,"method":"Decision SAN-2024-020 of 2024-12-05","region":"France","grade":"B","src":["S48"],"as_of":"2024-12-05","ttl":"V4"}
{"type":"measure","subject":"US job and employment scam losses reported to FTC, 2024","measure":"reported losses","unit":"USD","value":501000000,"method":"Reported via secondary article; 2020 figure 90,000,000 USD","region":"US","grade":"B","src":["S58"],"as_of":"2024-12-31","ttl":"V3"}
{"type":"measure","subject":"Contingency recruiter fee","measure":"share of first-year base salary","unit":"percent","lo":15,"hi":25,"method":"Practitioner sources; retained 25-35% of total compensation","grade":"C","src":["S59"],"as_of":"2026-11-11","ttl":"V3"}
{"type":"measure","subject":"TCS Bring Your Buddy referral incentive","measure":"mid-level hire bonus","unit":"INR","value":40000,"region":"India","grade":"C","src":["S32"],"as_of":null,"ttl":"V3","note":"Date not shown in extract"}
{"type":"measure","subject":"Infosys referral bonus by job level","measure":"bonus","unit":"INR","lo":10000,"hi":50000,"region":"India","grade":"C","src":["S33"],"as_of":null,"ttl":"V3","note":"Aggregator quoting ET; date not shown"}
{"type":"measure","subject":"India GCC hiring 2026","measure":"projected jobs","unit":"jobs","value":510452,"method":"foundit Insights Tracker; 64% of new GCC roles need AI or data skills","region":"India","grade":"B","src":["S34"],"as_of":"2026-07-01","ttl":"V3"}
```

```jsonl
{"type":"absence","item":"Measured candidate-initiated reply or interview rate by channel and message type","searched":"Instantly, Pin, Huntr summaries, interviewing.io, vendor and practitioner posts","grade":"E","src":[],"as_of":"2026-11-11","note":"Only proxies, a ranking survey and untraceable vendor claims"}
{"type":"absence","item":"Success rate of referral requests","searched":"Vendor, practitioner and academic searches","grade":"E","src":[],"as_of":"2026-11-11"}
{"type":"absence","item":"Yield of warm introductions and alumni networks in GenAI hiring","searched":"Economics literature, vendor blogs","grade":"E","src":["S19"],"as_of":"2026-11-11"}
{"type":"absence","item":"Vouched vs submit-only referral split in ATS vendor data","searched":"Ashby, Gem, Greenhouse, Lever pages","grade":"E","src":["S1"],"as_of":"2026-11-11"}
{"type":"absence","item":"Official referral-policy pages at frontier labs and Big Tech","searched":"Careers FAQ searches; only GitLab handbook found","grade":"E","src":["S24"],"as_of":"2026-11-11"}
{"type":"absence","item":"Workday referral mechanics","searched":"Search; documentation behind login","grade":"E","src":[],"as_of":"2026-11-11"}
{"type":"absence","item":"Law or employer code on selling referrals; Topmate policy on referral sales","searched":"News, platform pages","grade":"E","src":["S30","S31"],"as_of":"2026-11-11"}
{"type":"absence","item":"Regulator statement on job-seeker outreach under CAN-SPAM, PECR, CASL, Spam Act, PDPA","searched":"FTC, ICO, ISED, ACMA, PDPC pages and secondary summaries","grade":"E","src":["S37","S39","S40","S46","S47"],"as_of":"2026-11-11"}
{"type":"absence","item":"EU Member State rules on e-mail to professional or individual recipients","searched":"Not researched beyond Directive art 13","grade":"E","src":["S36"],"as_of":"2026-11-11"}
{"type":"absence","item":"Indian measured referral share of hires; regulator view on HR contact spreadsheets","searched":"Naukri, foundit, news searches; DPDP texts","grade":"E","src":["S34","S42"],"as_of":"2026-11-11"}
{"type":"absence","item":"Accuracy of email pattern guessing; standalone verifier tools","searched":"Vendor audit pages; not researched further","grade":"E","src":["S7"],"as_of":"2026-11-11"}
{"type":"absence","item":"Terms of service of Wiza, ContactOut, Forager, Apollo, Hunter","searched":"Pricing and audit pages only","grade":"E","src":["S7","S51","S52"],"as_of":"2026-11-11"}
{"type":"absence","item":"X direct-message and LinkedIn InMail data for candidates","searched":"Vendor and practitioner searches","grade":"E","src":[],"as_of":"2026-11-11"}
{"type":"absence","item":"Gee et al., Fernandez-Weinberg, Hensvik-Skans, Kramarz-Skans, Zottoli-Wanous","searched":"Not retrieved in this session","grade":"E","src":[],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K1","verdict":"confirmed","finding":"Ashby 40%/25%/3% and Gem 11x confirmed from vendor pages; Gem's sourced multiple is 4-8x; ratios are per application and descriptive","suggested":"Add information-effect and gating caveats alongside selection","grade":"B","src":["S1","S4"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K2","verdict":"confirmed","finding":"Referral about 18% of hires, inbound 43-52%; 70-85% traces to a 1966 claim and a 2016 poll","suggested":"Keep grade E for 70-85%","grade":"B","src":["S2","S21","S22"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K3","verdict":"updated","finding":"Treatment of already-applied candidates is employer and ATS specific; GitLab downgrades to an endorsement","suggested":"Reword to: ask the referrer how their process treats existing applicants","grade":"B","src":["S24","S25","S26","S27","S28"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K4","verdict":"unverifiable","finding":"No measurement of apply-then-note sequence found","grade":"D","src":["S9"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K5","verdict":"unverifiable","finding":"No measured effect of artefacts on replies; practitioner advice only","suggested":"Regrade to P","grade":"D","src":["S62"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K6","verdict":"unverifiable","finding":"Under-80-word proxy and 58% first-email share are vendor-reported; no candidate data for caps or follow-up count","grade":"B","src":["S5"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K7","verdict":"confirmed","finding":"4.87% bound confirmed by calculation; no candidate rate exists; 60 sends cannot separate 0-3%","grade":"M","src":["S5","S6"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K8","verdict":"confirmed","finding":"Instantly 3.43%/5.5% and Pin 17.08% confirmed; Pin figure is recruiter-to-candidate","grade":"B","src":["S5","S6"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K9","verdict":"confirmed","finding":"52% vs 35% confirmed in Ashby's own 2026 benchmarks (54M applications)","suggested":"Cite Ashby directly instead of a secondary summary","grade":"B","src":["S3"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K10","verdict":"confirmed","finding":"LinkedIn help page bars bots and extensions that automate or scrape and names account restriction","grade":"B","src":["S49","S50"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K11","verdict":"updated","finding":"Apollo free tier captured at 900 credits a year (75 a month) in September to November 2026; earlier 100 a month; sources conflict","suggested":"Update figure and re-verify on apollo.io/pricing","grade":"C","src":["S52"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K12","verdict":"updated","finding":"Hunter free 50 credits a month confirmed; it covers about a third of a 30-sends-a-week cadence","suggested":"State coverage limit","grade":"B","src":["S51"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K13","verdict":"updated","finding":"29.8% confirmed; price is annual-only at about $396-399, not $329","suggested":"Update price","grade":"C","src":["S7","S54"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K14","verdict":"updated","finding":"Clay Launch is $185 a month on monthly billing and $167 on annual","suggested":"Correct billing basis","grade":"C","src":["S53"],"as_of":"2026-11-11"}
{"type":"repo_delta","k":"K15","verdict":"confirmed","finding":"Find rates 55.2/48.2/45.9% confirmed in a vendor-run audit; hit rate not deliverability","suggested":"Note COI and population (recruiter lists)","grade":"C","src":["S7"],"as_of":"2026-11-11"}
```
