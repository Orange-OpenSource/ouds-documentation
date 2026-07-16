---
type: source
tags: [design-system, ia, agents, metadata, composants, tokens, figma, pratique, guide]
created: 2026-06-29
updated: 2026-06-29
sources: []
related:
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## Agentic design system: how to build a component library AI agents can actually use

**URL** : https://designproject.io/blog/agentic-design-system/
**Auteur** : Dianne Alter (The Design Project)
**Date** : 7 mai 2026

## Thèse principale

Un design system agentique supprime l'étape d'interprétation humaine — chaque décision ("utilise ça ici", "ne l'utilise jamais là") est écrite dans un fichier metadata structuré parce que l'agent ne peut pas l'inférer. La metadata est le handoff.

## Thèses secondaires

**Trois pilliers d'un composant agentique.** Props (états/variants, mappés 1:1 depuis Figma), Relationships (contexte de composition : parent, voisinage interdit, hiérarchie), Tokens (en anglais raisonnable — `emphasis`, `default`, `subtle` — pas `color-1`). Manquer un pilier = l'agent recommence à deviner.

**Structure de 6 fichiers par composant.** `.tsx` + `.meta.json` + `.tokens.css` + `.stories.tsx` + `.test.tsx` + `index.ts`. Storybook reste la vue visuelle humaine ; le `.meta.json` est la vue agentique. Même composant, deux lectures.

**Programming in English.** Citation Karpathy : "the hottest new programming language is English." L'instruction la plus puissante dans un fichier metadata est ce que le composant ne doit pas faire. Les anti-patterns spécifiques (jamais un bouton destructif dans un onboarding, jamais minimal dans un card header) ne peuvent pas être générés — ils viennent du savoir d'équipe et doivent être écrits manuellement.

**Audit Figma : intent vs position.** Les variables Figma doivent décrire le rôle (`emphasis`, `default`, `subtle`), non la position hiérarchique (`primary`, `secondary`, `tertiary`). Chaque variable doit avoir une description textuelle d'une ligne. Ces descriptions voyagent avec le design et donnent à l'agent le contexte pour choisir.

**Processus en 6 étapes.** (1) Sibling package sur branche, (2) schéma metadata d'abord, (3) audit Figma, (4) un composant end-to-end avant de scaler, (5) lecture et affinage manuel de la metadata, (6) encoder comme Claude Code skill.

## Citations clés (≤ 15 mots)

> "The metadata is the handoff."

> "The most powerful instruction in English is telling the agent what *not* to do."

> "An agentic design system removes the judgment step."

> "Drift stops happening because the agent has no excuse to invent."

## Données empiriques

Client B2B SaaS, ~20 composants structurés : feature work 5 jours → 1 après-midi. Throughput revendiqué : ~10x. Pas de protocole contrôlé (témoignage client).

## Connexions identifiées

La structure 6-fichiers est une implémentation alternative à celle de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) (`.metadata.ts` co-localisé). Les deux partagent la même logique (co-localisation, purpose, anti-patterns, tokens) mais divergent sur le format (`.meta.json` vs `.metadata.ts`) et le nombre de champs.

La distinction `emphasis/default/subtle` vs `primary/secondary/tertiary` pour les variables Figma est une application directe de [priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md) à la couche Figma — non plus au niveau des tokens de code, mais des variables de design.

Le skill `ai-component-metadata` de Chris Carini (référencé dans la source) est potentiellement une entité à documenter dans [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) ou dans une entité séparée — Chris Carini semble être la même personne que Cristian Morales Achiardi.
