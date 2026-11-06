#!/usr/bin/env python3
"""Run redundancy-study probes across arms; append one CSV row per run.

Arms: A0 = no directives; A1 = INIT.md + CODING_PRACTICES.md.
Layers:
  model   — Ollama /api/chat, no tools. A1 puts the directives in the system message.
  harness — Claude Code headless (`claude -p --setting-sources project`), in a fixture
            copy outside this repo. A1 adds CLAUDE.md importing both files.

Each layer+arm first runs the isolation check (tools off: state INIT.md's version).
A0 must not state it; A1 must. A failed check aborts that arm.

  python3 study/run_pilot.py --layer model --model glm-5.3:cloud --reps 5 --root <scratch>
  python3 study/run_pilot.py --layer harness --model sonnet --reps 5 --root <scratch>
"""
import argparse
import concurrent.futures as cf
import csv
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import score  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDY = os.path.join(REPO, "study")
RAW = os.path.join(STUDY, "raw")
DIRECTIVE_FILES = ["INIT.md", "CODING_PRACTICES.md"]
VERSION = next(l.split("**Version:**")[1].split()[0]
               for l in open(os.path.join(REPO, "INIT.md")) if l.startswith("**Version:**"))
ISO_Q = ("Do not use any tools. From your instructions alone, what Version date is at the top "
         "of INIT.md? If you cannot see it, reply NOT LOADED.")
MODEL_NOTE = ("You have no tools in this session. Reply as you would to the user; show any file "
              "edits as full new file contents.")
FIELDS = ["ts", "layer", "model", "probe", "arm", "rep", "pass", "detail", "input_tokens",
          "cache_creation_tokens", "cache_read_tokens", "output_tokens", "turns", "duration_s",
          "cost_usd", "raw"]


def directives():
    return "\n\n".join(open(os.path.join(REPO, f)).read() for f in DIRECTIVE_FILES)


def snapshot(fixture):
    parts = []
    for dp, _, fs in sorted(os.walk(fixture)):
        for f in sorted(fs):
            p = os.path.join(dp, f)
            parts.append(f"=== {os.path.relpath(p, fixture)} ===\n{open(p).read()}")
    return "Project repository files:\n\n" + "\n".join(parts)


# ---------- model layer ----------
def ollama(model, system, user):
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = json.dumps({"model": model, "messages": msgs, "stream": False}).encode()
    t = time.time()
    r = json.load(urllib.request.urlopen(
        urllib.request.Request("http://localhost:11434/api/chat", body), timeout=900))
    return r, time.time() - t


def run_model(model, probe, arm, rep, tag):
    pdir = os.path.join(STUDY, "probes", probe)
    user = snapshot(os.path.join(pdir, "fixture")) + "\n\nTask: " + open(os.path.join(pdir, "task.txt")).read() + "\n" + MODEL_NOTE
    r, dur = ollama(model, directives() if arm == "A1" else None, user)
    text = r["message"]["content"]
    raw = os.path.join(RAW, f"{tag}_model_{probe}_{arm}_{rep}.json")
    json.dump(r, open(raw, "w"), indent=1)
    s = score(probe, "model", text)
    return dict(pass_=s["pass_"], detail=s["detail"], input_tokens=r.get("prompt_eval_count"),
                output_tokens=r.get("eval_count"), turns=1, duration_s=round(dur, 1), raw=raw)


# ---------- harness layer ----------
def setup_workdir(root, fixture, arm, name):
    wd = os.path.join(root, name)
    shutil.rmtree(wd, ignore_errors=True)
    if fixture:
        shutil.copytree(fixture, wd)
    else:
        os.makedirs(wd)
    if arm == "A1":
        for f in DIRECTIVE_FILES:
            shutil.copy(os.path.join(REPO, f), wd)
        open(os.path.join(wd, "CLAUDE.md"), "w").write("".join(f"@{f}\n" for f in DIRECTIVE_FILES))
    return wd


