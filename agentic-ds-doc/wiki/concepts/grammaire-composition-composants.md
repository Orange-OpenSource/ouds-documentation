---
type: concept
tags: [design-system, composition, agentique, ia, architecture, composants, patterns, langage, grammaire]
created: 2026-06-30
updated: 2026-07-09
sources:
  - "[ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md)"
  - "[meta-astryx-harsha-sridhar](../sources/meta-astryx-harsha-sridhar.md)"
  - "[building-language-design-systems](../sources/building-language-design-systems.md)"
  - "[design-systems-contracts-not-libraries](../sources/design-systems-contracts-not-libraries.md)"
related:
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[schema-metadata-composant](schema-metadata-composant.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[generation-spec-agentique](generation-spec-agentique.md)"
  - "[architecture-contexte-agentique](architecture-contexte-agentique.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[langage-design-system](langage-design-system.md)"
  - "[composant-comme-contrat](composant-comme-contrat.md)"
---

## Grammaire de composition des composants

La grammaire de composition est l'ensemble des règles qui définissent comment des composants individuels s'assemblent en interfaces cohérentes. C'est la quatrième couche du modèle AI-ready de [ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md), et l'une des plus distinctives : elle opère au niveau que ni les [contrats de composant](schema-metadata-composant.md) (qui décrivent chaque pièce isolément) ni les tokens (qui décrivent les valeurs visuelles) ne couvrent.

## Pourquoi la grammaire est distincte du contrat

Un modèle de langue peut connaître tous les mots d'une langue et produire une mauvaise phrase. La même limite s'applique aux composants : un agent qui connaît chaque composant individuellement ne sait pas nécessairement comment les agencer. Le contrat de `FormField` dit qu'il peut afficher un label, un input, un hint et un message d'erreur. La grammaire dit qu'en contexte de settings, les `FormField` se regroupent dans un `FieldGroup` qui possède l'espacement vertical — les champs individuels ne peuvent pas ajouter de marges arbitraires.

Cette distinction — entre connaître les pièces et connaître les règles d'assemblage — est analogue à ce que [generation-spec-agentique](generation-spec-agentique.md) appelle la différence entre spécifier un composant et spécifier un système.

## Structure d'une grammaire de composition

Une grammaire bien formée définit plusieurs dimensions :

**Les relations parent/enfant valides** spécifient quels composants peuvent contenir quels autres, et dans quel ordre. Par exemple :

```
SettingsPage
  ├── PageHeader
  ├── SettingsSection (1..n)
  │     ├── SectionHeading
  │     ├── FieldGroup
  │     └── InlineAlert? (optionnel)
  └── StickyActionBar? (optionnel)
```

Cette notation arborescente rend les dépendances traversables algorithmiquement — elle encode ce qu'un senior designer saurait intuitivement mais qu'un agent doit trouver explicitement.

**L'ownership de l'espacement** précise quel composant est responsable des marges entre ses enfants. C'est une information que la grammaire peut encoder et que les tokens ne couvrent pas : un `FieldGroup` possède le gap vertical entre ses `FormField` ; un `FormField` ne doit pas modifier son propre margin-bottom. Cette règle évite l'accumulation de marges ad hoc qui fragilise la cohérence visuelle à l'échelle.

**Les combinaisons interdites** listent explicitement ce qu'un agent ne doit pas faire — `Modal` contenant un autre `Modal`, `Toast` déclenché depuis un `Dialog`, `DestructiveButton` utilisé pour une action réversible. Sans cette liste, l'agent improvise à partir des descriptions individuelles et produit des combinaisons visuellement plausibles mais sémantiquement incorrectes.

**Les transformations responsive** décrivent comment la structure change selon le viewport : un `SidebarLayout` qui se replie en `BottomSheet` sur mobile, un `DataTable` qui devient une liste de `CardRow` sous un certain breakpoint. Ces règles ne peuvent pas être déduites des composants isolés.

## Grammaire vs patterns produit

La [layer 5 (patterns produit)](../sources/ai-ready-design-system-olha-bondar.md) couvre un niveau supérieur : des flux complets comme "invitation d'un membre" ou "confirmation d'une action destructive". La grammaire de composition opère en dessous — elle définit les règles structurelles qui s'appliquent à toute interface, quel que soit le domaine métier. Un pattern produit *utilise* la grammaire ; il ne la remplace pas.

La distinction est utile pour la maintenance : la grammaire change rarement (les règles d'assemblage sont stables), tandis que les patterns produit évoluent avec le produit lui-même.

## Relation avec les [trois-couches-composants-agents](trois-couches-composants-agents.md)

Dans le modèle des trois couches ([trois-couches-composants-agents](trois-couches-composants-agents.md)), la grammaire de composition appartient à la couche intermédiaire — entre les métadonnées de composant (couche basse) et le contexte d'intention (couche haute). Elle traduit les règles structurelles du design system en contraintes navigables par un agent, sans pour autant encoder la logique métier qui appartient au niveau produit.

## Composants scellés vs composants ouverts : l'axe d'architecture de composition

La distinction entre composant scellé et composant ouvert est une décision architecturale dont les implications dépassent la DX développeur. Un composant scellé (`<Dialog>`) est une boîte noire : les props entrent, l'UI sort. Ce modèle simplifie les mises à jour et limite la surface d'API, mais il bloque toute composition non anticipée. Un composant ouvert exporte ses primitives (`Dialog.Root`, `Dialog.Overlay`, `Dialog.Content`) et laisse l'assemblage au consommateur — philosophie introduite par Radix UI, appliquée à l'échelle par Astryx ([meta-astryx-harsha-sridhar](../sources/meta-astryx-harsha-sridhar.md)).

Pour un agent IA, cette distinction a une conséquence directe : un composant scellé peut être *utilisé* (l'agent passe des props) mais pas *composé* (l'agent ne peut pas assembler une variante non prévue). Un système à primitives exposées permet à l'agent de construire depuis les fondamentaux si les composants de haut niveau ne correspondent pas à l'intent. C'est un degré de liberté supplémentaire — mais aussi une surface d'erreur supplémentaire si la grammaire des assemblages valides n'est pas documentée. Les primitives sans règles de composition explicites créent le risque inverse : l'agent assemble librement, sans contrainte structurelle.

La conclusion opérationnelle : l'exposabilité des primitives est une condition nécessaire mais pas suffisante pour la composabilité agentique. Elle doit être accompagnée d'une grammaire qui documente quels assemblages sont valides, lesquels sont interdits, et quelles règles de composition s'appliquent.

## Grammaire et vocabulaire : les deux couches du langage

Achiardi ([building-language-design-systems](../sources/building-language-design-systems.md), juillet 2026) nomme explicitement la distinction que Bondar encode sans la verbaliser : la grammaire est l'une des deux composantes du [langage-design-system](langage-design-system.md), l'autre étant le vocabulaire. Le vocabulaire (tokens, noms de props, noms de composants nommés par intent) dit *quels termes existent*. La grammaire (règles d'assemblage, relations parent/enfant, ownership de l'espacement, combinaisons interdites) dit *comment les termes s'assemblent*.

Un agent qui connaît le vocabulaire sans la grammaire peut nommer correctement les composants et les assembler incorrectement. Un agent qui connaît la grammaire sans le vocabulaire peut assembler dans le bon ordre des termes sans signification. Les deux couches sont complémentaires et doivent être déclarées ensemble pour que la Phase 3 du [protocole-arc](protocole-arc.md) (Compose) soit praticable.

## Ce qui se passe sans grammaire explicite

Un agent sans grammaire peut générer des interfaces qui respectent tous les contrats de composant individuels et violent pourtant la cohérence systémique : des `FormField` avec des marges incohérentes, des `Dialog` imbriqués, des `Toast` déclenchés depuis des états d'erreur où un `InlineAlert` serait approprié. Ces violations sont difficiles à détecter par test unitaire — elles nécessitent une validation au niveau de la composition, pas du composant.

C'est pourquoi la grammaire et la [boucle de validation](boucle-feedback-infrastructure.md) sont complémentaires : la grammaire définit les règles, la validation détecte les infractions à l'échelle du système assemblé.
