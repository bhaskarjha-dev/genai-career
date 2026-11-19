---
id: roles.rankings
title: "Role Rankings: The Composite Career Index (All Demand)"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-06
summary: "Evidence-weighted ranking of the GenAI roles on all demand for each title (CCI): pillar scores with uncertainty ranges, Monte Carlo ranks, weight sensitivity, goal, persona and India lenses, and a dossier per role."
sources: [T0-01, T0-02, T0-03, T0-06, T0-15, T0-16, T0-17, T0-44, T0-45, T0-48, T0-49, T0-50, T0-51, T0-52, T0-53, T0-54, T0-55, T0-56, T0-57, T0-58, T0-59, T0-60, T0-61, T0-62, T0-63, T0-64, T0-65, T0-66, T0-69, T0-70]
---
# Role Rankings: The Composite Career Index (All Demand)
## An Evidence-Weighted, Uncertainty-Aware Composite Career Index (CCI) for Every Canonical GenAI Role

> **Method:** Composite Career Index (CCI) with anchored 0–10 pillars, uncertainty ranges and Monte Carlo simulation.
> **Role universe:** the 29 canonical roles of the [role catalog](role-catalog.md): 24 individual-contributor (IC) roles plus 5 leadership/independent tracks
> **Evidence standard:** EGP-1.0. Composite scores are **model outputs (Grade M** per the [README](../../README.md) evidence standard: a model output inherits the weakest grade among its inputs). They combine graded measurements (A–C) with labelled judgements (D). They are decision aids, not facts.
> **Reproduce:** `python3 scripts/rank_roles.py --update` reads [data/role_scores.json](../../data/role_scores.json) and rewrites every block between the `BEGIN/END GENERATED` markers in this file, including Appendix A (standard library only, fixed seed). The narrative and the hand-written tables in §0, §5.1 and §7 are checked by hand after any change in ranks
> **Companions:** [role-skill-maps.md](../03-skills-and-tech/role-skill-maps.md) gives the narrative skill map for every ranked role · [role-skill-inventories.md](../03-skills-and-tech/role-skill-inventories.md) types every skill per role (concepts, methods, tools, frameworks, platforms, non-technical skills) with evidence · [resume-skills-matrix.md](../06-job-search/resume-skills-matrix.md) tiers those skills for resumes
> **Role hubs:** each role's rank, scores and evidence are summarised on its one-page hub ([hubs](hubs/README.md)); the [role map](role-map.md) shows where each role's work sits.
> **Scope: all demand.** This index scores every posting in a title family, GenAI or not. The GenAI-only order is [GenAI target roles](genai-target-roles.md): it counts only the postings that name LLM (76.7% of AI Engineer and 45.0% of ML Engineer postings [B · JobsPipe JD, 2026-11-02]) and averages eight lenses, which puts AI Engineer first, while ML Engineer's full family, with its recsys, ads and autonomous-vehicle work and higher broad-market pay, makes it #1 here [M].

---

## 0. The Answer

**Co-#1: Machine Learning Engineer (CCI 77.9) and AI Engineer (CCI 76.3).** Both sit in Band S and land in the top three in nearly every Monte Carlo draw (`1 (1–2)` and `2 (1–3)`):
- **Weight profiles:** MLE takes #1 on four of the six profiles (Base, Equal, Pay-max, Moat-first); AI Engineer takes #1 on Hiring-safety and Switcher.

Choose between them on preference:
- **Machine Learning Engineer wins on pay and depth.** US total comp P50 is $287K vs $155K; P90 is $497.5K vs $280K (Levels.fyi, Nov 2026 [B · T0-44]). Within Google, employer and level mix explain 62–69% of the log title gap (`AI Engineer` P50 $240K vs `MLE` ~$290–302K, a +21–26% within-employer MLE premium [B/M · T0-48]).
- **AI Engineer wins on demand and accessibility.** It is the largest GenAI title family in the measured corpora: 1,697 US, 398 India (10.1% of global, correcting a Phase 0 13.6% erratum) and 3,944 global live postings (re-checked 2026-11-13, unchanged since 2026-10-19 [B · T0-48, T0-70]). It also has the shortest modelled switch routes; backend engineers take about 6 months.

