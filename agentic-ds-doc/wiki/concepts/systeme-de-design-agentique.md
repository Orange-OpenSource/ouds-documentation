---
type: concept
tags: [design-system, agentic, ia, agents, automatisation]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-system-most-important-asset-ai-era]]"
  - "[[towards-agentic-design-system]]"
  - "[[design-systems-that-document-ai]]"
  - "[[agentic-design-systems-2026-bradfrost]]"
  - "[[design-system-documentation-spec]]"
  - "[[meta-astryx-design-system]]"
  - "[[tdp-agentic-design-system-guide]]"
  - "[[zeroheight-design-systems-report-2026]]"
  - "[[agentic-ds-from-chatbot-to-orchestration]]"
  - "[[meta-astryx-harsha-sridhar]]"
related:
  - "[[design-system-as-infrastructure]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[trois-couches-composants-agents]]"
  - "[[mcp-model-context-protocol]]"
  - "[[pipeline-intent-context-systeme]]"
  - "[[knowledge-graph-design-system]]"
  - "[[protocole-arc]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[deux-lectures-du-design-system-ia]]"
  - "[[modele-maturite-ia-design-system]]"
  - "[[brad-frost]]"
  - "[[composant-comme-contrat]]"
  - "[[orchestration-multi-agents]]"
---

## Système de design agentique

Un système de design agentique est un design system conçu pour être opéré, interrogé et étendu par des agents IA, en plus des équipes humaines. C'est la réponse structurelle à un monde où 41 % du code est généré par IA et où des agents autonomes prennent des décisions de composition sans supervision directe ([[design-system-most-important-asset-ai-era]]).

La différence avec un design system traditionnel est qualitative, pas seulement quantitative. Un design system standard documente pour les humains : des guidelines en prose, des exemples visuels, des règles implicites portées par la culture d'équipe. Un système agentique documente pour les machines : des descriptions structurées, des métadonnées de contexte explicites, des règles de sélection formalisées que l'agent peut traverser algorithmiquement.

## Les trois propriétés d'un agent

Ce qui rend un agent différent d'un simple outil d'autocomplétion, c'est trois caractéristiques combinées : l'autonomie (il prend des décisions sans supervision continue), l'utilisation d'outils (il interagit avec des systèmes externes via [[mcp-model-context-protocol]] ou CLI), et les boucles de feedback (il observe le résultat de ses actions et s'ajuste). Ces trois propriétés impliquent que le système de design doit fournir non seulement quoi faire, mais pourquoi et quand — voir [[trois-couches-composants-agents]].

## Ce que ça change concrètement

Quand un développeur demande "un dialog de confirmation pour supprimer un workspace", un agent agentique ne se contente pas de suggérer un composant Dialog. Il lit l'index pour connaître les dépendances, consulte les métadonnées pour comprendre l'intent (action destructive → variante `destructive`), suit le raisonnement de composition (Dialog + Alert + deux Buttons), et applique le token approprié (`color.bg.danger` et non `color.bg.primary`). Ce flux complet ne fonctionne que si les trois couches sont présentes ([[trois-couches-composants-agents]]).

## Quand l'IA devient agentique : la distinction User/Maintainer

[[cristian-morales-achiardi]] affine la définition avec un critère opérationnel ([[towards-agentic-design-system]]) : un design system est agentique quand l'IA peut passer du rôle de *User* (qui consomme le système) au rôle de *Maintainer* (qui fait respecter ses contrats). Un User répond à "comment j'utilise ce composant ?". Un Maintainer répond à "est-ce que ce composant devrait exister ?" et détecte les dérives par rapport aux décisions architecturales encodées. Voir [[user-vs-maintainer-ia]] pour le développement de cette distinction.

## Cadre de maturité : le protocole ARC

Le [[protocole-arc]] (Audit → Report → Compose) structure la progression vers l'auto-gouvernance en trois phases : Phase 1 (l'IA comme consommateur, prouvée empiriquement), Phase 2 (l'IA comme mainteneur, validée), Phase 3 (l'IA comme auto-gouverneur, future). Chaque phase requiert un niveau de complétude supérieur des [[trois-couches-composants-agents]].

## Une deuxième lecture du terme "agentique"

[[romina-kavcic]] introduit dans "Design Systems That Document AI" ([[design-systems-that-document-ai]]) une lecture différente du syntagme "design system et IA" : non plus l'IA qui opère le design system, mais le design system qui documente les fonctionnalités IA pour les utilisateurs humains. Cette lecture produit des concepts distincts — [[modele-maturite-ia-design-system]], [[quatre-regles-ia-ux]], value gate — et une question différente : comment documenter les patterns d'interface pour des fonctionnalités comme la génération de texte, la suggestion ou la classification ?

