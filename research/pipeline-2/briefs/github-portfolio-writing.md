<!-- RP2 brief. Sessions and metadata: research/pipeline-2/catalogue.json. Assemble the prompt: python3 -B scripts/research_pipeline.py --prompt <session id> -->

# RESEARCH BRIEF: {{id}}: {{title}}

## DECISION

What should a GenAI job seeker publish on GitHub, a personal portfolio site and a technical blog so that a recruiter or hiring manager who looks can verify their skills in minutes, and what evidence shows that these surfaces change hiring outcomes? This informs decisions {{decisions}} and these outputs of the knowledge base: {{feeds}}. Door: two-way. What would change the advice: evidence on how often and how reviewers open these surfaces, what they check, and which formats lead to interviews.

## BRIEF

We are investigating the public proof surfaces of a GenAI engineer or researcher: the GitHub profile and its README, pinned repositories, project READMEs, Hugging Face profiles and Spaces, Kaggle, personal portfolio websites and technical writing (personal blogs, Substack, Medium, dev.to, conference talks). Question type: evaluative. Audience: job seekers from new graduate to staff level, worldwide, including people without a brand-name employer or degree, for whom public proof matters most.

The knowledge base already holds a verifiability ladder for proof of work (V0 self-asserted, V1 reproducible, V2 externally attested, V3 operationally evidenced) and level-calibrated standards; it states that the weight of a live demo against a repository, how often reviewers open GitHub, and blog-to-offer rates are unmeasured. The aim is to find whatever evidence exists (hiring-manager statements with sources, studies of GitHub signals in hiring, employer postings that ask for public work), to collect strong exemplars, and to separate measured findings from practice.

## SCOPE

- **Temporal anchor:** today is {{date}}. Evidence window: 2023-01-01 to {{date}} for practice; any date for peer-reviewed studies of developer hiring signals. Flag platform features older than 2025-07-01 as possibly stale.
- **In scope:** GitHub profile README, pinned repositories, the contribution graph, stars and followers as signals, project README structure for AI systems (evaluation results, cost and latency, reproduction command, architecture, limits), GitHub Actions badges and CI-gated evaluations, model and dataset cards on Hugging Face, Spaces and demos, Kaggle ranks, portfolio site structure and hosting, writing cadence and formats, talks and podcasts, authorship verification in the age of AI-generated code and text, and the GenAI-specific artefacts reviewers ask for (evaluation harnesses, traces, benchmarks, postmortems).
- **Out of scope:** LinkedIn (another session covers it); open-source contribution strategy beyond what profiles display (covered in the knowledge base); generic web-design advice.
- **Source priorities:** peer-reviewed studies of signals in developer hiring; hiring managers and engineers at named employers writing in their own name; employer postings that name public work; GitHub and Hugging Face documentation; large surveys with a method (for example Stack Overflow and GitHub surveys); then practitioners (C or D).

## KNOWN

The knowledge base's claims, to be tested:

- K: Every headline claim in a portfolio should be V1 or better: one command regenerates it from committed data. Authorship verification is the live problem of 2026, because READMEs and dashboards are cheap to generate [B/C · D for the rule].
- K: Calibrate to the target level: new graduate to junior, one measured system with every claim at V1; mid-level, evaluation-gated releases and a 30-day operating log; senior, at least one externally attested (V2) item such as a merged upstream pull request; staff or principal, V2 as the norm plus adoption by others [D].
- K: No project type is universally flagged as weak. What reads as tutorial-grade is no measurement, no baseline, no deployment hygiene, a one-shot commit history and unexplained choices. RAG appears in roughly a third to 40% of AI-engineer postings, so retrofit a RAG repository with evaluation rather than delete it [C; B for the share].
- K: Evaluation is the most consistently cited separator in hiring write-ups. Strong evaluation evidence means 20–50 tasks drawn from real failures, code graders first, model graders calibrated against human labels, several trials; about 100 traces read and coded; each judge checked on about 50 pass and 50 fail human labels [B; A for the task guidance].
- K: Keep two or three deep repositories rather than many small demos [C].
- K: A live demo is optional and should be replay-first, capped and dated: unbounded spend, leaked keys, free-tier changes and dead links are documented risks; its weight against a repository is unmeasured [A for the risks; D for the weight].
- K: Archive unmodified tutorial forks, Titanic, MNIST and Iris notebooks and single-commit repositories; upgrade a mediocre repository into a measured system instead of deleting it [C].
- K: Writing as an inbound channel rests on two prolific authors' anecdotes; no blog-to-offer data exists. One employer posting (Inferact, posted 18 June 2026) lists widely shared technical blogs or side projects on vLLM or LLM inference as a bonus [C; B for the posting].
- K: Many reviewers never open GitHub, and keyword screens reward terms such as "RAG", so keep the keywords on the résumé and add evidence behind them [C; D for the rule].
- K: In eight open-source repositories examined, 49–82% of contributor identities stopped after one merged commit; drive-by pull requests have become a liability because of AI-generated low-quality submissions [A; B].

