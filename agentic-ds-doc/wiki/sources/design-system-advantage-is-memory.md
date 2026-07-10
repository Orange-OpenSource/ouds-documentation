---
type: source
tags: [design-system, ia, mémoire, contexte, données, agents, économie]
created: 2026-07-08
updated: 2026-07-08
sources: []
related:
  - "[[memoire-design-system]]"
  - "[[design-system-comme-dataset]]"
  - "[[knowledge-graph-design-system]]"
  - "[[mode-exploration-vs-navigation]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[inversion-economique-code-comprehension]]"
  - "[[romina-kavcic]]"
---

## The Design System Advantage Is Memory

**Auteure** : [[romina-kavcic]]
**Publication** : 25 mai 2026
**Source** : https://learn.thedesignsystem.guide/p/the-design-system-advantage-is-memory

## Résumé

Kavcic part d'un constat personnel : en connectant 105 outils MCP à son design system, elle pensait l'avoir rendu AI-ready. Il ne l'était pas, parce que les outils donnaient accès à la surface (tokens, docs, composants, Figma) mais pas aux décisions passées — les raisons pour lesquelles un pattern avait été rejeté, les renommages de tokens et leurs justifications, les deprecations et leurs historiques. Cette mémoire vivait dans des Slack, des ADRs, des commentaires Figma non liés entre eux. L'agent avait l'accès. Il n'avait pas la mémoire.

La thèse centrale : l'avantage concurrentiel d'un design system dans l'ère agentique n'est pas le modèle, ni le nombre d'outils, ni le prompt. C'est la mémoire — et spécifiquement la mémoire rendue *retrievable* avant que l'agent commence à agir.

## Thèses principales

**Le contexte partiel crée de la confiance coûteuse.** Un agent qui ne peut accéder qu'à une partie de la mémoire d'équipe ne répond pas "je ne sais pas" — il répond avec assurance à partir du contexte partiel disponible. Répéter la décision correcte à chaque session coûte des tokens. Corriger une recommendation incorrecte coûte de la confiance.

**La distinction visible/invisible est la distinction stratégique.** Le "visible 10%" (tokens, docs, composants, Figma) est forçable. N'importe qui peut forker un JSON de tokens. Le "invisible 90%" (décisions, rejections, critiques, historique de dépréciation, raisons des renommages, ADRs, drift reports) ne peut pas être forké parce qu'il n'est pas dans un fichier structuré — il est dans la mémoire collective de l'équipe. C'est ce deuxième colonne qui constitue le fossé.

**L'architecture a un ordre obligatoire : données → structure → agent.** La plupart des équipes commencent par l'agent (un modèle, un MCP) et remontent. Kavcic inverse : construire d'abord le corpus de données de qualité, puis y superposer un index ou un graphe qui permet le raisonnement croisé, puis seulement orchestrer les agents sur cette base. Sauter la couche 1 produit de "l'hallucination plausible". Sauter la couche 2 produit un agent qui *trouve* un fichier mais ne peut pas le connecter à rien.

**Le graphe est supérieur à la pile de fichiers.** Une collection de documents plate ne suffit pas : l'agent peut lire les fichiers individuellement mais ne peut pas raisonner à travers eux. La question "qu'est-ce qui a changé sur Alert cette année et pourquoi ?" requiert de connecter un commentaire Figma, un thread Slack, une PR fermée et un ADR — ce qu'un grep ne peut pas faire. Le graphe encode ces relations : token → composant → décision → outcome → token. L'agent marche le graphe au lieu de fouiller la pile.

**QMD comme premier pas.** [[romina-kavcic]] documente son expérience avec QMD (Tobi Lütke) : un outil local de recherche hybride (BM25 + vecteur + reranking LLM) qui indexe des dossiers localement en quelques minutes. Ce n'est pas un graphe — c'est le test minimal pour savoir si un corpus a du signal avant d'investir dans l'architecture graphe. Elle l'a utilisé sur 1 511 documents répartis en 6 collections (décisions Tidy, specs clients, brouillons Substack, recherche utilisateur, transcriptions de réunions, matériel de conférence). La recherche hybride a surfacé des connexions que ni le keyword search ni le vector search seuls n'auraient trouvées.

**Deux phases, deux réalités.** En phase 0→1 (founding), l'équipe est dans le mode "faire marcher le système" — les données générées sont majoritairement jetables et ne méritent pas d'être indexées. En phase 1→100 (scaling), l'équipe dispose déjà de trois ans de renommages documentés, d'une douzaine de deprecations et leurs raisons, de rapports de drift, de critiques récurrentes — une mémoire institutionnelle considérable. La plupart des équipes 1→100 ont déjà cette mémoire. Elles ne l'ont juste pas rendue retrievable.

## Citations clés

"I had given the agent access. I had not given it memory."

"The advantage is the memory your company has and whether your agent can use it, not the model, the number of tools, or the clever prompt."

"Partial context creates expensive confidence."

"The design system is no longer the deliverable. It is the dataset."

"Skip layer one, and the agent generates plausible nonsense."

## Données économiques citées

Microsoft a commencé à annuler les licences Claude Code dans son groupe Experiences + Devices (The Verge). Le CTO d'Uber : "le budget que je pensais nécessaire est déjà explosé" (The Information). Le VP Applied Deep Learning de Nvidia : "pour mon équipe, le coût du compute dépasse déjà celui des employés" (Axios). Gartner prédit une baisse de 90% du prix des tokens d'ici 2030, mais les systèmes agentiques consomment 5 à 30 fois plus de tokens qu'un chatbot standard. METR estime que la longueur des tâches que les agents peuvent compléter à 50% de fiabilité double tous les 7 mois — ce qui signifie que chaque session nécessite plus de contexte, plus d'appels d'outils, et plus de risques de récupérer la mauvaise mémoire.

## Connexions identifiées

Cette source enrichit directement : [[knowledge-graph-design-system]] (graphe vs pile + QMD), [[mode-exploration-vs-navigation]] (QMD comme solution lightweight), [[gouvernance-design-system-ia]] (coût économique du mauvais contexte), [[inversion-economique-code-comprehension]] (données chiffrées nouvelles). Elle crée deux nouveaux concepts : [[memoire-design-system]] et [[design-system-comme-dataset]].
