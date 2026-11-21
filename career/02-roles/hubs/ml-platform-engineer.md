---
id: roles.hub.ml-platform-engineer
title: "ML Platform / MLOps Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "ML Platform / MLOps Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-58]
roles: [ml-platform-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# ML Platform / MLOps Engineer

> Builds the internal platform for the ML model lifecycle and serving: Kubernetes, IaC, CI/CD, experiment tracking and registries (MLflow/Kubeflow), observability, feature stores and emerging LLMOps.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| AI Infrastructure & Platform | L3 Inference and ML platforms; also L1 Compute and hardware | Established (E) | #9 of 24 | #9 of 24 · band A · Monte Carlo rank 10 (P10–P90 7–14) | D2 Platform & infrastructure |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 6.5 (5.5–7.5) | B | Graduated V -> E: Axial 1,959 US MLOps postings Jan to 2026-07-13 (~70/wk steady, B); ITJobsWatch 184 UK permanent jobs citing MLOps in 6 mo (B); Fast AI Jobs 1,099 broad ML-platform/infra listings [T0-58]. |
| Pay | 6.5 (5.5–7.5) | B | Generalist-vs-Big-Tech split: Levels.fyi US MLOps Engineer TC median $145,200 (P25 $120K / P75 $200K / P90 $295K, 2026-10-11, B) and Fast AI Jobs posted-base median $179,250 (n=430, 2026-11-12, B) vs senior/Big Tech ML Platform posted base $150K–$357K (median midpoint $245K, n=8, M) [T0-44, T0-58 K4]. |
| Durability | 6.5 (5–8) | D | Judgement. Platform need persists (DORA 2025: 90% internal platforms, 76% dedicated teams, C) and 32% of postings add LLMOps; fast serving-tool churn (TGI archived, NVIDIA Triton renamed Dynamo-Triton 2025-03-18) [T0-03 KF6, T0-58 KF12/KF14]. |
| Leverage | 7.5 (6.5–8.5) | D | Judgement. Platform-as-a-product multiplies DS and MLE velocity (Uber Michelangelo architecture for thousands of models; Wellhub internal platform product [T0-58 L276]). |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 6 (5–7.5) | C | 13 of 37 postings in India across GCCs (Walmart Global Tech, Rakuten Symphony, Aptiv) and IT services (HCLTech, Quantiphi), predominantly titled MLOps Engineer [T0-58]. |
| India pay | 5.5 (4.5–6.5) | C | Bengaluru MLOps P50 Rs23.6L, P75 Rs41.1L, P90 Rs63.5L [T0-02:147]; 0/13 India postings in T0-58 disclose pay (conflicting secondary bands: edtech/aggregator Rs8–20 LPA vs OwnYourCareer entry Rs8–15L / mid Rs20–35L / senior Rs38–65L, C) [T0-58 K6]. |

India rank (CCI with India inputs): #8 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 7 | ◐ 5 | ◐ 4 | ○ 1.5 | ◐ 4 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Kubernetes, Terraform / IaC, Git & CI/CD, Docker, Python (production), AWS / Azure / GCP, Observability (OpenTelemetry traces, metrics), MLOps lifecycle (model & prompt CI/CD).
- **Important (headline):** Linux, KServe / Ray Serve, LLM gateways, OAuth/OIDC, RBAC, SSO, Model supply chain & CVEs, SRE (SLOs, on-call, incidents), vLLM / SGLang / TensorRT-LLM.
- **Full inventory:** 77 skills (Must 8 · Important 16 · Should 34 · Optional 19), each with its evidence and posting keywords: [ml-platform-engineer.md](../../03-skills-and-tech/inventories/ml-platform-engineer.md).
- **Prerequisites:** Backend, DevOps or SRE background; India GCCs use the MLOps Engineer title (Taggd, C)
- **Credentials (tie-breakers, not skills):** Certified Kubernetes Administrator (CKA) (Optional: intermediate live CLI exam ($445); 1/47 T0-32 infra postings, common in K8s platform hiring (K8s 61.3% in T0-58)); AWS Certified Machine Learning Engineer – Associate (MLA-C01) (Avoid: retired in English 2026-09-28; replaced by AWS MLA-C02); AWS Certified ML Engineer – Associate (MLA-C02) (Optional: replaces MLA-C01; beta, GA 2027-01-14; adds GenAI and agentic workloads); Certified Kubernetes Application Developer (CKAD) (Optional: CNCF Certified Kubernetes Application Developer (live CLI exam); complements CKA for GPU/ML workload deployment (T0-32)); SnowPro Core Certification (COF-C03) (Optional: Snowflake platform baseline; relevant only where target ML platform or SA accounts run Snowflake Cortex/Snowpark (T0-31)); Databricks Certified Machine Learning Professional (Optional: $200, 59 Q, 120 min; production ML platform engineering on Databricks Lakehouse (T3-01)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A self-hosted vLLM/SGLang cluster with continuous synthetic load benchmarks, automated failover, dynamic LoRA routing and Grafana dashboards
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P6 Self-hosted LLM platform on Kubernetes](../../05-portfolio/project-archetypes.md#p6) (92%); [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (32%); [P15 Internal AI-enablement pilot (MCP servers, adoption metrics)](../../05-portfolio/project-archetypes.md#p15) (18%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Infrastructure.** It tests sub-discipline specific: serving and inference (systems coding, distributed-systems design; KV-cache maths, decode roofline, continuous batching and prefill/decode disaggregation appear in prep guides [C]), GPU cluster ops (Slurm, InfiniBand/RDMA, NCCL debugging, bare-metal failure recovery, Kubernetes at scale), MLOps/ML platform (IaC, CI/CD, drift monitoring, feature stores, ML job schedulers) and GPU kernels (simulated-accelerator take-home [A, COI], profiler walkthrough, roofline analysis, numerics/dtype tolerances). Source: T0-14, T0-46, T0-54, T0-56, T0-58, T0-63, T1-03.
- **Practise:** the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** D2 Platform & infrastructure (AI Systems & Infrastructure); headline pattern: "AI Infrastructure Engineer: GPUs, Kubernetes, model serving". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** MLOps, LLMOps, Kubernetes (69.4% of DevOps postings), Terraform (59.1%), CI/CD (81.2%), model serving, KServe, monitoring
- **Leave out or reframe:** Generic DevOps bullets with no model-serving scope
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ml-platform-engineer).

## Specialisations inside this role

- **Vector search infrastructure** (L5 Orchestration and context): Candidate title: Vector Search & Retrieval Systems Engineer, role catalog §5.3.
- **MCP and agent protocols** (L5 Orchestration and context): Specialisation label MCP Control Plane Engineer in the A–Z index; no literal title (MCP named in 19.0% of Skillenai / 26.7% of sampled AI Enablement postings [T0-62]).
- **Gateways and model routing** (L3 Inference and ML platforms): No title of its own in the catalog (Agent Gateway Engineer: legacy label, 0 postings; 0/37 ML Platform postings named LLM/MCP gateways [T0-58]).
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [AI Infrastructure / GPU Platform Engineer](ai-infrastructure-engineer.md) (0.45); [AI Security Engineer / AI Red Teamer](ai-security-engineer.md) (0.21); [Inference / LLM Serving Engineer](inference-engineer.md) (0.15).
- **Same family (AI Infrastructure & Platform):** [Inference / LLM Serving Engineer](inference-engineer.md), [GPU Kernel / ML Compiler Engineer](gpu-kernel-engineer.md), [AI Infrastructure / GPU Platform Engineer](ai-infrastructure-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ml-platform-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ml-platform-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A November 2026 sample of 37 core postings (31 coded for skills; 5 read in full on employer boards, plus 4 German-language probe records) shows that "ML Platform / MLOps Engineer" spans **four distinct operating models** under one umbrella [A/M · T0-58 L49, L63, L107–113]:

| Variant | Example employers | Core day-to-day focus |
|---|---|---|
| **1. Big Tech SWE on an ML/AI platform team** | Uber (Michelangelo), Netflix, Pinterest, Microsoft AI, NVIDIA | Large-scale distributed systems, multi-thousand-model serving platforms and lifecycle observability; Uber's staff posting names no Kubernetes, Terraform, Docker or Python |
| **2. AI-cloud and AI-native platform** | Together AI, Scale AI, Mistral AI, Synthesia | Kubernetes internals, IaC, Go or Python, GPU scheduling and multi-tenant serving platforms |
| **3. Product-company ML platform** | Wellhub, Mollie, dv01, SumerSports | Platform-as-a-product for embedded DS/ML teams: Kubeflow, Feast, Spark-on-Kubernetes, Terraform/Crossplane, CI/CD and LLMOps lifecycle requirements |
| **4. India services and GCC MLOps** | HCLTech, Rakuten Symphony, Aptiv, Quantiphi, Fractal, TransUnion, Calix | End-to-end model pipelines with MLflow, Kubeflow, Airflow and managed cloud ML services (SageMaker, Vertex AI, Azure ML) |

**Key realities revising the Phase 0 scorecard:**
- **LLMOps extends MLOps rather than replacing it:** LLM-specific content (LLMOps lifecycle, RAG, vector databases, RLHF, LLM-provider integration or vLLM) appears in 10 of 31 coded postings (32.3%), such as Wellhub's AI Platform Engineer role [A/M · T0-58 L72, L188, L274]. However, **LLM gateways (0%), MCP/agent protocols (0/37) and model supply-chain/CVE tooling (0%)** were unseen in postings, and IAM appeared in only 3.2% (1/31) [M · T0-58 L64, L198–200, L282–286]. Work sits primarily in layer L3, with L1 GPU/Slurm work in 5/31 coded postings and L5 orchestration/MCP unseen [M · T0-58 L280, L343].
- **Skill shares and Phase 0 feeder artefacts:** Across 31 coded postings (extract-limited lower bounds), the leaders are **model-lifecycle tooling** (`mlops_lifecycle`, 67.7% — promoted from Phase 0 Important to Must), Kubernetes (61.3%), cloud platforms (51.6%; Axial reports >67% across 1,959 US postings [B]), CI/CD/Git (45.2%), IaC (41.9%), observability (41.9%) and Python (38.7%; Axial >67% [B]) [M/B · T0-58 L64, L177–183]. **MLflow** (45.2%) and **Kubeflow** (41.9%; union 51.6%) — omitted from Phase 0's headline card and added to Important from T0-58 — lead tool mentions, though inflated in the India subset by query wording [M · T0-58 L51, L184–185, L202]. The Phase 0 DevOps-feeder shares for DevOps (99.0%), Git/CI (81.2%) and Docker (53.4%) are not reproduced (9.7%, 45.2% and 29.0%), and the ontology's Phase 0 links double-counted `iac`/`terraform` (both 59.1%) and `cloud`/`aws` (both 52.9%) from the same DevOps feeder snapshot [M · T0-58 L64, L392].
- **Confirmed tool churn (live-verified 2026-11-19):** NVIDIA renamed Triton Inference Server to **NVIDIA Dynamo-Triton** (as of 2025-03-18) with NVIDIA Dynamo as its LLM-serving successor, and Hugging Face placed **TGI** in maintenance mode and archived its GitHub repository on 2026-03-21 (one sample posting still names TGI) [B on session extracts; live-verified 2026-11-19 · T0-58 L70, L194]. Watch item: NVIDIA's announced $12.93B agreement to acquire Hugging Face (flagged unverified in T0-58 L397; live-confirmed as announced and pending regulatory approvals on 2026-11-19) may further reshape open-model platform tooling.
- **Proof of work and résumé framing:** No first-party hiring-manager statement backs the scorecard's exact self-hosted vLLM/SGLang dynamic-LoRA cluster project (`K14` is unverified) [C · T0-58 L244, L349]. Together AI asks candidates to discuss how systems they built failed and treats open-source maintenance as a plus [A · T0-58 L244]; recruiter and vendor sources favour deployed-system write-ups with incident post-mortems and OSS contributions (MLflow, Kubeflow, Feast, Ray) over certificates [C · T0-58 L244, L663]. Tie every platform bullet to model-serving or model-lifecycle scope rather than generic Kubernetes/DevOps work [C/P · T0-58 L307, L350].

## Employer landscape and title confusion

**Measured volume (upgrading the Phase 0 Grade D demand gap):**
- **Steady US demand:** Axial tracks **1,959 US MLOps postings** from January to 2026-07-13 (~70 new postings/week, flat rather than surging; 34% at employers with 10,000+ staff, 13% at firms under 50, 13% contract) [B · T0-58 L59, L61, L131–138].
- **Rising UK skill citations:** ITJobsWatch records **184 UK permanent IT jobs citing MLOps** in the six months to 2026-02-18 (against 156 and 139 in the two prior years, +18%) [B/M · T0-58 L59, L136].
- **Noisy startup category:** Fast AI Jobs' broad "MLOps / Infrastructure Engineer" category rose from 630 (~June 2026) to **1,099 open roles across 423 companies** on 2026-11-12 (+74%), but includes unrelated systems and SRE roles and overstates ML platform volume [B/M · T0-58 L60, L133–135].

**Title fragmentation and traps:**
- **Real titles seen (`n = 37`):** 21 use *MLOps* or *ML Ops* (including *MLOps / ML Platform Engineer*), 5 *AI Platform* (Uber, Wellhub, Veralto ×2, Vriba), 3 *ML Platform Engineer* (Together AI, Mollie, Synthesia), 3 *Software Engineer* on an ML/AI platform team (Pinterest, Netflix, Walmart Global Tech India), 3 *Platform Engineer* with ML scope (Together AI, Lorien, Mistral), and 2 *AI/ML Infrastructure* (RoundCircle, Scale AI) [M · T0-58 L62, L116–123]. **0 of 37** carry *LLMOps Engineer*, *MCP Control Plane Engineer*, *Agent Gateway Engineer* or *Enterprise AI Control Plane* — treat those as watchlist labels, not search queries [M · T0-58 L62, L82, L337]. In German-language markets, search *KI Platform Engineer* and *Cloud & MLOps Expert* [B/C · T0-58 L62, L125].
- **Frontier labs and Big Tech rarely say "MLOps":** Mistral posts *Platform Engineer, Data Infrastructure & MLOps*; Netflix, Uber and Pinterest use *Software Engineer* titles on ML/AI Platform teams; Anthropic posts adjacent *Kubernetes Platform* infrastructure roles [A/B · T0-58 L71, L83].
- **Stale and geo-locked listings:** Two of four employer URLs retested live on 2026-11-13 were dead (Walmart `R-2465787` and Epidemic Sound) while aggregator copies persisted, and SumerSports replaced its job ID on relisting [A · T0-58 L24, L168, L318]. "Remote" tags also hide country locks: Wellhub's and CI&T's remote postings are open only to candidates in Brazil [A · T0-58 L291, L319].
- **Credentials (live-verified 2026-11-19):** Only **1 of 37 postings** names any certification (HCLTech, optional — citing the already-retired AWS ML Specialty and Google Professional ML Engineer), and 0/37 name CKA or AWS MLA [A/M · T0-58 L69, L253–254]. Exam statuses as of 2026-11-19: **AWS ML Specialty (`MLS-C01`)** retired 2026-03-31 (do not pursue or list as current); **AWS ML Engineer – Associate (`MLA-C01`)** English exam ended 2026-09-28; **`MLA-C02`** entered beta on 2026-09-29 ($75 beta fee, 170 min, 85 questions, GA set for 2027-01-14, adding Bedrock/RAG/agentic workloads — note T0-58 flagged an AWS page code typo `ME1-C02`); **CKA** is active ($445 including one retake, 120 min performance-based, 2-year validity) [A for AWS MLA-C01/C02; B (live-verified 2026-11-19) for MLS-C01 and CKA · T0-58 L69, L248–256]. See [credential ROI](../../04-certifications/credential-roi.md).

## Career path, India demand and market signals

**Seniority and entry routes:** Axial reports a US mix of 36% mid, 33% senior, 13% principal, **9% junior** and 8% management, with 63% requiring a degree [B · T0-58 L61, L137, L164]. In the 37-posting sample, only 1 posting is junior (Mollie), 5 mid, 15 senior, 7 lead/staff+ and 9 unstated (median minimum 4.5 years, `n = 6`), with 3 stating a degree (all accepting equivalent experience) [M · T0-58 L162–164]. Strongest entry feeders are backend/distributed-systems engineers (Big Tech and AI-cloud variants) and DevOps/SRE engineers adding model-lifecycle/serving depth [A/C · T0-58 L262–263]; data scientists need production Kubernetes and IaC [D · T0-58 L264]; early-career applicants should expect thin direct openings and enter via adjacent platform, DevOps or data-engineering roles [B/M · T0-58 L84, L267].

**Progression and durability:** IC ladders run through Staff and Principal (Uber Staff asks 8+ years; Pinterest Principal band $243K–$500K [C]), with exits into engineering management (Pinterest Sr EM $208.6K–$429.5K [C]) or frontier-lab infrastructure/inference roles [A/C · T0-58 L273]. Durability signals show structural platform demand (secondary DORA 2025 reporting cites 90% internal platform use and 76% dedicated platform teams [C], and vendor surveys show widespread AI workload hosting alongside daily AI-tool usage [C, COI]), though routine IaC and CI boilerplate is exposed to AI coding automation while GPU scheduling, serving reliability, cost governance and platform architecture remain more durable [C/D · T0-58 L72, L275].

**Pay reconciliation, geography and sponsorship:** Full pay tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). **Do not blend US pay sources:** T0-58's posted-base sample (`n = 8`, senior/Big-Tech/startup-weighted) spans $150K–$357K (median midpoint **$245K** [M]), Fast AI Jobs' broad category median is **$179,250** (`n = 430` on 2026-11-12 [B]), and Levels.fyi US "Machine Learning Ops Engineer" total compensation is **$145,200** median (p25 $120K, p75 $200K, p90 $295K as of 2026-10-11 [B], pooling all levels and employers — contrast Apple MLOps median TC at $439,250 [B]) [M/B · T0-58 L65, L208–216, L228]. UK advertised medians (ITJobsWatch, B): London £75,000 (six months to 2026-10-20), UK outside London £87,500 (p75 £95K, p90 £127K, six months to 2026-02-18) [B · T0-58 L66, L221–222]. Geography is broader and far more remote-friendly than GPU-cluster or inference roles: California holds 27% of Axial US postings (Texas and NY ~9% each), and **42% of US postings stating a work model are fully remote** (38% hybrid, 20% on-site) [B · T0-58 L61, L139, L290]. On sponsorship (pointers, not legal advice; verify in [visa and relocation](../../11-tracks/visa-and-relocation.md)): 0 of 5 full-read postings state US visa sponsorship, and no MLOps-titled DOL LCA count was found (the adjacent AI/ML engineer family logged 8,275 certified LCAs across FY2025–FY2026 Q3; filings are not pay) [B · T0-58 L73, L295].

**India demand and nuance:** India accounts for **13 of 37 sample postings** (12 Bengaluru, 1 Hyderabad) across **GCCs** (Rakuten Symphony, Aptiv, Walmart Global Tech India), **IT services** (HCLTech, Quantiphi, Fractal), **enterprises** (TransUnion, Veralto ×2, Calix), a startup (Autonomize) and agencies (RoundCircle, Vriba) [M/B · T0-58 L324]. Eight of 13 use *MLOps* in the title, and GCC postings typically combine Kubernetes, Kubeflow, MLflow and Airflow (though MLflow/Kubeflow's 11/13 share is a query-biased upper bound) [M/B · T0-58 L325–326]. **Nuance on the Phase 0 Quess GCC supply gap:** The 18–43% range traces to Quess Q3 FY26; subsequent Quess reports cite 32–36% for platform engineering (Q1 FY27) and 38–42% for AI and data (Q2 FY27), with 4–12 years' experience representing 56% of GCC demand — **alongside a 3.5% quarter-on-quarter drop in GCC tech hiring in July–September 2026** (staffing-firm COI) [C · T0-58 L67, L327–328]. **India pay remains conflicting (`K6` unverifiable):** 0 of 13 India postings disclose pay, and secondary sources diverge sharply by population — all-level edtech averages of ₹8–20 LPA [C, COI] against experience-banded estimates of ₹8–15L entry, ₹20–35L mid and ₹38–65L senior [C] (putting Phase 0's ₹23.6L Bengaluru P50 in the mid-career band; see [pay benchmarks](../../09-compensation/pay-benchmarks.md)) [C · T0-58 L66, L224–228, L341].

## Interview themes and preparation notes

**How the Infrastructure track applies to ML Platform / MLOps (`K9` updated):** The track's inference-serving sub-discipline (continuous batching, KV cache, disaggregated serving) fits **only the inference-platform subset** (such as Together AI or Scale AI serving roles), whereas standard ML Platform / MLOps loops focus on the platform-engineering topics below [C · T0-58 L68, L240].
- **What standard MLOps and ML-platform loops actually test:** Aggregated candidate reports (Dataford, C) show technical rounds in 56–77% of loops and take-home deployment exercises in 33–46%, centred on **IaC, experiment tracking, model versioning, containerisation, CI/CD for models, drift-monitoring design, real-time feature stores and pipeline bottlenecks** [C · T0-58 L68, L234–235].
- **Big Tech ML-platform loops:** Netflix AI Platform teams (L4–L6 across Training Platform, Model Serving Systems, Data/Feature Infrastructure and Agent Platform) reportedly weight team-drawn **ML-platform system design** most heavily (such as an ML job scheduler, internal platform portal or freshness-aware feature serving), alongside coding [C · T0-58 L237]; LinkedIn AI Platform follows a general SWE coding-plus-system-design loop [C · T0-58 L236]. A July 2026 press report claiming Netflix permits AI tools in coding rounds cites no Netflix primary source [D · T0-58 L68, L237].
- **Preparation focus (no model answers, per D-018):** Match prep to your target variant — pair the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack) with model-lifecycle platform design (CI/CD, feature stores, drift/observability, job scheduling) and check [interview loops](../../08-interviewing/interview-loops.md). No India-specific loop evidence or employer-published AI-tool interview policy was found [E · T0-58 L330, L364–365].

## Dossier evidence and limits

- **Low full-read rate and freshness caveats:** T0-58 has the thinnest primary-page access in this cluster: only **10 of 92 ledger sources (11%) were read in full**, only **5 of 37 core postings (14%) were opened on employer boards**, and only **12 of 37 (32%) meet the strict 90-day freshness window** [M · T0-58 L24, L167]. Treat the JD sample as a directional cross-check on Axial, ITJobsWatch and Fast AI Jobs rather than a standalone share measurement (±17 pp margin at `n = 31`, extract-limited lower bounds) [M · T0-58 L24, L64].
- **Epistemic audit (Extract-only Grade A downgrades):** Eleven T0-58 ledger rows (S44, S47, S48, S53, S54, S56, S57, S68, S72, S84, S85) and one JSONL credential record (`cncf_cka`, L653, combining Extract S48 with Grade C guide S49) were labelled Grade A despite Extract-only access. Under sceptical verification, all Extract-only rows are downgraded to Grade B on session evidence alone; live web checks on 2026-11-19 independently confirmed CKA fees/validity, AWS MLS-C01/MLA-C01/MLA-C02 timelines, TGI archiving (2026-03-21) and NVIDIA Dynamo-Triton.
- **Query bias and COI:** India search queries explicitly named "Kubeflow MLflow", inflating those tools in the India subset [T0-58 L51, L202]. Fourteen ledger rows carry COI (staffing firm Quess, edtech salary blogs, platform-tooling sponsors Vultr/Perforce/Pulumi, hiring vendors, and Anthropic as model developer on adjacent row S72) [T0-58 L13, L383–384].
- **Explicit absences (not measured as of 2026-11-13):** MLOps-titled US LCA filings; primary India pay data and Levels.fyi India/Europe figures; first-party hiring-manager proof-of-work statements; published analyses of prior roles of hired engineers; the primary Taggd GCC report; full exam-page reads for Google Professional ML Engineer and AWS MLOps Demonstrated; India-specific interview loops; employer-stated AI-tool interview policies; frontier-lab MLOps postings beyond Mistral; and JobsPipe MLOps-specific counts [E · T0-58 L354–369].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
