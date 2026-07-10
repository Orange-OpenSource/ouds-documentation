---
type: entity
tags: [outil, ia, documentation, design-system, context, llm, libraries]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[20-ai-workflows-design-system-teams]]"
related:
  - "[[mcp-model-context-protocol]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[priori-conflictuels-nommage]]"
---

## Context7

Context7 (https://context7.com/) est un outil qui fournit aux agents IA la documentation à jour des libraries qu'ils utilisent. Les modèles de langage ont une date de coupure d'entraînement : quand un agent génère du code utilisant Style Dictionary v4, Radix Themes, ou Tailwind v4, il peut travailler sur une API de l'année précédente sans le savoir.

L'usage recommandé ([[20-ai-workflows-design-system-teams]]) : ajouter Context7 comme source de référence dans les workflows IA. Quand on génère des composants ou qu'on débogue des transformations de tokens, demander à l'agent de vérifier l'API courante via Context7 avant de produire du code. Évite de déboguer des problèmes qui n'existent pas dans la version actuelle des libraries.

Ce problème est une forme concrète des [[priori-conflictuels-nommage]] : l'agent n'arrive pas ignorant d'une API, il arrive avec des connaissances sur une version passée — ce qui peut être plus trompeur que l'ignorance pure.
