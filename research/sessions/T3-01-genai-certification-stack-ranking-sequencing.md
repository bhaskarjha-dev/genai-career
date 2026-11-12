---
id: T3-01
title: "GenAI / ML / AI-infra certification stack: value ranking, knowledge-overlap sequencing and dated execution calendars (November 2026)"
date: 2026-11-08
status: complete-with-gaps
topic: ai-certification-strategy
tags: [certifications, genai, agentic-ai, forward-deployed-engineer, claude, aws, google-cloud, databricks, github, nvidia, amd, sequencing, hiring-signal, partner-programmes]
informs_decisions:
  - "Which AI credentials to pursue, skip or defer, by employer segment"
  - "Order of study that exploits blueprint overlap and validity windows"
  - "Whether to pursue partner and FDE gateways (AWS, Google, Anthropic, Microsoft) and what each requires"
  - "Study hours versus portfolio hours at each decision gate"
confidence: "medium. Vendor facts are high confidence where Grade A/B (about 70% of fact-sheet cells). Rankings, overlap percentages, hour estimates and calendars are model outputs (Grade M) built on disclosed assumptions. Hiring-signal evidence is thin and mostly qualitative."
schema_version: "1.0"
temporal_anchor: "2026-11"
last_verified: 2026-11-08
upstream: [T0-11]
---

# T3-01: GenAI certification stack, ranking and sequencing (November 2026)

### Bottom line (read this first)

1. **The question is mostly about access, not exam difficulty.** Two of the most strategically valuable credential families are gated to employers: Claude certifications (Claude Partner Network staff only) and the Gemini Enterprise Partner Specialist badges (Google partner-only). The FDE programmes are partner-linked as well; whether an individual can enrol in AWS FDE without a partner employer is unverified. An individual with no partner employer can open-enrol in AWS, Google Professional, Databricks, GitHub, NVIDIA and AMD credentials. [A: S03, S01; B: S13, S20]
2. **Ranking (composite /40, model):** AIP-C01 29.1 > Google Professional Agentic Architect (PAA) 28.5 > CCAR-P 25.8 > CCAR-F 25.7 > CCDV-F 25.4 > PMLE 24.3 > Gemini Agent Dev 23.9 > MLA 23.8. Tier 1 is **AIP-C01, PAA and (if you have partner access) CCAR-F**. The top-five set does not change under startup-heavy or services-heavy segment weights, but only hiring-signal weights were varied; W2 to W5 are judgement and held fixed.
3. **Knowledge compounding is real but order matters little.** Studying the 24 in-scope credentials independently costs about 917 h (likely case). With blueprint overlap, any sensible order costs about 500 h; the best order found costs about 480 h, and random orders average 501 h (SD 5). So roughly **45% of hours are saved by overlap itself and only about 4% by clever ordering.** The overlap saving is fragile to the transfer-efficiency assumption (28% at eta 0.4, 55% at eta 0.8). [M]
4. **"Google Agentic Architect is the first GenAI credential with hands-on labs" is only half right.** The hybrid format is confirmed (proctored MCQ plus two Google Skills labs). It is not the first hands-on credential (AWS Demonstrated microcredentials, Gemini partner badges and AWS FDE pre-date it), and I found no evidence that any lab component is proctored. [A: S11, S20, S13]
5. **Do not buy a stack for hiring signal alone.** The only causal evidence (Athey and Palikot RCT) shows effects concentrated in weak-signal candidates, and it studies MOOC certificates, not vendor professional exams. Hiring-signal evidence for vendor AI certifications lives in partner/SI job posts (Deloitte AWS FDE posts list AIP-C01 and MLA among qualifying certifications) and in partner-tier headcount arithmetic, not in frontier-lab hiring. [A: S43; B: S27, S28, S10]
6. **Three dated plans** are in the Recommendation: A (10 h/week) ends 2027-11-29 with the optional AWS and Google FDE programmes, or 2027-10-12 without them; B (20 h/week, career switcher) ends 2027-03-28 (2027-05-20 with a portfolio split); C (40 h/week, everything) ends 2027-03-15. Each carries optimistic and pessimistic bands.

> **List-size discrepancy to resolve.** The brief says "35 credentials + 3 FDE programmes" (and "38 credentials/programmes"), but the enumerated list contains **24 credentials + 4 FDE entries (28 line items)**. I analysed all 28, plus credentials discovered during research. If 10 or more credentials were dropped from the pasted list, they are not covered here.

### Evidence grades used throughout

| Grade | Meaning |
|---|---|
| **A** | Vendor-canonical source retrieved this session (official exam page, exam guide, vendor blog, Credly badge, Pearson VUE page, Microsoft Learn). Canonical URL or title in the ledger. |
| **B** | Specific and checkable but second-hand: partner press release, job posting, independent tracker that cites vendor pages, multiple consistent third-party summaries. |
| **C** | Single blog, community post, marketing page or anecdote. Treat as a lead. |
| **D** | Recalled from model memory, not verified this session. Capped at D. |
| **M** | Model estimate computed from stated assumptions (overlap, hours, scores, calendars). Not evidence about the world. |
| **X** | Prior belief contradicted by evidence. |

### ID key (abbreviations used in the tables)


| ID used in tables | Credential |
|---|---|
| AIP-C01 | AWS Certified GenAI Developer – Professional |
| PAA | Google Professional Agentic Architect |
| CCAR-P | Claude Certified Architect – Professional |
| CCAR-F | Claude Certified Architect – Foundations |
| CCDV-F | Claude Certified Developer – Foundations |
| PMLE | Google Professional ML Engineer |
| GEM-AGT | Gemini Enterprise Partner Specialist – Agent Development |
| MLA | AWS Certified ML Engineer – Associate (C01→C02) |
| GEM-DEP | Gemini Enterprise Partner Specialist – Deployment |
| GH-300 | GitHub Copilot (GH-300) |
| DBX-GAI | Databricks GenAI Engineer Associate |
| GH-600 | GitHub Agentic AI Developer (GH-600) |
| DBX-CTX | Databricks Context Engineer Associate |
| DBX-MLP | Databricks ML Professional |
| NCP-AAI | NVIDIA NCP-AAI |
| NCP-GENL | NVIDIA NCP-GENL |
| AIF-C01 | AWS Certified AI Practitioner |
| GAIL | Google Generative AI Leader |
| DBX-MLA | Databricks ML Associate |
| AIB-C01 | AWS Certified AI Business Strategist |
| NCA-GENL | NVIDIA NCA-GENL |
| GH-700 | GitHub Agentic AI Business Professional (GH-700, beta) |
| AMD | AMD ROCm Certified Associate |
| CCAO-F | Claude Certified Associate – Foundations |
| AWS-FDE-V | AWS Partner FDE Validated (programme) |
| AWS-FDE-A | AWS Partner FDE Advanced (programme) |
| GOOG-FDE | Google Gemini Enterprise FDE enablement (programme) |
| MS-FTE | Microsoft Frontier Transformation Engineer, LevelUp (programme; out of scope) |


---

## Prior (propositions held before research; recalled, Grade D)

| # | Proposition (checkable) | Prior belief | How tested | Result (details in Delta) |
|---|---|---|---|---|
| P1 | Google's Professional Agentic Architect is the first major GenAI credential with a hands-on lab component. | 70% | Google FAQ and exam guide; search for earlier hands-on credentials | **Partly contradicted** |
| P2 | Claude certifications can be bought by any individual (Anthropic site or Pearson VUE) for about $99 to $175 and last 12 months. | 55% | Anthropic Partner Academy FAQ, Pearson VUE page | **Price and validity right; open access wrong (X)** |
| P3 | AWS MLA-C01 is the current AWS ML associate; AIF-C01 and AIP-C01 are the AWS GenAI pair. | 80% | AWS blog, exam pages | **Partly wrong:** MLA-C01 retired in English on 2026-09-28; MLA-C02 beta is live |
| P4 | Databricks Context Engineer is the only context-engineering credential and overlaps about 60% with the GenAI Engineer Associate. | 60% | Blueprint comparison, vendor claims, competitor search | **Uniqueness supported; overlap revised down to about 35 to 42%** |
| P5 | FDE programmes accept an equivalent professional certification from another vendor. | 30% | AWS, Google, Microsoft programme rules | **Contradicted (no cross-vendor acceptance found)** |
| P6 | Certifications are weak hiring signals at frontier labs and can read negatively when stacked; value concentrates in IT services and partner/SI segments. | 75% | JD samples, surveys, RCT | **Supported; evidence mostly qualitative** |
| P7 | Study order materially changes total hours (more than 25% versus random order). | 60% | Blueprint-overlap model, 2,000 random orders plus annealing | **Contradicted:** order changes about 4%; overlap itself saves about 45% |

---

## Research Question

Given the November 2026 landscape (vendor agentic credentials, a hybrid hands-on exam, partner FDE programmes with certification prerequisites, new context-engineering and agentic-governance categories), **which credentials deliver the most career value per hour, what is their evidence-grounded rank, and what sequence minimises hours and maximises pass probability and hiring signal for three personas** (10 h/week engineer, 20 h/week career switcher, 40 h/week "everything")?

Scope: the enumerated list plus directly competing credentials found during research. Out of scope: degrees, generic cloud-architect certifications, Microsoft certifications (excluded by the requester; the Microsoft FTE gateway is mapped as a gap because it gates a major FDE route).

---

## Key Findings (18, each with an evidence grade)

**F1. Claude certifications are partner-gated, not publicly purchasable. [A]** Anthropic's Partner Academy eligibility and FAQ pages restrict the four exams (CCAO-F, CCDV-F, CCAR-F, CCAR-P) to staff of Claude Partner Network organisations using a partner email domain; Pearson VUE's Anthropic page says the same. Exams are delivered by Pearson VUE (OnVUE or test centre), 120 minutes, closed book, passing score 720/1000, English and Japanese. List fees: CCAO-F $99, CCDV-F $125, CCAR-F $125 (raised from $99 on 2026-06-30), CCAR-P $175. Retakes wait 14, 30 and 90 days, maximum four attempts per rolling 12 months. [S01, S02, S03, S04]

**F2. Claude validity is 12 months (previously 6), with a free non-proctored renewal if done on time; a lapse means a full-fee retake. [A]** This confirms the UNVERIFIED upstream claim. Exam content for CCAO-F, CCDV-F and CCAR-P updates on **2026-12-07** (new guides from 2026-11-17); CCAR-F is not listed in that refresh. Higher partner tiers get 50% off and Global Premier fees are waived entirely through 2026-12-31. [S01, S03]

**F3. Claude certifications carry institutional pull rather than open-market pull. [A/B]** The Claude Partner Network launched 2026-03-12 with a $100M commitment; Anthropic's services-track post (2026-06-03) ties partner tiers to counts of active certified individuals (secondary summaries give roughly 10 / 100 / 1,000 for Select / Preferred / Global Premier; verify). CCAO-F does **not** count toward partner eligibility; CCDV-F, CCAR-F and CCAR-P do. One partner JD (Bounteous Lead FDE) lists a Claude Architect certification as preferred; I found no certification requirement or preference in 8+ of Anthropic's own FDE postings. A claim that 46,000 firms hold more than 175,000 Claude certifications comes via secondary coverage of Anthropic's Frontier Academy post and conflicts with a June figure of 10,000+; treat as unverified. [S03, S04, S05, S06, S07, S09, S10]

**F4. Google PAA is a confirmed hybrid: proctored MCQ plus two hands-on labs in Google Skills. [A]** GA exam $200 (beta $120), 2 hours (beta 3), labs under 5 hours to complete within two months of passing, **1-year validity** with a continuing-education path, GA mid-November 2026. Five sections: low-code agents about 13%, coding agents about 17%, custom agents about 33%, evaluation and deployment about 22%, security and governance about 15%. MCP and A2A are explicitly in scope. [S11, S12]

**F5. PAA is not the first hands-on credential and I could not verify that its labs are proctored. [A, with absence-of-evidence caveat]** AWS "Demonstrated" microcredentials (for example Agentic AI Demonstrated) are timed hands-on challenges in live AWS environments; Google's Gemini Enterprise Partner Specialist badges are lab-based; AWS FDE validation runs in AWS-provisioned environments; AMD's programme agreement allows practical demonstration. Searched Google's FAQ, AWS pages and AMD's agreement: none states lab proctoring. What PAA is first at (within my search): a **professional-tier certification that couples a proctored exam with mandatory labs.** [S11, S19, S20, S13, S41]

**F6. The AWS line-up changed under the brief's feet. [A]** AIP-C01 is live ($300, 75 questions with 65 scored, 180 minutes, MC/MR, Pearson VUE, passing 750, domains 31/26/20/12/11). **MLA-C01 closed in English on 2026-09-28**; MLA-C02 beta (English only; $75, 85 questions and 170 minutes per third-party sources, Grade C) opened 2026-09-29; AWS's blog dates GA to **2027-01-14** (the exam page still says TBD; third-party sources). The AI Business Strategist (AIB-C01, Business category, beta $50, standard $100, 3-year validity, no AWS-service testing) is in beta. [S19, S21, S22, S23, S54]

**F7. FDE programmes demand same-vendor credentials; I found no cross-vendor acceptance. [A/B]** AWS FDE Validated needs an active AWS Associate or Professional certification plus pathway validation; FDE Advanced needs an active **AIP-C01** plus validation across all three pathways (Ground, Orchestrate, Prove); both are free via Skill Builder and assessed by hands-on validation (not only MCQ), which confirms the upstream claim. Google's FDE enablement (4 days) required two Gemini Enterprise certifications, one Google Cloud Professional certification and an active Gemini Enterprise customer project (partner press release). Microsoft's FTE LevelUp requires GH-300 plus AI-103 (AI-102 reported as accepted) plus AB-100, about 86 hours across three milestones. Anthropic's Claude Frontier Academy is nomination-only. [S20, S15, S37, S07]

