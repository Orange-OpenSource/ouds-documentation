---
type: source
tags: [design-system, langage, vocabulaire, grammaire, contrat, tokens, composition, achiardi]
created: 2026-07-09
updated: 2026-07-09
sources: []
related:
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[langage-design-system](../concepts/langage-design-system.md)"
  - "[grammaire-composition-composants](../concepts/grammaire-composition-composants.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md)"
---

## Building language for design systems

**Auteur** : [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)
**Publication** : Design Systems Collective, juillet 2026
**URL** : https://www.designsystemscollective.com/building-language-for-design-systems-1b2f260b0bdf

## Résumé

Article central de la série Achiardi 2026. La thèse : un design system est un langage, pas seulement une bibliothèque. Il est composé d'un vocabulaire (les tokens, les props, les noms de composants — termes d'intent) et d'une grammaire (les règles d'assemblage des composants, les flux d'état, les conventions de nommage). Ces deux couches doivent être déclarées explicitement et encodées de façon machine-lisible pour que la Phase 3 du [protocole-arc](../concepts/protocole-arc.md) (Compose) devienne praticable.

## Thèses principales

Le vocabulaire et la grammaire sont hérités du framework choisi, mais ils doivent être *déclarés* pour être enforçables. Sans déclaration explicite, design et code accumulent des grammaires divergentes — chaque développeur importe ses priors de framework, chaque designer ses conventions de Figma. La déclaration commune crée le contrat.

Un token de design est du vocabulaire au niveau des valeurs : une équipe l'écrit, décide de sa signification, l'orthographie d'une seule façon, et pointe design et code vers une source de vérité unique. Le standard W3C DTCG formalise le format de ce vocabulaire.

Le contract est la table de correspondance partagée contre laquelle design et code composent : quelles props existent, quelles valeurs chaque prop accepte, un terme par signification, nommé par intent. "Un vocabulaire qu'on peut auditer est un contrat." Ce contrat, écrit dans une forme machine-lisible, peut être enforçé automatiquement — la machine enforce le vocabulaire avec une consistance qu'un humain n'atteint pas.

## Citations clés

- "When you choose a framework you inherit language, its vocabulary and its grammar."
- "A vocabulary you can audit is a contract."
- "Machines are how you easily enforce vocabulary across surfaces."

## Apport au vault

Cet article fournit le socle conceptuel manquant pour la [Phase 3 (Compose)](../concepts/protocole-arc.md) : la "composition" agentique présuppose un langage déclaré — sans vocabulaire et grammaire explicites, l'agent improvise, accumule des priors contradictoires ([priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md)), et produit des assemblages visuellement plausibles mais sémantiquement incorrects. C'est la dimension "langage" que les articles précédents de la série (indexation, orchestration, gouvernance) n'avaient pas encore nommée.

Crée le concept [langage-design-system](../concepts/langage-design-system.md) comme couche liant [intent-token](../concepts/intent-token.md) (vocabulaire valeurs), [grammaire-composition-composants](../concepts/grammaire-composition-composants.md) (vocabulaire assemblage), et [composant-comme-contrat](../concepts/composant-comme-contrat.md) (vocabulaire composant).