Ces deux lectures sont complémentaires mais non interchangeables. Un système peut atteindre le Niveau 5 de la maturité IA-pour-humains (infrastructure Copilot UI Kits cross-platform) sans avoir aucune infrastructure machine-readable pour les agents — et vice versa. La confusion entre les deux lectures est précisément ce que [[deux-lectures-du-design-system-ia]] cherche à dissoudre.

## DS+AI vs vibe coding

[[brad-frost]] introduit une distinction terminologique utile ([[agentic-design-systems-2026-bradfrost]]) : **DS+AI** désigne l'usage de l'IA délibérément contraint par le design system, par opposition au **vibe coding** où l'IA génère librement sans contrainte de cohérence. "The AI is deliberately constrained to using the high-quality design system materials to ensure what's being generated adheres to the organization's established standards."

Cette distinction confirme la thèse centrale du vault depuis un angle différent : la valeur du design system agentique n'est pas d'accélérer la génération, mais de lui donner de la qualité et de la cohérence. Un agent sans design system peut produire vite ; un agent avec design system produit *bien*. C'est la formulation opérationnelle de [[seeds-vs-trees]] et de [[lisibilite-machine-design-system]] : les fondations ne ralentissent pas la génération — elles en font la qualité.

Brad Frost introduit également le terme **"mouth coding"** : des membres non-techniques (PMs, content designers, chercheurs) verbalisent des features produit pendant des sessions collaboratives, et voient le résultat émerger en temps réel via les composants du design system. C'est l'illustration la plus concrète de la valeur finale de DS+AI : non pas remplacer les développeurs, mais étendre l'accès à la création de prototypes production-grade à toute l'équipe.

## Séries de référence

Le concept est développé en parallèle par deux auteurs : [[romina-kavcic]] dans sa série "Agentic Design Systems" présentée à l'[[into-design-systems-conference]] 2026 (approche conceptuelle et outillage), et [[cristian-morales-achiardi]] dans sa série "Agentic Design System" sur Design Systems Collective (approche empirique et implémentation). Les deux convergent sur les fondamentaux, avec des vocabulaires légèrement différents : Kavcic parle de "machine-readable design system", Morales de "AI-ready infrastructure" — voir [[lisibilite-machine-design-system]].

## Astryx : premier DS conçu ground-up pour les agents (Meta, 2026)

[[meta-astryx-design-system]] marque un seuil dans le domaine : Meta open-source en juin 2026 le premier design system majeur conçu "ground-up to be AI-operable" — non pas un système existant retrofitté, mais une architecture dont l'opérabilité agentique est un principe fondateur. La distinction est posée explicitement dans la documentation officielle : "opposed to retrofitting existing design systems to play nicely with agent behaviors."

L'architecture agent-ready d'Astryx repose sur trois couches techniques. Les composants portent des annotations JSDoc avec composition hints lisibles par les agents. Un CLI (`astryx` / `xds`) expose la même API qu'un développeur humain utiliserait — avec une commande clé : `npx astryx manifest --json`, qui retourne un manifest auto-descriptif de chaque commande, argument, flag et type de réponse. "The same kind of structured specification that the backend world has had in OpenAPI for a decade, now applied to a frontend design system for the first time." Un serveur MCP compatible Cursor, Claude Code et GitHub Copilot permet aux agents de scaffolder, naviguer et documenter via cette API structurée.

Astryx valide empiriquement la thèse centrale du vault : un design system agentique ne se construit pas en ajoutant un MCP à l'existant — il requiert de repenser l'architecture depuis le départ. La conception est identique à [[protocole-pas-produit]] (Kavcic) : l'infrastructure de distribution (CLI + MCP + manifest) prime sur les fonctionnalités. 13 000 applications internes Meta testées sur 8 ans, licence MIT, Beta depuis juin 2026.

## Le gap adoption/satisfaction comme mesure d'AI readiness (zeroheight, 2026)

[[zeroheight-design-systems-report-2026]] quantifie l'état de terrain avec la donnée macro la plus importante publiée à ce jour : **56 % des équipes DS utilisent l'IA, mais seulement 15 % estiment qu'elle est à la hauteur des attentes** — soit un gap de 41 points. Cette statistique est la preuve en volume que le problème d'AI readiness n'est pas théorique. Les équipes adoptent massivement, les résultats ne suivent pas.

L'interprétation cohérente avec le corpus : les équipes utilisent des agents IA sur des DS non préparés pour la consommation agentique — pas de metadata machine-readable, pas de MCP, nommage opaque — et obtiennent des sorties décevantes. Le gap n'est pas un problème d'outil. C'est un problème de substrat. La contrainte de ressources aggrave la situation : 61 % des équipes ont 5 personnes ou moins, 56 % citent le staffing comme challenge #1 — les équipes les plus contraintes sont celles qui ont le moins de capacité à transformer leur infrastructure.

