---
type: entity
tags: [personne, design-system, ia, github, gouvernance, primer]
created: 2026-06-22
updated: 2026-06-24
sources:
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
  - "[into-design-systems-agentic-guide](../sources/into-design-systems-agentic-guide.md)"
related:
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
  - "[into-design-systems-conference](into-design-systems-conference.md)"
---

## Jan Six

Membre de l'équipe Primer chez GitHub. Intervenant à l'AI Design Systems Conference 2026, où il a présenté l'approche de gouvernance agentique adoptée par l'équipe Primer de GitHub.

## Contribution documentée

Sa contribution principale est une décision architecturale radicale en matière de [niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md) : dans le système Primer, les agents ne peuvent créer qu'une issue, jamais merger du code. Cette contrainte structurelle — et non une règle en markdown — garantit qu'aucune modification automatisée n'atteint la production sans validation humaine.

L'équipe Primer fait tourner des workflows agentiques en QA et maintenance quotidienne, mais tous les outputs sont qualifiés de "safe outputs" soumis à revue humaine. Cette posture est cohérente avec la distinction que [romina-kavcic](romina-kavcic.md) nomme "level 3" dans son framework de [niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md) : les décisions de gouvernance restent au niveau "suggest only" parce qu'elles "nécessiteront toujours du jugement humain."

La différence avec d'autres approches du vault est que Jan Six n'applique pas les niveaux de confiance par type d'action (auto-merge pour les typos, draft PR pour les tokens) mais par architecture de système : le niveau de confiance maximal autorisé est encodé dans la capacité même de l'agent, pas dans une règle que l'agent pourrait contourner. C'est une forme de [concevoir-les-conditions](../concepts/concevoir-les-conditions.md) appliquée à la gouvernance agentique.

Un détail d'implémentation notable : GitHub Primer utilise des **sous-agents spécialisés** — par exemple un agent "accessibility reviewer" — pour maintenir le contexte principal propre lors des workflows de génération. Cette approche évite la pollution du contexte principal par des tâches périphériques, et correspond au principe de [architecture-contexte-agentique](../concepts/architecture-contexte-agentique.md) : des bulles de contexte séparées pour des responsabilités séparées. ([into-design-systems-agentic-guide](../sources/into-design-systems-agentic-guide.md))

Sa formule centrale sur le problème de l'invisibilité : "The invisible part of your system is way bigger than your visible part. If the agent can't see it, it has to hallucinate." Cette phrase synthétise mieux que toute autre la raison d'être d'un design system machine-readable.
