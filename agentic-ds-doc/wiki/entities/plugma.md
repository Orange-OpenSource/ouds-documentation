---
type: entity
tags: [outil, figma, plugin, design-system, toolchain, typescript, dev]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[20-ai-workflows-design-system-teams]]"
related:
  - "[[architecture-skills-rules-instructions]]"
  - "[[gouvernance-design-system-ia]]"
---

## plugma

plugma (https://www.plugma.dev/) est un toolchain moderne pour développer des plugins Figma : hot reload, TypeScript, bundling. Il simplifie suffisamment la chaîne de build pour que l'IA puisse écrire la logique du plugin pendant que plugma gère l'infrastructure.

Le cas d'usage design system ([[20-ai-workflows-design-system-teams]]) : construire un validateur de tokens qui scanne les frames sélectionnées et signale les violations (hex hardcodés, tokens primitifs utilisés directement en composants, couleurs de statut dans le mauvais contexte). Ce type de plugin transforme les règles de gouvernance en feedback en temps réel dans Figma — au lieu de les répéter dans les revues.

Initialisation : `npx create-plugma@latest my-token-validator`
