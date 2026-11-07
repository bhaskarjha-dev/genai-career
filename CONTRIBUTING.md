# Contributing

This repository aims to be the most accurate, best-organised source on GenAI careers, for people and for AI agents. These conventions keep it that way. AI agents should also read [AGENTS.md](AGENTS.md).

## 1. Where things go

| You are adding… | Put it in | And |
|---|---|---|
| A guide, reference or tool for one lifecycle stage | `career/NN-stage/` (kebab-case file name) | List it in that folder's `README.md`; move its row out of "Planned" |
| A tool used across stages (workbook, tracker, catalog, glossary) | `career/00-start/` with `content_type: tool` (or `reference`) | Link it from [Start Here](career/README.md) |
| A cross-cutting playbook for a background, location or working model | `career/11-tracks/` | Same |
| A fact about a role (definition, work footprint, interview track, pillar score) | `data/role_scores.json` | Run the generators; the role hubs and the role map are rebuilt from it |
| Structured data that documents are built from | `data/` (snake_case), with a schema in `data/schemas/` when the structure matters | Add a generator in `scripts/` rather than hand-copying values into documents |
| New research | `research/sessions/` as a new session (see [research/README.md](research/README.md)) | Run `python3 -B scripts/build_findings.py --update` |
| A correction to a Phase 0 record | `research/ERRATA.md` | Fix the affected career documents |
| An architectural decision | Append to `research/DECISIONS.md` | Reference it in [CHANGELOG.md](CHANGELOG.md) |

The lifecycle stages are: 00 start-here tools, 01 landscape, 02 roles, 03 skills and technology, 04 certifications, 05 portfolio, 06 job search, 07 networking, 08 interviewing, 09 compensation, 10 onboarding, 11 tracks. Reference material sits in the stage where it is used. The folder numbers differ from the 12-stage funnel numbers in D-001; [AGENTS.md](AGENTS.md) maps the two.

## 2. Front matter

Every document under `career/`, and the research index pages, starts with YAML front matter. The schema is [data/schemas/frontmatter.schema.json](data/schemas/frontmatter.schema.json).

```yaml
---
id: job-search.ats-mechanics       # unique, dotted, lowercase
title: "ATS Mechanics: How Screening Works"
content_type: guide                # index | guide | reference | method | tool
stage: 6                           # 0 = cross-stage; must match the folder number
status: published                  # planned | draft | published | stale
last_verified: 2026-11-05
review_by: 2027-01-21              # optional: earliest expiry of the volatile facts on the page (D-017)
summary: "One sentence, 20-320 characters: what the reader gets."
sources: [T0-04, T0-10]            # research sessions relied on
roles: [all]                       # optional: role slugs
geos: [global, india]              # optional
tags: [ats, resume]                # optional
generated_by: scripts/x.py         # only for generated files
---
```

`scripts/build_manifest.py` turns front matter into [llms.txt](llms.txt) and [data/manifest.json](data/manifest.json). Run it with `--update` after adding or retitling a document, or after changing any front-matter field.

**`review_by`:** set it on any page that states volatile facts: the earliest date on which one of them passes its time-to-live (§3). A page quoting tool statuses verified on 2026-10-23 gets `review_by: 2027-01-21`; a page quoting posting counts taken on 2026-10-19 gets `2026-11-19`. A past date is allowed and honest. The validator lists published pages past their date as DUE.

## 3. Writing standard (EGP-1.0 in brief)

The full protocol is [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) (decision D-012).

**Grade every empirical claim:**

| Grade | Meaning |
|---|---|
| A | Primary authoritative source: official documentation, government filings, peer-reviewed research, measured data |
| B | Established secondary source with a transparent method, or a sizeable vendor dataset |
| C | Third-party analysis, vendor report or a single corroborating source; always attribute it ("Datadog reports…") |
| D | Recalled, unverified, judgement or a single anecdote |
| E | Speculative, unverifiable or promotional, or nothing found after searching (T1-02 §10.3.1). Never asserted: quote it with attribution and a warning, or report the absence |
| M | Model output (calculations, estimates); it inherits the weakest grade among its inputs |
| P | Practice-curated: standard practice but unmeasured, equivalent to D. Use it for formats and rules of thumb that no session measures |

