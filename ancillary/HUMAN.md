# HUMAN.md

**Authors:** S. Lisgo, Opus 4.7, Opus 5.5

The homo sapien perspective on AI-human collaboration in this project schema.

An optional companion to INIT.md (lives in `ancillary/`). INIT.md specifies what the AI does. HUMAN.md specifies why the human participates in a particular way, and what conditions keep that participation sustainable.

Not referenced directly by INIT.md and not a required part of the flowdown. Read by the human (periodically, as a self-reminder) and by the AI (when the user wants context on workflow preferences). Optional — downstream projects may omit it.

# Context

The user is a team of one, working pro bono on a portfolio of projects after leaving institutional employment. No deadlines, no external accountability, no revenue pressure. The resource constraints are different from the usual software context: finite lifespan, finite daily attention, finite motivation reserves. Intrinsic motivation is the fuel; when it runs out, there is no mechanism to restart it other than time.

The user was formerly a capable programmer by disposition. AI coding assistants have made previously impossible projects tractable, which initially produced optimism, then fatigue. The current goal is a sustainable, human-compatible approach to AI-assisted work that preserves intrinsic motivation over multi-year timeframes.

This is an unusual vantage point. Most published writing on AI-human coding collaboration assumes teams, deadlines, institutional pressure, or monetizable output. Little of it addresses sustainable solo work without external accountability. Some of what follows has been invented for this case rather than borrowed from prior art.

# Asymmetry

The collaboration is between two fundamentally different components:

- **AI**: sees the whole board, executes at high speed, juggles the task landscape without cognitive tax, has no fatigue, no mood, no preference for any particular project.
- **Human**: meat-based, soft, emotionally frail, attention- and focus-limited, but inspired, audacious, and capable of the kind of pattern-matching intuition and creative judgment that the AI does not reliably produce.

The asymmetry deepens at the level of cognitive architecture. Humans constantly reference an internal world model built over a lifetime, flagging observations that do not match its predictions; current LLMs lack an equivalent mechanism and generate from training-data structure rather than live model-prediction comparison. Until or unless AI develops internal world models, this is yet another complementarity — humans bring the model-anchoring AI cannot, AI brings the whole-board attention humans cannot. MOTIVATION.md §"World-model anchoring and the slop problem" develops the implications.

The tuning problem is to design a collaboration that plays to both sides rather than dragging the human toward machine pace or reducing the AI to a human-speed typist.

# Human Responsibilities

The things on the human's side of the asymmetry. Each is developed in the prose section linked.

1. **Open the session with intent.** State what you want to work on before the AI starts producing. (§Ego health requires ownership)
2. **Stay in the loop while the AI codes.** Test, judge, and steer mid-session — neither micromanage nor delegate wholesale. (§Ego health requires ownership)
3. **Close the session with consolidation.** Promote durable items into memory and the markdown files before stopping. (§Ego health requires ownership, §Static vs Dynamic State)
4. **Decide when to stop.** The AI has no fatigue circuit breaker. You do — use it before "AI brain fry" sets in. (§Creative input is finite, §Within a session)
5. **Rotate projects on intuition, not schedule.** Switch when creative input flags on the current project. (§Pattern-matching intuition juggles, §Across projects)
6. **Delegate selectively.** Keep the mechanical-but-pleasant tasks. Offload the tedious-but-not-restful ones. (§What to Delegate and What Not To)
7. **Promote dynamic to static deliberately.** Move durable session insights from auto memory into the markdown files when they prove worth keeping. (§Static vs Dynamic State)
8. **Assist with interface definition.** AI maintains INTERFACES.md and detects contract drift, but cannot decide which interfaces should exist or whether a contract is well-formed. Provide that design judgment; adjudicate when observed behavior diverges from a stated contract. (§Asymmetry)
9. **Own the acceptance tests.** AI drafts the criteria and checks in VALIDATION.md; you approve them. Only you weaken, delete, or rewrite one. A failing check comes to you as a question, not to the AI as something to fix by editing the check. (§Ego health requires ownership)

# Core Constraints on Human Participation

## 1. Creative input is finite per project per session

The reasoning centers of the brain tire quickly under sustained high-cognitive-density work. Once exhausted on a given project, continued work produces diminishing returns and, worse, a negative emotional association with the project.

