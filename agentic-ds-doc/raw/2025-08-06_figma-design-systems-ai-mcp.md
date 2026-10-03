---
source_url: https://www.figma.com/blog/design-systems-ai-mcp/
author: Ana Boyer (Figma, Designer Advocate)
published: 2025-08-06
ingested: 2026-07-16
---

# Design systems and AI: Why MCP servers are the unlock

Source brute — contenu issu du blog Figma (billet officiel).

## Résumé du contenu

Paired with MCP servers, design systems become a productivity coefficient for AI-powered workflows, ensuring that AI agents produce output that's relevant and on brand.

Quand les agents IA ont le contexte de design depuis Figma, ils rendent le design system plus efficace — ce qui produit un meilleur output de code. Le Figma MCP server apporte du contexte (styles, variables, variable code syntax, Code Connect) à l'IDE.

### Deux statistiques clés (Figma AI report 2025)
- 68 % des développeurs utilisent l'IA pour écrire du code.
- Seulement 32 % des designers et développeurs disent faire confiance ("trust") à l'output généré.

### Ce que le MCP server apporte quand il a du contexte design system
- Réutilisation des composants et patterns existants (réduction de la duplication)
- Application automatique des design tokens (alignement marque/accessibilité)
- Code de départ de haute qualité pour les développeurs
- Raccourcissement des boucles de feedback entre design et engineering

### Génération automatique de règles ("automated design system rule generation")
Le MCP server peut scanner la codebase et produire un fichier de règles structuré : définitions de tokens, bibliothèques de composants, hiérarchies de style, conventions de nommage. Ce fichier sert de guide système pour l'agent, réduisant l'ambiguïté et garantissant que le code généré respecte les standards de l'équipe.

### Trois usages documentés pour les équipes design system
1. **Générer du code de composant aligné avec les standards** : combine le contexte MCP d'un nouveau design de composant avec le code des composants existants pour produire un nouveau composant cohérent ; génère du code dans le langage/framework réellement utilisé par l'équipe (pas seulement React/Tailwind par défaut).
2. **Automatiser le travail sur les design tokens** : identifie où appliquer ou introduire des tokens ; s'assure que les nouveaux tokens respectent les standards déjà définis ; aide à écrire des scripts/automations via le plugin API et la REST API.
3. **Auditer et améliorer l'alignement design/code** : audite l'usage des tokens dans le code vs le design sélectionné (et inversement) ; signale les noms de layers à améliorer pour l'alignement Figma/code ; suggère des améliorations de props Figma pour un meilleur alignement.

### Annotations
Les annotations (accessibilité, comportement d'interaction, contenu) sont un contexte additionnel que le Figma MCP server transmet aux agents — cette information se reflète dans le code généré ("design-informed codegen").
