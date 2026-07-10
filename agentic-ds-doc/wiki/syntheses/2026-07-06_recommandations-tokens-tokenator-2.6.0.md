---
type: synthesis
tags: [recommandations, design-tokens, ouds, ai-readiness, tokenator, actions]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[2026-07-06_audit-tokens-tokenator-2.6.0]]"
related:
  - "[[2026-06-19_audit-ai-readiness-ouds-documentation]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[schema-metadata-composant]]"
---

# Recommandations d'actions — Tokens OUDS Tokenator 2.6.0

> Issu de l'audit du 2026-07-06. Score actuel : 1-2/4. Objectif : atteindre 3/4 en 4 chantiers séquencés.
> Chaque action est indépendante mais l'ordre est délibéré : les premières débloquent les suivantes.

---

## P1 — Remplir les descriptions sur les tokens composants

**Impact : critique / Effort : élevé mais mécanisable**

926 tokens de composants (`1f4a0_action`, `1f4a0_control`, `1f4a0_navigation`, `1f4a0_dialog`, `1f4a0_indicator`, `1f4a0_content-display`, `1f4a0_visual-assets`, `1f4a0_foundation`, `1f4a0_layout`) n'ont aucun champ `$description`. C'est la lacune la plus coûteuse pour un agent de génération UI : sans description, il ne peut pas choisir le bon token pour le bon contexte.

**Format cible pour chaque token :**

```json
"$description": "<Composant> — <propriété CSS>. <Contexte d'usage en 1 phrase>. <Contrainte ou exclusion si pertinente>."
```

Exemple :

```json
"ouds.1f4a0_action.button.color.bg.brand.enabled-light": {
  "$type": "color",
  "$value": "{ouds.color.surface.brand.primary-light}",
  "$description": "Button — background-color. Couleur de fond du bouton brand en état actif, mode clair. Utiliser pour les actions primaires sur fond neutre. Ne pas utiliser sur fond coloré (voir ouds.1f4a0_action.button.color.bg.brand-on-colored-bg.*)."
}
```

**Séquence suggérée :**

Traiter catégorie par catégorie dans cet ordre (du plus utilisé au moins utilisé) :

1. `1f4a0_action` — 236 tokens (button, FAB, expand-button)
2. `1f4a0_control` — 253 tokens (chip, checkbox, inputs, switch)
3. `1f4a0_navigation` — 183 tokens (link, breadcrumb, tabs)
4. `1f4a0_indicator` — 73 tokens (badge, skeleton, tag)
5. `1f4a0_dialog` — 53 tokens (alert-message, inline-alert)
6. `1f4a0_content-display` — 92 tokens
7. `1f4a0_visual-assets` — 17 tokens
8. `1f4a0_foundation`, `1f4a0_layout` — 5 tokens

Une session assistée avec un LLM couvre une catégorie entière en partant des noms de tokens (suffisamment sémantiques pour générer des descriptions pertinentes). Valider les descriptions générées sur 10 % des tokens par catégorie avant commit.

**Critère de complétion :** coverage `$description` ≥ 95 % sur les tokens composants.

---

## P2 — Migrer les marqueurs emoji vers des métadonnées structurées

**Impact : élevé / Effort : moyen**

201 tokens portent un marqueur WIP (🚧) et 7 un marqueur "interdit" (🚫) directement dans leur nom. Cette pratique rend impossible toute séparation programmatique entre tokens stables et tokens en cours de conception.

**Action 1 — Introduire un champ `$status` dans le schéma.**

Valeurs proposées : `stable` | `wip` | `deprecated` | `experimental`.

Tous les tokens sans `$status` sont implicitement `stable`. Seuls les tokens non-stables ont besoin du champ.

```json
"ouds.1f4a0_navigation.🚧_tabs.color.bg.selected.enabled-light": {
  "$type": "color",
  "$value": "...",
  "$status": "wip",
  "$description": "..."
}
```

**Action 2 — Renommer les tokens WIP** en retirant le 🚧 du nom une fois le champ `$status` en place. Un token nommé `ouds.1f4a0_navigation.tabs.color.bg.selected.enabled-light` avec `"$status": "wip"` est à la fois lisible et filtrable.

**Action 3 — Traiter les tokens 🚫 (7 tokens dans `navigation.link.color.chevron`).** Ces tokens encodent une contrainte d'inutilisabilité dans leur nom. Les migrer vers `"$status": "deprecated"` avec une `$description` indiquant l'alternative.

**Critère de complétion :** zéro emoji dans les noms de tokens ; champ `$status` présent sur tous les tokens non-stables.

---

## P3 — Clarifier les préfixes de catégorie et la relation des fichiers

**Impact : moyen / Effort : faible**

