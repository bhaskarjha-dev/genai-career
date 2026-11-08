<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What do interview loops for GenAI roles look like at the research date, by employer and by interview track: which rounds, what each assesses, the policy on AI assistants, take-homes, in-person rounds, timelines and pass rates? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: employers publishing new interview guides or AI-use policies; consistent candidate reports of new round types; pass-rate data.

## BRIEF

We are refreshing the knowledge base's interview evidence, which dates from October 2026 and rests largely on candidate reports (B/C) and a few employer guides. Loops changed quickly in 2025–2026: AI-enabled coding rounds, design-document reviews, latency-debugging exercises, values rounds at labs, a return to in-person rounds at some employers, and new rules on candidates' use of AI. The aim is a dated, employer-by-employer and track-by-track picture, with question themes for practice prompts (themes and what a strong answer covers, never model answers). Question type: lookup and evaluative. Audience: GenAI job seekers preparing for loops at frontier labs, Big Tech, AI-native startups, enterprises, GCCs and IT-services firms, in the US, Europe and India.

The knowledge base's interview tracks, with what each tests (classify every loop into one of these):

{{interview_tracks}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-07-01 to {{date}}; flag reports older than 2026-01-01 as possibly stale.
- **In scope:** at least 25 employers across frontier labs, Big Tech, AI-native startups, enterprises and consultancies, GCCs and IT-services firms in India; loop structure (screens, online assessments, rounds, hiring committees, team matching); round formats (classic coding, practical coding, AI-enabled coding, ML or AI system design, design-document review, debugging, research discussion, paper presentation, product sense, customer role-play, behavioural and values); take-homes; AI-assistant policies; in-person requirements; timelines; offer and pass rates; India-specific assessments; model prices used in AI system-design estimation.
- **Out of scope:** AI screening and AI interviewers at the application stage (another session); model answers.
- **Source priorities:** employers' own interview guides and candidate-AI policies (A); recruiter statements on record; aggregated candidate reports with dates and counts (Glassdoor, Blind, Levels.fyi, interviewing.io; B or C); individual candidate write-ups (C or D); vendor pricing pages for model prices (A).

## KNOWN

The knowledge base's claims, to be tested:

- K: Loops are heterogeneous by role and team; classify the loop before preparing by asking the recruiter which rounds, which kind of system design, and the AI-tool policy; preparing for the wrong track is the most avoidable failure [B/C].
- K: Classify by team, not employer: Google runs classic or ML design depending on role and interviewer, OpenAI's reported prompt pool mixes classic and AI-product prompts, and Databricks varies by track [B/C; C].
- K: A behavioural or values "No Hire" is a near-automatic veto at Anthropic (values round); at Google it sinks the packet at the target level, though the hiring committee may downlevel; at Meta it triggers downlevel or rejection [B/C, and the sources disagree on Google].
- K: Anthropic's live rounds default to no AI assistance; where an AI-enabled coding round exists (Meta, spring 2026, an early signal), candidates are scored on directing and auditing the assistant, and blind reliance is a strong No Hire signal [B/C]. Sources disagree on whether Meta's round is a coding or a design round.
- K: A design-document review round, in which the candidate critiques a pre-written design and orders findings by severity, rests on three Anthropic reports first observed in April 2026; a latency-debugging exercise rests on one report [B; C].
- K: Onsite-to-offer is 29% in Gem's engineering data, and about 15–20% by industry consensus; no firm publishes its own rate [B; C].
- K: Getting into loops binds harder than passing them; run 3–5 parallel loops, staggered so offers overlap [B/C; D].
- K: No interview-preparation platform has independent outcome evidence [E].

Context (what the knowledge base already holds or lacks; no verdict needed):

- For AI system-design estimation it holds only Anthropic's model prices (fetched 2026-10-21); OpenAI's and Google's are unverified.

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Candidate reports are self-selected and often undated: give dates and counts, and prefer patterns seen across several reports. Employer guides describe intended loops; candidate reports describe experienced ones; keep both and note conflicts.

## APPROACH

Cover every item, or list it under Absences:

1. **Employer loops.** For each employer in scope, a `loop` record per track it hires for: stages, round formats, duration, take-home, AI policy, in-person requirement, level calibration and committee, with dates and sources.
2. **Track patterns.** For each interview track above: the typical round mix by employer type and what each round assesses, and how it changed since 2025.
3. **AI-assistant policies.** Employers' published or reported rules on candidates using AI in applications, take-homes and live rounds (allowed, banned, allowed with disclosure, AI-enabled rounds), with dates.
4. **In-person and integrity.** Employers that reinstated in-person rounds or added identity checks since 2025, and why.
5. **Take-homes.** Prevalence for GenAI roles, length, payment, AI policy and evaluation criteria.
6. **System design for GenAI.** Archetypes that appear in 2025–2026 loops (for example retrieval with access control, agent loop control, evaluation architecture, inference cost and latency, multi-tenant serving, MCP integrations), and the model prices and limits needed for estimation, taken from vendor pricing pages at the research date.
7. **Behavioural and values rounds.** What labs and other employers assess (mission, safety, collaboration), how rounds are scored, and red flags.
8. **Research loops.** Paper discussions, research presentations, coding for researchers, and research-taste interviews.
9. **India.** Loops at GCCs, product startups, Indian AI labs and IT-services firms: online assessments, data-structures emphasis, aptitude tests, managerial and HR rounds.
10. **Timelines and rates.** Time from application to offer for AI roles, number of rounds, and any pass or offer rates by stage, with sources.
11. **Practice prompts.** For each track, 8–15 question themes as `prompt` records: the track ID (one of the IDs above, or `behavioural` or `coding`), the prompt as candidates report it, what a strong answer covers, red flags, and who reported it. Themes and criteria only; never model answers.

Research moves: CORROBORATE every round format across at least two independent reports; FALSIFY assumptions that loops are uniform within an employer; WIDEN to non-US reports, including India.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence, including a resolution or a sharper statement of the two source conflicts.
2. At least 25 employers have dated `loop` records.
3. Every interview track has its round mix, assessment criteria and `prompt` records.
4. AI-assistant policies and in-person requirements are tabulated with dates.
5. Model prices for estimation are given from vendor pages with dates.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the employer-loop table (employer · track · rounds · AI policy · take-home · in person · date · grade); the track table; the AI-policy table; and the model-price table (model · input and output price per million tokens · context window · date · source).
