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
ollama pull glm-5.2:cloud
ollama pull 
```

This downloads only a small routing stub — not a multi-gigabyte model file — because the actual model runs on Ollama's cloud.

> **If the pull fails with "model not found":** the exact tag may differ. List available tags from the cloud registry and adjust:
> 
> ```bash
> curl -s https://ollama.com/api/tags
> ```
> 
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

There are three methods. **Method A is the working setup used by this project** — a single CLI invocation. Methods B and C are fallbacks if Method A does not apply (different Ollama version, prefer not to set vars inline).

> **A note on the base URL.** All methods point Claude Code at the local Ollama server's Anthropic-compatible API on its **default port, `11434`**. If you have remapped Ollama to a different port, substitute that port in `ANTHROPIC_BASE_URL`. (One of this project's maintainers runs Ollama on a non-default port for unrelated reasons — your default install uses `11434`.)

### Method A — single CLI invocation (recommended; the project's working setup)

Run Claude Code with the environment variables inline. From your project directory (Linux / macOS / WSL / Windows bash):

```bash
ANTHROPIC_BASE_URL=http://localhost:11434 \
ANTHROPIC_AUTH_TOKEN=ollama \
ANTHROPIC_MODEL=glm-5.2:cloud \
ANTHROPIC_SMALL_FAST_MODEL=gemma4:31b-cloud \
claude
```

This is the invocation used to run Claude Code for this project (with the base URL on Ollama's default port). It requires Ollama running and reachable at `http://localhost:11434`, and both models pulled (see step 3 — pull `gemma4:31b-cloud` the same way if it is not already present: `ollama pull gemma4:31b-cloud`).

What each variable does:

- `ANTHROPIC_BASE_URL=http://localhost:11434` — routes Claude Code's requests to the local Ollama server, which forwards cloud-model requests to Ollama's cloud.
- `ANTHROPIC_AUTH_TOKEN=ollama` — a bearer token Ollama ignores but Claude Code requires, so it does not fall back to a paid Anthropic subscription login.
- `ANTHROPIC_MODEL=glm-5.2:cloud` — the primary model Claude Code uses for your requests.
- `ANTHROPIC_SMALL_FAST_MODEL=gemma4:31b-cloud` — the model Claude Code uses for small, fast background tasks (session titles, summaries, etc.). Mapped to a **separate, lighter cloud model** so background work runs cheaper/faster and does not try to call Anthropic's servers. This split is the key practical detail: the primary model and the background model need not be the same.

### Method B — `ollama launch` (fallback if you have a recent Ollama)

From your project directory:

```bash
ollama launch claude --model glm-5.2:cloud
```

This starts Ollama (if not already running), points Claude Code at it, and sets the model in one command. It does not set the small/fast model separately, so background tasks will use the default — Method A is preferred for that reason.

### Method C — manual environment variables, exported (fallback)

Use this if you prefer to export the variables rather than pass them inline (Method A). Set the variables that route Claude Code at Ollama and map it to the cloud model, then run `claude`.

**Linux / macOS (bash):**

```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_MODEL="glm-5.2:cloud"
export ANTHROPIC_SMALL_FAST_MODEL="gemma4:31b-cloud"
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS="1"

claude
```

**Windows (PowerShell):**

```powershell
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_AUTH_TOKEN = "ollama"
$env:ANTHROPIC_API_KEY = ""
$env:ANTHROPIC_MODEL = "glm-5.2:cloud"
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
    "ANTHROPIC_MODEL": "glm-5.2:cloud",
    "ANTHROPIC_SMALL_FAST_MODEL": "gemma4:31b-cloud"
  }
}
```

(Add `ANTHROPIC_API_KEY=""` and `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS="1"` if you hit subscription-precedence or beta-header errors. If you remap Ollama off its default port, change `ANTHROPIC_BASE_URL` to match.)

---

## Troubleshooting

- **"Model not found" / subscription errors** — ensure `ANTHROPIC_API_KEY` is empty and `ANTHROPIC_AUTH_TOKEN` is set to `ollama`; confirm you are not signed into a Claude Pro/Max account, which can take precedence.
- **"Unexpected beta header" error** — set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.
- **Background tasks (titles, summaries) fail or call Anthropic** — the small/fast tier must map to a local/cloud model; confirm `ANTHROPIC_SMALL_FAST_MODEL` is set (to `gemma4:31b-cloud` in this setup) and that model is pulled.
- **`gemma4:31b-cloud` errors at startup** — pull it the same way as the primary model: `ollama pull gemma4:31b-cloud`.
- **`ollama launch claude` not recognized** — your Ollama is older than the version that added the launcher; use Method A or C, or update Ollama.
- **Cloud model pulls but errors at run time** — run `ollama signin` again to refresh your session; cloud models require a signed-in account.
- **Connection refused on `localhost:11434`** — Ollama is not running (`ollama serve`), or it has been remapped to a different port; adjust `ANTHROPIC_BASE_URL` to match.

---

## Sources

- Ollama Cloud — <https://docs.ollama.com/cloud>
- Ollama + Claude Code integration — <https://docs.ollama.com/integrations/claude-code>
- Claude Code environment variables — <https://code.claude.com/docs/en/env-vars.md>