#!/usr/bin/env python3
"""Research pipeline 2: validate the session catalogue, keep its tracker current and assemble session prompts.

research/pipeline-2/catalogue.json lists every planned session: its brief (a template in research/pipeline-2/briefs/),
its parameters, the knowledge-base outputs it feeds, the tool categories it owns and its status. This script:

  * --update / --check: validates the catalogue and the briefs, assembles every session's prompt as a dry run, and
    writes (or checks) the tracker block in research/pipeline-2/README.md. A session counts as saved once
    research/sessions/<id>-<slug>.md exists.
  * --prompt ID: prints the complete prompt for one session: the brief with the knowledge base's current claims
    filled in from data/ (numbered K1, K2 ...), followed by the shared protocol (research/pipeline-2/PROTOCOL.md).
  * --next: lists the sessions not yet saved, in recommended order.
  * --appendix PATH|ID: checks a session report (a draft before you save it, or a saved session): front matter,
    required sections, Key Findings, a verdict for every K-number, and every data-appendix record.
  * --verify PATH|ID: prints the verification prompt (research/pipeline-2/VERIFY.md) followed by the report's
    load-bearing claims, with their sources, in batches of 25.

Usage:
    python3 -B scripts/research_pipeline.py --update
    python3 -B scripts/research_pipeline.py --check
    python3 -B scripts/research_pipeline.py --prompt T0-19 > ~/T0-19-prompt.md     # optionally --date YYYY-MM-DD
    python3 -B scripts/research_pipeline.py --next
    python3 -B scripts/research_pipeline.py --appendix ~/Downloads/T0-19-draft.md
    python3 -B scripts/research_pipeline.py --verify T0-19

It writes only the tracker block; prompts and reports go to standard output. Standard library only.
"""
import argparse
import datetime
import json
import random
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common import RELATIVE_TIME, gh_slug, load_json, prose  # noqa: E402

RP2 = ROOT / "research" / "pipeline-2"
CATALOGUE = RP2 / "catalogue.json"
BRIEFS = RP2 / "briefs"
README = RP2 / "README.md"
PROTOCOL = RP2 / "PROTOCOL.md"
VERIFY = RP2 / "VERIFY.md"
SESSIONS = ROOT / "research" / "sessions"
DECISIONS = ROOT / "research" / "DECISIONS.md"
DATA = ROOT / "data"

BEGIN = "<!-- BEGIN GENERATED: scripts/research_pipeline.py (tracker) -->"
END = "<!-- END GENERATED: scripts/research_pipeline.py (tracker) -->"
PROMPT_MARK = "<!-- BEGIN PROMPT -->"
BLOCKS = ["DECISION", "BRIEF", "SCOPE", "KNOWN", "CALIBRATION", "APPROACH", "DONE", "FORMAT"]
SECTIONS = ["Prior", "Research Question", "Key Findings", "Recommendation", "Alternatives Considered",
            "Detailed Findings", "Repository Deltas", "Absences", "Open Questions & Risks", "Discovered Concerns",
            "Delta", "Sources & Evidence Ledger", "Data Appendix"]
FRONT_MATTER_KEYS = ["id", "title", "date", "status", "topic", "confidence", "temporal_anchor", "authored_by_model",
                     "protocol_version"]
PRIORITIES = ["P0", "P1", "P2"]
VERIFY_MODES = ["required", "sample"]
DRY_RUN_DATE = "2026-11-08"  # fixed, so that --check is deterministic
MAX_PROMPT_CHARS = 80000
BATCH = 25         # items per verification batch
SAMPLE_EXTRA = 20  # records below A/B added at random to a sample-mode verification packet

