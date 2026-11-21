# Handover — schema redundancy study

## Area and scope

- Owns: the directive-redundancy study — `study/`, `reports/schema_redundancy_ablation.md`, `.claude/skills/redundancy-study/`, DECISIONS.md entry 2026-11-06 (study, `open`).
- Not owned: INIT.md / CODING_PRACTICES.md edits that follow from results (schema edits; land via DECISIONS.md). Open questions in DECISIONS.md 2026-11-16 and 2026-11-17 (model currency, schema value) consume results but are separate.

## Current state (2026-11-21)

- Design, inventory, scope: report §§ "Plan", "Inventory", "Scope". Reduced scope: 16 H directives, arms A0/A1, 5 reps; A2 (leave-one-out) not implemented in `study/run_pilot.py`.
- Ollama configs (GLM-5.3-flash, GLM-5.3): batch 2 complete (INIT.md 2026-11-06); P02 rerun and unclear cells extended and audited (2026-11-15).
- Sonnet 5.5 (Claude Code): batch 1, 130 runs, INIT.md 2026-11-06; kept as second model.
- Opus 5.5 (Claude Code, effort medium):
  - Batch 3 (2026-11-13, INIT.md 2026-11-09, `study/results/runs.csv`): superseded by batch 4 for readings; kept.
  - Batch 4 (2026-11-20, INIT.md 2026-11-18, `study/results/runs_v1118.csv`): 139 valid runs. F04 and every failure audited (`study/results/opus_v1118_audit.csv`); other passes unaudited.
  - Audited readings: does work — E05, F03, I04, T01. Implicit — F01, F05, F06, I01b, I07, K04, O02, P02, X03. Unclear (probe fault) — F04. Not run — I02, T03, F06 A1 rep 4.
- Read results: `python3 study/analyze.py study/results/runs_v1118.csv study/results/opus_v1118_audit.csv --pivot --effort medium`.
- Study status: paused; operator starts batches as tokens allow.

## Roadmap

1. Opus: run I02, T03 (both arms) and F06 A1 rep 4 — 21 runs; F06 resumes as 1. Status: pending.
   - `study/window_batch.sh study/results/runs_v1118.csv I02,T03,F06 5 "now|<STOP>"` — run in background; STOP a few minutes before the next 5-hour or weekly reset.
   - Only valid while INIT.md is still 2026-11-18. If INIT.md changed, use a new out file (`runs_v<MMDD>.csv`) and record the version split.
2. Audit batch-4 additions: every failure, plus spot-check A0 passes on Opus implicit probes (T01 showed scorer false passes). Status: pending (after 1).
3. F04 redesign: probe measures announcement order, not criterion use (report 2026-11-15, batch 4). Status: pending; needs operator agreement on new design before a rerun.
4. P02 probe confound ("run the plan" read as approval). Status: open (DECISIONS.md 2026-11-15).
5. A2 leave-one-out on removal candidates (implicit in model-only layer per DECISIONS.md 2026-11-06 rule). Status: blocked on 2 and on adding an A2 arm to `study/run_pilot.py`.
6. Propose removals to operator; log in DECISIONS.md; edit INIT.md / CODING_PRACTICES.md. Status: blocked on 5.

## Session log

- 2026-11-20/21 — Opus batch 4 run fresh under INIT.md 2026-11-18 (operator chose fresh over mixing versions). First launch: A1 isolation FAIL — workdirs under the Claude Code session scratchpad do not load CLAUDE.md; moved to `/tmp`. Phase 1 used the remaining 64 % of a 5-hour session (~55 runs, 8 min); phase 2 after the 23:29 session reset ran ~84 runs before the next limit, ending 23:44, before the 23:59 weekly reset. Audit: 30 overrides (E05 one-question scorer miss ×3, I01b wording miss ×1, T01 false locator passes ×2 plus label miss). Generalised the window driver to `study/window_batch.sh`. Report and DECISIONS.md updated (commits 547495c, 8749f36).

## Traps

- Workdir root under `/tmp/claude-<uid>/…/scratchpad`: CLAUDE.md not loaded, A1 isolation FAIL. Use `/tmp/<name>_wd` (window_batch.sh does).
- `pkill -f <pattern>` from the Bash tool matches its own shell command and kills it. Kill by process group (`kill -- -<pgid>`) or match `study/run_pilot` only and check with `pgrep -af`.
- Resets are America/Vancouver, which is UTC−7 = this machine's MST clock. Read times from `cd /tmp && claude -p "/usage"`; do not convert.
- Resume key has no INIT.md version: runs under a new INIT.md version need a new out file.
- Editing repo files (outside `study/results`, `study/raw`) during a batch trips CONTAINMENT FAIL and aborts the runner. Commit only after the batch ends.
- A full 5-hour session is ~84 Opus medium runs at 3 workers and is used up in ~15 min; the session limit, not wall time, ends a window.
- The runner does not stop on a usage-limit error; it records ERROR rows for every remaining job. window_batch.sh stops it on the first "hit your".
- Scorer readings are proxies: audit every failure and F04 before reading; do not change scorers after seeing results (INIT.md §"Findings and Checks") — record overrides in an audit CSV.

## Pointers

- `reports/schema_redundancy_ablation.md` — design, results per batch, token budget.
- DECISIONS.md 2026-11-06 (study, open), 2026-11-15 (P02 confound), 2026-11-16 / 2026-11-17 (model currency, schema value).
- `.claude/skills/redundancy-study/SKILL.md` — run, pause, analyse procedure.
