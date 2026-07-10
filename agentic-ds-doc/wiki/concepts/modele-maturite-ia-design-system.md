---
type: concept
tags: [design-system, ia, maturite, gouvernance, documentation, patterns, taxonomie]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-systems-that-document-ai]]"
  - "[[ai-ready-design-system-olha-bondar]]"
related:
  - "[[romina-kavcic]]"
  - "[[systeme-de-design-agentique]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[quatre-regles-ia-ux]]"
  - "[[deux-lectures-du-design-system-ia]]"
  - "[[protocole-arc]]"
  - "[[contraintes-fixed-preferred-exploratory]]"
  - "[[grammaire-composition-composants]]"
updated: 2026-06-30
---

## Modèle de maturité IA des design systems

[[romina-kavcic]] établit une taxonomie en cinq niveaux à partir de l'analyse de 156 design systems publics, dont 26 seulement documentent l'IA ([[design-systems-that-document-ai]]). Le modèle décrit comment les systèmes progressent dans leur prise en charge des fonctionnalités IA destinées aux utilisateurs humains — ce qui est une dimension distincte de la question de l'IA *opérant* le design system (voir [[deux-lectures-du-design-system-ia]]).

## Niveau 0 — Aucune couche IA

130 systèmes sur 156 (83 %) n'ont aucun composant, token, guideline, ni documentation dédiés à l'IA. Ce n'est pas nécessairement un retard ; certaines équipes ont fait un choix délibéré de ne pas documenter prématurément des patterns encore instables. Mais la majorité reflète simplement l'absence de priorité.

## Niveau 1 — L'IA comme décoration

Le premier niveau d'engagement : créer un langage visuel distinctif pour les fonctionnalités IA. Rôles de couleur spéciaux, tokens nommés, styling réservé. Shopify Polaris en est l'exemple canonique avec le rôle de couleur "Magic" et le token `--p-color-bg-surface-magic` — une teinte irisée appliquée aux surfaces IA. L'IA est visible, signalée, différenciée visuellement. Mais le système ne documente pas encore son comportement.

Ce niveau répond à la première des [[quatre-regles-ia-ux]] ("marquer toujours") sans aller plus loin. Il encode la reconnaissance sans encoder la compréhension.

## Niveau 2 — L'IA comme composant

L'étape suivante : créer un ou plusieurs composants dédiés, réutilisables à travers le système. IBM Carbon en est l'exemple le plus documenté : un label "AI" standardisé couplé à un popover d'explicabilité, déployé sur 13 composants différents dans le système. Le composant porte à la fois la signalisation et la couche d'explication — deux des quatre règles encodées dans un artefact.

La valeur de niveau 2 est la réutilisabilité : au lieu que chaque équipe implémente sa propre solution de labeling IA, le composant devient le point de cohérence. Toute évolution du pattern (formulation du label, contenu du popover, états d'accessibilité) se propage automatiquement.

## Niveau 3 — L'IA comme pattern d'interaction

Au niveau 3, le système ne se contente plus de définir comment *paraît* l'IA, mais comment elle *se comporte*. Atlassian documente les différences comportementales entre les modes : suggest (l'IA propose, l'humain valide), respond (l'IA répond à une requête), handoff (l'IA transfère le contrôle). Ces distinctions impliquent des guidelines de contenu (formulations d'invitation vs de résultat), des patterns d'interaction différenciés (accepter/rejeter vs libre texte), et des états différents selon le mode.

C'est le niveau où la [[quatre-regles-ia-ux|règle "humain en contrôle"]] devient documentée explicitement : quelle forme prend le consentement selon la criticité de l'action, comment est rendu le undo, quel est le niveau de consentement minimum pour déclencher une action IA irréversible.

## Niveau 4 — L'IA comme couche de gouvernance

Microsoft Fluent 2 atteint un niveau que aucun autre système du corpus n'a encore formalisé : une rubrique Responsible AI (RAI) intégrée directement au design system. Cette rubrique évalue chaque feature IA avec des notes par lettre et des critères d'auto-fail — des conditions qui, si non remplies, bloquent le passage à la production indépendamment des autres critères.

C'est l'instance la plus avancée du [[gouvernance-design-system-ia|value gate]] : non pas une liste de recommandations, mais un mécanisme de contrôle formel encodé dans le système lui-même. La gouvernance n'est plus une activité parallèle au design — elle est architecturalement intégrée.

