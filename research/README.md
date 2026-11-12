---
id: research.index
title: "Research Layer: Sessions, Findings, Decisions and Errata"
content_type: index
stage: 0
status: published
last_verified: 2026-11-05
summary: "Index of the evidence layer: the 24 research sessions (22 Phase 0, 2 Phase 3), the findings registry distilled from them, the decision registry, the Founding Architecture Document, errata and how to add research."
sources: [T0-01, T0-02, T0-03, T0-04, T0-05, T0-06, T0-07, T0-08, T0-09, T0-10, T0-11, T0-12, T0-13, T0-14, T0-15, T0-16, T0-17, T0-18, T1-01, T1-02, T1-03, T2-01, T3-01, T3-02]
---

# Research Layer

This folder is the repository's **evidence layer**. Each session is a dated research report: its prior beliefs, its research question, evidence-graded findings, a source ledger and the belief changes it caused. The user-facing guidance in [career/](../career/README.md) is built from it.

**How to use it:**
1. **Start with the [findings registry](findings.md).** It lists all 262 key findings, each with its grade and exact line, grouped by lifecycle stage.
2. **Go to a session** for the full evidence: method, detailed findings, sources and open questions.
3. **Check [ERRATA.md](ERRATA.md)** before relying on a Phase 0 record. Known errors are listed there, with corrections.

**Rules:**
- Sessions are **snapshots**. Every figure is as of its session date (October 2026). Volatile facts carry expiry classes under EGP-1.0 ([T1-02](sessions/T1-02-evidence-grounding-protocol.md)).
- Sessions are **not edited**. Corrections go to [ERRATA.md](ERRATA.md), and new evidence goes into new sessions.

---

## Key documents

| Document | What it is | Status |
|---|---|---|
| [findings.md](findings.md) | Generated registry of every session's key findings, by stage and by session ([data](../data/findings.json); `python3 scripts/build_findings.py --update`) | Current |
| [ERRATA.md](ERRATA.md) | Known errors in the Phase 0 records, with the correct reading and evidence | Current |
| [DECISIONS.md](DECISIONS.md) | Architecture decision registry: D-001 to D-012 from Phase 0, plus later decisions appended (D-013 repository architecture v2; D-014 versioning; D-015 the stack map; D-016 the legacy-handbook policy and the guide pattern; D-017 review-by dates; D-018 evidence conventions for the stage guides; D-019 one owner per fact; D-020 generated review dates and a weekly reminder; D-021 research pipeline 2) | Append-only (status fields and calibration records are updated in place) |
| [FAD.md](FAD.md) | Founding Architecture Document: the Phase 0 capstone synthesis and Phase 1 plan | Historical record; superseded in parts (see its status note) |
| [RESEARCH-PIPELINE.md](RESEARCH-PIPELINE.md) | The Phase 0 pipeline specification: session DAG, briefs and execution rules | Historical record |
| [pipeline-2/](pipeline-2/README.md) | Research pipeline 2 (D-021): 53 planned sessions (T0-19 to T0-71) designed backwards from the data and pages they feed, with the shared protocol, the briefs, a generated tracker, and the verification and integration steps | Active |
| [templates/](templates/) | The Vivechak research-pipeline templates. In use: [SESSION](templates/SESSION.template.md) (every new session) and [DECISIONS](templates/DECISIONS.template.md) (the front-matter fields of D-013 onward). Kept for future phases: COMPARISON-SESSION and CONFLICT-RESOLUTION (optional session types), FOUNDING-ARCHITECTURE and PHASE-0-GATE (the Phase 0 synthesis and gate; patterns for a later synthesis) | Reusable |
| `.vivechak.json`, `.gitignore` | Vivechak tool files: the project marker the Vivechak MCP server reads, and its ignore rule for lock files | Tooling |

---

## Phase 0 pipeline (complete)

```text
Layer 0 │ Foundational landscape   │ 18 sessions (T0-01 … T0-18)
Layer 1 │ Structural blueprints    │  3 sessions (T1-01 … T1-03)
Layer 2 │ Action-plan synthesis    │  1 session  (T2-01)
Layer 3 │ Grand synthesis          │  FAD.md · 12 decisions locked
```

## Sessions by theme

### Market, roles and compensation

| Session | Focus |
|---|---|
| [T0-01](sessions/T0-01-genai-role-taxonomy-market-volume.md) | Role taxonomy: which GenAI titles have verified hiring demand, and which are speculative |
| [T0-02](sessions/T0-02-global-regional-compensation-benchmarks.md) | Compensation distributions across the US, UK, EU, India, Singapore and the Gulf |
| [T0-17](sessions/T0-17-compensation-progression-plateaus-equity.md) | Promotion velocity, equity dilution, hop-vs-stay calculus, India pay ceilings |
| [T0-15](sessions/T0-15-regulatory-ai-governance-career-families.md) | Regulatory AI careers: EU AI Act, NIST AI RMF, ISO/IEC 42001 |

### Engineering stack and interviews

