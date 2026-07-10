---
type: concept
tags: [format, index, tokens, ia, codebase, optimisation, benchmark]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[towards-agentic-design-system]]"
  - "[[mapping-design-system-for-ai-agents]]"
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
related:
  - "[[knowledge-graph-design-system]]"
  - "[[trois-couches-composants-agents]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[mode-exploration-vs-navigation]]"
  - "[[diana-wolosin]]"
---

## TOON : format d'index token-efficient

TOON est un format de sérialisation utilisé par [[cristian-morales-achiardi]] pour encoder le codebase index d'un design system agentique. Il est conçu pour être lu par des agents IA de manière optimale : compact, structuré, et économe en tokens ([[towards-agentic-design-system]]).

## Avantage documenté

TOON offre 30 à 60 % de tokens en moins que JSON pour les mêmes données dans certains cas. Pour un index de design system (relations de composants, dépendances, cartographie de l'usage), cette compression est significative : elle réduit le coût de chaque requête agent et améliore la vitesse de réponse.

## Ce qu'un index TOON contient

Dans le setup documenté par l'auteur, le répertoire `.ai/relationships/` contient trois fichiers TOON : `component-usage.toon` (où chaque composant est utilisé), `dependencies.toon` (les dépendances entre composants), et `data-flow.toon` (les flux de données). Ces fichiers constituent la couche 1 des [[trois-couches-composants-agents]] dans sa forme concrète.

L'index documente 57 composants, 302 relations mappées, et 53 fichiers de métadonnées dans l'exemple décrit. Avec infrastructure TOON : l'agent répond en 1:52 au lieu de 4:26 et trouve 100 % des composants (57/57) contre 43-44/57 sans index.

## Génération automatique

L'index TOON est produit par un script Python (`CodebaseIndexer`) qui scanne `src/components`, parse les imports, construit le graphe de relations, et génère les fichiers TOON ([[mapping-design-system-for-ai-agents]]). Le script détecte automatiquement le framework (React, Vue, Svelte, Astro, Angular via leurs extensions et patterns d'import). Il produit : `component-usage.toon` (inventaire et usages), `data-flow.toon` (flux de données). Il est relancé après chaque ajout ou suppression de composant et versionné avec le code. Les protocols de requête (CLAUDE.md) dictent ensuite comment l'agent doit lire cet index : charger une fois, raisonner sur le cache, ne jamais re-lire dans la même session.

## Coût de chargement et ROI

Un index complet de 55 composants et 302 relations coûte ~4 000 tokens à charger ([[mapping-design-system-for-ai-agents]]). Ce coût est fixe par session. Sans index, l'agent dépense des tokens à chaque question pour explorer — et produit des résultats à 26,5 % de variance. Le seuil de rentabilité est rapide : dès qu'une session comporte plusieurs questions sur la structure du système, l'index est moins cher que l'exploration.

## Position dans l'architecture

TOON est un détail d'implémentation de la couche index ([[knowledge-graph-design-system]]). L'essentiel n'est pas le format lui-même mais la logique qu'il représente : traiter le design system comme une structure de données requêtable plutôt que comme du texte à interpréter. D'autres formats (JSON, YAML, formats propriétaires) peuvent remplir la même fonction — TOON est simplement optimisé pour le coût en tokens des LLMs. Il fonctionne particulièrement bien quand les données ont une structure consistante (mêmes champs pour chaque composant) ; son avantage disparaît si les structures varient fortement.

## ⚡ Tension avec le benchmark de Wolosin

[[diana-wolosin]] a inclus TOON dans son benchmark de 8 configurations MCP ([[machine-readable-design-systems-designing-for-ai-as-a-user]]). Sur les 5 formats testés (Markdown, plain Markdown, Markdown+JSON hybride, JSON, TOON), JSON a battu TOON en précision et/ou en efficacité tokens dans le contexte d'un MCP RAG. Cela ne contredit pas nécessairement l'avantage de TOON pour l'indexation de codebase décrit par [[cristian-morales-achiardi]] — les deux usages sont différents (index de dépendances vs métadonnées de composants pour RAG). Mais le benchmark de Wolosin suggère que pour un usage MCP avec retrieval vectoriel, JSON est suffisant et potentiellement supérieur. La recommandation de Wolosin : JSON pour le MCP, Markdown pour les instructions. TOON reste documenté comme format d'index de codebase, pas comme format de métadonnées MCP.
