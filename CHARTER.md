# Charter: GenAI Career Intelligence System

> **Status note (2026-11-07).** This charter was written for Phase 0 (October 2026) and is kept as the statement of vision and scope; where it and later records differ, the later records apply:
> - **Research:** "23 research sessions" counts the 22 session files in [research/sessions/](research/sessions/) plus the Founding Architecture Document ([research/FAD.md](research/FAD.md)), the Layer 3 synthesis.
> - **Grades:** besides A–E, the repository uses M (model output) and P (practice-curated); the definitions are in [CONTRIBUTING.md](CONTRIBUTING.md) §3.
> - **Pay tiers:** the six tiers remain a vocabulary, but their bands are contested in the evidence ([research/ERRATA.md](research/ERRATA.md) U5 and U14), so the guides use measured pay by title, level and location ([pay benchmarks](career/09-compensation/pay-benchmarks.md)) rather than tier bands.
> - **Scope rule in practice:** the repository curates and does not teach; interview prep packs give prompts, what a strong answer covers and red flags, never model answers (decision D-018).

## Vision

Build the most reliable source of career intelligence for professionals working in Generative AI, ML Systems, and Applied AI Engineering.

The repository exists because the information landscape for AI careers is fractured, ephemeral, and unreliable. Salary claims are recycled without sources. Role titles proliferate without hiring demand. Tool recommendations are affiliate-driven. Tax and visa guidance is outdated within months. Career advice is generic across a field where the difference between a ₹30L role and a ₹3Cr role is not "work harder" but a concrete, measurable set of technical depth, proof-of-work, and positioning decisions.

This project closes that gap by treating career navigation as an **intelligence problem** — one that requires the same rigour applied to engineering systems: verified inputs, explicit assumptions, traceable conclusions, and continuous recalibration against reality.

---

## Scope

### What This Is

A structured knowledge repository that synthesises primary-source evidence into actionable career intelligence across the full professional lifecycle. The repository:

1. **Verifies which roles exist.** Measures live hiring demand against a quorum threshold, separating established careers from speculative titles.
2. **Maps compensation empirically.** Documents salary, equity, and total compensation distributions by role, seniority tier, and geography — sourced from employer disclosures, aggregator datasets, and government filings, not self-reported anecdotes.
3. **Evaluates the ecosystem.** Audits tools, platforms, certifications, and communities across every career stage with an explicit rating rubric, evidence grades, and "last verified" timestamps.
4. **Provides situational guidance.** Delivers different advice for different users: a fresh graduate in India, a senior engineer weighing equity at a frontier lab, and a European professional navigating cross-border contracting face fundamentally different decisions.
5. **Maintains itself.** Enforces temporal freshness through TTL-based recency classes, CI-enforced linting, and a structured evidence protocol (EGP-1.0) that flags stale or unverified claims.

### What This Is Not

| | |
|---|---|
| **Not a course or curriculum** | The repository curates and evaluates external learning resources. It does not teach ML fundamentals. |
| **Not a job board** | It provides intelligence on where and how to find opportunities. It does not host listings. |
| **Not an opinion piece** | Claims are grounded in evidence or explicitly flagged as unverified. "I think" is replaced with "the data shows" or "no data found." |
| **Not a snapshot** | Content is designed for continuous maintenance. Every technology claim carries a verification timestamp. Every factual assertion is traceable to a source. |

---

## Audience

The repository serves any professional navigating a GenAI career, without geographic or experience-level restriction. The design explicitly accommodates:

- **Entry-level** engineers choosing their first AI role and building foundational skills.
- **Mid-career** professionals transitioning from adjacent fields (backend engineering, data science, product, academia) into AI.
- **Senior and Staff+** engineers evaluating frontier lab equity, planning tier jumps, or optimising international compensation.
- **India-based** professionals seeking maximum domestic or international compensation through remote contracting, GCC employment, or relocation.
- **Independent practitioners** building fractional AI consulting or advisory practices.

The common thread: each user arrives at a different career stage, with a different background, targeting a different outcome. The repository must serve them all with tier-appropriate, situation-specific intelligence — never with generic, one-size-fits-all advice.

---

## Organising Frameworks

Three orthogonal dimensions structure all content:

### 1. The 12-Stage Career Lifecycle Funnel

The primary navigation spine. Every professional traverses these stages, though not necessarily in order:

| # | Stage | What It Covers |
|---|---|---|
| 1–2 | **Awareness & Exploration** | Market landscape, role taxonomy, employer tiers, geographic compensation |
| 3 | **Skill Building** | Technical competencies, compute infrastructure, learning paths |
| 4 | **Certification** | Cloud credentials, vendor badges, recruiter filtering signal |
| 5 | **Portfolio** | Production proof-of-work, project archetypes, platform risk |
| 6–7 | **Discovery & Application** | Job boards, ATS mechanics, resume strategy, auto-apply risks |
| 8 | **Networking** | Communities, conferences, mentorship, referral channels |
| 9–10 | **Interview Prep & Execution** | System design patterns, coding rounds, employer AI policies |
| 11 | **Negotiation** | Compensation stratification, equity valuation, offer diligence |
| 12 | **Onboarding & Growth** | First 90 days, promotion velocity, hop-vs-stay calculus |

