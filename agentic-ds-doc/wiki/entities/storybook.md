---
type: entity
tags: [outil, composants, mcp, tests, documentation, storybook]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[storybook-mcp-ai-aware-component-libraries](../sources/storybook-mcp-ai-aware-component-libraries.md)"
  - "[agentic-design-systems-2026-bradfrost](../sources/agentic-design-systems-2026-bradfrost.md)"
related:
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[brad-frost](brad-frost.md)"
---

## Storybook

Storybook est l'outil de développement isolé de composants le plus répandu de l'écosystème design system (React, Vue, Web Components, etc.). Depuis la version 10.3, il embarque `@storybook/addon-mcp`, un serveur MCP qui expose la bibliothèque de composants comme un ensemble d'outils interrogeables par un agent à l'exécution plutôt que comme du texte collé dans un prompt.

Repéré une première fois dans le vault comme quatrième point d'entrée MCP de l'écosystème (aux côtés d'Indeed, New York State et Tidy/Kavcic) via [brad-frost](brad-frost.md) ([agentic-design-systems-2026-bradfrost](../sources/agentic-design-systems-2026-bradfrost.md)), puis documenté en détail avec démonstration technique complète dans [storybook-mcp-ai-aware-component-libraries](../sources/storybook-mcp-ai-aware-component-libraries.md) : six outils MCP répartis en trois toolsets (docs, dev, test), backés par des manifests de composants générés au build. Le toolset test (`run-story-tests`) est ce qui permet à un agent de vérifier et corriger son propre travail avant qu'un humain ne le voie, une instance concrète de [boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md) entièrement automatisée à l'échelle d'un composant.
