---
id: T0-05
title: "Unconventional hiring tactics for GenAI roles, late 2026: OSS contributions, public micro-audits, targeted outreach"
date: 2026-10-23
status: complete
topic: "Which unconventional tactics (OSS contribution to vLLM/Ollama/Langfuse/LiteLLM/SGLang and peers, public technical micro-audits, targeted outreach to engineering leaders) bypass ATS queues and generate interview loops for GenAI roles"
tags: [genai-jobs, hiring-tactics, ats-bypass, open-source, vllm, sglang, ollama, langfuse, litellm, micro-audit, cold-outreach, deliverability, funnel-benchmarks, cfaa-tos-risk]
informs_decisions:
  - "How to split job-search hours across OSS contribution, public micro-audits, targeted outreach and standard applications"
  - "Which repos to contribute to, and what counts as a qualifying contribution"
  - "Outreach tooling, weekly send cap, and stop/pivot rules"
  - "The legal/ToS envelope for publishing audits of third-party AI products"
confidence: medium-low  # high on repo gates, funnel baselines and legal/ToS constraints (primary or large-n sources); low on per-tactic conversion and time-vs-yield (no direct measurement exists; modeled)
---

# Unconventional hiring tactics for GenAI roles (late 2026): OSS contributions, public micro-audits, targeted outreach

> **How to read this file.** Evidence grades: **A** = primary/canonical source retrieved and read (repo file at a pinned commit, policy page, RFC, employer posting, large first-party dataset); **B** = named reputable secondary, or vendor dataset with a stated method; **C** = vendor marketing, unsourced or self-selected estimate, headline/snippet-only, or my own inference from data; **D** = recalled from memory, or modeled with assumed parameters. Tags such as `[A · E1-05]` point to the ledger at the end. *Found* = retrieved this session; *recalled* = from memory, capped at D until verified. Research ran 2026-10-21 → 2026-10-23. "T1–T4" are undefined in the brief; I assume **employer tiers**: T1 frontier labs and flagship inference/infra companies; T2 well-funded AI-native startups; T3 growth-stage or large tech adding GenAI; T4 SMB/enterprise/agency GenAI roles.

## Prior

Recorded 2026-10-21, before any search. All Grade D (memory). Outcomes are scored in the **Delta** section.

| # | Proposition (checkable) | P(true) |
|---|---|---|
| P1 | The "single merged PR → 10× recruiter inbound vs 500 Easy Applies" figure has no published measurement. The direction (OSS signal beats mass-apply) is plausible; the ratio is folklore. | 0.80 |
| P2 | OSS→job conversion runs through *sustained, non-trivial* contribution and company-employed maintainers, not one-off PRs. Pipelines are informal; paid sponsorships/fellowships exist but are rare and small. A single merged PR is the modal outcome in big repos, so it is a weak differentiator. | 0.65 |
| P3 | (a) High-context outreach carrying a verifiable artifact beats recruiter-style InMail and generic cold email, but no public dataset isolates candidate→hiring-manager reply rates by personalization depth; citable numbers will be adjacent proxies. (b) At ≤ ~30 sends/week, deliverability risk comes from missing authentication and content patterns, not volume; LinkedIn automation carries account-restriction risk; GitHub rules restrict harvesting emails for unsolicited recruiting. | 0.70 / 0.70 |
| P4 | Teardown→hire stories are well documented in security/prompt-injection and "I built a tool for X" cases, and mostly anecdotal and survivorship-biased elsewhere. Dominant failure modes: factual errors from black-box inference; tone/entitlement; legal/ToS exposure when moving from passive measurement to active probing of production AI endpoints. | 0.65 |
| P5 | The standard funnel (application → recruiter screen) is low single digits; referrals convert at multiples. No source quantifies offer-yield *per hour* for unconventional tactics, so time-vs-yield will be a model with wide error bars. | 0.75 |

## Research Question

**Decision.** Which unconventional tactics reliably bypass ATS queues and generate interview loops for GenAI roles in late 2026: (1) open-source contributions to vLLM, Ollama, Langfuse, LiteLLM, SGLang (plus transformers, llama.cpp, Axolotl); (2) public technical micro-audits/teardowns of target companies' products; (3) targeted cold outreach to engineering directors and founders?

**Sub-questions (domain probes).** Which repos have hiring pipelines or sponsorship programs? What makes an audit succeed versus get dismissed? What tooling and deliverability setup lets a job seeker stage outreach without burning a domain? Which reproducible templates exist (TTFT/TPOT profiling, leak detection, prompt-injection audits)? What are verified response rates for high-context DMs versus recruiter InMails? What are the legal/IP/boundary risks of analyzing private AI APIs?

**Known claim to test (unverified at brief time).** "A single merged PR in a high-velocity tier-1 AI repo (vLLM, transformers, Ollama) delivers 10× higher recruiter inbound than 500 cold LinkedIn Easy Applies."

**Out of scope.** Generic LinkedIn connection spam, mass email blasts, in-person meetups.

## Key Findings

Twelve findings, each with its evidence grade. Detail and sources follow in *Detailed Findings* and the ledger.

**1. The "10× per merged PR" claim has no measurement behind it, and it is ill-posed.** Two direct searches for the claim returned no source that states or measures it (only Easy Apply guidance and job-board pages), and an extended search for contributor→hire stories surfaced only opinion pieces with no numbers ("Not because it guarantees attention", `W-12`; a "cheat code" anecdote, `W-12`). The claim divides a *recruiter-inbound* outcome by an *application* input whose own inbound yield is ≈ 0 by construction. The only measured baseline (Ashby, all roles) is 3% application→interview and ≈ 0.2% application→offer, so 500 Easy Applies ≈ 15 interviews and ≈ 1 offer; 10× that is ~150 recruiter contacts from one PR, a scale nothing I found supports. Authors of merged vLLM-class PRs are also already-strong candidates (confounding). **Grade C** (absence after targeted search; honest gap). `[C · W-06, W-12, F-06]`

**2. The measurable lever is *who initiates*, not which trick you use.** Gem (165M+ applications): ~1 hire per 200 applications (0.5%), only 8% pass the initial screen, sourced candidates are ~8× and referrals ~11× likelier to be hired than inbound. Ashby (38M applications, 2021–2024): application→interview is 3% inbound vs 25% sourced vs 40% referral; offer rate in Q4 2024 was 0.2% inbound vs 7.3% referral (≈ 36×). These lifts are correlational (referred and sourced candidates are pre-filtered), but they say any tactic that makes a *named human at the company pull you in* has large leverage. None of the three tactics has been measured against this baseline. **Grade A/B** for the lever; **C** for mapping tactics onto it. `[A/B · F-05, F-06, F-07]`

**3. A single merged contribution is the modal outcome in every repo I examined, so it is a weak signal by itself.** From git history of eight repos: 49–82% of all contributor identities have exactly one commit (Ollama 81%, transformers 68%, Axolotl 68%, Langfuse 68%, llama.cpp 64%, vLLM 59%, LiteLLM 57%, SGLang 50%). Among newcomers whose first commit fell 12–24 months ago, only 1.8–17.4% reached ≥ 10 commits within a year (SGLang 17.4%, Langfuse 15.6% (n = 45), vLLM 11.5%, Axolotl 8.9% (n = 56), llama.cpp 7.4%, LiteLLM 5.5%, transformers 2.5%, Ollama 1.8%), and only 0.9–18.7% were still active six months later. Caveats: commits ≠ PR merge rates; corporate-domain shares are lower bounds. **Grade A** for the numbers (reproducible from pinned SHAs); **C** for interpretation. `[A/C · E2]`

**4. The bar is explicit and rising, and cheap contributions are now risky.** vLLM's past committers had "approximately 30+ PRs of substantial quality and scope" plus "approximately 10+" reviews of external PRs (57 active committers). vLLM bans pure-agent PRs ("automatic banning") and one-off typo PRs; transformers asks first-timers not to use code agents, closes agent-written PRs without review and rejects "busywork"; llama.cpp permanently bans undisclosed AI use and caps new contributors at one open PR; Axolotl "do[es] not accept contribution farming… to pad a GitHub profile". GitHub added open-PR caps for non-write users (2026-06-17) and PR/issue restriction settings; Hacktoberfest 2026 stopped counting PRs toward rewards. A first PR now has to be something "agents can't do": a bisected bug with a reproducer, a regression test, a minimal diff. **Grade A.** `[A · E1-02, E1-05, E1-08, E1-09, E1-13, L-15, X-01]`

**5. Hiring pipelines exist but live in employer postings, not repo processes, and no named contributor→hire case could be verified.** Hugging Face's Open-Source MLE role *requires* "A public open-source track record, such as merged pull requests to ML or data libraries" (Workable, 2026-05-29). Inferact's MTS Inference posting lists "Contributions to open-source ML or system infrastructure projects" as preferred and "Implemented core features in vLLM" as a bonus. RadixArk's DevTech role prefers hands-on SGLang/vLLM work and OSS contributions, and RadixArk runs a paid one-year "AI Infra Resident" program (Palo Alto, listed at $200,000). A Red Hat llama.cpp role required "prior experience contributing to a major open-source project". LiteLLM and Langfuse test code in interviews (LiteLLM: "solving an issue on LiteLLM's github together"; Langfuse: code review → feature-building) but do not source from contributors. Searches for a documented "merged PR → hired" case for vLLM, SGLang, Ollama, LiteLLM, Langfuse or Axolotl found none. **Grade A/B** (postings); the gap is itself a finding. `[A/B · W-05, W-07, W-08, W-10, W-11, H-01, H-02, O-04]`

**6. In vLLM and SGLang, the people who ship are mostly employees of hardware and platform vendors, which shapes who benefits.** Twelve-month commit authors by email domain (distinct identities / commits): vLLM — amd.com 149/1,225, nvidia.com 81/336, intel.com 65/586, redhat.com 38/628, ibm.com 30/200, meta.com 25/186, inferact.ai 11/273; SGLang — amd.com 79/760, nvidia.com 47/273, intel.com 45/292, thinkingmachines.ai 14/100, radixark.ai 4/202. A noisy proxy for personal→corporate identity transitions finds 30 cases in vLLM (3 in 2024, 12 in 2025, 15 in 2026; median ~216 days after first commit), 12 in SGLang, 19 in transformers, 8 in llama.cpp, 4 in LiteLLM, 2 in Axolotl, 1 in Langfuse, 0 in Ollama. Ollama, Langfuse, Axolotl and LiteLLM are dominated by small core teams (top-10 authors = 63–87% of 12-month commits). **Grade C** (own inference; proxy is noisy in both directions). `[C · E2]`

