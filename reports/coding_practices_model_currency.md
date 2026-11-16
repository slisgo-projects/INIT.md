# CODING_PRACTICES.md and Model-Generation Currency

**Date:** 2026-11-16
**Status:** current
**Baseline:** INIT.md version 2026-11-09; CODING_PRACTICES.md as of commit f7b9e05.
**Provenance:** Anthropic documentation and the interview transcript were read in full; quoted passages were checked against the local copies in §"References". Third-party studies and commentary are search summaries only. Mappings to INIT.md and CODING_PRACTICES.md, and every verdict, are AI judgment. No directive has been probed on a current model in this project; nothing here is a measured result.

## Disposition

- DECISIONS.md, 2026-11-16: logged `open`. No edit to CODING_PRACTICES.md or INIT.md yet.

## Question

- Are the directives in CODING_PRACTICES.md obsolete, redundant or counterproductive for current models (Claude 5 generation)?
- Trigger: an interview with Anthropic's engineering lead for Claude says skills and instructions written for earlier models go stale fast.
- Secondary: does the same guidance bear on INIT.md's own rules?

## Findings

### 1. Interview: "Stop Using Claude Like It's 2024"

YouTube `D-SVFneJ_Nk`, interviewee introduced as engineering lead for Claude at Anthropic. Auto-captions spell the name "Felix Riesberg"; probably Rieseberg (unverified). Line numbers refer to the local transcript.

- **Skills go stale.** "our official Anthropic guidance, as well as my personal guidance, is be really careful with skills"; "the half-life of a good skill is very short"; "if you completely remove the skill, you actually get better output" (l. 137–138). Removal is judged against an eval (l. 140). The "official guidance" claim is the speaker's; see §2 for what the docs say.
- **Self-judgment unreliable.** "I really want the current session to judge itself. That I think is still really iffy" (l. 168). Preference order: hard outside evidence, then another session (l. 170).
- **Adversarial review.** Spawn several sessions tasked to prove the work wrong (l. 83–84, 90–91); a separate "judge" session validates the criticisms (l. 94–97); the authoring session decides whether to act (l. 97–98). Reviewers can run "a step down in intelligence" (l. 86–87).
- **Grade the method, not the answer.** A correct guess at the temperature "should not be a passing grade"; a slightly-off answer from reputable sources should score higher (l. 50–53).
- **Single-agent fact-checking trusted** when every number must trace to a verified primary source (l. 109–111).
- **No personas.** "You're an excellent [X]" was "very in vogue sort of like 2024" (l. 159–160); role prompts produce "role play" (l. 163). Ask instead for the tools and techniques a top practitioner would use (l. 161–164). Organise by work item, not role (l. 158).
- **Full access over pre-sliced data.** "Model experience": give raw data and well-documented tools (l. 141–143, 124–126); "I don't really make this a priori decision anymore on what kind of data do you need" (l. 135–136).
- **Feedback to principles.** Gather all feedback given; condense to rules; a further pass for principles held but unstated; use as review input (l. 181–184). Build trust by running AI review side by side with your own (l. 189–194).
- **Advice decays.** "all the advice I've given you today in about 10 weeks, we're probably going to have a new revision on all of it" (l. 307).

### 2. Anthropic prompting documentation

Retrieved 2026-11-16. Covers Fable 5.2, Opus 5.5, Opus 5, earlier.

