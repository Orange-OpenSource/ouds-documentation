---
type: concept
tags: [design-system, ia, proactif, auto-amelioration, agentique, futur, phase3]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[[automating-design-system-ai-efficiency]]"
related:
  - "[[boucle-feedback-infrastructure]]"
  - "[[protocole-arc]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[accessibilite-continue]]"
  - "[[systeme-de-design-agentique]]"
  - "[[knowledge-graph-design-system]]"
---

## Système de design proactif

Un système de design proactif est un design system qui détecte et anticipe les besoins d'évolution sans être sollicité explicitement — en observant les patterns d'usage, les overrides récurrents et les comportements émergents pour générer des recommandations d'amélioration avant que les équipes en formulent la demande. C'est le stade le plus avancé du continuum décrit dans le [[protocole-arc]] : au-delà de la Phase 2 (Report, qui mesure), la Phase 3 (Compose) dans sa version la plus complète.

## Ce que ça signifie concrètement

[[mehmet-celik]] articule la vision en trois comportements distincts ([[automating-design-system-ai-efficiency]]) :

Le système **remarque un pattern émergent** à travers plusieurs projets — des designers indépendants composent la même combinaison de composants pour résoudre un problème identique — et suggère de le formaliser en composant ou pattern officiel. C'est la détection ascendante de la valeur, à partir de l'usage réel plutôt que de décisions top-down.

Le système **prédit des risques d'accessibilité** dans une direction de design proposée, avant même que cette direction soit testée ou prototypée. L'[[accessibilite-continue]] atteint son stade le plus avancé : non plus la vérification en temps réel, mais l'anticipation proactive.

Le système **recommande des ajustements de tokens** en observant les overrides récurrents. Quand plusieurs équipes surchargent systématiquement la même valeur de token, c'est le signe que le token ne capture pas correctement un besoin réel — le système le détecte et propose la correction. Cet usage est documenté pour Salesforce Lightning, qui explore la création prédictive de tokens à partir des patterns d'override ([[automating-design-system-ai-efficiency]]).

## Relation avec la boucle de feedback

La [[boucle-feedback-infrastructure]] telle que documentée par [[cristian-morales-achiardi]] est encore semi-manuelle : l'agent génère le rapport, l'humain lit la recommandation et implémente le correctif. Le système proactif décrit par [[mehmet-celik]] est la version entièrement automatisée de cette boucle — l'observation, la détection, et la recommandation (voire l'implémentation) sont déléguées à l'infrastructure. La boucle de Morales Achiardi est l'étape intermédiaire; le système proactif est la destination.

Cette progression correspond au passage de la Phase 2 à la Phase 3 du [[protocole-arc]] : Phase 2 mesure et rapporte, Phase 3 compose et améliore automatiquement. Au moment de la publication des sources du vault, la Phase 3 reste prospective — les équipes en sont majoritairement à l'automatisation aux marges ([[automating-design-system-ai-efficiency]]).

## Le [[knowledge-graph-design-system]] comme fondation

La détection de patterns émergents requiert que le système ait une représentation des usages réels à travers le temps et à travers les projets. Sans [[knowledge-graph-design-system]], il n'y a pas de données sur lesquelles fonder la détection — le système proactif reste conceptuellement possible mais techniquement hors de portée. C'est pourquoi l'Observatory dashboard de [[romina-kavcic]], qui croise Figma, GitHub, Storybook, Linear, Chromatic, Playwright et PostHog, est la première instance documentée d'une infrastructure suffisamment riche pour rendre ce type de proactivité réaliste.

## ⚡ Tension : proactivité vs accountability

Si le système est suffisamment autonome pour détecter et proposer — voire implémenter — des changements, la question de responsabilité se pose explicitement : "Who's accountable for automated updates that go live?" ([[automating-design-system-ai-efficiency]]). Cette question est absente du corpus technique du vault (Morales Achiardi, Wolosin, Gardner), qui se concentre sur comment encoder la gouvernance. Elle pointe vers un défi organisationnel : les modèles de gouvernance actuels supposent un humain qui valide avant déploiement. Un système proactif à déploiement automatique requiert des garanties différentes — ou un humain maintenu dans la boucle à un niveau d'abstraction plus élevé. Voir [[gouvernance-design-system-ia]].
