---
id: roles.rankings
title: "Best GenAI Jobs, Ranked"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-05
summary: "Evidence-weighted ranking of the GenAI roles (CCI): pillar scores with uncertainty ranges, Monte Carlo ranks, weight sensitivity, goal, persona and India lenses, and a dossier per role."
sources: [T0-01, T0-02, T0-17, T0-03, T0-06, T0-15, T0-16]
---
# Best GenAI Jobs, Ranked
## An Evidence-Weighted, Uncertainty-Aware Composite Career Index (CCI) for Every Canonical GenAI Role

> **Updated:** 2026-11-04 · **Method:** Composite Career Index (CCI) with anchored 0–10 pillars, uncertainty ranges and Monte Carlo simulation.
> **Role universe:** the 29 canonical roles of the [master catalog](role-catalog.md): 24 individual-contributor (IC) roles plus 5 leadership/independent tracks
> **Evidence standard:** EGP-1.0. Composite scores are **model outputs (Grade M** per the [README](../../README.md) evidence standard: a model output inherits the weakest grade among its inputs). They combine graded measurements (A–C) with labelled judgements (D). They are decision aids, not facts.
> **Reproduce:** `python3 scripts/rank_roles.py --update` reads [data/role_scores.json](../../data/role_scores.json) and rewrites every block between the `BEGIN/END GENERATED` markers in this file, including Appendix A (standard library only, fixed seed). The narrative and the hand-written tables in §0, §5.1 and §7 are checked by hand after any change in ranks
> **Companions:** [role-skill-maps.md](../03-skills-and-tech/role-skill-maps.md) gives the full skill stack for every ranked role · [role-skill-inventories.md](../03-skills-and-tech/role-skill-inventories.md) types every skill per role (concepts, methods, tools, frameworks, platforms, non-technical skills) with evidence · [resume-skills-matrix.md](../06-job-search/resume-skills-matrix.md) tiers those skills for resumes

---

## 0. The Answer

**Co-#1: Machine Learning Engineer and AI Engineer.** They are statistically tied:
- **Monte Carlo:** MLE ranks #1 in 64% of 20,000 draws and AI Engineer in 34%; both land in the top three in ≥98% of draws.
- **Weight profiles:** each takes #1 under three of the six profiles.

Choose between them on preference:
- **Machine Learning Engineer wins on pay and depth.** US total comp P50 is $280K vs $154K; P90 is $497.5K vs $280K (Levels.fyi, B). About half of that gap is employer mix (the MLE title concentrates at Big Tech); within Google, the MLE title still earns 26–39% more (T0-02).
- **AI Engineer wins on demand and accessibility.** It is the largest GenAI title family in the measured corpora: 1,697 US, 398 India and 3,944 global live postings (family counts that include robotics, construction and Power Platform variants). It also has the shortest modelled switch routes; backend engineers take about 6 months.

**#3: Research Engineer / Member of Technical Staff** (top 5 in 90% of draws; between #2 and #5 under every weight profile).
- **For it:** the highest engineering pay in the corpus (OpenAI/Anthropic SWE/MTS TC medians ~$875–882.5K on Levels.fyi, n=242 and n=49; cached OpenAI medians have ranged $555–875K), and it absorbs post-training/RL work.
- **Against it:** narrow access (PhD, fellowships, strong OSS), a live count that is unmeasured, and pay that is 49–72% semi-liquid stock at senior levels.

**#4: Forward Deployed Engineer** (top 5 in 79% of draws).
- **For it:** the largest title family at AI startups (a 933-role cluster) and the joint-highest Leverage judgement (8.5, Grade D).
- **Against it:** only about half the cluster is engineer-titled; its median posted base is the **lowest** of the measured families ($180–248K); its ~20% growth matched AI and ML Engineer rather than outpacing them.

**#5–#8 are a statistical tie band (CCI 66.7–68.0):** Applied AI Engineer, Research Scientist, Applied Scientist and AI Infrastructure Engineer. Their order flips with the weights, so choose among them with the lenses in §5.

