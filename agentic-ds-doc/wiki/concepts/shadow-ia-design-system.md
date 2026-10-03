---
type: concept
tags: [shadow-ai, design-system, gouvernance, bypass, ia, adoption, derive, accessibilite]
created: 2026-07-06
updated: 2026-07-16
sources:
  - "[state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)"
related:
  - "[shadow-code](shadow-code.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[design-system-as-infrastructure](design-system-as-infrastructure.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[documentation-lag](documentation-lag.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
---

## Le Shadow AI dans les design systems

Le Shadow AI désigne l'usage d'outils d'intelligence artificielle par d'autres équipes (produit, engineering, PM) pour générer de l'UI sans impliquer l'équipe design system, et souvent sans utiliser le système comme référence. Le terme est introduit par zeroheight dans son rapport de mai 2026 ([state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)) pour décrire un phénomène qui touche déjà **50 % des équipes DS**.

## Pourquoi c'est structurellement différent de la dérive classique

La dérive des design systems n'est pas nouvelle. Ce qui change avec le Shadow AI, c'est la vitesse et l'invisibilité. Un développeur qui s'écarte manuellement du DS laisse des traces — commits, code reviews, questions Slack. Un agent IA qui génère une interface en 30 secondes depuis un prompt vague ne génère pas ces traces : l'UI "ressemble" au système, utilise des valeurs hardcodées proches des tokens réels, et passe souvent les premières revues visuelles.

Zeroheight formule le mécanisme : Figma Make et des outils comme Lovable "default to Tailwind or Radix — leaving users assuming the output is system-compliant when it isn't." L'apparence de conformité est la nouveauté. L'ancienne dérive était visible comme telle ; le Shadow AI produit une dérive que les stakeholders approuvent.

## Six modes de bypass documentés

**Looks-like-the-system bypass.** L'IA génère de l'UI visuellement proche du DS en hardcodant des valeurs copiées de mémoire ou d'un screenshot. Tokens absents, composants réinventés plutôt que réutilisés, patterns ad hoc construits depuis des primitives. La cohérence de surface masque l'incohérence structurelle.

**Prototype-devient-spec.** Des PMs et des ingénieurs génèrent des prototypes avec des outils IA (Figma Make, Lovable, v0) pour communiquer des idées. Ces prototypes arrivent devant les stakeholders avant que l'équipe DS ait pu intervenir. Une fois qu'un prototype a été approuvé — même informellement — il crée une attente de forme que l'implémentation finale doit respecter. L'équipe DS hérite d'une contrainte qu'elle n'a pas posée.

**Attentes de stakeholders verrouillées.** Le prototype vibe-codé crée une représentation visuelle que les stakeholders ont "vue" et validée. La reformulation sur le DS — qui produirait une interface légèrement différente, ou nécessiterait de revoir les patterns — est perçue comme une régression, pas comme une correction. "People create prototypes, and those prototypes create UI expectations with stakeholders." ([state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md))

**Accessibilité silencieusement supprimée.** Quand les agents IA génèrent ou réécrivent des composants, ils peuvent supprimer le comportement d'accessibilité intégré dans les composants du DS — aria-labels, gestion du focus, annonces pour les lecteurs d'écran. Ce n'est pas une erreur visible dans un premier regard visuel : elle émerge lors d'un test d'accessibilité downstream, si tant est qu'il ait lieu.

**L'équipe DS ne peut pas surveiller à cette échelle.** Chaque artefact généré par des agents IA dans une grande organisation est une surface potentielle de dérive. L'équipe DS, typiquement de taille très réduite ([metriques-adoption-ia-design-system](metriques-adoption-ia-design-system.md)), n'a pas la capacité de review systématique. Le bypass n'est pas délibéré — il est structurel.

**Shadow skills et plugins contradictoires.** Certaines équipes construisent leurs propres skills IA, prompts et plugins sans validation par l'équipe DS. Des bundles prépackagés, en particulier pour Claude et Cursor, contiennent des instructions qui contredisent les guidelines du DS — et tirent le code généré hors du système. Les règles deviennent des "contraintes de départ" contournables plutôt que des invariants.

## Réponse organisationnelle : la tolérance comme défaut

