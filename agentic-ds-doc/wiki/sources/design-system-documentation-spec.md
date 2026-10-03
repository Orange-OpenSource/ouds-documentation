---
type: source
tags: [dsds, design-system, machine-readable, schema, json, standard, format, agents, documentation]
created: 2026-06-24
updated: 2026-06-24
sources: []
related:
  - "[dsds-format](../concepts/dsds-format.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[documentation-lag](../concepts/documentation-lag.md)"
  - "[pj-onori](../entities/pj-onori.md)"
---

## Design System Documentation Spec (DSDS) 0.12.0

**URL** : https://designsystemdocspec.org  
**Auteur** : PJ Onori  
**Version** : 0.12.0 Draft  
**Date de publication** : 23 juin 2026  
**Statut** : Draft spec, non endorsée par un organisme de normalisation. Feedback via GitHub Issues.

## Résumé

DSDS est un format JSON machine-readable pour documenter les design systems. Il couvre les composants, tokens, thèmes, fondations, patterns et guides, dans un format unique lisible par des humains, des parsers, et des agents IA. L'ambition : une source de vérité portative pour tout un design system.

La distinction centrale de la spec : DSDS documente le *comment et le pourquoi* — pas les valeurs de tokens elles-mêmes. Il se positionne comme complémentaire au W3C Design Tokens Format (DTCG), qui gère le *quoi*.

## Thèses principales

**1. La portabilité comme valeur fondamentale.** Les outils changent. Les budgets changent. Les organisations restructurent. La source de vérité d'un design system doit survivre à tout rebuild, reorg, ou rethink. DSDS répond à ce risque en proposant un format ouvert, non lié à une plateforme ou un outil de documentation. "Information is more valuable when it's portable."

**2. Une documentation qui ne choisit pas son camp.** Humains, parsers, et agents ont tous besoin de la documentation. DSDS veut être la source de vérité pour chacun. Pas de documentation séparée pour humains et machines — un seul fichier, deux audiences.

**3. La séparation documentBlocks / agentDocumentBlocks.** Pour gérer la double audience sans la diluer, DSDS sépare formellement les deux espaces. `documentBlocks` est ce que tout le monde lit. `agentDocumentBlocks` est ce que seuls les agents lisent — les règles dures, les distinguos entre composants similaires, les critères de vérification. Les outils n'affichent jamais agentDocumentBlocks aux humains. Les agents lisent les deux.

**4. Les critères comme mécanisme de vérification.** Le système de criteria formalise ce que beaucoup de design systems tentent de faire informellement : des règles vérifiables avec un mode de vérification déclaré (automated / assisted / manual) et des exemples fixtures (pass/fail). Les niveaux RFC 2119 (must, should, should-not, must-not) permettent aux agents de distinguer ce qui est obligatoire de ce qui est recommandé.

## Citations clés

- "A design system's source of truth should survive any rebuild, reorg, or rethink." (core tenets)
- "Documentation shouldn't have to pick a side." (core tenets)
- "Tools never show agentDocumentBlocks to people, and agents read both arrays." (humans-and-agents)
- "The statement is always the source of truth. The check is its executable shadow." (sur les criteria)
- "A quick test: would a person reading the docs need this? If yes → documentBlocks." (humans-and-agents)

## Connexions identifiées

DSDS est la première spécification ouverte qui formalise ce que le corpus a décrit comme architecture nécessaire d'un [systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md). Les concepts développés dans le vault — [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md), [schema-metadata-composant](../concepts/schema-metadata-composant.md), [ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md), [dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md) — trouvent ici une implémentation formelle standardisée. Le duo DSDS + DTCG (W3C) couvre l'ensemble : quoi (valeurs) + comment/pourquoi (documentation structurée). L'auteur [pj-onori](../entities/pj-onori.md) est le seul mainteneur actuel de la spec.

## Périmètre et limites

Version 0.12.0 Draft, non endorsée. Sujet à changement. Pas d'outillage de génération automatique documenté. La spec schema-architecture complète (>97KB) couvre les types d'entités, les propriétés de chaque block, et les modèles partagés — non ingérée en totalité.
