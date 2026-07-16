---
type: concept
tags: [design-system, agents, specs, documentation, mcp, figma, accessibilite, uber]
created: 2026-06-24
updated: 2026-06-29
sources:
  - "[uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md)"
  - "[figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)"
related:
  - "[pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[skills-avant-mcp](skills-avant-mcp.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[accessibilite-continue](accessibilite-continue.md)"
  - "[documentation-lag](documentation-lag.md)"
  - "[ian-guisard](../entities/ian-guisard.md)"
---

## Génération de spec agentique

La génération de spec agentique est une variante de l'automatisation de la documentation dans laquelle un agent IA produit des pages de spécifications structurées — anatomie du composant, documentation API, annotation de tokens, règles d'accessibilité — directement dans l'outil de design (Figma), en lisant les données réelles du composant via MCP plutôt qu'en transcrivant manuellement.

À distinguer du [pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md), qui synchronise une documentation narrative (MDX, Mintlify) à destination des équipes. La génération de spec agentique produit des artefacts de design formels — à destination des ingénieurs qui vont implémenter le composant — et écrit directement dans le fichier Figma.

## Le problème résolu

Le [documentation-lag](documentation-lag.md) sur les specs de composants est plus sévère que sur la documentation narrative : une spec doit être exhaustive (chaque propriété, chaque état, chaque token, chaque valeur d'accessibilité par plateforme), précise (aucune ambiguïté tolérée pour un ingénieur qui implémente), et à jour (une spec obsolète génère du code incorrect directement). À l'échelle d'Uber — des centaines de composants sur 7 stacks d'implémentation — le maintien manuel des specs est structurellement impossible sans dérive ([uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md)).

## L'architecture à deux couches

La solution d'[ian-guisard](../entities/ian-guisard.md) chez Uber (uSpec) repose sur une séparation entre ce que la machine peut calculer et ce que le LLM doit interpréter.

La couche déterministe — le [mcp-model-context-protocol](mcp-model-context-protocol.md) (Figma Console MCP, open-source, développé par Southleft) — connecte l'agent à Figma Desktop via WebSocket local. Elle crawle la structure arborescente des composants, extrait les tokens nommés, les variables, les variantes, les sous-composants. Ce que cette couche renvoie est exact : le nom du token est le vrai nom du token dans Figma, pas une hallucination. Aucune donnée propriétaire ne quitte le réseau local — propriété critique en contexte enterprise.

La couche interprétative — les agent skills — porte la connaissance métier. Chaque section de spec correspond à un skill distinct, chargeant ses propres règles de validation, ses schémas structurés, et sa documentation de référence. Le skill "screen reader" charge les APIs d'accessibilité de VoiceOver, TalkBack et ARIA avant d'analyser le composant ; il sélectionne depuis des APIs documentées, il ne devine pas. Comme [ian-guisard](../entities/ian-guisard.md) le formule : "The agent doesn't guess at property names — it selects from documented APIs."

Les plugins programmatiques seuls (sans LLM) extraient les données mais ne les interprètent pas — ils ne peuvent pas décider quel rôle ARIA correspond sémantiquement à un composant. Les LLMs seuls interprètent mais hallucinent les valeurs en l'absence d'accès aux données réelles. uSpec combine les deux.

## Les sections de spec générées

Chaque section est un skill autonome : **Anatomy** (marqueurs numérotés sur l'instance du composant, tableau d'attributs), **API** (propriétés, valeurs, defaults, exemples de configuration), **Properties** (axes de variantes et toggles booléens avec previews d'instances), **Color annotation** (mapping de chaque élément à son design token à travers les états), **Structure** (hauteurs, paddings, espacements à travers les variants de taille et de densité), **Screen reader** (VoiceOver, TalkBack et ARIA en un seul passage).

## Le cas emblématique : la spec screen reader

La section screen reader est l'exemple le plus saillant de ce que l'automatisation débloque. Écrire correctement une spec d'accessibilité multi-plateforme requiert de cross-référencer manuellement les documentations VoiceOver (modificateurs et traits), TalkBack (semantics), et ARIA (rôles et états) — chacune avec des centaines de propriétés, chacune différente. Une erreur dans une propriété signifie une expérience cassée pour les utilisateurs d'assistive technology. ([uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md))

uSpec génère une spec screen reader couvrant les 3 plateformes en moins de 2 minutes. En production chez Uber : ce qui nécessitait des heures de travail par composant est devenu une invocation d'agent. Un système avec des centaines de composants qui demandait des mois de rédaction peut désormais générer des specs complètes en jours.

## Rendu direct dans Figma

L'agent ne produit pas un document intermédiaire : il importe le template de documentation depuis la librairie Figma, le détache, et le peuple directement — textes, tableaux, marqueurs anatomiques — via le MCP. La spec finie apparaît dans le fichier Figma sans étape manuelle de formatage. C'est la propriété distinctive par rapport aux générateurs de documentation classiques qui produisent du Markdown ou du HTML.

## Lien avec la gouvernance de l'accessibilité

La génération de spec agentique est une implémentation de l'[accessibilite-continue](accessibilite-continue.md) au niveau de la documentation plutôt qu'au niveau du linting en temps réel. Là où [accessibilite-continue](accessibilite-continue.md) vérifie la conformité au moment de la création des composants, la génération de spec agentique garantit que la documentation d'accessibilité est complète et à jour pour chaque composant — et qu'un ingénieur qui implémente dispose des bonnes valeurs de propriétés, sur les bonnes plateformes, sans ambiguïté.

## ⚡ Tension : specs générées vs specs révisées

La génération automatique pose une question de responsabilité : si l'agent génère la spec screen reader et qu'une propriété est incorrecte, qui en est responsable ? Le modèle de confiance de [niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md) s'applique : l'agent génère, mais le designer spécialisé valide. [ian-guisard](../entities/ian-guisard.md) reconnaît que "drift detection" et des boucles de vérification sont sur la roadmap de uSpec — ce qui confirme que la génération sans validation reste une demi-solution. La question de qui audite les specs générées par l'agent est ouverte.

## Cas de référence : le frame OUDS Button comme output cible

Le fichier Figma Actions---Button de l'OUDS ([figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)) est un exemple de ce que la génération de spec agentique vise à produire automatiquement. Le frame principal (node 2071:11587) mesure 31 742 × 13 443 px et contient plusieurs colonnes de documentation — une par variante du composant — avec anatomie numérotée, panneaux de propriétés, grilles d'états, et règles de layout. C'est un artefact produit manuellement par l'équipe OUDS, mis à jour le 2026-06-26.

Ce frame illustre deux contraintes concrètes pour un système de génération : (1) la taille — 2,3M de caractères XML en get_metadata, inaccessible sans crawl sélectif — et (2) la forme visuelle — les specs sont dans des tableaux et marqueurs graphiques, pas dans des champs texte structurés. Un système comme uSpec qui écrit directement dans Figma via MCP doit donc anticiper la lecture de ce qu'il produit par d'autres agents qui passeront par le même MCP. La lisibilité-machine de la sortie dépend de la façon dont elle est structurée au moment de la génération.
