---
id: research.index
title: "Research Layer: Sessions, Findings, Decisions and Errata"
content_type: index
stage: 0
status: published
last_verified: 2026-11-19
summary: "Index of the evidence layer: 75 research sessions (22 Phase 0, 2 Phase 3, 51 RP2), the findings registry distilled from them, the decision registry, the Founding Architecture Document, errata and how to add research."
sources: [T0-01, T0-02, T0-03, T0-04, T0-05, T0-06, T0-07, T0-08, T0-09, T0-10, T0-11, T0-12, T0-13, T0-14, T0-15, T0-16, T0-17, T0-18, T0-19, T0-20, T0-21, T0-22, T0-23, T0-24, T0-25, T0-26, T0-27, T0-29, T0-30, T0-31, T0-32, T0-34, T0-35, T0-36, T0-37, T0-38, T0-39, T0-40, T0-41, T0-42, T0-43, T0-44, T0-45, T0-46, T0-47, T0-48, T0-49, T0-50, T0-51, T0-52, T0-53, T0-54, T0-55, T0-56, T0-57, T0-58, T0-59, T0-60, T0-61, T0-62, T0-63, T0-64, T0-65, T0-66, T0-67, T0-68, T0-69, T0-70, T0-71, T1-01, T1-02, T1-03, T2-01, T3-01, T3-02]
---

# Research Layer

This folder is the repository's **evidence layer**. Each session is a dated research report: its prior beliefs, its research question, evidence-graded findings, a source ledger and the belief changes it caused. The user-facing guidance in [career/](../career/README.md) is built from it.

**How to use it:**
1. **Start with the [findings registry](findings.md).** It lists all 1,034 key findings from 75 sessions, each with its grade and exact line, grouped by lifecycle stage.
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
| [DECISIONS.md](DECISIONS.md) | Architecture decision registry: D-001 to D-012 from Phase 0, plus later decisions appended (D-013 architecture v2; D-014 versioning; D-015 stack map; D-016 legacy-handbook policy and guide pattern; D-017 review-by dates; D-018 evidence conventions; D-019 one owner per fact; D-020 freshness tracking; D-021 research pipeline 2; D-022 generic scope; D-023 to D-026 RP2 integration architecture) | Append-only (status fields and calibration records are updated in place) |
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

### Research pipeline 2 sessions (51 of 53 saved, November 2026)

Outcome-first sessions from [research pipeline 2](pipeline-2/README.md) (D-021); T0-28 and T0-33 are deferred past 2026-12-05.