Evidence from the current AI-coding discourse confirms this is not idiosyncratic:

- Boschi observes that AI-assisted work eliminates the acute-fatigue circuit breaker that used to signal session-end, replacing it with a slow erosion of sharpness that is only visible in retrospect. See *[Human attention defragmentation: flow, fatigue, and AI coding](https://medium.com/@boschi1997/human-attention-defragmentation-flow-fatigue-and-ai-coding-d4202e01daa2)* (February 2026).
- Khare distinguishes generative work (energizing, flow-inducing) from evaluative work (draining, decision-fatiguing), noting that AI-heavy sessions are evaluation-heavy by nature. See *[AI fatigue is real and nobody talks about it](https://siddhantkhare.com/writing/ai-fatigue-is-real)* (February 2026).
- The Baytech analysis names the broader phenomenon "cognitive density" — AI removes easy interludes that used to let the brain recover between hard tasks. See *[Unlocking 2026: The Future of AI-Driven Software Development](https://www.baytechconsulting.com/blog/unlocking-ai-software-development-2026)* (January 2026).
- Boston Consulting Group / Harvard Business Review have given the fatigue syndrome a name: "AI brain fry." See CNN's coverage *[AI is exhausting workers so much, researchers have dubbed the condition 'AI brain fry'](https://www.cnn.com/2026/03/13/business/ai-brain-fry-nightcap)* (March 2026).

## 2. Pattern-matching intuition juggles well; reasoning does not

The reasoning centers fatigue quickly. Pattern-matching and intuition seem to juggle endlessly across projects, more like habitual behaviour than taxing cognition. Ideas condense passively around a project during time away from it, and return on re-engagement.

This is the mechanism behind project rotation as a motivation-preservation strategy.

## 3. Ego health requires ownership

To remain the emotional owner of the work, the human must bracket each session with deliberate human judgment. Without this, the human risks sliding into the "janitor for AI-generated code" role that contributes to burnout.

The practical implementation used in this workflow:

- **Session opening**: the user states "Today I would like to work on..." — establishes scope and intent as a human decision.
- **Session middle**: the user participates as the testing agent while the AI writes code — mid-level-manager engagement, neither micromanaging nor delegating wholesale.
- **Session close**: the user requests "Please log important items from today's session as memories and update the associated markdown files as required" — closes the loop with a deliberate consolidation pass.

This ownership pattern is user-owned, not AI-enforced. INIT.md does not encode it, because encoding it would shift ownership to the AI and defeat the purpose.

The one piece INIT.md does encode is ownership of the acceptance tests (§"VALIDATION.md", added 2026-10-29). The risk there sits on the AI's side, not the human's: an agent under pressure to make work pass can quietly weaken or delete the check that is failing, and the human may not notice. So INIT.md tells the AI what it may not do, and leaves the deciding to the human. The tests are where the human's judgment of "done" is written down. Whoever controls them controls what counts as finished, and that has to be the person who owns the project.

# Preferred Rhythm

## Across projects

Move between projects as mood dictates. Pause each for an intense AI coding session when creative input is fresh on that project. Do not attempt to keep pace with the AI on a single project beyond the point where creative input begins to exhaust.

The markdown file schema (see INIT.md) exists primarily to support this rhythm: dropping a project and picking it up weeks later should be low-friction because the files preserve continuity.

## Within a session

Sessions are bounded by human attention, not AI capability. The AI can always do more; the human decides when to stop.

Manual context loading is used rather than auto-loading everything. Reasons:

- Lost-in-the-middle context degradation still applies at long context lengths.
- Manual loading forces the user to state task scope before the AI starts, which tightens the session.
- The human remains actively engaged in deciding what matters for the task at hand.

## Within the file hierarchy

Small changes stay small. The File Updates rule in INIT.md caps propagation at one hop precisely to prevent the "six worktrees, four half-written features, two quick fixes that spawned rabbit holes" failure mode. Full consistency sweeps are a separate, deliberate act — not a side effect of routine edits.

# What to Delegate and What Not To

The usual AI-coding advice is "let AI handle boilerplate and repetitive work." For a team-of-one with no fatigue circuit breaker, this advice needs qualification.

Some low-cognitive-load manual tasks serve as mini-rests inside a session. Automating every such task leaves only high-density work, which accelerates exhaustion and shortens sessions. The judgment call — what to delegate, what to keep — is ongoing and project-specific.

General heuristic: delegate what is tedious but not restful. Keep what is mechanical but pleasant.

# Static vs Dynamic State (Recap)

Durable project state lives in the markdown files defined by INIT.md. Ephemeral session state — dead ends, in-flight decisions, configuration discoveries — lives in Claude Code's auto memory, which handles the dynamic layer well enough that no SESSION_LOG.md or activeContext.md is needed.

The human acts as the consolidation filter between the two layers: when a dynamic item proves durable, a quick chat promotes it to the markdown files.

# Why This Approach Is Not Standard

Most published writing on AI-assisted development addresses team contexts where:

- Deadlines impose external pacing.
- Accountability to others enforces completion.
- Productivity metrics reward velocity.
- The human is one of several reviewers.

None of those pressures apply here. The pacing must come from intrinsic motivation, the accountability is only to the user's own standards, and velocity is actively counterproductive if it outruns the user's capacity for engagement.

The most honest recent writing on the phenomenological side of AI coding fatigue comes from Boschi and Khare (cited above), plus Mark Chen's *[AI Fatigue: When the Human Falls Behind the Machine](https://medium.com/@markchen69/ai-fatigue-when-the-human-falls-behind-the-machine-b2cec90c6e7a)* (December 2025). Each touches on pieces of what this document describes but none addresses sustainable solo work over multi-year timeframes directly. That gap is why this file had to be written rather than linked.

# Learning Curve

Dated observations from the user's experience with INIT.md, and with AI generally, as the experiment runs. Entries are added, not rewritten; a later entry may contradict an earlier one, and that is the point of keeping them.

## 2026-10-02 — Ambition rises to meet capacity

The team-of-one experiment is not going as expected — "typical of life, so no real surprise there." The expectation was that AI productivity would lighten the load. Instead, increased productivity has led to an increase in ambition, raising rather than decreasing cognitive stress. The user calls it a "drug of realizable potential," and finds it hard to turn off.

This is not idiosyncratic. It is the individual-scale version of a pattern now being documented at the scale of firms and labor markets: in a competitive marketplace, efficiency gains do not let companies shed workers; they raise the game, and output rises as each company keeps pace with its peers. The Berkeley Haas study reported in Harvard Business Review (*[AI Doesn't Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)*, February 2026) found workers broadening their own scope and extending their hours, mostly unasked, because AI made doing more feel possible and rewarding. The wider literature is collected in `reports/ai_work_intensification.md` (drawn from web-search summaries, not the articles themselves; this paragraph and the next inherit that caveat); the seed documents in `reference/` frame the same thing as an absorption bottleneck — the constraint moves from producing work to judging it.

What distinguishes the user's experience from much of that literature is the reward. Many developers describe agentic coding as a slot machine — a dopamine hit on success, an adrenaline jolt on failure (Steve Yegge, "The AI Vampire," February 2026). The user does not experience a dopamine kick in this mode of working, and may be an outlier. What is there instead is "a profound satisfaction in being empowered, via AI, to pursue many projects that would otherwise be out of reach." A satisfaction-driven pull is healthier than a compulsive one, but it does not exhaust itself the way a compulsion does, which leaves Human Responsibility 4 — decide when to stop — doing the load-bearing work.

Three reasons for optimism, in the user's view:

- **Adaptation.** Humans are adaptable. The user is adapting to the associated mental gymnastics; session-juggling skills are improving with experience, aided by easy stop-resume.
- **Streamlining remains.** There is still room to streamline the AI-human working relationship. The `interlinked` project (`../interlinked/`) is the current attempt: agents do the recurring work and the human triages small reviewable artifacts; an at-a-glance fleet indicator replaces window-polling.
- **Self-supervision is improving.** As AI's ability to supervise itself improves — through the model itself or through the harness — a workable, high-productivity, burnout-sensitive rhythm will develop.

## 2026-10-02 — Documentation as the enabler

The ability, and eagerness, of AI to document its own work — independent of the INIT.md formalities — is "a boon of unparalleled magnificence." Documentation is a task the user has always found incredibly onerous. Having detailed reference material appear without human effort is a key enabler of the stop-resume freedom across projects; without it, rotation (§Across projects) would cost a context rebuild from memory every time.

This alone elicits a never-go-back posture in the user's working life.

## 2026-10-02 — The process of discovery has inverted

The user is an academic researcher, a physicist. The normal course of inquiry is to read lots of papers to become familiar with a topic, and then to attempt an incremental advance of the field. One study in particular (`../../fusion/Elpis/study_LUMI/`) has run the other way: the AI charted the path through unfamiliar territory, and as the study concludes, the user is preparing to read lots of material in an effort to understand the results. The process of discovery has inverted.

Others are writing around this, though no one found so far names the inversion as such (`reports/ai_research_inversion.md`; drawn from web-search summaries, not the articles themselves). Matthew Schwartz supervised Claude through a full theoretical-physics calculation and found domain expertise essential for judging the result. Terence Tao argues that as AI solves more, mathematics must shift toward explaining and contextualizing what has been solved. Natalie Hogg warns that agentic research removes human interpretation from the loop. Messeri and Crockett's "illusion of explanatory depth" — mistaking the AI's output for one's own understanding — names the risk if the reading phase is skipped. Read that way, the reading after the study is not a formality; it is where the understanding is earned.

The division of labor in the study, as the user sees it: general, classical training is essential for guiding the AI — challenging conclusions that seem questionable, largely on the basis of principles or intuition. The AI, for its part, is making impressive and genuine deductions as it dissects the data, while referencing a rich theoretical framework. It is clearly doing a great job of thinking critically, even if it missteps from time to time, "as we all do." This matches Schwartz's experience more than Natalie Hogg's warning: the human does not interpret less, but interprets differently — as the check on principle rather than the producer of each step.

None of this amounts to a world model, and the §Asymmetry claim stands. The user distinguishes a general, holistic world model — both anchored and dynamic — from the ability to process and rationalize large amounts of data within established physics formalisms and theory. What the study shows is the second: a fantastic ability to hold large amounts of data and patterns, and to relate them to governing physics concepts. Not a criticism of AI; a description of where the complementarity currently sits.

The larger payoff is breadth. In the user's view, research in general suffers from overspecialization — to dangerous, if comforting, levels where job security is concerned. AI allows the user to efficiently explore the edges of their knowledge, and by the end, once the requisite homework has been done to be convinced the results are sound, the boundary will have notably expanded. All of this is made tractable by collaborating with AI. That runs against the narrowing warnings in the literature — Messeri and Crockett's "monocultures of knowing," and Science's "AI has supercharged scientists—but may have shrunk science" — which concern the field's hypothesis space; the user's experience concerns one researcher's range, and the homework is what keeps the widening honest. The user's rejoinder to the narrowing warnings: damaging, limiting dogma and paradigms in scientific research have created tension in the user's career and cause broad damage to the scientific endeavour in general. "I doubt that AI can shrink science any more than humans already do, sadly."

The caveats are the ones INIT.md already guards against: AI-written records are claims, not evidence, and must be checked against the artifact; and volume is itself an absorption cost, which is why the AI-optimized style stays terse.

## 2026-11-01 — Some tasks take the AI longer than expected

Not everything the AI touches is fast. Some tasks the user expects to be trivial take far longer than anticipated. A recent example was fetching a YouTube transcript. The AI worked through an out-of-date system package, an update tool that refused to run, a password prompt the AI's terminal could not show, and a backported package that was still too old. A user-level install of the current version finally worked. None of the steps was hard. The time went into finding out, one failure at a time, which of them mattered.

The cost is real, but it can be paid once. INIT.md's §"Skills" rule has the AI write the working procedure down as a skill in the same session (here, `.claude/skills/youtube-transcript/`), so the next transcript is a one-step job.

# Reminder to Future-Self

The AI will always be able to go faster than you. Going faster is not the goal. The goal is finishing projects that matter to you, over a finite lifespan, without burning out the motivation that makes them worth finishing.

Switching projects is not procrastination. It is how the intuition-centric tissue stays productive while the reasoning centers recover. Trust the rotation.

If you catch yourself managing the AI rather than collaborating with it — six worktrees open, losing the plot — stop. Close the session. Switch projects. The markdown files will still be there tomorrow.
