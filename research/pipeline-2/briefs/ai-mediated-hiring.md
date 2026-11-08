<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

How does AI mediate hiring at the research date, from AI screening of applications to AI interviewers, employers' rules on candidates' own AI use, cheating tools, and identity-fraud checks, and what should an honest GenAI candidate do about each? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: vendor documentation of new screening features; court rulings or regulations on automated hiring; employer policy changes on AI use; data on fraud and detection.

## BRIEF

We are investigating the AI layer of hiring from the candidate's side. Employers use AI to rank applications, run asynchronous or live AI interviews and detect cheating and fake candidates; candidates use AI to write, practise and, sometimes, cheat; regulators and courts are setting rules. Question type: lookup and evaluative. Audience: GenAI job seekers worldwide, including India, who need to know what software will read and score them, what AI use is allowed, how to prepare for AI interviewers, and how to avoid being mistaken for a fraudulent applicant.

The knowledge base documents applicant-tracking mechanics from vendor documentation (knockout questions are the only documented automatic rejection; AI ranking layers score requirements against extracted facts) and lists two US lawsuits as allegations. It has little on AI interviewers, candidate-AI policies, cheating tools or identity fraud.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2024-01-01 to {{date}}; legal statuses dated to the day.
- **In scope:** AI screening and ranking features in applicant-tracking and recruiting products (for example Workday's HiredScore, Eightfold, Phenom, Greenhouse, Ashby, LinkedIn's hiring assistant), adoption data and bias audits; AI interviewers (asynchronous video and live voice or chat interviewers used for technical roles); employers' policies on candidates' use of AI; interview copilots and cheating tools, their detection and consequences; identity fraud in remote hiring (deepfakes, proxy interviews, fraudulent remote IT workers) and employers' countermeasures (identity verification, in-person rounds, background checks); candidates' legal rights (notices, audits, explanation, human review, opt-outs).
- **Laws, as pointers (this session owns the law on AI in hiring):** New York City Local Law 144; Illinois' AI Video Interview Act (2020) and the Human Rights Act amendment on AI in employment decisions (HB 3773, in force 1 January 2026); Colorado's AI Act and its effective date; California's rules on automated decision systems in employment; Ontario's requirement to disclose AI use in job postings; the EU AI Act's high-risk employment obligations and any change to their timetable; GDPR Article 22; India's DPDP Act as it applies to hiring; with status at the research date.
- **Out of scope:** interview loop formats (another session); résumé formatting (another session).
- **Source priorities:** vendor documentation (A for what a feature does; C with COI for claims about fairness or accuracy); regulator guidance, statutes and court records (A); published bias audits (A or B); government advisories on fraud (for example FBI and US Department of Justice notices) (A); reputable reporting (B); vendor surveys (C).

## KNOWN

The knowledge base's claims, to be tested:

- K: Greenhouse, Lever, Ashby, Workday and Taleo/Oracle document automatic rejection only as knockout rules the employer configures on application answers; none of the vendor documents retrieved describes rejection for résumé wording or a failed parse [A, retrieved 2026-10-23].
- K: AI ranking layers compare the recruiter's requirement list with extracted titles, skills, years, dates and employers plus learned similarity; Eightfold scores title similarity; HiredScore's LLM mode became an opt-in from 5 August 2026 [A].
- K: How many employers switch on AI ranking features, and how often recruiters open candidates below the top of a sorted list, is not published [gap].
- K: More than 90% of employers using recruiting-management systems relied on them for a first cut or ranking (a 2021 Harvard Business School and Accenture survey of 2,275 executives in the US, UK and Germany) [B].
- K: Two US lawsuits, *Kistler v. Eightfold* and *Mobley v. Workday*, allege de-facto exclusion by ranking; they are allegations, not findings [B, as of October 2026].
- K: Fraud and spam dilute cold-inbound conversion averages [B].
- K: Anthropic's live interview rounds default to no AI assistance [B/C].

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Vendors describe their own fairness and accuracy: grade those claims C with COI. Distinguish a lawsuit's allegations from rulings, and give each case's procedural status with its date. Fraud statistics from security vendors need their method stated.

## APPROACH

Cover every item, or list it under Absences:

1. **AI screening.** For each major product: what the documentation says it scores, whether it can auto-reject, how employers configure it, adoption evidence, published bias audits, and what a candidate can do (as `practice` records).
2. **Lawsuits and enforcement.** The status at the research date of *Mobley v. Workday*, *Kistler v. Eightfold* and any other significant case or enforcement action on automated hiring, with dates.
3. **Regulation.** For each law in scope: what it requires of employers, what rights it gives candidates, its effective date and status, as `rule` records.
4. **AI interviewers.** Products used for technical hiring, how they work (asynchronous video, live voice, chat), what they score, adoption for engineering roles, candidate rights and opt-outs, and practice-curated preparation, as `tool` and `practice` records.
5. **Candidate AI policies.** Employers' published or reported rules on AI use in applications, take-homes and interviews; how employers detect undisclosed use; consequences.
6. **Cheating tools.** Interview copilots and similar tools: what they do, their terms, detection by interview platforms, employer responses, and the reputational and legal risk to candidates, with a verdict.
7. **Identity fraud.** The scale of fraudulent remote applicants and proxy interviews (official advisories, prosecutions, employer reports), countermeasures employers use, and what honest candidates should expect and prepare (identity checks, camera on, in-person final rounds, background verification), including India's background-verification practice.
8. **Rights and remedies.** How a candidate can request notice, an explanation or human review under the laws in scope, with official sources.

Research moves: DEEPEN to vendor documentation and court dockets; FALSIFY claims that AI screening auto-rejects most applicants; CORROBORATE fraud scale across official and independent sources.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. Every major screening product and AI-interviewer product in scope has a documented description with a date.
3. Every law and case in scope has its status and date.
4. Candidate-AI policies are tabulated by employer, and cheating tools have verdicts.
5. Fraud countermeasures and what candidates should expect are stated as graded decision rules.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the screening-product table (product · what it scores · auto-reject? · audits · source · date); the AI-interviewer table; the law and case table (item · requirement or allegation · status · date · source); and the employer AI-policy table.
