<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

How should a GenAI job seeker get referred, get introduced and reach hiring managers, founders and engineers directly, within the law and platform rules, and what does the evidence say about the yield of each route? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: a measured candidate-initiated reply or interview rate by channel and message type; employer data on referral quality; a legal ruling or regulator guidance on job-seeker outreach.

## BRIEF

We are investigating the routes in which a named person pulls a candidate into a hiring process: employee referrals, warm introductions, alumni networks, cold outreach by email, LinkedIn or X, artefact-led outreach (sending a short audit, benchmark or pull request), and third-party recruiters. Question type: evaluative and causal (what works, and how much of the measured advantage is selection rather than effect). Audience: job seekers worldwide, with depth for India, from early career to leadership.

The knowledge base's guidance rests on large applicant-tracking vendor datasets (Ashby, Gem) that show referred and sourced candidates converting far better than inbound applicants, which it treats as selection effects, and on judgement for message length, volume and stop rules. It states that no verified candidate-to-hiring-manager reply rate exists and that the law on cold email (GDPR, India's DPDP Act, CAN-SPAM) was not researched. The aim is to add the economics literature on referrals, any measured outreach data, the legal position, and practical, graded scripts.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: any date for peer-reviewed studies of referral hiring; 2024-01-01 to {{date}} for platform rules, datasets and law.
- **In scope:** how referral programmes work at employers of each type (frontier labs, Big Tech, AI startups, enterprises and GCCs, IT services); what a referral changes in the applicant-tracking system; the economics literature on referral hiring (quality, retention, wages, selection); how to ask for a referral from strong, weak and no ties; referral requests to strangers and paid referral services, and employer policies on them; warm and double-opt-in introductions; alumni networks; cold outreach structure, timing and follow-up; finding contact details (email-pattern and contact-data tools) and their accuracy and terms; the law on unsolicited messages and on processing contact data in the EU, UK, US, Canada, India, Singapore and Australia; working with agency and executive-search recruiters, and recruiter-fee scams.
- **Out of scope:** LinkedIn profile optimisation and X tactics (other sessions); community participation (another session).
- **Source priorities:** peer-reviewed economics and sociology; applicant-tracking vendor datasets with sample sizes; regulator guidance and statute (data-protection authorities, the FTC, the CRTC, India's Ministry of Electronics and IT); platform help pages; employer referral-policy pages; then practitioners (C or D).

## KNOWN

The knowledge base's claims, to be tested:

- K: In Ashby's data (38 million applications, 2021–2024), 3% of inbound applications reach an interview, against 25% of sourced and 40% of referred ones; Gem puts referrals at about 11× and sourced candidates at about 8× inbound per application. These are selection effects, not the effect of a tactic [B].
- K: Referrals are about 15–18% of hires and inbound about half; the "70–85% hidden job market" has no evidence base [A].
- K: Ask a contact for a referral before applying, because a cold application sent first may block the referral [P].
- K: Without a referral, apply through the normal channel, then send the hiring manager a note within 24–48 hours; the sequence is unmeasured [D].
- K: Every outreach message should carry one artefact the reader can verify (a merged pull request, a reproducible benchmark or a short audit with a one-command reproduction) [B/C].
- K: Send at most 30 outreach messages a week; a first touch of about 80–90 words or fewer, with one link and one ask; one follow-up on day 5–7; then stop. The length rule borrows from cold sales email, where the best first touches run under 80 words [D; B for the sales benchmark].
- K: Plan for 3–8% replies and decide at 60 sends. No verified candidate-to-hiring-manager reply rate exists; 25–50% reply claims are unverified. Zero replies after 60 sends puts the one-sided 95% upper bound on the true rate at 4.9% [D; M].
- K: Cold B2B email averages a 3.43% reply rate, with the top quartile at 5.5% or more (Instantly); Pin's 17.08% LinkedIn reply rate is for recruiter-to-candidate messages [B].
- K: Referred candidates passed screens at 52% against 35% in one secondary summary [B/C].

Context (what the knowledge base already holds or lacks; no verdict needed):

- Privacy and anti-spam law for cold email (GDPR, India's DPDP Act, CAN-SPAM) has not been researched for it.

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Separate three things the literature often merges: the selection effect (who gets referred), the information effect (what the referrer knows) and any causal effect of a tactic. Sales-email and recruiter-message benchmarks are proxies for candidate outreach, not measurements of it: label them so.

## APPROACH

Cover every item, or list it under Absences:

1. **The economics of referrals.** Peer-reviewed findings on referred hires' interview and offer rates, wages, performance and retention, and on how much of the advantage is selection. Name the studies, samples and settings.
2. **Referral mechanics by employer type.** What a referral does inside Greenhouse, Lever, Ashby and Workday (source tagging, recruiter review, priority); referral bonuses; strong (vouched) against submit-only referrals; differences at frontier labs, Big Tech, startups, GCCs and IT services in India.
3. **Asking for a referral.** From strong ties, weak ties and strangers: what to send, when, and how often requests succeed (any data); employer policies on referring people the employee does not know; paid referral services and their legality and ethics.
4. **Warm introductions and alumni networks.** Double-opt-in introductions; university and former-employer alumni groups; evidence on yield.
5. **Cold outreach.** Structure, length, subject lines, personalisation, artefact attachment, timing and follow-up; measured candidate-initiated reply or interview rates (any dataset, with method); proxies, labelled as proxies; differences by recipient (hiring manager, founder, engineer, recruiter) and by channel (email, LinkedIn message or InMail, X direct message).
6. **Contact details.** How job seekers find work emails (pattern guessing, verification, contact-data tools); the accuracy of contact-data vendors; their terms of service; data-protection complaints or enforcement against them; the "HR contact" spreadsheets sold to job seekers in India and their exposure under the DPDP Act; paid mentorship and referral marketplaces (for example Topmate).
7. **The law.** For each of the EU (GDPR and the ePrivacy rules), the UK (UK GDPR and PECR), the US (CAN-SPAM), Canada (CASL), India (the DPDP Act 2023 and its rules), Singapore (PDPA) and Australia (Spam Act): whether a job seeker's unsolicited message to a person at a company is regulated, what makes it lawful, and what the regulator has said, as `rule` records. Official sources only; pointers, not advice.
8. **Recruiters and agencies.** How agency (contingency) and retained search recruiters work for GenAI roles and leadership roles; how to work with them; evidence on their conversion; red flags, including recruiters who charge candidates a fee.
9. **India.** Referral culture at Indian employers and GCCs; referral drives; referral requests on LinkedIn and in WhatsApp or Telegram groups; scams.
10. **Yield per hour by channel.** Using any measured data (vendor datasets, studies, the knowledge base's claims above), compare what an hour spent on cold applications, referral requests, artefact-led outreach, community participation and public writing returns in screens or interviews; say plainly where the comparison is unmeasured and what would measure it. This tests the premise that networking is the highest-yield activity.
11. **Scripts.** Practice-curated templates for a referral request, a warm-introduction request, a cold note to a hiring manager with an artefact, and a follow-up, each tagged with the evidence behind each element or [P]. Templates are formats, not ghost-written messages for a specific person.
12. **Tools.** Contact-finding, email-verification, outreach-automation and outreach-tracking tools as `tool` records at stage 7, with legal and terms-of-service risk.

Research moves: DEEPEN every referral statistic to its dataset; FALSIFY the claim that referrals are mostly hidden jobs; WIDEN to labour-economics journals and regulator guidance.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. The referral literature is summarised with samples and settings, and selection is separated from effect.
3. The legal position for each jurisdiction in scope is stated with an official source and a date, or as an absence.
4. Every outreach tactic is a graded `practice` record, any measured candidate-initiated rate is reported with its method (or its absence is confirmed), and the yield-per-hour comparison states what is measured and what is not.
5. The scripts are given as templates with evidence tags.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: a table of referral studies (study · sample · setting · finding · grade); a table of routes (route · measured yield · source · grade); the jurisdiction table (jurisdiction · rule · applies to job-seeker outreach? · official source · date · grade); and the templates.
