#!/usr/bin/env python3
"""Per-run token usage from pilot results, and projected totals for the full study.

Per run, tokens = input + cache_creation + cache_read (all prompt tokens processed) + output.
Cache reads are billed at a fraction of input on the Claude API and count toward subscription
limits differently; they are reported separately.

  python3 study/token_estimate.py study/results/pilot.csv
  python3 study/token_estimate.py --selftest
"""
import csv
import statistics
import sys
from collections import defaultdict

DIRECTIVES = 37          # tested B rows (scripts/inventory_counts.py test order)
ARMS = 3                 # A0, A1, A2 (A3 optional, excluded)
SCENARIOS = {            # layer -> number of models
    "model": 8,          # Ollama cloud models + Claude API
    "harness": 3,        # Claude Code (1 model) + OpenCode (2 models)
}
REPS = (5, 10)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def per_run(rows):
    g = defaultdict(list)
    for r in rows:
        if r.get("pass") == "" or str(r.get("detail", "")).startswith("ERROR"):
            continue
        prompt = num(r["input_tokens"]) + num(r["cache_creation_tokens"])
        cached = num(r["cache_read_tokens"])
        g[(r["layer"], r["arm"])].append((prompt, cached, num(r["output_tokens"])))
    out = {}
    for k, v in g.items():
        out[k] = {"n": len(v),
                  "prompt": statistics.mean(x[0] for x in v),
                  "cache_read": statistics.mean(x[1] for x in v),
                  "output": statistics.mean(x[2] for x in v)}
        out[k]["total"] = out[k]["prompt"] + out[k]["cache_read"] + out[k]["output"]
    return out


def project(pr):
    res = {}
    for layer, models in SCENARIOS.items():
        arms = [pr[(layer, a)] for a in ("A0", "A1") if (layer, a) in pr]
        if not arms:
            continue
        # A2 ~ A1 in size; A0 measured; average over the 3 arms.
        a0 = pr.get((layer, "A0"), arms[0])["total"]
        a1 = pr.get((layer, "A1"), arms[-1])["total"]
        mean_run = (a0 + 2 * a1) / 3
        for reps in REPS:
            runs = DIRECTIVES * ARMS * models * reps
            res[(layer, reps)] = (runs, runs * mean_run)
    return res


def report(rows):
    pr = per_run(rows)
    lines = ["| Layer | Arm | n | Prompt (uncached) | Cache read | Output | Total/run |",
             "|---|---|---|---|---|---|---|"]
    for (layer, arm), d in sorted(pr.items()):
        lines.append(f"| {layer} | {arm} | {d['n']} | {d['prompt']:,.0f} | {d['cache_read']:,.0f} | "
                     f"{d['output']:,.0f} | {d['total']:,.0f} |")
    lines += ["", "| Layer | Models | Reps | Runs | Tokens |", "|---|---|---|---|---|"]
    for (layer, reps), (runs, tok) in sorted(project(pr).items()):
        lines.append(f"| {layer} | {SCENARIOS[layer]} | {reps} | {runs:,} | {tok/1e6:,.1f} M |")
    return "\n".join(lines)


def selftest():
    rows = [
        {"layer": "model", "arm": "A0", "pass": "True", "detail": "", "input_tokens": "100",
         "cache_creation_tokens": "", "cache_read_tokens": "", "output_tokens": "50"},
        {"layer": "model", "arm": "A1", "pass": "True", "detail": "", "input_tokens": "1000",
         "cache_creation_tokens": "", "cache_read_tokens": "", "output_tokens": "200"},
        {"layer": "model", "arm": "A1", "pass": "", "detail": "ERROR x", "input_tokens": "9e9",
         "cache_creation_tokens": "", "cache_read_tokens": "", "output_tokens": "0"},
    ]
    pr = per_run(rows)
    assert pr[("model", "A0")]["total"] == 150 and pr[("model", "A1")]["total"] == 1200, pr
    # mean_run = (150 + 2*1200)/3 = 850; runs at 5 reps = 37*3*8*5 = 4440
    runs, tok = project(pr)[("model", 5)]
    assert runs == 4440 and abs(tok - 4440 * 850) < 1e-6, (runs, tok)
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        print(report(list(csv.DictReader(open(sys.argv[1])))))
