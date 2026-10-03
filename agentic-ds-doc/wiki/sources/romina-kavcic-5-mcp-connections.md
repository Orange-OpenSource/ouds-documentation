---
type: source
tags: [design-system, mcp, outils, figma, github, gitlab, posthog, slack, mintlify]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[figma](../entities/figma.md)"
  - "[mintlify](../entities/mintlify.md)"
---

## 5 MCP Connections Every Design System Team Needs Right Now

**Auteur** : [romina-kavcic](../entities/romina-kavcic.md)
**Publication** : thedesignsystem.guide (Substack)
**Date** : 2025-08-22
**URL** : https://learn.thedesignsystem.guide/p/5-mcp-connections-every-design-system
**Fichier brut** : `raw/2025-08-22_romina-kavcic-5-mcp-connections.md`

## Résumé

Article le plus ancien de Kavcic ingéré dans le vault (août 2025, antérieur à toute sa série "Agentic Design Systems"). Inventaire pratique de 6 connecteurs MCP pour équipes design system — Figma, Mintlify, GitHub, GitLab, PostHog, Slack — avec niveau de complexité d'installation et exemples de prompts concrets. Complète le vault sur un angle jusqu'ici dispersé en mentions narratives plutôt que structuré : un inventaire outil par outil, avec ce que chacun débloque spécifiquement.

## L'inventaire

**Figma MCP** (facile) — lecture de composants, tokens, variants ; génération de specs, prototypes cliquables avec états.

**Mintlify** (facile, clé API requise) — documentation comme base de connaissances vivante ; lookup direct depuis l'éditeur sans changer de fenêtre.

**GitHub** (facile, PAT requis) — prévient la dérive design/code ; review de PR avec détection de tokens manquants, génération de changelog, comparaison Figma Variables vs tokens du repo.

**GitLab** (modérée — nécessite tier Premium/Ultimate, absent sur Free/Starter) — gestion d'issues, commentaires sur MR, déclenchement de pipeline CI.

**PostHog** (modérée — nécessite tracking d'événements configuré) — valide les décisions de design system avec des données d'usage réelles : adoption comparée ancien/nouveau composant, CRO post-publication, taux de complétion de flow.

**Slack MCP** (modérée — approbation admin + OAuth) — transforme les conversations d'équipe en connaissance interrogeable : retrouver une décision de design review, compiler du feedback, alerter sur des patterns de duplication émergents.

## Apport net par rapport aux sources déjà ingérées

Le vault documentait déjà plusieurs de ces connecteurs de façon éparse dans [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md) (Figma, GitHub, Storybook, PostHog cités dans le workflow de production de Kavcic elle-même, [self-healing-design-system](self-healing-design-system.md)). Cette source apporte trois éléments absents : un niveau de complexité d'installation par outil (utile pour prioriser une adoption progressive), des exemples de prompts concrets et actionnables par outil, et GitLab / Slack comme connecteurs documentés pour la première fois avec un usage détaillé plutôt qu'une simple mention.

## Ce que ça confirme

La récurrence de Figma comme point d'entrée le plus simple et le plus recommandé ("I suggest you start by connecting Figma and Cursor/Claude and continue from there") est cohérente avec la position centrale de Figma dans le reste du corpus. La progression suggérée par Kavcic — commencer petit, un outil, une tâche répétitive automatisée — est la même logique que [seeds-vs-trees](../concepts/seeds-vs-trees.md) appliquée à l'infrastructure MCP plutôt qu'aux fondations de métadonnées.

## Citations clés

"The key difference with MCP is that AI moves from being a general assistant to being deeply integrated with your specific design system." (Romina Kavcic)

"With MCP, you control exactly what data and tools AI can access." (Romina Kavcic)
