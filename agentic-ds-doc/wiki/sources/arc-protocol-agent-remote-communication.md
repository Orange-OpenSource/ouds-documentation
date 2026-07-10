---
type: source
tags: [protocole, multi-agent, rpc, communication, sécurité, post-quantique, infrastructure]
created: 2026-07-09
updated: 2026-07-09
sources: []
related:
  - "[[arc-protocol-rpc]]"
  - "[[mcp-model-context-protocol]]"
  - "[[orchestration-multi-agents]]"
  - "[[protocole-pas-produit]]"
---

## Agent Remote Communication Protocol (ARC Protocol)

**Auteur** : arcprotocol (open-source)
**URL** : https://arc-protocol.org/
**GitHub** : https://github.com/arcprotocol/arcprotocol
**Ingestion** : 2026-07-09

> ⚠️ Disambiguation : "ARC Protocol" ici désigne le protocole réseau de arc-protocol.org. Ne pas confondre avec le [[protocole-arc]] d'Achiardi (Audit → Report → Compose), qui est un cadre de maturité pour design systems agentiques.

## Résumé

ARC Protocol est un protocole RPC stateless pour systèmes multi-agents, avec trois composants : le protocole de communication (endpoint unique + routing), ARC Ledger (registre de découverte d'agents), et ARC Compass (ranking sémantique d'agents). Caractéristiques distinctives : chiffrement post-quantique hybride (X25519 + Kyber-768) et traçage end-to-end via traceId.

## Positionnement dans le paysage des protocoles

ARC occupe une niche distincte dans la pile des protocoles agentiques 2026. MCP gère l'exposition d'outils et de contexte à un LLM. AG-UI gère la communication entre agents et frontends. A2A adresse la collaboration inter-agents à haut niveau sémantique. ARC est la couche RPC basse — le protocole réseau qui route les appels entre agents spécialisés avec garanties de sécurité et observabilité.

La métaphore du site : "Route hundreds of specialized agents through a single endpoint" — là où MCP expose les capacités, ARC les distribue.

## Apport au vault

Ajoute un protocole infrastructure au corpus existant — complémentaire à [[mcp-model-context-protocol]] et [[cli-vs-mcp]]. L'approche "single endpoint + intelligent routing" est une réponse architecturale au problème de prolifération d'endpoints multi-agents documenté dans [[orchestration-multi-agents]]. La sécurité post-quantique est un angle nouveau dans le corpus.
