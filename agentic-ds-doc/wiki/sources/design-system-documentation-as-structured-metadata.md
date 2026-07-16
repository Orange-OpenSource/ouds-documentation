---
type: source
tags: [design-system, metadata, documentation, ia, schema, composants]
created: 2026-06-17
updated: 2026-06-17
sources: []
related:
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[workflows-ia-metadata](../concepts/workflows-ia-metadata.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## Design system documentation as structured metadata

**Auteur** : [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)
**Publication** : Design Systems Collective (Medium), 9 janvier 2026
**URL** : https://www.designsystemscollective.com/design-system-documentation-as-structured-metadata-315f62c6eab1
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 3
**Fichier brut** : `raw/Design system documentation as structured metadata.md`

---

## Résumé structuré

Article de fond sur la couche 2 des [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md) : les métadonnées de composants. L'argument central est que la documentation structurée comme métadonnées n'est pas une nouvelle documentation — c'est la même documentation, traduite dans un format que les machines peuvent interroger. Aucune connaissance nouvelle n'est créée : on rend explicite et queryable ce qui existait déjà dans Figma, Storybook, Notion, les revues de code, les conversations Slack.

L'article détaille le schéma complet à 9 sections, explique la distinction entre sections critiques pour l'IA (décisions) et sections de complétude (référence), présente le processus de génération en 5 étapes, compare les formats (TypeScript, JSON, Markdown), et décrit les 4 types de workflows que les métadonnées activent.

---

## Thèses principales

**Thèse 1 — Traduction, pas création.** La documentation structurée est une traduction de la documentation existante, pas un effort additionnel. Une règle en annotation Figma, un paragraphe Storybook, un commentaire de code review — c'est le même savoir, encodé différemment. Le metadata file est le quatrième format, optimisé pour les machines.

**Thèse 2 — Structure force la précision.** Un anti-pattern en prose peut rester vague ("évitez les boutons primaires multiples"). Le format metadata exige la précision : un scénario exact, une raison explicite, une alternative concrète. Cette précision profite aussi aux humains (juniors, onboarding).

**Thèse 3 — Deux niveaux de lecture pour la performance.** La séparation Header (discovery) / Body (intent) permet aux agents de scanner les headers de tous les composants pour identifier les candidats, puis de lire le détail uniquement des composants pertinents. Optimisation du coût en tokens.

**Thèse 4 — Les métadonnées activent 4 workflows.** Sélection de composants, graphes de relations, validation de code généré, génération de code. Ce sont des workflows distincts, tous alimentés par le même fichier de métadonnées.

---

## Citations clés

> "Component metadata isn't new documentation. It's the same documentation, translated to a machine-readable domain."

> "It's not about creating new documentation. It's about reformatting existing knowledge."

> "Every component has decisions baked in. Decisions that live in Figma, Storybook, Notion, team memory. Component metadata is how we make those decisions explicit and queryable."

> "The structure forces precision." (à propos des anti-patterns)

---

## Connexions identifiées

Développe en profondeur la couche 2 de [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md). Complète [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) avec l'argument de la traduction (pas de création). Les 4 workflows activés par les métadonnées font écho à [protocole-arc](../concepts/protocole-arc.md) phases 1 et 2. La validation pre-génération (vérification des anti-patterns avant de générer du code) opérationnalise [user-vs-maintainer-ia](../concepts/user-vs-maintainer-ia.md).
