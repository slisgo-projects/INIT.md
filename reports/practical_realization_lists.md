# Useful and Potentially Relevant Lists

**Date:** 2026-11-02 (disposition added 2026-11-03)
**Status:** current
**Baseline:** INIT.md version 2026-11-01; USE_CASE_INIT.md and CODING_PRACTICES.md as of this date.
**Provenance:** item text checked against the sources in §"References", at the depth recorded per source. Mappings and impact ratings are AI judgment, not measured results. No candidate directive has been tried on a project.

## Disposition

Operator decisions, 2026-11-03 (DECISIONS.md). These override the original recommendation and ratings below.

- **D3:** adopted in reduced form, as one line in INIT.md §"Inconsistency Handling" checkpoint reviews. The five-step sequence was not adopted. Impact for the operator's minimalist projects: Low to Medium, not High.
- **D1:** declined. The operator does not tend to make feasibility claims.
- **D2:** declined. The report treated a complete flowdown as a risk and missed bookending, a deliberate schema feature (MOTIVATION.md §"Bookending development from both ends"). Findings and item tables that describe this as a gap are retained as originally written.
- **D4–D12:** not pursued.

## Question

- Which practitioner lists on turning ideas into working systems hold wisdom INIT.md lacks?
- Per list item: where does INIT.md already represent it, and how meaningful would a new directive be?

## Findings

- 109 items reviewed across 8 lists: 22 Covered, 33 Partial, 28 Not represented, 26 N/A.
- **Largest gap: contact with reality.** INIT.md polices negative findings, checks, and status records. It does not police optimistic feasibility claims or require early real-world contact.
- **Second gap: removal.** INIT.md governs how content is added, moved, archived, and superseded. It has no directive to question or remove requirements, phases, or records before optimizing them.
- **Heilmeier is mostly represented.** 5 of 8 questions are covered; the other 3 are partial.
- **Rickover's practical traits are symptoms, not goals.** Used as criteria, they would reward cost, delay, and bloat. Use only the academic traits, as warning signs.
- **Maturity levels do not fill the gap.** USE_CASE_INIT.md §"Maturity Levels" tracks specification and commitment progress (Draft, Scoped, Validated, Active), not demonstrated performance.
- **The schema is exposed to the same test.** This repo skips VALIDATION.md and IMPLEMENTATION.md, and "project-type-agnostic" resembles Rickover's "very flexible in purpose." Downstream use is its evidence, not internal consistency.

## Rating key

**Coverage**

- Covered — INIT.md or a companion file already directs this.
- Partial — related content exists; the item's main point is missing or limited in scope.
- **NOT REPRESENTED** — applicable, with no directive in the schema.
- N/A — domain-specific, organizational, humorous, purely diagnostic, or not actionable for a team of one.

**Impact of a new directive** (Partial and NOT REPRESENTED only)

- High — changes session behavior on most projects and catches a failure the schema currently misses.
- Medium — real value, but only on some projects or partly overlapping an existing rule.
- Low — marginal, narrow, or not worth its length.

## Candidate directives

