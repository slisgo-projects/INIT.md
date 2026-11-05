# BootLoops Verification Protocols

**Date:** 2026-11-05
**Status:** current
**Baseline:** INIT.md version 2026-11-05, before this report's edits.
**Provenance:** quotes were checked against the local copies in §"References". The mappings to INIT.md and the impact ratings are AI judgment. No BootLoops protocol has been tried on an INIT.md project.

## Disposition

Operator decisions, 2026-11-05 (DECISIONS.md):

- **Adopted:** R1, R2, R3, R4. The edits are in INIT.md §"Findings and Checks", §"Report Files" and §"Skills".
- **Not adopted:** the timing discipline; referee-sim, prove-protocol and constant-recognition as INIT.md rules.
- **Open:** G1, judgment by an operator outside their domain.

## Question

- BootLoops (M. D. Schwartz, 2026) is an LLM harness for quantitative science. Does anything in it apply directly to INIT.md, and would it make a real difference?

## Findings

### What BootLoops is

- **Two halves.** The `bootloops` toolkit holds computing packages, each with a guide. The `skills` repo holds 12 protocol files in Agent Skills format (`skills_README.md` §"The roster").
- **No project-document schema.** It has no project flowdown, no decision log and no continuity files, so nothing competes with INIT.md's structure. What it offers is verification discipline.
- **Results:** 36 preprints in about 3 months, across 22 fields according to the Science headline (Science PDF p. 1–2). About 400 candidate problems were screened down to 36 (Singularity Hub). Some outlets give 18 fields (search summaries only).

### Evidence quality

- **Reported only.** The Science article gives no independent validation of the preprints or of the protocols' effectiveness.
- **Human role.** The tools "still needs extensive human involvement and judgment" (Science p. 2). The model "lacked research taste" (p. 3).
- **Criticism.** Readers on a Voynich-manuscript forum called that paper "slop" (p. 3). On colleagues' advice, Schwartz withheld insufficiently validated results (p. 3).
- **Funding.** Anthropic funded the project, and the skills carry Anthropic copyright (`skills_README.md` §"License and attribution"). Treat this as a practitioner's account, not a measured result.

### Failure modes Schwartz reports

These match the failures INIT.md's verification rules exist to catch.

- **Premature victory.** "Claude loves to declare victory. 'Done, with one asterisk' is often 'not done at all.'" (Anthropic post, failure-modes list).
- **Automated checks.** "Even with all the monitors I set up, I've found the automated checks still can't be trusted." He asks to see plots himself (same list).
- **Outside his field.** He "found it harder to tell when Claude was overselling its findings in fields he was less familiar with" and brought in field experts (Singularity Hub).
- **Grinding instead of building tools.** The model ran long calculations instead of building tools; he had to say "think smarter, not harder" (Anthropic post).

### Mapping to INIT.md

| ID | BootLoops protocol (locator) | INIT.md before this report | Gap | Impact |
|---|---|---|---|---|
| R1 | acceptance-gate §"The procedure" steps 0 and 2; independence-bookkeeping §"The one-way contamination rule"; planted-truth step 0 | §"Findings and Checks": checks must be able to fail. Fresh-context review is independence of context only. | A check can share the blind spot it is meant to catch, for example a test built from the same misreading. A check designed after the result is chosen to pass. | High |
| R2 | acceptance-gate step 8 ("An honest OPEN is a result; a false CLOSED is damage") | §"Inconsistency Handling": status records are claims when read. | No rule for how a claim is written. "Done, with one asterisk" is unregulated. | High |
| R3 | reading-contract, THE CONTRACT and steps 1–3 | §"Report Files": read depth is recorded per source. | A claim cannot be traced to where the source states it, so memory can pass as reading. | Medium |
| R4 | tool-stewardship §"The four-question page", question 4 | §"Skills": content lists failure modes encountered. | No statement of what valid output looks like. | Low–Medium |
| G1 | Singularity Hub (out-of-field overselling); bootloops.ai (domain experts brought in) | §"VALIDATION.md": criteria are human-owned. | Assumes the operator can judge the result. A team of one has no outside reviewer when a project leaves the operator's field. | Medium; no fix proposed |