| Session | Focus |
|---|---|
| [T0-03](sessions/T0-03-skills-compute-infra-eval-stack.md) | Skills classification, serving engines, fleet telemetry, evaluation stack |
| [T0-16](sessions/T0-16-agentic-protocol-stack-enterprise-demand.md) | Agentic protocol stack (MCP, A2A, AG-UI) and enterprise demand |
| [T0-14](sessions/T0-14-ai-system-design-interview-patterns.md) | AI system-design interview archetypes, latency budgets, scoring rubrics |
| [T1-03](sessions/T1-03-interview-execution-offer-negotiation.md) | Interview execution, behavioural calibration, negotiation, equity diligence |

### Job search, tools, portfolio and visibility

| Session | Focus |
|---|---|
| [T0-04](sessions/T0-04-ats-filtering-funnel-conversion-math.md) | ATS parsing, AI screening layers, funnel conversion maths |
| [T0-05](sessions/T0-05-unconventional-hiring-tactics-oss-audits.md) | Open-source contributions, micro-audits and outreach as hiring signals |
| [T0-10](sessions/T0-10-career-tooling-ecosystem-12-stage-funnel.md) | Career tools audited across the 12 lifecycle stages |
| [T0-11](sessions/T0-11-certification-cloud-credential-roi.md) | Certification and cloud-credential ROI |
| [T3-01](sessions/T3-01-genai-certification-stack-ranking-sequencing.md) | GenAI certification stack: value ranking, knowledge-overlap sequencing and dated execution calendars |
| [T3-02](sessions/T3-02-genai-certification-stack-ranking-sequencing.md) | GenAI certification stack (cross-check run): independent analysis with 9-module taxonomy, /35 composite scoring, directed overlap transfer tables |
| [T0-12](sessions/T0-12-high-signal-communities-technical-visibility.md) | High-signal communities, open-source networks, conference strategy |
| [T0-13](sessions/T0-13-production-portfolio-proof-of-work-standards.md) | Portfolio proof-of-work standards and the verifiability ladder |

### Transitions, international rails and legal

| Session | Focus |
|---|---|
| [T0-06](sessions/T0-06-career-transition-timelines-5-backgrounds.md) | Transition roadmaps from five starting backgrounds |
| [T0-07](sessions/T0-07-india-remote-tax-statutory-compliance.md) | India remote-work tax: §44ADA, GST LUT, FIRC, EOR models |
| [T0-08](sessions/T0-08-global-talent-visa-relocation-pathways.md) | Talent-visa corridors: O-1A, EB-1A, UK Global Talent, EU Blue Card |
| [T0-09](sessions/T0-09-onboarding-probation-first-90-days.md) | First 90 days: the AI expectations gap, probation rubrics, retention |
| [T0-18](sessions/T0-18-freelance-fractional-ai-practice-economics.md) | Fractional and freelance AI practice: rate cards, contracts, client acquisition |
| [T2-01](sessions/T2-01-tier-calibrated-execution-playbooks.md) | Tier-calibrated execution playbooks across 6 tiers and 5 personas |

### Repository architecture and method

| Session | Focus |
|---|---|
| [T1-01](sessions/T1-01-repository-information-architecture.md) | Information architecture, directory schema, navigation design |
| [T1-02](sessions/T1-02-evidence-grounding-protocol.md) | The evidence-grounding protocol (EGP-1.0): grades, expiry classes, citation rules |

---

## Adding research

New research is planned in [research pipeline 2](pipeline-2/README.md): 53 sessions, each with a brief, the outputs it feeds and the claims it must test, run in a deep-research tool from a prompt that `python3 -B scripts/research_pipeline.py --prompt <id>` assembles. Its [protocol](pipeline-2/PROTOCOL.md) carries the rules below into every prompt; check a report with `--appendix` before saving it, verify it ([VERIFY.md](pipeline-2/VERIFY.md)) and integrate it ([INTEGRATE.md](pipeline-2/INTEGRATE.md)). A session outside the pipeline follows the same steps:

1. Start from [templates/SESSION.template.md](templates/SESSION.template.md). Continue the numbering of the layer the research belongs to, skipping IDs the pipeline 2 catalogue has reserved: foundational landscape research T0-72 onward (T0-19 to T0-71 are reserved, as of 2026-11-08); structural blueprints T1-04, …; action-plan synthesis T2-02, …. (Layer 3 is the grand synthesis, the [FAD](FAD.md).) Add the session to [pipeline-2/catalogue.json](pipeline-2/catalogue.json) so the tracker lists it, and record the brief (the research question and its scope) at the top of the session.
2. Follow EGP-1.0: log priors before searching; grade every claim; give dates; keep a source ledger; state the belief changes.
3. Put the key findings under a `## Key Findings` heading, as `**F1. …**` lines or a table with an ID column, so that [scripts/build_findings.py](../scripts/build_findings.py) can register them, and add the session's lifecycle stages to `SESSION_STAGES` in that script (an unlisted session defaults to stage 0).
4. Add a row for it under "Sessions by theme" above, and update the hand-written session counts (this page, [README.md](../README.md), [AGENTS.md](../AGENTS.md)); the generated pages count sessions themselves.
5. Run `python3 -B scripts/build_all.py`, then update the affected career documents (their owners, per D-019) and [CHANGELOG.md](../CHANGELOG.md).
6. Measurements that data files cite (for example a new posting-term snapshot) go into the data file as a new dated snapshot ([data/posting_skill_shares.json](../data/posting_skill_shares.json)), not into a prose page.
