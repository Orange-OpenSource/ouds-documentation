---
type: concept
tags: [design-system, ia, ux, patterns, règles, gouvernance, convergence]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)"
related:
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[modele-maturite-ia-design-system](modele-maturite-ia-design-system.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[user-vs-maintainer-ia](user-vs-maintainer-ia.md)"
  - "[deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md)"
---

## Les quatre règles convergentes de l'IA UX

[romina-kavcic](../entities/romina-kavcic.md) identifie quatre règles qui ont émergé *indépendamment* dans les design systems d'IBM, AWS, GitLab, Red Hat, SAP, Workday et Apple ([design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)). Ces organisations n'ont pas coordonné leurs approches. Elles ont convergé. La convergence est le signal que ces règles décrivent des contraintes profondes de l'interface IA avec les humains — pas des choix stylistiques.

## La règle préalable : le value gate

Avant les quatre règles, IBM, GitLab, Red Hat et Apple posent toutes la même guideline en premier : la permission de *ne pas utiliser l'IA*. Le droit d'opt-out est le préalable à toute documentation de fonctionnalités IA.

Ce positionnement est révélateur. Ces organisations reconnaissent que l'IA n'est pas toujours la meilleure option, que les utilisateurs doivent pouvoir choisir, et que la crédibilité du système dépend de cette possibilité d'absence. Le value gate n'est pas une mesure défensive — c'est un principe de design : toute feature IA doit être justifiable par la valeur qu'elle apporte, pas par sa présence.

## Règle 1 : Marquer toujours

Toute sortie IA doit être marquée comme telle. Ce marquage prend trois formes : un label texte explicite ("Généré par IA", "Suggestion IA"), un styling réservé (voir [Niveau 1 du modèle de maturité](modele-maturite-ia-design-system.md)), et une iconographie distincte. La règle comporte aussi une contrainte inverse : ne pas sur-marquer. Tout couvrir de labels IA crée une fatigue visuelle qui neutralise le signal.

Le marquage systématique répond à un besoin d'agentivité cognitive : les utilisateurs calibrent leur confiance et leur niveau d'attention différemment selon la source du contenu. Confondre contenu IA et contenu humain, même involontairement, est une forme de manipulation.

## Règle 2 : Expliquer en couches

L'explicabilité n'est pas un écran de documentation — c'est une architecture de révélation progressive. La règle structure l'explication sur trois niveaux : **Quoi** (ce que l'IA a produit), **Pourquoi** (sur quelle base, avec quelle confiance), **Comment** (la mécanique sous-jacente si l'utilisateur en a besoin). Chaque niveau n'est révélé que sur demande, et le niveau de détail révélé est proportionnel aux enjeux de la décision.

IBM Carbon encode ce principe dans son composant : le label IA est la couche de surface (Quoi), le popover d'explicabilité est la couche intermédiaire (Pourquoi), et la documentation complète du modèle est la couche profonde (Comment). Atlassian le structure dans ses guidelines comportementales : la révélation du reasoning s'adapte selon que l'IA suggère une couleur ou supprime un workspace.

## Règle 3 : Humain en contrôle

Toute action IA doit être réversible. L'override doit être toujours disponible. Le niveau de consentement requis avant l'action est proportionnel à sa criticité : pour une suggestion de formulation, l'acceptation implicite suffit ; pour une action destructive ou irréversible, un consentement explicite est obligatoire.

Cette règle fait écho à la distinction [user-vs-maintainer-ia](user-vs-maintainer-ia.md) : même quand l'IA est en position de Maintainer (capable de prendre des décisions systémiques), elle ne doit jamais retirer à l'humain la possibilité de dire non. La criticité détermine le niveau de consentement, pas les préférences de l'équipe produit.

Un pattern documenté dans plusieurs systèmes : la "confirmation graduelle" — pour les actions à faible enjeu, l'IA agit et notifie ; pour les actions à enjeu moyen, l'IA propose et attend validation ; pour les actions à haut enjeu, l'IA expose ses hypothèses et demande confirmation explicite avant même de formuler une proposition.

## Règle 4 : Concevoir l'échec

L'IA échoue différemment des interfaces déterministes. Elle produit des confiances variables, des sorties incertaines, des hallucinations. Concevoir pour l'échec signifie : des états d'erreur explicites (pas de spinner infini, pas de silence), des fallbacks gracieux (si l'IA ne peut pas répondre, que se passe-t-il ?), et des chemins de récupération clairs (l'utilisateur sait comment corriger, réessayer, ou contourner).

Le gap le plus fréquent dans le corpus : la confiance/incertitude. Moins de 5 systèmes sur 26 documentent comment exposer le niveau de confiance d'une sortie IA à l'utilisateur. Pourtant, une suggestion à 60 % de confiance et une suggestion à 95 % de confiance ne devraient pas être présentées identiquement — l'utilisateur a besoin de ce signal pour calibrer sa propre décision.

## Le vrai pattern : 15 questions

Une fonctionnalité IA complètement documentée requiert des réponses à 15 questions : (1) intent utilisateur, (2) déclencheur, (3) input attendu, (4) output produit, (5) comportement système, (6) contrôles utilisateur disponibles, (7) mécanisme de feedback, (8) état d'erreur, (9) confiance et incertitude, (10) explicabilité, (11) accessibilité, (12) données et vie privée, (13) exemples concrets, (14) anti-patterns documentés, (15) notes d'implémentation. La plupart des systèmes du corpus couvrent 3 à 5 dimensions seulement — typiquement le styling (règle 1), un état d'erreur basique (règle 4), et l'override (règle 3 partiellement).

Les dimensions les moins couvertes dans le corpus public : confiance/incertitude, récupération des hallucinations, boucles de correction utilisateur, workflows multi-agents, permissions d'agents. Ces lacunes définissent la frontière de l'état de l'art actuel.

## Ce que la convergence implique

Que ces règles aient émergé indépendamment dans des organisations aussi différentes qu'IBM et Apple, ou SAP et Shopify, suggère qu'elles ne sont pas des choix de design — elles sont des contraintes. Les utilisateurs humains d'interfaces IA ont des besoins cognitifs et éthiques spécifiques qui transcendent les contextes produit. Toute interface qui viole systématiquement l'une de ces règles crée des problèmes de confiance, de compréhension, ou d'agentivité — indépendamment de la qualité de l'IA sous-jacente.
