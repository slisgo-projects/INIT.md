---
name: redundancy-study
description: Run, pause and analyse the INIT.md schema-redundancy study batches (study/). Use when running probes, resuming the reduced-scope batch, or checking plan usage before a batch.
---

# Redundancy study batches

Design and status: `reports/schema_redundancy_ablation.md`.

## Before a batch

- Check Claude usage: `cd /tmp && claude -p "/usage"` (5-hour block and week). Run batches overnight or late in the weekly window (operator, 2026-11-06).
- Ollama usage has no readout; ask the operator.
- Self-tests: `python3 study/score.py --selftest`, `python3 study/analyze.py --selftest`.

## Run

- Ollama-backed configs (no Claude usage): `study/batch.sh ollama <scratch-root>`
- Claude Code on Sonnet, candidates only: `study/batch.sh claude <scratch-root> <probe,probe,...>`
- Single config: `python3 study/run_pilot.py --layer model|harness [--harness claude|opencode] [--provider anthropic|ollama] --model <m> --probes <list> --root <scratch> --out study/results/runs.csv`
- `--root` must be outside the repo. Run long batches in the background.

## Pause

- Stop the background task, then `pkill -f study/run_pilot.py; pkill -f 'opencode run'`. Confirm with `pgrep -af run_pilot`.
- Completed rows stay in `study/results/runs.csv`. The runner does not skip completed runs yet.

## Failure modes

- `CONTAINMENT FAIL` in a log: an agent wrote into the repo. `git status`, revert the agent's files, find the cause before rerunning. Editing repo files yourself during a batch also trips it.
- Isolation `FAIL`: directives leaked or did not load; the arm is skipped. OpenCode needs `OPENCODE_DISABLE_CLAUDE_CODE=1` (set by the runner).
- OpenCode must get `--dir` and `PWD` (set by the runner); it ignores the process cwd.
- `opencode` is at `~/.opencode/bin/opencode`, not on `PATH`.

## Valid output

- One CSV row per run; `pass` True/False, empty for errors and inconclusive runs.
- `python3 study/analyze.py study/results/runs.csv [audit.csv] --pivot` gives A0/A1 per probe and config with the reading.
- Audit every F04 run and every failure before reading results.
