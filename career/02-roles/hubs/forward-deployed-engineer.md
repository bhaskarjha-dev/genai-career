---
id: roles.hub.forward-deployed-engineer
title: "Forward Deployed Engineer: Role Hub"
content_type: reference
stage: 2
status: published
last_verified: 2026-11-19
review_by: 2026-12-13
summary: "Forward Deployed Engineer on one page: what it is, where the work sits, its scores with evidence grades, who it suits, the skills and proof it needs, how it is interviewed and how to present for it, with links to the full evidence."
sources: [T0-51, T0-01, T0-03, T0-06, T0-14, T0-17, T0-48, T0-53]
roles: [forward-deployed-engineer]
generated_by: "scripts/build_role_hubs.py (generated blocks)"
---

<!-- BEGIN GENERATED: scripts/build_role_hubs.py (card) -->
# Forward Deployed Engineer

> Engineer embedded with customers who deploys, integrates and adapts AI products end to end, usually with domain depth and travel.

| Family | Work footprint | Evidence status | GenAI target | CCI rank | Résumé variant |
|---|---|---|---|---|---|
| Forward Deployment & Solutions | L6 Applications and deployment; also L5 Orchestration and context | Established (E) | #4 of 24 | #3 of 24 · band A · Monte Carlo rank 4 (P10–P90 3–6) | A2 Deployer |

