# GenAI Career Intelligence System

> Evidence-grounded career intelligence for Generative AI, ML Systems, and Applied AI Engineering professionals — from entry-level to apex frontier lab roles, across geographies.

---

## What This Is

A structured knowledge repository that treats AI career navigation as an intelligence problem. Every claim is sourced. Every tool recommendation carries a verification timestamp. Every salary figure traces to primary data.

The repository covers the **full career lifecycle** — from understanding which roles actually exist and what they pay, through skill-building, job search, interviewing, compensation negotiation, and long-term growth planning. Content is organised around a 12-stage funnel, cross-referenced by role, compensation tier, and transition persona.

**Who it serves:** Any professional navigating a GenAI career — fresh graduates choosing their first role, mid-career engineers transitioning from adjacent fields, senior engineers evaluating frontier lab equity, India-based professionals maximising international compensation, and independent practitioners building consulting practices.

Read the full project vision, scope, and constraints in [CHARTER.md](CHARTER.md).

---

## Project Status

The project has completed **Phase 0: Foundational Research**. All 22 research sessions and 1 capstone synthesis (FAD) are done, all 12 architectural decisions are locked, and the Founding Architecture Document is sealed.

```
Phase 0 — Research Pipeline                                        COMPLETE
═══════════════════════════════════════════════════════════════
Layer 0 │ Foundational Landscape     │ ████████████████████ 18/18  ✓
Layer 1 │ Structural Blueprints      │ ████████████████████  3/3   ✓
Layer 2 │ Action Plan Synthesis      │ ████████████████████  1/1   ✓
Layer 3 │ Grand Synthesis (FAD.md)   │ ████████████████████  1/1   ✓
═══════════════════════════════════════════════════════════════
Total: 22 sessions + 1 synthesis = 23 pipeline outputs · 12/12 decisions locked
```

**Next:** Phase 1 (user-facing content generation in `career/`) begins with Sprint 0 infrastructure setup. See [FAD.md §18](research/FAD.md) for the full 16-week implementation roadmap.

---

## Completed Research

All 22 research sessions are in [`research/sessions/`](research/sessions/). The capstone synthesis is [`research/FAD.md`](research/FAD.md). Each session follows a standardised format with prior beliefs, evidence-graded findings, source ledgers, and belief-change deltas.

### Market, Roles & Compensation

| Session | Focus |
|---|---|
| [T0-01](research/sessions/T0-01-genai-role-taxonomy-market-volume.md) | Role taxonomy — which GenAI titles have verified hiring demand vs speculative hype |
| [T0-02](research/sessions/T0-02-global-regional-compensation-benchmarks.md) | Compensation distributions across US, UK, EU, India, Singapore, GCC |
| [T0-17](research/sessions/T0-17-compensation-progression-plateaus-equity.md) | Promotion velocity, equity dilution, hop-vs-stay calculus, India comp ceilings |

### Engineering Stack & Interviews

| Session | Focus |
|---|---|
| [T0-03](research/sessions/T0-03-skills-compute-infra-eval-stack.md) | Skills classification, serving engines, fleet telemetry, eval stack |
| [T0-14](research/sessions/T0-14-ai-system-design-interview-patterns.md) | AI system design interview archetypes, latency budgets, scoring rubrics |
| [T0-16](research/sessions/T0-16-agentic-protocol-stack-enterprise-demand.md) | Agentic protocol stack (MCP, A2A, AG-UI) and enterprise demand |

### Job Search, Tools & Portfolio

| Session | Focus |
|---|---|
| [T0-04](research/sessions/T0-04-ats-filtering-funnel-conversion-math.md) | ATS parsing mechanics, bot detection, funnel conversion math |
| [T0-05](research/sessions/T0-05-unconventional-hiring-tactics-oss-audits.md) | OSS contributions, micro-audits, cold outreach as hiring signals |
| [T0-10](research/sessions/T0-10-career-tooling-ecosystem-12-stage-funnel.md) | 64+ career tools audited across all 12 lifecycle stages |
| [T0-11](research/sessions/T0-11-certification-cloud-credential-roi.md) | Cloud certification ROI — which credentials have measurable hiring signal |
| [T0-12](research/sessions/T0-12-high-signal-communities-technical-visibility.md) | High-signal communities, open-source networks, conference strategies |
| [T0-13](research/sessions/T0-13-production-portfolio-proof-of-work-standards.md) | Production portfolio standards — what separates signal from noise |

### Transitions, International Rails & Legal

| Session | Focus |
|---|---|
| [T0-06](research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) | Transition roadmaps across 5 starting backgrounds |
| [T0-07](research/sessions/T0-07-india-remote-tax-statutory-compliance.md) | India remote tax structuring — Section 44ADA, GST LUT, FIRC, EOR models |
| [T0-08](research/sessions/T0-08-global-talent-visa-relocation-pathways.md) | Visa corridors — O-1A, EB-1A, UK Global Talent, EU Blue Card |
| [T0-09](research/sessions/T0-09-onboarding-probation-first-90-days.md) | First 90 days — AI expectations gap, probation rubrics, retention |
| [T0-15](research/sessions/T0-15-regulatory-ai-governance-career-families.md) | Regulatory AI careers — EU AI Act, NIST AI RMF, ISO 42001 |
| [T0-18](research/sessions/T0-18-freelance-fractional-ai-practice-economics.md) | Fractional AI practice — rate cards, contracts, client acquisition |

### Architecture, Methodology & Synthesis