- **Covered already:** checks seen to fail (planted-truth corruption tests ≈ seeded fault), fresh-context review (Schwartz's separate adversarial-referee session), agents not weakening checks, and mechanical enforcement.
- **Domain-specific, not adopted as rules:** timing-discipline (compute planning; better as a project skill), referee-sim (audit of an outward-facing document), prove-protocol, constant-recognition. Research projects can install these from the `skills` repo directly.
- **Overlap with prior report:** R1 partly addresses gaps A19 and A25 in `reports/practical_realization_lists.md` (surprising positives; post-hoc explanation of failure).

## Implications

- **INIT.md edits, from R1–R4:**
  - §"Findings and Checks" gains "Checks must be independent" and "Claims are closed or open".
  - §"Report Files" per-report content requires locators for load-bearing claims.
  - §"Skills" content adds what valid output looks like and how to check it.
- **G1 is still open.** Possible home: `ancillary/HUMAN.md` or §"VALIDATION.md".
- **Inspiration entry:** INSPIRATIONS.md §"Executable specification and verification-first".
- **Durable decisions:** DECISIONS.md, 2026-11-05.

## References

Local copies are in `reference/` and are not committed.

- Zhao, C. "Problems in 22 scientific fields had solutions hiding in plain sight. An AI has found them." *Science* News, 2026-10-09; Vol 394, Issue 6822. doi:10.1126/science.zwu3e54. https://www.science.org/content/article/problems-22-scientific-fields-had-solutions-hiding-plain-sight-ai-has-found-them. Local: `reference/Problems in 22 scientific fields had solutions hiding in plain sight. An AI has found them _ Science _ AAAS.pdf` (saved by operator; direct fetch returned 403). Read in full.
- Schwartz, M. D. "Claude-shaped science." Anthropic research blog, 2026-10-01 (date per Science). https://www.anthropic.com/research/claude-shaped-science. Local: `reference/anthropic_claude_shaped_science.html`. Read first as a fetch-tool summary; quoted passages then checked against the local copy.
- Gent, E. "New AI tool could help scientists make rare cross-disciplinary leaps more common." Singularity Hub, 2026-10-19. https://singularityhub.com/2026/10/19/new-ai-tool-could-help-scientists-make-rare-cross-disciplinary-leaps-more-common/. Local: `reference/singularityhub_bootloops_2026-10-19.html`. Read first as a fetch-tool summary; quoted passage then checked against the local copy.
- BootLoops-ai. `bootloops` repository, README, commit 95dfb72 (2026-10-22). https://github.com/BootLoops-ai/bootloops. Local: `reference/bootloops_skills_ca89227/bootloops_README_95dfb72.md`. README read in full; tool code not read.
- BootLoops-ai. `skills` repository, commit ca89227 (2026-09-30). https://github.com/BootLoops-ai/skills. Local: `reference/bootloops_skills_ca89227/`. README and roster read in full. SKILL.md files read in part:
  - acceptance-gate: lines 1–120 of 209.
  - independence-bookkeeping: lines 1–80 of 192.
  - tool-stewardship: lines 1–70 of 95.
  - referee-sim: lines 1–60 of 123.
  - timing-discipline: lines 1–50 of 184.
  - reading-contract: lines 1–45 of 206.
  - planted-truth: opening section only.
  - Not read: constant-recognition, prove-protocol, lit-review, ref-check, prose-lint (roster lines only).
- BootLoops. Project site. https://www.bootloops.ai. Local: `reference/bootloops_ai_home.html`. Fetch-tool summary only.
- Search summaries (2026-11-05) of the-decoder.com, unite.ai, runtimewire.com and ecosistemastartup.com coverage. Not read; used only to note the 18-versus-22 field-count discrepancy.
