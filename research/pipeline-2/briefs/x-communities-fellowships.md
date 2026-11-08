<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which public communities, platforms, fellowships, events and competitions give a GenAI job seeker the best chance of being noticed by people who hire, including people at frontier labs, and how should they take part? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: a community, fellowship or event publishing hiring outcomes; first-person accounts from hiring managers who source from a venue; evidence that a tactic on X or in a community leads to interviews.

## BRIEF

We are investigating the visibility layer beyond LinkedIn: X (Twitter) and its alternatives (Bluesky, Threads, Mastodon) as used by AI researchers and engineers; Discord, Slack and forum communities; fellowships, residencies and scholar programmes that feed hiring at labs and AI companies; conferences, meetups and hackathons; and competitions and leaderboards. Question type: evaluative, with a directory refresh. Audience: job seekers worldwide, including people in India without US, UK or Canadian work authorisation, people without a brand-name employer, and PhD researchers moving to industry.

The knowledge base holds a tiered communities directory audited on 21 October 2026 and a weekly participation routine; it states that no community in scope publishes a conversion rate, that the documented hiring mechanism is company-initiated, and that X's role rests on one news report. The aim is to measure what can be measured, refresh the directory, add the fellowship and competition routes, and grade engagement tactics honestly.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2024-01-01 to {{date}}. Community activity and programme status change quickly: date every status and flag anything older than 2026-01-01.
- **In scope:** X, Bluesky and Threads use by the AI research and engineering community, including documented hires and moves that started there; Discord and Slack servers and forums for AI engineering, inference, kernels, evaluation, safety and open models; fellowships and residencies (for example the Anthropic Fellows programme, MATS, Cohere Labs scholars, programmes at Google DeepMind, OpenAI and Meta, safety programmes such as SPAR, ARENA, ERA, LASR and Astra, open-source mentorships such as Google Summer of Code and LFX), with eligibility, geography, stipends and published outcomes; conferences (research conferences and their workshops, the AI Engineer World's Fair and Summit, PyTorch Conference, Ray Summit, KubeCon AI tracks), regional events including India's, and hackathons that report hiring; competitions (Kaggle, ARC Prize, AIMO, GPU MODE, NeurIPS competition tracks); paid cohorts and referral groups on Telegram or WhatsApp.
- **Out of scope:** LinkedIn tactics (another session); general social-media growth advice.
- **Source priorities:** programme pages and their published outcome reports; first-person accounts by hiring managers and researchers in their own name; reporting that names sources; community rules and public statistics (member counts, message volumes); then practitioner commentary (C or D).

## KNOWN

The knowledge base's claims, to be tested:

- K: Communities raise visibility and conversion; they are not a door to hidden jobs. In Ashby's data on nearly 250,000 hires (January 2021 to June 2025), referrals are about 18% of hires; "hidden job market" figures of 70–90% could not be traced to a measurement [A].
- K: Budget four or five communities and about six hours a week, all of it public output; X and LinkedIn only distribute what you make. The hours and weighting are judgement [C].
- K: The documented hiring mechanism is company-initiated: teams that run a community (Cursor, Zed, Appwrite) watch who contributes consistently and reach out; no conversion rate exists for any community in scope [A].
- K: Community etiquette converges: self-promotion and job requests only in designated channels; mass-messaged CVs count as spam; open a discussion before a pull request, keep pull requests small and disclose AI help [A/B].
- K: Re-rank communities after 4–6 weeks of participation and drop one after 4–6 weeks with no two-way exchange [C/D].
- K: From India, the best-evidenced offline venues are screened or approval-gated and the largest events are vendor- or enterprise-heavy; the deep routes open to anyone are remote and public-output: GPU MODE competitions, EleutherAI, the vLLM developer Slack and Cohere Labs [A/B; B/C].
- K: The only quantified community-to-hire route found, the Anthropic Fellows programme, is gated to people with US, UK or Canadian work authorisation [A/B, as of October 2026].
- K: Axios (10 September 2026) describes AI-industry hiring moves ricocheting on X [B].
- K: No AI-lab hiring manager was found describing, in the first person, sourcing candidates from Discord [as of October 2026].

Context (what the knowledge base already holds or lacks; no verdict needed):

- Paid cohorts, career masterminds and Telegram or WhatsApp referral groups have not been researched for it.

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Hiring stories from community owners are selected success stories: record selection and survivorship where they apply. A follower count or member count is not evidence of hiring influence.

## APPROACH

Cover every item, or list it under Absences:

1. **X and its alternatives.** How AI researchers and engineers use X in 2025–2026; documented cases of hires, offers or collaborations that began with posts on X (named first-person accounts or reporting); what frontier researchers say about engaging with strangers (replies, reproductions, follow-up work); measured or reported migration of ML researchers to Bluesky or Threads; risks (reputation, low-effort replies, impersonation).
2. **Engagement tactics.** Tactics such as publishing reproductions of a researcher's paper, writing follow-ups to their posts, replying with substance, and sending direct messages: what is claimed, what evidence exists, and a verdict for each, as `practice` records.
3. **Community directory refresh.** For each community in the knowledge base's directory and any significant new one: kind, URL, access (open, application, invite), activity with a date and a source (members, messages a month, events), any evidence of hiring, regions, and a verdict, as `community` records.
4. **Fellowships and residencies.** For each programme: host, focus (research, safety, engineering, open source), eligibility including nationality and work-authorisation limits, remote or in person, stipend, duration, application window, published outcomes (for example the share of alumni hired by labs), status at the research date (open, paused, discontinued), and fit by background.
5. **Events.** Which conferences, workshops, meetups and hackathons show evidence of hiring (career fairs, sponsor recruiting, documented hires); costs; visa considerations for attendees from India; call-for-proposals acceptance rates and what gets accepted, where published.
6. **Competitions and leaderboards.** Which competitions have led to hires or interviews (named cases, sponsor statements); team and time costs; how to present results on a résumé.
7. **India.** Communities and events in Bengaluru, Hyderabad, Pune, Delhi NCR, Chennai and Mumbai, and online communities run from India, with access rules and activity evidence.
8. **Open source as a route.** Which AI open-source projects (for example inference engines, training and evaluation libraries, agent frameworks) document hiring their contributors, how maintainers say they spot candidates, and what contribution pattern precedes those hires; refresh the knowledge base's open-source thresholds against that evidence.
9. **Paid groups and cohorts.** Paid communities, cohort courses that promise networking, and Telegram or WhatsApp referral groups: what they offer, prices, evidence of outcomes, and scam reports.

Research moves: WIDEN across platforms and languages; FALSIFY the idea that a large audience is needed to be hired; CORROBORATE any hiring claim with a second, independent source.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. The community directory is refreshed with dated activity evidence and verdicts, including India venues.
3. Every fellowship and residency in scope has its eligibility, geography, status and published outcomes (in the `community` record's `eligibility`, `work_authorisation`, `stipend` and `status` fields), or an absence record.
4. Engagement tactics on X and in communities are graded, with folklore separated from documented practice.
5. A weekly visibility routine for each of three readers (an engineer in India, an engineer in the US or Europe, a PhD researcher) is stated as decision rules, each graded.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the community table; the fellowship table (programme · host · eligibility · geography · stipend · outcomes · status · grade); the events table; and the tactics table.
