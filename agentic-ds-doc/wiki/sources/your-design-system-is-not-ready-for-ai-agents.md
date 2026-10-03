---
type: source
tags: [design-system, ia, mcp, gouvernance, documentation, conférence, benchmark, spotify, github, indeed]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[documentation-lag](../concepts/documentation-lag.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[seeds-vs-trees](../concepts/seeds-vs-trees.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[brad-frost](../entities/brad-frost.md)"
  - "[jan-six](../entities/jan-six.md)"
  - "[sil-bormuller](../entities/sil-bormuller.md)"
  - "[into-design-systems-conference](../entities/into-design-systems-conference.md)"
---

## Your Design System Is Not Ready for AI Agents

Article de [sil-bormuller](../entities/sil-bormuller.md), fondatrice d'Into Design Systems, publié le 10 avril 2026. Synthèse des cinq talks de l'AI Design Systems Conference 2026, chacun présentant un "failure mode" concret observé en production quand les équipes connectent leur design system à des agents IA.

## Thèses principales

L'article est organisé autour d'un constat simple : les design systems ont été construits pour des humains. Les agents IA les parsent différemment — ils extraient ce que le prompt demande, et comblent les lacunes avec leurs a priori issus des données d'entraînement. Quand ces a priori sont faux, le résultat semble correct en surface mais viole les fondations du système.

Cinq points de rupture sont documentés :

**1. La dérive documentaire** — [romina-kavcic](../entities/romina-kavcic.md) chiffre à 30-40 % le temps des équipes design system consacré à la maintenance pure (régressions d'accessibilité, mauvais usages de tokens, documentation désynchronisée). Pour un agent, une source qui dit une chose, les tokens une autre et les composants une troisième est catastrophique : il ne peut pas juger laquelle est juste. La réponse : un "self-healing loop" basé sur le framework IBM MAPE-K (Observe, Detect, Suggest, Fix, Learn), avec un drift-scoring engine alimenté par l'API Figma, les hooks CI et les analytics d'usage.

**2. Le Markdown brut dans un MCP sans benchmark** — [diana-wolosin](../entities/diana-wolosin.md) teste 77 composants, 8 configurations MCP, 1 056 prompts. Résultat : Markdown ~30 000 tokens par requête, 82 % de couverture, hallucinations présentes. JSON : précision identique ou supérieure, 80 % de tokens en moins, 5× moins cher annuellement ($300 vs $1 500). Règle : "JSON for MCP, Markdown for LLM." Indeed a produit 4 300 prototypes IA en 4 mois après avoir migré vers JSON.

**3. L'absence de niveaux de confiance par action** — Sans gouvernance de l'autonomie agentique, un agent qui a accès au design system peut merger des PRs, mettre à jour des tokens, modifier des APIs — sans validation humaine. [romina-kavcic](../entities/romina-kavcic.md) propose une hiérarchie par niveau de risque : auto-merge (linting, typos d'accessibilité), draft PR (mise à jour de valeurs de tokens, changements de description), suggest only (nouvelles APIs, changements breaking, décisions de gouvernance). [jan-six](../entities/jan-six.md) chez GitHub Primer va plus loin structurellement : les agents ne peuvent créer qu'une issue, jamais merger du code.

**4. Le MCP sans règles toujours actives** — [brad-frost](../entities/brad-frost.md) nomme le problème fondamental : le MCP est on-demand. Un prompt "build me a card" retourne les métadonnées de Card et Button. Il n'appelle pas les fondations (espacement, typographie, couleurs) — car elles ne sont pas dans le prompt. Le LLM comble ce vide avec ses propres hypothèses. Solution : progressive disclosure of context en trois couches — règles always-on pour les fondations (injectées dans chaque prompt), MCP on-demand pour les composants, AGENTS.md comme couche d'orchestration définissant quelles règles sont always-on, où trouver le MCP, et quels niveaux de confiance s'appliquent.

**5. Les définitions de composants monolithiques** — Spotify Encore a découvert que les agents IA contournaient le design system en allant directement sur Cursor, produisant du code non-Encore. Cause : la documentation monolithique (props + variants + styles + comportements + accessibilité + guidelines dans un seul fichier) impose une fenêtre de contexte massive pour un résultat partiel. Solution : trois couches architecturales indépendantes — Foundation (tokens et primitives), Style (apparence visuelle), Behavior (logique d'interaction). Chaque couche forme un "context bubble" plus petit, raisonnable séparément. Résultat : 220 000+ usages de styles partagés (50 % de croissance YoY), 93 % de satisfaction développeur.

## Citations clés

"Our docs are written for humans. The new user, AI, needs structured metadata, not documentation prose." ([diana-wolosin](../entities/diana-wolosin.md))

"You don't want agents to run in the wild. Some decisions will never go past level three because they'll always need human judgment." ([romina-kavcic](../entities/romina-kavcic.md))

"Plant seeds, not trees." — consensus des cinq speakers sur la stratégie de démarrage.

## Connexions

Cette source est la première synthèse conférence du vault : elle regroupe des contributions de [romina-kavcic](../entities/romina-kavcic.md), [diana-wolosin](../entities/diana-wolosin.md), [brad-frost](../entities/brad-frost.md) et [jan-six](../entities/jan-six.md) dans un cadre unifié des "failure modes". Elle n'introduit pas de concepts entièrement nouveaux pour les trois premiers intervenants (Kavcic, Wolosin, Frost sont déjà bien documentés), mais elle : (1) ajoute la dimension MAPE-K à [documentation-lag](../concepts/documentation-lag.md), (2) formalise le cadre [niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md), (3) introduit [jan-six](../entities/jan-six.md) et l'approche GitHub Primer, (4) ajoute l'architecture Spotify Encore à [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md).
