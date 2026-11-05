# Data: Machine-Readable Sources of Truth

The documents in [career/](../career/README.md) that show scores, skills or findings are generated from these files by [scripts/](../scripts/README.md). Edit the data, then run the generator; never hand-edit generated output.

| File | What it holds | Edited by | Generates |
|---|---|---|---|
| [role_scores.json](role_scores.json) | Every role's pillar scores (demand, pay, durability, leverage, access) as [lo, mid, hi] ranges, each with an evidence grade and sourced basis | Hand | Role-ranking tables (`rank_roles.py`), target order (`target_roles.py`) |
| [skills_ontology.json](skills_ontology.json) | 523 typed skills, choose-one classes, credentials, resume variants, every role's tiered and evidence-tagged skill links, tier decisions, verification summary | Hand | Skills vocabulary, role inventories, resume skills matrix (`build_skills.py`, `build_resume_matrix.py`) |
| [project_archetypes.json](project_archetypes.json) | 20 proof-of-work project archetypes and the headline skills each one evidences | Hand | The job-search strategy's computed blocks (`resume_layers.py`) |
| [findings.json](findings.json) | The 262 key findings of the research sessions, with grade, exact line and lifecycle stages | `build_findings.py` | [research/findings.md](../research/findings.md) |
| [manifest.json](manifest.json) | Every document's front matter and section headings | `build_manifest.py` | [llms.txt](../llms.txt) |
| [schemas/](schemas/) | JSON Schemas for the skills ontology and for document front matter | Hand | — |
