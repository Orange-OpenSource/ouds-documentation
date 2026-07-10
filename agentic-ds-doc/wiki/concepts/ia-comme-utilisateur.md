---
type: concept
tags: [ia, design-system, machine-readable, utilisateur, documentation, format]
created: 2026-06-17
updated: 2026-06-29
sources:
  - "[[figma-ouds-button-specs]]"
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[design-systems-for-ai-agents-paradigm-shift]]"
  - "[[agent-workflows-design-system-teams]]"
  - "[[miro-ai-design-system-mcp-claude-code-skills]]"
  - "[[figma-library-invisible-ai-agents]]"
  - "[[design-system-documentation-spec]]"
  - "[[wwdc-2026-apple-ai-native-os-levinriegner]]"
related:
  - "[[lisibilite-machine-design-system]]"
  - "[[systeme-de-design-agentique]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[schema-metadata-composant]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[diana-wolosin]]"
  - "[[invisibilite-produit-os-agentique]]"
updated: 2026-06-30
  - "[[architecture-contexte-agentique]]"
  - "[[vicente-g]]"
  - "[[workflows-agent-sans-mcp]]"
  - "[[gerard-pamies]]"
  - "[[ia-comme-nouvelle-recrue]]"
  - "[[andressa-lombardo]]"
---

## L'IA comme utilisateur

"AI is a new user" est la thèse fondatrice de [[diana-wolosin]] ([[machine-readable-design-systems-designing-for-ai-as-a-user]]). Elle reformule le rôle du design system : il n'est plus une infrastructure à destination exclusive des designers et développeurs humains, mais une infrastructure à double audience. Les humains lisent, interprètent, décident. Les IA requêtent, raisonnent programmatiquement, génèrent.

Ces deux audiences n'ont pas les mêmes besoins de format. Un humain lit une page de documentation en prose et reconstruit mentalement les règles implicites. Un LLM reçoit du texte, extrait des patterns, et génère — avec une variabilité proportionnelle à l'ambiguïté du format. La documentation prose, bien que parfaite pour les humains, introduit cette variabilité par construction : elle demande à la machine de reconstruire une structure que le rédacteur avait en tête mais n'a pas rendue explicite.

## Ce que "machine-readable" implique

