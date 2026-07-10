---
type: concept
tags: [design-system, ia, dataset, données, corpus, scaling, mémoire]
created: 2026-07-08
updated: 2026-07-08
sources:
  - "[[design-system-advantage-is-memory]]"
related:
  - "[[memoire-design-system]]"
  - "[[knowledge-graph-design-system]]"
  - "[[seeds-vs-trees]]"
  - "[[design-system-as-infrastructure]]"
  - "[[inversion-economique-code-comprehension]]"
  - "[[romina-kavcic]]"
---

## Le design system comme dataset

La thèse terminale de [[romina-kavcic]] dans [[design-system-advantage-is-memory]] est une reformulation de ce qu'est un design system dans l'ère agentique : "The design system is no longer the deliverable. It is the dataset."

Ce déplacement n'est pas métaphorique. Il désigne un changement de finalité. Pendant des années, un design system était évalué à la qualité de ses composants, de ses tokens, de sa documentation : ce qu'il livrait aux équipes. Dans un environnement où les agents IA sont des consommateurs permanents du système — pas seulement les designers et les développeurs — la valeur du design system dépend aussi de la qualité du corpus de données qu'il constitue pour ces agents.

## Deux phases, deux rapports aux données

[[romina-kavcic]] distingue deux phases dans la vie d'un design system, qui ont des rapports fondamentalement différents à la question des données.

En phase **0→1** (founding), l'équipe est en mode de survie : faire marcher le système, prouver sa valeur sur quelques composants à fort impact, stabiliser les conventions de nommage, obtenir une première adoption. Les données générées dans cette phase — les essais, les erreurs, les décisions provisoires — sont majoritairement jetables. Ce n'est pas le moment d'investir dans l'indexation ou le graphe.

En phase **1→100** (scaling), la situation est radicalement différente. L'équipe dispose désormais de plusieurs années d'historique : des renommages de tokens avec leurs raisons, des composants dépréciés et les threads qui expliquent pourquoi, des compromis de gouvernance et les conversations qui les ont produits, des rapports de drift sur plusieurs surfaces et marques, des notes de critique qui font apparaître les mêmes angles morts à répétition. C'est la mémoire institutionnelle du design system.

La plupart des équipes 1→100 ont déjà cette mémoire. Elles ne l'ont pas rendue retrievable pour leurs agents.

## Ce que "être un dataset" implique

Traiter le design system comme un dataset change les questions que l'on pose. On ne demande plus seulement "ce composant est-il bien documenté ?" mais "est-ce que la décision qui a conduit à ce composant est dans le corpus ?" On ne demande plus seulement "les tokens sont-ils dans DTCG ?" mais "est-ce que les raisons des renommages sont liées à ces tokens ?" On ne demande plus seulement "la documentation est-elle à jour ?" mais "est-ce que l'agent peut retrouver en une requête pourquoi nous avons abandonné ce pattern il y a deux ans ?"

Cette perspective converge avec [[seeds-vs-trees]] — construire les fondations avant l'automatisation — mais l'approfondit : les fondations ne sont pas seulement l'architecture technique du design system, ce sont aussi les données historiques qui permettent à un agent de raisonner sur ses décisions passées.

## Le dataset comme fossé concurrentiel

[[romina-kavcic]] signale que le "visible 10%" d'un design system (tokens, composants, docs, Figma) est forkable : n'importe quelle organisation peut copier la structure. Ce qui ne peut pas être forké, c'est l'historique des décisions, les raisons des rejections, les critiques qui ont façonné les choix. Ce corpus est propre à chaque équipe et à chaque organisation.

C'est précisément pour cette raison que le dataset constitue un avantage défendable. Les modèles s'améliorent sur la roadmap de quelqu'un d'autre. Le corpus de décisions de l'équipe, lui, ne s'accumule que par le travail de l'équipe. L'investissement dans la retrievability de ce corpus est un investissement à rendement croissant : chaque décision bien documentée et indexée réduit le coût de toutes les sessions futures qui auraient pu toucher le même terrain.
