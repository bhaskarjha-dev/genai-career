---
id: roles.hub.physical-ai-engineer
title: "Physical AI / Robotics AI Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "Physical AI / Robotics AI Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-64]
roles: [physical-ai-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Physical AI / Robotics AI Engineer

> AI for robots and physical systems: robot foundation and vision-language-action models, and sim-to-real transfer.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Embodied & Physical AI | L2 Foundation models and research; also L4 Post-training and adaptation, L6 Applications and deployment; planes: Evaluation and quality | Verified (V) | #17 of 24 | #17 of 24 · band B · Monte Carlo rank 18 (P10–P90 15–20) | B3 Robotics |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 4.5 (3–5.5) | C | Graduated W -> V: 48 in-scope postings across 38 distinct employer entries (33 named: startups, OEMs, Big Tech, frontier labs, IT services); Phase 0 Figure 'Helix' share corrected (Helix is a Figure department, not standalone volume) [T0-64]. |
| Pay | 7 (6–8.5) | B | US posted base sample (n=18) median midpoint ~$242.5K (~$235K per employer) plus equity at robotics labs and AV/humanoid firms [T0-64]. |
| Durability | 6.5 (4.5–8.5) | C | Industrial/warehouse deployments and funding growth provide upside, balanced by robotics hardware startup shutdowns and capital-intensity cycles [T0-64]. |
| Leverage | 7 (6–8) | D | Judgement. Close to customer and industrial hardware deployments (Skild, Applied Intuition, Wipro PoV, Samsung manufacturing, Siemens Energy India [T0-64 L280]). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 3 (2–4) | B | physicalai.jobs tracks 35 India roles (0.7% of 4,875, 2026-11-11, B); 8 India postings sampled across IT services (Wipro, TELUS Digital), industrial GCC-style R&D (Siemens Energy India), robotics OEM (Addverb) and startups (Origin, Upsurge Labs, Weekday client) [T0-64 L325–330]. |
| India pay | 5 (3.5–6.5) | D | No India evidence: 0 of 8 India postings disclose pay; generic ML proxies only (viral Rs22.4 LPA / 1,240 Bangalore claim is untraceable Grade E) [T0-45, T0-64 K6]. |

India rank (CCI with India inputs): #19 of 24. One input (India comp) is a Grade D placeholder.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ○ 3.5 | ○ 3 | ○ 2 | ○ 1 | ◐ 5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Robotics fundamentals, C++, Python (production), Simulation & sim-to-real, ROS, Robot learning & VLA models, PyTorch, Real-robot deployment & hardware bring-up.
- **Important (headline):** Edge inference, Teleoperation data pipelines, Safety cases, Imitation learning, Computer vision & robot perception, Reinforcement learning.
- **Full inventory:** 43 skills (Must 8 · Important 13 · Should 17 · Optional 5), each with its evidence and posting keywords: [physical-ai-engineer.md](../../03-skills-and-tech/inventories/physical-ai-engineer.md).
- **Prerequisites:** Robotics or controls background with ML
- **Credentials (tie-breakers, not skills):** NVIDIA-Certified Professional: OpenUSD Development (NCP-OUSD) (Optional: $200 (120 min, 60-70 Q, 24-mo validity); sole catalogued Physical AI/Isaac OpenUSD exam; 0/47 T0-32 JD mentions (T0-32:L197, L449, L848)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A sim-to-real or manipulation project with measured success rates and failure analysis
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P16 Sim-to-real robotics project](../../05-portfolio/project-archetypes.md#p16) (94%); [P7 Small-scale distributed training / post-training study](../../05-portfolio/project-archetypes.md#p7) (22%); [P8 Paper re-implementation with rigorous evals and a write-up](../../05-portfolio/project-archetypes.md#p8) (17%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Robot learning.** It tests real-hardware failure questions, demonstration curation, sim-to-real gaps, evaluation of rare but dangerous failures, practical coding rather than puzzles, and a presentation of past work or a design round on the employer's own robots (prep guides, C; Apptronik's knock-out application questions are employer-published, A). Source: T0-64.
- **Practise:** the [robot learning prep pack](../../08-interviewing/prep-packs.md#robot-learning-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** B3 Robotics (ML & Applied Science); headline: for robotics backgrounds only. How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** robotics, VLA, imitation learning, reinforcement learning, sim-to-real, ROS, perception
- **Leave out or reframe:** Simulation-only results presented as real-world performance
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-physical-ai-engineer).

## Specialisations inside this role

- **Robot learning and VLA models** (L2 Foundation models and research): Covered by the canonical Physical AI / Robotics AI Engineer.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Research Engineer / Member of Technical Staff](research-engineer.md) (0.17); [Machine Learning Engineer](ml-engineer.md) (0.16); [Research Scientist (AI/ML)](research-scientist.md) (0.15).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-physical-ai-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-physical-ai-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A November 2026 sample of 48 postings across 38 employer entries (12 full-text reads) shows that "Physical AI / Robotics AI Engineer" centres on training, evaluating and deploying learned robot policies (VLA models, imitation learning, reinforcement learning and sim-to-real transfer), split across **six practical variants** [M · T0-64 L45, L104–111, L125]:

| Variant | Typical employers | Primary layer and technical emphasis |
|---|---|---|
| **1. Model-centric robot learning and VLA** | Figure AI, Skild AI, Physical Intelligence, Genesis AI, NVIDIA GEAR, 1X | L2 / L4: VLA architectures (π0, GR00T, OpenVLA), diffusion/action-chunking policies, large-scale multimodal training and teleoperation datasets |
| **2. RL for locomotion and whole-body control** | Figure AI (Controls dept), Apptronik | L4: PPO/SAC, domain randomisation, reward shaping, robot dynamics and control theory, hard-real-time C++ |
| **3. Deployment and applied robotics** | Skild AI, Google DeepMind (Applied Robotics), Agile Robots, Boston Dynamics (Stretch) | L6: closing the sim-to-real gap on physical manipulators/arms (Franka, UR, Unitree), edge deployment (Jetson, TensorRT, ONNX) and failure debugging |
| **4. Industrial / enterprise physical AI** | Siemens Energy India, Samsung SDS America, Wipro | L6: digital twins, industrial MLOps, Omniverse/Isaac Sim, safety-minded validation and client-site deployment (a variant absent from Phase 0) |
| **5. Simulation, synthetic data and eval tooling** | UnitX, NVIDIA (Simulation), Boston Dynamics (Behaviour-Cloning Tools) | Simulation/data/eval plane (4/48): physics simulation (Isaac Sim/Lab, MuJoCo, Drake, ManiSkill) and collect-train-evaluate pipelines |
| **6. World models and generative physical AI** | Hedra, Laplacian Robotics | L2: action-conditioned video and world models for physical control |

By primary work layer (`n = 48`), 15 sit in L2 models/research, 16 in L4 post-training/adaptation, 13 in L6 applications/deployment, and 4 in a simulation, data and evaluation plane (reflected by the added evaluation plane on the updated card) [M · T0-64 L68, L125].

**Skill shifts revising the Phase 0 scorecard (`K9`, `K10`):**
- **Real-robot learning, Python, PyTorch and simulation are the true universal core:** Across 48 postings (`full-text n = 12` in brackets), the dominant skills are **robot learning** (`38/48`, `11/12` — promoted from Phase 0 Important to Must, noting query inflation), **real-robot deployment experience** (`26/48`, `11/12` — absent from Phase 0 and added to Must), **simulation & sim-to-real** (`22/48`, `10/12`, led by Isaac Sim/Lab and MuJoCo — including emerging GPU-accelerated bridges such as `mjlab` / MuJoCo Warp, live-verified 2026-11-19), **Python** (`18/48`, `10/12`) and **PyTorch / DL frameworks** (`15/48`, `8/12` — promoted from Phase 0 Should to Must), backed by **imitation learning** (`20/48`, `10/12`), **reinforcement learning** (`20/48`, `9/12`), **VLA models** (`24/48`, `6/12`) and **teleoperation data pipelines** (`13/48`, `6/12`) [M · T0-64 L61, L170–192].
- **C++ and ROS are variant-dependent, NOT universal Musts:** **C++** appears in only `9/48` (`19%`; `5/12` full-text; platform C++:Python ratio is 0.85 across the wider physical-AI market) and **ROS / ROS 2** in only `7/48` (`15%`; `3/12` full-text; `10%` platform-wide) [M/B · T0-64 L61, L171, L175, L201]. ROS is absent from sampled postings at Figure, Skild, Apptronik, 1X and Siemens, while hard-real-time C++ is Must for humanoid-OEM and runtime roles (1X, Apptronik) and ROS 2 stays Important for integration, deployment and IT-services variants (Wipro, Samsung, Agile Robots) [A/M · T0-64 L78, L171, L175]. Formal `safety_cases` (0/48 formal; generic safety-minded validation in 3/48), `control_systems` (13%, Must only for RL/WBC variants) and `motion_planning` (4%) sit lower than Phase 0 tiered them [M · T0-64 L179, L183–184].
- **Proof of work and ATS screens:** Employers sharply distinguish physical transfer from simulation: Figure ("real-world performance and transfer"), Samsung ("not just simulation"), Agile Robots ("beyond notebook-level prototypes") and Apptronik (deploying learned policies on legged robots or manipulators) all screen for real-robot evidence [A · T0-64 L252]. Report the exact policy family (ACT, diffusion, VLA), robot platform, simulator, trial count, measured success rate and failure taxonomy — and explicitly label any simulation-only project as simulation [P · T0-64 L77, L299–306]. Watch application forms carefully: Skild asks for 2–3 concrete projects/open-source launches, Apptronik runs knock-out questions on years of RL (5+) and legged-robot deployment (2+), and Figure discloses Greenhouse AI-powered Talent Matching on some postings [A · T0-64 L69, L251, L301].

## Employer landscape and title confusion

**Major Phase 0 correction — "Helix AI Engineer" is NOT a role alias (`K2`, `K3`):** On Figure AI's Greenhouse board (103 jobs read on 2026-11-13), `AI - Helix Team` listed 7 titles: Android, Backend, Data Infrastructure, Localization and Mapping, Perception, Training Performance and Video Pretraining — and `Helix AI Engineer, Backend` read in full was a consumer-app payments, auth and billing job [A · T0-64 L56, L387, L481]. Meanwhile, Figure's `Reinforcement Learning Engineer, Whole Body Control` sat in the Controls department *without* the Helix prefix [A · T0-64 L56, L541]. Phase 0's demand claim built on Figure Helix titles therefore overstated robot-learning demand [A/B · T0-64 L345, L387].

**Demand context and employer mix (November 2026):** The 48 postings span **38 employer entries** (27 AI-native/robotics startups, 8 enterprises/OEMs including Samsung SDS, Agile Robots, Boston Dynamics ×3, Bosch and Addverb, 5 Big Tech including NVIDIA ×3, Amazon FAR and Qualcomm, 3 IT services including Wipro and TELUS Digital, 1 frontier lab DeepMind, 1 GCC-type R&D unit Siemens Energy India, and 3 staffing/other) [M · T0-64 L152, L343]. That breadth supports moving status from Watch (`W`) toward Verified-unmeasured (`V`), while keeping role-proper volume unmeasured [M/B · T0-64 L343]. For wider market scale, `physicalai.jobs` tracks **4,875 open roles** across 115 companies on 2026-11-11 — 970 (20%) tagged Embodied AI and 291 (6%) Robotics Engineer — led by autonomy and defence employers (Shield AI 407, Tesla 329, Waymo 249, Zipline 211, Amazon Robotics 196, Applied Intuition 195, Anduril 194, NVIDIA 133, Wayve 129) [B · T0-64 L57, L131–133, L144]. OpenAI listed 21 San Francisco robotics roles on 2026-09-18 [B · T0-64 L140].

**Aliases to search instead (`K2` updated):** Exact "Physical AI" appears in only 6 of 48 titles (two of them unnamed staffing listings) [M · T0-64 L56, L312, L319]. Search by activity: *Robot Learning Engineer* / *Robotic Learning* (8/48), *Research Engineer, Robotics* (~13/48), *VLA* / *Robot Foundation Model Engineer* (5/48), *Reinforcement Learning Engineer (Whole Body Control)* (3/48) and *Embodied AI Engineer* (1/48) [M · T0-64 L75, L115–122, L344]. Drop *Autonomous Systems Engineer* as an alias: platform autonomy volume is dominated by self-driving and defence [B · T0-64 L94, L344]. Classical controls, runtime software, firmware, fleet operations and perception-only roles sit adjacent on the same boards (e.g., Physical Intelligence separates controls, runtime, ML infra and fleet roles) [A · T0-64 L112].

**Credentials and degrees:** **0 of 48 postings** name a certification [M · T0-64 L62, L259]. Of the 16 postings stating a degree, MS or PhD is required in 6 (Samsung, NVIDIA loco-manipulation summary, Wayve, Boston Dynamics Stretch, Qualcomm, Bosch), a Bachelor's is explicitly sufficient in 4 (Siemens Energy India, Apptronik Principal, Boston Dynamics tools, 1X), 4 accept equivalent experience (Skild ×2, Agile Robots, Laplacian) and 2 prefer MS/PhD [M/A · T0-64 L62, L263].

## Career path, India demand and market signals

**Seniority and entry routes:** Direct entry is narrow: **2 of 48 postings** are entry/junior (Datamentors Madeira; Upsurge Labs Bangalore 0–2 years), 11 mid, 10 senior/lead, 3 staff-plus and 22 unspecified [M · T0-64 L63, L155, L264]. **Beware non-engineering operator traps:** Figure's high-volume *Humanoid Robot Operator*, *Robot Pilot* and *Helix Data Creator* roles and Physical Intelligence's $25/hour *Robot Operator* role are shift data-collection jobs, not engineering entry routes [A · T0-64 L270; live-confirmed 2026-11-19]. Realistic engineering paths: PhDs directly into lab/research-engineer titles; backend/DevOps/SRE engineers via deployment, build/release or simulation-tooling roles (Skild deployment/test, Physical Intelligence build/release); data scientists via perception, data curation and evaluation; and new graduates via junior startup/research-engineer roles backed by open-source real-robot work [D · T0-64 L266–272].

**Progression and capital-cycle durability (`K7` updated):** IC ladders reach Staff and Principal (Apptronik Principal, Boston Dynamics Staff, Qualcomm Sr Staff/Principal, Tesla P2–P4), with exits into Research Scientist, Lead/Head of Physical AI or startup founding roles [A/B/C · T0-64 L276–277]. Durability is **strongly employer-dependent** as of November 2026: large H1 2026 funding (vendor-quoted Crunchbase: $18.8B robotics startups / $47.4B broader physical AI [C, COI]) and enterprise customer deployments support the upside, while **hardware startup shutdowns (K-Scale Labs — live-confirmed 2026-11-19 after failing to close a Series A despite $2M in preorders — and Cartwheel Robotics), cooling China embodied-AI fundraising from autumn 2026, and small-firm financing gaps** widen downside risk [B/C · T0-64 L65, L143, L278].

**Pay signals, geography and export-control traps:** Full pay tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). Closing the Phase 0 "no pay data" gap (`K4`), T0-64's 18 US postings with bands give a median midpoint of **~$242.5K** (~$235K at one value per employer, `n = 11`; IQR ~$201K–$279K) [M · T0-64 L59, L207–208]. **Watch employer-wide band conventions:** Figure's $200K–$400K band appears identically on Robot Learning, Modeling, Perception and non-ML Backend Payments, and Skild's $100K–$300K appears on Research, ML and Test; narrower role-specific bands sit lower (Boston Dynamics behaviour-cloning tools $135K–$170K; Relari $125K–$175K + equity), while 1X posts $166.6K–$350K, NVIDIA senior $148K–$356.5K, OpenAI robotics $255K–$325K SWE / $380K–$500K ML pipeline, and total compensation at large payers sits much higher (Tesla ML Engineer median $380K TC; Figure company-wide median $380.7K TC on Levels.fyi) [A/B/C · T0-64 L59–60, L209–226]. Geographically, **77% of tracked roles are in the US** (3,745 of 4,875: Mountain View, Sunnyvale, SF, Seattle, Austin, Santa Clara), followed by UK (153), Germany (148; Munich/Zürich/London in Europe) and Japan (79), with **only 4% remote** both on the platform and in the sample due to physical hardware access [B/M · T0-64 L58, L134–135, L284–285]. On US sponsorship (pointers, not legal advice; verify in [visa and relocation](../../11-tracks/visa-and-relocation.md)): Figure (26 LCAs in 2025, 16 in 2026), Skild (15 in 2025) and Field AI (30 certified in 2026) file H-1B LCAs routinely (filings are not pay) [B · T0-64 L60, L288–293], **but Apptronik restricts applicants to US persons (citizens, permanent residents or protected individuals) due to export-controlled data**, and another consumer-robotics startup states no sponsorship [A/B · T0-64 L60, L295, L390].

