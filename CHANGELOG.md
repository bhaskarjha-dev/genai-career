# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html); see decision D-014 in [research/DECISIONS.md](research/DECISIONS.md).

## [Unreleased]

Research pipeline 2 (RP2): the plan for targeted research on every high-impact element, designed backwards from the data and pages it will change. No research has been run yet; the owner runs the sessions. An independent review on 2026-11-08, before any session ran, split oversized sessions and tightened the record contract.

### Added
- **Decision D-021** (research pipeline 2: outcome-first targeted sessions), appended as accepted, not yet human-reviewed.
- **Decision D-022** (generic scope: personal records live in a personal career repository, for example pramedha-template), appended as accepted, not yet human-reviewed.
- **`research/pipeline-2/`:**
  - `README.md`: why a second pipeline (with the evidence gaps measured on the data), design principles, what deep research can and cannot do, the outcome map from each element to its owner pages, a generated tracker, waves and a ten-session minimum, how to run a session, quality gates, the reduce steps with the proposed methods for the credential value order and the country ranking, five measurement instruments, the refresh cadence and the limits.
  - `PROTOCOL.md`: the output and evidence protocol appended to every prompt (EGP-1.0 grades and freshness classes for an agent that cannot open the repository, conflict-of-interest rules, ethics, the report format, and a JSON Lines data appendix with 17 record types that use the repository's role and skill IDs).
  - `catalogue.json`: 53 sessions (T0-19 to T0-71) and nine reduce steps. Wave 1 (18): LinkedIn; GitHub, READMEs, portfolio sites and writing; X, communities, fellowships and open source as a route; referrals and cold outreach with the law and a yield-per-hour comparison; the résumé; global boards (owning ghost jobs, pay transparency and scams) and national boards with India in depth; job-search tools, agents and MCP servers; target employers and sponsor registers; a seven-part certification census; a two-part country and city scan. Wave 2 (23): six visa dossiers, remote cross-border work, pay (global and India), interview loops, AI-mediated hiring and dossiers for the twelve highest GenAI target roles. Wave 3 (12): dossiers for the other 17 roles, transitions for DevOps/SRE, product managers, IT-services engineers and students, learning resources, skill momentum and emerging titles, the market pulse and onboarding. Each of the 42 tool categories has one owning session. The certification seeds include the owner's list of credentials missing from the repository, marked unverified.
  - `briefs/`: 23 brief templates in Vivechak's eight-block form; the role, visa, country and certification briefs serve several sessions each.
  - `VERIFY.md` (an independent verification prompt with acceptance thresholds and batches) and `INTEGRATE.md` (registration, a record-to-owner mapping, dates, conflicts, reduce steps).
- **`scripts/research_pipeline.py`** (registered in `GENERATORS`): validates the catalogue, the briefs and tool-category ownership, keeps the tracker current, assembles each session's prompt with the repository's claims rendered from `data/` (`--prompt`), lists what to run (`--next`), checks a session report and its data appendix before it is saved (`--appendix`) and builds a batched verification packet (`--verify`). Six new tests (21 in total).

### Changed
- The writing-rule helpers (`RELATIVE_TIME`, `prose()`) moved from the validator to `scripts/common.py`, so the validator and the report checker share them.
- The validator lints `research/pipeline-2/` (links, tables, relative-time words) and checks its README's front matter; the manifest and `llms.txt` index it.
- ROADMAP: phase 5 is designed; P0-2 (run wave 1), P1-6 (integrate by reduce step), P1-7 (the job-description collector) and scripts for official registers, net pay and logged-in counts added; P1-1 to P1-3 and the target-company and learning-resource items mapped to sessions; open decisions on the wave order and on the data shapes for the RP2 rankings; D-021 added to the decisions awaiting confirmation; the session-ID namespace limit recorded.
- research/README, AGENTS, CONTRIBUTING, README and scripts/README point to the pipeline; new standalone sessions take IDs after the catalogue's reserved range (T0-72 onward).
- **Generic scope (D-022):** pages that duplicated personal records keep their GenAI-specific content and point to the reader's own career repository:
  - the application operating system's tracker becomes a list of the fields the metrics need (four tabs and CSV headers removed);
  - the targeting workbook's fill-in tables become "record" instructions, with a column naming the pramedha-template file for each step and a mapping of its scores to pramedha-template's P1–P8 role table;
  - the offer comparison worksheet keeps its rows and how to fill them, without per-offer columns;
  - the behavioural story-bank matrix keeps the core-story set, without fill-in columns;
  - the résumé strategy's master-inventory schema becomes the skill-ID tagging rule, with one example bullet;
  - the job-search strategy, the interview loops, the gap-analysis docs (stage 00 index, `scripts/README.md`, the script's docstring) and AGENTS.md (placement rule) follow suit.

### Removed
- ROADMAP P0-1 (the résumé generator), withdrawn by D-022; open decisions 1 (build P0-1) and 4 (generic or personal) closed by D-022. The stage 00 and 06 indexes, the README and the research pipeline 2 résumé step (R5, the résumé brief and the catalogue) no longer refer to it.

## [0.3.0] - 2026-11-08

Consolidation after a whole-repository audit (2026-11-07): every shared fact has one owner, every guide follows the guide pattern, generated pages carry review dates, and the machinery enforces more of what it promises. One page is removed and data formats change, so the next release is a minor version under D-014.

### Added
- **Decisions:** D-019 (one owner per fact) and D-020 (generated review dates and a weekly reminder), appended as accepted, not yet human-reviewed; D-017's calibration record, filled when its trigger fired (35 pages with review dates, against 20).
- **Data:**
  - `data/posting_skill_shares.json` and its schema: the JobsPipe posting-term shares retrieved 2026-11-02, moved unchanged from the role skill maps. `scripts/build_skills.py` checks every JD share in the ontology against it (154 of 154 match) and renders it in the role skill inventories under "Posting evidence".
  - `data/role_titles.json` and its schema: the A–Z title list, moved out of `scripts/build_index.py`; canonical titles are checked against the role ids.
  - A schema for `data/role_scores.json`; in that file, the GenAI-restricted demand ranges and the track playbooks (both moved out of scripts) and the date each posting-count source was last verified.
  - Per-variant résumé headlines in the skills ontology (from the résumé strategy's variant catalogue).
- **Machinery:**
  - `scripts/build_all.py`: every generator in dependency order, then the validator; its `GENERATORS` list is the single registry, and the validator fails if a script with `--check` is missing from it.
  - `scripts/common.py`: the JSON Schema subset, citation checks for session line references, and shared text helpers.
  - `scripts/tests/`: 15 tests (schema subset, citations, the validator's document rules, every data file against its schema, a smoke test of the gap-analysis tool), run in CI before the validator.
  - `.github/workflows/due-report.yml`: a weekly run with `--strict` that fails while any page is due (D-020); `validate.yml` gained `permissions: contents: read`.
- **For agents:** a session-ID-to-file map and the project documents in `llms.txt`; the owners table in AGENTS.md §2; rules to prefer Layer 0 sessions over syntheses and to curate, not teach.

### Changed
- **Every guide follows the guide pattern** (`LEGACY_GUIDES` is empty): GenAI target roles, the job-search strategy and the résumé strategy were migrated. The résumé strategy is the single résumé guide (layers, variant catalogue, tailoring, master inventory and the computed résumé decisions, whose blocks `scripts/resume_layers.py` now writes there); the job-search strategy keeps hiring levers, binding constraints and sequencing, and links the stage guides added in v0.2.0.
- **One owner per fact (D-019):**
  - the role skill maps are narrative only (944 → 473 lines): the D-004 tier lists, which contradicted the ontology, and the D-004 pay claim that ERRATA U20 rejects are gone; duplicated sections point to their owners;
  - the role catalog's §6.1 and §8.1–§8.3 point to career transitions, pay benchmarks, the role map and the market overview; the market overview links pay benchmarks instead of copying pay;
  - pay figures, funnel rates, transition timelines, credential and tool statuses, interview tables, visa and India facts are each kept by one owner, with one line and a link elsewhere.
- **Role pages:**
  - role rankings retitled "Role Rankings: The Composite Career Index (All Demand)", with a note on why it and the GenAI target order have different first roles; the role-views reading order is the same on README, Start Here and the roles folder (target roles, hubs, map, then the evidence);
  - role hubs print each role's own résumé headline (13 hubs printed the family's, 5 of them the literal "(per flavour)"); 8 hubs no longer show an India rank built only on placeholder inputs, and 7 flag a single placeholder input; leadership hubs open with their track playbook; leadership ranks read "Leadership #N", so they no longer look like layer codes;
  - interview-track sources cite T1-03 and T0-14 directly.
- **Skills:** borrowed posting shares carry "(feeder)", "(adjacent)" or "(closest)" in the inventories' summaries (AGENTS §3.4); the skills-ontology method page was merged into the role skill inventories; the inventories folder page and the vocabulary's credentials section point to the single tables; credential ROI links credentials by role instead of keeping its own status register.
- **Freshness (D-020):** 99 pages carry `review_by` (35 before). Role hubs take theirs from the oldest posting-count source they cite (2026-11-14 to 2026-12-03), inventories from the tool-status date. The role catalog and rankings fall due on 2026-11-14 (Skillenai counts). The visa page collects its contested-rule statuses in one dated table and stays due until someone re-verifies it.
- **Validation:** the validator rejects schema keywords it does not enforce (the front-matter `maximum` is now enforced); no schema check is skipped when a schema file is missing; session line references in `tools.json` and `interview_prompts.json`, prompt counts and track and archetype coverage are checked; rank checks fail when a format stops matching; counts in generated text are computed from the data; the manifest ignores headings inside code blocks.
- **Prep packs:** role lists are names, linked once in the track table (113.6 KB → 90.4 KB).
- **Documentation:** AGENTS, CONTRIBUTING (owners, British spelling in prose, the generator registry, tests), README (one-line grade summary), research/README (the research pipeline 2 procedure, session numbering by layer, the Vivechak templates and tool files), data/README (every reader of each file), scripts/README (build order, shared modules, tests), CHARTER (a dated status note), the session template's pointer to EGP-1.0.

### Fixed
- ERRATA's list of records with errata, and its copies in AGENTS.md and the glossary, now include T0-06 (U25); its sources and next-ID instruction were corrected.
- Negotiation playbook: ≈0.2% is application to hire, not to offer (ERRATA U24). Pay benchmarks: platform data are Grade B (D-018). Role rankings: an unsourced "$220–330K+" base replaced with sourced T0-02 figures. Role skill inventories: a fact-check claim contradicted by its own verification section. Résumé strategy: the target order is computed, not hand-edited. Channels and boards and referrals and outreach now agree on referral timing; channels links the tool catalog's verdicts. Stack model: three candidate titles match the catalog. CAIO hub: T0-18 rates the demand evidence "conflicting". Employer landscape: a non-EGP grade tag. Coding rounds: both readings of T0-03 on lab job descriptions.

### Removed
- `career/03-skills-and-tech/skills-ontology-method.md` (merged into the role skill inventories).

## [0.2.0] - 2026-11-07

Every lifecycle stage now has its core guides. The structure of an older handbook informed some formats (decision D-016); every fact comes from the repository's own research. This release changes paths, a schema and data formats, so it is a minor version under D-014. Known issues at release are listed in `ROADMAP.md` §7, and two pages are due for re-verification: visa and relocation, and the market overview's pay snapshot.

### Added
- **Role map and stack model (D-015):** `data/stack_model.json` and its schema (six layers, four cross-cutting planes, the map from every skill category to a layer or plane, 26 specialisations inside roles); a definition, work footprint and interview track for every role in `data/role_scores.json`; `scripts/build_role_map.py` generates `career/02-roles/role-map.md`. The map shows where work sits; it is not a pay model.
- **Role hubs:** one generated page per role (29) and an index in `career/02-roles/hubs/` (`scripts/build_role_hubs.py`), linking each role's numbers, skills, projects, interview pack, résumé block and track playbook.
- **Stage 00, start-here tools:** the targeting workbook, the glossary and the tool catalog (`data/tools.json` and its schema; `scripts/build_tool_catalog.py`).
- **Stage guides** in the guide pattern (D-016):
  - 01: market overview, employer landscape, emerging roles;
  - 03: learning roadmaps, agentic protocols;
  - 04: credential ROI;
  - 05: proof-of-work standards;
  - 06: ATS mechanics, channels and boards, application operating system;
  - 07: referrals and outreach, communities guide, online presence;
  - 08: interview loops, system-design archetypes, behavioural calibration, coding rounds;
  - 09: pay benchmarks, offer evaluation, negotiation playbook, India remote tax;
  - 10: first 90 days, growth and progression;
  - 11: career transitions, PhD to industry, India remote playbook, visa and relocation, freelance and fractional, governance careers.
- **Generated views:**
  - the skills radar and credentials by role (`scripts/build_skills_views.py`), with a register of devalued skills and what to learn instead in the ontology (T0-03 §4.3, §6.8.2);
  - project archetype cards with minimal project sets (`scripts/build_archetypes.py`; `data/project_archetypes.json` format 1.1 with problem, build steps, evidence, verifiability target, effort, compute, interview archetypes, pitfalls and sources, plus a schema);
  - interview prep packs (`data/interview_prompts.json` and its schema; `scripts/build_prompts.py`).
- **Personal gap analysis:** `scripts/gap_analysis.py` compares your 0–3 self-ratings with several target roles and prints gaps, priorities and the projects that would evidence them; `personal/` is git-ignored for such files.
- **Decisions:** D-015 (stack map), D-016 (legacy-handbook policy and the guide pattern), D-017 (review-by dates and a due report), D-018 (evidence conventions for the stage guides).
- **`ROADMAP.md` §7, known issues and follow-ups:** candidate errata to verify, grading edge cases, checks against primary sources, and data that need refreshing.
- **Errata U13–U26:** a retired AWS certification in T2-01, conflicting India tier bands, FAD's repeat of U12, FAD's ATS "parser bypass" plan and Jobscan, FAD's interview-platform list, FAD's "PhD skips stage 03", T2-01's dollar conversion of the India tax dead zone, D-004's unmeasured ">80% of postings" tier thresholds, T2-01's misread onboarding statistics, D-007's wrong T0-08 finding numbers, T2-01's UK hourly-rate range, T1-03's funnel stage rates against T0-04, T0-06's leisure-share range and T1-03's count of Anthropic infrastructure reports.
- **Front matter:** `content_type: tool` and an optional `review_by` date.
- **Validator:** writing rules (relative-time words outside quotes and code; any reference to the legacy handbook, and its signature phrases outside quotes and code, in the documents and the data files), a dead-end check, the guide-pattern headings (D-016), the stack-model checks, every new generator's `--check`, a list of pages past their `review_by` date (`--strict` counts them as problems), and `--files` for checking single documents.

### Changed
- **Start Here** (`career/README.md`): routes by situation (eleven situations) and by question, shows the map of the field, defines the five role labels once, gives the stage status and paths for five researched backgrounds (with modelled times) plus three provisional ones.
- **Stage READMEs 01–11:** list the new documents; record the merges (visa and regulated careers into stage 11, unconventional tactics into referrals and outreach) and the renaming of the planned compensation ladder to pay benchmarks.
- **`AGENTS.md`:** the folder-to-funnel stage map, sources of truth for the new data files and generators, freshness rules, the D-016 legacy rule, the D-018 conventions, the validator's options, and a pointer to the pending work in ROADMAP §4–§7. **`CONTRIBUTING.md`:** placement (stage 00, role facts in data), front matter, the writing standard with the P grade, the guide pattern, the generators table, and the steps before finishing, including an independent fact-check of new guides.
- **`README.md`, `ROADMAP.md`, `research/README.md`, `data/README.md`, `scripts/README.md`:** updated for full stage coverage, the remaining research gaps, the maintenance calendar and the open decisions.
- **`scripts/target_roles.py`:** `--update` writes the GenAI target order into the skills ontology and `--check` verifies it and the target-roles table.
- **Skills ontology format 1.1:** adds the devalued-skills register, validated by `build_skills.py`.
- **Role catalog:** the registry's family labels match `data/role_scores.json`; every profile links to its hub; the catalog, rankings and target roles point to the hubs and the role map.
- **`llms.txt` and the manifest:** a stage 00 section, the hubs grouped under Optional, and the new data files.
- **Skill maps:** role headings read "CCI rank #N", and inventory links use the `inventories/` path.
- D-013 to D-018 are marked as human-reviewed: the owner approved D-013 and D-014 on 2026-11-05 and D-015 to D-018 on 2026-11-07.
- **`CONTRIBUTING.md` §3** states EGP-1.0's time-to-live classes as T1-02 §10.6 defines them (posting counts 31 days, tool statuses 90 days, pay medians 180 days, with pay re-verified here after 90), and the rule that Levels.fyi, JobsPipe and Fast AI Jobs data are Grade B; the guides' `review_by` dates and platform grades follow them.
- **Fact-check:** 13 independent agents checked 4,829 claims in the new guides against their cited session lines and made 234 fixes; a script cross-checked every figure against the lines each page cites.
- **Leak check (D-016):** on 2026-11-07 a script compared the legacy handbook with the repository's published content. No figure that appears only in the handbook, and none of its prose, appears in the content. The overlaps it found are standard terms (a stock-option definition, the public X-Y-Z résumé pattern, TTFT and TPOT), two FAD and T0-17 pay bands written in a different format, and job titles that the v0.1.0 catalog already classified. The stack map's layer order follows the handbook's six-layer stack by design, as its basis states. The validator keeps the handbook's signature phrases as canaries, so the check no longer needs the handbook.

### Fixed
- The FDE pay contradiction: the catalog and the rankings said the corpus had no FDE pay data, while both quoted a measured posted base of $180–248K (n=304) [B · T0-03]. Both now say that FDE has posted base pay only and no total-compensation data.
- "a AI" in the generated inventory headers.
- Grade E in `CONTRIBUTING.md` and `README.md` now matches EGP-1.0 (T1-02 §10.3.1): speculative, unverifiable or promotional, or nothing found; never asserted.
- A relative-time word in `CHARTER.md`.
- The job-search strategy's `generated_by` now marks it as a file with generated blocks.
- The role catalog's Voice AI entry now gives both of T0-14's attributions (Meta's ML pool and a multi-company question pool) instead of Meta alone.
- Project archetype P2's verifiability target is V1 with a 30-day operations log, as reference spec R2 sets it (T0-13 L275), not V3; the archetype data and page carry a `review_by` date for their dollar caps.

## [0.1.0] - 2026-11-04

First development release: the Phase 0 evidence base and the Phase 1 foundation.

### Added
- **Evidence base (Phase 0):** 22 research sessions across Layer 0 (landscape), Layer 1 (blueprints) and Layer 2 (tier playbooks), written to the Evidence-Grounding Protocol (EGP-1.0), plus the research pipeline and session templates.
- **Founding architecture and governance:** the project charter, the Founding Architecture Document (FAD) and the decision registry (D-001 to D-014).
- **Role catalog and rankings:**
  - 29 canonical GenAI roles, with 241 title strings classified in an A–Z index generated by `scripts/build_index.py`.
  - Evidence-weighted Composite Career Index (CCI) rankings with uncertainty ranges and Monte Carlo rank intervals (`scripts/rank_roles.py`, `data/role_scores.json`).
  - GenAI target-role shortlist (`career/02-roles/genai-target-roles.md`, `scripts/target_roles.py`).
- **Skills ontology and inventories:**
  - One source of truth in `data/skills_ontology.json`: 523 typed skills in 19 types, 35 choose-one classes, 20 credentials, 15 resume variants and 1,529 evidence-tagged role links.
  - The skills vocabulary, the inventories index and 26 role skill inventories, generated by `scripts/build_skills.py`.
  - Per-role skill maps: table-stakes, differentiating and frontier skills (`career/03-skills-and-tech/role-skill-maps.md`).
- **Job search and resumes:**
  - Layered resume strategy (L0 master → L1 universal → L2 family → L3 role → L4 posting-tailored).
  - Resume skills matrix generated from the ontology's headline skills (`scripts/build_resume_matrix.py`).
  - 20 proof-of-work project archetypes and the project sets that cover every role (`data/project_archetypes.json`, `scripts/resume_layers.py`).
- **Navigation and documentation:**
  - Start Here page (`career/README.md`) and an index for each of the 11 lifecycle stages (decision D-013).
  - `ROADMAP.md` (coverage, phases, build plan, open decisions) and `CONTRIBUTING.md` (placement, front matter, writing standard, versioning).
  - Research index (`research/README.md`) and errata for the sealed Phase 0 records (12 errors, `research/ERRATA.md`).
  - Front-matter schema for every career document (`data/schemas/frontmatter.schema.json`).
- **Findings registry and AI discoverability:**
  - 262 key findings extracted into `data/findings.json` and `research/findings.md` (`scripts/build_findings.py`).
  - Rules for AI agents in `AGENTS.md`.
  - Document manifest and LLM index generated by `scripts/build_manifest.py` (`data/manifest.json`, `llms.txt`).
- **Validation:** `scripts/validate_docs.py`, run by CI (`.github/workflows/validate.yml`) on every push and pull request, checks relative links and anchors, table shapes, front matter, every generator's output, cross-file ranks and corpus coverage.

[Unreleased]: https://github.com/bhaskarjha-dev/genai-career/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/bhaskarjha-dev/genai-career/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/bhaskarjha-dev/genai-career/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/bhaskarjha-dev/genai-career/releases/tag/v0.1.0
