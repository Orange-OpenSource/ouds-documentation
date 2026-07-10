---
type: concept
tags: [métriques, adoption, ia, design-system, gouvernance, mcp, mesure, outils, satisfaction]
created: 2026-06-22
updated: 2026-07-06
sources:
  - "[[miro-ai-design-system-mcp-claude-code-skills]]"
  - "[[atlassian-design-md-lessons]]"
  - "[[zeroheight-design-systems-report-2026]]"
  - "[[state-of-ai-design-systems-2026-zeroheight]]"
  - "[[20-ai-workflows-design-system-teams]]"
related:
  - "[[gouvernance-design-system-ia]]"
  - "[[boucle-feedback-infrastructure]]"
  - "[[andressa-lombardo]]"
  - "[[aura-miro]]"
  - "[[design-md-format]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[shadow-ia-design-system]]"
  - "[[mcp-model-context-protocol]]"
  - "[[bypass-patterns-comme-user-research]]"
---

## Métriques d'adoption IA pour un design system

Le problème de mesure de l'adoption IA dans un design system est paradoxal : quand l'infrastructure fonctionne bien, elle devient invisible. Les agents opèrent en background, les calls MCP disparaissent des dashboards actifs, le call count — la métrique instinctive — s'effondre précisément au moment où l'adoption est la plus forte.

[[andressa-lombardo]] chez Miro l'a formulé directement : "It sounds like a problem, but it meant it's working" ([[miro-ai-design-system-mcp-claude-code-skills]]). Ils avaient volontairement rendu le MCP "frictionless" — l'agent l'utilise sans que l'utilisateur ait à l'invoquer explicitement — et l'adoption avait grimpé, mais les traces actives avaient disparu.

## Ce qu'il faut mesurer à la place

Le remplacement du call count : les questions qu'on n'a plus à répondre.

**Volume de questions dans le canal Slack design system.** C'est la métrique la plus directe. Une baisse de 70 à 80 % des questions dans le canal Miro est ce qu'[[andressa-lombardo]] et [[eddie-machado]] ont mesuré après la mise en place du MCP + instruction de routage. Les ingénieurs obtenaient leurs réponses dans l'IDE — le support canal devenait inutile pour les questions simples.

**Time-to-answer pour les questions design system.** La vitesse de réponse aux questions de contribution peut être mesurée même sans savoir si c'est l'agent ou un humain qui a répondu. Une baisse de la latence de réponse indique que l'agent prend en charge le premier niveau de support.

**Contributions depuis l'extérieur de l'équipe core.** Si les contributeurs externes posent moins de questions préalables avant de soumettre un PR, c'est un signal que l'agent leur a fourni le contexte nécessaire. [[eddie-machado]] observe : "we see people more eager to contribute because there's less of a restriction now" — le wrap-up skill réduit la friction de contribution, pas seulement les questions de support.

**Témoignages qualitatifs.** [[andressa-lombardo]] pose un principe pragmatique : "Any figure is better than no figure." Même une estimation approximative, un témoignage d'ingénieur, ou un exemple documenté constituent une base pour construire le cas auprès du management. La rigueur méthodologique idéale ne doit pas empêcher de collecter ce qu'on peut avoir.

## Le problème en amont : visibilité des appels

La perte de visibilité sur les calls MCP est le prix de la fluidité. Quand le routage est explicite (l'utilisateur doit taper "use the design system MCP"), chaque appel est tracé. Quand le routage est dans le fichier Claude (transparent pour l'utilisateur), les appels se font sans signal visible. La mesure par call count suppose une friction que la bonne UX élimine.

Ce n'est pas spécifique au design system : c'est le même problème dans tout système IA qui vise la transparence. La solution n'est pas de restaurer la friction pour mesurer l'adoption — c'est de définir des métriques d'impact plutôt que de process.

## Benchmark de performance comparée (Atlassian, 2026)

[[atlassian-design-md-lessons]] publie les premières métriques de performance comparées entre approches de contexte design system. L'intérêt pour ce wiki est double : d'une part, les chiffres eux-mêmes (tokens, temps, turns) ; d'autre part, la méthodologie — une tâche fixe (écran login), quatre configurations, mesurée sur un échantillon de runs avec calcul de variance.

Les résultats clés : ADS MCP (80% contexte, 3,75M tokens, 5m1s, 35,1 turns) surpasse DESIGN.md (30% contexte, 7,21M tokens, 6m46s, 45,3 turns) et surpasse même l'absence de contexte (4,20M tokens, 6m19s, 43 turns). La surprise : no-context est plus économique que DESIGN.md — ce qui reflète la saturation du contexte par un fichier trop dense chargé all-at-once.

Atlassian précise explicitement que ces résultats ne sont "pas conclusifs" hors de leur contexte (modèle, prompts, qualité des sources, environnement). Ils constituent néanmoins le seul benchmark public à ce niveau de détail. La variance 2,7x de DESIGN.md entre les runs est la métrique la plus utile opérationnellement : elle indique une instabilité structurelle qui rend la qualité de sortie difficile à prévoir.

## Données macro sectorielles : le gap adoption/satisfaction (zeroheight, 2026)

[[zeroheight-design-systems-report-2026]] publie la mesure d'adoption IA la plus large disponible dans le secteur. Sur l'ensemble des équipes DS interrogées : **56 % utilisent l'IA**, mais seulement **15 % estiment qu'elle est à la hauteur de leurs attentes**. Ce gap de 41 points est la métrique sectorielle la plus utile de l'année — il chiffre le problème d'AI readiness à l'échelle de l'industrie, pas seulement dans les cas documentés du corpus.

