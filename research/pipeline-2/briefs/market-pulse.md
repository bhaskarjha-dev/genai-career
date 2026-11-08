<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Re-run it quarterly with a new session id. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What has changed in the GenAI job market since the knowledge base's last market snapshot: hiring volume by title and region, layoffs and hiring freezes, funding, the employer mix, entry-level hiring and pay pressure, and which of the knowledge base's market signals still hold? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: a material change in volume, employer mix or entry-level hiring; a change in a title's status under the knowledge base's quorum rules.

## BRIEF

This is a recurring market pulse. The knowledge base's market overview describes the market as of October 2026 in nine signals, and its role scores rest on posting counts that expire 31 days after they were counted. The pulse re-measures the signals with dated, comparable sources, records what changed, and flags any title that crosses the knowledge base's 50-posting quorum or falls below it. Question type: measurement. Audience: job seekers timing and targeting a search, and the knowledge base's maintainers.

## SCOPE

- **Temporal anchor:** today is {{date}}. Compare with the knowledge base's October 2026 figures and with any earlier pulse; every figure dated.
- **In scope:** live posting counts for the GenAI titles the knowledge base tracks (US, India, global) from the same platforms it uses ({{count_sources}}); applications per job; layoffs and hiring freezes at AI employers; venture funding for AI companies; hiring announcements and headcount plans; entry-level hiring; pay-pressure signals; India GCC expansion; regulatory events that affect hiring.
- **Out of scope:** pay benchmarks in detail (the pay sessions), visa rules (the regional dossiers).
- **Source priorities:** the same platforms the knowledge base uses for counts, with the same queries (B); official statistics (A); layoffs and funding trackers with methods (B or C); company announcements (A for what they say); reputable reporting (B).

## KNOWN

The knowledge base's claims, to be tested:

- K: Only AI Engineer, Machine Learning Engineer and Forward Deployed Engineer have a measured count above the 50-posting quorum; agentic, context and evaluation work shows up as skills inside AI Engineer postings rather than as new titles [B, as of October 2026].
- K: JobsPipe counted 1,697 live US AI Engineer postings, 398 in India and 3,944 globally (corpus 2026-10-19, page unchanged 2026-11-02) [B].
- K: About 66% of US AI-engineering postings (January–July 2026) are individual-contributor roles, 35% mid-level and 31% senior [C].
- K: Applications per job rose about 110% from 2022 to 2025 (Greenhouse), and cold applications end in a hire about 0.2% of the time [B].
- K: India has the highest AI-title share of postings of the five countries compared (3.0% against 1.3% in the US) and about twice the US entry-level share of AI roles (21.2% against 10.4%) [B].
- K: Evaluation appears in the postings of 68.2% of 198 companies, yet only 52.4% of agent teams run offline evaluations [B; B/C].

Roles and their current evidence status in the knowledge base:

{{roles}}

## CALIBRATION

Apply the five calibration rules in the protocol. Counts are only comparable when the platform, query, filters and region match: reuse the knowledge base's sources and say exactly what you queried. Distinguish a layoff announcement from a measured change in hiring.

## APPROACH

Cover every item, or list it under Absences:

1. **Recount.** Live posting counts for every title above that has a measured count, on the same platforms, with the same scope, as `measure` records (`subject` `role:<id>`, `measure` `us_postings`, `india_postings` or `global_postings`).
2. **Quorum changes.** Any title that crosses the 50-posting quorum in either direction, with evidence.
3. **Employer mix and announcements.** Hiring announcements, freezes and layoffs at AI employers since October 2026, dated.
4. **Funding.** AI venture funding in the most recent quarter against earlier quarters, from a tracker with a stated method.
5. **Applicant pressure.** Applications per job and time-to-hire for AI roles, where published.
6. **Entry level.** New-graduate and entry-level hiring signals for AI roles.
7. **India.** GCC expansion, Indian AI-startup hiring and posting volume changes.
8. **Signals check.** For each of the knowledge base's market signals under KNOWN, whether it still holds.

Research moves: CORROBORATE every change with a second source; FALSIFY headline narratives with counts.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every measured title has a dated recount on the same platforms, or an explanation.
3. Quorum changes are flagged with evidence.
4. Employer, funding, applicant-pressure, entry-level and India changes are dated and graded.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use `ttl` V1 for posting counts. In Detailed Findings include: the recount table (title · platform · region · previous count and date · new count and date · change); the events table; and the signals check.
