# Schema Redundancy Ablation

**Date:** 2026-11-06
**Status:** current — plan and inventory only; no probe has been run.
**Baseline:** INIT.md version 2026-11-05; CODING_PRACTICES.md as of commit f709098.
**Provenance:** literature findings come from arXiv abstract pages and search summaries, not full papers (see §"References"). The directive inventory, its classes and its prior predictions are AI judgment. Counts in §"Inventory summary" come from `scripts/inventory_counts.py`.

## Question

- Which INIT.md and CODING_PRACTICES.md directives do models and harnesses already follow without being told? Removing those slims the schema.
- Proposed method: run probe tasks on agents with and without the directives, and compare their behavior.

## Literature

### Context files, measured

- **Gloaguen et al. 2026 (ETH SRI; ICLR 2026).** Context files (AGENTS.md style) did not generally raise task success across several agents and LLMs. They raised inference cost by over 20% (abstract). Agents follow the instructions they contain (abstract). Repository overviews did not help (abstract). Recommendation: keep human-written files to minimal requirements, such as non-standard practices and repository-specific tooling (abstract). Secondary coverage gives about −2–3% for LLM-generated files and about +4% for developer-written ones (search summary only).
- **Khatri 2026 (REALM 2026).** Controlled ablation of how context is injected, on Claude Code and Codex; 17 tasks, 288 runs, gold-test scoring. No measurable correctness effect. Equivalence testing bounds the effect at about 10–15 pp (abstract). Failures came from implementation skill, not missing repository knowledge. Which tasks are borderline differs by agent (Spearman ρ = 0.75), which may explain conflicting single-agent studies (abstract).
- **Gap.** Both papers measure task correctness on coding benchmarks. Neither tests governance or process directives (flag contradictions, log decisions, checks with controls). INIT.md consists mostly of those, so these results cannot be carried over. The study proposed here fills that gap.

### Instruction load

- **Jaroslawicz et al. 2025 (IFScale).** Instruction-following accuracy falls as the number of instructions rises. The best frontier models reach about 68% at 500 instructions. Models favor instructions that appear earlier (abstract).
- **Harada et al. 2025 (ManyIFEval, StyleMBPP).** Performance falls consistently as instructions are added. A logistic model on instruction count predicts unseen combinations within about 10% (abstract).
- **Implication.** A redundant directive is not free: it dilutes attention on the others. Removing one can improve compliance with the rest. Leave-one-out arms measure this; whole-file arms cannot.

### Measurement hazards

- **Sclar et al. 2024 (FormatSpread; ICLR 2024).** Changing format without changing meaning moved accuracy by up to 76 pp on LLaMA-2-13B. Format effects correlate weakly across models (abstract and summaries). Implication: a removed directive's effect can be smaller than the effect of rewording. Hold the wording of the other directives fixed across arms. Never compare a reworded file against the original.
- **LLM judges.** Judges favor text resembling their own output (Wataoka et al. 2024; low-perplexity preference). Position bias varies by model generation (search summaries). Implication: score mechanically where possible. Otherwise use a judge from a different model family than the agent, give it no arm labels, and swap positions in pairwise comparisons.
- **Practitioner reports.** Line-by-line system-prompt ablation is used informally to find dead weight (Tian Pan blog; DEV Community post). These are anecdotal, not studies.

## Plan

### Arms

| Arm | Directive context | Purpose |
|---|---|---|
| A0 baseline | none | What the model and harness do unprompted. |
| A1 full | INIT.md + CODING_PRACTICES.md | Reference compliance. |
| A2 leave-one-out | A1 minus directive X, wording otherwise identical | Redundancy with model or harness, *or* with other directives. |
| A3 single | directive X alone | Optional; separates X's own effect from interactions. |

### Harness × model matrix

| Layer | Option | Notes |
|---|---|---|
| Model only | Ollama API, cloud models (DeepSeek, GLM, Kimi, MiniMax, Qwen, Gemma, Mistral), plus Claude API | No harness system prompt. Separates model-implicit from harness-implicit. |
| Harness | Claude Code `claude -p --bare` | `--bare` skips CLAUDE.md auto-discovery. Treatment arms add the directives with `--append-system-prompt-file`. Use `--bare` in **both** arms so the arms differ only in the directives. |
| Harness | OpenCode via `ollama launch opencode` / `opencode run` | Load directives through `instructions` in `opencode.json`; `@` imports do not load (DECISIONS.md 2026-11-04). |

