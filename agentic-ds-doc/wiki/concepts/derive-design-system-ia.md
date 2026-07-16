---
type: concept
tags: [design-system, drift, tokens, ia, echec, taxonomie, agents]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[superdesign-ai-design-system-drift](../sources/superdesign-ai-design-system-drift.md)"
related:
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[composant-comme-contrat](composant-comme-contrat.md)"
  - "[boucle-feedback-infrastructure](boucle-feedback-infrastructure.md)"
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[accountability-gap-ia](accountability-gap-ia.md)"
---

## La dérive de design system induite par l'IA

La dérive ("drift") de design system est la divergence lente entre le système réel d'une équipe et ce qu'un agent IA génère en son nom ([superdesign-ai-design-system-drift](../sources/superdesign-ai-design-system-drift.md)). Chaque génération est un peu décalée (une couleur inventée, un espacement différent, un composant reconstruit plutôt que réutilisé), et sur un produit multi-écrans ces petits écarts se cumulent jusqu'à ce que la marque devienne visuellement incohérente.

À distinguer de l'AI slop, déjà documenté ailleurs dans le vault comme convergence vers la moyenne générique de l'entraînement : le drift est une divergence par rapport au système *spécifique* de l'équipe. Une interface peut éviter le slop (elle a l'air soignée, professionnelle) et dériver quand même (elle ne correspond pas aux tokens et composants réels du système) — les deux problèmes sont orthogonaux.

## Les quatre modes de dérive

**Fabrication de tokens.** L'agent écrit un nom de token plausible qui n'existe pas dans le système — `--color-primary-500` quand le système utilise `--brand-action-bg`. Le nom sonne juste, donc passe une revue rapide sans être détecté. C'est le mode le plus proche de ce que [50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md) documentait déjà (audit de 50 fichiers, absence quasi-universelle de couche de sens) mais formulé ici comme comportement observé de l'agent plutôt que comme propriété manquante du fichier source.

**Dérive intra-session.** Le même composant, utilisé trois fois dans une même conversation, reçoit trois espacements légèrement différents. L'agent perd la valeur qu'il a choisie deux messages plus tôt — la cohérence se dégrade à l'intérieur même d'une session de travail continue.

**Amnésie inter-session.** Ce que l'agent a établi hier a disparu aujourd'hui. Une nouvelle conversation fabrique des tokens différents pour les mêmes composants — le build de lundi et celui de mercredi se désaccordent silencieusement, sans qu'aucune des deux versions ne soit explicitement fausse.

**Ruptures silencieuses.** Une v2 d'un composant est livrée avec une prop renommée. L'agent continue d'émettre la v1, parce que rien dans son contexte ne lui a signalé que le système avait bougé.

## La propriété commune : rien n'échoue visiblement

Aucun de ces quatre modes ne produit d'erreur explicite. C'est précisément ce qui les rend dangereux : "The output looks on-brand at a glance and is off-system underneath, which is harder to catch than something obviously wrong." Un composant visiblement cassé s'arrête à la revue. Un composant plausiblement correct mais structurellement décalé la traverse.

## Cause racine

L'agent n'a pas d'accès réel aux composants et tokens du système, et pas de mémoire persistante d'eux entre les sessions — il devine à partir de la moyenne statistique de toute l'UI sur laquelle il a été entraîné. Tout ce qui n'est pas explicitement mis devant lui (config Tailwind, APIs de composants, raisonnement derrière l'échelle d'espacement) est réinventé à chaque génération.

## Le coût comme taxe, pas comme crash

Contrairement à un bug qui casse visiblement quelque chose, le coût de la dérive se paie en continu : dette de composants (chaque élément off-system doit être reconstruit avant de shipper réellement), rework qui prend le pas sur les nouvelles fonctionnalités, burn de tokens et de crédits à chaque cycle de correction (le contexte est rechargé et régénéré à chaque round), lock-in du prompt (chaque ajustement mineur redevient un aller-retour avec l'agent), et érosion de la confiance — les équipes reviennent discrètement au travail manuel plutôt que de continuer à corriger.

## Les contre-mesures documentées

Geler les tokens dans un fichier unique que l'agent lit et ne régénère jamais, possédé par un humain (instance de la couche Rules always-on déjà documentée dans [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)). Contraindre l'agent aux composants réels plutôt qu'à la génération libre. Verrouiller les régions stables d'une interface (layout, header, sidebar) pour qu'une régénération ne les reconstruise pas. Valider systématiquement l'output contre le système avant livraison — lint sur les valeurs brutes, boucle render-screenshot-compare, parce que l'agent qui a écrit le code ne peut pas juger lui-même s'il correspond au système.

## Limite reconnue par la source

Un fichier de règles figé (type DESIGN.md) est nécessaire mais pas suffisant : il fixe les tokens, mais les agents dérivent encore sur l'*application* de ces tokens (comment composer un layout, quand une règle s'assouplit, un composant que le fichier ne mentionne jamais). Un fichier écrit une fois devient obsolète dès que le système réel évolue — la contrainte doit être un flux vivant, pas un artefact statique.

## Lien avec accountability-gap-ia

La dérive de design system est une des voies concrètes par lesquelles se matérialisent les défaillances composites décrites dans [accountability-gap-ia](accountability-gap-ia.md) : chaque mode de dérive pris isolément passe les contrôles automatiques (le token fabriqué a l'air d'un vrai token, la prop renommée compile), mais leur accumulation produit exactement le type d'incohérence qui échappe à l'audit composant par composant.
