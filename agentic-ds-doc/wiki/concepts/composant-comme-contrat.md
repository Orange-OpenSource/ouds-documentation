---
type: concept
tags: [design-system, agentic, composants, contrats, ia, intent, gouvernance, langage]
created: 2026-07-03
updated: 2026-07-09
sources:
  - "[[agentic-ds-from-chatbot-to-orchestration]]"
  - "[[design-systems-contracts-not-libraries]]"
  - "[[building-language-design-systems]]"
related:
  - "[[composants-context-aware]]"
  - "[[trois-couches-composants-agents]]"
  - "[[intent-token]]"
  - "[[systeme-de-design-agentique]]"
  - "[[schema-metadata-composant]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[concevoir-les-conditions]]"
  - "[[grammaire-composition-composants]]"
  - "[[langage-design-system]]"
---

## Le composant comme contrat

Le renversement conceptuel le plus net de l'approche agentique est celui-ci : dans un design system traditionnel, un composant est quelque chose qu'on importe. Dans un design system agentique, un composant devient un *contrat* entre design, code, intent produit, accessibilité et comportement ([[agentic-ds-from-chatbot-to-orchestration]]).

La formulation synthétique de Kavcic — "From Here is a button to Here are the rules, intent, constraints, accessibility requirements, and usage conditions for this action pattern" — est le déplacement épistémique central. Le composant ne change pas visuellement. Ce qui change, c'est ce qu'il est censé *transporter* : non plus une apparence, mais une décision.

## Ce que contient un contrat de composant

Un contrat minimal structuré selon Kavcic couvre cinq dimensions :

**Intent** : à quoi sert ce composant dans le flux produit. Un bouton primaire sert à l'action principale. Un bouton destructif sert aux actions irréversibles. Ce n'est pas la même chose — et l'agent doit pouvoir distinguer les deux sans inférence.

**Variants** : quels variants existent, avec quelles contraintes d'usage. La règle n'est pas "voici les variants" mais "voici quand utiliser chaque variant et ce qu'on doit faire si le variant requis n'existe pas" (escalader, pas improviser).

**Rules** : règles d'usage, de composition, d'accessibilité. Ne jamais utiliser un styling destructif sans confirmation. Toujours associer un cancel à un confirm. Préserver la navigation clavier. Utiliser les états loading pour les actions asynchrones.

**Accessibility** : contraintes qui ne sont pas optionnelles et que l'agent ne peut pas assouplir. Ratio de contraste minimum. Comportement focus. Labelling.

**Anti-patterns** : ce qu'on ne fait pas et pourquoi. Ne pas créer de styling one-off sans vérifier la disponibilité d'un token. Ne pas utiliser primary pour une action secondaire.

## La différence avec un composant non-contractualisé

Sans contrat, l'agent peut générer du code fonctionnel — la syntaxe est correcte, le composant s'affiche. Ce n'est pas le même registre que générer du code *correct* : respectant les décisions de design, l'intent du produit, les contraintes d'accessibilité, les règles de composition du système.

C'est la racine de ce que Kavcic nomme "design debt at machine speed" : un agent sans contrat produit vite mais accumule de la dette silencieuse. Chaque génération ajoute une couche de déviation de l'intent. Avec un contrat, le chemin naturel est le chemin correct — le même principe que [[concevoir-les-conditions]].

## Relation avec les autres formulations du vault

Le contrat de composant est la vue composant de ce que [[schema-metadata-composant]] formalise en termes de structure (useWhen, doNotUseWhen, accessibility). Il est la couche 2 de [[trois-couches-composants-agents]] exprimée du point de vue de ce que le composant *transporte* plutôt que de ce que le système *doit contenir*. Il est aussi la version à grain composant de ce que [[concevoir-les-conditions]] formule à l'échelle du système : on conçoit les conditions sous lesquelles les interfaces se construisent correctement.

La [[grammaire-composition-composants]] (Bondar) est complémentaire : le contrat dit ce qu'un composant *est* et *impose*. La grammaire dit comment les composants *s'assemblent* entre eux. Les deux ensemble constituent ce qu'un agent a besoin pour composer correctement.

## Gouvernance par contrat

Le contrat de composant est aussi un mécanisme de gouvernance. Si un agent demande une composition qui violerait un contrat déclaré, le système peut le détecter avant génération — c'est la gouvernance pré-génération décrite dans [[gouvernance-design-system-ia]]. Le contrat est la règle ; l'auditeur est son exécuteur.

Cette logique rejoint [[existence-vs-intent-violations]] : la gouvernance ne se réduit pas à vérifier que le composant *existe*, mais que son usage *respecte l'intent du contrat*. Un composant utilisé dans le mauvais contexte est une violation d'intent — détectable seulement si le contrat est encodé.

## Le design system comme contrat formel (Achiardi, mai 2026)

Achiardi radicalise cette formulation dans [[design-systems-contracts-not-libraries]] : le design system entier est un contrat, pas seulement chaque composant individuellement. L'atomic design de Brad Frost n'est pas seulement une hiérarchie de complexité — c'est une hiérarchie de contrats. Les atomes définissent les primitives (contrats de valeur). Les molécules encapsulent des combinaisons valides (contrats de composition). Les organismes encodent des patterns produit (contrats d'usage).

Cette lecture articule les niveaux : le composant-comme-contrat ([[agentic-ds-from-chatbot-to-orchestration]]) est la vue micro — ce que *ce composant* engage. La formulation d'Achiardi est la vue macro — ce que *le système entier* engage vis-à-vis de ses consommateurs. Les deux niveaux sont nécessaires : un composant peut respecter son propre contrat tout en violant le contrat systémique (usage dans un contexte non prévu, combinaison non répertoriée dans la grammaire).

La conséquence pour la [[protocole-arc|Phase 3 (Compose)]] : pour que l'agent compose en respectant les contrats à tous les niveaux, les contrats doivent être déclarés à tous les niveaux — des tokens aux composants aux patterns. C'est ce que [[langage-design-system]] formalise comme la couche "contrat" du langage.

## ⚡ Tension : contrat vs flexibilité

Le modèle contrat crée une tension avec les besoins d'adaptation contextuelle documentés dans [[composants-context-aware]]. Un composant context-aware *doit* se comporter différemment selon son contexte — un bouton dans une alert n'a pas les mêmes règles qu'un bouton dans la navigation. Cela signifie que le contrat doit être *contextuel*, pas absolu : non pas "use primary" mais "use primary when in a flow's main action position, use destructive when confirming irreversible deletion."

La solution n'est pas de choisir entre contrat et contextualité — c'est de les combiner. Le contrat définit les règles ; le contexte détermine quelle règle s'applique. Voir [[composants-context-aware]] pour les exemples concrets (Button dans trois contextes, Accordion dans trois produits).
