---
type: source
tags: [design-system, agentic, mcp, conference, synthese, indeed, github, new-york-state, spotify, figma]
created: 2026-06-24
updated: 2026-06-24
sources: []
related:
  - "[[romina-kavcic]]"
  - "[[diana-wolosin]]"
  - "[[jesse-gardner]]"
  - "[[jan-six]]"
  - "[[brad-frost]]"
  - "[[into-design-systems-conference]]"
  - "[[systeme-de-design-agentique]]"
  - "[[design-system-as-infrastructure]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[seeds-vs-trees]]"
  - "[[niveaux-confiance-actions-agentiques]]"
---

## Into Design Systems — "Agentic Design Systems: The Complete Guide"

**Auteur** : Into Design Systems (synthèse de 5 speakers, AI Design Systems Conference 2026)
**Speakers** : Romina Kavcic, Diana Wolosin (Indeed), Jesse Gardner (New York State), Jan Six (GitHub), Brad Frost + Ian Frost, TJ Pitre (Southleft)
**Date** : 2026
**URL** : https://www.intodesignsystems.com/agentic-design-systems

## Thèse principale

Guide de synthèse issu de l'AI Design Systems Conference 2026. Document d'agrégation — la plupart des concepts sont documentés individuellement dans d'autres sources déjà ingérées. La valeur de cette source est la mise en constellation des contributions des 5 speakers et les formulations condensées qui en émergent.

## Apport net par rapport aux sources déjà ingérées

Les concepts centraux (MAPE-K, MCP on-demand vs Rules always-on, seeds-vs-trees, AGENTS.md, niveaux de confiance, benchmark JSON vs Markdown) sont déjà bien couverts dans le vault. Les additions nettes sont :

**Nouvelles citations de référence :**
- Jan Six : "The invisible part of your system is way bigger than your visible part. If the agent can't see it, it has to hallucinate." — formulation la plus directe sur le problème de l'invisibilité dans les design systems.
- Diana Wolosin : "JSON is like a contract. It has explicit keys, explicit values, explicit boundaries, and there is no ambiguity." — formule la supériorité du JSON non pas en termes de précision mais de *contractualité* — une métaphore distincte du benchmarking.

**Concept "Context > Probability" formalisé :**
"Without infrastructure, AI collapses toward the average of the internet. Design systems give AI something it cannot get from training data: your encoded decisions." — cette formulation spécifique est plus forte que les versions précédentes du même argument. Elle change l'angle : ce n'est pas que le DS est mieux que rien, c'est que sans DS l'IA *régresse vers la moyenne*.

**Détail Jan Six — sous-agents :**
GitHub Primer utilise des sous-agents spécialisés (ex : un "accessibility reviewer") pour maintenir le contexte principal propre. Workflow : Storybook → preview env → review. Les workflows agentiques tournent en QA quotidien et maintenance, mais avec safe outputs — l'agent peut uniquement créer une issue, jamais merger.

**Stats de contexte (Kavcic, conférence) :**
28 modèles frontier sortis en 9 mois, $200B+ investis en IA dans l'année, croissance MCP de 100K → 8M+ downloads en moins d'un an. Signaux qui justifient l'urgence.

**FigmaLint (Brad Frost / Southleft) :**
Plugin Figma qui score les composants (26/100 → 100/100 après corrections), vérifie l'usage des tokens, le naming de layers, l'accessibilité, les descriptions de composants. Démo Figma Console MCP : "Create a new theme called Lavender" déploie instantanément les nouveaux tokens sur Figma, Storybook et React Native. C'est une implémentation de [[generation-spec-agentique]] en sens inverse : non pas specs → docs, mais thème → déploiement multi-destinations.

## Ce que cette source confirme sans ajouter

Already covered in vault: benchmark Indeed (1,056 prompts, 8 configs, $300 vs $1,500), Tidy (Kavcic, 66 MCP tools), Observatory, Jesse Gardner 13-minute form demo, Spotify Encore layered architecture, AGENTS.md, progressive disclosure of context (Frost), niveaux de confiance (Kavcic).

## Citations clés

- "AI generates code, design systems generate understanding." (Kavcic)
- "The invisible part of your system is way bigger than your visible part. If the agent can't see it, it has to hallucinate." (Jan Six)
- "JSON is like a contract. It has explicit keys, explicit values, explicit boundaries, and there is no ambiguity." (Wolosin)
- "The question isn't whether AI can generate interfaces, it can. The question is what infrastructure makes that output good or trustworthy." (Gardner)
