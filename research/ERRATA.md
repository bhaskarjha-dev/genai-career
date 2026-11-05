---
id: research.errata
title: "Research Errata: Known Errors in the Phase 0 Research Records"
content_type: reference
stage: 0
status: published
last_verified: 2026-11-04
summary: "Errors found in the sealed Phase 0 records (FAD, DECISIONS, T0-03, T1-01, T2-01) and the correct reading, with evidence. Read before relying on those files."
sources: [T0-01, T0-03, T0-06, T0-14, T0-17, T1-01, T2-01]
---

# Research Errata

The research sessions, FAD and the decision registry are dated Phase 0 records. They are kept as written, so that their provenance stays intact. Errors found later are logged here, with the correct reading and its evidence. **The career documents already apply these corrections.** When a sealed record and this list disagree, this list wins.

## Upstream errors found while building the role catalogs (2026-11-03)

| # | Location | Error | Correct reading | Evidence |
|---|---|---|---|---|
| U1 | FAD §5.1 (L165); T1-01:80 | Applied Scientist "~700" postings, "Established" | No primary source; T0-01 measured 14 at 12 AI startups (Jun 9) and left Big Tech unmeasured | T0-01 D2 row 12; T0-01 Bottom line |
| U2 | FAD §17 A5 (L629) | "4 Established, 5 Partial, 9 Quarantined" | 3 established title families | T0-01 Bottom line |
| U3 | FAD §5.3 (L179) | Quarantine list | Adds 5 never-searched buzzwords and LLMOps; drops Prompt Wizard, Context Architect, Context Harness Engineer, Principal Agentic Context Engineer and Vibe Engineer | T0-01 D4, Recommendations 3–4 |
| U4 | FAD §4.2–4.3, §12.1 (L136, L144–145, L436–437); T1-01:84 | "$312K T2 median" and "India T2 median ₹1.06–1.22Cr", both credited to T0-02 | $312K is the US all-company Senior median (T0-17). ₹1.06–1.22Cr is the top-5 employers' senior medians, ≈P90; the Greater Bengaluru Senior SWE median (Levels.fyi) is ₹56.0L. Neither figure is in T0-02 | T0-17:129, 137 |
| U5 | FAD §4.1; DECISIONS D-003 | US T0 cap $120K and T1 cap $200K | Both sit below the measured Entry ($155K) and Mid ($226K) medians | T0-17:129 |
| U6 | DECISIONS D-002 rationale | "T0-01 KF6 shows function-first classification is more stable" | T0-01 F6 is about false-positive platform counts | T0-01 F6 |
| U7 | T2-01 §4.1 header | US tier ranges ($80–150K T1, $150–312K T2, $312–450K T3) | Differ from FAD §4.1 | FAD §4.1 |
| U8 | T2-01:632 | 8.2-year median attributed to AI PMs | Belongs to AI consultants/strategists | T0-06:109, 174 |
| U9 | T2-01 KF1 | "8–12 high-volume corridors" | Its own matrix has 5 ● cells | T2-01:92–98 |
| U10 | T1-01:78, 325, 372 | "10 verified roles" | 4 verified + 5 partial were listed (and 3 verified per T0-01) | T1-01:80 |
| U11 | T0-03 L454–455 | KV cache 327,680 B/token labelled FP8 | That is the BF16 value; FP8 is half (T0-14 gives 320 KiB/token at BF16) | T0-14:L646 |
| U12 | T0-03 L58, L536 | "11.1%–19.2% of specialized company listings", which reads as a share of postings | It is the S09 company share (TRT-LLM 11.1% to vLLM 19.2% of companies), not a share of postings | T0-03 §6.3 |

## How to add an erratum

1. Give it the next ID (U13, U14, …).
2. Cite the exact location (file, section and line).
3. State the correct reading and its evidence (session and line, or an external source with a date).
4. Apply the correction in the affected career documents, and note it in [CHANGELOG.md](../CHANGELOG.md).
