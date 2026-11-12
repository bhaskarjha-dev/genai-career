#!/usr/bin/env python3
"""Findings registry: extracts the key findings of every research session.

Writes data/findings.json (one record per finding: ID, session, number, statement,
evidence grade, exact line, lifecycle stages) and renders research/findings.md, a
one-page map of what the research sessions found, grouped by lifecycle stage and
by session. This is the machine count FAD §17 asked for (gap A2) and the first layer
of distilling the sessions into reusable knowledge.

Parsing: each session's "Key Findings" section (from its heading to the next level-2
heading). A finding is a table row, bold line or heading that starts with an ID such
as KF5, F5 or KF-5. When that section has none, the "Detailed Findings" section is used.

Usage:
    python3 scripts/build_findings.py            # print counts per session
    python3 scripts/build_findings.py --update   # write data/findings.json and research/findings.md
    python3 scripts/build_findings.py --check    # exit 1 if either is out of date

Standard library only.
"""
import argparse
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESSIONS = ROOT / "research" / "sessions"
DATA = ROOT / "data" / "findings.json"
DOC = ROOT / "research" / "findings.md"
STAGES = OrderedDict([
    (1, "Landscape"), (2, "Roles"), (3, "Skills and technology"), (4, "Certifications"), (5, "Portfolio"),
    (6, "Job search"), (7, "Networking"), (8, "Interviewing"), (9, "Compensation"), (10, "Onboarding"),
    (11, "Tracks and transitions"), (0, "Method, tooling and repository design"),
])
# Session -> lifecycle stages (FAD §3.2 primary sessions, plus T0-06/T2-01 to tracks and T0-10/T1-01/T1-02 to method)
SESSION_STAGES = {
    "T0-01": [1, 2], "T0-02": [1, 9], "T0-03": [3], "T0-04": [6], "T0-05": [5, 6], "T0-06": [11], "T0-07": [9, 11],
    "T0-08": [1, 11], "T0-09": [10], "T0-10": [0], "T0-11": [4], "T0-12": [7], "T0-13": [5], "T0-14": [8],
    "T0-15": [1, 2], "T0-16": [2, 3], "T0-17": [9], "T0-18": [9, 11], "T1-01": [0], "T1-02": [0], "T1-03": [8],
    "T2-01": [11],
    "T3-01": [4],
    "T3-02": [4],
}
ID = r"\*{0,2}(?:KF|F|K)?-?(\d{1,2})\*{0,2}"
ROW = re.compile(r"^\|\s*" + ID + r"\s*\|(.*)$")
BOLD = re.compile(r"^\*\*(?:KF|F|K)?-?(\d{1,2})(?=[\s.:·—–)(-])(.*)$")
HEAD = re.compile(r"^#{2,4}\s+(?:\d+\.\d+\s+)?(?:KF|F|K)-?(\d{1,2})\b(.*)$")
GRADE_TXT = re.compile(r"Grade[:\s]*\**\s*([A-E](?:\s*/\s*[A-E])*)\b")
GRADE_MODEL = re.compile(r"Grade[:\s]*\**\s*model\b", re.I)
GRADE_BRACKET = re.compile(r"\[([A-E](?:\s*/\s*[A-E])*)\]|\[([A-E])\b[^\]]{0,60}\]")
GRADE_PAREN = re.compile(r"^\s*\(([A-E](?:/[A-E])?)\)")
LETTERS = re.compile(r"(?<![A-Za-z])([A-E])(?![A-Za-z])")


def grade_of(text):
    """First explicit grade in a piece of text: 'Grade B', '[B/C]', '[A for limits; B ...]' or 'Grade: model'."""
    m = GRADE_TXT.search(text)
    if m:
        return re.sub(r"\s+", "", m.group(1))
    m = GRADE_BRACKET.search(text)
    if m:
        inner = text[m.start():m.end()]
        letters = list(OrderedDict.fromkeys(LETTERS.findall(inner)))
        return "/".join(letters)
    if GRADE_MODEL.search(text):
        return "M"
    return ""


def grade_cell(cell):
    """A short table cell that carries a grade, such as 'B', 'A / B / C', '↑B/C' or 'A (facts) / B (implication)'."""
    c = cell.replace("*", "").strip()
    if not c or len(c) > 40 or len(c.split()) > 6:
        return ""
    letters = list(OrderedDict.fromkeys(LETTERS.findall(c)))
    stripped = LETTERS.sub("", re.sub(r"\([^)]*\)", "", c))
    if letters and not re.search(r"[A-Za-z]{2,}", stripped):
        return "/".join(letters)
    return ""


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            if k and not k.startswith((" ", "#")):
                fm[k.strip()] = v.split("#")[0].strip().strip('"')
    return fm


def section(lines, pattern):
    start = next((i for i, l in enumerate(lines) if re.match(r"^##\s", l) and re.search(pattern, l, re.I)), None)
    if start is None:
        return None, []
    end = next((j for j in range(start + 1, len(lines)) if re.match(r"^##\s", lines[j])), len(lines))
    return start, lines[start + 1:end]


def clean(text):
    text = re.sub(r"`\[[^\]]*\]`", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "").replace("*", "")
    text = re.sub(r"\s+", " ", text).strip(" |·.:—–-")
    return text