# Data-appendix record types: the fields each must carry beyond type, grade, src and as_of (PROTOCOL.md §10).
# A tuple means "any one of these". Every type except repo_delta and absence also needs ttl.
RECORD_TYPES = OrderedDict([
    ("repo_delta", ["k", "verdict", "finding"]),
    ("absence", ["item", "searched"]),
    ("measure", ["subject", "measure", "unit", ("value", "lo")]),
    ("credential", ["id", "name", "issuer", "level", "state", "url"]),
    ("board", ["id", "name", "url", "kind", "regions", "verdict", "why"]),
    ("tool", ["id", "name", "stage", "category", "what", "verdict", "why", "url"]),
    ("company", ["name", "employer_type", "hq", "regions"]),
    ("jd", ["employer", "title", "url", "seen", "location", "seniority", "must"]),
    ("pay", ["role", "location", "stat", "currency", "period", "basis", "source_name", ("value", "lo")]),
    ("visa_route", ["country", "route", "kind", "eligibility", "url"]),
    ("rule", ["jurisdiction", "instrument", "requirement", "status", "url"]),
    ("practice", ["area", "tactic", "claim", "evidence", "verdict"]),
    ("community", ["name", "kind", "url", "access", "verdict"]),
    ("resource", ["name", "provider", "url", "kind", "verdict"]),
    ("skill_signal", ["role", "skill", "n", "source_kind", ("share", "count")]),
    ("loop", ["employer", "track", "stages"]),
    ("prompt", ["track", "prompt", "covers"]),
])
NO_TTL = {"repo_delta", "absence"}
GRADES = {"A", "B", "C", "D", "E", "M", "P"}
DELTA_VERDICTS = {"confirmed", "updated", "contradicted", "stale", "unverifiable"}
ENUMS = {
    ("repo_delta", "verdict"): DELTA_VERDICTS,
    ("practice", "verdict"): {"use", "use-with-care", "avoid", "untested"},
    ("board", "verdict"): {"use", "use-with-care", "avoid", "watch"},
    ("tool", "verdict"): {"use", "use-with-care", "avoid", "watch"},
    ("community", "verdict"): {"use", "use-with-care", "avoid", "watch"},
    ("resource", "verdict"): {"use", "use-with-care", "avoid", "watch"},
    ("credential", "state"): {"active", "beta", "announced", "retiring", "retired", "renamed"},
    ("company", "employer_type"): {"frontier-lab", "big-tech", "ai-startup", "enterprise", "gcc", "it-services", "public-sector",
                          "other"},
    ("pay", "stat"): {"p10", "p25", "p50", "p75", "p90", "mean", "range", "offer"},
    ("pay", "basis"): {"base", "tc", "rate"},
    ("pay", "period"): {"year", "month", "day", "hour"},
    ("visa_route", "kind"): {"employer-sponsored", "self-sponsored", "talent", "points", "job-seeker", "founder",
                             "intra-company", "remote-work", "graduate"},
    ("rule", "status"): {"in-force", "enacted", "proposed", "pending", "litigated", "repealed"},
    ("skill_signal", "source_kind"): {"jd-sample", "platform", "survey"},
    ("prompt", "track"): {"application", "customer-application", "ml-system-design", "infrastructure", "evaluation",
                          "research", "governance", "product", "behavioural", "coding"},
}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TTL = re.compile(r"^V[0-6]$")
PLACEHOLDER = re.compile(r"\{\{([a-z_]+)(?::([^}]*))?\}\}")
K_LINE = re.compile(r"^- K: ", re.M)
TIER_NAMES = OrderedDict([("M", "Must"), ("I", "Important"), ("S", "Should"), ("O", "Optional"), ("X", "Avoid")])
# Labels from the knowledge base's own vocabulary that may reach a prompt, with what they mean to an outside reader.
LEGEND = OrderedDict([
    (r"\bS09\b", "S09: a corpus of 2026 AI-engineering job postings analysed in one of the knowledge base's research sessions"),
    (r"\bT[0-5]–T[0-5]\b", "T0–T5 (as in \"for T2–T3\"): the knowledge base's career tiers, from entry (T0) to apex (T5)"),
    (r"\bCCI\b", "CCI: the knowledge base's composite career index, a model output"),
    (r"\bD-0\d\d\b", "D-0nn: a decision in the knowledge base's decision registry"),
])


# ---------------------------------------------------------------- loading
def catalogue():
    return load_json(CATALOGUE)


def session_file(sid):
    """The saved session file for an ID, or None."""
    hits = sorted(SESSIONS.glob(f"{sid}-*.md"))
    return hits[0] if hits else None


def decision_ids():
    return set(re.findall(r"^# (D-\d{3}):", DECISIONS.read_text(encoding="utf-8"), re.M))


def headings(path):
    text = re.sub(r"(?ms)^```.*?^```", "", path.read_text(encoding="utf-8"))
    return {gh_slug(h) for h in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}


class Context:
    """The data the placeholders read, loaded once."""

    def __init__(self):
        self.scores = load_json(DATA / "role_scores.json")
        self.onto = load_json(DATA / "skills_ontology.json")
        self.tools = load_json(DATA / "tools.json")
        self.tool_categories = load_json(DATA / "schemas" / "tools.schema.json")["$defs"]["category"]["enum"]
        self.titles = load_json(DATA / "role_titles.json")
        self.shares = load_json(DATA / "posting_skill_shares.json")
        self.stack = load_json(DATA / "stack_model.json")
        self.roles = OrderedDict((r["id"], r) for r in self.scores["roles"])


# ---------------------------------------------------------------- rendering helpers
def first_sentence(text, limit=240):
    s = re.split(r"(?<=\.)\s", text.strip(), maxsplit=1)[0].rstrip(";:, ")
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + " …"


def bullets(items):
    return "\n".join(f"- {x}" for x in items) if items else "- (none)"


def k_lines(items):
    return "\n".join(f"- K: {x}" for x in items)


def clean_tool_text(text):
    """Replace the tool catalogue's internal labels with plain words for an outside reader."""
    text = re.sub(r"Hard disqualifier D\d:\s*", "A hard disqualifier in the verdict rubric applies: ", text)
    text = re.sub(r"\(T\d-\d\d (Caution|Avoid|Use)\)", r"(rated \1 by a knowledge-base session)", text)
    text = re.sub(r"\bT\d-\d\d (Caution|rates|rated|treats|relied)\b", r"a knowledge-base session \1", text)
    text = re.sub(r"\bT\d-\d\d R\d+\b", "a knowledge-base rule", text)
    text = re.sub(r"\bTier 1 data\b", "low-sensitivity data", text)
    text = re.sub(r"\bTier 3 data in T\d-\d\d's upload rules\b", "the most sensitive class of personal data", text)
    return text


def render_tools(ctx, session):
    cats = session.get("tool_categories", [])
    rows = [t for t in ctx.tools["tools"] if t["category"] in cats]
    if not cats:
        return ""
    head = (f"Tools the knowledge base lists in the categories this session owns ({', '.join(cats)}), with its verdicts "
            "(each line is a claim to test):\n\n")
    if not rows:
        return head + "- (No tools listed yet in these categories.)"
    return head + k_lines(clean_tool_text(
        f"{t['name']} ({t['category']}): verdict {t['verdict']}, as of {t['as_of']}"
        + (f"; status {t['status']}" if t.get("status") else "") + f". {first_sentence(t['why'])}") for t in rows)


def render_tool_rubric(ctx, _arg):
    return bullets(f"**{k}:** {v}" for k, v in ctx.tools["rubric"].items())


def credential_roles(ctx, cid):
    """'Role (tier)' for every role in the ontology that lists the credential."""
    return [f"{r['name']} ({TIER_NAMES.get(c['tier'], c['tier'])})"
            for r in ctx.onto["roles"].values() for c in r.get("credentials", []) if c["id"] == cid]