**India demand and nuance (revising Phase 0 "No India evidence"):** India demand exists but is small: `physicalai.jobs` tracks **35 India roles** (0.7% of 4,875), Corvi Careers shows 32 robotics roles in Hyderabad (all robotics, 2026-07-05), and T0-64 samples **8 India postings** across **IT-services labs** (**Wipro** `Physical AI Engineering Lead`, Bengaluru — live-verified 2026-11-19 under Wipro Innovation Network Labs, plus TELUS Digital and an unnamed firm), a **GCC-style R&D unit** (**Siemens Energy India** `AI Engineer – Physical AI & Digital Twin Systems`, Bengaluru/Gurugram/Pune, 2–5 years, industrial MLOps/digital twins), a **robotics OEM** (**Addverb** `Robot AI Researcher`), and **startups** (**Origin**, **Upsurge Labs** 0–2 years, a Weekday client) [A/B/C · T0-64 L66, L324–330]. Ignore the viral "1,240 Bangalore robotics openings / ₹22.4 LPA" blog claim — it is untraceable (Grade E) [E · T0-64 L66, L372]. **India pay remains unmeasured (`K6`):** 0 of 8 India postings disclose pay, leaving only generic ML engineer proxies (see [pay benchmarks](../../09-compensation/pay-benchmarks.md)) [D · T0-64 L227–229, L332, L348].