## Le composant comme contrat : la reformulation de Kavcic (mai 2026)

[[romina-kavcic]] reformule le paradigme agentique avec une précision supplémentaire dans "From Chatbot to Orchestration" ([[agentic-ds-from-chatbot-to-orchestration]]) : la bonne question n'est pas "comment utiliser l'IA pour générer des composants plus vite", mais "est-ce que l'IA peut comprendre *pourquoi* ce composant existe, *quand* l'utiliser, et *quand ne pas le faire* ?" Le design system agentique se juge à la qualité de cette compréhension, pas à la vitesse de génération.

La contribution conceptuelle principale est le renversement composant → contrat : dans un design system agentique, un composant n'est plus quelque chose qu'on importe mais un contrat entre design, code, intent produit, accessibilité et comportement. Un bouton porte non seulement son API (`<Button variant="primary">`) mais ses règles d'usage (quand utiliser primary vs destructive), ses contraintes (escalader si le variant requis n'existe pas, ne jamais créer de styling one-off sans vérifier les tokens), ses exigences d'accessibilité non-négociables. Voir [[composant-comme-contrat]] pour le développement complet.

Cette formulation converge avec [[trois-couches-composants-agents]] et [[schema-metadata-composant]], mais depuis un angle différent : Kavcic part de l'intent du composant pour définir ce qu'un contrat doit contenir, là où Morales Achiardi part de l'infrastructure machine-readable pour définir ce que le système doit exposer.

## Validation de marché externe : "first with product, not a footnote"

La couverture officielle Meta ([[meta-astryx-design-system]]) documente Astryx depuis la communication de l'éditeur. [[meta-astryx-harsha-sridhar]] (Harsha Sridhar, juillet 2026) apporte la validation externe qui manquait : "Astryx is the first system from a major vendor that's answered the 'and what about agents?' question with actual product, not a footnote." Cette formulation confirme la thèse centrale du vault depuis un angle de marché — non pas depuis l'intérieur de Meta, mais depuis le regard d'un praticien qui compare Astryx à MUI, Atlaskit et Shadcn/ui.

La partition que Sridhar dessine révèle ce qu'occupait chaque quadrant avant Astryx : MUI (composants scellés, visual lock-in), Atlaskit (scellés, Atlassian-shaped), Shadcn/ui (ouverts, mais sans maintien centralisé). Aucun n'avait de CLI structuré pour agents, aucun n'avait de serveur MCP, aucun n'avait de "Quick Start with AI" dans sa documentation. "The design systems that will matter over the next few years will be judged on a different axis: how well they compose, how much of their internals they expose, and how legibly they present themselves to both a human and a model." Voir [[astryx-vs-mui-atlaskit-shadcn]] pour la comparaison complète.

## Orchestration multi-agents : la configuration opérationnelle

La même source introduit le modèle d'orchestration multi-agents comme configuration opérationnelle d'un design system agentique : quatre agents spécialisés (designer, développeur, documentation, QA) coordonnés par un orchestrateur qui décide des niveaux d'autonomie par action. Voir [[orchestration-multi-agents]] pour l'architecture détaillée.

Le principe central est la "governed autonomy" : déléguer juste assez pour que le système accélère, pas assez pour perdre la supervision. Chaque agent proposé, l'orchestrateur valide ; les changements risqués escaladent. Ce modèle est la réalisation opérationnelle du [[protocole-arc]] Phase 3 — encore théorique dans les sources antérieures, maintenant articulée comme architecture cible. Le précédent empirique le plus proche dans le vault est la boucle self-healing de [[romina-kavcic]] avec 12 outils MCP ([[self-healing-design-system]]), qui est la version mono-agent de ce système multi-agents.

## Format de référence standardisé : DSDS (Onori, 2026)

[[pj-onori]] publie en juin 2026 la [[dsds-format|Design System Documentation Spec (DSDS)]] ([[design-system-documentation-spec]]), première spécification ouverte qui codifie le format d'un design system agentique. DSDS couvre les 7 types d'entités d'un design system (component, token, token-group, theme, foundation, pattern, guide), 16 types de document blocks, et le mécanisme formel `agentDocumentBlocks` — l'espace séparé pour les règles que seuls les agents lisent.

Là où le corpus décrit les propriétés nécessaires d'un système agentique, DSDS est le premier format à les formaliser dans une spec validable et portable. Un design system agentique au sens du vault — avec ses trois couches ([[trois-couches-composants-agents]]) et ses règles machine-readable — peut désormais être exprimé dans un format standard, non lié à une plateforme, survivant aux changements d'outil. DSDS est à la documentation de design system ce que le DTCG est aux tokens : la tentative de standardiser ce qui était jusqu'alors une convention maison variable.
