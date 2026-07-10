---
type: concept
tags: [agentic, orchestration, agents, design-system, gouvernance, autonomie]
created: 2026-07-03
updated: 2026-07-03
sources:
  - "[[agentic-ds-from-chatbot-to-orchestration]]"
related:
  - "[[systeme-de-design-agentique]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[niveaux-confiance-actions-agentiques]]"
  - "[[protocole-arc]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[boucle-feedback-infrastructure]]"
  - "[[concevoir-les-conditions]]"
---

## Orchestration multi-agents en design system

L'orchestration multi-agents est le passage du modèle chatbot (un agent répond à des questions) au modèle opérationnel (plusieurs agents coordonnent du travail à travers des outils, fichiers, workflows et portes d'approbation). C'est la configuration que Kavcic nomme "governed autonomy" : pas de délégation totale, mais une délégation structurée avec supervision humaine sur les décisions critiques ([[agentic-ds-from-chatbot-to-orchestration]]).

## La structure : quatre agents spécialisés + un orchestrateur

Un système d'orchestration agentique pour le design system s'organise autour de quatre agents spécialisés coordonnés par un orchestrateur.

**L'agent designer** surveille Figma en continu pour détecter la dérive : composants sans description, variants ne respectant pas les conventions de nommage, instances détachées, styles locaux qui devraient utiliser des variables, annotations d'accessibilité manquantes, composants qui ont trop proliféré en variants. Il ne modifie pas — il produit un rapport, suggère des correctifs, et escalade les changements risqués.

**L'agent développeur** surveille le codebase pour les mismatches tokens/code : couleurs hardcodées, usage incorrect de tokens, composants custom qui dupliquent des composants système, props dépréciés, tests manquants, composants qui ne correspondent pas aux specs Figma. Sa valeur est de rendre visible la dérive invisible entre design et implémentation.

**L'agent documentation** lutte contre la [[documentation-lag]] : guidelines d'usage des composants, tableaux de variants, notes d'accessibilité, exemples, changelogs, guides de migration, références de tokens. C'est le point d'entrée le plus facile parce que le risque d'une documentation incorrecte est plus faible qu'un correctif de code automatisé.

**L'agent QA** exécute les vérifications répétitives avant merge : tests d'accessibilité, régressions visuelles, tests d'interaction clavier, comportement responsive, conformité tokens, compatibilité navigateur, validation Storybook. Sa valeur est la consistance : il applique les mêmes checks à chaque PR, sans fatigue, sans oubli.

**L'orchestrateur** est la pièce critique. Il coordonne les quatre agents et prend les décisions de routage : quel changement peut être automatisé directement, lequel doit passer en review, qui doit approuver quoi, quels tests doivent passer, quand ouvrir une PR, quand rollback, quand escalader. Sans orchestrateur, chaque agent est un outil isolé. Avec orchestrateur, ils forment un système.

## Governed autonomy : déléguer juste assez

La notion de "governed autonomy" est la formulation opérationnelle de [[concevoir-les-conditions]] appliquée aux agents : on ne conçoit pas ce que l'agent fait — on conçoit les conditions sous lesquelles l'agent peut agir en sécurité. Déléguer juste assez pour que le système accélère, pas assez pour perdre la supervision.

Cela rejoint [[niveaux-confiance-actions-agentiques]] : l'autonomie n'est pas binaire (l'agent décide tout ou rien). Elle est graduée par type d'action. Auto-merge pour les corrections à faible impact. Draft PR pour les changements de valeurs. Suggest only pour les décisions architecturales. L'orchestrateur est la couche qui applique cette graduation à chaque action.

## Pré-requis : la structure prime sur les agents

L'orchestration multi-agents ne fonctionne que si le design system est suffisamment structuré pour que les agents aient quelque chose à lire. Un agent designer ne peut pas détecter qu'un composant viole une convention de nommage si les conventions ne sont pas encodées. Un agent développeur ne peut pas détecter une violation d'intent token si les tokens n'ont pas d'intent ([[intent-token]]). Le modèle multi-agents amplifie la qualité de l'infrastructure — dans les deux sens. "AI does not magically fix weak systems; it amplifies them."

C'est pourquoi Kavcic recommande de commencer par les tâches les plus "boring" : détecter la dérive, mettre à jour la documentation, ouvrir des PR de migration, flaguer les problèmes d'accessibilité. "Boring is where trust starts." La confiance dans le système multi-agents se construit par accumulation de petits succès vérifiables, pas par délégation totale immédiate.

## Relation avec le protocole ARC et la boucle self-healing

L'orchestration multi-agents est la réalisation concrète du [[protocole-arc]] Phase 3 (l'IA comme auto-gouverneur). La Phase 1 (consommateur) correspond à un agent isolé qui répond à des questions. La Phase 2 (mainteneur) correspond à un agent qui audite et produit des rapports. La Phase 3 est le système coordonné où les agents proposent, valident, escaladent et exécutent sous supervision.

La boucle Watch/Analyze/Execute/Observe de [[boucle-feedback-infrastructure]] (Kavcic, Self-Healing Design System) est la version opérationnelle de cette Phase 3 en production depuis un an — avec 12 outils MCP connectés à Claude Code. L'orchestration multi-agents conceptualisée ici est la généralisation de cette boucle à plusieurs agents spécialisés plutôt qu'un seul.

## ARC Protocol (RPC) comme couche d'infrastructure possible

L'[[arc-protocol-rpc]] (arc-protocol.org, 2026) est un protocole RPC stateless open-source qui répond à un problème d'infrastructure lié à l'orchestration multi-agents : comment router des centaines d'agents spécialisés via un seul endpoint, avec sécurité et observabilité garanties. Son ARC Ledger (registre d'agents) et ARC Compass (ranking sémantique) sont des primitives d'infrastructure qui pourraient sous-tendre un orchestrateur multi-agents en production.

À distinguer du [[protocole-arc]] d'Achiardi (Audit → Report → Compose), qui est un cadre de maturité, pas un protocole réseau. Les deux "ARC" coexistent dans le domaine sans relation directe.

## ⚡ Tension : orchestration vs contrôle humain

À mesure que l'orchestrateur prend plus de décisions de routage automatiquement, la question de responsabilité se déplace. Un orchestrateur qui décide seul qu'un correctif est "safe to auto-merge" prend une décision qui auparavant revenait à un humain. La limite n'est pas technique — elle est organisationnelle : qui répond quand l'orchestrateur se trompe ?

Le corpus du vault ([[gouvernance-design-system-ia]]) documente les mécanismes techniques (audit logs, rollback, approval gates) mais laisse ouverte la question de responsabilité organisationnelle pour les décisions automatisées qui vont en production sans validation humaine. L'orchestration multi-agents aggrave cette tension en multipliant les points de décision automatisée.
