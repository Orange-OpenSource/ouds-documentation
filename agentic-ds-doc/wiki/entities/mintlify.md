---
type: entity
tags: [outil, documentation, hébergement, git, mdx, deploy]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)"
related:
  - "[pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)"
  - "[documentation-lag](../concepts/documentation-lag.md)"
  - "[romina-kavcic](romina-kavcic.md)"
---

## Mintlify

Mintlify (mintlify.com) est une plateforme d'hébergement de documentation qui transforme des fichiers Markdown/MDX en sites de documentation consultables et stylisés. [romina-kavcic](romina-kavcic.md) la décrit comme "Vercel, but specifically for documentation" ([how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)).

## Fonctionnement

Les fichiers `.mdx` vivent dans un dépôt Git. Mintlify se connecte au dépôt via une GitHub App, surveille les pushs, et reconstruit et déploie le site de documentation automatiquement à chaque commit — délai de 2 à 3 minutes. Chaque projet reçoit un sous-domaine (`your-project.mintlify.app`) sur le plan gratuit. La configuration se fait via un fichier `mint.json`.

## Rôle dans le pipeline automatisé

Dans l'architecture [pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md), Mintlify est la couche de sortie : elle reçoit les fichiers `.mdx` mis à jour par Claude Code (screenshots synchronisés depuis Figma, specs actualisées, exemples régénérés), les déploie automatiquement quand les PR sont mergées, et garantit que le site de documentation reflète toujours l'état du dépôt Git. C'est la connexion entre le pipeline d'automatisation et la documentation accessible aux équipes.

## Lien avec d'autres outils

Mintlify joue dans l'espace que Storybook occupe parfois — la documentation des composants accessible aux équipes — mais avec un focus sur le contenu éditorial (guidelines, quand utiliser, accessibilité, exemples) plutôt que sur les démonstrations interactives de composants. Elle s'intègre dans l'écosystème MCP de [romina-kavcic](romina-kavcic.md) aux côtés de Figma, GitHub, Storybook, Chromatic, Notion.
