---
type: synthesis
tags: [audit, design-tokens, ouds, ai-readiness, tokenator]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[ouds-tokenator-main-fm-tokens-2.6.0-early-access]]"
related:
  - "[2026-06-19_audit-ai-readiness-ouds-documentation](../questions/2026-06-19_audit-ai-readiness-ouds-documentation.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
---

# Audit AI-Readiness — Tokens OUDS Tokenator 2.6.0 Early Access

> Audit fondé sur l'inspection directe du dossier `ouds-tokenator-main-fm-tokens-2.6.0-early-access-tokens`. Prend en compte les conclusions de [2026-06-19_audit-ai-readiness-ouds-documentation](../questions/2026-06-19_audit-ai-readiness-ouds-documentation.md) et les approfondit sur la totalité du corpus token.

---

## Périmètre et inventaire

Le dossier expose **12 fichiers JSON** répartis en 5 couches architecturales. Le format utilisé est DTCG-aligné (W3C Design Token Community Group), avec les champs `$value`, `$type`, `$description`.

| Fichier | Tokens | Alias | Raw | Desc |
|---|---|---|---|---|
| `Core-OUDS/Core tokens.Raw value` | 374 | 0 | 374 | 0 |
| `Core-Orange/Core tokens.Raw value` | 80 | 0 | 80 | 0 |
| `Core-Sosh/Core tokens.Raw value` | 131 | 0 | 131 | 4* |
| `Core-Wireframe/Core tokens.Raw value` | 139 | 0 | 139 | 0 |
| `Android/Core tokens.Raw value` | 7 | 0 | 7 | 0 |
| `Android/System tokens.value` | 103 | 102 | 1 | 0 |
| `Brands/Brands.Orange` | 1 883 | 1 745 | 138 | 2* |
| `Brands/Brands.Orange Compact` | 1 883 | 1 738 | 145 | 2* |
| `Brands/Brands.Sosh` | 1 883 | 1 769 | 114 | 2* |
| `Brands/Brands.Wireframe` | 1 883 | 1 764 | 119 | 2* |
| `Brands/Orange` | 175 | 169 | 6 | 0 |
| `Core-OUDS/Comp changelog` | 37 | 0 | 37 | 0 |
| **TOTAL** | **8 578** | **7 287** | **1 291** | **12 (0,1 %)** |

*\* Les 4 descriptions dans Core-Sosh sont "Test for support Figma" (test interne, non opérationnel). Les 2 descriptions dans chaque fichier Brands sont : une de test ("Test for support Figma") et une seule description fonctionnelle (`ouds.brand` : "Specific tokens for components requiring a variant depending on the brand."). Aucune description sémantique réelle n'existe dans le corpus.*

---

## Architecture des couches

Le corpus suit une chaîne de résolution en trois niveaux :

**Couche 1 — Core Raw** (`Core-OUDS`, `Core-Orange`, `Core-Sosh`, `Core-Wireframe`, `Android/Core`). Valeurs primitives brutes : couleurs hex, dimensions en pixels, familles de polices. Aucun alias. C'est la source de vérité de bas niveau.

**Couche 2 — Repository / Brand Semantic** (sections `color.1f525_repository`, `font.family.system` dans les fichiers Brands). Palette intermédiaire qui mappe les primitives de la couche 1 vers des noms sémantiques de marque. La différentiation inter-marque s'opère ici : Orange → `core-orange.color.orange.550`, Sosh → `core-sosh.color.raspberry.500` pour le même token `ouds.color.1f525_repository.primary.medium`.

**Couche 3 — Semantic Brand Tokens + Component Tokens** (fichiers `Brands/Brands.*`). 1 883 tokens par marque, dont 92 % sont des alias vers les couches précédentes. Couvre les couleurs sémantiques (`ouds.color.bg.primary-light`), les dimensions (`ouds.space.*`, `ouds.size.*`), la typographie, et les tokens de composants (`ouds.1f4a0_action.button.*`, `ouds.1f4a0_control.*`, etc.).

La profondeur de résolution mesurée est de 1 à 3 sauts, répartis équitablement (547 tokens à 1 saut, 610 à 2, 588 à 3). Un seul alias non résolu a été détecté : `ouds.1f4a0_content-display.🚧_legal-notice.space.padding-inline.content` pointe vers `{ouds.grid.margin}` qui n'existe pas dans le corpus exposé.

---

## Catégories de tokens (Brands.Orange — référence)

Les 1 883 tokens de la couche Brand se répartissent en 19 catégories :