Le parallèle avec [[existence-vs-intent-violations]] est direct : la rubrique RAI de Fluent 2 fait pour les fonctionnalités IA ce que l'auditeur de tokens v2 fait pour les tokens — elle vérifie non pas si les éléments existent, mais s'ils correspondent à leur intent de design.

## Niveau 5 — L'IA comme infrastructure du système

Le niveau le plus avancé observé dans le corpus : l'IA n'est plus une couche spécialisée du design system mais une dimension transversale de son infrastructure. Microsoft Fluent documente des Copilot UI Kits complets couvrant Web, iOS et Android — un tier entier de l'offre système dédié aux interfaces IA.

La différence avec les niveaux précédents est l'exhaustivité architecturale. Le niveau 5 implique un cycle de vie complet : gouvernance des patterns, composants multi-plateformes, guidelines d'interaction, documentation des anti-patterns, exemples de code prêts à l'emploi, notes d'accessibilité. L'IA est traitée comme n'importe quel autre domaine d'interface (formulaires, navigation, data visualisation) — avec la même rigueur systématique.

## Ce que le modèle éclaire

La distribution réelle — 83 % au niveau 0 — montre que la majorité des organisations n'a pas encore engagé le sujet. Parmi les 17 % qui l'ont fait, la progression du niveau 1 au niveau 5 correspond à une progression de l'esthétique vers la gouvernance : d'abord signaler (couleur), puis unifier (composant), puis structurer (pattern), puis contrôler (gouvernance), puis intégrer (infrastructure).

Cette progression est analogue à celle du [[protocole-arc]] pour les design systems agentiques : d'abord consommer, puis auditer, puis composer. Les deux modèles décrivent une montée en maturité qui passe par des seuils qualitatifs, pas de simples améliorations incrémentales.

## Un troisième axe : la maturité d'opérabilité agent (Bondar, 2026)

[[ai-ready-design-system-olha-bondar]] introduit un troisième modèle de maturité, orthogonal aux deux précédents. Là où le modèle Kavcic mesure la documentation des features IA pour les humains, et le [[protocole-arc]] mesure la capacité de l'IA à opérer et gouverner le système, le modèle Bondar mesure la capacité du système à être *interprété et exécuté* par un agent pour produire de l'interface :

**Niveau 0 — Visual library** : couleurs, icônes, composants. L'IA peut imiter le style visuel mais doit inventer les décisions d'implémentation. La grande majorité des équipes se trouvent ici.

**Niveau 1 — Structured system** : fondations en tokens, nommage cohérent, documentation basique. L'IA localise les ressources mais les décisions produit restent ambiguës.

**Niveau 2 — Connected system** : composants design mappés aux composants production, tokens connectés au code. L'IA réutilise des ressources réelles au lieu de les recréer. Bondar estime que "la plupart des équipes se trouvent entre les niveaux 1 et 2."

**Niveau 3 — Operational system** : règles de composition ([[grammaire-composition-composants]]), patterns produit, exemples, guidance de contenu structurée, validation. Les agents peuvent implémenter des tâches d'interface complètes et recevoir un feedback quand ils violent le système.

**Niveau 4 — Agentic system** : workflows bout en bout contrôlés — retrieve requirements → select patterns → generate design and code → run tests → inspect failures → correct → create reviewable change → record which system decisions were used. Les humains restent responsables du jugement produit et de l'approbation.

La différence structurelle avec les modèles précédents est l'unité de mesure : non pas "l'IA est-elle documentée ?", ni "l'IA peut-elle gouverner le système ?", mais "l'agent peut-il produire de l'interface correcte à partir du système ?" — Discover → Understand → Select → Compose → Implement → Validate → Explain. La tripartition [[contraintes-fixed-preferred-exploratory]] est l'outil de calibration qui accompagne ce modèle.

## ⚡ Tension / Contradiction

Le modèle de maturité Kavcic décrit ici mesure la maturité dans la documentation des fonctionnalités IA pour les humains. Le [[protocole-arc]] mesure la maturité dans l'usage de l'IA pour opérer le design system lui-même. Le modèle Bondar mesure la capacité d'opérabilité du système par un agent. Un système peut être au niveau 5 du premier modèle, au niveau 3 du second, et au niveau 1 du troisième — les trois axes sont indépendants. La confusion entre ces axes est précisément ce que [[deux-lectures-du-design-system-ia]] cherche à dissoudre.
