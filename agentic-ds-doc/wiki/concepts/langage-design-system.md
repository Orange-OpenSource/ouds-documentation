---
type: concept
tags: [design-system, langage, vocabulaire, grammaire, contrat, tokens, composition, ia]
created: 2026-07-09
updated: 2026-07-09
sources:
  - "[building-language-design-systems](../sources/building-language-design-systems.md)"
  - "[design-systems-contracts-not-libraries](../sources/design-systems-contracts-not-libraries.md)"
related:
  - "[protocole-arc](protocole-arc.md)"
  - "[grammaire-composition-composants](grammaire-composition-composants.md)"
  - "[intent-token](intent-token.md)"
  - "[composant-comme-contrat](composant-comme-contrat.md)"
  - "[priori-conflictuels-nommage](priori-conflictuels-nommage.md)"
  - "[dtcg-annotation-schema](dtcg-annotation-schema.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
---

## Le design system comme langage

Un design system est un langage partagé entre design et code. Il est composé de trois couches indissociables : un vocabulaire (les termes d'intent), une grammaire (les règles d'assemblage), et des contrats (les engagements formels entre les couches). Cette formulation, proposée par [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) en juillet 2026, fournit le socle conceptuel de la Phase 3 du [protocole-arc](protocole-arc.md) (Compose) : pour que l'IA compose correctement, le langage doit être déclaré — et non inféré.

## Le vocabulaire : termes d'intent

Le vocabulaire est l'ensemble des termes que design et code partagent, nommés par intent plutôt que par apparence. Un token de design est du vocabulaire au niveau des valeurs : l'équipe le nomme une fois, décide de sa signification, et pointe les deux surfaces (design tool + codebase) vers cette source de vérité unique ([building-language-design-systems](../sources/building-language-design-systems.md)).

Le standard W3C DTCG (Design Token Community Group) formalise le format du vocabulaire de tokens. Le [dtcg-annotation-schema](dtcg-annotation-schema.md) en est la mise en oeuvre pratique : `$description`, `$deprecated`, `$extensions` comme porteurs du sens au-delà de la valeur brute.

La distinction [readable-vs-usable-token](readable-vs-usable-token.md) s'applique directement ici : un token machine-readable (le pipeline compile) n'est pas nécessairement machine-usable (l'agent raisonne correctement). Le vocabulaire n'est usable que si chaque terme est nommé par intent et accompagné des règles d'usage. Un token `color-red-600` sans intent déclaré n'est pas du vocabulaire — c'est du bruit.

## La grammaire : règles d'assemblage

La grammaire est l'ensemble des règles qui définissent comment les termes du vocabulaire s'assemblent. Elle couvre les conventions de nommage (casing, préfixe, suffixe), les relations parent/enfant entre composants, l'ownership de l'espacement, les combinaisons interdites, et les règles de composition par contexte ([grammaire-composition-composants](grammaire-composition-composants.md)).

Quand une équipe choisit un framework, elle hérite sa grammaire : la façon dont les composants exposent leurs props (PascalCase ou camelCase), la façon dont le state circule (props-down, events-up), ce qui est idiomatic et ce qui "fight the grain". Cette grammaire héritée coexiste avec la grammaire déclarée du design system — et lorsque les deux divergent, les agents arrivent avec des priors contradictoires et les mélangent ([priori-conflictuels-nommage](priori-conflictuels-nommage.md)).

La solution n'est pas d'éliminer les grammaires héritées, mais de déclarer explicitement la grammaire du système : nommer les règles, les encoder dans des fichiers consultables, et les rendre enforçables automatiquement.

## Le contrat : engagement formel entre les couches

Le contrat est la table de correspondance partagée contre laquelle design et code composent : quelles props existent, quelles valeurs chaque prop accepte, quel variant s'applique dans quel contexte, quelles combinaisons sont interdites. "Un vocabulaire qu'on peut auditer est un contrat" ([building-language-design-systems](../sources/building-language-design-systems.md)).

Un contrat machine-lisible peut être enforçé par une machine avec une consistance qu'aucun reviewer humain n'atteint. Le [composant-comme-contrat](composant-comme-contrat.md) est la vue composant de ce concept : chaque composant transport non plus une apparence mais une décision formalisée — intent, variants, règles d'accessibilité, anti-patterns.

Les [design systems comme contrats](../sources/design-systems-contracts-not-libraries.md) (Achiardi, mai 2026) nomment explicitement ce déplacement : un design system n'est pas une bibliothèque qu'on importe — c'est un contrat formel entre design et code, comparable à une interface TypeScript ou une spécification d'API. Importer sans respecter le contrat produit du code fonctionnel mais incorrect.

## Les trois couches forment un système

```
Vocabulaire (tokens, noms de composants, props)
     ↓ nourrit
Grammaire (règles d'assemblage, casing, relations parent/enfant)
     ↓ structure
Contrats (engagements formels : quand utiliser quoi, quelles combinaisons, quels anti-patterns)
     ↓ rendus machine-lisibles deviennent
Langage enforçable par agents
```

La lisibilité machine ([lisibilite-machine-design-system](lisibilite-machine-design-system.md)) est la propriété émergente de ces trois couches correctement encodées. Sans vocabulaire d'intent, l'agent improvise les noms. Sans grammaire déclarée, il assemble avec ses priors de framework. Sans contrats, il utilise les composants correctement de façon syntaxique et incorrectement de façon sémantique.

## Implications pour la Phase 3 du protocole ARC

La Phase 3 du [protocole-arc](protocole-arc.md) (Compose / Auto-gouverné) requiert que l'agent puisse composer des interfaces à partir des primitives du design system sans intervention humaine. Cette composition n'est praticable que si le langage est déclaré : le vocabulaire fournit les termes, la grammaire fournit les règles, les contrats fournissent les garde-fous. Un agent composant sans langage déclaré produit des interfaces plausibles mais non gouvernées — ce que le corpus du vault nomme "design debt at machine speed" ([composant-comme-contrat](composant-comme-contrat.md)).

Achiardi formule la question ouverte pour la Phase 3 : si la Phase 1 prouve que l'IA peut lire un design system avec 100 % de précision, et si la Phase 2 prouve qu'elle peut l'auditer, la Phase 3 exige qu'elle puisse le *parler* — utiliser le langage du système, pas seulement l'indexer.
