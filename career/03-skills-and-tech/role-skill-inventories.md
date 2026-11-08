---
id: skills.inventories
title: "GenAI Role Skill Inventories"
content_type: index
stage: 3
status: published
last_verified: 2026-11-04
review_by: 2027-01-21
summary: "Index of the complete typed skill inventory per role, with cross-role views for universal and family resumes, the tier decisions, verification, and the requirements and tier rule behind the skills ontology."
sources: [T0-03, T0-06, T0-13, T0-14, T0-15, T0-16, T1-03]
generated_by: "scripts/build_skills.py (generated blocks)"
---
# GenAI Role Skill Inventories
## Every Skill for Every Role: Typed, Tiered and Evidence-Tagged, From One Ontology

> **Updated:** 2026-11-04 · **Scope:** Comprehensive typed skill inventories across 24 IC roles and 2 leadership tracks.
> **What this is:** the complete skill inventory for each of the 24 individual-contributor GenAI roles and the 2 employed leadership tracks. Each inventory covers:
> - technical knowledge: concepts and methods;
> - concrete technologies: languages, frameworks, libraries, models, platforms, data stores, infrastructure tools, specialised products, hardware, protocols and regulations;
> - non-technical skills: communication, behavioural competencies, business, leadership, domain knowledge and research craft.
>
> Every skill has a tier (Must → Avoid) and an evidence tag.
>
> **Source of truth:** [data/skills_ontology.json](../../data/skills_ontology.json). The per-role files in [inventories/](inventories/) and the generated blocks below are rebuilt by `python3 -B scripts/build_skills.py --update`; [AGENTS.md §2](../../AGENTS.md#2-sources-of-truth) lists the generators to run after a data change. How the ontology is designed is in §5.
>
> **Companions:**
> - [skills-vocabulary.md](skills-vocabulary.md): every skill, typed, with aliases, relations, status and corpus mentions.
> - [resume-skills-matrix.md](../06-job-search/resume-skills-matrix.md): the concise resume layer and the variant blueprints.
> - [resume-strategy.md](../06-job-search/resume-strategy.md): the resume system.
> - [role-skill-maps.md](role-skill-maps.md): narrative skill maps.
> - [genai-target-roles.md](../02-roles/genai-target-roles.md): the target order.

---

## 0. How to Use It

**One role:**
1. Open the role's inventory from the index (§1).
2. **Skills section:** list the Must and Important skills that are true for you, in the posting's wording.
   - Group them under resume headings by type: Languages; Frameworks & libraries; Cloud & platforms; Data; Infrastructure; Evaluation, observability & security tools; Protocols & standards.
3. **Bullets:** prove concepts and methods with a measured result. Show non-technical skills rather than listing them.
4. **Gaps:** fill in the self-assessment table in each file (§7 there), using the 0–3 scale and the V0–V3 evidence ladder. Close Must gaps first, then build two or three Important skills into proof of work.
5. **Per posting:** swap in the Should and Optional skills the posting names, and use the keyword list (§6 in each file) to mirror its wording when true.

**A family or universal resume:** take the variant's anchor role from the [resume matrix blueprints](../06-job-search/resume-skills-matrix.md), then add the sibling roles' Must and Important skills. §2 shows which skills recur across roles.

**Key:**

| Tier | Meaning |
|---|---|
| **Must** | Screen gate: role-defining, or named in most postings |
| **Important** | Differentiators that win interviews and level |
| **Should** | Common supporting skills; list them if true |
| **Optional** | Employer-specific or frontier; include only when the posting names it |
| **Avoid** | Archived, dormant, deprecated or devalued; leave it out, or reframe it |

**Tier rule.** Where a measured share of postings exists, the tier follows it: about 50% or more is Must, 20–50% is Important, and lower is Should or Optional. A role-defining skill can depart from the rule, and the link's note says why; the measured decisions are listed in §3.

| Tag | Evidence | Grade |
|---|---|:---:|
| [JD x%] | Share of live postings for the title, or for a labelled feeder or adjacent title, that name the skill (JobsPipe, retrieved 2026-11-02) | B |
| [S09 x%] | Share of the 3,647-posting S09 corpus ([T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) §6.3; skews senior and infra) | B |
| [S · T0-xx] | Named for the role in a research session or in a job description cited there; the ontology stores the exact session lines | A–C |
| [P] | Practice-curated: standard for the role but not evidenced in the corpus; check it against 10–20 live postings before investing heavily | D |

**How the inventories were built** (2026-11-04):
1. **Vocabulary.** The 138 skills of the initial headline matrix were typed and their bundles split: interchangeable tools became choose-one classes, and complementary tools became concepts implemented by individual tools. Added to them:
   - every technology named in the research sessions and the role skill maps;
   - the JobsPipe skill terms that had no match;
   - the T1-03 behavioural competencies C1–C4;
   - common practice-curated tools;
   - the skills the role agents proposed.
2. **Assignment.** One agent per role family drafted each inventory from the catalogs (including the role's skill map in [role-skill-maps.md](role-skill-maps.md) §3, as it stood on 2026-11-04), the initial headline tiers and the sessions, citing exact session lines for every [S] link. Tiers follow measured shares where they exist. A checker enforced:
   - coverage of all 19 types, or a stated reason why a type does not apply;
   - the evidence formats;
   - the status rules.
3. **Verification.** A scripted check matched every posting share to its source and every [S] link to a session line that names the item, and low-relevance lines plus a random sample were read by hand (§4). The planned independent agent fact-check of every link was blocked by the model quota on 2026-11-04 and has not been run ([ROADMAP](../../ROADMAP.md) P1-5).

---

## 1. Role Index

<!-- BEGIN GENERATED: scripts/build_skills.py (role index) -->
| Rank | Role | Variant | Skills | Must | Important | Should | Optional | Avoid | Evidenced (JD · S09 · S) | Practice-curated | Non-technical | Inventory |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| #1 | AI Engineer | A1 | 148 | 4 | 20 | 59 | 63 | 2 | 14 · 7 · 88 | 39 (26%) | 12 | [open](inventories/ai-engineer.md) |
| #2 | Machine Learning Engineer (GenAI/LLM track) | B1 | 84 | 4 | 18 | 28 | 34 | 0 | 11 · 2 · 24 | 47 (56%) | 9 | [open](inventories/ml-engineer.md) |
| #3 | Research Engineer / Member of Technical Staff | C1 | 59 | 6 | 14 | 18 | 21 | 0 | 6 · 1 · 26 | 26 (44%) | 11 | [open](inventories/research-engineer.md) |
| #4 | Forward Deployed Engineer (AI) | A2 | 57 | 5 | 15 | 17 | 20 | 0 | 2 · 0 · 28 | 27 (47%) | 18 | [open](inventories/forward-deployed-engineer.md) |
| #5 | Applied Scientist (GenAI/LLM teams) | B2 | 64 | 6 | 17 | 25 | 16 | 0 | 13 · 1 · 15 | 35 (55%) | 13 | [open](inventories/applied-scientist.md) |
| #6 | Applied AI Engineer | A2 | 46 | 4 | 16 | 14 | 12 | 0 | 11 · 0 · 10 | 25 (54%) | 12 | [open](inventories/applied-ai-engineer.md) |
| #7 | AI Infrastructure / GPU Platform Engineer | D2 | 59 | 7 | 17 | 22 | 13 | 0 | 12 · 3 · 26 | 18 (31%) | 7 | [open](inventories/ai-infrastructure-engineer.md) |
| #8 | Research Scientist (LLM research) | C2 | 54 | 6 | 16 | 16 | 16 | 0 | 10 · 0 · 6 | 38 (70%) | 14 | [open](inventories/research-scientist.md) |
| #9 | Inference / LLM Serving Engineer | D1 | 71 | 7 | 17 | 26 | 20 | 1 | 0 · 6 · 49 | 16 (23%) | 8 | [open](inventories/inference-engineer.md) |
| #10 | Agentic AI Engineer | A1 | 73 | 5 | 18 | 31 | 17 | 2 | 4 · 1 · 55 | 13 (18%) | 10 | [open](inventories/agentic-ai-engineer.md) |
| #11 | ML Platform / MLOps (LLMOps) Engineer | D2 | 77 | 7 | 15 | 34 | 21 | 0 | 12 · 5 · 34 | 26 (34%) | 6 | [open](inventories/ml-platform-engineer.md) |
| #12 | AI Product Manager | E1 | 47 | 4 | 16 | 20 | 7 | 0 | 9 · 0 · 15 | 23 (49%) | 24 | [open](inventories/ai-product-manager.md) |
| #13 | AI Evaluation Engineer | A1 | 65 | 5 | 19 | 28 | 12 | 1 | 5 · 3 · 42 | 15 (23%) | 10 | [open](inventories/ai-evaluation-engineer.md) |
| #14 | AI / GenAI Solutions Architect | A2 | 56 | 5 | 17 | 25 | 9 | 0 | 12 · 0 · 12 | 32 (57%) | 20 | [open](inventories/ai-solutions-architect.md) |
| #15 | GPU Kernel / ML Compiler Engineer | D1 | 45 | 6 | 15 | 11 | 13 | 0 | 0 · 2 · 30 | 13 (29%) | 7 | [open](inventories/gpu-kernel-engineer.md) |
| #16 | AI Security Engineer / AI Red Teamer | D3 | 49 | 7 | 14 | 19 | 9 | 0 | 8 · 0 · 26 | 15 (31%) | 7 | [open](inventories/ai-security-engineer.md) |
| #17 | AI Governance Programme Lead / Manager | E2 | 58 | 6 | 21 | 19 | 12 | 0 | 0 · 0 · 38 | 20 (34%) | 16 | [open](inventories/ai-governance-lead.md) |
| #18 | Physical AI / Robotics AI Engineer | B3 | 42 | 6 | 14 | 18 | 4 | 0 | 1 · 0 · 4 | 37 (88%) | 8 | [open](inventories/physical-ai-engineer.md) |
| #19 | Frontier AI Safety / Alignment Researcher | C2 | 41 | 4 | 13 | 20 | 4 | 0 | 5 · 0 · 12 | 24 (59%) | 11 | [open](inventories/ai-safety-researcher.md) |
| #20 | AI Enablement Engineer | A1 | 51 | 4 | 14 | 22 | 11 | 0 | 2 · 0 · 16 | 33 (65%) | 13 | [open](inventories/ai-enablement-engineer.md) |
| #21 | AI Product Engineer (AI Frontend) | A1 | 53 | 5 | 17 | 17 | 14 | 0 | 8 · 0 · 20 | 25 (47%) | 8 | [open](inventories/ai-product-engineer.md) |
| #22 | AI Risk, Audit & Compliance Specialist | E2 | 47 | 5 | 18 | 14 | 10 | 0 | 0 · 0 · 30 | 17 (36%) | 9 | [open](inventories/ai-risk-assurance-specialist.md) |
| #23 | Responsible AI / AI Governance Engineer | E2 | 56 | 3 | 20 | 26 | 7 | 0 | 0 · 0 · 45 | 11 (20%) | 9 | [open](inventories/responsible-ai-engineer.md) |
| #24 | Domain Evaluation Specialist / AI Trainer | E3 | 42 | 4 | 7 | 19 | 12 | 0 | 0 · 0 · 14 | 28 (67%) | 16 | [open](inventories/domain-evaluation-specialist.md) |
| L1 | AI Engineering Manager / Director | L1 | 44 | 4 | 16 | 17 | 7 | 0 | 7 · 0 · 5 | 32 (73%) | 24 | [open](inventories/ai-engineering-manager.md) |
| L2–L3 | VP / Head of AI / CAIO | L2 | 41 | 4 | 14 | 17 | 6 | 0 | 2 · 0 · 9 | 30 (73%) | 25 | [open](inventories/vp-head-of-ai.md) |
<!-- END GENERATED -->

---

## 2. Cross-Role Views: What Recurs (For Universal and Family Resumes)

<!-- BEGIN GENERATED: scripts/build_skills.py (cross-role views) -->
**Concrete technologies most often at Must or Important across the 19 engineering and research roles:**

| Skill | Type | Must or Important in | Listed at any tier in |
|---|---|:---:|:---:|
| Python (production) | Programming language | 18 (95%) | 19 (100%) |
| AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | Platform / cloud service | 7 (37%) | 12 (63%) |
| PyTorch | Framework / SDK | 5 (26%) | 6 (32%) |
| C++ | Programming language | 4 (21%) | 6 (32%) |
| Kubernetes | Infrastructure / DevOps tool | 3 (16%) | 10 (53%) |
| Docker | Infrastructure / DevOps tool | 2 (11%) | 12 (63%) |
| MCP (Model Context Protocol) | Protocol / standard | 2 (11%) | 9 (47%) |
| Amazon Web Services (AWS) | Platform / cloud service | 2 (11%) | 7 (37%) |
| Linux | Infrastructure / DevOps tool | 2 (11%) | 5 (26%) |
| Terraform | Infrastructure / DevOps tool | 2 (11%) | 4 (21%) |
| vLLM / SGLang / TensorRT-LLM (choose 1: vLLM \| SGLang \| TensorRT-LLM) | Framework / SDK | 2 (11%) | 4 (21%) |
| OAuth 2.x | Protocol / standard | 1 (5%) | 9 (47%) |
| NVIDIA Hopper (H100 / H200) | Hardware / accelerator | 1 (5%) | 7 (37%) |
| OWASP Top 10 for LLM Applications | Regulation / framework | 1 (5%) | 7 (37%) |
| Agent frameworks (choose 1: LangGraph \| OpenAI Agents SDK \| Claude Agent SDK \| Pydantic AI \| Microsoft Agent Framework \| Google Agent Development Kit \| LlamaIndex \| CrewAI \| Mastra) | Framework / SDK | 1 (5%) | 6 (32%) |
| SQL | Programming language | 1 (5%) | 6 (32%) |
| TypeScript / JavaScript | Programming language | 1 (5%) | 6 (32%) |
| LLM API providers (choose 1: OpenAI API platform \| Anthropic API \| Gemini API) | Platform / cloud service | 1 (5%) | 5 (26%) |
| Managed AI (choose 1: Amazon Bedrock \| Azure AI Foundry / Azure OpenAI \| Google Vertex AI) | Platform / cloud service | 1 (5%) | 4 (21%) |
| SGLang | Framework / SDK | 1 (5%) | 4 (21%) |

**Knowledge skills (concepts and methods) most often at Must or Important across the 19 engineering and research roles:**

| Skill | Type | Must or Important in | Listed at any tier in |
|---|---|:---:|:---:|
| LLM APIs & tool calling | Concept / knowledge area | 10 (53%) | 10 (53%) |
| LLM evaluation (golden sets, calibrated judges, CI gates) | Concept / knowledge area | 9 (47%) | 11 (58%) |
| ML fundamentals | Concept / knowledge area | 7 (37%) | 7 (37%) |
| Git & CI/CD | Method / practice | 6 (32%) | 9 (47%) |
| Agents & tool use | Concept / knowledge area | 5 (26%) | 8 (42%) |
| OAuth/OIDC, RBAC, SSO | Concept / knowledge area | 5 (26%) | 5 (26%) |
| Deep learning & transformers | Concept / knowledge area | 4 (21%) | 6 (32%) |
| Retrieval quality (hybrid, reranking, recall@k) | Concept / knowledge area | 4 (21%) | 5 (26%) |
| Data structures & algorithms | Concept / knowledge area | 4 (21%) | 4 (21%) |
| Observability (OpenTelemetry traces, metrics) | Concept / knowledge area | 3 (16%) | 9 (47%) |
| RAG | Concept / knowledge area | 3 (16%) | 9 (47%) |
| Eval statistics (CIs, power, pass^k) | Method / practice | 3 (16%) | 5 (26%) |
| Statistics (inference, hypothesis tests, regression) | Concept / knowledge area | 3 (16%) | 5 (26%) |
| Cost & latency engineering | Concept / knowledge area | 3 (16%) | 4 (21%) |
| Generative AI | Concept / knowledge area | 3 (16%) | 4 (21%) |
| Profiling & roofline (Nsight) | Method / practice | 3 (16%) | 4 (21%) |
| Research methods & re-implementation | Method / practice | 3 (16%) | 4 (21%) |
| Experiment design & A/B testing | Method / practice | 3 (16%) | 3 (16%) |
| LLM security (prompt injection, OWASP) | Concept / knowledge area | 3 (16%) | 3 (16%) |
| Prompt & context design | Concept / knowledge area | 3 (16%) | 3 (16%) |

**Non-technical skills most often at Must or Important across all 24 individual-contributor roles:**

| Skill | Type | Must or Important in | Listed at any tier in |
|---|---|:---:|:---:|
| Pragmatism under ambiguity (C1) | Behavioural competency | 23 (96%) | 24 (100%) |
| Responsible-AI judgement (C4) | Behavioural competency | 23 (96%) | 24 (100%) |
| Explaining probabilistic trade-offs (C2) | Behavioural competency | 23 (96%) | 23 (96%) |
| Ownership & incident response (C3) | Behavioural competency | 23 (96%) | 23 (96%) |
| Communication (written & verbal) | Communication & collaboration | 13 (54%) | 24 (100%) |
| Stakeholder communication | Communication & collaboration | 4 (17%) | 10 (42%) |
| Product sense | Business & product | 3 (12%) | 5 (21%) |
| Research taste & problem selection | Research craft | 3 (12%) | 3 (12%) |
| Domain expertise | Domain knowledge | 2 (8%) | 12 (50%) |
| Technical writing | Communication & collaboration | 2 (8%) | 7 (29%) |
| Scientific writing | Research craft | 2 (8%) | 6 (25%) |
| Token & unit economics | Business & product | 2 (8%) | 6 (25%) |
| Executive & board communication | Communication & collaboration | 2 (8%) | 4 (17%) |
| Novel research & publications | Research craft | 2 (8%) | 4 (17%) |
| Customer scoping & demos | Business & product | 2 (8%) | 3 (12%) |
| Leadership & mentoring | Leadership & people | 2 (8%) | 3 (12%) |
| Clear writing & presenting | Communication & collaboration | 2 (8%) | 2 (8%) |
| Mentoring | Leadership & people | 1 (4%) | 21 (88%) |
| Cross-functional collaboration | Communication & collaboration | 1 (4%) | 8 (33%) |
| Presenting & live demos | Communication & collaboration | 1 (4%) | 7 (29%) |
<!-- END GENERATED -->

---

## 3. Tier Decisions Backed by Measured Shares

Where a measured share of postings decided a skill's tier, the decision and its reason are listed here. The concise resume matrix is generated from the same ontology, so it uses these tiers.

<!-- BEGIN GENERATED: scripts/build_skills.py (change log) -->
| Role | Skill | Tier | Why | Stage |
|---|---|:---:|---|---|
| AI Engineer | AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | I | AWS and Azure are each named in 35.1% of AI Engineer postings (JobsPipe) | assignment |
| AI Engineer | Git & CI/CD | I | CI/CD is named in 34.4% of AI Engineer postings (JobsPipe) | assignment |
| AI Engineer | ML fundamentals | I | "machine learning" is named in 39.8% of AI Engineer postings (JobsPipe) | assignment |
| AI Engineer | Embeddings & vector search | I | vector databases are named in 32.6% of AI Engineer postings (JobsPipe) | assignment |
| Machine Learning Engineer (GenAI/LLM track) | C++ | I | C++ is named in 23.3% of ML Engineer postings (JobsPipe) | assignment |
| Machine Learning Engineer (GenAI/LLM track) | Data structures & algorithms | I | data structures are named in 33.7% of ML Engineer postings (JobsPipe) | assignment |
| Machine Learning Engineer (GenAI/LLM track) | Experiment design & A/B testing | I | A/B testing is named in 23.5% of ML Engineer postings (JobsPipe) | assignment |
| Machine Learning Engineer (GenAI/LLM track) | TensorFlow / JAX (choose 1: TensorFlow \| JAX) | I | TensorFlow is named in 31.8% of ML Engineer postings (JobsPipe) | assignment |
| Applied Scientist (GenAI/LLM teams) | SQL | I | SQL is named in 63.8% of Data Scientist postings (feeder title) | assignment |
| Applied AI Engineer | AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | I | AWS and Azure are each named in 35.1% of AI Engineer postings, the closest measured title | assignment |
| Applied AI Engineer | Git & CI/CD | I | CI/CD is named in 34.4% of AI Engineer postings, the closest measured title | assignment |
| Applied AI Engineer | Embeddings & vector search | I | vector databases are named in 32.6% of AI Engineer postings, the closest measured title | assignment |
| AI Infrastructure / GPU Platform Engineer | AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | I | AWS is named in 52.9% of DevOps Engineer postings (feeder title) | assignment |
| AI Infrastructure / GPU Platform Engineer | Docker | I | Docker is named in 53.4% of DevOps Engineer postings (feeder title) | assignment |
| AI Infrastructure / GPU Platform Engineer | Git & CI/CD | I | CI/CD is named in 81.2% of DevOps Engineer postings (feeder title) | assignment |
| Research Scientist (LLM research) | Data structures & algorithms | I | data structures are named in 26.0% of all-field Research Scientist postings (JobsPipe) | assignment |
| ML Platform / MLOps (LLMOps) Engineer | Linux | I | Linux is named in 45.1% of DevOps Engineer postings (feeder title) | assignment |
| AI Product Manager | Agents & tool use | S | "agentic AI" is named in 13.6% of Product Manager postings (feeder title) | assignment |
| AI Product Manager | GRC & risk assessment | I | "compliance" is named in 26.1% of Product Manager postings (feeder title) | assignment |
| AI Product Manager | Leadership & mentoring | I | leadership is named in 40.1% of Product Manager postings (feeder title) | assignment |
| AI / GenAI Solutions Architect | Python (production) | I | Python is named in 23.6% of Solutions Architect postings (JobsPipe) | assignment |
| AI Security Engineer / AI Red Teamer | AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | I | AWS is named in 38.8% of Security Engineer postings (feeder title) | assignment |
| AI Security Engineer / AI Red Teamer | GRC & risk assessment | I | "compliance" is named in 39.4% of Security Engineer postings (feeder title) | assignment |
| AI Security Engineer / AI Red Teamer | MCP (Model Context Protocol) | S | MCP is named in 13.0% of AI Security Specialist postings (T0-16, small sample) | assignment |
| AI Product Engineer (AI Frontend) | AWS / Azure / GCP (choose 1: Amazon Web Services \| Microsoft Azure \| Google Cloud) | I | AWS is named in 41.3% of Full-Stack Engineer postings (feeder title) | assignment |
| AI Product Engineer (AI Frontend) | Git & CI/CD | I | CI/CD is named in 37.8% of Full-Stack Engineer postings (feeder title) | assignment |
| AI Product Engineer (AI Frontend) | Python (production) | I | Python is named in 41.8% of Full-Stack Engineer postings (feeder title) | assignment |
| AI Engineering Manager / Director | GRC & risk assessment | I | "compliance" is named in 30.9% of Engineering Manager postings (feeder title) | assignment |
<!-- END GENERATED -->

<a id="posting-evidence"></a>
### Posting evidence: the measured shares behind JD tags

Every `[JD x%]` tag in the inventories is one of these shares. A tag marked (feeder), (adjacent) or (closest) borrows the share of the related title named in its evidence table. `scripts/build_skills.py` checks every JD share in the ontology against this table on each run.

<!-- BEGIN GENERATED: scripts/build_skills.py (posting evidence) -->
**JobsPipe, retrieved 2026-11-02** (Grade B). Platform aggregate of live postings: for each posting title, the skills most often named and their share of postings (per cent). Grade B under decision D-018 (platform data). Recorded on 2026-11-02 in career/03-skills-and-tech/role-skill-maps.md §2.1 and moved to this data file unchanged on 2026-11-07. Sample sizes were not recorded. Expiry: EGP-1.0 class V3 (skill-demand shares): 180 days from retrieval, so re-verify by 2027-05-01. Data: [data/posting_skill_shares.json](../../data/posting_skill_shares.json).

| Posting title | Skills named most often (share of postings, %) | Notes |
|---|---|---|
| **AI Engineer** | Python 78.4 · LLM 76.7 · agentic AI 59.3 · RAG 54.0 · machine learning 39.8 · AI 37.8 · generative AI 37.6 · Azure 35.1 · AWS 35.1 · CI/CD 34.4 · vector DBs 32.6 · prompt engineering 31.1 | Remote 11.0%; pay disclosed 19.6%; senior 24.6%, entry 7.0% |
| **Machine Learning Engineer** | ML 98.6 · Python 71.3 · PyTorch 48.2 · LLM 45.0 · data structures 33.7 · deep learning 32.6 · TensorFlow 31.8 · communication 30.3 · AI 27.0 · A/B testing 23.5 · NLP 23.3 · C++ 23.3 | Remote 14.0%; pay disclosed 38.5%; entry 13.7%, senior 23.2% |
| **Research Scientist (all fields)** | Python 42.3 · communication 41.3 · ML 39.2 · data structures 26.0 · PyTorch 25.4 · AI 25.1 · LLM 24.4 · creativity 23.0 · deep learning 18.6 · C++ 17.4 · reinforcement learning 17.1 | Remote 3.3%; US 65.0% of postings |
| **Solutions Architect** | AWS 53.6 · leadership 43.0 · communication 42.9 · mentoring 35.1 · Azure 29.5 · adaptability 26.5 · compliance 25.3 · Python 23.6 · AI 23.2 · GCP 22.6 · DevOps 17.2 · generative AI 17.1 | Remote 16.2% |
| **Data Scientist** | data science 90.1 · Python 86.0 · ML 69.3 · SQL 63.8 · statistics 52.7 · communication 42.3 · data analysis 33.1 · LLM 30.1 · AI 27.2 · AWS 24.8 · generative AI 22.0 | Feeder for AI Engineer / Evals |
| **Product Manager** | product management 92.6 · communication 53.7 · leadership 40.1 · compliance 26.1 · time management 24.0 · agile 22.7 · roadmapping 18.4 · AI 15.4 · stakeholder management 14.2 · agentic AI 13.6 | Feeder for AI PM |
| **Software Engineer** | Python 44.4 · communication 44.2 · Java 32.4 · CI/CD 31.3 · AWS 30.8 · system design 28.3 · C++ 24.6 · AI 24.0 | — |
| **Backend Engineer** | communication 40.4 · AWS 39.7 · Python 38.4 · system design 37.0 · Kubernetes 31.2 · PostgreSQL 30.7 · Docker 28.0 · CI/CD 26.8 · observability 25.0 | Remote 31.6% |
| **Full-Stack Engineer** | React 69.4 · TypeScript 52.7 · Python 41.8 · AWS 41.3 · CI/CD 37.8 · Node.js 32.3 · REST API 27.6 | Remote 21.6% |
| **DevOps Engineer** | DevOps 99.0 · CI/CD 81.2 · Kubernetes 69.4 · Terraform 59.1 · Python 55.7 · Docker 53.4 · AWS 52.9 · Linux 45.1 | Feeder for ML Platform / AI Infra |
| **Security Engineer** | Python 45.7 · cybersecurity 42.3 · compliance 39.4 · AWS 38.8 · incident response 32.4 · application security 26.5 · IAM 21.6 | Feeder for AI Security |
| **Engineering Manager** | leadership 72.7 · communication 51.4 · mentoring 47.1 · compliance 30.9 · system design 25.3 · observability 18.0 · agentic AI 14.8 | Feeder for AI EM |
<!-- END GENERATED -->

---

## 4. Verification

<!-- BEGIN GENERATED: scripts/build_skills.py (verification) -->
- **Links:** 1529 role links across 26 roles; evidence JD 154 · S09 31 · S 679 · P 665 (computed by scripts/build_skills.py)
- **Date:** 2026-11-04
- **Posting shares:** all 154 JD shares match their title's row in data/posting_skill_shares.json (scripts/build_skills.py checks this on every run); all 31 S09 shares matched to the cited T0-03 §6.3 line
- **Session citations:** all 679 S citations point at an existing session line that names the item; candidate lines were scored for role relevance (role keyword on or near the line, terms from the note, table or bullet rows), weak knowledge-skill citations at Should or Optional were downgraded to P (11), and the remaining low-relevance lines plus a random sample of 40 were read and 40 were replaced with exact lines or downgraded
- **Rules:** every role covers all 19 types or states why a type does not apply; archived, dormant and retired tools and retired credentials are tiered Avoid; every change to a headline tier carries a reason
- **Limits:** the planned independent agent fact-check of every link was blocked by the model quota on 2026-11-04, so citations matched by keyword can still be weaker than a close reading; tool tiers outside the measured titles rest on session mentions and practice curation until job-description mining (30+ dated postings per role) measures them
<!-- END GENERATED -->

---

## 5. How the Ontology Is Designed

The method behind [data/skills_ontology.json](../../data/skills_ontology.json) and the pages generated from it: the [skills vocabulary](skills-vocabulary.md), these inventories, the [résumé skills matrix](../06-job-search/resume-skills-matrix.md), the [skills radar](skills-radar.md) and [credentials by role](../04-certifications/credentials-by-role.md). Evidence grades are EGP-1.0: A/B measured; C small-sample, vendor or practitioner; D judgement; M model output.

### 5.1 Ten requirements: what a résumé needs from the skills layer

A résumé can only be as good as its skills input. The ontology was designed against ten requirements:

| # | Requirement | Why | Evidence | How the ontology meets it |
|---|---|---|---|---|
| R1 | Exact names of tools, frameworks and platforms | Recruiter searches key on titles, languages and frameworks; AI screening extracts canonical skill names | C · [T0-11](../../research/sessions/T0-11-certification-cloud-credential-roi.md); A · [T0-04](../../research/sessions/T0-04-ats-filtering-funnel-conversion-math.md) | Concrete entries across 11 concrete types, unbundled |
| R2 | Concept phrases (RAG, LLM evaluation, agents) | Screening criteria and human readers judge capability | A · T0-04 | Concept and method entries, with sub-concepts linked to their parents |
| R3 | Tool ↔ concept links and groups of alternatives | Turns "used Qdrant" into "vector search"; handles "LangGraph or similar" | D | `implements` links; choose-one classes such as vector stores and tracing products |
| R4 | Aliases and posting wording | "evals" vs "LLM evaluation"; "GenAI" vs "generative AI" | B · JobsPipe terms | `aliases` on every entry; each role file lists keywords to mirror |
| R5 | Priority per role, Must → Optional | Fills a limited skills section | — | Five tiers: Must, Important, Should, Optional, Avoid |
| R6 | Status and freshness of each tool | Don't list archived or dormant tools such as TGI, RAGAS or AutoGen | A/B · [T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) | Dated `status`; archived, dormant and retired items are always tiered Avoid |
| R7 | Non-technical skills, shown rather than listed | Postings measure them, interviews probe them, and a behavioural "No Hire" is a near-veto | B · JobsPipe; B/C · [T1-03](../../research/sessions/T1-03-interview-execution-offer-negotiation.md) | Six non-technical types, present in every role inventory |
| R8 | How to evidence each skill | Unbacked skills are discounted; AI review cites evidence per requirement | A · T0-04; [T0-13](../../research/sessions/T0-13-production-portfolio-proof-of-work-standards.md) | A résumé pattern per type; the V0–V3 verifiability ladder |
| R9 | A proficiency scale | Gap analysis and honest claims | [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) D9 | The 0–3 scale; self-assessment tables in every role file |
| R10 | Credentials and prerequisites kept apart from skills | They are facts, not skills | T0-11; T0-04 | Separate `credentials` entries; prerequisites and proof kept as role facts |

### 5.2 Design rules

- **Types and relations.** Every skill has exactly one of 19 types in three groups (technical knowledge, technical concrete, non-technical), and four kinds of relation: implements, parent (part of), choose-one classes, and aliases (posting wording). A choose-one class link is satisfied by any member, and a link can require *n* members. [Skills vocabulary §0](skills-vocabulary.md#0-how-to-read-this-file) defines each type, where it goes on a résumé and how the relations read.
- **Role links.** Each role link carries a tier (M, I, S, O or X: Must, Important, Should, Optional, Avoid) and one of the four evidence classes in the tag table in §0.
- **Tiers.** Measured shares set tiers by the tier rule in §0. Every change to a headline tier is recorded with its reason (§3).
- **Two layers for résumés.** The *headline* layer holds the concise skills-section phrases in the résumé matrix, including classes such as "AWS / Azure / GCP"; the *full inventory* holds every typed entry. Both are projections of the same links, so they cannot disagree.
- **Rules checked on every build,** beyond the JSON Schema ([scripts/build_skills.py](../../scripts/build_skills.py)):
  - every ID resolves, and `implements` and `parent` point at concepts or methods;
  - every S link cites a real session line, and JD and S09 links carry a share and a source;
  - archived, dormant and retired tools and credentials are tiered Avoid;
  - every role covers all 19 types or says why a type does not apply, and has at least one Must, one communication and one behavioural link.
- **Coverage.** The validator checks that every technology on the skills audit list of 2026-11-04 has a typed entry; that audit also found all 114 JobsPipe skill terms typed. Entry counts by type are in the [vocabulary summary](skills-vocabulary.md#1-summary), and skills per role in the role index (§1).
- **Never cite a session line that does not support the claim;** use P when the corpus is silent.
- **To change something,** edit the data, run the generators that [AGENTS.md §2](../../AGENTS.md#2-sources-of-truth) lists for it, then run the validator. Never edit a generated block or an inventory file.

---

<a id="5-limits-and-next-steps"></a>
## 6. Limits and Next Steps

- **Practice-curated items are hypotheses.** Each [P] tag marks a skill that is standard for the role but unmeasured in the research. Physical AI rests almost entirely on [P].
- **Shares come from adjacent titles for many roles.** JobsPipe measures a dozen titles, and several inventories cite a feeder title (for example Security Engineer for AI Security). The inventories say so where they do.
- **Next: job-description mining.**
  - Sample 30 or more dated postings per role from public ATS boards (Greenhouse, Lever, Ashby) and career pages.
  - Extract skills with model assistance and human checks.
  - Accept an inventory as complete only when at least 95% of the skills those postings name are in it, under a canonical name or an alias.
  - Promote measured tools from [S] or [P] to [JD].
  - Start with the roles whose practice-curated share in the role index (§1) is highest.
- **Maintenance:** re-verify tool statuses every 90 days (next by 2027-01-21), then regenerate.
