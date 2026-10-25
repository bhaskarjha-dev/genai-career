---
id: T0-09
title: "GenAI engineer first 90 days (2026): the expectations gap, probation rubrics and a 30-60-90 operating playbook"
date: 2026-10-23
status: final-with-gaps
topic: "Post-hire execution, probation standards and early retention of GenAI engineers in AI startups, enterprise engineering orgs and India GCCs"
tags: [genai-engineering, onboarding, probation, first-90-days, 30-60-90, ai-expectations-gap, evals, non-determinism, llm-cost, compute-quota, compliance, india-gcc, attrition]
informs_decisions:
  - "How to structure the first 90 days (week-by-week deliverables) at a startup, an enterprise team or an India GCC"
  - "What to verify in weeks 1-2 (data, compute, budget, approvals, success metrics) and when to escalate, renegotiate scope or leave"
  - "Which early quick wins (regression evals, measured cost cuts) to stake credibility on, and how to report non-deterministic results upward"
confidence: "Medium on mechanisms (why AI projects stall; non-determinism; quota and cost levers). Low on prevalence (no AI-specific early-attrition dataset found; the 35% claim is unsourced). Very low on startup-vs-GCC probation rubrics (no public GenAI-specific rubric found)."
---

# First 90 days of a GenAI engineer, 2026: what decides success, probation outcomes and early exits

> **Bottom line.**
> 1. The claim "up to 35% of AI engineering hires face friction, reviews or early departure within 6 months" has no traceable source after fifteen logged queries. Do not repeat it as fact. The nearest published numbers measure other things (F1).
> 2. "AI Expectations Gap" is a descriptive label used mostly by vendors, not an established construct. The mechanism behind it (misdefined problem, missing data, weak infrastructure, no eval baseline, non-determinism, nobody owning pilot-to-production) is well documented at project level. The headline failure rates are soft (F2, F4-F6).
> 3. What the evidence supports for your first 90 days: turn vague expectations into a written, measured contract in weeks 1-2. Then ship small, evidence-backed artifacts every week: a golden set built from real failures, run-to-run variance (pass^k with error bars), cost per task, and a risk/approval register (F3, F6, F8, F10).
> 4. Public evidence on GenAI-specific probation rubrics and on startup-vs-GCC differences is thin. Where this file gives a scorecard or a contrast, it is my synthesis (Grade D) built on cited pieces, and it says so.
>
> Grades: **A** primary/canonical page fetched and read; **B** reputable secondary source, or a primary seen only as abstract/snippet; **C** vendor material, blog, anecdote, or survey with opaque method; **D** recalled from memory or my own inference. A trailing "-" (A-, B-, C-) marks a weaker case within the grade, such as a third-party copy, a partial page or an undisclosed sample. Words after a grade name the source type: "A, vendor docs" means the vendor's own documentation was read, which settles what the vendor says but not whether its performance claims hold. IDs such as [E23] point to the Evidence Ledger at the end.

## Prior

Condensed from a pre-research notes file whose header says it was written on 2026-10-21 from model memory before any search, so these are Grade D hypotheses. The propositions and confidence levels are unchanged. They are checked in the Delta section.

| # | Proposition (checkable) | Prior confidence | Would be falsified by |
|---|---|---|---|
| P1 | The "up to 35% ... within 6 months" figure has no primary, citable source; it is a blog or vendor extrapolation, or a conflation of other statistics. | 75% | A dated survey or dataset giving an early-departure share for AI-engineering hires. |
| P2 | RAND (">80% fail"), Gartner (30% of GenAI projects abandoned after PoC) and MIT NANDA (95% of pilots show no P&L impact) are real publications that measure *project* outcomes with loose definitions and self-selected samples. They support an expectations gap qualitatively and say nothing quantitative about new-hire attrition. Their root causes are mostly organizational and data-related, not model capability. | 80% | Any of them measuring individual hire outcomes, or root causes dominated by model limits. |
| P3 | Early attrition among newcomers is driven mainly by role ambiguity and unmet expectations (psychological-contract breach, low role clarity). AI-specific early-attrition data is scarce, so most AI-engineer onboarding evidence will be practitioner anecdote (Grade C). | 75% | A rigorous AI-specific early-attrition dataset, or evidence that other drivers (pay, manager) dominate. |
| P4 | In 2026 managers judge new AI engineers mostly on shipped, measured outputs (a trusted eval harness, a production release, cost/latency/quality numbers, incident hygiene), and AI fluency has become an explicit review criterion at many firms. Public rubric specifics are sparse. | 60% | Public rubrics that emphasize something else, or no firm making AI usage a review criterion. |
| P5 | Startups vs GCCs: GCC constraints are dominated by approvals and parent-company dependencies (data residency, infosec red lines, tool procurement, GPUs or credits held at HQ) and by formal 3-6 month probation/confirmation cycles. Startup constraints are runway and credit limits, founder-driven ambiguity and no formal rubric. | 55% | GCC evidence pointing elsewhere (no HQ dependency), or startups with formal rubrics. |

## Research Question

**Decision.** What structural obstacles, performance-review rubrics and operational deliverables determine whether a newly hired GenAI engineer succeeds in the first 90 days, or fails probation or leaves early, in 2026, across (a) venture-backed AI startups, (b) enterprise engineering orgs and (c) Global Capability Centers (GCCs, mostly in India)?

**Sub-questions.**
1. How common is early failure or attrition, and does any source support "up to 35% within 6 months"? (F1, F3, D1, D4)
2. What are the root causes of the "AI Expectations Gap", with cases? (F2, F4-F7, F12, D2, D3, D5)
3. How are new AI hires evaluated at 30/60/90 days, and which quantitative metrics are tracked? (F8, R5, D6)
4. How do engineers secure compute, API budget and data permissions, and what do they do when the promised infrastructure is absent? (F5, R2, R4, D5, D10)
5. Which quick wins establish credibility (a first regression eval suite, a ~40% token-spend cut)? (F10, D10)
6. Which political, security and compliance cross-currents stall initiatives, and how are they navigated? (F7, F11, R7, D9)
7. How should an engineer manage upward on non-determinism? (F6, R6)
8. Which tools support onboarding, documentation and team dashboards? (D8)

**Working definitions.**
- *Early failure*: failing, extending or being managed out of probation, or a voluntary exit, within roughly the first 6 months. Sources use 45 days, 90 days, 6 months or 1 year, so their numbers are not comparable.
- *Attrition*: annual separations. *Retention*: share still employed after N years. *Intent to quit*: survey intention, not realized exits.
- *AI Expectations Gap*: the brief's working label. Leaders expect instant, autonomous, high-accuracy AI; teams meet data, compute/budget, integration, evaluation and non-determinism limits.

**Method and limits.** Public web only: no access to internal manager rubrics, 1:1 notes or HR data. Pages were read through a summarizing fetch tool, so load-bearing numbers were requested verbatim and cross-checked against a second source where possible (noted in the ledger). Seven parallel research threads were attempted and cut off by a usage limit before saving notes; all evidence below was gathered directly in one thread, with provenance in `research_notes/GenAI engineer first 90 days 2/evidence_log.md`. A pre-existing notes folder from an earlier run was used only for the Prior and as unverified leads. Research ran 2026-10-21 to 2026-10-23.

## Key Findings

**F1. The "up to 35%" claim has no traceable source; the nearest published numbers measure different things.** Grade: negative result (not found after searching); the nearest general-workforce figures are A/B and the AI-specific ones C.
- Fifteen logged queries (D1) found no page that gives 35% for AI-engineering hires, within six months, attributed to ambiguous expectations or missing data and GPU.
- Nearest published figures. None gives a realized early-exit rate for AI hires with causes attributed:
  - 34% of all workers planned to quit within 3-6 months, against 51% of gen-AI "creators and heavy users" (McKinsey; n=12,802 in Canada, the UK and the US; fielded Jul-Aug 2023; intent, not exits) [E134 A, E125 B].
  - 33% quit within 90 days (Jobvite 2018, n=1,500 US workers, reported via press) [E50 B].
  - 31% have "quit a job within the first six months" (BambooHR 2015, n=1,005; the wording means "ever") [E19 B].
  - Annual attrition of 28% for AI/ML individual contributors against 17% for software engineers (Pave 2025; vendor payroll data, sample undisclosed) [E97 B-].
  - 18-25% annual attrition in AI and Cloud roles in India GCCs (Zinnov 2026; annual, not early) [E16 B].
  - "Nearly two-thirds" of UK data leaders planning to quit within 12 months (Lucent Search 2025; leaders, not engineers; intent; trade-press relay, sample and method not stated) [E141 C].
  - In a vendor's voluntary survey of 200+ India AI and ML engineers (Jul-Sep 2026), 39% named no growth, 21% a better offer and 19% "broken promises" (a job different from the one accepted) as what pushed them out of a role early. These are shares of stated reasons, not an early-exit rate [E146 C].
- Implication: treat 35% as an unsupported planning heuristic. If you must use it, say "unsourced; the nearest published figures are 31-34%, for general workers".
- Caveat: "not found" is not "does not exist". Paywalled analyst reports and internal HR data were out of reach.

**F2. "AI Expectations Gap" is a descriptive label, not an established construct. The mechanism is documented, but the headline failure rates are soft.** Grade: B overall (individual primary sources A).
- Label: found only in vendor and opinion material. MetaCTO writes of "the gap between executive AI ambitions and engineering realities" [E110 C]. SimScale's survey of 300 engineering leaders (simulation-software domain, not GenAI engineering) reports that 93% expect productivity gains while "only 3%" achieve the "very high" level that 30% expected [E109 C]. Peak's CEO told Fortune in 2022 that "line-of-business executives think the technology can do more than it really can" [E108 C]. No canonical definition or academic origin found.
- Mechanism: RAND's 65 interviews give five root causes: problem misunderstood or miscommunicated; insufficient data; technology over problem; weak infrastructure; problems beyond AI. RAND's ">80%" is "by some estimates", taken from a 2022 Fortune piece, not measured by RAND [E1 A].
- Rates: IBM (2,000 CEOs): "only 25% of AI initiatives have delivered expected ROI" and "only 16% have scaled enterprise wide" [E75 A]. Gartner's figures are predictions: more than 40% of agentic projects cancelled by end-2027 [E2 A]; 60% of AI projects unsupported by AI-ready data abandoned through 2026 [E76 A]; 30% of GenAI projects abandoned after PoC by end-2025 [E3 B]. S&P: 42% of companies abandoning most initiatives [E6 B]. MIT NANDA's "95%" rests on 52 organization interviews, 153 survey responses and 300+ public deployments, is "directionally accurate based on individual interviews", shifts denominator between "organizations" and "enterprise AI solutions", and diagnoses a "learning gap" rather than infrastructure or talent [E130 A-; critique E5 C].
- GCC: "nearly 70%" of India GCCs are stuck at AI pilots, and "nobody owns the space between a successful pilot and a production deployment" [E129 A-, E68 B, E70 B].

**F3. At the individual level, early failure looks like role/expectation mismatch plus thin onboarding. AI-specific measurement is missing.** Grade: B (general research), C (AI-specific anecdotes and vendor surveys).
- A newcomer-adjustment meta-analysis (70 samples) links role clarity, self-efficacy and social acceptance to adjustment, performance and turnover (abstract only; effect sizes not retrieved) [E20 B, abstract only]. A psychological-contract-breach meta-analysis exists (bibliographic record only) [E21 B-].
- 43% of surveyed job seekers said the day-to-day role was not what the hiring process led them to expect (Jobvite 2018, via press) [E50 B].
- AI-specific evidence is anecdote. A senior ML engineer's account of failing probation after about three months cites data-engineering and troubleshooting work instead of ML, and "few or zero guidance" [E127 C]. A recruiter reports a Series B's first AI hire leaving at eight months after about $200,000 in salary "had produced nothing customers used", and lists failure modes: researcher hired for a builder's job, no measure of success, no accountable executive [E121 C].
- Pay is not the main stated driver. India GCC high performers cite skill momentum, autonomy/scope and recognition, "None of them are compensation" [E16 B]. For gen-AI heavy users, compensation ranks seventh as a motivator [E134 A]. In a vendor's survey of 200+ India AI and ML engineers, no growth (39%) led the reasons for leaving a role early, ahead of a better offer (21%), broken promises (19%) and poor management (18%); compensation was the least-named reason to stay (4%) [E146 C].
- Caveat: stated reasons are not revealed reasons, and no source isolates "expectations" for GenAI hires. The vendor survey is voluntary, skews early to mid career, and does not state the question wording or the response base.

**F4. Data problems are among the most-cited blockers, and "no usable data" is a common starting state, not an exception.** Grade: B (A for the Gartner, IBM and RAND pages, C for the vendor-sponsored survey).
- 63% of organizations lack, or are unsure they have, data-management practices for AI (Gartner; the page gives two inconsistent sample sizes, 1,203 and 248) [E76 A]. IBM: 50% of CEOs report "disconnected, piecemeal technology" and 68% call integrated enterprise-wide data architecture critical [E75 A]. India GCC barriers include "fragmented data, legacy systems, unclear governance, immature security controls, insufficient compute planning" [E129 A-]. A Qlik-sponsored survey of 500 US AI professionals at companies with at least $500 million in revenue (fielded 4-18 Feb 2025) found 81% report significant data-quality issues and 85% believe leadership is not addressing them [E143 C, vendor-sponsored].
- Practitioner canon: data collection, flow and analytics sit below ML in Rogati's hierarchy [E100 B, dated]. Ng: "We might need a costly initial data collection phase" [E71 B]. Google's Rules of ML: "Don't be afraid to launch a product without machine learning" [E29 A].
- The "99% accuracy on zero-shot unstructured PDFs" example: on a 2026 benchmark of 1,475 pages in 10 domains, in clean, digitally degraded and real-capture versions, the best of 40 parsers scored about 74 out of 100, and rankings shift with document type and degradation [E136 A, E135 A]. These benchmarks score text, formula and table parsing, not business-field extraction. I found no source supporting 99% on unconstrained PDFs; you need your own labeled sample.

**F5. Compute and budget are gated by process and usage history. The levers are documented; the "negotiation tactics" are inference.** Grade: A for mechanics (vendor docs), C for how common GPU scarcity is, D for tactics.
- Quotas: AWS GPU quotas count vCPUs per region, and denials are linked to "limited usage history or a very large increase" [E31 A-]. Azure: "priority goes to customers who actively use their existing quota allocation" [E32 A]. Claude API tiers follow "usage history and account standing", with per-workspace spend caps (not settable on the Default Workspace) [E66, E65 A]. LiteLLM team budgets return HTTP 422 when exceeded (configurable to 429) [E34 A].
- Money: 98% of 1,192 FinOps respondents now manage AI spend [E33 A]. Startup credits exist but are conditional: Google up to $350,000 for Scale-tier AI startups, with third-party models excluded [E137 A]; AWS Activate Portfolio up to $200,000 [E138 A], redeemable for third-party Bedrock models [E139 A]; Microsoft typically $100,000 through an investor offer [E140 A]. India: the IndiaAI portal lists 38,000+ GPUs at about Rs 65 per GPU-hour, allocated by eligibility and requested hours [E48 B, E49 A-].
- Scarcity is common. In a survey of 1,367 AI professionals sponsored by the cloud provider Civo, 85% worked for organizations that had delayed projects because of limited GPU access, and 39% put the delays at three to six months [E142 C, vendor-sponsored].
- No study found on how engineers actually obtain quota, credits or data permissions, or on how long a new hire waits for a first GPU or dataset grant. A vendor-authored article says onboarding takes "weeks when it could take days" but gives no measurements [E148 C]. Recommendation R4 is my synthesis of the mechanics above.

