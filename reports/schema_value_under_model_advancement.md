# Schema Value Under Model Advancement

**Date:** 2026-11-17
**Status:** current
**Reassess:** 2027-11 (12 months).
**Baseline:** INIT.md version 2026-11-17, after the approval-seeking relaxations and checkpoint review of the same date (DECISIONS.md 2026-11-17 entries).
**Provenance:** AI judgment (Opus 5.5) from a session discussion with the operator. Sourced claims carry locators; everything else is inference. No new measurement.

## Question

- As models improve, do INIT.md's project-management rules still add value, or do they now over-constrain capable models?
- Operator framing: the rules partly compensate for human limits (evolutionary timescales are years, not months); that compensation may now cost productivity.

## Findings

### 1. INIT.md rules fall into three kinds that age differently

| Kind | Examples | Compensates for | Trajectory (inference) |
|---|---|---|---|
| How the model should work | Ask thresholds, verify loops, surgical edits, writing style, most of CODING_PRACTICES.md | Model weakness | Decaying fast; expect near-zero within a few model generations |
| State the model cannot see | VISION.md, DECISIONS.md, OPERATIONS.md, `handover/`, `reports/` | Missing memory across sessions | Durable; rising value with parallel sessions |
| Human judgment and attention | Elicited guideposts, VALIDATION.md human-owned, checkpoint reviews, HUMAN.md, §"Findings and Checks" | Human limits; partly model self-judgment | Durable as gates; verification moves into harness mechanisms |

### 2. Evidence for the first kind decaying

- Redundancy study, Opus 5.5 medium: 8 of 10 probes run read implicit (followed without the directive). Unaudited, partial batch. DECISIONS.md 2026-11-06 entry, update 2026-11-13; `reports/schema_redundancy_ablation.md`.
- Anthropic guidance: remove explicit verification instructions (Opus 5, carried to 5.5); accumulated caution causes unnecessary approval-seeking (Fable 5.2). `reports/coding_practices_model_currency.md` §2.
- Claude Code team talk (second-hand): emphatic CLAUDE.md lines cause extra tool calls and worse results on Opus 5.5; CLAUDE.md should hold only what Claude cannot see from the code. `reports/coding_practices_model_currency.md` §6; transcript l. 5–7.

### 3. The second kind is an information problem, not a capability problem

- A more capable model still starts each session without the project's history: why an alternative was rejected, which host must not be touched, what the operator intends.
- These pass the talk's test ("could Claude figure this out by reading the code?") as non-derivable. Inference.
- With many concurrent sessions ("managers for dozens of sessions", transcript l. 2), shared written state is how parallel agents coordinate. Inference.

### 4. The third kind protects the actual bottleneck

- As execution gets cheaper, the scarce resource is the operator's attention: knowing what is true, decided and safe to trust. Inference.
- The productivity cost lies in gating *reversible* steps on human approval, not in the human owning intent. The 2026-11-17 edits removed the former and kept the latter.
- Verification rules also compensate for a live model weakness: self-judgment "still really iffy" (Anthropic Claude engineering lead, `reports/coding_practices_model_currency.md` §1, transcript D-SVFneJ_Nk l. 168). Expected to migrate from prose into hooks, deny rules and separate-context reviewers, as this project did on 2026-11-17 (`.claude/settings.json`).

### 5. Process ceremony likely over-weighted (inference)

- Sequential drafting of the flowdown files assumes expensive work. Once code exists, ARCHITECTURE.md for software is largely derivable on demand.
- §"File Updates" propagation checklist: a strong model needs the one-hop cap more than the list.
- §"Scaffolding Files" naming example and file-structure template: 62 lines (INIT.md 2026-11-17, from `### Naming and Organization` to `### Integration with IMPLEMENTATION.md`, counted by awk) for what is essentially a field list.

### 6. Limits of the external evidence

- Published context-file studies (ETH Zurich Feb 2026; 288-run ablation Jul 2026) measure single-task coding correctness and find little gain (`reports/coding_practices_model_currency.md` §3, search summaries only). They do not measure multi-session continuity or governance, where the state layer is meant to pay off.

## Implications

- **Projected shape (inference):** INIT.md moves from a process spec to (a) a spec for non-derivable state, (b) a short list of human decision points (intent, acceptance criteria, irreversible actions), (c) mechanical enforcement.
- **Four-way review test, per directive:**
  1. Records something the model cannot derive → keep.
  2. Protects operator judgment or an irreversible action → keep; enforce mechanically where possible.
  3. Tells the model how to do something it already does well → delete, or measure first via the redundancy study.
  4. Gates a reversible step on human approval → remove.
- **Instrument:** the redundancy study (`study/`), paused 2026-11-17, resumes as tokens allow. Add a cost/side-effect measure (unnecessary questions, redundant re-checks, tokens) per `reports/coding_practices_model_currency.md` §"Implications".
- **Candidate future edits (not applied):** make ARCHITECTURE.md derivable-on-demand for software projects with code; shorten the propagation checklist and scaffolding template; add the four-way test to the checkpoint "what can be removed" question.

## Reassessment checklist (2027-11)

- Which first-kind directives remain, and does the study still read them as needed on the then-current models?
- Did any second-kind file stop earning its keep (never read, never consulted by sessions)?
- Did human gates move into harness mechanisms, and did approval-seeking drop?
- Has the "Schema longevity is an experiment" guidepost (VISION.md) resolved toward survival, modification or replacement?

## References

- `reports/coding_practices_model_currency.md` (2026-11-16, updated 2026-11-17) and its references: Anthropic prompting docs (Opus 5, Opus 5.5, Fable 5.2), interview YouTube `D-SVFneJ_Nk`, video YouTube `8Pg6G5h05hk`. Local transcripts: `reference/youtube_D-SVFneJ_Nk_transcript_2026-11-16.txt`, `reference/youtube_8Pg6G5h05hk_transcript_2026-11-17.txt`. Read in full.
- `reports/schema_redundancy_ablation.md` and DECISIONS.md 2026-11-06 entry (study status and partial Opus results). Read.
- Third-party context-file studies: via `reports/coding_practices_model_currency.md` §3. Search summaries only.
