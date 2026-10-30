# USE_CASE Init Protocol

Universal use-case formulation protocol. Governs every use case specification, formulated inline in `USE_CASES.md` by default. When an individual case grows unwieldy it is extracted to its own `USE_CASE_<identifier>.md` daughter file (see INIT.md §"Stopping Criteria"); the protocol is identical inline or extracted — extraction changes file location, not protocol.

**Goal:** a coherent use case capturing motivation, scope, stakeholders, and the category-specific structure required for that use case's domain — sufficient for stakeholder review, downstream specification, and eventual action.

**Primary reader:** an AI in future sessions. When refreshing context, the user requests `USE_CASES.md` or the relevant extracted `USE_CASE_<identifier>.md` file. Favor structured, explicit content over narrative prose.

**Scope of application:** all use case formulation. Inline is the default home; daughter-file extraction is length-triggered only, per INIT.md §"Stopping Criteria." Do not subdivide unilaterally — wait for user direction.

---

# Entry Protocol

On formulating a use case (new inline in `USE_CASES.md`, or extracting an existing one to its own file):

1. User provides the use case identifier and a description (place, problem, project, application, etc.).
2. AI selects the **primary category** that fits the use case, with a **secondary category** noted when the use case spans more than one. Categories A–F defined in §"Category-Specific Sections" below.
3. AI assigns primary (and secondary) category and records a one-line basis in the header. Proceed without waiting. Pause for user confirmation only when (a) two categories fit comparably, or (b) the assignment would be the first use case in its category. User may override at Charter review.
4. AI creates the use case with a header (identifier, name, status, primary category, secondary category if applicable, category basis, maturity level) and proposes the Charter (Stage 1) for review.

**Header / changelog / maturity placement:** inline in `USE_CASES.md` — per use-case block; extracted to `USE_CASE_<identifier>.md` — per file. Content is otherwise identical.

Advance one stage at a time. Confirm satisfaction before proceeding. Do not generate all stages at once.

**Multi-category handling:** the use case inherits the primary category's structure and pulls specific elements from the secondary category as needed. The hybrid is declared in the header so future sessions know to consult both category sections.

---

# Formulation Stages

Use case construction is staged. Each stage has an entry condition, a deliverable, and a quality gate. Stages are universal; gate criteria adapt by category (see §"Quality Gates").

| Stage | Entry Condition | Deliverable | Quality Gate |
|---|---|---|---|
| 1. Charter | Place, problem, or opportunity identified | One-page charter | Alignment: is this the right problem framed correctly? |
| 2. Foundation | Charter approved | Universal foundational elements + category-specific elements populated | Completeness: do we know who, where, when, why? |
| 3. Inventory | Foundation complete | Category-specific inventory of resources (assets / BoM / dependencies / data sources / source materials, etc.) | Plausibility: are entries credible at appropriate granularity? |
| 4. Analysis | Inventory complete | Cross-cutting frameworks and dependency map | Consistency: do the pieces fit without contradiction? |
| 5. Specification | Analysis complete | Structured data objects for all actions / work items | Quality: does every claim trace to source or explicit assumption? |
| 6. Validation | Specification complete | Domain-appropriate review (stakeholder, peer, expert, beta-reader, user-tester, field-tester) | Credibility: would a knowledgeable reader recognize this as real? |
| 7. Commitment | Validation passed | Final document and action items | Decision: ready to advance to action? |

**Rules of progression:**
- Stages can be traversed iteratively. A failed gate returns to the previous stage.
- Not all use cases need all stages. Skipped stages must be explicitly noted with rationale.

---

# Universal Foundational Elements

Every use case, regardless of category, includes the following. Stage 2 (Foundation) is not complete until these are populated.

## Motivation

Why this use case exists and why this category of intervention is the appropriate response.

- Trigger event, trend, or opportunity.
- Counterfactual: what happens if no action is taken.
- Why this approach over alternatives.

## Goal / Mission / Vision

What success looks like at three resolutions.

- **Vision**: aspirational end state (one sentence).
- **Goal**: measurable target with time bound (one sentence).
- **Mission**: immediate purpose of this document (one sentence).

If these cannot be distinguished, the use case is not yet focused enough.

## Scope

Inside and outside the boundary.

| Dimension | Question | Resolution |
|---|---|---|
| Spatial | Where does this apply? | Geography, deployment locale, system boundary |
| Temporal | What time horizon matters? | Project duration, lifecycle, target dates |
| Populational | Whose lives or systems are affected? | Users, residents, species, codebases, datasets |

State exclusions explicitly and why.

## Stakeholders

Who is affected, who decides, who must be consulted.