La formulation de Wolosin : "Codify your design system knowledge into structured data, metadata, schemas, explicit constraints so LLM can parse it, reason about it and use it programmatically." Ce n'est pas une reformulation de la documentation existante — c'est un changement de forme. Les mêmes décisions de design (quand utiliser ce composant, quelles contraintes d'accessibilité, quels anti-patterns) doivent être exprimées dans un format que la machine peut traverser sans interprétation.

La leçon de la première expérience de Wolosin chez Indeed (un Google Spreadsheet converti en snippets JSON) : l'approche "almost worked" — assez pour valider l'hypothèse, pas assez pour un usage en production. Ce "presque" est instructif : il montre que le problème n'est pas la technologie sous-jacente (LLM, MCP, RAG), mais la qualité et la forme du contenu fourni.

## Lien avec l'inversion économique

Cette reformulation de l'utilisateur s'articule directement avec [[inversion-economique-code-comprehension]] : si le code est gratuit et la compréhension est chère, alors la compréhension encodée dans un format machine-readable est l'actif qui détermine la qualité des sorties IA. L'IA-comme-utilisateur accède à cet actif par le MCP — mais uniquement si l'actif est dans le bon format.

## Le système comme knowledge API — et les nouvelles responsabilités qui en découlent

[[vicente-g]] prolonge la thèse "IA comme utilisateur" avec une reformulation du design system comme **knowledge API** ([[design-systems-for-ai-agents-paradigm-shift]]) : un système conçu pour être consommé programmatiquement, pas seulement lu humainement. Ce déplacement introduit des responsabilités d'équipe inédites :

Auditer si l'IA interprète le système correctement — mesurer les interprétations fautives, pas seulement les violations de tokens. Créer des bons ET mauvais exemples intentionnellement — les contre-exemples ont une valeur pédagogique pour l'agent que les documentations humaines n'exploitent pas. Exposer les patterns comme des recettes réutilisables — pas seulement des composants atomiques mais des assemblages nommés et contraints. Définir des standards de qualité vérifiables — des critères que l'agent peut appliquer en auto-évaluation. Ces responsabilités étendent [[gouvernance-design-system-ia]] dans la dimension de l'évaluation de la compréhension plutôt que seulement de la conformité aux règles.

## L'agent comme externaliseur du savoir tribal

[[gerard-pamies]] apporte une angle complémentaire sur ce que l'IA-comme-utilisateur rend possible côté équipe interne ([[agent-workflows-design-system-teams]]) : l'agent alimenté en contexte DS peut se comporter comme le membre le plus expert de l'équipe. "You get consistent answers similar to what you'd get from the most knowledgeable person on the team — without interrupting them." Cette formulation explicite le transfert qui s'opère : le savoir tacite des seniors (les ADRs, les conventions implicites, les décisions historiques) est externalisé dans l'agent. Les équipes contributrices obtiennent des réponses cohérentes avec la gouvernance interne sans saturer les membres seniors.

C'est la même thèse que l'IA-comme-utilisateur, lue du côté de la consommation interne plutôt que de la consommation de génération de code. Le design system, une fois structuré pour la machine, n'est plus seulement un guide pour développeurs — c'est une base de connaissance interrogeable par toute l'équipe, sous forme conversationnelle. Voir [[workflows-agent-sans-mcp]] pour les workflows concrets de cette pratique.

## ⚡ Tension / Variation : l'IA comme nouvelle recrue (Lombardo / Miro)

[[andressa-lombardo]] chez Miro propose une reformulation complémentaire mais distincte : "l'IA comme nouvelle recrue" ([[miro-ai-design-system-mcp-claude-code-skills]]). Là où Wolosin demande "comment le design system doit-il être structuré pour qu'une IA puisse le requêter ?", Lombardo demande "comment embarque-t-on un nouveau membre d'équipe ?" Les réponses se recoupent — métadonnées structurées, règles cohérentes, exemples et contre-exemples — mais l'angle change ce qu'on priorise.

La thèse Wolosin est une décision d'infrastructure : JSON, MCP, schémas. La thèse Lombardo est une décision pédagogique : descriptions "do not use", cohérence des règles, espace pour l'expérimentation et la correction. Un design system peut avoir la bonne architecture et les mauvaises descriptions — les sorties seront quand même inexactes. L'inverse est aussi vrai : des descriptions très riches dans un format peu structuré produisent mieux que des métadonnées vides parfaitement structurées.

Cette tension est utile pour diagnostiquer les problèmes en production : si les sorties IA sont imprécises malgré un MCP fonctionnel, c'est peut-être une lacune d'onboarding (contenu), pas d'architecture (format). Voir [[ia-comme-nouvelle-recrue]] pour le développement complet.

## Convergence avec Morales Achiardi

[[cristian-morales-achiardi]] pose la même prémisse dans un vocabulaire différent : le design system doit être "AI-ready" pour que les agents puissent opérer en mode Maintainer, pas seulement en mode User ([[user-vs-maintainer-ia]]). Wolosin précise la dimension technique de ce "AI-ready" : ce n'est pas une question de documentation complète, mais de format adapté à la consommation programmatique. Les deux auteurs convergent sur le même problème de fond en l'abordant par des angles différents (architecture agentique pour Morales Achiardi, benchmark de format pour Wolosin).

## Le nouveau lecteur dans la pièce : Figma MCP et la rupture d'audience (Nurkhon, 2026)

[[figma-library-invisible-ai-agents]] apporte une reformulation de la thèse "IA comme utilisateur" ancrée dans une expérience vécue et dans un événement daté. Avant le lancement du Figma MCP (24 mars 2026), un design system avait deux lecteurs — designers et développeurs — les deux arrivant avec du contexte, de la mémoire, et la capacité de demander des clarifications. Avec le MCP, un troisième lecteur est entré dans la pièce : un agent qui "doesn't become familiar — it queries." Chaque session commence à zéro, sans accès à l'historique implicite, sans mémoire des conversations qui ont produit les noms.

Ce cadrage enrichit la thèse de Wolosin en précisant l'événement déclencheur. Wolosin écrit pour une audience qui doit anticiper l'IA-comme-utilisateur ; Nurkhon écrit après le fait — Figma MCP est là, les agents lisent déjà les libraries, et la plupart des libraries leur sont illisibles.

Le problème du **contrat implicite** est la contribution conceptuelle centrale. Chaque nom dans un design system encode une histoire : la conversation où v1 a été dépréciée, la raison pour laquelle `input-v2-final` a remplacé `input-v1` (accessibilité, non documentée). La communication humaine compresse ; les agents n'ont pas le décompresseur. Ce n'est pas une métaphore — c'est une description mécanique de pourquoi `nav-item-active-v3` est traité comme une chaîne opaque plutôt que comme un signe.

La conséquence opérationnelle est le bypass pattern : un agent qui ne peut pas parser efficacement une library choisit le chemin plus court — générer depuis zéro — et le résultat est visuellement correct, entièrement déconnecté du système. Spotify Encore est le cas de référence : système de haute qualité, 220 000+ usages de styles partagés, et pourtant les développeurs allaient sur Cursor parce que la library était trop complexe pour qu'un agent la traverse rapidement. L'IA-comme-utilisateur peut contourner le design system aussi facilement qu'elle peut l'utiliser.

## La double audience formalisée dans un standard : agentDocumentBlocks (DSDS, 2026)

## Le champ Keywords OUDS comme signal d'audience explicite

La description Figma du Button OUDS ([[figma-ouds-button-specs]]) contient un champ "Key words" : "button, icon button, close button, action, primary action, secondary action, CTA". Cette liste n'est pas pour les designers — un designer qui cherche un bouton sait déjà ce qu'il cherche, et la barre de recherche Figma lui suffit. Elle est pour les systèmes de recherche et les agents MCP qui doivent résoudre une ambiguïté sémantique : "icon button" et "close button" sont-ils le même composant que "button" ou des composants distincts ? La réponse — ils partagent le même `component_set` dans la bibliothèque OUDS — n'est accessible que si ces termes sont co-localisés dans la description.

C'est une implémentation minimale mais opérationnelle de la thèse de Wolosin : écrire pour une machine qui requête sans contexte. L'équipe OUDS n'a probablement pas formulé sa décision en ces termes, mais le résultat est identique. Le champ Keywords est le seul endroit dans la description où l'audience IA est implicitement mais clairement adressée.

## La double audience formalisée dans un standard : agentDocumentBlocks (DSDS, 2026)

[[pj-onori]] traduit en juin 2026 la thèse "IA comme utilisateur" dans un mécanisme de spec formel ([[design-system-documentation-spec]]) : le champ `agentDocumentBlocks`. Là où Wolosin décrit une intention (documenter pour deux audiences), DSDS fournit l'implémentation — un tableau séparé dans chaque entité, jamais affiché aux humains, contenant uniquement ce que les agents ont besoin de savoir : règles dures, distinguos entre entités similaires, critères de vérification avec preuves.

La règle de construction dans DSDS est une traduction directe du test de Wolosin ("would a person reading the docs need this?") : si oui, c'est `documentBlocks`. Si non et que seul un agent agit dessus, c'est `agentDocumentBlocks`. Ce test binaire remplace la décision d'architecture par une convention partagée dans un format validable. L'agent comme utilisateur n'est plus une métaphore — c'est un champ de la spec. Voir [[dsds-format]] pour la structure complète.


## L'OS comme troisième audience : App Intents et l'invisibilité système (Apple, WWDC 2026)

[[wwdc-2026-apple-ai-native-os-levinriegner]] ajoute une troisième audience au cadre "IA comme utilisateur" — au-delà des agents de code (Figma MCP, Claude Code) et des agents de documentation (Wolosin) : le système d'exploitation lui-même comme orchestrateur d'intent. Avec iOS 27 et App Intents, Apple Intelligence, Siri, et Spotlight constituent une couche qui consulte les capacités exposées des apps avant de décider comment répondre à une demande utilisateur.

Cette audience a une propriété distinctive par rapport aux deux premières : elle est **systémique et permanente**. Un agent de code est invoqué à la demande. L'OS agentique est actif en permanence, prêt à médier toute interaction. Les apps qui ne participent pas à cette couche ne subissent pas un handicap occasionnel — elles sont structurellement absentes d'un layer de plus en plus central à l'expérience utilisateur.

Le concept d'audience se précise ainsi en trois niveaux distincts : (1) agents de génération de code qui lisent les design systems pour produire de l'interface (Wolosin, Nurkhon), (2) agents de documentation et de gouvernance qui maintiennent la cohérence du système (Morales Achiardi), (3) agents d'orchestration OS qui médient l'accès utilisateur aux capacités des apps (Apple Intelligence, Siri). Voir [[invisibilite-produit-os-agentique]] pour le développement du troisième niveau.
