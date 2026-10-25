---
id: T0-01
title: "GenAI role taxonomy and live market volume: which titles clear a 50-posting quorum (Oct 2026)"
date: 2026-10-21
status: complete-with-gaps
topic: genai-role-taxonomy-market-volume
tags: [genai, job-titles, role-taxonomy, ai-engineer, forward-deployed-engineer, context-engineering, agent-architect, india-gcc, hiring-volume, evidence-graded]
informs_decisions:
  - Title architecture and leveling ladder for GenAI engineering roles
  - Which titles to publish externally versus map to an existing family
  - Quarantine register for speculative titles, with graduation tests
  - India GCC role design versus US/EU role design
confidence: "medium for tier assignments; low for any exact count on LinkedIn, Indeed, Wellfound, Otta or Ashby individually (none could be queried directly in this session)"
evidence_window: 2026-07-30 to 2026-10-21
---

# T0-01: GenAI role taxonomy and live market volume

**Bottom line.** Three title families clear the 50-posting quorum with room to spare: **AI Engineer**, **Machine Learning Engineer**, and **Forward Deployed Engineer (FDE, with aliases)**. "Applied AI Engineer" is very likely a large sub-node of AI Engineer but could not be counted separately. **Context Engineer, Agent Architect, Cognitive Architect and Prompt Wizard do not reach quorum** in any corpus I could reach; Cognitive Architect and Prompt Wizard have essentially no new-wave postings at all. The blog claim that "AI Engineer has split into Agent Architect and Context Engineer" is **not supported at title level**; the split is happening as *skills inside* AI Engineer postings (agentic AI is named in about 59% of them). Two caveats matter more than any number below: (1) none of the five named platforms can be queried exactly from here, so verdicts are corpus-relative; (2) raw platform search counts are badly inflated by fuzzy matching (Finding 6).

---

## Prior

Recorded before searching. All are recalled beliefs, so Grade D by rule.

| ID | Checkable proposition | Initial confidence | Grade |
|---|---|---|---|
| P1 | "AI Engineer" and "Machine Learning Engineer" each have well over 50 live postings; AI Engineer has overtaken ML Engineer on startup-oriented boards. | High | D |
| P2 | Context Engineer, Agent Architect, Cognitive Architect, Prompt Wizard are each under 50 live postings in aggregate; Prompt Wizard is about zero; standalone "Prompt Engineer" has declined from its 2023 peak. | High (Prompt Wizard), medium (others) | D |
| P3 | Forward Deployed Engineer, Applied AI Engineer and LLM post-training roles are all established (50+). | Medium | D |
| P4 | Most "AI Engineer" JDs emphasize API orchestration, RAG and agents over fine-tuning/RLHF; fine-tuning is named in under 20% of them. | Medium | D |
| P5 | India: large volume, but GCC titles skew to "GenAI Developer / AI-ML Engineer", broader scope, more junior, reporting through GCC engineering heads rather than a Chief AI Officer. | Low-medium | D |

---

## Research Question

**Decision:** Which GenAI engineering/technical titles have verifiable live hiring volume of at least 50 active postings in Q3/Q4 2026 (so they belong in the core taxonomy), and which are speculative and should be quarantined?

**Operational definitions used**
- *Live posting*: an active posting in a named corpus on the retrieval date (not a requisition; multi-location duplicates and ghost postings inflate it, see Risks).
- *Quorum*: 50+ distinct active postings for the exact title or a declared alias cluster. Precedent: Indeed's own "AI-labeled title" rule uses a 5-postings-per-quarter floor (S30), so 50 is a conservative bar.
- *Corpora (proxies for the five named platforms)*: JobsPipe (11.5M active postings, 30+ sources including LinkedIn, Indeed, Workday, Greenhouse, Lever, Ashby; S4); Fast AI Jobs (38,517 AI-startup postings pulled from company ATS pages such as Ashby/Greenhouse/Lever; S10); plus small keyword aggregators (Rise, devjobsscanner, Weekday) used only as corroboration.
- *Evidence grades*: **A** = primary dataset or live page I fetched directly, dated, reproducible. **B** = dated secondary/vendor page or search-cached snapshot with a URL. **C** = blog/news/small-corpus keyword count, partially corroborated. **D** = recalled, promotional, or unverified. Grades apply to the claim *as scoped*, not to the market truth beyond that scope.

---

## Key Findings

**F1 (A). AI Engineer is established and now outnumbers ML Engineer in both corpora.** JobsPipe shows 1,697 live US "AI Engineer" roles versus 1,084 US "Machine Learning Engineer" (ratio 1.57; global ML Engineer 2,157): https://jobspipe.dev/jobs/ai-engineer/usa.md and https://jobspipe.dev/jobs/machine-learning-engineer/usa.md. Fast AI Jobs (AI startups only, updated 2026-10-19) shows 326 AI Engineer roles across 183 startups versus 273 ML Engineer across 159 (ratio 1.19): https://www.fastaijobs.com/jobs/role/ai-engineer and https://www.fastaijobs.com/jobs/role/ml-engineer. LinkedIn's Jobs on the Rise 2026 ranks AI engineer #1 (B): https://digital-release.wgnradio.com/?p=2781179. *Scope warning:* the "AI Engineer" count is a family, not a GenAI-only count (F2).

**F2 (A). "AI Engineer" is a heterogeneous bucket.** Of the 50 newest rows on the Oct 19 Fast AI Jobs AI Engineer page (S8): 16 are "Applied AI Engineer" variants, 8 are Figure AI "Helix AI Engineer" robotics roles, 5 are agent-titled, 4 are FDE-flavored, 2 are "GTM AI Engineer". JobsPipe's US sample also includes "Physical AI Engineer" and "Site AI Engineer" (construction). The two employer mixes differ sharply: AI Engineer is led by Capital One (33), TCS (22), American Express (16), Deloitte (13), Infosys (12); ML Engineer is led by TikTok (74), Adobe (21), Apple (20), Capital One (20) (S1, S3). AI Engineer is enterprise/services-heavy; ML Engineer is Big Tech/recsys/AV-heavy.

