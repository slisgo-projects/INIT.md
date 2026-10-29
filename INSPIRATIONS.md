# INSPIRATIONS.md

Adjacent projects, conventions, and frameworks that inform INIT.md. Everything is a remix; entries below contributed elements visible in the schema.

Per entry: name + link, borrow, avoid, relevance.

**Search date:** 2026-09-30 (live search per INIT.md §"INSPIRATIONS.md": same-domain, adjacent, institutional/educational). Entries predating this search: date not recorded. §"Executable specification and verification-first": 2026-10-29 (targeted search on sources cited in Farley video).

## AI coding agent context conventions

Files auto-loaded by AI coding tools to instruct behavior in a specific codebase.

### AGENTS.md
- **Link:** [agents.md](https://agents.md/), [github.com/agentsmd/agents.md](https://github.com/agentsmd/agents.md)
- **What:** Multi-vendor open convention. Single markdown file at repo root with build/test commands, conventions, security notes, agent boundaries. Adopted by Codex, Cursor, Windsurf, Kilo, Factory, Builder, Augment, ~2,500+ public repos.
- **Borrow:** Single predictable location; tool-agnostic markdown; simplicity (one file, no schema enforcement).
- **Avoid:** Grows into a junk drawer mixing build commands with code style; lacks subdivision once large.
- **Relevance:** Direct ancestor of CLAUDE.md Bootstrap (§"CLAUDE.md Bootstrap"). INIT.md adds explicit subdivision (foundational / sequential / cross-cutting / scaffolding / reference / reports / continuity) so growth is structured rather than monolithic.

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

### Agent Skills open standard (SKILL.md)
- **Link:** [agentskills.io](https://agentskills.io/)
- **What:** Folder per skill with a `SKILL.md` (name + description frontmatter, instructions) plus optional scripts and references. Progressive disclosure: descriptions load at discovery, full body on activation. Released by Anthropic as an open standard 2025-12-18; supported by 27+ agents.
- **Borrow:** Progressive disclosure — cheap index always loaded, body on demand.
- **Avoid:** Skill sprawl without an index or ownership.
- **Relevance:** Format behind INIT.md §"Skills". Multi-vendor adoption narrows the coupling in §"Skills" to the directory path.

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

### OpenSpec
- **Link:** [github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- **What:** Repo-resident CLI layer: `openspec/specs/` (current requirements), `changes/` (in-flight proposals as delta specs), `archive/` (completed changes). Propose → apply → archive loop; agent-agnostic.
- **Borrow:** Delta specs recording only what a change adds, modifies, or removes; archive-on-completion.
- **Avoid:** Per-change software framing; no foundational or rationale layer.
- **Relevance:** `changes/` → `archive/` lifecycle parallels scaffolding → `scaffolding/integrated/` and continuity → `handover/closed/`.

### GSD (Get Shit Done)
- **Link:** [github.com/open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) (moved from `gsd-build/get-shit-done`), [docs](https://www.mintlify.com/gsd-build/get-shit-done)
- **What:** Context-engineering and spec-driven layer for Claude Code, OpenCode, Gemini CLI, Codex, aimed at solo developers. `.planning/` holds PROJECT.md (vision + requirements), REQUIREMENTS.md, ROADMAP.md (phases), STATE.md (project memory), research/. Targets context rot.
- **Borrow:** Explicit STATE.md separate from the roadmap; phase-mapped requirements.
- **Avoid:** Software-only; slash-command machinery couples the workflow to the tool.
- **Relevance:** Closest same-domain peer for team-of-one. PROJECT/ROADMAP/STATE map onto VISION/IMPLEMENTATION/continuity files.

### Tessl
- **Link:** [tessl.io](https://tessl.io/), [spec-driven-development tile](https://tessl.io/registry/tessl-labs/spec-driven-development)
- **What:** Spec-as-source platform. `.spec.md` files with frontmatter naming target files and linking tests per requirement; registry of versioned library usage specs and methodology tiles (agent interviews one question at a time before specifying).
- **Borrow:** Requirement-to-verification links inside the spec.
- **Avoid:** Commercial registry dependency; code-generation premise.
- **Relevance:** Per-requirement test links echo INTERFACES.md verification field and VALIDATION.md.

## Executable specification and verification-first

Counter-current to markdown-prose specs: intent is only binding when it fails visibly. Verification, not generation, is the bottleneck.

### Dave Farley — ATDD for AI agents
- **Link:** [youtube.com/watch?v=EkH_uoybj8k](https://www.youtube.com/watch?v=EkH_uoybj8k) (Modern Software Engineering, 2026), [xpunconf recap of four-layer model](https://xpunconf-org.pages.dev/pages/insights-2025-part-2)
- **What:** Acceptance-test-driven development as the human's job when agents write code. Executable specifications in problem-domain language, four layers: test cases → domain DSL → protocol drivers → system under test. Three rules: write the spec first, watch it fail; keep the spec out of the agent's reach; one scenario per step (red, green, review, commit). Translation chain: wish → story → example → executable spec → working system; human owns the first three.
- **Borrow:** Red-first as proof the check can catch a wrong answer; human ownership of the check; specs state what, never how; "can't think of an example → don't understand the problem."
- **Avoid:** Software-only mechanism (DSL, protocol drivers); course-coupled skill.
- **Relevance:** Four-layer split ≈ VALIDATION.md (intent) over INTERFACES.md (coupling); translation chain ≈ VISION → USE_CASES → VALIDATION → IMPLEMENTATION. Direct critique of prose-only specs, INIT.md included.

### Understanding Spec-Driven Development (Böckeler)
- **Link:** [martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (2025-10)
- **What:** Field test of Kiro, spec-kit, Tessl. Three levels: spec-first, spec-anchored (kept and evolved), spec-as-source (humans edit only spec). Distinguishes spec (per-feature) from memory bank (always-applicable context). Agents frequently ignored instructions; verbose markdown harder to review than code; tooling mis-sized for small problems. Thoughtworks Radar placed SDD at Assess ([radar](https://www.thoughtworks.com/radar/techniques/spec-driven-development), 2025-11).
- **Borrow:** spec / memory-bank distinction; level taxonomy as self-classification lens; process weight sized to problem.
- **Avoid:** Spec-as-source rigidity (MDD failure mode plus LLM non-determinism).
- **Relevance:** INIT.md is spec-anchored (sequential files) plus memory bank (foundational + cross-cutting). Instruction-skipping finding bears on every prose rule in INIT.md.

### Why AI Coding Agents Still Need Clear Specs (Eisele)
- **Link:** [oreillyradar.substack.com/p/why-ai-coding-agents-still-need-clear](https://oreillyradar.substack.com/p/why-ai-coding-agents-still-need-clear) (2026-07-08)
- **What:** U-shaped cost curve over spec completeness; minimum near acceptance criteria / BDD scenarios. Spec validation as a distinct pre-execution step. Failure modes: inconsistent, incomplete, untestable, misdirected ("precisely what you wrote but not what you meant"). BDD collapses spec writing and validation into one artifact.
- **Borrow:** four spec failure modes as a review checklist; mark mechanically checkable vs. judgment-only criteria; examples plus counterexamples; explicit non-goals.
- **Avoid:** Multi-agent typed-handoff machinery for team-of-one.
- **Relevance:** Checklist maps onto USE_CASE_INIT.md Gate 5 and VALIDATION.md; inconsistent ≈ §"Inconsistency Handling."

### Uncle Bob's agent pipeline (Martin)
- **Link:** [dev.to summary](https://dev.to/adrianbailador/uncle-bobs-agent-pipeline-from-informal-specs-to-mutation-tested-net-code-35d6), [coverage](https://startupfortune.com/uncle-bob-martin-says-he-no-longer-reads-ai-generated-code-and-the-developer-world-is-split/) (2026-07)
- **What:** Does not read agent code. Roles: informal notes (human) → Specifier (structured specs + task list, human-reviewed; Gherkin, human spot-checked) → Coder (sees only Gherkin) → Refactorer → Architect (mutation testing on code and on Gherkin). Gates: fail-then-pass, complexity ceiling, surviving mutants killed.
- **Borrow:** Human review concentrated on the spec, not the output; mutation testing as a check on the checks; implementer isolated from the raw intent.
- **Avoid:** Role-swarm ceremony; total abdication of reading the output.
- **Relevance:** Mutation testing generalizes to a seeded-fault control on any verification (§"Findings and Checks": checks require a control).

### Augmented coding (Beck)
- **Link:** [newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent](https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent) (2025-06)
- **What:** TDD as a "superpower" with agents, which introduce regressions. Agents delete failing tests to get green. "Augmented coding" (care about code, tests, coverage) vs. vibe coding.
- **Borrow:** Treat any edit to a check as suspect.
- **Avoid:** —
- **Relevance:** Agent-weakened checks are the verification analogue of silently resolved inconsistencies.

### Claude Code best practices (Anthropic)
- **Link:** [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) (accessed 2026-10-29)
- **What:** "Give Claude a check to run" — pass/fail signal lets the agent close its own loop. Ask for evidence (command + output), not "tests pass." Non-deterministic (prompt, CLAUDE.md) vs. deterministic (hooks, CI) enforcement; a rule repeatedly missed in CLAUDE.md belongs in a hook. Independent reviewer: fresh session or subagent that did not see the reasoning; review against SPEC.md, skip style.
- **Borrow:** Deterministic enforcement for exceptionless rules; evidence over claims; fresh-context review.
- **Avoid:** Claude Code-specific mechanisms (hooks, `/goal`, `/code-review`).
- **Relevance:** Evidence rule matches §"Inconsistency Handling" status records. Enforcement split names a gap: INIT.md rules are all non-deterministic prose.

### The New Code (Grove, OpenAI)
- **Link:** [ai.engineer/talks/specifications-are-the-new-code](https://ai.engineer/talks/specifications-are-the-new-code) (AI Engineer World's Fair, 2025-06)
- **What:** Specifications, not code, are the durable artifact; code is a lossy translation of intent. Discarding prompts while keeping code ≈ versioning the binary and shredding the source. OpenAI Model Spec as worked example.
- **Borrow:** Intent as version-controlled source.
- **Avoid:** Spec-as-source premise unqualified by executable checks.
- **Relevance:** Supports the flowdown-as-source stance; Farley's rejoinder: the spec must run.

### TDD, Where Did It All Go Wrong (Cooper)
- **Link:** [infoq.com/presentations/tdd-original](https://infoq.com/presentations/tdd-original) (NDC Oslo 2013)
- **What:** Test behaviors at the public boundary, not implementation details; a new behavior, not a new method, triggers a test.
- **Borrow:** Checks anchored at element boundaries survive redesign.
- **Avoid:** —
- **Relevance:** Places VALIDATION.md criteria at ARCHITECTURE.md element boundaries, i.e. INTERFACES.md entries.

Video citations not located by 2026-10-29 search (treat as unverified): Tornhill on end-to-end failing tests; Bache practitioner survey and "all the tests together form the specification"; Adzic on spec-kit detail; Eberhardt on markdown-spec formality; "stochastically degraded" quote; Anthropic "If you can't verify it, don't ship it" (absent from current best-practices page).

## Session continuity and agent memory

Files an agent reads at session start and rewrites as work lands, so work survives context resets.

### Cline Memory Bank
- **Link:** [docs.cline.bot/prompting/cline-memory-bank](https://docs.cline.bot/prompting/cline-memory-bank)
- **What:** `memory-bank/` of six markdown files: projectbrief, productContext, activeContext, systemPatterns, techContext, progress. Agent reads all at task start, updates as it works.
- **Borrow:** Hierarchy rooted in one brief; explicit active-context vs. progress split.
- **Avoid:** Load-everything-every-task; no drain rule, so files grow into a shadow spec.
- **Relevance:** projectbrief ≈ VISION.md, systemPatterns ≈ ARCHITECTURE.md, activeContext/progress ≈ continuity files + IMPLEMENTATION.md status.

### Anthropic long-running agent harness
- **Link:** [anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **What:** Initializer agent writes `claude-progress.txt` (per-session log), `feature_list.json` (requirements with pass flags), `init.sh`, first commit. Each later session reads progress + git log, verifies the app works, implements one feature, commits.
- **Borrow:** Verify current state against the artifact before new work; git history as part of the handoff.
- **Avoid:** Single-app software premise.
- **Relevance:** Independent validation of continuity files and the §"Inconsistency Handling" status-record rule (records are claims; check the artifact).

### planning-with-files (Manus-style)
- **Link:** [mdskills.ai/skills/planning-with-files](https://www.mdskills.ai/skills/planning-with-files)
- **What:** Skill creating task_plan.md, findings.md, progress.md for multi-step tasks and research. Context window = RAM, filesystem = disk.
- **Borrow:** Findings kept separate from plan and log.
- **Avoid:** Task-scoped only; no project-level hierarchy.
- **Relevance:** findings.md ≈ `reports/`; progress.md ≈ continuity session log.

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
- **Relevance:** Inspired INIT.md's group classification (§"Project Markdown Files") — purposes differ but the category-by-role idea is the same.

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

### NASA Systems Engineering Handbook — Interface Management
- **Link:** [NASA SP-2016-6105 Rev2](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf)
- **What:** Interface management as a crosscutting technical-management process; Interface Control Documents under change control — no unilateral changes once agreed.
- **Borrow:** Crosscutting placement; bilateral change control.
- **Avoid:** Multi-center institutional ceremony (boards, signatures).
- **Relevance:** Institutional source of the ICD pattern behind INTERFACES.md fields and its cross-cutting placement.

## Empirical research on context files

### Evaluating AGENTS.md (Gloaguen et al.)
- **Link:** [arxiv.org/abs/2602.11988](https://arxiv.org/abs/2602.11988) (v3 2026-09-29)
- **What:** Four coding agents on SWE-bench and CTXBENCH. Context files do not generally improve task success and raise inference cost by 20%+; repository overviews unhelpful; instructions in context files are followed.
- **Borrow:** Auto-loaded content should carry instructions, not overviews of what the agent can discover.
- **Avoid:** Treating the result as general — measured on single-issue code fixes, not multi-session project work.
- **Relevance:** Supports a lean CLAUDE.md stub and auto-loading INIT.md's behavioral rules; cautions against auto-loading overview files. Bears on the 2026-09-30 import decision and the open INIT.md split row.

### Context Engineering for AI Agents in Open-Source Software
- **Link:** [arxiv.org/abs/2510.21413](https://arxiv.org/abs/2510.21413)
- **What:** Survey of AGENTS.md / CLAUDE.md / Copilot / GEMINI.md files in open-source repos. No established content structure; wide variation in style (descriptive, prescriptive, prohibitive, conditional).
- **Borrow:** Style taxonomy as a lens on directive voice.
- **Avoid:** Descriptive only; no outcome measure.
- **Relevance:** Confirms the gap INIT.md §"CLAUDE.md Bootstrap" fills: no agreed structure for auto-loaded files.

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
- **Session-state files.** Memory Bank (activeContext, progress), Anthropic harness (claude-progress.txt), GSD (STATE.md), planning-with-files (progress.md), INIT.md continuity files — independent convergence on a rewritten state file separate from the spec.
- **Load cost scrutinized.** Auto-loaded context now measured empirically (Gloaguen et al.); lean, instruction-only auto-load favored.
- **Verification over generation.** Farley, Martin, Beck, Anthropic, Eisele — intent binds only through a check that can fail; humans own the check; prose specs drift unnoticed.

INIT.md's distinguishing claims relative to peers:
- **Project-type-agnostic.** Most peers are software-only.
- **Explicit team-of-one targeting.** Most peers assume teams; RFDs explicitly require them.
- **HUMAN.md companion.** No peer addresses individual sustainability over multi-year solo work. (HUMAN.md is an optional companion in `ancillary/`, not required for downstream projects.)
- **Schema-longevity-as-experiment self-awareness.** Most peers assert their structure as final.