La réponse dominante au bypass dans les organisations est la tolérance — 44 % tolèrent, 23 % normalisent, seulement 15 % le découragent activement. C'est cohérent avec les contraintes de temps et de taille d'équipe : on ne peut pas surveiller ce qu'on n'a pas le temps de suivre. La tolérance n'est pas un choix stratégique, c'est le défaut en l'absence d'infrastructure.

L'effet d'échelle est net : dans les grandes entreprises (> 1 000), le bypass "généralisé" atteint 18 % contre 10 % dans les petites. Plus la surface est large, plus le Shadow AI prospère. C'est le même mécanisme que la dérive classique à la vitesse agentique.

## Pourquoi la politique seule ne suffit pas

zeroheight le formule directement dans ses 8 recommandations : "A policy crackdown won't work. Making the design system AI-consumable by default and actual change management does." La tension est structurelle : si générer de l'UI avec Figma Make ou Cursor sans le DS est plus rapide, plus simple, et que le résultat "ressemble" au DS, les équipes le feront — avec ou sans politique.

La solution n'est pas réglementaire, elle est économique. Le chemin vers le DS doit être le chemin de moindre résistance pour les agents. Cela passe par : un MCP exposant le DS dans l'IDE des développeurs (l'agent se connecte au DS naturellement), des composants nommés de façon que les agents les trouvent, une documentation structurée que les agents peuvent parser sans ambiguïté. Si l'infrastructure agentique est absente, les agents se rabattent sur les primitives disponibles — Tailwind, Radix, ou simplement des valeurs hardcodées.

Ce diagnostic converge avec [lisibilite-machine-design-system](lisibilite-machine-design-system.md) : le Shadow AI est la conséquence prévisible d'un DS non machine-readable. Un DS que les agents ne peuvent pas lire et utiliser efficacement est un DS que les agents contourneront — pas par défaut de volonté des équipes, mais par manque de chemin.

## Lien avec la gouvernance

Le Shadow AI est une nouvelle couche au problème de [gouvernance-design-system-ia](gouvernance-design-system-ia.md). La gouvernance existante (auditeurs de tokens, drift scoring, niveaux de confiance) adresse les agents opérant à l'intérieur du DS — ceux qui lisent les métadonnées, utilisent le MCP, respectent les contrats. Le Shadow AI adresse les agents opérant en dehors, sans connexion au DS.

La gouvernance du Shadow AI requiert une infrastructure distincte : des outils de détection de bypass à l'échelle (crawl d'applications, détection de composants non-DS), des signaux dans les outils que les équipes produit utilisent (linting dans Figma Make, alertes Cursor), et un modèle de partenariat plutôt que de contrôle — parce que les équipes qui bypassen le DS le font pour résoudre des problèmes réels, et la solution est de rendre le DS meilleur à résoudre ces problèmes.

## ⚡ Disambiguation avec le shadow code

À ne pas confondre avec [shadow-code](shadow-code.md), concept distinct introduit dans le vault le 2026-07-16 : le Shadow AI décrit ici est un problème de *contournement* (l'UI générée ne passe pas par le design system, avec ou sans intention). Le shadow code est un problème d'*opacité* (le code passe par les bons canaux, peut même respecter le design system, mais personne n'a tracé ses hypothèses ni son comportement sous conditions limites). Un artefact peut être Shadow AI sans être shadow code (un prototype Figma Make visible et reconnu comme hors-système) et inversement (du code généré via le MCP officiel du design system, donc non-Shadow AI, mais jamais audité en profondeur). Les deux se renforcent : un DS que les agents contournent structurellement produit plus de surface pour l'opacité, parce que moins de code passe par les contrôles centralisés de l'équipe DS.

## ⚡ Tension : le DS comme infrastructure vs. le DS comme goulot

Le Shadow AI révèle une tension dans l'argument [design-system-as-infrastructure](design-system-as-infrastructure.md). Si le DS est bien l'infrastructure sur laquelle tout le reste s'appuie, il devrait être automatiquement utilisé par tous les agents. En pratique, 50 % des équipes voient leur DS contourné. L'infrastructure n'est "automatiquement utilisée" que si elle est accessible et lisible — c'est-à-dire si les agents la trouvent et la comprennent. Un DS infrastructure-au-sens-conceptuel n'est pas automatiquement infrastructure-au-sens-agentique. La lisibilité machine n'est pas optionnelle, elle est la condition de la promesse.