Compound grades in the findings registry (for example B/C) mean the finding rests on sources of both grades; quote the weaker grade when you rely on the whole finding.

**Other rules:**
- **Dates, not relative time.** Write "as of October 2026"; never "currently", "recently", "nowadays" or "latest" without a date. The validator enforces this outside quotes and code.
- **Volatile facts expire.** EGP-1.0 gives each class of fact a time-to-live, counted from the date the fact was last verified ([T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) §10.6):
  - V0, live status of contested policies and pending rules (visa litigation, enforcement): 14 days;
  - V1, monthly series such as live posting counts and posting indices: 31 days;
  - V2, platform and product facts such as tool and credential statuses, prices and model names: 90 days;
  - V3, market estimates such as pay medians and skill-demand shares: 180 days (this repository re-verifies pay after 90 days);
  - V4, statute and rule text and annual datasets: 365 days; V5, foundations: 1,095 days; V6, dated history: no expiry.
  A page may count from a dataset's own, older date to be conservative; it says so when it does (decision D-018).
- **Cite precisely.** Name the session and, where you can, the line, section or finding ID ([T0-04.F10], T0-13 §4.1, T0-14 L576), or an external source with its date.
- **Grade platform data B.** Levels.fyi, JobsPipe and Fast AI Jobs figures are Grade B (a platform aggregate whose method is taken on trust), even where a session graded them A ([T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) L164; [role catalog §1.3](career/02-roles/role-catalog.md#13-evidence-grades-and-conventions)). Visa wage filings (LCA) are A for what was filed, never for what people earn (decision D-018).
- **Use ranges with reasons** when sources conflict, rather than picking one number.
- **Treat viral statistics sceptically.** Trace them to the original measurement before repeating them.
- **Never invent numbers.** Prefer [P] or "not measured" to a weak citation.
- **Show the decision rule.** Guides say what to do, when, and why, with the evidence one click away.
- **Plain register.** No "definitive", "ultimate", "guarantee" or "top 1%". Say what the evidence supports and stop.
- **Diagrams in mermaid** (GitHub renders them), or as tables. Avoid ASCII art.
- **The legacy handbook is not a source** (decision D-016). An older GenAI career handbook informed some of this repository's formats. Never cite or link it, and never copy a figure from it. The validator rejects references to it and flags its signature phrases.

## 4. The guide pattern

Every new guide (`content_type: guide`) follows this pattern (decision D-016). It puts the action first and the evidence one click away:

```markdown
# <Title>

> <the one promise of this page, matching the front-matter summary>

## The short answer          <!-- 3–6 decision rules, each graded -->
## At a glance               <!-- one mermaid diagram or small table that shows the whole framework -->
## <Named framework>         <!-- the framework, with its parts counted and each part cited -->
## How to do it              <!-- numbered steps, each with a "done when" criterion -->
## Templates and examples    <!-- fill-in blocks; weak → strong pairs; [P] where unmeasured -->
## Checklist                 <!-- GitHub task list: - [ ] … -->
## Pitfalls                  <!-- red flag → why it hurts → fix -->
## Evidence and limits       <!-- what is measured, what is judgement, dates, what would change the advice -->
## Next steps                <!-- the next stage, related guides, role hubs -->
```

Rules for the pattern:
- **Section titles may be specific** ("The 45-minute blueprint" instead of "Named framework"), but keep the order and keep "The short answer", "Checklist", "Evidence and limits" and "Next steps" as written.
- **Templates are fill-in blocks**, with placeholders in square brackets. Mark any template that no session measures as [P].
- **Contrast pairs show weak and strong side by side**: an outreach note, a résumé line, an interview answer.
- **Persona and geography variations** go in their own short subsections, only where the evidence differs.
- **No dead ends.** Every page links onward; the validator rejects pages without a link to another document.
- **The validator enforces the four fixed headings** for every guide, except three that predate the pattern (listed in `LEGACY_GUIDES` in `scripts/validate_docs.py`).

## 5. Generated content

Some documents, or blocks within them, are generated from `data/` by `scripts/`. Generated blocks sit between `BEGIN GENERATED` and `END GENERATED` markers; fully generated files say so in their front matter (`generated_by`) and carry no markers. Edit the data or the generator, never the output.

| Generator | Output |
|---|---|
| `rank_roles.py` | Role-ranking tables |
| `build_index.py` | A–Z title index |
| `build_skills.py` | Skills vocabulary, inventories index, per-role inventories |
| `build_resume_matrix.py` | Concise résumé skills matrix |
| `resume_layers.py` | Job-search strategy computed blocks |
| `target_roles.py` | The GenAI target order: `--update` writes it into the skills ontology; `--check` also verifies the target-roles table |
| `build_role_map.py` | The role map (`career/02-roles/role-map.md`) |
| `build_role_hubs.py` | One hub per role (`career/02-roles/hubs/`) |
| `build_skills_views.py` | The skills radar and credentials by role |
| `build_archetypes.py` | Project archetypes (`career/05-portfolio/project-archetypes.md`) |
| `build_prompts.py` | Interview prep packs (`career/08-interviewing/prep-packs.md`) |
| `build_tool_catalog.py` | The tool catalog (`career/00-start/tool-catalog.md`) |
| `build_findings.py` | Findings registry |
| `build_manifest.py` | `llms.txt`, `data/manifest.json` |

Every generator supports `--check`. [scripts/README.md](scripts/README.md) lists what each one reads; `scripts/gap_analysis.py` is a personal tool that writes nothing to the repository.

## 6. Before you finish

1. Update `last_verified` (and `review_by`, where the page has volatile facts) in the front matter of every document whose facts you changed or re-checked. Do this first: the manifest copies these fields.
2. Run the generators you affected, then `python3 -B scripts/build_manifest.py --update`.
3. Run `python3 -B scripts/validate_docs.py`. It checks links, anchors, tables, front matter, writing rules, dead ends, the guide pattern, every generated output, the stack model, cross-file ranks and corpus coverage, and must print `PROBLEMS: 0`. It also lists documents due for re-verification. CI runs the same check on every push and pull request. While drafting, `python3 -B scripts/validate_docs.py --files <path>` checks one document.
4. For a new or substantially revised guide, have someone other than the author check every figure against the line it cites, and fix or relabel what no source supports (decision D-018). Record open problems in [ROADMAP.md](ROADMAP.md) §7.
5. Add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

**Scripts:** standard library only; run them with `python3 -B` so that no `__pycache__` is left behind.

## 7. Versioning and releases

The repository follows [Semantic Versioning](https://semver.org/) with git tags. Documents carry no version number; each one has `last_verified` and `status` instead (decision D-014).

| Change | Version bump |
|---|---|
| Corrections, refreshed evidence, small additions | Patch (0.1.0 → 0.1.1) |
| A ROADMAP milestone, or a change to paths, document IDs, skill IDs or a data schema | Minor while below 1.0 (0.1.x → 0.2.0) |
| From 1.0 on, a change to paths, IDs or schemas that breaks readers or scripts | Major |

**1.0.0** comes when every lifecycle stage has its core guide (ROADMAP phase 3), paths, IDs and schemas are declared stable, and the reference documents have had an independent fact-check.

**To release:**
1. Move the entries under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) to a new `## [x.y.z] - YYYY-MM-DD` section.
2. Commit, then tag and push: `git tag -a vx.y.z -m "vx.y.z"` and `git push origin vx.y.z`.

**History is append-only.** Published commits are never rewritten. Corrections go forward: errors in research records to [research/ERRATA.md](research/ERRATA.md), everything else to the changelog.

**Data files** version their own format (`schema: <name>/<major.minor>`). Bump the major number only for a change that breaks readers of the file.
