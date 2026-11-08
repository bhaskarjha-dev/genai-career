<!-- RP2 brief template: one census session per issuer group. Sessions, groups, seeds and probes: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which GenAI-relevant certifications do these issuers offer at the research date ({{param:group}}), what does each involve and cost, how much hiring signal and channel value does each carry, for which role families, and how do they compare? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: a reproducible audit showing a certification in more than 10% of GenAI postings for a market segment; changes to partner-programme rules; launches, renamings and retirements.

## BRIEF

We are building a complete, dated census of certifications relevant to GenAI careers, so that readers can decide which to take, in what order, at what cost, and when to stop. Six sessions split the census by issuer group; this one covers **{{param:group}}**. A later step in the knowledge base computes value orders across every group from the records you return, using a published rubric, so the attributes matter more than your final ranking. Still give a comparison and a provisional order within this group, with your reasons.

Question type: lookup (issuer facts) and evaluative (signal and value). Audience: job seekers in every role family listed below, worldwide, with depth for India, where IT-services firms, GCCs and hyperscaler partners hire at volume and certification targets are common, and including readers who want to collect many certifications and need an order.

The knowledge base lists only a few credentials for these issuers (below). The requester's own research named credentials that the knowledge base does not list; they are in the seed list, unverified. Confirm each one with its exact official name, issuer page and status, or report it as an absence. Do not assume a seed exists because it is listed, and do not stretch a similar-sounding course or badge to fit a seed: say what exists instead.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}. Record retirements since 2025-01-01 as history.
- **In scope:** every certification, certificate or badge from these issuers that relates to generative AI, machine learning, data for AI, AI infrastructure, agentic AI, AI security, AI governance or AI business strategy, at every level from foundational to expert, including beta and announced credentials. Keep proctored exams apart from course-completion certificates and skill badges, and say which each is. General credentials from these issuers are in scope only where the probes below name them (for example as prerequisites or common pairings).
- **Out of scope:** bootcamps and courses without a credential (another session covers learning resources); credentials from issuers in other groups, except to note overlaps.
- **Source priorities:** the issuer's own certification and exam-guide pages (A); the issuer's partner-programme documentation (A); job postings you observe yourself (B for counts; state your method); analyst and recruiter reports (C); training vendors and exam-preparation sites (C, with COI).

## KNOWN

The knowledge base's claims, to be tested:

{{claims}}

{{context}}

{{tools}}

Credentials the knowledge base lists for these issuers, with their statuses (each line is a claim to test):

{{credentials}}

Seed list to verify (requester-stated or from the knowledge base's backlog; unverified):

{{param:seeds}}

Role families (use these names in `families`):

{{families}}

## CALIBRATION

Apply the five calibration rules in the protocol. Issuers, training vendors and exam-preparation sites all gain from certification demand: grade their value claims C with COI. If you are a model built by one of these issuers, say so in `authored_by_model` and treat claims about that issuer's credentials as COI. A certification's existence and terms are A only from the issuer's own page.

## APPROACH

Cover every item, or list it under Absences:

1. **Census.** Every credential in scope as a `credential` record with every field you can establish: exact official name, exam code, level, format (multiple choice, performance-based lab, project, course completion, badge), proctoring, duration, number of items, passing score, fee (and `fee_local` where the issuer lists an INR or other local price), validity and renewal, prerequisites, launch date, retirement date, former name, typical preparation hours (with source), the exam guide's domains and weights (`domains`), how to register (`access`, for example through a partner academy or an employer programme), and the issuer URL.
2. **Seeds.** Each seed confirmed with its exact name, or an `absence` record that says where you searched.
3. **Hiring signal.** For each credential, the number of postings that name it in a sample of GenAI job postings that you draw yourself: state the boards, query, region, date and sample size, separately for the US and India where possible. Expect few hits; zero counts with their sample size are informative, so report them. Add any published data on mention rates. Record as `jd_signal` on the credential and as `measure` records.
4. **Channel value.** Partner-programme rules that count individual certifications towards partner tiers, competencies or specialisations; employer statements on certification targets, bonuses or reimbursement (IT services, GCCs, consultancies); public-sector or client-contract requirements ("certified resource" clauses).
5. **Rigour and verifiability.** Hands-on or multiple choice; proctoring; public verification (for example Credly); exam-security incidents and the prevalence of exam dumps.
6. **Skill alignment.** Which role families above the exam domains serve (in `families`).
7. **Cost to earn.** Fee, typical preparation hours, renewal cost, free vouchers and challenges, and regional pricing.
8. **Currency.** Launch and update dates, announced retirements, and how often this issuer has reorganised its credentials since 2024.
9. **Provisional order within the group.** For each role family that at least five of this group's credentials serve, a provisional top five with a one-line reason each and the main uncertainty. Do not compute weighted scores: the knowledge base computes its own order from your records.

Probes specific to this group:

{{param:probes}}

Research moves: DEEPEN every credential to the issuer's page; WIDEN with issuer, product and partner-programme vocabulary; FALSIFY claims of hiring value with your own postings sample.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every credential in scope has a `credential` record or an `absence` record, and every seed is resolved.
3. The hiring-signal sample is reported with its method, or its absence is explained.
4. Partner-programme and employer-channel value is documented with sources.
5. The provisional top five per role family is given with reasons.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the credential table (name · code · level · format · proctored · fee · validity · prerequisites · status and date · grade); the hiring-signal table (credential · US count / n · India count / n · method · date); the channel-value table; and the provisional orders.
