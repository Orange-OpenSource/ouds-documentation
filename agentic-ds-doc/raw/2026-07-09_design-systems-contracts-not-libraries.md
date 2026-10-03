---
source_url: https://www.designsystemscollective.com/design-systems-are-contracts-not-libraries-4876d8e1d401
author: Cristian Morales Achiardi
published: mai 2026
ingested: 2026-07-09
---

# Design systems are contracts, not libraries

Source brute — contenu reconstitué depuis snippets indexés (page client-rendered).

## Thèse principale

Un design system n'est pas une bibliothèque de composants qu'on importe — c'est un contrat formel entre design et code. La distinction n'est pas sémantique : elle change ce que signifie "utiliser correctement" le design system. Une bibliothèque s'utilise si le code compile. Un contrat s'utilise correctement seulement si ses termes sont respectés.

## Concepts clés

**Atomic design comme hiérarchie de contrats** : les atomes, molécules et organismes de Brad Frost ne sont pas seulement une hiérarchie de complexité — ils forment une hiérarchie de contrats. Les atomes définissent les primitives. Les molécules encapsulent des combinaisons valides. Les organismes encodent des patterns produit. À chaque niveau, un contrat précise ce qui peut être composé, dans quelles conditions, avec quelles règles.

**Tout composant comme compound** : presque tout dans un design system fonctionnel est un composant composé — combinant inputs, feedback et structure dans des proportions spécifiques, reliés par des contrats. Un composant "simple" comme un bouton est déjà un compound : texte + icône (optionnelle) + état (hover, active, disabled) + variante sémantique (primary, destructive, ghost), tenu ensemble par des règles de composition formelles.

**Architecture décide de ce qu'on hérite et de ce qu'on compose** : les décisions architecturales (tokens vs hardcode, composants scellés vs primitives ouvertes, props-driven vs slot-based) ne sont pas des préférences techniques — elles décident du contrat que les consommateurs héritent et de ce qu'ils peuvent composer à partir de lui.

**Contrat vs utilisation** : utiliser une bibliothèque = importer et compiler. Respecter un contrat = utiliser dans le contexte prévu, avec les variantes prévues, en respectant les anti-patterns déclarés. La violation de contrat n'est pas syntaxique (le linter ne la voit pas) — elle est sémantique.

## Citations clés

- "Almost everything in a working system is a compound made by combining inputs, feedback, and structure in specific proportions, held together by contracts."
- "Architecture decisions shape what you inherit and author."
- "A design system is not a library you import — it's a contract you sign."

## Connexions identifiées

- [[composant-comme-contrat]] : article fondateur de ce concept dans la série Achiardi.
- [[grammaire-composition-composants]] : atomic design comme hiérarchie de grammaires.
- [[protocole-arc]] : le contrat est ce que la Phase 3 (Compose) enforça automatiquement.
- [[langage-design-system]] : vocabulaire (tokens) + grammaire (assemblage) + contrat = le langage.
- [[existence-vs-intent-violations]] : violation de contrat = violation d'intent, pas d'existence.
- [[concevoir-les-conditions]] : concevoir les conditions sous lesquelles le contrat est respecté.
