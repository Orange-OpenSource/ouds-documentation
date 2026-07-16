---
type: question
tags: [meta, veille, gouvernance, accountability, gap, comparaison, mcp]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[gouvernance-organisationnelle-ia](../concepts/gouvernance-organisationnelle-ia.md)"
  - "[deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[ecriture-agents-canvas-design](../concepts/ecriture-agents-canvas-design.md)"
---

## Quel thème de veille complèterait le mieux le vault, en ciblant ses angles morts ?

Le vault documente abondamment les succès (Indeed, New York State, GitHub Primer, Spotify Encore, Miro, uSpec/Uber, Storybook MCP) mais quasiment jamais l'échec en production. Trois signaux convergents :

**Deux `[GAP]` déjà notés dans le journal** : aucune source ne documente l'implémentation concrète des quatre règles IA-UX dans un produit réel ([deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md)) ; aucune source ne documente un workflow bout-en-bout reliant spec formelle, métadonnées machine et documentation narrative — les sources couvrent chaque phase séparément.

**[accountability-gap-ia](../concepts/accountability-gap-ia.md) reste entièrement théorique** : Murphy Trueman y décrit un scénario de défaillance composite (composants accessibles individuellement, parcours inaccessible au global) sans qu'aucune source du vault ne rapporte un incident réel, nommé, avec conséquences et résolution documentées. Le seul cas concret de chaîne de responsabilité qui fonctionne (l'échelle de jaune chez Enara) est un bug de token isolé, pas une défaillance composite à l'échelle d'une interface.

**La tension "readiness technique vs organisationnelle"** ([overview](../overview.md)) pose la question sans réponse empirique : qui décide qu'un output IA est assez bon pour shipper, que se passe-t-il quand ça tourne mal.

## Recommandation principale

Une veille centrée sur les retours d'expérience négatifs et la gouvernance organisationnelle réelle : incidents documentés d'interfaces générées par IA ayant causé un problème de production (accessibilité, régression UX, incohérence de marque), post-mortems d'équipes design system sur des déploiements agentiques ratés, modèles concrets de contribution/ownership adoptés par des organisations pour trancher qui répond des outputs agentiques. Sans cet angle, le vault risque de devenir un argumentaire de vente pour l'agentique plutôt qu'une base de connaissance équilibrée.

## Angles secondaires

Une comparaison structurée des offres MCP commerciales concurrentes (zeroheight MCP, Knapsack MCP, Storybook MCP, Figma MCP) — le dossier `comparisons/` du vault ne contient qu'une comparaison de bibliothèques de composants ([astryx-vs-mui-atlaskit-shadcn](../comparisons/astryx-vs-mui-atlaskit-shadcn.md)), aucune comparaison d'infrastructure MCP.

Une preuve de la Phase 3 du [protocole-arc](../concepts/protocole-arc.md) à l'échelle d'un système de production entier plutôt qu'à l'échelle d'un seul composant — question encore ouverte depuis le cas Storybook MCP ingéré le 2026-07-16 (voir [overview](../overview.md), section Questions ouvertes).
