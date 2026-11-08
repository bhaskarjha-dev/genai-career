<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

How should a GenAI job seeker set up and use LinkedIn so that recruiters and hiring managers find them for the right roles, can check them quickly and reach out, and which widely shared LinkedIn tactics have evidence behind them? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: platform documentation or data showing which profile fields, settings and activities change recruiter-search visibility, message response or interview rates.

## BRIEF

We are investigating LinkedIn as a job-search instrument for GenAI roles (the role list is under KNOWN), from three sides:

1. **Being found:** how recruiters search and filter in LinkedIn Recruiter, Recruiter Lite and LinkedIn Jobs; which profile fields are indexed and weighted; what settings such as Open to Work and job preferences do; and what LinkedIn's AI recruiting features launched between 2024 and the research date read from a profile.
2. **Being checked:** what a hiring manager or recruiter looks for once they open a profile.
3. **Being remembered:** whether posting, commenting and networking activity measurably raise inbound opportunities, and what the feed ranking rewards or penalises.

Question type: evaluative, with lookups of platform documentation. Audience: job seekers from early career to staff level, worldwide, with depth for India, where LinkedIn is a primary hiring channel. The knowledge base's networking guidance rests mostly on practice-curated rules [P] and states that nobody has measured how often recruiters open profiles or which headline formats work. The aim is to replace as many [P] rules as the evidence allows with documented mechanics (A), datasets (B) or attributed practitioner analysis (C), and to label the rest honestly.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2024-01-01 to {{date}}. LinkedIn changes features often: date every feature claim and flag anything older than 2025-07-01 as possibly stale.
- **In scope:** profile fields (headline, About, experience, skills, Featured, projects, certifications, recommendations, custom URL, location, photo, banner); Open to Work in both forms (recruiters only, public frame); job alerts; Easy Apply against applying on the employer's site; LinkedIn Recruiter and its AI features (natural-language search, AI-drafted outreach, hiring-assistant agents); Premium Career; the feed ranking (dwell time, comments, external links, formats, cadence, engagement pods); connection and InMail limits; the end of Creator mode; skill assessments, verification badges and LinkedIn Learning certificates; recruiter behaviour in India.
- **Out of scope:** paid advertising; sales prospecting, except where job seekers use the same tools; personal-branding advice unconnected to hiring.
- **Source priorities:** LinkedIn's Help Center, Talent Blog, Talent Solutions documentation, Engineering Blog and Economic Graph research; peer-reviewed studies; large practitioner datasets that publish their sample and method; recruiter surveys with a method; then recruiter and practitioner posts (C or D).

## KNOWN

The knowledge base's claims, to be tested:

- K: LinkedIn profiles are where a reviewer checks a candidate rather than where the candidate gets found. LinkedIn's documented problem is application volume: about 11,000 applications a minute, up 45% year on year (a late-2024 figure). In 2026, 74% of India recruiters told LinkedIn they struggle to find qualified candidates, with AI-generated applications a key challenge [B, as of October 2026].
- K: Use LinkedIn and X as a distribution layer for your own work, not as a separate content programme [B].
- K: Published 2026 recruiter Boolean strings for AI/ML engineers key on titles, languages and frameworks and contain no certification acronyms [C].
- K: AI matching layers in hiring software score title similarity (Eightfold) and recruiter-set skills, experience, title and location (Phenom) [A, vendor documentation retrieved 2026-10-23].
- K: Keep one identity everywhere (the same name, titles, employers and dates on the résumé, LinkedIn and GitHub). That consistency lowers false fraud flags is an inference held with low confidence [D].
- K: Nobody has measured how often recruiters or hiring managers open LinkedIn, GitHub or a blog, or which headline format performs better; the prevalence of engagement farming on LinkedIn and X was searched for and not found [as of October 2026].
- K: A randomised experiment on LinkedIn's People You May Know feature (more than 20 million people over five years; *Science*, 15 September 2022) found that moderately weak ties produced the most job mobility [A].
- K: LinkedIn's user agreement prohibits automation tools, and automated activity risks account restriction [A, as of October 2026].
- K: Pin's dataset of more than 4 million recruiter-to-candidate messages (June 2025 to May 2026) shows a 17.08% reply rate on LinkedIn; that rate does not transfer to messages a candidate initiates [B for the figure; D for the transfer judgement].

