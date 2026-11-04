# INIT.md

**Authors:** S. Lisgo, Opus 4.7, Fable 5, Opus 5, Fable 5.1, Opus 5.5

**Version:** 2026-11-03 (date of last substantive change; see §"Versioning")

**License:** Copyright (c) 2026 S. Lisgo. MIT License: https://github.com/slisgo-projects/INIT.md/blob/main/LICENSE

Guidance for the AI assistant on drafting and maintaining the markdown files that define a project.

**Goal:** a coherent flowdown of activity guidelines capturing project scope, objectives, milestones, timelines, resource requirements, stakeholders, and desired impact.

**Primary reader:** an AI in future sessions, in most cases. INIT.md and VISION.md auto-load every session via CLAUDE.md imports (see §"CLAUDE.md Bootstrap"). When refreshing context, the user typically requests MOTIVATION.md plus whatever lower-level files are appropriate; IMPLEMENTATION.md loads on the trigger in §"Context Refresh". Favor structured, explicit content over narrative prose, and write so files re-ingest efficiently. This is the default optimization for project files.

**Deliberate exception:** MOTIVATION.md is written in prose for the human running the project. Do not AI-optimize it; AI sessions still read it on context refresh.

Converging on a clean project characterization is iterative.

# Entry Protocol

On first invocation ("Let's set up a project"), the user provides:
- VISION.md, either as a file or as content in the prompt.
- Initial suggestions on inspirations, architecture, and implementation.
- Optionally, seed documents in `reference/` as background to VISION.md and MOTIVATION.md (see §"Reference Files").

**Interview variant.** When the user arrives without VISION.md: read any `reference/` seed documents, then elicit VISION.md by structured interview before drafting anything. Ask open-ended questions derived from the VISION.md required content (north star, guideposts, objectives) and the MOTIVATION.md per-strand structure (problem, approach, limits), one question at a time, each building on prior answers. Draft only from the user's answers; do not propose answers. Interview output seeds MOTIVATION.md; it does not complete it.

Elicit before drafting for judgment-heavy content anywhere in the flowdown (guideposts, objectives, strategic decomposition). Do not ghost-write.

First move: read VISION.md and the user's suggestions. Create empty placeholder files for all cross-cutting files (GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md), to be populated as the project progresses. Create an empty placeholder for MOTIVATION.md, to be developed iteratively as the user works through their reasons for the project. Then propose a draft of the first sequential file (INSPIRATIONS.md) for review.

MOTIVATION.md is drafted iteratively across sessions, not in a single pass. Capture motivation material whenever the user surfaces it, regardless of which sequential file is currently in focus.

Advance one sequential file at a time. Confirm satisfaction before proceeding.

Do not generate all sequential files at once.

# Inconsistency Handling

During drafting: if inconsistencies surface between files, flag them and iterate with the user. Do not silently resolve them.

Status records (phase states, status lines, "not yet run" caveats) are claims, not evidence. Before asserting what is done, collected, or available, check the artifact itself: file presence, contents, checksums, the built or deployed thing. On divergence, correct the record and log the correction in DECISIONS.md.

During review: the user will request thorough reviews at checkpoints. Surface any inconsistencies for resolution. Run checkpoint reviews in a context that did not author the changes under review. Checkpoint reviews also ask what can be removed: unnecessary content, requirements, phases, recurring records. Removed items follow the owning file's archive rule, if any.

# Findings and Checks

- **Negative findings require a control.** Before recording anything as unavailable or broken, either show the probe succeeds on a known-good instance, or reproduce the failure through an independent pathway. Unconfirmed negatives are `open` questions in DECISIONS.md, not constraints.
- **Checks require a control.** A check is evidence only after it has been seen to fail: run it before the work exists, or against a seeded fault.

# File Updates

When the user requests a change mid-project: touch the requested file, then propagate logically related updates to maintain self-consistency. Report what was propagated.

**Propagation cap:** one hop from the changed file. Full consistency sweeps are a separate, deliberate act.