def render_credentials(ctx, arg, params):
    issuers = [s.strip() for s in arg.split(",")] if arg else params.get("issuers", [])
    rows = []
    for cid, c in ctx.onto["credentials"].items():
        if issuers and not any(i.lower() in c["issuer"].lower() for i in issuers):
            continue
        st = c.get("status") or {}
        state = f"{st.get('state', 'status not recorded')}" + (f" as of {st['as_of']}" if st.get("as_of") else "")
        note = f" ({st['note']})" if st.get("note") else ""
        roles = credential_roles(ctx, cid)
        listed = f" Listed for: {', '.join(roles)}." if roles else ""
        rows.append(f"{c['name']}, issuer {c['issuer']}, level {c['level']}: {state}{note}.{listed}")
    return k_lines(rows) if rows else "- (The knowledge base lists no credentials for these issuers.)"


def skill_label(ctx, sid):
    e = ctx.onto["skills"].get(sid) or ctx.onto["classes"].get(sid)
    name = re.sub(r" \(C\d\)$", "", e["name"]) if e else sid
    return f"{name} [{sid}]"


def stack_name(ctx, key):
    if key in ctx.stack["layers"]:
        return f"{key} {ctx.stack['layers'][key]['name']}"
    return ctx.stack["planes"][key]["name"] if key in ctx.stack["planes"] else key


def render_role_cards(ctx, params):
    out = []
    for rid in params.get("roles", []):
        r = ctx.roles[rid]
        o = ctx.onto["roles"].get(rid)
        claims, context = [], []
        claims.append(f"Definition: {r['definition']} Family: {r['family']}; evidence status {r['status']} "
                      "(E established, V verified but volume unmeasured, W emerging or watchlist, A absorbed specialisation).")
        aliases = [t["title"] for t in ctx.titles["titles"] if t.get("maps_to") == rid and t["type"] != "Canonical"]
        if aliases:
            claims.append("Title aliases and variants recorded for this role: " + "; ".join(aliases[:25]) + ".")
        for key, label in [("demand", "Demand evidence"), ("comp", "Pay evidence")]:
            if key in r:
                claims.append(f"{label}: {r[key]['basis']} [grade {r[key]['grade']}]")
        for key, label in [("demand", "India demand evidence"), ("comp", "India pay evidence")]:
            if r.get("india", {}).get(key):
                claims.append(f"{label}: {r['india'][key]['basis']} [grade {r['india'][key]['grade']}]")
        if "durability" in r:
            claims.append(f"Durability evidence (a judgement; test what it cites): {r['durability']['basis']} [grade {r['durability']['grade']}]")
        st = r.get("stack") or {}
        if st.get("primary"):
            foot = stack_name(ctx, st["primary"])
            if st.get("secondary"):
                foot += "; also " + ", ".join(stack_name(ctx, x) for x in st["secondary"])
            if st.get("planes"):
                foot += "; planes: " + ", ".join(stack_name(ctx, x) for x in st["planes"])
            claims.append(f"Work footprint in the AI stack (a judgement): {foot}.")
        if r.get("interview_track"):
            t = ctx.scores["interview_tracks"][r["interview_track"]]
            claims.append(f"Interview track: {t['name']}; it tests {t['tests']}.")
        if o:
            for tier in ("M", "I"):
                names = [skill_label(ctx, l["id"]) + (f" ({l['share']} of postings)" if l.get("share") else "")
                         for l in o.get("links", []) if l["tier"] == tier]
                if names:
                    claims.append(f"{TIER_NAMES[tier]} skills: " + "; ".join(names) + ".")
            creds = [f"{ctx.onto['credentials'][c['id']]['name']} ({TIER_NAMES.get(c['tier'], c['tier'])}: {c.get('note', '')})"
                     for c in o.get("credentials", []) if c["id"] in ctx.onto["credentials"]]
            if creds:
                claims.append("Credentials: " + "; ".join(creds) + ".")
            for key, label in [("prereq", "Prerequisites"), ("proof", "Proof of work it needs"),
                               ("avoid", "Leave out or reframe")]:
                if o.get(key):
                    claims.append(f"{label}: {o[key]}")
        scores = []
        for key, label in [("demand", "demand"), ("comp", "pay"), ("durability", "durability"), ("leverage", "leverage")]:
            if key in r:
                scores.append(f"{label} {r[key]['mid']} ({r[key]['lo']}–{r[key]['hi']})")
        if scores:
            context.append("Scores on its anchored 0–10 rubric: " + ", ".join(scores) + "."
                           + (f" Leverage basis: {r['leverage']['basis']}" if "leverage" in r else ""))
        if r.get("persona_access"):
            context.append("Access from each background, 0–10 (judgement): "
                           + ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in r["persona_access"].items()) + ".")
        if o and isinstance(o.get("target"), int):
            n_ic = sum(isinstance(x.get("target"), int) for x in ctx.onto["roles"].values())
            context.append(f"Its GenAI target order puts this role #{o['target']} of {n_ic} (a model output).")
        specs = [s["name"] for s in ctx.stack["specialisations"] if rid in s.get("home", [])]
        if specs:
            context.append("Specialisations it records inside this role (report their shares in your sample): " + "; ".join(specs) + ".")
        out.append(f"#### {r['name']} (role ID `{rid}`)\n\n{k_lines(claims)}\n\nContext for this role (no verdict needed):\n\n{bullets(context)}\n")
    return "\n".join(out).rstrip()


