---
id: research.errata
title: "Research Errata: Known Errors in the Phase 0 Research Records"
content_type: reference
stage: 0
status: published
last_verified: 2026-11-06
summary: "Errors found in the sealed Phase 0 records (FAD, DECISIONS, T0-03, T0-06, T0-17, T1-01, T1-03, T2-01) and the correct reading, with evidence. Read before relying on those files."
sources: [T0-01, T0-02, T0-03, T0-04, T0-06, T0-07, T0-08, T0-09, T0-10, T0-11, T0-14, T0-17, T0-18, T1-01, T1-03, T2-01]
---

# Research Errata

The research sessions, FAD and the decision registry are dated Phase 0 records. They are kept as written, so that their provenance stays intact. Errors found later are logged here, with the correct reading and its evidence. **The career documents already apply these corrections.** When a sealed record and this list disagree, this list wins.

**Records with errata (2026-11-07):** FAD, DECISIONS, T0-03, T0-06, T0-17, T1-01, T1-03 and T2-01. Candidate errata that are not yet confirmed are listed in [ROADMAP.md](../ROADMAP.md) §7. Of the 33 record locations the 26 errata cite (one per record per row), 29 are in syntheses (FAD, DECISIONS, T1-01, T1-03, T2-01); the corrections rest on the Layer 0 sessions.

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

## Errors found while building the stage guides (2026-11-05)