**#3–#5: Forward Deployed Engineer (71.8), Research Engineer / MTS (71.4) and Applied Scientist (70.7).** All three sit in Band A with overlapping Monte Carlo ranges (`4 (3–6)`, `4 (2–6)`, `5 (3–7)`):
- **Forward Deployed Engineer (#3)** moved up after new Levels.fyi US FDE total-comp data ($205K P50 / $350K P90, above US AI Engineer [B · T0-44]) and Fast AI Jobs cluster growth (1,007 roles across 353 AI startups, though only 23/50 newest rows are IC FDE titles [B/M · T0-51, T0-70]).
- **Research Engineer / MTS (#4)** remains the highest-paying engineering ladder (lab US base $205K–$850K; SWE/MTS TC medians ~$875–882.5K [B · T0-02, T0-50]) and a quorum-crossing candidate (`223` on Fast AI Jobs, 2026-11-12 [B · T0-70]), offset by narrow access and semi-liquid equity.
- **Applied Scientist (#5)** rose two places once Research Pipeline 2 replaced its Grade D placeholders with direct Big Tech evidence: Amazon Science listed `451` Applied Science openings on 2026-11-13 (~270 literally AS-titled, 90 in India [B · T0-52]) and Levels.fyi Amazon AS TC spans $245K (L4) to $653K (L7) [B · T0-52].

**#6–#10: Applied AI Engineer (68.6), Research Scientist (67.8), AI Infrastructure (66.7), ML Platform / MLOps (65.2) and AI Security Engineer (65.1).** Two roles broke into Band A in November 2026 on newly measured Grade B volume: **ML Platform / MLOps Engineer** graduated from Verified to Established (`E`: Axial 1,959 US MLOps postings + ITJobsWatch 184 UK permanent jobs + Fast AI Jobs 1,099 [B · T0-58]) and **AI Security Engineer** jumped from #19 to #10 after SANS's live tracker recorded >850 AI/ML security-engineer postings (~100 red-team, 93 supply-chain) alongside dated US bands of $178K–$356.5K [B · T0-60, T0-69].

**The most important finding still holds: the best skills are often broader than their standalone titles.** Agentic AI (59.3% of AI Engineer JDs) and evaluation (19.0% of S09 JDs) remain stronger as force multipliers inside Tier 1–2 titles than as standalone titles (Agentic AI Engineer #14, AI Evaluation Engineer #15).

### Why Notable Roles Rank Where They Do

| Role | Rank (CCI) | What the evidence shows |
|---|:---:|---|
| Machine Learning Engineer | 1 (77.9) | Second-largest measured demand and highest broad-market pay distribution ($287K P50 / $497.5K P90 [B · T0-44]) |
| AI Engineer | 2 (76.3) | Largest measured demand (3,944 global / 1,697 US / 398 India, static 2026-11-13) and best accessibility; comp trimmed -0.25 to 6.5 per Nov 2026 Levels.fyi ($155K P50) and Axial (-5% to -12% vs ML ceilings) [B · T0-44, T0-48] |
| *Forward Deployed Engineer* | **3 (71.8)** | New Levels.fyi US TC ($205K P50 / $350K P90) sits above US AI Engineer [B · T0-44]; Fast AI Jobs cluster reached 1,007 roles at 353 AI startups (23/50 newest IC FDE titles) [B/M · T0-51, T0-70] |
| *Research Engineer / Member of Technical Staff* | **4 (71.4)** | Highest engineering pay (lab base $205–850K; SWE/MTS TC $875–882.5K [B · T0-02, T0-50]); Fast AI Jobs 223 (quorum candidate for 2026-12-01 recount [B · T0-70]) |
| *Applied Scientist* | **5 (70.7)** | Direct Big Tech demand (Amazon Science 451 Applied Science openings, 90 India [B · T0-52]) and Amazon AS TC ($245K–$653K [B · T0-52]) replaced Phase 0 Grade D placeholders |
| *Applied AI Engineer* | **6 (68.6)** | Live Levels.fyi US TC (P50 $232K / P75 $340K / P90 $505–605K [B · T0-44, T0-53]) and 21 of newest 50 Fast AI Jobs AI rows (42%) |
| Research Scientist (AI/ML) | 7 (67.8) | Highest Pay score (9.5; Pave $4.1–4.7M equity downgraded A→B [B · T0-55]), but Access is 2.9 (PhD + publications; falls to #15 for switchers) |
| AI Infrastructure / GPU Platform Engineer | 8 (66.7) | US posted base median midpoint $261K (labs ~$360K; OpenAI $230–490K [A/B · T0-54]); 10/35 sampled postings in India |
| *ML Platform / MLOps Engineer* | **9 (65.2)** | Graduated V→E on Axial 1,959 US MLOps postings, ITJobsWatch 184 UK perm and Fast AI Jobs 1,099 [B · T0-58] |
| *AI Security Engineer / AI Red Teamer* | **10 (65.1)** | Jumped from #19 on SANS's >850 AI/ML security postings (~100 red-team, 93 supply-chain [B · T0-60, T0-69]), US bands $178–356.5K and 9 India roles |
| Inference / LLM Serving Engineer | 11 (64.6) | Strong US posted base ($288K median midpoint, n=14 [B · T0-56]), but smaller title volume (Inference Jobs 341 upper bound; 37 verified active) |
| AI / GenAI Solutions Architect | 12 (64.1) | Strong proxies (Axial 16,927 US 'AI architecture', JobsPipe SA) and US base $152–248K+ plus Bengaluru SA proxy [B/C · T0-45, T0-62] |
| AI Product Manager | 13 (63.5) | Top non-engineering option (#1 non-technical, #4 India on upgraded Bengaluru Sr PM proxy [C · T0-45, T0-59]); lab senior bands reach $240–490K base |
| Agentic AI Engineer | 14 (63.3) | Kept Watch (W): Skilark 107/28,771 (0.37%), failed 3 graduation tests; US product firms hire under AI Engineer while India services/GCCs use the title [C · T0-57] |
| AI Evaluation Engineer | 15 (62.6) | 22 named postings globally (5+ India) and bimodal US base ($120–304K Microsoft to $310–500K Transluce [A/B · T0-60]); still smaller than broad builder roles |
| AI Governance Programme Lead / Manager | 19 (57.0) | EU Reg. (EU) 2026/1744 delayed Annex III high-risk duties 16 months to Dec 2027 and Colorado repealed SB 24-205, moderating near-term urgency [A/B · T0-61, T0-70] |
| AI Enablement Engineer | 23 (49.0) | Skillenai 90-day count fell 57 → 42 (2026-11-05) and bimodal pay ($120–180K base) pulled it down from #20 [B/C · T0-62] |
| VP / Head of AI; Chief AI Officer | L2 (58.0); L3 (53.0), separate board | Leadership tracks are ranked separately (§4); RP2 added posted US base ($170–315K VP; $118–200K public CAIO; SBI India up to ₹160L) [A/B · T0-65] |
| Speculative titles (Context Engineer, Cognitive Architect, Prompt Wizard, etc.) | Not ranked | No posting evidence, or quarantined titles that cannot be scored honestly (§8) |

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
| 2 | AI Engineer | **76.3** | S | 10 | 6.5 | 6 | 7.5 | 7.9 | High | 2 (1–3) | 100% |
| 3 | Forward Deployed Engineer | **71.8** | A | 7.5 | 7 | 6.5 | 8.5 | 6.6 | Medium | 4 (3–6) | 83% |
| 4 | Research Engineer / Member of Technical Staff | **71.4** | A | 5.5 | 9 | 7.5 | 8 | 5.4 | High | 4 (2–6) | 83% |
| 5 | Applied Scientist | **70.7** | A | 6.5 | 7.75 | 7.5 | 7.5 | 5.9 | High | 5 (3–7) | 74% |
| 6 | Applied AI Engineer | **68.6** | A | 5 | 7.75 | 6.5 | 8.5 | 7.3 | Medium | 6 (4–10) | 30% |
| 7 | Research Scientist (AI/ML) | **67.8** | A | 5 | 9.5 | 8 | 7.5 | 2.9 | High | 8 (5–12) | 12% |
| 8 | AI Infrastructure / GPU Platform Engineer | **66.7** | A | 5.5 | 7 | 7.5 | 8.5 | 5.2 | Medium | 8 (6–13) | 9% |
| 9 | ML Platform / MLOps Engineer | **65.2** | A | 6.5 | 6.5 | 6.5 | 7.5 | 5.7 | High | 10 (7–14) | 2% |
| 10 | AI Security Engineer / AI Red Teamer | **65.1** | A | 5.5 | 7 | 7.5 | 8 | 4.6 | High | 11 (7–15) | 2% |
| 11 | Inference / LLM Serving Engineer | **64.6** | B | 4.5 | 7.5 | 7 | 8.5 | 5.3 | Medium | 11 (8–15) | 1% |
| 12 | AI / GenAI Solutions Architect | **64.1** | B | 5.5 | 7 | 6 | 8.5 | 5.4 | Medium | 12 (8–16) | 1% |
| 13 | AI Product Manager | **63.5** | B | 6 | 6.5 | 6 | 8 | 5.5 | Medium | 12 (7–16) | 3% |
| 14 | Agentic AI Engineer | **63.3** | B | 4.5 | 6.75 | 6.5 | 7.5 | 7.3 | Medium | 13 (10–16) | 0% |
| 15 | AI Evaluation Engineer | **62.6** | B | 4 | 7 | 6.5 | 7.5 | 7.2 | High | 13 (8–16) | 1% |
| 16 | GPU Kernel / ML Compiler Engineer | **59.8** | B | 4 | 7.5 | 6.5 | 8.5 | 3.6 | Medium | 16 (13–18) | 0% |
| 17 | Physical AI / Robotics AI Engineer | **58.2** | B | 4.5 | 7 | 6.5 | 7 | 4.0 | Medium | 18 (15–20) | 0% |
| 18 | Frontier AI Safety / Alignment Researcher | **57.9** | B | 3 | 7.5 | 8 | 7 | 3.4 | Medium | 18 (15–20) | 0% |
| 19 | AI Governance Programme Lead / Manager | **57.0** | B | 5.5 | 5.5 | 6 | 7 | 4.7 | Medium | 19 (17–20) | 0% |
| 20 | AI Product Engineer (AI Frontend) | **54.5** | C | 3.5 | 6.5 | 5.5 | 6.5 | 5.8 | Medium | 20 (17–22) | 0% |
| 21 | AI Risk, Audit & Compliance Specialist | **54.1** | C | 4.5 | 6 | 6 | 6.5 | 4.1 | High | 21 (19–22) | 0% |
| 22 | Responsible AI / AI Governance Engineer | **52.3** | C | 2.5 | 6.5 | 6 | 6.5 | 5.4 | High | 22 (20–23) | 0% |
| 23 | AI Enablement Engineer | **49.0** | C | 2.5 | 5.5 | 4.5 | 6.5 | 6.8 | Medium | 23 (22–24) | 0% |
| 24 | Domain Evaluation Specialist / AI Trainer | **46.2** | C | 5.5 | 3.5 | 3.5 | 5 | 6.1 | High | 24 (23–24) | 0% |
<!-- END GENERATED -->

**How to read the board:**
- **CCI** is a decision aid built from graded evidence plus explicit judgement. It is not a measured fact.
- **The P10–P90 interval is the honest rank.** "6 (3–10)" for Applied Scientist means it could reasonably land anywhere from #3 to #10 once it is measured.
- **Pay 6.75 (AI Engineer) vs 8.5 (MLE)** reflects each title's market pay distribution. Like-for-like posted base differs much less ($200–275K vs $213–288K); about half the total-comp gap is employer mix.

| Band | Roles |
|---|---|
| **S (≥75)** | Machine Learning Engineer, AI Engineer |
| **A (65–75)** | Forward Deployed Engineer, Research Engineer/MTS, Applied Scientist, Applied AI Engineer, Research Scientist, AI Infrastructure Engineer, ML Platform/MLOps, AI Security Engineer |
| **B (55–65)** | Inference Engineer, AI Solutions Architect, AI Product Manager, Agentic AI Engineer, AI Evaluation Engineer, GPU Kernel Engineer, Physical AI Engineer, AI Safety Researcher, AI Governance Lead |
| **C (<55)** | AI Product Engineer, AI Risk/Audit/Compliance, Responsible AI Engineer, AI Enablement Engineer, Domain Evaluation Specialist |

---

## 3. Robustness: How Much Do the Weights Matter?

<!-- BEGIN GENERATED: scripts/rank_roles.py (sensitivity) -->
| Role | Base | Equal | Pay-max | Hiring-safety | Moat-first | Switcher | Best–worst |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Machine Learning Engineer | 1 | 1 | 1 | 2 | 1 | 2 | 1–2 |
| AI Engineer | 2 | 2 | 4 | 1 | 4 | 1 | 1–4 |
| Forward Deployed Engineer | 3 | 3 | 7 | 3 | 6 | 3 | 3–7 |
| Research Engineer / Member of Technical Staff | 4 | 4 | 2 | 5 | 2 | 6 | 2–6 |
| Applied Scientist | 5 | 5 | 5 | 4 | 3 | 5 | 3–5 |
| Applied AI Engineer | 6 | 6 | 6 | 7 | 8 | 4 | 4–8 |
| Research Scientist (AI/ML) | 7 | 8 | 3 | 9 | 5 | 15 | 3–15 |
| AI Infrastructure / GPU Platform Engineer | 8 | 7 | 8 | 8 | 7 | 10 | 7–10 |
| ML Platform / MLOps Engineer | 9 | 10 | 14 | 6 | 11 | 8 | 6–14 |
| AI Security Engineer / AI Red Teamer | 10 | 11 | 10 | 11 | 9 | 14 | 9–14 |
| Inference / LLM Serving Engineer | 11 | 9 | 9 | 13 | 10 | 13 | 9–13 |
| AI / GenAI Solutions Architect | 12 | 13 | 13 | 12 | 15 | 12 | 12–15 |
| AI Product Manager | 13 | 15 | 15 | 10 | 16 | 11 | 10–16 |
| Agentic AI Engineer | 14 | 12 | 12 | 14 | 12 | 7 | 7–14 |
| AI Evaluation Engineer | 15 | 14 | 11 | 15 | 13 | 9 | 9–15 |
| GPU Kernel / ML Compiler Engineer | 16 | 16 | 16 | 18 | 17 | 19 | 16–19 |
| Physical AI / Robotics AI Engineer | 17 | 17 | 18 | 17 | 18 | 18 | 17–18 |
| Frontier AI Safety / Alignment Researcher | 18 | 18 | 17 | 20 | 14 | 24 | 14–24 |
| AI Governance Programme Lead / Manager | 19 | 19 | 21 | 16 | 19 | 16 | 16–21 |
| AI Product Engineer (AI Frontend) | 20 | 20 | 19 | 21 | 20 | 17 | 17–21 |
| AI Risk, Audit & Compliance Specialist | 21 | 21 | 22 | 19 | 21 | 23 | 19–23 |
| Responsible AI / AI Governance Engineer | 22 | 22 | 20 | 23 | 22 | 22 | 20–23 |
| AI Enablement Engineer | 23 | 23 | 23 | 24 | 23 | 20 | 20–24 |
| Domain Evaluation Specialist / AI Trainer | 24 | 24 | 24 | 22 | 24 | 21 | 21–24 |
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
| L1 | AI Engineering Manager / Director of AI Engineering | **64.5** | 5.5 | 7.5 | 7 | 8 | 4 | High |
| L2 | VP / Head of AI | **58.0** | 3 | 8 | 7 | 9 | 2 | Medium |
| L3 | Chief AI Officer (CAIO) | **53.0** | 2.5 | 8 | 5.5 | 9 | 1.5 | High |
| L4 | Independent AI Consultant / Contractor | **45.5** | 4.5 | 4 | 5 | 6.5 | 3 | High |
| L5 | Fractional Head of AI / Fractional CAIO | **38.8** | 2.5 | 4 | 4.5 | 7 | 2 | High |
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
| Hiring-safety | AI Engineer (81) | Machine Learning Engineer (80) | Forward Deployed Engineer (72) | Applied Scientist (69) | Research Engineer / Member of Technical Staff (67) |
| Pay-max | Machine Learning Engineer (78) | Research Engineer / Member of Technical Staff (75) | Research Scientist (AI/ML) (73) | AI Engineer (72) | Applied Scientist (72) |
| Moat-first | Machine Learning Engineer (75) | Research Engineer / Member of Technical Staff (72) | Applied Scientist (72) | AI Engineer (71) | Research Scientist (AI/ML) (70) |
| Switcher | AI Engineer (79) | Machine Learning Engineer (74) | Forward Deployed Engineer (70) | Applied AI Engineer (68) | Applied Scientist (67) |
| Equal | Machine Learning Engineer (76) | AI Engineer (76) | Forward Deployed Engineer (72) | Research Engineer / Member of Technical Staff (71) | Applied Scientist (70) |
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
| Backend / Systems SWE | AI Engineer (83) | Forward Deployed Engineer (74) | Machine Learning Engineer (73) | Applied AI Engineer (72) | AI Infrastructure / GPU Platform Engineer (69) | Agentic AI Engineer, ML Platform / MLOps Engineer |
| Data Scientist / BI | Machine Learning Engineer (78) | AI Engineer (78) | AI Evaluation Engineer (66) | Applied AI Engineer (65) | Forward Deployed Engineer (63) | Applied Scientist, Agentic AI Engineer |
| Frontend / Full-Stack | AI Engineer (79) | Forward Deployed Engineer (72) | Applied AI Engineer (65) | Agentic AI Engineer (63) | AI Evaluation Engineer (61) | AI / GenAI Solutions Architect, AI Product Engineer (AI Frontend) |
| Non-Technical (5+ yrs domain) | AI Product Manager (65) | Forward Deployed Engineer (62) | AI Governance Programme Lead / Manager (59) | AI / GenAI Solutions Architect (58) | Domain Evaluation Specialist / AI Trainer (54) | AI Risk, Audit & Compliance Specialist, AI Enablement Engineer |
| PhD / Academic Researcher | Machine Learning Engineer (78) | AI Engineer (76) | Applied Scientist (75) | Research Engineer / Member of Technical Staff (73) | Applied AI Engineer (67) | Forward Deployed Engineer, AI Evaluation Engineer |
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
| 1 | AI Engineer | 73.2 | 10 | 5.25 | 2 | 1 (1–2) |
| 2 | Machine Learning Engineer | 71.7 | 7 | 8 | 1 | 2 (1–3) |
| 3 | Applied Scientist | 66.3 | 5 | 7.5 | 5 | 3 (2–6) |
| 4 | AI Product Manager | 66.0 | 5.5 | 8 | 13 | 4 (3–7) |
| 5 | AI Infrastructure / GPU Platform Engineer | 63.0 | 4.5 | 6.5 | 8 | 6 (4–10) |
| 6 | Applied AI Engineer | 61.7 | 4 | 6 | 6 | 8 (4–14) |
| 7 | AI / GenAI Solutions Architect | 61.6 | 4 | 7.5 | 12 | 8 (5–13) |
| 8 | ML Platform / MLOps Engineer | 61.5 | 6 | 5.5 | 9 | 8 (5–12) |
| 9 | Forward Deployed Engineer | 60.6 | 4.5 | 5.5 | 3 | 10 (5–14) |
| 10 | Research Engineer / Member of Technical Staff | 60.1 | 2 | 8 | 4 | 11 (7–15) |
| 11 | AI Security Engineer / AI Red Teamer | 60.1 | 4.5 | 6 | 10 | 10 (6–14) |
| 12 | Inference / LLM Serving Engineer | 59.6 | 4 | 6 | 11 | 11 (6–15) |
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
- **GCC demand carries execution risk:** "nearly 70%" of India GCCs are stuck at AI pilots [B · T0-09 L77].
- **Most India-lens inputs are Grade C/D; treat this ranking as directional** (Appendix A.3).

---

## 6. Top-10 Dossiers

<a id="rank-1-ml-engineer"></a>
### #1 Machine Learning Engineer: CCI 77.9 · Band S · High confidence
`Demand 9 · Pay 8.5 · Durability 7 · Leverage 7.5 · Access 6.0 · Monte Carlo 1 (1–2)`
- **Why #1:**
  - The second-largest measured GenAI title (US 1,084; global 2,157; Axial H1 2026 US 13,776 [B/C · T0-24, T0-49]), with the highest broad-market pay distribution (US TC P50 $287K, P90 $497.5K [B · T0-44]).
  - LLM is named in 45.0% of MLE postings (JobsPipe count date 2026-09-10 [B · T0-49, T0-69]), so MLE is a core GenAI hiring channel, not "legacy ML".
- **Pay anchors:**
  - Big Tech: Meta E5 $472–497K, E6 $660–790K; Amazon L6 $401K; Google L5 $393–445K, L6 $607–646K [B · T0-44].
  - Axial posted base ceilings: $180–300K (senior $241K). Bengaluru TC (2026-11-12, n=97): P50 ₹44.4L–₹44.7L, P90 ₹80.7L [B · T0-45].
- **Best for:** PhDs, data scientists who can engineer, and backend engineers willing to add ML depth.
- **Interview track:** classic ML system design plus coding.
- **Watch:** API-first adoption shifts routine application work toward AI Engineer; differentiate on evals, serving, post-training and scale optimisation. → [Hub](hubs/ml-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ml-engineer) · [Profile](role-catalog.md#profile-ml-engineer)

<a id="rank-2-ai-engineer"></a>
### #2 AI Engineer: CCI 76.3 · Band S · High confidence
`Demand 10 · Pay 6.5 · Durability 6 · Leverage 7.5 · Access 7.9 · Monte Carlo 2 (1–3)`
- **Why #2:**
  - The largest GenAI title family in the measured corpora (US 1,697; India 398 = 10.1% of global; global 3,944, static 2026-11-13; Fast AI Jobs 352; LinkedIn Jobs on the Rise #1 [B · T0-48, T0-70]).
  - The shortest switch routes: backend ~6 months, frontend ~7, data scientist ~8.
- **Pay anchors:**
  - Levels.fyi US TC (Nov 2026): P25 $110K / P50 $155K / P75 $212K / P90 $280K (SF Bay P50 $225K / P90 $460K); Axial senior posted base ceiling $213K (5–12% below ML ceilings) [B · T0-44].
  - Google within-employer check shows 62–69% of the log title gap vs MLE is employer and level mix [B/M · T0-48]. Greater Bengaluru P50 ₹20.0L, P90 ₹60.6L [B · T0-45].
- **Best for:** backend, frontend/full-stack and data-science engineers, and India-based engineers (GenAI Engineer/Developer is the top GCC label per Taggd, C).
- **Interview track:** application track (coding, RAG/agent design, evals, plus emerging AI-assisted build rounds).
- **Watch:** wrapper-level work is commoditised; move into evals, agent reliability and cost/latency engineering. → [Hub](hubs/ai-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-engineer) · [Profile](role-catalog.md#profile-ai-engineer)

<a id="rank-3-forward-deployed-engineer"></a>
### #3 Forward Deployed Engineer: CCI 71.8 · Band A · Medium confidence
`Demand 7.5 · Pay 7 · Durability 6.5 · Leverage 8.5 · Access 6.6 · Monte Carlo 4 (3–6)`
- **Why #3:**
  - The largest AI-startup cluster: Fast AI Jobs reached 1,007 open roles at 353 AI startups on 2026-11-12 (+29% vs late Jul 779 [B · T0-51, T0-70]), and Indeed India / IANS reported a 19× YoY India surge from a low base [B · T0-25].
  - New Levels.fyi US FDE TC (2026-09-08) puts P50 at $205K / P75 $277K / P90 $350K — clearly above US AI Engineer ($155K P50) — and Google FDE median reaches $292K [B · T0-44].
  - Joint-highest Leverage (8.5, Grade D): each deployment moves revenue.
- **Why not higher:**
  - Only 23 of the newest 50 Fast AI Jobs rows (46%) are IC FDE titles; 22 are adjacent strategist/GTM/field roles [B/M · T0-51, T0-70].
  - Early-stage startup equity requires heavy risk adjustment (0.4–0.8× Series C–D; lower for stale unicorns [C/D · T0-17]), and the work is mostly non-remote with travel.
- **Interview track:** customer-application track (coding/debugging, architecture/decomposition for RAG/agents/evals, and customer scoping or technical presentation [B/C · T0-51]).
- **Watch:** drift into non-coding pre-sales. Protect production engineering scope. → [Hub](hubs/forward-deployed-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-forward-deployed-engineer) · [Profile](role-catalog.md#profile-forward-deployed-engineer)

<a id="rank-4-research-engineer"></a>
### #4 Research Engineer / Member of Technical Staff: CCI 71.4 · Band A · High confidence
`Demand 5.5 · Pay 9 · Durability 7.5 · Leverage 8 · Access 5.4 · Monte Carlo 4 (2–6)`
- **Why #4:**
  - The highest-paying engineering ladder: Nov 2026 US lab posted base bands span $205–555K (OpenAI), $315–850K (Anthropic), $180–600K (xAI) and $350–475K (Thinking Machines), with SWE/MTS TC medians $875–882.5K [A/B · T0-02, T0-50].
  - Fast AI Jobs reached 223 Research Engineer roles (2026-11-12, flagged as a quorum-crossing candidate for the 2026-12-01 recount [B · T0-70]).
  - Absorbs post-training, RL and training-systems work; stays between #2 and #6 under every weight profile.
- **Why not higher:**
  - Narrow access outside PhD-level profiles, fellowships or strong OSS (vLLM, SGLang), though only 1/18 T0-50 postings required a PhD [B/C · T0-50].
  - Senior lab packages are 49–72% semi-liquid stock; risk-adjust to 0.5–0.8× [C/D · T0-17].
- **Routes:** PhD (~8–18 months), fellowships (Anthropic Fellows requires US/UK/CA work authorisation and reports >40% Safety / 25–50% RL conversion [C, COI · T0-22]), or merged OSS PRs. → [Hub](hubs/research-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-research-engineer) · [Profile](role-catalog.md#profile-research-engineer)

<a id="rank-5-applied-scientist"></a>
### #5 Applied Scientist: CCI 70.7 · Band A · High confidence
`Demand 6.5 · Pay 7.75 · Durability 7.5 · Leverage 7.5 · Access 5.9 · Monte Carlo 5 (3–7)`
- **Why #5:**
  - Direct Big Tech demand replaced Phase 0 placeholders: Amazon Science listed 451 Applied Science category openings on 2026-11-13 (~270 literally AS-titled; 90 India science openings = 14% of global [B · T0-52]), alongside Microsoft, Uber, Zalando and Mistral.
  - Direct US TC benchmarks now exist: Levels.fyi Amazon Applied Scientist mean TC runs L4 $245K, L5 $324K, L6 $407K, L7 $653K (median $306–335K [B · T0-52]).
  - Strongest PhD corridor (#1 for PhDs in the GenAI persona lens), while Microsoft (BS+2/MS+1) and Uber (BS+3–4/MS+2) open non-PhD routes [A/C · T0-52].
- **Watch:** employer concentration in Big Tech exposes hiring to corporate headcount cycles, and India pay remains unmeasured (Grade D). → [Hub](hubs/applied-scientist.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-applied-scientist) · [Profile](role-catalog.md#profile-applied-scientist)

<a id="rank-6-applied-ai-engineer"></a>
### #6 Applied AI Engineer: CCI 68.6 · Band A · Medium confidence
`Demand 5 · Pay 7.75 · Durability 6.5 · Leverage 8.5 · Access 7.3 · Monte Carlo 6 (4–10)`
Customer- and solutions-facing LLM engineering at labs and AI vendors (OpenAI, Anthropic, Mistral, Scale, Snorkel); 21 of the newest 50 Fast AI Jobs AI-Engineer rows (42%, 2026-11-11) carry this title [C · T0-53]. Live Levels.fyi US TC now measures P25 $165K / P50 $232K / P75 $340K / P90 $505–605K (reconciling T0-53 $505K vs T0-44 $605K [B · T0-44, T0-53]). Suits backend engineers and PhDs as the bridge between AI Engineer and FDE. → [Hub](hubs/applied-ai-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-applied-ai-engineer) · [Profile](role-catalog.md#profile-applied-ai-engineer)

<a id="rank-7-research-scientist"></a>
### #7 Research Scientist (AI/ML): CCI 67.8 · Band A · High confidence
`Demand 5 · Pay 9.5 · Durability 8 · Leverage 7.5 · Access 2.9 · Monte Carlo 8 (5–12)`
Highest Pay score (9.5): lab RS TC medians reach ~$1.25M at OpenAI (B) and $0.75–0.83M at Anthropic (C), with Pave senior new-hire equity of $4.1–4.7M (downgraded from Grade A to B as vendor intended grant value [B · T0-55]). Fast AI Jobs lists 333 RS roles at 171 startups and BLS projects +21.8% US growth to 2035 [B · T0-27, T0-55]. Access is only 2.9 (PhD plus top-venue publications; NBER WP 34964 confirms +63% higher probability of top-firm entry), so it drops to #15 for career switchers. → [Hub](hubs/research-scientist.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-research-scientist) · [Profile](role-catalog.md#profile-research-scientist)

<a id="rank-8-ai-infrastructure-engineer"></a>
### #8 AI Infrastructure / GPU Platform Engineer: CCI 66.7 · Band A · Medium confidence
`Demand 5.5 · Pay 7 · Durability 7.5 · Leverage 8.5 · Access 5.2 · Monte Carlo 8 (6–13)`
Runs GPU clusters, high-speed fabrics and storage. US posted base median midpoint is $261K (n=12), rising to ~$360K at frontier labs (OpenAI $230–490K [A], Anthropic $315–485K [A · T0-54]); 10 of 35 sampled postings (28.6%) are in India (NVIDIA, Microsoft, Oracle, neoclouds [B · T0-54]). Durable physical-systems work for SRE, DevOps and backend infrastructure engineers. → [Hub](hubs/ai-infrastructure-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-infrastructure-engineer) · [Profile](role-catalog.md#profile-ai-infrastructure-engineer)

<a id="rank-9-ml-platform-engineer"></a>
### #9 ML Platform / MLOps Engineer: CCI 65.2 · Band A · High confidence
`Demand 6.5 · Pay 6.5 · Durability 6.5 · Leverage 7.5 · Access 5.7 · Monte Carlo 10 (7–14)`
Graduated from Verified to Established (`E`) in November 2026 on Axial's 1,959 US MLOps postings (~70/wk steady [B]), ITJobsWatch's 184 UK permanent jobs citing MLOps in 6 months [B] and Fast AI Jobs' 1,099 broad platform listings [B · T0-58]. US posted base runs $150–357K (median midpoint $245K for senior/Big Tech roles [B · T0-58]), and 13/37 sampled postings sit in India GCCs and services firms under the MLOps Engineer title. → [Hub](hubs/ml-platform-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ml-platform-engineer) · [Profile](role-catalog.md#profile-ml-platform-engineer)

<a id="rank-10-ai-security-engineer"></a>
### #10 AI Security Engineer / AI Red Teamer: CCI 65.1 · Band A · High confidence
`Demand 5.5 · Pay 7 · Durability 7.5 · Leverage 8 · Access 4.6 · Monte Carlo 11 (7–15)`
Jumped from #19 to #10 after SANS's live tracker recorded >850 AI/ML security-engineer postings (~100 AI red-team, +13% WoW; 93 supply-chain security [B · T0-60, T0-69]) and RP2 replaced its Grade D pay placeholder with dated US bands (Amazon Senior AI Red Team $178.4–226.7K + RSUs [A], Microsoft MTS $119.8–234.7K [B], NVIDIA $224–356.5K [A]) plus 9 India postings (₹25–50L [B · T0-60]). Queued for exact-title deduplicated recount on 2026-12-01. → [Hub](hubs/ai-security-engineer.md) · [Skills](../03-skills-and-tech/role-skill-maps.md#skills-ai-security-engineer) · [Profile](role-catalog.md#profile-ai-security-engineer)

---

## 7. Roles 11–24 at a Glance

| Rank | Role | CCI | What holds it back | What would lift it | Best for |
|:---:|---|:---:|---|---|---|
| 11 | Inference / LLM Serving Engineer | 64.6 | Smaller title volume (Inference Jobs 341 upper bound; 37 verified active [B/C · T0-56]) despite strong US base ($288K median midpoint) | Broader enterprise self-hosting demand | Systems/C++ engineers; backend engineers with infra depth |
| 12 | AI / GenAI Solutions Architect | 64.1 | No exact AI-SA title count (Axial 16,927 'AI architecture' proxy [C · T0-62]); pre-sales/travel skew | Dedicated AI-SA title volume and OTE transparency | Senior engineers, consultants, cloud architects |
| 13 | AI Product Manager | 63.5 | No exact AI-PM title count (AI Pulse 570 category [C · T0-70]); entry narrowing to experienced PMs | Verified AI-PM count in 2026-12-01 recount | Experienced PMs (#1 non-technical; #4 India) |
| 14 | Agentic AI Engineer | 63.3 | Kept Watch (W): Skilark 107/28,771 (0.37%), failed 3 graduation tests; US product firms hire under AI Engineer [C · T0-57] | Passing graduation tests 1–4 in US product market | Backend and distributed-systems engineers; India GCC/services titles |
| 15 | AI Evaluation Engineer | 62.6 | Smaller title (22 named postings globally, 5+ India [B · T0-60]) despite strong bimodal pay ($120–500K) | Dedicated eval-engineering ladders outside labs/Big Tech | Backend/DS/PhD engineers; *every* AI Engineer as a core skill |
| 16 | GPU Kernel / ML Compiler Engineer | 59.8 | Narrow access (3.6); tile DSLs and agentic kernel tools abstract routine kernel writing [B/C · T0-63] | Broad custom-silicon and inference-compiler expansion | Systems/C++/CUDA/Triton engineers, PhDs |
| 17 | Physical AI / Robotics AI Engineer | 58.2 | Graduated W→V (48 postings across 38 employer entries; US median base ~$242.5K [B/C · T0-64]), but capital-intensive hardware risk | Industrial/humanoid deployment scale beyond pilots | Robotics/controls/ML engineers |
| 18 | Frontier AI Safety Researcher | 57.9 | ~600 technical FTEs (+21%/yr [C · T0-60]); 0/23 India postings; wide pay split (labs $350–500K vs non-profits $120–240K) | Continued lab and institute safety headcount growth | PhDs, fellowship alumni (US/UK/CA work auth) |
| 19 | AI Governance Programme Lead | 57.0 | EU Reg. (EU) 2026/1744 delayed Annex III 16 months to Dec 2027; Colorado repealed SB 24-205; mid pay ($152–170K IAPP medians) [A/B · T0-61] | Approaching Dec 2027 EU Annex III & May 2027 India DPDP deadlines | GRC, privacy and audit professionals |
| 20 | AI Product Engineer (AI Frontend) | 54.5 | Alias family with no exact title count; dispersion from $140K startup to $315K Staff AI Frontend [A/B · T0-62] | Standardised AI-frontend ladders across product firms | Frontend/full-stack engineers (median 2 yrs exp in T0-62) |
| 21 | AI Risk, Audit & Compliance Specialist | 54.1 | Absorbed inside audit/MRM/banking; SR 26-2 Footnote 3 still excludes GenAI [A/B · T0-61] | GenAI MRM guidance and ISO 42001 audit uptake | Auditors and model-risk professionals |
| 22 | Responsible AI / AI Governance Engineer | 52.3 | Thin niche (6 core live titles globally; 5/12 sampled in India [B · T0-61]) | Harmonised technical compliance standards | MLOps and security engineers in regulated firms |
| 23 | AI Enablement Engineer | 49.0 | Skillenai 90-day count fell 57 → 42 (2026-11-05); bimodal pay ($120–180K) and temporary rollout risk [B/C · T0-62] | Durable internal AI-platform mandates | Internal tools/DevEx engineers and ops/L&D leads |
| 24 | Domain Evaluation Specialist / AI Trainer | 46.2 | Standing contract pools (Mercor 3/3), wide hourly spread ($20–300/hr), no formal interview track (`null`) [A/B · T0-66] | Transition into salaried evaluation-engineering roles | Credentialed domain experts, as a bridge into AI |

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
| Demand | 9 [8–9.5] · B | JobsPipe 2,157 global / 1,084 US / 108 UK / 90 India (re-checked 2026-11-13; static refresh caveat); Fast AI Jobs 298 at AI startups (2026-11-12, up from 227); Axial H1 2026 US 13,776 (~490/wk, C); FY2025 DOL exact-title LCAs 1,053–1,071 [T0-24, T0-27, T0-49, T0-70]. |
| Pay | 8.5 [7.5–9] · B | Levels.fyi US ML Engineer TC P25 $200K / P50 $286,958 / P75 $389,850 / P90 $497,500 (n=1,027, 2026-11-11; 1.44x US SWE); Axial posted base ceilings $180K–$300K (senior $241K, n=13,776); Meta E5 $472–497K / E6 $660–790K, Amazon L6 $401K; FY2025 LCA floor $179,982 (n=3,745) [T0-44, T0-49]. |
| Durability | 7 [5.5–8.5] · D | Judgement. Broad ML engineering spans recommendation, ranking, forecasting and LLM training/serving; API-first adoption shifts routine application work toward AI Engineer while leaving model-training, fine-tuning and scale optimisation intact [T0-49]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Owns models behind ranking, recsys, fraud and fine-tuned systems. |
| Access | 6.0 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-engineer"></a>
**#2 · AI Engineer** (`ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 10 [9–10] · B | JobsPipe 3,944 global / 1,697 US / 398 India (re-checked 2026-11-13; static vs 2026-10-19 refresh caveat); Fast AI Jobs 352 open roles at 188 AI startups (2026-11-12, up from 326; 64% of newest 50 rows customer-facing); LinkedIn Jobs on the Rise 2026 #1 [T0-01, T0-24, T0-48, T0-70]. |
| Pay | 6.5 [5.75–7.25] · B | Levels.fyi US AI Engineer TC P25 $110K / P50 $155K / P75 $212K / P90 $280K (0.54–0.56x US ML; SF Bay P50 $225K / P90 $460K; 2026-11-11); Axial US AI engineering posted base ceilings $170K–$270K (senior $213K, n=43,480; 5–12% below ML); AI/ML LCA floor $169K (n=4,459); Google within-employer check shows 62–69% of log gap is employer/level mix [T0-44, T0-48]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Title persists and leads growth, but the table-stakes layer (SDK calls, naive RAG, prompting) is commoditised [T0-03 6.4 Tier 1]; evals, agent reliability and cost engineering keep value [T0-03 Tier 2]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Ships the revenue-facing AI features; enterprise and services employer mix [T0-01 F2]. |
| Access | 7.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-forward-deployed-engineer"></a>
**#3 · Forward Deployed Engineer** (`forward-deployed-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 7.5 [6.5–8.5] · M | Fast AI Jobs FDE cluster 1,007 open roles at 353 AI startups (2026-11-12, +29% vs late Jul 779); 260–1,276 across six boards (Plank 1,276, fdejobslist 391); caveat: 23/50 newest Fast AI Jobs rows are IC FDE titles, 22 adjacent strategist/GTM roles [T0-51, T0-70]. |
| Pay | 7 [6–7.75] · B | Levels.fyi US FDE TC (2026-09-08): P25 $172K / P50 $205K / P75 $277K / P90 $350K (above US AI Engineer); Google FDE median $292K; Fast AI Jobs startup posted base median $180,656 (n=164, range $75K–$375K); international FDE beats SWE (UK GBP 139.6K, CA CA$186.3K, NL EUR 135.5K) [T0-44, T0-51]. |
| Durability | 6.5 [5–8] · D | Judgement. Customer embedding and integration judgement; risk of drift into non-coding roles (about half the cluster is non-engineering) [T0-01 F3]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Converts deployments directly into revenue and retention. |
| Access | 6.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-research-engineer"></a>
**#4 · Research Engineer / Member of Technical Staff** (`research-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–7] · B | Fast AI Jobs 223 Research Engineer roles (2026-11-12, up from 171; quorum-crossing candidate flagged for 2026-12-01 recount); AI Pulse 569 category count (C); Anthropic 670–674 total listings (>=30 RE page 1), OpenAI 822 via Epoch AI (2026-11-06) [T0-50, T0-70]. |
| Pay | 9 [8–10] · B | Frontier US posted base bands (Nov 2026): Anthropic $315K–$850K, OpenAI $205K–$555K, xAI $180K–$600K, Thinking Machines $350K–$475K, DeepMind $166K–$244K, Microsoft AI IC4–IC5; equity lifts lab TC well above $500K–$1M+ [T0-44, T0-50]. |
| Durability | 7.5 [6–9] · D | Judgement. Frontier skills (distributed training, post-training/RL infra) [T0-03 6.4 Tier 3]. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-applied-scientist"></a>
**#5 · Applied Scientist** (`applied-scientist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 6.5 [5.5–8] · B | Amazon Science listed 451 Applied Science category openings on 2026-11-13 (central estimate ~270 literally AS-titled, Wilson range 141–375); Fast AI Jobs 23 AI-startup roles (confirming Big Tech concentration); active hiring at Microsoft, Uber, Zalando, Mistral [T0-52, T0-70]. |
| Pay | 7.75 [6.75–8.75] · B | Levels.fyi Amazon Applied Scientist US TC (2026-08-18): L4 $245K, L5 $324K, L6 $407K, L7 $653K (median $306K–$335K); corroborated by Microsoft/Uber posted US bands [T0-44, T0-52]. |
| Durability | 7.5 [6–9] · C | Amazon retained 451 Applied Science openings on 2026-11-13 despite corporate headcount reductions across Oct 2025–Jul 2026; subject to Big Tech employer-cycle risk [T0-52]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. |
| Access | 5.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-applied-ai-engineer"></a>
**#6 · Applied AI Engineer** (`applied-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [4–6.5] · C | 21 of newest 50 Fast AI Jobs AI-Engineer rows (42%) on 2026-11-11 carry 'Applied AI' titles; JobsPipe has no standalone Applied AI Engineer page; strong lab/scale-up cluster (Anthropic, OpenAI, Mistral, Snorkel, Scale) [T0-53]. |
| Pay | 7.75 [6.5–8.75] · B | Levels.fyi US Applied AI Engineer TC (Nov 2026): P25 $165K / P50 $232K / P75 $340K / P90 $505K–$605K (reconciling T0-53 2026-11-11 $505K vs T0-44 2026-11-13 extract $605K); lab posted base bands $210K–$440K+ [T0-44, T0-53]. |
| Durability | 6.5 [5–8] · D | Judgement. Customer-facing technical delivery at labs and vendors. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Customer deployment and go-to-market at labs and vendors (8.5-9 anchor: directly moves revenue). |
| Access | 7.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-research-scientist"></a>
**#7 · Research Scientist (AI/ML)** (`research-scientist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5 [4–6.5] · B | JobsPipe all-fields count date 2026-09-10; Fast AI Jobs 333 open RS roles at 171 AI startups (54% Pre-Seed–Series B); ellis.com 188 OpenAI MTS/research listings; BLS 2025–35 projects +21.8% US computer & information research scientist growth [T0-27, T0-55]. |
| Pay | 9.5 [8–10] · B | Frontier posted base bands $210K–$650K+ plus major equity; Pave P6 $4.09M / M6 $4.72M equity downgraded from Grade A to Grade B (vendor intended grant value); Big Tech RS (Google/Meta/Microsoft/NVIDIA) spans $300K–$1M+ TC [T0-44, T0-55]. |
| Durability | 8 [6.5–9.5] · D | Judgement. Research taste and novel methods. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Long-horizon capability gains. |
| Access | 2.9 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-infrastructure-engineer"></a>
**#8 · AI Infrastructure / GPU Platform Engineer** (`ai-infrastructure-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4–7] · C | 52 base-disclosing postings in S09 [T0-03]; Inference Jobs 446 GPU Infrastructure Engineering listings (undeduplicated upper bound); active hyperscaler, neocloud and frontier-lab hiring [T0-54]. |
| Pay | 7 [6–8] · B | US posted-base median midpoint $261K (n=12): frontier labs/AI-native ~$360K (OpenAI $230K–$490K + equity [A], Anthropic $315K–$485K [A]) vs cloud/neocloud/enterprise $180K–$270K [T0-44, T0-54]. |
| Durability | 7.5 [6–9] · D | Judgement. Physical fleets, networking and reliability; distributed-systems minimum in top-band JDs [T0-03 J1]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Capacity, uptime and cost of the GPU estate (8.5-9 anchor: large cost line). |
| Access | 5.2 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ml-platform-engineer"></a>
**#9 · ML Platform / MLOps Engineer** (`ml-platform-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 6.5 [5.5–7.5] · B | Graduated V -> E: Axial 1,959 US MLOps postings Jan to 2026-07-13 (~70/wk steady, B); ITJobsWatch 184 UK permanent jobs citing MLOps in 6 mo (B); Fast AI Jobs 1,099 broad ML-platform/infra listings [T0-58]. |
| Pay | 6.5 [5.5–7.5] · B | Sample US posted base $150K–$357K, median midpoint $245K (n=8 senior/Big Tech, M); broader MLOps market tracks senior DevOps/SWE ($180K–$280K TC) [T0-44, T0-58]. |
| Durability | 6.5 [5–8] · D | Judgement. Platform need persists; LLMOps absorbed; fast tool churn (TGI archived, Triton renamed Dynamo Triton) [T0-03 KF6]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. |
| Access | 5.7 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-security-engineer"></a>
**#10 · AI Security Engineer / AI Red Teamer** (`ai-security-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–6.5] · B | SANS AI security job tracker (mid-Sep 2026, corroborated live 2026-11-19): >850 AI/ML security engineer postings, ~100 AI red-team (+13% WoW), 93 AI supply-chain security; queued for 2026-12-01 exact-title recount [T0-60, T0-69]. |
| Pay | 7 [5.5–8.5] · B | Dated US posted base bands: Amazon Senior AI Red Team $178.4K–$226.7K + RSUs (A), Microsoft MTS $119.8K–$234.7K (B), NVIDIA Senior AI Security Researcher $224K–$356.5K (A) [T0-60]. |
| Durability | 7.5 [6–9] · D | Judgement. Adversarial and growing surface: CVSS 9.8 serving-engine CVEs, MCP CVEs, Braintrust key breach, OWASP LLM/Agentic Top 10 [T0-03 KF12, T0-16 8, T0-14 6.8]. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 4.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-inference-engineer"></a>
**#11 · Inference / LLM Serving Engineer** (`inference-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3.5–5.5] · C | Inference Jobs 341 'Inference Engineer' listings on 2026-11-13 (upper bound; page 1 ~40% aged <=3 months); 37 verified active postings across labs, inference clouds and hardware vendors [T0-56]. |
| Pay | 7.5 [6.5–8.5] · B | Date-clean US sample (n=14) posted base median midpoint $288K (IQR $261K–$344K, bounds $165K–$500K) plus equity at labs and inference platforms [T0-56]. |
| Durability | 7 [5.5–8.5] · D | Judgement. Strong latency/cost demand balances rapid engine churn (TGI archived, TensorRT-LLM static backend removed) and emerging automated kernel-optimisation tooling [T0-56, T0-69]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Direct GPU-cost and latency leverage. |
| Access | 5.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-solutions-architect"></a>
**#12 · AI / GenAI Solutions Architect** (`ai-solutions-architect`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4–7] · C | No exact AI-SA title count yet, but strong proxies: Axial 16,927 US 'AI architecture' postings (C), JobsPipe Solutions Architect live volume and active hiring at OpenAI, Anthropic, Databricks, AWS, Microsoft, Google [T0-62]. |
| Pay | 7 [5.5–8.5] · B | Posted US base $152K–$248K+ (Google CE III $152K–$221K + bonus + equity; Databricks $180K–$248K+ OTE; lab SAs higher) [T0-62]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Enterprise integration and vendor ecosystems. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. Pre-sales and enterprise architecture (8.5-9 anchor: directly moves revenue). |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-product-manager"></a>
**#13 · AI Product Manager** (`ai-product-manager`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 6 [4.5–8] · C | JobsPipe global PM 12,166 live (2026-11-13, B); AI Pulse 570 AI PM category postings (C; flagged for 2026-12-01 recount); 41 in-window AI PM postings read across frontier labs, Big Tech and startups [T0-59, T0-70]. |
| Pay | 6.5 [5–8.5] · C | Broad PM market anchors mid-6s while frontier-lab senior bands ($240K–$490K base + equity [A]) lift the ceiling [T0-59]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Product judgement for probabilistic systems. |
| Leverage | 8 [7–9] · D | Judgement. Decides what gets built and how it is measured. |
| Access | 5.5 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-agentic-ai-engineer"></a>
**#14 · Agentic AI Engineer** (`agentic-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3.5–5.5] · C | Exact standalone title stays Watch (W): Skilark 107 'agentic'-titled listings of 28,771 (0.37%); JobsPipe agentic skill appears in 59.3% of AI Engineer postings (2026-09-10) while US product firms hire under AI Engineer [T0-57, T0-69]. |
| Pay | 6.75 [6–7.5] · C | US senior-skewed posted base midpoint median ~$197K (n=8 in-window postings in T0-57); tracks AI Engineer band rather than a separate premium [T0-57]. |
| Durability | 6.5 [5–8] · D | Judgement. Multi-step agent capabilities are rising while framework brands churn (Microsoft Agent Framework 1.0 GA 2026-04-03; AutoGen dormant); title likely merges into AI Engineer [T0-57, T0-69]. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Workflow automation value. |
| Access | 7.3 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-evaluation-engineer"></a>
**#15 · AI Evaluation Engineer** (`ai-evaluation-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [3–5.5] · B | No platform title count yet, but T0-60 documented 22 named postings across frontier labs (5), Big Tech (Microsoft >=4), eval vendors/scale-ups (7) and enterprise/services [T0-60]. |
| Pay | 7 [5.5–9] · B | Bimodal US posted base bands: Microsoft AI IC4–IC5 $119.8K–$274.8K (NYC/SF to $304.2K, A), Scale AI $179.4K–$270K (B), Transluce $310K–$500K (B) and frontier labs above $300K base + equity [T0-60]. |
| Durability | 6.5 [5–8] · D | Judgement. Adoption gap (52.4% offline / 37.3% online evals among agent teams) [T0-03 KF4] vs risk that evals stay a skill inside AI Engineer. |
| Leverage | 7.5 [6.5–8.5] · D | Judgement. Release gating and quality. |
| Access | 7.2 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-gpu-kernel-engineer"></a>
**#16 · GPU Kernel / ML Compiler Engineer** (`gpu-kernel-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4 [3–5.5] · C | CUDA/GPU kernels named in 6.6% of S09 postings (29.3% of companies) [T0-03 6.3]; River AI (GPU kernels) and AMD (Triton kernels) among T0-13's inference/kernel postings [T0-13:112, 737]. |
| Pay | 7.5 [6.5–8.5] · B | US core sample (n=17) median posted base band $190K–$287.5K (median midpoint $235.8K, IQR $217.5K–$275K); frontier labs and NVIDIA/AMD Staff/Principal reach $400K–$700K+ TC [T0-63]. |
| Durability | 6.5 [5–8] · D | Judgement. Frontier scarcity vs counter-evidence: tile DSLs (Helion, CuteDSL, CUDA Tile) and automated kernel agents abstract kernel writing [T0-03:L542, L101]; no labour data either way [T0-03:L571]. |
| Leverage | 8.5 [7.5–9.5] · D | Judgement. GPU efficiency moves a large cost line (8.5-9 anchor). |
| Access | 3.6 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-physical-ai-engineer"></a>
**#17 · Physical AI / Robotics AI Engineer** (`physical-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3–5.5] · C | Graduated W -> V: 48 in-scope postings across 38 distinct employer entries (33 named: startups, OEMs, Big Tech, frontier labs, IT services); Phase 0 Figure 'Helix' share corrected (Helix is a Figure department, not standalone volume) [T0-64]. |
| Pay | 7 [6–8.5] · B | US posted base sample (n=18) median midpoint ~$242.5K (~$235K per employer) plus equity at robotics labs and AV/humanoid firms [T0-64]. |
| Durability | 6.5 [4.5–8.5] · C | Industrial/warehouse deployments and funding growth provide upside, balanced by robotics hardware startup shutdowns and capital-intensity cycles [T0-64]. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 4.0 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-safety-researcher"></a>
**#18 · Frontier AI Safety / Alignment Researcher** (`ai-safety-researcher`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4] · C | McAleese ~600 technical FTEs (+21%/yr, C); June 2026 snapshot of 69 open roles across 8 non-lab safety orgs (6% early-career); AI Pulse 89 category count (may include trust-and-safety) [T0-60, T0-70]. |
| Pay | 7.5 [5.5–10] · B | Lab-vs-independent bifurcation: Anthropic Alignment $350K–$500K (A, COI), OpenAI Safety Systems $380K–$500K (B), DeepMind AGI Safety $174K–$300K+ vs non-profit/independent orgs $120K–$240K [T0-60]. |
| Durability | 8 [6.5–9.5] · D | Judgement. Growing research field. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 3.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-governance-lead"></a>
**#19 · AI Governance Programme Lead / Manager** (`ai-governance-lead`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4.5–6.5] · C | Axial 1,997–3,700 US AI-governance postings (K3 arithmetic fixed: 1,997 at ~71/wk implies ~28.1 wks, C); SANS ~430 AI GRC leads (mid-Sep 2026, B); GRC Careers 67 deduplicated [T0-61, T0-69]. |
| Pay | 5.5 [4.5–6.5] · B | Axial median $169K; Axial reports top-of-range figures, so typical offers are lower (C) [T0-15:162]; IAPP medians $151.8K (AI governance only), $169.7K (with privacy) (B) [T0-15:130]; manager $244K, director $268K (tops of ranges) [T0-15:417]. |
| Durability | 6 [4.5–7.5] · D | Judgement. EU Digital Omnibus (Regulation (EU) 2026/1744, in force 2026-07-27) defers Annex III high-risk duties 16 months to 2027-12-02 (Annex I to 2028-08-02), and Colorado repealed SB 24-205, moderating near-term regulatory urgency; India DPDP Phase 2/3 (2026-11-13 / 2027-05-13) sustains APAC compliance hiring [T0-61, T0-70]. |
| Leverage | 7 [6–8] · D | Judgement. Regulatory exposure (e.g., EU AI Act Art. 101 fines for GPAI providers of up to EUR 15m or 3%) [T0-15:233]. |
| Access | 4.7 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-product-engineer"></a>
**#20 · AI Product Engineer (AI Frontend)** (`ai-product-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3.5 [2.5–5.5] · C | No exact AI Product Engineer or AI Frontend Engineer title count; median stated experience is 2 years (n=6 in T0-62, dropping Phase 0 'senior-skewed' claim) [T0-62]. |
| Pay | 6.5 [4.5–8.5] · B | Wide dispersion across startup and lab tiers: Within mid $140K–$205K (B) and Staff AI Frontend $235K–$315K base (A); OpenAI ChatGPT frontend/product bands higher [T0-62]. |
| Durability | 5.5 [4–7] · D | Judgement. Agent UX is differentiated; generic UI work is exposed to code generation. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 5.8 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-risk-assurance-specialist"></a>
**#21 · AI Risk, Audit & Compliance Specialist** (`ai-risk-assurance-specialist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3.5–5.5] · B | Deloitte >=10 AI governance/risk/assurance requisitions globally, U.S. Bank >=4 AI-risk postings, plus Big 4 and banking model-risk teams [T0-61]. |
| Pay | 6 [5–7] · B | GRC Careers US AI-risk posted midpoints ~$150K–$215K (replacing unretrieved Phase 0 Deloitte $171.6K–$338.3K figure) [T0-61]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Enforcement-dependent; SR 26-2 excludes generative and agentic AI [T0-15:355]. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 4.1 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-responsible-ai-engineer"></a>
**#22 · Responsible AI / AI Governance Engineer** (`responsible-ai-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · B | Thin niche confirmed: 6 core live/in-window titles globally (Cognizant [A], SnowHeap, Experian, Accenture, Workday, Salesforce); remains Watch (W) [T0-61]. |
| Pay | 6.5 [5.5–7.5] · B | Updated US posted bands: Workday Sr RAI Systems Eng $169K–$253K (C), Salesforce Sr/Lead Applied Scientist RAI and enterprise AI engineering bands [T0-61]. |
| Durability | 6 [4.5–7.5] · D | Judgement. Regulation-driven (EU AI Act Annex III from 2 Dec 2027) with reversal risk [T0-15:72, 232]. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 5.4 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-enablement-engineer"></a>
**#23 · AI Enablement Engineer** (`ai-enablement-engineer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · B | Skillenai direct 90-day count fell from 57 (to 2026-09-03) to 42 (to 2026-11-05); small and contracting standalone title [T0-62]. |
| Pay | 5.5 [4–7.5] · C | Bimodal pay across builder vs adoption variants: Fabletics builder $160.4K–$180K base (A) vs Scotiabank adoption $120K–$140K [T0-62]. |
| Durability | 4.5 [3–6] · D | Judgement. Exact-title count fell 57 to 42; adoption/training variant tracks temporary rollout waves while platform-enablement roles fold into DevEx/IT [T0-62]. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. Internal productivity. |
| Access | 6.8 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-domain-evaluation-specialist"></a>
**#24 · Domain Evaluation Specialist / AI Trainer** (`domain-evaluation-specialist`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [3.5–7.5] · B | LinkedIn Jobs on the Rise 2026 US #4 data annotators (growth not volume, B); Mercor 3/3 full-read listings are standing pools not vacancies (A; stale 30,000 replaced by COI claim); 4/4 India postings are salaried evaluation-engineering employee roles (B) [T0-66]. |
| Pay | 3.5 [2–5] · B | Domain-segmented hourly contracts: generalist $20–$70/hr (micro1 $20–$35, Mercor $35–$70, Outlier up to $50, xAI $35–$75), professional/tech $60–$120/hr, legal/medical/finance/specialised SWE $100–$300/hr (Mercor $100–$200, Scale HFC $300); Mercor headline average unstable ($80–$141) [T0-44, T0-66]. |
| Durability | 3.5 [2–5] · D | Judgement. 'A bridge, not a destination' [T0-06:273, 650]. |
| Leverage | 5 [4–6] · D | Judgement. |
| Access | 6.1 [±1] · D | 0.5 × max + 0.5 × mean of persona scores (A.2) |

<a id="ledger-ai-engineering-manager"></a>
**L1 · AI Engineering Manager / Director of AI Engineering** (`ai-engineering-manager`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 5.5 [4–7] · B | Fast AI Jobs 608 EM roles at 239 AI startups on 2026-11-12 (+54% vs 394 in late Jul), of which 20–24% (~122–146) are AI-system EM roles; Anthropic 8/15 EM titles AI-system teams (COI); AI Pulse 68 category count (C) [T0-65, T0-70]. |
| Pay | 7.5 [6.25–9] · B | Posted US base bands: SandboxAQ $163K–$306K, NVIDIA $200K–$356.5K, Scale AI Director $285.2K–$356.5K, Anthropic $320K–$405K (A, COI; Growth EM $405K–$485K) plus equity; Levels.fyi EM anchors [T0-44, T0-65]. |
| Durability | 7 [5.5–8.5] · D | Judgement. AI-startup EM volume rose +54% (Jul–Nov 2026), offset by SignalFire 2026 management thinning and wider spans of control (~12 at tech majors, ~15 at startups) [T0-65, T0-70]. |
| Leverage | 8 [7–9] · D | Judgement. |
| Access | 4 [3–5] · M | Text-visible postings (n=8) ask 8+ years engineering and 2–6 (median 3) years managing; 0/8 name certifications; backend/SRE/devtools EMs can cross without a research background [T0-65]. |

<a id="ledger-vp-head-of-ai"></a>
**L2 · VP / Head of AI** (`vp-head-of-ai`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 3 [2–4] · C | Noisy board counts (Indeed US ~2,000, Glassdoor US 505, Indeed India 300); Axial Search tracked 65 US executive AI-engineering postings over 6 months [T0-65]. |
| Pay | 8 [6.5–9.5] · B | Posted US base bands sit below vendor studies: Accela $240K–$280K + bonus (A), SimplePractice $250K–$315K (B), Synchrony VP $170K–$290K (B); UK GBP 120K–150K (B); equity/bonus lifts late-stage/enterprise TC [T0-65]. |
| Durability | 7 [5.5–8.5] · D | Judgement. |
| Leverage | 9 [8–10] · D | Judgement. |
| Access | 2 [1–3] · D | Multi-year leadership track record. |

<a id="ledger-chief-ai-officer"></a>
**L3 · Chief AI Officer (CAIO)** (`chief-ai-officer`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · B | Rarely advertised (2 dated in-window employer postings: SBI India, UCSF Health); OMB M-25-21 (2025-04-03, A) mandates US federal agency CAIO designation but permits dual-hatted CIO/CDO/CTO; counted Fortune 500 + S&P 500 prevalence 10.7% (71/665, C) [T0-65]. |
| Pay | 8 [5–10] · B | Bifurcated pay: US public-sector/higher-ed posted base $117.7K–$200K (B) and SBI India GM & CAIO negotiable CTC up to Rs160L fixed term (B, live-verified 2026-11-19) vs private corporate executive packages $400K–$1M+ [T0-65]. |
| Durability | 5.5 [4–7] · C | Avasant reports ~2.2-year average Fortune 500 CAIO tenure (C); >=4 of 10 Oct 2026 appointments were internal/dual-hatted; IBM IBV reports only 18% hold full direct AI budget [T0-65]. |
| Leverage | 9 [8–10] · D | Judgement. |
| Access | 1.5 [0.5–2.5] · D | Executive track record. |

<a id="ledger-independent-ai-consultant"></a>
**L4 · Independent AI Consultant / Contractor** (`independent-ai-consultant`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 4.5 [3–6] · B | UK GenAI contract adverts tripled to 1,466 in 6 months to 2026-11-12 (vs 472 in 2025, 176 in 2024; 49 live LLM contracts on 2026-11-14; IT Jobs Watch, B); LinkedIn Jobs on the Rise 2026 US #2 AI consultants/strategists (growth not volume, B) [T0-66]. |
| Pay | 4 [3–5.5] · B | UK GenAI median flat at GBP 550/day (P25 GBP 460, P75 GBP 675, P90 GBP 788, n=933; live senior picks GBP 500–1,000/day, B); US agency contract postings $50–$80/hr (B); direct independent senior engagements higher [T0-66]. |
| Durability | 5 [3.5–6.5] · D | Judgement. |
| Leverage | 6.5 [5.5–7.5] · D | Judgement. |
| Access | 3 [2–4] · C | 5+ years, >=50 referral sources, 6 months of reserves [T2-01:631-635]. |

<a id="ledger-fractional-ai-leader"></a>
**L5 · Fractional Head of AI / Fractional CAIO** (`fractional-ai-leader`)

| Pillar | Score | Basis |
|---|---|---|
| Demand | 2.5 [1.5–3.5] · B | Mostly bench/network/marketplace pages: only 1 of 13 qualifying postings on an employer's own page; Go Fractional CAIO logged 10 posts in rolling 90 days (4 open; checked 2026-11-12) [T0-18, T0-66, T0-70]. |
| Pay | 4 [3–5.5] · B | Reconciled across T0-18, T0-65 and T0-66: employer-side postings $75–$150/hr (B); asking corridor $150–$250/hr (Go Fractional $205/hr & from $5K/mo C COI; Upwork $150–$195/hr C; retainers $3K–$20K/mo, T0-18 $8K–$13K/mo for 10–13 h/wk); ZipRecruiter annualised $151,203 (B noisy, hours unstated) [T0-66]. |
| Durability | 4.5 [3–6] · D | Judgement. UK GenAI contract median held flat at GBP 550/day across 2025–2026 vs GBP 625 in 2024 (B); fractional seats often convert or transition out once execution scales (C, COI) [T0-66]. |
| Leverage | 7 [6–8] · D | Judgement. |
| Access | 2 [1–3] · B | Postings stating experience ask 10+ years or 5+ years as fractional C-suite; 9 of 13 expect prior Head/VP/CTO seat; Go Fractional asks 7+ yrs and 5+ leadership/fractional (B); Fractional Jobs survey 87% 11+ yrs, 83% Director+ (C) [T0-18, T0-66]. |

### A.2 Persona access scores (inputs to the Access pillar and the persona lenses)

Scale: ≥7.5 ≈ a T2-01 ● corridor (about 6–8 months at 15–20 h/week); 4–7 ≈ ◐ (plausible but extended); <4 ≈ ○ (not plausible within 12 months; excluded from that persona's lens). Timelines come from T0-06 R2 and T2-01 §4.1 (Grade D models, conditional on success); cells without a modelled corridor are inferred from skill adjacency (Grade D).

| Role | Backend SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Researcher | Access pillar |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Machine Learning Engineer | 5.5 | 7 | 3.5 | 1.5 | 7 | 6.0 |
| AI Engineer | 9 | 7.5 | 8 | 2 | 7 | 7.9 |
| Forward Deployed Engineer | 7.5 | 4.5 | 7 | 4 | 5 | 6.6 |
| Research Engineer / Member of Technical Staff | 3 | 3 | 2 | 1 | 7.5 | 5.4 |
| Applied Scientist | 3 | 4.5 | 2 | 1 | 8 | 5.9 |
| Applied AI Engineer | 8.5 | 6.5 | 6.5 | 2 | 7 | 7.3 |
| Research Scientist (AI/ML) | 1 | 1.5 | 1 | 1 | 4 | 2.9 |
| AI Infrastructure / GPU Platform Engineer | 7 | 2.5 | 2.5 | 1 | 3.5 | 5.2 |
| ML Platform / MLOps Engineer | 7 | 5 | 4 | 1.5 | 4 | 5.7 |
| AI Security Engineer / AI Red Teamer | 5.5 | 3 | 3.5 | 2 | 4 | 4.6 |
| Inference / LLM Serving Engineer | 7 | 2.5 | 2.5 | 1 | 4.5 | 5.3 |
| AI / GenAI Solutions Architect | 6 | 4.5 | 5 | 4.5 | 4 | 5.4 |
| AI Product Manager | 4 | 4.5 | 4 | 6.5 | 3.5 | 5.5 |
| Agentic AI Engineer | 8.5 | 6.5 | 7 | 2 | 6.5 | 7.3 |
| AI Evaluation Engineer | 7 | 8 | 6.5 | 3 | 7.5 | 7.2 |
| GPU Kernel / ML Compiler Engineer | 4 | 2 | 1.5 | 1 | 4.5 | 3.6 |
| Physical AI / Robotics AI Engineer | 3.5 | 3 | 2 | 1 | 5 | 4.0 |
| Frontier AI Safety / Alignment Researcher | 2 | 2 | 1.5 | 1.5 | 4.5 | 3.4 |
| AI Governance Programme Lead / Manager | 2.5 | 3 | 2 | 6 | 3 | 4.7 |
| AI Product Engineer (AI Frontend) | 6 | 4 | 7 | 2 | 4 | 5.8 |
| AI Risk, Audit & Compliance Specialist | 2 | 4 | 1.5 | 5 | 3 | 4.1 |
| Responsible AI / AI Governance Engineer | 5.5 | 6 | 3.5 | 3 | 5.5 | 5.4 |
| AI Enablement Engineer | 7.5 | 6 | 7 | 5 | 5 | 6.8 |
| Domain Evaluation Specialist / AI Trainer | 4 | 5 | 3 | 7 | 7 | 6.1 |

### A.3 India-lens inputs

India Demand bands (live India postings): ≥300 → 10 · 150–299 → 8.5 · 75–149 → 7 · 30–74 → 5.5 · 10–29 → 4 · 1–9 → 2.5 · ≈0 → 1. India Pay anchors (TC): P50 ≥ ₹60L → 9.5 · ₹40–60L → 8 · ₹25–40L → 6.5 · ₹15–25L → 5 · < ₹15L → 3, adjusted for the P90 ceiling. Roles without India data carry wide ranges and Grade D.

| Role | India Demand | India Pay | Basis |
|---|---|---|---|
| Machine Learning Engineer | 7 [6–7.5] · B | 8 [6.75–8.5] · B | JobsPipe India 90 live of 2,157 global (4.2% M; static 2026-11-13 check); heavy GCC and big-tech presence in Bengaluru and Hyderabad [T0-49]. / Levels.fyi Greater Bengaluru ML Engineer TC (2026-11-12, n=97): P25 Rs30.3L / P50 Rs44.4L–Rs44.7L / P75 Rs65.7L / P90 Rs80.7L (down from Oct Rs94.6L); India ML/AI-focus SWE P50 Rs28.7L; Flexiple Bengaluru CTC P50 Rs19.9L (n=422, C) [T0-45]. |
| AI Engineer | 10 [9–10] · B | 5.25 [4.5–6.25] · B | JobsPipe India 398 of 3,944 global (10.1% M — correcting Phase 0 13.6% erratum; static 2026-11-13 check; consulting-heavy coverage artefact); Indian boards show 10,953–55,203 GenAI/AI keyword listings; Naukri JobSpeak AI/ML YoY +20% to +49% across 2026 [T0-25, T0-48, T0-69]. / Levels.fyi Greater Bengaluru AI Engineer TC (2026-11-12): P25 Rs13.8L / P50 Rs20.0L (variants Rs18.3L–Rs20.5L) / P75 Rs39.7L / P90 Rs60.6L; GCC 0–2 yr fixed Rs13.2L, senior Rs58–60L (C) [T0-45]. |
| Forward Deployed Engineer | 4.5 [3–6] · C | 5.5 [4–7.25] · D | Indeed India / IANS (2026-10-14) reported ~19x (1,807% YoY) growth in India FDE postings from a low base; verified Bengaluru/Hyderabad hiring at Palantir-style AI vendors and labs [T0-25, T0-51]. / No India FDE Levels.fyi title page; kept Grade D placeholder pending role-specific India TC data (top-end widened slightly to reflect Bengaluru product/lab offers) [T0-45, T0-51]. |
| Research Engineer / Member of Technical Staff | 2 [1–3] · C | 8 [6–9.5] · D | Two verified live India RE postings (Google DeepMind Bangalore, Sarvam Bengaluru); 0 RE titles on Anthropic page 1 and Microsoft AI Bengaluru (77 listings) [T0-50]. / No India evidence. |
| Applied Scientist | 5 [4–6.5] · B | 7.5 [6–9] · D | Amazon Science listed 90 India science roles (14% of 642 global) on 2026-11-13; verified postings across Amazon India and Microsoft IDC (Hyderabad/Bengaluru) [T0-52]. / Proxy: Google MLE Bengaluru L4 Rs65.2L, L5 Rs168.3L (small n) [T0-02:254]. |
| Applied AI Engineer | 4 [2.5–5.5] · C | 6 [4–8] · D | Verified active India hiring at OpenAI (Bengaluru Applied AI Engineer/Architect), Anthropic India partner/field roles and funded AI startups; no platform title count [T0-53]. / No India evidence. |
| Research Scientist (AI/ML) | 2.5 [1.5–3.5] · B | 7.5 [5.5–9] · C | JobsPipe India 3.7% (all fields, counted 2026-09-10); 9 verified India postings across DeepMind India, IBM Research India, GE Vernova, Sarvam AI and Accenture [T0-55]. / Levels.fyi Google RS India L3 Rs30.5L (2026-07-20, B; n hidden); 0 of 9 India postings disclose pay; senior/staff lab claims Rs80L–Rs1.5Cr lack methodology (C/D) [T0-55]. |
| AI Infrastructure / GPU Platform Engineer | 4.5 [3.5–6] · B | 6.5 [5–8] · D | 10 of 35 sampled postings (28.6%) in India: NVIDIA x4 (DGX Cloud, SRE research clusters), Microsoft, Oracle, CoreWeave/neocloud and GCCs [T0-54]. / No India evidence. |
| ML Platform / MLOps Engineer | 6 [5–7.5] · C | 5.5 [4.5–6.5] · C | 13 of 37 postings in India across GCCs (Walmart Global Tech, Rakuten Symphony, Aptiv) and IT services (HCLTech, Quantiphi), predominantly titled MLOps Engineer [T0-58]. / Bengaluru MLOps P50 Rs23.6L, P75 Rs41.1L, P90 Rs63.5L [T0-02:147]. |
| AI Security Engineer / AI Red Teamer | 4.5 [3.5–6] · B | 6 [4.5–7.5] · B | 9 India AI-security postings (36% of n=25 sample) across Wipro, GlobalLogic, Teamware, Backbase, Ekfrazo, Razorpay, o9 Solutions (Bengaluru/Hyderabad) [T0-60]. / Posted India pay bands found: Rs25–35L (2–5 yrs) and up to Rs50L (founding AI/ML security engineer) [T0-60]. |
| Inference / LLM Serving Engineer | 4 [3–5.5] · B | 6 [4.5–7.5] · C | 9 of 37 sampled postings (24.3%) in India across Bengaluru, Hyderabad and Gurugram (inference clouds, silicon vendors, GCCs) [T0-56]. / 1 of 9 India postings discloses pay: Rs24–36L (5+ yrs, Weekday client, 2026, B) plus adjacent senior infra/ML Bengaluru bands [T0-56]. |
| AI / GenAI Solutions Architect | 4 [3–5.5] · C | 7.5 [6–8.5] · C | JobsPipe India SA 64 live (~4% of US, B) vs Corvi 761 snapshot (C, coverage caveat); strong hyperscaler and SI hiring in Bengaluru/Hyderabad/Mumbai [T0-62]. / Upgraded from Grade D placeholder via adjacent Levels.fyi Greater Bengaluru Solution Architect (n=179) benchmark [T0-45]. |
| AI Product Manager | 5.5 [4–7] · C | 8 [6.5–9] · C | JobsPipe India share 5.3% of 12,166 global PM (~645 live PM postings, M); verified India AI PM hiring at Microsoft AI, Sarvam, Uber and product startups [T0-59]. / Upgraded from Grade D placeholder via adjacent Levels.fyi India PM (n=1,518) and Greater Bengaluru Senior PM (n=578, P50 ~Rs55–65L+) benchmarks [T0-45]. |
| Agentic AI Engineer | 4.5 [3.5–5.5] · C | 5.25 [4.5–6.25] · D | Exact 'Agentic AI Engineer' title is actively used by Indian IT services, GCCs and consultancies (6/10 India sample in T0-57) [T0-57]. / Single Cutshort India posting insufficient to upgrade; tracks Greater Bengaluru AI Engineer Levels.fyi benchmark (Rs20.0L P50) [T0-45, T0-57]. |
| AI Evaluation Engineer | 4 [3–5] · B | 5.5 [4–7] · C | Expanded beyond Backbase alone: 5 verified India postings (Glean, LogicMonitor, GlobalLogic Bengaluru; Backbase, HCLTech Hyderabad) plus 5 mirrored listings [T0-60]. / One startup posted band Rs12–36L (Ressl AI founding role, B) plus C-grade adjacent AI/LLM engineer benchmarks [T0-60]. |
| GPU Kernel / ML Compiler Engineer | 4 [3–5] · B | 6.5 [5–8] · C | 8 of 41 core postings (19.5%) in India across Bengaluru and Hyderabad: NVIDIA, AMD, Qualcomm, Sarvam AI and silicon GCCs [T0-63]. / No employer-posted India kernel band; one Bengaluru recruiter band Rs70–90L base (C) plus NVIDIA/AMD Bengaluru staff engineering bands [T0-63]. |
| Physical AI / Robotics AI Engineer | 3 [2–4] · B | 5 [3.5–6.5] · D | physicalai.jobs tracks 35 India roles (0.7% of 4,875, 2026-11-11, B); 8 India postings sampled across robotics startups, auto OEMs and IT services [T0-64]. / No India evidence. |
| Frontier AI Safety / Alignment Researcher | 1 [1–2] · C | 5 [3–8] · D | Confirmed 0 of 23 safety postings in India; Anthropic Fellows requires US/UK/Canada work authorisation with no visa sponsorship [T0-60]. / No India evidence. |
| AI Governance Programme Lead / Manager | 3.5 [2.5–5] · C | 5 [3.5–6.5] · D | Alstom (Bangalore), Eaton (Pune), EXL JDs; no India count [T0-15:95, 300-302]. / T0-15 did not use unsourced INR ranges [T0-15:469]. |
| AI Product Engineer (AI Frontend) | 2.5 [1.5–4] · C | 5 [4–6.5] · D | 2 of 16 sampled postings in India (CirrusLabs Bengaluru, Alpha remote India); no title count [T0-62]. / No India evidence. |
| AI Risk, Audit & Compliance Specialist | 3 [2–4] · C | 5 [3.5–6.5] · D | DPO/privacy demand expected to lead in India; DPDP main obligations 13 May 2027 [T0-15:142]. / No India evidence. |
| Responsible AI / AI Governance Engineer | 3.5 [2.5–4.5] · B | 4.5 [3.5–6] · D | 5 of 12 sampled postings in India across Cognizant (Chennai/Bengaluru/Hyderabad, A) and Accenture Bengaluru [T0-61]. / T0-15 deliberately did not use unsourced INR ranges [T0-15:469]. |
| AI Enablement Engineer | 2.5 [1.5–3.5] · C | 5 [4–6] · D | 2 of 15 sampled postings in India (Ather Energy Bengaluru, Siemens GCC Bengaluru); no India title count [T0-62]. / No India evidence. |
| Domain Evaluation Specialist / AI Trainer | 5 [3.5–6.5] · B | 3.5 [2–5.5] · B | 4/4 India evaluation postings in T0-66 are salaried office/hybrid evaluation-engineering roles in Hyderabad and Bengaluru (Kore.ai, BT, Backbase, HCLTech, B); remote expert-grader India volume unmeasured [T0-66]. / Global-remote micro1 $20–$35/hr (B); Outlier India coding tiers ~$13–$27+/hr (C); Alignerr states non-US rates vary (B); India salaried eval-eng postings disclose no pay [T0-66]. |

### A.4 Single-pillar leaders (IC roles, mid scores; ties shown)

- **Pay ceiling:** Research Scientist (AI/ML) 9.5; Research Engineer / Member of Technical Staff 9; Machine Learning Engineer 8.5; Applied AI Engineer 7.75; Applied Scientist 7.75; Frontier AI Safety / Alignment Researcher 7.5; GPU Kernel / ML Compiler Engineer 7.5; Inference / LLM Serving Engineer 7.5
- **Demand:** AI Engineer 10; Machine Learning Engineer 9; Forward Deployed Engineer 7.5; Applied Scientist 6.5; ML Platform / MLOps Engineer 6.5; AI Product Manager 6
- **Durability (judgement):** Frontier AI Safety / Alignment Researcher 8; Research Scientist (AI/ML) 8; AI Infrastructure / GPU Platform Engineer 7.5; AI Security Engineer / AI Red Teamer 7.5; Applied Scientist 7.5; Research Engineer / Member of Technical Staff 7.5
<!-- END GENERATED -->

---
*Ranked index maintained under the Vivechak research governance framework. Composite scores are Grade M model outputs; judgement pillars are Grade D. Pay figures carry a 90-day TTL (next review 2027-01-31); posting counts are re-verified within 31 days (next by 2026-12-03). Not legal, tax or financial advice.*