def render_roles(ctx, _arg):
    rows = ["| Role ID | Role | Family | Evidence status | GenAI target |", "|---|---|---|:---:|:---:|"]

    def order(r):
        t = ctx.onto["roles"].get(r["id"], {}).get("target")
        return (0, t) if isinstance(t, int) else (1, r["id"])
    for r in sorted(ctx.roles.values(), key=order):
        t = ctx.onto["roles"].get(r["id"], {}).get("target", "—")
        rows.append(f"| `{r['id']}` | {r['name']} | {r['family']} | {r['status']} | {t if isinstance(t, int) else '—'} |")
    return "\n".join(rows)


def render_families(ctx, _arg):
    fam = OrderedDict()
    for r in ctx.roles.values():
        fam.setdefault(r["family"], []).append(r["name"])
    return bullets(f"**{f}:** {', '.join(names)}" for f, names in fam.items())


def render_interview_tracks(ctx, _arg):
    return bullets(f"**{t['name']}** (`{k}`): {t['tests']}" for k, t in ctx.scores["interview_tracks"].items())


def render_count_sources(ctx, _arg):
    return ", ".join(f"{k} ({v})" for k, v in ctx.scores["count_sources"].items())


def render_resume_variants(ctx, _arg):
    out = []
    for vid, v in ctx.onto["resume_variants"].items():
        fl = "; ".join(f"{fid} {txt}" for fid, txt in v.get("flavours", {}).items())
        out.append(f"Variant {vid}, {v['name']}: headline \"{v['headline']}\". Flavours: {fl}.")
    return bullets(out)


def render_posting_titles(ctx, _arg):
    snap = ctx.shares["snapshots"][-1]
    out = []
    for t in snap["titles"]:
        top = ", ".join(f"{s['name']} {s['share']}%" for s in t["skills"][:8])
        out.append(f"{t['title']} ({snap['source']}, retrieved {snap['retrieved']}): {top}" + (f". {t['notes']}" if t.get("notes") else ""))
    return bullets(out)


def render_devalued(ctx, _arg):
    return k_lines(f"{d['name']}: {d['verdict']}. {d['evidence']} [{d.get('grade', '')}]" for d in ctx.onto["devalued"])


def render_watchlist(ctx, _arg):
    kinds = {"Quarantined": "quarantined", "Unmeasured buzzword": "never measured", "Candidate (unmeasured)": "a candidate title, unmeasured"}
    rows = [f"\"{t['title']}\" is {kinds[t['type']]}" + (f": {t['note']}" if t.get("note") else ".")
            for t in ctx.titles["titles"] if t["type"] in kinds]
    return k_lines(rows) if rows else "- (none)"


def derived_params(ctx, params):
    out = dict(params)
    roles = params.get("roles")
    if roles:
        names = [ctx.roles[r]["name"] for r in roles]
        out.setdefault("subject", f"the {names[0]} role" if len(names) == 1
                       else "these roles: " + ", ".join(names[:-1]) + " and " + names[-1])
        out.setdefault("jd_target", 30 if len(roles) == 1 else 15)
    if isinstance(out.get("countries"), list):
        out["countries"] = ", ".join(out["countries"])
    return out


def min_records(ctx, session):
    """Minimum record counts the brief asks for: explicit params, plus the job-description target of role dossiers."""
    params = derived_params(ctx, session.get("params", {}))
    mins = dict(session.get("params", {}).get("min_records", {}))
    if params.get("roles"):
        mins.setdefault("jd", params["jd_target"] * len(params["roles"]))
    return mins


def expand(ctx, session, date, text):
    params = derived_params(ctx, session.get("params", {}))
    simple = {
        "id": session["id"], "title": session["title"], "date": date,
        "filename": f"{session['id']}-{session['slug']}.md",
        "decisions": ", ".join(session["decisions"]) if session["decisions"] else "none directly",
        "feeds": "; ".join(f"`{f}`" for f in session["feeds"]),
        "records": ", ".join(f"`{r}`" for r in session["records"]),
        "stages": ", ".join(str(s) for s in session["stages"]),
    }
    data = {
        "tool_rubric": render_tool_rubric, "roles": render_roles, "families": render_families,
        "interview_tracks": render_interview_tracks, "count_sources": render_count_sources,
        "resume_variants": render_resume_variants, "posting_titles": render_posting_titles, "devalued": render_devalued,
        "watchlist": render_watchlist,
    }

    def sub(m):
        name, arg = m.group(1), m.group(2)
        if name in simple and arg is None:
            return simple[name]
        if name in data:
            return data[name](ctx, arg or "")
        if name == "tools" and arg is None:
            return render_tools(ctx, session)
        if name == "credentials":
            return render_credentials(ctx, arg, params)
        if name == "role_cards":
            return render_role_cards(ctx, params)
        if name == "claims":
            return k_lines(params.get("claims", []))
        if name == "context":
            items = params.get("context") or []
            return ("Context (what the knowledge base already holds or lacks; no verdict needed):\n\n" + bullets(items)
                    if items else "")
        if name == "param" and arg:
            if arg not in params:
                raise KeyError(f"{session['id']}: placeholder {{{{param:{arg}}}}} has no parameter '{arg}'")
            v = params[arg]
            return bullets(v) if isinstance(v, list) else str(v)
        raise KeyError(f"{session['id']}: unknown placeholder {m.group(0)}")
    for _ in range(2):  # a second pass expands placeholders written inside parameters
        text = PLACEHOLDER.sub(sub, text)
    return text


def number_claims(text):
    n = [0]

    def sub(_m):
        n[0] += 1
        return f"- K{n[0]}. "
    return K_LINE.sub(sub, text), n[0]


