---
type: source
tags: [design-system, gouvernance, mcp, figma, agents, skills, ecriture, securite]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[thiago-victorino](../entities/thiago-victorino.md)"
  - "[figma](../entities/figma.md)"
  - "[ecriture-agents-canvas-design](../concepts/ecriture-agents-canvas-design.md)"
  - "[gouvernance-technique-ia](../concepts/gouvernance-technique-ia.md)"
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
---

## Design Systems Just Became AI Governance Infrastructure

**Auteur** : [thiago-victorino](../entities/thiago-victorino.md), Victorino Group (The Thinking Wire)
**Date** : 2026-03-26
**URL** : https://victorinollc.com/thinking/design-governance-agent-era
**Fichier brut** : `raw/2026-03-26_victorino-design-governance-agent-era.md`

## Résumé

Synthèse analytique de deux événements convergents de mars 2026 : l'ouverture du canvas Figma aux agents IA en écriture via MCP beta, et l'essai de Wenbin sur la transformation du design system quand l'IA change le produit sous-jacent. La thèse : le design system passe de document de référence à contrainte d'exécution ("runtime constraint").

## Ce que change le MCP en écriture

Jusqu'ici, le vault documentait le Figma MCP uniquement comme canal de lecture (l'agent consulte les composants, tokens et styles pour informer son code, voir [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)). Cette source documente le changement de régime : le MCP beta permet à l'agent de créer des frames, placer des composants, modifier des designs existants — à l'intérieur de Claude Code, Cursor, VS Code, GitHub Copilot. L'agent produit de vrais artefacts Figma qui vivent dans le fichier. Voir le nouveau concept [ecriture-agents-canvas-design](../concepts/ecriture-agents-canvas-design.md).

## Le mécanisme de contrainte

Avant de créer quoi que ce soit, l'agent lit la bibliothèque de composants existante et construit avec ce qui existe déjà — il ne peut pas inventer une quatrième variante de bouton si seules trois existent. C'est une gouvernance par architecture (les limites sont structurelles, l'agent ne peut littéralement pas référencer ce qui n'existe pas), distincte de la gouvernance par contraintes exécutables déjà documentée dans [gouvernance-technique-ia](../concepts/gouvernance-technique-ia.md) (auditeurs, linting post-génération).

## Figma Skills comme gouvernance-as-code

Skill fondationnel `figma-use`, extensible par skills custom d'organisation. Une règle du type "utilise toujours le composant NavBar de la librairie core, ne crée jamais d'élément de navigation custom" est une règle de gouvernance encodée comme instruction agent plutôt que comme page wiki lue (ou pas) par un humain. Cette source apporte un exemple concret Figma-natif au concept déjà bien développé dans [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md).

## La complétude comme métrique de sécurité

Argument original de cette source : si le design system couvre 60 % des patterns d'interface d'un produit, les agents improviseront les 40 % restants sans contrainte. La couverture du design system cesse d'être un OKR d'équipe design pour devenir une métrique de risque — un angle absent des formulations de gouvernance déjà présentes dans le vault (qui se concentrent sur l'audit post-génération plutôt que sur la complétude comme surface d'exposition).

## L'échelle d'évolution

Style guide (suggère) → bibliothèque de composants (fournit) → linting (impose) → couche de contrainte pour agents (gouverne). Chaque étape augmente l'autorité du système sur ce qui est produit.

## Limites reconnues par l'auteur

Le MCP Figma en écriture est en beta : aucune entreprise ne tourne cela à l'échelle production documentée au moment de la publication. L'auteur qualifie explicitement son analyse de "signal directionnel, pas de pattern établi" — une prudence méthodologique rare dans le corpus du vault, qui vaut la peine d'être notée sans être lissée.

## Citations clés

"The design system is not a reference document anymore. It is a runtime constraint." (Thiago Victorino)

"Coverage is no longer a design team OKR. It is a risk metric." (Thiago Victorino)

"Everyone else will wonder why their AI keeps inventing new button styles." (Thiago Victorino)
