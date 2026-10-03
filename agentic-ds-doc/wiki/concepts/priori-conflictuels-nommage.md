---
type: concept
tags: [tokens, nommage, ia, priors, entrainement, grammaire, conventions, variance]
created: 2026-06-22
updated: 2026-06-29
sources:
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md)"
  - "[tdp-agentic-design-system-guide](../sources/tdp-agentic-design-system-guide.md)"
related:
  - "[intent-token](intent-token.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[dtcg-annotation-schema](dtcg-annotation-schema.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
---

## Le problème des priors conflictuels

[romina-kavcic](../entities/romina-kavcic.md) identifie dans son audit de 50 systèmes ([50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)) un mécanisme contre-intuitif : les agents IA ne génèrent pas des noms de tokens par ignorance — ils les génèrent à partir de priors d'entraînement qui incluent toutes les conventions documentées dans les systèmes publics. Ce qui signifie qu'un agent arrive dans un codebase avec **10 grammaires de nommage incompatibles en tête simultanément**, et qu'il les mélange.

Ce n'est pas un bug de raisonnement. C'est le comportement attendu d'un modèle entraîné sur des données hétérogènes. Le résultat est un nom de token *plausible* — il ressemble à quelque chose de professionnel — mais qui ne correspond à la convention d'aucun des 10 systèmes : "un dotted path ici, un kebab role là, un camelCase state collé à la fin."

## La diversité mesurée

L'audit documente au moins 8 conventions de nommage en usage actif pour désigner la même chose — une couleur de background sémantique :

- `surface.default` (Workday)
- `color-background-strong` (Twilio)
- `color-bg-fill-critical-hover` (Polaris)
- `colorNeutralForeground1` (Fluent)
- `action.primary.background.default` (GitLab)
- `global.background.color.primary.default` (PatternFly)
- `colorBackgroundButtonPrimaryActive` (Cloudscape)
- `accent-background-color-default` (Spectrum)

Et pour la primitive "bleu" : `blue.500`, `blue[6]`, `--blue-9`, `--blue-7`, `blue50`, `base.color.blue.5`, `blue-500`, `SCIENCE_BLUE` — aucune grammaire commune.

La colonne de droite dans le tableau comparatif de Kavcic résume le problème : même *l'ordre de l'information* dans le nom diffère. Certains systèmes mettent la propriété en premier, d'autres le rôle, d'autres encore le contexte. Cloudscape encode cinq faits dans un seul nom ; `layer01` de Carbon en encode deux.

## Pourquoi les tokens générés semblent bons mais ne le sont pas

Un agent qui génère un nom de token dans un codebase ne produit pas un nom aléatoire. Il produit le nom le plus probable selon ses données d'entraînement — qui agrège toutes les conventions connues. Le résultat est syntaxiquement valide et sémantiquement cohérent dans une logique quelconque, mais ce n'est pas *votre* logique.

C'est plus difficile à détecter que l'ignorance pure. Un token inventé par mélange de conventions passe la review si le reviewer ne connaît pas intimement la convention maison. Il sera utilisé, copié, et propagé. La dérive s'installe non pas par erreur flagrante mais par plausibilité.

## Le correctif : déclarer la grammaire

La correction est explicitement minimale — une ligne dans le fichier source ou le document de conventions, à l'endroit que l'agent chargera en premier :

> "Our tokens follow `category-role-state`, kebab-case, semantic names only."

Un agent peut suivre une grammaire déclarée avec précision. Ce qu'il ne peut pas faire, c'est deviner laquelle des 10 grammaires tu as choisie. La déclaration n'est pas de la documentation supplémentaire — c'est lever une ambiguïté que le modèle ne peut pas résoudre autrement.

Ce principe est l'application directe du concept de [lisibilite-machine-design-system](lisibilite-machine-design-system.md) au niveau du nommage : rendre explicite ce qui est implicite dans la culture d'équipe.

## Le judgment gap : accidents historiques vs décisions intentionnelles (Nurkhon, 2026)

[figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md) ajoute une dimension absente de l'audit Kavcic : les priors conflictuels ne sont pas le seul problème de nommage. Il y a une couche antérieure — le **judgment gap** — que les priors conflictuels ne peuvent pas résoudre même avec une grammaire déclarée.

Dans un fichier Figma typique, deux composants visuellement identiques peuvent coexister : l'un production-approved, l'autre une expérience de Q3 2024 jamais supprimée. Les noms des deux composants peuvent respecter la grammaire déclarée du système (`category/component/state`), et pourtant l'un est signal et l'autre est bruit. L'agent traite les deux identiquement — "it reads what's there and uses it. It has no mechanism for noticing that `card-light-updated` was an experiment from Q3 2024 that was never production-approved."

Ce judgment gap est distinct du problème des priors : il ne s'agit pas d'une confusion entre 10 grammaires incompatibles, mais de l'impossibilité pour l'agent de distinguer ce qui est intentionnel de ce qui est accidentel dans un système par ailleurs correctement nommé. La correction est irréductiblement humaine — un audit de la librairie pour séparer le canonique du résiduel, avant que l'agent commence à lire. La grammaire déclarée guide la génération de nouveaux noms ; elle ne nettoie pas les artefacts historiques mal étiquetés.

La formulation condensée : "Consistent wrong output, with high confidence, at scale." Un agent consommant une librairie bruitée ne produit pas des erreurs aléatoires — il reproduit le bruit systématiquement, à l'échelle, avec la même confiance qu'il aurait sur du signal propre.

## Nommage de variables Figma : intent vs position (Alter / TDP, 2026)

[tdp-agentic-design-system-guide](../sources/tdp-agentic-design-system-guide.md) applique la même logique que Kavcic au niveau des variables Figma (et non des tokens de code), avec une distinction terminologique nette. Les variables nommées par **position hiérarchique** — `primary`, `secondary`, `tertiary` — sont des priors positionnels : elles disent à l'agent où la variable se situe dans la hiérarchie, pas pourquoi elle existe. Les variables nommées par **rôle sémantique** — `emphasis`, `default`, `subtle` — sont des priors d'intent : elles disent à l'agent le comportement visuel qu'elles encodent.

La différence opérationnelle est la même que dans le corpus tokens : un agent peut raisonner sur `emphasis` ("cette zone nécessite de l'emphase visuelle → j'utilise la variable emphasis") mais pas sur `primary` ("quelle est la règle d'emploi de la variable primary ? je ne sais pas"). Les noms positionnels fonctionnent dans un contexte où le lecteur connaît la hiérarchie — ce que l'agent ne connaît pas par défaut.

Prescriptions pratiques d'Alter : chaque variable Figma doit avoir une description textuelle d'une ligne ("Hover state on items with subtle emphasis", "Active background for primary CTAs"). Ces descriptions voyagent avec le design lors de l'extraction MCP et fournissent à l'agent le contexte qui manquait dans le nom seul.

## Lien avec les violations d'intent

Les priors conflictuels créent un type spécifique de [violation d'intent](existence-vs-intent-violations.md) : le token *existe* (il a été généré avec une convention valide), mais il ne suit pas la convention du système (il suit une convention mélangée). C'est une violation invisible pour tout outil qui ne connaît pas la grammaire déclarée — ce qui est le cas de la quasi-totalité des linters standards.
