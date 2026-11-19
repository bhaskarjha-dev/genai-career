---
id: tracks.career-transitions
title: "Career Transitions into GenAI: Roadmaps from Nine Starting Backgrounds"
content_type: guide
stage: 11
status: published
last_verified: 2026-11-19
review_by: 2026-12-03
summary: "Roadmaps into GenAI from nine starting backgrounds (including DevOps/SRE, product managers, India IT-services engineers and students): what transfers, traps, modelled timelines and gates G1–G4."
sources: [T0-06, T2-01, T0-01, T0-12, T0-67]
roles: [ai-engineer, applied-ai-engineer, ai-product-engineer, ai-evaluation-engineer, forward-deployed-engineer, ai-infrastructure-engineer, inference-engineer, ml-platform-engineer, ai-enablement-engineer, ai-product-manager, ai-governance-lead, domain-evaluation-specialist, ai-solutions-architect, applied-scientist, research-engineer]
geos: [global, us, uk, eu, canada, india]
tags: [career-transition, roadmap, upskilling, evals, portfolio, timelines, milestone-gates, devops, sre, product-management, it-services, students, entry-level]
---

# Career Transitions into GenAI

> Roadmaps into GenAI from nine starting backgrounds (including DevOps/SRE, product managers, India IT-services engineers and students): what transfers, traps, modelled timelines and gates G1–G4.

**Dates and grades.** Routes 1–5, gates G1–G4 and the time model come from [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) (21 October 2026); skills-stage week plans and the viability matrix come from [T2-01](../../research/sessions/T2-01-tier-calibrated-execution-playbooks.md) (25 October 2026); Routes 6–9 (DevOps/SRE, product managers, India IT-services engineers, students and new graduates) and the entry-level market audit come from [T0-67](../../research/sessions/T0-67-transitions-devops-pm-it-services-students.md) (13 November 2026; 7 of 75 sources opened in full, 68 read as search extracts, which caps those rows at B). Market figures carry their own dates: re-verify US post-study visa rules (class V0, 14 days from live verification on 2026-11-19) and JobsPipe feeder counts (2026-11-02; class V1) by 2026-12-03, and pay figures by 2027-01-09. Grades (EGP-1.0): A primary or measured; B transparent secondary or extract-capped primary; C vendor or single source; D judgement; E unverifiable or not found; M model output; P practice-curated. **Every month count on this page is a model output, not cohort data:** no longitudinal study of GenAI career changers or measured time-to-first-offer exists for any of the nine backgrounds [D · T0-06.F9; E · T0-67 L379].

**Two kinds of tier.** *Hours tiers* A, B and C are your weekly study budget (T0-06). *Target tiers* T0 to T5 are employer and pay levels (T2-01). This page uses target-tier names only, because their band values are unmeasured and inconsistent ([ERRATA](../../research/ERRATA.md) U7, U14).

## The short answer

1. **Test an internal move first, and build in parallel — without assuming it is fast.** Spend 6–8 weeks seeking a scoped AI assignment or internal bridge programme at your employer. Employer-side vendor data show internal hires filling roles faster (about 20 days against 49 for external), and 27% of surveyed HR leaders report avoidable external hires from skills-data gaps, but candidate-side transition speed is unmeasured and the four Phase 0 practitioner accounts were not independently located [C employer-side; E candidate speed · T0-67 L142, L367; D · T0-06 L205].
2. **Move laterally; do not restart as a junior.** In Axial Search's US AI-engineering postings, 66% is the mid-level (35%) plus senior (31%) subtotal, while total individual-contributor postings sit near 86% (companion report dated 2026-05-22; the January–July 2026 window in T0-06 is unconfirmed) [C · T0-67 L54, L368]. Employment of 22–25-year-olds in the most AI-exposed US occupations stood 19% below counterfactual as of 2026-06-30 (Stanford Digital Economy Lab, August 2026 revision; descriptive, not causal, and shrinks under education controls), with no comparable gap for experienced workers [B · T0-67 L52, L369]. Prior tacit experience is the hedge [A/B · T0-06.F2].
3. **Commit to one route and one hours tier for 90 days, judge progress by gates G1–G4, and plan for a long search tail.** Re-plan at month 6 from your interview-funnel numbers [M · T0-06 L241]. As a general US base rate, August 2026 unemployment duration averaged 26.3 weeks (median 11.4 weeks), with 27.0% out for 27 weeks or more; budget a 6–12-month runway with a week-27 checkpoint [B · T0-67 L72, L223, L332].
4. **Match proof to the role's actual gate: evaluation for application and AI-PM roles, serving for inference and infrastructure.** Evaluation is the most-cited stack challenge (20% of survey respondents) [B · T0-06 L139], appears in 7 of 9 postings in one vendor AI-PM subgroup [C · T0-67 L63, L371] and is taught in early-career fellowships such as Claude Corps [B · T0-67 L321]. It is **not** universal: across 11 inference, SRE and MLOps posting extracts in T0-67, evaluation was absent while model-serving frameworks appeared in 11 of 11 and Kubernetes in 6 of 11 [B/M · T0-67 L62, L371].
5. **Plan on modelled months, conditional on success — and treat Routes 6–9 as unmeasured.** At 15–20 hours a week, T0-06's model gives about 6 months to a first offer for backend engineers, 7 for frontend and non-technical AI-adjacent routes, 8 for data scientists and PhDs, 11 for BI analysts and 22 for engineering from zero code [M · T0-06 L261–269]. No transition-time measurements exist for DevOps/SRE, PMs, IT-services engineers or students; any analogue is untested [E · T0-67 L327–332, L372]. Every modelled value assumes you persist and eventually succeed [T0-06 L375].
6. **Do not mix funnels.** Experience gates and proof differ sharply across tracks: frontier-lab AI PM asks 5–10+ years against ~3 years in enterprise AI teams [B · T0-67 L63, L154–155], FDE asks 5+ years with customer-facing deployment [B · T0-67 L63], inference roles ask 4–6+ years of systems/serving [B · T0-67 L62, L327], and fellowships split strictly by experience band [B · T0-67 L373; M · T0-06 L255].

## At a glance

```mermaid
flowchart LR
  bg["Your background"] --> route["One route and one hours tier for 90 days"]
  route --> internal["Internal ask, 6-8 weeks, in parallel"]
  route --> g1["G1 Measured v0, month 3"]
  g1 --> g2["G2 Operable v1, month 6"]
  g2 --> g3["G3 Second pattern and external proof, month 9"]
  g3 --> offer["G4 Offer or internal move, month 12"]
  g3 --> replan["G4 Funnel diagnosis and re-plan"]
  internal --> offer
```

Months are for hours tier B.

### Background router

| Background | What transfers | First targets | Modelled months, tier B (range) | Role hubs |
|---|---|---|---|---|
| Backend or systems, 5+ years | Testing, CI/CD, observability, rate limiting, caching [M · T0-06 L414] | Applied AI engineer, AI platform or infrastructure, FDE-adjacent, at your level | ~6 (3.5–8) | [AI Engineer](../02-roles/hubs/ai-engineer.md), [Applied AI](../02-roles/hubs/applied-ai-engineer.md), [AI Infrastructure](../02-roles/hubs/ai-infrastructure-engineer.md), [FDE](../02-roles/hubs/forward-deployed-engineer.md) |
| Data scientist | Error analysis, metric design, experimental design, judge validation [C · T0-06 L490] | AI engineer with an evaluation edge; evaluation-heavy roles | ~8 (5–11) | [AI Engineer](../02-roles/hubs/ai-engineer.md), [AI Evaluation](../02-roles/hubs/ai-evaluation-engineer.md), [ML Engineer](../02-roles/hubs/ml-engineer.md) |
| BI analyst | SQL, metric definitions, stakeholder communication [M · T0-06 L469] | Analytics-AI engineer; analytics engineering with GenAI scope as a bridge | ~11 (7–15) | [AI Engineer](../02-roles/hubs/ai-engineer.md) |
| Frontend or full-stack | UX for uncertainty, streaming interfaces, product intuition [M · T0-06 L544] | AI product or full-stack engineer; frontend-heavy FDE | ~7 (5–11) | [AI Product Engineer](../02-roles/hubs/ai-product-engineer.md), [Applied AI](../02-roles/hubs/applied-ai-engineer.md), [FDE](../02-roles/hubs/forward-deployed-engineer.md) |
| Non-technical, 5+ years in a domain, product or operations | Domain judgement for rubrics, golden sets, pilots and customers [C · T0-06.F7] | One lane: AI PM, AI ops or enablement, domain-evaluation lead, solutions or FDE-adjacent | ~7 (5–11) | [AI Product Manager](../02-roles/hubs/ai-product-manager.md), [Domain Evaluation](../02-roles/hubs/domain-evaluation-specialist.md), [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md) |
| Non-technical, engineering from zero code | Domain knowledge | Junior engineering, as a two-year plan | ~22 (15–34) | [AI Engineer](../02-roles/hubs/ai-engineer.md) |
| Academic or quantitative PhD who can code | Mathematics, statistics, experimental design, measurement rigour [M · T0-06 L658] | Applied AI engineer, applied scientist, research engineer; research scientist as upside | ~8 (5–12.5) | [Applied Scientist](../02-roles/hubs/applied-scientist.md), [Research Engineer](../02-roles/hubs/research-engineer.md) |
| DevOps, SRE or cloud engineer (Route 6) | Kubernetes, autoscaling, SLOs, observability, cloud ops [B · T0-67 L120–122] | Inference engineer, AI infrastructure, ML platform; FDE infra only with 5+ yr customer record | Unmeasured (unverified backend analogue ~6) [E · T0-67 L327] | [Inference Engineer](../02-roles/hubs/inference-engineer.md), [AI Infrastructure](../02-roles/hubs/ai-infrastructure-engineer.md), [ML Platform](../02-roles/hubs/ml-platform-engineer.md) |
| Product manager (Route 7) | Product discovery, metrics, shipping, stakeholder alignment [B · T0-67 L154–155] | Enterprise or mid-size AI PM first (~3 yr gate); frontier-lab AI PM after 5–10+ yrs and shipped LLM work | Unmeasured (unverified AI-adjacent analogue ~7) [E · T0-67 L328] | [AI Product Manager](../02-roles/hubs/ai-product-manager.md), [AI Evaluation](../02-roles/hubs/ai-evaluation-engineer.md), [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md) |
| IT-services engineer, India (Route 8) | Enterprise delivery, client integration, QA and cloud tooling [B · T0-67 L181–183] | Internal GenAI practice or bridge (2-quarter test), then GCC AI platform / enablement / applied AI at 4+ yrs | Unmeasured (unverified SWE analogue ~6–7) [E · T0-67 L329] | [Applied AI](../02-roles/hubs/applied-ai-engineer.md), [AI Enablement](../02-roles/hubs/ai-enablement-engineer.md), [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md) |
| Student or new graduate (Route 9) | Internships (in-person preferred), evaluated end-to-end project, campus placement [B · T0-67 L65, L88–89] | Internships and structured early-career SWE/data/AI programmes; avoid mass cold graduate applications | Schedule-bound by campus/internship cycle [E · T0-67 L330] | [AI Engineer](../02-roles/hubs/ai-engineer.md), [ML Engineer](../02-roles/hubs/ml-engineer.md), [FDE](../02-roles/hubs/forward-deployed-engineer.md) |