- **Verification instructions — remove (Opus 5).** "Claude Opus 5 verifies its own work without being told to. If your prompt contains explicit verification instructions … remove them: instructions like these cause over-verification on Claude Opus 5, and removing them reduces wasted tokens with no loss in quality" (Opus 5 guide, §"Task scope and over-verification"). Also: "Avoid instructing re-checks it already performs" (§"Self-correction"). The best-practices page repeats this as the exception to its "Ask Claude to self-check" advice (§"Leverage thinking and interleaved thinking capabilities").
- **Opus 5 patterns carry to Opus 5.5.** "Existing Claude Opus 5 prompts should perform well without changes, and the patterns in Prompting Claude Opus 5 remain a reasonable starting point" (Opus 5.5 guide, intro).
- **Clarification threshold raised (Opus 5).** Suggested scope prompt: "Make routine judgment calls yourself, and check in only when different readings of the request would lead to materially different work. If the request seems mistaken or a better approach exists, say so in a sentence and continue with the task as asked" (Opus 5 guide, §"Task scope and over-verification").
- **Scope expansion persists (Opus 5).** "Claude Opus 5 can also expand the scope of a task, adding steps that weren't requested" — constrain explicitly for narrow tasks (same section).
- **Overengineering guidance — conditional, Opus 4.5/4.6.** "Claude Opus 4.5 and Claude Opus 4.6 have a tendency to overengineer … If you're seeing this undesired behavior, add specific guidance". The sample prompt (scope, documentation, defensive coding, abstractions) closely matches CODING_PRACTICES.md §2–§3 (best practices, §"Overeagerness").
- **Emphatic wording overtriggers (4.5+).** Replace "CRITICAL: You MUST use this tool when…" with "Use this tool when…" (best practices, §"Tool usage"). "Remove over-prompting" (same page, §"Overthinking and excessive thoroughness").
- **Thinking prompts — remove (Opus 5.5).** "Delete 'think hard' and 'think carefully.'… removing those lines made replies start sooner, with no clear drop in quality" (Anthropic article, "Using Claude Opus 5.5 as your daily driver", tips list). Same in Opus 5.5 guide, §"Thinking instructions in chat system prompts".
- **Accumulated caution (Fable 5.2).** "Cautious instructions can build up from past sessions through memory, notes, and instruction files … counterproductive when Claude Fable 5.2 follows the instructions closely and asks for unnecessary approval" (Fable 5.2 guide, §"Keep caution from piling up"). Remedies: name steps needing no approval; remove or narrow stopping conditions such as "stop and review at the first error"; "The model treats an instruction that contains 'never' as absolute" (same section).
- **Rules need scope and reason (Fable 5.2).** "delete cautions whose reason no longer holds, and rewrite absolute rules with their scope and reason" (Fable 5.2 guide, §"Review prompts and harnesses designed for earlier models", item "Rules, notes, and memories that have built up").
- **Writing-style rules over-followed (Fable 5.2).** "a hard limit such as 'one instruction per sentence, in 20 words or fewer' can make its prose choppy. Remove the rules you no longer need" (same section, item "Style rules for writing").

### 3. Third-party evidence (search summaries only)

- **ETH Zurich, Feb 2026** (Gloaguen et al., "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"): on SWE-bench Lite and a 138-task benchmark, Claude Code was the only agent where developer-written context files did not beat no file; commentary reports about −3% success.
- **288-run ablation, Jul 2026** (Developers Digest): context-file injection strategy did not measurably change correctness on Claude Code or Codex; a summary reports runtime −29%, tokens −17%.
- **Claude Code system prompt cut >80% for Claude 5 models** with no measurable eval loss (Developers Digest blog). Not found in an Anthropic primary source.
- **Karpathy-derived file specifically:** viral claim of mistake rate 41% → 11% (no file → 4 rules); unverified, model unstated. One review notes the upstream repo's last commit was April 2026, before Claude 5. No test of the file on Opus 5 / 5.5 / Fable 5.x found.
- **Practitioner tooling:** `evolsb/claude-instruction-ablation` reports one cleanup cut 63,572 → 18,200 instruction words across repos; argues stale instructions become "confident, specific, wrong".

### 4. Directive-by-directive assessment

Row IDs from `reports/schema_redundancy_ablation.md` §"Directive inventory". Verdicts are priors for probing, not results.

