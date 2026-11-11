# Scripts: Generators, Validator and Tests

Standard-library Python 3 only. Run them from the repository root with `python3 -B` (or `PYTHONDONTWRITEBYTECODE=1`), so that no `__pycache__` is left behind.

## Everyday commands

```bash
python3 -B scripts/build_all.py                       # run every generator in order (--update), then the validator
python3 -B scripts/build_all.py --check               # check every generated output, then validate (what CI does)
python3 -B scripts/validate_docs.py --files <path>    # document checks for the pages you are editing
python3 -B -m unittest discover -s scripts/tests -v   # tests for the machinery
```

`GENERATORS` in [build_all.py](build_all.py) is the single registry of generators and their order; the validator fails if a script supports `--check` but is missing from it. Every generator supports `--update` (rewrite its output) and `--check` (exit 1 if the output is stale).

## Generators, in build order

| Script | Reads | Writes |
|---|---|---|
| [build_findings.py](build_findings.py) | `research/sessions/` | `data/findings.json`, `research/findings.md` |
| [build_index.py](build_index.py) | `data/role_titles.json` + schema, `data/role_scores.json` (role ids) | The A–Z index block in `career/02-roles/role-catalog.md` |
| [rank_roles.py](rank_roles.py) | `data/role_scores.json` + schema | Generated blocks in `career/02-roles/role-rankings.md` |
| [target_roles.py](target_roles.py) | `data/role_scores.json` (via `rank_roles.py`) | `--update` writes the GenAI target order into `data/skills_ontology.json`; `--check` also verifies the table in `career/02-roles/genai-target-roles.md` |
| [build_skills.py](build_skills.py) | `data/skills_ontology.json` + schema, `data/posting_skill_shares.json`, `research/sessions/` (citations and corpus counts) | Blocks in `career/03-skills-and-tech/skills-vocabulary.md` and `role-skill-inventories.md`; `inventories/*.md` |
| [build_resume_matrix.py](build_resume_matrix.py) | `data/skills_ontology.json` | Generated blocks in `career/06-job-search/resume-skills-matrix.md` |
| [resume_layers.py](resume_layers.py) | `data/skills_ontology.json`, `data/project_archetypes.json` | The computed résumé-layer blocks in the job-search guides |
| [build_skills_views.py](build_skills_views.py) | `data/skills_ontology.json`, `data/posting_skill_shares.json` | `career/03-skills-and-tech/skills-radar.md`, `career/04-certifications/credentials-by-role.md` |
| [build_archetypes.py](build_archetypes.py) | `data/project_archetypes.json` + schema, the ontology, the stack model, `data/interview_prompts.json` | `career/05-portfolio/project-archetypes.md` |
| [build_role_map.py](build_role_map.py) | `data/stack_model.json`, `data/role_scores.json`, the ontology, the project archetypes | `career/02-roles/role-map.md` |
| [build_role_hubs.py](build_role_hubs.py) | Every data file above, plus `rank_roles.py` and `resume_layers.py` | `career/02-roles/hubs/` (one hub per role and an index) |
| [build_prompts.py](build_prompts.py) | `data/interview_prompts.json` + schema, `data/role_scores.json`, the ontology, session line counts | `career/08-interviewing/prep-packs.md` |
| [build_tool_catalog.py](build_tool_catalog.py) | `data/tools.json` + schema, session line counts | `career/00-start/tool-catalog.md` |
| [research_pipeline.py](research_pipeline.py) | `research/pipeline-2/catalogue.json`, its briefs and protocol, `data/role_scores.json`, the ontology, `data/role_titles.json`, `data/tools.json`, `data/posting_skill_shares.json`, `research/sessions/` (which sessions are saved) | The tracker block in `research/pipeline-2/README.md`. Also, writing nothing: `--prompt <id>` prints a session's prompt, `--next` lists sessions to run, `--appendix` checks a session report, `--verify` prints a verification packet |
| [build_manifest.py](build_manifest.py) | Front matter of `career/` and the research index pages; session front matter | `llms.txt`, `data/manifest.json` (last, because it indexes everything) |

## Shared modules, validator and tests

- [common.py](common.py): the JSON Schema subset (`schema_errors`, which rejects keywords it does not implement), session line-reference checks, and small text helpers (`esc`, `short`, `skill_name`, `gh_slug`, `heading_slug`).
- [stack_lib.py](stack_lib.py): loading and validating the stack model and role footprints (decision D-015), labels shared by the role map and hubs.
- [validate_docs.py](validate_docs.py): reads everything and writes nothing. It checks links, anchors, tables, front matter, writing rules, dead ends, the guide pattern, every generator's `--check`, the stack model, cross-file ranks and corpus coverage, prints `PROBLEMS: <n>`, and lists documents past their `review_by` date. `--files <path>` checks single documents; `--strict` counts due documents as problems.
- [tests/](tests/): unit tests for the schema subset, citation checks, the validator's document rules, every data file against its schema, and a smoke test of the personal tool. CI runs them before the validator.

## Personal tool

[gap_analysis.py](gap_analysis.py) compares your own 0–3 skill ratings with one or more target roles and prints the gaps, the skills to close first and the projects that would evidence them. It writes nothing to the repository; keep your self-assessment in your own career repository (decision D-022) or under `personal/` (git-ignored).

```bash
python3 -B scripts/gap_analysis.py --template ai-engineer applied-ai-engineer > personal/me.json
python3 -B scripts/gap_analysis.py personal/me.json
```