| ID | Directive (draft text) | INIT.md location | Sources | Impact |
|---|---|---|---|---|
| D1 | **Feasibility claims require contact.** Until demonstrated by a working prototype, measurement, or real use, record claims that something is simple, cheap, fast, off-the-shelf, or needs little development as assumptions, not facts. | §"Findings and Checks" | Rickover, TRL | High |
| D2 | **Early contact.** The first phase exercises the highest-risk or least-proven element against reality, at the smallest useful scope, on the path to the actual goal. Flowdown completeness is not evidence of progress. | §"IMPLEMENTATION.md" | Rickover, Johnson, Akin | High |
| D3 | **Delete before optimizing.** Before refining, accelerating, or automating a requirement, phase, or recurring record, ask whether it can be removed. Order: question, delete, simplify, accelerate, automate. Record removals per the owning file's archive rule. | §"File Updates" or new workflow section | Musk, Akin, Johnson | High |
| D4 | **Requirement provenance.** Each requirement names its source: user statement, external constraint, or AI inference. Question AI-inferred requirements first. | §"USE_CASES.md", §"VALIDATION.md" | Musk, Akin | Medium |
| D5 | **Decision on failure.** Where failure would put the project in question, the phase entry states what result triggers a stop, pivot, or re-scope. | §"IMPLEMENTATION.md" | Heilmeier | Medium |
| D6 | **Disconfirming evidence.** Topic reports state what would undermine each main finding, and report failed attempts and unfavorable results. | §"Report Files" | Feynman, Akin | Medium |
| D7 | **State of practice.** INSPIRATIONS.md states how the problem is solved today and the limits of those solutions. Each MOTIVATION.md strand states what is new relative to current practice. | §"INSPIRATIONS.md", §"MOTIVATION.md" | Heilmeier, Akin | Medium |
| D8 | **Quantified estimates.** State risks and feasibility claims with numbers where they can be estimated. Mark each as estimated or measured; replace estimates when measurements arrive. | §"Findings and Checks" | Akin | Medium |
| D9 | **Projection to completion.** State-of-progress includes projected remaining time and cost (tokens, money), and compares actuals with the original estimate. | §"IMPLEMENTATION.md" | Johnson, Akin | Medium |
| D10 | **Premortem.** When first drafting project risks, assume the project has failed and list why. Run it in a context that did not write the plan. | §"ARCHITECTURE.md" or §"CONSTRAINTS.md" | Klein | Medium |
| D11 | **Evidence level.** Each ARCHITECTURE.md element records its strongest evidence: concept, tested in isolation, tested in a relevant environment, or in real use. | §"ARCHITECTURE.md" | TRL, Rickover | Medium |
| D12 | **Non-compliance register.** List requirements that will knowingly not be met, with reasons. | §"VALIDATION.md" | Johnson | Low |

## Original recommendation (2026-11-02; see §"Disposition")

- Adopt D1, D2, and D3 first. They address the two largest gaps and cost a few lines.
- Consider D6 and D5 next.
- Do not adopt all twelve. Doing so would conflict with the concision guidepost and with D3.
- Merge D11 into D1 if D1 proves too coarse; do not add both by default.
- Trial new directives on one downstream project and log the outcome in DECISIONS.md. Under D1, their expected value here is itself an untested claim.

## Item mapping

### Heilmeier Catechism

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| H1 | What are you trying to do, with no jargon? | VISION.md north star, objectives, "simple language" | Covered | — | — |
| H2 | How is it done today; what are the limits of current practice? | INSPIRATIONS.md borrow / avoid; limits not required | Partial | D7 | Medium |
| H3 | What is new, and why will it succeed? | MOTIVATION.md "why the approach is positioned"; "what is new" not required | Partial | D7 | Medium |
| H4 | Who cares; what difference will success make? | MOTIVATION.md, USE_CASES.md | Covered | — | — |
| H5 | What are the risks? | ARCHITECTURE.md, CONSTRAINTS.md, INTERFACES.md risks | Covered | — | — |
| H6 | How much will it cost? | CONSTRAINTS.md budget; IMPLEMENTATION.md estimates | Covered | — | — |
| H7 | How long will it take? | CONSTRAINTS.md deadlines; IMPLEMENTATION.md estimates | Covered | — | — |
| H8 | What are the mid-term and final "exams"? | VALIDATION.md, IMPLEMENTATION.md verification; consequence of failure absent | Partial | D5 | Medium |

### Rickover "Paper Reactor" memo

Academic traits, read as warning signs when claimed without evidence:

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| RA1 | It is simple | None for positive claims | **NOT REPRESENTED** | D1 | High |
| RA2 | It is small | None for positive claims | **NOT REPRESENTED** | D1 | Medium |
| RA3 | It is cheap | Estimates exist; not treated as assumptions | **NOT REPRESENTED** | D1 | High |
| RA4 | It is light | None for positive claims | **NOT REPRESENTED** | D1 | Low |
| RA5 | It can be built very quickly | Estimates exist; not treated as assumptions | **NOT REPRESENTED** | D1 | High |
| RA6 | Very flexible in purpose ("omnibus reactor") | USE_CASES.md forces specific uses; no warning on generality claims | Partial | D1 | Medium |
| RA7 | Very little development; mostly off-the-shelf | None | **NOT REPRESENTED** | D1 | High |
| RA8 | In the study phase; not being built now | Entry Protocol permits a full paper flowdown first | **NOT REPRESENTED** | D2 | High |

