# AI_install.md

> **Document status — unclassified.** This guide is no part of the INIT.md flowdown. It carries no flowdown group, is not registered in the CLAUDE.md markdown-hierarchy stub, and is governed by per-project direction rather than the spec. It lives in `ancillary/` purely to keep the project root clean. See INIT.md §"Project Markdown Files" (Directory layout). Skip the rest of this note if you are here to install something.

Getting started with AI for a new user of this project: install Ollama, set up a free Ollama account, pull the `kimi-k2.6:cloud` model, install Claude Code, and run Claude Code through Ollama using that model.

This guide uses a **cloud** model (`kimi-k2.6:cloud`). Cloud models run on Ollama's servers, so you do **not** need a powerful GPU or large amounts of RAM — the local Ollama process proxies your requests to Ollama's cloud. This is the easiest path for a new user. (A fully local model would instead need a 64k+ context window and sufficient local hardware; not covered here.)

**Prerequisite:** a modern web browser (for the one-time Ollama sign-in) and an internet connection.

**On Windows 11?** Sections 1–5 are written platform-neutrally, but §6 is a self-contained PowerShell walkthrough covering the same ground with the Windows-specific traps handled. Go straight there. §3.1 (finding models) applies to every platform.

---

## 1. Install Ollama

### Windows

1. Download the installer from <https://ollama.com/download> and run it.

2. Ollama installs as a background service (`Ollama.exe`) and starts automatically. Confirm it is running — an Ollama icon appears in the system tray.

3. Open a terminal (PowerShell or Command Prompt) and verify:
   
   ```powershell
   ollama --version
   ```

### Linux

