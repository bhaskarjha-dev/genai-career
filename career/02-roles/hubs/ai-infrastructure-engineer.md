---
id: roles.hub.ai-infrastructure-engineer
title: "AI Infrastructure / GPU Platform Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "AI Infrastructure / GPU Platform Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-54]
roles: [ai-infrastructure-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# AI Infrastructure / GPU Platform Engineer

> Runs the compute estate behind training and inference: GPU clusters, scheduling, high-speed networking, storage, reliability and capacity.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| AI Infrastructure & Platform | L1 Compute and hardware; also L3 Inference and ML platforms | Verified (V) | #7 of 24 | #8 of 24 · band A · Monte Carlo rank 8 (P10–P90 6–13) | D2 Platform & infrastructure |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 5.5 (4–7) | C | 52 base-disclosing postings in S09 [T0-03]; Inference Jobs 446 GPU Infrastructure Engineering listings (undeduplicated upper bound); active hyperscaler, neocloud and frontier-lab hiring [T0-54]. |
| Pay | 7 (6–8) | B | US posted-base median midpoint $261K (n=12): frontier labs/AI-native ~$360K (OpenAI $230K–$490K + equity [A], Anthropic $320K–$485K [A, COI]) vs cloud/neocloud/enterprise $180K–$270K [T0-44, T0-54]. |
| Durability | 7.5 (6–9) | D | Judgement. Physical fleets, networking and reliability (distributed-systems minimum in top-band JDs [T0-03 J1]); agent-driven fleet automation/self-healing appears in 4 postings (OpenAI, Anthropic x2, fal) while capacity, topology and failure ownership stays with engineers [T0-54 KF12]. |
| Leverage | 8.5 (7.5–9.5) | D | Judgement. Multi-thousand-GPU cluster uptime, capacity and estate cost (8.5–9 anchor: large cost line) [T0-54]. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4.5 (3.5–6) | B | 10 of 35 core postings (28.6%) in India: NVIDIA x4 (DGX Cloud, SRE research clusters, NCX, EngOps), Deloitte USI x2, Sarvam AI x2, AION and Soket AI Labs; 0 GCC postings found in window [T0-54]. |
| India pay | 6.5 (5–8) | D | No India evidence: 0 of 10 India postings disclose pay [T0-45, T0-54 K6]. |

India rank (CCI with India inputs): #5 of 24. One input (India comp) is a Grade D placeholder.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 7 | ○ 2.5 | ○ 2.5 | ○ 1 | ○ 3.5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Linux, Kubernetes, Networking, Terraform / IaC, Python (production), SRE (SLOs, on-call, incidents), Observability (OpenTelemetry traces, metrics), GPU fleet ops & scheduling.
- **Important (headline):** Git & CI/CD, Docker, AWS / Azure / GCP, System design, NCCL / RDMA / InfiniBand, Checkpointing & storage throughput, Hardware-fault reliability, Capacity & GPU/API cost governance.
- **Full inventory:** 59 skills (Must 8 · Important 17 · Should 21 · Optional 13), each with its evidence and posting keywords: [ai-infrastructure-engineer.md](../../03-skills-and-tech/inventories/ai-infrastructure-engineer.md).
- **Prerequisites:** Infrastructure depth; best feeders are SRE, DevOps and backend infrastructure engineers
- **Credentials (tie-breakers, not skills):** Certified Kubernetes Administrator (CKA) (Optional: intermediate live CLI exam ($445); CNCF KCSP requires 3+ CKA; 0/35 direct AI infra JD mentions); NVIDIA-Certified Professional: AI Infrastructure (NCP-AII) (Optional: $400, 70-75 Q + hands-on lab included (76% cluster bring-up/test/troubleshooting); top GPU infra exam (T0-32:L585, T0-54:L258)); NVIDIA-Certified Professional: AI Operations (NCP-AIO) (Optional: $500, 30 MCQ + 3 live VM labs (only NVIDIA exam with confirmed live lab split); targets GPU cluster operations (T0-32:L599, T0-54:L259)); NVIDIA-Certified Associate: AI Infrastructure and Operations (NCA-AIIO) (Optional: $125 (50 Q, 60 min; 40% AI infra, ~7h prep); entry-level stepping stone ahead of NCP-AII/NCP-AIO (T0-32:L459, L588; T0-54:L260)); Certified Kubernetes Application Developer (CKAD) (Optional: CNCF Certified Kubernetes Application Developer (live CLI exam); complements CKA for GPU/ML workload deployment (T0-32)); Certified Kubernetes Security Specialist (CKS) (Optional: CNCF Certified Kubernetes Security Specialist (requires active CKA); relevant for multi-tenant GPU cluster security (T0-32)); NVIDIA-Certified Professional: Generative AI LLMs (NCP-GENL) (Optional: announced (verify live Certiverse booking); NCP-AII and NCP-AIO target GPU infra more directly). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A self-hosted cluster with continuous synthetic load, automated failover, autoscaling and dashboards, plus a written postmortem
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P6 Self-hosted LLM platform on Kubernetes](../../05-portfolio/project-archetypes.md#p6) (60%); [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (25%); [P20 Responsible-AI compliance packet with runtime guardrails](../../05-portfolio/project-archetypes.md#p20) (15%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Infrastructure.** It tests sub-discipline specific: serving and inference (systems coding, distributed-systems design; KV-cache maths, decode roofline, continuous batching and prefill/decode disaggregation appear in prep guides [C]), GPU cluster ops (Slurm, InfiniBand/RDMA, NCCL debugging, bare-metal failure recovery, Kubernetes at scale), MLOps/ML platform (IaC, CI/CD, drift monitoring, feature stores, ML job schedulers) and GPU kernels (simulated-accelerator take-home [A, COI], profiler walkthrough, roofline analysis, numerics/dtype tolerances). Source: T0-14, T0-46, T0-54, T0-56, T0-58, T0-63, T1-03.
- **Practise:** the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** D2 Platform & infrastructure (AI Systems & Infrastructure); headline pattern: "AI Infrastructure Engineer: GPUs, Kubernetes, model serving". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** GPU, Kubernetes, infrastructure, distributed systems, NCCL, InfiniBand, SRE, Terraform (DevOps JDs: Kubernetes 69.4%, Terraform 59.1%, Linux 45.1%)
- **Leave out or reframe:** Listing Slurm or parallel storage systems (Lustre, Weka) you have not operated at cluster scale (Slurm appears in 15/35 T0-54 postings); generic DevOps bullets with no GPU scale
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ai-infrastructure-engineer).