Practical traits, diagnostic only:

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| RP1 | It is being built now | Implied by IMPLEMENTATION.md; timing not required | **NOT REPRESENTED** | D2 | High |
| RP2 | It is behind schedule | Symptom; not a criterion | N/A | — | — |
| RP3 | Immense development on apparently trivial items | No directive to expect or surface these | **NOT REPRESENTED** | D1, D2 | High |
| RP4 | Corrosion, in particular, is a problem | Domain-specific | N/A | — | — |
| RP5 | It is very expensive | Symptom; not a criterion | N/A | — | — |
| RP6 | Long build time from engineering development problems | Symptom; not a criterion | N/A | — | — |
| RP7 | It is large | Symptom; not a criterion | N/A | — | — |
| RP8 | It is heavy | Symptom; not a criterion | N/A | — | — |
| RP9 | It is complicated | Symptom; not a criterion | N/A | — | — |

### Kelly Johnson's 14 rules (Skunk Works)

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| J1 | Manager has near-complete program control | Inherent in team-of-one (VISION.md) | Covered | — | — |
| J2 | Strong, small project offices on both sides | Multi-organization structure | N/A | — | — |
| J3 | Restrict people connected to the project; use few, good ones | Team-of-one covers humans; no limit on agents | **NOT REPRESENTED** | — | Low |
| J4 | Simple drawing release system, flexible for changes | Markdown files; §"File Updates"; §"Versioning" | Covered | — | — |
| J5 | Minimum reports, but record important work thoroughly | Concision guidepost, drain rule, DECISIONS.md; no test of whether a record earns its upkeep | Partial | D3 | Medium |
| J6 | Monthly cost review, including projected cost to completion | Estimates and ceilings; no projection | **NOT REPRESENTED** | D9 | Medium |
| J7 | Contractor responsible for good vendor bids | Procurement practice; CONSTRAINTS.md tracks vendor risk only | N/A | — | — |
| J8 | Do not duplicate inspection | Fresh-context reviews required; no limit on duplication | **NOT REPRESENTED** | — | Low |
| J9 | Test your own product early, or lose design competence | §"Findings and Checks", VALIDATION.md; early timing absent | Partial | D2 | High |
| J10 | Agree specifications early; state items knowingly not met | VALIDATION.md upstream of implementation; no non-compliance list | Partial | D12 | Low |
| J11 | Timely program funding | CONSTRAINTS.md funding cliffs | Covered | — | — |
| J12 | Mutual trust and daily liaison with the customer | Multi-organization relationship | N/A | — | — |
| J13 | Strictly control outside access | CONSTRAINTS.md cybersecurity; OPERATIONS.md prohibitions | Covered | — | — |
| J14 | Reward by performance, not number supervised | Compensation; no team-of-one analogue | N/A | — | — |

### Musk's five-step process

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| M1 | Make requirements less dumb; each has a named person | CODING_PRACTICES.md "push back"; elicit-before-drafting; VALIDATION.md human-owned; no provenance or questioning step | Partial | D3, D4 | Medium |
| M2 | Delete the part or process step | CODING_PRACTICES.md §2 limits additions; nothing directs removal | **NOT REPRESENTED** | D3 | High |
| M3 | Simplify or optimize, only after steps 1–2 | CODING_PRACTICES.md §2 for code; no ordering; not applied to flowdown | Partial | D3 | Medium |
| M4 | Accelerate cycle time | No ordering rule | **NOT REPRESENTED** | D3 | Low |
| M5 | Automate last | §"Skills" encourages capture and mechanical enforcement; no ordering | Partial | D3 | Medium |

### Akin's Laws of Spacecraft Design

