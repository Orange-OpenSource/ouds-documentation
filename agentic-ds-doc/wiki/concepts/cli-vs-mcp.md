---
type: concept
tags: [mcp, cli, ia, agents, outils, architecture]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
related:
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
---

## CLI vs MCP : deux modes complémentaires

Dans l'architecture d'un système de design agentique, deux approches de connexion aux outils coexistent et se complètent : CLI et MCP. [romina-kavcic](../entities/romina-kavcic.md) insiste sur le fait que les deux sont nécessaires — l'erreur serait de choisir l'un contre l'autre ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

## CLI : la vitesse

Le CLI (Command Line Interface) est adapté à l'exécution directe de commandes simples. Pas de serveur, pas de schéma, pas de négociation de protocole. C'est le chemin rapide : les designers peuvent commencer immédiatement avec les outils locaux, les workflows intra-outil (entièrement dans Figma par exemple) s'y prêtent parfaitement.

Exemple concret : une commande `token color.bg.danger` qui résout la valeur d'un token Figma directement depuis le terminal (`→ #DC2626`). Ou un script shell qui compose un pattern complet dans Figma en un appel HTTP direct à un plugin local. Zero infrastructure. Utile en minutes.

## MCP : l'échelle

Le [mcp-model-context-protocol](mcp-model-context-protocol.md) est adapté à l'orchestration multi-outils. Quand l'agent doit connecter Figma, GitHub, Storybook, la documentation et le CI dans un seul flux, MCP est la seule option viable. Il permet à l'agent de comprendre des données de design structurées (composants, tokens, variantes), de propager des changements de bout en bout (design → code → docs), et de faire tourner des agents autonomes en CI.

## La règle de décision

CLI quand le workflow reste dans un seul outil ou ne nécessite pas de raisonnement inter-outils. MCP quand l'agent doit "connecter les points" entre plusieurs sources de données — par exemple : "un token a changé dans Figma, quels composants l'utilisent, quelles pages sont affectées, quel est leur trafic, doit-on ouvrir un PR ?"

[romina-kavcic](../entities/romina-kavcic.md) décrit son propre setup comme utilisant les deux : l'API HTTP de Tidy pour la composition de patterns à vitesse CLI, et les données structurées MCP pour la couche d'orchestration ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).