| Field | Required | Notes |
|---|---|---|
| Role name | Yes | Functional label |
| Primary concerns | Yes | What they care about most; shapes success-measure selection |
| Secondary concerns | Yes | What they care about less |
| Decision rights | Recommended | Approve, veto, fund, influence |
| Representative | Optional | Named person or organization |
| Engagement status | Optional | Consulted, informed, not yet engaged, resistant |

**Rule:** include at least one stakeholder who would be negatively affected by the most promising action. If every stakeholder benefits from every action, the analysis is incomplete.

## Data Sources and Gaps

Epistemic status for every claim.

| Status | Meaning | Action |
|---|---|---|
| Confirmed | Verified by direct observation or authoritative source | Cite source |
| Estimated | Derived from model, proxy, or analogy | Document method and confidence |
| Assumed | No direct evidence; used to unblock analysis | Flag; describe sensitivity |
| Missing | Needed for decision; not yet available | Describe consequence; propose mitigation |

**Rule:** a use case with more than 20% of foundational fields marked Missing should not advance past Stage 3. Scope the missing information as a pre-implementation deliverable.

---

# Category-Specific Sections

Each category instantiates the universal concepts (inventory of resources, challenges/risks, actions/work items, dependencies, success measures) in domain-appropriate form. Use the section that matches the primary category; pull elements from a secondary section when the use case spans categories.

## A. Software systems

### Inventory
Code modules and dependencies; third-party libraries and services; data sources and APIs; deployment targets; existing user base or workload.

### Challenges / Risks
Technical debt; performance bottlenecks; security exposure; scaling limits; vendor or platform coupling; data-quality issues.

### Actions / Work Items
Features, refactors, integrations, deployments. Each with identifier, name, status, owner, dependencies, target environment.

### Dependency Map
Import or call graphs; data-flow dependencies; deployment ordering; cross-references to INTERFACES.md for service-boundary contracts.

### Success Measures
Performance metrics; uptime / availability; user adoption; code-quality metrics; security audit outcomes.

### Domain-Specific Extensions
API stability checks; security audits; compliance frameworks (SOC2, GDPR, HIPAA, etc., where applicable); accessibility requirements.

## B. Physical and embodied systems

### Inventory
Bill of materials (parts, suppliers, lead times); tools and facilities; firmware and software stack; certifications held or required; engineering knowledge resources.

### Challenges / Risks
Mechanical reliability; thermal and electrical limits; safety hazards; supply-chain risks; environmental operating conditions; manufacturing yield.

### Actions / Work Items
Design iterations; fabrication tasks; integration tests; certification work; field deployment phases. Each with identifier, name, status, owner, prerequisites.

### Dependency Map
Assembly sequence; mechanical and electrical interface contracts (cross-references INTERFACES.md); software-hardware coupling; certification dependencies.

### Success Measures
Performance specifications; reliability metrics (MTBF, MTTR); safety compliance; manufacturing yield; field deployment outcomes.

### Domain-Specific Extensions
Safety analyses (FMEA, FTA, hazard analyses); regulatory compliance frameworks (FCC, CE, FDA, FAA, transport authorities); environmental impact; export-control checks.

## C. Scientific research programs

### Inventory
Data sources (experimental, observational, archival); prior literature; experimental facilities; collaborators and institutions; computing resources; instrumentation.

### Challenges / Risks
Hypothesis testability; data gaps; reproducibility threats; institutional bottlenecks; funding cycles; dual-use concerns.

### Actions / Work Items
Experiments; analyses; publications; conference presentations; collaborative engagements; code or data releases. Each with identifier, name, status, owner, prerequisites.

### Dependency Map
Experimental sequence; data pipeline (collection → processing → analysis → publication); peer-review chain; funding gates; collaborator handoffs.

### Success Measures
Peer-reviewed publications; citation metrics; replication outcomes; data-quality metrics; design-decision impact downstream; community adoption of methods or codes.

### Domain-Specific Extensions
Peer review protocols; data-sharing standards (FAIR, IMAS, OMFIT, domain-specific); ethics / IRB compliance; dual-use review; open-access policies.

## D. Authorship and analytical work

### Inventory
Source materials; references and bibliography; chapter or section outlines; target venue or publisher; author networks; subject-matter consultants.

### Challenges / Risks
Voice consistency; factual rigor; audience mismatch; libel and intellectual-property risk; pacing and length management.

### Actions / Work Items
Drafts; revisions; fact-checks; copy edits; submissions; promotional activities. Each with identifier, name, status, owner, due date.

### Dependency Map
Chapter or section flow; fact-citation chain; beta-reader pipeline; editor handoffs; pre-publication review.

### Success Measures
Word-count milestones; beta-reader feedback quality; publication acceptance; reader engagement (reviews, citations, sales when applicable).

