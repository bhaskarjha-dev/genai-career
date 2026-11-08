<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

Which learning resources (official documentation, free courses, university lectures, books, paid cohorts, bootcamps and degree programmes) best build the skills each GenAI role family needs, how should they be rated when almost none has independent outcome data, and which are poor value? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: independent outcome data for a course or bootcamp; resources going stale or being superseded; price changes.

## BRIEF

The knowledge base deliberately links primary specifications and documentation rather than course rankings, because its Phase 0 research found no outcome data for GenAI courses or bootcamps other than vendor-reported figures. Readers still ask which courses and books to use. The aim is a transparent rating method that does not pretend to measure outcomes, applied to a curated census of resources per role family and skill area, with honest verdicts and a list of resources to avoid. Question type: evaluative. Audience: learners in every role family, with free options first, and India-specific programmes covered.

Role families (use these names):

{{families}}

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: resources updated since 2024-01-01 for fast-moving topics (LLM applications, agents, evaluation, serving); any date for foundations (deep learning, statistics, systems), with the edition or version.
- **In scope:** official documentation and specifications; free courses and lecture series (for example university courses on language modelling and systems, Hugging Face courses, DataTalks.Club courses, GPU MODE lectures); books (with edition and date); paid cohorts and bootcamps (international and Indian, for example upGrad, Great Learning, Simplilearn, Scaler, Interview Kickstart), with prices and outcome claims; degree and certificate programmes only as context (another session covers certificates); compute for learning (free notebook tiers, credits programmes, GPU rental prices).
- **Out of scope:** certifications (other sessions); interview-preparation platforms (the interview session covers them).
- **Source priorities:** the resource itself (syllabus, last update, exercises) (A for what it contains); authors' track records (A or B); independent outcome studies or regulator actions (A); learner reviews and surveys (C, attributed); vendor outcome claims (C with COI, or E if untraceable).

## KNOWN

The knowledge base's claims, to be tested:

- K: No GenAI course or bootcamp has outcome data other than vendor-reported figures [D, as of October 2026].
- K: Learn by building toward a gate, not by finishing a syllabus: for application roles, ship a hosted-model v0 in the first two weeks and learn theory when the build needs it; reverse the order only for the research-engineer track [D; the rule is untested].
- K: Put evaluation first in every role family; hand-write 30 evaluation cases in the first two weeks and build the harness before the second feature [P; M].
- K: Spend time before money: API credits and a free notebook tier cover months 1–6 of application-layer work; rent GPUs only for serving or fine-tuning labs [M].
- K: Fast-moving tools change shape within months (in 2026, AI SDK 6 and WebMCP changed; OpenAI acquired Promptfoo, ClickHouse acquired Langfuse and RAGAS went dormant), so spend most hours on durable concepts and pin tool versions [A/C].

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Popularity is not quality and enrolment is not completion: do not treat star counts, enrolment figures or affiliate "best course" lists as evidence. Course outcome claims ("X% got jobs") are E unless a method and an independent audit exist.

## APPROACH

Cover every item, or list it under Absences:

1. **Rating method.** A rubric for resources without outcome data, with criteria such as author authority, currency (last update against the topic's speed of change), hands-on depth (graded exercises, projects), alignment with the role family's Must and Important skills, cost in money and hours, and any independent outcome evidence. State weights and how each criterion is scored.
2. **Census.** For each role family, the strongest 5–10 resources across formats (documentation, free course, lecture series, book, paid cohort), as `resource` records with provider, URL, kind, cost, hours, level, last update, outcome evidence and a verdict.
3. **Outcome evidence.** Any independent study, audit, regulator action or consumer-court record on course and bootcamp outcomes, including Indian ed-tech refund and mis-selling cases.
4. **Paid programmes.** For the main paid cohorts and bootcamps: price, duration, syllabus currency, instructors, outcome claims and their status (traceable or not), refund terms, and verdict.
5. **Staleness.** Which popular resources are outdated at the research date and what supersedes them.
6. **Compute.** Free notebook tiers and their limits, student and researcher credit programmes, and GPU rental prices at the research date, as `tool` records at stage 3.
7. **Minimal sets.** For each role family, a minimal free set and a minimal paid set, with the reason for each item.

Research moves: DEEPEN each resource to its syllabus and update history; FALSIFY outcome claims; WIDEN to Indian and non-English resources.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. The rating method is stated with weights and scoring rules.
3. Every role family has rated `resource` records and minimal sets.
4. Paid programmes have verdicts with their outcome claims checked.
5. Stale resources and their replacements are listed.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: the rubric; one resource table per role family (resource · kind · cost · hours · last update · rubric score · verdict · grade); the paid-programme table; and the compute table.