Lecture croisée avec le vault : le gap n'est pas un problème de satisfaction envers les outils IA en général. Les outils fonctionnent. Le problème est que les équipes les appliquent sur des DS non préparés pour la consommation agentique — pas de metadata machine-readable, pas de MCP, nommage opaque — et obtiennent des sorties inconsistantes. La déception est structurelle, pas conjoncturelle.

Donnée additionnelle : 12 % des équipes utilisent l'IA pour la livraison de documentation, 57 % souhaiteraient le faire — soit un gap aspirationnel de 45 points sur le cas d'usage le plus direct. Ce chiffre valide l'absence de pipeline pipeline Figma→docs comme lacune opérationnelle majeure dans les équipes. En attendant la transformation d'infrastructure, les 44 % restants documentent encore manuellement.

## Lien avec la gouvernance

Cette problématique de mesure est une extension de [[gouvernance-design-system-ia]] : la gouvernance agentique nécessite non seulement de monitorer la qualité des outputs (drift scoring, audits) mais aussi de mesurer l'utilité perçue de l'infrastructure. Un système parfaitement gouverné mais non adopté a le même impact qu'une absence de système. Les métriques d'adoption ferment la boucle entre infrastructure et valeur réelle.

## Adoption et outils IA : benchmark sectoriel complet (zeroheight, mai 2026)

[[state-of-ai-design-systems-2026-zeroheight]] apporte le benchmark d'adoption le plus complet disponible sur le secteur (N=123, mai 2026). Le chiffre macro : **82 % des équipes DS utilisent l'IA sous une forme quelconque**, dont 32 % l'ont opérationnalisée ("part of workflow") et 50 % expérimentent encore. La progression est rapide : 61 % disent que l'usage a "crû significativement" dans les 12 derniers mois.

La répartition des outils (multi-select) est la première donnée publique sur les parts de marché réelles dans ce segment :

- **Claude : 74 %** — outil dominant, miroir de l'influence communautaire en ligne
- **Figma Make : 56 %** — #2 probable par effet de licence existante dans les grandes entreprises
- **ChatGPT : 37 %**
- **GitHub Copilot : 36 %**
- **Gemini : 31 %**
- **Cursor : 29 %**

Le stack moyen est de 2 à 4 outils. Les grandes entreprises (> 1 000 personnes) s'appuient davantage sur les outils pour lesquels elles ont déjà des licences (GitHub Copilot +28 pp vs. petites, Figma Make +4 pp) — indépendamment de si ce sont les meilleurs outils pour le job.

## Satisfaction par cas d'usage : la polarisation est la donnée

Le rapport zeroheight mai 2026 fournit la première cartographie publique de satisfaction par cas d'usage IA dans les DS. La polarisation est frappante :

- Documentation : **63 % satisfaits** / 19 % insatisfaits (+44 net)
- Audit/review de docs : 42 % satisfaits / 8 % insatisfaits
- Génération de code : 38 % satisfaits / 25 % insatisfaits
- Linting & compliance : 28 % satisfaits / 10 % insatisfaits
- Design generation : 14 % satisfaits / **67 % insatisfaits** (-53 net)

Ce gradient n'est pas aléatoire. La documentation est un problème de transformation d'un existant structuré en prose — ce que les LLMs font bien. La génération de design est un problème de création depuis des contraintes implicites — ce que les LLMs font mal sans contexte encodé précis. L'écart de 116 points de satisfaction nette (documentation vs. design generation) est la donnée la plus opérationnellement utile du rapport.

Implication : les équipes qui commencent par la documentation gagnent en confiance et produisent des résultats visibles. Celles qui commencent par la génération de design s'exposent à 67 % de déception — et risquent de conclure que "l'IA ne marche pas pour le DS", alors que le problème est le cas d'usage choisi.

## L'adoption MCP comme métrique d'infrastructure (zeroheight, mai 2026)

47 % des équipes DS ont déjà un serveur MCP en production — soit le signal sectoriel le plus fort qu'un changement d'infrastructure est en cours. 31 % planifient l'adoption. Seulement 3 % ne sont "pas convaincus de la valeur" — le débat "si" est clos, le débat "comment" est ouvert.

Ce chiffre complète la mesure qualitative de l'adoption MCP documentée dans [[mcp-model-context-protocol]] avec un ancrage quantitatif : à mi-2026, presque la moitié des équipes DS ont fait le pas de l'infrastructure, pas seulement de l'expérimentation avec des clients IA.

## Build-time signals comme alternative aux métriques runtime

[[romina-kavcic]] ([[20-ai-workflows-design-system-teams]]) propose une architecture de métriques build-time comme substitut aux métriques runtime invasives. Le tracking runtime (qui utilise quel composant en production, en temps réel) est perçu comme une surveillance par les équipes consommatrices. Les métriques build-time — extraites du code au moment du build, pas de l'exécution — décrivent l'état du codebase sans observer les personnes.

Quatre signaux build-time concrets : **component imports/usage counts** (combien de fois un composant est importé dans des fichiers réels), **token drift counts** (nombre de valeurs hardcodées détectées dans le codebase), **bypass signals** (occurrences de `<button>` brut, de inline styles, d'autres patterns de contournement), et **PR drift delta** (variation du drift entre deux états du code). Ces métriques sont des faits extraits du code, pas des inférences comportementales.

La recommandation : construire d'abord avec ces quatre métriques, prouver qu'elles sont utiles, puis ajouter de la complexité seulement si le besoin est démontré. C'est cohérent avec la posture de [[andressa-lombardo]] : "Any figure is better than no figure." — une estimation approximative vaut mieux qu'un dashboard parfait qu'on n'a pas.

Les bypass signals build-time sont la face quantitative de [[bypass-patterns-comme-user-research]] : ils mesurent la fréquence du problème, l'analyse IA du drift report en diagnostique les causes.
