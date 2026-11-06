#!/bin/sh
# Reduced-scope batch (reports/schema_redundancy_ablation.md §"Token budget"): 16 H-impact probes,
# arms A0/A1, 5 reps. A2 runs later, on removal candidates only.
#   study/batch.sh ollama <scratch-root>   Ollama-backed configs (Ollama Cloud usage, no Claude usage)
#   study/batch.sh claude <scratch-root> [probes]   Claude Code on Anthropic (Claude plan usage);
#                                          pass the removal candidates from the Ollama results.
set -e
cd "$(dirname "$0")/.."
ROOT=${2:?scratch root outside the repo}
H=I01b,I02,I07,F05,F06,T01,T03,K04,X03,O02,P02,E05,I04,F01,F03,F04
OUT=study/results/runs.csv
mkdir -p "$ROOT/logs"
case "$1" in
ollama)
  for m in glm-5.3:cloud deepseek-v4-pro:cloud kimi-k3:cloud; do
    python3 study/run_pilot.py --layer model --model $m --probes $H --workers 3 --root "$ROOT/model_$m" \
      --out $OUT > "$ROOT/logs/model_$m.log" 2>&1 &
  done
  python3 study/run_pilot.py --layer harness --provider ollama --model glm-5.3:cloud --probes $H --workers 3 \
    --root "$ROOT/claude-ollama" --out $OUT > "$ROOT/logs/claude-ollama.log" 2>&1 &
  python3 study/run_pilot.py --layer harness --harness opencode --model glm-5.3:cloud --probes $H --workers 3 \
    --root "$ROOT/opencode-ollama" --out $OUT > "$ROOT/logs/opencode-ollama.log" 2>&1 &
  wait ;;
claude)
  python3 study/run_pilot.py --layer harness --model sonnet --probes "${3:-$H}" --workers 3 \
    --root "$ROOT/claude-anthropic" --out $OUT > "$ROOT/logs/claude-anthropic.log" 2>&1 ;;
*) echo "usage: $0 ollama|claude <root> [probes]" >&2; exit 2 ;;
esac
