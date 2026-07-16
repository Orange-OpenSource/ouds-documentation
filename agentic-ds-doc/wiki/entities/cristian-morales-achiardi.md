---
type: entity
tags: [personne, design-system, ia, auteur, ingénieur]
created: 2026-06-17
updated: 2026-07-09
sources:
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[user-vs-maintainer-ia](../concepts/user-vs-maintainer-ia.md)"
  - "[format-toon](../concepts/format-toon.md)"
  - "[concevoir-les-conditions](../concepts/concevoir-les-conditions.md)"
  - "[designops-devops-seam](../concepts/designops-devops-seam.md)"
---

## Cristian Morales Achiardi

Cristian Morales Achiardi est designer et développeur spécialisé en design systems, auteur d'une série complète de 7 articles sur les "Agentic Design Systems" publiés sur Design Systems Collective (Medium) entre fin 2025 et mars 2026. Il tient également le site giorris.dev, où il publie son design system personnel, un dashboard de données, et un catalogue de Claude skills open-sourcé. Le design system d'Enara, documenté tout au long de la série, est son terrain d'expérimentation principal : il en est le seul designer, travaillant directement avec l'ingénierie sans équipe design.

Son approche est empirique et expérimentale : il construit sur sa propre codebase, mesure les résultats (11 essais contrôlés documentés dans [towards-agentic-design-system](../sources/towards-agentic-design-system.md)), et partage les données brutes publiquement (benchmark et rapport d'adoption en Google Docs ouverts). La série couvre l'infrastructure AI-ready, le système agentique, la documentation comme métadonnées structurées, l'indexation de codebase, l'orchestration, la gouvernance encodée, et — dans la partie conclusive — la couche humaine qui rend tout le reste opérant.

Sa contribution technique distinctive est le [protocole-arc](../concepts/protocole-arc.md) (Audit → Report → Compose) et l'usage du [format-toon](../concepts/format-toon.md) pour les index de composants. Il cite [diana-wolosin](diana-wolosin.md) et son article "Intent-Driven Context for AI Design Systems" comme parallèle théorique à son approche pratique. Sa position organisationnelle — sole designer sans équipe, sans politique d'adoption à négocier — lui permet de construire l'infrastructure sans friction institutionnelle, au prix d'une accountability totale sur les outputs : quand le système exécute une décision incorrecte, il n'y a personne d'autre à qui l'attribuer ([human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)).

En 2026, la série se prolonge avec deux articles qui développent le cadre conceptuel de la Phase 3 (Compose) : "Design systems are contracts, not libraries" (mai 2026, [design-systems-contracts-not-libraries](../sources/design-systems-contracts-not-libraries.md)) pose la distinction fondamentale — un design system est un contrat formel, pas une bibliothèque — et "Building language for design systems" (juillet 2026, [building-language-design-systems](../sources/building-language-design-systems.md)) explicite ce que "composer" signifie concrètement : parler le vocabulaire du système, en respecter la grammaire, exécuter ses contrats. Ces deux articles constituent le développement conceptuel attendu de la Phase 3 du [protocole-arc](../concepts/protocole-arc.md), et créent le concept de [langage-design-system](../concepts/langage-design-system.md) comme couche liant tokens, grammaire de composition et contrats de composants.
