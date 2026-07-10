---
type: concept
tags: [design-system, gouvernance, tokens, format, standard, pipeline, synchronisation, ia]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[[your-design-system-fragmenting-agent-files]]"
related:
  - "[[agents-md-format]]"
  - "[[design-md-format]]"
  - "[[dtcg-annotation-schema]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[intent-token]]"
  - "[[readable-vs-usable-token]]"
  - "[[murphy-trueman]]"
---

## La dispersion des décisions de design

La multiplication des formats agent-facing (AGENTS.md, SKILL.md, DESIGN.md, Storybook Component Manifest, Zeroheight MCP) crée un phénomène structurel nouveau : une décision de design unique se réplique dans plusieurs emplacements sans lien automatique entre eux ([[your-design-system-fragmenting-agent-files]]).

## Le cas de la couleur primaire

Trueman trace concrètement où se propage une décision unique — par exemple la couleur primaire d'un produit. La source de vérité canonique vit dans un fichier JSON de tokens au format DTCG ([[dtcg-annotation-schema]]), compilé via Style Dictionary vers des CSS variables et une bibliothèque Figma Variables. De là, la valeur se propage dans quatre autres emplacements.

DESIGN.md encode la valeur en dur dans le front matter YAML, sans lien programmatique vers le fichier JSON source. Toute modification du token JSON n'est pas répercutée automatiquement dans DESIGN.md — c'est une mise à jour manuelle. AGENTS.md la référence de façon indirecte, via une règle comme "use tokens from @acme/tokens, never hardcode colours" : la règle est durable mais ne contient pas la valeur réelle. Un Figma Skill encode la procédure pour *trouver* la valeur (lire le contexte de design, identifier la variable, trouver le token projet correspondant) sans stocker la valeur elle-même. Le Storybook Component Manifest la fait émerger comme prop default ou token reference, généré automatiquement depuis les stories.

La même décision vit donc dans cinq emplacements, chacun avec un mode de représentation distinct. "Derivable in principle from the tokens file but rarely derived in practice unless someone has built the pipeline." ([[murphy-trueman]])

## La nature du problème : gouvernance, pas technologie

Cette dispersion n'est pas un bug technique corrigeable par un meilleur tooling. C'est une conséquence structurelle de l'hétérogénéité des formats. DESIGN.md est conçu pour être un fichier autonome et portable, pas une vue dérivée d'une source de vérité externe. AGENTS.md est en prose, pas en référence de tokens. Les Figma Skills sont des procédures, pas des registres de valeurs.

Le lien entre ces représentations n'existe que si une équipe construit le pipeline qui l'automatise. Sans ce pipeline, chaque format est maintenu manuellement, et la dérive entre les représentations s'accumule au fil du temps — la valeur de la couleur primaire dans DESIGN.md peut diverger de celle dans le fichier JSON sans que personne ne le détecte. La question que pose Trueman est de gouvernance : "Who maintains the seams between them? There is no role on the org chart whose job is to keep the seams healthy."

## Cartographie de propriété recommandée par Trueman

Trueman propose une répartition par couche. Les tokens restent en JSON, sous ownership du design system. Les conventions d'ingénierie vont dans AGENTS.md, maintenu par l'engineering. L'identité visuelle va dans DESIGN.md, sous ownership de quiconque détient la marque dans l'organisation. Les métadonnées de composants sont générées automatiquement depuis Storybook — pas de fichier séparé à maintenir. Le savoir procédural sur les workflows va dans SKILL.md, sous ownership de l'équipe qui pilote le tooling agent.

Cette répartition est plus claire que ce que la plupart des équipes ont aujourd'hui. Elle est aussi plus de travail que ce pour quoi la plupart des équipes sont dimensionnées. "That's a clearer architecture than most teams have today. It's also more work than most teams are scoped for, which is the real problem nobody is solving." ([[murphy-trueman]])

## Lien avec la pile de formats agent-facing

La dispersion des décisions est la contrepartie directe de la richesse des formats disponibles. Plus une organisation adopte de formats distincts pour exposer son design system aux agents, plus le nombre de représentations de chaque décision augmente. La solution n'est pas de ne pas adopter ces formats — ils ont chacun une valeur légitime pour des audiences d'agents différentes. La solution est de clarifier quelle représentation fait autorité, qui la maintient, et quel pipeline (si il existe) propage les changements vers les autres.

## ⚡ Tension : autonomie des formats vs cohérence globale

La propriété qui rend chaque format utile (il est autonome et portable — on peut donner DESIGN.md à un agent sans lui donner le reste du système) est aussi ce qui produit la dispersion. Un format qui dépend de la source de vérité centrale pour être valide n'est pas portable. Un format portable doit encoder suffisamment d'information pour fonctionner seul, ce qui signifie dupliquer des informations qui vivent déjà ailleurs. Il n'y a pas de solution élégante à cette tension — seulement des pipelines de synchronisation plus ou moins automatisés, et une gouvernance organisationnelle qui décide quelle représentation gagne en cas de conflit.
