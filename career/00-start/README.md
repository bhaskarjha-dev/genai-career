---
id: stage-00
title: "Stage 00: Start-here tools"
content_type: index
stage: 0
status: published
last_verified: 2026-11-05
summary: "Index of stage 00 (start-here tools): the workbook, glossary and tool catalog that help at every stage of a GenAI career search, plus a personal script that turns your skill ratings into a gap report."
sources: [T0-06, T0-10]
---

# Stage 00: Start-here tools

> **The question this stage answers:** Which tools help at every stage?
> **Status:** Covered: the targeting workbook, the glossary, the tool catalog and the personal gap-analysis script exist. Overall progress is tracked in [ROADMAP.md](../../ROADMAP.md).

These pages are not tied to one lifecycle stage. Use them alongside [Start Here](../README.md), which routes you by situation.

## In this folder

| Document | What it gives you |
|---|---|
| [targeting-workbook.md](targeting-workbook.md) | A fill-in workbook from "where do I start?" to a ranked target list (primary, adjacent and stretch) and a 90-day plan: self-assessment, constraints, shortlist scoring, gates |
| [glossary.md](glossary.md) | Every term and acronym used in the repository, with a plain definition and where it is used |
| [tool-catalog.md](tool-catalog.md) | External career tools and platforms by stage, each with a verdict (use, use with care, avoid, watch), its evidence grade and the date it was checked; generated from [data/tools.json](../../data/tools.json) |

## Personal tool: skill-gap analysis

[scripts/gap_analysis.py](../../scripts/gap_analysis.py) compares your own 0–3 skill ratings with the tiered skills of one or more target roles in [data/skills_ontology.json](../../data/skills_ontology.json), and prints a gap report:
- for each target role, how much of its Must and Important skills you cover, and every gap;
- across all your targets, the skills to close first, weighted by tier and by how many targets need them;
- the [project archetypes](../05-portfolio/project-archetypes.md) that would evidence the most of your gaps.

The scale is T0-06's: 0 none, 1 tutorial-level, 2 built and shipped something small with feedback, 3 owns it in production. The target level per tier (Must 3, or 2 at entry level; Important 2; Should 1) is judgement [D, anchored on T0-06]. The script prints to standard output only and writes nothing to the repository. Your ratings are personal data: keep them outside the repository or in its `personal/` folder, which git ignores.

```bash
python3 -B scripts/gap_analysis.py --template ai-engineer applied-ai-engineer > personal/me.json
# edit personal/me.json: set each level from 0 to 3
python3 -B scripts/gap_analysis.py personal/me.json
python3 -B scripts/gap_analysis.py personal/me.json --entry     # accept 2 for Must skills (entry level)
```

Role IDs are the role slugs that name the hub files, such as `ai-engineer` (see the [role hubs](../02-roles/hubs/README.md)); the script accepts any role that has skill tiers in the ontology. Use the report in Steps 2 and 5 of the [targeting workbook](targeting-workbook.md).

## Planned

| Document | Scope | Built from |
|---|---|---|
| Résumé generator | Builds role-variant résumés from a personal, git-ignored inventory (roadmap P0-1) | `data/skills_ontology.json`, résumé strategy |

## Evidence to read now

- **Findings:** the [findings registry](../../research/findings.md) lists every key finding by stage, each with its grade and line.
- **Research sessions:**
  - [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md): career transition timelines, skill deltas and quarterly roadmaps for five starting backgrounds (October 2026)
  - [T0-10](../../research/sessions/T0-10-career-tooling-ecosystem-12-stage-funnel.md): the evidence-graded career tooling ecosystem across the 12-stage funnel (October 2026)

[← Start Here](../README.md)
