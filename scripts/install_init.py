#!/usr/bin/env python3
"""install_init.py — bootstrap installer for INIT.md projects.

For a novice user: checks/installs Git and Claude Code, explains the two
Claude billing routes (paid plan vs API-key billing) with pros and cons,
optionally sets up Ollama (the open-model route), scaffolds a project folder
with the three companion files, and prints first-session starter prompts.

Usage:
    python3 install_init.py                 interactive run
    python3 install_init.py --check         diagnose only; changes nothing
    python3 install_init.py --skip-ollama   skip the optional Ollama branch
    python3 install_init.py --dir PATH      project directory (default: prompt)

Stdlib only. Idempotent: safe to re-run; every step checks before acting.

Scope (v1): Linux and macOS, Claude Code primary. Windows is out of scope
here; this script points to the Windows walkthrough in
ancillary/AI_install.md §6 of the INIT.md repo.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request

REPO = "https://github.com/slisgo-projects/INIT.md"
RAW = "https://raw.githubusercontent.com/slisgo-projects/INIT.md/main"
WINDOWS_GUIDE = REPO + "/blob/main/ancillary/AI_install.md"
CLAUDE_SIGNUP = "https://claude.com/signup"
CLAUDE_CONSOLE = "https://console.anthropic.com"
CLAUDE_PRICING = "https://claude.com/pricing"
OLLAMA_PRICING = "https://ollama.com/pricing"

COMPANION_FILES = ["INIT.md", "USE_CASE_INIT.md", "CODING_PRACTICES.md"]

WIN_NOTE = (
    "Windows: this script targets Linux/macOS. Follow the Windows walkthrough in "
    "ancillary/AI_install.md §6 of the INIT.md repo: " + WINDOWS_GUIDE
)

BILLING_CLAUDE = f"""Two ways to pay for Claude:

  Option 1 — Paid Claude plan (Pro or higher): {CLAUDE_PRICING}
    Pros:
      - Flat monthly fee; predictable cost, no usage metering to watch.
      - Claude Code included; sign-in is one browser step.
    Cons:
      - Heavier use of higher-tier models can hit weekly limits.
      - More expensive than metered billing for occasional light use.

  Option 2 — Claude Console account, billed by usage (API key): {CLAUDE_CONSOLE}
    Pros:
      - Pay per token; cheaper for light or occasional use.
      - Works with any harness that speaks the Anthropic API.
    Cons:
      - Bills can spike with long sessions or agent loops; you watch usage.
      - Extra setup: create an API key in the Console and put it in
        Claude Code when asked (or run: export ANTHROPIC_API_KEY=sk-ant-...).

  Recommendation: occasional use -> Option 2 (API key); regular project work
  -> Option 1 (plan). Both work with Claude Code and with INIT.md."""

OLLAMA_PITCH = (
    "Ollama is the open-model route; no Anthropic account needed.\n"
    "  - Local models: no account, no per-token cost, full privacy — but need\n"
    "    a capable machine (tool-calling model, 64k+ context, ample RAM).\n"
    "  - Cloud models: run on Ollama's servers; Pay as you go is $0 to join and\n"
    "    you buy usage credits (" + OLLAMA_PRICING + "). No monthly plan required.\n"
    "  Claude Code runs on Ollama models; setup is in ancillary/AI_install.md."
)

STARTER_PROMPTS = [
    ("Describe your project first, then start:",
     "Please read INIT.md in this folder and let's set up a project. I want to "
     "do this because: (1) … (2) … (3) … The deliverables I have in mind are: "
     "(a) … (b) … (c) …"),
    ("Or have Claude interview you:",
     "Please read INIT.md and interview me about the project."),
]

INSTALL_README_TEMPLATE = """# Getting started with INIT.md

Files in this folder: `INIT.md` (the rules), `USE_CASE_INIT.md` (how use cases
are described), `CODING_PRACTICES.md` (AI working habits). That is all you need
from the upstream repository: {repo}

## Sign in (one-time)

Claude asks you to sign in the first time it runs. In the browser window that
opens, create a Claude account or sign in, and pick a billing route:

{billing}

## Start your first session

Open a terminal in this folder and run:

    claude

Then paste one of these as your first message:

{prompts}

Claude drafts the first planning document and checks with you at each step.
A full project setup can take about an hour for an ambitious project.

## Alternatives

- **Ollama (open models, no Anthropic account):** install from
  <https://ollama.com/download>, then follow the INIT.md repo's
  `ancillary/AI_install.md` for running Claude Code on Ollama models.
- **Windows:** use the walkthrough in the INIT.md repo's
  `ancillary/AI_install.md` §6: {win_guide}