Months and targets for Routes 1–5: [M · T0-06 R2 L261–269]; Routes 6–9 targets and unmeasured status: [B/C/E · T0-67 L118–209, L327–330]. Experienced software engineers are the dominant feeder into AI-engineer titles and data scientists a steady second; "backend is fastest" cannot be tested with public data [B/D · T0-06.F3].

### Where each background has a high-volume corridor

| Background | High-volume corridor ● | Plausible but extended ◐ |
|---|---|---|
| Backend or systems | T1 Growth (fastest), T2 Senior (primary) | T3 Staff, 12–18 months |
| Data scientist or BI | T1 Growth (data scientists) | T0 Entry (BI only), T2 Senior (production gap) |
| Frontend or full-stack | T1 Growth (AI product engineer) | T2 Senior (senior AI product) |
| Non-technical | None | T0 Entry (evaluation, annotation), T1 Growth (AI PM, ops) |
| PhD or researcher | T2 Senior (applied scientist) | T1 Growth (applied engineering), T3 Staff (research engineer), T4 Elite (frontier lab) |

Every other cell is implausible within 12 months. The matrix is a design judgement [D · T2-01 L92–104], and it has five high-volume cells, not the "8–12 corridors" its key finding claims (ERRATA U9).

## The shared spine: four gates and an hours budget

Each route below specialises one spine: four pass/fail gates, due at months 3, 6, 9 and 12 at hours tier B. The deliverables are author-designed, and each maps to a hiring signal in the sources [M · T0-06 L389–398].

| Gate | Due (tier B) | Done when | How a stranger checks it |
|---|---|---|---|
| **G1 Measured v0** | Month 3 | A running LLM application (retrieval and/or tool use) over a real corpus or task from your domain; 50+ labelled eval cases, 30+ of them hand-written from real work, versioned with the code; 2+ baselines compared; an error taxonomy from 100+ reviewed traces, with counts; a "what broke" memo of 500+ words naming three failures | The README's headline eval numbers reproduce in under 30 minutes |
| **G2 Operable v1** | Month 6 | Evals run in CI on every prompt, model or retrieval change, with a regression threshold; any LLM judge validated on 100+ human-labelled examples, with agreement reported and one bias (position or verbosity) tested; tracing with p50/p95 latency and cost per request; deployed to 1+ real user other than you; one postmortem of a real regression, with the test that stops it recurring | CI badge and log, judge-agreement table, live URL or recorded demo, postmortem |
| **G3 Second pattern and external proof** | Month 9 | A second system with a different failure surface; one public write-up with numbers; one external contribution (pull request, talk or community review); 5+ mock loops of your target loop type; 15–20 targeted applications | Public links, mock-loop notes, an application tracker |
| **G4 Convert or re-plan** | Month 12 | 1+ offer or internal role change, **or** a written funnel diagnosis and a re-plan that changes loop type, level or tier | Offer letter, or the diagnosis reviewed by one practitioner |

**When a gate slips** [M · T0-06 L251, L400–405]:
- **G1 not passed by the end of month 4:** check adherence, then scope creep, then whether an eval set exists. Move to the next-longer tier before adding hours.
- **G2 not passed by month 8:** the system is probably over-scoped. Cut features; keep the evals and CI.
- **No screens after 15 targeted applications:** the problem is positioning or résumé signal, not skill. Get a practitioner to review the artifacts and the résumé.
- **Three failed take-homes:** invest in eval design and error analysis.
- **Failed system-design onsites:** practise system design and DSA for big-company loops, or retarget applied-AI loops.
- **Logged hours below 70% of plan for three consecutive weeks:** re-plan on the next-longer tier instead of pushing harder.

Start applying when roughly 70% of the build gates are passed [M · T0-06 L221]. For the G3 contribution, go discussion-first: AI-generated "slop" has turned the drive-by pull request from a hiring tactic into a liability [B · T0-12.F10].

### Hours tiers

| Tier | Nominal h/week | Adherence | Effective h/week | Fits | Share of average leisure: no child under 18 / child under 18 |
|---|---|---|---|---|---|
| A | 9 | 0.75 | 6.75 | Employed, caregiving or heavy workload | 29% / 38% |
| B | 17.5 | 0.75 | 13.1 | Employed and disciplined; the central planning case | 56% / 74% |
| C | 38 | 0.85 | 32.3 | Sabbatical, notice period, bench time, full-time programme | 121% / 160%: not possible alongside full-time work |

Parameters and shares are T0-06's model [M · T0-06 L341–345, L379–383]. The base is BLS time-use data: employed adults without a child under 18 averaged 4.5 hours of leisure a day in 2025, more than an hour above those with one [A · T0-06 L211]. Hours, not compute, are the binding constraint [A · T0-06.F10]; API credits plus a free notebook tier cover months 1–6 of application-layer work [M · T0-06 L233].

### Modelled months to a first offer

| Route | Tier A | Tier B | Tier C | Core hours: central (low–high) | Search lag, weeks |
|---|---|---|---|---|---|
| Backend or systems, 5+ years | ~10 (6–14) | **~6 (3.5–8)** | ~3 (2–4.5) | 250 (150–350) | 6 (4–8) |
| Data scientist | ~13 (9–19) | **~8 (5–11)** | ~5 (3–6.5) | 300 (200–450) | 11 (8–14) |
| BI analyst | ~18 (12–26) | **~11 (7–15)** | ~6 (4–8) | 450 (300–650) | 12 (8–16) |
| Frontend or full-stack | ~12 (8–18) | **~7 (5–11)** | ~4 (3–6) | 300 (200–450) | 9 (6–12) |
| Non-technical, AI-adjacent roles | ~10.5 (7–16) | **~7 (5–11)** | ~5 (3.5–8) | 200 (120–300) | 16 (12–24) |
| Non-technical, engineering from zero code | not meaningful (~39) | **~22 (15–34)** | ~12 (8–18) | 1,000 (700–1,500) | 20 (12–32) |
| PhD, applied roles | ~13 (9–20) | **~8 (5–12.5)** | ~5 (3–8) | 300 (200–450) | 12 (8–20) |

Source: [M · T0-06 L261–269, L347–355]. How to read it:
- **Formula:** weeks = core hours ÷ (nominal hours × adherence) + search lag; months = weeks ÷ 4.345 [M · T0-06 L330–335].
- **Ranges are not intervals.** They run from all-low to all-high parameters [T0-06 L259].
- **Conditional on success.** Every value assumes you persist and eventually succeed; no denominators of attempts exist [T0-06 L375].
- **Anchors:** an 8-month employed frontend retrospective, a 14–19 month vendor reference class for zero-experience changers, and Huntr's 82–108 day search medians [D/C · T0-06 L275].
- **Sensitivity:** adherence of 0.6 instead of 0.75 stretches the build by 25%; doubling the search lag adds about 1.4–3.7 months (about 4.6 for engineering from zero code); core hours, the least-validated parameter, matter most. Recalibrate them from your own progress to G1 by month 3 [M · T0-06 L387].
- **Not modelled:** internal transfers can beat these numbers, but there is no timing data [T0-06 L272]. Expert-contract evaluation work can start in weeks; it is paid AI-adjacent work, not a first offer [M · T0-06 L273].

## Route 1: backend or systems engineer

**Profile.** Owns services, concurrency, queues, observability and on-call. Likely gaps: Python (if Java or Go only), LLM API patterns, retrieval, evaluation and probabilistic thinking [M · T0-06 L411]. Mature teams built much of their AI tooling in-house (Sentry chose not to adopt LangChain; incident.io used Postgres with pgvector alongside Go), and in one case in-house developers with no prior AI experience built a feature in about two months after an agency quoted six to nine [B, single case · T0-06 L414–415].

