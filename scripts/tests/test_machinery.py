#!/usr/bin/env python3
"""Tests for the repository machinery: the schema checker, citation checks, the validator's document rules,
the data files against their schemas, a smoke test of the personal gap-analysis tool, and research pipeline 2
(catalogue validation, prompt assembly and the session-report checker).

Run:  python3 -B -m unittest discover -s scripts/tests -v
Standard library only; temporary files go to the system temp directory, never into the repository.
"""
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
sys.dont_write_bytecode = True

import common  # noqa: E402
import validate_docs as vd  # noqa: E402


class SchemaSubset(unittest.TestCase):
    def test_maximum_and_minimum(self):
        sch = {"type": "integer", "minimum": 0, "maximum": 12}
        self.assertEqual(common.schema_errors(5, sch), [])
        self.assertTrue(any("above 12" in e for e in common.schema_errors(13, sch)))
        self.assertTrue(any("below 0" in e for e in common.schema_errors(-1, sch)))

    def test_array_rules(self):
        sch = {"type": "array", "minItems": 1, "maxItems": 2, "uniqueItems": True, "items": {"type": "string"}}
        self.assertEqual(common.schema_errors(["a", "b"], sch), [])
        self.assertTrue(any("at most 2" in e for e in common.schema_errors(["a", "b", "c"], sch)))
        self.assertTrue(any("unique" in e for e in common.schema_errors(["a", "a"], sch)))
        self.assertTrue(any("expected string" in e for e in common.schema_errors([1], sch)))

    def test_unsupported_keyword_is_reported(self):
        sch = {"type": "object", "minProperties": 1}
        errs = common.schema_errors({"a": 1}, sch)
        self.assertTrue(any("unsupported keyword" in e and "minProperties" in e for e in errs), errs)

    def test_ref_and_additional_properties(self):
        sch = {"type": "object", "properties": {"d": {"$ref": "#/$defs/date"}}, "additionalProperties": False,
               "$defs": {"date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"}}}
        self.assertEqual(common.schema_errors({"d": "2026-11-07"}, sch), [])
        self.assertTrue(common.schema_errors({"d": "7 Nov"}, sch))
        self.assertTrue(any("unexpected key" in e for e in common.schema_errors({"d": "2026-11-07", "x": 1}, sch)))


class Citations(unittest.TestCase):
    def setUp(self):
        self.counts = common.session_line_counts()

    def test_valid_references(self):
        self.assertEqual(common.ref_errors("T0-01 L1, L5", self.counts, "t"), [])
        self.assertEqual(common.ref_errors("T0-14 L385–386", self.counts, "t"), [])

    def test_line_past_the_end(self):
        self.assertTrue(common.ref_errors("T0-01 L999999", self.counts, "t"))

    def test_unknown_session(self):
        self.assertTrue(any("not a session" in e for e in common.ref_errors("T9-99 L1", self.counts, "t")))


