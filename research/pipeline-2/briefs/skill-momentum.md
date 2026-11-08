<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which GenAI skills, tools, frameworks and protocols are rising or falling in employer demand and practitioner use at the research date, measured as dated series rather than single snapshots, and which should job seekers learn first, keep or drop? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: new dated measurements that move a skill between rings, acquisitions or deprecations, or protocol and framework adoption shifts.

## BRIEF

The knowledge base tiers 523 skills per role and draws a skills radar, but it has no measured "surging" ring: outside about a dozen posting titles measured once (JobsPipe, 2 November 2026), its tool tiers rest on research-session mentions and practice curation. The aim is to assemble dated series (at least two time points per signal) from independent sources (posting shares, developer surveys, package downloads, repository activity, official adoption announcements) and to classify skills as rising, stable or falling, with the signal type and grade behind each call. Question type: measurement and evaluation. Audience: job seekers deciding what to learn and drop, and the knowledge base's skills radar.

Posting titles the knowledge base has measured once, with their top terms:

{{posting_titles}}

Skills the knowledge base has marked as devalued (each line is a claim to test):

{{devalued}}

Titles the knowledge base keeps in quarantine or on its watchlist, or has never measured (each line is a claim to test):

{{watchlist}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Series from 2024-01-01 to {{date}}; each data point dated.
- **In scope:** protocols (for example MCP, A2A, AG-UI), agent frameworks and SDKs, retrieval and vector stores, evaluation and observability tools, serving engines and inference optimisation, fine-tuning and post-training methods, coding agents, multimodal and voice, on-device and small models, AI security, governance frameworks, and the programming languages and clouds GenAI postings name; in the US, Europe and India where data allow.
- **Out of scope:** model leaderboards as such (a model's benchmark rank is not a skill signal).
- **Source priorities:** posting-share series from job platforms and labour-market analytics with methods (B); official developer surveys with samples (for example Stack Overflow, JetBrains, GitHub Octoverse) (B); package-download statistics from registries (PyPI, npm) and repository activity (A for the counts, with caveats on what they measure); official adoption and deprecation announcements (A); analyst reports (C).

## KNOWN

The knowledge base's claims, to be tested:

- K: Agentic AI was named in 59.3% of AI Engineer postings (counted 2026-09-10), while the exact title "Agent Architect" had about 2 postings and "Context Engineer" roughly 10–25 worldwide (an estimate): new work appears as skills long before it appears as a title [B; C].
- K: Evaluation appeared in the postings of 68.2% of 198 companies in one corpus (snapshot 2026-08-05) [B].
- K: Thin-wrapper skills are commoditised, and Prompt Engineer is a legacy title [B; B/C].

Context (what the knowledge base already holds or lacks; no verdict needed):

- Its tool tiers outside about a dozen measured posting titles rest on research-session mentions and practice curation, and its skills radar has no measured "surging" ring.

## CALIBRATION

Apply the five calibration rules in the protocol. Each signal measures something different: posting shares measure employer demand, surveys measure self-reported use, downloads include automated installs, and stars measure attention. Never treat one as another, and require at least two independent signals before calling a skill rising or falling.

## APPROACH

Cover every item, or list it under Absences:

1. **Series.** For each skill area in scope, dated data points from at least two independent signal types, as `measure` records with `subject` like `skill:<name>` and `measure` names such as `posting_share`, `survey_use_share`, `monthly_downloads` or `github_stars`.
2. **Posting shares.** Where platforms publish skill shares for AI titles at two or more dates, report them with n where known, as `skill_signal` records (`source_kind` `platform`).
3. **Classification.** For each skill, a call of rising, stable or falling, the signals behind it, and a grade; separate durable concepts (for example evaluation, retrieval quality, tool schemas) from fast-moving tools.
4. **Devalued skills.** A verdict on each skill under KNOWN that the knowledge base marks devalued: still devalued, recovered or gone.
5. **Acquisitions, deprecations and dormancy.** Tools acquired, renamed, deprecated or dormant since 2025, with dates, and what replaced them.
6. **Protocols.** Adoption evidence for agent protocols: official specification governance, vendor support, registry or server counts with dates, and posting mentions.
7. **India.** Skill-demand trends specific to India, where data exist.
8. **Emerging titles.** For each title under KNOWN, and any new GenAI title you find with real postings (for example AI developer relations or GenAI data scientist), dated posting counts and whether it passes the knowledge base's seven graduation tests: volume, persistence, breadth, a shared skill set, a seniority ladder, adoption by a lab or Big Tech employer, and not being an alias.
9. **Learn, keep, drop.** A graded list per role family of skills to learn first, keep and drop.

Research moves: CORROBORATE every rising or falling call with a second signal type; FALSIFY hype with posting data; WIDEN to non-US labour-market analytics.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every skill area in scope has a dated series from at least two signal types, or an absence record.
3. Every rising or falling call states its signals and grade.
4. Every devalued skill under KNOWN has a verdict.
5. The learn, keep and drop lists are given per role family.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: one series table per skill area (skill · signal type · date · value · source · grade); the classification table (skill · call · signals · grade); and the learn, keep and drop lists.

Role families (use these names):

{{families}}
