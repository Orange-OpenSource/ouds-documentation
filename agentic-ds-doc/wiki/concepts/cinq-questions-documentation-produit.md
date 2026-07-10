---
type: concept
tags: [documentation, design-system, ia, structure, reference, specifications, changelogs, how-to, tasks, framework]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[making-product-docs-work-humans-ai-gerireid]]"
related:
  - "[[geri-reid]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[documentation-lag]]"
  - "[[schema-metadata-composant]]"
  - "[[design-system-as-infrastructure]]"
  - "[[readable-vs-usable-token]]"
  - "[[gouvernance-design-system-ia]]"
---

## Les cinq questions de la documentation produit

[[geri-reid]] propose dans [[making-product-docs-work-humans-ai-gerireid]] un cadre de structuration de la documentation produit fondé sur cinq questions. L'argument de départ : les frameworks existants (Diátaxis, arc42) ne couvrent pas la réalité des équipes produit. Les composants de design system, l'architecture des design tokens, les matrices d'ownership, les tickets Jira, les release notes — rien de tout cela ne rentre naturellement dans les catégories "tutorials / how-to guides / reference / explanation" de Diátaxis. Ce ne sont pas des guides utilisateurs. Ils documentent des systèmes, des décisions, de l'ownership, du travail.

La solution proposée : chaque document qu'une organisation produit répond principalement à l'une de ces cinq questions, et identifier laquelle clarifie le but du document, accélère la consultation, et rend le contenu plus interprétable par les machines.

## Question 1 : Que existe-t-il ? — Référence

La documentation de référence décrit les choses. C'est une ressource de consultation, pas d'instruction. Dans une organisation produit, cela couvre les catalogues de composants, les props, les endpoints API, les structures d'équipe, les matrices RACI. L'articulation dual-audience est directe : pour les humains, c'est la recherche rapide — trouver ce qui existe sans demander autour. Pour les machines, c'est la base des définitions sur laquelle un agent peut raisonner correctement. "AI tools rely on clear definitions to answer questions accurately." ([[geri-reid]])

La référence est la fondation : on ne peut pas définir des règles ni écrire des guides sans avoir d'abord défini ce qui existe.

## Question 2 : Quelles sont les règles ? — Spécifications

Les spécifications définissent les contraintes, les comportements, les standards. Si la référence dit ce qui existe, les spécifications disent comment les choses doivent se comporter. Dans les équipes produit : les conventions de nommage, l'architecture des design tokens, les standards d'accessibilité technique, les schémas d'API. Pour les humains, les specs réduisent l'ambiguïté et accélèrent l'alignement. Pour les machines, elles fournissent les règles que les agents peuvent appliquer pour générer des outputs conformes.

La formulation de Reid est précise : "Specifications turn decisions into infrastructure. Once written, they guide behaviour across teams and systems." C'est la même logique que [[concevoir-les-conditions]] appliquée à la couche documentation : encoder les décisions pour qu'elles guident le comportement sans intervention humaine répétée.

Ce type documentaire est directement lié aux [[schema-metadata-composant]] et aux [[intent-token]] du corpus existant — les spécifications au sens de Reid sont la forme en prose et en structure de ce que les métadonnées encodent de façon formelle.

## Question 3 : Que doit-on faire ? — Tâches

Les tâches sont souvent négligées comme documentation, mais elles capturent l'intent et enregistrent les décisions là où le travail se passe. Tickets Jira, checklists d'implémentation, task lists. Pour les humains, une tâche bien rédigée réduit les questions de clarification. Pour les machines, les tâches structurées permettent l'automatisation — un agent peut résumer, prioriser, ou générer des actions de suivi. "Tasks are documentation in motion."

## Question 4 : Comment faire quelque chose ? — How-to guides

Les how-to guides sont certains des documents les plus consultés. Déployer en production, configurer un environnement de développement, tester avec un lecteur d'écran, créer un nouveau composant. Pour les humains, ils permettent l'autonomie. Pour les machines, les étapes structurées sont interprétables et réutilisables. Ils transforment le savoir tacite en processus répétable.

## Question 5 : Que s'est-il passé ? — Changelogs

Les changelogs capturent l'histoire et préservent la mémoire institutionnelle. Changelogs produit, changelogs design system, release notes, Architecture Decision Records. Pour les humains, ils fournissent le contexte et la traçabilité — comprendre quand quelque chose a changé et pourquoi. Pour les machines, ce sont des données historiques structurées, cherchables, résumables, analysables.

La connexion avec [[gouvernance-design-system-ia]] est directe : les changelogs sont la mémoire de la gouvernance. Un système qui n'a pas de changelog perd ses décisions architecturales dans le temps — elles deviennent de la convention implicite, invisible aux agents.

## Le dual-audience comme principe unificateur

Reid formule l'insight central de l'article en une phrase : "The interesting part is that the same things that make documentation more accessible for people also make it more useful for AI. Clear structure. Plain language. Accessible formats." C'est une observation qui manquait au corpus du vault, lequel traite généralement la lisibilité machine comme une propriété supplémentaire à ajouter à la documentation humaine existante (annotations, métadonnées JSON, DTCG). Reid inverse le regard : ce n'est pas un surcoût — c'est la même ambition, pour deux audiences simultanées.

La formulation de terrain : "Companies are investing heavily in AI. This feels like our chance to quietly make documentation better for everyone." L'investissement IA devient le prétexte politique pour régler un problème structurel qui existait bien avant les agents.

## Limite du cadre Diátaxis pour les équipes produit

Reid identifie le gap pratique des frameworks existants : Diátaxis (tutorials / how-to guides / reference / explanation) est conçu pour la documentation logicielle et open source. Il ne couvre pas les artefacts quotidiens des équipes produit — component specs, token architecture, ownership matrices, tickets, changelogs. Ces documents "ne comptent pas vraiment comme documentation au sens de Diátaxis" mais sont pourtant centraux à la base de connaissance d'une organisation. Les cinq questions comblent ce gap sans remplacer Diátaxis — elles opèrent à un niveau de granularité différent, plus proche de la pratique produit.

## ⚡ Tension : framework générique vs infrastructure formelle

Le cadre des cinq questions est délibérément générique et accessible — il s'adresse à des équipes produit qui n'ont pas encore de documentation structurée, pas à des équipes avancées avec un MCP actif et des métadonnées DTCG. La limite est l'inverse de celle documentée dans [[readable-vs-usable-token]] : là où ce corpus souligne que beaucoup de systèmes sont machine-readable sans être agent-usable, Reid s'adresse à des équipes qui ne sont pas encore machine-readable du tout. Les deux cadres sont complémentaires sur l'axe de maturité : Reid pour les premières étapes de structuration, le corpus existant pour les étapes avancées d'optimisation agentique.
