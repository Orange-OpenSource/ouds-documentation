---
type: concept
tags: [pipeline, documentation, mcp, design-system, monorepo, single-source, automatisation]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[typeform-design-system-documentation-scale-ai](../sources/typeform-design-system-documentation-scale-ai.md)"
related:
  - "[pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md)"
  - "[notion-cms-design-system](notion-cms-design-system.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[documentation-lag](documentation-lag.md)"
  - "[fernando-coelho](../entities/fernando-coelho.md)"
---

## Pipeline multi-destinations

Un pipeline multi-destinations est une architecture dans laquelle une source de contenu unique alimente simultanément plusieurs applications distinctes — typiquement : site de documentation (pour les humains), serveur MCP (pour les agents IA), et environnement sandbox (pour l'expérimentation interactive).

[fernando-coelho](../entities/fernando-coelho.md) chez Typeform documente la variante la plus complète de ce pattern dans le corpus du vault ([typeform-design-system-documentation-scale-ai](../sources/typeform-design-system-documentation-scale-ai.md)). La source unique est Notion (converti en Markdown via API). Les trois destinations : Docusaurus (documentation humaine), le MCP server (assistance IA), le Sandbox (playground interactif). Le même Notion API Client et le même package de code snippets sont consommés par les trois applications dans un monorepo.

## La propriété clé : cohérence garantie structurellement

La valeur principale d'un pipeline multi-destinations est qu'il garantit structurellement que l'agent IA a accès exactement à la même documentation que celle que lisent développeurs et designers. Pas une version approximative, pas une copie potentiellement désynchronisée — la même. Cette cohérence est une propriété architecturale : elle ne dépend pas de processus de synchronisation manuels ou de discipline d'équipe.

C'est la résolution la plus directe du problème de fragmentation décrit dans [documentation-lag](documentation-lag.md) : au lieu de connecter des sources multiples (Figma + Notion + Storybook) après coup, on produit une source unique et on la distribue vers plusieurs consommateurs.

## Les code snippets comme sous-cas

[fernando-coelho](../entities/fernando-coelho.md) documente un cas particulier du pattern : un package de code snippets consommé par les trois applications. Les exemples de code dans la documentation, les exemples dans le sandbox, et les exemples que le MCP suggère sont tous produits depuis le même package. L'agent ne peut pas suggérer un pattern d'implémentation incorrect par rapport à la documentation — ils sont générés depuis la même source.

Ce principe d'une "single source of truth" distribué vers plusieurs consommateurs est applicable à d'autres assets : les tokens (déjà souvent dans ce pattern via Style Dictionary), les icônes (un package d'assets consommé par la doc, le code et le MCP), les guidelines d'accessibilité.

## Comparaison avec les autres pipelines du vault

Le vault documente plusieurs pipelines de documentation, chacun avec une source et une architecture différentes :

**[pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md) (Kavcic/Romina)** — source : Figma ; destination : documentation MDX ; agent : Claude Code. Le pipeline est unidirectionnel et ciblé sur la synchronisation design → docs. L'accent est sur la fraîcheur (le design comme source de vérité) plutôt que sur la pluralité des destinations.

**Pipeline Indeed (Wolosin)** — source : documentation MDX ; parsers JavaScript × 4 domaines ; destination : JSON → Vectra → MCP. L'accent est sur la conversion vers un format agent-optimal (JSON) et sur la régénération automatique à chaque mise à jour.

**Pipeline Typeform (Coelho)** — source : Notion ; destination : docs (Docusaurus) + MCP + Sandbox. L'accent est sur la démocratisation de la contribution (Notion comme interface) et sur la cohérence multi-destinations.

Les trois pipelines répondent à des priorités différentes : Kavcic prioritise la fraîcheur, Wolosin prioritise la précision agentique (JSON), Coelho prioritise la contribution et la cohérence. Ils sont complémentaires plutôt que substituables.

## Limites de l'approche

La limite principale est le format de sortie. Un pipeline dont la source est Markdown (Notion → Markdown → MCP) ne produit pas le format optimal pour les agents IA — [diana-wolosin](../entities/diana-wolosin.md) documente que JSON réduit de 80 % les tokens et divise par 5 le coût par rapport à Markdown ([lisibilite-machine-design-system](lisibilite-machine-design-system.md)). Le pipeline multi-destinations tel que décrit par Typeform est un point de départ, pas un état final d'optimisation agentique.

La seconde limite est le délai de mise à jour : GitHub Actions hebdomadaire signifie une latence maximale de 7 jours entre une mise à jour Notion et sa propagation vers les destinations. Pour les modifications critiques, le déclenchement manuel est disponible — mais il requiert une action humaine consciente.
