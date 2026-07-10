---
type: source
tags: [design-system, ia, agentique, composition, tokens, validation, maturite, contenu]
created: 2026-06-30
updated: 2026-06-30
sources: []
related:
  - "[[systeme-de-design-agentique]]"
  - "[[modele-maturite-ia-design-system]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[schema-metadata-composant]]"
  - "[[readable-vs-usable-token]]"
  - "[[grammaire-composition-composants]]"
  - "[[contraintes-fixed-preferred-exploratory]]"
  - "[[trois-couches-composants-agents]]"
  - "[[mcp-model-context-protocol]]"
  - "[[architecture-contexte-agentique]]"
---

## What Is an AI-Ready Design System? — Olha Bondar

**URL** : https://olyacooper.medium.com/what-is-an-ai-ready-design-system-008334f5e3a1
**Date** : 22 juin 2026 — **Durée** : 19 min

## Thèse principale

Un design system AI-ready n'est pas une bibliothèque connectée à un outil IA : c'est un modèle structuré de la logique d'interface produit, suffisamment explicite pour qu'un agent puisse Discover → Understand → Select → Compose → Implement → Validate → Explain sans inventer les règles. La phrase-clé : "If a system is clear, AI can scale the system. If a system is ambiguous, AI can scale the ambiguity."

## Thèses secondaires

L'argument central est que l'AI-readiness est un projet de maturité du design system avant d'être un projet IA. Les lacunes qui pénalisent un agent (nommage visuel, drift design/code, documentation sans logique de sélection, tokens sans sémantique, connaissance produit non encodée) sont exactement les lacunes qui pénalisaient déjà les équipes humaines — l'agent les amplifie, il ne les crée pas.

La distinction **AI-generated vs AI-ready** est structurante : générer 500 composants avec l'IA ne rend pas le système AI-ready. L'AI-ready décrit comment le système peut être *interprété et opéré* par un agent, pas comment ses assets ont été produits.

## Les huit couches

L'article structure le problème en huit couches ordonnées par dépendance : (1) fondations machine-readable, (2) contrats de composant explicites, (3) identité partagée design/code, (4) grammaire de composition, (5) patterns produit et implémentations de référence, (6) guidance de contenu structurée, (7) validation exécutable, (8) accès et livraison de contexte aux agents. Les couches 4 et 6 sont les plus originales par rapport à l'état du wiki.

## Citations clés

- "The design system stops being a place where assets are stored. It becomes the infrastructure through which product decisions are executed." (≤15 mots)
- "Context architecture, not context volume. More documentation does not automatically produce better AI output." (≤15 mots)
- "The model is shared. The system is not." (formule sur l'avantage concurrentiel)
- "AI will generate the states you specify. It will improvise the states you omit."

## Concepts créés ou enrichis

- **Créé** : [[grammaire-composition-composants]] — layer 4 : règles parent/enfant, ownership de l'espacement, combinaisons interdites
- **Créé** : [[contraintes-fixed-preferred-exploratory]] — tripartition fixed/preferred/exploratory pour calibrer la liberté des agents
- **Enrichi** : [[schema-metadata-composant]] — avec le format JSON de contrat de composant (useWhen/doNotUseWhen/accessibility)
- **Enrichi** : [[modele-maturite-ia-design-system]] — avec les niveaux 0–4 de Bondar (distinct du modèle Kavcic centré sur les features IA pour humains)
- **Enrichi** : [[lisibilite-machine-design-system]] — avec la layer 6 (contenu structuré) et la layer 7 (validation exécutable)
- **Enrichi** : [[architecture-contexte-agentique]] — avec "context architecture vs context volume"

## Connexions identifiées

Forte résonance avec [[trois-couches-composants-agents]] (même logique de stratification), [[protocole-arc]] (même vision de la maturité par seuils), [[readable-vs-usable-token]] (même argument sur la sémantique des tokens). La section "mistakes" enrichit [[gouvernance-design-system-ia]] (piège du gros fichier d'instructions) et rejoint [[architecture-skills-rules-instructions]].

## Limites et biais

Article de praticien, pas de recherche empirique. Pas de données sur des systèmes réels ayant atteint les niveaux 3-4. Le modèle de maturité en 5 niveaux (0-4) est autonome et non référencé à d'autres taxonomies existantes dans le domaine — à croiser avec [[modele-maturite-ia-design-system]] (Kavcic) pour voir si les deux modèles mesurent bien des axes orthogonaux.
