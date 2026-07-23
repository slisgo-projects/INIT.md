# INIT.md

A meta-specification for AI–human collaboration on project setup. `INIT.md` defines a markdown hierarchy that captures a project's scope, objectives, architecture, and rationale as a coherent "flowdown" — structured files drafted in order, optimized primarily for an AI assistant to re-ingest in future sessions, with the deliberate exception of `MOTIVATION.md` (prose for the human).

This repository is also structured per its own schema: the spec is the deliverable and the first project applying it. There is no code, build, or tests — the deliverables are these markdown files.

## The flowdown

Five file groups plus a companion tier:

- **Foundational** — `VISION.md`, `MOTIVATION.md`
- **Sequential** (drafted in order) — `INSPIRATIONS.md`, `ARCHITECTURE.md`, `USE_CASES.md`, `VALIDATION.md`, `IMPLEMENTATION.md`
- **Cross-cutting** — `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`
- **Scaffolding** — phase-specific working files (see `INIT.md`)
- **Reference** — externally generated seed documents in `reference/`
- **Reports** — AI-authored topic reports in `reports/`

Companion files (`INIT.md`, `USE_CASE_INIT.md`, `CODING_PRACTICES.md`, `CLAUDE.md`) sit outside the flowdown and govern or accompany it. `HUMAN.md` is an optional companion kept in `ancillary/` to keep the root clean.

## Initializing a new project

> **The artifacts to copy or follow into a downstream project are `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md`.** These three files are the spec. A downstream project sets itself up by taking them and filling in its own flowdown files. (`HUMAN.md` is optional — it lives in `ancillary/` as a sustainability companion, not a required part of the flowdown.)

`INIT.md` is authoritative. The summary below captures the entry protocol; read `INIT.md` itself before drafting.

1. **Copy in the spec.** Take `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md` into the new project's directory. Optionally also copy `ancillary/HUMAN.md` if you want the sustainability framing.
2. **Provide a vision.** On first invocation ("Let's set up a project") supply `VISION.md` (as a file or prompt content), initial suggestions on inspirations/architecture/implementation, and optionally seed documents in `reference/`. If you arrive without `VISION.md`, the AI elicits it by structured interview before drafting anything.
3. **Bootstrap `CLAUDE.md`.** Populate it with (a) the coding behavioral guidelines from `CODING_PRACTICES.md`, (b) a markdown-hierarchy stub listing the file groups and the context-refresh rule, and (c) a version stamp: `Initialized against INIT.md version: YYYY-MM-DD`.
4. **Create placeholders.** Create empty placeholder files for the cross-cutting files (`GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`) and `MOTIVATION.md`, to be populated as the project progresses.
5. **Draft one sequential file at a time.** The AI proposes a draft of `INSPIRATIONS.md` first for review; advance one file at a time, confirming satisfaction before proceeding. Do not generate all sequential files at once. Elicit (don't ghost-write) judgment-heavy content; flag inconsistencies rather than silently resolving them.

## Working rules

- **File Updates** — touch the requested file, then propagate logically related updates to maintain self-consistency. Cap propagation at one hop; full consistency sweeps are a separate deliberate act.
- **Inconsistency Handling** — flag contradictions during drafting and review; do not silently resolve them.
- **Context refresh** — load foundational + cross-cutting files by default; scaffolding only when implementing the relevant phase; reference and reports only when the session touches the file's topic.
- **Versioning** — `INIT.md` carries a date-based version stamp; bump on substantive change, not typo fixes.