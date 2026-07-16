---
type: concept
tags: [gouvernance, design-system, ia, organisation, accountability, decision-rights, politique, plateforme]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md)"
  - "[state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)"
  - "[wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)"
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
related:
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[gouvernance-technique-ia](gouvernance-technique-ia.md)"
  - "[accountability-gap-ia](accountability-gap-ia.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[murphy-trueman](../entities/murphy-trueman.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
---

## Le chantier ouvert

Le corpus technique documenté dans [gouvernance-technique-ia](gouvernance-technique-ia.md) — auditeurs de tokens, contraintes exécutables, niveaux de confiance par action — adresse la gouvernance de ce que les agents *font*. [murphy-trueman](../entities/murphy-trueman.md) dans [design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md) nomme un problème distinct et plus difficile : la gouvernance de ce que les *humains décident*, valident, et dont ils répondent.

La thèse de Trueman : quand l'IA rend la création d'interfaces accessible à tous, le design system technique peut être parfaitement prêt — tokens machine-readable, Code Connect actif, documentation complète — sans que l'organisation soit prête à ce que ça fonctionne. La statistique déclencheuse : 55 % des product builders prennent désormais en charge des tâches hors de leur périmètre habituel (Figma research). Paige Costello (VP Product Figma) formule le résultat : le workflow linéaire a "collapsed". Ce collapse crée une crise de gouvernance organisationnelle que la gouvernance technique ne résout pas.

## Les quatre dimensions non résolues

**Les droits décisionnels.** Qui peut approuver de l'output IA pour la production ? Le seuil change-t-il selon la nature du changement — un contenu vs un nouveau flux utilisateur ? Ces distinctions doivent être établies avant d'avoir la conversation sous pression de deadline. Les équipes qui gèrent le mieux ne sont pas celles avec l'outillage le plus sophistiqué : "They're the ones who got serious about decision rights before AI forced the question." ([design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md))

**Le standard de qualité explicite.** Que signifie "assez bon pour shipper" quand le créateur est un PM avec un prompt plutôt qu'un designer avec des années de craft ? Ce standard vit implicitement dans le jugement collectif de l'équipe. Le rendre explicite — applicable indépendamment de qui a fait la chose — est un travail inconfortable mais nécessaire. Sans cela, le processus de review change de nature : on juge potentiellement la compétence d'un collègue qui a suivi toutes les règles.

**L'accountability pour les failures composites.** L'IA peut assembler des composants accessibles en un parcours inaccessible, des éléments on-brand en une expérience off-brand, des parties techniquement valides en un modèle mental cassé. Ces failures passent tous les contrôles automatiques existants — elles émergent à l'intersection des composants, pas dans chaque composant pris séparément. Qui en est responsable doit être décidé avant que ça arrive. Voir [accountability-gap-ia](accountability-gap-ia.md).

**L'adaptation des modèles de contribution.** Les processus de contribution supposent un humain derrière la requête. Quand l'IA identifie que des équipes combinent trois composants de la même façon, est-ce un pattern à promouvoir ? La boucle de feedback devient circulaire : l'outil qui propose des contributions est aussi l'outil qui génère les données d'usage. "Teams who wait until AI is actively contributing to figure out how to evaluate those contributions will find themselves in reactive chaos." ([design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md))

## La relation avec la gouvernance technique

Les deux dimensions adressent des registres différents. La gouvernance technique contraint ce que l'IA *peut* faire. La gouvernance organisationnelle cadre ce que les humains *décident* de valider et dont ils répondent. Un système peut avoir une gouvernance technique robuste et une gouvernance organisationnelle entièrement absente — c'est précisément la situation décrite dans les données zeroheight : 82 % des équipes utilisent l'IA, 15 % n'ont aucune politique IA ([state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)).

La lacune documentée dans [gouvernance-technique-ia](gouvernance-technique-ia.md) — "Who's accountable for automated updates that go live ?" — est exactement ce que Trueman adresse. Sa réponse n'est pas technique : c'est une décision de gouvernance organisationnelle, à prendre avant d'être sous pression.

## La politique IA comme instrument de gouvernance

Les données sectorielles ([state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)) montrent que **15 % des organisations n'ont aucune politique IA** (23 % dans les petites entreprises). Sans cadre minimal, le [shadow-ia-design-system](shadow-ia-design-system.md) et les pratiques contradictoires se propagent sans friction. Mais les 35 % qui ont une politique formelle "restrictive" illustrent le risque inverse — une politique trop contraignante bloque l'adoption légitime et accélère le contournement.

La politique optimale est légère, orientée partenariat plutôt que contrôle, et couplée à une infrastructure qui rend la compliance naturelle. La gouvernance-par-règles et la gouvernance-par-infrastructure ne sont pas alternatives : les règles orientent la culture, l'infrastructure encode les contraintes.

## Gouvernance par mandat plateforme : le cas Apple WWDC 2026

WWDC 2026 documente une forme de gouvernance design system inédite dans le corpus : le **mandat plateforme**. Apple supprime le mécanisme d'opt-out de Liquid Glass — toute app recompilée avec Xcode 27 adopte automatiquement le nouveau design language, sans action des équipes produit ([wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)).

Ce cas éclaire une limite des modèles de gouvernance documentés dans ce vault (Kavcic, Six, Wolosin) : ils supposent une organisation qui contrôle son propre système. Quand la plateforme impose un changement, le contrôle est partiel. Les tokens sémantiques internes peuvent rester cohérents, mais si le rendu visuel de la plateforme change de façon non-négociable, la cohérence du design system est conditionnelle à la stabilité de la plateforme en dessous.

La convergence avec [concevoir-les-conditions](concevoir-les-conditions.md) reste : les équipes qui ont architecturé leurs tokens de façon sémantique (role-based plutôt que value-based) absorbent mieux un tel changement de plateforme que celles qui avaient hardcodé des valeurs. La gouvernance interne ne protège pas contre les mandats plateforme, mais elle peut réduire le coût de l'adaptation.

## ⚡ Tension : la gouvernance organisationnelle précède la gouvernance technique

Le corpus documente abondamment *comment* encoder la gouvernance dans l'infrastructure. Il documente moins *qui décide* de ce qu'il faut encoder, et selon quelle légitimité. La gouvernance organisationnelle est la condition de possibilité de la gouvernance technique : sans droits décisionnels clairs, sans accountability définie, sans standard de qualité explicite, les contraintes exécutables encodent les décisions du premier arrivé plutôt que les décisions de l'organisation. La gouvernance technique amplifie les décisions organisationnelles — bonnes ou mauvaises.
