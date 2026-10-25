---
id: T0-04
title: "ATS parsing, AI screening layers and cold-inbound funnel math for GenAI engineering resumes (October 2026)"
date: 2026-10-23
status: complete-with-declared-gaps
topic: "Technical audit of resume parsing and automated filtering in Greenhouse, Lever, Ashby, Workday and Taleo/Oracle, plus AI matching layers (Eightfold, Phenom, HiredScore, SeekOut, Beamery) and channel-level conversion benchmarks"
tags: [ats, resume-parsing, textkernel, greenhouse, lever, ashby, workday, taleo, ai-screening, eightfold, phenom, hiredscore, funnel-conversion, referrals, genai-hiring, prompt-injection, latex, pdf-extraction]
informs_decisions:   # assumed: the brief named no downstream decision IDs
  - resume-export-pipeline-and-format-standard
  - application-channel-allocation
  - ats-checker-tool-selection
confidence: medium   # high: vendor-documented mechanics; medium: vendor-published benchmarks; low: parser-engine identity, GenAI-only and Fortune-500-only funnel rates
---

# T0-04: ATS parsing, AI screening layers and funnel math (October 2026)

> **Reading guide.** Evidence grades A to D are defined in the scale at the start of §9 (A = primary source retrieved this session; B = credible secondary source or vendor dataset; C = single marketing source, my own local experiment, or my own arithmetic; D = recalled or inferred; R = refuted, used as a verdict tag). Memory never exceeds D. Markers: **[Derived]** my arithmetic on published rates; **[Local]** my sandbox experiment (§D4, Appendix A); **[Inference]** reasoning beyond what a source states; **[Recalled]** from memory before searching. Source IDs such as `[S07]` point to the ledger in §9. Temporal anchor: 2026-10-23. Sources are paraphrased; no passage is reproduced.

---

## 1. Prior (logged before searching; all [Recalled], Grade D)

| # | Checkable proposition | Credence before | How it was tested |
|---|---|---|---|
| P1 | The ">75% of cold inbound resumes are rejected by automated filters before any human sees them" statistic has no primary-source basis. Deterministic automated rejection is mostly employer-configured knockout rules on application-question answers, not resume-content scoring. | 75% | Origin trace; vendor auto-reject documentation; surveys (§D1) |
| P2 | Standard parsers do garble some two-column or design-tool PDFs, but modern vendor parsers handle ordinary text-layer multi-column files. Hard failures are image-only or flattened PDFs and content in text boxes, headers and footers. | 60% | Vendor documentation; local extractor experiments (§D3, §D4) |
| P3 | In Greenhouse, Lever and Ashby a parse failure leaves the original resume attached and visible, so it is not itself a silent rejection. The real friction is Workday/Taleo-style structured re-entry and knockout questions. | 60% | Vendor documentation (§D2) |
| P4 | Cold inbound application-to-offer for engineering is on the order of 0.2–0.5%. Referrals convert at least 5–15x better per application. Recruiter-sourced candidates sit in between. | 50% | Gem, Ashby and Greenhouse datasets (§D7) |
| P5 | AI-native layers (Eightfold, Phenom, HiredScore, Ashby AI, Greenhouse Talent Matching) rank or recommend by design instead of auto-rejecting. Hidden-text and keyword-stuffing tricks offer no reliable benefit and carry detection risk. | 65% | Vendor documentation; arXiv studies; surveys; local test (§D6, §D1) |

**Recalled engine map (untested, Grade D):** Greenhouse and Lever use Sovren/Textkernel-class parsers; Ashby uses an in-house or LLM-first pipeline; Workday uses a native parser with HiredScore grading on top; Taleo uses an older rules-based parser.

---

## 2. Research Question

> How do the major ATS platforms and AI matching layers ingest, parse, score and filter a GenAI-engineering resume in October 2026; where do silent failures occur and what are their technical root causes; and what is the measured conversion funnel for cold inbound applications versus employee referrals and recruiter outbound?

The six domain probes map to findings as follows.

| Probe | Where answered |
|---|---|
| Which engines power Greenhouse, Lever, Ashby, Workday, and how do they handle modern PDFs? | KF2, KF4, D2, D3 |
| What drives the "Workday black hole", and why do columns and tables corrupt extraction? | KF2, KF5, D2, D4 |
| How do AI layers score relevance, and how are knockouts enforced before human review? | KF1, KF3, KF8, D6 |
| What is the cold-inbound pass-through rate for GenAI roles at startups versus Fortune 500? | KF9, KF11, D7 (partial; gaps declared) |
| Which formatting rules "guarantee 100%" parse accuracy? | D5 (the guarantee is not supportable; see there) |
| What are the channel deltas (inbound, referral, outbound)? | KF10, D7 |

**Scope.** In scope: Greenhouse, Lever, Ashby, Workday, Taleo/Oracle; Textkernel/Sovren/Daxtra parsing; Eightfold, Phenom, HiredScore, SeekOut, Beamery, Greenhouse Talent Matching, Ashby AI review. Out of scope: unverifiable resume hacks and formatting superstition without a parser basis (tested only to falsify).

---

## 3. Key Findings

Verdict tags: CONFIRMED / UPDATED / CONTRADICTED / UNRESOLVED / NEW.

### KF1. The ">75% auto-rejected" statistic is unsupported as stated; deterministic rejection exists, but it is employer-configured and keyed to form answers, not resume prose
The statistic traces to a 2012 sales claim by a resume-optimisation start-up that closed in 2013, not to measured ATS behaviour [S32]. Every named ATS documents auto-reject as a recruiter-configured rule on application-question answers: Greenhouse (Plus and Pro tiers), Ashby, Lever (auto-archive workflows), Workday (condition rules) and Taleo/Oracle (scored disqualification questions) [S03, S05, S08, S11, S13]. None of the documents I retrieved describes rejection triggered by resume wording or by a parse failure. Counter-pressure: screening is heavily automated even without auto-reject. In a vendor survey 53% of US recruiters said they had handed most screening to AI/ATS (self-reported) [S29], and a 2021 Harvard Business School and Accenture survey of 2,275 executives (US, UK, Germany) found that more than 90% of employers using recruiting-management systems rely on them for a first cut or ranking, with 88% agreeing that qualified high-skill candidates are vetted out for not matching exact criteria [S33].
**Verdict: CONFIRMED with nuance** (blanket statistic contradicted; "automation shapes who is read first" supported). **Grade A** (mechanisms) / **B** (origin, surveys).

### KF2. Parsing is convert-then-extract; most failures originate in conversion; vendors document the same triggers
Textkernel's developer documentation says the parser first converts the file to plain text and then analyses that text, and that the vast majority of parsing problems come from the conversion step (images, text not laid out in reading order, rotated text). It flags image-only inputs, gates OCR behind an optional add-on with limits, and advises avoiding PDF where possible to minimise conversion problems (while noting that many PDFs convert fine and that most failure reports involve corrupt PDFs) [S14]. Greenhouse lists practical triggers for an unsuccessful parse: files over 2.5 MB, letter-spaced text, graphics, photos or word-art, image uploads, complex tables, contact data in headers, footers or text boxes, column layouts, missing section structure. The consequence is empty fields and a merely attached file awaiting manual entry [S01]. Workday states that parse results vary with format and word order, advises resumes without images, and says Skills and Languages are not auto-filled [S10]. Lever says image files (JPG/PNG) are not parsed [S02].
**Grade A.** Caveat: Greenhouse's article is written for the recruiter-side upload path; I found no statement on whether the candidate-facing autofill path differs.

### KF3. A parse failure is not a rejection, but parse output now feeds ranking layers, so conversion quality can change who is read first
Greenhouse Talent Matching extracts titles, skills, years of experience, dates and companies from the resume using fine-tuned and third-party LLMs, scores Strong, Good, Partial or Limited, routes unprocessable resumes to "manual review", and states it never advances or rejects anyone [S07]. Workday HiredScore grades from the *parsed* profile; since August 2026 an opt-in LLM mode evaluates each screenable qualification separately, with basic qualifications deciding A/B versus C/D [S12]. Ashby's AI review evaluates resume and application answers against recruiter-written criteria and exposes a sortable "criteria met %" [S04]. Whether a lower grade means "never opened" depends on tenant configuration and queue volume, which no vendor publishes [Inference]. Adoption of these opt-in or metered layers is unknown.
**Grade A** (mechanics) / **D** (prioritisation effect).

### KF4. No vendor-confirmed parser engine was found for Greenhouse, Lever, Ashby or Workday; the recalled Sovren/Textkernel map is unverified; third-party "ATS checker" sites contradict one another
Documented: Greenhouse uses ML models and, for matching, fine-tuned LLMs plus third-party models [S07]. Textkernel sells a parser (70+ formats, optional OCR, optional LLM parser) and lists an Oracle Recruiting Cloud integration [S14, S15]. Oracle's Taleo documentation says resume parsing is delivered through a third-party partner service, as-is, and shows a paste-plain-text path that is parsed to pre-fill applications [S13]; Textkernel and RChilli each list Oracle integrations [S15]. Workday and Ashby documents describe behaviour without naming an engine [S10, S04]. One SEO checker asserts Greenhouse historically used Sovren; another asserts Greenhouse has no match score, which Greenhouse's own Talent Matching documentation contradicts [S07, S36].
**Verdict: UNRESOLVED.** **Grade A** (what is documented) / **D** (engine map).

### KF5. Two-column "garbling" is real but extractor-dependent; no single open-source strategy survives all layouts [Local]
Same resume content, seven extraction modes. Geometry-based extractors (pdfplumber, `pdftotext -layout`, pdfminer on flowing columns) interleaved or scrambled the columns. Even `pdftotext`'s default reading order placed sidebar contact lines inside the Experience block. Stream-order extractors (PyMuPDF, pypdf, `pdftotext -raw`) were clean when the file was written in reading order but scrambled the Experience block when text objects were created in arbitrary order, as design tools may do. Single-column and simple table layouts passed everywhere. These are open-source extractors, not vendor parsers: Textkernel claims multi-column support [S15], while Greenhouse lists column layouts as a failure trigger [S01].
**Grade C** (local) + **A** (Greenhouse list).

### KF6. LaTeX PDFs are not inherently unparseable; failures come from the font-encoding pipeline [Local]
pdfLaTeX with default OT1 Type 1 fonts extracted all six ligature test words intact in all five extractors, which contradicts the folklore that LaTeX ligatures always break ATS parsing. What did break: (a) T1 encoding without scalable fonts produced Type 3 bitmap fonts with no Unicode map, so ligatures were lost ("work ow") and `glyphtounicode` did not repair it, while `cmap` did in four of five extractors; (b) OT1 accented letters extracted as separate marks in four of five extractors ("Jos´e"); (c) XeLaTeX/OpenType emitted the "ff" in "efficient" as the single ligature code point U+FB00, which matches an ASCII keyword only after NFKC normalisation; a font-level `Ligatures=NoCommon` removed it, while a document-wide `\defaultfontfeatures` setting did not; (d) OT1 bullets extracted as the control character U+0088. Public bug trackers show the same ToUnicode failure family in other toolchains [S34].
**Grade C** (local) / **B** (bug trackers).

### KF7. Hidden or white-font text is extracted and measurable; it is unvalidated as a tactic and carries detection risk
In my test all six extractors returned both 1-pt and 10-pt white text, while OCR of the rendered page did not see it [Local]. A May 2026 measurement on production screening corpora found hidden injections in about 1% of 196,682 resumes, over 90% of them keyword-style "data" injections, and reported detectors with roughly 86–93% precision; it explicitly did not measure whether injections change outcomes [S30]. A small controlled lab study (ten resumes, two LLMs, raw text) found ranking gains when few candidates inject and near-zero gains when most do [S31]. In Greenhouse's survey 40% of US candidates said they had used prompt injection [S29]. Neither "always works" nor "never works" is evidenced in production; the expected value looks negative given detection and fraud-flag exposure [Inference, D].
**Grade A/B** (measurement) / **C** (local).

