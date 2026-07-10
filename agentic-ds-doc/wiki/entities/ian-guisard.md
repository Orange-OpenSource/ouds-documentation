---
type: entity
tags: [personne, design-system, uber, agentic, mcp, accessibilite]
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[[uber-uspec-agentic-design-specs]]"
related:
  - "[[generation-spec-agentique]]"
  - "[[mcp-model-context-protocol]]"
  - "[[accessibilite-continue]]"
  - "[[pipeline-figma-docs-automatise]]"
---

## Ian Guisard

Lead du Base design system chez Uber. Auteur de uSpec, un système agentique open-source pour la génération automatique de specs de composants via Cursor + Figma Console MCP.

Sa contribution principale : démontrer à grande échelle (centaines de composants, 7 stacks d'implémentation) que la documentation de spec — anatomie, API, tokens, accessibilité multi-plateforme — peut être entièrement générée par un agent IA en quelques minutes plutôt qu'en semaines, sans que les données design propriétaires ne quittent le réseau local.

Il a présenté un framework pour créer des specs détaillées à l'échelle dans Figma, dont la popularité a révélé que le problème de la documentation bottleneck dans les design systems n'est pas spécifique à Uber. C'est l'arrivée du Figma Console MCP (Southleft) qui a rendu la réponse automatisée possible.

Formule emblématique : "Programmatic plugins can extract component data from Figma, but they can't interpret what that data means."

**uSpec** : https://github.com/redongreen/uSpec — https://uspec.design
**Article** : [[uber-uspec-agentic-design-specs]]