### Domain-Specific Extensions
Fact-checking protocol; copyright and permissions; quotation and excerpting standards; beta-reader process; legal review for critique work.

## E. Civic and community initiatives

### Inventory: Assets

What the community or system already has.

| Capital category | Examples |
|---|---|
| Natural | Forests, watersheds, minerals, biodiversity, scenic value |
| Built | Roads, buildings, power lines, broadband, facilities |
| Human | Skills, education, institutional memory |
| Social | Trust, volunteer networks, cooperative history, Indigenous knowledge |
| Financial | Grants, endowments, revenue, investment capacity |
| Institutional | Tenure rights, regulatory authority, partnerships, political support |

Tag each asset: **confirmed**, **inferred**, or **assumed**.

### Challenges / Risks

What is going wrong or could go wrong.

- Specific, not generic.
- Measurable where possible.
- Explicitly coupled where they interact.
- Ranked by urgency and severity.

Top 2–3 challenges must be traceable directly to success measures (KPIs).

### Actions / Work Items: Initiatives

| Field | Required | Notes |
|---|---|---|
| Identifier | Yes | Stable code (e.g., `ND-01`, `COAST-03`) |
| Name | Yes | Human-readable |
| Category | Yes | Controlled vocabulary |
| Status | Yes | Concept, proposed, approved, in progress, complete, blocked, deferred |
| Champion / Lead | Yes | Person or organization with authority to advance |
| Funding sources | Recommended | Actual or potential |
| Spatial footprint | Recommended | Where it would happen |

Include a status-quo or "do nothing" pseudo-initiative as baseline.

### Dependency Map: Interconnection Graph

How initiatives affect each other.

Examine every initiative against every other for potential relationships. Common types: enables, depends_on, synergy, complements, protects, conflicts_with, overlaps.

**Rule:** if an initiative has zero interconnections, explain why it is isolated or question whether it belongs in this use case.

### Success Measures: KPIs

Each KPI must be:
- Measurable with available or obtainable data.
- Have a current estimate and a target.
- Traceable to at least one initiative impact and one challenge.
- Have a data source and update frequency.

Maximum 5–10 KPIs. Group into composite indices if more are needed.

### Domain-Specific Extensions

Examples: Energy Litmus Test, DRIPA Compliance, FireSmart Funding Eligibility, Fisheries Passage, Fiscal Impact Model, Biodiversity Offset.

**Criteria for adding a module:**
1. It applies to three or more initiatives.
2. It produces a go/no-go or ranked recommendation.
3. It has explicit, externally justifiable thresholds.
4. It includes a monitoring requirement.

**Required structure:**
- Why this framework matters (1–2 sentences).
- Rules / thresholds table.
- Implications per initiative (pass/fail/rank).
- Monitoring requirement.

## F. Personal infrastructure and self-sufficiency

### Inventory
Tools and equipment; materials in stock; knowledge resources (manuals, courses, references); workspaces and storage; time and attention budgets.

### Challenges / Risks
Maintenance burden; skill gaps; climate or seasonal constraints; cost of acquisition; obsolescence of stockpiled tools or knowledge.

### Actions / Work Items
Builds, repairs, learning tasks, system improvements. Each with identifier, name, status, target completion, prerequisite skills or materials.

### Dependency Map
Build sequence; seasonal timing windows; skill prerequisites; tool dependencies; storage capacity.

### Success Measures
Capability targets (e.g., kg of food produced, kWh generated, items cataloged); maintenance frequency; resilience metrics (e.g., autonomy duration during supply disruption).

### Domain-Specific Extensions
Local building codes; agricultural and water regulations; fair-use and copyright for cataloged knowledge; insurance considerations.

---

# Quality Gates

Detailed criteria for each stage gate. A stage is not complete until all checkboxes pass; otherwise return to the prior stage and address the gap. Universal criteria apply to all categories; criteria marked *category-specific* are interpreted using the primary category's instantiation.

### Gate 1: Charter Completeness
- [ ] Motivation linked to a concrete event, trend, or opportunity.
- [ ] Goal is measurable and time-bound.
- [ ] At least one stakeholder with decision rights identified.
- [ ] Scope (spatial, temporal, populational) defined and defensible.
- [ ] Primary category selected; secondary noted if applicable.

### Gate 2: Foundation Completeness
- [ ] Universal foundational elements populated (Motivation, Goal/Vision/Mission, Scope, Stakeholders, Data Sources and Gaps).
- [ ] *Category-specific:* inventory of relevant resources contains at least one entry per category-specific subdivision.
- [ ] *Category-specific:* challenge/risk inventory contains at least two coupled entries.
- [ ] Action/work-item list contains a baseline ("do nothing" or "status quo").
- [ ] Every action has a champion or lead identified.

