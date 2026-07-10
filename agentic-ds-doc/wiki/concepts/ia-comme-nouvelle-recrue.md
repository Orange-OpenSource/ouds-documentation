---
type: concept
tags: [ia, design-system, onboarding, métaphore, documentation, miro]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[[miro-ai-design-system-mcp-claude-code-skills]]"
related:
  - "[[ia-comme-utilisateur]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[seeds-vs-trees]]"
  - "[[andressa-lombardo]]"
  - "[[aura-miro]]"
  - "[[documentation-lag]]"
---

## L'IA comme nouvelle recrue

"L'IA comme nouvelle recrue" est la reformulation que [[andressa-lombardo]] et [[eddie-machado]] ont adoptée chez Miro pour définir leur travail ([[miro-ai-design-system-mcp-claude-code-skills]]). Elle se distingue de la thèse "IA comme utilisateur" de [[diana-wolosin]] ([[ia-comme-utilisateur]]) par son angle : non pas le format du système (readable, queryable), mais le processus de préparation du système (onboarding, matériel pédagogique).

## La distinction avec "IA comme utilisateur"

[[diana-wolosin]] pose la question : "comment le design system doit-il être structuré pour qu'une IA puisse le requêter ?" La réponse : métadonnées structurées, JSON, MCP. [[andressa-lombardo]] pose la question : "comment embarque-t-on un nouveau membre d'équipe ?" La réponse : on lui écrit les règles, on lui montre les exemples et les contre-exemples, on lui laisse de la place pour expérimenter et se corriger.

Ces deux questions ont des réponses qui se recoupent — l'onboarding matériel et les métadonnées structurées servent les deux audiences — mais l'angle change ce qu'on priorise. La thèse Wolosin pointe vers l'architecture du MCP. La thèse Lombardo pointe vers la qualité de ce qu'on met dedans : les descriptions "do not use", les exemples et contre-exemples, la cohérence des règles.

## Les trois principes d'onboarding que Miro a appliqués

Andressa et Eddie ont déduit trois principes de ce qu'impliquerait onboarder une nouvelle recrue humaine, puis les ont appliqués à Aura :

**Show, don't tell.** Expliquer et montrer — y compris le "why not". Un humain peut inférer un contre-exemple depuis une règle générale ; une IA littérale a besoin qu'on lui montre explicitement ce qu'il ne faut pas faire et pourquoi.

**Be consistent.** Les règles ne doivent pas être ambiguës. Une IA ne peut pas inférer la règle depuis des exemples contradictoires — elle produit une réponse moyenne ou prend le premier exemple rencontré. La cohérence n'est pas une qualité stylistique, c'est une condition de fiabilité.

**Give room to experiment.** Les meilleures progressions viennent de l'essai, de l'erreur et de l'auto-correction. Aura a besoin du même espace — et l'équipe a besoin de tolérance pour les sorties imparfaites au début.

## Ce que ça change dans le travail concret

La reformulation en "nouvelle recrue" a une conséquence directe sur la hiérarchie des priorités. Andressa et Eddie ont consacré des mois à auditer la documentation, écrire des descriptions d'icônes, ajouter des best practices de composants, remplir les métadonnées manquantes. Travail non-glamour, invisible en démo, pas ce qui "fait briller les yeux du senior leadership." Mais c'est exactement ce qu'on prépare pour un nouveau venu : le contexte dont il a besoin pour ne pas inventer ce qu'il ne sait pas.

La formule de gestion interne qui en découle : "Prove the concept first. Explain it second." Montrer que ça fonctionne (Aura qui génère des sorties correctes avec les bonnes icônes, le canal Slack qui se tait) avant de défendre le pourquoi du travail ingrat.

## Tension avec "IA comme utilisateur"

Les deux reformulations sont complémentaires mais ne disent pas exactement la même chose. "IA comme utilisateur" (Wolosin) implique de traiter l'IA comme une deuxième audience permanente du design system — une décision d'infrastructure, durable et structurelle. "IA comme nouvelle recrue" (Lombardo) implique de traiter l'IA comme un être avec une courbe d'apprentissage — une décision pédagogique et processuelle. Le premier cadre produit des schémas JSON et des MCP servers. Le second produit des descriptions "do not use", des contre-exemples explicites et une personnalité nommée.

Un design system peut répondre aux deux : avoir la bonne architecture (MCP, JSON) et le bon contenu (descriptions complètes, règles cohérentes). La distinction est utile pour diagnostiquer les lacunes : si les sorties de l'IA sont imprécises malgré un MCP fonctionnel, ce n'est peut-être pas une lacune d'architecture mais une lacune d'onboarding.
