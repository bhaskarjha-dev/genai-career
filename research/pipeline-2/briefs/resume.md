<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What résumé format, order, length, design and content give a GenAI candidate the best chance of being read and shortlisted in 2026, by human reviewers and by applicant-tracking and AI screening software, in each major hiring region, and what should differ between role families? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: experiments or large datasets linking résumé features to callbacks; vendor documentation of AI screening criteria; evidence on how reviewers treat AI-written résumés.

## BRIEF

We are investigating the résumé as a document that must survive three readers: a parser, an AI ranking layer and a human reviewer who spends little time on it. Question type: evaluative and causal (which features change callbacks, and by how much). Audience: GenAI job seekers from new graduate to staff level and leaders, applying in the US, the UK, the EU, India, the Gulf, Singapore, Japan, Australia and Canada.

The knowledge base already documents applicant-tracking mechanics from vendor documentation (knockout questions are the only documented automatic rejection; parse failures leave fields empty) and runs a layered model: one private master inventory, one universal résumé, two or three family variants and light tailoring. Its formats and templates are practice-curated [P]. The aim is to ground format, length, order, bullet style, GenAI-specific content and regional norms in the best available evidence (field experiments, audit studies, large datasets, vendor documentation), to document how AI screening and AI-written résumés changed the picture in 2024–2026, and to grade the rest honestly. The output feeds a planned résumé generator that builds each résumé from one tagged inventory.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: any date for experiments and audit studies on résumé features; 2024-01-01 to {{date}} for screening software, AI-written résumés and recruiter surveys.
- **In scope:** format (reverse-chronological, hybrid, functional); length by seniority and region; section order (header, headline or summary, skills, experience, projects, education, publications, credentials); design (columns, fonts, colour, file type, text layer, photos, links, QR codes); bullet construction (action, method, measured result; X-Y-Z and similar patterns) and quantification; keyword mirroring; summaries; cover letters; tailoring depth; GenAI-specific content (evaluation metrics, latency and cost figures, scale, model and framework names, safety work, honest disclosure of AI-assisted work); how LLM-based screening ranks résumés and its documented biases; prompt-injection and hidden text in résumés and how employers detect and treat them; recruiter attitudes to AI-written résumés; regional conventions (photo, date of birth, nationality, visa status, CTC and notice period, Europass, Japan's rirekisho); research CVs against engineering résumés against product and governance résumés.
- **Out of scope:** LinkedIn profiles (another session); interview preparation.
- **Source priorities:** field experiments, correspondence and audit studies, and peer-reviewed work; applicant-tracking and AI-screening vendor documentation; large vendor datasets with a method; government guidance on discriminatory information (for example Singapore's tripartite guidelines, Germany's equal-treatment law); recruiter surveys with a method; then practitioners (C or D).

## KNOWN

The knowledge base's claims, to be tested:

- K: Knockout questions are the only documented automatic rejection: Greenhouse, Lever, Ashby, Workday and Taleo/Oracle document auto-reject only as rules the employer configures on application-form answers; none of the vendor documents retrieved describes rejection for résumé wording or for a failed parse [A, documentation retrieved 2026-10-23].
- K: A failed parse leaves fields empty for manual entry; where an AI layer is on, it reads the extracted facts, so a poor conversion can change who is read first. Submit a single-column file with a real text layer, and test it [A for the mechanics; D for the effect].
- K: AI ranking layers compare the recruiter's requirement list with extracted titles, skills, years, dates and employers, plus learned similarity; give each requirement in the posting one verifiable evidence line in a recent role [A; D for the rule].
- K: An "ATS score" from a checker is not a gate: no study links checker scores to real screening outcomes or interview rates; use a checker only as a list of gaps [C].
- K: Hidden text, keyword blocks and mass auto-apply are counter-productive: every text extractor tested returned white text, detectors exist, and the effect on ranking in production is unmeasured [A/B].
- K: Run one private master inventory, one universal résumé anchored on one identity, and two or three variants, one per role family the candidate can back with a flagship project [D].
- K: Tailor every application lightly and truthfully in 10–20 minutes; in Huntr's vendor data, tailored applications had a 4.23% interview rate against 2.07% untailored (correlational) [C].
- K: Recruiter searches key on titles, and screening software scores title similarity, so the universal résumé cannot hold "the best of all roles" [A; C].
- K: The X-Y-Z bullet pattern (accomplished X, as measured by Y, by doing Z) is an optional practice-curated form [P].
- K: In a field experiment with about half a million job seekers on one online labour market, non-generative writing help raised hires by 8% and wages by 10%; after an AI cover-letter tool launched on one platform, cover letters became less correlated with hiring [B].
- K: 72% of AI-engineering postings state a degree requirement [C].

Résumé variants the knowledge base uses (families and their headline patterns are generated from its data):

{{resume_variants}}

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Résumé advice is dominated by sellers of résumé services and templates: attribute their claims and grade them C or D. A recruiter survey reports what recruiters say, not what changes callbacks; keep the two apart. Eye-tracking and "six seconds" figures must be traced to their original study and sample.

## APPROACH

Cover every item, or list it under Absences:

1. **Experiments and audit studies.** Findings on length, format, layout, bullet style, quantification, summaries, skills sections, photos, gaps, degree signals and cover letters, with samples, settings and dates.
2. **Reviewer behaviour.** Evidence on how long reviewers read and where they look (trace every figure to its study), and how hiring managers and recruiters for technical roles differ.
3. **Format, length and order.** The best-supported choices by seniority (new graduate, mid, senior, staff, leader), by role family, and by region, with grades; when two pages are expected or penalised.
4. **Design and file type.** Single against multi-column layouts in vendor parsers; fonts and text layers; PDF against DOCX by applicant-tracking system; photos and links; whether templates from popular design tools keep a text layer.
5. **Bullets and evidence.** What makes a bullet credible to a technical reviewer; quantification without fabrication; mirroring a posting's wording; how to show proof (links to repositories, papers, demos) without breaking parsing.
6. **GenAI-specific content.** What hiring managers for GenAI roles say they look for on a résumé in 2025–2026 (evaluation results, cost and latency engineering, scale, production incidents, safety and governance work, open-source and papers), and what reads as inflation (tool lists without evidence, legacy titles such as "Prompt Engineer"). Use named sources.
7. **AI screening, as it affects the document.** How LLM-based screening features read résumés (documentation); published audits of bias in LLM résumé ranking; prompt injection or hidden instructions in résumés, detection features and employer policies. The law on automated screening belongs to another session: note only what changes résumé advice.
8. **AI-written résumés and cover letters.** Evidence on detection, recruiter attitudes, effects on signal value (for example studies of cover letters after generative tools spread), and employers' stated policies on AI use in applications.
9. **Regional conventions.** For the US, Canada, the UK, Germany and the DACH region, France, the Netherlands, the Nordics, India, the Gulf states, Singapore, Japan and Australia: photo, date of birth, nationality, visa status, marital status, salary and notice period, length and format norms, with official or authoritative sources where they exist.
10. **Role families.** How a résumé differs for each role family below (for example publications first for research roles, customer outcomes for forward-deployed and solutions roles, governance artefacts for governance roles, product outcomes for product roles).
11. **Tools.** Résumé builders, open-source résumé generators (for example JSON Resume and RenderCV), parse checkers and AI writing tools, as `tool` records at stage 6, with verdicts.

Research moves: DEEPEN every statistic to its study; FALSIFY one-page dogma and keyword-density advice; WIDEN to labour-economics and HR research journals and to non-English regional guidance.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every résumé feature in scope has its best evidence and grade, with experiments separated from opinion.
3. A section-order skeleton for a one- to two-page GenAI résumé is given per seniority band, and differences per role family are stated, each element tagged with evidence or [P].
4. A regional-conventions table covers every region in scope.
5. The state of AI screening and AI-written résumés at the research date is summarised with documentation and dates.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: a table of résumé features (feature · best evidence · effect · grade); the skeletons; the regional table (region · photo · date of birth · nationality and visa · salary and notice · length · source · grade); and a table of AI-screening products and what their documentation says they score.

Role families the knowledge base covers:

{{families}}
