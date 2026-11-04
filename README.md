# GenAI Career Intelligence System

> Evidence-grounded career intelligence for Generative AI, ML systems and applied AI engineering, from entry level to frontier-lab roles, across geographies. Every claim is graded, dated and traceable to its source.

---

## What this is

A structured knowledge repository that treats AI career navigation as an intelligence problem.
- **What it covers:** the full lifecycle, from understanding which roles exist and what they pay, through skills, proof of work, job search, interviewing and negotiation, to the first 90 days.
- **How it is organised:** content follows a lifecycle spine. Each role, skill and claim links back to the research that supports it.

**Who it serves:** anyone navigating a GenAI career, for example:
- fresh graduates choosing a first role;
- engineers moving from adjacent fields;
- researchers moving to industry;
- product, governance and domain experts entering AI work;
- India-based professionals working across borders;
- independent practitioners.

It is written to be equally usable by **people** (readable Markdown on GitHub) and by **AI agents** (front matter on every document, machine-readable data, generated indexes, explicit evidence grades). Read the vision, scope and constraints in [CHARTER.md](CHARTER.md).

## Start here

| I want to… | Go to |
|---|---|
| Find my way around the career content | **[career/README.md](career/README.md): Start Here** |
| See which GenAI roles exist and which are best | [Role catalog](career/02-roles/role-catalog.md) · [Role rankings](career/02-roles/role-rankings.md) · [GenAI target roles](career/02-roles/genai-target-roles.md) |
| Know everything a role needs, with priority and evidence | [Role skill inventories](career/03-skills-and-tech/role-skill-inventories.md) |
| Plan a job search and resumes for several roles | [Job-search strategy](career/06-job-search/job-search-strategy.md) · [Resume strategy](career/06-job-search/resume-strategy.md) |
| See what the research found, by topic | [Findings registry](research/findings.md) (262 graded findings from 22 sessions) |
| Know what is covered and what comes next | [ROADMAP.md](ROADMAP.md) |

## What's inside

| Folder or file | Layer | Contents |
|---|---|---|
| [career/](career/README.md) | Reference and guidance | User-facing content in lifecycle stages `01-landscape` … `11-tracks`; each folder has a README index |
| [research/](research/README.md) | Evidence and knowledge | 22 dated research sessions (immutable), the findings registry, errata, the decision registry, the Founding Architecture Document and the pipeline specification |
| [data/](data/) | Sources of truth | Role scores, the skills ontology, project archetypes, findings, the document manifest, and JSON Schemas |
| [scripts/](scripts/) | Machinery | Generators (`--update` / `--check`) and `validate_docs.py` |
| [ROADMAP.md](ROADMAP.md) · [CHANGELOG.md](CHANGELOG.md) | Meta | Coverage, plans and open decisions; history of changes |
| [AGENTS.md](AGENTS.md) · [llms.txt](llms.txt) | For AI | Rules for agents; an LLM index of every document |
| [CONTRIBUTING.md](CONTRIBUTING.md) | For contributors | Placement, front matter, writing standard, generated content, validation |

## Status

- **Phase 0 (research)** is complete: 22 sessions, the Founding Architecture Document, and 12 locked decisions.
- **Phase 1 (content)** has:
  - delivered the role catalogs, rankings, target order, skills ontology and role inventories, and the job-search and resume strategy;
  - put the architecture-v2 foundation in place: the stage spine, front matter, data layer, AI indexes, findings registry and CI.
- **The remaining stages** have their research in place, with guides planned. See [ROADMAP.md](ROADMAP.md).

## Evidence standard

All content follows the Evidence-Grounding Protocol (EGP-1.0; [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md), decision D-012):

| Grade | Meaning |
|---|---|
| **A** | Primary authoritative source: official documentation, government filings, peer-reviewed research |
| **B** | Established secondary source with a transparent method |
| **C** | Third-party analysis, vendor report or a single corroborating source |
| **D** | Recalled from memory, unverified, or a single anecdote |
| **E** | No evidence found after searching |
| **M** | Model output (calculations, estimates); it inherits the weakest grade among its inputs |

**Other rules:**
- Every factual claim cites its source and grade, or is flagged `[UNVERIFIED]`.
- Volatile facts carry re-verification dates.
- Known errors in the Phase 0 records are listed in [research/ERRATA.md](research/ERRATA.md).

## Contributing and validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) (people) or [AGENTS.md](AGENTS.md) (AI agents). Before finishing any change, run:

```bash
python3 scripts/validate_docs.py     # must print PROBLEMS: 0; CI runs it on every push
```

## Research methodology

The research pipeline uses the [Vivechak](research/RESEARCH-PIPELINE.md) research-governance framework: parallel, independent, evidence-grounded sessions with explicit priors, graded findings, source ledgers and belief-change deltas. Its outputs are indexed in [research/README.md](research/README.md).

## License

This work is licensed under [CC-BY-SA-4.0](LICENSE). See the [CHARTER.md](CHARTER.md) disclaimer about tax, legal and financial content.

---

*Temporal anchor: October 2026 (research). Maintained under the Vivechak research-governance framework.*
