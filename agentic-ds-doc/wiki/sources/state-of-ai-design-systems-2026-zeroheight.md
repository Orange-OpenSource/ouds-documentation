---
type: source
tags: [design-system, ia, adoption, statistiques, rapport, mcp, shadow-ai, documentation, outils, equipes, gouvernance]
created: 2026-07-06
updated: 2026-07-06
sources: []
related:
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
  - "[shadow-ia-design-system](../concepts/shadow-ia-design-system.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[documentation-lag](../concepts/documentation-lag.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[design-system-as-infrastructure](../concepts/design-system-as-infrastructure.md)"
  - "[zeroheight-design-systems-report-2026](zeroheight-design-systems-report-2026.md)"
---

## The State of AI in Design Systems 2026 — zeroheight

**URL** : https://zeroheight.com/resources/state-of-ai-design-systems/report/
**Auteur** : zeroheight (rapport annuel dédié à l'IA)
**Date** : mai 2026
**Échantillon** : N=123 praticiens DS, majorité in-house, entreprises 100+ personnes, systèmes centralisés
**Fichier brut** : [2026-07-06_state-of-ai-design-systems-2026-zeroheight](../../raw/2026-07-06_state-of-ai-design-systems-2026-zeroheight.md)

Ce rapport est distinct du [zeroheight-design-systems-report-2026](zeroheight-design-systems-report-2026.md) (mars 2026, rapport général DS). Celui-ci est entièrement centré sur l'IA. Il constitue le benchmarking sectoriel le plus complet disponible sur l'adoption IA dans les design systems à mi-2026.

## Thèses principales

**L'adoption est massive mais les résultats polarisés.** 82 % des équipes utilisent l'IA. La documentation est le cas d'usage gagnant (63 % satisfaits). La génération de design est le cas d'usage perdant (67 % insatisfaits). L'écart n'est pas conjoncturel — il reflète une différence structurelle : générer de la documentation à partir d'un système existant est un problème différent de générer du design ex nihilo.

**La documentation est le goulot d'étranglement.** Seulement 17 % des équipes estiment leur documentation "très prête pour l'IA". Les 83 % restants ont un plafond implicite sur tout ce qu'elles veulent faire faire à l'IA : une documentation mal structurée produit des outputs IA mal structurés. "AI will compound good or compound bad."

**Le shadow AI est un fait de terrain.** 50 % des équipes signalent que l'usage IA par d'autres équipes leur crée des problèmes. 59 % voient de l'UI qui contourne le DS. La réponse dominante est la tolérance (44 %), pas la politique. C'est un problème d'infrastructure, pas de règles.

**Le temps, pas le budget, est la contrainte.** 25 % citent "pas de temps" comme premier frein à l'adoption IA. Budget : 5 %. Le leadership mandate et les budgets existent ; le temps d'expérimentation ne suit pas.

**La préoccupation principale n'est pas l'emploi mais la qualité.** 61 % citent la qualité des outputs comme première inquiétude. Le déplacement d'emplois : 22 % — bien derrière la qualité, l'homogénéisation, et la sur-dépendance.

## Données clés

**Adoption et outils :**
- 82 % utilisent l'IA (32 % opérationnalisé, 50 % expérimentent)
- Claude : 74 % / Figma Make : 56 % / ChatGPT : 37 % / GitHub Copilot : 36 % / Gemini : 31 % / Cursor : 29 %
- Stack moyen : 2 à 4 outils

**MCP :**
- 47 % font tourner un serveur MCP
- 31 % prévoient d'en adopter un
- 3 % non convaincus de la valeur — le "si" est réglé

**Documentation AI-readiness :**
- 17 % "très prête pour l'IA" (Very structured)
- 27 % structurée ; 35 % inconsistante ; 20 % pas organisée
- Aucune équipe ne peut compenser avec le MCP une documentation mal structurée en amont

**Satisfaction par cas d'usage (% plus satisfait) :**
- Documentation : 63 % / Audit docs : 42 % / Code generation : 38 % / Linting : 28 %
- Token management : 12 % / Design generation : 14 %
- Insatisfaction design generation : 67 %

**Shadow AI :**
- 50 % : problèmes causés par l'IA d'autres équipes
- 59 % : UI contournant le DS
- 44 % : tolérance organisationnelle

**Barrières à l'adoption IA :**
- No time : 25 % / Sécurité/politiques : 17 % / Qualité : 16 % / No budget : 5 %

**Sentiment :**
- 63 % favorables / 67 % disent overhyped — ambivalence cohérente
- 43 % : l'IA renforce la position de l'équipe DS
- 38 % : s'attendent à ce que leur équipe soit remise en question
- 39 % : gap leadership/réalité (leadership attend plus que délivré)

## Citations clés

"AI flipped documentation from writing to reviewing — half a day per component down to under an hour." (répondant)

"Don't rush — get your design system documentation right. AI will compound good or compound bad." (répondant)

"The biggest gap isn't capability — it's clarity. There's been an explosion of new tools, concepts, and abstractions and the taxonomy is inconsistent." (répondant)

"The teams winning with AI are the ones who made their design systems legible to it. Documentation, MCP, partnership, policy, time. In that order." (zeroheight, conclusion)

## Connexions identifiées

Les 17 % de AI-readiness valident empiriquement la thèse de [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) : la quasi-totalité des équipes DS n'a pas encore atteint l'état machine-readable au niveau où les agents peuvent l'utiliser de façon consistante.

Les 47 % d'adoption MCP sont la première donnée sectorielle disponible sur le déploiement réel du MCP dans les équipes DS. Elle ancre les cas d'usage documentés dans [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md) dans une réalité de terrain plutôt que dans des cas isolés.

Le shadow AI (50 % de problèmes signalés) est un nouveau concept absent du corpus antérieur du vault, documenté dans [shadow-ia-design-system](../concepts/shadow-ia-design-system.md). Il représente une menace symétrique à la promesse de l'infrastructure agentique : les agents externes contournent le DS avec autant de facilité que les agents internes peuvent le respecter.

Le gap leadership (39 %) est cohérent avec la chute du buy-in documentée dans [zeroheight-design-systems-report-2026](zeroheight-design-systems-report-2026.md) (42 %→32 %) mais l'explique différemment : le problème n'est plus le manque de soutien, c'est un excès d'attentes non calibrées.

## ⚡ Tension avec le corpus existant

Le rapport positionne la documentation comme "le goulot" et recommande de "commencer par la documentation". Le corpus du vault (Morales Achiardi, Wolosin, Kavcic) va plus loin : la documentation structurée n'est qu'un prérequis, le vrai levier est l'infrastructure agentique complète (MCP, métadonnées, gouvernance). Le rapport de zeroheight reflète l'état du terrain en 2026 ; le corpus du vault reflète l'état de l'art. L'écart entre les deux est précisément le gap qu'il faut combler.
