---
type: source
tags: [accountability, gouvernance, ia, ownership, raci, reviewer-of-record]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[modele-accountability-trois-couches](../concepts/modele-accountability-trois-couches.md)"
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
---

## Who Owns AI-Generated Code When It Ships to Production?

**Auteur** : Lance Dacy (Big Agile)
**Date** : 2026-06-01
**URL** : https://big-agile.com/blog/who-owns-ai-generated-code-when-it-ships-building-a-chain-of-human-accountability
**Fichier brut** : `raw/2026-06-01_big-agile-who-owns-ai-generated-code.md`

## Résumé

Apporte exactement ce qui manquait à [accountability-gap-ia](../concepts/accountability-gap-ia.md) : un modèle opérationnel concret plutôt qu'un problème seulement nommé. La thèse : l'IA n'a pas supprimé l'accountability, elle l'a diffusée à travers tant de mains que plus personne ne possède le résultat — et la responsabilité diffuse équivaut en pratique à une absence de responsabilité. Voir [modele-accountability-trois-couches](../concepts/modele-accountability-trois-couches.md) pour le détail du modèle.

## Les données qui fondent l'argument

Ox Security "Army of Juniors" (oct. 2025, 300+ repos analysés) : 10 patterns architecturaux et sécuritaires typiques de l'IA, "insecure by dumbness" selon leur VP Research — pas que l'IA écrit un code pire ligne par ligne, mais qu'elle supprime les goulots naturels (revues de code, second passage de debug) qui filtraient auparavant ce qui atteignait la production. Apiiro (Fortune 50, ~6 mois) : vélocité de commit 3-4x plus rapide mais avec des PRs plus grosses et moins fréquentes, findings de sécurité mensuels x10, failles architecturales +322 %.

## Le modèle à trois couches

Individuelle (un humain nommé, "reviewer of record", par changement assisté par IA) → Équipe (accord sur quelles catégories de travail exigent une review renforcée) → Organisationnelle (politique de leadership, mesure de qualité, revue trimestrielle). Chaque couche doit exister avec un nom humain attaché, sinon la couche du dessous n'a rien sur quoi s'appuyer.

## Le test des 30 secondes

Pour tout artefact généré par IA atteignant un client, on doit pouvoir tracer une chaîne d'accountability humaine en 30 secondes. La pratique minimale testée en production : une ligne "Reviewer of record : [nom]" dans chaque PR assistée par IA — coût nul, effet immédiat sur la qualité des conversations d'équipe sur l'usage de l'IA.

## Apport net par rapport à accountability-gap-ia

Murphy Trueman (déjà ingéré) nomme le problème et documente son absence de réponse dans la plupart des organisations, avec quatre candidats à la responsabilité sans arbitrage clair. Dacy apporte la réponse structurelle : un mécanisme à coût quasi nul (une ligne dans une PR) qui force la décision au moment du merge plutôt que de la reporter à un post-mortem. C'est la différence entre documenter un vide et documenter un pont.

## Citations clés

"Diffused accountability is not accountability." (Lance Dacy)

"You don't need a 50-page AI governance policy to start closing this gap. What you need is to engineer it into the workflow: a single named human attached to every AI-generated change that actually ships." (Lance Dacy)