**F3 (A). Forward Deployed Engineer is the largest new family, and it is alias-heavy.** Fast AI Jobs (updated 2026-10-20) lists 933 open FDE-cluster roles across 343 AI startups (Series C 184, Series A 176, Series G+ 147, Series B 119, Series D 110; 38% early-stage): https://www.fastaijobs.com/jobs/role/forward-deployed-engineer. That is up about 20% from 779 at 288 startups in the early-August cached snapshot, in line with AI Engineer (+18.5%) and ML Engineer (+20.3%) over a similar window. **Composition matters:** of the 50 newest rows (Oct 15-20), about 24 (48%) are engineer-titled (FDE, Deployment Engineer, "Frontier Agents Engineer (Forward Deployed Engineering)"); the rest are Deployment Strategists (6), Forward Deployed/Product Managers (6), managers and TPMs (6), GTM Engineers (4), plus a pre-sales field engineer, a "Forward-Deployed Banker" and a research role. Engineer-titled FDE volume is therefore roughly half of 933 if the sample is representative (an extrapolation), still far above quorum. Aliases seen across snapshots: "AI Deployment Engineer" and "Deployment Strategist" (OpenAI, Writer, Didero, ElevenLabs), "AI Engineer - FDE" (Databricks), "Applied AI Engineer" at some labs (S11, S35).

**F4 (A/B). The "split" is happening as skills inside AI Engineer postings, not as new titles.** In JobsPipe's AI Engineer JD measurement (counted 2026-09-10): Python 78.4%, LLM 76.7%, agentic AI 59.3%, RAG 54.0%, ML 39.8%, generative AI 37.6%, Azure and AWS 35.1% each, CI/CD 34.4%, vector databases 32.6%, prompt engineering 31.1% (https://jobspipe.dev/job-description/ai-engineer). Across all salaried postings (Sept 1-18), agentic AI (1.7%) already exceeds machine learning (1.5%) as a named skill (https://jobspipe.dev/blog/highest-paying-ai-jobs-september-2026.md). Agentic and context work are real; they are tags on one family so far.