### KF8. AI layers score explicit recruiter-visible criteria plus learned similarity; vendors say they never auto-reject, but several expose sortable rankings, and two high-profile suits allege de-facto exclusion
Eightfold: embeddings plus hundreds of features (recency-weighted skill overlap, title similarity and predicted next title, company and industry similarity, "hireability"), trained on historical candidate-position outcomes, output as 0–5 in half-point steps [S16]. Phenom: grades from recruiter-set skills, experience, title and location, with must-have versus preferred skills and learning from outcomes and feedback [S18]. Workday HiredScore: A–D grades [S12]. Greenhouse: four match levels from extracted resume facts, validated by back-testing against past advance decisions [S07]. Ashby: per-criterion meets, does not meet or undecided, with citations and PII redaction [S04]. SeekOut: scorecards with Yes, Partial or No criteria and an explicit statement that candidates are never auto-rejected [S19]. Ranking weights are proprietary, and I found no independent validation beyond vendor-commissioned bias audits [S18, S20]. Pending litigation: *Kistler v. Eightfold* (motion to dismiss submitted, no ruling as of 1 October 2026) [S21] and *Mobley v. Workday* (discovery; partial motion-to-dismiss ruling in June 2026) [S22]. Both are allegations, not findings.
**Grade A** (self-described mechanics) / **B** (litigation status).

### KF9. Cold-inbound engineering funnel: about 0.2% application-to-hire, roughly 340–380 applications per offer and 460–520 per hire; 3.6–6% reach a first human stage
Gem's engineering chain (6% to pre-onsite, 17% to onsite, 29% to offer, 73% accept) multiplies to 0.22% [Derived; S24, S28]. Ashby's technical Q1-2026 rates (3.6% to interview, 7.3% interview-to-offer, 73% accept) give 0.19% [Derived; S28, S39]. Gem prints 0.2% for engineering [S24]. Two independent datasets converge. Over 2021→2025 Gem's application-to-pre-onsite rate fell from 13% to 8% across all functions [S28]. Greenhouse reports applications per job up roughly 110% (116 to 244) and applications per recruiter up 204% (1,610 to 4,890 per year) from 2022 to 2025 [S27]. **Unresolved:** the company-size table on the same Gem page (startups 12/58/22/84; enterprises 28/31/14/80) multiplies to 1.3% and 1.0%, which is 5–6x the 0.2% headline, so I do not use it to compare startups with enterprises. No GenAI-only or Fortune-500-only funnel was found.
**Grade B** (inputs) with [Derived] arithmetic.

### KF10. Channel deltas are large and cross-validate: sourced about 8x inbound; referral about 11–36x inbound per application, depending on the metric
Ashby (38M applications, 2021–2024): application-to-interview 3% inbound, 25% sourced, 40% referral, 42% internal and agency; interview-to-offer 6%, 6%, 16% (referral), 32% (internal). Derived offers per 1,000 applications: about 1.8 inbound, 15 sourced, 64 referral [Derived; S25]. Ashby's own quoted offer rates (0.2% inbound versus 7.3% referral) imply 36x [S25]. Gem reports referrals at 11x and sourced at about 8x inbound for hires per application [S23, S24]. The 8x sourced figure matches my 8.3x derived from Ashby's stage rates [Derived]. In Gem's engineering data referrals are about 2% of applications but 18.7% of hires; job boards are about 40% of applications but 21.9% of hires [S24]. These are selection effects (someone vouched, or a recruiter pre-screened), not formatting effects.
**Grade B.**

### KF11. GenAI-specific funnel data are not published; proxies show non-inbound channels carry much of the hiring for AI-titled roles, and fraud or spam dilutes cold-inbound averages
Ashby (July 2026), technical roles with "AI" in the title: 37.1% of hires from inbound, 28.0% from sourcing, 9.2% from agencies, so about 26% from referral, internal and other by subtraction [S26; figures read from chart text]. Gem: engineering 0.2% and data science 0.1% application-to-hire; 35–36 interviews per engineering hire [S24]. In a Greenhouse pilot for a Machine Learning role, more than 35% of applicants carried high-risk fraud signals and 91% of the high-risk candidates that were reviewed were confirmed fraudulent [S09]. The signals derive from phone, email, IP and location [S09]. Population-average odds therefore understate those of a genuine, well-matched applicant, by an amount nobody has published [Inference].
**Grade B** / gap declared.

### KF12. "ATS score" checkers are keyword or rule simulations with no demonstrated link to real ATS outputs; extractors and vendor parser demos are the defensible checks
Jobscan describes a match rate from comparing resume text with a posting and, per a third-party summary of its own statements, says its scanner uses a parsing engine of the kind many ATS use; neither claim is independently validated [S36]. None of the Greenhouse, Lever, Ashby or Workday documents I retrieved describes a keyword-match percentage computed on the resume; the score-bearing features are Talent Matching, AI review, HiredScore and similar layers [S04, S07, S12]. I found no independent study showing that checker scores predict ATS ranking or interview rates. An average parser pass rate of about 91% claimed by one comparison site is unverifiable [S36].
**Grade C** with an honest gap.

### Confidence by area

| Area | Confidence | Why |
|---|---|---|
| Vendor-documented parse triggers and auto-reject mechanisms | High | Primary vendor pages (A) |
| Parser engine identity per ATS | Low | Not vendor-confirmed anywhere I searched |
| Layout and encoding failure mechanics | Medium | Reproducible, but open-source extractors only |
| Funnel rates, engineering overall | Medium | Two datasets converge; vendor customer bases are tech-forward |
| Startup versus enterprise, GenAI-only, Fortune-500 funnel | Low | Conflicting or missing |
| AI-layer ranking criteria | Medium (what is scored), Low (weights, effect) | Self-described by vendors; no independent validation |

---

## 4. Recommendation

**Decision framed:** how to prepare and route GenAI-engineering applications given what parsers, AI layers and funnels actually do. Each action cites the findings it rests on and its evidence grade.

| # | Action | Rests on | Grade |
|---|---|---|---|
| R1 | **Budget cold inbound as a roughly 0.2% per-application channel** (about one offer per 340–380 applications at population-average odds). Use it for high-fit roles only. Put the saved hours into channels with 8–36x per-application yield: referrals, recruiter-sourced or outbound discovery, and re-discovery inside ATS databases (Gem reports 46% of sourced engineering hires were already in the ATS [S24]). Treat 0.2% as a planning floor, not a personal forecast (see objection 3 in §7). | KF9, KF10, KF11 | B |
| R2 | **Keep two artifacts.** (a) A *portal resume*: single column, real text layer (a verified text-layer PDF, with a clean single-column DOCX variant ready), standard plain-case headings, contact block as body text, dates on the same line as title and employer. (b) A designed resume for humans and referral emails. Do not submit (b) to a portal unless it passes the D5 checks. | KF2, KF5 | A (triggers) / C (local) |
| R3 | **Verify the portal resume before every new template or toolchain**: `pdffonts` (no Type 3 rows, Unicode map present), two extractors read in order, NFKC and control-character check, copy-paste test. After submitting, read the parsed fields on each ATS review page and fix them by hand. Workday never auto-fills Skills or Languages. | KF2, KF6, D5 | A / C |
| R4 | **Write for criteria-based evaluators.** For each requirement in the posting, put one verifiable evidence line in a *recent* role (what, where, when, scale, tools). Keep the skills list consistent with those bullets and keep dates explicit. | KF3, KF8 | A (mechanics) / D (the advice itself is inference) |
| R5 | **Answer every knockout question exactly and completely.** Form-answer rules are the only documented deterministic rejection path, and Ashby's AI review treats a blank or unrelated long-form answer as unmet. Where a threshold cannot be met honestly (for example a years-of-experience cut-off on a technology that is only a few years old), a referral or direct outreach routes around form-based rules: Ashby's documentation confirms that applications submitted through an application-request link skip its auto-reject and application-limit rules [S06]; for other systems this is inference. | KF1, KF3 | A / D |
| R6 | **No hidden text, no keyword blocks, no mass auto-apply.** Detection exists, effect is unmeasured in production, fraud signals and application limits exist, and the funnel math does not reward volume. Use "ATS score" tools only as a posting-gap list, never as a pass/fail gate. | KF7, KF9, KF11, KF12 | A/B |
| R7 | **Reduce false fraud flags**: stable real email address and mobile number, no VPN or disposable email during applications, consistent identity across resume, LinkedIn and GitHub. | KF11 | D (inferred from the documented signal types) |
| R8 | **Do not chase "100% parse accuracy across four ATS".** No source supports a guarantee; Workday itself says results vary. The achievable standard is: no documented trigger present, passes at least two extractors, parsed fields verified after submission. | KF2, KF4 | A |
| R9 | **Re-test quarterly and extend the evidence.** Vendors change behaviour often (Workday's HiredScore LLM mode is an August 2026 opt-in; Greenhouse's parse article was updated in March 2026). Obtain a vendor parser demo or sandbox and run the §D4 corpus through it. That test was not possible here. | §7 | n/a |

**What would change this recommendation**
- A vendor-parser test showing multi-column files parse correctly would relax the layout rule for those employers, but not for triggers Greenhouse documents.
- Evidence that Workday, Taleo or Ashby reject on parse failure would raise the priority of R3.
- A published GenAI-only funnel with materially higher inbound conversion (for example above 1%) would raise the inbound budget in R1.
- Rulings or disclosures in *Kistler* or *Mobley* that expose ranking criteria or automated exclusion rates.

**Confidence:** medium-high for R2, R3, R5, R6, R8; medium for R1 and R4; low for R7.

---

## 5. Alternatives Considered

| Alternative | Verdict | Reasoning | Evidence |
|---|---|---|---|
| A. Optimise to an "ATS score" (Jobscan- or Teal-style 75–80% match) | Reject as a gate; keep as a posting-gap list | Scores are keyword simulations. No vendor document I retrieved describes such a score on the resume. No validation study found. | KF12, [S36] |
| B. DOCX instead of PDF as the universal default | Not adopted as a universal rule; upload whichever format the portal parses correctly, starting from a verified text-layer PDF with a clean single-column DOCX ready | Only Textkernel's developer documentation takes a position: it advises avoiding PDF to minimise conversion problems, while saying many PDFs convert fine and most failures involve corrupt files [S14]. Greenhouse, Workday and Lever do not rank formats. In my test a body-paragraphs-only DOCX reader dropped header, table and text-box content. | [S14], [S01], [S10], [Local] E5 |
| C. Plain-text or pasted resume everywhere | Use as a fallback (Taleo paste path, failed autofill) | Highest parse fidelity, poor for human readers. Taleo documents a paste-and-parse path. | [S13], [S14] |
| D. Design-tool template (Canva and similar) as the portal resume | Reject until the exported file passes D5 | Canva's official help is silent on text-layer retention; third-party claims conflict; a "flatten" option exists in third-party tutorials. | [S35] (gap) |
| E. LaTeX template | Acceptable when built by the XeLaTeX route (or pdfLaTeX with `cmap` and scalable fonts) and verified | Default OT1 ligatures extracted fine; Type 3, accent, ff-ligature and bullet pitfalls exist. | KF6 |
| F. Hidden keyword block or prompt-injection text | Reject | About 1% prevalence with working detectors; production effect unmeasured; fraud-flag exposure. | KF7 |
| G. Mass auto-apply | Reject | About 0.2% average conversion; application limits and fraud signals exist; AI-generated volume is what screening layers are being tuned against. | KF9, KF11, [S06], [S09] |
| H. Referral and outbound-first strategy | Adopt as primary | 8–36x per-application yield. | KF10 |
| I. Wait for vendor transparency or regulation | Reject | *Kistler* and *Mobley* are unresolved with no ruling timeline. | [S21], [S22] |

---

## 6. Detailed Findings

### D1. Myth ledger: what was tested and what survived

The brief's unverified known-claim has two halves: ">75% auto-rejected before human review" and "two-column and Canva layouts parse as garbled strings". Results: the first is **not supported as a blanket statistic**; the second is **partly true and extractor-dependent**, with Canva **unverified**.

