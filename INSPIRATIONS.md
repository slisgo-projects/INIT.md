# INSPIRATIONS.md

Adjacent projects, conventions, and frameworks that inform INIT.md. Everything is a remix; entries below contributed elements visible in the schema.

Per entry: name + link, borrow, avoid, relevance.

## AI coding agent context conventions

Files auto-loaded by AI coding tools to instruct behavior in a specific codebase.

### AGENTS.md
- **Link:** [agents.md](https://agents.md/), [github.com/agentsmd/agents.md](https://github.com/agentsmd/agents.md)
- **What:** Multi-vendor open convention. Single markdown file at repo root with build/test commands, conventions, security notes, agent boundaries. Adopted by Codex, Cursor, Windsurf, Kilo, Factory, Builder, Augment, ~2,500+ public repos.
- **Borrow:** Single predictable location; tool-agnostic markdown; simplicity (one file, no schema enforcement).
- **Avoid:** Grows into a junk drawer mixing build commands with code style; lacks subdivision once large.
- **Relevance:** Direct ancestor of CLAUDE.md Bootstrap (§"CLAUDE.md Bootstrap"). INIT.md adds explicit subdivision (foundational / sequential / cross-cutting / scaffolding) so growth is structured rather than monolithic.

### CLAUDE.md (Anthropic Claude Code)
- **Link:** [docs.claude.com/en/docs/claude-code/memory](https://docs.claude.com/en/docs/claude-code/memory)
- **What:** Anthropic's convention for Claude Code project memory. Auto-loaded each session. Hierarchical (user-level / project / nested).
- **Borrow:** Auto-load per session removes load-context friction; hierarchical scoping for global vs. per-project rules.
- **Avoid:** Underspecified contents — projects each invent their own structure, which fragments the ecosystem.
- **Relevance:** INIT.md §"CLAUDE.md Bootstrap" specifies what populates CLAUDE.md (CODING_PRACTICES + hierarchy stub), filling the gap Anthropic leaves.

### Cursor Rules (.cursor/rules/*.mdc)
- **Link:** [cursor.com/docs/rules](https://cursor.com/docs/rules)
- **What:** Modular per-rule markdown files with YAML frontmatter controlling activation scope (always / glob-matched / agent-requested / manual).
- **Borrow:** Modular files over a monolith; explicit activation scope prevents over-loading context.
- **Avoid:** Frontmatter complexity; tool-specific format (`.mdc`) couples convention to one IDE.
- **Relevance:** Scaffolding subdirectory pattern (per-phase files) and "not read on context refresh" rule both echo Cursor's scope-controlled activation.

### Aider CONVENTIONS.md
- **Link:** [aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html)
- **What:** Plain markdown specifying coding conventions (library preferences, type annotations, style). Loaded read-only per session; cacheable.
- **Borrow:** Conventions in a separate file from project context, loaded on demand; community-contributed conventions repo.
- **Avoid:** No structure beyond freeform markdown; user invents the format each time.
- **Relevance:** Direct ancestor of CODING_PRACTICES.md. INIT.md's "copy CODING_PRACTICES.md into CLAUDE.md" instruction fuses Aider's pattern with the AGENTS.md/CLAUDE.md auto-load.

### Kiro Steering Files (AWS)
- **Link:** [kiro.dev/docs/steering](https://kiro.dev/docs/steering/)
- **What:** Markdown files in `.kiro/steering/` (workspace) or `~/.kiro/steering/` (global) containing patterns, libraries, standards.
- **Borrow:** Workspace + global scoping; folder convention discoverable by tooling.
- **Avoid:** Tool-specific naming locks projects to Kiro.
- **Relevance:** Reinforces conventions-as-files-on-disk pattern. INIT.md is deliberately tool-agnostic (markdown only, no special directory required).

## Spec-driven development

Specs as durable artifact; code is derived. Phased flowdown of definition → plan → tasks.

### GitHub Spec Kit
- **Link:** [github.com/github/spec-kit](https://github.com/github/spec-kit), [github.blog post (2026)](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- **What:** Three-stage markdown workflow: `spec.md` (what + why) → `plan.md` (technical approach) → `tasks.md` (decomposed work). Scaffolded via `specify` CLI. Works with Copilot, Claude Code, Gemini CLI, Cursor, Windsurf.
- **Borrow:** Three-stage progression mirrors INIT.md's general-to-specific flowdown; AI-tool-agnostic (plain markdown).
- **Avoid:** Software-only assumptions (file paths, dependencies presume code projects); thin support for hardware or social projects.
- **Relevance:** Strongest direct analogue. INIT.md's VISION → ARCHITECTURE → IMPLEMENTATION sequence parallels spec-kit's spec → plan → tasks but generalizes beyond software. spec-kit's existence raises the stakes of VISION.md's schema-longevity guidepost — multiple competing schemas are being authored simultaneously.

### Kiro Specs (requirements / design / tasks)
- **Link:** [kiro.dev](https://kiro.dev/), [aws.amazon.com/documentation-overview/kiro](https://aws.amazon.com/documentation-overview/kiro/)
- **What:** Three structured markdown files per feature: `requirements.md` in EARS notation (Easy Approach to Requirements Syntax), `design.md`, `tasks.md`. Generated from natural-language prompt.
- **Borrow:** Tight phase quality gates (requirements lock before design); EARS notation for unambiguous requirements.
- **Avoid:** Tool-coupled (only works inside Kiro IDE); EARS adds rigor at the cost of human readability.
- **Relevance:** Validates INIT.md's Entry Protocol staging ("Advance one sequential file at a time. Confirm satisfaction before proceeding."). spec-kit and Kiro converge on similar staging from independent designs, suggesting the pattern generalizes.

## Elicitation-driven definition

AI interviews the user to define the project before drafting; content originates in the user's answers. Informs INIT.md §"Entry Protocol" interview variant. See also spec-kit's `/speckit.clarify` (up to 5 targeted questions, answers encoded into the spec) under §"Spec-driven development."

### BMAD-METHOD
- **Link:** [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD), [docs.bmad-method.org](https://docs.bmad-method.org/)
- **What:** Multi-agent agile framework. Analyst persona runs facilitated brainstorming and interactive elicitation to produce a Project Brief (their "single source of truth"); a PM agent then builds a PRD section-by-section with user feedback at each step. Stated stance: AI coaches ideas out of the user, does not generate them.
- **Borrow:** elicitation-not-generation stance; section-by-section interactive drafting with per-section confirmation.
- **Avoid:** 30 agent personas is institutional-team ceremony for a team of one; document chain heavier than the flowdown needs.
- **Relevance:** closest analogue to the Entry Protocol interview variant; independently validates the draft-only-from-answers rule.

### Harper Reed's idea-honing workflow
- **Link:** [harper.blog/2025/02/16/my-llm-codegen-workflow-atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)
- **What:** Pre-spec conversational phase: "Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea." Questions build on prior answers; at natural conclusion the LLM compiles a developer-ready spec.
- **Borrow:** one-question-at-a-time pacing (prevents question-dump and keeps the human the content source); compile-at-end step.
- **Avoid:** single-pass spec output — conflicts with iterative MOTIVATION.md drafting; greenfield-software assumption.
- **Relevance:** minimal form of the interview variant; its pacing rule is adopted in §"Entry Protocol."

## Documentation frameworks (pre-AI lineage)

Older structures that organize project knowledge for human readers. Categorical thinking carries forward.

### Diátaxis
- **Link:** [diataxis.fr](https://diataxis.fr/)
- **What:** Four-quadrant taxonomy of technical documentation: tutorials (learning), how-to guides (problem-solving), reference (information), explanation (understanding). Adopted by Canonical, Django.
- **Borrow:** Categorical sorting by reader need rather than subject matter; explicit acknowledgment that one document cannot serve all purposes.
- **Avoid:** Software-documentation-specific framing; quadrants map onto AI-optimized files imperfectly.
- **Relevance:** Inspired INIT.md's group classification (foundational / sequential / cross-cutting / scaffolding / reference) — purposes differ but the category-by-role idea is the same.

### arc42
- **Link:** [arc42.org](https://arc42.org/)
- **What:** 12-section template for software architecture documentation: introduction/goals, constraints, context, solution strategy, building blocks, runtime, deployment, crosscutting concepts, decisions, quality, risks, glossary. Tool-agnostic.
- **Borrow:** Standardized section names; explicit "everything is optional — fill what serves your project."
- **Avoid:** 12 sections invite empty-section syndrome and check-the-box completion; software-architecture-only.
- **Relevance:** Direct lineage for ARCHITECTURE.md, CONSTRAINTS.md, GLOSSARY.md, and the decisions section (arc42 §9 explicitly references Nygard ADRs).

### README-Driven Development
- **Link:** [tom.preston-werner.com/2010/08/23/readme-driven-development](https://tom.preston-werner.com/2010/08/23/readme-driven-development)
- **What:** Preston-Werner's 2010 manifesto: write the README before any code. Forces clarity of vision before implementation.
- **Borrow:** Documentation-first as forcing function for thinking; "until you've written about your software, you have no idea what you'll be coding."
- **Avoid:** Single-document scope (README only); doesn't address what comes after project start.
- **Relevance:** Direct philosophical ancestor of VISION.md as the entry point. INIT.md generalizes "write the README first" to "write the flowdown first."

## Decision and discussion records

Artifacts for capturing *why* choices were made.

### Architecture Decision Records (ADRs) — Nygard format
- **Link:** [adr.github.io](https://adr.github.io/), [Nygard's original (2011)](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- **What:** Short markdown docs per architectural decision. Fields: title, status (proposed / accepted / superseded), context, decision, consequences. One or two pages each.
- **Borrow:** Lightweight, append-only, status field for supersession, explicit consequences (positive and negative).
- **Avoid:** "One file per decision" grows unwieldy without an index; date-sorting only works if consistently followed.
- **Relevance:** DECISIONS.md is a direct simplification — a single-table index rather than per-decision files, with the same Date / Decision / Alternatives / Rationale / Status fields and the same supersession lifecycle.

### Oxide RFDs (Requests for Discussion)
- **Link:** [rfd.shared.oxide.computer/rfd/0001](https://rfd.shared.oxide.computer/rfd/0001), [oxide.computer/blog/rfd-1](https://oxide.computer/blog/rfd-1-requests-for-discussion)
- **What:** Numbered, branch-and-PR-merged markdown documents covering technical, organizational, and process decisions. Lineage: IETF RFCs → Joyent → Rust RFCs → Kubernetes proposals → Oxide.
- **Borrow:** "Writing things down enables rigorous formulation and candid discussion"; PR-based review; scope extends beyond technical to company process.
- **Avoid:** Heavyweight for team-of-one (no other humans to discuss with); branch/PR workflow assumes a git-native team.
- **Relevance:** Reinforces MOTIVATION.md's prose form — some arguments warrant developed reasoning, not bullets. The team-of-one targeting in VISION.md is partly defined by *not* needing RFD-style discussion infrastructure.

## Pattern observations

Convergent evolution across the field, visible in INIT.md:

- **Markdown as source of truth.** Every entry above uses plain markdown. INIT.md follows the herd deliberately — markdown survives tool churn.
- **Phased flowdown.** spec-kit (spec→plan→tasks), Kiro (requirements→design→tasks), arc42 (12 sections in canonical order), INIT.md (VISION→...→IMPLEMENTATION) — all converge on staged refinement.
- **Decisions captured separately from code.** ADRs, RFDs, arc42 §9, INIT.md DECISIONS.md — the genre is well-established.

INIT.md's distinguishing claims relative to peers:
- **Project-type-agnostic.** Most peers are software-only.
- **Explicit team-of-one targeting.** Most peers assume teams; RFDs explicitly require them.
- **HUMAN.md companion.** No peer addresses individual sustainability over multi-year solo work.
- **Schema-longevity-as-experiment self-awareness.** Most peers assert their structure as final.
