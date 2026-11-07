#!/usr/bin/env python3
"""Documentation validator for the career catalogs.

Checks, across every career/*.md file, the generated role inventories and README.md:
  * relative links resolve to existing files and anchors; no absolute file:// links;
    no duplicate anchors; no leftover template placeholders
  * every Markdown table row has the same number of cells as its header
  * every generated block is current: rank_roles.py, build_index.py, build_skills.py, build_resume_matrix.py,
    resume_layers.py, build_findings.py, target_roles.py, build_role_map.py, build_role_hubs.py,
    build_skills_views.py, build_archetypes.py, build_prompts.py, build_tool_catalog.py and build_manifest.py
    are each run with --check
  * ranks agree across the master catalog, the skills catalog, the ranked catalog's
    dossiers and scripts/rank_roles.py
  * every career/ document and research index page carries valid front matter
    (data/schemas/frontmatter.schema.json), with a unique id and a stage that matches its folder
  * the skills ontology covers exactly the individual-contributor roles of role_scores.json
  * corpus coverage: every technology named in the research sessions or the skills catalog
    (the 2026-11-04 audit list below) resolves to a typed vocabulary entry
  * the stack model (data/stack_model.json) and every role's work footprint are consistent (decision D-015)
  * writing rules (EGP-1.0 and D-016): no relative-time words outside quotes and code ("currently",
    "recently", "nowadays", "these days", "as of now", "right now", "at present", "at the moment", or
    "latest" without a date nearby); no references to the legacy handbook (once kept in the git-ignored temp/
    folder), and none of its signature phrases outside quotes and code, in the documents and in data/*.json
  * no dead ends: every document under career/ links to at least one other document
  * the guide pattern (D-016): every guide has "The short answer", "Checklist", "Evidence and limits" and
    "Next steps", in that order (three guides that predate the pattern are listed in LEGACY_GUIDES)
  * freshness: documents whose front matter `review_by` date has passed are listed as DUE
    (reported, not counted as problems unless --strict)

Usage:
    python3 scripts/validate_docs.py                  # prints PROBLEMS: <n> and the list; exit 1 if any
    python3 scripts/validate_docs.py --strict         # also counts DUE documents as problems
    python3 scripts/validate_docs.py --files A.md B.md  # document-level checks for the named files only

Standard library only.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
CAREER = ROOT / "career"
sys.path.insert(0, str(SCRIPTS))
import rank_roles as rr  # noqa: E402
from build_manifest import parse_front_matter  # noqa: E402
from build_skills import schema_errors  # noqa: E402
import stack_lib  # noqa: E402

SEALED = {"FAD.md", "DECISIONS.md", "RESEARCH-PIPELINE.md"}  # Phase 0 records: checked by hand, not linted here
FILES = (sorted(CAREER.rglob("*.md")) + sorted(ROOT.glob("*.md"))
         + sorted(p for p in (ROOT / "research").glob("*.md") if p.name not in SEALED)
         + [p for p in [ROOT / "llms.txt", ROOT / "data" / "README.md", ROOT / "scripts" / "README.md"] if p.exists()])
GENERATORS = ["rank_roles.py", "build_index.py", "build_skills.py", "build_resume_matrix.py", "resume_layers.py",
              "build_findings.py", "target_roles.py", "build_role_map.py", "build_role_hubs.py", "build_skills_views.py",
              "build_archetypes.py", "build_prompts.py", "build_tool_catalog.py", "build_manifest.py"]
RELATIVE_TIME = re.compile(r"\b(currently|recently|nowadays|these days|as of now|right now|at present|at the moment)\b"
                           r"|\blatest\b(?![^\n]{0,40}\d{4}(-\d{2}){0,2})", re.I)
LEGACY = re.compile(r"old-genai-career|temp/old")
# Signature phrases of the legacy handbook (decision D-016). A final scan on 2026-11-07 compared the handbook with this
# repository and found no figure or prose from it that is not also in the research records; these phrases keep a leak
# check running after the handbook is deleted.
LEGACY_PHRASES = re.compile(r"\b54 roles\b|\b(?:7|seven) (?:macro )?clusters\b|\b6-layer AI stack\b|\bTier-1 projects?\b|"
                            r"\bTalent Bridge Matrix\b|300% year-over-year", re.I)
LEGACY_EXEMPT = {"AGENTS.md", "CONTRIBUTING.md", "CHANGELOG.md"}  # they state the rules, so they may name what is banned
LEGACY_PHRASES_SKIP = {"research/findings.md"}  # generated from the sealed sessions, so it cannot be edited to comply
FRONT_MATTER_PAGES = ["research/README.md", "research/findings.md", "research/ERRATA.md"]
GUIDE_HEADINGS = ["The short answer", "Checklist", "Evidence and limits", "Next steps"]
# Guides written before the guide pattern was adopted (D-016, 2026-11-05); migrate each when it is next revised.
LEGACY_GUIDES = {"career/02-roles/genai-target-roles.md", "career/06-job-search/job-search-strategy.md",
                 "career/06-job-search/resume-strategy.md"}

# Technologies named in the research sessions or the skills catalog (skills audit, 2026-11-04).
TECH = """Python TypeScript JavaScript C++ Rust Go Java SQL CUDA Scala
LangChain LangGraph LlamaIndex Haystack DSPy Semantic Kernel AutoGen CrewAI OpenAI Agents SDK Claude Agent SDK Pydantic AI
Microsoft Agent Framework ADK smolagents Mastra Vercel AI SDK CopilotKit
FastAPI Flask Django Next.js React Node.js Streamlit Gradio
PyTorch TensorFlow JAX Keras scikit-learn XGBoost Transformers PEFT TRL Accelerate DeepSpeed Megatron FSDP Unsloth Axolotl
LlamaFactory verl OpenRLHF sentence-transformers spaCy NumPy pandas Polars Ray Spark
vLLM SGLang TensorRT-LLM TGI Triton Inference Server Dynamo llm-d LMCache Mooncake FlashInfer FlashAttention ONNX llama.cpp
Ollama KServe Ray Serve BentoML NIM CUTLASS CuTe Helion CuteDSL XLA TorchInductor ROCm HIP NCCL Nsight
pgvector Pinecone Weaviate Qdrant Milvus Chroma FAISS Elasticsearch OpenSearch Redis PostgreSQL MongoDB Neo4j Snowflake
BigQuery Databricks Kafka Langfuse LangSmith Arize Phoenix Braintrust Helicone OpenTelemetry Datadog Prometheus Grafana
W&B MLflow DeepEval Promptfoo RAGAS TruLens Inspect Giskard LiteLLM MCP A2A AG-UI FastMCP OAuth OIDC JSON Schema
OpenAPI gRPC Temporal Celery Airflow Kubeflow Bedrock SageMaker Lambda Azure OpenAI AI Foundry Vertex AI Cloud Run
Hugging Face Modal Replicate Together AI Fireworks Anyscale Baseten Docker Kubernetes Terraform Helm GitHub Actions SLURM
InfiniBand RDMA NeMo Guardrails Guardrails AI Llama Guard Presidio OWASP OneTrust Credo AI Holistic AI OpenPages Fairlearn
SHAP LIME Captum AIF360 C2PA EU AI Act NIST AI RMF ISO 42001 SR 26-2 LL144 DPDP GDPR ROS Isaac MuJoCo WebGPU
Transformers.js WebMCP Instructor Outlines Unstructured Cohere"""
MULTI_WORD = ['Semantic Kernel', 'OpenAI Agents SDK', 'Claude Agent SDK', 'Pydantic AI', 'Microsoft Agent Framework', 'Vercel AI SDK', 'Triton Inference Server', 'Ray Serve', 'JSON Schema', 'Azure OpenAI', 'AI Foundry', 'Vertex AI', 'Cloud Run', 'Hugging Face', 'Together AI', 'GitHub Actions', 'NeMo Guardrails', 'Guardrails AI', 'Llama Guard', 'Credo AI', 'Holistic AI', 'EU AI Act', 'NIST AI RMF', 'ISO 42001', 'SR 26-2']
EXTRA_TERMS = ["garak", "PyRIT", "Microsoft Responsible AI Toolbox", "OpenLineage", "Giskard", "Llama Guard", "NeMo Guardrails"]
# Short or ambiguous names in the list that resolve to a specific entry.
TERM_TO_ID = {"Triton": "triton_lang", "Inspect": "inspect_ai", "Phoenix": "phoenix", "OWASP": "owasp_llm_top10",
              "OAuth": "oauth", "OIDC": "oidc", "ISO 42001": "iso_42001", "SR 26-2": "sr_26_2", "LL144": "nyc_ll144",
              "ADK": "google_adk", "Lambda": "aws_lambda", "Azure OpenAI": "azure_ai_foundry", "AI Foundry": "azure_ai_foundry",
              "Megatron": "megatron", "Dynamo": "dynamo", "Ray Serve": "ray_serve", "Ray": "ray", "CuTe": "cute",
              "CuteDSL": "cutedsl", "Cohere": "cohere_models", "Transformers": "transformers", "Accelerate": "accelerate",
              "FSDP": "fsdp", "Nsight": "nsight", "NIM": "nim", "Isaac": "isaac", "ROS": "ros", "W&B": "wandb"}


def gh_slug(heading):
    s = heading.strip().lower()
    s = re.sub(r"[`*_~]", "", s)
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


@lru_cache(maxsize=None)
def anchors(path):
    text = Path(path).read_text(encoding="utf-8")
    found = set(re.findall(r'<a id="([^"]+)"></a>', text))
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                found.add(gh_slug(m.group(2)))
    return frozenset(found)


def check_doc(path, problems):
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT)
    if "@@" in text:
        problems.append(f"{name}: leftover template placeholder")
    if re.search(r"\]\(file://", text):
        problems.append(f"{name}: absolute file:// link")
    ids = re.findall(r'<a id="([^"]+)"></a>', text)
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        problems.append(f"{name}: duplicate anchors {dups}")
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", text):
        url = m.group(1)
        if url.startswith(("http://", "https://", "mailto:")):
            continue
        target_path, _, frag = url.partition("#")
        target = (path.parent / target_path).resolve() if target_path else path
        if not target.exists():
            problems.append(f"{name}: missing file {url}")
        elif frag and target.suffix == ".md" and frag not in anchors(str(target)):
            problems.append(f"{name}: missing anchor {url}")
    lines, in_code, i = text.splitlines(), False, 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
        if (not in_code and line.lstrip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1])):
            ncol = len(re.findall(r"(?<!\\)\|", line))
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                cells = len(re.findall(r"(?<!\\)\|", lines[j]))
                if cells != ncol:
                    problems.append(f"{name}:{j + 1}: table row has {cells} pipes, header {ncol}")
                j += 1
            i = j
            continue
        i += 1


def prose(text):
    """Text with fenced code, inline code, HTML comments, link targets and quoted strings removed."""
    out, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    t = "\n".join(out)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"`[^`\n]*`", " ", t)
    t = re.sub(r"\]\([^)\s]*\)", "]", t)
    t = re.sub(r'"[^"\n]*"', " ", t)
    t = re.sub(r"\u201c[^\u201d\n]*\u201d", " ", t)
    return t


def check_writing(path, problems):
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT)
    body = prose(text)
    for m in RELATIVE_TIME.finditer(body):
        line = body[:m.start()].count("\n") + 1
        problems.append(f"{name}: relative-time word '{m.group(0)}' near prose line {line}; write a date (EGP-1.0)")
    if path.name not in LEGACY_EXEMPT:
        if LEGACY.search(text):
            problems.append(f"{name}: refers to the legacy handbook (decision D-016: never linked or cited)")
        if name.as_posix() not in LEGACY_PHRASES_SKIP:
            for m in LEGACY_PHRASES.finditer(body):  # prose only: a phrase in quotes or code may be discussed
                problems.append(f"{name}: '{m.group(0)}' is a signature phrase of the legacy handbook (decision D-016); "
                                "use the repository's own evidence")


def check_legacy_data(problems):
    """The D-016 checks for the data files (the manifest is skipped: it repeats the documents' front matter)."""
    for p in sorted((ROOT / "data").glob("*.json")):
        if p.name == "manifest.json":
            continue
        text = p.read_text(encoding="utf-8")
        for m in list(LEGACY.finditer(text)) + list(LEGACY_PHRASES.finditer(text)):
            problems.append(f"{p.relative_to(ROOT)}: '{m.group(0)}' refers to or copies the legacy handbook (decision D-016)")


def check_dead_end(path, problems):
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("career/"):
        return
    text = path.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s#]+)(#[^)\s]*)?\)", text):
        url = m.group(1)
        if not url.startswith(("http://", "https://", "mailto:")) and url.endswith(".md"):
            if (path.parent / url).resolve() != path.resolve():
                return
    problems.append(f"{rel}: dead end (links to no other document)")


def check_guide_pattern(path, problems):
    """Guides follow the D-016 pattern: these four headings, in this order (other sections may sit between them)."""
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("career/") or rel in LEGACY_GUIDES:
        return
    text = path.read_text(encoding="utf-8")
    try:
        fm = parse_front_matter(text)
    except ValueError:
        return
    if not fm or fm.get("content_type") != "guide":
        return
    heads = re.findall(r"^## (.+?)\s*$", text, re.M)
    pos = [next((i for i, h in enumerate(heads) if h == want), None) for want in GUIDE_HEADINGS]
    missing = [w for w, p in zip(GUIDE_HEADINGS, pos) if p is None]
    if missing:
        problems.append(f"{rel}: guide pattern (D-016) is missing the heading(s) {missing}")
    elif pos != sorted(pos):
        problems.append(f"{rel}: guide pattern (D-016) headings are out of order; expected {GUIDE_HEADINGS}")


def due_documents(today):
    due = []
    for p in sorted(CAREER.rglob("*.md")) + [ROOT / q for q in FRONT_MATTER_PAGES if (ROOT / q).exists()]:
        try:
            fm = parse_front_matter(p.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if fm and fm.get("review_by") and fm["review_by"] < today and fm.get("status") == "published":
            due.append(f"{p.relative_to(ROOT).as_posix()}: review_by {fm['review_by']} has passed")
    return due


def check_stack(problems):
    stack = stack_lib.load(stack_lib.STACK)
    scores = stack_lib.load(stack_lib.SCORES)
    onto = stack_lib.load(stack_lib.ONTOLOGY)
    problems.extend(stack_lib.errors(stack, scores, onto))


def check_generators(problems):
    for script in GENERATORS:
        run = subprocess.run([sys.executable, "-B", str(SCRIPTS / script), "--check"], capture_output=True, text=True, cwd=ROOT)
        if run.returncode != 0:
            problems.append(f"{script} --check: " + (run.stdout + run.stderr).strip()[:1500])


def check_ranks(problems):
    data = json.loads((ROOT / "data" / "role_scores.json").read_text(encoding="utf-8"))
    _, res = rr.tables(data)
    rank = {r["id"]: str(r["rank"]) for r in res["base"]}
    rank.update({r["id"]: f"L{r['rank']}" for r in res["leadership"]})
    cci = {r["id"]: r["cci"] for r in res["base"]}
    master = (CAREER / "02-roles" / "role-catalog.md").read_text(encoding="utf-8")
    for slug, rk in re.findall(r"^#### `([a-z0-9-]+)`: .*? · Rank ([L0-9]+)$", master, re.M):
        if rank.get(slug) != rk:
            problems.append(f"master catalog: profile {slug} says Rank {rk}, rank_roles.py says {rank.get(slug)}")
    for slug, rk in re.findall(r"^\| `([a-z0-9-]+)` \| .*\| ([L0-9]+) \|$", master, re.M):
        if slug in rank and rank[slug] != rk:
            problems.append(f"master catalog: registry {slug} says {rk}, rank_roles.py says {rank[slug]}")
    order = [s for s, _ in re.findall(r"^\| `([a-z0-9-]+)` \| \[.*\| ([L0-9]+) \|$", master, re.M)]
    if order != [r["id"] for r in res["base"]] + [r["id"] for r in res["leadership"]]:
        problems.append("master catalog: registry rows are not in rank order")
    skills = (CAREER / "03-skills-and-tech" / "role-skill-maps.md").read_text(encoding="utf-8")
    for n, slug, rk in re.findall(r"^### 3\.(\d+) .*?\(`([a-z0-9-]+)`\) · CCI rank #(\d+)$", skills, re.M):
        if rank.get(slug) != rk or n != rk:
            problems.append(f"skills catalog: section 3.{n} {slug} says Rank #{rk}, rank_roles.py says {rank.get(slug)}")
    ranked = (CAREER / "02-roles" / "role-rankings.md").read_text(encoding="utf-8")
    for rk, title, val in re.findall(r"^### #(\d+) (.*?): CCI ([0-9.]+) ", ranked, re.M):
        sid = res["base"][int(rk) - 1]["id"]
        want = f"{float(cci[sid]) + 1e-9:.1f}"
        if val != want:
            problems.append(f"ranked catalog: dossier #{rk} {title} shows CCI {val}, rank_roles.py gives {want}")


def check_ontology(problems):
    onto = json.loads((ROOT / "data" / "skills_ontology.json").read_text(encoding="utf-8"))
    scores = json.loads((ROOT / "data" / "role_scores.json").read_text(encoding="utf-8"))
    ic = {r["id"] for r in scores["roles"] if r["track"] == "ic"}
    known = {r["id"] for r in scores["roles"]}
    on_ic = {k for k, r in onto["roles"].items() if isinstance(r["target"], int)}
    if on_ic != ic:
        problems.append(f"skills ontology IC roles differ from role_scores.json: missing {sorted(ic - on_ic)}, extra {sorted(on_ic - ic)}")
    for k, r in onto["roles"].items():
        for slug in r.get("covers", [k]):
            if slug not in known:
                problems.append(f"skills ontology: unknown role slug {slug}")

    def norm(x):
        return re.sub(r"[^a-z0-9+#]", "", x.lower())
    names = {}
    for sid, e in onto["skills"].items():
        base = e["name"].split(" (")[0]
        for term in [e["name"], base] + e.get("aliases", []) + base.split(" / "):
            names.setdefault(norm(term), sid)
    for cid, c in onto["classes"].items():
        names.setdefault(norm(c["name"]), cid)
    rest, terms = " ".join(TECH.split()), []
    for m in MULTI_WORD:
        if m in rest:
            terms.append(m)
            rest = rest.replace(m, " ")
    terms += rest.split() + EXTRA_TERMS
    unresolved = sorted({t for t in terms if norm(t) not in names and t not in TERM_TO_ID})
    if unresolved:
        problems.append(f"vocabulary coverage: {len(unresolved)} named technologies have no typed entry: {unresolved}")
    bad = sorted(k for k, v in TERM_TO_ID.items() if v not in onto["skills"] and v not in onto["classes"])
    if bad:
        problems.append(f"validate_docs.py TERM_TO_ID points to unknown IDs: {bad}")


def check_front_matter(problems, only=None):
    schema = json.loads((ROOT / "data" / "schemas" / "frontmatter.schema.json").read_text(encoding="utf-8"))
    paths = sorted(CAREER.rglob("*.md")) + [ROOT / p for p in FRONT_MATTER_PAGES if (ROOT / p).exists()]
    if only is not None:
        paths = [p for p in paths if p.resolve() in only]
    seen = {}
    for p in paths:
        rel = p.relative_to(ROOT).as_posix()
        try:
            fm = parse_front_matter(p.read_text(encoding="utf-8"))
        except ValueError as ex:
            problems.append(f"{rel}: bad front matter ({ex})")
            continue
        if fm is None:
            problems.append(f"{rel}: missing front matter")
            continue
        problems.extend(f"{rel}: front matter {e[2:]}" for e in schema_errors(fm, schema, schema))
        if fm.get("id") in seen:
            problems.append(f"{rel}: front matter id {fm['id']!r} also used by {seen[fm['id']]}")
        seen[fm.get("id")] = rel
        m = re.match(r"career/(\d\d)-", rel)
        if m and fm.get("stage") != int(m.group(1)):
            problems.append(f"{rel}: front matter stage {fm.get('stage')} does not match its folder ({int(m.group(1))})")


def main():
    ap = argparse.ArgumentParser(description="Validate documents, generated outputs and data consistency.")
    ap.add_argument("--strict", action="store_true", help="count documents past their review_by date as problems")
    ap.add_argument("--files", nargs="+", metavar="PATH", help="run only the document-level checks on these files")
    args = ap.parse_args()
    problems = []
    if args.files:
        only = {Path(f).resolve() for f in args.files}
        for path in [Path(f) for f in args.files]:
            path = path.resolve()
            check_doc(path, problems)
            check_writing(path, problems)
            check_dead_end(path, problems)
            check_guide_pattern(path, problems)
        check_front_matter(problems, only)
        print("PROBLEMS:", len(problems))
        for p in problems:
            print(" -", p)
        sys.exit(1 if problems else 0)
    for path in FILES:
        check_doc(path, problems)
        check_writing(path, problems)
        check_dead_end(path, problems)
        check_guide_pattern(path, problems)
    check_front_matter(problems)
    check_legacy_data(problems)
    check_stack(problems)
    check_generators(problems)
    check_ranks(problems)
    check_ontology(problems)
    due = due_documents(datetime.date.today().isoformat())
    if args.strict:
        problems += due
    print("PROBLEMS:", len(problems))
    for p in problems:
        print(" -", p)
    if due and not args.strict:
        print("DUE FOR RE-VERIFICATION:", len(due))
        for d in due:
            print(" -", d)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
