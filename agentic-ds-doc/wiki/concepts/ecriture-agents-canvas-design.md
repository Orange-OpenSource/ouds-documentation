---
type: concept
tags: [design-system, mcp, figma, gouvernance, ecriture, agents, canvas, autonomie]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md)"
  - "[uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md)"
related:
  - "[figma](../entities/figma.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[generation-spec-agentique](generation-spec-agentique.md)"
  - "[gouvernance-technique-ia](gouvernance-technique-ia.md)"
  - "[niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
---

## L'écriture agentique dans le canvas de design

Jusqu'ici, l'intégration MCP entre agents IA et outils de design documentée dans le vault était structurellement asymétrique : l'agent *lit* le contexte (composants, tokens, styles depuis Figma) pour informer du code qu'il écrit ailleurs, dans un IDE. Le [mcp-model-context-protocol](mcp-model-context-protocol.md) est décrit comme un canal de lecture dans la quasi-totalité des sources ingérées avant juillet 2026.

[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md) documente un changement de régime : le Figma MCP beta (24 mars 2026) permet à l'agent d'*écrire* directement dans le canvas — créer des frames, placer des composants, modifier des designs existants. L'agent ne produit plus une suggestion que le designer implémente ; il produit l'artefact final, qui vit dans le fichier Figma partagé par l'équipe.

## Le mécanisme de contrainte par architecture

La propriété qui rend cette écriture gouvernable plutôt que dangereuse : avant de créer quoi que ce soit, l'agent lit la bibliothèque de composants existante et ne peut construire qu'avec ce qui y figure. Si le design system ne compte que trois variantes de bouton, l'agent ne peut pas en référencer une quatrième — elle n'existe pas dans l'espace de ce qu'il peut appeler. C'est une contrainte structurelle, pas une consigne contournable par le prompt, au même titre que la contrainte de permission de [jan-six](../entities/jan-six.md) chez GitHub Primer (l'agent ne peut créer qu'une issue, jamais merger) documentée dans [niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md) — sauf qu'ici la contrainte porte sur le vocabulaire disponible plutôt que sur le niveau d'action permis.

## Un précédent antérieur : uSpec (Uber)

L'écriture agentique dans Figma n'est pas inaugurée par le MCP officiel de mars 2026. [uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md) documente dès 2026-03-11 un agent qui écrit directement dans un fichier Figma via le Figma Console MCP open-source (Southleft) — importe un template, le peuple de texte, tableaux et marqueurs anatomiques. Voir [generation-spec-agentique](generation-spec-agentique.md). La différence : uSpec écrit de la documentation structurée (specs), pas des composants d'interface fonctionnels destinés à être livrés tels quels. L'écriture documentée par Victorino porte sur l'artefact de design lui-même, pas sur sa documentation.

## La complétude comme métrique de sécurité

Conséquence directe de l'écriture contrainte par architecture : un design system incomplet devient un problème de sécurité, pas seulement de qualité. Si le système ne couvre que 60 % des patterns d'un produit, l'agent improvisera les 40 % restants sans qu'aucune contrainte structurelle ne s'applique — l'improvisation d'un logiciel autonome sur l'interface d'un produit est l'inverse de la gouvernance. Cet argument déplace [gouvernance-technique-ia](gouvernance-technique-ia.md) (centrée sur l'audit post-génération et les contraintes exécutables) vers une préoccupation amont : la couverture elle-même comme condition de possibilité de la gouvernance, pas seulement sa cible de mesure.

## ⚡ Limite reconnue

Victorino qualifie explicitement le MCP en écriture de beta sans déploiement production documenté à l'échelle. L'écart entre "un agent peut écrire dans un fichier Figma" et "un agent produit de façon fiable du travail de qualité production dans les contraintes d'une entreprise" reste ouvert. Ce concept documente une capacité et son cadre de gouvernance émergent, pas un résultat validé en production.