| # | Item (abridged) | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| A1 | Analysis without numbers is only an opinion | Measurable objectives; estimates "where meaningful"; risks need no numbers | Partial | D8 | Medium |
| A2 | Design to operate when some things are wrong | Domain-level design choice | **NOT REPRESENTED** | — | Low |
| A3 | Design is iterative | "Converging... is iterative" | Covered | — | — |
| A4 | Best efforts end up unused; accept it | Scaffolding superseded state | Covered | — | — |
| A5 | Three points determine a curve | Humor | N/A | — | — |
| A6 | Everything is linear on log-log with a fat marker | Humor | N/A | — | — |
| A7 | Most eager team leader is least capable | Team-of-one | N/A | — | — |
| A8 | Distrust optima at extreme points | Domain heuristic | N/A | — | — |
| A9 | Missing information is no excuse not to start | Open DECISIONS.md entries; no directive to proceed | Partial | D2 | Medium |
| A10 | Estimate or guess, then clean up when real numbers arrive | Status-record checks; no estimate lifecycle | Partial | D8 | Medium |
| A11 | Sometimes restart from scratch | Scaffolding superseded; schema-longevity guidepost; no project-level trigger | Partial | D5 | Low |
| A12 | No single right solution, many wrong ones | DECISIONS.md alternatives | Covered | — | — |
| A13 | Nothing better than requirements dictate | CODING_PRACTICES.md §2 for code | Partial | D3 | Medium |
| A14 | "Better" is the enemy of "good" | CODING_PRACTICES.md §2; §"Stopping Criteria" sets no quality stop | Partial | D3 | Low |
| A15 | Interfaces are where design improves and breaks | INTERFACES.md | Covered | — | — |
| A16 | Do not defer to prior analysis or present it as yours | Report references; INSPIRATIONS.md avoid; no state-of-practice limits | Partial | D7 | Low |
| A17 | Being in print does not make it correct | Status records are claims; references record read depth | Covered | — | — |
| A18 | Too much reality can doom a worthwhile design | Guidepost unrealizable license; moderates D2 | Covered | — | — |
| A19 | You are unlikely to be smarter than the field; suspect surprising results | Findings controls cover negatives and checks, not surprising positives | Partial | D6 | Medium |
| A20 | Presentation can doom a design | Team-of-one; little external audience | N/A | — | — |
| A21 | Half of classroom teaching is wrong | Humor; A17 covers the usable point | N/A | — | — |
| A22 | When in doubt, document | Self-updating rules; DECISIONS.md | Covered | — | — |
| A23 | Schedules are fiction until enforced | Estimates and hard deadlines; no reality comparison | Partial | D9 | Low |
| A24 | Work grows without enforced structure | IMPLEMENTATION.md phases | Covered | — | — |
| A25 | After failure, analysis can be refined to explain it | VALIDATION.md forbids weakening; post-hoc explanation not addressed | Partial | D6 | Medium |
| A26 | Don't do anything dumb | Not actionable | N/A | — | — |
| A27 | Schedules move in only one direction | Estimates are not re-projected | **NOT REPRESENTED** | D9 | Medium |
| A28 | No free launch | CONSTRAINTS.md budget | Covered | — | — |
| A29 | Multiply time by pi and cost by ten | Estimates required; no correction against past overruns | **NOT REPRESENTED** | D9 | Medium |
| A30 | Designs converge on the first concept drawing | Elicit before drafting; do not ghost-write | Covered | — | — |
| A31 | Cannot reach the moon by climbing taller trees | Not addressed; D2 needs this limit | **NOT REPRESENTED** | D2 | Medium |
| A32 | Important visitors miss working demonstrations | Humor | N/A | — | — |
| A33 | Good plan now beats perfect plan next week | "Converging" and one-file-at-a-time; no bias to execution | Partial | D2 | Medium |
| A34 | Do what you can with what you have | Too general to act on | N/A | — | — |
| A35 | Perfection is when nothing is left to remove | "No filler" covers text; not scope | Partial | D3 | High |
| A36 | Elegant < efficient < effective | USE_CASES.md backcasting partly addresses this | Partial | — | Low |
| A37 | Establish clear lines of blame | INTERFACES.md owners; VALIDATION.md human-owned; no general requirement source | Partial | D4 | Low |
| A38 | Capabilities drive requirements | Schema-longevity guidepost; no project-level directive | Partial | — | Low |
| A39 | A program including a new launch vehicle is a launch vehicle program | ARCHITECTURE.md element risks; hidden dominant dependency not named | Partial | — | Low |
| A39a | Alternate: no new launch vehicles | Domain-specific form of A39 | N/A | — | — |
| A40 | Can't make it better until it works | Not addressed for flowdown polish | **NOT REPRESENTED** | D2 | Medium |
| A41 | Always enough time to do it over | Aphorism | N/A | — | — |
| A42 | Flight program: no time; none: no money | Funding environment | N/A | — | — |
| A43 | Understand on third sight or first teaching | `reports/ai_research_inversion.md` notes a possible comprehension step | **NOT REPRESENTED** | — | Low |
| A44 | "Plenty of time" quickly runs out | Aphorism | N/A | — | — |
| A45 | Space is unforgiving; mistakes can kill | Domain-specific; CONSTRAINTS.md holds regulatory limits | N/A | — | — |

