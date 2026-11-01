# AI Research Inversion

**Date:** 2026-10-02
**Status:** current
**Provenance:** findings drawn from web-search tool result summaries (2026-10-02), not from the source pages; no page was opened. Quotes, figures, and claims are second-hand and unverified against originals.

## Question

- Are researchers writing about AI inverting the order of discovery — AI charts the path through unfamiliar territory first; the human reads the literature afterward to understand the results?
- Trigger: operator's experience in `../../fusion/Elpis/study_LUMI/` (laser-actuated dense plasma focus PIC study).

## Findings

- **No source found naming the inversion as such.** Adjacent writing covers its parts: understanding lagging results, and the human role shifting to verification and explanation.
- **Supervised AI research, first-person (physics).** Matthew Schwartz (Harvard, IAIFI), "Vibe Physics: The AI grad student" (Anthropic research blog): supervised Claude Opus 4.5 through a full theoretical calculation without touching files; ~2 weeks vs. ~1 year; 110 drafts, 36M tokens. Claude fast but sloppy; domain expertise essential for evaluation.
- **Understanding as the new bottleneck (mathematics).** Terence Tao, 2026: as AI solves more, the field must shift toward explaining and contextualizing results; warns indiscriminate solution-extraction meets short-term goals "at the cost of sustaining the ecosystem for the next wave of progress." Coverage frames this as "proof indigestion."
- **Interpretation removed from the loop (astrophysics critique).** Natalie B. Hogg, "Agentic research is oxymoronic" (arXiv 2608.31161, 2026-08-31): agentic LLMs obviate human interpretation of results; predicts distrust in the literature.
- **Profession-level purpose question (astrophysics).** David W. Hogg, "Why do we do astrophysics?" (arXiv 2602.10181, 2026-02-10): LLMs beginning to design, execute, write up, referee data-science projects; field must agree on what it is for; rejects both "let-them-cook" and "ban-and-punish."
- **Structural view (physics).** Xiao-Liang Qi, "The Agentification of Scientific Research: A Physicist's Perspective" (arXiv 2604.14718, 2026-04-16): AI moving from tool to collaborator; changes collaboration, publishing, evaluation; continuous learning and idea diversity required for original discovery.
- **Illusion of understanding (framework).** Messeri & Crockett, Nature 627 (2024): illusions of explanatory depth (mistaking AI output for one's own understanding), exploratory breadth (hypothesis space narrows to AI-testable), objectivity; "produce more but understand less."
- **Narrowing at scale.** Science, "AI has supercharged scientists—but may have shrunk science."
- **Code analogue.** "Comprehension debt": code written and code understood are now separate events.

## Implications for the project

- Inversion fits the absorption-bottleneck frame (`reports/ai_work_intensification.md`, `reference/`): production of results is cheap; human understanding of them is the scarce step.
- The post-study reading phase is the comprehension-debt repayment; Messeri & Crockett's explanatory-depth illusion is the failure mode if it is skipped.
- Candidate USE_CASES.md relevance: research use cases (knowledge-deliverable projects) may need a comprehension step after results, not only a literature step before.

## References

URLs as returned by the search tool; pages not fetched (all search summaries).

- https://anthropic.com/research/vibe-physics
- https://academy.openai.com/en/public/blogs/terence-tao-ai-is-ready-for-primetime-in-math-and-theoretical-physics-2026-03-06
- https://www.besthub.dev/articles/terence-tao-25-fields-medalists-warn-ai-math-breakthroughs-cause-proof-indigestion-f0133e851e71
- https://dailymaverick.co.za/article/2026-05-03-crossed-wires-what-does-the-worlds-greatest-living-mathematician-think-of-ai
- https://arxiv.org/pdf/2608.31161
- https://arxiv.org/abs/2602.10181v1
- https://aiweekly.co/alerts/david-hogg-what-astrophysics-is-for-as-llms-enter-the-field
- https://arxiv.org/pdf/2604.14718
- https://ideas.repec.org/a/nat/nature/v627y2024i8002d10.1038_s41586-024-07146-0.html
- https://citp.princeton.edu/news/2024/producing-more-understanding-less-risks-ai-scientific-research
- https://www.science.org/content/article/ai-has-supercharged-scientists-may-have-shrunk-science
- https://www.nature.com/articles/d41586-026-00934-w
- https://dev.to/amit_shrivastava_e813c728/comprehension-debt-what-ai-written-code-actually-costs-2m02
