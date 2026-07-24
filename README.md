# INIT.md

A meta-specification for AI–human collaboration on a project. `INIT.md` defines a markdown hierarchy that captures a project's scope, objectives, architecture, and rationale as a coherent "flowdown" — structured files drafted in order, optimized primarily for an AI assistant to re-ingest in future sessions, with the deliberate exception of `MOTIVATION.md` (prose for the human).

This repository is also structured per its own schema: the spec is the deliverable and the first project applying it. There is no code, build, or tests — the deliverables are these markdown files.

## The flowdown

Five file groups plus a companion tier:

- **Foundational** — `VISION.md`, `MOTIVATION.md`
- **Sequential** (drafted in order) — `INSPIRATIONS.md`, `ARCHITECTURE.md`, `USE_CASES.md`, `VALIDATION.md`, `IMPLEMENTATION.md`
- **Cross-cutting** — `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`
- **Scaffolding** — phase-specific working files (see `INIT.md`)
- **Reference** — externally generated seed documents in `reference/`
- **Reports** — AI-authored topic reports in `reports/`

Companion files (`INIT.md`, `USE_CASE_INIT.md`, `CODING_PRACTICES.md`, `CLAUDE.md`) sit outside the flowdown and govern or accompany it. 

## Initializing a new project

> **The only files from this repo that you need: `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md`.** 

`INIT.md` is authoritative and controls the document flowdown. Steps:

1. **Copy in the spec.** Put `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md` into the new project's directory. 
2. **Set the AI tool to "auto" mode.** Otherwise, you have to answer endless premission requests. For Claude Code in a Linux terminal, press SHIFT+TAB until it says "auto mode on" at the bottom of the window.
3. **Provide a vision.** Give intialization instructions to the AI: "Please read INIT.md in the current directory. I would like to create a new project because: (1) ... (2) ... (3) ... . The following are the desired deliverables: (a) ... (b) ... (c) ... ." Alternatively, you can put the seed information in a file in `reference/` and ask the AI to read it. If you don't want to provide a project description beforehand, the AI leads a structured interview before drafting anything.
4. **Draft one sequential file at a time.** The AI will lead the user through the INIT.md project specification, first proposing a draft of `INSPIRATIONS.md` ("prior art" from its training data or a web search) for review; and then advancing one file at a time for the document flowdown, confirming satisfaction before proceeding.  The AI is instructed to ask about (don't ghost-write) judgment-heavy content; flagging inconsistencies rather than silently resolving them.

## Working rules

- **File Updates** — touch the requested file, then propagate logically related updates to maintain self-consistency. Cap propagation at one hop; full consistency sweeps are a separate deliberate act.
- **Inconsistency Handling** — flag contradictions during drafting and review; do not silently resolve them.
- **Context refresh** — load foundational + cross-cutting files by default; scaffolding only when implementing the relevant phase; reference and reports only when the session touches the file's topic.
- **Versioning** — `INIT.md` carries a date-based version stamp; bump on substantive change, not typo fixes.