| CODING_PRACTICES.md | Rows | Current-model guidance | Prior |
|---|---|---|---|
| Header: "bias toward caution over speed" | — | Fable 5.2: accumulated caution causes unnecessary approval-seeking | Counterproductive on Fable 5.2; untested elsewhere |
| §1 "If something is unclear, stop, name what's confusing, and ask" | C01, C04 | Opus 5: decide routine calls; ask only when readings lead to materially different work | Threshold too low; likely counterproductive in unattended runs |
| §1 "present [interpretations] — don't pick silently" | C02 | Same; Opus 5 says flag in a sentence and continue | Partly redundant |
| §1 "If a simpler approach exists, say so. Push back when warranted." | C03 | Matches Opus 5 scope prompt | Current; possibly redundant |
| §2 No speculative features, abstractions, configurability, error handling | C05, C06 | Anthropic sample prompt, conditional on observed overengineering (Opus 4.5/4.6); Opus 5 still expands scope | Current but conditional |
| §3 Surgical changes; match style; mention dead code; remove own orphans | C07–C09 | Same sample prompt (scope, documentation) | Current but conditional |
| §4 "Loop until verified"; "Ensure tests pass before and after" | C10, C11 | Opus 5: remove explicit verification instructions; cause over-verification | Counterproductive on Opus 5 / 5.5 |
| §4 "Write a test that reproduces it, then make it pass" | C10 | Not addressed: a method, not a re-check | Unknown |

### 5. Bearing on INIT.md itself

- **No embedded rationale** (INIT.md §"Writing Style", "No embedded rationale") conflicts with Fable 5.2's "rewrite absolute rules with their scope and reason". Inference: rationale moved to DECISIONS.md is not in context when the rule is applied, so absolute rules lose their scope.
- **Absolute prohibitions.** INIT.md and CODING_PRACTICES.md use many "Do not" / "Don't" rules; Fable 5.2 treats "never"-type rules as absolute.
- **Terse style rules** (bullets, one concept per bullet, no filler) resemble the Fable 5.2 "style rules for writing" example; that example concerns the model's prose output, not files it writes to a schema. Bearing uncertain.
- **§"Skills"** mandates capture with no review or retirement rule; the interview says skill half-life is short. INIT.md skills are procedural (commands, failure modes), which the interview's warning fits less well than behavioral instructions.
- **Corroborated:** checkpoint reviews in a non-authoring context (§"Inconsistency Handling"); "Checks must be independent" and source locators (§"Findings and Checks", §"Report Files"); per-work-area `handover/` files; the "Schema longevity is an experiment" guidepost (VISION.md).
- **Tension, not contradiction:** §"Context Refresh" selects files up front; the interview favours full access with documented tools. The CLAUDE.md hierarchy stub already works as such an index.

## Implications

- **Probe before editing.** Per INIT.md §"Findings and Checks", these are `open` priors. The redundancy study's queued rows C01, C02, C07, C08, C10 (priority 22–26) are the vehicle.
- **Widen the study's outcome measure.** The study asks whether a directive is followed unprompted. Anthropic's guidance says some directives degrade output (over-verification, approval-seeking, tokens). Add a cost/side-effect measure (tokens, redundant re-checks, unnecessary questions) to the C-row probes.
- **Model-specific scope.** Guidance differs by model: verification removal is Opus 5-line; caution and rules-with-reasons are Fable 5.2. The study also runs GLM-5.3-flash, which has no equivalent vendor guidance. A directive may be harmful on one model and needed on another; CODING_PRACTICES.md is imported unconditionally.
- **Candidate edits, pending probes and operator decision:**
  - §4: drop "Loop until verified" and verification wording; keep test-first reproduction if probes show value.
  - §1: raise the ask threshold to "materially different work".
  - Header: drop or narrow "bias toward caution over speed".
  - §2–§3: mark conditional, or keep as-is.
  - INIT.md §"Skills" and §"Inconsistency Handling": add skills and imported behavioral files to the checkpoint "what can be removed" question.
  - INIT.md §"Writing Style": revisit "No embedded rationale" for absolute rules (scope clause inline).
  - INIT.md §"Inconsistency Handling": optional adversarial-review pattern (attackers → judge → author decides).

## References

Local copies are in `reference/` and are not committed.