| Session | Focus |
|---|---|
| [T1-01](research/sessions/T1-01-repository-information-architecture.md) | Repository information architecture, directory schema, navigation design |
| [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) | Evidence-grounding protocol (EGP-1.0) — grading rubric, TTL classes, citation standards |
| [T1-03](research/sessions/T1-03-interview-execution-offer-negotiation.md) | Interview execution playbook, negotiation scripts, equity due diligence |
| [T2-01](research/sessions/T2-01-tier-calibrated-execution-playbooks.md) | Tier-calibrated execution playbooks across 6 tiers × 5 personas |
| [FAD.md](research/FAD.md) | Founding Architecture Document — capstone synthesis, all decisions locked |

---

## Repository Structure

### Current Structure (Phase 0 — Research Complete)

```
genai-career-research/
├── README.md                  ← You are here
├── CHARTER.md                 # Project vision, scope, constraints, success criteria
├── LICENSE                    # CC-BY-SA-4.0
│
└── research/                  # Research pipeline (produces the evidence base)
    ├── RESEARCH-PIPELINE.md   # Pipeline DAG, session specifications, execution rules
    ├── DECISIONS.md           # Architecture Decision Registry (12/12 locked)
    ├── FAD.md                 # Founding Architecture Document (Phase 0 capstone)
    ├── sessions/              # 22 completed research sessions (~2.2 MB of evidence)
    └── templates/             # Session and decision templates
```

### Planned Structure (Phase 1 — Content Generation)

The following directories will be created during Phase 1, as specified in [FAD.md §15](research/FAD.md):

```
genai-career-research/
├── career/                    # User-facing content (generated in Phase 1)
│   ├── 01-landscape/          # Market awareness & exploration
│   ├── 02-roles/              # Verified role deep dives
│   ├── 03-skills-and-tech/    # Skill building & learning paths
│   ├── 04-certifications/     # Certification ROI
│   ├── 05-portfolio/          # Portfolio & proof-of-work
│   ├── 06-job-search/         # Discovery & application
│   ├── 07-networking/         # Communities & conferences
│   ├── 08-interviewing/       # Interview prep & execution
│   ├── 09-compensation/       # Negotiation & equity
│   ├── 10-onboarding/         # First 90 days & career growth
│   ├── 11-tracks/             # Cross-cutting deep dives (India remote, visas, transitions)
│   └── ecosystem/             # Universal tool catalog
│
├── indices/                   # Cross-cutting navigation matrices
├── .github/workflows/         # CI pipelines (lint, evidence validation, TTL audit)
└── docs/                      # MkDocs Material site configuration
```

### Stage Mapping: 12 Conceptual Stages → 10 Content Directories

| Conceptual Stages | Directory | Content Scope |
|---|---|---|
| 1–2: Awareness + Exploration | `01-landscape/` | Market overview, role volumes, geographic analysis |
| 2: Role Discovery | `02-roles/` | Role taxonomy, verified vs quarantined titles |
| 3: Skill Building | `03-skills-and-tech/` | Technical competency tiers, compute stacks |
| 4: Certification | `04-certifications/` | Credential ROI analysis |
| 5: Portfolio | `05-portfolio/` | Proof-of-work standards, anti-portfolio |
| 6–7: Discovery + Application | `06-job-search/` | ATS mechanics, unconventional tactics |
| 8: Networking | `07-networking/` | Communities, technical visibility |
| 9–10: Interview Prep + Execution | `08-interviewing/` | System design, behavioral, coding |
| 11: Negotiation | `09-compensation/` | 6-tier ladder, negotiation, equity |
| 12: First 90 Days | `10-onboarding/` | 30-60-90 frameworks, failure prevention |

Cross-cutting deep dives (`11-tracks/`) and the tool catalog (`ecosystem/`) span multiple stages.

---

## How to Navigate

| If you want to... | Go to... |
|---|---|
| Understand the project's goals and constraints | [CHARTER.md](CHARTER.md) |
| Read the capstone synthesis and Phase 1 roadmap | [research/FAD.md](research/FAD.md) |
| See the full research pipeline and session specifications | [research/RESEARCH-PIPELINE.md](research/RESEARCH-PIPELINE.md) |
| Review architectural decisions (all 12 locked with rationale) | [research/DECISIONS.md](research/DECISIONS.md) |
| See the decision summary table with chosen options | [research/FAD.md §11](research/FAD.md) |
| Read a specific research session | [research/sessions/](research/sessions/) |
| Understand the evidence-grading methodology | [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) |
| See the planned content structure | [T1-01](research/sessions/T1-01-repository-information-architecture.md) |

---

## Evidence Standard

All content follows the Evidence-Grounding Protocol (EGP-1.0):

- **Grade A:** Primary authoritative source (official documentation, government filings, peer-reviewed research)
- **Grade B:** Established secondary source with transparent methodology
- **Grade C:** Third-party analysis, vendor report, or single corroborating source
- **Grade D:** Recalled from memory, unverified, or single anecdote
- **Grade E:** No evidence found after searching
- **Grade M:** Model output (calculations, estimates) — inherits the weakest grade among inputs

Every factual claim in the repository either cites its source and grade, or is explicitly flagged as `[UNVERIFIED]`. Full protocol details in [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md).

---

## Research Methodology

The research pipeline uses the [Vivechak](research/RESEARCH-PIPELINE.md) research governance framework — a structured methodology for conducting evidence-grounded research through parallel, independent sessions with explicit dependency management. Vivechak enforces session templates, decision records, conflict resolution, and exit gates. The pipeline spec, session prompts, and execution DAG are documented in [`research/RESEARCH-PIPELINE.md`](research/RESEARCH-PIPELINE.md).

---

## License

This work is licensed under [CC-BY-SA-4.0](LICENSE). See the [CHARTER.md](CHARTER.md) disclaimer regarding tax, legal, and financial content.

---

*Temporal anchor: October 2026. Maintained under the Vivechak research governance framework.*
