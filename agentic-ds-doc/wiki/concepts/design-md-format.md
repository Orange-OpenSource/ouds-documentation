---
type: concept
tags: [design-system, machine-readable, format, standard, google, tokens, cli, open-source, identite-visuelle, agents-md, skill-md]
created: 2026-06-26
updated: 2026-07-07
sources:
  - "[[google-design-md-spec]]"
  - "[[atlassian-design-md-lessons]]"
  - "[[your-design-system-fragmenting-agent-files]]"
related:
  - "[[lisibilite-machine-design-system]]"
  - "[[dsds-format]]"
  - "[[intent-token]]"
  - "[[dtcg-annotation-schema]]"
  - "[[readable-vs-usable-token]]"
  - "[[systeme-de-design-agentique]]"
  - "[[accessibilite-continue]]"
  - "[[protocole-pas-produit]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[metriques-adoption-ia-design-system]]"
  - "[[agents-md-format]]"
  - "[[dispersion-decision-design]]"
  - "[[murphy-trueman]]"
---

## Le format DESIGN.md

DESIGN.md est une spécification de format open source (Apache 2.0, Google Labs, avril 2026) permettant de décrire une identité visuelle à des coding agents. C'est la réponse la plus directe du marché au problème que [[readable-vs-usable-token]] a formalisé : les tokens sont compilables mais l'agent ne sait pas pourquoi choisir `tertiary` plutôt que `primary` ([[google-design-md-spec]]).

L'architecture du format repose sur une combinaison délibérée de deux couches. Le YAML front matter encode les valeurs exactes des tokens (couleurs, typographie, espacement, border-radius, composants) sous une forme directement parsable. Le corps Markdown encode le *pourquoi* : pourquoi ce primary est "de l'encre profonde pour les titres", pourquoi ce tertiary est "le seul driver d'interaction". Les tokens disent à l'agent *quoi* ; la prose lui dit *quand et comment* — la même distinction que [[intent-token]] formalise pour les tokens DTCG individuels, mais élevée au niveau du système entier.

Un agent qui lit un fichier DESIGN.md valide peut produire une UI cohérente avec la marque sans que le prompt ne ré-explique les valeurs à chaque session. C'est un mécanisme de persistance du contexte de design system : le fichier est importé une fois, lu à chaque génération.

## Structure du format

Le schéma de tokens supporte cinq catégories : `colors` (toute syntaxe CSS valide, y compris oklch), `typography` (objet avec fontFamily, fontSize, fontWeight, lineHeight, letterSpacing, fontFeature, fontVariation), `rounded` (scale par niveau : sm, md, lg), `spacing` (scale par niveau), et `components` (mapping nom → propriétés, avec support des token references de type `{colors.primary}`).