Evidence status follows the [catalog's classes](../role-catalog.md#12-status-classes-for-canonical-roles). The GenAI target order and the CCI rank answer different questions: the [target order](../genai-target-roles.md) is restricted to GenAI work; the [CCI rank](../role-rankings.md) scores the role as a whole career. The work footprint is judgement (Grade D) from the [role map](../role-map.md).

## The numbers

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| Demand | 7.5 (6.5–8.5) | M | Fast AI Jobs FDE cluster 1,007 open roles at 353 AI startups (2026-11-12, +29% vs late Jul 779); 260–1,276 across six boards (Plank 1,276, fdejobslist 391); caveat: 23/50 newest Fast AI Jobs rows are IC FDE titles, 22 adjacent strategist/GTM roles [T0-51, T0-70]. |
| Pay | 7 (6–7.75) | B | Levels.fyi US FDE TC (2026-09-08): P25 $172K / P50 $205K / P75 $277K / P90 $350K (above US AI Engineer); Google FDE median $292K; Fast AI Jobs startup posted base median $180,656 (n=164, range $75K–$375K); international FDE beats SWE (UK GBP 139.6K, CA CA$186.3K, NL EUR 135.5K) [T0-44, T0-51]. |
| Durability | 6.5 (5–8) | D | Judgement. Customer embedding and integration judgement; risk of drift into non-coding roles (about half the cluster is non-engineering) [T0-01 F3]. |
| Leverage | 8.5 (7.5–9.5) | D | Judgement. Converts deployments directly into revenue and retention. |

Scores use the anchored rubric in [role-rankings §1](../role-rankings.md#1-method-composite-career-index-cci); the composite (CCI) is a model output (Grade M). The same inputs, with every source, are in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs). Measured pay by title, city and level is in [pay benchmarks](../../09-compensation/pay-benchmarks.md).

**India lens:**

| Pillar | Score (0–10: mid, range) | Grade | Basis |
|---|---|:---:|---|
| India demand | 4.5 (3–6) | C | Indeed India / IANS (2026-10-14) reported ~19x (1,807% YoY) growth in India FDE postings from a low base; verified Bengaluru/Hyderabad hiring at Palantir-style AI vendors and labs [T0-25, T0-51]. |
| India pay | 5.5 (4–7.25) | D | No India FDE Levels.fyi title page; kept Grade D placeholder pending role-specific India TC data (top-end widened slightly to reflect Bengaluru product/lab offers) [T0-45, T0-51]. |

India rank (CCI with India inputs): #9 of 24.

## Who it suits

| Backend / Systems SWE | Data Scientist / BI | Frontend / Full-Stack | Non-Technical (5+ yrs domain) | PhD / Academic Researcher |
|:---:|:---:|:---:|:---:|:---:|
| ● 7.5 | ◐ 4.5 | ◐ 7 | ◐ 4 | ◐ 5 |

Access from each background (0–10): ● ≥7.5 is a high-volume corridor (about 6–8 months at 15–20 hours a week), ◐ 4–7.4 is plausible but extended, ○ below 4 is not plausible within 12 months. These timelines are model outputs (Grade D). The modelled time to a first offer by background is in [career transitions](../../11-tracks/career-transitions.md#modelled-months-to-a-first-offer); the best targets by background are in [GenAI target roles](../genai-target-roles.md#best-targets-by-background).

## What you need

- **Must (headline):** Python (production), APIs & integrations, LLM APIs & tool calling, RAG, Customer scoping & demos.
- **Important (headline):** Retrieval quality (hybrid, reranking, recall@k), OAuth/OIDC, RBAC, SSO, Agents & tool use, LLM evaluation (golden sets, calibrated judges, CI gates), Domain expertise, Stakeholder communication.
- **Full inventory:** 58 skills (Must 5 · Important 15 · Should 18 · Optional 20), each with its evidence and posting keywords: [forward-deployed-engineer.md](../../03-skills-and-tech/inventories/forward-deployed-engineer.md).
- **Prerequisites:** One JD: 2–6 years and up to 50% travel [B · T0-01]. Only ~48% of the cluster is engineer-titled, so target those titles
- **Credentials (tie-breakers, not skills):** AWS Certified Generative AI Developer – Professional (AIP-C01) (Optional: services channels); Microsoft AI-103 (Azure AI apps and agents) (Optional: Azure customers; replaces AI-102 (retired 2026-06-30); status provisional pending T0-28); Salesforce Certified Agentforce Specialist (Optional: ); Palantir AI Engineer Specialist (Optional: ). Whether one is worth it: [credential ROI](../../04-certifications/credential-roi.md).
- What to learn first and what to drop across roles: [skills radar](../../03-skills-and-tech/skills-radar.md); in what order: [learning roadmaps](../../03-skills-and-tech/learning-roadmaps.md).

## How to prove it

- **What the evidence asks for:** A customer pilot case study with numbers; a demo on real data shown to at least two potential users; a deployment write-up that covers failure modes
- **Project archetypes that cover the most of its Must and Important skills** (Grade M): [P1 Evaluated RAG system over a real corpus](../../05-portfolio/project-archetypes.md#p1) (48%); [P2 Reliable agent: approvals, sandboxed tools, replay, failure injection](../../05-portfolio/project-archetypes.md#p2) (37%); [P11 Customer pilot / reference architecture with a cost model](../../05-portfolio/project-archetypes.md#p11) (33%). One project rarely covers a role; the [job-search strategy](../../06-job-search/job-search-strategy.md#the-constraints-that-bind-first) computes the smallest sets that do.
- How verifiable the proof must be, and what to publish: [proof-of-work standards](../../05-portfolio/proof-of-work-standards.md).

## How you are interviewed

- **Track: Application plus customer scoping.** It tests Coding and debugging (often practical or production-adjacent), system architecture or decomposition (RAG, agents, enterprise integration, evals), and customer scoping, discovery or technical-presentation rounds. Source: T0-14, T0-46, T0-51, T0-53, T0-62.
- **Practise:** the [application plus customer scoping prep pack](../../08-interviewing/prep-packs.md#application-plus-customer-scoping-pack), plus the behavioural and coding packs.
- Classify the loop first, then prepare by round: [interview loops](../../08-interviewing/interview-loops.md).

## Résumé

- **Variant:** A2 Deployer (Applied GenAI Engineering); headline pattern: "Forward Deployed / Applied AI Engineer: customer-facing LLM systems". How to tailor it: [résumé strategy](../../06-job-search/resume-strategy.md).
- **Keywords to mirror, only when true:** forward deployed, FDE, customer-facing, deployment, integration, RAG, agents, travel
- **Leave out or reframe:** A pre-sales-only story with no production code; vague "AI solutions" claims without customer outcomes
- The concise skills section for this role: [résumé skills matrix](../../06-job-search/resume-skills-matrix.md#resume-forward-deployed-engineer).

## Related roles

- **Most similar by skill overlap** (weighted overlap of tiered headline skills, Grade M): [Applied AI Engineer](applied-ai-engineer.md) (0.43); [AI Engineer](ai-engineer.md) (0.40); [Agentic AI Engineer](agentic-ai-engineer.md) (0.31).
- **Same family (Forward Deployment & Solutions):** [AI / GenAI Solutions Architect](ai-solutions-architect.md).

## Go deeper

- [Catalog profile](../role-catalog.md#profile-forward-deployed-engineer): definition, demand, pay, who hires, entry routes, aliases and watch items.
- [Role rankings](../role-rankings.md#2-master-leaderboard-ic-roles): leaderboard, lenses and dossiers; scoring inputs in [Appendix A](../role-rankings.md#appendix-a-scoring-inputs).
- [GenAI target roles](../genai-target-roles.md#at-a-glance-the-sorted-target-list): where this role sits in the GenAI target order and why.
- [Skill map](../../03-skills-and-tech/role-skill-maps.md#skills-forward-deployed-engineer): narrative skills, tools, interview and typical gaps.

## Evidence and dates

- Pillar scores as of 2026-11-19; skills ontology as of 2026-11-19; tool and credential statuses are due for re-verification by 2027-02-17.
- The demand scores rest on posting counts (Fast AI Jobs 2026-11-12), which expire 31 days after they were counted (EGP-1.0 class V1), so this page is due for re-verification by 2026-12-13.
- The work footprint is judgement (Grade D, decision D-015); ranks, coverage and similarity are model outputs (Grade M).
<!-- END GENERATED -->

## What the role actually looks like

A genuine Forward Deployed Engineer is a software engineer embedded with customers who **writes, ships, and owns production code in the customer's environment** — increasingly LLM applications, agent workflows, and evaluation pipelines — and remains accountable for adoption after the initial demonstration [A/B · T0-51 L93, L148–L152]. Across the 28 text-based postings sampled in November 2026 (excerpt-weighted lower bounds), the top required capabilities are customer scoping (50.0%, 14/28), Python (42.9%, 12/28), LLM APIs (39.3%, 11/28), agents (35.7%, 10/28), customer communication (35.7%, 10/28), APIs/integrations (32.1%, 9/28), pragmatism under ambiguity (32.1%, 9/28), and evaluation (21.4%, 6/28) [M · T0-51 L90, L305–L324]. One company essay (PostHog, Grade C) puts the day-to-day split at 60–80% customer time with 20–50% travel [C · T0-51 L153].

**Role-defining operating constraints distinguish FDE from desk-bound engineering:**
- **Heavy travel and on-site presence:** Travel or customer-site work is stated in **13 of 28 (46.4%)** text-based postings — reaching 25–75% at Palantir Edge, 4–5 days a week on customer sites at Palantir Colorado Springs, 25–50% at Anthropic (COI), up to 50% at OpenAI Healthcare, and 40–50% at Growth Signals; only 5 of 42 sampled postings are remote [A/B/M · T0-51 L92, L275, L440].
- **Domain, clearance, and language verticals:** Active verticals span government and defence (Palantir US Government, Anduril, Scale AI Public Sector, Anthropic Federal Civilian), edge/tactical systems (Palantir Edge, WebAI), healthcare (OpenAI Healthcare with protected-health-information safeguards), legal (OpenAI Legal), voice and computer-use agents (PolyAI, Snorkel), and data platforms (Databricks) [A/B · T0-51 L474–L483]. Three of 28 postings require security-clearance eligibility (Palantir US-government/edge roles; Anthropic Federal Civilian notes clearance is a plus, not required), and European customer hubs impose local-language gates — Anthropic Paris requires native French and Munich native German alongside 8+ years' experience [A/B · T0-51 L92, L330, L440, L511].
- **Mid-level versus senior and staff scope:** Early-career and mid-level FDEs (new-graduate to ~4 years) embed on individual customer deployments, build integrations, and debug data/API pipelines [A/B · T0-51 L428–L430]. Senior and Staff FDEs (e.g., OpenAI Healthcare 6+ years, Anthropic Staff FDE) own multi-stakeholder enterprise architectures, lead advisory and architecture-review engagements, operationalise evaluation and human-review workflows, and channel recurring field gaps back to core product teams [A/B · T0-51 L456, L741, L760].

**Four-part screening test (judgement, Grade D, grounded in practitioner evidence [C · T0-51 L191–L196]):** Treat a posting as genuine FDE work only when it (1) writes and ships production code in the customer's environment, (2) owns outcomes beyond the demo, (3) is measured on deployment and adoption rather than sales quota or billable utilisation, and (4) feeds field learning back into the core product.

## Employer landscape and title confusion

**Funded AI startups dominate measurable volume, with heavy title noise.** Fast AI Jobs tracks **1,007 open FDE-cluster roles across 353 AI startups** as of 2026-11-11 — up **+29.3%** in 103 days from 779 roles across 288 startups on 2026-07-31 [B/M · T0-51 L85, L204–L207]. Because roles per startup rose only from 2.70 to 2.85, growth reflects more startups adopting the FDE label rather than massive individual teams; 63.0% sit at Series A–D and 37.2% at Pre-Seed to Series B, exposing the cluster to venture-funding cycles [M · T0-51 L85, L210, L544]. External growth multiples all show sharp expansion from small bases — Lightcast >1,000% (Jan–Aug 2026 vs 2025; broader tech +13%), Indeed US +729% (Apr 2026), and Indeed India ~19× (Jun 2026) — though each tracks a different definition, so no single multiple should be read as market size [B · T0-51 L86, L220–L231]. Meanwhile, **no live Big Tech FDE postings** were found at Microsoft, Google, AWS, or Salesforce (a Melbourne Salesforce Agentforce FDE closed on 2026-06-26) [T0-51 L78, L619].

**Nearly half of the headline FDE cluster is not FDE-titled engineering [M · T0-51 L87, L214–L215]:**

| Title slice in newest 50 Fast AI Jobs rows (2026-11-13) | Share | What it is and how to treat it |
|---|---|---|
| **FDE-titled engineer ICs** (*FDE*, *FDSE*, *Forward Deployed AI Engineer*) | **44%** (22/50) | Core engineering target (~440 indicative roles across the 1,007 cluster; ±14 pp) [M · T0-51 L214–L215] |
| **FDE engineering leadership** (*Manager FDE*, *Deployment Lead*, *Head of FDE*) | **10%** (5/50) | Combined engineer-titled + FDE leadership = **54%** (~540 indicative roles) [M · T0-51 L214–L215] |
| **Adjacent engineer titles** (*Deployment Engineer*, *Field Engineer*, *Forward Deployed Solutions Engineer*) | **18%** (9/50) | Screen every posting: pre-sales risk is high inside sales organisations [B/M · T0-51 L179–L180, L829] |
| **GTM Engineer** | **6%** (3/50) | Revenue-operations / go-to-market automation; not core FDE [M · T0-51 L181, L214] |
| **Non-engineering cluster titles** (*Deployment Strategist*, *Creative*, *Forward Deployed Banker*) | **22%** (11/50) | Non-coding titles riding FDE title arbitrage; exclude from engineering searches [B/M · T0-51 L87, L182] |

**Verified aliases and false-positive traps:**
- **Confirmed aliases to search:** `Forward Deployed Software Engineer (FDSE)`, `Forward Deployed AI Engineer`, `Forward Deployment Engineer` (Neuron7, Infosys), `Full-Stack Software Engineer (Forward Deployed)` (Scale AI), `Member of Technical Staff (Forward Deployed Engineer)` (Anthropic LCAs), `Member of Forward Deployed Staff (FDE)` (OpenAI LCAs), and `Frontier Agents Engineer (Forward Deployed Engineering / Applied AI)` at Scale AI (verified via T0-48 L530, T0-53 L439–L440, and live check on scale.com on 2026-11-19, correcting T0-51 L183's missed lookup) [A/B · T0-51 L171–L178; T0-53 L439].
- **Pre-sales and consulting rebrands:** Two FDE-labelled postings (Prodapt *Data and AI Presales* and SnapLogic filed under *Sales – Pre-Sales*) were pure pre-sales and excluded [B · T0-51 L93, L293]. Services firms span very different realities under the same label: Accenture states its role is "not a consulting role", Infosys specifies ~70–80% embedded implementation (5–12 years), and GlobalLogic's `Forward-Deployed AI Product Architect` asks 15+ years and executive-facing advisory [A/B · T0-51 L93, L192].
- **Overlap with Applied AI Engineer:** Anthropic places its US FDE roles inside the Applied AI team (`Forward Deployed Engineer, Applied AI`), and OpenAI runs parallel Applied AI and FDE tracks; see [Applied AI Engineer](applied-ai-engineer.md) for the sibling family [A · T0-51 L194; T0-53 L126].

## Career path, India demand and market signals

**Entry routes and experience bar.** Across 15 text-based postings stating minimum years, the median ask is **5 years** (range 1–15), with stated levels distributed evenly between entry/mid (13 of 30) and senior/staff (14 of 30; plus 3 manager) [M · T0-51 L91, L424, L468]. Degrees appear in only 8 of 28 postings (6 of 8 accept equivalent experience) and zero require a PhD [M · T0-51 L91, L420]. Three concrete routes appear in the postings:
1. **Early-career tracks:** New-graduate FDE programmes at Palantir (US Government, NY) and Chalk, plus 1–4-year Indian AI-native/product postings (Sarvam AI 1–3, Darwinbox 1–4, Zamp 2–5) [B · T0-51 L428–L429, L434].
2. **Mid-career backend or full-stack engineers:** 4+ years of customer-facing production engineering is the main corridor into frontier labs (Anthropic US 4+, OpenAI Healthcare 6+, Anthropic Europe 8+) [A/B · T0-51 L430, L435].
3. **Former technical founders:** Three of four Anthropic postings explicitly encourage technical founders to apply (COI) [A · T0-51 L436].

**Progression ladder and durability risk.** Postings confirm a clear ladder: Entry / New Grad → Mid / Senior → Staff FDE (Anthropic, Databricks) → Manager FDE / Deployment Lead (OpenAI Munich and Singapore, Accenture Senior Manager) → VP / Head of FDE (Snorkel AI) [A/B · T0-51 L95, L448–L455]. No empirical dataset tracks post-FDE exits (founder, PM, EM) [T0-51 L458]. The central career risk is **services drift** — roles where success degrades into billable utilisation, endless bespoke engagements, and customer learning that never reaches the core product [C · T0-51 L95, L460, L544].

**Pay split by employer tier.** Full benchmarks are owned by [pay benchmarks](../../09-compensation/pay-benchmarks.md) (D-019). The November 2026 dossier closes Phase 0's total-compensation and India gaps and shows that FDE pay splits sharply by employer tier:
- **US frontier labs (posted base + equity):** Anthropic posts **$280K–$320K** base across Applied AI and Staff FDE roles (COI; midpoint 1.66× the Fast AI Jobs median base), and OpenAI posts **$185K–$300K + equity** (Healthcare SF; SF mirror $180K–$280K) [A/B/M · T0-51 L88, L348–L352, L373].
- **Palantir and broad US AI-native market:** Broad dataset base medians cluster tightly at **$172K–$183K** (Fast AI Jobs median $180,656, n = 222; Indeed mean $171,911; Bloomberry/Paraform $173.8K–$183K C), while **Levels.fyi US FDE total compensation** sits at **P25 $172K / P50 $205K / P75 $277K / P90 $350K** (updated 2026-09-08) [B/C · T0-51 L88, L360, L363–L366]. Palantir posts **$135K–$200K** base (New Grad NY $135K–$145K), while its **Levels.fyi FDE TC median is $233K** (n = 232, updated 2026-10-23; SWE level row shows $175K base + $106K/yr stock + $6.6K bonus) [B · T0-51 L353–L355, L361–L362]. No systematic startup-FDE equity dataset was found, and Phase 0's unpublicised $188K-vs-$145K comparison and 0.4–0.8× equity factor could not be reproduced [T0-51 L378–L380]. No European FDE pay dataset exists [E · T0-51 L370].
- **US sponsorship:** Statements split across employers (4 Anthropic postings sponsor; Crisp and a Wellfound enterprise do not; 22 silent), while DOL-derived LCA filings confirm active H-1B sponsorship for FDE titles at Palantir (52 of 292 certified filings = 17.8%), OpenAI (≥7), and Anthropic (≥3; page-1 lower bounds) [A/B · T0-51 L92, L489–L500]. Contested H-1B fee litigation status is owned by [visa and relocation](../../11-tracks/visa-and-relocation.md).

**India demand and pay (newly evidenced).** Indeed India reported a nearly **19-fold (1,807%)** year-on-year surge in FDE postings in June 2026 vs June 2025 (live-verified 2026-11-19: accelerating from March 2026, moderating to ~16× in July and >6× in August 2026 across Bengaluru, Hyderabad, Chennai, Mumbai, and New Delhi) [B · T0-51 L89, L224]. Nine India postings entered the sample across AI-native/product employers (Sarvam AI, Zamp, Darwinbox, Neuron7, Resilinc, two Weekday clients) and IT-services firms (Infosys, GlobalLogic), spread evenly across entry (3), mid (3), and senior (3); no India GCC FDE posting surfaced [B/M · T0-51 L567–L571]. Newly observed India pay sits at **₹16.75L median TC on Levels.fyi** (INR 1,674,888 — page header displayed a US label with INR currency, corroborated by live check reporting ~₹17.5–17.7L median and ₹42L P75), **₹17.0L mean** on Glassdoor Bengaluru via a blog (C), and **₹25–40 LPA posted** for 5–7 years' experience (Weekday/Bayt, 2026-11-11) [B/C · T0-51 L89, L367–L369, L382].

**Credentials:** Zero of 28 postings require a certification; one (Infosys) lists cloud/AI certifications as preferred [B/M · T0-51 L96, L418]. Both AWS AIP-C01 (active; 75 questions, 180 min, $300, pass 750; independently read in T0-53 L473) and Microsoft AI-103 (live-verified GA in June 2026, updating T0-51 L416's stale beta extract) remain optional tie-breakers for cloud-services channels; see [credential ROI](../../04-certifications/credential-roi.md).

## Interview themes and preparation notes

Employer-published FDE interview documentation is thin: Palantir's getting-hired pages rendered titles only (*technical phone interview*, *working inside existing systems*, *analysing code efficiency*), and Anthropic publishes an all-role candidate AI-usage policy rather than stage lists [B · T0-51 L94, L390, L396; A · T0-53 L464]. Third-party guides and hiring-side essays (Grade C) converge on four assessed areas [C · T0-51 L94, L391–L398]:

1. **Open-ended decomposition / customer scoping (45–60 minutes):** The signature FDE round — starting from a vague enterprise goal to clarify stakeholders, users, KPIs, assumptions, risk sequencing, and failure modes across application, data, and ML layers [C · T0-51 L391, L393–L395].
2. **Practical coding:** Real-world data manipulation, messy inputs, APIs, rate-limiting/retries, or notebook-based coding rather than pure abstract puzzles [C · T0-51 L391, L393, L395].
3. **AI system design and productionisation:** Evaluation, governance, trust boundaries, prompt-versus-RAG-versus-fine-tuning trade-offs, and taking a prototype into production [C · T0-51 L391, L393].
4. **Past-project walkthrough and client judgement:** Defending an end-to-end shipped system, handling deployment delays, blocked customer security access, and stakeholder disagreement [C · T0-51 L391, L393, L395].

**Correction to the Databricks loop description.** Phase 0's card notes that the Databricks AI-FDE loop tests "RAG over sensitive, fast-changing documents and evaluating a multi-agent system". Falsification searching in T0-51 found no candidate report confirming those two specific prompts: sensitive-document RAG appeared only as a prep vendor's own practice exercises, and multi-agent evaluation appeared only in job-posting preferences [C · T0-51 L76, L400, L597].

**AI-usage rules and proof of work.** Anthropic's candidate AI guidance (live-verified 2026-11-19; read in T0-53 L464) encourages refining self-written application drafts and interview prep with AI, restricts take-homes to no AI unless stated, and prohibits AI in live interviews unless explicitly permitted [A · T0-53 L244; B · T0-51 L396]. On proof of work, employers and founders ask for shipped production builds and end-to-end walkthroughs of past customer problems; Phase 0's three specific portfolio artefacts (pilot case study with numbers, demo to ≥2 users, deployment failure-mode write-up) remain untested practice guidance (`[P]`) rather than employer-named prerequisites [C/D · T0-51 L402–L409]. Practise with the [application plus customer scoping prep pack](../../08-interviewing/prep-packs.md#application-plus-customer-scoping-pack) (no model answers).

## Dossier evidence and limits

- **Primary dossier:** [T0-51](../../../research/sessions/T0-51-role-dossier-forward-deployed-engineer.md) (retrieved 2026-11-13 to 2026-11-14; 44 sources: 8 Read, 35 Extract-only, 1 Blocked; 42 JD records: 28 text-based and 14 listing-level rows) [T0-51 L55, L679–L726].
- **Statistical and sampling limits:** Skill shares use n = 28 text-based records (**±18 percentage points**), of which **19 are short search/mirror excerpts**, making every share a strict lower bound [M · T0-51 L57, L69]. Consequently, T0-51's proposed demotion of `rag` and nine Important skills is **not** adopted without a larger full-text read (n ≥ 60). Big Tech (Microsoft, Google, AWS, Salesforce), European pay datasets, and Indian GCCs were unreached; independent liveness was not verified for excerpt-based rows [T0-51 L65, L611–L622].
- **Epistemic audit corrections applied:** (1) Four Extract-only ledger rows graded A in T0-51 (`S19`, `S20`, `S21`, `S24` — backing five Grade-A JSONL records) are downgraded to Grade B within T0-51 (with AIP-C01 and Anthropic guidance corroborated by full reads in T0-53 and AI-103 verified GA via live search on 2026-11-19); (2) Anthropic postings (`S22`, `S23`) and guidance (`S24`) are flagged COI because T0-51 was authored by Claude Sonnet 5.5 (Anthropic) without marking COI [T0-51 L13, L704–L706]; (3) T0-51's K8 verdict (L468–L470, L596) misread the repository's D-015 stack layers (`L6 plus L5`) as seniority bands L5/L6 — the stack-layer footprint itself stands; (4) untraced viral claims circulating online (FT 800% growth, $9B committed, 224 roles at 39 companies, 68% travel) are excluded as Grade E [T0-51 L79, L660].
- **What would change this view:** Full-text reads across ≥60 postings; direct Big Tech and Indian GCC counts; repeat tracking of Fast AI Jobs' engineer-titled share (falling below 35% across two 31-day reads would cut engineering demand); and verified European pay and startup equity datasets [T0-51 L104, L640–L645].

## Next steps

- [All role hubs](README.md) · [The role map](../role-map.md) · [Start Here](../../README.md)