class DocumentRules(unittest.TestCase):
    """The validator's document checks, run on pages in a temporary tree."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "career").mkdir()
        self._root = vd.ROOT
        vd.ROOT = self.root

    def tearDown(self):
        vd.ROOT = self._root
        self.tmp.cleanup()

    def page(self, name, text):
        path = self.root / "career" / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_relative_time_word_in_prose(self):
        path = self.page("a.md", "Demand is currently high.\n\n```\ncurrently in code is fine\n```\n")
        problems = []
        vd.check_writing(path, problems)
        self.assertEqual(len(problems), 1, problems)

    def test_legacy_handbook_phrase(self):
        path = self.page("b.md", "Use the Talent Bridge Matrix to pick a route.\n")
        problems = []
        vd.check_writing(path, problems)
        self.assertTrue(any("legacy handbook" in p for p in problems), problems)

    def test_dead_end(self):
        path = self.page("c.md", "# A page\n\nNo links here.\n")
        problems = []
        vd.check_dead_end(path, problems)
        self.assertTrue(any("dead end" in p for p in problems), problems)

    def test_guide_pattern(self):
        text = ("---\nid: x\ntitle: \"X\"\ncontent_type: guide\nstage: 6\nstatus: published\nlast_verified: 2026-11-07\n"
                "summary: \"x\"\n---\n\n# X\n\n## The short answer\n\n## Evidence and limits\n\n## Next steps\n")
        path = self.page("d.md", text)
        problems = []
        vd.check_guide_pattern(path, problems)
        self.assertTrue(any("Checklist" in p for p in problems), problems)

    def test_absolute_file_link(self):
        path = self.page("e.md", "See [x](file:///tmp/x.md).\n")
        problems = []
        vd.check_doc(path, problems)
        self.assertTrue(any("file://" in p for p in problems), problems)


class DataFiles(unittest.TestCase):
    """Every data file with a schema validates against it."""

    PAIRS = ["role_scores", "role_titles", "posting_skill_shares", "skills_ontology", "stack_model",
             "project_archetypes", "interview_prompts", "tools"]

    def test_schemas(self):
        for name in self.PAIRS:
            with self.subTest(name=name):
                data = json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))
                schema = json.loads((ROOT / "data" / "schemas" / f"{name}.schema.json").read_text(encoding="utf-8"))
                self.assertEqual(common.schema_errors(data, schema, schema), [])

    def test_every_schema_uses_supported_keywords(self):
        for path in sorted((ROOT / "data" / "schemas").glob("*.json")):
            with self.subTest(schema=path.name):
                self.assertEqual(common.schema_keyword_errors(json.loads(path.read_text(encoding="utf-8"))), [])


class GapAnalysisSmoke(unittest.TestCase):
    def test_template_then_report(self):
        script = SCRIPTS / "gap_analysis.py"
        tpl = subprocess.run([sys.executable, "-B", str(script), "--template", "ai-engineer"],
                             capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(tpl.returncode, 0, tpl.stderr)
        me = json.loads(tpl.stdout)
        me["levels"] = {k: 1 for k in me["levels"]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "me.json"
            path.write_text(json.dumps(me), encoding="utf-8")
            run = subprocess.run([sys.executable, "-B", str(script), str(path)], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("AI Engineer", run.stdout)


class ResearchPipeline(unittest.TestCase):
    """Research pipeline 2: the catalogue validates, prompts assemble, and the report checker catches errors."""

    @classmethod
    def setUpClass(cls):
        import research_pipeline as rp
        cls.rp = rp
        cls.cat = rp.catalogue()
        cls.ctx = rp.Context()

    def session(self, sid):
        return next(s for s in self.cat["sessions"] if s["id"] == sid)

    def test_catalogue_is_valid(self):
        self.assertEqual(self.rp.validate(self.cat, self.ctx), [])

    def test_every_tool_category_has_exactly_one_owner(self):
        owners = [c for s in self.cat["sessions"] for c in s["tool_categories"]]
        self.assertEqual(sorted(owners), sorted(self.ctx.tool_categories))

    def test_prompts_assemble_with_numbered_claims(self):
        for sid in ("T0-19", "T0-28", "T0-37", "T0-48", "T0-65"):
            with self.subTest(session=sid):
                prompt, n = self.rp.build_prompt(self.ctx, self.session(sid), "2026-11-08")
                self.assertNotIn("{{", prompt)
                self.assertGreater(n, 0)
                found = [int(k) for k in re.findall(r"^- K(\d+)\. ", prompt, re.M)]
                self.assertEqual(found, list(range(1, n + 1)))
                self.assertIn("# OUTPUT AND EVIDENCE PROTOCOL", prompt)
                self.assertIn(f"{sid}-{self.session(sid)['slug']}.md", prompt)
                self.assertIn("today is 2026-11-08", prompt)

    def test_front_matter_is_found_when_fenced_or_indented(self):
        fm = "---\nid: \"T0-22\"\ndate: \"2026-11-08\"\n---\n"
        for raw in (fm, "```yaml\n" + fm + "```\n", "".join("    " + line for line in fm.splitlines(True)), "\ufeff" + fm.replace("\n", "\r\n")):
            with self.subTest(raw=raw[:12]):
                self.assertEqual(self.rp.front_matter(self.rp.normalise(raw + "# body\n")).get("id"), "T0-22")

    def report(self, sid, records_extra=(), drop_k=False):
        _, n = self.rp.build_prompt(self.ctx, self.session(sid), "2026-11-08")
        ks = [f"K{i}" for i in range(1, n + 1)]
        if drop_k:
            ks = ks[1:]
        recs = [{"type": "practice", "area": "outreach", "tactic": "short note", "claim": "replies", "evidence": "survey",
                 "verdict": "use-with-care", "grade": "C", "src": ["S1"], "as_of": "2026-11-08", "ttl": "V3"}]
        recs += list(records_extra)
        body = ["---", f'id: "{sid}"', 'title: "t"', 'date: "2026-11-08"', "status: complete", 'topic: "x"',
                'confidence: "medium"', 'temporal_anchor: "2026-11"', 'authored_by_model: "test"',
                'protocol_version: "EGP-1.0"', "---", "", f"# {sid}: t", ""]
        for name in self.rp.SECTIONS:
            body += [f"## {name}", ""]
            if name == "Key Findings":
                body += ["| # | Finding | Key evidence | Grade |", "|---|---|---|---|"]
                body += [f"| **KF{i}** | Finding {i} | [S1] | **B** |" for i in (1, 2, 3)] + [""]
            elif name == "Repository Deltas":
                body += ["| K# | Claim | Verdict | Evidence | Grade |", "|---|---|---|---|---|"]
                body += [f"| {k} | c | confirmed | [S1] | B |" for k in ks] + [""]
            elif name == "Data Appendix":
                body += ["```jsonl"] + [json.dumps(r) if isinstance(r, dict) else r for r in recs] + ["```", ""]
            elif name == "Sources & Evidence Ledger":
                body += ["| # | Source | Published | Retrieved | Grade | Access | Modifiers | Used for |",
                         "|---|---|---|---|---|---|---|---|", "| S1 | A report, https://example.org | 2026-01-01 | 2026-11-08 | B | Read | — | KF1 |", ""]
            else:
                body += ["Text.", ""]
        return "\n".join(body)

    def check(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "draft.md"
            path.write_text(text, encoding="utf-8")
            return self.rp.check_report(self.cat, self.ctx, path)

    def test_report_checker_accepts_a_complete_report(self):
        errs, _warns, counts, n_kf, n_src = self.check(self.report("T0-22"))
        self.assertEqual(errs, [])
        self.assertEqual((n_kf, n_src), (3, 1))
        self.assertEqual(counts["practice"], 1)

    def test_report_checker_catches_errors(self):
        bad = [{"type": "credential", "id": "x", "name": "X", "issuer": "Y", "level": "associate", "state": "live",
                "url": "https://example.org", "ttl": "V2", "grade": "A", "src": ["S9"], "as_of": "2026-11-08"},
               {"type": "measure", "subject": "role:ai-engineer", "measure": "us_postings", "value": 10, "ttl": "V1",
                "grade": "B", "src": ["S1"], "as_of": "8 Nov 2026"},
               {"type": "company", "name": "Z", "employer_type": "unicorn", "hq": "US", "regions": ["US"], "grade": "B",
                "src": ["S1"], "as_of": "2026-11-08"},
               {"type": "pay", "role": "ai-engineer", "location": "US", "stat": "p50", "currency": "USD", "period": "year",
                "basis": "tc", "source_name": "x", "lo": 1, "ttl": "V3", "grade": "B", "src": ["S1"], "as_of": "2026-11-08"},
               "{not json"]
        errs, *_ = self.check(self.report("T0-22", records_extra=bad, drop_k=True))
        joined = " ".join(errs)
        self.assertIn("state 'live'", joined)
        self.assertIn("['S9'] not in the ledger", joined)
        self.assertIn('missing "unit"', joined)
        self.assertIn("as_of must be YYYY-MM-DD", joined)
        self.assertIn('missing "ttl"', joined)
        self.assertIn('"lo" needs "hi"', joined)
        self.assertIn("employer_type 'unicorn'", joined)
        self.assertIn("not valid JSON", joined)
        self.assertIn("no verdict in the Repository Deltas table for ['K1']", joined)


if __name__ == "__main__":
    unittest.main()