| Claim | Test performed | Result | Verdict | Grade |
|---|---|---|---|---|
| More than 75% of resumes are auto-rejected before a human sees them | Origin trace; vendor auto-reject documentation; surveys | Origin is a 2012 sales claim by a start-up that shut down in 2013; an investigator traced the citation chain through career sites and business press back to it [S32]. Vendor auto-reject exists but runs on form answers [S03, S05, S08, S11]. | Unsupported as stated | B (origin) / A (mechanisms) |
| An ATS rejects resumes it cannot parse | Greenhouse, Workday, Lever, Talent Matching documentation | Greenhouse leaves fields empty and attaches the file [S01]; Talent Matching sends unprocessable resumes to manual review [S07]; Workday and Lever documents describe unpopulated fields or varying results, not rejection [S10, S02]. Ashby and Taleo parse-failure behaviour: not documented in retrieved pages. | Not supported for the vendors documented; gap for Ashby and Taleo | A |
| Two-column layouts are garbled by standard parsers | Seven extraction modes over four layouts; vendor documents | Extractor-dependent: interleaving with geometry-based extractors, scrambling with stream-order extractors when export order is arbitrary (D4). Greenhouse lists columns as a trigger; Textkernel claims support [S01, S15]. | Partly true; avoid columns | C + A |
| Canva templates parse as garbage | Canva help pages; third-party guides | Canva's download-file-types and PDF-import help pages do not say whether exported text stays a text layer; the import page mentions "flattened" text (text turned into an image) in an import context. Third-party guides conflict on which export option keeps text. | Unverified, not refuted; test the exported file | D / C (gap) |
| LaTeX PDFs break ATS parsing because of ligatures | pdfLaTeX, XeLaTeX variants, five extractors | Default OT1 ligatures extracted intact; failures came from Type 3 fonts, accent composition, the ff-ligature code point and bullet glyphs (D4). | Conditional, not inherent | C |
| White-font keywords boost ranking | arXiv measurement and lab study; local extraction test | Extracted by all six extractors; about 1% prevalence; detectors exist; production effect unmeasured; lab gain collapses when widespread [S30, S31]. | Unvalidated; avoid | A/B + C |
| A high "ATS score" (for example 80%+) is needed to pass | Vendor documents; tool pages | No retrieved vendor document describes a keyword-match percentage on the resume; the score-bearing layers are Talent Matching, AI review, HiredScore, Eightfold, Phenom. | Unsupported | C |
| PDF is universally safer than DOCX, or the reverse | Textkernel documentation; Greenhouse and Workday documents; local DOCX test | Only Textkernel's documentation takes a position: it advises avoiding PDF to minimise conversion problems, while saying many PDFs convert fine and most failures involve corrupt files [S14]. Greenhouse, Workday and Lever do not rank formats. A body-only DOCX reader dropped header, table and text-box content in my test. | Unresolved; verify per portal | B + C |
| "98% of Fortune 500 companies use an ATS, so filtering is universal" | Third-party restatements of a Jobscan usage report | Adoption is not auto-filtering. | Non sequitur | C |
| Referral candidates are 10x or more likely to be hired | Gem and Ashby datasets | 11x (Gem, hires per application) to 36x (Ashby, offers per application, derived); selection effects apply. | Supported, not causal | B |

**What automated exclusion or de-prioritisation actually looks like (documented or inferred)**
1. *Knockout and auto-reject rules* on form answers, configured per job [S03, S05, S08, S11, S13]. Rules attach to application forms, so candidates who enter another way do not pass through them: Ashby's documentation states that applications submitted through an application-request link are not checked against auto-reject or application-limit rules [S06]; for other systems this is inference.
2. *AI grade or rank prioritisation* where a tenant enables it (HiredScore, Talent Matching, Ashby AI review, Eightfold, Phenom). Effect on "who is opened" depends on queue volume and recruiter practice [Inference].
3. *Fraud and spam flags* (phone, email, IP, location signals) in Greenhouse Real Talent [S09].
4. *Capacity*: 4,890 applications per recruiter per year in Greenhouse's 2025 data means many applications are skimmed or never opened regardless of software [S27].

### D2. Vendor-by-vendor audit

| Vendor | Parse and extraction (documented) | Documented failure triggers and consequence | AI or scoring layer | Auto-reject or knockout mechanism | Grade |
|---|---|---|---|---|---|
| **Greenhouse** | ML-based parse fills candidate fields. Talent Matching extracts titles, skills, years of experience, dates and companies with fine-tuned LLMs plus third-party models [S07]. | Files over 2.5 MB, letter-spaced text, graphics, photos or word-art, image uploads, complex tables, headers, footers, text boxes, column layouts, no clear sections, incomplete titles. Consequence: file attached, fields left for manual entry [S01]. For Talent Matching an unprocessable resume goes to manual review [S07]. | Talent Matching (Real Talent add-on): Strong, Good, Partial or Limited; never advances or rejects; hidden after the initial review stage; criteria weighted by the recruiter [S07]. Fraud signals [S09]. | Auto-Reject on answers to Yes/No, single-select or multi-select application questions (Plus and Pro tiers); people subscribed to new-application alerts are not notified of auto-rejected applicants; Auto-Tag and Auto-Advance also exist [S08]. | A |
| **Lever** | Help-centre extract: parser extracts basic fields (name, organization, contact details); image files (JPG, PNG) are not parsed; parsing is not run for some import paths (email, Chrome extension, API) [S02]. Page body could not be fetched (script-rendered); evidence is the search-engine extract. | Image-only files leave fields unpopulated [S02]. | Lever AI features: not retrieved (gap). | Automation workflows (LeverTRM for Enterprise or the Advanced Automation add-on) can auto-archive when an application form is submitted, optionally with a rejection email; Lever's recipe page includes a knock-out recipe on questions such as right to work or years of experience; a 2020 release announced "auto-screening" to disqualify candidates who miss requirements [S03]. | A (extract) |
| **Ashby** | No parser or engine documentation found. AI review reads the resume against criteria [S04]. | Not documented. In AI review a blank or unrelated long-form answer is marked as not meeting its criterion [S04]. | AI-Assisted Application Review: per-criterion meets, does not meet, or undecided; citations; PII redacted before model calls; sortable "criteria met %"; metered credits; evaluations can be hidden for candidates who did not pass through the hosted application path with its legal notice [S04]. | Auto-Reject on form answers (Foundations, Plus, Enterprise tiers), global rules at Enterprise; rules run only when the application is submitted, on new applications, in listed order [S05]. Application Requests (Plus, Enterprise) let recruiters collect form data from referred or sourced candidates, and applications submitted through a request link are not checked against auto-reject or application-limit rules; Application Limits throttle repeat applications [S06]. | A |
| **Workday** | Resume parsing populates fields for review; no engine named [S10]. | Results vary with format and word order; resumes without images work best; Skills and Languages (and hidden fields) are not populated; a template can hide parsing from external candidates [S10]. | HiredScore: A–D grades from the parsed profile; since 5 Aug 2026 an opt-in LLM mode evaluates each screenable qualification separately, and basic qualifications decide A/B versus C/D [S12]. | Condition rules auto-advance or auto-decline, evaluated in order, for example on eligibility answers [S11]. | A |
| **Taleo / Oracle** | Oracle's Taleo documentation says resume parsing is delivered by a third-party partner service, as-is; candidates on mobile can paste a plain-text resume that is parsed to pre-fill the application [S13]. Textkernel and RChilli each list Oracle integrations [S15]. | Not documented in retrieved pages. | Not researched beyond the above. | Taleo Enterprise and Oracle Recruiting both document scored disqualification questions; in Oracle Recruiting a single negative-scored answer disqualifies automatically [S13]. | A (Taleo and Oracle docs) / B (vendor integration pages) |

**Unpacking the "Workday black hole".** The label bundles several distinct mechanisms, and I found no measured Workday response-rate dataset, so it is a composite description, not a measured phenomenon.
1. *Re-entry friction.* Parsing is partial and varies with layout; Skills and Languages are never auto-filled; parsing can be hidden entirely by template [S10].
2. *Rule-based dispositions.* Tenant-defined condition rules can decline at submission or at later steps [S11].
3. *Grade-based queues.* HiredScore grades from the parsed profile feed recruiter views, with an LLM option since August 2026 [S12].
4. *Volume.* Cross-vendor data show applications per recruiter roughly tripled between 2022 and 2025 [S27].
5. *No feedback loop.* Silence after a rejection is a process choice, not a parser effect [Inference].

**Not found after searching** (parser engine per vendor): Greenhouse, Lever, Ashby and Workday support and developer pages; Textkernel's integration and partner pages; Oracle documentation. Only Oracle Recruiting Cloud has a vendor-listed Textkernel integration.

### D3. Parser architecture: what the engineering documentation actually says

```
file (PDF / DOCX / image)
  └─ stage 1: conversion to plain text (layout analysis; OCR only if enabled)   <- most failures [S14]
       └─ usability check (image-only? no text? implausible word lengths?)
            └─ stage 2: field extraction (rules or ML, optionally an LLM) -> structured profile
                 ├─ autofill and recruiter-visible fields (Greenhouse, Workday, Lever)
                 └─ AI layers read the profile or the resume text
                    (Talent Matching, HiredScore, Ashby AI review, Eightfold, Phenom)
```
*A composite of documented stages, not any one vendor's architecture [Inference].*

- **Two stages, errors concentrated in the first.** Textkernel says the parser converts to plain text first, then analyses; the vast majority of problems come from conversion, not from analysing clean text. It calls PDF a format that often hides problems, because the way a page looks is not how its text is stored. It notes candidates sometimes use images, diagonal or vertical text [S14].
- **Conversion diagnostics.** Textkernel returns conversion result codes: image-only documents (ovIsImage), no usable text (ovNoText), corrupt files, timeouts, and warnings such as an implausibly short average word length (ovAvgWordLengthLessThan4), so a bad conversion is detectable before parsing [S14].
- **Format advice.** Textkernel's getting-started page advises avoiding PDF where possible to minimise conversion problems, while stating that many PDFs convert fine and that most failure reports involve corrupt PDFs [S14]. It is guidance for integrators of its own parser, not a statement about Greenhouse, Lever, Ashby or Workday.
- **OCR is an add-on with limits.** Textkernel's platform documentation says about 5% of documents need OCR, that OCR is limited to 10 pages and stops after 120 seconds, and that images take considerably longer [S14]. My OCR test shows why accuracy still matters: at 100 dpi only 7 of 11 key tokens came back exact, at 150–300 dpi 10 of 11 [Local, E4d].
- **LLM parser.** Textkernel offers it as a per-request option at extra cost, falls back to the standard parser, and documents limits (some description fields are not returned; hallucination is possible) [S14]. Greenhouse's matching uses a series of fine-tuned LLMs, each for one extraction task, plus third-party models [S07]. Ashby's review uses LLM evaluation against criteria [S04]. None of these documents says whether the PDF-to-text conversion step changed; I treat stage-1 conversion as a shared risk across classic and LLM pipelines [Inference, D].
- **Vendor concentration.** Textkernel advertises very large annual parsing volume and multi-column support [S15]; that the Sovren parser is now offered by Textkernel is recalled, not re-verified [Recalled]. Another HR system's documentation (outside scope) names Sovren as its parser and says test or fake data may be rejected (read in an earlier extract, not re-verified) [S38]. Oracle's own Taleo documentation and the integration pages of Textkernel and RChilli [S13, S15] fit the same pattern: parsing is commonly bought in from a small set of specialist vendors. That supports "a few shared engines sit behind many ATS products" as a pattern, but not any specific mapping to the four ATS in scope.

### D4. Local extraction experiments [Local, Grade C; ledger S40]

**Purpose and limits.** These tests isolate the mechanisms behind the triggers vendors document. They do **not** measure vendor parsers: vendor engines add layout analysis, OCR and ML on top of conversion, and may behave differently on every row below.

**Environment.** Ubuntu 24.04 sandbox; pdfTeX 1.40.25 and XeTeX (TeX Live 2023); poppler `pdftotext` 24.02.0; PyMuPDF 2.0 (pip); pypdf 5.9.0; pdfminer.six 20251230; pdfplumber 0.11.9; Tesseract 5.3.4; LibreOffice 24.2.7.2 (headless); python-docx 1.2.0; Python 3.12.3. `lmodern` and `cm-super` were not installed, which is why requesting T1 encoding produced Type 3 bitmap fonts. LuaLaTeX did not compile in the sandbox (missing font metrics) and is excluded. Sandbox network access was limited to package registries, so no vendor parser or demo endpoint could be called.

