# Data: Machine-Readable Sources of Truth

The documents in [career/](../career/README.md) that show scores, skills, projects, prompts, tools or findings are generated from these files by [scripts/](../scripts/README.md). Edit the data, then run the generator; never hand-edit generated output.

| File | What it holds | Edited by | Generates |
|---|---|---|---|
| [role_scores.json](role_scores.json) | Every role's definition, work footprint (layers and planes), interview track, and pillar scores (demand, pay, durability, leverage, access) as [lo, mid, hi] ranges, each with an evidence grade and sourced basis; the interview tracks | Hand | Role-ranking tables (`rank_roles.py`), target order (`target_roles.py`), role map (`build_role_map.py`), role hubs (`build_role_hubs.py`) |
| [stack_model.json](stack_model.json) | The stack map (decision D-015): six layers, four cross-cutting planes, the map from skill categories to layers, and the specialisations inside roles | Hand | Role map, role hubs |
| [skills_ontology.json](skills_ontology.json) | 523 typed skills, choose-one classes, credentials, resume variants, every role's tiered and evidence-tagged skill links, tier decisions, the register of devalued skills, verification summary | Hand (targets by `target_roles.py`) | Skills vocabulary, role inventories, resume skills matrix, skills radar, credentials by role (`build_skills.py`, `build_resume_matrix.py`, `build_skills_views.py`) |
| [project_archetypes.json](project_archetypes.json) | The proof-of-work project archetypes: problem, build steps, evidence to publish, verifiability target, effort, compute, interview archetypes, pitfalls, sources and the headline skills each one evidences | Hand | Project archetypes page (`build_archetypes.py`), the job-search strategy's computed blocks (`resume_layers.py`) |
| [interview_prompts.json](interview_prompts.json) | Practice prompts keyed to interview tracks, the 15 system-design archetypes, roles and skills, with what a strong answer covers and red flags | Hand | Prep packs (`build_prompts.py`) |
| [tools.json](tools.json) | External career tools and platforms by stage, with verdict, evidence grade, source and date | Hand | Tool catalog (`build_tool_catalog.py`) |
| [findings.json](findings.json) | The 262 key findings of the research sessions, with grade, exact line and lifecycle stages | `build_findings.py` | [research/findings.md](../research/findings.md) |
| [manifest.json](manifest.json) | Every document's front matter and section headings | `build_manifest.py` | [llms.txt](../llms.txt) |
| [schemas/](schemas/) | JSON Schemas for the data files and for document front matter | Hand | — |
