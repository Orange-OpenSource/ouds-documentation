---
type: entity
tags: [outil, ia, notes, réunions, mcp]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-system-most-important-asset-ai-era]]"
related:
  - "[[mcp-model-context-protocol]]"
  - "[[systeme-de-design-agentique]]"
---

## Granola

Granola est un outil de prise de notes IA qui transcrit les appels en arrière-plan, sans bot visible dans la réunion. Il produit des résumés structurés, des action items et des prochaines étapes automatiquement à partir de la transcription.

Sa pertinence dans le contexte des design systems agentiques tient à son support MCP ([[mcp-model-context-protocol]]). Les notes de réunion Granola peuvent être connectées directement à Claude ou ChatGPT comme contexte interrogeable. Le workflow décrit par [[romina-kavcic]] : la réunion se termine, le résumé est disponible immédiatement, des recipes (prompts pré-écrits) permettent de générer des follow-ups ou de préparer la réunion suivante, Zapier pousse les action items vers Linear ou Jira, et MCP connecte tout l'historique à Claude comme contexte requêtable ([[design-system-most-important-asset-ai-era]]).

Granola est présenté comme une "couche de données supplémentaire" dans un système de design agentique : les décisions de design system prises en réunion deviennent un contexte structuré que l'agent peut interroger ("Qu'avons-nous décidé pour l'API du composant mardi dernier ?").
