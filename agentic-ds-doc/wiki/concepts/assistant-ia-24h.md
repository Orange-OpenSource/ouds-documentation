---
type: concept
tags: [assistant-ia, self-hosted, design-system, openclaw, automatisation, infrastructure, memoire, securite]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[20-ai-workflows-design-system-teams]]"
related:
  - "[[architecture-skills-rules-instructions]]"
  - "[[metriques-adoption-ia-design-system]]"
  - "[[boucle-feedback-infrastructure]]"
  - "[[mcp-model-context-protocol]]"
  - "[[niveaux-confiance-actions-agentiques]]"
---

## L'assistant IA 24/7 comme infrastructure d'équipe

Un des problèmes récurrents dans l'adoption de l'IA par les équipes design system est la dépendance à des interfaces SaaS avec des sessions sans mémoire. Chaque conversation repart de zéro. Les membres de l'équipe ne partagent pas de contexte accumulé. Les jobs récurrents (audit hebdomadaire, veille concurrents) doivent être relancés manuellement.

**OpenClaw** (anciennement clawdbot) adresse ce problème via un assistant self-hosted tournant 24/7 sur un serveur propre ([[20-ai-workflows-design-system-teams]]). Le coût d'entrée est bas : un VPS Hetzner à ~5$/mois suffit.

## Capacités

OpenClaw se connecte aux messageries d'équipe (Telegram, Slack, Discord, WhatsApp), ce qui signifie que n'importe quel membre peut interroger le système depuis l'interface qu'il utilise déjà. Il maintient une **mémoire persistante** entre les conversations, contrairement aux sessions stateless des interfaces SaaS. Il peut exécuter des **scripts**, interroger les fichiers de tokens, lire le repo. Il supporte les **cron jobs** pour automatiser des tâches récurrentes. Le modèle sous-jacent est configurable : Claude, GPT, Gemini, DeepSeek.

**Exemples de cas d'usage concrets :**

Un cron job matinal lance un token drift scan et poste les résultats dans un canal Slack dédié. Un membre de l'équipe interroge le bot en direct : "Quelle est l'échelle de spacing actuelle ?" — le bot lit les fichiers de tokens réels et répond, sans qu'on ait besoin de naviguer jusqu'à la documentation. Un job hebdomadaire automatisé surveille les releases des systèmes concurrents (Polaris, Carbon, Primer) et poste un résumé.

## Contrainte de sécurité critique

[[romina-kavcic]] formule explicitement la frontière : accès en **lecture seule** sur un **clone** des fichiers de tokens et de la documentation, pas sur le codebase de production. L'assistant est un "team assistant with a read-only badge, not an engineer with push access."

Cette contrainte est cohérente avec [[niveaux-confiance-actions-agentiques]] : un agent avec accès en écriture au codebase de production opère à un niveau de confiance qui requiert une supervision humaine systématique. Un agent avec accès en lecture seule à un clone peut opérer de manière autonome sans risque de dommage irréversible.

## Position dans l'écosystème d'outils

Ce pattern complète les Skills ([[architecture-skills-rules-instructions]]) et le MCP ([[mcp-model-context-protocol]]) en ajoutant la dimension temporelle : alors que les Skills et MCP répondent à des requêtes synchrones dans une session de travail, l'assistant 24/7 opère de manière asynchrone et permanente. C'est moins un outil de génération de composants qu'une infrastructure de support et de monitoring.

## ⚡ Tension

Le self-hosting implique une charge de maintenance que les équipes SaaS n'ont pas. Un VPS Hetzner à 5$/mois est peu cher en argent mais pas en temps de configuration et de maintenance. Pour une petite équipe design system déjà sous pression capacitaire, ajouter de l'infrastructure serveur à maintenir peut coûter plus qu'il n'économise. Le calcul dépend du volume de tâches récurrentes que l'assistant automatise réellement.
