---
type: synthesis
tags: [analyse, architecture, design-tokens, ouds, robustesse, maintenabilite, debug]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[2026-07-06_audit-tokens-tokenator-2.6.0]]"
related:
  - "[[2026-07-06_recommandations-tokens-tokenator-2.6.0]]"
  - "[[2026-06-19_audit-ai-readiness-ouds-documentation]]"
---

# Analyse architecturale — Tokens OUDS Tokenator 2.6.0

> Analyse fondée sur inspection programmatique de l'intégralité des 8 578 tokens du corpus. Couvre : pertinence du modèle, robustesse des références, debuggabilité, maintenabilité, scalabilité. Distincte de l'audit AI-readiness — ici l'angle est l'ingénierie du système de tokens lui-même.

---

## Verdict général

L'architecture est **structurellement saine mais opérationnellement fragile**. Les fondations sont bonnes : le modèle en couches est cohérent, les références sont intègres, la parité inter-marque est parfaite. Mais deux problèmes critiques et plusieurs problèmes secondaires créent une fragilité silencieuse — des états qui passent en CI sans erreur mais produisent des comportements incorrects en production.

---

## Ce qui fonctionne bien

### Intégrité référentielle

Zéro alias circulaire sur l'ensemble du corpus. Zéro mismatch de type entre les quatre brands (Orange, Orange Compact, Sosh, Wireframe) pour le même token. Les 1 883 tokens sémantiques existent dans les quatre brand files sans exception. C'est un résultat remarquable pour un corpus de cette taille et indique une discipline de génération outillée (Tokenator), pas manuelle.

La profondeur de résolution est bornée à 3 sauts maximum, répartis quasi-uniformément (1 saut : 547 tokens, 2 sauts : 610, 3 sauts : 588). Ce plafond est raisonnable et délibéré.

### Parité light/dark

370 tokens couleur en variante `-light` et 370 en variante `-dark`, sans aucun token non apparié. Pour un système qui gère le dark mode, c'est une propriété critique et elle est parfaitement respectée. Aucun token couleur sémantique n'est "orphelin" de sa variante.

### Différentiation Orange Compact

Le fichier `Brands.Orange Compact` diffère de `Brands.Orange` sur exactement 242 tokens, concentrés sur la typographie (90 tokens), les tailles (64), les composants (contrôles, dialog, indicator) et la grille (18). Le profil de différence est cohérent avec ce qu'on attend d'une variante compacte : réduction des tailles d'affichage, pas de changement de couleurs ou de comportements. L'architecture multi-brand fonctionne ici comme prévu.

### Format DTCG

L'usage du format W3C Design Token Community Group (`$value`, `$type`, `$description`) est le bon choix. Il est interopérable avec Style Dictionary, Theo, Supernova, et la majorité des pipelines de build modernes. Il supporte les champs d'extension arbitraires, ce qui facilite l'ajout futur de `$status`, `$aiHints`, etc.

### Versioning des composants

Le fichier `Comp changelog.tokens.json` trace les versions de 37 composants (button en 3.2.0, checkbox en 2.4.0, FAB en 0.0.0, etc.). C'est un signal de maturité rare dans les design systems. Il permet de corréler des régressions avec des bumps de version et d'informer les consommateurs des composants sur la stabilité attendue.

---

## Problèmes critiques

### Mélange de formats de couleur `#RRGGBB` et `#AARRGGBB`

C'est le problème le plus sévère du corpus. Deux formats coexistent dans les fichiers Core :

- `#RRGGBB` (7 caractères) : 141 tokens dans Core-OUDS. Format CSS standard.
- `#AARRGGBB` (9 caractères) : 61 tokens dans Core-OUDS + 71 tokens raw dans Brands.Orange. Format Android ARGB.

Ces deux formats sont **incompatibles et silencieusement incorrects** selon le consommateur. En CSS, `#AARRGGBB` n'est pas un format valide — la plupart des navigateurs l'ignorent ou le rejettent sans erreur explicite. En Android XML, `#RRGGBB` est valide mais interprété différemment que `#AARRGGBB`. Aucun linter standard ne détecte cette incohérence à la compilation.

La conséquence pratique : un token comme `core-ouds.color.functional.white.with-opacity` qui vaut `#ffffffff` (blanc opaque en ARGB) et un token `core-ouds.color.functional.white` qui vaut `#ffffff` (blanc en RGB) ont la même valeur visuelle, mais un pipeline CSS qui tente d'utiliser le premier comme valeur de `color` ou `background` obtiendra un comportement indéfini selon le navigateur.

