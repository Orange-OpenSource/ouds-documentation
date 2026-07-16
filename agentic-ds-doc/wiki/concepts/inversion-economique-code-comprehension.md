---
type: concept
tags: [ia, economie, code, comprehension, productivite]
created: 2026-06-17
updated: 2026-07-08
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md)"
  - "[design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)"
related:
  - "[design-system-as-infrastructure](design-system-as-infrastructure.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
---

## L'inversion économique : le code est gratuit, la compréhension est chère

L'un des arguments structurants de [romina-kavcic](../entities/romina-kavcic.md) est celui d'une inversion économique fondamentale induite par l'IA. Historiquement, le coût dominant du développement logiciel était le coût d'écriture du code — le temps de traduire une intention en syntaxe. L'IA compresse ce coût à presque zéro. En 2025, 41 % de tout le code produit était généré par IA, et les études montrent une augmentation de productivité de 39 % pour les développeurs utilisant des agents ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

Mais la productivité brute ne suffit pas. Ce que l'IA génère facilement, c'est du code syntaxiquement correct. Ce qu'elle ne sait pas faire sans aide, c'est décider qu'un bouton dans un alert doit utiliser le token `color.bg.danger` plutôt que `color.bg.primary`, ou qu'un bouton dans une card ne doit pas concurrencer le CTA principal de la page. Cette décision est sémantique, pas syntaxique.

## Du syntaxique au sémantique

Le travail se déplace. Ce n'est plus "comment j'écris ça" mais "quoi doit faire ça et pourquoi". C'est précisément le contenu que le design system encode : les conventions de nommage, l'intent des tokens, les descriptions de composants, les règles d'usage. Ces assets deviennent la partie chère du travail — et donc la partie qui mérite le plus d'investissement.

La formulation condensée de [romina-kavcic](../entities/romina-kavcic.md) : "When code is cheap and understanding it is expensive, architecture must optimize for the impermanence of code" ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)). Ce n'est pas une métaphore — c'est un principe d'architecture.

## Chiffres de contexte

## Le shift de compétence : craft visuel vs architecture structurelle (Nurkhon, 2026)

[figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md) traduit l'inversion économique en terme de compétence professionnelle, avec une précision que Kavcic ne formulait pas. Le travail a migré de l'écriture du code (syntaxique) vers la structuration de la connaissance (sémantique) — mais cette migration crée une bifurcation entre deux disciplines qui ne sont pas détenues par les mêmes personnes.

**Construire une librairie de composants** est un problème de *craft visuel* : variants, états, composition, hiérarchie, cohérence. Les décisions sont visuelles et méta-compositionnelles. Un designer excellent dans cet exercice choisit des noms qui ont du sens *pour les personnes dans la pièce* — qui partagent l'historique, les conventions implicites, la culture du produit.

**Rendre cette librairie machine-readable** est un problème d'*architecture structurelle* : schémas de nommage, taxonomies de tokens, contrats sémantiques entre couches, distinction canonique/résiduel. Les décisions sont épistémiques — pas "est-ce que ce nom est joli" mais "est-ce que ce nom donne à un agent assez d'information pour utiliser le composant correctement sans contexte."

Ces deux disciplines ne s'impliquent pas mutuellement. La formulation de Nurkhon : "Token naming is structural legibility, not a cosmetic concern." Ce déplacement est la conséquence directe de l'inversion économique de Kavcic — et son corollaire le plus inconfortable, parce que le recrutement, la formation, et les descriptions de poste dans les équipes de design n'ont pas encore absorbé la distinction.

28+ modèles frontière ont été publiés par 6 labos majeurs en moins de 10 mois. 226 milliards de dollars ont été investis dans l'IA en 2025, presque le double de l'année précédente. 84 % des développeurs utilisent des outils IA quotidiennement. Gartner prédit que 40 % des applications enterprise embarqueront des agents IA d'ici fin 2026 ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

[romina-kavcic](../entities/romina-kavcic.md) ajoute des données sur le coût des systèmes agentiques en contexte de design system ([design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)) : Gartner prédit une baisse de 90% du coût unitaire des tokens d'ici 2030, mais les systèmes agentiques consomment 5 à 30 fois plus de tokens par tâche qu'un chatbot standard. METR documente que la longueur des tâches complétables par les agents à 50% de fiabilité double tous les 7 mois — ce qui signifie que chaque nouvelle capacité agentique s'accompagne d'une demande accrue de contexte, amplifiant la consommation. La conséquence : l'inversion économique ne se résout pas seulement par la baisse des prix. Elle exige une optimisation du *contexte* — rendre le corpus de mémoire institutionnelle retrievable pour éviter les re-découvertes coûteuses à chaque session. Voir [memoire-design-system](memoire-design-system.md).
