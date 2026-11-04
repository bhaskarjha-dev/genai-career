# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-11-04

### Added
- **Evidence Base (Phase 0):** 22 empirical research sessions across Layer 0 (landscape), Layer 1 (blueprints), and Layer 2 (tier playbooks), adhering to the Evidence-Grounding Protocol (EGP-1.0).
- **Founding Architecture & Governance:** Founding Architecture Document (FAD), decision registry (D-001 through D-014), and project charter.
- **Role Master Catalog & Rankings:**
  - 29 canonical GenAI roles classified and de-duplicated across 241 title strings with an automated A–Z index generator (`scripts/build_index.py`).
  - Evidence-weighted Composite Career Index (CCI) scoring and rankings with uncertainty intervals and Monte Carlo simulation (`scripts/rank_roles.py`).
  - GenAI target-role consensus shortlist (`career/02-roles/genai-target-roles.md`, `scripts/target_roles.py`).
- **Skills Ontology & Inventories:**
  - Single source of truth in `data/skills_ontology.json` (523 typed skills across 19 categories, 35 choose-one classes, 20 credentials, 15 resume variants, and 1,529 evidence-linked role connections).
  - Generators for skills vocabulary, inventories index, and 26 comprehensive role skill inventories (`scripts/build_skills.py`).
  - Per-role skill maps covering table-stakes, differentiating, and frontier skills (`career/03-skills-and-tech/role-skill-maps.md`).
- **Job Search & Resume Strategy:**
  - Layered resume strategy (L0 master -> L1 universal -> L2 family -> L3 role -> L4 posting-tailored).
  - Programmatic resume skills matrix derived from ontology headline skills (`scripts/build_resume_matrix.py`).
  - 20 proof-of-work project archetypes with optimal coverage sets (`data/project_archetypes.json`, `scripts/resume_layers.py`).
- **Findings Registry & AI Discoverability:**
  - Extraction of 262 key findings into `data/findings.json` and `research/findings.md` (`scripts/build_findings.py`).
  - Agent governance rules in `AGENTS.md`.
  - Machine-readable manifest and AI index generated via `scripts/build_manifest.py` (`data/manifest.json`, `llms.txt`).
- **Automation & Quality Assurance:**
  - Complete CI validation pipeline (`scripts/validate_docs.py`, `.github/workflows/validate.yml`) verifying relative links, anchor targets, table layouts, JSON schemas, front matter compliance, and generator parity.
