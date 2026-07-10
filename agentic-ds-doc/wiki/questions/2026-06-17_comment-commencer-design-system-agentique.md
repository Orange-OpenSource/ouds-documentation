---
type: question
tags: [design-system, agentic, ia, strategie, adoption, mcp, getting-started]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-system-most-important-asset-ai-era]]"
  - "[[towards-agentic-design-system]]"
  - "[[design-system-documentation-as-structured-metadata]]"
  - "[[agent-orchestration-for-design-systems]]"
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[design-systems-mcp-complete-guide]]"
  - "[[encoding-governance-agentic-design-systems]]"
related:
  - "[[seeds-vs-trees]]"
  - "[[protocole-arc]]"
  - "[[trois-couches-composants-agents]]"
  - "[[ia-comme-utilisateur]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[code-source-de-verite-mcp]]"
  - "[[concevoir-les-conditions]]"
  - "[[deux-lectures-du-design-system-ia]]"
  - "[[schema-metadata-composant]]"
  - "[[processus-generation-metadata-echelle]]"
  - "[[pipeline-figma-docs-automatise]]"
---

## Question : Comment commencer à faire évoluer mon design system vers l'agentique ?

La première chose à comprendre est que la question "comment commencer" contient un piège. Le corpus du vault y répond unanimement : on ne commence pas par l'automatisation. [[romina-kavcic]] l'exprime sous la métaphore [[seeds-vs-trees]] — "without structure, AI amplifies noise at scale. With structure, it amplifies understanding." L'erreur la plus commune est de vouloir l'arbre (un agent autonome qui compose des interfaces) avant d'avoir planté les graines (une structure lisible par la machine). L'ordre n'est pas arbitraire : un agent sans fondations prend de mauvaises décisions à grande vitesse et à grande échelle.

## Étape 0 — Reformuler le problème

Avant de toucher quoi que ce soit dans le design system, le changement de perspective que [[diana-wolosin]] nomme [[ia-comme-utilisateur]] est nécessaire. Le design system ne doit pas être *documenté davantage* pour l'IA — il doit être *reformaté* pour elle. Un agent ne lit pas la documentation comme un designer junior : il envoie une requête, récupère ce qu'il a demandé, et comble le reste avec ses propres hypothèses. Si la documentation n'est pas structurée pour être *requêtée*, elle est invisible. Ce n'est pas un problème de quantité de contenu — c'est un problème de format.

Il est aussi utile de clarifier quelle lecture de "design system et IA" correspond à votre contexte (voir [[deux-lectures-du-design-system-ia]]) : est-ce que vous cherchez à faire opérer le design system par des agents IA (la Lecture A, sujet de la quasi-totalité du corpus), ou à documenter des fonctionnalités IA pour vos utilisateurs humains (la Lecture B, objet de [[modele-maturite-ia-design-system]]) ? Les deux demandent des investissements différents.

## Étape 1 — Commencer sans infrastructure : les workflows immédiats

Un point d'entrée à friction quasi-nulle existe sans MCP ni infrastructure vectorielle : créer un Project dans ChatGPT ou Claude, y uploader un fichier Markdown listant composants et propriétés, et utiliser l'agent pour des tâches concrètes — résumé de composant, benchmarking externe, premier jet de documentation, audit QA via export JSON Figma. Ce point d'entrée force à résoudre la question première : qu'est-ce que l'agent a besoin de savoir ? Les gaps que vous identifierez dans ces premiers échanges définissent exactement ce qui doit être encodé dans la couche suivante.

## Étape 2 — Construire les trois couches dans l'ordre

Le [[protocole-arc]] structure la progression en trois phases. La Phase 1 (Audit) ne demande qu'une seule chose : que le design system soit *auditable*. C'est la **couche 1** des [[trois-couches-composants-agents]] : un index de ce qui existe, des dépendances, des relations. [[cristian-morales-achiardi]] l'implémente en `format-toon` dans `.ai/`. [[romina-kavcic]] le formule simplement : "just document your naming conventions, then your 5 to 10 components."

La **couche 2** (métadonnées) documente l'intent de chaque composant — cas d'usage, anti-patterns, variants et leur raison d'être, critères de sélection explicites. Le [[schema-metadata-composant]] à 9 sections et le [[processus-generation-metadata-echelle]] en 5 étapes documentent comment y arriver en s'appuyant sur l'IA pour l'extraction depuis la documentation existante.

La **couche 3** (logique de composition) arrive en dernier : les règles de sélection, les patterns d'assemblage, les playbooks par situation. C'est ce qui permet à l'agent de ne pas juste identifier des composants, mais de les composer correctement.

## Étape 3 — Choisir son modèle d'implémentation MCP

Quand l'index et les métadonnées sont en place, trois modèles d'implémentation MCP sont documentés dans le vault, chacun adapté à une topologie d'équipe :

**Documentation-led** (MDX comme source de vérité) → approche [[diana-wolosin]]/Indeed : parsers JavaScript par domaine → JSON → base vectorielle → MCP.

**Engineering-led** (le code précède la documentation) → approche [[jesse-gardner]]/New York State : JSDoc sur les composants → custom element manifest → MCP server. Voir [[code-source-de-verite-mcp]].

**Design-led** (Figma comme source de vérité) → approche [[romina-kavcic]] : Figma MCP → Claude Code → MDX ([[pipeline-figma-docs-automatise]]), ou directement via le plugin Tidy.

## Étape 4 — L'architecture toujours-on

Quel que soit le modèle MCP choisi, [[mcp-on-demand-vs-rules-always-on]] est la mise en garde centrale : le MCP ne retourne que ce qu'on lui demande. Les fondations (typographie, espacement, couleurs) doivent être portées par une couche always-on (fichier de Rules injecté à chaque session). [[laura-fehre]] nuance : ces Rules orientent sans bloquer — "the prompt wins in nearly 100% of cases." Pour les violations intolérables, des contraintes exécutables (linters, auditeurs de tokens) sont nécessaires en complément. Voir [[concevoir-les-conditions]] et [[existence-vs-intent-violations]].

## Le déplacement de fond

Le déplacement le plus profond n'est pas technique : faire évoluer un design system vers l'agentique, c'est progressivement cesser de concevoir des interfaces pour commencer à concevoir les règles sous lesquelles elles se construisent correctement ([[concevoir-les-conditions]]). Le défi épistémique du Maintainer ([[user-vs-maintainer-ia]]) : formuler explicitement des règles qui jusqu'ici vivaient comme intuitions d'équipe.
