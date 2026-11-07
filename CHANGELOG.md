# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html); see decision D-014 in [research/DECISIONS.md](research/DECISIONS.md).

## [Unreleased]

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

[Unreleased]: https://github.com/bhaskarjha-dev/genai-career/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/bhaskarjha-dev/genai-career/releases/tag/v0.1.0
