---
id: "T0-58"
title: "Role Dossier: ML Platform / MLOps Engineer"
date: "2026-11-13"
status: complete-with-gaps
topic: "role-dossier-ml-platform-engineer"
tags: ["role-dossier", "ml-platform-engineer", "mlops", "job-postings", "india-lens"]
informs_decisions: ["D-002", "D-004", "D-015"]
confidence: "medium"
schema_version: "0.1.0"
temporal_anchor: "2026-11"
last_verified: "2026-11-13"
authored_by_model: "Claude Sonnet 5.5 (Anthropic), claude.ai with web search and fetch. Anthropic is the author's developer: the one Anthropic posting used (S72) is adjacent evidence and is marked COI."
evidence_window: "2025-03-18 to 2026-11-13"
protocol_version: "EGP-1.0"
pipeline: "RP2"
claims_tested: 15
---

# T0-58: Role Dossier: ML Platform / MLOps Engineer

This dossier tests the knowledge base's record for the ML Platform / MLOps Engineer role against dated evidence. Sources are numbered S1 to S92 in the ledger. Grades follow the protocol: A is an employer's own page that I opened; B is platform or aggregator data, or an extract of an employer page; C is third-party analysis; D is recall or judgement; M is my own calculation from the sample; P is practice-curated. The brief's anchor date is 2026-11-11. Every page was retrieved on 2026-11-13, in three research passes on that day, and the 90-day window runs from 2026-08-13.

