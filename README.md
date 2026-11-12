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
| Find my way around the career content, by situation or by question | **[career/README.md](career/README.md): Start Here** |
| See where each GenAI role's work sits, from GPUs to applications | [Role map](career/02-roles/role-map.md) · [Role hubs](career/02-roles/hubs/README.md) (one page per role) |
| See which GenAI roles to target, then the evidence | [GenAI target roles](career/02-roles/genai-target-roles.md) → [role hubs](career/02-roles/hubs/README.md) → [role catalog](career/02-roles/role-catalog.md) and [role rankings](career/02-roles/role-rankings.md) (all demand) |
| Choose my targets and plan the next 90 days | [Targeting workbook](career/00-start/targeting-workbook.md) |
| Know everything a role needs, with priority and evidence | [Role skill inventories](career/03-skills-and-tech/role-skill-inventories.md) · [Skills radar](career/03-skills-and-tech/skills-radar.md) |
| Build proof of work that hiring teams believe | [Proof-of-work standards](career/05-portfolio/proof-of-work-standards.md) · [Project archetypes](career/05-portfolio/project-archetypes.md) |
| Plan a job search and résumés for several roles | [Job-search strategy](career/06-job-search/job-search-strategy.md) · [Résumé strategy](career/06-job-search/resume-strategy.md) · [Referrals and outreach](career/07-networking/referrals-and-outreach.md) |
| Prepare for interviews | [Interview loops](career/08-interviewing/interview-loops.md) · [Prep packs](career/08-interviewing/prep-packs.md) |
| Evaluate and negotiate an offer | [Offer evaluation](career/09-compensation/offer-evaluation.md) · [Negotiation playbook](career/09-compensation/negotiation-playbook.md) |
| See what the research found, by topic | [Findings registry](research/findings.md) (graded findings from 24 sessions) |
| Know what is covered and what comes next | [ROADMAP.md](ROADMAP.md) |

## What's inside

| Folder or file | Layer | Contents |
|---|---|---|
| [career/](career/README.md) | Reference and guidance | User-facing content: start-here tools in `00-start` and the lifecycle stages `01-landscape` … `11-tracks`; each folder has a README index |
| [research/](research/README.md) | Evidence and knowledge | 24 dated research sessions (immutable), the findings registry, errata, the decision registry, the Founding Architecture Document, the Phase 0 pipeline specification and [research pipeline 2](research/pipeline-2/README.md) (53 planned sessions) |
| [data/](data/README.md) | Sources of truth | Role facts and scores, role titles, the skills ontology, posting-term snapshots, the stack model, project archetypes, interview prompts, tools, findings, the document manifest, and JSON Schemas |
| [scripts/](scripts/README.md) | Machinery | Generators (`--update` / `--check`) run by `build_all.py`, `validate_docs.py`, tests, and a personal gap-analysis tool |
| [ROADMAP.md](ROADMAP.md) · [CHANGELOG.md](CHANGELOG.md) | Meta | Coverage, plans and open decisions; history of changes |
| [AGENTS.md](AGENTS.md) · [llms.txt](llms.txt) | For AI | Rules for agents; an LLM index of every document |
| [CONTRIBUTING.md](CONTRIBUTING.md) | For contributors | Placement, front matter, writing standard, the guide pattern, generated content, validation |

## Status

- **Phase 0 (research)** is complete: 22 sessions, the Founding Architecture Document, and 12 locked decisions. Two additional sessions (T3-01 and T3-02, November 2026) deepen the certification evidence with independent cross-check analyses.
- **Phase 1 (content)** has:
  - delivered the role catalogs, rankings, target order, skills ontology and role inventories, and the job-search and resume strategy;
  - put the architecture-v2 foundation in place: the stage spine, front matter, data layer, AI indexes, findings registry and CI;
  - added the role map and one hub per role, and the core guides for every lifecycle stage, from the market overview to growth after the first 90 days, with track playbooks.
- **What remains:** research the corpus does not yet hold, planned as the 53 sessions of [research pipeline 2](research/pipeline-2/README.md) (networking, résumés, job search, certifications, countries and visas, pay, interviews and every role), an independent fact-check of the v0.1.0 reference documents and a human expert review of the guides, and the known issues listed in [ROADMAP.md](ROADMAP.md) §7.

## Evidence standard

All content follows the Evidence-Grounding Protocol (EGP-1.0; [T1-02](research/sessions/T1-02-evidence-grounding-protocol.md), decision D-012). Every empirical claim carries a grade, from A (primary or measured) to E (speculative, never asserted), plus M for model output and P for practice-curated; the definitions are in [CONTRIBUTING.md §3](CONTRIBUTING.md#3-writing-standard-egp-10-in-brief).

**Other rules:**
- Every factual claim cites its source and grade, or is flagged `[UNVERIFIED]`.
- Volatile facts carry re-verification dates; pages that state them carry a `review_by` date, the validator lists pages that are due, and a weekly CI run fails while any page is due.
- Each fact that several pages need has one owner; the other pages link it (decision D-019).
- Known errors in the Phase 0 records are listed in [research/ERRATA.md](research/ERRATA.md).

## Contributing and validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) (people) or [AGENTS.md](AGENTS.md) (AI agents). Before finishing any change, run:

```bash
python3 -B scripts/build_all.py                       # regenerate everything, then validate: must print PROBLEMS: 0
python3 -B -m unittest discover -s scripts/tests      # if you changed a script; CI runs both on every push
```

## Research methodology

The research pipeline uses the [Vivechak](research/RESEARCH-PIPELINE.md) research-governance framework: parallel, independent, evidence-grounded sessions with explicit priors, graded findings, source ledgers and belief-change deltas. Its outputs are indexed in [research/README.md](research/README.md). The second pipeline, [research pipeline 2](research/pipeline-2/README.md), keeps Vivechak's prompt discipline and designs each session backwards from the data and pages it feeds (decision D-021).

## License

This work is licensed under [CC-BY-SA-4.0](LICENSE). See the [CHARTER.md](CHARTER.md) disclaimer about tax, legal and financial content.

---

*Temporal anchor: October 2026 (research). Maintained under the Vivechak research-governance framework.*
