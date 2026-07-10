# Design System Documentation Spec 0.12.0

**Source** : https://designsystemdocspec.org  
**Date d'ingestion** : 2026-06-24  
**Auteur** : PJ Onori  
**Version** : 0.12.0 Draft (publié 23 juin 2026)  
**Statut** : Draft specification — non endorsée par un organisme de normalisation

---

## Overview (page principale)

A machine-readable format for design system documentation.

This standard puts design system docs in one shared format that any tool can read. It now covers components, design tokens, themes, foundations, patterns, and guides. The goal is one source of truth for a design system — to feed docs, train agents, and fill every touchpoint.

**Core tenets :**
- Information is more valuable when it's portable. Tools change. Needs change. Budgets change. A design system's source of truth should survive any rebuild, reorg, or rethink.
- Documentation shouldn't have to pick a side. Humans, parsers, and agents all need the docs. Teams shouldn't have to serve each one on its own. This standard aims to be the source of truth for everyone and everything it serves.
- A format that grows with you. Getting started should be easy. A docs standard should also grow to meet a system's needs.

**Flexible and modular.** All structured docs use one document block system. Each entry is a typed object with a kind field. The spec defines 16 block kinds — from guidelines, anatomy, and api to states, motion, and accessibility. Each entity type accepts only the block types that fit it.

---

## Quick Start

**Key idea:** DSDS documents the *how and why* of your design system — not the token values themselves. It complements the W3C Design Tokens Format which handles the *what*.

**What you get :**
- Structured — every section has a defined shape, no guessing
- Machine-readable — tools can parse, generate, validate, and transform it
- Portable — not locked to any docs tool or platform
- Extensible — add vendor metadata without breaking compatibility
- Validatable — JSON Schema catches errors before they reach consumers

### Document structure

A DSDS file requires dsdsVersion and one of two shapes:

**Single-entity files** — Use `entity` when each component, token, or pattern lives in its own file.

**Multi-entity files** — Use `entityGroups` to put several entities in one file, or as a manifest that points to separate entity files.

**$ref linking** — Entity arrays accept `$ref` objects that point to other DSDS files (JSON Pointer fragment `#/entity`).

### Entity types (7 kinds)

| Kind        | Description |
| ----------- | ----------- |
| component   | A reusable UI element — buttons, inputs, modals. Supports anatomy, API, variants, states, and design specs. |
| token       | A single design token — color, spacing, typography. Link to W3C DTCG definitions via source. |
| token-group | A nested group of related tokens. Recursive. |
| theme       | A named set of token overrides — dark mode, high-contrast, compact density, brand variants. |
| foundation  | A design base — color, typography, spacing, elevation. |
| pattern     | A broad action pattern showing how components combine to solve a user need. |
| guide       | A long-form, reading-oriented document — getting-started, contribution, tutorial, migration. |

**Common properties** : kind, identifier, name, optional description and metadata, plus documentBlocks and agentDocumentBlocks. The optional `agentDocumentBlocks` array is a separate space for agent-only docs. Tools never show it to humans; agents read both arrays.

**Status** : string or object with per-platform tracking (overall + platforms map).

### Document block system (16 kinds)

- useCases — When to use, stance: "recommended" | "discouraged", alternative
- guidelines — RFC 2119 levels: "must", "should", "should-not", "must-not"
- anatomy, api, variants, states, accessibility, checklist, content, design-specifications, document-blocks, guidelines, imports, interactions, motion, principles, scale, sections, steps

**Criteria (verification)** : automated (tool decides), assisted (human decides with tool surfacing candidates), manual (pure human judgment). Examples on a criterion are fixtures with "pass"/"fail" outcomes.

### Conventions

1. `status` has exactly two shapes: bare string or object with `overall`
2. It's always `identifier` (machine key), never `name`
3. `tokens` is a purpose-keyed map, not an array
4. Flag vs. enum variants (boolean vs. named options)

### Validation

```bash
# Bundled schema for editor autocompletion:
"$schema": "https://designsystemdocspec.org/v0.12.0/dsds.bundled.schema.json"

# CLI:
npx ajv validate -s spec/schema/dsds.bundled.schema.json -d my-system.dsds.json
```

---

## Humans & Agents

A DSDS document has two readers: people and AI agents. The same file serves both.

**documentBlocks** — the docs everyone reads. You write it for a person to read and act on: anatomy, API, variants, states, guidelines, accessibility. Agents read it too. Default home for everything.

**agentDocumentBlocks** — extra notes, for agents only. Tools never show it to people. Accepts same block kinds.

What belongs in agentDocumentBlocks:
- Hard rules (MUST/MUST NOT as firm limits)
- Telling look-alikes apart
- Limits backed by proof (evidence from testing)
- Checks an agent can run (pass/fail criteria)

What stays in documentBlocks: anything a person needs to read. A quick test: would a person reading the docs need this? If yes → documentBlocks. If no, and only a tool would act on it → agentDocumentBlocks.

"Agents read both arrays — the human docs first, then the agent-only notes. So agentDocumentBlocks adds to the human docs; it does not replace them."

Rules:
- Do not move human-facing content into agentDocumentBlocks.
- Do not repeat the human docs there. Agent notes should extend, never echo.

---

## Schema Architecture (partial — page trop large)

Full reference at https://designsystemdocspec.org/schema-architecture. Covers: document structure, entity properties, document block types, all shared models. JSON Schema in spec/schema/ for normative definitions.

---

## Links

- **GitHub** : https://github.com/somerandomdude/design-system-documentation-schema
- **Schema JSON** : https://designsystemdocspec.org/v0.12.0/dsds.bundled.schema.json
- **Feedback** : GitHub Issues
