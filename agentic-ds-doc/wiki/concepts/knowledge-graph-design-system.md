---
type: concept
tags: [design-system, knowledge-graph, ia, agents, relations, contexte]
created: 2026-06-17
updated: 2026-07-08
sources:
  - "[[design-system-most-important-asset-ai-era]]"
  - "[[towards-agentic-design-system]]"
  - "[[mapping-design-system-for-ai-agents]]"
  - "[[agent-orchestration-for-design-systems]]"
  - "[[design-system-advantage-is-memory]]"
related:
  - "[[systeme-de-design-agentique]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[trois-couches-composants-agents]]"
  - "[[composants-context-aware]]"
  - "[[mcp-model-context-protocol]]"
  - "[[format-toon]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[mode-exploration-vs-navigation]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[memoire-design-system]]"
  - "[[design-system-comme-dataset]]"
---

## Knowledge graph du design system

Le knowledge graph d'un design system est une représentation structurée des relations entre les composants, les tokens, les patterns, les pages produit et les règles d'usage. C'est la matière première que les agents IA interrogent pour prendre des décisions contextuelles.

Contrairement à une documentation statique ou à un Storybook, le knowledge graph est relationnel : il ne dit pas seulement "ce composant existe" mais "ce composant est utilisé dans ces 34 pages, qui appartiennent à ces 6 produits, avec ces tokens, dans ces contextes". C'est cette dimension relationnelle qui permet la [[composants-context-aware|documentation context-aware]] et la priorisation par criticité business.

## Ce que le knowledge graph rend possible

Avec un knowledge graph, un agent peut déterminer automatiquement qu'un composant sur la homepage et le checkout est plus critique qu'un composant uniquement dans l'admin ([[design-system-most-important-asset-ai-era]]). Il peut générer des exemples do/dont contextualisés sans qu'on lui demande explicitement. Il peut détecter quels composants sont affectés par un changement de token. Il peut construire la couche de raisonnement ([[trois-couches-composants-agents]]) à partir des patterns observés plutôt qu'écrits manuellement.

## Le knowledge graph comme condition du self-healing

Dans la série "Agentic Design Systems" de [[romina-kavcic]], le knowledge graph est annoncé comme l'un des éléments centraux de la partie 3, "The Self-Healing Design System". L'idée : un système capable de détecter ses propres incohérences et de les corriger en boucle fermée ne peut fonctionner que si l'agent a une carte complète des dépendances. Le knowledge graph est cette carte. Sans elle, l'agent détecte les symptômes mais ne peut pas tracer leur origine ni évaluer l'impact d'un correctif.

## Construction via MCP

La connexion [[mcp-model-context-protocol]] à Figma, GitHub, Storybook, et les outils analytics (PostHog par exemple) est ce qui permet de construire et de maintenir ce graph à jour. Le graph n'est pas statique — il évolue avec le produit.

## Implémentation concrète : le codebase index de Morales Achiardi

[[cristian-morales-achiardi]] donne une implémentation du knowledge graph sous forme d'un codebase index en [[format-toon]], stocké dans `.ai/` ([[towards-agentic-design-system]]). Le répertoire `.ai/relationships/` contient trois fichiers : `component-usage.toon` (où chaque composant est instancié), `dependencies.toon` (les dépendances inter-composants), `data-flow.toon` (les flux de données). Complété par un fichier `index.toon` de synthèse. Exemple de scale documenté : 55 composants, 302 relations, ~4 000 tokens pour le chargement complet, auto-généré par un script Python. Ce graph est ce qui permet les rapports d'audit à $0,20 et la détection de dettes techniques invisibles à l'œil nu — voir [[gouvernance-design-system-ia]].

## Algorithme de deep tracing

L'algorithme complet de deep tracing, tel que formalisé dans les rules de [[cristian-morales-achiardi]] ([[agent-orchestration-for-design-systems]]), est un parcours récursif avec détection de cycles : (1) partir des imports directs de la page cible, (2) pour chaque import, consulter son champ `uses` dans le graphe, (3) si `uses` n'est pas vide, récurser sur ces composants, (4) continuer jusqu'aux composants avec `uses[0]` (pas de dépendances — nœuds terminaux), (5) filtrer par catégorie pour trouver les atomes. La règle encode explicitement l'erreur à éviter : "s'arrêter au premier niveau" manque les composants profondément imbriqués. Les usages de deep tracing : construire une UI depuis un user flow (mapper "copy to clipboard" → CopyButton → savoir que Tooltip est déjà inclus), analyser l'impact d'une dépréciation (supprimer Tooltip casse trois niveaux de composition), produire des rapports d'adoption sans faux négatifs.

