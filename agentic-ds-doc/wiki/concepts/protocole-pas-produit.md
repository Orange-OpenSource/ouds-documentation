---
type: concept
tags: [mcp, architecture, design-system, agentique, interoperabilite, orchestration, strategie]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[self-healing-design-system](../sources/self-healing-design-system.md)"
  - "[wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md)"
related:
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[seeds-vs-trees](seeds-vs-trees.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[invisibilite-produit-os-agentique](invisibilite-produit-os-agentique.md)"
updated: 2026-06-30
---

## Protocole, pas produit

"Protocole, pas produit" est un principe architectural formulé par [romina-kavcic](../entities/romina-kavcic.md) après un an de maintien en production d'une architecture de design system agentique ([self-healing-design-system](../sources/self-healing-design-system.md)). Le principe est simple : construire les intégrations sur le standard MCP plutôt que sur des APIs propriétaires d'outils IA spécifiques, de sorte que la couche d'orchestration (l'IA au centre) soit remplaçable sans avoir à reconstruire quoi que ce soit d'autre.

## Ce que ça signifie en pratique

Dans l'architecture de Kavcic, Claude Code est au centre — connecté via MCP à Figma/Tidy, GitHub, Storybook, PostHog, Granola, Sentry, la documentation, et Observatory. Mais Claude Code n'est pas soudé à ces intégrations. Kavcic a testé la même architecture avec Cursor, Codex, et d'autres outils IA sans reconstruire aucune des connexions MCP. Le swap du centre ne touche pas la périphérie.

Sa formulation : "If a better tool shows up tomorrow, you swap the center, and everything else stays the same. That's the point of building on a protocol, not a product" ([self-healing-design-system](../sources/self-healing-design-system.md)).

## Pourquoi c'est stratégiquement important

L'écosystème IA est en évolution rapide. Les modèles qui dominent aujourd'hui sont challengés dans les mois suivants. Une architecture couplée à un outil spécifique est donc fragile : chaque avancée du marché requiert soit de rester sur un outil inférieur, soit de reconstruire les intégrations. Une architecture sur protocole absorbe l'évolution sans friction.

Cette logique est exactement celle que [mcp-model-context-protocol](mcp-model-context-protocol.md) décrit à un niveau plus générique ("USB pour l'IA") — mais Kavcic l'applique ici à la décision architecturale concrète : ne jamais construire une intégration sur l'API propriétaire d'un outil IA quand une couche MCP standard est disponible.

## Le benchmark comme confirmation

Kavcic court les mêmes exercices sur tous les nouveaux modèles à leur sortie (Gemini, GPT 5.2 à 5.4, Llama, Mistral, Cursor, Codex) précisément parce que l'architecture le lui permet. Ce benchmark continu n'est possible que parce que les intégrations ne changent pas d'un outil à l'autre. Le protocole est la condition de possibilité de l'évaluation comparative.

Au moment de la publication, Claude Code donne les meilleurs résultats "for design system work, particularly in reasoning about component relationships and token semantics" — mais la formulation elle-même anticipe que ça peut changer, et l'architecture est prête pour ce changement ([self-healing-design-system](../sources/self-healing-design-system.md)).

## Relation avec la pérennité des investissements

Ce principe est une application du concept [design-system-as-infrastructure](design-system-as-infrastructure.md) à la couche d'outillage IA. De la même façon qu'un design system bien architecturé est un investissement durable malgré l'évolution des frameworks frontend, une architecture d'orchestration sur protocole est un investissement durable malgré l'évolution des modèles IA. Les fondations (index, métadonnées, graph) persistent. L'outil au centre peut être swappé.

## App Intents comme implémentation Apple du principe (WWDC 2026)

[wwdc-2026-apple-ai-native-os-levinriegner](../sources/wwdc-2026-apple-ai-native-os-levinriegner.md) documente une instance du même principe à l'échelle du système d'exploitation. Apple App Intents est un framework propriétaire (pas MCP), mais il repose sur la même logique : les apps exposent leurs capacités via un contrat structuré standard, et l'orchestrateur (Siri, Spotlight, Apple Intelligence) peut les invoquer sans être couplé à chaque app individuellement. L'app est le "produit" ; App Intents est le "protocole" qui la rend invocable.

La différence avec MCP est architecturale : App Intents est côté device et propriétaire Apple ; MCP est côté serveur et ouvert. Les deux coexistent dans l'écosystème WWDC 2026 — MCP natif est adopté par Xcode pour les agents de développement, App Intents reste le standard pour exposer les capacités applicatives à l'OS. Cette dualité soulève une question non résolue : voir [invisibilite-produit-os-agentique](invisibilite-produit-os-agentique.md) section ⚡ Tension.

## ⚡ Tension : MCP comme vrai standard ouvert ?

La thèse "protocole, pas produit" suppose que MCP reste un standard suffisamment stable et universel pour que les intégrations construites dessus soient portables entre outils. Si un outil IA dominant décidait d'un standard concurrent, ou si MCP évoluait de façon non-rétrocompatible, la portabilité serait compromise. Cette dépendance au standard n'est pas documentée comme une limite dans le corpus — la stabilité de MCP est présupposée plutôt qu'argumentée. L'adoption native de MCP par Apple dans Xcode (WWDC 2026) renforce l'argument de stabilité, mais uniquement pour le layer de développement — pas encore pour le layer applicatif.