**Propagation checklist.** For each first-hop candidate, check whether the edit forces an update:
- ARCHITECTURE.md — element entries, dependencies, file or component enumerations.
- INTERFACES.md — contracts at element boundaries the edit crosses.
- IMPLEMENTATION.md — phases touching affected elements.
- USE_CASES.md — category implications or per-use-case entries affected.
- VALIDATION.md — V&V criteria affected.
- GLOSSARY.md — terms that gain, lose, or shift meaning.
- CONSTRAINTS.md — constraints added, relaxed, or now violated.
- OPERATIONS.md — hosts, access paths, runtime environments, or deploy steps affected.
- DECISIONS.md — when the edit is a choice with alternatives worth recording.
- VISION.md / MOTIVATION.md — guideposts or rationale affected.
- INSPIRATIONS.md — rarely a propagation target; include only if an inspiration's borrow / avoid / relevance assessment is materially affected.
- `reports/` topic reports — rarely a propagation target; mark a report superseded when an edit overturns its findings.
- `handover/` continuity files — the file for the affected work area, when the edit changes its current state or roadmap.

Skip unchanged candidates silently. Surface uncertain cases per §"Inconsistency Handling."

# Versioning

INIT.md carries a date-based version stamp at the top: `Version: YYYY-MM-DD`.

Update the version date on any substantive change — additions, deletions, or content rewrites affecting:
- The file taxonomy or per-file content specs.
- Workflow rules (Entry Protocol, File Updates, Versioning, Inconsistency Handling, Findings and Checks, Context Refresh, Stopping Criteria, Skills, CLAUDE.md Bootstrap).
- Writing style rules.

Do not bump for typo fixes, pure prose touch-ups in MOTIVATION.md, or DECISIONS.md log entries that don't change INIT.md itself.

Downstream projects record the version they were initialized against in their CLAUDE.md bootstrap stub (see §"CLAUDE.md Bootstrap"). When a downstream project is re-bootstrapped against a newer INIT.md, update the recorded version.

Date-based, not semantic. Per-change rationale lives in DECISIONS.md; downstream projects compare their initialization date against INIT.md's current date to scope drift, then read DECISIONS.md entries between those dates for specifics.

# Context Refresh

INIT.md and VISION.md are auto-loaded at session start (see §"CLAUDE.md Bootstrap").

When the user asks for a re-read to refresh context, also re-read by default:
- All **foundational files** (VISION.md, MOTIVATION.md), as these establish what the project is and why it is worth doing.
- All **cross-cutting files** (GLOSSARY.md, CONSTRAINTS.md, INTERFACES.md, DECISIONS.md, and OPERATIONS.md where the project has one), as these apply everywhere.

**Load IMPLEMENTATION.md** whenever the session's work touches an implementation phase — building, changing, verifying, or reporting on a phase deliverable — whether or not the user asked for a re-read. Load it before writing state-of-progress per §"IMPLEMENTATION.md."

**Do NOT** read scaffolding files on context refresh. They are working artifacts. Read them only when implementing the relevant phase. After a phase completes, the scaffolding file is moved to `scaffolding/integrated/` per §"Scaffolding Files," not deleted.

**Do NOT** read reference or report files on context refresh. Load a seed document or topic report only when the session touches its topic (see §"Reference Files" and §"Report Files").

**Do NOT** read continuity files on context refresh. The user pulls the `handover/` file for the work area being resumed into context; loading every area's file defeats the group's purpose (see §"Continuity Files").

# Stopping Criteria

No hard length criterion per file. Length is project-specific.

If a file appears to be growing unwieldy, mention it and ask whether to subdivide. Do not subdivide unilaterally.

Subdivided files use the naming pattern USE_CASE_<identifier>.md, RISK_<identifier>.md, etc.

When a use case is subdivided into its own `USE_CASE_<identifier>.md`, follow USE_CASE_INIT.md (same protocol as inline formulation; extraction changes file location, not protocol).

# Skills

Repeatable operational procedures — executing a software package, accessing a remote resource, build/run/deploy steps — are captured as skills, not rediscovered.

