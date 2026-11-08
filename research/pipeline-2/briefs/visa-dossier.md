<!-- RP2 brief template: one visa and work-permit dossier per region. Sessions, countries, claims and probes: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

For a GenAI professional who wants to work in {{param:region}}, which legal routes to work exist at the research date, what does each require, cost and take, how likely is an employer to use it for an AI role, and what leads to permanent residence? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way for the knowledge base; one-way for a reader who acts on it, so accuracy and dates matter more than breadth. What would change the advice: rule changes, court rulings, new thresholds or quotas, processing-time shifts.

## BRIEF

We are building route-by-route dossiers of work authorisation for skilled foreign tech workers, so that readers can see which routes they qualify for, what to prepare, how long it takes and what it costs, and so that a country ranking can score access on a common basis. Question type: lookup (official rules) and evaluative (practical likelihood). Audience: GenAI engineers, researchers and leaders, with a specific lens for Indian nationals (backlogs, bilateral schemes, document attestation, consular waits) and a generic lens for other non-EU nationals. Everything here is a pointer to official sources, not legal advice.

Countries in this dossier: {{param:countries}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Rules as in force at the research date; announced and pending changes with their dates and status. Flag any official page you could not open.
- **In scope, for each country:** employer-sponsored skilled work permits; talent and self-sponsored routes; points-based routes; job-seeker visas; graduate and post-study routes; intra-company transfers; founder and start-up routes (briefly); remote-work and digital-nomad visas (briefly, including whether holders may work for foreign employers); bilateral or special schemes for Indian nationals; dependants' rights; paths to permanent residence and citizenship; language requirements; degree recognition; employer obligations (sponsor licences, labour-market tests, levies); official processing times and fees; quotas, caps and lotteries; changes enacted or proposed since 2025-01-01.
- **Out of scope:** tax advice beyond one-line pointers; asylum and family-only routes; routes closed to skilled workers.
- **Source priorities:** government immigration sites, statute and official guidance, official processing-time and fee pages (A); official statistics and registers (A); court records (A); law-firm and reputable media summaries (B), labelled as summaries; relocation vendors (C, with COI).

## KNOWN

The knowledge base's claims, to be tested:

{{claims}}

{{context}}

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Immigration rules are often summarised wrongly by vendors and media: take every threshold, fee and time from the official page, quote it exactly with its effective date, and say when you could only read a summary. Processing times on official pages are service standards or historical medians; say which. Do not estimate approval odds for an individual.

## APPROACH

Cover every item, or list it under Absences:

1. **Route census.** For each country, every route in scope as a `visa_route` record: official name, kind, eligibility (education, experience, occupation lists and whether AI, ML or ICT roles are on shortage or priority lists), salary threshold with currency, period and effective date (and any reduced threshold), quota or lottery, official processing time, government fees and employer levies, validity and renewal, dependants and spouse work rights, path to permanent residence (years and conditions), language requirement, the official URL, and changes since 2025-01-01 with dates and status.
2. **Employer reality.** Evidence on how often employers use each route for AI and software roles (official registers or statistics where they exist), whether sponsorship is common for GenAI roles, the employer's cost and effort, and practical timelines from offer to start date.
3. **Indian nationals.** For each country: backlogs or caps that bind Indian nationals, bilateral schemes, consular appointment waits, document attestation and police clearance, recognition of Indian degrees, and anything else that differs for Indian applicants.
4. **Remote work while resident.** Whether a resident on each main route may work for a foreign employer or as a contractor, and the one-line tax-residence pointer.
5. **Status table.** Every pending or contested rule, and every rule changed since 2025-01-01, with the date it describes, its status and the official source, so the knowledge base can date each row (class V0).
6. **Comparison.** For each country, the two or three routes most likely to fit a GenAI professional, compared on eligibility, time, cost, employer dependence and settlement path, with a one-line recommendation for each of three readers: a mid-level engineer with an offer, a senior engineer or researcher without an offer, and a recent graduate.

Probes specific to this region:

{{param:probes}}

Research moves: DEEPEN every threshold to the official page in the country's official language; CORROBORATE processing times with official statistics; FALSIFY vendor claims of "easy" routes.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every country has `visa_route` records for every route in scope, each with an official URL and an effective date, or absences that say what could not be verified.
3. The status table lists every pending or contested item with dates.
4. Indian-national specifics are covered for every country.
5. The comparison and the three reader recommendations exist for every country.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use `ttl` V4 for rule text and thresholds in force, V1 for processing times and consular waits, and V0 for pending or contested items. In Detailed Findings include, per country: the route table (route · kind · eligibility · salary threshold and date · processing · fees · dependants · path to permanent residence · source · grade) and the status table (item · status · as of · official source · grade).
