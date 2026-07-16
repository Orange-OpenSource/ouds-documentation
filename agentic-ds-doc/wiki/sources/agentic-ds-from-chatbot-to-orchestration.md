---
type: source
tags: [design-system, agentic, orchestration, contrats-composants, tokens, gouvernance, risques]
created: 2026-07-03
updated: 2026-07-03
sources: []
related:
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[orchestration-multi-agents](../concepts/orchestration-multi-agents.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[composants-context-aware](../concepts/composants-context-aware.md)"
---

## Agentic Design System — From Chatbot to Orchestration

**Auteur** : Romina Kavcic
**Publication** : The Design System Guide (Substack)
**URL** : https://learn.thedesignsystem.guide/p/agentic-design-system-from-chatbot
**Date** : 10 mai 2026

## Thèses principales

L'article reformule le problème central du design system agentique avec une précision nouvelle : la plupart des équipes préparent le mauvais futur IA. Elles s'interrogent sur *comment générer des composants plus vite*, alors que la vraie question est *si l'agent peut comprendre pourquoi un composant existe, quand l'utiliser, et quand ne pas le faire*.

Trois thèses structurantes traversent l'article :

Première thèse — la transition chatbot → orchestration. Un chatbot répond. Un agent agit. Un système d'agents coordonne du travail à travers des outils, fichiers, workflows et portes d'approbation. Le design system cesse d'être une bibliothèque passive et devient une couche d'orchestration opérationnelle.

Deuxième thèse — le composant devient contrat. Ce renversement conceptuel est la contribution la plus originale de l'article : dans un design system agentique, un composant n'est plus quelque chose qu'on importe, mais un contrat entre design, code, intent produit, accessibilité et comportement. Un bouton n'est pas `<Button variant="primary">Submit</Button>` — c'est aussi les règles : quel variant pour quelle intention, quand escalader, quand refuser la composition.

Troisième thèse — structure > prompts. Les entreprises qui gagnent seront celles qui préparent leur design system pour la lecture machine. "The prompt is not the moat. The structure is."

## Citations clés

"The next generation of design systems will not be judged by how many components they have. They will be judged by how well agents can read them, reason with them, and safely act on them." (≤15 mots : "judged by how well agents can read them, reason with them, and safely act on them")

"Your design system is no longer just for humans. It is becoming infrastructure for agents."

"The prompt is not the moat. The structure is."

"Governance gaps: agentic systems need approval rules, audit logs, rollback mechanisms, permission levels, test gates, ownership models, escalation paths."

"AI does not magically fix weak systems; it amplifies them."

## Connexions identifiées

L'article étend [systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md) avec le modèle d'orchestration multi-agents (4 agents spécialisés + orchestrateur), qui n'était pas encore formalisé dans le vault. Il introduit le concept de [composant-comme-contrat](../concepts/composant-comme-contrat.md) comme renversement du paradigme traditionnel. Il enrichit [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md) avec un inventaire des risques spécifiques à l'autonomie agentique (design debt machine-speed, fausse confiance, manipulation UX, governance gaps). Il précise [intent-token](../concepts/intent-token.md) avec des exemples de métadonnées riches `useFor`/`avoidFor`/`accessibility` — plus élaborés que le champ `$description` DTCG déjà documenté. Il converge avec [concevoir-les-conditions](../concepts/concevoir-les-conditions.md) via la notion de "governed autonomy" : déléguer juste assez pour que le système accélère sans perdre la supervision.