def parse(sid, lines):
    out = OrderedDict()
    for name in ("Key Findings", "Detailed Findings"):
        start, body = section(lines, name)
        if start is None:
            continue
        for k, line in enumerate(body):
            n = start + 2 + k
            ahead = " ".join(body[k:k + 4])
            m = ROW.match(line)
            if m:
                cells = [c.strip() for c in m.group(2).split("|")]
                cells = [c for c in cells if c]
                grade = next((g for g in (grade_cell(c) for c in cells) if g), "") or grade_of(m.group(2))
                statement = next((c for c in cells if not grade_cell(c)), "")
            else:
                m = BOLD.match(line) or HEAD.match(line)
                if not m:
                    continue
                rest = m.group(2)
                g = GRADE_PAREN.match(rest)
                grade = g.group(1) if g else grade_of(ahead)
                rest = GRADE_PAREN.sub("", rest)
                statement = re.split(r"\s*\*?\[?Grade[:\s]|\s\[[A-E](?:/[A-E])*\]", rest)[0]
                if "**" in statement:
                    statement = statement.split("**")[0]
            num = int(m.group(1))
            statement = clean(statement)
            if num in out or not statement:
                continue
            out[num] = (statement[:400], grade, n)
        if out:
            break
    return out


def collect():
    records, sessions = [], OrderedDict()
    for p in sorted(SESSIONS.glob("T*.md")):
        sid = p.name[:5]
        text = p.read_text(encoding="utf-8")
        fm = front_matter(text)
        found = parse(sid, text.splitlines())
        sessions[sid] = OrderedDict([("file", p.name), ("title", fm.get("title", "")), ("date", fm.get("date", "")),
                                     ("findings", len(found)), ("stages", SESSION_STAGES.get(sid, [0]))])
        for num, (statement, grade, line) in found.items():
            records.append(OrderedDict([("id", f"{sid}.F{num}"), ("session", sid), ("number", num), ("statement", statement),
                                        ("grade", grade), ("line", line), ("stages", SESSION_STAGES.get(sid, [0]))]))
    return sessions, records


def render(sessions, records):
    grades = Counter((r["grade"] or "ungraded").split("/")[0] for r in records)
    lines = ["---", "id: research.findings", 'title: "Research Findings Registry"', "content_type: reference", "stage: 0",
             "status: published", f"last_verified: {max(s['date'] for s in sessions.values() if s['date'])}",
             f'summary: "Every key finding of the {len(sessions)} research sessions, with its evidence grade and exact line, grouped by lifecycle stage and by session."',
             "sources: [" + ", ".join(sessions) + "]", "generated_by: scripts/build_findings.py", "---", "",
             "<!-- GENERATED by scripts/build_findings.py from research/sessions/. Do not edit by hand. -->", "",
             "# Research Findings Registry", "",
             f"> **{len(records)} key findings from {len(sessions)} research sessions.** Each finding keeps the session's own evidence grade "
             "(EGP-1.0: A/B measured or primary; C small-sample, vendor or practitioner; D judgement) and the exact line where it is stated. "
             "Data: [data/findings.json](../data/findings.json). Sessions are dated snapshots; known errors are listed in [ERRATA.md](ERRATA.md).", "",
             "**Grades:** " + " · ".join(f"{g} {grades[g]}" for g in sorted(grades)) + ".", "",
             "## By lifecycle stage", ""]
    for stage, label in STAGES.items():
        rs = [r for r in records if stage in r["stages"]]
        if not rs:
            continue
        head = f"Stage {stage:02d}: {label}" if stage else label
        anchor = f"stage-{stage:02d}" if stage else "method"
        lines += [f'<a id="{anchor}"></a>', f"### {head} ({len(rs)})", "", "| Finding | Grade | Statement |", "|---|:---:|---|"]
        for r in rs:
            f = sessions[r["session"]]["file"]
            lines.append(f"| [{r['id']}](sessions/{f}) L{r['line']} | {r['grade'] or '—'} | {r['statement'].replace('|', '/')} |")
        lines.append("")
    lines += ["## By session", "", "| Session | Title | Date | Findings | Stages |", "|---|---|---|:---:|---|"]
    for sid, s in sessions.items():
        st = ", ".join(f"{x:02d}" if x else "method" for x in s["stages"])
        lines.append(f"| [{sid}](sessions/{s['file']}) | {s['title'].replace('|', '/')} | {s['date']} | {s['findings']} | {st} |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    sessions, records = collect()
    data = json.dumps(OrderedDict([("schema", "findings/1.0"), ("description", "Key findings of the research sessions, extracted by scripts/build_findings.py"),
                                   ("sessions", sessions), ("findings", records)]), indent=1, ensure_ascii=False) + "\n"
    doc = render(sessions, records)
    if args.update:
        DATA.write_text(data, encoding="utf-8")
        DOC.write_text(doc, encoding="utf-8")
        print(f"wrote {len(records)} findings from {len(sessions)} sessions")
    elif args.check:
        stale = [str(p.relative_to(ROOT)) for p, t in ((DATA, data), (DOC, doc)) if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("out of date: " + ", ".join(stale))
            sys.exit(1)
        print("up to date")
    else:
        for sid, s in sessions.items():
            print(f"{sid} {s['findings']:3d}  {s['title'][:70]}")
        print("total", len(records), dict(Counter(r["grade"] or "?" for r in records)))


if __name__ == "__main__":
    main()