1. Install with the official script:
   
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Start the Ollama server (most installs start it automatically; if not):
   
   ```bash
   ollama serve
   ```
   
   (Run this in its own terminal, or as a background service per your distro's conventions.)

3. Verify in a second terminal:
   
   ```bash
   ollama --version
   ```

Ollama needs version **0.14.0 or later** for Anthropic-API compatibility (required by Claude Code). If your version is older, reinstall from <https://ollama.com/download>.

---

## 2. Create a free Ollama account and sign in

Ollama accounts are free.

1. In your terminal, run:
   
   ```bash
   ollama signin
   ```

2. This opens your browser at <https://ollama.com/connect>. Create an account (or sign in if you already have one) and authorize the CLI.

3. Return to the terminal; it confirms you are signed in.

To confirm later, run `ollama signin` again — it will report you are already connected, or let you switch accounts.

---

## 3. Pull the Ollama models

Pull the cloud model stub so your local Ollama knows how to route requests to the cloud:

```bash
ollama pull kimi-k2.6:cloud
ollama pull gemma4:31b-cloud
```

This downloads only a small routing stub — not a multi-gigabyte model file — because the actual model runs on Ollama's cloud.

> **If the pull fails with "model not found":** the exact tag has probably moved. See §3.1 below to find the current tag, then use that name in place of `kimi-k2.6:cloud` throughout this guide.

Verify the model is available locally:

```bash
ollama list
```

You should see `kimi-k2.6:cloud` in the list.

---

## 3.1 Find and pull additional models

Model names and tags change over time — new models ship, old ones retire. Use this section whenever a tag in this guide has gone stale, or when you want to try a different model.

### Browse the catalogue (easiest)

There is **no `ollama search` command**. Discovery happens on the website:

- **All models:** <https://ollama.com/search>
- **Cloud models only:** <https://ollama.com/search?c=cloud> — these are the ones that need no local GPU. Start here.
- **One model's tags:** `https://ollama.com/library/<model>` — e.g. <https://ollama.com/library/gemma4>. The tag list on that page is authoritative; the model page also shows the exact `ollama run` command to copy.

The search page filters by capability (Cloud, Embedding, Vision, Tools, Thinking) and sorts by Popular or Newest.

### List cloud models from the terminal

```bash
curl -s https://ollama.com/api/tags
```

> **Trap:** this endpoint returns base names **without** the cloud suffix — you will see `kimi-k2.6` and `gemma4:31b`, not `kimi-k2.6:cloud` and `gemma4:31b-cloud`. Add the suffix yourself per the naming rule below, or confirm the tag on the model's library page.

> **Windows PowerShell:** `curl` is an alias for `Invoke-WebRequest` in Windows PowerShell 5.1 and the flags above will fail. Use `irm` instead — see §6.4.

### Cloud tag naming

Cloud variants append `-cloud` to the size tag, or use a bare `:cloud` tag when the model has no size variants:

| Model page shows            | Pull as              |
| --------------------------- | -------------------- |
| a size tag (`31b`)          | `gemma4:31b-cloud`   |
| no size variants            | `kimi-k2.6:cloud`    |
| a size tag, largest default | `gpt-oss:120b-cloud` |

### Pull and verify

```bash
ollama pull <model>:<tag>     # download (a small stub for cloud models)
ollama list                   # confirm it is present locally
ollama show <model>:<tag>     # context window, capabilities, parameters
ollama run <model>:<tag>      # quick interactive smoke test; /bye to exit
```

`ollama show` is worth running before you commit to a model as your primary: check the context window is large enough for Claude Code (64k or more; `kimi-k2.6:cloud` offers far more).

### Using a different model with Claude Code

Any pulled model can be swapped in by changing the environment variables in step 5 — nothing else in the setup changes:

- `ANTHROPIC_MODEL` — your primary model. Needs a large context window and tool-calling support.
- `ANTHROPIC_SMALL_FAST_MODEL` — background tasks. A smaller, cheaper model is the point; it does not need a large context.

Pull the model first, then start Claude Code with the new name.

### Local (non-cloud) models

Local models run entirely on your machine — no account, no network, no per-token cost — but they download the full weights and need the RAM/VRAM to hold them. Pull them without the cloud suffix:

```bash
ollama pull gemma4:12b
```

Rough guide: a model's download size is close to its RAM requirement, and you need headroom on top for the context window. For Claude Code specifically, a local model must support tool calling and a 64k+ context to be usable, which puts realistic local setups at the high end of consumer hardware. This is why the guide defaults to cloud models.

Housekeeping:

```bash
ollama list          # what is installed
ollama ps            # what is currently loaded in memory
ollama stop <model>  # unload from memory
ollama rm <model>    # delete
```

---

## 4. Install Claude Code

### Linux

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Then verify:

```bash
claude --version
```

### Windows (PowerShell)

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then verify:

```powershell
claude --version
```

---

## 5. Run Claude Code through Ollama using `kimi-k2.6:cloud`

There are three methods. **Method A is the working setup used by this project** — a single CLI invocation. Methods B and C are fallbacks if Method A does not apply (different Ollama version, prefer not to set vars inline).

> **On Windows PowerShell, skip to §6.** Method A's inline-variable syntax is bash-only and fails in PowerShell.

> **A note on the base URL.** All methods point Claude Code at the local Ollama server's Anthropic-compatible API on its **default port, `11434`**. If you have remapped Ollama to a different port, substitute that port in `ANTHROPIC_BASE_URL`. (One of this project's maintainers runs Ollama on a non-default port for unrelated reasons — your default install uses `11434`.)

### Method A — single CLI invocation (recommended; the project's working setup)

Run Claude Code with the environment variables inline. From your project directory (Linux / macOS / WSL / Windows bash):

```bash
ANTHROPIC_BASE_URL=http://localhost:11434 \
ANTHROPIC_AUTH_TOKEN=ollama \
ANTHROPIC_MODEL=kimi-k2.6:cloud \
ANTHROPIC_SMALL_FAST_MODEL=gemma4:31b-cloud \
claude
```

