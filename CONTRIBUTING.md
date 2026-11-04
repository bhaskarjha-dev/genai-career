# Contributing

This repository aims to be the most accurate, best-organised source on GenAI careers, for people and for AI agents. These conventions keep it that way. AI agents should also read [AGENTS.md](AGENTS.md).

## 1. Where things go

| You are adding… | Put it in | And |
|---|---|---|
| A guide, reference or tool for one lifecycle stage | `career/NN-stage/` (kebab-case file name) | List it in that folder's `README.md`; move its row out of "Planned" |
| A cross-cutting playbook for a background, location or working model | `career/11-tracks/` | Same |
| Structured data that documents are built from | `data/` (snake_case), with a schema in `data/schemas/` when the structure matters | Add a generator in `scripts/` rather than hand-copying values into documents |
| New research | `research/sessions/` as a new session (see [research/README.md](research/README.md)) | Run `python3 scripts/build_findings.py --update` |
| A correction to a Phase 0 record | `research/ERRATA.md` | Fix the affected career documents |
| An architectural decision | Append to `research/DECISIONS.md` | Reference it in [CHANGELOG.md](CHANGELOG.md) |

The lifecycle stages are: 01 landscape, 02 roles, 03 skills and technology, 04 certifications, 05 portfolio, 06 job search, 07 networking, 08 interviewing, 09 compensation, 10 onboarding, 11 tracks. Reference material sits in the stage where it is used.

## 2. Front matter

Every document under `career/`, and the research index pages, starts with YAML front matter. The schema is [data/schemas/frontmatter.schema.json](data/schemas/frontmatter.schema.json).

```yaml
---
id: job-search.ats-mechanics       # unique, dotted, lowercase
title: "ATS Mechanics: How Screening Works"
content_type: guide                # index | guide | reference | method
stage: 6                           # 0 = cross-stage; must match the folder number
status: draft                      # planned | draft | published | stale
last_verified: 2026-11-04
summary: "One sentence, 20-320 characters: what the reader gets."
sources: [T0-04, T0-10]            # research sessions relied on
roles: [all]                       # optional: role slugs
geos: [global, india]              # optional
tags: [ats, resume]                # optional
generated_by: scripts/x.py         # only for generated files
---
```

`scripts/build_manifest.py` turns front matter into [llms.txt](llms.txt) and [data/manifest.json](data/manifest.json). Run it with `--update` after adding or retitling a document.

## 3. Writing standard (EGP-1.0 in brief)

The full protocol is [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md) (decision D-012).

**Grade every empirical claim:**

| Grade | Meaning |
|---|---|
| A | Primary authoritative source: official documentation, government filings, peer-reviewed research, measured data |
| B | Established secondary source with a transparent method, or a sizeable vendor dataset |
| C | Third-party analysis, vendor report or a single corroborating source; always attribute it ("Datadog reports…") |
| D | Recalled, unverified, judgement or a single anecdote |
| E | No evidence found after searching |
| M | Model output (calculations, estimates); it inherits the weakest grade among its inputs |
| P | Practice-curated (in the skills data): standard for the role but unmeasured, equivalent to D |

**Other rules:**
- **Dates, not relative time.** Write "as of October 2026"; never "now", "currently", "recently" or "latest". Volatile facts carry re-verification dates: tool statuses 90 days, pay figures 90 days, visa and regulatory status 14–31 days.
- **Cite precisely.** Name the session (T0-03) and, where you can, the line or section, or an external source with its date.
- **Use ranges with reasons** when sources conflict, rather than picking one number.
- **Treat viral statistics sceptically.** Trace them to the original measurement before repeating them.
- **Never invent numbers.** Prefer [P] or "not measured" to a weak citation.
- **Show the decision rule.** Guides say what to do, when, and why, with the evidence one click away.

## 4. Generated content

Some documents, or blocks within them, are generated from `data/` by `scripts/`. Generated blocks sit between `BEGIN GENERATED` and `END GENERATED` markers; fully generated files say so in their front matter (`generated_by`). Edit the data or the generator, never the output.

| Generator | Output |
|---|---|
| `rank_roles.py` | Role-ranking tables |
| `build_index.py` | A–Z title index |
| `build_skills.py` | Skills vocabulary, inventories index, per-role inventories |
| `build_resume_matrix.py` | Concise resume skills matrix |
| `resume_layers.py` | Job-search strategy computed blocks |
| `build_findings.py` | Findings registry |
| `build_manifest.py` | `llms.txt`, `data/manifest.json` |
| `target_roles.py` | Prints the GenAI target-order analysis (no files) |

Every generator supports `--check`.

## 5. Before you finish

1. Run the generators you affected.
2. Run `python3 scripts/validate_docs.py`. It checks links, anchors, tables, front matter, every generated output, cross-file ranks and corpus coverage, and must print `PROBLEMS: 0`. CI runs the same check on every push and pull request.
3. Add an entry to [CHANGELOG.md](CHANGELOG.md), and bump the `version` and `last_verified` in the front matter of the documents you changed.

**Scripts:** standard library only; run them with `python3 -B` so that no `__pycache__` is left behind.
