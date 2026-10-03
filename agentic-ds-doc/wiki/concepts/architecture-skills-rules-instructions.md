---
type: concept
tags: [design-system, orchestration, ia, skills, rules, instructions, claude-md, plugin, agents-md, skill-md]
created: 2026-06-17
updated: 2026-07-16
sources:
  - "[agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)"
  - "[machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)"
  - "[agent-workflows-design-system-teams](../sources/agent-workflows-design-system-teams.md)"
  - "[20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)"
  - "[your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)"
  - "[figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md)"
  - "[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md)"
related:
  - "[ecriture-agents-canvas-design](ecriture-agents-canvas-design.md)"
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[schema-metadata-composant](schema-metadata-composant.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[agents-md-format](agents-md-format.md)"
  - "[design-md-format](design-md-format.md)"
  - "[prompt-injection-design-system](prompt-injection-design-system.md)"
---

## Architecture d'instructions : Skills, Rules, Instructions

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) formalise l'architecture d'orchestration d'un système de design agentique en trois couches d'instructions distinctes, chacune avec un rôle précis ([agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)). Cette architecture répond à la question pratique : comment configurer un agent pour qu'il utilise le design system correctement, de manière consistante, à chaque session ?

## Skills : les outils

Les Skills sont des capacités exécutables qui effectuent des opérations spécifiques. Exemples : `/ai-component-metadata` génère la documentation structurée d'un composant, `/ai-ds-composer` guide la sélection de composants, `/codebase-index` régénère les cartes de dépendances. Propriété clé : les Skills sont **réutilisables entre projets**. Le générateur de métadonnées fonctionne sur n'importe quelle bibliothèque de composants qui suit le [schema-metadata-composant](schema-metadata-composant.md).

## Rules : le contexte

Les Rules sont des contraintes et guidelines passives qui se chargent selon le contexte de travail. Le schéma de métadonnées qui définit les champs requis. La hiérarchie de design atomique qui impose la direction des dépendances. La méthodologie de deep tracing qui enseigne le parcours récursif. Propriété clé : les Rules sont **spécifiques au projet**. Elles encodent *les décisions de votre système*, pas des conventions universelles.

Les rules s'activent par chemin de fichier (`paths: "src/components/.ai/**"`). Quand l'agent travaille avec des fichiers d'index, les règles de deep tracing se chargent automatiquement. Quand il travaille avec des fichiers de composants, les règles de composition se chargent. Le chargement est contextuel, pas global — pour éviter de bloater chaque conversation avec des instructions non pertinentes.

## Instructions : la stratégie

Les Instructions sont la méthodologie qui lie Skills et Rules. Quand charger le codebase index. Comment approcher différents types de requêtes. Quels artefacts produire et où ils alimentent. C'est la couche qui donne la cohérence d'ensemble.

## CLAUDE.md comme routeur

La hiérarchie complète : CLAUDE.md (le routeur) → pointe vers les Rules (contexte par chemin) → qui référencent les Skills (capacités réutilisables) → qui produisent des Artefacts (métadonnées, indexes, relations tracées).

CLAUDE.md n'est pas un fichier de documentation — c'est un système de routage. Il dirige l'agent vers les bonnes rules selon ce sur quoi il travaille, et les rules lui indiquent quels skills invoquer.

## Relation avec les trois couches de Kavcic

Cette architecture précise et enrichit la couche 3 (Raisonnement) des [trois-couches-composants-agents](trois-couches-composants-agents.md). Le "playbook" de Kavcic se décompose en : Rules (les règles de sélection et de composition encodées par projet) + Skills (les capacités d'exécution) + Instructions dans CLAUDE.md (la logique de chargement et d'orchestration). Les trois couches de Kavcic décrivent *quoi* avoir ; les trois couches de Morales décrivent *comment l'activer*.

## Note d'évolution

L'architecture a émergé des outils vers le haut, pas de la théorie vers le bas : les Skills ont été construits d'abord pour résoudre des problèmes concrets, puis les Rules ont été ajoutées pour donner le contexte projet, puis le chargement efficace a été conçu pour que les rules ne saturent pas chaque conversation. C'est une architecture pragmatique, pas un design a priori.

## Skills métier pour les design systems : exemples concrets

[romina-kavcic](../entities/romina-kavcic.md) ([20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)) nomme les Skills les plus utiles pour un design system team. **token-migration-assistant** détecte le format de tokens et migre entre Style Dictionary, W3C DTCG, Figma Variables, CSS, et Tailwind. **component-audit** lance des audits complets : accessibilité, theming, responsivité, qualité de code. **documentation-standards** génère des docs composant cohérentes avec le format de l'équipe. **brand-guidelines** applique les règles de la marque (couleurs, typographie, spacing, motion). **figma-variables-generator** génère du Figma Variables JSON depuis les design tokens.

La différence entre une bibliothèque de prompts et des Skills est opérationnelle : "A prompt library is a document people forget exists. A Skill auto-loads when Claude Code detects it is relevant. That difference is everything." Les Skills créent la cohérence d'équipe sans demander à chaque membre de mémoriser les règles.

**Format d'un Skill custom :** un fichier Markdown avec front matter YAML. Champs essentiels : `name`, `description`, `autoload` (condition de déclenchement). Chemin : `.claude/skills/` pour les Skills projet (versionnés, partagés avec l'équipe) ou `~/.claude/skills/` pour les Skills personnels.

