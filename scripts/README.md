# Scripts: Generators and Validator

Standard-library Python 3 only. Run them from the repository root, with `python3 -B` (or `PYTHONDONTWRITEBYTECODE=1`) so that no `__pycache__` is left behind. Every generator supports `--update` (rewrite its output) and `--check` (exit 1 if the output is stale).

| Script | Reads | Writes |
|---|---|---|
| [rank_roles.py](rank_roles.py) | `data/role_scores.json` | Generated blocks in `career/02-roles/role-rankings.md` |
| [target_roles.py](target_roles.py) | `data/role_scores.json` (via `rank_roles.py`) | Prints the GenAI target-order analysis behind `career/02-roles/genai-target-roles.md` |
| [build_index.py](build_index.py) | Its own structured title list | The A–Z index in `career/02-roles/role-catalog.md` |
| [build_skills.py](build_skills.py) | `data/skills_ontology.json` + schema, `research/sessions/` (corpus counts) | `career/03-skills-and-tech/skills-vocabulary.md` and `role-skill-inventories.md` blocks, `inventories/*.md` |
| [build_resume_matrix.py](build_resume_matrix.py) | `data/skills_ontology.json` (headline layer) | Generated blocks in `career/06-job-search/resume-skills-matrix.md` |
| [resume_layers.py](resume_layers.py) | `data/skills_ontology.json`, `data/project_archetypes.json` | Computed blocks in `career/06-job-search/job-search-strategy.md` |
| [build_findings.py](build_findings.py) | `research/sessions/` | `data/findings.json`, `research/findings.md` |
| [build_manifest.py](build_manifest.py) | Front matter of `career/` and the research index pages | `llms.txt`, `data/manifest.json` |
| [validate_docs.py](validate_docs.py) | Everything above | Nothing. It checks links, anchors, tables, front matter, every generator's `--check`, cross-file ranks and corpus coverage, and prints `PROBLEMS: <n>` |