{{tools}}

Role families the knowledge base covers (use these names in your records):

{{families}}

## CALIBRATION

Apply the five calibration rules in the protocol. Most advice in this field comes from people who sell courses, tools or coaching: attribute it, grade it C or D, and look for the method behind every number. A claim about "the algorithm" counts only with LinkedIn's own documentation, a disclosed sample or a controlled comparison.

## APPROACH

Cover every item, or list it under Absences:

1. **Recruiter search.** Which fields LinkedIn Recruiter indexes and lets recruiters filter on (title, skills, company, location, years of experience, school, Open to Work, languages); how keyword and AI semantic search treat them; how LinkedIn's AI recruiting features build candidate lists and draft outreach. Quote the documentation.
2. **Open to Work.** What each form does, LinkedIn's own figures on its effect (with date and method), counter-evidence such as stigma studies or recruiter surveys, and views specific to India.
3. **What reviewers weigh.** Evidence on the headline, About, experience bullets, skills section (count limits, endorsements, assessments, verification), Featured, recommendations, photo and custom URL. Separate measured findings from opinion.
4. **Skills and keywords.** How the skills section feeds search and job matching ("top applicant", skills match); whether GenAI terms (LLM, RAG, agents, evaluation, MCP) are recognised skills; the risks of keyword stuffing.
5. **Applying on LinkedIn.** Easy Apply against the employer's own site: evidence on response rates, applicant volume per GenAI posting, promoted and reposted jobs, ghost jobs, and the status at the research date of the Texas Attorney General investigation of LinkedIn reported in July 2026.
6. **Content and the feed.** What LinkedIn engineering has published about feed ranking since 2024; large-sample studies of formats, length, external links, comments, dwell time and cadence; the documented treatment of engagement pods and automation; and any evidence that posting changes recruiter outreach or interview invitations.
7. **Engagement.** Commenting on others' posts, connection requests with and without notes, InMail against messages to connections, weekly invitation limits: what is documented and what is folklore.
8. **Paid tiers.** Premium Career features (InMail credits, applicant insights, AI writing tools) and any independent evidence of benefit.
9. **Trust.** Identity and workplace verification, the prevalence of fake profiles and recruiter scams, and how employers use verification.
10. **India.** LinkedIn's role against Naukri, Instahyre and others for GenAI hiring; recruiter behaviour; conventions such as notice period and CTC on profiles.
11. **GenAI profile patterns.** Headline and About patterns among people hired into the roles listed above in 2025–2026 at labs, Big Tech and AI startups, described in aggregate from published analyses (do not profile individuals).
12. **Tools.** LinkedIn add-ons, profile optimisers and automation tools: what they do, terms-of-service status, evidence and a verdict, as `tool` records at stage 7.

Research moves: DEEPEN every algorithm claim to its origin; FALSIFY popular claims (for example "posting daily triples recruiter views"); WIDEN to recruiter forums and statements by LinkedIn employees.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Recruiter-search mechanics are documented from LinkedIn sources, or their absence is stated.
3. Every tactic reported is a `practice` record with its grade, its evidence and a verdict, and a table separates measured tactics from folklore.
4. Open to Work, Easy Apply and content effects each have the best available evidence and its limits.
5. A recommended LinkedIn set-up and weekly routine for a GenAI job seeker is stated as decision rules, each graded.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: a table of profile fields (field · what search and reviewers do with it · evidence · grade); a table of tactics (tactic · claimed effect · evidence · grade · verdict); and a table of tools.
