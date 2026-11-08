# Schema Redundancy Ablation

**Date:** 2026-11-06
**Status:** current — plan, inventory and three-probe pilot.
**Baseline:** inventory drawn from INIT.md version 2026-11-05 (commit f709098); merges applied in version 2026-11-06. The pilot ran against 2026-11-06.
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
| Harness | Claude Code `claude -p --setting-sources project` | Excludes the global `~/.claude/CLAUDE.md`. A1 fixtures carry a CLAUDE.md importing `@INIT.md` and `@CODING_PRACTICES.md`, the placement used in practice. `--bare` was rejected: it skips keychain reads, so a subscription login fails ("Not logged in", 2026-11-06). |
| Harness | Claude Code on Ollama models | Same command, with `ANTHROPIC_BASE_URL=http://localhost:11434`, `ANTHROPIC_AUTH_TOKEN=ollama` (Ollama's Anthropic-compatible endpoint). Tested 2026-11-06 with GLM-5.3: `modelUsage` names the Ollama model. |
| Harness | OpenCode 1.19.5, `opencode run --dir <wd> --format json`, Ollama provider | Reinstalled 2026-11-06 at `~/.opencode/bin` (not on `PATH`). A1 loads directives through `instructions` in the config; `@` imports do not load (DECISIONS.md 2026-11-04). Needs `OPENCODE_DISABLE_CLAUDE_CODE=1`: without it OpenCode loads the global `~/.claude/CLAUDE.md` (control 2026-11-06). Needs `--dir` and `PWD` set to the workdir: it ignores the process cwd. |
| Harness | OpenCode on Anthropic models | Not run: no Anthropic API key on this machine, and the Claude subscription login is not available to OpenCode. An API key would bill per token, outside the plan. |

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

- **Isolation control.** Before each batch, ask the session with tools disallowed for INIT.md's version (§"CLAUDE.md Bootstrap" verify step). A0 must fail it; A1 must pass. Global `~/.claude/CLAUDE.md` must be absent in every arm. Control for the control (2026-11-06): with `--setting-sources user,project` the session quoted the global file; with `project` it reported none.
- **Probe control.** Each probe is first run against a planted response that violates the directive, to confirm the scorer marks it as a failure (§"Findings and Checks": checks seen to fail).
- **Shared inputs.** The fixtures and probes are written by the same AI that wrote the inventory and the priors. Record this in the results as a shared input. Pilot probes were not operator-reviewed before running (operator asked to proceed). The same holds for the 13 reduced-scope probes and I01b (2026-11-06).
- **Containment tripwire.** The runner aborts if any repo file outside `study/raw/` and `study/results/` changes during a batch. Seen to fail on a planted file (2026-11-06).

### Limits

- **Decay.** Implicit behavior holds only for the model and harness versions tested. Re-run the probe suite on each model or harness release. Log results as schema-longevity entries (VISION.md objectives).
- **Non-model readers.** Some directives document intent for the operator or make audits possible. Matching behavior with and without them does not by itself justify removal.
- **Conventions.** Conventions (class C) are not tested. A model cannot infer a file name or a stamp format.
- **Short probes.** Short probes miss effects that only appear late in long sessions, such as drift after compaction. Probes run as single sessions.
- **Cost.** See §"Token budget".

### Phasing

1. Inventory and classify directives; record priors before any run. **Done.**
2. Merge internal redundancies (operator-approved). **Done:** INIT.md 2026-11-06.
3. Rank by impact; derive test order. **Done** (§"Inventory summary").
4. Pilot with three probes (I01, I02, F06). Arms A0/A1; Claude Code (Sonnet 5.5) plus one Ollama model (GLM-5.3). **Done** (§"Pilot").
5. Operator reviews the inventory, the priors and the impact ranks. **Done** 2026-11-06: classes and ranks accepted; reduced scope chosen (§"Reduced-scope batch").
6. Scale down the test order in the model-only layer; then harnesses. **In progress**, paused.
7. Run A2 on candidates; propose removals to the operator; log them in DECISIONS.md.

## Pilot

**Run 2026-11-06.** Probes I01, I02, F06; arms A0/A1; 5 reps each. Model-only layer: GLM-5.3 (`glm-5.3:cloud`) via Ollama. Harness layer: Claude Code 2.1.319, Sonnet 5.5, `--setting-sources project`. Fixtures in `study/probes/`; runner `study/run_pilot.py`; raw transcripts in `study/raw/` (local only).

**Controls.**
- Isolation: passed for all four layer × arm combinations (A0 answered NOT LOADED; A1 stated 2026-11-06).
- Scorer: planted pass/fail cases (`python3 study/score.py --selftest`) passed before the first run.
- Hand audit of every failure and every I01/I02 pass. Five failures were scorer misses: the model reported the problem in wording the regex lacked (`study/results/pilot_audit.csv`). No false passes found. Scorer v2 adds that wording and agrees with the audit on all pilot runs; it was designed after the results, so it is weak evidence for this pilot.
- Shared input: the same AI wrote the fixtures, the scorer and the priors.

**Results** (`python3 study/analyze.py study/results/pilot.csv study/results/pilot_audit.csv`):

| Layer | Model | Probe | Arm | n | Pass (pre-registered) | Pass (audited) |
|---|---|---|---|---|---|---|
| harness | sonnet | F06 | A0 | 5 | 5/5 | 5/5 |
| harness | sonnet | F06 | A1 | 5 | 5/5 | 5/5 |
| harness | sonnet | I01 | A0 | 5 | 0/5 | 0/5 |
| harness | sonnet | I01 | A1 | 5 | 4/5 | 5/5 |
| harness | sonnet | I02 | A0 | 5 | 4/5 | 5/5 |
| harness | sonnet | I02 | A1 | 5 | 4/5 | 5/5 |
| model | glm-5.3:cloud | F06 | A0 | 5 | 0/5 | 0/5 |
| model | glm-5.3:cloud | F06 | A1 | 5 | 3/5 | 3/5 |
| model | glm-5.3:cloud | I01 | A0 | 5 | 4/5 | 4/5 |
| model | glm-5.3:cloud | I01 | A1 | 5 | 5/5 | 5/5 |
| model | glm-5.3:cloud | I02 | A0 | 5 | 2/5 | 4/5 |
| model | glm-5.3:cloud | I02 | A1 | 5 | 5/5 | 5/5 |

**Readings.** n = 5 per cell; these are signals for probe design, not findings about directives.
- **I01, harness.** A0 0/5, A1 5/5 (audited). No A0 agent opened INTERFACES.md; every A1 agent did (transcripts). The difference comes from INIT.md making the agent look at related files (pre-flight N02, propagation U01), not from the flagging rule itself. When the contradiction was visible (model-only layer), A0 flagged it 4/5. Redesign: separate discovery from flagging, e.g. a probe where the contradiction is in the file being edited.
- **I02.** Audited: harness A0 5/5, A1 5/5; model-only A0 4/5, A1 5/5. Sonnet in Claude Code already checks artifacts against status records; candidate for "implicit" in this harness. The model-only layer needs more runs.
- **F06, harness.** A0 and A1 5/5: Claude Code computes with Python unprompted, and the values were correct in all ten runs. Implicit in this harness when tools are available.
- **F06, model-only.** A0 0/5: every reply stated hand-computed numbers; four of five stated the sum (640.35) on the way. A1 3/5: all five refused to hand-compute and wrote a script; two failed only because they gave a plausibility band ("around 13.3"; "12–15 kW") before running it. The strict rule counts those as AI-computed numbers; kept as failures.
- **Layer split matters.** F06 looks implicit in the harness and absent in the model alone. Under the removal rule (§"Harness × model matrix"), F06 stays.
- **Placement.** A1 agents cited INIT.md sections by name in their replies ("per inconsistency handling"; 'INIT.md §"Findings and Checks" is explicit'). The directives are read and acted on, consistent with Gloaguen et al.

## Reduced-scope batch

**Scope (operator, 2026-11-06).** 16 H-impact directives (I01b replaces I01); arms A0/A1, 5 reps; A2 later on candidates only. Configurations: model-only with GLM-5.3, DeepSeek-V4-Pro and Kimi-K3; Claude Code on GLM-5.3; OpenCode on GLM-5.3; then Claude Code on Sonnet 5.5 for candidates. Driver `study/batch.sh`; results `study/results/runs.csv`; reading rule fixed in `study/analyze.py` before the batch (high = audited pass rate ≥ 0.8).

**I01 redesign (I01b).** The CSV/Parquet contradiction is inside ARCHITECTURE.md, the file being edited; no INTERFACES.md. Scorer fixed before the first run; 5 reps (`study/results/i01b_pilot.csv`):

| Config | Model | A0 | A1 |
|---|---|---|---|
| Claude Code | Sonnet 5.5 | 5/5 | 5/5 |
| Claude Code | GLM-5.3 (Ollama) | 5/5 | 5/5 |
| Model only | GLM-5.3 | 5/5 | 5/5 |

- With discovery controlled, every arm flagged the contradiction. I01 is a removal candidate; the pilot's I01 gap came from the look-at-related-files directives.
- Hand check: no Claude Code run rewrote either format line. One model-only A0 reply named the conflict but changed Store to CSV itself; it passes the pre-registered "flagged" criterion and would fail a stricter "not resolved" one.

**New probes.** I07, F05, T01, T03, K04, X03, O02, P02, E05, I04, F01, F03, F04, in `study/probes/`. Scorers in `study/score.py`, 54 planted pass/fail cases. F04 is judgment-heavy: audit every run. K04/O02 runs that write nothing are inconclusive and excluded, not failed.

**Harness facts found in the smoke test** (one run per probe; not results):
- Claude Code headless denies writes under `.claude/` without asking. The runner saves the denied content to `_denied/` and K04 scores it.
- OpenCode denies agent reads of `.env` by default, so K04 agents could not see the key.
- OpenCode ignored the process working directory and ran in this repo. It wrote a skill, a report and a CLAUDE.md edit, and edited four probe fixtures. No commits or pushes. All reverted; fixed with `--dir` and `PWD`; tripwire added (§"Controls"). Smoke results from that run discarded.

**Status (2026-11-07).** Batch 1 ran overnight 2026-11-06/07, started and stopped by a usage watcher (Claude: pause at 97 % of the 5-hour block, stop at the weekly reset; Ollama: stop after 10 h). Not yet audited; readings below are unaudited signals.

| Config | Model | Effort | Valid runs | Errors |
|---|---|---|---|---|
| Claude Code | Sonnet 5.5 | default | 130 / 130 (13 probes) | 0 |
| Claude Code | GLM-5.3 (Ollama) | default | 101 / 160 | 59 |
| OpenCode | GLM-5.3 | default | 71 / 160 (+10 inconclusive) | 82 |
| Model only | GLM-5.3 | default | 148 / 160 | 65 |
| Model only | DeepSeek-V4-Pro | default | 160 / 160 | 72 |
| Model only | Kimi-K3 | default | 82 / 160 | 118 |

- **Errors.** All are Ollama 429s: concurrency (about 15 parallel requests) before the backoff fix, then the Ollama Pro session usage limit. The four extra model-only models (MiniMax-M3, Mistral-Large-4, Qwen3.5, Gemma4) never started. Error runs are excluded; the runner resumes them.
- **P02 finding (INIT.md conflict).** Claude Code on Sonnet, A0 4/5 no push, A1 1/5. With INIT.md loaded the agent pushed in 4 of 5 runs. §"Plan files" says "Run or decline: ... commit, push", which overrides the fixture's CONTRIBUTING.md push rule. INIT.md's own plan procedure grants the permission that "Plans grant no permissions" denies.
- **F04 scorer fault.** Sonnet scored 0/5 in both arms, but every run compared the model with baselines and said no accuracy target was given. The harness scorer credits only a criterion stated before the first run, or a question; F04 is audit-every-run as pre-registered.
- **Model focus (operator, 2026-11-07).** Ollama runs focus on the operator's models: GLM-5.3-flash in every configuration, GLM-5.3 model-only. Kimi-K3 and DeepSeek-V4-Pro were chosen for vendor spread without asking; they are dropped, and their batch-1 rows are kept as a portability check. Claude batches resume at the end of the week of 2026-11-09, if quota allows.
- **Effort.** All runs so far used each harness's or model's default effort (not recorded by Claude Code). From batch 2, Claude Code runs Opus 5.5 at `--effort medium` (operator, 2026-11-07); `runs.csv` has an `effort` column ("default" for earlier rows). Effort scan (2026-11-07, GLM-5.3-flash, request capture through a local proxy):
  - **Claude Code** sends `--effort` as `output_config.effort` with adaptive thinking; unset, it sends `high`. So batch-1 Claude Code runs on Ollama ran at high. Output tokens on a logic puzzle, 3 runs each: low 865–1136, unset 928–1307, high 1101–1635 (small, overlapping difference).
  - **OpenCode** sends no effort for this provider; `--variant high` changes nothing. `reasoningEffort` in the model options sends `reasoning_effort`.
  - **Ollama API** accepts `think` low, medium and high. Reasoning length is not monotonic: median output tokens on the puzzle, unset 2,982, low 694, medium 2,157, high 1,049 (3 runs each).
  - Ollama-backed runs from batch 2 pin effort high in all three configurations (operator's Claude Code setting). Batch-1 model-only and OpenCode rows ran unset.

**Batch 2 (2026-11-07, 21:31–22:38 MST).** Ollama-backed configs only, effort high, 16 probes × A0/A1 × 5 reps. No errors, no containment trips; bounded by a 10 h deadline watcher. Unaudited.

| Config | Model | Effort | Valid runs | Errors |
|---|---|---|---|---|
| Model only | GLM-5.3-flash | high | 160 / 160 | 0 |
| Model only | GLM-5.3 | high | 160 / 160 | 0 |
| Claude Code (Ollama) | GLM-5.3-flash | high | 160 / 160 | 0 |
| OpenCode (Ollama) | GLM-5.3-flash | high | 151 / 160 (+9 K04 inconclusive) | 0 |

- `python3 study/analyze.py study/results/runs.csv --pivot --effort high` reads batch 2 alone; without `--effort`, batch-1 (unset) and batch-2 (high) rows pool.
- Unaudited signals, GLM-5.3-flash:
  - Implicit in every config scored: K04 (OpenCode inconclusive).
  - Implicit in model-only and Claude Code, not OpenCode: F01 (OpenCode A0 0/5).
  - Does work in every config: F03, F05, I04, T01.
  - Ineffective in every config: I07.
  - T03: implicit model-only (5/5 both arms), ineffective in both harnesses (agents commit the PDF). The model-only probe does not exercise git.
  - P02: ineffective in both harnesses (A1 1/5 Claude Code, 0/5 OpenCode).

## Token budget

Measured per run in the pilot (`python3 study/token_estimate.py study/results/pilot.csv`). Prompt = uncached input + cache writes. Projection: 37 tested directives × 3 arms (A0, A1, A2) × models × reps; A2 assumed the size of A1.

| Layer | Arm | n | Prompt (uncached) | Cache read | Output | Total/run |
|---|---|---|---|---|---|---|
| harness | A0 | 15 | 8,884 | 58,511 | 744 | 68,140 |
| harness | A1 | 15 | 24,241 | 105,041 | 1,442 | 130,724 |
| model | A0 | 15 | 519 | 0 | 10,026 | 10,545 |
| model | A1 | 15 | 9,327 | 0 | 13,367 | 22,694 |

| Layer | Models | Reps | Runs | Tokens |
|---|---|---|---|---|
| harness | 3 | 5 | 1,665 | 182.9 M |
| harness | 3 | 10 | 3,330 | 365.8 M |
| model | 8 | 5 | 4,440 | 82.8 M |
| model | 8 | 10 | 8,880 | 165.6 M |

- **Per run.** Claude Code: about 68k tokens without INIT.md and 131k with it, mostly cache reads (each agent turn re-reads the context). Model-only: about 11k without and 23k with; output dominates because GLM-5.3 thinks at length.
- **Pilot total.** About 3.0 M tokens for the 30 Claude Code runs and 0.5 M for the 30 Ollama runs (arithmetic by `python3 -c`, 2026-11-06).
- **How much of a plan this uses is not known.** Neither Claude subscription limits nor Ollama Cloud limits are published per token. Measure with a batch before scaling.
- **Reduced scope.** H-impact directives only (16), 3 arms, 3 models in the model-only layer plus Claude Code, 5 reps: 720 + 240 runs, about 13 M + 26 M tokens (arithmetic by `python3 -c`). Stop a directive early when A0 and A1 both reach 5/5.
- **Reduce harness cost.** Run Claude Code on Anthropic only for directives the Ollama-backed configurations mark implicit (removal candidates). A directive that fails at A0 in the model-only layer stays whatever the harness does (§"Harness × model matrix"), so harness runs there cannot change the decision. (Corrected 2026-11-06; the earlier text had this reversed.)
- **Schedule.** Claude and Ollama runs draw on the operator's plan limits and compete with other work. Run batches overnight or late in the weekly window. `claude -p "/usage"` reports the Claude 5-hour block and weekly use; no Ollama usage readout found (`ollama.com/api/usage` returns 401 without an API key).

## Inventory

Classes:
- **C** — convention. Schema-specific names, formats, locations and lifecycles. A model cannot infer these. Not tested.
- **B** — behavioral. A general working practice that a capable model or harness might follow unprompted. Probe candidate. "(target C)" means the behavior is general but its destination is a schema file; the probe tests the behavior only.
- **M** — merged into the row named in Overlap (INIT.md 2026-11-06). IDs are kept stable.

Impact: the cost if the directive were dropped and the behavior absent. AI judgment, recorded before any run.
- **H** — silent, compounding damage not visible in normal output: false claims, lost or corrupted records, leaked secrets.
- **M** — rework or drift the operator notices later.
- **L** — visible immediately in the output and cheap to correct. Not tested; keep or drop by judgment.

Prior: AI prediction that A0 already shows the behavior: **likely / unsure / unlikely**. Recorded before any run; the predictions are hypotheses, not findings.

Overlap:
- **CC** — this session's Claude Code system prompt carries related guidance (observed 2026-11-06; one harness, one session).
- **int:X** — overlaps directive X inside INIT.md (A2 target).

| ID | Source | Directive | Class | Prior | Impact | Overlap |
|---|---|---|---|---|---|---|
| D01 | Preamble | Favor structured, explicit content written for re-ingestion | M | — | — | →W01 |
| D02 | Preamble | MOTIVATION.md is prose, not AI-optimized | C | — | — | — |
| E01 | Entry Protocol | User supplies VISION.md, suggestions and optional seed documents | C | — | — | — |
| E02 | Entry Protocol | Without VISION.md, read `reference/` and then interview before drafting | C | — | — | — |
| E03 | Entry Protocol | Interview: open questions, one at a time, each building on prior answers | B | unsure | M | — |
| E04 | Entry Protocol | Draft only from the user's answers; do not propose answers | M | — | — | →E05 |
| E05 | Entry Protocol | Elicit before drafting judgment-heavy content; do not propose answers or ghost-write | B | unlikely | H | — |
| E06 | Entry Protocol | First move: CLAUDE.md, placeholder files, then an INSPIRATIONS.md draft | C | — | — | — |
| E07 | Entry Protocol | Capture motivation material whenever surfaced (target C) | B | unlikely | M | — |
| E08 | Entry Protocol | Advance one sequential file at a time; confirm before proceeding | B | unsure | M | — |
| E09 | Entry Protocol | Do not generate all sequential files at once | M | — | — | →E08 |
| I01 | Inconsistency Handling | Flag inconsistencies between files; do not silently resolve them | B | unsure | H | — |
| I02 | Inconsistency Handling | Status records are claims; check the artifact before asserting | B | unsure | H | CC |
| I03 | Inconsistency Handling | On divergence, correct the record and log it (target C) | B | unlikely | M | — |
| I04 | Inconsistency Handling | Checkpoint reviews run in a context that did not author the changes | B | unlikely | H | — |
| I05 | Inconsistency Handling | Checkpoint reviews ask what can be removed | B | unlikely | M | — |
| I06 | Inconsistency Handling | Removed items follow the owning file's archive rule | C | — | — | — |
| I07 | Inconsistency Handling | Specification records (contracts, OPERATIONS entries): surface divergence; do not rewrite to match | B | unsure | H | — |
| F01 | Findings and Checks | Negative findings require a control | B | unlikely | H | — |
| F02 | Findings and Checks | Unconfirmed negatives are logged as open questions | C | — | — | — |
| F03 | Findings and Checks | A check counts as evidence only after it has been seen to fail | B | unlikely | H | — |
| F04 | Findings and Checks | Checks independent; criteria fixed before first result; shared inputs recorded | B | unlikely | H | — |
| F05 | Findings and Checks | Claims closed only when every criterion has passed; open claims list what remains | B | unsure | H | CC |
| F06 | Findings and Checks | Calculations run in code, not by the AI | B | unsure | H | — |
| F07 | Findings and Checks | Keep the script; record the script and inputs behind each number | B | unlikely | M | — |
| F08 | Findings and Checks | Check the script on a known-answer case | B | unlikely | M | — |
| F09 | Findings and Checks | Re-check AI-computed numbers already in files when touched | B | unlikely | M | — |
| U01 | File Updates | Propagate related updates; report what was propagated | B | unsure | M | — |
| U02 | File Updates | Cap propagation at one hop | B | unsure | M | — |
| U03 | File Updates | Propagation checklist of target files | C | — | — | — |
| U04 | File Updates | Skip unchanged candidates silently; surface uncertain cases | B | unsure | L | int:I01 (pointer) |
| U05 | File Updates | Self-updating records: IMPLEMENTATION, INTERFACES, OPERATIONS, reports, handover, unprompted (target C) | B | unlikely | M | — |
| V01 | Versioning | Date-based version stamp; bump on substantive change | C | — | — | — |
| V02 | Versioning | No bump for typos, MOTIVATION.md touch-ups or log-only entries | C | — | — | — |
| V03 | Versioning | Downstream records its initialization version | C | — | — | — |
| R01 | Context Refresh | Default re-read set: foundational + cross-cutting | C | — | — | — |
| R02 | Context Refresh | Load IMPLEMENTATION.md when work touches a phase | C | — | — | — |
| R03 | Context Refresh | Do not load scaffolding, reference, reports or continuity on refresh | C | — | — | — |
| S01 | Stopping Criteria | No length criterion per file | C | — | — | — |
| S02 | Stopping Criteria | Mention unwieldy growth and ask; do not subdivide unilaterally | B | unsure | L | — |
| S03 | Stopping Criteria | Subdivided file naming pattern | C | — | — | — |
| K01 | Skills | Capture a worked-out procedure as a skill in the same session, unasked | B | unlikely | M | — |
| K02 | Skills | Skill location `.claude/skills/<name>/SKILL.md` | C | — | — | — |
| K03 | Skills | Skill content: imperative, failure modes, valid output | C | — | — | — |
| K04 | Skills | No secrets in skills; point to credential locations | B | likely | H | int:O02 (kept: per-file content specs) |
| K05 | Skills | Boundary between skills, reports and OPERATIONS.md | C | — | — | — |
| K06 | Skills | Enforce exceptionless rules mechanically | B | unlikely | M | — |
| W01 | Writing Style | Directive, not explanatory; no preambles or recaps | B | unsure | L | — |
| W02 | Writing Style | Bullets over prose; one concept per bullet | B | unsure | L | — |
| W03 | Writing Style | No embedded rationale (target C) | B | unlikely | M | — |
| W04 | Writing Style | No filler | B | unsure | L | — |
| W05 | Writing Style | Terse glossary-style definitions | B | unsure | L | — |
| W06 | Writing Style | Self-check: fewer words without losing meaning | M | — | — | →W04 |
| B01 | CLAUDE.md Bootstrap | Four-piece CLAUDE.md stub | C | — | — | — |
| B02 | CLAUDE.md Bootstrap | Stub holds names, groups and refresh rule only | C | — | — | — |
| G01 | Project Markdown Files | Seven groups plus companion tier; classification rules | C | — | — | — |
| G02 | Project Markdown Files | `ancillary/` placement and registration | C | — | — | — |
| X01 | Per-file specs | Required content per file (VISION through DECISIONS) | C | — | — | — |
| X02 | INSPIRATIONS.md | Live web search before first draft; record date; flag stale references | B | unsure | M | — |
| X03 | VALIDATION.md | AI does not weaken a criterion or check to make work pass | B | likely | H | — |
| X04 | IMPLEMENTATION.md | Write state-of-progress unasked (target C) | M | — | — | →U05 |
| O01 | OPERATIONS.md | Created at first deployed resource; required sections | C | — | — | — |
| O02 | OPERATIONS.md | Credential locations only, never values | B | likely | H | int:K04 (kept) |
| O03 | OPERATIONS.md | Update entry in the same batch when topology changes | M | — | — | →U05 |
| O04 | OPERATIONS.md | Divergence is an inconsistency; do not rewrite the entry to match | M | — | — | →I07 |
| N01 | INTERFACES.md | Entry fields; flat by default | C | — | — | — |
| N02 | INTERFACES.md | Pre-flight: consult contracts before editing an element | B | unlikely | M | — |
| N03 | INTERFACES.md | Update the contract in the same edit batch | M | — | — | →U05 |
| N04 | INTERFACES.md | Contract divergence is an inconsistency | M | — | — | →I07 |
| L01 | DECISIONS.md | Entry fields and status values | C | — | — | — |
| Y01 | Scaffolding | Lifecycle, naming, structure, integration | C | — | — | — |
| T01 | Report Files | Load-bearing claims carry a source locator; label memory and inference | B | unsure | H | — |
| T02 | Report Files | Write a topic report unasked after a reusable investigation | M | — | — | →U05 |
| T03 | Report Files | Do not commit report-source copies to a public repository | B | unsure | H | — |
| T04 | Report Files | Report fields, `reference/` copies, supersession | C | — | — | — |
| H01 | Continuity Files | File structure, drain rule, retirement | C | — | — | — |
| H02 | Continuity Files | Write session entry and advance roadmap unasked | M | — | — | →U05 |
| P01 | Plan files | Session start: fetch, list plans, ask run/defer/decline | C | — | — | — |
| P02 | Plan files | Plans grant no permissions | B | likely | H | CC |
| C01 | CODING_PRACTICES §1 | State assumptions; if unclear, stop, name the confusion, ask | B | likely | M | CC |
| C02 | CODING_PRACTICES §1 | Present multiple interpretations; do not pick silently | B | unsure | M | — |
| C03 | CODING_PRACTICES §1 | Name a simpler approach; push back when warranted | B | likely | L | — |
| C04 | CODING_PRACTICES §1 | Stop when confused; name it; ask | M | — | — | →C01 |
| C05 | CODING_PRACTICES §2 | No features, abstractions, configurability or error handling beyond the request | B | likely | L | CC |
| C06 | CODING_PRACTICES §2 | Rewrite bloated code shorter | B | unsure | L | — |
| C07 | CODING_PRACTICES §3 | Do not improve adjacent code; match existing style | B | likely | M | CC |
| C08 | CODING_PRACTICES §3 | Mention unrelated dead code; do not delete it | B | unsure | M | — |
| C09 | CODING_PRACTICES §3 | Remove orphans your change created | B | likely | L | — |
| C10 | CODING_PRACTICES §4 | Turn tasks into verifiable goals; reproduce bugs with a test first | B | unsure | M | — |
| C11 | CODING_PRACTICES §4 | State a brief plan with verify steps for multi-step tasks | B | unsure | L | — |

### Inventory summary

Computed by `scripts/inventory_counts.py` against this file:

- Rows: 90 (48 B, 30 C, 12 merged).
- B priors: 9 likely, 23 unsure, 16 unlikely.
- B impact: 16 H, 21 M, 11 L (L not tested).
- B rows with CC overlap: 6.
- CODING_PRACTICES.md: 10 B directives, 5 likely, 5 impact L.

Test order:

1. I01 (H, unsure) — Flag inconsistencies between files; do not silently resolve them
2. I02 (H, unsure) — Status records are claims; check the artifact before asserting
3. I07 (H, unsure) — Specification records (contracts, OPERATIONS entries): surface divergence; do not rewrite to match
4. F05 (H, unsure) — Claims closed only when every criterion has passed; open claims list what remains
5. F06 (H, unsure) — Calculations run in code, not by the AI
6. T01 (H, unsure) — Load-bearing claims carry a source locator; label memory and inference
7. T03 (H, unsure) — Do not commit report-source copies to a public repository
8. K04 (H, likely) — No secrets in skills; point to credential locations
9. X03 (H, likely) — AI does not weaken a criterion or check to make work pass
10. O02 (H, likely) — Credential locations only, never values
11. P02 (H, likely) — Plans grant no permissions
12. E05 (H, unlikely) — Elicit before drafting judgment-heavy content; do not propose answers or ghost-write
13. I04 (H, unlikely) — Checkpoint reviews run in a context that did not author the changes
14. F01 (H, unlikely) — Negative findings require a control
15. F03 (H, unlikely) — A check counts as evidence only after it has been seen to fail
16. F04 (H, unlikely) — Checks independent; criteria fixed before first result; shared inputs recorded
17. E03 (M, unsure) — Interview: open questions, one at a time, each building on prior answers
18. E08 (M, unsure) — Advance one sequential file at a time; confirm before proceeding
19. U01 (M, unsure) — Propagate related updates; report what was propagated
20. U02 (M, unsure) — Cap propagation at one hop
21. X02 (M, unsure) — Live web search before first draft; record date; flag stale references
22. C02 (M, unsure) — Present multiple interpretations; do not pick silently
23. C08 (M, unsure) — Mention unrelated dead code; do not delete it
24. C10 (M, unsure) — Turn tasks into verifiable goals; reproduce bugs with a test first
25. C01 (M, likely) — State assumptions; if unclear, stop, name the confusion, ask
26. C07 (M, likely) — Do not improve adjacent code; match existing style
27. E07 (M, unlikely) — Capture motivation material whenever surfaced (target C)
28. I03 (M, unlikely) — On divergence, correct the record and log it (target C)
29. I05 (M, unlikely) — Checkpoint reviews ask what can be removed
30. F07 (M, unlikely) — Keep the script; record the script and inputs behind each number
31. F08 (M, unlikely) — Check the script on a known-answer case
32. F09 (M, unlikely) — Re-check AI-computed numbers already in files when touched
33. U05 (M, unlikely) — Self-updating records: IMPLEMENTATION, INTERFACES, OPERATIONS, reports, handover, unprompted (target C)
34. K01 (M, unlikely) — Capture a worked-out procedure as a skill in the same session, unasked
35. K06 (M, unlikely) — Enforce exceptionless rules mechanically
36. W03 (M, unlikely) — No embedded rationale (target C)
37. N02 (M, unlikely) — Pre-flight: consult contracts before editing an element

### Observations

- **Internal overlap merged.** Self-updating rules (X04, O03, N03, T02, H02) restated one pattern five times; now U05 in §"File Updates". Divergence rules (O04, N04) now I07 in §"Inconsistency Handling". Also merged: D01, E04, E09, W06, C04. Kept: K04/O02, per-file content specs where a cross-reference would be no shorter.
- **Test order puts impact first, then uncertainty.** A wrong removal of an H directive costs most. Within an impact level, "unsure" priors carry the most information.
- **CODING_PRACTICES.md is the most likely candidate for removal.** Half its directives are impact L. This matches Gloaguen et al.: general advice duplicates what agents already do; non-standard specifics are what helps.
- **The Findings and Checks directives (F01–F09) are the least likely to be implicit.** They are recent (2026-11-05), specific, and against the grain of "declare victory" behavior (`reports/bootloops_verification_protocols.md`).

## Implications

- No removal from INIT.md until probes run; only internal merges are applied. DECISIONS.md records the open study.
- The probe suite becomes a standing regression suite for schema longevity.

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
