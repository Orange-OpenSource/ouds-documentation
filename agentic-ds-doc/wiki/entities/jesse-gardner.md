---
type: entity
tags: [personne, design-system, ia, mcp, new-york-state, web-components]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)"
related:
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[code-source-de-verite-mcp](../concepts/code-source-de-verite-mcp.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[into-design-systems-conference](into-design-systems-conference.md)"
---

## Jesse Gardner

Jesse Gardner est Director of User Research au sein du gouvernement de l'État de New York, où il dirige le développement du design system officiel de New York State. Il est intervenu à l'AI Design Systems Conference 2026 d'Into Design Systems.

Son apport principal au corpus : une troisième voie d'implémentation d'un MCP de design system, distincte de l'approche MDX-first d'Indeed ([diana-wolosin](diana-wolosin.md)) et de l'approche Figma-first de [romina-kavcic](romina-kavcic.md). Chez New York State, le code est la source de vérité unique. Les web components sont construits en Lit et TypeScript, documentés avec du JSDoc riche (usage guidance incluse : "use filled for primary action, outline for secondary"), puis transformés en custom element manifest → MCP server. La parité design/code est assurée via Code Connect. Voir [code-source-de-verite-mcp](../concepts/code-source-de-verite-mcp.md).

Son cas le plus cité : avoir alimenté Claude Code avec un PDF de 5 pages décrivant un processus administratif complexe pour parents adoptifs, et obtenu un formulaire multi-étapes fonctionnel stylé aux normes NY State en 13 minutes — en s'appuyant sur le MCP pour les composants et les tokens.

Il identifie deux erreurs courantes dans les approches non structurées : pointer l'IA directement sur la codebase brute (50–80K tokens gaspillés, fenêtre de contexte saturée) et exclure les designers des boucles de génération ("vibe coding without systems thinkers recreates the silos we're trying to break down"). Sa formulation condensée de la valeur du MCP : "Code generation is becoming a commodity. But what's not becoming a commodity is trustworthy implementation. And that's the gap."