- **Trigger:** when a session works out, or re-derives, such a procedure, capture it as a skill in the same session. Do not wait to be asked. Re-derivation is a mandatory trigger.
- **Location:** `.claude/skills/<name>/SKILL.md` in the project directory. Project-scoped, not `$HOME/.claude/`.
- **Content:** imperative how-to — commands, parameters, prerequisites, failure modes encountered. No secrets; point to credential locations instead.
- **Boundary:** skills hold procedures (how to do); `reports/` topic reports hold findings (what was learned); OPERATIONS.md holds standing facts (what exists, where, who reaches it). A skill for reaching a host cites OPERATIONS.md for the host's identity and access rules rather than restating them. See §"Report Files" and §"OPERATIONS.md."
- **Enforcement:** rules that admit no exceptions are enforced mechanically (hook, CI, script) where the host tool supports it.
- **Coupling:** `SKILL.md` follows the Agent Skills open standard (agentskills.io), supported across vendors. Only the `.claude/skills/` path is Claude Code-specific; other agents use their own skill directory.

# Writing Style for AI-Optimized Files

MOTIVATION.md is prose for the human and exempt from these rules. All other files — including VISION.md — are AI-optimized and must follow them.

**Hard rules:**

- **Directive, not explanatory.** Write what is, not what the section is about. No section preambles ("This file captures..."), no recaps ("As described above...").
- **Bullets over prose.** One concept per bullet. If a point needs a paragraph, it belongs in MOTIVATION.md (why) or DECISIONS.md (rationale), not here.
- **No embedded rationale.** AI-optimized files state the choice; rationale lives in DECISIONS.md. Do not justify entries inline.
- **No filler.** Cut "in order to," "it is important to note," "the following," and similar scaffolding. If a sentence still parses without a phrase, the phrase was filler.
- **Terse definitions.** Glossary-style: term — definition. Not "Term refers to the concept of..."

**Before / after:**

Verbose, explanatory:

> This section captures the various inspirations that have informed the design of the project. Inspirations are projects in development or active use that share characteristics with the current project. They support ideation because everything is a remix.
>
> - Project A: This project does X very well, and we should consider how they approach it. The clean separation between X and Y is something worth borrowing for our own work.

Directive, concise:

> Per entry: name, what to borrow, what to avoid, relevance.
>
> - Project A — does X.
>   - Borrow: clean X/Y separation.
>   - Avoid: tight coupling of X to internal Z.
>   - Relevance: Phase 2 needs the same split.

**Self-check before writing:** could this point be made in fewer words without losing meaning? If yes, cut. If a sentence is explaining what the file is doing rather than carrying content, delete it.

# CLAUDE.md Bootstrap

CLAUDE.md is auto-loaded every session. Populate it once during project setup with four pieces:

1. **Coding behavioral guidelines.** Import CODING_PRACTICES.md with an `@CODING_PRACTICES.md` line, on its own line and outside code spans. Put project-specific coding guidance in CLAUDE.md beside the import. For an AI tool that does not expand `@` imports, paste the file's contents instead.

