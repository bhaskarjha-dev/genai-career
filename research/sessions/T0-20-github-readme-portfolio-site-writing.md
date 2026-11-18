---
id: "T0-20"
title: "GitHub Profiles, Project READMEs, Portfolio Websites and Technical Writing"
date: "2026-11-13"
status: complete-with-gaps
topic: "github-readme-portfolio-site-writing"
tags: ["github-profile", "readme", "portfolio", "technical-writing", "hugging-face", "kaggle", "hiring-signals", "authorship"]
informs_decisions: ["D-011"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai chat with web search and fetch. Anthropic develops this model, so rows citing Anthropic pages (S21, S23, S25, S34, S45, S53) are marked COI."
evidence_window: "2013-02 to 2026-11-02"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 22
---

# T0-20: GitHub Profiles, Project READMEs, Portfolio Websites and Technical Writing

Sources are cited as [S#] and listed in the Sources & Evidence Ledger. Grades follow EGP-1.0. A means a primary page opened in full. B means an established source, or a primary page seen only as a search extract. C means a practitioner, vendor or self-selected survey. D means recall or a single anecdote. M means my own count from a postings sample. P means practice-curated and unmeasured. Retrieval was on 2026-11-13; the brief's temporal anchor is 2026-11-11, and nothing dated after 2026-11-11 was relied on. Only three pages were opened in full (S1, S11, S34); everything else is a search extract and is capped at B. Platform features older than 2025-07-01 are flagged "stale-risk". Anthropic pages are COI because Anthropic develops the model that wrote this report.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | At AI employers, recruiters and hiring managers usually open candidate GitHub links during screening. | 0.55 | D |
| P2 | A personal website adds little beyond GitHub and LinkedIn for most engineering roles. | 0.70 | D |
| P3 | Stars, followers and the contribution graph are weak, gameable signals. | 0.85 | D |
| P4 | Hugging Face Spaces offers free Gradio demos to individuals. | 0.65 | D |
| P5 | Kaggle rank is a mainstream hiring signal for GenAI engineers. | 0.35 | D |
| P6 | Peer-reviewed measurements of what recruiters infer from GitHub profiles exist for 2023-2026. | 0.40 | D |

## Research Question

**Decision (D-011, two-way door):** what should a GenAI job seeker publish on GitHub, a personal site and a technical blog so a reviewer can verify skills quickly, and what evidence shows these surfaces change hiring outcomes?

**Reading chosen.** "Reviewers" means recruiters, hiring managers and engineers who screen. "Public proof" means GitHub, Hugging Face, Kaggle, a personal site and writing or talks. The K-claims were treated as hypotheses.

**Sub-questions:** the 11 coverage items in the brief.

**Method.**
- About 48 web searches and 3 full page reads (a CSCW paper, the Hugging Face Spaces docs, an Anthropic posting).
- Postings sample: 71 postings at 40 employers or posters across 12 role families. Postings came from role- and employer-targeted searches. The Hugging Face and Sarvam queries contained GitHub or open-source terms, so positives there are over-represented. Every posting was seen as an extract except Anthropic's Forward Deployed Engineer posting, which was read in full. "Not seen" therefore means not seen in the extract; positives are verified, negatives are weaker.
- Falsification searches:
  - evidence that portfolios do not matter (S6, S7);
  - postings in roles unlikely to ask for public work (AI governance, S36; human-data contracts, S55; product, S54; India IT services, S66; Anthropic FDE, S34);
  - blog-to-offer datasets (none found);
  - evidence that fake stars or AI-generated pull requests are not a problem (found the opposite, S3, S28-S30).
- Constraint: only URLs surfaced by searches could be fetched, so JavaScript-rendered applicant-tracking pages were mostly unreadable.
- Survivorship: exemplars and first-person accounts come from people who were hired or became known. Statements from reviewers and employers were preferred.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | Whether reviewers look at public work depends on employer type and role family. In 71 sampled postings (40 employers or posters), 37 name public work: Hugging Face 3/3, Sarvam 9/9, Inferact 4/4, NVIDIA 3/3, embodied-AI employers 6/6, Anthropic research postings 3/6, Leadership 4/9, AI product 2/5, a fractional Head of AI 1/1, India enterprise and IT services 2/11. Not seen: Anthropic's FDE posting (read in full), AI governance 0/6, human-data and evaluation contracts 0/6. Selection-biased; not a rate. | [S31]-[S36] [S53]-[S58] [S65] [S66] | M |
| KF2 | No study measures how often, at which stage or for how long reviewers open GitHub, sites or blogs. Peer-reviewed interviews with employers date from 2013 (n=13). Surveys are self-selected (60+ hiring managers, 2021) or untraceable. | [S1] [S2] [S6] [S7] | A (S1); C |
| KF3 | Cheap-to-fake signals are discounted and costly, verifiable ones favoured. In 2013 employers distrusted watcher and fork counts and weighted accepted contributions and sustained work. A 2024 preprint reports about 4.5 million suspected fake stars. GitHub's policy bans automated starring and following. The contribution graph counts light actions. | [S1] [S3] [S4] [S5] | A/B |
| KF4 | A personal site is a supplement, not a gate. 93% of 60+ hiring managers would probably look (65% definitely), but 51% said having none would not lower chances (2021, frontend-weighted). Gun.io reports 95% look and 15% say it carries weight. A 2025 developer survey (n=4,040) found developers rate GitHub above sites for showing skill (37% versus 17%). | [S6] [S7] [S9] | C |
| KF5 | Authorship verification is moving to process. Anthropic asks for no AI in take-homes and live interviews unless allowed. It redesigned its performance take-home as Claude beat it, then opened the original to the public. 49% of 1,500 US hiring managers flag heavily AI-generated application materials. | [S23] [S24] [S37] [S38] [S45] | B/C, COI |
| KF6 | Evaluation guidance: 20-50 tasks from real failures and code graders first (Anthropic) holds. A practitioner FAQ modified 2026-09-01 asks for 100 traces, at least 30 annotated by you, and 100-200 labelled examples per judge failure mode, superseding 50 pass plus 50 fail. One 2026 analysis of 390 AI-engineer postings found 56% mention evaluation. | [S25] [S26] [S27] [S60] | B/C |
| KF7 | Limitations and evaluation are the least-filled sections across 32,111 Hugging Face model cards. Adding detailed cards to 42 models correlated moderately with downloads. karpathy/nanochat shows cost, reproduction script, report card, limits and a leaderboard in one README; rasbt/LLMs-from-scratch shows multi-platform CI badges on a teaching repository. | [S40] [S41] [S52] | B |
| KF8 | Demo hosting rules changed after many tutorials were written. Hugging Face Gradio and Docker Spaces on compute need PRO ($9/month on HF's pages); static Spaces are free; free hardware sleeps. Railway Free is a $1/month credit. Replicate is part of Cloudflare (2025-12-01). Read.cv closed in 2025. OpenAI hard limits return 429 but are not instantaneous; Claude Console cannot cap its Default Workspace. | [S11]-[S13] [S16]-[S18] [S20] [S21] | A/B |
| KF9 | Drive-by pull requests cost maintainers more. curl ended its bug bounty (Jan 2026), tldraw began closing external PRs, GitHub added settings to disable or restrict PRs (reported 2026-02-13) and Ladybird closed public PRs (2026-06-05). Employers such as Hugging Face ask for a reviewable OSS record. | [S28]-[S31] | B/C |
| KF10 | Writing is named as a plus by some infrastructure and OSS employers (four Inferact postings; Hugging Face invites posts and talks). First-person accounts exist (Willison, Thomas, Yan) but come from survivors; one author reports 4-5 data-science offers and about two dozen technical-writing offers over 2.5 years. A secondary report says Cursor's CEO scanned X and GitHub profiles. No blog-to-interview dataset exists. | [S8] [S10] [S31] [S33] [S48]-[S51] | B/C |
| KF11 | Kaggle rank is role-specific. NVIDIA's KGMON posting asks for a Grandmaster-level competition record; another NVIDIA team treats it as a plus. | [S35] | B |
| KF12 | Public proof is not universal. None of six AI-governance postings, six human-data contract postings or Anthropic's FDE posting asks for GitHub, blogs or portfolios; they screen on years, degrees, certifications and exercises. Two of five AI-product postings mention a portfolio or OSS; two of eleven India enterprise and IT-services postings mention OSS or publications; four of nine Leadership postings ask for publications, OSS or speaking. | [S34] [S36] [S54] [S55] [S58] [S65] [S66] | M |
| KF13 | Research and embodied-AI roles ask for publications or OSS: all six embodied-AI postings do; three of six Anthropic research postings name research, OSS frameworks or papers; Apollo Research's extract does not. | [S53] [S56] | M |
| KF14 | India: Sarvam (Bengaluru, a startup) routinely lists a GitHub portfolio or OSS record in engineering postings. In eleven India enterprise and IT-services postings (Walmart Global Tech, HCLTech, Cognizant, Infosys, GlobalLogic and one unnamed), two list OSS or publications: a Walmart Staff posting (preferred) and an HCLTech architect posting (optional). GCC and IT-services behaviour beyond that is unmeasured. | [S32] [S44] [S58] [S66] | M/C |
| KF15 | RAG appears in 26-40% of AI-engineer postings across four analyses (samples of 390 to 4,155 postings; 15.4% in ML-engineer postings), and evaluation in 56% of one 390-posting analysis. Practitioner and hiring-manager accounts describe portfolios built only from Titanic, Iris or MNIST as tutorial-grade. | [S59]-[S62] | C |

## Recommendation

Decision rules, each with its failure mode.

1. **Resume first, evidence second.** Keep the keywords on the resume and add two or three links to evidence. *Failure mode:* links go unopened, and 58% of hiring managers in one vendor survey use AI to screen [S37].
2. **Curate GitHub.** Pin at most six items [S5], and aim for three deep repositories. Archive unmodified tutorial forks and single-commit repositories. Do not spend effort on stars, followers or the graph [S1, S3, S4, S5]. *Failure mode:* a polished pin set built from AI output that you cannot defend in a walkthrough (rule 7).
3. **Give every pinned system an evidence README** (skeleton in Detailed Findings section 4). *Failure mode:* numbers that cannot be regenerated, which are self-asserted at best.
4. **Demos: replay-first.** Use a static Space, Cloudflare or GitHub Pages replay, or a recorded walkthrough. If live, set a hard spend limit. *Failure mode:* the cap is hit (429) while a reviewer is trying it, a free tier changes [S11, S12], or free hardware sleeps. Keep a dated video as fallback.
5. **Upstream work: pre-discussed and small.** Prefer a merged fix after an issue discussion, or publish an evaluation through an official registry such as Inspect Evals [S43]. Avoid drive-by pull requests [S28-S30]. *Failure mode:* maintainers close external PRs, so keep the issue and review trail as evidence.
6. **Writing: two to four deep write-ups.** Choose postmortems, evaluation write-ups or reproductions with committed code, on a static site you control, cross-posted. *Failure mode:* no measured payoff, survivor-biased advice [S48-S50], and generic AI-sounding prose.
7. **Authorship: keep it checkable.** Keep incremental commit history, a decision log and an AI-use note, and be ready for a 10-minute live walkthrough [S23, S37, S38]. *Failure mode:* squashed or bulk-generated history reads as fabricated.
8. **Allocate by role family** (profile skeletons below).
   - Infrastructure: merged upstream pull requests, kernels or benchmarks, and blogs.
   - Evaluation: a registered evaluation plus error analysis.
   - Research and embodied: papers, open-source releases, reproductions and demo video [S53, S56].
   - Product: one shipped prototype and a decision memo [S54].
   - Governance and human-data: sanitised artefacts, credentials and exercises, with minimal GitHub [S36, S55].
   - Leadership and fractional: talks, publications or OSS leadership where the posting asks (four of nine Leadership postings) [S57, S65].
   - Kaggle: only for competition-oriented teams.
   *Failure mode:* misreading the employer. Read the posting's own words first.
9. **India.** At startups that ask (Sarvam-type), a GitHub portfolio is in scope. For GCC and services roles, stay resume-first [S58, S66]. *Failure mode:* eleven postings are not a market; GCC behaviour is unmeasured.

**What would change these rules:**
- a measured link-open rate (candidate-side tracked links or applicant-tracking analytics);
- a peer-reviewed field experiment on GitHub links and callbacks;
- employer postings adding or dropping public-work lines;
- price or policy changes at Hugging Face, Cloudflare, Railway or GitHub;
- provenance features (verified AI-use disclosure) that reviewers adopt.

## Alternatives Considered

| Option | Verdict | Reason |
|---|---|---|
| Portfolio site first | Rejected | Reviewers say it is optional (51% no cost) [S6, S7]. Build after resume and GitHub. |
| Many small demos | Rejected | Cheap signals are discounted [S1]; hosting is volatile [S11]. Direction supported, number untested. |
| Live demo as the centrepiece | Rejected as default | Weight unmeasured; spend, sleep and policy risks [S11, S20]. Replay-first instead. |
| Medium, Substack or dev.to as the sole home | Rejected | Platform risk: Read.cv closed with a four-month export window [S18]; Hugging Face blog publishing sits in a paid tier [S13]. Use a static site you control and cross-post. |
| Kaggle-first | Rejected as general rule | Role-specific [S35]. |
| Star, follower or graph building | Rejected | Fake-star scale and policy bans [S3, S4]. |
| Drive-by open-source pull requests | Rejected | Maintainers are closing routes [S28-S30]. |
| Resume only, no public proof | Preferred for governance, human-data and most product roles | Postings sampled screen on years, frameworks, degrees and certifications [S36, S54, S55]. |
| AI-generated repository polish | Rejected | Practitioners report walk-through screens; 49% flag AI-written materials [S37, S38]. |

## Detailed Findings

### 1. Do reviewers look? (KF1, KF2, KF4, KF10)

- **Peer-reviewed.** Marlow and Dabbish interviewed 13 people in 2013 (7 employers, 6 job seekers) [S1]. Employers favoured signals they could check quickly and that were costly to fake (accepted contributions, ownership, sustained activity) and treated watcher and fork counts as unreliable. Capiluppi, Serebrenik and Singer (2013) argue that interpreting social-web signals is the hard part and that developers can manipulate them [S2]. Both are stale-risk.
- **Surveys.**
  - Profy.dev, 60+ hiring managers, posted 2021-08: 65% would definitely look at an inexperienced candidate's site and 93% likely. 51% said no site would not lower chances. Self-selected and frontend-weighted [S6].
  - Gun.io: 95% look, 15% say it carries weight, date not stated [S7].
  - daily.dev 2025, n=4,040 developers: 37% say GitHub best shows their skills versus 17% portfolios. This is developers' self-view, not reviewers' behaviour [S9].
- **Employers.** A secondary summary of a Business Insider report says Cursor's CEO personally scanned X and GitHub profiles [S10]. Underdog.io (a recruiting marketplace, COI) advises starting outbound sourcing from GitHub, Hugging Face, blogs and talks [S8].
- **By employer type.** Evidence exists for an OSS-centred employer (Hugging Face), startups (Cursor report, Inferact, Sarvam), robotics startups (S56), a frontier lab (Anthropic: no public-work ask in the FDE posting, three of six research postings name research or OSS, and a public take-home route exists), enterprise GCC and IT-services employers (Walmart Global Tech India, HCLTech and others; mostly silent) and Leadership postings (four of nine ask). Big Tech beyond Anthropic and NVIDIA: none found.
- **Stage and duration.** Not measured. One Dataquest feature attributes to a hiring professional the claim that managers spend 1-2 minutes on a resume and 15+ minutes on a portfolio (single anecdote, D) [S62].

### 2. Studies of GitHub signals (KF3)

| Signal | What reviewers infer | Evidence | Grade |
|---|---|---|---|
| Merged pull requests to well-known projects | Third-party-verified competence | 2013 employers weighted accepted contributions [S1]; Hugging Face asks for merged PRs reviewable on GitHub [S31] | A; B |
| Sustained, substantive activity and ownership | Commitment, ability to ship | [S1] | A |
| Contribution graph | Activity, weakly | Counts default-branch commits, repository creation, issues, discussions and reviews; the GHES 3.12 copy of the docs also lists forking; needs commit-email mapping; stale-risk docs. Post-2013 evaluator inference unmeasured [S5] | B |
| Stars | Popularity, perhaps quality | About 4.5 million suspected fake stars in a preprint (v1) [S3]; automated starring banned [S4] | B |
| Followers | Reputation | Automated following banned [S4]; no inference study found | B |
| Forks and watchers | Little | Negligible effort, discounted in interviews [S1] | A |
| Pinned repositories (max six) | What the candidate considers best | Cap per docs [S5]; reviewer weight unmeasured | B / P |
| Commit history and decision trail | Process, authorship | Walk-through screens reported [S38, S39]; Anthropic verifies by process [S23] | C |
| README with evaluation, cost and limits | Rigour | Limitations and evaluation least-filled in model cards [S40]; nanochat pattern [S41] | B |
| CI badge, Actions | Tests exist and run | Standard hosted runners free on public repositories [S14]; rasbt repository shows multi-OS badges [S52]; reviewer inference unmeasured | B / P |
| Live demo or Space | "It runs" | Compute Spaces need PRO; free hardware sleeps [S11]; weight unmeasured | A / D |
| Model or dataset card | Documentation maturity | 32,111-card analysis; 42-model intervention moderately correlated with downloads [S40] | B |
| Kaggle rank | Competitive-ML skill | Required by NVIDIA KGMON [S35] | B |
| Personal site | Supplement | [S6] [S7] | C |
| Technical blog or postmortem | Depth, communication | Bonus lines in four Inferact postings [S33]; first-person accounts [S48-S50]; effect unmeasured | B / absence |
| Registered public evaluation | Evaluation skill, externally listed | Inspect Evals route and maintenance paper [S43] | B |
| Talks, podcasts | Visibility | Hugging Face covers talk travel [S31]; no data | P |

The 2024 preprint reports that fake-star effects fade quickly (v1 figures; later revisions may differ) [S3]. GitHub's policy also bars using scraped or API data to send unsolicited email or sell personal data to recruiters or job boards [S4].

### 3. The GitHub profile

- **Profile README.** A repository named after your username renders on the profile. Simon Willison's self-updating version pulls releases, blog entries and TILs through Actions [S42]. The technique dates from 2020 (stale-risk).
- **Pins.** Up to six public repositories or gists [S5]. Choose evidence over volume.
- **Private work.** The graph can include anonymised private contributions [S5]. Prefer public, reviewable work.
- **Hide or archive.** Unmodified forks, tutorial notebooks, single-commit repositories [P; only the fork discount has evidence, S1].

**Profile skeleton by role family (practice-curated).** Tags give evidence or [P]. "V" levels are the knowledge base's ladder (V0 self-asserted, V1 reproducible, V2 externally attested, V3 operationally evidenced).

| Role family | First screen | Pinned set | Best proof | Skip |
|---|---|---|---|---|
| Applied AI Engineering | One-line scope; evidence stream of releases and posts [S42] | One agent or RAG system with CI-gated eval [S25, S26]; one reusable library with releases; one write-up | V1; V2 if upstream merged | Tutorial clones [P] |
| ML Engineering and Applied Science | Training or fine-tune results link | Reproducible run with cost, time and report card [S41]; model and dataset cards with limits [S40]; tested teaching repository optional [S52] | V1 | Titanic-type notebooks [P] |
| Forward Deployment and Solutions | Sanitised delivery case studies | MCP servers, agent skills and runbooks with no client data [S34 lists such artefacts]; one end-to-end build; Sarvam's solutions role accepts side projects or OSS [S32] | V1-V3 | Client material [P] |
| AI Infrastructure and Platform | Hardware, benchmark and kernel links | Merged upstream PRs (vLLM, Triton, NCCL and similar) [S32, S33]; reproducible benchmarks; one technical post [S33] | V2 | Unmeasured speed claims [P] |
| Evaluation, Safety and Security | Evaluation list with method links | Registered evaluation and paper [S43]; error-analysis write-up [S26] | V1-V2 | Dangerous payloads; follow disclosure norms [P] |
| Research | Papers, reproductions, Scholar link | Code with configs and seeds; reproduction with deltas; research, OSS frameworks or papers are named in Anthropic research postings [S53]; long-form research notes on a static blog [S63] | V2 (publication) | Unreviewed claims [P] |
| Governance, Risk and Assurance | Skip GitHub; short site or PDF | Sanitised model cards, risk registers, control mappings [S36 names such artefacts]; credentials | V1-V3 | Confidential material [S36, P] |
| Product and Program | Case-study write-ups | One shipped prototype and a decision memo; two of five postings mention a portfolio or OSS [S54] | V1 | Feature lists [P] |
| Human Data and Evaluation Ops | Domain credentials, sanitised guideline sample | Agreement-statistics write-up [P]; postings screen on degrees, years and exercises [S55] | V1 | Client data [P] |
| Embodied and Physical AI | Demo videos | Simulation or ROS repositories with benchmarks; publications or OSS releases [S56] | V1-V2 | Unreproducible demos [P] |
| Leadership and Executive | Talks and operating-model posts | Team outcomes, public talks; four of nine Leadership postings ask for publications, OSS or speaking [S65] | V3 | Code volume [P] |
| Independent and Fractional | Storefront site; links to publications and GitHub where asked [S57] | Client-safe case studies, public tools [P] | V1-V3 | Transactions on GitHub Pages [S15] |

### 4. The project README for an AI system

| Element | What to put | Evidence or tag |
|---|---|---|
| Claim line | One sentence with date and version | [P] |
| Results table | Task count, baseline, system, metric, trials, variance | [S25] [S26] |
| Reproduction | One command regenerates the table from committed data | [S41]; V1 rule [P] |
| Cost and latency | Dollars per run, hardware, wall-clock; cost per task | [S41]; [S25] |
| Evaluation method | Tasks drawn from real failures, graders, trial count, judge calibration | [S25] [S26] |
| Architecture | One diagram, one data-flow paragraph | [P] |
| Limits and failure modes | Known failures, out of scope | [S40] [S41] |
| Decision log | Choices and rejected alternatives | [P] |
| CI | Tests plus a capped smoke evaluation on PRs; scheduled full run; badge from endpoint JSON | [S14] [S19]; [P] |
| Demo | Replay-first, dated "last verified", spend cap if live | [S11] [S20] |
| Cards | Links to model and dataset cards with limitations | [S40] |
| Provenance | AI-use note, intact history | [S23] [S37] |
| Citation and licence | CITATION.cff or cite block | [S41] [S43] [S52] |

Judge validation: the FAQ modified 2026-09-01 asks for 100-200 labelled examples per failure mode, superseding the earlier 50 pass plus 50 fail [S26, S27]. Larger Actions runners are not free for public repositories; GPU CI needs a budget [S14].

### 5. Hugging Face and Kaggle

- **Hugging Face.** Static Spaces are free. Gradio and Docker Spaces on compute need PRO (personal) or Team/Enterprise (organisations). Free accounts can host up to two ZeroGPU Spaces. Free hardware sleeps when unused [S11]. Forum threads from 2026 show confusion and staff confirmation of the restriction [S12]. HF's own pages list PRO at $9/month and include publishing blog articles on an HF profile among its features [S13].
- **When HF beats GitHub.** Model, dataset and Space artefacts matter where the employer's product is the Hub (Hugging Face reviews GitHub records [S31]). Hub-specific reviewer behaviour: absence.
- **Kaggle.** NVIDIA's KGMON posting requires a Grandmaster-level record; a data-curation posting treats it as a plus [S35]. All KGMoN members are competition Grandmasters who also publish code and tutorials [S35]. No evidence beyond competition-oriented teams.

### 6. Portfolio websites

- **Signal beyond GitHub and LinkedIn.** Reviewers look when given a link but rarely treat it as decisive [S6, S7]. A badly built site can hurt, per the Profy write-up [S6].
- **Hosting.** GitHub Pages: sites up to 1 GB, soft 100 GB/month bandwidth, soft 10 builds/hour (not for custom Actions workflows), and no commercial SaaS use [S15]. Avoid proprietary portfolio platforms: Read.cv wound down from 2025-01-17 with export until 2025-05-16 [S18].
- **What goes first.** Resume link, three evidence links, one write-up [P].
- **Site generators.** Not compared; absence.

### 7. Technical writing and talks (KF10)

- **Employer asks.**
  - Four Inferact postings list technical blogs, side projects or a public portfolio of artefacts. The 2026-06-18 date appears on the developer-relations posting at one aggregator [S33].
  - Hugging Face's voice-agent role invites posts, demos and talks and covers travel [S31].
- **Sourcing.** A secondary report says Cursor executives scout X and GitHub [S10].
- **First-person accounts (survivors).**
  - Simon Willison says most of the jobs in his career can be attributed at least partly to his blog [S48].
  - Rachel Thomas (2019) says she knows of people whose blog posts led to job offers [S49].
  - Eugene Yan describes his writing as a "bat signal" and credits it with accelerating his career [S50].
  - One Towards Data Science author reports 4-5 data-science offers and about two dozen technical-writing offers over about 2.5 years; most offers were technical writing, and he advises a year of effort first (single anecdote, D) [S51].
- **Outcome data.** None; blog-to-offer rates remain unmeasured (see Absences).
- **Formats with evidence.** Employer-authored postmortems (S23) and evaluation write-ups (S25, S26) show the pattern. Writing that is itself an artefact with code fits "V1" best [P].

### 8. Authorship and AI-generated work (KF5)

- **Anthropic** asks candidates not to use AI in take-homes or live interviews unless told; its performance take-home explicitly allows AI. About 1,000 candidates completed it over about a year and a half, and it helped hire most of the performance team. Claude models repeatedly beat the earlier versions [S23, S24]. Anthropic then published the original and invited resumes from people who beat Claude's best score [S45].
- **Surveys and practitioners.** 49% of 1,500 US hiring managers (Resume Genius, a resume vendor) treat heavily AI-generated application materials as a red flag, and 58% use AI to screen [S37]. A mentoring marketplace and a developer outlet report walk-through-your-code screens [S38, S39].
- **README and blog reception.** No peer-reviewed or large-sample data (see Absences).
- **Maintainer side.** AI-generated contributions led curl to end its bug bounty, tldraw to close external PRs, GitHub to add disable and restrict settings, and Ladybird to close public PRs [S28-S30].

### 9. Employer postings sample

**Method.** Search-engine retrievals by employer and role family, 2026-11-13. Unit: one posting. Access: Read for Anthropic's FDE posting (row 17); Extract for the rest (employer page or aggregator copy). "Names public work" means GitHub, OSS record, blog, portfolio, publications or competition rank. This is a purposive, clustered, non-random sample (n=71, 40 employers or posters). The Hugging Face and Sarvam queries contained the terms searched for. "Not seen" means not seen in the extract. Wording is paraphrased.

| # | Employer | Role | Family | Public work named? | Words (paraphrased) | Tier | Src |
|---|---|---|---|---|---|---|---|
| 1 | Hugging Face | Open-Source ML Engineer, EMEA | ML Engineering | Yes | Public OSS record (for example merged PRs) reviewable on GitHub | Required | S31 |
| 2 | Hugging Face | Open-Source ML Engineer, US | ML Engineering | Yes | Public OSS track record; prior library contributions a plus | Required | S31 |
| 3 | Hugging Face | Senior ML Engineer, Voice Agents | Applied AI | Yes | Substantial OSS contributions; invites posts and talks | Required | S31 |
| 4 | Sarvam | ML Engineer, Vision | ML Engineering | Yes | OSS contributions or solid GitHub portfolio | Preferred | S32 |
| 5 | Sarvam | Backend Engineer, API Team | Infrastructure | Yes | OSS backend work or GitHub portfolio | Preferred | S32 |
| 6 | Sarvam | Backend AI Engineer, Studio | Applied AI | Yes | OSS contributions or strong GitHub portfolio | Listed | S32 |
| 7 | Sarvam | Backend Engineer, AI and ML | Applied AI | Yes | Strong GitHub portfolio or OSS AI/ML work | Listed | S32 |
| 8 | Sarvam | AI Researcher or Research Engineer, Agents | Research | Yes | OSS participation; send publications or portfolios | Listed | S32 |
| 9 | Sarvam | ML Engineer, CV and VLM | ML Engineering | Yes | Publications; OSS to vision and NLP libraries | Preferred | S32 |
| 10 | Sarvam | Training-infrastructure role (title not captured) | Infrastructure | Yes | Meaningful OSS in Megatron, DeepSpeed, vLLM, Triton, NCCL | Listed | S32 |
| 11 | Sarvam | Solutions or applied role (title not captured) | Forward Deployment | Yes | Side projects, OSS or shipped products | Listed | S32 |
| 12 | Sarvam | ML Engineer, Data | ML Engineering | Yes | Meaningful OSS in data tooling | Listed | S32 |
| 13 | Inferact | MTS, Inference | Infrastructure | Yes | Blogs or side projects on vLLM or inference | Bonus | S33 |
| 14 | Inferact | MTS, Kernel Engineering | Infrastructure | Yes | Deep blogs on GPU optimisation | Bonus | S33 |
| 15 | Inferact | MTS, Exceptional Generalist | Infrastructure | Yes | Shared blogs or impactful side projects | Bonus | S33 |
| 16 | Inferact | MTS, Developer Relations | Applied AI | Yes | Strong public portfolio of technical artefacts | Listed | S33 |
| 17 | Anthropic | Forward Deployed Engineer | Forward Deployment | Not seen (read in full) | None; delivery artefacts are duties | None | S34 |
| 18 | NVIDIA | Senior Applied Agent Research Engineer (KGMON) | ML / Research | Yes | Kaggle Grandmaster-level record | Required | S35 |
| 19 | NVIDIA | Senior Applied Research Scientist, Data Curation | ML / Research | Yes | Kaggle Grandmaster or strong results | Plus | S35 |
| 20 | NVIDIA | Senior LLM Technologist | Applied AI | Yes | Kaggle Grandmaster, NLP or LLM golds | Required | S35 |
| 21 | Teneo | AI Governance Manager | Governance | Not seen | 5-8+ years; certifications | None | S36 |
| 22 | Crowe | AI Governance Consulting Technical Manager | Governance | Not seen | AIGP or equivalent; produce model cards | None | S36 |
| 23 | Qureos poster | AI Governance Lead or Manager | Governance | Not seen | 10+ years; certifications | None | S36 |
| 24 | Unnamed (Tampa) | AI Governance Lead | Governance | Not seen | Frameworks; certifications preferred | None | S36 |
| 25 | Unnamed (South St Paul) | AI Governance Manager | Governance | Not seen | Framework alignment; audit exposure | None | S36 |
| 26 | Barclay Simpson | AI Governance Manager | Governance | Not seen | Governance experience; framework knowledge | None | S36 |
| 27 | Anthropic | RE or RS, RL Frontiers | Research | Yes | Original technical work shown through research, OSS or production impact | Listed | S53 |
| 28 | Anthropic | RE, Pretraining Scaling | Research | Yes | OSS LLM frameworks; published research | Preferred | S53 |
| 29 | Anthropic | RE or RS, Alignment Science | Research (safety) | Yes | Experience authoring research papers | Listed | S53 |
| 30 | Anthropic | RE, Discovery | Research | Not seen | LM training, evaluation and inference familiarity | None | S53 |
| 31 | Anthropic | RE or Scientist, Frontier Red Team (Cyber) | Evaluation, Safety | Not seen | Security expertise; agent research | None | S53 |
| 32 | Anthropic | RE, Search and Knowledge Post-Training | Research | Not seen | Shipped ML research; evaluation building | None | S53 |
| 33 | Apollo Research | Research Scientist or Engineer | Evaluation, Safety | Not seen | Scientific writing; welcomes self-taught | None | S53 |
| 34 | 7AI | AI Product Manager | Product | Yes | Portfolio of AI-native prototypes | Nice to have | S54 |
| 35 | Arcade | AI Product Manager | Product | Yes | Personal projects or OSS count; shipped side projects a bonus | Listed | S54 |
| 36 | Eliza | AI Product Manager | Product | Not seen | Client-delivery experience | None | S54 |
| 37 | Fractal (via aggregator) | GenAI Technical Product Manager | Product | Not seen | RAG and evaluation-framework knowledge | None | S54 |
| 38 | Truelancer poster | Product Manager, AI and Product Evaluation (contract) | Product / Human Data | Not seen | CV and PM summary | None | S54 |
| 39 | Mercor | Training or L&D Evaluator | Human Data | Not seen | 5+ years; Office and Slides; degree preferred | None | S55 |
| 40 | Mercor | Rubrics Evaluator (Professional experience) | Human Data | Not seen | Profile update; short evaluation exercise | None | S55 |
| 41 | Mercor | Software, AI, IT and Data Evaluator | Human Data | Not seen | Master's preferred | None | S55 |
| 42 | Mercor | ML Evaluation Designer | Human Data | Not seen | Technical screen, live code review, domain interview | None | S55 |
| 43 | Turing | LLM Annotator (Master's degree) | Human Data | Not seen | Degree; structured-data familiarity | None | S55 |
| 44 | Surge AI (via DataAnnotation) | Generative AI Generalist | Human Data | Not seen | Domain expertise; degree preferred | None | S55 |
| 45 | Humanoid | Robot Learning Engineer, London | Embodied | Yes | Top-tier publications or equivalent OSS | Listed | S56 |
| 46 | 1X | Research Engineer, Robotics Learning | Embodied | Yes | Large personal projects (for example OSS) | Bonus | S56 |
| 47 | 1X | Embodied AI or AGI Researcher | Embodied | Yes | Influential publications, adopted methods or deployed systems | Required | S56 |
| 48 | General Robotics | Robotics Engineer, Manipulation | Embodied | Yes | First-author publications; OSS releases | Listed | S56 |
| 49 | General Robotics | Robotics Engineer, Humanoids | Embodied | Yes | First-author publications | Required | S56 |
| 50 | Skild AI | Physics Simulation Scientist | Embodied | Yes | Publications, OSS or shipped systems | Strong plus | S56 |
| 51 | Motoniq | Head of AI (VLA), fractional | Independent / Leadership | Yes | Publications or major OSS; send links to publications and GitHub | Required | S57 |
| 52 | Walmart Global Tech India | Staff Software Engineer, Bengaluru | Applied AI | Yes | OSS contributions or publications in GenAI, RAG or agentic frameworks | Preferred | S58 |
| 53 | Walmart Global Tech India | Senior Software or ML Engineer | ML Engineering | Not seen | Years, Python, frameworks | None | S58 |
| 54 | Walmart Global Tech India | Data Scientist III | ML Engineering | Not seen | GenAI fundamentals | None | S58 |
| 55 | Walmart Global Tech India | Senior Data Scientist | ML Engineering | Not seen | Soft line on engaging with research and OSS communities; no evidence requested | None | S58 |
| 56 | Unnamed (Bangalore) | Generative AI Engineer, 8-12 years | Applied AI | Not seen | RAG, vector databases, Azure tooling | None | S58 |
| 57 | Unnamed (via Indeed) | Head of AI (10+ years) | Leadership | Yes | Published research, patents, OSS or recognised technical leadership | Listed | S65 |
| 58 | Unnamed services firm | Head of AI, North America delivery | Leadership | Not seen (duty only) | Speaking and publishing are duties, not required evidence | None | S65 |
| 59 | Janea Systems | Senior AI engineering leadership role (title not captured) | Leadership | Yes | Thought-leadership content or speaking at industry events | Required | S65 |
| 60 | Unnamed (recruiter client) | CTO and Chief AI Officer | Leadership | Yes | Published research, patents or OSS in AI/ML; thought-leader duties | Required | S65 |
| 61 | MakroPro | Head of Retail AI Platform | Leadership | Yes | OSS platform leadership; public speaking or thought leadership | Preferred | S65 |
| 62 | Robert Walters poster | Head of AI, London | Leadership | Not seen | Demonstrated leadership of AI or ML teams | None | S65 |
| 63 | Virtual Vocations poster | Head of AI, remote | Leadership | Not seen | 10+ years with leadership responsibility | None | S65 |
| 64 | Jobgether poster | Head of AI Engineering | Leadership | Not seen | Platform and strategy leadership experience | None | S65 |
| 65 | Venture studio (via mirror) | Chief AI Officer (IC role) | Leadership | Not seen | Hands-on modelling; evaluate open-source models | None | S65 |
| 66 | HCLTech | Senior Technical Architect, Pune | Forward Deployment | Yes | Publications or contributions to the AI/ML community | Optional | S66 |
| 67 | HCLTech | Technical Consultant, Bengaluru | Forward Deployment | Not seen | 2-5 years; LLM exposure | None | S66 |
| 68 | HCLTech | AI Solution Architect I | Forward Deployment | Not seen | Architecture experience; RAG and agent frameworks | None | S66 |
| 69 | Cognizant | Generative AI Architect | Forward Deployment | Not seen (duty only) | Publishing white papers is a duty, not required evidence | None | S66 |
| 70 | Infosys | Gen AI Senior Lead, Bengaluru | Forward Deployment | Not seen | Consulting delivery; GenAI techniques | None | S66 |
| 71 | GlobalLogic | Gen AI Architect, Hyderabad | Forward Deployment | Not seen | 15-18 years IT; LLM experience | None | S66 |

**Counts (M, inputs A/B).** 37 of 71 (52.1%) name public work in the extract. 10 are required or must-have (rows 1, 2, 3, 18, 20, 47, 49, 51, 59, 60); 27 are preferred, bonus, optional or listed. By cluster: Hugging Face 3/3; Sarvam 9/9; Inferact 4/4; NVIDIA 3/3; embodied-AI 6/6; fractional Head of AI 1/1; Anthropic research 3/6 (Apollo 0/1); Leadership 4/9; AI product 2/5; India enterprise and IT services 2/11; Anthropic FDE 0/1; AI governance 0/6; human-data contracts 0/6. Do not extrapolate: the sample is clustered and the first two clusters were retrieved with search terms that favour positives. Sarvam lists 46 open roles as of 2026-11-02 and routes applications through Ashby [S44].

### 10. Role differences

- Public proof is central for OSS-library, infrastructure and competition-team roles [S31, S33, S35].
- It is expected for research and embodied roles, usually as publications or OSS releases [S53, S56].
- It is common but secondary at an Indian startup [S32] and mostly silent at the enterprise and IT-services postings sampled (2 of 11) [S58, S66].
- It is occasional for product roles [S54], absent from governance and human-data postings [S36, S55], and absent from Anthropic's FDE posting [S34].
- Leadership and fractional roles: four of nine Leadership postings ask for publications, OSS or speaking, two of them as requirements [S65]; one fractional posting asks for publications and GitHub links [S57].

### 11. Tools (stage 5; verified as of 2026-11-13)

| Tool | Verdict | Verified facts | Src |
|---|---|---|---|
| GitHub Pages | use-with-care | Public repositories on Free; 1 GB; soft 100 GB/month; soft 10 builds/hour; no commercial or SaaS use | S15 |
| Hugging Face Spaces | use-with-care | Static free; Gradio and Docker on compute need PRO ($9/month on HF pages); two free ZeroGPU Spaces; free hardware sleeps | S11, S13 |
| Railway | use-with-care | Free $1 credit; Hobby $5 including $5 usage; Pro $20 | S16 |
| Replicate | watch | Announced 2025-11-17; part of Cloudflare from 2025-12-01 | S17 |
| Read.cv | avoid | Acquired 2025-01-17; wound down; export to 2025-05-16 | S18 |
| GitHub Actions | use | Free for standard hosted runners on public repositories; larger runners not free; self-hosted fee postponed | S14 |
| Shields.io endpoint badges | use-with-care | schemaVersion 1, label and message required; cache values below 300 seconds ignored | S19 |
| OpenAI project spend limits | use | Enforce a hard limit returns 429; alerts only notify; not instantaneous | S20 |
| Claude Console workspace limits | use | Default Workspace cannot be limited; workspace limit below organisation limit | S21 |
| OSS Insight | use | Docs state 5+ billion rows; free; REST API | S22 |
| git log on a treeless clone | use-with-care | Plain git log needs only commits; git log with a path downloads trees for almost every commit; GitHub advises against daily use and suggests blobless clones | S47 |
| GitHub GraphQL API | use-with-care | 5,000 points/hour per user; 1,000 per hour per repository for GITHUB_TOKEN in Actions; AUP bars recruiter lead lists | S4, S46 |
| Inspect AI | use | Evaluation framework with a community evaluations registry | S43 |

### 12. Exemplars

| Exemplar | URL | Role family | Why it is strong |
|---|---|---|---|
| Simon Willison profile README and blog | https://github.com/simonw/simonw | Applied AI | Self-updating evidence stream via Actions; 2020 technique (stale-risk); survivor caveat [S42, S48] |
| karpathy/nanochat | https://github.com/karpathy/nanochat | ML Eng; Research | Reproduction script, stated cost and time, report-card table, plain limits, dated leaderboard to 2026-03 [S41] |
| rasbt/LLMs-from-scratch | https://github.com/rasbt/LLMs-from-scratch | ML Eng (teaching) | Chapter structure, exercises, CITATION.cff and CI badges for Linux, Windows and macOS; large following, survivor caveat; repository summarised, not opened [S52] |
| mlabonne/llm-course | https://github.com/mlabonne/llm-course | ML Eng (teaching) | Roadmaps plus runnable notebooks; the author is listed as Head of Post-Training at Liquid AI in a third-party summary; causal link to hiring not established [S52] |
| AI Evals FAQ (Husain, Shankar) | https://hamel.dev/blog/posts/evals-faq/ | Evaluation; Applied AI | Maintained (modified 2026-09-01), numbers and stopping rules [S26] |
| Eugene Yan writing FAQ and site | https://eugeneyan.com/writing/writing-faq/ | Applied AI; ML Eng | Long-running site with a stated writing process and audience aims; survivor caveat [S50] |
| Lil'Log (Lilian Weng) | https://lilianweng.github.io/ | Research | Long-form research notes since 2017 on a static GitHub Pages blog; posts dated 2026-06-24 and 2026-07-04; survivor caveat [S63] |
| Chip Huyen: site and aie-book | https://github.com/chiphuyen/aie-book | ML Eng; Applied AI | Book-companion repository with resources, plus an own-domain site; profile pins projects with star counts; survivor caveat [S64] |
| Anthropic: Designing AI-resistant technical evaluations | https://www.anthropic.com/engineering/AI-resistant-technical-evaluations | Infrastructure; Evaluation | Postmortem pattern: iterations, what broke, open challenge; COI [S23] |
| anthropics/original_performance_takehome | https://github.com/anthropics/original_performance_takehome | Infrastructure; Kernels | Public challenge with a route to apply; repository not opened; COI [S45] |
| Inspect AI | https://github.com/UKGovernmentBEIS/inspect_ai | Evaluation, Safety | Framework README with development, test and citation conventions [S43] |
| Inspect Evals | https://github.com/UKGovernmentBEIS/inspect_evals | Evaluation, Safety | Registration route (arXiv URL plus source link); maintenance paper on 70+ evaluations [S43] |
| NVIDIA KGMoN team | https://blogs.nvidia.com/?p=67659 | ML Eng; Research | Members publish code, discussions and tutorials; employer asks for the record [S35] |
| Anthropic: Demystifying evals for AI agents | https://www.anthropic.com/research/demystifying-evals-for-ai-agents | Evaluation; Applied AI | Task, trial and grader vocabulary; capability versus regression evaluations; cost and latency baselines; COI [S25] |
| HF speech-to-speech and Space | https://github.com/huggingface/speech-to-speech | Applied AI (voice) | Open library paired with a public Spaces demo; both linked from the posting; not opened [S31] |
| modded-nanogpt | https://github.com/KellerJordan/modded-nanogpt | Research Eng; Infrastructure | Described in nanochat's README as gamifying nanoGPT with metrics and a leaderboard; URL from recall (D), not opened [S41] |
| vLLM | https://github.com/vllm-project/vllm | Infrastructure (inference) | Venue Inferact's postings point to; URL from recall (D), not opened [S33] |

### 13. Skill-demand shares and tutorial-grade projects (KF15)

- **RAG share.** Four analyses of AI-engineer postings put RAG at 26% (390 postings, KDnuggets summary [S60]), 29% (Heavybit [S61]), 32% (Axial Search [S61]) and 39.6-40% (InterviewStack, samples of 4,155 and 3,449 [S59]). Definitions and samples differ and all are C-grade vendor or practitioner analyses. In ML-engineer postings the figure is 15.4% (n=3,849, June 2026) [S59].
- **Evaluation share.** One 2026 analysis of 390 AI-engineer postings found 56% mention AI evaluation, 50% agents and 26% RAG [S60].
- **Tutorial-grade projects.** Practitioner and hiring-manager accounts say portfolios built only from Titanic, Iris, MNIST or house-price notebooks signal tutorial completion [S62]. The accounts are data-science-oriented, unmeasured and mostly from publishers or vendors.
- **Implication.** Retrofit RAG repositories with evaluation rather than delete them (K3); archive tutorial-only projects and upgrade them into measured systems (K7) [P].

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Headline claims V1+; authorship verification is the live problem | confirmed | Anthropic's process and redesigns [S23, S24]; 49% red flag [S37]; walk-through screens [S38]; the V1 rule is practice | B/C |
| K2 | Calibrate proof to level | unverifiable | No source calibrates by level; a Hugging Face US posting tagged Junior also asks for a public OSS record [S31] | C |
| K3 | No project type universally weak; RAG share a third to 40% | confirmed | RAG share 26-40% across four analyses [S59-S61]; ML-engineer postings 15.4% [S59]; the no-universally-weak-project half is untested | C |
| K4 | Evaluation separator; 20-50 tasks; ~100 traces; 50+50 judge labels | updated | 20-50 tasks [S25]; 100 traces holds; judge at 100-200 labels per failure mode as of 2026-09-01 [S26, S27]; evaluation named in 56% of 390 postings in one analysis [S60] | B/C |
| K5 | Two or three deep repositories | confirmed | Direction only: cheap counts discounted [S1]; pins capped at six [S5]; the number is untested | C |
| K6 | Live demo optional; risks documented | confirmed | Paid-plan rule and sleep [S11, S12]; alerts do not cap, hard limits not instantaneous [S20]; Default Workspace uncappable [S21]; key-leak risk not re-tested; weight unmeasured | B |
| K7 | Archive tutorial forks, Titanic and similar | confirmed | Fork discount [S1]; practitioner and hiring-manager accounts call Titanic, Iris and MNIST-only portfolios tutorial-grade [S62]; archive-versus-delete is practice | C |
| K8 | Writing rests on anecdotes; one Inferact posting | updated | Four Inferact postings [S33]; Hugging Face invites posts and talks [S31]; secondary report on CEO sourcing [S10]; first-person accounts [S48-S51]; the 2026-06-18 date attaches to the developer-relations posting; no blog-to-offer data | B |
| K9 | Many reviewers never open GitHub; keep keywords | updated | Employer-dependent [S31, S32, S56 versus S34, S36, S55]; 58% use AI screening in one vendor survey [S37] | C |
| K10 | 49-82% single-commit contributors; drive-by PR liability | confirmed | Liability half confirmed [S28-S30]; the 49-82% figures are internal and untested | B/C |
| K11 | GitHub Pages use-with-care | confirmed | Limits and commercial-use rule [S15] | B |
| K12 | Hugging Face Spaces paid-plan change | confirmed | Docs read in full [S11]; forum confusion [S12]; $9 PRO price on HF pages [S13] | A |
| K13 | Railway tiers | confirmed | [S16] | B |
| K14 | Replicate part of Cloudflare | confirmed | Announced 2025-11-17; closing stated 2025-12-01 [S17] | B |
| K15 | Read.cv closed | confirmed | [S18] | B |
| K16 | GitHub Actions free on public repositories | confirmed | Larger runners excluded; self-hosted fee postponed [S14] | B |
| K17 | Shields endpoint JSON | confirmed | [S19] | B |
| K18 | OpenAI hard limit | confirmed | 429 behaviour; not instantaneous [S20] | B |
| K19 | Claude Console workspace limits | confirmed | [S21] | B |
| K20 | OSS Insight | confirmed | Docs state 5+ billion rows; free; REST API [S22] | B |
| K21 | git log on treeless clone | updated | Plain git log needs only commits; path-filtered log downloads trees for almost every commit; GitHub advises against daily use and recommends blobless clones for history queries [S47] | B |
| K22 | GraphQL API, research only (AUP section 7) | updated | AUP clause sits under "Services Usage Limits" (section 6 in the extract), with an added research clause tied to open-access publication [S4]; 5,000 points/hour confirmed [S46] | B |

## Absences

| Item | Where looked | Result |
|---|---|---|
| Measured open rates, stage or duration for GitHub, sites, blogs | CSCW and IEEE papers; vendor and hiring-manager surveys; practitioner posts | 2013 interviews and a 2021 self-selected survey only; vendor percentages untraceable |
| A traced origin for "87% of tech recruiters review GitHub" | Several vendor and SEO pages | Not traceable, grade E; the trail ended at unsourced pages |
| Evaluator inference from graph, stars and followers after 2013 | Peer-reviewed searches | None found |
| Blog or talk to interview and offer rates | Employer statements; first-person accounts | No dataset; accounts come from survivors |
| Weight of a live demo against a repository | Practitioner and survey searches | None |
| Large-sample or peer-reviewed data on reception of AI-written READMEs and blogs | Vendor surveys; practitioner posts | Only an application-material survey found |
| Reviewer behaviour at Big Tech and India IT-services employers | Postings and hiring posts | Not found beyond posting text; eleven India enterprise and IT-services postings sampled |
| Level-calibrated proof standards (K2) | Not measured | Gap |
| Leadership and Executive roles | Nine Leadership postings plus one fractional posting; no exemplars | Thin |
| Verified exemplars for governance, product, human-data and embodied roles | Searches returned postings, not exemplars | None verified |
| Opened pages for further individual exemplars (for example Sebastian Raschka's site, Jason Liu) | Not opened | Not listed |
| Business Insider original article | Not opened | Secondary only, grade C |
| Site-generator comparison (Astro, Hugging Face, Jekyll, Quarto) | Not researched | Gap |

## Open Questions & Risks

**Risks.** Selection bias in the postings sample (clustering, queries including search terms, extract-only reading). Stale peer-reviewed evidence (2013). Platform volatility (Hugging Face policy, GitHub settings). Vendor COI in several surveys (S6-S9, S37, S38). Extract-only evidence for almost all sources. First-person writing accounts are survivor-biased.

**Open question.** What link-open rate would candidate-side tracked links or applicant-tracking analytics show, by employer type?

**Strongest objections.**

| Objection | For | Against |
|---|---|---|
| Recruiters do not open GitHub; this is noise | 51% no lower chances without a site [S6]; 15% weight [S7]; FDE, governance and human-data postings ask nothing [S34, S36, S55] | Hugging Face, Sarvam and embodied employers ask explicitly [S31, S32, S56]; 2013 employer interviews [S1] |
| Survivorship: exemplars were hired for other reasons | Willison, Karpathy and Raschka are prominent | No counterfactual data; unresolved |
| A live demo beats a repository | Practitioner claims [S38] | No measurement; hosting and spend risks [S11, S20] |
| AI makes artefacts cheap, so employers move to live tests | Anthropic's process [S23]; 49% flag AI-written materials [S37] | Hugging Face asks for a reviewable record [S31]; open challenge shows artefacts remain in use [S45] |
| The postings sample is biased | True | Per-cluster counts reported; no rate claimed |
| Evidence is old and platforms changed | True for 2013 | 2024 star-fraud data corroborates the structure [S3] |
| India GCCs rely on the applicant-tracking system, not GitHub | Plausible; Walmart India and IT-services postings mostly silent (2 of 11) [S58, S66] | Eleven postings only; Sarvam is a startup outlier [S32] |

## Discovered Concerns

1. **GitHub policy and research method (K22).** Public non-personal data may be used for research only if resulting publications are open access, and use for recruiter lead lists is barred [S4]. This matters for any knowledge-base research that uses GitHub data.
2. **Hugging Face Spaces change.** Tutorials describing free Gradio Spaces on CPU are stale [S11-S13]. Demo decision trees should default to static or replay.
3. **Inspect Evals route.** Contributions go through a registration step [S43]; direct-PR assumptions in open-source guidance are stale.
4. **Pull-request restrictions.** GitHub added disable and restrict settings, and several projects closed external PRs [S28-S30].
5. **Actions pricing.** The self-hosted runner fee was postponed after announcement; larger runners are not free for public repositories [S14].
6. **Anthropic open take-home** is a hiring route that is itself COI-sensitive [S45].
7. **Vendor-survey COI.** Resume, mentoring and recruiting vendors supply many "recruiter" statistics [S8, S37, S38].
8. **Treeless clones.** GitHub advises against them for daily work; repository-research methods that use path-filtered history should use blobless clones [S47].
9. **Platform dependence in writing.** Hugging Face lists blog publishing among PRO features [S13]; the Read.cv closure shows the portability risk [S18].
10. **Skill-demand analyses.** Posting-share figures come from interview-prep vendors and practitioner blogs with partly disclosed methods; RAG shares range from 26% to 40% [S59-S61].

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Recruiters usually open GitHub links | Updated | Employer-dependent; no measurement [S31, S32, S34, S36, S55, S56] | Check each posting's wording |
| P2 | Sites add little | Confirmed | [S6] [S7] | Site is optional |
| P3 | Stars, followers and graph are weak | Confirmed | [S1] [S3] [S4] [S5] | Do not invest in them |
| P4 | Free Gradio Spaces for individuals | Contradicted | [S11] [S12] | Use static or replay |
| P5 | Kaggle is mainstream | Contradicted | [S35] | Role-specific only |
| P6 | Peer-reviewed measurements for 2023-2026 exist | Contradicted | None found; interviews date to 2013 [S1] | Keep claims at practice grade |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Activity Traces and Signals in Software Developer Recruitment and Hiring, Marlow and Dabbish, CSCW 2013. https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf | 2013-02 | 2026-11-13 | A | Read | stale-risk | Employer inference, signal reliability |
| S2 | Assessing Technical Candidates on the Social Web, IEEE Software 30(1). https://bura.brunel.ac.uk/handle/2438/7042 | 2013 | 2026-11-13 | B | Extract | stale-risk | Signal interpretation and manipulation |
| S3 | 4.5 Million (Suspected) Fake Stars in GitHub, arXiv 2412.13459. https://arxiv.org/html/2412.13459v1 | 2024-12 | 2026-11-13 | B | Extract | preprint; v1 figures | Star fraud |
| S4 | GitHub Acceptable Use Policies, GitHub. https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies ; archived capture 2020-11-19 https://webcf.waybackmachine.org/web/20201119121944/https://docs.github.com/en/free-pro-team%40latest/articles/github-acceptable-use-policies | n/d | 2026-11-13 | B | Extract | archived | K22; rank abuse |
| S5 | Viewing contributions on your profile, GitHub Docs (GHES 3.12 copy). https://docs.github.com/en/enterprise-server@3.12/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/viewing-contributions-on-your-profile | n/d | 2026-11-13 | B | Extract | stale-risk | Graph rules; six pins |
| S6 | Don't waste your time on a (React) portfolio website, Profy.dev. https://dev.to/profydev/this-survey-among-60-hiring-managers-reveals-don-t-waste-your-time-on-a-react-portfolio-website-17ge (reader copy https://hn.jakechampion.name/reader/https://profy.dev/article/portfolio-websites-survey) | 2021-08 (Reddit post 2021-08-06) | 2026-11-13 | C | Extract | self-selected; stale-risk | Site survey |
| S7 | Gun.io article on portfolios. https://gun.io/?p=2956 | n/d | 2026-11-13 | C | Extract | vendor; single-source | Site weight |
| S8 | How to Hire AI Engineers, Underdog.io. https://underdog.io/blog/how-to-hire-ai-engineers | 2026-08-15 | 2026-11-13 | C | Extract | COI | Sourcing channels |
| S9 | Software Engineer Portfolio That Proves You Can Ship, Underdog.io (cites daily.dev 2025 survey). https://underdog.io/blog/software-engineer-portfolio | 2025 | 2026-11-13 | C | Extract | COI; secondary | Developer self-view |
| S10 | Summary of Business Insider report on AI coding startups' recruiting. https://econdash.org/news/bootcamps-work-trials-token-burn-inside-the-recruiting-practices-at-the-hottest--129450 ; https://letsdatascience.com/news/cursor-uses-coordinated-recruiting-for-ai-engineers-ab34211f | 2026-08-09 | 2026-11-13 | C | Extract | secondary | CEO profile scanning |
| S11 | Spaces Overview, Hugging Face Hub docs. https://huggingface.co/docs/hub/en/spaces-overview | n/d | 2026-11-13 | A | Read | corroborated | K12; sleep |
| S12 | Hugging Face forum threads on CPU Basic and Docker Spaces. https://discuss.huggingface.co/t/free-cpu-basic-quota-is-0-on-new-account/180764 ; https://discuss.huggingface.co/t/new-free-accounts-cannot-create-cpu-basic-gradio-spaces-only-zerogpu-available/177629 | 2026 (n/d) | 2026-11-13 | C | Extract | user posts | Policy change |
| S13 | Hugging Face pricing and PRO subscription pages; eesel.ai explainer for daily quotas. https://huggingface.co/pricing ; https://huggingface.co/subscribe/pro ; https://www.eesel.ai/en/blog/hugging-face-pricing | n/d | 2026-11-13 | B | Extract | corroborated; eesel is C | PRO price; blog publishing feature |
| S14 | About billing for GitHub Actions, GitHub Docs; Pricing changes for GitHub Actions, GitHub Resources. https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions ; https://resources.github.com/actions/2026-pricing-changes-for-github-actions/ | 2025-12-15 to 2025-12-17 | 2026-11-13 | B | Extract | corroborated | K16 |
| S15 | GitHub Pages limits, GitHub Docs. https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits | n/d | 2026-11-13 | B | Extract | | K11 |
| S16 | Pricing Plans, Railway Docs. https://docs.railway.com/pricing/plans | n/d | 2026-11-13 | B | Extract | | K13 |
| S17 | Cloudflare to Acquire Replicate, Business Wire; Why Replicate is joining Cloudflare, Cloudflare Blog. https://www.businesswire.com/news/home/20251117400765/en/Cloudflare-to-Acquire-Replicate-to-Build-the-Most-Seamless-AI-Cloud-for-Developers ; https://blog.cloudflare.com/why-replicate-joining-cloudflare/ | 2025-11-17; 2025-12-01 | 2026-11-13 | B | Extract | corroborated | K14 |
| S18 | Perplexity acquires Read.cv, TechCrunch; Read.cv wind-down timeline, Neowin. https://techcrunch.com/2025/01/17/perplexity-acquires-read-cv-a-social-media-platform-for-professionals/ ; https://www.neowin.net/news/readcv-announces-acquisition-by-perplexity-as-it-begins-winding-down-operations/ | 2025-01-17 | 2026-11-13 | B | Extract | corroborated | K15 |
| S19 | Endpoint Badge, Shields.io. https://shields.io/badges/endpoint-badge | n/d | 2026-11-13 | B | Extract | stale-risk | K17 |
| S20 | Spend limits, OpenAI developer docs. https://developers.openai.com/api/docs/guides/spend-limits | n/d | 2026-11-13 | B | Extract | | K18 |
| S21 | Workspaces, Claude Platform docs; Understanding usage and spend limits, Claude Help. https://platform.claude.com/docs/en/manage-claude/workspaces.md ; https://support.claude.com/en/articles/9796807-understanding-usage-and-spend-limits | n/d | 2026-11-13 | B | Extract | COI | K19 |
| S22 | About OSS Insight, OSS Insight docs. https://ossinsight.io/docs | n/d | 2026-11-13 | B | Extract | | K20 |
| S23 | Designing AI-resistant technical evaluations, Anthropic Engineering. https://www.anthropic.com/engineering/AI-resistant-technical-evaluations | 2026-01-21 | 2026-11-13 | B | Extract | COI | Authorship; exemplar |
| S24 | Anthropic manager drops coding interviews, TechSpot. https://www.techspot.com/news/114391-anthropic-manager-drops-coding-interviews-after-realizing-claude.html | 2026 (n/d) | 2026-11-13 | B | Extract | | Candidate AI guidance |
| S25 | Demystifying evals for AI agents, Anthropic; summary at besthub.dev. https://www.anthropic.com/research/demystifying-evals-for-ai-agents ; https://www.besthub.dev/articles/decoding-anthropic-s-agent-evaluation-methodology-challenges-graders-and-best-practices-811e7442e485 | 2026-01 | 2026-11-13 | B | Extract | COI; 20-50 figure from secondary | K4 |
| S26 | AI Evals FAQ: How many examples do I need, Husain and Shankar. https://hamel.dev/blog/posts/evals-faq/how-many-examples-do-i-need-for-an-eval.html | 2026-09-01 (modified) | 2026-11-13 | C | Extract | named practitioners | K4 |
| S27 | Eval Audit skill, aiuxplayground.com. https://aiuxplayground.com/skills/eval-audit | n/d | 2026-11-13 | C | Extract | secondary | Earlier 50+50 figure |
| S28 | GitHub ponders kill switch for pull requests, The Register. https://www.theregister.com/2026/02/03/github_kill_switch_pull_requests_ai | 2026-02-03 | 2026-11-13 | B | Extract | | PR controls |
| S29 | Open source has a big AI slop problem, LeadDev. https://leaddev.com/software-quality/open-source-has-a-big-ai-slop-problem | 2026-02-17 | 2026-11-13 | B | Extract | | curl, tldraw |
| S30 | Is AI overwhelming open source, Telerik; open-source review-cost table, braindetox.kr. https://www.telerik.com/blogs/is-ai-overwhelming-open-source ; https://braindetox.kr/en/posts/open_source_ai_contributions_review_cost_2026.html | 2026 (n/d) | 2026-11-13 | C | Extract | secondary | Ladybird; 2026-02-13 setting |
| S31 | Hugging Face postings on Workable (EMEA 81B46579FE, US 19A136F8E2, Voice 9E2A4C02C7). https://apply.workable.com/huggingface/jobs/view/81B46579FE | 2026-05-29 | 2026-11-13 | B | Extract | corroborated | Postings 1-3 |
| S32 | Sarvam postings. https://www.sarvam.ai/careers/jobs/282019f4-f86b-4fe0-a643-bbac0cd8a751 ; https://careers.kula.ai/sarvam-ai/17537/apply ; https://careers.kula.ai/sarvam-ai/14292 ; https://careers.kula.ai/sarvam-ai/2955 ; https://careers.kula.ai/sarvam-ai/5594/ ; https://careers.kula.ai/sarvam-ai/5607/ ; https://www.sarvam.ai/careers/jobs/e9fb1269-fc4b-4879-aa35-0b75a8c83611 ; https://careers.kula.ai/sarvam-ai/32675 ; https://simplify.jobs/p/5a60cb12-db16-4fc2-ac53-31dd2ab08a3c/ML-Engineer | 2026 (n/d) | 2026-11-13 | B | Extract | templated; mirrors | Postings 4-12 |
| S33 | Inferact postings. https://startup.jobs/member-of-technical-staff-inference-inferact-8280046 ; https://startup.jobs/member-of-technical-staff-kernel-engineering-inferact-8115126 ; https://seedtable.com/jobs/14084 ; https://standout.work/jobs/member-of-technical-staff-exceptional-generalist-remote-at-inferact | 2026-06 (DevRel 2026-06-18) | 2026-11-13 | B | Extract | aggregator copies | Postings 13-16 |
| S34 | Forward Deployed Engineer, Anthropic (Greenhouse). https://job-boards.greenhouse.io/anthropic/jobs/4985877008 | n/d | 2026-11-13 | A | Read | COI | Posting 17 |
| S35 | NVIDIA KGMON and related postings; KGMoN blog. https://findroles.com/jobs/5465402090-senior-applied-agent-research-engineer ; https://jobs.anitab.org/companies/nvidia/jobs/91456990-senior-applied-research-scientist-data-curation ; https://www.talentify.io/job/senior-llm-technologist---nvidia-jr1974253-5 ; https://blogs.nvidia.com/?p=67659 | 2025-12 to 2026-03 | 2026-11-13 | B | Extract | aggregator copies | Postings 18-20; Kaggle |
| S36 | AI-governance postings. https://www.teneo.com/careers/open-positions/7786577003/ ; https://jobs.mitalent.org/job-seeker/job-details/JobCode/344710675 ; https://app.qureos.com/company/hiringMavericks ; https://www.wearedevelopers.com/en/jobs/ext/5947324/ai-governance-lead ; https://www.wearedevelopers.com/en/jobs/ext/6071633/ai-governance-manager ; https://www.barclaysimpson.com/job/mjs-44736/ai-governance-manager/ | 2026 (n/d) | 2026-11-13 | B | Extract | mirrors | Postings 21-26 |
| S37 | Resume Genius 2026 Hiring Trends Report, via CPA Practice Advisor. https://www.cpapracticeadvisor.com/?p=188492 | 2026-08-13 | 2026-11-13 | C | Extract | COI; secondary | AI red flag |
| S38 | Entry-level hiring filters, MentorCruise. https://mentorcruise.com/blog/how-to-get-an-entry-level-software-engineer-job-what-hiring-managers-actually-fi/ | 2026 (n/d) | 2026-11-13 | C | Extract | COI | Walk-through screens |
| S39 | How AI changes developer portfolios, The New Stack. https://thenewstack.io/how-ai-changes-developer-portfolios/ | n/d | 2026-11-13 | C | Extract | | Paper-trail advice |
| S40 | What's documented in AI? 32K model cards, Liang et al.; Nature Machine Intelligence 6(7). https://arxiv.org/abs/2402.05160v1 ; https://scholars.duke.edu/publication/1684733 | 2024-07 | 2026-11-13 | B | Extract | peer-reviewed | Model-card findings |
| S41 | karpathy/nanochat README. https://github.com/karpathy/nanochat | n/d (entries to 2026-03-09) | 2026-11-13 | B | Extract | | README exemplar |
| S42 | Building a self-updating profile README for GitHub, Willison. https://simonwillison.net/2020/Jul/10/self-updating-profile-readme | 2020-07-10 | 2026-11-13 | B | Extract | stale-risk | Profile exemplar |
| S43 | Inspect Evals README; arXiv 2507.06893; CASRAI guide. https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_evals/main/README.md ; https://arxiv.org/html/2507.06893v1 ; https://casrai.org/guides/inspect-ai-evaluation-framework-uk-aisi | 2025-07 to 2026-09 | 2026-11-13 | B | Extract | | Evaluation exemplars |
| S44 | Sarvam AI hiring article, CareerIndia. https://www.careerindia.com/news/sarvam-ai-careers-2026-open-engineering-roles-bengaluru-application-guide-011-68035.html | 2026-11-02 (as-of) | 2026-11-13 | C | Extract | secondary | Sarvam context |
| S45 | Anthropic performance take-home coverage, Gigazine. https://gigazine.net/gsc_news/en/20260126-anthropic-claude-code-test-design | 2026-01-26 | 2026-11-13 | B | Extract | COI (about Anthropic) | Open challenge; repository URL |
| S46 | Rate limits and query limits for the GraphQL API; Resource limitations, GitHub Docs. https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api ; https://docs.github.com/graphql/overview/resource-limitations | n/d | 2026-11-13 | B | Extract | | K22 rate limit |
| S47 | Get up to speed with partial clone and shallow clone, GitHub Blog. https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/ | 2020-12-21 | 2026-11-13 | B | Extract | stale-risk | K21 |
| S48 | Simon Willison on Technical Blogging, Write That Blog. https://writethatblog.substack.com/p/simon-willison-on-technical-blogging | n/d | 2026-11-13 | C | Extract | first-person; survivor | Writing outcomes |
| S49 | Advice for Better Blog Posts, Rachel Thomas, fast.ai. https://rachel.fast.ai/posts/2019-05-13-blogging-advice | 2019-05-13 | 2026-11-13 | C | Extract | first-person; stale-risk | Writing outcomes |
| S50 | Frequently Asked Questions about My Writing Process, Eugene Yan; Amazon Science feature. https://eugeneyan.com/writing/writing-faq/ ; https://eugeneyan.com/speaking/amazon-science-feature/ | n/d | 2026-11-13 | C | Extract | first-person; survivor | Writing outcomes; exemplar |
| S51 | Can blogging about data science really get you hired, Towards Data Science. https://towardsdatascience.com/can-blogging-about-data-science-really-get-you-hired-as-a-data-scientist-7f02fec085ec/ | n/d | 2026-11-13 | D | Extract | single-source anecdote | Offer mix from one blog |
| S52 | rasbt/LLMs-from-scratch and mlabonne/llm-course repository summaries. https://www.sourcepulse.org/projects/1272031 ; https://science.ecosyste.ms/projects/52431 ; https://www.sourcepulse.org/projects/1828242 | n/d | 2026-11-13 | C | Extract | secondary; repositories not opened | Exemplars |
| S53 | Anthropic research and alignment postings; Apollo Research posting. https://www.indexventures.com/startup-jobs/anthropic/research-engineer-research-scientist-rl-frontiers/ ; https://www.indexventures.com/startup-jobs/anthropic/research-engineer-pretraining-scaling-1/ ; https://jobs.accel.com/companies/anthropic/jobs/69411776-research-engineer-scientist-alignment-science ; https://www.anthropic.com/careers/jobs/4669581008 ; https://www.indexventures.com/startup-jobs/anthropic/research-engineer-scientist-frontier-red-team-cyber/ ; https://job-boards.greenhouse.io/anthropic/jobs/5206456008 ; https://www.escapethecity.org/opportunity/10-research-scientist--engineer-at-apollo-research | 2026-03 to 2026-10-13 | 2026-11-13 | B | Extract | COI (Anthropic); mirrors | Postings 27-33 |
| S54 | AI product manager postings. https://jobgether.com/offer/69cbe8a55bd3b40540a35141-ai-product-manager ; https://www.jobera.com/job/arcade-ai-product-manager-ai-da560da1/ ; https://www.jobera.com/job/eliza-ai-product-manager-27c492d6/ ; https://www.serendipath.com/jobs/tech-product-manager-at-fractal-3431 ; https://remowork.life/jobs/6ac0a195d2f3bde811bec6a8/product-manager-ai-and-product-evaluation | 2026 (n/d) | 2026-11-13 | B | Extract | mirrors | Postings 34-38 |
| S55 | Human-data and evaluation contractor postings. https://remowork.life/jobs/6a24ad75a1c6ddd4f4b59c19/training-onboarding-landd-evaluator ; https://remowork.life/jobs/6a09def4442cac0153e5cc65/rubrics-evaluator-professional-experience ; https://remowork.life/jobs/6a24b22b22d5d46a683c3888/software-ai-it-data-evaluator ; https://tallo.com/talent/job/technology/artificial-intelligence-engineer/remote/ml-evaluation-designer-exper-e6ccd388 ; https://remowork.life/jobs/6aa851215d989acfeaedd3cf/llm-annotator-masters-degree ; https://remowork.life/jobs/69fcad61032fe6d231de6baa/generative-ai-generalist | 2026-05 to 2026-09 | 2026-11-13 | B | Extract | mirrors | Postings 39-44 |
| S56 | Embodied and robotics postings. https://visasponsor.jobs/job/robot-learning-engineer-humanoid ; https://www.1x.tech/open-positions/research-engineer-robotic-learning-2 ; https://1x.recruitee.com/o/embodied-aiagi-researcher ; https://jobs.khoslaventures.com/companies/scaled-foundations/jobs/92625815-robotics-engineer-manipulation-focus ; https://jobs.khoslaventures.com/companies/scaled-foundations/jobs/92625814-robotics-engineer-humanoids-focus ; https://www.whatjobs.com/company/skild-ai/profile | 2026 (n/d) | 2026-11-13 | B | Extract | mirrors | Postings 45-50 |
| S57 | Head of AI (VLA), Motoniq. https://diversityemployment.com/job/head-of-ai-vla | n/d | 2026-11-13 | C | Extract | single-source | Posting 51 |
| S58 | India enterprise postings: Walmart Global Tech and an unnamed Bangalore employer. https://simplify.jobs/p/223ccd15-851c-44fb-90bb-1787865c6a1b/Staff--Software-Engineer ; https://jobs.anitab.org/companies/walmart/jobs/73729081-senior-software-engineer ; https://jobs.anitab.org/companies/walmart/jobs/83335806-ind-data-scientist-iii ; https://jobs.anitab.org/companies/walmart/jobs/92686797-ind-senior-data-scientist ; https://www.monster.co.th/job/generative-ai-engineer-suitable-ai-bengaluru-bangalore-61158137 | 2025-11 to 2026-09 | 2026-11-13 | B | Extract | mirrors | Postings 52-56 |
| S59 | AI-engineer skill analyses, InterviewStack.io (also on DEV). https://interviewstack.io/blog/how-ai-is-changing-ai-engineer-2026 ; https://dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l ; https://dev.to/gnana_6392e836fd500a957dc/ai-is-rewriting-the-machine-learning-engineer-job-in-2026-50pi | 2026 (ML-engineer sample 2026-06) | 2026-11-13 | C | Extract | COI (interview-prep vendor); method partly disclosed | RAG share (K3) |
| S60 | The AI Skills That Actually Show Up in Job Postings, KDnuggets. https://www.kdnuggets.com/the-ai-skills-that-actually-show-up-in-job-postings-right-now | 2026 (n/d) | 2026-11-13 | C | Extract | secondary; origin of the 390-posting analysis not identified | RAG and evaluation shares |
| S61 | So You Want to Be an AI Engineer, Heavybit; AI engineering skills, Axial Search. https://heavybit.com/library/article/so-you-want-to-be-an-ai-engineer ; https://axialsearch.com/insights/ai-engineering-skills | 2026 (n/d) | 2026-11-13 | C | Extract | practitioner; method not seen | RAG share |
| S62 | Tutorial-project statements: Statology; KDnuggets 2022 and 2019; Dataquest. https://www.statology.org/what-titanic-iris-and-house-prices-say-about-your-portfolio/ ; https://www.kdnuggets.com/2022/05/data-science-projects-land-job-2022.html ; https://kdnuggets.com/2019/12/4-ways-not-hired-data-scientist.html ; https://dataquest.io/blog/building-and-presenting-your-data-portfolio | 2019-12 to 2026 (Dataquest 2025-02-28) | 2026-11-13 | C | Extract | practitioner; data-science focus; review-time claim is D | K7; review time |
| S63 | Lil'Log, Lilian Weng. https://lilianweng.github.io/ ; https://lilianweng.github.io/posts/2026-07-04-harness/ ; https://lilianweng.github.io/posts/2026-06-24-scaling-laws/ | 2026-07-04 | 2026-11-13 | B | Extract | survivor | Research exemplar |
| S64 | Chip Huyen site and aie-book repository. https://huyenchip.com/ ; https://github.com/chiphuyen/aie-book ; https://github.com/chiphuyen ; https://www.sourcepulse.org/projects/1849456 | n/d | 2026-11-13 | C | Extract | survivor; star counts from a secondary page | Exemplar |
| S65 | Leadership postings. https://www.wearedevelopers.com/jobs/ext/2599484-head-of-ai ; https://www.wearedevelopers.com/jobs/ext/584902-head-of-ai.md ; https://www.janeasystems.com/careers/5980938004 ; https://www.careers-page.com/talent-search/job/5WR7Y365 ; https://apply.workable.com/joinmakropro/jobs/view/AB3B598DB1.md ; https://www.robertwalters.co.uk/technologydigital/jobs/datascienceairesearch/1877980-head-of-ai.html ; https://www.virtualvocations.com/job/head-of-ai-2857455-i.html ; https://www.ziprecruiter.ie/jobs/563649025-head-of-ai-engineering-at-jobgether ; https://resumegeni.com/jobs/chief-ai-officer-ic-role-novatalent-167d338b39 | 2026-01 to 2026-06 (n/d for some) | 2026-11-13 | B | Extract | mirrors | Postings 57-65 |
| S66 | India IT-services postings. https://careers.hcltech.com/job/Senior-Technical-Architect/1360916555/ ; https://careers.hcltech.com/job/Technical-Consultant/1360193855/ ; https://careers.hcltech.com/job/AI-Solution-Architect-I/1358076955/ ; https://careers.cognizant.com/apj-ph/jobs/00068031261/generative-ai-architect/ ; https://resumegeni.com/jobs/gen-ai-sr-lead-8fb72333e6 ; https://www.globallogic.com/?p=163352 | 2026-04 (n/d for some) | 2026-11-13 | B | Extract | mirrors | Postings 66-71 |

## Data Appendix

```jsonl
{"type":"practice","grade":"P","src":["S5"],"as_of":"2026-11-13","ttl":"V3","area":"github-profile","tactic":"Pin up to six items and choose three deep repositories with evidence READMEs","claim":"Pins are capped at six; evidence over volume","evidence":"Cap confirmed in docs; reviewer weight unmeasured","verdict":"use","risk":"Polished pins that cannot be defended in a walkthrough"}
{"type":"practice","grade":"P","src":["S42"],"as_of":"2020-07-10","ttl":"V3","area":"github-profile","tactic":"Self-updating profile README that lists releases, posts and notes","claim":"Gives a live evidence stream","evidence":"Exemplar from 2020; benefit unmeasured","verdict":"use-with-care","risk":"Broken workflow or noise; technique is stale-risk"}
{"type":"practice","grade":"B","src":["S1","S3","S4","S5"],"as_of":"2026-11-13","ttl":"V3","area":"github-profile","tactic":"Do not invest in stars, followers or the contribution graph","claim":"Cheap signals are discounted and gameable","evidence":"2013 interviews; 4.5M suspected fake stars; policy bans rank abuse","verdict":"avoid","risk":"Account enforcement; credibility loss"}
{"type":"practice","grade":"P","src":["S25","S26","S41"],"as_of":"2026-11-13","ttl":"V3","area":"project-readme","tactic":"Results table with task count, baseline, trials and variance, plus a one-command reproduction","claim":"Makes claims regenerable","evidence":"Practitioner and employer guidance; nanochat pattern","verdict":"use","risk":"Numbers drift if data or seeds are not committed"}
{"type":"practice","grade":"B","src":["S40","S41"],"as_of":"2026-11-13","ttl":"V3","area":"project-readme","tactic":"Write an explicit limits and failure-modes section","claim":"Limitations and evaluation are the least-filled model-card sections","evidence":"32,111-card analysis; nanochat states limits","verdict":"use","risk":"Vague limits read as filler"}
{"type":"practice","grade":"P","src":["S14","S19","S25","S52"],"as_of":"2026-11-13","ttl":"V2","area":"ci","tactic":"Tests plus a capped smoke evaluation on pull requests and a scheduled full run, with an endpoint badge","claim":"Standard hosted runners are free on public repositories","evidence":"Billing docs; endpoint schema; multi-OS badge example","verdict":"use","risk":"Larger runners are not free; evaluation spend"}
{"type":"practice","grade":"A","src":["S11","S20","S21"],"as_of":"2026-11-13","ttl":"V2","area":"demo","tactic":"Replay-first demo with a hard spend limit if live and a dated last-verified note","claim":"Hosting and spend rules changed","evidence":"HF docs read in full; spend-limit docs","verdict":"use-with-care","risk":"Cap triggers 429 during review; free hardware sleeps"}
{"type":"practice","grade":"A","src":["S11","S12","S13"],"as_of":"2026-11-13","ttl":"V2","area":"demo","tactic":"Rely on free Gradio or Docker Spaces on compute","claim":"Creation requires PRO","evidence":"HF docs read in full; forum staff statements; HF pricing pages","verdict":"avoid","risk":"Dead or unbuildable demo"}
{"type":"practice","grade":"B","src":["S28","S29","S30"],"as_of":"2026-11-13","ttl":"V3","area":"open-source","tactic":"Drive-by pull requests to popular repositories for visibility","claim":"Maintainers are closing or restricting pull-request routes","evidence":"curl, tldraw, Ladybird, GitHub settings","verdict":"avoid","risk":"Rejected or ignored work"}
{"type":"practice","grade":"B","src":["S31"],"as_of":"2026-05-29","ttl":"V3","area":"open-source","tactic":"Merged, pre-discussed pull requests where the employer asks for a reviewable record","claim":"Hugging Face requires a public record reviewable on GitHub","evidence":"Employer postings","verdict":"use-with-care","risk":"Slow review; closed routes"}
{"type":"practice","grade":"P","src":["S33","S31","S48","S49","S50"],"as_of":"2026-11-13","ttl":"V3","area":"writing","tactic":"Two to four deep postmortems or evaluation write-ups with committed code","claim":"Some infrastructure employers list blogs as a bonus; survivors credit writing","evidence":"Four Inferact postings; first-person accounts; no outcome data","verdict":"use-with-care","risk":"No measured payoff; survivor bias; generic prose"}
{"type":"practice","grade":"C","src":["S23","S37","S38"],"as_of":"2026-11-13","ttl":"V3","area":"authorship","tactic":"Keep incremental history, a decision log and an AI-use note; prepare a live walkthrough","claim":"Verification is moving to process","evidence":"Anthropic redesigns; 49% red-flag survey; practitioner reports","verdict":"use","risk":"Squashed history looks fabricated"}
{"type":"practice","grade":"B","src":["S35"],"as_of":"2026-11-13","ttl":"V3","area":"kaggle","tactic":"Pursue Kaggle rank only for competition-oriented teams","claim":"Required by NVIDIA KGMON; a plus elsewhere","evidence":"NVIDIA postings","verdict":"use-with-care","risk":"Time spent where no employer asks"}
{"type":"practice","grade":"C","src":["S6","S7","S15"],"as_of":"2026-11-13","ttl":"V3","area":"portfolio-site","tactic":"Build a static site as a supplement after resume and GitHub","claim":"Reviewers look but rarely decide on it","evidence":"2021 survey; vendor survey","verdict":"use-with-care","risk":"A broken or dated site can hurt"}
{"type":"practice","grade":"B","src":["S43"],"as_of":"2026-11-13","ttl":"V3","area":"evaluation-public","tactic":"Publish an evaluation with an arXiv write-up and register it with Inspect Evals","claim":"Registration route is documented","evidence":"README and maintenance paper","verdict":"use-with-care","risk":"Process changes; slow maintainer capacity"}
{"type":"practice","grade":"M","src":["S34","S36","S55"],"as_of":"2026-11-13","ttl":"V1","area":"governance-and-human-data","tactic":"Skip a GitHub portfolio for governance and human-data roles; show sanitised artefacts, credentials and pass exercises","claim":"None of twelve governance and human-data postings asked for public work","evidence":"Postings sample","verdict":"use-with-care","risk":"Some employers may value public writing"}
{"type":"practice","grade":"M","src":["S53","S56"],"as_of":"2026-11-13","ttl":"V1","area":"research-and-embodied","tactic":"Show publications, open-source releases and demo video for research and embodied roles","claim":"Six of six embodied postings and three of six Anthropic research postings name publications or OSS","evidence":"Postings sample","verdict":"use","risk":"Extract-only reading; selection bias"}
{"type":"practice","grade":"M","src":["S54"],"as_of":"2026-11-13","ttl":"V1","area":"product","tactic":"Show one shipped prototype and a decision memo for AI product roles","claim":"Two of five postings mention a portfolio or OSS","evidence":"Postings sample","verdict":"use-with-care","risk":"Three of five postings did not mention it"}
{"type":"practice","grade":"M","src":["S32","S58","S66"],"as_of":"2026-11-13","ttl":"V1","area":"india","tactic":"Lead with GitHub at startups that ask; stay resume-first for enterprise and GCC roles","claim":"Sarvam lists GitHub or OSS in nine of nine extracts; two of eleven enterprise and IT-services postings do","evidence":"Postings sample","verdict":"use-with-care","risk":"Small, clustered sample; GCC behaviour unmeasured"}
{"type":"tool","grade":"B","src":["S15"],"as_of":"2026-11-13","ttl":"V2","id":"github-pages","name":"GitHub Pages","stage":5,"category":"Portfolio hosting","what":"Static hosting from a repository","verdict":"use-with-care","why":"Free on public repositories; limits and no commercial or SaaS use","url":"https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits","status":"active","risk":"1 GB site; soft 100 GB per month; soft 10 builds per hour","price":"Free on GitHub Free for public repositories","open_source":false}
{"type":"tool","grade":"A","src":["S11","S12","S13"],"as_of":"2026-11-13","ttl":"V2","id":"hugging-face-spaces","name":"Hugging Face Spaces","stage":5,"category":"Portfolio hosting","what":"Hosted demos","verdict":"use-with-care","why":"Static free; Gradio and Docker on compute need PRO; two free ZeroGPU Spaces","url":"https://huggingface.co/docs/hub/en/spaces-overview","status":"active","risk":"Free hardware sleeps; policy changed in 2026","price":"PRO 9 USD per month on HF pages","open_source":false}
{"type":"tool","grade":"B","src":["S16"],"as_of":"2026-11-13","ttl":"V2","id":"railway","name":"Railway","stage":5,"category":"Portfolio hosting","what":"Usage-billed app hosting","verdict":"use-with-care","why":"Free plan gives 1 USD monthly credit; Hobby minimum 5 USD","url":"https://docs.railway.com/pricing/plans","status":"active","risk":"Credit covers little; Hobby fee is due even if unused","price":"Free 0 (1 USD credit); Hobby 5 USD; Pro 20 USD per month","open_source":false}
{"type":"tool","grade":"B","src":["S17"],"as_of":"2025-12-01","ttl":"V2","id":"replicate","name":"Replicate","stage":5,"category":"Portfolio hosting","what":"Model-running API platform","verdict":"watch","why":"Part of Cloudflare from 2025-12-01; product direction may change","url":"https://blog.cloudflare.com/why-replicate-joining-cloudflare/","status":"acquired","risk":"Roadmap change","open_source":false}
{"type":"tool","grade":"B","src":["S18"],"as_of":"2025-05-16","ttl":"V2","id":"read-cv","name":"Read.cv","stage":5,"category":"Portfolio hosting","what":"Professional profile and site platform","verdict":"avoid","why":"Wound down after acquisition; export closed 2025-05-16","url":"https://techcrunch.com/2025/01/17/perplexity-acquires-read-cv-a-social-media-platform-for-professionals/","status":"closed","risk":"Platform shutdown","open_source":false}
{"type":"tool","grade":"B","src":["S14"],"as_of":"2026-11-13","ttl":"V2","id":"github-actions","name":"GitHub Actions","stage":5,"category":"Portfolio tooling","what":"CI and scheduled jobs","verdict":"use","why":"Free for standard hosted runners on public repositories","url":"https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions","status":"active","risk":"Larger runners are not free; self-hosted fee postponed, not cancelled","price":"Free for public repositories on standard runners","open_source":false}
{"type":"tool","grade":"B","src":["S19"],"as_of":"2026-11-13","ttl":"V2","id":"shields-io-endpoint-badges","name":"Shields.io endpoint badges","stage":5,"category":"Portfolio tooling","what":"Badges from a public JSON endpoint","verdict":"use-with-care","why":"schemaVersion 1, label and message required; cache below 300 seconds ignored","url":"https://shields.io/badges/endpoint-badge","status":"active","risk":"Third-party dependency; stale cache","open_source":true}
{"type":"tool","grade":"B","src":["S20"],"as_of":"2026-11-13","ttl":"V2","id":"openai-project-spend-limits","name":"OpenAI project spend limits","stage":5,"category":"Demo cost control","what":"Per-project monthly cap","verdict":"use","why":"Enforce a hard limit returns 429; alerts only notify","url":"https://developers.openai.com/api/docs/guides/spend-limits","status":"active","risk":"Enforcement is not instantaneous; small overshoot possible","open_source":false}
{"type":"tool","grade":"B","src":["S21"],"as_of":"2026-11-13","ttl":"V2","id":"anthropic-console-workspace-limits","name":"Claude Console workspace spend limits","stage":5,"category":"Demo cost control","what":"Per-workspace monthly cap","verdict":"use","why":"Default Workspace cannot be limited; workspace limit sits below organisation limit","url":"https://platform.claude.com/docs/en/manage-claude/workspaces.md","status":"active","risk":"Keys in the Default Workspace are uncapped; COI","open_source":false}
{"type":"tool","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V2","id":"oss-insight","name":"OSS Insight","stage":5,"category":"Open-source research","what":"GitHub event analytics with data explorer and REST API","verdict":"use","why":"Docs state 5+ billion rows; free","url":"https://ossinsight.io/docs","status":"active","risk":"Public data only","price":"Free","open_source":true}
{"type":"tool","grade":"B","src":["S47"],"as_of":"2026-11-13","ttl":"V2","id":"git-log-treeless-clone","name":"git log on a treeless clone","stage":5,"category":"Open-source research","what":"Repository history analysis without full checkout","verdict":"use-with-care","why":"Plain git log needs only commits; path-filtered log downloads trees for almost every commit","url":"https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/","status":"active","risk":"Slow on path-filtered history; GitHub advises against daily use; blobless clones suit history queries","open_source":true}
{"type":"tool","grade":"B","src":["S4","S46"],"as_of":"2026-11-13","ttl":"V2","id":"github-graphql-api","name":"GitHub GraphQL API","stage":5,"category":"Open-source research","what":"Programmatic profile and repository data","verdict":"use-with-care","why":"5,000 points per hour per user; policy bars unsolicited email and selling personal data to recruiters; research use needs open-access publication","url":"https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api","status":"active","risk":"Policy breach; secondary limits apply","open_source":false}
{"type":"tool","grade":"B","src":["S43"],"as_of":"2026-11-13","ttl":"V2","id":"inspect-ai","name":"Inspect AI","stage":5,"category":"Evaluation harness","what":"Evaluation framework with community evaluations registry","verdict":"use","why":"Used for public evaluations and a documented registration route","url":"https://github.com/UKGovernmentBEIS/inspect_ai","status":"active","risk":"Contribution process has changed","open_source":true}
{"type":"measure","grade":"C","src":["S6"],"as_of":"2021-08-06","ttl":"V3","subject":"Hiring managers who would definitely look at an inexperienced candidate's portfolio site","measure":"share","unit":"percent of respondents","value":65,"n":60,"method":"Self-selected online survey, frontend-weighted","note":"n given as 60+"}
{"type":"measure","grade":"C","src":["S6"],"as_of":"2021-08-06","ttl":"V3","subject":"Hiring managers who would likely look at a portfolio site","measure":"share","unit":"percent of respondents","value":93,"n":60,"method":"Self-selected online survey","note":"n given as 60+"}
{"type":"measure","grade":"C","src":["S6"],"as_of":"2021-08-06","ttl":"V3","subject":"Hiring managers saying no site would not lower a candidate's chances","measure":"share","unit":"percent of respondents","value":51,"n":60,"method":"Self-selected online survey","note":"85% said at most slightly lower"}
{"type":"measure","grade":"C","src":["S7"],"as_of":"2026-11-13","ttl":"V3","subject":"Hiring managers who say a portfolio carries weight in the decision","measure":"share","unit":"percent","value":15,"n":null,"method":"Vendor survey, method not seen","note":"95% reportedly look; date not stated"}
{"type":"measure","grade":"A","src":["S1"],"as_of":"2013-02-23","ttl":"V5","subject":"Interviews on signals in developer recruiting","measure":"count","unit":"interviews","value":13,"n":13,"method":"Qualitative interviews","note":"7 employers and 6 job seekers"}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2024-10-31","ttl":"V5","subject":"Suspected fake GitHub stars","measure":"count","unit":"stars","value":4500000,"n":null,"method":"Preprint v1 detection method","note":"Later revisions may differ"}
{"type":"measure","grade":"B","src":["S3"],"as_of":"2024-10-31","ttl":"V5","subject":"Repositories with suspected fake-star campaigns","measure":"count","unit":"repositories","value":15835,"n":null,"method":"Preprint v1","note":"Period July 2019 to October 2024"}
{"type":"measure","grade":"C","src":["S37"],"as_of":"2026-08-13","ttl":"V3","subject":"US hiring managers treating heavily AI-generated application materials as a red flag","measure":"share","unit":"percent of respondents","value":49,"n":1500,"method":"Vendor survey via secondary report","note":"COI"}
{"type":"measure","grade":"C","src":["S37"],"as_of":"2026-08-13","ttl":"V3","subject":"Hiring managers using AI to screen resumes","measure":"share","unit":"percent of respondents","value":58,"n":1500,"method":"Vendor survey via secondary report","note":"COI"}
{"type":"measure","grade":"C","src":["S9"],"as_of":"2025-12-31","ttl":"V3","subject":"Developers saying GitHub best represents their skills","measure":"share","unit":"percent of respondents","value":37,"n":4040,"method":"daily.dev survey via secondary page","note":"Portfolios 17%, LinkedIn 14%; developers' self-view"}
{"type":"measure","grade":"B","src":["S40"],"as_of":"2024-07-01","ttl":"V5","subject":"Hugging Face model cards analysed","measure":"count","unit":"model cards","value":32111,"n":74970,"method":"Content analysis of 74,970 model repositories","note":"Limitations, evaluation and environmental sections least filled"}
{"type":"measure","grade":"B","src":["S40"],"as_of":"2024-02-07","ttl":"V5","subject":"Popular models given detailed cards in an intervention study","measure":"count","unit":"models","value":42,"n":42,"method":"Intervention study","note":"Moderate correlation with weekly downloads"}
{"type":"measure","grade":"B","src":["S23"],"as_of":"2026-01-21","ttl":"V3","subject":"Candidates who completed Anthropic's performance take-home","measure":"count","unit":"candidates","value":1000,"n":null,"method":"Employer statement, approximate","note":"About one and a half years; COI"}
{"type":"measure","grade":"C","src":["S26"],"as_of":"2026-09-01","ttl":"V3","subject":"Labelled examples per LLM-judge failure mode","measure":"range","unit":"examples","lo":100,"hi":200,"n":null,"method":"Practitioner guidance","note":"Start with 100 traces; annotate at least 30 yourself"}
{"type":"measure","grade":"B","src":["S25"],"as_of":"2026-01-31","ttl":"V3","subject":"Initial evaluation tasks drawn from real failures","measure":"range","unit":"tasks","lo":20,"hi":50,"n":null,"method":"Employer guidance via secondary summary","note":"COI"}
{"type":"measure","grade":"M","src":["S31","S32","S33","S34","S35","S36","S53","S54","S55","S56","S57","S58","S65","S66"],"as_of":"2026-11-13","ttl":"V1","subject":"Sampled GenAI postings naming public work","measure":"count","unit":"postings","value":37,"n":71,"method":"Purposive, clustered sample of 71 postings at 40 employers or posters; extracts except one full read","note":"52.1 percent; selection-biased, not a rate"}
{"type":"measure","grade":"M","src":["S31","S35","S56","S57","S65"],"as_of":"2026-11-13","ttl":"V1","subject":"Sampled postings where public work is required or must-have","measure":"count","unit":"postings","value":10,"n":71,"method":"Same sample","note":"Hugging Face x3, NVIDIA x2, 1X, General Robotics, Motoniq, Janea Systems, one CTO and CAIO posting"}
{"type":"measure","grade":"M","src":["S31"],"as_of":"2026-11-13","ttl":"V1","subject":"Hugging Face postings naming a public OSS record","measure":"count","unit":"postings","value":3,"n":3,"method":"Posting extracts","note":"Reviewable on GitHub"}
{"type":"measure","grade":"M","src":["S32"],"as_of":"2026-11-13","ttl":"V1","subject":"Sarvam postings naming OSS, GitHub or publications","measure":"count","unit":"postings","value":9,"n":9,"method":"Posting extracts retrieved with GitHub-related terms","note":"Selection-biased"}
{"type":"measure","grade":"M","src":["S56"],"as_of":"2026-11-13","ttl":"V1","subject":"Embodied-AI postings naming publications or OSS","measure":"count","unit":"postings","value":6,"n":6,"method":"Posting extracts","note":"Four employers"}
{"type":"measure","grade":"M","src":["S36"],"as_of":"2026-11-13","ttl":"V1","subject":"AI-governance postings naming public work","measure":"count","unit":"postings","value":0,"n":6,"method":"Posting extracts","note":"Not seen in extracts"}
{"type":"measure","grade":"M","src":["S55"],"as_of":"2026-11-13","ttl":"V1","subject":"Human-data and evaluation contract postings naming public work","measure":"count","unit":"postings","value":0,"n":6,"method":"Posting extracts","note":"Not seen in extracts"}
{"type":"measure","grade":"M","src":["S54"],"as_of":"2026-11-13","ttl":"V1","subject":"AI product postings naming a portfolio or OSS","measure":"count","unit":"postings","value":2,"n":5,"method":"Posting extracts","note":"7AI and Arcade"}
{"type":"measure","grade":"M","src":["S58","S66"],"as_of":"2026-11-13","ttl":"V1","subject":"India enterprise and IT-services postings naming OSS or publications","measure":"count","unit":"postings","value":2,"n":11,"method":"Posting extracts","note":"Walmart Staff posting (preferred) and HCLTech architect posting (optional)"}
{"type":"measure","grade":"A","src":["S11"],"as_of":"2026-11-13","ttl":"V2","subject":"Free-account ZeroGPU Spaces allowed","measure":"limit","unit":"Spaces","value":2,"n":null,"method":"Official docs","note":"Gradio and Docker on compute need PRO"}
{"type":"measure","grade":"B","src":["S13"],"as_of":"2026-11-13","ttl":"V2","subject":"Hugging Face PRO monthly price","measure":"price","unit":"USD per month","value":9,"n":null,"method":"HF pricing page extract","note":"Includes publishing blog articles on an HF profile"}
{"type":"measure","grade":"B","src":["S14"],"as_of":"2025-12-17","ttl":"V2","subject":"Proposed self-hosted runner platform charge, postponed","measure":"price","unit":"USD per minute","value":0.002,"n":null,"method":"Vendor announcement","note":"Postponed after announcement of 2025-12-15"}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-11-13","ttl":"V2","subject":"Maximum pinned items on a profile","measure":"limit","unit":"items","value":6,"n":null,"method":"Docs extract","note":"Public repositories or gists"}
{"type":"measure","grade":"B","src":["S22"],"as_of":"2026-11-13","ttl":"V2","subject":"OSS Insight GitHub events dataset size","measure":"count","unit":"rows","value":5000000000,"n":null,"method":"Docs statement","note":"Stated as 5+ billion"}
{"type":"measure","grade":"B","src":["S46"],"as_of":"2026-11-13","ttl":"V2","subject":"GraphQL API primary rate limit per user","measure":"limit","unit":"points per hour","value":5000,"n":null,"method":"Docs extract","note":"GITHUB_TOKEN in Actions: 1,000 points per hour per repository"}
{"type":"measure","grade":"C","src":["S29","S30"],"as_of":"2026-01-31","ttl":"V3","subject":"curl share of valid bug-bounty reports","measure":"share","unit":"percent, upper bound","value":5,"n":null,"method":"Secondary reports of maintainer statements","note":"Programme ended January 2026"}
{"type":"practice","grade":"M","src":["S57","S65"],"as_of":"2026-11-13","ttl":"V1","area":"leadership","tactic":"Show talks, publications and OSS leadership where the posting asks for them","claim":"Four of nine Leadership postings ask for publications, OSS or speaking; two as requirements","evidence":"Postings sample","verdict":"use-with-care","risk":"Small sample; duties often listed instead of evidence"}
{"type":"practice","grade":"C","src":["S1","S62"],"as_of":"2026-11-13","ttl":"V3","area":"portfolio-projects","tactic":"Archive tutorial-only projects (Titanic, Iris, MNIST) and upgrade them into measured systems","claim":"Practitioners call tutorial-only portfolios a weak signal","evidence":"Practitioner and hiring-manager accounts; fork discount in 2013 interviews","verdict":"use","risk":"Data-science sources; unmeasured for GenAI roles"}
{"type":"measure","grade":"M","src":["S65"],"as_of":"2026-11-13","ttl":"V1","subject":"Leadership postings naming publications, OSS or speaking","measure":"count","unit":"postings","value":4,"n":9,"method":"Posting extracts","note":"Two as requirements (Janea Systems; CTO and CAIO posting)"}
{"type":"measure","grade":"C","src":["S59","S60","S61"],"as_of":"2026-11-13","ttl":"V3","subject":"AI-engineer postings mentioning RAG","measure":"share","unit":"percent of postings","lo":26,"hi":40,"n":null,"method":"Four vendor or practitioner analyses; samples of 390 to 4,155 postings","note":"26 (KDnuggets summary), 29 (Heavybit), 32 (Axial Search), 39.6 to 40 (InterviewStack); definitions differ"}
{"type":"measure","grade":"C","src":["S60"],"as_of":"2026-11-13","ttl":"V3","subject":"AI-engineer postings mentioning AI evaluation","measure":"share","unit":"percent of postings","value":56,"n":390,"method":"2026 analysis summarised by KDnuggets; origin not identified","note":"Agents 50%, RAG 26%"}
{"type":"measure","grade":"C","src":["S59"],"as_of":"2026-06-30","ttl":"V3","subject":"ML-engineer postings mentioning RAG","measure":"share","unit":"percent of postings","value":15.4,"n":3849,"method":"Vendor analysis, June 2026","note":"Vendor COI"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Measured open rates, stage and duration for recruiters opening GitHub, sites and blogs","searched":"CSCW and IEEE papers; vendor and hiring-manager surveys; practitioner posts","note":"Only 2013 interviews and a 2021 self-selected survey found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Original measurement behind the claim that 87% of tech recruiters review GitHub","searched":"Several vendor and SEO pages","note":"Trail ended at unsourced pages"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Evaluator inference from contribution graph, stars and followers after 2013","searched":"Peer-reviewed searches on GitHub hiring signals","note":"None found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Blog or talk to interview and offer rates","searched":"Employer statements; first-person accounts","note":"No dataset; accounts come from survivors"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Weight of a live demo against a repository","searched":"Practitioner and survey searches","note":"Unmeasured"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Large-sample or peer-reviewed data on reception of AI-written READMEs and blogs","searched":"Vendor surveys; practitioner posts","note":"Only application-material survey found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Reviewer behaviour at Big Tech and India IT-services employers","searched":"Postings and hiring posts","note":"Eleven India enterprise and IT-services postings sampled"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Level-calibrated proof standards (K2)","searched":"Not measured in this session","note":"Unverifiable"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Leadership and Executive postings and exemplars","searched":"Nine Leadership postings and one fractional posting","note":"Thin; no exemplars"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Verified exemplars for governance, product, human-data and embodied roles","searched":"Searches returned postings, not exemplars","note":"None verified"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Opened pages for further individual exemplars (for example Sebastian Raschka's site, Jason Liu)","searched":"Not opened","note":"Not listed"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Business Insider original article on AI coding startups' recruiting","searched":"Secondary summaries only","note":"Graded C"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Site-generator comparison (Astro, Hugo, Jekyll, Quarto)","searched":"Not researched","note":"Out of time budget"}
```
