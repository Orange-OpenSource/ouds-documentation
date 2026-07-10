---
type: source
tags: [design-system, ia, agents-md, skill-md, design-md, format, standard, gouvernance, storybook, prompt-injection]
created: 2026-07-07
updated: 2026-07-07
sources: []
related:
  - "[[agents-md-format]]"
  - "[[design-md-format]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[dispersion-decision-design]]"
  - "[[prompt-injection-design-system]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[murphy-trueman]]"
  - "[[diana-wolosin]]"
---

## Your design system is fragmenting into agent files

**Auteur** : [[murphy-trueman]] — Design Systems Collective, 14 mai 2026.
**URL** : https://www.designsystemscollective.com/your-design-system-is-fragmenting-into-agent-files-26a9b19a2fad

## Thèse principale

Trois formats — AGENTS.md, SKILL.md, DESIGN.md — ont émergé en douze mois comme conventions de facto pour exposer un design system aux agents IA. Ils ne sont pas en concurrence : ils adressent des couches distinctes. La plupart des praticiens ne comprennent pas où chacun s'insère, ce qui produit des décisions d'adoption mal calibrées.

## Résumé structuré

### Les trois formats et leurs rôles

**AGENTS.md** est la couche d'orchestration. Il vit à la racine du dépôt et dit aux coding agents comment opérer dans le projet : commandes de build et de test, conventions de nommage, règles de lint, limites de modification. Il n'est pas de la documentation *sur* le design system — c'est le routeur qui indique à l'agent *où aller* (quel fichier de tokens, quelle librairie de composants, quel MCP consulter). Soutenu par Codex, Cursor, Windsurf, GitHub Copilot. Claude Code utilise CLAUDE.md (formats interchangeables en pratique). Précédence inconsistante entre agents (Codex : fichier le plus proche gagne ; Cursor : merge). Meilleure pratique communautaire : < 150 lignes.

**SKILL.md** est la couche procédurale. Un Skill est un répertoire avec un SKILL.md à la racine, plus des scripts ou templates. Le fichier est une recette, pas une description : il dit à l'agent *comment faire* quelque chose, étape par étape. Figma's MCP server livre plusieurs Skills bundlés : `figma-use`, `figma-generate-design`, `figma-implement-design`, `figma-create-design-system-rules`. La portabilité du fichier est réelle (readable everywhere) mais l'exécution n'est pas consistante (different agents load Skills differently, invoke them with different triggers).

**DESIGN.md** est la couche d'identité visuelle compressée. Format open source Google Labs (alpha, 21 avril 2026). YAML front matter pour les valeurs de tokens, corps Markdown pour les règles d'usage en prose. Sa limite structurelle (déjà documentée depuis [[atlassian-design-md-lessons]]) : c'est une spec for reimplementing, pas un guide for using. Optimal pour les environnements sans codebase existante ; insuffisant quand une bibliothèque de composants est en production.

### La plomberie sous-jacente

Storybook 10.3 livre un addon MCP qui expose le contenu Storybook via un Storybook Component Manifest — un fichier JSON listant composants, props, stories, et documentation dans un format token-efficient. Chromatic héberge ces manifests. Zeroheight a son propre MCP server exposant la doc design system aux agents. Diana Wolosin (Indeed) publie sur la construction de MCP servers customs depuis MDX, avec parsers auto-sync.

Le pattern commun : prendre du contenu existant en format humain (Storybook stories, Zeroheight pages, MDX) et en exposer un sous-ensemble structuré et machine-readable aux agents via MCP. Les trois formats Markdown couvrent les angles que les MCP servers n'adressent pas.

### La dispersion d'une décision de design

Une décision unique (ex : la couleur primaire) se propage désormais dans cinq emplacements distincts : le fichier JSON tokens (DTCG), DESIGN.md (hardcodé dans le YAML frontmatter), AGENTS.md (référence indirecte via règle "use tokens from @acme/tokens"), un Figma Skill (procédure de lookup sans stocker la valeur), le Storybook Component Manifest (généré depuis les stories). Aucun lien automatique entre DESIGN.md et le fichier JSON source. "Derivable in principle from the tokens file but rarely derived in practice unless someone has built the pipeline." La question est de gouvernance, pas de technologie.

### La gouvernance des coutures

La design system team de 2025 maintient désormais : JSON tokens file, component manifest (généré depuis Storybook), AGENTS.md, DESIGN.md, SKILL.md files, endpoint MCP Zeroheight. Aucun de ces artefacts n'existait il y a dix-huit mois. Aucun modèle de gouvernance existant n'a été conçu pour eux. Et personne dans l'org chart n'a pour rôle de maintenir les coutures entre ces couches. Qui possède AGENTS.md (engineering), SKILL.md (design tooling/platform engineering), DESIGN.md (souvent : celui qui l'a écrit en premier), la génération du manifest Storybook (automatique).

### La sécurité comme angle ignoré

AGENTS.md, SKILL.md, et les component manifests sont des *instructions exécutables* pour les agents. Quiconque peut éditer ces fichiers peut influencer le comportement des agents. "Instructions delivered through MCP payloads increasingly need the same review discipline teams already apply to code and CI configuration." Prompt injection n'est pas théorique quand la documentation du design system est une entrée exécutable.

### L'empirisme de Wolosin confirmé

Trueman cite le benchmark de [[diana-wolosin]] chez Indeed : 77 composants extraits de MDX, 1 056 prompts, 8 configurations de métadonnées. Markdown : ~30 000 tokens, couverture 82%, hallucinations visibles. JSON : précision plus haute, 80% moins de tokens, coût annuel 5× inférieur. Règle opérationnelle : "JSON for MCP, Markdown for LLM." Données structurées (APIs, props, variants) en JSON. Guidance en prose pour le modèle en Markdown. DESIGN.md (YAML+Markdown) correspond à cette bipartition.

### Séquence d'adoption recommandée

1. Écrire un AGENTS.md en premier (quelques heures, ROI immédiat sur toutes les interactions agent avec le codebase).
2. Installer le Storybook MCP addon (manifest généré automatiquement, connaissance composant structurée sans double saisie).
3. Écrire un DESIGN.md si l'équipe utilise des outils IA de design génératif (Stitch, Lovable, v0).
4. Ne pas écrire de Skills customs avant d'identifier un workflow répétitif qui le justifie.

## Citations clés

"AGENTS.md is not, in itself, documentation about your design system. It's the orchestration layer." ([[murphy-trueman]])

"Long files slow the agent and bury signal." (Factory docs, cité par Trueman)

"A Skill is best understood as a recipe rather than a description of your design system." ([[murphy-trueman]])

"The question for your team is whether you're shaping the formats that touch your system or accepting whatever the next release decides." ([[murphy-trueman]])

## Connexions identifiées

La thèse "JSON for MCP, Markdown for LLM" de Wolosin valide rétrospectivement l'architecture YAML+Markdown de DESIGN.md. La séquence d'adoption recommandée par Trueman (AGENTS.md d'abord) converge avec la conclusion opérationnelle de [[mcp-on-demand-vs-rules-always-on]] (les Rules/AGENTS.md sont la couche nécessaire que le MCP ne peut pas couvrir). Le risque de prompt injection est un angle absent de [[gouvernance-design-system-ia]] avant cette source. La dispersion d'une décision en 5 emplacements est un nouveau concept qui n'existait pas dans le corpus.