2. **Markdown hierarchy stub.** A short index of this project's markdown files — its instantiation of the schema. The stub contains:
   - The seven file groups (foundational, sequential, cross-cutting, scaffolding, reference, reports, continuity) and which files belong to each.
   - The context-refresh rule (foundational + cross-cutting by default; IMPLEMENTATION.md when the session's work touches a phase; scaffolding only when implementing the relevant phase; reference and reports only when the session touches the topic; continuity only for the work area being resumed, pulled in by the user).
   - The names of the active `handover/` continuity files and the work area each covers, so a session knows which one to ask for.
   - A pointer to INIT.md as the authoritative source for required content per file.

3. **INIT.md version stamp.** One line near the top of CLAUDE.md: `Initialized against INIT.md version: YYYY-MM-DD`. Records the version of INIT.md the project was bootstrapped against. Updated when the project is re-bootstrapped against a newer INIT.md (see §"Versioning").

4. **Auto-load imports.** Two lines, each on its own line and outside code spans: `@INIT.md` and `@VISION.md`. Claude Code expands them into context at session start, so every session runs under INIT.md's rules and VISION.md's scope unprompted. Path-qualify if either file is not at the project root.

Keep the stub to names, groups, and the refresh rule. Per-file required content stays in INIT.md to avoid drift.

# Project Markdown Files

Seven flowdown groups plus a companion tier:
- **Foundational files** anchor the human side of the project. Read by AI on context refresh because they establish what the project is and why it is worth doing. VISION.md is AI-optimized and compressed; MOTIVATION.md is prose for the human reader and not AI-optimized. Rare — most projects need at most one or two.
- **Sequential files** follow the flowdown, general to specific. Drafted in order during project setup. AI-optimized.
- **Cross-cutting files** are consulted and updated throughout the project lifecycle. Not part of the linear flowdown. AI-optimized. OPERATIONS.md joins the group once the project has deployed hosts or physical devices.
- **Scaffolding files** capture implementation-detail design work (concepts, open questions, code templates) for a phase or subsystem. Markdown files that grow from concept to code during the planning phase. Moved to `scaffolding/integrated/` once implementation begins, preserved as historical record (as-designed state, not current truth). Not read on context refresh — only when implementing the relevant phase.
- **Reference files** hold externally generated background material in `reference/`: seed documents gathered around project inception (inputs to VISION.md and MOTIVATION.md), and local copies of sources cited by topic reports. Stored as-is. Loaded when a session touches the relevant topic; not read on context refresh.
- **Report files** hold AI-authored write-ups of mini-studies or investigations in `reports/`: topic reports from mini-investigations during project execution. Self-updating, status-tracked, cited from the flowdown file where load-bearing. Loaded when a session touches the relevant topic; not read on context refresh.
- **Continuity files** hold per-work-area session-continuity records in `handover/`: the state a new session needs to resume a work area that spans many context windows. Current state, roadmap with per-job status, dated session log, traps. Self-updating; drained to the governed files as work lands; retired to `handover/closed/`. Loaded when the user pulls the file for the area being resumed; not read on context refresh.
- **Companion files** sit outside the flowdown. Schema-level artifacts that govern or accompany the flowdown rather than participate in it: INIT.md (this spec), USE_CASE_INIT.md (universal use-case formulation protocol; governs USE_CASES.md content inline and in any extracted daughter file), HUMAN.md (optional sustainability companion; lives in `ancillary/` when present, not a required part of the flowdown), CODING_PRACTICES.md (downstream coding-behavior template), CLAUDE.md (auto-load bootstrap stub). Not subject to the flowdown's loading patterns; loaded on demand or per the auto-load convention of the host AI tool.

Additional project files may be defined and classified into one of the seven flowdown groups. The companion tier is reserved for schema-level companions, not for per-project content.

**Directory layout.** Classification determines a file's flowdown group and therefore its loading and context-refresh behavior; it is independent of physical path. Flowdown and companion files live at the project root by default. Classified files that would clutter the root may instead live in an `ancillary/` subdirectory — they keep their flowdown group and all its rules (a cross-cutting file in `ancillary/` is still re-read on context refresh). Every classified `ancillary/` file is registered in the CLAUDE.md markdown-hierarchy stub with its group and path; cross-doc references are path-qualified so they resolve. `ancillary/` may also hold unclassified files that are no part of the flowdown; these carry no group, are not registered in the stub, and are governed by per-project direction rather than this spec. INIT.md governs only flowdown and companion files, plus classified files placed in `ancillary/`.

Each entry below: one-line purpose, then required content.

## Foundational Files

### VISION.md

Highest-level document. Expresses the grand ideas behind the project in simple language.

- Authors line at the top: `**Authors:** [human operator], [AI model(s)]`. Append each AI model that substantively edits the file.
- North-star statement (one paragraph).
- Guideposts (essential list of principles or aspirational targets; no fixed cap).
- Some aspects will be unrealizable. Retained as guideposts regardless. This license is guidepost-only.
- Objectives: measurable project-level targets, time-bound where meaningful. Derived from the guideposts and MOTIVATION.md. Expected to be met — the unrealizable license does not extend to objectives.
- Pointer to MOTIVATION.md for the developed argument behind the entries.

### MOTIVATION.md

Developed argument behind the guideposts in VISION.md. Carries the underlying reasoning at the length the arguments deserve, freeing VISION.md to remain compressed and to-the-point.

Authors line at the top: `**Authors:** [human operator], [AI model(s)]`. Append each AI model that substantively edits the file.

Per strand of motivation:
- Statement of the problem or opportunity addressed.
- Why the project's chosen approach is positioned to address it.
- Honest acknowledgment of limits — what the project cannot do, even in principle.
- Connection to the corresponding guidepost(s) in VISION.md.

Optional supporting material: relevant quotes, concrete instances, counter-arguments engaged honestly. Prose form is preserved deliberately; do not compress to bullet points.

## Sequential Files

### INSPIRATIONS.md

Similar projects in development or active use. Supports ideation ("everything is a remix").

Sources: user-provided, training data, internet searches.

Per entry:
- Name and link.
- Borrow: features worth taking forward.
- Avoid: pitfalls observed.
- Relevance: connection to the current project.

**Live search before first draft.** Training data misses recent entrants. Search the web for same-domain, adjacent, and institutional/educational work. Record the search date. Flag reference documents the search shows to be stale.

### ARCHITECTURE.md

Logical breakdown of project elements and their interdependencies. Author with that weight in mind.

- **Element inventory.** Each element with its interdependencies and any element-specific risks.

**Not in ARCHITECTURE.md:**
- Strategic decomposition rationale (why these elements, why this granularity, alternatives considered) → DECISIONS.md.
- Development sequence → IMPLEMENTATION.md.
- Per-phase effort/resource estimates → IMPLEMENTATION.md.
- Project-wide resources (budget, compute), regulatory boundaries, cybersecurity strategy → CONSTRAINTS.md.
- Decision supersession tracking → DECISIONS.md.

### USE_CASES.md

End-user applications of the project, backcast into requirements, design decisions, and feature lists.

Home for all use case specifications, formulated inline.

- Each use case is formulated per USE_CASE_INIT.md (universal formulation protocol: staged construction, quality gates, universal foundational elements, category selection, maturity level). Stage/gate machinery scales down — trivial use cases skip stages with noted rationale per USE_CASE_INIT.md §"Flexibility and Exceptions."
- Per use case, primary category (optional secondary) and current maturity level are load-bearing, set via the protocol; these are the portfolio-rollup dimensions.
- When an individual use case grows unwieldy, extract it to its own `USE_CASE_<identifier>.md` and replace the inline text with a pointer (see §"Stopping Criteria"). Extraction is length-triggered only; the protocol is identical inline or extracted.
- Knowledge-deliverable projects (research, authorship): formulate use cases at the first identifiable consumer (modeler, domain expert, referee, reader); ultimate-impact chains belong in MOTIVATION.md.

### VALIDATION.md

Testing and validation philosophy. Defines what counts as evidence the project works.

Defined upstream of implementation because it shapes what gets built and in what order.

- Unit, integration, and acceptance criteria.
- Domain-specific V&V requirements.
- Per criterion: observable behavior at an element boundary (what, not how), its check, and the pass/fail signal. Mark judgment-only criteria explicitly.
- At least one concrete example per acceptance criterion, in problem-domain language.
- **Human-owned.** AI drafts; the user approves. AI does not weaken, delete, or rewrite a criterion or its check to make work pass. A failing check is surfaced per §"Inconsistency Handling."

### IMPLEMENTATION.md

Detailed sequence of code development sub-projects.

Topic areas covered:
- Data collection and processing.
- Backend infrastructure (server components, code-code coupling).
- Human-machine interface.
- Robust validation and verification (see VALIDATION.md).
- Documentation.

Per-phase entry includes:
- Element identities drawn from ARCHITECTURE.md (do not re-define).
- Deliverables and dependencies.
- Effort/resource estimates (time, tokens, money), where meaningful. Project-wide resource ceilings remain in CONSTRAINTS.md.
- Verification criteria (per VALIDATION.md).

Explicit phases, resolved in sequence, typical of Claude Code plan mode.

**Self-updating:** as each phase is worked on, write state-of-progress to IMPLEMENTATION.md automatically. Do not wait to be asked.

## Cross-Cutting Files

### GLOSSARY.md

Domain-specific terms and their project-scoped definitions.

Per entry:
- Term.
- Definition.
- Example or pointer to the file where the term is load-bearing.

### CONSTRAINTS.md

Cross-cutting constraints and project-wide risks that do not belong to any single sequential file.

- Project-wide budget.
- Project-wide compute envelope.
- Licensing.
- Team skills.
- Hard deadlines.
- Regulatory boundaries that apply project-wide.
- Cybersecurity strategy.
- Project-wide risks: vendor dependencies, supply chain, technology obsolescence, funding/staffing cliffs.

### OPERATIONS.md

Deployed topology and the rules for reaching it. The standing facts a session needs before it touches anything real: what exists, where it runs, how it is reached, how a change gets there.

Created when the project acquires its first deployed host, device, or account — not at Entry Protocol. Projects with nothing deployed have no OPERATIONS.md.

- **Resource inventory.** Per host, device, or account: name, address, role, and what runs on it.
- **Access.** How a session reaches each resource: alias, user, auth mode. Divergences from the obvious (a login name that differs from the operator's, a host reachable only from one machine) are load-bearing — state them.
- **Runtime environments.** Interpreter, environment, and service-manager units per resource, where they differ across resources.
- **Change path.** The write point, how a change propagates to each resource, what restarts it, how it is rolled back.
- **Physical facts that bind a session.** Exclusive devices, power and thermal limits, throttling, storage that cannot be relied on.
- **Credential locations.** Paths and key names only. Never values.
- **Prohibitions.** Actions a session must not take against a resource, and why.

Rules:
- Cross-cutting: re-read on context refresh alongside GLOSSARY/CONSTRAINTS/INTERFACES/DECISIONS.
- **Self-updating.** When a session changes topology, access, environment, or change path, update the entry in the same edit batch. Do not wait to be asked. Mirrors the self-updating rule in §"IMPLEMENTATION.md."
- **Boundary.** CONSTRAINTS.md holds project-wide limits and risks; INTERFACES.md holds contracts between elements; a skill holds an executable procedure; OPERATIONS.md holds the standing facts those three refer to. A fact recorded here is not restated in a skill — the skill cites it.
- **Divergence is an inconsistency.** If a resource behaves differently from what is recorded, surface it per §"Inconsistency Handling." Do not silently rewrite the entry to match.

### INTERFACES.md

Interface inventory across the project. Captures contracts at element boundaries — the artifact most likely to break under independent edits to either side. Project-type-agnostic: applies to software APIs, hardware electrical/mechanical mating, and social handoffs alike.

Seeded once ARCHITECTURE.md elements exist; consulted and updated thereafter throughout the lifecycle.

Per entry:
- Interface ID.
- Connected elements (identities drawn from ARCHITECTURE.md; do not re-define).
- Direction. Uni- or bi-directional; producer → consumer where applicable.
- Contract. Data format, protocol, signature, cadence, units, tolerances — whichever apply for the project type.
- Owner of each side.
- Change procedure. How a proposed change to either side is reviewed and propagated.
- Verification. How the contract is checked. Cross-references VALIDATION.md when present.
- Status: proposed / active / deprecated / superseded.
- Interface-specific risks.

Flat by default. Subdivide hierarchically (system → subsystem → component) only if the flat list grows unwieldy; record the subdivision decision in DECISIONS.md.

A change to an interface entry triggers one-hop propagation to both connected ARCHITECTURE.md elements and any IMPLEMENTATION.md phase that touches them, per §"File Updates."

Active management:
- **Pre-flight.** Before editing any element, consult INTERFACES.md for entries touching that element. Treat listed contracts as constraints on the edit.
- **Self-updating.** When an element edit affects a contract, update the INTERFACES.md entry in the same edit batch. Do not wait to be asked. Mirrors the self-updating rule in §"IMPLEMENTATION.md."
- **Contract divergence is an inconsistency.** If observed or intended behavior diverges from a stated contract, surface as a contradiction per §"Inconsistency Handling." Do not silently rewrite the entry to match.

### DECISIONS.md

Lightweight architecture decision log. Captures *why* choices were made, not just what they are.

Per entry:
- Date.
- Decision.
- Alternatives considered.
- Rationale.
- Status (active / superseded / revisited / open / resolved). `open` for questions logged but not yet decided; `resolved` for previously-open entries that have been settled.

## Scaffolding Files

Files in `scaffolding/` directory that capture implementation-detail design and code templates during the planning phase. Not part of the official documentation hierarchy. Design work on a phase accumulates gradually across sessions: concept → open questions → design decisions → code templates. Once implementation begins, the scaffolding file moves to `scaffolding/integrated/` as a historical record of the as-designed state.

### Lifecycle

1. **Pending**: Phase is planned in IMPLEMENTATION.md. A scaffolding file is created with concept, open questions, and structure. No code blocks yet (or placeholders only).
2. **Active**: Design solidifies during planning. Code blocks are added. Scaffolding file grows as the concept evolves.
3. **Integrated**: Phase implementation begins. Code blocks are extracted and placed in source files (`src/`, `server/`, etc.). Before moving, promote durable rationale to DECISIONS.md (the archive supplements DECISIONS.md, does not replace it). Then move the file to `scaffolding/integrated/` and prepend a header line: `→ historical: as-designed state at integration; current truth is the code and DECISIONS.md.`
4. **Superseded**: Design changes before implementation. Move the old file to `scaffolding/integrated/` marked `status: superseded` with a pointer to the replacement; write a new active file reflecting the updated design.

### Naming and Organization

Located in `scaffolding/` directory. Named by concept or phase, not by target file:

```
scaffolding/
  phase3_geospatial_pipeline.md    ← covers preprocess.py + terrain_ops.py concepts
  phase3_delta_system.md           ← covers delta_manager.py + geospatialDelta.js
  phase4_climate_layer.md
  phase7_policy_system.md
  integrated/
    phase1_data_ingest.md          ← integrated; historical reference only
    phase2_auth_layer.md           ← superseded; pointer to phase2_auth_layer_v2.md
```

When a concept spans multiple target files, group by concept. When a phase is large, separate concepts into distinct files (e.g., `phase3_geospatial_pipeline.md` and `phase3_delta_system.md`).

### File Structure

Each scaffolding file is markdown with this structure:

```markdown
# <Phase> — <Concept Name>

## Concept
Prose explanation of the design. What problem does this solve? What's the key insight?
Grows across sessions as understanding deepens.

## Open Questions
- [ ] Question 1
- [ ] Question 2

Resolves as design clarifies. Checked off when decision is made.

## Design Decisions
Key choices made during planning. Why were alternatives rejected?

### Decision 1: ...
Rationale and implications.

### Decision 2: ...
Rationale and implications.

## Code: <target-file-path>

→ target: `server/geospatial/preprocess.py`
→ status: pending | active | integrated | superseded

```python
...code template...
```

## Code: <target-file-path>

→ target: `src/simulation/geospatialDelta.js`
→ status: pending | active | integrated | superseded

```js
...code template...
```
```

### Integration with IMPLEMENTATION.md

IMPLEMENTATION.md describes **what** each phase delivers, **why**, and **verification**. It does NOT contain code or detailed technical concepts.

When a scaffolding file exists for a phase:

```markdown
### Phase 3 — Geospatial Data Pipeline

...entry conditions, deliverables, verification...

**Technical design and code templates**: See `scaffolding/phase3_geospatial_pipeline.md` and `scaffolding/phase3_delta_system.md`.
```

This keeps IMPLEMENTATION.md readable as a project management document while moving implementation detail to the scaffolding files.

### What does NOT go in scaffolding files

- Design rationale that belongs in DECISIONS.md (decisions made, alternatives considered, project-wide implications) — scaffolding files contain working rationale; decisions that should be preserved go to DECISIONS.md
- Architectural patterns or high-level choices (→ ARCHITECTURE.md)
- Testing strategy (→ VALIDATION.md)

### Context Refresh

Per §"Context Refresh"; load only when implementing the relevant phase. Integrated files are supplementary, not authoritative — current truth is the code and DECISIONS.md.

## Reference Files

Files in `reference/` holding externally generated background material, consulted by topic.

- **Seed documents.** Externally generated material gathered around project inception. Inputs to VISION.md and MOTIVATION.md. Stored as-is; exempt from §"Writing Style for AI-Optimized Files."
- **Report sources.** Local copies of references cited by topic reports (see §"Report Files"). Stored as-is.

Rules:
- Not read on context refresh; load when the session touches the file's topic.
- Reference files persist; they do not move or integrate. Stored as-is, not rewritten into AI-optimized style.
- Do not commit report-source copies to a public repository.

## Report Files

Files in `reports/` holding AI-authored topic reports — write-ups of mini-studies or investigations run during project execution. Frame subsequent sessions on the same topic.

Per topic report:
- Topic and question investigated.
- Findings.
- Implications for the project.
- Date. Findings reflect that date's state; treat as potentially stale.
- Status: current / superseded (with pointer to replacement).
- References, at the end: per source, author or publisher, title, date, URL or path, and whether it was read in full or seen only as a search summary.

Rules:
- Where a reference can be downloaded, save a copy to `reference/` and add its local path to the entry.
- Cite each topic report, path-qualified, from the flowdown file where its findings are load-bearing.
- Not read on context refresh; load when the session touches the file's topic.
- Report files persist; they do not move or integrate. When findings are overturned, mark the report superseded with a pointer — do not delete.
- Durable decisions arising from a report go to DECISIONS.md. The report supplements DECISIONS.md, does not replace it.
- **Self-updating:** when a session completes an investigation worth reusing, write the topic report without being asked. Mirrors the self-updating rule in §"IMPLEMENTATION.md."

## Continuity Files

Files in `handover/` carrying the state a new session needs to resume a work area that outlives a single context window. One file per active work area, named `handover/<area>.md`.

The governed files record what the project decided and what it is. A continuity file records where the work got to — the running state between them.

Per continuity file:
- **Area and scope.** What this file owns, and which sibling areas it does not.
- **Current state.** What is done, what is live, what is deferred. The first thing a resuming session reads.
- **Roadmap.** Remaining jobs in dependency order, each with a status: pending / blocked (on what) / done (with the commit or artifact reference).
- **Session log.** Dated entries: what was attempted, what landed, what was learned.
- **Traps.** Failure modes that cost a session's time and are not visible in the code or the governed files. Stated as the check to run, not the story.
- **Pointers.** The governed files this area's work updates.

Rules:
- Not read on context refresh. The user pulls in the file for the area being resumed. A session that needs one and has not been given it asks by name rather than loading every area.
- Spawn a new file when a work area separates out; cross-reference siblings rather than duplicating their content. Standing operational fact belongs in OPERATIONS.md, cited from here.
- **Drain rule.** As each session closes, promote durable content to the file that owns it: rationale → DECISIONS.md, phase status → IMPLEMENTATION.md, contracts → INTERFACES.md, topology and access → OPERATIONS.md. Compact the drained session-log entry to a one-line pointer. The continuity file supplements the governed files; it does not replace them, and unbounded growth means the drain is not happening.
- **Self-updating.** Write the session entry and advance the roadmap statuses at the end of a working session, unprompted. Mirrors the self-updating rule in §"IMPLEMENTATION.md."
- **Retirement.** When the area closes, drain, then move the file to `handover/closed/` and prepend: `→ historical: continuity record for a closed work area; current truth is the governed files and the code.` Not deleted.
- AI-optimized per §"Writing Style for AI-Optimized Files," with one bounded exception: session-log entries may carry the narrative needed to reconstruct a state — what was tried, what it looked like, why it was wrong. A wrong diagnosis that cost a session is content here, not rationale in the wrong file.

### What does NOT go in continuity files

- Decisions with alternatives worth preserving (→ DECISIONS.md).
- Standing topology, access, and deploy facts (→ OPERATIONS.md).
- Repeatable procedures (→ a skill, per §"Skills").
- Pre-implementation design and code templates (→ `scaffolding/`).
