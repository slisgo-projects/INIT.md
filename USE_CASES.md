# USE_CASES.md

Categories of activity where INIT.md is applied. Captures the bounding scope the schema must support and the implications each category surfaces for INIT.md.

Structure is categorical, not per-project. Individual projects are developed per-project as INIT.md is applied to each. Examples below are illustrative bounding cases, not entries.

When a per-project use case grows unwieldy and is subdivided into its own `USE_CASE_<identifier>.md`, follow the daughter-file protocol in USE_CASE_INIT.md.

Per category per INIT.md §"USE_CASES.md", with one addition (Implications for INIT.md) to make explicit the back-cast that the spec preamble promises but does not list as a field. Some fields are recast where the original civic-tech-flavored framing maps poorly (e.g., "Geographic region" → typical loci, "Regulatory requirements" → typical external constraints).

## 1. Software systems

- **Motivation.** Code-centric deliverables. Includes foundational AI infrastructure, large-scale simulation, knowledge management and indexing software, embedded software for hardware projects, monitoring and assistive software.
- **Geographic region of application.** Typically N/A — software is location-independent unless coupled to regulated-sector deployment.
- **Potential stakeholders.** Operator; upstream model and platform providers (when AI-coupled); downstream projects that consume the software as substrate; external users when applicable.
- **Target audience.** Variable — operator-private (knowledge management) through broad public (simulation, communications platforms).
- **Deliverables.** Auditable codebases; integration interfaces; deployment configurations.
- **Timelines.** Iterative; multi-year typical for non-trivial systems given solo + AI cadence.
- **Regulatory requirements.** Domain-dependent. Pure-software projects often have none; sector-touching projects (healthcare, government, financial) inherit the sector's regime.
- **Implications for INIT.md.** Schema's natural home; INSPIRATIONS.md peer schemas (spec-kit, Kiro, arc42) all assume this category. Most ergonomic fit. Custom domain-specific files (DATA_LAYERS.md, AGENT.md patterns) often emerge. INTERFACES.md mostly within-project; cross-project software dependencies (one project's code consumed by another) surface a portfolio-level interface question the schema does not yet address.

## 2. Physical and embodied systems

- **Motivation.** Hardware deliverables: mechanical assemblies, robotics, electronic systems, integrated hardware-software products. Includes autonomous robots, humanoid assistive systems, modular physical platforms producing many derivative products, biofeedback and therapeutic hardware, propulsion and aerospace concept hardware.
- **Geographic region of application.** Often the operator's locale; wider when products distribute. Outdoor-deployment subset adds local regulatory context.
- **Potential stakeholders.** Operator; upstream component vendors and supply chain; safety/regulatory bodies (medical, transport, aerospace) where applicable; end-users when products distribute.
- **Target audience.** Self, household, hobbyist communities, or external users by project.
- **Deliverables.** Physical artifacts plus their controlling software, build instructions, BOMs, integration tests, safety and graceful-degradation behaviors.
- **Timelines.** Hardware iteration is slower than software; supply-chain dependent; prototyping intervals typically dominant.
- **Regulatory requirements.** Safety frameworks (electrical, mechanical, transport); medical-device regulation when therapeutic; outdoor-operation rules; export controls for some technologies.
- **Implications for INIT.md.** Strongest test of the project-type-agnostic claim. INTERFACES.md becomes load-bearing in the canonical ICD sense (mechanical mating, electrical, protocol). VALIDATION.md is intrinsic — physical V&V is the deliverable, not optional. Custom hardware-specific files recur (TURTLEBOT.md pattern). Modular-platform projects (one platform spawning many derivative products: a tube-and-connector system yielding trailers, scooters, buggies, boats) need a sub-project relationship the schema does not directly express.

## 3. Scientific research programs

- **Motivation.** Domain research producing knowledge deliverables: simulation codes, materials characterization, energy-concept development, advanced propulsion concepts, technical critique of existing programs. Often coupled to experimental campaigns or design programmes.
- **Geographic region of application.** International research community; specific institutional collaborations across partner labs and funding-agency jurisdictions.
- **Potential stakeholders.** Scientific community; research institutions and partners (universities, national labs, international consortia); funding bodies; peer reviewers; community of code or data users.
- **Target audience.** Researchers; integrated-modeling teams; future-device design groups; policy audiences for critique-style work.
- **Deliverables.** Research codes; published findings (papers, presentations); design analyses; reference datasets; technical position papers.
- **Timelines.** Multi-year characteristic; coupled to experimental campaigns and funding cycles; large-programme contexts span decades.
- **Regulatory requirements.** Domain data-exchange standards (e.g., IMAS/OMFIT for fusion) function as de facto regulation; institutional ethics review when applicable; export controls for dual-use technologies; publication norms.
- **Implications for INIT.md.** Stakeholder structure stresses the team-of-one assumption — solo + AI collaboration must coexist with external collaborators using different tooling, often without AI-optimized inputs. VALIDATION.md is intrinsic (scientific validity is the deliverable). Custom process files (REFACTORING.md pattern) common. Document handoff to non-AI-using collaborators may require selectively relaxing AI-optimization rules — an open question for the schema's adaptability that the team-of-one MOTIVATION.md strand acknowledged but did not resolve.