### 2. Six Universal Compensation Tiers

Cross-cutting lens for all career advice. Each tier represents a distinct compensation band with different skill requirements, proof-of-work expectations, and negotiation dynamics. Tiers span T0 (Entry/New Grad) through T5 (Distinguished/VP+), with US and India ranges documented in the compensation research.

### 3. Transition Personas

User archetypes that define the most common starting points: Backend/Systems SWE, Data Scientist/Analyst, Frontend/Full-Stack, Non-Technical Professional, and Academic/PhD Researcher. Each persona has a different optimal path through the lifecycle stages.

---

## Evidence Standard

The repository operates under an epistemic protocol (EGP-1.0, defined in research session T1-02) with these non-negotiable rules:

1. **Every factual claim cites a source or is flagged.** No unmarked assertions of fact.
2. **Sources are graded A–E** by type, with explicit downgrade flags for conflicts of interest, staleness, and methodological weakness.
3. **Technology claims carry verification timestamps.** Tool versions, API behaviours, and pricing can change within weeks.
4. **Honest gaps are valued.** "Searched X and found no evidence" is a valid, publishable result. An honest gap is infinitely more valuable than a plausible-sounding fabrication.
5. **Temporal freshness is enforced.** Seven volatility classes with TTLs from 14 days (policy status) to "none" (historical facts). Stale content is flagged, not silently left in place.

---

## Success Criteria

The project succeeds when:

| Criterion | Measurable Target |
|---|---|
| **Coverage** | User-facing content exists for all 12 lifecycle stages, with ≥3 files per stage directory |
| **Evidence depth** | ≥80% of factual claims in published content carry Grade A or B evidence |
| **Temporal freshness** | ≤5% of published content files have `last_verified` dates older than their TTL class allows |
| **Audience breadth** | Navigation journeys validated for ≥4 distinct personas across ≥2 geographies |
| **Ecosystem audit** | ≥50 tools catalogued with explicit ratings and "last verified" timestamps |
| **Compensation accuracy** | Tier boundaries and ranges validated against ≥3 independent primary sources per geography |
| **Maintenance sustainability** | Content update cadence of ≤quarterly for all files with TTL ≤365 days |

---

## Constraints

- **Temporal anchor: October 2026.** All current findings reflect late-2026 ground truth. Content from earlier periods is valid only where explicitly marked as historical or where the underlying fact has not changed.
- **Global breadth, India depth.** The repository is globally applicable but provides unmatched tactical depth for India-based professionals — reflecting both the author's context and the complexity of India's cross-border compensation, tax, and immigration landscape.
- **Single-author capacity.** The repository is maintained by one person (as of November 2026). Architectural decisions must account for this constraint. Automation is preferred over manual process wherever the scale justifies it.
- **Not legal, tax, or financial advice.** The repository documents regulatory landscapes and tax structures for informational purposes. Users must consult qualified professionals for their specific circumstances.

---

## Research Methodology

The repository's content is produced through a structured research pipeline (the Vivechak framework) consisting of 23 research sessions across four layers:

| Layer | Purpose | Sessions |
|---|---|---|
| **Layer 0** | Foundational landscape research — independent, parallel investigations into each domain | 18 sessions |
| **Layer 1** | Structural blueprints — information architecture, evidence protocol, tactical synthesis | 3 sessions |
| **Layer 2** | Action plan synthesis — tier-calibrated playbooks across all persona × tier combinations | 1 session |
| **Layer 3** | Grand synthesis — the Founding Architecture Document that locks all decisions and launches Phase 1 | 1 session |

Each session follows a standardised format: prior beliefs → research question → key findings (with evidence grades) → recommendation → alternatives considered → open questions → belief-change delta → source ledger. The full pipeline specification lives in [`research/RESEARCH-PIPELINE.md`](research/RESEARCH-PIPELINE.md).

---

## Governance

- **Decision Registry:** All significant structural and methodological decisions are recorded in [`research/DECISIONS.md`](research/DECISIONS.md) with explicit status, evidence references, and review triggers.
- **Anti-dogmatism clause:** Nothing in this repository is immune to revision. If primary evidence contradicts an existing position, the position is updated. Structural commitments, personal preferences, and sunk-cost reasoning are not valid reasons to preserve incorrect content.
- **Transparency:** The repository's research process, including its limitations, gaps, and unresolved questions, is published alongside its conclusions. The research sessions document what was searched, what was found, and what was not found.
