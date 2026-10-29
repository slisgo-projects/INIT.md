# ARCHITECTURE.md

Logical breakdown of INIT.md-as-a-project. The "elements" are the conceptual building blocks the deliverable files must define and operationalize.

## Element inventory

Each element with its interdependencies (→ depends on) and element-specific risks. Interface contracts at the boundaries between elements live in INTERFACES.md and are not duplicated here.

### 1. File taxonomy (seven-group classification)

Foundational / sequential / cross-cutting / scaffolding / reference / reports / continuity. Each group has a distinct loading pattern: always-on / loaded-in-order during setup / consulted-on-demand throughout / phase-only-during-implementation / topic-triggered / topic-triggered / user-pulled for the work area being resumed.

- **Depends on:** nothing. Top of the architecture.
- **Risk:** if AI context windows become effectively unlimited and lost-in-the-middle degradation disappears, the loading-pattern argument weakens. Taxonomy collapses to "everything always loaded." Partial exception: the continuity group is motivated by sessions ending, not by window size, and survives that collapse.

### 2. Per-file specifications

Required-content templates for each file in the taxonomy (VISION, MOTIVATION, INSPIRATIONS, ARCHITECTURE, USE_CASES, USE_CASE_INIT, VALIDATION, IMPLEMENTATION, GLOSSARY, CONSTRAINTS, OPERATIONS, INTERFACES, DECISIONS, scaffolding, reference, reports, continuity).

- **Depends on:** taxonomy (1).
- **Risk:** if AI improves at inferring required content from minimal seeds, detailed specs become overhead. Currently load-bearing because consistency across projects depends on them.

### 3. Workflow rules

Entry Protocol, File Updates (one-hop propagation), Inconsistency Handling, Findings and Checks, Versioning, Context Refresh, Stopping Criteria, Skills. CLAUDE.md Bootstrap is element (5).

- **Depends on:** taxonomy (1) for which-files-load-when; per-file specifications (2) for what each file contains.
- **Risk:** tightly coupled to current AI's tendencies (single-pass response habits, evaluation fatigue, manual-load friction). May not survive AI architectural shifts toward persistent project-scoped memory.

### 4. Writing style rules

AI-optimization rules (directive voice, bullets, no embedded rationale, no filler) + prose exception for MOTIVATION.md + foundational/AI-optimized split for VISION.md vs. MOTIVATION.md.

- **Depends on:** team-of-one targeting in VISION.md (without single-human assumption, prose for shared human-AI reading would dominate).
- **Risk:** most fragile element. If AI compresses or restructures input on read, directive-voice rules become unnecessary. Style rules age out before structural rules.

### 5. Bootstrap mechanism (CLAUDE.md injection)

Auto-load entry point per project: CODING_PRACTICES contents + taxonomy stub + `@INIT.md` / `@VISION.md` imports in CLAUDE.md so future sessions reload schema with zero per-session friction.

- **Depends on:** taxonomy (1) for stub content; CODING_PRACTICES.md (7) for coding rules.
- **Risk:** tied to Anthropic's CLAUDE.md convention. Vendor-specific. Equivalent slots in other tools (AGENTS.md, `.cursor/rules/`, `.kiro/steering/`) vary in semantics; a portable schema requires per-tool adapters or surrender of auto-load. `@` import syntax is Claude Code-specific; a tool that does not expand it runs sessions without INIT.md's rules. The skills-capture rule (INIT.md §"Skills") shares only the `.claude/skills/` path; `SKILL.md` follows the multi-vendor Agent Skills open standard.

### 6. Human companion (HUMAN.md)

Sustainability framing, human responsibilities list, prose argument for team-of-one solo work over multi-year timeframes. An optional companion in `ancillary/` — not required for downstream projects. Sits outside the flowdown — not referenced from INIT.md.

- **Depends on:** team-of-one targeting in VISION.md.
- **Risk:** obsolete if team-of-one assumption breaks. Otherwise the most enduring element — sustainability concerns persist regardless of AI capability shifts.

### 7. Coding practices template (CODING_PRACTICES.md)

Reusable AI coding behavioral guidelines, copied wholesale into downstream CLAUDE.md per Bootstrap mechanism (5).

- **Depends on:** Bootstrap mechanism (5) for the copy-into-CLAUDE.md instruction.
- **Risk:** conflicts with downstream projects' existing conventions; merge friction. Mitigated by INIT.md instruction to "merge with project-specific guidance."

## Interdependency summary

```
        (1) taxonomy
            ↓
        (2) specs ──→ (3) workflow rules
            ↓
        (5) bootstrap ←── (7) coding practices
            ↑
   (4) style rules   (6) HUMAN.md
            ↑              ↑
         VISION.md guidepost: team-of-one
```

(1), (4), (6) are the deepest dependencies — changes here propagate through the schema. (2), (3), (5), (7) are derived and absorb upstream change without forcing redesign.

Decomposition rationale, alternatives considered, and out-of-scope items live in DECISIONS.md.
