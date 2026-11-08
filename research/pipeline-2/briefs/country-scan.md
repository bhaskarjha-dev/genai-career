<!-- RP2 brief template: one country and city scan per world region. Sessions, countries, cities and claims: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which countries and cities in {{param:region}} offer a GenAI professional the best combination of job volume, pay after tax and living costs, legal access for foreign workers, remote-hiring reach and ecosystem depth, and how does the order change for different readers? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: new posting or pay data by country; visa rule changes; tax regime changes; shifts in where AI employers hire.

## BRIEF

We are gathering the measured inputs for a country and city ranking for GenAI careers, analogous to the knowledge base's role ranking. Each country (and its main AI cities where data allow) gets dated, graded measures on several pillars; the knowledge base then computes rankings for several reader lenses with a published rubric. A sister session covers the other half of the world with the same brief, so use the same sources and definitions wherever possible. Question type: lookup and evaluative. Audience: GenAI professionals choosing where to target, remotely or by relocating, with a specific lens for Indian nationals (the knowledge base's deepest readership) and a generic lens for other non-EU nationals.

Other sessions go deeper on each region's visa routes, on pay by role, and on remote cross-border work. This session gathers the cross-country measures and a one-line headline of access, so that every country is compared on the same basis.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-01-01 to {{date}}; official tax and visa thresholds as in force at the research date, noting announced changes.
- **Countries:** {{param:countries}}
- **Cities:** {{param:cities}}
- **In scope, per country (and per city where data allow):** GenAI posting volume; AI talent concentration; headline pay for AI and ML engineers and the software-engineer baseline; income tax and social contributions at one reference salary, including special regimes for incoming workers; living costs and rent; a one-line headline of access for foreign workers; remote-hiring openness; ecosystem depth (frontier labs, major AI employers, AI venture funding, compute investment); policy stability; language requirements.
- **Out of scope:** route-by-route visa detail and pay by role (other sessions); quality-of-life rankings unrelated to work.
- **Source priorities:** official statistics, tax authorities and government calculators; OECD (for example Taxing Wages and OECD.AI), the Stanford AI Index and LinkedIn's Economic Graph for talent indicators; Levels.fyi city pages and posted salary ranges (B); job platforms for counts (B, with query and date); cost-of-living indices with stated methods (B or C, attributed).

## KNOWN

The knowledge base's claims, to be tested:

{{claims}}

{{context}}

## CALIBRATION

Apply the five calibration rules in the protocol. Cross-country comparisons fail on definitions: state the population, currency, year, component (base or total) and level behind every pay figure, and convert currencies with a named rate and date (purchasing-power-parity conversions separately). Tax figures are illustrative calculations (grade M on A inputs), not advice. Posting counts on different platforms are not comparable: use one source per measure across countries where you can, and name it.

## APPROACH

Cover every item, or list it under Absences:

1. **Demand.** GenAI posting counts per country and city from one consistent source where possible (state query, filters and date, and never log in to see counts), plus AI talent indicators (for example LinkedIn's AI talent concentration, the Stanford AI Index country indicators), as `measure` records.
2. **Headline pay.** For each country and main city: mid-level and senior AI or ML engineer total compensation from one consistent source (Levels.fyi where it covers the city; otherwise the best official or posted-range source), with n, date and component, and the software-engineer baseline. The pay sessions go deeper; here comparability matters more than detail.
3. **Net pay.** Effective income tax and employee social contributions at one reference salary per country (the local senior AI-engineer median from item 2), from official calculators or published schedules; special regimes for incoming workers (for example the Dutch 30% ruling and its scheduled changes, Spain's special regime, Portugal's IFICI, Italy's and France's impatriate regimes, Denmark's researcher scheme, Sweden's expert relief, zero personal income tax in the UAE, Saudi Arabia and Qatar) with eligibility and dates.
4. **Living costs.** Rent for a one-bedroom flat in the main city and a cost-of-living index, attributed; disposable income after tax and rent at the reference salary (grade M).
5. **Access headline.** For each country, one line: the main route for a skilled foreign tech worker, its key threshold, typical processing time, any quota or lottery, and the path to permanent residence, with an official source; plus a one-line note for Indian nationals (for example backlogs, or bilateral schemes such as the UK–India Young Professionals Scheme or Australia's MATES).
6. **Remote reach.** The share of GenAI postings open to remote work in or from each country; whether employers there hire foreign residents remotely (through contractors or employers of record); time-zone overlap with India.
7. **Ecosystem.** Frontier labs and major AI employers with engineering or research teams in each country and city; AI venture funding in the most recent full year (source, method); public AI programmes and compute investment.
8. **Stability.** Immigration, tax and AI-policy changes announced or enacted in 2025–2026 that raise or lower risk for an incoming worker, dated.
9. **Language.** Whether the AI job market works in English, and what language settlement needs.
10. **Provisional top five per lens.** For five lenses (highest net pay; fastest legal access for an Indian national with a bachelor's degree and five years' experience; best remote reach from India; best long-term settlement path; best for early-career candidates), a provisional top five among this session's countries with a one-line reason each. Do not compute weighted scores: the knowledge base computes its own ranking from your measures.

Research moves: WIDEN to each country's official statistics in its own language; CORROBORATE pay figures across two sources; FALSIFY "best country" claims from relocation marketers.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every country in scope has dated `measure` records for demand, headline pay, net pay, living costs, remote reach and ecosystem, or absences that say what is missing.
3. The access headline exists for every country, with an official source.
4. City-level figures exist for the main AI hiring cities listed.
5. The provisional top five per lens is given with reasons.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use `subject` values like `country:DE` and `city:DE-Berlin` (ISO 3166 codes) and snake_case `measure` names (for example `genai_postings`, `pay_p50_ml_engineer_tc_mid`, `effective_tax_rate_at_reference`, `rent_1br_city_centre`, `remote_share`, `ai_vc_funding`). In Detailed Findings include: one table per pillar (country · city · value · unit · date · source · grade), the access headlines and the provisional top fives.