- **Decision rule for removal:** behavior matches in A0 and A1 in the model-only layer, across the target models. Matching only inside one harness ties INIT.md to that harness. That conflicts with the portability claims in §"Skills" and §"CLAUDE.md Bootstrap".

### Probes

- One fixture repo and one task per behavioral directive. The task gives the model a chance to show the behavior without naming the rule.
- Pass criteria and scoring are written before any run (§"Findings and Checks": checks fixed before first result).
- Scoring is mechanical where possible (file diffs, file presence, a script in the output). Judgment-only probes use a judge per §"Measurement hazards" and are marked as such.
- Number of runs: 5–10 per arm × probe × model to start. Increase the count where A0 and A1 come out close.
- Pass rates and comparisons are computed by script, kept in `scripts/`.

### Reading results

| A0 vs A1 | Reading | Action |
|---|---|---|
| Both high | Implicit | Candidate for removal; confirm with A2. |
| A1 ≫ A0 | Directive does work | Keep. |
| Both low | Directive ineffective | Rewrite, do not remove. |
| A2 ≈ A1, A0 low | Redundant with another directive | Merge. |

### Controls

- **Isolation control.** Before each batch, ask the session with tools disallowed for INIT.md's version (§"CLAUDE.md Bootstrap" verify step). A0 must fail it; A1 must pass. Global `~/.claude/CLAUDE.md` must be absent in every arm (`--bare`, or `--setting-sources` without `user`).
- **Probe control.** Each probe is first run against a planted response that violates the directive, to confirm the scorer marks it as a failure (§"Findings and Checks": checks seen to fail).
- **Shared inputs.** The fixtures and probes are written by the same AI that wrote the inventory and the priors. Record this in the results as a shared input. Have the operator review the probes before the first run.

### Limits

- **Decay.** Implicit behavior holds only for the model and harness versions tested. Re-run the probe suite on each model or harness release. Log results as schema-longevity entries (VISION.md objectives).
- **Non-model readers.** Some directives document intent for the operator or make audits possible. Matching behavior with and without them does not by itself justify removal.
- **Conventions.** Conventions (class C) are not tested. A model cannot infer a file name or a stamp format.
- **Short probes.** Short probes miss effects that only appear late in long sessions, such as drift after compaction. Probes run as single sessions.
- **Cost.** The full matrix is 58 behavioral directives × 4 arms × ~8 models × 5–10 runs = 9,280–18,560 runs (arithmetic by `python3 -c`, 2026-11-06). Pilot first, then prune.

### Phasing

1. Inventory and classify directives; record priors before any run. **Done (this report).**
2. Operator reviews the inventory and the priors.
3. Pilot with three probes (I01 inconsistency, F06 calculations, I02 status claims). Arms A0/A1 only; Claude Code `--bare` plus one Ollama model. Goal: check that isolation, scoring and planted-failure controls work.
4. Scale to all class-B directives in the model-only layer; then harnesses.
5. Run A2 on candidates; propose removals to the operator; log them in DECISIONS.md.

## Inventory

Classes:
- **C** — convention. Schema-specific names, formats, locations and lifecycles. A model cannot infer these. Not tested.
- **B** — behavioral. A general working practice that a capable model or harness might follow unprompted. Probe candidate. "(target C)" means the behavior is general but its destination is a schema file; the probe tests the behavior only.

Prior: AI prediction that A0 already shows the behavior: **likely / unsure / unlikely**. Recorded before any run; the predictions are hypotheses, not findings.

Overlap:
- **CC** — this session's Claude Code system prompt carries related guidance (observed 2026-11-06; one harness, one session).
- **int:X** — overlaps directive X inside INIT.md (A2 target).