**Method.** One synthetic resume (fictional "José Núñez", GenAI engineer, two roles, education, skills). Eleven target tokens: six ligature-sensitive words (workflow, workflows, Fine-tuned, efficient, flagship, Certified), the accented name, email, phone, a job title and "PyTorch". A token counts as intact if it appears verbatim after whitespace collapsing. Layout tests use anchor strings in expected order and count sidebar lines that land inside the Experience block.

#### E1. Encoding and ligatures (LaTeX variants; five extractors)
Cells list results for pdftotext / PyMuPDF / pdfminer.six / pypdf / pdfplumber, in that order.

| Variant | Fonts in the PDF | Ligature words intact (of 6) | Name "José Núñez" |
|---|---|---|---|
| L1 pdfLaTeX, OT1 default | Type 1 (plus one Type 3 font without a Unicode map) | 6 / 6 / 6 / 6 / 6 | decomposed (matches after NFC) / damaged / damaged / damaged / damaged |
| L2 OT1 + `glyphtounicode` | same as L1 | 6 / 6 / 6 / 6 / 6 | same as L1 |
| L3 pdfLaTeX, T1, no scalable T1 fonts installed | Type 3 bitmap fonts, no Unicode map | 1 / 1 / 1 / 1 / 1 | intact / intact / damaged / intact / damaged |
| L4 T1 + `glyphtounicode` | same as L3 | 1 / 1 / 1 / 1 / 1 | same as L3 |
| L5 OT1 + `cmap` | same as L1 | 6 / 6 / 6 / 6 / 6 | same as L1 |
| L6 T1 + `cmap` | Type 3 | 6 / 6 / 6 / **3** / 6 | intact in all five |
| L7 XeLaTeX + fontspec (OpenType) | CID Type 0C, Unicode map present | 5 / 5 / 5 / 5 / 5 | intact in all five |
| L10 XeLaTeX + font-level `Ligatures=NoCommon` | CID Type 0C, Unicode map present | 6 / 6 / 6 / 6 / 6 | intact in all five |

```text
L3 (T1, Type 3), pdftotext:    "... Built a RAG work ow serving 2M queri..."
L3 (T1, Type 3), pdfplumber:   "... Built a RAG work(cid:29)ow serving 2M quer..."
L1 (OT1), pdfplumber, name:    "Jos´e Nu´n˜ez"
L1 (OT1), pypdf, name:         "Jos´ e N´ u˜ nez"
L7 (XeLaTeX), all extractors:  "... eﬀicient ..."    <- U+FB00 (ff ligature) followed by "icient"
```

Readings:
- **Folklore not reproduced:** default pdfLaTeX output (Type 1 fonts with Unicode maps) kept every ligature word intact in all five extractors.
- **Type 3 bitmap fonts** (T1 requested without scalable fonts) lose fi, fl and ffi. `glyphtounicode` did not repair this; `cmap` did in four of five extractors (pypdf inserted spaces inside words).
- **Accents:** OT1 builds accented letters from separate accent and base glyphs; four of five extractors damaged the name, and pdftotext returned a decomposed form that matches only after NFC normalisation.
- **ff ligature code point:** XeLaTeX with Latin Modern emitted U+FB00 inside "efficient", so an ASCII keyword match fails without NFKC normalisation. Setting `Ligatures=NoCommon` on the font (`\setmainfont{Latin Modern Roman}[Ligatures=NoCommon]`) fixed all five extractors; a document-wide `\defaultfontfeatures{Ligatures=NoCommon}` did **not** (the default font had already been loaded).
- **Bullets:** with OT1, `\item` bullets extracted as the control character U+0088 in pdftotext and as `(cid:136)` in pdfplumber. XeLaTeX bullets extracted as "•".
- Not tested: pdfLaTeX with `lmodern` (package unavailable in the sandbox) and LuaLaTeX.

#### E2. Layout (XeLaTeX-generated PDFs, which isolate layout from encoding; seven extraction modes)

| Layout | pdftotext | pdftotext -raw | pdftotext -layout | PyMuPDF | pdfminer.six | pypdf | pdfplumber |
|---|---|---|---|---|---|---|---|
| X1 single column | clean | clean | clean | clean | clean | clean | clean |
| X2 sidebar (two side-by-side blocks) | 3 sidebar lines inside Experience | clean | 3 sidebar lines inside Experience | clean | clean | clean | lines merged across columns |
| X3 table, dates in left cell | clean | clean | clean | clean | clean | clean | clean |
| X4 two flowing columns | in order | in order | scrambled | in order | scrambled | in order | scrambled |

```text
pdftotext (default), X2:          pdfplumber, X2:
  José Núñez                        José Núñez EXPERIENCE
  EXPERIENCE                        CONTACT Senior Machine Learning Engineer Jan 2024 – Present
  CONTACT                           jose.nunez@example.com Northwind Labs, San Francisco, CA
  jose.nunez@example.com            +1 415 555 0142
  +1 415 555 0142                   • Built a RAG workflow serving 2M queries/day with p95 latency under
  github.com/josenunez              github.com/josenunez
  linkedin.com/in/josenunez         800 ms.
  Senior Machine Learning Engineer  linkedin.com/in/josenunez
```
TeX writes each block in reading order, so stream-order extractors stay clean; geometry-based ones re-sort by position and mix the blocks. In the default pdftotext output the contact block sits between the "EXPERIENCE" heading and the first job, which could attach contact lines to the wrong section, and the first role's date arrives after the sidebar.

#### E3. Export order (emulating a design-tool PDF; two row-aligned columns drawn with ReportLab)
This emulates a design export; it is **not** a Canva export (not testable here).

| Order in which text objects were written | pdftotext | pdftotext -raw | pdftotext -layout | PyMuPDF | pdfminer.six | pypdf | pdfplumber |
|---|---|---|---|---|---|---|---|
| D1 column by column (reading order) | 6 sidebar lines inside Experience | clean | 6 sidebar lines inside Experience | clean | 4 sidebar lines inside Experience | clean | 6 sidebar lines inside Experience |
| D2 row by row across both columns | 6 inside | 6 inside | 6 inside | 6 inside | 4 inside | 6 inside | 6 inside |
| D3 arbitrary designer order | 6 inside | **scrambled** | 6 inside | **scrambled** | 4 inside | **scrambled** | 6 inside |
| D4 random z-order | 6 inside | **scrambled** | 6 inside | **scrambled** | 4 inside | **scrambled** | 6 inside |

```text
D3, PyMuPDF (stream order):                    D3, pdftotext default (geometry):
  - Cut training time 3x with FSDP ...           José Núñez
  - Shipped a fraud-detection pipeline ...       EXPERIENCE
  Jun 2021 - Dec 2023                            CONTACT
  Machine Learning Engineer, Contoso AI, Remote  Senior Machine Learning Engineer
  - Designed an evaluation harness ...           jose.nunez@example.com
  - Fine-tuned open-weight LLMs ...              Northwind Labs, San Francisco, CA
  SKILLS                                         +1 415 555 0142
```
**Root cause.** A PDF stores positioned glyph runs, not a reading order. An extractor must infer order either from the order the producer wrote the text (stream order) or from page geometry. Row-aligned columns defeat geometry heuristics; producer write order that differs from reading order defeats stream-order heuristics. No single strategy was safe across E2 and E3. This matches Textkernel's statement that how a page looks is not how its text is stored [S14].

#### E4. Other documented triggers

| Test | Result |
|---|---|
| (a) Hidden text: white 1-pt and white 10-pt tokens beside visible text | All six extraction modes returned both hidden tokens. OCR of the rendered page did not return them. |
| (b) Letter-spaced heading: PDF character spacing versus literal spaces | With character spacing, five of six modes returned "E X P E R I E N C E" (pypdf returned "EXPERIENCE"). With literal spaces all returned spaced letters. An exact "EXPERIENCE" header match fails unless the parser normalises. |
| (c) Contact shown only as link text (Email, GitHub, LinkedIn) | The text layer held only the anchor words; the three real URLs existed only in link annotations. |
| (d) Image-only PDF (page rasterised and re-wrapped) | No fonts; pdftotext returned 0 characters. Tesseract OCR: 7 of 11 tokens exact at 100 dpi (email, phone, "Certified", name missed); 10 of 11 at 150 and 300 dpi (only the accented name missed). |

#### E5. DOCX
| Test | Result |
|---|---|
| Contact in the header and experience in a table; reader sees body paragraphs only (python-docx `doc.paragraphs`) | 1 of 5 sampled tokens found (only "PyTorch"); email, phone, title and date missing. |
| Same file; reader also walks tables and headers | 5 of 5 found. |
| Same file rendered to PDF by LibreOffice, then pdftotext | 5 of 5 found. |
| Contact inside a text box (DOCX produced by LibreOffice from an ODT frame) | Content is present in the XML and in the rendered PDF, but a body-paragraphs-only reader does not see it (email not found; body-text title found). |

**Root cause.** DOCX keeps header, table-cell and text-box content in different parts of the document tree from body paragraphs; a reader that walks only body paragraphs misses them. Greenhouse lists headers, footers and text boxes as parse triggers [S01].

### D5. Parser-proof formatting guidelines and verification protocol

**What "parser-proof" can and cannot mean.** A guarantee of 100% accuracy across Greenhouse, Lever, Ashby and Workday is **not supportable**. Engines are not vendor-confirmed (KF4); Workday itself says results vary with format and word order [S10]; Greenhouse's triggers include content-level conditions such as incomplete job titles, not only layout [S01]; my five extractors disagreed on the same files. The achievable standard is: no documented trigger present, passes at least two extractors, parsed fields verified after submission.

| # | Rule | Root cause it addresses | Evidence | Grade |
|---|---|---|---|---|
| G1 | Single column in linear reading order. No sidebars, text boxes or layout tables for core content. | PDFs carry no reading order; extractors infer it. | [S01], E2, E3 | A + C |
| G2 | Contact block as plain body text at the top: full email, phone, city or region, URLs spelled out. Never only in a header, footer, text box, icon or link anchor. | Header, text-box and annotation content lives outside the body text. | [S01], E4c, E5 | A + C |
| G3 | Standard plain-case headings (Experience, Education, Skills, Projects, Publications). No letter-spacing, no creative section names. | Header matching fails on spaced letters; Greenhouse lists missing section structure. | [S01], E4b | A + C |
| G4 | Keep a real text layer with embedded fonts and a Unicode map. No image-only or flattened text, no photos or graphics. | No text objects means OCR dependence; OCR accuracy drops with resolution and accents. | [S14], [S02], [S10], E4d | A + C |
| G5 | LaTeX: XeLaTeX with OpenType fonts and `\setmainfont{...}[Ligatures=NoCommon]`; or pdfLaTeX with `\usepackage{cmap}` loaded before `fontenc` and scalable fonts installed. Verify with `pdffonts`. | Type 3 bitmap fonts, split accents, ligature code points. | E1 | C |
| G6 | Dates as "Mon YYYY – Mon YYYY" or "Present" on the same line as the full job title and employer. | Association by adjacency; Greenhouse lists incomplete titles. | [S01], E2 | A (trigger) / D (format) |
| G7 | Bullets from fonts whose glyphs extract to real Unicode; check output for control characters. | OT1 bullet extracted as U+0088. | E1 | C |
| G8 | File hygiene: under 2.5 MB, single file, no password, no embedded media; never use fake or test data in a live portal. | Size limit; Greenhouse flags fake resumes; another system's parser rejects test data. | [S01], [S38] | A |
| G9 | Names with diacritics: confirm the extracted name equals the name you enter in the form. Switch pipeline if accents split. | OT1 accent composition. | E1 | C |
| G10 | After upload, correct the parsed fields on the ATS review page. In Workday enter Skills and Languages yourself. | Parsing does not populate them. | [S10] | A |
| G11 | Skills as canonical names, with proof in recent bullets (what, where, when, scale). | Extraction of titles, skills, dates; per-criterion evaluation with citations; recency-weighted skill overlap. | [S07], [S04], [S16] | A (mechanics) / D (advice) |
| G12 | No hidden text, no keyword blocks. | Extracted by every tool; detectors exist. | [S30], E4a | A/B + C |
| G13 | Keep a portal version and a designed version. | Different readers (parsers versus people). | judgement | D |

