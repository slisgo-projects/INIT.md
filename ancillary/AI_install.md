# AI_install.md

Getting started with AI for a new user of this project: install Ollama, set up a free Ollama account, pull the `glm-5.2:cloud` model, install Claude Code, and run Claude Code through Ollama using that model.

This guide uses a **cloud** model (`glm-5.2:cloud`). Cloud models run on Ollama's servers, so you do **not** need a powerful GPU or large amounts of RAM — the local Ollama process proxies your requests to Ollama's cloud. This is the easiest path for a new user. (A fully local model would instead need a 64k+ context window and sufficient local hardware; not covered here.)

**Prerequisite:** a modern web browser (for the one-time Ollama sign-in) and an internet connection.

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
4. Verify in a second terminal:
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

## 3. Pull the `glm-5.2:cloud` model

Pull the cloud model stub so your local Ollama knows how to route requests to the cloud:

```bash
ollama pull glm-5.2:cloud
```

This downloads only a small routing stub — not a multi-gigabyte model file — because the actual model runs on Ollama's cloud.

> **If the pull fails with "model not found":** the exact tag may differ. List available tags from the cloud registry and adjust:
> ```bash
> curl -s https://ollama.com/api/tags
> ```
> Look for a `glm-5.2` entry with a `cloud` tag and use that exact name in place of `glm-5.2:cloud` throughout this guide.

Verify the model is available locally:
```bash
ollama list
```
You should see `glm-5.2:cloud` in the list.

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

## 5. Run Claude Code through Ollama using `glm-5.2:cloud`

There are two methods. **Method A is simplest** if your Ollama version supports it; **Method B** (manual environment variables) always works.

### Method A — `ollama launch` (recommended)

From your project directory:
```bash
ollama launch claude --model glm-5.2:cloud
```
This starts Ollama (if not already running), points Claude Code at it, and sets the model in one command.

### Method B — manual environment variables

Set the variables that route Claude Code at your local Ollama server and map it to the cloud model, then run `claude`.

**Linux / macOS (bash):**
```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_MODEL="glm-5.2:cloud"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-5.2:cloud"
export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-5.2:cloud"
export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-5.2:cloud"
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS="1"

claude
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:ANTHROPIC_API_KEY = ""
$env:ANTHROPIC_MODEL = "glm-5.2:cloud"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "glm-5.2:cloud"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL = "glm-5.2:cloud"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL = "glm-5.2:cloud"
$env:CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS = "1"

claude
```

What each variable does:
- `ANTHROPIC_BASE_URL` — sends Claude Code's requests to your local Ollama server (`http://localhost:11434`) instead of Anthropic's API.
- `ANTHROPIC_AUTH_TOKEN` — a bearer token Ollama ignores but Claude Code requires, so it does not fall back to a paid Anthropic subscription login.
- `ANTHROPIC_API_KEY` — explicitly emptied to avoid "model not found" errors from subscription precedence.
- `ANTHROPIC_MODEL` and the `DEFAULT_*_MODEL` set — map every Claude Code model tier (primary, Haiku for background tasks, Sonnet, Opus) to `glm-5.2:cloud`, so background operations (session titles, summaries) do not try to call Anthropic's servers and fail.
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` — prevents "unexpected beta header" errors when using a non-Anthropic backend.

### Make it permanent (optional)

To avoid setting the variables every session, add them to `~/.claude/settings.json` (Linux) or `%USERPROFILE%\.claude\settings.json` (Windows):

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:11434",
    "ANTHROPIC_AUTH_TOKEN": "ollama",
    "ANTHROPIC_API_KEY": "",
    "ANTHROPIC_MODEL": "glm-5.2:cloud",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5.2:cloud",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2:cloud",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2:cloud",
    "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS": "1"
  }
}
```

---

## Troubleshooting

- **"Model not found" / subscription errors** — ensure `ANTHROPIC_API_KEY` is empty and `ANTHROPIC_AUTH_TOKEN` is set to `ollama`; confirm you are not signed into a Claude Pro/Max account, which can take precedence.
- **"Unexpected beta header" error** — set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` (included above).
- **Background tasks (titles, summaries) fail** — the Haiku tier must map to your model; confirm `ANTHROPIC_DEFAULT_HAIKU_MODEL` is set.
- **`ollama launch claude` not recognized** — your Ollama is older than the version that added the launcher; use Method B, or update Ollama.
- **Cloud model pulls but errors at run time** — run `ollama signin` again to refresh your session; cloud models require a signed-in account.

---

## Sources

- Ollama Cloud — <https://docs.ollama.com/cloud>
- Ollama + Claude Code integration — <https://docs.ollama.com/integrations/claude-code>
- Claude Code environment variables — <https://code.claude.com/docs/en/env-vars.md>