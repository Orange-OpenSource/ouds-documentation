---
type: entity
tags: [outil, ia, self-hosted, assistant, design-system, automation, open-source]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)"
related:
  - "[assistant-ia-24h](../concepts/assistant-ia-24h.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
---

## OpenClaw

OpenClaw (anciennement clawdbot, https://docs.openclaw.ai/) est un assistant IA open-source self-hosted. Il tourne 24/7 sur un serveur personnel (~5$/mois sur Hetzner VPS) et se connecte aux messageries d'équipe : Telegram, Slack, Discord, WhatsApp.

Capacités : accès fichiers et scripts, mémoire persistante entre conversations, cron jobs, choix du modèle (Claude, GPT, Gemini, DeepSeek). Voir [assistant-ia-24h](../concepts/assistant-ia-24h.md) pour les cas d'usage design system détaillés et la contrainte de sécurité critique (accès read-only sur clone, jamais sur le codebase de production).