**The most important finding: the best skills are not the best titles.** Evals, agent reliability and inference/cost engineering are the strongest differentiators in the evidence, but as standalone titles they are small (Agentic AI Engineer #12, AI Evaluation Engineer #14). Use them as force multipliers inside AI Engineer, MLE, FDE or Research Engineer.

### Why Notable Roles Rank Where They Do

| Role | Rank (CCI) | What the evidence shows |
|---|:---:|---|
| Machine Learning Engineer | 1 (77.9) | Second-largest measured demand and the highest measured broad-market pay distribution |
| AI Engineer | 2 (76.9) | Largest measured demand and best accessibility |
| *Research Engineer / Member of Technical Staff* | **3 (71.4)** | Highest engineering pay in the corpus ($220–330K+ base) |
| Forward Deployed Engineer | 4 (70.6) | The corpus has no FDE pay data, and the measured posted base is the lowest family median. The 933 count is a cluster of which ~48% is engineer-titled (an extrapolation), and its growth matched other families |
| *Applied AI Engineer* | **5 (68.0)** | Strong startup and frontier-lab demand; T0-01 "likely pass" sub-node |
| Research Scientist (AI/ML) | 6 (67.8) | Highest Pay score (9.5), but Access is only 2.9: it needs a PhD |
| Applied Scientist | 7 (67.5) | Big Tech volume and pay are unmeasured in the corpus; low confidence |
| AI Infrastructure / GPU Platform Engineer | 8 (66.7) | Posted base $203–270K (n=52), level with AI Engineer; durable physical-systems work with high cost leverage |
| Inference / LLM Serving Engineer | 9 (64.4) | Systems pay premium "not validated" (T0-02); title volume is small (Rise 28); skill shares are not counted as title demand |
| AI Product Manager | 10 (63.5) | No AI-PM title count or pay data; keyword shares of PM postings are used only as an upper bound |
| Agentic AI Engineer | 12 (63.3) | Agentic skills appear in 59.3% of AI Engineer JDs, but that is a skill share, not title demand; the title has ~66 postings in 90 days |
| AI / GenAI Solutions Architect | 13 (61.6) | No AI-architect title count (only keyword shares of generic SA postings); no pay data |
| AI Evaluation Engineer | 14 (61.3) | The skill is broad (19% of postings) but the title is small; pay premium unverified |
| AI Governance Programme Lead / Manager | 16 (58.0) | Demand is real (1,997 US AI-governance postings Jan–Sep 2026, Axial, C), but measured pay is mid-range (IAPP medians $151.8–169.7K) and the route needs GRC experience |
| AI Security Engineer / AI Red Teamer | 19 (57.6) | ~23 title postings in 90 days (derived from 3 MCP-mentioning postings, so imprecise; band 3); no pay data, so the default pay prior applies |
| AI Enablement Engineer | 20 (55.0) | ~53 postings in 90 days; no pay data; the role may be transitional |
| VP / Head of AI; Chief AI Officer | L2 (60.5); L3 (54.3), separate board | Leadership tracks are not comparable with IC roles (§4); the corpus has no count or pay data for either |
| Speculative titles (Pre-Training, Vector Search, Voice, Edge SLM, Data Ops & RLHF, Mech Interp, AI Data Governance, Prompt & Context Optimization, Context Engineer, Cognitive Architect) | Not ranked | No posting evidence, or quarantined titles that cannot be scored honestly (§8) |

---

## 1. Method: Composite Career Index (CCI)

### 1.1 Design rules that keep bias out

1. **Anchors before scores.** Every pillar has a written 0–10 scale (§1.3), fixed before any role was scored.
2. **Evidence before opinion.**
   - Demand and Pay come from measured data wherever it exists (A–C).
   - The judgement pillars (Durability, Leverage) are labelled D and carry uniform uncertainty bands. For IC roles they stay within 3.5–8.5, which limits their influence.
3. **Like with like.** IC roles are ranked together. Leadership and independent tracks, which people reach after years of experience, are ranked separately (§4).
4. **No default persona.** Access blends the best of five backgrounds with their average (50/50) instead of assuming an experienced software engineer.
5. **Uncertainty is visible.** Each score has a [lo–hi] range, and the Monte Carlo turns those ranges into rank intervals.
6. **Weights are stress-tested.** Six weight profiles are run; a role counts as robust only if it stays near the top across them.
7. **Titles are not skills.** A skill's or keyword's share of postings never counts as demand for a title. At most it caps the upper end of a range.
8. **One pay instrument where possible.** Posted base from the same S09 corpus compares app, infra, platform and FDE roles. Levels.fyi TC is used where a title has it, and frontier-lab ladders mark the ceiling. Roles with no pay data get the same default prior (6.5), with a wide range, unless a documented proxy applies (Applied Scientist, Applied AI Engineer, AI Safety Researcher, Agentic AI Engineer). The leadership pay scores (VP / Head of AI 9, CAIO 8.5) are unanchored judgements.
9. **Reproducible.** One data file, one script, a fixed seed.

### 1.2 Pillars and weights

| Pillar | Base weight | Question it answers | Primary evidence |
|---|:---:|---|---|
| **Demand & liquidity** | 25 | Can you get hired, and switch employers, easily? | Live postings: JobsPipe, Fast AI Jobs, Skillenai, Axial (T0-01, T0-15, T0-16) |
| **Pay** | 25 | What does the role pay at senior level and at the reachable ceiling? | Levels.fyi TC, posted base (S09), visa-filing (LCA) base, IAPP/Axial (T0-02, T0-03, T0-15, T0-17) |
| **Durability** | 20 | Will the work keep its value as tools and AI coding agents improve? | D-004 skill tier, structural embedding and counter-evidence (judgement) |
| **Leverage** | 15 | How directly does the role move revenue, cost or risk? | Judgement anchored on cost, revenue and risk mechanisms |
| **Access** | 15 | How many backgrounds can reach it within about 12 months? | T0-06 R2 timelines and the T2-01 viability matrix (models) |

`CCI = Σ weight × score / 10`. A role scoring 10 on every pillar reaches 100.

### 1.3 Anchored scales (0–10)

**Demand:** best estimate of distinct live US postings for the title cluster. When one employer dominates the observed postings (D5 breadth test), 0.5 is deducted. Counts are live postings for title families (including non-GenAI variants), not openings: duplicates, mass posters and possible ghost postings inflate them (one vendor reports 9.5% of active postings visible for 45+ days) [B/C · T0-01].

| Score | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|
| Live postings | ≥1,500 | 1,000–1,499 | 600–999 | 300–599 | 150–299 | 50–149 (quorum) | 25–49 | 10–24 | 1–9 | ≈0 |

**Pay:** US total comp where available, otherwise posted base. Roles with no pay data in the corpus get a default prior of 6.5, the low end of the measured AI-engineering family scores (6.5–7), with a wide range and grade D, unless a documented proxy applies. Using the family median (6.75) instead would leave ranks 1–15 unchanged; Physical AI and AI Security would move above AI Governance and AI Safety (a near-tie at #16–#19), and AI Enablement would enter band B.

| Score | Senior-level typical | Reachable ceiling |
|---|---|---|
| 9–10 | ≥ $450K | ≥ $1M (frontier-lab ladders) |
| 8–8.5 | $300–450K | $500K–$1M |
| 7–7.5 | $220–300K | $300–500K |
| 6–6.5 | $160–220K | $250–350K |
| 5–5.5 | $120–170K | $200–270K |
| 3–4 | < $120K, or hourly/contract | < $200K |

**Durability** (judgement, ±1.5). This scores whether the *work* keeps its value; title instability is scored under Demand, not here.
- **8:** frontier-skill work (D-004 Tier 3: under 5% of postings) with structural embedding: research taste, physical systems or an adversarial domain.
- **6.5–7.5:** differentiating-skill work (D-004 Tier 2).
- **5–6:** work heavy on table-stakes skills, or likely to be transitional.
- **≤4:** bridge or gig work, or a collapsing title.

No session measures displacement of any ranked role by AI coding agents. The nearest evidence is occupation-level: Stanford's *Canaries in the Coal Mine?* (August 2026 version) finds employment of 22–25-year-olds in the most AI-exposed occupations 19% below trend, and its interpretation is contested [A for the figures · T0-06]. Nothing in the evidence supports calling any role "automation-proof".

**Leverage** (judgement, ±1):
- **8.5–9:** directly moves revenue (deployment, pre-sales, go-to-market) or a large cost line (GPU spend).
- **7–8:** core product, platform, research or risk enabler.
- **5–6.5:** indirect or internal impact.

**Access** (computed):
- Each IC role gets a 0–10 score for each of the five backgrounds (Appendix A.2):
  - ≥7.5 ≈ a T2-01 "●" corridor (about 6–8 months at 15–20 h/week);
  - 4–7 ≈ "◐" (plausible but extended);
  - <4 ≈ "○" (not plausible within 12 months).
- `Access = 0.5 × best background + 0.5 × average across the five backgrounds.`
- Leadership tracks use an explicit experience-gate score instead.

**India lens:**
- **Demand** uses live India postings: ≥300 → 10 · 150–299 → 8.5 · 75–149 → 7 · 30–74 → 5.5 · 10–29 → 4 · 1–9 → 2.5 · ≈0 → 1.
- **Pay** uses India TC anchors: P50 ≥ ₹60L → 9.5 · ₹40–60L → 8 · ₹25–40L → 6.5 · ₹15–25L → 5 · < ₹15L → 3, adjusted for the P90 ceiling.
- The inputs are in Appendix A.3.

### 1.4 Evidence confidence

| Label | Rule |
|---|---|
| **High** | Demand and Pay both rest on A/B evidence |
| **Medium** | The weaker of the two is C, or a model estimate built from B inputs (M) |
| **Low** | Either rests on judgement or a proxy (D). Expect these ranks to move when the role is measured |

**Placement exception.** EGP-1.0 keeps C and D claims out of summaries and tables of figures (T1-02 §10.3). A scoring document cannot follow that rule literally: Durability and Leverage are judgement pillars (D), so under the README rule every composite inherits D-level confidence. This catalog therefore grades every input in Appendix A, shows C/D items in summaries and tables only with their grade, and bases its recommendations (§0, §9) on A/B Demand and Pay evidence plus robustness across weight profiles. The top-two result holds under all six profiles, including Moat-first, which puts 40% on the Durability judgement.

### 1.5 Uncertainty, sensitivity and bands

- **Monte Carlo:** 20,000 draws, seed `20261102`. Each pillar is sampled from a triangular distribution over its [lo, mid, hi]. Reported as median rank (rounded half-up), P10–P90 rank interval and P(top 5).
- **Sensitivity:** six weight profiles:

  | Profile | Demand | Pay | Durability | Leverage | Access |
  |---|:---:|:---:|:---:|:---:|:---:|
  | Base | 25 | 25 | 20 | 15 | 15 |
  | Equal | 20 | 20 | 20 | 20 | 20 |
  | Pay-max | 15 | 40 | 20 | 10 | 15 |
  | Hiring-safety | 40 | 20 | 15 | 10 | 15 |
  | Moat-first | 15 | 20 | 40 | 10 | 15 |
  | Switcher | 25 | 15 | 15 | 10 | 35 |

- **Bands:** S ≥ 75 · A 65–75 · B 55–65 · C < 55. Bands use the unrounded CCI, so AI Enablement Engineer (54.95, displayed as 55.0) is band C.

### 1.6 Tie-break cascade

Ties are broken on unrounded CCI, then Demand, then Durability, then Pay, then name. CCI and lens values are rounded half-up, so equal displayed scores (for example the 57.9s at #17 and #18) are genuine near-ties.

### 1.7 What is ranked, and what is not

All 29 canonical roles are ranked: 24 IC roles on the main board and 5 leadership/independent tracks separately.

Not ranked (§8):
- quarantined titles, because there is no stable role to score;
- legacy titles;
- unmeasured buzzwords;
- candidate roles with no posting evidence.

Titles that do not exist as jobs, such as Cognitive Architect, get no scores at all.

### 1.8 Reproduce or re-weight

```bash
python3 scripts/rank_roles.py                     # prints every generated table, including Appendix A
python3 scripts/rank_roles.py --update            # rewrites the GENERATED blocks in this file in place
python3 scripts/rank_roles.py --markdown out.md   # writes the tables to a file
python3 scripts/rank_roles.py --json out.json     # ranks, intervals, P(#1/top-3/top-5), profiles, all lenses
```

After each recount, edit `data/role_scores.json` (scores, ranges, grades, basis text), then run `python3 scripts/rank_roles.py --update`. The script validates every range, including Access and India inputs, and rewrites the blocks between the `BEGIN/END GENERATED` markers in this file. The narrative (§0, the §2 band table, §3–§7 commentary and the hand-written tables) is written from that output, so re-read it after any change in ranks.

---

## 2. Master Leaderboard: IC Roles

<!-- BEGIN GENERATED: scripts/rank_roles.py (base leaderboard) -->
| Rank | Role | CCI /100 | Band | Demand | Pay | Durability | Leverage | Access | Evidence confidence | Monte Carlo rank (P10–P90) | P(top 5) |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Machine Learning Engineer | **77.9** | S | 9 | 8.5 | 7 | 7.5 | 6.0 | High | 1 (1–2) | 100% |
| 2 | AI Engineer | **76.9** | S | 10 | 6.75 | 6 | 7.5 | 7.9 | High | 2 (1–2) | 100% |
| 3 | Research Engineer / Member of Technical Staff | **71.4** | A | 5.5 | 9 | 7.5 | 8 | 5.4 | Medium | 3 (3–5) | 90% |
| 4 | Forward Deployed Engineer | **70.6** | A | 7.5 | 6.5 | 6.5 | 8.5 | 6.6 | Medium | 4 (3–6) | 79% |
| 5 | Applied AI Engineer | **68.0** | A | 5 | 7.5 | 6.5 | 8.5 | 7.3 | Low | 6 (4–9) | 40% |
| 6 | Research Scientist (AI/ML) | **67.8** | A | 5 | 9.5 | 8 | 7.5 | 2.9 | Medium | 7 (4–9) | 28% |
| 7 | Applied Scientist | **67.5** | A | 5 | 8 | 7.5 | 7.5 | 5.9 | Low | 6 (3–10) | 37% |
| 8 | AI Infrastructure / GPU Platform Engineer | **66.7** | A | 5.5 | 7 | 7.5 | 8.5 | 5.2 | Medium | 7 (5–11) | 17% |
| 9 | Inference / LLM Serving Engineer | **64.4** | B | 4 | 7.5 | 7.5 | 8.5 | 5.3 | Medium | 10 (7–13) | 3% |
| 10 | AI Product Manager | **63.5** | B | 6 | 6.5 | 6 | 8 | 5.5 | Low | 11 (7–15) | 4% |
| 11 | ML Platform / MLOps Engineer | **63.4** | B | 5.5 | 6.75 | 6.5 | 7.5 | 5.7 | Low | 11 (8–14) | 1% |
| 12 | Agentic AI Engineer | **63.3** | B | 4.5 | 6.75 | 6.5 | 7.5 | 7.3 | Low | 11 (8–14) | 0% |
| 13 | AI / GenAI Solutions Architect | **61.6** | B | 5 | 6.5 | 6 | 8.5 | 5.4 | Low | 14 (10–17) | 0% |
| 14 | AI Evaluation Engineer | **61.3** | B | 4 | 6.5 | 6.5 | 7.5 | 7.2 | Low | 14 (11–17) | 0% |
| 15 | GPU Kernel / ML Compiler Engineer | **59.8** | B | 4 | 7.5 | 6.5 | 8.5 | 3.6 | Medium | 15 (12–18) | 0% |
| 16 | AI Governance Programme Lead / Manager | **58.0** | B | 5.5 | 5.5 | 6.5 | 7 | 4.7 | Medium | 17 (14–20) | 0% |
| 17 | Physical AI / Robotics AI Engineer | **57.9** | B | 4.5 | 6.5 | 7 | 7 | 4.0 | Low | 18 (14–21) | 0% |
| 18 | Frontier AI Safety / Alignment Researcher | **57.9** | B | 3 | 7.5 | 8 | 7 | 3.4 | Low | 17 (13–21) | 0% |
| 19 | AI Security Engineer / AI Red Teamer | **57.6** | B | 3 | 6.5 | 7.5 | 8 | 4.6 | Low | 17 (14–20) | 0% |
| 20 | AI Enablement Engineer | **55.0** | C | 3.5 | 6.5 | 5 | 6.5 | 6.8 | Low | 21 (18–23) | 0% |
| 21 | AI Product Engineer (AI Frontend) | **54.5** | C | 3.5 | 6.5 | 5.5 | 6.5 | 5.8 | Low | 20 (17–23) | 0% |
| 22 | AI Risk, Audit & Compliance Specialist | **54.1** | C | 4.5 | 6 | 6 | 6.5 | 4.1 | Medium | 21 (19–23) | 0% |
| 23 | Responsible AI / AI Governance Engineer | **52.3** | C | 3 | 6 | 6 | 6.5 | 5.4 | Medium | 23 (20–23) | 0% |
| 24 | Domain Evaluation Specialist / AI Trainer | **46.2** | C | 5.5 | 3.5 | 3.5 | 5 | 6.1 | Low | 24 (24–24) | 0% |
<!-- END GENERATED -->

**How to read the board:**
- **CCI** is a decision aid built from graded evidence plus explicit judgement. It is not a measured fact.
- **The P10–P90 interval is the honest rank.** "6 (3–10)" for Applied Scientist means it could reasonably land anywhere from #3 to #10 once it is measured.
- **Pay 6.75 (AI Engineer) vs 8.5 (MLE)** reflects each title's market pay distribution. Like-for-like posted base differs much less ($200–275K vs $213–288K); about half the total-comp gap is employer mix.

| Band | Roles |
|---|---|
| **S (≥75)** | Machine Learning Engineer, AI Engineer |
| **A (65–75)** | Research Engineer/MTS, FDE, Applied AI Engineer, Research Scientist, Applied Scientist, AI Infrastructure Engineer |
| **B (55–65)** | Inference Engineer, AI Product Manager, ML Platform/MLOps, Agentic AI Engineer, AI Solutions Architect, AI Evaluation Engineer, GPU Kernel Engineer, AI Governance Lead, Physical AI Engineer, AI Safety Researcher, AI Security Engineer |
| **C (<55)** | AI Enablement Engineer, AI Product Engineer, AI Risk/Audit/Compliance, Responsible AI Engineer, Domain Evaluation Specialist |

---

## 3. Robustness: How Much Do the Weights Matter?

<!-- BEGIN GENERATED: scripts/rank_roles.py (sensitivity) -->
| Role | Base | Equal | Pay-max | Hiring-safety | Moat-first | Switcher | Best–worst |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Machine Learning Engineer | 1 | 2 | 1 | 2 | 1 | 2 | 1–2 |
| AI Engineer | 2 | 1 | 3 | 1 | 3 | 1 | 1–3 |
| Research Engineer / Member of Technical Staff | 3 | 4 | 2 | 4 | 2 | 5 | 2–5 |
| Forward Deployed Engineer | 4 | 3 | 7 | 3 | 6 | 3 | 3–7 |
| Applied AI Engineer | 5 | 5 | 6 | 5 | 8 | 4 | 4–8 |
| Research Scientist (AI/ML) | 6 | 8 | 4 | 8 | 4 | 15 | 4–15 |
| Applied Scientist | 7 | 6 | 5 | 6 | 5 | 7 | 5–7 |
| AI Infrastructure / GPU Platform Engineer | 8 | 7 | 8 | 7 | 7 | 9 | 7–9 |
| Inference / LLM Serving Engineer | 9 | 9 | 9 | 12 | 9 | 12 | 9–12 |
| AI Product Manager | 10 | 11 | 13 | 9 | 15 | 10 | 9–15 |
| ML Platform / MLOps Engineer | 11 | 12 | 11 | 10 | 11 | 11 | 10–12 |
| Agentic AI Engineer | 12 | 10 | 10 | 11 | 10 | 6 | 6–12 |
| AI / GenAI Solutions Architect | 13 | 14 | 16 | 13 | 16 | 13 | 13–16 |
| AI Evaluation Engineer | 14 | 13 | 12 | 14 | 13 | 8 | 8–14 |
| GPU Kernel / ML Compiler Engineer | 15 | 15 | 14 | 16 | 17 | 20 | 14–20 |
| AI Governance Programme Lead / Manager | 16 | 17 | 21 | 15 | 19 | 16 | 15–21 |
| Physical AI / Robotics AI Engineer | 17 | 18 | 18 | 17 | 18 | 19 | 17–19 |
| Frontier AI Safety / Alignment Researcher | 18 | 19 | 15 | 20 | 12 | 24 | 12–24 |
| AI Security Engineer / AI Red Teamer | 19 | 16 | 17 | 21 | 14 | 18 | 14–21 |
| AI Enablement Engineer | 20 | 20 | 19 | 19 | 23 | 14 | 14–23 |
| AI Product Engineer (AI Frontend) | 21 | 21 | 20 | 22 | 20 | 17 | 17–22 |
| AI Risk, Audit & Compliance Specialist | 22 | 22 | 22 | 18 | 21 | 23 | 18–23 |
| Responsible AI / AI Governance Engineer | 23 | 23 | 23 | 24 | 22 | 21 | 21–24 |
| Domain Evaluation Specialist / AI Trainer | 24 | 24 | 24 | 23 | 24 | 22 | 22–24 |
<!-- END GENERATED -->

- **Robust top three:**
  - MLE and AI Engineer stay between #1 and #3 under every profile.
  - Research Engineer/MTS stays between #2 and #5.
- **Near the top under every profile:** FDE (#3–#7), Applied AI Engineer (#4–#8), Applied Scientist (#5–#7) and AI Infrastructure (#7–#9).
- **The most weight-sensitive top-ten role is Research Scientist.** It is #4 when pay or moat dominates, but #15 for career switchers. On the full board only Frontier AI Safety Researcher swings more (#12 moat-first to #24 switcher).
- **The switcher profile lifts the easy-entry roles:** Agentic (#6), Evals (#8) and AI Enablement (#14). They are easier to enter but have smaller measured demand.
- **The #5–#8 band is a tie.** The Monte Carlo P10–P90 intervals overlap almost completely: Applied AI 4–9, Research Scientist 4–9, Applied Scientist 3–10, AI Infrastructure 5–11.

---

## 4. Leadership and Independent Tracks

<!-- BEGIN GENERATED: scripts/rank_roles.py (leadership) -->
| Rank | Role | CCI /100 | Demand | Pay | Durability | Leverage | Access | Evidence confidence |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| L1 | AI Engineering Manager / Director of AI Engineering | **62.0** | 5 | 7 | 7 | 8 | 4 | Low |
| L2 | VP / Head of AI | **60.5** | 3 | 9 | 7 | 9 | 2 | Low |
| L3 | Chief AI Officer (CAIO) | **54.3** | 2.5 | 8.5 | 5.5 | 9 | 1.5 | Low |
| L4 | Independent AI Consultant / Contractor | **44.3** | 4 | 4 | 5 | 6.5 | 3 | Low |
| L5 | Fractional Head of AI / Fractional CAIO | **38.8** | 2.5 | 4 | 4.5 | 7 | 2 | Medium |
<!-- END GENERATED -->

- **AI Engineering Manager / Director leads, but on thin evidence.** Its demand proxy ("lead or manager" labels on 5.6% of AI Engineer and 9.2% of MLE postings) mixes IC leads with managers. Its pay rests on one top-of-market data point: the median LCA base of $405K for Anthropic's MTS (Manager) positions. T0-02 rejects LCA wages as a pay anchor because they are floors.
- **VP / Head of AI and CAIO score high on pay and leverage**, but the corpus has no count or pay data for them. Their Pay scores (9 and 8.5) are unanchored judgements rather than the 6.5 default prior of §1.3 (low confidence), and the paths into them are long.
- **Independent consulting and fractional leadership are late-career, high-variance options, not entry routes.** The evidence:
  - Asks run $150–250/hr, but offers come in at 0.59–0.91× of asks.
  - Go Fractional labels CAIO demand "falling sharply", although its own CAIO post count rose from 6 to 10 in 90 days across two reads (326 profiles on the first read). T0-18 rates the demand evidence "conflicting" (C).
  - Modelled US net income has a median of $105K for practitioners who get traction; if 30–60% of entrants stall, the median falls to $39–87K (a model output, D · T0-18).
  - The UK GenAI contract day-rate median fell from £613–625/day (2024) to £550/day (2025, and the six months to 2026-10-20).

---

## 5. Lenses: The Best Job for *You*

### 5.1 Goal lenses (computed, not curated)

<!-- BEGIN GENERATED: scripts/rank_roles.py (goal lenses) -->
| Goal (profile) | #1 | #2 | #3 | #4 | #5 |
|---|---|---|---|---|---|
| Hiring-safety | AI Engineer (82) | Machine Learning Engineer (80) | Forward Deployed Engineer (71) | Research Engineer / Member of Technical Staff (67) | Applied AI Engineer (64) |
| Pay-max | Machine Learning Engineer (78) | Research Engineer / Member of Technical Staff (75) | AI Engineer (73) | Research Scientist (AI/ML) (73) | Applied Scientist (71) |
| Moat-first | Machine Learning Engineer (75) | Research Engineer / Member of Technical Staff (72) | AI Engineer (72) | Research Scientist (AI/ML) (70) | Applied Scientist (70) |
| Switcher | AI Engineer (79) | Machine Learning Engineer (74) | Forward Deployed Engineer (70) | Applied AI Engineer (68) | Research Engineer / Member of Technical Staff (65) |
| Equal | AI Engineer (76) | Machine Learning Engineer (76) | Forward Deployed Engineer (71) | Research Engineer / Member of Technical Staff (71) | Applied AI Engineer (70) |
<!-- END GENERATED -->

**Pay pillar alone (senior-typical pay and reachable ceiling), highest score first.** The Applied Scientist, Applied AI Engineer and AI Safety Researcher scores are proxies, not evidenced ceilings:

| Score | Role | Evidence |
|---|---|---|
| 9.5 | Research Scientist | Lab RS TC medians ~$1.25M (OpenAI, B) and $0.75–0.83M (Anthropic, C); Pave senior new-hire equity $4.1–4.7M (A) |
| 9 | Research Engineer / MTS | Lab TC medians ~$875–882.5K |
| 8.5 | Machine Learning Engineer | US P90 $497.5K; Meta E6 $782K |
| 8 | Applied Scientist | Proxy |
| 7.5 | Applied AI Engineer · AI Safety Researcher · GPU Kernel Engineer · Inference Engineer | Inference: typical posted base ~$270K, up to $485K at labs |

Two caveats apply:
- 49–72% of senior frontier-lab packages is semi-liquid stock. T0-17 models a 0.5–0.8× risk adjustment (T0-02's own discount model gives 0.64–0.88 for tender-backed lab stock); both are model outputs, and tenders are gated by tenure.
- AI/ML attrition of ~28% a year implies an expected vested fraction of 0.56 on a 4-year grant (0.71 at 17%) [B inputs; model output · T0-17].
- The systems/infra pay premium is "not validated" (T0-02).

### 5.2 Persona lenses (switcher weights; roles not plausible within 12 months are excluded)

<!-- BEGIN GENERATED: scripts/rank_roles.py (persona lenses) -->
| Persona | #1 | #2 | #3 | #4 | #5 | Next best |
|---|---|---|---|---|---|---|
| Backend / Systems SWE | AI Engineer (83) | Forward Deployed Engineer (73) | Machine Learning Engineer (73) | Applied AI Engineer (72) | AI Infrastructure / GPU Platform Engineer (69) | Agentic AI Engineer, ML Platform / MLOps Engineer |
| Data Scientist / BI | AI Engineer (78) | Machine Learning Engineer (78) | AI Evaluation Engineer (65) | Applied AI Engineer (65) | Forward Deployed Engineer (63) | Agentic AI Engineer, Applied Scientist |
| Frontend / Full-Stack | AI Engineer (80) | Forward Deployed Engineer (71) | Applied AI Engineer (65) | Agentic AI Engineer (63) | AI Evaluation Engineer (60) | AI Product Engineer (AI Frontend), AI / GenAI Solutions Architect |
| Non-Technical (5+ yrs domain) | AI Product Manager (65) | Forward Deployed Engineer (61) | AI Governance Programme Lead / Manager (60) | AI / GenAI Solutions Architect (56) | Domain Evaluation Specialist / AI Trainer (54) | AI Risk, Audit & Compliance Specialist, AI Enablement Engineer |
| PhD / Academic Researcher | Machine Learning Engineer (78) | AI Engineer (76) | Research Engineer / Member of Technical Staff (73) | Applied Scientist (71) | Applied AI Engineer (67) | Forward Deployed Engineer, AI Evaluation Engineer |
<!-- END GENERATED -->

- **Backend / Systems SWE:** AI Engineer is the fastest corridor (~6 months; high-volume at T1–T2). FDE, MLE and Applied AI Engineer come next. AI Infrastructure enters the top five on an inferred backend Access score (7, Grade D). T2-01's backend playbook targets Senior/Staff AI Inference Engineer or Applied AI Engineer roles; its Staff (T3) tier takes ~10–14 months with infrastructure depth (12–18 months in T2-01's own matrix).
- **Data Scientist / BI:** AI Engineer with an evals edge (~8 months from DS; ~11 from BI), or MLE. Evals is the natural specialisation, because error analysis and judge validation are data-science strengths.
- **Frontend / Full-Stack:** AI Engineer (full-stack) in ~7 months. T0-06 finds "AI Frontend" demand thin and Staff-skewed (C/D; the four postings it examined were all Staff-level), so apply as a "full-stack AI engineer".
- **Non-technical (5+ years in a domain):**
  - AI PM: ◐ (plausible but extended), ~7 months. One recruiter template asks for 4+ years as a PM plus a shipped model-powered feature; T2-01 asks for 5+ years in product/ops plus notebook-level Python.
  - "FDE" here means FDE-*adjacent* roles: ◐, ~10 months, and coding is required.
  - Governance: if you come from GRC, privacy or audit.
  - Domain evaluation: "weeks, if credentialed", but "a bridge, not a destination".
  - Engineering from zero code takes ~22 months.
- **PhD:** MLE and AI Engineer top the lens on demand. Research Engineer and Applied Scientist follow; they are T2-01's high-volume PhD corridors (~8 months). Research Engineer pays more at the top (Pay 9 vs MLE 8.5); Applied Scientist has no corpus pay data, and its proxy score (8) is below MLE's. Frontier research *science* is "not plannable".

### 5.3 India lens (India demand and pay replace the US inputs)

<!-- BEGIN GENERATED: scripts/rank_roles.py (India lens) -->
| India rank | Role | CCI (India) | India Demand | India Pay | Global rank | Monte Carlo rank (P10–P90) |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| 1 | AI Engineer | 73.8 | 10 | 5.5 | 2 | 1 (1–2) |
| 2 | Machine Learning Engineer | 71.7 | 7 | 8 | 1 | 2 (1–2) |
| 3 | Applied Scientist | 63.8 | 4 | 7.5 | 7 | 4 (3–8) |
| 4 | ML Platform / MLOps Engineer | 62.7 | 6.5 | 5.5 | 11 | 5 (3–9) |
| 5 | AI Product Manager | 62.3 | 5.5 | 6.5 | 10 | 6 (3–11) |
| 6 | Inference / LLM Serving Engineer | 60.6 | 3 | 7 | 9 | 8 (4–12) |
| 7 | AI Infrastructure / GPU Platform Engineer | 60.5 | 3.5 | 6.5 | 8 | 8 (4–13) |
| 8 | Agentic AI Engineer | 60.2 | 4.5 | 5.5 | 12 | 9 (5–13) |
| 9 | Research Engineer / Member of Technical Staff | 60.1 | 2 | 8 | 3 | 9 (5–14) |
| 10 | Forward Deployed Engineer | 59.3 | 4 | 5.5 | 4 | 10 (5–14) |
| 11 | Applied AI Engineer | 59.2 | 3 | 6 | 5 | 9 (5–14) |
| 12 | Research Scientist (AI/ML) | 59.0 | 2.5 | 8.5 | 6 | 12 (7–15) |
<!-- END GENERATED -->

- **AI Engineer leads in India** (#1 in 78% of Monte Carlo draws; MLE in 22%).
  - It has 398 live postings, and its aliases GenAI Engineer and GenAI Developer are the top GCC AI label according to Taggd (C · T0-01 D8); title-level GCC counts were not obtained.
  - JobsPipe's live counts put India at 0.23× the US (398 vs 1,697), but its September JD page implies 0.49× (13.6% vs 27.9% of postings). T0-01 flags this disagreement without reconciling it.
- **MLE pays more in India too, but has far fewer live postings (90).** Bengaluru TC: MLE P50 ₹44.5L, P90 ₹94.6L; AI Engineer P50 ₹21.4–24.5L, P90 ₹62.6L.
- **Applied Scientist ranks #3 in India on proxies alone** (low confidence): the corpus has no India count, and the pay proxy is Google Bengaluru MLE (L4 ₹65.2L, L5 ₹168.3L; small n). Expect this rank to move at the first India recount.
- **ML Platform/MLOps rises to #4:** MLOps Engineer is a common GCC title according to Taggd (C), and T0-01 relays a Quess estimate of 18–43% supply gaps in GCC AI/MLOps/platform clusters (C).
- **FDE drops to #10:** there is little India-based FDE demand evidence, and the US cluster was mostly non-remote in the August snapshot.
- **Research roles drop:** India accounts for 3.7% of all-field Research Scientist postings.
- **India pay is two populations.** The broad market centres on ₹10–15L (Glassdoor, Indeed, Payscale and AIM Research figures relayed by T0-02, mostly C); MNC, GCC and product firms pay far more. For Bengaluru senior SWEs on Levels.fyi (not AI-specific; n=4,836, a large-employer-skewed sample), the median is ₹56.0L and the five best-paying employers' senior medians are ₹1.06–1.22Cr (≈ the P90 of ₹1.07Cr) [B · T0-17].
- **AI titles are rarely remote.** JobsPipe JD measurements (2026-11-02) show remote shares of AI Engineer 11.0% and MLE 14.0%, against 31.6% for generic backend postings.
- **Independent contracting from India:**
  - Up to ₹75L (≈$79K), s.58 (old §44ADA) presumptive tax keeps ~83–84% of billing (67–73% under actual books), provided cash receipts are ≤5% of gross receipts; otherwise the ceiling is ₹50L.
  - Above the ceiling presumptive tax is not available: one rupee over ₹75L adds ~₹11.8L of tax, and it takes ~₹92–98L of billing to match the ₹75L take-home (the "dead zone"). At ₹1.2Cr about 65% is kept under actual books or a company.
  - India-based seniors are quoted $50–100/hr.
  - Not legal or tax advice.
- **GCC demand carries execution risk:** "nearly 70%" of India GCCs are stuck at AI pilots [A-/B · T0-09].
- **Most India-lens inputs are Grade C/D; treat this ranking as directional** (Appendix A.3).

---

## 6. Top-10 Dossiers

<a id="rank-1-ml-engineer"></a>
### #1 Machine Learning Engineer: CCI 77.9 · Band S · High confidence
`Demand 9 · Pay 8.5 · Durability 7 · Leverage 7.5 · Access 6.0 · Monte Carlo 1 (1–2)`
- **Why #1:**
  - The second-largest measured GenAI title (US 1,084; global 2,157), with the highest broad-market pay distribution (US TC P50 $280K, P90 $497.5K).
  - LLM is named in 45% of MLE postings (JobsPipe JD, 2026-11-02), so MLE is a core GenAI hiring channel, not "legacy ML".
- **Pay anchors:**
  - Big Tech: Meta E5 $458K, E6 $782K; Google L5 $393–445K, L6 $607–646K, L7 $743K.
  - Posted base: $213–288K. Bengaluru: P50 ₹44.5L, P90 ₹94.6L.
- **Best for:** PhDs, data scientists who can engineer, and backend engineers willing to add ML depth.
- **Interview track:** classic ML system design plus coding. Databricks MLE loops reportedly include LLM training systems and RAG over millions of documents [C · T0-14].
- **Watch:** in a study of 20 deployed systems, 70% used off-the-shelf models without fine-tuning. Differentiate on evals, serving and data-centric work, not fine-tuning alone. Mass posters (TikTok: 74 postings) inflate the count.
- **Could fall if** GenAI hiring shifts from MLE to AI Engineer titles at non-Big-Tech employers. No such shift is measured: from early August to 2026-10-20, AI-startup postings grew +18.5% for AI Engineer and +20.3% for ML Engineer [B · T0-01 F3]. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ml-engineer) · [Profile](role-catalog.md#profile-ml-engineer)

<a id="rank-2-ai-engineer"></a>
### #2 AI Engineer: CCI 76.9 · Band S · High confidence
`Demand 10 · Pay 6.75 · Durability 6 · Leverage 7.5 · Access 7.9 · Monte Carlo 2 (1–2)`
- **Why #2:**
  - The largest GenAI title family in the measured corpora (US 1,697; India 398; global 3,944; LinkedIn Jobs on the Rise #1). GenAI-specific volume is lower, because the family includes non-GenAI variants.
  - The shortest switch routes: backend ~6 months, frontend ~7, data scientist ~8.
- **Pay anchors:**
  - US TC P50 $154K, P90 $280K. The title mix is heavy with enterprise and services employers.
  - Posted base: AI Engineer (Application) $200–275K (n=55). Across all S09 AI-engineering postings, Senior $185–253K and Staff+/Principal $230–310K.
  - The AI premium over non-AI engineers rises to +18.7% at Staff.
- **Best for:** backend, frontend/full-stack and data-science engineers, and India-based engineers (GenAI Engineer/Developer is the top GCC label per Taggd, C).
- **Interview track:** application track: RAG with ACL enforcement, agent loop control, eval architecture, context management.
- **Watch:** wrapper-level work is commoditised. To stay at the top of the band, move into evals, agent reliability and cost/latency engineering.
- **Could rise if** pay data separates product-company AI engineers from services-firm titles. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-engineer) · [Profile](role-catalog.md#profile-ai-engineer)

<a id="rank-3-research-engineer"></a>
### #3 Research Engineer / Member of Technical Staff: CCI 71.4 · Band A · Medium confidence
`Demand 5.5 · Pay 9 · Durability 7.5 · Leverage 8 · Access 5.4 · Monte Carlo 3 (3–5)`
- **Why #3:**
  - The highest-paying engineering ladder with real hiring evidence. Lab TC medians are ~$875–882.5K; OpenAI L5 is $911K and Anthropic Staff $1.41M.
  - It absorbs post-training and RL work, a frontier-tier skill.
  - It is robust: it ranks between #2 and #5 under every weight profile.
- **Why not higher:**
  - Live volume is unmeasured. The proxy is 2025 LCA positions: OpenAI MTS-RE 84, Anthropic RE 63.
  - Access is narrow outside PhDs.
- **Pay caveat:** 49–72% of senior lab packages is stock; tenders are tenure-gated; risk-adjust to 0.5–0.8× (a T0-17 model output, C/D).
- **Routes:**
  - PhD: Tier 2 is a high-volume corridor (~8 months); Tier 3 takes 12–18 months.
  - Anthropic Fellows: no PhD required. Anthropic reports that >40% of the first cohort later joined it full-time 🏷️ (self-reported by the programme owner; B · T0-06, which discloses an Anthropic conflict of interest).
  - Strong OSS contributions (vLLM, SGLang). → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-research-engineer) · [Profile](role-catalog.md#profile-research-engineer)

<a id="rank-4-forward-deployed-engineer"></a>
### #4 Forward Deployed Engineer: CCI 70.6 · Band A · Medium confidence
`Demand 7.5 · Pay 6.5 · Durability 6.5 · Leverage 8.5 · Access 6.6 · Monte Carlo 4 (3–6)`
- **Why #4:**
  - The largest title family at AI startups: a 933-role cluster across 343 startups. Postings rose >1,000% year on year from a small base.
  - Joint-highest Leverage (8.5, a Grade D judgement shared with five other roles): each deployment is revenue.
  - Median advertised FDE pay is >$188K vs ~$145K for software engineers generally [B · T0-06].
- **Why not higher:**
  - Only ~48% of the cluster is engineer-titled (an extrapolation from the 50 newest rows, 2026-10-15 to 10-20).
  - Its ~20% growth from early August to 2026-10-20 matched AI Engineer (+18.5%) and ML Engineer (+20.3%).
  - Measured posted base ($180–248K) is the lowest of the measured families. Posted base excludes equity, and only 14% of AI-engineering postings mention equity.
  - T0-17 models a 0.4–0.8× risk adjustment for Series C–D AI-startup equity (0.15–0.3× for stale unicorns; seed/Series A is too assumption-sensitive to band), a model output (C/D). 38% of the FDE cluster is early-stage [B · T0-01 F3].
  - The work is mostly non-remote: only 65 of ~779 roles were remote in the August snapshot, and one JD lists up to 50% travel.
- **Best for:** backend or full-stack engineers who like customers, ambiguity and travel.
- **Interview track:** Databricks' AI-FDE loop covers RAG over sensitive, fast-changing documents and evaluating a multi-agent system [C · T0-14]. T1-03 files it under the application track.
- **Watch:** drift into non-coding pre-sales. Protect your production engineering scope. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-forward-deployed-engineer) · [Profile](role-catalog.md#profile-forward-deployed-engineer)

<a id="rank-5-applied-ai-engineer"></a>
### #5 Applied AI Engineer: CCI 68.0 · Band A · Low confidence
`Demand 5 · Pay 7.5 · Durability 6.5 · Leverage 8.5 · Access 7.3 · Monte Carlo 6 (4–9)`
Customer-facing LLM engineering at labs and vendors (OpenAI, Anthropic, Scale, Databricks); 16 of the 50 newest Fast AI Jobs AI-Engineer rows (2026-10-19) carry this title. Pay is unmeasured; the proxy is a lab-heavy employer mix. It suits backend engineers and PhDs, and is the bridge between AI Engineer and FDE. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-applied-ai-engineer) · [Profile](role-catalog.md#profile-applied-ai-engineer)

<a id="rank-6-research-scientist"></a>
### #6 Research Scientist (AI/ML): CCI 67.8 · Band A · Medium confidence
`Demand 5 · Pay 9.5 · Durability 8 · Leverage 7.5 · Access 2.9 · Monte Carlo 7 (4–9)`
It has the highest Pay score (9.5): lab RS TC medians of ~$1.25M at OpenAI (B, cached) and $0.75–0.83M at Anthropic (C), and Pave senior new-hire equity of $4.1–4.7M, more than double ML/AI Engineering (A). Level-specific RE/MTS packages reach higher (Anthropic Staff $1.41M). It shares the highest durability judgement (8) with AI Safety Researcher. But Access is only 2.9: it needs a PhD plus publications, and offers are "not plannable". It falls to #15 for career switchers. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-research-scientist) · [Profile](role-catalog.md#profile-research-scientist)

<a id="rank-7-applied-scientist"></a>
### #7 Applied Scientist: CCI 67.5 · Band A · Low confidence
`Demand 5 · Pay 8 · Durability 7.5 · Leverage 7.5 · Access 5.9 · Monte Carlo 6 (3–10)`
Big Tech's research-to-production title, and one of the PhD's two main high-volume corridors (~8 months). The corpus has no Big Tech count (startups: 14 at 12, June 2026) and no pay data, so it is scored by proxy (Big Tech MLE). An unverified "~700 postings" figure has no primary source. Of all the ranks, this is the most likely to move at the next recount. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-applied-scientist) · [Profile](role-catalog.md#profile-applied-scientist)

<a id="rank-8-ai-infrastructure-engineer"></a>
### #8 AI Infrastructure / GPU Platform Engineer: CCI 66.7 · Band A · Medium confidence
`Demand 5.5 · Pay 7 · Durability 7.5 · Leverage 8.5 · Access 5.2 · Monte Carlo 7 (5–11)`
Runs the compute estate. Posted base is $203–270K (n=52), level with AI Engineer; OpenAI GPU-infrastructure postings show $230–490K base (C). It is a good path for SRE, DevOps and backend infrastructure engineers, and is durable physical-systems work with high cost leverage. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-infrastructure-engineer) · [Profile](role-catalog.md#profile-ai-infrastructure-engineer)

<a id="rank-9-inference-engineer"></a>
### #9 Inference / LLM Serving Engineer: CCI 64.4 · Band B · Medium confidence
`Demand 4 · Pay 7.5 · Durability 7.5 · Leverage 8.5 · Access 5.3 · Monte Carlo 10 (7–13)`
- **For it:** high leverage on GPU spend (under-utilisation costs 2.5–24× at low load), and strong pay at labs and specialist vendors (typical JD base ~$270K, up to $485K).
- **Against it:** a small measured title volume (Rise 28), and a systems pay premium that is "not validated".
- Backend engineers can target Senior inference roles via T2-01's backend playbook. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-inference-engineer) · [Profile](role-catalog.md#profile-inference-engineer)

<a id="rank-10-ai-product-manager"></a>
### #10 AI Product Manager: CCI 63.5 · Band B · Low confidence
`Demand 6 · Pay 6.5 · Durability 6 · Leverage 8 · Access 5.5 · Monte Carlo 11 (7–15)`
The best non-engineering option globally (#1 for non-technical persons, #5 in India). The corpus has no AI-PM title count. About 970–1,820 US PM postings mention AI or agentic AI (derived from keyword shares, M); that keyword count caps the upper end of its demand range, because it does not count AI-PM titles. No pay data. → [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-product-manager) · [Profile](role-catalog.md#profile-ai-product-manager)

---

## 7. Roles 11–24 at a Glance

| Rank | Role | CCI | What holds it back | What would lift it | Best for |
|:---:|---|:---:|---|---|---|
| 11 | ML Platform / MLOps Engineer | 63.4 | No count; small pay sample (n=10) | A title-level count; GCC demand data | DevOps, SRE, backend; India GCCs (#4 in the India lens) |
| 12 | Agentic AI Engineer | 63.3 | Small title (~66 + 28 postings in 90 days); likely to stay a skill inside AI Engineer | Passing graduation tests 1–4 | Backend and distributed-systems engineers (#6 for switchers) |
| 13 | AI / GenAI Solutions Architect | 61.6 | No AI-architect title count; no pay data | A title-level count and pay data | Senior engineers, consultants, cloud architects |
| 14 | AI Evaluation Engineer | 61.3 | Small title; pay premium unverified | Evidence of dedicated eval teams and pay | DS, PhD and QA-minded engineers; *every* AI Engineer, as a skill |
| 15 | GPU Kernel / ML Compiler Engineer | 59.8 | Narrow access; DSLs and kernel agents abstract raw kernel work | Counts and pay-premium evidence | Systems/C++/CUDA engineers, PhDs |
| 16 | AI Governance Programme Lead | 58.0 | Mid pay ($152–170K medians); needs ~5 years in GRC | EU AI Act Annex III enforcement (Dec 2027) | GRC, privacy and audit professionals |
| 17 | Physical AI / Robotics AI Engineer | 57.9 | One employer dominates the observed postings | Breadth across employers | Robotics/controls engineers with ML |
| 18 | Frontier AI Safety Researcher | 57.9 | ~600 technical FTEs (single-author 2025 estimate, C · T0-15); no pay data | Continued ~21%/yr headcount growth (same estimate, C) | PhDs, fellowship alumni |
| 19 | AI Security Engineer / AI Red Teamer | 57.6 | Small title (~23 postings in 90 days, derived from 3 MCP mentions); no pay data | Growth of dedicated AI-security teams | Application-security engineers |
| 20 | AI Enablement Engineer | 55.0 | Small title; may be transitional | Durable internal-platform mandates | Backend/DevEx engineers; ops leads |
| 21 | AI Product Engineer (AI Frontend) | 54.5 | Thin, Staff-skewed demand | Agent-UX roles scaling | Frontend engineers (apply as "full-stack AI engineer") |
| 22 | AI Risk, Audit & Compliance Specialist | 54.1 | A specialisation inside other careers; credential gates | Enforcement (LL144, EU AI Act, DPDP) | Auditors, model-risk professionals |
| 23 | Responsible AI / AI Governance Engineer | 52.3 | Thin niche ("few openings") | Harmonised standards; Annex III | MLOps and security engineers in regulated firms |
| 24 | Domain Evaluation Specialist / AI Trainer | 46.2 | Contract work; low durability | Long-term in-house eval-lead roles | Credentialed domain experts, as a bridge into AI |

---

## 8. Not Ranked

| Title | Why not ranked | Where the work maps |
|---|---|---|
| Context Engineer (and its variants) | Quarantined: ~10–25 live globally (an estimate, C · T0-01 F5), three incompatible archetypes | Skill tag "context/retrieval design" inside AI Engineer |
| Cognitive Architect, Prompt Wizard, Agent Architect (exact), Context Harness Engineer, Principal Agentic Context Engineer, Vibe Engineer | Quarantined (T0-01 D4; Vibe Engineer was never searched) | — |
| Prompt Engineer | Legacy: 0.35% of LinkedIn AI postings (2025 arXiv study) | AI Engineer |
| AI Whisperer, Neural Network Designer, Transformer Specialist, Foundation Model Engineer, Reasoning Engineer | Never searched (unmeasured) | — |
| Voice AI Engineer, On-Device/Edge AI Engineer, Retrieval/Vector Search Engineer, AI DevRel, AI TPM | Candidate roles with no title-level count | Measure at the next recount |
| Foundation Model Pre-Training Engineer; Data Ops & RLHF Lead; Mechanistic Interpretability Researcher; AI Data Governance & Privacy Architect | Unsourced labels [P] with no posting evidence | Research Engineer / AI Infrastructure; Domain Evaluation Specialist; AI Safety Researcher; AI Risk & Audit |

> [!CAUTION]
> Don't use a quarantined or legacy title as your résumé headline. Use the canonical title and show the work as skills in your project bullets (adapted from T0-01 Recommendation 5, which advises employers; T0-11).

---

## 9. Strategic Takeaways

Each claim carries its evidence grade. EGP-1.0 (T1-02 §10.3–10.4, rule C4) admits only A/B claims as grounds for a recommendation, so every takeaway below rests on A/B evidence; C and C/D items are attributed context, not the basis of the advice.

1. **Target a canonical title and build differentiating skills on top of it.** AI Engineer and MLE are the two robust best bets (composite, Grade M):
   - **MLE** if you have, or will build, ML depth and want Big-Tech-style pay.
   - **AI Engineer** for the most live postings and the fastest entry.
   - If you have a PhD or can win a fellowship, **Research Engineer/MTS** is the highest-paying robust alternative.
2. **Make evaluation your edge in any role.** Evals appear in 19% of S09 postings and at 68% of companies [B · T0-03]. In a vendor-run LangChain survey (n=1,340), only 52.4% of agent teams ran offline evals [B/C · T0-03]. That adoption gap is the opportunity.
3. **Employer tier drives pay more than the app-vs-infra split.** Median posted base ranges are nearly identical across the AI Engineer, infrastructure/platform and ML Engineer families ($200–288K), with FDE lower at $180–248K; top-of-band pay concentrates at labs and specialist vendors [B · T0-03 KF1, §6.1.2]. Choose employers deliberately.
4. **Discount frontier-lab paper wealth.** 49–72% of senior lab packages is stock [B · T0-02]. T0-17 models a 0.5–0.8× risk adjustment for frontier-lab equity, and tenders are tenure-gated and capped [C/D · T0-17].
5. **FDE is a large cluster that grew fast from a small base, but it is not the pay leader.** Postings rose >1,000% Jan–Aug 2026 vs 2025 [B · T0-06], then ~20% from early August to 2026-10-20, in line with AI and ML Engineer [B · T0-01 F3]. It has the lowest posted-base median among the measured families [B · T0-03] and was mostly non-remote in the August snapshot [B · T0-01].
6. **Levelling up pays more than hopping sideways.**
   - On Levels.fyi, each level step from Entry to Staff is worth ×1.38–1.46 in median TC (Staff to Principal ×1.21), and the AI premium rises from +6.2% at Entry to +18.7% at Staff [B · T0-17].
   - T0-17 estimates a same-tier hop at about +15–25% [C].
7. **In India:**
   - AI Engineer (GenAI Engineer) is the volume play [B · T0-01].
   - MLE and top product/GCC employers are the pay play [B · T0-02, T0-17].
   - T0-01 relays a Quess estimate of 18–43% supply gaps in GCC AI/MLOps/platform clusters [C].
8. **Lead with referrals.** Referrals convert at 11–36× the per-application rate of cold applications, an association with selection effects rather than a causal estimate; cold inbound converts at ≈0.2% application-to-hire [B · T0-04].

---

## 10. Review Record

### 10.1 Claims Checked and Rejected

These claims were checked against the corpus while the index was built.

| Claim | Finding | Outcome |
|---|---|---|
| Agentic AI Engineer demand inferred from the 59.3% agentic skill share | A skill is not a title | Title evidence only (design rule 7) |
| Inference "prime comp differentiator"; "pays their salary in 3 weeks"; "SWE agents cannot optimize CUDA kernels" | Unsupported or contradicted: the premium is not validated (T0-02); kernel DSLs and agents counter the moat claim (T0-03) | Rejected |
| GPU cluster work "100% automation proof"; "99.5%+ MTBF" | Unsupported; MTBF is a duration | Rejected |
| FDE "~48% write production code daily"; "immune to automation"; contractors "retain up to 78%" | Misread (48% of postings are engineer-*titled*); unsupported; contradicted (83–84% below ₹75L, ~65% at ₹1.2Cr) | Corrected reading used |
| AI Engineer has the "highest callback rate in the market" | No role-level funnel data exists (T0-04) | Rejected |
| "<1% hallucination … out-competes 95% of applicants" | Unsupported; T0-13 calls this "benchmark-number theater" | Rejected |
| "The EU AI Act requires legal human liability" | Contradicted: the Act names no required officer (T0-15) | Rejected |
| GPU and inference roles have the highest pay ceilings | Contradicted: research and MTS ladders pay the most | Computed pay ceiling (§5.1) |

### 10.2 Adversarial Review of the Scoring Inputs

An adversarial review on 2026-11-03 changed these scoring inputs before publication; the value before each arrow is the pre-review score.

| Change | Reason |
|---|---|
| AI PM demand 7 → 6 (D); AI Solutions Architect demand 6.5 → 5 (D) | Keyword shares of generic PM/SA postings had been counted as title demand (design rule 7); in the calibrated index they only cap the range |
| Inference demand 5 → 4; pay 8 → 7.5 (C) | Rise 28 is band 4, and the concept-share uplift broke rule 7. Typical JD base (~$270K) is band 7–7.5 |
| GPU Kernel pay 8 → 7.5 (C); AI Infrastructure pay 7.5 → 7 (C); ML Platform pay 7 → 6.75 | One pay instrument: posted base for these families is level with AI Engineer |
| Default pay prior 6.5 for AI PM, AI Security, AI SA, AI Enablement, AI Evaluation, Physical AI; Agentic pay = AI Engineer's (6.75) | Unmeasured roles had been scored above measured comparables with no proxy |
| AI Security demand 4 → 3 | ~23 postings in 90 days is band 3; the AI share of generic security postings is unmeasured |
| Applied Scientist demand 6 → 5 (range 3–8) | The only count is 14 (startups); Big Tech volume is unmeasured |
| FDE demand 8 → 7.5 (M, Medium confidence) | The engineer-titled share is an extrapolation |
| Agentic durability 5.5 → 6.5 | Title instability is scored only under Demand (no double penalty) |
| Leverage 8.5 for Applied AI, AI SA, AI Infrastructure and GPU Kernel | The 8.5–9 anchor (revenue or GPU-spend lines) is applied uniformly across infrastructure roles |
| Persona corrections: RE (PhD) 6 → 7.5; Inference and AI Infra (backend) → 7; AI Product Engineer (frontend) 9 → 7; Domain Eval (non-technical) 8.5 → 7; AI Evaluation Engineer (non-technical) 5 → 3; Applied AI (PhD) 7.5 → 7 | Aligned with the T2-01 matrix (●/◐/○) and T0-06 routes |
| Leadership: EM demand and pay to grade D; consultant and fractional pay 5 → 4; CAIO pay range widened | Thin proxies; the hourly/contract pay anchor applies |
| The ranking generator reproduces Appendix A and all lens results with verified ranges and rounding (`--update`) | Every generated figure comes from the script, not from hand edits |
| Narrative audit (51 findings): over-claims corrected (for example "largest GenAI title anywhere" and "highest pay ceiling of any role"), C-grade claims attributed, model outputs labelled, relative-time words removed, dossier band letters relabelled so they cannot be read as evidence grades, and an EGP placement exception stated (§1.4) | Accuracy and EGP-1.0 compliance |

---

## Appendix A: Scoring Inputs

<!-- BEGIN GENERATED: scripts/rank_roles.py (Appendix A) -->
### A.1 Score justification ledger

Format: `mid [lo–hi] · grade`. Durability and Leverage are labelled judgements (Grade D) with uniform ±1.5 / ±1.0 bands. Access is computed from A.2.

<a id="ledger-ml-engineer"></a>
**#1 · Machine Learning Engineer** (`ml-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 9 [8–9.5] · B | JobsPipe US 1,084, global 2,157, India 90; Fast AI Jobs 273 at 159 startups [T0-01 F1, D2]; LLM named in 45.0% of MLE postings (JobsPipe JD, 2026-11-02). Includes recsys/ads/AV and mass posters (TikTok 74). |
| Pay | 8.5 [7.5–9] · B | Levels.fyi US TC P50 $280K / P75 $385.5K / P90 $497.5K (n=1,063) [T0-02:67]; Meta E5 $458K, E6 $782K; Google L5 $393-445K, L6 $607-646K [T0-02:232-235]; posted base $213-288K (n=201) [T0-03 6.1.2]. |
| Durability | 7 [5.5–8.5] · D | Judgement. Decades-stable title with deep-learning depth; offset: 70% of production apps use off-the-shelf models without SFT/RL [T0-03 S31]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Owns models behind ranking, recsys, fraud and fine-tuned systems. |
| Access | 6.0 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-engineer"></a>
**#2 · AI Engineer** (`ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 10 [9–10] · B | JobsPipe US 1,697 live (corpus 2026-10-19; page unchanged 2026-11-02), India 398, global 3,944; Fast AI Jobs 326 at 183 AI startups; LinkedIn Jobs on the Rise 2026 #1. Family count includes non-GenAI variants (robotics, construction, Power Platform) [T0-01 F1, F2]. |
| Pay | 6.75 [6–7.5] · B | Levels.fyi US TC P50 $154K / P75 $212.5K / P90 $280K (n=335) [T0-02:67]; posted base AI Engineer (Application) $200-275K (n=55); across all S09 AI-engineering postings, Senior $185-253K (n=462) and Staff+ $230-310K (n=322) [T0-03 6.1.2]. The title earns ~0.55x the ML Engineer title; about half of that gap is employer mix, and within Google the MLE title still earns 26-39% more [T0-02:67, 480]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Title persists and leads growth, but the table-stakes layer (SDK calls, naive RAG, prompting) is commoditised [T0-03 6.4 Tier 1]; evals, agent reliability and cost engineering keep value [T0-03 Tier 2]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Ships the revenue-facing AI features; enterprise and services employer mix [T0-01 F2]. |
| Access | 7.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-research-engineer"></a>
**#3 · Research Engineer / Member of Technical Staff** (`research-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–7] · C | Live count unmeasured [T0-01 D2 row 11]. 2025 LCA filings: OpenAI MTS-Research Engineer 84, MTS-SWE 107, MTS-AI Systems 67 positions; Anthropic Research Engineer 63, MTS 223 [T0-02:303-316]. Filings are not live postings. |
| Pay | 9 [8–10] · B | OpenAI SWE/MTS TC median $875K (n=242); Anthropic $882.5K (n=49) [T0-02:73]; OpenAI MTS-RE LCA base median $335K [T0-02:310]; stock is 49-72% of senior lab packages (OpenAI L4-L5 59-60%, Anthropic Senior 49%, Lead/Staff 61-72%) [T0-02:561]; risk-adjust 0.5-0.8x [T0-17 R3]. |
| Durability | 7.5 [6–9] · D | Judgement. Frontier skills (distributed training, post-training/RL infra) [T0-03 6.4 Tier 3]. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-forward-deployed-engineer"></a>
**#4 · Forward Deployed Engineer** (`forward-deployed-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 7.5 [6.5–8.5] · M | Fast AI Jobs: 933 FDE-cluster roles at 343 AI startups (2026-10-20); ~48% of the newest 50 rows are engineer-titled, so ~450 engineering roles (an extrapolation) [T0-01 F3]. Growth of ~20% since early Aug was in line with AI Engineer (+18.5%) and ML Engineer (+20.3%). FDE postings up >1,000% Jan-Aug 2026 vs 2025 from a small base [T0-06:175]; 304 base-disclosing FDE postings in S09 [T0-03 6.1.2]. No broad-market count. |
| Pay | 6.5 [5.5–7.5] · B | Posted base $180-248K (n=304), the lowest family median in S09 [T0-03:230]; median advertised >$188K vs ~$145K for SWEs [T0-06:175]; Series C-D startup equity risk-adjusted 0.4-0.8x (model) [T0-17 R3]; 38% of the cluster is early-stage [T0-01 F3]. |
| Durability | 6.5 [5–8] · D | Judgement. Customer embedding and integration judgement; risk of drift into non-coding roles (about half the cluster is non-engineering) [T0-01 F3]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Converts deployments directly into revenue and retention. |
| Access | 6.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-applied-ai-engineer"></a>
**#5 · Applied AI Engineer** (`applied-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [4–6.5] · C | 16 of the newest 50 Fast AI Jobs AI-Engineer rows (2026-10-19), ~100 of 326 if representative (unverified extrapolation) [T0-01 D2 row 4]; OpenAI, Anthropic, Scale, Databricks titles [T0-01 D7]. |
| Pay | 7.5 [6–9] · D | No role-specific pay in corpus; employer mix spans frontier labs (OpenAI/Anthropic SWE TC medians $875K-$882.5K) [T0-02:73] and enterprise vendors. |
| Durability | 6.5 [5–8] · D | Judgement. Customer-facing technical delivery at labs and vendors. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Customer deployment and go-to-market at labs and vendors (8.5-9 anchor: directly moves revenue). |
| Access | 7.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-research-scientist"></a>
**#6 · Research Scientist (AI/ML)** (`research-scientist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [4–6.5] · C | AI-specific count unmeasured; OpenAI MTS-Research Scientist 68 LCA positions (2025) [T0-02:312]; JobsPipe research-scientist JD (all fields): LLM in 24.4%, RL 17.1%, US 65% (2026-11-02). |
| Pay | 9.5 [8.5–10] · B | OpenAI Research Scientist TC ~$1.25M (cached, B); Anthropic $0.75-0.83M (C) [T0-02:73]; Pave AI research scientist median new-hire equity $4.09M (P6) / $4.72M (M6) (A) [T0-02:75]. |
| Durability | 8 [6.5–9.5] · D | Judgement. Research taste and novel methods. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Long-horizon capability gains. |
| Access | 2.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-applied-scientist"></a>
**#7 · Applied Scientist** (`applied-scientist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [3–8] · D | Only count: 14 at 12 AI startups (Fast AI Jobs, 2026-06-09) = band 3 [T0-01 D2 row 12]. Big Tech, the title's main market, is unmeasured in the corpus. The '~700' in T1-01:80 / FAD 5.1 has no primary source. Mid set between the startup band and plausible Big Tech volume; wide range. |
| Pay | 8 [6.5–9] · D | No corpus pay. Big Tech title; ML Engineer at Big Tech as proxy (Meta E5 $458K, Google L5 $393-445K) [T0-02:234]. |
| Durability | 7.5 [6–9] · D | Judgement. Research-to-production scientists at large firms. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. |
| Access | 5.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-infrastructure-engineer"></a>
**#8 · AI Infrastructure / GPU Platform Engineer** (`ai-infrastructure-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4–7] · C | 52 base-disclosing 'Infrastructure/Platform Engineer (GPU clusters, inference platforms)' postings in S09 [T0-03:228]; distributed systems in 19.1% of S09 postings [T0-03 6.3]; OpenAI GPU-infrastructure postings [T0-17:182]. |
| Pay | 7 [6–8] · C | Posted base $203-270K (n=52), nearly identical to AI Engineer (Application) $200-275K [T0-03 6.1.2]; ceiling evidence is C: OpenAI GPU-infrastructure base ranges $230-490K [T0-17:182]. |
| Durability | 7.5 [6–9] · D | Judgement. Physical fleets, networking and reliability; distributed-systems minimum in top-band JDs [T0-03 J1]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Capacity, uptime and cost of the GPU estate (8.5-9 anchor: large cost line). |
| Access | 5.2 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-inference-engineer"></a>
**#9 · Inference / LLM Serving Engineer** (`inference-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [3–5.5] · C | Rise 'inference engineer' 28 (small corpus) = band 4 [T0-01 D2 row 9]; >=8 named JDs at Anthropic, NVIDIA, Together AI, Baseten, Inferact plus RadixArk and Red Hat [T0-03 6.2, T0-05]. The 14.8% inference-optimisation concept share is a skill mention and is not used (rule 7). |
| Pay | 7.5 [6.5–8.5] · C | Typical posted base across 8 named JDs is ~$270K (range $150-485K; Anthropic $320-485K at the top) [T0-03 6.2]; S09 puts inference platforms in the Infra/Platform family ($203-270K); systems/research-engineering titles +13-31% base in two datasets, 'not validated' [T0-02:480]. |
| Durability | 7.5 [6–9] · D | Judgement. Serving economics (2.5-24x under-utilisation penalty at 1-10 req/s) [T0-03 KF10]; tripwire: a large closed-model price drop narrows self-hosting [T0-03 4.5]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Direct GPU-cost and latency leverage. |
| Access | 5.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-product-manager"></a>
**#10 · AI Product Manager** (`ai-product-manager`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 6 [4.5–8] · D | No AI-PM title count in the corpus. Upper bound only: JobsPipe Product Manager US 6,289 live (2026-11-02); 'artificial-intelligence' named in 15.4% and 'agentic-ai' in 13.6% of PM postings, i.e. ≥~970 (≤~1,820) AI-mentioning PM postings. These are keyword shares, not titles (rule 7). PM = 8.0% of 1,747 MCP postings [T0-16:392]. |
| Pay | 6.5 [5–8] · D | No AI-PM pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 6 [4.5–7.5] · D | Judgement. Product judgement for probabilistic systems. |
| Leverage | 8 [7–9] · D | Judgement. Decides what gets built and how it is measured. |
| Access | 5.5 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ml-platform-engineer"></a>
**#11 · ML Platform / MLOps Engineer** (`ml-platform-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–7] · D | No posting count: 'probable, count missing' [T0-01 D2 row 8]; India GCC AI/MLOps/platform supply gap 18-43% (Quess, C) [T0-01 F10]; 10 base-disclosing MLOps postings in S09 [T0-03:229]. |
| Pay | 6.75 [5.75–7.75] · C | MLOps/ML Platform posted base $186-277K (n=10, small) [T0-03:229], in line with AI Engineer; Bengaluru MLOps P50 Rs23.6L, P90 Rs63.5L (C) [T0-02:147]. |
| Durability | 6.5 [5–8] · D | Judgement. Platform need persists; LLMOps absorbed; fast tool churn (TGI archived, Triton renamed Dynamo Triton) [T0-03 KF6]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. |
| Access | 5.7 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-agentic-ai-engineer"></a>
**#12 · Agentic AI Engineer** (`agentic-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3.5–5.5] · C | Skillenai 90-day window: ~66 Agentic AI Engineer (derived) + 28 Agent Engineer postings [T0-16:389-390]; ~5 of newest 50 AI rows [T0-01 D2 row 5]. Agentic AI as a skill is in 59.3% of AI Engineer postings (a skill tag, not a title). |
| Pay | 6.75 [6–7.5] · D | No title-specific pay; scored as an AI Engineer variant (same pay score). |
| Durability | 6.5 [5–8] · D | Judgement. The work (durable runtimes, tool gateways, sandboxing) is a Tier-2 differentiating skill [T0-03 6.4]; title instability is handled under Demand, not Durability. Framework churn (AutoGen dormant) [T0-03 KF9]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Workflow automation value. |
| Access | 7.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-solutions-architect"></a>
**#13 · AI / GenAI Solutions Architect** (`ai-solutions-architect`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [3.5–6.5] · D | Title-level count not measured: 'AI / Agentic / GenAI Architect: not measured; 6+ distinct postings seen; probable, services-concentrated' [T0-01 D2 row 13]. Upper bound only: JobsPipe Solutions Architect US 1,515 live (2026-11-02), of which ≥23.2% (~350) name AI and 17.1% generative AI. These are keyword shares, not AI-architect titles (rule 7). |
| Pay | 6.5 [5–7.5] · D | No pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 6 [4.5–7.5] · D | Judgement. Enterprise integration and vendor ecosystems. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Pre-sales and enterprise architecture (8.5-9 anchor: directly moves revenue). |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-evaluation-engineer"></a>
**#14 · AI Evaluation Engineer** (`ai-evaluation-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [3–5] · C | Rise 'LLM evaluation' 26 (keyword) [T0-01 D2 row 14]; named postings at Haparz, Backbase (Hyderabad), deeprec, Artificial Analysis, FurtherAI [T0-03 J12, T0-09:421-422, T0-05:326]. As a skill, evals appear in 19.0% of S09 postings (68.2% of companies) and 59.7% of AI-first roles [T0-03 6.3, T0-13:94]. |
| Pay | 6.5 [5–7.5] · D | Pay premium for pure eval roles unverified [T0-03:L556, L583]. No pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 6.5 [5–8] · D | Judgement. Adoption gap (52.4% offline / 37.3% online evals among agent teams) [T0-03 KF4] vs risk that evals stay a skill inside AI Engineer. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Release gating and quality. |
| Access | 7.2 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-gpu-kernel-engineer"></a>
**#15 · GPU Kernel / ML Compiler Engineer** (`gpu-kernel-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [3–5.5] · C | CUDA/GPU kernels named in 6.6% of S09 postings (29.3% of companies) [T0-03 6.3]; River AI (GPU kernels) and AMD (Triton kernels) among T0-13's inference/kernel postings [T0-13:112, 737]. |
| Pay | 7.5 [6.5–8.5] · C | Inference-titled JDs with kernel requirements: NVIDIA DL SWE $152-356.5K base (midpoints ~$220-270K); Anthropic inference runtime $405-485K [T0-03 6.2]. Three postings, so Grade C. |
| Durability | 6.5 [5–8] · D | Judgement. Frontier scarcity vs counter-evidence: tile DSLs (Helion, CuteDSL, CUDA Tile) and automated kernel agents abstract kernel writing [T0-03:L542, L101]; no labour data either way [T0-03:L571]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. GPU efficiency moves a large cost line (8.5-9 anchor). |
| Access | 3.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-governance-lead"></a>
**#16 · AI Governance Programme Lead / Manager** (`ai-governance-lead`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–6.5] · C | Axial: 1,997 US AI-governance postings Jan-Sep 2026 (~2,700/yr; ~51/week by arithmetic, while Axial quotes ~71) [T0-15:91]; programme-owner class is 6 of 13 sampled JDs; 56% at 10,000+ staff firms; 73% senior+ [T0-15:110, 152, 260]. |
| Pay | 5.5 [4.5–6.5] · B | Axial median $169K; Axial reports top-of-range figures, so typical offers are lower (C) [T0-15:162]; IAPP medians $151.8K (AI governance only), $169.7K (with privacy) (B) [T0-15:130]; manager $244K, director $268K (tops of ranges) [T0-15:417]. |
| Durability | 6.5 [5–8] · D | Judgement. Driven by sector regulators and the EU AI Act; dates moved once; NIST AI RMF voluntary [T0-15:138]. |
| Leverage | 7 [6–8] · D | Judgement. Regulatory exposure (e.g., EU AI Act Art. 101 fines for GPAI providers of up to EUR 15m or 3%) [T0-15:233]. |
| Access | 4.7 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-physical-ai-engineer"></a>
**#17 · Physical AI / Robotics AI Engineer** (`physical-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3–5.5] · C | 8 of the newest 50 AI-Engineer rows were Figure AI 'Helix AI Engineer' (~50 of 326 if representative = band 5) [T0-01 F2]; minus 0.5 for single-employer concentration (D5 breadth test). JobsPipe US sample includes 'Physical AI Engineer'. |
| Pay | 6.5 [5–8] · D | No pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 7 [5.5–8.5] · D | Judgement. Physical-world systems. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 4.0 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-safety-researcher"></a>
**#18 · Frontier AI Safety / Alignment Researcher** (`ai-safety-researcher`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4] · C | ~600 technical FTEs across 67 organisations (single-author 2025 estimate), growing ~21% a year [T0-15:122, 380]. |
| Pay | 7.5 [5–10] · D | No pay or volume figures for this market [T0-15:380]; lab-employed researchers sit on RS/RE ladders, many organisations are non-profits. |
| Durability | 8 [6.5–9.5] · D | Judgement. Growing research field. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 3.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-security-engineer"></a>
**#19 · AI Security Engineer / AI Red Teamer** (`ai-security-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4.5] · C | ~23 'AI Security Specialist' postings in 90 days (Skillenai; derived from 13.0% = 3 MCP mentions) [T0-16:393], i.e. about band 3 live. The AI share of 2,827 generic US Security Engineer postings is unmeasured and not used (rule 7). |
| Pay | 6.5 [5–8] · D | No pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 7.5 [6–9] · D | Judgement. Adversarial and growing surface: CVSS 9.8 serving-engine CVEs, MCP CVEs, Braintrust key breach, OWASP LLM/Agentic Top 10 [T0-03 KF12, T0-16 8, T0-14 6.8]. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 4.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-enablement-engineer"></a>
**#20 · AI Enablement Engineer** (`ai-enablement-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3.5 [2.5–4.5] · C | ~53 postings in 90 days (Skillenai; derived from 30.2% = 16 MCP-mentioning postings) [T0-16:393]. |
| Pay | 6.5 [5–7.5] · D | No pay data in corpus. Default prior: 6.5, the low end of the measured AI-engineering family pay scores (6.5-7), with a wide range. |
| Durability | 5 [3.5–6.5] · D | Judgement. Internal adoption roles may be transitional. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. Internal productivity. |
| Access | 6.8 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-product-engineer"></a>
**#21 · AI Product Engineer (AI Frontend)** (`ai-product-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3.5 [2.5–5] · C | AI-frontend demand 'thin and senior-skewed' [T0-06:97, 158]; Productboard, Artisan and one recruiter-listed Staff AI Frontend posting [T0-06:167]. |
| Pay | 6.5 [5.5–7.5] · D | One Staff AI Frontend posting at $250-315K (C/D) [T0-06:167]; otherwise AI-Engineer-like. |
| Durability | 5.5 [4–7] · D | Judgement. Agent UX is differentiated; generic UI work is exposed to code generation. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 5.8 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-risk-assurance-specialist"></a>
**#22 · AI Risk, Audit & Compliance Specialist** (`ai-risk-assurance-specialist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3.5–5.5] · C | Specialisations inside audit, model-risk and privacy teams [T0-15:153-155]; Deloitte AI Risk & Validation listing seen 16 times; 41 of 50 large banks had dedicated AI-governance staff at end-2024, with 247 responsible-AI staff across all 50 (~4.9 per bank); NYC LL144: 18 of 391 employers posted an audit [T0-15:103, 114, 315]. |
| Pay | 6 [5–7] · C | Deloitte Mgr/Sr Mgr AI Risk & Validation $171.6-338.3K (posted range, C) [T0-15:315]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Enforcement-dependent; SR 26-2 excludes generative and agentic AI [T0-15:355]. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 4.1 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-responsible-ai-engineer"></a>
**#23 · Responsible AI / AI Governance Engineer** (`responsible-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4] · C | Thin technical niche: Stryker, Beacon Hill, Cognizant, Infosys, Workday postings; 'expect few openings' [T0-15:110, 123, 303-314]. |
| Pay | 6 [5–7] · C | Stryker AI Governance Engineer $112.8-239.9K; Beacon Hill $75-85/hr (C) [T0-15:303-304]; IAPP tech-sector technical AI governance median $221K (B) [T0-15:398]. Weakest input C. |
| Durability | 6 [4.5–7.5] · D | Judgement. Regulation-driven (EU AI Act Annex III from 2 Dec 2027) with reversal risk [T0-15:72, 232]. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-domain-evaluation-specialist"></a>
**#24 · Domain Evaluation Specialist / AI Trainer** (`domain-evaluation-specialist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [3.5–7.5] · D | LinkedIn Jobs on the Rise: data annotators #4 (C) [T0-06:174]; Mercor >30,000 experts on contract (C/D) [T0-06:177]; marketplace demand not measured as postings. |
| Pay | 3.5 [2–5.5] · C | Mercor ~$85+/hr, ~$110/hr average (Bloomberg relay); ~$120/hr (SWE) to $400/hr (civil-rights attorneys); >=10 h/week at-will contracts [T0-06:177]. |
| Durability | 3.5 [2–5] · D | Judgement. 'A bridge, not a destination' [T0-06:273, 650]. |
| Leverage | 5 [4–6] · D | Judgement. |
| Access | 6.1 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-engineering-manager"></a>
**L1 · AI Engineering Manager / Director of AI Engineering** (`ai-engineering-manager`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [3.5–6.5] · D | 'Lead or manager' labels on 5.6% of AI Engineer and 9.2% of MLE postings (JobsPipe JD) mix IC leads with managers; Head/Director/Manager of AI Engineering posts at Teradata, Front, Harrington Starr [T0-01 D3]. |
| Pay | 7 [6–9] · D | One top-of-market data point: Anthropic 'MTS (Manager)' LCA base median $405K [T0-02:303]; T0-02 rejects LCA wages as an anchor [T0-02:106]; no broad EM pay in corpus. |
| Durability | 7 [5.5–8.5] · D | Judgement. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 4 [3–5] · D | Needs a lead/manager track record; AI engineers move into management in under 3 years (C) [T0-17:126]. |

<a id="ledger-vp-head-of-ai"></a>
**L2 · VP / Head of AI** (`vp-head-of-ai`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4] · D | No count in corpus. |
| Pay | 9 [7.5–10] · D | No pay data in corpus (Radford 'Head of AI' family is paywalled) [T0-02:491]. Unanchored judgement: no proxy. |
| Durability | 7 [5.5–8.5] · D | Judgement. |
| Leverage | 9 [8–10] · D | Judgement. |
| Access | 2 [1–3] · D | Multi-year leadership track record. |

<a id="ledger-chief-ai-officer"></a>
**L3 · Chief AI Officer (CAIO)** (`chief-ai-officer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · C | OMB M-25-21 requires a CAIO at US federal agencies (B) [T0-15:357]; '76% of firms report a CAIO' (IBM via secondary, C) [T0-01 F12]. |
| Pay | 8.5 [5–10] · D | No pay data in corpus; corporate and US-federal CAIO pay differ widely, so the range is wide. Unanchored judgement: no proxy. |
| Durability | 5.5 [4–7] · D | Judgement. May be transitional; fractional CAIO demand 'falling sharply' [T0-18:193-194]. |
| Leverage | 9 [8–10] · D | Judgement. |
| Access | 1.5 [0.5–2.5] · D | Executive track record. |

<a id="ledger-independent-ai-consultant"></a>
**L4 · Independent AI Consultant / Contractor** (`independent-ai-consultant`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [2.5–5.5] · D | Network-driven: 92% find clients through networks [T0-18:104]; no posting count. |
| Pay | 4 [3–5.5] · C | US asks $150-250/hr; senior AI contractor cards cluster at $130-235/hr, '$300+ is marketing'; UK median GBP550/day; India-based seniors quoted $50-100/hr; modelled net P50 US $105K, India $53K for practitioners with traction (model) [T0-18:82-116]. Contract/hourly income maps to the 3-4 anchor. |
| Durability | 5 [3.5–6.5] · D | Judgement. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 3 [2–4] · C | 5+ years, >=50 referral sources, 6 months of reserves [T2-01:631-635]. |

<a id="ledger-fractional-ai-leader"></a>
**L5 · Fractional Head of AI / Fractional CAIO** (`fractional-ai-leader`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · C | Go Fractional: CAIO 6 then 10 posts in 90 days (label 'falling sharply') vs 326 profiles; Fractional CTO 19 then 17 posts (labels 'rising sharply', then 'rising') vs 1,042-1,116 profiles [T0-18:52, 193-196]. T0-18 rates this demand evidence 'conflicting' [T0-18:1261]. |
| Pay | 4 [3–5.5] · C | Asks $150-250/hr; offers 0.59-0.91x asks; retainers ~$8-13K/month for 10-13 h/week; modelled US net P50 $105K, P90 $160K for practitioners with traction (model, D) [T0-18:82-89, 116]. Contract/hourly income maps to the 3-4 anchor. |
| Durability | 4.5 [3–6] · D | Judgement. UK GenAI contract median fell from GBP613-625 (2024) to GBP550 (2025-26); T0-18 models that a 30% cut in delivery hours needs a 43% higher hourly rate to hold revenue [T0-18:95, 119, 148]. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 2 [1–3] · C | Fractional Jobs survey respondents (n=1,733, all functions, incl. past and aspiring fractionals): 87% have 11+ years; 83% Director-level or above [T0-18:1406]. |

### A.2 Persona access scores (inputs to the Access pillar and the persona lenses)

Scale: ≥7.5 ≈ a T2-01 ● corridor (about 6–8 months at 15–20 h/week); 4–7 ≈ ◐ (plausible but extended); <4 ≈ ○ (not plausible within 12 months; excluded from that persona's lens). Timelines come from T0-06 R2 and T2-01 §4.1 (Grade D models, conditional on success); cells without a modelled corridor are inferred from skill adjacency (Grade D).

| Role | Backend SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Researcher | Access pillar |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Machine Learning Engineer | 5.5 | 7 | 3.5 | 1.5 | 7 | 6.0 |
| AI Engineer | 9 | 7.5 | 8 | 2 | 7 | 7.9 |
| Research Engineer / Member of Technical Staff | 3 | 3 | 2 | 1 | 7.5 | 5.4 |
| Forward Deployed Engineer | 7.5 | 4.5 | 7 | 4 | 5 | 6.6 |
| Applied AI Engineer | 8.5 | 6.5 | 6.5 | 2 | 7 | 7.3 |
| Research Scientist (AI/ML) | 1 | 1.5 | 1 | 1 | 4 | 2.9 |
| Applied Scientist | 3 | 4.5 | 2 | 1 | 8 | 5.9 |
| AI Infrastructure / GPU Platform Engineer | 7 | 2.5 | 2.5 | 1 | 3.5 | 5.2 |
| Inference / LLM Serving Engineer | 7 | 2.5 | 2.5 | 1 | 4.5 | 5.3 |
| AI Product Manager | 4 | 4.5 | 4 | 6.5 | 3.5 | 5.5 |
| ML Platform / MLOps Engineer | 7 | 5 | 4 | 1.5 | 4 | 5.7 |
| Agentic AI Engineer | 8.5 | 6.5 | 7 | 2 | 6.5 | 7.3 |
| AI / GenAI Solutions Architect | 6 | 4.5 | 5 | 4.5 | 4 | 5.4 |
| AI Evaluation Engineer | 7 | 8 | 6.5 | 3 | 7.5 | 7.2 |
| GPU Kernel / ML Compiler Engineer | 4 | 2 | 1.5 | 1 | 4.5 | 3.6 |
| AI Governance Programme Lead / Manager | 2.5 | 3 | 2 | 6 | 3 | 4.7 |
| Physical AI / Robotics AI Engineer | 3.5 | 3 | 2 | 1 | 5 | 4.0 |
| Frontier AI Safety / Alignment Researcher | 2 | 2 | 1.5 | 1.5 | 4.5 | 3.4 |
| AI Security Engineer / AI Red Teamer | 5.5 | 3 | 3.5 | 2 | 4 | 4.6 |
| AI Enablement Engineer | 7.5 | 6 | 7 | 5 | 5 | 6.8 |
| AI Product Engineer (AI Frontend) | 6 | 4 | 7 | 2 | 4 | 5.8 |
| AI Risk, Audit & Compliance Specialist | 2 | 4 | 1.5 | 5 | 3 | 4.1 |
| Responsible AI / AI Governance Engineer | 5.5 | 6 | 3.5 | 3 | 5.5 | 5.4 |
| Domain Evaluation Specialist / AI Trainer | 4 | 5 | 3 | 7 | 7 | 6.1 |

### A.3 India-lens inputs

India Demand bands (live India postings): ≥300 → 10 · 150–299 → 8.5 · 75–149 → 7 · 30–74 → 5.5 · 10–29 → 4 · 1–9 → 2.5 · ≈0 → 1. India Pay anchors (TC): P50 ≥ ₹60L → 9.5 · ₹40–60L → 8 · ₹25–40L → 6.5 · ₹15–25L → 5 · < ₹15L → 3, adjusted for the P90 ceiling. Roles without India data carry wide ranges and Grade D.

| Role | India Demand | India Pay | Basis |
|---|---|---|---|
| Machine Learning Engineer | 7 [6–7.5] · B | 8 [7–8.5] · B | JobsPipe India 90 live; India 7.7% of MLE postings vs US 50.3% (JobsPipe JD 2026-11-02). / Levels.fyi Bengaluru MLE TC P50 Rs44.5L, P90 Rs94.6L (n=96) [T0-02:145]; Hyderabad P50 Rs30.3L [T0-02:149]. |
| AI Engineer | 10 [9–10] · B | 5.5 [4.5–6.5] · B | JobsPipe India 398 live; India 13.6% of AI Engineer postings; GenAI Engineer/Developer is the dominant GCC alias [T0-01 F10, D8]. / Levels.fyi Bengaluru AI Engineer P50 Rs21.4-24.5L, P75 Rs40.4L, P90 Rs62.6L (unstable) [T0-02:146, T0-17:139]; broad market centres Rs10-15L [T0-02:71]. |
| Research Engineer / Member of Technical Staff | 2 [1–3] · D | 8 [6–9.5] · D | Frontier-lab research hiring is US/UK-concentrated; Research Scientist postings are 3.7% India (JobsPipe JD). / No India evidence. |
| Forward Deployed Engineer | 4 [2.5–5.5] · D | 5.5 [4–7] · D | Forward Deployed AI Engineer appears on Weekday India listings [T0-01 D8]; no India count. FDE postings were mostly non-remote in the Aug snapshot (SF 172, NY 133, Remote 65 of ~779) [T0-01 D2]; one JD lists up to 50% travel. / No India pay data in corpus. |
| Applied AI Engineer | 3 [2–4.5] · D | 6 [4–8] · D | No India evidence. / No India evidence. |
| Research Scientist (AI/ML) | 2.5 [1.5–3.5] · C | 8.5 [6.5–9.5] · D | India 3.7% of Research Scientist postings vs US 65.0% (JobsPipe JD, all fields, 2026-11-02); scope mismatch (not AI-specific), so Grade C. / No India evidence. |
| Applied Scientist | 4 [2.5–6] · D | 7.5 [6–9] · D | No India evidence in corpus. / Proxy: Google MLE Bengaluru L4 Rs65.2L, L5 Rs168.3L (small n) [T0-02:254]. |
| AI Infrastructure / GPU Platform Engineer | 3.5 [2–5] · D | 6.5 [5–8] · D | No India evidence. / No India evidence. |
| Inference / LLM Serving Engineer | 3 [2–4] · D | 7 [5.5–8.5] · D | No India evidence. / No India evidence. |
| AI Product Manager | 5.5 [4–7] · D | 6.5 [5–8] · D | JobsPipe Product Manager India 719 live (2026-11-02); AI-mention share assumed as US (≥15.4%, ~110) as an upper bound; no AI-PM title count. / No India evidence. |
| ML Platform / MLOps Engineer | 6.5 [5–8] · C | 5.5 [4.5–6.5] · C | MLOps Engineer is a common GCC AI title (Taggd, C); 18-43% supply gap in AI/MLOps/platform clusters [T0-01 D8, F10]. / Bengaluru MLOps P50 Rs23.6L, P75 Rs41.1L, P90 Rs63.5L [T0-02:147]. |
| Agentic AI Engineer | 4.5 [3–5.5] · C | 5.5 [4.5–6.5] · D | Agentic AI Engineer and Principal Agentic AI Engineer on Weekday India listings [T0-01 D8]. / Treated as AI Engineer. |
| AI / GenAI Solutions Architect | 4 [3–5.5] · D | 6 [4.5–7.5] · D | JobsPipe Solutions Architect India 64 live (2026-11-02); AI-mention share assumed as US (upper bound ~15); no AI-architect title count. / Recruiter guides: senior AI roles at GCCs/top product firms Rs55-80L+ (C) [T0-02:340]. |
| AI Evaluation Engineer | 3 [2–4.5] · C | 5.5 [4–7] · D | Backbase Principal AI Evaluation Engineer, Hyderabad [T0-09:422]. / No India evidence. |
| GPU Kernel / ML Compiler Engineer | 3 [2–4] · D | 7 [5.5–8.5] · D | No India evidence. / No India evidence. |
| AI Governance Programme Lead / Manager | 3.5 [2.5–5] · C | 5 [3.5–6.5] · D | Alstom (Bangalore), Eaton (Pune), EXL JDs; no India count [T0-15:95, 300-302]. / T0-15 did not use unsourced INR ranges [T0-15:469]. |
| Physical AI / Robotics AI Engineer | 2 [1–3] · D | 5 [3.5–6.5] · D | No India evidence. / No India evidence. |
| Frontier AI Safety / Alignment Researcher | 1 [1–2] · D | 5 [3–8] · D | No India evidence. / No India evidence. |
| AI Security Engineer / AI Red Teamer | 3 [2–4.5] · D | 6 [4.5–7] · D | Generic Security Engineer India 239 live (2026-11-02); AI share unknown. / No India evidence. |
| AI Enablement Engineer | 2.5 [1.5–4] · D | 5 [4–6] · D | No India evidence. / No India evidence. |
| AI Product Engineer (AI Frontend) | 2.5 [1.5–4] · D | 5 [4–6.5] · D | No India evidence. / No India evidence. |
| AI Risk, Audit & Compliance Specialist | 3 [2–4] · C | 5 [3.5–6.5] · D | DPO/privacy demand expected to lead in India; DPDP main obligations 13 May 2027 [T0-15:142]. / No India evidence. |
| Responsible AI / AI Governance Engineer | 3.5 [2.5–4.5] · C | 4.5 [3.5–6] · D | Cognizant Responsible AI Engineer (Chennai); Infosys Sr. Responsible AI Analyst (Bengaluru, fresher, closed) [T0-15:306-307]. / T0-15 deliberately did not use unsourced INR ranges [T0-15:469]. |
| Domain Evaluation Specialist / AI Trainer | 5 [3–7] · D | 4 [2.5–6] · D | Remote contract marketplaces; India-specific volume unknown. / USD contract rates if accessible; unknown. |

### A.4 Single-pillar leaders (IC roles, mid scores; ties shown)

- **Pay ceiling:** Research Scientist (AI/ML) 9.5; Research Engineer / Member of Technical Staff 9; Machine Learning Engineer 8.5; Applied Scientist 8; Applied AI Engineer 7.5; Frontier AI Safety / Alignment Researcher 7.5; GPU Kernel / ML Compiler Engineer 7.5; Inference / LLM Serving Engineer 7.5
- **Demand:** AI Engineer 10; Machine Learning Engineer 9; Forward Deployed Engineer 7.5; AI Product Manager 6; AI Governance Programme Lead / Manager 5.5; AI Infrastructure / GPU Platform Engineer 5.5; Domain Evaluation Specialist / AI Trainer 5.5; ML Platform / MLOps Engineer 5.5; Research Engineer / Member of Technical Staff 5.5
- **Durability (judgement):** Frontier AI Safety / Alignment Researcher 8; Research Scientist (AI/ML) 8; AI Infrastructure / GPU Platform Engineer 7.5; AI Security Engineer / AI Red Teamer 7.5; Applied Scientist 7.5; Inference / LLM Serving Engineer 7.5; Research Engineer / Member of Technical Staff 7.5
<!-- END GENERATED -->

---
*Ranked index maintained under the Vivechak research governance framework. Composite scores are Grade M model outputs; judgement pillars are Grade D. Pay figures carry a 90-day TTL (next review 2027-01-31); posting counts are re-verified within 31 days (next by 2026-12-03). Not legal, tax or financial advice.*
