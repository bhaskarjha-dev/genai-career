---
id: T0-13
title: "Production GenAI Portfolio Proof-of-Work Standards: High-Signal Artifacts vs. the Tutorial-Clone Anti-Portfolio (Oct 2026)"
date: 2026-10-21
status: complete-draft
topic: "Engineering-portfolio signal quality for GenAI roles, Junior through Principal"
tags:
  - genai
  - portfolio
  - hiring-signal
  - anti-portfolio
  - llm-evals
  - llmops
  - observability
  - inference-serving
  - benchmarking
  - rubric
informs_decisions:
  - "Which repos to keep, retrofit, or archive on a public GitHub profile, by experience tier"
  - "Which artifacts (eval harness, benchmarks, cost accounting, telemetry) are mandatory in every portfolio repo"
  - "Where and how to deploy public demos (platform, caps, rate limits) without creating a liability"
  - "How to budget compute for systems-level proof-of-work without cluster access"
  - "Which rubric hiring managers should use to review candidate GitHub profiles"
confidence: "medium overall. Hiring-effect claims: low-to-medium (practitioner testimony; no controlled study found). Tool/platform facts: medium-high (retrieved 2026-10-21; perishable). Rubric: synthesized in this session and untested."
---

# T0-13: Production GenAI Portfolio Proof-of-Work Standards

**Temporal anchor:** 2026-10-21. Prices, limits, licences, and product status were retrieved on that date. Several source pages carry earlier "last verified" stamps; these are noted in the ledger. Treat every number in D5 (tool catalog) as perishable.

**Evidence grades used throughout**

| Grade | Meaning |
|---|---|
| A | Primary or canonical source retrieved this session (official docs, first-party engineering post, peer-reviewed paper, vendor pricing page) that states the claim directly. URL and title recorded. |
| B | Non-canonical copy of a primary source; a primary read only as a search excerpt; a preprint; an employer's own job posting; or three or more concordant, independent practitioner reports. |
| C | Single-source or low-provenance material: SEO or vendor blogs, community posts, anecdotes, third-party analyses with unclear method. |
| D | Recalled from model memory, inferred, derived by arithmetic, or this session's own synthesis. Not externally verified. |
| X | Contradicted by evidence found. |

Claims recalled from memory are capped at D until a source is attached. `S##` identifiers refer to the Sources & Evidence Ledger at the end of the file.

---

## 1. Prior

Five propositions held before searching, each with a falsification condition.

| ID | Proposition (pre-research) | Falsified if | Prior confidence |
|---|---|---|---|
| P1 | Generic RAG/PDF-chat, Streamlit-over-API, and MNIST/Titanic repos are widely treated by reviewers as low-signal. The stronger claim in the brief (they screen candidates out faster than having no GitHub) is plausible but has no controlled evidence behind it. | Sources show these project types are neutral or positive for screens, or a controlled study shows a measurable penalty. | 75% (low-signal); 30% (that a net penalty is *evidenced*) |
| P2 | By late 2026, evaluation practice (datasets, regression suites, judge validation) and cost/latency accounting are cited more consistently than any framework, in both public hiring guidance and job postings. | Posting and guidance analyses show frameworks or model-training skills dominating evaluation. | 70% |
| P3 | A live public endpoint is neither necessary nor sufficient for a strong portfolio, and an unhardened one is a liability (cost abuse, leaked keys, dead links). | Evidence that live demos are the dominant screening artifact, or that hardening cost is negligible. | 65% |
| P4 | At Senior and Staff level the discriminating evidence shifts from "built a thing" to externally verifiable work: merged upstream PRs, rigorous benchmark methodology, design documents. | Postings and rubrics for senior roles still centre on personal demos. | 70% |
| P5 | Distributed-training or large-scale-inference competence can be signalled credibly with under about US$500 of compute if scoped honestly and anchored to external benchmarks, leaderboards, or upstream review. | No credible modest-budget pattern exists, or reviewers discount all small-scale evidence. | 60% |

---

## 2. Research Question

**Primary question.** In October 2026, which technical artifacts, deployment metrics, and architectural designs distinguish a high-signal production GenAI portfolio from an anti-portfolio of tutorial clones, for Junior, Mid, Senior, and Staff roles? Separately: is the claim that listing generic RAG or tutorial projects screens a candidate out faster than listing no GitHub supported by evidence?

