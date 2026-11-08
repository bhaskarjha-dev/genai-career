<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which job-search tools (trackers, résumé builders and generators, parse checkers, autofill and auto-apply tools, AI job-search agents, open-source projects, job-data APIs and MCP servers for AI agents) help a GenAI job seeker, which carry account, legal, privacy or reputational risk, and what verdict should each get? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: independent outcome evidence for a tool category; a platform changing its terms on automation; security incidents; official APIs or MCP servers from job platforms.

## BRIEF

We are investigating the tool layer of a job search as it stands at the research date, including tools that are new since 2025: AI agents that search and apply, browser agents, and MCP servers that let an AI assistant query job platforms. Question type: lookup and evaluative (a census with verdicts). Audience: job seekers who will use AI assistants heavily, worldwide, with India coverage.

The knowledge base holds a tool catalog of verdicts by lifecycle stage (use, use-with-care, avoid, watch). Its stance, from Phase 0 research, is that auto-apply at volume has weak and mostly adverse evidence, that autofill is acceptable only when the candidate reviews every answer and submits personally, and that checker scores are not validated against outcomes. The aim is to refresh and extend the census, add open-source and agent tooling, and test those stances against evidence dated after October 2026 where it exists.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}. Tool statuses change monthly: date every status.
- **In scope:** application trackers; résumé builders and open-source résumé generators (for example JSON Resume, RenderCV, Reactive Resume, OpenResume); AI tailoring and writing tools; parse and match checkers; autofill extensions; auto-apply services and open-source auto-apply bots; AI job-search agents and matching services; general browser agents used to apply for jobs; job-data APIs offered officially by boards and governments; MCP servers and other agent integrations for job search (official and community); open-source job-search projects (scrapers, matchers, trackers), with licence, maintenance and terms-of-service status; labour-market data tools for job seekers.
- **Out of scope:** interview copilots and mock-interview tools (another session covers AI in hiring); salary tools; contact finders (the outreach session covers them).
- **Source priorities:** the tools' own documentation, pricing and terms; platform terms of service and help pages (LinkedIn, Indeed, Greenhouse, Ashby, Workday); repository metadata (stars, last commit, licence, issues); security advisories and incident reports; independent tests and reviews with a method; vendor outcome claims (C, with COI).

## KNOWN

The knowledge base's claims, to be tested:

- K: Auto-apply at volume has weak and mostly adverse evidence [B/C, as of October 2026].
- K: Use autofill only where you review the answers and click Submit yourself [B/C].
- K: Applicant-tracking systems keep an applicant's history, and Ashby identifies repeat applicants by email [A].
- K: LinkedIn's user agreement prohibits automation tools, and automated activity risks account restriction [A].
- K: No study links "ATS score" checkers to real screening outcomes; use them only as a list of gaps [C].
- K: In Huntr's correlational data, the interview rate was 9.25% for users sending 11–20 applications against 2.58% for those sending 100 or more [B/C].

The knowledge base's verdict rubric (use these verdicts with these meanings):

{{tool_rubric}}

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Tool vendors publish success rates about themselves: grade them C with COI unless independently corroborated. Repository stars measure attention, not quality or safety. For agents and MCP servers, check whether the underlying platform permits the access, and say so.

## APPROACH

Cover every item, or list it under Absences:

1. **Census by category.** For each category in scope: the significant tools at the research date, what each does, price, platform permissions, data handling, status, and a verdict with reasons, as `tool` records at the stage the knowledge base uses (6 for application tools, 0 for general assistants, 1 for labour-market data).
2. **Re-verify the listed tools.** For each tool under KNOWN: still operating, renamed, acquired, closed or changed; record status changes. Tools in other categories (boards, résumé builders, contact finders, interview tools) belong to other sessions; record new ones you meet, but do not re-verify them.
3. **Open-source projects.** Significant job-search repositories: purpose, licence, stars, last commit date, maintenance, terms-of-service exposure (scrapers of sites that forbid scraping), security, and verdict.
4. **Agents and MCP servers.** Which official or community MCP servers and agent integrations exist for job platforms and applicant-tracking systems; what each can read or do; authentication; whether the platform permits it; security risks (credential handling, prompt injection from postings); maturity; verdict.
5. **Official job-data APIs.** Boards and governments that offer job-search APIs or feeds to individuals (for example Adzuna, USAJOBS, Reed, Remotive, Jooble, Careerjet, Arbeitnow), with access terms and coverage of GenAI roles.
6. **Browser agents and auto-apply.** What general browser agents and auto-apply services do at the research date; platform terms; how employers' systems detect and treat automated or duplicate applications; evidence on outcomes; reputational risk with employers.
7. **Outcome evidence.** Any independent evidence that a tool category improves interviews or offers; vendor reports labelled as such; Huntr, Teal and similar reports with samples.
8. **Privacy and security.** Browser-extension permissions, résumé data retention and resale, breaches and complaints; red flags.
9. **A minimal stack.** A practice-curated recommended tool stack for a GenAI job seeker (free and paid), with a verdict and the evidence behind each choice, and what to avoid.

Research moves: WIDEN through repository searches, extension stores and platform policy pages; FALSIFY vendor success claims; CORROBORATE closures and acquisitions with a second source.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every tool listed under KNOWN has a refreshed status.
3. Every category in scope has its significant tools as `tool` records with verdicts and dates.
4. Open-source projects, agent integrations and official APIs are covered with terms-of-service status.
5. A minimal recommended stack is stated, with what to avoid and why.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the tool table by category (tool · category · what · price · permissions and data · status and date · verdict · grade); the open-source table (repository · purpose · licence · stars · last commit · terms risk · verdict); and the agent and API table (integration · official? · access · platform permits? · risks · verdict).
