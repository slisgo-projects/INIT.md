#!/usr/bin/env python3
"""Pass rates per layer x probe x arm: pre-registered scorer and after hand audit.

  python3 study/analyze.py study/results/pilot.csv study/results/pilot_audit.csv
  python3 study/analyze.py --selftest
"""
import csv
import sys
from collections import defaultdict


def rates(rows, audit):
    ov = {(a["layer"], a["probe"], a["arm"], a["rep"]): a["audited_pass"] == "True" for a in audit}
    g = defaultdict(lambda: [0, 0, 0])  # n, pre, audited
    for r in rows:
        if r["pass"] not in ("True", "False"):
            continue
        k = (r["layer"], r["model"], r["probe"], r["arm"])
        pre = r["pass"] == "True"
        g[k][0] += 1
        g[k][1] += pre
        g[k][2] += ov.get((r["layer"], r["probe"], r["arm"], r["rep"]), pre)
    return g


def render(g):
    out = ["| Layer | Model | Probe | Arm | n | Pass (pre-registered) | Pass (audited) |",
           "|---|---|---|---|---|---|---|"]
    for (layer, model, probe, arm), (n, pre, aud) in sorted(g.items()):
        out.append(f"| {layer} | {model} | {probe} | {arm} | {n} | {pre}/{n} | {aud}/{n} |")
    return "\n".join(out)


def selftest():
    rows = [dict(layer="m", model="x", probe="P", arm="A0", rep=str(i), pass_=p) for i, p in
            enumerate(["True", "False", "False", ""])]
    for r in rows:
        r["pass"] = r.pop("pass_")
    audit = [dict(layer="m", probe="P", arm="A0", rep="1", audited_pass="True")]
    g = rates(rows, audit)
    assert g[("m", "x", "P", "A0")] == [3, 1, 2], g
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        rows = list(csv.DictReader(open(sys.argv[1])))
        audit = list(csv.DictReader(open(sys.argv[2]))) if len(sys.argv) > 2 else []
        print(render(rates(rows, audit)))
