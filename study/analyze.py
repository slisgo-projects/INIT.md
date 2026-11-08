#!/usr/bin/env python3
"""Pass rates per configuration x probe x arm: pre-registered scorer and after hand audit.

Configuration: "model" (Ollama API, no tools) or "<harness>-<provider>" (e.g. claude-anthropic,
claude-ollama, opencode-ollama). Pilot rows without harness/provider columns are Claude Code
on Anthropic.

Reading (fixed 2026-11-06, before the reduced-scope batch): "high" = audited pass rate >= 0.8.
  A0 high and A1 high -> implicit (removal candidate; confirm with A2)
  A1 - A0 >= 0.4      -> does work (keep)
  both < 0.5          -> ineffective (rewrite)
  otherwise           -> unclear (more runs)

  python3 study/analyze.py <runs.csv> [<audit.csv>] [--pivot] [--effort high,default]
  python3 study/analyze.py --selftest
"""
import csv
import sys
from collections import defaultdict


def config(r):
    if r["layer"] == "model":
        return "model"
    return f"{r.get('harness') or 'claude'}-{r.get('provider') or 'anthropic'}"


def rates(rows, audit):
    ov = {(config(a), a.get("model", ""), a["probe"], a["arm"], a["rep"]): a["audited_pass"] == "True"
          for a in audit}
    ov_any = {(config(a), a["probe"], a["arm"], a["rep"]): a["audited_pass"] == "True"
              for a in audit if not a.get("model")}
    g = defaultdict(lambda: [0, 0, 0])  # n, pre, audited
    for r in rows:
        if r["pass"] not in ("True", "False"):
            continue
        c = config(r)
        k = (c, r["model"], r["probe"], r["arm"])
        pre = r["pass"] == "True"
        aud = ov.get((c, r["model"], r["probe"], r["arm"], r["rep"]),
                     ov_any.get((c, r["probe"], r["arm"], r["rep"]), pre))
        g[k][0] += 1
        g[k][1] += pre
        g[k][2] += aud
    return g


def by_effort(rows, efforts):
    """Keep rows whose effort is in the comma list; rows without an effort column count as default."""
    keep = set(efforts.split(","))
    return [r for r in rows if (r.get("effort") or "default") in keep]


def reading(a0, a1):
    if a0 >= 0.8 and a1 >= 0.8:
        return "implicit"
    if a1 - a0 >= 0.4:
        return "does work"
    if a0 < 0.5 and a1 < 0.5:
        return "ineffective"
    return "unclear"


def render(g):
    out = ["| Config | Model | Probe | Arm | n | Pass (pre-registered) | Pass (audited) |",
           "|---|---|---|---|---|---|---|"]
    for (c, model, probe, arm), (n, pre, aud) in sorted(g.items()):
        out.append(f"| {c} | {model} | {probe} | {arm} | {n} | {pre}/{n} | {aud}/{n} |")
    return "\n".join(out)


def pivot(g):
    cells = defaultdict(dict)
    for (c, model, probe, arm), (n, _, aud) in g.items():
        cells[(probe, c, model)][arm] = (aud, n)
    out = ["| Probe | Config | Model | A0 | A1 | Reading |", "|---|---|---|---|---|---|"]
    for (probe, c, model), d in sorted(cells.items()):
        if "A0" not in d or "A1" not in d:
            continue
        (p0, n0), (p1, n1) = d["A0"], d["A1"]
        out.append(f"| {probe} | {c} | {model} | {p0}/{n0} | {p1}/{n1} | {reading(p0 / n0, p1 / n1)} |")
    return "\n".join(out)


def selftest():
    rows = [dict(layer="m", model="x", probe="P", arm="A0", rep=str(i), pass_=p) for i, p in
            enumerate(["True", "False", "False", ""])]
    for r in rows:
        r["pass"] = r.pop("pass_")
    audit = [dict(layer="m", probe="P", arm="A0", rep="1", audited_pass="True")]
    g = rates(rows, audit)
    assert g[("claude-anthropic", "x", "P", "A0")] == [3, 1, 2], g
    rows2 = [dict(layer="harness", harness="opencode", provider="ollama", model="y", probe="Q", arm="A1",
                  rep="0", **{"pass": "False"})]
    audit2 = [dict(layer="harness", harness="opencode", provider="ollama", model="y", probe="Q", arm="A1",
                   rep="0", audited_pass="True")]
    assert rates(rows2, audit2)[("opencode-ollama", "y", "Q", "A1")] == [1, 0, 1]
    mixed = [dict(rows2[0], effort="high"), dict(rows2[0], effort="default", rep="1")]
    assert rates(by_effort(mixed, "high"), [])[("opencode-ollama", "y", "Q", "A1")] == [1, 0, 0]
    assert [reading(*x) for x in [(1, .8), (.2, .8), (.2, .4), (.6, .8), (.8, .6)]] == \
        ["implicit", "does work", "ineffective", "unclear", "unclear"]
    print("selftest ok")


if __name__ == "__main__":
    argv = sys.argv[1:]
    effort = None
    if "--effort" in argv:
        i = argv.index("--effort")
        effort = argv[i + 1]
        del argv[i:i + 2]
    args = [a for a in argv if a != "--pivot"]
    if args == ["--selftest"]:
        selftest()
    else:
        rows = list(csv.DictReader(open(args[0])))
        if effort:
            rows = by_effort(rows, effort)
        audit = list(csv.DictReader(open(args[1]))) if len(args) > 1 else []
        g = rates(rows, audit)
        print(pivot(g) if "--pivot" in sys.argv else render(g))
