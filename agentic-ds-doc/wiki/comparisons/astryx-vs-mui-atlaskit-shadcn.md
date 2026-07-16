---
type: comparison
tags: [design-system, astryx, mui, shadcn, atlaskit, marche, composition, ia, agents]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[meta-astryx-harsha-sridhar](../sources/meta-astryx-harsha-sridhar.md)"
  - "[meta-astryx-design-system](../sources/meta-astryx-design-system.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[grammaire-composition-composants](../concepts/grammaire-composition-composants.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[protocole-pas-produit](../concepts/protocole-pas-produit.md)"
---

## Astryx vs MUI vs Atlaskit vs Shadcn/ui

Cette comparaison est construite depuis deux sources : la fiche officielle Meta ([meta-astryx-design-system](../sources/meta-astryx-design-system.md)) et l'analyse externe de Harsha Sridhar ([meta-astryx-harsha-sridhar](../sources/meta-astryx-harsha-sridhar.md)). Elle se lit sur deux axes : l'architecture de composition (composants scellés vs ouverts) et l'opérabilité agentique (ce que le système expose aux agents IA).

## Les quatre systèmes

### MUI (Material UI)

MUI est le défaut pragmatique de l'écosystème React. Riche, documenté, largement adopté. Ses deux limites sont architecturalement distinctes. La première est visuelle : les applications construites avec MUI "look like MUI" — l'identité de la librairie transparaît à travers les thèmes personnalisés. La seconde est structurelle : les composants MUI sont majoritairement scellés. "Reaching inside a component often isn't allowed" — une `<Dialog>` est une Dialog, et si la Dialog ne convient pas, les options sont le fork ou le contournement. MUI n'expose pas de building blocks.

Sur l'axe agentique : MUI n'a aucun outillage CLI ou MCP pour les agents. Un agent doit lire la documentation prose pour comprendre comment utiliser le système.

### Atlaskit (Atlassian)

Atlaskit est poli et accessible, construit sur une longue histoire de produits Atlassian. Sa limite principale n'est pas la qualité mais la forme : le système "est shaped hard around Atlassian's product surface." Les décisions de composant, de pattern, de nomenclature reflètent les besoins de Jira, Confluence, Trello — pas nécessairement les besoins d'un projet tiers. L'adopter hors contexte Atlassian signifie se conformer à des décisions qui n'ont pas été prises pour vous.

Sur l'axe agentique : pas d'outillage CLI ou MCP documenté pour les agents.

### Shadcn/ui

Shadcn/ui a "flipped the model" — au lieu de distribuer une librairie, il distribue du code source : les composants sont copiés dans le codebase du projet, possédés, modifiables. Le `Button` qui ne convient pas peut être édité directement. Initialement construit sur Radix UI (primitives headless) + Tailwind, le projet supporte maintenant un écosystème plus large.

Ce modèle résout le problème des composants scellés et du styling lock-in simultanément. Il crée en contrepartie une friction différente : les mises à jour ne sont pas automatiques, et les équipes divergent progressivement des composants copiés. Il n'y a pas de maintien centralisé.

Sur l'axe agentique : Shadcn a un CLI (`npx shadcn add button`) — mais il est conçu pour l'installation, pas pour la discovery de composants par des agents.

### Astryx (Meta)

Astryx occupe l'intersection de Shadcn (philosophie de composition ouverte) et d'une librairie maintenue à l'échelle (160+ composants avec accessibilité intégrée, maintenus par Meta). Il emprunte la philosophie d'exposition des primitives Radix-style — `Dialog.Root`, `Dialog.Overlay`, `Dialog.Content` — tout en livrant un système complet que l'équipe n'a pas à maintenir elle-même.

Sur l'axe styling, il décapsule le moteur (StyleX reste interne) et laisse le choix : CSS vanilla, Tailwind, CSS modules. Les thèmes sont des CSS custom properties, pas une dépendance de build.

Sur l'axe agentique, c'est le différenciateur principal : CLI structuré dont chaque commande retourne un output canonical parseable (`npx astryx component Button`), JSON manifest auto-descriptif de toutes les commandes et flags, serveur MCP compatible Cursor, Claude Code, GitHub Copilot, et un "Quick Start with AI" dans la documentation officielle. Voir [meta-astryx-design-system](../sources/meta-astryx-design-system.md) pour le détail de l'architecture.

## Tableau synthétique

| Critère | MUI | Atlaskit | Shadcn/ui | Astryx |
|---|---|---|---|---|
| Composants accessibles, maintenus | Oui | Oui | Partiel (primitives Radix) | Oui (160+) |
| Composants scellés | Oui | Oui | Non (code source) | Non (primitives exposées) |
| Styling lock-in | Fort | Fort | Aucun | Aucun |
| Identité visuelle imposée | Oui (Material) | Oui (Atlassian) | Non | Non (7 thèmes, CSS vars) |
| CLI pour agents | Non | Non | Partiel (installation) | Oui (discovery + manifest JSON) |
| Serveur MCP | Non | Non | Non | Oui |
| Conçu explicitement pour agents | Non | Non | Non | Oui |

## Ce que la comparaison révèle sur le marché

Avant Astryx, chaque design system était jugé sur deux axes : qualité visuelle et richesse fonctionnelle. Les différenciateurs étaient la beauté du storybook, la complétude des composants, la cohérence du système de tokens.

Sridhar formule l'axe de différenciation qui émerge en 2026 : "how well they compose, how much of their internals they expose, and how legibly they present themselves to both a human and a model." Ce n'est pas un axe de qualité — c'est un axe d'architecture. Un système peut être excellent sur les deux premiers axes historiques et invisibles aux agents ([figma-library-invisible-ai-agents](../sources/figma-library-invisible-ai-agents.md)).

La conséquence pour les équipes DS qui construisent leur propre système : les décisions de composition (scellé vs ouvert) et de styling (couplé vs découplé) ne sont plus seulement des décisions de DX développeur — elles sont des décisions d'opérabilité agentique. Un composant scellé est opaque à l'agent autant qu'au développeur qui veut le modifier.

## ⚡ Tension : maintenabilité vs composabilité

Le modèle Shadcn (copier le code source) maximise la composabilité mais sacrifie la maintenabilité centralisée. Le modèle MUI/Atlaskit maximise la maintenabilité mais sacrifie la composabilité. Astryx revendique les deux simultanément — primitives exposées + maintien Meta — mais ce claim n'est pas encore validé à long terme. Le risque : que l'exposition des primitives crée de la surface d'API à maintenir, et que les breaking changes sur `Dialog.Root` soient plus coûteux que des breaking changes sur `<Dialog>`.
