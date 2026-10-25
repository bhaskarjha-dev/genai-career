---
id: T0-10
title: "Career Tooling Ecosystem Audit: Evidence-Graded Map of the 12-Stage Career Funnel (October 2026)"
date: 2026-10-21
status: complete-with-declared-gaps
topic: career-tooling-ecosystem
tags: [career-tools, 12-stage-funnel, ats, auto-apply, shadow-ban, bot-detection, resume-builders, interview-prep, ai-interview-assistants, compensation-benchmarking, privacy, job-search-security, evidence-grading]
informs_decisions:
  - "Which tools to adopt, tolerate, or avoid at each of the 12 career-lifecycle stages"
  - "Whether, and under what controls, to use AI auto-apply or agentic application tooling"
  - "Which compensation benchmarks and negotiation resources to trust for offers, especially private VC-backed equity"
  - "Data-handling policy for uploading resumes, offer letters, IDs and interview audio to third-party AI tools"
confidence: medium  # about 0.6 overall: high on ATS mechanisms (vendor docs), moderate on risk direction, low on tool efficacy and on equity-valuation accuracy
---

# Career Tooling Ecosystem Audit: 12-Stage Funnel, October 2026

**Reading notes.**
- Source IDs like [S05] point to the Sources & Evidence Ledger near the end. The Tool Catalog is the last section.
- Evidence grades: **A** = primary source directly on point (vendor/regulator/court documentation, peer-reviewed paper, official dataset); **B** = independent reporting or security research, or two or more independent corroborating sources; **C** = convergent community or aggregate signals, or a single specific-and-checkable source with a conflict of interest (COI); **D** = recalled from model memory, or a single weak or competitor-marketing source (memory-recalled claims are capped at D); **E** = searched and nothing found, or unverifiable.
- "COI" marks sources that sell a competing product. "Not re-verified" marks sources read earlier in the session whose URL I could not re-confirm at write time; those are cited by publisher and title only.
- Funnel stages: 1 Awareness, 2 Exploration, 3 Skills, 4 Certifications, 5 Portfolio, 6 Discovery, 7 Application, 8 Networking, 9 Prep, 10 Execution, 11 Negotiation, 12 Onboarding.
- Temporal anchor: 21 Oct 2026. Evidence base is mostly US/English-language; see Open Questions.

---

## 1. Prior (recalled before searching; Grade D cap)

Five checkable propositions, stated with my initial credence so the Delta section can show what moved.

| # | Proposition (as believed before research) | Initial credence | How it can be checked |
|---|---|---|---|
| P1 | Ashby and Greenhouse run employer-configurable bot/spam defenses, and browser-automation submissions can be rejected or flagged. But a persistent, cross-employer "shadow-ban" of a candidate's IP or identity is not a documented mechanism. | Mechanisms exist: 0.80. Cross-employer persistent shadow-ban documented: 0.15 | Vendor docs; incident reports; search for any shared blocklist |
| P2 | "ATS auto-rejects you for formatting or keywords" is mostly myth; knockout questions and employer rules do reject. Consumer "ATS scores" (Jobscan, Rezi, Teal, etc.) are proprietary heuristics with no independent validation. Multi-column or graphic-heavy templates are the most plausible parse risk. | 0.70 | Vendor statements; independent parser benchmarks; recruiter-side evidence |
| P3 | Mass auto-apply (LazyApply-class) converts worse than targeted applying, risks LinkedIn account restriction, and can hurt reputation with the same employer. "Simplify auto-apply" is really autofill with a human submit. | 0.75 (the Simplify clause: 0.60) | Conversion datasets; platform ToS; recruiter surveys; Simplify's own docs |
| P4 | Undisclosed live AI interview copilots (Cluely-class, Final Round AI "stealth") are net-negative: employers increasingly prohibit or detect them. AI mock interviews are low-risk practice but unvalidated for outcomes. | 0.85 | Employer policies; detection reports; complaint patterns |
| P5 | Levels.fyi is the strongest public comp dataset for big-tech and public-company roles; no tool reliably values private VC-backed equity. Resume-builder platforms carry non-trivial billing dark-pattern and data-exposure risk. | 0.70 | Methodology statements; breach reports; billing complaint patterns |

---

## 2. Research Question

**Decision.** Which career tools, platforms and automated job-search assistants are genuinely effective, and which are predatory, low-quality or dangerous to a candidate's reputation, at each of the 12 career-lifecycle stages in late 2026?

**Sub-questions (mapped to the five domain probes).**
- Q1. What bot-detection mechanisms do Ashby, Greenhouse and Lever document, and does the "AI mass-apply bots get IP-blacklisted and shadow-banned" claim hold up?
- Q2. Do resume builders and "ATS score" tools measurably help against real ATS parsers?
- Q3. Which technical-interview prep platforms offer verifiable value for GenAI system design versus legacy algorithm prep?
- Q4. Are AI mock-interview tools effective for practice, and what are the severe risks of live AI assistance during real screens?
- Q5. Which comp tools give the most reliable equity valuation for private VC-backed AI scaleups, and are salary databases and negotiation services fresh and trustworthy?
- Q6. What are the privacy, leakage and security risks of uploading resumes and offer letters to third-party AI career tools?

**Method (what I actually did).** About 75 search and fetch calls on 21 Oct 2026. I read primary vendor documentation for Ashby, Greenhouse and Lever; platform terms (LinkedIn); regulator and court material (CFPB, FTC, Mobley v. Workday); peer-reviewed or preprint studies; security-research reports; and community or review-site signals (Trustpilot, Blind, Hacker News). I **did not** hands-on test any tool, and I **did not** run automated submissions against any live ATS, which would breach employers' and platforms' terms. Where a question needed that (Q1), the verdict rests on documentation plus incident reports, and that limit is stated wherever it matters.

**Out of scope.** General productivity software (Notion, Google Docs) unless wired into career workflows; non-career uses of LLMs.

---

## 3. Key Findings (12)

**KF1. Bot and spam defenses exist at all three named ATSs, but they are employer-configured, signal-based and scoped to one employer.** Grade A (mechanisms) / B (practice).
Ashby lets each employer pick a spam-protection level (strict, permissive [recommended], less permissive, none) and warns that strict can reject real candidates [S01]. Ashby's separate fraud detection analyses device, IP, email and phone signals when an application is submitted and presents signals rather than verdicts [S03, S04]. Greenhouse uses invisible reCAPTCHA that watches mouse and typing behavior, with an email-code fallback and per-board sensitivity [S06]; an admin-managed IP/email-domain blocklist [S07]; and Real Talent fraud checks built on IPQS signals, where a data-center IP counts as a high-risk signal [S05]. Lever's documented control is repeat-application blocking keyed to email plus job-site source tag [S11]; I found no public bot-detection documentation for Lever (declared gap). Honeypots, submission-speed guards, disposable-email blocks and CAPTCHA recur across other ATSs [S12].

**KF2. The injected claim ("auto-apply bots trigger automated IP blacklists and ATS shadow-bans") is partly right and mostly wrong as stated.** Grade A/B for the pieces, E for the headline.
Confirmed: bot heuristics exist; automated browsers can be rejected (KF3); IP and email blocklists exist; data-center IPs are treated as high-risk. Not confirmed: that blocklists are populated automatically by bot behavior (Greenhouse's are admin-managed [S07]); that flags travel between employers (Greenhouse says fraud signals are specific to the organization, and IPQS does not use submitted candidate data to feed its network [S05]; the MyGreenhouse FAQ says candidate information is not shared across employers [S08]); that rejection is invisible in every case (Ashby's spam rejection shows an error to the applicant per [S13]). What *is* documented is **local, employer-configured silent rejection**: Greenhouse blocklist rejections send no rejection email by default [S07], and an Ashby application-limit block may show the board's default post-submission text if the employer left the block message blank [S02]. A flagged Greenhouse candidate can also be filtered out of recruiter search views [S05]. Net: employer-level silent blocks are real; a tool-triggered, persistent, cross-ATS shadow-ban has no supporting evidence found.

