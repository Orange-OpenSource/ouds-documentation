---
type: source
tags: [design-system, ia, mcp, notion, documentation, pipeline, monorepo, typeform, automatisation]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[[fernando-coelho]]"
  - "[[notion-cms-design-system]]"
  - "[[pipeline-multi-destinations]]"
  - "[[pipeline-figma-docs-automatise]]"
  - "[[documentation-lag]]"
  - "[[processus-generation-metadata-echelle]]"
  - "[[lisibilite-machine-design-system]]"
---

## Design System Documentation at Scale: Leveraging AI and Automation

Article de [[fernando-coelho]], Senior Frontend Engineer chez Typeform, publié le 3 octobre 2025. Documente l'architecture de documentation du design system Echo de Typeform : Notion comme CMS, Docusaurus, GitHub Actions, et un MCP server — tous alimentés par le même pipeline de contenu.

## Thèses principales

**Le problème de fragmentation comme point de départ.** Typeform avait trois sources de vérité divergentes : Figma pour les specs de design, Notion pour les guidelines, Storybook pour les exemples de code. Les incohérences entre ces sources créaient de la confusion, ralentissaient le développement et produisaient des erreurs d'implémentation. C'est une instance classique du [[documentation-lag]], avec une couche supplémentaire : la fragmentation affecte des audiences différentes (designers dans Figma, développeurs dans Storybook, tout le monde dans Notion).

**Notion comme CMS accessible.** La solution centrale : choisir Notion — déjà utilisé quotidiennement par toute l'équipe — comme source de vérité principale de la documentation. L'API Notion transforme le contenu en Markdown, qui alimente ensuite plusieurs destinations. L'argument clé : lowering the barrier of entry. N'importe qui dans l'équipe peut contribuer à la documentation sans connaissance technique, depuis un interface familier. Les bases de données Notion permettent en plus d'encoder des métadonnées riches : statut des composants, liens API, thumbnails, relations récursives entre composants.

**Un seul pipeline, trois destinations.** La même transformation Notion → Markdown alimente simultanément : le site de documentation (Docusaurus), le serveur MCP (markdown + tokens + code snippets), et l'environnement Sandbox. Le MCP a donc accès exactement à la même documentation que celle que consultent développeurs et designers — pas une version spéciale, la même.

**Les code snippets comme source de vérité partagée.** Un package dédié de code snippets est consommé par les trois applications (docs, sandbox, MCP). La cohérence entre les exemples dans la documentation et ceux que le MCP suggère est garantie structurellement — pas par synchronisation manuelle.

**L'automatisation avec double revue.** GitHub Actions tourne hebdomadairement (ou sur déclenchement manuel), fetche le contenu Notion mis à jour, et ouvre une PR. Chaque PR requiert la revue d'un ingénieur ET d'un designer avant merge — une gouvernance explicite qui maintient la qualité tout en permettant à n'importe qui de contribuer en amont.

## Ce que cette source apporte au vault

Source datée d'octobre 2025 — antérieure à la majorité du corpus. Elle représente une approche plus accessible et plus centrée sur la **démocratisation de la contribution** que les approches techniques du vault (Morales Achiardi, Wolosin). Sa proposition distinctive : utiliser un outil que l'équipe utilise déjà, plutôt que de construire une infrastructure ad hoc. C'est une instance de [[seeds-vs-trees]] appliquée au choix d'outillage : planter là où le sol est déjà préparé.

Les deux contributions conceptuelles nouvelles : [[notion-cms-design-system]] (Notion comme levier de contribution démocratisée) et [[pipeline-multi-destinations]] (un seul pipeline alimentant docs + MCP + sandbox). La tension principale avec le reste du vault : l'approche Notion produit du Markdown lisible par les humains, pas du JSON structuré pour les agents — ce qui la positionne en bas de la pyramide de lisibilité machine documentée par [[diana-wolosin]] et [[romina-kavcic]].

## Citations clés

"Since our company already extensively uses Notion on a daily basis, it was only natural to leverage it for our documentation needs."

"The same content pipeline that feeds our documentation website also powers our Model Context Protocol server."

"Each PR requires review from both an engineer and a designer, maintaining quality standards while allowing anyone on the team to contribute documentation updates through Notion alone."
