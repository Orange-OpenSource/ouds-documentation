---
type: concept
tags: [design-system, composants, context, ia, tokens]
created: 2026-06-17
updated: 2026-06-29
sources:
  - "[figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)"
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
related:
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[intent-token](intent-token.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
---

## Composants context-aware

Un composant context-aware est un composant dont le comportement attendu — token utilisé, règles d'usage, contraintes de composition — varie selon le contexte dans lequel il est instancié. C'est l'une des propriétés centrales d'un [systeme-de-design-agentique](systeme-de-design-agentique.md) : le même composant ne se comporte pas de la même façon selon où il vit dans le produit.

## Exemple : Button dans trois contextes

[romina-kavcic](../entities/romina-kavcic.md) illustre cela avec Button instancié dans trois contextes différents ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)) :

Dans un **alert** : utiliser `bg-danger`. Intent : action destructive. Toujours associer à un bouton Cancel.
Dans une **card** : utiliser `bg-neutral`. Intent : action secondaire. Ne pas concurrencer les CTAs de la page.
Dans la **navigation** : utiliser `bg-brand`. Intent : action de conversion. Un seul par barre de navigation maximum.

Même composant, trois specs différentes. Ce n'est pas une ambiguïté — c'est de la précision contextuelle.

## Exemple : Accordion dans trois produits

Le même composant Accordion produit de la documentation différente selon son contexte : dans une FAQ, les headers sont formulés en questions ("Comment réinitialiser mon mot de passe ?"). Dans Settings, ils sont formulés en noms ("Paramètres de notification"). Dans Checkout, ils suivent une troisième logique.

L'agent peut générer automatiquement ces trois documentations s'il sait dans quel contexte produit le composant est instancié. En analysant 34 instances d'Accordion sur 6 produits, un agent peut inférer les patterns, générer des exemples do/dont, et prioriser la documentation par criticité business (un composant présent sur la homepage et le checkout est plus critique qu'un composant uniquement dans l'admin).

## Ce que ça implique pour la documentation

La documentation context-aware n'est pas une documentation plus longue — c'est une documentation structurée par contexte de déploiement. Elle nécessite de mapper quelles pages représentent quels produits, puis de laisser l'agent inférer le reste. C'est un investissement en cartographie (la [knowledge-graph-design-system](knowledge-graph-design-system.md)) qui débloque une génération de documentation quasi-automatique.

## Context-awareness au niveau de la taxonomie : Button vs Navigation button (OUDS)

La description du Button OUDS ([figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)) encode un exemple de context-awareness à un niveau rarement documenté : la séparation taxonomique. "Button should be used only to trigger actions or events. Do not use it for navigation purposes — use Navigation button instead." Cette règle ne dit pas "utiliser Button différemment selon le contexte" — elle dit "deux contextes différents = deux composants différents."

C'est une décision architecturale sur où tracer la frontière entre composants plutôt qu'une règle d'usage interne à un composant. L'OUDS a choisi de séparer Button (actions) et Navigation button (directionalité dans un flux) en deux `component_set` distincts plutôt que d'ajouter un variant "navigation" au composant Button. Pour un agent, cette séparation est plus claire qu'un système à variantes car elle élimine une décision de sélection : il n'y a pas de "Navigation button intent dans un Button" à déduire — c'est un composant différent avec son propre point d'entrée.

Le pendant de cette clarté taxonomique est la multiplication des `component_set` dans la bibliothèque — un coût de maintenance que les équipes plus petites peuvent ne pas vouloir payer. La décision de séparer les composants est elle-même context-aware : elle dépend de l'échelle du système et du nombre de consommateurs.
