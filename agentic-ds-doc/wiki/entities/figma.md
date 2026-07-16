---
type: entity
tags: [outil, organisation, figma, mcp, design]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md)"
  - "[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md)"
related:
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
  - "[ecriture-agents-canvas-design](../concepts/ecriture-agents-canvas-design.md)"
  - "[generation-spec-agentique](../concepts/generation-spec-agentique.md)"
  - "[jesse-gardner](jesse-gardner.md)"
---

## Figma

Figma est l'outil de design d'interface le plus cité dans le vault, mais sans fiche entité dédiée jusqu'à cette ingestion malgré des dizaines de mentions dans [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md), [code-source-de-verite-mcp](../concepts/code-source-de-verite-mcp.md), [pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md) et [generation-spec-agentique](../concepts/generation-spec-agentique.md).

**Le Figma MCP server** (Dev Mode MCP server, lancé en beta juin 2025) expose aux agents le contexte design d'un fichier Figma : composants, styles, variables, variable code syntax, et [Code Connect](../concepts/code-source-de-verite-mcp.md) quand il est configuré. Documenté du point de vue éditeur dans [figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md) : trois usages (génération de composant alignée, automatisation de tokens, audit d'alignement design/code) et une fonctionnalité de génération automatique de fichier de règles depuis un scan de codebase (tokens, composants, hiérarchies de style, conventions de nommage).

**Le passage de la lecture à l'écriture** (MCP beta, 24 mars 2026) est le tournant documenté par [victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md) : un agent connecté peut désormais créer des frames, placer des composants et modifier des designs existants directement dans le canvas, pas seulement lire le contexte. Voir [ecriture-agents-canvas-design](../concepts/ecriture-agents-canvas-design.md) pour l'analyse de ce changement de régime.

**Figma Skills**, introduites au même moment que le MCP en écriture, sont des fichiers Markdown qui définissent comment un agent doit travailler dans Figma — skill fondationnel `figma-use`, extensible par skills custom d'organisation (`figma-create-design-system-rules`, `figma-generate-design`, `figma-implement-design`). Voir [architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md).

Figma est aussi le canal d'écriture direct utilisé par uSpec chez Uber (via le Figma Console MCP open-source de Southleft) pour générer des spécifications de composants directement dans le fichier — précédent documenté avant même le MCP en écriture officiel de Figma. Voir [generation-spec-agentique](../concepts/generation-spec-agentique.md).