**Verification protocol (about five minutes per template)**
```bash
pdffonts resume.pdf                 # want: emb=yes and uni=yes on every row; no "Type 3" rows
pdftotext resume.pdf - | head -60   # default reading order: contact, headings, dates in sequence?
pdftotext -layout resume.pdf - | head -60
python - <<'PY'
import pymupdf, unicodedata          # second engine plus code-point checks
t = "\n".join(p.get_text() for p in pymupdf.open("resume.pdf"))
print("compatibility code points:", [hex(ord(c)) for c in t if unicodedata.normalize("NFKC", c) != c][:10])
print("C1 control characters:", [hex(ord(c)) for c in t if 0x80 <= ord(c) <= 0x9f][:10])
PY
# Then: select-all, copy, paste into a plain-text editor and read it top to bottom.
```
Run a vendor parser demo if you can obtain one (not done here), and after each real submission read the parsed fields on the ATS review page.

### D6. AI-native screening layers: what is scored, and how knockouts are enforced

| Layer | Inputs | How relevance is computed (as the vendor describes it) | Output | Automated rejection? | Grade |
|---|---|---|---|---|---|
| **Greenhouse Talent Matching** (Real Talent add-on) [S07] | Resume text (application-form answers not used in the documented version); names and contact details not used | Fine-tuned LLMs, one per extraction task, plus third-party models extract skills, titles, years of experience, dates, companies; embeddings match skills and titles; recruiter weights criteria; validated by back-testing against which candidates passed initial review | Strong, Good, Partial, Limited; "needs manual review" when there is no resume, an unprocessable resume, or an opt-out; hidden after the initial review stage | Vendor states it never advances or rejects | A |
| **Ashby AI-Assisted Application Review** [S04] | Resume, application-form answers, profile data; PII redacted before model calls | An LLM judges each recruiter-written criterion and cites evidence | Per criterion: meets, does not meet, undecided; sortable "criteria met %"; credits metered per evaluation; evaluations can be hidden for candidates who did not pass through the hosted application path with its legal notice | Recruiters decide; the percentage works as a sort key | A |
| **Workday HiredScore** [S12] | Parsed profile (experience, education, skills, languages, certifications, summary) | Default algorithm not documented in retrieved pages; since 5 Aug 2026 an opt-in LLM evaluates each screenable qualification separately | A–D grade; basic qualifications decide A/B versus C/D; preferred qualifications separate A from B and C from D | Grades drive recruiter queues where enabled (the features are optional per customer); *Mobley* alleges harm from screening or ranking [S22] | A |
| **Eightfold** [S16] | Resume or profile and job description embedded with pretrained language models | Hundreds of features: skill overlap over full history and over recent roles, current-title similarity and predicted next title, company and industry similarity, "hireability", similarity to ideal candidates; trained on historical outcomes (applied, advanced, hired, thrived) | 0–5 score in half-point steps; ranked lists; explanations for employer users | Vendor frames output as recommendations; *Kistler* alleges lower-ranked candidates are discarded before human review (allegation) [S21] | A |
| **Phenom Fit Score** [S18] | Candidate profile versus recruiter-set skills, experience, title and location | Weighted criteria with must-have versus preferred skills; the vendor describes learning from outcomes and recruiter feedback | Grade used to prioritise review; vendor's audit materials say it should not be the sole basis for a decision | Customer-configured workflows; vendor does not control them | B |
| **SeekOut** (Evaluate, Sam) [S19] | Public profiles and resumes against a recruiter-defined scorecard | Per-criterion Yes, Partial or No with a score | Ranked shortlist; vendor states candidates are never auto-rejected | No (vendor statement) | B |
| **Beamery** [S20] | Talent graph profiles | Vendor describes explainable weights for skills, seniority, proficiency and industry relevance (2022 statements; no 2026 technical documentation retrieved) | Match recommendations | Not documented | B (dated) |