**Exemple de token drift audit Skill** (`.claude/skills/token-drift-audit/SKILL.md`) : définit ce qu'il faut flagger (hex hardcodés, pixel spacing bruts, tokens primitifs utilisés directement dans les composants), ce qu'il faut vérifier (couverture des thèmes, références cassées, contraste WCAG AA, convention de nommage), et le format de sortie (severity critique/warning/info, chemin de fichier + ligne, token suggéré, compte récapitulatif). Exécuté avec `claude "Run a token drift audit on the components/ folder"`.

## Implémentation légère : les ADRs comme Rules sans infrastructure

[gerard-pamies](../entities/gerard-pamies.md) ([agent-workflows-design-system-teams](../sources/agent-workflows-design-system-teams.md)) documente une variante low-tech de cette architecture : au lieu de Rules encodées dans des fichiers `.ai/rules` chargés par chemin de fichier, il uploade directement les **ADRs (Architecture Decision Records)** dans un ChatGPT Project. L'effet est analogue — l'agent dispose des décisions de design comme contexte passif — mais sans l'automatisation du chargement contextuel.

Cette approche confirme le principe fondamental de la couche Rules : ce qui compte n'est pas le mécanisme (fichier `.ai/rules` vs upload dans un Project), mais la présence d'un contexte de décisions encodé que l'agent peut référencer. La différence est de scalabilité et de pérennité : les ADRs uploadés manuellement peuvent être oubliés ou désynchronisés ; les Rules always-on sont systématiquement chargées. Voir [workflows-agent-sans-mcp](workflows-agent-sans-mcp.md) pour le contexte complet de l'approche Pàmies.

## SKILL.md dans la pile des formats agent-facing : recette, pas description

[murphy-trueman](../entities/murphy-trueman.md) précise la nature de SKILL.md dans le contexte plus large des trois formats (AGENTS.md, SKILL.md, DESIGN.md) ([your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)). Un Skill est une procédure — il dit à l'agent *comment faire* quelque chose, étape par étape, avec les cas limites traités en route. "A Skill is best understood as a recipe rather than a description of your design system." Ce qui le distingue d'[AGENTS.md](agents-md-format.md) (instructions opérationnelles sur le projet) et de [DESIGN.md](design-md-format.md) (identité visuelle compressée) : le Skill encode le *savoir-faire*, pas le *contexte*. Le système de métadonnées qu'il consulte en cours d'exécution vit ailleurs.

Deux propriétés importantes du format SKILL.md : la portabilité du fichier est réelle (n'importe quel agent qui supporte le format peut lire le Markdown), mais l'exécution n'est pas consistante. "Different tools load Skills differently, invoke them with different triggers, and handle their nested scripts and references with their own conventions. The file will be readable everywhere, though that doesn't mean it will run the same way everywhere." Le format est une convention de facto portée par Anthropic et OpenAI, pas un standard normalisé. Les équipes qui écrivent des Skills customs doivent valider le comportement spécifiquement sur chaque agent qu'elles ciblent.

Les Skills Figma bundlés couvrent la majorité des workflows courants — `figma-use`, `figma-generate-design`, `figma-implement-design`, `figma-create-design-system-rules` — et sont disponibles via le MCP server Figma et le répertoire OpenAI curated skills. Pour les conventions non standards (mode sombre spécifique, taxonomie de tokens atypique, étapes CI propres), écrire un Skill custom est le mécanisme pour encoder ce savoir de façon persistante. Mais l'investissement est plus élevé qu'AGENTS.md, et la plupart des équipes n'en ont pas encore besoin.

Le mécanisme concret derrière `figma-create-design-system-rules` : le MCP server scanne la codebase et produit un fichier de règles structuré (définitions de tokens, bibliothèques de composants, hiérarchies de style, conventions de nommage), qui devient ensuite la Rule always-on consultée par l'agent ([figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md)). C'est une instance concrète de la couche Rules décrite plus haut, générée automatiquement plutôt qu'écrite à la main.

[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md) reformule `figma-use` et les skills Figma custom comme de la **gouvernance-as-code** : une règle du type "utilise toujours le composant NavBar de la librairie core, ne crée jamais d'élément de navigation custom" n'est plus une consigne lue par un designer, c'est une instruction chargée dans le contexte de l'agent au moment de l'exécution. La gouvernance devient structurelle plutôt que déclarative — l'enforcement n'est plus une question de lecture humaine mais de chargement systématique. Voir [ecriture-agents-canvas-design](ecriture-agents-canvas-design.md) pour le changement de régime plus large (agents qui écrivent dans le canvas Figma) dans lequel s'inscrivent ces Skills.

Note sécurité : les fichiers SKILL.md et les payloads MCP sont des instructions exécutables pour les agents — tout acteur pouvant les éditer peut influencer le comportement agent. Voir [prompt-injection-design-system](prompt-injection-design-system.md).

## Convergence avec le "plugin" de Wolosin

[diana-wolosin](../entities/diana-wolosin.md) arrive à la même architecture depuis un angle différent ([machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)). Après avoir observé que le MCP seul produit des violations de fondations (typographie, espacement, couleurs jamais appelés dans les prompts), elle nomme la solution "plugin" : une architecture en couches combinant Rules (always-on, portent les fondations), MCP (on-demand, porte la connaissance composant), et AGENTS.md.

Sa terminologie diffère légèrement : elle utilise "Rules" pour les fondations always-on et "AGENTS.md" là où Morales Achiardi utilise "CLAUDE.md". Mais la structure est identique : un routeur stratégique (CLAUDE.md / AGENTS.md) + des contraintes passives de contexte (Rules) + des capacités on-demand (Skills / MCP). Le point clé que Wolosin rend explicite : les Rules ne sont pas une option d'optimisation — elles sont nécessaires parce que le MCP ne peut structurellement pas porter les fondations. Voir [mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md).