| ID | Source | Directive | Class | Prior | Overlap |
|---|---|---|---|---|---|
| D01 | Preamble | Favor structured, explicit content written for re-ingestion | B | unsure | int:W01–W06 |
| D02 | Preamble | MOTIVATION.md is prose, not AI-optimized | C | — | — |
| E01 | Entry Protocol | User supplies VISION.md, suggestions and optional seed documents | C | — | — |
| E02 | Entry Protocol | Without VISION.md, read `reference/` and then interview before drafting | C | — | — |
| E03 | Entry Protocol | Interview: open questions, one at a time, each building on prior answers | B | unsure | — |
| E04 | Entry Protocol | Draft only from the user's answers; do not propose answers | B | unlikely | int:E05 |
| E05 | Entry Protocol | Elicit before drafting judgment-heavy content; do not ghost-write | B | unlikely | int:E04 |
| E06 | Entry Protocol | First move: CLAUDE.md, placeholder files, then an INSPIRATIONS.md draft | C | — | — |
| E07 | Entry Protocol | Capture motivation material whenever surfaced (target C) | B | unlikely | — |
| E08 | Entry Protocol | Advance one sequential file at a time; confirm before proceeding | B | unsure | int:E09 |
| E09 | Entry Protocol | Do not generate all sequential files at once | B | unsure | int:E08 |
| I01 | Inconsistency Handling | Flag inconsistencies between files; do not silently resolve them | B | unsure | int:O04, N04 |
| I02 | Inconsistency Handling | Status records are claims; check the artifact before asserting | B | unsure | CC |
| I03 | Inconsistency Handling | On divergence, correct the record and log it (target C) | B | unlikely | — |
| I04 | Inconsistency Handling | Checkpoint reviews run in a context that did not author the changes | B | unlikely | — |
| I05 | Inconsistency Handling | Checkpoint reviews ask what can be removed | B | unlikely | — |
| I06 | Inconsistency Handling | Removed items follow the owning file's archive rule | C | — | — |
| F01 | Findings and Checks | Negative findings require a control | B | unlikely | — |
| F02 | Findings and Checks | Unconfirmed negatives are logged as open questions | C | — | — |
| F03 | Findings and Checks | A check counts as evidence only after it has been seen to fail | B | unlikely | — |
| F04 | Findings and Checks | Checks independent; criteria fixed before first result; shared inputs recorded | B | unlikely | — |
| F05 | Findings and Checks | Claims closed only when every criterion has passed; open claims list what remains | B | unsure | CC |
| F06 | Findings and Checks | Calculations run in code, not by the AI | B | unsure | — |
| F07 | Findings and Checks | Keep the script; record the script and inputs behind each number | B | unlikely | — |
| F08 | Findings and Checks | Check the script on a known-answer case | B | unlikely | — |
| F09 | Findings and Checks | Re-check AI-computed numbers already in files when touched | B | unlikely | — |
| U01 | File Updates | Propagate related updates; report what was propagated | B | unsure | — |
| U02 | File Updates | Cap propagation at one hop | B | unsure | — |
| U03 | File Updates | Propagation checklist of target files | C | — | — |
| U04 | File Updates | Skip unchanged candidates silently; surface uncertain cases | B | unsure | int:I01 |
| V01 | Versioning | Date-based version stamp; bump on substantive change | C | — | — |
| V02 | Versioning | No bump for typos, MOTIVATION.md touch-ups or log-only entries | C | — | — |
| V03 | Versioning | Downstream records its initialization version | C | — | — |
| R01 | Context Refresh | Default re-read set: foundational + cross-cutting | C | — | — |
| R02 | Context Refresh | Load IMPLEMENTATION.md when work touches a phase | C | — | — |
| R03 | Context Refresh | Do not load scaffolding, reference, reports or continuity on refresh | C | — | — |
| S01 | Stopping Criteria | No length criterion per file | C | — | — |
| S02 | Stopping Criteria | Mention unwieldy growth and ask; do not subdivide unilaterally | B | unsure | — |
| S03 | Stopping Criteria | Subdivided file naming pattern | C | — | — |
| K01 | Skills | Capture a worked-out procedure as a skill in the same session, unasked | B | unlikely | — |
| K02 | Skills | Skill location `.claude/skills/<name>/SKILL.md` | C | — | — |
| K03 | Skills | Skill content: imperative, failure modes, valid output | C | — | — |
| K04 | Skills | No secrets in skills; point to credential locations | B | likely | int:O02 |
| K05 | Skills | Boundary between skills, reports and OPERATIONS.md | C | — | — |
| K06 | Skills | Enforce exceptionless rules mechanically | B | unlikely | — |
| W01 | Writing Style | Directive, not explanatory; no preambles or recaps | B | unsure | — |
| W02 | Writing Style | Bullets over prose; one concept per bullet | B | unsure | — |
| W03 | Writing Style | No embedded rationale (target C) | B | unlikely | — |
| W04 | Writing Style | No filler | B | unsure | — |
| W05 | Writing Style | Terse glossary-style definitions | B | unsure | — |
| W06 | Writing Style | Self-check: fewer words without losing meaning | B | unsure | int:W04 |
| B01 | CLAUDE.md Bootstrap | Four-piece CLAUDE.md stub | C | — | — |
| B02 | CLAUDE.md Bootstrap | Stub holds names, groups and refresh rule only | C | — | — |
| G01 | Project Markdown Files | Seven groups plus companion tier; classification rules | C | — | — |
| G02 | Project Markdown Files | `ancillary/` placement and registration | C | — | — |
| X01 | Per-file specs | Required content per file (VISION through DECISIONS) | C | — | — |
| X02 | INSPIRATIONS.md | Live web search before first draft; record date; flag stale references | B | unsure | — |
| X03 | VALIDATION.md | AI does not weaken a criterion or check to make work pass | B | likely | — |
| X04 | IMPLEMENTATION.md | Write state-of-progress unasked (target C) | B | unlikely | int:O03, N03, T02, H02 |
| O01 | OPERATIONS.md | Created at first deployed resource; required sections | C | — | — |
| O02 | OPERATIONS.md | Credential locations only, never values | B | likely | int:K04 |
| O03 | OPERATIONS.md | Update entry in the same batch when topology changes | B | unlikely | int:X04 |
| O04 | OPERATIONS.md | Divergence is an inconsistency; do not rewrite the entry to match | B | unsure | int:I01 |
| N01 | INTERFACES.md | Entry fields; flat by default | C | — | — |
| N02 | INTERFACES.md | Pre-flight: consult contracts before editing an element | B | unlikely | — |
| N03 | INTERFACES.md | Update the contract in the same edit batch | B | unlikely | int:X04 |
| N04 | INTERFACES.md | Contract divergence is an inconsistency | B | unsure | int:I01 |
| L01 | DECISIONS.md | Entry fields and status values | C | — | — |
| Y01 | Scaffolding | Lifecycle, naming, structure, integration | C | — | — |
| T01 | Report Files | Load-bearing claims carry a source locator; label memory and inference | B | unsure | — |
| T02 | Report Files | Write a topic report unasked after a reusable investigation | B | unlikely | int:X04 |
| T03 | Report Files | Do not commit report-source copies to a public repository | B | unsure | — |
| T04 | Report Files | Report fields, `reference/` copies, supersession | C | — | — |
| H01 | Continuity Files | File structure, drain rule, retirement | C | — | — |
| H02 | Continuity Files | Write session entry and advance roadmap unasked | B | unlikely | int:X04 |
| P01 | Plan files | Session start: fetch, list plans, ask run/defer/decline | C | — | — |
| P02 | Plan files | Plans grant no permissions | B | likely | CC |
| C01 | CODING_PRACTICES §1 | State assumptions; ask when uncertain | B | likely | CC |
| C02 | CODING_PRACTICES §1 | Present multiple interpretations; do not pick silently | B | unsure | — |
| C03 | CODING_PRACTICES §1 | Name a simpler approach; push back when warranted | B | likely | — |
| C04 | CODING_PRACTICES §1 | Stop when confused; name it; ask | B | unsure | int:C01 |
| C05 | CODING_PRACTICES §2 | No features, abstractions, configurability or error handling beyond the request | B | likely | CC |
| C06 | CODING_PRACTICES §2 | Rewrite bloated code shorter | B | unsure | — |
| C07 | CODING_PRACTICES §3 | Do not improve adjacent code; match existing style | B | likely | CC |
| C08 | CODING_PRACTICES §3 | Mention unrelated dead code; do not delete it | B | unsure | — |
| C09 | CODING_PRACTICES §3 | Remove orphans your change created | B | likely | — |
| C10 | CODING_PRACTICES §4 | Turn tasks into verifiable goals; reproduce bugs with a test first | B | unsure | — |
| C11 | CODING_PRACTICES §4 | State a brief plan with verify steps for multi-step tasks | B | unsure | — |

