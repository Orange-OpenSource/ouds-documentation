---
type: entity
tags: [outil, design-system, ia, miro, mcp, skills, pratique]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)"
related:
  - "[andressa-lombardo](andressa-lombardo.md)"
  - "[eddie-machado](eddie-machado.md)"
  - "[ia-comme-nouvelle-recrue](../concepts/ia-comme-nouvelle-recrue.md)"
  - "[skills-avant-mcp](../concepts/skills-avant-mcp.md)"
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
---

## Aura (Miro)

Aura est le nom interne de l'AI design system practice de Miro — pas un outil unique, mais le stack complet construit par l'équipe sur un an : documentation restructurée, métadonnées d'icônes et tokens, un MCP server, des Claude Code skills et des workflows de contribution agentique. Six personnes au service de 48+ product teams.

## Profil de personnalité

[andressa-lombardo](andressa-lombardo.md) et [eddie-machado](eddie-machado.md) ont délibérément donné un nom et un profil à leur IA : "extrêmement enthousiaste, très capable, et extrêmement littérale." Elle essaie tout ce qu'on lui soumet, mais elle ne connaît rien des conventions Miro et a zéro tolérance pour l'ambiguïté. Travailler avec elle ressemble à travailler avec n'importe quelle nouvelle recrue : "where's this library?", "how come we don't have this variant?", "where can I find this?"

Ce nommage n'est pas cosmétique — il incarne la reformulation de la méthode de travail (voir [ia-comme-nouvelle-recrue](../concepts/ia-comme-nouvelle-recrue.md)). Nommer la pratique signifie qu'on lui prépare des onboarding materials, pas des configurations.

## Stack technique

Le MCP server Miro expose deux outils : `list components` et `get component docs`. Simple par construction — [eddie-machado](eddie-machado.md) a résisté à la tentation de sur-ingénierie. Une instruction de routage dans le fichier Claude root pointe Aura vers ce MCP pour toutes les questions composants.

Les limites du MCP (docs internes Miro rendues en React, non crawlables par les agents) ont été contournées par des Claude Code skills : `search icons` et `search tokens`. Le skill de recherche d'icônes est passé de 33 000 à 410 tokens après compression avec `/simplify`. Un `wrap-up` skill automatise la création de PRs. Un workflow Jira permet à Aura de prendre des tickets tagués "Aura ready", d'exécuter le travail et de soumettre les PRs.

## Résultats mesurés

Questions Slack dans le canal design system : **–70 à 80 %** après la mise en place du MCP + instruction de routage. Lors du premier bug-bash avec le workflow Jira : **17 PRs en une heure**.

## Posture opérationnelle

Aura est documentée comme un travail en cours, pas un état fini. [andressa-lombardo](andressa-lombardo.md) insiste : "A lot of this is still trial and error, a lot of it is still in the testing phase. This is the potential the team sees, not the finished state." Cette honnêteté est elle-même instructive — c'est la posture [seeds-vs-trees](../concepts/seeds-vs-trees.md) appliquée à un cas réel.
