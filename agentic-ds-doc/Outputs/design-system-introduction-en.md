# Design System & AI: From Infrastructure to Generated Code

## What is a design system

A design system is a set of formalized, shared design decisions: UI components, style tokens (colors, typography, spacing), usage guidelines, and the documentation that accompanies them. It is the organizational answer to a simple question: how do we prevent every team from independently reinventing the same buttons, forms, and patterns?

It exists at the intersection of three disciplines: design (what things look like), code (how they are implemented), and governance (who decides what and how the system evolves). Most design systems that fail neglect the third pillar.

Since June 2024, in line with the Lead the Future plan, the Orange Unified Design System aims to rationalize and consolidate multiple design system initiatives across the group. Officially launched in early 2026, it was certified L4 (mandatory) by Federation IT in June 2026.

## Why it is beneficial

**For production speed.** Teams do not start from scratch. A developer building an onboarding screen assembles existing components rather than creating new ones. The gain is not dramatic on a single task. It is massive at organizational scale over time.

**For experience consistency.** Without a shared source of truth, every team produces subtle variations: slightly different buttons, inconsistent spacing, contradictory behaviors. The end user experiences this as a fragmented product, even without being able to articulate why. A design system ensures the product "speaks with one voice" regardless of how many teams contribute to it.

**For structural quality.** Design system components are designed and tested once for all contexts: accessibility, responsiveness, error states, dark mode. Without a DS, this work is repeated in every team, often partially and with uneven results. An accessibility bug fixed in a shared component disappears everywhere simultaneously. The same bug in a component duplicated ten times must be found, fixed, and tested ten times.

**For maintenance.** Changing a brand color or updating a typographic rule happens in one place and propagates everywhere. Without a DS, the same change must be applied manually across every product, often incompletely. Without a DS, the cost of maintenance is not added up: it is multiplied.

**For collaboration.** Designers and developers share the same vocabulary. "Use the Card component with the elevated variant" is an unambiguous instruction when the DS exists. Without it, every design-to-dev handoff is a negotiation.

---

In short: a design system reduces the surface area of local decision-making so that teams can focus their energy on what is genuinely new, rather than on what has already been solved elsewhere in the organization.

## The design system as infrastructure

The distinction between a tool and infrastructure is not semantic. It determines how we invest, how we govern, and what we are willing to let degrade.

A tool can be set aside. Infrastructure is inherited, whether we want it or not. We do not evaluate an electrical grid by asking whether people "use it." We look at whether the voltage is stable, whether the load is absorbed, whether the supply is reliable. And above all: a grid of poor quality does not simply sit idle — it damages what is connected to it.

**It is shared and invisible when it works.** Nobody thinks about the electrical grid when they turn on a light. In the same way, a good DS disappears into the workflow. Developers do not consciously "use" it; they build on top of it. It only becomes visible when something breaks or when teams deviate from it.

**It is a convergence point for multiple systems.** The DS is where design, code, brand, accessibility, and documentation meet. Removing or degrading this convergence point does not destroy a tool: it desynchronizes entire systems that depended on a shared source of truth.

**It produces network effects.** The more it is adopted, the more its value increases. Every team that works around it reduces its value for everyone else, creates forks, and fragments the user experience. This is exactly the behavior of infrastructure, not a tool.

**Its debt is systemic.** Neglecting a tool is visible. Neglecting infrastructure produces diffuse effects, in projects that never identify the root cause. Design system debt manifests as visual inconsistencies, duplicated components, and recurring accessibility bugs. Never attributed to the DS itself, but always caused by its absence.

---

In short: treating a DS as a tool means accepting that it is optional. Treating it as infrastructure means recognizing that its quality determines the quality of everything built on top of it. In the age of agentic AI, it is urgent to channel the influx of new OUDS users that LLMs represent.

## How AI impacts design systems

The rise of code assistants (Copilot, Cursor, Claude) introduces a new variable into the design system equation. These tools generate code continuously, for every developer, on every task. The question is no longer "do our developers use the DS?" but "does the AI they use know the DS?"

**AI amplifies what already exists.** If the DS is well-structured, documented, and exposed to tools, AI generates compliant code: the right components, the right tokens, the right variants. If the DS is opaque or poorly documented, AI ignores it and produces generic code that bypasses the infrastructure. It is not neutral: it amplifies either coherence or debt.

**An "LLM-readable" DS changes the nature of the gain.** Until now, a DS accelerated production by preventing developers from starting from scratch. With AI, it can go further: a well-contextualized assistant can suggest the right component, flag an incorrect usage, or generate a complete screen while respecting the system's constraints. The DS becomes the reference the AI consults with every line of code it produces.