**7. Teardown→hire evidence is real but thin and survivorship-biased; the surviving cases share a pattern.** Riley Goodside was hired by Scale AI (Dec 2022) "after some of his prompts gained attention online" `[B · W-13]`; The Wire reports that Nisarga Adhikary, who reported five critical vulnerabilities in CBSE's OSM portal to CERT-In, was hired at IIT Kanpur's cybersecurity hub (headline and meta description only; body not retrieved) `[C · C-01]`; Artificial Analysis publicly tested Reflection 70B in September 2024 and said it could not verify what it had tested `[B · V-01]` (a firm's reputation, not a hire); Johann Rehberger published a daily prompt-injection report series in August 2025 with disclosure notes, but the source states no employment outcome `[A · C-02]`. Common features: public, reproducible, claim-calibrated, relevant to a specific audience, and disclosed through proper channels. I found no dataset of audit→reply or audit→loop conversion. **Grade C.**

**8. Legal/ToS exposure is the sharpest tail risk of audits, and the safest surface is software you run yourself.** OpenAI's Usage Policies (effective 2025-10-29) prohibit "unsolicited safety testing" and "circumventing our safeguards"; its EU Terms (updated 2026-01-16) ban reverse engineering, automated extraction and bypassing protective measures. Anthropic's disclosure safe harbor excludes "red-teaming or adversarial testing of models" and forbids disclosure before prior written notice; its model bug bounty is invite-only with an NDA. DOJ's 2022 CFAA policy covers only conduct that is "solely" good-faith research and, per WSGR, "does not provide any concrete legal protections". India's IT Act s.43 "does not distinguish" ethical researchers (IFF, 2021; may be dated). Practical envelope: passive, documented-API, own-account, normal-rate measurement of *public* behavior, or audits of open-source components on your own hardware; vulnerabilities go through the vendor's channel before anything is public. **Grade A** (policy texts), **B** (legal commentary). `[A/B · L-03…L-12]`

**9. No verified candidate→hiring-manager reply rate exists in what I could access; the verified numbers are adjacent.** Pin (4M+ recruiter→candidate messages, 2025-06 → 2026-05): recruiter-written email 6.31%, automated email 4.96%, LinkedIn message 17.08%, engineering & data 4.64%. Instantly (cold B2B email, billions of sends, 2025): average reply 3.43%, top quartile 5.5%+, top decile 10.7%+, best first touches under 80 words, 58% of replies come from step 1. Figures that circulate for job seekers are not measurements: interviewing.io's 25–50% (personalized email to targets with an online presence) is the author's estimate with no sample; PitchHired's "roughly 5% to 15%" is the author's planning range; the only public-account study (79 self-reported outcomes) is non-random and reports no reply rate. **Planning range (judgment, Grade D): 3–8% reply, 10%+ as a stretch; treat 25–50% claims as unverified.** `[B/C · F-01, F-03, F-09, J-01, J-02]`

**10. At ≤ 30 sends/week the constraints are authentication, address accuracy, platform rules and complaints, and paid tooling is mostly unnecessary.** Google's and Microsoft's formal bulk rules target senders above 5,000 messages/day (both via secondary sources); Instantly advises bounce < 2% and a 5–10/day ramp for new domains over 4–6 weeks. Vendor claims for email finders (90–99%) collapse in an independent-style audit by Pin (1.3M lookups, Mar–May 2026): find rates RocketReach 29.8%, Wiza 55.2%, ContactOut 48.2%, Forager 45.9% (Apollo and Hunter not tested; Pin is itself a vendor). LinkedIn removed Apollo and Seamless.ai company pages on 2025-03-06; PhantomBuster's own guidance is ~50–100 connection requests/week and "paid plans don't remove invitation limits". GitHub's Acceptable Use Policy §7 bars using information from the service "for the purposes of sending unsolicited emails to users… such as to recruiters, headhunters, and job boards". Free tiers (Apollo, Hunter) plus manual verification are enough. **Grade B/C.** `[B/C · T-01, T-02, F-03, T-06, T-07, T-08, T-09, T-10, T-12, L-01, L-13]`

**11. On time-vs-yield, no tactic shows a 10× per-hour advantage; the case for unconventional tactics rests on saturation of the cheap channel, tier access and compounding signal.** Using sourced anchors (Ashby 0.2% inbound application→offer; Gem 0.5% application→hire; Instantly/Pin reply rates) and *assumed* conversion parameters (labeled in D6), the base case is ~0.27 offers per 100 focused hours for artifact-carrying outreach, ~0.45 for tailored applications, and ~0.30 offers total from mass-applying to an assumed pool of ~300 openings (which saturates after ~20 hours). Outreach beats tailored applications per hour only if the target tier's inbound application→offer rate is below ~0.09%. An OSS sprint (100 h) breaks even only if it lifts the effectiveness of later outreach by ≥ 32%; a company-specific audit (12 h for one target) needs a ~17× multiple on that target's offer probability, while a category-level artifact reused across 20 targets needs ~1.8×. **Grade D (modeled)**; the "no 10× per-hour edge" result holds in all three scenarios, but the ranking of the tactics against each other does not. `[D · model_checks.py, F-05, F-06, F-03]`

**12. Every channel is raising its guard against low-effort volume, which raises the relative value of hard-to-fake, verifiable artifacts.** Ashby reports "fraudulent candidates have begun creeping their way into the droves of inbound applications" and inbound at 52% of hires in Q2 2025; AI engineer is LinkedIn's fastest-growing title for young workers for a second year (75,000 of 639,000 AI-related US postings added 2023–2025); curl ended its bug bounty at end of January 2026 over AI-generated reports; GitHub's maintainer controls (2026-02 → 2026-06) exist because "the cost to create has dropped but the cost to review has not". **Grade B/C.** `[B/C · F-07, M-02, L-14, L-15]`

## Recommendation

**Run the three tactics as one pipeline — artifact → named human → interview loop — not as three independent bets, and size each by its evidence.** The only large-n finding in this file is that being pulled in by a named human converts far better than applying cold (Finding 2). The tactics are different ways of earning that pull; their conversion has not been measured, so the plan includes measurement and stop rules.

**1. Hour budget (per 100 search hours per quarter; judgment, Grade D).**

| Share | Activity | Why |
|---|---|---|
| ~25 h | Standard applications to the ~300 (assumed) relevant GenAI openings, each tied to a named-human route where one exists | Cheap and saturating: the pool is finite, so extra hours here have zero marginal yield. Do it first, then stop. |
| ~45 h | Artifact-carrying outreach: one *category-level* artifact (≈ 10–15 h, reusable across ~20 targets) plus ≈ 8–12 h of company-specific tailoring for the top 5 targets; ≤ 30 sends/week | Highest-evidence route to a named human (Findings 2, 9). Company-specific audits only pay for priority targets (Finding 11). |
| ~20 h | OSS in **one** repo whose steward or major contributing employer is on your target list, only if you can sustain ~8–10 h/week for 8–12 weeks; otherwise move these hours to outreach | Slow-burn signal with no verified per-hour yield (Findings 3–5); worth it mainly as the source of artifacts and maintainer relationships. |
| ~10 h | Instrumentation: a log of every send, reply, loop and outcome | Without it none of the stop rules work. |

**2. OSS rules.** (a) Do not count on a single merged PR for inbound; use OSS as the headline only after ≥ 3 merged or in-review PRs plus ≥ 5 reviews/triage actions in one area (≥ 5 commits puts a newcomer in the top ~3–29% of recent cohorts depending on repo, `E2`). (b) Start with what agents cannot do (bisect, reproducer, regression test, minimal diff), disclose AI assistance, open an issue first where the repo requires it, and respect PR caps. (c) Choose by employer fit: hardware/platform vendors staff vLLM/SGLang/llama.cpp (T3 route); Inferact/RadixArk/Hugging Face are T1 routes; Langfuse/LiteLLM/Ollama/Axolotl (T2) are core-team-dominated and low-retention, so contribute there for a specific reason and treat outreach as the main route. (d) Stop-loss: no merged PR and no substantive maintainer exchange after 8 weeks → reallocate.

**3. Micro-audit rules.** Green-zone only (D3.2): passive, public, documented-API, own-account, normal-rate measurement; or an *own-instance* audit of open-source components (vLLM, SGLang, Ollama, LiteLLM, Langfuse) on your own hardware, which is also the natural bridge to PRs. Two tiers: a **category-level benchmark/teardown** (reusable across many targets) and a **company-specific 1–2 page note** for the top 5. Use the template and rubric in D3.4; private notice before any publication of a vulnerability; calibrated language ("observed", "could not verify").

**4. Outreach rules.** Target named engineering directors, hiring managers and founders (not generic inboxes); ≤ 30 sends/week; ramp 10 → 15 → 20 → ≤ 30 over four weeks; first touch ≤ ~80–90 words, one artifact link, one specific ask; one follow-up at day 5–7; authenticate your domain (SPF/DKIM/DMARC); verify addresses; manual LinkedIn only; never harvest emails from GitHub for bulk contact. Planning reply rate 3–8%.

**5. Decision checkpoints (computed in D6).** After 60 targeted sends: **0 replies** → the one-sided 95% upper bound on your true rate is 4.9%, so change the artifact or targeting before sending more (volume is not the problem); **1–2 replies** (95% CI 0–11.5%) → continue and tighten; **≥ 3 replies** (5%) → within the planning range, continue. At week 8 judge OSS against its stop-loss; at week 12 review the whole portfolio and move hours to whichever route produced loops.

**6. Tier playbook (assumed tiers; the employer examples are sourced, the routes and cautions are judgment, Grade D).**

| Tier | Examples in the evidence | Best-supported route | Lead artifact | Caution |
|---|---|---|---|---|
| T1 | Inferact, RadixArk, Hugging Face (frontier labs not researched) | Outreach + sustained OSS in their repo; early-career residency where offered (RadixArk, 1-year, listed $200K) | Merged PRs + a measured benchmark/teardown | No tier-specific funnel data found; most roles seen are US-based (visa/location not assessed) |
| T2 | Langfuse (ClickHouse), LiteLLM, Ollama, Axolotl | Founder outreach naming a specific issue/PR; own-instance audit of their OSS | Small fix with tests; integration repro; short audit | Small core teams, 1–7% of newcomers still active after 6 months; LiteLLM's onsite includes fixing a repo issue, so contributions double as rehearsal |
| T3 | AMD, NVIDIA, Intel, Red Hat/IBM, Meta (the dominant vLLM/SGLang/llama.cpp contributors) | OSS in the repo they staff + referral + standard application | Hardware-backend/kernel PRs, benchmarks on their hardware | Heavy ATS use; combine with a referral |
| T4 | SMB/enterprise/agency | Standard + referral; passive audit of a public AI feature | 1–2 page audit | Heavy OSS has lower payoff per hour here |

## Alternatives Considered

| Alternative | Evidence | Why it is not the primary plan |
|---|---|---|
| Warm referrals / existing network | Strongest measured: Ashby 40% application→interview vs 3% inbound; Gem referrals 11× inbound `[A/B · F-05, F-06]` | Requires an existing network; the three tactics are how you *create* introductions. Use whenever available. |
| Weak-tie introductions (second-degree contacts) | Science 2022, ~20M LinkedIn users: moderately weak ties (inflection ≈ 10 mutual connections) transmit jobs best, more so in digital industries `[B · J-03]` | Measured for LinkedIn friend-adds, not for cold messages; adopted as a targeting heuristic inside outreach. |
| Recruiter InMail / being sourced | Pin: 17.08% reply to recruiter LinkedIn messages `[B · F-01]` | The direction is recruiter→candidate; candidates cannot buy their way into being sourced (Premium plans give 5–15 InMails/month `[C · T-09]`). |
| Mass Easy Apply / auto-apply | ~0–1% per 100–300 applications (Reddit anecdotes), 0.1–2% offer-or-response (Interview Guys via Whali) `[C · J-02]`; Ashby flags fraud creeping into inbound `[A/B · F-07]` | Finite openings and low per-application yield; but cheap, so it is kept as a saturating baseline. |
| Fellowships / residencies | RadixArk one-year resident program `[A · H-01]`; a16z grants fund maintainers, not job seekers `[A · O-03]`; LFX/GSoC mentorship for these repos not verified | Few programs, US-located, competitive; take if available. |
| Writing/benchmarks as standalone content | Inferact bonus: "Written widely-shared technical blogs or side projects on vLLM or LLM inference" `[B · W-05]`; Goodside `[B · W-13]` | Folded into the artifact strategy rather than run separately. |
| Contract/bounty work converting to full-time | Not researched | No evidence gathered; listed as an open question. |
| Hackathons / competitions | Not researched | Partly in-person (out of scope); no evidence gathered. |

## Detailed Findings

### D0. Method, evidence discipline, and limits of this session

- **Found vs recalled.** Five priors and sixteen recalled facts (R1–R16) were written down before any search and are tested in the *Delta* section. Anything not retrieved is flagged as recalled (Grade D) or as a search-only lead.
- **Repo policy text (Grade A).** Read from git objects of treeless clones at pinned commits, so every quote is reproducible: `git show <SHA>:<path>`. Pinned SHAs: vllm `96e59c60…b25ce`, sglang `43728298…09879c`, transformers `6b75aeea…e810d4`, llama.cpp `f8490953…e96f`, litellm `a31c5230…5fcd4e`, langfuse `f8363911…78872`, ollama `2cd63f7a…1707c56`, axolotl `dfb9cb36…cfbc1e`; full SHAs and permalinks are in the ledger (`E1-xx`). All eight policy files exist at those SHAs (checked).
- **Contributor statistics (original analysis, `E2`).** `git log --no-merges` on each repo's default branch; bots removed by regex; identity = lowercase author email (GitHub `noreply` → username); "last 12 months" = 2025-10-21 → 2026-10-21; **newcomer cohort** = identities whose first commit fell 24–12 months before 2026-10-21, so each has a full 12-month follow-up. Sensitivity run merging identities that share a multi-token display name moves single-commit shares by ≤ 3 percentage points. **Limits:** only merged commits on the default branch are visible, so there are *no PR merge rates*; squash-merge attribution; people with several emails are split; corporate-domain shares are lower bounds (noreply/gmail hide employers); cohorts include employees contributing as part of their job, which inflates retention relative to a job-seeking newcomer.
- **Web research.** WebSearch/WebFetch only; URLs not surfaced by a search or the conversation were refused by the tool's allowlist (e.g., Google's sender-guidelines page and genai.owasp.org), so those facts rest on secondary sources and are labeled; the DOJ's CFAA charging policy itself was not fetched either and is known only through law-firm summaries. JS-rendered pages (Microsoft Tech Community) returned empty. One fetch (flosshub wage-premium paper) failed and is unused.
- **Session constraints.** Eight parallel research subagents all terminated on a usage limit (HTTP 429) and were abandoned; the research was redone sequentially with notes saved to ledger files. Two fetch batches also hit the limit and were retried successfully after it reset. The `gh` token was invalid, so the GitHub GraphQL API was **not executed**; the snippet in D4.2 is untested. The shell could reach GitHub via git but not the open web.

### D1. The standard funnel, and what it implies for the "10×" claim

| Metric | Value | Source | Grade |
|---|---|---|---|
| Application → hire, all roles | ~1 hire per 200 applications (0.5%) | Gem 2026 benchmarks (165M+ applications, 15M candidates, 1.2M hires; Jun 2021–May 2025) `F-05` | A/B |
| Applicants passing the initial screen | 8% | Gem `F-05` | A/B |
| Inbound share of applications vs of hires | ~90% vs ~half | Gem `F-05` | A/B |
| Direct sourcing | 11% of hires from 2.6% of applications (≈ 4.2×) | Gem `F-05` | A/B |
| Referral vs inbound conversion; sourced vs inbound | ~11×; ~8× | Gem `F-05` | A/B |
| Application → interview | inbound 3%; sourced 25%; referral 40%; internal 42%; agency 42% | Ashby (38M applications, 93K jobs, 2021–2024) `F-06` | A/B |
| Interview → offer | inbound 6%; sourced 6%; referral 16%; internal 32%; agency 8% | Ashby `F-06` | A/B |
| Offer rate, Q4 2024 (metric undefined on the page; consistent with 3% × 6% ≈ 0.18%) | inbound 0.2%; referral 7.3% (≈ 36×); internal 17.9% | Ashby `F-06` | A/B |
| Share of hires by source, Jan 2021–Jun 2025 (~250K hires) | inbound 43–52% (52% in Q2 2025); referral ~18%; sourced ~16%; tech roles 24% sourced | Ashby `F-07` | A/B |
| Applications per hire, Q1 2026; interviews per hire | 291; 11.7 (business) / 17.6 (technical) | Pin citing Ashby (secondary) `F-08` | C |
| "242 applications per opening → 0.4%" | Business Insider via Novorésumé via The Interview Guys; no sample or period; 0.4% is just 1/242 | `M-01` | C |
| Recruiter → candidate reply rate | automated email 4.96%; recruiter-written email 6.31%; LinkedIn message 17.08%; engineering & data 4.64% (4M+ messages, 2025-06-01 → 2026-05-31) | Pin `F-01` | B |
| Cold B2B email reply rate | average 3.43%; top quartile 5.5%+; top decile 10.7%+ | Instantly `F-03` | B |

**Reading the table.**

1. Inbound applications are ~90% of volume but ~half of hires, and they convert 3% to interview. Sourced and referred candidates convert 8–13× better per application. *Selection explains part of this* (referrals are pre-vetted), so treat the multiples as the size of the prize for being pulled in by a human, not as a causal effect of any tactic.
2. Gem's and Ashby's customers skew toward tech-forward companies that run modern ATSs; the direction of bias for GenAI startups and for large incumbents is unknown. **No GenAI-specific funnel rate is published** (searched: Greenhouse/Ashby/LinkedIn/Glassdoor AI-role application volume; only the all-role figures above, and a LinkedIn note that AI engineer is the fastest-growing title `M-02`).
3. Pin's LinkedIn-vs-email gap (17% vs ~5–6%) is a recruiter→candidate effect; it does not transfer to candidate→manager outreach, and Pin itself labels the email+LinkedIn association as non-causal.

**Why "10× recruiter inbound per merged PR vs 500 Easy Applies" cannot be taken at face value.** (i) Not measured anywhere I could find. (ii) Metric mismatch: recruiter *inbound contacts* are not an output of Easy Apply at all, so the ratio's denominator is ≈ 0 and "10×" is trivially satisfiable or undefined. (iii) If "inbound" is read as "interview requests", the all-role Ashby baseline for 500 applications is ~15 interviews (3%) or ~1 offer (0.2%); 10× would imply ~150 contacts from one PR. (iv) The population that merges PRs into vLLM-class repos is already strong and often already employed (AMD/NVIDIA/Intel/Red Hat domains dominate), so any correlation with inbound is confounded. (v) GitHub's Acceptable Use Policy §7 bars using GitHub-derived information to send unsolicited emails "such as to recruiters, headhunters, and job boards", which limits one plausible mechanism for recruiter inbound from commit metadata `[A · L-01]`. (vi) What *is* plausible: a merged, non-trivial contribution makes you discoverable and credible, which can move you from "inbound" to "sourced" or "referred" status; the size of that move for GenAI roles is unmeasured.

**What a valid test would look like.** Randomize *targets*, not days: for ≥ 100 target roles, apply-only vs apply + artifact + named-human outreach; outcomes = reply within 14 days, interview loop within 60 days; analyze with the interval table in D6. A retrospective version would need employer-side data (applicant source flags plus contributor identity), which only an ATS vendor or a hiring team could supply.

### D2. Tactic 1 — OSS contributor → hire pipeline