Les composants encodent leurs propriétés via un jeu fermé de clés valides : `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Les variantes d'état (hover, active, pressed) sont des entrées séparées avec un nom dérivé (`button-primary-hover`). Cette convention de nommage est le seul mécanisme de liaison entre état de base et variante — pas d'héritage explicite.

L'ordre canonique des sections Markdown suit une hiérarchie logique : Overview → Colors → Typography → Layout → Elevation → Shapes → Components → Do's and Don'ts. Les sections peuvent être omises ; celles présentes doivent respecter cet ordre (vérifié par le linter).

## La CLI comme outil de gouvernance

La CLI `@google/design.md` est l'infrastructure opérationnelle du format. Elle expose trois commandes principales.

`lint` applique 9 règles de validation : références de tokens cassées (error), absence de couleur primary (warning), paires bg/textColor sous le seuil WCAG AA de 4,5:1 (warning), tokens définis mais jamais référencés (warning), sections absentes ou hors ordre (warning/info), clés YAML ressemblant à des fautes de frappe (warning). Cette dernière règle est remarquable : elle bascule la détection de typos du niveau humain au niveau outillé, sans faux positifs sur les clés d'extension custom.

`diff` compare deux versions d'un fichier DESIGN.md et produit un rapport de régression token-level — quelles couleurs ont été ajoutées, supprimées ou modifiées, si la modification constitue une régression (plus d'erreurs/warnings dans le "after"). C'est une primitive de CI/CD pour le design system : un push qui dégrade la conformité WCAG peut être bloqué automatiquement.

`export` convertit les tokens vers trois formats cibles : Tailwind v3 (JSON theme.extend), Tailwind v4 (CSS @theme block avec custom properties), et W3C DTCG (tokens.json). Ce dernier export crée un pont de DESIGN.md vers l'écosystème DTCG ([[dtcg-annotation-schema]]), ouvrant la possibilité d'un pipeline DESIGN.md → DTCG → outils existants sans réécriture.

## Rapport avec les autres formats du corpus

DESIGN.md n'est pas en concurrence avec DSDS ([[dsds-format]]) ni avec DTCG ([[dtcg-annotation-schema]]) — les trois formats couvrent des couches distinctes. DTCG gère les valeurs de tokens brutes avec leurs annotations sémantiques. DSDS gère la documentation comportementale des composants (API, variants, states, patterns, governance). DESIGN.md gère l'identité visuelle globale du projet — le *character* du système plutôt que ses règles internes.

La division du travail est opérationnelle : DESIGN.md est un fichier par projet (une identité), DSDS est un fichier par entité (un composant ou pattern), DTCG est un fichier de tokens (les valeurs). Un système mature peut embarquer les trois sans redondance.

La différence de philosophie est aussi de complexité d'adoption. DESIGN.md est conçu pour être simple : un fichier, une CLI npm, un concept clair. DSDS est plus exhaustif mais suppose une structuration par entités et un investissement de format plus significatif. Pour une équipe qui part de zéro, DESIGN.md offre un point d'entrée à faible friction vers la lisibilité machine.

## Adoption et statut

Lancé en alpha depuis Google Stitch le 21 avril 2026, le format a atteint 15 800 étoiles GitHub et 1 500 forks en moins de trois mois — une adoption exceptionnellement rapide pour une spec de format. La licence Apache 2.0 et le détachement délibéré de Google Stitch ("usable by any coding agent on any platform") sont des signaux forts d'une stratégie de standardisation ouverte.

Le format est en version alpha ; le schéma, la spec et la CLI sont sous développement actif. Cela signifie que les propriétés de composants, l'ordre des sections et les règles de linting peuvent évoluer. Pour des équipes qui adoptent le format dès maintenant, un suivi des breaking changes entre versions est nécessaire.

## Preuve empirique : portabilité contre performance (Atlassian, 2026)

[[atlassian-design-md-lessons]] publie le premier benchmark contrôlé comparant DESIGN.md à un MCP design system sur une tâche de production réelle (écran login, 50+ composants, ADS). Les résultats quantifient ce que la spec elle-même reconnaît : le format capture "l'intent, pas les détails complets". ADS MCP : 3,75M tokens, 5m1s, 35 turns, ~80% du contexte disponible. DESIGN.md : 7,21M tokens, 6m46s, 45,3 turns, ~30% du contexte. Soit 92% plus de tokens pour moins de deux fois moins de contexte — et 2,7x plus de variance entre les runs.

Atlassian identifie trois limites structurelles. D'abord, le chargement all-at-once : là où un MCP fait un tool call ciblé pour un composant spécifique (voir [[mcp-on-demand-vs-rules-always-on]]), DESIGN.md charge tout en début de contexte, entraînant troncature précoce et coût fixe élevé. Ensuite, la compression forcée : leur fichier de 80 KB (~19 800 tokens) ne représente que 30% du contenu réellement disponible dans leur MCP, après avoir coupé la quasi-totalité des guidelines de composants. Enfin, la distinction la plus conceptuellement significative : DESIGN.md est une **spec for reimplementing** — une description qui permet de reconstruire le design system depuis zéro. Un MCP de production est un **guide for using** — une documentation pour importer et utiliser les composants existants. En testant DESIGN.md sur leur codebase, les agents recréaient systématiquement les composants Atlassian au lieu de les importer depuis `@atlaskit/button`.

Cette distinction *reimplementing vs using* reformule la limite du format de façon précise : DESIGN.md est optimal pour les environnements sans codebase existante (prototypage, nouvel outil, green-field) et insuffisant pour les environnements avec une bibliothèque de composants déjà en production. Atlassian identifie quatre cas d'usage légitimes : direction artistique haut niveau, prototypage rapide cross-tools, interopérabilité avec les design tools qui assemblent par customisation, et **customer theming for adaptive UIs** — permettre aux clients d'une plateforme de décrire leur propre marque pour que les dashboards et rapports IA générés reflètent leur identité plutôt que celle du vendeur. Ce dernier cas est un nouveau pattern agentique qui n'existait pas dans le corpus.

## DESIGN.md dans la pile des trois formats

[[murphy-trueman]] positionne DESIGN.md dans le contexte de la pile complète des formats agent-facing ([[your-design-system-fragmenting-agent-files]]). Dans cette pile, [[agents-md-format|AGENTS.md]] est la couche d'orchestration (le routeur qui indique à l'agent où trouver les autres ressources), [[architecture-skills-rules-instructions|SKILL.md]] est la couche procédurale (comment faire quelque chose étape par étape), et DESIGN.md est la couche d'identité visuelle (ce que le produit doit *être*). Les trois ne se substituent pas — ils s'articulent. Un AGENTS.md bien écrit inclut une ligne pointant vers le DESIGN.md comme source canonique pour les décisions de design. DESIGN.md n'a pas connaissance d'AGENTS.md.

La validité empirique de l'architecture YAML+Markdown de DESIGN.md est confirmée par le benchmark [[diana-wolosin]] chez Indeed : "JSON for MCP, Markdown for LLM" — données structurées (APIs, props, variants) en JSON, guidance en prose pour le modèle en Markdown. DESIGN.md implémente exactement cette bipartition avec son YAML front matter (valeurs parsables) et son corps Markdown (règles d'usage en prose).

Trueman précise aussi le contexte d'usage optimal : "DESIGN.md matters most to teams using AI design tools (Google Stitch, Lovable, v0) where the agent doesn't have access to your Figma library and needs to generate UI from a prompt. If your engineers use Cursor or Claude Code against an existing codebase with components already built, DESIGN.md is less load-bearing because the agent can read your component implementations directly." Ce calibrage précise la limite structurelle déjà documentée depuis [[atlassian-design-md-lessons]] : c'est une spec for reimplementing, pas un guide for using.

Enfin, DESIGN.md n'est pas un remplacement pour une architecture DTCG complète. Les tokens DESIGN.md sont une surface agent-facing à plat — ils ne portent pas la structure sémantique, les thèmes, les modes, ni la séparation par tier d'un système DTCG ([[dtcg-annotation-schema]]). Les deux couches sont complémentaires, pas interchangeables.

## ⚡ Tension : DESIGN.md vs standardisation par organisme

DESIGN.md est une spécification open source portée par Google Labs, sans endorsement d'un organisme de normalisation (W3C, ISO). La rapidité de son adoption contraste avec la lenteur de l'adoption du W3C DTCG, soutenu institutionnellement mais mis des années à s'imposer. La question ouverte : un standard de facto porté par un acteur dominant (Google) a-t-il plus de chances de s'imposer qu'un standard de jure porté par un consortium ? L'histoire des formats web offre des exemples dans les deux sens. La même tension s'applique à DSDS ([[dsds-format]]) : les deux formats sont des drafts sans endorsement institutionnel — leur compétition pour l'adoption réelle est encore ouverte.
