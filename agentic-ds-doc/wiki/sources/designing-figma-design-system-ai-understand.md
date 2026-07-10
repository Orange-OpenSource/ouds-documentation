---
type: source
tags: [figma, naming, tokens, component-properties, auto-layout, lisibilite-machine, pratique]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[[designing-figma-design-system-ai-understand]]"
related:
  - "[[alpesh-karanpuria]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[intent-token]]"
  - "[[trois-couches-composants-agents]]"
  - "[[schema-metadata-composant]]"
---

## Designing a Figma Design System That AI Can Understand (Karanpuria, 2026)

[[alpesh-karanpuria]], publié sur Design Systems Collective (2026-03-10). Guide pratique Figma-centrique en 10 recommandations pour rendre un DS lisible par les agents IA. Audience : designers en début de parcours. Pas de données empiriques, pas de benchmark. Style : pédagogique, visuel (nombreux exemples de code).

**Thèse** : "Most design systems today are built only for humans. They are visually organized but structurally unclear for machines." Sans structure explicite, l'IA voit des formes et des calques — pas un système de relations.

## 10 recommandations (résumé)

Naming hiérarchique (`Category / Component / Variant / State / Size`), token-first avec tokens sémantiques, Component Properties plutôt que multiples composants, Auto Layout partout, descriptions machine-readable dans Figma, structure de fichier numérotée (00 Foundations, 01 Tokens, 02 Components, 03 Patterns...), mapping tokens→composants, nommage sémantique des calques, documentation des règles d'usage implicites, connexion design→code via export JSON partagé.

## Modèle 4 couches

Karanpuria propose une taxonomie 4 couches pour le DS AI-ready :

**Design Layer** — composants et layouts dans Figma.  
**Token Layer** — tokens structurés définissant les propriétés visuelles.  
**Logic Layer** — Component Properties et règles d'interaction.  
**Knowledge Layer** — documentation et contraintes d'usage.

Comparaison avec les modèles du vault : les 3 couches de [[trois-couches-composants-agents]] (Index / Métadonnées / Raisonnement) opèrent à un niveau d'abstraction plus élevé et sont centrées sur l'architecture d'un agent. Le modèle Karanpuria est Figma-natif — il décrit la structure du fichier Figma lui-même. Les deux sont complémentaires : Karanpuria décrit le contenu à produire dans Figma, Kavcic/Morales Achiardi décrivent comment l'architecture agentique le consomme.

## Citations clés

"Without structure, AI only sees shapes and layers. With structure, it sees a system of relationships." ([[alpesh-karanpuria]])

"This transforms the design system into a knowledge base, not just a component library." ([[alpesh-karanpuria]])

## Évaluation

Source de niveau "awareness + guide pratique" — la plus orientée Figma du corpus. Complémentaire aux sources Wolosin/Morales Achiardi qui s'adressent aux équipes avec une stack technique avancée. Utile comme référence pour les équipes qui commencent par la structuration du fichier Figma avant de construire l'infrastructure MCP. Apport principal au vault : formalisation de la convention de nommage composants, argument Component Properties, et Auto Layout comme signal comportemental — trois angles Figma-natifs absents du reste du corpus.