def add_legend(text):
    """Explain internal labels that reached the KNOWN section, just before CALIBRATION."""
    known = text.split("\n## KNOWN", 1)[-1].split("\n## CALIBRATION", 1)[0]
    found = [expl for pat, expl in LEGEND.items() if re.search(pat, known)]
    if not found:
        return text
    note = "Labels used above:\n\n" + bullets(found) + "\n"
    return text.replace("\n## CALIBRATION", "\n" + note + "\n## CALIBRATION", 1)


def strip_comments(text):
    return re.sub(r"^\s*(<!--.*?-->\s*)+", "", text, flags=re.S)


def protocol_text():
    text = PROTOCOL.read_text(encoding="utf-8")
    if PROMPT_MARK not in text:
        raise SystemExit(f"{PROTOCOL.relative_to(ROOT)}: missing the {PROMPT_MARK} marker")
    return text.split(PROMPT_MARK, 1)[1].strip()


def build_prompt(ctx, session, date):
    brief = strip_comments((BRIEFS / session["brief"]).read_text(encoding="utf-8"))
    body = re.sub(r"\n{3,}", "\n\n", expand(ctx, session, date, brief))
    body, n_claims = number_claims(add_legend(body))
    return body.rstrip() + "\n\n---\n\n" + protocol_text() + "\n", n_claims