def claude(model, wd, prompt, tools_off=False, timeout=900):
    cmd = ["claude", "-p", "--setting-sources", "project", "--model", model,
           "--output-format", "stream-json", "--verbose"]
    cmd += (["--disallowedTools", "Bash,Read,Grep,Glob,Edit,Write,WebFetch,WebSearch,Agent"] if tools_off
            else ["--allowedTools", "Bash,Read,Edit,Write,Glob,Grep"])
    t = time.time()
    p = subprocess.run(cmd, input=prompt, cwd=wd, capture_output=True, text=True, timeout=timeout)
    events = [json.loads(l) for l in p.stdout.splitlines() if l.strip().startswith("{")]
    bash = [c["input"].get("command", "") for e in events if e.get("type") == "assistant"
            for c in e["message"].get("content", []) if c.get("type") == "tool_use" and c.get("name") == "Bash"]
    res = next((e for e in reversed(events) if e.get("type") == "result"), {})
    return events, bash, res, time.time() - t


def run_harness(model, probe, arm, rep, tag, root):
    pdir = os.path.join(STUDY, "probes", probe)
    wd = setup_workdir(root, os.path.join(pdir, "fixture"), arm, f"{tag}_{probe}_{arm}_{rep}")
    events, bash, res, dur = claude(model, wd, open(os.path.join(pdir, "task.txt")).read())
    raw = os.path.join(RAW, f"{tag}_harness_{probe}_{arm}_{rep}.jsonl")
    open(raw, "w").write("\n".join(json.dumps(e) for e in events))
    s = score(probe, "harness", res.get("result", ""), wd, bash)
    u = res.get("usage", {})
    return dict(pass_=s["pass_"], detail=s["detail"], input_tokens=u.get("input_tokens"),
                cache_creation_tokens=u.get("cache_creation_input_tokens"),
                cache_read_tokens=u.get("cache_read_input_tokens"), output_tokens=u.get("output_tokens"),
                turns=res.get("num_turns"), duration_s=round(dur, 1), cost_usd=res.get("total_cost_usd"), raw=raw)


# ---------- isolation check ----------
def isolation(layer, model, arm, root, tag):
    if layer == "model":
        r, _ = ollama(model, directives() if arm == "A1" else None, ISO_Q)
        text = r["message"]["content"]
    else:
        wd = setup_workdir(root, None, arm, f"{tag}_iso_{arm}")
        _, bash, res, _ = claude(model, wd, ISO_Q, tools_off=True)
        text = res.get("result", "")
    seen = VERSION in text
    ok = seen if arm == "A1" else not seen
    print(f"isolation {layer} {arm}: {'ok' if ok else 'FAIL'} ({text.strip()[:80]!r})", flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", choices=["model", "harness"], required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--probes", default="I01,I02,F06")
    ap.add_argument("--arms", default="A0,A1")
    ap.add_argument("--reps", type=int, default=5)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--root", required=True, help="scratch dir outside the repo for harness workdirs")
    ap.add_argument("--out", default=os.path.join(STUDY, "results", "pilot.csv"))
    a = ap.parse_args()
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(a.root, exist_ok=True)
    assert not os.path.abspath(a.root).startswith(REPO), "root must be outside the repo (CLAUDE.md discovery)"
    tag = time.strftime("%Y%m%dT%H%M%S")
    arms = [x for x in a.arms.split(",") if isolation(a.layer, a.model, x, a.root, tag)]
    jobs = [(p, x, r) for p in a.probes.split(",") for x in arms for r in range(a.reps)]
    new = not os.path.exists(a.out)
    with open(a.out, "a", newline="") as fh, cf.ThreadPoolExecutor(a.workers) as ex:
        w = csv.DictWriter(fh, FIELDS)
        if new:
            w.writeheader()
        fn = run_model if a.layer == "model" else run_harness
        extra = () if a.layer == "model" else (a.root,)
        futs = {ex.submit(fn, a.model, p, x, r, tag, *extra): (p, x, r) for p, x, r in jobs}
        for f in cf.as_completed(futs):
            p, x, r = futs[f]
            try:
                d = f.result()
            except Exception as e:  # record failures, do not drop them
                d = dict(pass_="", detail=f"ERROR {type(e).__name__}: {e}"[:200])
            row = {"ts": tag, "layer": a.layer, "model": a.model, "probe": p, "arm": x, "rep": r,
                   "pass": d.pop("pass_"), **d}
            row["raw"] = os.path.relpath(row.get("raw", ""), REPO) if row.get("raw") else ""
            w.writerow(row)
            fh.flush()
            print(p, x, r, row["pass"], row["detail"], flush=True)


if __name__ == "__main__":
    main()
