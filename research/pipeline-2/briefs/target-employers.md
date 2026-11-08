<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which employers hire for GenAI roles at volume, in which locations, through which applicant-tracking systems, and with what evidence of visa sponsorship and remote hiring; and which public datasets let a job seeker build and maintain a target list lawfully? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: new employer-level hiring or sponsorship data; changes in the terms or legality of company and contact datasets.

## BRIEF

We are investigating the employer side of a GenAI job search: who is hiring, where, how many GenAI roles each has open, how each hires (applicant-tracking vendor and public board URL), whether each sponsors visas (from official registers), its remote policy and its presence in India. We also want the data corpora a job seeker can use: company and funding databases, official sponsor registers, curated employer lists and contact-data products, with their legal and terms-of-service status. Question type: lookup (a structured census) and evaluative (which sources to trust). Audience: job seekers worldwide, with depth for India-based readers targeting India, remote work and relocation.

The knowledge base's employer landscape defines six employer types (frontier labs, Big Tech, AI-native startups by stage, enterprises and global capability centres (GCCs), IT services, public sector) and maps how each hires and pays, but it has no named target-company lists, and its evidence is thinnest for IT services and the public sector. The employer records you return will also seed a planned script that samples public job postings from employers' own boards, so each record's applicant-tracking vendor and board URL matter.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}} for hiring and sponsorship; the most recent complete fiscal year for official registers.
- **In scope:** employers of all six types in the US, Canada, the UK, the EU, Switzerland, Israel, the Gulf, India, Singapore, Japan, South Korea and Australia; open GenAI roles per employer (observed on the employer's own careers page, dated); the applicant-tracking vendor and public board URL; sponsorship evidence from official registers (US Department of Labor LCA disclosure data and the USCIS H-1B Employer Data Hub; the UK Register of Licensed Sponsors; the Netherlands IND public register of recognised sponsors; any equivalent elsewhere); remote and India-hiring policy; curated lists (for example Forbes AI 50, CB Insights AI 100, Y Combinator batches, NASSCOM and Zinnov GCC reports); company, funding and hiring databases (for example Crunchbase, Dealroom, Tracxn, layoffs trackers); contact-data products (for example Apollo, RocketReach, Hunter, ZoomInfo, Lusha) and their terms, accuracy and data-protection enforcement.
- **Out of scope:** pay by employer (the pay sessions cover it); individual recruiters' or employees' personal details.
- **Source priorities:** employers' own careers pages and boards; official registers and their downloadable data; curated lists from their publishers; database vendors' own terms and documentation; regulator decisions; then secondary reporting.

## KNOWN

The knowledge base's claims, to be tested:

- K: The GenAI employer market is usefully split into six types: frontier labs, Big Tech, AI-native startups by stage, enterprises and GCCs, IT services, and the public sector; evidence is thickest for labs, Big Tech and AI startups and thinnest for IT services and the public sector [D for the taxonomy, as of October 2026].
- K: Employer type moves pay more than title: the US AI Engineer title earns 0.55–0.56× the ML Engineer title, and about half of that gap is employer mix [B].
- K: Frontier labs pay about 3× the US ML Engineer median in total compensation, almost entirely through equity [B].
- K: In India the employer type is the pay decision, and "nearly 70%" of India GCCs were reported stuck at the pilot stage of AI work [B].
- K: Fast AI Jobs listed 326 AI Engineer postings at 183 AI startups on 2026-10-19 [B].
- K: US LCA wage filings are evidence of what employers filed, not of what people earn [A for the filings].

Context (what the knowledge base already holds or lacks; no verdict needed):

- It has no named target-company list; building one is planned work.

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. An open-roles count is a snapshot: give the date and the filter you used. Register data shows filings or licences, not willingness to sponsor a particular role; say so. Do not record personal data about employees or recruiters.

## APPROACH

Cover every item, or list it under Absences:

1. **Employer census.** At least 40 employers that hire for GenAI roles at volume (more if the evidence allows), spanning all six types and the regions in scope, prioritising those with the most open GenAI roles, each as a `company` record: employer type, headquarters, hiring regions, open GenAI roles observed on its careers page (count, date, filter), applicant-tracking vendor and public board URL, sponsorship evidence, remote policy, India presence. A later script will extend the list from employers' public job boards.
2. **India.** GCCs, Indian AI startups, IT-services firms' GenAI practices and Indian offices of global firms that hire for GenAI roles: names, cities, volume evidence, and how each hires.
3. **Sponsorship registers.** How to use each official register (what it contains, how often it updates, download links), and for US LCA data the employers with the most filings for AI and ML job titles in the most recent fiscal year, with counts and the title filter used.
4. **Curated lists.** The publishers, dates and methods of the main lists of AI employers, and how much they overlap with observed hiring volume.
5. **Hiring signals.** Which public signals predict that a company is hiring for GenAI (funding, headcount growth, open roles, product launches), with any evidence; layoffs and hiring freezes at the research date.
6. **Datasets and their terms.** For each company, funding and hiring dataset in scope: what it holds, price, terms of service on use and scraping, accuracy evidence, and data-protection complaints or enforcement, as `tool` records at stage 1. Contact-data products belong to the outreach session; note only what matters for building a target list.
7. **A target-list method.** A practice-curated method for building and maintaining a list of 50–100 target employers by role family, geography and visa needs, with tiers and a review cadence, each step tagged with evidence or [P].

Research moves: DEEPEN every list to its publisher and method; CORROBORATE open-role counts on the employer's own site; WIDEN beyond US-centric lists to Europe, the Gulf and Asia.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. At least 40 employers have `company` records with employer type, regions, a dated open-roles count or an explanation, the applicant-tracking vendor and board URL where public, and sponsorship evidence where an official register exists.
3. India's employer landscape is covered across GCCs, startups, IT services and global firms.
4. Every dataset in scope has its terms and legal risk stated.
5. The target-list method is stated.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the employer table (employer · type · regions · open GenAI roles and date · applicant-tracking vendor · sponsorship evidence · remote and India · grade); the register guide; and the dataset table (dataset · what · price · terms · legal risk · verdict).
