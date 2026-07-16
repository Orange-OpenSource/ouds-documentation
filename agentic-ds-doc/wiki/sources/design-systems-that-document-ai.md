---
type: source
tags: [design-system, ia, documentation, gouvernance, ux, maturite, patterns]
created: 2026-06-17
updated: 2026-06-17
sources: []
related:
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)"
  - "[quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md)"
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md)"
---

## Design Systems That Document AI

**Auteure** : [romina-kavcic](../entities/romina-kavcic.md)
**Date** : 2026-06-01
**Source** : thedesignsystem.guide (Substack)
**Fichier brut** : `raw/Design Systems That Document AI.md`

## Thèse principale

La majorité des design systems ignorent encore totalement la question de l'IA comme *contenu à documenter* — c'est-à-dire les patterns d'interface pour les fonctionnalités IA destinées aux utilisateurs humains. Sur 156 systèmes publics analysés, seuls 26 documentent l'IA. Ces 26 systèmes ont convergé indépendamment vers les mêmes quatre règles fondamentales. La convergence est le signal. Le corpus établit une taxonomie de maturité en cinq niveaux.

**Point d'attention pour le vault** : cet article documente comment les design systems documentent les *fonctionnalités IA pour utilisateurs humains* — dimension entièrement différente de la question centrale du reste du corpus (comment les agents IA opèrent des design systems). Voir [deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md) pour la distinction formalisée.

## Dataset

156 design systems publics examinés. 130 (83 %) n'ont aucune couche IA visible. 26 (17 %) documentent l'IA à un niveau ou un autre. Représentés : IBM Carbon, Microsoft Fluent 2, Atlassian, Shopify Polaris, AWS Cloudscape, GitLab Pajamas, Red Hat PatternFly, SAP Fiori, Workday Canvas, Apple HIG.

## Le modèle de maturité en cinq niveaux

Le [modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md) décompose la progression ainsi :

- **Niveau 0** — Aucune couche IA (130/156 systèmes). Aucun composant, token, ni guideline dédié.
- **Niveau 1** — IA comme décoration : rôles de couleur spéciaux, tokens nommés, styling distinctif. Exemple : Shopify Polaris avec le rôle "Magic" (`--p-color-bg-surface-magic`).
- **Niveau 2** — IA comme composant : composant dédié réutilisable. Exemple : IBM Carbon avec le label AI + popover d'explicabilité, déployé sur 13 composants.
- **Niveau 3** — IA comme pattern d'interaction : guidelines comportementales (suggest vs respond vs handoff). Exemple : Atlassian.
- **Niveau 4** — IA comme couche de gouvernance : rubrique RAI avec notes par lettre, auto-fails. Exemple : Microsoft Fluent 2 Responsible AI rubric.
- **Niveau 5** — IA comme infrastructure du système : tier Copilot UI Kits cross-platform (Web/iOS/Android). Exemple : Microsoft Fluent.

## Les quatre règles convergentes

Ces quatre règles ont émergé indépendamment chez IBM, AWS, GitLab, Red Hat, SAP, Workday et Apple — voir [quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md) :

1. **Marquer toujours** — label IA, styling réservé, sans sur-marquer.
2. **Expliquer en couches** — Quoi/Pourquoi/Comment, révélation progressive selon les enjeux.
3. **Humain en contrôle** — toujours override, undo ; plus l'action est risquée, plus le consentement doit être explicite.
4. **Concevoir l'échec** — erreurs explicites, fallbacks, chemin de récupération.

## Le value gate

IBM, GitLab, Red Hat et Apple positionnent tous comme *première* guideline : la permission de *ne pas utiliser l'IA*. Avant de définir comment documenter les features IA, ces systèmes établissent le droit de les désactiver. C'est un signal de gouvernance, pas d'ergonomie — intégré dans [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md).

## Le vrai pattern : 15 questions

Un pattern d'interaction IA complet exige 15 éléments documentés : intent utilisateur, déclencheur, input, output, comportement système, contrôles utilisateur, mécanisme de feedback, état d'erreur, confiance/incertitude, explicabilité, accessibilité, données/vie privée, exemples, anti-patterns, notes d'implémentation. La plupart des systèmes ne couvrent que 3 à 5 de ces 15 dimensions — souvent le styling et les états d'erreur basiques.

## Citations clés

- "83% of design systems have no AI layer at all." ([romina-kavcic](../entities/romina-kavcic.md))
- "The convergence is the signal — these teams never talked to each other." ([romina-kavcic](../entities/romina-kavcic.md))
- "Permission not to use AI is the first guideline." (IBM, GitLab, Red Hat, Apple — indépendamment)

## Ce qui manque publiquement

Les zones documentées par moins de 5 systèmes sur 26 : confiance/incertitude, récupération des hallucinations, boucles de correction utilisateur, workflows multi-agents, permissions d'agents, comportements offline/dégradés. Ces lacunes définissent la frontière de l'état de l'art actuel.

## Connexions identifiées

L'article crée une connexion directe avec [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md) via le Level 4 (Fluent RAI rubric comme instance de gouvernance formalisée). Il enrichit [systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md) en ajoutant une deuxième lecture du terme "agentique" : non plus le DS opéré par des agents, mais le DS qui documente les agents au service des humains. La tension entre ces deux lectures est formalisée dans [deux-lectures-du-design-system-ia](../syntheses/deux-lectures-du-design-system-ia.md).