## Interview themes and preparation notes

T0-64 closed Phase 0's "No interview-track evidence" gap, grounding the dedicated **Robot learning** interview pattern rather than a generic LLM-engineer loop [A/B/C · T0-64 L64, L237–247]:
- **Employer formats:** **1X Technologies** lists a three-step loop (introductory → talent acquisition → hiring manager/senior technical) [B · T0-64 L242]. Secondary guides (partly reconstructed, C) describe **Skild AI** splitting research (past-work presentation plus RL/IL generalisation) from engineering (real-hardware failure debugging); **Figure AI** running fast loops (~2 weeks) with take-homes or presentation case studies and design rounds tied to Figure's own robots; **Physical Intelligence** prioritising practical coding over algorithmic puzzles plus hands-on robot/teleop depth; **Apptronik** pairing application knock-out questions [A] with live discussions of demonstration curation, evaluating policies that rarely fail but fail dangerously, and sim-to-real gaps [C]; and **Nimble Robotics** running 4 rounds with a take-home [C · T0-64 L239–245].
- **Preparation focus (no model answers, per D-018):** Be ready to dissect real-hardware failure modes, demonstration-data quality bugs, sim-to-real discrepancies, safety/recovery boundaries and practical Python/C++ systems code rather than LeetCode-only drills [C · T0-64 L247]. Pair this with [interview loops](../../08-interviewing/interview-loops.md) and the [robot learning prep pack](../../08-interviewing/prep-packs.md#robot-learning-pack). No employer AI-tool interview policy or India-specific robotics loop evidence was found [E · T0-64 L333, L364].

## Dossier evidence and limits

- **Freshness and cache caveat (major limit):** Although 48 postings were sampled (12 full-text reads), **only 4 of 48 (8%) carry explicit posting dates inside the 90-day window** (Applied Intuition, Wipro, Weekday client, Laplacian) [M · T0-64 L67, L160]. Greenhouse, Ashby, Siemens and 1X pages omit posting dates, and the fetch tool can serve cached copies of unknown age (Figure's Robot Learning and Modeling pages loaded as open when a later board listing omitted them; a live DeepMind London page still showed a 2025-05-21 deadline) [A/M · T0-64 L49, L67, L388–389]. Always check live employer boards and set board alerts rather than relying on mirrors [T0-64 L76].
- **Epistemic audit (Extract-only Grade A rows):** Five T0-64 ledger rows (S3, S5, S10, S11, S12) were labelled Grade A despite Extract-only access; under sceptical review these are treated as Grade B.
- **Query bias and COI:** Queries explicitly targeted VLA, robot-learning and Physical AI terms, over-representing model-centric VLA roles and under-sampling classical ROS/C++ integration roles [T0-64 L46, L379]. COI disclosures apply to recruiting vendor HeroHunt (S52), sponsored partner content Ohio Tech News (S53) and résumé vendor ResumeGeni (S14) [T0-64 L143, L255, L382].
- **Explicit absences (not measured as of 2026-11-13):** role-proper volume isolated from wider physical AI; monthly posting time series since 2025; India posted pay and classic GCC robot-learning pay; full-text reads of staff-plus postings (all 3 were mirrors); AI-tool policies in robotics loops; named hiring-manager proof statements; published analyses of prior roles hired; Levels.fyi robot-learning titles at Physical Intelligence, Skild or 1X; NVIDIA Workday and blocked DeepMind 7543224 pages; and systematic Japanese, Chinese and German sampling [E · T0-64 L359–373].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
