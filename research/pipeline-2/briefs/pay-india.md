<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What do GenAI roles pay in India at the research date, by city, level, employer type and role, how are Indian offers structured, and how should an India-based candidate negotiate? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: new pay datasets for India's AI roles, changes in offer structures, or evidence on negotiation outcomes in India.

## BRIEF

We are deepening the knowledge base's India pay evidence. It holds two populations about 3–4× apart (a broad market centred on ₹10–15 lakh and an MNC, GCC and product-firm population with a Levels.fyi Bengaluru ML Engineer median of ₹44.5 lakh), a measurable local senior ceiling, and several roles whose India pay inputs are placeholders. Its negotiation playbook says India evidence is thin. The aim is dated, graded pay records by city, level, employer type and role; an explanation of Indian offer structures (fixed, variable, joining and retention bonuses, ESOPs, provident fund and gratuity, in-hand pay against CTC); and documented negotiation norms (notice periods and buy-outs, counter-offers, hike expectations on switching). Question type: lookup and evaluative. Audience: India-based GenAI job seekers at every level, and the India lens of the knowledge base's role ranking.

Roles to cover (put the role ID in the `role` field; the knowledge base has placeholder India inputs for inference, AI infrastructure, applied AI, GPU kernel, AI enablement, AI product engineering, physical AI and AI safety roles, so cover those too):

{{roles}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2025-07-01 to {{date}} for pay; appraisal and hike surveys from the most recent cycle.
- **Cities:** Bengaluru, Hyderabad, Pune, Delhi NCR (Gurugram, Noida), Chennai and Mumbai; note others where AI hiring is significant.
- **Employer types:** global capability centres (GCCs) of foreign firms; Big Tech India; Indian product companies and unicorns; AI-native startups including Indian model builders; IT-services and consulting firms; foreign employers hiring remotely (briefly; another session covers remote work).
- **In scope:** pay by role, level, city and employer type; CTC components and in-hand pay; variable pay realisation; joining, relocation and retention bonuses; ESOP terms and liquidity events; annual increment and promotion-hike surveys; switch hikes; notice periods and buy-outs; counter-offers; offer reneging and its consequences; salary-history and expected-CTC questions; negotiation norms by employer type.
- **Out of scope:** tax computation (the knowledge base's India remote-tax page owns it); relocation abroad.
- **Source priorities:** posted ranges where Indian postings disclose them (A for the posting, with n); Levels.fyi India (B); salary platforms such as AmbitionBox and Glassdoor India (B or C, with their biases); increment surveys from established consultancies (B or C, attributed); recruitment-firm salary guides (C); employer statements and offer-structure documentation; then practitioners (D).

## KNOWN

The knowledge base's claims, to be tested:

- K: Levels.fyi's Greater Bengaluru ML Engineer P50 is ₹44.5 lakh (n = 96, 12 Oct 2026), while broad-market sources such as Glassdoor and Indeed centre on ₹10–15 lakh; employer type explains the gap [B; C].
- K: The local senior ceiling is a Bengaluru senior software-engineer median of about ₹56.0 lakh and a P90 of about ₹1.07 crore; a local staff role typically does not reach ₹1.2 crore [B; C for the staff estimate].
- K: Levels.fyi's Bengaluru AI Engineer figures are P50 ₹21.4–24.5 lakh, P75 ₹40.4 lakh and P90 ₹62.6 lakh, and are unstable [B].
- K: Senior software-engineer medians at named Bengaluru employers run from ₹24.9 lakh to ₹121.9 lakh [B/C].
- K: India has about twice the US entry-level share of AI roles (21.2% against 10.4%) [B].
- K: In a vendor's voluntary survey of 200+ India AI and ML engineers (July–September 2026), no growth (39%) outranked a better offer (21%) as the reason for leaving a role early [C].

Context (what the knowledge base already holds or lacks; no verdict needed):

- Its India negotiation evidence is thin, and its India pay inputs for eight roles are placeholders.

## CALIBRATION

Apply the five calibration rules in the protocol. Indian pay data is split by employer population: always state which population a figure describes. CTC figures often include variable pay, retention bonuses and employer contributions that are not cash in hand: say what each figure includes. Salary platforms and recruitment guides rarely state samples; grade them accordingly.

## APPROACH

Cover every item, or list it under Absences:

1. **Pay by role, level and city.** For each role above, pay records by level (entry, mid, senior, staff or principal) for the cities in scope, from at least two sources where possible, each with population, statistic, component, n and date.
2. **Pay by employer type.** How pay differs between GCCs, Big Tech India, product companies, AI-native startups, Indian model builders and IT-services firms for the same role and level.
3. **Offer structure.** CTC components, typical fixed-to-variable split, variable realisation, joining and retention bonuses, ESOP grants and vesting, buy-backs and liquidity events at Indian startups in 2025–2026, provident fund and gratuity, and how to compute in-hand pay (pointers only).
4. **Increments and switch hikes.** Annual increment and promotion surveys from the most recent cycle before the research date for technology and AI roles, and evidence on hikes when switching employers.
5. **Negotiation norms.** Notice periods and buy-outs; counter-offers and how employers treat them; holding several offers and offer reneging (frequency, employer responses); expected-CTC and current-CTC questions (and the law: salary-history questions are legal in India); documented tactics and their evidence.
6. **Senior and leadership pay.** Pay for staff, principal, director and head-of-AI roles in India, and how they compare with remote roles for foreign employers.
7. **Data quality.** For each source used, its population, method and biases, and which questions it can and cannot answer.

Research moves: CORROBORATE each figure across two sources; FALSIFY viral "AI engineer earns ₹X crore" claims; WIDEN to Indian-language business media and consultancy surveys.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every role above has India pay records for at least Bengaluru, by level, or absences that say why not; the eight placeholder roles are covered or explicitly reported as unmeasured.
3. Offer structure is explained with sources.
4. Negotiation norms in India are documented with grades.
5. A source-quality table exists.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. Use currency `INR`, `period` `year`, and say in `note` whether a figure is CTC, fixed or in-hand. In Detailed Findings include: a table by role, level and city; the employer-type comparison; the offer-structure table; and the negotiation table (norm · evidence · grade).