| Catégorie | Tokens | Nature |
|---|---|---|
| `color` | 392 | Couleurs sémantiques + palette repository |
| `1f4a0_action` | 236 | Tokens composant (button, FAB, expand-button) |
| `1f4a0_control` | 253 | Tokens composant (chip, checkbox, inputs, switch) |
| `1f4a0_navigation` | 183 | Tokens composant (link, breadcrumb, tabs) |
| `font` | 177 | Typographie (famille, poids, taille, interligne) |
| `size` | 134 | Tailles (icônes, assets) |
| `space` | 94 | Espacements |
| `grid` | 85 | Grille responsive |
| `1f4a0_content-display` | 92 | Tokens composant (bullet list, legal notice) |
| `1f4a0_indicator` | 73 | Tokens composant (badge, skeleton, tag) |
| `1f4a0_dialog` | 53 | Tokens composant (alert-message, inline-alert) |
| `elevation` | 35 | Ombres et niveaux d'élévation |
| `dimension` | 27 | Dimensions génériques |
| `border` | 16 | Rayons et largeurs de bordure |
| `opacity` | 8 | Niveaux d'opacité |
| `1f4a0_visual-assets` | 17 | Assets visuels (avatars, illustrations) |
| `1f4a0_foundation` | 4 | Fondations (dark mode flag) |
| `1f4a0_layout` | 1 | Layout (divider) |
| `effect` | 1 | Effets visuels |

En parallèle, `Brands/Orange` expose 175 tokens spécifiques à Orange dans la catégorie `1f4ca_dataviz` (dataviz : gridlines, highlights, séries de couleurs), absents des fichiers `Brands.Orange.*`. Ce fichier a une relation floue avec `Brands.Orange.tokens.json` — il semble être un fichier complémentaire pour la dataviz Orange, non intégré dans la structure principale.

---

## Analyse des conventions de nommage

### Points positifs

Le schéma de nommage est cohérent et sémantique sur les tokens fondamentaux. La séparation `light`/`dark` par suffixe (`ouds.color.bg.primary-light` / `ouds.color.bg.primary-dark`) est systématique et couvre 794 tokens — ce qui rend le mode couleur explicite dans le nom lui-même, sans ambiguïté pour un agent.

Les états d'interaction sont nommés de façon uniforme : `enabled`, `hover`, `pressed`, `focus`, `loading`, `disabled` — 90 à 98 tokens par état. Un agent peut inférer la sémantique des états depuis les noms sans documentation supplémentaire.

La différentiation inter-marque est propre : les 277 tokens qui diffèrent entre Orange et Sosh varient uniquement dans leur alias de résolution (ex. `{core-orange.color.orange.550}` vs `{core-sosh.color.raspberry.500}`), pas dans la structure. L'architecture multi-brand est donc saine pour un agent qui reçoit explicitement le contexte de marque.

### Problèmes critiques

**Emojis structurels dans les noms de tokens.** Trois types d'emojis sont utilisés comme marqueurs sémantiques dans les noms de tokens :

- `🔥` (1F525, écrit `1f525` en ASCII) : préfixe la couche "repository" des couleurs (`ouds.color.1f525_repository.*`). 110 tokens affectés.
- `🏠` (1F4A0, écrit `1f4a0`) : préfixe toutes les catégories de composants (`ouds.1f4a0_action.*`, `ouds.1f4a0_control.*`, etc.). 926 tokens affectés.
- `📈` (1F4CA, écrit `1f4ca`) : préfixe la catégorie dataviz dans `Orange.tokens.json`. 175 tokens affectés.
- `📄` (1F4C4) : apparaît dans 8 tokens de navigation.
- `🚧` : marqueur de travail en cours (WIP). 201 tokens affectés — soit 10,7 % du total Brand.
- `🚫` : marqueur "interdit / non applicable". 7 tokens affectés.

Les emojis comme `🚧` et `🚫` ont une sémantique de gouvernance (WIP, deprecated) mais sont encodés dans les noms de tokens eux-mêmes plutôt que dans des métadonnées dédiées. Pour un agent, un token nommé `ouds.1f4a0_navigation.🚧_tabs.color.bg.selected.enabled-light` est ambigu : est-il utilisable ? temporaire ? à ignorer ? La réponse est dans l'emoji, pas dans un champ `status` lisible programmatiquement.

