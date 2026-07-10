---
title: "Agentic design system: how to build a component library AI agents can actually use"
source: "https://designproject.io/blog/agentic-design-system/"
author:
  - "Dianne Alter"
published: 2026-05-07
created: 2026-06-29
tags:
  - "clippings"
---

# Agentic design system: how to build a component library AI agents can actually use

## What is an agentic design system?

An agentic design system is a component library structured so AI agents can use it without guessing. Each component is shipped with machine-readable metadata that defines its purpose, variants, tokens, relationships, and explicit anti-patterns — what the agent must never do. The result is a single source of truth that humans browse visually and agents query programmatically, so the same button means the same thing in Figma, in code, and in Claude Code.

The traditional design system was built around one assumption: a designer or developer would read it, interpret it, and apply judgment. An agentic design system removes the judgment step. Every "use this here" or "don't use this there" gets written down — because the agent can't infer it.

In practice, an agentic component bundles:
- The implementation (the actual React or Vue code)
- A metadata file describing purpose, variants, when-to-use, and when-not-to-use
- Token definitions in CSS
- Storybook stories so the team can still see it visually
- Tests that enforce correct usage

### Agentic design system vs. traditional design system

A traditional design system documents components for humans — Figma libraries, Storybook pages, written guidelines. An agentic design system adds a structured metadata layer (JSON, YAML, or typed schema) that an AI agent can parse directly, with explicit fields for relationships, anti-patterns, and intent.

### Agentic design system vs. design tokens

Design tokens are a piece of an agentic system, not the whole thing. Tokens give the agent the right colors and spacing values, but they don't tell it which component to reach for or when not to use it. An agentic system layers component-level reasoning on top of token-level primitives.

### Agentic design system vs. Figma MCP

Figma MCP exposes your Figma file to an agent — it can see the layers, variables, and frames. That's a great starting point, but Figma alone doesn't capture intent ("don't put two primary buttons side by side") or relationships ("this lives inside a form, not a navbar"). An agentic design system fills the gaps Figma can't.

## Why a human-readable design system fails AI agents

When a developer opens your Storybook, they bring context: they know what the product does, they've seen primary buttons before, they understand that two CTAs side by side looks weird. An agent brings none of that. It pattern-matches on whatever's most visible — usually whatever it saw most often during training — and ships that.

That's how you end up with components in your codebase that look right but quietly drift from your system. New variants appear. Spacing values get rounded. Disabled states get reinvented because the agent didn't realize one already existed.

Done right, an agentic design system flips this:
- Speed compounds instead of decays. The agent pulls components correctly the first time. ~10x throughput on feature work once a client's system is properly structured.
- Your design system stays a system. Drift stops happening because the agent has no excuse to invent — every decision is already documented.
- Designers and engineers stop translating. The handoff between Figma and code collapses, because the metadata is the handoff.

## The three pillars of an agentic component

Every component in an agentic system needs three things. Miss one and the agent starts guessing again.

**1. Props.** The properties that define the component's states and variants — primary, secondary, disabled, loading, size, etc. These map directly to what you've already built in Figma.

**2. Relationships.** What the agent must understand *before* placing the component. Is it a child of a form? A toolbar? A dialog? Where is it most often used? What can it not live next to? This is the layer humans figure out from context — and the layer agents can't.

**3. Tokens.** The design tokens the component consumes. Good tokens are written in *English the agent can reason about* — `emphasis`, `default`, `subtle`, `core-grey-200` — not arbitrary names like `color-1` or `brandBlue`.

On top of those three pillars, every component's metadata needs to capture four decisions:

| Decision | What it answers |
|---|---|
| State and implied tokens | Primary, hover, pressed, disabled — and which token each maps to |
| Variants | Appearance, size, density — the axes the component can flex along |
| Accessibility | How the component behaves for screen readers, keyboard, focus |
| Purpose and anti-patterns | What this component is *for*, and explicitly what it should *never* be used for |

> "the hottest new programming language is English" — Andrej Karpathy. When you're writing metadata for an agent, you're programming in English. The most powerful instruction in English is telling the agent what *not* to do.

## What an agentic component looks like in practice

### Structure de fichiers : 6 fichiers par composant

- `button.tsx` — l'implémentation
- `button.meta.json` — metadata (purpose, variants, commonPatterns, antiPatterns, tokens)
- `button.tokens.css` — token definitions propres au composant
- `button.stories.tsx` — Storybook stories
- `button.test.tsx` — tests enforcing correct token consumption and state coverage
- `index.ts` — export

### Exemple : button.meta.json

- `category: atom`
- `purpose: "Interactive trigger for a single decisive action. The most common interactive primitive — use exactly one per intent. Variant signals hierarchy."`
- `variants: primary | secondary | minimal | destructive` (avec raison pour chaque)
- `commonPatterns: ["dialog confirm/cancel", "form submit", "toolbar action"]`
- `antiPatterns: ["two primary buttons side by side", "buttons used for navigation", "destructive variant without a confirm step"]`
- `tokens: { background: "color.action.primary", text: "color.text.on-primary", spacing: "spacing.button" }`

**Résultat client B2B SaaS après ~20 composants structurés :** feature work 5 jours → 1 afternoon.

## How to build an agentic design system

1. Créer un sibling package sur une branche (ne pas refactorer le DS live)
2. Définir le schéma de metadata *avant* de construire le premier composant
3. Auditer Figma pour l'AI-readiness
4. Construire un composant end-to-end avant de scaler
5. Lire la metadata générée et l'affiner (les anti-patterns spécifiques ne viennent que des connaissances d'équipe)
6. Encoder le processus comme un Claude Code skill

### Audit Figma : naming des variables

**Variables avec intent (bon) vs positionnelles (mauvais) :**

| Mauvais | Bon |
|---|---|
| `primary`, `secondary`, `tertiary` | `emphasis`, `default`, `subtle` |
| `blue-1`, `blue-2`, `blue-3` | `core-grey-200`, `core-grey-300` |
| Pas de description | "Hover state on items with subtle emphasis" |

Chaque token doit avoir une description dans Figma : "Active background for primary CTAs", "Hover state on items, subtle raising." Ces descriptions voyagent avec le design et donnent à l'agent le contexte pour choisir correctement.

## Ressources mentionnées

- Claude Code : l'agent layer
- Figma MCP : connexion Figma → agent
- Storybook : vue humaine du système agentique
- **AI Component Metadata skill** (Chris Carini) : `npx claude-skill ai-component-metadata` — scaffold la couche metadata, pose les bonnes questions pour la cohérence entre composants
- Context7 plugin : documentation up-to-date des bibliothèques open-source
