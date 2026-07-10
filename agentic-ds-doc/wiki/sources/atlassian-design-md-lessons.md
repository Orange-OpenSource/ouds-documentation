---
type: source
tags: [design-system, design-md, mcp, benchmark, atlassian, portabilité, production, prototypage]
created: 2026-06-26
updated: 2026-06-26
sources: []
related:
  - "[[design-md-format]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[metriques-adoption-ia-design-system]]"
  - "[[readable-vs-usable-token]]"
  - "[[systeme-de-design-agentique]]"
---

## Atlassian's DESIGN.md is here: what we learned testing portable design context in practice

**URL** : https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice
**Auteurs** : Kylor Hall (Principal Prompt Engineer) + Andrew Campbell (Senior Design Technologist), Atlassian
**Date** : 15 juin 2026

## Thèse principale

DESIGN.md est un format de portabilité, pas un remplacement pour un MCP ou des AI skills. Dans un contexte de production avec codebase existante, il consomme 92% plus de tokens que le MCP pour seulement 30% du contexte disponible. Sa valeur réelle est pour le prototypage, l'interopérabilité cross-tools et le theming client.

## Contribution empirique centrale

Premier benchmark contrôlé publié comparant DESIGN.md à un MCP design system sur une tâche de production réelle (écran login, ADS Atlassian) :

| Approche | Contexte DS | Tokens moyens | Temps moyen | Turns moyens |
|---|---|---|---|---|
| No context | ~5% | 4,20M | 6m19s | 43 |
| ADS MCP | **~80%** | **3,75M** | **5m1s** | **35,1** |
| ADS skill | ~80% | 4,43M | 5m23s | 36 |
| DESIGN.md | ~30% | 7,21M | 6m46s | 45,3 |

NB : résultats non conclusifs en dehors du contexte ADS — modèle, prompts, qualité des sources et environnement influent les résultats.

## Distinction conceptuelle clé

DESIGN.md est une **spec for reimplementing** (l'agent déduit comment reconstruire le système depuis zéro à partir de ses propriétés). Un MCP est un **guide for using** (l'agent sait comment importer et utiliser les composants existants). En production, c'est le second qu'on veut — et DESIGN.md produit systématiquement le mauvais comportement : agents qui recréent les composants plutôt que de les importer.

## Trois limites structurelles

Chargement all-at-once vs on-demand (coût et troncature de contexte) ; compression forcée (DESIGN.md Atlassian = 80 KB / ~19 800 tokens vs 2,5 MB de contenu ADS disponible on-demand) ; orientation "reimplementation" incompatible avec les codebases de production.

## Quatre cas d'usage légitimes

Direction artistique haut niveau ; prototypage rapide dans des environnements inconnus (blue-sky, nouvel outil, sans stack configuré) ; interopérabilité avec des design tools qui customisent des composants pré-construits ; **customer theming for adaptive UIs** — permettre aux clients d'une plateforme de décrire leur marque pour que les outputs IA générés reflètent leur identité.

## Citations clés (≤ 15 mots)

> "DESIGN.md is a useful portability format as a snapshot, not a replacement."

> "A production codebase is a very different environment to building from scratch."

> "We'd rather shape this standard than just react to it."

## Connexions identifiées

La limite #1 (chargement all-at-once) est la preuve empirique du problème théorisé dans [[mcp-on-demand-vs-rules-always-on]] : la distinction on-demand/always-on est maintenant quantifiée en tokens et en temps de réponse. La limite #3 (spec for reimplementing) introduit une dimension que le wiki n'avait pas : la différence entre décrire le système pour le refaire et le documenter pour l'utiliser. Le cas customer theming est un nouveau pattern d'usage agentique non encore présent dans le vault.
