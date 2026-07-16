---
type: concept
tags: [design-system, ia, mémoire, décisions, contexte, agents, corpus]
created: 2026-07-08
updated: 2026-07-08
sources:
  - "[design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)"
related:
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[mode-exploration-vs-navigation](mode-exploration-vs-navigation.md)"
  - "[design-system-comme-dataset](design-system-comme-dataset.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[inversion-economique-code-comprehension](inversion-economique-code-comprehension.md)"
  - "[architecture-contexte-agentique](architecture-contexte-agentique.md)"
  - "[seeds-vs-trees](seeds-vs-trees.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
---

## La mémoire comme avantage du design system

L'argument de [romina-kavcic](../entities/romina-kavcic.md) dans "The Design System Advantage Is Memory" ([design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)) est une reformulation du problème de l'IA-readiness qui déplace l'attention des outils vers les données. Connecter 105 outils MCP à un design system n'a pas suffi à le rendre utile pour les agents — parce que les outils donnaient accès à la *surface* (tokens, composants, docs, Figma) mais pas aux *décisions* (pourquoi un pattern a été rejeté, pourquoi un token a été renommé, pourquoi un composant a été déprécié). Cette deuxième couche, la mémoire institutionnelle de l'équipe, est ce que les agents manquent presque universellement.

La formulation condensée : "I had given the agent access. I had not given it memory."

## Le visible 10% et l'invisible 90%

La structure du problème peut se représenter comme deux colonnes. La colonne visible — tokens, documentation, composants, code Figma — est ce que les agents peuvent déjà lire. Elle est *forkable* : n'importe qui peut copier un JSON de tokens. La colonne invisible — décisions, rejections, critiques récurrentes, historiques de dépréciation, renommages et leurs raisons, rapports de drift, ADRs — est ce qui constitue le fossé concurrentiel réel. Elle vit dans des threads Slack, des commentaires Figma, des PRs fermées, des documents internes non liés entre eux. Elle ne peut pas être forkée parce qu'elle n'est pas structurée.

La plupart des équipes ont bâti leur outillage agentique exclusivement sur la colonne visible. C'est pour cette raison que les agents répètent des erreurs connues, proposent des patterns déjà rejetés, et doivent être constamment corrigés sur des décisions que l'équipe a déjà prises.

## Le coût de la mémoire partielle

Un agent qui n'a accès qu'à une partie de la mémoire d'équipe ne répond pas "je ne sais pas" — il répond avec assurance à partir du contexte partiel disponible. Kavcic appelle cela la "confident ignorance" : un contexte partiel crée une confiance coûteuse.

Chaque re-découverte d'une décision déjà prise coûte des tokens. Chaque correction d'une recommendation incorrecte coûte de la confiance. Chaque passage par un pattern rejeté coûte du temps d'équipe. Et ces coûts s'accumulent à chaque session, parce que les agents n'ont pas de mémoire persistante entre les runs. Le coût n'est pas ponctuel — il est structurel.

Les données économiques sont convergentes : Uber a dépassé son budget IA, Nvidia déclare que le compute coûte plus que les salariés, Gartner documente que les systèmes agentiques consomment 5 à 30 fois plus de tokens qu'un chatbot standard (voir [gouvernance-design-system-ia](gouvernance-design-system-ia.md) pour le détail). La baisse du coût unitaire des tokens ne compense pas une consommation qui croît plus vite que les économies.

## La distinction : avoir vs rendre retrievable

La mémoire institutionnelle existe dans la plupart des équipes en phase 1→100 ([design-system-comme-dataset](design-system-comme-dataset.md)) : trois ans de renommages documentés, une douzaine de deprecations et leurs raisons, des critiques récurrentes, des rapports de drift, des ADRs. Le problème n'est pas l'absence de mémoire. C'est que cette mémoire n'est pas *retrievable* avant que l'agent commence à agir.

Un fichier qui existe dans un dossier inaccessible a la même valeur pour un agent qu'un fichier qui n'existe pas. La mémoire utile est celle que l'agent peut interroger, structurée de façon à ce que la question "pourquoi ce token a été renommé ?" puisse trouver une réponse dans le corpus sans que l'humain doive la répéter.

## L'architecture qui rend la mémoire opérationnelle

Rendre la mémoire retrievable exige une architecture en trois couches dans un ordre obligatoire. En bas, les données : tokens, décisions, drift, critiques, ADRs, historique de dépréciation — tout ce qui constitue l'invisible 90%. Au-dessus, la structure : un index hybride (comme QMD) ou un graphe qui permet à l'agent de raisonner *à travers* le corpus et pas seulement de lire des fichiers un par un. En haut, l'agent : la couche la plus petite, essentiellement de l'orchestration sur les deux premières.

Sauter la première couche produit de "l'hallucination plausible". Sauter la deuxième produit un agent qui *trouve* un fichier mais ne peut pas le connecter à rien. Bien exécuter les deux premières rend la troisième presque triviale — et les modèles interchangeables.

## QMD comme test minimal

Avant d'investir dans un graphe complet, [romina-kavcic](../entities/romina-kavcic.md) recommande QMD (Tobi Lütke) comme test minimal de signal. QMD est un outil local de recherche hybride — BM25 (keyword), vecteur, reranking LLM — qui indexe un dossier localement en quelques minutes et s'expose comme outil MCP. Son usage est simple : choisir un dossier avec du signal réel (ADRs, critiques, specs composants), l'indexer, poser cinq vraies questions que l'équipe pose régulièrement, regarder les manques. Un miss signifie soit que le document est absent, soit que le document existe mais que son langage est trop vague pour être retrouvé. QMD ne construit pas un graphe — il teste si un corpus mérite qu'on y investisse la structure d'un graphe.

## Relation avec les autres concepts du vault

Cette formulation de la mémoire comme avantage est complémentaire au [knowledge-graph-design-system](knowledge-graph-design-system.md) : le graphe est l'architecture qui *structure* cette mémoire pour la rendre traversable. Elle confirme et approfondit [mode-exploration-vs-navigation](mode-exploration-vs-navigation.md) : sans mémoire structurée, l'agent explore (coûteux, variable) ; avec mémoire retrievable, il navigue (déterministe, précis). Elle est en tension productive avec l'emphase sur les outils MCP présente dans plusieurs sources du vault : les outils sont nécessaires, mais ils sont la couche supérieure, pas le fondement.

## ⚡ Tension / Contradiction

Plusieurs sources du vault ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md), [mcp-model-context-protocol](mcp-model-context-protocol.md), [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)) placent l'outillage MCP — le nombre d'outils connectés, la richesse des endpoints — comme mesure de maturité d'un design system agentique. Kavcic contredit directement cette lecture : "The advantage is the memory your company has and whether your agent can use it, not the model, the number of tools, or the clever prompt." La maturité se mesure à la qualité du corpus et à sa retrievability, pas à la quantité d'outils exposés. Les deux positions ne sont pas inconciliables — les outils MCP accèdent au corpus — mais la hiérarchie est inversée : les données précèdent et conditionnent l'utilité des outils.