#### D2.1 Gates, on-ramps and hiring text by repo

| Repo (steward; commercial entity) | On-ramp | Hard gates and AI policy | Hiring text found |
|---|---|---|---|
| **vLLM** (vllm-project; Inferact raised $150M seed at $800M, 2026-01-22 `W-01`; Red Hat; AMD/NVIDIA/Intel staff) | `good first issue` label; "Selected onboarding tasks" project `E1-06` | DCO sign-off; AI disclosure; "Pure code-agent PRs are **not allowed**"; "Breaching these guidelines can result in automatic banning"; no one-off typo PRs `E1-05, E1-06`. Committers are "highly selective and merit based", nominated on a private list with a two-week feedback period; past committers had "approximately 30+ PRs of substantial quality and scope" and "approximately 10+" reviews of external PRs; 57 active + 18 emeritus, listed by area (kernels, quantization, model support, KV connectors, AMD/Intel/NVIDIA/TPU integrations, CI, docs) `E1-01…E1-04` | Inferact MTS Inference ($200–400K + equity; posted 2026-06-18; job-board mirror): minimum "Experience with LLM inference systems (vLLM, TensorRT-LLM, SGLang, TGI)"; preferred "Contributions to open-source ML or system infrastructure projects"; bonus "Implemented core features in vLLM", "Contributed to vLLM integrations (verl, OpenRLHF, Unsloth, LlamaFactory, etc)", "Written widely-shared technical blogs…" `W-05`. a16z Open Source AI Grant (2023) funded Woosuk Kwon and Zhuohan Li for vLLM `O-03` |
| **SGLang** (sgl-project; RadixArk, ~$400M valuation per anonymous sources, 2026-01-21 `W-02`) | Contribution guide `E1-07` | New contributors have no write permission; "only top and trusted contributors have permission to trigger CI tests" (`CI_PERMISSIONS.json`, `run-ci` label); merge needs Merge Oncall/Codeowner approvals `E1-07` | RadixArk **AI Infra Resident (1-year, paid, Palo Alto, listed $200,000)**: BS/MS, Python and/or C++, CUDA/JAX/distributed a plus; SGLang experience *not* required; responsibilities include "Contribute to SGLang, Miles, and other open-source projects" `H-01` (the Accel listing shows "Posted 6+ months ago" and mentions no conversion to full-time; the Greenhouse copy of the same posting lists no salary `H-01b`). **DevTech MTS**: 4+ years GPU/LLM-infra; preferred "Hands-on work with SGLang, Miles, vLLM, TensorRT-LLM, Megatron" and "contributions to open-source AI/ML projects" `H-02` |
| **transformers** (Hugging Face) | `Good First Issue` and `Good Second Issue` labels `E1-08` | First-time contributors are asked not to use code agents; agent-written PRs "closed without review", repeat offenders may be blocked; "Avoid small or 'busywork' PRs… given the current flood"; "you need to do things that agents can't do" (diagnose with `git bisect`, reproducer, compare against other models, minimal diff) `E1-08` | HF Open-Source MLE (Workable, posted 2026-05-29): requires "A public open-source track record, such as merged pull requests to ML or data libraries" plus a cover letter; nice-to-have prior contributions to Transformers/Datasets/Accelerate `W-07` |
| **llama.cpp** (ggml-org; ggml.ai joined Hugging Face, reported 2026-02-20 `W-04`) | Three levels: Contributors → Collaborators (Triage) → Maintainers `E1-09` | New contributors: "Limit your open PRs to 1", no trivial fixes; "Features must begin with an issue, not a PR"; bug fixes need a reproducible issue plus regression test; "Undisclosed AI usage may result in your account being permanently banned"; AI-written posts prohibited `E1-09` | Red Hat Principal/Senior Principal ML Engineer, llama.cpp ($189,600–351,050; closed): "Prior experience contributing to a major open-source project" `W-08` |
| **LiteLLM** (BerriAI, YC W23) | CLA; tests `E1-11` | CLA is "a legal requirement for all contributions to be merged"; "Adding at least 1 test is a hard requirement"; Conventional Commits `E1-11` | Backend LLM Engineer ($120–180K + 0.25–0.75% equity): 30-min intro → 1-hr HackerRank → 3-hr virtual onsite including "solving an issue on LiteLLM's github together"; contributions not required `W-10`. PyPI versions 1.82.7/1.82.8 were malicious on 2026-03-24 `S-01` |
| **Langfuse** (acquired by ClickHouse 2026-01-16; core stays MIT `W-03`) | `good first issue`; PR preview deployments `E1-12` | Open an issue before significant changes; undiscussed changes "may be rejected" `E1-12` | CONTRIBUTING banner: "We hire engineers who love open source and great developer experiences." Process: recruiter screen → code review → past-projects deep dive → feature-building interview → Super Day → meet ClickHouse → offer; no contributor-sourcing language `E1-12, W-11` |
| **Ollama** | Issue first for non-trivial PRs `E1-10` | Ideal issues are bugs, performance, security; features/refactors/large docs are "harder to review"; no AI-contribution policy found (its AGENTS.md is build instructions only) `E1-10` | Eight open roles on an aggregator (all Palo Alto: Developer Relations, four software-engineering roles, PMM, AE, GTM engineer); requirement text *not retrieved* `H-03` — **gap** |
| **Axolotl** (axolotl-ai-cloud) | "You do not need a history of merged PRs or access to a GPU to contribute" `E1-13` | "We do not accept contribution farming… submitting changes primarily to collect merged PRs and pad a GitHub profile"; PR template asks for Motivation and Context (how you use Axolotl) and an AI-usage disclaimer; AGENTS.md tells agents to refuse profile-credit PRs `E1-13` | None found |

#### D2.2 Contributor statistics (original analysis, `E2`; default-branch commits, 2026-10-21)

| Repo | Identities (all-time) | % with exactly 1 commit (raw / name-merged) | Last 12 months: identities / commits | Top-10 / top-50 share of 12-month commits | Newcomer cohort n | Cohort with ≥2 / ≥5 / ≥10 commits in 12 months | Cohort still active in last 6 months |
|---|---|---|---|---|---|---|---|
| vLLM | 3,796 | 58.9 / 56.5 | 2,479 / 12,888 | 19.0% / 41.3% | 1,114 | 46.3 / 20.5 / 11.5 | 15.4% |
| SGLang | 2,092 | 50.2 / 48.8 | 1,591 / 14,470 | 32.3% / 60.8% | 609 | 56.3 / 29.2 / 17.4 | 18.7% |
| transformers | 4,140 | 68.2 / 67.0 | 675 / 3,456 | 42.6% / 73.1% | 724 | 24.9 / 6.6 / 2.5 | 2.9% |
| llama.cpp | 2,168 | 64.0 / 63.2 | 978 / 4,983 | 42.1% / 66.4% | 417 | 41.0 / 13.2 / 7.4 | 10.1% |
| LiteLLM | 1,825 | 57.4 / 57.3 | 950 / 19,657 | 63.5% / 89.7% | 580 | 39.3 / 13.6 / 5.5 | 1.9% |
| Langfuse | 234 | 67.5 / 68.3 | 158 / 4,934 | 79.2% / 97.8% | 45 | 33.3 / 15.6 / 15.6 | 6.7% |
| Ollama | 649 | 81.2 / 81.8 | 119 / 1,216 | 83.4% / 94.3% | 221 | 13.1 / 2.7 / 1.8 | 0.9% |
| Axolotl | 285 | 67.7 / 66.4 | 70 / 606 | 86.6% / 96.7% | 56 | 26.8 / 8.9 / 8.9 | 3.6% |

**Top corporate email domains among 12-month commit authors (distinct identities / commits; lower bounds).** vLLM: amd.com 149/1,225; nvidia.com 81/336; intel.com 65/586; redhat.com 38/628; ibm.com 30/200; meta.com 25/186; daocloud.io 12/155; google.com 12/26; inferact.ai 11/273; cohere.com 10/28; mistral.ai 8/82. SGLang: amd.com 79/760; nvidia.com 47/273; intel.com 45/292; antgroup.com 19/62; thinkingmachines.ai 14/100; alibaba-inc.com 11/51; meta.com 11/42; huawei.com 11/26; bytedance.com 8/37; modal.com 8/13; radixark.ai 4/202. transformers: intel.com 12/274; huggingface.co 8/422 (HF staff mostly use noreply, so a lower bound); nvidia.com 8/9. llama.cpp: qualcomm.com 20/262; nvidia.com 15/257; intel.com 12/60; huggingface.co 5/619; ibm.com 7/78; redhat.com 6/77. LiteLLM: berri.ai 29/8,698 of 19,657 commits (core team); others 1–4 identities each (stripe.com, zocdoc.com, lasso.security, amazon.com, anthropic.com 2/13, fireworks.ai, coreweave.com). Langfuse: clickhouse.com 7/427; langfuse.com 6/853. Ollama: ollama.com 6/260. Axolotl: axolotl.ai 2/401.

**Personal → corporate identity transitions (noisy proxy).** Same multi-token name appears first under a personal/noreply identity and ≥ 90 days later under a corporate-domain identity. Overstates where the person was already employed; understates where they stayed on noreply. vLLM 30 (2024: 3, 2025: 12, 2026: 15; destinations nvidia 4, redhat 3, meta 3, amd 2, antgroup 2, mistral 2, inferact 1, poolside 1; median 216 days from first commit, median 1 personal commit before); SGLang 12 (thinkingmachines 2, amd 2, nvidia 1, intel 1, radixark 1…; median 180 days); transformers 19 (2020–2026); llama.cpp 8 (median 349 days); LiteLLM 4; Axolotl 2; Langfuse 1; Ollama 0.

**Interpretation (Grade C, own inference).**
1. One merged commit is the *modal* outcome everywhere, so "one merged PR" cannot by itself distinguish you.
2. vLLM and SGLang are corporate-staffed (AMD, NVIDIA, Intel, Red Hat/IBM): the plausible channel is *contribution → hired by a hardware/platform vendor or an inference startup*, and the transition proxy shows it occurs (vLLM: 15 cases in 2026 alone) — but it cannot show that contribution caused the hire. Ant OSS's December 2025 community post names contributors who are employees elsewhere (an OpenAI engineer with 77 vLLM PRs; an Alibaba Cloud researcher who moved from vLLM to SGLang; an Oracle engineer who is a core SGLang contributor) and says vLLM author Zhuohan "largely stopped contributing after joining OpenAI": affiliation patterns, with no hiring causation described `O-02`.
3. Ollama, Langfuse, Axolotl and LiteLLM are core-team-dominated (top-10 = 63–87% of 12-month commits) with very low newcomer retention, so commit data alone shows little community→hire flow there.
4. Percentile anchors for "worth mentioning": ≥ 5 commits in a year is top 20.5% (vLLM), 29.2% (SGLang), 13.2% (llama.cpp), 13.6% (LiteLLM), 6.6% (transformers), 15.6% (Langfuse; n = 45), 8.9% (Axolotl; n = 56) and 2.7% (Ollama) of newcomer cohorts; ≥ 10 commits is 11.5%, 17.4%, 7.4%, 5.5%, 2.5%, 15.6%, 8.9% and 1.8% respectively.

#### D2.3 What counts as a qualifying contribution (criteria)

