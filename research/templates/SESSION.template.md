---
id: "[SESSION-ID]"
title: "[Session Title]"
date: "[YYYY-MM-DD]"
status: draft                    # draft | complete | complete-with-gaps
topic: "[topic-slug]"
tags: ["tag1", "tag2"]
informs_decisions: ["D-NNN"]     # Use D-### IDs, not prose descriptions
confidence: "[high|medium|low]"  # Use string labels, not floats
schema_version: "0.1.0"
temporal_anchor: "[YYYY-MM]"     # Month of temporal anchor (ISO format)
last_verified: "[YYYY-MM-DD]"    # Date of last verification pass
# Optional fields:
# confidence_note: "[Detailed confidence breakdown by claim type]"
# author_disclosure: "[LLM model name or human author, plus any COI flags]"
# authored_by_model: "[Model name if LLM-authored, e.g., gemini-2.5-pro, claude-opus-4]"
# evidence_window: "[YYYY-MM-DD to YYYY-MM-DD]"
# dependencies_consumed: ["T#-##"]  # Upstream sessions consumed (Layer 1+ only)
# protocol_version: "EGP-1.0"
---

# [SESSION-ID]: [Session Title]

> **Epistemic Guide.** `S##` references the Sources & Evidence Ledger (§9). Grades **A–E** follow EGP-1.0 (see `.agents/rules/egp-protocol.md`). Grade **M** = model output inheriting weakest input grade. `↑` = inherited grade from upstream session. `[D]` = design judgement. The temporal anchor is [YYYY-MM-DD].

## Prior

Beliefs held *before* searching, written as checkable propositions. Section 8 (Delta) reports what the evidence did to each.

| # | Checkable Proposition | Initial Confidence | Grade |
|---|---|---|---|
| P1 | [Pre-research assumption 1] | [High/Medium/Low] | D |
| P2 | [Pre-research assumption 2] | [High/Medium/Low] | D |

## Research Question

**Decision.** [The specific question this session investigates.]

**Sub-questions:**
1. [Sub-question mapped to domain probes]
2. [Sub-question mapped to domain probes]

**Scope.** In scope: [what's covered]. Out of scope: [what's excluded].

**Method.** [Data sources, search strategies, corpus sizes, deliberate falsification searches.]

## Key Findings

| # | Finding Headline | Key Empirical Evidence | Grade |
|---|---|---|---|
| **KF1** | **[Finding 1]** | [Evidence-grounded statement with source refs `[S##]`] | **[A-E/M]** |
| **KF2** | **[Finding 2]** | [Evidence-grounded statement with source refs `[S##]`] | **[A-E/M]** |

## Recommendation

[What to do and why, referencing evidence above. Include what would change this recommendation.]

## Alternatives Considered

| Option | Verdict | Key Tradeoff |
|---|---|---|
| **[Option A]** | **Recommended** | [Why this wins] |
| **[Option B]** | **Rejected** | [Why this loses] |

## Detailed Findings

### KF1 — [Finding 1 Title]

[Extended analysis with full evidence chain, sub-claims with individual grades, and source references.]

### KF2 — [Finding 2 Title]

[Extended analysis...]

## Open Questions & Risks

| Risk / Question | Impact | Mitigation |
|---|---|---|
| [Risk 1] | [High/Medium/Low] | [How to mitigate] |

## Discovered Concerns

<!-- Document unexpected findings, risks, constraints, or failure modes discovered OUTSIDE
the original research scope. These are things you didn't expect to find.
For one-way door sessions, this section must contain substantive analysis (≥50 characters). -->
- **[Concern Title]**: [Description, potential impact, and suggested follow-up]

## Delta

| # | Prior Belief | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | [Prior 1] | [Confirmed/Contradicted/Updated] | [What changed] | [High/Medium/Low] |

## Sources & Evidence Ledger

| # | Source | Grade | Access | Modifiers | Used For |
|---|---|---|---|---|---|
| S1 | [Source name and URL] | [A-E] | [Read/Extract/Blocked/Gap] | [corroborated · fresh · COI:vendor] | [What claim it supports] |