# ---------------------------------------------------------------- validation
def validate(cat, ctx):
    errs = []
    req = ["id", "slug", "title", "family", "wave", "priority", "brief", "decisions", "stages", "feeds", "records",
           "tool_categories", "verify", "params", "status"]
    known_decisions = decision_ids()
    seen, used_briefs, owners = set(), set(), {}
    for s in cat["sessions"]:
        sid = s.get("id", "?")
        missing = [k for k in req if k not in s]
        if missing:
            errs.append(f"{sid}: missing fields {missing}")
            continue
        if not re.match(r"^T[0-2]-\d\d$", sid):
            errs.append(f"{sid}: session IDs follow T#-## (research/README.md)")
        if sid in seen:
            errs.append(f"{sid}: duplicate session ID")
        seen.add(sid)
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", s["slug"]):
            errs.append(f"{sid}: slug must be kebab-case")
        if s["family"] not in cat["families"]:
            errs.append(f"{sid}: unknown family {s['family']}")
        if str(s["wave"]) not in cat["waves"]:
            errs.append(f"{sid}: unknown wave {s['wave']}")
        if s["priority"] not in PRIORITIES:
            errs.append(f"{sid}: priority must be one of {PRIORITIES}")
        if s["verify"] not in VERIFY_MODES:
            errs.append(f"{sid}: verify must be one of {VERIFY_MODES}")
        if s["status"] not in cat["statuses"]:
            errs.append(f"{sid}: unknown status {s['status']}")
        if "run_after" in s and not DATE.match(str(s["run_after"])):
            errs.append(f"{sid}: run_after must be YYYY-MM-DD")
        if not (BRIEFS / s["brief"]).exists():
            errs.append(f"{sid}: brief {s['brief']} not found in {BRIEFS.relative_to(ROOT)}")
        used_briefs.add(s["brief"])
        for d in s["decisions"]:
            if d not in known_decisions:
                errs.append(f"{sid}: decision {d} is not in research/DECISIONS.md")
        for st in s["stages"]:
            if not (isinstance(st, int) and 0 <= st <= 11):
                errs.append(f"{sid}: stage {st!r} is not 0–11")
        for f in s["feeds"]:
            path, _, anchor = f.partition("#")
            if not (ROOT / path).exists():
                errs.append(f"{sid}: feeds {path}, which does not exist")
            elif anchor and anchor not in headings(ROOT / path):
                errs.append(f"{sid}: feeds {f}, but that anchor does not exist")
        bad = [r for r in s["records"] if r not in RECORD_TYPES]
        if bad:
            errs.append(f"{sid}: unknown record types {bad}")
        for c in s["tool_categories"]:
            if c not in ctx.tool_categories:
                errs.append(f"{sid}: tool category {c!r} is not in data/schemas/tools.schema.json")
            elif c in owners:
                errs.append(f"{sid}: tool category {c!r} is already owned by {owners[c]} (one owning session per category)")
            else:
                owners[c] = sid
        for k, v in s["params"].get("min_records", {}).items():
            if k not in RECORD_TYPES or not (isinstance(v, int) and v > 0):
                errs.append(f"{sid}: min_records needs record types and positive counts ({k}: {v!r})")
        for rid in s["params"].get("roles", []):
            if rid not in ctx.roles:
                errs.append(f"{sid}: unknown role {rid}")
        saved = session_file(sid)
        if saved and not saved.name.startswith(f"{sid}-{s['slug']}"):
            errs.append(f"{sid}: research/sessions/{saved.name} uses this ID with another slug ({s['slug']} expected)")
        if s["status"] == "integrated" and not saved:
            errs.append(f"{sid}: status integrated, but no session file research/sessions/{sid}-{s['slug']}.md")
    orphans = [c for c in ctx.tool_categories if c not in owners]
    if orphans:
        errs.append(f"tool categories owned by no session (their tools would never be re-verified): {orphans}")
    for p in sorted(BRIEFS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        if p.name not in used_briefs:
            errs.append(f"briefs/{p.name}: no session uses this brief")
        if not re.search(r"^# RESEARCH BRIEF: ", text, re.M):
            errs.append(f"briefs/{p.name}: needs a '# RESEARCH BRIEF: ' title")
        found = re.findall(r"^## ([A-Z]+)\s*$", text, re.M)
        if found != BLOCKS:
            errs.append(f"briefs/{p.name}: blocks must be exactly {BLOCKS} in order (found {found})")
    for r in cat["reduce"]:
        if not re.match(r"^R\d+$", r.get("id", "")):
            errs.append(f"reduce step {r.get('id')}: IDs are R1, R2 ...")
        for sid in r.get("needs", []):
            if sid not in seen:
                errs.append(f"reduce {r['id']}: needs unknown session {sid}")
        if r.get("status") not in ("pending", "done"):
            errs.append(f"reduce {r.get('id')}: status must be pending or done")
    if not errs:
        for s in cat["sessions"]:
            try:
                prompt, _n = build_prompt(ctx, s, DRY_RUN_DATE)
            except (KeyError, ValueError) as ex:
                errs.append(f"{s['id']}: prompt assembly failed: {ex}")
                continue
            if "{{" in prompt:
                errs.append(f"{s['id']}: unexpanded placeholder in the prompt")
            if len(prompt) > MAX_PROMPT_CHARS:
                errs.append(f"{s['id']}: prompt is {len(prompt)} characters (limit {MAX_PROMPT_CHARS})")
    return errs


# ---------------------------------------------------------------- tracker
def session_status(s):
    f = session_file(s["id"])
    if s["status"] == "dropped":
        return "dropped"
    if f:
        word = "integrated" if s["status"] == "integrated" else "saved, to integrate"
        return f"{word}: [{f.name[:5]}](../sessions/{f.name})"
    return f"ready (best after {s['run_after']})" if s.get("run_after") else "ready"


def tracker(cat):
    sessions = cat["sessions"]
    states = Counter("dropped" if s["status"] == "dropped" else "integrated" if s["status"] == "integrated"
                     else "saved" if session_file(s["id"]) else "ready" for s in sessions)
    lines = [BEGIN, "",
             f"**{len(sessions)} sessions:** {states['ready']} ready to run, {states['saved']} saved and awaiting "
             f"integration, {states['integrated']} integrated, {states['dropped']} dropped. "
             f"**{len(cat['reduce'])} reduce steps:** {sum(r['status'] == 'done' for r in cat['reduce'])} done.", ""]
    lines += ["| Family | Sessions | Wave 1 | Wave 2 | Wave 3 |", "|---|:---:|:---:|:---:|:---:|"]
    for fam, label in cat["families"].items():
        fs = [s for s in sessions if s["family"] == fam]
        if fs:
            lines.append(f"| {label} | {len(fs)} | " + " | ".join(str(sum(s['wave'] == w for s in fs) or "") for w in (1, 2, 3)) + " |")
    lines += ["", "| Wave | Priority | ID | Session | Family | Verify | Status |", "|:---:|:---:|---|---|---|:---:|---|"]
    for s in sorted(sessions, key=lambda s: (s["wave"], s["id"])):
        lines.append(f"| {s['wave']} | {s['priority']} | {s['id']} | [{s['title']}](briefs/{s['brief']}) | "
                     f"{cat['families'][s['family']]} | {s['verify']} | {session_status(s)} |")
    lines += ["", "| Step | What | Inputs saved | Status |", "|---|---|:---:|---|"]
    for r in cat["reduce"]:
        have = sum(1 for sid in r["needs"] if session_file(sid))
        lines.append(f"| {r['id']} | {r['title']} | {have} of {len(r['needs'])} | {r['status']} |")
    lines += ["", END]
    return "\n".join(lines)


def updated_readme(cat):
    text = README.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        raise SystemExit(f"{README.relative_to(ROOT)}: missing the tracker markers")
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    return head + tracker(cat) + tail


# ---------------------------------------------------------------- report checks
def resolve_report(arg):
    p = Path(arg).expanduser()
    if p.exists():
        return p
    f = session_file(arg)
    if f:
        return f
    raise SystemExit(f"no file {arg}, and no saved session with that ID")


def normalise(text):
    """Tolerate what research tools add: a byte-order mark, Windows line ends, a code fence around the front matter,
    or the front matter indented as it is shown in the protocol."""
    text = text.lstrip("\ufeff").replace("\r\n", "\n")
    text = re.sub(r"\A\s*```(?:ya?ml)?\s*\n(\s*---\n.*?\n\s*---)\s*\n```\s*\n", r"\1\n", text, flags=re.S)
    m = re.match(r"\A\s*\n?( +)---\n(.*?\n)\1---\n", text, re.S)
    if m:
        pad = len(m.group(1))
        inner = "".join(line[pad:] if line.startswith(" " * pad) else line for line in m.group(2).splitlines(True))
        text = "---\n" + inner + "---\n" + text[m.end():]
    return text


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            if k and not k.startswith((" ", "#")):
                out[k.strip()] = v.split("#")[0].strip().strip('"')
    return out


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def ledger_rows(text):
    body = section(text, "Sources & Evidence Ledger") or ""
    return {m.group(1): m.group(0) for m in re.finditer(r"^\|\s*\**(S\d+)\**\s*\|.*$", body, re.M)}


def delta_table(text):
    """{K-number: verdict} from the Repository Deltas table."""
    out = {}
    for line in (section(text, "Repository Deltas") or "").splitlines():
        m = re.match(r"^\|\s*\**(K\d+)\**\s*\|(.*)$", line)
        if m:
            words = {c.strip().strip("*").lower() for c in m.group(2).split("|")}
            out[m.group(1)] = next((w for w in words if w in DELTA_VERDICTS), "")
    return out


def appendix_records(text):
    body = section(text, "Data Appendix") or ""
    records, errs = [], []
    for block in re.findall(r"```jsonl?\s*\n(.*?)```", body, re.S):
        for line in block.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as ex:
                errs.append(f"appendix: not valid JSON ({ex.msg}): {line[:90]}")
                continue
            if not isinstance(rec, dict):
                errs.append(f"appendix: a line is not a JSON object: {line[:90]}")
                continue
            records.append(rec)
    return records, errs


def record_tag(rec):
    key = rec.get("id") or rec.get("name") or rec.get("k") or rec.get("item") or rec.get("subject") or rec.get("employer") or ""
    return f"{rec.get('type') or '?'} record {key}".strip()


def record_errors(rec, sources):
    errs = []
    t, tag = rec.get("type"), record_tag(rec)
    if t not in RECORD_TYPES:
        return [f"{tag}: unknown type {t!r}"]
    for k in ("grade", "src", "as_of"):
        if k not in rec:
            errs.append(f"{tag}: missing \"{k}\"")
    if t not in NO_TTL and "ttl" not in rec:
        errs.append(f"{tag}: missing \"ttl\"")
    if rec.get("grade") not in GRADES or (rec.get("grade") == "E" and t != "absence"):
        errs.append(f"{tag}: grade {rec.get('grade')!r} (A, B, C, D, M or P; E only for absences)")
    if not isinstance(rec.get("src", []), list) or (t != "absence" and not rec.get("src")):
        errs.append(f"{tag}: src must be a non-empty list of ledger IDs")
    else:
        unknown = [s for s in rec.get("src", []) if s not in sources]
        if unknown and sources:
            errs.append(f"{tag}: src {unknown} not in the ledger")
    if rec.get("as_of") and not DATE.match(str(rec["as_of"])):
        errs.append(f"{tag}: as_of must be YYYY-MM-DD")
    if "ttl" in rec and not TTL.match(str(rec["ttl"])):
        errs.append(f"{tag}: ttl must be V0–V6")
    for field in RECORD_TYPES[t]:
        if isinstance(field, tuple):
            if not any(f in rec for f in field):
                errs.append(f"{tag}: needs one of {list(field)}")
        elif field not in rec:
            errs.append(f"{tag}: missing \"{field}\"")
    if "lo" in rec and "hi" not in rec:
        errs.append(f"{tag}: \"lo\" needs \"hi\"")
    for (rt, field), allowed in ENUMS.items():
        if rt == t and field in rec and rec[field] not in allowed:
            errs.append(f"{tag}: {field} {rec[field]!r} is not one of {sorted(allowed)}")
    if t == "tool" and not (isinstance(rec.get("stage"), int) and 0 <= rec["stage"] <= 11):
        errs.append(f"{tag}: stage must be an integer 0–11")
    return errs


def check_report(cat, ctx, path):
    text = normalise(path.read_text(encoding="utf-8"))
    errs, warns = [], []
    fm = front_matter(text)
    sid = fm.get("id", "")
    session = next((s for s in cat["sessions"] if s["id"] == sid), None)
    if not fm:
        errs.append("no front matter (it must open the document, between --- lines, outside any code fence)")
    missing = [k for k in FRONT_MATTER_KEYS if k not in fm]
    if fm and missing:
        errs.append(f"front matter lacks {missing}")
    if not session:
        errs.append(f"front matter id {sid!r} is not a session in the catalogue")
    elif path.parent == SESSIONS and not path.name.startswith(f"{sid}-{session['slug']}"):
        errs.append(f"file name should be {sid}-{session['slug']}.md")
    if fm.get("date") and not DATE.match(fm["date"]):
        errs.append("front matter date must be YYYY-MM-DD")
    for name in SECTIONS:
        if section(text, name) is None:
            errs.append(f"missing section '## {name}'")
    kf = re.findall(r"^\|\s*\*{0,2}KF(\d+)\*{0,2}\s*\|(.*)$", section(text, "Key Findings") or "", re.M)
    if not kf:
        errs.append("Key Findings has no rows numbered KF1, KF2 …")
    graded = 0
    for n, row in kf:
        m = re.search(r"\|\s*\**\s*([A-EMP](?:\s*/\s*[A-EMP])*)\s*\**\s*\|?\s*$", row)
        if not m:
            warns.append(f"KF{n}: no grade in the last column")
        elif re.match(r"[AB]", m.group(1)):
            graded += 1
    if kf and graded < 3:
        warns.append(f"only {graded} Key Findings graded A or B (the quality bar asks for at least three)")
    sources = set(ledger_rows(text))
    if not sources:
        errs.append("the ledger has no rows numbered S1, S2 …")
    records, parse_errs = appendix_records(text)
    errs += parse_errs
    for rec in records:
        errs += record_errors(rec, sources)
    counts = Counter(r.get("type") for r in records)
    if session:
        for t in session["records"]:
            if t != "absence" and not counts.get(t):
                warns.append(f"no {t} records, although the brief asks for them")
        for t, n in min_records(ctx, session).items():
            if counts.get(t, 0) < n:
                warns.append(f"{counts.get(t, 0)} {t} records; the brief asks for at least {n}")
        _, n = build_prompt(ctx, session, DRY_RUN_DATE)
        stated = fm.get("claims_tested", "")
        if stated.isdigit() and int(stated) != n:
            warns.append(f"claims_tested is {stated}, but the brief renders {n} claims from the data as they stand; "
                         "the data changed after the prompt was assembled, so the report's number is used")
            n = int(stated)
        wanted = [f"K{i}" for i in range(1, n + 1)]
        table = delta_table(text)
        extra = {r.get("k"): r.get("verdict") for r in records if r.get("type") == "repo_delta"}
        lacking = [k for k in wanted if k not in table and k not in extra]
        if lacking:
            errs.append(f"no verdict in the Repository Deltas table for {lacking}")
        bad = [k for k in wanted if k in table and not table[k] and k not in extra]
        if bad:
            errs.append(f"Repository Deltas rows without a valid verdict ({sorted(DELTA_VERDICTS)}): {bad}")
    body = prose(text)
    for m in RELATIVE_TIME.finditer(body):
        warns.append(f"relative-time word '{m.group(0)}' (write a date)")
    return errs, warns, counts, len(kf), len(sources)


def verification_packet(cat, path):
    text = normalise(path.read_text(encoding="utf-8"))
    fm = front_matter(text)
    sid = fm.get("id", "?")
    session = next((s for s in cat["sessions"] if s["id"] == sid), None)
    rows = ledger_rows(text)
    records, _ = appendix_records(text)
    items = [f"**KF{n}** |{row}" for n, row in re.findall(r"^\|\s*\*{0,2}KF(\d+)\*{0,2}\s*\|(.*)$", section(text, "Key Findings") or "", re.M)]
    core = [r for r in records if r.get("grade") in ("A", "B") and r.get("type") not in ("repo_delta", "absence")]
    rest = [r for r in records if r not in core and r.get("type") not in ("repo_delta", "absence")]
    extra = []
    if session and session["verify"] == "sample" and rest:
        extra = random.Random(sid).sample(rest, min(SAMPLE_EXTRA, len(rest)))
    items += [f"`{r['type']}` " + json.dumps({k: v for k, v in r.items() if k != "type"}, ensure_ascii=False)[:600]
              for r in core + extra]
    out = [f"## Session under review: {sid}: {fm.get('title', '?')} (dated {fm.get('date', '?')})", "",
           f"{len(items)} items: every Key Finding, every data record graded A or B"
           + (f", and {len(extra)} other records chosen at random" if extra else "")
           + f". Send one batch of up to {BATCH} items per message if the tool struggles with the whole list.", ""]
    for b in range(0, len(items), BATCH):
        out += [f"### Batch {b // BATCH + 1}", ""] + [f"{i}. {x}" for i, x in enumerate(items[b:b + BATCH], b + 1)] + [""]
    cited = sorted({s for r in core + extra for s in r.get("src", [])}
                   | set(re.findall(r"\[(S\d+)\]", section(text, "Key Findings") or "")), key=lambda s: int(s[1:]))
    out += ["### Ledger rows cited above", ""] + [rows.get(s, f"| {s} | (not found in the ledger) |") for s in cited]
    return "\n".join(out)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--update", action="store_true", help="validate and rewrite the tracker block")
    g.add_argument("--check", action="store_true", help="validate; exit 1 if anything is invalid or the tracker is stale")
    g.add_argument("--prompt", metavar="ID", help="print the complete prompt for one session")
    g.add_argument("--next", action="store_true", help="list sessions not yet saved, in recommended order")
    g.add_argument("--appendix", metavar="PATH_OR_ID", help="check a session report and its data appendix")
    g.add_argument("--verify", metavar="PATH_OR_ID", help="print the verification prompt and claim packet for a report")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="research date for --prompt (YYYY-MM-DD)")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # prompts contain non-ASCII text; Windows consoles default to a code page
    cat, ctx = catalogue(), Context()

    if args.update or args.check:
        errs = validate(cat, ctx)
        if errs:
            print("catalogue problems:\n - " + "\n - ".join(errs))
            return 1
        new = updated_readme(cat)
        if args.check:
            if README.read_text(encoding="utf-8") != new:
                print("out of date: research/pipeline-2/README.md (run --update)")
                return 1
            print(f"ok: {len(cat['sessions'])} sessions, {len(cat['reduce'])} reduce steps, tracker current")
            return 0
        README.write_text(new, encoding="utf-8")
        print(f"updated research/pipeline-2/README.md ({len(cat['sessions'])} sessions)")
        return 0

    if args.prompt:
        s = next((s for s in cat["sessions"] if s["id"] == args.prompt), None)
        if not s:
            raise SystemExit(f"no session {args.prompt} in the catalogue")
        if not DATE.match(args.date):
            raise SystemExit("--date must be YYYY-MM-DD")
        if s.get("run_after") and args.date < s["run_after"]:
            print(f"note: {s['id']} is best run after {s['run_after']} "
                  f"({s['params'].get('run_after_reason', 'see the catalogue')})", file=sys.stderr)
        prompt, _ = build_prompt(ctx, s, args.date)
        sys.stdout.write(prompt)
        return 0

    if args.next:
        rank = {p: i for i, p in enumerate(PRIORITIES)}
        todo = [s for s in cat["sessions"] if s["status"] == "ready" and not session_file(s["id"])]
        for s in sorted(todo, key=lambda s: (s["wave"], rank[s["priority"]], s["id"])):
            after = f"  (best after {s['run_after']})" if s.get("run_after") else ""
            print(f"{s['id']}  wave {s['wave']}  {s['priority']}  verify:{s['verify']:<8}  {s['title']}{after}")
        print(f"\n{len(todo)} of {len(cat['sessions'])} sessions not yet saved. "
              "Assemble one with: python3 -B scripts/research_pipeline.py --prompt <ID>")
        return 0

    if args.appendix:
        path = resolve_report(args.appendix)
        errs, warns, counts, n_kf, n_src = check_report(cat, ctx, path)
        print(f"{path.name}: {n_kf} key findings, {n_src} ledger sources, "
              f"{sum(counts.values())} records ({', '.join(f'{k} {v}' for k, v in sorted(counts.items())) or 'none'})")
        for e in errs:
            print(" ERROR  ", e)
        for w in warns:
            print(" warning", w)
        print("PROBLEMS:", len(errs))
        return 1 if errs else 0

    if args.verify:
        path = resolve_report(args.verify)
        text = VERIFY.read_text(encoding="utf-8")
        if PROMPT_MARK not in text:
            raise SystemExit(f"{VERIFY.relative_to(ROOT)}: missing the {PROMPT_MARK} marker")
        sys.stdout.write(text.split(PROMPT_MARK, 1)[1].strip() + "\n\n---\n\n" + verification_packet(cat, path) + "\n")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