**What the ranking criteria have in common** (from the vendors' own descriptions; weights are unpublished)
1. They compare an explicit requirement list with *extracted facts* (titles, skills, years, dates, employers), usually adding embedding similarity. Extraction quality, which is stage-1 conversion quality, therefore reaches the ranking.
2. Recency matters (Eightfold weights recent-experience skill overlap separately).
3. Trajectory and "pedigree" features exist at least in Eightfold (title path, company similarity, hireability), so unusual career paths can score lower even when skills match [Inference].
4. Greenhouse, Phenom and Eightfold validate or train against past recruiter decisions, so scores partly encode historical preferences [Inference from [S07], [S16], [S18]].
5. No independent empirical validation of ranking weights or outcomes was found, only vendor-commissioned bias audits [S18, S20].
6. Ashby's description sits between "no ranking" and "ranking": its AI page says the AI never ranks or gives numerical ratings and that a human must always decide, while its documentation describes a "criteria met %" column that can be sorted from best to worst fit [S04].

**How knockout and auto-reject rules are enforced before human review**

| System | Mechanism | Notes | Evidence |
|---|---|---|---|
| Greenhouse | Auto-Reject rules on answers to Yes/No, single-select or multi-select application questions, with optional rejection email; Auto-Tag and Auto-Advance also exist | Plus and Pro tiers; recruiters subscribed to new-application alerts are not notified of auto-rejected applicants | [S08] |
| Ashby | Auto-Reject rules on application-form answers, run only when the application is submitted; global rules at Enterprise tier | Per-job configuration; applications submitted through an application-request link are not checked | [S05], [S06] |
| Lever | Automation workflows triggered by application-form or referral-form submission can auto-archive, optionally with a rejection email; Lever's recipes include a knock-out recipe on form questions | LeverTRM for Enterprise or the Advanced Automation add-on | [S03] |
| Workday | Condition rules auto-advance or auto-decline when a candidate applies (for example an ineligible-to-work answer) or at later stages; evaluated in order; configured through automatic stage routing | Tenant-defined | [S11] |
| Oracle Recruiting and Taleo Enterprise | Scored disqualification questions; in Oracle Recruiting a single negative-scored answer disqualifies automatically | Products differ | [S13] |

Common pattern: rules run when the form is submitted, on structured answers (Greenhouse limits auto-reject to Yes/No, single-select and multi-select questions), not on resume prose. Ashby documents that application-request submissions bypass its rules; for other systems a bypass for candidates who enter another way is an inference [S06].

### D7. Funnel math

#### D7.1 Cold-inbound engineering funnel: per 1,000 applications [Derived from B inputs]

| Stage | Gem engineering chain (6% / 17% / 29% / 73%) | Ashby technical, Q1 2026 (3.6% / 7.3% / 73%) |
|---|---|---|
| First human stage (Gem "pre-onsite"; Ashby "interview") | 60 | 36 |
| Onsite | 10.2 | not reported |
| Offers | 2.96 | 2.63 |
| Hires (73% acceptance) | 2.16 | 1.92 |
| Applications per offer | about 338 | about 380 |
| Applications per hire | about 463 | about 521 |
| Application-to-hire | 0.22% | 0.19% |

Gem prints 0.2% for engineering and 0.1% for data science [S24]. Gem's engineering stage rates are as restated by a secondary synthesis [S28]; Ashby's 7.3% and 73% are corroborated by two further restatements [S39]; the 3.6% interview rate is from the synthesis only [S28].

**Mapping to the brief's ladder.** The brief's stages (inbound, recruiter screen, tech screen, system design, final offer) are not how published benchmarks segment. Gem reports application, pre-onsite, onsite, offer, accept; Ashby reports application, interview, offer. Recruiter screen, tech screen and system design cannot be separated from the published figures I retrieved. A secondary synthesis cites Ashby stage pass-through figures (for example recruiter screen 35%, onsite 24%) that I could not verify on an Ashby page and whose denominators are unclear, so I did not use them [S28].

#### D7.2 Channel deltas (Ashby, 38M applications, Jan 2021 to Dec 2024, all roles) [S25]

| Channel | Share of applications | Application to interview | Interview to offer | Interviews per 1,000 applications | Offers per 1,000 applications | Multiple of inbound | Hires per 1,000 (73–82% acceptance) |
|---|---|---|---|---|---|---|---|
| Inbound | 93.8% | 3% | 6% | 30 | 1.8 | 1.0x | 1.3–1.5 |
| Sourced | 4.8% | 25% | 6% | 250 | 15.0 | 8.3x | 10.9–12.3 |
| Referral | 1.0% | 40% | 16% | 400 | 64.0 | 35.6x | 46.7–52.5 |
| Agency | 0.4% | 42% | 8% | 420 | 33.6 | 18.7x | 24.5–27.6 |
| Internal | 0.05% | 42% | 32% | 420 | 134.4 | 74.7x | 98.1–110.2 |

Stage rates are Ashby's; the per-1,000, multiple and hires columns are [Derived]. Ashby's own recent-window offer rates differ somewhat (inbound 0.2%, referral 7.3%, internal 17.9%) because they average the latest quarters [S25]. Inbound's offer rate had fallen about 70% (7 per 1,000 to 2 per 1,000) over the period [S25].

**Cross-checks**
- Sourced versus inbound: 8.3x derived from Ashby, and "nearly eight times" reported by Gem for hires per application [S23]. Two datasets agree.
- Referral versus inbound: 11x from Gem (hires per application, all functions) [S23]; 36x derived from Ashby (offers per application). The gap reflects different metrics, populations and windows. I report the range 11–36x and do not pick a point value.
- These are selection effects. A referrer pre-screens; a recruiter chooses whom to contact. They show where hiring decisions come from, not that formatting or tactics can convert an inbound applicant into a referral.

**Engineering yield by channel, 2025 (Gem) [S24; ratios Derived]**

| Channel | Share of applications | Share of hires | Yield ratio |
|---|---|---|---|
| Direct sourcing | about 4% | 17.2% | 4.3x |
| Employee referrals | about 2% | 18.7% | 9.4x |
| Company marketing | about 38% | 31.6% | 0.83x |
| Job boards | about 40% | 21.9% | 0.55x |

The four itemised channels cover 84% of applications; the rest is not itemised in the figures I retrieved.

#### D7.3 Cumulative odds at population-average rates [Derived; assumes independent applications]

| Applications sent (N) | P(at least one offer), Gem engineering (0.296% each) | P(at least one offer), Ashby technical (0.263% each) |
|---|---|---|
| 25 | 7.1% | 6.4% |
| 50 | 13.8% | 12.3% |
| 100 | 25.6% | 23.1% |
| 200 | 44.7% | 40.9% |
| 300 | 58.9% | 54.6% |
| 500 | 77.3% | 73.2% |

For comparison, at the Ashby-derived referral rate (6.4% per referred application) three referred applications give about 18% and ten give about 48%; at the sourced rate (1.5%) twenty give about 26%. These are averages across a population dominated by low-fit and fraudulent applications (D7.5), so they are planning floors, not individual forecasts.

#### D7.4 Trend and capacity
- Gem, all functions: application to pre-onsite fell from 13% to 8%, pre-onsite to onsite from 30% to 19%, onsite to offer from 47% to 39%, acceptance 81% to 82% (2021 to 2025, as restated in [S28]). Compounded, application-to-hire fell from about 1.5% to about 0.49% [Derived], consistent with Gem's 0.5% headline [S23].
- Greenhouse (6,000+ companies, 640M+ applications): applications per job rose from 116 (2022) to 244 (2025); applications per recruiter per year from 1,610 to 4,890; recruiters per organisation fell from 10.4 to 4.6; 69.8% of jobs closed with a hire; time to fill about 60 days [S27].
- Ashby: applications per hire about 291 in Q1 2026 versus about 100 in early 2021 (as restated in [S28]); Greenhouse about 203 applications per hire (same restatement).

#### D7.5 GenAI-role proxies, startup versus enterprise, and unresolved conflicts

| Item | Figure | Source | Note |
|---|---|---|---|
| Hire sources for technical roles with "AI" in the title | Inbound 37.1%, sourced 28.0%, agency 9.2%; about 26% referral, internal and other (by subtraction) | [S26] | Read from chart text; share of tech hires with an AI title rose from under 1% in 2023 to about 8% |
| Application-to-hire, data science | 0.1% (about 1 in 1,000) | [S24] | Gem customers |
| Interviews per engineering hire | 35–36 | [S24] | |
| ML-role applicants flagged high-risk for fraud (Greenhouse pilot) | More than 35%; 91% of flagged candidates reviewed were confirmed fraudulent | [S09] | Signals: phone, email, IP, location |
| Share of 2025 US candidates self-reporting prompt injection | 40% | [S29] | Self-reported survey |
| Startup versus enterprise, engineering | Startups (under 500): 12% / 58% / 22% / 84%; enterprises (2,000+): 28% / 31% / 14% / 80% | [S24] | Multiply to 1.3% and 1.0% |

**Unresolved conflicts (declared, not smoothed over)**
1. The company-size table above multiplies to about 1.3% and 1.0%, which is 5–6x Gem's 0.2% engineering headline on the same page. Stage definitions or denominators differ in ways the page does not explain, so I do not use it to compare startups with enterprises.
2. Gem's all-function text says small companies pass about 25% of applicants to pre-onsite but hire about 0.3%, while large companies pass under 10% and hire about 0.7% [S23]. The engineering table points the other way at the top of the funnel (startups 12%, enterprises 28%). Different stage definitions and populations are the likely explanation; I could not reconcile them.
3. The brief's "1–3% pass-through" prior is at or below the low end of what I found: 3% (Ashby inbound to interview, all roles), 3.6% (Ashby technical), 6% (Gem engineering to pre-onsite). GenAI-only and Fortune-500-only pass-through rates were not found.

### D8. Tool catalog

| Tool | Category | What it does (source type) | What it does not show | Status here |
|---|---|---|---|---|
| Textkernel Extract! / Tx Platform (includes Sovren) | Parsing engine and API | Converts and parses 70+ formats; optional OCR; optional LLM parser; conversion result codes [S14, S15] | That it is the engine inside Greenhouse, Lever, Ashby or Workday; only Oracle Recruiting Cloud lists an integration | Documentation read; demo or API not reachable from the sandbox |
| Daxtra | Parsing vendor | Named in the brief | Not researched | Not evaluated |
| Jobscan | Resume-to-posting match checker | Match rate from keyword overlap plus formatting checks (vendor and third-party descriptions) [S36] | Any validated link to real ATS output; claims about its parser are third-party and unverified | C |
| Teal | Job tracker, resume builder, keyword match | Third-party comparisons [S36] | Same | C |
| Resume Worded | Resume feedback and score | Third-party comparisons [S36] | A replica of any ATS parser | C |
| Huntr | Job tracker, autofill, resume builder | Vendor blog [S36] | A parser check | C |
| Ashby "candidate portal" | Candidate-facing surface | No candidate login portal found in Ashby documentation; a third-party guide asserts none exists. Found instead: hosted application forms and Application Requests links [S06] | | C |
| Open-source extractors (pdftotext, PyMuPDF, pdfminer.six, pypdf, pdfplumber) and Tesseract | Stage-1 conversion probes | Used in D4 | Vendor parser behaviour | Tools exist (A); conclusions C |
| Greenhouse "Unsuccessful resume parse" article | Vendor-documented checklist | Lists parse triggers [S01] | Candidate-side autofill parity | A |

### D9. Litigation and regulatory context (status as retrieved)
- ***Kistler v. Eightfold AI*** (No. 26-cv-01768, N.D. Cal. after removal): filed 20 Jan 2026 in Contra Costa County Superior Court; removed to the Northern District of California on 2 Mar 2026. Plaintiffs allege that 0–5 Match Scores and candidate profiles are consumer reports under the Fair Credit Reporting Act and a California analogue, and that lower-ranked candidates are discarded before human review. Eightfold denies the characterisation and says it only licenses software that employers use internally. A motion to dismiss was filed 20 Apr 2026; the 4 Aug hearing was vacated and the motion has been under submission since the 9 Jul reply, with no ruling as of 1 Oct 2026 [S21]. Allegations, not findings.
- ***Mobley v. Workday*** (No. 23-cv-00770, N.D. Cal.): preliminary ADEA collective certification on 16 May 2025; a July 2025 order (docket 158) put applicants whose applications were scored, sorted, ranked or screened with HiredScore AI features inside the collective and required Workday to identify customers who had enabled those optional features; notice plan approved 2 Dec 2025; partial motion-to-dismiss ruling in late June 2026 [S22]. One law-firm summary reports that interlocutory review was denied in July 2026 (single source, not verified). Allegations, not findings.
- Phenom's and Beamery's published bias audits reference New York City's Local Law 144 [S18, S20]. Phenom's audit states it is not an opinion on whether Fit Score is an automated employment decision tool [S18]. Vendors have an incentive to position scores as decision support [Inference].

---

## 7. Open Questions & Risks

### 7.1 Strongest objections an expert would raise, and what the evidence says

| # | Objection | Evidence for | Evidence against | Net |
|---|---|---|---|---|
| 1 | "Open-source extractors are not vendor parsers, so D4 says nothing about Greenhouse, Lever, Ashby or Workday." | No vendor parser was run. Textkernel claims multi-column support and vendor engines add layout analysis and OCR [S14, S15]. | Greenhouse and Workday list the same kinds of triggers [S01, S10]. Textkernel says conversion is the dominant failure source [S14]. D4 isolates mechanisms, not prevalence. | Valid. D4 stays Grade C; rules G1–G4 rest on vendor documents, with D4 as illustration. |
| 2 | "The benchmarks come from tech-forward, growth-stage customers of Gem, Ashby and Greenhouse, not the Fortune 500, and stage definitions differ." | Gem's own cuts conflict (D7.5). No Fortune-500-specific dataset. Customer bases skew to tech companies [Inference]. The engineering chain is a secondary restatement [S28]. | Greenhouse's sample is large (6,000+ companies, 640M+ applications) [S27]. Two vendors converge near 0.2% for engineering. The sourced-versus-inbound ratio agrees across vendors. | Valid for enterprise and for GenAI-only. Treat 0.2% as an engineering average for tech-forward employers. |
| 3 | "Population averages are diluted by spam and fraud, so 0.2% is irrelevant to a qualified candidate." | More than 35% of applicants to one Greenhouse ML-role pilot were high-risk; applications per job more than doubled; 40% of US candidates say they used prompt injection [S09, S27, S29]. | No dataset gives genuine-applicant rates. A well-matched applicant's odds are probably higher but unquantified; evaluators also face more noise, which can hurt genuine applicants. | Valid. Use 0.2% as a floor for effort budgeting. |
| 4 | "Referral multipliers are selection, not causation." | A referrer pre-screens; a recruiter chooses whom to contact. | Referral candidates also convert interview-to-offer at 16% versus 6% [S25], so the advantage persists after the interview. | Valid. The implication is channel strategy, not formatting. |
| 5 | "'Never auto-rejects' is marketing; exclusion happens through prioritisation." | Ashby's sortable percentage; ranked lists in Eightfold and Phenom; litigation allegations; 53% of US recruiters say they handed most screening to AI/ATS [S04, S16, S18, S21, S22, S29]. | Greenhouse hides match results after the initial review and sends unprocessable resumes to manual review; SeekOut and Greenhouse make explicit statements; no measured exclusion data exists [S07, S19]. | Unresolved. Assume prioritisation risk. |
| 6 | "Documents go stale; vendors change behaviour constantly." | Workday's parsing concept page is dated 2023; HiredScore's LLM mode is an August 2026 opt-in; the Lever page body could not be fetched. | Greenhouse's parse article was updated in March 2026; Ashby's documentation carries September 2026 screenshots. | Valid. Re-test quarterly (R9). |
| 7 | "Hidden text may work against some LLM pipelines; 'avoid' is a risk judgement, not a refutation." | A lab study shows gains when injection is rare; 40% self-report use; the large-scale study did not measure effect [S29, S30, S31]. | About 1% prevalence with detectors at 86–93% precision [S30]; lab gains collapse when widespread [S31]; Greenhouse's matching uses task-scoped extraction models rather than a free-form ranking prompt [S07], which plausibly limits susceptibility [Inference]; fraud-flag exposure [S09]. | "Unvalidated", not "refuted". The recommendation stands as risk management. |
| 8 | "Score-based or AI-driven auto-reject may be more widespread than the documents show." | Surveys say recruiters hand most screening to AI/ATS [S29, S33]. *Kistler* alleges low-ranked candidates are discarded before human review [S21]. Kula (outside scope) documents rule-based auto-rejection without manual review [S37]. | No retrieved document for the four ATS describes score-based auto-reject; Greenhouse, Ashby and SeekOut state that humans decide [S04, S07, S19]. | Not evidenced for the four ATS; remains a configuration-dependent risk. |

### 7.2 Negative and partial results ("searched X, found nothing")

| Item | Searched | Result |
|---|---|---|
| Parser engine for Greenhouse, Lever, Ashby, Workday | Vendor support and developer pages; Textkernel and RChilli partner pages; Oracle documentation | Not vendor-confirmed for any of the four. Oracle says Taleo parsing is a third-party partner service (unnamed); Textkernel and RChilli list Oracle integrations. |
| Ashby resume-parsing documentation | Ashby docs, blog, knowledge base | None found; only AI review, auto-reject, application-request and application-limit pages. |
| Lever full help article and AI screening | Help-centre fetch returned a script-rendered shell; AI screening pages not retrieved | Evidence limited to a search extract and the automation pages. |
| Canva export text-layer statement | Canva Help (download file types; PDF import) and third-party guides | None from Canva; third-party guides conflict. |
| GenAI-only or Fortune-500-only funnel | Gem, Ashby, Greenhouse, Pin, HeroHunt, candidate.fyi | None; proxies only. |
| Independent validation of Eightfold, Phenom, Beamery ranking | Vendor and audit materials | Vendor-commissioned audits only; no Beamery 2026 technical documentation. |
| Production effect of hidden text on ranking | arXiv | Prevalence measured; effect not measured; lab only. |
| Workday response-rate or "black hole" dataset | Web search | None. |
| Full Gem benchmark PDF | Direct fetch | Failed (response too large); used Gem web pages plus a secondary restatement. |
| Vendor parser demo or sandbox | Sandbox network limited to package registries | Not attempted. |
| Checker scores versus real ATS output (Jobscan, Teal, Resume Worded) | Web search | No validation found. |
| Taleo parse-failure consequences | Oracle documentation | Not documented in retrieved pages. |
| pdfLaTeX with `lmodern`; LuaLaTeX | Local build | Not testable in the sandbox. |

### 7.3 Open questions, ranked by decision value
1. Which engine and conversion method does each of the four ATS use, and does an LLM stage change PDF-to-text conversion? (Test: vendor trial or sandbox with the D4 corpus; ask the vendors.)
2. What share of tenants enable Talent Matching, Ashby AI review and HiredScore (the latter is optional per customer), and how often do recruiters open candidates below the top of a sorted list?
3. What is the GenAI-only funnel (applicants, screens, offers) for AI/ML roles at startups versus large enterprises? (Possible sources: custom cuts from Ashby or Gem; your own tracking.)
4. Does each Canva export option keep a text layer? (Test with the D5 protocol.)
5. How do fraud-signal features treat genuine applicants who use VPNs, aliases or VoIP numbers?
6. Will *Kistler* or *Mobley* rulings compel disclosure of scoring features or exclusion rates?
7. What are Workday response rates by application path (form, referral, recruiter-sourced)?

### 7.4 Risk register

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Vendor parser behaviour differs from my extractor results | Layout rules may be stricter or looser than needed | Medium | Vendor demo test; keep G1–G4 because they match documented triggers |
| Inbound conversion keeps falling as AI-generated volume grows | Inbound budget in R1 becomes too high | High | Track your own funnel; re-pull Gem and Ashby benchmarks each release |
| Documents outdated | Wrong rule applied | Medium | Quarterly re-check |
| Secondary restatements misquote primary data | Wrong numbers in D7 | Medium | Flagged; verify against the Gem PDF when it can be fetched |
| Local environment artefacts (no `cm-super` or `lmodern`) | Type 3 failure prevalence overstated in E1 | High for L3, L4, L6 | Stated; E1 shows mechanism, not prevalence |
| Litigation outcomes change vendor behaviour | AI layers disabled, disclosed or reconfigured | Low to medium | Watch dockets and vendor release notes |

### 7.5 DONE-criteria status

| Criterion | Status | Gap |
|---|---|---|
| Parser architecture and failure modes for the top four ATS documented with technical root causes | **Partially met** | Engine identity unconfirmed for all four; no Ashby parse documentation; Workday parse page dated 2023; root causes documented at the generic (Textkernel) level and by local experiment |
| Full funnel math benchmarked with real-world rates | **Partially met** | Benchmarks use Gem and Ashby stage definitions, not the brief's five-stage ladder with system design; no GenAI-only or Fortune-500-only data; the startup-versus-enterprise table conflicts |
| AI screening demystified with empirical ranking criteria | **Partially met** | Features documented per vendor; weights unpublished; no independent validation |
| Common myths debunked or validated | **Met** | Hidden-text effect in production unmeasured; Canva unverified |
| Actionable parser-proof formatting guidelines | **Met with caveat** | A 100% guarantee across four ATS is not supportable; no vendor parser was tested |

---

## 8. Delta (belief change table)

Credences are my subjective estimates before and after the evidence.

| Belief | Before | After | Change | Why (evidence grade) |
|---|---|---|---|---|
| P1: ">75% auto-rejected" is baseless; real rejection is configured knockouts on form answers | 75% | about 90% | Strengthened | Origin trace (B); documented rules on question answers in all four ATS (A). Nuance added: automation still shapes who is read first (B). |
| P2: Column and Canva layouts garble extraction; vendor parsers handle ordinary text multi-column files | 60% | about 50% | Weakened and made conditional | Greenhouse lists columns as a trigger (A); Textkernel claims support (B); local results are extractor-dependent (C); Canva unverified. |
| P3: Parse failure is not a silent rejection in Greenhouse, Lever, Ashby; friction is re-entry and knockouts | 60% | about 80% (Greenhouse, Lever documented; Ashby unknown) | Strengthened with caveats | Documents (A). New: parse output feeds AI layers (A); Workday never auto-fills Skills and Languages (A). |
| P4: Cold inbound is about 0.2–0.5%; referrals at least 5–15x; sourced in between | 50% | about 85% on the 0.2% floor; magnitudes revised | Updated | Gem and Ashby converge at 0.19–0.22% (B, derived); referral 11–36x per application (above the prior range); sourced about 8x (B, derived). |
| P5: AI layers rank rather than reject; hidden-text tricks give no reliable benefit | 65% | about 70% | Slightly strengthened | Vendor statements (A). Nuance: Ashby's sortable percentage; litigation allegations (B); hidden text "unvalidated", not refuted (A/B/C). |
| Recalled engine map (Sovren or Textkernel behind Greenhouse and Lever; others in-house) | Grade D | Unresolved | Not confirmed | No vendor-confirmed engine (A, negative result); Oracle says Taleo uses a third-party partner service (A). |
| "Greenhouse has no AI scoring" (claim on SEO checker sites) | circulating | Contradicted | New | Talent Matching documentation (A). |
| "LaTeX ligatures always break ATS parsing" | circulating | Contradicted for default OT1 Type 1 output; conditional failures remain | New | Local tests (C). |
| "Ashby never ranks" | circulating | Nuanced | New | Ashby's AI page says no ranking; its documentation describes a sortable criteria-met percentage (A). |
| Auto-reject is universal and applies to everyone | assumed | Tier-gated and form-bound; Ashby documents a bypass for application-request links | New | Greenhouse Plus/Pro; Ashby tiers; Lever Enterprise or add-on (A). |
| One format (PDF or DOCX) is settled | assumed | Unresolved; Textkernel advises avoiding PDF where possible | New | Textkernel documentation (A) versus my DOCX test (C). |
| Gem's company-size funnel and headline are consistent | assumed | They are not (1.3% and 1.0% versus 0.2%) | New | Derived from Gem's page (B). |

---

## 9. Sources & Evidence Ledger

All sources were retrieved or searched on 2026-10-23. "Extract" means only a search-engine extract of the page was available. Third-party pages are used only where graded C or D, or to document contradictions.

### Evidence grading scale

| Grade | Meaning |
|---|---|
| A | Primary or canonical source retrieved this session (vendor documentation, support or developer pages, recognised litigation trackers, arXiv papers with data), and the source itself states the claim. |
| B | Credible secondary source, or a vendor-published dataset with a stated sample or method, retrieved this session. Vendor self-reports sit here when they are the only source. |
| C | Single marketing or anecdotal source; **or my own reproducible local experiment** (open-source extractors, not vendor parsers); **or arithmetic I derived from A/B inputs**. |
| D | Recalled from model memory, or inference without retrieved support. |
| R | Verdict tag: refuted or contradicted by retrieved evidence. |

### Ledger

| ID | Source | URL(s) | Type | Date or version seen | Supports | Grade |
|---|---|---|---|---|---|---|
| S01 | Greenhouse Support, "Unsuccessful resume parse" | https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse | Vendor support article (fetched) | Page showed an update of 2 Mar 2026 | KF2, D2, D5 | A |
| S02 | Lever Help Center, "Understanding Resume Parsing" | https://help.lever.co/hc/en-us/articles/20087345054749 (alt: https://help.lever.co/s/article/Understanding-Resume-Parsing) | Vendor help article; body not fetchable (script-rendered), extract only | n/a | KF2, D2 | A (extract) |
| S03 | Lever Help Center: "Creating and managing automation workflows"; "Automation workflow recipes"; "Operating the Archive"; Lever Winter Release press release | https://help.lever.co/hc/en-us/articles/20087323591069 ; https://help.lever.co/hc/en-us/articles/20087246036893 ; https://help.lever.co/hc/en-us/articles/20087374094365 ; https://www.businesswire.com/news/home/20200206005189/en/Levers-Winter-Release-Introduces-Auto-screening-Confidential-Postings-and-12-Other-Major-New-Features | Vendor documentation and press release (extracts) | Press release Feb 2020 | KF1, D2, D6 | A |
| S04 | Ashby Knowledge Base, "AI-Assisted Application Review" (fetched); Ashby release post; Ashby AI page; ADP marketplace listing | https://docs.ashbyhq.com/ai-assisted-application-review ; https://www.ashbyhq.com/blog/product/ai-assisted-application-review ; https://ashbyhq.com/ai ; https://apps.adp.com/en-US/apps/555443/Ashby%20for%20ADP%20Workforce%20Now%C2%AE/features | Vendor documentation | Docs screenshots dated through 24 Sep 2026; release post 10 Sep 2024 | KF3, KF8, D2, D6 | A |
| S05 | Ashby: "Auto-Reject Applications"; product update "Pre-Screen Candidates with Auto-Reject"; "Global Application Questions & Global Auto-Reject Rules" | https://docs.ashbyhq.com/auto-reject-applications ; https://www.ashbyhq.com/product-updates/pre-screen-candidates-with-auto-reject ; https://docs.ashbyhq.com/global-application-questions-and-global-auto-reject-rules | Vendor documentation | n/a | KF1, D2, D6 | A |
| S06 | Ashby: "Application Requests" (docs and product update); "Application Limits" | https://docs.ashbyhq.com/application-requests ; https://www.ashbyhq.com/product-updates/use-application-requests-to-enrich-candidate-profiles-and-application-details ; https://docs.ashbyhq.com/application-limits | Vendor documentation | n/a | R5, R6, D1, D2, D6 | A |
| S07 | Greenhouse Support, "Talent Matching Data Processing FAQ" | https://support.greenhouse.io/hc/en-us/articles/41131616864283-Talent-Matching-Data-Processing-FAQ | Vendor support article (fetched) | n/a | KF3, KF8, D2, D6 | A |
| S08 | Greenhouse Support: "Application Rules Overview"; auto-reject application-rule article | https://support.greenhouse.io/hc/en-us/articles/203105595-Application-Rules-Overview ; https://support.greenhouse.io/hc/en-us/articles/360000653472 | Vendor support articles | n/a | KF1, D2, D6 | A |
| S09 | Greenhouse Real Talent page; Greenhouse blog on spotting fraud earlier | https://www.greenhouse.com/greenhouse-real-talent ; https://www.greenhouse.com/blog/real-talent-spot-fraud-earlier-protect-recruiter-time | Vendor page and blog | n/a | KF11, D6, D7.5 | B |
| S10 | Workday Administrator Guide, "Concept: Resume Parsing" | https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html | Vendor documentation | Last updated 2023-06-23 | KF2, D2 | A |
| S11 | Workday Administrator Guide, "Steps: Automatically Advance or Decline Candidates"; questionnaire page | https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/prospect-and-candidate-management/uwd1485375819245.html ; https://doc.workday.com/admin-guide/en-us/manage-workday/business-processes/questionnaires/questionnaire-video-examples/collect-information-from-job-applicants/review-the-responses-to-a-questionnaire.html | Vendor documentation | Last updated 2024-09-20 | KF1, D2, D6 | A |
| S12 | Workday HiredScore release notes, 5 August 2026 | https://doc.workday.com/hiredscore/en-us/workday-hiredscore/hiredscore-release-notes/2026/august/wednesday--5th-august.html | Vendor release notes (fetched) | 2026-08-05 | KF3, KF8, D6 | A |
| S13 | Oracle documentation: Taleo Enterprise "Plain Text Resume Parsing for Mobile Devices"; "Supported Languages"; "Create Disqualification Question in Library"; Oracle Recruiting "Guidelines for Scoring Questions" | https://docs.oracle.com/en/cloud/saas/taleo-enterprise/22d/otcug/c-plaintextresumeparsingmobile.html ; https://docs.oracle.com/en/cloud/saas/taleo-enterprise/21c/otrcg/r-supportedlanguages.html ; https://docs.oracle.com/en/cloud/saas/taleo-enterprise/23c/otfru/t-createdusqualificationquestioninlibrary.html ; https://docs.oracle.com/en/cloud/saas/talent-management/faimh/guidelines-for-scoring-questions.html | Vendor documentation | n/a | KF4, D2, D6 | A |
| S14 | Textkernel developer documentation: resume parser Getting Started (v9); LLM Parser (v9); document conversion result codes (v10); job parser overview with OCR facts (v9); supported file formats | https://developer.textkernel.com/tx-platform/v9/resume-parser/overview/getting-started/ ; https://developer.textkernel.com/tx-platform/v9/resume-parser/overview/llm-parser/ ; https://developer.textkernel.com/tx-platform/v10/resume-parser/overview/document-conversion-code/ ; https://developer.textkernel.com/tx-platform/v9/job-parser/overview/ ; https://developer.textkernel.com/TKPlatform/master/file-formats | Vendor developer documentation | n/a | KF2, D3, D4 | A |
| S15 | Textkernel product pages (Extract; Oracle Recruiting Cloud integration); RChilli Oracle HCM page | https://textkernel.com/solution/extract ; https://www.textkernel.com/integrations/oracle-recruiting-cloud/ ; https://www.rchilli.com/oracle-hcm | Vendor marketing (the first two seen in search results, not re-fetched) | n/a | KF4, KF5, D3 | B |
| S16 | Eightfold Engineering Blog, "AI-powered talent matching: the tech behind smarter and fairer hiring" | https://eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring/ | Vendor engineering blog (fetched) | 13 Aug 2025 | KF8, D6 | A |
| S17 | Withdrawn: Eightfold matching-model page (URL not re-verified; not used) | n/a | n/a | n/a | n/a | n/a |
| S18 | Phenom Fit Score page and report page; Fit Score 2024 audit reports | https://www.phenom.com/fit-score ; https://www.phenom.com/resource/phenom-fit-score-report ; https://assets.phenom.com/hubfs/02_Assets/ebook/Phenom_Fit_Score_2024_Audit_Report.pdf ; https://go.phenom.com/hubfs/Phenom%20Fit%20Score%202024%203rd%20Party%20Bias%20Audit.pdf | Vendor pages and audit reports | n/a | KF8, D6, D9 | B |
| S19 | SeekOut Evaluate-tab help article; SeekOut Sam page | https://intercom.help/seekout/en/articles/14049111-workspaces-evaluate-tab ; https://seekout.com/solutions/sam | Vendor documentation and marketing | n/a | KF8, D6 | B |
| S20 | Beamery, "Beamery completes AI audit for bias" | https://beamery.com/resources/news/beamery-completes-ai-audit-for-bias | Vendor press release | 2022 | KF8, D6, D9 | B (dated) |
| S21 | *Kistler v. Eightfold* coverage: Jones Walker (1 Oct 2026); OpenClassActions; Jones Walker (earlier article); Reuters via Yahoo Finance (21 Jan 2026); Akin tracker | https://www.joneswalker.com/en/insights/blogs/ai-law-blog/your-adverse-action-workflow-starts-too-late.html ; https://openclassactions.com/lawsuits/consumer-protection/eightfold-ai-hiring-fcra-class-action-lawsuit.php ; https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-hiring-under-fire-what-the-eightfold-lawsuit-means-for-every-employer-using-a.html ; https://finance.yahoo.com/news/ai-company-eightfold-sued-helping-181520410.html ; https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/ai-hiring-platform-faces-fcra-class-action-over-data-use-or-kistler-et-al-v-eightfold-ai-inc | Law-firm and tracker pages | Status as of 1 Oct 2026 | KF8, D9 | B |
| S22 | *Mobley v. Workday*: Civil Rights Litigation Clearinghouse; Order Re HiredScore Dispute (docket 158); Gunderson Dettmer spring 2026 update; Akin tracker; one law-firm summary | https://clearinghouse.net/case/44074/ ; https://storage.courtlistener.com/recap/gov.uscourts.cand.408645/gov.uscourts.cand.408645.158.0.pdf ; https://www.gunder.com/en/news-insights/client-news/client-insight-quarterly-employment-law-update-spring-2026 ; https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/district-court-grants-preliminary-certification-of-collective-action-for-discrimination-claim-against-ai-based-system ; https://www.daeryunlaw.com/us/practices/detail/ai-employment-discrimination | Docket order, trackers, law-firm pages | Latest item: June to July 2026 | KF8, D9 | B (docket order A; last item single-source C) |
| S23 | Gem, "Key takeaways from the 2026 Recruiting Benchmarks Report" | https://www.gem.com/blog/key-takeaways-from-the-2026-recruiting-benchmarks-report | Vendor dataset blog (fetched) | 1 Dec 2025 | KF10, D7 | B |
| S24 | Gem, "Hiring AI & engineering talent in 2026" | https://www.gem.com/resource/tech-hiring-guide | Vendor report page (fetched) | n/a | KF9, KF10, KF11, D7 | B |
| S25 | Ashby Talent Trends, "Are referred candidates more likely to get hired?" | https://www.ashbyhq.com/talent-trends-report/reports/referrals | Vendor dataset (fetched) | 16 May 2025; data Jan 2021 to Dec 2024 | KF10, D7.2 | B |
| S26 | Ashby Talent Trends, AI job postings report | https://www.ashbyhq.com/talent-trends-report/reports/ai-job-postings | Vendor dataset (fetched; figures read from chart text) | 9 Jul 2026 | KF11, D7.5 | B |
| S27 | Greenhouse hiring benchmarks page ("The Hire Standard") | https://www.greenhouse.com/recruiting-benchmarks | Vendor dataset (fetched) | March 2026 | KF9, D7.4 | B |
| S28 | HeroHunt, "Recruiting Funnel Conversion Rates 2026: Stage Benchmarks" | https://www.herohunt.ai/blog/recruiting-funnel-conversion-rates-2026-stage-benchmarks/ | Vendor blog synthesising Gem, Ashby and Greenhouse (fetched) | 28 Sep 2026 | KF9, D7.1, D7.4 | C |
| S29 | Greenhouse, "AI in Hiring Report" | https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/691b3f85d9304d0f30b57773_3274b13134499af4515ec383ff3b1f01_Greenhouse-2025_AI_in_Hiring_Report.pdf | Vendor survey, about 4,100 respondents, self-reported (fetched) | Nov 2025 | KF1, KF7, D7.5 | B |
| S30 | arXiv:2605.28999, "Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening" | https://arxiv.org/html/2605.28999v1 | Preprint (fetched) | May 2026 | KF7 | A/B |
| S31 | arXiv:2606.27287, "Prompt Injection in Automated Résumé Screening with LLMs" | https://arxiv.org/pdf/2606.27287 | Preprint (fetched) | 25 Jun 2026 | KF7 | B |
| S32 | The Conversation via phys.org, "What everyone gets wrong about the modern job search"; HR Tact, "Your Job Application Was Rejected by a Human, Not a Computer" | https://phys.org/news/2026-07-wrong-modern-job.html ; https://hrtact.com/2020/10/05/your-job-application-was-rejected-by-a-human-not-a-computer/ | Article and investigation (both fetched) | 6 Jul 2026; 5 Oct 2020 | KF1, D1 | B |
| S33 | Harvard Business School Working Knowledge; HR Dive; The Register on "Hidden Workers: Untapped Talent" | https://hbswk.hbs.edu/item/how-to-tap-the-talent-automated-hr-platforms-miss ; https://www.hrdive.com/news/report-applicant-tracking-systems-may-exclude-whole-segments-of-candidates/606614/ ; https://www.theregister.com/2021/09/08/harvard_jobs_report/ | Authors' article and press coverage (extracts) | 2021 | KF1 | B |
| S34 | Ghostscript bug tracker: 704478, 704674, 704681 | https://bugs.ghostscript.com/show_bug.cgi?id=704478 ; https://bugs.ghostscript.com/show_bug.cgi?id=704674 ; https://bugs.ghostscript.com/show_bug.cgi?id=704681 | Bug reports (extracts) | n/a | KF6 | A (for the existence of the ToUnicode ligature failure family only) |
| S35 | Canva Help: "Download file types"; PDF import pages | https://www.canva.com/en/help/download-file-types/ ; https://www.canva.com/en_au/help/import-and-edit-pdfs-canva/ | Vendor help pages (extracts) | n/a | D1 | A (silent on the text layer) |
| S36 | Third-party ATS-checker and tool pages: scale.jobs scanner comparison; jobshinobi Jobscan pages; Jobright Jobscan review; Huntr "Huntr vs Teal"; plus domains atsverification.com, resumegeni.com, enhancv.com, apply-mate.com (domain-level; URLs not re-verified) | https://scale.jobs/blog/ats-resume-scanners-comparison-accuracy-test ; https://jobshinobi.com/blog/jobscan-resume-scanner-how-it-works ; https://jobright.ai/blog/jobscan-review-2026-walkthrough-features-and-alternatives/ ; https://huntr.co/blog/huntr-vs-teal | Marketing and comparison pages | n/a | KF4, KF12, D8 | C/D |
| S37 | Kula Help Center, "Auto-rejection rules and knockout questions" (outside the brief's scope) | https://support.kula.ai/articles/7962068559-auto-rejection-rules-and-knockout-questions | Vendor documentation | n/a | §7.1 | B |
| S38 | Sage People help, "Resume Parsing" (outside the brief's scope); Sovren-engine and test-data statements read in an earlier extract, not re-verified | https://help-people.sage.com/Content/SP_Talent_Acq/Use/SP_TalentAcq_Use_ResumeParsing.htm | Vendor documentation (extract) | n/a | D3, G8 | B |
| S39 | candidate.fyi and Pin benchmark pages restating Ashby Q1 2026 stage rates | https://candidate.fyi/post/recruiting-funnel-benchmarks ; https://www.pin.com/blog/recruitment-funnel-benchmarks/ | Secondary restatements | n/a | KF9, D7.1 | C |
| S40 | Local experiments run this session (Appendix A) | n/a | Reproducible sandbox tests | 2026-10-23 | KF5, KF6, KF7, D4, D5 | C |

---

## Appendix A. Reproduction recipe for the local experiments

**Environment:** Ubuntu 24.04; pdfTeX 1.40.25 and XeTeX (TeX Live 2023); poppler `pdftotext` 24.02.0; PyMuPDF 2.0; pypdf 5.9.0; pdfminer.six 20251230; pdfplumber 0.11.9; Tesseract 5.3.4; LibreOffice 24.2.7.2; python-docx 1.2.0; Python 3.12.3.

**Test document.** One synthetic resume (fictional "José Núñez"; two roles; education; skills; a certification line) containing the ligature-sensitive words workflow, workflows, Fine-tuned, efficient, flagship and Certified. Eleven target tokens: those six, the accented name, email, phone, the first job title, and "PyTorch".

**LaTeX preamble variants (E1)**
```latex
% L1  pdfLaTeX, OT1 default           : (nothing added)
% L2  + glyph-to-Unicode              : \input{glyphtounicode}\pdfgentounicode=1
% L3  T1 encoding                     : \usepackage[T1]{fontenc}        % no lmodern or cm-super installed -> Type 3 fonts
% L5  OT1 + cmap                      : \usepackage{cmap}
% L6  T1 + cmap                       : \usepackage{cmap}\usepackage[T1]{fontenc}
% L7  XeLaTeX                         : \usepackage{fontspec}
% L10 XeLaTeX, font-level fix         : \usepackage{fontspec}
%                                       \setmainfont{Latin Modern Roman}[Ligatures=NoCommon]
% (L9) \defaultfontfeatures{Ligatures=NoCommon} did NOT remove the ff ligature in my run.
```

**Layouts (E2).** X1 single column; X2 two `minipage` blocks side by side (sidebar); X3 `tabular` with dates in the left cell; X4 `multicols` with two flowing columns. All compiled with XeLaTeX.

**Export-order emulation (E3).** A ReportLab page with two row-aligned columns; the same text objects written in four orders (column by column; row by row; arbitrary; random).

**Extraction modes (seven):** `pdftotext` (default), `pdftotext -raw`, `pdftotext -layout`, PyMuPDF `get_text()`, pdfminer.six `extract_text`, pypdf `extract_text`, pdfplumber `extract_text`.

**Token status function (verbatim logic).**
```python
import re, unicodedata
def norm(s): return re.sub(r"\s+", " ", s)
def token_status(text, tok):
    t = norm(text)
    if tok in t: return "OK"
    if tok in unicodedata.normalize("NFC", t):  return "decomposed accents"
    if tok in unicodedata.normalize("NFKC", t): return "ligature code points"
    if tok.replace(" ", "") in re.sub(r"\s+", "", t): return "spaced letters"
    return "damaged or missing"
```

**Layout metric.** Locate anchor strings for the main column in the normalised extracted text; the main column is "in order" if the anchor indices increase; "sidebar lines inside Experience" counts sidebar anchors whose index falls between the first and last main-column anchors; "lines merged across columns" means an anchor string could not be found because lines from both columns were joined.

**Other tests.** (E4a) ReportLab page with white 1-pt and white 10-pt text; check presence in extractor output and OCR the rendered page. (E4b) heading drawn with PDF character spacing versus literal spaces. (E4c) LaTeX `\href{mailto:...}{Email}` links; list URIs from `/Annots` with pypdf. (E4d) Rasterise X1 at 100, 150 and 300 dpi with `pdftoppm`, wrap each image in a PDF, run `tesseract --psm 4`. (E5) python-docx document with header and a two-column table; a flat-ODT text frame converted to DOCX by LibreOffice; compare body-paragraphs-only reading, table-and-header reading, and PDF-render-then-extract.

**Limits.** Open-source extractors only; no vendor parser; lmodern and LuaLaTeX untested; single synthetic document; Canva exports not tested.
