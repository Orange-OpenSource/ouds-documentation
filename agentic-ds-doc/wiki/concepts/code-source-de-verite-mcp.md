---
type: concept
tags: [design-system, mcp, code, jsDoc, web-components, source-de-verite, ia]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)"
related:
  - "[jesse-gardner](../entities/jesse-gardner.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[schema-metadata-composant](schema-metadata-composant.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md)"
---

## Code comme source de vérité pour le MCP

[jesse-gardner](../entities/jesse-gardner.md) documente chez New York State une approche d'implémentation MCP distincte des deux modèles déjà présents dans le vault : là où [diana-wolosin](../entities/diana-wolosin.md) part de la documentation MDX existante (MDX → parsers JavaScript → JSON → Vectra) et [romina-kavcic](../entities/romina-kavcic.md) part de Figma (Figma MCP → Claude Code → MDX), Gardner fait du code la source de vérité primaire pour les humains et les machines simultanément ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)).

## Le principe

L'idée centrale : la documentation ne vit pas dans un fichier Markdown séparé qui risque de diverger du code — elle vit *dans* le code, sous forme de JSDoc. Les web components sont construits en Lit et TypeScript. Chaque composant, chaque prop, chaque token est documenté directement dans le code source avec des commentaires JSDoc riches, incluant la guidance d'usage ("use filled for primary action, outline for secondary"). Ce JSDoc est ensuite transformé automatiquement en custom element manifest, puis exposé via un MCP server.

Le résultat est une source de vérité unique : quand un développeur met à jour un composant et son JSDoc, la documentation humaine et les métadonnées machines se synchronisent en même temps, automatiquement. Il n'y a pas de pipeline de synchronisation à maintenir entre documentation et code — ils sont le même artefact.

## Ce que ça change par rapport aux autres modèles

Dans l'approche Indeed, la documentation humaine (MDX dans GitLab) est la source primaire, et un pipeline de parsers la convertit en JSON pour les agents. La synchronisation est automatique (déclenchée à chaque update de documentation), mais la source reste la documentation humaine — le code n'est qu'une sortie.

Dans l'approche Kavcic, Figma est la source primaire. Claude Code lit les specs via MCP Figma et génère la documentation MDX.

Dans l'approche Gardner, le code Lit/TypeScript est la source primaire. Ni Figma ni MDX ne précèdent le code — le code précède tout. La parité design/code est maintenue via Figma Code Connect, qui mappe les composants Figma aux composants code après coup.

## Le résultat mesuré

[jesse-gardner](../entities/jesse-gardner.md) documente un cas de production : un PDF de 5 pages décrivant un processus administratif complexe (formulaire pour parents adoptifs) transformé en formulaire multi-étapes fonctionnel, stylé aux normes New York State, en 13 minutes. Le MCP a fourni les composants et tokens; Claude Code a composé le formulaire en respectant les contraintes du système.

## ⚡ Tension / Contradiction

L'approche Gardner suppose que le code est déjà la source de vérité — ce qui est vrai pour les équipes engineering-led où Figma suit le code. Dans les équipes design-led (où Figma précède le code, ou existe en parallèle sans synchronisation), cette approche ne fonctionne pas directement. Le choix entre les trois modèles (MDX-first, Figma-first, Code-first) n'est pas universel : il dépend de la topologie de l'équipe et de la gouvernance de la source de vérité.

Jesse Gardner le formule clairement : "You don't unlock AI infrastructure by writing better prompts. You unlock it by closing the gap between design and code." Son modèle résout ce gap d'une façon particulière — en faisant du code la source de vérité commune plutôt qu'en synchronisant deux sources distinctes.

Un risque supplémentaire qu'il nomme : "50–80k tokens wasted when you point AI at raw custom elements code." Le MCP est précisément ce qui filtre le signal utile du bruit de la codebase brute.