## 4. Authorship and analytical work

- **Motivation.** Text-driven deliverables: fiction, non-fiction, technical and bureaupathological critique. The deliverable IS prose; code or hardware are supporting at most.
- **Geographic region of application.** Typically N/A; subject matter may be region-specific.
- **Potential stakeholders.** Author (operator); editors; publishers; subject-matter experts consulted; eventual readership; subjects of critique work where present.
- **Target audience.** Readers; varies by genre and intent (general public, technical audience, policy audience).
- **Deliverables.** Manuscripts; structured critiques; reference apparatus; published or self-published works.
- **Timelines.** Months to years per work; multi-work portfolios extend longer.
- **Regulatory requirements.** Copyright; libel and defamation considerations for critique work; publication-contract terms when applicable.
- **Implications for INIT.md.** Strongest counter-pressure on the project-type-agnostic claim. ARCHITECTURE.md and INTERFACES.md become awkward — text deliverables do not have "elements with interface contracts" in the systems-engineering sense; they have chapters or sections with logical flow. IMPLEMENTATION.md as phased code development does not fit; a sequential drafting/revision arc replaces it. VALIDATION.md is unclear (peer review, coherence checks, fact-checking, beta-reader feedback?). May justify either a writing-flavored variant of the schema or explicit field-recasting guidance for prose-deliverable projects.

## 5. Civic and community initiatives

- **Motivation.** Multi-stakeholder, public-facing, social-organizational work. Includes large-scale simulation-as-civic-infrastructure, continent- or ocean-spanning communications backbones, community empowerment and self-sufficiency programmes, advocacy and reconciliation work, and shared linguistic or cultural infrastructure (constructed languages, common protocols, crowdsourced standards).
- **Geographic region of application.** Locally specific (a town, a region) or globally distributed (international infrastructure, universal-adoption-aimed standards). Region is load-bearing in this category.
- **Potential stakeholders.** Government bodies (local through international); community members; partner organizations; funding bodies; broader public audiences; critics and opposition; co-authors and contributors for crowdsourced work. Stakeholder count and heterogeneity highest of any category.
- **Target audience.** General public; specific affected communities; policymakers; civic institutions; learner or adopter populations for shared-standard work.
- **Deliverables.** Software platforms for civic engagement; communications materials at multiple attention budgets; deliberation infrastructure; community organizing structures; trained local capacity; specifications and definitional artifacts for shared standards or languages.
- **Timelines.** Slow-burn; political, community, and adoption cycles dominant; impact horizons in decades.
- **Regulatory requirements.** Privacy and dual-use concerns prominent; political and legal contexts; consultation requirements; transparency and attribution standards for AI-generated communications; intellectual property and licensing for shared-standard work.
- **Implications for INIT.md.** Highest stakeholder heterogeneity and political risk profile of any category. The original "regulatory requirements / connections to broader policy directives" framing in INIT.md's USE_CASES.md spec is strongest-fit here — that field is civic-tech-rooted, not merely civic-tech-flavored, and its phrasing earns its place when applied to this category specifically. Communications infrastructure subset (audience-targeted multi-format outputs at varying attention budgets) is a recurring deliverable not currently listed in the schema. **Crowdsourced-formulation sub-pattern** (constructed language, public-spec-by-contribution): the first place in the portfolio where non-AI humans are co-authors of the deliverable itself, not merely stakeholders. The team-of-one assumption breaks more strongly here than in scientific research collaborations — contribution review and aggregation become first-class workflow concerns absent from the current schema. HUMAN.md's single-person sustainability framing requires supplementing with collaborative-partner discipline for civic work spanning multiple actors.

## 6. Personal infrastructure and self-sufficiency

- **Motivation.** Self-directed practical projects serving the operator's own use without external audience. Includes homestead capability, reference-library cataloging, modular physical platforms used as the basis for derivative projects, lifestyle systems.
- **Geographic region of application.** Operator's locale.
- **Potential stakeholders.** Operator; household; immediate community when shared.
- **Target audience.** Self.
- **Deliverables.** Working systems serving the operator: organized archives, food/energy/shelter capability, platforms supporting derivative projects, daily-life infrastructure.
- **Timelines.** Long-arc; intermittent; rotation across life seasons typical.
- **Regulatory requirements.** Local — building codes for homestead modifications, copyright and fair-use for archived knowledge, agricultural and water rules where applicable.
- **Implications for INIT.md.** Strongest test of the team-of-one + no-external-audience configuration HUMAN.md targets. Sustainability framing is most directly load-bearing here. Modular-platform sub-project hierarchy (one platform, many derivative artifacts) recurs from category 2 and is the same structural finding from a different vantage. Self-as-only-stakeholder collapses several spec fields (Geographic region, Potential stakeholders, Target audience all become trivial), reinforcing that the category-level USE_CASES.md is necessary — per-project recasting of the same trivial fields would be empty repetition.

---

*The six categories above bound the schema's intended scope. As individual projects are pursued, they inherit the relevant category's implications.*
