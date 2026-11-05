---
id: skills.method
title: "Skills Ontology: Requirements, Design, Build and Maintenance"
content_type: method
stage: 3
status: published
last_verified: 2026-11-04
summary: "Requirements, design, build, verification and maintenance of the skills ontology that generates the vocabulary, the role inventories and the resume matrix."
sources: [T0-03, T0-04, T0-06, T0-11, T0-13, T1-02, T1-03]
---
# Skills Ontology: Requirements, Design, Build and Maintenance
## Why the Skills Layer Is Shaped the Way It Is, How It Was Built and Verified, and How to Keep It Accurate

> **Updated:** 2026-11-04 · **Scope:** Methodological architecture of the typed GenAI skills ontology.
> **What this covers:** the method behind [data/skills_ontology.json](../../data/skills_ontology.json) and the documents generated from it:
> - [skills-vocabulary.md](skills-vocabulary.md);
> - [role-skill-inventories.md](role-skill-inventories.md) and the [inventories/](inventories/) files;
> - [resume-skills-matrix.md](../06-job-search/resume-skills-matrix.md).
>
> **Evidence:** EGP-1.0 grades: A/B measured; C small-sample, vendor or practitioner; D judgement; M model output.

---

## 1. What a Resume Needs From the Skills Layer

A resume can only be as good as its skills input. The ontology was designed against ten requirements:

| # | Requirement | Why | Evidence | How the ontology meets it |
|---|---|---|---|---|
| R1 | Exact names of tools, frameworks and platforms | Recruiter searches key on titles, languages and frameworks; AI screening extracts canonical skill names | C · [T0-11](../../research/sessions/T0-11-certification-cloud-credential-roi.md); A · [T0-04](../../research/sessions/T0-04-ats-filtering-funnel-conversion-math.md) | 274 concrete entries across 11 concrete types, unbundled |
| R2 | Concept phrases (RAG, LLM evaluation, agents) | Screening criteria and human readers judge capability | A · T0-04 | Concept and method entries, with sub-concepts linked to their parents |
| R3 | Tool ↔ concept links and groups of alternatives | Turns "used Qdrant" into "vector search"; handles "LangGraph or similar" | D | `implements` links; choose-one classes such as vector stores and tracing products |
| R4 | Aliases and posting wording | "evals" vs "LLM evaluation"; "GenAI" vs "generative AI" | B · JobsPipe terms | `aliases` on every entry; each role file lists keywords to mirror |
| R5 | Priority per role, Must → Optional | Fills a limited skills section | — | Five tiers: Must, Important, Should, Optional, Avoid |
| R6 | Status and freshness of each tool | Don't list archived or dormant tools such as TGI, RAGAS or AutoGen | A/B · [T0-03](../../research/sessions/T0-03-skills-compute-infra-eval-stack.md) | Dated `status`; archived, dormant and retired items are always tiered Avoid |
| R7 | Non-technical skills, shown rather than listed | Postings measure them, interviews probe them, and a behavioural "No Hire" is a near-veto | B · JobsPipe; B/C · [T1-03](../../research/sessions/T1-03-interview-execution-offer-negotiation.md) | Six non-technical types, present in every role inventory |
| R8 | How to evidence each skill | Unbacked skills are discounted; AI review cites evidence per requirement | A · T0-04; [T0-13](../../research/sessions/T0-13-production-portfolio-proof-of-work-standards.md) | A resume pattern per type; the V0–V3 verifiability ladder |
| R9 | A proficiency scale | Gap analysis and honest claims | [T0-06](../../research/sessions/T0-06-career-transition-timelines-5-backgrounds.md) D9 | The 0–3 scale; self-assessment tables in every role file |
| R10 | Credentials and prerequisites kept apart from skills | They are facts, not skills | T0-11; T0-04 | Separate `credentials` entries; prerequisites and proof kept as role facts |

---

## 2. Design

**Types.** The first-principles split is technical vs non-technical, and within technical, concrete tools vs knowledge areas. The ontology extends it to 19 types in three groups:

| Group | Types |
|---|---|
| Technical: knowledge | Concept / knowledge area · Method / practice |
| Technical: concrete | Programming language · Framework / SDK · Library / package · Model / model family · Platform / cloud service · Data store · Infrastructure / DevOps tool · Specialised product · Hardware / accelerator · Protocol / standard · Regulation / framework |
| Non-technical | Communication & collaboration · Behavioural competency · Business & product · Leadership & people · Domain knowledge · Research craft |

[skills-vocabulary.md](skills-vocabulary.md) §0 defines each type, where it goes on a resume and how the relations read.

**Relations:**
- **implements:** a tool realises a concept;
- **parent:** a sub-concept sits under a broader one;
- **choose-one classes:** any member satisfies a class link, and a link can require *n* members;
- **aliases:** the wording postings use.

**Role links.** Each role link carries a tier (M, I, S, O, X) and one of four evidence classes:

| Evidence | Meaning | Grade |
|---|---|:---:|
| JD | Share of live postings for the title, or for a labelled feeder or adjacent title (JobsPipe, retrieved 2026-11-02) | B |
| S09 | Share of the 3,647-posting S09 corpus (T0-03 §6.3) | B |
| S | Named for the role in a research session; the ontology stores the exact session lines | A–C |
| P | Practice-curated: standard for the role, but not evidenced in the corpus | D |

