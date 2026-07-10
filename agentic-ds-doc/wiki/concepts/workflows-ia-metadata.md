---
type: concept
tags: [design-system, metadata, ia, workflows, agents, validation, génération]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-system-documentation-as-structured-metadata]]"
related:
  - "[[schema-metadata-composant]]"
  - "[[protocole-arc]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[knowledge-graph-design-system]]"
---

## Workflows IA activés par les métadonnées de composants

Une fois les fichiers de métadonnées en place, ils alimentent quatre types de workflows distincts, identifiés par [[cristian-morales-achiardi]] ([[design-system-documentation-as-structured-metadata]]). Ces workflows correspondent aux phases du [[protocole-arc]] et opérationnalisent la distinction [[user-vs-maintainer-ia]].

## 1. Sélection de composants (Agent consommateur)

Un agent de sélection lit les métadonnées pour choisir le bon composant face à un besoin exprimé. Pour construire un formulaire, il consulte `usage.useCases` pour trouver les composants liés aux formulaires, `aiHints.selectionCriteria` pour choisir entre variantes, et `usage.antiPatterns` pour éviter les erreurs courantes. C'est la phase 1 du [[protocole-arc]] — l'IA comme consommateur précis.

## 2. Graphes de relations (Cartographie)

Les métadonnées permettent de comprendre les hiérarchies de composants et de tracer les dépendances. En utilisant les champs `category` et `composition`, un agent peut cartographier quels atomes sont utilisés à travers l'application, compter les instances récursivement, et construire le [[knowledge-graph-design-system]]. C'est l'alimentation automatique du graph depuis les métadonnées déclarées.

## 3. Validation pre-génération (Agent mainteneur)

Avant de suggérer ou générer du code, l'agent vérifie que le résultat ne viole pas les règles encodées : il contrôle les `antiPatterns` (pas de plusieurs boutons primaires dans la même section), respecte les `composition.parentConstraints` (ce composant peut-il être utilisé ici ?), suit les `accessibility` requirements. Ce workflow est celui qui fait franchir à l'IA la frontière User → Maintainer ([[user-vs-maintainer-ia]]) : l'agent ne génère pas d'abord et ne vérifie pas ensuite — il vérifie avant de générer.

## 4. Génération de code (Contrat d'implémentation)

Les métadonnées servent de contrat pour la génération. La section `examples` fournit des templates copy-paste. La section `props` définit l'interface TypeScript. La section `variants` explique quelles options existent et quand les utiliser. L'agent génère du code qui respecte les conventions du système dès le premier essai, sans exploration. C'est la concrétisation de l'argument de [[inversion-economique-code-comprehension]] : le code est gratuit, la compréhension (encodée dans les métadonnées) est ce qui le rend correct.

## Relation avec le protocole ARC

Les workflows 1 et 4 correspondent à la phase Audit (consommateur). Le workflow 3 correspond à la phase Report (mainteneur) — la validation est un acte de gouvernance. Les workflows 2 et 3 combinés posent les fondations de la phase Compose (auto-gouverné), où l'agent détecte la dérive et produit les correctifs de manière autonome.