This file consolidates and supersedes the two earlier drafts of this session. It differs from them in four ways. Two sample postings were dropped after a liveness retest (Walmart R-2465787 returned "not found"; Epidemic Sound's posting redirected to its careers home page). Wellhub's roles are corrected to Brazil-only. The sample grew to 37 postings, with four German-language probe records kept outside the statistics. K5, K7 and K12 have evidence in this version. **Main limit:** only five of the 37 sample postings were read in full on an employer board, and only 12 meet the strict window test, so the sample is a cross-check on platform data, not a measurement.

## Prior

| # | Proposition | Confidence | Grade |
|---|---|---|---|
| P1 | Kubernetes, Terraform, Docker, Python, CI/CD and a public cloud are each named in most postings. | 0.8 | D |
| P2 | US posted base for MLOps and ML platform roles clusters at $150–250K, with staff level above $250K. | 0.7 | D |
| P3 | Titles built on LLM gateways, MCP or agent gateways are under 5% of postings. | 0.8 | D |
| P4 | India postings use "MLOps Engineer" more than "ML Platform Engineer" and rarely post pay. | 0.7 | D |
| P5 | Frontier labs hire this work under "infrastructure" or "inference" titles, not MLOps. | 0.6 | D |
| P6 | Certifications are named in under 10% of postings. | 0.75 | D |

## Research Question

**Decision question:** what must the knowledge base say about the ML Platform / MLOps Engineer role on definition, demand, pay, skills, proof, credentials, interviews, careers and geography, and which of its 15 claims (K1 to K15) should change?

**Sub-questions:** the 15 coverage items in the brief, plus two session probes: how platform teams changed with generative AI (MLOps against LLM operations), and measured volume (graded D in the knowledge base).

**Scope as applied:** postings live or dated from 2026-08-13; other evidence from 2025-01-01. I classified each posting by what it asks for. A posting counts as this role if its work is the platform for the model lifecycle or model serving. Inference-engine optimisation, GPU-fleet reliability, cloud-platform engineering, application AI engineering, field engineering and management roles were treated as adjacent and excluded.

**Method:**
- About 28 web searches and 14 page-fetch attempts across three passes on 2026-11-13. Ten fetches returned content, one was blocked by bot detection (not worked around), and three were refused by the tool because the URL had not appeared in earlier results.
- Posting queries combined title variants with region or employer type: US and AI-cloud, Bengaluru, Europe, Big Tech, enterprises and consultancies, frontier labs, and German-language titles. Extra queries surfaced specific employer-board pages (Wellhub, Together AI).
- Platform pages (Axial, Fast AI Jobs, Levels.fyi, ITJobsWatch) gave demand and pay. Guide pages gave interview evidence. Issuer pages (AWS, CNCF, NVIDIA, Hugging Face) gave credential and tool facts.
- Sample size: 37 core postings (13 US, 3 Brazil, 6 Europe, 13 India, 2 other) plus 4 German-language probe records outside the statistics. Of the 37, 31 carried skill text and were coded.

**What the sampling biases:** the search engine favours large employers and English-language pages; the India query named "Kubeflow MLflow", which inflates those two tools for India; extracts are truncated, so skill shares are lower bounds; no random draw was possible, so the sample is what the searches surfaced.

**Falsification:** I tested the knowledge base's skill shares (K10, K11) and aliases (K2) against the sample and found that several shares and three alias families were not reproduced. I also retested four employer-board URLs on 2026-11-13; two were dead, which removed two sample records.

## Key Findings

| # | Finding | Key evidence | Grade |
|---|---|---|---|
| KF1 | US demand is steady, not surging. Axial counts 1,959 US MLOps postings from January to 2026-07-13, about 70 new a week, with no spike or contraction. ITJobsWatch counts 184 UK permanent jobs citing MLOps in the six months to 2026-02-18, against 156 and 139 in the two prior years (+18% by my arithmetic). | [S5, S7, S65] | B |
| KF2 | Fast AI Jobs' broad "MLOps / Infrastructure Engineer" category lists 1,099 open roles at 423 companies on 2026-11-12, against 630 around mid-June (+74%). The category includes unrelated systems and reliability roles, so it overstates ML platform demand. | [S8, S9] | B |
| KF3 | The US market is individual-contributor heavy: mid 36%, senior 33%, principal 13%, junior 9%, management 8%. Employers with 10,000 or more staff post 34%. Of the 44% of postings stating a work model, 42% are fully remote. California holds 27%. | [S5, S6, S7] | B |
| KF4 | Titles in the 37-posting sample: 21 say MLOps, 3 ML Platform, 5 AI Platform, 3 are Software Engineer on an ML or AI platform team, 3 are Platform Engineer with ML scope, 2 are AI or ML infrastructure. None says LLMOps, MCP or Agent Gateway. German postings use KI Platform Engineer, AI Platform Engineer and Cloud & MLOps Expert. | jd records; [S78–S82] | M/C |
| KF5 | One title covers several variants: Big Tech software engineers on ML platform teams (distributed systems and serving; the Uber staff posting names no Kubernetes or Terraform); AI-cloud platform roles (Kubernetes internals, IaC, Go or Python, GPU scheduling); product-company platform roles (Kubeflow, Feast, Spark-on-Kubernetes, platform-as-a-product); India services and GCC MLOps (MLflow, Kubeflow, Airflow plus cloud ML services). A vendor calls the title at least three jobs in one. | [S1, S2, S28, S67, S75] | A/M/C |
| KF6 | Skill shares (n=31 coded of 37): lifecycle tooling 68%, Kubernetes 61%, cloud 52%, CI/CD or Git 45%, IaC 42%, observability 42%, Python 39%, Docker 29%, MLflow or Kubeflow 52%. LLM gateways, MCP and supply-chain skills are 0%; IAM is 3%. The knowledge base's CI/CD 81%, Docker 53% and DevOps 99% are not reproduced; its Kubernetes 69%, IaC 59%, Python 56% and cloud 53% sit inside the sample's margin of about ±17 points. All sample shares are extract-limited lower bounds. Axial says Python, cloud and MLOps tooling each exceed two-thirds. | skill_signal records; [S5] | M/B |
| KF7 | US pay depends on source type. Sample posted base (n=8): $150K–$357K, median midpoint $245K. Levels.fyi total compensation for "Machine Learning Ops Engineer": median $145,200, p25 $120K, p75 $200K, p90 $295K (as of 2026-10-11). Fast AI Jobs posted-base median: $175K (about June), $170K (July), $179,250 (2026-11-12, n=430). The sources measure different populations and are not reconciled. | [S1, S2, S8, S23, S29, S50, S52, S83] | M/B |
| KF8 | Outside the US: London median advertised salary £75,000 (six months to 2026-10-20); UK outside London £87,500 (six months to 2026-02-18); one Munich recruiter posting shows €80,000–100,000. India sources conflict: all-level averages of ₹8–20 LPA (edtech blogs citing Glassdoor and AmbitionBox) against mid-career ₹20–35L and senior ₹38–65L (as of October 2026). None of 13 India postings discloses pay. | [S61, S62, S63, S65, S66, S81] | B/C |
| KF9 | India GCC demand: Quess reports supply gaps of 18–43% across AI/ML Ops, platform engineering, cybersecurity and GenAI operations (Q3 FY26), 32–36% for platform engineering (Q1 FY27) and 38–42% for AI and data (Q2 FY27). GCC tech hiring fell 3.5% quarter on quarter in July–September 2026. People with 4–12 years' experience were 56% of GCC hiring demand (Q1 FY27). The source is a staffing firm. | [S58, S59, S60] | C |
| KF10 | Interview loops are tooling-and-systems loops: IaC, CI/CD, containerisation, drift monitoring and feature-store design in aggregated reports; at Netflix, coding plus ML-platform system design drawn from team work, with system design weighing most. A take-home appears in 33–46% of aggregated reports. No source describes KV-cache or decode-roofline questions for this role, so the infrastructure track fits only the inference-platform variant. A press report (not a Netflix page) says Netflix allows AI tools in coding rounds. | [S10, S11, S12, S13, S77] | C/D |
| KF11 | Credentials are moving and rarely named. AWS ML Specialty had its last exam date on 2026-03-31. The ML Engineer Associate's MLA-C01 English exam ended 2026-09-28 and MLA-C02 is in beta. CKA costs $445 with one retake. One of 37 postings names a certification (HCLTech, as optional: AWS ML Specialty and Google Professional ML Engineer); none names CKA or MLA. An adjacent South African posting names CKA or CKAD. | [S3, S46, S47, S48, S49, S87] | A/M |
| KF12 | K7's tool-churn facts are confirmed. NVIDIA renamed Triton Inference Server to Dynamo Triton as of 2025-03-18 and calls Dynamo its successor. Hugging Face put TGI in maintenance mode and says it has since been archived (a third party dates the archive to 2026-03-21). One sample posting still names TGI. | [S53, S54, S55, S56, S57, S22] | A/C |
| KF13 | Frontier labs and Big Tech use platform and infrastructure titles. Mistral lists "Platform Engineer, Data Infrastructure & MLOps". Anthropic lists a Staff+ Kubernetes Platform role at $320K–$485K base (adjacent AI infrastructure; COI). NVIDIA lists a Senior MLOps Engineer at $184K–$357K. Netflix, Uber and Pinterest use Software Engineer titles on AI platform teams. A vendor catalogue also lists Mistral inference and ML-infrastructure roles and Anyscale ML platform engineers working on Ray Serve. | [S69, S72, S73, S83, S30, S2, S29] | A/B/C |
| KF14 | Durability: platform teams are widespread (a secondary report of Google's 2025 DORA research: 90% of organisations use an internal platform and 76% have dedicated platform teams), and surveys say most platform teams host or plan AI workloads and use AI daily for code and documents. LLM operations sit inside ML platform postings: Wellhub's platform role defines LLMOps lifecycle requirements, and 32% of coded postings carry LLM-specific content. Entry is thin: junior 9% (Axial), 1 of 37 in the sample. | [S67, S5, S88, S89, S90, S91] | C/M |
| KF15 | Evidence hygiene: 12 of 37 sample postings meet the strict window test and 5 were read in full on an employer board. Two employer URLs retested on 2026-11-13 were dead. SumerSports' job ID changed. Wellhub's roles are open only to candidates in Brazil. No MLOps-titled LCA counts were found; an adjacent family shows 8,275 certified H-1B LCAs. | [S4, S17, S21, S67, S76] | A/B |

## Recommendation

| Decision rule | Failure mode |
|---|---|
| A backend, DevOps or SRE engineer should build one model-serving and lifecycle project (serving, CI/CD, monitoring) on a Kubernetes and IaC base, then apply to ML platform, MLOps and AI platform titles. | Postings differ by variant, so one project may fit only one of them. |
| Pick the variant before tailoring. India services and GCC: MLflow, Kubeflow, Airflow and a cloud ML service. Big Tech: distributed systems and serving. AI cloud: Kubernetes internals, GPU scheduling, Go or Python. Product company: Kubeflow, Feast and platform-as-a-product. | Variant boundaries are inferred from n=37, and the India tool shares are query-biased. |
| Treat certifications as optional. If AWS-centric employers matter, use the AWS ML Engineer Associate on its newer exam (MLA-C02, beta); do not plan around the retired ML Specialty. Take CKA only if your Kubernetes evidence is thin. | One employer segment may screen on certificates, and exam status can change after 2026-11-13. |
| Do not search for LLMOps, MCP or agent-gateway titles. Read for LLM operations inside ML platform and AI platform postings. | Such titles may appear later or at employers not sampled. |
| For frontier labs and Big Tech, search "infrastructure", "Kubernetes platform" and "software engineer, ML platform" titles as well as MLOps. | Those are partly adjacent roles with different loops and pay. |
| Early-career applicants should expect few openings and target adjacent platform, DevOps or data-engineering roles first. | The thin-entry evidence rests on Axial's 9% and one sample posting. |
| Check that a posting is live on the employer's board before investing in it; use aggregator copies only to find it. | Employer boards also keep reposted or stale roles. |
| Use source-specific pay figures: posted base for US startups and Big Tech, Levels.fyi total compensation for offers, and do not expect posted pay in India. | India pay evidence is secondary only. |

**What would change these rules:** a sample of 100 or more postings read in full from employer boards that reproduces the knowledge base's shares; LLMOps, MCP or gateway titles appearing in volume; a shift of more than 30% in Axial's weekly volume; a primary India pay source that matches neither the edtech averages nor the experience bands.

## Alternatives Considered

| Option | Verdict |
|---|---|
| One role page with several variants (Big Tech SWE-on-ML-platform, AI-cloud platform, product-company platform, India MLOps) | Preferred: JDs differ by variant but share a core. Risk: variants are inferred from a small, search-led sample. |
| Split into separate roles per variant | Rejected: too little evidence to justify new scores. |
| Use aggregator shares only, no sample | Rejected: category counts are noisy (KF2) and platform pages do not give title-level skill shares. |
| Add LLMOps, MCP and gateway aliases as first-class titles | Rejected: 0 of 37 titles. Keep as watchlist. |
| Treat DevOps-titled postings as this role | Rejected: only postings with model-lifecycle or serving scope were kept. |
| Rely on Levels.fyi or posted bands alone for US pay | Rejected: they differ by about $80K at the median and measure different things; report both. |

## Detailed Findings

### 1. Definition, variants and aliases

Postings describe building shared infrastructure for model training, deployment and monitoring, and increasingly for LLM serving. Examples: Together AI's container platform for custom-model inference [S1]; Uber's serving platform for thousands of production models [S2]; Wellhub's ML development lifecycle platform on Kubeflow, Feast and Spark-on-Kubernetes, run as a product with LLMOps lifecycle requirements [S67]; HCLTech's MLflow, Kubeflow and TFX pipelines with Terraform and CI [S3].

| Variant | Examples | What the postings stress | Evidence |
|---|---|---|---|
| Big Tech software engineer on an ML or AI platform team | Uber, Netflix, Pinterest, Microsoft AI, NVIDIA | Distributed systems, serving, lifecycle observability; the Uber staff posting names no Kubernetes or Terraform | [S2, S29, S30, S83, S84] |
| AI-cloud and AI-native platform | Together AI, Scale AI, Mistral, Synthesia | Kubernetes internals, IaC, Go or Python, GPU scheduling, serving platforms | [S1, S28, S69, S85, S19] |
| Product-company ML platform | Wellhub, Mollie, dv01, SumerSports | Kubeflow, Feast, Spark-on-Kubernetes, Terraform or Crossplane, CI/CD, platform-as-a-product | [S67, S18, S24, S4] |
| India services and GCC MLOps | HCLTech, Rakuten Symphony, Aptiv, Quantiphi, Fractal, TransUnion, Calix | MLflow, Kubeflow, Airflow, cloud ML services | [S3, S31–S35, S37] |

Excluded as adjacent: inference-stack optimisation (Kimchi/CAST AI, S44), GPU-fleet reliability (Together staff AI infra, S45), cloud-platform engineering (Baseten), Kubernetes platform for compute fleets (Anthropic, S72), field engineering (a Jobgether role), and application AI/ML engineering (a JPMorgan lead role).

| Title family (core sample n=37) | Count |
|---|---|
| MLOps or ML Ops in the title (includes the hybrid "MLOps / ML Platform Engineer") | 21 |
| AI Platform (Uber, Wellhub, Veralto ×2, Vriba) | 5 |
| ML Platform Engineer (Together AI, Mollie, Synthesia) | 3 |
| Software Engineer on an ML or AI platform team (Pinterest, Netflix, Walmart Global Tech India) | 3 |
| Platform Engineer with ML scope (Together AI, Lorien, Mistral) | 3 |
| AI or ML infrastructure or serving (RoundCircle, Scale AI) | 2 |

German-language probe: "KI Platform Engineer" (Techniker Krankenkasse, StepStone, published 2026-08-10, three days before the window [S82]), "Cloud & MLOps Expert" (enercity [S79]) and "Software Engineer – KI, MLOps & Fullstack" (E. Zoller, published 2026-09-17 [S78]). One Munich recruiter treats MLOps, ML Platform, ML DevOps and AI Infrastructure Engineer as interchangeable titles [S81].

### 2. Demand

| Metric | Value | Source | As of | Grade |
|---|---|---|---|---|
| US MLOps postings since 2026-01 | 1,959 | Axial [S5] | 2026-07-13 | B |
| New US MLOps postings per week | about 70, flat | [S5, S7] | H1 2026 | B |
| Open roles in "MLOps / Infrastructure Engineer" (global, startup-led) | 1,099 roles; 423 companies | Fast AI Jobs [S8] | 2026-11-12 | B |
| Same category, earlier snapshot | 630 | [S9] | about 2026-06-16 | B |
| Change in that category | +74% | my arithmetic | 2026-11-12 | M |
| UK permanent IT jobs citing MLOps | 184 (six months to 2026-02-18); 156 and 139 in the two prior years | ITJobsWatch [S65] | 2026-02-18 | B |
| Seniority, US | junior 9, mid 36, senior 33, principal 13, management 8 (%) | Axial [S6, S7] | 2026-07-13 | B |
| Employer size and contract, US | 34% from firms of 10,000 or more; 13% from firms under 50; 13% contract | Axial [S6] | 2026-07-13 | B |
| Remote (of the 44% stating a model) | 42% remote, 38% hybrid, 20% on-site | Axial [S6, S7] | 2026-07-13 | B |
| India: MLOps and model deployment share of AI postings, 2025 | 10%, up 42% | foundit via Masai School [S14] | 2025 | C (COI) |
| India GCC supply gaps | 18–43% (Q3 FY26); platform engineering 32–36% (Q1 FY27); AI and data 38–42% (Q2 FY27) | Quess via news [S58–S60] | 2025-12 to 2026-09 | C |
| India GCC tech hiring | −3.5% quarter on quarter, July–September 2026 | [S60] | 2026-09-30 | C |
| Sample: remote-eligible / India / pay disclosed | 14 of 37 / 13 of 37 / 8 of 37 | jd records | 2026-11-13 | M |

**Trend since 2025.** Axial reports a flat flow of about 70 US postings a week through the first half of 2026. ITJobsWatch shows UK counts rising from 139 to 156 to 184 across three six-month windows. Fast AI Jobs' category rose from 630 to 1,099 between mid-June and 2026-11-12, but its definition is broad and may have changed. I treat demand as flat to rising, with low confidence on direction. Employer mix and seniority are in the tables above and in section 3.

### 3. Job-description sample

The 37 core records and 4 probe records are in the Data Appendix. Job IDs are given where a page shows one.

| Employer type | US | Brazil | Europe | India | Other | Total |
|---|---|---|---|---|---|---|
| AI-native startup | 4 | 0 | 2 | 1 | 0 | 7 |
| Big Tech | 5 | 0 | 0 | 0 | 0 | 5 |
| Frontier lab (Mistral) | 0 | 0 | 1 | 0 | 0 | 1 |
| Enterprise or product company | 3 | 2 | 1 | 4 | 0 | 10 |
| GCC | 0 | 0 | 0 | 3 | 0 | 3 |
| IT services or consultancy | 1 | 1 | 0 | 3 | 1 | 6 |
| Agency or other | 0 | 0 | 2 | 2 | 1 | 5 |
| **Total** | **13** | **3** | **6** | **13** | **2** | **37** |

- **Seniority:** lead or staff and above 7; senior 15; mid 5; junior 1; unstated 9.
- **Years stated** in 6 postings (3 to 8; median of the lower bounds 4.5).
- **Degree stated** in 3 postings (Together AI, Uber, CI&T), all accepting equivalent experience or a related field. Axial reports 63% of US postings require a degree [S5].
- **Posted pay:** disclosed in 8 of 13 US postings and in none of the other 24.
- **ATS known** for 11: Greenhouse, Rippling, Ashby, Lever, SAP SuccessFactors and Uber's own site.
- **Window:** 12 of 37 meet the strict test (live when opened, or dated or valid within it). Five were read in full on an employer board (Together AI, Uber, HCLTech, Wellhub AI Platform, CI&T). The other 25 are undated or unverified.
- **Liveness retests that removed records:** Walmart R-2465787 returned "not found" and Epidemic Sound's posting redirected to its careers home page on 2026-11-13 [S17, S21].
- **Exclusions (seen and not sampled, not exhaustive):** 13 not this role (Kimchi/CAST AI, three Together AI roles, Baseten, two Jobgether roles, JPMorgan, Uber senior ML engineer, Netflix and Pinterest managers, Anthropic Kubernetes platform, an ML-engineer role in South Africa); 16 outside the window or closed (Avride 2026-04-02, Airkit 2026-01-25, C the Signs 2026-03-04, Neko Health 2026-06-18, TalonOne 2026-03-07, CuspAI 2025-11-07, EY GDS 2025-10-09, Deloitte 2025-10-24, Pierce 2025-09-10, a closed Greenhouse Software role, an older Synthesia copy 2026-06-26, two NVIDIA roles, Ki Group 2026-06-19, Forschungszentrum Jülich, Techniker Krankenkasse 2026-08-10); 3 with too little detail (DoorDash, Xcede, Pinterest principal); 2 failed liveness retests.

### 4. Skills (n=31 coded of 37)

Skills are coded only where the text I saw names them, so shares are lower bounds. Observability counts named tools or telemetry practices (Prometheus, Grafana, Datadog, ELK, CloudWatch, SLOs, monitoring and logging); "monitoring" appearing only as a pipeline stage is not counted. Cloud counts a named provider or a provider-managed ML service. The six uncoded postings are Pinterest, Netflix, Wellhub MLOps, NVIDIA, Microsoft and Scale AI.

| Skill | Share | Count | Suggested tier | KB tier | Reason |
|---|---|---|---|---|---|
| mlops_lifecycle | 67.7% | 21 | Must | Important | Named lifecycle tooling (MLflow, Kubeflow, registry, tracking, feature store) or explicit lifecycle wording. |
| kubernetes | 61.3% | 19 | Must | Must | Inside the margin of K10's 69.4%. |
| cloud (AWS, Azure, GCP) | 51.6% | 16 | Must | Must | Axial: over two-thirds. |
| git_ci | 45.2% | 14 | Must | Must | K10's 81.2% not reproduced. |
| iac | 41.9% | 13 | Must | Must | Inside the margin of K10's 59.1%; "terraform" and "iac" are duplicate IDs. |
| observability | 41.9% | 13 | Must | Must | Axial: close behind the leading group. |
| python | 38.7% | 12 | Must | Must | Extracts often omit languages; Axial: over two-thirds. |
| new:mlflow | 45.2% | 14 | Important | absent | India-led; the India query named the tool. |
| new:kubeflow | 41.9% | 13 | Important | absent | MLflow or Kubeflow union 16 of 31 (51.6%). |
| docker | 29.0% | 9 | Important | Must | Often implicit in Kubernetes. |
| aws | 32.3% | 10 | Should | Important | Cloud is split across providers. |
| new:llm-ops | 32.3% | 10 | Should | absent | LLMOps, RAG, vector DB, RLHF, LLM-provider integration or LLM serving (for example vLLM) named. |
| linux | 16.1% | 5 | Should | Important | |
| new:airflow | 16.1% | 5 | Should | absent | |
| new:gpu-scheduling | 16.1% | 5 | Should | absent | Important for the AI-cloud variant. |
| new:feature-store | 16.1% | 5 | Optional | absent | |
| sre | 12.9% | 4 | Should | Important | On-call or SLO language. |
| serving_engines | 9.7% | 3 | Should | Important | Name vLLM, SGLang and Dynamo Triton; TGI is in maintenance mode [S53, S56]. |
| new:go | 9.7% | 3 | Optional | absent | |
| devops | 9.7% | 3 | Should | Important | K10's 99.0% is not reproducible. |
| kserve_ray | 6.5% | 2 | Should | Important | KServe only. |
| iam | 3.2% | 1 | Optional | Important | |
| llm_gateways | 0% | 0 | Optional | Important | MCP and agent protocols also 0 of 37. |
| supply_chain | 0% | 0 | Optional | Important | |

**Regional split.** Among coded postings, MLflow or Kubeflow is named in 11 of 13 India postings and 5 of 18 others. Treat the India figure as an upper bound because the India query named both tools. Non-technical skills (c1 to c4) were not coded.

### 5. Pay

| Population | Statistic | Value | n | Source | Grade |
|---|---|---|---|---|---|
| US posted base, all levels (sample) | range | $150K–$357K | 8 | [S1, S2, S23, S24, S27, S28, S29, S83] | M |
| US posted midpoints (sample) | median / mean | $245K / $229K | 8 | same | M |
| Staff (Uber, Sequen, Pinterest) | range | $170K–$351K | 3 | same | M |
| Senior (Together AI, dv01, NVIDIA) | range | $160K–$357K | 3 | same | M |
| Mid (Egen, Together AI Model Shaping, 3+ years) | range | $150K–$290K | 2 | same | M |
| Fast AI Jobs category, posted base | median | $179,250 (range $51,360–$999,999) | 430 | [S8] | B |
| Same, earlier | median | $175,000 (about June, n=212); $170,000 (July, n=289) | | [S9, S52] | B |
| Levels.fyi "Machine Learning Ops Engineer", US, total compensation | median; p25 / p75 / p90 | $145,200; $120K / $200K / $295K | not shown | [S50] | B |
| Levels.fyi Apple, total compensation | median | $439,250 (page also shows a $464K ICT4 package) | | [S51] | B |
| LinkedIn MLOps postings, US, base | range | $120K–$326K | not stated | [S12] | C |
| Anthropic Staff+ Kubernetes Platform (adjacent), base | range | $320K–$485K | 1 | [S72] | B (COI) |
| Pinterest principal AI platform, base | range | $243K–$500K | 1 | [S43] | C |
| Pinterest senior engineering manager, base | range | $208,592–$429,454 | 1 | [S42] | C |
| London, advertised | median | £75,000 | | [S66] | B |
| UK outside London, advertised | median; UK p75 / p90 | £87,500; £95,000 / £127,000 | | [S65] | B |
| Munich recruiter posting | range | €80,000–100,000 | 1 | [S81] | C |
| India, all levels | average bands | ₹8–20 LPA (blogs citing Glassdoor and AmbitionBox); ₹12–16 LPA | | [S62, S63] | C (COI) |
| India by experience | bands | entry ₹8–15L; mid ₹20–35L; senior ₹38–65L | | [S61] | C |
| India postings | disclosed pay | none | 0 of 13 | sample | M |

**Reconciliation.** The sample's median midpoint ($245K) sits above Levels.fyi's median total compensation ($145,200), which is unexpected because total compensation includes equity. The likely reasons are that the sample over-represents US startups, Big Tech and senior roles, and that Levels.fyi pools all levels and employers; I could not test this. Posted bands are not realised pay. For India, K6's P50 of ₹23.6L fits the mid-career band but not the all-level averages; the populations differ and none of the sources states a method. "In line with AI Engineer" in K4 is untested because I retrieved no AI Engineer comparator.

### 6. Interview loop

| Source or employer type | Rounds and what is assessed | AI-tool policy | Grade |
|---|---|---|---|
| Aggregated MLOps reports (Dataford, 2026-09-04) [S10] | Technical interviews in 77% of reports, take-home 46%, behavioural 38%, final onsite 8%. Topics: IaC, experiment tracking, model versioning, containerisation, CI/CD for AI models, drift-monitoring design. | not found | C |
| Aggregated ML Platform reports (Dataford) [S11] | Recruiter screen 56%, technical 56%, take-home 33%. Prompts: real-time feature store, pipeline bottleneck. | not found | C |
| LinkedIn AI Platform (DataInterview) [S12] | No platform-specific report; general loop: coding screen, two coding rounds, system design, manager round, project deep dive. | not found | C |
| Netflix AI Platform teams (DataInterview, reviewed October 2026) [S77] | Software engineer levels 4 to 6 on teams such as Training Platform, Model Serving Systems, Data and Feature Infrastructure and Agent Platform. Reported onsite: coding and system design drawn from team work, with design weighing most (for example an ML job scheduler, a platform portal, feature serving by freshness). Netflix publishes no process. | A July 2026 press report says AI tools are allowed in coding rounds; it cites no Netflix source | C/D |
| Employer-side framework (HireInSouth) [S13] | Technical screen, take-home deployment with monitoring, MLOps platform design. | n/a | C |

**Fit of K9.** The infrastructure track fits inference-platform postings (Together AI, Scale AI serving). Reported ML platform and MLOps prompts concern schedulers, portals, feature serving, CI/CD and drift monitoring. I found no report of KV-cache maths or decode-roofline questions for this role. Another session owns employer-wide loop formats.

### 7. Proof of work

No first-party hiring-manager source was found. Employer text asks candidates to discuss how what they built has failed and treats open-source maintenance as a plus (Together AI [S1, S28]). Recruiter and vendor sources agree on three signals: deployed systems, open-source contributions to MLOps tooling (MLflow, Kubeflow, Feast, Ray) and write-ups of production incidents, with Axial saying artifacts outweigh badges [S74, S75] (C). The specific project in K14 appears in no source. AWS lists a hands-on "MLOps Demonstrated" micro-credential that I did not open. Strongest public examples were not collected.

### 8. Credentials

| Credential | State as of 2026-11-13 | Key facts | Sample signal | Source |
|---|---|---|---|---|
| CKA | active | $445 including one retake; online proctored, performance-based. Two-year validity and a two-hour exam come from third-party guides. | 0 of 37 | [S48, S49] |
| AWS ML Engineer Associate, MLA-C01 | retiring | $150; 130 minutes; 65 questions; 3-year validity. English exam ended 2026-09-28; other languages continue until MLA-C02 is generally available. | 0 of 37 | [S46] |
| AWS ML Engineer Associate, MLA-C02 | beta | $75 beta fee; 170 minutes; 85 questions; beta delivery from 2026-09-29; general availability date not stated. Lists MLOps and LLMOps engineers among candidate roles. | 0 of 37 | [S46] |
| AWS ML Specialty, MLS-C01 | retired | Last exam date 2026-03-31; holders keep it for 3 years from the date earned. | 1 of 37 (HCLTech, optional) | [S47, S3] |
| Google Professional ML Engineer | not researched | Named by HCLTech as optional. | 1 of 37 | [S3] |

The AWS page lists the MLA-C02 code as "ME1-C02", an inconsistency to check before recording the code. Employers' statements on credentials: HCLTech lists optional certificates (one that can no longer be earned); an adjacent South African ML-engineer posting prefers CKA or CKAD [S87]. Axial says no credential unlocks this market [S74].

### 9. Entry routes and prerequisites

| Background | Evidence | Access |
|---|---|---|
| Backend engineer | Uber and Together AI ask for distributed-systems and backend depth [S1, S2] | Strongest (A/M) |
| DevOps or SRE | Lorien asks for a senior platform or DevOps background; Pragmatike names MLOps, platform engineering and SRE [S20, S22] | Strong (C/M) |
| Data scientist | India postings pair ML tooling with DevOps; no posting names data scientist as a feeder | Possible with Kubernetes and IaC (D) |
| Front-end, non-technical, product management | No evidence in any posting | No evidence |
| PhD | No sample posting asks for a PhD | No evidence |
| New graduate | One junior posting (Mollie, level I); Axial junior share 9% | Thin (B/M) |

Typical prior roles of people hired, from published analyses, were not found. Degree and experience shares are in section 3.

### 10. Progression, durability and leverage

- **Ladders and exits.** Senior to staff to principal: Uber's staff role needs 8 or more years; Pinterest's principal band is $243K–$500K (C). Axial puts principal individual contributors at 13% and management at 8%. Netflix posts levels 4 to 6 on AI platform teams [S77]. Management exit: a Pinterest senior engineering manager band of $208,592–$429,454 (C). Lateral exits: inference and AI-infrastructure roles at frontier labs and AI clouds [S45, S72].
- **MLOps against LLM operations.** No sample title says LLMOps. LLM-specific content appears in 10 of 31 coded postings (32%). Wellhub's platform role defines LLMOps lifecycle requirements; Vriba's role integrates LLM providers; Lorien's platform adds LLM inference to Kubeflow and KServe [S67, S70, S20]. The pattern is extension of the MLOps stack, not replacement (A/M).
- **Durability signals.** A secondary report of Google's 2025 DORA research says 90% of organisations use an internal platform and 76% have dedicated platform teams [S88]. Sponsor-run surveys say most platform teams host or plan AI workloads and use AI daily for code and documents, and that teams expect agents to take on more infrastructure work [S89, S90, S91] (C, COI). Together AI asks for judgement on when to use LLMs for code [S1]. My reading (D): demand persists, routine IaC and CI authoring is the part most exposed to AI tools, and GPU scheduling, serving reliability, cost and governance are less exposed. Tool churn is real and confirmed (KF12).
- **Leverage.** Evidence is scope and pay, not revenue attribution: Uber's staff role owns architecture for thousands of models [S2]; Wellhub frames the role as a product serving embedded data-science teams [S67]; frontier-lab infrastructure bands run higher than the sample's staff band [S72]. Grade C/D.

### 11. Work footprint and specialisations

The footprint is mainly layer L3 (inference and ML platforms). GPU, CUDA, Slurm or HPC work (layer L1) appears in 5 of 31 coded postings. No posting names orchestration or agent protocols (L5). Netflix's Agent Platform team appears only in a guide [S77].

| Specialisation in the role card | Sample share (n=37) | Postings |
|---|---|---|
| Vector search infrastructure | 2.7% | 1 (Veralto, senior) |
| Gateways and model routing | 2.7% | 1 (Pragmatike, request-routing layers) |
| MCP and agent protocols | 0% | 0 |

### 12. Geography and sponsorship

- **US:** Axial shows California 27%, Texas and New York about 9% each, and San Francisco 9.3% of postings excluding remote-only [S5, S7]. Sample cities include San Francisco, Sunnyvale, Santa Clara and Mountain View.
- **Brazil:** three sample roles (Wellhub ×2, CI&T) are remote but open only to candidates in Brazil [S67, S68, S71].
- **Europe:** Amsterdam and Lisbon, London (two roles), remote Europe, a Polish board listing and one unstated; London median advertised salary £75,000 [S66].
- **India:** Bengaluru 12 of 13, Hyderabad 1.
- **Remote:** 14 of 37 are remote-eligible, of which 3 are Brazil-only.
- **Sponsorship:** none of the five postings read in full states visa sponsorship; Wellhub's form asks about sponsorship but the role is Brazil-only. I found no LCA counts for MLOps-titled filings. An aggregator built on Department of Labor files reports 8,275 certified H-1B LCAs for the AI/ML engineer title family across FY2025 and FY2026 through Q3, with median wages of $165,350 and $169,000 and 3,853 in California [S76] (B, adjacent family). An LCA shows what an employer filed, not what people are paid. Official files were not opened.

### 13. Résumé and profile signals

| Skill | Evidence-line pattern (fill with your own facts) | Grade |
|---|---|---|
| Kubernetes | Operated [n] clusters or namespaces serving [n] models, with [metric] improved | P |
| Model lifecycle | Built a registry and promotion path in [MLflow or Kubeflow], cutting time to deploy from [x] to [y] | P |
| IaC | Codified [platform component] in [Terraform or Crossplane] across [n] environments | P |
| Observability | Added [Prometheus, Grafana or Datadog] instrumentation and SLOs for latency or data freshness | P |
| Cloud | Ran inference on [AWS, GCP or Azure] with cost per [unit] tracked | P |

Postings suggest reviewers look for platform-as-a-product thinking (Wellhub), reliability and on-call experience (Together AI, Pragmatike), open-source work and honest discussion of failures (Together AI). Red flags: generic DevOps bullets with no model scope, tool lists with no scale or outcome, and certificates that can no longer be earned (the AWS ML Specialty). Headline patterns that match postings: "ML Platform / MLOps Engineer – Kubernetes, IaC, model serving, MLflow or Kubeflow" (P).

### 14. Misconceptions and risks

| Myth or risk | Evidence |
|---|---|
| MLOps is DevOps with notebooks | Postings ask for model-lifecycle or serving scope; Lorien says the focus is not simply running Kubernetes clusters [S20]. |
| The role needs a PhD or ML research | No sample posting asks for one; the three that state a degree accept equivalent experience or a related field. |
| LLMOps and gateway roles are a separate market | 0 of 37 titles; LLMOps appears inside platform roles. |
| Certificates open doors | 1 of 37 names one, and it is retired; Axial says none unlocks the market. |
| Title inflation and hidden scope | "Senior Advisor", "Specialist" and "Lead" titles in India; contract and agency listings (Egen, Lorien); Big Tech uses "Software Engineer" for platform work. |
| Stale and reposted postings | Two of four employer URLs retested were dead; SumerSports' job ID changed; Mistral's role was reposted twice. |
| "Remote" can mean one country | Wellhub and CI&T roles are Brazil-only. |
| Stale requirement text | HCLTech names a certification AWS has retired. |

### 15. India

- **Volume and mix.** 13 of 37 sample postings. Employers: IT services (HCLTech, Quantiphi, Fractal), GCCs (Rakuten Symphony, Aptiv, Walmart Global Tech India), enterprises (TransUnion, Veralto ×2, Calix), a startup (Autonomize) and agencies (RoundCircle, Vriba). The remote Canibuild listing is counted under "other", not India.
- **Aliases.** 8 of 13 are MLOps-titled; the others are AI/ML Platform (Veralto ×2, Vriba), AI/ML Infrastructure (RoundCircle) and Software Engineer on an ML platform team (Walmart Global Tech India).
- **Tools.** MLflow or Kubeflow in 11 of 13 (upper bound). The GCC postings list Kubernetes, Kubeflow, MLflow and Airflow [S31, S32]; HCLTech's posting names MLflow, Kubeflow, TFX, Terraform and CI but no Kubernetes [S3].
- **Seniority.** Lead or staff 4, senior 7, mid 1, unstated 1. Quess reports 4 to 12 years of experience as 56% of GCC hiring demand [S59].
- **Demand signals.** Supply gaps of 32–42% in the two most recent Quess reports alongside a 3.5% fall in GCC tech hiring [S59, S60]; a staffing firm's interest may colour the gap framing.
- **Pay.** No posting discloses pay; secondary sources conflict (section 5).
- **Interviews.** No India-specific loop evidence was found.

## Repository Deltas

| K# | Claim (short) | Verdict | Evidence [S#] | Grade |
|---|---|---|---|---|
| K1 | Definition: lifecycle, LLM serving, Kubernetes serving, gateways, MCP, CI/CD for models and prompts, cost attribution | updated | Lifecycle, serving, CI/CD and observability supported [S1, S2, S3, S67]; gateways, MCP and prompt CI/CD appear in 0 of 37; platform-as-a-product and LLMOps lifecycle requirements added [S67]. Volume is measured at grade B, so evidence status could move from V towards E | M/A |
| K2 | Nine title aliases | updated | Four of nine seen as families; LLMOps, MCP Control Plane, Agent Gateway and Enterprise AI Control Plane titles 0 of 37. Add "Software Engineer, ML/AI Platform" (Uber, Netflix, Pinterest) and German "KI Platform Engineer" [S2, S29, S30, S82] | M/C |
| K3 | No count (D); Quess gap 18–43% | updated | Measured: US 1,959; category 1,099; UK 184. Quess range traced to Q3 FY26, later gaps 32–36% and 38–42% [S5, S8, S58–S60, S65] | B/C |
| K4 | Posted base $186–277K (n=10), in line with AI Engineer | updated | Sample $150K–$357K, median midpoint $245K (n=8); Levels.fyi total compensation median $145,200; Fast AI Jobs median $179,250; AI Engineer comparison not tested [S8, S50] | M/B |
| K5 | India GCC title; supply gap 18–43% | updated | Gap traced to Quess Q3 FY26; later reports 32–36% and 38–42% with GCC hiring down 3.5%; MLOps-titled GCC postings (Rakuten Symphony, Aptiv); Taggd source not opened [S31, S32, S58–S60] | C |
| K6 | Bengaluru P50 ₹23.6L, P75 ₹41.1L, P90 ₹63.5L | unverifiable | Secondary sources conflict by population (all-level ₹8–20 LPA against mid-career ₹20–35L); no primary source; 0 of 13 India postings disclose pay [S61–S63] | C |
| K7 | Platform need persists; LLMOps absorbed; TGI archived; Triton renamed | confirmed | NVIDIA rename as of 2025-03-18; Hugging Face TGI maintenance mode and archive; LLMOps inside platform roles; steady posting flow [S53–S57, S67, S5] | A/M |
| K8 | Footprint L3, L5, L1 | updated | L3 primary; L1 in 5 of 31 coded postings; L5 unseen in postings [jd records] | M |
| K9 | Infrastructure track (KV-cache, roofline) | updated | Fits the inference-platform subset only; MLOps and ML-platform loops centre on IaC, CI/CD, monitoring and platform design [S10–S13, S77] | C |
| K10 | Must skills with shares | updated | Membership supported; shares recomputed at n=31; add MLflow and Kubeflow as Important; lifecycle tooling suggested as Must; Docker suggested as Important | M/B |
| K11 | Important skills | updated | devops 9.7%, serving_engines 9.7%, sre 12.9%, iam 3.2%, llm_gateways 0%, supply_chain 0%; duplicate IDs flagged | M |
| K12 | CKA and MLA-C01 optional | updated | MLS-C01 retired 2026-03-31; MLA-C01 English ended 2026-09-28 and MLA-C02 in beta; CKA $445; 1 of 37 postings names a certificate [S3, S46–S49] | A/M |
| K13 | Backend, DevOps or SRE prerequisites; India GCC MLOps title | confirmed | Postings name backend and DevOps or SRE feeders; MLOps-titled GCC postings [S2, S20, S22, S31, S32] | C/M |
| K14 | Self-hosted vLLM/SGLang cluster as proof | unverifiable | Only generic proof signals found; the specific project appears in no source [S74, S75, S1] | C |
| K15 | Leave out generic DevOps bullets | confirmed | Lorien requires ML scope; HCLTech and CI&T list ML tooling [S20, S3, S71] | C/P |

## Absences

| Item | Where I looked |
|---|---|
| MLOps-titled US LCA filings | careery.pro, visa-bulletin.us and h1bvisajobs aggregator pages: only AI/ML engineer, ML engineer, DevOps and data-engineer families. Official DOL files not opened. |
| Primary India pay source | AmbitionBox pages that surfaced were for other titles; edtech and content pages only, none with a disclosed method. |
| Levels.fyi figures for India or Europe | Not surfaced by the searches. |
| First-party hiring-manager statements on proof of work | One search; only recruiter and vendor blogs. |
| Typical prior roles of people hired, from published analyses | Not found. |
| Strongest public proof-of-work examples | Not collected. |
| Taggd GCC claim | Not opened; the Quess figures were traced through news coverage. |
| AWS MLOps Demonstrated and Google Professional ML Engineer details | Named on other pages; not opened. |
| India-specific interview differences | No India-specific loop evidence found. |
| AI-tool policies in this role's loops | Only a press report on Netflix (D). |
| Frontier-lab postings titled MLOps or ML platform | One combined search plus platform pages: Mistral (data-infrastructure and MLOps) found; Anthropic's role is adjacent infrastructure. |
| Full-text reads on employer boards | 32 of 37 sample records not read in full: Wellhub MLOps blocked by bot detection (not worked around); AbsenceSoft and Together AI Model Shaping refused by the fetch tool; others not attempted. |
| Non-English postings beyond German; non-technical skills (c1 to c4) | Not searched or not coded. |
| JobsPipe MLOps-specific count | Surfaced ML Engineer and DevOps pages only [S16]. |

## Open Questions & Risks

The strongest objections an expert would raise, with the evidence for and against each:

| Objection | Evidence for | Evidence against |
|---|---|---|
| The sample is search-led, extract-limited and query-biased, so shares are unreliable. | MLflow and Kubeflow are concentrated in India postings returned by a query that named them; CI/CD and Docker shares are far below K10's; only 5 of 37 read in full. | Axial's platform data agree on direction for Python, cloud and MLOps tooling. |
| The Fast AI Jobs category is too broad to measure demand. | It includes systems and reliability roles. | Axial's narrower US count shows a steady flow, and ITJobsWatch counts rise. |
| Axial is a recruiter-run vendor with an undisclosed classifier. | It is the only source for US counts and shares. | UK counts from a separate source move in the same direction. |
| Posted ranges are not pay, and Levels.fyi disagrees with them. | Median $245K (sample) against $145,200 (Levels.fyi). | Fast AI Jobs' $179,250 median sits between them. |
| Title noise: Big Tech "Software Engineer" roles may be backend roles, and Mistral's and Anthropic's roles are infrastructure. | The Uber staff posting names no ML tooling. | Uber's role owns the model-serving platform; Mistral's title contains MLOps. |
| Liveness: most sample records lack a verified window. | Two of four retested employer URLs were dead; a job ID was replaced. | 12 meet the strict test; the dead records were removed. |
| India evidence is secondary and conflicting, and Quess is a staffing firm. | No primary pay source; COI on edtech and staffing sources. | Independent-looking bands bracket K6's P50 at the mid-career band. |
| Durability evidence comes from sponsor-run surveys. | Vultr, Perforce and Pulumi sell platform tooling. | A secondary report of DORA 2025 also shows widespread platform teams. |

**Open questions:** a 100-posting sample read in full from employer boards; a primary India pay source; a frontier-lab sample; MLOps-titled LCA counts from official files; first-party hiring-manager statements; whether MLA-C02 reaches general availability and AWS corrects its exam code.

## Discovered Concerns

| Concern |
|---|
| K10 and K11 give identical shares to "terraform" and "iac" (59.1%) and to "aws" and "cloud" (52.9%), which looks like double counting. A 99.0% "devops" share cannot be a role-level posting share. |
| Content-farm pages: atr-blog.pages.dev cites Levels.fyi and LinkedIn Talent Insights without method and was graded E and excluded; corpready.in derives pay bands from an occupation classification (D, excluded). |
| The AWS certification page shows MLA-C02's exam code as "ME1-C02". |
| Levels.fyi's "10/11/2026" is ambiguous; I read it as 2026-10-11 because the same site shows "6/15/2026" for another page. |
| Aggregator copies lag employer boards: Walmart's posting was gone and Epidemic Sound's had moved, while copies persisted. Job IDs can change on relisting (SumerSports). |
| Wikipedia reports an NVIDIA agreement to acquire Hugging Face (2026-09-03). I did not verify it and did not use it; it matters to Hugging Face as an employer and to the inference-engine landscape. |
| The brief's anchor date (2026-11-11) differs from the retrieval date (2026-11-13). |

## Delta

| # | Prior | Status | Evidence | Impact |
|---|---|---|---|---|
| P1 | Six core skills each named in most postings | Updated | Only lifecycle tooling (68%) and Kubernetes (61%) are majorities; cloud 52%, CI/CD 45%, IaC 42%, Python 39%, Docker 29% (extract-limited) | Tier shares need a larger sample |
| P2 | $150–250K, staff above $250K | Updated | Sample $150K–$357K, staff $170K–$351K, median midpoint $245K; Levels.fyi total compensation median $145,200 | Widen the pay range and cite both source types |
| P3 | Gateway and MCP titles under 5% | Confirmed | 0 of 37 | Keep as watchlist |
| P4 | India uses MLOps titles and rarely posts pay | Confirmed | 8 of 13 India postings MLOps-titled; 0 of 13 disclose pay (India query was tool-biased) | India lens holds |
| P5 | Frontier labs use infrastructure titles | Confirmed | Mistral "Data Infrastructure & MLOps"; Anthropic Kubernetes platform; Big Tech software-engineer titles | Needs a larger frontier-lab sample |
| P6 | Certificates under 10% of postings | Confirmed | 1 of 37 (2.7%) | Keep certificates Optional |

## Sources & Evidence Ledger

| # | Source (title, publisher, URL) | Published | Retrieved | Grade | Access | Modifiers | Used for |
|---|---|---|---|---|---|---|---|
| S1 | Together AI, Machine Learning, Platform Engineer, job-boards.greenhouse.io/togetherai/jobs/4835988007 | n/s | 2026-11-13 | A | Read | | jd, pay, proof |
| S2 | Uber, Staff Software Engineer - AI Platform (Michelangelo), uber.com/global/hu/careers/list/155038/ | n/s | 2026-11-13 | A | Read | | jd, pay |
| S3 | HCLTech, Senior MLOps Technical Lead, careers.hcltech.com/job/Senior-MLOps-Technical-Lead/1356949955/ | n/s | 2026-11-13 | A | Read | | jd, certificates |
| S4 | SumerSports on Rippling, ats.rippling.com/sumersports/jobs (MLOps / ML Platform Engineer listing) | n/s | 2026-11-13 | A | Read | job ID changed | jd, ID churn |
| S5 | Axial, The State of the MLOps Job Market in 2026, axialsearch.com/insights/mlops-jobs | 2026-07-13 | 2026-11-13 | B | Extract | single-source; classifier undisclosed | demand, skills, degree |
| S6 | Axial, Who's Hiring MLOps Engineers in 2026, axialsearch.com/insights/mlops-hiring | 2026-07 | 2026-11-13 | B | Extract | | seniority, size, remote |
| S7 | Axial, The MLOps Hiring Market in 2026: Demand and Top Employers, axialsearch.com/insights/mlops-job-demand | 2026-07 | 2026-11-13 | B | Extract | | trend, geography |
| S8 | Fast AI Jobs, MLOps / Infrastructure Engineer role page, fastaijobs.com/roles/mlops-infra-engineer | 2026-11-12 | 2026-11-13 | B | Read | | counts, pay, Wellhub dates |
| S9 | Fast AI Jobs, same URL, earlier snapshot | about 2026-06-16 | 2026-11-13 | B | Extract | | earlier count and median |
| S10 | Dataford, MLOps Engineer interview guide, dataford.io/roles/mlops-engineer | 2026-09-04 | 2026-11-13 | C | Extract | method undisclosed | loop |
| S11 | Dataford, ML Platform Engineer interview guide, dataford.io/roles/ml-platform-engineer | 2026-09-04 | 2026-11-13 | C | Extract | method undisclosed | loop |
| S12 | DataInterview, LinkedIn MLOps engineer interview, datainterview.com/blog/linkedin-mlops-engineer-interview | 2026-10 | 2026-11-13 | C | Extract | | loop, pay |
| S13 | HireInSouth, How to hire MLOps engineers remotely, hireinsouth.com/post/how-to-hire-mlops-engineers-remotely | n/s | 2026-11-13 | C | Extract | COI (hiring vendor) | loop |
| S14 | Masai School, MLOps skills Indian employers ask for, masaischool.com/blog/mlops-skills-model-deployment-roles/ | 2026 | 2026-11-13 | C | Extract | COI (edtech); cites foundit, original not opened | India demand |
| S15 | Masai School, ML engineer demand in India, masaischool.com/blog/machine-learning-engineer-demand-in-india/ | 2026 | 2026-11-13 | C | Extract | COI (edtech) | context only |
| S16 | JobsPipe, ML Engineer jobs US, jobspipe.dev/jobs/machine-learning-engineer/usa | n/s | 2026-11-13 | B | Extract | | absence note |
| S17 | Walmart, (USA) Senior Software Engineer, careers.walmart.com/us/en/jobs/R-2465787 | n/s | 2026-11-13 | A | Read (page not live: job not found) | | liveness retest; record removed |
| S18 | Mollie, Machine Learning Platform Engineer I, magnet.me/en/opportunity/1095672/machine-learning-platform-engineer-i | 2026-10-15 | 2026-11-13 | B | Extract | aggregator copy | jd |
| S19 | Synthesia, ML Platform Engineer, jobs.accel.com/companies/synthesia/jobs/87795276-ml-platform-engineer (tags from aijobs.net/job/ml-platform-engineer-europe-200044) | 2026-07-28 | 2026-11-13 | B | Extract | aggregator copies | jd |
| S20 | Lorien, Senior Platform Engineer, lorien.sites.sourceflow.co.uk/jobs/151333-Senior-Platform-Engineer- | 2026-09-08 | 2026-11-13 | C | Extract | agency listing | jd |
| S21 | Epidemic Sound, MLOps Engineer, careers.epidemicsound.com/jobs/6543122-mlops-engineer | n/s | 2026-11-13 | A | Read (redirected to careers home page) | | liveness retest; record removed |
| S22 | Pragmatike, ML Ops Engineer, bulldogjob.com/companies/jobs/239784-ml-ops-engineer-pragmatike | n/s | 2026-11-13 | C | Extract | | jd, TGI still named |
| S23 | Sequen, Staff MLOps Engineer, employbl.com/jobs/staff-mlops-engineer-sequen-1649453 | 2026-08-21 | 2026-11-13 | B | Extract | | jd, pay |
| S24 | dv01, MLOps Engineer, builtinaustin.com/job/mlops-engineer/9857042 | n/s | 2026-11-13 | B | Extract | | jd, pay |
| S25 | TinyFish, MLOps Engineer, builtinchicago.org/job/mlops-engineer/9913437 | n/s | 2026-11-13 | B | Extract | | jd |
| S26 | AbsenceSoft, ML Ops Engineer, ats.rippling.com/absencesoft/jobs/47f6d8bf-9a68-4738-81dc-26a5954825f5 | n/s | 2026-11-13 | B | Extract (fetch refused by tool) | | jd |
| S27 | Egen, MLOps Engineer, builtinboston.com/job/mlops-engineer/8002413 | n/s | 2026-11-13 | B | Extract | | jd, pay |
| S28 | Together AI, Platform Engineer, Model Shaping, job-boards.greenhouse.io/togetherai/jobs/4790243007 | n/s | 2026-11-13 | B | Extract (fetch refused by tool) | | jd, pay |
| S29 | Pinterest, Staff Software Engineer, ML Platform, jobr.pro/job/29273979/staff-software-engineer-ml-platform | n/s | 2026-11-13 | C | Extract | aggregator copy | jd, pay |
| S30 | Netflix, Software Engineer L4/L5 Model Serving Systems, workingnomads.com/jobs/software-engineer-l4l5-model-serving-systems-machine-learning-platform-netflix-1640254 | n/s | 2026-11-13 | C | Extract | aggregator copy | jd |
| S31 | Rakuten Symphony, Senior MLOps Engineer, foundit.in/job/senior-mlops-engineer-rakuten-symphony-bengaluru-bangalore-60478569 | n/s | 2026-11-13 | B | Extract | | jd |
| S32 | Aptiv, Senior ML Ops Engineer, themuse.com/jobs/aptiv/senior-ml-ops-engineer-b98787 | n/s | 2026-11-13 | B | Extract | | jd |
| S33 | Quantiphi, Senior MLOps Engineer, builtinbengaluru.in/job/senior-mlops-engineer/4282019 | n/s | 2026-11-13 | B | Extract | | jd |
| S34 | Fractal, Senior Engineer MLOps, builtinbengaluru.in/job/senior-engineer-mlops-5-10yrs/4678832 | n/s | 2026-11-13 | B | Extract | | jd |
| S35 | TransUnion, Senior Advisor OneTru Platform MLOps, builtinhyderabad.in/job/senior-advisor-onetru-platform-mlops/7746409 | n/s | 2026-11-13 | B | Extract | | jd |
| S36 | Veralto, AI/ML Platform Engineer Specialist, builtinbengaluru.in/job/ai-ml-platform-engineer-specialist/7577562 and builtinbengaluru.in/job/senior-ai-ml-platform-engineer-specialist/9083422 | n/s | 2026-11-13 | B | Extract | | jd |
| S37 | Calix, Staff ML Ops Engineer, builtinbengaluru.in/job/staff-ml-ops-engineer/7778546 | n/s | 2026-11-13 | B | Extract | | jd |
| S38 | Autonomize AI, Senior MLOps Engineer, nexthire.breezy.hr/p/f1308550e0f1-autonomize-ai-senior-mlops-engineer | n/s | 2026-11-13 | B | Extract | | jd |
| S39 | RoundCircle, AI/ML Infrastructure Automation Lead, expertini.work (Bengaluru listing) | n/s | 2026-11-13 | C | Extract | aggregator copy | jd |
| S40 | Walmart Global Tech India, Staff Software Engineer (ML Platform team), echojobs.io/job/walmart-ind-staff-software-engineer-7mo4y | n/s | 2026-11-13 | C | Extract | aggregator copy | jd |
| S41 | Canibuild, ML Ops Engineer (remote), builtinbengaluru.in/job/ml-ops-engineer-remote/4236805 | n/s | 2026-11-13 | B | Extract | | jd |
| S42 | Pinterest, Senior Engineering Manager AI/ML Serving Platform, resumegeni.com copy | 2026-03-07 | 2026-11-13 | C | Extract | older than 90 days | management-exit pay |
| S43 | Pinterest, Principal Engineer AI Platform, hotfix.jobs copy | n/s | 2026-11-13 | C | Extract | | principal pay |
| S44 | Kimchi (CAST AI), Senior ML Engineer inference optimisation, job-boards.greenhouse.io/kimchi/jobs/4451244009 | n/s | 2026-11-13 | A | Extract | | exclusion |
| S45 | Together AI, Staff AI Infra Engineer, jobs.generalcatalyst.com/companies/together-ai-2/jobs/97659531 | 2026-10-21 | 2026-11-13 | B | Extract | | exclusion, exit |
| S46 | AWS, Certified Machine Learning Engineer - Associate, aws.amazon.com/certification/certified-machine-learning-engineer-associate/ | 2026-11-12 | 2026-11-13 | A | Read | | credentials |
| S47 | AWS, Certified Machine Learning - Specialty, aws.amazon.com/en/certification/certified-machine-learning-specialty | n/s | 2026-11-13 | A | Extract | | retirement |
| S48 | CNCF, Certified Kubernetes Administrator, cncf.io/certification/CKA/ and cncf.io/training/certification/cka/ | n/s | 2026-11-13 | A | Extract | | fee, format |
| S49 | Training Camp, What is CKA, trainingcamp.com/what-is-cka/ | 2026-09 | 2026-11-13 | C | Extract | | validity, duration |
| S50 | Levels.fyi, Machine Learning Ops Engineer salary, levels.fyi/t/software-engineer/title/machine-learning-ops-engineer | 2026-10-11 | 2026-11-13 | B | Extract | date format ambiguous | US total compensation |
| S51 | Levels.fyi, Apple ML Ops Engineer salaries (en-gb page) | 2026-06-15 | 2026-11-13 | B | Extract | | Apple package |
| S52 | Fast AI Jobs, MLOps / Infrastructure salary page, fastaijobs.com/salaries/mlops-infra-engineer | 2026-07 | 2026-11-13 | B | Extract | | pay series |
| S53 | Hugging Face, text-generation-inference documentation, huggingface.co/docs/text-generation-inference/en/index.md | n/s | 2026-11-13 | A | Extract | | TGI maintenance mode |
| S54 | Hugging Face blog, huggingface.co/blog/hf-dwarez/hf-aws-sagemaker-skills | n/s | 2026-11-13 | A | Extract | | TGI archived |
| S55 | Spheron, TGI migration guide, spheron.network/blog/migrate-tgi-to-vllm-sglang-2026/ | 2026 | 2026-11-13 | C | Extract | vendor | archive date |
| S56 | NVIDIA developer blog, Optimize AI inference performance, developer.nvidia.com/blog/optimize-ai-inference-performance-with-nvidia-full-stack-solutions | 2025-03 | 2026-11-13 | A | Extract | | Triton rename |
| S57 | NVIDIA, Dynamo, developer.nvidia.com/en-us/dynamo.md | n/s | 2026-11-13 | A | Extract | | Dynamo successor |
| S58 | Storyboard18, Quess GCC talent shortfall, storyboard18.com/how-it-works/indias-1900-gccs-face-18-43-talent-shortfall-in-key-tech-roles-quess-corp-90866.htm | 2026-02-26 | 2026-11-13 | C | Extract | COI (staffing firm) | gap range |
| S59 | Business Today, Quess GCC Talent Trends Q1 FY27 (article dated 2026-07-15), businesstoday.in | 2026-07-15 | 2026-11-13 | C | Extract | COI (staffing firm) | platform gap, 4–12 years |
| S60 | Business Standard, Quess GCC Talent Trends Q2 FY27 (article dated 2026-11-05), business-standard.com | 2026-11-05 | 2026-11-13 | C | Extract | COI (staffing firm) | hiring dip, AI gap |
| S61 | OwnYourCareer, MLOps Engineer salaries India, ownyourcareer.in/careers/mlops-engineer/salaries | 2026-07 | 2026-11-13 | C | Extract | method undisclosed | India bands |
| S62 | Futurense, MLOps engineer salary in India, futurense.com/blog/mlops-engineer-salary-in-india | 2026 | 2026-11-13 | C | Extract | COI (edtech) | India average |
| S63 | IIT Kharagpur online, AI/ML engineer salary India, online.iitkgp.ac.in/blog/ai-ml-engineer-salary-india | 2026 | 2026-11-13 | C | Extract | COI (edtech) | India average |
| S64 | CorpReady, MLOps engineer salary, corpready.in/salary/mlops-engineer | 2026 | 2026-11-13 | D | Extract | derived, not measured | excluded |
| S65 | ITJobsWatch, MLOps UK, itjobswatch.co.uk/jobs/uk/mlops.do | 2026-02-18 | 2026-11-13 | B | Extract | skill-citation count | UK demand, pay |
| S66 | ITJobsWatch, MLOps East London, itjobswatch.co.uk/jobs/east%20london/mlops.do?p=6 | 2026-10-20 | 2026-11-13 | B | Extract | | London median |
| S67 | Wellhub, Senior AI Platform Engineer, job-boards.greenhouse.io/gympass/jobs/8539560002 | n/s | 2026-11-13 | A | Read | | jd, LLMOps, geography |
| S68 | Wellhub, Senior MLOps Engineer, job-boards.greenhouse.io/gympass/jobs/8590439002 | n/s | 2026-11-13 | A | Extract (fetch Blocked by bot detection) | | jd |
| S69 | Mistral AI, Platform Engineer Data Infrastructure & MLOps, freehire.me/jobs/platform-engineer-data-infrastructure-mlops-mistral-2ewtc2c5 | 2026-08-31 | 2026-11-13 | B | Extract | aggregator copy | jd |
| S70 | Vriba, AI / MLOps Platform Engineer, bebee.com/in/jobs/ai-mlops-platform-engineer-vriba-bengaluru--t7xk-888212613 | 2026-11 | 2026-11-13 | C | Extract | aggregator copy | jd |
| S71 | CI&T, Senior MLOps Engineer, jobs.lever.co/ciandt/19b90ec5-87f3-40f2-9d46-4f1c1379b22d | n/s | 2026-11-13 | A | Read | | jd |
| S72 | Anthropic, Staff+ Software Engineer Kubernetes Platform, job-boards.greenhouse.io/anthropic/jobs/5211241008 (pay from an indexventures.com copy) | 2026-09-05 | 2026-11-13 | A | Extract | COI (author's developer) | adjacent frontier-lab role and pay |
| S73 | AI Infra Interviews, companies hiring AI infrastructure engineers, aiinfrainterviews.com/guide/companies-hiring-ai-infrastructure-engineers | 2026-09 | 2026-11-13 | C | Extract | vendor catalogue | frontier-lab titles |
| S74 | Axial, MLOps skills, axialsearch.com/insights/mlops-skills | 2026 | 2026-11-13 | C | Extract | recruiter | proof of work, credentials |
| S75 | Devlyn, How to hire an MLOps engineer, alpeshnakrani.pages.dev/blog/hire-mlops-engineer/ | 2026-04-17 | 2026-11-13 | C | Extract | COI (sells MLOps engineers) | variants, proof |
| S76 | careery.pro, AI/ML engineer H-1B LCAs, careery.pro/h1b-sponsors/role/ai-ml-engineer | FY2026 data | 2026-11-13 | B | Extract | adjacent family | LCA context |
| S77 | DataInterview, Netflix MLOps engineer interview, datainterview.com/blog/netflix-mlops-engineer-interview | 2026-10 | 2026-11-13 | C | Extract | | loop, AI-tool report |
| S78 | StepStone, E. Zoller Software Engineer KI, MLOps & Fullstack, stepstone.de/stellenangebote--software-engineer-m-w-d-ki-mlops-fullstack-mannheim-e-zoller-gmbh-co-kg--14515719-inline.html | 2026-09-17 | 2026-11-13 | B | Extract | German-language probe | alias |
| S79 | enercity, Cloud & MLOps Expert (J2025782), enercity.de/karriere/jobsuche/cloud-mlops-expert-J2025782 | n/s | 2026-11-13 | B | Extract | German-language probe | alias |
| S80 | Computacenter, MLOps Engineer Data & AI Platforms, StepStone listing page stepstone.de/jobs/tooling-engineer/in-hallbergmoos | n/s | 2026-11-13 | C | Extract | German-language probe; listing page | alias, tools |
| S81 | Right Search, (Senior) AI Engineer / MLOps Engineer Munich, arbeitnow.com/jobs/companies/right-search/senior-ai-engineer-mlops-engineer-munich-86006 | n/s | 2026-11-13 | C | Extract | recruiter | alias, Germany pay |
| S82 | StepStone, Techniker Krankenkasse KI Platform Engineer Hamburg, stepstone.de/stellenangebote--ki-platform-engineer-m-w-d-hamburg-techniker-krankenkasse--14383305-inline.html | 2026-08-10 | 2026-11-13 | B | Extract | outside window by 3 days | alias |
| S83 | NVIDIA, Senior MLOps Engineer, builtincharlotte.com/job/senior-mlops-engineer/7292191 | n/s | 2026-11-13 | B | Extract | aggregator copy | jd, pay |
| S84 | Microsoft AI, Machine Learning Operations (MLOps) Engineer, microsoft.ai/job/machine-learning-operations-mlops-engineer/ | n/s | 2026-11-13 | A | Extract | | jd |
| S85 | Scale AI, AI Infrastructure Engineer Serving Platform, scale.com/careers/4717977005 | n/s | 2026-11-13 | A | Extract | | jd |
| S86 | TensorOps, MLOps Engineer, builtincharlotte.com/job/mlops-engineer/7381416 | n/s | 2026-11-13 | B | Extract | aggregator copy | jd |
| S87 | IT-Online, Senior Data Scientist (ML Engineer), it-online.co.za/2026/09/14/senior-data-scientist-ml-engineer/ | 2026-09-14 | 2026-11-13 | B | Extract | adjacent role | CKA named |
| S88 | DevClass, partner content on platform engineering citing DORA 2025, devclass.com/ml-ai/2026/08/06/partner-content-platform-engineering-20-your-platform-was-built-for-a-different-era-ai-just-exposed-it/5283935 | 2026-08-06 | 2026-11-13 | C | Extract | partner content (COI); DORA original not opened | durability |
| S89 | Vultr and platformengineering.org, State of AI in Platform Engineering (via CRN India), crn.in/ai/platform-engineers-emerge-as-ai-enablers-amid-enterprise-adoption-gaps | n/s | 2026-11-13 | C | Extract | COI (sponsor) | durability |
| S90 | Perforce, State of Platform Engineering 2026, perforce.com/press-releases/state-of-platform-engineering-2026 | 2026-07-08 | 2026-11-13 | C | Extract | COI (vendor) | durability |
| S91 | Pulumi, State of Agentic Infrastructure, pulumi.com/state-of-agentic-infrastructure/ | 2026 | 2026-11-13 | C | Extract | COI (vendor) | durability |
| S92 | Fast AI Jobs, Together AI Platform Engineer Model Shaping job page, fastaijobs.com/job/greenhouse--4790243007 | 2026-07-10 | 2026-11-13 | B | Extract | | posting date |

## Data Appendix

The first block holds the 37 core jd records followed by four German-language probe records that are outside the sample statistics. Must fields hold short skill phrases or paraphrases, not full sentences, because of the quotation limit. Job IDs are given only where a page shows one. A note beginning "Window:" states whether the record meets the 90-day test.

```jsonl
{"type":"jd","grade":"A","src":["S1"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Together AI","title":"Machine Learning, Platform Engineer","url":"https://job-boards.greenhouse.io/togetherai/jobs/4835988007","job_id":"4835988007","seen":"2026-11-13","location":"San Francisco, CA, US","remote":"on-site (Built In copy)","seniority":"senior","years":5,"degree":"BS/MS CS or equivalent practical experience","must":["large-scale fault-tolerant distributed systems","Python, Go, Rust, C++ or Haskell","Terraform-style IaC","Kubernetes internals or other orchestration"],"nice":["serverless inference platform","on-call"],"pay":{"lo":160000,"hi":250000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Read. Board shows no post date. Window: live."}
{"type":"jd","grade":"B","src":["S28","S92"],"as_of":"2026-07-10","ttl":"V1","role":"role:ml-platform-engineer","employer":"Together AI","title":"Platform Engineer, Model Shaping","url":"https://job-boards.greenhouse.io/togetherai/jobs/4790243007","job_id":"4790243007","seen":"2026-11-13","location":"San Francisco, CA, US","remote":"on-site","seniority":"mid","years":3,"must":["Linux","Docker and Kubernetes","Python or Go","deployment of services for AI training or inference","networking fundamentals","on-call rotation"],"nice":["open-source contributions","GPU/HPC networking"],"pay":{"lo":200000,"hi":290000,"currency":"USD","period":"year"},"ats":"Greenhouse","note":"Search extracts only; fetch refused by the tool. Fast AI Jobs lists it as posted 2026-07-10; other copies say 2026-07-28 and 6+ months ago. On-call rotation in the role. Window: outside by posting date; live status unverified."}
{"type":"jd","grade":"A","src":["S2"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Uber","title":"Staff Software Engineer - AI Platform (Michelangelo)","url":"https://www.uber.com/global/hu/careers/list/155038/","job_id":"155038","seen":"2026-11-13","location":"Sunnyvale, CA, US","remote":"office at least half of working time","seniority":"staff","years":8,"degree":"BS/MS CS or equivalent experience","must":["large-scale distributed systems in production","backend and system architecture","performance optimisation"],"nice":["ML serving and inference orchestration","ML lifecycle observability"],"pay":{"lo":232000,"hi":258000,"currency":"USD","period":"year"},"ats":"Uber careers site","note":"Read. Names no Kubernetes, Terraform, Docker or Python. Window: live."}
{"type":"jd","grade":"C","src":["S29"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Pinterest","title":"Staff Software Engineer, ML Platform","url":"https://jobr.pro/job/29273979/staff-software-engineer-ml-platform","seen":"2026-11-13","location":"San Francisco, CA or US remote","remote":"hybrid or US remote","seniority":"staff","must":["ML serving and inference-engine technical strategy"],"pay":{"lo":170000,"hi":351000,"currency":"USD","period":"year"},"ats":"Greenhouse (per aggregator)","note":"Aggregator copy; date unknown; range as shown by the aggregator. Window: unverified."}
{"type":"jd","grade":"C","src":["S30","S77"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Netflix","title":"Software Engineer L4/L5 - Model Serving Systems, Machine Learning Platform","url":"https://www.workingnomads.com/jobs/software-engineer-l4l5-model-serving-systems-machine-learning-platform-netflix-1640254","seen":"2026-11-13","location":"USA","seniority":"mid-senior","must":[],"note":"Aggregator copy; requirements not visible. A guide says Netflix posts ML platform work as software engineer levels 4 to 6 on AI Platform teams. Window: unverified."}
{"type":"jd","grade":"B","src":["S83"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"NVIDIA","title":"Senior MLOps Engineer","url":"https://builtincharlotte.com/job/senior-mlops-engineer/7292191","job_id":"7292191","seen":"2026-11-13","location":"2 locations (not named in the extract)","remote":"in-office or remote","seniority":"senior","must":["infrastructure for AI research and product development","ML pipelines","shorter ML job start-up and data-load times, failure recovery"],"pay":{"lo":184000,"hi":357000,"currency":"USD","period":"year"},"note":"Extract of a Built In copy; posting date not shown. Window: unverified."}
{"type":"jd","grade":"B","src":["S84"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Microsoft (Microsoft AI, Copilot team)","title":"Machine Learning Operations (MLOps) Engineer","url":"https://microsoft.ai/job/machine-learning-operations-mlops-engineer/","job_id":"200016559","seen":"2026-11-13","location":"Mountain View, CA, US","seniority":null,"must":[],"note":"Extract shows title, team and job number only. Window: unverified."}
{"type":"jd","grade":"B","src":["S23"],"as_of":"2026-08-21","ttl":"V1","role":"role:ml-platform-engineer","employer":"Sequen","title":"Staff MLOps Engineer - Machine Learning Platform","url":"https://www.employbl.com/jobs/staff-mlops-engineer-sequen-1649453","seen":"2026-11-13","location":"New York, San Francisco or remote (US)","remote":"yes","seniority":"staff","must":["low-latency model deployment","distributed inference pipelines","observability and drift monitoring","evaluation pipelines"],"nice":["feature stores","experiment tracking"],"pay":{"lo":220000,"hi":280000,"currency":"USD","period":"year"},"ats":"Ashby","note":"Extract; Series A employer. Window: in window by date."}
{"type":"jd","grade":"B","src":["S24"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"dv01","title":"MLOps Engineer","url":"https://www.builtinaustin.com/job/mlops-engineer/9857042","job_id":"9857042","seen":"2026-11-13","location":"Remote (US)","remote":"yes","seniority":"senior","must":["CI/CD for ML workloads","automated tests and staged rollouts"],"pay":{"lo":185000,"hi":200000,"currency":"USD","period":"year"},"note":"Extract of a Built In copy. Window: unverified."}
{"type":"jd","grade":"B","src":["S25"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"TinyFish","title":"MLOps Engineer","url":"https://www.builtinchicago.org/job/mlops-engineer/9913437","job_id":"9913437","seen":"2026-11-13","location":"Remote or hybrid (US)","remote":"yes","seniority":"senior","must":["Prometheus, Grafana and Datadog instrumentation","SLIs and SLOs for data freshness and model latency","alerts and runbooks"],"note":"Extract; reports to the Director of Infra. Window: unverified."}
{"type":"jd","grade":"A","src":["S4"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"SumerSports","title":"MLOps / ML Platform Engineer","url":"https://ats.rippling.com/sumersports/jobs/65f3a402-7cba-40ac-aa47-d0e1a447fb1f","job_id":"65f3a402-7cba-40ac-aa47-d0e1a447fb1f","seen":"2026-11-13","location":"Remote (US)","remote":"yes","seniority":null,"must":["model serving, deployment and observability","IAM, secrets and container security","CI/CD and IaC"],"ats":"Rippling","note":"Board listing read. Description text taken from a search extract under earlier ID 8e1ffdbd-82d9-4181-92cf-f2217d8ef525, which returned job_not_found on 2026-11-13. Window: live."}
{"type":"jd","grade":"B","src":["S26"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"AbsenceSoft","title":"ML Ops Engineer","url":"https://ats.rippling.com/absencesoft/jobs/47f6d8bf-9a68-4738-81dc-26a5954825f5","job_id":"47f6d8bf-9a68-4738-81dc-26a5954825f5","seen":"2026-11-13","location":"Remote (US)","remote":"yes","seniority":null,"must":["Terraform, Kubernetes and Docker","CI/CD (GitHub Actions, Jenkins, Argo, CircleCI)","training-to-monitoring pipelines"],"nice":["RLHF and PEFT workflows"],"ats":"Rippling","note":"Extract; fetch refused by the tool and ID not re-checked (IDs can change). Window: unverified."}
{"type":"jd","grade":"B","src":["S27"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Egen","title":"MLOps Engineer (Principal MLOps Architect, contract)","url":"https://www.builtinboston.com/job/mlops-engineer/8002413","job_id":"8002413","seen":"2026-11-13","location":"Remote tag; text says hybrid in Nashville, TN","seniority":"mid","must":["MLOps pipelines for training, deployment and monitoring","Terraform"],"pay":{"lo":150000,"hi":180000,"currency":"USD","period":"year"},"note":"Extract; consultancy; tag and text conflict on location. Window: unverified."}
{"type":"jd","grade":"A","src":["S67"],"as_of":"2026-11-11","ttl":"V1","role":"role:ml-platform-engineer","employer":"Wellhub","title":"Senior AI Platform Engineer","url":"https://job-boards.greenhouse.io/gympass/jobs/8539560002","job_id":"8539560002","seen":"2026-11-13","location":"Brazil (remote; open only to candidates in Brazil)","remote":"yes, Brazil only","seniority":"senior","must":["Kubeflow, Feast and Spark-on-Kubernetes","CI/CD and IaC (Terraform or Crossplane)","observability","Python libraries, APIs and tooling","AWS and Kubernetes","DevOps applied to ML and AI platforms"],"nice":["LLMOps lifecycle requirements","data catalogue and governance integration"],"ats":"Greenhouse","note":"Read. Date from the Fast AI Jobs listing. Form asks about sponsorship need and pay expectations in BRL. Window: live."}
{"type":"jd","grade":"B","src":["S68"],"as_of":"2026-11-11","ttl":"V1","role":"role:ml-platform-engineer","employer":"Wellhub","title":"Senior MLOps Engineer","url":"https://job-boards.greenhouse.io/gympass/jobs/8590439002","job_id":"8590439002","seen":"2026-11-13","location":"Brazil (remote; open only to candidates in Brazil)","remote":"yes, Brazil only","seniority":"senior","must":["infrastructure and ML/AI orchestration","MLOps practice and LLMOps lifecycle requirements"],"ats":"Greenhouse","note":"Search extract only; page fetch blocked by bot detection and not worked around. Window: in window by date."}
{"type":"jd","grade":"A","src":["S71"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"CI&T","title":"Senior MLOps Engineer (Job-21621)","url":"https://jobs.lever.co/ciandt/19b90ec5-87f3-40f2-9d46-4f1c1379b22d","job_id":"19b90ec5-87f3-40f2-9d46-4f1c1379b22d","seen":"2026-11-13","location":"Sao Paulo, Brazil (remote)","remote":"yes, Brazil","seniority":"senior","degree":"Computer Engineering, Data Science, Information Systems or a related field","must":["Kedro, Argo Workflows and ArgoCD","MLflow tracking and registry","Docker, Kubernetes (EKS) and Helm","Grafana, Prometheus and CloudWatch","AWS with Git and GitHub Actions or GitLab CI"],"nice":["Terraform","DVC, Delta Lake","JFrog Artifactory"],"ats":"Lever","note":"Read. Date not shown. Window: live."}
{"type":"jd","grade":"B","src":["S18"],"as_of":"2026-10-15","ttl":"V1","role":"role:ml-platform-engineer","employer":"Mollie","title":"Machine Learning Platform Engineer I","url":"https://magnet.me/en/opportunity/1095672/machine-learning-platform-engineer-i","seen":"2026-11-13","location":"Amsterdam, NL (Lisbon hub; team spans both)","remote":"remote or hybrid","seniority":"junior","must":["Python and Terraform daily","GCP","CI/CD for ML training and inference","Kubernetes model-serving endpoints","experiment tracking, versioning and monitoring"],"note":"Extract of an aggregator copy; another copy is dated 2026-10-26. Window: in window by date."}
{"type":"jd","grade":"B","src":["S19"],"as_of":"2026-07-28","ttl":"V1","role":"role:ml-platform-engineer","employer":"Synthesia","title":"ML Platform Engineer","url":"https://jobs.accel.com/companies/synthesia/jobs/87795276-ml-platform-engineer","job_id":"87795276","seen":"2026-11-13","location":"Europe (remote)","remote":"yes","seniority":null,"must":["Kubernetes","Terraform","Python","GitHub Actions","Linux","observability (Datadog)"],"nice":["GPU workloads","Temporal"],"note":"Extract; tags from an aggregator page that appears to be this posting; one copy is dated 2026-07-28, outside the window. Window: unverified."}
{"type":"jd","grade":"C","src":["S20"],"as_of":"2026-09-08","ttl":"V1","role":"role:ml-platform-engineer","employer":"Lorien (agency; end client undisclosed)","title":"Senior Platform Engineer (contract)","url":"https://lorien.sites.sourceflow.co.uk/jobs/151333-Senior-Platform-Engineer-","job_id":"BBBH175971_1788884054","seen":"2026-11-13","location":"London, UK","seniority":"senior","must":["Kubernetes-based ML platform","Helm and Terraform","exposure to Kubeflow, KServe or vLLM","LLM inference workloads"],"nice":["JupyterHub","DevOps background"],"note":"Extract; agency contract listing. Window: in window by date."}
{"type":"jd","grade":"C","src":["S22"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Pragmatike (client is a GPU cloud)","title":"ML Ops Engineer","url":"https://bulldogjob.com/companies/jobs/239784-ml-ops-engineer-pragmatike","job_id":"239784","seen":"2026-11-13","location":"not shown (Polish board)","seniority":"mid","years":4,"must":["vLLM, TGI or Triton serving","GPU workloads in production","model registries and CI/CD deployment pipelines","observability and on-call"],"nice":["blue/green and canary rollouts"],"note":"Extract; location unconfirmed. Window: unverified."}
{"type":"jd","grade":"B","src":["S69"],"as_of":"2026-08-31","ttl":"V1","role":"role:ml-platform-engineer","employer":"Mistral AI","title":"Platform Engineer, Data Infrastructure & MLOps","url":"https://freehire.me/jobs/platform-engineer-data-infrastructure-mlops-mistral-2ewtc2c5","seen":"2026-11-13","location":null,"seniority":null,"must":["data infrastructure for training and fine-tuning (compute fleets, storage)","secure MLOps pipelines","Kubernetes"],"note":"Aggregator extract; posted 2026-08-10, updated 2026-08-31, reposted twice; location not shown. Frontier lab; data-infrastructure leaning. Window: in window by update date."}
{"type":"jd","grade":"B","src":["S85"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Scale AI","title":"AI Infrastructure Engineer, Serving Platform","url":"https://scale.com/careers/4717977005","job_id":"4717977005","seen":"2026-11-13","location":"London, UK","seniority":null,"must":["platforms for scalable, reliable LLM serving"],"note":"Extract of the employer page; date not shown; inference-platform variant. Window: unverified."}
{"type":"jd","grade":"A","src":["S3"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"HCLTech","title":"Senior MLOps Technical Lead","url":"https://careers.hcltech.com/job/Senior-MLOps-Technical-Lead/1356949955/","job_id":"1356949955","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"lead","must":["MLflow, Kubeflow Pipelines, TFX and Metaflow","Terraform, CloudFormation and Ansible","Jenkins, GitLab CI and GitHub Actions","Prometheus, Grafana and ELK","Python","DevOps practices and tools"],"nice":["AWS ML Specialty certification","Google Professional ML Engineer certification"],"ats":"SAP SuccessFactors","note":"Read. No Kubernetes named; years and pay not shown. The AWS certification named is retired (last exam 2026-03-31). Window: live."}
{"type":"jd","grade":"B","src":["S31"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Rakuten Symphony","title":"Senior MLOps Engineer","url":"https://www.foundit.in/job/senior-mlops-engineer-rakuten-symphony-bengaluru-bangalore-60478569","job_id":"151586279","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"senior","must":["Kubernetes (operators, CRDs, Helm)","Kubeflow including KServe","MLflow","Feast, Spark and Airflow","SageMaker, Vertex AI or Azure ML"],"note":"Extract from foundit. Window: unverified."}
{"type":"jd","grade":"B","src":["S32"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Aptiv","title":"Senior ML Ops Engineer","url":"https://themuse.com/jobs/aptiv/senior-ml-ops-engineer-b98787","job_id":"Aptiv-J000663843","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"senior","must":["Docker, Kubernetes and Kubeflow","Airflow and SLURM","MLflow and Metaflow","Python, Linux and Git","AWS, Azure or GCP"],"note":"Extract of aggregator copies. Window: unverified."}
{"type":"jd","grade":"B","src":["S33"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Quantiphi","title":"Senior MLOps Engineer","url":"https://builtinbengaluru.in/job/senior-mlops-engineer/4282019","job_id":"4282019","seen":"2026-11-13","location":"Bengaluru, IN (per Built In Bengaluru)","seniority":"senior","must":["Kubernetes and Slurm multi-GPU scheduling","Kubeflow, MLflow and AutoML","Azure ML","CI/CD, Linux and Python"],"nice":["LLMOps"],"note":"Extract. Window: unverified."}
{"type":"jd","grade":"B","src":["S34"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Fractal","title":"Senior Engineer - MLOps (5-10 years)","url":"https://builtinbengaluru.in/job/senior-engineer-mlops-5-10yrs/4678832","job_id":"4678832","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"senior","years":5,"must":["MLflow or Kubeflow model registry","AWS, Azure or GCP","Docker","Python"],"nice":["Dataiku, DataRobot, Hopsworks"],"note":"Extract; years 5 to 10 from the title. Window: unverified."}
{"type":"jd","grade":"B","src":["S35"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"TransUnion","title":"Senior Advisor, OneTru Platform MLOps","url":"https://builtinhyderabad.in/job/senior-advisor-onetru-platform-mlops/7746409","job_id":"7746409","seen":"2026-11-13","location":"Hyderabad, IN","seniority":"senior","must":["MLflow, Kubeflow and Airflow","Docker and Kubernetes","CI/CD"],"note":"Extract. Window: unverified."}
{"type":"jd","grade":"B","src":["S36"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Veralto","title":"AI/ML Platform Engineer Specialist","url":"https://builtinbengaluru.in/job/ai-ml-platform-engineer-specialist/7577562","job_id":"7577562","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"mid","must":["AWS (SageMaker, ECS/EKS, Terraform or CloudFormation)","MLflow, Kubeflow, Vertex AI or Azure ML","Docker and Python"],"nice":["LangChain, Ray, Hugging Face"],"note":"Extract. Window: unverified."}
{"type":"jd","grade":"B","src":["S36"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Veralto","title":"Senior AI/ML Platform Engineer Specialist","url":"https://builtinbengaluru.in/job/senior-ai-ml-platform-engineer-specialist/9083422","job_id":"9083422","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"senior","must":["MLflow, Kubeflow, Vertex AI or Azure ML","LLM infrastructure, vector databases and RAG"],"note":"Extract; sibling of the posting above. Window: unverified."}
{"type":"jd","grade":"B","src":["S37"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Calix","title":"Staff ML Ops Engineer","url":"https://builtinbengaluru.in/job/staff-ml-ops-engineer/7778546","job_id":"7778546","seen":"2026-11-13","location":"Bengaluru, IN (per Built In Bengaluru)","seniority":"staff","must":["GCP ML training and inference infrastructure","Airflow, Kubeflow and MLflow","Kubernetes and Docker","Prometheus, Grafana and ELK","Python and Go"],"note":"Extract. Window: unverified."}
{"type":"jd","grade":"B","src":["S38"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Autonomize AI","title":"Senior MLOps Engineer","url":"https://nexthire.breezy.hr/p/f1308550e0f1-autonomize-ai-senior-mlops-engineer","seen":"2026-11-13","location":"Bangalore, IN","seniority":"senior","years":4,"must":["Kubeflow and MLflow workflows","Python","LLM management systems"],"note":"Extract of a Breezy copy. Window: unverified."}
{"type":"jd","grade":"C","src":["S39"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"RoundCircle (agency)","title":"AI/ML Infrastructure Automation Lead (Senior MLOps Engineer)","url":"https://expertini.work/result/work-aiml-infrastructure-automation-lead-bengaluru-roundcircle-622737009695656005-india/","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"lead","must":["Azure, Databricks and MLflow","Kubernetes deployments","Terraform IaC","monitoring and logging"],"note":"Aggregator extract. Window: unverified."}
{"type":"jd","grade":"C","src":["S40"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Walmart Global Tech India","title":"Staff Software Engineer (ML Platform team)","url":"https://echojobs.io/job/walmart-ind-staff-software-engineer-7mo4y","seen":"2026-11-13","location":"Bengaluru, IN","seniority":"staff","must":["advanced Kubernetes cluster management","two or more clouds (GCP, Azure, AWS)","Linux and shell","SQL"],"note":"Aggregator extract. Window: unverified."}
{"type":"jd","grade":"C","src":["S70"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Vriba","title":"AI / MLOps Platform Engineer","url":"https://bebee.com/in/jobs/ai-mlops-platform-engineer-vriba-bengaluru--t7xk-888212613","seen":"2026-11-13","location":"Bengaluru, IN","seniority":null,"must":["Vertex AI, Azure ML or SageMaker","feature stores, model registry and experiment tracking","IaC (Terraform, Bicep)","Kubernetes (AKS, GKE, EKS)","LLM provider integration (OpenAI, Azure OpenAI, Gemini, Claude)","monitoring of AI services and model health"],"note":"Aggregator copy; listing valid until 2026-12-22; employer type unverified. Window: live by validity."}
{"type":"jd","grade":"B","src":["S41"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Canibuild","title":"ML Ops Engineer (remote)","url":"https://builtinbengaluru.in/job/ml-ops-engineer-remote/4236805","job_id":"4236805","seen":"2026-11-13","location":"Remote (listed on Built In Bengaluru)","remote":"yes","seniority":null,"must":["MLflow, Kubeflow and Airflow","SageMaker, Vertex AI or Azure ML","Docker and Kubernetes","CI/CD for ML"],"note":"Extract. Window: unverified."}
{"type":"jd","grade":"B","src":["S86"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"TensorOps","title":"MLOps Engineer","url":"https://builtincharlotte.com/job/mlops-engineer/7381416","job_id":"7381416","seen":"2026-11-13","location":"not shown (remote)","remote":"remote (listing)","seniority":null,"must":["ML infrastructure on GCP and AWS","CI/CD for ML, model-serving infrastructure and observability","MLflow, Weights & Biases and Langfuse","FastAPI, TorchServe and TensorFlow Serving"],"note":"Consultancy; extract of a Built In copy; date unknown. Window: unverified."}
{"type":"jd","grade":"B","src":["S78"],"as_of":"2026-09-17","ttl":"V1","role":"role:ml-platform-engineer","employer":"E. Zoller GmbH & Co. KG","title":"Software Engineer (m/w/d) - KI, MLOps & Fullstack","url":"https://www.stepstone.de/stellenangebote--software-engineer-m-w-d-ki-mlops-fullstack-mannheim-e-zoller-gmbh-co-kg--14515719-inline.html","seen":"2026-11-13","location":"Mannheim, DE","seniority":null,"must":[],"note":"German-language probe; outside the sample statistics; extract shows title and date only. Window: in window by date."}
{"type":"jd","grade":"B","src":["S79"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"enercity","title":"Cloud & MLOps Expert (w/m/d)","url":"https://www.enercity.de/karriere/jobsuche/cloud-mlops-expert-J2025782","job_id":"J2025782","seen":"2026-11-13","location":null,"seniority":null,"must":["technology base for scalable, secure AI systems"],"note":"German-language probe; outside the sample statistics; date not shown. Window: unverified."}
{"type":"jd","grade":"C","src":["S80"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Computacenter","title":"MLOps Engineer (w/m/d) - Data & AI Platforms","url":"https://www.stepstone.de/jobs/tooling-engineer/in-hallbergmoos","seen":"2026-11-13","location":null,"seniority":null,"must":["MLOps tools such as Kubeflow and MLflow","operation of data and AI platforms"],"note":"German-language probe; outside the sample statistics; the URL is a listing page because the posting URL was not shown. Window: unverified."}
{"type":"jd","grade":"C","src":["S81"],"as_of":"2026-11-13","ttl":"V1","role":"role:ml-platform-engineer","employer":"Right Search (recruiter)","title":"(Senior) AI Engineer / MLOps Engineer (w/m/d)","url":"https://www.arbeitnow.com/jobs/companies/right-search/senior-ai-engineer-mlops-engineer-munich-86006","seen":"2026-11-13","location":"Munich, DE","seniority":"senior","must":[],"pay":{"lo":80000,"hi":100000,"currency":"EUR","period":"year"},"note":"German-language probe; outside the sample statistics; recruiter listing that treats MLOps, ML Platform, ML DevOps and AI Infrastructure Engineer as interchangeable titles. Window: unverified."}
```

The second block holds skill signals (computed over the 31 coded core records), measures and pay.

```jsonl
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"kubernetes","n":31,"source_kind":"jd-sample","count":19,"share":0.613,"tier_hint":"must","note":"Coded over 31 of 37 core jd records with skill text; lower bound."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"mlops_lifecycle","n":31,"source_kind":"jd-sample","count":21,"share":0.677,"tier_hint":"must","note":"Named lifecycle tooling (MLflow, Kubeflow, registry, tracking, feature store) or explicit lifecycle wording."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"cloud","n":31,"source_kind":"jd-sample","count":16,"share":0.516,"tier_hint":"must"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"git_ci","n":31,"source_kind":"jd-sample","count":14,"share":0.452,"tier_hint":"must","note":"Platform figure in the knowledge base is 81.2%; not reproduced."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"iac","n":31,"source_kind":"jd-sample","count":13,"share":0.419,"tier_hint":"must","note":"The knowledge base lists terraform and iac as separate IDs with identical shares."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"observability","n":31,"source_kind":"jd-sample","count":13,"share":0.419,"tier_hint":"must"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"python","n":31,"source_kind":"jd-sample","count":12,"share":0.387,"tier_hint":"must","note":"Extracts often omit languages."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"docker","n":31,"source_kind":"jd-sample","count":9,"share":0.29,"tier_hint":"important"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"aws","n":31,"source_kind":"jd-sample","count":10,"share":0.323,"tier_hint":"should"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"linux","n":31,"source_kind":"jd-sample","count":5,"share":0.161,"tier_hint":"should"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"devops","n":31,"source_kind":"jd-sample","count":3,"share":0.097,"tier_hint":"should","note":"Explicit word DevOps only; the knowledge base figure is 99.0%."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"serving_engines","n":31,"source_kind":"jd-sample","count":3,"share":0.097,"tier_hint":"should","note":"vLLM, TGI, Triton or KServe named. Name vLLM, SGLang and Dynamo Triton; TGI is in maintenance mode (S53, S56)."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"kserve_ray","n":31,"source_kind":"jd-sample","count":2,"share":0.065,"tier_hint":"should","note":"KServe only; Ray named without Ray Serve."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"sre","n":31,"source_kind":"jd-sample","count":4,"share":0.129,"tier_hint":"should","note":"On-call or SLO language."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"iam","n":31,"source_kind":"jd-sample","count":1,"share":0.032,"tier_hint":"optional"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"llm_gateways","n":31,"source_kind":"jd-sample","count":0,"share":0,"tier_hint":"optional","note":"MCP and agent protocols also 0 of 37."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"supply_chain","n":31,"source_kind":"jd-sample","count":0,"share":0,"tier_hint":"optional"}
{"type":"skill_signal","grade":"M","src":["S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:mlflow","n":31,"source_kind":"jd-sample","count":14,"share":0.452,"tier_hint":"important","note":"India-led; the India query named the tool."}
{"type":"skill_signal","grade":"M","src":["S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:kubeflow","n":31,"source_kind":"jd-sample","count":13,"share":0.419,"tier_hint":"important","note":"MLflow or Kubeflow union 16 of 31 (51.6%); 11 of 13 India postings and 5 of 18 others."}
{"type":"skill_signal","grade":"M","src":["S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:airflow","n":31,"source_kind":"jd-sample","count":5,"share":0.161,"tier_hint":"should"}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:gpu-scheduling","n":31,"source_kind":"jd-sample","count":5,"share":0.161,"tier_hint":"should","note":"GPU, CUDA, Slurm or HPC; important for the AI-cloud variant."}
{"type":"skill_signal","grade":"M","src":["S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:llm-ops","n":31,"source_kind":"jd-sample","count":10,"share":0.323,"tier_hint":"should","note":"LLMOps, RAG, vector DB, RLHF, LLM-provider integration or LLM serving (for example vLLM) named."}
{"type":"skill_signal","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:go","n":31,"source_kind":"jd-sample","count":3,"share":0.097,"tier_hint":"optional"}
{"type":"skill_signal","grade":"M","src":["S67","S71"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"new:feature-store","n":31,"source_kind":"jd-sample","count":5,"share":0.161,"tier_hint":"optional"}
{"type":"skill_signal","grade":"B","src":["S5"],"as_of":"2026-07-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"python","n":1959,"source_kind":"platform","share":0.667,"tier_hint":"must","note":"Axial states over two-thirds; the value is a lower bound."}
{"type":"skill_signal","grade":"B","src":["S5"],"as_of":"2026-07-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"cloud","n":1959,"source_kind":"platform","share":0.667,"tier_hint":"must","note":"Axial states over two-thirds for cloud platforms; the value is a lower bound."}
{"type":"skill_signal","grade":"B","src":["S5"],"as_of":"2026-07-13","ttl":"V3","role":"role:ml-platform-engineer","skill":"mlops_lifecycle","n":1959,"source_kind":"platform","share":0.667,"tier_hint":"must","note":"Axial states over two-thirds for MLOps tooling; the value is a lower bound. Observability and CI/CD follow close behind."}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-07-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"US MLOps postings since 2026-01-01","unit":"postings","value":1959,"region":"US","method":"vendor classifier over public boards; undisclosed","note":"Older than 31 days at retrieval."}
{"type":"measure","grade":"B","src":["S5","S7"],"as_of":"2026-07-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"new US MLOps postings per week","unit":"postings per week","value":70,"region":"US","note":"Flat through the first half of 2026."}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ml-platform-engineer","measure":"open roles in the MLOps / Infrastructure Engineer category","unit":"roles","value":1099,"region":"global (startup-led)","note":"Broad category including systems and reliability roles."}
{"type":"measure","grade":"B","src":["S8"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ml-platform-engineer","measure":"companies hiring in the same category","unit":"companies","value":423,"region":"global"}
{"type":"measure","grade":"B","src":["S9"],"as_of":"2026-06-16","ttl":"V1","subject":"role:ml-platform-engineer","measure":"open roles in the same category, earlier snapshot","unit":"roles","value":630,"region":"global","note":"Snapshot date inferred from listed posting dates."}
{"type":"measure","grade":"M","src":["S8","S9"],"as_of":"2026-11-12","ttl":"V1","subject":"role:ml-platform-engineer","measure":"change in category open roles, mid-June to 2026-11-12","unit":"percent","value":74.4,"note":"Category definition may have changed."}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings at mid level","unit":"percent","value":36,"region":"US"}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings at senior IC level","unit":"percent","value":33,"region":"US"}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings at principal IC level","unit":"percent","value":13,"region":"US"}
{"type":"measure","grade":"B","src":["S7"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings at junior IC level","unit":"percent","value":9,"region":"US"}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings in management","unit":"percent","value":8,"region":"US"}
{"type":"measure","grade":"B","src":["S6","S7"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"fully remote share among postings stating a work model (44% state one)","unit":"percent","value":42,"region":"US","note":"Hybrid 38, on-site 20."}
{"type":"measure","grade":"B","src":["S6"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings from employers of 10,000 or more staff","unit":"percent","value":34,"region":"US","note":"Employers under 50 staff post 13%; contract share 13%."}
{"type":"measure","grade":"B","src":["S5","S7"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings in California","unit":"percent","value":27,"region":"US","note":"Texas and New York about 9% each; San Francisco 9.3% excluding remote-only."}
{"type":"measure","grade":"B","src":["S5"],"as_of":"2026-07-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of US postings requiring a degree","unit":"percent","value":63,"region":"US","note":"Computer science named in 67% of degree-specifying postings."}
{"type":"measure","grade":"B","src":["S65"],"as_of":"2026-02-18","ttl":"V1","subject":"role:ml-platform-engineer","measure":"UK permanent IT jobs citing MLOps, six months to 2026-02-18","unit":"jobs","value":184,"region":"GB","method":"ITJobsWatch skill-citation count","note":"Skill count, not title count. Share of UK permanent IT jobs 0.27% (0.32% a year earlier)."}
{"type":"measure","grade":"B","src":["S65"],"as_of":"2025-02-18","ttl":"V1","subject":"role:ml-platform-engineer","measure":"UK permanent IT jobs citing MLOps, same six-month window a year earlier","unit":"jobs","value":156,"region":"GB","note":"Two years earlier: 139."}
{"type":"measure","grade":"M","src":["S65"],"as_of":"2026-02-18","ttl":"V1","subject":"role:ml-platform-engineer","measure":"year-on-year change in UK jobs citing MLOps","unit":"percent","value":17.9,"region":"GB","note":"184 against 156."}
{"type":"measure","grade":"C","src":["S58"],"as_of":"2025-12-31","ttl":"V3","subject":"role:ml-platform-engineer","measure":"India GCC supply gap across AI/ML Ops, platform engineering, cybersecurity and GenAI operations (Q3 FY26)","unit":"percent","lo":18,"hi":43,"region":"IN","note":"GCC-wide; staffing-firm report (Quess); date is the quarter end."}
{"type":"measure","grade":"C","src":["S59"],"as_of":"2026-06-30","ttl":"V3","subject":"role:ml-platform-engineer","measure":"India GCC platform engineering supply gap (Q1 FY27)","unit":"percent","lo":32,"hi":36,"region":"IN","note":"GCC-wide, not role-specific."}
{"type":"measure","grade":"C","src":["S60"],"as_of":"2026-09-30","ttl":"V3","subject":"role:ml-platform-engineer","measure":"India GCC AI and data analytics supply gap (Q2 FY27)","unit":"percent","lo":38,"hi":42,"region":"IN","note":"GCC-wide, not role-specific."}
{"type":"measure","grade":"C","src":["S60"],"as_of":"2026-09-30","ttl":"V3","subject":"role:ml-platform-engineer","measure":"India GCC tech hiring demand, quarter on quarter (July to September 2026)","unit":"percent","value":-3.5,"region":"IN","note":"GCC-wide."}
{"type":"measure","grade":"C","src":["S59"],"as_of":"2026-06-30","ttl":"V3","subject":"role:ml-platform-engineer","measure":"share of India GCC hiring demand from professionals with 4 to 12 years of experience (Q1 FY27)","unit":"percent","value":56,"region":"IN","note":"GCC-wide."}
{"type":"measure","grade":"C","src":["S14"],"as_of":"2025-12-31","ttl":"V3","subject":"role:ml-platform-engineer","measure":"MLOps and model deployment share of AI postings, India, 2025","unit":"percent","value":10,"region":"IN","note":"Reported by Masai School citing foundit (up 42%); original not opened; COI (edtech). Date is the period end."}
{"type":"measure","grade":"B","src":["S76"],"as_of":"2026-06-30","ttl":"V4","subject":"role:ml-platform-engineer","measure":"certified H-1B LCAs, AI/ML engineer title family, FY2025 plus FY2026 through Q3","unit":"LCAs","value":8275,"region":"US","method":"aggregator over DOL disclosure files","note":"Adjacent family, not MLOps-titled. LCAs show what was filed, not pay. California 3,853."}
{"type":"measure","grade":"C","src":["S88"],"as_of":"2026-08-06","ttl":"V3","subject":"role:ml-platform-engineer","measure":"organisations with an internal platform, per a secondary report of DORA 2025","unit":"percent","value":90,"region":"global","note":"76% have dedicated platform teams. Partner content; the DORA original was not opened. As-of is the article date."}
{"type":"measure","grade":"C","src":["S89"],"as_of":"2026-11-13","ttl":"V3","subject":"role:ml-platform-engineer","measure":"platform teams hosting or planning AI workloads","unit":"percent","value":75,"region":"global","note":"Sponsor-run survey (Vultr and platformengineering.org); 89% use AI daily for code and documents; COI; survey date not shown, so as-of is the retrieval date."}
{"type":"measure","grade":"M","src":["S1","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample postings remote-eligible","unit":"percent","value":38,"n":37,"method":"jd sample","note":"14 of 37; 3 are open only to candidates in Brazil."}
{"type":"measure","grade":"M","src":["S1","S2","S3","S67","S71"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample postings meeting the strict window test","unit":"percent","value":32,"n":37,"method":"jd sample","note":"12 of 37; 5 read in full on an employer board."}
{"type":"measure","grade":"M","src":["S3"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample postings naming any certification","unit":"percent","value":2.7,"n":37,"method":"jd sample","note":"1 of 37 (HCLTech, optional)."}
{"type":"measure","grade":"M","src":["S1","S2","S23","S24","S27","S28","S29","S83"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"US sample postings disclosing base pay","unit":"percent","value":61.5,"n":13,"method":"jd sample","note":"8 of 13 US postings; none of the 24 non-US postings disclosed pay."}
{"type":"measure","grade":"M","src":["S3","S31","S32"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"India sample postings with MLOps in the title","unit":"percent","value":61.5,"n":13,"method":"jd sample","note":"8 of 13."}
{"type":"measure","grade":"M","src":["S36"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample share in specialisation: vector search infrastructure","unit":"percent","value":2.7,"n":37,"method":"jd sample","note":"1 of 37 (Veralto senior)."}
{"type":"measure","grade":"M","src":["S22"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample share in specialisation: gateways and model routing","unit":"percent","value":2.7,"n":37,"method":"jd sample","note":"1 of 37 (Pragmatike, request-routing layers)."}
{"type":"measure","grade":"M","src":["S1","S2","S3"],"as_of":"2026-11-13","ttl":"V1","subject":"role:ml-platform-engineer","measure":"sample share in specialisation: MCP and agent protocols","unit":"percent","value":0,"n":37,"method":"jd sample","note":"0 of 37; Netflix lists an Agent Platform team in a guide only."}
{"type":"pay","grade":"M","src":["S1","S2","S23","S24","S27","S28","S29","S83"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"T0-58 jd sample, posted ranges","lo":150000,"hi":357000,"n":8,"note":"Posted bands, not realised pay."}
{"type":"pay","grade":"M","src":["S1","S2","S23","S24","S27","S28","S29","S83"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"T0-58 jd sample, band midpoints","value":245000,"n":8,"note":"Mean midpoint 229200."}
{"type":"pay","grade":"M","src":["S2","S23","S29"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"US","level":"staff","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"T0-58 jd sample","lo":170000,"hi":351000,"n":3,"note":"Uber 232-258K, Sequen 220-280K, Pinterest 170-351K."}
{"type":"pay","grade":"M","src":["S1","S24","S83"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"US","level":"senior","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"T0-58 jd sample","lo":160000,"hi":357000,"n":3,"note":"Together AI 160-250K, dv01 185-200K, NVIDIA 184-357K."}
{"type":"pay","grade":"M","src":["S27","S28"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"US","level":"mid","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"T0-58 jd sample","lo":150000,"hi":290000,"n":2,"note":"Egen 150-180K; Together AI Model Shaping (3+ years) 200-290K."}
{"type":"pay","grade":"B","src":["S8"],"as_of":"2026-11-12","ttl":"V3","role":"role:ml-platform-engineer","location":"global (USD parsed)","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Fast AI Jobs, MLOps / Infrastructure Engineer","value":179250,"n":430,"note":"Disclosing postings only; range 51,360 to 999,999; broad category."}
{"type":"pay","grade":"B","src":["S9"],"as_of":"2026-06-16","ttl":"V3","role":"role:ml-platform-engineer","location":"global (USD parsed)","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Fast AI Jobs, MLOps / Infrastructure Engineer","value":175000,"n":212,"note":"Snapshot date inferred."}
{"type":"pay","grade":"B","src":["S52"],"as_of":"2026-07-01","ttl":"V3","role":"role:ml-platform-engineer","location":"global (USD parsed)","employer_type":"ai-startup","stat":"p50","currency":"USD","period":"year","basis":"base","source_name":"Fast AI Jobs, MLOps / Infrastructure Engineer at AI startups","value":170000,"n":289,"note":"Month only is stated (July 2026)."}
{"type":"pay","grade":"C","src":["S12"],"as_of":"2026-10-29","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"DataInterview, LinkedIn MLOps postings","lo":120000,"hi":326000,"note":"Software Engineer to Sr. Staff; n not stated."}
{"type":"pay","grade":"B","src":["S50"],"as_of":"2026-10-11","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"p25","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Machine Learning Ops Engineer","value":120000,"note":"n not shown; Software Engineer family, DevOps specialisation."}
{"type":"pay","grade":"B","src":["S50"],"as_of":"2026-10-11","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Machine Learning Ops Engineer","value":145200}
{"type":"pay","grade":"B","src":["S50"],"as_of":"2026-10-11","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"p75","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Machine Learning Ops Engineer","value":200000}
{"type":"pay","grade":"B","src":["S50"],"as_of":"2026-10-11","ttl":"V3","role":"role:ml-platform-engineer","location":"US","stat":"p90","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Machine Learning Ops Engineer","value":295000}
{"type":"pay","grade":"B","src":["S51"],"as_of":"2026-06-15","ttl":"V3","role":"role:ml-platform-engineer","location":"US","employer_type":"big-tech","stat":"p50","currency":"USD","period":"year","basis":"tc","source_name":"Levels.fyi, Apple Machine Learning Ops Engineer","value":439250,"note":"The page also shows an ICT4 package of 464K (base 230K, stock 200K a year, bonus 34.3K); the two figures differ."}
{"type":"pay","grade":"B","src":["S72"],"as_of":"2026-09-05","ttl":"V3","role":"role:ml-platform-engineer","location":"San Francisco, New York or Seattle, US","level":"staff+","employer_type":"frontier-lab","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Anthropic Staff+ SWE, Kubernetes Platform (posted band)","lo":320000,"hi":485000,"note":"Adjacent AI-infrastructure role, not in the sample statistics; COI (author's developer)."}
{"type":"pay","grade":"C","src":["S43"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"San Francisco, US","level":"principal","employer_type":"big-tech","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Pinterest principal AI platform (hotfix.jobs copy)","lo":243000,"hi":500000,"note":"Posting date unknown."}
{"type":"pay","grade":"C","src":["S42"],"as_of":"2026-03-07","ttl":"V3","role":"role:ml-platform-engineer","location":"US","level":"senior engineering manager","employer_type":"big-tech","stat":"range","currency":"USD","period":"year","basis":"base","source_name":"Pinterest Sr EM AI/ML Serving Platform (resumegeni copy)","lo":208592,"hi":429454,"note":"Management exit; older than 90 days."}
{"type":"pay","grade":"B","src":["S66"],"as_of":"2026-10-20","ttl":"V3","role":"role:ml-platform-engineer","location":"London, UK","stat":"p50","currency":"GBP","period":"year","basis":"base","source_name":"ITJobsWatch, jobs citing MLOps","value":75000,"note":"Advertised salaries; skill-citing jobs, all levels."}
{"type":"pay","grade":"B","src":["S65"],"as_of":"2026-02-18","ttl":"V3","role":"role:ml-platform-engineer","location":"UK excluding London","stat":"p50","currency":"GBP","period":"year","basis":"base","source_name":"ITJobsWatch, jobs citing MLOps","value":87500}
{"type":"pay","grade":"B","src":["S65"],"as_of":"2026-02-18","ttl":"V3","role":"role:ml-platform-engineer","location":"UK","stat":"p75","currency":"GBP","period":"year","basis":"base","source_name":"ITJobsWatch, jobs citing MLOps","value":95000}
{"type":"pay","grade":"B","src":["S65"],"as_of":"2026-02-18","ttl":"V3","role":"role:ml-platform-engineer","location":"UK","stat":"p90","currency":"GBP","period":"year","basis":"base","source_name":"ITJobsWatch, jobs citing MLOps","value":127000}
{"type":"pay","grade":"C","src":["S81"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"Munich, DE","level":"senior","stat":"range","currency":"EUR","period":"year","basis":"base","source_name":"Right Search recruiter posting","lo":80000,"hi":100000,"n":1,"note":"Single posting; date not shown."}
{"type":"pay","grade":"C","src":["S61"],"as_of":"2026-10-01","ttl":"V3","role":"role:ml-platform-engineer","location":"India","level":"entry","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"OwnYourCareer","lo":800000,"hi":1500000,"note":"Method undisclosed; basis not stated, assumed CTC."}
{"type":"pay","grade":"C","src":["S61"],"as_of":"2026-10-01","ttl":"V3","role":"role:ml-platform-engineer","location":"India","level":"mid (3-5 years)","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"OwnYourCareer","lo":2000000,"hi":3500000}
{"type":"pay","grade":"C","src":["S61"],"as_of":"2026-10-01","ttl":"V3","role":"role:ml-platform-engineer","location":"India","level":"senior (6+ years)","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"OwnYourCareer","lo":3800000,"hi":6500000}
{"type":"pay","grade":"C","src":["S62"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"Futurense (edtech, COI)","lo":1200000,"hi":1600000,"note":"Reported as the broad market average band, all levels."}
{"type":"pay","grade":"C","src":["S63"],"as_of":"2026-11-13","ttl":"V3","role":"role:ml-platform-engineer","location":"India","stat":"range","currency":"INR","period":"year","basis":"tc","source_name":"IIT Kharagpur online blog citing Glassdoor (COI)","lo":800000,"hi":2000000,"note":"Reported as an average range, all levels."}
```

The third block holds credential, loop, practice and absence records.

```jsonl
{"type":"credential","grade":"A","src":["S48","S49"],"as_of":"2026-11-13","ttl":"V2","id":"cncf_cka","name":"Certified Kubernetes Administrator (CKA)","issuer":"CNCF with The Linux Foundation","level":"performance-based (listed under the CNCF expert path)","state":"active","url":"https://www.cncf.io/certification/CKA/","format":"online proctored, hands-on tasks in a live cluster","proctored":true,"duration_min":120,"fee":{"amount":445,"currency":"USD"},"validity_months":24,"jd_signal":{"value":0,"unit":"postings naming it","n":37,"region":"all","method":"T0-58 jd sample, extract-limited"},"note":"Fee, one free retake and online proctored format from the CNCF page extract (A); duration and validity from third-party guides (C). An adjacent South African ML-engineer posting prefers CKA or CKAD (S87)."}
{"type":"credential","grade":"A","src":["S46"],"as_of":"2026-11-13","ttl":"V2","id":"aws_mla_c01","name":"AWS Certified Machine Learning Engineer - Associate (exam MLA-C01)","issuer":"Amazon Web Services","level":"associate","state":"retiring","url":"https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/","exam_code":"MLA-C01","format":"65 questions, multiple choice and multiple response","proctored":true,"duration_min":130,"items":65,"fee":{"amount":150,"currency":"USD"},"validity_months":36,"retires":"2026-09-28","jd_signal":{"value":0,"unit":"postings naming it","n":37,"region":"all","method":"T0-58 jd sample, extract-limited"},"note":"English exam ended 2026-09-28; Korean, Japanese and Simplified Chinese versions stay until MLA-C02 general availability. AWS lists MLOps engineer among the candidate roles."}
{"type":"credential","grade":"A","src":["S46"],"as_of":"2026-11-13","ttl":"V2","id":"aws_mla_c02","name":"AWS Certified Machine Learning Engineer - Associate (exam MLA-C02, beta)","issuer":"Amazon Web Services","level":"associate","state":"beta","url":"https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/","exam_code":"MLA-C02 (page lists ME1-C02)","format":"85 questions, multiple choice and multiple response","proctored":true,"duration_min":170,"items":85,"fee":{"amount":75,"currency":"USD"},"validity_months":36,"launched":"2026-09-29","renamed_from":"aws_mla_c01","note":"Beta registration opened 2026-09-01 and beta delivery began 2026-09-29, English only; general availability date not stated; fee is beta pricing. Adds Bedrock, RAG, agentic AI and LLM operationalisation; lists LLMOps engineer among candidate roles."}
{"type":"credential","grade":"A","src":["S47","S3"],"as_of":"2026-11-13","ttl":"V2","id":"aws_mls_c01","name":"AWS Certified Machine Learning - Specialty (MLS-C01)","issuer":"Amazon Web Services","level":"specialty","state":"retired","url":"https://aws.amazon.com/en/certification/certified-machine-learning-specialty","exam_code":"MLS-C01","validity_months":36,"retires":"2026-03-31","jd_signal":{"value":1,"unit":"postings naming it","n":37,"region":"all","method":"T0-58 jd sample (HCLTech, as optional)"},"note":"Last exam date 2026-03-31; existing holders keep the credential for 3 years from the date earned."}
{"type":"loop","grade":"C","src":["S10"],"as_of":"2026-09-04","ttl":"V3","employer":"Aggregated MLOps Engineer reports (Dataford)","track":"infrastructure","stages":["recruiter screen","technical interviews (77% of reports)","assessment or take-home (46%)","behavioural (38%)","final onsite (8%)"],"formats":"IaC, MLOps, experiment tracking, model versioning, Docker; CI/CD for AI models; drift-monitoring design","ai_policy":null,"take_home":"46% of reports","note":"Method undisclosed. The knowledge base's KV-cache and decode-roofline content fits inference-platform postings only."}
{"type":"loop","grade":"C","src":["S11"],"as_of":"2026-09-04","ttl":"V3","employer":"Aggregated ML Platform Engineer reports (Dataford)","track":"infrastructure","stages":["recruiter screen (56%)","technical interviews (56%)","assessment or take-home (33%)"],"formats":"real-time feature store design; pipeline bottleneck","ai_policy":null,"take_home":"33% of reports"}
{"type":"loop","grade":"C","src":["S12"],"as_of":"2026-10-29","ttl":"V3","employer":"LinkedIn (AI Platform teams)","track":"infrastructure","stages":["coding phone screen","two coding rounds","system design","hiring-manager behavioural","technical communication on a past project"],"ai_policy":null,"note":"No report specific to AI Platform; general software engineer loop."}
{"type":"loop","grade":"C","src":["S77"],"as_of":"2026-10-31","ttl":"V3","employer":"Netflix (AI Platform teams)","track":"infrastructure","stages":["onsite coding","onsite system design drawn from team work (weighs most)"],"formats":"reported prompts: an ML job scheduler, an ML platform portal, feature serving by freshness","ai_policy":"A July 2026 press report says AI tools are allowed in coding rounds; it cites no Netflix source (D).","note":"Netflix publishes no process; guide reviewed October 2026, day not shown."}
{"type":"loop","grade":"C","src":["S13"],"as_of":"2026-11-13","ttl":"V3","employer":"Employer-side framework (HireInSouth)","track":"infrastructure","stages":["technical screen","take-home or live deployment exercise with monitoring","MLOps platform system design"],"ai_policy":null,"note":"A recommendation to hiring managers by a hiring vendor, not a report."}
{"type":"practice","grade":"P","src":["S20","S3","S71"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"Tie each platform bullet to model-serving or model-lifecycle scope","claim":"Generic DevOps bullets with no ML scope are weak for this role","evidence":"Agency postings say the focus is not simply running Kubernetes clusters; HCLTech and CI&T list ML tooling","verdict":"use"}
{"type":"practice","grade":"C","src":["S74","S75","S1"],"as_of":"2026-11-13","ttl":"V3","area":"proof","tactic":"Publish a deployed-system write-up with a production-incident post-mortem, and contribute to MLOps open source (MLflow, Kubeflow, Feast, Ray)","claim":"Recruiter sources weight deployed systems, open-source work and incident write-ups above certificates","evidence":"Axial recruiter guidance; Devlyn vendor blog (COI); Together AI asks candidates to discuss failures","verdict":"use-with-care","risk":"Vendor and recruiter sources, not first-party hiring-manager statements."}
{"type":"practice","grade":"C","src":["S75","S1","S2","S67"],"as_of":"2026-11-13","ttl":"V3","area":"resume","tactic":"State which variant the resume targets: platform, infrastructure or applied MLOps","claim":"MLOps is several jobs under one title","evidence":"Vendor view (COI) and the sample's variants (Big Tech serving platform, AI-cloud platform, product-company platform, India MLflow and Kubeflow MLOps)","verdict":"use-with-care"}
{"type":"practice","grade":"A","src":["S46","S47"],"as_of":"2026-11-13","ttl":"V2","area":"credentials","tactic":"Check exam status on the issuer page before booking or citing a certificate","claim":"AWS ML Specialty can no longer be earned and MLA-C01 has moved to MLA-C02 (beta)","evidence":"AWS certification pages","verdict":"use"}
{"type":"practice","grade":"M","src":["S17","S21","S4"],"as_of":"2026-11-13","ttl":"V1","area":"job search","tactic":"Confirm a posting is live on the employer's board before investing in an application; use aggregator copies only to find it","claim":"Aggregator copies outlive employer postings","evidence":"Walmart R-2465787 returned not found and Epidemic Sound's posting redirected on 2026-11-13; SumerSports' job ID was replaced","verdict":"use"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"US LCA filings for MLOps-titled roles","searched":"careery.pro, visa-bulletin.us and h1bvisajobs aggregator pages; only AI/ML engineer, ML engineer, DevOps and data-engineer families surfaced; official DOL files not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Primary India pay source for MLOps titles","searched":"AmbitionBox pages (other titles only), edtech and content pages; none with a disclosed method"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Levels.fyi figures for India or Europe","searched":"One Levels.fyi search; only US pages surfaced"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"First-party hiring-manager statements on proof of work","searched":"One search; only recruiter and vendor blogs found"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Typical prior roles of people hired into the role, from published analyses","searched":"Not found in the searches run"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Strongest public proof-of-work examples","searched":"Not collected in this session"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Taggd GCC MLOps title claim","searched":"Quess reports opened via news coverage; the Taggd source was not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"AWS MLOps Demonstrated and Google Professional ML Engineer exam pages","searched":"Named on other pages; not opened"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"India-specific interview differences for this role","searched":"No India-specific loop evidence surfaced in the interview searches"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Employer-stated AI-tool policies in this role's loops","searched":"Guides S10 to S13 and S77; only a press report on Netflix (D)"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Frontier-lab postings titled MLOps or ML platform beyond Mistral","searched":"One combined search plus platform pages; Anthropic's role is adjacent infrastructure"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Full-text reads of sample postings on employer boards","searched":"5 of 37 read in full; Wellhub MLOps blocked by bot detection (not worked around); AbsenceSoft and Together AI Model Shaping refused by the fetch tool"}
{"type":"absence","grade":"E","src":[],"as_of":"2026-11-13","item":"Non-English postings beyond German; non-technical skills (c1 to c4)","searched":"One German-language search; non-technical skills not coded"}
{"type":"absence","grade":"E","src":["S16"],"as_of":"2026-11-13","item":"JobsPipe MLOps-specific count","searched":"Surfaced ML Engineer and DevOps pages only"}
```
