---
type: source
tags: [design-system, ia, open-source, mcp, cli, react, meta, agents, agentic, ground-up]
created: 2026-06-29
updated: 2026-06-29
sources: []
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[protocole-pas-produit](../concepts/protocole-pas-produit.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[design-md-format](../concepts/design-md-format.md)"
---

## Introducing Astryx by Meta: an open source design system built for how we build now

**URL** : https://astryx.atmeta.com/blog/introducing-astryx
**Auteur** : Meta
**Date** : 18 juin 2026
**Licence** : MIT (Beta)

## Thèse principale

Astryx est le premier DS majeur conçu **ground-up pour être AI-operable** — non pas un système existant retrofitté pour les agents, mais une architecture pensée dès l'origine pour la double audience humains/agents. "We have to rethink how design systems are structured and the role that they play."

## Thèses secondaires

**"AI-operable by design" vs retrofitting.** La distinction posée explicitement : "Astryx was built ground-up to be AI-operable, opposed to retrofitting existing design systems to play nicely with agent behaviors." C'est une reformulation du problème de lisibilité machine — la solution n'est pas d'adapter, c'est de repenser.

**Le JSON manifest comme OpenAPI du CLI.** `npx astryx manifest --json` retourne une spec complète de chaque commande, argument, flag et type de réponse. "The same kind of structured specification that the backend world has had in OpenAPI for a decade, now applied to a frontend design system for the first time." Les agents lisent un payload structuré au lieu de parser du texte `--help`.

**Le MCP comme API agentique.** Le MCP server Astryx est compatible Cursor, Claude Code, GitHub Copilot. Les agents scaffoldent, naviguent et documentent via la même API structurée qu'un développeur humain utiliserait.

**Theming via CSS variable cascade.** Les 10 thèmes (neutral, daily, butter, chocolate, matcha, stone, gothic, brutalist, y2k, default) s'appliquent en changeant des CSS variables — le code composant ne change jamais. Même mécanique que le customer theming identifié dans [design-md-format](../concepts/design-md-format.md).

## Citations clés (≤ 15 mots)

> "Astryx was built ground-up to be AI-operable."

> "Design systems have historically been designed for human consumption."

> "An open source design system built for how we build in this new world."

## Données factuelles

- 8 ans d'usage interne Meta (Facebook, Instagram, WhatsApp, Threads)
- 13 000+ applications internes
- 150+ composants (site docs) / 90+ (repo GitHub)
- 10 thèmes ready-made, MIT, Beta depuis juin 2026
- StyleX : CSS compile-time, atomic, statique — même moteur que Figma et Snowflake

## Comparatif agent tooling (vs shadcn/ui, MUI)

| Système | Agent tooling |
|---|---|
| Astryx | CLI + MCP server + JSON manifest |
| shadcn/ui | CLI pour ajouter des composants |
| MUI | Aucun |

## Connexions identifiées

Astryx concrétise la thèse de [protocole-pas-produit](../concepts/protocole-pas-produit.md) (Kavcic) : l'infrastructure de distribution prime sur les fonctionnalités. Le MCP + CLI + manifest JSON est l'infrastructure ; les composants sont le contenu.

La distinction "AI-operable vs retrofitted" est une nouvelle entrée dans [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) : il ne s'agit plus seulement de documenter pour la machine, mais de concevoir l'architecture du système pour qu'elle soit nativement lisible.

Le JSON manifest répond au problème documenté dans [ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md) (l'agent lit le fichier sans contexte) par une solution d'infrastructure : donner à l'agent une spec formelle de ce qu'il peut faire, au format qu'il sait lire.