**Sub-questions (the brief's domain probes)**

- SQ1. Which project types are flagged as red flags or tutorial spam, and is there a "universal" list?
- SQ2. What quantitative proof must a README contain to demonstrate production competence?
- SQ3. How should a candidate demonstrate evaluation literacy inside a personal repo?
- SQ4. How should observability and tracing tools be integrated into public demos?
- SQ5. What role do live hosted endpoints play compared with static repositories?
- SQ6. How can senior candidates show distributed-training or large-scale-inference experience without a multi-GPU cluster?

**Method.** About 50 searches and 5 full-page fetches on 2026-10-21, across six strategies: (A) negative-signal content; (B) production standards and public rubrics; (C) tiered archetypes; (D) repository anatomy taken from real exemplar repositories; (E) verification of tools and platforms (pricing, limits, licences, ownership); (F) falsification (failure modes, contradicting evidence, decay of advice).

**Limits that shape every conclusion**

- No hiring-manager interviews were possible. Proxies used: named practitioners' public posts, employer job postings, community threads.
- No access to private candidate portfolios or private rejection postmortems. The "repository anatomy" comes from public exemplar repositories (nanochat, nano-vLLM, GuideLLM and inference-perf docs, Anthropic's open take-home). These are not candidate portfolios.
- The negative-signal literature is dominated by SEO and vendor content, some of it visibly echoing other posts. Grades reflect that.
- Three of the A-grade sources (S01 to S03) are first-party Anthropic material, and this memo was written by Claude, which Anthropic builds. Independent corroboration for evaluation practice comes from S05, S07, and S08.

---

## 3. Key Findings

Twelve findings. Each grade reflects the weakest link the conclusion depends on.

**F1. The brief's premise is not established; a narrower claim is.** *Grade: C for the narrow claim, D for the strong claim.*
No controlled study, résumé A/B test, or systematic postmortem set was found showing that listing generic RAG or tutorial repos screens candidates out faster than listing no GitHub. What exists: repeated practitioner assertions that undifferentiated repos are low-signal or counterproductive (S34, S37, S41, S42); one fully narrated n=1 postmortem in which a hiring manager reviewed five AI demos and concluded the candidate had shown tool assembly rather than engineering, followed by an evaluation-driven re-scope and a first technical interview (S35); and a documented but contested "dilution" mechanism, under which extra mildly positive information lowers an impression when a single candidate is judged alone (S47). Against that: many reviewers never open GitHub (S36, S41), and keyword screens reward "RAG" (S33). Working conclusion: undifferentiated repos are low-signal at best and a risk at the hiring-manager stage; "worse than no GitHub" remains unverified.

**F2. No project type is "universally" flagged; the failure modes are.** *Grade: C (taxonomy), B (demand data).*
Sources split on RAG itself: some call a RAG document-Q&A the gold-standard first project (S39), others list generic PDF-chat wrappers as the junior tell (S37). They converge on what makes a project read as tutorial-grade: no measurement, no baseline, no deployment hygiene, a one-shot commit history, unexplained choices. RAG appears in roughly a third to 40% of AI-engineer postings (S33), so the corrective is measurement, not avoidance.

**F3. Evaluation literacy is the most consistently cited separator.** *Grade: B.*
Cited by Anthropic's evaluation guide (S01), the Yan and Liu hiring framework (S04), and Husain's evaluation guidance (S05). Posting analyses agree in direction but not magnitude: 59.7% of AI-first roles in a 6,964-posting analysis require evaluation-related skills (S33); 68% of 198 companies mention evals or benchmarking in another (S33); a 100-posting sample found only 12 mentioning evals (S33). Definitions and samples differ, so treat the range as "common, not universal".

**F4. What counts as evaluation evidence is now specific.** *Grade: A (Anthropic, Zheng et al.), B (Husain-derived practice).*
Start with 20 to 50 tasks drawn from real failures; prefer code-based graders; calibrate model graders against human labels; separate capability suites from near-100% regression suites; report pass@k and pass^k over multiple trials; read transcripts (S01). Open-code roughly 100 traces, use binary single-failure judges, and validate each judge on about 50 pass and 50 fail human labels (S05, S06, S07). LLM judges show position, verbosity, and self-enhancement bias (S08) and anchoring bias (S55).

**F5. Latency and cost proof must include methodology, not only numbers.** *Grade: B (tool docs A).*
Report p50/p95/p99, time-to-first-token, inter-token latency, throughput, goodput under an SLO, and concurrency or request-rate sweeps (S27). Single-process Python load clients can inflate TTFT/TPOT at high concurrency, so client capacity must be checked (S09). First-run effects can be large: one tool report shows 2,484 ms first-run against about 73 ms steady-state TTFT (S27). k6 thresholds exit with code 99 and should be validated to fail when they should (S26). Cost is tokens times a dated price table, plus infrastructure dollars per hour converted to dollars per thousand requests (D, derived).

**F6. Live endpoints cut verification cost but carry real risk; their weight relative to repos is unmeasured.** *Grade: A (platform and security facts), D (relative weight).*
Employers inspect activity traces that are cheap to verify (S46); a working demo is one. Risks: denial-of-wallet and unbounded consumption (S10); free-tier changes, since Hugging Face Gradio and Docker Spaces now require a paid PRO plan except for two ZeroGPU Spaces, and free CPU Spaces sleep (S11, S12, S13); a hard spend cap must be switched on explicitly at OpenAI (S50). Practitioner content calls a dead demo link worse than no link (S42, C).

**F7. Observability tooling is mature; the standard is not.** *Grade: B.*
All OpenTelemetry `gen_ai.*` attributes were still at "Development" status in mid-September 2026, and the conventions moved to a dedicated repository on 2026-06-12 (S22). Langfuse is MIT-licensed and ClickHouse-owned since January 2026, with a free tier of 50k units and 30 days of data (S18). Phoenix is source-available under Elastic License 2.0 (S19). LangSmith's free tier caps at 5,000 base traces per month with 14-day base retention (S20). Free-tier retention is short, so a demo's traces vanish; commit sanitized exports and the scripts that recompute metrics from them.

**F8. Authorship verification is the live problem of 2026.** *Grade: B/C.*
A hiring manager reporting 500+ candidate interviews says a GitHub review takes about 30 seconds and includes spotting AI-generated slop (S34). Anthropic reports that Claude Opus 4 outperformed most applicants on its performance take-home and Opus 4.5 matched the strongest within the time limit, forcing a redesign (S02); its candidate guidance asks for own first drafts and AI-free take-homes unless stated (S03). An IEEE Spectrum piece reports a notable share of interviewees unable to explain solutions they presented (S44). Cheap-to-generate artifacts (READMEs, dashboards) lose signal; externally verifiable or novel artifacts gain it.

**F9. Senior and Staff evidence is externally verifiable engineering plus influence.** *Grade: B.*
Postings from NVIDIA, Inferact (the vLLM creators), Together AI, AMD, and River AI ask for upstream PRs, shipped performance features (paged-KV, speculative decoding, scheduling, quantization-aware serving), maintainer relationships, and technical writing (S32). Yan and Liu's AICE dimensions (ambiguity, influence, complexity, execution) frame senior-plus evaluation (S04).

**F10. Systems-scale credibility on modest hardware is feasible if scoped honestly.** *Grade: B.*
Working patterns: compact reimplementations with disclosed hardware (nano-vLLM, about 1,200 lines, benchmarked on an 8 GB laptop GPU) (S28); Mini-SGLang (about 5k lines) (S29); leaderboards whose rows carry commit hashes (nanochat time-to-GPT-2) (S30); organizer-provided hardware in kernel competitions (AMD x GPU MODE, US$1.1M prize pool) (S31); a public take-home with a published cycle-count threshold (S02); CPU/gloo smoke tests of FSDP2 wiring (S51); simulator-validated load harnesses (S27, S56); rented per-second GPUs (S15). Caveat: educational engines and simulators do not support production or hardware claims.

**F11. The 2026 platform landscape moved; stale tool advice is itself a red flag.** *Grade: A/B.*
Hugging Face's free-tier change (S11); Langfuse joined ClickHouse in January 2026 (S18); Promptfoo joined OpenAI in March 2026 (S23); Replicate joined Cloudflare (S24); GitHub Actions stays free for public repos while a self-hosted-runner fee was announced then postponed (S16); OpenTelemetry's GenAI conventions moved repositories in June 2026 (S22). READMEs should date-stamp results and pin tool and model versions.

**F12. Gotcha screens and vendor red-flag lists decay quickly.** *Grade: B (dates), C (the lists).*
A May 2026 hiring guide told reviewers to treat a claim of experience with "Sonnet 5" as fabricated (S38). Claude Sonnet 5 shipped on 2026-06-30 and Sonnet 5.5 on 2026-09-28 (S49). Trivia-style screens on fast-moving model names produce false rejects within weeks. Most red-flag lists are marketing content that echo one another (S38 to S43).

---

## 4. Recommendation

**Adopt a verifiability-first portfolio standard.** The portfolio's job is to lower a reviewer's cost of verifying competence (S46) in a market where text and dashboards are cheap to fake (S02, S34). Concretely:

**4.1 Classify every claim on a verifiability ladder.**

| Level | Name | Example | Reviewer cost |
|---|---|---|---|
| V0 | Self-asserted | Screenshot, "achieves 95% accuracy" | Cannot verify |
| V1 | Reproducible | One command regenerates `results.json` and the README table; raw data and pinned versions committed; CI run linked | Minutes |
| V2 | Externally attested | Merged upstream PR; leaderboard row with commit hash; independent reproduction; third-party users | Minutes, trusts a third party |
| V3 | Operationally evidenced | 30+ days of uptime and spend logs, an incident postmortem, real users | Minutes to hours |

Every headline README claim must be V1 or higher. Tier 3 portfolios need at least one V2 item; Tier 4 portfolios need V2 as the norm.

**4.2 Retrofit before building.** Do not delete a mediocre RAG or agent repo; upgrade it into a measured system (dataset card, baselines, error analysis, CI-gated evaluation, cost and latency table, telemetry exports). The one postmortem found (S35) and the Anthropic guidance on starting small (S01) both point to this. Archive anything that cannot be retrofitted: unmodified tutorial forks, Titanic/MNIST/Iris notebooks, and repos with a single commit.

**4.3 Mandatory artifacts by tier.** Fifteen artifacts (PA-01 to PA-15) are defined in D2. Tier 0 to 1 needs PA-01 to PA-04, PA-07, and PA-10 to PA-12, plus basic versions of PA-05 (a smoke evaluation in CI), PA-06 (a basic latency table), PA-08 (basic telemetry), and PA-09 if any endpoint is live. Tier 2 requires the full versions of PA-04 to PA-06, PA-08, and PA-09, and adds PA-13. Tier 3 adds PA-14. Tier 4 adds PA-15.

**4.4 Treat live demos as optional, replay-first, and capped.** Default to a static or replay demo that serves pre-computed outputs. If a live model call is needed: a dedicated key with a hard monthly cap, per-IP rate limits, token caps, no side-effecting tools, and a visible budget meter (D6). Put the date of last verification on the README.

**4.5 For systems depth, buy verifiability rather than hardware.** Prefer measured small-scale results with disclosed hardware, external leaderboards or open challenges, and upstream PRs. Label simulated or modelled results as such (D8).

**4.6 Use the review rubric in D9 with calibration.** It is a synthesized instrument, unvalidated. Before adoption, have three reviewers score the same ten public repos independently and revise the anchors until they agree.

**4.7 Keep the portfolio fresh.** Pin tool and model versions, date every benchmark, and re-run the smoke evaluation on a schedule. Stale instructions (for example "deploy a free Gradio Space") are a visible tell.

**4.8 Reference specifications.** Four level-calibrated specifications are in D3: R1 (Junior), R2 (Mid), R3 (Senior), R4 (Staff/Principal).

---

## 5. Alternatives Considered

| # | Alternative | Evidence for | Evidence against | Verdict |
|---|---|---|---|---|
| A1 | Skip portfolios; optimize the résumé for ATS keywords | "RAG" appears in about a third to 40% of postings (S33), so keyword presence helps early screens; many reviewers never open GitHub (S36, S41) | Hiring-manager stage reviews do open repos and judge quickly (S34); a portfolio is the only artifact that can raise a stalled funnel (S35) | Rejected as a sole strategy; keep keywords, add evidence |
| A2 | Many small demos (breadth) | Low effort per repo | Breadth without measurement reads as tool assembly (S35, S37); dilution risk when reviewed alone (S47) | Rejected; 2 to 3 deep repos instead |
| A3 | Live demo only, no repo | Cheap to verify (S46) | Hosting policy and cost risk (S10, S11); no way to inspect method; dead links hurt (S42) | Rejected; use replay-first plus a repo |
| A4 | Train or fine-tune a model as the headline project | Distinctive when done honestly (S30) | Training claims without baselines or held-out evaluation are a listed red flag (S38); compute cost | Narrow use: small, scoped, fully evaluated runs only |
| A5 | Open-source contributions instead of personal repos | Strong for Senior and above (S32); V2-class evidence | Hard for juniors; maintainers' review capacity is limited (D) | Complement at Tier 1+, primary at Tier 3+ |
| A6 | Competitions and leaderboards as attestation | External, comparable metrics (S30, S31) | Narrow niches; requires time; some need specific hardware | Include where the target role matches |
| A7 | Writing only (blog posts and talks) | Cited in postings (S32) | Easy to produce with AI; weak without reproducible code (S34) | Pair writing with V1 artifacts |
| A8 | Wait for a validated rubric before changing anything | Avoids acting on weak evidence | No validated rubric exists or is likely soon; the cost of the recommended artifacts is low and independently useful for learning | Rejected; act now, calibrate the rubric as you go |

---

## 6. Detailed Findings

### D1. The anti-portfolio: nine project archetypes and why each fails

**Premise check (SQ1).** The sources do not support a universal ban list (F2). They support a failure-mode list. Each archetype below is "disqualifying as presented", meaning a reviewer who sees only this artifact learns nothing they can trust. Each has a redemption path, because most can be retrofitted.

**A swap test (synthesized, Grade D).** Replace the model call with a stub or a non-AI baseline. If the project looks the same, cannot be tested, or nobody can say what got worse, the model is decoration and the repo is a wrapper.

**AP-1. "Chat with your PDF" (LangChain or LlamaIndex, a vector store, Streamlit).** *Grade C.*
- Why it fails: it shows library assembly, not judgment. There is no retrieval baseline, question set, or error analysis, so output quality is unknowable, and nearly every candidate has one. In the single narrated postmortem, a hiring manager's review reduced five such demos to a statement that the candidate had shown tool assembly (S35). A junior-tell list names the same pattern (S37).
- 30-second signals: default chunking, unpinned requirements, screenshot-only README, no tests, one or two commits, no evaluation folder.
- Redemption: specification R1.

**AP-2. A Streamlit or Gradio wrapper over a hosted LLM API.** *Grade C (taxonomy), A (platform facts).*
- Why it fails: the system prompt is the whole product, so the repo has nothing beyond an API call to assess. It also carries operational liabilities: key handling, no rate limit or spend cap (S10), sleeping or erroring demos (S13), and hosting-policy changes (S11).
- Signals: under about 150 lines; one chat input and one API call; keys in a committed `.env`; a deployed URL that errors.
- Redemption: add a measurable differentiator (own data plus evaluation, or cost-aware routing) and harden (D6), or archive.

**AP-3. Classical-ML staples and course datasets (MNIST, Titanic, Iris, house prices, tweet sentiment).** *Grade C.*
- Why it fails: identical across candidates, so it carries no discriminating information, and there is no problem framing or constraint-driven decision. One guide names these as red flags for experienced technical recruiters (S39).
- Signals: tutorial dataset; notebook only; accuracy on a clean split; no baseline discussion.
- Redemption: archive. If kept, reframe as a calibration exercise (for example comparing a model judge to human labels), not as a headline project.

**AP-4. Metric-free multi-agent demos ("AI research team", "autonomous X agent").** *Grade B (guidance A, red-flag list C).*
- Why it fails: agent failures compound. Without outcome-based graders, multiple trials, and failure-mode discussion, the demo shows nothing reproducible (S01). A vendor list includes "agent with no failure-mode discussion" (S38).
- Signals: several agent frameworks; role names such as researcher, writer, critic; no tasks file; demo video only; no cost per task.
- Redemption: specification R2 (state-check graders, pass@1 and pass^k, cost per task).

**AP-5. Benchmark-number theater.** *Grade B.*
- Why it fails: headline claims ("98% accuracy", "100% deflection") with no defined test set, split, grader, or interval show evaluation illiteracy. The same vendor list flags RAG built with no recall figure and perfect-accuracy claims (S38). Evaluation guidance asks for dataset provenance and judge calibration (S01, S05, S08).
- Signals: a number with no link to a script; labels produced by the same model being evaluated; test data used for prompt tuning.
- Redemption: PA-01, PA-03, PA-04.

**AP-6. Single-commit, tutorial-fork, or AI-one-shot repositories.** *Grade B/C.*
- Why it fails: authorship cannot be assumed. A hiring manager with 500+ interviews says he can tell quickly and can spot AI-generated slop (S34); other sources list one-large-commit and generic-README patterns (S43). Anthropic asks for own first drafts (S03). The harm is raised verification cost, not the content itself.
- Signals: one large commit; boilerplate README with emoji headers; no iteration; unchanged tutorial structure and names.
- Redemption: iterative history, `docs/PROCESS.md` disclosing AI assistance, and the ability to explain any file in an interview.

**AP-7. Training or fine-tuning claims without baselines, held-out evaluation, or cost.** *Grade C.*
- Why it fails: "trained an LLM" frequently means a small LoRA run judged by feel; a vendor list flags unsupported training claims (S38). Conflating fine-tuning with pretraining is a credibility loss (D).
- Signals: no base-model comparison; evaluation on training data; no cost or seed; no loss curves.
- Redemption: base versus tuned on a held-out set with intervals, a cost table, and an ablation; or a scaled-down run against a public metric (S30).

**AP-8. Framework-only fluency.** *Grade C.*
- Why it fails: if all logic sits inside framework abstractions, the reviewer cannot see what the candidate understood. A vendor list suggests probing for what was built without the framework (S38); Yan and Liu probe depth through the candidate's own project (S04). Using a framework is not disqualifying; being unable to explain what it sends over the wire is.
- Signals: deep chain or agent abstractions, no raw request logs, no tracing of the prompt actually sent.
- Redemption: show raw request and response in traces; implement one component (retriever or tool loop) directly, with tests.

**AP-9. Unsafe or dead public demos.** *Grade A (risk class), C (hiring effect).*
- Why it fails: committed keys, open proxies, unbounded spend, or an erroring link. Unbounded consumption is an OWASP risk class (S10); GitHub scans public repositories for provider keys, so a leaked key is revoked and still visible in history (S17); practitioner content treats a broken link as worse than none (S42). Hosting-policy changes can silently kill free demos (S11, S13).
- Signals: keys in history; no rate limit or cap; an error page; stale last-updated date.
- Redemption: D6 checklist; a replay-first demo.

### D2. Mandatory production artifacts (SQ2, SQ3, SQ4)

Fifteen artifacts. "Tier min" is the first tier at which the artifact is expected. Pass criteria are written so a reviewer can check them in minutes. The numeric defaults come from S01, S05, S06 and are starting points, not standards.

| ID | Artifact | Path | Pass criteria (reviewer-checkable) | Anchors | Tier min |
|---|---|---|---|---|---|
| PA-01 | Evidence block | `README.md` (first screen) | Claim, metric, method, command, date, commit SHA, and hardware for each headline number. Every number links to a file in `bench/` or `eval_harness/`. | S34, S46 | T0 |
| PA-02 | One-command reproduction | `Makefile`, lockfile, `Dockerfile` | `make repro` regenerates tables from raw data. Dependencies pinned; model IDs and price-table date recorded; seeds fixed where applicable; run cost stated. | S01 | T0 |
| PA-03 | Dataset card | `docs/dataset-card.md` | Source, licence, size, splits, labelling protocol and labeller, known gaps, PII handling, checksum. Dev and test strictly separated. | S01, S05 | T0 |
| PA-04 | Evaluation harness | `eval_harness/` | Tasks as data; code-based graders first; model graders only where needed, with versioned prompts; three or more trials for stochastic tasks; capability and regression suites kept apart; judge calibration report (TPR and TNR on about 50 pass and 50 fail human labels); error-analysis notes from about 100 coded traces. | S01, S05–S08 | T0 (small), T2 (full) |
| PA-05 | CI gates | `.github/workflows/` | PR runs tests plus a cheap smoke evaluation (cached or capped); scheduled full evaluation; fails on regression; uploads artifacts; per-run spend cap; badge fed by CI-produced JSON and linked to the run. | S01, S16, S25 | T1 (smoke), T2 (full) |
| PA-06 | Latency and throughput benchmark | `bench/`, `benchmarks.md` | p50, p95, p99; TTFT; ITL or TPOT; tokens/s; error rate; concurrency or rate sweep; warm and cold reported separately; hardware, client spec, and engine/driver versions; raw files plus plot script; client-saturation check; three or more repeats with spread. | S09, S26, S27 | T0 (basic), T2 (full) |
| PA-07 | Cost accounting | `benchmarks.md` or `cost/` | Tokens times a dated price table (URL and date) gives dollars per request and per successful task; infrastructure dollars per hour convert to dollars per 1k requests; monthly burn of any live demo; budget cap stated. | S50, D | T0 |
| PA-08 | Telemetry | `src/…/telemetry`, `docs/traces/` | Spans carry model ID, tokens in and out, latency, finish reason, retrieval IDs, tool names, error type, and cost. Sanitized dated exports committed; at least one failing trace promoted to an evaluation case; content capture off on the public demo; semantic-convention version pinned. | S01, S18–S22 | T1 (basic), T2 (full) |
| PA-09 | Abuse resistance | `docs/SECURITY.md`, code | Per-IP and per-key rate limits; input and output token caps; timeouts; hard spend cap on a dedicated key; no side-effecting tools on a public demo; secrets only in the platform store; injection tests including tool-output injection. | S10, S17, S50 | T1 (if live), T2 |
| PA-10 | Architecture and decisions | `docs/architecture.md`, `architecture.svg`, `docs/decisions/` | Data and control flow diagram; at least three ADRs, each naming a rejected alternative; a non-AI baseline comparison. | S04 | T0 |
| PA-11 | Failure analysis | `docs/failure-analysis.md` | Failure taxonomy with counts; negative results; threats to validity; explicit non-claims. | S01, S04 | T0 |
| PA-12 | Authorship and AI-use disclosure | `docs/PROCESS.md` | What was AI-assisted; what was verified by hand; iterative commit history; licence. | S03, S34 | T0 |
| PA-13 | Operational evidence | `docs/ops/` | SLOs with thresholds; uptime and spend log of 30 or more days; at least one incident postmortem (real or staged); runbook and rollback; a model-swap report. | S01, S04 | T2 |
| PA-14 | Profiling and systems analysis | `latency_profiling/` | Profiler timelines, roofline or bandwidth analysis, ablation table, correctness tests against a reference for every custom kernel, hardware fingerprint. | S09, S32 | T3 |
| PA-15 | Design docs and adoption trail | `docs/rfcs/` | RFC with alternatives and threats to validity; external review trail; versioned spec and changelog; independent reproductions; upstream merges. | S02, S04, S32 | T4 |

**Cross-cutting rules (Grade D, synthesized from the sources above)**
1. Charts are generated from committed raw data by a script. Hand-edited images are V0.
2. Every number has a command that regenerates it.
3. Include negative results and non-claims.
4. Pin versions and date every benchmark and price table.
5. Never commit secrets; assume history is public.
6. A badge is only evidence if it links to the workflow run or the result file that produced it.

**SQ3: how to demonstrate evaluation literacy inside a personal repo.** The reviewer should be able to find, in order: the failure taxonomy that motivated the cases (S05, S06); the cases themselves, sourced from real or realistic failures (S01); the graders and which are code-based; the judge prompt, its version, and its TPR/TNR against human labels (S06, S08); trial counts and the pass@k versus pass^k choice (S01); the regression suite wired into CI (S01); and a short note on one eval bug the candidate found and fixed (S01 reports grader bugs that changed a headline score).

**SQ4: telemetry inside public demos.** Instrument with OpenTelemetry or a vendor SDK, pin the semantic-convention version because all `gen_ai.*` attributes remain at Development status (S22), and export to a backend whose retention you control or whose limits you understand: Langfuse Hobby offers 50k units and 30 days (S18); LangSmith's free plan caps at 5,000 base traces a month with 14-day base retention (S20); Phoenix self-hosts free under Elastic License 2.0 (S19); TruLens is MIT and OpenTelemetry-native (S21). Because free-tier data expires, commit sanitized trace exports with dates and the script that recomputes p95 and cost from them. On Hugging Face Spaces, outbound traffic is limited to ports 80, 443, and 8080 (S11), and Phoenix's default OTLP gRPC port is 4317 (S19), so use HTTPS ingestion; this port conflict is an inference from the two documents and should be tested (D).

### D3. Tiered archetypes and four reference specifications (SQ1–SQ6)

**Tier model (Grade D, synthesized; calibrated against S04, S32, S33).**

| Tier | Level | What the portfolio must prove | Archetype that carries signal | Typical evidence ceiling |
|---|---|---|---|---|
| T0 | New graduate or career switcher (0–1 y) | You can finish, measure, and explain a small system | Measured retrieval or extraction over a non-generic corpus, with baselines and error analysis | V1 |
| T1 | Junior (1–2 y) | You can ship and maintain a small service with tests and CI | The T0 system plus CI-gated evaluation, a capped deployment, and one docs or test PR upstream | V1–V2 |
| T2 | Mid (3–5 y) | Production judgment: reliability, cost, evaluation-gated releases | Evaluation-gated agent or service with a router, tracing, load tests, and an incident postmortem | V1–V3 |
| T3 | Senior (6–9 y) | Depth and trade-off command at system or kernel level | Serving, quantization, or kernel study with rigorous method and an upstream contribution | V2 |
| T4 | Staff or Principal (10+ y) | Leverage: standards, reference implementations, adoption | Methodology or benchmark program with external adopters and design docs | V2–V3 |

Four reference specifications follow: **R1** (T0–T1, Junior), **R2** (T2, Mid), **R3** (T3, Senior), **R4** (T4, Staff and Principal). Names are illustrative. Numeric defaults (question counts, trial counts, budgets) are starting points derived from S01, S05, S06, and S15 and should be changed with a stated reason.

| Spec | Tier | Compute cap | Time (part-time) | Verification target | Rubric threshold (D9) |
|---|---|---|---|---|---|
| R1 | T0–T1 | about US$25–30 API spend, no GPU | 4–6 weeks | V1 throughout | 60 or above, no hard fail |
| R2 | T2 | about US$100 (API plus hosting) | 8–10 weeks | V1, plus V3-lite (30+ day demo log) | 65 or above |
| R3 | T3 | about US$300 (rented GPU hours) | 6–10 weeks | V1, plus at least one V2 item | 70 or above |
| R4 | T4 | about US$500 own spend; rest via collaborators | 3–6 months | V2 as the norm, at least one V3 item | 70 or above |

---

#### R1. Junior (T0–T1): a measured retrieval-and-answer system over a non-generic corpus

**Signal claimed:** "I can finish a small system, measure it, find where it fails, and report honestly." **Not claimed:** scale or operations.

```
corpus snapshot ─> ingest/chunk ─> index (BM25 | dense | hybrid)
                                      │
question ─> retrieve(k) ─> [rerank?] ─> generate (with citations)
                                      │
                          traces (spans/logs) ─> eval_harness/
                                                  ├─ retrieval: recall@k, MRR
                                                  ├─ code graders: citation validity, abstention
                                                  └─ one binary judge + human-label calibration
```

**MUST**
1. **Corpus.** Public, licensed, versioned, not a generic PDF; snapshot hash recorded; roughly 300 or more documents or equivalent. Prefer corpora with checkable answers and drift, such as a library's versioned docs and changelogs, or public regulations.
2. **Question set.** At least 50 author-written questions with gold answer spans and gold source IDs; at least 10 unanswerable questions to test abstention (balanced positive and negative cases, S01); dev and test split fixed before tuning; labeller recorded.
3. **Baseline ladder.** BM25, dense, and hybrid retrieval; optional reranker; an extractive non-LLM baseline. Report recall@k and MRR for retrieval and answer-level scores for each rung. Document at least one negative result.
4. **Answer evaluation.** Code graders for citation validity (cited ID exists and quoted span appears in it) and for abstention. One binary LLM judge for one failure mode, such as an unsupported claim, validated on about 50 pass and 50 fail human labels with TPR and TNR reported (S06). At least three trials where sampling is stochastic; report mean and interval.
5. **Error analysis.** Open-code about 100 traces (or all dev traces if fewer) into a taxonomy with counts (S05). Fix the top class and show before and after on dev and on the untouched test split.
6. **CI.** Tests plus a smoke evaluation on 10 to 15 cases using cached responses or a capped key; nightly or manual full run; badge fed by CI JSON (S25).
7. **Performance and cost.** p50 and p95 latency for three configurations at concurrency 1, 4, and 8; tokens in and out; dollars per query from a dated price table; hardware and client spec; cold and warm reported separately.
8. **Telemetry.** Structured spans or logs with latency, tokens, and document IDs; five sanitized traces in `docs/traces/`; one failing trace linked to a case in `eval_harness/`.
9. **Delivery.** A replay-first static demo, or a live endpoint with per-IP rate limit, token caps, and a hard-capped key (D6); `docs/SECURITY.md`.
10. **Honesty.** Evidence block in the README, limitations, and `docs/PROCESS.md`.

**SHOULD:** chunk-size and k ablation; comparison against a non-LLM approach; one docs or test PR to a dependency.

**Defense questions:** Show a query where dense lost to hybrid and say why. What are your judge's TPR and TNR, and what did you do about the misses? What breaks if the corpus is 100 times larger?

**Avoid:** tuning on the test split; a judge that grades its own generator's outputs without calibration; claiming accuracy without the question set in the repo.

---

#### R2. Mid (T2): an evaluation-gated, tool-using agent service with a router, tracing, and operational evidence

**Signal claimed:** production judgment: releases gated by evaluation, cost-aware routing, tracing, and failure handling.

```
client ─> API (FastAPI) ─> auth + rate limit ─> router (small model | large model)
                               │                      │
                          job queue ─> agent worker ──┴─> tools ─> mock commerce backend (SQLite)
                               │
                        OTel spans ─> Langfuse or Phoenix ─> dashboards + alert
CI:  PR ─> unit tests ─> smoke eval (<=15 tasks) ─> gate
     nightly ─> full eval (>=50 tasks x 5 trials) ─> report + badge JSON
Flywheel: weekly error analysis of traces ─> new regression cases
```

**Environment.** A simulated commerce backend with a policy document and tools (`lookup_order`, `check_policy`, `issue_refund` with a limit, `escalate`). Tasks are an initial state, a scripted or simulated-user conversation, and an expected end state. Grade outcomes by checking state in code, add turn and cost limits, and use a calibrated model-graded rubric only for tone and policy adherence (S01 describes this outcome-grading pattern).

**MUST**
1. **Task suite.** At least 50 tasks, split into capability and regression sets; at least 5 trials per task; report pass@1 and pass^k with intervals, plus cost and latency per task (S01).
2. **Evaluation-gated CI.** A PR must keep the regression suite above a stated threshold; model or prompt changes require a diff report in `reports/`.
3. **Model-swap report.** Run the suite on two models or versions; publish a cost versus pass^k frontier and the decision taken.
4. **Router.** Rules or a classifier that sends simple intents to a cheaper model; ablate against single-model baselines; report cost change and success change with intervals.
5. **Reliability.** Idempotency keys on refunds; retries with jitter; timeouts; provider-failure fallback; a chaos test injecting 429s and timeouts, with results.
6. **Safety.** Least-privilege tools; human approval above a refund threshold; injection tests via tool output (ticket text); a red-team suite (custom or Promptfoo, S23) in CI.
7. **Telemetry.** OpenTelemetry GenAI attributes or a vendor SDK; a trace for every task; dashboards for p95 latency, daily spend, and pass rate; at least one alert rule; weekly error analysis that promotes at least three production-style traces into regression cases.
8. **Load testing.** k6 or Locust with thresholds in CI for non-model paths (S26); streaming-aware TTFT and ITL measurement for model-facing paths using a multi-process client (S09, S27); state provider variance if a hosted API is used.
9. **Operations.** SLOs; a 30-day or longer uptime and spend log for the live demo; one incident postmortem (real or staged); runbook and rollback.
10. **Hardening.** PA-09 in full; replay-first; hard-capped key.

**Hosting options (verified in D5):** Railway Hobby at US$5 a month (S14), Modal Starter with US$30 monthly credit (S15), or a Hugging Face Docker Space on PRO at US$9 a month (S12).

**Defense questions:** What was your pass^5 versus pass@1, and what does the gap tell you? Which regression case came from a trace, and what was the failure? What did the router cost you in success rate?

**Avoid:** an LLM judge as the only grader for state-changing tasks; shared state between trials; reporting pass@1 only.

---

#### R3. Senior (T3): a serving study with rigorous method, one profiled kernel, and an upstream contribution

**Objective.** Map the throughput, latency, quality, and cost frontier for serving a 7B to 8B-class open model under stated SLOs on one rented GPU, and attribute differences with profiling.

```
load generator (multi-process) ─> OpenAI-compatible server (vLLM or SGLang) ─> 1 GPU
     │                                  configs: BF16 | FP8 or 4-bit | prefix cache | spec decode
     │                                  optional: custom Triton kernel path
     ├─ raw.jsonl + env.json (hardware, driver, CUDA, engine SHA, flags, checkpoint hash)
     └─ summary.json ─> plot.py ─> benchmarks.md
quality gate per config: perplexity + 2–3 task metrics + domain set, with intervals
profiling: PyTorch profiler or Nsight timelines ─> latency_profiling/
```

**Experimental matrix.** Choose 3 to 5: BF16 baseline; FP8 or a 4-bit weight-only scheme the engine supports; prefix caching on and off; chunked prefill; speculative decoding on and off where supported; one custom Triton kernel against a reference.

**MUST**
1. **Load method.** Multi-process generator (inference-perf or GuideLLM) with Poisson arrivals and concurrency sweeps; discard warm-up; at least three repeats with spread; record input and output length distributions; record client CPU headroom to rule out a client-bound plateau (S09, S27).
2. **Environment capture.** `env.json` with GPU model, driver, CUDA, engine version or SHA, flags, and checkpoint hash.
3. **Quality gate.** Per configuration, perplexity plus two or three task metrics plus a domain set, with intervals; report quantization regressions rather than hiding them.
4. **Cost.** Dollars per million output tokens at the SLO (goodput-based) using a dated list price (S15).
5. **Profiling and kernel.** Timeline attribution (prefill, decode, attention, GEMM, communication where relevant); a roofline or bandwidth-bound argument; correctness tests against a PyTorch reference that run on CPU; microbenchmarks.
6. **CPU-side CI.** Load-generator tests against an inference simulator (llm-d inference simulator, S27, S56) and kernel-reference tests; GPU runs manual, with raw logs committed.
7. **Upstream.** At least one PR or well-formed issue (benchmark script, test, bug fix, or docs) to the engine or a benchmark tool, with a link to the maintainers' review (S32).
8. **Extrapolation note.** "What changes at 8 GPUs": parallelism and memory arithmetic grounded in the Ultra-Scale Playbook (S52), labelled a model, not a measurement.

**Budget arithmetic (Grade D, derived from S15's list rates):** an H100 at US$0.001097 a second is about US$3.95 an hour, so 40 GPU-hours is about US$158; an A100 80 GB at US$0.000694 a second is about US$2.50 an hour, so 60 GPU-hours is about US$150. Prices are perishable.

**Defense questions:** Why did throughput plateau where it did, and how do you know the client was not the bottleneck? What did quantization cost you in quality, with what interval? What would change at tensor-parallel 8?

**Avoid:** comparing engines with different flags; reporting means only; presenting educational reimplementations as production evidence; extrapolating to clusters without labelling the model.

---

#### R4. Staff and Principal (T4): a methodology-and-standards program with external adoption

**Objective.** Close a real measurement or reliability gap by publishing a versioned method that others adopt. Pick one gap: client-side measurement bias and cold-start contamination in LLM-serving benchmarks (S09, S27); agent-evaluation reproducibility, including trial isolation, grader leakage, and saturation (S01); or SLO-aware cost reporting, meaning dollars per successful task at a stated p95.

```
problem statement ─> RFC ─> reference harness ─> cross-system results (raw logs, provenance)
        ▲                                             │
        └──── external review + independent reproductions ◄┘ ─> upstream merges / adoption ─> versioned spec
```

**MUST**
1. **RFC.** Problem, prior art, alternatives, threats to validity, rollout.
2. **Reference harness.** Multi-process, deterministic configuration, environment capture.
3. **Cross-system results.** At least two engines or hardware classes, with raw logs and provenance; community-contributed runs clearly attributed.
4. **Validation.** At least two independent reproductions, and maintainers' review of configuration parity before any "winner" is claimed.
5. **Adoption.** Merged PRs to upstream benchmark tools, or documented use in others' repositories or posts.
6. **Governance.** Versioned spec, changelog, contribution guide, deprecation policy.
7. **Mentorship.** At least two contributors onboarded through reviews and labelled issues.
8. **Credibility.** At least one published correction or retracted result, with an explanation.

**Mapping.** Yan and Liu's AICE dimensions (S04): ambiguity (defining the problem), influence (adoption), complexity (multiple systems), execution (shipped and versioned). Postings reward the same behaviors: upstream-first work, roadmap input, maintainer relationships, technical writing (S32).

**Defense questions:** Who outside your organization depends on this, and how do you know? What did a reproduction find that you got wrong? What is out of scope, and why?

**Avoid:** cross-engine "leaderboards" without configuration parity; multi-node claims without multi-node data; solo authorship with no external review.

---

### D4. Repository anatomy (SQ2)

Derived from exemplar public repositories, not candidate portfolios: nanochat's single-command reference run and leaderboard table with commit hashes (S30); nano-vLLM's compact benchmark script and disclosed hardware (S28); GuideLLM and inference-perf's benchmark configurations (S27); Anthropic's open take-home with published cycle-count thresholds (S02). Names follow the brief (`benchmarks.md`, `eval_harness/`, `latency_profiling/`, `architecture.png` or `.svg`).

```
repo/
├── README.md                    # evidence block first; limitations; link to PROCESS.md
├── Makefile                     # repro | eval-smoke | eval-full | bench | cost | report
├── pyproject.toml + lockfile    # pinned dependencies
├── Dockerfile / compose.yaml
├── benchmarks.md                # generated from bench/results/*; never hand-edited
├── architecture.svg             # diagram; editable source alongside
├── .github/workflows/
│   ├── ci.yml                   # tests + smoke eval, capped spend
│   ├── nightly-eval.yml         # full eval; writes badge JSON; uploads artifacts
│   └── bench-badge.yml          # optional: publishes badge endpoint JSON
├── docs/
│   ├── architecture.md
│   ├── decisions/ADR-0001-*.md
│   ├── dataset-card.md
│   ├── failure-analysis.md
│   ├── PROCESS.md               # authorship and AI-use disclosure
│   ├── SECURITY.md              # threat model, caps, rate limits, kill switch
│   ├── ops/                     # SLOs, uptime and spend logs, postmortems (T2+)
│   ├── rfcs/                    # design docs (T4)
│   └── traces/                  # sanitized, dated trace exports and screenshots
├── eval_harness/
│   ├── datasets/                # jsonl + schema + checksums
│   ├── tasks/                   # capability/ and regression/
│   ├── graders/                 # code-based first
│   ├── judges/                  # versioned prompts
│   ├── calibration/             # human labels + TPR/TNR report
│   ├── cases_from_prod/         # promoted failures
│   └── runs/                    # committed summaries, not full transcripts
├── latency_profiling/           # T3+: profiler timelines, roofline, kernel microbenchmarks
├── bench/
│   ├── load/                    # k6, Locust, GuideLLM, or inference-perf configs
│   ├── results/YYYY-MM-DD_<hardware>_<sha>/{raw.jsonl,summary.json,env.json}
│   └── plot.py
├── src/<package>/
└── tests/
```

**README evidence block (template; every value is a placeholder).**

```markdown
## Evidence (generated YYYY-MM-DD from commit <sha>)
| Claim | Metric | Method | Reproduce | Hardware / env | Level |
|---|---|---|---|---|---|
| Hybrid retrieval beats dense on my test split | recall@5 <x> vs <y> (95% CI <a–b>) | <N>-question test split, author-labelled | `make eval-full` (about <N> min, about $<N>) | API only | V1 |
| p95 latency at 8 concurrent | <N> ms (cold <N> ms) | k6, 5 min, 3 repeats | `make bench` | client <spec>; server <spec> | V1 |
| Cost per successful task | $<N> | price table dated YYYY-MM-DD (<URL>) | `make cost` | n/a | V1 |
| Upstream fix merged | <PR link> | maintainer review | link | n/a | V2 |
```

### D5. Tool and platform catalog (as of 2026-10-21; perishable)

Facts below were retrieved on the anchor date. Where a source page is a mirror or third-party summary, the grade says so. "Verify" means check the vendor's current page before spending money.

| Tool | Portfolio role | Verified facts | Gotchas | Grade / source |
|---|---|---|---|---|
| Hugging Face Spaces | Demo hosting | Static Spaces are free. Creating Gradio or Docker Spaces that run on compute requires a paid plan (PRO, US$9 a month); free personal accounts in good standing can host up to 2 Gradio Spaces on ZeroGPU. Free CPU hardware sleeps after about 48 hours idle. Outbound traffic is limited to ports 80, 443, and 8080. A secrets scanner is built in. Examples of paid GPU rates: T4 small US$0.40 an hour, L4 US$0.80, A10G small US$1.00, A100 large US$2.50. | Older tutorials still say Gradio and Docker Spaces are free. A paid GPU Space keeps billing until paused (a T4 small left on for 30 days is about US$288, derived). ZeroGPU hardware and daily-quota figures conflict across sources (H200 on HF's pricing page; Blackwell RTX Pro 6000 in third-party summaries; free quota 2 to 5 min a day, PRO 25 to 40); verify. | A (S11, S12, S13); quotas unresolved |
| Modal | Serverless CPU and GPU | Starter plan is US$0 a month with US$30 monthly credit; billing per second. List GPU rates per second: H100 US$0.001097, A100 80 GB US$0.000694, L40S US$0.000542, B200 US$0.001736. Starter limits reported as 100 containers and 10 GPU concurrency. Academic and startup credit programs exist. A third party reports network-egress billing from 2026-10-01 (US$0.04 per GiB beyond 1 TiB on Starter). | The pricing page read was a non-canonical mirror host. At list rates, US$30 buys about 7.6 H100-hours (derived). | B (S15); egress C |
| Railway | App hosting | Free plan with a US$1 monthly credit; Hobby US$5 a month including US$5 usage; Pro US$20 a month; a one-time US$5 trial grant. Usage rates: RAM US$10 per GB-month, CPU US$20 per vCPU-month, egress US$0.05 per GB, volumes US$0.15 per GB-month; billed per minute. | Phoenix's gRPC port needs Railway's TCP proxy. Free resources are small. | A (S14) |
| Replicate | Model API hosting | Part of Cloudflare after an announced acquisition (November 2025). Per-second billing for hosted models reported. | Product direction may change post-acquisition. | B (S24) |
| GitHub Actions | CI and scheduled evaluation | Standard hosted runners remain free for public repositories. A 2026 pricing revision announced a platform charge for self-hosted runners; that charge was postponed after criticism. | Current status of the self-hosted fee not re-verified. GPU runner availability and price not verified. Evaluation that calls paid APIs needs a per-run spend cap. | A (S16 announcements); status B |
| k6 (Grafana) | Load tests with pass/fail thresholds | Thresholds (for example a p(95) bound) make the run exit with code 99 on breach; Grafana's guide advises checking that thresholds fail when they should. | Request duration covers the whole response, so streaming TTFT and ITL need custom metrics or an LLM-aware tool (inference, D). | A (S26) |
| Locust | Python load tests | Can run headless in CI (recalled, snippet only). | Not verified against current docs. | D |
| `vllm bench serve` | Engine-native serving benchmark | Request-rate and max-concurrency controls; reports TTFT, ITL, and TPOT percentiles. | Single-process client bias at high concurrency (S09). | B (S27) |
| GuideLLM | LLM benchmarking sweeps | vLLM-project tool; targets OpenAI-compatible servers, including the llm-d simulator. | Fork copy and PR read, not the canonical repo. | B (S27) |
| inference-perf (kubernetes-sigs) | LLM performance benchmarking | Load patterns plus TTFT, TPOT, ITL, and goodput metrics. Proposed in S09 as the multi-process fix for client bias. | Newer tool; flags change. | A (repo), B (S09) |
| NVIDIA AIPerf | LLM benchmarking | A third-party guide describes it as the successor to GenAI-Perf. | Provenance weak. | C (S27) |
| llm-d inference simulator | GPU-free mock server | Used in GuideLLM's docs and cited in S09 for testing harnesses without a GPU. | Validates harness logic only. | B (S27, S56) |
| Shields.io endpoint badge | CI-fed badges | Endpoint JSON needs `schemaVersion` (1), `label`, `message`; `color` optional. The Dynamic Badges action writes such JSON to a Gist. | A badge is V0 unless it links to the run or file that produced it. | B (S25) |
| Langfuse | Tracing, evaluation, prompt management | MIT-licensed core; ClickHouse acquired it in January 2026 and states it stays open source and self-hostable. Cloud Hobby: free, 50k units a month, 30-day data access, 2 users. Core US$29 a month. Units are traces plus observations plus scores; one third-party example shows about 7 units per trace (so Hobby is roughly 7k traces a month, derived). | Free-tier retention of 30 days. Production self-hosting is a multi-service stack (Kubernetes or Terraform). | A (S18) |
| Arize Phoenix | Tracing, evaluation | Elastic License 2.0: source-available, not OSI-approved. Self-hosting is free. Default OTLP gRPC port 4317. | gRPC is awkward on Railway and blocked by Spaces' egress rule (inference). | A (S19) |
| LangSmith | Tracing, evaluation | Developer plan US$0 with 5,000 base traces a month; base retention 14 days; personal organizations capped at 5,000 traces a month until a card is added. A third-party comparison says self-hosting is Enterprise-only (C), and another third party reports a retention change effective 2026-09-14 (C). | A public-demo traffic spike can hit the cap and drop traces. | A (S20); change C |
| TruLens | Evaluation and tracing | MIT-licensed; OpenTelemetry-native; maintained by Snowflake. | Smaller ecosystem than Langfuse (D). | A (S21) |
| Maxim AI | Commercial evaluation and observability | Capabilities come from the vendor's own marketing. | Free-tier terms not verified. | C |
| OpenTelemetry GenAI conventions | Vendor-neutral attribute names | All `gen_ai.*` attributes at Development status as of mid-September 2026; moved to a dedicated repository on 2026-06-12 (v1.42.0); message-content capture is opt-in. | Many blog posts wrongly call them stable. Pin the version. | B (S22) |
| Promptfoo | Prompt, agent, and red-team evaluation in CI | MIT-licensed; joined OpenAI in March 2026 and stated it remains open source. | Governance may shift; pin versions. | B (S23) |
| Harbor, Braintrust, Ragas, DeepEval | Evaluation frameworks | Harbor and Braintrust appear in Anthropic's framework appendix (S01). Ragas and DeepEval are named in vendor guides and a docs index. | Pricing and terms not verified. | A (listing in S01); rest C |
| OpenAI spend limits | Cost cap | Organization and project monthly limits; an "Enforce a hard limit" toggle makes calls fail with 429 after the limit; alerts only notify; enforcement is not instantaneous, so spend can slightly overshoot. | A limit set without the toggle is only an alert. | A (S50) |
| Anthropic Console spend limits | Cost cap | Per-tier monthly spend limits; workspace-level spend and rate limits that must sit below the organization limit; no limits on the Default Workspace. | Create a named workspace per demo. | A (S50) |
| GPU MODE and Popcorn CLI (AMD x GPU MODE hackathon) | Kernel competition on provided hardware | US$1.1M prize pool; Phase 1 6 March to 6 April 2026, Phase 2 7 April to 15 May, awards 18 May. | Past event; check for the next round. | A (S31) |
| nanochat | Full-stack small-LLM training and leaderboard | MIT-licensed. `runs/speedrun.sh` is the reference 8xH100 run; `runs/runcpu.sh` runs on CPU or Apple silicon; leaderboard metric is wall-clock time to a GPT-2-grade CORE score (0.256525) with commit hashes per row. Logs MFU and tokens per second. | Record runs need an 8xH100 node. | A (S30) |
| PyTorch FSDP2 | Distributed training API | Official tutorial; the examples repo selects a backend per device so a CPU/gloo run is possible. | CPU runs verify wiring only. | A (S51 tutorial), B (commit) |
| Hugging Face Ultra-Scale Playbook | Parallelism and memory reference | Reports 4,000 or more scaling experiments up to 512 GPUs (per InfoQ). | Read via secondary coverage. | B (S52) |

### D6. Live endpoints versus repositories, and hardening (SQ5)

**What the evidence supports.** A live demo lowers a reviewer's cost of checking that the system runs (S46). Nothing found measures how much weight reviewers give it relative to a repository (D). The risks are documented: unbounded consumption (S10), hosting-policy change (S11), dead links (S42), and leaked keys (S17).

**Rule.** Replay-first, capped, and dated. A live path is an optional extra, never the only proof.

**Hardening checklist (Grade D synthesis; each item is anchored to the cited risk).**
- H1. Default to a replay mode that serves pre-computed outputs from the evaluation set. Live calls only through a rate-limited path or a bring-your-own-key path.
- H2. Use a dedicated provider project or workspace for the demo with a hard monthly cap and alert thresholds. Turn on OpenAI's hard-limit toggle; set an Anthropic workspace limit below the organization limit (S50).
- H3. Add per-IP and global rate limits, plus an application-level daily budget counter, because provider caps are not instantaneous (S10, S50).
- H4. Cap input length and output tokens; set timeouts and a concurrency limit (S10).
- H5. No side-effecting tools in public mode; use read-only sandbox data. (OWASP's 2025 list names LLM06 Excessive Agency, visible in the S10 page index; the LLM06 page itself was not opened, so the mitigation advice is Grade D.)
- H6. Keep secrets in the platform secret store, enable secret scanning, rotate any exposed key, and assume history is public (S17).
- H7. Leave telemetry content capture off in public mode and redact inputs (S22: content capture is opt-in).
- H8. Run direct and indirect (tool-output or document) injection tests in CI.
- H9. Provide a kill switch that forces replay-only.
- H10. Add an uptime monitor and a "last verified" date in the README.
- H11. Show a visible budget meter ("demo spend this month: $x of $y").
- H12. Publish an abuse contact and takedown path in `SECURITY.md`.
- H13. Document cold-start and sleep behavior (free CPU Spaces sleep, S13).
- H14. State a retirement plan: "demo retired on <date>; replay and traces remain."

**Platform decision tree.**
- No spend budget at all: a static Space or static site with replay and a recorded walkthrough (S11).
- Up to about US$10 a month: Railway Hobby at US$5 (S14) or a Hugging Face PRO Docker Space at US$9 (S12).
- Intermittent GPU: Modal with monthly credit (S15), or ZeroGPU after verifying quotas.
- Persistent GPU: rarely justified for a portfolio; if used, set auto-shutdown.

### D7. Observability by tier

| Tier | What telemetry competence looks like | Reviewer check |
|---|---|---|
| T0–T1 | Structured spans or logs with latency, tokens, and document IDs; five sanitized traces committed; one failing trace turned into an evaluation case | Open one trace and find its case in `eval_harness/` |
| T2 | OpenTelemetry or vendor instrumentation on every request; dashboards for latency, cost, and pass rate; at least one alert; weekly error analysis that creates regression cases; a stated retention approach | Recompute p95 and cost from the exported traces and match the README |
| T3 | Engine-side metrics (TTFT, ITL, queue time, KV-cache use) correlated with client-side timings; GPU metrics; profiler timelines | A client-versus-server timing reconciliation table |
| T4 | Contributions to or definitions of telemetry conventions; a documented definition of cost per successful task; adoption by others | External repos or posts using the definitions |

### D8. Large-scale systems experience on modest budgets (SQ6)

The aim is credible, scoped evidence, not simulated prestige. Each rung states what it proves and what it does not.

| # | Strategy | How, on a modest budget | Evidence ceiling | Does not prove | Sources |
|---|---|---|---|---|---|
| M1 | Memory and throughput model, validated | Use the Playbook's parallelism and memory arithmetic to predict per-GPU memory and throughput for a target configuration; validate against 1-GPU measurements | V1 | Cluster operations | S52 |
| M2 | CPU/gloo smoke tests | Launch several CPU processes to verify sharding, checkpoint, and resume logic of DDP or FSDP2 | V1 | Performance, NCCL, topology issues | S51 |
| M3 | Scaled-down single-GPU runs | Use nanochat's roughly 5-minute small-model scale and its scaling-law scripts; report MFU and tokens per second | V1 | Multi-node scaling | S30 |
| M4 | Leaderboards and open challenges | AMD x GPU MODE kernel competitions on organizer hardware; Anthropic's public take-home runs in a Python simulator and needs no GPU; nanochat record runs need an 8xH100 node, so most candidates contribute smaller-scale ablations and discussion | V2 | General engineering ability beyond the task | S02, S30, S31 |
| M5 | Compact reimplementation | A nano-vLLM-style engine (continuous batching, paged KV, prefix caching) in 1k to 2k lines; benchmark against vLLM on the same hardware and configuration. nano-vLLM's README reports 1,434 versus 1,362 tokens a second in one configuration on an 8 GB laptop GPU; Mini-SGLang is about 5k lines | V1 | Production readiness or general superiority | S28, S29 |
| M6 | Simulation and harness engineering | Validate load harnesses against the llm-d inference simulator; build and label a scheduling simulator; calibrate it on small real runs | V1 | Hardware performance | S27, S56 |
| M7 | Upstream contributions | Tests, benchmarks, bug fixes, or docs to vLLM, SGLang, Triton, or similar | V2 | Authorship of core design | S32 |
| M8 | One short rented multi-GPU session | A single measured 2- to 4-GPU tensor-parallel experiment with a cost log; for example 4 GPUs for 3 hours at about US$3.95 an hour is about US$47 (derived) | V1 | Sustained operations | S15 |

**Claim-language templates (Grade D).**
- "Measured on 1x <GPU> (<VRAM>): <metric>. Modelled for 8x <GPU> under assumptions A, B, C: <metric> (not measured)."
- "Simulated with the llm-d inference simulator: validates the load harness only."
- "Educational reimplementation; one configuration; not a production claim."

### D9. Reviewer rubric for candidate GitHub profiles

**Status: synthesized in this session (Grade D as an instrument), each dimension anchored to the cited evidence. No inter-rater reliability data exists.** No major employer was found publishing a GitHub-profile scoring rubric; the closest public artifacts are Anthropic's take-home design principles (S02), the Yan and Liu interview framework (S04), and vendor scorecard templates (S53, C).

Rate each dimension 0 to 3. Score = sum of weight times rating divided by 3.

| ID | Dimension | 0 | 1 | 2 | 3 | Anchors | Weights T0–1 / T2 / T3 / T4 |
|---|---|---|---|---|---|---|---|
| D-1 | Problem reality; model is load-bearing | Tutorial domain; swap test fails | Plausible domain, no data provenance | Documented real data and a non-AI or smaller-model baseline | Real users or third-party adoption; ablation against a non-AI baseline | S34, S35 | 15 / 10 / 8 / 5 |
| D-2 | Evaluation rigor | None or "vibes" | Off-the-shelf metric only | Own dataset from real failures; code graders; error analysis; regression suite in CI | Judge validated against human labels (TPR and TNR); trials with pass@k and pass^k; capability and regression split | S01, S05–S08 | 20 / 20 / 15 / 15 |
| D-3 | Reproducibility and CI | No run instructions | README steps | One command, pinned dependencies, container, green CI | CI gates on quality and latency thresholds; dated pins; artifacts; capped cost | S01, S16 | 15 / 12 / 12 / 10 |
| D-4 | Performance and cost accounting | None | Anecdotal timing | Percentiles, tokens, dollars per request, hardware and concurrency disclosed, warm and cold separated | Sweeps, goodput under SLO, client-saturation check, repeats with spread, cost per successful task | S09, S26, S27 | 8 / 12 / 20 / 15 |
| D-5 | Observability | None | Print logs | Traces with token, latency, cost; sanitized exports committed | Trace-to-evaluation loop closed; dashboards and alert; retention approach | S18–S22 | 5 / 10 / 8 / 5 |
| D-6 | Reliability, safety, abuse resistance | Open endpoint or leaked secrets | Basic auth only | Rate limits, caps, hard spend limit, timeouts, injection tests | Red-team suite in CI, kill switch, threat model, postmortem | S10, S17, S50 | 5 / 10 / 7 / 5 |
| D-7 | Engineering hygiene and authorship | Single commit or forked tutorial | Some tests, sparse history | Iterative history, tests, ADRs, AI use disclosed | Defensible line by line; external review trail | S03, S34 | 15 / 10 / 7 / 5 |
| D-8 | Honesty and limitations | Claims only | Generic caveats | Failure taxonomy and explicit non-claims | Negative results and a published correction | S04 | 10 / 8 / 8 / 10 |
| D-9 | Third-party verifiability | Self-assertion | Live demo only | Independent reproduction or independent users | Merged upstream PRs, leaderboard row with commit, maintainer review | S02, S30–S32 | 5 / 5 / 10 / 15 |
| D-10 | Tier-specific depth and influence | Absent | Present but shallow | Solid for the tier | Exemplary for the tier | S04, S32 | 2 / 3 / 5 / 15 |

Each weight column sums to 100.

**Thresholds (arbitrary starting values).** Advance on portfolio evidence at 60 or above for T0–T1, 65 or above for T2, 70 or above for T3 and T4. A score from 50 up to the threshold means "advance with verification probes". Below 50, do not rely on the portfolio.

**Hard fails (any one caps the outcome at "do not advance on portfolio evidence").**
- HF-1. A live secret in the repository or its history.
- HF-2. A headline metric contradicted by the repository's own raw data, or not reproducible.
- HF-3. A copied or forked tutorial presented as original work.
- HF-4. A public endpoint with unbounded spend or unauthenticated side-effecting tools.
- HF-5 (interview stage). The candidate cannot explain core files, or contradicts their own AI-use disclosure.

**Five-minute review protocol.**
1. 0:00 to 1:00. README first screen: quantified, dated claims with an evidence block?
2. 1:00 to 2:00. CI: does the badge link to a recent run, and does the workflow gate evaluation?
3. 2:00 to 3:00. `eval_harness/`: dataset card, graders, calibration report, error analysis.
4. 3:00 to 4:00. `benchmarks.md` and `bench/results/`: hardware, percentiles, repeats, raw data present?
5. 4:00 to 5:00. Commit history, `docs/PROCESS.md`, a quick search for key patterns; decide advance, probe, or pass.

**Interview verification probes (Grade D, adapted from S04's project deep-dive).** Pick one README number and ask the candidate to regenerate it; ask for a failing trace and the case it became; ask what changes at 10 times the load; ask them to alter a grader live and predict the effect.

**Calibration protocol before adoption.** Three reviewers independently score the same ten public repositories; compute agreement; revise anchors where raters diverge; repeat. Record the revision log.

### D10. Market context and source-quality notes

- **Market context.** Stanford's Digital Economy Lab reports, in a revised analysis, a relative employment decline of about 16% for ages 22 to 25 in the most AI-exposed occupations; coverage cites software developers aged 22 to 25 at nearly 20% below their late-2022 peak, and the authors caution that factors other than generative AI may contribute (S48; figures via secondary coverage, C). Entry slots appear scarce, which raises the value of clear signals. No source links portfolio quality to outcomes (D).
- **Mechanism evidence on screening.** Early GitHub-hiring research found employers examine traces that are cheap to verify (S46, interview study, 2013, pre-GenAI). A University of Michigan study reports that adding mildly favorable information can lower an impression when a single résumé is judged alone, and that the best strategy differs when résumés are compared side by side (S47). A student thesis reports a failed replication of the dilution effect in personnel selection (S47, C/D). Automated screens may add noise: a September 2026 preprint reports that LLM-based screening is sensitive to presentation (S54, abstract-level reading, C).
- **Source quality.** Most negative-signal sources are SEO or vendor content (S37 to S43). Several use first-person anecdotes that cannot be verified (S41). The highest-provenance hiring evidence is a named hiring manager's public post (S34), an engineering post from a lab on its own evaluation design (S01, S02), and employer job postings (S32, S33).


---

## 7. Open Questions & Risks

### 7.1 Searched, not found (honest gaps)

| # | Item sought | Result |
|---|---|---|
| NF1 | A controlled study or résumé audit showing a penalty for listing generic AI-wrapper or tutorial repos versus listing no GitHub | Not found after searching hiring-signal literature, Hacker News and Reddit mirrors, and practitioner blogs. Only anecdote and a contested mechanism. |
| NF2 | A public corpus of postmortems of rejected GenAI portfolios | Not found beyond one detailed anecdote (S35) and several comments (S36). |
| NF3 | A published GitHub-profile scoring rubric from a major lab or employer | Not found. Found interview frameworks (S04), take-home design principles (S02), and vendor scorecard templates (S53). |
| NF4 | Hiring-manager interviews | Not possible with the available tools. Proxies used (S34, S04, postings). |
| NF5 | Measured effect of a live demo on callbacks or offers | Not found. |
| NF6 | Whether any employer lists "generic RAG repos" as an explicit screening criterion | Not found. |
| NF7 | First-party OpenTelemetry GenAI spec page | Not opened; relied on secondary summaries (S22). |
| NF8 | Canonical `modal.com/pricing` | Not opened; a non-canonical mirror and secondary sources were used (S15). |
| NF9 | Maxim AI free-tier terms | Not verified. |
| NF10 | GPU-enabled GitHub Actions runner availability and price | Not verified. |
| NF11 | Current ZeroGPU hardware and daily quotas | Sources conflict; unresolved (D5). |
| NF12 | Locust specifics | Snippet-level only. |

### 7.2 Open questions

- **OQ1.** Does a net penalty for generic repos exist? A test would be a blinded reviewer experiment: matched profiles with and without generic repos, scored by hiring managers, or a matched-résumé audit across real postings (Grade D, design suggestion).
- **OQ2.** What share of hiring managers open GitHub at all, by company size, role, and region? Unknown.
- **OQ3.** How much weight do reviewers give a live demo relative to a repository? Unknown.
- **OQ4.** Does the D9 rubric predict hiring-manager judgment or job performance? Untested; needs the calibration protocol.
- **OQ5.** How fast will AI-assisted generation erode trust in evaluation artifacts through 2027? Anthropic's take-home history suggests a continuing shift toward novel and externally verifiable work (S02).
- **OQ6.** When will OpenTelemetry's GenAI attributes stabilize, and will names change? Unknown (S22).
- **OQ7.** Do these findings transfer across markets? Several sources are US- or India-market content; the requester's region was not used to filter.

### 7.3 Risks

- **K1. Perishability.** Pricing, free-tier policy, and tool ownership changed repeatedly in 2025–2026 (F11). Re-verify D5 before acting.
- **K2. Source echo.** Many negative-signal posts repeat one another (S38 to S43). Convergence among them is weaker evidence than it looks.
- **K3. Goodhart.** Once evidence-block patterns spread, they can be faked. The verifiability ladder and HF-2 are the mitigations; V2 and V3 are costly to fake.
- **K4. Cost overrun.** Provider caps are not instantaneous (S50), so keep application-level counters and a low cap.
- **K5. Over-indexing on evaluation.** A portfolio does not replace coding skill, system design, or referrals (objection O2).
- **K6. Role mismatch.** R3 and R4 suit infrastructure and performance roles (S32); applied-AI roles may value R2 more.
- **K7. Data and licence exposure.** Datasets with personal data or restrictive licences, and committed traces, can leak data. Review before publishing.
- **K8. Conflict of interest.** S01 to S03 are Anthropic first-party sources and the author is an Anthropic model. See objection O8.
- **K9. Equity.** Even with low cash caps, 6 to 10 weeks of unpaid time is a barrier. R1 is sized for part-time work for this reason.

### 7.4 Strongest objections an expert would raise, and what the evidence says

| # | Objection | Evidence for | Evidence against | Effect on this memo |
|---|---|---|---|---|
| O1 | "Hiring managers rarely open GitHub, so the negative-signal question is moot." | Reports that some managers stopped reviewing junior portfolios (S36); a blog claim that most never look (S41); a recruiting platform arguing GitHub is a poor filter (S42). | A named hiring manager reviews GitHub in about 30 seconds (S34); early research found employers examine cheap-to-verify traces (S46); the one postmortem shows a reviewer who did look and react (S35). | Claims are scoped to reviewers who open the repo; the keyword and ATS caveat is kept (F1). |
| O2 | "Hiring turns on coding interviews, system design, and referrals; artifacts are second-order." | Vendor-described loops include live coding (S40); a commenter says projects matter only after a résumé is opened (S35); a hiring manager reports dropping take-homes because of AI (S45). | Yan and Liu's loop includes an inference-endpoint coding exercise and a deep-dive on the candidate's own project (S04); S34 treats the portfolio as the résumé. | Accepted. The recommendation raises signal conditional on review; it does not replace other stages. |
| O3 | "AI makes dashboards and READMEs cheap to fake, so these artifacts carry little signal." | Models matched Anthropic's take-home under time limits (S02); sources list "vibe-coded" fingerprints (S43); S34 claims to spot slop. | The same Anthropic post reports humans still beat the model at unlimited time and publishes an open challenge (S02); V2 and V3 evidence is costly to fake. | Accepted. This is why the standard centres on the verifiability ladder and `PROCESS.md`. |
| O4 | "RAG is the most requested skill; steering candidates away from RAG repos is harmful." | RAG appears in about a third to 40% of postings (S33); some guides call it the best first project (S39). | The flagged pattern is unmeasured RAG, not RAG (S35, S37, S38). | Accepted. The advice is to retrofit RAG repos with measurement (4.2, R1), not to avoid them. |
| O5 | "Small-hardware results are not real distributed experience; infrastructure employers will discount them." | Infrastructure postings emphasize upstream PRs and shipped performance features (S32); nano-vLLM numbers are one configuration and educational (S28). | D8 labels each rung's ceiling and ranks V2 upstream work highest; nanochat itself uses small experimental scales (S30). | Accepted in part. D8 lists "does not prove" for every rung. |
| O6 | "The rubric is arbitrary and unvalidated." | It is a synthesis; weights and thresholds are untested (D9). | Each dimension is anchored to cited practice, and a calibration protocol is included. | Accepted; labelled Grade D as an instrument. |
| O7 | "The source base is SEO and AI-generated content echoing a meme; the premise may be folklore." | Many near-identical claims in low-provenance posts (S41 to S43); a dated trivia screen failed within weeks (S38 versus S49). | Independent primary signals exist: S34, S35, S01, S02, S04. | Accepted. The premise stays unverified (F1). |
| O8 | "Anthropic-heavy primary sources bias the evaluation advice." | S01 to S03 are first-party; the author is an Anthropic model. | Zheng et al. (S08), Husain (S05), Langfuse (S07), and Yan and Liu (S04) independently corroborate the same practices. | Partly mitigated; disclosed in section 2. |
| O9 | "A live demo is the one artifact reviewers actually click; discouraging it harms candidates." | Low verification cost (S46). | Documented risks (S10 to S13, S17). | Rejected as a misreading. The advice is replay-first plus an optional capped live path. |

---

## 8. Delta (belief changes)

### 8.1 Priors

| ID | Prior | Evidence found | Direction | Posterior |
|---|---|---|---|---|
| P1 | Low-signal 75%; "net penalty is evidenced" 30% | Many practitioner sources; one n=1 postmortem (S35); a contested dilution mechanism (S47); no controlled study; some sources praise RAG projects (S39); many reviewers may never open repos (S36, S41). | **Updated (narrowed)** | Low-signal at the hiring-manager stage about 70% (C); "net penalty versus nothing" is evidenced at about 25% (D). Premise remains unverified. |
| P2 | 70% | Anthropic, Yan and Liu, and Husain agree on evaluation (S01, S04, S05); postings: 59.7% of AI-first roles (S33), 68% of companies (S33); one sample found only 12 of 100 (S33). | **Confirmed, magnitude uncertain** | About 80% that evaluation is the most consistently cited separator. |
| P3 | 65% | Hosting-policy change (S11), unbounded-consumption risk (S10), spend-cap behavior (S50); no data on demo weight. | **Confirmed (risk); unresolved (weight)** | About 70% on the liability claim; weight unknown. |
| P4 | 70% | Postings ask for upstream PRs, shipped performance features, maintainer relationships, technical writing (S32); AICE (S04); Anthropic's open challenge (S02). | **Confirmed** | About 80%. |
| P5 | 60% | Patterns exist (S02, S28 to S31, S51); reviewers' weighting unmeasured; infrastructure postings emphasize upstream work (S32). | **Confirmed with scoping** | About 65%. |

### 8.2 Recalled facts tested against sources

| # | Recalled claim | Result | Direction | Grade now |
|---|---|---|---|---|
| RF1 | Hugging Face Spaces offers free CPU hosting for Gradio and Docker apps | Current docs: only Static Spaces are free; Gradio and Docker on compute need PRO; free accounts get up to 2 ZeroGPU Gradio Spaces (S11) | **Contradicted (X)** | A |
| RF2 | ClickHouse acquired Langfuse in January 2026 | Confirmed by both companies' posts (S18) | Confirmed | A |
| RF3 | Promptfoo joined OpenAI in March 2026 and stays MIT | Confirmed via a README copy and secondary coverage (S23) | Confirmed | B |
| RF4 | Cloudflare acquired Replicate | Confirmed via secondary coverage (S24) | Confirmed | B |
| RF5 | Modal's Starter plan includes US$30 monthly credit | Confirmed on a mirror of the pricing page (S15) | Confirmed | B |
| RF6 | OpenTelemetry GenAI conventions are "experimental" | Status is "Development"; the conventions moved repositories on 2026-06-12; many blogs wrongly say stable (S22) | **Updated** | B |
| RF7 | GitHub Actions is free for public repositories | Confirmed; a self-hosted-runner fee was announced then postponed (S16) | Confirmed, updated | A/B |
| RF8 | Arize Phoenix is open source | Source-available under Elastic License 2.0, not OSI-approved (S19) | **Updated** | A |
| RF9 | LangSmith's free tier gives 5,000 traces a month | Confirmed; also a hard cap for personal organizations, 14-day base retention, and Enterprise-only self-hosting (S20) | Confirmed, updated | A |
| RF10 | The "dilution effect" is an established résumé finding | Documented but contested, and dependent on separate versus joint evaluation (S47) | **Updated** | B/C |
| RF11 | Hiring managers reliably flag RAG chatbots as red flags | Flagged when unmeasured; RAG itself is widely requested (S33, S35, S37, S39) | **Updated** | C |
| RF12 | OpenAI budgets are alerts only | Current docs offer an "Enforce a hard limit" toggle (S50) | **Updated** | A |
| RF13 | About 100 traces for error analysis and about 50 pass and 50 fail labels for judge validation | Matches the Husain-derived audit guidance read via a mirror (S06) | Confirmed | B |

---

## 9. Sources & Evidence Ledger

URLs were copied from search results or fetches during the session on 2026-10-21. "Read as" says how the page was read: **fetched** (full page) or **excerpt** (search excerpt only). Where a mirror or secondary source was used instead of the canonical page, the grade reflects that. Quoted phrases were kept short; all other material is paraphrased.

| ID | Source (title or description) | URL | Type | Grade | Read as | Supports |
|---|---|---|---|---|---|---|
| S01 | Anthropic Engineering, "Demystifying evals for AI agents" (published 2026-01-09, modified 2026-03-18) | https://anthropic.com/engineering/demystifying-evals-for-ai-agents | First-party engineering post | A | fetched | F3, F4, D2, R2 |
| S02 | Anthropic Engineering, "Designing AI-resistant technical evaluations" (2026-01-21, modified 2026-10-18); open take-home repo linked from the page: `anthropics/original_performance_takehome` | https://anthropic.com/engineering/AI-resistant-technical-evaluations | First-party engineering post | A | fetched | F8, F10, D8, R3, R4, O3 |
| S03 | Anthropic, "Guidance on Candidates' AI Usage" | https://www.anthropic.com/candidate-ai-guidance | Employer policy | A | excerpt | F8, AP-6, PA-12 |
| S04 | Eugene Yan and Jason Liu, "How to Interview and Hire ML/AI Engineers" (2024) | https://eugeneyan.com/writing/how-to-interview/ | Practitioner framework | A (content); 2024 date | fetched | F3, F9, D2, D9, R4 |
| S05 | Hamel Husain, AI Evals FAQ: "What parts of evals can be automated with LLMs?" (2025-07-24) and FAQ index | https://hamel.dev/blog/posts/evals-faq/what-parts-of-evals-can-be-automated-with-llms.html ; https://hamel.dev/blog/posts/evals-faq/ | Practitioner guidance | A (content) | excerpt | F3, F4, D2 |
| S06 | `hamelsmu/evals-skills`, eval-audit skill (registry mirror of a GitHub repo) | https://tessl.io/registry/skills/github/hamelsmu/evals-skills/eval-audit | Mirror of repo | B | excerpt | F4, PA-04, R1 |
| S07 | Langfuse blog, "Error Analysis to Evaluate LLM Applications" (2025-08-29) | https://langfuse.com/blog/2025-08-29-error-analysis-to-evaluate-llm-applications | Vendor blog adapting S05 | B | excerpt | F4 |
| S08 | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023) | https://arxiv.org/html/2306.05685v4 ; https://neurips.cc/virtual/2023/poster/73434 | Peer-reviewed paper | A | excerpt | F4, D2 |
| S09 | Chandrasekar and Kramberger, "Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks" (arXiv 2605.24217) | https://arxiv.org/pdf/2605.24217 | Preprint | B | excerpt (abstract) | F5, R3, R4, D5 |
| S10 | OWASP GenAI Security Project, "LLM10:2025 Unbounded Consumption" (page index also lists LLM06:2025 Excessive Agency) | https://genai.owasp.org/llmrisk/LLM10/ | Standards body | A | excerpt | F6, AP-9, D6 |
| S11 | Hugging Face Hub docs, "Spaces Overview" | https://huggingface.co/docs/hub/en/spaces-overview | Official docs | A | fetched | F6, F11, AP-2, D5, D6, RF1 |
| S12 | Hugging Face, Pricing (PRO US$9 a month; hardware prices) and Hub billing docs | https://huggingface.co/pricing ; https://huggingface.co/docs/hub/billing.md | Official pages | A | excerpt | F6, D5, D6 |
| S13 | `huggingface_hub` docs, Space runtime (free hardware sleep) | https://huggingface.co/docs/huggingface_hub/en/package_reference/space_runtime.md | Official docs | A | excerpt | F6, AP-2, D6 |
| S14 | Railway docs, Pricing and Plans | https://docs.railway.com/pricing ; https://docs.railway.com/pricing/plans | Official docs | A | excerpt | D5, D6, R2 |
| S15 | Modal pricing (non-canonical mirror host); flexprice summary for egress change | https://frontend-deadbeef.modal.com/pricing ; https://flexprice.io/pricing-index/modal | Mirror; third party | B; egress C | excerpt | F10, D5, R3, D8 |
| S16 | GitHub Changelog, "Coming soon: Simpler pricing and a better experience for GitHub Actions" (2025-12-16); GitHub Resources, "2026 pricing changes for GitHub Actions"; Techzine on postponement | https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/ ; https://resources.github.com/actions/2026-pricing-changes-for-github-actions/ ; https://www.techzine.eu/news/devops/137396/github-bends-to-criticism-and-delays-paid-self-hosting-of-runners/ | Official; news | A; status B | excerpt | F11, D5, PA-05 |
| S17 | GitHub Docs, "Supported secret scanning patterns" | https://docs.github.com/en/code-security/reference/secret-security/supported-secret-scanning-patterns | Official docs | A | excerpt | AP-9, D6, PA-09 |
| S18 | Langfuse, "Langfuse joins ClickHouse"; ClickHouse announcement; Langfuse engineering clarifications (dated 2026-08-20); Langfuse pricing | https://langfuse.com/blog/joining-clickhouse ; https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability ; https://langfuse.com/resources/engineering/clarifications ; https://langfuse.com/pricing.md | First-party | A | excerpt | F7, F11, D5, RF2 |
| S19 | Arize docs, Phoenix self-hosting license; Railway template page for Phoenix | https://arize.com/docs/phoenix/self-hosting/license ; https://railway.com/deploy/arize-phoenix | Official docs; template | A; template B | excerpt | F7, D5 |
| S20 | LangChain, LangSmith pricing; LangSmith billing docs; ZenML pricing explainer | https://www.langchain.com/pricing-langsmith ; https://docs.langchain.com/langsmith/billing/index.html ; https://www.zenml.io/blog/langsmith-pricing | Official; third party | A; change C | excerpt | F7, D5 |
| S21 | TruLens repository and site | https://github.com/truera/trulens ; https://trulens.org | Official | A | excerpt | F7, D5 |
| S22 | OpenTelemetry GenAI conventions status: Dash0 explainer; DEV Community post | https://www.dash0.com/knowledge/opentelemetry-genai-semantic-conventions-explained ; https://dev.to/azena-ai/opentelemetrys-genai-semantic-conventions-are-not-stable-yet-heres-what-actually-shipped-in-2026-3mke | Secondary | B | excerpt | F7, F11, D5 |
| S23 | Promptfoo README copy noting it joined OpenAI (March 2026); secondary summary | https://github.com/DeepDocs-eval/promptfoo ; https://www.dsebastien.net/promptfoo/ | Fork copy; blog | B | excerpt | F11, D5, R2 |
| S24 | Coverage of Cloudflare's acquisition of Replicate | https://www.thestack.technology/cloudflare-to-buy-replicate-cto-were-building-the-ai-cloud/ ; https://rywalker.com/research/replicate | News; blog | B | excerpt | F11, D5 |
| S25 | Shields.io endpoint-badge docs (mirror); Dynamic Badges action | https://shields.mitmproxy.org/badges/endpoint-badge ; https://github.com/Schneegans/dynamic-badges-action/ | Docs mirror; action | B | excerpt | PA-05, D5 |
| S26 | Grafana k6 docs: when thresholds fail; validate thresholds | https://grafana.com/docs/learning-hub/k6-performance-testing/03-establishing-a-baseline/19b-when-thresholds-fail/ ; https://grafana.com/docs/learning-paths/establish-k6-baseline/validate-thresholds/ | Official docs | A | excerpt | F5, D5 |
| S27 | LLM benchmarking tools: inference-perf; BentoML benchmark guide; Tenstorrent benchmarking doc (cold-start example); GuideLLM PR #328 (simulator use); Spheron guide; AIPerf guide | https://github.com/kubernetes-sigs/inference-perf ; https://bentoml.com/llm/inference-optimization/llm-performance-benchmarks ; https://github.com/tenstorrent/tt-inference-server/blob/main/docs/benchmarking_tools.md ; https://github.com/vllm-project/guidellm/pull/328/files ; https://www.spheron.network/blog/load-testing-your-llm-endpoint-finding-your-real-concurrency/ ; https://lucaberton.com/blog/nvidia-aiperf-llm-inference-benchmarking-guide/ | Mixed | A (inference-perf); B; C (Spheron, AIPerf guide) | excerpt | F5, D5, R3, M6 |
| S28 | nano-vLLM README copy and summary (about 1,200 lines; laptop-GPU benchmark) | https://github.com/vovovovovov/nano-vllm ; https://www.sourcepulse.org/projects/5172490 | Repo copy; summary | B | excerpt | F10, D8 |
| S29 | LMSYS blog, Mini-SGLang (2025-12-17) | https://lmsys.org/blog/2025-12-17-minisgl | First-party blog | A/B | excerpt | F10, D8 |
| S30 | nanochat repository and README (leaderboard, scripts, CPU run); mirror with leaderboard rows; third-party summary | https://github.com/karpathy/nanochat ; https://raw.githubusercontent.com/karpathy/nanochat/master/README.md ; https://cnb.cool/IndexMirror/nanochat ; https://emelia.io/hub/nanochat-karpathy | Repo; mirror; blog | A (README); B (rows); C (summary) | excerpt | F10, D4, D5, D8 |
| S31 | AMD, "New GPU MODE virtual hackathon: E2E model speedrun" (2026) | https://www.amd.com/en/developer/resources/technical-articles/2026/new-gpumode-virtual-hackathon--e2e-model-speedrun.html | Vendor announcement | A | excerpt | F10, D5, D8 |
| S32 | Employer job postings (statements of requirements): NVIDIA Principal AI Inference; NVIDIA Senior AI Inference; Inferact (vLLM); River AI (GPU kernels); AMD (Triton kernels); Together AI; Sciforium; Intel | https://inferencejobs.com/companies/nvidia/jobs/principal-software-engineer-ai-inference ; https://meet4jobs.jobboardly.com/jobs/senior-software-engineer-ai-inference-f00b5202 ; https://seedtable.com/jobs/14880 ; https://jobs.generalcatalyst.com/companies/river-ai-2/jobs/93095676-software-engineer-gpu-kernels ; https://jobs.aihub.masstech.org/companies/amd/jobs/68392204-ml-ai-software-engineer-triton-gpu-kernel-optimization ; https://job-boards.greenhouse.io/togetherai/jobs/4687884007 ; https://www.wearedevelopers.com/jobs/48412-gpu-kernel-engineer.md ; https://www.iagora.com/work/en/offer/job-china-it/6339726 | Postings (job-board copies) | B | excerpt | F9, D3, D8, R3, R4 |
| S33 | Job-posting analyses: Grigorev AI Engineering Field Guide (6,964 postings); Axial (43,480 US postings); aijobprep (3,647 postings, 198 companies); AI Shipping Labs; AI Engineering Insider (100 postings, May 2026) | https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/role/02-skills.md ; https://axialsearch.com/insights/ai-engineering-careers ; https://aijobprep.app/ai-engineer-skills ; https://aishippinglabs.com/blog/what-is-an-ai-engineer-based-on-job-descriptions ; https://aiengineeringinsider.substack.com/p/the-ai-engineer-job-market-has-moved | Third-party analyses | B (Grigorev, Axial); C (rest) | excerpt | F2, F3, O4 |
| S34 | Towards Data Science, "How to Get Hired in the AI Era" (hiring manager at DareData with 500+ interviews; 2026-05-01) | https://towardsdatascience.com/how-to-get-hired-in-the-ai-era/ | Named practitioner | B | excerpt | F1, F8, AP-6, O1 |
| S35 | r/cscareerquestionsIN postmortem: a candidate with five AI demos, zero interviews, and a hiring manager's review (mirror; date shown as 2025-11-17 on one mirror, not independently verified) | https://rl.klein.ruhr/r/cscareerquestionsIN/comments/1v478q9/i_kept_building_ai_projects_and_still_got_zero/ | Community anecdote (n=1) | C | excerpt | F1, AP-1, O1, O2 |
| S36 | Reddit snapshot, "Are junior portfolios being replaced by AI-generated noise?" (2025-12-26) | https://reddit.sentinel-team.org/posts/1ps4yet/snapshots/2025-12-26T18%3A31%3A31.46825Z | Community thread | C | excerpt | F1, O1 |
| S37 | Medium (Write a Catalyst), "The AI Portfolio Projects That Instantly Tell Recruiters You're a Junior" | https://medium.com/write-a-catalyst/the-ai-portfolio-projects-that-instantly-tells-recruiters-youre-a-junior-f9629b9a38da | Blog | C | excerpt | F1, F2, AP-1 |
| S38 | Digital Applied, AI developer hiring skills 2026 (red-flag list; "Sonnet 5" screen; published 2026-05) | https://www.digitalapplied.com/blog/ai-developer-hiring-skills-that-matter-2026 | Vendor blog | C | fetched | F12, AP-4, AP-5, AP-7, AP-8 |
| S39 | Upskillist portfolio guide; Medium (jhquilty) generative-AI portfolio guide; Dataquest AI projects | https://www.upskillist.com/blog/10-ai-portfolio-examples-impress-recruiters/ ; https://medium.com/@jhquilty99/how-to-build-a-generative-ai-portfolio-that-actually-gets-you-hired-c64ace605001 ; https://www.dataquest.io/blog/ai-projects/ | Blogs | C | excerpt | F2, AP-3, O4 |
| S40 | techinterview.org, AI portfolio and AI-engineer interview posts | https://www.techinterview.org/post/3233475399/ai-portfolio-built-with-ai-2026-interviews/ ; https://www.techinterview.org/post/3233476824/ai-engineer-interview-rag-agents-evals/ | Blog | C | excerpt | O2 |
| S41 | bswen, GitHub mistakes and portfolio posts (first-person narratives; unverifiable) | https://docs.bswen.com/blog/2026-03-29-github-mistakes-job-applications ; https://docs.bswen.com/blog/2026-03-29-github-portfolio-hiring-help | Blog | C/D | excerpt | F1, O1, O7 |
| S42 | Instahyre GitHub checklist; Underdog.io on GitHub and hiring (two posts) | https://resources.instahyre.com/blog/github-profile-checklist/ ; https://underdog.io/blog/why-github-wont-help-you-with-hiring ; https://underdog.io/blog/what-hiring-managers-look-for-on-github | Vendor blogs | C | excerpt | F1, F6, AP-9, O1 |
| S43 | SlateGit and CoderCops posts on AI-generated repos and GitHub as a hiring signal | https://slategit.com/blog/ai-generated-github-projects-recruiters-suspicious-2026 ; https://blog.codercops.com/blog/github-profile-as-hiring-signal-2026 | Vendor blogs | C | excerpt | F8, AP-6, O3 |
| S44 | IEEE Spectrum, AI tools in interviews | https://spectrum.ieee.org/ai-tools-interviews | Magazine | B | excerpt | F8 |
| S45 | "AI Broke Recruiting" (Substack) | https://acflippo.substack.com/p/ai-broke-recruiting | Blog | C | excerpt | O2 |
| S46 | Marlow and Dabbish, "Activity Traces and Signals in Software Developer Recruitment and Hiring" (CSCW 2013); arXiv summary | https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf ; https://arxiv.org/pdf/2303.14702 | Peer-reviewed (interview study) | A (existence); B (mechanism, 2013, small sample) | excerpt | F6, Recommendation, O1 |
| S47 | University of Michigan News, "Building your résumé: sometimes less is more"; Illinois LAS news (2009, preliminary); Lund student thesis on non-replication | https://news.umich.edu/building-your-resume-sometimes-less-is-more ; https://las.illinois.edu/news/2009-05-01/want-job-better-rethink-facebook-profile ; https://lup.lub.lu.se/student-papers/record/9089249 | University news; thesis | B; C; C/D | excerpt | F1, D10 |
| S48 | Stanford Digital Economy Lab, "Canaries in the Coal Mine" update; LeadDev summary; DEV Community summary | https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers ; https://leaddev.com/hiring/young-devs-steepest-losses-exposed-roles-stanford-study-finds ; https://dev.to/prpatel05/the-entry-level-job-is-the-canary-2m3b | Research lab; news | A (existence); B/C (figures) | excerpt | D10 |
| S49 | Claude release timing: 9to5Mac (Sonnet 5); Vercel AI Gateway model page; ITDaily (Sonnet 5.5) | https://9to5mac.com/?p=1058997 ; https://vercel.com/ai-gateway/models/claude-sonnet-5/about ; https://itdaily.com/news/software/claude-sonnet-5-5/ | News; platform page | B | excerpt | F12, O7 |
| S50 | OpenAI "Spend limits" guide; Anthropic API rate and spend limits docs; Digital Applied comparison | https://developers.openai.com/api/docs/guides/spend-limits ; https://docs.anthropic.com/claude/reference/rate-limits ; https://www.digitalapplied.com/blog/ai-spend-controls-compared-usage-caps-2026 | Official docs; vendor blog | A; C | excerpt | F6, D5, D6, PA-07, PA-09 |
| S51 | PyTorch FSDP2 tutorial; `pytorch/examples` commit selecting a backend per device | https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html ; https://github.com/pytorch/examples/commit/cf74c6f23ca1b205ec75415048eaafbcb8ca58c5 | Official docs; repo commit | A; B | excerpt | F10, D8 |
| S52 | InfoQ coverage of the Hugging Face Ultra-Scale Playbook | https://www.infoq.com/news/2025/03/huggingface-ultra-scale-playbook | News | B | excerpt | D5, D8, R3 |
| S53 | Hirevire AI-engineer interview scorecard (vendor template) | https://hirevire.com/interview-ai-scorecard/ai-engineer | Vendor template | C | excerpt | D9 |
| S54 | arXiv 2609.16517, résumé perturbations and LLM screening | https://arxiv.org/pdf/2609.16517 | Preprint | C | excerpt (abstract) | D10 |
| S55 | CEUR short paper on evaluation bias; summary of an anchoring-bias study in LLM judges | https://ceur-ws.org/Vol-4275/short14.pdf ; https://themodelwire.com/article/llm-judges-show-systematic-bias-from-prior-scores-in-production-evaluations-01M10JT3JWYHRS4VDP58G85NGM | Workshop paper; news summary | C | excerpt | F4 |
| S56 | llm-d inference simulator, referenced as the container image `ghcr.io/llm-d/llm-d-inference-sim` in GuideLLM PR #328 (S27) and cited in S09; repository page not opened | (see S27 and S09) | Referenced tool | B | excerpt | F10, D5, D8, R3 |

*End of file.*
