---
type: source
tags: [design-system, mcp, ia, benchmark, implémentation, json, gouvernance]
created: 2026-06-17
updated: 2026-06-17
sources: []
related:
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[jesse-gardner](../entities/jesse-gardner.md)"
  - "[laura-fehre](../entities/laura-fehre.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[into-design-systems-conference](../entities/into-design-systems-conference.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[code-source-de-verite-mcp](../concepts/code-source-de-verite-mcp.md)"
---

## Design Systems MCP: The Complete Guide

**Source** : Into Design Systems — https://www.intodesignsystems.com/design-systems-mcp
**Conférenciers** : [diana-wolosin](../entities/diana-wolosin.md) (Indeed), [jesse-gardner](../entities/jesse-gardner.md) (New York State), [laura-fehre](../entities/laura-fehre.md) (Figma), [romina-kavcic](../entities/romina-kavcic.md) (The Design System Guide)
**Contexte** : Synthèse des talks de l'AI Design Systems Conference 2026
**Fichier brut** : `raw/2026-06-17_design-systems-mcp-complete-guide.md`

## Thèse principale

Un MCP de design system codifie composants, tokens et guidelines en métadonnées machine-readable afin que les LLM puissent générer du code UI conforme au système. La source consolide quatre implémentations réelles avec des résultats mesurables, et introduit deux arguments nouveaux par rapport au corpus existant : la thèse de Jesse Gardner ("code as source of truth") et la mise en garde radicale de Laura Fehre ("guidelines are not laws — the prompt wins").

## Apports spécifiques par conférencier

**[diana-wolosin](../entities/diana-wolosin.md)** (already in vault) — Confirmation et compléments du benchmark (1 056 prompts, 8 configurations, JSON gagnant). Formule la distinction MCP déterministe / LLM stochastique comme principe architectural.

**[jesse-gardner](../entities/jesse-gardner.md) (New York State)** — Implémentation inédite dans le vault : web components Lit + TypeScript, JSDoc comme source de vérité unique pour humains ET machines, Figma parity via Code Connect, manifest → MCP server. Cas concret : 5 pages PDF d'un formulaire complexe → formulaire fonctionnel multi-étapes stylé NY State en 13 minutes. Chiffre critique : 50–80K tokens gaspillés quand on pointe l'IA sur la codebase brute sans MCP. Voir [code-source-de-verite-mcp](../concepts/code-source-de-verite-mcp.md).

**[laura-fehre](../entities/laura-fehre.md) (Figma)** — Expérience de traduction cross-platform : Figma Make (React/Tailwind/Radix) → SwiftUI via un fichier de mapping des composants. Argument principal : les guidelines en markdown ne contrôlent pas le résultat — le prompt gagne dans presque 100% des cas. Un fichier markdown monolithique surcharge la fenêtre de contexte. Voir tension dans [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md) et [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md).

**[romina-kavcic](../entities/romina-kavcic.md)** — Plugin Tidy : 66 outils MCP couvrant audit du naming, health score sur 6 catégories, validation de variables, composition de patterns (formulaire login, confirmation destructive). Couplé à Observatory, un dashboard de visualisation du knowledge graph à travers Figma, GitHub, Storybook, Linear, Chromatic, Playwright et PostHog.

## Citations clés

- "AI is a new user. You now need to codify your knowledge so LLM can consume it, reason over it and build with it." (Wolosin)
- "JSON is like a contract. Explicit keys, explicit values, explicit boundaries, no ambiguity." (Wolosin)
- "You don't unlock AI infrastructure by writing better prompts. You unlock it by closing the gap between design and code." (Gardner)
- "Code generation is becoming a commodity. Trustworthy implementation is not." (Gardner)
- "Guidelines are not laws. In nearly 100% of cases the prompt will win over the guidelines." (Fehre)
- "Don't skip designers in the loop — vibe coding without systems thinkers recreates silos." (Gardner)

## Connexions identifiées

La citation de Laura Fehre crée une tension directe avec [concevoir-les-conditions](../concepts/concevoir-les-conditions.md) et [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md) (contraintes exécutables). Jesse Gardner introduit un troisième modèle d'implémentation aux côtés d'Indeed (MDX → JSON) et de Kavcic (Figma → MDX) : Code → JSDoc → manifest → MCP. La notion "progressive disclosure of context" (Wolosin) consolide [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md) avec un modèle d'activation par couches.
