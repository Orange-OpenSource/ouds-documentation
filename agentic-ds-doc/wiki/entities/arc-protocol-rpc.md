---
type: entity
tags: [protocole, infrastructure, multi-agent, rpc, communication, open-source]
created: 2026-07-09
updated: 2026-07-09
sources:
  - "[arc-protocol-agent-remote-communication](../sources/arc-protocol-agent-remote-communication.md)"
related:
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[orchestration-multi-agents](../concepts/orchestration-multi-agents.md)"
  - "[protocole-pas-produit](../concepts/protocole-pas-produit.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
---

## ARC Protocol (Agent Remote Communication Protocol)

> ⚠️ Disambiguation : à ne pas confondre avec le [protocole-arc](../concepts/protocole-arc.md) d'Achiardi (cadre de maturité Audit → Report → Compose pour design systems agentiques). La coïncidence de l'acronyme est fortuite.

ARC Protocol (arc-protocol.org) est un protocole RPC open-source pour la communication entre agents dans des systèmes multi-agents. Il répond au problème de prolifération d'endpoints : comment router des centaines d'agents spécialisés depuis un point d'accès unique, avec sécurité et observabilité garanties.

## Écosystème

L'écosystème ARC se compose de trois couches :

**ARC Protocol** est la couche de communication : protocole RPC stateless, endpoint unique, routing par `targetAgent` / `requestAgent`, SSE pour le streaming, traceId pour l'observabilité end-to-end.

**ARC Ledger** est le registre de découverte : il maintient les "agent cards" (capacités, endpoints, métadonnées) de tous les agents enregistrés. C'est la source de vérité de la topologie du système multi-agents.

**ARC Compass** est le moteur de ranking sémantique : il sélectionne l'agent optimal pour une tâche donnée en interrogeant le Ledger et en appliquant des algorithmes de capability matching.

## Caractéristiques techniques distinctives

Le chiffrement post-quantique hybride est la caractéristique la plus distinctive d'ARC dans le paysage des protocoles : X25519 (ECDH classique) combiné à Kyber-768 (FIPS 203 ML-KEM, post-quantique). Cette approche hybride protège les communications aujourd'hui et contre les futures menaces quantiques sans sacrifier la compatibilité actuelle.

Le traçage end-to-end via traceId automatique distingue ARC des protocoles plus simples : chaque interaction distribuée entre agents est traçable depuis l'initiation jusqu'à la réponse finale, avec intégration native LangFuse et OpenTelemetry.

## Position dans le paysage des protocoles agentiques

```
MCP (Model Context Protocol)  → expose outils et contexte à un LLM
AG-UI                         → connecte agents et frontends (SSE events)
A2A (Google)                  → collaboration inter-agents haut niveau
ARC Protocol                  → RPC inter-agents basse couche (routing, sécurité, observabilité)
```

ARC complète la pile là où MCP s'arrête : MCP dit à un agent ce qu'il peut *utiliser* (outils, ressources) ; ARC dit au système comment les agents se *parlent* entre eux. Les deux sont complémentaires.

## Références

- Site : https://arc-protocol.org/
- GitHub : https://github.com/arcprotocol/arcprotocol
- SDK Python : `pip install arc-sdk`