| Old habit | What it looks like | New habit | Evidence |
|---|---|---|---|
| Determinism assumption | Expecting 100% pass rates; treating a flaky eval as a bug in the test | Set pass-rate thresholds as a product decision, not a correctness target | [C · T0-06 L430] |
| "It's just an API call" | Underestimating the data and evaluation work behind a good answer | Budget the eval set and error analysis first | [M · T0-06 L431] |
| Retrieval by default | A vector database before measuring; no keyword search | Measure first; compare keyword, hybrid and reranked retrieval | [D · T0-06 L432] |
| Framework-first | Orchestration frameworks before the underlying patterns | Learn the patterns; framework APIs churn | [C/D · T0-06 L433] |
| Infra polish before measurement | A polished platform around unmeasured quality | Measure quality, then build the platform | [M · T0-06 L434] |

Watch for competence-transfer overconfidence, infra bias and demo bias [M · T0-06 L436].

**Ranked skill delta** [M · T0-06 L418–424]:
1. Evaluation design and error analysis: the largest gap.
2. LLM API fluency and context engineering: structured output, tool calling, streaming, token budgets.
3. Retrieval: hybrid search, chunking, reranking, and knowing when not to retrieve.
4. Python (async, typing, pydantic), if you come from Java or Go.
5. Agent reliability: loop limits, budgets, approvals, replayable traces.
6. A domain model of what "good" looks like for your application.

**Quarterly roadmap** (tier B; add about 4 months at tier A) [M · T0-06 L438–445]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Fluency and a measured v0 | Python fluency if needed; a hosted-model app with structured output, tool calling and streaming over a corpus you know; 50 eval cases and a metrics table (recall@k, rubric correctness, citation faithfulness); two baselines; error analysis on 100+ traces with the top three failure classes fixed; hybrid retrieval and a reranker tested; cost and latency logged; memo written | G1 |
| 4–6 | Make it operable | Eval suite in CI with a regression threshold; judge calibrated on 100+ human labels; tracing; timeouts, retries, budgets and idempotent tool calls; container deployment; a real user; a load test; one postmortem | G2 |
| 7–9 | Second pattern and proof | A tool-using agent with human approval, per-run budget, sandboxed tools, deterministic trace replay and failure-injection tests; a serving lab measuring tokens/s, p95 latency and cost per million tokens for an open-weight model against an API; public write-up; one open-source contribution; 5+ mock loops; 15–20 targeted applications; an internal-role conversation | G3 |
| 10–12 | Convert | One eval-design and one LLM system-design round practised; one failure story with data; loops for applied AI engineer, AI platform or infrastructure and FDE-adjacent roles at your level | G4 |

**Skills stage in weeks.** T2-01 front-loads serving: weeks 1–2 serving architecture (KV-cache math, continuous batching, prefill/decode disaggregation) with a toy vLLM deployment; 3–4 retrieval over a real corpus from your domain; 5–6 evaluation (golden sets, LLM judges, pass^k) with 30+ hand-labelled cases and two baselines; 7–8 agent patterns with every call traced [D · T2-01 L233–241]. That order fits infrastructure-track targets, because backend moves to T3 and above interview infrastructure-heavy [B/C · T2-01.F5]. For application roles, keep T0-06's order, with the measured v0 first. Ignore T2-01's suggestion of the AWS Machine Learning – Specialty exam: it is retired (ERRATA U13).

**Checkpoints (tier B)** [M · T0-06 L447–451]: month 3, G1 and one public artifact; offers are unlikely unless the route is internal or FDE-adjacent. Month 6, G2 and active interviews; the modelled median first offer falls here (3.6–8.0 months). Month 9, most who persisted have an offer or decisive loop feedback. Month 12, offers for many who held to the gates; otherwise a G4 diagnosis.

**Portfolio specialisation.** A reliability layer for LLM applications: a small, well-tested gateway and harness with caching, backoff, budgets, fallbacks, trace replay, eval-regression CI and a public log of postmortems. It plays to your strengths and stands apart from the RAG-chatbot portfolios that hiring write-ups describe as commonplace [M/D · T0-06 L453].

## Route 2: data scientist or BI analyst

**Profile.** Data scientists bring statistics, ML, experimentation, SQL and notebooks; their likely gaps are production code, deployment, system design and on-call ownership. BI analysts bring SQL, metric definitions, dashboards and stakeholder communication; their gaps are Python, ML-adjacent skills and software engineering [M · T0-06 L468–469].

**The "can't ship" trope is half right** [C/D · T0-06.F5]. Data scientists are among the top three feeders into AI-engineer titles on both LinkedIn lists [C · T0-06 L130], and, as Hamel Husain argues, the core eval loop is data science: trace review, metric design, judge validation and test-set design [C · T0-06 L152]. The gaps show in big-company loops. A ranked hypothesis of what disqualifies data scientists, from guides and candidate reports with no frequency data [D · T0-06 L471–479]: coding rounds; system design; no production-ownership artifacts or stories; operational thinking about latency, cost and failure modes; customer-facing scoping. No source cited statistics or ML knowledge as the main disqualifier; that is an absence of evidence, not proof [T0-06 L481].

| Old habit | What it looks like | New habit | Evidence |
|---|---|---|---|
| Train-first identity | Fine-tuning before showing that prompting and retrieval fail | Exhaust prompting and retrieval first: 80% of surveyed teams prompt, 26% fine-tune | [B · T0-06 L496] |
| Notebook as deliverable | A notebook handed over as the product | An installable, tested package behind a service | [D · T0-06 L497] |
| Generic, unvalidated metrics | Off-the-shelf "helpfulness" scores; judges never checked against human labels | Task-specific metrics; judges validated against human labels | [C · T0-06 L498] |
| Months on theory | Weeks of derivations before shipping an API | Ship first; the 8-month retrospective dropped a four-week theory block as low-yield | [D · T0-06 L499] |
| Undervaluing cost and latency | No cost or latency view | Track both: 40% of surveyed teams say cost shapes their ambition | [B · T0-06 L500] |
| Dashboard thinking (BI) | A chat box on a dashboard with no evaluation of generated SQL or narrative | Score generated SQL by execution accuracy | [M · T0-06 L501, L518] |

Watch for expertise anchoring (LLM judges still need validation), the streetlight effect and the tool-hammer effect [M · T0-06 L503].

**Ranked skill delta, data scientist** [M · T0-06 L483–490]:
1. Production hygiene: typed, tested, installable Python; containers; CI/CD.
2. LLM application patterns: API fluency, structured outputs, tool use, retrieval.
3. Serving and operations: an API service with async handling, retries, auth, observability and cost tracking.
4. Loop preparation: DSA-style coding and system design for big-company loops.
5. Product scoping and communication. Lean on your strengths: error analysis, metric design, experimental design, judge validation.

**BI analyst:** the largest gaps are production Python, LLM API fluency, retrieval and production operations [M · T0-06 L740].

**Quarterly roadmap, data scientist** (tier B; add about 5 months at tier A) [M · T0-06 L505–512]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Package discipline and a measured v0 | One prior analysis refactored into an installable package with tests, type checks, Docker and CI; the LLM application built; a stratified trace sample, an error taxonomy with agreement between two reviewers, and confidence intervals on every eval metric | G1 |
| 4–6 | Serve it and calibrate the judge | A FastAPI service (async, auth, retries, timeouts) deployed; hybrid retrieval plus a reranker; a published judge-calibration study (100+ human labels, agreement statistic, position and verbosity bias tests); eval in CI; a cost-quality frontier chart | G2 |
| 7–9 | Loop readiness and a second pattern | 4–6 weeks of DSA basics and LLM-app system design; a cost-reducing router or an embedding fine-tune as a GPU lab; mock loops and targeted applications | G3 |
| 10–12 | Convert | Loops for applied AI engineer and evaluation-heavy roles; your level floor decided before offers arrive | G4 |

**Quarterly roadmap, BI analyst** (tier B; add about 7 months at tier A) [M · T0-06 L514–521]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Python and a text-to-SQL v0 | pandas, typing, pytest, packaging; a text-to-SQL copilot over a public schema with 50 questions and gold SQL, scored by execution accuracy | G1-lite |
| 4–6 | Governance and CI | Metric definitions as context (semantic layer); read-only access; row limits; eval in CI; deployed as an internal tool with at least one real user | G2 |
| 7–9 | Agentic analysis | A second pattern with human approvals and a documented business-impact case study | G3 |
| 10–12 | Convert | Analytics-AI roles in your industry; analytics engineering with GenAI scope as a bridge | G4 |

**Skills stage in weeks** [D · T2-01 L365–372]:

| Weeks | Data scientist | BI analyst |
|---|---|---|
| 1–3 | Python packaging, testing, CI/CD | Python fundamentals: scripts, tests and packages, not notebooks |
| 4–6 | LLM application patterns: RAG, tool use, agents | The same, plus basic ML and NLP concepts |
| 7–9 | Evaluation methodology | Evaluation plus text-to-SQL and analytics-copilot patterns |
| 10–12 | System design basics: API design, deployment, monitoring | Deployment: containers, cloud basics |

**Checkpoints (tier B)** [M · T0-06 L524–525]: data scientists have a refactored package and evals at month 3 (no offers expected), a published judge study and starting loops at month 6, and a modelled median first offer near month 8 (5.3–11.1). BI analysts have a v0 and Python fluency at month 3 and G2-lite plus applications at month 6; early offers are rare at month 9, and the modelled median is near month 11 (7.1–15.1), so month 12 is borderline. The data-scientist route targets mid level: watch for down-levelling and set your floor in advance [M · T0-06 L264, L512].

**Portfolio specialisation** [M · T0-06 L528–529]. Data scientist: an evaluation and error-analysis lab with a public golden set, an error taxonomy, judge calibration with bias tests and a cost-quality frontier. BI analyst: an analytics copilot with execution-accuracy evals, read-only guardrails and business-metric semantics.