{{tools}}

## CALIBRATION

Apply the five calibration rules in the protocol. Survivorship is the main bias here: people who were hired describe what they published. Record it where it applies, and prefer statements from people who review candidates over statements from people who were hired.

## APPROACH

Cover every item, or list it under Absences:

1. **Do reviewers look?** Any measurement or credible first-person account of how often recruiters and hiring managers open GitHub, portfolio sites and blogs, at what stage, and for how long; differences by employer type (labs, Big Tech, startups, services firms, India GCCs).
2. **Studies of GitHub signals.** Peer-reviewed or large-sample work on what profile signals (contribution graph, stars, followers, languages, pull-request history) evaluators infer, and whether those signals predict anything; risks such as gaming the contribution graph.
3. **The GitHub profile.** What a strong profile README and pinned set look like for each role family below; exemplars from named engineers who have written about their own profiles; what to hide or archive.
4. **The project README for an AI system.** The structure reviewers want (problem, architecture, evaluation table with baseline, cost and latency budget, reproduction command, limits, decision log); exemplars from well-regarded open-source AI projects and individual portfolios; CI-gated evaluation and badges.
5. **Hugging Face and Kaggle.** When a model card, dataset card, Space or Kaggle rank is a stronger signal than a GitHub repository, and for which roles.
6. **Portfolio websites.** Whether a personal site adds signal beyond GitHub and LinkedIn; structures used by GenAI engineers and researchers with strong public profiles; hosting choices and their maintenance cost; what to put first.
7. **Technical writing and talks.** Evidence that writing or speaking leads to interviews or offers (named cases, employer statements, any dataset); formats that reviewers value (postmortems, benchmarks, paper reproductions, evaluation write-ups); cadence; platform choice.
8. **Authorship and AI-generated work.** How reviewers check that public work is the candidate's own in 2025–2026 (live walkthroughs, commit history, take-home extensions); evidence on how AI-written READMEs and blogs are received.
9. **Employer postings.** Count, in a sample of GenAI postings, how many ask for public work (GitHub, papers, blog, portfolio) and in what words; give the sample size and method.
10. **Role differences.** What public proof means for each role family listed below (for example papers and reproductions for research roles, deployed systems for application roles, kernels and benchmarks for infrastructure roles, governance artefacts for governance roles).
11. **Tools.** Portfolio and README tooling (site generators, demo hosts, cost guards, evaluation dashboards) as `tool` records at stage 5.

Research moves: WIDEN to hiring managers' posts and talks at named companies; FALSIFY the claim that a portfolio matters for every role; CORROBORATE every "hiring managers want X" statement with at least one employer-side source.

## DONE

This session is complete when:

1. Every K-number has a verdict with evidence.
2. The evidence on whether and how reviewers look at these surfaces is summarised with grades, including absences.
3. A README skeleton for an AI system and a profile skeleton for each role family are given as practice-curated templates, each element tagged with the evidence behind it or [P].
4. At least ten exemplars (repositories, profiles, sites or posts that are public and current) are listed with what makes each strong.
5. The employer-postings sample is reported with its size and method.

## FORMAT

Follow the protocol below. The report will be saved as `{{filename}}`. Data appendix record types: {{records}}. In Detailed Findings include: a table of signals (signal · what reviewers infer · evidence · grade); the README and profile skeletons; the exemplar table (exemplar · URL · role family · why it is strong); and the postings-sample table.

Role families the knowledge base covers:

{{families}}
