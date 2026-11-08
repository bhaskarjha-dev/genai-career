<!-- RP2 brief template: one dossier per role, or per small group of related roles. Sessions, roles and probes: research/pipeline-2/catalogue.json. The role cards under KNOWN are rendered from data/role_scores.json, data/role_titles.json and data/skills_ontology.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What does the knowledge base need to know about {{param:subject}} to tell a job seeker accurately what the job is, how much demand and pay it carries, what skills, proof and credentials it requires, how candidates are interviewed and presented, how careers in it progress, and where the jobs are? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: measured posting volume or pay that moves the role's scores; job-description evidence that changes its skill tiers; interview or career evidence that changes its track or durability.

## BRIEF

We are building a role dossier: everything a role's page in the knowledge base needs, researched from primary evidence. The knowledge base scores every role on demand, pay, durability and leverage (each with a low-mid-high range, an evidence grade and a sourced basis), keeps an India lens, ranks roles for GenAI job seekers, tiers each role's skills as Must, Important, Should, Optional or Avoid with evidence tags, and gives each role an interview track, a résumé variant, prerequisites and the proof of work it needs. For many roles these inputs rest on feeder titles, small samples or judgement (grades C, D or P). Your dossier should confirm, correct or replace them with dated, graded evidence.

Question type: lookup, measurement by sampling, and evaluation. Audience: job seekers choosing or preparing for this role, in the US, Europe and India especially, from early career to staff level.

The core of the dossier is a dated sample of real job postings, read from employers' own applicant-tracking boards or careers pages wherever possible: **at least {{param:jd_target}} postings per role**, spread across employer types (frontier labs, Big Tech, AI-native startups, enterprises and consultancies, GCCs and Indian employers) and regions (US, Europe, India, remote), with every posting's URL, its job ID where the board shows one, and the date you read it. A sample this size is good for aliases, requirement wording, seniority and degree patterns and posted pay bands; its skill shares carry wide uncertainty (about ±18 percentage points at n = 30), so report them with n and treat them as a cross-check on platform shares, not as a measurement on their own.

## SCOPE

- **Temporal anchor:** today is {{date}}. Postings must be live or dated within 90 days of the research date; other evidence from 2025-01-01 onwards; flag anything older.
- **In scope, for each role:** definition and variants; title aliases and their volumes; demand (posting counts with source and date, trend, employer mix, seniority mix, remote share); the job-description sample; skills with shares; pay (posted ranges, Levels.fyi or equivalent, India); interview loop; proof of work; credentials; entry routes and prerequisites; career progression and exits; durability; geography and sponsorship; résumé and profile signals; misconceptions and red flags; India specifics.
- **Out of scope:** roles other than those named, except as adjacent roles; generic career advice.
- **Source priorities:** employers' postings on their own boards (A per posting); employers' engineering blogs and career pages describing the role (A); platform aggregates such as JobsPipe, Fast AI Jobs and Levels.fyi (B); official wage filings (A for filings only); interview reports (B or C); practitioners in the role writing in their own name (C or D).

## KNOWN

The knowledge base's current record for each role. Every line is a claim to test; the K-numbers continue across roles.

{{role_cards}}

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. A posting sample drawn through search engines over-represents large employers and English-language postings: say how you sampled and what that biases. A skill's share of postings is not demand for a title. Titles are noisy: "AI Engineer" postings include robotics, low-code and MLOps jobs; classify each posting by what it asks for, and exclude postings that are not this role (say how many you excluded).

## APPROACH

Cover every item for each role, or list it under Absences:

1. **Definition and variants.** What the job is at the research date, the variants by employer type, and the boundary with adjacent roles; aliases seen in postings, with counts.
2. **Demand.** Live posting counts (US, India, global and any other major market) with source, query and date; the trend since 2025; employer-type mix; seniority mix (entry, mid, senior, staff and above); remote share; as `measure` records with subjects like `role:<id>`.
3. **Job-description sample.** At least {{param:jd_target}} postings per role as `jd` records: employer, title, URL, job ID, date seen, location, remote, seniority, years required, degree, Must requirements (verbatim phrases), nice-to-haves, posted pay range, applicant-tracking vendor.
4. **Skills.** From the sample, the share of postings naming each skill, tool, framework, protocol and non-technical skill (n stated), as `skill_signal` records whose `skill` is the bracketed skill ID from the role card (or `new:<name>` for a skill the card lacks), plus your suggested tier (Must, Important, Should, Optional or Avoid) with the reason.
5. **Pay.** Posted base ranges from the sample by level and region; Levels.fyi or equivalent figures for matching titles; India pay by level and employer type; as `pay` records with population, statistic, component, n and date.
6. **Interview loop.** What is specific to this role's loop at different employer types (rounds, what each assesses, AI-tool policies) and whether the knowledge base's interview track fits, as `loop` records. Another session owns employer-wide loop formats; do not repeat them.
7. **Proof of work.** What hiring managers for this role say they want to see (projects, papers, open-source work, deployed systems, evaluations), from named sources; the strongest public examples.
8. **Credentials.** How many postings in the sample name any certification (which ones), and what employers say about credentials for this role.
9. **Entry routes and prerequisites.** Degree and experience shares in the sample; typical prior roles of people hired into the role (from published analyses, not individual profiles); realistic routes from backend engineering, data science, front-end engineering, non-technical domain work, PhD research, DevOps or SRE, product management and new graduates.
10. **Progression, durability and leverage.** Levels and ladders; typical next roles and exits; signs of growth or commoditisation (for example tasks automated by AI tools); and evidence of leverage (how close the work sits to revenue or to decisions, scope of ownership), with sources.
11. **Work footprint and specialisations.** Which layers of the AI stack the postings' work sits in (application and deployment; orchestration and context; post-training; models and research; serving; infrastructure; and the evaluation, assurance and product planes), and the share of the sample in each specialisation listed in the role card's context.
12. **Geography and sponsorship.** Where postings concentrate (countries and cities); remote availability; how often employers sponsor visas for the role (for example US LCA filings for its titles; A for filings).
13. **Résumé and profile signals.** What reviewers for this role look for on a résumé and profile; headline and keyword patterns that match the postings; red flags; practice-curated evidence-line patterns for the role's Must and Important skills (patterns, not invented achievements).
14. **Misconceptions and risks.** Common myths about the role, title inflation, and red flags in postings.
15. **India.** Volume, employer mix, aliases, pay and interview differences in India.

Probes specific to this session:

{{param:probes}}

Research moves: DEEPEN aggregate counts to their platforms and dates; WIDEN titles to aliases and non-English postings; FALSIFY the knowledge base's tiers with your sample; CORROBORATE pay with two sources.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Each role has at least {{param:jd_target}} dated `jd` records with URLs, or the shortfall is explained.
3. Each role has `skill_signal` records computed from the sample with n, and suggested tiers with reasons.
4. Each role has demand and pay `measure` and `pay` records with dates, including India.
5. Interview, proof, credentials, entry routes, progression, geography and résumé signals are covered for each role with grades.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use the role IDs from KNOWN in every `role` and `subject` field (`role:<id>`). In Detailed Findings include, per role: the demand table; the skills table (skill · share · n · suggested tier · knowledge base tier · reason); the pay table; the loop table; and the sample summary (n by employer type and region, exclusions and their reasons).
