---
type: entity
tags: [personne, design-system, ia, figma, markdown, gouvernance]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)"
related:
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[concevoir-les-conditions](../concepts/concevoir-les-conditions.md)"
  - "[into-design-systems-conference](into-design-systems-conference.md)"
---

## Laura Fehre

Laura Fehre est Designer Advocate chez Figma. Elle est intervenue à l'AI Design Systems Conference 2026 d'Into Design Systems sur le thème du Markdown, des scripts et de la traduction cross-platform de design systems.

Son apport principal est une mise en garde empirique qui crée une tension directe avec la thèse des contraintes exécutables développée dans le reste du corpus : "Guidelines are not laws. Writing more rules into a guideline file doesn't control the outcome. In nearly 100% of cases the prompt will win over the guidelines." ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)). Cette observation ne concerne pas les linters ou les auditeurs de tokens (registre de [cristian-morales-achiardi](cristian-morales-achiardi.md)), mais les fichiers de guidelines en markdown injectés dans les règles "always-on" — ce que [diana-wolosin](diana-wolosin.md) appelle les Rules dans son architecture plugin. Voir la tension formalisée dans [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md).

Sa deuxième contribution pratique porte sur la structuration des fichiers de contexte : un fichier markdown monolithique surcharge la fenêtre de contexte et casse les tâches. La règle qu'elle pose — "split into multiple smaller files" — est une déclinaison pratique du principe de progressive disclosure of context.

Son expérience documentée : traduction de l'output de Figma Make (React, Tailwind, shadcn, Radix) en SwiftUI pour un clone de l'app Notes d'Apple, via un fichier de mapping des composants (Radix → HIG). Cursor a parsé les Apple Human Interface Guidelines depuis une URL, produit des fichiers markdown structurés, et Figma Make a utilisé ces fichiers pour guider la génération SwiftUI. C'est une instance concrète de "DS comme source de contexte cross-platform" : un mapping explicite entre deux systèmes permet à l'IA de traverser la frontière technologique sans perte sémantique.

Sa formulation du rôle du Markdown : "Markdown isn't about formatting. It's about communication. It's about making your intent visible and building something that both humans and machines can actually agree on."