## Route 3: frontend or full-stack engineer

**Profile.** Strong React and TypeScript, state management, streaming, design systems, accessibility and product sense. Likely gaps: retrieval and data work, evaluation, a service layer, system design for LLM applications and inference literacy [M · T0-06 L542]. The one detailed 8-month retrospective is from a React developer who also had to do real backend work: hybrid retrieval, reranking, async and caching, an eval harness [D · T0-06 L544].

**Test the frontend bet before relying on it.** The client-side platform is real as of October 2026: Khronos describes WebGPU as available in all major browsers (22 July 2026), Transformers.js v4 shipped a WebGPU runtime (9 February 2026), and Chrome's Translator, Language Detector and Summarizer APIs are stable from Chrome 138 [A · T0-06 L161–163]. Demand for AI-frontend specialists is thin and senior-skewed: the four postings examined in detail were Staff-level and asked for 5–6+ years, and no census exists [C/D · T0-06 L167]. Treat client-side AI as a differentiator on top of full-stack AI competence [M · T0-06 L169]. Count postings in your market that name frontend-specific AI skills against postings for full-stack AI engineers; if the former are a small minority, apply as a full-stack AI engineer [M · T0-06 L564].

| Old habit | What it looks like | New habit | Evidence |
|---|---|---|---|
| UI-wrapper plateau | A polished interface over a model whose quality is never measured | Measure quality before polishing the interface | [D · T0-06 L570] |
| Model output as trusted data | Unvalidated structured output crashing the UI | Validate output against a schema; design error and partial states | [M · T0-06 L571] |
| "Streaming means done" | Ignoring time to first token, cancellation, partial JSON and retries | Measure time to first token; handle cancellation and partial output | [M · T0-06 L572] |
| UX judged by vibes | No telemetry on acceptance, edit rate or abandonment | Instrument acceptance, edit rate and abandonment | [M · T0-06 L573] |
| Client-side inference as a universal fix | Ignoring device variance, download size, memory and battery | Feature-detect and fall back to WASM or a server | [A · T0-06 L558, L574] |
| Chasing API surfaces | Rebuilding for each framework release | Freeze stack choices for six weeks; invest in concepts | [M · T0-06 L254, L575] |

Watch for comfort-zone bias, the demo effect and novelty bias toward new APIs such as WebMCP [M · T0-06 L577].

**Ranked skill delta** [M · T0-06 L546–552]:
1. Evaluation and error analysis: the largest gap.
2. Retrieval and data: hybrid search, chunking, reranking; the "backend half" of most AI features.
3. A service layer with auth, queues, retries and observability, in Python (FastAPI) or server-side TypeScript.
4. Agent reliability and human-in-the-loop design: tool schemas, approvals, budgets.
5. Inference literacy: tokens, context windows, latency and throughput, on-device constraints.
6. System design for LLM applications, at interview grade.

**Quarterly roadmap** (tier B; add about 5 months at tier A) [M · T0-06 L579–586]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Backend-capable measured v0 | A service path chosen (Python and FastAPI, or a TypeScript server with the AI SDK); a streaming chat or agent UI over an app with retrieval; 50 eval cases with task-success scoring plus UX metrics (time to first token p50/p95, abort handling, error states); two baselines; error taxonomy; memo | G1 |
| 4–6 | Citations, tools and approvals | Retrieval with citations; tool calling with a human-approval UI; schema-validated output; judge calibration; eval in CI; deployment; real users; acceptance and edit-rate telemetry; one postmortem | G2 |
| 7–9 | On-device module and proof | A Transformers.js v4 module for browser-side embeddings or a small model on a bounded task, measured for size, load time, throughput and accuracy against the server version on 3+ device and browser combinations, with feature detection and a fallback; public write-up; an accessible open-source component; mock loops; 15–20 targeted applications | G3 |
| 10–12 | Convert | Loops for AI product or full-stack engineer, AI-frontend engineer and frontend-heavy FDE roles; an LLM system-design answer and an agent-UX case study with numbers | G4 |

