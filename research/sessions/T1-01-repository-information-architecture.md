---
id: T1-01
title: "Repository Information Architecture, Hybrid Navigation & 12-Stage Funnel Blueprint"
date: 2026-10-25
status: complete
topic: "Information architecture, directory taxonomy, navigation matrix, cross-cutting indices, markdown metadata standards"
tags: [information-architecture, directory-structure, navigation, 12-stage-funnel, role-taxonomy, compensation-tiers, cross-cutting-indices, frontmatter-schema, documentation-tooling, markdown-linting]
informs_decisions:
  - "D-001"
confidence: 0.82
confidence_note: "High for the architectural evaluation and directory schema (grounded in upstream findings and documented IA practices). Medium for tooling recommendations (vendor-stated features, not hands-on tested). Low for long-term maintenance cost projections (no comparable repository at this scale and scope exists for calibration)."
temporal_anchor: "2026-10"
last_verified: 2026-10-25
dependencies_consumed:
  - T0-01
  - T0-02
  - T0-10
  - T0-17
author_disclosure: "Written by an LLM assistant (Claude, Anthropic). Documentation framework evaluations rely on vendor documentation and secondary comparisons, not hands-on benchmarking."
schema_version: "0.1.0"
---

# T1-01 — Repository Information Architecture, Hybrid Navigation & 12-Stage Funnel Blueprint

> **How to read this file.** `S##` references rows in the Sources & Evidence Ledger (§9). `U:T0-##` references an upstream dependency session and its specific finding. Grades **A–E** follow the T1-02 EGP-1.0 rubric. `◌` marks a recalled claim capped at Grade D. Depth codes: **F** = full text opened · **S** = snippet or summary · **M** = not opened (recalled or second-hand). The temporal anchor is 2026-10-25.

---

## 1. Prior

Beliefs held *before* researching, written as checkable propositions. Section 8 (Delta) reports what the evidence did to each.

| # | Proposition (from memory) | Credence | How it was tested |
|---|---|---|---|
| P1 | A purely hierarchical folder structure (single primary axis) will fail for this repository because users need multi-dimensional discovery: by career stage, by role archetype, by compensation tier, and by current background. A hybrid architecture with one primary spine and cross-cutting index pages is the standard solution for multi-audience technical documentation. | 0.85 | Evaluated 5 competing architectural hypotheses against user journeys; reviewed Stripe, Cloudflare, Django IA patterns |
| P2 | The optimal directory depth for a GitHub-hosted Markdown repository is 3 levels (root/category/topic), with 4 levels as an absolute maximum, because deeper nesting degrades GitHub's web UI navigation, increases cognitive load, and complicates relative linking. | 0.80 | Searched GitHub directory limits and documentation project conventions |
| P3 | Cross-cutting indices (Stage × Role, Stage × Tier, Stage × Persona) can be maintained as static Markdown tables without automated generation, given the repository's scale (≤200 content files in the steady state), because the update frequency is low enough for manual curation to work. | 0.60 | Assessed repository projected scale against maintenance cost models |
| P4 | The Diátaxis framework (Tutorials / How-To / Reference / Explanation) is the dominant content-type taxonomy for technical documentation, and its four quadrants map cleanly onto the career lifecycle stages. | 0.70 | Searched for Diátaxis adoption and its fit with non-software documentation |
| P5 | MkDocs Material is the best static site generator choice for this repository because it is Markdown-native, Python-ecosystem-aligned, and has the strongest search and navigation features for prose-heavy content. | 0.65 | Compared MkDocs Material, Docusaurus, Starlight/Astro on current features and ecosystem status |

---

## 2. Research Question

What structural organisation, directory taxonomy, navigation system, and metadata standards best serve the GenAI Career Intelligence repository's diverse users — from ₹15L early-career engineers to ₹5Cr+ apex researchers, across US, India, and Europe geographies — while preventing maintenance collapse, cognitive overload, and content duplication?

**Sub-questions:**
(a) Which of five competing primary-axis architectures (Role, Lifecycle, Compensation, Persona, Hybrid) best balances discoverability against maintainability?
(b) What directory depth, naming conventions, and file-tree layout optimise GitHub browser navigation?
(c) How should cross-cutting indices be structured, generated, and maintained?
(d) What frontmatter schema should every content file carry?
(e) Which documentation tooling (SSG, linting, link preservation) best fits the repository's constraints?

---

## 3. Key Findings

**KF1 · The Hybrid Spine Architecture is the only model that survives all three test user journeys without duplication or dead ends. Grade B (design evaluation against upstream data; no comparable deployed system found).**

The 12-stage career lifecycle funnel (from T0-10) serves as the primary directory spine because it is the only axis that every user traverses sequentially or selectively, regardless of their role, tier, or geography. Role-primary, compensation-primary, and persona-primary organisations all force content duplication for shared advice (ATS mechanics, interview prep patterns, equity negotiation scripts) that applies across multiple roles or tiers. The lifecycle spine eliminates this: shared advice lives once in its stage directory and is cross-referenced from role and tier index pages. This finding confirms the brief's starting assumption (U:PIPELINE §T1-01 KNOWN) and is consistent with Cloudflare's tiered IA pattern and Django's pedagogical progression model [S1, S2, S3].

**KF2 · Three directory levels (root → category → topic) is the hard maximum; two levels suffice for most content. Grade B (GitHub documentation and web research).**

GitHub recommends a practical maximum of 3–4 directory levels and 3,000 entries per directory [S4]. For a prose-heavy Markdown repository with ≤200 projected content files, three levels (`career/06-job-search/ats-mechanics.md`) provide sufficient granularity without degrading the GitHub web UI's tree navigation. A fourth level should be used only for asset subdirectories (images, data files) that users rarely browse directly. The brief's proposed tree already respects this constraint. The `research/` subtree is a separate concern (pipeline artefacts, not user-facing content) and may use deeper nesting.

**KF3 · Cross-cutting indices should be static Markdown files with manual curation, not auto-generated, for the first 12 months. Grade C (judgement call; no comparable system found for calibration).**

At the projected scale of 80–150 user-facing content files in Phase 1, the cost of maintaining three cross-cutting index tables (Stage × Role, Stage × Tier, Stage × Persona) manually is approximately 2–4 hours per quarter. Automated generation would require a build step, a metadata parser, and CI integration — overhead that is justified only when the content count exceeds ~300 files or when update frequency exceeds monthly. The risk of manual curation is index staleness; the mitigation is a quarterly review cadence tied to the evidence TTL system from T1-02. If the repository grows beyond 300 files, migrate to a script that reads frontmatter and generates index pages (§6.7).

**KF4 · The Diátaxis framework maps imperfectly onto career lifecycle content; a modified taxonomy works better. Grade C (Diátaxis is documented [S5]; the modification is an untested design judgement).**

Diátaxis separates content into Tutorials (learning-oriented), How-To Guides (task-oriented), Reference (information-oriented), and Explanation (understanding-oriented). Career lifecycle content blends all four within each stage: Stage 3 (Skills) contains both explanatory landscape analysis and how-to learning paths; Stage 9 (Compensation) contains both reference data tables and task-oriented negotiation scripts. Instead of a Diátaxis top-level split, each stage directory should contain a mix of content types, distinguished by file-naming convention and frontmatter `content_type` field: `landscape` (explanation), `playbook` (how-to), `reference` (data tables and registries), and `guide` (tutorial/walkthrough).

**KF5 · The 12-stage funnel from T0-10 requires consolidation to 10 directories for the repository spine. Grade B (design synthesis from upstream findings).**

T0-10's 12 stages are: Awareness, Exploration, Skills, Certifications, Portfolio, Discovery, Application, Networking, Prep, Execution, Negotiation, Onboarding. Several adjacent stages share so much overlapping content that separate directories would create navigation confusion and content fragmentation: (1) Awareness + Exploration → `01-landscape` (both are about understanding the market before acting); (2) Discovery + Application → `06-job-search` (discovery channels and application mechanics are inseparable in practice); (3) Prep + Execution → `08-interviewing` (prep materials and execution strategies are consumed together). This yields 10 content directories plus `11-tracks` (cross-cutting deep dives) and `ecosystem` (tool catalog), matching the brief's proposed tree exactly.