1. Passes the repo's hard gates in D2.1 (issue-first where required, tests, DCO/CLA, AI disclosure, PR cap, no agent-only PRs).
2. Is something an agent can't do on its own (transformers: "you need to do things that agents can't do"): a bisected regression, a minimal reproducer, a regression test, a comparison against other models/hardware, a minimal diff (transformers' own list `E1-08`).
3. Lands in an area with a named owner (vLLM's `committers.md` lists areas; SGLang requires trusted-contributor CI triggering) and is aimed at bugs, performance or security rather than new surface area (Ollama's "ideal issues").
4. Is part of a *pattern*: at least 3 merged or in-review PRs plus 5 reviews/triage actions in one area before you headline it (my threshold; vLLM's committer bar of ~30+/~10+ is the aspirational anchor).
5. Comes with a public, reproducible write-up of what you measured (the Inferact posting lists "widely-shared technical blogs" as a bonus).

#### D2.4 Step-by-step protocol

| Step | What to do | Time (assumed unless stated) | Gate / evidence |
|---|---|---|---|
| 0. Pick the repo | Use D2.5. Require a hiring entity or employer on your target list, a newcomer on-ramp, and a skills match. | 2–3 h | Employer fit beats repo fame. |
| 1. Read the gates *at current HEAD* | Re-read CONTRIBUTING, AGENTS.md and governance files; these changed recently (agent bans, PR caps) and my pinned SHAs are from 2026-10-21. | 2–4 h | Links in the ledger (`E1-xx`). |
| 2. Build and run tests | Reproduce the dev environment; for GPU-gated repos plan for CI that you cannot trigger (SGLang: maintainers apply `run-ci`). | 4–10 h | A green local test run. |
| 3. Triage and review first (weeks 1–2) | Reproduce 3–5 open issues, add minimal reproducers, bisect where you can; comment on others' PRs only with substance. vLLM committers had ~10+ external-PR reviews. | 5–10 h/week | Maintainers start recognizing your handle. |
| 4. First PR (weeks 2–4) | Pick a bug/perf/security issue; open or claim the issue first; minimal diff; tests; DCO/CLA; disclose AI assistance; one open PR at a time. Expect slow review: a vLLM tool-parser PR took ~4 months from submission (2025-04-20) to merge (2025-08-16), including a maintainer request for tests and upstream CI failures `O-01` (one data point). | 8–20 h of work; 8–16 weeks of calendar time | Merged, or substantive review within 2 weeks. |
| 5. Widen within one area (weeks 4–12) | Aim for 3+ merged/in-review PRs and 5+ reviews/triage actions; use area owners from `committers.md` (vLLM) to find the right reviewer. | 8–10 h/week | The D2.3 pattern criterion. |
| 6. Publish evidence | One short technical note per merged PR: problem, measurement, diff, result, reproduction command. | 2–4 h each | Becomes the artifact for outreach. |
| 7. Convert | Identify the steward company and a named engineering leader (git-log domains, OSS Insight company tables, governance pages); send script S2 or S5 (D4.5); apply to roles that list contributions (Inferact, Hugging Face, RadixArk, Red Hat) and cite your PRs. Ask maintainers for feedback and introductions, not for jobs. | 3–6 h | A named human replies. |
| 8. Stop-loss | **Week 8:** no merged PR and no substantive maintainer exchange → reallocate. **Week 12:** fewer than 3 merged/in-review PRs in one area → treat OSS as a one-off artifact source, not a pipeline. | — | Keeps the sunk-cost trap out. |

#### D2.5 Which repo to choose

| If your profile and targets are… | Choose | Why (evidence) |
|---|---|---|
| CUDA/ROCm/Triton or systems work; targets include AMD, NVIDIA, Intel, Red Hat, Inferact, RadixArk | vLLM or SGLang | Corporate-staffed with named areas; Inferact and RadixArk postings reference both; 12-month transitions to vendors visible (`E2`, `W-05`, `H-02`) |
| Python/ML engineer aiming at Hugging Face | transformers | HF posting requires merged PRs `W-07`; but only 2.5% of newcomers reach 10 commits and agent-style PRs are rejected |
| C/C++ edge inference; Qualcomm, NVIDIA, Intel, Red Hat | llama.cpp | Employer domains in 12-month commits; Red Hat role `W-08`; but one-open-PR cap and permanent-ban policy |
| Backend/gateway/observability; startup roles | LiteLLM or Langfuse | LiteLLM's onsite includes fixing a repo issue `W-10`; Langfuse interviews code review and feature-building `W-11`; low external retention, so pair with founder outreach |
| Local inference, product-minded | Ollama | Bugs/perf/security welcomed `E1-10`, but 81% single-commit and a tiny core; best used for an *own-instance audit* artifact, not a pipeline |
| Fine-tuning/training tooling | Axolotl | Explicitly welcomes real use-case contributions, rejects profile padding `E1-13` |

#### D2.6 Pipeline map: evidence per hop

| Hop | Evidence for | Gap |
|---|---|---|
| Newcomer → first merged contribution | 50–81% of identities stop at one commit `E2`; ~4 months to merge in one documented vLLM case `O-01` | No merge-rate data (only merged commits are visible) |
| First → sustained (≥ 5 commits) | Cohort rates 2.7–29.2% `E2` | Cohorts include employees; the rate for a *job-seeking newcomer* is unknown |
| Sustained → employer exposure | Vendor-staffed repos; 30 vLLM identity transitions `E2` | Noisy proxy; no named cases; causation not shown |
| Exposure → interview loop | Postings that require/prefer contributions (HF, Inferact, RadixArk, Red Hat) `W-05, W-07, W-08, H-02` | No data on loop rates for applicants with contributions |
| Loop → offer | Referral interview→offer 16% vs 6% inbound (all roles) `F-06` | Not OSS-specific |

**Academic context (Grade B, abstracts only).** A 2024 ifo working paper on ~22,900 GitHub developers finds job movers raise OSS activity ≈ 16% during job search, concentrated in visibility-boosting projects in labor-market-valued languages, and that signaling also induces first-time contributions `A-01`. So the signal is crowded, which is consistent with Axolotl's and transformers' anti-farming rules. Hann, Roberts and Slaughter (ISR, 2013; Apache projects, six-year cohort) find "rank within an OSS meritocracy" associated with up to an 18% wage increase and call it "a credible and precise signal of participants' productive capacity" `A-02`: the premium attaches to *rank* (earned status), not to mere participation. Both predate or sit outside GenAI-specific hiring and report no employer-hire outcomes for it.

### D3. Tactic 2 — Public technical micro-audits

#### D3.1 What the evidence shows (cases)

| Case | What was public | Outcome | Evidence | What it teaches |
|---|---|---|---|---|
| Riley Goodside → Scale AI (Dec 2022) | Public prompt experiments that "gained attention online" | Hired by Scale AI as a prompt engineer | Washington Post via Independent on Saturday, 2023-02-27 `W-13` **B** | Public, demonstrable work aimed at the field the employer sits in. A single case from the early ChatGPT period. |
| Nisarga Adhikary → IIT Kanpur cybersecurity hub (The Wire, 2026-06-11) | Reported five critical vulnerabilities in CBSE's OSM portal to CERT-In "as early as February 25" | Headline says he was hired at IIT Kanpur's cybersecurity hub | Headline and meta description only; body not retrieved `C-01` **C** | Disclosure through the official channel (CERT-In), not publication first. Who decided the hire, and what legal pushback occurred, is unknown. |
| Artificial Analysis on Reflection 70B (Sept 2024) | Public benchmark numbers (MMLU equal to Llama 3 70B and "significantly lower than Meta's Llama 3.1 70B"); then, after private API access, "impressive performance but not to the level of the initial claims"; said it could not verify what it had tested and would re-test on released weights | Reputation for the evaluator; not a hire | VentureBeat `V-01` **B** | The calibrated sentence is the template: observed / could not verify / will re-test. |
| Johann Rehberger, "Month of AI Bugs" (Aug 2025) | One prompt-injection report per day across ChatGPT, Codex, Cursor, Claude Code, GitHub Copilot, Google Jules and others, each with disclosure notes; several vendors did not fix within 90/120-day windows | **No employment outcome stated** | Simon Willison, 2025-08-15 `C-02` **A** (for what the page says) | Persistence, a stated disclosure policy, and a clear vulnerability taxonomy (data exfiltration via Markdown images and allow-listed domains, command execution, privilege escalation via agent config files; "AI Kill Chain"). |
| curl ends its bug bounty (Jan 2026) — *negative case* | Flood of low-quality, often AI-generated reports | Bounty ended end of Jan 2026; Stenberg says he will keep publicly shaming "silly" submissions | The Register 2026-01-21 `L-14` **B** | What gets dismissed: unreproducible, not understood, AI-slop. "You should NEVER report a bug or a vulnerability unless you actually understand it – and can reproduce it." |
| OpenAI o1 probing warnings (Sept 2024) — *negative case* | Users probing o1's reasoning | Warning emails ("Please halt this activity…"); no confirmed bans | Ars Technica via eDiscovery Today `L-09` **B** | Probing production AI endpoints can trigger policy enforcement. |

**Pattern in the successes:** public, reproducible, claim-calibrated, relevant to a specific audience, routed through proper channels. **Pattern in the dismissals:** unreproducible or misunderstood findings, volume over verification, entitlement, ToS-violating methods. **Evidence gaps:** no dataset of audit→reply or audit→loop conversion; the positive cases are survivors (survivorship bias cannot be corrected from public accounts); two of the four positive cases are not hires of a job seeker.

#### D3.2 Legal/ToS envelope (not legal advice)

| Zone | Examples | Basis |
|---|---|---|
| **Green — default** | Measure *public, documented* behavior with your own account, the documented API, at normal rates and within usage policies (latency, throughput, cost, rate-limit behavior, documented limits). Audit open-source components you run on your own hardware (vLLM, SGLang, Ollama, LiteLLM, Langfuse): performance, default-config security (unauthenticated endpoints, default binds), docs accuracy. Review public artifacts (docs, changelogs, status pages, model cards, public repos). | No access to anything you were not given; no circumvention. |
| **Amber — only with explicit scope, otherwise don't** | Jailbreak/prompt-injection/system-prompt-leak probing of *production* AI endpoints; high-volume automated extraction; testing hosts or endpoints you discovered but the vendor never published; anything touching other users' data. | OpenAI Usage Policies (effective 2025-10-29) prohibit "unsolicited safety testing" and "circumventing our safeguards" `L-05`; OpenAI EU Terms (updated 2026-01-16) bar reverse engineering, "automatically or programmatically extracting data or Output", and bypassing protective measures `L-06`; Anthropic's disclosure safe harbor covers its internet-facing systems but *excludes* "red-teaming or adversarial testing of models" `L-07`; its Model Safety Bug Bounty is invite-only with an NDA and no explicit safe harbor (page dated 2026-09-08) `L-08`. |
| **Red — never** | Using credentials, keys or tokens you find (including "just to check they work"); accessing non-public systems; bypassing authentication, rate limits or safeguards; exfiltrating data; load that could degrade service; publishing a vulnerability before the vendor has notice; implying you will disclose unless something happens (extortion). | DOJ's May 2022 CFAA charging policy covers only access "solely for purposes of good-faith testing, investigation, and/or correction of a security flaw" and excludes extortion `L-03`; WSGR: it "does not provide any concrete legal protections" and "arguably increases the likelihood of civil exposure" `L-04`; post-*Van Buren*, ToS-only violations are not to be charged by DOJ, but civil/contract exposure remains. |

Further context: (i) a 24-author paper argues AI developers' terms "discourage good-faith safety testing" and researchers fear "account suspensions or legal reprisal", proposing a safe harbor — which means none exists today `L-10`; (ii) as a norm for vulnerabilities, Google Project Zero uses 90 days (+30 if patched) and, since 2025-07-29, releases limited details within a week of vendor notification `L-11`; (iii) check `/.well-known/security.txt` (RFC 9116) for the vendor's disclosure route: `Contact`, `Policy`, and a `Hiring` field that links to security-related job positions `L-02`; (iv) **India:** IT Act s.43 penalises unauthorised access and "does not distinguish" malicious from ethical actors; CERT-In's disclosure policy (2021-09-03) Clause 7 requires reporters to "comply with all the extant laws and regulations while discovering the vulnerabilities"; the 2021 Mobikwik legal-threat case is the cautionary tale `L-12` (advocacy source from 2021; may be dated). *I am not a lawyer; jurisdiction, the target's terms and the exact method all matter.*

#### D3.3 Reproducible measurement recipes

*None of these were executed in this session (no GPU, no outbound access from the shell); they are documented practice, with sources for the method.*

**(a) Latency and throughput profile (TTFT / TPOT / ITL / E2EL).** Definitions used by vLLM's serving benchmark: TTFT = time to first token; TPOT = time per output token after the first; ITL = inter-token latency; E2EL = end-to-end latency; *goodput* = request rate that meets your latency SLOs (configurable via `goodput_config_dict`) `T-15`. Method guidance from Anyscale `T-14`: report mean, median and P99 of TTFT/TPOT/ITL; sweep request rate and concurrency; fix input/output lengths; warm up first; prefix caching inflates results; autoscaling skews tests. Protocol:

1. Fix a small grid of (input, output) lengths, e.g., 128/128, 1,024/256, 4,096/512 (my choice of grid).
2. Warm up and discard the first requests; then run ≥ 200 requests per concurrency level (my minimum) at 1, 4, 16, 32.
3. Randomize prompts, or state clearly that caching was on or off; note any autoscaling.
4. Record vantage point (region, client, network round-trip), model ID/version string, date and time; repeat at two times of day.
5. Report mean/median/P99 for TTFT, TPOT, ITL and E2EL, throughput vs P99-TTFT curves, and raw CSV.
6. For self-hosted engines, the serving benchmark is `vllm bench serve` (module `vllm.benchmarks.serve`); typical flags include a random dataset with input/output lengths, number of prompts, request rate, and percentile metrics. *Flags vary by version; confirm with `--help`.*

**(b) Leak detection (passive only).** (i) Scan the target's *public* repos, packages and images for committed secrets with a secret scanner (gitleaks and trufflehog are examples I recall; not verified here). (ii) If you find a live-looking credential, **do not use or validate it**; report privately through the vendor's disclosure route. (iii) Review your own client traffic and public docs for PII in telemetry, verbose errors and stack traces. (iv) For open-source components you run yourself, check default configuration: unauthenticated admin/API endpoints, default binds, permissive CORS, default credentials.

**(c) Prompt-injection / system-prompt-leakage audit.** Vocabulary: OWASP Top 10 for LLM Applications 2025 — LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM10 Unbounded Consumption (via a secondary source, `P-02`). Run it **only** on (1) an app you built, (2) a self-hosted open-source deployment, or (3) an asset explicitly in a vendor's disclosure scope. Template: threat model → test corpus (direct injection; indirect injection through documents or tool output; Markdown-image and allow-listed-domain exfiltration as in Rehberger's reports `C-02`) → success criteria (data exfiltration, unintended tool call, instruction override) → full logging → mitigations (least privilege, human confirmation for sensitive tools, output sanitization, tightening egress allow-lists).

**(d) Cost/quality audit of an LLM feature.** Token counts per request versus what the provider bills; cache-hit behavior; structured-output failure rate on a public eval set; for retrieval-augmented features, retrieval hit rate on a documented corpus. Always against public models/documented behavior.

**(e) Gateway/observability parity audit (own instance).** Run LiteLLM or Langfuse yourself; compare traced token/cost accounting against provider-reported usage on a fixed prompt set; report missing or mismatched fields; offer the fix as a PR. *This is my suggestion, not a documented case;* it is legally the cleanest bridge between Tactic 1 and Tactic 2 for the target repos.

#### D3.4 Micro-audit template and execution rubric

**Template (≤ 2 pages; send privately for company-specific notes):**

```markdown
# [Target] — [aspect] micro-audit, v1 (YYYY-MM-DD)
**Scope and ethics.** What I tested / did not test; own account; documented endpoints; request volume; no PII; no circumvention; nothing non-public.
**TL;DR** (≤ 3 bullets, each with a confidence word: observed / likely / unknown).
**Setup.** Model/version, region, client, concurrency levels, input/output lengths, warm-up, repetitions, date and time window, caching/autoscaling notes.
**Results.** One table + one chart: mean / median / P99 (TTFT, TPOT, ITL, E2EL), N per cell.
**Interpretation and limits.** What this does *not* show; what I cannot see from outside.
**Suggested fixes.** 2–3, ranked by effort and impact; "I can send a patch for #1."
**Reproduce.** Repo link, commit hash, one command, raw CSV.
**Disclosure status.** Private notice date; response; planned public date (category-level only).
**About me.** Two lines and three links (PRs, write-ups, profile).
```

**Execution rubric (100 points; pass = ≥ 75 *and* the safety gate).** Weights are my judgment (Grade D); the dismissal triggers come from the negative cases in D3.1.

| Criterion | Points | Full marks looks like |
|---|---|---|
| Relevance to the team's problem | 20 | Names a problem on the team's public roadmap, issues or job posting; not a generic critique |
| Measurement validity and reproducibility | 20 | Fixed inputs, warm-up, percentiles, N stated, confounders controlled (caching, autoscaling), one-command repro, raw data |
| Claim calibration | 15 | "Observed / in my setup / could not verify"; no claims about internals; explicit limits |
| Actionability | 15 | Two or three ranked fixes; offer of a patch; effort/impact stated |
| **Safety and legal (gate)** | 15 | Green zone only; scope statement; no PII; no credentials; private notice for any vulnerability. **Any red-zone item = automatic fail** |
| Concision | 10 | ≤ 2 pages; TL;DR first |
| Credibility | 5 | Two-line bio, consistent identity, no hype |

**Automatic dismissal triggers (any one):** a factual error about the target; unreproducible numbers; a method that violates the target's terms; a "gotcha" or shaming tone; publication of a vulnerability before notice; unverified AI-generated claims; more than three pages; no next step; no disclosure statement.

**Claim-hygiene phrasebook** (adapted from `V-01`): "In my setup, X was observed"; "I could not verify what I tested"; "This may reflect a configuration I cannot see"; "I will re-run when [version] is available."

#### D3.5 Delivery protocol

1. **Pre-flight.** Read the target's terms and usage policy and any disclosure policy; fetch `/.well-known/security.txt` (RFC 9116) for `Contact` and `Policy` `L-02`. If the method is amber or red, stop.
2. **If you found a vulnerability:** report privately first; wait for acknowledgement; treat 90 days (+30 if patched) as the reference norm, not a right `L-11`; Anthropic's policy forbids public disclosure without prior written notice `L-07`. Never publish exploit details first.
3. **If it is performance or quality:** send the note privately to the engineering lead *before* anything goes public. This lowers the risk of a factual error and gives the target a chance to respond (my recommendation, Grade D).
4. **Publish only category-level artifacts** (a vendor-neutral benchmark of several providers or open-source engines). Keep company-specific notes private and use them as the outreach artifact. This limits reputational and legal exposure.
5. **Attach to outreach** using script S1 (D4.5); log the send.