## Specialisations inside this role

- **Pre-training at scale** (L2 Foundation models and research): Candidate title (ungraduated): live pre-training postings at 4 employers and Distributed Training Engineer at OpenAI/Periodic Labs in Nov 2026 [C · T0-69 K17–K18; ERRATA U38], role catalog §5.2.
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [ML Platform / MLOps Engineer](ml-platform-engineer.md) (0.45); [Inference / LLM Serving Engineer](inference-engineer.md) (0.15); [AI Engineer](ai-engineer.md) (0.13).
- **Same family (AI Infrastructure & Platform):** [Inference / LLM Serving Engineer](inference-engineer.md), [GPU Kernel / ML Compiler Engineer](gpu-kernel-engineer.md), [ML Platform / MLOps Engineer](ml-platform-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ai-infrastructure-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ai-infrastructure-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A November 2026 sample of 35 job descriptions (`n = 35`, 12 opened in full on employer boards) shows that "AI Infrastructure / GPU Platform Engineer" is four distinct jobs sharing a compute-estate core rather than one uniform role [M · T0-54 L56, L112–118]:

| Variant | Sample share | Typical employers and titles | Distinguishing technical asks |
|---|---|---|---|
| **A. Fleet and host-systems lifecycle** | 11/35 (31%) | OpenAI (GPU Infrastructure, Compute Foundations, Frontier Clusters); Anthropic (Node Infra, Cluster Infrastructure); CoreWeave (Server Fleet, Compute Services) | Kubernetes at scale (10/11), Go or Python (6/11 each), bare-metal bring-up, OS images, firmware, automated node repair; Slurm 0/11 |
| **B. GPU platform, control plane and scheduler** | 9/35 (26%) | Sarvam AI (Platform Engineer); Microsoft (Principal AI Infrastructure, CoreAI); Anthropic (Kubernetes Platform); Perplexity; fal; NVIDIA DGX Cloud; AION; Deloitte | Kubernetes controllers, operators and CRDs, gang scheduling (Kueue, Volcano, Run:ai), MIG/MPS, observability; Slurm 6/9 |
| **C. HPC/Slurm cluster engineering and bring-up** | 11/35 (31%) | Prime Intellect; NexGen Cloud; IFM; H Company; Meta (AI/HPC Production Engineer); Microsoft Supercomputing; Soket AI Labs; Deloitte USI; Office Beacon | Slurm (8/11), InfiniBand/RoCE/NCCL (9/11), GPU drivers and firmware, parallel storage (Weka, Lustre, BeeGFS, GPFS), NCCL/HPL validation, customer-facing deployment |
| **D. SRE and cluster operations** | 4/35 (11%) | NVIDIA (SRE AI Research Clusters, NCX, EngOps Cluster Operations); Sarvam AI (Infrastructure SRE – HPC) | Operated-at-scale evidence (such as 2,000+ GPUs), on-call rotas, interconnect telemetry (3/4); Sarvam explicitly separates "build" (variant B) from "operate" (variant D) |

**Key realities that revise the Phase 0 scorecard above:**
- **Not an ML-modelling job:** machine-learning modelling knowledge is a Must in 0 of 35 postings [M · T0-54 L46, L314]. Even GPU or accelerator experience is not universal: among the 12 postings opened in full, 6 require it, 4 treat it as a bonus or one of several acceptable backgrounds, and 2 do not ask for it (Anthropic London Cluster Infrastructure and CoreWeave Compute Services) [M · T0-54 L58, L568].
- **Kubernetes is dominant, but not the whole stack:** Kubernetes appears in 80.0% of all 35 postings (91.7% of the 12 read in full), yet OpenAI's Compute Foundations Systems role is a pure Linux kernel, driver, OS-image and firmware role with no Kubernetes requirement [M · T0-54 L56–57, L483]. Conversely, Slurm appears in 42.9% overall (50.0% full-read) and 62.5% (15/24) across variants B, C and D, while appearing in 0/11 variant A postings [M · T0-54 L57, L181].
- **Skill-tier shifts vs the DevOps feeder baseline:** GPU fleet operations (94.3% all-35; 83.3% full-read), Kubernetes (80.0%; 91.7%), networking including InfiniBand/RDMA (51.4%; 83.3%) and Linux (34.3%; 66.7%) form the Must core [M · T0-54 L172–175]. Slurm (42.9%; 50.0%) and Go (31.4%; 66.7%, especially variants A and B) are prominent omissions from the Phase 0 headline card, while parallel storage (22.9%; 33.3%) and Ansible (20.0%; 33.3%) recur in bring-up roles [M · T0-54 L181–189]. The Phase 0 DevOps-feeder shares for DevOps (99.0%), Git/CI (81.2%) and Docker (53.4%) are not reproduced even in the full-read subset (8.3%, 25.0% and 25.0%) [M · T0-54 L70, L187–196].
- **Training vs inference split:** 27/35 postings (77.1%) cover mixed training and inference estates, 6/35 (17.1%) are training-primary and 2/35 (5.7%) are inference-primary; "pre-training" appears in 0/35 titles [M · T0-54 L69, L290].
- **Proof of work and résumé positioning:** No named hiring-manager statement on portfolio projects was found, so the Phase 0 self-hosted cluster recommendation is unverified [D · T0-54 L246, L252]. Postings ask for operated-at-scale evidence (10,000+ nodes at Anthropic staff level, 2,000+ GPUs at NVIDIA SRE, 1,000+ GPUs as a plus at Prime Intellect), NCCL/HPL validation (NexGen) and open-source work on Kubernetes, Linux kernel, scheduling or HPC [A/B · T0-54 L247–250]. A home lab cannot prove employer-scale reliability, though it can still demonstrate Slurm, GPU Operator and observability mechanics [P · T0-54 L252]. Because Slurm (15/35) and parallel storage products (8/35) are widely named, the résumé rule is to list only schedulers and storage systems operated in production — never drop genuine Slurm or Lustre/Weka experience, and quantify fleet scale on every bullet [M/P · T0-54 L303, L361, L607–608].

## Employer landscape and title confusion

**Employer mix and demand context (November 2026):** In the 35-posting sample, frontier and AI labs make up 40.0% (14: OpenAI ×6, Anthropic ×3, Sarvam ×2, IFM, H Company, Soket), neoclouds and AI-native infrastructure startups 25.7% (9: CoreWeave ×3, Perplexity, Prime Intellect, fal, NexGen, Nebius-like, AION), Big Tech and semiconductors 22.9% (8: NVIDIA ×4, Microsoft ×3, Meta), and enterprises/consultancies 11.4% (4: Deloitte USI ×2, Edvantis, Office Beacon), with 0 in-window GCC postings [M · T0-54 L62, L153]. Because the sample is search-surfaced, it over-represents large labs. No clean title-level volume exists: niche aggregators show 630 "MLOps / Infrastructure Engineer" listings across 265 startups on Fast AI Jobs (a noisy category containing unrelated systems roles, snapshot undated, dated items to 2026-06-16) and 446 "GPU Infrastructure Engineering" listings on Inference Jobs (undated) [B · T0-54 L61, L137–140, L397].

**Title fragmentation and boundaries:**
- **Literal catalog aliases are rare:** "AI Infrastructure Engineer" or "AI Infra Engineer" appears in only 3 of 35 titles (NVIDIA DGX Cloud, Perplexity, Office Beacon); "ML Infrastructure Engineer", "GPU Cluster & Infra Platform Engineer" and "Distributed Training Engineer" appear in 0 of 35 [M · T0-54 L119].
- **Titles to search instead:** *Software Engineer, GPU Infrastructure / Compute Foundations / Frontier Clusters* (OpenAI); *Staff+ Infrastructure / Node Infra / Kubernetes Platform Engineer* (Anthropic); *HPC Engineer / HPC Infrastructure Engineer*; *Principal Software Engineer, AI Infrastructure / CoreAI / Supercomputing Operations* (Microsoft); *Production Engineer, AI/HPC Systems* (Meta); *Member of Technical Staff, GPU Infrastructure* (Prime Intellect); *Cloud Integrated Infrastructure Engineer (AI Infra/HPC)* (Deloitte USI); *SRE, AI Research Clusters / Infrastructure SRE – HPC / EngOps Cluster Operations / NCX Senior Engineer* (NVIDIA, Sarvam); and *Platform Engineer, AI Infrastructure* (Sarvam) [M · T0-54 L120–127].
- **Boundaries with adjacent roles:** SRE and HPC systems administration sit inside variants C and D, whereas GPU kernel/performance engineering, network-only engineering, runtime/sandbox engineering, generic Kubernetes platform roles without a GPU core, and application-side "AI production engineer" postings sit outside the role (22 of 73 screened candidates were excluded on scope) [M · T0-54 L44, L131].
- **Mirror staleness and operational caveats:** In 16 conclusive employer-board liveness checks on 2026-11-13, 3 postings (18.8%) had already closed while mirrors still listed them (Anthropic London Kubernetes/Accelerator, E2E Networks, Deloitte India LLP) [M · T0-54 L68, L162, L400]. Always confirm openings on the employer's own ATS board. Also check operational terms before applying: several neocloud, vendor and consultancy postings carry customer-facing pre-sales/field duties (Prime Intellect, NVIDIA NCX, Deloitte) or explicit 24/7 or rotating on-call (Prime Intellect, CoreWeave, NexGen) [A/B · T0-54 L323].
- **Credentials:** Certifications are named in only 2 of 35 postings (5.7%: Prime Intellect and Office Beacon, both preferred), and CKA in 0 of 35 [M · T0-54 L65, L256]. **Credential focus:** `NCP-GENL` is an LLM training/fine-tuning exam rather than a GPU-infrastructure credential; NVIDIA's dedicated infrastructure credentials (verified 2026-10-16 and live-checked 2026-11-19) are **NCP-AII** ($400, 120 min, 70–75 questions: 31% server bring-up, 33% cluster test) and **NCP-AIO** ($500, 120 min, 30 questions plus 3 live hands-on labs on Slurm, Kubernetes and Base Command Manager), plus associate **NCA-AIIO** (~$125–135) [A/B · T0-54 L65, L257–263]. Both professional exams suit variants C and D (data-centre, partner and consultancy routes), not lab software roles; see [credential ROI](../../04-certifications/credential-roi.md).

## Career path, India demand and market signals

**Seniority and entry routes:** The market is overwhelmingly senior: 0/35 postings are entry-level, 2/35 mid, 14/35 senior, 8/35 staff/principal/lead and 11/35 unspecified, with a median stated minimum of 5 years (`n = 10`) and 10+ years preferred at Anthropic staff level [M · T0-54 L59, L155–156]. Fast AI Jobs lists only 6 entry-level openings against 630 in its broader MLOps/Infrastructure category (~1%) [B · T0-54 L59, L139]. A degree is stated in only 3/35 postings (Anthropic ×2 bachelor's or equivalent; Deloitte USI named engineering degrees) [M · T0-54 L157, L267].
- **Strongest feeders (revising K13):** Production SREs and platform engineers with Kubernetes at scale (variants A, B, D); **Linux kernel, OS-image and firmware engineers** (host-systems postings in variant A such as OpenAI Compute Foundations Systems and Anthropic Node Infra); **HPC/systems administrators** (variant C, adding Go/Python and Kubernetes controllers for lab roles); and backend engineers targeting control-plane/scheduler roles (variant B), where some staff postings do not require prior GPU experience [B/D · T0-54 L75–82, L268–276]. Early-career candidates and data scientists face low direct access and should build production SRE, platform or HPC operations experience first [D · T0-54 L83, L277–280].

**Progression and durability:** IC ladders extend through Senior, Staff, Senior Staff and Principal, with lateral exits into GPU kernel/performance engineering, network production engineering, research engineering, field/solutions architecture or engineering management [B · T0-54 L284]. Durability evidence is mixed as of November 2026: physical fleets, high-speed fabrics and host kernel/firmware reliability anchor the role, yet four sampled postings explicitly embed AI-driven or agent-driven fleet operations and automated repair (OpenAI London, Anthropic Cluster Infrastructure and Node Infra, fal) [B/C · T0-54 L67, L285]. Ownership of capacity strategy, topology and failure diagnosis remains with the engineer, while routine operational toil is the primary automation target [C · T0-54 L67, L285].

**Pay signals and geography:** Detailed pay tables live in [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). The T0-54 dossier confirms the scorecard's central US band and upgrades the top-end ceiling to Grade A on employer boards, showing that **employer tier drives a nearly 2× spread**: the US sample median of posted base midpoints is $261K (`n = 12`, M), splitting into $360K at frontier labs and AI-native firms (`n = 6`, with OpenAI posting $230K–$490K plus equity and Anthropic $320K–$485K US / £325K–£485K London [A, COI for Anthropic]), $209K at Big Tech (Microsoft Principal, `n = 3`, B), and $198K at neoclouds/startups (CoreWeave and Prime Intellect, `n = 3`, A/B), against broad aggregator medians of $171.6K–$175K [M/B · T0-54 L60, L204–227]. Beware currency and title traps: Microsoft Principal bands sit well below OpenAI's general band, and Anthropic posts nearly identical headline figures in GBP and USD [A/B · T0-54 L227, L318, L322]. Geographically, US hubs lead (SF/Sunnyvale, Seattle/Redmond/Bellevue, NY/NJ), followed by Europe (London first, then Paris, Amsterdam, Berlin) and India; only 5/35 postings (14.3%) are remote-eligible, with hybrid or on-site norms (such as Anthropic's 25% office minimum and Sarvam/IFM on-site) [M · T0-54 L62, L294–295].

**Sponsorship (pointers, not legal advice):** Among the 12 full-read postings, 4 state visa sponsorship (Anthropic ×2, Prime Intellect, IFM), 1 requires UK right to work without sponsorship (NexGen), and 7 are silent [A · T0-54 L63, L296]. Secondary DOL LCA data show 311 certified LCAs at OpenAI OpCo and 55 at CoreWeave across all titles (FY2025 to FY2026 Q3; filings are not pay) [B · T0-54 L63, L297]. Under DHS final rule 90 FR 60864 (effective 2026-02-27), cap-subject H-1B selection is weighted by offered wage level — verify live regulatory and litigation status on USCIS and in [visa and relocation](../../11-tracks/visa-and-relocation.md) before acting [B · T0-54 L63, L298, L411].

**India demand and nuance (revising the Phase 0 "No India evidence" placeholder):** T0-54 surfaces 10 of 35 postings (28.6%) in India — **NVIDIA India ×4** (DGX Cloud, SRE AI Research Clusters, NCX, EngOps Cluster Operations), **Deloitte USI ×2**, **Sarvam AI ×2** (Platform Engineer and Infrastructure SRE – HPC), **AION** (observability-led) and **Soket AI Labs** — centred in Bengaluru, Hyderabad, Pune, Chennai and Gurugram [B/M · T0-54 L64, L328]. Total India volume remains unmeasured, and **0 in-window GCC postings** entered the sample (Dell and Cisco Bengaluru CoE postings fell outside the 90-day window; E2E Networks removed its Accelerated Computing Engineer listing, though E2E targets GCCs as GPU-cloud customers) [A/C · T0-54 L64, L329]. Experience bars are high (5+ years at Sarvam and NVIDIA DGX Cloud; 6–9 years at Deloitte USI; 6–10 years at AION) [A/B · T0-54 L331]. Sarvam's bonus list explicitly values familiarity with Indian NVIDIA Cloud Partners (NCPs) and sovereign/partner GPU clouds (DGX SuperPOD, Lambda, CoreWeave, NeevCloud) [A · T0-54 L333]. **India pay remains an absence:** 0 of 10 postings disclose pay, and only non-title-matched proxies exist (see [pay benchmarks](../../09-compensation/pay-benchmarks.md)) [D · T0-54 L229, L332].

## Interview themes and preparation notes

The generated card assigns the **Infrastructure** track; T0-54 shows that Phase 0's inference-serving topic list (KV-cache maths, decode roofline, continuous batching) only partly fits `ai-infrastructure-engineer` and adds cluster-operations depth [C · T0-54 L66, L242]:
- **What is corroborated:** Anthropic's application form states that its coding rounds mirror on-the-job work rather than LeetCode-style puzzles, lets candidates pick a language, and requires agreement to AI partnership guidelines (secondary reports say AI is permitted for drafting/preparation and restricted in live rounds and take-homes unless stated) [A for form, COI; C for details · T0-54 L66, L235]. Prep sites report an inference-API design round (batching, KV cache, GPU utilisation) at Anthropic [C · T0-54 L236].
- **Cluster-operations themes (added from T0-54 to the Infrastructure track):** Prep reports for xAI, CoreWeave and OpenAI (backend-adjacent) and job-posting requirements point to **GPU cluster architecture, Kubernetes at scale (apiserver, etcd, custom controllers, device plugins), Slurm and topology-aware gang scheduling, InfiniBand/RDMA/NCCL throughput and debugging, parallel storage bottlenecks, bare-metal Linux/kernel/firmware debugging, automated node health and failure recovery, and capacity planning** [C · T0-54 L238–242].
- **Preparation focus (no model answers, per D-018):** Classify which of the four variants the loop targets before revising; pair the [infrastructure prep pack](../../08-interviewing/prep-packs.md#infrastructure-pack) with distributed-systems and cluster-operations drills, and prepare concrete production incident post-mortems covering hardware, fabric or scheduler failures [P · T0-54 L242, L309]. See [interview loops](../../08-interviewing/interview-loops.md) for cross-employer loop structure. No India-specific loop evidence or neocloud AI-tool policy was found [E · T0-54 L242, L374].

## Dossier evidence and limits

- **Sample and access:** 35 sampled postings (plus 1 supplementary duplicate excluded from shares) from 73 examined candidates, retrieved 2026-11-13 (anchor 2026-11-11, 90-day window from 2026-08-13). Only **12 of 35 (34%) were opened in full** on employer boards (Grade A); 23 were read from search extracts or mirrors (Grade B/C), so all-35 skill shares are lower bounds while full-read shares come from a convenience subset lacking Big Tech and NVIDIA (wide 95% intervals: roughly ±16 pp at `n = 35`, ±28 pp at `n = 12`) [M · T0-54 L22, L166]. Two OpenAI pages blocked automated fetches and were not circumvented [T0-54 L42, L162].
- **Sampling bias and COI:** Search-surfaced English-only sampling over-represents frontier labs (40% of the sample) and under-represents GCCs, smaller firms and non-English markets [T0-54 L43, L384]. The session was authored by an Anthropic model, and Anthropic accounts for 3 of 35 postings plus 1 supplementary duplicate and the primary application-form loop statement; all Anthropic rows carry explicit COI disclosures [T0-54 L13, L412].
- **Date and source hygiene:** 9 of 12 full-read employer pages carry no posting date, and 3 opened postings carried July 2026 dates (older than 90 days) while remaining live [T0-54 L160, L379, L403]. Model-derived city salary pages (such as Orbyt) were graded E and rejected [T0-54 L407].
- **Explicit absences (not measured as of 2026-11-13):** live title-level LinkedIn/Indeed volume by country; a title-matching Levels.fyi page; employer-posted or title-matched India pay; in-window India GCC postings; named hiring-manager proof-of-work statements; published analyses of prior roles of hired engineers; neocloud and India interview loops; full CKA/NCA-AIIO official page reads; and official DOL LCA / full DHS rule text reads [E · T0-54 L365–379].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
