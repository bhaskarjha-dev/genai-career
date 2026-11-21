---
id: stage-00
title: "Stage 00: Start-here tools"
content_type: index
stage: 0
status: published
last_verified: 2026-11-19
summary: "Index of stage 00 (start-here tools): the workbook, glossary and 291-tool catalog that help at every stage of a GenAI career search, plus a personal script that turns your skill ratings into a gap report."
sources: [T0-06, T0-10, T0-19, T0-23, T0-26, T0-27, T0-43, T0-47, T0-67, T0-68, T1-02]
---

# Stage 00: Start-here tools

> **The question this stage answers:** Which tools help at every stage?
> **Status:** Covered: the targeting workbook, the glossary, the 291-tool catalog (with the 4-Tier Data Hygiene upload policy) and the personal gap-analysis script exist. Overall progress is tracked in [ROADMAP.md](../../ROADMAP.md).

These pages are not tied to one lifecycle stage. Use them alongside [Start Here](../README.md), which routes you by situation.

## In this folder

| Document | What it gives you |
|---|---|
| [targeting-workbook.md](targeting-workbook.md) | A step-by-step workbook from "where do I start?" to a ranked target list (primary, adjacent and stretch) across nine starting backgrounds and a 90-day plan, recorded in your own career repository: self-assessment, constraints, shortlist scoring, gates |
| [glossary.md](glossary.md) | Every term, code and acronym used in the repository (updated for RP2), with a plain definition and where it is used |
| [tool-catalog.md](tool-catalog.md) | 291 external career tools and platforms by stage, each with a verdict (use, use with care, avoid, watch), evidence grade, check date and the T0-10 4-Tier Data Hygiene policy; generated from [data/tools.json](../../data/tools.json) |

## Cross-stage generated catalogs and directories

| Resource | Where it lives |
|---|---|
| Target GenAI employers (95 employers + 7 sponsor registers) | [target-employers.md](../01-landscape/target-employers.md) |
| GenAI career hype register (Decision D-012) | [hype-register.md](../01-landscape/hype-register.md) |
| Rated learning resources (Decision D-027) | [learning-resources.md](../03-skills-and-tech/learning-resources.md) |
| Ranked credential catalog (Decision D-026) | [credential-catalog.md](../04-certifications/credential-catalog.md) |
| Country and city rankings (Decision D-025) | [country-rankings.md](../11-tracks/country-rankings.md) |

## Personal tool: skill-gap analysis

[scripts/gap_analysis.py](../../scripts/gap_analysis.py) compares your own 0–3 skill ratings with the tiered skills of one or more target roles in [data/skills_ontology.json](../../data/skills_ontology.json), and prints a gap report:
- for each target role, how much of its Must and Important skills you cover, and every gap;
- across all your targets, the skills to close first, weighted by tier and by how many targets need them;
- the [project archetypes](../05-portfolio/project-archetypes.md) that would evidence the most of your gaps.

The scale is T0-06's: 0 none, 1 tutorial-level, 2 built and shipped something small with feedback, 3 owns it in production. The target level per tier (Must 3, or 2 at entry level; Important 2; Should 1) is judgement [D, anchored on T0-06]. The script prints to standard output only and writes nothing to the repository. Your ratings are personal data: keep them in your own career repository (decision D-022), or in this repository's `personal/` folder, which git ignores.

```bash
python3 -B scripts/gap_analysis.py --template ai-engineer applied-ai-engineer > personal/me.json
# edit personal/me.json: set each level from 0 to 3
python3 -B scripts/gap_analysis.py personal/me.json
python3 -B scripts/gap_analysis.py personal/me.json --entry     # accept 2 for Must skills (entry level)
```

Role IDs are the role slugs that name the hub files, such as `ai-engineer` (see the [role hubs](../02-roles/hubs/README.md)); the script accepts any role that has skill tiers in the ontology. Use the report in Steps 2 and 5 of the [targeting workbook](targeting-workbook.md).

## Planned

Nothing is planned for this stage. Your own records, from these ratings to your résumés, live in your own career repository, not here (decision D-022); [pramedha-template](https://github.com/bhaskarjha-dev/pramedha-template) is one free implementation.

## Evidence to read

- **Findings:** the [findings registry](../../research/findings.md) lists every key finding across the 75 sessions by stage, each with its grade and line.
- **Research sessions:**
  - [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) and [T0-67](../../research/sessions/T0-67-transitions-devops-pm-it-services-students.md): career transition timelines, skill deltas and roadmaps across nine starting backgrounds (October–November 2026)
  - [T0-10](../../research/sessions/T0-10-career-tooling-ecosystem-12-stage-funnel.md), [T0-26](../../research/sessions/T0-26-job-search-tools-agents-oss-mcp.md), [T0-27](../../research/sessions/T0-27-target-employers-sponsor-registers-data.md) and [T0-68](../../research/sessions/T0-68-learning-resources-rated.md): evidence-graded career tooling, automation, data-hygiene and compute audits (October–November 2026)
  - [T1-02](../../research/sessions/T1-02-evidence-grounding-protocol.md): EGP-1.0 evidence standard, CAP-1 and Hype Register rules (October 2026)

[← Start Here](../README.md)
