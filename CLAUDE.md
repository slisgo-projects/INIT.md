# CLAUDE.md

**Initialized against INIT.md version:** 2026-07-12

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A meta-specification for AI-human collaboration on project setup. The repo is also structured recursively per its own schema, so it is both the deliverable and the first project applying it.

No code, no build, no tests — deliverables are markdown spec files that downstream projects copy or follow.

The working directory is named `INIT.md` (a directory, not a file). Targeted at team-of-one (one human + many AI agents), not multi-person institutional teams.

## Markdown hierarchy

Five flowdown groups plus a companion tier (per INIT.md §"Project Markdown Files"):

- **Foundational**: VISION.md, MOTIVATION.md.
- **Sequential**: INSPIRATIONS.md, ARCHITECTURE.md, USE_CASES.md, VALIDATION.md, IMPLEMENTATION.md. VALIDATION.md and IMPLEMENTATION.md deliberately skipped for this recursive project (see DECISIONS.md 2026-05-10).
- **Cross-cutting**: GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md.
- **Scaffolding**: none in this project.
- **Reference**: `reference/HUMAN.md` (optional sustainability companion; seed documents + AI topic reports not yet present in this project).
- **Companion**: INIT.md, USE_CASE_INIT.md, CODING_PRACTICES.md, CLAUDE.md.

**Context-refresh rule:** load foundational + cross-cutting by default. Scaffolding only when implementing the relevant phase. Reference only when the session touches the file's topic (HUMAN.md loads when workflow context is needed). Companion files load on demand (CLAUDE.md auto-loaded; INIT.md when schema questions arise; USE_CASE_INIT.md when a use case is being formulated or refined, inline or extracted).

INIT.md is authoritative for required content per file.

## Files

**Deliverable files** (the spec being authored):
- **INIT.md** — authoritative spec for the project markdown hierarchy. Read first.
- **HUMAN.md** — optional reference companion to INIT.md (lives in `reference/`). Human side of the collaboration and sustainability rationale. Not referenced by INIT.md; not a required part of the flowdown.
- **CODING_PRACTICES.md** — behavioral guidelines copied into downstream projects' CLAUDE.md per INIT.md §"CLAUDE.md Bootstrap."
- **USE_CASE_INIT.md** — universal use-case formulation protocol. Governs every use case specification: formulated inline in `USE_CASES.md` by default; extracted to its own `USE_CASE_<identifier>.md` only when an individual case grows unwieldy (length-triggered; protocol identical either way). Defines universal foundational elements plus a section per category (A–F); AI selects primary and optional secondary category from the user's description and applies the corresponding structure.

**Project files** (this repo structured per INIT.md schema):
- **VISION.md** — north-star and guideposts. AI-optimized.
- **MOTIVATION.md** — developed argument behind guideposts. Prose for shared human-AI reading; the deliberate prose exception.
- **GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md** — cross-cutting; populate as the project develops.
- **INSPIRATIONS.md** and onward — sequential files drafted in order per INIT.md §"Sequential Files."

## Working in this repo

**Edits follow the rules INIT.md itself defines.** Specifically:

- AI-optimized files (everything except MOTIVATION.md): directive voice, bullets over prose, no embedded rationale, no filler. See INIT.md §"Writing Style for AI-Optimized Files."
- `reference/HUMAN.md` is prose for a human reader and exempt from the AI-optimization rules, except for the "Human Responsibilities" list near its top.

**File Updates rule** (INIT.md §"File Updates"): when changing one file, propagate logically related updates to other files. Cap propagation at one hop. Report what was propagated. Full consistency sweeps are a separate deliberate act.

**Inconsistency Handling** (INIT.md §"Inconsistency Handling"): flag contradictions, do not silently resolve.

**Scaffolding files** are not read on context refresh, are preserved in `scaffolding/integrated/` after phase completion (not deleted), and supplement DECISIONS.md rather than replace it.

This is not a git repository.

## Coding behavioral guidelines

This is a no-code meta-spec; CODING_PRACTICES.md applies to spec edits by analogy (surface tradeoffs before writing; minimal change; surgical edits; goal-driven verification). Full contents copied below per INIT.md §"CLAUDE.md Bootstrap" — keep in sync with CODING_PRACTICES.md if it changes.

---

Behavioral guidelines to reduce common LLM coding mistakes (https://github.com/multica-ai/andrej-karpathy-skills).

**Tradeoff:** these guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

Test: every changed line traces directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria enable independent looping. Weak criteria ("make it work") require constant clarification.