**Skills stage in weeks** [D · T2-01 L431–438]: weeks 1–3 Python backend basics if missing (FastAPI, basic cloud deployment); 4–6 LLM application patterns (RAG, tool use, streaming, agent UX); 7–8 evaluation, where your edge is UX and human-in-the-loop evals; 9–10 on-device AI (Transformers.js v4, Chrome's built-in Prompt API, WebGPU). Frontend moves to T2 interview on the application track [B/C · T2-01.F5].

**Checkpoints (tier B)** [M · T0-06 L588]: month 3, G1 with a streaming UI and evals; offers unlikely. Month 6, G2; interviews begin. Month 9, the on-device module ships; the modelled median first offer is near month 7 (4.9–10.7). Month 12, offers likely for most who held to the gates.

**Portfolio specialisation.** An agent-UX lab: measured UX outcomes (acceptance rate, edit distance, abandonment, time to first token), approval flows and failure states. Add a private, browser-first semantic search with measured latency and accuracy trade-offs, and accessible open-source components [M · T0-06 L590].

## Route 4: non-technical professional

**Core claim.** Raw-coding competition is the wrong game. The leverage is domain judgement applied to evaluation, product, operations or customer implementation, and each lane has an entry fee in experience, credentials or coding [C · T0-06.F7].

| Lane | Entry fee in the sources | First proof | Main risk | Hub |
|---|---|---|---|---|
| Domain evaluation lead, in-house first | Credentials and seniority; expert marketplaces seek advanced degrees and years of experience [C · T0-06 L606] | Golden set, rubric, inter-rater agreement | Contract volatility, credential gating, LLM judges used alongside human experts | [Domain Evaluation](../02-roles/hubs/domain-evaluation-specialist.md) |
| AI ops, enablement or internal-tools PM | Operations experience and process knowledge [D · T0-06 L605] | A pilot with adoption and time-saved metrics, a runbook, a risk register | Title confusion; budget cycles | [AI Product Manager](../02-roles/hubs/ai-product-manager.md) |
| AI product manager | Product fundamentals first; one recruiter's template asks for 4+ years of PM experience and one model-powered feature shipped and measured, and the recruiter is paid on placements [D · T0-06 L604] | A PRD, an eval rubric, pilot metrics | Credibility with engineers; many roles ask for technical fluency | [AI Product Manager](../02-roles/hubs/ai-product-manager.md) |
| Solutions, FDE-adjacent or AI consultant | AI consultants and strategists report a median of 8.2 years' experience on LinkedIn's 2026 list [C · T0-06 L174]; FDE postings need coding too [B · T0-06 L175] | A customer pilot case study | A senior bar; FDE needs code | [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md), [FDE](../02-roles/hubs/forward-deployed-engineer.md) |
| Engineering from zero code | About 22 months (15–34) at tier B [M · T0-06 L268]; a vendor reference class says 14–19 months [D · T0-06 L199] | None until you can program | The entry-level squeeze [A · T0-06 L118] | [AI Engineer](../02-roles/hubs/ai-engineer.md) |

T0-06 ranks the niches by leverage: domain evaluation lead first, because evaluation is the top stack challenge and domain experts should own the labels; then AI ops or enablement PM; AI PM if you already have product fundamentals; solutions or FDE-adjacent roles; and expert-contract evaluation last, as a bridge rather than a destination [M · T0-06 L645–652]. The 8.2-year median belongs to AI consultants and strategists, not AI PMs (ERRATA U8). Mercor's senior domain-expert listings ask for 4+ years of full-time experience, at least 10 hours a week and at-will contractor status [C · T0-06 L177]; apply to expert networks only once your golden set exists [M · T0-06 L638].

**What AI-assisted building changes.** Under half of survey respondents say non-developers ship features (mostly internal), 17% say they regularly ship full-size customer-facing ones, and 59% agree that AI-generated code creates major liabilities [B · T0-06 L610]. Verification is the bottleneck, so evaluation skill matters more than prompting skill [M · T0-06 L610].

| Old habit | What it looks like | New habit | Evidence |
|---|---|---|---|
| Prompt-trick identity | Collecting prompts and tool demos | Measure outcomes on real tasks | [M · T0-06 L623] |
| Certificate collecting | Course completions without artifacts | Build artifacts; no source showed certificates carrying hiring signal | [D · T0-06 L624] |
| Fluency mistaken for competence | Using a tool well, taken as building and evaluating a system | Build and evaluate one workflow end to end | [M · T0-06 L625] |
| Automation bias | Trusting fluent outputs and LLM judges | Calibrate judges against human labels | [M · T0-06 L626] |
| Gig-market mirage | Treating expert-contract work as a career track | Use it as a bridge; it is volatile and credential-sensitive | [C · T0-06 L627] |
| Coding avoidance or overreach | Refusing any code, or shipping AI-written code without tests | Learn SQL and notebook Python; test what you ship | [M · T0-06 L628, L637] |

Watch for the Dunning-Kruger effect after early wins, the halo effect of fluent text and sunk cost on credentials [M · T0-06 L630].

**Ranked skill delta** [M · T0-06 L612–617]:
1. AI literacy beyond tool use: tokens and context, hallucination, retrieval versus fine-tuning versus prompting, cost and latency.
2. Evaluation fluency: rubrics, golden sets, inter-rater agreement, reading error analyses.
3. Notebook-level data skills: SQL and basic Python to analyse eval results and logs.
4. Pilot execution: scoping, adoption measurement, change management, risk and governance documents.
5. Technical communication with engineers.

**Quarterly roadmap, AI-adjacent lane** (tier B; add about 3–4 months at tier A) [M · T0-06 L632–639]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Domain workflow and a golden set | One lane and one workflow you know deeply, built with hosted or low-code tools; a domain golden set of 100+ real tasks (de-identified, or synthetic with permission) with rubrics, adjudication rules and agreement between two reviewers; 2–3 models or prompts compared against the existing human process | G1-domain |
| 4–6 | Pilot and measurement | A pilot with 5–10 colleagues measuring adoption, time saved and error rate; judge agreement with human labels checked; a PRD or runbook and a risk register; SQL and notebook Python learned for log analysis | G2-domain |
| 7–9 | Scale and visibility | An extended pilot; a cost-per-task model; a governance and guardrails document; an internal presentation; a de-identified public write-up; a request to leadership to define a role; targeted applications to vertical-AI companies | G3 |
| 10–12 | Convert | Loops for AI PM, AI ops or solutions roles with scope negotiated, or an explicit plan for the next six months | G4 |

**Skills stage in weeks** [D · T2-01 L487–496]: weeks 1–3 LLM fundamentals (capabilities, cost, latency and quality trade-offs); 4–6 evaluation methodology (rubrics, labelling, judging quality); 7–9 product process (success metrics, managing expectations, reporting non-determinism); 10–12 hands-on prompt building and output evaluation in Anthropic Console or OpenAI Playground. T2-01 labels this track "no coding required", but T0-06 lists notebook-level coding among the lanes' entry fees [C · T0-06 L181] and as a mandatory skill; add SQL and notebook Python by month 6 [M · T0-06 L615, L637].

**Checkpoints (tier B)** [M · T0-06 L641]: month 3, golden set done and pilot starting; contract evaluation work is possible earlier. Month 6, pilot results and a PRD. Month 9, an internal role redefinition or interviews; the modelled median is near month 7 (4.9–10.8), concentrated in internal moves and vertical-AI companies. Engineering from zero code is not achievable within 12 months at tier A or B.

**Portfolio specialisation.** A domain gold standard: a de-identified benchmark with rubric and agreement statistics, pilot results, a governance playbook and an AI-ops runbook, the artifact engineers cannot produce without you [M · T0-06 L643]. Never put an employer's or client's confidential data in a portfolio artifact [M · T0-06 L847].

## Route 5: academic researcher or quantitative PhD

**This route has its own guide, [PhD to industry](phd-to-industry.md).** It holds the profile and the seven translation barriers, the research habits to unlearn (in its pitfalls), the ranked skill delta, the 8-week skills block, the quarter-by-quarter plan with its deliverables, the portfolio specialisation, fellowships and the O-1A angle. This page keeps what it owns for every route:

- **Timeline.** About 8 months (5–12.5) to a first applied-role offer at hours tier B, about 13 (9–20) at tier A and 5 (3–8) at tier C, from 300 core hours (200–450) and a 12-week search lag (8–20) [M · T0-06 L269, L355]. The modelled median falls near month 8 (5.3–12.5); frontier research roles are not plannable [M · T0-06 L708].
- **Gates.** The shared spine applies unchanged: G1–G4 at months 3, 6, 9 and 12. At G1 the PhD route adds one test: every sophisticated step must beat a simple baseline on the eval set [M · T0-06 L697–L704].
- **Targets.** Applied AI engineer, applied scientist or research engineer is the plannable path; research scientist is upside [M · T0-06 L192, L660]. PhDs do not skip the skills stage (ERRATA U18).

## Route 6: DevOps, SRE or cloud engineer

**Profile.** Runs production Kubernetes, CI/CD, observability, incident response and cloud infrastructure. Feeder posting volumes are large (JobsPipe, 2026-11-02: DevOps Engineer 1,269 US / 3,183 global / 429 India, 69.4% naming Kubernetes; SRE 776 / 1,838 / 240; Cloud Engineer 803 / 1,587 / 128) [B · [role catalog](../02-roles/role-catalog.md) §7]. Across 11 inference, SRE and MLOps posting extracts in T0-67 (convenience sample; Extract-only), **model-serving frameworks (vLLM, SGLang, Triton, TensorRT-LLM) appeared in 11 of 11, Kubernetes in 6 of 11, observability or SLA language in 4 of 11, and model training in 0 of 11**; 3 of 11 stated 4+ years' experience [B/M · T0-67 L62, L120–128]. Model research is not the gate — serving and GPU fleet operations are.

**Ranked target-role fit** [B/C/M · T0-67 L118–128]:

| Priority | Role | Overlap | Gaps to close | Evidence |
|---|---|---|---|---|
| 1 | [Inference Engineer](../02-roles/hubs/inference-engineer.md) | High: serving, Kubernetes, SLOs, autoscaling | Model-serving frameworks (vLLM, SGLang, TensorRT-LLM), GPU scheduling, quantisation, benchmarking | Serving 11/11, K8s 6/11 [B/M · T0-67 L120] |
| 2 | [AI Infrastructure Engineer](../02-roles/hubs/ai-infrastructure-engineer.md) | High: distributed systems and cloud operations | GPU fleet operations, networking, cost per GPU-hour | Same sample; title variants [B/M · T0-67 L121] |
| 3 | [ML Platform Engineer](../02-roles/hubs/ml-platform-engineer.md) | High (best entry for ops-only staff without ML serving) | Kubeflow, MLflow, model registry, feature stores, GPU scheduling | Named in sample extracts [B · T0-67 L74, L122] |
| 4 | [Forward-Deployed Engineer](../02-roles/hubs/forward-deployed-engineer.md) (infra family) | Medium | Customer-facing deployment record; 5+ year gate | OpenAI FDE posting mirror [B/C · T0-67 L123] |
| 5 | [AI Enablement Engineer](../02-roles/hubs/ai-enablement-engineer.md) | Medium–high | Internal developer tooling, adoption metrics | No posting evidence in T0-67 [W · T0-67 L124] |

**Decision rules and traps** [B/C · T0-67 L73–76, L338–342]:
- **Under 4 years' experience:** target senior SRE roles handling GPU workloads or ML platform roles rather than frontier-lab infrastructure postings, which gate at 4–6+ years [B · T0-67 L75, L327, L338].
- **Skip model training first:** training was absent from all 11 extracts; building generic Kubernetes demos without GPU serving, SLOs or cost-per-1,000-token metrics misses the hiring bar [B · T0-67 L339, L341].
- **Audit aggregator listings:** one inference-engineer mirror carried a 13% trust score on its aggregator; verify open roles on the employer's own careers page [C · T0-67 L340, L573].
- **Senior residency option:** engineers with 5+ years and checkable public technical work can evaluate programmes such as the Anthropic Residency (secondary summaries note the 2026 round closing 2026-11-22; check live eligibility on the employer's page) [B · T0-67 L76, L144].

**Quarterly roadmap** (timeline unmeasured; unverified backend analogue ~6 months at tier B [E · T0-67 L327]) [B/P · T0-67 L134–140]:

| Window | Focus | Done when | Gate |
|---|---|---|---|
| Weeks 1–8 | Internal test (parallel) | Requested an inference or GPU-platform assignment at your employer and logged the answer | Internal ask [P · T0-67 L136] |
| Months 1–3 | Serving v0 with metrics | One open-weight model served with vLLM or Triton on GPU nodes; latency (TTFT, p95), throughput and cost per 1,000 tokens measured | G1 [B skill set; P metrics · T0-67 L137] |
| Months 4–6 | Operable GPU cluster | Kubernetes autoscaling on GPU node pools, SLO dashboard, alerts and an incident runbook | G2 [B · T0-67 L138] |
| Months 7–9 | Second serving pattern and proof | A second serving stack (quantised model or multi-model router) plus one public benchmark write-up or upstream fix | G3 [P; outcomes unmeasured · T0-67 L139] |
| Months 10–12 | Convert | Offer in inference, AI infrastructure or ML platform, or a weekly funnel diagnosis split by role family | G4 [P · T0-67 L140] |

## Route 7: product manager

**Profile.** Brings product discovery, prioritisation, metrics, roadmap ownership and stakeholder alignment. JobsPipe (2026-11-02) shows 15.4% of general Product Manager postings naming AI and 13.6% naming agentic AI [B · [role catalog](../02-roles/role-catalog.md) §7]. Across T0-67's posting sample, **enterprise and mid-size AI-PM postings ask for about 3 years of PM or technical programme experience, whereas frontier-lab and AI-native AI-PM postings gate at 5–10+ years plus shipped LLM or agentic products** (OpenAI Core Models 5+, Anthropic 6+, Vanta 8+, OpenAI Youth 10+) [B · T0-67 L63, L154–155].

**Ranked target-role fit** [B/C · T0-67 L152–160]:

| Priority | Role | Overlap | Gaps to close | Evidence |
|---|---|---|---|---|
| 1 | [AI Product Manager](../02-roles/hubs/ai-product-manager.md) (enterprise or mid-size AI team) | High on PM core | Evaluation design, LLM failure modes, cost/latency trade-offs, data literacy | Postings asking ~3 years PM/TPM [B · T0-67 L154] |
| 2 | [AI Product Manager](../02-roles/hubs/ai-product-manager.md) (frontier or AI-native) | High on PM core | 5–10+ years PM experience; shipped LLM/agentic features | 4 named postings in sample [B · T0-67 L155] |
| 3 | [AI Evaluation Engineer](../02-roles/hubs/ai-evaluation-engineer.md) (PM-led eval or human-data roles) | Medium | Rubric design, annotation pipelines, judge validation | Vendor subgroup: evals in 7 of 9 postings [C, COI · T0-67 L63, L156] |
| 4 | [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md) or [FDE](../02-roles/hubs/forward-deployed-engineer.md) | Medium | Technical architecture; FDE gates at 5+ years customer-facing engineering/deployment | OpenAI FDE posting mirror [B · T0-67 L79, L157] |
| 5 | [AI Governance Lead](../02-roles/hubs/ai-governance-lead.md) | Medium for compliance PMs | Governance and assurance frameworks | Not tested in T0-67 [W · T0-67 L158] |

**Interviews and traps** [B/C/P · T0-67 L162–164, L343–346]:
- **Loop signals (vendor-described, no employer-published AI-PM guide found [E · T0-67 L381]):** vendor and practitioner accounts say AI-PM loops probe product sense on model failure cases, feature evaluation metrics, and live prototype exercises in some loops [C · T0-67 L162].
- **Four traps:** applying to frontier-lab AI PM with under 5 years' PM experience [B · T0-67 L343]; showing prompt collections without a scored eval set and a written ship-or-no-ship decision [C · T0-67 L344]; relabelling generalist PM history as "AI PM" without shipping an LLM feature [P · T0-67 L345]; applying to FDE roles without a 5+ year technical customer-facing record [B · T0-67 L346]. Do not cite the 8.2-year LinkedIn median as an AI-PM requirement: it belongs to AI consultants and strategists (ERRATA U8).
- **Early-career India signal:** IIT Guwahati's 2025–26 placement report lists associate product manager among non-technical campus profiles [A · T0-67 L160], and Deloitte India's 2026 campus survey places AI and digital PM roles in its top-10 campus outcomes [B · T0-67 L160].

**Quarterly roadmap** (timeline unmeasured; unverified non-technical AI-adjacent analogue ~7 months at tier B [E · T0-67 L328]) [B/C/P · T0-67 L168–173]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Pilot feature and evals | One LLM feature built as a pilot or prototype, backed by a scored eval set (100+ cases [P]) and a written ship-or-no-ship memo | G1 [C · T0-67 L170] |
| 4–6 | Production telemetry | Quality, cost and latency monitoring live, with a documented workflow turning real user failures into eval test cases | G2 [C/P · T0-67 L171] |
| 7–9 | Second domain and proof | A second LLM feature in a different failure surface, plus one de-identified public case study with metrics | G3 [P · T0-67 L172] |
| 10–12 | Convert | Offer at an enterprise or mid-size AI team, or a funnel diagnosis separating frontier-lab from enterprise gates | G4 [B · T0-67 L173] |

## Route 8: IT-services engineer (India)

**The India IT-services transition reality.** The traditional fresher pyramid has contracted sharply while experienced demand shifted to global capability centres (GCCs):
- **Fresher contraction:** estimates put Indian IT-sector fresher hiring down from roughly 600,000 (FY22) to roughly 120,000 (FY25), and IT-BPM fresher hiring from ~400,000 (FY22) to ~175,000 (FY26) [C · T0-67 L59, L232–233]. TCS reported over 25,000 FY26 fresher offers on its earnings call (with 60% AI-skilled; secondary outlets cite 44,000 onboarded — an unresolved conflict) [B/C · T0-67 L59, L234–235, L419].
- **GCCs are the experienced growth channel:** India's 2,117 GCCs (2.36 million staff) added roughly 200,000 net employees in FY26 against roughly 110,000 at IT-services firms, with **over 77% of GCC hiring at mid-to-senior levels** [C · T0-67 L60, L244–245].
- **Training counts are not capability or job moves:** Infosys discloses internal bridge programmes without publishing move counts [B · T0-67 L191]; Wipro reported 93,994 AI-certified staff against roughly 60,000 active users out of ~242,000 staff (secondary arithmetic) [C · T0-67 L61]; Accenture reported roughly 550,000 staff trained in generative-AI fundamentals (out of ~780,000) against nearly 110,000 AI and data professionals in FY2026 [B/C · T0-67 L61, L191]. Corporate labels ("AI-aware", "AI-skilled", "AI Master") are not comparable across firms [T0-67 L426].
- **Documented restructuring pressure:** Accenture's US$865 million restructuring phases out roles with nonviable skills and ties senior leadership promotion to regular internal AI-tool use [B · T0-67 L197]; TCS's chief executive cited skills mismatch and limited redeployment in reductions (via MediaNama) [C · T0-67 L197].

**Three routes and target-role fit** [B/C/D · T0-67 L80–83, L179–195]:
1. **Internal GenAI practice or bridge programme first** (time-box to **two quarters**; if no move materialises, pivot externally — no IT-services employer publishes reskilling-to-GenAI move rates [E · T0-67 L199, L387]).
2. **GCC transfer at 4+ years' experience:** target [Applied AI Engineer](../02-roles/hubs/applied-ai-engineer.md), [AI Enablement Engineer](../02-roles/hubs/ai-enablement-engineer.md), [AI Evaluation Engineer](../02-roles/hubs/ai-evaluation-engineer.md) (strong fit for QA/test leads) or, at 5+ years, [AI Solutions Architect](../02-roles/hubs/ai-solutions-architect.md) and [FDE](../02-roles/hubs/forward-deployed-engineer.md) [B/C · T0-67 L81, L181–188].
3. **Direct move to product companies:** unevidenced in T0-67 [D · T0-67 L193]; treat as upside once production proof exists. TCS's Prime track reviews AI/data projects in technical rounds, signalling that deployed artifacts — not certificates — set the bar [C · T0-67 L195]. Engineers with 5+ years and checkable public work can also evaluate lab residencies alongside internal routes [B · T0-67 L83].

**Quarterly roadmap** (timeline unmeasured; unverified SWE analogue ~6–7 months at tier B [E · T0-67 L329]) [B/C/P · T0-67 L203–208]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Internal bridge ask and measured v0 | Asked for an internal bridge or GenAI-practice assignment; built one internal GenAI use case with an eval harness and baseline | G1 [B bridge existence; P metrics · T0-67 L205] |
| 4–6 | Operable internal tool with usage | Deployed internal tool with adoption measured against seats or licences (documenting active usage, not certificates) | G2 [C/P · T0-67 L206] |
| 7–9 | Public reproducible proof | Public repository and deployed demo built to project-review standard (Prime-track bar), plus targeted GCC outreach if internal transfer stalled | G3 [C/P · T0-67 L207] |
| 10–12 | Convert | Internal move into a GenAI practice, or a GCC offer at 4+ years' experience | G4 [C · T0-67 L208] |

## Route 9: student or new graduate

**The entry-level market across four geographies** (dated measurements; the regions measure different constructs) [A/B/C/E · T0-67 L52–59, L214–248]:

| Region | Key entry-level indicators (as dated) | What it means | Grade · source |
|---|---|---|---|
| **US** | NACE Spring 2026 projects +5.6% Class of 2026 hiring (45% rate market "fair"); NACE AI-skill measures conflict (10.5% chart vs >1/3 article — treat as 10–33%). NY Fed graduates aged 22–27 unemployment ~5.6% in Q2 2026 (5.2% in Q3 2026 per T0-70 L80), underemployment 42%; CS 7.0% and CE 7.8% (2024 ACS; CE 95% CI ~4–11%). CS new enrolment −8.4% (spring 2026). JobsPipe US AI-titled entry share 10.4% vs 35.8% all postings | Tight competition and seniorised entry roles (PwC: 7× more likely to ask for senior judgement [B · T0-06 L122]); internships dominate entry | B · T0-67 L53, L55–58, L214–222 |
| **UK** | ISE member graduate hiring −8% in 2024–25, stabilised in 2025–26 at **141 applications per graduate vacancy (172 London)**. Adzuna advertised graduate vacancies −45.6% YoY (July 2026; ISE notes adverts are not hires). 87% of UK employers expect AI to change entry roles; 53% maintain and 27% expand entry recruitment | Mass cold applications face extreme ratios; focus on structured internships and work-experience conversion | B · T0-67 L57, L225–229 |
| **EU** | Eurostat recent-graduate employment rate 83.0% overall and 87.0% tertiary (aged 20–34, 1–3 years post-graduation, 2025). **No EU-wide AI-specific graduate hiring series was found** | Broad graduate employment is stable; verify local AI-title demand yourself | B (general); E (AI-specific) · T0-67 L230–231 |
| **India** | JobsPipe AI-titled entry share 21.2% vs 31.9% all postings (2026-10-11, one platform, no counts). Deloitte India 2026 (n=257 orgs): 35% say AI creates new entry roles/skills, 20–25% AI/data campus premium, median B.Tech pay 3.3× higher at top-10 (₹18.7L) vs tier-3 (₹5.75L). **Official campus data:** IIT Guwahati 2025–26 placement 63% overall, B.Tech 81.11% (median 22.01 LPA), CSE 90.75%, Biosciences 56.71% (AI titles not broken out) | Campus placement is the primary route; outcomes vary sharply by institute tier and discipline, and IT-services fresher volume fell by roughly four-fifths | A (IIT Guwahati); B (Deloitte, JobsPipe) · T0-67 L53, L237–246, L397 |

**What works — ranked by outcome evidence** [B/C · T0-67 L65, L84–91, L252–262, L314–321]:
1. **In-person internships (strongest measured route):** NACE reports **63.1% intern-to-full-time conversion** (88.3% acceptance, 2024–25 cohort), and **in-person interns received offers at 71.9% against 56.2% for hybrid interns** (2023–24 cohort) [B · T0-67 L65, L252]. In India, Deloitte reports pre-placement offer conversion up ~6% YoY; IIT Guwahati recorded 198 PPOs in 2025–26 [A/B · T0-67 L252, L551].
2. **Proof employers actually ask for:** NACE employers prioritise teamwork, problem-solving and communication (28% seek AI-using early talent; nearly 60% assign interns AI projects [B]); Deloitte India ranks behavioural competencies (75%) and learning agility (72%) above technical skills for PPO conversion [B]; ISE highlights AI literacy, judgement and critical thinking [B]; CodePath reports 56% rating evaluation of AI outputs very or extremely important [C, COI] [T0-67 L314–321].
3. **Proof channels — NOT standalone hiring pipelines:**
   - *Open source (GSoC):* 30–36% of surveyed participants said it helped with a job or internship (programme self-reports, COI) [C · T0-67 L258].
   - *Competitions (Kaggle, hackathons):* platform stats (>29M users) and vendor-hosted employer case studies exist, but **no independent outcome data**; practitioners treat ranks as weak signal unless you explain the engineering [C, COI · T0-67 L259, L382].
   - *Research assistantships and REUs:* one 10-year single-site NSF REU survey found **74.7% pursued advanced degrees and 22.6% entered industry** — choose REUs for graduate study, not as an industry-hiring shortcut [C · T0-67 L90, L260].
   - *Early-career AI programmes:* Claude Corps offers a paid 12-month US nonprofit placement for US-authorised candidates with under 2 years' experience (covers prompt design, API building and evaluation; no outcome data yet — treat as a placement, not a guaranteed hiring pipeline) [B · T0-67 L87, L261]. OpenAI Residency 2026 closed [B · T0-67 L261].
   - *Bootcamps:* no independent GenAI outcome data; see [learning roadmaps](../03-skills-and-tech/learning-roadmaps.md) [E · T0-67 L262].

**Master's degrees and studying abroad (pointers, not legal or immigration advice):**
- **Small cost-adjusted return for CS:** causal Texas administrative estimates (Altonji & Zhu, NBER WP 33530) and the PEER report give cost-adjusted lifetime returns of **+6% for computer science, +2% for computer engineering and +4% for electrical/mechanical engineering**, against +17% average, +13% MBA and +41% law [B · T0-67 L64, L264]. BLS 2025 puts raw median earnings at US$97,552 for master's vs US$82,056 for bachelor's (~US$15,500 gap, selection uncontrolled), while graduate costs rose 233% since 2000 (Georgetown CEW) [B · T0-67 L264]. Take a CS master's only for a specific visa or research reason [B · T0-67 L86].
- **Study-abroad tuition and post-study work rules (as of November 2026; full visa trackers live in [visa and relocation](visa-and-relocation.md)):**
  - *Canada:* official Statistics Canada 2026/27 international graduate tuition averages CAD 24,693/year (computing CAD 24,068; engineering CAD 27,473); master's and PhD students at public institutions are exempt from the study-permit cap, and the PGWP field-of-study list is frozen for 2026 [B · T0-67 L85, L272–274, L289].
  - *UK:* Graduate Route stay **falls from 2 years to 18 months** for bachelor's and master's applications from 2027-01-01 (PhD keeps 3 years); secondary international master's tuition spans GBP 13,000–35,000/year [B/C · T0-67 L66, L276, L288].
  - *US (V0 — high variance):* secondary international master's tuition spans US$25,000–55,000/year (no official US average found) [C/E · T0-67 L277–278]. Post-study rules face active rulemaking and litigation: DHS proposed university-paid OPT fees (US$70,000 initial / US$30,000 subsequent; comments closed 2026-11-09, not in effect) and a US$103,265 cap-subject H-1B fee, while the US$100,000 H-1B proclamation fee is blocked/vacated by federal courts with appeals pending [B · T0-67 L66, L286–287]. Student-visa arrivals earn a median US$115,000 vs US$87,000 native-born (NSCG 2023, selection uncontrolled), while working-paper estimates find OPT extensions shifted domestic starting wages by −0.8% to −3.5% and raised foreign graduates' starting wages by +2.6% [B · T0-67 L66, L296–297].

**Quarterly roadmap, student or new graduate** (schedule-bound by internship and campus cycles [E · T0-67 L330]) [B/C/P · T0-67 L303–308]:

| Months | Focus | Done when | Gate |
|---|---|---|---|
| 1–3 | Evaluated v0 in public | One evaluated LLM application in a public repository, demonstrating teamwork/problem-solving and AI output evaluation | G1 [B · T0-67 L305] |
| 4–6 | Real users and internship funnel | Deployed application with real users; structured internship applications tracked by stage (targeting in-person roles early) | G2 [P · T0-67 L306] |
| 7–9 | Reviewable external proof | One reviewable competition entry, discussion-first OSS contribution or research project (as proof, not a sole pipeline) | G3 [C; outcomes unmeasured · T0-67 L307] |
| 10–12 | Convert | In-person internship offer (or campus placement / PPO), or a funnel review benchmarked against vacancy competition | G4 [B · T0-67 L308] |

### Geography

- **Most quantitative transition evidence in T0-06 is US-centric** [T0-06 L39]; check local postings before committing [M · T0-06 L848].
- **India:** AI-titled roles are 3.0% of India postings against 1.3% in the US, and the entry-level share of AI roles is 21.2% in India against 10.4% in the US (JobsPipe, 2026-10-11; one platform, no counts, and India's all-postings entry share is lower at 31.9% vs 35.8%) [B · T0-67 L53, L409]. India's experienced growth sits in GCCs (>77% mid-to-senior hiring), while IT-services fresher intake contracted sharply [C · T0-67 L59–60]. See the [India remote playbook](india-remote-playbook.md).
- **UK and EU:** UK graduate competition averages 141 applications per vacancy (172 London) [B · T0-67 L57]; EU general recent-graduate employment sits at 83.0%, with no EU-wide AI-specific graduate series [B/E · T0-67 L230–231].

## How to do it: the first 14 days

Steps from T0-06's 14-day plan [M · T0-06 L277–285]:

1. **Score yourself.** Rate each skill from 0 (none) to 3 (owns it in production or could teach it) and run the three fast tests below [M · T0-06 L718]. *Done when* the scores and test results are written down.
2. **Pick a route and an hours tier.** Block the hours and compare them with the leisure shares in the tier table. *Done when* the blocks are in your calendar for 12 weeks.
3. **Hand-write 30 evaluation cases** from real work in one corpus or task from your domain. *Done when* they are versioned in a repository; they are the prerequisite for G1.
4. **Ship a v0 in two weeks** on a hosted model API, logging every trace. *Done when* it runs end to end and the traces are stored.
5. **Ask for internal scope.** Find an internal sponsor or AI initiative and ask for a scoped assignment. *Done when* you have asked and dated a check-in 6–8 weeks out.
6. **Open free accounts only** (Hugging Face, Modal credits, Kaggle); do not pay for GPUs yet. *Done when* nothing is billed.
7. **Calendar the gates.** Put G1–G4 in the calendar, plus a monthly review that records applications, screens, take-homes, onsite loops and offers. *Done when* the review recurs.

**Three fast tests, about one day each** [M · T0-06 L745–748]:
- **Q&A over 50 documents.** Build a pipeline for 20 questions with known answers; report recall@5 and answer faithfulness. *Pass:* a reproducible script, a metrics table and two failure cases explained.
- **Explain the request.** Explain what happens between a user pressing Enter and the answer appearing: context assembly, retrieval, tool calls, streaming, cost. *Pass:* failure modes and cost named at each stage.
- **Design the eval.** For a task in your domain, write 30 test cases, a rubric and a plan to validate an LLM judge. *Pass:* two reviewers score a 20-case pilot and you report their agreement.

**Largest gaps by background** [M · T0-06 L737–743]: backend, evaluation design, API fluency and retrieval (plus Python from Java or Go); data scientist, production code, production operations and system design, then API fluency and agents; BI analyst, production code, API fluency, retrieval and production operations; frontend, evaluation design, retrieval, error analysis and production operations; non-technical, evaluation fluency, error analysis, API fluency and basic code; PhD, production code and operations, system design, and product sense with stakeholder communication.

## Templates and examples

**Transition plan** [P]:

```text
Route: [backend | data scientist | BI | frontend | non-technical lane | PhD applied | DevOps/SRE | PM | IT services | student]
Hours tier: [A | B | C]; planned [h]/week; adherence = logged ÷ planned, reviewed weekly
Target: [role] at [level]; loop type [applied-AI startup | big-company ML/AI | frontier lab | GCC]
Internal ask: sponsor [name]; scope [assignment or bridge]; asked [date]; check-in [date]
Domain corpus or task: [corpus]; 30 hand-written eval cases by [date] (or serving benchmark for DevOps/SRE)
Gates: G1 [date] · G2 [date] · G3 [date] · G4 [date] · Week-27 runway check [date]
Level floor if down-levelled: [lowest level you will accept]
Monthly funnel review: [day]; applications, screens, take-homes, onsites, offers
```

**Recalibrate your timeline** [M, the formula from T0-06 L330–335]:

```text
Effective hours/week = [planned hours] × [adherence: logged ÷ planned]
Build weeks          = [core hours for your route] ÷ [effective hours/week]
Weeks to first offer = [build weeks] + [search lag for your route]
Months               = [weeks] ÷ 4.345
```

**Funnel diagnosis at G4** [M · T0-06 L398, L403–405]:

```text
Applications [n] → screens [n] → take-homes [n] → onsites [n] → offers [n]
Where I lose: [stage]
Rule that applies: [no screens after 15 → positioning | 3 failed take-homes → eval design | system-design onsites → DSA and design, or retarget applied-AI loops]
Change: [loop type | level | hours tier]; reviewed by [practitioner] on [date]
```

**Weak → strong** [P]:

| Weak | Strong |
|---|---|
| "Completed three GenAI courses and a RAG tutorial." | "Built [system] over [corpus]; [n]-case eval set versioned with the code; recall@5 of [x] against a BM25 baseline of [y]; [link]." |
| "Data scientist passionate about LLMs." | "Validated an LLM judge against [n] human labels (agreement [statistic]); tested position and verbosity bias; [link to write-up]." |
| "Domain expert interested in AI." | "Built a [domain] golden set of [n] real tasks with a rubric and two-reviewer agreement of [statistic]; piloted with [n] colleagues; time saved [x]." |
| "Kubernetes engineer learning LLM training." | "Served [open-weight model] with vLLM on autoscaled GPU node pools; measured TTFT, p95 latency and cost per 1,000 tokens against SLOs; [runbook link]." |
| "Completed employer GenAI certification programme." | "Deployed internal GenAI tool to [N] colleagues; tracked active weekly usage against licences and logged regression failures into CI evals." |

## Checklist

- [ ] Route, hours tier and target loop type written down; diagnostic scored and fast tests run
- [ ] Internal ask (or IT-services bridge request) made in the first two weeks, with a 6–8 week check-in (or two-quarter time-box for IT-services bridges)
- [ ] 30 hand-written eval cases versioned and v0 shipped within two weeks (or serving v0 with latency/cost metrics for DevOps/SRE)
- [ ] Adherence logged weekly; tier changed after three weeks below 70% of plan
- [ ] Month 3, G1: measured v0 (evals + baselines + error taxonomy for app/PM routes; served model + latency/cost per 1,000 tokens for DevOps/SRE)
- [ ] Month 6, G2: operable v1 (CI evals + judge calibration + telemetry + real user; GPU autoscaling + SLOs + runbook for DevOps/SRE)
- [ ] Month 9, G3: a second system on a different failure surface; a public write-up with numbers; one discussion-first external contribution; 5+ mock loops; 15–20 targeted applications
- [ ] Month 12, G4: an offer or internal move, or a funnel diagnosis reviewed by a practitioner and a re-plan (with a week-27 long-tail check)
- [ ] Monthly funnel review held and recorded
- [ ] Only one funnel worked per 90-day block

## Pitfalls

| Red flag | Why it hurts | Fix |
|---|---|---|
| Hours not logged | Planning fallacy: the one detailed retrospective spent much of its effort on evaluation, retrieval tuning and latency work that tutorials rarely budget for [D · T0-06 L786] | Log hours weekly; move to the next-longer tier when adherence is below 70% |
| Success stories quoted as base rates | Every retrospective comes from someone who made it; no denominator exists [D · T0-06 L787] | Treat all ranges as conditional; track your own funnel and plan for BLS's 27-week+ tail [B · T0-67 L72] |
| Months 4–5 feel fraudulent | The retrospective describes this trough in both directions [D · T0-06 L788] | Pre-commit to G2 as the checkpoint, not to a feeling |
| A foundations-first plan for an application role | Tutorial hell; hiring write-ups ask for building and evaluating [D · T0-06 L253, L789] | Ship v0 in two weeks; reverse this only for the research-engineer track |
| Studying model training before serving (DevOps/SRE) | Training appeared in 0 of 11 inference/SRE extracts; serving frameworks appeared in 11 of 11 [B/M · T0-67 L62, L341] | Start with vLLM/Triton serving, GPU scheduling, SLOs and cost per 1,000 tokens |
| Counting corporate AI training as proof (IT services) | Training counts far outstrip active use or AI-role headcount (Wipro ~60k/242k active; Accenture ~550k trained vs ~110k AI pros) [B/C · T0-67 L61, L348] | Ship a deployed system with measured usage and reproducible public code |
| Targeting frontier-lab AI PM or FDE below the experience gate | Frontier AI-PM postings gate at 5–10+ yrs and FDE at 5+ yrs customer-facing deployment [B · T0-67 L63, L343, L346] | Enter via enterprise/mid-size AI PM (~3 yr gate) first and ship an evaluated LLM feature |
| Relying on mass graduate applications or a CS master's alone | UK graduate roles average 141 applications per vacancy [B · T0-67 L57]; CS master's cost-adjusted return is +6% [B · T0-67 L64] | Prioritise in-person internships (71.9% offer rate [B · T0-67 L65]); take a master's only for a concrete visa or research reason |
| Building in private | The retrospective built privately for five months and says visibility mattered [D · T0-06 L790] | Publish at G1 |
| Mass applications | 66% of recruiters plan to increase AI pre-screening in 2026, per LinkedIn [A · T0-06 L843] | Targeted applications with role-specific artifacts |
| Drive-by pull requests for G3 | AI "slop" has made them a liability [B · T0-12.F10] | Contribute discussion-first |
| Mixing funnels | Different gatekeepers and proof [B · T0-67 L373; M · T0-06 L255] | One funnel per 90-day block |
| Burnout at tier B | Tier B's 17.5 h/week is 56–74% of average leisure [M · T0-06 L382, L792] | Schedule recovery, or accept tier A and a longer horizon |
| Chasing API releases | AI SDK 6 was superseded by AI SDK 7 within six months and WebMCP renamed its API [B/C · T0-68 L79, L365] | Freeze stack choices for six weeks; invest in concepts |

## Evidence and limits

- **Measured:** market demand weighting and wage premium (B) [B · T0-06.F1; B · T0-67 L224]; the US early-career employment gap (19% as of 2026-06-30, descriptive, not causal, contested by other studies; B per T0-67) [B · T0-67 L52, L369; C · T0-06 L122]; BLS time-use data (A) and August 2026 unemployment duration (B) [B · T0-67 L223]; IIT Guwahati 2025–26 official placement report (A) [A · T0-67 L240]; NACE, ISE, NY Fed, Eurostat and Statistics Canada graduate indicators (B) [T0-67 L55–58, L214–230, L272].
- **T0-67 access and sample caveat:** T0-67 opened only 7 of 75 cited sources in full (68 were read as search extracts, capping their grade at B), includes 14 conflicted vendor/industry sources, and uses small convenience posting samples (11 inference/SRE/MLOps, 6 AI PM, 2 FDE) that do not represent entire markets [T0-67 L22, L42, L425].
- **Modelled:** every month count, hours figure and gate for Routes 1–5 is T0-06's model (M). Confidence is medium-low for backend and low for the rest [T0-06 L263–269], and the model is most sensitive to core hours, its least-validated parameter [T0-06 L387]. Routes 6–9 have **no measured transition timelines** (A1) [E · T0-67 L327–330, L379].
- **Judgement:** T2-01's viability matrix and skills-stage week plans are design judgements [D · T2-01 L104]. Gate metrics for Routes 6–9 are practice-curated [P · T0-67 L134–308].
- **Not found (Grade E):** longitudinal cohort studies, success denominators, measured time to first offer by background [T0-06 L816–823; T0-67 L379], the four Phase 0 internal-transfer accounts (A2) [T0-67 L380], employer-published AI-PM or inference/FDE interview guides (A3, A10) [T0-67 L381, L388], independent outcome data for competitions, open source, fellowships or bootcamps (A4, A5, A20) [T0-67 L382–383, L398], an EU-wide AI-specific graduate series (A6) [T0-67 L384], IT-services reskilling move rates (A9) [T0-67 L387], and AI-specific master's returns (A17) [T0-67 L395].
- **Open source conflicts:** TCS FY26 fresher counts conflict (>25,000 offers on the company call vs 44,000 onboarded in secondary press) [T0-67 L419]; NACE's two AI-skill entry shares conflict (10.5% vs >1/3) [T0-67 L56, L423]; US OPT counts conflict across summaries (240k, 300k, 418k) [T0-67 L422].
- **Survivorship:** every retrospective anchor comes from someone who succeeded [T0-06 L804].
- **Errata applied:** U7 and U14 (tier band values not used), U8 (the 8.2-year median is the AI consultants' figure), U9 (five high-volume corridors), U13 (retired AWS exam), U18 (PhDs run the skills stage), plus the T0-67 K2 correction to T0-06 L108 (Axial's 66% is mid plus senior; total IC sits near 86%) [C · T0-67 L54, L368].
- **What would change this advice** [T0-06 L861–864; T0-67 L70–91]: a cohort study showing measured speeds by background would rewrite the timing tables; published internal move rates from IT-services firms would replace the two-quarter bridge rule; finalisation or permanent vacatur of US OPT and H-1B fee rules would change study-abroad planning; evidence that credentials outperform artifacts would revise the gates.

## Next steps

- **Choose the target:** the [targeting workbook](../00-start/targeting-workbook.md), [GenAI target roles](../02-roles/genai-target-roles.md) and the [role map](../02-roles/role-map.md).
- **Learn:** the [learning roadmaps](../03-skills-and-tech/learning-roadmaps.md) (with rated free and paid resources), [skill maps](../03-skills-and-tech/role-skill-maps.md) and the [skills radar](../03-skills-and-tech/skills-radar.md). Certificates are a tie-breaker at best: see [credential ROI](../04-certifications/credential-roi.md).
- **Build G1–G3 artifacts:** [project archetypes](../05-portfolio/project-archetypes.md) and [proof-of-work standards](../05-portfolio/proof-of-work-standards.md).
- **Search and interview:** [job-search strategy](../06-job-search/job-search-strategy.md#27-recommended-sequencing-expanding-rings), [referrals and outreach](../07-networking/referrals-and-outreach.md), [interview loops](../08-interviewing/interview-loops.md) and the [prep packs](../08-interviewing/prep-packs.md).
- **Other tracks:** [PhD to industry](phd-to-industry.md), [India remote playbook](india-remote-playbook.md), [governance careers](governance-careers.md), [freelance and fractional](freelance-fractional.md) and [visa and relocation](visa-and-relocation.md).
- **After the offer:** [first 90 days](../10-onboarding/first-90-days.md) and [growth and progression](../10-onboarding/growth-and-progression.md).