### Feynman

Principles extracted by this report; neither source presents them as a numbered list.

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| F1 | You must not fool yourself; you are the easiest person to fool | Status records are claims; fresh-context reviews; controls | Covered | — | — |
| F2 | Bend over backwards to show how you may be wrong | Reports need findings and limits on staleness; no disconfirmation | **NOT REPRESENTED** | D6 | Medium |
| F3 | Report everything that might invalidate an experiment | Report content omits this; negative-finding controls are different | **NOT REPRESENTED** | D6 | Medium |
| F4 | Publish the result whichever way it comes out | Continuity session log records failed attempts; reports do not require this | Partial | D6 | Medium |
| F5 | Reality takes precedence over public relations | Inconsistency Handling; artifact checks; no anti-paper-progress rule | Partial | D1, D2 | High |

### NASA Technology Readiness Levels

| # | Item (abridged) | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| T1 | Basic research translating into R&D | No element evidence scale | **NOT REPRESENTED** | D11 | Medium |
| T2 | Speculative concept; little experimental proof | No element evidence scale | **NOT REPRESENTED** | D1, D11 | Medium |
| T3 | Analytical and lab studies; proof of concept | No element evidence scale | **NOT REPRESENTED** | D11 | Medium |
| T4 | Components tested together | VALIDATION.md integration criteria; not a recorded level | Partial | D11 | Low |
| T5 | Breadboard; rigorous testing in near-realistic simulation | VALIDATION.md criteria; not a recorded level | Partial | D11 | Low |
| T6 | Fully working prototype | No recorded level | Partial | D11 | Low |
| T7 | Prototype demonstrated in the real environment | VALIDATION.md acceptance; not a recorded level | Partial | D11 | Medium |
| T8 | Tested and qualified for integration | VALIDATION.md acceptance | Covered | — | — |
| T9 | Proven in real operation | USE_CASE_INIT.md Active means committed, not proven | **NOT REPRESENTED** | D11 | Medium |

### Klein premortem

Steps extracted by this report from the article's prose; the article does not number them.

| # | Item | INIT.md mapping | Coverage | Directive | Impact |
|---|---|---|---|---|---|
| K1 | Brief the team on the plan | Context refresh and flowdown files | Covered | — | — |
| K2 | Declare that the project has failed spectacularly | Risk fields do not use prospective hindsight | **NOT REPRESENTED** | D10 | Medium |
| K3 | Independently write every reason for failure | Fresh-context reviews are for changes, not plan risks | **NOT REPRESENTED** | D10 | Medium |
| K4 | Share reasons one at a time until all are recorded | Humans-in-a-room mechanic | N/A | — | — |
| K5 | Review the list to strengthen the plan | Risk fields exist; no feedback step | Partial | D10 | Medium |

## Tensions

