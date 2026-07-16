---
type: concept
tags: [design-system, composants, metadata, index, raisonnement, ia]
created: 2026-06-17
updated: 2026-06-22
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)"
  - "[agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)"
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
related:
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[composants-context-aware](composants-context-aware.md)"
  - "[intent-token](intent-token.md)"
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[format-toon](format-toon.md)"
  - "[protocole-arc](protocole-arc.md)"
  - "[schema-metadata-composant](schema-metadata-composant.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
---

## Les trois couches pour rendre les composants lisibles par un agent

[romina-kavcic](../entities/romina-kavcic.md) identifie trois couches d'information qu'un design system doit exposer pour qu'un agent IA puisse l'utiliser de manière fiable ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)). La majorité des design systems aujourd'hui ont une partie de la première, peu de la seconde, et presque rien de la troisième.

## Couche 1 : L'index

L'index répond à la question : **qu'est-ce qui existe, qu'est-ce qui utilise quoi, qu'est-ce qui dépend de quoi ?**

C'est la carte relationnelle du système. L'agent y apprend que le composant Dialog existe, que Button a 4 variantes, qu'Alert est lié à Dialog et à Button. Sans index, l'agent est aveugle — il ne sait même pas ce qui est disponible. C'est le niveau le plus élémentaire, et pourtant encore incomplet dans beaucoup de systèmes.

## Couche 2 : Les métadonnées

Les métadonnées répondent à la question : **comment et pourquoi utiliser ce composant ?**

C'est la couche d'intent. Une description de composant bien écrite pour Button dira : "utilise la variante destructive pour les actions irréversibles, toujours associée à une option d'annulation." Cette phrase unique est ce qui permet à l'agent de savoir qu'une confirmation de suppression nécessite un bouton Cancel en plus du bouton d'action. Sans métadonnées, l'agent sait que les composants existent mais pas quand les utiliser. Voir aussi [intent-token](intent-token.md) pour la même logique appliquée aux tokens.

## Couche 3 : Le raisonnement

Le raisonnement répond à la question : **quelle est la logique de sélection et de composition ?**

C'est le playbook. Pour un dialog de confirmation : Dialog + Alert + deux Buttons. Pour un formulaire de login : Input + Input + Button. Ce sont des règles de composition contextuelles que l'agent peut traverser. Sans cette couche, l'agent assemble des pièces au hasard — il a les ingrédients mais pas la recette.

## État actuel des design systems

La plupart des équipes ont de la couche 1 (une Storybook avec la liste des composants), très peu de couche 2 (des descriptions d'intent structurées), et presque aucune couche 3 (une logique de composition formalisée). C'est le fossé principal à combler pour passer à un [systeme-de-design-agentique](systeme-de-design-agentique.md).

## Implémentation concrète (Morales Achiardi)

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) donne une implémentation concrète de ces trois couches dans [towards-agentic-design-system](../sources/towards-agentic-design-system.md) :

**Couche 1 → Codebase Index** : un fichier `index.toon` en [format-toon](format-toon.md) dans `.ai/`, auto-généré, cartographiant 57 composants et 302 relations. Sous-fichiers : `component-usage.toon`, `dependencies.toon`, `data-flow.toon`.

**Couche 2 → Component Metadata** : un fichier `.metadata.ts` co-localisé avec chaque composant, selon un [schema-metadata-composant](schema-metadata-composant.md) à 9 sections. Les sections critiques pour l'IA sont `usage` (cas d'usage, anti-patterns avec scénario/raison/alternative), `aiHints` (critères de sélection explicites), `variants` (options et intent de chacune), `composition` (contraintes d'imbrication), `behavior` (états, interactions). Les sections de complétude sont `props`, `accessibility`, `examples`. La section `component` forme le header — lue en premier pour la discovery. Le [processus-generation-metadata-echelle](processus-generation-metadata-echelle.md) décrit comment produire ces fichiers à grande échelle en 5 étapes.

**Couche 3 → Query Protocols (CLAUDE.md)** : instructions qui fonctionnent comme des "pilotes système", enseignant à l'agent comment lire l'index plutôt que de deviner les chemins de fichiers. Référencent les règles de composition atomique, les patterns de composition, et les règles d'optimisation de requêtes. L'[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md) détaille comment cette couche 3 se décompose en Skills (capacités exécutables réutilisables), Rules (contraintes passives spécifiques au projet, activées par chemin de fichier), et Instructions stratégiques dans CLAUDE.md (le routeur qui lie les deux).

## ⚡ Tension : une deuxième signification des "trois couches" (Spotify Encore)

L'AI Design Systems Conference 2026 introduit une lecture différente des "trois couches" — non pas les couches d'information exposées à l'agent (index, métadonnées, raisonnement) mais les couches architecturales du composant lui-même ([your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)). L'équipe Spotify Encore a découvert que les agents contournaient Encore pour aller directement sur Cursor, produisant du code non-conforme. Cause diagnostiquée : les définitions monolithiques de composants (props + variants + styles + comportements + accessibilité + guidelines dans un seul bloc) imposent une fenêtre de contexte massive — l'agent doit tout parser pour comprendre une partie.

La réponse de Spotify : trois couches architecturales indépendantes dans la définition du composant :

**Foundation layer** — tokens et primitives. **Style layer** — apparence visuelle. **Behavior layer** — logique d'interaction.

Ces couches sont indépendantes : un agent peut raisonner sur les fondations sans charger les styles, ou prendre les styles d'un composant existant et y adjoindre un comportement custom. Spotify appelle ça des "smaller context bubbles" — des fenêtres de raisonnement autonomes et réduites, en opposition aux blocs monolithiques. Résultat en production : 220 000+ usages de styles partagés (50 % de croissance year-over-year), 93 % de satisfaction développeur.

Cette signification est distincte des trois couches de Kavcic/Morales Achiardi : les deux taxonomies parlent de "couches" mais à des niveaux différents. Kavcic/Morales Achiardi définissent les couches d'*information* que le design system doit exposer à l'agent. Spotify définit les couches d'*architecture interne* du composant qui rendent cette information raisonnable par parties. Les deux sont complémentaires et non substituables.