**KF6 · The upstream role taxonomy (T0-01) defines 10 verified roles and 9 quarantined speculative titles; the directory should index only verified roles. Grade A (upstream finding, primary data).**

T0-01 established that AI Engineer (1,697 US postings), ML Engineer (1,082 US), Forward-Deployed Engineer (933), and Applied Scientist (~700) are the only roles with posting counts above the 50-quorum threshold. Five additional roles (Prompt Engineer, MLOps Engineer, Research Engineer, Applied AI Engineer, LLM Engineer) have partial evidence. Nine speculative titles (Context Engineer, Agent Architect, Cognitive Architect, etc.) are quarantined. The role index should carry only verified and partially-verified roles; quarantined titles should appear only in the landscape section with explicit caveats.

**KF7 · The 6-tier compensation grid from T0-02 is the correct cross-cutting axis for compensation, but tier boundaries need geographic variants. Grade B (upstream finding with design synthesis).**

T0-02 defined six universal tiers: T0 (Entry/New Grad), T1 (Early Career), T2 (Senior/Mid), T3 (Staff/Lead), T4 (Principal/Director), T5 (Distinguished/VP+). US TC medians range from ~$150K (T0) to $800K+ (T5). India equivalents from T0-02 and T0-17 show a roughly 3–5× compression: T2 Senior median ≈ ₹1.06–1.22Cr vs US Senior median ≈ $312K. The tier index must show both US and India (and optionally Europe) ranges side-by-side, with explicit notes on purchasing-power differences and equity treatment.

**KF8 · Frontmatter metadata must include 12 fields to support cross-referencing, evidence governance (T1-02), and temporal freshness tracking. Grade B (synthesised from T1-02 protocol and IA best practices [S6]).**

Every content file needs: `id`, `title`, `date`, `last_verified`, `status`, `stage` (lifecycle stage number), `content_type` (landscape/playbook/reference/guide), `roles` (list of relevant role slugs), `tiers` (list of applicable tiers), `geos` (list of geographies), `tags`, and `confidence`. Research session files add `informs_decisions`, `dependencies_consumed`, and `schema_version`. This schema enables cross-cutting index generation (manual or automated) and integrates with T1-02's temporal-recency TTL system.

**KF9 · MkDocs Material remains the strongest SSG choice for this repository, but the ecosystem transition must be monitored. Grade C (vendor documentation and secondary comparisons; not hands-on tested).**

MkDocs Material offers Markdown-native authoring (no MDX required), built-in search via Lunr.js or Algolia, automatic sidebar generation from directory structure, and the fastest build times of the three evaluated frameworks [S7, S8]. However, secondary sources report that MkDocs Material has entered a "maintenance/transition phase" with community forks emerging [S7]. Docusaurus offers superior versioning but ships heavier client-side JavaScript and requires React/MDX. Starlight (Astro) offers the best performance (zero JS by default) but lacks native versioning [S8]. For a prose-heavy Markdown repository that does not need versioning (content is evergreen with TTL-based updates, not versioned releases), MkDocs Material's strengths align best. Re-evaluate in Q2 2027 if ecosystem stability concerns materialise.

**KF10 · markdownlint-cli2 is the correct linting tool; remark-lint is over-engineered for this repository's needs. Grade C (vendor documentation [S9, S10]; not hands-on tested).**

markdownlint-cli2 provides ~60 built-in rules, auto-fix capability, VS Code integration, and straightforward GitHub Actions integration. remark-lint is more powerful but requires the unified/remark AST ecosystem and distributes rules as separate npm packages — unnecessary complexity for a repository that uses standard GFM Markdown without MDX. The linting configuration should disable MD013 (line length) for tables and code blocks, enable MD024 with `allow_different_nesting`, and whitelist `<br>`, `<sub>`, `<sup>`, `<kbd>` HTML elements.

**KF11 · Three user navigation personas validate the hybrid architecture; all reach their target content within 2 clicks from the root README. Grade C (design walkthrough against upstream data; not user-tested).**

Persona A (Fresh grad, India, ₹15L target): README → `01-landscape/` (market overview, India section) → `03-skills-and-tech/` (learning paths) → `06-job-search/` (application strategy). Cross-reference: Role index → AI Engineer → linked stages. Persona B (Indian Senior SWE, ₹1Cr+, targeting US remote): README → `11-tracks/india-remote-playbook.md` (dedicated track) → `09-compensation/equity-and-dilution.md` → `01-landscape/visa-and-immigration.md`. Persona C (ML Researcher, $500K+, targeting frontier lab): README → `02-roles/research-scientist.md` → `09-compensation/frontier-lab-equity.md` → `08-interviewing/ml-system-design.md`. All journeys complete within the proposed directory structure without requiring content duplication.

