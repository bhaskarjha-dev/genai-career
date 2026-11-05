#!/usr/bin/env python3
"""A-Z title index generator for career/02-roles/role-catalog.md.

Every title string the catalogs classify lives in the structured list E below
(title, type, maps-to slug, evidence or note). The script sorts it and renders the
table between the <!-- BEGIN GENERATED INDEX --> and <!-- END GENERATED INDEX -->
markers, so the order and the counts are computed, not typed by hand.

Usage:
    python3 scripts/build_index.py              # print the table and the type counts
    python3 scripts/build_index.py --update     # rewrite the index block in the master catalog
    python3 scripts/build_index.py --check      # exit 1 if the index block is out of date

Standard library only.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "career" / "02-roles" / "role-catalog.md"
BEGIN, END = "<!-- BEGIN GENERATED INDEX -->\n", "\n<!-- END GENERATED INDEX -->"

# (title, type, maps_to, evidence/note)
# types: Canonical, Alias, Level variant, Specialisation, Cluster variant, Brief label,
#        Legacy/absorbed, Quarantined, Unmeasured buzzword, Candidate (unmeasured),
#        Persona, Certification, Programme, Not a role
E = [
# ---------------- canonical (29) ----------------
("AI Engineer", "Canonical", "ai-engineer", "E · US 1,697 / India 398 live (JobsPipe) · T0-01 F1"),
("Applied AI Engineer", "Canonical", "applied-ai-engineer", "V · 16 of newest 50 AI rows (Fast AI Jobs) · T0-01 D2"),
("Agentic AI Engineer", "Canonical", "agentic-ai-engineer", "W · ~66 postings/90 days (Skillenai, derived) · T0-16"),
("AI Product Engineer", "Canonical", "ai-product-engineer", "W · thin, senior-skewed AI-frontend demand · T0-06 KF-6"),
("AI Enablement Engineer", "Canonical", "ai-enablement-engineer", "W · ~53 postings/90 days (Skillenai, derived) · T0-16"),
("Machine Learning Engineer", "Canonical", "ml-engineer", "E · US 1,084 / global 2,157 live (JobsPipe) · T0-01 F1"),
("Applied Scientist", "Canonical", "applied-scientist", "V · 14 at 12 AI startups (Jun 2026); Big Tech unmeasured · T0-01 D2"),
("Forward Deployed Engineer (FDE)", "Canonical", "forward-deployed-engineer", "E · 933-role cluster at 343 AI startups · T0-01 F3"),
("AI / GenAI Solutions Architect", "Canonical", "ai-solutions-architect", "V · no AI-architect title count; ≥~350 US SA postings mention AI (upper bound, model) · JobsPipe 2026-11-02"),
("Inference / LLM Serving Engineer", "Canonical", "inference-engineer", "V · Rise 28; ≥8 named JDs · T0-01 D2, T0-03 §6.2"),
("GPU Kernel / ML Compiler Engineer", "Canonical", "gpu-kernel-engineer", "V · CUDA/kernels in 6.6% of S09 postings · T0-03 §6.3"),
("AI Infrastructure / GPU Platform Engineer", "Canonical", "ai-infrastructure-engineer", "V · 52 base-disclosing infra postings (S09) · T0-03 §6.1.2"),
("ML Platform / MLOps Engineer", "Canonical", "ml-platform-engineer", "V · probable; GCC supply gap 18–43% · T0-01 D2, F10"),
("AI Evaluation Engineer", "Canonical", "ai-evaluation-engineer", "W · Rise 'LLM evaluation' 26; named JDs · T0-01 D2, T0-03 J12"),
("AI Security Engineer / AI Red Teamer", "Canonical", "ai-security-engineer", "W · ~23 'AI Security Specialist' postings/90 days · T0-16"),
("Responsible AI / AI Governance Engineer", "Canonical", "responsible-ai-engineer", "W · thin technical niche · T0-15 F6"),
("Research Engineer / Member of Technical Staff", "Canonical", "research-engineer", "V · OpenAI MTS-RE 84, Anthropic RE 63 LCA positions (2025) · T0-02"),
("Research Scientist (AI/ML)", "Canonical", "research-scientist", "V · OpenAI MTS-RS 68 LCA positions (2025) · T0-02"),
("Frontier AI Safety / Alignment Researcher", "Canonical", "ai-safety-researcher", "V · ~600 technical FTEs across 67 orgs (C) · T0-15 F8"),
("AI Governance Programme Lead / Manager", "Canonical", "ai-governance-lead", "V · 1,997 US AI-governance postings Jan–Sep 2026 (C) · T0-15"),
("AI Risk, Audit & Compliance Specialist", "Canonical", "ai-risk-assurance-specialist", "A · specialisation inside audit/model-risk/privacy · T0-15"),
("AI Product Manager", "Canonical", "ai-product-manager", "V · no AI-PM title count; ≥~970 US PM postings mention AI (upper bound, model) · JobsPipe 2026-11-02"),
("Domain Evaluation Specialist / AI Trainer", "Canonical", "domain-evaluation-specialist", "W · expert-contract marketplaces (Mercor >30,000 experts) · T0-06"),
("Physical AI / Robotics AI Engineer", "Canonical", "physical-ai-engineer", "W · 8 of newest 50 AI rows were Figure AI · T0-01 F2"),
("AI Engineering Manager / Director of AI Engineering", "Canonical", "ai-engineering-manager", "V · lead/manager label on 5.6% of AI Eng postings · JobsPipe JD"),
("VP / Head of AI", "Canonical", "vp-head-of-ai", "V · Radford 'Head of AI' survey job family (data paywalled); no count or pay in corpus · T0-02"),
("Chief AI Officer (CAIO)", "Canonical", "chief-ai-officer", "V · OMB M-25-21 federal mandate (B) · T0-15"),
("Fractional Head of AI / Fractional CAIO", "Canonical", "fractional-ai-leader", "V · Go Fractional rates and post counts · T0-18"),
("Independent AI Consultant / Contractor", "Canonical", "independent-ai-consultant", "V · asking corridor $150–$250/hr (US) · T0-18"),
# ---------------- Applied AI aliases/variants ----------------
("AI Application Engineer", "Alias", "ai-engineer", "~30 postings/90 days (Skillenai, derived) · T0-16 §9.2"),
("AI Software Engineer", "Alias", "ai-engineer", "Generic variant; no separate count"),
("AI Developer", "Alias", "ai-engineer", "India broad-market title (Glassdoor n=167) · T0-02, T0-11"),
("GenAI Engineer / GenAI Developer", "Alias", "ai-engineer", "Dominant India GCC label (Taggd, C) · T0-01 D8"),
("Generative AI Engineer", "Alias", "ai-engineer", "Quest Global, Genia, Danta postings · T0-01 D2"),
("LLM Engineer", "Alias", "ai-engineer", "Partial evidence; EggAI JD · T0-01 D2, T0-03 J11"),
("Backend LLM Engineer", "Alias", "ai-engineer", "n=1 (LiteLLM, $120–180K + equity) · T0-05"),
("Full-Stack AI Engineer", "Alias", "ai-engineer", "Advice: apply under this title from frontend · T0-06"),
("Cleared GenAI Engineer", "Alias", "ai-engineer", "Accenture Federal Services posting · T0-11"),
("Graduate / Junior GenAI Engineer", "Level variant", "ai-engineer", "Capgemini Singapore posting · T0-11"),
("AWS and GenAI Engineer", "Alias", "ai-engineer", "Staffing-agency posting · T0-11"),
("Senior AI Engineer", "Level variant", "ai-engineer", "Senior cut of all S09 AI-engineering postings: posted base $185–253K (n=462) · T0-03 §6.1.2"),
("Staff AI Engineer", "Level variant", "ai-engineer", "Staff scope = shared eval/observability practice · T0-14"),
("Principal AI Engineer", "Level variant", "ai-engineer", "Staff+/Principal posted base $230–310K (n=322) · T0-03"),
("Lead AI Engineer", "Level variant", "ai-engineer", "JobsPipe sample posting"),
("Distinguished AI Engineer / Fellow", "Level variant", "ai-engineer", "T5 level; 'not observable in medians' · T0-17"),
("Site AI Engineer", "Specialisation", "ai-engineer", "Construction domain variant (Suffolk Construction posting in the JobsPipe US sample, 2026-11-02) · T0-01 F2"),
("Power Platform & AI Engineer", "Specialisation", "ai-engineer", "Enterprise-automation variant inside the AI Engineer family · T0-01 F2"),
("Analytics-AI Engineer", "Specialisation", "ai-engineer", "BI route: text-to-SQL / analytics copilots · T0-06 R2"),
("Production AI Application Engineer", "Brief label", "ai-engineer", "Pipeline-brief target for DS/BI; no posting count · T2-01"),
("Prompt Engineer", "Legacy/absorbed", "ai-engineer", "72 of 20,662 LinkedIn AI postings (0.35%; 2025 arXiv study) · T0-03 KF2; T0-01 F8"),
("Prompt & Context Optimization Engineer", "Legacy/absorbed", "ai-engineer", "Unsourced label [P]; no posting evidence"),
("Vector Search & Retrieval Systems Engineer", "Candidate (unmeasured)", "ai-engineer", "Unsourced label [P]; retrieval is a skill area (RAG in 54% of AI Eng JDs)"),
("Retrieval / Search Engineer (LLM)", "Candidate (unmeasured)", "ai-engineer", "No title count in corpus; retrieval quality is a Tier-2 skill · T0-03"),
("Context Retrieval Engineer", "Specialisation", "applied-ai-engineer", "Databricks 'Senior Staff Applied AI Engineer – Context Retrieval' · T0-01 D7"),
("Partner Applied AI Engineer", "Alias", "applied-ai-engineer", "OpenAI posting · T0-01 D7"),
("AI Agent Engineer", "Alias", "agentic-ai-engineer", "~5 of newest 50 AI rows · T0-01 D2"),
("Agent Engineer", "Alias", "agentic-ai-engineer", "28 postings/90 days (Skillenai) · T0-16"),
("Agentic Systems / Multi-Agent Engineer", "Alias", "agentic-ai-engineer", "Unsourced label [P]; no separate posting count"),
("Principal Agentic AI Engineer", "Level variant", "agentic-ai-engineer", "Weekday India listing · T0-01 D8"),
("AI-Frontend Engineer", "Alias", "ai-product-engineer", "Productboard/Artisan-style postings · T0-06"),
("Frontend Engineer (AI)", "Alias", "ai-product-engineer", "Forward-deployed frontend listing · T0-06"),
("Staff AI Frontend Engineer", "Level variant", "ai-product-engineer", "One recruiter posting, $250–315K (C/D) · T0-06"),
("Agent Interface Architect", "Brief label", "ai-product-engineer", "Pipeline-brief target; no posting count · T2-01"),
("Client-Side AI Specialist", "Not a role", "ai-product-engineer", "Persona-3 heading; on-device AI 'a differentiator, not a job' · T2-01"),
("On-Device / Edge AI Engineer", "Candidate (unmeasured)", "ai-product-engineer", "No posting evidence; differentiator only · T2-01, T0-06"),
("On-Device & Edge SLM Engineer", "Candidate (unmeasured)", "ai-product-engineer", "Unsourced label [P]; CoreML/ONNX claims not found in the corpus"),
("AI Enablement & Internal DevEx Lead", "Level variant", "ai-enablement-engineer", "Unsourced label [P]; only 'AI Enablement Engineer' is evidenced"),
("AI Ops / Enablement Lead (non-coding)", "Specialisation", "ai-enablement-engineer", "Non-technical lane ~7 months (model) · T0-06 R2"),
("AI Product Ops", "Brief label", "ai-enablement-engineer", "Pipeline-brief target; no posting count · T2-01"),
("Conversational & Voice AI Engineer", "Candidate (unmeasured)", "ai-engineer", "Voice is an interview archetype (C), no title count · T0-14 A12"),
# ---------------- ML / science ----------------
("ML Engineer", "Alias", "ml-engineer", "Short form"),
("AI/ML Engineer", "Alias", "ml-engineer", "Common India GCC label · T0-01 D8"),
("Deep Learning Engineer", "Alias", "ml-engineer", "No separate count"),
("Open-Source Machine Learning Engineer", "Alias", "ml-engineer", "n=1 (Hugging Face, US Remote; merged PRs required) · T0-05"),
("Senior Machine Learning Engineer", "Level variant", "ml-engineer", "JobsPipe title facets: senior 814 of 2,157 (~38%; JD seniority labels give 23.2%) · T0-01 D3"),
("Machine Learning Engineer (GenAI MLE)", "Alias", "ml-engineer", "Unsourced label [P]"),
("NLP Engineer", "Specialisation", "ml-engineer", "Domain variant; not measured in corpus"),
("Computer Vision Engineer", "Specialisation", "ml-engineer", "Domain variant; not measured in corpus"),
("Recommender Systems Engineer", "Specialisation", "ml-engineer", "MLE employer mix skews recsys/ads/AV · T0-01 F2"),
("Applied Research Scientist", "Alias", "applied-scientist", "Radford job family; data paywalled · T0-02"),
("Applied Scientist (GenAI)", "Alias", "applied-scientist", "Unsourced label [P]"),
# ---------------- FDE / solutions ----------------
("Forward Deployed Software Engineer (FDSE)", "Alias", "forward-deployed-engineer", "Alias map · T0-01 Recommendation 1"),
("Forward Deployed AI Engineer", "Alias", "forward-deployed-engineer", "Weekday India listings · T0-01 D8"),
("AI Deployment Engineer", "Alias", "forward-deployed-engineer", "OpenAI posting (Jul 2026) · T0-01 D7"),
("Deployment Engineer", "Alias", "forward-deployed-engineer", "Engineer-titled FDE variant · T0-01 F3"),
("AI Engineer – FDE", "Alias", "forward-deployed-engineer", "Databricks, many countries · T0-01 D7"),
("Frontier Agents Engineer", "Alias", "forward-deployed-engineer", "'(Forward Deployed Engineering)'; ~22 postings/90 days · T0-01 F3, T0-16"),
("FDE Lead / Manager, Forward Deployed Engineering", "Level variant", "forward-deployed-engineer", "n8n, OpenAI postings · T0-01 D3, D7"),
("Deployment Strategist", "Cluster variant", "forward-deployed-engineer", "Non-engineering; 6 of newest 50 FDE rows · T0-01 F3"),
("Forward Deployed Product Manager (FDPM)", "Cluster variant", "forward-deployed-engineer", "6 of newest 50 FDE rows; see ai-product-manager · T0-01 F3"),
("GTM AI Engineer / GTM Engineer", "Cluster variant", "forward-deployed-engineer", "4 of newest 50 FDE rows · T0-01 F3"),
("Forward Deployed Banker", "Cluster variant", "forward-deployed-engineer", "Single financial-services listing · T0-01 F3"),
("Pre-sales Field Engineer (AI)", "Cluster variant", "forward-deployed-engineer", "1 of newest 50 FDE rows · T0-01 F3"),
("Forward Deployed AI Engineer (FDE / FDSE)", "Alias", "forward-deployed-engineer", "Unsourced label [P]"),
("AI Architect / Enterprise AI Architect", "Alias", "ai-solutions-architect", "Probable, services-concentrated · T0-01 D2 row 13"),
("Agentic AI Architect", "Alias", "ai-solutions-architect", "≥5 postings (Cognizant, Air India, Zoom) · T0-01 F7"),
("Principal AI Architect – Agentic", "Level variant", "ai-solutions-architect", "One of ≥5 agentic-architect postings (employer unspecified) · T0-01 F7"),
("Enterprise AI Solutions Architect", "Alias", "ai-solutions-architect", "Unsourced label [P]"),
("Customer Engineer, AI/ML", "Alias", "ai-solutions-architect", "Google Cloud; experience-based · T0-11"),
("Sr. Specialist Solutions Architect, GenAI", "Alias", "ai-solutions-architect", "Amazon (Bedrock GTM); no certification listed · T0-11"),
("AWS AI Architect", "Alias", "ai-solutions-architect", "Staffing-agency posting; AWS certs preferred · T0-11"),
("AWS AI Solutions Architect", "Not a role", "ai-solutions-architect", "Unsourced label [P]; neither a job title nor a certification in T0-11"),
("Agent Architect (exact)", "Quarantined", "ai-solutions-architect", "~2 exact postings; alias of AI/Solutions Architect · T0-01 F7, D4"),
# ---------------- Infra ----------------
("Inference Engineer", "Alias", "inference-engineer", "Rise 'inference engineer' 28 (small corpus) · T0-01 D2"),
("LLM Serving Engineer", "Alias", "inference-engineer", "No separate count"),
("Inference Systems Engineer", "Alias", "inference-engineer", "Archetype label · T0-03 §4.1"),
("Model Performance Engineer", "Alias", "inference-engineer", "Baseten 'SWE, Model Performance' ($150–250K) · T0-03 J6"),
("Inference Runtime Engineer", "Alias", "inference-engineer", "Anthropic Staff+ SWE, Inference Runtime ($405–485K) · T0-03 J2"),
("Member of Technical Staff, Inference", "Alias", "inference-engineer", "Inferact ($200–400K + equity) · T0-03 J8, T0-05"),
("Optimization Engineer (LLM Serving)", "Alias", "inference-engineer", "Together AI 'LLM Inference Frameworks & Optimization Engineer' · T0-03 J5"),
("Senior / Staff AI Inference Engineer", "Brief label", "inference-engineer", "Pipeline-brief backend target · T2-01"),
("AI/ML System Performance Specialist", "Not a role", "inference-engineer", "Robert Half Zurich salary-guide category, not a posting title · T0-02"),
("Principal ML Engineer, llama.cpp", "Alias", "inference-engineer", "Red Hat ($189,600–351,050; closed) · T0-05"),
("Inference & Serving Systems Engineer", "Alias", "inference-engineer", "Unsourced label [P]"),
("Kernel Engineer / CUDA Engineer", "Alias", "gpu-kernel-engineer", "NVIDIA, AMD, River AI postings · T0-13"),
("ML Compiler Engineer", "Alias", "gpu-kernel-engineer", "XLA/Triton/NeuronX toolchains in JDs · T0-03 J2"),
("Deep Learning Software Engineer, Inference (NVIDIA)", "Alias", "gpu-kernel-engineer", "Base $152–356.5K · T0-03 J3, J4"),
("Member of Technical Staff, Developer Technology", "Alias", "gpu-kernel-engineer", "RadixArk; 4+ yrs GPU/LLM infra · T0-05"),
("AI Infrastructure Engineer", "Alias", "ai-infrastructure-engineer", "Title not counted; infra cut in S09 · T0-03"),
("GPU Cluster & Infra Platform Engineer", "Alias", "ai-infrastructure-engineer", "Unsourced label [P]; scarcity claims unsupported"),
("ML Infrastructure Engineer", "Alias", "ai-infrastructure-engineer", "Physical Intelligence 'ML Infra Engineer, Platform' · T0-01 D2"),
("AI Infra Resident", "Programme", "ai-infrastructure-engineer", "RadixArk paid 1-year residency, listed $200K · T0-05"),
("Distributed Training Engineer", "Unmeasured buzzword", "ai-infrastructure-engineer", "Title not found; function carried under MTS/RE or infra titles · T0-03 Tier 3"),
("Foundation Model Pre-Training Engineer", "Unmeasured buzzword", "research-engineer", "Unsourced label [P]; no posting evidence; Levels.fyi has no pre-training cut · T0-02"),
("ML Platform Engineer", "Alias", "ml-platform-engineer", "Archetype · T0-03 §4.1"),
("MLOps Engineer", "Alias", "ml-platform-engineer", "Partial evidence; posted base $186–277K (n=10) · T0-01, T0-03"),
("AI Platform Engineer", "Alias", "ml-platform-engineer", "No separate count"),
("LLMOps Engineer", "Legacy/absorbed", "ml-platform-engineer", "Skill tag under ML Platform/MLOps (T0-01 Rec. 3); FAD §5.3 mislists it as quarantined"),
("Platform Engineer (Enterprise AI)", "Alias", "ml-platform-engineer", "Boston Scientific 'Senior Platform Engineer – Enterprise AI' · T0-16"),
("Senior Platform Engineer – Enterprise AI", "Level variant", "ml-platform-engineer", "Boston Scientific (MCP gateway) · T0-16"),
("Senior Enterprise AI Control Plane Engineer", "Specialisation", "ml-platform-engineer", "PTC (MCP/LLM gateways, OAuth/OIDC) · T0-16"),
("MCP Control Plane Engineer", "Specialisation", "ml-platform-engineer", "No literal title (T0-16 KF-10); MCP hiring 'not verified at scale' (T0-16 verdict); fold into platform"),
("Agent Gateway Engineer", "Legacy/absorbed", "ml-platform-engineer", "0 postings found; fold into platform · T0-16"),
# ---------------- Evals / safety / security ----------------
("Evals Engineer", "Alias", "ai-evaluation-engineer", "No separate count"),
("Model Quality Engineer / Evals Specialist", "Alias", "ai-evaluation-engineer", "FurtherAI 'Evals & Model Quality' · T0-01 D2"),
("Staff AI Evaluation Engineer", "Level variant", "ai-evaluation-engineer", "Haparz 'Senior & Staff AI Evaluation Engineer' · T0-03 J12"),
("Principal AI Evaluation Engineer", "Level variant", "ai-evaluation-engineer", "Backbase, Hyderabad · T0-09"),
("ML Engineer, LLM Evals & Agent Systems", "Alias", "ai-evaluation-engineer", "deeprec, London · T0-09"),
("Member of Technical Staff, Language Model Evaluations", "Alias", "ai-evaluation-engineer", "Artificial Analysis · T0-05"),
("AI Engineer, LLMOps & Evaluation", "Alias", "ai-evaluation-engineer", "Auxilius AI, Munich · T0-03 J9"),
("AI Security Specialist", "Alias", "ai-security-engineer", "13.0% MCP share, n=3 (~23 postings/90 days) · T0-16"),
("AI Red Teamer", "Alias", "ai-security-engineer", "Red-teaming appears as a JD skill · T0-15"),
("AI Security & Red Team Engineer", "Alias", "ai-security-engineer", "Unsourced label [P]"),
("AI Security Fellow", "Programme", "ai-security-engineer", "Anthropic Fellows programme (US/UK/CA authorisation) · T0-12"),
("Responsible AI Engineer", "Alias", "responsible-ai-engineer", "Cognizant (Chennai) · T0-15"),
("AI Governance Engineer", "Alias", "responsible-ai-engineer", "Stryker $112.8–239.9K; Beacon Hill $75–85/hr · T0-15"),
("AI Safety Engineer (Enterprise Responsible AI)", "Alias", "responsible-ai-engineer", "Exact title returned 0 at regulated enterprises · T0-15"),
("Senior Responsible AI Systems Engineer", "Level variant", "responsible-ai-engineer", "Workday title, posting not read · T0-15"),
("Sr. Responsible AI Analyst", "Alias", "responsible-ai-engineer", "Infosys Bengaluru, fresher, closed · T0-15"),
# ---------------- research ----------------
("Research Engineer", "Alias", "research-engineer", "Anthropic LCA base median $215K (63 positions) · T0-02"),
("Member of Technical Staff (MTS)", "Alias", "research-engineer", "Title wrapper that hides level and function · T0-02"),
("MTS – Research Engineer", "Alias", "research-engineer", "OpenAI LCA title; 84 positions, base median $335K · T0-02"),
("MTS – Software Engineer", "Alias", "research-engineer", "OpenAI LCA title; 107 positions, base median $255K · T0-02"),
("MTS – AI Systems Engineer", "Alias", "research-engineer", "OpenAI LCA title; 67 positions, base median $335K · T0-02"),
("Frontier Lab Research Engineer", "Brief label", "research-engineer", "Pipeline-brief PhD target · T2-01"),
("Post-Training Engineer / RLHF Engineer", "Legacy/absorbed", "research-engineer", "Below quorum as exact title; carried under RE/MTS · T0-01 F9"),
("Post-Training Specialist", "Brief label", "research-engineer", "Pipeline-brief label; no tier, skills or demand data · T2-01"),
("Foundation Model Engineer", "Unmeasured buzzword", "research-engineer", "Listed in FAD §5.3; never searched in T0-01"),
("Research Scientist", "Alias", "research-scientist", "JobsPipe JD (all fields): LLM 24.4%, RL 17.1%"),
("MTS – Research Scientist", "Alias", "research-scientist", "OpenAI LCA title; 68 positions, base median $360K · T0-02"),
("AI Research Scientist (PhD Foundation)", "Alias", "research-scientist", "Unsourced label [P]"),
("Senior Research Scientist (Lab)", "Level variant", "research-scientist", "Lab RS TC medians ~$0.75M–$1.25M · T0-02"),
("Apex / Named Frontier Researcher", "Level variant", "research-scientist", "T5 bespoke packages; 'not observable in medians' · T0-17"),
("AI Safety Engineer (Frontier Alignment)", "Alias", "ai-safety-researcher", "~600 technical FTEs · T0-15 F8"),
("Alignment Researcher", "Alias", "ai-safety-researcher", "No separate count"),
("Mechanistic Interpretability Researcher", "Specialisation", "ai-safety-researcher", "Unsourced label [P]; no headcount source in the corpus"),
("Anthropic Fellow", "Programme", "ai-safety-researcher", "~4 months; >40% of first cohort joined Anthropic · T0-06, T0-12"),
# ---------------- governance ----------------
("AI Governance Officer / Manager / Lead", "Alias", "ai-governance-lead", "PwC, ERGO, Alstom JDs · T0-15"),
("AI Governance Analyst", "Level variant", "ai-governance-lead", "Hays (aviation client), contract · T0-15"),
("AI Governance Specialist", "Alias", "ai-governance-lead", "Alstom Bangalore, Eaton Pune, EXL · T0-15"),
("AI Governance & Compliance Lead", "Alias", "ai-governance-lead", "Unsourced label [P]"),
("Responsible AI Governance Lead", "Alias", "ai-governance-lead", "McKinsey JD (Dec 2024), $152.3–203K · T0-15"),
("Responsible AI Officer", "Alias", "ai-governance-lead", "RBI FREE-AI report term (India), not a recommendation · T0-15"),
("AI Ethics Officer / AI Ethicist", "Legacy/absorbed", "ai-governance-lead", "'Not shown either way'; avoid standalone positioning · T0-15"),
("EU AI Office Staff", "Specialisation", "ai-governance-lead", ">125 professionals; ~40 contract agents sought (D) · T0-15"),
("AI Compliance Specialist", "Legacy/absorbed", "ai-risk-assurance-specialist", "Distinct career 'mostly no'; sits in privacy/legal/GRC · T0-15"),
("Algorithmic Auditor", "Specialisation", "ai-risk-assurance-specialist", "Inside assurance firms; AAIA needs CISA/CIA/CPA · T0-15"),
("AI Risk Manager / Model Risk Validator", "Specialisation", "ai-risk-assurance-specialist", "Model-risk teams; SR 26-2 excludes GenAI · T0-15"),
("Manager / Senior Manager, AI Risk & Validation", "Level variant", "ai-risk-assurance-specialist", "Deloitte, $171.6–338.3K (seen 16 times) · T0-15"),
("Senior AI Risk Analyst", "Alias", "ai-risk-assurance-specialist", "Victaulic title only · T0-15"),
("Responsible AI Analyst / Senior AI Risk Analyst", "Alias", "ai-risk-assurance-specialist", "Unsourced label [P]; one string for two different JD titles (see Sr. Responsible AI Analyst)"),
("Data Protection Officer (DPO, AI)", "Specialisation", "ai-risk-assurance-specialist", "Adjacent statutory role; India DPDP duties from 13 May 2027 · T0-15"),
("ISO/IEC 42001 Auditor", "Specialisation", "ai-risk-assurance-specialist", "No hiring-weight data · T0-15"),
("Conformity Assessor (Notified Body)", "Specialisation", "ai-risk-assurance-specialist", "Not mandated for most Annex III uses · T0-15"),
("AI Data Governance & Privacy Architect", "Not a role", "ai-risk-assurance-specialist", "Unsourced label [P]; not found in any session"),
# ---------------- product ----------------
("Non-Technical AI Product Manager", "Alias", "ai-product-manager", "Non-technical lane ~7 months (model) · T0-06"),
("AI PM", "Alias", "ai-product-manager", "Entry fee: 4+ yrs PM + one shipped model feature (D) · T0-06"),
("Senior Product Manager, Enterprise MCP/AI Control Plane", "Level variant", "ai-product-manager", "Workato posting · T0-16"),
("AI Product Manager (AIPM)", "Alias", "ai-product-manager", "Unsourced label [P]"),
# ---------------- human data ----------------
("Domain Evaluation Lead", "Alias", "domain-evaluation-specialist", "'Highest leverage' non-technical lane · T0-06"),
("Data Annotator", "Alias", "domain-evaluation-specialist", "LinkedIn Jobs on the Rise #4 (C) · T0-06"),
("Expert Contractor (AI Training)", "Alias", "domain-evaluation-specialist", "Mercor ~$85–110/hr average (C/D) · T0-06"),
("Data Operations & RLHF Lead", "Level variant", "domain-evaluation-specialist", "Unsourced label [P]"),
# ---------------- physical ----------------
("Physical AI Engineer", "Alias", "physical-ai-engineer", "JobsPipe US sample · T0-01 F2"),
("Helix AI Engineer", "Alias", "physical-ai-engineer", "Figure AI (8 of newest 50 AI rows) · T0-01 F2"),
("Autonomous Systems Engineer", "Alias", "physical-ai-engineer", "Unsourced label [P]; not found in any session"),
# ---------------- leadership ----------------
("Director of AI Engineering", "Alias", "ai-engineering-manager", "Posts at Teradata, Front, Harrington Starr · T0-01 D3"),
("AI Engineering Manager", "Alias", "ai-engineering-manager", "Front 'AI Engineering Manager (Core AI Platform)' · JobsPipe"),
("Director of Forward Deployed Engineering & AI GTM", "Alias", "ai-engineering-manager", "Aircall · T0-01 D3"),
("Head of AI", "Alias", "vp-head-of-ai", "Radford job family (paywalled) · T0-02"),
("VP of AI / VP of Machine Learning", "Alias", "vp-head-of-ai", "No count or pay in corpus"),
("Chief AI Officer / VP of AI", "Alias", "chief-ai-officer", "Unsourced label [P]; one string for two distinct roles (see Chief AI Officer and VP / Head of AI)"),
("Fractional Chief AI Officer (Fractional CAIO)", "Alias", "fractional-ai-leader", "Asks avg $190–208/hr; demand 'falling sharply' · T0-18"),
("Fractional Chief Technology Officer (Fractional CTO)", "Alias", "fractional-ai-leader", "19 then 17 posts vs 1,042–1,116 profiles (labels 'rising sharply', then 'rising') · T0-18"),
("Fractional AI Architect", "Alias", "fractional-ai-leader", "Vantage Point package $1,800–6,400/month · T0-18"),
("Fractional AI CTO", "Alias", "fractional-ai-leader", "Agency marketing $200–500/hr (C) · T0-18"),
("Independent GenAI Consultant / Advisory Practitioner", "Alias", "independent-ai-consultant", "'$300+ is marketing' · T0-18"),
("AI Consultant / Strategist", "Alias", "independent-ai-consultant", "LinkedIn Jobs on the Rise #2; median 8.2 yrs (C) · T0-06"),
("Senior AI Engineer (Contractor)", "Alias", "independent-ai-consultant", "$130–235/hr rate cards · T0-18"),
# ---------------- quarantined & unmeasured ----------------
("Context Engineer", "Quarantined", "—", "Watchlist: 10–25 live globally, three archetypes · T0-01 F5, D4"),
("AI Context Engineer", "Quarantined", "—", "Adobe title; part of Context Engineer count · T0-01 F5"),
("Data / Context Engineer", "Quarantined", "—", "Staffing listing; part of Context Engineer count · T0-01 F5"),
("Context Architect / Enterprise Context Architect / AI Context Architect", "Quarantined", "—", "2–3 listings · T0-01 D4"),
("Context Harness Engineer", "Quarantined", "—", "One aggregator count, likely fuzzy · T0-01 D4"),
("Principal Agentic Context Engineer", "Quarantined", "—", "Single blog citation, unverified · T0-01 D4"),
("Cognitive Architect", "Quarantined", "—", "339–1,000 raw hits are false positives, except one legacy IBM posting · T0-01 F6"),
("Prompt Wizard", "Quarantined", "—", "0 postings (null result) · T0-01 F8"),
("Vibe Engineer", "Quarantined", "—", "Not searched; blog-labelled 'theater' · T0-01 D2, D4"),
("AI Whisperer", "Unmeasured buzzword", "—", "2023 media label (T0-05 W-13); listed in FAD §5.3 without a search"),
("Neural Network Designer", "Unmeasured buzzword", "—", "Listed in FAD §5.3 without a search"),
("Transformer Specialist", "Unmeasured buzzword", "—", "Listed in FAD §5.3 without a search"),
("Reasoning Engineer", "Unmeasured buzzword", "—", "Listed in FAD §5.3 without a search"),
# ---------------- personas, certs, non-roles ----------------
("Backend / Systems Software Engineer", "Persona", "feeder: backend", "~6 months to applied AI engineer at 15–20 h/wk (model) · T0-06"),
("Data Scientist / BI Analyst", "Persona", "feeder: data_scientist", "DS ~8 months, BI ~11 months (model) · T0-06"),
("Frontend / Full-Stack Engineer", "Persona", "feeder: frontend", "~7 months to AI product/full-stack engineer (model) · T0-06"),
("Non-Technical Professional (Product / Ops / Domain)", "Persona", "feeder: non_technical", "~7 months with 5+ yrs domain; ~22 months from zero code · T0-06"),
("Academic / PhD Researcher", "Persona", "feeder: phd", "~8 months to applied scientist / RE (model) · T0-06"),
("Academic ML/NLP Researcher", "Persona", "feeder: phd", "Unsourced label [P]; duplicate string for the PhD feeder persona"),
("PhD / Academic ML Researcher", "Persona", "feeder: phd", "Unsourced label [P]; duplicate string for the PhD feeder persona"),
("Frontend / Full-Stack Engineer (AI Product Engineer)", "Persona", "feeder: frontend", "Unsourced label [P]; one string for a feeder persona and a target role (see AI Product Engineer)"),
("Azure AI Engineer Associate (AI-102)", "Certification", "—", "Retired 30 Jun 2026; replaced by AI-103 · T0-11"),
("Databricks Certified Generative AI Engineer Associate", "Certification", "—", "$200 exam; 'Low' signal at startups · T0-11"),
("Google Cloud Professional ML Engineer (PMLE)", "Certification", "—", "Active; refreshed for GenAI · T0-11"),
("AWS Certified Machine Learning – Specialty", "Certification", "—", "Retired 31 Mar 2026; successor MLA-C01 · T0-11"),
("Pragmatic Engineer", "Not a role", "—", "A newsletter (G. Orosz), cited as a source · T0-06, T0-09, T0-10"),
("AI Developer Network (AIDN) Developer", "Not a role", "—", "Fabricated from an event name 'AIDN Developer Day' · T0-12"),
("Workday / ATS Systems Administrator", "Not a role", "—", "Fabricated from a vendor document title (T0-04 S10)"),
("GCC AI Specialist", "Not a role", "—", "Null search: not found as a title · T0-01 D8"),
("Functional Safety Engineer (Automotive AI, ISO/PAS 8800)", "Not a role", "—", "Different meaning of 'safety'; out of scope · T0-15"),
("AI Developer Advocate / DevRel (AI)", "Candidate (unmeasured)", "—", "One Ollama DevRel opening on an aggregator · T0-05"),
("Technical Program Manager (AI)", "Candidate (unmeasured)", "—", "Only as 'managers and TPMs (6)' inside the FDE sample · T0-01 F3"),
]


def sort_key(title):
    # Case-insensitive; ignore punctuation and leading articles for a natural A-Z order.
    t = title.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def table():
    titles = [e[0] for e in E]
    dup = [t for t, c in Counter(titles).items() if c > 1]
    if dup:
        raise SystemExit(f"duplicate titles: {dup}")
    canon = {e[2] for e in E if e[1] == "Canonical"}
    mapped = {e[2] for e in E if e[2] not in ("—",) and not e[2].startswith("feeder")}
    if mapped - canon:
        raise SystemExit(f"titles map to non-canonical slugs: {sorted(mapped - canon)}")
    rows = sorted(E, key=lambda e: sort_key(e[0]))
    out = ["| # | Title (as seen) | Type | Maps to | Evidence / note |", "|:---:|---|---|---|---|"]
    for i, (t, ty, m, ev) in enumerate(rows, 1):
        mm = f"`{m}`" if m not in ("—",) and not m.startswith("feeder") else m
        out.append(f"| {i} | {t} | {ty} | {mm} | {ev} |")
    return "\n".join(out)


def block_span(text):
    if text.count(BEGIN) != 1:
        raise SystemExit("expected exactly one BEGIN GENERATED INDEX marker")
    i = text.index(BEGIN) + len(BEGIN)
    j = text.find(END, i - 1)
    if j < 0:
        raise SystemExit("no END GENERATED INDEX marker")
    return i, j


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true", help="rewrite the index block in the master catalog")
    g.add_argument("--check", action="store_true", help="exit 1 if the index block is out of date")
    args = ap.parse_args()
    tbl = table()
    if args.update or args.check:
        text = DOC.read_text(encoding="utf-8")
        i, j = block_span(text)
        if args.check:
            if text[i:j] != tbl:
                print("out of date: career/02-roles/role-catalog.md (A-Z index)")
                sys.exit(1)
            print("up to date")
            return
        DOC.write_text(text[:i] + tbl + text[j:], encoding="utf-8")
        print(f"updated the A-Z index ({len(E)} titles)")
        return
    print(tbl)
    print()
    print("TOTAL", len(E))
    for k, v in sorted(Counter(e[1] for e in E).items(), key=lambda kv: -kv[1]):
        print(k, v)


if __name__ == "__main__":
    main()
