---
type: concept
tags: [ia, agents, index, determinisme, drift, design-system]
created: 2026-06-17
updated: 2026-07-08
sources:
  - "[mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)"
  - "[design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)"
related:
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[protocole-arc](protocole-arc.md)"
  - "[seeds-vs-trees](seeds-vs-trees.md)"
  - "[memoire-design-system](memoire-design-system.md)"
---

## Mode Exploration vs Mode Navigation

La distinction Exploration / Navigation est le cadre conceptuel central de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) pour expliquer pourquoi le codebase index change fondamentalement le comportement d'un agent IA ([mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)). Elle articule le problème que les métadonnées seules ne peuvent pas résoudre.

## Mode Exploration (sans carte)

En l'absence d'index, un agent doit construire sa compréhension du système à chaque session : `find src/components`, grep pour les imports, lecture de fichiers un par un. Ce mode a quatre caractéristiques défavorables.

La **variance** : sans protocole de lecture consistant, l'agent choisit différemment à chaque run (parfois grep, parfois bash find, parfois lecture manuelle). La variance mesurée est de 26,5 % entre trials — le même agent, la même question, des résultats significativement différents.

Les **faux négatifs** : l'agent déduit l'usage à partir des fichiers qu'il trouve, pas de la structure réelle. Si `<Tooltip>` n'apparaît pas dans les pages (parce qu'il est 3 niveaux de profondeur dans une chaîne CopyButton → CodeBlock → SkillCard), l'agent le signale comme "non utilisé" et recommande sa suppression. Supprimer Tooltip aurait cassé la fonctionnalité copy-to-clipboard sur tout le site.

La **dérive** : même quand l'agent *trouve* un composant, il peut ne pas l'utiliser. Le cas documenté — Claude importe ThoughtCard au début du fichier, puis recrée le même markup en HTML brut juste en dessous, l'import inutilisé. Il savait que le composant *existait*, mais pas qu'il était *approprié dans ce contexte précis*.

La **lenteur** : 4 à 5 minutes par session, contre moins de 2 minutes en mode Navigation.

## Mode Navigation (avec carte)

Avec un index pré-calculé (inventaire, graphe de relations, statistiques), l'agent lit la carte au lieu d'explorer. Le graphe rend les dépendances explicites — Tooltip est dans `usedBy[1]: CopyButton`, CopyButton dans `usedBy[1]: CodeBlock`. Pas besoin de grep récursif. La chaîne est là.

Les protocols de requête (CLAUDE.md) convertissent l'index de données passives en comportement déterministe : charger l'index une fois, raisonner sur le cache, ne jamais re-lire les fichiers de relations dans la même session. Résultat : 0,04 % de variance contre 26,5 %, zéro faux négatif, temps de réponse divisé par 2,5.

## La formulation centrale

"Without a map, AI explores. With a map, AI navigates. The difference is determinism" ([mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)). Le déterminisme est la propriété clé : un système agentique dont le comportement varie fortement d'une session à l'autre ne peut pas être gouverné. Il peut seulement être surveillé.

## QMD : navigation légère avant le graphe

[romina-kavcic](../entities/romina-kavcic.md) propose QMD (Tobi Lütke) comme étape intermédiaire entre le mode Exploration et le mode Navigation complet ([design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)). QMD est un outil local de recherche hybride (BM25 + vecteur + reranking LLM) qui indexe un corpus de fichiers localement et s'expose comme outil MCP. Il ne construit pas un graphe de relations — il construit un index plat mais hybride, plus puissant qu'un grep ou qu'une recherche vectorielle seule. Son usage diagnostique : pointer QMD sur un dossier avec du signal réel (ADRs, critiques, specs), poser les vraies questions de l'équipe, observer les manques. Un miss signifie soit que le document est absent, soit que le langage est trop vague. QMD transforme le mode Exploration en une navigation partielle — suffisante pour valider si le corpus mérite l'investissement dans un graphe complet.

## Relation avec les autres concepts

Le mode Exploration correspond à la situation décrite dans [seeds-vs-trees](seeds-vs-trees.md) — amplification du bruit sans structure. Le mode Navigation est ce que le [knowledge-graph-design-system](knowledge-graph-design-system.md) rend possible. La distinction illustre également pourquoi les [trois-couches-composants-agents](trois-couches-composants-agents.md) sont cumulatives : la couche 2 (métadonnées) résout le *quoi*, mais sans la couche 1 (index), l'agent ne sait toujours pas *où* et ne peut donc pas naviguer. [memoire-design-system](memoire-design-system.md) complète le tableau : le problème n'est pas seulement d'indexer les fichiers existants, mais d'avoir d'abord capturé les décisions qui méritent d'être retrouvées.
