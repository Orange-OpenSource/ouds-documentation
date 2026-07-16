---
type: concept
tags: [gouvernance, ia, design-system, confiance, automatisation, agentique, github, primer]
created: 2026-06-22
updated: 2026-07-16
sources:
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
  - "[wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)"
  - "[amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md)"
related:
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[jan-six](../entities/jan-six.md)"
  - "[boucle-feedback-infrastructure](boucle-feedback-infrastructure.md)"
  - "[contraintes-fixed-preferred-exploratory](contraintes-fixed-preferred-exploratory.md)"
updated: 2026-06-30
---

## Niveaux de confiance pour les actions agentiques

Le problème des niveaux de confiance apparaît dès qu'un agent dispose d'un accès en écriture à un design system. Sans contrainte explicite, rien n'empêche l'agent de merger des PRs, modifier des APIs de composants ou mettre à jour des tokens — des actions qui, selon leur contexte, requièrent ou non une validation humaine. Confondre les deux registres crée une gouvernance instable : trop d'autonomie sur les décisions à fort impact, trop de friction sur les corrections triviales.

## Le cadre par niveau de risque (Romina Kavcic)

[romina-kavcic](../entities/romina-kavcic.md) propose de définir les niveaux de confiance par action, et non par agent ([your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)). La métaphore utilisée est celle de la progression de carrière : un junior ne prend pas les mêmes décisions qu'un principal. La traduction en niveaux opérationnels :

**Auto-merge** — haute confiance, risque faible. S'applique aux corrections de lint, aux typos dans la documentation, aux labels d'accessibilité manquants. Ces actions ont un impact limité et réversible, elles ne modifient pas l'interface programmatique du système.

**Draft PR** — confiance moyenne. S'applique aux mises à jour de valeurs de tokens, aux changements de description de composants, aux ajustements de métadonnées. L'agent produit le changement, un humain valide avant merge.

**Suggest only** — confiance faible ou impact élevé. S'applique aux nouvelles APIs de composants, aux changements breaking, aux décisions de gouvernance architecturale. Certaines décisions "ne passeront jamais le niveau 3 parce qu'elles nécessiteront toujours du jugement humain."

Ce cadre triadique est une instance de [gouvernance-design-system-ia](gouvernance-design-system-ia.md) appliquée non pas au contenu du système mais à ses droits d'accès.

## La version structurelle (Jan Six / GitHub Primer)

[jan-six](../entities/jan-six.md) implémente une variante plus radicale : au lieu de définir des niveaux de confiance comme des règles que l'agent choisit de respecter, GitHub Primer encode la contrainte dans la capacité même du système. Les agents Primer peuvent créer une issue, jamais merger du code. Le niveau de confiance maximal autorisé est architectural — pas une instruction en markdown, mais une limite de permission dans l'infrastructure.

Cette distinction est conceptuellement importante. Un framework de niveaux en prose (comme celui de Kavcic) oriente l'agent dans les cas normaux mais peut être contourné par un prompt contradictoire — ce que [laura-fehre](../entities/laura-fehre.md) documente comme "le prompt gagne sur les guidelines" ([gouvernance-design-system-ia](gouvernance-design-system-ia.md)). Un niveau de confiance encodé dans les permissions systèmes est une contrainte exécutable au sens de [concevoir-les-conditions](concevoir-les-conditions.md) : il ne peut pas être contourné par un prompt.

## La tension entre efficacité et contrôle

Le cadre triadique n'est pas sans coût. Placer trop d'actions au niveau "suggest only" annule le gain d'efficacité de l'automatisation — l'agent signale tout, les humains valident tout, on est revenu à l'état manuel. Placer trop d'actions au niveau "auto-merge" expose à des dérives non détectées. Le calibrage des seuils est une décision de gouvernance qui dépend du contexte d'équipe, de la maturité de l'infrastructure, et de la fréquence des changements.

## Lien avec la boucle de feedback

Les niveaux de confiance ne sont pas statiques. Ils doivent évoluer avec la maturité de l'infrastructure. Un agent qui produit des auto-merges fiables pendant 3 mois mérite probablement de voir son périmètre d'auto-merge élargi. La [boucle-feedback-infrastructure](boucle-feedback-infrastructure.md) fournit les métriques pour valider ce type de décision : taux d'erreur par type d'action, fréquence de rollback, violations détectées post-merge.

## Un contre-exemple de calibration ratée : le cas Amazon

[amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md) documente ce qui arrive quand les niveaux de confiance ne sont pas calibrés avant le déploiement à l'échelle. Amazon a effectivement laissé l'essentiel des changements de code assistés par IA opérer à un niveau proche de l'auto-merge (mandat de 80 % d'adoption, déploiements sans documentation ni approbation formelle dans au moins un des incidents) sans le cadre à trois niveaux de Kavcic ni la contrainte structurelle de Jan Six. Après quatre Sev-1 en 90 jours, la correction a été un recalibrage brutal vers l'extrême "suggest only" : sign-off senior obligatoire, review à deux personnes, audits VP sur 335 systèmes Tier-1 — la tension entre efficacité et contrôle décrite plus haut, mais vécue en sens inverse et sous contrainte de crise plutôt qu'anticipée. L'auteur de la source note que cette réponse n'est pas soutenable : elle réinsère la friction humaine à chaque étape plutôt que de construire une vérification automatisée qui scale à la vitesse de génération.

## L'approche Apple : "agentic with a human in the loop, not autonomous" (WWDC 2026)

Apple offre un cas de calibration à l'échelle plateforme. La citation de Forbes (John Koetsier, juin 2026) sur les annonces WWDC : "nearly all of this is agentic with a human in the loop, not autonomous — confirmation-gated, privacy-walled, slower by design." Apple ne positionne pas cette friction comme un défaut à corriger mais comme un avantage différenciant face à des agents plus autonomes.

Cette posture est une implémentation de "suggest only" généralisée au niveau OS : Siri propose, déclenche avec confirmation, ne prend pas d'action irréversible sans validation explicite. Le choix est délibéré et s'appuie sur la confiance comme avantage concurrentiel — les utilisateurs font davantage confiance à un système qui demande avant d'agir. C'est une traduction du niveau 3 de Kavcic ("suggest only pour l'impact élevé") élevée en principe de plateforme.

La convergence avec [contraintes-fixed-preferred-exploratory](contraintes-fixed-preferred-exploratory.md) est directe : Apple traite la confirmation humaine comme une règle **fixed** pour toutes les actions conséquentes — non négociable, encodée dans l'architecture, pas dans la documentation.