**Tier rule.** Where a measured share exists, the tier follows it:
- about 50% or more is Must;
- 20–50% is Important;
- lower is Should or Optional.

A role-defining skill can depart from the rule, and the link's note says why.

**Two layers for resumes:**
- The *headline* layer: the concise skills-section phrases in the resume matrix, including classes such as "AWS / Azure / GCP".
- The *full inventory*: every typed entry.

Both are projections of the same links, so they cannot disagree.

---

## 3. Data, Scripts and How to Edit

| File | Role |
|---|---|
| [data/skills_ontology.json](../../data/skills_ontology.json) | The single source: skills, classes, credentials, resume variants, role links, tier changes, verification summary |
| [data/skills_ontology.schema.json](../../data/schemas/skills_ontology.schema.json) | JSON Schema for the ontology |
| [data/project_archetypes.json](../../data/project_archetypes.json) | Proof-of-work archetypes used by the [job-search blueprint](../06-job-search/job-search-strategy.md) |
| [scripts/build_skills.py](../../scripts/build_skills.py) | Validates the ontology (schema plus rules) and regenerates the vocabulary, the inventories index and the 26 role files |
| [scripts/build_resume_matrix.py](../../scripts/build_resume_matrix.py) | Regenerates the concise resume matrix from the headline layer |
| [scripts/resume_layers.py](../../scripts/resume_layers.py) | Recomputes the blueprint's resume-layer and proof-of-work figures |
| [scripts/validate_docs.py](../../scripts/validate_docs.py) | Checks the whole `career/` doc set: links, anchors, tables, every generated block, cross-file ranks and corpus coverage |

**Rules the validator enforces** (beyond the schema):
- every ID resolves;
- `implements` and `parent` point at concepts or methods;
- every S link cites a real session line;
- JD and S09 links carry a share and a source;
- dead tools and credentials are tiered Avoid;
- every role covers all 19 types or says why a type does not apply, and has at least one Must, one communication and one behavioural link.

**To change something:**
1. Edit `skills_ontology.json`. Add a skill with a type, category and aliases, or add a role link with a tier and evidence.
   - Record every tier change to a headline skill in `changes`, with a reason.
   - Never cite a session line that does not support the claim. Use P when the corpus is silent.
2. Run `python3 scripts/build_skills.py --update`, `python3 scripts/build_resume_matrix.py --update` and `python3 scripts/resume_layers.py --update`.
3. Run `python3 scripts/validate_docs.py`. It must report 0 problems.

---

## 4. How the Foundation Ontology Was Built (2026-11-04)

1. **Vocabulary.**
   - The 138 skills of the initial headline matrix were typed.
   - Their bundles were split: interchangeable tools became choose-one classes, and complementary tools became concepts implemented by individual tools.
   - Added to them:
     - every technology named in the research sessions or the skills catalog;
     - the JobsPipe skill terms that had no match;
     - the T1-03 behavioural competencies C1–C4;
     - common practice-curated tools.
   - The result: 523 entries.
2. **Assignment.**
   - Each role inventory was written from the role's fact-checked map in [role-skill-maps.md](role-skill-maps.md) §3 and the initial headline tiers.
   - Tiers follow measured shares where they exist.
   - 28 headline tiers changed, each with its reason. They are listed in [role-skill-inventories.md](role-skill-inventories.md) §3.
3. **Evidence and verification.**
   - Every S link was resolved to an exact session line that names the item.
   - Candidate lines were scored for role relevance: a role keyword on or near the line, terms from the note, and table or bullet rows.
   - Weak knowledge-skill citations at Should or Optional were downgraded to P.
   - All JD shares were matched to their title's row in the catalog's §2.1, and all S09 shares to §2.2.
   - Low-relevance lines and a random sample were read by hand and corrected.
   - The summary is in [role-skill-inventories.md](role-skill-inventories.md) §4.

**Limits:**
- **No independent agent fact-check.** It was planned but blocked by the model quota, so a few keyword-matched citations may be weaker than a close reading would accept.
- **Many tool tiers are not measured.** Outside the measured titles they rest on session mentions and practice curation (§5).

---

## 5. Coverage Checks

The checks from the 2026-11-04 skills audit, as the ontology meets them:

| Check | Result |
|---|---|
| Concrete technologies | 274 concrete entries, unbundled; 205 are named in the research |
| Corpus technologies with a typed entry | All of the audit list; the validator enforces it |
| JobsPipe skill terms | All 114 typed |
| Roles with at least one non-technical skill | All 26 |
| Type, relations, aliases, status | On every entry |
| Skills per role | 41–148 |

---

## 6. Maintenance

- **Tool statuses** are class V2 facts under EGP-1.0. Re-verify them within 90 days of 2026-10-23, so by 2027-01-21, then regenerate.
- **Job-description mining** is the next research step. It measures tool tiers and tests completeness:
  1. Sample 30 or more dated postings per role from public ATS boards (Greenhouse, Lever, Ashby) and career pages.
  2. Extract the skills with model assistance and human checks.
  3. Accept an inventory as complete only when at least 95% of the skills those postings name are in it, under a canonical name or an alias.
  4. Promote measured items from S or P to JD.
- **The practice-curated share is highest** for Physical AI, the leadership tracks, Research Scientist, Domain Evaluation and AI Enablement. Mine those roles first.