**Détection recommandée** : ajouter un linter qui rejette tout token de type `color` dont la valeur raw est une chaîne hex de 9 caractères dans un contexte de build web.

### 70 couleurs `#ff000000` dans le repository — placeholders silencieux

70 tokens dans `ouds.color.1f525_repository.*` ont pour valeur `#ff000000`. En ARGB (Android), cette valeur signifie "noir opaque". En CSS (si ce format était valide), ce serait du noir transparent. Dans le contexte du repository, qui est la palette intermédiaire entre les primitives Core et les tokens sémantiques, ce motif indique très probablement des **slots de palette non encore attribués** pour la brand Orange — des positions dans l'échelle chromatique (primary.lowest, primary.lower, secondary.*, tertiary.*) qui n'ont pas de valeur Brand définie et ont été remplies par un placeholder.

Le problème : rien ne le signale. Ces tokens passent en CI, sont exportés dans le build, et peuvent se retrouver appliqués silencieusement comme "noir" dans l'interface si un token sémantique les référence. Il n'y a pas de valeur sentinelle explicite (`null`, `"UNDEFINED"`, token de type `$status: "placeholder"`) qui permettrait à un pipeline de les détecter et de lever une erreur.

Les 70 tokens affectés couvrent les échelles primary, secondary et tertiary dans les teintes qui ne correspondent pas à la palette orange de la marque (les teintes orange valides — `primary.low` et `primary.medium` — pointent vers `{core-orange.color.orange.500}` et `{core-orange.color.orange.550}`, les autres sont des #ff000000).

---

## Problèmes de debuggabilité

### Chaîne de résolution invisible

Pour résoudre `ouds.font.family.web.display` jusqu'à sa valeur finale `Helvetica Neue`, un développeur doit ouvrir trois fichiers dans le bon ordre :

1. `Brands.Orange` → `{ouds.font.family.system.web}`
2. `Brands.Orange` → `{core-orange.font.family.brand.default}`
3. `Core-Orange` → `Helvetica Neue`

Sans outillage de résolution intégré (ex. Style Dictionary avec `resolve: true`), cette trace est entièrement manuelle. Le corpus ne fournit aucun fichier de tokens "résolus" (flattened) qui permettrait l'inspection directe. En l'état, déboguer pourquoi une valeur apparaît incorrecte en production nécessite de remonter la chaîne à la main.

### Emojis comme marqueurs de statut

201 tokens WIP (🚧) et 7 tokens "interdits" (🚫) portent leur statut dans le nom. Un pipeline de build qui ne connaît pas cette convention va traiter ces tokens exactement comme des tokens stables. Il n'existe aucun moyen de les exclure de la compilation sans parser les noms de tokens avec une regex unicode — ce qui est une dépendance fragile et non documentée.

### 14 valeurs hardcodées dans les tokens composants

138 tokens raw existent dans `Brands.Orange` (idéalement zéro pour une couche purement sémantique). La majorité (124) est dans `color.1f525_repository` — c'est la palette intermédiaire, acceptable. Mais 14 autres se trouvent dans des tokens de composants : navigation (4), content-display (3), dialog (3), foundation (1), visual-assets (1), plus les méta-tokens `brand` et `version`. Ces hardcodes sont des bombes à retardement : si la valeur doit changer, elle ne sera pas trouvée par une recherche dans les fichiers Core et ne sera pas propagée automatiquement.

---

## Problèmes de maintenabilité

### 206 tokens Core orphelins dans le contexte Orange

454 tokens existent dans les fichiers Core (OUDS + Orange). Seulement 248 sont référencés depuis `Brands.Orange`. 206 sont non référencés, dont la totalité des couleurs décoratives Orange (`core-orange.color.decorative.amber.*`, `core-orange.color.decorative.amethyst.*`, etc. — 9 teintes × ~9 niveaux). Ces tokens peuvent être légitimement utilisés par d'autres brands, par la dataviz (via `Orange.tokens.json`), ou par des composants futurs. Mais sans documentation de leur usage attendu, ils constituent une surface à maintenir dont on ne sait pas si elle est vivante ou morte.

### Quadruplication structurelle des brands

Les quatre fichiers Brand (`Brands.Orange`, `Brands.Orange Compact`, `Brands.Sosh`, `Brands.Wireframe`) partagent une structure identique à 1883 tokens chacun. Tout ajout d'un nouveau token sémantique — un nouvel état d'interaction, un nouveau composant — doit être répercuté dans les quatre fichiers. Tokenator gère probablement cette synchronisation via un export Figma. Mais si le processus d'export est partiel ou si un fichier est édité manuellement, la divergence structurelle est indétectable sans diff outillé.

Le vrai risque est l'introduction future d'un cinquième brand (hypothétique `Brands.Pro`, `Brands.Business`) : il faut garantir que le processus d'export le génère avec exactement la même structure, y compris les tokens WIP et les placeholders #ff000000.

### Surface d'ambiguïté : `Orange.tokens.json` vs `Brands.Orange.tokens.json`

Deux fichiers coexistent pour la brand Orange sans relation documentée entre eux. `Brands.Orange` couvre les 1883 tokens sémantiques et composants. `Orange.tokens.json` couvre 175 tokens de dataviz dans un namespace `orange.*` différent. Un consommateur du corpus qui charge `Brands.Orange` et ignore `Orange.tokens.json` a une brand Orange incomplète. L'inverse est impossible (les 175 tokens de dataviz ne peuvent pas fonctionner sans les tokens sémantiques). Cette dépendance implicite n'est pas documentée.

---

## Pertinence du modèle

L'architecture en trois couches (Core → Repository → Semantic+Component) est le modèle standard et pertinent pour un design system multi-brand. L'alternance entre tokens primitifs (Core), palette intermédiaire (Repository), et tokens d'usage (Semantic) est exactement ce que recommandent les approches Tokens Studio, NDS, et la spec W3C.

La couche Repository (`color.1f525_repository`) joue un rôle crucial souvent absent dans les design systems moins matures : elle isole la spécificité de marque (la teinte primaire orange vs framboise de Sosh) de la sémantique d'usage (couleur d'action, couleur de fond primaire). Cette isolation garantit que changer la teinte primaire d'une marque ne nécessite que de modifier 2-3 tokens Repository, pas des centaines de tokens sémantiques.

