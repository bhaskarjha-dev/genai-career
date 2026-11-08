<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which national and regional job boards carry GenAI roles in each market a GenAI professional might target, with India measured in depth, and which are worth a job seeker's time? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: dated measurements of GenAI posting volume, employer mix and quality on each national board.

## BRIEF

A separate session covers cross-border boards (aggregators, AI-specific, startup, remote and employers' own boards) and owns ghost jobs, pay transparency and scams. This session covers the boards each country uses domestically, because many GenAI roles at local employers, global capability centres (GCCs) and national champions never reach the cross-border boards. India is the priority: its platforms have been an open question for the knowledge base since its first research phase, and India is its deepest readership. Question type: lookup and evaluative. Audience: job seekers targeting India and the countries listed below, whether they live there already or plan to relocate.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}; counts dated to the day observed.
- **India in depth:** Naukri, Instahyre, Hirist, Cutshort, Foundit, iimjobs, Wellfound India, LinkedIn India, Apna's white-collar segment if relevant, campus platforms (Unstop, Internshala), and the hiring channels of GCCs and IT-services firms.
- **Other markets:** the main national boards for technology roles in: {{param:markets}}. Examples to check, not a complete list: StepStone, XING and Make it in Germany (Germany); Welcome to the Jungle (France); jobs.ch (Switzerland); Jobindex (Denmark), Platsbanken (Sweden) and FINN (Norway); InfoJobs (Spain); Landing.jobs (Portugal); Just Join IT and No Fluff Jobs (Poland); EURES (EU); Reed, Totaljobs and CWJobs (UK); Job Bank (Canada); AllJobs (Israel); Bayt, GulfTalent and Naukrigulf (Gulf); MyCareersFuture, JobStreet and NodeFlair (Singapore); JobsDB (Hong Kong); 104 (Taiwan); Wanted and Saramin (South Korea); Japan Dev and TokyoDev (Japan); Seek (Australia and New Zealand); BOSS Zhipin and Liepin (China, for completeness).
- **Out of scope:** cross-border boards, ghost-job law, pay transparency and scams (the global session); tools (the tools session).
- **Never log in, create accounts or bypass bot walls to count postings.** Report what is visible without logging in, and say where counts need a login; the owner may run logged-in counts separately with fixed queries.
- **Source priorities:** the boards themselves (observed counts, features, prices); operators' published statistics and hiring reports (for example Naukri's hiring indices); industry bodies (for example NASSCOM reports on GCC hiring); reputable reporting; then practitioners.

## KNOWN

The knowledge base's claims, to be tested:

{{claims}}

{{context}}

## CALIBRATION

Apply the five calibration rules in the protocol. A board's advertised total is not a count of live, unique GenAI postings: state your query, filters and date. Indian platforms mix GCC, product-company, services and staffing postings: classify a sample by employer type before drawing conclusions. Translate non-English queries and state the terms used.

## APPROACH

Cover every item, or list it under Absences:

1. **India census.** For each Indian platform: who uses it (job seekers, recruiters, employer types), GenAI posting volume for a fixed query set (state it, for example "generative AI", "LLM", "GenAI engineer", "AI engineer", "machine learning engineer") with the date, the employer-type mix in a sample of at least 30 GenAI postings, seniority mix, posted pay where shown, paid tiers for job seekers, recruiter spam and scam reports, and a verdict, as `board` and `measure` records.
2. **India hiring channels.** How GCCs, Indian product companies, AI startups and IT-services firms recruit for GenAI roles (their own career sites, referral drives, campus, staffing partners), with sources.
3. **Other markets.** For each market listed, the national boards that carry technology and GenAI roles: what they list, volume where visible (with query and date), language, employer mix, apply path, cost and a verdict, as `board` records.
4. **Language and access.** Boards where postings or applications need the local language; boards that list relocation or visa sponsorship; boards closed to foreign applicants.
5. **A discovery routine per market group:** India; Europe; the Gulf; Asia-Pacific; Canada.

Research moves: WIDEN to non-English board names and queries; FALSIFY operators' volume claims with observed counts; CORROBORATE India findings across two platforms.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every Indian platform in scope has a `board` record and dated `measure` records, or an absence record that says why.
3. Each listed market has at least one `board` record or an absence record.
4. The India hiring-channel picture and a discovery routine per market group are stated, each graded.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use `subject` values like `board:naukri` in `measure` records. In Detailed Findings include: the India table (platform · users · GenAI volume and date · employer mix · pay shown · paid tiers · verdict · grade); a table per market group; and the query list with translations.
