---
type: concept
tags: [design-system, format, standard, ia, orchestration, agents-md, coding-agents, gouvernance]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)"
related:
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[design-md-format](design-md-format.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[dispersion-decision-design](dispersion-decision-design.md)"
  - "[murphy-trueman](../entities/murphy-trueman.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
---

## Le format AGENTS.md

AGENTS.md est le plus ancien des trois formats de la nouvelle pile agent-facing (avec [design-md-format](design-md-format.md) et SKILL.md décrit dans [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)). Il vit à la racine du dépôt de code et joue un rôle spécifique : dire aux coding agents comment opérer à l'intérieur du projet ([your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)).

Ce que le fichier porte : commandes de build et de test, règles de lint, conventions de nommage, limites de modification (ce qu'on peut modifier sans approbation, ce qu'il ne faut pas toucher). L'analogie la plus précise est le briefing d'un premier jour : les informations opérationnelles qu'on transmettrait à un ingénieur arrivant sur le projet.

## Ce que AGENTS.md n'est pas

AGENTS.md n'est pas de la documentation sur le design system. C'est la couche d'orchestration qui indique à l'agent *où trouver* cette documentation. Pour un projet avec un design system, il pointe vers : le fichier tokens source, la librairie de composants, les MCP servers à consulter, les fichiers DESIGN.md ou CLAUDE.md qui portent les règles de design. "AGENTS.md is not, in itself, documentation about your design system. It's the orchestration layer." ([murphy-trueman](../entities/murphy-trueman.md))

Cette distinction est opérationnellement importante : enrichir AGENTS.md avec les règles du design system lui-même est une erreur. Le fichier enfle, le coût en tokens monte plus vite que l'utilité, et l'agent traite de l'information redondante à chaque interaction. Factory le formule directement : "Long files slow the agent and bury signal."

## Origine et adoption

OpenAI a publié la spec AGENTS.md en août 2025, puis l'a donnée à la Linux Foundation's Agentic AI Foundation en décembre 2025. Soutenu par Codex, Cursor, Windsurf, GitHub Copilot, et de nombreux autres coding agents. Claude Code utilise CLAUDE.md à la place, mais les formats sont interchangeables en pratique — beaucoup d'équipes créent un symlink entre les deux.

## Inconsistance de comportement entre agents

Le fichier est portable mais son comportement ne l'est pas entièrement. Codex parcourt le dépôt depuis la racine vers le bas et laisse le fichier le plus proche gagner. Cursor fusionne les fichiers trouvés. Certains outils traitent AGENTS.md comme du contexte toujours actif ; d'autres ne le chargent que quand ils le jugent pertinent. Les équipes qui dépendent d'un comportement précis de précédence doivent vérifier comment leur agent spécifique traite le fichier.

## Structure et bonnes pratiques

Le format est du Markdown pur, sans structure requise. La spec recommande : Project Overview, Development Environment, Build and Test Commands, Code Style Guidelines, Testing Instructions. La meilleure pratique communautaire converge sur moins de 150 lignes. Au-delà de ce seuil, le coût en tokens croît plus vite que l'utilité apportée — la densité du signal baisse.

Pour un projet avec design system, les sections les plus utiles à inclure : où vit la bibliothèque de composants et quand l'utiliser en priorité sur la génération, où vivent les tokens et pourquoi ne pas hardcoder des valeurs, quels MCP servers consulter (Storybook, Zeroheight), quel fichier porte l'identité visuelle canonique (DESIGN.md ou équivalent), quelles zones sont modifiables sans revue et lesquelles ne le sont pas.

## Relation avec les autres couches

Dans l'architecture décrite par [diana-wolosin](../entities/diana-wolosin.md) et [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) (voir [mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md) et [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)), AGENTS.md / CLAUDE.md joue le rôle de routeur stratégique. Il orchestre les Rules (contraintes passives always-on par contexte), les Skills (capacités on-demand), et les MCP servers (knowledge structuré à la demande). La valeur d'AGENTS.md est précisément qu'il empêche l'agent d'ignorer les sources d'autorité du projet — sans ce routeur, l'agent fait de l'[exploration](mode-exploration-vs-navigation.md) plutôt que de la navigation.

La relation avec [design-md-format](design-md-format.md) est complémentaire et dirigée : AGENTS.md contient typiquement une ligne référençant DESIGN.md comme source canonique pour les décisions d'identité visuelle. DESIGN.md ne fait pas référence à AGENTS.md. AGENTS.md est le point d'entrée qui rend tous les autres formats découvrables.

## Priorité d'adoption

Trueman argumente qu'AGENTS.md est le format à adopter en premier si une équipe ne doit en choisir qu'un : quelques heures de rédaction produisent un fichier consulté par la plupart des coding agents sur toutes les tâches quotidiennes ([your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)). Le ROI est immédiat et transversal à l'ensemble des interactions agent/codebase. Cette priorité est cohérente avec le diagnostic de [mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md) : sans couche de contexte always-on, les fondations du design system ne sont jamais chargées dans les sessions agent.

## ⚡ Tension : portabilité du fichier vs inconsistance d'exécution

Le fichier AGENTS.md est lisible partout — n'importe quel agent qui supporte le format peut lire le Markdown. Mais ce qu'il *fait* de ce fichier varie significativement d'un agent à l'autre. Cursor merge les fichiers trouvés dans différents dossiers ; Codex laisse le plus proche gagner ; d'autres le chargent de façon sélective. L'inconsistance d'exécution est le même problème que Trueman identifie pour SKILL.md : le format est une convention de facto, pas un standard normalisé. Les équipes qui s'appuient sur un comportement de précédence spécifique ou sur un chargement systématique peuvent constater des divergences entre agents. La portabilité du contenu ne garantit pas la portabilité du comportement.
