---
type: source
tags: [design-system, drift, tokens, ia, echec, taxonomie]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[derive-design-system-ia](../concepts/derive-design-system-ia.md)"
  - "[readable-vs-usable-token](../concepts/readable-vs-usable-token.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
---

## Why AI Breaks Your Design System (and How to Fix the Drift)

**Auteur** : Jason Zhou (Superdesign)
**Date** : 2026-06-22
**URL** : https://superdesign.dev/blog/ai-design-system-drift
**Fichier brut** : `raw/2026-06-22_superdesign-ai-design-system-drift.md`

## Résumé

Premier document du vault à documenter des modes de défaillance design-system-spécifiques avec un mécanisme causal précis, plutôt que l'affirmation générale que "l'IA fait des erreurs". Note d'attribution : publié par l'éditeur d'un outil concurrent (Superdesign), le contenu a une teneur partiellement promotionnelle en fin d'article, mais la taxonomie des quatre modes de dérive est factuelle et indépendante de l'outil vendu — elle cite d'ailleurs des sources tierces (DLS Lead, AutonomyAI, UXPin, Rork) qui convergent sur le même diagnostic. Voir [derive-design-system-ia](../concepts/derive-design-system-ia.md) pour le détail.

## Les quatre modes de dérive

Fabrication de tokens (invente un nom plausible qui n'existe pas), dérive intra-session (le même composant reçoit des espacements différents dans une même conversation), amnésie inter-session (les tokens fabriqués changent d'une session à l'autre), ruptures silencieuses (continue d'utiliser une prop renommée sans le signaler). Aucun de ces modes ne produit d'erreur explicite — c'est précisément pourquoi ils atteignent la review humaine sans être détectés.

## La distinction avec l'AI slop

Le slop est la convergence vers la moyenne générique de tout ce sur quoi le modèle a été entraîné. Le drift est la divergence par rapport au système *spécifique* de l'équipe. Une page peut éviter le slop (elle a l'air soignée) et dériver quand même (elle ne correspond pas au système réel) — les deux problèmes sont orthogonaux, pas synonymes.

## Le coût comme taxe, pas comme crash

Dette de composants (chaque élément off-system doit être reconstruit avant de shipper), rework qui prend le pas sur les nouvelles features, burn de tokens/crédits à chaque cycle de correction, lock-in du prompt, érosion de la confiance (les équipes reviennent discrètement au travail manuel).

## Apport net par rapport au vault existant

Le vault documentait déjà la fabrication de tokens comme risque théorique (via [readable-vs-usable-token](../concepts/readable-vs-usable-token.md) et l'audit de 50 fichiers de Kavcic) mais sans nommer les trois autres modes (dérive intra-session, amnésie inter-session, ruptures silencieuses) ni les articuler comme une taxonomie unique avec une cause commune. C'est un vocabulaire précis qui manquait pour nommer ce qui casse concrètement.

## Citations clés

"The output looks on-brand at a glance and is off-system underneath, which is harder to catch than something obviously wrong." (Jason Zhou)

"Drift is not a model that is bad at design. It is a model designing from a system it was never allowed to see." (Jason Zhou)
