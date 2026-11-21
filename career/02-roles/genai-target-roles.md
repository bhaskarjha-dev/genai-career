---
id: roles.genai-targets
title: "GenAI Target Roles: The Sorted Shortlist"
content_type: guide
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-06
summary: "Which GenAI roles to target, in order: a sorted shortlist from a consensus of eight lenses restricted to GenAI demand, with the tier rules, one line per role, and a method for choosing one cluster, its top title and two adjacent titles."
sources: [T0-01, T0-02, T0-03, T0-04, T0-06, T0-14, T0-15, T0-17, T0-18, T0-44, T0-45, T0-48, T0-49, T0-50, T0-51, T0-52, T0-53, T0-54, T0-55, T0-56, T0-57, T0-58, T0-59, T0-60, T0-61, T0-62, T0-63, T0-64, T0-65, T0-66, T0-69, T0-70]
roles: [all]
geos: [global, india]
tags: [target-roles, shortlist, genai, ranking, tiers, clusters, persona, india]
---
# GenAI Target Roles: The Sorted Shortlist

> Which GenAI roles to target, in order: a sorted shortlist from a consensus of eight lenses restricted to GenAI demand, with the tier rules, one line per role, and a method for choosing one cluster, its top title and two adjacent titles.

**Dates and grades.** The order is computed by `scripts/target_roles.py` from [data/role_scores.json](../../data/role_scores.json) (data as of 2026-11-19). Its GenAI restriction uses JobsPipe posting counts and shares re-checked on 2026-11-13 (underlying skill-share count date 2026-09-10 [T0-69]) and Skillenai counts as of 2026-11-05, so this page is due for re-verification by 2026-12-06 (31 days from oldest count source, EGP-1.0 class V1). Grades follow EGP-1.0 ([CONTRIBUTING §3](../../CONTRIBUTING.md#3-writing-standard-egp-10-in-brief)): A is a primary source or measured data; B an established secondary source or a sizeable platform dataset; C third-party analysis, a vendor report or a single source, always attributed; D judgement; M a model output, which inherits the weakest grade among its inputs; P practice-curated. The order itself is Grade M.

**Scope.** GenAI work only. Classic-titled roles (ML Engineer, Applied Scientist, Research Scientist) are included through their GenAI track. The [role rankings](role-rankings.md) score all demand for each title instead, which is why their #1 is ML Engineer and this page's #1 is AI Engineer.

## The short answer

1. **Start with AI Engineer or the GenAI track of ML Engineer.** They are the only Tier 1 roles: both average under 2.5 across all eight lenses [M]. Counting only postings that name LLM, AI Engineer has about 2.7× the US postings of ML Engineer (~1,302 vs ~488) [M · JobsPipe, 2026-09-10 count]; ML Engineer pays more, and 62–69% of the log title gap at Google is employer and level mix ([pay benchmarks](../09-compensation/pay-benchmarks.md#united-states-bands-by-title-and-city)) [B/M · T0-48].
2. **Take a Tier 2 role only if you can pass its gate.** Applied Scientist (#3) has direct Big Tech volume (Amazon Science 451 Applied Science openings, 90 in India as of 2026-11-13 [B · T0-52]) and Amazon TC benchmarks; FDE (#4) has Levels.fyi US TC ($205K P50, above AI Engineer [B · T0-44]) and India TC (₹16.75L–17.7L P50 [B · T0-51]) but involves customer travel; Research Engineer / MTS (#5) requires a PhD-level profile, fellowship or strong OSS; Applied AI Engineer (#6) carries a lab-tier bar ($200K P25 / $250K P50 / $475K P75 / $505–605K P90 [B · T0-44, T0-53]).
3. **Carry agents, evals or inference as your edge, not as your only title.** Agentic AI is named in 59.3% of AI Engineer postings [B · T0-01.F4], while Agentic AI Engineer (#14) stays on the catalog's [watchlist](role-catalog.md#54-watchlist-against-the-graduation-tests) after failing three graduation tests [T0-57]. Build one of them inside a Tier 1 or Tier 2 title.
4. **Pick one cluster, aim at its top title, and apply to two adjacent titles in the same cluster with the same portfolio** [D]. The five clusters are under [How to do it](#target-clusters-one-skill-stack-several-titles).
5. **Leave leadership and independent tracks until you meet their entry conditions.** People reach them after years of experience, so they are ranked separately, L1–L5 [D · role rankings §1.1].
6. **Read the order as a model output, not a measurement.** Within a tier, differences sit inside uncertainty bands. Research Engineer / MTS, AI Security Engineer, AI Product Manager and AI Solutions Architect are the roles most likely to shift at the 2026-12-01 recount [M].

<a id="0-the-sorted-target-list"></a>
## At a glance: the sorted target list

| # | Target role (GenAI track) | Tier | Consensus rank (mean of 8 lenses) | Lens range (best–worst) | GenAI centrality | Evidence confidence | Best for |
|:---:|---|:---:|:---:|:---:|---|:---:|---|
| 1 | [**AI Engineer**](hubs/ai-engineer.md) | 1 | 2.3 | 1–6 | Core (LLM named in 76.7% of postings) | High | Backend, frontend/full-stack, data scientists, India |
| 2 | [**Machine Learning Engineer, GenAI/LLM track**](hubs/ml-engineer.md) | 1 | 2.4 | 2–3 | Mixed: target the 45% of postings that name LLM | High | Data scientists, PhDs, ML-leaning backend engineers |
| 3 | [**Applied Scientist, GenAI/LLM teams**](hubs/applied-scientist.md) | 2 | 4.1 | 3–5 | Mixed: target LLM teams | High | PhDs, applied ML researchers, Amazon/Microsoft/Uber tracks |
| 4 | [**Forward Deployed Engineer (AI)**](hubs/forward-deployed-engineer.md) | 2 | 4.4 | 2–9 | Core (AI-startup cluster) | Medium | Backend/full-stack engineers who like customers and travel |
| 5 | [**Research Engineer / Member of Technical Staff**](hubs/research-engineer.md) | 2 | 4.4 | 1–10 | Core (frontier labs) | High | PhDs, fellowship alumni, strong OSS contributors |
| 6 | [**Applied AI Engineer**](hubs/applied-ai-engineer.md) (labs and AI vendors) | 2 | 6.0 | 4–8 | Core | Medium | Backend engineers, PhDs |
| 7 | [**AI Infrastructure / GPU Platform Engineer**](hubs/ai-infrastructure-engineer.md) | 3 | 7.6 | 5–10 | Majority (GPU clusters for training and inference) | Medium | SRE, DevOps, backend infrastructure |
| 8 | [Research Scientist, LLM research](hubs/research-scientist.md) | 4 | 8.8 | 3–16 | Mixed: target LLM / RL / post-training research | High | PhDs with publications |
| 9 | [ML Platform / MLOps (LLMOps) Engineer](hubs/ml-platform-engineer.md) | 4 | 9.5 | 6–14 | Majority | High | DevOps, SRE, backend; India GCCs |
| 10 | [AI Security Engineer / AI Red Teamer](hubs/ai-security-engineer.md) | 4 | 10.9 | 9–14 | Core (LLM and agent security) | High | Application-security and offensive-security engineers |
| 11 | [Inference / LLM Serving Engineer](hubs/inference-engineer.md) | 4 | 11.0 | 9–13 | Core | Medium | Systems/C++ engineers; backend engineers with infrastructure depth |
| 12 | [AI / GenAI Solutions Architect](hubs/ai-solutions-architect.md) | 4 | 12.0 | 7–15 | Majority | Medium | Senior engineers, cloud architects, consultants |
| 13 | [AI Product Manager](hubs/ai-product-manager.md) | 4 | 12.0 | 4–16 | Majority | Medium | Experienced PMs; the best non-engineering target |
| 14 | [Agentic AI Engineer](hubs/agentic-ai-engineer.md) | 4 | 12.1 | 7–14 | Core | Medium | Backend and distributed-systems engineers; India GCC/services titles |
| 15 | [AI Evaluation Engineer](hubs/ai-evaluation-engineer.md) | 4 | 13.0 | 9–15 | Core | High | Backend engineers, data scientists, PhDs |
| 16 | [GPU Kernel / ML Compiler Engineer](hubs/gpu-kernel-engineer.md) | 5 | 16.6 | 15–19 | Majority | Medium | CUDA/Triton/C++ systems engineers, PhDs |
| 17 | [Physical AI / Robotics AI Engineer](hubs/physical-ai-engineer.md) | 5 | 17.8 | 17–19 | Adjacent (robot foundation / VLA models) | Medium | Robotics and controls engineers with ML |
| 18 | [AI Governance Programme Lead / Manager](hubs/ai-governance-lead.md) | 5 | 18.3 | 16–21 | Majority | Medium | GRC, privacy and audit professionals |
| 19 | [Frontier AI Safety / Alignment Researcher](hubs/ai-safety-researcher.md) | 5 | 19.0 | 14–24 | Core | Medium | PhDs, fellowship alumni (US/UK/CA work auth) |
| 20 | [AI Product Engineer (AI Frontend)](hubs/ai-product-engineer.md) | 5 | 19.6 | 17–21 | Core | Medium | Frontend/full-stack engineers building streaming AI UX |
| 21 | [AI Risk, Audit & Compliance Specialist](hubs/ai-risk-assurance-specialist.md) | — | 21.1 | 19–23 | Adjacent (SR 26-2 excludes GenAI) | High | Not a primary GenAI target |
| 22 | [Responsible AI / AI Governance Engineer](hubs/responsible-ai-engineer.md) | — | 21.4 | 18–23 | Majority | High | Not a primary GenAI target |
| 23 | [AI Enablement Engineer](hubs/ai-enablement-engineer.md) | — | 22.6 | 20–24 | Core (contracting title count) | Medium | Internal DevEx/ops leads; not a primary standalone target |
| 24 | [Domain Evaluation Specialist / AI Trainer](hubs/domain-evaluation-specialist.md) | — | 23.4 | 21–24 | Core | High | A bridge, not a destination |

Leadership and independent tracks are ranked separately: L1 AI Engineering Manager / Director, L2 VP / Head of AI, L3 CAIO, L4 Independent AI Consultant, L5 Fractional Head of AI ([when to target them](#leadership-and-independent-tracks-when-to-target-them)).

**How to read the table.** Tier, consensus rank and lens range are model outputs [M], checked against the data by `python3 -B scripts/target_roles.py --check`. GenAI centrality follows the filter below. Evidence confidence follows the [role rankings' rule](role-rankings.md#14-evidence-confidence): High when demand and pay both rest on A or B evidence, Low when either rests on judgement or a proxy.

## How the order is computed: a GenAI filter, eight lenses and five tiers

The order takes the 24 individual-contributor roles of the [role catalog](role-catalog.md), scored on five pillars in data/role_scores.json, and applies four steps. Every step is reproducible with `python3 -B scripts/target_roles.py`, which reuses the functions, fixed seed and data file of [scripts/rank_roles.py](../../scripts/rank_roles.py).

### 1. The GenAI-domain filter: four classes

All 29 canonical roles in the catalog touch GenAI, so none was removed. Each individual-contributor role is labelled by how central GenAI is to its work.

| Class | Roles | Basis |
|---|---|---|
| **Core**: the work *is* building, deploying, evaluating, securing or researching LLM / foundation-model systems | AI Engineer, Applied AI, Agentic, FDE (AI-startup cluster), Research Engineer/MTS, Inference, AI Evaluation, AI Security, AI Safety, AI Product Engineer, AI Enablement, Domain Evaluation | AI Engineer: LLM named in 76.7% of postings [B · JobsPipe JD]. Other roles: scope as defined in the catalog |
| **Majority**: GenAI drives most of the work, but the title also covers other ML | AI Infrastructure, GPU Kernel, ML Platform/MLOps, AI PM, AI Solutions Architect, AI Governance Lead, Responsible AI Engineer | Catalog scope [D] |
| **Mixed**: you must target the GenAI track | ML Engineer, Research Scientist, Applied Scientist | LLM is named in 45.0% of MLE postings and 24.4% of all-field research-scientist postings [B · JobsPipe JD]. Applied Scientist: share unmeasured [D] |
| **Adjacent**: related to GenAI but not centred on it | Physical AI, AI Risk/Audit/Compliance | Robot foundation models (Physical AI). SR 26-2 excludes generative and agentic AI, so GenAI risk has no settled owner [B · T0-15] (AI Risk) |

<a id="12-genai-restriction-of-the-two-mixed-title-families"></a>
### 2. The GenAI restriction of the two mixed title families

The catalog counts every AI Engineer and ML Engineer posting, including robotics, construction, recsys, ads and autonomous-vehicle work. For a GenAI target list only the GenAI subset matters. The share of postings that name LLM serves as the GenAI share; it is a lower bound, because some GenAI postings say "generative AI" without naming LLM.

| Role | Catalog count (US / India) | Postings naming LLM | GenAI subset (US / India) [M] | Demand score: catalog → GenAI | India demand: catalog → GenAI |
|---|---|:---:|---|:---:|:---:|
| AI Engineer | 1,697 / 398 [B · JobsPipe] | 76.7% | ~1,302 / ~305 | 10 → 9 | 10 → 10 |
| ML Engineer | 1,084 / 90 [B · JobsPipe] | 45.0% | ~488 / ~41 | 9 → 7 | 7 → 5.5 |

The restricted ranges and their arithmetic are recorded in data/role_scores.json (`genai_demand` and `genai_india_demand`, Grade M) and are used only for this order. No other input changes: the other roles are already scored on GenAI evidence (frontier labs, AI startups or LLM-specific titles).

**Effect on the scores** [M]:
- The GenAI CCI is AI Engineer 73.8, ML Engineer 72.9, FDE 71.8, Research Engineer 71.4 and Applied Scientist 70.7.
- In the Monte Carlo (20,000 draws), AI Engineer is #1 in 43% of draws, ML Engineer in 25%, Research Engineer in 13%, FDE in 10% and Applied Scientist in 7%. Without the restriction, ML Engineer leads instead ([role rankings §0](role-rankings.md#0-the-answer)).
- The conclusion holds even if ML Engineer's true GenAI share were 60%: that is ~650 postings (band 8), still below AI Engineer's band 9.

### 3. Consensus across eight lenses

A role's target position is its **mean rank across eight lenses**, each weighted equally. Ties are broken by GenAI CCI.

| Lens | What it rewards |
|---|---|
| Base weights (25/25/20/15/15) | Balanced: demand, pay, durability, leverage, access |
| Equal weights | No pillar favoured |
| Pay-max | Pay (40%) |
| Hiring-safety | Demand (40%) |
| Moat-first | Durability of the work (40%) |
| Switcher | Ease of entry (35% Access) |
| India lens | India postings and India pay replace the US inputs |
| Monte Carlo median | Robustness to uncertainty in every input |

The lens range in the table shows the best and worst position a role takes across the eight lenses. A narrow range means a robust target.

<a id="14-tier-rules"></a>
### 4. Tier rules

| Tier | Rule | Meaning |
|:---:|---|---|
| 1 | Mean ≤ 2.5 and top 6 in all eight lenses | Primary targets |
| 2 | Mean ≤ 6.5 and top 10 in at least seven lenses | High-value targets with an entry gate |
| 3 | Mean ≤ 8 and top 10 in at least six lenses | Strong specialist targets |
| 4 | Mean ≤ 14 | Solid targets for specific backgrounds, or specialisations to carry inside a Tier 1 title |
| 5 | Mean ≤ 21 | Niche or conditional targets |
| — | Mean > 21 | Not recommended as a primary GenAI target |

## How to do it

Choose a cluster before you choose a title: one portfolio then serves three applications [D].

1. **Choose one cluster.** Read the five [target clusters](#target-clusters-one-skill-stack-several-titles) and pick the one whose shared core skills you hold, or can build within your timeline ([career transitions](../11-tracks/career-transitions.md)). *Done when:* you have named one cluster and listed which of its shared core skills you already hold.
2. **Make the cluster's top reachable title your primary target.** Read its line in [the 24 roles](#the-24-roles-one-line-each) and its hub, and check the gate. *Done when:* your primary target is one canonical title, and you meet its gate or have a dated step that will.
3. **Add two adjacent titles from the same cluster.** The cluster table's last column shows what each title adds to the shared stack. *Done when:* you have two adjacent titles, and one portfolio covers the proof that all three hubs ask for.
4. **Check your background and location.** Find your row in [best targets by background](#best-targets-by-background); if you search in India, read the [India-first order](#india-the-india-first-order). *Done when:* each of your three titles appears in your background row, or you have written down why not, and for an India search each sits in the India top 12.
5. **Write the shortlist down and set a recount date.** Record it in the [targeting workbook](../00-start/targeting-workbook.md) (its long-list and shortlist steps). *Done when:* the workbook holds your three titles with their gates, and a re-read after the 2026-12-01 recount is in your calendar.

<a id="7-target-clusters-one-skill-stack-several-titles"></a>
### Target clusters: one skill stack, several titles

The efficient strategy is to pick one cluster, aim at its top title, and apply to two adjacent titles in the same cluster with the same portfolio [D].

```mermaid
flowchart LR
    subgraph APP["Applied GenAI stack"]
        AIE["1 · AI Engineer"]
        FDE["4 · FDE"]
        AAI["6 · Applied AI Engineer"]
        AGE["14 · Agentic AI Engineer"]
        EVAL["15 · AI Evaluation Engineer"]
    end
    subgraph MODEL["Model stack"]
        MLE["2 · ML Engineer, GenAI track"]
        AS["3 · Applied Scientist"]
    end
    subgraph FRONT["Frontier research stack"]
        RE["5 · Research Engineer / MTS"]
        RS["8 · Research Scientist"]
        SAFE["19 · AI Safety Researcher"]
    end
    subgraph SYS["Systems & security stack"]
        INFRA["7 · AI Infrastructure"]
        PLAT["9 · ML Platform / MLOps"]
        SEC["10 · AI Security Engineer"]
        INF["11 · Inference Engineer"]
        KER["16 · GPU Kernel"]
    end
    subgraph PROD["Product and governance"]
        SA["12 · AI Solutions Architect"]
        PM["13 · AI Product Manager"]
        GOV["18 · AI Governance Lead"]
    end
    AIE ---|evals, serving literacy| MLE
    MLE ---|distributed training, post-training| RE
    AIE ---|cost and latency engineering| INF
    INF ---|lab infrastructure rounds| RE
    AIE ---|customer scoping| SA
```

| Cluster | Shared core skills | Titles (target #) | What each title adds |
|---|---|---|---|
| **Applied GenAI** | Production Python/TypeScript, LLM APIs and tool calling, retrieval quality, evals, agent reliability, observability and cost | AI Engineer (1), FDE (4), Applied AI (6), Agentic (14), AI Evaluation (15); also AI Solutions Architect (12), AI Product Engineer (20), AI Enablement (23) | FDE: customer scoping and enterprise integration. Applied AI: customer delivery at labs. Agentic: durable execution and MCP. Evals: statistics and judge calibration |
| **Model** | ML and statistics depth, PyTorch, fine-tuning judgement, eval statistics, serving literacy | ML Engineer (2), Applied Scientist (3) | Applied Scientist: research-to-production and causal / A-B methods. MLE: serving and small-budget training evidence |
| **Frontier research** | PyTorch internals, distributed training, post-training/RL, evals at scale | Research Engineer/MTS (5), Research Scientist (8), AI Safety (19) | Research Scientist: publications. Safety: alignment and interpretability |
| **Systems & security** | Kubernetes, GPU scheduling, serving engines, KV cache, profiling, red-teaming | AI Infrastructure (7), ML Platform (9), AI Security (10), Inference (11), GPU Kernel (16) | Inference: engine internals. Platform: MLOps lifecycle. Security: prompt-injection, red-teaming, AppSec. Kernel: CUDA/Triton |
| **Product and governance** | Product sense, eval rubrics, regulation literacy, stakeholder communication | AI Solutions Architect (12), AI PM (13), AI Governance Lead (18) | Solutions Architect: cloud reference architectures. Governance: EU AI Act, NIST, ISO 42001 |

<a id="3-tiers-45-at-a-glance"></a>
### The 24 roles, one line each

One line per role, in target order. Each role's hub holds its numbers, skills, proof, interview track and résumé pointers, each with its grade. Gates and risks below are the catalog's readings (judgement, D) unless a grade is shown.

1. **[AI Engineer](hubs/ai-engineer.md)** (Tier 1, core): aim for AI Engineer, GenAI Engineer or Developer, LLM Engineer and Full-Stack AI Engineer postings; no formal gate; stay above commoditised wrapper work through evals, retrieval quality, agent reliability and cost and latency engineering.
2. **[Machine Learning Engineer, GenAI track](hubs/ml-engineer.md)** (Tier 1, mixed): filter for postings that name LLM work (fine-tuning, LLM inference, embeddings, LLM evals), because much ML Engineer hiring is recsys, ads and autonomous vehicles; gate: ML maths and statistics plus production engineering.
3. **[Applied Scientist, GenAI/LLM teams](hubs/applied-scientist.md)** (Tier 2, mixed, high confidence): Big Tech's research-to-production title on LLM teams (Amazon Science 451 openings, 90 in India; Levels.fyi Amazon AS TC $245K–$653K [B · T0-52]); gate: production ML + coding (Amazon uses PhD or Master's+4; Microsoft and Uber open BS/MS routes).
4. **[Forward Deployed Engineer (AI)](hubs/forward-deployed-engineer.md)** (Tier 2, core): apply to the IC engineer-titled roles in the cluster (23/50 newest Fast AI Jobs rows [B/M · T0-51, T0-70]); new Levels.fyi US TC ($205K P50 / $350K P90) sits above AI Engineer [B · T0-44]; gate: customer-facing work and travel; protect engineering scope from pre-sales drift.
5. **[Research Engineer / Member of Technical Staff](hubs/research-engineer.md)** (Tier 2, core): frontier-lab titles for post-training, RL, training infrastructure and evals at scale (223 on Fast AI Jobs, quorum-crossing candidate [B · T0-70]); gate: strong systems/ML profile, fellowship or OSS (vLLM, SGLang; only 1/18 T0-50 JDs required a PhD); senior pay is heavily stock-weighted (semi-liquid private equity at OpenAI/xAI vs newly public `ANT` at Anthropic on 2026-11-19 with staggered lock-ups [A/B · U52]).
6. **[Applied AI Engineer](hubs/applied-ai-engineer.md)** (Tier 2, core): customer- and solutions-facing LLM engineering at labs and AI vendors (21/50 newest Fast AI Jobs AI rows; Levels.fyi US TC P25 $200K / P50 $250K / P75 $475K / P90 $505–605K [B · T0-44, T0-53]); gate: lab-tier bar plus customer scoping and evals.
7. **[AI Infrastructure / GPU Platform Engineer](hubs/ai-infrastructure-engineer.md)** (Tier 3, majority): GPU clusters, fabrics and storage (US posted base median midpoint $261K, labs ~$360K; 10/35 sampled in India [A/B · T0-54]); gate: Kubernetes, Slurm, networking and SRE depth.
8. **[Research Scientist, LLM research](hubs/research-scientist.md)** (Tier 4, mixed): LLM, post-training, RL, reasoning or interpretability research; gate: PhD plus top-venue publications (NBER WP 34964 confirms +63% top-firm move probability [B · T0-55]); frontier offers are "not plannable" [D · T0-06], and it falls to #16 for switchers.
9. **[ML Platform / MLOps (LLMOps) Engineer](hubs/ml-platform-engineer.md)** (Tier 4, majority): graduated to Established (`E`: Axial 1,959 US MLOps, ITJobsWatch 184 UK perm, Fast AI Jobs 1,099 [B · T0-58]); strongest in DevOps/SRE and India GCCs.
10. **[AI Security Engineer / AI Red Teamer](hubs/ai-security-engineer.md)** (Tier 4, core): rose sharply on SANS's >850 AI/ML security postings (~100 red-team, 93 supply-chain [B · T0-60, T0-69]), dated US bands ($178–431.25K) and 9 India roles (₹25–50L); gate: AppSec/offensive security plus prompt-injection and red-teaming depth.
11. **[Inference / LLM Serving Engineer](hubs/inference-engineer.md)** (Tier 4, core): strong US posted base ($288K median midpoint, n=14; 9/37 sampled in India [B · T0-56]); gate: vLLM/SGLang/TensorRT-LLM, KV-cache/batching and systems depth; smaller title volume (Inference Jobs 341 upper bound).
12. **[AI / GenAI Solutions Architect](hubs/ai-solutions-architect.md)** (Tier 4, majority): hyperscalers, labs, AI vendors and SI/partner channels (US posted base $152–247.5K, Databricks range is "Local Pay Range" not OTE [B · T0-62]; Bengaluru SA proxy upgraded [C · T0-45]); gate: 5–10+ yrs customer-facing architecture (entry-level hyperscaler CSA exists).
13. **[AI Product Manager](hubs/ai-product-manager.md)** (Tier 4, majority): the best non-engineering GenAI target (#1 non-technical, #4 India [M · T0-45, T0-59]); splits into AI-fluent builder PM (evals + AI-assisted prototyping) and senior platform PM leader; lab senior base reaches $240–490K.
14. **[Agentic AI Engineer](hubs/agentic-ai-engineer.md)** (Tier 4, core): kept Watch (`W`) after failing three graduation tests (Skilark 107/28,771 = 0.37% [C · T0-57]); US product firms hire under AI Engineer while India IT services/GCCs use the exact title.
15. **[AI Evaluation Engineer](hubs/ai-evaluation-engineer.md)** (Tier 4, core): 22 named postings globally (5+ India) with bimodal US pay ($120–304K Microsoft to $310–500K Transluce [A/B · T0-60]); target directly where open, otherwise carry evals as a core edge inside Tier 1–2 roles.
16. **[GPU Kernel / ML Compiler Engineer](hubs/gpu-kernel-engineer.md)** (Tier 5, majority): chip and inference vendors (US base median midpoint $235.8K; 8/41 core postings in India [B · T0-63]); gate: CUDA/Triton/C++ depth, kernel PRs and GPU MODE leaderboards; narrow access.
17. **[Physical AI / Robotics AI Engineer](hubs/physical-ai-engineer.md)** (Tier 5, adjacent): graduated W→V (48 postings across 38 employer entries; US base median midpoint ~$242.5K; 35 India on physicalai.jobs [B/C · T0-64]); gate: robot learning/VLA, PyTorch and real-robot deployment.
18. **[AI Governance Programme Lead / Manager](hubs/ai-governance-lead.md)** (Tier 5, majority): for GRC, privacy and audit professionals (median 10 yrs for lead/director vs ~5 yrs all-level [C · T0-61]); EU Reg. (EU) 2026/1744 delayed Annex III 16 months to Dec 2027, moderating near-term hiring urgency.
19. **[Frontier AI Safety / Alignment Researcher](hubs/ai-safety-researcher.md)** (Tier 5, core): lab research ladders ($350–500K), independent institutes ($100K–$503K: METR $250–503.1K and Goodfire $200–400K overlap labs; UK AISI £65–145K + 28.97% pension; FAR.AI $100–250K [B/C · T0-60]) and fellowships (Anthropic Fellows requires US/UK/CA work auth; 0/23 India postings [A/B · T0-60]).
20. **[AI Product Engineer (AI Frontend)](hubs/ai-product-engineer.md)** (Tier 5, core): alias family for React/TypeScript engineers shipping streaming agent UX (median 2 yrs exp in T0-62, dropping the Staff-only overstatement; dedicated `product-frontend` interview track [B/C · T0-62]).
21. **[AI Risk, Audit & Compliance Specialist](hubs/ai-risk-assurance-specialist.md)**, 22. **[Responsible AI / AI Governance Engineer](hubs/responsible-ai-engineer.md)**, 23. **[AI Enablement Engineer](hubs/ai-enablement-engineer.md)** and 24. **[Domain Evaluation Specialist / AI Trainer](hubs/domain-evaluation-specialist.md)**: not primary standalone GenAI targets; see below.

<a id="4-not-primary-genai-targets-and-titles-to-avoid-as-a-headline"></a>
### Not primary GenAI targets, and titles to avoid as a headline

| Role | Why it is not a primary GenAI target | Use it as |
|---|---|---|
| [AI Risk, Audit & Compliance Specialist](hubs/ai-risk-assurance-specialist.md) (#21) | A specialisation inside audit, model-risk and privacy careers. SR 26-2 Footnote 3 excludes generative/agentic AI [A/B · T0-15, T0-61] | A move for auditors and model-risk professionals (ISACA AAIA requires active CISA or a qualifying international accounting credential, excluding Indian CA, not as a job gate [A · U43]) |
| [Responsible AI / AI Governance Engineer](hubs/responsible-ai-engineer.md) (#22) | A thin niche (6 core live titles globally; 5/12 sampled in India [B · T0-61]) | A specialisation for MLOps and security engineers in regulated firms |
| [AI Enablement Engineer](hubs/ai-enablement-engineer.md) (#23) | Small and contracting exact title (Skillenai 90-day count fell 57 → 42 on 2026-11-05 [B · T0-62]); bimodal pay ($120–180K) | Internal DevEx/IT/ops rollout lane, not a broad external job market |
| [Domain Evaluation Specialist / AI Trainer](hubs/domain-evaluation-specialist.md) (#24) | Standing contract pools (Mercor 3/3), wide hourly spread ($20–300/hr) and no formal interview track (`null`) [A/B · T0-66] | A paid bridge into AI for credentialed domain experts |

> [!CAUTION]
> Don't headline a quarantined, legacy or unmeasured title: Context Engineer, Prompt Engineer, Cognitive Architect, Agent Architect (as an exact title), Prompt Wizard, Vibe Engineer, AI Whisperer and the like. Use the canonical title, and show the work as skills in your project bullets. The registers, with their evidence, are in [role catalog §5](role-catalog.md#5-quarantine-watchlist-and-unmeasured-register); how to judge a new title is in [emerging roles](../01-landscape/emerging-roles.md).

<a id="5-best-targets-by-background-genai-persona-lenses"></a>
### Best targets by background

Scores use switcher weights and that background's own Access score; roles that are not plausible within 12 months are excluded [M]. The modelled time to a first offer for each background is kept in [career transitions](../11-tracks/career-transitions.md#modelled-months-to-a-first-offer) (T0-06, Grade D).

| Background | Primary target | Next targets (lens order) | Stretch or later |
|---|---|---|---|
| Backend / Systems SWE | AI Engineer (80) | FDE (74), Applied AI (72), AI Infrastructure (68), Agentic (68), ML Platform (68) | Inference Engineer (Staff level, after infrastructure depth) |
| Data Scientist / BI | AI Engineer with an evals edge (75) | ML Engineer (73), AI Evaluation Engineer (66), Applied AI (65), FDE (63) | Applied Scientist (62) |
| Frontend / Full-Stack | AI Engineer, full-stack (77) | FDE (72), Applied AI (65), Agentic (63), AI Evaluation (60) | AI Product Engineer (streaming AI UX) |
| Non-technical (5+ years in a domain) | AI Product Manager (64) | FDE-adjacent roles (62; FDE proper requires coding), AI Governance Lead (59), AI Solutions Architect (58) | Domain evaluation (54, as a bridge) |
| PhD / Researcher | Applied Scientist (75) or AI Engineer / MLE (73) | Research Engineer/MTS (73), Applied AI (67), FDE (65) | Research Scientist ("not plannable") |

<a id="6-india-first-target-order-genai-india-lens"></a>
### India: the India-first order

The India lens replaces US demand and pay with India inputs [M]. RP2 upgraded India benchmarks for AI Product Manager, AI Solutions Architect, Forward Deployed Engineer, Applied Scientist, AI Security, AI Infrastructure, Inference and GPU Kernel, while 12 of 24 IC India pay inputs still rest on Grade D (0 of 24 India demand inputs are Grade D).

| India # | Role | India CCI | Note |
|:---:|---|:---:|---|
| 1 | AI Engineer | 73.2 | #1 in 89% of Monte Carlo draws [M]. Greater Bengaluru P50 ₹20.0L / P90 ₹60.6L [B · T0-45]; top GCC label per Taggd [C] |
| 2 | ML Engineer (GenAI track) | 67.9 | Higher pay (Bengaluru P50 ₹44.4L / P90 ₹80.7L [B · T0-45]), smaller India GenAI subset (~41 postings) [M] |
| 3 | Applied Scientist | 66.3 | Amazon Science listed 90 India science roles (14% of global, 2026-11-13 [B · T0-52]); India pay still Grade D (proxies only) |
| 4 | AI Product Manager | 66.0 | Upgraded via Levels.fyi India PM (n=1,518) and Bengaluru Senior PM (n=578) proxies [C · T0-45, T0-59] |
| 5 | AI Infrastructure / GPU Platform | 63.0 | 10/35 core postings (28.6%) in India (NVIDIA ×4, Deloitte USI ×2, Sarvam ×2, AION, Soket; 0 GCCs [B · T0-54]) |
| 6 | Applied AI Engineer | 61.7 | Verified India hiring at OpenAI Bengaluru, Anthropic partner/field roles and startups [C · T0-53] |
| 7 | AI / GenAI Solutions Architect | 61.6 | Upgraded via Bengaluru Solution Architect (n=179) proxy [C · T0-45, T0-62] |
| 8 | ML Platform / MLOps | 61.5 | Graduated to Established (E); common India GCC/services title (13/37 sampled in India [C · T0-58]) |
| 9 | Forward Deployed Engineer | 60.6 | Indeed India / IANS reported ~19× YoY growth from a low base [C · T0-25, T0-51]; Levels.fyi India FDE TC P50 ₹16.75L–17.7L / P75 ₹42L and Weekday ₹25–40 LPA [B · T0-51]; mostly non-remote |
| 10 | Research Engineer / MTS | 60.1 | Two verified live India postings (DeepMind Bangalore, Sarvam Bengaluru [C · T0-50]); 0/2 disclose pay |
| 11 | AI Security Engineer / AI Red Teamer | 60.1 | 9 India postings (36% of sample) and posted bands ₹25–50L [B · T0-60] |
| 12 | Inference / LLM Serving Engineer | 59.6 | 9/37 core postings (24.3%) in India (startups, DigitalOcean ×2/Rackspace, Weekday; 0 GCCs/silicon vendors); one posted band ₹24–36L [B/C · T0-56] |

The India market facts behind these notes (remote shares, GCC demand and pilot risk, the two pay populations) are in the [market overview's India section](../01-landscape/market-overview.md#8-india-more-ai-intensive-younger-smaller-in-counts-split-in-pay). Independent contracting tax is in [India remote tax](../09-compensation/india-remote-tax.md) (pointers, not tax advice), and the routes are in the [India remote playbook](../11-tracks/india-remote-playbook.md).

<a id="8-leadership-and-independent-tracks-when-to-target-them"></a>
### Leadership and independent tracks: when to target them

Their order and scores are in [role rankings §4](role-rankings.md#4-leadership-and-independent-tracks) [M].

| # | Track | When to target it | Evidence |
|:---:|---|---|---|
| L1 | [AI Engineering Manager / Director](hubs/ai-engineering-manager.md) | After Senior or Staff IC: text-visible postings (n=8) ask 8+ years engineering and 2–6 (median 3) years managing; backend/SRE/devtools EMs can cross without research [M · T0-65] | Fast AI Jobs 608 EM roles at 239 AI startups on 2026-11-12 (+54% vs Jul; 20–24% AI-system EMs [B · T0-65, T0-70]); US posted base $163–405K + equity [A/B · T0-65]; India SWE Manager proxy P50 ₹85.6L (n=975 [B · T0-45]) ([pay benchmarks](../09-compensation/pay-benchmarks.md#independent-contract-and-leadership-rates)) |
| L2 | [VP / Head of AI](hubs/vp-head-of-ai.md) | After EM or Director, with 5–15+ (median 10, n=7) years engineering or product leadership (45% hands-on player-coach, 55% CEO/CTO report [C · T0-65]) | Axial Search tracked 65 US executive AI-engineering postings over 6 months [C · T0-65]; US posted base $170–315K + bonus/equity and UK £120–150K [A/B · T0-65] |
| L3 | [Chief AI Officer](hubs/chief-ai-officer.md) | Executive track (12–15+ years senior leadership [B · T0-65]) | OMB M-25-21 (2025-04-03 [A · U43]) mandates US federal agency CAIO designation (dual-hatted permitted); Crist Kolder Fortune 500 + S&P 500 prevalence 10.7% (71/665 [B · U47, T0-65]); US public/higher-ed $118–200K, SBI India up to ₹160L [B], corporate $400K–$1M+ [C · T0-65] |
| L4 | [Independent AI Consultant](hubs/independent-ai-consultant.md) | Late career, with a network: independent freelancer surveys report 53–75% network sourcing (vs Go Fractional's 92% sponsor survey [C · U47]) | UK GenAI contract ads tripled to 1,466 in 6 months to 2026-11-12 while median day rate held flat at £550/day (n=933 [B · T0-66]); US agency $50–80/hr [B]; direct asks $150–250/hr ([freelance and fractional](../11-tracks/freelance-fractional.md)) |
| L5 | [Fractional Head of AI / CAIO](hubs/fractional-ai-leader.md) | Late career: 10+ years or prior Head/VP/CTO seat (9/13 postings); Fractional Jobs survey reports 87% 11+ years [B/C · T0-18, T0-66] | Only 1/13 qualifying postings on an employer's own page; Go Fractional logged 10 CAIO posts in 90 days (4 open, 2026-11-12 [B · T0-66, T0-70]); employer offers $75–150/hr [B] vs $150–250/hr asking corridor [C] ([freelance and fractional](../11-tracks/freelance-fractional.md)) |

## Templates and examples

### Target shortlist [P]

A filled example for a backend engineer, built from the tables on this page:

```text
Background:        Backend engineer, 6 years (Python, Kubernetes)
Cluster:           Applied GenAI
Primary title:     AI Engineer (target #1, Tier 1); gate: none formal
Adjacent title 1:  Forward Deployed Engineer (#4, Tier 2); gate: customer work, travel
Adjacent title 2:  Applied AI Engineer (#6, Tier 2); gate: lab-tier hiring bar
Edge skill:        evaluation in CI (golden set, calibrated judge)
One portfolio:     one evaluated RAG system and one reliable agent
Location check:    India search? AI Engineer is India #1; FDE #9 (mostly non-remote)
Re-read after:     the 2026-12-01 recount
```

The blank version:

```text
Background:        [your row in "best targets by background"]
Cluster:           [Applied GenAI | Model | Frontier research | Systems | Product and governance]
Primary title:     [top title in the cluster whose gate you meet] (target #[n], Tier [t]); gate: [gate]
Adjacent title 1:  [title] (#[n], Tier [t]); gate: [gate]
Adjacent title 2:  [title] (#[n], Tier [t]); gate: [gate]
Edge skill:        [agents | evals | inference | other], proved by [artefact]
One portfolio:     [projects that cover the proof all three hubs ask for]
Location check:    [India rank of each title, or n/a]
Re-read after:     [next recount date]
```

### Weak and strong shortlists [P]

| Weak | Strong | Why |
|---|---|---|
| "Context Engineer, Prompt Engineer, AI Whisperer" | "AI Engineer; Agentic AI Engineer and FDE as adjacent titles" | Quarantined, legacy and unmeasured titles are not targets; the canonical title carries the work |
| "AI Engineer, Research Scientist, AI Governance Lead" | "AI Engineer, FDE, Applied AI Engineer" | Three clusters need three portfolios; one cluster needs one |
| "Agentic AI Engineer only" | "AI Engineer with agent reliability as the edge; Agentic AI Engineer where the title exists" | The skill is broad, the title small |

## Checklist

- [ ] I chose one cluster.
- [ ] My primary target is the highest-ranked title in that cluster whose gate I meet, or will meet by a dated step.
- [ ] I added two adjacent titles from the same cluster that one portfolio serves.
- [ ] I read the hub of each of my three titles.
- [ ] My edge skill (agents, evals or inference) sits inside a Tier 1 or Tier 2 title, not as my only target.
- [ ] No quarantined, legacy or unmeasured title is in my headline.
- [ ] I checked my background row, and the India-first order if I search in India.
- [ ] I added a leadership or independent track only because I already meet its entry conditions.
- [ ] The shortlist is in the targeting workbook, with a re-read date after the 2026-12-01 recount.

## Pitfalls

| Red flag | Why it hurts | Fix |
|---|---|---|
| Applying across three clusters at once | Each cluster needs its own portfolio, so no application gets your best proof [D] | One cluster: its top title plus two adjacent titles |
| Making a strong skill your only target title | Agents and evals are broad skills but small titles: agentic AI is named in 59.3% of AI Engineer postings [B · T0-01.F4], while Agentic AI Engineer and AI Evaluation Engineer stay on the catalog's watchlist | Target AI Engineer and lead with the skill; apply to the small title where it exists |
| Reading the CCI #1 as the GenAI #1 | The CCI counts all demand, including recsys, ads and autonomous-vehicle work; restricting to GenAI swaps #1 and #2 [M] | Use this order for GenAI work and the [role rankings](role-rankings.md) for the whole career |
| Splitting hairs inside a tier | Differences within a tier sit inside the uncertainty bands [M] | Choose within a tier by gate, background and location |
| Betting everything on a medium-confidence rank | Applied AI Engineer (#6) still rests on C-grade demand and a volatile P90 ($505K–$605K), while AI PM (#13) and AI Solutions Architect (#12) lack exact title-level counts | Keep a Tier 1 title on the shortlist; re-read after the 2026-12-01 recount |
| A quarantined or legacy title in your headline | Screening layers score title similarity [A · T0-04.F8] | Use the canonical title; show the work as skills |
| Comparing a frontier-lab offer at paper value | 49–72% of senior lab packages is stock [B · T0-02]; private equity is semi-liquid while Anthropic's newly public `ANT` (2026-11-19) carries staggered lock-ups [A · U52] | Risk-adjust it first ([offer evaluation](../09-compensation/offer-evaluation.md)) |
| Planning a leadership track as a first move | People reach these tracks after years of experience [D] | Add one only once you meet its entry conditions |

<a id="9-caveats-and-what-would-change-the-order"></a>
## Evidence and limits

- **Measured (B):** the posting counts and the shares of postings that name LLM behind the GenAI restriction (JobsPipe, underlying count date 2026-09-10, re-checked 2026-11-13 [T0-69]), and the demand and pay inputs scored in [role rankings Appendix A](role-rankings.md#appendix-a-scoring-inputs), each with its own grade.
- **Model outputs (M):** the order, the tiers, the consensus means and lens ranges, the GenAI subsets and CCIs, the Monte Carlo shares and the persona and India lens values. All are computed by `scripts/target_roles.py` from data/role_scores.json (data as of 2026-11-19), and each inherits the weakest grade among its inputs.
- **Judgement (D):** the Durability and Leverage pillars, the centrality class of the Majority roles, the gates and risks in the role lines, and the one-cluster strategy.
- **The GenAI subsets are derived.** They use "LLM named" as the GenAI share, a lower bound; the AI Engineer > ML Engineer result holds even at a 60% share for ML Engineer.
- **Roles most likely to move at the next recount:** Research Engineer / MTS (quorum-crossing candidate on Fast AI Jobs), AI Security Engineer (queued for exact-title recount after SANS >850), AI Product Manager and AI Solutions Architect (no exact title-level counts) and Applied AI Engineer (C-grade demand; P90 shifted $605K to $505K across Oct–Nov 2026). T0-01's recounts are due on 2026-12-01 and 2027-01-15 [T0-01 L84].
- **India:** the India lens is directional, because 12 of 24 IC India pay inputs still rest on Grade D (proxies or small samples).
- **Dates:** review by 2026-12-06, 31 days after the oldest count source in data/role_scores.json (Skillenai 2026-11-05; EGP-1.0 class V1).
- **What would change the order:** quorum recounts for Research Engineer / MTS and AI Security Engineer, exact title-level counts for AI Product Manager, AI Solutions Architect and Applied AI Engineer, direct India pay series for the 12 Grade D roles, or a measured change in the share of ML Engineer postings that name LLM.

## Next steps

- **Your three titles:** open each one's [role hub](hubs/README.md); every hub links its skills inventory, proof and interview pack.
- **Write the shortlist down:** the [targeting workbook](../00-start/targeting-workbook.md).
- **Explore around it:** the [role map](role-map.md) shows where the work sits, and [emerging roles](../01-landscape/emerging-roles.md) shows how to read a new title.
- **The evidence:** the [role catalog](role-catalog.md) (definitions, status classes and registers) and the [role rankings](role-rankings.md) (the all-demand CCI, its lenses and the scoring inputs).
- **Timelines and routes by background:** [career transitions](../11-tracks/career-transitions.md), [PhD to industry](../11-tracks/phd-to-industry.md) and the [India remote playbook](../11-tracks/india-remote-playbook.md).
- **Next stage:** [skills and technology](../03-skills-and-tech/README.md), starting with the [learning roadmaps](../03-skills-and-tech/learning-roadmaps.md), then the [proof-of-work standards](../05-portfolio/proof-of-work-standards.md).
