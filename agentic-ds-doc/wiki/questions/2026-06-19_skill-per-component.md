---
type: question
tags: [design-system, skills, agents, architecture, mcp, metadata, intent, context-aware]
created: 2026-06-19
updated: 2026-06-19
sources:
  - "[agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)"
  - "[machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)"
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
related:
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md)"
  - "[composants-context-aware](../concepts/composants-context-aware.md)"
  - "[intent-token](../concepts/intent-token.md)"
---

## Is it a good idea to create one skill per DS component, invokable on demand by an agent?

The answer depends on what the skill encodes. If the answer is component data, no. If the answer is contextual usage reasoning, the intuition is right but the architecture leads somewhere different.

## Version 1: Skills as component knowledge stores

The simplest form — a Button skill that contains Button's variants, props, and anti-patterns — is a category error. According to [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md), **Skills are executable capabilities**, not knowledge containers. A Button's variants, anti-patterns, and composition rules are declarative knowledge. Storing them in a Skill is the wrong abstraction.

The right place for this, per [schema-metadata-composant](../concepts/schema-metadata-composant.md), [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md), and [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md), is a structured `.metadata.ts` (or JSON) file co-located with the component, served via MCP. [diana-wolosin](../entities/diana-wolosin.md)'s benchmark at Indeed (77 components, 1 056 test prompts) confirms that JSON-structured metadata via MCP outperforms prose-based alternatives on both precision and cost — 5× cheaper than Markdown, with no loss in accuracy.

Two structural problems remain regardless: **discovery** (the agent needs a routing layer to know which skill to invoke — MCP with semantic search solves this without the overhead) and **cross-component reasoning** (a task like "build a delete confirmation dialog" requires Button + Dialog + Alert simultaneously; a per-Button skill can't resolve that).

## Version 2: Skills as contextual usage reasoners

A more interesting refinement: per-component skills that don't store data but encode *how to use the component given intent and context*. A Button skill that knows "in a destructive action context, use the danger variant and always pair with Cancel" rather than "Button has these props."

The wiki's answer here is that this encoding already exists in the architecture — but it lives in **metadata sections**, not in skills. The `aiHints.selectionCriteria` field of [schema-metadata-composant](../concepts/schema-metadata-composant.md) does exactly this: explicit, intent-based decision rules per component ("usePrimary: Main action user should take on page/section", "useDanger: Destructive actions requiring attention"). The `usage.antiPatterns` structure goes further: each entry requires a `scenario` (what context triggers the mistake), a `reason` (why it's wrong in this context), and an `alternative` (what to use instead). This is contextual usage reasoning, per component, structured for agents — and it lives in JSON, queryable via MCP.

[composants-context-aware](../concepts/composants-context-aware.md) formalises the problem precisely: Button in an alert context uses `bg-danger` and requires a Cancel sibling; Button in a card uses `bg-neutral` and must not compete with page CTAs; Button in navigation uses `bg-brand` with a maximum of one instance. Same component, three different contextual specs.

## Why "data in metadata, reasoning in a single skill" is the better split

Whether the intent-and-context logic lives in per-component metadata or in per-component skills matters for one reason: **cross-component tasks**. "Button in an alert always needs a Cancel button" is not just a Button rule — it implies knowing that Alert and Button compose together, and knowing the composition rule at the graph level. A per-Button skill can't resolve that. The [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md) traversal can — but only if the data is relational and queryable, not locked inside isolated skill invocations.

The architecture that falls out of [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md) resolves this cleanly: **per-component `aiHints` in JSON metadata** (intent-and-context data, distributed, queryable via MCP) + **a single `/ai-ds-composer` skill** that reads this data, traverses the graph, and produces composition decisions. The reasoning capacity is centralised; the intent data is distributed. That separation is what enables cross-component reasoning while preserving the per-component intent granularity.

## The clean rule

From [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md) and [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md):

**JSON for component knowledge and intent (MCP, on-demand) — Markdown for rules and foundations (always-on) — Skills for executable procedures that reason across the graph.**

One skill that knows *how to consult the DS* is more powerful than N skills each carrying the reasoning for one component, because the important questions are always cross-component.
