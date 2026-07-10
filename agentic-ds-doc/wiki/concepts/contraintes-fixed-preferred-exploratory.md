---
type: concept
tags: [design-system, agentique, ia, gouvernance, contraintes, autonomie, génération]
created: 2026-06-30
updated: 2026-06-30
sources:
  - "[[ai-ready-design-system-olha-bondar]]"
related:
  - "[[gouvernance-design-system-ia]]"
  - "[[niveaux-confiance-actions-agentiques]]"
  - "[[systeme-de-design-agentique]]"
  - "[[protocole-arc]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[concevoir-les-conditions]]"
---

## Contraintes fixed / preferred / exploratory

La tripartition fixed / preferred / exploratory est un cadre de calibration de l'autonomie des agents IA dans un design system. Elle répond à une tension fondamentale : sans contraintes, l'IA génère de l'incohérence ; avec des contraintes totales, elle génère des produits répétitifs. Le cadre distingue trois régimes selon le degré de liberté accordé ([[ai-ready-design-system-olha-bondar]]).

## Les trois régimes

**Fixed** désigne les règles que l'agent doit suivre sans exception. Ce sont les invariants du système — les décisions dont la violation produirait une défaillance de sécurité, d'accessibilité, ou de cohérence fondamentale. Exemples : les exigences d'accessibilité (rôle ARIA, focus management, contraste), l'usage des tokens sémantiques (pas de couleur codée en dur quand un token existe), les imports de composants de production (pas de réimplémentation locale d'un composant existant), le comportement des actions destructives (toujours une confirmation explicite). Ces règles sont candidates à l'automatisation : elles peuvent être encodées dans un linter ou un test de régression.

**Preferred** désigne l'approche par défaut, applicable sauf raison explicite de dévier. Ce sont les patterns recommandés qui couvrent la grande majorité des cas sans les contraindre tous. Exemples : la composition standard d'une page de settings, l'espacement recommandé entre sections, la structure de contenu habituelle pour un état vide. Un agent peut dévier d'une règle preferred à condition de le justifier — ce qui rend la déviation traçable et délibérée plutôt qu'accidentelle.

**Exploratory** désigne les zones où la variation est intentionnellement permise. Ce sont les espaces où la génération libre apporte de la valeur sans menacer la cohérence systémique. Exemples : les pages de campagne marketing, les compositions éditoriales, l'exploration de nouveaux patterns d'interaction, les prototypes précoces. Un agent opérant en zone exploratory peut composer librement — la contrainte est levée, pas oubliée.

## Pourquoi la distinction est opérationnellement importante

La confusion entre les trois régimes est une source fréquente d'échec dans les workflows agentiques. Traiter une règle preferred comme fixed bloque des décisions légitimes et force les équipes à contourner le système. Traiter une règle fixed comme preferred ouvre la porte à des violations d'accessibilité ou de cohérence qui passent inaperçues dans la génération à grande échelle.

La tripartition rend la distinction explicite et machine-lisible — l'agent peut interroger le régime d'une règle avant de décider s'il peut dévier. C'est une forme de [[gouvernance-design-system-ia|gouvernance encodée]] plutôt que mémorisée.

## Relation avec les [[niveaux-confiance-actions-agentiques]]

Les niveaux de confiance des actions agentiques ([[niveaux-confiance-actions-agentiques]]) et la tripartition fixed/preferred/exploratory sont deux grilles orthogonales qui se combinent. Un agent peut opérer sur une règle fixed (haute confiance requise) ou une règle exploratory (faible confiance suffisante). La grille de confiance décrit le niveau de supervision nécessaire pour exécuter une action ; la tripartition décrit le degré de liberté accordé pour la décider.

## Relation avec [[architecture-skills-rules-instructions]]

Le cadre rejoint l'architecture skills/rules/instructions dans sa logique de séparation : les principes opérationnels durables (fixed) appartiennent aux règles globales, les approches recommandées (preferred) peuvent être encodées dans des skills ou des instructions de tâche, et les zones exploratory définissent les espaces où aucune règle n'est invoquée. La tripartition peut donc servir de grille de classification pour décider où encoder chaque décision de design system.

## ⚡ Tension / Contradiction

Le cadre postule qu'il est possible de classifier chaque règle dans l'un des trois régimes — mais en pratique, la frontière entre fixed et preferred est souvent contestée. Ce qui est "non négociable" pour l'équipe d'accessibilité peut être "recommandé avec exceptions" pour l'équipe produit. La tripartition est un outil de clarification des désaccords autant qu'un schéma de classification — son utilité réelle dépend de la capacité de l'organisation à s'accorder sur les frontières.
