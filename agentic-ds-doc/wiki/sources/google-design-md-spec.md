---
type: source
tags: [design-system, machine-readable, format, standard, google, tokens, cli, open-source]
created: 2026-06-26
updated: 2026-06-26
sources: []
related:
  - "[[design-md-format]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[dsds-format]]"
  - "[[intent-token]]"
  - "[[dtcg-annotation-schema]]"
  - "[[readable-vs-usable-token]]"
  - "[[systeme-de-design-agentique]]"
---

## DESIGN.md — Format Specification (Google Labs, 2026)

**URL** : https://github.com/google-labs-code/design.md
**Auteur** : Google Labs (google-labs-code)
**Date** : v0.2.0 — 26 mai 2026 (open-sourcé depuis Google Stitch le 21 avril 2026)
**Licence** : Apache 2.0 | **Stars** : 15 800

## Thèse principale

DESIGN.md est une spécification de format permettant de décrire une identité visuelle à des coding agents. L'architecture centrale du format est la combinaison de deux couches complémentaires : un YAML front matter (tokens machine-readable — valeurs exactes) et un corps Markdown (prose humain-readable — le *pourquoi* des valeurs). Les tokens disent à l'agent *quoi* ; la prose lui dit *quand et comment*.

## Thèses secondaires

Un agent qui lit un fichier DESIGN.md valide peut produire une UI cohérente avec la marque sans que le prompt ne ré-explique les valeurs à chaque session. Le format est conçu pour être persistant et réutilisable cross-sessions.

La CLI associée (`@google/design.md`) fournit trois outils opérationnels : `lint` (9 règles de validation dont vérification WCAG AA sur les paires de couleurs), `diff` (détection de régressions token-level entre deux versions), `export` (conversion vers Tailwind v3, Tailwind v4 CSS, ou W3C DTCG).

Le format est délibérément alpha et minimaliste — il couvre couleurs, typographie, espacement, border-radius et composants. Il ne prétend pas remplacer DSDS ([[dsds-format]]) ou DTCG ([[dtcg-annotation-schema]]) : il est le complément de présentation de l'identité visuelle là où DSDS gère le comportement et la documentation structurée des composants.

## Citations clés (≤ 15 mots)

> "Tokens give agents exact values. Prose tells them *why* those values exist."

> "An agent that reads this file will produce a UI consistent with the brand."

> "The DESIGN.md format is at version alpha."

## Connexions identifiées

Le mécanisme YAML+prose de DESIGN.md est la réponse la plus directe au problème identifié dans [[readable-vs-usable-token]] : les tokens sont machine-readable (le build pipeline compile) mais pas agent-usable (l'agent ne sait pas pourquoi choisir `tertiary` plutôt que `primary`). La prose DESIGN.md encode ce *pourquoi* de façon structurée et réutilisable.

La CLI `lint` avec vérification WCAG AA s'inscrit dans la problématique de [[accessibilite-continue]] — la conformité est vérifiable dès la définition des tokens, avant toute implémentation.

La CLI `export --format dtcg` crée un pont de DESIGN.md vers le format W3C DTCG ([[dtcg-annotation-schema]]), potentiellement un point de convergence entre les deux écosystèmes.

La référence aux token references `{colors.primary}` comme mécanisme de composition s'articule avec [[intent-token]] : les références sémantiques (plutôt que les valeurs brutes) permettent aux composants de pointer vers l'intent plutôt que vers la valeur.

## Rapport avec DSDS

DESIGN.md et DSDS ([[dsds-format]]) opèrent à des niveaux distincts. DESIGN.md couvre l'identité visuelle (tokens couleur, typo, espacement, composants visuels simples). DSDS couvre la documentation comportementale (API, variants, states, patterns, governance). Ils sont complémentaires et non concurrents — un système mature pourrait embarquer les deux.

La divergence est de philosophie de format : DESIGN.md est un fichier par projet (une seule identité visuelle), DSDS est un fichier par entité (un composant, un token group, un pattern). DESIGN.md est simple à adopter — un seul fichier, une CLI npm. DSDS est plus exhaustif mais plus complexe.