La présence de tokens composants dans les Brand files (`1f4a0_action.button.*`, etc.) est un choix architectural qui a du sens : les composants peuvent avoir des valeurs différentes selon la marque. Mais cela ajoute 926 tokens à la surface à maintenir dans chaque brand file, et crée le risque de dérive silencieuse entre brands si un composant est mis à jour dans Orange mais pas dans Sosh.

---

## Scalabilité

Le modèle tient à l'échelle actuelle (4 brands, 41 composants versionnés, 1883 tokens par brand). Il commence à montrer des limites sur deux axes.

En surface de tokens, l'ajout de chaque nouveau composant ajoute N tokens × 4 brands. Le composant le plus dense est `button` avec 155 tokens (états × propriétés × modes). Si le DS s'étend aux patterns (modales, formulaires complets, pages entières), la surface explose sans refactoring vers des tokens plus abstraits.

En chaîne de résolution, le plafond de 3 sauts est sain. Si la couche Repository est étendue (ajout d'une couche "thème" entre Repository et Semantic pour le white-labeling avancé), le risque est de franchir 4-5 sauts, ce qui rend le debug exponentiel et les performances de build dégradées.

---

## Résumé des métriques clés

| Métrique | Valeur | Verdict |
|---|---|---|
| Tokens totaux | 8 578 | — |
| Alias circulaires | 0 | ✅ |
| Alias cassés | 1 | ⚠️ |
| Parité light/dark | 370/370 | ✅ |
| Mismatch de type inter-brand | 0 | ✅ |
| Coverage inter-brand | 1883/1883 | ✅ |
| Formats couleur distincts | 2 (#RRGGBB + #AARRGGBB) | ❌ |
| Placeholders silencieux (#ff000000) | 70 | ❌ |
| Tokens WIP non isolés | 201 | ❌ |
| Tokens core orphelins (contexte Orange) | 206 | ⚠️ |
| Valeurs hardcodées dans les composants | 14 | ⚠️ |
| Profondeur d'alias max | 3 sauts | ✅ |
| Composants versionnés | 37 | ✅ |
| Descriptions fonctionnelles | 1 / 8 578 | ❌ |
