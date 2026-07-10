---
type: source
tags: [design-system, agentique, ia, mcp, storybook, collaboration, vibe-coding, brad-frost]
created: 2026-06-18
updated: 2026-06-18
sources: []
related:
  - "[[brad-frost]]"
  - "[[systeme-de-design-agentique]]"
  - "[[mcp-model-context-protocol]]"
  - "[[seeds-vs-trees]]"
---

## Agentic Design Systems in 2026

**Auteur** : [[brad-frost]]
**Publication** : bradfrost.com
**Date** : 2025-12-16
**URL** : https://bradfrost.com/blog/post/agentic-design-systems-in-2026/
**Fichier brut** : `raw/2025-12-16_agentic-design-systems-2026-bradfrost.md`

⚠️ **Note** : article très court (3 paragraphes substantiels). L'essentiel du contenu est dans deux vidéos YouTube non transcrites et dans une promotion du cours "AI & Design Systems" (aianddesign.systems). L'ingest est proportionnel au contenu disponible.

## Résumé

Article-billet de Brad Frost (auteur d'Atomic Design) documentant sa participation à une démo Storybook sur DS+AI, et lançant son cours sur le sujet. La contribution conceptuelle principale est la distinction entre **DS+AI** et **vibe coding**, et l'introduction du terme **"mouth coding"** pour décrire des workflows collaboratifs où des membres non-techniques verbalisent des features qui s'implémentent en temps réel via les composants du design system.

## Thèses principales

**DS+AI vs vibe coding.** "This is what distinguishes DS+AI from vibe coding; the AI is deliberately constrained to using the high-quality design system materials to ensure what's being generated adheres to the organization's established standards." La contrainte au design system n'est pas une limitation — c'est précisément ce qui rend la génération IA exploitable en production, par opposition au vibe coding qui laisse l'IA improviser librement. Voir [[systeme-de-design-agentique]].

**Mouth coding.** Des membres non-techniques d'une équipe (PMs, chercheurs, content designers) peuvent "mouth coder" — verbaliser des features produit pendant une session collaborative — et voir le résultat émerger en temps réel via les composants du design system. C'est un nouveau mode de collaboration cross-disciplinaire rendu possible par DS+AI.

**Storybook MCP.** L'équipe Storybook a lancé un MCP qui permet de générer de l'UI en s'appuyant sur les bibliothèques de composants du design system. Nouvel outil dans l'écosystème, complémentaire au Figma MCP et au MCP Indeed.

## Citations clés

"This is what distinguishes DS+AI from vibe coding; the AI is deliberately constrained to using the high-quality design system materials to ensure what's being generated adheres to the organization's established standards." ([[brad-frost]])

"Non-technical team members can 'mouth code' a product feature during a collaboration session and collectively we can see things come to life using the production-grade foundations of the design system." ([[brad-frost]])

## Connexions identifiées

La contrainte DS+AI confirme [[seeds-vs-trees]] et [[lisibilite-machine-design-system]] depuis un angle différent : la valeur du design system est précisément sa capacité à contraindre la génération IA vers des standards établis. Storybook MCP s'ajoute aux outils documentés dans [[mcp-model-context-protocol]] (aux côtés de Figma MCP et MCP Indeed). Mouth coding est un concept d'usage, pas d'infrastructure — il illustre la valeur finale de DS+AI pour les équipes cross-disciplinaires.