## Deep tracing et chaînes de dépendances

L'un des apports essentiels du graph est la capacité de traçage en profondeur ([[mapping-design-system-for-ai-agents]]). Un composant comme Tooltip peut être absent de toutes les pages directement, mais présent à 3 niveaux de profondeur dans une chaîne : Tooltip → CopyButton → CodeBlock → SkillCard → pages. Sans le graph, un agent grep qui cherche `<Tooltip>` dans les pages ne trouve rien et le signale comme "inutilisé" — une recommandation de suppression qui casserait la fonctionnalité copy-to-clipboard du site. Avec le graph, la chaîne est explicite. Les protocols de requête prévoient la règle : "les composants avec `uses[0]` sont des nœuds terminaux (atomes) — même s'ils n'apparaissent pas dans les pages, tracer leurs `usedBy` pour confirmer l'usage."

## Import count vs instance count

Le graph trace les *imports* (combien de fichiers référencent un composant) mais l'adoption réelle se mesure en *instances* (combien de fois un composant est effectivement rendu). La distinction est concrète : Icon.astro est importé dans plusieurs fichiers mais instancié 126 fois. Un composant importé une fois dans une liste peut être rendu 50 fois selon la taille des données. Le vrai indicateur d'adoption est le nombre d'instances, qui requiert le parsing des templates (compter les balises `<Button>`) et non des imports. Cette distinction est critique pour les métriques de gouvernance ([[gouvernance-design-system-ia]]).

## Graphe vs pile de fichiers (Kavcic)

[[romina-kavcic]] apporte une critique directe de l'approche "dump everything into a folder, point Claude at it, hope" ([[design-system-advantage-is-memory]]). Une collection plate de documents laisse l'agent capable de lire des fichiers individuels, mais incapable de raisonner à travers eux. La question "qu'est-ce qui a changé sur Alert cette année et pourquoi ?" requiert de connecter un commentaire Figma, un thread Slack, une PR fermée et un ADR — qu'aucun grep ou recherche vectorielle seul ne peut relier. Le graphe encode ces relations explicitement : token → composant → décision → outcome → token. L'agent marche le graphe au lieu de fouiller la pile.

Dans cette perspective, les noeuds d'un graphe de design system sont plus larges que des fichiers : token, composant, pattern, décision, owner, surface, marque. Les arêtes sont : uses, supersedes, depends_on, was_decided_by, drifted_from. C'est cette carte relationnelle que Kavcic a reconstruite dans Tidy — chaque composant connaît ses variants, ses tokens, son owner, son historique de décisions, son drift score.

**QMD comme étape intermédiaire.** Avant de construire le graphe complet, [[romina-kavcic]] recommande QMD (Tobi Lütke) : un outil local de recherche hybride (BM25 + vecteur + reranking LLM) qui indexe un corpus localement en quelques minutes et s'expose comme outil MCP. Ce n'est pas un graphe — c'est un test de signal. Si QMD ne peut pas répondre aux vraies questions de l'équipe sur son corpus, le problème est soit que les documents manquent, soit que leur langage est trop vague pour être retrouvé. Un miss sur QMD est un signal d'investissement : écrire le document manquant, ou clarifier le langage du document existant. Ce n'est qu'après avoir validé le signal du corpus qu'il vaut la peine d'investir dans l'architecture graphe.

## La distinction quoi / où / devrait-on

[[cristian-morales-achiardi]] formule la complémentarité entre métadonnées et index de manière précise ([[mapping-design-system-for-ai-agents]]) : les métadonnées répondent à "comment utiliser Button ?" (consulter `Button.metadata.ts`), l'index répond à "où Button est-il utilisé ?" (consulter `component-usage.toon`), et les deux ensemble permettent de répondre à "devrait-on créer un nouveau composant card ?" (vérifier l'index pour les cards existantes, les métadonnées pour leurs capacités). Aucune des deux couches seule ne suffit pour cette troisième question.
