# CLAUDE.md

**Initialized against INIT.md version:** 2026-11-04

**Auto-loaded every session** (per INIT.md §"CLAUDE.md Bootstrap"):

@INIT.md
@VISION.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A meta-specification for AI-human collaboration on project setup. The repo is also structured recursively per its own schema, so it is both the deliverable and the first project applying it.

No code, no build, no tests — deliverables are markdown spec files that downstream projects copy or follow.

The working directory is named `INIT.md` (a directory, not a file). Targeted at team-of-one (one human + many AI agents), not multi-person institutional teams.

## Markdown hierarchy

Seven flowdown groups plus a companion tier (per INIT.md §"Project Markdown Files"):

- **Foundational**: VISION.md, MOTIVATION.md.
- **Sequential**: INSPIRATIONS.md, ARCHITECTURE.md, USE_CASES.md, VALIDATION.md, IMPLEMENTATION.md. VALIDATION.md and IMPLEMENTATION.md deliberately skipped for this recursive project (see DECISIONS.md 2026-05-10).
- **Cross-cutting**: GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md. No OPERATIONS.md — this project deploys nothing.
- **Scaffolding**: none in this project.
- **Reference**: `reference/Seramount-The-AI-Productivity-Paradox-Insight-Paper.pdf`, `reference/The AI Point Elasticity_ When More Capacity Becomes a Liability.pdf` (seed documents — externally generated inputs). Report-source copies saved here are local only; `.gitignore` keeps them out of the public repo.
- **Reports**: `reports/ai_work_intensification.md`, `reports/ai_research_inversion.md`, `reports/practical_realization_lists.md` (AI-authored topic reports from mini-investigations).
- **Continuity**: none in this project (`handover/`; per-work-area session-continuity records). Schema edits are single-session and land in DECISIONS.md.
- **Companion**: INIT.md, USE_CASE_INIT.md, CODING_PRACTICES.md, CLAUDE.md. (HUMAN.md is an optional companion living in `ancillary/HUMAN.md`, not at root.)
- **Ancillary**: `ancillary/HUMAN.md` — optional sustainability companion (companion group; registered here per §"Project Markdown Files" Directory layout). `ancillary/` is a path, not a flowdown group.

**Context-refresh rule:** load foundational + cross-cutting by default. IMPLEMENTATION.md when the session's work touches a phase (none in this project). Scaffolding only when implementing the relevant phase. Reference and reports only when the session touches the file's topic. Continuity only for the work area being resumed, pulled in by the user. Companion files load on demand (CLAUDE.md and INIT.md auto-loaded; HUMAN.md when workflow context is needed; USE_CASE_INIT.md when a use case is being formulated or refined, inline or extracted).

INIT.md is authoritative for required content per file.

## Files

**Deliverable files** (the spec being authored):
- **INIT.md** — authoritative spec for the project markdown hierarchy. Read first.
- **HUMAN.md** — optional companion to INIT.md (lives in `ancillary/HUMAN.md`). Human side of the collaboration and sustainability rationale. Not referenced by INIT.md; not a required part of the flowdown.
- **CODING_PRACTICES.md** — behavioral guidelines imported into downstream projects' CLAUDE.md per INIT.md §"CLAUDE.md Bootstrap."
- **USE_CASE_INIT.md** — universal use-case formulation protocol. Governs every use case specification: formulated inline in `USE_CASES.md` by default; extracted to its own `USE_CASE_<identifier>.md` only when an individual case grows unwieldy (length-triggered; protocol identical either way). Defines universal foundational elements plus a section per category (A–F); AI selects primary and optional secondary category from the user's description and applies the corresponding structure.

**Project files** (this repo structured per INIT.md schema):
- **VISION.md** — north-star and guideposts. AI-optimized.
- **MOTIVATION.md** — developed argument behind guideposts. Prose for shared human-AI reading; the deliberate prose exception.
- **GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md** — cross-cutting; populate as the project develops.
- **INSPIRATIONS.md** and onward — sequential files drafted in order per INIT.md §"Sequential Files."

## Working in this repo

**Edits follow the rules INIT.md itself defines.** Specifically:

- AI-optimized files (everything except MOTIVATION.md): directive voice, bullets over prose, no embedded rationale, no filler. See INIT.md §"Writing Style for AI-Optimized Files."
- `ancillary/HUMAN.md` is prose for a human reader and exempt from the AI-optimization rules, except for the "Human Responsibilities" list near its top.

**File Updates rule** (INIT.md §"File Updates"): when changing one file, propagate logically related updates to other files. Cap propagation at one hop. Report what was propagated. Full consistency sweeps are a separate deliberate act.

**Inconsistency Handling** (INIT.md §"Inconsistency Handling"): flag contradictions, do not silently resolve.

**Scaffolding files** are not read on context refresh, are preserved in `scaffolding/integrated/` after phase completion (not deleted), and supplement DECISIONS.md rather than replace it.

Git repository; commit only on request.

## Coding behavioral guidelines

This is a no-code meta-spec; CODING_PRACTICES.md applies to spec edits by analogy (surface tradeoffs before writing; minimal change; surgical edits; goal-driven verification). Imported per INIT.md §"CLAUDE.md Bootstrap":

@CODING_PRACTICES.md
