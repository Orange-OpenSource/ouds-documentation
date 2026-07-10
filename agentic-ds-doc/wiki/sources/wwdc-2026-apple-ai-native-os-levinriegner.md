---
type: source
tags: [apple, wwdc, ios27, siri, app-intents, agentique, os, plateforme, invisibilite, design-system]
created: 2026-06-30
updated: 2026-06-30
sources: []
related:
  - "[[invisibilite-produit-os-agentique]]"
  - "[[ia-comme-utilisateur]]"
  - "[[architecture-contexte-agentique]]"
  - "[[protocole-pas-produit]]"
  - "[[niveaux-confiance-actions-agentiques]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[figma-library-invisible-ai-agents]]"
  - "[[mcp-model-context-protocol]]"
---

## Key topics from Apple's WWDC 2026: Preparing apps for an AI-native operating system — Ivan Leider (L+R)

**URL** : https://www.levinriegner.com/news/wwdc-26-takeaways/
**Date** : 8 juin 2026 — **Auteur** : Ivan Leider, L+R (agence produit/UX, NYC/Barcelone)

## Thèse principale

WWDC 2026 n'est pas "Apple tue l'App Store". C'est Apple qui fait de l'IA une capacité du système d'exploitation : l'assistant est connecté à ce que l'appareil sait, à ce que l'utilisateur fait, et à ce que les apps peuvent faire. La question pertinente pour les équipes produit n'est plus "faut-il un chatbot ?" mais : **"Notre produit peut-il participer à cette couche d'intent ?"**

## Thèses secondaires

Le concept structurant de l'article est l'**invisibilité produit** : "If the system cannot understand your content or invoke your workflow, your product may be technically installed and practically invisible." L'entrée vers une app ne commence plus nécessairement par un tap sur l'icône — elle peut commencer par une question à Siri, une recherche Spotlight, une sélection de texte, un regard via la caméra, ou une description de tâche depuis une autre app. Les apps qui n'exposent pas leurs actions et entités via App Intents deviennent transparentes au système.

La première action recommandée après WWDC n'est pas de construire un produit IA. C'est d'**auditer l'existant** : quel contenu doit être indexable ? Quelles actions doivent être disponibles via App Intents ? Quel contexte peut être exposé de façon sûre ? Quels workflows peuvent être invoqués sans ouvrir l'app ?

## Citations clés

- "Technically installed and practically invisible." (formule centrale)
- "The first move for many brands is not to build a giant AI product. It is to audit the existing product."
- "The value will not be the model by itself. It will be the integration."
- "Apps need to express their actions and entities to the system — that is not a cosmetic integration."

## Faits factuels WWDC 2026 (confirmés)

D'après cette source et MacRumors ([[wwdc-2026-macrumors-state-of-union]]) :
- **App Intents** : entity schemas + intent schemas pour Spotlight semantic index + View Annotations API (Siri agit sur le contenu à l'écran)
- **Foundation Models** : accès gratuit Private Cloud Compute pour développeurs < 2M downloads, image input, serveurs tiers (Claude, Gemini), Dynamic Profiles pour multi-agent workflows, open source prévu
- **Liquid Glass migration forcée** : opt-out supprimé — toutes les apps recompilées avec Xcode 27 adoptent le nouveau design
- **Xcode 27 agentic coding** : agents peuvent interagir avec simulator, localiser apps, lancer tests, corriger crashes
- **MCP natif dans Xcode** : Apple valide MCP comme standard d'intégration

## Concepts créés ou enrichis

- **Créé** : [[invisibilite-produit-os-agentique]] — invisibilité par non-exposition des App Intents au système OS
- **Enrichi** : [[ia-comme-utilisateur]] (le système OS comme nouvelle audience intermédiaire)
- **Enrichi** : [[architecture-contexte-agentique]] (l'OS comme orchestrateur d'intent — extension de la notion de MCP)
- **Enrichi** : [[protocole-pas-produit]] (App Intents = équivalent Apple du MCP)
- **Enrichi** : [[niveaux-confiance-actions-agentiques]] (Apple = agentic with human in the loop, délibérément)
- **Enrichi** : [[gouvernance-design-system-ia]] (Liquid Glass forcé = gouvernance design par mandat plateforme)

## Connexions identifiées

Forte résonance avec [[figma-library-invisible-ai-agents]] (Nurkhon) : même problème d'invisibilité à deux niveaux distincts — invisible au design system pour les agents de code, invisible à l'OS pour les agents Siri. La formule de Nurkhon "AI agents parse, not infer" s'applique au niveau OS : Siri ne devine pas ce que l'app peut faire, elle parse les App Intents exposés. Sans exposition, pas d'existence dans le layer agentique.

Connexion à [[concevoir-les-conditions]] : l'audit App Intents recommandé par Leider est exactement ce que désigne Morales Achiardi — concevoir les conditions sous lesquelles le système peut agir correctement.

## Limites

Analyse de praticien d'agence, pas de recherche empirique. L'enthousiasme pour la direction Apple est explicite ("I remain the same Apple fanboy"). La partie visionOS est prospective. La situation Europe documentée reste vague sur les causes réglementaires exactes.
