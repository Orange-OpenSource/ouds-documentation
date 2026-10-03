---
type: concept
tags: [design-system, agentique, architecture, contexte, jugement, composition, couches, mcp]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[design-systems-for-ai-agents-paradigm-shift](../sources/design-systems-for-ai-agents-paradigm-shift.md)"
  - "[ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md)"
related:
  - "[ia-comme-utilisateur](ia-comme-utilisateur.md)"
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[vicente-g](../entities/vicente-g.md)"
---

## Le design system comme architecture de contexte

L'architecture de contexte est une reformulation du design system proposée par [vicente-g](../entities/vicente-g.md) qui déplace l'accent de la livraison de composants vers la livraison organisée de contexte pour les agents IA ([design-systems-for-ai-agents-paradigm-shift](../sources/design-systems-for-ai-agents-paradigm-shift.md)). Le design system "cesse d'être seulement une bibliothèque de composants et un hub de documentation, et devient une architecture de contexte."

Ce déplacement répond à une limite structurelle : un agent IA ne comble pas les lacunes de contexte comme un designer senior — il improvise. "When an agent cannot find a rule, it invents one." Si la hiérarchie typographique n'est pas dans le contexte, il improvise. Si la grammaire d'espacement est absente, il distribue les éléments génériquement. Si les règles d'icônes ne sont pas encodées, il utilise des emojis.

## Exposer le jugement, pas seulement les composants

La thèse centrale : "A Design System cannot limit itself to exposing components. It has to expose judgment." Le jugement désigne la connaissance compositionnelle implicite que les designers expérimentés ont internalisée et que les agents n'ont pas — à moins qu'elle ne soit explicitement structurée.

Ce jugement se décompose en quatre dimensions : le *quoi* (quel composant), le *comment* (quel comportement dans ce contexte), le *quand* (dans quelle situation préférer ce composant à un autre), et le *pourquoi* (quelle intention visuelle et fonctionnelle est servie). Un design system qui ne couvre que le *quoi* est une bibliothèque de composants. Un design system qui couvre les quatre dimensions est une architecture de contexte.

## L'UX vit dans les relations, pas dans les composants

Une conséquence directe : "UX Design does not live only inside components. It lives in the relationships between them." Un agent peut sélectionner les bons composants et produire une interface fausse — pas d'un point de vue de l'existence (le bon bouton, la bonne card, les bons tokens) mais d'un point de vue de la composition (rythme absent, hiérarchie incorrecte, densité inadaptée, espacement générique, intention visuelle manquante).

Ceci affine la [couche 3 (Raisonnement)](trois-couches-composants-agents.md) de Kavcic : la logique de sélection de composants n'est pas suffisante. Il faut également une couche de règles de composition — les relations entre composants, les contraintes d'assemblage, les patterns approuvés, les anti-patterns. Ce n'est pas la même chose que de savoir *quel* composant utiliser ; c'est savoir *comment les assembler ensemble*.

## Couches progressives de contexte

L'architecture de contexte s'organise en couches qui se chargent progressivement selon la phase de la tâche ([design-systems-for-ai-agents-paradigm-shift](../sources/design-systems-for-ai-agents-paradigm-shift.md)) :

**Phase 1 — Fondations** : typo, espacement, couleur, iconographie. Doivent être présentes *avant* la génération d'UI. Ce sont les always-on au sens de [mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md). Si elles ne sont pas là au départ, tout ce qui est généré ensuite est potentiellement incohérent.

**Phase 2 — Règles composants** : apparaissent à la demande, quand un composant est sollicité. C'est le domaine naturel du MCP on-demand — les métadonnées de [schema-metadata-composant](schema-metadata-composant.md), les variantes, les props, les anti-patterns.

**Phase 3 — Composition et qualité** : s'activent quand l'agent assemble des layouts ou raffine les sorties. Règles de relation entre composants, standards de qualité vérifiables, exemples bons et mauvais, recettes de patterns.

Cette structure progressive répond au problème des fondations cassées documenté par [diana-wolosin](../entities/diana-wolosin.md) (les 4 300 prototypes Indeed avec typographie inventée) : si les fondations ne sont pas dans le contexte dès la Phase 1, elles ne seront jamais demandées par l'agent.

## Le MCP comme orchestrateur des couches

[vicente-g](../entities/vicente-g.md) attribue au MCP un rôle légèrement étendu par rapport à [diana-wolosin](../entities/diana-wolosin.md) : non pas seulement un retriever on-demand, mais un orchestrateur qui connecte les différentes couches de contexte. "The MCP becomes the orchestrator that connects all those layers together, allowing the AI not only to retrieve information, but also to reason within the logic, standards, and intent of the Design System itself."

L'architecture complète proposée : **MCP + Documentation structurée + Règles contextuelles + Vrais exemples + Couche qualité**. Cette formulation est cohérente avec le "plugin" de [diana-wolosin](../entities/diana-wolosin.md) (Rules + MCP + AGENTS.md) mais l'explicite davantage en introduisant les examples et la couche qualité comme couches distinctes.

## Nouvelles responsabilités des équipes DS

L'article formalise un ensemble de responsabilités nouvelles pour les équipes, dont plusieurs ne figuraient pas dans le corpus du vault (voir [ia-comme-utilisateur](ia-comme-utilisateur.md)) :

Auditer si l'IA interprète le système correctement — ce que [diana-wolosin](../entities/diana-wolosin.md) appelle mesurer les hallucinations comme métrique ([gouvernance-design-system-ia](gouvernance-design-system-ia.md)). Créer des bons ET mauvais exemples intentionnellement — les contre-exemples comme outil d'enseignement pour l'agent. Exposer les patterns comme des recettes réutilisables. Définir des standards de qualité vérifiables. Concevoir le système comme une knowledge API.

## Context architecture vs context volume (Bondar, 2026)

[ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md) formule la même thèse de façon encore plus tranchante : "AI readiness depends on context architecture, not context volume. More documentation does not automatically produce better AI output. Better retrieval produces better AI output." Cette formulation déplace le critère de qualité de l'exhaustivité (combien de documentation) vers la pertinence contextuelle (quelle documentation, au bon moment, pour la bonne tâche).

L'exemple concret donné : pour une page de settings de facturation, l'agent a besoin du pattern settings, des règles produit billing, des composants pertinents, des tokens sémantiques, de la guidance de contenu, et d'une implémentation de référence — pas de la spécification complète de navigation mobile ni de la librairie d'illustrations. La livraison de l'ensemble du système dans chaque prompt est "expensive, noisy, and counterproductive."

Ceci affine le MCP comme orchestrateur des couches (section précédente) en précisant le critère d'orchestration : non pas "tout livrer" mais "livrer le plus petit ensemble utile à la tâche courante." La Layer 8 de Bondar ([ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md)) — accès et livraison de contexte — peut impliquer des MCP servers, des fichiers de repo, des APIs, des manifestes de composants, des systèmes de retrieval, des Skills, des fichiers d'instructions, des intégrations outillées. La forme importe moins que la précision de la sélection.

## Relation avec concevoir-les-conditions

[concevoir-les-conditions](concevoir-les-conditions.md) de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) décrit le déplacement du rôle du designer (concevoir les interfaces → concevoir les conditions sous lesquelles elles se construisent correctement). L'architecture de contexte de [vicente-g](../entities/vicente-g.md) en est la version centrée sur l'artefact plutôt que sur le rôle : ce n'est pas seulement le designer qui change de niveau d'abstraction — c'est le design system lui-même qui change de nature, passant de bibliothèque à infrastructure de jugement.
