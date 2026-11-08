<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What are the realistic routes into GenAI roles for four starting points the knowledge base has not researched: DevOps and site-reliability engineers, product managers, engineers in IT-services firms (a large group in India), and students and new graduates? Which target roles fit each, what skill and proof gaps must each close, how long does it take, and what does the evidence say about the entry-level market? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: data on transitions from these backgrounds; changes in entry-level hiring; employer statements on hiring from these backgrounds.

## BRIEF

The knowledge base models transitions from five backgrounds (backend or systems engineer, data scientist or BI analyst, front-end or full-stack engineer, non-technical professional, academic researcher or PhD), with four gates (G1 a measured v0 by month 3, G2 an operable v1 by month 6, G3 a second system and external proof by month 9, G4 an offer or a funnel diagnosis by month 12) and modelled months to a first offer. Its routes for DevOps and SRE engineers, product managers and students are provisional and practice-curated [P], and it has no route for IT-services engineers. The aim is to replace them with researched routes. Question type: evaluative and causal (what works, and what limits it). Audience: people in those four groups, worldwide, with depth for India, where campus hiring, the IT-services workforce and the entry-level share of AI roles differ from the US.

Target roles in the knowledge base (use these role names):

{{roles}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2024-01-01 to {{date}}, plus earlier peer-reviewed labour-market studies.
- **In scope:** for DevOps and SRE engineers, moves into AI infrastructure, ML platform, inference and LLM operations roles, and into forward-deployed and solutions roles; for product managers, moves into AI product management and adjacent roles (AI product operations, solutions, evaluation); for students and new graduates, the entry-level market for AI roles (hiring trends, internships, return offers, campus hiring in India, graduate programmes), routes (internships, research assistantships, open source, competitions, fellowships), degree choices and their evidence, and the proof a new graduate needs; skill deltas, time to first offer, failure modes and evidence of success for each group.
- **Out of scope:** the five backgrounds already modelled, except for comparison.
- **Source priorities:** labour-market studies and official statistics (A or B); employer statements and programme pages (A); job-posting requirements (A per posting, with a sample); surveys with a method (B or C); first-person transition accounts in the author's own name (C or D, noting survivorship).

## KNOWN

The knowledge base's claims, to be tested:

- K: Ask for an internal move first: spend 6–8 weeks seeking a scoped AI assignment at your employer; four practitioner accounts name internal transfer as the fastest route [D].
- K: Move laterally rather than restart as a junior: about 66% of US AI-engineering postings (January–July 2026) are individual-contributor roles, 35% mid-level and 31% senior [C].
- K: Employment of 22–25-year-olds in the most AI-exposed occupations is 19% lower than if it had kept pace with less-exposed peers, with no comparable gap for experienced workers [A].
- K: India has about twice the US entry-level share of AI roles (21.2% against 10.4%) [B].
- K: Evaluation is the universal gate across all five modelled backgrounds and should be the spine of the portfolio [B].
- K: At 15–20 hours a week, modelled months to a first offer are about 6 for backend engineers, 7 for front-end and non-technical AI-adjacent routes, 8 for data scientists and PhDs, 11 for BI analysts and 22 for engineering from zero code; every value assumes the person persists and eventually succeeds [M].
- K: Do not mix funnels: expert-contract work, AI product management, forward-deployed engineering and AI engineering have different gatekeepers and different proof [M].

Context (what the knowledge base already holds or lacks; no verdict needed):

- Its routes for DevOps and SRE engineers, product managers and students are provisional and practice-curated [P].

## CALIBRATION

Apply the five calibration rules in the protocol. Transition stories are survivor accounts: weigh them below data and employer statements. Entry-level market claims swing with news cycles: use dated statistics and say which population (country, degree, field) each covers.

## APPROACH

Cover every item, or list it under Absences:

1. **DevOps and SRE.** Which target roles have the highest overlap with DevOps and SRE skills (compare posting requirements, with a sample), the skill and proof deltas, evidence of people making the move and how long it took, and the gates adapted to this background.
2. **Product managers.** What AI product-manager postings require beyond general product management (technical depth, evaluation, data, AI user experience), the interview differences, evidence of transitions, and alternatives (AI product operations, solutions, evaluation roles).
3. **IT-services engineers.** Routes from IT-services and consulting delivery roles (for example at TCS, Infosys, Wipro, HCLTech, Accenture or Cognizant) into GenAI roles: internal GenAI practices, moves to GCCs and product companies, the skill and proof gaps that hold people back, and evidence of successful moves.
4. **The entry-level market.** Hiring trends for new graduates in AI and software roles in the US, Europe and India since 2024, with official statistics and studies; internship and return-offer rates; new-graduate programmes at AI employers; campus placements for AI roles in India (published placement reports).
5. **Routes for students.** Internships, research assistantships, open-source programmes, competitions and fellowships as entry routes, with outcome evidence; the role of a master's degree or PhD, with evidence on returns where it exists; and a master's abroad as a route into AI roles and post-study work rights (costs, post-study work routes, outcome evidence).
6. **Proof for new graduates.** What employers say they want from new graduates for AI roles, from named sources.
7. **Timelines.** Evidence-based or modelled time to first offer for each group, with assumptions stated (grade M where modelled).
8. **Failure modes.** Common reasons transitions from each group fail, with sources.
9. **Practice-curated routes.** For each group, a route in the knowledge base's gate format (G1–G4 adapted), each element tagged with evidence or [P].

Research moves: WIDEN to Indian campus-placement data and European graduate statistics; FALSIFY doom narratives about entry-level AI jobs with official data, and optimistic ones with the same; CORROBORATE transition claims with employer-side evidence.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Each of the four groups has its best-fit target roles ranked with reasons, its skill and proof deltas, its timeline and its failure modes.
3. The entry-level market is described with dated statistics for the US, Europe and India.
4. Each group has a route in the gate format with evidence tags.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include, per group: the target-role fit table (role · overlap · gaps · evidence · grade); the route; and for the entry-level market, a statistics table (statistic · population · value · date · source · grade).