This is the invocation used to run Claude Code for this project (with the base URL on Ollama's default port). It requires Ollama running and reachable at `http://localhost:11434`, and both models pulled (see step 3 — pull `gemma4:31b-cloud` the same way if it is not already present: `ollama pull gemma4:31b-cloud`).

What each variable does:

- `ANTHROPIC_BASE_URL=http://localhost:11434` — routes Claude Code's requests to the local Ollama server, which forwards cloud-model requests to Ollama's cloud.
- `ANTHROPIC_AUTH_TOKEN=ollama` — a bearer token Ollama ignores but Claude Code requires, so it does not fall back to a paid Anthropic subscription login.
- `ANTHROPIC_MODEL=kimi-k2.6:cloud` — the primary model Claude Code uses for your requests.
- `ANTHROPIC_SMALL_FAST_MODEL=gemma4:31b-cloud` — the model Claude Code uses for small, fast background tasks (session titles, summaries, etc.). Mapped to a **separate, lighter cloud model** so background work runs cheaper/faster and does not try to call Anthropic's servers. This split is the key practical detail: the primary model and the background model need not be the same.

### Method B — `ollama launch` (fallback if you have a recent Ollama)

From your project directory:

```bash
ollama launch claude --model kimi-k2.6:cloud
```

This starts Ollama (if not already running), points Claude Code at it, and sets the model in one command. It does not set the small/fast model separately, so background tasks will use the default — Method A is preferred for that reason.

### Method C — manual environment variables, exported (fallback)

Use this if you prefer to export the variables rather than pass them inline (Method A). Set the variables that route Claude Code at Ollama and map it to the cloud model, then run `claude`.

**Linux / macOS (bash):**

```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_MODEL="kimi-k2.6:cloud"
export ANTHROPIC_SMALL_FAST_MODEL="gemma4:31b-cloud"
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS="1"

claude
```

**Windows (PowerShell):**

```powershell
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:ANTHROPIC_API_KEY = ""
$env:ANTHROPIC_MODEL = "kimi-k2.6:cloud"
$env:ANTHROPIC_SMALL_FAST_MODEL = "gemma4:31b-cloud"
$env:CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS = "1"

claude
```

Additional variables (Method C only):

- `ANTHROPIC_API_KEY` — explicitly emptied to avoid "model not found" errors from subscription precedence.
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` — prevents "unexpected beta header" errors when using a non-Anthropic backend.

### Make it permanent (optional)

To avoid typing the Method A command every session, add the variables to `~/.claude/settings.json` (Linux) or `%USERPROFILE%\.claude\settings.json` (Windows):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:11434",
    "ANTHROPIC_AUTH_TOKEN": "ollama",
    "ANTHROPIC_MODEL": "kimi-k2.6:cloud",
    "ANTHROPIC_SMALL_FAST_MODEL": "gemma4:31b-cloud"
  }
}
```

(Add `ANTHROPIC_API_KEY=""` and `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS="1"` if you hit subscription-precedence or beta-header errors. If you remap Ollama off its default port, change `ANTHROPIC_BASE_URL` to match.)

---

## 6. Windows 11 + PowerShell — complete walkthrough

Sections 1–5 cover every platform. This section is the same setup as a single copy-paste sequence for Windows 11, with the Windows-specific differences called out. Follow this **instead of** sections 1–5 if you are on Windows.

> **The one thing that catches everyone:** Method A in §5 (`VAR=value claude`) is bash syntax. It **does not work in PowerShell** — PowerShell reads `ANTHROPIC_BASE_URL=http://localhost:11434` as a command name and fails with `The term '...' is not recognized`. On Windows, use §6.5 below.

### 6.1 Open the right terminal

Press <kbd>Win</kbd> and type "Terminal" — open **Windows Terminal**. It defaults to PowerShell; the prompt reads `PS C:\Users\YourName>`. If the `PS` is missing you are in Command Prompt, and the commands below will not work.

Administrator rights are **not** needed for any step except the `winget` installs.

Everything here works in both Windows PowerShell 5.1 (the built-in one) and PowerShell 7+. Where the two differ, it is noted.

### 6.2 Install Ollama

Either use winget (in an **Administrator** terminal):

```powershell
winget install --id Ollama.Ollama -e
```

Or download the installer from <https://ollama.com/download> and run it.

Ollama installs as a background service and starts automatically — look for the llama icon in the system tray (you may need to click the `^` to expand hidden icons). Windows Defender Firewall may prompt on first run; allowing it on private networks is enough.

**Close and reopen your terminal** so the updated `PATH` is picked up, then verify:

```powershell
ollama --version
```

You need **0.14.0 or later** for the Anthropic-API compatibility Claude Code relies on. If `ollama` is still not recognized after reopening the terminal, refresh `PATH` in the current session:

```powershell
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
```

> On Windows, `ollama serve` is usually unnecessary — the tray service already holds port 11434. Running it manually while the tray app is active fails with `Only one usage of each socket address ... is normally permitted`. That error means Ollama is already running, not that something is broken.

### 6.3 Sign in

```powershell
ollama signin
```

Your browser opens at <https://ollama.com/connect>. Create the free account or sign in, authorize the CLI, then return to the terminal.

### 6.4 Pull the models

```powershell
ollama pull kimi-k2.6:cloud
ollama pull gemma4:31b-cloud
ollama list
```

To browse for other models, use the website links in §3.1. If you want the terminal listing, **do not use the `curl` command from §3.1** — in Windows PowerShell 5.1 `curl` is an alias for `Invoke-WebRequest` and rejects the `-s` flag. Use `irm` (`Invoke-RestMethod`), which also parses the JSON for you:

```powershell
(irm https://ollama.com/api/tags).models.name
```

Remember the suffix rule from §3.1: that listing prints `kimi-k2.6`, but you pull `kimi-k2.6:cloud`.

(In PowerShell 7+ the `curl` alias was removed, so `curl.exe -s https://ollama.com/api/tags` works there. `irm` works in both.)

### 6.5 Install Claude Code

```powershell
irm https://claude.ai/install.ps1 | iex
```

If that is blocked with `running scripts is disabled on this system`, allow scripts for this session only — this does not change your machine-wide policy:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then rerun the install line. Alternatively, install via winget in an Administrator terminal (`winget install Anthropic.ClaudeCode`), which needs no execution-policy change but does not auto-update.

**Reopen your terminal**, then verify:

```powershell
claude --version
```

**Optional but recommended:** install [Git for Windows](https://git-scm.com/downloads/win). Claude Code uses Git Bash for its Bash tool when present; without it, it falls back to a PowerShell tool with a narrower command set.

### 6.6 Run Claude Code through Ollama

Set the variables, then launch. From your project directory:

```powershell
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:ANTHROPIC_API_KEY = ""
$env:ANTHROPIC_MODEL = "kimi-k2.6:cloud"
$env:ANTHROPIC_SMALL_FAST_MODEL = "gemma4:31b-cloud"
$env:CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS = "1"

claude
```

The variables mean the same thing as in §5 — see the explanations there.

`$env:` assignments last only for the current terminal window. You must repeat them every time you open a new one, unless you make them permanent (§6.7).

### 6.7 Make it permanent

Two options. **Pick one, not both** — duplicated settings in two places is the most common source of "I changed it and nothing happened."

**Option A — Claude Code settings file (recommended).** Scoped to Claude Code, so it cannot affect other tools:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude" | Out-Null
notepad "$env:USERPROFILE\.claude\settings.json"
```

Paste, save, close:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:11434",
    "ANTHROPIC_AUTH_TOKEN": "ollama",
    "ANTHROPIC_MODEL": "kimi-k2.6:cloud",
    "ANTHROPIC_SMALL_FAST_MODEL": "gemma4:31b-cloud"
  }
}
```

If Notepad offers to save as `settings.json.txt`, choose "All Files" in the save dialog. Confirm the result parses:

```powershell
Get-Content "$env:USERPROFILE\.claude\settings.json" | ConvertFrom-Json
```

Then `claude` alone works from any directory.

**Option B — persistent user environment variables.** Machine-wide for your user account, visible to every program:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "http://localhost:11434", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "ollama", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "kimi-k2.6:cloud", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_SMALL_FAST_MODEL", "gemma4:31b-cloud", "User")
```

These apply to **new** terminals only. To undo any of them, set the value to `$null`.

### 6.8 Windows-specific notes

- **Model storage.** Cloud stubs are tiny, but local models land in `%USERPROFILE%\.ollama\models` on your system drive. To move them to another drive, set `OLLAMA_MODELS`:
  
  ```powershell
  [Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\ollama\models", "User")
  ```
  
  Restart Ollama from the tray afterwards.
- **Paths in `settings.json`** need doubled backslashes (`"C:\\Program Files\\Git\\bin\\bash.exe"`) — JSON treats a single backslash as an escape character.
- **WSL is an alternative, not a requirement.** If your projects already live in WSL, install Ollama and Claude Code inside the WSL distribution and follow the Linux instructions in §§1–5 instead. Do not mix: a Claude Code running in WSL reaching a Windows-side Ollama needs a different host address than `localhost`.
- **Diagnostics.** `claude doctor` prints installation and settings health, including JSON parse errors in `settings.json`, without starting a session.

---

## Troubleshooting

- **"Model not found" / subscription errors** — ensure `ANTHROPIC_API_KEY` is empty and `ANTHROPIC_AUTH_TOKEN` is set to `ollama`; confirm you are not signed into a Claude Pro/Max account, which can take precedence.
- **"Unexpected beta header" error** — set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.
- **Background tasks (titles, summaries) fail or call Anthropic** — the small/fast tier must map to a local/cloud model; confirm `ANTHROPIC_SMALL_FAST_MODEL` is set (to `gemma4:31b-cloud` in this setup) and that model is pulled.
- **`gemma4:31b-cloud` errors at startup** — pull it the same way as the primary model: `ollama pull gemma4:31b-cloud`.
- **`ollama launch claude` not recognized** — your Ollama is older than the version that added the launcher; use Method A or C, or update Ollama.
- **Cloud model pulls but errors at run time** — run `ollama signin` again to refresh your session; cloud models require a signed-in account.
- **Connection refused on `localhost:11434`** — Ollama is not running (`ollama serve`), or it has been remapped to a different port; adjust `ANTHROPIC_BASE_URL` to match.
- **A model tag in this guide fails to pull** — the tag has moved. Find the current one per §3.1 and substitute it.
- **`ollama search` is not a command** — there is no CLI search; browse <https://ollama.com/search?c=cloud> (§3.1).

Windows / PowerShell:

- **`The term 'ANTHROPIC_BASE_URL=http://localhost:11434' is not recognized`** — you ran Method A's bash syntax in PowerShell. Use §6.6.
- **`running scripts is disabled on this system`** — execution policy blocks the installer; run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and retry (§6.5).
- **`ollama` or `claude` not recognized right after installing** — `PATH` is stale; close and reopen the terminal (§6.2).
- **`curl -s https://...` fails with "A parameter cannot be found that matches parameter name 's'"** — `curl` is an alias for `Invoke-WebRequest` in Windows PowerShell 5.1. Use `irm` (§6.4).
- **`Only one usage of each socket address ... is normally permitted`** — Ollama's tray service already owns port 11434. Do not run `ollama serve` on Windows.
- **Settings changes have no effect** — you likely set the variables in both `settings.json` and the user environment; §6.7 says pick one. Run `claude doctor` to check the settings file parses.

---

## Sources

- Ollama Cloud — <https://docs.ollama.com/cloud>
- Ollama cloud model catalogue — <https://ollama.com/search?c=cloud>
- Ollama + Claude Code integration — <https://docs.ollama.com/integrations/claude-code>
- Claude Code environment variables — <https://code.claude.com/docs/en/env-vars.md>
- Claude Code setup, incl. Windows — <https://code.claude.com/docs/en/setup>
