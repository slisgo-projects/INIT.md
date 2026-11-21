#!/bin/bash
# Claude Code on Anthropic (Opus 5.5, effort medium, 3 workers) inside Claude plan usage windows.
#   study/window_batch.sh <out.csv> <probes> <reps> <window> [<window> ...]
#   window = "START|STOP" (GNU date -d strings, local time; START may be "now").
# Each window waits for START, runs until done, the usage limit ("hit your" in the log) or STOP,
# then kills the runner's process group. The next window resumes error and missing runs.
# Set STOP a few minutes before the reset it must not cross. Logs: /tmp/<out-basename>_logs.
# Workdirs go under /tmp: Claude Code does not load CLAUDE.md under its session scratchpad.
set -u
cd "$(dirname "$0")/.." || exit 1
OUT=$1 PROBES=$2 REPS=$3; shift 3
NAME=$(basename "$OUT" .csv)
LOGS=/tmp/${NAME}_logs; mkdir -p "$LOGS"
n=0
for w in "$@"; do
  n=$((n + 1))
  start=$(date -d "${w%%|*}" +%s) stop=$(date -d "${w##*|}" +%s) || exit 2
  log=$LOGS/window$n.log
  while [ "$(date +%s)" -lt "$start" ]; do sleep 30; done
  [ "$(date +%s)" -ge "$stop" ] && { echo "window $n: STOP already passed, skipped" | tee -a "$log"; continue; }
  echo "== $(date) window $n until $(date -d @$stop)" >> "$log"
  setsid python3 study/run_pilot.py --layer harness --model opus --effort medium --probes "$PROBES" --reps "$REPS" \
    --workers 3 --root "/tmp/${NAME}_wd" --out "$OUT" >> "$log" 2>&1 &
  pid=$!
  while kill -0 $pid 2>/dev/null; do
    grep -q "hit your" "$log" && break
    [ "$(date +%s)" -ge "$stop" ] && break
    sleep 5
  done
  if kill -0 $pid 2>/dev/null; then kill -- -$pid; sleep 3; kill -9 -- -$pid 2>/dev/null; fi
  echo "== $(date) window $n ended$(grep -q 'hit your' "$log" && echo ' (usage limit)')" | tee -a "$log"
done
