---
type: concept
tags: [dsds, format, schema, json, standard, machine-readable, design-system, documentation, agents, portabilite]
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[design-system-documentation-spec](../sources/design-system-documentation-spec.md)"
related:
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[schema-metadata-composant](schema-metadata-composant.md)"
  - "[dtcg-annotation-schema](dtcg-annotation-schema.md)"
  - "[ia-comme-utilisateur](ia-comme-utilisateur.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[documentation-lag](documentation-lag.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[pj-onori](../entities/pj-onori.md)"
  - "[design-md-format](design-md-format.md)"
  - "[google-design-md-spec](../sources/google-design-md-spec.md)"
updated: 2026-06-26
---

## Le format DSDS

DSDS (Design System Documentation Spec) est un format JSON open source pour documenter les design systems de façon machine-readable. À la différence des schémas de métadonnées maison décrits dans [schema-metadata-composant](schema-metadata-composant.md), DSDS est une spec ouverte, validable via JSON Schema, versionnée, et conçue pour être portative entre outils. La version 0.12.0 (draft, juin 2026) est maintenue par [pj-onori](../entities/pj-onori.md) ([design-system-documentation-spec](../sources/design-system-documentation-spec.md)).

La distinction fondatrice : DSDS documente le *comment et le pourquoi* du design system — pas les valeurs de tokens elles-mêmes. C'est le complément formel du W3C DTCG ([dtcg-annotation-schema](dtcg-annotation-schema.md)), qui gère le *quoi*. Ensemble, les deux formats couvrent l'ensemble de la connaissance d'un design system : valeurs (DTCG) + contexte, règles, patterns et raisonnement (DSDS).

## Structure d'un fichier DSDS

Un fichier DSDS exige `dsdsVersion` et l'un de deux patterns : `entity` pour les fichiers mono-entité (un composant, un token, un pattern par fichier) ou `entityGroups` pour les fichiers multi-entités (plusieurs entités regroupées par domaine). Les deux patterns sont composables via le mécanisme de `$ref` (JSON Pointer), qui permet un manifest centralisé pointant vers des fichiers séparés — une architecture de repo distribuée sans perte de cohérence.

Cette dualité résout un problème fréquent : les petits systèmes bénéficient d'un fichier unique, les grands systèmes nécessitent la distribution. DSDS supporte les deux sans bifurquer le format.

## Les 7 types d'entités

DSDS reconnaît sept types d'entités identifiés par un champ `kind` :

`component` — éléments UI réutilisables (boutons, inputs, modals), avec support pour l'anatomy, l'API, les variants, les states et les design specs. `token` — un design token unique, lié à sa définition DTCG via le champ `source`. `token-group` — regroupement récursif de tokens. `theme` — ensemble de surcharges de tokens (dark mode, high-contrast, brand variants) ; la valeur réelle reste dans le fichier DTCG. `foundation` — base de design (couleur, typographie, espacement, élévation). `pattern` — comment plusieurs composants se combinent pour résoudre un besoin utilisateur. `guide` — documentation longue forme (getting started, contribution, migration).

Toutes les entités partagent une enveloppe commune : `kind`, `identifier`, `name`, `description`, `metadata`, `documentBlocks`, et optionnellement `agentDocumentBlocks`. L'`identifier` est toujours la clé machine ; `name` est toujours le label humain — une convention sans exception dans tout le schéma.

## Le système de document blocks (16 kinds)

Les entités sont documentées via un tableau `documentBlocks`, chaque entrée étant un objet typé par son champ `kind`. Les 16 kinds couvrent : `useCases`, `guidelines`, `anatomy`, `api`, `variants`, `states`, `accessibility`, `checklist`, `content`, `design-specifications`, `imports`, `interactions`, `motion`, `principles`, `scale`, `sections`, `steps`.

Chaque kind est scoped : un component accepte les blocks component-scoped et les blocks généraux ; un pattern accepte ses propres scoped blocks. Cette contrainte d'attribution évite la prolifération de documentation non pertinente et rend le schéma validable.

Le block `guidelines` encode des règles au format RFC 2119 : `must`, `should`, `should-not`, `must-not`. Les agents traitent les entrées `must`/`must-not` comme des limites dures. Chaque guideline peut porter un `evidence` (la preuve backing) et des `criteria` (conditions testables).

## Les criteria comme mécanisme de vérification formelle

