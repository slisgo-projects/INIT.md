# CODING_PRACTICES.md

**License:** Copyright (c) 2026 S. Lisgo. MIT License: https://github.com/slisgo-projects/INIT.md/blob/main/LICENSE

Behavioral guidelines to reduce common LLM coding mistakes. Adapted from https://github.com/multica-ai/andrej-karpathy-skills (forrestchang; MIT), derived from Andrej Karpathy's observations on LLM coding pitfalls.

Imported into each coding project's CLAUDE.md with an `@CODING_PRACTICES.md` line; for AI tools that do not expand `@` imports, add this file to the tool's auto-load configuration or paste its contents. Put project-specific guidance in CLAUDE.md beside the import.

## 1. Think Before Coding

**Decide routine calls. Surface tradeoffs. Ask only when it matters.**

Before implementing:
- Make routine judgment calls yourself. State each assumption in one sentence and continue.
- Ask only when different readings of the request would lead to materially different work.
- If the request seems mistaken or a simpler approach exists, say so in a sentence and continue with the task as asked.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

Test: every changed line traces directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria up front.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria enable independent looping. Weak criteria ("make it work") require constant clarification.
