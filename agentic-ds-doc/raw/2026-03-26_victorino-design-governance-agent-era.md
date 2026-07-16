---
source_url: https://victorinollc.com/thinking/design-governance-agent-era
author: Thiago Victorino (Victorino Group, The Thinking Wire)
published: 2026-03-26
ingested: 2026-07-16
---

# Design Systems Just Became AI Governance Infrastructure

Source brute — contenu issu de The Thinking Wire (Victorino Group). Synthétise l'annonce beta du Figma MCP (mars 2026) et l'essai de Wenbin "What Happens to the Design System When AI Changes the Product?" (Medium, mars 2026).

## Thèse centrale

Deux événements de la même semaine de mars 2026 : Figma ouvre son canvas aux agents IA via MCP (écriture, pas seulement lecture). Wenbin publie un essai sur ce qui arrive aux design systems quand l'IA change le produit sous-jacent. Le design system n'est plus un document de référence — c'est une contrainte d'exécution ("runtime constraint").

## Ce que fait concrètement le Figma MCP beta (24 mars 2026)

Ne se limite pas à la lecture : un agent connecté peut créer des frames, placer des composants, définir des propriétés de layout, modifier des designs existants — à l'intérieur de Claude Code, Cursor, VS Code, GitHub Copilot, etc. L'agent produit de vrais artefacts Figma qui vivent dans le fichier, utilisent les composants de l'équipe, référencent ses variables.

Mécanisme de contrainte : avant de créer quoi que ce soit, l'agent lit la bibliothèque de composants existante et construit avec ce qui existe déjà. S'il n'existe que 3 variantes de bouton, l'agent ne peut pas en inventer une quatrième. C'est une gouvernance par architecture, pas par document de politique : les limites sont structurelles.

## Figma Skills comme gouvernance-as-code

Aux côtés du MCP, Figma introduit les "Skills" : des fichiers Markdown qui définissent comment les agents doivent travailler dans Figma. Skill fondationnel : `figma-use`. Extensible avec des skills custom par organisation. Une règle du type "quand tu construis une navigation, utilise toujours le composant NavBar de la librairie core, ne crée jamais d'élément de navigation custom" est une règle de gouvernance exprimée comme instruction agent.

## Les limites honnêtes

Le MCP Figma est en beta. Aucune entreprise ne tourne cela à l'échelle production aujourd'hui. L'écart entre "les agents peuvent écrire dans un fichier Figma" et "les agents produisent de façon fiable du travail de design de qualité production dans les contraintes d'une entreprise" reste significatif.

## Trois implications pour les équipes de gouvernance

1. Les équipes design system doivent avoir une place à la table de gouvernance IA : la bibliothèque de composants devient une surface de contrôle.
2. La complétude du design system devient une question de sécurité : les composants qui n'existent pas dans la librairie sont des composants que l'agent ne peut pas utiliser correctement — il improvisera le reste. La couverture n'est plus un OKR design, c'est une métrique de risque.
3. Un design system incomplet + des agents = décisions non contraintes sur l'interface produit, à l'échelle machine.

## L'échelle d'évolution

Style guide (suggère) → bibliothèque de composants (fournit) → linting (impose) → couche de contrainte pour agents (gouverne). Chaque évolution augmente l'autorité du système. Les design systems passent de la documentation à l'infrastructure à la gouvernance.