### Inventory summary

Computed by `scripts/inventory_counts.py` against this file:

- Directives inventoried: 88 (30 C, 58 B).
- B priors: 9 likely, 28 unsure, 21 unlikely.
- Rows with CC overlap: 6. Rows with internal overlap: 18.
- CODING_PRACTICES.md: 11 directives, 5 likely, 3 with CC overlap.

### Observations

- **Internal overlap is the cheapest win.** Self-updating rules (X04, O03, N03, T02, H02) restate one pattern five times. Divergence rules (I01, O04, N04) restate one rule three times. Consolidating them needs no experiment, only operator approval; A2 confirms that nothing is lost.
- **The highest-value probes are B directives with prior "unsure".** For "likely" and "unlikely" priors the outcome is mostly predictable, so those runs mainly test the priors.
- **CODING_PRACTICES.md is the most likely candidate for removal.** Five of its eleven directives have prior "likely" and three overlap CC guidance. This matches Gloaguen et al.: general advice duplicates what agents already do; non-standard specifics are what helps.
- **The Findings and Checks directives (F01–F09) are the least likely to be implicit.** They are recent (2026-11-05), specific, and against the grain of "declare victory" behavior (`reports/bootloops_verification_protocols.md`).

## Implications

- No change to INIT.md until probes run. This report proposes; DECISIONS.md records an open entry.
- If the pilot works, the probe suite becomes a standing regression suite for schema longevity.
- OpenCode is not on `PATH` on this machine. It is launched through `ollama launch opencode` (`ancillary/AI_install.md` §7).