**F5 (B/C). Context Engineer is real but tiny, and it is three different jobs under one title.** Dated exact-title postings: EY (Manager, Mar 4 2026; Senior, Jul 7 2026), Adobe "AI Context Engineer" (undated on the page I read; a promotional source says April 2026), a Flexa posting dated May 26 2026 whose URL slug indicates BT (mirrored on apna.co for Bengaluru), and a staffing "Data / Context Engineer" (S17-S20). Small aggregators show single digits to low tens (Rise: 7; devjobsscanner: about 5 exact plus variants; S21-S22). My union estimate is **roughly 10-25 live postings globally**, an estimate, not a measurement. JD archetypes diverge: EY wants semantic data engineering (ontologies, knowledge graphs); BT wants prompt/tool/memory/retrieval design for SDLC agents; the staffing role wants RAG/vector-store engineering. Gartner formally defines context engineering and advises appointing a context lead or team integrated with AI engineering and governance (A for existence: https://www.gartner.com/en/articles/context-engineering), but a discipline definition is not a title-volume signal. Second Talent's "fastest-rising title" and Medium's "$250-400k" claims carry no counts (D).

**F6 (B). Raw platform counts for speculative titles are false positives.** Indeed shows 921 "cognitive architect" jobs, ZipRecruiter 388, Glassdoor 339 (US), SimplyHired 1,000, yet the visible results are solutions, PLM, network and digital architects (https://www.indeed.com/q-cognitive-architect-jobs.html, https://www.ziprecruiter.com/Jobs/Cognitive-Architect, https://www.glassdoor.com/Job/cognitive-architect-jobs-SRCH_KO0,19.htm). The only true "Cognitive Architect" hit is a legacy IBM Watson-era posting (S26). A naive quorum test would have **wrongly passed** this title; exact-title filtering is mandatory.

**F7 (B/C). Agent Architect exists only in single digits; the enterprise cluster is "(Agentic) AI Architect".** Exact "AI Agent Architect"/"Agent Architect": about 2 (Virtual Vocations, Aug 2026; Protodigy, Jun 2026). "Agentic AI Architect"/"Agentic Architect"/"Principal AI Architect - Agentic": at least 5 (Cognizant, Air India Gurugram, Zoom, Virtual Vocations; S24-S25). Required experience is incoherent across them (3-5, 6-10, 7+, 8+ years), a sign the title has no settled ladder.

**F8 (B/C). Prompt Wizard: null. Prompt Engineer: legacy and thin.** Exact-string searches for "Prompt Wizard" returned no job postings (null result, 2026-10-21). Indeed's Prompt Engineer page rests on 52 salary datapoints over 36 months (updated Aug 16 2026; https://www.indeed.com/career/prompt-engineer), consistent with fewer than 50 live roles. A "40% decline since 2023" figure circulates (Recrew) with no traceable source (D).

**F9 (C). LLM post-training is not a quorum-level exact title in accessible corpora; this contradicts the brief's "established" label.** Rise keyword counts (small corpus, undated cache): post-training 9, RLHF 17, RL 9, SFT 4, GRPO 2 (https://joinrise.co/jobs/k/post-training, /rlhf, /rl). Post-training work is mostly carried under "Research Engineer" or "Member of Technical Staff" at labs and data vendors (Cohere, Mercor, MLabs; Reflection AI posts "Forward Deployed Engineer, Lead - LLM Post-training"). Real demand is not disproven; the *title string* is. Research Engineer/Scientist counts were not measured.

**F10 (A/B). India has the highest AI-title intensity and a younger AI-role profile, but a smaller absolute AI Engineer count than the US.** AI-titled roles are 3.0% of India postings versus 1.3% US, 1.7% UK, 1.6% Germany, 0.9% France; entry-level share of AI roles is 21.2% India versus 10.4% US (JobsPipe, 2026-10-11; https://jobspipe.dev/blog/ai-jobs-entry-level.md). Live "AI Engineer" count: India 398 versus US 1,697 (0.23x; https://jobspipe.dev/jobs/ai-engineer/india.md), though the Sept JD page implies India at about 0.49x of US share (13.6% vs 27.9%); the two JobsPipe figures disagree and I flag that rather than reconcile it. Keyword-based Indeed AI Tracker, 2026-09-30: US 7.34%, UK 9.92%, Germany 5.74%, France 4.53%, Canada 18.97%; **India is not in that dataset** (A: https://github.com/hiring-lab/ai-tracker). GCC context: 2,100+ centres, AI/data the fastest-growing function (+38% YoY), supply gaps of 18-43% in AI/MLOps/platform clusters (C: S32).

**F11 (C). Title inflation is measurable, and practitioners expect collapse into AI Engineer.** Indeed's count of frequently advertised AI-referencing titles rose from 264 (2022) to 822 (Q1 2026) per press coverage of an Indeed analysis (https://www.pymnts.com/?p=3961580). A practitioner CTO guide argues most titles reduce to three jobs (build on APIs, train/fine-tune, keep the plumbing running) and lists "Context Engineer (at consulting shops)" among theater titles (https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/). Both are Grade C; the second includes an unverified claim about Cognizant.

**F12 (C/D). Reporting-line evidence is the weakest part of this study.** No JD-level "reports to" statistics were found. Survey-level signals only: hub-and-spoke is the preferred AI operating model for about two thirds of senior respondents in one leader survey (https://welovesalt.com/wp-content/uploads/2026/07/AI-Leadership-Pulse-Report_Salt-Solutions-Group.pdf); IBM-reported findings link hub-and-spoke or centralized models to higher ROI and report 76% of firms with a Chief AI Officer in 2026 (secondary: https://www.peoplematters.in/amp/news/ai-and-emerging-tech/76percent-of-firms-now-have-a-chief-ai-officer-up-from-26percent-in-a-year-ibm-49550). Per-title reporting lines in Detailed Findings are **inferences from team labels in JDs**, not measurements.

---

## Recommendation

1. **Adopt three core nodes:** AI Engineer (family, with level and domain modifiers), Machine Learning Engineer, Forward Deployed Engineer (family; alias map: AI Deployment Engineer/Strategist, FDSE, "AI Engineer - FDE").
2. **Adopt "Applied AI Engineer" as a provisional sub-node of AI Engineer** (customer/solutions-facing at OpenAI, Anthropic, Scale), pending an isolated count.
3. **Keep Tier-2 titles as skill tags or sub-specializations, not title nodes, until counted:** Agentic AI Engineer, GenAI Engineer/Developer (India alias), ML Platform/MLOps/LLMOps, Inference Engineer, AI Evaluation Engineer, AI/Agentic Architect, Research Engineer/MTS (post-training).
4. **Quarantine:** Cognitive Architect, Prompt Wizard, Agent Architect (exact), Context Engineer (watchlist), Context Architect variants, Context Harness Engineer, Principal Agentic Context Engineer, Vibe Engineer. Treat Prompt Engineer as legacy and map it to AI Engineer.
5. **Do not publish quarantined titles externally.** If a team does the work, label it with a skill tag ("context/retrieval design", "agent orchestration") on an AI Engineer posting.
6. **Re-run the counts on 2026-12-01 and 2027-01-15** using the protocol in D10, with the graduation tests in D5.

**What would change this recommendation:** a direct exact-title count of 50+ distinct requisitions for Context Engineer or Agent Architect from LinkedIn/Indeed/Ashby; or evidence that the engineer-titled share of the FDE cluster (about half in the Oct 20 sample) is much lower than sampled.

---

## Alternatives Considered

| Alternative | Why not adopted |
|---|---|
| Adopt the "10 titles worth hiring for" lists from industry blogs | They are opinion, not volume; several named titles failed the quorum or had no counts (F5-F8, F11). |
| Trust raw platform search counts | Fuzzy matching produced 339-1,000 "Cognitive Architect" hits where exact matches are about zero (F6). |
| Skills-only taxonomy (no titles) | Closest to the data (F4), but hiring ladders, comp bands and candidate search still run on title strings. Partly adopted via skill tags. |
| Use candidate-prep or survey data as a proxy for demand | Dataford's prep counts (FDE 229, GenAI Engineer 215, Agentic AI Engineer 125) are demand-side signals, not postings (C: S31). Used as corroboration only. |
| Declare the study blocked until the five platforms are queried directly | Their exact-title search is unavailable here; dual-corpus proxies (one LinkedIn/Indeed/ATS aggregate, one ATS-direct board) give a defensible first verdict. |

---

## Detailed Findings

### D1. Method and what could not be done
- **Could not query directly:** LinkedIn (login-gated), Indeed (public API retired per vendor description S36; search pages fuzzy), Wellfound (vendor reports API gone and site behind a bot challenge, S36), Otta/Welcome to the Jungle (not accessed), Ashby (only per-company boards; reached through links on Fast AI Jobs).
- **Proxies:** JobsPipe pages give exact-canonical-title counts, with LinkedIn job-view URLs in the samples. Fast AI Jobs gives role-cluster counts with direct ATS links (Ashby, Greenhouse, Lever).
- **Direct primary data used:** Indeed Hiring Lab AI Tracker CSV (downloaded 2026-10-21, series through 2026-09-30).
- **Series revision note:** the CSV shows 4.44% for US on 2025-12-31 while Hiring Lab's January blog cited a 4.2% high; secondary sites quote 6.28% for 2026-07-31 versus 6.39% in the CSV. Treat tracker values as about +/-0.3pp.
- **Community strategy only partly executed:** one adversarial query returned practitioner blogs, not Hacker News/Reddit/Latent Space threads. Treat the community leg as not done.

### D2. Volume versus 50-posting quorum

| # | Title (as searched) | Best observed live count (corpus, as-of) | Corroboration | Verdict | Grade |
|---|---|---|---|---|---|
| 1 | AI Engineer | US 1,697; India 398 (JobsPipe, Oct 21); 326 at 183 AI startups (Fast AI Jobs, Oct 19) | Weekday 3,130 blended "AI & AI Engineer" (Oct 9, India-heavy); Lensa 5,573 (undated, fuzzy) | **PASS, core** | A |
| 2 | Machine Learning Engineer | US 1,084; global 2,157; India 90; UK 108; Canada 60 (JobsPipe); 273 at 159 startups (Fast AI Jobs, Oct 19) | - | **PASS, core** | A |
| 3 | Forward Deployed Engineer (+aliases) | 933 at 343 AI startups (Fast AI Jobs, Oct 20); about half engineer-titled in newest 50. Earlier cached: 779 at 288 (~Aug 3); SF 172, NY 133, Remote 65 | Dataford prep 229; lab usage (OpenAI, Databricks, Scale) | **PASS, core (alias-heavy)** | A |
| 4 | Applied AI Engineer | Not isolated; 16 of newest 50 AI-cluster rows (Oct 19). If representative, about 100 of 326 (unverified extrapolation) | OpenAI, Anthropic, Scale, Edison, PhaseV | **LIKELY PASS, sub-node** | C |
| 5 | Agentic AI Engineer / AI Agent Engineer | Not isolated; about 5 of newest 50 | PepsiCo, Fractal, Cato; skill in 59.3% of AI Eng JDs; prep 125 | Watchlist, skill tag | C |
| 6 | GenAI / Generative AI Engineer or Developer | Not isolated | Quest Global, Genia, Danta; top GCC label (Taggd); prep 215 | Alias of AI Engineer | C |
| 7 | LLM Engineer | Not isolated | Evlo AI "LLM / GenAI Engineer" | Unmeasured | D |
| 8 | ML Platform / MLOps / LLMOps | Not isolated; Preply posts 2 roles x 3 cities (6 postings) | GCC MLOps supply gap 18-43% (Quess) | Probable, count missing | C |
| 9 | Inference / ML Infra Engineer | Rise "inference engineer" 28 (small corpus) | Physical Intelligence "ML Infra Engineer, Platform" | Probable, unmeasured at scale | C |
| 10 | Post-Training / RLHF / RL Engineer | Rise: 9 / 17 / 9 (small corpus) | Carried under "Research Engineer"/MTS | **Below quorum as exact title** | C |
| 11 | Research Engineer / Scientist / MTS | Not measured | MTS wrapper at Edison, Context AI | Unmeasured | - |
| 12 | Applied Scientist | 14 at 12 AI startups (Fast AI Jobs, Jun 9) | Big-Tech-heavy title absent from corpus | Below in startup corpus; Big Tech unmeasured | B |
| 13 | AI / Agentic / GenAI Architect | Not measured; 6+ distinct postings seen | Cognizant, Air India, Zoom, Korn Ferry | Probable, services-concentrated | C |
| 14 | AI Evaluation / Evals Engineer | Rise "LLM evaluation" 26 | FurtherAI "Evals & Model Quality" | Probable as skill/team | C |
| 15 | Prompt Engineer | 52 salary datapoints / 36 months (Indeed) | Coursera: only a handful in titles | **Below; legacy** | B |
| 16 | Context Engineer | Estimate 10-25 live | EY, Adobe, BT, staffing; Rise 7 | **Below; quarantine/watchlist** | C |
| 17 | Agent Architect (exact) | About 2 | "Agentic AI Architect" 5+ | **Below; quarantine** | C |
| 18 | Cognitive Architect | About 0 new-wave; 1 legacy IBM | Raw counts 339-1,000 are fuzzy | **Null; quarantine** | B |
| 19 | Prompt Wizard | 0 | - | **Null; quarantine** | B |
| 20 | Context / Enterprise Context / AI Context Architect | About 2-3 | devjobsscanner lists | Quarantine | C |
| 21 | Context Harness Engineer | One aggregator shows 39 "positions" (likely fuzzy) | - | Quarantine, unverified | D |
| 22 | Vibe Engineer | Not searched | Called "theater" in one blog | Quarantine, unverified | D |

Fast AI Jobs and JobsPipe count *postings*. Where one employer posts the same role in several cities (Preply, Databricks FDE), requisition-level counts are lower.

### D3. Skills, seniority and reporting lines (mapped to real JDs)

| Title | Primary skills seen in JDs | Seniority signal | Reporting line (inference, Grade C/D) |
|---|---|---|---|
| AI Engineer | Python, LLM APIs, agent orchestration, RAG + vector DBs, cloud, CI/CD, prompt design (S5) | Senior 24.6%, entry 7.0%, mid 6.0%, lead/manager 5.6% of postings; AI-titled roles entry-level 10.4% US, 21.2% India (S5, S6) | Product engineering or a central AI platform "hub" with embedded "spokes"; "Head/Director/Manager of AI Engineering" posts exist (Teradata, Front, Harrington Starr) |
| ML Engineer | Training/inference systems, PyTorch, recsys/ads/AV; LLM eval and fine-tuning appear in newer JDs | JobsPipe facets: senior 814, lead 359, entry 240 of 2,157 (about 38% / 17% / 11%) | ML or data-science org inside product engineering |
| Forward Deployed Engineer | End-to-end deployments at customer sites, agent/LLM integration, vertical depth (Databricks splits by manufacturing, public sector, financial services, retail); 2-6 yrs and up to 50% travel in one JD | Title-signaled: lead 25, staff 18, entry 5 (Jun snapshots) | Own "Forward Deployed Engineering" or "Client Solutions" department at some firms; elsewhere GTM/solutions. Leadership titles: Director FDE & AI GTM (Aircall), FDE Lead (n8n) |
| Applied AI Engineer | LLM application delivery for customers, evals, safety in regulated settings (Anthropic "Beneficial Deployments"; OpenAI "Startups", "Digital Natives") | Mostly mid-senior | Applied/customer engineering org at labs |
| ML Platform / MLOps | Feature pipelines, distributed training, low-latency inference, observability | Mid-senior | Platform engineering/infra |
| AI Architect (agentic) | Python, LangGraph/CrewAI/AutoGen, MCP, RAG, governance, enterprise integration (ERP/CRM/APIs) | 3-5 to 8+ yrs; inconsistent | Architecture/CTO office alongside AI, data and platform teams |
| Context Engineer (EY) | Data pipelines, ontologies, taxonomies, knowledge graphs for agentic AI | Senior, Manager | Consulting "AI & Data" practice |
| Context Engineer (Flexa/apna posting; slug indicates BT) | System prompts, tool definitions, memory, retrieval for SDLC agents | Not stated | Software engineering/SDLC tooling |
| Context Engineer (Adobe) | Context templates, memory compression, cost/latency | Not stated | Digital Employee Experience (internal IT) |

### D4. Quarantine dossiers

| Title | Evidence | Why quarantined | Gap to graduation |
|---|---|---|---|
| Cognitive Architect | Legacy IBM Watson-era title; platform counts are fuzzy artifacts | No new-wave postings; old meaning | Not plausible without a new, consistent JD signature |
| Prompt Wizard | No postings found | Marketing coinage | Any distinct postings at all |
| Agent Architect | About 2 exact; inconsistent seniority | Alias of AI/Solutions Architect | 50+ requisitions; stable ladder |
| Context Engineer | 10-25 est.; three JD archetypes | Below quorum; no stable skill signature; mostly consulting/staffing | See D5 tests 1-3 |
| Context / Enterprise Context / AI Context Architect | 2-3 listings | Variant of the above | Same |
| Context Harness Engineer | Single aggregator count, likely fuzzy | Unverified | Exact-title verification |
| Principal Agentic Context Engineer | Cited as "real" by one blog; not verified | Unverified | Exact-title verification |
| Vibe Engineer | Blog-labelled theater; name disputed per same blog | Workflow, not a role | Postings plus stable duties |
| Prompt Engineer (legacy) | Thin demand; absorbed into AI Engineer | Declining | Reverse trend unlikely |

### D5. Graduation criteria (quarantined to verified)
1. **Volume:** 50+ *distinct requisitions* (multi-location duplicates collapsed) for the exact title or declared alias cluster, in two independent corpora, one ATS-direct (Ashby/Greenhouse/Lever).
2. **Persistence:** the threshold holds on two counts at least 30 days apart.
3. **Breadth:** at least 10 employers; no single employer above 30%; at least 3 outside consulting and staffing firms.
4. **Skill signature:** 70%+ of postings share at least 3 core skills, and the cluster differs from AI Engineer by at least 2 core skills (JobsPipe `skills_or` shares).
5. **Ladder:** at least 3 distinct seniority levels with distinct pay bands.
6. **Lab adoption:** at least one tier-1 AI lab or Big Tech employer uses it as a formal role family.
7. **Alias test:** if substituting "AI Engineer" or "Solutions Architect" leaves the JD materially unchanged, it is an alias and fails.

Status today for Context Engineer: fails 1, 2, 3 (consulting-heavy), 4 (three archetypes); tests 5-6 unmeasured.

### D6. JD reality check (domain probes DP2 and DP4)
- **DP2, wrapper developers or systems engineers?** The measured JD signature is software-engineering-led: Python, LLM APIs, agent frameworks, RAG, cloud and CI/CD dominate. Evaluation and infra competencies are not in the top 12 skills, though they appear in specific JDs (Evals at FurtherAI; observability at GCCs). One-quarter of AI Engineer postings come from employers with 1,000+ staff (28.4%). Verdict: mostly full-stack/backend engineers with LLM orchestration; eval/infra-heavy variants are a minority (C).
- **DP4, fine-tuning/RLHF versus orchestration/RAG:** RAG is named in 54.0% and agentic AI in 59.3% of AI Engineer JDs; fine-tuning does not appear in the top 12, so its share is below 31.1%, exact share unmeasured. Among all salaried postings, RAG 0.4% versus PyTorch 0.3% (weak training proxy). Fine-tuning/RL concentrates at labs and data vendors (F9). My prior of "under 20%" is neither confirmed nor refuted. To measure: JobsPipe `skills_or` for fine-tuning versus RAG on `job_title_or: ["ai engineer"]`.

### D7. Tier-1 naming observed (DP3)
Observed in live postings (Oct 2026): OpenAI "Applied AI Engineer" (Startups, Digital Natives, Codex), "Partner Applied AI Engineer", and (Jul) "AI Deployment Engineer" plus "Manager, Forward Deployed Engineer"; Anthropic "Applied AI Engineer" (Beneficial Deployments, Startups, Enterprise Tech); Databricks "AI Engineer - FDE" across many countries and a "Senior Staff Applied AI Engineer - Context Retrieval"; Scale "Applied AI Engineer, Global Public Sector". Three frontier firms supply 13 of the newest 50 AI-cluster rows. **Not found:** any dated announcement of a title being formally created or deprecated; naming conventions are inferred from postings, not from HR changelogs. Meta FAIR and Google DeepMind were not sampled.

### D8. India and GCC versus US/EU

| Metric | India | US | UK | Germany | France | Source |
|---|---|---|---|---|---|---|
| AI-titled share of postings (title-based) | 3.0% | 1.3% | 1.7% | 1.6% | 0.9% | JobsPipe, 2026-10-11 |
| Entry-level share of AI roles | 21.2% | 10.4% | 11.0% | 18.8% | 21.2% | same |
| Live "AI Engineer" count | 398 | 1,697 | n/a | n/a | n/a | JobsPipe, Oct 21 |
| Share of AI Engineer postings by country | 13.6% | 27.9% | 7.2% | 9.1% | 5.4% | JobsPipe JD, Sep 10 |
| Indeed AI keyword share (2026-09-30) | not covered | 7.34% | 9.92% | 5.74% | 4.53% | Indeed AI Tracker |

- India-centric board Weekday lists 2,527 India versus 490 US AI roles (Oct 9-10); this reflects the board's audience, not the market.
- **Titles:** GCC AI hiring leans on GenAI Engineer, AI/ML Engineer, MLOps Engineer, Prompt Engineer (Taggd, C); Agentic AI Engineer, Principal Agentic AI Engineer and Forward Deployed AI Engineer appear on Weekday India listings. **"GCC AI Specialist" was not found as a title.**
- **GCC volume:** NASSCOM-Zinnov 2026 puts GCCs at 2,100+ centres and 2.3M staff; AI/data/analytics is the fastest-growing function (+38%); about two in three new GCC roles need AI/data/automation skills; 56% of GCC hiring is 4-10 years' experience (C: S32). **Title-level GCC posting counts were not obtained.**
- Scope difference (inference): GCC JDs bundle GenAI delivery, MLOps and governance more often; US JDs split applied (customer-facing) from platform. Not directly measured.

### D9. Tool catalog

| Tool | Gives | Access this session |
|---|---|---|
| Indeed Hiring Lab AI Tracker | Daily AI/GenAI posting shares, 9 countries, CC BY 4.0 | **Used** (CSV) |
| JobsPipe API/pages/Pulse CSV | Exact-title counts, JD skill shares, 30+ sources | Pages used; API not called (vendor) |
| Fast AI Jobs | AI-startup role clusters, direct ATS links | **Used** |
| Rise, devjobsscanner, Weekday, StartupHub, Lensa | Keyword/title lists; small or biased corpora | Corroboration only |
| Lightcast Job Postings/Skills APIs | Licensed postings analytics | Not accessed (vendor says free Skills tier is nonprofit-only since Apr 2026, S36) |
| LinkedIn Talent Insights / Economic Graph | Jobs on the Rise; talent data | Secondary only |
| Wellfound, Otta (Welcome to the Jungle), Levels.fyi, Hired, Layoffs.fyi | Startup roles, comp, layoffs | **Not accessed** |
| Ashby / Greenhouse public boards | Per-company listings | Reached via links only |
| Coresignal, TheirStack, Revelio Labs, Textkernel | Commercial postings/workforce data | Named by vendor pages, not used |

### D10. Reproduction protocol
- JobsPipe: `POST https://api.jobspipe.dev/v1/jobs/search` with `{"job_title_or":["context engineer"],"status":"active","limit":25}`; repeat per title; use `skills_or` for skill shares.
- Fast AI Jobs: read the "There are currently N open ..." line at `https://www.fastaijobs.com/jobs/role/<slug>`; slugs seen: ai-engineer, ml-engineer, forward-deployed-engineer, applied-scientist.
- Indeed tracker: `https://raw.githubusercontent.com/hiring-lab/ai-tracker/main/AI_posting.csv`.
- Always inspect the first 20 results for exact-title match before accepting a count.

---

## Open Questions & Risks

**DONE-criteria scorecard**

| Criterion | Status |
|---|---|
| 15+ titles measured against the 50 quorum with sources | **Partial.** 19 titles have some numeric observation, but only 4 (AI Engineer, ML Engineer, FDE, Applied Scientist) rest on exact-title counts in large corpora; the rest are small-corpus, estimated or null. |
| 5+ speculative titles quarantined with rationale | **Met** (9 listed in D4; some rest on thin evidence). |
| Skills/seniority mapped to real JDs for verified roles | **Partial.** AI Engineer measured; ML Engineer and FDE qualitative. |
| Graduation criteria defined | **Met** (D5). |
| India titling and GCC volumes benchmarked | **Partial.** Titles and shares done; GCC title-level counts missing. |

**Strongest objections an expert would raise**
1. *"You never queried the five named platforms."* True. Evidence for mitigation: JobsPipe aggregates LinkedIn/Indeed/Ashby postings and Fast AI Jobs links straight to Ashby/Greenhouse. Evidence against: both are third-party and normalize titles. Residual risk: moderate.
2. *"Posting counts are not demand."* Supported: one vendor reports 9.5% of active postings visible 45+ days (https://jobspipe.dev/blog/ghost-job-index.md, description only, C); Preply's 6 postings are 2 roles; mass posters (TikTok 74 of 1,084 US ML roles) skew counts.
3. *"The AI Engineer count is a family count."* Supported (F2): robotics, construction and Power Platform variants are included, so GenAI-specific volume is lower than 1,697 or 326.
4. *"Absence of evidence for Context/Agent Architect reflects crawl lag."* Plausible: first dated postings appear Mar-May 2026, so these titles are young. Mitigation: five independent sources agree on small counts; re-run on 2026-12-01.
5. *"Frontier-lab roles hide behind MTS/Research Engineer."* Agreed; post-training demand may be real while the exact title is not (F9).
6. *"Vendor bias."* JobsPipe sells data and Fast AI Jobs is a board; mitigated by grading and by using the Indeed CSV as an independent primary anchor.
7. *"Quorum of 50 ignores corpus size."* Fair: 50 is 0.13% of Fast AI Jobs but a rounding error in JobsPipe. Consider a share-of-corpus floor next session.

**Other open items:** direct LinkedIn/Indeed/Wellfound/Otta counts; October refresh of Applied Scientist (still a Jun 9 snapshot); isolated Applied AI Engineer, LLM Engineer, MLOps, Research Engineer counts; reporting-line statistics from JDs; GCC title counts; Meta FAIR/DeepMind naming; HN/Reddit/Latent Space primary threads.

---

## Delta

| Prior | Before | After | Direction | Evidence |
|---|---|---|---|---|
| P1 | AI Eng and ML Eng both 50+; AI Eng leads on startup boards | Confirmed, and AI Eng also leads in the broad corpus (1.57x US) | Confirmed, strengthened | S1, S3, S8, S9 |
| P2 | All four speculative titles under 50 | Cognitive Architect (about 0) and Prompt Wizard (0) confirmed; Agent Architect about 2; **Context Engineer larger than assumed (10-25) but still under 50**, with dated postings since Mar 2026 | Mostly confirmed; Context Engineer upgraded to watchlist | S17-S26 |
| P2b | Prompt Engineer declined | Direction plausible (thin Indeed data) but the "-40%" figure is untraceable | Unquantified | S28, S29 |
| P3 | FDE, Applied AI Eng and post-training all established | FDE confirmed and larger than expected (933 on Oct 20, about half engineer-titled); Applied AI Eng likely; **post-training exact title contradicted** at small-corpus level | Split | S11, S8, S22 |
| P4 | Fine-tuning under 20% of AI Eng JDs | Orchestration/RAG/agents dominate; fine-tuning below 31% (unmeasured exactly) | Directionally confirmed | S5, S7 |
| P5 | India large volume, GenAI Developer titles, junior, GCC reporting | India has highest AI-title share (3.0%) and juniors (21.2%); live AI Engineer count is 0.23-0.49x US; "GCC AI Specialist" not found; reporting lines unevidenced | Partly confirmed | S6, S2, S32 |
| New | - | Raw platform counts for exotic titles are false positives | New finding | S26 |

---

## Sources & Evidence Ledger

Retrieval date for all fetched pages: 2026-10-21 unless stated. "Cached" means seen via search result only.

| ID | Source | URL | As-of | Supports | Grade |
|---|---|---|---|---|---|
| S1 | JobsPipe, AI Engineer US | https://jobspipe.dev/jobs/ai-engineer/usa.md | Oct 21 (corpus Oct 19) | F1, F2, D2 | A |
| S2 | JobsPipe, AI Engineer India | https://jobspipe.dev/jobs/ai-engineer/india.md | Oct 21 | F10, D8 | A |
| S3 | JobsPipe, ML Engineer US and global | https://jobspipe.dev/jobs/machine-learning-engineer/usa.md ; https://jobspipe.dev/jobs/machine-learning-engineer | Oct 21 | F1, F2, D3 | A |
| S4 | JobsPipe corpus statement (llms.txt) | https://jobspipe.dev/llms.txt?src=md-twin | Oct 19 | Corpus size and sources (vendor claim) | B |
| S5 | JobsPipe AI Engineer JD measurement | https://jobspipe.dev/job-description/ai-engineer | counted Sep 10 | F4, D3, D6 | A |
| S6 | JobsPipe AI jobs and entry-level | https://jobspipe.dev/blog/ai-jobs-entry-level.md | Oct 11 | F10, D8 | B |
| S7 | JobsPipe highest-paying AI jobs (skill shares) | https://jobspipe.dev/blog/highest-paying-ai-jobs-september-2026.md | Sep 1-18 | F4, D6 | B |
| S8 | Fast AI Jobs, AI Engineer | https://www.fastaijobs.com/jobs/role/ai-engineer | Oct 19 | F1, F2 | A |
| S9 | Fast AI Jobs, ML Engineer | https://www.fastaijobs.com/jobs/role/ml-engineer | Oct 19 | F1 | A |
| S10 | Fast AI Jobs index (38,517 jobs) | https://www.fastaijobs.com/jobs | Oct 19 | Corpus size | A |
| S11 | Fast AI Jobs, FDE (fetched Oct 20; stage and city splits from an earlier cached snapshot to ~Aug 3) | https://www.fastaijobs.com/jobs/role/forward-deployed-engineer ; /jobs/stage/series-d-plus/forward-deployed-engineer ; /jobs/role/forward-deployed-engineer/san-francisco | Oct 20 (fetched); ~Aug 3 (cached) | F3 | A / B |
| S12 | Fast AI Jobs, Applied Scientist (cached) | https://www.fastaijobs.com/jobs/role/applied-scientist | Jun 9 | D2 row 12 | B |
| S13 | Indeed Hiring Lab AI Tracker | https://github.com/hiring-lab/ai-tracker (AI_posting.csv) | through Sep 30 | F10, D8 | A |
| S14 | Hiring Lab January 2026 update | https://www.hiringlab.org/2026/01/22/january-labor-market-update-jobs-mentioning-ai-are-growing-amid-broader-hiring-weakness | Jan 22 | Series context | B |
| S15 | LinkedIn Jobs on the Rise 2026 (via NewsNation/WGN) | https://digital-release.wgnradio.com/?p=2781179 | Jan 2026 | F1 | B |
| S16 | Gartner, Context Engineering | https://www.gartner.com/en/articles/context-engineering (read via https://gcom.pdo.aws.gartner.com/en/articles/context-engineering) | 2026 | F5 | A (existence) |
| S17 | EY Context Engineer postings | https://careers.ey.com/ey/job/New-York-Context-Engineer-Senior-Consulting-Location-OPEN-NY-10001-8604/1412469633/ ; https://careers.ey.com/ey/job/New-York-Context-Engineer-Manager-Consulting-Location-OPEN-NY-10001-8604/1370274733 | Jul 7; Mar 4 | F5, D3 | A |
| S18 | Adobe AI Context Engineer | https://www.hirebase.org/company/adobe/jobs/ai-context-engineer-59b3d526 | 2026 | F5 | B |
| S19 | BT Context Engineer | https://flexa.careers/jobs/bt-context-engineer-6a15525c487ddf2ecc375d54 ; https://apna.co/job/1553317027 | May 26 | F5 | B |
| S20 | Staffing "Data / Context Engineer" | https://www.monster.com/job-openings/data-context-engineer-texas-township-il--0447710c-7f60-4338-a1da-a9235dc9560a | 2026 | F5 | B |
| S21 | devjobsscanner (LinkedIn-sourced titles) | https://www.devjobsscanner.com/company/contexte/ | cached | F5 | C |
| S22 | Rise keyword pages | https://joinrise.co/jobs/k/context-engineering ; /post-training ; /rlhf ; /rl ; /sft ; /grpo ; /inference-engineer ; /llm-evaluation | cached, undated | F5, F9, D2 | C |
| S23 | Second Talent, Context Engineer | https://www.secondtalent.com/occupations/context-engineer/ | 2026 | Hype claims only | D |
| S24 | Agent/Agentic architect postings | https://www.virtualvocations.com/job/ai-agent-architect-3219768-i.html ; https://www.virtualvocations.com/job/agentic-architect-2986770-i.html ; https://www.ziprecruiter.fr/jobs/546809096-lead-autonomous-ai-agent-architect-remote-a-protodigy | Aug 25; Apr 3; Jun 20 | F7 | B |
| S25 | Cognizant and Air India agentic architect postings | https://careers.cognizant.com/us-en/jobs/00069574701/agentic-ai-architect/ ; https://careers.airindia.com/job/Gurugram-Agentic-AI-Architect/55349644/ | Apr 24 (Air India) | F7, D3 | A |
| S26 | Cognitive Architect raw counts and IBM legacy | https://www.indeed.com/q-cognitive-architect-jobs.html ; https://www.ziprecruiter.com/Jobs/Cognitive-Architect ; https://www.glassdoor.com/Job/cognitive-architect-jobs-SRCH_KO0,19.htm ; https://www.simplyhired.com/search?q=cognitive+architect ; https://www.wayup.com/i-Management-Consulting-j-IBM-428651733367651/ | cached | F6 | B/C |
| S27 | Prompt Wizard exact-string searches | (searches run 2026-10-21; no postings) | Oct 21 | F8 null | B (null) |
| S28 | Indeed, Prompt Engineer | https://www.indeed.com/career/prompt-engineer | Aug 16 | F8 | B |
| S29 | Coursera prompt-engineering jobs; Recrew | https://www.coursera.org/articles/prompt-engineering-jobs ; https://www.recrew.ai/blog/reality-of-recruiting-prompt-engineers | 2026 | F8 | C / D |
| S30 | Indeed AI-labeled titles (PYMNTS; Indeed method via summary) | https://www.pymnts.com/?p=3961580 ; https://book.st-hakky.com/en/news/ai-related-jobs-spread-across-fields-bey | 2026 | F11, quorum precedent | C |
| S31 | Dataford (via Packt) and CTO guide | https://www.packtpub.com/en-NO/learning/author-posts ; https://www.ivanturkovic.com/2026/04/24/ai-job-titles-2026-naming-chaos/ | Jan-Jun; Apr 24 | F11, D2 | C |
| S32 | India/GCC: Weekday, Taggd, Swarajya (NASSCOM-Zinnov), Storyboard18 (Quess) | https://www.weekday.works/jobs/ai-jobs-in-india-2 ; https://taggd.in/blogs/gcc-skills-in-demand/ ; https://swarajyamag.com/economy/ai-data-skills-now-drive-two-in-three-new-gcc-jobs-in-india-as-hiring-rises-11-per-cent ; https://www.storyboard18.com/how-it-works/indias-1900-gccs-face-18-43-talent-shortfall-in-key-tech-roles-quess-corp-90866.htm | Oct 9; 2026 | F10, D8 | B/C |
| S33 | Reporting/org structure: Salt PDF; People Matters (IBM) | https://welovesalt.com/wp-content/uploads/2026/07/AI-Leadership-Pulse-Report_Salt-Solutions-Group.pdf ; https://www.peoplematters.in/amp/news/ai-and-emerging-tech/76percent-of-firms-now-have-a-chief-ai-officer-up-from-26percent-in-a-year-ibm-49550 | Jul 2026; 2026 | F12 | C |
| S34 | DataHub context report (vendor survey) | https://datahub.com/blog/context-engineer/ | 2026 | Context (95% plan training) | C |
| S35 | FDE alias and lab usage (UKY/Exponent; IIT) | https://pigmancareers.uky.edu/blog/2026/05/28/forward-deployed-engineer-interview-the-definitive-2026-guide-fde/ ; https://www.iit.edu/blog/forward-deployed-engineer | May 28 | F3 | C |
| S36 | JobsPipe vendor posts on Indeed/Wellfound/Lightcast access (descriptions only) | https://jobspipe.dev/llms.txt?src=md-twin | Oct 19 | D1, D9 | C |
| S37 | Lensa via Institute of Data (5,573 "ai engineer" jobs) | https://jobs.institutedata.com/jobs/ai-engineer-jobs/ | undated | D2 row 1 | C |
| S38 | Recalled, not tested: context-engineering term popularized by practitioners in mid-2025; Otta acquired by Welcome to the Jungle | (none) | - | Background only | D |
