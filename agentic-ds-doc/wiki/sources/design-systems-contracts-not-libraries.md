---
type: source
tags: [design-system, contrat, bibliothèque, composition, atomic-design, architecture, achiardi]
created: 2026-07-09
updated: 2026-07-09
sources: []
related:
  - "[[cristian-morales-achiardi]]"
  - "[[composant-comme-contrat]]"
  - "[[langage-design-system]]"
  - "[[protocole-arc]]"
  - "[[grammaire-composition-composants]]"
  - "[[existence-vs-intent-violations]]"
---

## Design systems are contracts, not libraries

**Auteur** : [[cristian-morales-achiardi]]
**Publication** : Design Systems Collective, mai 2026
**URL** : https://www.designsystemscollective.com/design-systems-are-contracts-not-libraries-4876d8e1d401

## Résumé

Article charnière de la série Achiardi qui pose la distinction conceptuelle fondamentale : un design system est un contrat formel, pas une bibliothèque. Cette distinction a des conséquences pratiques directes sur ce que signifie "utiliser correctement" un système. Une bibliothèque s'utilise si le code compile. Un contrat s'utilise correctement seulement si ses termes sont respectés — ce qui est une condition sémantique, non syntaxique.

## Thèse principale

Les décisions architecturales (tokens vs hardcode, composants scellés vs primitives ouvertes) ne sont pas des préférences techniques — elles définissent la forme du contrat que les consommateurs héritent. L'atomic design de Brad Frost n'est pas seulement une hiérarchie de complexité : c'est une hiérarchie de contrats (atomes → primitives, molécules → combinaisons valides, organismes → patterns produit).

Presque tout dans un système fonctionnel est un "compound" : un composant composé de primitives reliées par des règles formelles. Ces règles — quelles combinaisons sont valides, dans quelles conditions, avec quels anti-patterns — sont le contrat. Un agent qui importe sans respecter le contrat produit du code syntaxiquement correct et sémantiquement incorrect.

## Position dans la série Achiardi

Cet article est le maillon conceptuel entre les articles techniques (indexation, orchestration, gouvernance — déjà ingérés) et l'article de juillet 2026 sur le langage ([[building-language-design-systems]]). La progression de la série est maintenant lisible :

1. Infrastructure AI-ready (index, métadonnées, orchestration) → *comment rendre le système lisible*
2. Gouvernance encodée → *comment enforcer les règles*
3. Contrats (mai 2026) → *quelle est la nature formelle de ces règles*
4. Langage (juillet 2026) → *comment vocabulaire, grammaire et contrats forment un tout*

## Apport au vault

Enrichit [[composant-comme-contrat]] avec la dimension architecturale : le contrat n'est pas seulement dans les métadonnées du composant (intent, variants, anti-patterns) mais dans les décisions d'architecture qui définissent ce que les consommateurs peuvent composer. Un composant scellé impose un contrat d'usage plus strict qu'un composant à primitives ouvertes — mais ce contrat doit être explicite dans les deux cas pour être enforçable.

Consolide le lien entre [[existence-vs-intent-violations]] et la composition : une violation de contrat de design system est toujours une violation d'intent, rarement une violation d'existence (le composant existe, il est simplement utilisé hors contrat).
