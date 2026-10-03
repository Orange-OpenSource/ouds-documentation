---
type: source
tags: [design-system, mcp, storybook, composants, contrat, self-healing, accessibilite, claude-code, benchmark]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[storybook](../entities/storybook.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[accessibilite-continue](../concepts/accessibilite-continue.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
---

## Storybook MCP for AI-aware component libraries

**Auteur** : Ikeh Akinyemi
**Publication** : LogRocket Blog
**Date** : 2026-07-06
**URL** : https://blog.logrocket.com/storybook-mcp-component-libraries/
**Fichier brut** : `raw/Storybook MCP for AI-aware component libraries.md`

## Résumé

Démonstration technique pas à pas du serveur MCP intégré à Storybook 10.3 (`@storybook/addon-mcp`), avec comparaison contrôlée avant/après sur un agent Claude Code chargé de générer un formulaire de login. L'article documente concrètement ce que [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md) mentionne déjà comme quatrième point d'entrée MCP de l'écosystème design system (aux côtés d'Indeed, New York State et Tidy/Kavcic) : Storybook comme source de vérité, cette fois avec du code réel, des captures d'écran et des chiffres avant/après.

## Ce que le serveur expose

Six outils répartis en trois toolsets. Le **toolset docs** (`list-all-documentation`, `get-documentation`, `get-documentation-for-story`) gère la découverte de composants et le lookup de props. Le **toolset dev** (`get-storybook-story-instructions`, `preview-stories`) gère l'écriture de stories et la prévisualisation live. Le **toolset test** (`run-story-tests`) exécute des tests de composants et d'accessibilité et retourne des résultats structurés. Le toolset docs s'appuie sur des manifests de composants (JSON structuré généré au build depuis les stories), actuellement React-only.

## Démonstration avant/après

Sans `AGENTS.md` ni outils MCP connectés, Claude Code repère l'existence de composants Button et TextInput dans le projet mais écrit quand même 263 lignes de HTML natif avec sa propre logique de validation et des classes Tailwind ad hoc, sans aucun appel d'outil. Avec `AGENTS.md` et le serveur MCP actifs, le même prompt déclenche six appels d'outils *avant* la moindre ligne de code (instructions de story, index des composants, documentation Button, documentation TextInput, lecture de fichiers existants, confirmation du framework installé), puis produit 188 lignes qui importent et composent les vrais composants du design system, avec chaque prop conforme au contrat documenté.

## La boucle self-healing du test loop

Premier `run-story-tests` : 3 échecs sur 5 stories, cause identifiée par l'agent lui-même (label non lié à l'input via `htmlFor`/`id`, à la fois échec de test et violation d'accessibilité). L'agent corrige seul le composant partagé `TextInput` (id dérivé du label, `aria-invalid`, `aria-describedby`), relance les tests, obtient 5/5. Point notable : la correction ne porte pas sur le formulaire généré mais sur le composant partagé du design system lui-même — chaque autre story consommant `TextInput` bénéficie donc immédiatement de la correction d'accessibilité, sans intervention humaine entre la détection et le fix.

## Apport net par rapport aux sources déjà ingérées

Le vault documentait déjà la boucle self-healing au niveau conceptuel (Watch/Analyze/Execute/Observe de Kavcic dans [self-healing-design-system](self-healing-design-system.md)) et au niveau semi-manuel (rapport → diagnostic humain → correctif, [agent-orchestration-for-design-systems](agent-orchestration-for-design-systems.md)). Cette source est la première du vault à documenter une instance *entièrement automatisée* et vérifiable (code avant/après, nombre d'appels d'outils, résultats de tests) où l'agent détecte, diagnostique et corrige lui-même un composant partagé, sans validation humaine intermédiaire. Elle illustre aussi de façon concrète le [composant-comme-contrat](../concepts/composant-comme-contrat.md) : le contrat de props (`get-documentation`) est ce qui empêche l'hallucination, démontré par la différence de comportement du même agent avec et sans accès à ce contrat.

## Citations clés

"The result often looks close enough at first glance, but it relies on invented APIs and ignores decisions your codebase has already made." (Ikeh Akinyemi)

"The fix the agent made was not to the login form, but to the shared TextInput component in the design system." (Ikeh Akinyemi)