- **D2 vs. A18, A31.** Early contact can kill worthwhile designs or reward an easy demo that cannot reach the goal. The D2 draft requires contact "on the path to the actual goal"; the phrase needs testing.
- **D2 across project types.** "Reality" must cover a hardware bench test or a pilot conversation with a social project's participants, not only running code.
- **D3 vs. preservation rules.** USE_CASE_INIT.md says "Never delete; archive"; reports and scaffolding persist too. D3 removes items from active scope, not from the record.
- **D3 add-back heuristic.** Not adopted: Musk's "adding back 10%" test has no shown fit outside hardware design.
- **D4 for a team of one.** A named person adds little when the owner is always the same human, so D4 records source type instead.
- **J3 for agents.** Johnson's restriction concerns people. Extending it to agent counts is an analogy, with no evidence here.
- **M1–M5 attribution.** The source is one executive's engineering heuristic for hardware and manufacturing, not a validated method.

## Implications

- Cited from DECISIONS.md (2026-11-03 entries).
- Considered and excluded: Gall's Law and Brooks's "plan to throw one away" (support D2 without a new directive); Amazon PR/FAQ (overlaps USE_CASES.md and Heilmeier); Gawande's *The Checklist Manifesto* (relevant only to the propagation checklist). All from memory; sources not checked.

## References

Local copies are in `reference/` and are not committed.

- DARPA. "The Heilmeier Catechism." Undated page; created by George H. Heilmeier, DARPA director 1975–1977 (tenure from search summary). https://www.darpa.mil/work-with-us/heilmeier-catechism. Local: `reference/darpa_heilmeier_catechism.html`. Questions read in full.
- Rickover, H. G. "Paper Reactor" memo. 1953-06-05. *Journal of Reactor Science and Technology* 3(3), as reproduced by N. Touran, What is Nuclear, 2022-08-23. https://whatisnuclear.com/rickover.html. Local: `reference/rickover_paper_reactor_memo_1953.html`. Memo body read from reproduction; original not seen.
- Johnson, C. L. "Kelly." 14 rules, formalized early 1950s. Libarynth reproduction of a Lockheed Martin page, https://lib.fo.am/skunkworks. Local: `reference/johnson_skunk_works_rules_libarynth.html`. Rules read in full from the reproduction; the Lockheed Martin URL tried returned 404, so wording is not verified against Lockheed Martin.
- Musk, E., interviewed by T. Dodd, *Everyday Astronaut*, as quoted by OODA Loop, 2021-08-13. https://oodaloop.com/analysis/archive/the-everyday-astronaut-elon-musk-and-his-five-step-engineering-process/. No local copy (direct download returned 403). Quoted excerpts only, via fetch tool; interview not watched.
- Isaacson, W. *Elon Musk*. 2023. Search summaries only; book not read. Used only to note that the process is also recounted there.
- Akin, D. "Akin's Laws of Spacecraft Design." Undated. University of Maryland Space Systems Laboratory. https://spacecraft.ssl.umd.edu/akins_laws.html. Local: `reference/akin_laws_spacecraft_design.html`. Read in full.
- Feynman, R. P. "Cargo Cult Science." Caltech commencement address, 1974. https://calteches.library.caltech.edu/51/2/CargoCult.htm. Local: `reference/feynman_cargo_cult_science_1974.html`. Quoted passages only, via fetch tool.
- Feynman, R. P. "Personal Observations on the Reliability of the Shuttle." Rogers Commission Report, Appendix F, 1986. https://www.nasa.gov/history/rogersrep/v2appf.htm. Local: `reference/feynman_appendix_f_1986.html`. Closing passage only.
- NASA. "Technology Readiness Levels." Undated page. https://www.nasa.gov/directorates/somd/space-operations/technology-readiness-levels/. Local: `reference/nasa_technology_readiness_levels.html`. Level definitions read as a fetch-tool summary.
- Klein, G. "Performing a Project Premortem." *Harvard Business Review*, September 2007. Copy at https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf. Local: `reference/klein_project_premortem_2007.pdf`. Read in full.