Upstream repository and documentation: {repo}
"""


# --- helpers ----------------------------------------------------------------


def say(msg=""):
    print(msg)


def have(cmd):
    return bool(shutil.which(cmd))


def sh(cmd):
    """Run a shell command; return (ok, output, error)."""
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return False, "", "timed out"
    return p.returncode == 0, (p.stdout or "").strip(), (p.stderr or "").strip()


def on_windows():
    return sys.platform in ("win32", "cygwin", "msys")


def download(url):
    """Fetch url; return bytes. Raises on failure."""
    req = urllib.request.Request(
        url, headers={"User-Agent": "install_init.py/1.0 (INIT.md installer)"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def ask(prompt, default=None):
    """Yes/no prompt. default=True/False applies to empty input; None requires y/n."""
    while True:
        r = input(prompt + " [y/n] ").strip().lower()
        if r in ("y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        if default is not None and r == "":
            return default
        say("  please answer y or n")


def version_of(cmd):
    ok, out, _ = sh(f"{cmd} --version")
    return out.splitlines()[0] if ok and out else "unknown"


# --- checks -----------------------------------------------------------------


def net_ok():
    try:
        download(RAW + "/LICENSE")
        return True
    except Exception:
        return False


def report_checks():
    """Diagnose only; change nothing. Returns dict of states."""
    git = have("git")
    claude = have("claude")
    ollama = have("ollama")
    net = net_ok()

    say("== Requirements check ==")
    say(f"  [{'ok' if sys.version_info >= (3, 8) else '!!'}] Python 3.8+ (this installer): "
        f"{sys.version_info.major}.{sys.version_info.minor}")
    say(f"  [{'ok' if git else '!!'}] git: {version_of('git') if git else 'not installed'}")
    say(f"  [{'ok' if claude else '!!'}] claude (Claude Code): "
        f"{version_of('claude') if claude else 'not installed'}")
    say(f"  [{'ok' if ollama else '--'}] ollama (optional route): "
        f"{version_of('ollama') if ollama else 'not installed'}")
    say(f"  [{'ok' if net else '!!'}] network access to {RAW}")
    say("")
    if not claude:
        say("  To install Claude Code: curl -fsSL https://claude.ai/install.sh | bash")
        say("  (Windows: see " + WINDOWS_GUIDE + ")")
    if not git:
        say("  git is recommended; install with your package manager.")
    return {"git": git, "claude": claude, "ollama": ollama, "net": net}


# --- install steps ----------------------------------------------------------


def install_git():
    if have("git"):
        say("[ok] git already installed: " + version_of("git"))
        return True
    if on_windows():
        say(WIN_NOTE)
        return False
    say("[..] git is missing. Recommended so the AI can version your project.")
    ok, out, err = sh("sudo apt-get update && sudo apt-get install -y git")
    if not ok:
        say("  apt install failed (may need a different package manager, or sudo")
        say("  refused). Install git yourself, then re-run this script:")
        say("    Debian/Ubuntu: sudo apt-get install -y git")
        say("    Fedora:        sudo dnf install -y git")
        say("    macOS:         xcode-select --install")
        if err:
            say("  (" + err.splitlines()[-1][:200] + ")")
        return False
    say("[ok] git installed: " + version_of("git"))
    return True


def install_claude():
    if have("claude"):
        say("[ok] Claude Code already installed: " + version_of("claude"))
        return True
    if on_windows():
        say(WIN_NOTE)
        return False
    say("[..] installing Claude Code (official installer)...")
    ok, _, err = sh("curl -fsSL https://claude.ai/install.sh | bash")
    if not ok or not have("claude"):
        say("  installer did not produce a 'claude' command. Manual install:")
        say("    https://claude.com/claude-code")
        if err:
            say("  (" + err.splitlines()[-1][:200] + ")")
        return False
    say("[ok] Claude Code installed: " + version_of("claude"))
    return True


def scaffold(directory):
    """Download the three companion files into directory; return True on success."""
    say("")
    say("== Project folder: " + directory + " ==")
    os.makedirs(directory, exist_ok=True)
    all_ok = True
    for name in COMPANION_FILES:
        dest = os.path.join(directory, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            say(f"[ok] {name} already present")
            continue
        try:
            data = download(f"{RAW}/{name}")
        except Exception as e:
            say(f"[FAILED] {name}: {e}")
            all_ok = False
            continue
        with open(dest, "wb") as f:
            f.write(data)
        head = data[:60].decode("utf-8", "replace").splitlines()[0]
        say(f"[dl] {name}: {len(data)} bytes — {head}")
    readme = os.path.join(directory, "INSTALL_README.md")
    if not os.path.exists(readme):
        with open(readme, "w") as f:
            f.write(INSTALL_README_TEMPLATE.format(
                repo=REPO, billing=BILLING_CLAUDE, win_guide=WINDOWS_GUIDE,
                prompts="\n".join("    " + text for _, text in STARTER_PROMPTS),
            ))
        say("[**] wrote INSTALL_README.md (billing options, first-session prompts)")
    return all_ok


def end_to_end_probe():
    """Functional check: a real non-interactive call, not just binary presence."""
    say("")
    say("== End-to-end probe ==")
    if not have("claude"):
        say("[skip] claude not installed yet")
        return
    say("  running: claude -p (headless, expects a one-word reply)")
    ok, out, err = sh('claude -p "Reply with exactly the word: OK"')
    if ok and "OK" in out:
        say("[ok] probe passed — Claude Code reached a live model and replied: " + out[:40])
        return
    say("[warn] probe did not pass yet — usually just means you have not signed in.")
    say("  Sign-in happens the first time you run 'claude' in your project folder;")
    say("  after signing in, re-run this script to see the probe pass.")
    if err:
        say("  (" + err.splitlines()[-1][:200] + ")")


def ollama_branch(skip):
    if skip:
        return
    say("")
    say("== Ollama (optional open-model route) ==")
    say(OLLAMA_PITCH)
    if have("ollama"):
        say("[ok] Ollama already installed: " + version_of("ollama"))
    elif ask("Install Ollama now?"):
        if on_windows():
            say(WIN_NOTE)
        else:
            ok, _, err = sh("curl -fsSL https://ollama.com/install.sh | sh")
            if ok and have("ollama"):
                say("[ok] Ollama installed: " + version_of("ollama"))
            else:
                say("  installer failed; manual install: https://ollama.com/download")
                if err:
                    say("  (" + err.splitlines()[-1][:200] + ")")
    else:
        say("[skip] Ollama skipped (can re-run this script any time)")
        return
    if ask("Open the Ollama sign-in / account page in your browser? (cloud models need credits; local models need no account)"):
        try:
            import webbrowser
            webbrowser.open(OLLAMA_PRICING)
        except Exception:
            say("  open manually: " + OLLAMA_PRICING)
        say("  Choose 'Pay as you go' ($0 to join). Then run: ollama signin")
        say("  Full model + Claude Code setup: ancillary/AI_install.md in the INIT.md repo")


def handoff(probe_ok):
    say("")
    say("== Ready ==")
    if not probe_ok:
        say("  One step left before the first session: sign in to Claude.")
        say("    Run 'claude' once; a browser window opens; pick a billing route")
        say("    (paid plan or API key — pros and cons printed above and in")
        say("    INSTALL_README.md).")
    say("  First session — in this folder, run: claude")
    for label, text in STARTER_PROMPTS:
        say("")
        say("  " + label)
        say("    " + text)
    say("")
    say("Full guide: " + REPO + " (README.md); Windows route: " + WINDOWS_GUIDE)


# --- main -------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description="INIT.md project bootstrap installer")
    ap.add_argument("--check", action="store_true", help="diagnose only, change nothing")
    ap.add_argument("--skip-ollama", action="store_true", help="skip the optional Ollama branch")
    ap.add_argument("--dir", metavar="PATH", help="project directory (default: prompt)")
    args = ap.parse_args()

    say("INIT.md installer — sets up the tools and files for an AI-assisted project.")
    say(REPO)
    if on_windows():
        say("")
        say(WIN_NOTE)

    states = report_checks()

    if args.check:
        return 0

    say("")
    say(BILLING_CLAUDE)

    if not states["net"]:
        say("")
        say("ERROR: cannot reach " + RAW + " — needed to fetch the companion files.")
        say("Check your internet connection and re-run.")
        return 1

    if not ask("Continue with setup?", default=True):
        return 0

    install_git()
    say("")
    if not ask("Install/verify Claude Code now?"):
        say("[skip] Claude Code install skipped — install later from:")
        say("  https://claude.com/claude-code")
        claude_ok = False
    else:
        claude_ok = install_claude()

    ollama_branch(args.skip_ollama)

    directory = args.dir
    if not directory:
        default_dir = os.path.join(os.path.expanduser("~"), "INIT.md-project")
        r = input("Project directory [" + default_dir + "]: ").strip()
        directory = os.path.expanduser(r or default_dir)
    scaffold_ok = scaffold(directory)
    if not scaffold_ok:
        say("")
        say("ERROR: one or more companion files failed to download; the project")
        say("folder is incomplete. Fix the network problem and re-run this script —")
        say("completed files are kept.")
        return 1

    if claude_ok:
        end_to_end_probe()
    handoff(probe_ok=claude_ok)
    return 0


if __name__ == "__main__":
    sys.exit(main())
