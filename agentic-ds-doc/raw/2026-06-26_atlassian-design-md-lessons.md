---
source_url: https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice
ingested: 2026-06-26
slug: atlassian-design-md-lessons
auteurs: Kylor Hall, Andrew Campbell
date_publication: 2026-06-15
---

# Atlassian's DESIGN.md is here: what we learned testing portable design context in practice

Kylor Hall (Principal Prompt Engineer) et Andrew Campbell (Senior Design Technologist), Atlassian — 15 juin 2026.

## Contexte

Atlassian a une infrastructure IA design system mature : ADS MCP server, AI skills (structured content pipeline), lint rules. Quand DESIGN.md est sorti, ils ont généré leur propre fichier depuis la même pipeline qui alimente leur MCP, puis ont benchmarké les deux approches sur une tâche de production.

## Benchmark : résultats bruts

Tâche : produire un écran de login utilisateur.

| Approche | Contexte DS dispo | Tokens moyens | Temps moyen | Turns moyens |
|---|---|---|---|---|
| No context | ~5% | 4,20M | 6m19s | 43 |
| ADS MCP | ~80% | 3,75M | 5m1s | 35,1 |
| ADS skill | ~80% | 4,43M | 5m23s | 36 |
| DESIGN.md | ~30% | 7,21M | 6m46s | 45,3 |

DESIGN.md : 92% plus de tokens que le MCP, 2,7x plus de variance entre les runs, plus lent que le MCP, presque aussi lent que sans contexte.

## Les trois limites structurelles de DESIGN.md

**Limitation #1 — Tout est chargé d'un coup, pas on-demand.**
Un MCP charge le contexte à la demande (tool call ads_plan → contexte pour ce composant uniquement). DESIGN.md charge tout d'un coup, dès le début. Pour leur système de 2,5 MB de contenu (guided on-demand), le fichier DESIGN.md résultant est de 80 KB (~19 800 tokens LLM). Plus le fichier grossit, plus la troncature du contexte survient tôt.

**Limitation #2 — La portabilité nécessite de couper.**
Pour tenir dans la taille acceptable, Atlassian a dû éliminer : la majorité des guidelines des 50+ composants, une grande partie de la documentation des fondations, plusieurs design tokens peu utilisés. 30% du contexte disponible vs 80% avec le MCP.

**Limitation #3 — Spec for reimplementing, not guide for using.**
DESIGN.md est une spec pour *réimplémenter* le design system depuis zéro ("intent, not full details"). Dans une codebase de production, ce qu'on veut, c'est qu'un agent importe et utilise les composants existants, pas qu'il les recrée. En testant DESIGN.md, les agents recréaient systématiquement les composants ADS plutôt que de les importer.

Exemple du problème :
```
# Ce que DESIGN.md donne (spec pour réimplémenter)
button-default:
  backgroundColor: '{colors.background-neutral-subtle}'
  ...
## Button: "use {rounded-medium} token to maintain a soft, organic feel..."
```
vs
```
# Ce qu'un guide for using devrait donner
import Button from '@atlaskit/button';
<Button appearance="primary" spacing="compact" />
```

## Où DESIGN.md est réellement utile

Quatre cas d'usage légitimes identifiés par Atlassian :
1. **Direction artistique haut niveau** : encodage du feeling et de l'intent visuel si pas déjà documenté.
2. **Prototypage rapide dans des environnements inconnus** : blue-sky prototyping ou test d'un nouvel outil sans configurer tout le stack.
3. **Interopérabilité avec les design tools** : certains outils IA assemblent l'UI en customisant des composants pré-construits — DESIGN.md fournit exactement le bon niveau de guidance.
4. **Customer theming for adaptive UIs** : si votre produit génère des interfaces dynamiques (dashboards, rapports), DESIGN.md permet aux clients de décrire leur marque pour que les outputs générés reflètent leur identité, pas la vôtre.

Le point commun de ces cas : génération d'UI dans un environnement où les outputs existants du design system ne sont pas disponibles ou pas praticables.

## Ce qu'ils ont publié

DESIGN.md Atlassian disponible à atlassian.design/DESIGN.md.
Diverge du standard sur quelques points : propriétés non-standard pour le rendu des composants, dark mode variant séparé (atlassian.design/DESIGN.short.md).

## Test préalable : démo Team '26

Premier test : keynote demo Team '26 (Anaheim), Figma Make générant des dashboards personnalisés avec le Teamwork Graph. Sans MCP interne disponible, DESIGN.md a produit une UI "recognizably Atlassian" vs le "slop" générique sans contexte. Succès pour le cas de prototypage.