- Rieseberg, F. (name per auto-captions "Riesberg"; unverified), interview, "Claude Engineering Lead: 'Stop Using Claude Like It's 2024'", YouTube, accessed 2026-11-16. https://www.youtube.com/watch?v=D-SVFneJ_Nk. Local: `reference/youtube_D-SVFneJ_Nk_transcript_2026-11-16.txt` (auto-captions, folded at 200 chars). Read in full.
- Anthropic. "Prompting best practices." Claude Platform Docs, retrieved 2026-11-16. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices. Local: `reference/anthropic_docs_claude-prompting-best-practices_2026-11-16.html`. Searched for relevant sections; those sections read in full.
- Anthropic. "Prompting Claude Opus 5." Claude Platform Docs, retrieved 2026-11-16. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5. Local: `reference/anthropic_docs_prompting-claude-opus-5_2026-11-16.html`. Read in full.
- Anthropic. "Prompting Claude Opus 5.5." Claude Platform Docs, retrieved 2026-11-16. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5. Local: `reference/anthropic_docs_prompting-claude-opus-5-5_2026-11-16.html`. Read in full.
- Anthropic. "Prompting Claude Fable 5.2." Claude Platform Docs, retrieved 2026-11-16. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2. Local: `reference/anthropic_docs_prompting-claude-fable-5-2_2026-11-16.html`. Sections "Keep caution from piling up" and "Review prompts and harnesses designed for earlier models" read in full; rest not read.
- Anthropic. "Using Claude Opus 5.5 as your daily driver for knowledge work." claude.com, undated, retrieved 2026-11-16. https://claude.com/resources/articles/using-claude-opus-5-5-as-your-daily-driver-for-knowledge-work. Local: `reference/anthropic_opus55_daily_driver.html`. Tips section read.
- The Decoder. "Anthropic says outdated prompting habits are slowing down Claude Opus 5.5." 2026-11-14. https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/. Local: `reference/decoder_opus55_prompting_2026-11-14.html`. Fetch-tool summary; used only to locate the Anthropic article.
- Gloaguen et al. "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" ETH Zurich, Feb 2026. Seen via https://todatabeyond.substack.com/p/do-agentsmdclaudemd-files-help-coding and https://medium.com/@reliabledataengineering/claude-md-dont-work-eth-zurich-study-shows-context-files-reduce-success-rates-by-3-1518cac80929. Search summaries only; paper not read.
- Developers Digest. "AGENTS.md Files Don't Move Coding Agent Correctness: A 288-Run Ablation." Jul 2026. https://www.developersdigest.tech/blog/context-files-coding-agents-ablation-2026. Search summary only.
- Generative Labs. "CLAUDE.md Files Make Coding Agents Cheaper, Not More Correct." https://www.generativelabs.com/insights/claude-md-agents-md-context-files. Search summary only.
- Developers Digest. "The New Rules of Context Engineering for Claude 5 Models." 2026. https://www.developersdigest.tech/blog/context-engineering-claude-5-new-rules-2026. Search summary only (source of the ">80% system prompt cut" claim).
- Better Stack. "How to Prompt Claude Opus 5.5: What Changed and What to Remove." https://betterstack.com/community/guides/ai/claude-opus-55-prompting-guide/. Search summary only.
- multica-ai / forrestchang. `andrej-karpathy-skills` repository. https://github.com/multica-ai/andrej-karpathy-skills. Search summary only.
- AI Parabellum. "Karpathy CLAUDE.md Guidelines: Do They Improve Claude Code? We Tested Them." https://aiparabellum.com/karpathy-claude-md-guidelines-tested/. Search summary only (source of the April 2026 last-commit note).
- Developers Digest. "Karpathy CLAUDE.md Skills: Use the Viral Rules as a Menu, Not a Template." https://www.developersdigest.tech/blog/karpathy-claude-md-skills-menu. Search summary only.
- Mnilax. "Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%." X article. https://x.com/Mnilax/article/2053116311132155938. Search summary only.
- TechTimes. "Karpathy CLAUDE.md Grows to Ten Rules." 2026-06-28. https://www.techtimes.com/articles/319214/20260628/karpathy-claudemd-grows-ten-rules-new-self-check-protocol-ai-coding-loops.htm. Search summary only.
- evolsb. `claude-instruction-ablation` repository. https://github.com/evolsb/claude-instruction-ablation. Search summary only.
