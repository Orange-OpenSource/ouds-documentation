---
type: concept
tags: [workflows, agent, sans-mcp, chatgpt-projects, documentation, contribution, audit, low-barrier]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[[agent-workflows-design-system-teams]]"
related:
  - "[[ia-comme-utilisateur]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[processus-generation-metadata-echelle]]"
  - "[[architecture-contexte-agentique]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[gerard-pamies]]"
---

## Workflows agent sans MCP

Ce concept désigne les workflows d'agent IA appliqués au design system qui ne requièrent pas d'infrastructure MCP, de base vectorielle, ou de pipeline de documentation automatisé. Le contexte est fourni directement via des fichiers Markdown uploadés dans un ChatGPT Project (ou équivalent). L'agent répond, documente, compare et audite à partir de ces inputs.

L'approche est formulée explicitement par [[gerard-pamies]] ([[agent-workflows-design-system-teams]]) : "What matters is providing clear prompts, reusable templates, and structured inputs like Markdown, ADRs, and token/component exports." Pas d'infrastructure — de la discipline dans la structuration des inputs.

## Positionnement dans le parcours vers le DS agentique

Dans la réponse query [[2026-06-17_comment-commencer-design-system-agentique]], l'étape 1 recommandait de "commencer sans infrastructure" avant de construire les trois couches MCP. Ce concept page est la formalisation de cette étape 1. Il représente le point d'entrée le plus accessible au DS agentique : faisable aujourd'hui, sans budget infrastructure, avec un investissement limité à la structuration d'un MD d'inventaire de composants.

Ce n'est pas une alternative au MCP — c'est une antéchambre. Les mêmes principes de lisibilité machine (voir [[lisibilite-machine-design-system]]) et de contexte structuré (voir [[trois-couches-composants-agents]]) s'appliquent, mais l'implémentation est manuelle et locale plutôt qu'automatisée et systémique.

## L'input principal : le MD d'inventaire de composants

[[gerard-pamies]] identifie un document central : le fichier Markdown listant tous les composants du DS avec leurs propriétés. C'est le document que l'agent doit avoir en priorité pour produire une documentation cohérente et des réponses contextualisées.

Template :

```markdown
<!-- List of existing components in my Design system -->

# MyComponentName_01
| Name | Description | Values | CodeOnly |
|---|---|---|---|---|
| propertyName | Description text | list of variants | - |

## Nested components:

# MyComponentName_02
```

Ce tableau de propriétés est un sous-ensemble du [[schema-metadata-composant]] de Morales Achiardi — moins complet (9 sections vs 4 colonnes), mais opérationnel pour les cas d'usage prioritaires.

## Les ADRs comme inputs de gouvernance

[[gerard-pamies]] signale une pratique de gouvernance légère : alimenter l'agent avec les ADRs (Architecture Decision Records) du projet. Quand un contributeur demande comment implémenter un composant dans une technologie spécifique, l'agent peut référencer les décisions internes — produit une réponse cohérente avec la gouvernance sans que le contributeur ait à naviguer dans l'historique des décisions.

C'est une implémentation légère du principe encodé dans [[architecture-skills-rules-instructions]] : les décisions de design (Rules / Instructions) orientent le comportement de l'agent. La différence est structurelle : dans l'approche Morales Achiardi, les Rules sont encodées dans un fichier CLAUDE.md toujours-on ; dans l'approche Pàmies, les ADRs sont uploadés dans le Project comme fichiers de contexte à la demande. L'effet est proche, l'automatisation est moindre.

## L'agent comme membre le plus expert de l'équipe

La formulation de Pàmies est la plus directe du vault sur ce sujet : "You get consistent answers similar to what you'd get from the most knowledgeable person on the team — without interrupting them." C'est la même thèse que [[ia-comme-utilisateur]] vue du côté de l'équipe interne — non pas l'IA comme consommateur du DS, mais l'IA comme externaliseur du savoir tribal de l'équipe.

Le cas d'usage contribution support est l'illustration la plus concrète : les équipes contributrices posent leurs questions à l'agent, l'agent répond en cohérence avec les décisions internes, et les membres seniors ne sont pas interrompus. Le savoir tacite (ce qui se passait dans la tête des seniors) est externalisé dans les ADRs qui alimentent l'agent.

## L'audit Anova : pont vers la gouvernance quantitative

Le workflow d'audit de composants via l'export JSON du plugin **Anova** (Figma) est le plus proche d'une automation de gouvernance légère. L'export JSON fournit une représentation structurée de l'état des composants ; l'agent l'utilise pour QA et vérification de cohérence. C'est une implémentation manuelle de ce que [[boucle-feedback-infrastructure]] et [[existence-vs-intent-violations]] formalisent : détecter les dérives entre l'intent et l'état actuel.

## ⚡ Tension / Contradiction

L'approche "no MCP required" est efficace pour des tâches ponctuelles mais ne résout pas le problème structurel identifié par [[diana-wolosin]] ([[mcp-on-demand-vs-rules-always-on]]) : les fondations (Design Principles, Accessibility Guidelines) ne sont actives que si l'humain pense à les inclure dans le Project à chaque session. Il n'existe pas d'équivalent de la couche "always-on" dans cette architecture — les Guidelines peuvent être oubliées, les ADRs pas mis à jour. L'approche Pàmies est une entrée accessible ; elle ne remplace pas une architecture pérenne.