Deux ambiguïtés bloquent la compréhension du corpus par un agent qui le découvre à froid.

**3a — Préfixes emoji-encoded dans les noms de catégories.**

Les segments `1f525_repository`, `1f4a0_action`, `1f4ca_dataviz` encodent des rôles architecturaux via des codepoints Unicode ASCII-ifiés. Pour un LLM ou un linter, ce sont des chaînes opaques.

Options :
- Renommer proprement : `repository`, `component-action`, `dataviz` (breaking change, nécessite migration outillage).
- Documenter dans AGENTS.md (voir P4) la table de décodage. Effort minimal, effet immédiat pour les agents.

Recommandation : documenter d'abord (P4), renommer lors de la prochaine version majeure.

**3b — Rôle ambigu de `Brands/Orange.tokens.json`.**

Ce fichier expose 175 tokens `orange.color.1f4ca_dataviz.*` absents de `Brands/Brands.Orange.tokens.json`. Il n'est pas clair si ce fichier est : (a) un complément optionnel pour la dataviz, (b) un fichier legacy en cours de migration, ou (c) un fichier destiné à un autre pipeline.

Action : ajouter un commentaire de fichier (champ `$description` à la racine du JSON si le format le permet, sinon un README dans le dossier `Brands/`) expliquant le rôle et les conditions d'inclusion.

**3c — Corriger l'alias cassé.**

`ouds.1f4a0_content-display.🚧_legal-notice.space.padding-inline.content` pointe vers `{ouds.grid.margin}` qui n'existe pas dans le corpus exposé. À corriger ou à marquer `$status: "wip"` en attendant la définition du token manquant.

**Critère de complétion :** zéro alias non résolu ; rôle de chaque fichier documenté.

---

## P4 — Créer un fichier AGENTS.md à la racine du corpus

**Impact : moyen / Effort : faible**

Un agent qui charge le corpus sans contexte ne peut pas inférer : l'ordre de résolution des couches, la convention de nommage light/dark, la signification des préfixes de catégorie, ni quels tokens sont stables.

**Contenu minimal du fichier :**

```markdown
# AGENTS.md — OUDS Token Corpus 2.6.0

## Architecture des couches
1. Core Raw (Core-OUDS, Core-Orange, Core-Sosh, Core-Wireframe) — valeurs primitives
2. Repository / Brand Semantic (dans Brands.*) — palette intermédiaire par marque
3. Semantic + Component (Brands.Orange, Brands.Sosh, etc.) — tokens d'usage

## Résolution des alias
Les alias suivent la notation `{nom.du.token}`. Résolution en 1 à 3 sauts maximum.
Charger les fichiers Core avant les fichiers Brands pour une résolution complète.

## Convention light/dark
Tous les tokens de couleur existent en deux variantes : suffixe `-light` et `-dark`.
Sélectionner la variante selon le mode d'affichage du contexte.

## Préfixes de catégorie
- `1f525_repository` = palette de couleurs intermédiaire (ne pas utiliser directement)
- `1f4a0_*` = tokens de composants (action, control, navigation, dialog, indicator, etc.)
- `1f4ca_dataviz` = tokens spécifiques à la dataviz Orange (fichier Orange.tokens.json)

## Tokens à ignorer
- Préfixe `🚧` dans le nom = token en cours de conception, ne pas utiliser en production
- Préfixe `🚫` dans le nom = token désactivé, ne pas utiliser

## Fichiers par marque
- Brands.Orange + Orange = brand Orange (Orange.tokens.json ajoute la dataviz)
- Brands.Orange Compact = variante compacte de la brand Orange
- Brands.Sosh = brand Sosh
- Brands.Wireframe = wireframing (couleurs neutres)
```

**Critère de complétion :** fichier AGENTS.md présent à la racine, relu par un LLM à froid pour valider qu'il répond aux questions d'un agent naïf.

---

## Récapitulatif

| Priorité | Action | Tokens concernés | Effort | Impact |
|---|---|---|---|---|
| P1 | Remplir `$description` sur les tokens composants | 926 | Élevé | Critique |
| P2 | Migrer emojis WIP/forbidden vers `$status` | 208 | Moyen | Élevé |
| P3 | Clarifier préfixes, fichiers et alias cassé | ~1 | Faible | Moyen |
| P4 | Créer AGENTS.md | — | Faible | Moyen |

L'ordre optimal est P3 → P4 → P2 → P1 si l'objectif est de corriger les problèmes structurels avant d'investir dans le contenu. L'ordre P1 → P2 → P3 → P4 est préférable si l'objectif est de maximiser l'impact AI-readiness le plus vite possible, quitte à refactorer les descriptions après la migration emoji.