**F8. Gemini Enterprise Partner Specialist badges are partner-only, lab-based and short-lived. [B]** Each requires three skill badges (challenge labs) in Google Skills for Partners; Credly shows "Validation, Advanced"; example badges carry **six-month validity** (the brief's 2027-02-11 expiry is consistent with an August 2026 issue). Because Google's FDE route needs both, these must be timed just before the bootcamp. [S13, S14, S16]

**F9. Databricks Context Engineer: facts verified, "first" claim unrefuted, overlap with GenAI Engineer is about 35 to 42%, not 80%. [A for facts; M for overlap]** 45 scored questions, 90 minutes, $200, proctored, 2-year validity, GA 2026-07-29; seven domains (foundations 16, system prompts 9, retrieval and Genie 20, memory with Lakebase and MLflow 18, tools and MCP 13, compaction 11, multi-agent 13). Databricks calls it the industry's first context-engineering certification. Extended search found no other vendor credential dedicated to context engineering; Claude (CCAR-F, CCAR-P), Google PAA and GH-600 embed context and memory domains. Using blueprint weights and study hours, GenAI Engineer covers about 42% of the Context Engineer blueprint; the other direction is about 34%. About 36% of the Context Engineer weight (memory, compaction, context failure modes) has no counterpart in the GenAI Engineer blueprint. [S30, S31, S32, M]

**F10. GH-600 covers MCP at configuration depth and has no A2A; PAA covers both. [A]** Microsoft Learn's study guide lists MCP server configuration (adding servers as tools, the GitHub remote server, registries, allow lists) inside a GitHub/Copilot implementation frame, and does not mention A2A. PAA's guide names MCP and A2A for orchestrating agents. Studying PAA first covers about 68% of the GH-600 blueprint; the reverse is about 35% (M). [S33, S12]

**F11. NVIDIA NCP-AAI is real but has registration ambiguity; its blueprint sums to 98%. [A/B]** 120 minutes, $200, 60 to 70 questions, remote proctored (Certiverse), 2-year validity, ten topic areas of which NVIDIA platform content is only 7%. The NVIDIA EU page (updated 2026-10-30) still shows "(Coming soon)" beside registration while third-party guides and Credly's AI badge roundup treat it as live; published topic weights sum to 98%, which I normalised. [S38, S52]

**F12. AMD ROCm Certified Associate is free, 24-month and AMD-ecosystem-bound. [A/B]** Launched 2026-07-24 via AMD AI Academy with a Credly badge; the associate scope is ROCm fundamentals, HIP programming and GPU performance concepts; Professional (RCCL distributed training, vLLM/SGLang inference) is "coming soon" and Expert is announced for early 2027. I found no employer outside AMD's ecosystem naming it. [S40, S41, S42]

**F13. Hiring-signal evidence sits in partner/SI job posts, and no credential exceeds a 10% JD share in anything I could verify. [B/C]** Deloitte US FDE-AWS lists "at least 3 of 6" named AWS certifications (visible entries: Cloud Practitioner, Solutions Architect Associate, AIF-C01, AIP-C01; the Lead FDE post's list also names MLA-C01 and Data Engineer Associate); Deloitte's Senior AWS FDE post lists one Associate-level certification (including MLA) and one Professional-level certification (including AIP-C01). The snippets do not show whether those sections are labelled required or preferred. Surveys are weak: a 2025 survey reported by Rework found 23% of hiring managers actively screen for AI certifications; KDnuggets and InfoWorld repeat portfolio-over-certification claims. I could not run LinkedIn, Indeed, Wellfound or Ashby counts or recruiter Boolean-string audits with the tools available (honest gap). [S27, S28, S44, S45, S46]

**F14. The causal evidence is real but narrow. [A]** Athey and Palikot ran an RCT on 800,000+ MOOC certificate earners in developing countries without college degrees; credential-sharing encouragement raised new employment by 6% (1.0 percentage point) and by 9% (1.2 pp) for certificate-related jobs, concentrated among weak baseline profiles, with a resume experiment showing 15 to 20 point effects for weak resumes and near zero for strong ones. Upstream's "+11pp" figure was **not reproduced** (I may be seeing intent-to-treat versus complier estimates). External validity to experienced engineers taking vendor professional exams is weak. [S43]

**F15. Blueprint overlap is large for same-vendor and agentic clusters, small for ML-versus-GenAI. [M, anchored on A/B blueprints]** Strongest directional transfers: PAA to Gemini Agent Dev 82%, CCAR-P to CCDV-F 84%, PAA to CCAR-P 78%, PAA to NCP-AAI 76%, CCAR-F to CCDV-F 76%, PMLE to MLA 73%, GH-600 to GH-300 72%, PAA to GH-600 68%. Almost nothing transfers between the ML cluster (MLA, PMLE, Databricks ML) and the agentic cluster (PAA, CCAR, GH-600): 1 to 12%. AIF-C01 as a seed is poor (its 14 hours cover 9% of AIP-C01) while AIP-C01 covers 78% of AIF-C01. [S: model]

**F16. Seeds and ordering. [M]** Best "seed" credentials by hours saved across the remaining 23: PAA 248 h, AIP-C01 226 h, CCAR-P 219 h, PMLE 218 h, NCP-AAI 211 h. Total: 917 h standalone; 498 h in my curated order; 480 h best found; 501 h random mean; 493 h smallest-first. A weighted-completion-time objective front-loads cheap credentials (GH-300, CCDV-F, AIF-C01), which is mathematically sound and strategically wrong, so the recommended order is curated. [M]

**F17. Validity ranges from 6 months to 3 years and shapes the calendar. [A/B/D]** Gemini badges 6 months (B); Claude, PAA and GitHub exams 12 months (GitHub: annual free Microsoft renewal per Microsoft Learn; third parties say 2 years, so conflicting); Databricks, NVIDIA, AMD 24 months; AWS 36 months (AIP and AIF listed on 3-year terms; recalled for MLA); PMLE 24 months is recalled (D) and unverified. Short-validity credentials belong last in a sequence, and renewal cost is part of the real price. [S03, S11, S33, S41, S30]

**F18. Total cost and exam integrity. [M/B/C]** List fees for all 24 credentials total **$3,427 (about Rs 3.82 lakh at Rs 94.58 per USD with an assumed 18% GST)**; AWS's repeat-exam 50% voucher takes the AWS block from $650 to about $375 if AIF-C01 is taken first (about $475 if AIP-C01 goes first). Claude and Gemini badges are free or discounted only through partner employers; Microsoft's LevelUp offers vouchers to partner staff. Commercial exam-question vendors already advertise new exams (Databricks Context Engineer and GitHub agentic exams), so signal dilution is plausible; AWS does not publish pass rates, so any quoted pass rate is unverified. [S48, S51; M]

---

## Recommendation

### R1. Value-ranked tier list

Tiers combine the composite score (Detailed Findings D3), redundancy (how much of the credential is already covered by higher-ranked ones), access (open versus partner-gated) and availability (beta, retiring, or GA pending). "Gated" means an individual cannot enrol without an employer relationship. All scores are Grade M; the facts behind them are graded in D1.

| Tier | Credential | Composite /40 | Access | Why it earns the tier | Skip or defer when |
|---|---|---|---|---|---|
| **1 Must-do** | **AWS Certified GenAI Developer – Professional (AIP-C01)** | 29.1 | Open | Only credential that is open-enrolment, named in SI job posts (Deloitte AWS FDE posts), the hard prerequisite for AWS FDE Advanced, 3-year validity, and the second-best seed (226 h saved across the stack). $300, 180 min. | You will never work on AWS: use PAA or PMLE as your cloud flagship. If you plan to take AIF-C01 anyway, take it first and use the 50% repeat voucher. |
| **1 Must-do** | **Google Professional Agentic Architect (PAA)** | 28.5 | Open (GA mid-Nov 2026) | Highest knowledge utility (two hands-on labs, MCP and A2A, evaluation, security), the Google "Professional" gateway to the FDE bootcamp, best seed in the stack (248 h saved). $200. | Cost per validity-year is the highest in Tier 1 because it lasts 12 months. Defer 2 to 4 weeks if you depend on third-party prep, which is still thin for a GA that is days old. |
| **1 Must-do (conditional)** | **Claude Certified Architect – Foundations (CCAR-F)** | 25.7 | **Gated** (Claude Partner Network staff) | Cheapest professional-grade agentic credential ($125), counts toward partner tiers, 64% already covered after PAA, so about 20 h marginal. | Your employer is not in the Claude Partner Network: ask it to join (secondary sources say the Registered tier is free for organisations; verify) or cover the same ground with PAA plus GH-600 or Databricks Context Engineer. |
| 2 Strong situational | Claude Certified Architect – Professional (CCAR-P) | 25.8 | Gated | Seniority depth (governance 14%, stakeholder and lifecycle, evaluation 16%). After PAA and CCAR-F it adds about 25 h. | You are not in a Claude-heavy consultancy; CCAR-F already counts for partner headcount. |
| 2 | Google Professional ML Engineer (PMLE) | 24.3 | Open | Only 32% covered by PAA, so it is a separate cluster; the Google "Professional" alternative; right for training, serving and pipeline roles on GCP. | Role is agent-application engineering, not model pipelines. |
| 2 | AWS ML Engineer Associate (MLA; C02) | 23.8 | Open (beta now, GA 2027-01-14) | AWS Associate-level gateway to FDE Validated; named in Deloitte lists; 73% covered by PMLE if taken second. | **MLA-C01 can no longer be booked in English.** Wait for C02 GA unless you want the $75 beta. |
| 2 | Gemini Enterprise Partner Specialist: Agent Development and Deployment | 23.9 / 22.1 | **Partner-only** | Hard prerequisites for Google FDE; PAA already covers 82% and 78% of them, so each is 8 to 12 h. | You are not in a Google partner. **Six-month validity: take them within about six weeks of the bootcamp.** |
| 2 | Databricks GenAI Engineer Associate (DBX-GAI) | 20.1 | Open | Enterprise data-platform signal; 64% covered by AIP-C01. | Employer is not on Databricks. |
| 2/3 | GitHub Copilot (GH-300) | 21.0 | Open | Cheap ($99, about 9 to 14 h) and a mandatory prerequisite for Microsoft FTE; modest knowledge value. | Not pursuing the Microsoft route or a Copilot-heavy employer. |
| 3 Nice-to-have | Claude Developer – Foundations (CCDV-F) | 25.4 | Gated | 76% covered by CCAR-F; a "developer" label for partner headcount. | You already hold CCAR-F. |
| 3 | GH-600, Databricks Context Engineer, Databricks ML Professional, NCP-AAI, NCP-GENL, AIF-C01 | 19.8, 19.6, 19.1, 18.0, 17.8, 17.0 | Open | Each is either largely redundant (GH-600 68% and NCP-AAI 76% covered by PAA), platform-specific (Databricks) or a cheap rule-filler (AIF-C01 counts in Deloitte's "3 of 6" rule). | No named requirement in your target JDs or partner tier. |
| 4 Skip or learning-only | CCAO-F, Gen AI Leader, AIB-C01, NCA-GENL, Databricks ML Associate, GH-700, AMD ROCm Associate | 12.4 to 15.7 | Mixed | CCAO-F does not count toward partner eligibility (A) and is 90% covered by CCAR-P; Leader and AIB are non-technical; NCA-GENL is fully subsumed by NCP-GENL; ML Associate is 80% subsumed by ML Professional; GH-700 is a beta business credential; AMD ROCm is free and worth studying for GPU skills but has no recognition I could find outside AMD. | Take only if a named requirement exists. AMD ROCm costs nothing, so "learning-only" is a cost of time, not money. |

**FDE programmes (not scored in the composite):**
- **AWS FDE Validated and Advanced: Tier 1 for staff at AWS partners.** Free, hands-on, about 8 h and about 26 h on top of the prerequisite certification.
- **Google Gemini Enterprise FDE enablement: Tier 2 (partner).** Needs a Google Professional certification, two Gemini badges and an active customer project.
- **Microsoft FTE LevelUp: gap.** GH-300 plus AI-103 plus AB-100, about 86 h; Microsoft exams were excluded from scope.
- **Claude Frontier Academy: nomination-only.** No individual path exists; employer nomination is the route (S07).

**By employer segment (what the evidence supports):**

| Segment | What helps | What does not |
|---|---|---|
| Frontier lab | Shipped systems, evals, open-source contributions. I found no certification requirement or preference in 8+ Anthropic FDE postings. | Stacking. Certifications neither required nor, as far as I found, rewarded; a long list can read as substituting study for building (practitioner opinion, Grade C). |
| AI startup | One broad credential (AIP-C01 or PAA) at most; NCP-GENL if the role is inference or GPU work. | A full stack; no verified demand. |
| Enterprise product team | The platform credential that matches the company's cloud (AIP-C01, PAA, PMLE) and Databricks if on a lakehouse. | Vendor-neutral or niche (AMD, GH-700). |
| IT services / GCC | AIP-C01, CCAR-F, PAA, GH-300; the employer's partner tier makes your certification count commercially. | Credentials the employer's partner programmes do not count. |
| Partner / SI | The full gated stack for the partners you work with; FDE programmes. | Nothing in Tiers 1 and 2 hurts here. |

### R2. Optimal sequencing plan

**What the model says (Grade M; method and assumptions in D2).**

| Scenario (24 credentials) | Total hours | Note |
|---|---|---|
| Naive: each credential studied from scratch | **917** (589 low / 1,360 high) | Sum of standalone likely-case hours |
| Random order, mean of 2,000 shuffles | 501 (SD 5) | Overlap alone: about 45% saved |
| The brief's list order | 499 | |
| Smallest-first | 493 | |
| **Recommended (curated) order** | **498** | Chosen for value, access and validity, not minimum hours |
| Best order found (annealing on hours only) | 480 | Ordering adds only about 4% over curated |
| Curated order, transfer efficiency eta = 0.4 / 0.5 / 0.65 / 0.8 | 659 / 594 / 498 / 412 | Savings versus naive: 28% / 35% / 46% / 55% |
| FDE add-ons (AWS Validated 8 h, Advanced 26 h, Google bootcamp 32 h) | +66 | Microsoft FTE (86 h) excluded; GH-300 is inside it |

Naive with FDE add-ons is 983 h; optimised is about 564 h.

**Reading the numbers honestly.** Ordering barely matters because most of the saving comes from having many overlapping credentials, not from sequencing them cleverly. The more important sequencing effects are non-hour effects: validity decay, partner-gated windows, fee discounts and event dates. I therefore recommend a curated order in waves:

1. **Wave 1, open Tier 1 seeds: AIP-C01 then PAA.** Together they cover the widest swathe of later blueprints (PAA seeds 248 h, AIP-C01 226 h). AIP-C01's 3-year validity makes it safe to take first; PAA's 12 months argues for taking it second, so Wave 2 can ride on fresh labs. If you are AWS-partner staff, add **AWS FDE Validated then Advanced** here, while the hands-on skills are warm.
2. **Wave 2, Claude block (gated): CCAR-F, then CCAR-P, then CCDV-F.** Keep all three within one 12-month window (one cheap renewal covers them). Book CCAR-P and CCDV-F after **2026-12-07** (content refresh; new guides from 2026-11-17). If your employer is Global Premier, finish all four exams before **2026-12-31** (fees waived).
3. **Wave 3, platform branches (choose only the ones your stack matches):** Databricks (GAI then CTX), GitHub (GH-300 then GH-600), NVIDIA (NCP-AAI, then NCP-GENL for GPU work).
4. **Wave 4, ML cluster (separate knowledge domain): PMLE, then MLA-C02 (after GA 2027-01-14), then Databricks ML Associate and Professional only if required.**
5. **Wave 5, cheap tail, only for a named requirement:** AIF-C01, AIB-C01, Gen AI Leader, GH-700, CCAO-F, AMD ROCm, NCA-GENL.
6. **Wave 6, just-in-time short-validity items: Gemini Agent Development, Gemini Deployment, then the Google FDE bootcamp** (six-month badges must not expire before the bootcamp).

**"If you study X first, you already know Y%"** (directional blueprint-overlap model, Grade M, plan for ±15 points):

| Study first | Then you already cover roughly… |
|---|---|
| **PAA** | Gemini Agent Development **82%**, CCAR-P **78%**, Gemini Deployment **78%**, NCP-AAI **76%**, CCDV-F **72%**, GH-600 **68%**, CCAR-F **64%**, AIP-C01 **62%**, GH-300 55% |
| **AIP-C01** | AIF-C01 **78%**, CCDV-F **70%**, CCAR-P **68%**, NCP-AAI **65%**, PAA **58%**, Gemini Deployment 55%, CCAR-F 49% |
| **CCAR-P** | CCAO-F 90%, CCDV-F **84%**, CCAR-F **72%**, GH-600 57% |
| **CCAR-F** | CCDV-F **76%**, Gemini Agent Dev 58%, CCAR-P 48% |
| **PMLE** | AIF-C01 75%, **MLA 73%**, Databricks ML Professional 60% |
| **Databricks ML Professional** | Databricks ML Associate **80%**, PMLE 69%, MLA 68% |
| **GH-600** | GH-300 72%, GH-700 68%, CCAR-F 54% |
| **Databricks GenAI Engineer** | Databricks Context Engineer **42%** (not 80%), CCDV-F 49% |
| Weak seeds | AIF-C01 covers only 9% of AIP-C01; CCAO-F 19% of AIF-C01; MLA 3% of PAA; the ML cluster and the agentic cluster share 1 to 12% |

### R3. Three dated calendars

**Common assumptions.** Start Monday **2026-11-09**. Hours are the overlap-adjusted likely case for the order shown plus 3 h of exam logistics each; **no retake buffer** (add 10 to 15% contingency). Weekly hours are all spent on certifications unless stated. Plans A and B pause 2026-12-21 to 2027-01-03. Plan B multiplies hours by 1.3 (weaker baseline). Expiry dates assume the validity in D1. Partner-gated items assume your employer holds the relevant partner status; **the no-access variant is below each plan.**


**Plan A — working engineer, 10 h/week (Mon 2026-11-09 start; 2-week holiday pause 2026-12-21 → 2027-01-03)**

| # | Credential / programme | Study start | Target exam / completion | Hours (incl. 3 h exam logistics) | Expires |
|---|---|---|---|---|---|
| 1 | AIP-C01 | 2026-11-09 | **2027-01-16** | 78 | 2030-01-16 |
| 2 | PAA | 2027-01-17 | **2027-02-22** | 53 | 2028-02-22 |
| 3 | CCAR-F | 2027-02-23 | **2027-03-11** | 23 | 2028-03-11 |
| 4 | CCAR-P | 2027-03-12 | **2027-03-29** | 24 | 2028-03-29 |
| 5 | AWS-FDE-V (FDE programme) | 2027-03-30 | **2027-04-04** | 8 | n/a |
| 6 | AWS-FDE-A (FDE programme) | 2027-04-05 | **2027-04-23** | 26 | n/a |
| 7 | DBX-GAI | 2027-04-24 | **2027-05-13** | 28 | 2029-05-13 |
| 8 | DBX-CTX | 2027-05-14 | **2027-05-29** | 22 | 2029-05-29 |
| 9 | GH-300 | 2027-05-30 | **2027-06-05** | 9 | 2028-06-05 |
| 10 | GH-600 | 2027-06-06 | **2027-06-23** | 25 | 2028-06-23 |
| 11 | PMLE | 2027-06-24 | **2027-08-06** | 62 | 2029-08-06 |
| 12 | MLA | 2027-08-07 | **2027-08-25** | 27 | 2030-08-25 |
| 13 | NCP-AAI | 2027-08-26 | **2027-09-13** | 26 | 2029-09-13 |
| 14 | NCP-GENL | 2027-09-14 | **2027-10-04** | 30 | 2029-10-04 |
| 15 | CCDV-F | 2027-10-05 | **2027-10-14** | 13 | 2028-10-14 |
| 16 | AIF-C01 | 2027-10-15 | **2027-10-20** | 8 | 2030-10-20 |
| 17 | GEM-AGT | 2027-10-21 | **2027-10-29** | 12 | 2028-04-29 |
| 18 | GEM-DEP | 2027-10-30 | **2027-11-06** | 11 | 2028-05-06 |
| 19 | GOOG-FDE (FDE programme) | 2027-11-07 | **2027-11-29** | 32 | n/a |
| | **Total** | 2026-11-09 | **2027-11-29** | **517** | |


- *Plan A without partner access* (drop Claude, Gemini, FDE programmes): 11 credentials (AIP-C01, PAA, DBX-GAI, DBX-CTX, GH-300, GH-600, PMLE, MLA, NCP-AAI, NCP-GENL, AIF-C01), about 373 h, ends **2027-08-16**.
- *Plan A bands (core 16 credentials, excluding FDE add-ons):* optimistic 279 h to 2027-06-15; base 451 h to 2027-10-12; pessimistic 824 h to 2028-06-28.
- *Expiry watch:* the 12-month items lapse within about 3 to 4 months of the plan's end (PAA 2028-02-22, CCAR-F 2028-03-11, CCAR-P 2028-03-29); renew only if they are counted for a partner tier or an FDE gate (Gate 4).

**Plan B — career switcher, 20 h/week all-in on certifications (hours ×1.3 for weaker baseline)**

| # | Credential / programme | Study start | Target exam / completion | Hours (incl. 3 h exam logistics) | Expires |
|---|---|---|---|---|---|
| 1 | AIF-C01 | 2026-11-09 | **2026-11-16** | 21 | 2029-11-16 |
| 2 | AIP-C01 | 2026-11-17 | **2026-12-20** | 95 | 2029-12-20 |
| 3 | PAA | 2026-12-21 | **2027-01-27** | 68 | 2028-01-27 |
| 4 | DBX-GAI | 2027-01-28 | **2027-02-09** | 35 | 2029-02-09 |
| 5 | MLA | 2027-02-10 | **2027-03-04** | 64 | 2030-03-04 |
| 6 | PMLE | 2027-03-05 | **2027-03-23** | 54 | 2029-03-23 |
| 7 | GH-300 | 2027-03-24 | **2027-03-28** | 12 | 2028-03-28 |
| | **Total** | 2026-11-09 | **2027-03-28** | **349** | |

**Plan B′ — same, but 14 h cert + 6 h portfolio per week (recommended)**

| # | Credential / programme | Study start | Target exam / completion | Hours (incl. 3 h exam logistics) | Expires |
|---|---|---|---|---|---|
| 1 | AIF-C01 | 2026-11-09 | **2026-11-19** | 21 | 2029-11-19 |
| 2 | AIP-C01 | 2026-11-20 | **2027-01-20** | 95 | 2030-01-20 |
| 3 | PAA | 2027-01-21 | **2027-02-23** | 68 | 2028-02-23 |
| 4 | DBX-GAI | 2027-02-24 | **2027-03-13** | 35 | 2029-03-13 |
| 5 | MLA | 2027-03-14 | **2027-04-15** | 64 | 2030-04-15 |
| 6 | PMLE | 2027-04-16 | **2027-05-13** | 54 | 2029-05-13 |
| 7 | GH-300 | 2027-05-14 | **2027-05-20** | 12 | 2028-05-20 |
| | **Total** | 2026-11-09 | **2027-05-20** | **349** | |


*Plan B bands (all 20 h/week to certification):* optimistic 220 h to 2027-02-10; base 349 h to 2027-03-28; pessimistic 586 h to 2027-06-19. Partner-gated items are excluded because a switcher usually has no partner employer; once hired by a partner, slot CCAR-F and the AWS FDE steps after PAA. I recommend the **B′ split (14 h certification plus 6 h portfolio per week)**; the Athey and Palikot effect is largest for weak-signal candidates, and a switcher's signal is weak, so portfolio and certification are complements, not substitutes.


**Plan C — everything as fast as possible, 40 h/week, no breaks**

| # | Credential / programme | Study start | Target exam / completion | Hours (incl. 3 h exam logistics) | Expires |
|---|---|---|---|---|---|
| 1 | AIP-C01 | 2026-11-09 | **2026-11-22** | 78 | 2029-11-22 |
| 2 | PAA | 2026-11-23 | **2026-12-02** | 53 | 2027-12-02 |
| 3 | AWS-FDE-V (FDE programme) | 2026-12-03 | **2026-12-04** | 8 | n/a |
| 4 | AWS-FDE-A (FDE programme) | 2026-12-05 | **2026-12-09** | 26 | n/a |
| 5 | CCAR-F | 2026-12-10 | **2026-12-14** | 23 | 2027-12-14 |
| 6 | CCAR-P | 2026-12-15 | **2026-12-19** | 24 | 2027-12-19 |
| 7 | CCDV-F | 2026-12-20 | **2026-12-22** | 13 | 2027-12-22 |
| 8 | DBX-GAI | 2026-12-23 | **2026-12-27** | 28 | 2028-12-27 |
| 9 | DBX-CTX | 2026-12-28 | **2026-12-31** | 22 | 2028-12-31 |
| 10 | GH-300 | 2027-01-01 | **2027-01-02** | 9 | 2028-01-02 |
| 11 | GH-600 | 2027-01-03 | **2027-01-07** | 25 | 2028-01-07 |
| 12 | NCP-AAI | 2027-01-08 | **2027-01-12** | 26 | 2029-01-12 |
| 13 | PMLE | 2027-01-13 | **2027-01-23** | 62 | 2029-01-23 |
| 14 | MLA | 2027-01-24 | **2027-01-28** | 27 | 2030-01-28 |
| 15 | DBX-MLA | 2027-01-29 | **2027-02-02** | 23 | 2029-02-02 |
| 16 | DBX-MLP | 2027-02-03 | **2027-02-10** | 43 | 2029-02-10 |
| 17 | NCA-GENL | 2027-02-11 | **2027-02-13** | 12 | 2029-02-13 |
| 18 | NCP-GENL | 2027-02-14 | **2027-02-19** | 29 | 2029-02-19 |
| 19 | AMD | 2027-02-20 | **2027-02-22** | 13 | 2029-02-22 |
| 20 | AIF-C01 | 2027-02-23 | **2027-02-24** | 8 | 2030-02-24 |
| 21 | AIB-C01 | 2027-02-25 | **2027-02-26** | 10 | 2030-02-26 |
| 22 | GAIL | 2027-02-27 | **2027-02-28** | 6 | 2030-02-28 |
| 23 | GH-700 | 2027-03-01 | **2027-03-02** | 7 | 2028-03-02 |
| 24 | CCAO-F | 2027-03-03 | **2027-03-04** | 6 | 2028-03-04 |
| 25 | GEM-AGT | 2027-03-05 | **2027-03-07** | 12 | 2027-09-07 |
| 26 | GEM-DEP | 2027-03-08 | **2027-03-09** | 11 | 2027-09-09 |
| 27 | GOOG-FDE (FDE programme) | 2027-03-10 | **2027-03-15** | 32 | n/a |
| | **Total** | 2026-11-09 | **2027-03-15** | **636** | |


*Plan C bands (excluding FDE add-ons):* optimistic 350 h to 2027-01-22; base 570 h to 2027-03-02; pessimistic 1,049 h to 2027-05-21. At 40 h/week for 16 weeks the burnout and retake risk is the real constraint; the pessimistic band is the honest planning number. **Date flags:** (i) CCAO-F lands on 2027-03-04, after the 2026-12-31 Global Premier fee waiver, so pull it forward if that applies; (ii) AIB-C01 lands after the reported 2027-02-15 beta cut-off (Grade C), so pull it forward if you want the $50 beta price and early-adopter badge; (iii) MLA lands on 2027-01-28, after C02's GA (2027-01-14), which is correct; (iv) the two Gemini badges expire in September 2027, which is fine only because the bootcamp follows immediately.

### R4. Decision gates (stop and assess before buying more)

| Gate | When (Plan A / B′ / C) | Question | Stop rule |
|---|---|---|---|
| **G0** | Before spending (now) | (a) Target segment? (b) Does my employer hold Claude, AWS, Google or Microsoft partner status? (c) Is my signal strong (shipped systems, top-tier employer, OSS) or weak (switcher)? | Strong signal and frontier or startup target: stop after one cloud flagship (AIP-C01 or PAA) and put the remaining hours into shipped work. Weak signal or services/partner target: proceed. |
| **G1** | After AIP-C01 and PAA (2027-02-22 / 2027-02-23 / 2026-12-02) | Did the credentials change screens, interviews or a partner gate? Does a named JD, partner tier or customer contract call for the next credential? | If the next credential's unique share against what you hold is under 30% and no named requirement exists: stop buying and ship a project (at least 40 h) before continuing. |
| **G2** | After the Claude block and AWS FDE (Plan A 2027-04-23) | Which one or two platform branches match your employers' stacks? | Pick at most two branches (Databricks, GitHub, NVIDIA, ML cluster). The rest are Tier 3 and need a named requirement. |
| **G3** | Before any Tier 3 or 4 purchase | Is there a named requirement (JD line, partner rule, client contract)? | No named requirement: treat as learning-only (free study, no exam). |
| **G4** | 60 days before expiry of any 12-month credential | Is it counted for a partner tier, a prerequisite or an active job requirement? | Renew only if yes. Claude renewal is free if done on time; a lapse costs a full-fee retake. |
| **Portfolio parity** | Continuous | For every 40 h of exam study, ship at least 15 h of public work (a deployed agent with evals, traces and a README). | A heuristic of mine (Grade M), not an evidence-based ratio. |

### R5. Minimum credential set to qualify for all three FDE programmes

| Programme | Prerequisite found | Minimum credential(s) |
|---|---|---|
| AWS FDE Validated | Active AWS Associate or Professional certification plus pathway validation | **AIP-C01** (Professional, also satisfies Validated) |
| AWS FDE Advanced | Active **AIP-C01** plus validation across all three pathways | **AIP-C01** |
| Google Gemini Enterprise FDE | One Google Cloud Professional certification, two Gemini Enterprise certifications, an active customer project | **PAA** (or PMLE), **Gemini Deployment**, **Gemini Agent Development** |
| Microsoft FTE (LevelUp) | GH-300, AI-103 (AI-102 reported accepted), AB-100, Project Ready courses, HVE exam | **GH-300**, **AI-103**, **AB-100** |

**Minimum set = 7 exams or badges (AIP-C01, PAA, two Gemini badges, GH-300, AI-103, AB-100) plus the three programme steps.** List fees about **$929** ($300 + $200 + $0 + $0 + $99 + $165 + $165; AB-100's price is an assumption), roughly **306 h** (AIP-C01 78 + PAA 53 + Gemini badges 23 + Google bootcamp 32 + AWS FDE 34 + Microsoft FTE 86). I found no evidence that any programme accepts another vendor's certification: a Claude Architect Professional would not satisfy the Google "Professional certification" prerequisite or the AWS prerequisite (probe 2). Microsoft items fall in the scope gap flagged in the brief.

---

## Alternatives Considered

| Alternative | Verdict | Evidence |
|---|---|---|
| **Portfolio-only, no certifications** | Best default for strong-signal candidates targeting frontier labs and startups. Weaker for switchers and for partner/SI roles with explicit certification lines. | Athey and Palikot: effects near zero for strong resumes; Anthropic FDE postings carry no certification line (B); Deloitte AWS FDE posts do (B). |
| **One flagship per cloud (AIP-C01 plus PAA only)** | The recommended minimum for most engineers; about 130 h. | Highest composite scores; best seeds; both open-enrolment. |
| **Single-vendor depth (all AWS)** | Cheap and coherent but narrows employer fit; AWS has the best pull in the SI segment (Deloitte lists). | AIP-C01, MLA, AIF-C01 are named in postings. |
| **Vendor-neutral stack (NVIDIA plus Databricks)** | Weak on gateway value; no FDE programme counts them. | Phase 3 findings; NVIDIA and Databricks partner linkage not verified. |
| **Partner-first (join a partner employer, certify at their cost)** | Often the highest-value move for a switcher: Claude, Gemini, AWS FDE and Microsoft FTE become reachable and often free or discounted. | Claude eligibility rule (A); Global Premier fee waiver through 2026-12-31 (A); LevelUp vouchers (C). |
| **Governance track (IAPP AIGP, ISACA AAISM/AAIR/AAIA, CompTIA SecAI+)** | Adjacent, not competing: the "agentic governance" category is mostly served by existing governance credentials and by embedded domains in CCAR-P (14%), PAA (15%) and GH-600 (10 to 15%). AIGP's body of knowledge v2.1 (effective 2026-02-02) adds agentic emphasis (B). | S49, S50 |
| **Hours-minimising order** | Rejected as the recommendation: it differs from the curated order by about 4% in hours and ignores access, validity and value timing. | Annealing result (M). |
| **Weighted-completion-time optimiser** | Rejected: it front-loads small, low-value credentials (GH-300, CCDV-F, AIF-C01) because of the shortest-processing-time effect. | Optimiser output (M). |
| **Wait for re:Invent (2026-11-30 to 12-04) before buying Tier 3** | Sensible. AWS says it will show new microcredentials and FDE credentials; Tier 1 purchases do not need to wait. | S25 |

---

## Detailed Findings

### D1. Fact sheets (every enumerated item, plus discovered competitors)

**Reading the tables.** Grades apply to the row's key facts; cells marked *(C)* or *(D)* inside a row override the row grade. **Credly earner counts were not retrievable for any credential**: static Credly pages (AIP-C01 badge fetched) expose no earner counts, and no vendor publishes per-credential counts. The only volume signal is a secondary report of Anthropic's claim of more than 175,000 Claude certifications from professionals at 46,000 firms (S07, Grade B/C, conflicts with a June figure of 10,000+). Pass rates are not published by AWS, Databricks, Anthropic, NVIDIA or Google; community anecdotes exist but I did not find a pass-rate figure I would trust.

#### D1.1 Anthropic Claude (all four exams: Pearson VUE OnVUE or test centre, 120 min, closed book, pass 720/1000, MC plus scenario-based multiple-response, English and Japanese, Credly badges, retakes after 14/30/90 days, four attempts per rolling 12 months; S01, S03: Grade A)

| ID | Credential | Fee | Validity | Items and domains (third-party; S08, Grade C) | Access and partner linkage (Grade A) |
|---|---|---|---|---|---|
| CCAO-F | Claude Certified Associate – Foundations | $99 | 12 months; free non-proctored renewal if on time, full retake if lapsed | About 60 items, 7 domains (weights not retrieved) | Partner-org staff only. **Does not count toward partner eligibility.** Content refresh 2026-12-07. |
| CCDV-F | Claude Certified Developer – Foundations | $125 | 12 months | About 53 items, 8 domains (weights not retrieved) | Partner staff only; counts toward partner tiers. Refresh 2026-12-07. |
| CCAR-F | Claude Certified Architect – Foundations | $125 (was $99 until 2026-06-30) | 12 months | About 60 items, 5 domains: agent architecture and orchestration 27%, Claude Code configuration and workflows 20%, prompt engineering and structured output 20%, tool design and MCP integration 18%, remaining about 15% (by subtraction; context management and reliability) | Partner staff only; counts toward partner tiers. **Not listed in the 2026-12-07 refresh.** |
| CCAR-P | Claude Certified Architect – Professional | $175 | 12 months | About 63 items, 7 domains: solution design 17%, models, prompting and context engineering 13%, integration 19%, evaluation, testing and optimisation 16%, governance, safety and risk 14%, stakeholder communication and lifecycle 14%, developer productivity and operational enablement 7% | Partner staff only; counts toward partner tiers. Refresh 2026-12-07. |

Partner discounts: Registered tier pays list; Select, Preferred and Global Premier get 50% off; Global Premier fees are waived entirely through 2026-12-31 (S03). Tier thresholds of roughly 10 / 100 / 1,000 certified individuals are from secondary summaries of S06 (verify before relying on them).

#### D1.2 AWS

| ID | Credential | Format and length | Fee | Validity | Proctoring | Domains (weights) | Access / linkage | Grade |
|---|---|---|---|---|---|---|---|---|
| AIF-C01 | AI Practitioner (Foundational) | About 65 questions, 90 min, pass 700 | $100 | 3 years | Pearson VUE test centre or online | Fundamentals of AI/ML 20, fundamentals of GenAI 24, applications of foundation models 28, responsible AI 14, security, compliance and governance 14 | Open. Listed in Deloitte's "3 of 6". Does **not** satisfy FDE Validated (Associate or Professional needed). | B |
| AIP-C01 | GenAI Developer – Professional | 75 questions (65 scored), MC/MR, 180 min, pass 750; English, Japanese, Korean, Simplified Chinese | $300 | 3 years (B) | Pearson VUE test centre or online | FM integration, data management and compliance 31, implementation and integration 26, safety, security and governance 20, operational efficiency and optimisation 12, testing, validation and troubleshooting 11 | Open. **Prerequisite for AWS FDE Advanced.** Recommended 2+ years production AWS and 1+ year GenAI. | **A** |
| MLA | ML Engineer – Associate: **C01 retired in English 2026-09-28**; **C02 beta from 2026-09-29, GA 2027-01-14 (AWS blog)** | C01: 65 questions, 130 min, pass 720. C02 beta: 85 questions, 170 min (C) | C01 $150; **C02 beta $75** (C); GA price not announced (I assume $150) | 3 years (recalled) | Pearson VUE | C01: data preparation 28, model development 26, deployment and orchestration 22, monitoring, maintenance and security 24. C02 adds GenAI, LLM and agentic workloads (weights not retrieved) | Open. Qualifies for FDE Validated as an Associate. Named in Deloitte lists. | A (status) / B (C01) / C (C02 detail) |
| AIB-C01 | AI Business Strategist (Business category) | Beta 85 questions, 170 min; standard exam shorter (about 130 min) | **Beta $50; standard $100** | 3 years | Pearson VUE | AI fundamentals and literacy 24, AI strategy and business value 28, governance and responsible AI leadership 24, business readiness, leadership and transformation 24. No AWS-service testing | Open. Business category, so not an Associate or Professional for FDE purposes (my inference from AWS's wording). Early-adopter badge cut-off reported as 2027-02-15 (C). | A / C |

AWS also runs free **"Demonstrated" microcredentials** (MLOps, Agentic AI, Securing Agent Identities, Databases for Agentic AI): timed hands-on challenges in live AWS environments, no MCQ (S19, S20; Grade A/B). Holders of any AWS certification receive a 50% voucher toward the next exam (B; confirm in your AWS Certification account).

#### D1.3 Google Cloud

| ID | Credential | Format and length | Fee | Validity | Proctoring | Domains (weights) | Access / linkage | Grade |
|---|---|---|---|---|---|---|---|---|
| GAIL | Generative AI Leader | MCQ, 90 min, about 50 to 60 questions, no prerequisites | $99 | 3 years | Not verified | Fundamentals about 30, Google Cloud GenAI offerings about 35, techniques to improve output about 20, business strategies about 15 | Open; non-technical | B |
| PAA | Professional Agentic Architect | **Hybrid:** proctored MCQ (GA 2 h; beta 3 h) **plus two hands-on labs** in Google Skills (<5 h, within two months of passing) | **GA $200** (beta $120, 2026-09-08 to 09-30) | **1 year**, with a continuing-education path | MCQ proctored (Pearson); lab proctoring not stated | Low-code agents about 13, coding agents about 17, custom agents about 33, evaluation and deployment about 22, security and governance about 15; MCP and A2A in scope | Open. GA mid-November 2026. Google "Professional" gateway. | **A** |
| PMLE | Professional ML Engineer | About 2 h; MCQ/MR | $200 | **2 years (D, recalled)** | Not verified | 2026 refresh adds GenAI (Model Garden, agent builder) (B); current section weights not retrieved | Open. Google Ambassador AI/ML track requires Cloud Architect plus PMLE (A, S17). Satisfies FDE "Professional" prerequisite (inference). | B / D |
| GEM-DEP | Gemini Enterprise Certified Partner Specialist – Deployment | Three skill badges (challenge labs) | Partner programme; no public fee | **6 months** (example badges; B) | Lab-based; proctoring not stated | Deployment, identity, data connectors, agents in Gemini Enterprise | **Partner-only.** Required for Google FDE. | A (Credly) / B (validity) |
| GEM-AGT | Gemini Enterprise Certified Partner Specialist – Agent Development | Three skill badges (challenge labs) | as above | 6 months | as above | Agent development with ADK, MCP and A2A, sessions and memory, evaluation (from badge descriptions) | **Partner-only.** Required for Google FDE. | A / B |

#### D1.4 Databricks (all proctored via Kryterion Webassessor, $200, 2-year validity, 14-day retake wait, no published passing score; an online dual-camera rule applies to Context Engineer and to the ML exams from 2026-12-01; S30: Grade B)

| ID | Credential | Items and time | Domains (weights) | Notes | Grade |
|---|---|---|---|---|---|
| DBX-GAI | Generative AI Engineer Associate | 45 scored, 90 min | Design applications 14, data preparation 14, application development 30, assembling and deploying 22, governance 8, evaluation and monitoring 12 (guide dated 2026-03-18) | Covers Agent Bricks, MCP servers, AI Gateway | B |
| DBX-CTX | **Context Engineer Associate** | 45 scored, 90 min | Foundations 16, system prompt and instruction design 9, knowledge retrieval and Genie 20, memory with Lakebase and MLflow 18, tools, MCP and agent context 13, compaction 11, multi-agent and long-horizon 13 | GA 2026-07-29; Databricks calls it the industry's first context-engineering certification (S31, vendor claim) | A / B |
| DBX-MLA | Machine Learning Associate (your list says "ML Engineer Associate") | 48 questions, 90 min (guide dated 2025-03-01) | Section weights not retrieved | Naming difference: the official names are Machine Learning Associate and Professional | B |
| DBX-MLP | Machine Learning Professional | 59 questions, 120 min | ML operations 44, model development 44, remainder not retrieved | | B |

#### D1.5 GitHub (Microsoft-run exam programme; Pearson VUE)

| ID | Credential | Format | Fee | Validity | Domains | Notes | Grade |
|---|---|---|---|---|---|---|---|
| GH-300 | GitHub Copilot | About 100 min, pass 700; question count reported as 40 to 65 (conflict) | $99 | **Conflict:** annual free Microsoft renewal (Microsoft Learn) versus 2 years (third party) | Copilot features, responsible AI, prompting, privacy and testing | Prerequisite for Microsoft FTE | B / C |
| GH-600 | Certified Agentic AI Developer | 120 min, pass 700, proctored | **$165** (B) | Annual free renewal assessment (Microsoft Learn) versus 2 years (C) | Architecture and SDLC 15 to 20, tool use and environment 20 to 25, memory and state 10 to 15, evaluation, error analysis and tuning 15 to 20, multi-agent 15 to 20, guardrails and accountability 10 to 15 | GA July 2026 (C). **Beta was unavailable in India**; confirm GA availability before scheduling | **A** (domains) / B |
| GH-700 | Agentic AI Business Professional (**beta**) | 100 min, pass 700, English, proctored | $165 list; **80% off for the first 300 who take it by 2026-11-09** (mirror pages say 2026-11-02) | Not published | Business-level agentic workflow topics | GA expected December 2026 | A / C |

#### D1.6 NVIDIA and AMD

| ID | Credential | Format | Fee | Validity | Proctoring | Domains | Grade |
|---|---|---|---|---|---|---|---|
| NCA-GENL | Generative AI LLMs (Associate) | 60 min, about 50 to 60 questions | $125 | 2 years | Remote proctored (Certiverse) | Core ML 30, software development 24, experimentation 22, data analysis and visualisation 14, trustworthy AI 10 | C |
| NCP-GENL | Generative AI LLMs (Professional) | 120 min, 60 to 70 questions | $200 | 2 years | Remote proctored | Not retrieved (official page not fetched) | C |
| NCP-AAI | Agentic AI (Professional) | 120 min, 60 to 70 questions, English | $200 | 2 years | Remote proctored (Certiverse) | Ten areas: agent architecture 15, agent development 15, evaluation and tuning 13, deployment and scaling 13, cognition, planning and memory 10, knowledge integration 10, NVIDIA platform 7, run and monitor 5, safety and ethics 5, human-AI interaction 5 (**sums to 98%**) | **A** |
| AMD | ROCm Certified Associate | Knowledge-based exam plus practical tasks via AMD AI Academy; Credly badge | **Free** | **24 months** | Not stated | ROCm basics, HIP programming, GPU performance concepts (memory hierarchy, occupancy, streams) | A / B |

#### D1.7 FDE programmes

| Programme | Prerequisites (Grade) | Assessment | Cost | Hours | Notes |
|---|---|---|---|---|---|
| AWS FDE **Validated** | Active AWS Associate or Professional certification; complete all validation activities in at least one pathway; required points across Ground, Orchestrate and Prove (A: S20) | Hands-on validation in AWS-provisioned environments, not solely MCQ | Free via Skill Builder | About 8 h (my estimate; a practitioner write-up says about 6 h, C) | Partner-linked; individual access to be verified |
| AWS FDE **Advanced** | Active **AIP-C01** plus validation across all three pathways (A) | as above | Free | About 26 h (M) | |
| Google **Gemini Enterprise FDE** enablement | One Google Cloud Professional certification, two Gemini Enterprise certifications, an active assignment to a Gemini Enterprise customer project (B: S15) | Four-day programme | Not published | About 32 h (M) | Partner nomination |
| Microsoft **FTE LevelUp** | GH-300, AI-103 (AI-102 reported accepted), AB-100 (B: S37) | Three milestones, Project Ready courses, HVE exam of at least 80% | Partner vouchers (C) | About 86 h (B) | **Out of scope; mapped as a gap** |
| Anthropic **Claude Frontier Academy** (discovered) | Employer nomination; Claude Resident Engineer badge, 12-week residency, then Claude Frontier Deployed Engineer badge expected early 2027 (B: S07) | Residency | $100M programme, 10,000 FDE target by end 2027 (B) | n/a | No individual route |

#### D1.8 Discovered competing or adjacent credentials

| Credential | Why it matters | Finding | Grade |
|---|---|---|---|
| AWS "Demonstrated" microcredentials | Hands-on, free, pre-date PAA | Four exist; timed live-environment challenges | A/B |
| IAPP AIGP | Mature AI-governance credential | $649 members / $799 non-members, about 100 questions, body of knowledge v2.1 effective 2026-02-02 adds agentic emphasis | B |
| ISACA AAISM, AAIA, AAIR | AI security, audit and risk | AAISM requires CISM or CISSP; AAIR launched April 2026 | A/B |
| CompTIA SecAI+ | AI security | Launched 2026-02-17, about $298 | B |
| Microsoft AI-103, AB-100, AI-102 | Gateways to Microsoft FTE | Not assessed (excluded) | gap |
| OpenAI, Salesforce Agentforce, Snowflake, Oracle OCI GenAI, IBM watsonx, ServiceNow | Possible competitors | **Not researched in depth (gap)** | n/a |

Grade note: I did not find any dedicated "agentic AI governance" vendor credential. Governance is covered inside CCAR-P (14%), PAA (15%), GH-600 (10 to 15%), AIB-C01 (24%) and by the governance bodies' credentials above.

---

### D2. Knowledge-overlap matrix (Grade M, anchored on A/B blueprints)

**Method.** I mapped each blueprint's domain weights onto 14 topics (T1 to T14), allocating weight to vendor-specific implementation (T11) where a domain is product-configuration-heavy. For source credential X and target Y, coverage of topic t is

`cov = min(1, (x_t × hours_X × depth_X) / (y_t × hours_Y))`, multiplied by a cross-vendor factor (T11 = 0, T12 = 0.5, T14 = 0.4, all else 1.0) or a same-vendor factor (T11 = 0.5, all else 1.0). Coverage from several credentials combines as 1 minus the product of (1 − cov). Overlap(X to Y) is the Y-weighted average of cov over topics, and study hours given prior knowledge are `hours_Y × max(0.30, 1 − 0.65 × overlap)`. The 0.65 transfer efficiency and 0.30 floor are assumptions (sensitivity in R2). Depth factors: Foundational or business 0.6, Associate 0.7 to 0.8, "Foundations" scenario exams 0.8, Professional 1.0.

**Reading the matrix.** Row = what you studied first; column = target; cell = percentage of the target's blueprint effectively already covered. It is **directional**: PAA covers 62% of AIP-C01 but AIP-C01 covers 58% of PAA. Treat every cell as ±15 points.


| X ↓ studied first / Y → target | AIP-C01 | PAA | CCAR-P | CCAR-F | CCDV-F | PMLE | GEM-AGT | MLA-C0x | GEM-DEP | GH-300 | DBX-GAI | GH-600 | DBX-CTX | DBX-MLP | NCP-AAI | NCP-GENL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AIP-C01** | — | 58 | 68 | 49 | 70 | 24 | 45 | 19 | 55 | 35 | 64 | 47 | 44 | 12 | 65 | 37 |
| **PAA** | 62 | — | 78 | 64 | 72 | 32 | 82 | 6 | 78 | 55 | 63 | 68 | 45 | 12 | 76 | 32 |
| **CCAR-P** | 46 | 49 | — | 72 | 84 | 20 | 65 | 6 | 40 | 51 | 48 | 57 | 38 | 12 | 59 | 28 |
| **CCAR-F** | 23 | 25 | 48 | — | 76 | 6 | 58 | 1 | 23 | 41 | 27 | 38 | 41 | 1 | 31 | 12 |
| **CCDV-F** | 22 | 21 | 40 | 48 | — | 11 | 39 | 2 | 24 | 41 | 30 | 23 | 30 | 5 | 25 | 14 |
| **PMLE** | 24 | 30 | 30 | 13 | 33 | — | 22 | 73 | 52 | 35 | 37 | 12 | 17 | 60 | 32 | 51 |
| **GEM-AGT** | 12 | 20 | 26 | 31 | 33 | 6 | — | 3 | 42 | 31 | 18 | 27 | 26 | 0 | 21 | 3 |
| **MLA-C0x** | 11 | 3 | 5 | 2 | 4 | 43 | 10 | — | 13 | 20 | 6 | 6 | 0 | 35 | 5 | 26 |
| **GEM-DEP** | 12 | 16 | 13 | 10 | 15 | 12 | 36 | 6 | — | 20 | 19 | 13 | 16 | 0 | 16 | 9 |
| **GH-300** | 4 | 5 | 8 | 9 | 14 | 4 | 13 | 3 | 8 | — | 6 | 12 | 3 | 0 | 5 | 4 |
| **DBX-GAI** | 29 | 27 | 32 | 25 | 49 | 18 | 31 | 4 | 42 | 33 | — | 22 | 42 | 15 | 39 | 22 |
| **GH-600** | 28 | 35 | 51 | 54 | 45 | 8 | 66 | 6 | 40 | 72 | 31 | — | 33 | 6 | 46 | 13 |
| **DBX-CTX** | 18 | 18 | 25 | 37 | 36 | 8 | 40 | 0 | 35 | 15 | 34 | 25 | — | 3 | 29 | 11 |
| **DBX-MLP** | 14 | 13 | 20 | 3 | 18 | 69 | 0 | 68 | 0 | 0 | 37 | 11 | 10 | — | 19 | 38 |
| **NCP-AAI** | 45 | 50 | 63 | 48 | 54 | 23 | 53 | 6 | 55 | 35 | 59 | 56 | 44 | 12 | — | 37 |
| **NCP-GENL** | 29 | 24 | 34 | 25 | 40 | 40 | 10 | 27 | 28 | 35 | 39 | 15 | 21 | 26 | 41 | — |


**Domain probe 3 detail (Databricks):** GenAI Engineer to Context Engineer **42%**; Context Engineer to GenAI Engineer **34%**. The Context Engineer blueprint puts about 36% on memory architecture, compaction and context-failure design that the GenAI Engineer blueprint barely touches. A community exam-note repo (C) frames the Context Engineer exam as a roughly two-week sprint for someone who already holds the GenAI Engineer credential, consistent with 35 to 50% rather than 80% overlap.

**Limits of the matrix.** (1) Topic mapping is mine. (2) CCDV-F, GH-300, GH-700, the Gemini badges and NCP-GENL use estimated weights because official weights were not retrieved; GH-600 uses the midpoints of Microsoft's ranges; PMLE uses a recalled blueprint (D). (3) NCP-AAI's weights were normalised from 98% to 100%. (4) Depth within a topic is not modelled beyond the hours-ratio. (5) "Covered" means knowledge, not exam-specific recall such as product names and limits, which is why the 0.30 floor exists.

#### Topic taxonomy and parameters


| Topic | Meaning | Cross-vendor transfer factor |
|---|---|---|
| T1 | LLM fundamentals, prompting, structured output | 1.0 |
| T2 | RAG, retrieval, vector search, GenAI data prep | 1.0 |
| T3 | Agent design & orchestration | 1.0 |
| T4 | Tool use, MCP/A2A, integration protocols | 1.0 |
| T5 | Memory, state, context management | 1.0 |
| T6 | Evaluation, testing, observability (GenAI) | 1.0 |
| T7 | Deployment, scaling, cost/latency, lifecycle (LLMOps) | 1.0 |
| T8 | Safety, security, governance, responsible AI | 1.0 |
| T9 | Classical ML lifecycle | 1.0 |
| T10 | MLOps (pipelines, CI/CD, drift) | 1.0 |
| T11 | Vendor-platform implementation specifics | 0 (never transfers across vendors) |
| T12 | Coding-agent & SDLC tooling | 0.5 (concepts transfer, product details do not) |
| T13 | Business strategy, ROI, adoption, stakeholders | 1.0 |
| T14 | Accelerated compute / GPU programming / model optimisation | 0.4 (GPU concepts transfer, APIs differ) |


#### Credential topic weights (percent of blueprint; the model's input)


| ID | Depth | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | T14 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AIP-C01 | 1.0 | 6 | 14 | 9 | 8 |  | 9 | 10 | 21 |  |  | 23 |  |  |  | 100 |
| PAA | 1.0 | 3 | 11 | 13 | 8 | 3 | 9 | 8 | 12 |  |  | 21 | 12 |  |  | 100 |
| CCAR-P | 1.0 | 7 |  | 17 | 12 | 6 | 10 | 12 | 14 |  |  | 7 | 7 | 8 |  | 100 |
| CCAR-F | 0.8 | 20 |  | 22 | 14 | 10 | 3 |  | 2 |  |  | 9 | 20 |  |  | 100 |
| CCDV-F | 0.8 | 18 |  | 14 | 18 |  | 6 | 12 | 4 |  |  | 10 | 18 |  |  | 100 |
| PMLE | 1.0 | 4 | 4 |  |  |  | 4 | 8 | 4 | 32 | 26 | 18 |  |  |  | 100 |
| GEM-AGT | 0.8 |  |  | 20 | 15 | 15 |  |  | 10 |  |  | 25 | 15 |  |  | 100 |
| MLA | 0.8 |  |  |  |  |  |  |  | 6 | 40 | 28 | 26 |  |  |  | 100 |
| GEM-DEP | 0.8 |  | 15 | 10 | 10 |  |  |  | 20 |  |  | 45 |  |  |  | 100 |
| GH-300 | 0.7 | 15 |  |  |  |  |  |  | 20 |  |  | 25 | 40 |  |  | 100 |
| DBX-GAI | 0.8 | 7 | 16 | 12 | 4 |  | 9 | 10 | 6 |  |  | 36 |  |  |  | 100 |
| GH-600 | 0.85 |  |  | 20 | 8 | 12 | 16 |  | 11 |  |  | 16 | 17 |  |  | 100 |
| DBX-CTX | 0.85 | 13 | 12 | 10 | 10 | 36 |  |  |  |  |  | 19 |  |  |  | 100 |
| DBX-MLP | 1.0 |  |  |  |  |  | 6 | 6 |  | 28 | 30 | 30 |  |  |  | 100 |
| NCP-AAI | 0.9 | 5.1 | 10.2 | 26.5 | 5.1 | 6.1 | 16.3 | 12.2 | 8.2 |  |  | 7.1 |  |  | 3.1 | 100 |
| NCP-GENL | 0.9 | 20 | 5 |  |  |  | 8 | 25 | 5 | 22 |  | 5 |  |  | 10 | 100 |
| AIF-C01 | 0.6 | 30 | 8 |  |  |  | 6 | 4 | 22 | 14 |  | 16 |  |  |  | 100 |
| GAIL | 0.6 | 28 | 6 |  |  |  | 3 |  | 3 | 10 |  | 35 |  | 15 |  | 100 |
| DBX-MLA | 0.8 |  |  |  |  |  |  |  |  | 44 | 16 | 40 |  |  |  | 100 |
| AIB-C01 | 0.6 | 14 |  | 4 |  |  |  |  | 24 | 6 |  |  |  | 52 |  | 100 |
| NCA-GENL | 0.7 | 20 | 6 |  |  |  | 10 | 4 | 10 | 46 |  |  |  |  | 4 | 100 |
| GH-700 | 0.7 |  |  | 15 |  |  |  |  | 15 |  |  | 25 | 25 | 20 |  | 100 |
| AMD | 0.6 |  |  |  |  |  |  |  |  | 5 |  | 25 |  |  | 70 | 100 |
| CCAO-F | 0.6 | 35 |  |  |  |  | 10 |  | 10 |  |  | 20 |  | 25 |  | 100 |


---

### D3. Composite scoring (Grade M on A/B evidence)

**Rubrics.**
- **W1 hiring signal (0 to 10)** = weighted mean of five employer-segment scores (0 to 10 each). Segment weights are my assumption: frontier lab 0.10, AI startup 0.15, enterprise product 0.25, IT services/GCC 0.30, partner/SI 0.20, reflecting where certification-linked demand showed up in T0-11 F7 and this session. Segment scores are anchored on: Deloitte AWS FDE postings (S27, S28, S29), the Bounteous FDE posting (S09), partner-tier headcount rules (S03, S06), FDE prerequisites (S20, S15, S37), the absence of any certification line in Anthropic FDE postings (S10), and survey data (S44 to S46). A credential with no job-posting or partner evidence is capped at 4 even in services.
- **W2 knowledge utility (0 to 10):** does preparation teach production skills (hands-on labs, MCP and A2A, evaluation, security, context management) rather than exam recall?
- **W3 gateway value (0 to 10):** does it unlock an FDE programme, a partner-tier count, or employer-specific roles? Anchors: AIP-C01 is the named prerequisite of AWS FDE Advanced; CCAO-F explicitly does not count toward partner eligibility; Gemini badges are named prerequisites of Google FDE.
- **W4 rigour and credibility (0 to 5):** proctored +1.5; level (foundational or associate +0.5, "Foundations" scenario exams +1.0, professional +1.5); scenario or multi-response +0.5; unproctored hands-on component +1.0; verifiable badge +0.5; cap 5. PAA scores highest (4.5); AMD lowest (1.5; proctoring not stated).
- **W5 cost efficiency (0 to 5):** `5 × clamp(ln(3500/c) / ln(3500/150), 0, 1)` where c = annualised three-year cost (exam fee + likely hours × $40/h + renewals at their cost). Renewal assumptions: Claude 4 h free; GitHub 2 h free; PAA 10 h free (assumed); Gemini badges re-earned at half hours; all others retake at fee plus half the hours. The $40/h is an assumption; $20/h and $80/h leave the top six unchanged.

**Composite = W1 + W2 + W3 + W4 + W5 (maximum 40).** "Unique share" is 1 minus the highest overlap from any higher-ranked credential: a low value means the credential is mostly redundant given what a higher-ranked one teaches.


| # | ID | W1 hiring | W2 utility | W3 gateway | W4 rigour | W5 cost | **Composite /40** | Startup-wt | Services-wt | Unique share* | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AIP-C01 | 6.2 | 8 | 9 | 4.0 | 1.8 | **29.1** | 26.8 | 30.6 | 100% | 1 |
| 2 | PAA | 5.5 | 9 | 8 | 4.5 | 1.5 | **28.5** | 26.5 | 29.8 | 42% | 1 |
| 3 | CCAR-P | 5.5 | 7 | 7 | 4.0 | 2.3 | **25.8** | 23.6 | 27.6 | 22% | 2 (gated) |
| 4 | CCAR-F | 5.5 | 8 | 6 | 3.5 | 2.7 | **25.7** | 23.5 | 27.5 | 28% | 1 (gated) |
| 5 | CCDV-F | 4.9 | 8 | 6 | 3.5 | 3.0 | **25.4** | 23.3 | 27.0 | 16% | 3 (gated) |
| 6 | PMLE | 5.5 | 7 | 7 | 3.5 | 1.2 | **24.3** | 22.4 | 25.4 | 68% | 2 |
| 7 | GEM-AGT | 4.5 | 8 | 7 | 2.5 | 1.8 | **23.9** | 21.3 | 26.0 | 18% | 2 (partner) |
| 8 | MLA | 5.4 | 7 | 6 | 3.0 | 2.4 | **23.8** | 21.7 | 25.0 | 27% | 2 |
| 9 | GEM-DEP | 4.5 | 6 | 7 | 2.5 | 2.1 | **22.1** | 19.6 | 24.2 | 22% | 2 (partner) |
| 10 | GH-300 | 4.2 | 4 | 6 | 2.5 | 4.3 | **21.0** | 18.9 | 22.3 | 45% | 2/3 |
| 11 | DBX-GAI | 5.1 | 7 | 3 | 3.0 | 2.0 | **20.1** | 18.5 | 21.2 | 36% | 2 |
| 12 | GH-600 | 3.9 | 7 | 3 | 3.5 | 2.4 | **19.8** | 18.5 | 20.6 | 32% | 3 |
| 13 | DBX-CTX | 4.3 | 7 | 3 | 3.0 | 2.2 | **19.6** | 18.3 | 20.4 | 55% | 3 |
| 14 | DBX-MLP | 4.6 | 7 | 3 | 3.5 | 1.0 | **19.1** | 17.8 | 19.9 | 40% | 3 |
| 15 | NCP-AAI | 3.9 | 7 | 2 | 3.5 | 1.7 | **18.0** | 17.1 | 18.6 | 24% | 3 |
| 16 | NCP-GENL | 3.9 | 7 | 2 | 3.5 | 1.5 | **17.8** | 16.9 | 18.4 | 49% | 3 |
| 17 | AIF-C01 | 4.2 | 3 | 3 | 2.5 | 4.4 | **17.0** | 15.0 | 18.3 | 18% | 3 |
| 18 | GAIL | 3.2 | 3 | 2 | 2.5 | 5.0 | **15.7** | 14.2 | 16.6 | 32% | 4 |
| 19 | DBX-MLA | 3.6 | 5 | 2 | 3.0 | 2.0 | **15.6** | 14.3 | 16.4 | 20% | 4 |
| 20 | AIB-C01 | 2.2 | 3 | 2 | 2.5 | 4.4 | **14.1** | 12.9 | 14.7 | 29% | 4 |
| 21 | NCA-GENL | 2.9 | 4 | 2 | 2.5 | 2.8 | **14.1** | 13.2 | 14.7 | 0% | 4 |
| 22 | GH-700 | 2.0 | 3 | 2 | 2.5 | 4.2 | **13.7** | 12.6 | 14.4 | 32% | 4 |
| 23 | AMD | 0.9 | 5 | 1 | 1.5 | 4.3 | **12.7** | 12.5 | 12.8 | 76% | 4 |
| 24 | CCAO-F | 2.1 | 2 | 1 | 3.0 | 4.2 | **12.4** | 11.5 | 13.0 | 10% | 4 |


**Segment scores behind W1 (0 to 10; judgement anchored as above):**


| ID | Frontier lab | AI startup | Enterprise product | IT services/GCC | Partner/SI | W1 |
|---|---|---|---|---|---|---|
| AIP-C01 | 1 | 3 | 6 | 8 | 9 | 6.2 |
| PAA | 1 | 3 | 5 | 7 | 8 | 5.5 |
| CCAR-P | 1 | 3 | 3 | 8 | 9 | 5.5 |
| CCAR-F | 1 | 3 | 3 | 8 | 9 | 5.5 |
| CCDV-F | 1 | 2 | 3 | 7 | 8 | 4.9 |
| PMLE | 1 | 3 | 6 | 7 | 7 | 5.5 |
| GEM-AGT | 0 | 1 | 2 | 7 | 9 | 4.5 |
| MLA | 1 | 2 | 6 | 7 | 7 | 5.4 |
| GEM-DEP | 0 | 1 | 2 | 7 | 9 | 4.5 |
| GH-300 | 0 | 1 | 4 | 6 | 6 | 4.2 |
| DBX-GAI | 1 | 3 | 5 | 7 | 6 | 5.1 |
| GH-600 | 1 | 2 | 4 | 5 | 5 | 3.9 |
| DBX-CTX | 1 | 3 | 4 | 6 | 5 | 4.3 |
| DBX-MLP | 1 | 3 | 5 | 6 | 5 | 4.6 |
| NCP-AAI | 1 | 3 | 4 | 5 | 4 | 3.9 |
| NCP-GENL | 1 | 3 | 4 | 5 | 4 | 3.9 |
| AIF-C01 | 0 | 1 | 4 | 6 | 6 | 4.2 |
| GAIL | 0 | 1 | 3 | 5 | 4 | 3.2 |
| DBX-MLA | 0 | 2 | 4 | 5 | 4 | 3.6 |
| AIB-C01 | 0 | 0 | 3 | 3 | 3 | 2.2 |
| NCA-GENL | 0 | 2 | 3 | 4 | 3 | 2.9 |
| GH-700 | 0 | 0 | 2 | 3 | 3 | 2.0 |
| AMD | 0 | 1 | 1 | 1 | 1 | 0.9 |
| CCAO-F | 0 | 1 | 2 | 3 | 3 | 2.1 |


**Sensitivity (Grade M).** Varying only the W1 segment weights (startup-heavy 0.25 / 0.40 / 0.20 / 0.075 / 0.075 or services-heavy 0 / 0.05 / 0.15 / 0.45 / 0.35) moves no credential by more than one rank (Spearman 0.997 and 0.998). That stability is partly an artefact: W2 to W5 were held fixed. Perturbing those instead: dropping W3 gives Spearman 0.949 (maximum shift 6; top five become PAA, AIP-C01, CCAR-F, CCDV-F, CCAR-P); doubling W2 gives 0.976; dropping W5 gives 0.980 and swaps PMLE in for CCDV-F; W1 alone gives 0.945 and also swaps PMLE in. **AIP-C01 and PAA are the top two in every variant I tried;** the order inside the Claude trio and PMLE's rank depend on how much you weight gateway value and cost.

---

### D4. FDE prerequisite graph

```
AWS      any active AWS Associate or Professional cert (e.g. MLA-C02, SAA, AIP-C01)
           └─► + pathway validation (Ground / Orchestrate / Prove, free, hands-on) ─► AWS FDE VALIDATED
         active AIP-C01
           └─► + validation across ALL three pathways ─────────────────────────────► AWS FDE ADVANCED

GOOGLE   one Google Cloud PROFESSIONAL cert (PAA | PMLE | other)
         + Gemini Enterprise Partner Specialist: Deployment   (6-month badge)
         + Gemini Enterprise Partner Specialist: Agent Dev    (6-month badge)
         + active assignment to a Gemini Enterprise customer project
           └─► 4-day FDE enablement programme (partner-nominated) ─────────────────► GOOGLE FDE

MICROSOFT GH-300 + AI-103 (AI-102 reported accepted) + AB-100
         + Project Ready courses + HVE exam >= 80% (3 milestones, about 86 h)
           └─► Frontier Transformation Engineer (LevelUp) ─────────────────────────► MICROSOFT FTE

ANTHROPIC employer in Claude Partner Network ─► employer nomination ─► Claude Resident Engineer badge
           └─► 12-week residency ─► Claude Frontier Deployed Engineer badge (expected early 2027)

CROSS-VENDOR EDGES: none found (AWS and Microsoft name their own exams; Google's release names Google credentials).
```

| Credential | Unlocks | Gate type |
|---|---|---|
| AIP-C01 | AWS FDE Validated and Advanced; Deloitte-style SI job lists | Hard prerequisite |
| Any AWS Associate (MLA-C02, SAA) | AWS FDE Validated | Hard prerequisite |
| PAA or PMLE | Google FDE (Professional certification) | Hard prerequisite (per partner release) |
| Gemini Deployment and Agent Development badges | Google FDE | Hard prerequisites (six-month shelf life) |
| GH-300, AI-103/AI-102, AB-100 | Microsoft FTE | Hard prerequisites |
| CCAR-F, CCAR-P, CCDV-F | Partner-tier headcount; employer eligibility for Anthropic programmes | Soft (employer-level) |
| CCAO-F | Nothing (explicitly excluded from partner eligibility) | None |
| Everything else | No FDE or partner gate found | None |

---

### D5. Cost model (USD and INR) and hours

**Assumptions.** USD/INR **94.58** (rupee settled at 94.58 on 2026-11-04, PTI via HDFC Sky; S48, Grade B). GST **18%** is an assumption (Grade D): the effective INR price depends on each vendor's India invoicing, which I did not verify. Time valued at $40/h (assumption). Fees are list prices; Microsoft vouchers, Claude partner discounts and AWS vouchers are shown separately. FDE programmes carry no exam fee.


| ID | Fee USD (list) | Fee INR incl. 18% GST* | Hours (low / likely / high) | Overlap-optimised hrs in curated stack order | Validity (months) | 3-yr cost incl. renewals + $40/h time |
|---|---|---|---|---|---|---|
| AIP-C01 | $300 | ₹33,481 | 50 / 75 / 110 | 75.0 | 36 | $3,300 |
| PAA | $200 | ₹22,321 | 50 / 80 / 120 | 49.6 | 12 | $4,200 |
| CCAR-P | $175 | ₹19,531 | 35 / 50 / 70 | 21.5 | 12 | $2,495 |
| CCAR-F | $125 | ₹13,951 | 25 / 38 / 55 | 20.3 | 12 | $1,965 |
| CCDV-F | $125 | ₹13,951 | 18 / 28 / 40 | 10.3 | 12 | $1,565 |
| PMLE | $200 | ₹22,321 | 50 / 75 / 110 | 58.9 | 24 | $4,900 |
| GEM-AGT | $0 | ₹0 | 16 / 24 / 36 | 9.3 | 6 | $3,360 |
| MLA | $150 | ₹16,741 | 35 / 55 / 85 | 23.9 | 36 | $2,350 |
| GEM-DEP | $0 | ₹0 | 14 / 20 / 30 | 8.0 | 6 | $2,800 |
| GH-300 | $99 | ₹11,049 | 6 / 11 / 18 | 5.9 | 12 | $699 |
| DBX-GAI | $200 | ₹22,321 | 28 / 42 / 60 | 24.5 | 24 | $2,920 |
| GH-600 | $165 | ₹18,415 | 30 / 48 / 75 | 21.8 | 12 | $2,245 |
| DBX-CTX | $200 | ₹22,321 | 22 / 36 / 52 | 18.9 | 24 | $2,560 |
| DBX-MLP | $200 | ₹22,321 | 55 / 85 / 120 | 39.6 | 24 | $5,500 |
| NCP-AAI | $200 | ₹22,321 | 35 / 55 / 85 | 23.0 | 24 | $3,700 |
| NCP-GENL | $200 | ₹22,321 | 40 / 62 / 90 | 25.9 | 24 | $4,120 |
| AIF-C01 | $100 | ₹11,160 | 8 / 14 / 24 | 5.3 | 36 | $660 |
| GAIL | $99 | ₹11,049 | 4 / 7 / 12 | 2.8 | 36 | $379 |
| DBX-MLA | $200 | ₹22,321 | 28 / 42 / 60 | 20.5 | 24 | $2,920 |
| AIB-C01 | $100 | ₹11,160 | 8 / 14 / 20 | 7.0 | 36 | $660 |
| NCA-GENL | $125 | ₹13,951 | 15 / 26 / 40 | 9.1 | 24 | $1,810 |
| GH-700 | $165 | ₹18,415 | 6 / 10 / 16 | 4.0 | 12 | $725 |
| AMD | $0 | ₹0 | 6 / 12 / 20 | 9.7 | 24 | $720 |
| CCAO-F | $99 | ₹11,049 | 5 / 8 / 12 | 2.9 | 12 | $739 |
| **TOTAL (24)** | **$3,427** | **₹382,468** | **589 / 917 / 1360** | **498** | | |


*Fee INR = USD fee × 94.58 × 1.18 (assumed GST).

**Scenario totals (fees only, list):**

| Scenario | Credentials | List fees (USD) | INR incl. assumed GST | Notes |
|---|---|---|---|---|
| Everything on the list (24) | 24 | **$3,427** | **₹3.82 lakh** | Excludes Microsoft exams |
| Same, with AWS repeat voucher in curated order (AIP-C01 first) | 24 | $3,252 | ₹3.63 lakh | 50% off MLA, AIF, AIB |
| Same, with AIF-C01 first | 24 | $3,152 | ₹3.52 lakh | AIF, then 50% off AIP, MLA, AIB; costs about 6 to 9 extra early hours |
| Plan A core (16) | 16 | $2,439 ($2,314 with voucher) | ₹2.72 lakh (₹2.58 lakh) | |
| Plan B (7) | 7 | $1,249 ($1,024 with voucher) | ₹1.39 lakh (₹1.14 lakh) | AIF first |
| Claude four exams | 4 | $524 | ₹0.58 lakh | $262 at Select tier or above; $0 at Global Premier through 2026-12-31 |
| Minimum FDE set (7 exams or badges) | 7 | about $929 | about ₹1.04 lakh | AB-100 price assumed $165; LevelUp vouchers may cut Microsoft exams |

**Hours.** Naive 917 (589 low, 1,360 high) versus 498 overlap-adjusted in curated order; with FDE add-ons 983 versus about 564. **Time dominates fees roughly 6 to 1:** 498 h at $40/h is about $19,900 against $3,427 in fees. The decision is mostly about hours.

---

### D6. Hiring-signal audit

**What I could and could not do.** Live LinkedIn, Indeed, Wellfound and Ashby searches with counts were not possible with the tools available; I sampled postings retrieved through search. Recruiter Boolean-string audits: **searched, nothing found.** No per-credential job-posting share above 10% was verified (consistent with T0-11 F4, which I could neither confirm nor refute at scale).

| Employer segment | Posting or evidence | Credential mention | Strength | Grade |
|---|---|---|---|---|
| Partner/SI | Deloitte US "Forward Deployed Engineer – AWS" (S27) | "At least 3 of 6" certifications from a list including Cloud Practitioner, Solutions Architect Associate, AIF-C01 and AIP-C01 (the Lead FDE post's list also names MLA-C01 and Data Engineer Associate) | Listed qualification (required/preferred label not visible) | B |
| Partner/SI | Deloitte US "Senior AWS Forward Deployed Engineer – GPS" (S28) | One or more Associate-level certifications (SAA, Developer, SysOps, Data Engineer, MLA) **and** one or more Professional-level (SAP, DevOps Pro, **GenAI Developer – Professional**) | Listed qualification | B |
| Partner/SI | Deloitte "Project GenAI Engineer III" (S29) | AWS Certified AI Practitioner among listed skills | Listed skill | B |
| Partner/SI | Bounteous Lead FDE (S09) | "Anthropic certification, such as Claude Certified Architect (Foundations or Professional)" | Preferred | B |
| Frontier lab | Anthropic FDE postings, eight or more locations (S10) | None | None | B |
| Partner/SI (Google) | Partner FDE posting for Gemini Enterprise (retrieved via search; URL not retained) | Google Cloud certification described as a strong differentiator; PMLE preferred | Preferred | C |
| Survey | 2025 survey of 1,200 hiring managers reported by Rework (S46) | 23% actively screen for AI certifications | Weak | C |
| Survey | KDnuggets (S44), InfoWorld citing a WGU 2026 report (S45), Dice (S47) | Portfolio and hands-on experience valued above certifications; 41% look at hands-on experience versus 34% at certifications (WGU) | Weak | C |
| Causal | Athey and Palikot RCT (S43) | Certificates raise employment mainly for weak-signal candidates | Narrow external validity | A |

**Reading it.** Hiring-signal evidence for vendor AI certifications is **institutional**, not market-wide: SI and partner firms list them because partner tiers, FDE gates and client assurance count certified headcount. For employers that hire on evidence of building, there is no sign of certification screening in what I retrieved.

**Gateway credentials (unlock something real):** AIP-C01 (AWS FDE Advanced); any AWS Associate (AWS FDE Validated); a Google Professional certification plus two Gemini badges (Google FDE); GH-300, AI-103 and AB-100 (Microsoft FTE); CCAR-F, CCAR-P and CCDV-F (Claude partner-tier headcount; nominated programmes through employers).

**T0-11 findings re-checked.** F4 (no certification above 10% of JDs): consistent, not verifiable at scale here. F5 (premium for non-certified AI skills versus certifications; combinations outperform): not re-verified. F6 (RCT): verified as arXiv 2405.00247, but the effect sizes I retrieved were +1.0 pp (6%) on new employment and +1.2 pp for related jobs, not +11 pp; the 15 to 20 point effects belong to the resume experiment for weak resumes. F7 (partner programmes create institutional demand): **strongly confirmed** (Claude tiers, AWS FDE, Google FDE, Microsoft FTE). F9 (no hands-on proctored AI exams): **superseded** (see probe 1).

---

### D7. Domain probes

| # | Probe | Answer | Grade |
|---|---|---|---|
| 1 | First GenAI certification with proctored hands-on labs? Google PAA? | **Not verified, and probably not.** PAA is a confirmed hybrid (proctored MCQ plus two Google Skills labs). But hands-on credentials pre-date it (AWS Demonstrated microcredentials, Gemini partner badges, AWS FDE of 2026-10-01), and no source says PAA's labs are proctored. The defensible claim: PAA is the first **professional-tier certification** I found that requires labs after a proctored exam. | A for facts; absence of evidence for "first" and proctoring |
| 2 | Do any FDE programmes accept another vendor's credential? Can CCAR-P satisfy the Google "1 professional certification" prerequisite? | **No evidence of any cross-vendor acceptance.** AWS names AWS certifications only; Google's partner release names a Google Cloud Professional certification; Microsoft names its own exams. CCAR-P would not satisfy Google's or AWS's prerequisite (inference from wording). | A/B |
| 3 | Databricks Context Engineer versus GenAI Engineer overlap: 80% or 20%? | **About 42% (GenAI Engineer to Context Engineer) and 34% (reverse).** Roughly 36% of the Context Engineer blueprint is memory, compaction and context-failure design absent from the GenAI Engineer blueprint. | M, anchored on A/B blueprints |
| 4 | Does GH-600 cover MCP and A2A at Google PAA's depth? | **No.** GH-600 covers MCP server configuration (servers as tools, the GitHub remote server, registries, allow lists) inside a GitHub/Copilot frame and does not mention A2A. PAA names MCP and A2A for agent orchestration and also touches coding agents with MCP servers. | A (S33, S12) |
| 5 | How do Claude certifications compare with vendor-neutral credentials; are they recognised outside the Anthropic partner ecosystem? | **Recognition outside the partner ecosystem is unproven.** Access is partner-gated (A); the only posting naming them is from a partner firm (B); Anthropic's own FDE postings do not mention certifications (B). Credly's 2026 top-AI-badge roundup lists CCAR-P, so the badges are visible but not demand-validated (B). Vendor-neutral credentials (NVIDIA, Databricks) are open but have no FDE or partner gateway. | A/B |
| 6 | Is AMD ROCm Associate useful beyond AMD? | The skills (HIP, memory hierarchy, occupancy, streams) transfer conceptually to CUDA work (my model assumes 40% cross-vendor transfer for GPU topics); **I found no employer outside AMD's ecosystem naming the credential.** I did not run a ROCm-specific job-posting audit. It is free, so "learning-only" costs hours, not money. | C / absence of evidence |
| 7 | Total cost (USD and INR) and hours for everything; optimised total? | **$3,427 list ($3,252 to $3,152 with AWS repeat vouchers), about ₹3.82 lakh (₹3.52 to 3.63 lakh) at ₹94.58/USD with assumed 18% GST. Hours: 917 naive, about 498 overlap-adjusted (480 best found), 983 and 564 with FDE add-ons.** Microsoft exams excluded. | M; fees A/B |
| 8 | Minimum credential set for all three FDE programmes? | AIP-C01, PAA, two Gemini badges, GH-300, AI-103, AB-100 (7 exams or badges), about $929 and about 306 h. See R5. | A/B |
| 9 | Which credentials have the shortest validity; how does it change sequencing? | Gemini badges **6 months** (B); Claude, PAA and GitHub **12 months** (A; GitHub conflicting). Place short-validity items last or just-in-time; the Claude cluster inside a single 12-month window; renewals are free for Claude (on time) and GitHub, otherwise a retake. | A/B |
| 10 | Q1 2027 launches that change the ranking? | **MLA-C02 GA 2027-01-14** (A); Claude Frontier Deployed Engineer badges early 2027 (B, nomination-only); AMD Professional ("coming soon") and Expert (early 2027) (A); GH-700 GA December 2026 (A/B); PAA GA mid-November 2026 and Claude exam content refresh 2026-12-07 (A); re:Invent 2026-11-30 to 12-04 may add microcredentials and FDE credentials (A). AIB-C01 beta cut-off reported 2027-02-15 (C). **Not searched:** NVIDIA GTC, Google Cloud Next, Microsoft Build announcements (gap). Likely effect: MLA-C02's GenAI content raises MLA's utility; nothing found displaces AIP-C01 or PAA. | A/B/C |

---

### D8. Falsification and counter-arguments

**(a) The strongest argument that earning all of these is a waste, and its evidence.**
1. *Signal:* only a minority of hiring managers screen for AI certifications (23%, C); portfolio claims dominate surveys (C); the only RCT shows near-zero effect for strong resumes (A); none of the Anthropic FDE postings I read mention certifications (B).
2. *Redundancy:* the model puts many credentials at 60 to 100% covered by another (CCAR-P to CCAO-F 90%, PAA to Gemini Agent Dev 82%, NCP-GENL to NCA-GENL 100%); beyond the first three or four, new credentials add signal repetition, not knowledge.
3. *Obsolescence:* validity runs 6 to 36 months; Claude's validity just changed from 6 to 12 months; three Claude exams refresh on 2026-12-07; MLA-C01 closed in English on 2026-09-28; PAA lasts 12 months.
4. *Time dominates cost* (about 6 to 1), so the real price of the full stack is roughly 500 to 1,000 hours.
5. *Integrity:* commercial question-bank vendors already advertise brand-new exams (Databricks Context Engineer, GitHub agentic exams) and AWS does not publish pass rates, so difficulty and signal quality are unverified. (Commercial pages surfaced in search; URLs not retained.)
6. *Opportunity cost:* the same hours could ship several deployed agent systems with evaluations.

**(b) Segments where the full stack helps or hurts.** *Helps:* IT services/GCC and partner/SI, where certified headcount drives tiers and FDE gates. *Neutral to mildly negative:* enterprise product teams beyond the platform credential. *Possibly negative:* frontier labs and startups, where practitioners argue a long certification list can read as substituting study for building (Grade C opinion from Dice and KDnuggets). **I searched for experimental or survey evidence of a stacking penalty and found none**; the negative-signal claim is unproven rather than refuted.

**(c) Obsolescence risk and its effect on the plan.** Short-validity items are placed last (Gemini badges 6 months) or in one window (Claude 12 months). AWS and Databricks cost the most to renew (a retake at full fee). Event-driven obsolescence: MLA-C01 is gone in English, so anyone with a plan built on MLA-C01 had to rebuild; a Q1 2027 check on re:Invent announcements before buying Tier 3 is prudent.

**(d) Portfolio alternative.** 498 hours is about 12 weeks full-time, or roughly three to five deployed agent systems at 100 to 150 hours each (my estimate, M). No study I found compares hiring signal per hour of certifications versus projects; the indirect evidence says projects dominate at frontier labs and startups, and certifications dominate where a partner tier or FDE gate is counting headcount. The recommended compromise is the portfolio-parity rule in R4. A cheap self-test is to log screen-to-interview conversion before and after each credential and stop at the first gate where it does not move.

**Strongest objections an expert would raise, and what I found.**

| Objection | Evidence found | Verdict |
|---|---|---|
| "The overlap percentages are arbitrary." | Method and inputs disclosed (D2); anchors are official domain weights; the total saving is sensitive to transfer efficiency (28% to 55%) but the ordering effect is small regardless. | Fair; treat as ±15 points, Grade M |
| "Hours are optimistic." | Pessimistic bands are 824 h (Plan A core) and 1,049 h (Plan C); AIP-C01 itself recommends 2+ years of production experience. | Fair; plan on the pessimistic band if unsure |
| "The composite score is subjective." | Rank stability: top two never change; top five change only if cost or hiring signal is removed (Spearman 0.945 to 0.998). | Partly answered |
| "Half the list is inaccessible to individuals." | Confirmed (Claude, Gemini badges, FDE programmes); no-access variants provided. | Correct; partner-first is an alternative |
| "No job-posting counts." | Confirmed; a sample of postings only. | Honest gap |
| "Microsoft exclusion makes the FDE minimum incomplete." | Mapped; AB-100's price assumed. | Acknowledged |
| "The RCT does not apply to engineers." | Population is MOOC certificate earners without degrees; effect sizes smaller than upstream's figure. | Correct; used as directional only |
| "Vendor numbers are marketing." | Anthropic's 175,000-certification claim and Databricks' "first" claim are single-source vendor statements. | Flagged as claims, not facts |

---

## Open Questions & Risks

**Open questions (each is a verified gap, not a guess):**

1. **List size.** The brief says 35 credentials plus 3 FDE programmes; the pasted list has 24 plus 4. Were about 10 credentials dropped?
2. **Individual access to partner programmes.** I could not confirm whether an individual with no partner employer can enrol in AWS FDE (one practitioner write-up says AWS Partner Network membership is required, Grade C) or any Claude route (for example via a training partner). Anthropic's own pages say partner staff only.
3. **PAA labs.** Are they proctored? What does the continuing-education renewal cost in hours and fees? Neither is stated in Google's FAQ.
4. **GitHub validity and regional availability.** GH-300 and GH-600 are annual (Microsoft Learn) or two-year (third parties); GH-600's beta was unavailable in India and I did not confirm GA availability.
5. **MLA-C02.** GA price, GA-date confirmation (AWS blog says 2027-01-14; the exam page says TBD), domain weights, and whether employers' lists naming MLA-C01 will accept C02.
6. **NCP-AAI.** The NVIDIA EU page shows "(Coming soon)" beside registration (updated 2026-10-30) while other sources treat it as live.
7. **Earner counts and pass rates.** Not retrievable. Credly static pages hide counts; vendors publish no pass rates.
8. **Job-posting counts at scale and recruiter Boolean strings.** Not run (tooling limit) or not found.
9. **Official weights not retrieved:** CCAO-F and CCDV-F domain weights, NCA-GENL and NCP-GENL official pages, PMLE's 2026 blueprint, Databricks ML Associate and Professional official guides, GH-300's official page.
10. **GST and INR pricing.** The 18% GST is an assumption; vendors may invoice India differently.
11. **Microsoft gap.** AI-103, AB-100 and AI-102 were not assessed; AB-100's fee is an assumption.
12. **Competitors not researched in depth:** OpenAI, Salesforce Agentforce, Snowflake, Oracle, IBM watsonx, ServiceNow.
13. **Q1 2027 events not searched:** NVIDIA GTC, Google Cloud Next, Microsoft Build.

**Risks:**

| Risk | Effect | Mitigation |
|---|---|---|
| Content refresh on **2026-12-07** (CCAO-F, CCDV-F, CCAR-P) | Study material written before the refresh may be stale | Use guides published from 2026-11-17; book those exams after 2026-12-07 |
| **PAA GA is days old** | Little third-party prep; question quality unknown | Use the official exam guide and labs; consider waiting 2 to 4 weeks |
| Claude validity has changed once (6 to 12 months) | Policy could change again | Time Claude exams close to need; renew only if counted |
| Global Premier fee waiver ends **2026-12-31** | Higher cost afterwards | Book before the cut-off if your employer is Global Premier |
| MLA-C02 GA slip | Plan dates for MLA move | Sit the beta ($75) or wait for GA |
| Gemini badges lapse in 6 months | Google FDE prerequisite lost | Take them within about six weeks of the bootcamp |
| Remote proctoring and dual-camera rules (Databricks) | Failed sessions and wasted fees | Test equipment; use test centres where offered |
| INR volatility (rupee at record lows in the search results) | Fees in INR move | Pay early where discounts exist |
| Model error in overlap, hours and scores | Plans mis-timed | Use bands; revisit at each gate |
| **Signal dilution** (dump vendors, mass-certification pushes) | Value per credential falls over time | Prefer credentials with hands-on components (PAA, AWS FDE) |

---

## Delta (what changed from the priors and from T0-11)

| Belief | Before | After | Basis | Grade |
|---|---|---|---|---|
| PAA is the first hands-on GenAI credential | 70% yes | **Partly wrong:** hybrid confirmed; earlier hands-on credentials exist; lab proctoring unverified | S11, S19, S20, S13 | A |
| Claude certifications are open to individuals | 55% yes | **Wrong (X):** partner-org staff only | S03, S01, S04 | A |
| Claude certifications last 12 months | Unverified | **Confirmed** (previously 6 months), with free on-time renewal | S03 | A |
| AWS FDE uses sandbox/hands-on validation, not MCQ | Unverified | **Confirmed** | S20 | A |
| MLA-C01 is the current AWS ML associate | 80% yes | **Wrong (X):** closed in English 2026-09-28; C02 beta, GA 2027-01-14 | S21 | A |
| Databricks Context Engineer is the first context-engineering credential | Unverified | **Vendor claim; no competing dedicated credential found** (not independently proven) | S31 and searches | A (claim) / C (absence) |
| Context Engineer overlaps GenAI Engineer about 60% | 60% | **About 35 to 42%** (about 36% of the blueprint is new) | D2 | M |
| FDE programmes accept other vendors' professional certifications | 30% yes | **Contradicted** | S20, S15, S37 | A/B |
| Ordering saves more than 25% versus random | 60% yes | **Contradicted:** ordering about 4%; overlap itself about 45% | D2 and R2 | M |
| Gemini badge expiry of 2027-02-11 | Given | **Consistent with 6-month validity** | S13, S14, S16 | B |
| Certifications hurt when stacked at frontier labs | 75% | **Unproven:** no certification line in Anthropic FDE postings, but no stacking-penalty evidence either | S10, S47 | B/C |
| T0-11 F9: no verified exam had hands-on labs | Given | **Superseded** | S11 and others | A |
| T0-11 F6: RCT effect +11 pp | Given | **Not reproduced:** +1.0 pp (6%) on new employment in the paper's headline estimate; larger effects only in the resume audit for weak resumes | S43 | A |
| T0-11 F7: partner programmes create institutional demand | Given | **Strongly confirmed** | S03, S06, S20, S15, S37 | A/B |
| AMD ROCm Associate has value beyond AMD | Open | **Free and skill-relevant; no outside recognition found** | S40 to S42 | A/B/C |

---

## Sources & Evidence Ledger

Mode: **F** = fetched and read in full; **S** = search result or snippet only. All retrieved 2026-11-08. URLs marked "not retained" were seen in search results but not recorded; re-verify before relying on them.

| ID | Source | URL or anchor | Supports | Grade | Mode |
|---|---|---|---|---|---|
| S01 | Pearson VUE: Anthropic exams page | https://www.pearsonvue.com/us/en/anthropic.html | Claude exam delivery, retakes, 2026-12-07 refresh, partner access | A | F |
| S02 | Anthropic Partner Academy: CCAR-F exam page | https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification | CCAR-F $125 | A | F |
| S03 | Anthropic Partner Academy: Certifications FAQ | https://anthropic-partners.skilljar.com/page/faq-certifications | Fees, 12-month validity, renewal, discounts, format, eligibility | A | F |
| S04 | Anthropic Partner Academy: Partner certifications | https://anthropic-partners.skilljar.com/page/partner-certifications | Which exams count for partner standing | A | F |
| S05 | Anthropic: Claude Partner Network | https://www.anthropic.com/news/claude-partner-network | Network launch, $100M, certification launch | B | S |
| S06 | Anthropic: services track and partner hub | https://www.anthropic.com/news/services-track-partner-hub | Tier thresholds (via secondary summaries) | B | S |
| S07 | Anthropic: Claude Frontier Academy | https://www.anthropic.com/news/claude-frontier-academy | FDE nomination programme; certification volume claim | B | S |
| S08 | claudecertificationguide.com: new Claude certifications | https://claudecertificationguide.com/blog/new-claude-certifications-2026 | Items, domains, weights (third party) | C | F |
| S09 | Bounteous: Lead Forward Deployed Engineer | https://www.usaremotejobs.app/job/bounteous-lead-forward-deployed-engineer-fde-remote | Claude certification preferred | B | S |
| S10 | Anthropic FDE postings (Greenhouse and mirrors) | https://job-boards.greenhouse.io/anthropic/jobs/5391016008 | No certification line | B | S |
| S11 | Google Cloud Certification Help: Professional Agentic Architect | https://support.google.com/cloud-certification/answer/18080541?hl=en | Hybrid format, price, validity, GA | A | F |
| S12 | Google: PAA exam guide (PDF) | https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf | Sections, MCP and A2A scope | A | F |
| S13 | Credly: Gemini Enterprise Partner Specialist, Deployment | https://www.credly.com/org/google-cloud/badge/certified-partner-specialist-gemini-enterprise-depl | Badge scope, type, level | A | S |
| S14 | Credly: Gemini Enterprise Partner Specialist, Agent Development | https://www.credly.com/org/google-cloud/badge/certified-partner-specialist-gemini-enterprise-agen | Badge scope, type, level | A | S |
| S15 | Devoteam: Google FDE enablement completion | https://www.devoteam.com/news-and-pr/devoteam-becomes-one-of-the-first-companies-in-europe-to-complete-google-clouds-forward-deployed-engineer-fde-enablement-program/ | Google FDE prerequisites | B | S |
| S16 | Medium: Gemini Agent Development certification | https://medium.com/@uxraspberry/certified-partner-specialist-in-gemini-enterprise-agent-development-4dd895df0115 | Six-month validity | C | S |
| S17 | Google Cloud Ambassador Program | https://partners.cloud.google.com/google-cloud-ambassadors | AI/ML ambassador certification requirements | A | S |
| S18 | Google Cloud: Generative AI Leader page; PMLE summaries | https://cloud.google.com/learn/certification/generative-ai-leader?hl=en (PMLE third-party summaries; URLs not retained) | GAIL fee, length, sections; PMLE fee | B | S |
| S19 | AWS: Certified Generative AI Developer – Professional | https://aws.amazon.com/certification/certified-generative-ai-developer-professional | AIP-C01 format, fee, domains, microcredentials | A | F |
| S20 | AWS Partner Network blog: new FDE pathways (2026-10-01) | https://aws.amazon.com/blogs/apn/new-fde-pathways-for-aws-partners-get-ready-for-production-agentic-ai-delivery/ | FDE Validated and Advanced prerequisites and assessment | A | F |
| S21 | AWS Training and Certification blog: September 2026 offerings | https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/ | MLA-C01 retirement, MLA-C02 beta and GA date | A | S |
| S22 | AWS: Certified ML Engineer – Associate | https://aws.amazon.com/certification/certified-machine-learning-engineer-associate | C01 format, fee, status | A | S |
| S23 | AWS: Certified AI Business Strategist exam page | aws.amazon.com/certification (page seen via search 2026-11-08; URL not retained) | AIB-C01 beta, fee, domains, validity | A | S |
| S24 | Credly: AWS Certified GenAI Developer – Professional | https://www.credly.com/org/amazon-web-services/badge/aws-certified-generative-ai-developer-professional | Badge exists; no earner count visible | A | F |
| S25 | AWS Partner Network blog: re:Invent 2026 guide | https://aws.amazon.com/blogs/apn/know-before-you-go-an-aws-partners-guide-to-reinvent-2026/ | Event dates, certification offers | A | S |
| S26 | howtoai.com: AWS AI certifications | https://howtoai.com/aws-ai-certifications/ | MLA-C02 and AIF-C01 details; repeat voucher | C | S |
| S27 | Deloitte US: Forward Deployed Engineer – AWS (Monster) | https://www.monster.com/job-openings/forward-deployed-engineer-aws-tempe-az--e6489610-0da1-45f4-8c8b-cd4c94d8c8a4 | "3 of 6" AWS certifications | B | S |
| S28 | Deloitte US: Senior AWS FDE – GPS | https://apply.deloitte.com/en_US/careers/JobDetail/Senior-AWS-Forward-Deployed-Engineer-GPS/367967 | Associate and Professional certification lists | B | S |
| S29 | Deloitte US: Project GenAI Engineer III | https://apply.deloitte.com/en_US/careers/JobDetail/Project-GenAI-Engineer-III/364356 | AIF-C01 among skills | B | S |
| S30 | brickster.ai: Databricks certification cost and full list | https://www.brickster.ai/articles/databricks-certification-cost-full-list | Databricks fees, formats, domains, rules | B | F |
| S31 | Databricks blog: Context Engineer Associate, "industry's first" | databricks.com/blog (title: "Databricks Context Engineer Associate: industry's first certification for reliable AI agent systems"; slug not retained) | Vendor claim | A (claim) | S |
| S32 | GitHub: lukaleet/databricks-context-engineer-exam-notes | https://github.com/lukaleet/databricks-context-engineer-exam-notes | Study framing from GenAI Engineer | C | F |
| S33 | Microsoft Learn: GH-600 study guide | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-600 | Domains, MCP scope, no A2A, annual renewal statement | A | F |
| S34 | Microsoft Tech Community: GitHub Agentic AI Business Professional | https://techcommunity.microsoft.com/blog/skills-hub-blog/new-github-certified-agentic-ai-business-professional/4564534 | GH-700 beta terms | A | S |
| S35 | trainingcamp.com: GitHub Agentic AI Developer and Copilot explainers | https://trainingcamp.com/what-is-github-agentic-ai-developer/ | GH-600 and GH-300 fees and validity (conflicting) | C | S |
| S36 | Microsoft Reactor: GH-600 event | https://reactor.microsoft.com/en-us/reactor/events/27225/ | Beta unavailable in India | B | S |
| S37 | Microsoft LevelUp: Frontier Transformation Engineer | https://skillupwithlevelup.com/frontier | FTE prerequisites and hours | B | S |
| S38 | NVIDIA: NCP-AAI | https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/ | Format, fee, validity, blueprint | A | F |
| S39 | NVIDIA: certification hub | https://www.nvidia.com/en-eu/learn/certification/ | Credly delivery of badges | A | S |
| S40 | AMD: announcing the ROCm certification program | https://www.amd.com/en/developer/resources/technical-articles/2026/announcing-the-rocm-certification-program.html | Levels, scope, Expert early 2027 | A | S |
| S41 | AMD: ROCm Certified Developer Program Agreement | https://developer.amd.com/legal/rocm-certified-developer-program-agreement/ | 24-month validity; evaluation types | A | S |
| S42 | AMD: ROCm Certified programs | https://developer.amd.com/rocm/ | Associate July 2026; Professional and Expert "coming soon" | A | S |
| S43 | Athey and Palikot: value of non-traditional credentials (arXiv 2405.00247) | https://arxiv.org/abs/2405.00247 | RCT design and effect sizes | A | S |
| S44 | KDnuggets: 5 AI certifications worth paying for | https://www.kdnuggets.com/5-ai-certifications-worth-paying-for-in-2026-and-which-to-skip | Portfolio versus certification claims | C | S |
| S45 | InfoWorld: Are AI certifications still worth it? | https://www.infoworld.com/article/4242723/are-ai-certifications-still-worth-it-what-changed-in-2026.html | WGU survey figures | C | S |
| S46 | Rework: AI certification market 2026 | https://resources.rework.com/news/ai-jobs-skills/ai-certification-market-2026-what-matters | 23% screening figure | C | S |
| S47 | Dice: certifications get you the interview, portfolios get you the job | https://www.dice.com/career-advice/certifications-get-you-the-interview.-portfolios-get-you-the-job | Stacking opinion | C | S |
| S48 | HDFC Sky (PTI): rupee settles at 94.58 | https://hdfcsky.com/news/rupee-gains-17-paise-to-settle-at-94-58-against-us-dollar | USD/INR rate | B | S |
| S49 | IAPP: AIGP | https://westin.iapp.org/certify/aigp (also iapp.org) | AIGP fees and scope | B | S |
| S50 | ISACA: AAIR launch | https://www.isaca.org/about-us/newsroom/press-releases/2026/isaca-launches-advanced-in-ai-risk-aair-certification-to-equip-it-risk-professionals | AI-risk credential | A | S |
| S51 | cloudaqube: AIP-C01 difficulty | https://cloudaqube.com/blog/aws-genai-developer-professional-difficulty | AWS does not publish pass rates | C | S |
| S52 | Credly: top AI badges 2026 | https://learn.credly.com/blog/explore-credlys-top-ai-badges-across-foundational-to-advanced-levels-2026 | CCAR-P and NCP-AAI badges exist | B | S |
| S53 | Secondary coverage of Claude Frontier Academy (unite.ai, fullstack.com, digitalapplied.com, highcircl.com) | domains as surfaced in search; URLs not retained | Frontier Academy details; 175,000 certification claim | B/C | S |
| S54 | DEV Community: AWS MLA-C02 beta guide | https://dev.to/sajeevsebastian/aws-mla-c02-exam-guide-2026-beta-domains-and-study-plan-227o | MLA-C02 beta details | C | S |
| U1 | T0-11 upstream findings (October 2026) | Not re-retrieved | F4 to F9 as given; re-checked in D6 | n/a | n/a |
| M1 | Model files (topic vectors, coverage, scoring, calendars) | Method in D2, D3 and D5; parameters listed there | All Grade M outputs | M | n/a |

**What I searched for and did not find:** per-credential Credly earner counts; vendor-published pass rates; recruiter Boolean strings naming these credentials; any stacking-penalty experiment; any non-AMD employer naming the ROCm Associate; any other vendor's dedicated context-engineering credential; any FDE programme accepting another vendor's certification.