### D4. Tactic 3 — Targeted outreach to engineering directors and founders

#### D4.1 Targeting

- **Who.** The person who *owns the problem your artifact addresses*: the director/manager of that team, or the founder at ≤ ~50-person companies (Inferact's posting lists 11–50 employees `W-05`). Not `careers@`, not a random recruiter. Build 30–40 targets from (i) open roles at T1–T2 companies, (ii) maintainers and committers named in public governance files, (iii) OSS Insight company tables, (iv) manual LinkedIn title searches.
- **Explicit invitations exist.** Artificial Analysis's careers page lists 16 roles (including MTS Inference, MTS Language Model Evaluations and a Forward Deployed Engineer for language models) and says: "If you're interested in working with us but don't quite fit the listed roles, please still reach out." Its process is four stages (Initial Connect → technical round or case study → Culture & Fit → Final Round) and it states no open-source, portfolio or resume policy `C-03`.
- **Heuristics (Grade C, author's guidance, no sample).** interviewing.io advises targeting managers rather than VPs, particularly those under two years in role, emailing a work address, asking for a conversation, not attaching a resume, and including three components: common ground, proof, call to action `F-09`.
- **Second-degree routes.** The 2022 *Science* study of ~20M LinkedIn users found moderately weak ties (inflection ≈ 10 mutual connections) transmit jobs best, especially in digital industries `J-03`. Use it as a tiebreaker for who to ask for an introduction.
- **Sequence.** Apply through the normal channel first, then message within 24–48 hours referencing the application so the manager can find and flag it. (Unmeasured; the DearHiringManager sample shows people contacted before or around the application 16 times, after applying but before an interview 28, after an interview or late in the process 18, after a rejection 12 (5 other), but the page itself says "This distribution is not a test of which moment works best" `J-01`.)

#### D4.2 Tool catalog

| Tool | Role in this workflow | Price (source, grade) | Limits and risks | Verdict at ≤ 30 sends/week |
|---|---|---|---|---|
| Apollo.io | Prospect and email lookup | Free $0 (1,200 email credits/yr); Basic $49/mo annual; Professional $79; Organization $119; overage $0.20/credit (Docket roundup, "verified April 2026") `T-06` C | Not in Pin's email-finder audit; LinkedIn removed its company page 2025-03-06 `L-13`; its claim that 3–6% is a good reply rate for broad B2B email is unsourced `F-04` | Free tier for lookups only |
| Hunter.io | Domain email finder/verifier | Free 50 credits/mo; Starter $34/mo annual (2,000 credits); Growth $104; Scale $209 (MarketBetter, verified Sept 2026) `T-07` C | Not in Pin's audit | Free tier + manual verification |
| RocketReach | Contact lookup | Essentials $329/yr (1,200 exports, email only); Pro $829/yr (3,600); Ultimate $1,699/yr (20,000); team from ~$6,000/yr; overage $0.30–0.45; 5 free lookups (SalesIntel, a competitor; updated 2026-09-29) `P-01` C | Lowest find rate in Pin's audit (29.8%) vs vendor claims of 90–99% `T-12`; the source page is internally inconsistent on "unlimited" | Skip |
| Clay | Enrichment/workflow orchestration | Free 100 Data Credits + 500 Actions; Launch $185/mo annual; Growth $495; Enterprise from ~$30K/yr (Docket, March 2026 overhaul) `T-08` C | Built for GTM teams; credit economics | Skip |
| PhantomBuster | LinkedIn automation | Not retrieved | Vendor guidance ~50–100 connection requests/week to start; "Paid plans don't remove invitation limits" `T-10`; platform-restriction risk `L-13` | Avoid |
| LinkedIn Premium / Sales Navigator | Title/tenure search filters; InMail credits | Premium Career $39.99/mo (5 InMails); Business $69.99 (15); Sales Navigator Core $119.99 (50); Advanced $159.99 (50); Recruiter Lite $170 (30) (Evaboot, updated 2026-09-13) `T-09` C | InMail is a recruiter-style channel; no data that candidate InMail beats artifact email | Optional: one month only if you need tenure/title filters |
| GitHub GraphQL API | Research: who commits where, and when | Free; 5,000 points/hr/user; 500,000-node limit per call; secondary limits of 100 concurrent requests, 2,000 points/min for GraphQL, 80 content-creating requests/min; 10 s timeout `T-04` A | AUP §7 bars using results to send unsolicited emails `L-01`; my snippet is untested (token invalid in this session) | Research only |
| OSS Insight | Breakdowns of PR creators, issue creators and stargazers by company and geography; "5+ billion rows of GitHub events data"; Data Explorer; public API `T-05` A | Free | Aggregates; employer inferred from public profile data | Use for repo/employer selection |
| `git log` on a treeless clone | Local, unmetered author-domain counts (what I used) | Free | Counts commits, not PRs; noreply hides employers | **Preferred** for repo research |

*Untested GraphQL sketch (schema recalled, not run):*

```graphql
query($owner:String!, $name:String!, $since:GitTimestamp!, $after:String) {
  repository(owner:$owner, name:$name) {
    defaultBranchRef { target { ... on Commit {
      history(since:$since, first:100, after:$after) {
        pageInfo { hasNextPage endCursor }
        nodes { committedDate author { user { login company } } }
      }
    } } }
  }
}
```

*Tested local alternative (ran on the vLLM clone this session):*

```bash
git clone --filter=tree:0 --no-checkout --single-branch https://github.com/<org>/<repo>.git
cd <repo> && git log --no-merges --since="12 months ago" --format='%aE|%aN|%aI' \
  | awk -F'|' '{n=split($1,a,"@"); if(n>1) print a[2]}' | sort | uniq -c | sort -rn | head -20
```

Use both for *aggregate research* (which employers staff a repo; who owns which area). Do not turn the output into an email list: GitHub's Acceptable Use Policy §7 bars using information from the service "for the purposes of sending unsolicited emails to users" `L-01`. Reach people through channels they publish for professional contact.

#### D4.3 Staging and deliverability protocol

1. **Authenticate.** SPF and DKIM on the sending domain, plus DMARC. Google requires SPF/DKIM for all senders and adds DMARC and one-click unsubscribe for bulk senders (> 5,000/day to Gmail), with spam-rate guidance of < 0.10% and never ≥ 0.30% `T-01` (secondary: Mailsuite, 2024-07-23). Microsoft applies similar requirements to senders of > 5,000 emails/day from 2025-05-05, routing non-compliant mail to Junk first and rejecting later `T-02` (secondary: Petri, 2025-04-07). At job-seeker volume these thresholds do not formally apply; authentication is cheap hygiene that prevents misrouting (Grade D inference).
2. **Prefer an established mailbox for early sends.** If you use a new domain, follow the vendor ramp: 5–10 per day for 4–6 weeks `F-03` (Instantly; cold-sales context, Grade B).
3. **Verify every address** and keep bounces < 2% `F-03`. Prefer addresses the person publishes for contact; do not pattern-guess in bulk. Independent-style audit data show finder accuracy is far below vendor claims `T-12`.
4. **Complaints.** At 30 emails/week a single spam report is ~3% of a week's sends; the formal 0.10%/0.30% thresholds target bulk senders, but a complaint still damages a small sender's reputation (Grade D inference). Make the message easy to ignore: "No reply needed if this isn't relevant."
5. **Content.** Plain text; ≲ 80–90 words (Instantly's best first touches are under 80 words `F-03`); one link; no attachments; vary wording per recipient. Avoiding tracking pixels and link shorteners is common deliverability practice that I did not verify here (Grade D).
6. **Cap and ramp.** 10 → 15 → 20 → ≤ 30 per week over four weeks, counting follow-ups.
7. **Stop conditions.** Bounce rate > 2% over ≥ 50 sends → pause and clean the list; any spam complaint or hostile reply → stop contacting that domain and review the template; never re-approach someone through another channel after an explicit no.
8. **LinkedIn: manual only.** PhantomBuster's own numbers (50–100 requests/week to start; acceptance target 40–60%; paid plans do not lift limits) `T-10` and LinkedIn's removal of Apollo's and Seamless.ai's company pages on 2025-03-06 `L-13` mean automation adds restriction risk without evidence of benefit at ≤ 30 contacts/week.
9. **Log everything** in a CSV: date, target, channel, artifact, reply, loop, outcome. That log is the only source of a *real* response rate for your situation.

#### D4.4 Response-rate benchmarks and stop rules

| Dataset | Direction / population | Result | Method / size | Grade | Transfer to candidate → manager |
|---|---|---|---|---|---|
| Pin `F-01` | Recruiter → candidate | Automated email 4.96%; recruiter-written email 6.31%; LinkedIn message 17.08%; engineering & data 4.64% (PM 9.94%, healthcare 2.81%); first name in message 5.13% vs 2.61% without; email by step 5.52 / 5.40 / 4.21 / 3.34 / 2.93%; 3 touches = 93.2% of replies | 4M+ messages, 1,500+ orgs, 2025-06-01 → 2026-05-31; reply in thread / delivered | B | Direction reversed; useful for step shape and the engineering-reply penalty |
| Instantly `F-03` | Cold B2B sales email | Average 3.43%; top quartile 5.5%+; top decile 10.7%+; < 80 words; 58% of replies from step 1; bounce < 2% | Billions of interactions, 2025-01-01 → 2025-12-18 | B | Not hiring; best public volume benchmark for cold-email mechanics |
| Apollo `F-04` | B2B | 3–6% called a good rate for broad B2B email (no source); cites Belkins 5.8% (16.5M emails, 2024), Sales.co 2.09% reply / 14.1% positive (2M+, Feb 2026), Cleverly 3.43% | Vendor marketing | C | Low |
| Instantly and Saleshandy, as cited by PitchHired `J-02` | B2B | 3.4–3.7% average; Saleshandy: sequences under 200 prospects get ~2× the replies of large blasts, and follow-ups account for ~44% of positive replies | Saleshandy analysis of 53M emails, Jan–Jun 2026 (secondary; methods not described) | B/C | Suggests small, targeted lists beat blasts |
| interviewing.io `F-09` | Candidate → hiring manager | 25–50% personalized (targets with an online presence); 5–25% generic LinkedIn-only | **Author's estimates, no sample** | C | Unverified |
| PitchHired `J-02` | Candidate → hiring manager | "5% to 15%" planning range | **Author's estimate, no source** | C | Unverified |
| DearHiringManager `J-01` | Candidate → hiring manager (public accounts) | No reply rate; 79 outcomes, 43 reached an interview or beyond ("not an effectiveness rate") | Non-random, self-selected, unverified, vendor-run | C | Not usable as a rate |
| Gem email-outreach benchmarks `F-02` | Recruiter outreach | Gated; no rates visible | 6.2M sequences / 15.5M messages in 2025 | — | — |

**Planning range used in this file: 3–8% reply for artifact-carrying notes to *named* leaders; 10%+ is a stretch.** Rationale: it sits at or above Instantly's average and top-quartile cold-email rates (3.43%; 5.5%+) and brackets Pin's engineering reply (4.64%) and recruiter-written email (6.31%) rates. It is a judgment (Grade D); no verified candidate-side measurement exists.

**Stop/pivot table (computed by `model_checks.py`; 95% Clopper–Pearson intervals for the true reply rate).**

| Replies after 60 sends | Observed | 95% interval | Action |
|---|---|---|---|
| 0 | 0% | 0–6.0% (one-sided 95% upper bound 4.9%) | Stop this template; change the artifact or the targeting before sending more |
| 1 | 1.7% | 0–8.9% | Tighten the message and targets; continue |
| 2 | 3.3% | 0.4–11.5% | Continue; inside the planning range |
| 3 | 5.0% | 1.0–13.9% | Continue |
| 5 | 8.3% | 2.8–18.4% | Continue; cap stays at 30/week |
| 8 | 13.3% | 5.9–24.6% | Above plan; check whether warm contacts inflated it |

After 30 sends the intervals are wide: 0 replies → 0–11.6%; 1 → 0.1–17.2%; 2 → 0.8–22.1%; 3 → 2.1–26.5%. At p = 5%, the chance of at least one reply in 20 sends is 64.2% (45.6% at 3%; 81.1% at 8%); in 60 sends it is 95.4% (83.9% at 3%; 99.3% at 8%). **Consequence:** at ≤ 30 sends/week you cannot A/B test message variants; change one thing between 30-send batches and judge by *quality of loops*, not small differences in reply rate.

#### D4.5 Scripts

*No verified reply or loop rate exists for these exact scripts.* They implement what the (verified) cold-email benchmarks and the (unverified) job-seeker guidance agree on: short, one specific ask, one link, relevant to the recipient's problem, easy to forward or ignore. Replace every bracket; delete anything you cannot back with a link.

**S1 — artifact-first note to an engineering director (email, ≈ 85 words with greeting and signature; ≈ 78 in the body).**

> Subject: [Product]: reproducible TTFT numbers on [documented endpoint]
>
> Hi [First name] —
>
> I'm [Name], an inference/serving engineer. I benchmarked [documented endpoint] on my own account: fixed prompt lengths, 200 requests per concurrency level. In my setup, p99 TTFT was [X]× p50 at concurrency 16. Method, raw CSV and one-command repro: [link].
>
> I can't see your infrastructure, so this may reflect a setting I'm unaware of. I have two ideas for [specific fix] and can send a patch.
>
> I'm looking for [role/area]; if you're the wrong person, a pointer would help.
>
> [Name] · [PR or profile link]

**S2 — leader or founder note citing OSS work (email, ≈ 70 words with greeting and signature).**

> Subject: [repo] #[PR] — [one-line result]
>
> Hi [First name] —
>
> I've been working on [repo]: [PR link] ([what it fixed], [measured result]), and I reviewed [PR link]. I use [feature] in [project] and noticed [specific gap tied to a public issue or roadmap item]. Write-up with numbers: [link].
>
> I'd like to work on [area] full-time. Are you hiring for it, or is there someone on the team I should talk to?
>
> [Name] · [GitHub] · [site]

**S3 — maintainer scope check (GitHub issue comment; not a job request).**

> Before I start on #[N]: I reproduced [bug] on [version/commit] (repro: [link]) and bisected it to [commit]. Plan: [1–3 bullets]; test: [what]. Is this in scope, or does someone have a branch? AI use: [none / assisted; every line reviewed and run by me]. Happy to follow your preferred approach.

**S4 — follow-up at day 5–7.**

> Hi [First name] — one nudge in case this got buried: [one-line recap + link]. If it isn't relevant, no reply needed. Thanks for reading.

**S5 — second-degree introduction request.**

> Hi [First name] — we share [N] connections ([names]). I admire [specific work]. I built [artifact] aimed at [team]'s [problem]: [one-line result + link]. Would you be open to forwarding it to [Name], or pointing me to the right person? I can send a three-line blurb you can paste.

#### D4.6 Cadence

First touch → one follow-up at day 5–7 (S4) → stop. Pin: reply rate falls from 5.52% (step 1) to 5.40%, 4.21%, 3.34%, 2.93% (steps 2–5), and three touches account for 93.2% of replies `F-01`; Instantly recommends 4–7 touches for sales sequences and finds 42% of replies come from follow-ups `F-03`. For a job seeker contacting a specific named person, I recommend **two touches in total** because further touches add little and raise the etiquette risk (judgment, Grade D).

### D5. Failure modes and etiquette violations (catalog)

| # | Failure / violation | Where | Evidence | Mitigation |
|---|---|---|---|---|
| F1 | Agent-written or "pure agent" PRs | OSS | vLLM: "Pure code-agent PRs are **not allowed**… automatic banning" `E1-05`; transformers: closed without review, repeat offenders may be blocked `E1-08`; llama.cpp: permanent ban for undisclosed AI `E1-09`; Axolotl agent file refuses profile-credit PRs `E1-13` | Write and run the code yourself; disclose assistance as each repo requires |
| F2 | Profile-padding, "contribution farming", busywork and typo PRs | OSS | Axolotl `E1-13`; transformers "busywork… given the current flood" `E1-08`; vLLM no one-off typo PRs `E1-05`; llama.cpp no trivial fixes `E1-09` | Take bugs/performance/security with a reproducer; state your real use case |
| F3 | Undisclosed AI use | OSS | llama.cpp ban `E1-09`; vLLM "Disclose in PR" `E1-06`; Axolotl AI-usage disclaimer in PR template `E1-13` | Disclose every time |
| F4 | Feature PR before an issue / no prior discussion | OSS | llama.cpp "Features must begin with an issue, not a PR" `E1-09`; Ollama and Langfuse issue-first `E1-10, E1-12` | Open the issue; post a scope check (script S3) |
| F5 | Ignoring PR caps | OSS | llama.cpp new contributors limited to 1 open PR `E1-09`; GitHub's open-PR cap for non-write users from 2026-06-17, AI-agent PRs counted, drafts exempt `L-15` | One PR at a time; use drafts |
| F6 | Assuming CI/merge permissions | OSS | SGLang: no write access; CI only triggered by trusted contributors via `run-ci` `E1-07` | Ask for the label; plan for waiting |
| F7 | Missing tests, CLA or DCO | OSS | LiteLLM CLA mandatory and ≥ 1 test a "hard requirement" `E1-11`; vLLM DCO `E1-06`; llama.cpp regression test for bug fixes `E1-09` | Pre-submit checklist |
| F8 | AI-written posts and comments | OSS | llama.cpp: "strictly prohibited to use AI to write your posts for you" `E1-09` | Write your own words |
| F9 | Asking for a job inside issue/PR threads | OSS | **Not sourced** (norm inferred from the off-topic and AI-post rules above; Grade D) | Keep threads technical; take hiring conversations to email/DM with the PR as evidence |
| F10 | Event-driven PR bursts | OSS | Hacktoberfest 2026 no longer counts PRs toward rewards; its own page says low-effort and AI PRs are "easier than ever" to generate `X-01` | Do not time contributions to events |
| F11 | Harvesting emails from GitHub for unsolicited contact | Outreach | GitHub AUP §7 `L-01` | Use channels people publish for professional contact |
| F12 | LinkedIn automation or scraping | Outreach | Apollo and Seamless.ai disappeared from LinkedIn 2025-03-06, no LinkedIn statement `L-13`; PhantomBuster's own limits `T-10` | Manual only |
| F13 | Unauthenticated sending; high bounce rate | Outreach | Google/Microsoft sender rules (secondary) `T-01, T-02`; bounce < 2% `F-03` | SPF/DKIM/DMARC; verify addresses |
| F14 | Generic target or generic message | Outreach | First name in message 5.13% vs 2.61% without `F-01`; small targeted sequences ~2× replies of blasts (secondary) `J-02` | Named owner of the problem; one specific artifact |
| F15 | Long, multi-ask first touch | Outreach | Best first touches < 80 words; 58% of replies from step 1 `F-03` | Short, one ask, one link |
| F16 | Over-following-up | Outreach | Reply rate falls by step (5.52 → 2.93%) `F-01` | Two touches in total |
| F17 | Trusting email-finder accuracy claims | Outreach | Pin audit: 29.8–55.2% find rates vs 90–99% claimed `T-12` | Verify before sending |
| F18 | Factual errors from black-box inference | Audit | Reflection 70B's claims were contested in public within days; the evaluator's cautious wording (it said it could not verify what it had tested) was consistent with later events, including the developer's apology on 2024-09-10 `V-01` | Caveats, reproducibility, private pre-send |
| F19 | Unsolicited safety testing or jailbreaking of production AI | Audit | OpenAI Usage Policies `L-05`; o1 probing warning emails `L-09`; Anthropic safe harbor excludes model red-teaming `L-07` | Own-instance or sanctioned scope only |
| F20 | Automated extraction or circumvention of safeguards | Audit | OpenAI EU Terms `L-06` | Normal rates, documented API |
| F21 | Publishing a vulnerability before notice | Audit | Anthropic: no public disclosure without prior written notice `L-07`; Project Zero norm 90 + 30 `L-11` | Private first |
| F22 | Using found credentials | Audit | DOJ policy covers access "solely" for good-faith testing; WSGR: no concrete protection `L-03, L-04` | Never use or validate; report |
| F23 | "Gotcha" or shaming tone | Audit | curl's maintainer says he will keep publicly shaming "silly" submissions `L-14` | Claim-hygiene phrasebook (D3.4) |
| F24 | Low-effort AI-generated audit reports | Audit | curl ended its bounty over "crap and non-well researched reports… AI generated or not" `L-14`; GitHub: "The cost to create has dropped but the cost to review has not" `L-15` | Understand and reproduce before sending |
| F25 | Local legal exposure (India) | Audit | IT Act s.43 does not distinguish ethical researchers; CERT-In Clause 7; Mobikwik legal threat `L-12` (2021, advocacy source) | Written permission or a vendor disclosure policy; route through CERT-In where applicable |

### D6. Time-investment vs offer-yield (model; Grade D)

**Purpose.** No source publishes offer-yield per hour for any of these tactics. This model makes the assumptions explicit so you can see (i) what you would have to believe for each tactic to beat standard applications, and (ii) that no plausible parameter set gives the claimed ~10× per-hour advantage. It was computed with `model_checks.py` (arithmetic only; not run on data).

**Parameters (per attempt).** *Sourced* anchors are in the last column; everything else is **assumed**.

| Parameter | Pessimistic | Base | Optimistic | Anchor or status |
|---|---|---|---|---|
| Mass Easy Apply: minutes per application | 6 | 4 | 3 | Assumed |
| Mass Easy Apply: P(offer) per application | 0.03% | 0.10% | 0.20% | Assumed; upper anchor Ashby inbound application→offer 0.2% (Q4 2024, all roles) `F-06`; Gem 0.5% application→hire `F-05`. Assumes GenAI roles convert at or below the all-role average (no source) |
| Pool of suitable openings reachable per quarter | 300 | 300 | 300 | Assumed |
| Tailored application: minutes | 30 | 20 | 15 | Assumed |
| Tailored application: P(offer) | 0.05% | 0.15% | 0.30% | Assumed (0.25–1.5× the Ashby 0.2% anchor) |
| Outreach: minutes per target (research, write, verify, follow-up) | 60 | 45 | 30 | Assumed |
| Outreach: reply rate | 2% | 5% | 10% | Anchors: Instantly 3.43 / 5.5+ / 10.7+% `F-03`; Pin 4.64–6.31% `F-01`; PitchHired 5–15% (unsourced) `J-02` |
| P(interview loop \| reply) | 25% | 40% | 60% | Assumed; only anchor is Ashby sourced application→interview 25% `F-06` |
| P(offer \| loop) | 6% | 10% | 16% | Anchors: Ashby inbound 6%, referral 16% `F-06` |

**Results (expected offers per 100 focused hours).**

| Strategy | Pessimistic | Base | Optimistic | Notes |
|---|---|---|---|---|
| Mass Easy Apply, uncapped | 0.30 (1,000 apps) | 1.50 (1,500 apps) | 4.00 (2,000 apps) | **Not attainable**: the pool of openings is finite |
| Mass Easy Apply, capped at the 300-opening pool | 0.09 total, saturating after ~30 h | 0.30 total, ~20 h | 0.60 total, ~15 h | Hours beyond saturation have ~zero marginal yield |
| Tailored applications | 0.10 (200 apps) | 0.45 (300 apps) | 1.20 (400 apps) | |
| Artifact-carrying outreach | 0.03 (100 contacts → 2.0 replies → 0.5 loops) | 0.27 (133 → 6.7 → 2.7) | 1.92 (200 → 20 → 12) | P(offer) per contact 0.03% / 0.20% / 0.96% |

**What the model says.**

1. **No scenario gives outreach a 10× per-hour edge over standard applications.** At base, outreach (0.27) is below tailored applications (0.45); only in the optimistic case does it exceed them (1.92 vs 1.20, i.e., 1.6×).
2. **The structural case for unconventional tactics is saturation, not a multiplier.** Mass-applying is cheap per hour but exhausts the pool within ~15–30 hours; beyond that, extra hours should go to the next-best channel. This is why the recommended split spends ~25 hours on standard applications and the rest elsewhere.
3. **Break-even on the baseline.** Outreach beats tailored applications per hour only if the target tier's tailored-application P(offer) is below ~0.089% (0.27 offers ÷ 300 applications), i.e., less than ~45% of Ashby's all-role 0.2%. For T1/T2 GenAI roles with heavy inbound that is plausible but unverified; the "10×" claim implicitly assumes the baseline is ≈ 0.
4. **OSS sprint (100 hours).** With an assumed direct yield of ~0.013 offers per 100 hours (0.5 × 0.25 × 0.16 over a ~150-hour sprint; all assumed), a 100-hour sprint inside a 400-hour search year must raise the effectiveness of the remaining 300 hours of outreach by **≥ 32%** to break even (for example, reply 5% → 6.6%, or loop-per-reply 40% → 53%). Plausible if OSS credibility moves replies or loops; unmeasured. Latency is also long: ~8–16 weeks to a merged non-trivial PR in a vLLM-class repo (one documented case, `O-01`).
5. **Micro-audit artifacts.** A company-specific audit (12 hours for one target) needs a **~17×** multiple on that target's offer probability (0.20% → 3.4%) to pay back at base: only justifiable for top-priority targets, or when the audit is also reused in the application. A category-level artifact (12 hours amortised over 20 targets) needs **~1.8×** (0.20% → 0.36%), roughly an 80% lift in reply/loop conversion: feasible if the artifact is good.

**Sensitivity of base outreach yield (0.27 offers/100 h).** Reply 3% instead of 5%: 0.16 (−40%). Loop-per-reply 25% instead of 40%: 0.17 (−38%). P(offer | loop) 16% instead of 10%: 0.43 (+60%). 30 minutes per target instead of 45: 0.40 (+50%). The yield is most sensitive to reply rate and loop-per-reply, which are the two least-measured parameters.

**What the model leaves out.** Offer quality (compensation, tier, learning), finite targets inside outreach (30–40 named leaders), channel complementarity (an application plus a champion looks like a referral: Ashby's referral offer rate is 7.3% vs 0.2%), fraud filters on inbound, time-zone, visa and location constraints, and correlated failures (a weak artifact hurts every message that carries it).

### D7. Strongest expert objections, with evidence for and against

| # | Objection | Evidence for | Evidence against | Net |
|---|---|---|---|---|
| O1 | *OSS advocate:* "OSS is the one non-gameable signal; maintainers vouch; you underrate it." | Hugging Face requires merged PRs `W-07`; Inferact, RadixArk, Red Hat postings prefer or require contributions `W-05, H-02, W-08`; 30 vLLM identity transitions `E2`; OSS rank is associated with wage gains (Apache-era evidence) `A-02` | 49–82% of identities stop at one commit; low newcomer retention; bar rising (agent bans, PR caps); no named contributor→hire case found `E2, O-04`; signaling-motivated contributions are increasing, so the signal is crowded `A-01` | Agree it is the hardest to fake and the best artifact generator; the evidence supports *sustained* contribution, not one PR |
| O2 | *Skeptic:* "Cold outreach is spam, and your 3–8% is too optimistic for engineers." | Engineering & data replies are 4.64% in Pin's recruiter data `F-01`; Instantly average is 3.43% `F-03`; no candidate-side data; the public-account study is self-selected `J-01` | Small targeted lists get ~2× replies (secondary) `J-02`; name personalization doubles reply in Pin's data `F-01`; stop rules cap the cost of being wrong (D4.4) | The range is a judgment and could be off by 2×; the pivot table makes the error cheap |
| O3 | *Security/legal:* "Audits of AI products are risky and unwelcome; a job seeker has no safe harbor." | OpenAI and Anthropic terms `L-05…L-07`; DOJ caveats `L-04`; no safe harbor exists `L-10`; India s.43 `L-12` | Green-zone work (documented API, own account, own-instance OSS) is routine; the positive cases are of this type `V-01, C-02` | Agree; that is why the plan restricts audits to the green zone and keeps company-specific notes private |
| O4 | *Recruiting-ops:* "Referrals dominate; cold tactics waste hours." | Ashby referral 40% vs 3% application→interview `F-06`; Gem referrals 11× `F-05` | You need a path to a referral; weak-tie evidence says structured outreach to second-degree contacts is how introductions originate `J-03`; no data on how cold contact converts to referral | Use referrals whenever available; the tactics are how to create them |
| O5 | *Data skeptic:* "Commit stats cannot measure hiring; commit ≠ PR; employees inflate cohorts." | True: no merge rates, squash attribution, multi-email people, domain lower bounds (D0) | Single-commit shares move ≤ 3 points under name-merging; employee inflation means true newcomer retention is *lower* than shown | Conclusions on base rates and bars stand; there is no hiring-causality claim |
| O6 | *Methodologist:* "The time-vs-yield model is invented." | Most parameters are assumed (D6) | It is used only for break-evens, the saturation argument and to show no scenario yields 10×; the stop rules and week-8/12 gates do not depend on it | Treat as Grade D |
| O7 | *Selection bias:* "Gem, Ashby, Pin and Instantly describe their own customers." | Tech-forward ATS customers; recruiter direction; sales email | Only large-n public data available; direction of bias unknown | Used as graded anchors, flagged in D1 |
| O8 | *Scope:* "The tier mapping is arbitrary and frontier labs are not covered." | Frontier-lab hiring practices were not researched beyond the policies in the ledger | The recommendation's mechanism (named human → loop) does not depend on the tier labels | Open question |

### D8. DONE-criteria self-check

| Criterion | Status | Where | Gap |
|---|---|---|---|
| OSS contributor→hire pipeline documented with target repos and qualification criteria | Met in structure; thin on named cases | D2.1–D2.6; Findings 3–6 | No verified named contributor→hire case; hiring text for Ollama and Axolotl not found |
| Concrete micro-audit template and execution rubric | Met | D3.3–D3.5 | Recipes documented, not executed (no GPU/outbound access) |
| Outreach conversion benchmarks and scripts with verified response rates | **Partly**: benchmarks are verified as published (Pin, Instantly, Gem, Ashby) but adjacent; no rate exists for the scripts | D4.4–D4.5 | No candidate→hiring-manager measurement exists in accessible sources; the planning range is judgment |
| Failure modes and etiquette violations cataloged | Met | D5 | — |
| Time-investment vs offer-yield comparison | Met as a model (Grade D) | D6 | Parameters assumed; no published per-hour measurement |

*Status rationale:* marked `complete` because every deliverable exists and every gap is named; the one partly-met criterion is limited by the absence of public data, not by unfinished work.

## Open Questions & Risks

**Open questions (what would change the answer, and the cheapest way to close each).**

1. **Named contributor→hire cases.** Searched for documented "merged PR → hired" cases for vLLM, SGLang, Ollama, LiteLLM, Langfuse and Axolotl (including an extended search and the contributor stories I could fetch) and found none; the closest items are a contributor story with no job outcome `O-01`, a community-stories post with no hiring causation `O-02`, and a Red Hat profile of someone hired via an acquisition `W-09`. *Closing it:* ask Inferact, RadixArk, Hugging Face and Red Hat hiring managers for anonymized counts of hires who were prior contributors, or run a consent-based survey of committers.
2. **Candidate→hiring-manager reply and loop rates by artifact type.** Unmeasured in every source I could reach. *Closing it:* your own randomized log (D4.4, D6); a job-seeker platform dataset if one exists.
3. **GenAI-specific application→offer rates by employer tier.** Unpublished; this is the model's central uncertainty (D6).
4. **Frontier-lab hiring practices** (OpenAI, Anthropic, Google DeepMind, Meta and others) were not researched beyond the policy texts in the ledger; T1 conclusions rest on Inferact, RadixArk and Hugging Face.
5. **Location and work authorization.** Most postings found are US-located (Palo Alto, San Francisco, "US Remote"); your eligibility was not assessed.
6. **Privacy and anti-spam law for cold email** (GDPR, India's DPDP Act, CAN-SPAM) was not researched; the file covers platform rules (GitHub AUP, LinkedIn) only.
7. **Ollama and Axolotl hiring text** was not found (the Ollama aggregator listing showed no requirements; its Ashby postings were not read) `H-03`.
8. **Tier definitions** (T1–T4) are my assumption.
9. **Primary pages not retrieved**, so secondary sources were used and flagged: Google's sender-guidelines page and Microsoft's announcement (T-01, T-02), the DOJ policy (L-03), owasp.org (P-02), and the Hann et al. page title (A-02).
10. **Search-only leads** (titles/URLs seen, not read, not used as evidence): Flynn & Lake (2008) "If you need help, just ask" (Cornell eCommons; Stanford GSB summary); Stanford HAI, "Safeguarding Third-Party AI Research" (https://hai.stanford.edu/policy/safeguarding-third-party-ai-research); HeroHunt "Recruiting Outreach Benchmarks 2026"; BleepingComputer/Orca/NetSPI coverage of the LiteLLM compromise; a gitconnected post on a first four vLLM PRs; topgenaijobs "Open-Source LLM Careers"; the body of The Wire article `C-01`.
11. **Mirror postings.** The Inferact and Red Hat postings were read on job-board mirrors, not the companies' own ATS pages `W-05, W-08`.
12. **Staleness.** Repo AI-contribution rules, GitHub maintainer controls and tool pricing changed within months; my repo reads are pinned to 2026-10-21 and the prices are third-party roundups.

**Risks of acting on this file.**

- **Legal and ToS (audits).** Active probing of production AI endpoints can breach usage policies and may carry CFAA or local-law exposure; no safe harbor exists `L-04, L-10`. The green-zone envelope in D3.2 is a risk reducer, not legal advice.
- **Reputational (audits and outreach).** A factual error in a public teardown, or a mass-looking email, can close doors at exactly the companies you want.
- **Platform risk.** LinkedIn restricts automation; GitHub or a maintainer can ban accounts for agent-written or undisclosed-AI PRs `E1-05, E1-09, L-13`.
- **Opportunity cost and sunk cost (OSS).** ~4 months to a merged PR in one documented vLLM case `O-01`; the week-8 and week-12 gates exist to stop that.
- **Model risk.** The time-vs-yield figures are arithmetic on assumed inputs; do not quote them as measurements.
- **Evidence risk.** Success stories are survivors; vendor datasets describe vendors' customers; the commit statistics cannot show causation.
- **Process risk in this session.** A usage limit killed the first parallel research attempt; the final evidence base was built sequentially and some leads were left unfetched (item 10).

## Delta

**How my beliefs changed.** Priors are scored first; recalled facts follow.

| # | Prior (P) | Evidence | Posterior | Change |
|---|---|---|---|---|
| P1 | No credible quantification of the 10× claim (0.80) | Not found in two direct searches for the claim; an extended contributor→hire search surfaced only unquantified opinion (`W-12`); the claim compares an inbound-contact outcome to an application input with ≈ 0 yield; no D6 scenario gives a 10× per-hour edge | ≈ 0.92 that none exists in accessible sources | Confirmed; **new:** the claim is ill-posed, and the plausible mechanism (moving from inbound to sourced/referred) is real but unquantified for OSS |
| P2 | Sustained contribution, not one PR; informal pipelines; single PR is modal (0.65) | 49–82% single-commit identities; vLLM committer bar ~30+/~10+; employer-staffed repos; but Hugging Face *requires* merged PRs and RadixArk runs a paid residency | ≈ 0.85 | Confirmed; **surprises:** a formal posting-level gate exists at Hugging Face; a paid one-year program exists (not "small"); agent/farming bans are widespread (4 of 8 repos plus GitHub's own controls) |
| P3a | High-context outreach > generic; no candidate-side dataset (0.70) | Only adjacent proxies (Pin, Instantly); job-seeker figures are author estimates or self-selected | ≈ 0.85 | Confirmed; **surprises:** engineering replies are *below* average in Pin's data (4.64%); LinkedIn vs email gap is 17% vs 5–6% in the recruiter direction |
| P3b | Deliverability risk at ≤ 30/week is authentication/content; LinkedIn automation risky; GitHub restricts harvesting (0.70) | GitHub AUP §7 text; LinkedIn removed Apollo/Seamless.ai pages; vendor limits; Google/Microsoft thresholds target > 5,000/day | ≈ 0.80 | Confirmed; **surprise:** email-finder accuracy (29.8–55.2% in Pin's audit) is a bigger practical risk than volume |
| P4 | Teardown→hire documented in security/prompt-injection; elsewhere anecdotal; failure modes factual error, tone, legal (0.65) | Goodside `B`; Adhikary (headline only) `C`; Artificial Analysis (no hire); Rehberger (no hire stated); legal envelope sharper than expected | ≈ 0.70 | Partly confirmed; **surprise:** the legally cleanest audit surface is *open-source software you run yourself*, which reshapes Tactic 2 and links it to Tactic 1 |
| P5 | Standard funnel is low single digits; per-hour yield must be modeled (0.75) | Gem 0.5%; Ashby 3% / 0.2%; referral 11–13×; no per-hour source | ≈ 0.90 | Confirmed; **surprise:** the model finds no 10× scenario; the case rests on saturation of a finite opening pool and tier access |

**Recalled facts (R1–R16), tested.** Of 16: 9 confirmed, 5 partly confirmed, 2 not verified.

| # | Recalled claim | Prior | Outcome | Evidence |
|---|---|---|---|---|
| R1 | vLLM creators founded Inferact (seed ~Jan 2026, ~$150M at ~$800M) | 0.60 | **Confirmed** (TechCrunch 2026-01-22; a16z and Lightspeed; Simon Mo CEO) | `W-01` |
| R2 | SGLang commercialized as RadixArk (early 2026) | 0.50 | **Confirmed**; ~$400M valuation led by Accel per anonymous sources; round size unconfirmed | `W-02` |
| R3 | ClickHouse acquired Langfuse (Jan 2026) | 0.70 | **Confirmed** (2026-01-16); core stays MIT | `W-03` |
| R4 | vLLM is a PyTorch Foundation project (2025) | 0.80 | **Not verified**: governance files were read, but no foundation-membership source was retrieved; remains recalled (D) | `E1-01…E1-04` |
| R5 | Red Hat acquired Neural Magic (closed ~Jan 2025); large vLLM committer org | 0.85 | **Partly**: a Red Hat profile says the engineer joined Jan 2025 via the Neural Magic acquisition; closing date not independently verified; redhat.com is a top-4 vLLM domain (38 identities, 628 commits) | `W-09, E2` |
| R6 | a16z Open Source AI Grant funded vLLM/llama.cpp-type maintainers | 0.60 | **Partly**: vLLM (Woosuk Kwon, Zhuohan Li) confirmed; llama.cpp not in the first cohort | `O-03` |
| R7 | LiteLLM PyPI compromise in 2026 | 0.50 | **Confirmed**: versions 1.82.7 and 1.82.8 uploaded 2026-03-24 | `S-01` |
| R8 | curl ended its bug bounty in early 2026 over AI-slop reports | 0.60 | **Confirmed** (end of Jan 2026) | `L-14` |
| R9 | GitHub added maintainer controls to restrict/disable PRs in 2026 | 0.50 | **Confirmed**: PR access settings 2026-02-13; open-PR caps 2026-06-17; issue restriction 2026-06-29 | `L-15` |
| R10 | DOJ May-2022 CFAA policy: no charges for good-faith security research | 0.90 | **Confirmed** (via law-firm secondary), with the caveat that, per WSGR, it "does not provide any concrete legal protections" | `L-03, L-04` |
| R11 | Google/Yahoo bulk-sender rules (Feb 2024) and Microsoft (May 2025) | 0.80 | **Partly**: Google and Microsoft via secondary sources (thresholds above 5,000/day); Yahoo's rules not separately retrieved; primary pages not reachable | `T-01, T-02` |
| R12 | GitHub AUP bars using harvested info for unsolicited recruiter emails | 0.80 | **Confirmed** (§7 text) | `L-01` |
| R13 | RFC 9116 defines a `Hiring` field | 0.85 | **Confirmed** (§2.5.6) | `L-02` |
| R14 | LinkedIn acted against Apollo/Seamless.AI in 2025 | 0.50 | **Partly**: both companies' pages disappeared from LinkedIn on 2025-03-06; LinkedIn gave no statement and no reason | `L-13` |
| R15 | Riley Goodside's public work → Scale AI role | 0.80 | **Partly**: public attention → hire confirmed (Dec 2022); the source does not mention prompt injection specifically | `W-13` |
| R16 | Sholto Douglas / Trenton Bricken (Dwarkesh, 2024): Anthropic hires on demonstrated side projects/PRs | 0.60 | **Not verified**: the retrievable transcript stops before the hiring answer | `W-14` |

**Calibration note.** The five recalled *2026 events* I rated 0.5–0.6 (R1, R2, R7, R8, R9) all confirmed, so I was under-confident about recent events inside my knowledge window; the one high-confidence item I could not confirm (R4, 0.80) is a status claim about an organization, not an event. The one claim about people's hiring stories I rated 0.6 (R16) could not be tested.

## Sources & Evidence Ledger

Grades: **A** primary read; **B** reputable secondary or vendor dataset with a method; **C** vendor marketing, unsourced or self-selected estimate, headline-only, or my inference; **D** recalled or modeled. A split grade (A/B, B/C, A/C) means the grade differs by claim or property, for example canonical provenance (A) but vendor-run data (B), or reproducible data (A) but my interpretation (C); the finding text says which. *Basis* = fetched/read unless stated. Retrieval dates are the session dates on which the page was read (2026-10-21 → 2026-10-23). `E2` and the arithmetic in D6 are original analyses; their scripts (`analyze_git_history.py`, `sensitivity_name_merge.py`, `model_checks.py`) are in the session workspace and were not delivered with this file.

### A. Primary repo files and original analysis (pinned commits; read from git objects; 2026-10-21)

| ID | Source | URL | Grade |
|---|---|---|---|
| E1-01…03 | vLLM `docs/governance/process.md` (committer criteria; nomination; "belongs to individuals, not companies") | https://github.com/vllm-project/vllm/blob/96e59c60e025071476b3567f482cbd18066b25ce/docs/governance/process.md | A |
| E1-04 | vLLM `docs/governance/committers.md` (57 active, 18 emeritus, by area) | https://github.com/vllm-project/vllm/blob/96e59c60e025071476b3567f482cbd18066b25ce/docs/governance/committers.md | A |
| E1-05 | vLLM `AGENTS.md` | https://github.com/vllm-project/vllm/blob/96e59c60e025071476b3567f482cbd18066b25ce/AGENTS.md | A |
| E1-06 | vLLM `docs/contributing/README.md` | https://github.com/vllm-project/vllm/blob/96e59c60e025071476b3567f482cbd18066b25ce/docs/contributing/README.md | A |
| E1-07 | SGLang contribution guide | https://github.com/sgl-project/sglang/blob/43728298fe288648b944b7a897ec71c08109879c/docs/docs/developer_guide/contribution_guide.mdx | A |
| E1-08 | transformers `CONTRIBUTING.md` | https://github.com/huggingface/transformers/blob/6b75aeeab91d98bd3872b3f2382cfb4a8ce810d4/CONTRIBUTING.md | A |
| E1-09 | llama.cpp `CONTRIBUTING.md` | https://github.com/ggml-org/llama.cpp/blob/f849095365d5ac1f560886a4e6574531d559e96f/CONTRIBUTING.md | A |
| E1-10 | Ollama `CONTRIBUTING.md` | https://github.com/ollama/ollama/blob/2cd63f7a15039ccd790e97b31edc091fa1707c56/CONTRIBUTING.md | A |
| E1-11 | LiteLLM `CONTRIBUTING.md` | https://github.com/BerriAI/litellm/blob/a31c5230de303d342f62e0e2ecd62af83e5fcd4e/CONTRIBUTING.md | A |
| E1-12 | Langfuse `CONTRIBUTING.md` | https://github.com/langfuse/langfuse/blob/f836391186c916f4ca4219c3c2edae8dd4f78872/CONTRIBUTING.md | A |
| E1-13 | Axolotl `.github/CONTRIBUTING.md` | https://github.com/axolotl-ai-cloud/axolotl/blob/dfb9cb36611c6b8e77ded66cf65d4bf423cfbc1e/.github/CONTRIBUTING.md | A |
| E2 | Contributor statistics: `git log --no-merges` on treeless clones of the eight repos at the SHAs above (method and limits in D0) | https://github.com/vllm-project/vllm, https://github.com/sgl-project/sglang, https://github.com/huggingface/transformers, https://github.com/ggml-org/llama.cpp, https://github.com/BerriAI/litellm, https://github.com/langfuse/langfuse, https://github.com/ollama/ollama, https://github.com/axolotl-ai-cloud/axolotl | A (data) / C (interpretation) |

### B. Company, posting, case and academic sources

| ID | Source | URL | Retrieved | Grade |
|---|---|---|---|---|
| W-01 | TechCrunch 2026-01-22: Inferact $150M seed at $800M | https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/ | 2026-10-21/22 | B |
| W-02 | TechCrunch 2026-01-21: SGLang spins out as RadixArk, ~$400M valuation (sources) | https://techcrunch.com/2026/01/21/sources-project-sglang-spins-out-as-radixark-with-400m-valuation-as-inference-market-explodes | 2026-10-21/22 | B |
| W-03 | ClickHouse: acquires Langfuse (2026-01-16) | https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability | 2026-10-21/22 | A |
| W-04 | Simon Willison 2026-02-20: ggml.ai joins Hugging Face | https://simonwillison.net/2026/Feb/20/ggmlai-joins-hugging-face/ | 2026-10-21/22 | B |
| W-05 | Inferact "Member of Technical Staff, Inference" (job-board mirror; posted 2026-06-18) | https://startup.jobs/member-of-technical-staff-inference-inferact-8280046 | 2026-10-21/22 | B |
| W-06 | Searches for the 10× claim and for contributor→hire stories (no source found) | — (WebSearch) | 2026-10-21 → 2026-10-23 | C (absence) |
| W-07 | Hugging Face "Open-Source Machine Learning Engineer – US Remote" (Workable; posted 2026-05-29) | https://apply.workable.com/huggingface/jobs/view/19A136F8E2 | 2026-10-21/22 | A |
| W-08 | Red Hat Principal/Senior Principal ML Engineer, llama.cpp (mirror; closed) | https://jobs.anitab.org/companies/red-hat/jobs/58768110-principal-senior-principal-machine-learning-engineer-llama-cpp | 2026-10-21/22 | B |
| W-09 | Red Hat blog: Senior ML Engineer on the AI Inference team (profile) | https://www.redhat.com/ja/blog/senior-machine-learning-engineer-red-hats-ai-inference-team | 2026-10-21/22 | B |
| W-10 | LiteLLM "Backend LLM Engineer" (Work at a Startup) | https://www.workatastartup.com/jobs/89354 | 2026-10-21/22 | B |
| W-11 | Langfuse hiring process and careers pages | https://langfuse.com/handbook/how-we-hire/hiring-process.md ; https://langfuse.com/careers.md | 2026-10-21/22 | A |
| W-12 | Koutian Wu (2026-03-08) "GitHub PRs as Inbound Marketing…"; Bessi (2026-02-18) | https://koutian.is-a.dev/posts/2026/03/github-prs-as-inbound-marketing/ ; https://machinelearningatscale.substack.com/p/how-to-break-into-mlsys-through-open | 2026-10-21/22 | C (opinion) |
| W-13 | Washington Post via Independent on Saturday, 2023-02-27 (Riley Goodside) | https://independentonsaturday.co.za/business-report/companies/2023-02-27-have-you-heard-of-an-ai-whisperer-techs-hottest-new-job | 2026-10-21/22 | B |
| W-14 | Dwarkesh Patel transcript (Douglas & Bricken); hiring answer not retrievable | https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken | 2026-10-21/22 | not used as evidence |
| H-01 | RadixArk "AI Infra Resident (1-Year Program)" (Accel board) | https://jobs.accel.com/companies/radixark-2/jobs/72902529-ai-infra-resident-1-year-program | 2026-10-23 | A |
| H-01b | RadixArk "AI Infra Resident" (Greenhouse copy) | https://job-boards.greenhouse.io/radixark/jobs/4088962009 | 2026-10-23 | A |
| H-02 | RadixArk "Member of Technical Staff, Developer Technology" | https://job-boards.greenhouse.io/radixark/jobs/4329271009 | 2026-10-23 | A |
| H-03 | Ollama open roles (aggregator; no requirement text) | https://www.fastaijobs.com/companies/ollama | 2026-10-23 | C |
| O-01 | minpeter, "My vLLM Open Source Contribution Story" (published 2026-01-21) | https://minpeter.com/en/blog/vllm-contribution | 2026-10-23 | A (for what it says) |
| O-02 | Ant OSS, "The Community Stories of vLLM and SGL" (2025-12-17) | https://medium.com/@ant-oss/the-community-stories-of-vllm-and-sgl-d4675e77da6a | 2026-10-23 | B |
| O-03 | a16z, "Supporting the Open Source AI Community" (2023-08-30; Open Source AI Grant, first cohort) | https://a16z.com/2023/08/30/supporting-the-open-source-ai-community/ | 2026-10-23 | A |
| O-04 | Searches for named contributor→hire cases (none verified) | — (WebSearch, extended) | 2026-10-23 | C (absence) |
| A-01 | ifo working paper, "Career Concerns As Public Good — The Role of Signaling for Open Source Software Development" (2024; abstract page) | https://IFO.de/publikationen/2024/working-paper/career-concerns-public-good-role-signaling-open-source-software-0 | 2026-10-23 | B |
| A-02 | Hann, Roberts & Slaughter, *Information Systems Research*, DOI 10.1287/isre.2013.0474 (abstract page; title not captured) | https://pubsonline.informs.org/doi/fpi/10.1287/isre.2013.0474 | 2026-10-23 | B |
| J-01 | DearHiringManager.io, "Does Emailing the Hiring Manager Work? 79 Outcomes Analyzed" | https://dearhiringmanager.io/hiring-manager-outreach-study | 2026-10-23 | C |
| J-02 | PitchHired, "Cold Email Reply Rates for Job Seekers" | https://pitchhired.com/blog/cold-email-reply-rates-job-search-data | 2026-10-23 | C |
| J-03 | MIT News 2022-09-15 on Rajkumar et al., *Science* 2022, "A Causal Test of the Strength of Weak Ties" (paper itself not read) | https://news.mit.edu/2022/weak-ties-linkedin-employment-0915 | 2026-10-23 | B |
| M-01 | The Interview Guys, "The Average Job Opening Now Gets 242 Applications (And a 0.4% Chance of Landing It)" | https://blog.theinterviewguys.com/?p=10980 | 2026-10-23 | C |
| M-02 | LetsDataScience on LinkedIn's 2026 Grad's Guide | https://letsdatascience.com/news/linkedin-identifies-ai-engineer-as-fastest-growing-role-e82f85f1 | 2026-10-23 | C |
| S-01 | Help Net Security 2026-03-25: LiteLLM PyPI packages compromised | https://www.helpnetsecurity.com/2026/03/25/teampcp-supply-chain-attacks/ | 2026-10-23 | B |
| C-01 | The Wire 2026-06-11: Nisarga Adhikary hired at IIT Kanpur's cybersecurity hub (headline and meta only) | https://thewire.in/tech/nisarga-adhikary-who-exposed-cbse-portal-flaws-gets-hired-at-iit-kanpurs-cybersecurity-hub | 2026-10-23 | C |
| C-02 | Simon Willison 2025-08-15, "The Summer of Johann" | https://simonwillison.net/2025/Aug/15/the-summer-of-johann/ | 2026-10-23 | A |
| C-03 | Artificial Analysis careers page | https://artificialanalysis.ai/careers | 2026-10-23 | A |
| V-01 | VentureBeat (Sept 2024): Reflection 70B performance questioned | https://venturebeat.com/ai/new-open-source-ai-leader-reflection-70bs-performance-questioned-accused-of-fraud | 2026-10-23 | B |
| X-01 | Hacktoberfest 2026 (llms-full.txt) | https://hacktoberfest.com/llms-full.txt | 2026-10-23 | A |

### C. Funnel, outreach and deliverability datasets

| ID | Source | URL | Retrieved | Grade |
|---|---|---|---|---|
| F-01 | Pin, Recruiting Outreach Benchmarks 2026 | https://www.pin.com/blog/recruiting-outreach-benchmark-report/ | 2026-10-21/22 | B |
| F-02 | Gem, Email Outreach 2026 Benchmarks (gated; no rates visible) | https://www.gem.com/resource/email-outreach-2026-benchmarks-for-recruiters-report | 2026-10-21/22 | — |
| F-03 | Instantly, Cold Email Benchmark Report 2026 | https://instantly.ai/cold-email-benchmark-report-2026 | 2026-10-21/22 | B |
| F-04 | Apollo, "What Is a Good Benchmark for Reply Rates in Cold Outreach?" | https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach | 2026-10-21/22 | C |
| F-05 | Gem, Key takeaways from the 2026 Recruiting Benchmarks Report | https://app.gem.com/blog/key-takeaways-from-the-2026-recruiting-benchmarks-report | 2026-10-21/22 | A/B |
| F-06 | Ashby Talent Trends: Referrals | https://www.ashbyhq.com/talent-trends-report/reports/referrals | 2026-10-21/22 | A/B |
| F-07 | Ashby Talent Trends: Inbound | https://www.ashbyhq.com/talent-trends-report/reports/inbound | 2026-10-21/22 | A/B |
| F-08 | Pin, Sourcing Benchmarks 2026 (secondary, cites Ashby/Gem) | https://www.pin.com/blog/sourcing-benchmarks-report/ | 2026-10-21/22 | C |
| F-09 | interviewing.io, cold outreach to hiring managers, part 2 | https://interviewing.io/blog/how-to-get-in-the-door-at-top-companies-cold-out-reach-to-hiring-managers-part-2 | 2026-10-21/22 | C |
| T-01 | Mailsuite on Google's sender guidelines (2024-07-23; secondary) | https://mailsuite.com/blog/google-sender-guidelines/ | 2026-10-22 | B |
| T-02 | Petri on Microsoft's Outlook sender rules (2025-04-07; secondary) | https://petri.com/microsoft-outlook-email-authentication-rules/ | 2026-10-22 | B |
| T-04 | GitHub Docs: rate and query limits for the GraphQL API | https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api | 2026-10-22 | A |
| T-05 | OSS Insight docs | https://ossinsight.io/docs | 2026-10-22 | A |
| T-06 | Docket: Apollo pricing ("verified April 2026") | https://docket.io/resources/research/apollo-pricing | 2026-10-22 | C |
| T-07 | MarketBetter: Hunter.io pricing (verified Sept 2026) | https://marketbetter.ai/blog/hunter-io-pricing-breakdown-2026/ | 2026-10-22 | C |
| T-08 | Docket: Clay pricing (March 2026 overhaul) | https://docket.io/resources/research/clay-pricing | 2026-10-22 | C |
| T-09 | Evaboot: LinkedIn account types and prices (updated 2026-09-13) | https://evaboot.com/blog/linkedin-account-types | 2026-10-22 | C |
| T-10 | PhantomBuster: LinkedIn limits (modified 2026-07-08) | https://phantombuster.com/blog/social-selling/linkedin-limits/ | 2026-10-22 | C |
| T-12 | Pin: email-finder vendor audit (vendor-run; 1.3M lookups, Mar–May 2026) | https://www.pin.com/blog/email-finder-vendor-audit/ | 2026-10-22 | B/C |
| T-14 | Anyscale: LLM benchmarking guide | https://docs.anyscale.com/llm/serving/benchmarking/benchmarking-guide | 2026-10-22 | A/B |
| T-15 | vLLM docs: `vllm.benchmarks.serve` | https://docs.vllm.ai/en/stable/api/vllm/benchmarks/serve/ | 2026-10-22 | A |
| P-01 | SalesIntel (competitor): RocketReach pricing & plans (updated 2026-09-29) | https://salesintel.io/blog/rocketreach-pricing-plans/ | 2026-10-23 | C |
| P-02 | Invicti: OWASP Top 10 for LLM Applications 2025 (2025-09-21; secondary) | https://invicti.com/blog/web-security/owasp-top-10-risks-llm-security-2025 | 2026-10-23 | B |

### D. Legal, policy and failure-mode sources

| ID | Source | URL | Retrieved | Grade |
|---|---|---|---|---|
| L-01 | GitHub Acceptable Use Policies, §7 Information Usage Restrictions | https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies | 2026-10-22 | A |
| L-02 | RFC 9116 (security.txt), §2.5.6 `Hiring` | https://rfc-editor.org/rfc/rfc9116.html | 2026-10-22 | A |
| L-03 | Morrison & Foerster alert (2022-05-25) on DOJ's CFAA charging policy | https://www.mofo.com/resources/insights/220525-cyber-crime-charging-policy | 2026-10-22 | B |
| L-04 | WSGR (2022-05-25): limits of the DOJ policy | https://www.wsgr.com/en/insights/doj-acknowledges-limits-to-the-cfaa-but-questions-and-possible-civil-liability-remain-for-security-researchers-and-others.html | 2026-10-22 | B |
| L-05 | OpenAI Usage Policies (effective 2025-10-29) | https://openai.com/policies/usage-policies/ | 2026-10-22 | A |
| L-06 | OpenAI EU Terms of Use (updated 2026-01-16) | https://openai.com/policies/eu-terms-of-use/ | 2026-10-22 | A |
| L-07 | Anthropic Responsible Disclosure Policy (updated 2025-02-14) | https://www.anthropic.com/responsible-disclosure-policy | 2026-10-22 | A |
| L-08 | Anthropic Model Safety Bug Bounty (help-center page dated 2026-09-08) | https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program | 2026-10-22 | A |
| L-09 | eDiscovery Today (2024-09-18) on OpenAI's warnings to users probing o1 (citing Ars Technica) | https://ediscoverytoday.com/2024/09/18/openai-has-threatened-to-ban-users-who-probe-chatgpt-o1-artificial-intelligence-trends | 2026-10-22 | B |
| L-10 | Longpre et al., "A Safe Harbor for AI Evaluation and Red Teaming" (arXiv 2403.04893, 2024-03-07) | https://arxiv.org/abs/2403.04893v1 | 2026-10-22 | A |
| L-11 | Schneier (2025-08-08) on Google Project Zero's disclosure policy change | https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html | 2026-10-22 | B |
| L-12 | Internet Freedom Foundation (2021-10-13): don't penalise cybersecurity researchers | https://internetfreedom.in/dont-penalise-cybersecurity-researchers/ | 2026-10-22 | B |
| L-13 | MarTech: Apollo.io and Seamless.ai disappear from LinkedIn (2025-03-06) | https://martech.org/a-pair-of-lead-gen-providers-have-disappeared-from-linkedin/ | 2026-10-22 | B |
| L-14 | The Register (2026-01-21): curl ends its bug bounty | https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/ | 2026-10-22 | B |
| L-15 | Visual Studio Magazine (2026-06-30): GitHub extends contribution controls | https://visualstudiomagazine.com/articles/2026/06/30/github-extends-contribution-controls-from-prs-to-issues.aspx | 2026-10-22 | B |

**Attempted but not retrieved (no evidence drawn from them):** Google's primary sender-guidelines page (`support.google.com/a/answer/81126`, not on the fetch allowlist); Microsoft Tech Community announcement (rendered empty); genai.owasp.org (OWASP's own LLM Top 10 page; a secondary summary was used, `P-02`); the DOJ's CFAA charging policy itself (law-firm summaries used, `L-03`, `L-04`); the flosshub paper on OSS wage premiums (fetch error); the body of The Wire article (metadata only); RocketReach's own pricing page (a competitor's summary was used).

**Recalled, never verified (capped at D):** R4 (vLLM and the PyTorch Foundation), R16 (Anthropic's hiring route in the Dwarkesh episode), the secret-scanner names in D3.3(b) (gitleaks, trufflehog), the `/.well-known/security.txt` location convention, and common deliverability practices flagged as such in D4.3.