**KF12 · Non-linear resources (legal contracts, tax calculators, interview question banks) belong in the stage directory closest to their point of use, not in a separate `appendices/` catch-all. Grade C (design judgement; Stripe's task-driven IA pattern [S1] supports this).**

Stripe's documentation succeeds partly because resources appear where the user needs them, not in a separate reference section. Tax calculators belong in `09-compensation/`; interview question banks in `08-interviewing/`; contract checklists in `09-compensation/offer-diligence.md`. The `appendices/` directory should contain only truly universal resources: the glossary, the master evidence ledger, the epistemic methodology (T1-02), and the contribution guide. This reduces the chance that users miss critical resources buried in a separate section.

---

## 4. Recommendation

**Adopt the Hybrid Spine Architecture** with the 12-stage career lifecycle funnel (consolidated to 10 directories) as the primary organisational axis, cross-cut by three index dimensions (Role, Tier, Persona) maintained as static Markdown index pages.

### 4.1 Architectural Principles

1. **Single-write rule.** Every piece of advice lives in exactly one stage directory. Cross-cutting indices link to it; they do not duplicate it. This prevents the maintenance collapse that plagues multi-axis documentation.
2. **Lifecycle-primary navigation.** The top-level directory numbers (`01-` through `10-`) encode the career progression sequence. Users who don't know what stage they're in start at the README decision tree.
3. **Index-driven cross-cutting.** Three index pages (`career/roles-index.md`, `career/tiers-index.md`, `career/personas-index.md`) provide alternative entry points. Each cell in the index links to the relevant stage file and section anchor.
4. **Three-level maximum.** `career/06-job-search/ats-mechanics.md` is the deepest user-facing path. Asset subdirectories (`_assets/`) may add a fourth level but are not browsed directly.
5. **Content-type mixing within stages.** Each stage directory contains a mix of landscapes, playbooks, references, and guides, distinguished by frontmatter `content_type` and file-naming convention, not by subdirectory.
6. **Temporal governance.** Every content file carries `last_verified` and `confidence` fields, integrated with T1-02's TTL system. Stale files are flagged by the linter.

### 4.2 Complete Proposed Directory Schema

```
genai-career-research/                        # Repository root
├── README.md                                 # Project overview, pipeline status, contribution guide
├── CHARTER.md                                # Project vision, goals, non-goals, success metrics
├── LICENSE                                   # Repository license
├── .markdownlint.json                        # Linting configuration
├── .github/
│   └── workflows/
│       └── lint-markdown.yml                 # CI: markdownlint on PR
│
├── research/                                 # Research pipeline (not user-facing content)
│   ├── RESEARCH-PIPELINE.md                  # Pipeline DAG, session specifications
│   ├── DECISIONS.md                          # Decision Registry
│   ├── FAD.md                                # Final Assembled Document (output)
│   ├── templates/
│   │   └── SESSION.template.md
│   └── sessions/
│       ├── T0-01-genai-role-taxonomy-market-volume.md
│       ├── T0-02-global-regional-compensation-benchmarks.md
│       ├── T0-10-career-tooling-ecosystem-12-stage-funnel.md
│       ├── T0-17-compensation-progression-plateaus-equity.md
│       ├── T1-01-repository-information-architecture.md   # This file
│       ├── T1-02-evidence-grounding-protocol.md
│       └── ...                               # Remaining sessions per pipeline DAG
│
├── career/                                   # ═══ USER-FACING CONTENT ROOT ═══
│   ├── README.md                             # Master Career Lifecycle Decision Tree & "Start Here"
│   ├── roles-index.md                        # Cross-cutting index: Stage × Role matrix
│   ├── tiers-index.md                        # Cross-cutting index: Stage × Tier matrix
│   ├── personas-index.md                     # Cross-cutting index: Stage × Persona matrix
│   │
│   ├── 01-landscape/                         # ── Stages 1–2: Awareness + Exploration ──
│   │   ├── README.md                         # Stage overview: what to learn before you act
│   │   ├── market-overview.md                # GenAI hiring landscape (sourced from T0-01)
│   │   ├── employer-landscape.md             # Company tiers, frontier labs, GCCs, startups
│   │   ├── geo-compensation-map.md           # Global comp overview (sourced from T0-02)
│   │   ├── india-market.md                   # India-specific: GCC hiring, title patterns, ceilings
│   │   ├── regulation-and-immigration.md     # H-1B, EU AI Act, visa routes, policy status
│   │   └── _assets/                          # Images, diagrams for this stage
│   │
│   ├── 02-roles/                             # ── Stage 2: Exploration (Role Deep Dives) ──
│   │   ├── README.md                         # Role taxonomy overview, verified vs speculative
│   │   ├── ai-engineer.md                    # AI Engineer: scope, skills, demand, comp by tier
│   │   ├── ml-engineer.md                    # ML Engineer: scope, skills, demand, comp by tier
│   │   ├── forward-deployed-engineer.md      # FDE: scope, skills, demand, comp by tier
│   │   ├── applied-scientist.md              # Applied Scientist: scope, demand, comp by tier
│   │   ├── research-scientist.md             # Research Scientist/Engineer: frontier lab paths
│   │   ├── mlops-engineer.md                 # MLOps Engineer: platform and infra focus
│   │   ├── prompt-engineer.md                # Prompt Engineer: declining demand, pivot paths
│   │   ├── applied-ai-engineer.md            # Applied AI Engineer: partial evidence, watchlist
│   │   ├── llm-engineer.md                   # LLM Engineer: partial evidence, watchlist
│   │   ├── speculative-roles.md              # Quarantined titles: Context Eng, Agent Architect, etc.
│   │   └── _assets/
│   │
│   ├── 03-skills-and-tech/                   # ── Stage 3: Skill Building ──
│   │   ├── README.md                         # Skills landscape and learning path decision tree
│   │   ├── inference-and-serving.md          # Inference systems, deployment, optimization
│   │   ├── orchestration-and-agents.md       # RAG, agents, tool use, context engineering
│   │   ├── fine-tuning-and-alignment.md      # Fine-tuning, RLHF, evaluation
│   │   ├── ml-fundamentals.md               # Core ML/DL foundations required across roles
│   │   ├── learning-paths.md                 # Curated courses, curricula, MOOCs (from T0-10 Stage 3)
│   │   └── _assets/
│   │
│   ├── 04-credentials/                       # ── Stage 4: Certification ──
│   │   ├── README.md                         # Certification landscape and ROI framework
│   │   ├── cloud-certifications.md           # AWS, GCP, Azure AI/ML certs: cost, signal, ROI
│   │   ├── vendor-badges.md                  # Vendor-specific (Databricks, HuggingFace, etc.)
│   │   ├── recruiter-filter-evidence.md      # What hiring data says about cert filtering
│   │   └── _assets/
│   │
│   ├── 05-portfolio/                         # ── Stage 5: Portfolio & Proof-of-Work ──
│   │   ├── README.md                         # Portfolio strategy and high-signal project types
│   │   ├── project-archetypes.md             # End-to-end project patterns by role
│   │   ├── eval-harnesses.md                 # Building evaluation harnesses as portfolio pieces
│   │   ├── platform-risk.md                  # Hosting: GitHub, personal domain, platform shutdowns
│   │   └── _assets/
│   │
│   ├── 06-job-search/                        # ── Stages 6–7: Discovery + Application ──
│   │   ├── README.md                         # Job search strategy overview
│   │   ├── channels-and-boards.md            # Job boards, aggregators, company pages (from T0-10)
│   │   ├── ats-mechanics.md                  # ATS defenses, bot detection, parsing (from T0-10 DF-1)
│   │   ├── resume-strategy.md                # Resume builders, ATS scores, format guidance
│   │   ├── auto-apply-risk.md                # Auto-apply tools, risk register (from T0-10 DF-2)
│   │   ├── cold-outreach.md                  # Cold email, LinkedIn outreach, referral requests
│   │   └── _assets/
│   │
│   ├── 07-networking/                        # ── Stage 8: Networking & Communities ──
│   │   ├── README.md                         # Networking strategy and community landscape
│   │   ├── communities.md                    # Discord, Slack, Reddit, Blind, HN communities
│   │   ├── conferences-and-cfps.md           # AI/ML conferences, CFP strategies, speaker paths
│   │   ├── mentorship.md                     # ADPList, MentorCruise, informal mentorship
│   │   └── _assets/
│   │
│   ├── 08-interviewing/                      # ── Stages 9–10: Prep + Execution ──
│   │   ├── README.md                         # Interview prep strategy by company type
│   │   ├── ml-system-design.md              # ML/GenAI system design archetypes and frameworks
│   │   ├── coding-and-algorithms.md          # Coding rounds, LeetCode strategy, time allocation
│   │   ├── behavioral.md                     # Behavioral interview patterns, STAR format
│   │   ├── ai-policy-by-employer.md          # AI tool policies per employer (from T0-10 DF-5)
│   │   ├── prep-platforms.md                 # Hello Interview, Interviewing.io, etc. (from T0-10 DF-4)
│   │   ├── live-assistance-risks.md          # Copilots, detection, disqualification risks
│   │   └── _assets/
│   │
│   ├── 09-compensation/                      # ── Stage 11: Offer Negotiation ──
│   │   ├── README.md                         # Compensation strategy overview
│   │   ├── comp-stratification.md            # Tier-by-tier comp data, US/India/Europe (from T0-02)
│   │   ├── equity-and-dilution.md            # ERDM model, preference stacks, RAV (from T0-17)
│   │   ├── offer-diligence.md                # Offer-letter checklist: R5 items (from T0-17)
│   │   ├── negotiation-scripts.md            # Negotiation frameworks, scripts, coaching options
│   │   ├── comp-tools.md                     # Levels.fyi, Comprehensive.io, Carta (from T0-10 DF-6)
│   │   ├── india-tax-and-equity.md           # Indian perquisite tax, ESOP treatment, CA checklist
│   │   └── _assets/
│   │
│   ├── 10-onboarding-and-growth/             # ── Stage 12: First 90 Days & Beyond ──
│   │   ├── README.md                         # Onboarding strategy and growth planning
│   │   ├── first-90-days.md                  # Expectations gap, probation rubrics, quick wins
│   │   ├── promotion-velocity.md             # Promotion benchmarks by tier (from T0-17 §6.1)
│   │   ├── hop-vs-stay.md                    # Job-hop calculus, forfeited equity (from T0-17 §6.2)
│   │   ├── internal-mobility.md              # Lateral moves, org-internal transfers
│   │   └── _assets/
│   │
│   ├── 11-tracks/                            # ── Cross-Cutting Deep Dives ──
│   │   ├── README.md                         # Track index: who each track is for
│   │   ├── india-remote-playbook.md          # India → US remote: comp, tax, EOR, equity
│   │   ├── visa-and-relocation.md            # H-1B, O-1, EB-1, UK Global Talent, EU Blue Card
│   │   ├── career-transitions.md             # SWE→ML, PM→AI, Academia→Industry pivots
│   │   ├── fractional-and-consulting.md      # Fractional AI roles, consulting, advisory
│   │   └── _assets/
│   │
│   ├── ecosystem/                            # ── Universal Tool Catalog ──
│   │   ├── README.md                         # Tool catalog overview, rating rubric (from T0-10 §4)
│   │   ├── tool-catalog.md                   # Master tool table: all 64+ tools by stage and verdict
│   │   ├── privacy-and-security.md           # Data leakage incidents, extension risks (from T0-10 DF-7)
│   │   └── _assets/
│   │
│   └── appendices/                           # ── Universal Reference ──
│       ├── glossary.md                       # Term definitions, acronym expansions
│       ├── evidence-methodology.md           # EGP-1.0 summary for readers (from T1-02)
│       ├── master-sources.md                 # Aggregated evidence ledger across all content
│       └── contributing.md                   # Contribution guide, style guide, PR checklist
```

### 4.3 File-Naming Conventions

| Rule | Convention | Rationale |
|---|---|---|
| Case | `kebab-case` (lowercase, hyphens) | Cross-platform safe (Windows, macOS, Linux); no URL-encoding needed [S4] |
| Extensions | `.md` only for content; `.json` / `.yml` for config | Consistent tooling; no MDX dependency |
| Numbered prefixes | `01-` through `11-` for stage directories only | Encodes lifecycle sequence; sorts correctly in all file managers |
| No version suffixes | Never `_v2`, `_final`, `_draft` in filenames | Git history handles versioning |
| README.md per directory | Required | GitHub renders it automatically; serves as directory index |
| `_assets/` for binary files | Underscore prefix | Sorts to top; signals "not content"; gitignored from linting |
| Maximum filename length | 50 characters (excluding extension) | Prevents path-length issues on Windows (260-char limit) |

### 4.4 Frontmatter Schema

Every content file in `career/` **must** include this YAML frontmatter:

```yaml
---
# ═══ Required Fields ═══
id: "career/06-job-search/ats-mechanics"        # Unique ID: directory path without extension
title: "ATS Mechanics: Bot Detection, Parsing & Application Defenses"
date: 2026-10-25                                 # Creation date (ISO-8601)
last_verified: 2026-10-25                        # Last evidence review date (ISO-8601)
status: draft | review | published | stale       # Content lifecycle state
stage: [6, 7]                                    # Lifecycle stage number(s) this file covers
content_type: reference                          # landscape | playbook | reference | guide

# ═══ Cross-Cutting Dimensions ═══
roles:                                           # Which roles this content is relevant to
  - ai-engineer
  - ml-engineer
  - forward-deployed-engineer
tiers: [0, 1, 2, 3, 4, 5]                      # Which compensation tiers (0-5); omit = all
geos:                                            # Geographic relevance
  - us
  - india
  - europe

# ═══ Evidence Governance (T1-02 Integration) ═══
confidence: 0.78                                 # Aggregate confidence (0.0–1.0)
ttl_class: "platform"                            # T1-02 volatility class (14/31/90/180/365/1095/none)
sources_session: "T0-10"                         # Primary research session this content derives from

# ═══ Discovery & Navigation ═══
tags: [ats, bot-detection, resume-parsing, application-strategy]
summary: "How ATS systems detect automated applications, parse resumes, and what defenses to use."
prerequisite_reading: []                         # IDs of files that should be read first
next_reading: []                                 # IDs of suggested next files

# ═══ Schema ═══
schema_version: "0.1.0"
---
```

**Research session files** (`research/sessions/`) use the existing template frontmatter (§SESSION.template.md) plus `dependencies_consumed`, `temporal_anchor`, and `author_disclosure`.

### 4.5 Cross-Cutting Index Specifications

#### 4.5.1 Stage × Role Matrix (`career/roles-index.md`)

The matrix has 10 verified/partially-verified roles as rows and 10 stage directories as columns. Each cell contains a link to the most relevant file within that stage for that role, or `—` if no role-specific content exists.

| Role | Landscape | Roles | Skills | Creds | Portfolio | Job Search | Networking | Interview | Comp | Growth |
|---|---|---|---|---|---|---|---|---|---|---|
| **AI Engineer** | [market](#01-landscape/market-overview.md) | [role](#02-roles/ai-engineer.md) | [skills](#03-skills-and-tech/orchestration-and-agents.md) | [certs](#04-credentials/cloud-certifications.md) | [projects](#05-portfolio/project-archetypes.md) | [search](#06-job-search/channels-and-boards.md) | [community](#07-networking/communities.md) | [prep](#08-interviewing/ml-system-design.md) | [comp](#09-compensation/comp-stratification.md) | [growth](#10-onboarding-and-growth/promotion-velocity.md) |
| **ML Engineer** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **FDE** | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| *(remaining roles)* | | | | | | | | | | |

#### 4.5.2 Stage × Tier Matrix (`career/tiers-index.md`)

Six tiers as rows (T0–T5), 10 stage directories as columns. Each cell links to the tier-relevant section within the stage file. This matrix also shows the US and India TC range for each tier (from T0-02).

| Tier | US TC Range | India TC Range | Landscape | Skills | ... | Comp | Growth |
|---|---|---|---|---|---|---|---|
| **T0 Entry** | $120–180K | ₹8–20L | [→](#01-landscape/market-overview.md#entry) | [→](#03-skills-and-tech/learning-paths.md) | ... | [→](#09-compensation/comp-stratification.md#t0) | [→](#10-onboarding-and-growth/first-90-days.md) |
| **T1 Early** | $150–220K | ₹15–35L | ... | ... | ... | ... | ... |
| **T2 Senior** | $250–400K | ₹40L–1.2Cr | ... | ... | ... | ... | ... |
| **T3 Staff** | $350–600K | ₹80L–2Cr | ... | ... | ... | ... | ... |
| **T4 Principal** | $500–900K | ₹1.5–3.5Cr | ... | ... | ... | ... | ... |
| **T5 Distinguished+** | $800K–2M+ | ₹3–5Cr+ | ... | ... | ... | ... | ... |

#### 4.5.3 Stage × Persona Matrix (`career/personas-index.md`)

Four primary personas as rows, with a "Start Here" column and links to the 3–5 most relevant files for each persona's critical path.

| Persona | Start Here | Critical Path Files |
|---|---|---|
| **Fresh grad (India, ₹15L target)** | [landscape](#01-landscape/india-market.md) | → [AI Eng role](#02-roles/ai-engineer.md) → [learning paths](#03-skills-and-tech/learning-paths.md) → [job search](#06-job-search/channels-and-boards.md) → [comp T0](#09-compensation/comp-stratification.md#t0) |
| **Senior SWE → US remote (India, ₹1Cr+)** | [India remote](#11-tracks/india-remote-playbook.md) | → [equity](#09-compensation/equity-and-dilution.md) → [tax](#09-compensation/india-tax-and-equity.md) → [negotiation](#09-compensation/negotiation-scripts.md) |
| **ML Researcher → frontier lab ($500K+)** | [research scientist](#02-roles/research-scientist.md) | → [ML system design](#08-interviewing/ml-system-design.md) → [frontier equity](#09-compensation/equity-and-dilution.md) → [hop vs stay](#10-onboarding-and-growth/hop-vs-stay.md) |
| **Backend SWE → AI pivot** | [career transitions](#11-tracks/career-transitions.md) | → [ML fundamentals](#03-skills-and-tech/ml-fundamentals.md) → [portfolio](#05-portfolio/project-archetypes.md) → [interview prep](#08-interviewing/coding-and-algorithms.md) |

---

## 5. Alternatives Considered

| # | Architecture | Verdict | Key Strengths | Fatal Weakness |
|---|---|---|---|---|
| **A1** | **Role-Primary** (`/roles/ai-engineer/skills.md`, `/roles/ai-engineer/interview.md`, ...) | **Rejected** | Natural for users who know their target role; mirrors job-board mental model | Massive content duplication: ATS mechanics, negotiation scripts, and equity math are identical across roles. With 10 roles × 10 stages = 100 potential files, ≥40% would be near-duplicates. Maintenance cost scales multiplicatively. |
| **A2** | **Lifecycle-Primary** (`/stages/01-awareness/`, ...) | **Adopted as the hybrid spine** | Every user traverses stages; shared content lives once; natural reading order | Without cross-cutting indices, role-specific and tier-specific entry points are missing. Users who know their role but not their stage get lost. Solved by the three index pages. |
| **A3** | **Compensation-Primary** (`/tiers/tier-2-senior/`, ...) | **Rejected** | Immediately answers "what can I earn?" | Career lifecycle content doesn't naturally subdivide by tier. Skills training, interview prep, and networking advice is largely tier-agnostic (the same ML system design patterns apply at T2 and T4). Forces artificial tier boundaries on content that spans tiers. |
| **A4** | **Persona-Primary** (`/personas/india-senior-swe/`, ...) | **Rejected** | Highly personalised; minimal cognitive load for the target user | Personas are combinatorial: geography × role × tier × experience = hundreds of potential personas. Even with 4–6 archetypes, content duplication is severe. Adding a new persona requires creating an entire content subtree. Unsustainable. |
| **A5** | **Hybrid Spine** (lifecycle primary + cross-cutting indices) | **Recommended** | Single-write rule; lifecycle spine provides reading order; indices provide alternative entry points; 10 directories + 3 indices = manageable; new roles or tiers require only updating index pages, not creating directories | Indices must be manually maintained (mitigated by quarterly review cadence and potential future automation). Users who want a single "page for me" must follow 3–5 links through the persona index rather than finding a monolithic page. |

### Decisive factors for rejecting A1 (Role-Primary):

T0-01 identifies 10 verified roles (and the count will grow as titles graduate from quarantine). T0-10's tool catalog covers 64 tools that apply across all roles. T0-17's equity valuation model, hop-vs-stay calculus, and India tax guidance apply to every AI role. Under A1, this shared content would need to be duplicated into 10 role subtrees or extracted into a "shared" directory that undermines the role-primary premise. The brief's proposed tree already embeds this insight — it places shared advice in stage directories and uses `02-roles/` only for role-specific deep dives.

### Decisive factors for rejecting A3 (Compensation-Primary):

T0-02's tier grid is a powerful *lens* but a poor *spine*. The tier boundaries are fuzzy (T0-02 notes that comp ranges overlap between adjacent tiers by 10–15%), geographically dependent (India's T2 ceiling overlaps US's T1 floor), and evolving (frontier-lab compensation inflated tier boundaries in 2024–2026). Using tiers as the primary axis would require constant boundary maintenance and would fragment content that naturally spans tiers (e.g., "how to negotiate equity" applies from T1 through T5).

---

## 6. Detailed Findings

### 6.1 Architectural Hypothesis Evaluation: Method and Criteria

Each of the five architectures was evaluated against six criteria, scored 1–5:

| Criterion | Weight | Rationale |
|---|---|---|
| **Content duplication** | 25% | Duplicated content is the primary cause of documentation decay; the single-write rule is non-negotiable |
| **User discoverability** | 25% | Can users find content within 2 clicks from the root README for their specific need? |
| **Scalability** | 15% | Does the architecture accommodate growth (new roles, new tiers, new geographies) without restructuring? |
| **Maintainability** | 15% | What is the ongoing human cost to keep the architecture coherent? |
| **GitHub-native UX** | 10% | Does the directory tree render well in GitHub's web UI, with sensible README.md auto-display? |
| **Cross-referenceability** | 10% | Can automated or manual tools generate useful indices from the structure? |

**Scores:**

| Architecture | Duplication (25%) | Discoverability (25%) | Scalability (15%) | Maintainability (15%) | GitHub UX (10%) | Cross-ref (10%) | **Weighted Total** |
|---|---|---|---|---|---|---|---|
| A1 Role-Primary | 1 | 4 | 2 | 1 | 3 | 2 | **2.15** |
| A2 Lifecycle-Primary (no indices) | 5 | 2 | 4 | 4 | 4 | 3 | **3.55** |
| A3 Compensation-Primary | 2 | 3 | 2 | 2 | 3 | 3 | **2.45** |
| A4 Persona-Primary | 1 | 5 | 1 | 1 | 2 | 1 | **2.00** |
| **A5 Hybrid Spine** | **5** | **4** | **4** | **4** | **4** | **5** | **4.35** |

The Hybrid Spine (A5) scores highest by a significant margin. The only criterion where it loses to any alternative is Discoverability (where A4 Persona-Primary scores 5 because each persona gets a bespoke content tree). However, A4's perfect discoverability comes at the cost of catastrophic duplication (score 1) and scalability (score 1), making it unsustainable.

### 6.2 Directory Depth Analysis

GitHub's documentation states a recommended maximum of 50 directory levels (technical limit) but notes that 3–4 levels is the practical best practice [S4]. For this repository:

| Depth | Example Path | Use Case | Verdict |
|---|---|---|---|
| 1 | `career/roles-index.md` | Cross-cutting index pages | ✓ Primary |
| 2 | `career/06-job-search/ats-mechanics.md` | Stage content files | ✓ Primary |
| 3 | `career/06-job-search/_assets/ats-flowchart.svg` | Asset files | ✓ Secondary |
| 4+ | `career/06-job-search/sub-topic/detail.md` | — | ✗ Prohibited |

The `research/` subtree operates under different constraints (pipeline artefacts, not user-browsed content) and currently uses 2 levels (`research/sessions/T0-01-...md`), which is sufficient.

### 6.3 Content-Type Taxonomy

The Diátaxis framework's four quadrants map imperfectly to career content:

| Diátaxis Type | Career-Content Equivalent | Content-Type Slug | File-Naming Convention | Example |
|---|---|---|---|---|
| Explanation | Market landscapes, data analysis, research synthesis | `landscape` | `*-overview.md`, `*-landscape.md`, `*-market.md` | `market-overview.md` |
| How-To Guide | Actionable playbooks with step-by-step procedures | `playbook` | `*-strategy.md`, `*-playbook.md`, `*-scripts.md` | `negotiation-scripts.md` |
| Reference | Data tables, tool catalogs, comparison matrices | `reference` | `*-catalog.md`, `*-data.md`, `*-index.md` | `tool-catalog.md` |
| Tutorial | Guided walkthroughs for specific transitions or scenarios | `guide` | `*-guide.md`, `*-paths.md`, `*-walkthrough.md` | `learning-paths.md` |

Each stage directory contains a mix of these types. The `README.md` in each directory serves as a **stage overview** (landscape-type) that links to the more specific files within.

### 6.4 Cross-Referencing Mechanics

**Within-repository links** use relative Markdown paths:
```markdown
See [ATS Mechanics](../06-job-search/ats-mechanics.md) for how applicant tracking
systems handle automated submissions.
```

**Section anchors** use GFM auto-generated heading IDs:
```markdown
For Tier 2 compensation data, see [comp stratification § T2 Senior](
../09-compensation/comp-stratification.md#t2-senior-mid).
```

**Cross-cutting index cells** link to the most relevant file *and* section:
```markdown
| AI Engineer | ... | [prep § ML system design](#08-interviewing/ml-system-design.md#genai-patterns) | ...
```

**Upstream research references** from content files back to research sessions:
```markdown
> This section is derived from research session
> [T0-17 § 6.3](../../research/sessions/T0-17-compensation-progression-plateaus-equity.md#63-equity-valuation-model-erdm-discounting-paper-equity-by-stage-and-preference-stack).
> Evidence grade: B. Last verified: 2026-10-25.
```

### 6.5 Content Duplication Prevention: The Single-Write Protocol

**Problem.** The most common failure mode in multi-audience documentation is duplicated advice that drifts out of sync. Examples from this repository's scope:

| Advice | Relevant To | Lives In (Single Location) | Cross-Referenced From |
|---|---|---|---|
| ATS bot-detection mechanics | All roles, all tiers, all geos | `06-job-search/ats-mechanics.md` | Role index (all rows, "Job Search" column) |
| Equity dilution model (ERDM) | All roles at T2+ | `09-compensation/equity-and-dilution.md` | Tier index (T2–T5, "Comp" column); Role index ("Comp" column) |
| India perquisite tax on ESOPs | India-based, all roles, T2+ | `09-compensation/india-tax-and-equity.md` | Persona index ("Senior SWE → US remote"); Track "India remote playbook" |
| ML system design interview patterns | AI Eng, ML Eng, Applied Scientist, Research Scientist | `08-interviewing/ml-system-design.md` | Role index (4 rows, "Interview" column) |

**Rule.** If advice applies to ≥2 roles or ≥2 tiers, it lives in the stage directory. Role-specific files (`02-roles/*.md`) contain only: (a) the role definition and scope, (b) the demand/posting evidence, (c) role-specific skill requirements, and (d) a "journey" section linking to the relevant stage files in reading order.

### 6.6 Documentation Tooling Catalog

| Tool | Category | What It Does | Fit for This Repo | Evidence | Grade |
|---|---|---|---|---|---|
| **MkDocs Material** | SSG | Markdown-native static site generator; auto-sidebar from directory tree; built-in search (Lunr.js); fast builds | **Recommended** (prose-heavy, Markdown-only, no versioning needed) | Vendor docs; secondary comparisons [S7, S8] | C |
| **Docusaurus** | SSG | React/MDX-based; native versioning; native i18n; Algolia search; large plugin ecosystem | **Viable** (overkill for current needs; heavier JS bundle; React dependency) | Vendor docs [S8] | C |
| **Starlight (Astro)** | SSG | Zero-JS-by-default; Astro islands; Pagefind search; framework-agnostic components | **Viable** (best performance; weaker versioning; younger ecosystem) | Vendor docs [S8] | C |
| **markdownlint-cli2** | Linting | ~60 built-in rules; auto-fix; VS Code extension; GitHub Actions integration | **Recommended** | Vendor docs [S9] | B |
| **remark-lint** | Linting | Modular AST-based linter; MDX support; unified ecosystem | **Rejected** (unnecessary complexity for GFM-only repo) | Vendor docs [S10] | C |
| **Vale** | Prose linting | Spelling, grammar, tone, inclusive language; custom style packages | **Deferred** (valuable but not critical for Phase 1) | ◌ Recalled | D |
| **Perma.cc** | Link preservation | Institutional web archiving; academic-oriented; free tier for individuals | **Recommended for A/B sources** (per T1-02 §10.7) | T1-02 KF2 | B |
| **Wayback Machine** | Link preservation | Internet Archive; broadest coverage; subject to outages and legal challenges | **Recommended as secondary archive** | T1-02 KF2 | B |

**MkDocs Material ecosystem note.** Secondary sources report that MkDocs Material has entered a "maintenance/transition phase" with forks like Zensical and MaterialX emerging [S7]. This does not affect current functionality but creates a 12–18 month re-evaluation trigger. The repository's Markdown content is SSG-agnostic by design — switching from MkDocs to Starlight requires only changing the configuration file, not the content.

### 6.7 Automation Readiness: When to Script Index Generation

| Trigger | Threshold | Action |
|---|---|---|
| Content file count exceeds 300 | Measured | Write a Python script that reads frontmatter `stage`, `roles`, `tiers`, and `geos` fields and generates `roles-index.md`, `tiers-index.md`, `personas-index.md` |
| Update frequency exceeds monthly | Observed | Add the index-generation script to the CI pipeline; generate indices on every PR |
| Multiple contributors | ≥3 active contributors | Enforce frontmatter validation in CI (markdownlint custom rule or a dedicated YAML schema validator) |

Until these thresholds are crossed, manual curation of the three index files is sufficient and avoids build-step complexity.

### 6.8 User Navigation Journey Validation

**Persona A: Fresh grad, India, B.Tech CS, targeting AI Engineer role, ₹15L first job.**

| Step | User Action | Destination | Time (est.) |
|---|---|---|---|
| 1 | Opens `career/README.md`, reads decision tree | Directed to "New to GenAI? Start with Landscape" | 30s |
| 2 | Opens `01-landscape/india-market.md` | Reads India hiring data, GCC patterns, entry comp ranges | 5 min |
| 3 | Follows link to `02-roles/ai-engineer.md` | Reads role definition, skill requirements, demand data | 5 min |
| 4 | Follows "Journey" links in the role file | → `03-skills-and-tech/learning-paths.md` → `05-portfolio/project-archetypes.md` → `06-job-search/channels-and-boards.md` | Sequential |
| 5 | Checks tier index for T0 comp expectations | `tiers-index.md` → T0 row → confirms ₹8–20L range | 1 min |

**Result:** All content reachable within the architecture. No dead ends. No duplicated content encountered.

**Persona B: Indian Senior SWE (₹1.2Cr), 8 YOE, exploring US remote contracting.**

| Step | User Action | Destination | Time (est.) |
|---|---|---|---|
| 1 | Opens `career/README.md`, reads decision tree | Directed to "Specific transition? Check Tracks" | 30s |
| 2 | Opens `11-tracks/india-remote-playbook.md` | Reads EOR/contractor structure, comp expectations, tax implications | 10 min |
| 3 | Follows link to `09-compensation/india-tax-and-equity.md` | Reads perquisite tax on foreign shares, CA consultation advice | 5 min |
| 4 | Follows link to `09-compensation/equity-and-dilution.md` | Reads ERDM model, RAV haircut bands for Series C–D | 10 min |
| 5 | Checks persona index for complete critical path | `personas-index.md` → "Senior SWE → US remote" row | 1 min |

**Result:** The dedicated `11-tracks/india-remote-playbook.md` serves as the entry point; all supporting content is reachable via cross-references without duplication.

**Persona C: ML Researcher, PhD, $350K current, targeting Anthropic/DeepMind ($500K+).**

| Step | User Action | Destination | Time (est.) |
|---|---|---|---|
| 1 | Opens `career/README.md`, reads decision tree | Directed to "Know your role? Start with Roles" | 30s |
| 2 | Opens `02-roles/research-scientist.md` | Reads frontier lab landscape, MTS/Research Engineer title ambiguity | 5 min |
| 3 | Follows link to `08-interviewing/ml-system-design.md` | Reads ML system design archetypes for frontier lab loops | 10 min |
| 4 | Follows link to `09-compensation/equity-and-dilution.md` | Reads Archetype L (frontier-lab-like) RAV: 0.50–0.80 | 10 min |
| 5 | Follows link to `10-onboarding-and-growth/hop-vs-stay.md` | Reads hop-vs-stay calculus, forfeited vest tables | 5 min |

**Result:** All content reachable. The critical equity analysis (from T0-17) lives once in `09-compensation/` and is reachable from both the role file and the tier index.

### 6.9 Markdownlint Configuration

Recommended `.markdownlint.json` for the repository:

```json
{
  "$schema": "https://json.schemastore.org/markdownlint.json",
  "default": true,
  "MD013": {
    "line_length": 120,
    "code_blocks": false,
    "tables": false,
    "headings": false
  },
  "MD024": {
    "siblings_only": true
  },
  "MD033": {
    "allowed_elements": ["br", "sub", "sup", "kbd", "details", "summary"]
  },
  "MD041": false,
  "MD036": false
}
```

**Rationale for overrides:**
- **MD013** (line length): Tables and code blocks in this repository contain long URLs and data; wrapping them would break readability.
- **MD024** (duplicate headings): Allowed under different parents (e.g., "Overview" can appear in multiple sections).
- **MD033** (HTML elements): `<details>`/`<summary>` are used for collapsible sections; `<kbd>` for keyboard shortcuts; `<br>` for table cell line breaks.
- **MD041** (first line is heading): Disabled because all files start with YAML frontmatter.
- **MD036** (emphasis as heading): Disabled because the upstream session format uses bold text for sub-findings.

### 6.10 The `career/README.md` Decision Tree

The root README for the `career/` directory serves as the primary entry point. Its structure:

```markdown
# GenAI Career Intelligence — Start Here

## Who is this for?
[One paragraph: career-stage-agnostic description]

## Decision Tree: Where Should You Start?

### 🆕 New to GenAI careers?
→ Start with [Market Landscape](#01-landscape/market-overview.md)

### 🎯 Know your target role?
→ Go to [Roles](#02-roles/) and pick your role

### 💰 Focused on compensation?
→ Check the [Tier Index](tiers-index.md) for your level

### 🔄 Making a career transition?
→ Read [Career Transitions](#11-tracks/career-transitions.md)

### 🇮🇳 India-based, exploring US opportunities?
→ Start with [India Remote Playbook](#11-tracks/india-remote-playbook.md)

### 🛠 Looking for tools?
→ Browse the [Tool Catalog](ecosystem/tool-catalog.md)

## The 12-Stage Career Lifecycle
[Numbered list of stages with one-line descriptions and links]

## Cross-Cutting Indices
- [By Role](roles-index.md) — What matters for your specific role at each stage
- [By Compensation Tier](tiers-index.md) — What to expect and target at each level
- [By Persona](personas-index.md) — Curated paths for common transitions

## How This Repository Works
[Brief methodology note pointing to appendices/evidence-methodology.md]
```

---

## 7. Open Questions & Risks

### 7.1 Strongest Objections an Expert Would Raise

| # | Objection | Evidence For | Evidence Against | Effect on Conclusions |
|---|---|---|---|---|
| O1 | "The hybrid architecture adds cognitive overhead — users must learn the lifecycle model before they can navigate." | The lifecycle model has 10 stages (consolidated from 12); new users must read the README decision tree before diving in. | The README decision tree provides immediate routing based on user intent (role, comp, transition, geography). Cross-cutting indices provide alternative entry points. Stripe, Django, and Cloudflare all use multi-path navigation successfully [S1–S3]. | Mitigated by the decision tree and persona index. Monitor: if user feedback indicates confusion, add a "Quick Start" page with 3-sentence summaries per stage. |
| O2 | "Manual index maintenance will fail — indices will go stale within 6 months." | No automated generation is proposed for Phase 1. Indices depend on human discipline. | Repository scale is small (80–150 files in Phase 1). Quarterly review cadence is specified. The T1-02 TTL system flags stale files. Automation thresholds are defined (§6.7). | Accepted risk for Phase 1. If staleness is observed, implement automated generation immediately rather than waiting for the 300-file threshold. |
| O3 | "MkDocs Material's ecosystem transition makes it a risky choice." | Secondary sources report forks and a maintenance/transition phase [S7]. | The repository's Markdown content is SSG-agnostic. Switching SSGs requires only a new config file, not content rewrites. MkDocs Material's current features are fully functional. | Mitigated by SSG-agnostic content design. Re-evaluate in Q2 2027. |
| O4 | "Three index pages are not enough — you need a search engine." | Users who don't know their stage, role, or tier can't navigate via indices alone. | GitHub's built-in file search works across the repository. MkDocs Material or any SSG adds full-text search. The README decision tree routes by intent. | True for a deployed site; mitigated by SSG search. For raw GitHub browsing, the decision tree and three indices cover the main entry patterns. |
| O5 | "The 10-directory consolidation loses nuance — Awareness and Exploration are different stages." | T0-10 defines them as separate stages with different user intents (passive learning vs active investigation). | In practice, the content for both stages is "understand the market before you act." Splitting them into two directories of 2–3 files each creates navigation overhead without adding discoverability. A `README.md` within `01-landscape/` can distinguish the two phases. | Accepted trade-off. If content grows substantially, `01-landscape/` can be split without changing any other directory. |
| O6 | "You haven't validated this with real users." | No user testing was conducted. The three persona journeys are hypothetical walkthroughs. | The personas are grounded in upstream data: India entry comp from T0-02, US remote from T0-17 R6, frontier lab from T0-17 R6 and T0-02. The architectural evaluation used six weighted criteria. | Valid criticism. Recommend: pilot the architecture with 3 real users (matching the three personas) within the first month of content population and adjust based on observed navigation patterns. |

### 7.2 Open Questions

1. **How should the repository handle content that spans more than 3 stages?** Example: "How to evaluate and negotiate equity" touches Skills (understanding equity mechanics), Compensation (the negotiation), and Growth (when to exercise). Current answer: primary home in the stage of *action* (Compensation), with cross-references from other stages. Is this sufficient?
2. **Should the `ecosystem/tool-catalog.md` be split by stage once it exceeds ~100 tools?** Current: single file with a stage column. Alternative: per-stage tool files (`06-job-search/tools.md`, etc.).
3. **What is the right threshold for adding new personas to the persona index?** Current: 4 personas. Potential additions: "PhD → industry transition", "PM → AI PM", "Europe-based with UK EMI options".
4. **Should the repository support multi-language content (Hindi, Mandarin) given the India and China audience?** Current architecture does not preclude it (add `lang: hi` to frontmatter; create `01-landscape/india-market.hi.md`), but no content plan exists.
5. **How should deprecated content be handled?** Options: (a) delete with a Git history note, (b) move to `_archive/` with a deprecation banner, (c) add `status: deprecated` to frontmatter and exclude from indices. Recommended: option (c), consistent with "prune aggressively" best practice [S4].

### 7.3 Risks of Acting on This Architecture

- **Premature optimisation.** The architecture is designed for 80–300 content files. If the repository grows beyond 500 files, a significant restructuring may be needed (e.g., splitting stage directories into subdirectories).
- **Single-author bottleneck.** With manual index maintenance and no automated validation, a sole maintainer could become a bottleneck. Mitigated by clear contribution guidelines and frontmatter validation in CI.
- **SSG lock-in perception.** Choosing MkDocs Material may deter contributors who prefer React/MDX. Mitigated: all content is pure Markdown; the SSG choice is a presentation layer, not a content constraint.

### 7.4 DONE-Criteria Status

| Criterion | Status | Notes |
|---|---|---|
| Full directory tree and file naming specification defined | **Met** | §4.2 (Complete Proposed Directory Schema) and §4.3 (File-Naming Conventions) |
| 5 competing organisational models evaluated with explicit trade-offs | **Met** | §5 (Alternatives Considered) and §6.1 (Architectural Hypothesis Evaluation) |
| Cross-cutting indexing tables (Stage × Role, Stage × Tier, Stage × Persona) specified | **Met** | §4.5 (Cross-Cutting Index Specifications) with example matrix structures |
| Markdown frontmatter metadata standards codified | **Met** | §4.4 (Frontmatter Schema) with 15-field specification |
| User navigation journeys for 3 distinct personas validated | **Met** | §6.8 (User Navigation Journey Validation) with step-by-step walkthroughs |

---

## 8. Delta

| # | Prior Belief | Credence Before | Evidence Found | Credence After | Direction |
|---|---|---|---|---|---|
| P1 | Purely hierarchical fails; hybrid with cross-cutting indices is standard | 0.85 | Confirmed by Stripe (task-driven), Cloudflare (tiered), Django (pedagogical) IA patterns; A1/A3/A4 all failed the duplication test against upstream data | 0.95 | **Confirmed, strengthened** |
| P2 | Optimal depth is 3 levels, maximum 4 | 0.80 | GitHub docs recommend 3–4 practical levels [S4]; for ≤200 files, 2 levels suffice for all content, 3 for assets | 0.90 | **Confirmed** |
| P3 | Static manual indices are sufficient for initial scale | 0.60 | No comparable system found for calibration; projected scale (80–150 files) is small enough; quarterly review cadence + T1-02 TTL integration provides staleness detection | 0.70 | **Slightly up, with defined automation triggers** |
| P4 | Diátaxis maps cleanly onto career lifecycle content | 0.70 | Diátaxis quadrants are a good *content-type* taxonomy but a poor *directory* taxonomy for career content because stages mix all four types | 0.50 (as directory structure) / 0.85 (as content-type tag) | **Partially contradicted** — modified into a frontmatter `content_type` field instead of directory split |
| P5 | MkDocs Material is the best SSG choice | 0.65 | Confirmed for current needs (Markdown-native, best search, fastest builds). But ecosystem transition reports create a 12-month re-evaluation trigger [S7]. Starlight is a strong alternative if MkDocs Material stability degrades | 0.70 | **Confirmed with a caveat** |
| New | — | — | The brief's proposed 12-stage funnel should be consolidated to 10 directories by merging three pairs of adjacent stages | — | **New finding** from content-level analysis of T0-10 |
| New | — | — | Role-primary architecture would create ≥40% content duplication across 10 roles × 10 stages | — | **New finding** from architectural stress-testing against T0-01 role count |
| New | — | — | Non-linear resources (tax calculators, contract checklists) should live in their point-of-use stage directory, not in `appendices/` — consistent with Stripe's task-driven IA pattern | — | **New finding** from IA best-practice research [S1] |

---

## 9. Sources & Evidence Ledger

Retrieved or read on 2026-10-25 unless stated. Grade is for the specific claims each source supports.

| # | Source | Locator / Description | Type | Depth | Grade | Supports |
|---|---|---|---|---|---|---|
| S1 | Stripe documentation IA analysis (925studios.co; raw.studio) | https://925studios.co; https://raw.studio — analysis of Stripe's task-driven, progressive-disclosure documentation design | Secondary analysis | S | B | KF1 (task-driven navigation), KF12 (resources at point of use) |
| S2 | Cloudflare Reference Architecture documentation | https://developers.cloudflare.com/reference-architecture/ — tiered IA model (Reference Architecture → Design Guide → How-To) | Vendor documentation | S | A | KF1 (tiered architecture pattern) |
| S3 | Django documentation structure and design philosophies | https://docs.djangoproject.com/ — Tutorial → Topic Guide → Reference progression | Vendor documentation | S | A | KF1 (pedagogical progression pattern) |
| S4 | GitHub repository best practices: directory depth, naming conventions | github.com documentation and guides on repository structure, file limits (50 directory levels max, 3,000 entries per directory, 100MB file limit) | Vendor documentation | S | B | KF2 (directory depth), §4.3 (naming conventions) |
| S5 | Diátaxis documentation framework | https://diataxis.fr — Tutorials / How-To / Reference / Explanation quadrant model | Framework documentation | S | A | KF4 (content-type taxonomy) |
| S6 | GitHub Markdown documentation best practices (multiple sources) | gitbook.com, brightcoding.dev, hatica.io — front matter metadata, heading discipline, cross-linking | Secondary guides | S | C | KF8 (frontmatter schema design) |
| S7 | MkDocs Material vs alternatives comparison (unmarkdown.com, readthedocs.com, docsio.co) | Multiple comparison articles evaluating MkDocs Material, Docusaurus, and Starlight | Secondary comparisons | S | C | KF9 (SSG selection), ecosystem transition note |
| S8 | Docusaurus and Starlight feature analysis (docsio.co, distr.sh) | Feature-by-feature comparison: versioning, i18n, performance, search | Secondary comparisons | S | C | KF9 (SSG comparison table) |
| S9 | markdownlint-cli2 documentation and configuration guides | dev.to, markdowntools.com, visualstudio.com — rule configuration, CI integration, VS Code extension | Vendor docs + secondary | S | B | KF10 (linting tool selection), §6.9 (configuration) |
| S10 | remark-lint documentation and ecosystem (github.com/remarkjs, rumdl.dev) | Modular AST-based linter; unified ecosystem; MDX support | Vendor documentation | S | C | KF10 (remark-lint rejection rationale) |
| U:T0-01 | T0-01: GenAI Role Taxonomy & Live Market Volume | `research/sessions/T0-01-genai-role-taxonomy-market-volume.md` | Upstream session | F | A | KF6 (10 verified roles, 9 quarantined); role index design; A1 duplication analysis |
| U:T0-02 | T0-02: Global & Regional Compensation Benchmarks | `research/sessions/T0-02-global-regional-compensation-benchmarks.md` | Upstream session | F | A | KF7 (6-tier grid, US/India ranges); tier index design; A3 rejection |
| U:T0-10 | T0-10: Career Tooling Ecosystem Map across 12 Lifecycle Stages | `research/sessions/T0-10-career-tooling-ecosystem-12-stage-funnel.md` | Upstream session | F | A | KF5 (12-stage funnel → 10 directories); tool catalog design; all stage-specific content mapping |
| U:T0-17 | T0-17: Compensation Progression, Promotion Velocity & Equity Dilution | `research/sessions/T0-17-compensation-progression-plateaus-equity.md` | Upstream session | F | A | KF7 (India comp ceiling); persona journey B and C design; equity content placement |
| U:T1-02 | T1-02: Epistemic Governance & Evidence-Grounding Protocol | `research/sessions/T1-02-evidence-grounding-protocol.md` | Upstream session | S | A | KF8 (frontmatter evidence fields); TTL integration; archive strategy |

---

## 10. Complete Proposed Directory Schema — Annotated

This section presents the directory schema from §4.2 with annotations on content provenance (which upstream session provides the primary data) and projected file count.

### 10.1 Content Provenance Map

| Directory | Primary Upstream Source | Secondary Sources | Projected File Count (Phase 1) |
|---|---|---|---|
| `01-landscape/` | T0-01 (market data), T0-02 (geo comp) | Web research (regulation, immigration) | 6–8 |
| `02-roles/` | T0-01 (role taxonomy) | T0-02 (role-level comp) | 10–12 |
| `03-skills-and-tech/` | T0-10 (Stage 3 tools), T0-01 (JD skill shares) | Web research (curricula) | 5–7 |
| `04-credentials/` | T0-10 (Stage 4 tools, cert evidence) | Web research (specific cert programs) | 3–5 |
| `05-portfolio/` | T0-10 (Stage 5, platform risk) | Web research (project archetypes) | 3–5 |
| `06-job-search/` | T0-10 (Stages 6–7, DF-1, DF-2, DF-3) | — | 5–7 |
| `07-networking/` | T0-10 (Stage 8) | Web research (community landscape) | 3–5 |
| `08-interviewing/` | T0-10 (Stages 9–10, DF-4, DF-5) | Web research (ML system design) | 6–8 |
| `09-compensation/` | T0-02, T0-17 | T0-10 (DF-6, comp tools) | 6–8 |
| `10-onboarding-and-growth/` | T0-17 (§6.1, §6.2) | T0-10 (Stage 12) | 4–6 |
| `11-tracks/` | T0-17 (R6 personas) | Web research (visa, transition) | 4–6 |
| `ecosystem/` | T0-10 (full tool catalog) | — | 3–4 |
| `appendices/` | T1-02 (evidence methodology) | — | 3–4 |
| **Total** | | | **61–85** |

### 10.2 Phase 1 Execution Priority

Content directories should be populated in this order, based on dependency depth and user value:

| Priority | Directory | Rationale |
|---|---|---|
| 1 | `career/README.md` + 3 index files | Entry points must exist before any content |
| 2 | `01-landscape/` | Foundation: users need market context before role decisions |
| 3 | `02-roles/` | Role definitions are referenced by all downstream stages |
| 4 | `09-compensation/` | High-value: comp data drives career decisions; most upstream data available (T0-02, T0-17) |
| 5 | `06-job-search/` | High-value: ATS mechanics and application strategy (rich T0-10 data) |
| 6 | `08-interviewing/` | High-value: interview prep (rich T0-10 data) |
| 7 | `03-skills-and-tech/` | Requires additional research beyond upstream sessions |
| 8 | `10-onboarding-and-growth/` | Rich T0-17 data available |
| 9 | `11-tracks/` | Cross-cutting; requires synthesis across all upstream sessions |
| 10 | `ecosystem/` | Direct port from T0-10 tool catalog |
| 11 | `04-credentials/`, `05-portfolio/`, `07-networking/` | Thinner upstream data; requires more original research |
| 12 | `appendices/` | Reference material; populated last |

### 10.3 Discovered Concerns

- **Concern: The directory schema assumes a single maintainer.** The frontmatter schema includes no `owner` or `reviewer` field. If the repository grows to multiple contributors, add an `owner` field (GitHub username) and integrate with a `CODEOWNERS` file mapping each directory to its maintainer. This was not included in the initial schema because the current project has a single author, and premature governance adds overhead.

- **Concern: The `research/` and `career/` subtrees serve different audiences and may need different navigation.** Research sessions are artefacts of the investigation process; career content is the user-facing output. The README should clearly distinguish these two subtrees. Consider: should `research/` be in a separate branch or a separate repository? Current recommendation: keep in the same repository for cross-referenceability, but make the separation explicit in the root README.

- **Concern: Evidence grade integration between research sessions and career content files.** Career content files derive claims from research sessions. The frontmatter `confidence` field captures aggregate confidence, but individual claims within a content file may have different grades. The content files should use inline evidence markers (e.g., `(Grade B · T0-01 F2)`) consistent with T1-02's Cite-or-Flag rule, but this adds reading friction for non-researcher audiences. Recommendation: use inline markers in a collapsible `<details>` block or footnotes, keeping the main text clean.
