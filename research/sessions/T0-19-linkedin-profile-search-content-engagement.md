---
id: "T0-19"
title: "LinkedIn for GenAI Job Seekers: Recruiter Search, Profile, Content and Engagement"
date: "2026-11-11"
status: complete-with-gaps
topic: "linkedin-profile-search-content-engagement"
tags: ["linkedin", "recruiter-search", "open-to-work", "easy-apply", "feed-ranking", "networking", "india", "genai-jobs"]
informs_decisions: ["D-005", "D-011"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-11"
authored_by_model: "Claude Sonnet 5.5 (Anthropic) in claude.ai with web search and page fetch. Anthropic's products are not in scope; one cited analysis (S42) concerns Anthropic as an employer and is marked COI."
evidence_window: "2019-09-11 to 2026-11-11"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 10
---

# T0-19: LinkedIn for GenAI Job Seekers: Recruiter Search, Profile, Content and Engagement

S-numbers refer to rows of the Sources & Evidence Ledger (sub-rows such as S33a are listed there). Grades follow EGP-1.0: A primary source opened, B established secondary source or sizeable dataset, C attributed third-party analysis, D memory or anecdote, E untraceable (absence records and table rows only), M own calculation, P practice-curated. Research date is 2026-11-11; every source was retrieved on that date. The evidence window is 2024-01-01 to 2026-11-11. Older items are background and are flagged pre-window. LinkedIn Help Center pages refused automated fetching (robots rules), so Help claims rest on search extracts or vendor readings and are capped at B or C. This file merges the first draft with a verification pass run on 2026-11-11; the changes are listed at the end of the ledger section.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | Recruiter search relies mainly on structured fields (title, location, skills, years of experience); free-text About matters little | 60% | D |
| P2 | LinkedIn's claim that Open to Work roughly doubles recruiter messages comes from its own 2020 analysis and has no published method | 70% | D |
| P3 | No independent study shows that posting or commenting raises recruiter outreach or interview invitations for job seekers | 75% | D |
| P4 | Applying on employer sites converts better than Easy Apply, but the best data are self-selected tracker data | 70% | D |
| P5 | LinkedIn retired skill-assessment badges in 2023–2024, so advice to take assessments is stale | 75% | D |
| P6 | LinkedIn publishes a fixed weekly invitation cap (about 100) and a fixed monthly allowance of free personalised notes | 40% | D |

## Research Question

**Decision question.** How should a GenAI job seeker set up and use LinkedIn so that recruiters and hiring managers find them for the right roles, can check them quickly and reach out, and which widely shared tactics have evidence behind them?

**Sub-questions.** (1) Which fields and AI features shape recruiter search? (2) What do the two forms of Open to Work do, and what is the evidence on effect and stigma? (3) What do reviewers weigh? (4) How do skills and keywords work? (5) Easy Apply against employer sites, ghost jobs and the Texas Attorney General investigation. (6) Feed ranking and content effects. (7) Connection, InMail and limits. (8) Premium Career. (9) Verification and scams. (10) India. (11) GenAI profile patterns. (12) Tools.

**Reading chosen.** "Being found" is judged from LinkedIn's documentation of recruiter tools. "Being checked" is judged from surveys and experiments. Any hiring effect of content is judged from outcome data only. Engagement metrics (reach, likes) are reported but not treated as hiring evidence.

**Method.** About 55 searches (standard and extended modes). The 13 ledger rows marked Read were opened in full or part (S1–S4, S7, S9–S11, S13, S16, S22, S32, S49); all other rows rest on search extracts. A verification pass on 2026-11-11 re-opened or re-checked the Texas Attorney General release, the Hiring Assistant 2 report, LinkedIn's 2020 Open to Work post, the interviewing.io Open to Work study, and the invitation-limit, verification, dwell-time, Pin and FTC sources. Falsification searches: (a) an experiment or stigma study on Open to Work; (b) a controlled Easy Apply against direct-application comparison; (c) any study linking posting to recruiter outreach, plus a trace of "posting daily triples recruiter views"; (d) news on the Texas matter after July 2026; (e) aggregate headline or About patterns of GenAI hires. Results are in Absences. Largest samples used: Huntr 1.24M tracked applications (S29); Buffer 52M posts (S25); the Science experiment on 20M members (S11).

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Recruiter search combines structured filters (job title, location, Open to Work, skills, companies, schools, years of experience, seniority, languages, degree, company size) with keyword matching anywhere on a profile and AI semantic search. LinkedIn states that it standardises titles, skills and schools, excludes protected attributes from filters, and shows qualifications found and missed. Field weighting is unpublished. | [S1][S2] | A (mechanics) |
| KF2 | Being found and being checked are one surface. Hiring Assistant (charter 2024-10, English availability 2025-09) and Hiring Assistant 2 (announced 2026-09-30, rollout 2026-11) add fit signals, member verification, ATS and pre-screen insights and connected-app evidence to the candidate view. LinkedIn claims early adopters review 62% fewer profiles (COI). | [S3][S44][S51] | B |
| KF3 | Open to Work has two documented forms and, in India, recruiter-only notice-period and salary fields. LinkedIn's effect claims (about 2x recruiter messages; +40% InMails and +20% community messages with the public frame) date from 2020, give no method, and were repeated in 2024–2025. No independent causal study exists. Stigma claims are opinion. One 2023 dataset shows the badge's candidate-quality signal flipping with the market (44% pass rate in 2021, 56% in Q1 2023, against a 51% average). LinkedIn's 2020 post also documents one ranking signal: accepting or declining recruiter messages. | [S5][S6][S7][S8][S18][S52] | A/B mechanics; C effect |
| KF4 | Skill assessments are discontinued and badges were removed in 2024. LinkedIn says hirers value examples of applied skill, so skills are tagged to jobs, projects and credentials. "Large Language Models" is a most-common skill for AI Engineer in LinkedIn's data. Recognition of RAG, agents, evaluation or MCP as standard skills was not verified. | [S34][S41] | B |
| KF5 | Certification value is heterogeneous. A randomised experiment found credential sharing raised new employment by 1.0 pp (5.9%), concentrated in weak-baseline learners. An interviewing.io dataset found 53% against 57% pass rates for engineer profiles listing certifications. 2026 AI/ML recruiter strings contain no certification acronyms. | [S9][S10][S40] | B |
| KF6 | No controlled Easy Apply test exists. In Huntr tracker data (self-selected), LinkedIn-sourced applications reach interview at about 2.9–3.6% against 6.6–9.9% for Google-sourced ones; employer career sites run 1.7x job boards. Vendor figures of "1–2% against 15–30%" have no method. | [S29] | B (association) |
| KF7 | Volume is high (about 9,500–11,000 applications a minute, reported 2025). Texas issued a Civil Investigative Demand on 2026-07-14. Coverage on 2026-07-14 and 2026-07-15 reports no formal allegations and no lawsuit, and a law-firm note dated 2026-09 still describes an investigation; I found no later filing. The "one-fifth to one-third" ghost-job range is attributed by the Attorney General to unspecified independent studies; Greenhouse reports 18–22% a quarter on its own platform. | [S13][S14][S15][S16][S30][S31] | A (investigation); B/C (prevalence) |
| KF8 | LinkedIn Engineering reports an LLM-embedding retrieval stage and a sequence-based Generative Recommender ranking stage (blog 2026-03-12 as summarised; research papers 2025). Dwell time has been a documented input since a 2020 engineering post. LinkedIn documents visibility limits for excessive or automated comments (2025-08-20). No LinkedIn page found gives format, external-link or cadence weights; "the 360Brew algorithm" is marketers' wording for a 2025 research paper. | [S20][S21][S22][S53][S57] | A/B |
| KF9 | Large-sample format and cadence studies conflict and measure engagement on brand or scheduler samples, not hiring. No study links posting to recruiter outreach or interviews. LinkedIn's own "two posts a week, up to 5x profile views" has no method. | [S24][S25][S26][S27][S28] | C |
| KF10 | A randomised experiment on 20M members found moderately weak ties produced the most job mobility, strongest in digital industries. A South African randomised trial found four hours of LinkedIn training raised employment by 7 pp from 70%, through information gathering rather than content creation. | [S11][S12] | A; B |
| KF11 | No LinkedIn Help page that vendors checked states a weekly invitation number (about 100 a week is vendor consensus), and LinkedIn's pages reportedly disagree on the free personalised-note allowance (3 or 5 a month; Premium unlimited). InMail credits run from 5 (Premium Career) to 50 (Sales Navigator Core). Pin's 17.08% reply rate covers recruiter-sent LinkedIn messages (about 276,000–294,000 of a 4M+ message set); on the same 165,000+ candidates Pin reports 16.6% on LinkedIn against 4.4% on email. None of it transfers to candidate-initiated outreach. | [S37][S47][S55][S56] | C/D |
| KF12 | LinkedIn reports over 90M verified members (2025-09-04), over 100M (2025-12-18) and 115M with 700,000+ verified companies (2026-09-23). Workplace verification is required for recruiter and leadership titles (2025-09), a recruiter badge dates from 2024-04, and colleague vouching arrived 2026-09-23. LinkedIn's uplift claims (60% more views, 30% more connection requests, 13% more recruiter responses) give no method. Gartner forecasts that one in four candidate profiles will be fake by 2028. | [S32][S33a][S33b][S33c][S38][S59] | B facts; C uplift |
| KF13 | LinkedIn research reported 2026-02-03: 74% of India recruiters struggle to find qualified candidates, and 53% of those who say hiring is harder cite AI-generated applications. The survey base is LinkedIn's talent research (Censuswide, 6,554 global HR professionals, fielded 2025-11); the India sub-sample is not stated. LinkedIn added India-only notice-period and expected-salary fields and recruiter filters (2025-10). No independent comparison of LinkedIn, Naukri and Instahyre for GenAI hiring exists. | [S17][S18][S19][S45][S51] | B; C |
| KF14 | LinkedIn ranks AI Engineer first on its 2026 Jobs on the Rise (US) and says it overtook Machine Learning Engineer as the most common AI role. A single-author analysis of 1,680 Anthropic engineer profiles (2026-06) found few PhDs (13.7%) and classic infrastructure skills listed. Aggregate headline or About patterns of hires are not published. | [S41][S42] | B; C |
| KF15 | Premium Career has only LinkedIn's own outcome claims (3.9x hired when applying to "Top applicant" jobs, Jan 2025). No independent causal evidence was found. Price about $39.99 a month per the Texas Attorney General. | [S13][S36][S47] | C |

## Recommendation

Grades below grade the evidence behind each rule, not its expected size of effect. The door is two-way: every rule is cheap to reverse.

| # | Decision rule | Grade | Failure mode |
|---|---|---|---|
| R1 | Headline: one standard target title you can defend, then 2–4 evidenced stack or problem terms (for example LLM evaluation, RAG, inference serving). Keep real titles and dates in Experience. | A mechanism; P format | A headline title that differs from your real title can read as misrepresentation; unevidenced terms invite probing |
| R2 | Fill every structured field consistently with CV and GitHub: titles, employers, dates, location, education, languages. | A (fields); D (consistency lowers false flags, K5) | Date or title mismatches may trigger verification doubt; no data on false-flag rates |
| R3 | Skills: list skills you can evidence, tag them to the roles or projects showing them, and use the exact terms in three target postings. Do not pad to the 50 limit. Skip assessments. | B (retirement); P (selection) | Under-listing misses skill-filter searches; over-listing invites mismatch with AI-read evidence |
| R4 | Open to Work on, recruiters only, 2–5 target titles and location types. In India add notice period and expected salary only as ranges you can honour. Treat the public frame as optional. | A/B mechanics; C benefit | LinkedIn says it cannot ensure the status stays hidden from your employer; stated pay can anchor offers; stigma unmeasured |
| R5 | Featured: 2–3 proof artefacts (repo, demo, evaluation write-up) with one line of context, consistent with GitHub. Add connected apps only where the partner is relevant. | P (B for the premise that hirers value applied examples) | Dead or private links; overclaiming; data sharing with partner apps |
| R6 | Complete workplace verification (work email), optionally ID, and ask one or two colleagues to vouch. | B feature; C uplift | Personal-data sharing; uplift claims are LinkedIn's and probably selection |
| R7 | Certifications: list role-relevant ones, mainly when other signals are thin (early career, no degree); otherwise omit. | B | Omitting forgoes a signal that helped weak profiles; listing carries a negative association among engineers |
| R8 | Apply on the employer's career page or ATS when the posting links to one; Easy Apply as fallback; log every application and outcome. | B (association) | Selection bias in tracker data; some roles accept only Easy Apply |
| R9 | Before applying check posting age, the "reviewing applicants" or response-time indicator and the verified-company badge; deprioritise postings older than about 60 days without a human contact. | C | Age is not proof of a ghost job; evergreen roles exist |
| R10 | Network through moderately weak ties: second-degree contacts at target employers, alumni, co-authors, event contacts. One short, specific message with one ask. | A (weak ties); D (message form) | Evidence is from 2015–2019 connection-suggestion experiments; no LinkedIn source for "about 100 a week"; free personalised notes are 3 or 5 a month on different Help pages |
| R11 | Content as distribution for artefacts you already built: one post per artefact (aim 1–2 a month) and 2–3 substantive comments a week. No daily cadence. | D/P | Effect on recruiter outreach is unmeasured; time cost; generic posts earn little reach |
| R12 | Never use automation, activity-driving extensions, pods or AI comment tools. | B | Forgone reach compared with people who break the rules |
| R13 | Do not buy Premium Career by default. In an intensive search take one month for applicant insights and 5 InMails, measure replies, then cancel. | C | "Top applicant" is a weak signal; posting-quality allegations in Texas; no independent evidence |
| R14 | India: run LinkedIn with Naukri and one tech board (Instahyre, Cutshort, Hirist or Wellfound) in parallel; keep recruiter-visible fields current. | C | No independent channel comparison; scam risk on any board |
| R15 | Reply to genuine recruiter messages (accept or decline) after checking the sender's profile and verification. | C (LinkedIn statement, 2020, pre-window) | Replying to scam messages; the statement has no method |

**Weekly routine (about 2.5–3 hours; grade P, unmeasured).**

| When | Task | Minutes | Rules |
|---|---|---|---|
| Monday | Check Open to Work preferences, headline against three target postings, alerts | 20 | R1, R4 |
| Mon, Wed, Fri | Review alerts; apply to the best 1–2 roles on employer sites within 48 hours; log | 3 × 25 | R8, R9 |
| Tuesday | 5–8 targeted messages to second-degree contacts at employers you applied to | 30 | R10 |
| Wednesday | 2–3 substantive comments on practitioners' posts in your niche | 30 | R11 |
| Any day | Reply to genuine recruiter messages after checking the sender | 10 | R15 |
| Friday | Draft or post one artefact write-up (every 1–2 weeks); refresh Featured; check consistency with CV and GitHub | 45 | R2, R5, R11 |
| Monthly | Count recruiter messages and replies; decide on Premium; re-check feature changes (platform facts expire in 90 days) | 30 | R13 |

**What would change these rules.** LinkedIn publishing field weights, or an independent Open to Work experiment (R4); a controlled Easy Apply comparison (R8); the outcome of the Texas matter and any change to job-verification labels (R9, R13); documentation of Hiring Assistant 2 fit signals showing what is read from profiles (R1–R3, R5); evidence that posting moves recruiter outreach (R11).

## Alternatives Considered

| Option | Verdict | Why |
|---|---|---|
| Content programme (daily posting) | Rejected | No hiring evidence; LinkedIn's "up to 5x" claim has no method; datasets conflict (KF9) |
| High-volume Easy Apply | Rejected as primary | Lowest interview rates in tracker data (KF6); fine as a fallback |
| Network-first with profile as verification | Preferred, co-primary | Weak-ties experiment (A); the profile is read by AI and humans at the same step (KF2) |
| Continuous Premium Career | Rejected | Only vendor claims; price about $39.99 a month (KF15) |
| Public Open to Work frame by default | Conditional | LinkedIn and recruiters disagree and nobody measured; recruiters-only carries the same filter benefit |
| Automation or pods | Rejected | Prohibited; visibility limits; account restriction (KF8) |
| Certification-first profile | Rejected for mid and senior; conditional early career | Mixed evidence (KF5) |
| Third-party AI profile rewriting | Use with care | No outcome evidence; AI-read profiles are checked against evidence |
| Other boards in India in parallel | Preferred | LinkedIn alone is not shown to be sufficient; no independent comparison, so low confidence |

## Detailed Findings

### DF1. Recruiter search (KF1, KF2)

LinkedIn's semantic-search playbook (undated, c. 2025) lists the filters a Recruiter user can apply, including job title, location, Open to Work, skills, companies, schools, graduation year, industries, seniority, languages, years of experience, years in current position, fields of study, degree and company size [S2]. In my paraphrase of that document: protected attributes cannot be filtered; titles, skills and schools are standardised across languages; résumé search handles English-language résumés only; keyword search matches a term anywhere on a profile; and AI-Assisted Search returns a high, medium or low relevance label with qualifications found and missed. LinkedIn also says semantic search can match qualifications not typically written on a profile [S1]. No page I opened states how fields are weighted in candidate order (Absence A1).

| Date | Feature | Source | Grade |
|---|---|---|---|
| 2024-04-16 | "Verified recruiter" badge announced | S59 | B |
| 2024-10 | Hiring Assistant charter programme announced | S44 | B |
| 2025-09 (end) | Hiring Assistant available in English; German and French listed later | S44 | B |
| 2025-10-09 | India: notice period and expected salary in Open to Work; recruiter filters | S18, S19 | B |
| 2026-01-29 | Verified AI skill levels (secondary report) | S49 | C |
| 2026-06-17 | Connected apps (partner-verified activity on profiles) | S4 | A |
| 2026-09-23 | Colleague vouching; page-admin removal of false claims | S32 | B |
| 2026-09-30 | Hiring Assistant 2 announced: fit signals, verification, ATS and pre-screen signals; rollout 2026-11 for English users | S3 | B |

Pin (vendor, C) reports that AI-Assisted Search reached English-speaking Recruiter Corporate customers in 2024-05 [S44]. Hiring Assistant 2 screens against a recruiter's own rubric, coordinates interviews, and surfaces member verification and ATS, pre-screen and work-experience insights; the update is free for existing English-language users [S3]. Hiring Assistant can also evaluate applicants who applied off LinkedIn through ATS connections [S44]. It follows, as inference (D), that CV and profile consistency matters at one step.

### DF2. Open to Work (KF3)

*Mechanics.* Recruiters-only makes the status visible to Recruiter users, with LinkedIn saying it tries to hide it from recruiters at your employer but cannot ensure that. The public frame shows to everyone [S5][S18]. In India, notice period and expected annual salary are recruiter-only whatever the visibility setting [S5][S18].

*LinkedIn figures.* In its 2020-10-29 post LinkedIn said turning Open to Work on raises the likelihood of a recruiter message about 2X. It said more than three million members had added the public frame since the June 2020 launch and were on average 40% more likely to receive InMails, and that early results showed 20% more messages from the community (pre-window, no method) [S6]. The same post says accepting or declining recruiter messages signals engagement and helps ranking in recruiter search [S6]. LinkedIn told Fortune (2024-09-05) that about 200M members had the setting on behind the scenes and about 40M displayed it publicly [S7]. Its 2025-10 India release repeated the "double" claim [S18].

*Counter-evidence.* Recruiters quoted by Fortune split on whether the frame hurts (C) [S7]. An interviewing.io dataset (2023-04, pre-window) found engineers showing the badge in 2021 passed interviews at 44% against a 51% average, while the Q1 2023 cohort passed at 56%; badge prevalence rose from 1.4% to 4.2% among 10,000+ people with LinkedIn data. That measures candidate quality, not recruiter bias. The authors advised against listing it publicly because of residual bias [S8][S52]. No experiment on recruiter response exists (Absence A2).

### DF3. What reviewers weigh (KF1, KF2, KF4, KF5)

Stated-behaviour surveys exist, such as a 2026 vendor survey of 805 US hiring managers (fielded 2026-09 and 2026-10) reporting that 9 in 10 check social profiles [S43]. None observes profile opens (Absence A3). Profile-field evidence:

| Field | What search and reviewers do with it | Evidence | Grade |
|---|---|---|---|
| Headline | Indexed text; no published weight; no format test | S2 (keyword anywhere); S39 (title similarity in ATS layers) | A matching; P format |
| Titles in Experience | Title filter; standardised; matched to role title by ATS and AI layers; verification can mark the employer | S2, S39, S32 | A/B |
| About | Indexed; AI search and Hiring Assistant read qualifications beyond listed ones | S1, S2 | A mechanism; P advice |
| Experience bullets | Same index; LinkedIn says hirers value examples of applied skill | S34, S2 | B/P |
| Skills | Skills filter (LinkedIn claims 42% of recruiters use it weekly, global); assessments retired | S18, S34 | C usage; B retirement |
| Endorsements | One pre-window interviewing.io analysis reports little correspondence with interview performance (extract only) | S58 | C |
| Featured, projects | No indexing documentation found; skills are tagged to jobs, projects and credentials | S34 | P |
| Certifications | Positive for weak-signal profiles; negative association for engineers; absent from AI/ML strings | S9, S10, S40 | B |
| Recommendations | No evidence found | none | P |
| Photo, banner | Circulating multipliers have no traceable method | none | E |
| Custom URL | No evidence found | none | P |
| Location, languages, education, years of experience | Filters | S2 | A |
| Open to Work preferences | Filter; India adds notice-period and salary-band filters | S2, S5, S19 | A/B |
| Verification, vouches | Shown on profile and jobs; surfaced on the Hiring Assistant 2 candidate view | S3, S32 | B feature; C uplift |
| Connected apps | Partner-verified tool use visible to recruiters | S3, S4 | B |

### DF4. Skills and keywords (KF4, KF5)

LinkedIn's Help states Skill Assessments are no longer available and, on a second page, that badges were to be removed from profiles in 2024; it adds that hirers prefer examples of applied skill [S34]. Many 2026 optimisation guides still tell readers to take assessments, so that advice is stale. The 50-skill limit and the top-three display are widely repeated by practitioners (C). I found no study of an optimal skill count. In the 2026 AI/ML Boolean strings I saw (Pin, Juicebox, Taggd, Knowlee, GCC Journal), recruiters key on titles, Python, PyTorch or TensorFlow, LLM or NLP terms, location and exclusions, and none includes a certification acronym [S40]. Eightfold documents title similarity (cosine similarity of title vectors), skill overlap, seniority fit and industry similarity [S39]. Phenom documents skills, title, experience and location, editable by recruiters (page dated 2022-06-23, possibly stale) [S39]. Stuffing risk: LinkedIn's own tools display qualifications found and missed [S2], and Hiring Assistant 2 adds verification [S3], so unevidenced skills are exposed. Practitioners who urge filling all 50 give no outcome data (D). Whether RAG, agents, evaluation or MCP are standard LinkedIn skills was not checked (Absence A9).

### DF5. Applying on LinkedIn (KF6, KF7)

*Tracker data.* Huntr's users tracked 1.24M applications (2024-10-01 to 2026-07-01). Google Jobs reached interview at 6.60% (Indeed 2.92%) [S29]. A Q3 2026 preview over 12 months gives 9.9% for Google-sourced against 3.6% for LinkedIn (175,416 LinkedIn applications) and 1.7x for employer career sites over boards [S29]. Q2 and Q1 2026 cuts: 7.91% against 3.36%, and 7.12% against 2.94% [S29]. Caveats: users self-select, interviews are user-recorded, and Google Jobs mostly links to employer sites. Nothing is specific to Easy Apply or GenAI roles (Absence A6). Vendor figures of "1–2% Easy Apply against 15–30% direct" have no method and are not repeated.

*Volume.* About 11,000 applications a minute, up 45% year on year (New York Times figure relayed 2025-06-24) [S15]; "nearly 9,500" from a LinkedIn representative via CNBC (2025-10-29) [S16]. K1 dated the figure to late 2024; both reports are from 2025.

*Ghost jobs and Texas.* The Attorney General announced a Civil Investigative Demand on 2026-07-14 covering advertising, marketing, verification practices and representations about Premium and job listings. The release states that LinkedIn "does not independently verify the hiring status of most listings on its platform" and cites unspecified independent studies putting ghost jobs at one-fifth to one-third of online listings [S13]. LinkedIn's spokesperson said its policies require posted jobs to be authentic and accurately represented. LinkedIn also said it displays company response time and review status for many jobs, and pointed to verification of jobs, recruiters and company pages [S14]. Coverage on 2026-07-14 and 2026-07-15 reports no formal allegations of wrongdoing and no lawsuit; a law-firm note dated 2026-09 still describes a Civil Investigative Demand and LinkedIn's pushback; I found no later filing (V0; Absence A12) [S14]. Greenhouse reports 18–22% of postings on its platform each quarter (2024 analysis) and 17% in Q2 2025; a Congressional Research Service primer, as relayed by a secondary source, cautions that most quoted figures come from firms selling hiring services [S14][S30]. Hotfix tracked 13,434 tech listings (2026-02-28 to 2026-04-28): one in three still live at 60 days, one in eight at 90 days; this measures staleness, not intent [S31]. Promoted and reposted job labelling: only a headline-level report found (Absence A15).

### DF6. Content and the feed (KF8, KF9)

LinkedIn Engineering's 2020-05-12 post (pre-window) defines two kinds of dwell time, with feed dwell time starting when at least half of an update is visible, and describes a skip-prediction model added to ranking [S53]. LinkedIn Engineering's 2026-03-12 post, as summarised by Social Media Today, and LinkedIn's research papers describe a unified retrieval stage built on fine-tuned LLM embeddings and a transformer-based Generative Recommender that ranks from a member's interaction sequence [S20][S21]. I did not open the primary 2026 blog page (Absence A13). A practitioner inventory dated 2026-08-24 concludes that LinkedIn publishes no weighting between signals and no dwell-time target [S57]. "The 360Brew algorithm" is marketers' wording: 360Brew is the title of a 2025-01 research paper, which a secondary source describes as pre-production [S57]. Separately, LinkedIn added a Help line (2025-08-20) saying it may limit visibility of comments from excessive creation or automation tools, and told Social Media Today it reduces reach for pods when detected [S22]. A 2026-08-09 shift to relevance-ranked comments is reported by secondary sources (C) [S50]. Creator mode's toggle was removed in 2024-03 and its tools opened to all profiles [S35].

Large-sample format studies:

| Study | Sample | Finding | Grade |
|---|---|---|---|
| Buffer | 52M+ posts across platforms | LinkedIn carousels (PDF posts) median engagement rate 21.77% | B |
| Metricool | 673,658 posts, 63,108 accounts (company-page skew) | Carousels outperform single images on interactions | B |
| Ordinal | 256,356 posts | Text-only highest average impressions; multi-image highest engagement rate | C |
| The Shield Index | Monthly reach, Dec 2025–Mar 2026 | Image, text, carousel within about 2.6 points and drifting | C |
| Buffer | 2M+ posts, 94,000+ accounts | Higher frequency gives better per-post results within an account | B |

None measures recruiter outreach. Samples skew to brands and scheduler users, and several datasets pre-date the 2026-03 rebuild. No study ties posting to recruiter messages or interviews (Absence A4). LinkedIn's "twice a week, up to 5x profile views" is an uncontrolled claim, and profile views are not recruiter views [S28]. The only anecdote I found (D) reports more recruiter messages after stopping posting [S48].

### DF7. Engagement (KF10, KF11)

*Weak ties.* Science (2022-09-16) analysed randomised changes to connection suggestions for over 20M members (2015 and 2019 experiments; about 2 billion new ties; 600,000 new jobs). Moderately weak ties by mutual connections, and the weakest ties by interaction intensity, gave the most mobility. Weak ties helped more in digital industries, and LinkedIn staff co-authored [S11].

*Invitation limits.* Vendor readings of LinkedIn Help (one checked four Help pages on 2026-09-08) agree that no page states a weekly number; "about 100 a week" is vendor consensus. They report that LinkedIn's pages disagree on the free personalised-note allowance (3 a month on one page, 5 on others), at 200 characters for free accounts and 300 for Premium, and that a restriction typically lasts about a week [S56]. I could not open the Help pages (Absences A5 and A18).

*Reply rates.* Pin's 17.08% covers recruiter-sent LinkedIn messages through its own sequences. Pin's pages give the LinkedIn subset as roughly 276,000–294,000 messages inside a 4M+ set. On the same 165,000+ candidates Pin reports 16.6% on LinkedIn against 4.4% on email [S37][S55]. LinkedIn's own InMail average was 6.4% (2023-05 to 2024-04, relayed by Pin) [S37]. Neither is a candidate-initiated rate.

*Automation.* Automation is banned: LinkedIn warns users of such tools "risk having their accounts restricted or shut down" [S23].

### DF8. Paid tiers (KF15)

Premium Career: 5 InMails a month, applicant insights, Top applicant and Top choice, AI job tools and Learning [S36][S47]. The Texas Attorney General gives about $39.99 a month for Premium Career and $69.99 for Premium Business [S13]; aggregators list $29.99 and $59.99, which I attribute to annual billing or older lists (range $29.99–$39.99). Sales Navigator Core is $99.99–$119.99 monthly with 50 InMails (C) [S47]. LinkedIn claims Premium subscribers are 3.9x more likely to be hired when applying to Top applicant jobs (Jan 2025) and 43% more likely to get a recruiter message with Top choice (Jan 2024) [S36]. These are uncontrolled and company-reported (COI). No independent benefit evidence exists (Absence A10).

### DF9. Trust (KF12)

LinkedIn reports over 90M verified members (2025-09-04), over 100M (2025-12-18) and 115M with 700,000+ verified companies (2026-09-23) [S33a][S33c][S32]. In 2025-12 LinkedIn said about 60% of verified members confirmed a workplace and about 27% an identity through a government ID [S33c]. Workplace verification became required for recruiter and leadership titles (2025-09) [S33a], after a "verified recruiter" badge in 2024-04 [S59]. The 2026-09-23 changes add colleague vouching (the voucher must be verified, connected for a year, with two-factor authentication) and page-admin removal of false employment claims [S32]. LinkedIn's uplift claims for verified profiles vary by date and have no method: 60% more views, 30% more connection requests and 50% more post engagement (2025-09); 13% more recruiter responses (India release); 50% more post views and 90% more impressions (2026-09) [S32][S33a][S33b]. Gartner's survey of 3,000 candidates found 6% admitted interview fraud, and it forecasts that one in four candidate profiles will be fake by 2028 [S38]. The FTC reports losses to job and employment-agency scams rising from $90M (2020) to $501M (2024) [S54]. The prevalence of fake LinkedIn profiles was not measured independently (Absence A16 concerns an unsourced fake-account figure).

### DF10. India (KF13)

LinkedIn research as reported 2026-02-03: 74% of recruiters struggle to find qualified candidates, hiring runs 40% above pre-pandemic, and 53% of those finding it harder cite AI-generated applications (47% cite skills shortages). Also 71% of AI-using recruiters say it surfaces skills they would have missed, and about 80% plan more AI use [S17]. The survey base is LinkedIn's talent research: Censuswide, 6,554 global HR professionals, fielded 2025-11-10 to 2025-11-27; the India sub-sample size is not stated [S51]. Recruiter filters for notice period and salary band exist for India [S19]. Notice periods of 60–90 days are described as standard in Indian tech (vendor statement; source URL not retained; D) [S45]. Naukri JobSpeak (via a trade site) shows AI/ML hiring up 45% for FY26 (C) [S45]. A September–October 2026 analysis of 18,752 LinkedIn and Naukri postings finds 4.3% tagged entry-level (C) [S45]. Employer-side guides (COI) place LinkedIn Recruiter for senior sourcing, Naukri for IT-services volume, and Instahyre or Cutshort for product engineers [S45]. No independent channel comparison for GenAI roles exists (Absence A8).

### DF11. GenAI profile patterns (KF14)

LinkedIn's Jobs on the Rise 2026 (job starts 2023-01-01 to 2025-07-31) ranks AI Engineer first (US). Its most common skills include Large Language Models, MLOps, computer vision, PyTorch and TensorFlow, and common prior roles are software engineer, data scientist and data engineer [S41]. LinkedIn also reports AI Engineer overtook Machine Learning Engineer as the most common AI role [S41]. A single-author analysis (2026-06-11) of 1,680 engineer profiles at one lab found 13.7% PhDs and Python, Java and C++ as the most-listed skills; it is survivorship-biased and COI [S42]. Headline and About patterns of 2025–2026 hires across the listed role families are not published in aggregate (Absence A7). I did not profile individuals.

### DF12. Tools (stage 7)

| Tool | What | ToS or status | Evidence | Verdict |
|---|---|---|---|---|
| Premium Career | InMail, applicant insights, AI tools | Native; Texas CID allegations (V0) | LinkedIn claims only | use-with-care |
| Sales Navigator Core | 50 InMails; sales search | Native | None for job seekers | use-with-care |
| Recruiter, Hiring Assistant 2 | Employer-side search and agent | Native | Defines how profiles are read | watch |
| Open to Work (both forms) | Recruiter filter, public frame | Native | Mechanics A/B; effect C | use-with-care |
| Easy Apply | One-click application | Native | Lowest tracker rates | use-with-care |
| Job alerts | Saved searches | Native | Practitioner only | use |
| Verification, vouching | Identity and workplace signals | Native | Feature B; uplift C | use |
| Connected apps | Partner-verified activity | Native | Announced 2026-06-17 | watch |
| LinkedIn Learning certificates | Course credentials | Native | No evidence found | use-with-care |
| Third-party profile optimisers | Keyword and AI rewriting | Third party | No outcome evidence | use-with-care |
| Outreach automation and extensions | Auto-invite, auto-message, auto-comment | Prohibited | B | avoid |
| Engagement-pod services | Reciprocal engagement | Against policy; reach reduced | B | avoid |
| Schedulers and analytics extensions | Post planning | Allowed only if they do not automate or alter pages | Not verified per product | use-with-care |

### DF13. Tactics: documented or measured, then folklore

| Tactic | Claimed effect | Evidence | Grade | Verdict |
|---|---|---|---|---|
| **Documented or measured** | | | | |
| Standard target title plus evidenced keywords | Match in title and keyword search | S2, S39 | A | use |
| Open to Work, recruiters only | Appears in Open to Work filter | S2, S5 | A/B | use |
| India notice period and salary fields | Recruiter filters | S5, S18, S19 | B | use-with-care |
| Skill assessments | Badge raises rank | Retired (S34) | B | avoid |
| Employer-site over Easy Apply | Higher interview rate | S29 | B | use |
| Weak ties | More job mobility | S11 | A | use |
| LinkedIn training for low-resource seekers | +7 pp employment | S12 | B | use |
| Credential sharing with weak signals | +1.0 pp new jobs | S10 | B | use-with-care |
| Automation and extensions | More volume | Prohibited (S23) | B | avoid |
| Pods and automated comments | More reach | Visibility limits (S22) | B | avoid |
| **Folklore or unmeasured** | | | | |
| Reply to recruiter messages | Ranks higher in recruiter search | LinkedIn 2020 statement, no method (S6) | C | use |
| Post twice weekly for up to 5x profile views | More profile views | S28 | C | untested |
| Daily posting triples recruiter views | Triple views | Origin untraced; trail ended at unsourced blogs | D | untested |
| Carousels give "585% more engagement" | More engagement | S25 against S26–S27 conflict; not hiring | C | untested |
| External links in comments, not post | Avoids penalty | No LinkedIn documentation found (S57) | D | untested |
| Public #OpenToWork frame | +40% InMails against stigma | S6, S7, S52 | C | use-with-care |
| Five or more skills give large multipliers (17x views, 33x messages; 31x in one 2026 guide) | More views | Untraced (S60) | D | untested |
| Endorsements build trust | Higher response | One pre-window analysis found little correspondence (S58) | C | untested |
| Verified profile uplift | 60% more views; 13% more recruiter responses | S32, S33a, S33b | C | use |
| Premium gets you hired faster | 3.9x | S36 | C | use-with-care |
| Personalised connection note | Higher acceptance | Vendor claims, no method (S46) | D | use-with-care |
| Weekly cap about 100; free notes 3 or 5 a month | Safe limits | Vendor readings of Help (S56) | C | use-with-care |
| Headline formulas | Higher response | Not measured | P | use-with-care |
| Comment on big posts to be seen by recruiters | Visibility | Not measured; ranking by relevance (S50) | P | use-with-care |
| Cold-message hiring managers | 17% replies | S37 not transferable | D | use-with-care |
| LinkedIn Learning certificates | Credibility | None | P | untested |

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Profiles are for checking not being found; 11,000 applications a minute (+45%) dated late 2024; 74% of India recruiters struggle | updated | Search and Hiring Assistant are explicit sourcing tools [S1][S2][S3]. The 11,000 figure was reported 2025-06 [S15]; 9,500 in 2025-10 [S16]. The 74% India figure is confirmed, reported 2026-02-03 [S17], from a LinkedIn survey fielded 2025-11 (6,554 global HR professionals; India sub-sample not stated) [S51] | B |
| K2 | Use LinkedIn and X as a distribution layer, not a separate content programme | unverifiable | No study tests content strategy against hiring outcomes (Absence A4); consistent with topic-relevance ranking [S20] | D |
| K3 | 2026 recruiter Boolean strings for AI/ML key on titles, languages, frameworks, with no certification acronyms | confirmed | Strings in vendor guides [S40]; certification evidence mixed [S9][S10] | C |
| K4 | Eightfold scores title similarity; Phenom uses recruiter-set skills, experience, title, location | confirmed | Vendor documentation [S39]; Phenom page dated 2022-06-23, possibly stale | B |
| K5 | One identity everywhere; consistency lowers false fraud flags (low confidence) | unverifiable | No source on false-flag rates; fraud forecast and verification push noted [S38][S32] | D |
| K6 | Nobody measured profile opens or headline formats; engagement-farming prevalence not found | updated | Stated-behaviour surveys exist [S43]; no behavioural measure or format test; LinkedIn acknowledges pods but publishes no prevalence [S22] | C |
| K7 | Science 2022 weak-ties experiment (over 20M members) | confirmed | Abstract opened [S11] | A |
| K8 | User agreement prohibits automation; account restriction | confirmed | Help text and Section 8.2 as quoted [S23]; comment-visibility line [S22] | B |
| K9 | Pin 17.08% LinkedIn reply rate; not transferable | confirmed | Figure in Pin report [S37]; LinkedIn subset about 276,000–294,000 messages of 4M+, and 16.6% against 4.4% on the same candidates [S55]; vendor COI; transfer judgement stands | B |
| K10 | Premium Career about $39.99 (5 InMails); Sales Navigator Core $119.99 (50); use-with-care; Texas matter | confirmed | $39.99 and $69.99 from the Attorney General [S13]; Core $99.99–$119.99, 5 and 50 InMails [S47]; CID 2026-07-14, no lawsuit found [S14]; no independent benefit evidence | B |

## Absences

| # | Item | Where I looked |
|---|---|---|
| A1 | Published field weighting in Recruiter candidate ordering | S1, S2; Help Center (fetch disallowed) |
| A2 | Independent causal evidence on Open to Work effect on messages or interviews (2024–2026) | Fortune, ERE, interviewing.io, vendor blogs |
| A3 | Behavioural measure of recruiter profile opens; headline-format A/B | Surveys, vendor reports |
| A4 | Evidence that posting or commenting raises recruiter outreach or interviews | Practitioner datasets, LinkedIn tips, one anecdote |
| A5 | LinkedIn-published weekly invitation cap and a consistent free-note allowance | Vendor readings of Help; Help blocked |
| A6 | Controlled Easy Apply against employer-site comparison; applicants per GenAI posting | Huntr, vendor posts |
| A7 | Aggregate headline or About patterns of 2025–2026 hires into the listed roles | Lab-hiring analyses |
| A8 | Independent LinkedIn against Naukri against Instahyre comparison for GenAI hiring in India | Employer guides (COI) |
| A9 | Whether RAG, agents, evaluation or MCP are standard LinkedIn skills | Not checked in the taxonomy |
| A10 | Independent evidence of Premium Career benefit | Reviews, aggregators |
| A11 | Prevalence of engagement farming on LinkedIn and X | Trade coverage |
| A12 | Status of the Texas investigation after the 2026-09 law-firm note | News searches |
| A13 | Opened primary LinkedIn Engineering Blog post of 2026-03-12 | Secondary coverage and arXiv abstracts only |
| A14 | Effect of recommendations, photo, banner and custom URL on reviewer decisions | None found |
| A15 | Evidence on promoted and reposted job labelling | A headline-level report only (promoted-jobs library, 2025-05-26) |
| A16 | Primary source for an "80.6 million fake accounts stopped at registration" figure | Not re-found; earlier use withdrawn |
| A17 | Traceable origin of the "five or more skills" multipliers | Practitioner guides |
| A18 | LinkedIn Help invitation-limit pages read directly | Help fetch disallowed; five vendor readings used |

## Open Questions & Risks

| Objection | Evidence for | Evidence against | Net |
|---|---|---|---|
| Referrals dominate hiring, so profile work is low-yield | Tracker advice to seek referrals; weak-ties experiment | LinkedIn and Pin describe active sourcing and AI search [S1][S3] | Both channels; profile still read |
| All LinkedIn outcome numbers are conflicted | Every uplift claim lacks method [S6][S28][S32][S36] | Mechanics are documented [S2] | Graded C accordingly |
| Huntr data is selection-biased | Self-selected users; Google links to employer sites | Large sample, same pattern over four periods [S29] | Direction credible, size unknown |
| Credential experiment does not transfer to GenAI professionals | Sample is Coursera learners, developing countries, no degrees [S10] | Same experiment shows no effect for strong profiles; interviewing.io shows a negative association [S9] | Rule R7 is conditional |
| LLM feed rebuild makes format data obsolete | Rebuild 2026-03-12; monthly drift in format reach [S20][S27] | Format datasets mostly pre-date it | Treat all format advice as short-lived |
| Verification uplift is selection | Engaged members verify more | LinkedIn describes mechanics, not method [S32] | Low-cost, so kept |
| Open to Work stigma is real or imaginary | Recruiter opinion [S7]; the 2023 authors' caution [S52] | LinkedIn claims benefit [S6] | Unresolved; recruiters-only is the hedge |

Risks: platform facts expire in 90 days; Texas status can change within 14 days; LinkedIn Help claims were not opened; several numbers rest on vendor datasets with COI; a few ledger URLs were carried from search results and not re-opened (flagged in the ledger).

## Discovered Concerns

| # | Concern | Source | Grade |
|---|---|---|---|
| 1 | Hiring Assistant 2 can evaluate ATS applicants, including those who applied off LinkedIn, so profile and CV mismatch may surface at one step (inference) | S44 | D |
| 2 | Connected apps and verification create new personal-data exposure for job seekers | S4, S32 | C |
| 3 | US reported losses to job and employment-agency scams rose from $90M (2020) to $501M (2024) | S54 | B |
| 4 | "Ghost job" lumps evergreen postings with fraud; the Attorney General's range rests on unspecified studies and vendor analyses | S14, S30 | B |
| 5 | Help Center pages refuse automated fetching, so maintainers must verify Help claims by hand | S5 | A |

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Structured fields dominate | Updated | Filters plus keyword anywhere plus semantic reading [S2]; weights unpublished | Do both: fields and text |
| P2 | Open to Work "double" has no method | Confirmed | 2020 blog, repeated 2024 and 2025 [S6][S7][S18] | Grade C |
| P3 | No study links posting to recruiter outreach | Confirmed | None found; LinkedIn claim has no method [S28] | Content optional |
| P4 | Employer sites convert better | Confirmed | 2.9–3.6% against 6.6–9.9% [S29] | R8 |
| P5 | Assessments retired | Confirmed | Help text [S34] | Drop from advice |
| P6 | Fixed published limits | Contradicted | No weekly number on Help pages that vendors checked; about 100 is vendor consensus; the note allowance is stated as 3 or 5 a month on different pages [S56] | Treat the weekly number as folklore |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | AI-Assisted Search and Projects, LinkedIn Talent Solutions, https://business.linkedin.com/hire/ai-assisted-search-and-projects | n.d. | 2026-11-11 | A | Read | COI (value claims) | AI search facts |
| S2 | Using AI-Assisted Search / Semantic Search (PDF), LinkedIn Talent Solutions, https://business.linkedin.com/content/dam/lem/business/en/hire/product-update/Using%20AI-Assisted_Search_Semantic%20Search.pdf | n.d. | 2026-11-11 | A | Read | undated | Filters, keyword rule |
| S3 | LinkedIn announces its next generation recruiter agent, HR Brew, https://www.hr-brew.com/stories/linkedin-announces-its-next-generation-recruiter-agent | 2026-09-30 | 2026-11-11 | B | Read | re-read in verification pass | Hiring Assistant 2 |
| S4 | Visibility builds credibility (connected apps), LinkedIn Newsroom, https://news.linkedin.com/2026/visibility-builds-credibility---the-tools-you-use-every-day--now | 2026-06-17 | 2026-11-11 | A | Read | — | Connected apps |
| S5 | Let recruiters know you're open to work, LinkedIn Help, https://www.linkedin.com/help/linkedin/answer/67405 | n.d. | 2026-11-11 | B | Extract | fetch blocked | Open to Work, India fields |
| S6 | To Find Your Next Job More Quickly, Tell Your Community You're Open to Work, LinkedIn Blog, https://blog.linkedin.com/2020/october/29/the-benefits-of-sharing-with-your-community-you-re-open-to-work | 2020-10-29 | 2026-11-11 | C | Extract | COI; pre-window; text confirmed in verification pass | 2x, 40%, 20% claims; ranking signal |
| S7 | Millions use the #opentowork badge on LinkedIn, Fortune, https://fortune.com/2024/09/05/linkedin-opentowork-badge-recruiters-job-search/ | 2024-09-05 | 2026-11-11 | B | Read | — | Counts; recruiter views |
| S8 | Who's open to work?, interviewing.io, https://interviewing.io/blog/whos-open-to-work-a-tale-of-two-labor-markets | 2023-04 | 2026-11-11 | B | Extract | COI; pre-window; figures verified via S52 | Badge candidate quality |
| S9 | Why you shouldn't list certifications on LinkedIn, interviewing.io, https://interviewing.io/blog/why-you-shouldnt-list-certifications-on-linkedIn | n.d. (c. 2023) | 2026-11-11 | B | Read | COI; pre-window | Certification association |
| S10 | The Value of Non-Traditional Credentials in the Labor Market, Athey and Palikot, arXiv, https://arxiv.org/pdf/2405.00247v2 | 2025-11-06 | 2026-11-11 | B | Read | preprint | Credential experiment |
| S11 | A causal test of the strength of weak ties, Science 377(6612), https://pubmed.ncbi.nlm.nih.gov/36107999/ | 2022-09-16 | 2026-11-11 | A | Read | LinkedIn co-authors; pre-window | Weak ties |
| S12 | LinkedIn training in South Africa, J-PAL, https://www.povertyactionlab.org/evaluation/improving-youth-employment-opportunities-and-reducing-information-barriers-through | n.d. (paper 2019–2021) | 2026-11-11 | B | Extract | pre-window | Training experiment |
| S13 | Attorney General Ken Paxton Investigates LinkedIn, Texas Attorney General, https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-investigates-linkedin-advertising-fake-and-misleading-job-opportunities | 2026-07-14 | 2026-11-11 | A | Read | allegations; re-read in verification pass | Texas CID; prices |
| S14 | Texas investigation coverage: Fox 9 https://www.fox9.com/news/texas-launches-investigates-linkedin-over-claims-ghost-jobs ; Fox Business https://www.foxbusiness.com/technology/texas-investigates-linkedin-over-alleged-ghost-jobs-targeting-job-seekers.amp ; AfroTech https://afrotech.com/linkedin-is-being-investigated-in-texas-for-alleged-high-volume-of-ghost-jobs ; Bloomberg Government https://news.bgov.com/texas-brief/texas-probes-linkedin-for-advertising-fake-job-opportunities ; ERE https://www.ere.net/articles/texas-takes-aim-at-linkedin-over-ghost-jobs ; ClearanceJobs https://news.clearancejobs.com/2026/07/30/texas-ag-launched-investigation-of-linkedin-over-premium-subscriptions/ ; Foley & Lardner https://www.foley.com/insights/publications/2026/09/how-to-improve-hiring-transparency-amid-ghost-job-scrutiny/ | 2026-07-14 to 2026-09 | 2026-11-11 | B | Extract | corroborated; ClearanceJobs URL carried from earlier results | LinkedIn response; no charge or lawsuit; Greenhouse corroboration |
| S15 | Job Seekers Flood LinkedIn With 11,000 Applications a Minute, eWeek, https://www.eweek.com/news/ai-job-applications-linkedin/ ; Semafor 2025-06-24 (URL not retained) | 2025-06-25 | 2026-11-11 | B | Extract | secondary of NYT | 11,000 a minute |
| S16 | Recruiters are drinking through a fire hose (CNBC), Recruiting News Network, https://www.recruitingnewsnetwork.com/posts/recruiters-are-drinking-through-a-fire-hose-of-job-applications-experts-say--ai-is-partially-to-blame | 2025-10-30 | 2026-11-11 | B | Read | — | 9,500 a minute |
| S17 | AI-generated job applications add to hiring challenges in India, Storyboard18, https://storyboard18.com/digital/ai-generated-job-applications-add-to-hiring-challenges-in-india-report-88724.htm | 2026-02-03 | 2026-11-11 | B | Extract | single-source at article level | India 74% |
| S18 | LinkedIn adds notice period and salary, Newsbytes, https://www.newsbytesapp.com/news/science/linkedin-now-lets-job-seekers-add-notice-period-salary-expectations/story | 2025-10-09 | 2026-11-11 | B | Extract | corroborated with S5 | India fields; 42% claim |
| S19 | Enterprise recruiting tools (India), LinkedIn Talent Solutions, https://business.linkedin.com/en-in/talent-solutions/enterprise-recruiting-tools?ss=1 | n.d. | 2026-11-11 | B | Extract | — | Notice and salary filters |
| S20 | LinkedIn updates its Feed algorithm, Social Media Today, https://www.socialmediatoday.com/news/linkedin-updates-its-feed-algorithm/814638/ ; ppc.land (URL not retained) | 2026-03-12 | 2026-11-11 | B | Extract | secondary for LinkedIn Engineering post | Feed architecture |
| S21 | Large Scale Retrieval for the LinkedIn Feed using Causal Language Models, arXiv 2510.14223; From Features to Transformers, arXiv 2502.03417 | 2025-10; 2025-02 | 2026-11-11 | A | Extract | LinkedIn authors; abstracts | Feed models |
| S22 | LinkedIn Outlines New Measures To Combat Fake Engagement, Social Media Today, https://www.socialmediatoday.com/news/linkedin-limit-visibility-of-comments-made-via-automation-tools/758207/ | 2025-08-20 | 2026-11-11 | B | Read | quotes Help text | Automation limits |
| S23 | Prohibited software and extensions, LinkedIn Help, https://www.linkedin.com/help/linkedin/answer/a1341387 ; User Agreement 8.2 as quoted at https://contentin.io/blog/linkedin-mcp-terms-of-service/ | n.d.; 2026-07-28 | 2026-11-11 | B | Extract | corroborated | K8 |
| S24 | How Often Should You Post on LinkedIn, Buffer, https://buffer.com/resources/how-often-to-post-on-linkedin | 2025-08-28 | 2026-11-11 | B | Extract | COI | Cadence |
| S25 | Best Content Format on Social Platforms, Buffer, https://buffer.com/resources/data-best-content-format-social-media | 2026 | 2026-11-11 | B | Extract | COI | Formats |
| S26 | LinkedIn Study 2026, Metricool, via Merca2.0, https://www.merca20.com/?p=12616961 | 2026 | 2026-11-11 | B | Extract | COI; company pages | Formats |
| S27 | Ordinal https://www.tryordinal.com/blog/linkedin-marketing-strategy ; The Shield Index https://theshieldindex.beehiiv.com/p/march-2026-linkedin-reach-by-content-format | 2026 | 2026-11-11 | C | Extract | COI | Conflicting formats |
| S28 | LinkedIn performance tips, Social Media Today, https://www.socialmediatoday.com/news/linkedin-shares-tips-on-how-to-boost-your-in-app-performance-in-2026/808448/ | 2026 | 2026-11-11 | C | Extract | COI | 5x claim |
| S29 | Huntr Research: https://huntr.co/research/job-search-trends-q3-2026 ; https://huntr.co/research/best-job-boards ; https://huntr.co/research/2025-annual-job-search-trends-report | 2025–2026 | 2026-11-11 | B | Extract | COI; self-selected | Source rates |
| S30 | Greenhouse ghost-job analysis as reported by Xeito, https://xeito.ai/en/blog/spotting-ghost-job-postings-2026/ ; corroborated by Foley & Lardner (S14) | 2024; reported 2025-08 | 2026-11-11 | B | Extract | COI (ATS vendor); CRS caution via secondary; Xeito URL carried from search results | Ghost-job prevalence |
| S31 | One in three tech jobs is still up 60 days after posting, Hotfix Research, https://hotfix.jobs/blog/ghost-job-rate-q2-2026 | 2026-06-29 | 2026-11-11 | B | Extract | single-source | Staleness |
| S32 | LinkedIn adds new tools to fight fake profiles, TechCrunch, https://techcrunch.com/2026/09/23/linkedin-adds-new-tools-to-fight-fake-profiles-and-bogus-work-histories/ | 2026-09-23 | 2026-11-11 | B | Read | LinkedIn claims COI | Verification |
| S33a | LinkedIn expands company verification, mandates workplace checks, Help Net Security, https://www.helpnetsecurity.com/2025/09/04/linkedin-expands-company-verification-workplace-checks/ | 2025-09-04 | 2026-11-11 | B | Extract | COI | 90M verified; recruiter and leadership checks; uplift claims |
| S33b | New LinkedIn verification features, People Matters, https://www.peoplematters.in/news/strategic-hr/new-linkedin-verification-features-aim-to-protect-job-seekers-amid-uncertainty-43377 | n.d. (c. 2025-09) | 2026-11-11 | C | Extract | COI | 13% claim |
| S33c | LinkedIn's profile verification push is accelerating, TechCrunch, https://techcrunch.com/2025/12/18/linkedins-profile-verification-push-is-accelerating-and-india-is-leading-the-charge-in-2025 | 2025-12-18 | 2026-11-11 | B | Extract | LinkedIn statements | 100M; 60% and 27% split |
| S34 | Skill Assessments, LinkedIn Help, https://www.linkedin.com/help/linkedin/answer/94427 ; https://www.linkedin.com/help/learning/answer/a1690529 | n.d. | 2026-11-11 | B | Extract | fetch blocked | Assessments retired |
| S35 | LinkedIn is removing the Creator Mode option, Social Media Today, https://www.socialmediatoday.com/news/linkedins-removing-creator-mode-option/706585/ | 2024-02 | 2026-11-11 | B | Extract | — | Creator mode |
| S36 | Get hired faster, LinkedIn Premium, https://premium.linkedin.com/careers/get-hired-faster | n.d. (data 2024-01 to 2025-03) | 2026-11-11 | C | Extract | COI | Premium claims |
| S37 | Recruiting Outreach Benchmarks 2026, Pin, https://www.pin.com/blog/recruiting-outreach-benchmark-report/ ; https://www.pin.com/blog/automated-candidate-outreach/ | 2026 (data 2025-06 to 2026-05) | 2026-11-11 | B | Extract | COI | Reply rates |
| S38 | Gartner Survey Shows Only 26% of Job Applicants Trust AI, Gartner, https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them | 2025-07-31 | 2026-11-11 | B | Extract | forecast | Fraud context |
| S39 | Eightfold https://eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring ; Phenom https://www.phenom.com/blog/recruiters-can-use-ai-to-screen-source-and-hire-candidates | n.d.; 2022-06-23 | 2026-11-11 | B | Extract | COI; Phenom page stale | K4 |
| S40 | AI/ML Boolean guides: Pin https://ghost.pin.com/boolean-search-advanced-strings/ ; Juicebox https://juicebox.ai/blog/boolean-string-search-examples ; Taggd https://taggd.in/blogs/linkedin-boolean-search/ ; GCC Journal https://gccjournal.in/recruitment/gcc-recruiter-boolean-search-playbook/ | 2026 | 2026-11-11 | C | Extract | vendor content | K3 |
| S41 | Jobs on the Rise 2026 via Dice https://www.dice.com/career-advice/ai-related-jobs-top-linkedins-fastest-growing-roles-list-for-2026 ; LinkedIn News https://news.linkedin.com/2026/new-linkedin-research-finds-women-account-for-just-26-percent-of-ai-hires-as-ai-jobs-surge | 2026 | 2026-11-11 | B | Extract | — | GenAI titles, skills |
| S42 | Analysis of 1,680 Anthropic engineer profiles, TechTimes, https://www.techtimes.com/articles/318396/20260615/anthropic-engineering-team-infrastructure-army-new-analysis-1680-engineers.htm | 2026-06-11 | 2026-11-11 | C | Extract | COI; single-source | Profile patterns |
| S43 | Hiring managers and social screening, Software Finder, https://softwarefinder.com/resources/hiring-managers-social-media-recruiting-screening ; Challenger Gray 2017 via Security Magazine (URL not retained) | 2026; 2017 | 2026-11-11 | C | Extract | vendor survey; 2017 stale | K6 |
| S44 | Hiring Assistant globally available, LinkedIn News, https://news.linkedin.com/2025/hiring-assistant-globally-available ; https://business.linkedin.com/talent-solutions/hiring-assistant ; Pin https://www.pin.com/blog/linkedin-recruiter-new-features/ | 2025-09-04 | 2026-11-11 | B | Extract | Pin part C | Feature timeline |
| S45 | India channel sources: Careers360 https://news.careers360.com/tech-hiring-india-2026-entry-senior-level-jobs-data-engineering-share-doubles-freshers-experienced-linkedin-naukri-job-posting ; The Peoples Board https://www.thepeoplesboard.com/recruitment/recruitment-statistics-india-2026-whos-hiring-how-fast-and-what-it-costs/ ; Cutshort https://cutshort.io/best-platforms-to-hire-software-engineers-in-india ; Wisemonk (URL not retained) | 2026 | 2026-11-11 | C | Extract | COI; notice-period claim D | India context |
| S46 | Vendor explainers on personalised-note acceptance (Expandi, Contentin, Taplio, Salesforge); URLs not retained | 2025–2026 | 2026-11-11 | D | Extract | vendors; no method | Acceptance claims |
| S47 | Premium pricing aggregators: Overloop https://overloop.com/blog/linkedin-sales-navigator-pricing ; Kanbox; Temperstack; Leonar (URLs not retained) | 2026 | 2026-11-11 | C | Extract | conflicting; Overloop URL carried from search results | Prices, InMails |
| S48 | I quit posting on LinkedIn for 30 days, dev.to, https://dev.to/charliemorrison/i-quit-posting-on-linkedin-for-30-days-and-got-more-recruiter-outreach-here-is-what-replaced-it-2ddp | n.d. | 2026-11-11 | D | Extract | anecdote | Falsification |
| S49 | LinkedIn launches verified AI skill levels, Dataconomy, https://dataconomy.com/?p=88782 | 2026-01-29 | 2026-11-11 | C | Read | secondary | Verified skills |
| S50 | LinkedIn Comment Ranking Update, Vulse, https://vulse.co/blog/linkedin-comment-ranking-update ; Kompozy (URL not retained) | 2026-08 | 2026-11-11 | C | Extract | secondary | Comment ranking |
| S51 | LinkedIn Research: Talent 2026, LinkedIn Newsroom, https://news.linkedin.com/2026/LinkedIn-Research-Talent-2026 | n.d. (survey fielded 2025-11) | 2026-11-11 | A | Extract | COI (value claims) | Survey method; agent claims |
| S52 | Should you post that you're #OpenToWork, TechCrunch (interviewing.io authors), https://techcrunch.com/2023/04/03/should-you-post-that-youre-opentowork-a-tale-of-two-labor-markets ; The Debate Over Open to Work, ERE, https://ere.net/articles/the-debate-over-open-to-work | 2023-04-03; 2023-11-15 | 2026-11-11 | B | Extract | COI; pre-window | Verified badge figures |
| S53 | Understanding dwell time to improve LinkedIn feed ranking, LinkedIn Engineering, https://engineering.linkedin.com/blog/2020/understanding-feed-dwell-time | 2020-05-12 | 2026-11-11 | B | Extract | pre-window; extract only | Dwell time |
| S54 | New FTC data show a big jump in reported losses to fraud, FTC, https://www.ftc.gov/news-events/news/press-releases/2025/03/new-ftc-data-show-big-jump-reported-losses-fraud-125-billion-2024 | 2025-03-10 | 2026-11-11 | B | Extract | government source; snippets only | Job-scam losses |
| S55 | Pin: https://www.pin.com/blog/how-to-write-recruiting-pitch ; https://www.pin.com/blog/email-vs-linkedin-vs-sms-recruiting/ ; https://www.pin.com/blog/ai-vs-human-recruiting-outreach-study | 2026 | 2026-11-11 | B | Extract | COI | Subset sizes; same-candidate rates |
| S56 | Invitation-limit readings of LinkedIn Help: enrow https://enrow.io/en/blog/linkedin-limits ; Revenueflow https://www.revenueflow.com/blog/linkedin-connection-limit ; Swarmhit https://www.swarmhit.com/blog/linkedin-connection-limits ; Useartemis https://useartemis.co/blog/how-many-linkedin-invites-per-week ; Outreachbloom https://outreachbloom.com/linkedin-connection-request | 2026-08 to 2026-10 | 2026-11-11 | C | Extract | vendors; mutually consistent; Help pages not opened | Invitation limits |
| S57 | What LinkedIn has published about how the feed ranks posts, Recurpost, https://blog.recurpost.com/?p=34 | 2026-08-24 | 2026-11-11 | C | Extract | practitioner inventory | Feed documentation inventory |
| S58 | LinkedIn endorsements are dumb, interviewing.io, https://interviewing.io/blog/linkedin-endorsements-useless | n.d. | 2026-11-11 | C | Extract | COI; pre-window; snippet | Endorsements |
| S59 | LinkedIn announces verification for recruiters, via Recruiting News Network, https://www.recruitingnewsnetwork.com/posts/sociable-linkedin-announces-verification-for-recruiters-to-help-address-scam-pitches | 2024-04-16 | 2026-11-11 | B | Extract | — | Recruiter badge |
| S60 | LinkedIn-Profil-Optimierung 2026, ResumeGeni, https://resumegeni.com/de/blog/linkedin-profile-optimization-guide-2026 | 2026 | 2026-11-11 | D | Extract | vendor; untraced multipliers | Skills multipliers |

### Verification pass (2026-11-11): changes from the first draft

| # | Change | Basis |
|---|---|---|
| 1 | Cross-reference to the primary blog absence corrected (reads A13) | Absences table |
| 2 | S14 relabelled; unverified AOL and Fox 7 Austin URLs dropped; seven Texas sources listed; a candidacy remark withdrawn | S14 |
| 3 | S17: an item that appears to report a different survey removed; survey base added | S51 |
| 4 | S49 URL corrected to the page fetched | Fetch record |
| 5 | $501M job-scam figure re-sourced to the FTC; "recruiter impersonation reports" withdrawn | S54 |
| 6 | The combined verification row was split into S33a, S33b and S33c with URLs; an unsourced 80.6M fake-account figure withdrawn (A16) | S33a, S33b, S33c |
| 7 | Pin LinkedIn subset changed from "about 294,000" to "about 276,000–294,000"; same-candidate 16.6% against 4.4% added | S55 |
| 8 | Invitation limits: "3 to 10 a month" corrected to 3 or 5 a month on different Help pages; no weekly number; "about 100" is vendor consensus | S56 |
| 9 | S3 date verified as 2026-09-30; Hiring Assistant 2 details added | S3 |
| 10 | S6 text confirmed; documented ranking signal added; rule R15 added | S6 |
| 11 | S8 figures verified (44%, 56%, 51%, 1.4%, 4.2%) | S52 |
| 12 | Dwell time, sequence-recommender inventory and 360Brew caution added to KF8 and DF6 | S53, S57 |
| 13 | Endorsements row added | S58 |
| 14 | Texas status extended to the 2026-09 law-firm note; Attorney General and LinkedIn spokesperson statements re-checked | S13, S14 |
| 15 | Greenhouse 18–22% corroborated; unverified Fox 29 URL dropped | S14, S30 |
| 16 | Withdrawn as unverifiable: a reply-rate decline for automated connection requests; a "21x" photo multiplier; People Matters and Analytics Insight rows without URLs; Hans India row for S18 | — |

## Data Appendix

```jsonl
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Published weighting of profile fields in LinkedIn Recruiter candidate ordering", "searched": "LinkedIn Talent Solutions pages and playbook (S1, S2); Help Center (automated fetch disallowed); vendor explainers", "note": "Filters and matching mechanics are documented; weights and tie-breaks are not."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Independent causal evidence that Open to Work (either form) changes recruiter messages or interview rates, 2024-2026", "searched": "Fortune, ERE, interviewing.io, vendor blogs, experiment and stigma-study searches", "note": "Only LinkedIn claims, recruiter opinion and a 2023 candidate-quality dataset."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Behavioural measurement of how often recruiters open candidate LinkedIn profiles; headline-format A/B evidence", "searched": "Hiring-manager surveys, vendor reports", "note": "Stated-behaviour surveys only."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Evidence that posting or commenting raises recruiter outreach or interview invitations for job seekers", "searched": "Practitioner datasets, LinkedIn performance tips, trace of 'daily posting triples recruiter views'", "note": "LinkedIn's up-to-5x profile-view claim has no method; one anecdote points the other way."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "LinkedIn-published weekly invitation cap and a consistent free personalised-note allowance", "searched": "Vendor readings of Help; Help fetch blocked", "note": "About 100 a week is vendor consensus; notes are stated as 3 or 5 a month on different pages."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Controlled comparison of Easy Apply against employer-site applications; applicant counts per GenAI posting", "searched": "Huntr reports, vendor posts", "note": "Only self-selected tracker association."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Aggregate headline and About patterns of 2025-2026 hires into the listed GenAI roles", "searched": "Lab-hiring analyses, talent reports", "note": "One single-author analysis of engineer profiles at one employer."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Independent comparison of LinkedIn, Naukri and Instahyre effectiveness for GenAI hiring in India", "searched": "Employer-side guides, trade reports", "note": "Only vendor and employer-guide claims."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Confirmation that RAG, agents, evaluation and MCP are standard LinkedIn skills", "searched": "Jobs on the Rise coverage", "note": "Only Large Language Models, MLOps and computer vision were seen named."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Independent evidence of Premium Career benefit", "searched": "Reviews and aggregators", "note": "Only LinkedIn-reported claims."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Prevalence of engagement farming on LinkedIn and X", "searched": "Trade coverage, LinkedIn statements", "note": "LinkedIn acknowledges pods and automation; no prevalence published."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Status of the Texas investigation after the 2026-09 law-firm note", "searched": "News searches for lawsuit or settlement", "note": "No later item found."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Opened primary LinkedIn Engineering Blog post of 2026-03-12", "searched": "Secondary coverage and arXiv abstracts", "note": "Primary page not opened."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Effect of recommendations, photo, banner and custom URL on reviewer decisions", "searched": "Vendor and practitioner sources", "note": "Only untraceable multipliers."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Evidence on promoted and reposted job labelling", "searched": "Trade headlines", "note": "Headline-level report of a promoted-jobs library (2025-05-26); not opened."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Primary source for an '80.6 million fake accounts stopped at registration, 2024-07 to 2024-12' figure", "searched": "Not re-found in the verification pass", "note": "Earlier use withdrawn; check LinkedIn's Community Report."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "Traceable origin of 'five or more skills give 17x views and 33x messages'", "searched": "Practitioner guides; one 2026 guide gives 31x", "note": "No LinkedIn source or method found."}
{"type": "absence", "grade": "E", "src": [], "as_of": "2026-11-11", "item": "LinkedIn Help invitation-limit pages read directly", "searched": "Help Center fetch disallowed; five vendor readings used instead", "note": "Pages reportedly disagree on the free personalised-note allowance (3 or 5 a month)."}
{"type": "measure", "grade": "B", "src": ["S15"], "as_of": "2025-06-24", "ttl": "V3", "subject": "LinkedIn job applications submitted", "measure": "applications per minute", "unit": "applications per minute", "value": 11000, "method": "LinkedIn data reported by the New York Times, relayed by eWeek", "region": "global", "note": "Reported with +45% year on year; K1 dated it late 2024; a LinkedIn representative later gave nearly 9,500 per minute (S16)."}
{"type": "measure", "grade": "B", "src": ["S16"], "as_of": "2025-10-29", "ttl": "V3", "subject": "LinkedIn job applications submitted", "measure": "applications per minute", "unit": "applications per minute", "value": 9500, "method": "LinkedIn representative via CNBC, 'nearly 9,500'", "region": "global", "note": "Conflicts with 11,000; kept as a range."}
{"type": "measure", "grade": "B", "src": ["S15"], "as_of": "2025-06-24", "ttl": "V3", "subject": "LinkedIn job applications per minute", "measure": "year-on-year increase", "unit": "percent", "value": 45, "method": "Reported with the 11,000 figure", "region": "global", "note": "Second-hand."}
{"type": "measure", "grade": "B", "src": ["S17", "S51"], "as_of": "2026-02-03", "ttl": "V3", "subject": "India recruiters finding it harder to find qualified candidates", "measure": "share of recruiters", "unit": "percent", "value": 74, "region": "India", "method": "LinkedIn research as reported; survey base Censuswide for LinkedIn, 6,554 global HR professionals, fielded 2025-11-10 to 2025-11-27", "note": "India sub-sample size not stated; hiring activity 40% above pre-pandemic."}
{"type": "measure", "grade": "B", "src": ["S17"], "as_of": "2026-02-03", "ttl": "V3", "subject": "India recruiters saying hiring is harder who cite AI-generated applications", "measure": "share", "unit": "percent", "value": 53, "region": "India", "method": "LinkedIn research as reported", "note": "47% cite skills shortages."}
{"type": "measure", "grade": "B", "src": ["S7"], "as_of": "2024-07-01", "ttl": "V3", "subject": "Members with Open to Work switched on behind the scenes", "measure": "members", "unit": "members", "value": 200000000, "method": "LinkedIn statement to Fortune", "note": "Month described is July 2024; the day is not stated."}
{"type": "measure", "grade": "B", "src": ["S7"], "as_of": "2024-07-01", "ttl": "V3", "subject": "Members displaying the public Open to Work frame", "measure": "members", "unit": "members", "value": 40000000, "method": "LinkedIn statement to Fortune", "note": "Month described is July 2024; the day is not stated."}
{"type": "measure", "grade": "C", "src": ["S6", "S7"], "as_of": "2020-10-29", "ttl": "V3", "subject": "Public Open to Work frame effect on InMails", "measure": "more InMails received", "unit": "percent", "value": 40, "method": "LinkedIn claim, no method", "note": "Pre-window; repeated 2024-09-05."}
{"type": "measure", "grade": "C", "src": ["S6"], "as_of": "2020-10-29", "ttl": "V3", "subject": "Public Open to Work frame effect on messages from the community", "measure": "more messages from the LinkedIn community", "unit": "percent", "value": 20, "method": "LinkedIn early results, no method", "note": "Over three million members had added the frame."}
{"type": "measure", "grade": "C", "src": ["S18"], "as_of": "2025-10-09", "ttl": "V3", "subject": "Recruiters using the skills filter weekly", "measure": "share of recruiters", "unit": "percent", "value": 42, "region": "global", "method": "LinkedIn claim, no method", "note": "Same release repeats 'double' recruiter messages for Open to Work."}
{"type": "measure", "grade": "B", "src": ["S29"], "as_of": "2026-09-30", "ttl": "V3", "subject": "LinkedIn-sourced applications reaching interview", "measure": "interview rate", "unit": "percent", "value": 3.6, "n": 175416, "method": "Huntr tracker users, trailing 12 months, Q3 2026 preview", "note": "Self-selected; Google-sourced 9.9%; preview date approximate."}
{"type": "measure", "grade": "B", "src": ["S29"], "as_of": "2026-09-30", "ttl": "V3", "subject": "Google-sourced applications reaching interview", "measure": "interview rate", "unit": "percent", "value": 9.9, "method": "Huntr tracker users, trailing 12 months, Q3 2026 preview", "note": "Preview date approximate."}
{"type": "measure", "grade": "B", "src": ["S29"], "as_of": "2026-07-01", "ttl": "V3", "subject": "Interview rate: Indeed against Google Jobs", "measure": "interview rate", "unit": "percent", "lo": 2.92, "hi": 6.6, "n": 1240000, "method": "Huntr tracked applications 2024-10-01 to 2026-07-01", "note": "Lo is Indeed, hi is Google Jobs."}
{"type": "measure", "grade": "B", "src": ["S29"], "as_of": "2026-09-30", "ttl": "V3", "subject": "Employer career sites against job boards", "measure": "interview-rate multiple", "unit": "times", "value": 1.7, "method": "Huntr tracker users, Q3 2026 preview", "note": "Self-selected."}
{"type": "measure", "grade": "B", "src": ["S30", "S14"], "as_of": null, "ttl": "V3", "subject": "Postings on the Greenhouse platform classified as ghost jobs", "measure": "share per quarter", "unit": "percent", "lo": 18, "hi": 22, "method": "Greenhouse analysis of its own platform, 2024", "note": "Analysis month not confirmed; Q2 2025 reported 17%; a CRS primer cautions that quoted figures come from vendors."}
{"type": "measure", "grade": "B", "src": ["S31"], "as_of": "2026-04-28", "ttl": "V1", "subject": "Tech listings still live at 60 days", "measure": "share", "unit": "percent", "value": 33, "n": 13434, "method": "Hotfix tracked ATS listings 2026-02-28 to 2026-04-28", "note": "About one in eight live at 90 days; staleness, not intent."}
{"type": "measure", "grade": "C", "src": ["S13"], "as_of": "2026-07-14", "ttl": "V0", "subject": "Ghost jobs share of online listings", "measure": "share", "unit": "percent", "lo": 20, "hi": 33, "method": "Texas Attorney General cites unspecified independent studies", "note": "Allegation context; vendor analyses are the traceable sources."}
{"type": "measure", "grade": "B", "src": ["S32"], "as_of": "2026-09-23", "ttl": "V2", "subject": "LinkedIn verified members", "measure": "members", "unit": "members", "value": 115000000, "method": "LinkedIn statement to TechCrunch", "note": "Over 700,000 companies verified."}
{"type": "measure", "grade": "B", "src": ["S34"], "as_of": "2025-12-18", "ttl": "V3", "subject": "LinkedIn members with at least one verification", "measure": "members", "unit": "members", "value": 100000000, "method": "LinkedIn statement to TechCrunch", "note": "About 60% workplace and 27% government ID; about 30 million verifications added a year."}
{"type": "measure", "grade": "B", "src": ["S38"], "as_of": "2025-07-31", "ttl": "V3", "subject": "Candidates admitting interview fraud", "measure": "share", "unit": "percent", "value": 6, "n": 3000, "method": "Gartner survey 2Q25", "note": "Forecast of 1 in 4 profiles fake by 2028 is a prediction."}
{"type": "measure", "grade": "B", "src": ["S37"], "as_of": "2026-05-31", "ttl": "V3", "subject": "Recruiter-sent LinkedIn messages receiving a reply", "measure": "reply rate", "unit": "percent", "value": 17.08, "n": null, "method": "Pin platform data, 2025-06 to 2026-05", "note": "Vendor COI; LinkedIn subset about 276,000 to 294,000 messages inside a 4M+ set (S55); not candidate-initiated; n left null because Pin pages differ."}
{"type": "measure", "grade": "B", "src": ["S55"], "as_of": "2026-05-31", "ttl": "V3", "subject": "Recruiter LinkedIn messages inside Pin's benchmark", "measure": "LinkedIn messages in the sample", "unit": "messages", "lo": 276000, "hi": 294000, "method": "Pin pages differ on the subset size", "note": "Total set 4M+ messages, mostly email."}
{"type": "measure", "grade": "B", "src": ["S55"], "as_of": "2026-05-31", "ttl": "V3", "subject": "Same 165,000+ candidates contacted on LinkedIn and email by recruiting teams", "measure": "reply rate on LinkedIn", "unit": "percent", "value": 16.6, "n": 165000, "method": "Pin platform data, trailing 12 months", "note": "Email 4.4% for the same candidates; vendor COI."}
{"type": "measure", "grade": "C", "src": ["S37"], "as_of": "2024-04-30", "ttl": "V3", "subject": "LinkedIn InMail reply rate", "measure": "average reply rate", "unit": "percent", "value": 6.4, "method": "LinkedIn analysis 2023-05 to 2024-04, relayed by Pin", "note": "Second-hand."}
{"type": "measure", "grade": "B", "src": ["S10"], "as_of": "2025-11-06", "ttl": "V5", "subject": "Credential sharing on LinkedIn, effect on new employment", "measure": "percentage-point increase", "unit": "percentage points", "value": 1.0, "n": null, "method": "Randomised experiment, over 800,000 Coursera learners encouraged; baseline 17.3%", "note": "5.9% relative; concentrated in weak-baseline learners; analysed sample size not re-verified."}
{"type": "measure", "grade": "B", "src": ["S12"], "as_of": "2021-02-21", "ttl": "V5", "subject": "Four hours of LinkedIn training, end-of-programme employment", "measure": "percentage-point increase", "unit": "percentage points", "value": 7, "n": 1638, "method": "Randomised trial, South Africa, comparison mean 70%", "region": "South Africa", "note": "Pre-window."}
{"type": "measure", "grade": "B", "src": ["S9"], "as_of": null, "ttl": "V5", "subject": "Engineer profiles listing certifications, interview pass rate", "measure": "pass rate", "unit": "percent", "lo": 53, "hi": 57, "method": "interviewing.io dataset of about 20,000 profiles; 53% with certification against 57% without", "note": "Pre-window; post date not shown."}
{"type": "measure", "grade": "B", "src": ["S52"], "as_of": "2023-04-03", "ttl": "V3", "subject": "Engineers showing the Open to Work badge in 2021", "measure": "interview pass rate", "unit": "percent", "value": 44, "method": "interviewing.io platform data cross-referenced with LinkedIn profiles; average pass rate 51%", "note": "Pre-window; vendor COI; badge prevalence 1.4% among 10,000+ people with LinkedIn data."}
{"type": "measure", "grade": "B", "src": ["S52"], "as_of": "2023-04-03", "ttl": "V3", "subject": "Engineers showing the Open to Work badge in Q1 2023", "measure": "interview pass rate", "unit": "percent", "value": 56, "method": "As above; 5 pp above the average", "note": "Badge prevalence 4.2%; the sign reversed after the 2022-2023 layoffs."}
{"type": "measure", "grade": "B", "src": ["S25"], "as_of": null, "ttl": "V3", "subject": "LinkedIn carousel (PDF) posts", "measure": "median engagement rate", "unit": "percent", "value": 21.77, "method": "Buffer analysis of 52M+ posts", "note": "Report date not confirmed; engagement, not hiring; conflicts with S26 and S27."}
{"type": "measure", "grade": "C", "src": ["S28"], "as_of": null, "ttl": "V3", "subject": "Members posting twice a week", "measure": "profile views multiple", "unit": "times", "value": 5, "method": "LinkedIn claim, 'up to', no method", "note": "Page date not confirmed; not recruiter views."}
{"type": "measure", "grade": "C", "src": ["S36"], "as_of": "2025-01-01", "ttl": "V3", "subject": "Premium subscribers applying to Top applicant jobs", "measure": "hired more likely", "unit": "times", "value": 3.9, "method": "LinkedIn data, January 2025, no method", "note": "COI; day not stated; Top choice claim is +43% recruiter messages (Jan 2024)."}
{"type": "measure", "grade": "A", "src": ["S13"], "as_of": "2026-07-14", "ttl": "V2", "subject": "LinkedIn Premium Career monthly price", "measure": "price per month", "unit": "USD per month", "value": 39.99, "region": "Texas, USA", "method": "Stated in the Attorney General's release as approximate", "note": "Premium Business 69.99; aggregators list 29.99 for Career."}
{"type": "measure", "grade": "C", "src": ["S42"], "as_of": "2026-06-11", "ttl": "V3", "subject": "Engineers at one frontier lab holding a PhD", "measure": "share", "unit": "percent", "value": 13.7, "n": 1680, "method": "Single-author analysis of public LinkedIn profiles", "note": "COI; survivorship bias."}
{"type": "measure", "grade": "D", "src": ["S45"], "as_of": null, "ttl": "V3", "subject": "Indian tech notice periods", "measure": "typical notice period", "unit": "days", "lo": 60, "hi": 90, "region": "India", "method": "Vendor statement; source URL not retained", "note": "Not measured."}
{"type": "measure", "grade": "B", "src": ["S54"], "as_of": "2024-12-31", "ttl": "V4", "subject": "US reported losses to job and employment-agency scams", "measure": "reported losses in 2024", "unit": "USD", "value": 501000000, "region": "US", "method": "FTC Consumer Sentinel reports", "note": "90 million USD in 2020; reports about tripled 2020 to 2024; self-reported."}
{"type": "measure", "grade": "B", "src": ["S51"], "as_of": "2025-11-27", "ttl": "V3", "subject": "LinkedIn talent research sample", "measure": "global HR professionals surveyed", "unit": "respondents", "value": 6554, "region": "global", "method": "Censuswide for LinkedIn, fielded 2025-11-10 to 2025-11-27", "note": "India sub-sample size not stated; 19,113 consumers also surveyed."}
{"type": "measure", "grade": "C", "src": ["S51"], "as_of": null, "ttl": "V3", "subject": "Hiring Assistant early adopters", "measure": "fewer profiles reviewed", "unit": "percent", "value": 62, "method": "LinkedIn claim, no method", "note": "Page date not shown; COI; 69% better InMail acceptance also claimed."}
{"type": "measure", "grade": "B", "src": ["S51"], "as_of": null, "ttl": "V3", "subject": "Recruiters planning to increase AI use for pre-screening interviews in 2026", "measure": "share of recruiters", "unit": "percent", "value": 66, "region": "global", "method": "LinkedIn research, Censuswide survey fielded 2025-11", "note": "Page date not shown."}
{"type": "measure", "grade": "C", "src": ["S34"], "as_of": null, "ttl": "V3", "subject": "LinkedIn claim for verified profiles", "measure": "more responses from recruiters", "unit": "percent", "value": 13, "method": "LinkedIn India release as reported; no method", "note": "Article date not shown (c. 2025-09); also 60% more views and 30% more connection requests; COI; likely selection."}
{"type": "practice", "grade": "P", "src": ["S2", "S39"], "as_of": "2026-11-11", "ttl": "V2", "area": "profile", "tactic": "Headline with one standard target title plus 2-4 evidenced stack or problem terms", "claim": "Improves title and keyword matching", "evidence": "Mechanism documented (keyword anywhere, standardised titles, ATS title similarity); formats untested", "verdict": "use-with-care", "risk": "Title mismatch with real title; unevidenced terms"}
{"type": "practice", "grade": "D", "src": ["S38", "S32"], "as_of": "2026-11-11", "ttl": "V2", "area": "profile", "tactic": "Keep name, titles, employers and dates identical across CV, LinkedIn and GitHub", "claim": "Lowers false fraud flags", "evidence": "No source on false-flag rates; fraud forecast and verification push noted", "verdict": "use", "risk": "None beyond effort"}
{"type": "practice", "grade": "B", "src": ["S2", "S5"], "as_of": "2026-11-11", "ttl": "V2", "area": "open-to-work", "tactic": "Open to Work recruiters-only with 2-5 target titles", "claim": "Appears in recruiter Open to Work filter", "evidence": "Mechanics documented; LinkedIn effect claims are 2020 and unmethodical", "verdict": "use", "risk": "Employer visibility may not stay hidden"}
{"type": "practice", "grade": "C", "src": ["S6", "S7"], "as_of": "2026-11-11", "ttl": "V2", "area": "open-to-work", "tactic": "Public Open to Work frame", "claim": "More InMails against possible stigma", "evidence": "LinkedIn 40% claim; recruiters split; unmeasured", "verdict": "use-with-care", "risk": "Stigma; employer visibility"}
{"type": "practice", "grade": "B", "src": ["S5", "S18", "S19"], "as_of": "2025-10-09", "ttl": "V2", "area": "india", "tactic": "Add notice period and expected salary range in Open to Work (recruiter-only)", "claim": "Recruiters can filter on them", "evidence": "LinkedIn Help and India release; Recruiter filters listed", "verdict": "use-with-care", "risk": "Anchoring; leakage"}
{"type": "practice", "grade": "B", "src": ["S34", "S2"], "as_of": "2026-11-11", "ttl": "V2", "area": "skills", "tactic": "List evidenced skills tagged to roles or projects; do not pad", "claim": "Matches skills filter without mismatch", "evidence": "Skills filter exists; assessments retired; hirers want applied examples", "verdict": "use", "risk": "Under-listing misses searches"}
{"type": "practice", "grade": "B", "src": ["S34"], "as_of": "2026-11-11", "ttl": "V2", "area": "skills", "tactic": "Take LinkedIn skill assessments", "claim": "Badge raises rank", "evidence": "Feature discontinued; badges removed 2024", "verdict": "avoid", "risk": "Wasted effort"}
{"type": "practice", "grade": "D", "src": ["S2", "S3"], "as_of": "2026-11-11", "ttl": "V2", "area": "skills", "tactic": "Fill all 50 skills including unevidenced ones", "claim": "More search hits", "evidence": "Practitioner advice only; tools display qualifications found and missed", "verdict": "avoid", "risk": "Mismatch exposed by AI reading and verification"}
{"type": "practice", "grade": "B", "src": ["S9", "S10", "S40"], "as_of": "2026-11-11", "ttl": "V3", "area": "certifications", "tactic": "List certifications mainly when other signals are thin", "claim": "Raises employment for weak-signal profiles", "evidence": "Randomised experiment (+1.0 pp) against negative association among engineers; absent from AI/ML strings", "verdict": "use-with-care", "risk": "Negative association for strong engineer profiles"}
{"type": "practice", "grade": "P", "src": ["S34"], "as_of": "2026-11-11", "ttl": "V2", "area": "featured", "tactic": "Feature 2-3 proof artefacts with a line of context", "claim": "Shows applied skill", "evidence": "LinkedIn says hirers value applied examples; no measured effect", "verdict": "use", "risk": "Dead or private links"}
{"type": "practice", "grade": "B", "src": ["S4", "S3"], "as_of": "2026-06-17", "ttl": "V2", "area": "connected-apps", "tactic": "Connect partner apps that verify tool usage", "claim": "Recruiters see verified activity", "evidence": "Announced 2026-06-17; Hiring Assistant 2 surfaces it", "verdict": "untested", "risk": "Data sharing"}
{"type": "practice", "grade": "C", "src": ["S32", "S34"], "as_of": "2026-09-23", "ttl": "V2", "area": "verification", "tactic": "Complete workplace or ID verification", "claim": "More views and recruiter responses", "evidence": "LinkedIn uplift claims without method", "verdict": "use", "risk": "Personal data; selection"}
{"type": "practice", "grade": "B", "src": ["S32"], "as_of": "2026-09-23", "ttl": "V2", "area": "verification", "tactic": "Ask colleagues to vouch for experience", "claim": "Verifies work history claims", "evidence": "Feature launched 2026-09-23", "verdict": "untested", "risk": "Voucher must be verified and connected for a year"}
{"type": "practice", "grade": "B", "src": ["S29"], "as_of": "2026-09-30", "ttl": "V3", "area": "applying", "tactic": "Apply on employer career page or ATS instead of Easy Apply", "claim": "Higher interview rate", "evidence": "Huntr: 6.6-9.9% against 2.9-3.6%; employer sites 1.7x boards", "verdict": "use", "risk": "Selection bias; some roles Easy Apply only"}
{"type": "practice", "grade": "C", "src": ["S14", "S31"], "as_of": "2026-11-11", "ttl": "V0", "area": "ghost-jobs", "tactic": "Check posting age, reviewing indicator and verified badge before applying", "claim": "Avoids stale or inactive postings", "evidence": "LinkedIn says it displays response time and review status; staleness data", "verdict": "use", "risk": "Age is not proof"}
{"type": "practice", "grade": "A", "src": ["S11"], "as_of": "2022-09-16", "ttl": "V5", "area": "networking", "tactic": "Build moderately weak ties at target employers", "claim": "More job mobility, strongest in digital industries", "evidence": "Randomised experiments on over 20M members", "verdict": "use", "risk": "2015-2019 connection-suggestion setting"}
{"type": "practice", "grade": "D", "src": ["S46"], "as_of": "2026-11-11", "ttl": "V2", "area": "outreach", "tactic": "Short personalised note with connection request", "claim": "Higher acceptance", "evidence": "Vendor claims without method; free notes limited", "verdict": "use-with-care", "risk": "Note allowance; low replies"}
{"type": "practice", "grade": "D", "src": ["S37"], "as_of": "2026-05-31", "ttl": "V3", "area": "outreach", "tactic": "Cold message to recruiter or hiring manager", "claim": "17% replies", "evidence": "Pin figure is for recruiter-sent messages; not transferable", "verdict": "use-with-care", "risk": "Spam perception"}
{"type": "practice", "grade": "B", "src": ["S23", "S22"], "as_of": "2026-11-11", "ttl": "V2", "area": "automation", "tactic": "Third-party automation or extensions for invitations, messages, comments", "claim": "More volume", "evidence": "Prohibited; account restriction; comment visibility limits", "verdict": "avoid", "risk": "Account restriction"}
{"type": "practice", "grade": "B", "src": ["S22", "S23"], "as_of": "2025-08-20", "ttl": "V2", "area": "engagement-pods", "tactic": "Join engagement pods", "claim": "More reach", "evidence": "Against policy; LinkedIn reduces reach when detected", "verdict": "avoid", "risk": "Reach loss; restriction"}
{"type": "practice", "grade": "C", "src": ["S28"], "as_of": null, "ttl": "V3", "area": "content", "tactic": "Post twice a week for profile views", "claim": "Up to 5x profile views", "evidence": "LinkedIn claim, no method; profile views are not recruiter views", "verdict": "untested", "risk": "Time"}
{"type": "practice", "grade": "D", "src": ["S28"], "as_of": "2026-11-11", "ttl": "V3", "area": "content", "tactic": "Post daily to triple recruiter views", "claim": "Triple recruiter views", "evidence": "Origin untraced; trail ended at unsourced blogs; LinkedIn's own claim is twice a week for up to 5x profile views", "verdict": "untested", "risk": "Time; low-quality posts"}
{"type": "practice", "grade": "C", "src": ["S25", "S26", "S27"], "as_of": "2026-11-11", "ttl": "V3", "area": "content", "tactic": "Prefer carousel or PDF posts", "claim": "Higher engagement", "evidence": "Buffer and Metricool support; Ordinal and Shield Index conflict; engagement not hiring", "verdict": "untested", "risk": "Format drift after the 2026-03 rebuild"}
{"type": "practice", "grade": "P", "src": ["S50", "S22"], "as_of": "2026-11-11", "ttl": "V3", "area": "content", "tactic": "2-3 substantive comments a week on practitioners' posts", "claim": "Visibility to relevant audiences", "evidence": "Comments ranked by relevance (secondary); automated comments limited; no hiring outcome data", "verdict": "use", "risk": "Performative comments"}
{"type": "practice", "grade": "C", "src": ["S36", "S47"], "as_of": "2026-07-14", "ttl": "V2", "area": "premium", "tactic": "One month of Premium Career in an intensive search", "claim": "Hired faster", "evidence": "LinkedIn claims only; no independent evidence", "verdict": "use-with-care", "risk": "Top applicant is a weak signal; Texas allegations"}
{"type": "practice", "grade": "C", "src": ["S45", "S19"], "as_of": "2026-11-11", "ttl": "V3", "area": "india", "tactic": "Run LinkedIn with Naukri and one tech board in parallel", "claim": "Wider reach", "evidence": "Employer-side guides; no independent comparison", "verdict": "use", "risk": "Duplicate effort; scam risk"}
{"type": "practice", "grade": "B", "src": ["S12"], "as_of": "2021-02-21", "ttl": "V5", "area": "networking", "tactic": "Learn to use LinkedIn (profile, connections, job search) if you are a low-resource job seeker", "claim": "Raises employment", "evidence": "Randomised trial, South Africa: four hours of training raised end-of-programme employment by 7 pp from 70%; effect worked through information gathering", "verdict": "use", "risk": "Single country and population; pre-window"}
{"type": "practice", "grade": "D", "src": ["S20", "S57"], "as_of": "2026-11-11", "ttl": "V3", "area": "content", "tactic": "Put external links in the first comment instead of the post body", "claim": "Avoids a reach penalty", "evidence": "No LinkedIn documentation found; a practitioner inventory finds no published weighting between feed signals", "verdict": "untested", "risk": "Awkward reading flow"}
{"type": "practice", "grade": "D", "src": ["S60"], "as_of": "2026-11-11", "ttl": "V3", "area": "skills", "tactic": "Add at least five skills for large gains in views and messages", "claim": "17x views and 33x messages in older guides; 31x more often found in one 2026 guide", "evidence": "Multipliers differ between guides; no method or LinkedIn source was traced", "verdict": "untested", "risk": "Padding the skills list"}
{"type": "practice", "grade": "C", "src": ["S56"], "as_of": "2026-10-28", "ttl": "V2", "area": "outreach", "tactic": "Keep invitations near 100 a week and ration free personalised notes", "claim": "Safe volumes", "evidence": "Vendor readings of LinkedIn Help: no weekly number published; free allowance stated as 3 a month on one page and 5 on others; Premium unlimited", "verdict": "use-with-care", "risk": "Restriction typically lasting about a week; limits can change without notice"}
{"type": "practice", "grade": "P", "src": ["S9", "S10"], "as_of": "2026-11-11", "ttl": "V2", "area": "certifications", "tactic": "List LinkedIn Learning certificates", "claim": "Credibility", "evidence": "No evidence on LinkedIn Learning itself; related certification evidence is mixed", "verdict": "untested", "risk": "Clutter"}
{"type": "practice", "grade": "C", "src": ["S6"], "as_of": "2020-10-29", "ttl": "V2", "area": "open-to-work", "tactic": "Accept or decline recruiter messages instead of leaving them unread", "claim": "Signals an engaged seeker and helps rank higher in recruiter search", "evidence": "LinkedIn blog 2020-10-29; pre-window; no method", "verdict": "use", "risk": "Replying to scam messages; check the sender's profile and verification first"}
{"type": "practice", "grade": "C", "src": ["S6", "S7", "S52"], "as_of": "2026-11-11", "ttl": "V3", "area": "open-to-work", "tactic": "Avoid the public Open to Work frame to escape stigma", "claim": "The frame signals desperation", "evidence": "Recruiters split (Fortune 2024); interviewing.io authors advised against it in 2023 citing residual bias; LinkedIn claims +40% InMails; nobody measured recruiter response", "verdict": "untested", "risk": "Forgoing the community-message effect LinkedIn claims"}
{"type": "practice", "grade": "C", "src": ["S58"], "as_of": "2026-11-11", "ttl": "V3", "area": "skills", "tactic": "Collect endorsements to build trust", "claim": "Higher response from reviewers", "evidence": "One pre-window interviewing.io analysis found little correspondence between endorsements and interview performance; extract only", "verdict": "untested", "risk": "Time spent on a weak signal"}
{"type": "tool", "grade": "C", "src": ["S13", "S36", "S47"], "as_of": "2026-07-14", "ttl": "V0", "id": "linkedin-premium-career", "name": "LinkedIn Premium Career", "stage": 7, "category": "LinkedIn add-on", "what": "5 InMails a month, applicant insights, Top applicant and Top choice, AI job tools, Learning", "verdict": "use-with-care", "why": "Only LinkedIn claims; no independent benefit evidence; Texas allegations", "url": "https://premium.linkedin.com/careers/get-hired-faster", "status": "Texas CID issued 2026-07-14; allegations; no lawsuit found in coverage through 2026-09", "risk": "Vanity metrics", "price": "about 39.99 USD a month per the Texas Attorney General; aggregators list 29.99"}
{"type": "tool", "grade": "C", "src": ["S47"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-sales-navigator-core", "name": "LinkedIn Sales Navigator Core", "stage": 7, "category": "LinkedIn add-on", "what": "Sales prospecting search with 50 InMails a month", "verdict": "use-with-care", "why": "Built for sales; no job-seeker evidence", "url": null, "price": "99.99 to 119.99 USD a month (aggregators)", "note": "No LinkedIn page was opened for this tool."}
{"type": "tool", "grade": "B", "src": ["S1", "S2"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-recruiter", "name": "LinkedIn Recruiter with AI-Assisted Search", "stage": 7, "category": "LinkedIn add-on", "what": "Employer-side search with filters, semantic search and AI messages", "verdict": "watch", "why": "Defines how profiles are filtered and read; not bought by job seekers", "url": "https://business.linkedin.com/hire/ai-assisted-search-and-projects"}
{"type": "tool", "grade": "B", "src": ["S3", "S44"], "as_of": "2026-09-30", "ttl": "V2", "id": "linkedin-hiring-assistant", "name": "LinkedIn Hiring Assistant and Hiring Assistant 2", "stage": 7, "category": "LinkedIn add-on", "what": "Recruiter AI agent with fit signals, verification and connected-app signals", "verdict": "watch", "why": "Announced 2026-09-30, rollout 2026-11; candidate-view contents not documented in detail", "url": "https://business.linkedin.com/talent-solutions/hiring-assistant"}
{"type": "tool", "grade": "B", "src": ["S5", "S18"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-open-to-work", "name": "LinkedIn Open to Work", "stage": 7, "category": "LinkedIn add-on", "what": "Recruiters-only or public status with preferences; India notice period and salary", "verdict": "use-with-care", "why": "Mechanics documented; effect claims unmethodical", "url": "https://www.linkedin.com/help/linkedin/answer/67405", "risk": "Employer visibility may not stay hidden"}
{"type": "tool", "grade": "B", "src": ["S29"], "as_of": "2026-09-30", "ttl": "V3", "id": "linkedin-easy-apply", "name": "LinkedIn Easy Apply", "stage": 7, "category": "LinkedIn add-on", "what": "One-click application inside LinkedIn", "verdict": "use-with-care", "why": "Lower tracker interview rates than employer-site routes; selection bias", "url": null, "note": "No LinkedIn page opened."}
{"type": "tool", "grade": "D", "src": ["S29"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-job-alerts", "name": "LinkedIn job alerts", "stage": 7, "category": "LinkedIn add-on", "what": "Saved searches that notify on new postings", "verdict": "use", "why": "Free; supports early, targeted applications; no source documents alerts directly", "url": null, "note": "No LinkedIn page opened; Huntr covers source rates only."}
{"type": "tool", "grade": "B", "src": ["S32", "S34", "S34"], "as_of": "2026-09-23", "ttl": "V2", "id": "linkedin-verification", "name": "LinkedIn verification and vouching", "stage": 7, "category": "LinkedIn add-on", "what": "Workplace, identity and colleague-vouch signals", "verdict": "use", "why": "Low cost; recruiters and Hiring Assistant 2 can see it; uplift claims are LinkedIn's", "url": "https://techcrunch.com/2026/09/23/linkedin-adds-new-tools-to-fight-fake-profiles-and-bogus-work-histories/", "risk": "Personal-data sharing"}
{"type": "tool", "grade": "B", "src": ["S4", "S3"], "as_of": "2026-06-17", "ttl": "V2", "id": "linkedin-connected-apps", "name": "LinkedIn connected apps", "stage": 7, "category": "LinkedIn add-on", "what": "Partner-verified activity shown on profiles", "verdict": "watch", "why": "Announced 2026-06-17; no outcome evidence", "url": "https://news.linkedin.com/2026/visibility-builds-credibility---the-tools-you-use-every-day--now"}
{"type": "tool", "grade": "D", "src": ["S9", "S10"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-learning-certificates", "name": "LinkedIn Learning certificates", "stage": 7, "category": "LinkedIn add-on", "what": "Course completion credentials shown on profile", "verdict": "use-with-care", "why": "No evidence on LinkedIn Learning specifically; related certification evidence mixed", "url": null, "note": "Evidence is from Coursera credentials and interviewing.io, not LinkedIn Learning."}
{"type": "tool", "grade": "D", "src": ["S1", "S2"], "as_of": "2026-11-11", "ttl": "V2", "id": "third-party-profile-optimisers", "name": "Third-party profile optimisers and AI profile rewriting", "stage": 7, "category": "profile optimiser", "what": "Keyword suggestions and rewritten headline or About text", "verdict": "use-with-care", "why": "No outcome evidence; AI search shows qualifications found and missed", "url": null, "note": "Products not individually assessed."}
{"type": "tool", "grade": "B", "src": ["S23", "S22"], "as_of": "2026-11-11", "ttl": "V2", "id": "linkedin-outreach-automation", "name": "Outreach automation tools and activity-driving extensions", "stage": 7, "category": "automation", "what": "Auto-invite, auto-message, auto-comment through extensions or cloud tools", "verdict": "avoid", "why": "Prohibited by LinkedIn; account restriction; comment visibility limits", "url": "https://www.linkedin.com/help/linkedin/answer/a1341387", "risk": "Account restriction"}
{"type": "tool", "grade": "B", "src": ["S22", "S23"], "as_of": "2026-11-11", "ttl": "V2", "id": "engagement-pod-services", "name": "Engagement pod services", "stage": 7, "category": "automation", "what": "Reciprocal or automated likes and comments", "verdict": "avoid", "why": "Against policy; LinkedIn says it reduces reach when detected", "url": "https://www.linkedin.com/help/linkedin/answer/a1341387"}
{"type": "tool", "grade": "D", "src": ["S23"], "as_of": "2026-11-11", "ttl": "V2", "id": "post-schedulers-and-analytics-extensions", "name": "Post schedulers and analytics extensions", "stage": 7, "category": "automation", "what": "Post planning and analytics", "verdict": "use-with-care", "why": "Allowed only if they neither automate activity nor alter pages; not verified per product", "url": "https://www.linkedin.com/help/linkedin/answer/a1341387"}
{"type": "repo_delta", "grade": "B", "src": ["S15", "S16", "S17", "S51"], "as_of": "2026-11-11", "k": "K1", "verdict": "updated", "finding": "Volume figure reported 2025 not late 2024; profiles are both searched and checked; India 74% confirmed (reported 2026-02-03) from a LinkedIn survey fielded 2025-11 (6,554 global HR professionals; India sub-sample not stated)", "suggested": "Date the figure; cite the survey base; drop the found-versus-checked dichotomy"}
{"type": "repo_delta", "grade": "D", "src": ["S20"], "as_of": "2026-11-11", "k": "K2", "verdict": "unverifiable", "finding": "No outcome study of content strategy", "suggested": "Keep as practice, label P"}
{"type": "repo_delta", "grade": "C", "src": ["S40"], "as_of": "2026-11-11", "k": "K3", "verdict": "confirmed", "finding": "AI/ML strings in 2026 guides contain no certification acronyms", "suggested": "Keep C"}
{"type": "repo_delta", "grade": "B", "src": ["S39"], "as_of": "2026-11-11", "k": "K4", "verdict": "confirmed", "finding": "Vendor documentation matches; Phenom page dated 2022-06-23", "suggested": "Flag possibly stale"}
{"type": "repo_delta", "grade": "D", "src": ["S38"], "as_of": "2026-11-11", "k": "K5", "verdict": "unverifiable", "finding": "No source on false-flag rates", "suggested": "Keep low confidence"}
{"type": "repo_delta", "grade": "C", "src": ["S43", "S22"], "as_of": "2026-11-11", "k": "K6", "verdict": "updated", "finding": "Stated-behaviour surveys exist; no behavioural measure or format test", "suggested": "Reword to behavioural measurement"}
{"type": "repo_delta", "grade": "A", "src": ["S11"], "as_of": "2022-09-16", "k": "K7", "verdict": "confirmed", "finding": "Abstract opened; nuance on two tie-strength measures", "suggested": "Add that the weakest ties by interaction intensity also did well"}
{"type": "repo_delta", "grade": "B", "src": ["S23", "S22"], "as_of": "2026-11-11", "k": "K8", "verdict": "confirmed", "finding": "Help text and Section 8.2 quoted; comment-visibility line 2025-08-20", "suggested": "Add visibility-limit line"}
{"type": "repo_delta", "grade": "B", "src": ["S37", "S55"], "as_of": "2026-11-11", "k": "K9", "verdict": "confirmed", "finding": "The LinkedIn subset is about 276,000 to 294,000 messages inside a 4M+ set; the same-candidate comparison is 16.6% on LinkedIn against 4.4% on email", "suggested": "State the subset size range; keep the transfer caveat"}
{"type": "repo_delta", "grade": "B", "src": ["S13", "S14", "S47"], "as_of": "2026-07-14", "k": "K10", "verdict": "confirmed", "finding": "39.99 from the Texas Attorney General; CID 2026-07-14; no lawsuit found in coverage through 2026-09", "suggested": "Re-check within 14 days"}
```
