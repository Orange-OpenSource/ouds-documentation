---
type: source
tags: [design-system, ia, agentique, architecture, mcp, self-healing, orchestration, benchmark]
created: 2026-06-18
updated: 2026-06-18
sources: []
related:
  - "[[romina-kavcic]]"
  - "[[boucle-feedback-infrastructure]]"
  - "[[protocole-pas-produit]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[seeds-vs-trees]]"
  - "[[mcp-model-context-protocol]]"
  - "[[systeme-design-proactif]]"
---

## The Self-Healing Design System

**Auteur** : [[romina-kavcic]]
**Publication** : thedesignsystem.guide (Substack)
**Date** : 2026-04-04
**URL** : https://learn.thedesignsystem.guide/p/the-self-healing-design-system
**Fichier brut** : `raw/The Self-Healing Design System.md`
**Partie** : Agentic Design Systems, Part 3

⚠️ **Note** : le fichier brut est tronqué. Seules l'introduction et la section architecture sont disponibles. L'article promet également les sections "what AI genuinely cannot do" et "three phases you can start this week" — absentes du raw.

## Résumé

Troisième et dernière partie de la série "Agentic Design Systems" de Kavcic. Là où les parties 1 et 2 posaient le cadre conceptuel (le design system comme couche sémantique, l'IA comme utilisateur), la partie 3 décrit l'architecture de production qu'elle a construite et maintient depuis un an, et la boucle self-healing qui l'anime.

## Architecture de production

Au centre : **Claude Code** comme couche d'orchestration. Connecté via MCP à : Figma (via le plugin Tidy), GitHub, Storybook, PostHog (analytics), Granola (notes de réunion), Sentry (monitoring d'erreurs), la couche de documentation, et le dashboard Observatory.

La liste complète de MCP dans cet usage : Figma/Tidy, GitHub, Storybook, Chromatic, Granola, Notion, Jira, Stylelint, Linear, Mintlify, PostHog, Sentry. C'est l'instance la plus complète et la plus documentée d'une architecture de design system agentique en production.

## Le principe "protocole, pas produit"

La proposition architecturale clé : **la couche d'orchestration est remplaçable**. Parce que tout s'intègre via MCP, Kavcic a testé Cursor, Codex et d'autres outils dans la même architecture. Le fait de construire sur un protocole plutôt que sur un produit signifie que si un meilleur outil émerge demain, il remplace le centre sans qu'aucune des intégrations ne soit reconstruite. Voir [[protocole-pas-produit]].

## Benchmark multi-modèles

Kavcic exécute les mêmes exercices sur tous les nouveaux modèles à leur sortie : Gemini, GPT 5.2 à 5.4, Llama, Mistral, Cursor, Codex. Claude Code "consistently delivered the best results for design system work, particularly in reasoning about component relationships and token semantics." Ce benchmark est le seul dans le vault à être spécifiquement ciblé sur le raisonnement de design system (nommage de tokens, composition de composants, raisonnement au niveau système) plutôt que sur des tâches de code généraliste.

## La boucle self-healing

La boucle est formalisée en 4 étapes : **Watch** (détecter la dérive dans les tokens, composants, documentation) → **Analyze** (scorer la sévérité, prioriser les correctifs) → **Execute** (générer des PRs, mettre à jour la documentation, synchroniser les tokens) → **Observe** (vérifier les résultats et reboucler). C'est la forme la plus opérationnelle et la plus concrète de la [[boucle-feedback-infrastructure]] dans le vault. Voir aussi [[systeme-design-proactif]] pour la version prospective.

## La fondation comme prérequis absolu

"This architecture only works because the foundation is solid. Without clean token naming, without component descriptions, without intent documentation, the agent has nothing meaningful to work with." Cette phrase est la validation empirique la plus directe de [[seeds-vs-trees]] dans le vault — non pas comme principe théorique mais comme constat opérationnel après un an de production.

## Citations clés

"The architecture doesn't lock you in. If a better tool shows up tomorrow, you swap the center, and everything else stays the same. That's the point of building on a protocol, not a product." ([[romina-kavcic]])

"Claude Code consistently delivered the best results for design system work, particularly in reasoning about component relationships and token semantics." ([[romina-kavcic]])

"Without clean token naming, without component descriptions, without intent documentation, the agent has nothing meaningful to work with." ([[romina-kavcic]])
