---
type: source
tags: [design-system, agentic, mcp, figma, specs, accessibilite, uber, open-source, cursor]
created: 2026-06-24
updated: 2026-06-24
sources: []
related:
  - "[ian-guisard](../entities/ian-guisard.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[generation-spec-agentique](../concepts/generation-spec-agentique.md)"
  - "[pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)"
  - "[accessibilite-continue](../concepts/accessibilite-continue.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[skills-avant-mcp](../concepts/skills-avant-mcp.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
---

## Uber Engineering Blog — "How Uber Built an Agentic System to Automate Design Specs in Minutes"

**Auteur** : Ian Guisard, Lead du Base design system chez Uber
**Date** : 11 mars 2026
**URL** : https://www.uber.com/us/en/blog/automate-design-specs/

## Thèse principale

Le documentation lag — l'écart structurel entre la réalité des composants et leur spec documentée — est résolu à Uber par un système agentique nommé uSpec : un agent Cursor connecté à Figma via le Figma Console MCP (open-source, développé par Southleft). L'agent crawle la structure réelle du composant dans Figma, extrait tokens, variables et sous-composants, puis génère des pages de spec complètes directement dans le fichier Figma en quelques minutes. Ce qui prenait des semaines de travail manuel se fait désormais en une seule passe.

## Apport spécifique

La source illustre concrètement la combinaison **skills agentiques + MCP** pour la génération de specs à grande échelle dans un contexte enterprise (7 stacks d'implémentation : UIKit, SwiftUI, Android XML, Android Compose, Web React, Go, SDUI). Elle introduit une architecture à deux couches : les agent skills portent la connaissance métier (schémas de validation, règles, documentation API de référence), et le MCP fournit l'accès déterministe aux données Figma. Ni l'un ni l'autre ne suffit seul : les plugins programmatiques extraient les données sans les interpréter ; les LLMs interprètent sans avoir accès aux données réelles. uSpec combine les deux.

## Citations clés

- "Programmatic plugins can extract component data from Figma, but they can't interpret what that data means." (Ian Guisard)
- "The agent doesn't guess at property names—it selects from documented APIs." (Ian Guisard)
- "No proprietary design data ever leaves your network." (Ian Guisard — sur la sécurité enterprise)
- "We built the Figma Console MCP because we needed it for our own enterprise engagements." (TJ Pitre, Southleft)

## Cas d'usage emblématique : la spec screen reader

Le cas le plus frappant est la génération des specs d'accessibilité : une section screen reader couvrant VoiceOver (iOS), TalkBack (Android) et ARIA (Web) est générée en moins de 2 minutes. Manuellement, cette section requiert des heures de cross-référencement de documentation de plateforme. Le skill screen reader charge les références d'API d'accessibilité spécifiques à chaque plateforme avant d'analyser le composant — le LLM sélectionne depuis des APIs documentées plutôt que d'halluciner des valeurs de propriétés.

## Architecture technique

1. **Figma Console MCP** (open-source, Southleft) : connexion locale entre l'agent Cursor et Figma Desktop via WebSocket — aucune donnée ne quitte le réseau local.
2. **Agent skills** : fichiers d'instruction par section de spec (Anatomy, API, Properties, Color annotation, Structure, Screen reader), chacun chargant ses propres règles de validation et schémas structurés.
3. **Rendu direct dans Figma** : l'agent importe le template de documentation depuis la librairie, le détache, et le peuple — textes, tableaux, marqueurs anatomiques — via le MCP.

## Connexions avec le wiki

- Enrichit [generation-spec-agentique](../concepts/generation-spec-agentique.md) — nouveau concept créé lors de cette ingestion
- Enrichit [pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md) — variant de génération (specs structurées vs documentation narrative)
- Enrichit [accessibilite-continue](../concepts/accessibilite-continue.md) — cas concret de génération multi-plateforme des specs screen reader
- Renforce [skills-avant-mcp](../concepts/skills-avant-mcp.md) — chaque section de spec est un skill distinct avec ses propres règles
- Renforce [processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md) — nouvelle implémentation à grande échelle (centaines de composants, 7 stacks)
- Renforce [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md) — MCP comme couche d'accès déterministe aux données Figma
