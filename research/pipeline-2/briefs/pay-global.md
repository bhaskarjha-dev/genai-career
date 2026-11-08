<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What do GenAI roles pay at the research date in the US, Canada, the UK, the main European hubs, Israel, Singapore, the Gulf, Japan and Australia, by role, level, city and employer type, and what does the evidence say about negotiating pay in each region? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: new pay datasets, posted ranges under new pay-transparency laws, shifts in frontier-lab equity, or negotiation studies.

## BRIEF

We are refreshing and widening the knowledge base's pay evidence outside India (a separate session covers India). Its US figures are solid (Levels.fyi and a posted-salary corpus, Grade B), but its UK, European, Singapore and Gulf figures are thin, and its per-role pay for most of its 29 roles rests on feeder titles. The aim is dated, graded pay records by role, level, city and employer type, with every figure's population, component, statistic, sample size and date, plus the regional negotiation evidence that the knowledge base lacks. Question type: lookup and evaluative. Audience: GenAI job seekers comparing offers and markets, and the knowledge base's pay pillar for its role ranking.

Roles to cover (put the role ID in the `role` field; prioritise the first twelve):

{{roles}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-07-01 to {{date}} for pay; older figures only as history, labelled.
- **Places:** the US (San Francisco Bay Area, Seattle, New York, Boston, Austin and national), Canada (Toronto, Vancouver, Montreal), the UK (London, Cambridge), Ireland (Dublin), Germany (Berlin, Munich), the Netherlands (Amsterdam), France (Paris), Switzerland (Zurich), Sweden (Stockholm), Poland (Warsaw), Israel (Tel Aviv), Singapore, the UAE (Dubai, Abu Dhabi), Saudi Arabia (Riyadh), Japan (Tokyo) and Australia (Sydney).
- **In scope:** base, bonus and equity; total compensation; posted salary ranges where pay-transparency laws put them in postings (US states and cities, Canadian provinces; for the EU directive, report only whether postings in each place carry ranges, since another session owns the law); US LCA filed wages for AI titles (A for filings, never for what people earn); frontier-lab and AI-startup packages (equity, tenders, retention grants); level ladders and promotion steps; sign-on and relocation packages; negotiation norms and evidence per region.
- **Out of scope:** India (another session); independent and fractional rates (the knowledge base's freelance page owns them, and the independent-roles dossier refreshes them).
- **Source priorities:** posted ranges observed on employers' own postings (A for the posting, with n); official statistics where they cover AI roles (A); Levels.fyi and other platform aggregates with n (B); compensation-data vendors with stated methods, such as Carta, Pave and European vendors (B or C); salary guides from recruitment firms (C); media reports of individual packages (C, attributed).

## KNOWN

The knowledge base's claims, to be tested:

- K: US ML engineer pay is $280K as the Levels.fyi median of self-reported total compensation (n = 1,063, 19 Oct 2026), $213–288K as a median posted base range excluding equity (a posted-salary corpus, 5 Aug 2026), and a visa wage filing (LCA) shows a legal floor, not pay [B].
- K: The US AI Engineer title earns 0.55–0.56× the ML Engineer title at every percentile, yet within Google the ML Engineer premium is 26–39%, so about half of the title gap is employer mix [B].
- K: Median posted base is nearly identical for AI Engineer, infrastructure or platform and ML Engineer postings ($200–288K); forward-deployed engineer postings are lower at $180–248K [B].
- K: Frontier labs pay about 3× the US ML Engineer median in total compensation, almost entirely through equity; paper equity is 60% of an OpenAI L5 package and 72% of an Anthropic Staff package [B].
- K: The US software-engineer ladder (all companies, Levels.fyi 2025) is $155K → $226K → $312K → $457K → $551K, and level-median steps are ×1.38–1.46 [B; B/C].
- K: The AI premium over non-AI engineers rises from 6.2% at Entry to 18.7% at Staff [B].
- K: A systems or infrastructure premium of +13% to +31% in base appears in two datasets (OpenAI visa filings and Robert Half's Zurich guide), with seniority uncontrolled; it is not validated [B/C/D].
- K: Coaching services report that about 80–87% of candidates who negotiate receive a positive adjustment, but the lift depends on competing offers; Levels.fyi's coaching cohort reports median uplifts of +21–24% from self-selected clients [B/C].
- K: Counter once, in writing, 10–20% above the offer, anchored on external data [B/C]; many US jurisdictions ban salary-history questions [B].

{{tools}}

Context (what the knowledge base already holds or lacks; no verdict needed):

- Its pay evidence for the UK, Europe, Singapore and the Gulf is thin, and so is its negotiation evidence for India and Europe.

## CALIBRATION

Apply the five calibration rules in the protocol. Pay figures mislead when the population, component or statistic is unstated: every `pay` record needs role, location, level where known, statistic, base or total, currency, period, n where known, source and date. Self-reported platforms over-represent large employers and senior staff; posted ranges are wide and exclude equity; recruitment-firm guides rarely state samples. Say which bias applies to each source.

## APPROACH

Cover every item, or list it under Absences:

1. **US by role.** For each role above, posted base ranges from a sample of postings you observe (n, date, employer types) and Levels.fyi figures where a matching title exists, by level and for the five US cities.
2. **Employer types.** Frontier labs, Big Tech, AI-native startups by stage, enterprises and consultancies: the structure and size of packages, equity form (RSUs, options, profit units), tender and liquidity events, retention grants, with sources.
3. **LCA filings.** Filed wage ranges for AI and ML job titles at the employers with the most filings in the most recent fiscal year (A for filings), clearly separated from pay.
4. **Outside the US.** For each place in scope: AI or ML engineer pay by level (median and spread), the software-engineer baseline, and frontier-lab or Big Tech premiums where visible; posted ranges where transparency laws apply; local package conventions (13th-month pay, housing allowances, pension contributions).
5. **Ladders and steps.** Level ladders and promotion steps for AI roles at major employers, and how GenAI titles map to levels.
6. **Negotiation by region.** Evidence and documented norms for the US, Canada, the UK, continental Europe (works councils, collective agreements, notice periods, counter-offers), Israel, Singapore, the Gulf (allowances, end-of-service benefits), Japan and Australia; legal constraints such as salary-history bans and pay-transparency rights; any studies of negotiation outcomes.
7. **Relocation packages.** What employers typically cover when they relocate a GenAI hire (visa, flights, temporary housing, tax equalisation), with sources.

Research moves: CORROBORATE every median with a second source or a posted-range sample; FALSIFY viral package figures (trace to the original report); WIDEN to European compensation vendors and official wage statistics.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Each of the first twelve roles has US pay records by level from at least two sources, or absences that say why not.
3. Every place in scope has AI or ML engineer pay records with population, statistic, component, n and date.
4. Negotiation norms and evidence are given per region with grades.
5. A table states, for each place, the best available pay source and its biases.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use `ttl` V3 for pay. In Detailed Findings include: a US table by role and level; one table per non-US place; the employer-type package table; the LCA table; and the negotiation table (region · norm · evidence · grade).
