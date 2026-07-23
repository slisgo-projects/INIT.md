# INIT.md

A meta-specification for AI–human collaboration on project setup. `INIT.md` defines a markdown hierarchy that captures a project's scope, objectives, architecture, and rationale as a coherent "flowdown" — structured files drafted in order, optimized primarily for an AI assistant to re-ingest in future sessions, with the deliberate exception of `MOTIVATION.md` (prose for the human).

This repository is also structured per its own schema: the spec is the deliverable and the first project applying it. There is no code, build, or tests — the deliverables are these markdown files.

## The flowdown

Five file groups plus a companion tier:

- **Foundational** — `VISION.md`, `MOTIVATION.md`
- **Sequential** (drafted in order) — `INSPIRATIONS.md`, `ARCHITECTURE.md`, `USE_CASES.md`, `VALIDATION.md`, `IMPLEMENTATION.md`
- **Cross-cutting** — `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`
- **Scaffolding** — phase-specific working files (see `INIT.md`)
- **Reference** — seed documents and AI topic reports in `reference/`

Companion files (`INIT.md`, `USE_CASE_INIT.md`, `HUMAN.md`, `CODING_PRACTICES.md`, `CLAUDE.md`) sit outside the flowdown and govern or accompany it.

## Initializing a new project

`INIT.md` is authoritative. The summary below captures the entry protocol; read `INIT.md` itself before drafting.

1. **Provide a vision.** On first invocation ("Let's set up a project") supply `VISION.md` (as a file or prompt content), initial suggestions on inspirations/architecture/implementation, and optionally seed documents in `reference/`. If you arrive without `VISION.md`, the AI elicits it by structured interview before drafting anything.
2. **Bootstrap `CLAUDE.md`.** Populate it with (a) the coding behavioral guidelines from `CODING_PRACTICES.md`, (b) a markdown-hierarchy stub listing the file groups and the context-refresh rule, and (c) a version stamp: `Initialized against INIT.md version: YYYY-MM-DD`.
3. **Create placeholders.** Create empty placeholder files for the cross-cutting files (`GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`) and `MOTIVATION.md`, to be populated as the project progresses.
4. **Draft one sequential file at a time.** The AI proposes a draft of `INSPIRATIONS.md` first for review; advance one file at a time, confirming satisfaction before proceeding. Do not generate all sequential files at once. Elicit (don't ghost-write) judgment-heavy content; flag inconsistencies rather than silently resolving them.

## Working rules

- **File Updates** — touch the requested file, then propagate logically related updates to maintain self-consistency. Cap propagation at one hop; full consistency sweeps are a separate deliberate act.
- **Inconsistency Handling** — flag contradictions during drafting and review; do not silently resolve them.
- **Context refresh** — load foundational + cross-cutting files by default; scaffolding only when implementing the relevant phase; reference only when the session touches the file's topic.
- **Versioning** — `INIT.md` carries a date-based version stamp; bump on substantive change, not typo fixes.

## Repository note

This is not a git repo for application code — it is the spec itself. `INIT.md`, `HUMAN.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md` are the artifacts downstream projects copy or follow.