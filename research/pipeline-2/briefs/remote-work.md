<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

How can a GenAI professional earn a foreign employer's pay without relocating: which employers and platforms hire across borders, from which countries, at what pay, under which structures (employer of record, contractor, staff augmentation, AI-training platforms, freelance), and with what legal, tax and fraud risks, with depth for India-based readers? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: data on the share of GenAI roles open to cross-border remote hiring; changes in employer-of-record pricing or law; tax or foreign-exchange rule changes in India.

## BRIEF

We are investigating cross-border remote work for GenAI roles: who hires remotely across borders, which locations they accept, how they pay and contract, how pay is set by location, and what the worker must handle (tax, foreign exchange, contracts, intellectual property, payment rails, scams). Question type: lookup and evaluative. Audience: GenAI engineers and researchers outside the main hiring hubs, especially in India, who want global pay; and readers elsewhere (Eastern Europe, Latin America, South-East Asia) for comparison.

The knowledge base's India remote playbook says the local senior pay ceiling is measurable (a Bengaluru senior software-engineer median of about ₹56 lakh and a P90 near ₹1.07 crore on Levels.fyi estimates), that above it the options are a foreign employer, contracting or relocation, and that at the same client spend direct contracting keeps more cash than an employer of record (a model). Its India remote-tax page owns the tax structures. What it lacks is evidence on who actually hires India-based people remotely for GenAI roles, at what pay, and through which channels.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}.
- **In scope:** the share of GenAI postings open to remote work and to which locations ("remote, worldwide" against "remote, US only"); employers with documented cross-border remote hiring for AI roles; location-based pay policies and published compensation calculators; employer-of-record and contractor-of-record providers (for example Deel, Remote, Oyster, Rippling, Multiplier, Papaya) and their pricing and India coverage; staff-augmentation and talent platforms (for example Turing, Toptal, Andela, Crossover, Arc, Uplers); AI-training and expert-data platforms as a structure (another session covers their rates and complaints in depth); freelance marketplaces' AI demand (for example Upwork, Contra, A.Team); why some employers will not hire in India (permanent-establishment and compliance risk); payment rails (for example Wise, Payoneer, Skydo) and foreign-inward-remittance documentation; contract terms (intellectual-property assignment, non-compete, termination); remote-job scams; remote-to-relocation paths.
- **Out of scope:** detailed tax computation (the knowledge base owns it; give pointers and flag rule changes); relocation visas (the regional dossiers cover them).
- **Source priorities:** employers' careers pages and handbooks (for example published compensation calculators); providers' own pricing and documentation (C for marketing claims); government sources for rules (A); provider reports on global hiring with samples (B or C, attributed, with COI); platform terms and complaints records; then practitioners.

## KNOWN

The knowledge base's claims, to be tested:

- K: Inside India the senior pay ceiling is measurable: the Greater Bengaluru senior software-engineer median is about ₹56.0 lakh and the P90 about ₹1.07 crore, and a local staff role typically does not reach ₹1.2 crore, on Levels.fyi job-board estimates; above that line the options are a foreign employer, contracting or relocation [B; C for the staff estimate; D for the conclusion].
- K: At the same client spend, a sole proprietor under India's presumptive taxation keeps more cash than under an employer of record, so ask for a higher budget if a client offers an employer of record [M].
- K: Set the tax structure before quoting a rate: full-time contract rates straddle the presumptive-tax ceiling, where a little more billing costs a large step in tax [C; M].
- K: Vendors quote India-based senior AI consultants at $50–100 an hour, so plan on $70–100 [C].
- K: 11.0% of AI Engineer postings in JobsPipe's data were remote [B, as of 2026-11-02].
- K: The best-documented global pathways are gated by geography; the routes open from India are remote and public-output: competitions, research reading groups and open-source discussion boards [A/B].

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Employer-of-record providers and talent platforms publish reports that promote cross-border hiring: grade them C with COI unless their method is transparent. A "remote" label often hides a country restriction: read the posting's location rules, and say what share you could verify.

## APPROACH

Cover every item, or list it under Absences:

1. **Remote share.** The share of GenAI postings that are remote, and the share open to candidates outside the employer's country, from one or more sources with query and date, overall and for India-based candidates.
2. **Who hires.** Employers with documented cross-border remote hiring for AI roles (careers pages, handbooks, posting samples), as `company` records with the countries they accept and the structure they use.
3. **Pay.** Location-based pay policies and published calculators; reported pay for remote GenAI roles held by people in India and other lower-cost countries (sources, n, dates); platform rates for contractors and AI-training work, as `pay` records.
4. **Structures.** For each structure (employer of record, contractor of record, direct contractor, staff augmentation, AI-training platform, freelance marketplace): how it works, who bears costs, typical fees, the worker's protections, and India-specific implications, as `practice` and `tool` records.
5. **Employer refusals.** Why employers decline to hire in certain countries (permanent establishment, compliance, data access, sanctions, payroll) and which structures solve which objection.
6. **India rules, as pointers.** Foreign-exchange rules on export-of-services receipts, GST on exports (letter of undertaking), income-tax regimes for professionals, social-security treatment for employer-of-record employees; flag any change since 2025-01-01 with the official source. Do not compute tax.
7. **Contracts.** Intellectual-property assignment and pre-existing-materials carve-outs, non-competes, termination, liability caps, and AI-output disclaimers: what is standard on each structure.
8. **Payment rails.** Fees, speed, foreign-inward-remittance documentation and limits for the main rails used by India-based contractors.
9. **Payment and contract fraud.** Fraud specific to cross-border contracting (fake clients, overpayment and payment-reversal schemes, unpaid work), and complaints and enforcement against platforms. General job scams belong to another session.
10. **Remote to relocation.** Evidence that remote hires are later relocated or sponsored, and by which employers.

Research moves: DEEPEN each "remote, worldwide" claim to the posting's location rules; CORROBORATE platform rates with workers' public reports and complaint records; WIDEN to Latin American and Eastern European remote-work evidence for comparison.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. The remote share and the cross-border share of GenAI postings are reported with method and date.
3. At least 30 employers with documented cross-border remote hiring for AI roles are recorded, with accepted countries and structure.
4. Every structure in scope is explained with costs, protections and India implications, and every listed tool has a refreshed status.
5. Pay evidence for remote GenAI work from India is reported with sources, or its absence is confirmed.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the structure table (structure · how it works · who pays what · worker protections · India notes · grade); the employer table; the pay table; and the scam checklist.