## References

- Gloaguen, T., Mündler, N., Müller, M., Raychev, V., Vechev, M. "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" arXiv:2602.11988, 2026-02-12; ICLR 2026. https://arxiv.org/abs/2602.11988 — abstract read; numbers beyond the abstract from search summaries only.
- Khatri, P. "Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories." arXiv:2607.27250, 2026-07-28; REALM 2026. https://arxiv.org/abs/2607.27250 — abstract read (via summary).
- Jaroslawicz, D., Whiting, B., Shah, P., Maamari, K. "How Many Instructions Can LLMs Follow at Once?" arXiv:2507.11538, 2025-07-15. https://arxiv.org/abs/2507.11538 — abstract read (via summary).
- Harada, K. et al. "When Instructions Multiply: Measuring and Estimating LLM Capabilities of Multiple Instructions Following." arXiv:2509.21051, 2025-09. https://arxiv.org/abs/2509.21051 — search summary only.
- Sclar, M., Choi, Y., Tsvetkov, Y., Suhr, A. "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design." arXiv:2310.11324, 2023-10 (rev. 2024-07); ICLR 2024. https://arxiv.org/abs/2310.11324 — search summary only.
- Wataoka, K., Takahashi, T., Ri, R. "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819, 2024. https://arxiv.org/abs/2410.21819 — search summary only.
- Tian Pan. "Prompt Credit Assignment: Finding the Dead Weight in Your System Prompt." Blog, 2026-05-05. https://tianpan.co/blog/2026-05-05-prompt-credit-assignment-system-prompt-dead-weight — search summary only; practitioner, anecdotal.
- Pinho, W. "Do your agent system prompts do anything? I measured 19 of mine." DEV Community. https://dev.to/willianpinho/do-your-agent-system-prompts-do-anything-i-measured-19-of-mine-2ek1 — search summary only; practitioner, anecdotal.
- Local copies: none saved. Download PDFs to `reference/` before relying on findings beyond the abstracts.
