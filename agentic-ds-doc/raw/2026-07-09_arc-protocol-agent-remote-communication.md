---
source_url: https://arc-protocol.org/
author: arcprotocol (open-source)
published: 2026
ingested: 2026-07-09
---

# Agent Remote Communication (ARC) Protocol

Source brute — contenu issu de arc-protocol.org et de la documentation officielle.

## Description

ARC Protocol est un protocole RPC stateless pour systèmes multi-agents, avec chiffrement hybride post-quantique et routage multi-agents sur endpoint unique. Open-source, Python SDK disponible (pip install arc-sdk).

## Écosystème ARC

Trois composants forment l'écosystème :

**ARC Protocol** (couche de communication) : protocole RPC stateless, endpoint unique pour des centaines d'agents, routage intelligent par `targetAgent` / `requestAgent`, SSE streaming, traceId end-to-end.

**ARC Ledger** (registre de découverte) : registre centralisé maintenant les "agent cards" — capacités, endpoints, métadonnées. Requêtable pour découvrir quels agents sont disponibles et quelles sont leurs capacités.

**ARC Compass** (ranking sémantique) : système de ranking d'agents par algorithmes sémantiques et capability matching. Trouve l'agent optimal pour une tâche donnée parmi l'ensemble du Ledger.

## Caractéristiques techniques

- **Stateless RPC** : invocation de méthodes sans état de session — chaque requête est indépendante.
- **Endpoint unique** : des centaines d'agents spécialisés (finance, HR, support...) accessibles via un seul endpoint, avec routing intelligent côté protocole.
- **Quantum-safe TLS** : hybride X25519 (classique) + Kyber-768 (post-quantique, FIPS 203 ML-KEM). Protection future contre les menaces quantiques.
- **Workflow tracing** : propagation automatique du traceId à travers les interactions distribuées. Intégration LangFuse, OpenTelemetry.
- **Auth** : OAuth2 avec scope validation.
- **SDK Python** : ThreadManager (continuité conversationnelle), routing, auth, SSE.

## Flux de communication

```
Client → [Initiate] → ARC Protocol
ARC Protocol → [Query capabilities] → ARC Compass → ARC Ledger
ARC Ledger → [Agent cards] → ARC Compass
ARC Compass → [Ranking] → optimal agent sélectionné
ARC Protocol → [Secure comm] → agent cible
```

## Positionnement vs autres protocoles

- vs MCP : MCP est un protocole de contexte (outils et ressources exposés à un LLM). ARC est un protocole de communication inter-agents (RPC entre agents distincts). Complémentaires, pas concurrents.
- vs A2A (Google) : A2A adresse la collaboration inter-agents à haut niveau. ARC est plus bas niveau — un RPC stateless avec routing et sécurité.
- vs AG-UI : AG-UI est un protocole d'interface agent-frontend (SSE events). ARC est un protocole d'infrastructure agent-agent.

## Note de disambiguation

ARC Protocol (arc-protocol.org) est un projet distinct du [[protocole-arc]] de [[cristian-morales-achiardi]] (Audit → Report → Compose). La coïncidence de l'acronyme est fortuite. Le [[protocole-arc]] d'Achiardi est un cadre de maturité pour design systems agentiques ; ARC Protocol est un protocole réseau RPC pour communication inter-agents.
