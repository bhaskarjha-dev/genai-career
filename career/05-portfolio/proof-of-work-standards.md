---
id: portfolio.proof-of-work-standards
title: "Proof-of-Work Standards: What a GenAI Portfolio Must Show to Be Believed"
content_type: guide
stage: 5
status: published
last_verified: 2026-11-19
review_by: 2027-01-19
summary: "What a GenAI portfolio must show to be believed at your target level: the verifiability ladder (V0–V3), the 15 artefacts by tier, nine anti-portfolio patterns, open-source employer-domain commit map, the public micro-audit operating system with legal guardrails and break-even effort math, and demo hardening."
sources: [T0-13, T0-20, T2-01, T0-06, T0-05, T0-68]
roles: [all]
geos: [global, india]
tags: [portfolio, proof-of-work, verifiability, evaluation, benchmarks, observability, demo-hardening, anti-portfolio, open-source, github, micro-audit]
---

# Proof-of-Work Standards: What a GenAI Portfolio Must Show to Be Believed

> What a GenAI portfolio must show to be believed at your target level: the verifiability ladder (V0–V3), the 15 artefacts by tier, nine anti-portfolio patterns, the open-source employer-domain commit map, the public micro-audit operating system with legal guardrails and break-even effort maths, and demo hardening.

**Dates.** Tool, platform and price facts combine [T0-13](../../research/sessions/T0-13-production-portfolio-proof-of-work-standards.md) (retrieved 2026-10-21), [T0-05](../../research/sessions/T0-05-unconventional-hiring-tactics-oss-audits.md) (retrieved 2026-10-21), [T0-20](../../research/sessions/T0-20-github-readme-portfolio-site-writing.md) and [T0-68](../../research/sessions/T0-68-learning-resources-rated.md) (retrieved 2026-11-13; hosting, GPU rental and policy facts re-checked 2026-11-19); re-verify tool and price facts by 2027-01-19 (90 days from the earliest unrefreshed T0-13 prices; re-check marketplace GPU rates monthly). **Grades** (EGP-1.0): A primary or measured; B transparent secondary; C vendor, practitioner or single source; D judgement or synthesis; E searched, not found; M model output; P practice-curated and unmeasured. **Confidence.** T0-13 rates its hiring-effect claims low to medium (practitioner testimony, no controlled study) and its tool facts medium to high; its level model, artefact list, rubric and hardening checklist are its own synthesis, and the rubric is untested [T0-13 L24, L246, L260, L510]. T0-20 opened only 3 of its 66 sources in full (5%), so its remaining rows rest on search extracts capped at Grade B or lower [T0-20 L22]. **Disclaimer:** legal, terms-of-service and vulnerability-disclosure material below is an evidence pointer, **not legal advice**.

## The short answer

1. **Lower the reviewer's cost of checking you.** READMEs and dashboards are cheap to generate, so authorship verification is moving to process [B/C · T0-13.F8; T0-20 L62]: 49% of 1,500 surveyed US hiring managers (Resume Genius 2026, COI) flag heavily AI-generated materials, practitioners report 10-minute code walkthrough screens [C · T0-20 L62, L228], and every channel is raising its guard against low-effort volume [B/C · T0-05.F12]. Every headline claim must be V1 or better: one command regenerates it from committed data [D · T0-13 L134, L138].
2. **Calibrate to the level you target — while reading the posting first.** T0-13's synthesis targets one measured V1 system for new graduate/junior, evaluation-gated releases plus a 30-day operating log for mid, at least one V2 item for senior, and V2 as the norm plus adoption for staff/principal [D · T0-13 L138, L272–277]. Note that no empirical source calibrates proof by level: even a Junior-tagged Hugging Face US posting requests a public OSS record [C · T0-20 L372].
3. **Fix the failure modes; keep the topic.** No project type is universally flagged. What reads as tutorial-grade is no measurement, no baseline, no deployment hygiene, a one-shot commit history and unexplained choices [C · T0-13.F2]. RAG appears in 26–40% of AI-engineer postings across four 2026 analyses (15.4% in ML-engineer postings) [B · T0-13 L91; C · T0-20 L72, L362], so retrofit a RAG repo with evaluation rather than delete it [D · T0-13 L140; T0-20 L365].
4. **Make evaluation the core.** It is the most consistently cited separator (56% of 390 AI-engineer postings in one 2026 analysis [C · T0-20 L63, L363]) [B · T0-13.F3]. Start with 20 to 50 tasks drawn from real failures, code graders first, model graders calibrated against human labels and several trials [A · T0-13.F4; B · T0-20 L63]. Husain and Shankar's AI Evals FAQ (updated 2026-09-01) recommends reviewing ~100 traces, manually annotating at least 30 yourself first, and collecting **100 to 200 human-labelled examples per LLM-judge failure mode**, superseding the earlier 50 pass plus 50 fail rule of thumb [C · T0-20 L63, L196, L374].
5. **Go deep, not wide.** GitHub caps pinned items at six [B · T0-20 L157]; keep 2 to 3 deep repos rather than many small demos [C · T0-13 L161; P · T0-20 L79]. T2-01 asks for one evaluated end-to-end system at Tier 0–1, and two systems with different failure surfaces plus CI-gated evaluation at Tier 2–3 [B/C/D · T2-01.F9].
6. **Treat a live demo as optional, replay-first, capped and dated.** Its risks are documented: unbounded spend, leaked keys, sleeping free hardware and paid compute requirements for Gradio/Docker Spaces [A · T0-13.F6, L506; T0-20 L65, L200], plus dead links [C · T0-13.F6]. Its weight against a repository is unmeasured [D · T0-13 L506; E · T0-20 L402].