| Session | Focus |
|---|---|
| [T0-19](sessions/T0-19-linkedin-profile-search-content-engagement.md) | LinkedIn recruiter search, profile, content and engagement |
| [T0-20](sessions/T0-20-github-readme-portfolio-site-writing.md) | GitHub profiles, READMEs, portfolio sites and technical writing |
| [T0-21](sessions/T0-21-x-frontier-communities-fellowships-events.md) | X, frontier-lab communities, fellowships, events and competitions |
| [T0-22](sessions/T0-22-referrals-warm-intros-cold-outreach-law.md) | Referrals, warm introductions, cold outreach and outreach law |
| [T0-23](sessions/T0-23-resume-format-content-screening-2026.md) | GenAI résumé format, content, regional norms and AI screening (2026) |
| [T0-24](sessions/T0-24-job-boards-global-ai-startup-remote.md) | Global, AI-specific, startup, remote and employer job boards, ghost jobs and scams |
| [T0-25](sessions/T0-25-job-boards-regional-india-in-depth.md) | National and regional job boards, with India platforms in depth |
| [T0-26](sessions/T0-26-job-search-tools-agents-oss-mcp.md) | Job-search tools, trackers, auto-apply agents, open source and MCP servers |
| [T0-27](sessions/T0-27-target-employers-sponsor-registers-data.md) | Target employers, ATS board URLs, sponsor registers and hiring data corpora |
| [T0-29](sessions/T0-29-certifications-frontier-labs-ai-native-vendors.md) | Certification census 2: frontier labs and AI-native vendors |
| [T0-30](sessions/T0-30-certifications-courses-universities-india-programmes.md) | Certification census 3: course platforms, universities and India programmes |
| [T0-31](sessions/T0-31-certifications-data-enterprise-ai-platforms.md) | Certification census 4: data and enterprise AI platforms |
| [T0-32](sessions/T0-32-certifications-gpu-infrastructure-open-source.md) | Certification census 5: GPU, infrastructure, networking and open-source foundations |
| [T0-34](sessions/T0-34-certifications-governance-security-privacy-audit.md) | Certification census 7: AI governance, security, privacy and audit |
| [T0-35](sessions/T0-35-countries-cities-americas-europe-israel.md) | Countries and cities for GenAI careers 1: Americas, Europe and Israel |
| [T0-36](sessions/T0-36-countries-cities-gulf-india-asia-pacific.md) | Countries and cities for GenAI careers 2: Gulf, India and Asia-Pacific |
| [T0-37](sessions/T0-37-visa-dossier-united-states.md) | Visa and work-permit dossier: United States |
| [T0-38](sessions/T0-38-visa-dossier-canada.md) | Visa and work-permit dossier: Canada |
| [T0-39](sessions/T0-39-visa-dossier-uk-ireland-western-europe.md) | Visa and work-permit dossier: UK, Ireland, Germany, Netherlands, France, Switzerland |
| [T0-40](sessions/T0-40-visa-dossier-nordics-southern-central-europe.md) | Visa and work-permit dossier: Nordics, Southern and Central Europe |
| [T0-41](sessions/T0-41-visa-dossier-gulf-israel.md) | Visa and work-permit dossier: Gulf states and Israel |
| [T0-42](sessions/T0-42-visa-dossier-asia-pacific.md) | Visa and work-permit dossier: Asia-Pacific |
| [T0-43](sessions/T0-43-remote-cross-border-work-eor-platforms.md) | Remote cross-border work: employers, pay localisation, EOR platforms and structures |
| [T0-44](sessions/T0-44-pay-us-uk-europe-singapore-gulf.md) | Pay refresh: US, Canada, UK, Europe, Israel, Singapore, Gulf, Japan and Australia |
| [T0-45](sessions/T0-45-pay-negotiation-india-city-employer.md) | Pay and negotiation in India: by city, employer type, role and level |
| [T0-46](sessions/T0-46-interview-loops-genai-employers-2026.md) | Interview loops for GenAI roles by employer and track (2026) |
| [T0-47](sessions/T0-47-ai-mediated-hiring-screening-interviews-fraud.md) | AI-mediated hiring: screening, AI interviewers, candidate AI policies and fraud checks |
| [T0-48](sessions/T0-48-role-dossier-ai-engineer.md) | Role dossier: AI Engineer |
| [T0-49](sessions/T0-49-role-dossier-ml-engineer.md) | Role dossier: Machine Learning Engineer |
| [T0-50](sessions/T0-50-role-dossier-research-engineer.md) | Role dossier: Research Engineer / Member of Technical Staff |
| [T0-51](sessions/T0-51-role-dossier-forward-deployed-engineer.md) | Role dossier: Forward Deployed Engineer |
| [T0-52](sessions/T0-52-role-dossier-applied-scientist.md) | Role dossier: Applied Scientist |
| [T0-53](sessions/T0-53-role-dossier-applied-ai-engineer.md) | Role dossier: Applied AI Engineer |
| [T0-54](sessions/T0-54-role-dossier-ai-infrastructure-engineer.md) | Role dossier: AI Infrastructure / GPU Platform Engineer |
| [T0-55](sessions/T0-55-role-dossier-research-scientist.md) | Role dossier: Research Scientist (AI/ML) |
| [T0-56](sessions/T0-56-role-dossier-inference-engineer.md) | Role dossier: Inference / LLM Serving Engineer |
| [T0-57](sessions/T0-57-role-dossier-agentic-ai-engineer.md) | Role dossier: Agentic AI Engineer |
| [T0-58](sessions/T0-58-role-dossier-ml-platform-engineer.md) | Role dossier: ML Platform / MLOps Engineer |
| [T0-59](sessions/T0-59-role-dossier-ai-product-manager.md) | Role dossier: AI Product Manager |
| [T0-60](sessions/T0-60-role-group-evaluation-security-safety.md) | Role group dossier: Evaluation, Security and Safety |
| [T0-61](sessions/T0-61-role-group-governance-risk-responsible-ai.md) | Role group dossier: Governance, Risk and Responsible AI |
| [T0-62](sessions/T0-62-role-group-solutions-enablement-product-engineering.md) | Role group dossier: Solutions, Enablement and AI Product Engineering |
| [T0-63](sessions/T0-63-role-dossier-gpu-kernel-engineer.md) | Role dossier: GPU Kernel / ML Compiler Engineer |
| [T0-64](sessions/T0-64-role-dossier-physical-ai-engineer.md) | Role dossier: Physical AI / Robotics AI Engineer |
| [T0-65](sessions/T0-65-role-group-ai-leadership.md) | Role group dossier: AI Engineering Managers, Heads of AI and Chief AI Officers |
| [T0-66](sessions/T0-66-role-group-independent-fractional-contract.md) | Role group dossier: Independent, Fractional and Contract AI Work |
| [T0-67](sessions/T0-67-transitions-devops-pm-it-services-students.md) | Transitions: DevOps/SRE, product managers, IT-services engineers and students |
| [T0-68](sessions/T0-68-learning-resources-rated.md) | Learning resources rated: documentation, courses, books, cohorts and bootcamps |
| [T0-69](sessions/T0-69-skill-tool-momentum-dated-series.md) | Skill and tool momentum: dated rising/falling series and emerging titles |
| [T0-70](sessions/T0-70-market-pulse-hiring-layoffs-funding.md) | Market pulse: hiring volume, layoffs, funding and employer mix |
| [T0-71](sessions/T0-71-onboarding-growth-ai-roles.md) | First 90 days and growth in AI roles: probation, promotion and sustainable pace |