### Gate 3: Inventory Plausibility
- [ ] *Category-specific:* cost or resource estimates do not exceed identified funding or supply by an order of magnitude without explicit note.
- [ ] *Category-specific:* capacity claims (employment, throughput, deployment volume) do not exceed available capacity without note.
- [ ] Every success measure has a data source, even if estimated via proxy.

### Gate 4: Analysis Consistency
- [ ] Dependency map contains no orphaned actions without explanation.
- [ ] Every "depends_on" link traces to an earlier or higher-priority action.
- [ ] Cross-cutting frameworks produce at least one pass/fail/rank per applicable action.

### Gate 5: Specification Quality
- [ ] Every action has a structured data object.
- [ ] Every data gap has a mitigation or blocking flag.
- [ ] Every assumption is stated and its sensitivity described.
- [ ] All monetary values use the same currency or note conversions.
- [ ] Every success measure names its check and pass/fail signal, or is marked judgment-only; at least one concrete example per measure.

### Gate 6: Validation Credibility
- [ ] *Category-specific reviewer:* at least one local stakeholder (civic), domain expert (research), beta-reader (authorship), user-tester (software), field-tester (hardware), or operator self-check (personal) has reviewed and confirmed top entries are recognizable.
- [ ] Every success-measure current estimate is within an order of magnitude of the reviewer's understanding.
- [ ] No blocking data gap remains unresolved.

### Gate 7: Commitment Readiness
- [ ] Decision-maker can identify the next concrete action (meeting, vote, application, build, write session, deploy).
- [ ] Theory of change links at least one action to each success-measure target.
- [ ] Export document generated and matches session state.

---

# Inconsistency Handling

Per INIT.md §"Inconsistency Handling." Example use-case-level inconsistencies: a challenge not addressed by any action; an action's resource cost exceeding plausible funding.

---

# File Updates

When a stage is started or completed: update the header (current stage, maturity level if it changed), append a changelog entry, and add completion notes to the relevant stage section. Do not wait to be asked. Header, changelog, and maturity stamp are per use-case block when inline in `USE_CASES.md`, per file when extracted (see §"Entry Protocol").

When the user requests a change to an existing element:
- Touch the requested element.
- Propagate logically related updates to other elements to maintain self-consistency.
- Report what was propagated.
- Never delete; archive. Move dropped items to a "Deferred / Archived" section with the reason.

When advancing stages: do not advance until the current stage's quality gate is met.

---

# Context Refresh

When the user asks to re-read a use case, also re-read:
- This file (`USE_CASE_INIT.md`) — to verify current stage and gate criteria.
- The parent `USE_CASES.md` — to confirm the use case's place in the project's use-case set.
- Foundational and cross-cutting files of the project per INIT.md (`VISION.md`, `MOTIVATION.md`, `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`).
- Project-specific framework or exploration files when present (e.g., domain-specific frameworks, interactive-mode protocols).

---

# Stopping Criteria

Per INIT.md §"Stopping Criteria." Sub-subdivided files: `USE_CASE_<identifier>_<cluster>.md` (e.g., `USE_CASE_New_Denver_Energy.md`).

---

# Maturity Levels

Generic four-level scheme:

- **Draft:** actively in formulation; many fields TBD; not for external review.
- **Scoped:** foundational elements complete (Stage 2 passed); ready for inventory work.
- **Validated:** full specification complete and reviewed (Stage 6 passed); ready for action commitment.
- **Active:** action committed and in execution (Stage 7 passed).

Label the document's maturity prominently in the header. Update the level when it changes and append a changelog entry.

Project-specific maturity schemes may extend or replace these; refer to the project's own framework when present.

---

# Flexibility and Exceptions

This protocol is prescriptive but not rigid. Use cases vary across categories.

- **Multi-category use cases** (e.g., a hardware project with significant software components, or a civic initiative requiring custom software): primary category drives the structure; secondary category contributes elements where relevant. Header declares both.
- **AI exploration use cases** may have no human stakeholders, but must define the reward function or evaluation criterion that replaces the stakeholder concerns field.
- **Educational use cases** may invert the order: the action list (lesson modules) drives inventory and challenge selection.
- **Rapid-response use cases** (post-disaster, urgent deadline) may compress all stages into days. Document the compression and its risks.

When deviating:
1. State the deviation explicitly.
2. Explain why the standard element is not applicable.
3. Describe what replaces it, if anything.
4. Note the risk introduced.

---

*Maturity: Ratified — universal use-case formulation protocol adopted 2026-05-16 (DECISIONS.md); supersedes the daughter-file-only scope. Restructured 2026-05-09 from the World-Engine-specific original: civic content preserved as Category E; categories A–D and F added; universal foundational elements pulled out of the civic-specific instantiations.*
