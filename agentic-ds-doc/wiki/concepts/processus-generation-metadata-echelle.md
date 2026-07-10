---
type: concept
tags: [design-system, metadata, processus, ia, documentation, echelle, pipeline, indeed]
created: 2026-06-17
updated: 2026-06-22
sources:
  - "[[design-system-documentation-as-structured-metadata]]"
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[how-to-automate-design-system-documentation]]"
  - "[[typeform-design-system-documentation-scale-ai]]"
related:
  - "[[schema-metadata-composant]]"
  - "[[trois-couches-composants-agents]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[cristian-morales-achiardi]]"
  - "[[diana-wolosin]]"
---

## Processus de génération de métadonnées à l'échelle

Générer des fichiers de métadonnées pour l'ensemble des composants d'un design system semble être un effort colossal. [[cristian-morales-achiardi]] propose un processus en 5 étapes qui s'appuie sur l'IA pour l'extraction et les scripts pour les parties mécaniques, en partant du principe que la connaissance existe déjà — il s'agit de la rendre explicite, pas de la créer ([[design-system-documentation-as-structured-metadata]]).

## Étape 1 : Auditer la documentation existante

Recenser où vit la connaissance du design system : Storybook et docs, descriptions et annotations Figma, pages Notion/Confluence, commentaires de revues de code (les patterns qu'on corrige en boucle), conversations Slack ("quand utiliser X plutôt que Y ?"). Collecter les URLs, exporter les docs, réunir les exemples. L'objectif est un inventaire, pas une création.

## Étape 2 : Créer un template de métadonnées

Définir la structure du [[schema-metadata-composant]] dans un fichier template avec des commentaires inline expliquant ce que chaque champ doit contenir. Ce template devient le contrat : toute la génération en découlera.

## Étape 3 : Laisser l'IA extraire et peupler

Pointer un agent IA sur la documentation existante avec le template en main. Prompt type : "Lis [URL Storybook du composant Button]. Extrais ces informations et peuple le template de métadonnées : nom et description depuis la page du composant, cas d'usage depuis la section 'When to use', anti-patterns depuis les sections 'Avoid' ou 'Don't', variantes depuis le tableau des variants, props depuis la doc API, notes d'accessibilité depuis la section a11y." L'IA lit la prose et produit du JSON ou du TypeScript structuré. On révise et raffine.

## Étape 4 : Scripts pour les extractions mécaniques

Pour les champs techniques (props, types), écrire des scripts qui parsent les fichiers composants : extraire les interfaces TypeScript → section `props`, parser les commentaires JSX → champ `description`, détecter les imports → `composition.nestedComponents`, lire l'historique git → timestamps `created` et `modified`. Les scripts gèrent l'extraction mécanique. Les humains ajoutent l'intent de design.

## Étape 5 : Itérer et raffiner

Le premier composant est lent — on apprend ce qui compte, on fait émerger les patterns. Ensuite la cadence s'accélère. Stratégie différenciée : extraction IA pour les composants avec une documentation riche dans Storybook/Figma, traduction manuelle pour les composants complexes nécessitant de la nuance, scripts pour les opérations batch sur les champs techniques.

## Ce que ça implique

Le processus confirme l'argument central : ce n'est pas du travail de documentation additionnel, c'est une traduction. La connaissance existait. L'effort est de changer son format, non de la produire. Et comme [[romina-kavcic]] le note dans un contexte similaire ([[design-system-most-important-asset-ai-era]]), écrire 554 descriptions de composants peut tenir en une session avec l'IA.

## Le pipeline Figma → docs (Kavcic)

[[romina-kavcic]] documente une variante du processus de génération appliquée non pas aux métadonnées machines mais à la documentation humaine ([[how-to-automate-design-system-documentation]]). Voir [[pipeline-figma-docs-automatise]] pour le détail complet. La différence principale avec le processus de Morales Achiardi est la source (Figma via MCP plutôt que Storybook/Notion) et la sortie (fichiers MDX pour documentation humaine plutôt que JSON pour agents IA). Les deux partagent le même principe : l'extraction automatisée depuis les sources existantes évite le travail de production manuelle.

## Pipeline Typeform : Notion comme source, trois destinations

[[fernando-coelho]] chez Typeform documente une variante encore différente ([[typeform-design-system-documentation-scale-ai]]) : la source n'est pas Storybook/Figma ni MDX mais Notion, converti en Markdown via l'API Notion. Ce Markdown alimente trois destinations simultanément — documentation (Docusaurus), MCP server, et Sandbox. Un package de code snippets partagé garantit la cohérence des exemples de code entre les trois destinations.

La différence principale avec les pipelines de Morales Achiardi et Wolosin : l'optimisation n'est pas pour la précision agentique (JSON) mais pour la contribution humaine (Notion comme interface familière). Le Markdown produit est lisible par les agents, mais pas dans le format optimal — c'est un compromis délibéré qui résout d'abord le problème de contribution avant le problème de format. Voir [[notion-cms-design-system]] et [[pipeline-multi-destinations]].

## Pipeline Indeed : régénération automatique

[[diana-wolosin]] documente un pipeline de génération en production chez Indeed ([[machine-readable-design-systems-designing-for-ai-as-a-user]]) qui résout le problème de la maintenance des métadonnées. Le pipeline : documentation MDX → 4 parsers JavaScript (un par domaine : accessibilité, développement, localisation, design) → fusion en 1 JSON par composant → ingestion dans Vectra (base vectorielle open source) → service via MCP.

La propriété clé : **le pipeline se relance automatiquement à chaque mise à jour de documentation par un maintainer**. Les métadonnées servies par le MCP sont donc toujours fraîches — sans action manuelle. C'est la résolution concrète du problème de synchronisation entre documentation humaine et métadonnées machines. En production sur 77 composants, le pipeline a produit 4 300 prototypes en 4 mois sans intervention manuelle sur les métadonnées.