| # | Location | Error | Correct reading | Evidence |
|---|---|---|---|---|
| U13 | T2-01 L246 | Advises backend engineers to "consider the ML specialty cert" for AWS or GCP | AWS Machine Learning – Specialty was retired (last exam 31 March 2026). The current AWS option is Generative AI Developer – Professional (AIP-C01); Google's is Professional Machine Learning Engineer | T0-11 L165–166 |
| U14 | T0-17 L138 and T1-03 L368 vs FAD §4.1 (L133–138) and T2-01 L92 | Two different India tier bands are in use: T2 ₹60L–1.2Cr with a T3 floor of ₹1.2Cr (T0-17, T1-03, from the research brief) against T2 ₹30–75L and T3 ₹75L–1.5Cr (FAD, T2-01) | Neither band set is measured. Use the measured anchors instead: Greater Bengaluru Senior SWE median ≈ ₹56.0L, P90 ≈ ₹1.07Cr; top-employer senior medians ₹1.06–1.22Cr (Levels.fyi, n = 4,836) | T0-17 KF4 L137 |
| U15 | FAD §6.2 item 2 (L221) | "11–19% of specialised infrastructure employer postings" | The same error as U12: 11.1%–19.2% is a share of companies (S09), not of postings | T0-03 §6.3; U12 |
| U16 | FAD §18.4 (L707); FAD §10 (L382) | Plans ATS guidance as "parser bypass rules" and lists Jobscan as a primary ATS tool | Write parse-safe documents and answer knockout questions; do not game parsers (no hidden text or keyword blocks). Use "ATS score" tools only as a posting-gap list: they have no demonstrated link to real ATS outputs | T0-04 R6 L130; T0-04.F12 L102 |
| U17 | FAD §10 (L385) | Lists interviewing.io and Pramp as the primary interview-prep platforms | For GenAI system design the best-verifiable offering is Hello Interview, and no prep platform has independent outcome evidence | T0-10.F9 L85 |
| U18 | FAD §3.3 (L121) | "PhD → T3+: skip 01, 03, 04" | T2-01's own PhD playbook runs an 8-week Stage 3 (skills) block: production Python, deployment, evaluation infrastructure, agents | T2-01 L574–581; T0-06 D8 |
| U19 | T2-01 §8 (L706) | A $75K–$94K billing range is the §44ADA "dead zone" | At T2-01's own rate of ₹96 per dollar, T0-07's dead zone of ₹75L to roughly ₹92–98L is about $78K to $96–102K. Use T0-07's rupee band and convert at the current rate | T0-07 L125; T2-01 L706 |
| U20 | DECISIONS D-004 rationale (L271) | Table-stakes skills "appear in >80% of postings but command T0–T1 compensation"; differentiating skills appear in <30% and command T2–T4 | No measurement supports the >80% threshold: RAG is named in 54.0% of AI Engineer postings and 10.0% of broad postings, and LLM skills in 76.7% of AI Engineer postings. T0-03 itself finds that posted pay tracks seniority and employer tier more than skill tier. The skills ontology tiers skills by role-defining status and measured shares, not by these thresholds | T0-03 L41, L421; data/posting_skill_shares.json (JobsPipe, 2026-11-02; formerly role-skill-maps §2.1) |
| U21 | T2-01 KF6 (L78) | First-90-day failure modes: "role ambiguity (43% of all hires)" and "compute gating (85% delayed)" | 43% is the share of surveyed job seekers who said the role differed from what hiring led them to expect (Jobvite 2018). 85% is the share of 1,367 AI professionals whose organisations had delayed projects for lack of GPUs, in a survey sponsored by Civo, a GPU-cloud vendor. Neither is a per-hire rate | T0-09 L81, L94 |
| U22 | DECISIONS D-007 rationale (L463); T2-01 L177, L599 and KF4 (L76) | D-007 credits the 12–18-month O-1A evidence-building estimate to T0-08 KF1 and the UK no-employer route to T0-08 KF6; T2-01 credits the same estimate to T0-08 KF1–KF2 and grades it A/B in KF4 | In T0-08, 12–18 months is a practitioner estimate (Grade C; §8.1 L375, Recommendation L77). The UK no-employer route is Key Finding 7 (L58); Key Finding 1 (L46) is about USCIS policy and Key Finding 6 (L56) about O-1A as a bridge to permanent residence. Quote the 12–18 months as a Grade C practitioner estimate | T0-08 L46, L56, L58, L77, L375 |
| U23 | T2-01 §6.6 (L642) | UK contract rates "£463–£675/day (P25–P75)" shown beside "£58–£99/hr" | At 8 hours a day, P25–P75 is about £58–£84 an hour; £99 corresponds to the P90 day rate (£788). All are asking rates in job adverts, not transacted rates | T0-18 L95 |
| U24 | T1-03 §6.1 (L158–161); T1-03 KF1 (L70) | Stage rates attributed to Ashby and Gem: application → recruiter screen "≈ 12–18%", screen → loop 20–30%, offer → accept 50–70%; KF1 calls the ≈ 0.2% figure "cold-inbound to offer" | T0-04, which T1-03 builds on, reports the same sources as 3.6% (Ashby, technical, Q1 2026) to 6% (Gem, engineering) of applications reaching a first human stage, then 17% to onsite, 29% onsite to offer and 73% acceptance. Use T0-04's chain for planning. The ≈ 0.2% figure is application to hire (about 460–520 applications per hire); to offer it is about 340–380 applications | T0-04 KF9 L90–91, L397–407 |
| U25 | T0-06 L792, L846 | "15–20 h/week is 56–74% of average leisure" | 56–74% is the share for the 17.5-hour midpoint (against about 31.5 or 24 hours of weekly leisure, without or with a child under 18). Across 15–20 hours a week it is about 48–83% | T0-06 L211–213 |
| U26 | T1-03 KF2 (L71) and L104 | "41/112 Anthropic reports" for the whole infrastructure track (inference serving, batching, GPU scheduling) | 41 of the 112 aggregated reports are the inference-API prompt alone; batch inference (12), GPU cluster (7), mixed-size GPU allocation (4) and roofline analysis (4) are counted separately, so the infrastructure share is larger than 41 of 112. All counts are from one unaudited aggregator | T0-14 L80 |

## How to add an erratum

1. Give it the next free ID: one more than the last row above (U27 after U26).
2. Cite the exact location (file, section and line).
3. State the correct reading and its evidence (session and line, or an external source with a date).
4. Apply the correction in the affected career documents, and note it in [CHANGELOG.md](../CHANGELOG.md).