**F6. Non-determinism is measurable and partly engineering-fixable, and the engineer who quantifies it first controls the narrative.** Grade: A.
- 1,000 temperature-0 completions of one prompt gave 80 unique outputs. The cause is load-dependent batch size (lack of batch invariance), and deterministic kernels cost throughput (55 s against 26 s for default vLLM in the authors' test) [E23 A]. Accuracy varied by up to 15% across runs and best-versus-worst gaps reached 70% (5 LLMs, 8 tasks, 10 runs) [E53 A]. On tau-bench, pass^8 was under 25% in retail for gpt-4o-class agents [E52 A].
- Anthropic's eval guide: "a task that passed on one eval run might fail on the next"; pass@k is at least one success in k tries, pass^k is all k succeeding; "20-50 simple tasks drawn from real failures is a great start" [E74 A]. Evals need error bars [E38 A] and human validation because of "criteria drift" [E107 A]. "Your pass rate is a product decision" [E42 A].
- LinkedIn: 80% of the basic design in month one, and the remaining stretch took four more months; "You are essentially evaluating a subjective, non-deterministic product" [E36 B].

**F7. Governance gates are real and moving in 2026, and two common assumptions are wrong.** Grade: A (regulator text), B (law-firm summaries).
- US bank model-risk guidance: SR 26-2 (17 Apr 2026) supersedes SR 11-7 and states that generative and agentic AI "are not within the scope of this guidance" [E9, E10 A; E43 B]. A vendor blog claiming it covers LLMs is contradicted by the primary text [E11 C]. So approval of LLM use rests on internal policy; ask which policy applies.
- EU: Regulation (EU) 2026/1744 (in force 27 Jul 2026) moves Annex III high-risk obligations from 2 Aug 2026 to 2 Dec 2027 and Annex I to 2 Aug 2028; GPAI duties continue [E12, E13 B].
- India: DPDP Rules were notified 13 Nov 2025 and the core duties start 13 May 2027 per two sources (12 May per a third; one outlet's "13 March 2027" for sections 9 and 10 is uncorroborated) [E14, E81, E80, E44 B]. RBI FREE-AI is a framework of 7 sutras and 26 recommendations [E46 B].
- Security: shadow AI added $670,000 to the average breach cost, and 97% of organizations reporting an AI-related incident lacked proper AI access controls [E47 A]. Shared vocabulary: NIST AI 600-1's 12 GenAI risks; OWASP LLM02 (sensitive information) and LLM10 (unbounded consumption, "denial of wallet") [E92, E93, E94 A].
- Liability: a tribunal held Air Canada responsible for its chatbot's statements [E35 B]. A process that works: Adobe's single intake, six data points and pre-agreed "green" scenarios [E104 B].

**F8. Public, named GenAI probation rubrics essentially do not exist. The observable standards are job-posting deliverables, onboarding metrics, AI-fluency criteria and probation mechanics.** Grade: B/C.
- Job postings: Onit (Pune) asks for one production agent workflow with tracing/observability, an offline eval suite with regression gates, cost/latency targets and monitoring, and documented failure modes and fallback [E25, E26 A, postings]. Two other AI postings gave no 30/60/90 criteria [E28, E62].
- Onboarding metrics with public definitions: time to first PR and to 10th PR, plus a roughly 90-day sentiment survey. A vendor benchmark gives P50/P75/P90 of 11 / 6.4 / 3 days (first PR) and 50 / 43.6 / 28 days (10th PR), provenance undisclosed [E8 A, vendor docs]. Spotify cut time-to-10th-PR from about 60 days to under 20 [E7 A, vendor-promotional]. Big-tech targets include a production change in week one [E59 B].
- AI fluency in reviews: Shopify, "Reflexive AI usage is now a baseline expectation" [E39 B]. Meta made "AI-driven impact" a core expectation from 2026 and uses a tool that counts AI-generated code among 200+ data points [E111, E112 B].
- Probation mechanics: GitLab's handbook gives 1-9 month probation by location (India listed), a halfway performance review, a manager reminder 28 days before the end, and an outcome selected on "performance", with no further criteria [E82 A].
- Practitioner 30-60-90s (shadow, then three supervised artifacts, then narrow ownership; or a written "expectations contract") are Grade C [E95, E96].

**F9. Startup-vs-GCC differences are plausible but thinly evidenced; the GCC evidence is about aggregates.** Grade: B (GCC aggregates), D (inferred contrasts).
- GCC aggregates: 2,117 GCCs and an "operating-model gap in AI adoption" [E15 A-]; 64% have dual global mandates and "nearly 70%" are stuck at pilots [E68 B, E129 A-]. Attrition is 16% overall and 18-25% in AI/Cloud (Zinnov) against 9% overall (EY 2025). Samples and definitions differ, so the conflict is unresolved [E16 B, E69 A-].
- India probation: no central law caps it, and 6 months is typical according to an employer-of-record vendor whose page is internally inconsistent on ceilings [E118 C]. Four Labour Codes took effect 21 Nov 2025, with IT/ITES standing-order exemptions unclear [E117 B].
- Startups: no public evidence on probation or compute beyond a posting that stresses founder proximity [E28], credit programs [E137, E138, E139, E140] and a recruiter anecdote [E121].
- Not found: HQ-held GPU allocation as a documented GCC pattern; any GCC GenAI probation rubric.

**F10. Two quick wins have independent support (a small regression eval suite built from real failures, and measured cost cuts). "~40%" is plausible, workload-dependent and must be measured on your own traffic.** Grade: A (mechanics), C (case claims).
- Eval suite: start with 20-50 tasks drawn from real failures [E74 A]; log traces first and "remove all friction from the process of looking at data" [E42 A]; Onit's posting makes regression gates a 90-day deliverable [E25 A, posting].
- Cost: cache reads bill at 0.1x base input for most Claude models, with lower multipliers listed for the newest [E41 A]. The OpenAI Batch API gives a 50% discount with a 24-hour window and separate rate limits [E73 A]. An independent 2026 preprint measured 41-80% API-cost reduction and 13-31% faster time-to-first-token from prompt caching on long-horizon agentic tasks, and warns that naive caching can increase latency [E114 A]. Routing papers report "over 2 times" [E79 A] and "up to 98%" (2023, an upper bound) [E78 A, dated]. Blog claims (70% from caching plus routing; 77% input-token cost) lack method or were metadata-only [E105, E115 C].
- Over-claiming backfires: Klarna rehired humans and CBA reversed AI-driven job cuts [E24, E61 B].

**F11. Engineering-analytics platforms double as evaluation instruments on you, and productivity evidence is contested.** Grade: B/C.
- DX shows individual data only to admins [E8 A, vendor docs]. GitKraken reports per-developer and "Power-User" comparisons, AI-assisted share and spend by tier [E89 A, vendor docs]. Jellyfish breaks down adoption and token spend by tool, team and initiative [E91 A, vendor docs]. Atlassian completed its DX acquisition in Nov 2025 [E123 A]. Meta's performance tool counts AI-generated lines among 200+ data points [E111 B].
- Productivity effects are unsettled. METR's 2025 randomized study found developers 19% slower; its 2026 update reports an 18% speed-up for original participants and 4% for new ones, with intervals that include no effect, selection effects and "only very weak evidence" [E63, E64 A]. Jellyfish telemetry claims 2x PR throughput for top-quartile adopters without a stated method [E90 C]. DORA calls AI an "amplifier" of existing strengths and weaknesses [E72 A]. 46% of developers distrust the accuracy of AI output [E99 B].
- Implication: ask in week 1 which dashboards feed your review, and agree outcome metrics rather than activity counts.

**F12. Case library: failures share a shape. Early demo success, an inflated promise, no eval, guardrail or owner, then reversal or liability.** Grade: B (press, tribunal and regulator-adjacent reporting).
- LinkedIn's 80%/95% curve and "unattainable expectations" [E36]; Klarna's reversal [E24]; CBA's reversal ("did not adequately consider all relevant business considerations") [E61]; Air Canada's liability [E35]; Deloitte's partial refund over AI-generated errors in an A$440,000 report [E60, E102]; Replit's agent deleting a production database, followed by dev/prod separation [E101].
- These are organizational cases, not new-hire cases. They show what a new hire inherits, and why the weeks 1-2 diagnostic matters. I found no verified first-person retrospective by a first AI hire beyond anecdotes [E127, E121, E122].

## Recommendation

Run the first 90 days as an expectations-and-evidence program, not as a build sprint. The sources point the same way from different directions: newcomer research says role clarity drives adjustment [E20]; project-failure research says a misunderstood or miscommunicated problem is the first root cause [E1]; and GenAI-specific work says you must convert non-determinism into measured numbers before leadership forms its own picture from a demo [E36, E74]. Everything below is my synthesis (Grade D) of cited mechanics, except where a bracketed source states a fact. No controlled study shows that any 30-60-90 plan reduces early attrition for GenAI engineers (see Open Questions).

### R1. Operating stance

1. **Treat expectations as a deliverable.** Write the problem, the metric definitions and the constraints down in weeks 1-2 and get them acknowledged [E20, E1].
2. **Ship small, measured, reversible increments every week.** LinkedIn's first month produced 80% of the design and the rest took four more months; early progress "creates unattainable expectations" [E36].
3. **Quantify variance before anyone else sees it.** Put pass^k with error bars in every status [E52, E38, E74].
4. **Frame constraints as decisions for an owner** (options, cost of delay, a date), not as complaints.
5. **Keep a paper trail.** GitLab records a probation outcome against "performance" with few written criteria [E82], so your artifacts are the criteria.

### R2. Weeks 1-2: the "AI Expectations Gap" diagnostic checklist

Run it in days 3-10 and score each row green, amber or red. The "Why it matters" column cites the evidence behind each probe; the scoring rule below is my heuristic (Grade D).

| # | Probe (ask or inspect) | Red flag | Why it matters | First action |
|---|---|---|---|---|
| 1 | Which business metric moves? Who owns it and signs off pilot-to-production? | No named owner; the goal is "use AI". | Nobody owns the space between pilot and production [E70]; "no accountable executive" is a recruiter-listed failure mode [E121]; a misunderstood problem is RAND's first root cause [E1]. | One-paragraph problem statement initialed by the owner. |
| 2 | What exactly does "99% accurate" mean: per field, per document or per answer; on which inputs; against which human baseline; what does an error cost? | One headline number, zero-shot, unconstrained inputs, no human fallback. | Parser quality varies by document type and degradation [E135, E136]. "Your pass rate is a product decision" [E42]. "We don't know how accurate the system will be in advance" [E71]. | Define the metric per field and severity; commit to a measured range after the golden-set run, not before. |
| 3 | Show me 20 real inputs with their desired outputs, and where they live. | Nobody can produce them within a week. | 63% of organizations lack AI-ready data practices [E76]; data collection comes before ML [E100]; a "costly initial data collection phase" may be needed [E71]. | Request samples; if none exist, propose a two-week collection and labeling spike. |
| 4 | Who approves data access? Is production or customer data allowed in dev, in LLM APIs and in logs? | No classification; "use what you can find". | Shadow AI adds cost and 97% of organizations with AI incidents lacked AI access controls [E47]; least privilege [E94]. | Classify the input data (audience, objective, input type, classification, technology, output) and file it through the single intake [E104]. |
| 5 | Which model providers, regions and retention terms are approved? | None approved, or nobody knows. | OpenAI: no training on business data by default, API retention up to 30 days, zero data retention on request for eligible endpoints [E113]. Bedrock: model providers have no access to prompts or completions [E103]. | Map your use case to an approved path; request zero data retention where required. |
| 6 | API-only, hosted GPU or self-hosted? What quota exists today, per region and model? | Infrastructure promised in the interview loop is absent or at default quota. | Quotas reward usage history [E31, E32, E66]. | Check quotas on day 1-2; file small requests; start building usage history. |
| 7 | Is there a monthly LLM spend cap, a per-project key or workspace, alerting and cost attribution? | One shared org key; no caps. | Workspace caps and proxy budgets exist [E65, E34]; "denial of wallet" is an OWASP risk [E93]. | Create a per-project key with a budget and a daily spend view. |
| 8 | Is there trace logging, a golden set, a regression test, any baseline (even a heuristic)? | None; "we eyeball it". | Teams without evals "get bogged down in reactive loops" [E74]; a non-ML baseline is the starting point [E29]. | Start logging traces now; draft golden set v0 in week 3. |
| 9 | Has anyone run the same input ten times? Do stakeholders know outputs vary? | Stakeholders believe temperature 0 means identical outputs. | 80 unique outputs from 1,000 temperature-0 samples [E23]; up to 15% accuracy swings [E53]. | Run k=10 on a handful of cases and show the spread. |
| 10 | What happens when it is wrong? Who is liable? Is there a human fallback? | An autonomous expectation for customer-facing, legal or financial output. | Air Canada [E35]; Klarna [E24]; CBA [E61]; Deloitte [E60]. | Define severity classes and a fallback ladder. |
| 11 | Which reviews apply (legal, infosec, privacy, vendor, model risk) and what are their turnaround times? | Unknown, or serial reviews started late. | Adobe's single intake and pre-agreed green scenarios [E104]; SR 26-2 excludes GenAI, so internal policy governs [E10]. | List the gates with owners and SLAs; book early slots. |
| 12 | Which dashboards or tallies feed my review (DX, Jellyfish, GitKraken, AI-usage counts)? | Activity metrics only (lines AI-generated, usage), no outcome metric. | Per-developer comparisons exist [E89]; Meta and Shopify use AI-fluency criteria [E111, E39]. | Ask for the rubric; propose outcome metrics. |
| 13 | What was tried before? Postmortems, abandoned POCs, prompt and eval history? | No history, or nobody who remembers. | Blameless postmortems record contributing causes [E128]; reading prompt history before "cleaning up" a prompt is a practitioner rule (Grade C) [E95]. | Read six months of history; interview the previous owner. |
| 14 | List what was promised in the interview loop (data, GPUs, team, scope) against what you now see. | Two or more material gaps. | 43% said the role differed from what hiring led them to expect [E50]; role clarity predicts adjustment [E20]. | Document neutrally; turn each gap into an owner, a date or a re-scoped milestone. |
| 15 | What did leadership see (a demo?), and when do they expect production? | Dates set from a demo. | The 80%/95% curve [E36]. | Restate as staged milestones with exit criteria. |

**Scoring rule (heuristic).** Rows 1-8 are structural. Three or more reds there means the gap is structural, not a communication glitch: use the reset path in R8 rather than building harder.

### R3. The 30-60-90 plan with weekly deliverables

| Week | Deliverable (artifact) | Done when | Audience |
|---|---|---|---|
| **Days 1-30: establish credibility and map constraints** | | | |
| 1 | Orientation, one small reviewed change merged, access requests filed, six months of prompt/eval/incident history read | First PR merged. The vendor benchmark median is 11 days to first PR, and big tech aims for a production change in week one [E8, E59]. Every access request has a ticket. | Team |
| 2 | Diagnostic scored (R2) and Expectations Contract v1: outcomes, metric definitions, constraints, decision rights, review cadence | Manager has read and signed or commented; open items listed [E96 C] | Manager, owner |
| 3 | Access and Constraints Register (data sources and owners, classification, quotas, budget, gates and SLAs, approved vendors) plus golden set v0 (20-50 real cases) and trace logging on | Every blocker has an owner and a date; a domain expert reviewed the labels [E74, E42] | Manager, platform, security |
| 4 | Baseline report and 30-day readout: heuristic or human baseline against the current system, k=10 runs, pass@k and pass^k with intervals, cost per task, p50/p95 latency; current state, risks, decisions needed, proposed 60/90 criteria | 60/90 criteria agreed in writing | Manager, owner |
| **Days 31-60: make it measurable; first quick wins** | | | |
| 5 | Regression eval suite in CI | Runs on every prompt, model or config change; thresholds gate merges; failing cases link to traces [E74, E25] | Team |
| 6 | Cost and latency instrumentation: per-project key, monthly cap, alerts, cost-per-task dashboard | The owner or finance can see daily spend by feature [E65, E34, E91] | Owner, finance |
| 7 | Quick win #1 behind a flag: caching restructure, batch for offline jobs, or model routing | Eval suite shows no regression beyond error bars, and the cost change is measured on real traffic [E41, E73, E114, E79] | Manager, owner |
| 8 | 60-day readout and first blameless postmortem of a real failed case | Owner decisions logged (accuracy definition, human-review scope, budget) [E128] | Manager, owner |
| **Days 61-90: own something in production and formalize** | | | |
| 9 | Vertical slice in production or shadow mode with human review and a tested rollback | Real inputs flow and traces return | Users, owner |
| 10 | Compliance packet: intake form, data-flow diagram, vendor retention terms, risk register mapped to NIST AI 600-1 and the OWASP LLM Top 10 | Required reviewers signed or listed conditions [E104, E92, E93, E94] | Security, legal, privacy |
| 11 | Judge or rubric calibration if LLM-as-judge is used: hand-label about 100 production traces and compare with the judge; otherwise grow the golden set from production traces | Agreement reported with the rubric. A ">0.7 correlation" target is "widely cited" without a source, so treat it as a starting point [E95 C, E107]. | Team |
| 12 | Ownership and runbook: you own one feature, eval or judge, including regression and recalibration after model upgrades | A teammate can run it on call without you [E95 C] | Team |
| 13 | 90-day readout: results against the signed criteria, trends in quality, cost and latency, pending decisions, next-quarter plan with kill criteria and a "what we will not promise" list | The probation or confirmation conversation holds no surprises [E96 C, E82] | Manager, skip-level |

**Weekly rhythm.** Monday: add last week's failures to the golden set. Friday: a one-page update (template in R6). Every 1:1: the top three decisions you need, with owners and dates.

**Setting-specific adjustments (synthesis, Grade D).** No source documents startup-vs-GCC probation practice; these contrasts build on [E68, E70, E118, E129, E137, E138, E139, E140].

| Setting | Compress or expand | Emphasize | Watch for |
|---|---|---|---|
| Venture-backed startup | Compress: a production-touching change by week 2-3, the first eval suite by week 4. The Expectations Contract can be a one-page message to the founder. | Shipping cadence, scope judgment, cost discipline (credits are finite and conditional). Ask what "good at 90 days" means, in writing; probation may be informal. | No data owner; demo-driven founder expectations; credits that do not cover third-party models [E137]. |
| Enterprise engineering org (non-GCC) | Expand weeks 2-4 for intake and approvals: file the intake in week 2. | Security and privacy hygiene; cost allocation; platform dependencies. | Shadow AI temptations [E47]; approval queues; tool procurement. |
| India GCC | Expand weeks 1-4 for stakeholder mapping: identify the dual mandate (global parent against India leadership). | Who sets priorities, owns data and budget, approves tools. Get probation terms and review dates in writing. Assume parent-company security and data rules and Indian law (DPDP phases) both apply. Name a pilot-to-production owner [E68, E70]. | Pilots that never graduate; governance handled "after the fact" [E68]; remote stakeholders across time zones. |

### R4. Securing compute, API budget and data permissions

**Ten moves.**
1. **Start API-first and prove value before asking for GPUs.** Anthropic recommends "the simplest solution possible" [E77]; Google's Rules of ML says launch without ML if you can [E29]; large GPU asks without usage history are the ones denied [E31].
2. **Build usage history deliberately.** Steady, active use improves odds with quota systems: "priority goes to customers who actively use their existing quota" [E32]; tiers rise with usage history [E66]. Ask for increments proportional to history.
3. **File quota requests early, with numbers.** Size the workload (tokens per day or GPU-hours, duration, region, fallback). AWS quotas are per region and counted in vCPUs, Spot and Capacity Blocks are separate, and some quotas are not adjustable and need a support case [E31].
4. **Install your own guardrails first.** A per-project key with a budget and alerts [E65, E34] makes finance comfortable and matches OWASP's mitigations for unbounded consumption [E93].
5. **Use cost levers before asking for more budget.** Caching, batch and routing (D10), each verified against your eval suite [E41, E73, E79, E114].
6. **Ask whether the company has applied for credits, and read the conditions.** Google: up to $350,000 for Scale-tier AI startups that build on Gemini, third-party models excluded [E137]. AWS Activate: Portfolio up to $200,000 with an Org ID from an Activate provider; credits are redeemable for third-party Bedrock models [E138, E139]. Microsoft: most startups begin with $100,000 through an investor offer; no-investor credit is $1,000 for 90 days then $4,000 for 180 days; Azure OpenAI coverage is not stated on the FAQ page [E140]. India: the IndiaAI portal offers subsidized GPUs at about Rs 65 per GPU-hour for eligible startups and academia, with allocation by eligibility and requested hours [E48, E49]. All of these are conditional and change; verify live.
7. **Classify data first, then ask.** Use the intake's six data points to get a risk score, and propose "green" scenarios (low-risk data, no external users) for fast-tracking [E104]. Start with public, synthetic or redacted data. Request production samples with a stated purpose and retention plan, under least privilege [E94].
8. **Use approved providers with contractual terms you can cite.** OpenAI's enterprise privacy page: "By default, we do not use your business data for training our models"; API retention up to 30 days; zero data retention for eligible endpoints [E113]. Bedrock: model providers have no access to prompts or completions [E103]. Check your own organization's contracts, which may differ.
9. **Pre-wire the gatekeepers.** Meet infosec, legal and privacy before you need them; ask for SLAs; use one intake channel; keep a tech radar of approved tools (Adobe's lessons) [E104].
10. **Escalate by decision memo**: options, cost of delay and a date, not a complaint. Log every ask and its outcome in the Access Register.

**What not to do:** route around controls with personal accounts or unapproved tools. Shadow AI added $670,000 to the average breach cost in IBM's 2025 data [E47].

**When the promised infrastructure is missing ("no data, no compute").** This is the common case [E76, E129]. A sequence that fits the evidence:
1. Verify in the first 48 hours: quotas, data catalog, access, approved vendors (R2 rows 3-7).
2. Record the gap against what was said in interviews, neutrally and in writing (R2 row 14).
3. For the first 30 days, take the API-first path and a public or synthetic golden set so evaluation work is not blocked on approvals [E77, E29].
4. Request the minimum access with a sized business case and a classification (move 7).
5. Propose a short data-collection or labeling spike with an owner, since "a costly initial data collection phase" is a normal cost, not a failure [E71].
6. Re-baseline the milestones with the owner, and put the new dates in the Expectations Contract.
7. Track "cost of delay" per week in your status, so the decision belongs to the person who can unblock it.

### R5. Probation scorecard: what to ask your manager to confirm at day 14

The only quantitative onboarding metrics with public definitions are time to first and 10th PR plus a roughly 90-day sentiment survey [E8]. The rest below is my proposal (Grade D), with sources for each metric's definition.

| Dimension | By day 30 | By day 60 | By day 90 | Metric and source |
|---|---|---|---|---|
| Delivery | First PR merged; small change shipped | About 10 PRs or equivalent shipped | Owns a feature end to end | Time to first and 10th PR; vendor medians 11 and 50 days [E8] |
| Evaluation | Golden set v0 (20-50 cases) and traces | Regression suite gating merges | Judge calibrated; incidents become tests | Case count; share of incidents converted to tests [E74, E25] |
| Reliability reporting | pass@k and pass^k with intervals | Trend across releases | Variance targets agreed with the owner | pass^k, confidence intervals [E52, E38, E74] |
| Cost and latency | Baseline cost per task, p95 latency | One measured saving shipped | Budget cap, alerts, forecast | % change on real traffic with no quality regression [E41, E73, E114] |
| Expectations and communication | Contract signed; 30-day readout | 60-day readout; decisions logged | No surprises at review | Written 30/60/90 check-ins [E96 C, E20] |
| Risk and compliance | Access and Constraints Register | Intake filed | Compliance packet signed | Intake status; risk register [E104, E92, E93, E94] |
| Operations | Shadowed on-call; read postmortems | First blameless postmortem | Runbook; on-call ready | Postmortems written; time to detect [E128, E95 C] |
| AI fluency (only if the employer uses it as a criterion) | Ask how it is measured | Show a verified AI-assisted workflow | Document where AI did and did not help, with data | Shopify and Meta criteria [E39, E111, E112]; productivity evidence is contested [E63, E64] |

**Emphasis by setting (synthesis, Grade D).** Startups: delivery speed, scope judgment and cost discipline carry more weight, and the formal rubric may be absent, so write one. GCCs: expect heavier weight on stakeholder alignment across geographies, documentation, delivery predictability and compliance hygiene, and get the review calendar and confirmation terms in writing, since probation is typically about six months and not capped by a central law [E118 C]. If your manager will not state criteria by day 14, that is itself a finding (R8).

### R6. Managing upward on non-determinism

1. **Replace "accuracy" with a distribution.** Show the same input ten times. Explain pass@k (at least one success) against pass^k (all k succeed) and say which one the use case needs: "pass@k for tools where one success matters, pass^k for agents where consistency is essential" [E74, E52].
2. **Show error bars and sample sizes.** Avoid claiming one-point gains on 50 cases [E38].
3. **Make the acceptable failure rate an explicit product decision**, per failure type and severity [E42].
4. **Offer a fallback ladder:** heuristic, then LLM with human review, then autonomy for a low-risk slice. Human editing is an acceptable design [E29].
5. **Pre-commit to an experiment, not a number.** "We don't know how accurate the system will be in advance; this two-week experiment will tell us" [E71].
6. **Show the LinkedIn curve.** A demo reaches about 80% quickly; the last stretch takes most of the time. Ask stakeholders to plan on that shape [E36].
7. **Name the engineering variance and its cost.** Run-to-run differences at temperature 0 have a known cause (batch variation), and deterministic inference costs throughput [E23]. Provider seed behavior is best-effort in my memory but unverified here (Grade D).
8. **Use the cost-quality-latency triad.** "Agentic systems often trade latency and cost for better task performance" [E77].
9. **Keep a decision log and a weekly written update.** Blameless postmortems with criteria defined before incidents keep failures from becoming personal [E128].

Illustrative weekly update (numbers are invented for format only):

```
Weekly update (one page)
1. Metric: pass^5 on golden set v3 = 71% (95% CI 62-79%, n=60); last week 68%.
2. What changed: prompt v14 gained 3 points on invoice totals; no change elsewhere.
3. Variance: same input x10 gave 7 identical outputs; failure types A and B.
4. Cost and latency: $0.031 per task (-18% vs baseline); p95 4.2 s.
5. Decisions needed (owner, date): accuracy definition for totals vs line items; human review above $10k.
6. Next week: grow set to 80 cases; test cache restructure.
```

### R7. Compliance, security and political cross-currents: how to navigate

| Gate or instrument | Status as of Oct 2026 | What it means for a new GenAI engineer | Source |
|---|---|---|---|
| US bank model risk management | SR 26-2 (17 Apr 2026) supersedes SR 11-7 and excludes generative and agentic AI from scope; "separate guidance or rulemaking will address AI-related risks" | Do not assume "SR 11-7 approval" applies to an LLM feature. Ask which internal policy covers it and whether it borrows "effective challenge" practices. | [E9, E10, E43] |
| EU AI Act | Omnibus (Reg. 2026/1744) in force 27 Jul 2026: Annex III high-risk to 2 Dec 2027, Annex I to 2 Aug 2028; GPAI duties continue; two new prohibitions from 2 Dec 2026 | Confirm whether the product touches the EU and which tier applies before assuming a deadline. | [E12, E13] |
| India DPDP | Rules notified 13 Nov 2025; consent-manager rule 13 Nov 2026; core duties 13 May 2027 (12 May per one firm); a Removal of Difficulties Order (Oct 2026) amended ss. 9(1) and 10(2)(c)(ii) and left timelines unchanged | Start a data inventory and consent/notice mapping now. Verify exact dates on the Gazette. | [E14, E80, E81, E44] |
| RBI FREE-AI | Committee framework: seven sutras, six pillars, 26 recommendations; binding status not stated in the source | For regulated Indian entities, use it as a checklist of expected controls. | [E46] |
| NIST AI 600-1 and OWASP LLM Top 10 | NIST profile lists 12 GenAI risks; OWASP LLM02 and LLM10 cover data disclosure and runaway cost | Shared vocabulary for risk registers and security reviews. | [E92, E93, E94] |
| Shadow AI and access control | IBM 2025: shadow AI added $670,000 to breach cost; 97% of organizations with AI incidents lacked AI access controls | Use approved paths; expect infosec to ask for access-control evidence. | [E47] |
| Vendor data terms | OpenAI API: no training by default, up to 30 days retention, zero data retention on request for eligible endpoints; Bedrock model providers have no access to prompts or completions | Quote the clause in your intake; confirm your own contract. | [E113, E103] |
| Legal liability | Air Canada was held responsible for chatbot statements (CA$650 damages) | Treat outputs as company statements; define fallback and disclosure. | [E35] |
| Internal AI intake | Adobe: single intake, six data points, risk score, pre-agreed "green" scenarios, tech radar | Copy the structure if none exists; it shortens reviews for low-risk work. | [E104] |
| Political: AI mandates and savings narratives | Shopify and Meta tie AI fluency to reviews; Klarna and CBA reversed AI-first moves | Make claims you can defend with measured numbers; avoid being the public face of unmeasured savings. | [E39, E111, E112, E24, E61] |

### R8. Escalation and exit rules (heuristic, Grade D; not legal advice)

- **Green:** at most one red in R2 rows 1-8, and every red has an owner and a date by day 30. Proceed with R3.
- **Amber:** two reds, or any red without an owner. Send a one-page expectations-reset memo to your manager and the owner: what is known (baseline data), what is not, options (reduce scope, add human review, fund data collection, extend the timeline), cost of delay, and the decision needed by a date.
- **Red:** three or more reds in rows 1-8 after day 30 despite the memo, or the success criterion is "autonomous 99%" with no fallback and no owner for data or budget. Treat the role as mis-specified: get the 60/90 criteria rewritten in writing, escalate through your normal management chain, keep records, and start exit planning in parallel.
- **Contract check:** India has no central cap on probation, so probation length, notice and confirmation terms come from your contract and applicable standing orders [E118 C, E117 B]. Read yours in week 1.

## Alternatives Considered

| Alternative | Why it is tempting | Verdict | Evidence |
|---|---|---|---|
| Heads-down build first, communicate later | Avoids politics and shows output | Rejected | A misunderstood or miscommunicated problem is RAND's first root cause [E1]; early progress creates "unattainable expectations" [E36]; role clarity predicts newcomer adjustment [E20]. |
| Wait for GPUs and data before delivering | The interview loop promised them | Rejected as a default; accept only where self-hosting or fine-tuning is truly required | "Simplest solution possible" [E77]; launch without ML if you can [E29]; quota systems reward usage history, so waiting builds none [E31, E32]. |
| Promise a headline quick win publicly in week 1 (for example "cut tokens 40%") | Fast credibility | Modified: commit to measuring, not to a number | Savings are workload-dependent: 41-80% for caching in one preprint [E114], a method-less 70% blog claim [E105]. Klarna and CBA show reversals after over-claiming [E24, E61]. |
| Use a generic manager-oriented 30-60-90 template | Familiar and quick | Rejected as the main tool; fine for cadence | Templates exist (for example a marketplace "30-60-90" Notion portal [E87 C]) but carry no AI-specific checks. Other manager-oriented plans surfaced in search were not opened. |
| Treat early attrition as a pay problem | The AI labor market is hot | Partly rejected | Compensation ranks seventh for gen-AI heavy users [E134]; GCC high performers' exit drivers are "none ... compensation" [E16]; in a vendor's India AI-engineer survey, no growth (39%) outranks a better offer (21%) [E146 C]. But a better offer is still the second-named reason, an unsourced vendor blog claims outside offers pay 35-50% more [E98 C], and AI/ML attrition is higher than for software engineers in Pave's data [E97]. Stated and revealed reasons can differ. |
| Measure your success by AI-usage counts (a Meta-style tally) | Easy to track | Not recommended as the sole measure | Meta's tool counts AI-generated code among 200+ data points, and HR calls it "an impact-evidence starter" [E111]. Productivity evidence is contested [E63, E64]. |
| Exit early instead of resetting scope | Avoids sunk cost | Conditional; see R8 | No evidence on outcomes either way (Grade D). |

## Detailed Findings

### D1. The 35% claim: queries run and the nearest numbers

**Queries** (web search; first-page results inspected; none surfaced a primary source for 35%). Fifteen logged queries or query groups, run 2026-10-21 to 2026-10-23.
1. Earlier-session searches on the claim's own wording (35%, AI engineering hires, friction, performance reviews, early departure, six months), logged as one group of several wording variants. The best hit was a listicle with no traceable statistic [E27 C]: it contains no figure about AI engineers failing probation or leaving early, only unsourced team-level numbers attributed to "Pluralsight 2024", "SHRM 2025" and "IEEE Software 2024".
2. `"35%" AI engineers hires leave OR departure OR attrition "within six months" OR "first six months" ambiguous expectations data access GPU` returned contact-centre and retention blogs, Fortune on McKinsey [E125], HR Executive [E124] and techtree.dev [E126].
3. `AI engineer new hire failed probation OR "let go" OR resigned first months unrealistic expectations leadership LLM project no data access` returned employee-review and Blind posts: anecdotes [E127].
4. `early attrition new joiners first 90 days India GCC IT services offer dropouts joining ghosting survey 2026` returned a 2017 NASSCOM community post [E119] and a 2026 PlugScale blog [E120], both unsourced.
5. `"AI expectations gap" leaders engineers AI projects` returned [E108, E109, E110].
6. `first AI engineer hire startup lessons learned first 90 days no data no evals expectations founders` returned [E121, E95, E122].
7. `"35%" AI engineers new hires leave within six months unclear expectations lack of data access compute` returned the same recruiter and retention blogs, HR Executive [E124] and the listicle [E27]; no new source.
8. `survey machine learning engineers new hires waiting for GPU access and data access delays onboarding productivity 2026` returned a cloud-vendor GPU-scarcity survey [E142], a vendor onboarding statistic relayed by a third site [E147] and a vendor-authored HPC article [E148]. None measures how long a new hire waits for compute or data.
9. `AI talent retention report 2026 early attrition AI engineers first year turnover percent survey` returned India attrition coverage, a gated AIM Research study of AI and data professionals [E144] and Zinnov [E16].
10. `AI engineers unrealistic leadership expectations data quality attrition survey percent quit within first year 2026` returned a UK data-leader survey [E141], Upwork's AI-attrition release [E145] and a Qlik data-quality survey [E143].
11. `AI engineering hires "performance improvement plan" OR "failed probation" OR "early departure" percent ambiguous business goals study` returned a PIP template, the listicle [E27] and a gated Udemy page with three unsourced statistics [E151 C].
12. `"one in three" OR "35 percent" OR "35%" AI engineers hires quit OR leave OR "performance review" first six months expectations` returned the same pages plus a vendor survey of India AI engineers [E146].
13. Lookup of Upwork's "Great AI Attrition" release: its own page failed to load, so a syndicated copy was read [E145].
14. Lookup of AIM Research's India attrition studies [E144, E149].
15. Lookup of the Lucent Search 2025 survey: one article found [E141]. A DataIQ survey that surfaced alongside it is a different study with no quit-intent figure [E150 B].

Pages opened for numbers: Pave [E97], SignalFire [E18], Zinnov [E16], EY [E69], McKinsey [E134] and, from the later queries, Wisemonk [E146], DecisionMarketing on Lucent Search [E141], AIM Research [E144, E149] and Upwork's release through a syndicated copy [E145]. Gallup's page, fetched for an onboarding statistic recalled from memory, contained none, so that recalled figure stays unverified [E51].

**Nearest numbers, with what they measure.**

| Metric | Value | Population and window | Realized or intent | Source |
|---|---|---|---|---|
| Plan to quit within 3-6 months | 34% of all workers; 51% of gen-AI creators and heavy users | 12,802 workers in Canada, UK, US; fielded 28 Jul-15 Aug 2023 | Intent | [E134 A] |
| Quit within the first 90 days | 33% | 1,500 US workers; Jobvite 2018 via press | Retrospective | [E50 B] |
| "Have quit a job within the first six months" | 31% | 1,005 US employees; BambooHR 2015; wording means ever | Retrospective | [E19 B] |
| Annual attrition, AI/ML ICs | 28% (AI/ML managers 22%) against 17% for software engineers | Pave customer data; sample undisclosed; 2025 | Realized, annual | [E97 B-] |
| Attrition, India GCCs overall | 16% (Zinnov 2026) against 9% (EY 2025; EY's release gives no respondent count) | Different samples and definitions | Realized, annual | [E16 B, E69 A-, E17 B] |
| Attrition, India GCC AI and Cloud roles | 18-25% | Zinnov SIAH 2026 | Realized, annual | [E16 B] |
| Attrition of frontier AI roles in India | GenAI, LLM and MLOps roles "significantly higher" than enterprise data roles; no figures visible | AIM Research, 29 Apr 2026; report gated | Direction only | [E144 B] |
| Attrition, India data analytics industry | 18% in 2023 against 28% a year earlier | AIM Research; sample and method not stated; AI roles not mentioned | Realized, annual | [E149 B] |
| Two-year retention at frontier labs | Anthropic 80%, DeepMind 78%, OpenAI 67%, Meta 64% | LinkedIn-derived; hired 2023-2024 | Retention, not early | [E18 A] |
| Average tenure of AI engineers | "roughly 22 months in 2026" | No named study | Unsourced | [E98 C] |
| Dissatisfied new hires planning to leave within the first year | 78% | Page meta description only; sponsor and sample unnamed | Intent | [E124 C] |
| Plan to quit within 12 months | "Nearly two-thirds" of UK data leaders | Lucent Search survey 2025 via trade press; sample and method not stated; leaders, not engineers | Intent | [E141 C] |
| What pushed India AI and ML engineers out of a role early | No growth 39%; better offer 21%; broken promises 19%; poor management 18%; boredom 4% | 200+ respondents, Jul-Sep 2026; a vendor's own voluntary survey; question wording and response base not stated | Stated reasons, not a rate | [E146 C] |
| Early-stage-startup employees' odds of switching within six months | 29% higher odds than Big Tech peers | 2,830 Bay Area profiles; no baseline, method or date | Odds ratio | [E126 C-] |
| Offer drops and 45-day exits | 37% drop offers in India; 22% of new hires leave within 45 days (global) | 2017 blog; no sources | Unsourced | [E119 C-] |

No row gives a realized early-exit rate for AI hires with causes attributed to expectations, data or compute. The closest in subject, the India AI-engineer survey, reports only the mix of stated reasons, and its "broken promises" share is 19%.

**Possible origin of "35%" (Grade D).** The 34% general-workforce intent figure is the nearest number. A conflation of it with the 51% gen-AI heavy-user figure and with generic "friction" language is plausible but unverifiable.

### D2. The expectations gap: how the label is used and what the failure statistics measure

Usage of the label: vendor material only [E110, E109], plus an executive's 2022 quote [E108]. None defines the term or measures it.

| Statistic | Value | What it actually measures | Type | Source |
|---|---|---|---|---|
| RAND | ">80%" fail | Not measured by RAND: "By some estimates", cited to Fortune (Jul 2022). RAND itself ran 65 interviews (50 industry, 15 academia); failure means perceived as failure by the organization. | Second-hand | [E1 A] |
| Gartner | 30% of GenAI projects abandoned after PoC by end-2025 | Prediction (Aug 2024 reprint); causes named: poor data quality, inadequate risk controls, escalating costs, unclear business value | Prediction | [E3 B] |
| Gartner | More than 40% of agentic AI projects cancelled by end-2027 | Prediction; a Jan 2025 poll of 3,412 webinar attendees; "agent washing" noted | Prediction | [E2 A] |
| Gartner | 60% of AI projects abandoned through 2026 if unsupported by AI-ready data; 63% of organizations lack or are unsure of data practices | Prediction plus a survey whose sample is inconsistent on the page (1,203 vs 248) | Prediction and survey | [E76 A] |
| S&P Global Market Intelligence | 42% of companies abandoning most AI initiatives (17% a year earlier) | Survey of more than 1,000 respondents, North America and Europe | Survey | [E6 B] |
| IBM IBV | 25% of AI initiatives delivered expected ROI; 16% scaled enterprise-wide | 2,000 CEOs, 33 countries, fielded Feb-Apr 2025 | Survey | [E75 A] |
| MIT NANDA | "95%" getting zero return or failing | 52 organization interviews, 153 survey responses at four conferences, 300+ public deployments; success = beyond pilot with measurable KPIs, ROI measured six months after the pilot; "directionally accurate based on individual interviews rather than official company reporting"; the denominator shifts between "organizations" and "enterprise AI solutions". Press coverage described the sample differently (about 150 leader interviews and a 350-employee survey) [E4], another sign that secondary accounts of this report vary | Mixed | [E130 A-, E4 B] |
| Critique of MIT NANDA | Scope limited to custom, task-specific agentic implementations that reach production with measurable P&L impact; "fundamentally biased by an underlying agenda" | Opinion piece; also describes the sample differently ("about 150 survey responses and 52 structured interviews") | Opinion | [E5 C] |
| Dell-Zinnov | "Nearly 70%" of India GCCs at the AI pilot stage | More than 50 senior GCC leaders per a trade-press report; the whitepaper page states no sample | Survey | [E68 B, E129 A-] |
| LinkedIn | 80% of the design in month one; four more months for the rest | One company's account | Case | [E36 B] |

**Reading.** The pattern is consistent across sources (stalls between pilot and production, data and governance barriers, unclear value). The magnitudes are not comparable: definitions of "failure" range from "perceived as failure" to "no P&L impact within six months", and two of the best-known numbers are predictions. MIT's own diagnosis ("learning gap", not infrastructure, regulation or talent) partly cuts against a pure data-and-compute story [E130].

### D3. Case library

| Case | Promise or assumption | What happened | Lesson for a new hire | Source |
|---|---|---|---|---|
| LinkedIn GenAI product (2024) | Quick progress from an early build | 80% of the basic design in month one; the remaining stretch took four more months; metrics on hallucination rate, responsible-AI violations, coherence and style | Pre-brief leaders on the curve; invest in evaluation of a "subjective, non-deterministic product" | [E36 B] |
| Klarna (2025) | AI-driven customer service and a hiring freeze | Rehiring human agents; CEO: "investing in the quality of human support is the way of the future for us" | Keep a human fallback; report quality with cost | [E24 B] |
| Commonwealth Bank of Australia (Aug 2025) | 45 customer-service roles replaced by an AI voice bot | Reversed; the bank said it "did not adequately consider all relevant business considerations" and the roles were not redundant; a union said call volumes were rising | Business-case assumptions need measurement before commitments | [E61 B] |
| Air Canada, Moffatt (Feb 2024) | A chatbot as a separate source of information | Tribunal held the airline responsible for the chatbot's statements; about CA$650 in damages plus interest and fees | Outputs are company statements; define guardrails and disclosure | [E35 B] |
| Deloitte Australia (Oct 2025) | An AI-assisted report for a government client | A$440,000 report with apparent AI-generated errors, a fabricated quote and nonexistent references; partial refund | Add a verification step and provenance checks | [E60 B, E102 B] |
| Replit and a "vibe coding" experiment (Jul 2025) | An agent working in a live project | The assistant deleted a production database (a pet project); Replit promised automatic dev/prod separation, staging and backups | Enforce environment separation and least privilege for agents | [E101 B] |
| Anonymous senior ML engineer (Jun 2024) | An ML role | Terminated on probation about three months after the offer; says the work was data engineering and troubleshooting, onboarding was recorded videos, "few or zero guidance" | Role-content mismatch and thin onboarding are visible in week 1; clarify early | [E127 C] |
| A Series B's first AI hire (recruiter anecdote) | A first AI hire who would produce product | Left at eight months after about $200,000 in salary "had produced nothing customers used" | No accountable executive, no success measure, wrong profile | [E121 C] |

### D4. Early attrition: what is known, and why the numbers conflict

- **General newcomer research.** A meta-analysis of 70 samples ties role clarity, self-efficacy and social acceptance to adjustment, and adjustment to performance and turnover [E20]. A meta-analysis of psychological-contract breach exists, but I could not retrieve its abstract or effect sizes [E21]. Retrospective surveys report 31-33% leaving within six months or 90 days [E19, E50], and 43% citing a role that differed from what hiring led them to expect [E50].
- **AI-specific signals.** Intent to quit is higher among gen-AI heavy users (51% against 34%) [E134]. Annual attrition is higher for AI/ML ICs (28%) than for software engineers (17%) in one vendor's data [E97]. India GCC AI and Cloud attrition is 18-25% [E16]. AIM Research reports higher attrition for GenAI, LLM and MLOps roles than for enterprise data roles in India, direction only because the report is gated [E144 B]. Upwork's release says top AI performers are twice as likely to quit and ties quitting to opaque AI strategy and mismatched expectations, with no sample or method on the page [E145 C]. A UK survey puts quit intent among data leaders at nearly two-thirds, naming vague mandates and pressure for rapid ROI among the reasons, method not stated [E141 C]. None of these measures early exits.
- **Why sources conflict.** They differ in definition (attrition, retention, intent), population (all workers, AI roles, GCC staff), window (45 days to annual) and data source (vendor payroll, LinkedIn profiles, surveys). Zinnov's 16% and EY's 9% for India GCC attrition cannot both describe the same population and definition; EY discloses no respondent count [E16, E69].
- **Stated drivers.** Skill momentum, autonomy/scope and recognition for GCC high performers [E16]; meaningful work, supportive coworkers and caring leaders for gen-AI workers, with compensation low; McKinsey's own podcast framing is that "Compensation is not the driving factor here" [E134, E125, E133]. In the India AI-engineer vendor survey, no growth (39%) and a better offer (21%) lead the reasons for leaving a role early, "broken promises" is 19%, and compensation is the least-named reason to stay (4%); "broken promises" is defined there as a role sold as one thing that turned out to be another in scope, ownership or growth path [E146 C]. A vendor blog asserts a 35-50% outside-offer premium against 10-15% internal raises, unsourced [E98 C].
- **Implication.** You cannot quantify your personal early-exit risk from public data. Manage the controllable mechanism: clarity of role and success criteria, access, and visible evidence of progress.

### D5. Structural obstacles in more detail

**Data and documents.**
- Prevalence. 81% of 500 US AI professionals in a Qlik-sponsored survey report significant data-quality issues at their company, and 85% believe leadership is not addressing them (fielded 4-18 Feb 2025; vendor-sponsored) [E143 C]. A statistic relayed from another vendor says 43% of new hires wait more than a week for tools; it concerns basic workstation logistics and states no sample or method, so it is a weak signal [E147 C-].
- OmniDocBench (CVPR 2025): nine document sources, 19 layout categories and 15 attribute labels; general vision-language models "generalize better to unconventional formats (e.g., notes)", "struggle with high-density documents like newspapers" and "perform more robustly under degraded conditions (e.g., fuzzy scans)" [E135].
- PureDocBench (2026 preprint): 1,475 pages, 10 domains, 66 subcategories, each in clean, digitally degraded and real-capture versions (4,425 images), 40 models; "document parsing is far from solved: the best model scores only ~74 out of 100, with a 44.6-point gap" between best and weakest; general vision-language models lose only 0.99 and 8.52 Overall points under digital and real degradation [E136].
- Caveat: both score text, formula and table parsing, not field-level business correctness. They show that "zero-shot on unstructured PDFs" is an empirical question that depends on document type and capture quality. Sample 50-100 of your own documents, define field-level metrics with severity weights, and measure before agreeing to any percentage.

**Compute and budget mechanics.**

| Mechanism | What the documentation says | Gotcha | Source |
|---|---|---|---|
| AWS GPU instance quotas | Counted in vCPUs, per region; P-family instances share one On-Demand quota; Spot and Capacity Blocks separate; increases via Service Quotas; approval "typically 15 min - 48 hours" | Some quotas are not adjustable (support ticket); denials are linked to "limited usage history or a very large increase" | [E31] |
| Azure OpenAI / Foundry | Tokens-per-minute quota per subscription, region, model and deployment type; default quota on onboarding; more via a request form | "Priority goes to customers who actively use their existing quota allocation. Requests that don't meet this condition might be denied"; no processing time stated | [E32] |
| Claude API | Tiers set by "usage history and account standing"; limits rise as history builds; per-workspace spend and rate limits | Workspace limits can be lower, not higher, than the organization's; no spend limits on the Default Workspace; the rate-limits page lists monthly spend caps by tier (as fetched: $500, $1,000, $200,000, none), verify live | [E65, E66] |
| OpenAI Batch API | Separate rate-limit pool; 24-hour window; 50% discount | Offline workloads only | [E73] |
| LiteLLM proxy | Team budgets with `max_budget` and `budget_duration` | Exceeding returns HTTP 422 `budget_exceeded` (configurable to 429) | [E34] |
| IndiaAI compute portal | 38,000+ GPUs for Indian startups and academia; about Rs 65 per GPU-hour; allocation "determined by eligibility, requested compute hours and subsidy requirements" | Training takes about 80% of GPU hours; over 60% of requesting startups want inference; "unlikely to close India's AI capability gap on its own" | [E48 B, E49 A-] |
| Startup credit programs | Google up to $350,000 (AI startups); AWS Activate up to $200,000 (Portfolio); Microsoft typically $100,000 (investor offer) | Stage, funding-source and age conditions; Google excludes third-party models; Microsoft's FAQ is silent on Azure OpenAI | [E137, E138, E139, E140] |
| FinOps practice | 98% of 1,192 respondents manage AI spend (up from 31% two years earlier) | A survey of FinOps practitioners, so skewed toward mature cost programs | [E33] |
| GPU scarcity (survey) | 85% of 1,367 AI professionals work for organizations that have delayed projects because of limited GPU access; 39% put the delays at three to six months | Sponsored by a GPU-cloud vendor (Civo); organization-level, not per hire; no data on how long a new hire waits. A vendor-authored article says access takes "weeks when it could take days" without measurements | [E142 C, E148 C] |

**Evaluation and non-determinism.** Hamel Husain's three levels are unit tests, model and human evaluation, and A/B testing; "A prerequisite to performing human and model-based eval is to log your traces"; "You must remove all friction from the process of looking at data" [E42]. Evan Miller: "evaluations are experiments", so use experiment-analysis practice such as error bars [E38]. "Criteria drift": "users need criteria to grade outputs, but grading outputs helps users define criteria", and LLM-generated evaluators "inherit all the problems of the LLMs they evaluate" [E107]. Reliability decays with repetition: pass^8 under 25% in tau-bench retail [E52]. Interviews with 18 ML engineers found "three variables that govern success for a production ML deployment": velocity, validation and versioning (2022, dated, pre-LLM) [E106].

**Governance.** See D9 for details and discrepancies.

### D6. What is public about success criteria for new hires

| Artifact | Setting | What it defines | Grade |
|---|---|---|---|
| Onit "AI Engineer" and "Senior AI Engineer" postings, Pune on-site | Product company, India | 90 days: ship one production agent workflow with tracing and observability, an offline eval suite with regression gates, cost and latency targets with monitoring, documented failure modes and fallback [E25, E26] | A (postings) |
| deeprec "ML Engineer, LLM Evals and Agent Systems", London hybrid, early-stage | Startup | No 30/60/90 criteria; work with founders; shape the AI engineering function [E28] | A (posting; negative result) |
| Backbase "Principal AI Evaluation Engineer", Hyderabad | Enterprise software | No 30/60/90 criteria [E62] | A (posting; negative result) |
| DX onboarding metrics | Vendor docs | Time to first and 10th PR, 90-day sentiment survey; benchmark P50/P75/P90 of 11 / 6.4 / 3 and 50 / 43.6 / 28 days; surveys at tenure of 85-120 days; SRE and manager personas excluded; individual data visible only to admins; benchmark provenance not stated [E8] | A (vendor) |
| Spotify and Backstage | Large engineering org | Onboarding metric "time-to-merge your 10th pull request", from about 60 days to under 20 [E7] | A (vendor-promotional) |
| Pragmatic Engineer, "Onboarding to a New Company" | Big-tech practice | Clear goals for all, a buddy from day one, a production change in the first week, a tailored plan on day one, a check-in at about a month; rest paywalled [E59] | B |
| GitLab handbook | Remote-first company | Probation 1-9 months by location (India listed); halfway review; manager reminder 28 days before the end; outcome based on "performance" [E82] | A |
| Shopify memo coverage | Tech company | "Reflexive AI usage is now a baseline expectation"; coverage paraphrases AI proficiency as a performance-review factor [E39] | B |
| Meta memo and tool coverage | Big tech | "AI-driven impact" a core expectation from 2026; AI-usage metrics excluded from 2025 reviews; a tool counts AI-generated lines among 200+ data points; top ratings eligible for 200% bonus multipliers [E111, E112] | B |
| tianpan playbook and career ladder | Practitioner blog | Shadow, then three supervised artifacts, then narrow ownership; evals as the clearest seniority signal [E95, E131] | C |
| techinterview "expectations contract" | Practitioner blog | Written, co-authored success criteria at 30/60/90 with check-ins; "No surprises at 6 months" [E96] | C |
| KORE1 and Recruiting from Scratch | Recruiters | First 90 days: map where data lives, ship one small feature that moves a metric plus an eval harness; "evals are the job" [E121, E132] | C (vendor) |
| Teamed (employer of record) | India probation guidance | Written pass criteria at the start, reviews at about 30 and 60 days and before the end, written confirmation with reasons [E118] | C (vendor) |

**How managers evaluate new AI hires at 30/60/90, and which metrics are tracked.** Not found: manager 1:1 rubrics or probation scorecards from named engineering leaders for GenAI hires, in startups or GCCs. What exists is in the table: a job-posting version of 90-day deliverables, a vendor definition of onboarding metrics, AI-fluency criteria at two large companies, GitLab's probation mechanics, and Grade C practitioner plans. R5 is my synthesis.

### D7. Startup vs GCC vs enterprise: which contrasts are documented

| Claim | Status | Evidence |
|---|---|---|
| GCC AI initiatives stall between pilot and production | Documented (B) | "Nearly 70%" stuck at pilots; "nobody owns the space between a successful pilot and a production deployment" [E68, E70, E129] |
| GCC leaders face dual global mandates | Documented (B; trade-press report of a survey of more than 50 leaders) | 64% report dual global mandates [E68] |
| GCC governance and security are handled after the fact | Documented (B) | Governance is "dealt with after the fact"; barriers include "unclear governance, immature security controls" [E68, E129] |
| GCC overall attrition is about 16% | Conflicting | 16% (Zinnov) against 9% (EY) [E16, E69] |
| GCC AI and Cloud attrition is 18-25% | Documented (B) | [E16] |
| GPUs and credits are held at the parent company | Unverified (D) | Only "insufficient compute planning" appears as a barrier [E129] |
| GCC probation is a formal 3-6 month cycle | Plausible, thin (C) | Typical six months, no central cap [E118]; GitLab lists India among probation locations [E82] |
| Startups lack formal rubrics | Unverified (D) | A posting stresses founder proximity and shaping the function [E28] |
| Startup compute is credit-limited | Partly documented | Programs exist with conditions [E137, E138, E139, E140]; effect on hires unverified |
| Enterprise approvals dominate the timeline | Plausible (B) | Adobe's intake and "avoid overloading reviewers" [E104]; IBM's access-control findings [E47] |

### D8. Tool catalog: onboarding hubs, documentation, dashboards, postmortem repositories

| Tool or repository | Category | What the source says | How a new GenAI engineer can use it | Grade |
|---|---|---|---|---|
| Linear | Issue tracking | Triage Intelligence "automates the time consuming assessment and routing steps required when triaging issues" and suggests teams, projects, assignees, labels and duplicates, on Business and Enterprise plans [E83]. Linear Agent "can now write code using Claude Code and Codex" in cloud sessions that return a diff, needing GitHub access and AI credits [E84]. | Track failure inventory and golden-set tasks as issues; route AI-quality bugs with triage. Check plan tier and AI-credit cost first. | A (vendor docs) |
| Jira and Rovo (Atlassian) | Issue tracking, agents | Rovo agents are "configurable AI teammates", invoked in Jira and Confluence with /Rovo or /ai; they access data "depending on their knowledge sources" and act outside chat "with your confirmation" [E85]. DX is being integrated into Atlassian's "System of Work" [E123]. | Expect Jira data to feed engineering dashboards. Check which spaces and sources an agent can read before using it on sensitive material. | A (vendor docs) |
| Notion | Wiki, onboarding | A Custom Agent template, "Onboarding Guide", is a "24/7 digital 'buddy'" that answers from the company handbook and wiki [E86]. A third-party "30-60-90 New Hires Portal" template lists no contents [E87]. | Host your Expectations Contract, Access Register and decision log; beware doc rot [E95]. | A- and C |
| Slite | Knowledge base | The "lose 20% of work time" line comes from Slite's own survey: "close to a fifth of their time ... looking for information" [E88]. | Use as a knowledge base; treat the statistic as marketing. | C |
| Backstage (Spotify) | Internal developer portal | Spotify's onboarding metric is time to merge the 10th PR, cut from about 60 to under 20 days [E7]. | If your organization has a portal, find the golden paths and the service catalog in week 1. | A (vendor-promotional) |
| DX | Developer-productivity analytics | Time to first and 10th PR benchmarks; 90-day sentiment survey; individual data visible only to admins [E8]. Atlassian reportedly agreed to buy DX for about US$1 billion [E37] and announced completion in Nov 2025 [E123]. Marketing page has no definitions [E58]. | Ask what is measured on you and how it is used. | A (vendor) |
| Jellyfish | Engineering management and AI impact | Shows "spend and token usage by tool, team, or initiative"; vendor-agnostic across Copilot, Cursor, Claude Code and Amazon Q; derives signals from Git, planning and workflow data [E91]. Benchmark claims (700+ companies, 2x PR throughput) lack a stated method [E90]. | Use its spend view to defend or cut your own LLM spend; treat benchmarks as vendor claims. | A (docs), C (benchmarks) |
| GitKraken Insights | Engineering analytics | AI-impact metrics: Productivity Uplift, AI-Assisted Percentage, CapEx/OpEx split, Spend by Tier; includes per-developer and Power-User comparisons; does not define cost per PR [E89]. | Know that per-developer comparisons exist; agree outcome metrics. | A (vendor docs) |
| LiteLLM proxy | Cost control | Team budgets with `max_budget` and `budget_duration`; HTTP 422 on breach [E34]. | Per-project budgets and alerts (R4 move 4). | A |
| Claude Console workspaces | Cost control | Per-workspace spend and rate limits; no limits on the Default Workspace [E65]. | Separate environments and teams; cap monthly spend. | A |
| Langfuse | LLM observability | ClickHouse acquired Langfuse (16 Jan 2026); core features stay MIT-licensed; self-hosting unchanged [E56]. | Trace logging for the golden set. | A |
| promptfoo | LLM evals | Announced on 9 Mar 2026 that it "has agreed to be acquired by OpenAI" and will remain open source; closing not verified [E57]. | Regression evals in CI; watch vendor neutrality. | A |
| danluu/post-mortems | Postmortem repository | "A collection of postmortems", about 250 entries visible; mostly infrastructure failures, few AI-product entries [E67]. | Reading list for failure shapes. | A |
| Evidently AI ML and LLM system design database | Case-study repository | 800 case studies from 150+ companies; last updated 22 Dec 2025 [E54]. | Find prior art for your use case. | A |
| AI Incident Database and OECD AI incidents monitor | Incident repositories | Searchable incident text and metadata [E55]; the OECD entry on Deloitte's report is an example [E102]. | Build a failure-mode taxonomy for your risk register. | A-, B |
| Google SRE book, "Postmortem Culture" | Postmortem practice | Blameless postmortems; "define postmortem criteria before an incident occurs"; triggers include user-visible degradation and "Data loss of any kind" [E128]. | Template for your first AI-failure postmortem (week 8). | A |
| NIST AI 600-1 and OWASP LLM Top 10 | Risk frameworks | 12 GenAI risks including Confabulation, Data Privacy and Information Security [E92]; LLM02 sensitive information disclosure and LLM10 unbounded consumption [E93, E94]. | Structure the risk register in the compliance packet (week 10). | A |

### D9. Compliance and governance: details and discrepancies

- **SR 26-2.** Issued 17 Apr 2026 jointly by the Federal Reserve, OCC and FDIC; "supersedes and replaces SR letter 11-7" and SR 21-8; "most relevant to banking organizations with over $30 billion in total assets"; footnote 3: "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance" [E9, E10]. Baker Tilly: "The guidance does not address generative AI or advanced AI tools" and "separate guidance or rulemaking will address AI-related risks" [E43]. An Openlayer blog (28 Jul 2026) claims the opposite and is contradicted by the primary text [E11].
- **EU AI Act.** Regulation (EU) 2026/1744 was published in the Official Journal on 24 Jul 2026 and entered into force on 27 Jul 2026. It moves Annex III high-risk obligations to 2 Dec 2027 and Annex I to 2 Aug 2028, leaves GPAI obligations as planned, and mostly leaves transparency obligations from 2 Aug 2026 unchanged (with a four-month grace period for certain marking). Two new prohibitions apply from 2 Dec 2026 [E12, E13]. These are law-firm summaries; the Official Journal text was not opened.
- **DPDP date discrepancy.** Notification date 13 Nov 2025. Rule 4 (consent managers): 13 Nov 2026 [E14, E81]. Core duties: 13 May 2027 per two sources [E14, E81], 12 May 2027 per AZB & Partners, which also uses 12 Nov 2026 [E80]. India Briefing says sections 9 and 10 "are scheduled to come into effect on 13 March 2027" [E44], which no other source repeats, and a DPDP wiki page updated 9 Sep 2026 says "any further change would need a fresh notification" [E81]. A Removal of Difficulties Order (issued 5 Oct, gazetted 7 Oct 2026) amended section 9(1) and section 10(2)(c)(ii) and left timelines unchanged [E44]. In Nov 2025 the IT minister said the government was in talks to "significantly compress the compliance timelines", a proposal at that date [E45]. Working assumption: 13 May 2027; verify on the Gazette.
- **RBI FREE-AI.** Seven sutras, six pillars (Infrastructure, Policy, Capacity, Governance, Protection, Assurance) and 26 recommendations; binding status not stated in the source [E46].
- **NIST AI 600-1 (July 2024).** Twelve risks "unique to or exacerbated by" GenAI: CBRN information or capabilities; confabulation; dangerous, violent or hateful content; data privacy; environmental impacts; harmful bias or homogenization; human-AI configuration; information integrity; information security; intellectual property; obscene, degrading or abusive content; value chain and component integration. Confabulation is "The production of confidently stated but erroneous or false content" [E92].
- **IBM 2025 Cost of a Data Breach (Ponemon, 600 organizations).** Shadow AI "added an extra USD 670,000" to the average breach cost; "97% of breached organizations that experienced an AI-related security incident say they lacked proper AI access controls"; 63% had no AI governance policies; 13% reported an attack that affected AI models or applications [E47].
- **Adobe's intake.** A-F framework with six data points (audience, objective, input data type, input data classification, technology, output); a risk score from audience, input sensitivity and objective; lessons include early engagement of legal, security and privacy to define "green" scenarios that bypass triage, a tech radar of pre-approved technologies, one intake channel and a "minimum viable process". No review times are published [E104].
- **Legal and quality precedents.** Air Canada [E35]; Deloitte [E60, E102].

### D10. Cost levers: documented effects and gotchas

| Lever | Documented effect | Conditions and caveats | Source |
|---|---|---|---|
| Claude prompt caching | 5-minute cache write 1.25x base input price, 1-hour write 2x, cache read 0.1x (0.05x for Opus 5.5 and Sonnet 5.5; 0.025x for Fable 5.1 and Mythos 5.1); minimum cacheable prompt 512-4,096 tokens by model; 5-minute TTL refreshed on use; per the docs, cache hits are not deducted against your rate limit; no effect on output tokens | Needs a stable prefix; check live pricing | [E41 A] |
| OpenAI prompt caching | "50% discount" on cached input, automatic for prompts over 1,024 tokens (announced 1 Oct 2024) | Dated; current per-model discounts not verified | [E30 A, dated] |
| OpenAI Batch API | "50% cost discount compared to synchronous APIs"; completes within 24 hours; separate rate limits; up to 50,000 requests or 200 MB per batch | Offline jobs only | [E73 A] |
| Independent caching measurement | 41-80% API-cost reduction and 13-31% faster time to first token across providers on long-horizon agentic tasks | Preprint; naive full-context caching "can paradoxically increase latency"; put dynamic content at the end of the prompt | [E114 A] |
| Routing and cascades | FrugalGPT: match GPT-4 "with up to 98% cost reduction" (2023); RouteLLM: "over 2 times" without sacrificing response quality | Benchmark-specific; validate on your own evals | [E78 A, E79 A] |
| Practitioner claims | 70% cut from caching plus routing (author's own tool, no method; the first routing attempt "degraded quality for some queries"); 77% cut in input-token cost (page metadata only) | Not independently verified | [E105 C, E115 C] |
| Budget caps and attribution | Per-team budgets and per-workspace caps | Guardrail, not a saving by itself | [E34, E65] |

A "~40% token-spend cut" is therefore plausible on cache-friendly workloads (the lower bound of the independent range is 41%) but not a typical or guaranteed figure. Report a measured number from your own traffic, gated on your eval suite.

### D11. India probation and labor-law notes (not legal advice)

- No central law caps probation. An employer-of-record vendor says "The typical probation is 6 months for most roles", cites model standing orders at six months extendable by up to three (nine in total) and also states a "maximum 12 months total with extension" in its own terms, so its ceilings are inconsistent [E118 C]. It also says "No notice is required by law when dismissing during probation", which I could not verify elsewhere; read your contract.
- Four Labour Codes were notified to take effect from 21 Nov 2025. The Industrial Relations and Occupational Safety Codes are fully implemented, parts of the Wage and Social Security Codes await notification; certified standing orders now apply to establishments with 300 or more workers (previously 100); some states had exempted IT/ITES and it is unclear whether those exemptions continue; fixed-term employees receive benefits proportionate to tenure and pro-rata gratuity [E117 B].
- GitLab's handbook lists India among locations with probation periods and says common practice is to use the maximum allowable period per country [E82].
- Practical step: get the probation clause, review schedule and confirmation process from the offer letter in week 1, and ask when the first formal review will happen.

## Open Questions & Risks

### Status against the brief's completion criteria

| Criterion | Status | Where |
|---|---|---|
| Root causes of the expectations gap and early attrition documented with case examples | Met for project-level root causes and cases; only partly met for early attrition (anecdotes and vendor surveys of stated reasons, no AI-specific early-exit dataset) | F2-F4, F12, D2-D4 |
| A 30-60-90 framework with specific weekly deliverables | Met, as synthesis (Grade D) built on cited mechanics | R3 |
| Proven tactics for compute, API budget and data permissions | Mechanics documented (Grade A, vendor docs); "proven" tactics are not evidenced, so R4 is codified synthesis | F5, R4, D5, D10 |
| Probation rubrics from top engineering managers, startups vs GCCs | Not met as stated: none found. I documented what exists and proposed a scorecard | F8, F9, D6, D7, R5 |
| Strategies for managing upward on non-determinism | Met, grounded in Grade A non-determinism sources and Grade B/C expectation-setting sources | F6, R6 |

### Evidence gaps (searched, not found or not retrievable)

1. An AI-specific, early-tenure, realized-exit dataset (any source). Fifteen logged queries, plus Pave, SignalFire, Zinnov, EY, McKinsey and others (D1). Leads that may hold numbers but were gated or unretrievable: AIM Research's April 2026 India study of AI and data professionals [E144], the Upwork Research Institute report behind a syndicated release [E145] and the full Wisemonk India AI-engineer hiring report [E146].
2. GenAI-specific probation or 30/60/90 scorecards from named engineering managers, in startups or GCCs. Found job-posting deliverables and practitioner blogs only (D6).
3. GCC-specific probation or confirmation rubrics, and any documentation that GPUs or credits are held at a parent company (D7).
4. Verified first-person retrospectives by a first AI hire. Found one anonymous Blind post, one recruiter anecdote and one 2021 first-employee blog [E127, E121, E122].
5. Independent measurement of a typical token-spend saving across companies. Found one preprint range for caching (41-80%) and unsourced blog claims [E114, E105, E115].
6. A canonical definition or academic origin of "AI Expectations Gap" (D2).
7. Effect sizes for Bauer et al. 2007 and Zhao et al. 2007: only an abstract and a bibliographic record were retrieved [E20, E21].
8. The primary Jobvite 2018 and BambooHR 2015 reports: figures come via press coverage [E50, E19].
9. Not opened: the EU Official Journal text, the DPDP Gazette notification, Anthropic's batch and data-retention pages, McKinsey's 2026 State of AI and Stack Overflow's 2026 survey (relayed only through a recruiter blog [E121]).
10. How long a new hire waits for a first GPU allocation, dataset permission or API quota. No measurement found: only organization-level survey figures and vendor opinion [E142, E147, E148].

### Strongest objections an expert would raise, and what I found

| Objection | Evidence for | Evidence against or qualifying | Net |
|---|---|---|---|
| "No evidence that a 30-60-90 plan reduces early attrition for GenAI engineers." | None found. All plans here are Grade C or my synthesis. Only role clarity as a general mechanism has research support [E20]. | Job postings show 90-day deliverables in practice [E25, E26]; practitioners converge on eval-first, written-expectations plans [E95, E96]. | Valid. Treat R3 as a hypothesis to test with your manager, not a proven treatment. |
| "'AI Expectations Gap' is a rebranding of old requirements failure." | RAND's first root cause is a misunderstood problem [E1]; Ng's 2022 advice predates the term [E71]; the label appears in vendor material [E110]. | GenAI adds distinct mechanics: non-determinism, evaluation difficulty and variance [E23, E52, E53]. | Partly valid. The mechanism is old; the variance and evaluation mechanics are new. |
| "The famous failure statistics are unreliable, so you cannot infer anything." | RAND's ">80%" is second-hand [E1]; Gartner's are predictions [E2, E76, E3]; MIT's sample and denominators are inconsistent and critiqued [E130, E5]. | The root-cause lists and barriers recur independently across RAND, IBM, Gartner, Zinnov and others [E1, E75, E76, E129]. | Valid on magnitudes; qualitative pattern holds. I use them only qualitatively. |
| "Attrition is about compensation and a hot market, not expectations." | A better offer is the second-named reason for leaving a role early in the India AI-engineer vendor survey (21%) [E146 C]; a vendor blog cites a 35-50% outside-offer premium [E98 C]; AI/ML attrition runs higher than software engineering's [E97]. | Compensation ranks seventh for gen-AI heavy users [E134]; GCC high performers' drivers "none ... compensation" [E16]; in the India survey no growth (39%) leads and compensation is the least-named reason to stay (4%) [E146 C]. | Unresolved: stated and revealed reasons are non-comparable, and none of these is about new hires. |
| "GCCs are too heterogeneous to generalize." | 2,117 centres of very different size and mandate [E15]; the 16% vs 9% attrition conflict [E16, E69]. | Aggregate patterns are consistent across two surveys [E68, E129]. | Valid. Use D7 as hypotheses; confirm your own centre's mandate and approvals. |
| "Quick wins like a 40% token cut can backfire into quality regressions or cost-cutting theatre." | First routing attempt "degraded quality for some queries" [E105 C]; naive caching can increase latency [E114]; Klarna and CBA reversals [E24, E61]. | Independent measurements exist for caching (41-80%) and Batch is a flat 50% for offline work [E114, E73]. | Valid. Gate every saving on the eval suite and report measured, not promised, numbers. |
| "Eval-first is a luxury when leadership wants demos." | Demos are what leaders see; LinkedIn's early progress produced the pressure [E36]. | 20-50 tasks from real failures is "a great start" [E74]; teams without evals stay in reactive loops [E74]. | Qualified: a small eval set is cheap, and it is what makes the demo defensible. |
| "SR 26-2 excluding GenAI does not mean no model-risk review for LLMs." | Correct: banks still apply internal risk management, and separate AI guidance is expected [E43]. | None found. | Valid; R7 says "ask which internal policy applies". |
| "Telling a new hire to push back is politically risky in hierarchical GCC cultures." | Plausible; the sources show dual mandates and after-the-fact governance [E68]. | No evidence either way on outcomes. | Unresolved (Grade D). R4 and R8 use written, data-based, option-framed memos for this reason. |

### Risks of following this playbook

- **Over-documentation.** Artifacts can become the work. Keep each to one page and tie each to a decision.
- **Political cost of naming the gap.** Use neutral, data-based framing (R4 move 10); avoid quoting interview promises as accusations.
- **Local variance.** Probation terms, approval chains and cost levers differ by employer and cloud contract; verify each against your own documents.
- **Eval overfitting.** A golden set built from past failures can miss new failure modes; refresh it weekly from production traces [E74].
- **Vendor-claim dependence.** Several tool, cost and benchmark claims come from vendors (Grade A for what the docs say, C for performance claims).
- **Not legal advice.** The India probation and notice notes come from a law-firm update and an employer-of-record vendor; read your contract [E117, E118].

### Time-sensitive items to re-verify before acting

- Provider pricing and discounts (Claude caching multipliers, OpenAI caching and Batch terms): fetched 2026-10-22 from current docs, except OpenAI's caching announcement, which is from Oct 2024 [E41, E73, E30].
- Startup credit programs and conditions [E137, E138, E139, E140].
- DPDP dates (13 vs 12 May 2027; the 13 Mar 2027 outlier) [E44, E80, E81].
- EU Omnibus application dates, and any follow-up guidance [E12, E13].
- Whether OpenAI's acquisition of promptfoo has closed [E57]; plan tiers and AI-credit pricing for Linear and Atlassian features [E83, E84, E85].
- Any further federal AI-specific model-risk guidance after SR 26-2 [E43].

### What I would do with more budget

Interview 10-15 GenAI engineers and their managers in India GCCs and startups about probation outcomes; request internal rubrics under NDA; open the primary Jobvite, BambooHR and Pave reports; obtain AIM Research's gated India study and the question wording and response base behind the Wisemonk survey; retrieve Bauer and Zhao effect sizes; read the EU Official Journal text and the DPDP Gazette; and run the R2 diagnostic and R3 plan with a pilot cohort to see whether early-exit and probation outcomes differ.

## Delta

Belief change against the Prior and against other recalled starting points. "Direction" is confirmed, updated or contradicted.

| Belief (written before searching) | What the evidence showed | Direction |
|---|---|---|
| P1: the 35% figure has no primary source (75%) | Fifteen logged queries found none. Nearest numbers are 34% (intent, all workers), 33% and 31% (retrospective, general); the AI-specific sources give intent figures or the mix of stated reasons, not an early-exit rate (D1). Cannot prove non-existence; gated reports remain unread. | Confirmed (now about 85-90% that none is findable on the public web) |
| P2: famous failure statistics are project-level, soft, and organizational in cause (80%) | RAND's ">80%" is second-hand; Gartner's numbers are predictions; MIT's "95%" rests on 52 interviews, 153 survey responses and 300 public deployments, with its own limitations. Root causes are organizational and data-related. MIT itself names a "learning gap", not infrastructure or talent. | Confirmed and sharpened |
| P3: early attrition is role ambiguity and unmet expectations; AI-specific data is scarce (75%) | Role clarity and role-mismatch evidence hold (abstract and survey level); AI-specific data is scarce, anecdotal or vendor-run; effect sizes were not retrieved. In the one India AI-engineer survey found, "broken promises" is third (19%) behind no growth (39%) and a better offer (21%), so mismatch matters but does not dominate there. Pay appears less central in stated reasons than I expected, though a better offer is still second. | Partly confirmed (one weak AI-specific survey puts growth first) |
| P4: managers judge on shipped, measured outputs; AI fluency is a review criterion; rubrics sparse (60%) | AI fluency in reviews confirmed at Shopify and Meta. The output-centric part rests on one posting set and Grade C practitioner sources. Public rubrics are sparse, as expected. | Partly confirmed (about 50% on the output-centric part) |
| P5: GCC constraints are approvals and HQ dependencies; probation 3-6 months; startups informal (55%) | Pilot-to-production stalls, dual mandates and governance after the fact are documented at aggregate level. HQ-held GPUs not found. Typical probation is about 6 months per a vendor, with no central cap. Startup claims unverified. | Weakly supported (about 40%) |
| Recalled: SR 11-7 remains the US bank model-risk baseline | SR 26-2 (17 Apr 2026) supersedes it and excludes generative and agentic AI | Contradicted |
| Recalled: EU Omnibus delay proposed, adoption unknown | Adopted as Reg. 2026/1744, in force 27 Jul 2026; Annex III to 2 Dec 2027, Annex I to 2 Aug 2028 | Updated |
| Recalled: DPDP core duties about May 2027 | 13 May 2027 per two sources, 12 May per another; one outlier says 13 Mar 2027 for ss. 9-10 | Confirmed, with a date conflict |
| Recalled: GCCs about 1,700 with about 1.9M staff; IndiaAI about 34k GPUs | 2,117 GCCs (3,728 units, 2.36M talent, Mar 2026 data); IndiaAI 38,000+ GPUs at about Rs 65 per hour | Updated |
| Recalled: Atlassian acquired DX; Langfuse and promptfoo changed hands | DX: about US$1B reported, completion announced Nov 2025. Langfuse acquired by ClickHouse (16 Jan 2026). promptfoo: agreement to be acquired by OpenAI (9 Mar 2026), closing unverified | Confirmed (promptfoo partly) |
| Recalled: non-determinism numbers (80 unique of 1,000; 15% and 70%; pass^8 under 25%) | All confirmed in primary sources | Confirmed |
| Recalled: caching reads about 10% of price, Batch about 50% off, "40% plausible" | Confirmed (0.1x, and 0.05x or lower on the newest Claude models; 50% Batch). Independent caching range 41-80%. No evidence for a typical figure. | Confirmed, with caveat |
| Recalled: LinkedIn "80% fast, last 20% slow" | 80% in month one; the remaining stretch took four more months | Confirmed, with detail |
| Recalled: India probation 3-6 months | Typical 6 months (vendor); 3 months for junior operations roles; no central cap | Partly confirmed |
| Recalled: Gallup onboarding statistic (12% strongly agree) | The fetched Gallup page did not contain it | Not verified |

## Sources & Evidence Ledger

### Recalled, NOT verified (Grade D)

- Effect sizes in Bauer et al. (2007) and Zhao et al. (2007): not retrieved [E20, E21].
- Gallup's statistic on employees who strongly agree their organization onboards well: the fetched page did not contain it [E51].
- Microsoft's 2025 "AI is no longer optional" expectations and any related performance criteria: not fetched.
- Current per-model OpenAI cached-input discounts: only the Oct 2024 announcement was read [E30].
- Provider statements on determinism (seed parameters as best-effort; restrictions on temperature for reasoning models): recalled, not verified.
- Backstage's CNCF status: recalled, not verified.
- Any HQ control of GPU allocation in GCCs, and the specific interview-loop promise pattern in R2 row 14: my inference.
- The idea that "35%" derives from the 34% McKinsey figure: speculation.

### Searched, not found

See "Evidence gaps" above and the queries listed in D1.

### How to read the ledger

Each row gives the evidence ID, a description (publisher, date and what it is), the URL, the grade, how the page was opened, and where it is cited. Grades follow the key at the top. "FETCHED" means the page was opened with a fetch tool and the supporting passage was read; passages were requested verbatim for load-bearing numbers. Grades in the table are as assigned when the page was read; qualifiers such as "vendor" or "dated" are kept.

| ID | Source (publisher, date, what it is) | URL | Grade | Opened | Cited in |
|---|---|---|---|---|---|
| E1 | RAND RR-A2680-1, Ryseff/De Bruhl/Newberry, 13 Aug 2024 | https://www.rand.org/pubs/research_reports/RRA2680-1.html | A | FETCHED | F2, Rec, R1, R2, Alt, D2, OQ |
| E2 | Gartner press release 25 Jun 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | A | FETCHED | F2, D2, OQ |
| E3 | Reprint-style article 5 Aug 2024 (not labelled press release) | https://www.intelligentcio.com/me/2024/08/05/gartner-predicts-30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025/ | B | FETCHED | F2, D2, OQ |
| E4 | Fortune (S. Estrada) 18 Aug 2025 on MIT NANDA "GenAI Divide" | https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html | B | FETCHED | D2 |
| E5 | T. Wieberneit critique, 6 Nov 2025 | https://customerthink.com/the-great-genai-divide-debunking-the-myth-of-95-failure/ | C (opinion) | FETCHED | F2, D2, OQ |
| E6 | CIO Dive 14 Mar 2025 on S&P Global Market Intelligence | https://www.ciodive.com/news/ai-project-fail-data-spglobal/742590/ | B | FETCHED | F2, D2 |
| E7 | Spotify Backstage blog (undated) | https://backstage.spotify.com/discover/blog/how-we-measure-backstage-success-at-spotify/ | A (vendor-promotional) | FETCHED | F8, D6, D8 |
| E8 | DX product docs | https://docs.getdx.com/onboarding.md | A (vendor) | FETCHED | F8, F11, R3, R5, D6, D8 |
| E9 | Fed SR 26-2 "Revised Guidance on Model Risk Management", issued 17 Apr 2026 | https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm | A | FETCHED | F7, R7, D9 |
| E10 | SR 26-2 attachment | https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf | A | FETCHED | F7, R2, R7, D9 |
| E11 | Vendor blog 28 Jul 2026 | https://www.openlayer.com/blog/post/sr-26-2-mrm-guide-ai-teams | C | FETCHED | F7, D9 |
| E12 | Legal news | https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force | B | FETCHED | F7, R7, D9, OQ |
| E13 | Law-firm article 3 Aug 2026 | https://www.mondaq.com/eu-digital-omnibus-on-ai-enters-into-force/1825722 | B | FETCHED | F7, R7, D9, OQ |
| E14 | Law-firm article 14 Aug 2026 | https://www.mondaq.com/dpdp-act-and-rules-2025-the-2026-compliance-milestones-businesses-cant-afford-to-miss/1830402 | B | FETCHED | F7, R7, D9 |
| E15 | Zinnov-NASSCOM India GCC Landscape 2026 (page partly garbled) | https://zinnov.com/centers-of-excellence/zinnov-nasscom-india-gcc-landscape-2026-report/ | A- (landing page; text partly garbled) | FETCHED | F9, OQ |
| E16 | Zinnov blog 25 Jun 2026 citing its SIAH 2026 report | https://zinnov.com/global-talent/high-performer-attrition-gcc-india-2026-zinnov-blog/ | B | FETCHED | F1, F3, F9, Alt, D1, D4, D7, OQ |
| E17 | Storyboard18 24 Nov 2025 on EY India GCC Pulse Survey 2025 | https://www.storyboard18.com/amp/how-it-works/81-of-gccs-upskill-talent-in-genai-niche-hiring-at-63-cuts-attrition-to-9-ey-84664.htm | B | FETCHED | D1 |
| E18 | SignalFire State of Talent 2025 | https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025 | A | FETCHED | D1 |
| E19 | HR Dive 10 Sep 2015 on BambooHR survey | https://hrdive.com/news/many-employees-quit-early-due-to-poor-onboarding-survey-says/405359 | B | FETCHED | F1, D1, D4, OQ |
| E20 | Bauer et al. 2007, J Appl Psychol 92(3):707-721 | https://pubmed.ncbi.nlm.nih.gov/17484552/ | B (abstract only; effect sizes not retrieved) | ABSTRACT only (PubMed) | F3, Rec, R1, R2, R5, Alt, D4, OQ, Src |
| E21 | Zhao et al. 2007 record, Personnel Psychology | https://www.scienceopen.com/document/vid/fdc7a48f-17f3-46b7-b7fe-44c1831f8a10 | B- (bibliographic only) | BIBLIOGRAPHIC RECORD only | F3, D4, OQ, Src |
| E23 | Thinking Machines (Horace He et al.), 10 Sep 2025 | https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ | A | FETCHED | F6, R2, R6, OQ |
| E24 | Entrepreneur 9 May 2025 (citing Bloomberg) | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | B | FETCHED | F10, F12, R2, R7, Alt, D3, OQ |
| E25 | Onit "AI Engineer" posting, Pune on-site | https://jobs.lever.co/onit/983d3c5d-55d7-4802-9865-80bf58c68bd4 | A (posting) | FETCHED | F8, F10, R3, R5, D6, OQ |
| E26 | Onit "Senior AI Engineer" posting, Pune on-site | https://jobs.lever.co/onit/5110cadf-965f-4597-ae95-7d4c000675d7 | A (posting) | FETCHED | F8, D6, OQ |
| E27 | Listicle (15 Jun 2025, mod. 27 Dec 2025) | https://digitaldefynd.com/IQ/why-ai-engineers-get-fired/ | C | FETCHED | D1 |
| E28 | ML Engineer LLM Evals & Agent Systems, London hybrid, early-stage | https://www.deeprec.ai/jobs/ml-engineer-35119589 | A (posting; negative result) | FETCHED | F8, F9, D6, D7 |
| E29 | Google Rules of ML (Zinkevich), last updated 2025-08-25 | https://developers.google.com/machine-learning/guides/rules-of-ml/ | A | FETCHED | F4, R2, R4, R6, Alt |
| E30 | OpenAI announcement 1 Oct 2024 | https://openai.com/index/api-prompt-caching | A (dated) | FETCHED | D10, OQ, Src |
| E31 | AWS Startups prompt library page | https://startups.aws.com/prompt-library/gpu-instance-quota-assistant | A- | FETCHED | F5, R2, R4, Alt, D5 |
| E32 | Microsoft Learn: Azure OpenAI/Foundry quota | https://learn.microsoft.com/azure/foundry/openai/how-to/quota | A | FETCHED | F5, R2, R4, Alt, D5 |
| E33 | Linux Foundation/FinOps Foundation press 19 Feb 2026 | https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1 | A | FETCHED | F5, D5 |
| E34 | LiteLLM docs | https://docs.litellm.ai/docs/proxy/team_budgets.md | A | FETCHED | F5, R2, R3, R4, D5, D8, D10 |
| E35 | ABA Business Law Today 29 Feb 2024 | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ | B | FETCHED | F7, F12, R2, R7, D3, D9 |
| E36 | The New Stack 2 May 2024 (J. Jackson) on LinkedIn | https://thenewstack.io/5-lessons-from-linkedins-first-foray-into-genai-development/ | B | FETCHED | F6, F12, Rec, R1, R2, R6, Alt, D2, D3, OQ |
| E37 | BNN Bloomberg 18 Sep 2025 | https://www.bnnbloomberg.ca/business/2025/09/18/atlassian-to-acquire-developer-productivity-platform-dx-for-us1-billion | B | FETCHED | D8 |
| E38 | "Adding Error Bars to Evals", Evan Miller, 1 Nov 2024 | https://arxiv.org/abs/2411.00640v1 | A | FETCHED | F6, R1, R5, R6, D5 |
| E39 | Digital Commerce 360, 8 Apr 2025 | https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/ | B | FETCHED | F8, R2, R5, R7, D6 |
| E41 | Claude API docs: prompt caching | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | A | FETCHED | F10, R3, R4, R5, D10, OQ |
| E42 | Hamel Husain "Your AI Product Needs Evals", 29 Mar 2024 | https://hamel.dev/blog/posts/evals/ | A | FETCHED | F6, F10, R2, R3, R6, D5 |
| E43 | Baker Tilly 4 Jun 2026 | https://www.bakertilly.com/insights/updated-interagency-guidance-on-model-risk-management | B | FETCHED | F7, R7, D9, OQ |
| E44 | India Briefing | https://www.india-briefing.com/news/dpdp-removal-of-difficulties-order-2026-consent-data-audit-47274.html/ | B | FETCHED | F7, R7, D9, OQ |
| E45 | exchange4media 17 Nov 2025 | https://www.exchange4media.com/digital-news/govt-in-talks-with-industry-to-shorten-dpdp-act-compliance-deadlines-149420.html | B | FETCHED | D9 |
| E46 | KPMG India 26 Aug 2025 | https://kpmg.com/in/en/insights/2025/08/rbi-free-ai-committee-report-on-framework-for-responsible-and-ethical-enablement-of-artificial-intelligence.html | B | FETCHED | F7, R7, D9 |
| E47 | IBM 2025 Cost of a Data Breach (30 Jul 2025) | https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai | A | FETCHED | F7, R2, R3, R4, R7, D7, D9 |
| E48 | Business Standard 30 Jun 2026 | https://business-standard.com/technology/artificial-intelligence/india-ai-compute-race-subsidised-gpu-capability-gap-126062900734_1.html | B | FETCHED | F5, R4, D5 |
| E49 | Govt of India press release (page last updated 17 Apr 2026) | https://www.digitalindia.gov.in/press_release/indiaai-mission-expands-ai-ecosystem-with-affordable-compute-and-startup-support/ | A- | FETCHED | F5, R4, D5 |
| E50 | Psychology Today (L. Stybel) 3 Mar 2019 | https://www.psychologytoday.com/us/blog/platform-success/201903/why-33-percent-new-employees-quit-in-90-days | B | FETCHED | F1, F3, R2, D1, D4, OQ |
| E51 | Gallup | https://www.gallup.com/workplace/247172/problems-onboarding-program.aspx | A (negative) | FETCHED (statistic not found) | D1, Src |
| E52 | tau-bench (Yao, Shinn, Razavi, Narasimhan), 17 Jun 2024 | https://arxiv.org/pdf/2406.12045 | A | FETCHED | F6, R1, R5, R6, D5, OQ |
| E53 | Atil et al. "Non-Determinism of 'Deterministic' LLM Settings" (v5, 2 Apr 2025) | https://arxiv.org/abs/2408.04667 | A | FETCHED | F6, R2, OQ |
| E54 | Evidently AI database | https://evidentlyai.com/ml-system-design | A | FETCHED | D8 |
| E55 | AI Incident Database | https://incidentdatabase.ai/summaries | A- | FETCHED (no incident counts on page) | D8 |
| E56 | ClickHouse blog 16 Jan 2026 | https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability | A | FETCHED | D8 |
| E57 | promptfoo blog 9 Mar 2026 | https://promptfoo.dev/blog/promptfoo-joining-openai | A | FETCHED | D8, OQ |
| E58 | DX marketing page | https://getdx.com/onboarding/ | C | FETCHED | D8 |
| E59 | Pragmatic Engineer, "Onboarding to a New Company" (G. Orosz), 2 Nov 2021 | https://newsletter.pragmaticengineer.com/i/43450198/good-onboarding-processes | B | FETCHED | F8, R3, D6 |
| E60 | AP 7 Oct 2025 | https://www.news4jax.com/business/2025/10/07/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | B | FETCHED | F12, R2, D3, D9 |
| E61 | ACS Information Age 21 Aug 2025 | https://ia.acs.org.au/article/2025/cba-reverses-ai-driven-job-cuts--admits--error-.html | B | FETCHED | F10, F12, R2, R7, Alt, D3, OQ |
| E62 | Backbase Principal AI Evaluation Engineer, Hyderabad | https://job-boards.greenhouse.io/workatbackbase/jobs/7276393 | A (posting; negative) | FETCHED | F8, D6 |
| E63 | METR 10 Jul 2025 | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | A | FETCHED | F11, R5, Alt |
| E64 | METR 24 Feb 2026 | https://metr.org/blog/2026-02-24-uplift-update/ | A | FETCHED | F11, R5, Alt |
| E65 | Claude API docs: workspaces | https://platform.claude.com/docs/en/build-with-claude/workspaces | A | FETCHED | F5, R2, R3, R4, D5, D8, D10 |
| E66 | Claude API docs: rate limits | https://platform.claude.com/docs/en/api/rate-limits | A | FETCHED | F5, R2, R4, D5 |
| E67 | danluu/post-mortems | https://github.com/danluu/post-mortems | A | FETCHED | D8 |
| E68 | T2 Online 23 Sep 2026 on Dell-Zinnov "India GCCs 2030" | https://t2online.in/tech/tech-news/dell-zinnov-report--70--of-india-gccs-stuck-at-ai-pilots/2008202 | B | FETCHED | F2, F9, R3, D2, D7, OQ |
| E69 | EY India press release 23 Nov 2025 | https://www.ey.com/en_in/newsroom/2025/11/58-percent-gccs-in-india-investing-in-agentic-ai-two-third-creating-dedicated-innovation-teams-to-globalize-ideas-ey-gcc-pulse-survey-2025 | A- | FETCHED | F9, D1, D4, D7, OQ |
| E70 | Zinnov blog 8 Jul 2026 | https://zinnov.com/centers-of-excellence/what-no-one-tells-you-about-gccs-and-ai-blog/ | B | FETCHED | F2, R2, R3, D7 |
| E71 | Andrew Ng, The Batch, 18 May 2022 | https://charonhub.deeplearning.ai/how-to-build-ai-startups-part-3-set-customer-expectations/ | B | FETCHED | F4, R2, R4, R6, OQ |
| E72 | DORA 2025 report page | https://dora.dev/research/2025/dora-report/ | A | FETCHED | F11 |
| E73 | OpenAI API docs: Batch (undated) | https://developers.openai.com/api/docs/guides/batch | A | FETCHED | F10, R3, R4, R5, D5, D10, OQ |
| E74 | Anthropic Engineering "Demystifying evals for AI agents", 9 Jan 2026 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | A | FETCHED | F6, F10, Rec, R1, R2, R3, R5, R6, OQ |
| E75 | IBM IBV CEO Study, 6 May 2025 | https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles | A | FETCHED | F2, F4, D2, OQ |
| E76 | Gartner press release 26 Feb 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk | A | FETCHED | F2, F4, R2, R4, D2, OQ |
| E77 | Anthropic Engineering "Building effective agents", 19 Dec 2024 | https://www.anthropic.com/engineering/building-effective-agents | A | FETCHED | R4, R6, Alt |
| E78 | FrugalGPT (Chen, Zaharia, Zou), 9 May 2023 | https://arxiv.org/abs/2305.05176 | A (dated) | FETCHED | F10, D10 |
| E79 | RouteLLM (Ong et al.), ICLR 2025, arXiv v4 23 Feb 2025 | https://arxiv.org/abs/2406.18665 | A | FETCHED | F10, R3, R4, D10 |
| E80 | AZB & Partners, 14 Nov 2025 | https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/ | B | FETCHED | F7, R7, D9, OQ |
| E81 | DPDP Wiki (Mynd Solution), updated 9 Sep 2026 | https://dpdp.myndsolution.com/wiki/guides/key-dates-and-commencement/ | B- | FETCHED | F7, R7, D9, OQ |
| E82 | GitLab Handbook, probation page | https://handbook.gitlab.com/handbook/people-group/contracts-probation-periods/ | A | FETCHED | F8, R1, R3, D6, D7, D11 |
| E83 | Linear docs: Triage Intelligence | https://linear.app/docs/triage-intelligence | A (vendor) | FETCHED | D8, OQ |
| E84 | Linear changelog 11 Jun 2026 | https://linear.app/changelog/2026-06-11-coding-sessions | A (vendor) | FETCHED | D8, OQ |
| E85 | Atlassian Rovo docs: Agents | https://support.atlassian.com/rovo/docs/agents/ | A (vendor) | FETCHED | D8, OQ |
| E86 | Notion Custom Agent template "Onboarding Guide" | https://www.notion.com/custom-agent-templates/onboarding-guide | A- (vendor) | FETCHED | D8 |
| E87 | Notion marketplace template "Employee Onboarding - 30-60-90 New Hires Portal" (by Mona / ManagerHacks) | https://www.notion.com/templates/employee-onboarding-os | C | FETCHED | Alt, D8 |
| E88 | Slite article | https://slite.com/learn/internal-knowledge-base | C (vendor) | FETCHED | D8 |
| E89 | GitKraken Insights docs | https://help.gitkraken.com/gk-insights/ai-adoption-impact-cost-metrics/ | A (vendor) | FETCHED | F11, R2, D8 |
| E90 | Jellyfish press release 17 Mar 2026 | https://jellyfish.co/newsroom/jellyfish-reveals-ais-real-impact-on-engineering-teams/ | C (vendor telemetry) | FETCHED | F11, D8 |
| E91 | Jellyfish AI Impact product page | https://jellyfish.co/platform/jellyfish-ai-impact/ | A (vendor) | FETCHED | F11, R3, D8 |
| E92 | NIST AI 600-1 GenAI Profile, July 2024 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | A | FETCHED | F7, R3, R5, R7, D8, D9 |
| E93 | OWASP LLM10:2025 Unbounded Consumption | https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/ | A | FETCHED | F7, R2, R3, R4, R5, R7, D8 |
| E94 | OWASP LLM02:2025 Sensitive Information Disclosure (canonical URL; the legacy-looking slug .../llm02-insecure-output-handling/ served the same 2025 page when first fetched; re-fetched both 2026-10-23) | https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/ | A | FETCHED | F7, R2, R3, R4, R5, R7, D8 |
| E95 | Tian Pan blog, 14 May 2026 | https://tianpan.co/blog/2026-05-14-first-90-days-ai-engineer-onboarding-playbook | C | FETCHED | F8, R2, R3, R5, D1, D6, D8, OQ |
| E96 | techinterview.org, 5 May 2026 (updated 12 Jul 2026), no named author | https://www.techinterview.org/post/3233475078/expectations-contract-onboarding-engineers/ | C | FETCHED | F8, R3, R5, D6, OQ |
| E97 | Pave, 11 Feb 2025 | https://www.pave.com/blog-posts/ai-ml-talent-insights-4-key-takeaways-from-our-2025-report | B- (vendor payroll data; sample not stated) | FETCHED | F1, Alt, D1, D4, OQ |
| E98 | Intuz blog (P. Rupareliya), updated 20 Jul 2026 | https://www.intuz.com/blog/why-ai-engineers-quit-at-22-months/ | C | FETCHED | Alt, D1, D4, OQ |
| E99 | TechRepublic 30 Jul 2025 on Stack Overflow 2025 survey | https://www.techrepublic.com/article/news-developer-trust-in-ai-declines/ | B | FETCHED | F11 |
| E100 | Monica Rogati, HackerNoon, 12 Jun 2017 | https://hackernoon.com/lang/zh/the-ai-hierarchy-of-needs-18f111fcc007 | B (dated; concept origin) | FETCHED | F4, R2 |
| E101 | The Stack, 21 Jul 2025 | https://www.thestack.technology/vibe-coding-ceo-deletes-production-database/ | B | FETCHED | F12, D3 |
| E102 | OECD.AI incidents monitor entry, 5 Oct 2025 | https://oecd.ai/en/incidents/2025-10-05-be45 | B | FETCHED | F12, D3, D8, D9 |
| E103 | AWS Bedrock docs: data protection | https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html | A | FETCHED | R2, R4, R7 |
| E104 | IT Revolution (L. Brown), 26 Jun 2024 | https://itrevolution.com/articles/generative-ai-governance-at-scale-lessons-from-adobe/ | B | FETCHED | F7, R2, R3, R4, R5, R7, D7, D9 |
| E105 | DZone tutorial (D. Elumalai), Feb 2026 | https://dzone.com/articles/cut-ai-api-costs-by-70-without-sacrificing-quality | C | FETCHED | F10, Alt, D10, OQ |
| E106 | Shankar et al., "Operationalizing Machine Learning: An Interview Study", 16 Sep 2022 | https://arxiv.org/abs/2209.09125 | A | FETCHED | D5 |
| E107 | Shankar et al., "Who Validates the Validators?", 18 Apr 2024 | https://arxiv.org/abs/2404.12272 | A | FETCHED | F6, R3, D5 |
| E108 | Fortune, 30 Aug 2022 (Peak CEO Richard Potter) | https://www.fortune.com/2022/08/30/a-i-success-disconnect-executives-engineers-peak-richard-potter | C (opinion; no survey in the page) | FETCHED | F2, D1, D2 |
| E109 | SimScale "State of Engineering AI 2025" blog, 27 Jun 2025 | https://www.simscale.com/blog/the-engineering-ai-ambition-execution-gap-what-our-new-global-survey-reveals/ | C (vendor survey; engineering-simulation domain, not GenAI engineering) | FETCHED | F2, D1, D2 |
| E110 | MetaCTO (C. Fitkin), 9 Oct 2025 | https://www.metacto.com/blogs/managing-executive-expectations-for-ai-in-engineering | C (vendor, sells AI agency services) | FETCHED | F2, D1, D2, OQ |
| E111 | HR Grapevine (R. Dungan), 5 Feb 2026 | https://www.hrgrapevine.com/us/content/article/2026-02-05-meta-links-ai-adoption-usage-to-reviews-rewards | B | FETCHED | F8, F11, R2, R5, R7, Alt, D6 |
| E112 | Business Insider (J. Mann) via Yahoo Finance, 14 Nov 2025 | https://finance.yahoo.com/news/meta-start-grading-workers-ai-194500277.html | B | FETCHED | F8, R5, R7, D6 |
| E113 | OpenAI "Enterprise privacy at OpenAI", updated 8 Jan 2026 | https://openai.com/enterprise-privacy/ | A | FETCHED | R2, R4, R7 |
| E114 | Lumer et al., "Don't Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks", 9 Jan 2026 | https://arxiv.org/abs/2601.06007v1 | A (preprint) | FETCHED | F10, R3, R4, R5, Alt, D10, OQ |
| E115 | Deriv substack (O. Ghazal), modified 27 Jul 2026 | https://derivai.substack.com/p/prompt-caching-production-ai-agent-costs | C (metadata only; body NOT retrieved) | PAGE METADATA only (body not retrieved) | F10, D10, OQ |
| E117 | Trilegal, "Labour Codes Go Live", 22 Nov 2025 | https://www.ela.law/firms/trilegal/articles/trilegal-update-labour-codes-go-live | B | FETCHED | F9, R8, D11, OQ |
| E118 | Teamed (employer-of-record vendor), last reviewed 6 Oct 2026 | https://www.teamed.global/country-hiring-guides/india/probation-and-onboarding | C (vendor) | FETCHED | F9, R3, R5, R8, D6, D7, D11, OQ |
| E119 | NASSCOM community post (third-party blog), 5 Jan 2017 | https://community.nasscom.in/communities/talent/no-shows-are-killing-it-in-the-indian-job-market.html | C- (dated, unsourced) | FETCHED | D1 |
| E120 | PlugScale blog (V. Raju), 27 Mar 2026 | https://www.plugscale.com/gcc-attrition-india-2026 | C (unsourced vendor) | FETCHED | D1 |
| E121 | KORE1 recruiter blog (M. Carter), 21 Jun 2026, updated 21 Oct 2026 | https://www.kore1.com/hire-first-ai-engineer/ | C (vendor) | FETCHED | F3, F9, F12, R2, D1, D3, D6, OQ |
| E122 | Vocal.media (A. Romero), Jan 2021 | https://vocal.media/01/10-lessons-i-learned-as-the-first-employee-of-an-ai-startup | C (dated anecdote) | FETCHED | F12, D1, OQ |
| E123 | Atlassian press release (BusinessWire; release id suggests 10 Nov 2025; no date in fetched body) | https://www.businesswire.com/news/home/20251110683591/en/Atlassian-Completes-Acquisition-of-DX-Advancing-Engineering-Intelligence-for-Enterprises | A (vendor press) | FETCHED | F11, D8 |
| E124 | HR Executive (K. Smithberg), 3 Jun 2026 | https://hrexecutive.com/new-hire-satisfaction-plunges-when-jobs-dont-match-expectations/ | C (meta description only) | META DESCRIPTION only | D1 |
| E125 | Fortune (E. Burleigh), 19 Mar 2024, on McKinsey report | https://www.fortune.com/2024/03/19/ai-talent-planning-leave-quit-how-to-keep-work-culture/ | B | FETCHED | F1, D1, D4 |
| E126 | techtree.dev SF Bay Area ML/AI talent report (undated) | https://www.techtree.dev/reports/sf-bay-area-ml-ai-talent-report | C- | FETCHED | D1 |
| E127 | Blind post, 14 Jun 2024 (anonymous) | https://www.teamblind.com/post/failed-probation-hwhlhub4 | C (single anecdote) | FETCHED | F3, F12, D1, D3, OQ |
| E128 | Google SRE Book ch.15 "Postmortem Culture: Learning from Failure" (c) 2017 Google, O'Reilly | https://sre.google/sre-book/postmortem-culture/ | A | FETCHED | R2, R3, R5, R6, D8 |
| E129 | Zinnov-Dell "India GCCs 2030" whitepaper page, 28 Sep 2026 | https://zinnov.com/automation/zinnov-dell-india-gcc-2030-agentic-transformation-whitepaper/ | A- | FETCHED | F2, F4, F9, R3, R4, D2, D7, OQ |
| E130 | MIT NANDA "The GenAI Divide: State of AI in Business 2025" (Challapally, Pease, Raskar, Chari), cover date July 2025 -- copy hosted by law firm Webber Wentzel | https://webberwentzel.com/News/Documents/2025/MIT1757411281972.pdf | A- (original report, third-party copy) | FETCHED (third-party copy of the original PDF) | F2, D2, OQ |
| E131 | Tian Pan blog, 17 Apr 2026 | https://tianpan.co/blog/2026/04/17/ai-engineering-career-ladder-seniority | C | FETCHED | D6 |
| E132 | Recruiting from Scratch (no byline), 25 Jun 2026 | https://www.recruitingfromscratch.com/blog/how-to-hire-an-llm-ai-engineer-at-a-startup-2026 | C (vendor) | FETCHED | D6 |
| E133 | McKinsey Podcast "Gen AI talent: Your next flight risk", 2 May 2024 | https://www.mckinsey.com/capabilities/people-and-organization/our-insights/gen-ai-talent-your-next-flight-risk | B | FETCHED | D4 |
| E134 | McKinsey, "The human side of generative AI", 18 Mar 2024 | https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-human-side-of-generative-ai-creating-a-path-to-productivity | A | FETCHED | F1, F3, Alt, D1, D4, OQ |
| E135 | OmniDocBench (Ouyang et al.), arXiv v2 25 Mar 2025; CVPR 2025 paper | https://arxiv.org/html/2412.07626v2 | A | FETCHED | F4, R2, D5 |
| E136 | PureDocBench "How Far Is Document Parsing from Solved?" (arXiv, table dated 05/2026; no named authors on page) | https://arxiv.org/html/2605.07492v1 | A (preprint) | FETCHED | F4, R2, D5 |
| E137 | Google Cloud "AI startup program" page | https://cloud.google.com/startup/ai | A (vendor program page; verify live) | FETCHED | F5, F9, R3, R4, D5, D7, OQ |
| E138 | AWS Activate Credits page | https://aws.amazon.com/startups/credits/?lang=en-US | A (vendor program page; verify live) | FETCHED | F5, F9, R3, R4, D5, D7, OQ |
| E139 | AWS Startups announcement, byline 11 May 2026 | https://aws.amazon.com/aws-startups/learn/aws-activate-credits-now-accepted-for-third-party-models-on-amazon-bedrock/ | A (vendor) | FETCHED | F5, F9, R3, R4, D5, D7, OQ |
| E140 | Microsoft for Startups FAQ | https://learn.microsoft.com/en-us/startups/microsoft-for-startups/mfs-faqs | A (vendor; verify live) | FETCHED | F5, F9, R3, R4, D5, D7, OQ |
| E141 | DecisionMarketing (UK trade press) article on Lucent Search "AI and Data Leadership Survey 2025: The New Business Blueprint, AI From Hype to Execution", study dated 15 May 2025 | https://www.decisionmarketing.co.uk/?p=124036 | C (trade-press relay of a recruiter survey; sample and method not stated) | FETCHED | F1, D1, D4 |
| E142 | Techstrong.ai (M. Vizard), 22 Jan 2025, on a survey sponsored by cloud provider Civo | https://techstrong.ai/articles/survey-gpu-scarcity-delays-ai-initiatives | C (vendor-sponsored survey) | FETCHED | F5, D1, D5, OQ |
| E143 | Qlik press release via BusinessWire (URL dated 12 Mar 2025); survey by Wakefield Research | https://www.businesswire.com/news/home/20250312530068/en | C (vendor-sponsored survey; sample and field dates stated) | FETCHED | F4, D1, D5 |
| E144 | AIM Research "Attrition Study of AI and Data Professionals in India", page metadata 29 Apr 2026 (market report, gated) | https://aimresearch.co/reports/attrition-study-of-ai-and-data-professionals-in-india | B (primary page, summary only; full report gated) | FETCHED (summary only; full report gated) | D1, D4, OQ |
| E145 | Stacker-distributed Upwork release, 25 Aug 2025 (syndicated copy; Upwork's own page https://www.upwork.com/resources/great-ai-attrition-research failed to load, client_error) | https://abc17news.com/news/2025/08/25/the-great-ai-attrition-why-your-best-ai-talent-is-eyeing-the-exit/ | C (vendor release; no sample or method on page) | FETCHED (syndicated copy; Upwork page failed to load) | D1, D4, OQ |
| E146 | Wisemonk Team (India employer-of-record vendor), 8 Oct 2026 | https://www.wisemonk.io/blogs/why-indian-ai-engineers-leave-their-jobs | C (vendor's own survey; voluntary sample; base of percentages not stated) | FETCHED | F1, F3, Alt, D1, D4, OQ |
| E147 | nhimg.org article relaying StrongDM "25 Surprising Employee Onboarding Statistics in 2026" (13 Oct 2025) | https://nhimg.org/articles/employee-onboarding-statistics-expose-the-access-bottleneck-in-2026/ | C- (vendor statistics relayed by a third site; sample and method not stated) | FETCHED (relays another vendor's statistics) | D1, D5, OQ |
| E148 | HPCwire, M. Shaxted (CEO, Parallel Works), 23 Apr 2026 | https://www.hpcwire.com/2026/04/23/from-gpu-capacity-to-productivity-closing-the-operationalization-gap/ | C (vendor-authored opinion; no sample) | FETCHED | F5, D1, D5, OQ |
| E149 | AIM Research "Data & Analytics Attrition Study India 2023" page (undated; study labelled 2023) | https://aimresearch.co/?p=1573 | B (primary page, summary only) | FETCHED (summary only) | D1 |
| E150 | DataIQ, R. Bean, 10 Jan 2025: executive benchmark survey of 125 Fortune 1000 and global AI and data leaders | https://www.dataiq.global/articles/2025-ai-and-data-leadership/?rd=1 | B (opened; cited only as a non-match for E141) | FETCHED (non-match for E141) | D1 |
| E151 | Udemy Business "The New Engineering Mandate: Close the AI Performance Gap" (page metadata modified 2026-05-01; gated infographic) | https://business.udemy.com/resources/the-new-engineering-mandate-close-the-ai-performance-gap/ | C (vendor marketing page; statistics unsourced) | FETCHED (gated infographic page) | D1 |

