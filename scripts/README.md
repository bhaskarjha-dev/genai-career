# Scripts: Generators and Validator

Standard-library Python 3 only. Run them from the repository root, with `python3 -B` (or `PYTHONDONTWRITEBYTECODE=1`) so that no `__pycache__` is left behind. Every generator supports `--update` (rewrite its output) and `--check` (exit 1 if the output is stale).

| Script | Reads | Writes |
|---|---|---|
| [rank_roles.py](rank_roles.py) | `data/role_scores.json` | Generated blocks in `career/02-roles/role-rankings.md` |
| [target_roles.py](target_roles.py) | `data/role_scores.json` (via `rank_roles.py`) | `--update` writes the GenAI target order into `data/skills_ontology.json`; `--check` also verifies the table in `career/02-roles/genai-target-roles.md` |
| [build_index.py](build_index.py) | Its own structured title list | The A–Z index in `career/02-roles/role-catalog.md` |
| [build_role_map.py](build_role_map.py) | `data/stack_model.json`, `data/role_scores.json`, the ontology, the project archetypes | `career/02-roles/role-map.md` |
| [build_role_hubs.py](build_role_hubs.py) | Every data file above, plus `rank_roles.py` and `resume_layers.py` | `career/02-roles/hubs/` (one hub per role and an index) |
| [build_skills.py](build_skills.py) | `data/skills_ontology.json` + schema, `research/sessions/` (corpus counts) | `career/03-skills-and-tech/skills-vocabulary.md` and `role-skill-inventories.md` blocks, `inventories/*.md` |
| [build_skills_views.py](build_skills_views.py) | `data/skills_ontology.json` | `career/03-skills-and-tech/skills-radar.md`, `career/04-certifications/credentials-by-role.md` |
| [build_resume_matrix.py](build_resume_matrix.py) | `data/skills_ontology.json` (headline layer) | Generated blocks in `career/06-job-search/resume-skills-matrix.md` |
| [resume_layers.py](resume_layers.py) | `data/skills_ontology.json`, `data/project_archetypes.json` | Computed blocks in `career/06-job-search/job-search-strategy.md` |
| [build_archetypes.py](build_archetypes.py) | `data/project_archetypes.json` + schema, the ontology, the stack model, `data/interview_prompts.json` | `career/05-portfolio/project-archetypes.md` |
| [build_prompts.py](build_prompts.py) | `data/interview_prompts.json` + schema, `data/role_scores.json`, the ontology | `career/08-interviewing/prep-packs.md` |
| [build_tool_catalog.py](build_tool_catalog.py) | `data/tools.json` + schema | `career/00-start/tool-catalog.md` |
| [build_findings.py](build_findings.py) | `research/sessions/` | `data/findings.json`, `research/findings.md` |
| [build_manifest.py](build_manifest.py) | Front matter of `career/` and the research index pages | `llms.txt`, `data/manifest.json` |
| [validate_docs.py](validate_docs.py) | Everything above | Nothing. It checks links, anchors, tables, front matter, writing rules, dead ends, every generator's `--check`, the stack model, cross-file ranks and corpus coverage, prints `PROBLEMS: <n>`, and lists documents past their `review_by` date. `--files <path>` checks single documents; `--strict` counts due documents as problems |

[stack_lib.py](stack_lib.py) is a shared module (stack-model loading and validation), not a generator.

## Personal tool

[gap_analysis.py](gap_analysis.py) compares your own 0–3 skill ratings with one or more target roles and prints the gaps, the skills to close first and the projects that would evidence them. It writes nothing to the repository; keep your self-assessment under `personal/` (git-ignored) or elsewhere.

```bash
python3 -B scripts/gap_analysis.py --template ai-engineer applied-ai-engineer > personal/me.json
python3 -B scripts/gap_analysis.py personal/me.json
```
