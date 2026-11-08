<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Where are GenAI jobs posted across borders (aggregators, AI-specific boards, startup boards, employers' own applicant-tracking boards, venture-capital portfolio boards, remote boards, research and public-sector portals), which are worth a job seeker's time, and how should a job seeker set up discovery and filter out ghost jobs and scams? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: dated measurements of GenAI posting volume and freshness by board; conversion data by channel for AI roles; new rules on ghost jobs and pay transparency.

## BRIEF

We are investigating the cross-border discovery layer of a GenAI job search. A separate session covers national and regional boards (with India in depth); this one covers the boards and sources used across countries, and it owns three cross-cutting topics for the whole pipeline: ghost jobs, pay-transparency rules for postings, and job scams. Question type: lookup and evaluative (a census with measurements and verdicts). Audience: job seekers worldwide, with depth for India-based readers looking for roles abroad and remote.

The knowledge base's channels guide treats boards as places to find postings and people as the route in, and cites vendor conversion data (Ashby, Gem, Greenhouse, Huntr). It has no measured counts for the major boards and has not evaluated AI-specific boards as job-search tools. The aim is a dated census with volume, freshness and quality evidence per board, a refreshed view of channel conversion, and the state of ghost-job, pay-transparency and scam evidence.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}; posting counts dated to the day you observed them.
- **In scope:** general aggregators (for example LinkedIn Jobs, Indeed, Glassdoor, Google's job search, ZipRecruiter, hiring.cafe); startup and tech boards (for example Wellfound, Y Combinator's Work at a Startup, Welcome to the Jungle, Built In, Dice, Hacker News "Who is hiring?" threads); AI-specific boards (for example Fast AI Jobs, JobsPipe, aijobs.net and other AI-only boards; the 80,000 Hours board for safety and policy roles); boards hosted on applicant-tracking systems (Greenhouse, Lever, Ashby, Workday) and how to search them lawfully; venture-capital portfolio boards (for example those of a16z, Sequoia, Accel, Lightspeed and Y Combinator); remote boards; curated job lists on GitHub (for example SimplifyJobs' internship and new-graduate lists and remoteintech/remote-jobs) and community sources (Reddit, Blind); job platforms launched by AI companies (for example OpenAI's announced jobs platform: status at the research date); research job boards (university and lab career pages, EURAXESS, academic boards); public-sector AI hiring portals.
- **Out of scope:** national and regional boards (the regional session); trackers, autofill and other tools (the tools session); recruiters and referrals (the outreach session).
- **Never log in, create accounts or bypass bot walls to count postings.** Where a board shows counts only after login, say so; the owner may run logged-in counts separately with fixed queries.
- **Source priorities:** the boards themselves (observed counts and features, with the query and date); operators' published statistics; regulators and statutes on ghost jobs, pay transparency and scams; applicant-tracking vendors' benchmark reports with sample sizes; independent analyses; then practitioners.

## KNOWN

The knowledge base's claims, to be tested:

- K: Per application, a referral converts about 11 to 36 times better than cold inbound, depending on the metric, and a recruiter-sourced candidate about 8 times better (Gem; Ashby, 2021–2024); these are selection effects [B].
- K: Cold inbound turns about 0.2% of engineering applications into hires, roughly 460–520 applications per hire, yet it is the largest single source of hires: 43–52% at Ashby customers from January 2021 to June 2025, and 37.1% for technical roles with "AI" in the title in Ashby's July 2026 data [B; A].
- K: In Huntr's Q1 2026 data, interview rates fell from 6.07% for one application at a company to 1.91% for eight or more, and tailored applications converted at 4.23% against 2.07% untailored (vendor-run, correlational) [C].
- K: Job and employment-agency scam losses reported to the FTC rose from $90M in 2020 to $501M in 2024, and fake recruiters use coding tests to deliver malware [A; B].
- K: In a self-selected survey, 93% of about 593 respondents had applied to or suspected ghost jobs; no better measurement of ghost-job prevalence was found [C, as of October 2026].
- K: The Texas Attorney General was reported in July 2026 to have opened an investigation into LinkedIn tied to ghost-job listings and Premium subscriptions; these are allegations [B].

Context (what the knowledge base already holds or lacks; no verdict needed):

- It has no measured counts for LinkedIn, Indeed, Wellfound, Otta or Ashby, and has not evaluated Fast AI Jobs or JobsPipe as job-search tools.
- It counts GenAI posting volume from these sources (last counted): {{count_sources}}.

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Board operators overstate their reach: an advertised "jobs" number is not a count of live, unique GenAI postings. When you count, state the query, the filters, the date and whether duplicates and reposts are included. Grade your own observed counts B (a platform's display) and say what they cannot show.

## APPROACH

Cover every item, or list it under Absences:

1. **Census.** For every board and source in scope (and any significant one you find): what it lists, regions, focus, how listings are sourced (employer-posted, scraped, aggregated), apply path (redirect to the employer's system or native), cost to job seekers, alerts and feeds, controls against ghost jobs and scams, and a verdict, as `board` records.
2. **Volume and freshness.** For each major board, the GenAI postings you can observe without logging in for a fixed query set (state it, for example "LLM OR generative AI OR GenAI" plus the titles AI Engineer, Machine Learning Engineer and Forward Deployed Engineer) in the US, the UK, Germany, India and remote, with the date; the share older than 30 days where visible; duplicates and reposts. Record as `measure` records.
3. **AI-specific boards.** How their listings are sourced and verified, overlap with aggregators, update frequency, and whether they surface roles faster or more completely than aggregators.
4. **Searching employer systems.** How job seekers search Greenhouse, Lever, Ashby and Workday boards (site search operators, public board pages, feeds) within each vendor's terms.
5. **Venture-capital, community and curated lists.** Which portfolio boards, GitHub lists and community threads list GenAI roles, how fresh they are, and whether they are a distinct source.
6. **Ghost jobs (owned here).** Measurements of ghost or evergreen postings (studies, datasets, regulator statements); laws and bills that address them (for example Ontario's posting rules in force from 1 January 2026 for larger employers, and US state bills), as `rule` records with status and dates; how to detect a ghost posting.
7. **Pay transparency (owned here).** Jurisdictions that require salary ranges in postings (US states and cities, Canadian provinces) and the EU Pay Transparency Directive (2023/970; transposition due 7 June 2026): each member state's transposition status, and whether the range must appear in the posting or only before the interview. Record as `rule` records.
8. **Scams (owned here).** The most recent annual FTC Consumer Sentinel figures on job scams as of the research date, India's cybercrime reporting on task and job scams, documented malware campaigns that use fake coding interviews, and a verification checklist with sources.
9. **Channel conversion refresh.** Benchmark reports published since 2025-01-01 by applicant-tracking vendors and job-search tools on conversion by source, preferably for AI or engineering roles, with samples and dates.
10. **Alert set-up.** A practice-curated discovery routine (which boards, which alerts, how often) for three readers: one targeting remote roles, one targeting relocation, and a researcher.

Research moves: FALSIFY operators' volume claims with your own observed counts; CORROBORATE ghost-job figures across independent sources; DEEPEN every law to its official text.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every board and source in scope has a `board` record with a verdict, or an absence record.
3. Observed GenAI posting counts for the major boards are reported with query, filters and date, or the reason they could not be observed.
4. Ghost-job, pay-transparency and scam evidence is summarised with official sources and dates, with `rule` records for every law.
5. A discovery routine is given for each of the three readers.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the board table (board · kind · regions · sourcing · apply path · GenAI volume and date · ghost and scam controls · verdict · grade); the observed-count table with the query; and the law table (jurisdiction · rule · effective date · status · source).
