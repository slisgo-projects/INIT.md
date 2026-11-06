#!/usr/bin/env python3
"""Run redundancy-study probes across arms; append one CSV row per run.

Arms: A0 = no directives; A1 = INIT.md + CODING_PRACTICES.md.
Layers:
  model   — Ollama /api/chat, no tools. A1 puts the directives in the system message.
  harness — an agent harness in a fixture copy outside this repo:
    claude   — Claude Code headless (`claude -p --setting-sources project`). A1 adds CLAUDE.md
               importing both files. --provider ollama routes it to Ollama's Anthropic-compatible
               endpoint (ANTHROPIC_BASE_URL=http://localhost:11434).
    opencode — OpenCode headless (`opencode run --format json`), Ollama provider only.
               OPENCODE_DISABLE_CLAUDE_CODE=1 keeps ~/.claude/CLAUDE.md out (leak seen without it,
               2026-11-06). A1 lists both files under `instructions` in the config.

Each layer+arm first runs the isolation check (tools off: state INIT.md's version).
A0 must not state it; A1 must. A failed check aborts that arm.

  python3 study/run_pilot.py --layer model --model glm-5.3:cloud --reps 5 --root <scratch>
  python3 study/run_pilot.py --layer harness --model sonnet --reps 5 --root <scratch>
  python3 study/run_pilot.py --layer harness --model glm-5.3:cloud --provider ollama ...
  python3 study/run_pilot.py --layer harness --harness opencode --model glm-5.3:cloud ...
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
FIELDS = ["ts", "layer", "harness", "provider", "model", "probe", "arm", "rep", "pass", "detail", "input_tokens",
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
    ctx = os.path.join(pdir, "model_context.txt")
    user = (snapshot(os.path.join(pdir, "fixture")) + ("\n\n" + open(ctx).read() if os.path.exists(ctx) else "")
            + "\n\nTask: " + open(os.path.join(pdir, "task.txt")).read() + "\n" + MODEL_NOTE)
    r, dur = ollama(model, directives() if arm == "A1" else None, user)
    text = r["message"]["content"]
    raw = os.path.join(RAW, f"{tag}_model_{probe}_{arm}_{rep}.json")
    json.dump(r, open(raw, "w"), indent=1)
    s = score(probe, "model", text)
    return dict(pass_=s["pass_"], detail=s["detail"], input_tokens=r.get("prompt_eval_count"),
                output_tokens=r.get("eval_count"), turns=1, duration_s=round(dur, 1), raw=raw)


# ---------- harness layer ----------
OPENCODE = os.path.expanduser("~/.opencode/bin/opencode")


def setup_workdir(root, fixture, arm, name, harness="claude"):
    wd = os.path.join(root, name)
    shutil.rmtree(wd, ignore_errors=True)
    shutil.rmtree(wd + "_origin.git", ignore_errors=True)
    if fixture:
        shutil.copytree(fixture, wd)
        setup = os.path.join(os.path.dirname(fixture), "setup.sh")
        if os.path.exists(setup):  # runs before directive files are added, so they stay untracked
            subprocess.run(["sh", setup], cwd=wd, check=True, capture_output=True)
    else:
        os.makedirs(wd)
    if arm == "A1":
        for f in DIRECTIVE_FILES:
            shutil.copy(os.path.join(REPO, f), wd)
        if harness == "claude":
            open(os.path.join(wd, "CLAUDE.md"), "w").write("".join(f"@{f}\n" for f in DIRECTIVE_FILES))
    return wd


def claude_env(provider, model):
    env = dict(os.environ)
    if provider == "ollama":
        env.update(ANTHROPIC_BASE_URL="http://localhost:11434", ANTHROPIC_AUTH_TOKEN="ollama",
                   ANTHROPIC_API_KEY="", ANTHROPIC_DEFAULT_OPUS_MODEL=model,
                   ANTHROPIC_DEFAULT_SONNET_MODEL=model, ANTHROPIC_DEFAULT_HAIKU_MODEL=model,
                   CLAUDE_CODE_SUBAGENT_MODEL=model)
    return env


def opencode(model, wd, prompt, arm, tools_off=False, timeout=900):
    cfg = {"$schema": "https://opencode.ai/config.json",
           "provider": {"ollama": {"npm": "@ai-sdk/openai-compatible",
                                   "options": {"baseURL": "http://localhost:11434/v1"},
                                   "models": {model: {}}}},
           "permission": ({k: "deny" for k in ("read", "edit", "bash", "glob", "grep", "list", "task", "webfetch")}
                          if tools_off else {"edit": "allow", "bash": "allow", "webfetch": "deny"})}
    if arm == "A1":
        cfg["instructions"] = DIRECTIVE_FILES
    # OpenCode takes its project dir from PWD, not the process cwd: without --dir and PWD it ran in
    # this repo (smoke test 2026-11-06) and edited files here.
    env = dict(os.environ, PWD=wd, OPENCODE_DISABLE_CLAUDE_CODE="1", OPENCODE_CONFIG_CONTENT=json.dumps(cfg))
    t = time.time()
    p = subprocess.run([OPENCODE, "run", "--dir", wd, "--model", f"ollama/{model}", "--format", "json", prompt],
                       stdin=subprocess.DEVNULL, cwd=wd, env=env, capture_output=True, text=True, timeout=timeout)
    events = [json.loads(l) for l in p.stdout.splitlines() if l.strip().startswith("{")]
    parts = [e.get("part", {}) for e in events]
    seq = [("tool", x.get("tool"), x.get("state", {}).get("input", {}).get("command", "")) if x.get("type") == "tool"
           else ("text", x.get("text", ""), "") for x in parts if x.get("type") in ("tool", "text")]
    texts = [x for x in parts if x.get("type") == "text"]
    last = texts[-1]["messageID"] if texts else None
    final = "\n".join(x.get("text", "") for x in texts if x["messageID"] == last)
    tok = [x["tokens"] for x in parts if x.get("type") == "step-finish"]
    usage = {"input_tokens": sum(k.get("input", 0) for k in tok),
             "cache_creation_input_tokens": sum(k.get("cache", {}).get("write", 0) for k in tok),
             "cache_read_input_tokens": sum(k.get("cache", {}).get("read", 0) for k in tok),
             "output_tokens": sum(k.get("output", 0) + k.get("reasoning", 0) for k in tok)}
    res = {"result": final, "usage": usage, "num_turns": len(tok)}
    return events, seq, res, time.time() - t


def claude(model, wd, prompt, tools_off=False, timeout=900, provider="anthropic", agent_tool=False):
    cmd = ["claude", "-p", "--setting-sources", "project", "--model", model,
           "--output-format", "stream-json", "--verbose"]
    cmd += (["--disallowedTools", "Bash,Read,Grep,Glob,Edit,Write,WebFetch,WebSearch,Agent"] if tools_off
            else ["--allowedTools", "Bash,Read,Edit,Write,Glob,Grep" + (",Agent" if agent_tool else "")])
    t = time.time()
    p = subprocess.run(cmd, input=prompt, cwd=wd, env=dict(claude_env(provider, model), PWD=wd),
                       capture_output=True, text=True, timeout=timeout)
    events = [json.loads(l) for l in p.stdout.splitlines() if l.strip().startswith("{")]
    seq = [("tool", c.get("name"), c["input"].get("command", "")) if c.get("type") == "tool_use"
           else ("text", c.get("text", ""), "")
           for e in events if e.get("type") == "assistant"
           for c in e["message"].get("content", []) if c.get("type") in ("tool_use", "text")]
    res = next((e for e in reversed(events) if e.get("type") == "result"), {})
    for d in res.get("permission_denials") or []:
        fp, body = d.get("tool_input", {}).get("file_path", ""), d.get("tool_input", {}).get("content")
        if body is not None and fp.startswith(wd):
            out = os.path.join(wd, "_denied", os.path.relpath(fp, wd))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w").write(body)
    return events, seq, res, time.time() - t


def agent(harness, provider, model, wd, prompt, arm, tools_off=False, agent_tool=False):
    if harness == "opencode":
        return opencode(model, wd, prompt, arm, tools_off)
    return claude(model, wd, prompt, tools_off, provider=provider, agent_tool=agent_tool)


def pre_subject(seq, subject):
    """Agent text before the first shell command that mentions `subject`."""
    out = []
    for kind, a, b in seq:
        if kind == "tool" and subject in b:
            break
        if kind == "text":
            out.append(a)
    return "\n".join(out)


def run_harness(model, probe, arm, rep, tag, root, harness="claude", provider="anthropic"):
    pdir = os.path.join(STUDY, "probes", probe)
    wd = setup_workdir(root, os.path.join(pdir, "fixture"), arm, f"{tag}_{probe}_{arm}_{rep}", harness)
    events, seq, res, dur = agent(harness, provider, model, wd, open(os.path.join(pdir, "task.txt")).read(), arm,
                                  agent_tool=os.path.exists(os.path.join(pdir, "allow_agent")))
    bash = [b for k, n, b in seq if k == "tool" and n in ("Bash", "bash")]
    tools = [n for k, n, _ in seq if k == "tool"]
    subj = os.path.join(pdir, "subject.txt")
    pre = pre_subject(seq, open(subj).read().strip()) if os.path.exists(subj) else ""
    raw = os.path.join(RAW, f"{tag}_{harness}-{provider}_{probe}_{arm}_{rep}.jsonl")
    open(raw, "w").write("\n".join(json.dumps(e) for e in events))
    s = score(probe, "harness", res.get("result", ""), wd, bash, tools, pre)
    u = res.get("usage", {})
    return dict(pass_=s["pass_"], detail=s["detail"], input_tokens=u.get("input_tokens"),
                cache_creation_tokens=u.get("cache_creation_input_tokens"),
                cache_read_tokens=u.get("cache_read_input_tokens"), output_tokens=u.get("output_tokens"),
                turns=res.get("num_turns"), duration_s=round(dur, 1), cost_usd=res.get("total_cost_usd"), raw=raw)


# ---------- containment tripwire ----------
def repo_state():
    """Repo files outside study/raw and study/results: path -> (size, mtime)."""
    st = {}
    for dp, dns, fs in os.walk(REPO):
        rel = os.path.relpath(dp, REPO)
        if rel.split(os.sep)[0] == ".git" or rel.startswith(("study/raw", "study/results")):
            dns[:] = []
            continue
        dns[:] = [d for d in dns if d != "__pycache__"]
        for f in fs:
            p = os.path.join(dp, f)
            s = os.stat(p)
            st[os.path.relpath(p, REPO)] = (s.st_size, s.st_mtime)
    return st


def check_contained(before):
    after = repo_state()
    diff = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
    if diff:
        print("CONTAINMENT FAIL: repo changed during run:", diff[:10], flush=True)
        os._exit(3)


# ---------- isolation check ----------
def isolation(layer, model, arm, root, tag, harness="claude", provider="anthropic"):
    if layer == "model":
        r, _ = ollama(model, directives() if arm == "A1" else None, ISO_Q)
        text = r["message"]["content"]
    else:
        wd = setup_workdir(root, None, arm, f"{tag}_iso_{arm}", harness)
        _, _, res, _ = agent(harness, provider, model, wd, ISO_Q, arm, tools_off=True)
        text = res.get("result", "")
    seen = VERSION in text
    ok = seen if arm == "A1" else not seen
    print(f"isolation {layer} {harness}-{provider} {arm}: {'ok' if ok else 'FAIL'} ({text.strip()[:80]!r})", flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", choices=["model", "harness"], required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--harness", choices=["claude", "opencode"], default="claude")
    ap.add_argument("--provider", choices=["anthropic", "ollama"], default=None,
                    help="default: anthropic for claude, ollama for opencode")
    ap.add_argument("--probes", default="I01,I02,F06")
    ap.add_argument("--arms", default="A0,A1")
    ap.add_argument("--reps", type=int, default=5)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--root", required=True, help="scratch dir outside the repo for harness workdirs")
    ap.add_argument("--out", default=os.path.join(STUDY, "results", "runs.csv"))
    a = ap.parse_args()
    a.provider = a.provider or ("ollama" if a.harness == "opencode" else "anthropic")
    assert not (a.harness == "opencode" and a.provider == "anthropic"), "OpenCode: no Anthropic credential"
    if a.layer == "model":
        a.harness, a.provider = "", "ollama"
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(a.root, exist_ok=True)
    assert not os.path.abspath(a.root).startswith(REPO), "root must be outside the repo (CLAUDE.md discovery)"
    tag = time.strftime("%Y%m%dT%H%M%S")
    before = repo_state()
    arms = [x for x in a.arms.split(",") if isolation(a.layer, a.model, x, a.root, tag, a.harness, a.provider)]
    check_contained(before)
    jobs = [(p, x, r) for p in a.probes.split(",") for x in arms for r in range(a.reps)]
    new = not os.path.exists(a.out)
    with open(a.out, "a", newline="") as fh, cf.ThreadPoolExecutor(a.workers) as ex:
        w = csv.DictWriter(fh, FIELDS)
        if new:
            w.writeheader()
        fn = run_model if a.layer == "model" else run_harness
        extra = () if a.layer == "model" else (a.root, a.harness, a.provider)
        futs = {ex.submit(fn, a.model, p, x, r, tag, *extra): (p, x, r) for p, x, r in jobs}
        for f in cf.as_completed(futs):
            p, x, r = futs[f]
            try:
                d = f.result()
            except Exception as e:  # record failures, do not drop them
                d = dict(pass_="", detail=f"ERROR {type(e).__name__}: {e}"[:200])
            row = {"ts": tag, "layer": a.layer, "harness": a.harness, "provider": a.provider, "model": a.model, "probe": p, "arm": x, "rep": r,
                   "pass": d.pop("pass_"), **d}
            row["raw"] = os.path.relpath(row.get("raw", ""), REPO) if row.get("raw") else ""
            w.writerow(row)
            fh.flush()
            check_contained(before)
            print(p, x, r, row["pass"], row["detail"], flush=True)


if __name__ == "__main__":
    main()
