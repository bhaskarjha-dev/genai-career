---
id: roles.hub.ai-security-engineer
title: "AI Security Engineer / AI Red Teamer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-20
summary: "AI Security Engineer / AI Red Teamer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-60]
roles: [ai-security-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# AI Security Engineer / AI Red Teamer

> Secures LLM and agent systems: prompt injection, tool and agent abuse, supply chain, MCP authorisation and red-teaming.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Evaluation, Safety & Security | Security, safety and governance (plane); also L5 Orchestration and context, L3 Inference and ML platforms, L6 Applications and deployment | Watch (W) | #10 of 24 | #10 of 24 · band A · Monte Carlo rank 11 (P10–P90 7–15) | D3 Security |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 5.5 (4.5–6.5) | B | SANS AI security job tracker (mid-Sep 2026, corroborated live 2026-11-19): >850 AI/ML security engineer postings, ~100 AI red-team (+13% WoW), 93 AI supply-chain security; queued for 2026-12-01 exact-title recount [T0-60, T0-69]. |
| Pay | 7 (5.5–8.5) | B | Dated US posted base bands: Amazon Senior AI Red Team $178.4K–$226.7K + RSUs (A), Microsoft MTS $119.8K–$234.7K (B), NVIDIA Senior AI Security Researcher $224K–$431.25K + equity (B, mirror) [T0-60 L262]. |
| Durability | 7.5 (6–9) | D | Judgement. Adversarial and expanding surface: prompt-injection and agent-security hiring (SANS >850 AI/ML sec, ~100 red-team +13% WoW [T0-60 K20]), CVSS 9.8 serving-engine CVEs, MCP CVEs, Braintrust key breach and OWASP LLM/Agentic Top 10 [T0-03 KF12, T0-16 8, T0-14 6.8, T0-60]. |
| Leverage | 8 (7–9) | D | Judgement. Offensive red-teaming and agent-guardrail risk reduction across production AI systems [T0-60]. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4.5 (3.5–6) | B | 9 India AI-security postings (36% of n=25 sample) across Wipro, GlobalLogic, Teamware, Backbase, Ekfrazo, Razorpay, o9 Solutions (Bengaluru/Hyderabad) [T0-60]. |
| India pay | 6 (4.5–7.5) | B | Posted India pay bands found: Rs25–35L (2–5 yrs) and up to Rs50L (founding AI/ML security engineer) [T0-60]. |

India rank (CCI with India inputs): #11 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ◐ 5.5 | ○ 3 | ○ 3.5 | ○ 2 | ◐ 4 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** AppSec & threat modelling, Python (production), OAuth/OIDC, RBAC, SSO, Incident response & SIEM, LLM security (prompt injection, OWASP), Prompt-injection attack & defence, Red-teaming.
- **Important (headline):** Agent abuse & MCP authorisation, Model supply chain & CVEs, Containment (DLP, sandboxing, egress), AWS / Azure / GCP.
- **Full inventory:** 50 skills (Must 10 · Important 12 · Should 18 · Optional 10), each with its evidence and posting keywords: [ai-security-engineer.md](../../03-skills-and-tech/inventories/ai-security-engineer.md).
- **Prerequisites:** Application-security background; Anthropic AI Security Fellow requires US/UK/Canada work authorisation [A · T0-12]
- **Credentials (tie-breakers, not skills):** ISC2 CISSP (Optional: #1 Axial US AI-gov at 10.4% (C), 7.9% GRC Careers (B [COI]), 5/9 India (B); senior security baseline); Model Context Protocol Associate (MCPA) (Optional: Linux Foundation / AAIF MCP Associate ($250, 90 min); protocol specialist signal, hiring lift unmeasured (T0-32)); Certified Kubernetes Security Specialist (CKS) (Optional: CNCF Certified Kubernetes Security Specialist (requires active CKA); relevant for multi-tenant GPU cluster security (T0-32)); ISACA Certified Information Security Manager (CISM) (Optional: #2 on GRC Careers AI-gov at 13.2% (10/76, B [COI]), 8.1% Axial (C), 3/9 India (B); prerequisite for AAISM/AAIR); ISACA Advanced in AI Security Management (AAISM) (Optional: ISACA Advanced in AI Security Management (launched 2025-08; $459/$599 + $50); requires CISM or CISSP (T0-34:L56, T0-60:L79)); CompTIA SecAI+ (CY0-001) (Optional: CompTIA SecAI+ (launched 2026-02; 19% governance weight); vendor-neutral AI security practitioner exam (T0-34:L288, T3-01)); OffSec AI Red Teamer (OSAI / AI-300) (Optional: OffSec hands-on offensive AI security certification; fits offensive red-team tracks (T0-34)); Hack The Box Certified Offensive AI Expert (HTB COAE) (Optional: Hack The Box Certified Offensive AI Expert; lab-based offensive AI red-team credential (T0-34)); GIAC AI Platform Security (GAIPS) (Optional: GIAC AI Platform Security (ANAB ISO 17024 accredited, CyberLive labs; high SANS cost; T0-34:L273, L588)); IAPP CIPT (privacy technologist) (Optional: Privacy-technologist credential for AI data-protection and privacy-by-design security roles (T0-15, T0-34:L269)). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A red-team suite in CI against a working agent, with attack-success rates before and after mitigation; an MCP security audit
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P10 Red-team suite in CI against a working agent](../../05-portfolio/project-archetypes.md#p10) (55%); [P6 Self-hosted LLM platform on Kubernetes](../../05-portfolio/project-archetypes.md#p6) (28%); [P2 Reliable agent: approvals, sandboxed tools, replay, failure injection](../../05-portfolio/project-archetypes.md#p2) (28%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- No interview-track evidence in the corpus for this role. Practise with the closest track's [prep pack](../../08-interviewing/prep-packs.md) and the behavioural pack.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** D3 Security (AI Systems & Infrastructure); headline pattern: "AI Security Engineer: LLM and agent security". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** application security (26.5% of Security Engineer postings), cybersecurity (42.3%), Python (45.7%), IAM (21.6%), incident response (32.4%), AI security, prompt injection, red team, OWASP
- **Leave out or reframe:** Classifier-only defences presented as complete (adaptive attacks beat 12 published defences)
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-ai-security-engineer).

## Specialisations inside this role

- **Red-teaming and adversarial testing** (Security, safety and governance): Alias of AI Security Engineer (AI Red Teamer) in the A–Z index (SANS mid-Sep 2026 ~100 AI red-team postings, +13% WoW [B · T0-60]).
- **Agent and tool security** (Security, safety and governance): No title of its own in the catalog.
- **Content provenance** (Security, safety and governance): No title of its own in the catalog (thin JD signal: 0/25 AI Security [T0-60], 0/11 Governance and 0/8 Responsible AI Engineer postings named C2PA/provenance [T0-61]).
- These are kinds of work, not separate titles; see the [role map](../role-map.md#specialisations-inside-canonical-roles).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [ML Platform / MLOps Engineer](ml-platform-engineer.md) (0.21); [Agentic AI Engineer](agentic-ai-engineer.md) (0.21); [AI / GenAI Solutions Architect](ai-solutions-architect.md) (0.13).
- **Same family (Evaluation, Safety & Security):** [AI Evaluation Engineer](ai-evaluation-engineer.md), [Responsible AI / AI Governance Engineer](responsible-ai-engineer.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-ai-security-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-ai-security-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (as of 2026-11-19), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-20.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

AI Security Engineer / AI Red Teamer secures LLMs, agents, tool permissions and ML supply chains against adversarial abuse [A/B · T0-60 L72, L283, L399]. Across T0-60's extended November 2026 sample (n = 25 postings: 18 first-pass base plus 7 supplementary), the work divides into five distinct variants [A/B/M · T0-60 L72, L212, L283]:

- **Offensive AI red-teaming (14/18 base postings):** authorised adversarial testing for prompt injection, jailbreaks, data extraction, vulnerability discovery and lateral movement — strongly senior and offence-led in US postings (Amazon requires 5+ years of offensive security/pentesting and lists AI/ML security only as preferred) [A/B/M · T0-60 L72, L237, L283, L589].
- **Agent, tool and MCP security (7/18 base):** identifying and mitigating indirect prompt injection, agent hijacking, confused deputies, permission-boundary bypasses and MCP exploits (OpenAI, Menlo Security, NeuralTrust, GlobalLogic, Refractal) [B/M · T0-60 L72, L240, L283, L593–L595, L600, L602, L609].
- **Defensive guardrail and prompt-security platform engineering (3/25 extended):** building prompt-security platforms, prompt-fuzzing harnesses and automated guardrail regression suites (a London financial institution, o9 Solutions, Menlo Security) — the clearest non-offensive route into the field [B/M · T0-60 L72, L88, L254, L283, L605, L610].
- **Adversarial ML and model integrity (3/18 base):** data poisoning, model extraction, inference attacks and adversarial benchmark/tool creation (HiddenLayer, Microsoft AI Model Security Researcher, NVIDIA, Brave) [B/M · T0-60 L251, L285, L591–L592, L597, L608].
- **AppSec for AI and consultancy engagements:** secure AI delivery (Backbase Hyderabad) and client red-team campaigns against on-prem LLMs mapped to MITRE ATLAS and OWASP LLM Top 10 (Wipro, Teamware) [B · T0-60 L283, L601, L603, L606]. Zero of 25 postings covered the scorecard's content-provenance specialisation [M · T0-60 L283, L797].

**Skills reality (base n = 18; lower bounds from heavily excerpted text; ±23–25 pp Wilson intervals — cross-check only).** Red teaming (14/18, 78%, title-driven), prompt injection (8/18, 44%), offensive security experience (7/18, 39%) and agent/tool abuse (7/18, 39%) dominate visible text, alongside adversarial ML (3/18), guardrail engineering (3/25), MITRE ATLAS (2/18) and threat modelling (2/18) [M · T0-60 L72, L235–L254]. Classic scorecard Musts — AppSec (2/18), IAM (1/18), incident response (1/18) and explicit Python (1/18) — appear rarely in truncated excerpts, though baseline cybersecurity fluency is presumed across postings [M · T0-60 L72, L241–L246]. GRC appears in 0 of 18 postings because SANS tracks AI GRC as a separate ~430-posting job family [B/M · T0-60 L226, L247].

**Proof and credentials.** Only **1 of 18 base postings** names any certification (10a Labs lists PNPT, OSCP, CySA+, GCIH or GPEN as preferred; a sister listing adds Security+ and Google Cybersecurity Certificate), and **zero name CISSP** [B/M · T0-60 L79, L287, L598]. Two AI-specific security credentials launched in 2025–2026 (verified against primary CompTIA and ISACA pages on 2026-11-19):
- **CompTIA SecAI+ (CY0-001):** launched 2026-02-17; up to 60 multiple-choice and performance-based questions in 60 minutes, pass 600/900; 3–4 years IT plus 2+ years cybersecurity recommended; US exam price conflicts across resellers (USD 298, 359 and 392) [A/C · T0-60 L79, L287, L467; verified 2026-11-19]. Best treated as Optional for services/consultancy channels [P · T0-60 L92, L785].
- **ISACA AAISM:** launched August 2025; management-focused AI security credential strictly requiring an active, conferred CISM or CISSP; 90 questions in 150 minutes, USD 459 member / USD 599 non-member plus USD 50 application fee across seven secondary sources (one outlier cites USD 575/760) [A/C · T0-60 L79, L287, L467; verified 2026-11-19]. Keep Optional; see [credential ROI](../../04-certifications/credential-roi.md).

Employers instead ask for publications, talks and open-source tools (Amazon, Brave) or prompt-fuzzing and guardrail regression harnesses (o9 Solutions) [A/B · T0-60 L286]. T0-60 did not trace the scorecard's K27 adaptive-attacks citation ("adaptive attacks beat 12 defences", remains Grade D) [D · T0-60 L411].

## Employer landscape and title confusion

**Demand is substantially larger than Phase 0's narrow band-3 count.** Phase 0 rested on ~23 "AI Security Specialist" postings over 90 days (Skillenai), which the scorecard above replaced with the **SANS AI security job tracker** (mid-September 2026, reported by *Cybersecurity Dive* on 2026-10-20; independently confirmed 2026-11-19): **more than 850 AI/ML security engineer postings**, **nearly 100 AI red-team postings** (+13% week-on-week), **93 AI supply-chain security postings**, **48 AI security specialist postings** and **roughly 430 separate AI GRC lead postings**, naming enterprise hiring at Amazon, Mastercard, PepsiCo, SpaceX, Cloudflare and Lucid Motors [B · T0-60 L71, L221–L228; verified 2026-11-19]. Caveat: SANS does not disclose geography or deduplication criteria [B · T0-60 L71, L447].

| Employer group in T0-60 sample (n = 25) | Count | Sampled organisations | Grade |
|---|---|---|---|
| AI-security vendors and AI-native | 8/25 | Menlo Security, Lakera, HiddenLayer, 10a Labs, Pindrop, Refractal, White Circle, NeuralTrust | B · T0-60 L213 |
| Enterprise, services and staffing | 7/25 | Backbase, GlobalLogic, Wipro, Teamware, London bank (2 recruiter ads deduplicated to 1), Ekfrazo (×2) | B · T0-60 L213, L610 |
| Big Tech and frontier labs | 6/25 | Amazon (A-read), Microsoft (×2), NVIDIA; OpenAI (×2) | A/B · T0-60 L213 |
| Product firms and recruiter networks | 4/25 | Razorpay, o9 Solutions, Brave, Weekday partner listing | B · T0-60 L213 |

**High title noise (7 of 32 security postings read were excluded, 22%).** Keyword searches for "AI security" or "AI red team" pull in two major false positives:
1. **AI-for-security roles** that build LLM agents for cyber defence or automated pentesting rather than securing AI systems (excluded: NVIDIA offensive security with LLM agents, Microsoft Security AI engineer, Amazon STORM red team) [B/M · T0-60 L61, L217, L466].
2. **Non-cybersecurity contractor prompt-testing** listings (excluded: Handshake contractor "AI Red Teamer" and a London contract "adversarial tester" explicitly stating it is not a cybersecurity role) [B/M · T0-60 L61, L217, L292, L465].

Classify every posting by *what the job secures*. Observed aliases include `AI Red Team Engineer`, `AI Security Researcher / Research Engineer`, `Offensive Security Engineer (Agent Security)`, `Red Team Specialist - Cyber`, `AI/ML Security Specialist`, `AI & LLM Security Consultant`, `AI Offensive Security Researcher`, `Founding AI Security Engineer` and `AI supply-chain security engineer` [B · T0-60 L284, L400].

## Career path, India demand and market signals

**Entry routes by background.** US and services red-team roles are offence-led and senior (Amazon 5+ years required, 7+ preferred; Wipro and Teamware 5–8 years; GlobalLogic 10–15 years) [A/B · T0-60 L72, L215, L288]. Four practical entry routes appear in T0-60:
- **AppSec, pentesting or red-team engineers (5+ years):** the primary direct feeder into AI red-team postings [A/B · T0-60 L87, L288].
- **Backend and DevSecOps engineers:** target defensive guardrail and prompt-security platform roles that do not require an offensive background (note thin sample: 3/25) [B · T0-60 L88, L288].
- **ML engineers and data scientists:** target adversarial ML and security-research postings (HiddenLayer, Microsoft, Brave, NVIDIA — research variants ask for publications) [B · T0-60 L288].
- **Junior/entry and fellowship paths:** scarce — only 2 of 25 postings carry junior or entry-level aggregator tags (Lakera 1–3 yrs; Refractal London) [B/M · T0-60 L72, L215, L288]. Anthropic's AI Security Fellow workstream runs in partnership with its AI Safety Fellows programme and requires existing US, UK or Canada work authorisation with no visa sponsorship [A, COI · T0-60 L288, L409, L618]. No direct routes appeared for frontend, product-management or non-technical backgrounds; governance-oriented non-technical candidates fit [AI Governance Lead](ai-governance-lead.md) (~430 SANS postings) instead [B · T0-60 L226, L288].

**Pay signals and remote availability (D-019).** T0-60 replaced Phase 0's Grade D pay placeholder across three regions: US posted base ranges span USD 178.4K–226.7K at Amazon Senior AI Red Team (A, plus RSUs), USD 119.8K–234.7K at Microsoft MTS Senior Security Researcher (B) and USD 224K–431.25K plus equity at NVIDIA Senior AI Security Researcher (B), while SANS's broader advertised US medians sit at USD 140K (AI/ML security engineer, n > 850) and USD 124K (AI red team, n ≈ 100) as of mid-September 2026 [A/B · T0-60 L74, L258–L264]. In Europe, a London bank's prompt-security platform role advertises GBP 80K–120K across two recruiter ads and White Circle lists EUR 90K remote Europe [B · T0-60 L74, L265–L266]. Reject unsourced recruiter-blog claims ("USD 180–450k+") and synthetic salary-site India estimates (INR 11–22 lakh, Grade E) [C/E · T0-60 L270, L431]. Full benchmarks live in [pay benchmarks](../../09-compensation/pay-benchmarks.md#pay-by-genai-role-what-the-corpus-measures). Remote work is more common here than in evals or safety: 6 of 25 postings (24%) list remote (HiddenLayer, Lakera, 10a Labs, Pindrop, White Circle, Brave) [M · T0-60 L229, L746]. Refractal's founding London sibling states UK Skilled Worker sponsorship and Global Talent visa assistance; US LCA counts were not collected [B/E · T0-60 L290, L432].

**India demand and pay.** India accounts for **9 of 25 sampled postings (36%)** across Bangalore, Hyderabad and Pune: IT services and staffing firms (Wipro hiring 4 roles for air-gapped banking LLM red-teaming, GlobalLogic, Teamware, Ekfrazo ×2, Backbase Services), Indian product firms (Razorpay, o9 Solutions) and a Weekday partner listing, asking 2–15 years of experience [B · T0-60 L75, L293, L601–L606, L611–L613]. Posted India pay appears in two listings: INR 25–35 lakh (2–5 years, Weekday partner) and "up to" INR 50 lakh (founding AI/ML security engineer, Jumbo Consulting), plus an adjacent lead data-security/RL role at INR 25–60 lakh [B · T0-60 L74, L267–L269]. Note the scorecard's generic "239 Security Engineer India" figure was not re-verified [D · T0-60 L403].

## Interview themes and preparation notes

**No employer-authored AI security interview loop was found in T0-60**, confirming the scorecard's missing interview track [E · T0-60 L277, L433]. One vendor-published recruiter hiring framework (C/E, COI) proposes a practical security loop: screen → deep dive on prompt injection and agent safety → 60–90 minute practical exercise (take-home or live) → discussion of attack research [C/E, COI · T0-60 L276, L775].

**Preparation rules (no model answers; see [interview loops](../../08-interviewing/interview-loops.md) and [prep packs](../../08-interviewing/prep-packs.md)):**
- **Show measured attack-success reduction on a synthetic target.** Build a CI red-team harness against a working agent reporting attack-success rates before and after mitigations, mapped explicitly to OWASP LLM Top 10 and MITRE ATLAS — never disclose client targets [B/P · T0-60 L87, L291, L780].
- **Match artefact type to variant.** Offensive red-team candidates lead with responsibly disclosed findings, bypass write-ups and open red-team tooling; defensive platform candidates lead with prompt-fuzzing harnesses and guardrail regression suites [A/B/P · T0-60 L286, L781].

## Dossier evidence and limits

- **Low full-read rate (critical caveat):** Across T0-60 overall, only **7 of 70 ledger sources (10%)** were read in full; inside the AI security subset, **only 1 of 25 postings** (Amazon Senior Security Engineer, AI Red Team) was read in full on an employer page (alongside *Cybersecurity Dive*'s SANS summary), while 24 postings came from ATS excerpts or aggregator/recruiter mirrors (Grade B) [T0-60 L48, L212, L492–L493].
- **Extract verification and tracker limits:** Two Extract-only Grade A credential rows (S38 ISACA AAISM, S69 CompTIA SecAI+) were independently verified against primary issuer pages on 2026-11-19, though exam pricing still conflicts across third-party sources [T0-60 L467]. SANS tracker geography and classification methods are undisclosed, so classic security roles may inflate counts (consistent with T0-60's 7/32 exclusion rate) [T0-60 L447]. Skill shares on base n = 18 are truncated lower bounds (±23–25 pp Wilson intervals), and only 10 of 25 postings are verified live or dated within 90 days [T0-60 L48, L67, L216].
- **Key absences:** Employer-authored interview loops, Levels.fyi AI security pay pages, US LCA counts, India/Europe platform volume counts, verification of K17's Skillenai count and K27's adaptive-attack paper, and content-provenance postings [T0-60 L429–L440].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
