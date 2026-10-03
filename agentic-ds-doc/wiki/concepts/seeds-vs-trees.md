---
type: concept
tags: [ia, adoption, fondations, design-system, strategie]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[self-healing-design-system](../sources/self-healing-design-system.md)"
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
related:
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[design-system-as-infrastructure](design-system-as-infrastructure.md)"
---

## Seeds vs Trees : la posture d'adoption de l'IA

"Seeds vs Trees" est une métaphore de [romina-kavcic](../entities/romina-kavcic.md) pour décrire deux postures opposées face à l'intégration de l'IA dans un design system ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

Les **graines** (seeds) : on plante, on arrose, on attend. La croissance est lente mais réelle et enracinée. On construit les fondations d'abord — les conventions de nommage, la structure des tokens, les descriptions de composants, le knowledge graph — et l'automatisation pousse sur ces fondations.

Les **arbres** (trees) : on achète un arbre adulte et on le plante dans le jardin. Impressionnant le premier jour. Mais les racines ne sont pas là, le sol n'est pas préparé, et l'arbre ne survit pas ou ne s'adapte pas à l'environnement.

## Ce que ça implique

Toutes les équipes veulent l'agent entièrement autonome qui détecte, analyse, planifie et corrige les problèmes. C'est l'arbre. Le problème : sans les fondations structurelles adéquates, l'agent amplifie le bruit plutôt que la compréhension. Si la couche 1 est incomplète, si les tokens n'ont pas d'intent, si les composants n'ont pas de descriptions, l'agent prend de mauvaises décisions à grande vitesse et à grande échelle.

La bonne séquence est : d'abord les graines (structure, nommage, documentation machine-readable), ensuite les arbres (automatisation, agents autonomes, self-healing). Ce n'est pas une question de délai — c'est une question d'ordre. Les fondations peuvent être posées vite (554 descriptions de composants en une session avec l'IA). L'erreur serait de les sauter.

## Validation en production

Après un an de maintien d'une architecture agentique complète, [romina-kavcic](../entities/romina-kavcic.md) formule ce constat opérationnel dans la partie 3 de sa série ([self-healing-design-system](../sources/self-healing-design-system.md)) : "This architecture only works because the foundation is solid. Without clean token naming, without component descriptions, without intent documentation, the agent has nothing meaningful to work with." Ce n'est plus un principe de conception — c'est un résultat empirique. L'architecture Watch/Analyze/Execute/Observe de la [boucle-feedback-infrastructure](boucle-feedback-infrastructure.md) ne tient que parce que les graines ont été plantées d'abord.

## Consensus de conférence

Les cinq conférenciers de l'AI Design Systems Conference 2026 convergent sur ce principe comme point de départ commun : "Plant seeds, not trees" ([your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)). La formulation de consensus : naming conventions, token structure et descriptions de composants en premier — même des métadonnées structurées basiques donnent aux agents des sorties dramatiquement meilleures que l'absence totale de contexte. Ce consensus confirme empiriquement la thèse de Kavcic, formulée initialement comme principe de conception et validée maintenant par cinq équipes différentes en production.

## Formulation centrale

"Without structure, AI amplifies noise at scale. With structure, it amplifies understanding" ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)). Cette phrase est le principe directeur derrière la métaphore.
