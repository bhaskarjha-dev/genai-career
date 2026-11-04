#!/usr/bin/env python3
"""Documentation validator for the career catalogs.

Checks, across every career/*.md file, the generated role inventories and README.md:
  * relative links resolve to existing files and anchors; no absolute file:// links;
    no duplicate anchors; no leftover template placeholders
  * every Markdown table row has the same number of cells as its header
  * every generated block is current: rank_roles.py, build_index.py, build_skills.py,
    build_resume_matrix.py, resume_layers.py, build_findings.py and build_manifest.py are each
    run with --check
  * ranks agree across the master catalog, the skills catalog, the ranked catalog's
    dossiers and scripts/rank_roles.py
  * every career/ document and research index page carries valid front matter
    (data/schemas/frontmatter.schema.json), with a unique id and a stage that matches its folder
  * the skills ontology covers exactly the individual-contributor roles of role_scores.json
  * corpus coverage: every technology named in the research sessions or the skills catalog
    (the 2026-11-04 audit list below) resolves to a typed vocabulary entry

Usage:
    python3 scripts/validate_docs.py      # prints PROBLEMS: <n> and the list; exit 1 if any

Standard library only.
"""
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

SEALED = {"FAD.md", "DECISIONS.md", "RESEARCH-PIPELINE.md"}  # Phase 0 records: checked by hand, not linted here
FILES = (sorted(CAREER.rglob("*.md")) + sorted(ROOT.glob("*.md"))
         + sorted(p for p in (ROOT / "research").glob("*.md") if p.name not in SEALED)
         + [p for p in [ROOT / "llms.txt", ROOT / "data" / "README.md", ROOT / "scripts" / "README.md"] if p.exists()])
GENERATORS = ["rank_roles.py", "build_index.py", "build_skills.py", "build_resume_matrix.py", "resume_layers.py",
              "build_findings.py", "build_manifest.py"]
FRONT_MATTER_PAGES = ["research/README.md", "research/findings.md", "research/ERRATA.md"]

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
    for n, slug, rk in re.findall(r"^### 3\.(\d+) .*?\(`([a-z0-9-]+)`\) · Rank #(\d+)$", skills, re.M):
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


def check_front_matter(problems):
    schema = json.loads((ROOT / "data" / "schemas" / "frontmatter.schema.json").read_text(encoding="utf-8"))
    paths = sorted(CAREER.rglob("*.md")) + [ROOT / p for p in FRONT_MATTER_PAGES if (ROOT / p).exists()]
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
    problems = []
    for path in FILES:
        check_doc(path, problems)
    check_front_matter(problems)
    check_generators(problems)
    check_ranks(problems)
    check_ontology(problems)
    print("PROBLEMS:", len(problems))
    for p in problems:
        print(" -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