---

## Adding research

New research is planned in [research pipeline 2](pipeline-2/README.md): 53 sessions, each with a brief, the outputs it feeds and the claims it must test, run in a deep-research tool from a prompt that `python3 -B scripts/research_pipeline.py --prompt <id>` assembles. Its [protocol](pipeline-2/PROTOCOL.md) carries the rules below into every prompt; check a report with `--appendix` before saving it, verify it ([VERIFY.md](pipeline-2/VERIFY.md)) and integrate it ([INTEGRATE.md](pipeline-2/INTEGRATE.md)). A session outside the pipeline follows the same steps:

1. Start from [templates/SESSION.template.md](templates/SESSION.template.md). Continue the numbering of the layer the research belongs to, skipping IDs the pipeline 2 catalogue has reserved: foundational landscape research T0-72 onward (T0-19 to T0-71 are reserved, as of 2026-11-08); structural blueprints T1-04, …; action-plan synthesis T2-02, …. (Layer 3 is the grand synthesis, the [FAD](FAD.md).) Add the session to [pipeline-2/catalogue.json](pipeline-2/catalogue.json) so the tracker lists it, and record the brief (the research question and its scope) at the top of the session.
2. Follow EGP-1.0: log priors before searching; grade every claim; give dates; keep a source ledger; state the belief changes.
3. Put the key findings under a `## Key Findings` heading, as `**F1. …**` lines or a table with an ID column, so that [scripts/build_findings.py](../scripts/build_findings.py) can register them, and add the session's lifecycle stages to `SESSION_STAGES` in that script (an unlisted session defaults to stage 0).
4. Add a row for it under "Sessions by theme" above, and update the hand-written session counts (this page, [README.md](../README.md), [AGENTS.md](../AGENTS.md)); the generated pages count sessions themselves.
5. Run `python3 -B scripts/build_all.py`, then update the affected career documents (their owners, per D-019) and [CHANGELOG.md](../CHANGELOG.md).
6. Measurements that data files cite (for example a new posting-term snapshot) go into the data file as a new dated snapshot ([data/posting_skill_shares.json](../data/posting_skill_shares.json)), not into a prose page.
