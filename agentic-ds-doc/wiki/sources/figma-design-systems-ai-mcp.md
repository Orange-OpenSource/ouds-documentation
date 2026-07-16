---
type: source
tags: [design-system, mcp, figma, tokens, gouvernance, code-connect, statistiques]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[figma](../entities/figma.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
---

## Design systems and AI: Why MCP servers are the unlock

**Auteur** : Ana Boyer (Designer Advocate, [figma](../entities/figma.md))
**Publication** : Blog officiel Figma
**Date** : 2025-08-06
**URL** : https://www.figma.com/blog/design-systems-ai-mcp/
**Fichier brut** : `raw/2025-08-06_figma-design-systems-ai-mcp.md`

## Résumé

Source primaire (l'éditeur de l'outil) sur le rôle du Figma MCP server dans l'écosystème agentique des design systems. Contrairement aux sources secondaires déjà nombreuses dans le vault qui *décrivent* le Figma MCP depuis l'extérieur, celle-ci documente les cas d'usage tels que conçus par l'équipe qui les construit, avec des chiffres issus du rapport IA interne de Figma.

## Les deux chiffres structurants

68 % des développeurs utilisent déjà l'IA pour écrire du code, mais seulement 32 % font confiance à l'output généré (Figma AI report 2025). L'écart de 36 points entre adoption et confiance est l'argument central de l'article : le contexte design system est ce qui comble cet écart, pas un modèle plus puissant.

## Trois usages documentés pour les équipes design system

**Génération de code de composant aligné avec les standards** : l'agent combine le contexte MCP d'un nouveau composant avec le code des composants existants pour produire du code cohérent, dans le langage et framework réellement utilisés par l'équipe (pas limité à React/Tailwind par défaut).

**Automatisation du travail sur les tokens** : l'agent identifie où appliquer ou introduire des tokens, s'assure de la conformité aux standards déjà définis, aide à écrire des scripts d'automatisation via l'API plugin et la REST API.

**Audit et amélioration de l'alignement design/code** : audite l'usage des tokens dans le code vs le design sélectionné et inversement, signale les noms de layers à améliorer pour l'alignement, suggère des améliorations de props Figma.

## Génération automatique de fichier de règles

Fonctionnalité peu documentée ailleurs dans le vault avant cette source : le MCP server peut scanner la codebase et produire un fichier de règles structuré (définitions de tokens, bibliothèques de composants, hiérarchies de style, conventions de nommage), qui sert ensuite de guide système à l'agent. Le vault ne mentionnait jusqu'ici cette capacité que par une citation en passant dans [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md) (le skill `figma-create-design-system-rules`) — cette source explicite le mécanisme.

## Les annotations comme contexte additionnel

Les annotations Figma (accessibilité, comportement d'interaction, contenu) sont transmises par le MCP server à l'agent et se reflètent dans le code généré. C'est un canal de contexte distinct des tokens et composants — plus proche de l'intent que de la structure.

## Citations clés

"Asking an AI agent to generate code without design system context is like asking a new engineer to start shipping code before onboarding." (Ana Boyer)

"They also ensure that we don't all end up shipping the same generic UIs cobbled together from the same pool of AI-generated parts." (Ana Boyer)
