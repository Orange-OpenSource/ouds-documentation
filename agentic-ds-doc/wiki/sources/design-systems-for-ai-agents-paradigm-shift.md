---
type: source
tags: [design-system, ia, agentique, mcp, context-architecture, jugement, machine-readable]
created: 2026-06-18
updated: 2026-06-18
sources: []
related:
  - "[vicente-g](../entities/vicente-g.md)"
  - "[architecture-contexte-agentique](../concepts/architecture-contexte-agentique.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[concevoir-les-conditions](../concepts/concevoir-les-conditions.md)"
---

## Design Systems for AI agents: The New Paradigm Shift

**Auteur** : [vicente-g](../entities/vicente-g.md)
**Publication** : Medium (personnel)
**Date** : 2026-05-15
**URL** : https://medium.com/@vicentegrafico.com/design-systems-for-ai-agents-the-new-paradigm-shift-ad097cfae228
**Fichier brut** : `raw/2026-05-15_design-systems-for-ai-agents-paradigm-shift.md`

## Résumé

Article de synthèse en 6 minutes qui reformule le rôle des design systems à l'ère des agents IA. Orientation analytique, sans données empiriques propres — mais avec une rigueur conceptuelle supérieure aux articles d'awareness classiques. La contribution principale est une reformulation de la question centrale : ce n'est plus "est-ce que les équipes humaines comprennent notre DS ?" mais "est-ce qu'un système IA peut comprendre, consommer et appliquer correctement notre DS ?"

## Thèses principales

**Thèse 1 — Exposer le jugement, pas seulement les composants.** "A Design System cannot limit itself to exposing components. It has to expose judgment." C'est la formulation la plus directe du vault sur ce sujet. Le jugement désigne la connaissance compositionelle implicite : non pas *quoi* utiliser, mais *comment*, *quand*, *pourquoi*, et *dans quelle relation avec quoi*. Voir [architecture-contexte-agentique](../concepts/architecture-contexte-agentique.md).

**Thèse 2 — L'UX vit dans les relations, pas dans les composants.** "UX Design does not live only inside components. It lives in the relationships between them." Un agent peut choisir les bons composants et produire une interface fausse — rythme absent, hiérarchie incorrecte, densité inadaptée, espacement générique. La correction ne réside pas dans de meilleurs composants mais dans l'encodage des règles de composition et de relation. Voir [architecture-contexte-agentique](../concepts/architecture-contexte-agentique.md).

**Thèse 3 — Le DS comme architecture de contexte.** "The Design System stops being only a component library and documentation hub, and starts becoming a context architecture." Cette reformulation introduit le concept de couches progressives de contexte : fondations d'abord (typo, espacement, couleur), règles composants à la demande, couche qualité/composition en dernier. Le contexte se charge en fonction de la phase de la tâche, pas d'un seul bloc.

**Thèse 4 — Le MCP comme orchestrateur des couches.** Vicente donne au MCP un rôle légèrement différent de [diana-wolosin](../entities/diana-wolosin.md) : non pas seulement un retriever on-demand, mais un orchestrateur qui connecte les couches de contexte. L'architecture idéale : MCP + Documentation structurée + Règles contextuelles + Vrais exemples + Couche qualité.

**Thèse 5 — Nouvelles responsabilités d'équipe.** L'article liste 8 responsabilités nouvelles pour les équipes DS, dont certaines absentes du corpus du vault : auditer si l'IA interprète le système correctement, créer des bons ET mauvais exemples intentionnellement, exposer les patterns comme des recettes réutilisables, définir des standards de qualité vérifiables, concevoir le système comme une knowledge API.

## Citations clés

"A Design System cannot limit itself to exposing components. It has to expose judgment." ([vicente-g](../entities/vicente-g.md))

"UX Design does not live only inside components. It lives in the relationships between them." ([vicente-g](../entities/vicente-g.md))

"The Design System stops being only a component library and documentation hub, and starts becoming a context architecture." ([vicente-g](../entities/vicente-g.md))

"When an agent cannot find a rule, it invents one." ([vicente-g](../entities/vicente-g.md))

"The future of Design Systems is not only about documenting better. It is about building context better." ([vicente-g](../entities/vicente-g.md))

## Connexions identifiées

Converge avec [ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md) (Wolosin) sur le reformatage du DS pour les machines. Converge avec [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md) (Wolosin) sur la limite intrinsèque du MCP seul. Approfondit [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md) (Kavcic) avec la distinction "composants vs relations entre composants". Rejoint [concevoir-les-conditions](../concepts/concevoir-les-conditions.md) (Morales Achiardi) sur l'encodage du jugement plutôt que des règles. Apporte le concept nouveau d'[architecture-contexte-agentique](../concepts/architecture-contexte-agentique.md) — couches progressives par phase de tâche.