**Scope.** Whether reviewers open GitHub depends heavily on employer type and role family — routine at OSS, inference, startup and embodied-AI employers, but absent from sampled governance, human-data and FDE postings (see the 71-posting breakdown and role-family skeletons in [Online presence](../07-networking/online-presence.md#when-reviewers-look-employer-type-and-role-family)) [M · T0-20 L58, L69]. Because 58% of surveyed hiring managers use AI to screen résumés [C · T0-20 L78, L228] and keyword screens reward terms like "RAG" [C · T0-13.F1], keep keywords on your résumé and add checkable links [D · T0-13 L160; T0-20 L78]. A portfolio does not replace coding skill, system design or referrals [D · T0-13 L646].

## At a glance

The portfolio's job is to lower a reviewer's cost of verifying competence [D · T0-13 L127]. Every claim sits on one rung of this ladder, and each target level has a minimum rung:

```mermaid
flowchart LR
  V0["V0 Self-asserted: a screenshot or a bare number"] -->|"add one-command reproduction"| V1["V1 Reproducible: one command regenerates the result"]
  V1 -->|"a third party attests"| V2["V2 Externally attested: merged PR, leaderboard row, independent reproduction"]
  V1 -->|"it runs in operation"| V3["V3 Operationally evidenced: 30+ days of uptime and spend logs, a postmortem, real users"]
  V1 -.-> E["T0 new graduate and T1 junior: every headline claim at V1"]
  V3 -.-> M["T2 mid: V1 plus a 30-day demo log"]
  V2 -.-> S["T3 senior: V1 plus at least one V2 item"]
  V2 -.-> P["T4 staff or principal: V2 as the norm, at least one V3 item"]
  V3 -.-> P
```

Four tools sit around the ladder: the anti-portfolio (what to fix or archive), the 15 artefacts (what to ship), the reviewer's five minutes (how a repo is read) and demo hardening (how not to create a liability). T0–T4 on this page are T0-13's experience levels, not the compensation tiers used elsewhere in this repository; see "Two tier scales" below.

## The verifiability ladder and the level model

### The ladder

| Level | Name | Example | Reviewer cost |
|---|---|---|---|
| V0 | Self-asserted | A screenshot; "achieves 95% accuracy" | Cannot verify |
| V1 | Reproducible | One command regenerates `results.json` and the README table; raw data and pinned versions committed; CI run linked | Minutes |
| V2 | Externally attested | Merged upstream PR; leaderboard row with commit hash; independent reproduction; third-party users | Minutes, trusting a third party |
| V3 | Operationally evidenced | 30+ days of uptime and spend logs; an incident postmortem; real users | Minutes to hours |

Source: [D · T0-13 L131–136]. The rules: every headline README claim is V1 or higher; T3 portfolios need at least one V2 item; T4 portfolios need V2 as the norm [D · T0-13 L138]. Once evidence-block formats spread, they can be faked; V2 and V3 cost more to fake, which is why they carry the weight at senior levels [D · T0-13 L644].

### What each level must prove

| Level (T0-13) | Must prove | Archetype that carries signal | Verification target | Reference spec | D9 advance mark |
|---|---|---|---|---|---|
| T0 new graduate or switcher, 0–1 years | You can finish, measure and explain a small system | Measured retrieval or extraction over a non-generic corpus, with baselines and error analysis | V1 | R1: about US$25–30 API spend, no GPU, 4–6 weeks part-time | 60 |
| T1 junior, 1–2 years | You can ship and maintain a small service with tests and CI | The T0 system plus CI-gated evaluation, a capped deployment and one docs or test PR upstream | V1, ceiling V2 | R1 | 60 |
| T2 mid, 3–5 years | Production judgement: reliability, cost, evaluation-gated releases | Evaluation-gated agent or service with a router, tracing, load tests and an incident postmortem | V1 plus V3-lite: a 30+ day demo log | R2: about US$100 for API and hosting, 8–10 weeks | 65 |
| T3 senior, 6–9 years | Depth and trade-off command at system or kernel level | Serving, quantisation or kernel study with rigorous method and an upstream contribution | V1 plus at least one V2 item | R3: about US$300 of rented GPU hours, 6–10 weeks | 70 |
| T4 staff or principal, 10+ years | Leverage: standards, reference implementations, adoption | Methodology or benchmark programme with external adopters and design docs | V2 as the norm, at least one V3 item | R4: about US$500 own spend, the rest via collaborators, 3–6 months | 70 |

Source: [D · T0-13 L262–277], calibrated by T0-13 against an interview framework and employer postings. Spec numbers (question counts, trial counts, budgets) are starting points; change them with a stated reason [D · T0-13 L270].

**Two tier scales.** T2-01's portfolio rule uses compensation tiers (Tier 0 to Tier 5, defined by pay bands), not these experience levels. The band figures differ between sources and none is measured ([errata U7 and U14](../../research/ERRATA.md)), so this page quotes T2-01's rule only in its own terms. Both scales point the same way: depth and outside verification rise together.

**Track and background.** R3 and R4 suit infrastructure and performance roles; applied-AI roles may value R2 more [D · T0-13 L647]. Senior and staff postings from NVIDIA, Inferact (the vLLM creators), Together AI, AMD and River AI ask for upstream PRs, shipped performance features, maintainer relationships and technical writing [B · T0-13.F9]. Evaluation is the gate for every background in T2-01, and each brings a different advantage to it [B · T2-01.F3]; for data scientists the "can't ship" trope is half right, with real gaps in big-company loops and a real advantage in evaluation [C/D · T0-06.F5].

### How many projects

T0-13 rejected breadth: unmeasured small demos read as tool assembly, and extra mildly positive items risk diluting an impression when a profile is judged alone. It recommends 2 to 3 deep repos instead [C · T0-13 L161]. The dilution mechanism is contested: a student thesis reports a failed replication [C/D · T0-13 L605]. T2-01 sets the minimum by target tier [B/C/D · T2-01.F9], and T0-06's milestone spine shows one way to build it, at 15–20 hours a week [M · T0-06 L261, L393–397]; the gates' full criteria are in [career transitions](../11-tracks/career-transitions.md#the-shared-spine-four-gates-and-an-hours-budget):

| Target (T2-01 tier) | Minimum portfolio | How the T0-06 spine builds it |
|---|---|---|
| Tier 0–1 | One evaluated end-to-end system | G1 by month 3: a running application over a real corpus or task from your domain; at least 50 labelled evaluation cases (at least 30 hand-written from real work); at least 2 baselines; an error taxonomy from at least 100 reviewed traces; a "what broke" memo of 500+ words |
| Tier 2–3 | Two systems with different failure surfaces, plus CI-gated evaluation | G2 by month 6: evaluation in CI with a regression threshold; any LLM judge validated on at least 100 human labels; one real user other than you; one regression postmortem. G3 by month 9: a second system (a tool-using agent with approvals and budgets, an on-device or browser module, a domain benchmark or a serving lab), one public write-up with numbers and one external contribution |
| Tier 4–5 | Published research, industry-visible contributions and evidence meeting O-1A or equivalent standards | Beyond the spine: see spec R4 and [visa and relocation](../11-tracks/visa-and-relocation.md) |

**Reconciling them** (this page's judgement, D): one finished, evaluated system is the entry floor; a second with a different failure surface is the mid and senior step; a third repo earns its place only if it adds a new failure surface or a V2 item. Open-source work complements personal repos from T1 and becomes the primary evidence from T3 [D · T0-13 L164]. Competitions count where the target role matches [D · T0-13 L165]. Writing counts when paired with V1 artefacts [D · T0-13 L166]. A training or fine-tuning headline suits only small, scoped, fully evaluated runs [D · T0-13 L163].

## The anti-portfolio: nine patterns and how to redeem them

Each pattern is "disqualifying as presented": a reviewer who sees only it learns nothing they can trust, yet most can be retrofitted [C · T0-13 L175]. The sources support a failure-mode list, not a ban list [C · T0-13.F2], and most red-flag lists are SEO or vendor content that echo one another [C · T0-13 L606, L643].

**Swap test** [D · T0-13 L177]: replace the model call with a stub or a non-AI baseline. If the project looks the same, cannot be tested, or nobody can say what got worse, the model is decoration and the repo is a wrapper.

| # | Pattern | 30-second signal | Why it fails | Redemption |
|---|---|---|---|---|
| AP-1 | "Chat with your PDF": LangChain or LlamaIndex, a vector store, Streamlit (C) | Default chunking; unpinned requirements; screenshot-only README; no tests; one or two commits; no evaluation folder | Library assembly, not judgement: no retrieval baseline, question set or error analysis, and nearly every candidate has one. In the one narrated postmortem, a hiring manager reduced five such demos to "tool assembly" | Rebuild to spec R1: measured retrieval over a non-generic corpus |
| AP-2 | A Streamlit or Gradio wrapper over a hosted LLM API (C; platform facts A) | Under about 150 lines; one chat input and one API call; keys in a committed `.env`; a deployed URL that errors | The system prompt is the whole product. It also carries liabilities: key handling, no rate limit or spend cap, sleeping demos, hosting-policy changes | Add a measurable differentiator (own data plus evaluation, or cost-aware routing) and harden it (H1–H14), or archive |
| AP-3 | Course datasets: MNIST, Titanic, Iris, house prices, tweet sentiment (C) | Tutorial dataset; notebook only; accuracy on a clean split; no baseline discussion | Identical across candidates, so it discriminates nothing; no problem framing or constraint-driven decision | Archive. If kept, reframe it as a calibration exercise, such as a model judge against human labels, never a headline |
| AP-4 | Metric-free multi-agent demos: "AI research team", "autonomous X agent" (B) | Several agent frameworks; role names such as researcher, writer, critic; no tasks file; demo video only; no cost per task | Agent failures compound. Without outcome-based graders, multiple trials and failure-mode discussion, nothing is reproducible | Rebuild to spec R2: state-check graders, pass@1 and pass^k, cost per task |
| AP-5 | Benchmark-number theatre: "98% accuracy", "100% deflection" (B) | A number with no link to a script; labels produced by the model being evaluated; test data used for prompt tuning | No defined test set, split, grader or interval: it shows evaluation illiteracy | PA-01 evidence block, PA-03 dataset card, PA-04 evaluation harness |
| AP-6 | Single-commit, tutorial-fork or AI-one-shot repos (B/C) | One large commit; boilerplate README with emoji headers; no iteration; unchanged tutorial structure and names | Authorship cannot be assumed. The harm is the raised verification cost, not the content | Iterative history; `docs/PROCESS.md` disclosing AI help; the ability to explain any file in an interview |
| AP-7 | Training or fine-tuning claims without baselines, held-out evaluation or cost (C) | No base-model comparison; evaluation on training data; no cost or seed; no loss curves | "Trained an LLM" often means a small LoRA run judged by feel; confusing fine-tuning with pretraining costs credibility | Base versus tuned on a held-out set with intervals, a cost table and an ablation; or a scaled-down run against a public metric |
| AP-8 | Framework-only fluency (C) | Deep chain or agent abstractions; no raw request logs; no trace of the prompt actually sent | The reviewer cannot see what you understood. Using a framework is fine; not knowing what it sends over the wire is not | Show raw requests and responses in traces; implement one component, a retriever or a tool loop, directly and with tests |
| AP-9 | Unsafe or dead public demos (A for the risk; C for the hiring effect) | Keys in history; no rate limit or cap; an error page; a stale last-updated date | Unbounded consumption is an OWASP risk class; GitHub scans public repos for provider keys, so a leaked key is revoked yet stays in history; practitioner content calls a broken link worse than none | A replay-first demo and the H1–H14 checklist |

All rows: T0-13 D1 [T0-13 L179–222], with T0-13's grades in brackets.

## The fifteen artefacts

**Required set by level** [D · T0-13 L142]:

| Level | Required |
|---|---|
| T0–T1 | PA-01 to PA-04 (PA-04 small), PA-07, PA-10 to PA-12; basic PA-05 (a smoke evaluation in CI), PA-06 (a basic latency table) and PA-08 (basic telemetry); PA-09 if any endpoint is live |
| T2 | Full PA-04, PA-05, PA-06, PA-08 and PA-09; adds PA-13 |
| T3 | Adds PA-14 |
| T4 | Adds PA-15 |

**The artefacts** [D · T0-13 L228–244]. Pass criteria are written so a reviewer can check them in minutes; the numeric defaults are starting points, not standards [T0-13 L226].

| ID | Artefact | Where | Pass criteria | From |
|---|---|---|---|---|
| PA-01 | Evidence block | `README.md`, first screen | Claim, metric, method, command, date, commit SHA and hardware for each headline number; each number links to a file in `bench/` or `eval_harness/` | T0 |
| PA-02 | One-command reproduction | `Makefile`, lockfile, `Dockerfile` | `make repro` regenerates tables from raw data; dependencies pinned; model IDs and price-table date recorded; seeds fixed where applicable; run cost stated | T0 |
| PA-03 | Dataset card | `docs/dataset-card.md` | Source, licence, size, splits, labelling protocol and labeller, known gaps, PII handling, checksum; dev and test strictly separated | T0 |
| PA-04 | Evaluation harness | `eval_harness/` | Tasks as data; code graders first; versioned judge prompts; 3+ trials for stochastic tasks; capability and regression suites apart; judge TPR and TNR on 100–200 human-labelled examples per failure mode (updated 2026-09-01, superseding 50+50 [C · T0-20 L63, L196]); error-analysis notes from ~100 coded traces (at least 30 annotated manually first [C · T0-20 L63]) | T0 small, T2 full |
| PA-05 | CI gates | `.github/workflows/` | Each PR runs tests and a cached or capped smoke evaluation; a scheduled full run; fails on regression; uploads artefacts; per-run spend cap; standard hosted GitHub Actions runners are free on public repos (larger runners are paid; self-hosted fee postponed [B · T0-20 L329]); Shields.io endpoint badge linked to the run (cache <300 s ignored [B · T0-20 L330]) | T1 smoke, T2 full |
| PA-06 | Latency and throughput benchmark | `bench/`, `benchmarks.md` | p50, p95, p99; TTFT; ITL or TPOT; tokens per second; error rate; a concurrency or rate sweep; warm and cold apart; hardware, client and engine versions; raw files and plot script; client-saturation check; 3+ repeats with spread | T0 basic, T2 full |
| PA-07 | Cost accounting | `benchmarks.md` or `cost/` | Tokens times a dated price table (URL and date) gives dollars per request and per successful task; infrastructure dollars per hour become dollars per 1k requests; monthly burn of any live demo; budget cap stated | T0 |
| PA-08 | Telemetry | `src/…/telemetry`, `docs/traces/` | Spans carry model ID, tokens in and out, latency, finish reason, retrieval IDs, tool names, error type and cost; sanitised, dated exports committed; at least one failing trace promoted to an evaluation case; content capture off on the public demo; semantic-convention version pinned | T1 basic, T2 full |
| PA-09 | Abuse resistance | `docs/SECURITY.md`, code | Per-IP and per-key rate limits; input and output token caps; timeouts; hard spend cap on a dedicated key; no side-effecting tools on a public demo; secrets only in the platform store; injection tests, including tool-output injection | T1 if live, T2 |
| PA-10 | Architecture and decisions | `docs/architecture.md`, `architecture.svg`, `docs/decisions/` | Data and control flow diagram; at least 3 ADRs, each naming a rejected alternative; a non-AI baseline comparison | T0 |
| PA-11 | Failure analysis | `docs/failure-analysis.md` | Failure taxonomy with counts; negative results; threats to validity; explicit non-claims | T0 |
| PA-12 | Authorship and AI-use disclosure | `docs/PROCESS.md` | What was AI-assisted; what was verified by hand; iterative commit history; licence | T0 |
| PA-13 | Operational evidence | `docs/ops/` | SLOs with thresholds; uptime and spend log of 30+ days; at least one incident postmortem, real or staged; runbook and rollback; a model-swap report | T2 |
| PA-14 | Profiling and systems analysis | `latency_profiling/` | Profiler timelines; roofline or bandwidth analysis; ablation table; correctness tests against a reference for every custom kernel; hardware fingerprint | T3 |
| PA-15 | Design docs and adoption trail | `docs/rfcs/` | RFC with alternatives and threats to validity; external review trail; versioned spec and changelog; independent reproductions; upstream merges | T4 |

**Six cross-cutting rules** [D · T0-13 L246–252]: charts come from committed raw data by a script (hand-edited images are V0); every number has a command that regenerates it; include negative results and non-claims; pin versions and date every benchmark and price table; never commit secrets, and assume history is public; a badge is evidence only if it links to the run or result file that produced it.

**GitHub README, model-card and V2 registration additions (T0-20):**
- **Limitations and evaluation are the real differentiator in documentation.** Across 32,111 Hugging Face model cards (*Nature Machine Intelligence*, 2024), limitations and evaluation were the least-filled sections, and adding detailed cards to 42 models correlated moderately with downloads [B · T0-20 L64, L570–L571]. Link model/dataset cards and add a `CITATION.cff` or citation block (`karpathy/nanochat` and `UKGovernmentBEIS/inspect_ai` exemplars [B · T0-20 L192–L194, L343, L352]). The full 13-element README skeleton and role-family GitHub profile layouts live in [Online presence](../07-networking/online-presence.md#profile-skeletons-by-role-family).
- **Registering a public evaluation is an alternative V2 route.** Where upstream code PRs face maintainer backlogs or PR closures (curl, tldraw, Ladybird, GitHub PR-restrict settings [B/C · T0-20 L66, L230]), publishing an evaluation with an arXiv write-up and registering it through **Inspect Evals** provides an externally listed V2 artefact [B · T0-20 L82, L149, L353].
- **Ignore GitHub vanity metrics.** A 2024 preprint flagged ~4.5M suspected fake stars across 15,835 repos, GitHub bans automated starring/following, and employers discount watcher and fork counts [A/B · T0-20 L60, L136–L139, L566].

## How a reviewer reads a repo

One hiring manager reporting 500+ candidate interviews says a GitHub review takes about 30 seconds and includes spotting AI-generated slop [B/C · T0-13.F8]. T0-13 found no GitHub-profile scoring rubric published by a major lab or employer [E · T0-13 L619]. Its own protocol and rubric are a synthesis with no inter-rater reliability data [D · T0-13 L563]: use them to see your repo as a reviewer might, not as a pass mark.

**The five-minute protocol** [D · T0-13 L591–596]:
1. Minute 1, README first screen: quantified, dated claims with an evidence block?
2. Minute 2, CI: does the badge link to the run that produced it, how old is that run, and does the workflow gate evaluation?
3. Minute 3, `eval_harness/`: dataset card, graders, calibration report, error analysis.
4. Minute 4, `benchmarks.md` and `bench/results/`: hardware, percentiles, repeats, raw data.
5. Minute 5: commit history, `docs/PROCESS.md`, a quick search for key patterns; then advance, probe or pass.

**Hard fails.** Any one caps the outcome at "do not advance on portfolio evidence" [D · T0-13 L584–589]: HF-1, a live secret in the repo or its history; HF-2, a headline metric contradicted by the repo's own raw data, or not reproducible; HF-3, a copied or forked tutorial presented as original; HF-4, a public endpoint with unbounded spend or unauthenticated side-effecting tools; HF-5 (interview stage), you cannot explain core files, or you contradict your own AI-use disclosure.

**Where the weight shifts by level.** Ten dimensions are rated 0 to 3; the score is the sum of weight times rating, divided by 3 [D · T0-13 L565–580]:

| Dimension | T0–T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| D-1 Problem reality; the model is load-bearing | 15 | 10 | 8 | 5 |
| D-2 Evaluation rigour | 20 | 20 | 15 | 15 |
| D-3 Reproducibility and CI | 15 | 12 | 12 | 10 |
| D-4 Performance and cost accounting | 8 | 12 | 20 | 15 |
| D-5 Observability | 5 | 10 | 8 | 5 |
| D-6 Reliability, safety, abuse resistance | 5 | 10 | 7 | 5 |
| D-7 Engineering hygiene and authorship | 15 | 10 | 7 | 5 |
| D-8 Honesty and limitations | 10 | 8 | 8 | 10 |
| D-9 Third-party verifiability | 5 | 5 | 10 | 15 |
| D-10 Level-specific depth and influence | 2 | 3 | 5 | 15 |

The advance marks are arbitrary starting values: 60 for T0–T1, 65 for T2, 70 for T3 and T4. From 50 up to the mark means "advance with verification probes"; below 50 the portfolio is not relied on [D · T0-13 L582]. Evaluation rigour weighs most at T0–T2; performance and cost accounting peaks at T3; at T4, third-party verifiability and influence rise to match evaluation and performance.

**Probes to rehearse** [D · T0-13 L598, L310, L347, L381, L409]:
- Any level: regenerate one README number live; show a failing trace and the case it became; say what changes at 10 times the load; alter a grader and predict the effect.
- R1: a query where dense lost to hybrid, and why; your judge's TPR and TNR and what you did about the misses; what breaks at 100 times the corpus.
- R2: pass^5 against pass@1 and what the gap tells you; which regression case came from a trace; what the router cost in success rate.
- R3: why throughput plateaued, and how you know the client was not the bottleneck; what quantisation cost in quality, with what interval; what changes at tensor-parallel 8.
- R4: who outside your organisation depends on it, and how you know; what a reproduction found you got wrong; what is out of scope, and why.

## Live demos: replay-first, capped, dated

**Rule.** Replay-first, capped and dated; a live path is an optional extra, never the only proof [D · T0-13 L508]. Employers inspect activity traces that are cheap to verify, and a working demo is one [A · T0-13.F6], but that mechanism comes from a 2013, pre-GenAI interview study [T0-13 L605], no source measures a demo's effect on callbacks or offers [E · T0-13 L621], and a demo with no repo leaves the method uninspectable [D · T0-13 L162].

**Hosting by budget, refreshed November 2026.** Re-verify prices monthly before spending; tool verdicts are in the [tool catalog](../00-start/tool-catalog.md).

| Budget | Option | Grade · source |
|---|---|---|
| None | A static Space or static site (GitHub Pages: free up to 1 GB, 100 GB/mo soft cap) serving replays, plus a recorded walkthrough | A/B · T0-13 L527; T0-20 L207 |
| Up to about US$10 a month | Railway Hobby (US$5/month, incl. US$5 usage) or Hugging Face PRO (US$9/month: Gradio/Docker compute Spaces plus 40 min/day ZeroGPU; free ZeroGPU is 5 min/day) | A/B · T0-13 L478, L528; T0-68 L385 |
| Intermittent GPU | Modal Starter (US$0/month with US$30 monthly credit ≈ 7.6 H100-hours at US$3.95/h; T4 US$0.59/h, L4 US$0.80/h, A100 40GB US$2.10/h; academic grants up to US$10,000 by application) or in-stock marketplace GPUs (RTX 3090 US$0.29/h, RTX 4090 US$0.41/h, A100 US$0.68/h, L4 US$0.93/h as of 2026-11-11) | B/C · T0-68 L388–L391 |
| Persistent GPU | Rarely justified for a portfolio; if used, set auto-shutdown (H100 rentals ran US$2.89–4.59/h across RunPod/Lambda in Sept–Nov 2026) | B/D · T0-13 L530; T0-68 L389–L390 |

**Stale advice is itself a tell** [A/B · T0-13.F11; T0-20 L65]:
- Older tutorials say Gradio and Docker Spaces are free. Verified directly from Hugging Face Spaces docs [A · T0-20 L65, L200] (and re-checked 2026-11-19): Gradio and Docker Spaces running on compute need PRO (US$9/month on HF's pages, which also bundles HF profile blog publishing) or Team/Enterprise; static Spaces stay free; free accounts in good standing can host up to 2 ZeroGPU Spaces (Gradio SDK); free CPU hardware sleeps after idle periods [A · T0-13 L476; T0-20 L200]. Static replay sites on GitHub Pages are free for public repos up to 1 GB (soft 100 GB/month, no commercial/SaaS use [B · T0-20 L207]). Replicate completed joining Cloudflare on 2025-12-01 [B · T0-20 L327]. A paid T4 small Space left on for 30 days costs about US$288 (derived) [D · T0-13 L476].
- An OpenAI monthly limit without the "Enforce a hard limit" toggle only sends alerts, and enforcement is not instantaneous. Anthropic sets no limits on the Default Workspace, so create a named workspace per demo [A · T0-13 L497–498].
- Free tracing tiers expire data: Langfuse Hobby keeps 30 days (50k units a month); LangSmith's free plan caps at 5,000 base traces a month with 14-day base retention. Commit sanitised, dated trace exports and the script that recomputes p95 and cost from them [B · T0-13.F7].
- All OpenTelemetry `gen_ai.*` attributes were at Development status in mid-September 2026; pin the semantic-convention version [B · T0-13.F7].

## Systems depth on a modest budget

Buy verifiability, not hardware: measured small-scale results with disclosed hardware, external leaderboards or open challenges, and upstream PRs, with simulated or modelled results labelled as such [D · T0-13 L146]. This works if scoped honestly; educational engines and simulators do not support production or hardware claims [B · T0-13.F10]. Most GenAI application work needs no GPU [A/B · T0-06.F12].

| # | Strategy | How, on a modest budget | Ceiling | Does not prove |
|---|---|---|---|---|
| M1 | Validated memory and throughput model | Predict per-GPU memory and throughput with the Ultra-Scale Playbook's parallelism arithmetic; check it against 1-GPU measurements | V1 | Cluster operations |
| M2 | CPU/gloo smoke tests | Launch several CPU processes to verify DDP or FSDP2 sharding, checkpoint and resume | V1 | Performance, NCCL, topology |
| M3 | Scaled-down single-GPU runs | nanochat's roughly 5-minute small-model scale and scaling-law scripts; report MFU and tokens per second | V1 | Multi-node scaling |
| M4 | Leaderboards and open challenges | AMD x GPU MODE kernel competitions on organiser hardware; Anthropic's public take-home, which runs in a Python simulator with no GPU | V2 | Ability beyond the task |
| M5 | Compact reimplementation | A nano-vLLM-style engine (continuous batching, paged KV, prefix caching) in 1k to 2k lines, benchmarked against vLLM on the same hardware and configuration | V1 | Production readiness or general superiority |
| M6 | Simulation and harness engineering | Validate load harnesses against the llm-d inference simulator; label any scheduling simulator and calibrate it on small real runs | V1 | Hardware performance |
| M7 | Upstream contributions | Tests, benchmarks, bug fixes or docs to vLLM, SGLang, Triton or similar | V2 | Authorship of core design |
| M8 | One short rented multi-GPU session | A single measured 2- to 4-GPU tensor-parallel experiment with a cost log: 4 GPUs for 3 hours at about US$3.95 an hour is about US$47 (derived) | V1 | Sustained operations |

Source: [T0-13 L545–554]. **GPU arithmetic for spec R3** (reconciled with November 2026 rates [B/C · T0-68 L388–L391]): Modal H100 at US$3.95/h (40 GPU-hours ≈ US$158; A100 40 GB US$2.10/h; T4 US$0.59/h); RunPod Secure Cloud H100 PCIe US$2.89/h / SXM US$3.99/h / A100 PCIe US$1.79/h (2026-10-15); Lambda H100 SXM US$3.99–4.59/h (Sept–Nov 2026); cheapest in-stock marketplace consumer GPUs RTX 3090 US$0.29/h, RTX 4090 US$0.41/h and A100 US$0.68/h (2026-11-11).

**Claim language** [D · T0-13 L556–559]:
- "Measured on 1x [GPU] ([VRAM]): [metric]. Modelled for 8x [GPU] under assumptions A, B, C: [metric] (not measured)."
- "Simulated with the llm-d inference simulator: validates the load harness only."
- "Educational reimplementation; one configuration; not a production claim."

## Open-source contribution economics and employer-domain repo map (T0-05)

**Debunking "10× recruiter inbound per merged PR vs 500 Easy Applies" (`T0-05.F1`):** no measurement supports this claim, and the ratio is ill-posed [C · T0-05 L46, L147]. Recruiter *inbound contacts* are not an output of Easy Apply (making the denominator ≈ 0); against Ashby's all-role baseline (3% application→interview, 0.2% application→offer), 10× would imply ~150 inbound contacts from one PR; authors merging into vLLM-class repos are heavily confounded (many already work at AMD/NVIDIA/Intel/Red Hat); and GitHub's Acceptable Use Policy §7 bars scraping GitHub metadata for unsolicited recruiter emails [A · T0-05 L147]. What *is* supported: sustained, non-trivial contributions build discoverability and move you from cold inbound toward sourced or referred status [B/C · T0-05 L48, L147].

**Academic signalling context (`T0-05 D2.6`):** an ifo 2024 working paper (~22,900 GitHub developers) finds job movers raise OSS activity by ~16% during job search (so casual PR signalling is crowded), while Hann, Roberts & Slaughter (*ISR*, 2013; Apache six-year cohort) find up to an 18% wage lift attaching to **earned meritocracy rank**, not raw commit volume [B · T0-05 L232].

**Employer-domain commit map and hard gates across eight AI repos (12-month default-branch commits, retrieved 2026-10-21 [A/C · T0-05 L50–L56, L157–L186]):**

| Repository | Top 12-month corporate domains (distinct authors / commits; lower bounds) | Personal→corp transitions | 1-commit share / top-10 share | Hard gates & hiring reality |
|---|---|---|---|---|
| **vLLM** (`vllm-project`) | `amd.com` 149/1,225 · `nvidia.com` 81/336 · `intel.com` 65/586 · `redhat.com` 38/628 · `ibm.com` 30/200 · `meta.com` 25/186 · `inferact.ai` 11/273 | 30 (15 in 2026; median 216 d) | 58.9% / 19.0% | DCO + AI disclosure; pure code-agent PRs banned (auto-ban risk); no typo PRs; committers ~30+ PRs & ~10+ reviews; Inferact MTS lists vLLM contributions as preferred/bonus [A/B] |
| **SGLang** (`sgl-project`) | `amd.com` 79/760 · `nvidia.com` 47/273 · `intel.com` 45/292 · `thinkingmachines.ai` 14/100 · `radixark.ai` 4/202 | 12 (median 180 d) | 50.2% / 32.3% | Only trusted contributors trigger CI (`CI_PERMISSIONS.json`, `run-ci`); RadixArk AI Infra Resident ($200K listed on Accel, undated on Greenhouse) and DevTech MTS reference SGLang [A/B] |
| **llama.cpp** (`ggml-org`) | `qualcomm.com` 20/262 · `nvidia.com` 15/257 · `intel.com` 12/60 · `huggingface.co` 5/619 · `redhat.com` 6/77 | 8 (median 349 d) | 64.0% / 42.1% | Max 1 open PR for newcomers; issue-first for features; undisclosed AI = permanent ban; Red Hat llama.cpp role required major OSS record [A/B] |
| **transformers** (Hugging Face) | `intel.com` 12/274 · `huggingface.co` 8/422 (lower bound; noreply common) · `nvidia.com` 8/9 | 19 (2020–26) | 68.2% / 42.6% | First-timers asked not to use code agents (closed without review); only 2.5% of newcomers reach 10 commits; HF Open-Source MLE requires public merged PRs [A/B] |
| **LiteLLM** (`BerriAI`) | `berri.ai` 29/8,698 (core-dominated); 1–4 each at Stripe, Amazon, Anthropic, CoreWeave | 4 | 57.4% / 63.5% | CLA mandatory + **≥1 test hard gate**; onsite includes live repo issue fix; PyPI 1.82.7/1.82.8 compromised 2026-03-24 (pin & verify) [A/B] |
| **Langfuse** (ClickHouse) | `langfuse.com` 6/853 · `clickhouse.com` 7/427 (core-dominated) | 1 | 67.5% / 79.2% | Issue-first for major changes; low external retention — pair with direct outreach or own-instance parity audit [A/C] |
| **Axolotl** (`axolotl-ai-cloud`) | `axolotl.ai` 2/401 (core-dominated) | 2 | 67.7% / 86.6% | Explicit anti-farming policy (`AGENTS.md` tells agents to refuse profile-padding PRs) [A] |
| **Ollama** (`ollama`) | `ollama.com` 6/260 (core-dominated) | 0 | **81.2% / 83.4%** | Lowest newcomer retention (0.9% active at 6 mo); use for an own-instance audit artefact rather than a contributor pipeline [A/C] |

**Platform anti-slop controls and stop rules:** GitHub added open-PR caps for non-write users on `2026-06-17` alongside PR/issue restriction settings, and Hacktoberfest 2026 dropped PR-count rewards [A · T0-05 L52]. Target work agents cannot do alone (bisected regressions, minimal reproducers, regression tests, hardware comparisons), aim for **3+ merged/in-review PRs and 5+ reviews/triage actions in one area** before headlining OSS, and apply a hard stop-loss at **Week 8** (no merged PR and no substantive maintainer exchange → reallocate) [A/D · T0-05 L191–L209].

## Public technical micro-audit operating system (T0-05)

A micro-audit is a ≤2-page, reproducible technical measurement note sent privately to an engineering owner — or published as a vendor-neutral **category-level benchmark** (archetype [P21](project-archetypes.md)).

### Break-even effort economics (Grade D, modelled [T0-05 L66, L515–L520])

No unconventional tactic shows a 10× per-hour edge over standard applications across pessimistic, base or optimistic scenarios; the case rests on **channel saturation** (mass Easy Apply exhausts a ~300-opening pool in ~15–30 hours) and **reusability** [D · T0-05 L506–L519]:

- **Outreach vs tailored applications:** artifact-carrying outreach (~0.27 base offers/100 h) beats tailored applications (~0.45 base offers/100 h) only where inbound `P(offer)` falls below **~0.089%** (<45% of Ashby's 0.2% all-role baseline) [D · T0-05 L517].
- **100-hour OSS sprint:** inside a 400-hour search year, a 100-hour OSS sprint must lift the effectiveness of the remaining 300 outreach hours by **≥32%** (e.g. reply rate 5% → 6.6%) to break even, with ~8–16 weeks calendar merge lag [D · T0-05 L518].
- **12-hour company-specific vs category-level micro-audit:** a 12-hour single-company audit needs a **~17×** lift on that company's offer probability (0.20% → 3.4%) to pay back at base, whereas a **12-hour category-level audit amortised across 20 target employers** needs only **~1.8×** (0.20% → 0.36%) [D · T0-05 L519]. **Rule:** publish category-level benchmarks openly; reserve private company-specific notes strictly for top-priority targets.

### Legal and terms-of-service envelope (pointer, NOT legal advice [A/B/C · T0-05 L249–L257])

> **Not legal advice.** Jurisdiction, contract terms and exact testing methods govern liability; consult qualified counsel before testing any third-party system outside explicit scope.

| Zone | Allowed / prohibited actions | Documented legal & policy basis |
|---|---|---|
| **Green (default)** | Measure *public, documented* API behaviour on your own account at normal rates within usage policies (latency, cost, rate-limit behaviour); audit open-source components on **your own hardware** (`vLLM`, `SGLang`, `Ollama`, `LiteLLM`, `Langfuse`); review public docs, changelogs, model cards and public repos | No unauthorised access; no safeguard circumvention [A/D · T0-05 L253] |
| **Amber (explicit written scope only — otherwise stop)** | Jailbreak, prompt-injection or system-prompt-leak probing of *production* AI endpoints; high-volume automated extraction; undocumented host discovery; touching other users' data | OpenAI Usage Policies (`2025-10-29`) bar unsolicited safety testing and safeguard circumvention; OpenAI EU Terms (`2026-01-16`) bar reverse engineering and automated extraction; Anthropic's disclosure safe harbour **excludes** "red-teaming or adversarial testing of models" and its Model Safety Bug Bounty (`2026-09-08`) is invite-only under NDA with no explicit safe harbour [A · T0-05 L254] |
| **Red (never)** | Using discovered credentials/keys ("even to verify they work"); accessing non-public systems; bypassing authentication or rate limits; exfiltrating data; service-degrading load; publishing a vulnerability before vendor notice; extortionate disclosure leverage | US DOJ May 2022 CFAA policy covers *only* "solely good-faith" research (and WSGR notes it gives no concrete civil protection); post-*Van Buren* civil/contract exposure remains [A/B · T0-05 L255]. **India:** IT Act s.43 penalises unauthorised access without distinguishing ethical researchers; CERT-In disclosure policy (`2021-09-03`) Clause 7 requires compliance with all extant laws; the 2021 Mobikwik legal-threat case is a documented cautionary tale (advocacy source, 2021; may be dated) [B/C · T0-05 L257] |

**Disclosure hygiene:** fetch `/.well-known/security.txt` (RFC 9116: check `Contact`, `Policy` and the `Hiring` field for security roles [A · T0-05 L257]); report vulnerabilities privately first and treat Google Project Zero's **90 days (+30 if patched)** as an industry reference norm, not a legal right (Anthropic forbids public disclosure without prior written notice) [A/B · T0-05 L257, L316].

### Five reproducible measurement recipes (`T0-05 L263–L278`)

1. **Serving latency & goodput profile (`vllm bench serve`):** fix an `(input, output)` length grid (e.g. `128/128`, `1024/256`, `4096/512`), warm up and discard initial calls, run ≥200 requests per concurrency (`1, 4, 16, 32`) across two times of day, control prefix caching/autoscaling, and report mean/median/P99 for TTFT, TPOT, ITL, E2EL and SLO goodput with raw CSV [B/D · T0-05 L263–L270].
2. **Passive leak & default-config audit:** scan public repos/packages for committed secrets (if a live-looking key appears, **never test or validate it** — report privately); on own-instance OSS builds check unauthenticated admin ports, default binds and permissive CORS [D · T0-05 L272].
3. **Own-instance OWASP prompt-injection audit:** run strictly on your own app, self-hosted OSS or explicitly in-scope targets, mapping direct/indirect injection, Markdown-image/allow-listed exfiltration and excessive agency against OWASP GenAI LLM Top 10 2026 (`T0-68 L606`) and Agentic Top 10 [B/D · T0-05 L274].
4. **Public cost/quality audit:** compare measured token counts against provider billing, cache-hit rates, structured-output failure rates and retrieval recall on a public documented corpus [D · T0-05 L276].
5. **Own-instance gateway/observability parity audit (cleanest OSS bridge):** run `LiteLLM` or `Langfuse` locally, compare traced token/cost accounting against provider usage responses on a fixed prompt set, document mismatches and open a PR with tests [D · T0-05 L278].

### 100-point micro-audit execution rubric and 9 auto-dismissal triggers (`D · T0-05 L297–L311`)

Pass requires **≥75 / 100 AND clearing the Safety & legal gate** (any Red-zone action is an automatic fail):

| Criterion | Points | Full marks |
|---|:---:|---|
| Relevance to the team's public roadmap, issues or JD | 20 | Solves a named team bottleneck, not a generic critique |
| Measurement validity & reproducibility | 20 | Fixed inputs, warm-up, percentiles, N stated, confounders controlled, one-command repro, raw CSV |
| Claim calibration | 15 | Uses claim-hygiene phrasing ("In my setup, X was observed"; "I could not verify…"; "This may reflect a configuration I cannot see"; "I will re-run on [version]") |
| Actionability | 15 | 2–3 ranked fixes with effort/impact and patch offer |
| **Safety & legal (hard gate)** | **15** | Green zone only; explicit scope statement; zero PII/credentials; private disclosure for vulnerabilities |
| Concision | 10 | ≤2 pages, TL;DR first |
| Credibility | 5 | Two-line bio, consistent handle, zero hype |

**Nine automatic dismissal triggers (any one fails the note [D · T0-05 L309]):** (1) a factual error about the target; (2) unreproducible numbers; (3) any method violating target terms; (4) a "gotcha" or shaming tone; (5) publishing a vulnerability before vendor notice; (6) unverified AI-generated claims; (7) exceeding three pages; (8) no concrete next step; (9) missing disclosure/scope statement.

## How to do it

1. **Fix the target.** Name your level (T0–T4), your track (application or infrastructure) and the matching spec (R1–R4). Use the [targeting workbook](../00-start/targeting-workbook.md) and your role's hub. *Done when* you can state the spec, its verification target and its time box.
2. **Audit what is public.** Put every public repo through this flow [D · T0-13 L140, L177, L187, L192]. *Done when* each repo is labelled archive, retrofit or keep.

```mermaid
flowchart TD
  R["A public repo"] --> F{"Unmodified tutorial fork, course-dataset notebook or single commit?"}
  F -->|"Yes"| A["Archive it. Keep a course-dataset notebook only as a calibration exercise, never as a headline"]
  F -->|"No"| S{"Swap test: replace the model call with a stub or a non-AI baseline. Can anyone say what got worse?"}
  S -->|"No"| W["Wrapper: add own data plus evaluation, or cost-aware routing, and harden it; otherwise archive"]
  S -->|"Yes"| V{"Are its headline claims V1 or better?"}
  V -->|"No"| U["Retrofit: dataset card, baselines, error analysis, CI-gated evaluation, cost and latency table, telemetry exports"]
  V -->|"Yes"| K["Keep. Feature it if it fits your target spec"]
```

3. **Build the evaluation core first.** Start small, from real failures [A · T0-13.F4]. Spec R1 asks for at least 50 author-written questions with gold answer spans and source IDs, at least 10 unanswerable ones, and a dev and test split fixed before tuning [D · T0-13 L298]. *Done when* a reviewer can find, in order: the failure taxonomy behind the cases; the cases; the graders, marked code-based or model-based; the judge prompt, its version and its TPR and TNR against human labels; trial counts and the pass@k versus pass^k choice; the regression suite in CI; and a note on one evaluation bug you found and fixed [D · T0-13 L254].
4. **Measure speed and cost, and show the method.** Spec R1 reports p50 and p95 for three configurations at concurrency 1, 4 and 8, cold and warm apart, with hardware and client stated [D · T0-13 L303]. Keep them apart because first runs distort: one tool report shows 2,484 ms first-run against about 73 ms steady-state TTFT. Check that k6 thresholds (exit code 99) fail when they should [B · T0-13.F5]. *Done when* PA-06 (basic) and PA-07 pass.
5. **Instrument and close the loop.** Log latency, tokens and document IDs; commit five sanitised traces; link one failing trace to an evaluation case [D · T0-13 L304]. *Done when* a reviewer can open a trace and find its case (T0–T1), recompute p95 and cost from exported traces and match the README (T2), or read a client-versus-server timing reconciliation (T3) [D · T0-13 L536–538].
6. **Write it up honestly.** Fill in the evidence block, the failure analysis and `PROCESS.md` below. *Done when* every headline number is V1 or better and links to the file that produced it [D · T0-13 L230].
7. **Decide on a demo.** Default to replay. *Done when* you ship replay-only, or all of H1–H14 pass.
8. **Add outside proof from T1 up.** *Done when* one V2 item (a merged PR with maintainer review, a leaderboard row with a commit hash, an independent reproduction) is linked from your evidence block [D · T0-13 L135].
9. **Run the stranger test.** *Done when* someone else reproduces your headline evaluation numbers from the README in under 30 minutes [M · T0-06 L395] and the five-minute protocol finds no hard fail.
10. **Keep it fresh.** *Done when* tool and model versions are pinned, every benchmark and price table is dated, the smoke evaluation re-runs on a schedule and the README shows a "last verified" date [D · T0-13 L150, L520].

**If it is not working** [D · T0-06 L401–404]: G1 not met by month 4 at 15–20 hours a week means checking adherence first, then scope creep and a missing evaluation set, and extending the timeline before adding hours. No screens after 15 targeted applications points to positioning or résumé signal, not skill: get a practitioner to review the artefacts and the résumé. Three failed take-homes call for work on evaluation design and error analysis. The other slip rules are in [career transitions](../11-tracks/career-transitions.md#the-shared-spine-four-gates-and-an-hours-budget).

## Templates and examples

### README evidence block

T0-13's template, with every value a placeholder [D · T0-13 L458–468]. Put it on the first screen. The closing line follows T0-13's README layout and H10 [D · T0-13 L421, L520].

```markdown
## Evidence (generated [YYYY-MM-DD] from commit [sha])
| Claim | Metric | Method | Reproduce | Hardware / env | Level |
|---|---|---|---|---|---|
| [Hybrid retrieval beats dense on my test split] | recall@5 [x] vs [y] (95% CI [a–b]) | [N]-question test split, author-labelled | `make eval-full` (about [N] min, about $[N]) | API only | V1 |
| [p95 latency at 8 concurrent] | [N] ms (cold [N] ms) | k6, 5 min, 3 repeats | `make bench` | client [spec]; server [spec] | V1 |
| Cost per successful task | $[N] | price table dated [YYYY-MM-DD] ([URL]) | `make cost` | n/a | V1 |
| [Upstream fix merged] | [PR link] | maintainer review | [link] | n/a | V2 |

Limitations and non-claims: docs/failure-analysis.md. AI use: docs/PROCESS.md. Demo last verified: [YYYY-MM-DD].
```

### Weak and strong claims

The wording is [P]; the criteria come from T0-13 [T0-13 L133, L212, L230, L235–236, L334, L557].

| Claim | Weak: V0 | Strong: V1 or better |
|---|---|---|
| Quality | "Achieves 95% accuracy." | "Hybrid retrieval: recall@5 [x] vs [y] for dense (95% CI [a–b]) on a [N]-question test split fixed before tuning; `make eval-full`; commit [sha], [date]." |
| Latency | "Fast and production-ready." | "p95 [N] ms at 8 concurrent, warm; cold [N] ms; k6, 5 min, 3 repeats; client [spec], server [spec]." |
| Cost | "Cheap to run." | "$[N] per successful task from a price table dated [date] ([URL]); demo capped at $[N] a month." |
| Agent | "Autonomous research agent", with a demo video | "pass@1 [x] and pass^5 [y] over [N] tasks × 5 trials, end state checked in code; $[N] per task; failure modes in docs/failure-analysis.md." |
| Fine-tuning | "Fine-tuned an LLM; answers are much better." | "Base vs tuned on [N] held-out examples: [metric] [x] vs [y] (CI [a–b]); cost $[N]; seed [s]; ablation in [file]." |
| Scale | "Scales to 8 GPUs." | "Measured on 1x [GPU] ([VRAM]): [metric]. Modelled for 8x [GPU] under assumptions A, B, C: [metric] (not measured)." |
| Open source | "vLLM contributor." | "Merged PR [link] adding [a benchmark script, test or fix], reviewed by maintainers (V2)." |

### Failure post-mortem

Assembled here [P] from PA-11 and PA-13 [D · T0-13 L240, L242], T0-06's G1 "what broke" memo and G2 regression postmortem [M · T0-06 L395–396], and T0-13's eval-bug note [D · T0-13 L254]. Save it as `docs/failure-analysis.md`; keep incident postmortems in `docs/ops/`.

```markdown
# Failure analysis: [system] (as of [YYYY-MM-DD], commit [sha])

## 1. Failure taxonomy (PA-11)
Traces read and coded: [N] (G1 asks for at least 100).
| Failure class | Count | Example trace | Evaluation case it became |
|---|---|---|---|
| [class] | [n] | docs/traces/[file] | eval_harness/tasks/regression/[id] |

## 2. What broke: three specific failures (G1 memo, 500+ words in all)
### [Failure 1, in one line]
- Input, expected, observed: [...]
- Root cause, and the evidence for it: [...]
- Fix and effect, on dev and on the untouched test split: [before] → [after]
- Regression case that catches a repeat: [case id]

## 3. Incident postmortem: [title] (PA-13; say whether real or staged)
- Detected by: [alert, monitor or user report] at [time]
- Impact: [requests, users, spend, SLO breached]
- Timeline: [detection] → [mitigation] → [resolution]
- Root cause: [...]
- Rollback and runbook step used: [link]
- Test that prevents a repeat (G2): [case id], [CI run link]

## 4. An evaluation bug I found
- [grader or judge bug]; headline score [before] → [after]

## 5. Negative results
- [what did not help, with numbers]

## 6. Threats to validity
- [test-set size; author as labeller; one model version; price-table date]

## 7. Non-claims
- This does not show [scale / production readiness / multi-node behaviour].
```

### AI-use disclosure

PA-12 asks what was AI-assisted, what was verified by hand, an iterative history and a licence [D · T0-13 L241]. Anthropic's candidate guidance asks for own first drafts and AI-free take-homes unless stated [B/C · T0-13.F8], so follow each employer's rules for application work. Template [P]:

```markdown
# Process and AI use: [repo] (as of [YYYY-MM-DD])
- AI-assisted: [files or tasks], with [tool and model version]
- Written without AI: [files or tasks, for example evaluation labels and failure analysis]
- Verified by hand: [what you checked and how: tests run, traces read, labels audited]
- History: iterative commits; decisions in docs/decisions/
- Licence: [licence]
```

### Two-page micro-audit template (`D · T0-05 L282–L295`)

Keep company-specific notes private for engineering-lead outreach; publish only vendor-neutral category benchmarks openly:

```markdown
# [Target or Category] — [aspect] micro-audit, v1 ([YYYY-MM-DD])
**Scope and ethics.** What I tested / did not test; own account or own-instance OSS; documented endpoints; request volume; zero PII; zero circumvention; nothing non-public.
**TL;DR** (<=3 bullets, each tagged observed / likely / unknown).
**Setup.** Model/version, region, client, concurrency levels, input/output lengths, warm-up, repeats, date/time window, caching/autoscaling notes.
**Results.** One table + one chart: mean / median / P99 (TTFT, TPOT, ITL, E2EL), N per cell.
**Interpretation and limits.** What this does NOT show; internals not observable from outside.
**Suggested fixes.** 2–3 ranked by effort and impact; "I can send a patch for #1."
**Reproduce.** Repo link, commit SHA, one command, raw CSV.
**Disclosure status.** Private notice date; response; planned public date (category-level only).
**About me.** Two lines and three links (PRs, write-ups, profile).
```

## Checklist

**Before you share a repo link**
- [ ] Every headline number is V1 or better: a command regenerates it and it links to a file in `bench/` or `eval_harness/` (PA-01, PA-02).
- [ ] The dataset card names source, licence, splits and labeller, and dev and test never mix (PA-03).
- [ ] The evaluation harness has code graders first, a judge calibrated with TPR and TNR on 100–200 human labels per failure mode (after manually annotating 30+ of ~100 traces), and at least 3 trials where outputs vary (PA-04 [C · T0-20 L63, L196]).
- [ ] A smoke evaluation runs in CI under a spend cap, and the badge links to the run that produced it (PA-05).
- [ ] Latency shows p50 and p95, warm and cold apart, with hardware and client stated; cost comes from a dated price table (PA-06, PA-07).
- [ ] At least one failing trace became an evaluation case; sanitised, dated exports are committed (PA-08).
- [ ] An architecture diagram, at least 3 ADRs naming a rejected alternative, and a non-AI baseline (PA-10).
- [ ] A failure analysis with counts, negative results, threats to validity and non-claims (PA-11).
- [ ] `docs/PROCESS.md` discloses AI use; the history is iterative; you can explain every core file (PA-12, HF-5).
- [ ] The swap test shows the model is load-bearing.
- [ ] No hard fail: no secret in history, no headline number contradicted by raw data, no tutorial passed off as original, no unbounded public endpoint (HF-1 to HF-4).
- [ ] A stranger reproduces the headline evaluation numbers in under 30 minutes (G1).
- [ ] Versions pinned, results dated, a "last verified" date on the README.
- [ ] Level extras: PA-13 at T2; PA-14 and a V2 item at T3; PA-15 and V2 as the norm at T4.

**Public demo hardening (H1–H14)** [D · T0-13 L511–524]
- [ ] H1. Replay mode by default, serving pre-computed outputs from the evaluation set; live calls only through a rate-limited or bring-your-own-key path.
- [ ] H2. A dedicated provider project or workspace with a hard monthly cap and alert thresholds: OpenAI's hard-limit toggle on; an Anthropic workspace limit below the organisation limit.
- [ ] H3. Per-IP and global rate limits, plus an application-level daily budget counter, because provider caps are not instantaneous.
- [ ] H4. Caps on input length and output tokens; timeouts; a concurrency limit.
- [ ] H5. No side-effecting tools in public mode; read-only sandbox data.
- [ ] H6. Secrets only in the platform secret store; secret scanning on; any exposed key rotated; history assumed public.
- [ ] H7. Telemetry content capture off in public mode; inputs redacted.
- [ ] H8. Direct and indirect (tool-output or document) injection tests in CI.
- [ ] H9. A kill switch that forces replay-only.
- [ ] H10. An uptime monitor and a "last verified" date in the README.
- [ ] H11. A visible budget meter: "demo spend this month: $[x] of $[y]".
- [ ] H12. An abuse contact and takedown path in `SECURITY.md`.
- [ ] H13. Cold-start and sleep behaviour documented.
- [ ] H14. A retirement plan: "demo retired on [date]; replay and traces remain".

## Pitfalls

| Red flag | Why it hurts | Fix |
|---|---|---|
| Five shallow demos instead of one measured system | Unmeasured breadth reads as tool assembly [C · T0-13 L161] | Keep 2 to 3 deep repos; archive the rest |
| Tuning prompts or retrieval on the test split | It contaminates every headline number [D · T0-13 L312] | Fix the dev and test split before tuning; report on the untouched test split |
| An uncalibrated LLM judge grading its own generator | Judges show position, verbosity, self-enhancement and anchoring bias [A · T0-13.F4] | Code graders first; check the judge against human labels; report TPR and TNR |
| Reporting pass@1 or means only | It hides inconsistency across trials and tail latency [D · T0-13 L349, L383] | Report pass^k with intervals, and percentiles with spread over repeats |
| A single-process load client at high concurrency | It can inflate TTFT and TPOT, so the plateau may be the client's [B · T0-13.F5] | Use a multi-process client; record client CPU headroom |
| Educational engines or simulator runs shown as production evidence | They do not support production or hardware claims [B · T0-13.F10] | Use the claim language above and state each result's ceiling |
| A trivial upstream PR made for the résumé | One merged contribution is the modal outcome, so it is weak alone [A · T0-05.F3]; curl ended its bug bounty, tldraw and Ladybird closed external PRs, and GitHub added PR-restrict settings [A · T0-05.F4; B/C · T0-20 L66, L230] | Pre-discuss an issue tied to your own evidence, or register an evaluation via Inspect Evals [B · T0-20 L82, L353] |
| Stale instructions ("deploy a free Gradio Space") or undated results | A visible tell [D · T0-13 L150; A/B · T0-13.F11] | Pin versions; date benchmarks and price tables; re-run the smoke evaluation on a schedule |
| Committed traces or datasets with personal data or restrictive licences | They can leak data [D · T0-13 L648] | Review before publishing; keep content capture off; record licence and PII handling in the dataset card |
| Treating the portfolio as the whole search | Hiring also turns on coding skill, system design and referrals [D · T0-13 L646] | Pair the build with interview preparation and referrals |

## Evidence and limits

- **Measured.** Demand for evaluation skills is common, not universal: 59.7% of AI-first roles in a 6,964-posting analysis, 68% of 198 companies in another, 56% of 390 AI-engineer postings in a 2026 summary [C · T0-20 L63, L363], and 12 of a 100-posting sample; definitions and samples differ [B · T0-13.F3]. RAG appears in 26–40% of AI-engineer postings across four 2026 analyses (15.4% in ML-engineer postings) [B · T0-13 L91; C · T0-20 L72, L362]. Limitations and evaluation are the least-filled sections across 32,111 Hugging Face model cards [B · T0-20 L64]. Platform, licence and price facts are graded A or B as of 2026-10-21 (T0-13) and 2026-11-13 (T0-20, key hosting/policy/eval rules live-verified 2026-11-19) [T0-13 L476–498; T0-20 L322–L336].
- **Searched, not found.** No controlled study or résumé audit shows that generic repos hurt more than no GitHub, so that premise stays unverified [E · T0-13 L617; C · T0-13.F1]. No traceable origin for "87% of tech recruiters review GitHub" [E · T0-20 L399]. No measured effect of a live demo on callbacks or offers [E · T0-13 L621; T0-20 L402]. No published GitHub-profile rubric from a major lab or employer [E · T0-13 L619]. No empirical source calibrates proof requirements by level [C · T0-20 L372]. No source links portfolio quality to hiring outcomes [D · T0-13 L604], and no longitudinal outcome data exists for any transition corridor, so every timeline here is a model [D · T2-01.F10].
- **Read-depth and COI caveats.** T0-20 opened only 3 of its 66 sources in full (5%: Marlow & Dabbish 2013, HF Spaces docs, Anthropic FDE posting); the other 63 rest on search extracts capped at B or lower [T0-20 L22]. Both T0-13 and T0-20 disclose Anthropic COI because Anthropic models authored them and Anthropic engineering/evaluation sources are cited; independent sources (e.g. Husain & Shankar, Liang et al.) corroborate the core evaluation and documentation practices [T0-13 L649, L663; T0-20 L13].
- **Judgement.** The level model, specs R1–R4, artefact list, rubric weights and marks, swap test and hardening checklist are T0-13's synthesis [D · T0-13 L24, L260, L563]. T0-06's milestones are author-designed [M · T0-06 L391]. T0-13 advises that three reviewers score the same ten public repos before anyone adopts the rubric [D · T0-13 L600].
- **Source quality.** Negative-signal content is mostly SEO or vendor material that echoes itself [C · T0-13 L606, L643], and gotcha screens decay fast: a May 2026 hiring guide told reviewers to treat "Sonnet 5" experience as fabricated, and Claude Sonnet 5 shipped on 2026-06-30 [B · T0-13.F12]. T0-13 discloses that three of its primary sources are Anthropic's and that an Anthropic model wrote it; independent sources corroborate the same evaluation practices [T0-13 L649, L663].
- **Scope.** The advice applies when a reviewer opens the repo. T0-13 did not filter its sources by region, so there are no geography-specific findings [T0-13 L638]. Unpaid build time is a barrier, which is why R1 is sized for part-time work [D · T0-13 L650]; hours, not compute, are the binding constraint [A · T0-06.F10].
- **What would change the advice.** A blinded reviewer experiment or matched-résumé audit on generic repos [T0-13 L632]; data on how often hiring managers open GitHub, by company size, role and region [T0-13 L633]; a measure of a demo's weight against a repo [T0-13 L634]; a validated rubric [T0-13 L635]; stable OpenTelemetry GenAI conventions [T0-13 L637].

## Next steps

- **Choose what to build:** [project archetypes](project-archetypes.md), the [skills radar](../03-skills-and-tech/skills-radar.md) and the [learning roadmaps](../03-skills-and-tech/learning-roadmaps.md).
- **Put the evidence where screens see it:** [résumé strategy](../06-job-search/resume-strategy.md), [résumé skills matrix](../06-job-search/resume-skills-matrix.md), [ATS mechanics](../06-job-search/ats-mechanics.md), and the job-search strategy's [constraints that bind first](../06-job-search/job-search-strategy.md#the-constraints-that-bind-first).
- **Make it visible:** [online presence](../07-networking/online-presence.md), [LinkedIn guide](../07-networking/linkedin-guide.md) and [referrals and outreach](../07-networking/referrals-and-outreach.md).
- **Defend it in interviews:** [interview loops](../08-interviewing/interview-loops.md), [system-design archetypes](../08-interviewing/system-design-archetypes.md), and the prep packs for [evaluation design](../08-interviewing/prep-packs.md#evaluation-design-pack), [applications](../08-interviewing/prep-packs.md#application-pack) and [infrastructure](../08-interviewing/prep-packs.md#infrastructure-pack).
- **Certificate or artefact:** [credential ROI](../04-certifications/credential-roi.md).
- **By path:** [career transitions](../11-tracks/career-transitions.md), [PhD to industry](../11-tracks/phd-to-industry.md), and [visa and relocation](../11-tracks/visa-and-relocation.md) for O-1A evidence.
- **Role hubs:** [AI Engineer](../02-roles/hubs/ai-engineer.md), [AI Evaluation Engineer](../02-roles/hubs/ai-evaluation-engineer.md), [Agentic AI Engineer](../02-roles/hubs/agentic-ai-engineer.md), [Inference Engineer](../02-roles/hubs/inference-engineer.md), [AI Infrastructure Engineer](../02-roles/hubs/ai-infrastructure-engineer.md), [GPU Kernel Engineer](../02-roles/hubs/gpu-kernel-engineer.md).
- **Evidence:** [stage 5 findings](../../research/findings.md#stage-05); sessions [T0-13](../../research/sessions/T0-13-production-portfolio-proof-of-work-standards.md), [T0-20](../../research/sessions/T0-20-github-readme-portfolio-site-writing.md), [T2-01](../../research/sessions/T2-01-tier-calibrated-execution-playbooks.md), [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) and [T0-05](../../research/sessions/T0-05-unconventional-hiring-tactics-oss-audits.md); [errata](../../research/ERRATA.md).