**Making a DS readable by AI is not a separate project.** It starts with structure: semantically named design tokens to avoid ambiguity, components documented with their usage guidelines, associated code examples. This work also improves the experience for human developers. It is a dual-benefit investment, not an additional cost.

**The risk of doing nothing is asymmetric.** Without investment in the DS, developers' AI tools will produce code that ignores it, accumulating debt at a speed proportional to the adoption of those tools. A DS that is structured and exposed to models becomes a compounding advantage: every line of generated code respects the system, with no additional effort from the developer.

---

In short: AI does not replace the design system. It reveals its quality. A well-built DS becomes a force multiplier. A neglected DS becomes a blind spot that AI exploits unintentionally.

## Our plan to make the DS "LLM readable and usable"

Making a design system exploitable by AI is not simply a matter of writing more documentation. It is a structured effort across several layers, from the foundations (design tokens) to tooled exposure (agents and MCP servers), with governance that ensures everything stays synchronized over time.

### 1. Consolidate the semantic token architecture (in progress)

This is where everything starts. Design tokens are the vocabulary AI must master. OUDS already rests on a solid semantic architecture. The goal of this step is to enrich it to make it fully exploitable by models: adding explicit descriptions to each token, documenting correct usages and common mistakes (do/don't), and clarifying the relationships between the different layers of variables which, without descriptions, remain silent decisions: understandable to those who know the system, opaque to a model that must infer it.

### 2. Produce LLM-optimized documentation (in progress)

Standard DS documentation explains what components do. LLM-oriented documentation goes further: it explains *when* to use them, *why* one component over another, and *what not to do*, in a structured and pragmatic way. This last point is crucial for models to avoid misinterpretations. Anti-patterns, common misuses, and composition pitfalls allow an LLM to detect violations, not just suggest correct code.

Every component must be documented with its usage rules, its variants and their contexts of application, its accessibility constraints, and annotated code examples. Not raw snippets, but examples that explain *why* a given token, component, or structure is used. These annotated examples serve both as human reference material and as learning examples for models.

### 3. Produce agents.md files and skills (in progress)

Documentation alone is not enough: we need actionable artifacts that tools can load and execute. `agents.md` files define the system context to inject into an assistant. They embed DS rules, conventions, and constraints so that any LLM that loads them generates compliant code without manual configuration. Skills go further: they encapsulate complete workflows, including generating DS-compliant components and running conformance audits on existing code.

An audit skill is particularly strategic: it detects code that deviates from the DS (wrong tokens, non-standard components, non-conformant patterns) and produces an actionable report. This is the feedback loop that maintains quality over time.

### 4. Expose the DS via an MCP server

Static files (documentation, agents.md) are a good starting point. The next step is exposing the DS as an MCP server, a protocol that allows developers' tools to query the DS in real time. Rather than loading a static context at the start of a session, a developer can ask "which component fits this use case?" and get an up-to-date answer directly from the living DS. This is what transforms the DS from a documented reference into a queryable infrastructure, anchoring AI tools in the reality of the system rather than a frozen copy.

### 5. Define an evaluation framework

To know whether the effort is producing results, we need to measure. An evaluation framework defines test cases: given a code generation request, is the output compliant with the DS? Does it use the right components, the right tokens, the right variants? These evaluations allow us to iterate on the quality of agents and skills with an objective baseline, and to detect regressions as the DS evolves.

### 6. Govern updates over time

The least visible risk of this plan is desynchronization. When the DS evolves (new component, deprecated token, revised usage rule), the AI documentation, agents.md files, and skills must all be updated at the same time. Without an explicit process, the AI layer risks progressively drifting from the real DS, recreating exactly the problem it was meant to solve.

Update governance is not a technical subject: it is an organizational one. Who is responsible for coherence between the DS and its AI artifacts? At what point in the contribution cycle does a DS update trigger an update to LLM documentation? These answers must be documented and integrated into the contribution process from the outset, not added after the first desynchronization has already occurred.

---

These six layers form a coherent system: tokens are the foundation, documentation and examples are the content, agents and skills are the operational entry points, the MCP server is the real-time channel, evaluations are the measure, and governance is what keeps the whole thing alive. Each layer reinforces the others. The absence of any one of them weakens all the rest.

## Conclusion

A design system is not a project you ship and close. It is a living infrastructure. Its value depends on the rigor with which it is maintained and how it is exposed to the tools teams actually use.

AI is not a threat to the design system. It is a revealer. A DS that is structured, documented, and exposed to models produces more consistent code, faster, with fewer manual judgment calls for developers. Without this investment from the core team, AI tools silently bypass the infrastructure, one generated line of code at a time.

The plan presented here is not a bet on the future of AI. It is an investment in the quality of what is being produced today, with the tools that already exist in developers' hands.