Le sous-schéma `criterion` est la contribution technique la plus nouvelle de DSDS par rapport aux schémas maison décrits dans [schema-metadata-composant](schema-metadata-composant.md). Un critère relie une règle à son mode de vérification : `automated` (un outil décide — il déclare son scheme et sa config), `assisted` (l'outil surface des candidats, un humain décide), ou `manual` (jugement humain pur). Ce champ closed-set répond à *qui décide*. Les exemples fixtures sur un critère (outcome `pass` ou `fail`) permettent à un runner de confirmer que le check détecte ce qu'il prétend détecter.

"The statement is always the source of truth. The check is its executable shadow." ([design-system-documentation-spec](../sources/design-system-documentation-spec.md)). Cette formulation distingue DSDS d'un simple système de linting : la spec humaine reste normative, l'automatisation est son implémentation — et les deux sont liées dans le même fichier.

## La séparation documentBlocks / agentDocumentBlocks

Le mécanisme le plus directement pertinent pour l'architecture décrite dans [ia-comme-utilisateur](ia-comme-utilisateur.md) : DSDS formalise dans sa spec la distinction entre documentation humaine et documentation agentique. `documentBlocks` est ce que tout le monde lit. `agentDocumentBlocks` est ce que seuls les agents lisent — les outils ne l'affichent jamais aux humains.

Ce qui appartient à `agentDocumentBlocks` : les règles dures (MUST/MUST NOT comme limites absolues), les distinguos entre entités similaires ("use link for navigation, not button"), les limites documentées avec preuve empirique ("agents broke the touch target 9 times out of 10 when they shrank the height — don't"), et les critères qu'un agent peut exécuter en auto-vérification.

La règle de construction : les agents lisent les deux tableaux — les docs humaines d'abord, puis les notes agent. `agentDocumentBlocks` ajoute ; il ne remplace jamais. Il ne répète pas le contenu humain — il l'étend.

## La portabilité comme argument de conception

Le premier tenet de DSDS est la portabilité : "A design system's source of truth should survive any rebuild, reorg, or rethink." Cette formulation est une réponse directe au problème du vendor lock-in de la documentation — les plateformes de docs changent, les outils de design changent, les organisations restructurent. Un format JSON ouvert, validable, non lié à un outil, survit à ces changements.

Cette portabilité est la réponse structurelle à une dimension du [documentation-lag](documentation-lag.md) rarement traitée dans le corpus : le lag causé par la migration d'outil. Quand une équipe change de plateforme de documentation, elle perd souvent la cohérence accumulée. DSDS permet de changer la couche de rendu sans changer la source de vérité — la doc suit l'outil, pas l'inverse.

## Rapport avec les schémas maison décrits dans le corpus

DSDS et le [schema-metadata-composant](schema-metadata-composant.md) de Morales Achiardi ne sont pas en tension — ils opèrent à des niveaux différents. Le schéma maison (9 sections, TypeScript ou JSON, par composant) est une convention d'équipe : flexible, adaptée au contexte, sans garantie d'interopérabilité. DSDS est un standard ouvert : structuré, validable, portable. Un système qui adopte DSDS gagne l'interopérabilité et la validation automatique ; un système qui garde un schéma maison conserve la flexibilité de forme.

La distinction est opérationnelle : un MCP peut servir des fichiers DSDS sans adaptation, là où un schéma maison nécessite un parser custom par équipe. Pour un réseau d'équipes (plusieurs BUs partageant un système, une organisation multi-produits), DSDS élimine la fragmentation des formats.

## ⚡ Tension : standard ouvert vs adoption réelle

DSDS est un draft spec en version 0.12.0, non endorsé par un organisme de normalisation (W3C, ISO). Il n'existe pas encore de données d'adoption publiques. La question de savoir si un format ouvert sans endorsement peut s'imposer face aux conventions maison (comme le format maison d'Indeed décrit dans [schema-metadata-composant](schema-metadata-composant.md)) reste ouverte. L'adoption du W3C DTCG s'est faite lentement, sur plusieurs années, malgré un soutien institutionnel — DSDS part avec une visibilité moindre.

## ⚡ Tension : DSDS vs DESIGN.md — deux réponses au même problème

Avec l'open-sourcing de [design-md-format](design-md-format.md) par Google Labs en avril 2026 (15 800 étoiles en moins de trois mois), deux formats de description machine-readable de design systems coexistent maintenant. Ils ne sont pas directement en compétition — ils couvrent des couches différentes (DSDS : documentation comportementale par entité ; DESIGN.md : identité visuelle par projet) — mais ils répondent à la même question de départ : "comment rendre un design system lisible pour un agent ?" La divergence de réponse est significative.

DSDS part du composant : structure profonde, 7 types d'entités, 16 kinds de document blocks, criteria de vérification formelle. DESIGN.md part de l'identité : un seul fichier, 5 catégories de tokens, prose d'explication. DSDS est l'approche bottom-up (des composants vers le système). DESIGN.md est l'approche top-down (de la marque vers les tokens). Les deux sont complémentaires pour un système mature, mais une équipe qui démarre choisira probablement l'un avant l'autre — et les frictions d'adoption sont très différentes.

La question de convergence reste ouverte ([google-design-md-spec](../sources/google-design-md-spec.md)) : le `export --format dtcg` de DESIGN.md crée un pont vers l'écosystème DTCG que DSDS référence, ce qui suggère une possible interopérabilité technique, sans nécessairement unifier les formats eux-mêmes.