**KF3. Automated-browser submissions were demonstrably rejected by Ashby in at least one reproducible report; the mechanism is inferred, not confirmed.** Grade B/C.
A GitHub issue (career-ops #4269, reported by a vendor blog as opened 17 Sep 2026; date not visible on the page I fetched) describes Ashby rejecting Playwright-driven submissions as "flagged as possible spam" while the same details went through from an ordinary browser [S13]. The error text advises turning off VPN or proxy and pausing browser extensions, which hints that those signals feed the decision. The reporter's explanation (reCAPTCHA-style scoring of automation flags) is a hypothesis; Ashby has not confirmed it [S01]. The rejection was visible, per-submission and cleared on retry, which argues against a persistent IP ban. Inference, unverified: cloud-hosted auto-apply agents submit from data-center IPs, which Greenhouse treats as high-risk [S05]; at least one Show HN auto-apply product states it uses cloud browser sessions [S23].

**KF4. Auto-apply at volume has weak and mostly adverse evidence, and "Simplify auto-apply" needs correcting.** Grade B/C.
Huntr's Q1 2026 dataset (139,927 applications from 25,635 users; vendor-run, self-tracked, correlational) shows its interview-rate metric falling from 9.25% for users sending 11-20 applications to 2.58% for users sending 100+, and from 6.07% for a single application at a company to 1.91% for eight or more at the same company [S16]. Recruiter-side surveys agree on direction: in a Robert Half survey of 2,000+ US hiring managers (Mar 2026), 67% said AI-generated applications slowed hiring and 65% said skills were harder to verify (reported second-hand) [S19]; Greenhouse reports 3x the applications per recruiter since 2022 [S10]. LinkedIn prohibits bots and extensions that automate activity and says accounts risk restriction [S15]. LazyApply sits near 2.4/5 on Trustpilot with wrong-answer and refund complaints [S22]. **Premise correction:** Simplify Copilot is autofill where the human submits; a separate "Autopilot" auto-submit beta exists per a competitor's account of Simplify's help center [S17]; Jobscan is also reported to have launched an Auto Apply feature (not re-verified).

**KF5. AI writing help can raise hiring odds in narrow forms; generic AI text erodes the signal.** Grade A (RCT, narrow) / B.
A field experiment with roughly half a million jobseekers on an online labor market found that *non-generative* algorithmic writing assistance on resumes raised hiring by 8% and wages by 10%, with no sign employers were less satisfied (Management Science 2025) [S20]. After Freelancer.com introduced an AI cover-letter tool, cover letters became less correlated with hiring outcomes, while job-specific tailoring still predicted callbacks [S21]. Together: tailoring and clarity help; undifferentiated generative output is discounted. External validity to corporate ATS hiring is unproven.

**KF6. No independent ATS-parser benchmark of consumer resume builders exists in what I found; vendor "ATS scores" are internal heuristics, and "the ATS rejects you" is mostly a knockout-question and recruiter-triage story.** Grade C (absence: E).
Every benchmark I found was vendor- or affiliate-published, and they conflict with each other (for example on whether design-first templates parse) [S25, S26]. One roundup openly notes that Rezi's score is internal and that real ATSs have no universal score [S26]. Greenhouse's AI Talent Matching assigns match scores but states it does not automatically advance or reject candidates, and candidates can opt out of the score [S08]. Rule-based rejection still happens through screening and knockout questions (Huntr's reading) [S16]. "No ATS auto-screens" is also too strong: AI screening at Workday is the subject of unproven discrimination allegations in Mobley v. Workday (collective conditionally certified May 2025; in discovery as of spring 2026) [S28].

**KF7. The resume and career-builder category carries billing dark-pattern and data-exposure risk.** Grade B/C.
BOLD/Bold LLC-family builders (Zety, MyPerfectResume, LiveCareer, Resume Now) are consistently described as a low-priced trial (about $3) that converts to roughly $24 every four weeks, i.e. 13 charges a year, with cancellation and refund complaints on Trustpilot and the BBB (BBB claims second-hand) and a watchdog note on broad data sharing [S27]. LiveCareer exposed more than 5.1M files (mostly resumes dating back to 2016) in an unsecured Azure container, and had not acknowledged it at publication; HireClick (5.7M files) and TalentHook (about 26M files) had similar storage misconfigurations [S42]. On the employer side, McHire/Paradox.ai exposed up to 64M applicant records through default credentials plus an IDOR flaw (Paradox says five records were viewed, by the researchers) [S41].

**KF8. Live AI copilots are high-risk; employer policy is diverging; detection figures are vendor-sourced.** Grade B/C.
Amazon reportedly told recruiters to disqualify candidates found using AI tools in interviews; Meta piloted AI-assisted coding interviews with disclosed use; Anthropic initially asked applicants not to use AI and then reversed course (Business Insider via AOL) [S30]. Fabric, which sells detection, flagged 38.5% of 19,368 AI-run interviews (Jul 2025-Jan 2026); an independent critique notes these are Fabric's own figures and that 61% of flagged candidates still cleared the pass bar [S29]. A Gartner "72.4% run in-person interviews" figure is only available second-hand [S31]. Final Round AI shows 3.5/5 on Trustpilot (about 250 reviews) with refund, lock-out and copilot-latency complaints [S32]. Undisclosed live assistance in an assessed setting is a hard disqualifier in my rubric.

**KF9. For GenAI system design the best-verifiable prep offering is Hello Interview; no prep platform has independent outcome evidence.** Grade B (pricing) / C (value).
Hello Interview's pricing page (fetched 21 Oct 2026) lists Premium at $47 (1 month), $89 (1 year) and $299 (lifetime), including ML System Design and AI Coding tracks, 66 Guided Practice problems and AI-run "Live Practice" interviews; it no longer lists human mock-interview pricing, and a third-party directory says the human mock program ended 31 May 2026 [S33]. Interviewing.io and Exponent (which absorbed Pramp) remain the other mainstream options, with community praise for calibration and complaints about price [S34]. I found no independent outcome study for any platform (Grade E), the review ecosystem is affiliate-heavy, and GenAI-specific system-design coverage outside Hello Interview and ByteByteGo is thin or commodity-grade. Classic algorithm practice (LeetCode, NeetCode) stays the baseline because AI-permitted interview formats are still a minority and policies vary by employer [S30].

**KF10. Comp data is usable for base and big-tech total comp, but equity values (especially private-company options) are not standardized, and no tool has verified accuracy against realized outcomes.** Grade B/C (accuracy: E).
Levels.fyi's founder documents the method: new-offer submissions annualize the grant over the vesting schedule; existing-employee submissions report realized (W-2) value; sign-on bonuses are annualized at one quarter; benefits are excluded [S36]. Community threads show user confusion about RSU conventions and wide within-level variance, with one reply advising caution on RSU figures [S36]. For private companies, nothing I found shows a standard valuation basis. Posted-range tools (Comprehensive.io) cover legally posted base ranges [S38]; Carta says its startup data comes from HRIS and cap-table integrations (vendor claim, 2023 post, current status unverified) [S38]. Negotiation-service outcomes are self-reported (Levels.fyi sells flat-fee coaching with a money-back guarantee whose thresholds vary by package and page version; Rora charges a percentage of the increase) [S37]. Peer-reviewed work shows LLM salary advice varies by the persona asked [S39]. FairOffer: searched, not found.

**KF11. The discovery and execution layers are polluted by scams, ghost jobs and fake-recruiter malware.** Grade A/B.
FTC data show job and employment-agency scam losses rising from $90M (2020) to $501M (2024) [S45]. The North Korea-linked "Contagious Interview" campaign uses fake recruiters and coding tests to deliver malware; Microsoft says it has been active since at least December 2022, and Socket reported 338 malicious npm packages with 50,000+ downloads [S35]. Huntr's survey (about 593 respondents, self-selected) found 93% had applied to or suspected ghost jobs [S16]. The Texas Attorney General opened an investigation into LinkedIn (reported July 2026) [S46]. Source conversion in Huntr's data is highest for Google (7.12%) and Wellfound (5.02%) and lowest for Indeed (3.14%) and LinkedIn (2.94%) [S16]; these are correlational and depend on user mix.

**KF12. Platform stability and lock-in risk is real at the skills, portfolio and extension layers.** Grade A/B.
The CFPB's April 2024 consent order found BloomTech (formerly Lambda School) misdescribed income-share agreements as non-loans and inflated placement claims; the school's last day of instruction is reported as 31 Dec 2025 [S48]. Coursera and Udemy completed their merger in May 2026, so catalog and pricing may shift [S47]. Read.cv was acquired by Perplexity in January 2025 and users had until 16 May 2025 to export [S50]. Certification premiums are mixed: Huntr sees a flat effect by count, and Foote Partners data show premiums for certified skills moving against non-certified skills across periods [S16, S49]. Fake "AI assistant" Chrome extensions (LayerX "AiFrame") reached 260-300k installs by loading remote code that can change behavior without a store update, so any career extension with broad permissions is a supply-chain risk [S43].

---

## 4. Recommendation

### 4.1 Bottom line

1. **Adopt supervised automation.** Automate form-filling and tracking. Do not automate identity-bearing accounts (LinkedIn, Indeed), do not submit at volume, and never use anything undisclosed during a live assessment.
2. **Read the shadow-ban risk as local, not global.** The documented penalties are employer-level (repeat-application limits, admin blocklists, silent rejections), per-submission rejections of automated browsers, and a conversion penalty for volume. They are not a permanent cross-ATS blacklist. Do not become complacent: VPN/proxy use, data-center IPs, browser extensions and automation flags are all documented or reported risk signals [S01, S05, S13].
3. **Resumes:** a single-column, text-selectable PDF, tailored per role. Treat vendor "ATS scores" as a checklist at most, not as a measurement of any real ATS.
4. **Interviews:** AI for practice only. Follow the employer's stated AI policy. Run recruiter-supplied code in a disposable sandbox.
5. **Compensation:** triangulate. For private equity, get the numbers and model scenarios. Treat coaching-service outcome claims as unaudited marketing.
6. **Data:** assume anything uploaded to a free career tool is retained, possibly shared and possibly exposed. Upload the minimum.

### 4.2 Codified criteria: Recommended / Viable / Caution / Avoid

Each tool is scored 0-2 on six criteria (E1-E6, total 0-12). Scores are analyst judgments anchored to the definitions below. They are not measurements; treat plus or minus 1 as noise. Where something was searched and nothing was found, the criterion is scored conservatively.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **E1 Efficacy evidence** | Evidence of net harm, bias or contradicted claims in the core function, or no credible evidence the function works at all | Function documented and plausible (Grade C/D), outcomes unvalidated, or evidence conflicting | Grade A/B evidence of benefit, or official/primary-source status |
| **E2 Data exposure** | Documented breach or exposure; unknown handling of high-sensitivity inputs (audio, video, ID, offer letters); or remote-updatable broad-permission code in a category with incidents | Disclosed policy with broad permissions, or a training-on-user-content clause | Minimal data, local-only, open-source, or public/government data |
| **E3 ToS and reputation risk** | Core function prohibited by a platform's terms, or penalized by employers (documented) | Gray area, new, or unknown | Compliant and employer-neutral |
| **E4 Commercial conduct** | Regulator enforcement action or investigation concerning the product's commercial conduct, or a recurring billing/refund complaint pattern across at least two independent sources | Paid with unaudited conduct, isolated complaints, or opaque pricing | Free, or transparent pricing with no complaint pattern found when searched |
| **E5 Stability and lock-in** | Shut down, locked out users, or closing | Beta, young, recent acquisition or merger, or unclear export | Established three or more years, stable, exportable or stateless |
| **E6 Independence of evidence** | Vendor or competitor sources only | Mixed, or one independent source | Two or more independent (non-vendor, non-competitor) sources |

**Hard disqualifiers (force Avoid).**
- D1: a regulator or court finding of deceptive practice against the tool or its vendor.
- D2: the core function violates a platform's terms, exposing the user's account to restriction.
- D3: the primary function is undisclosed live assistance in an assessed setting.
- D4: defunct, or shut down without a working export path.

**Status rules, applied in this order.**
1. **Avoid:** any hard disqualifier, or total of 2 or less.
2. **Caution:** any of E1-E5 equals 0 (with no disqualifier), or total of 5 or less.
3. **Recommended:** total of 9 or more, and each of E1-E5 at least 1, and E3 equals 2, and E6 at least 1. This bar is deliberately hard: it requires independent evidence, which most of this category lacks.
4. **Viable:** everything else (so total 6-8, or 9+ while failing a Recommended condition).

A "Viable" label therefore means "usable with the stated controls, evidence is thin", not "validated". Statuses flip if evidence changes.

### 4.3 Recommended stack by stage

| Stage | Recommended | Viable (with controls) | Caution / Avoid |
|---|---|---|---|
| 1 Awareness | BLS Occupational Outlook Handbook; O*NET OnLine | Huntr trend reports (directional) | Caution: LLM chatbots as a sole career advisor |
| 2 Exploration | O*NET interest profiler and occupation data | roadmap.sh (recalled, D); ADPList conversations; LLMs for drafting questions | Caution: LLM advice for career-choice decisions |
| 3 Skills | none reaches the bar | Coursera/Udemy (post-merger), freeCodeCamp, Hugging Face / DeepLearning.AI / Kaggle free courses | Avoid: income-share-agreement bootcamps (BloomTech model) |
| 4 Certifications | none reaches the bar | Role-gated vendor cloud certs; CompTIA entry certs | Caution: unaccredited "AI certification" badges |
| 5 Portfolio | none reaches the bar | GitHub profile + Pages; Hugging Face Spaces / Kaggle | Avoid: Read.cv (defunct); keep work on exportable, own-domain hosting |
| 6 Discovery | none reaches the bar | Google Jobs and direct employer boards; LinkedIn (free); Wellfound; Indeed/Handshake | Caution: LinkedIn Premium Career, Jobright.ai, Scoutify |
| 7 Application | none reaches the bar | Simplify Copilot (autofill); Huntr; Teal; Jobscan; Rezi; Kickresume; Enhancv (single column); MyGreenhouse; CLEAR (employer-initiated only) | Caution: Simplify Autopilot, Jobscan Auto Apply, hosted agents, Sonara, BOLD-family builders, Resume.io, Canva templates. Avoid: LazyApply-class bulk apply |
| 8 Networking | none reaches the bar | LinkedIn (manual); ADPList; MentorCruise; Blind | Avoid: third-party LinkedIn automation |
| 9 Prep | none reaches the bar | Hello Interview; Interviewing.io; Exponent; NeetCode/LeetCode; Google Interview Warmup; Yoodli/Big Interview; ByteByteGo | Caution: Final Round AI (mock mode), Beyz / Interviews by AI |
| 10 Execution | Disposable VM/container sandbox for assessments | CLEAR verification (employer-initiated) | Avoid: Final Round AI live copilot; overlay copilots (Cluely, Interview Coder, Parakeet AI, LeetCode Wizard) |
| 11 Negotiation | Levels.fyi salary database (base and big-tech total comp; not a private-equity valuation tool) | Comprehensive.io posted ranges; Levels.fyi negotiation service; Carta; Candor; Rora | Caution: LLM as negotiation advisor; FairOffer (existence and status unverified) |
| 12 Onboarding | none reaches the bar | ADPList; MentorCruise; Blind | none |

### 4.4 Operating rules

**A. Auto-apply and agentic apply.**
- **R1.** Never run automation inside a logged-in LinkedIn or Indeed session. LinkedIn prohibits bots and extensions that automate activity and names account restriction as the consequence [S15].
- **R2.** Prefer autofill with a human clicking Submit (Simplify Copilot, MyGreenhouse). Treat any agent that submits for you as Caution until you have verified, for the specific ATS, that it works and what it answers on your behalf.
- **R3.** Target and cap. Build a short list, apply once per company per cycle unless roles are genuinely distinct, and tailor each application. Huntr's data show 1.91% for eight or more applications at the same company versus 6.07% for one, and 4.23% tailored versus 2.07% untailored (correlational) [S16].
- **R4.** Do not evade controls. No VPN-hopping, proxy rotation, or throwaway or alias emails to dodge application limits: Ashby identifies repeat applicants by email, and Recruitee ignores plus-aliases [S02, S12]. Evasion is deceptive and can turn a soft block into a fraud flag.
- **R5.** Review what is submitted. Wrong screening answers (work authorization, EEO, salary) are the most frequent failure pattern in complaints [S22]. Log every submission in a tracker.
- **R6.** If Ashby shows the spam error: stop, pause extensions, use a clean browser profile without VPN or proxy, retry once manually, and email the recruiter if it persists [S13].
- **R7.** Treat extension permissions like credentials. Install only from verified publishers, review permissions, and remove what you no longer use [S43].

**B. Data hygiene for AI career tools.**
- *Tier 1:* resume without home address, date of birth or ID numbers. Acceptable for reputable tools.
- *Tier 2:* offer letters, comp history, equity documents. Only to tools whose retention and training terms you have read, or redact company names and personal fields first.
- *Tier 3:* government ID or selfie. Only for employer-initiated verification via a link you reached through a known channel [S08, S10].
- *Tier 4:* interview audio or screen capture, and any LinkedIn credentials or session cookies. Do not give these to third-party tools.
- Use a dedicated email and phone number for job-search tooling (for compartmentalization, not evasion).
- Check retention period, training on user content (for example, Kickresume's policy reserves the right to train on anonymised user documents [S44]), subprocessors, and export and delete paths. Treat "free" builders as data-sharing unless the policy says otherwise [S27].

**C. Interviews.**
- Use AI before the interview, never undisclosed during it. Read the invite and the employer's published AI policy, because they differ (Amazon, Meta, Anthropic's reversal) [S30].
- Run recruiter-supplied code and take-homes only in a disposable VM or container with no credentials, because fake-interview malware campaigns are documented [S35].
- Verify recruiters against the company's official careers page. Legitimate processes do not ask for payment, crypto, or remote-control software [S45].

**D. Compensation.**
- Triangulate at least three sources and prefer new-offer data over existing-employee data when preparing an ask [S36].
- For private equity, request: fully diluted share count, strike price, the latest 409A (common) value, the last preferred price, and the liquidation-preference stack. Then model scenarios. None of the tools audited here do this reliably (accuracy Grade E).
- Do not rely on an LLM's number. Use it to structure the conversation and rehearse, and check any figure against two data sources [S39].

### 4.5 Re-audit triggers

Re-run this audit on any of: a terms change at LinkedIn, Greenhouse, Ashby or Lever; an ATS documenting new bot signals; Simplify Autopilot leaving beta or changing behavior; a regulator action or breach disclosure involving a catalogued tool; a pricing or ownership change at Hello Interview, Coursera/Udemy, or the BOLD-family brands. Otherwise re-audit every 90 days.

---

## 5. Alternatives Considered

| # | Alternative | Verdict | Why |
|---|---|---|---|
| A1 | Full-volume hosted auto-apply as the main strategy | Rejected as a default | Evidence of benefit is absent; adverse signals are consistent (volume and same-company conversion drop, recruiter fatigue, wrong-answer and refund complaints); documented bot defenses at Ashby and Greenhouse. If tried at all, run it as a logged N-of-1 experiment with a kill switch. |
| A2 | Fully manual applications | Keep for high-value targets | Lowest platform risk; tailoring correlates with better outcomes [S16, S21]. Costs time. |
| A3 | Autofill with human review | **Chosen default** | Keeps the human in the loop; no documented penalty for real-browser autofill. Residual unknown: Ashby's error text mentions pausing browser extensions [S13]. |
| A4 | Paying a person or service to apply for you | Not evaluated; not recommended | Same terms exposure as auto-apply, plus credential sharing; no evidence found. |
| A5 | A general LLM as a single "career copilot" | Use for drafting and rehearsal only | Documented bias and instability in advisory use [S39, S40]; privacy exposure for uploads; fabricated metrics risk. |
| A6 | Vendor "ATS score" tools versus a plain-format resume with manual job-description matching | Prefer the plain-format approach | No independent benchmark; the scores are proprietary heuristics [S25, S26]. |
| A7 | Human negotiation coaching versus data-only versus LLM | Hybrid: data first, coaching optional, LLM for rehearsal | Coaching outcomes are self-reported [S37]; data tools differ in method [S36]. |
| A8 | Live AI assistance with disclosure, where permitted | Viable only with explicit employer permission | Meta's pilot shows permitted formats exist; Amazon shows others prohibit [S30]. |
| A9 | Alternative classification schemes (star ratings, weighted composite or single "trust score") | Rejected | Unverifiable and easy to game; the categorical rubric ties each point to an evidence type. |
| A10 | "Stick to big-name tools" as a heuristic | Rejected | Large brands appear in the incident record (LiveCareer, McHire/Paradox.ai) [S41, S42]. |

---

## 6. Detailed Findings

### DF-1. Bot detection and the "shadow-ban" claim (Q1)

**Table A: documented controls, by ATS**

| ATS | Control | Keyed on / signals | Set by | Applicant sees it? | Shared across employers? | Src | Grade |
|---|---|---|---|---|---|---|---|
| Ashby | Application spam protection | Behavioral check of "real candidate vs bot"; method undisclosed (a reporter infers reCAPTCHA-style scoring) | Employer admin; four levels (strict, permissive, less permissive, none) | Yes: error shown (per reporter) | No evidence | S01, S13 | A (existence), C (mechanism) |
| Ashby | Application limits (throttle; repeat-after-rejection) | Email address | Employer admin; plan-gated; does not apply to Indeed applications | Employer-set message, or the default post-submit text if left blank; admin sees a blocked-submissions list | No evidence | S02 | A |
| Ashby | Candidate fraud detection | Device, IP, email, phone signals at submission | Employer toggle | No: flags the profile for reviewers; signals, not verdicts | No evidence | S03, S04 | A |
| Greenhouse | Invisible reCAPTCHA with email-code fallback | Mouse and typing behavior score | Employer sets sensitivity per job board | Yes: verification step | Score is computed Google-side (inference) | S06 | A (existence), D (inference) |
| Greenhouse | Spam and IP blocklist (beta) | IP, email, email domain (Gmail/Yahoo cannot be blocked) | Site admin | Auto-rejected with reason "Rejected by organization blocklist"; no rejection email by default | No | S07 | A |
| Greenhouse | Real Talent fraud detection | IPQS device and contact signals; data-center IP is a high-risk signal; optional ID verification (CLEAR) | Employer | No: recruiters can filter flagged candidates out of search and Talent Matching views | Flags not shared across customers; IPQS does not use submitted data to feed its network | S05, S09 | A |
| Lever | Block repeat applications | Email plus job-site source tag, per posting, within a time window | Employer | Message shown | No | S11 | A |
| Lever | Bot detection | None found in public docs | n/a | n/a | n/a | n/a | E (gap) |
| Workable | WAF, IP reputation, rate limiting, CAPTCHA | n/a | Platform | n/a | n/a | S54 (not re-verified) | A |
| Teamtailor | Spam filter (historic spam domains; suspiciously fast submissions) | n/a | Platform | n/a | n/a | S54 (not re-verified) | A |
| Other ATSs | Honeypot fields, disposable-email blocks, submission-speed guards; email/phone-keyed application limits that strip plus-aliases | Various | Employer or platform | Usually a message | No | S12 | A |

Context on scale: in Huntr's tracked applications, Greenhouse (23.73%), Workday (21.72%), Ashby (15.41%) and Lever (6.95%) are the largest ATSs [S16]. Huntr's users skew tech, so the share is directional. **Workday's bot defenses were not searched** (declared gap), even though it is the second-largest ATS in that sample.

**An infrastructure-level IP-reputation path exists, separate from any ATS.** Greenhouse's fraud checks consume IP and device reputation from IPQS. IPQS markets its own cross-customer threat network, in which abusive IPs reported across its customers can be listed more widely [S14]. So an IP that is abusive across the web (a data-center or proxy range used by many bots) can carry a poor reputation score regardless of which ATS it hits. That is an IP-reputation effect, not an ATS shadow-ban. Inference (Grade D): whether auto-apply vendors' egress IPs are scored badly is unverified.

**Table B: decomposition of the injected claim**

| Sub-claim | Verdict | Evidence | Grade |
|---|---|---|---|
| Auto-apply tools trigger bot-detection heuristics in Ashby and Greenhouse | **Partly confirmed.** Heuristics exist; one reproducible automated-browser rejection on Ashby. No evidence either way for extension-based autofill running in a human's own browser. | S01, S06, S09, S13 | A / C |
| ...which build IP blacklists automatically | **Not supported.** Greenhouse's blocklist is admin-curated. Data-center IPs raise a risk flag; they are not auto-blocked. | S05, S07 | A |
| ...across ATS vendors (Ashby plus Greenhouse plus Lever) | **Not supported.** Greenhouse says flags are customer-specific and not shared; MyGreenhouse says no cross-employer sharing; nothing found for Ashby or Lever. | S05, S08 | A |
| ...resulting in "shadow-bans" (silent and persistent) | **Split.** Silent *local* rejection is documented (blocklist default; Ashby default message). Persistent *global* shadow-ban: no evidence. Ashby's spam rejection is visible. | S02, S07, S13 | A / E |
| Repeat-application penalties at the same employer | **Confirmed (configurable).** Ashby, Lever, Recruitee and others block repeats by email or phone. | S02, S11, S12 | A |
| Recruiters downgrade serial or irrelevant applicants | **Plausible, correlational.** 1.91% at 8+ applications to one company versus 6.07% at one. | S16, S19 | C |

**What a decisive test would look like (not run here).** On a job board you control (an employer trial account on Ashby or Greenhouse), submit identical applications via (a) manual entry, (b) extension autofill, (c) a browser-automation framework, and (d) a hosted agent, from the same IP and from a data-center IP. Record block, flag and error rates, then repeat against a second board to look for cross-board effects. I did not run this: submitting automated traffic to employers' systems would breach their terms, and I had no authorized board.

### DF-2. Auto-apply risk register and tool landscape

**Risk register**

| # | Risk | Mechanism | Evidence | Grade | Mitigation |
|---|---|---|---|---|---|
| R1 | Platform account restriction | LinkedIn bans automation tools; restrictions can lift once the software is disabled | S15 (rule); incidence rates are vendor marketing (E) | A / E | Never automate logged-in LinkedIn/Indeed sessions |
| R2 | Per-submission rejection on Ashby or Greenhouse | Spam scoring, CAPTCHA or email-code gates, data-center or VPN flags | S01, S06, S13 | A / C | Human-driven browser; pause extensions; no VPN or proxy |
| R3 | Employer-level silent block | Repeat-application limits; admin blocklists | S02, S07, S11 | A | One application per company per cycle |
| R4 | Wrong or fabricated answers | Auto-filled screening, EEO or salary fields; AI-invented metrics | LazyApply complaints (S22); vendor test on AI bullet generators (S25) | C / D | Review every submission; keep a log |
| R5 | Reputation drag | Duplicates and low-fit applications | S16, S19 | C | Target list; tailor |
| R6 | Credential and data exposure | Sharing logins or cookies; broad extension permissions; remote-updatable code | S43 | B | Use verified publishers; minimize permissions |
| R7 | Billing and refund friction | Subscriptions and lifetime-deal conversions | S22, S27 | C | Read terms; use a card with dispute rights |
| R8 | Vendor churn | Shutdowns and brand resales (Sonara 2024) | S24 (competitor sources; not re-verified) | D | Keep your own tracker and exportable profile |

**Tool landscape (what the evidence supports).**
- **LazyApply.** Bulk-applies through job boards. Trustpilot shows about 2.4/5 on roughly 107 reviews on the page I read; recurring complaints are wrong answers, applications outside the user's qualifications, and refund difficulty. Competitor sources disagree on pricing (one-time versus annual) [S22]. LinkedIn's terms make the core function a violation [S15].
- **Simplify.** Copilot is autofill. A competitor's reading of Simplify's help center describes Autopilot as a beta that applies to jobs the user chose, uses weekly credits (about 20), has no review step, and fails rather than guesses when a field is unclear [S17]. I could not retrieve Simplify's own documentation for Autopilot, so this is Grade C/D.
- **Hosted agents.** FastApply's own test of eight bots (May 2026) claims only three actually click Submit [S18]. Vendor with COI; Grade D.
- **Sonara.** The original service shut down on 1 Feb 2024 and the brand was reportedly relaunched under BOLD, per competitor blogs and one user review about a suspension and refund dispute (not re-verified) [S24].
- **Community signal.** The Show HN threads I could retrieve were low-engagement (3 points) with generic or promotional-looking comments, so they carry almost no evidential weight [S23]. I found no high-quality Reddit or Hacker News thread documenting an ATS-level ban of a named tool (declared gap).

### DF-3. Resume builders versus parsers (Q2)

- **Benchmark quality.** I found no independent, reproducible parser benchmark of consumer resume builders. The "benchmarks" come from vendors and affiliates: atsverification.com runs an "ATS-style parser" of its own, and ranking pages put their publisher first (Rezi, Resume Genius) [S25, S26]. Their claims conflict, for example on whether Enhancv's design-heavy layouts parse and on how Greenhouse and Lever treat two-column files. Grade D.
- **What converges.** Vendor tests agree that single-column, text-selectable files are the safest format and that image-based exports (some design-tool PDFs) fail most often. Vendor-only; Grade D. A practical check (my suggestion, not sourced): paste the PDF's text into a plain-text editor; if reading order is scrambled, a parser will likely scramble it too.
- **Scores are internal.** One roundup states plainly that Rezi's score is internal and no real ATS has a single universal score [S26]. Treat Jobscan, Rezi, Teal and Enhancv scores as keyword-coverage checklists.
- **Reported prices (verify; roundups and vendor statements).** Teal+ about $9 per week or $29 per month; Rezi about $29 per month or $149 lifetime; Kickresume about EUR 8 per month on annual billing; Enhancv about $24.99 per month; Jobscan Premium about $49.95 per month [S26].
- **Real ATS behavior.** Greenhouse's AI Talent Matching scores applications but does not auto-advance or auto-reject, and offers an opt-out [S08]. Auto-rejection by rule happens through knockout questions [S16]. Workday's AI screening is alleged, not proven, to discriminate [S28].
- **Accuracy matters.** Huntr reports 18% of offers withdrawn in Q1 2026 (reasons not broken out in the figures I read) [S16]. Fabricated metrics from AI bullet generators are a reputational and background-check risk (vendor test, D) [S25].
- **Effect of writing help.** Positive for non-generative assistance (RCT), negative for undifferentiated generative output (cover-letter study) [S20, S21].

### DF-4. Interview-prep platforms: GenAI system design versus legacy algorithms (Q3)

| Platform | What it offers | GenAI/ML system-design coverage | Price seen | Evidence | Caveat |
|---|---|---|---|---|---|
| Hello Interview | Guided system design, low-level design, ML system design, AI-enabled coding; AI "Live Practice"; crowd-sourced question pages | Yes: ML System Design track and AI Coding track listed (21 Oct 2026) | Premium $47 (1 month), $89 (1 year), $299 (lifetime) | B (pricing), C (value) | Human mocks no longer on the pricing page; a directory says they ended 31 May 2026 [S33] |
| Interviewing.io | Anonymous mocks with experienced engineers | Not verified | Per-session or program pricing (not captured) | C (Blind sentiment) | Cost; community says calibration is strong [S34] |
| Exponent (incl. Pramp) | Courses plus peer and coach mocks | Not verified | Free tier with limited peer sessions; paid plans (secondary) | C/D | Pramp reportedly absorbed [S34] |
| NeetCode | Algorithm roadmap and videos | Not applicable | Free plus Pro | D (recalled) | Algorithms only |
| LeetCode | Problem bank and contests | Not applicable | Free plus Premium | D (recalled) | Question tags reflect past, not current, loops |
| ByteByteGo | System-design books and courses, including a GenAI system-design title | Yes (title reported in secondary mentions) | Paid | D | Not verified in-session |
| Commodity PDFs and "guides" on creator marketplaces | Packaged interview Q&A | Claims vary | Low price | E | Unvetted; many appear AI-generated |

**Verdict.** For GenAI and ML system design, Hello Interview is the only platform where I could verify current scope and price from a primary page. No platform in this table has independent outcome evidence (Grade E), and the review ecosystem is affiliate-heavy. Algorithm practice remains the baseline because AI-permitted rounds are a minority and policy varies by employer (Meta piloted AI-assisted coding rounds; Amazon prohibits AI tools) [S30]. Choose by (a) coverage of your target company's actual loop, (b) fidelity of feedback, and (c) price and refund terms.

### DF-5. AI mock interviews versus live assistants (Q4)

**Mock practice.** Roundups list Google Interview Warmup (free, short question sets), Yoodli (speech analytics), Big Interview, and mock modes of several copilots [S34]. I found no independent study that AI mocks improve real interview outcomes (Grade E). Low-stakes rehearsal is still sensible: the risk is mostly data exposure from recorded audio or video. Beyz and Interviews by AI: searched; I found no independent evidence about either (Grade E).

**Live assistance risks.**

| Risk | Evidence | Grade |
|---|---|---|
| Disqualification or offer rescission | Amazon reportedly instructs recruiters to disqualify candidates found using AI tools [S30] | B |
| Detection arms race | Fabric flagged 38.5% of 19,368 AI-run interviews using 21+ behavioral signals and known tool signatures; its own materials reportedly claim a 3-5% false-positive rate; an independent critique notes the figures are Fabric's own and that 61% of flagged candidates still passed [S29] | C |
| In-person retreat | A Gartner figure (72.4% of recruiting leaders running some in-person interviews) is second-hand [S31]; secondary sources also say Google and McKinsey reinstated in-person rounds (not verified against primary reporting) | D |
| Product reliability | Final Round AI Trustpilot: 3.5/5, about 250 reviews; complaints include refund eligibility, access being blocked, and copilot slowness or hallucination [S32] | C |
| Data capture | Continuous audio and screen capture is inherent to the category; I could not retrieve Final Round AI's primary privacy policy | E |
| Integrity and legal exposure | Violates stated policies of employers that prohibit AI during interviews [S30]; severity depends on employer and jurisdiction | B |

**Where policy is explicit and permissive.** Meta's pilot and Anthropic's reversal show employers that allow disclosed AI use in some rounds [S30]. Two secondary aggregators contradict primary reporting (one lists Meta as generally prohibiting AI; Business Insider reports a pilot), which is why policy must be checked per employer, per round.

### DF-6. Compensation tools and private-company equity (Q5)

| Tool | Data source (as documented) | Freshness evidence | Private-equity support | Cost | Grade |
|---|---|---|---|---|---|
| Levels.fyi | Self-submitted offers and compensation; the vendor says submissions are verified; founder documents annualization rules [S36] | Continuous submissions, but cohorts mix new offers with current-employee realized value; Blind threads say some entries are years old [S36] | Submitter-chosen valuation; no standard basis | Free data; paid services | B/C |
| Comprehensive.io | Crawls legally posted salary ranges from career pages (2023 founder interview; site claims 5,000+ companies) [S38] | Daily-crawl claim dates from 2023; not re-verified | Only equity ranges that are posted | Free benchmarks | C |
| Carta | Cap-table and HRIS-derived startup data; a 2023 post describes a free candidate-facing data program [S38] | Program status for 2026 unverified | Scenario calculators; not validated vs outcomes | Free calculator; employer products paid | C/D |
| Employer-side platforms (Pave and similar) | Payroll and HRIS integrations | Vendor claims only | Employer-facing, not candidate-accessible | Employer-paid | D (not re-verified) |
| FairOffer | Searched; no authoritative result | n/a | n/a | n/a | E |

**Freshness vetting result.** All freshness claims found are vendor-stated; I found no independent audit of any salary database's recency. For Levels.fyi, the documented methodology is itself the freshness risk: new offers are annualized grants, existing-employee entries are realized value, so a figure can be a different quantity depending on submitter cohort.

**Equity.** No tool in the evidence validates private-company equity valuation against realized exits (accuracy Grade E). A defensible process asks the company for the numbers that drive value (fully diluted shares, strike price, the latest 409A common valuation, the last preferred price, and the liquidation-preference stack) and models scenarios, recognizing that dilution and preferences can make options worth far less than a headline paper value. These valuation concepts are recalled general knowledge (Grade D), not sourced here; this is not financial, tax or legal advice, and tax treatment of options should be checked with a qualified professional.

**Coaching services.**
- Levels.fyi sells flat-fee negotiation with a money-back guarantee; the guarantee thresholds differ across page versions I saw, so read current terms [S37].
- Rora charges a percentage of the increase and shows a high self-reported Trustpilot score [S37].
- Candor is described as success-fee based (vendor-sourced, not re-verified).
- One Trustpilot reviewer of Levels.fyi called the service useful but not exceptional [S37].

All outcome claims are self-reported (Grade D); there is selection and survivorship bias in every testimonial set.

**LLM advice.** A peer-reviewed study (GeBNLP 2025) found that LLMs recommend different salary asks for different personas given the same facts [S39]. It tested earlier model generations, so the size of the effect in late-2026 models is unknown.

### DF-7. Privacy, leakage and security (Q6)

| Item | When | What happened or what the policy says | Src | Grade | Lesson |
|---|---|---|---|---|---|
| McHire / Paradox.ai (McDonald's) | Disclosed July 2025 | Test admin account with a trivial default password plus an IDOR flaw exposed up to 64M applicant records; Paradox says five records were accessed, by the researchers, and fixed it | S41 | B | Employer-chosen platform; you cannot opt out. Keep chat answers minimal |
| LiveCareer | Found Mar 2025; reported Jul 2025 | More than 5.1M files (mostly resumes back to 2016) in an unsecured cloud container; not acknowledged at publication | S42 | B | Resume builders hold full resumes with PII |
| HireClick | Reported 2025 (dates vary across secondary sources) | About 5.7M files in a misconfigured bucket (one outlet's headline says 57M, which looks like a typo) | S42 | B/C | Storage misconfiguration is the common cause |
| TalentHook | Reported 2025 | About 26M resume files exposed | S42 | B/C | Same pattern |
| AiFrame extensions (LayerX) | Feb 2026 | 30+ fake "AI assistant" Chrome extensions, roughly 260-300k installs, loading remote content so behavior can change without a store update | S43 | B | Extension permissions equal credentials |
| Kickresume privacy policy | Read in-session | May train on strictly anonymised data, including documents users generate | S44 | C (not re-verified) | Read training clauses |
| BOLD-family terms | Watchdog review | Broad data-sharing language flagged | S27 | C | "Free" often means data-for-service |
| Final Round AI | n/a | Primary privacy policy not retrieved | n/a | E | Unknown handling of audio and screen |

**Control summary.** Upload by data tier (see 4.4 B). Offer letters and comp history are the highest-value items for identity and social-engineering abuse, so redact or withhold them from general-purpose and unknown tools. Prefer tools that state retention periods and offer deletion. Remove unused browser extensions.

### DF-8. Stage-by-stage notes

| Stage | Notes (evidence in brackets) |
|---|---|
| **1 Awareness** | Official data first: BLS OOH is revised every two years; O*NET's data-source list cites BLS 2024-34 projections and CareerOneStop updates through March 2026 [S51]. Both likely lag fast AI-driven shifts (inference). LLM chat advice shows documented bias: a 17-chatbot study found a pro-AI-career tilt, a NeurIPS-listed audit found gender bias in stream recommendations, and a benchmark rated LLM career advice poorly [S40]. |
| **2 Exploration** | O*NET interest profiler and occupation pages (A). ADPList for conversations (self-published statistics; counts differ across its own pages [S53]). roadmap.sh is recalled only (D). Personality-type products were not audited (gap). |
| **3 Skills** | Platform consolidation: Coursera and Udemy merged in May 2026, so expect catalog and pricing changes [S47]. Education-finance red flag: the CFPB's BloomTech order on income-share agreements and placement claims [S48]. Free curricula (freeCodeCamp, Hugging Face, Kaggle, DeepLearning.AI) are recalled (D). No ROI evidence for any MOOC found (E). |
| **4 Certifications** | Mixed: flat effect by count in Huntr's data; Foote Partners shows certified-skill premiums moving against non-certified across periods; a staffing firm lists in-demand IT certs [S16, S49]. Pick certs a target posting names; verify the issuer and proctoring. |
| **5 Portfolio** | Platform risk is real: Read.cv was acquired and wound down within months [S50]. Keep source in version control and publish from a domain you own. Do not publish secrets or private data. Evidence on portfolio impact is thin (D). |
| **6 Discovery** | Source conversion in Huntr's data (Google 7.12%, Wellfound 5.02%, Indeed 3.14%, LinkedIn 2.94%) is correlational [S16]. Scams: FTC losses from job scams rose from $90M (2020) to $501M (2024) [S45]. Ghost jobs: 93% of survey respondents applied to or suspected them [S16]. LinkedIn is the subject of a Texas AG investigation [S46]. Fake recruiters deliver malware via coding tests [S35]. |
| **7 Application** | ATS defenses (DF-1); autofill versus auto-submit (DF-2); resume tools (DF-3); billing and leak history of builders (KF7). Defenses at Workday were not searched (gap). |
| **8 Networking** | In Huntr's survey data, about 38% of interviews came via referrals, recruiters or networking (self-reported) [S16]. LinkedIn automation is prohibited [S15]. Mentor platforms carry self-published evidence only [S53]. Blind is an anonymous sentiment source [S34, S36]. |
| **9 Prep** | DF-4. Check each employer's AI policy before assuming algorithm-only or AI-allowed rounds [S30]. |
| **10 Execution** | DF-5. Sandbox recruiter code [S35]. Employer-initiated identity verification exists (CLEAR via Greenhouse) [S09]. Live copilots and overlays are Avoid. |
| **11 Negotiation** | DF-6. Offers can be withdrawn (18% in Huntr's Q1 2026 data); keep communications professional and get terms in writing before resigning (my advice; D) [S16]. |
| **12 Onboarding** | Mentoring (ADPList, MentorCruise) and anonymous community (Blind) are the only tools with any evidence. Submit ID, banking and tax data only through links verified via a known channel; employment-scam data are rising [S45]. Evidence specific to onboarding tools is thin (E). |

### DF-9. Falsification log

| Attempt to disprove | Result |
|---|---|
| Find documentation of a cross-employer shadow-ban for auto-apply users | None found. Two vendor statements point the other way (S05, S08). |
| Confirm that Simplify is autofill only | Partly contradicted: an auto-submit "Autopilot" beta is described in a competitor's account of Simplify's help center (S17). Premise updated. |
| Find an independent ATS-parser benchmark of resume builders | None found. Vendor benchmarks conflict (S25, S26). |
| Find FairOffer's current status | Not found. |
| Find Final Round AI's primary privacy policy | Not retrieved. |
| Find substantive Hacker News or Reddit threads on auto-apply bans | Only low-engagement Show HN threads with generic comments (S23). |
| Find Lever bot-detection documentation | None found; only repeat-application blocking (S11). |
| Find independent validation of private-equity valuation in comp tools | None found. |
| Find authoritative evidence on Interview Kickstart or similar high-ticket prep programs | None found; not catalogued. |
| Find independent evidence for Beyz or Interviews by AI | None found. |
| Reconcile source conflicts | Meta's AI-interview policy: an aggregator says generally prohibited, Business Insider reports a pilot, so I used Business Insider. Anthropic's policy: sources conflict between a ban and a reversal; I used the reversal report and flag it as time-sensitive. Hello Interview mock programs: the pricing page lists none, consistent with a third-party wind-down claim, whose price figures differ from the page. |
| Test the Huntr reading against another source | Direction matches recruiter surveys; causality unproven (S16, S19). |

---

## 7. Open Questions & Risks

### 7.1 Strongest objections an expert would raise, and what I found

| # | Objection | Evidence for the objection | Evidence against | Effect on conclusions |
|---|---|---|---|---|
| O1 | Vendor docs describe capability, not adoption; you cannot infer how many employers enable these defenses. | Greenhouse's blocklist is a beta, admin-configured feature; Ashby recommends the permissive level and gates application limits by plan; no adoption telemetry found [S01, S02, S07]. | Greenhouse and Ashby both describe their fraud features as products they actively market [S04, S09]. | Treat the risk as heterogeneous: some employers have strong defenses, many do not. |
| O2 | One GitHub issue about Playwright says nothing about extension-based autofill or cloud agents. | The report involves a browser-automation framework; the reporter's explanation is a hypothesis [S13]. | The same details passed from a normal browser; the error text mentions extensions and VPN/proxy, so some extension or network signals may matter [S13]. | I downgraded KF3 to B/C and separated inference from observation. |
| O3 | Huntr's conversion data is confounded: heavy appliers differ from light appliers, outcomes are self-reported, and Huntr sells tailoring tools. | Vendor-run, self-tracked, correlational [S16]. | Direction matches independent recruiter surveys [S19, S10]; the same-company decay is steep. No experiment randomizing volume was found. | Direction is credible; magnitude and causality are not established. |
| O4 | "Recruiters can spot AI text" and detection statistics are overconfident. | Fabric's 38.5% is vendor-sourced; an independent critique notes 61% of flagged candidates passed [S29]. | Employer policies (Amazon) and fraud features (Ashby, Greenhouse) show real enforcement intent [S03, S05, S30]. | Treat detection figures as directional; the policy risk stands regardless of accuracy. |
| O5 | Competitor blogs (Scoutify, LoopCV, Resumly, JobWizard, FastApply, atsverification.com) supply many tool facts. | True: several tool facts rest on them [S17, S18, S24, S25]. | I used them for pointers and for claims checkable against primary sources, graded them C/D, and rated Scoutify's own product Caution on the same rubric. | Tool-level claims are weaker than mechanism-level claims. |
| O6 | The rubric is subjective. | Scores are analyst judgments. | Anchors and hard disqualifiers reduce but do not remove subjectivity. | Boundary cases (total 8-9) can flip: Levels.fyi database (9, Recommended), Simplify Copilot, Teal, Jobscan, Kickresume, Comprehensive.io (8, Viable). |
| O7 | You tested nothing. | Correct: no hands-on testing and no controlled submissions. | A decisive test design is given in DF-1. | Q1 is verified documentarily, not empirically (see 7.4). |
| O8 | Features and prices change quickly (Simplify Autopilot is a beta). | True. | Re-audit triggers are listed in 4.5. | Re-check before acting. |
| O9 | Several catalog entries are recalled, not verified. | roadmap.sh, freeCodeCamp, LeetCode, GitHub, Hugging Face/Kaggle, ByteByteGo and Yoodli/Big Interview are Grade D. | They are flagged D in the catalog and cannot reach Recommended. | No conclusion depends on them. |
| O10 | The evidence is US-centric. | Most sources are US vendors, regulators and surveys. | Mechanism-level findings (ATS controls) are global product behavior; legal and market findings are not. | Re-check local boards, laws and price points before applying outside the US. |

### 7.2 Open questions

1. Do extension-based autofill tools trip Ashby or Greenhouse scoring? (Test on a board you control.)
2. What bot defenses does Lever document, if any, and what does Workday (the second-largest ATS in Huntr's sample) document?
3. How widely are Greenhouse's blocklist and fraud features and Ashby's strict spam level actually enabled?
4. Do hosted agents' data-center IPs receive high-risk flags at scale, and with what effect on outcomes?
5. Do AI mock interviews improve real interview outcomes? (No randomized or controlled study found.)
6. How well do comp databases' private-company equity figures match realized exit outcomes?
7. What do Final Round AI and similar tools retain from audio and screen capture?
8. Does Simplify Autopilot change conversion or flag rates compared with Copilot autofill?
9. How do the findings change in non-US markets? (The EU's digital omnibus is reported to push high-risk employment-AI obligations to 2 December 2027; that is law-firm commentary and I did not check the Official Journal text [S52].)
10. Is Carta's candidate-facing data program still running, and does FairOffer exist in 2026?

### 7.3 Risks of acting on this audit

- Terms and enforcement can change faster than this audit (LinkedIn, Ashby, Greenhouse, Lever).
- "Viable" means usable with controls and thin evidence, not validated. Do not read it as endorsement.
- The operating rules assume a typical employer; each employer's stated policy overrides them (especially on AI use in interviews).
- Some tools may have changed since I read them; treat prices as indicative.
- Nothing here is financial, tax or legal advice. Option exercise, tax and contract questions need a qualified professional.

### 7.4 DONE-criteria status

| Criterion | Status | Notes |
|---|---|---|
| At least 35 tools audited and mapped across the 12 stages | **Met** | 64 catalog entries; each stage has at least 3 (see section 10). |
| Technical risks and shadow-ban mechanisms empirically verified | **Partly met** | Verified against vendor documentation and one incident report; no controlled test was run (stated limit). |
| Resume tools evaluated against modern parser benchmarks | **Not met in the strict sense** | No independent benchmark exists in what I found; vendor benchmarks are summarized and graded D. |
| Negotiation platforms and salary databases vetted for freshness | **Partly met** | Methodology and cohort mixing documented for Levels.fyi; other freshness claims are vendor-stated; no independent audit found. |
| Objective recommendation criteria codified | **Met** | Section 4.2. |

### 7.5 Disclosure

This audit was written by an LLM assistant (Claude, made by Anthropic). General-purpose LLM assistants appear in the catalog; their ratings rest on third-party research (S20, S21, S39, S40), not on self-assessment. I did not use any product-specific Anthropic facts beyond naming it as one LLM assistant.

---

## 8. Delta (belief change)

| Item | Prior (recalled) | Evidence found | Posterior | Direction |
|---|---|---|---|---|
| P1a. Bot or spam defenses exist at Ashby and Greenhouse and can reject automated browsers | 0.80 | Documented controls at both; one reproducible Ashby rejection [S01, S05-S07, S13] | 0.95 | Up |
| P1b. A persistent cross-employer shadow-ban of auto-apply users is documented | 0.15 | Explicit non-sharing statements; Ashby rejection is visible; nothing found [S05, S08, S13] | 0.03 | Down |
| P1c. Silent *local* (employer-level) rejection exists (new) | about 0.30 | Greenhouse blocklist default; Ashby default message; Greenhouse filter option [S02, S05, S07] | 0.90 | Up |
| P2a. ATS auto-reject-by-parsing is mostly a myth | 0.70 | Knockout questions reject; Greenhouse scores but does not auto-reject; Workday AI screening is alleged, not proven [S08, S16, S28] | 0.70 | Unchanged, with refinements |
| P2b. Consumer "ATS scores" are unvalidated | 0.80 | No independent benchmark; internal-score admission [S25, S26] | 0.90 | Up |
| P3a. Mass auto-apply converts worse than targeted applying | 0.75 | Huntr; recruiter surveys; correlational [S16, S19] | 0.85 | Up |
| P3b. "Simplify auto-apply" is only autofill | 0.60 | Autopilot beta described by a competitor [S17] | 0.35 | Down |
| P4a. Live undisclosed copilots are net-negative | 0.85 | Employer policies; complaints; detection stats are vendor-sourced [S29, S30, S32] | 0.90 | Up (detection accuracy remains uncertain) |
| P4b. AI mock interviews have validated outcomes | 0.30 | No independent study found | 0.30 | Unchanged |
| P5a. Levels.fyi is the strongest public comp source for big tech | 0.70 | Method documented; cohort mixing and variance noted [S36] | 0.70 | Unchanged, with caveats |
| P5b. No tool values private equity reliably | 0.85 | No validation found | 0.90 | Up |
| P5c. Resume-builder billing and data-exposure risk is material | 0.70 | BOLD-family pattern; LiveCareer, HireClick, TalentHook exposures [S27, S42] | 0.85 | Up |

**Surprises (not in the priors).**
- Greenhouse's reCAPTCHA plus email-code step is documented, and Ashby's error text advises pausing extensions [S06, S13].
- IPQS, the reputation vendor Greenhouse uses, markets its own cross-customer threat network even though Greenhouse flags are customer-specific [S05, S14].
- Older vendor posts say Greenhouse does not score resumes; Greenhouse now has AI match scores (assistive, opt-out) [S08].
- Coursera and Udemy completed their merger in May 2026 [S47].
- Hello Interview's current pricing page lists no human mock programs [S33].
- A Texas AG investigation of LinkedIn was reported in July 2026 [S46].
- Sonara was reportedly relaunched under BOLD, the owner of the billing-pattern brands (competitor sources) [S24, S27].
- Huntr's same-company decay (6.07% to 1.91%) is steeper than I expected [S16].

---

## 9. Sources & Evidence Ledger

Retrieved or read on 21 Oct 2026 unless noted. Grade is for the specific claims the source supports. "Not re-verified" means the source was read earlier in the session but its URL could not be re-confirmed at write time, so I cite publisher and title only.

| ID | Source | Locator | Type | Grade | Supports / caveats |
|---|---|---|---|---|---|
| S01 | Ashby Knowledge Base, "Job Board: Application Spam Protection" | https://docs.ashbyhq.com/job-board-application-spam-protection | Vendor docs | A | Four protection levels; strict can reject real candidates |
| S02 | Ashby Knowledge Base, "Application Limits" | https://docs.ashbyhq.com/application-limits | Vendor docs | A | Email-keyed throttle and repeat rules; candidate sees employer message or default text; admin-visible blocked list; plan-gated; excludes Indeed applications |
| S03 | Ashby Knowledge Base, "Candidate Fraud Detection Overview & Admin Settings" | https://docs.ashbyhq.com/candidate-fraud-detection | Vendor docs | A | Device, IP, email, phone signals at submission; flags for review |
| S04 | Ashby blog, "Ashby Launches the First ATS-Integrated Fraud Detection System"; Ashby product update on fraudulent-candidate detection | https://ashbyhq.com/blog/all/ashby-launches-the-first-ats-integrated-fraud-detection-system ; https://www.ashbyhq.com/product-updates/introducing-fraudulent-candidate-detection-and-management-to-help-you-focus-on-legitimate-candidates | Vendor | A (behavior); D (marketing claims) | Signals rather than verdicts; flagged versus unflagged review buckets |
| S05 | Greenhouse Support, "Fraud Detection and Spam Blocklist - Security & Privacy FAQ" (updated 13 Jan 2026) | https://support.greenhouse.io/hc/en-us/articles/45397259312027-Fraud-Detection-and-Spam-Blocklist-Security-Privacy-FAQ | Vendor docs | A | IPQS signals; data-center IP high risk; no auto-reject; recruiter filter; flags not shared across customers; blocklist runs before fraud checks |
| S06 | Greenhouse Support, reCAPTCHA / spam-protection article | https://support.greenhouse.io/hc/en-us/articles/115005448066 | Vendor docs | A | Invisible reCAPTCHA behavior analysis; email-code step; per-board sensitivity |
| S07 | Greenhouse Support, "Block IP addresses and email domains" | https://support.greenhouse.io/hc/en-us/articles/41595563125787-Block-IP-addresses-and-email-domains | Vendor docs | A | Admin blocklist (beta); auto-reject reason; no rejection email by default; Gmail/Yahoo cannot be blocked |
| S08 | Greenhouse Support, "MyGreenhouse FAQ for Candidates" (updated 2 Oct 2026) | https://support.greenhouse.io/hc/en-us/articles/43418495049499-MyGreenhouse-FAQ-for-Candidates | Vendor docs | A | No cross-employer sharing; Talent Matching score assistive, no auto-reject; opt-out |
| S09 | Greenhouse blog, "Introducing Greenhouse Real Talent with CLEAR"; CLEAR and Greenhouse press release (Jun 2025) | https://www.greenhouse.com/blog/introducing-greenhouse-real-talent ; https://ir.clearme.com/news-events/press-releases/detail/151/clear-and-greenhouse-announce-partnership-to-enable | Vendor | A (existence); D (efficacy claims) | Bot, fake-applicant and mass-application detection claims; optional ID verification |
| S10 | Greenhouse newsroom, "Greenhouse Launches New Tools to Tame Chaotic Hiring Funnels" | https://www.greenhouse.com/uk/newsroom/greenhouse-launches-new-tools-to-tame-chaotic-hiring-funnels | Vendor press | C | 3x applications per recruiter since 2022 (vendor statistic) |
| S11 | Lever Help, "Blocking repeat applications" | https://help.lever.co/hc/en-us/articles/20087458260893 | Vendor docs | A | Email plus job-site source tag; per posting; time window |
| S12 | Recruitee, "Set application limits"; HR Partner, "Recent improvements to Recruitment"; Haley Marketing, "Career Portal Anti-Spam Checks" | https://support.recruitee.com/en/articles/14106673-set-application-limits ; https://workplace.hrpartner.io/recent-improvements-to-recruitment/ ; https://helpme.haleymarketing.com/hc/en-us/articles/50515600603028-Career-Portal-Anti-Spam-Checks | Vendor docs | A | Email/phone-keyed limits (Recruitee ignores plus-aliases); CAPTCHA, honeypots, disposable-email blocks, speed guards |
| S13 | GitHub issue career-ops-hq/career-ops #4269 | https://github.com/career-ops-hq/career-ops/issues/4269 | Community bug report | C | Automated-browser rejection on Ashby; mechanism hypothesized; open date taken from a vendor blog |
| S14 | IPQS Privacy Policy; IPQS infographic PDF on detecting fake users and duplicate accounts | Publisher and title (ipqualityscore.com, ipqs.com); URL not re-verified | Vendor | A (policy text); D (marketing) | Cross-customer threat-network claims; limited consortium sharing from feedback forms |
| S15 | LinkedIn Help, "Prohibited software and extensions"; "Automated activity on LinkedIn" | https://www.linkedin.com/help/linkedin/answer/a1341387 ; https://www.linkedin.com/help/linkedin/answer/90586 | Platform terms | A | Automation prohibited; restriction; may lift after disabling software |
| S16 | Huntr, "Job Search Trends Q1 2026" (published 19 Oct 2026) | https://huntr.co/research/job-search-trends-q1-2026 | Vendor research | C | Volume and same-company conversion; source conversion; ATS share; ghost-job and scam survey; offer withdrawals; networking share; certification effect. Vendor-run, self-tracked, correlational |
| S17 | Scoutify blog, "Does auto-apply work"; "Scoutify vs Simplify" | https://scoutify.com/blog/does-auto-apply-work/ ; https://scoutify.com/blog/scoutify-vs-simplify/ | Competitor blog | C/D (COI) | Simplify Autopilot description; summary of Huntr data; Scoutify pricing |
| S18 | FastApply blog, "AI job application bots: which actually submit (2026)"; HRLens, "AI auto-apply bots for jobs" | https://blog.fastapply.co/ai-job-application-bots-which-actually-submit-2026 ; https://www.hrlens.io/articles/ai-auto-apply-bots-for-jobs | Vendor blogs | D (COI) | Test claims on eight bots |
| S19 | Hiration, "AI auto-apply bots" (reporting a Robert Half survey, Mar 2026) | https://www.hiration.com/blog/ai-auto-apply-bots/ | Secondary | C | 67% and 65% hiring-manager statistics, second-hand |
| S20 | Wiles, Munyikwa and Horton, Management Science (2025); NBER working paper w30886 | https://doi.org/10.1287/mnsc.2024.04528 ; https://www.nber.org/papers/w30886 | Peer-reviewed RCT | A | +8% hires, +10% wages with non-generative writing assistance |
| S21 | "Signaling in the Age of AI: Evidence from Cover Letters", arXiv:2509.25054 (authors not captured) | https://arxiv.org/abs/2509.25054 | Preprint | B | Cover-letter signal erosion after an AI tool launch; tailoring predicts callbacks |
| S22 | LazyApply: Trustpilot; Resumly, "LazyApply review"; LoopCV, "LazyApply review" | https://ca.trustpilot.com/review/lazyapply.com?page=3 ; https://resumly.ai/answers/lazyapply-review ; https://blog.loopcv.pro/lazyapply-review/ | Review site plus competitor blogs | C | About 2.4/5 on about 107 reviews; complaint themes; pricing conflict |
| S23 | Hacker News, Show HN thread on an auto-apply bot | https://news.ycombinator.com/item?id=47832631 | Community | D | Low engagement; cloud-browser claim |
| S24 | Sonara coverage: LoopCV, "What happened to Sonara"; Resumly, "What happened to Sonara AI"; Scoutify, "Sonara review" | Publisher and title; URLs not re-verified | Competitor blogs | D (COI) | Shutdown 1 Feb 2024; relaunch under BOLD; one user suspension and refund anecdote |
| S25 | atsverification.com, "ATS parsing benchmark 2026" and "AI resume builders tested 2026" | https://atsverification.com/blog/ai-resume-builders-tested-2026/ (first title: URL not re-verified) | Vendor | D (COI) | Parser-test claims using its own "ATS-style parser" |
| S26 | Dupple, "Best AI for resumes"; Fast.io, "Best AI resume builders 2026"; Resume Genius, "Best free resume maker" | https://dupple.com/learn/best-ai-for-resumes ; https://fast.io/resources/best-ai-resume-builders-2026/ ; https://resumegenius.com/faq/what-is-the-best-free-resume-maker | Affiliate and vendor roundups | D (COI) | Prices; internal-score admission; self-ranking |
| S27 | BOLD-family billing and data: ResumeCoach (Zety review); ResumeOptimizerPro (MyPerfectResume); Unstar app-review analysis; Trustpilot (Zety); Sikayetvar complaint; Resufit; terms.law "ToS Watchdog: Zety" | https://www.resumecoach.com/reviews/zety-resume-builder-review/ ; https://resumeoptimizerpro.com/blog/is-myperfectresume-legit ; https://unstar.app/blog/resume-io-zety-canva-indeed-novoresume-resume-builder-apps-ranked-2026 ; https://www.trustpilot.com/review/zety.com?page=7 ; https://www.sikayetvar.com/en/zety-us/zety-charged-me-without-consent-how-can-i-dispute-and-recover-money-q-36444 ; https://resufit.com/blog/myperfectresume-review-is-it-worth-the-cost-a-pricing-value-analysis/index.md ; https://terms.law/ToS-Watchdog/resume-builders/zety/ | Mixed; several are competitors | C | Trial-to-recurring pattern; cancellation complaints; BBB reference second-hand; data-sharing note |
| S28 | Mobley v. Workday: Akin AI Law and Regulation Tracker; Holland and Knight (May 2025) | https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/court-allows-discrimination-claims-against-ai-hiring-tool-to-proceed-or-mobley-v-workday-inc ; https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged | Law-firm analysis of court rulings | A/B | Collective conditionally certified May 2025; discovery as of spring 2026; allegations unproven |
| S29 | Fabric, "State of AI Interview Cheating in 2026"; SocialTalent, "Fabric's Cheating Data Argues Against the Interview It Sells" | https://www.fabrichq.ai/blogs/state-of-ai-interview-cheating-in-2026-insights-from-19-368-interviews ; https://www.socialtalent.com/?p=96408 | Vendor report plus independent critique | C | 38.5% flagged; thresholds; critique that 61% of flagged candidates passed |
| S30 | Business Insider via AOL, "Meta will let some job candidates use AI in their coding interviews"; GeekWire (2025); Coderbyte; DataDriven | https://www.aol.com/meta-let-job-candidates-ai-160303820.html ; https://www.geekwire.com/2025/is-it-cheating-ai-use-during-job-interviews-sparks-debate-over-whether-to-restrict-emerging-tools/ ; https://coderbyte.com/blog/6-pros-and-cons-of-letting-candidates-use-ai-during-your-coding-interview ; https://datadriven.io/blog/ai-in-data-engineer-interviews-the-2026-policy-divide | Journalism plus vendor blogs | B/C | Amazon, Meta and Anthropic policies; policy divergence |
| S31 | Hedy.ai, "Is using AI in job interviews cheating?" (second-hand Gartner figure) | https://hedy.ai/post/is-using-ai-in-job-interviews-cheating/ | Vendor blog | D | 72.4% in-person claim, second-hand |
| S32 | Trustpilot, Final Round AI | https://www.trustpilot.com/review/finalroundai.com | Review site | C | 3.5/5 on about 250 reviews; complaint themes |
| S33 | Hello Interview pricing page (fetched 21 Oct 2026); techinterview.org directory entry | https://hellointerview.com/pricing ; https://www.techinterview.org/bootcamp_directory/p/hello-interview/ | Vendor page plus secondary directory | A (pricing); D (wind-down claim) | Premium prices and tracks; no human mock pricing listed |
| S34 | Lodely, "interviewing.io pricing"; Blind threads on mock-interview sites and Interviewing.io; Fast.io, "Best AI interview prep tools 2026" | https://www.lodely.com/blog/interviewing-io-pricing ; https://www.teamblind.com/post/mock-interview-websites-comparision-qwggejy1 ; https://www.teamblind.com/post/what-do-people-think-of-interviewingio-j3bnmqj5 ; https://fast.io/resources/best-ai-interview-prep-tools-2026/ | Community plus affiliate | C/D | Sentiment; tool lists |
| S35 | Microsoft Security Blog on Contagious Interview; eSecurityPlanet (338 npm packages); LastPass, "Job fraud playbook" | https://www.microsoft.com/en-us/security/blog/?p=145718 ; https://www.esecurityplanet.com/news/338-malicious-npm-packages-linked-to-north-korean-hackers/ ; https://blog.lastpass.com/posts/job-fraud-playbook | Vendor security research plus trade press | B | Campaign active since at least Dec 2022; fake recruiters and coding tests; package counts |
| S36 | Levels.fyi community threads (founder explanation of total-comp calculation; RSU conventions); Blind threads on RSU valuation | https://www.levels.fyi/community/thread/pqqSpb/how-is-total-compensation-calculated ; https://www.levels.fyi/community/thread/xEqjXM/how-do-most-people-calculate-rsu-comp ; https://www.teamblind.com/post/what-is-your-method-for-calculating-rsu-value-h1irunoi ; https://www.teamblind.com/post/rsu-on-levelsfyi-rgqst2jp | Vendor community plus community | B/C | Annualization rules; variance; cohort mixing |
| S37 | Levels.fyi Services; Trustpilot (Levels.fyi); Rora; Tech Interview Handbook negotiation guide | https://www.levels.fyi/services/ ; https://se.trustpilot.com/review/levels.fyi ; https://teamrora.com/ ; https://techinterviewhandbook.org/negotiation | Vendor pages, review site, guide | C/D | Pricing models; guarantee terms vary by page version; reviews |
| S38 | Carta Insights, free startup salary and equity data (Nov 2023); Pragmatic Engineer on Comprehensive.io and Levels.fyi Jobs; HR Dive pay-transparency coverage | https://carta.com/data/linkedin-free-startup-salary-equity-data/ ; https://newsletter.pragmaticengineer.com/p/behind-the-scenes-with-two-new-salary ; https://hrdive.com/news/pay-transparency-tracker-California-NYC/640103 | Vendor plus trade press | C | Candidate-facing data program (2023); posted-range approach |
| S39 | "Surface Fairness, Deep Bias", GeBNLP 2025 (ACL Anthology 2025.gebnlp-1.20; arXiv:2506.10491) | https://arxiv.org/abs/2506.10491 | Peer-reviewed workshop paper | A/B | Persona-dependent salary advice from LLMs |
| S40 | LLM career-advice studies: Unite.ai coverage of a 17-chatbot study; NeurIPS 2026 virtual page; AIES paper; Renaissance Philanthropy on CareerNet | https://www.unite.ai/cs/chatbots-push-ai-careers-and-stocks-more-than-humans-do ; https://neurips.cc/virtual/2026/162727 ; https://ojs.aaai.org/index.php/AIES/article/download/43346/50906/47452 ; https://renaissancephilanthropy.org/insights/can-ai-give-reliable-career-advice-evaluating-llms-using-careernet | Papers plus coverage | B | Bias and weak benchmark performance in career advice |
| S41 | McHire / Paradox.ai: CSO Online; Communications of the ACM | https://www.csoonline.com/article/4020919/mcdonalds-ai-hiring-tools-password-123456-exposes-data-of-64m-applicants.html ; https://cacm.acm.org/?p=772435 | Trade press | B | Default password plus IDOR; up to 64M records; Paradox response |
| S42 | Resume-platform exposures: SC Media (LiveCareer; HireClick); teiss (LiveCareer; HireClick; TalentHook); TechRadar (TalentHook) | https://www.scworld.com/brief/over-5m-job-seekers-data-accidentally-exposed-by-livecareer ; https://www.teiss.co.uk/news/data-breach-exposes-over-5-million-resumes-on-popular-job-platform-livecareer-16061 ; https://www.scworld.com/brief/misconfigured-hireclick-storage-bucket-exposes-over-5-7m-files ; https://www.techradar.com/pro/security/over-26-million-resumes-exposed-in-top-cv-maker-data-breach-heres-what-we-know | Trade press citing security-researcher findings | B | 5.1M, 5.7M and about 26M files; a teiss headline on HireClick says 57M, likely a typo |
| S43 | LayerX "AiFrame" campaign: BleepingComputer; Dark Reading; Guardio threat-category audit | https://bleepingcomputer.com/news/security/fake-ai-chrome-extensions-with-300k-users-steal-credentials-emails ; https://www.darkreading.com/cyber-risk/chrome-fake-ai-browser-extensions ; https://guard.io/blog/malicious-browser-extensions-2026-threat-categories-audit | Security research plus trade press | B | 30+ fake AI extensions; about 260-300k installs; remote content |
| S44 | Kickresume Privacy Policy | Publisher and title (kickresume.com); URL not re-verified | Vendor policy | A (text); C (not re-verified) | May train on anonymised user documents |
| S45 | FTC, Consumer Sentinel 2024 press release | https://www.ftc.gov/node/87602 | Regulator | A | Job and employment-agency scam losses $90M (2020) to $501M (2024) |
| S46 | Staffing Industry Analysts and ClearanceJobs on the Texas AG investigation of LinkedIn; Engadget on LinkedIn Job Match | https://www.staffingindustry.com/news/global-daily-news/linkedin-investigated-over-listings-for-ghost-jobs ; https://news.clearancejobs.com/2026/07/30/texas-ag-launched-investigation-of-linkedin-over-premium-subscriptions/ ; https://www.engadget.com/social-media/linkedin-wants-you-to-apply-for-fewer-jobs-140049139.html | Trade press | B | Investigation reported July 2026 (allegations); Premium price; Job Match |
| S47 | Coursera and Udemy merger: Business Wire (17 Dec 2025); Las Vegas Sun reprint of Coursera Q2 2026 results; Let's Data Science | https://www.businesswire.com/news/home/20251217155893/en/Coursera-to-Combine-with-Udemy-to-Empower-the-Global-Workforce-with-Skills-for-the-AI-Era ; https://lasvegassun.com/news/2026/jul/29/coursera-reports-second-quarter-2026-financial-res/ ; https://letsdatascience.com/news/coursera-and-udemy-complete-25b-merger-creating-skills-platf-f913e24a | Press release plus trade | A/B | Announced Dec 2025; completed May 2026 |
| S48 | CFPB enforcement action, Bloom Institute of Technology; TechCrunch (17 Apr 2024); techinterview.org, "BloomTech: what happened" | https://consumerfinance.gov/enforcement/actions/bloom-institute-of-technology ; https://techcrunch.com/2024/04/17/consumer-financial-protection-bureau-fines-bloomtech-for-false-claims ; https://www.techinterview.org/post/3233477749/bloomtech-what-happened/ | Regulator plus press | A | Order April 2024; closure reported (secondary) |
| S49 | Certification evidence: Ironhack; Data Center Knowledge (Foote Partners); Robert Half | https://www.ironhack.com/us/blog/tech-certifications-worth-getting-in-2026-and-how-to-actually-use-them ; https://www.datacenterknowledge.com/training-certifications/certifications-boost-it-pro-job-prospects-salaries ; https://www.roberthalf.com/us/en/insights/career-development/which-it-certifications-are-most-valuable | Bootcamp blog (COI), trade press, staffing firm | C | Mixed premiums; in-demand certifications |
| S50 | TechCrunch, "Perplexity acquires Read.cv" (17 Jan 2025) | https://techcrunch.com/2025/01/17/perplexity-acquires-read-cv-a-social-media-platform-for-professionals/ | Press | A/B | Acquisition; export deadline 16 May 2025 |
| S51 | O*NET OnLine data-source page; BLS Occupational Outlook Handbook FAQs | https://www.onetonline.org/help/online/datasources ; https://www.bls.gov/ooh/about/OOH-FAQs.htm | Official | A | Source dates; OOH revision cadence |
| S52 | EU AI Act digital omnibus: Sidley Data Matters (22 Jun 2026); Cuatrecasas | https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ ; https://www.cuatrecasas.com/en/spain/labor-and-employment/art/digital-omnibus-on-ai-how-does-it-impact-employment-relations | Law-firm commentary | B | Delay of high-risk (employment) obligations, reported to 2 Dec 2027; not checked against the Official Journal |
| S53 | ADPList guides and state-of-mentorship pages; MentorCruise comparisons | https://adplist.org/guides/best-mentorship-platforms ; https://adplist.org/state-of-mentorship | Vendor self-published | C/D | Self-published statistics; inconsistent counts |
| S54 | Workable Help, "Managing AI generated and automated job applications"; Teamtailor Support, "Spam candidate filter" | Publisher and title; URLs not re-verified | Vendor docs | A (not re-verified) | WAF, IP reputation, rate limiting and CAPTCHA; spam-domain and speed filters |

---

## 10. Complete 12-Stage Tool Catalog

How to read: **Stage(s)** lists the primary stage first. **Pricing** is as reported by the cited source and may have changed; verify before paying. **Grade** is the evidence grade for the claims that determine the status. **E1-E6** are the rubric scores from 4.2 and the total is their sum. **Status** follows the rules in 4.2, including the hard disqualifiers (D1-D4). Grade D rows are recalled or weakly sourced and cannot reach Recommended.

**Catalog summary.** 64 tools: 4 Recommended, 39 Viable, 15 Caution, 6 Avoid. Evidence grades: 8 A, 8 B, 26 C, 20 D, 2 E. Tools per stage (a tool listed under several stages counts in each): 1 Awareness 4; 2 Exploration 6; 3 Skills 5; 4 Certifications 4; 5 Portfolio 4; 6 Discovery 8; 7 Application 21; 8 Networking 6; 9 Prep 11; 10 Execution 4; 11 Negotiation 9; 12 Onboarding 3. Statuses were recomputed mechanically from the E1-E6 scores and the disqualifier list (D1: row 10; D2: rows 36, 41; D3: rows 54, 55; D4: row 16), with no mismatches. Only four tools reach Recommended because the rubric requires independent evidence, which most of this category lacks.

| # | Tool | Category | Stage(s) | Pricing model (reported; verify) | Grade | E1/E2/E3/E4/E5/E6 = total | Status | Basis |
|---|---|---|---|---|---|---|---|---|
| 1 | BLS Occupational Outlook Handbook | Official occupational data | 1, 2 | Free | A | 2/2/2/2/2/2 = 12 | Recommended | Official; revised every two years; may lag fast AI-driven shifts [S51] |
| 2 | O*NET OnLine / My Next Move | Official occupation database and interest profiler | 1, 2 | Free | A | 2/2/2/2/2/2 = 12 | Recommended | Data sources cite BLS 2024-34 projections and CareerOneStop updates through Mar 2026 [S51] |
| 3 | Huntr Job Search Trends reports | Vendor labor-market research | 1, 6 | Free | C | 1/2/2/2/2/0 = 9 | Viable | Large self-tracked dataset; vendor-only evidence keeps it below Recommended [S16] |
| 4 | General LLM assistants as career or salary advisor (ChatGPT, Claude, Gemini and similar) | LLM assistant (advisory use) | 1, 2, 11 | Freemium plus subscription tiers (not audited here) | B | 0/1/2/1/2/2 = 8 | Caution | E1=0: documented bias and instability in advisory use [S39, S40] |
| 5 | General LLM assistants for drafting and rehearsal (human-verified) | LLM assistant (drafting) | 2, 7, 9 | Freemium plus subscription tiers (not audited here) | B | 1/1/1/1/2/1 = 7 | Viable | Non-generative writing aid helped in an RCT; generic generative text is discounted; verify every claim [S20, S21] |
| 6 | roadmap.sh | Role roadmaps (open source) | 2, 3 | Free | D | 1/2/2/2/2/0 = 9 | Viable | Recalled; not verified in-session |
| 7 | Coursera (incl. Udemy after merger) | MOOC and credential marketplace | 3, 4 | Subscription or per course (not audited) | B | 1/1/2/1/1/1 = 7 | Viable | Merger completed May 2026; catalog and pricing may shift; no ROI evidence found [S47] |
| 8 | freeCodeCamp | Free coding curriculum | 3, 5 | Free (nonprofit) | D | 1/2/2/2/2/0 = 9 | Viable | Recalled; not verified in-session |
| 9 | Hugging Face Learn / DeepLearning.AI short courses / Kaggle Learn | Free AI/ML courses | 3 | Free | D | 1/1/2/2/2/0 = 8 | Viable | Recalled; not verified in-session |
| 10 | Income-share-agreement bootcamps (BloomTech/Lambda School model) | Paid bootcamp with ISA | 3 | ISA or tuition | A | 0/1/1/0/0/2 = 4 | Avoid | D1: CFPB order Apr 2024; closure reported [S48] |
| 11 | Vendor cloud certifications (AWS, Azure, Google Cloud) | Certification | 4 | Exam fee plus renewal | C | 1/1/2/1/2/1 = 8 | Viable | Interview-rate effect flat by count in Huntr data; premiums mixed [S16, S49] |
| 12 | CompTIA entry certifications (Security+, Cloud+ and similar) | Certification | 4 | Exam fee | C | 1/1/2/1/2/1 = 8 | Viable | Listed as in-demand by a staffing firm; no outcome study [S49] |
| 13 | Unaccredited "AI certification" badges | Certificate or badge | 4 | Varies | D | 0/1/1/1/1/0 = 4 | Caution | E1=0: no credible employer signal found; check the issuer [S49] |
| 14 | GitHub profile plus Pages | Code hosting and portfolio | 5 | Free plus paid tiers | D | 1/1/2/2/2/0 = 8 | Viable | Recalled; keep source exportable, use your own domain, never commit secrets |
| 15 | Hugging Face Spaces / Kaggle notebooks | ML demo and notebook hosting | 5 | Free plus paid tiers | D | 1/1/2/2/2/0 = 8 | Viable | Recalled; not verified in-session |
| 16 | Read.cv | Professional profile and portfolio | 5 | Was free | A | 0/1/2/2/0/2 = 7 | Avoid | D4: acquired Jan 2025; export deadline 16 May 2025 [S50] |
| 17 | Google Jobs and direct employer career pages | Aggregator to direct apply | 6, 7 | Free | C | 1/1/2/2/2/0 = 8 | Viable | Highest source conversion in Huntr data (7.12%; correlational) [S16] |
| 18 | LinkedIn Jobs and networking (free tier, manual use) | Job board and social network | 6, 8 | Free | C | 1/1/2/1/2/1 = 8 | Viable | Large reach; low conversion in Huntr data (2.94%); Texas AG probe reported [S16, S46] |
| 19 | LinkedIn Premium Career | Subscription add-on | 6, 8 | Paid monthly (about $39.99 reported) | C | 1/1/2/0/2/1 = 7 | Caution | E4=0: state AG investigation concerning Premium marketing (allegation); no independent evidence of benefit found [S46] |
| 20 | Wellfound | Startup job board | 6 | Free for candidates | C | 1/1/2/2/2/0 = 8 | Viable | Huntr conversion 5.02% [S16] |
| 21 | Indeed / Glassdoor / Handshake | General and campus boards | 6 | Free | C | 1/1/2/1/2/0 = 7 | Viable | Huntr conversion about 3.1-3.4%; Ashby limits exclude Indeed applications [S16, S02] |
| 22 | Jobright.ai | AI job matching and agent | 6, 7 | Freemium plus subscription (not verified) | D | 1/1/1/1/1/0 = 5 | Caution | Evidence from competitor posts only [S17] |
| 23 | Scoutify (alerts and "Sniper") | Alerts plus career-site auto-apply | 6, 7 | About $5 / $15 / $25 per week (vendor-stated) | D | 1/1/1/1/1/0 = 5 | Caution | COI disclosure: I relied on its blog for other tools; rated on the same rubric [S17] |
| 24 | Simplify Copilot | Autofill browser extension | 7 | Free; Simplify+ paid (about $19.99 per week reported by a competitor) | C | 1/1/2/1/2/1 = 8 | Viable | Autofill with a human clicking submit [S17] |
| 25 | Simplify Autopilot (beta) | Auto-submit agent | 7 | Simplify+ credits (about 20 per week per a competitor) | D | 1/1/1/1/1/0 = 5 | Caution | Beta; no review step per competitor; no outcome evidence [S17] |
| 26 | Huntr (tracker and clipper) | Application tracker | 7 | Freemium (paid tier not verified) | C | 1/1/2/2/2/0 = 8 | Viable | Free tier; vendor-only evidence [S16] |
| 27 | Teal | Tracker plus resume builder | 7 | Free; Teal+ about $9 per week or $29 per month (roundups) | C | 1/1/2/1/2/1 = 8 | Viable | One reviewer flags weekly auto-renew; verify billing [S26] |
| 28 | Jobscan | Resume-to-job-description scanner | 7 | Freemium; about $49.95 per month (vendor-stated; not re-verified) | C | 1/1/2/1/2/1 = 8 | Viable | Proprietary match score; no independent validation [S26] |
| 29 | Jobscan Auto Apply | Agentic apply (new) | 7 | Premium add-on (not verified) | D | 1/1/1/1/1/0 = 5 | Caution | New feature; not re-verified |
| 30 | Rezi | Resume builder and internal ATS score | 7 | Free; about $29 per month or $149 lifetime (roundups) | C | 1/1/2/1/2/0 = 7 | Viable | Score is internal to Rezi; vendor-only evidence [S26] |
| 31 | Kickresume | Resume builder | 7 | Free; about EUR 8 per month on annual (roundup) | C | 1/1/2/1/2/1 = 8 | Viable | E2=1: policy allows training on anonymised user documents [S44] |
| 32 | Enhancv | Design-forward resume builder | 7 | Free trial; about $24.99 per month | D | 1/1/2/1/2/0 = 7 | Viable | Conflicting vendor parser claims; use a single-column template [S25, S26] |
| 33 | BOLD-family builders (Zety, MyPerfectResume, LiveCareer, Resume Now) | Resume builder | 7 | Trial about $3, then about $24 per 4 weeks | B | 1/0/2/0/1/1 = 5 | Caution | E2=0 (LiveCareer exposure; broad data-sharing note); E4=0 (billing pattern) [S27, S42] |
| 34 | Resume.io | Resume builder | 7 | Low-cost trial converting to a monthly subscription | C | 1/1/2/0/2/1 = 7 | Caution | E4=0: trial-to-recurring complaint pattern [S27] |
| 35 | Canva resume templates | Design templates | 7 | Free plus Pro | D | 0/1/2/1/2/0 = 6 | Caution | E1=0: vendor test reports parse failures from image-based export; use a text-based PDF and a copy-paste check [S25] |
| 36 | LazyApply | Bulk auto-apply extension | 7 | Reported one-time versus annual (sources conflict) | C | 0/1/0/0/1/1 = 3 | Avoid | D2: LinkedIn prohibits automation; Trustpilot about 2.4/5 [S15, S22] |
| 37 | Sonara (relaunched under BOLD) | Cloud auto-apply | 7 | Subscription (not verified) | D | 1/1/1/1/0/0 = 4 | Caution | E5=0: original service shut down Feb 2024; competitor sources only [S24] |
| 38 | Hosted cloud auto-apply services (named in vendor tests: FastApply, LoopCV, JobCopilot, Massive, AIApply) | Cloud auto-apply | 7 | Subscription (varies) | D | 1/1/1/1/1/0 = 5 | Caution | Not individually audited; vendor-only tests [S18] |
| 39 | MyGreenhouse (candidate profile and Quick Apply) | Candidate portal | 7 | Free | A | 1/1/2/2/2/0 = 8 | Viable | Opt-out of match score; no cross-employer sharing per vendor [S08] |
| 40 | CLEAR identity verification (employer-initiated via Greenhouse) | ID verification | 7, 10 | Free to candidate | A | 1/1/2/2/1/0 = 7 | Viable | Only via a link reached from a known channel; ID and selfie are Tier 3 data [S09] |
| 41 | Third-party LinkedIn automation (connection and message bots, scraping extensions) | Automation | 8 | Subscription | A | 0/0/0/1/1/2 = 4 | Avoid | D2: prohibited; account-restriction exposure [S15] |
| 42 | ADPList | Free mentorship marketplace | 2, 8, 12 | Free (paid tier exists) | C | 1/1/2/2/1/0 = 7 | Viable | Self-published statistics; counts inconsistent across pages [S53] |
| 43 | MentorCruise | Paid mentorship | 8, 12 | Paid subscription (price sources conflict) | D | 1/1/2/1/2/0 = 7 | Viable | Evidence from competitor comparisons [S53] |
| 44 | Blind | Anonymous workplace community | 8, 11, 12 | Free | C | 1/1/2/2/2/0 = 8 | Viable | Anonymous, unverifiable claims; used here only as sentiment [S34, S36] |
| 45 | LeetCode (incl. Premium) | Algorithm practice | 9 | Free plus Premium (price not audited) | D | 1/1/2/1/2/0 = 7 | Viable | Recalled; baseline for algorithm rounds |
| 46 | NeetCode (free plus Pro) | Algorithm roadmap and videos | 9 | Free plus Pro | D | 1/1/2/2/2/0 = 8 | Viable | Recalled; one third-party review (not re-verified) |
| 47 | Hello Interview | System design, ML system design and AI-coding prep | 9 | Premium $47 per month, $89 per year, $299 lifetime (21 Oct 2026) | B | 1/1/2/1/1/0 = 6 | Viable | Primary pricing page; human mocks no longer listed [S33] |
| 48 | Interviewing.io | Anonymous expert mock interviews | 9 | Per session or program (not captured) | C | 1/1/2/1/2/1 = 8 | Viable | Community praise for calibration; cost complaints [S34] |
| 49 | Exponent (incl. Pramp) | Courses plus peer and coach mocks | 9 | Free tier plus paid plans (secondary) | C | 1/1/2/1/2/0 = 7 | Viable | Pramp reportedly absorbed [S34] |
| 50 | ByteByteGo (incl. GenAI system-design title) | System-design books and courses | 9 | Paid | D | 1/1/2/1/2/0 = 7 | Viable | GenAI title reported in secondary mentions; not verified in-session |
| 51 | Google Interview Warmup | Free AI practice | 9 | Free | C | 1/1/2/2/1/1 = 8 | Viable | Secondary roundups only; experimental Google product, longevity unverified [S34] |
| 52 | Yoodli / Big Interview | AI practice with delivery analytics | 9 | Freemium plus subscription | D | 1/1/2/1/2/0 = 7 | Viable | Recalled; roundup mentions [S34] |
| 53 | Final Round AI (mock-interview mode) | AI mock interviews | 9 | Subscription (about $250 for three months reported by one complainant) | C | 1/0/1/0/2/1 = 5 | Caution | E2=0 (audio and screen handling unknown); E4=0 (refund complaint pattern) [S32] |
| 54 | Final Round AI (live Interview Copilot) | Live AI assistant | 10 | Subscription | B | 0/0/0/0/2/1 = 3 | Avoid | D3: undisclosed live assistance; policy and detection risk [S29, S30, S32] |
| 55 | Overlay copilots (Cluely, Interview Coder, Parakeet AI, LeetCode Wizard) | Undetectable live assistant | 10 | Subscription | B | 0/0/0/1/1/1 = 3 | Avoid | D3: undisclosed live assistance [S29, S30] |
| 56 | Beyz / Interviews by AI | AI mock interviews | 9 | Not verified | E | 1/1/1/1/1/0 = 5 | Caution | No independent evidence found; practice only |
| 57 | Disposable VM or container sandbox for assessments | Security practice | 10 | Free or open-source | A | 2/2/2/2/2/2 = 12 | Recommended | Fake-recruiter malware campaigns are documented [S35] |
| 58 | Levels.fyi salary database | Compensation database | 11 | Free data | B | 1/1/2/2/2/1 = 9 | Recommended | For base and big-tech total comp; not a private-equity valuation tool [S36] |
| 59 | Levels.fyi negotiation service | Paid coaching | 11 | Flat fee with money-back guarantee (thresholds vary) | C | 1/1/2/1/2/1 = 8 | Viable | Outcome claims are self-reported [S37] |
| 60 | Comprehensive.io | Posted salary-range benchmarks | 11 | Free benchmarks | C | 1/1/2/2/1/1 = 8 | Viable | Posted ranges only; current status taken from secondary sources [S38] |
| 61 | Carta (startup comp and equity data; calculators) | Equity data and calculators | 11 | Free calculator; employer products paid | C | 1/1/2/2/2/0 = 8 | Viable | Vendor-only evidence; candidate data program status unverified [S38] |
| 62 | Candor | Negotiation coaching | 11 | Success fee (vendor-described; not re-verified) | D | 1/1/2/1/1/0 = 6 | Viable | Self-reported outcomes; low confidence |
| 63 | Rora | Negotiation coaching | 11 | Percentage of the increase | C | 1/1/2/1/2/1 = 8 | Viable | Self-reported outcomes; high self-reported rating [S37] |
| 64 | FairOffer | Comp and negotiation (status unknown) | 11 | Unknown | E | 0/1/1/1/0/0 = 3 | Caution | Searched; no authoritative result; existence and status unverified |

