<!--
Research pipeline 2: the verification prompt. scripts/research_pipeline.py --verify <ID or path> prints everything below
the BEGIN PROMPT marker, followed by a packet of the report's load-bearing claims and the ledger rows they cite.
-->

# Verifying a Research Pipeline 2 Session

Every session report is checked before its records change a data file or a guide: decision D-018's rule 6 (an independent check of every figure against its source) applied to new research, as [decision D-021](../DECISIONS.md) sets out. The catalogue marks each session's check as **required** (check every Key Finding and every record graded A or B) or **sample** (the same, plus 20 other records chosen at random). The script prints the items in batches of 25; send one batch per message if the tool struggles with the whole list.

**How to run it**

1. Assemble the prompt: `python3 -B scripts/research_pipeline.py --verify <draft path or session ID> > ~/verify.md`.
2. Paste it into a fresh chat with web access, preferably in a different model family from the one that wrote the report (a Claude report checked by ChatGPT or Gemini, and so on). Attach the full report if the tool allows.
3. Act on the verdict:

| Result (practice-curated thresholds [P]) | Action |
|---|---|
| At least 90% of checked items supported (postings that have closed since the report are left out of the count), and no invented source | Accept. Apply the listed corrections |
| 75–90% supported, and no invented source behind a load-bearing claim | Accept with corrections: drop or downgrade every failed item |
| Below 75% supported, or an invented source behind a load-bearing claim | Re-run the session, or the failing part, with the verifier's findings as context |

**Where the result goes**

- **Before the report is saved** (the normal case): fix the draft (or ask the research tool to correct the failed items), then add the verifier's summary as a final section, `## Verification`, giving the date, the verifying model, the number of items checked and the pass rate. Then save the report in `research/sessions/`. Saved sessions are never edited.
- **After the report is saved:** do not edit it. Log each correction in [research/ERRATA.md](../ERRATA.md), and use the corrected values when integrating.

<!-- BEGIN PROMPT -->

# VERIFICATION BRIEF

You are an independent fact-checker for an evidence-graded knowledge base on careers in generative AI. Another AI research agent wrote the report summarised below. Your job is to find what is wrong with it, not to improve it. Do not ask clarifying questions; proceed with the packet as given.

## Rules

- Grades: A means a primary authoritative source that was opened (official documentation, statute, government guidance, court records, peer-reviewed research, an issuer's own page, an employer's own posting); B means an established secondary source with a transparent method, or a sizeable dataset (platform aggregates such as Levels.fyi, JobsPipe and Fast AI Jobs are always B); C means a vendor, practitioner or single source; D means memory, judgement or a single anecdote; E means unverifiable or not found, and must never be asserted; M means a calculation that inherits its weakest input; P means practice-curated advice that nobody has measured. US LCA wage filings are A for what was filed, never for what people earn. A claim resting only on a search snippet is at most B.
- Never invent. If you cannot open a source, mark it unreachable; do not guess what it says.
- Write dates as YYYY-MM-DD, in British English.

## Task

For every item in the packet:

1. Open each cited source (the ledger rows at the end give the URLs).
2. Give a verdict: **supported**, **partly supported** (say exactly what differs: figure, date, unit, population or wording), **not supported**, **unreachable**, **source does not exist**, or **posting closed** (a job posting that has expired since the report; it does not count against the report).
3. Check the grade against the rules, and give the correct grade if it is wrong.
4. Check the date and whether the fact may have changed since (freshness class: V0 contested status 14 days; V1 monthly series 31 days; V2 product facts 90 days; V3 market estimates 180 days; V4 rules and annual data 365 days).

Then:

5. For the five most load-bearing items (those that would change a ranking, a legal or visa fact, a credential's status or a pay figure), search for contradicting evidence and report what you find.
6. List anything that looks invented: a URL that does not resolve, a document that does not contain the claim, a quotation you cannot find, a credential or programme that does not exist.

## Output

Return one Markdown document:

1. `# Verification of <session id>`, with the date and the model you are.
2. A table: `# | Item | Verdict | What the source says | Correct grade | Note`.
3. A summary: counts by verdict, the pass rate (supported items ÷ items checked, leaving out closed postings), and the list of items to drop, downgrade or correct, each with the exact correction.
4. The falsification results for the five load-bearing items.
5. Suspected inventions, if any.
6. A recommendation: **accept**, **accept with corrections** or **re-run**, with one sentence of reasons.
