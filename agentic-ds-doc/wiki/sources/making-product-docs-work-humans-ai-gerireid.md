---
type: source
tags: [documentation, design-system, ia, structure, dual-audience, framework, product-team, hallucination]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[making-product-docs-work-humans-ai-gerireid]]"
related:
  - "[[geri-reid]]"
  - "[[cinq-questions-documentation-produit]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[documentation-lag]]"
  - "[[ia-comme-nouvelle-recrue]]"
  - "[[schema-metadata-composant]]"
  - "[[design-system-as-infrastructure]]"
---

## Making product documentation work for humans and AI

**Auteur** : [[geri-reid]] | **Publié** : avril 2026 | **Source** : https://gerireid.com/blog/making-product-docs-work-for-humans-and-ai/

## Thèse principale

La documentation d'équipe produit doit désormais servir deux audiences simultanément : les humains et les machines. L'insight clé : ce qui rend la documentation meilleure pour les humains (structure claire, langage simple, formats accessibles) la rend aussi plus utile pour les agents IA. Il n'y a pas de tension entre les deux objectifs — c'est la même ambition. L'investissement IA des organisations devient alors le levier politique pour remettre à plat des pratiques documentaires médiocres qui existaient bien avant les agents.

## Diagnostic : pourquoi la documentation médiocre est maintenant dangereuse

Jusqu'à récemment, les équipes muddlaient avec une documentation médiocre. Les humains sont bons pour contourner les mauvais systèmes — ils demandent sur Slack, cherchent dans les archives. C'est inefficace, mais ça fonctionne à peu près.

Les LLMs ne fonctionnent pas ainsi. Face à une documentation mal structurée, contradictoire, ou obsolète, le modèle "ne reconnaît pas son ignorance. Il trouve des patterns et construit une réponse. Une réponse confiante, bien formatée, complètement fausse, livrée comme un fait." [[geri-reid]] illustre avec un cas personnel : en utilisant l'IA pour écrire de la documentation d'accessibilité sur des composants, le modèle "wildly hallucinated components based on their name" avant qu'une liste de composants approuvés soit fournie.

La distinction avec le corpus existant est nette : [[documentation-lag]] traite le problème en termes de dérive temporelle (le lag entre Figma et la doc). Reid traite le problème en termes d'amplification qualitative : la documentation médiocre *ralentissait* les humains, elle *crée activement des mauvais outcomes* avec les agents. "Your team's messy Confluence space that nobody reads? Suddenly, it doesn't look quite so harmless."

## Le cadre des cinq questions

Reid propose de structurer toute documentation produit autour de cinq questions. Voir [[cinq-questions-documentation-produit]] pour le détail complet.

"What exists?" → Référence (catalogues de composants, props, endpoints API, structures d'équipe, RACI)
"What are the rules?" → Spécifications (conventions de nommage, token architecture, standards d'accessibilité, schémas API)
"What needs to be done?" → Tâches (tickets, checklists, task lists)
"How do I do something?" → How-to guides (déploiement, setup, test avec screen reader, création de composant)
"What changed?" → Changelogs (changelogs produit et design system, release notes, Architecture Decision Records)

La valeur du cadre est opérationnelle : quand un document répond explicitement à l'une de ces questions, son but est plus clair pour l'auteur, la consultation est plus rapide pour les humains, et l'interprétation est plus fiable pour les machines.

## Pourquoi Diátaxis ne suffit pas

Diátaxis (tutorials / how-to guides / reference / explanation) est respecté dans la documentation technique et open source. Mais dans les équipes produit, les artefacts quotidiens — component specs, token architecture, ownership matrices, tickets, changelogs — ne rentrent pas dans ces catégories. "These are not user guides. They document systems, decisions, ownership, and work." Le cadre des cinq questions comble ce gap sans remplacer Diátaxis.

## Citations clés

"The interesting part is that the same things that make documentation more accessible for people also make it more useful for AI. Clear structure. Plain language. Accessible formats." ([[geri-reid]])

"Outdated documentation used to just slow humans down but now it can actively create bad outcomes." ([[geri-reid]])

"Specifications turn decisions into infrastructure. Once written, they guide behaviour across teams and systems." ([[geri-reid]])

"Those boring docs no one reads are quietly becoming infrastructure." ([[geri-reid]])

## Artefact associé

Product Documentation Canvas — une page unique qui mappe les cinq questions sur les types documentaires correspondants. Disponible en PDF sur gerireid.com/images/Product-Documentation-Canvas.pdf. Travail en cours au moment de la publication.

## Connexions au vault

L'article complète [[lisibilite-machine-design-system]] par l'angle dual-audience (même effort, deux audiences) et [[documentation-lag]] par le diagnostic de l'amplification qualitative (médiocre → dangereux). Il fournit un cadre de structuration accessible là où le corpus existant documente des solutions avancées (DTCG, MCP, métadonnées JSON) — les deux opèrent sur des niveaux de maturité différents et sont complémentaires.