**Sous-couche repository non abstraite.** Le nom `ouds.color.1f525_repository.primary.medium` expose l'implémentation interne (le préfixe emoji-encoded `1f525`) dans un nom supposément sémantique. Un token sémantique devrait masquer la couche intermédiaire, pas la révéler.

---

## Tableau de maturité AI-Readiness

| Dimension | Score | Verdict |
|---|---|---|
| Format standard (DTCG / W3C) | ✅ | `$value`, `$type`, `$description` présents |
| Structure en couches | ✅ | Core → Repository → Semantic → Component |
| Résolution d'alias | ✅ | 1-3 sauts, 1 seul alias non résolu |
| Différentiation multi-brand | ✅ | 277 tokens différenciés par alias, architecture saine |
| Séparation light/dark | ✅ | Systématique par suffixe |
| États d'interaction | ✅ | Nomenclature uniforme |
| Versioning composants | ✅ | Comp changelog présent (37 versions) |
| Descriptions sémantiques | ❌ | 0,1 % de coverage — 1 description fonctionnelle réelle |
| Nommage sans emojis | ❌ | 201 tokens WIP (🚧), 7 forbidden (🚫), 110+ avec préfixe emoji |
| Tokens WIP isolés | ❌ | 201 tokens en production avec marqueur de draft |
| Intent / selectionCriteria | ❌ | Absent sur tous les tokens composants |
| AGENTS.md / fichier contexte | ❌ | Absent |
| Alias non résolu | ⚠️ | 1 alias cassé (`ouds.grid.margin`) |
| Relation Orange.tokens.json | ⚠️ | Rôle ambigu vis-à-vis de Brands.Orange |

**Score global : 1-2 / 4** — identique au corpus précédent. La bonne nouvelle est que l'architecture est solide. La mauvaise est que la surface lisible par un agent reste quasi-nulle.

---

## Comparaison avec l'audit précédent

L'audit [2026-06-19_audit-ai-readiness-ouds-documentation](../questions/2026-06-19_audit-ai-readiness-ouds-documentation.md) portait sur un export GitHub avec un dossier `tokens/jsonl-ai/` (64 fichiers, format différent). Ce corpus Tokenator 2.6.0 est une source Figma native. Les deux partagent le même gap fondamental — champs `description` vides — mais ce corpus présente des problèmes supplémentaires absents du précédent : emojis dans les noms, tokens WIP non isolés, et une relation de fichiers ambiguë.

Le point positif distinct de ce corpus : l'architecture multi-brand est plus explicite et le versioning des composants est présent (Comp changelog).

---

## Recommandations priorisées

**Priorité 1 — Remplir les descriptions sur les tokens composants.** Les 926 tokens de composants (`1f4a0_action`, `1f4a0_control`, `1f4a0_navigation`, etc.) sont les plus stratégiques : ce sont ceux qu'un agent de génération UI consulte pour choisir la bonne valeur au bon endroit. Un champ `$description` minimal doit indiquer le composant cible, la propriété CSS correspondante, et le contexte d'usage. Format suggéré : `"Couleur de fond du bouton brand en état enabled, mode clair. Utiliser pour les actions primaires sur fond neutre."` Une session assistée couvre une catégorie entière.

**Priorité 2 — Éliminer les emojis des noms de tokens ou les migrer en métadonnées.** Les préfixes `1f525`, `1f4a0`, `1f4ca` doivent devenir des segments purement textuels (`repository`, `component`, `dataviz`). Les marqueurs `🚧` et `🚫` doivent migrer vers un champ `$status: "wip" | "deprecated"` dans le frontmatter du token. Sans cette migration, tout outillage qui parse les noms de tokens (LLM, linter, générateur de code) reçoit du bruit non filtrable.

**Priorité 3 — Résoudre l'alias cassé et clarifier Orange.tokens.json.** L'alias `{ouds.grid.margin}` est rompu et produira une erreur silencieuse dans tout pipeline de résolution. `Brands/Orange.tokens.json` doit être documenté : est-ce un fichier complémentaire pour la dataviz, un fichier legacy, ou une alternative à `Brands.Orange.tokens.json` ? L'ambiguïté de rôle est une source d'erreur pour tout agent qui tente de charger le corpus.

**Priorité 4 — Ajouter un fichier AGENTS.md à la racine du corpus.** Ce fichier doit décrire : la structure des couches, l'ordre de résolution des alias, la convention `light`/`dark`, la signification des préfixes de catégories, et les tokens WIP à ignorer. Sans ce fichier, un agent qui découvre le corpus à froid ne peut pas inférer les règles implicites de l'architecture.
