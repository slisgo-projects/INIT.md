# INIT.md

A meta-specification for AI–human collaboration on a project. 

`INIT.md` defines a markdown hierarchy that captures a project's scope, objectives, architecture, and rationale as a coherent "flowdown" — structured files drafted in a specified order. 

The files are primarily optimized for an AI assistant to read, with the deliberate exception of `MOTIVATION.md` (prose for the human).

This repository is structured recursively per its own schema: the spec is the deliverable and also a project defined by the spec.

## The document flowdown

Seven file groups and a companion tier:

- **Foundational** — `VISION.md`, `MOTIVATION.md`
- **Sequential** (drafted in order) — `INSPIRATIONS.md`, `ARCHITECTURE.md`, `USE_CASES.md`, `VALIDATION.md`, `IMPLEMENTATION.md`
- **Cross-cutting** — `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`
- **Scaffolding** — phase/stage-specific working files (see `INIT.md`) in scaffolding/
- **Reference** — externally generated seed documents in `reference/`
- **Reports** — AI-authored topic reports in `reports/`
- **Ancillary** — All project files that do not fit into the above scheme live in `ancillary/`

Companion files (`INIT.md`, `USE_CASE_INIT.md`, `CODING_PRACTICES.md`, `CLAUDE.md`, `README.md`) sit outside the flowdown and govern or accompany it. 

## Initializing a new project

> **The only files from this repo that you need: `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md`.** 

`INIT.md` is authoritative and controls the document flowdown. 

Steps:

1. **Copy in the spec.** Put `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md` into the new project's directory. 
2. **Set the AI tool to "auto" mode.** Otherwise, you have to answer endless premission requests. For Claude Code in a Linux terminal, press SHIFT+TAB until it says "auto mode on" at the bottom of the window.
3. **Provide a vision.** Give intialization instructions to the AI: "Please read INIT.md in the current directory. I would like to create a new project because: (1) ... (2) ... (3) ... . The following are the desired deliverables: (a) ... (b) ... (c) ... ." Alternatively, you can put this seed information in a file in `reference/` and ask the AI to read it. If you don't want to provide a project description beforehand, the AI will lead a structured interview (untested).
4. **One sequential file is drafted at a time.** The AI will lead the user through the INIT.md project specification, first proposing a draft of `INSPIRATIONS.md` ("prior art" from its training data or a web search) for review; and then advancing one file at a time for the document flowdown, confirming satisfaction before proceeding.  The AI is instructed to ask about (don't ghost-write) judgment-heavy content; flagging inconsistencies rather than silently resolving them.

For a complex and ambitious project with steady back-and-forth between the human and the AI, the setup process can take several hours. 

The flowdown can use a large fraction of the context window on a full refresh, which is not ideal but workable. Hopefully, the burden is reduced as tokens become cheaper, window sizes increase, and the INIT.md scheme is refined.

## Document scheme working rules for the AI

- **File Updates** — touch the requested file, then propagate logically related updates to maintain self-consistency. Cap propagation at one hop; full consistency sweeps are a separate deliberate act initiated by the user, i.e. "Please read all project files and check for self-consistency".
- **Inconsistency Handling** — flag contradictions during drafting and review; do not silently resolve them.
- **Context refresh** — load foundational + cross-cutting files by default; scaffolding only when implementing the relevant phase; reference and reports only when the session touches the file's topic.
- **Versioning** — `INIT.md` carries author information and a date-based version stamp; bump on substantive change, not typo fixes.

## AI installation

Instructions for installing and executing an AI are in `ancillary/AI_install.md`.
