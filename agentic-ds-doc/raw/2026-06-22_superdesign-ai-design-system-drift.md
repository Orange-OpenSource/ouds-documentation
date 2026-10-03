---
source_url: https://superdesign.dev/blog/ai-design-system-drift
author: Jason Zhou (Superdesign)
published: 2026-06-22
ingested: 2026-07-16
---

# Why AI Breaks Your Design System (and How to Fix the Drift)

Source brute — issue du blog Superdesign (éditeur d'un outil de design assisté par IA, contenu à teneur partiellement promotionnelle mais taxonomie factuelle indépendante de l'outil).

## Définition

Le "design system drift" est la divergence lente entre le design system réel d'une équipe et ce qu'un agent IA génère en son nom. Chaque génération est un peu décalée (une couleur inventée, un espacement différent, un composant reconstruit plutôt que réutilisé) et sur un produit multi-écrans ces petits écarts se cumulent jusqu'à ce que la marque devienne floue. Distinct de l'"AI slop" (convergence vers la moyenne générique) : le drift est une divergence par rapport au système *spécifique* de l'équipe, pas par rapport à un standard générique.

## Les quatre modes de dérive

**Fabrication de tokens.** Le modèle écrit un nom de token plausible qui n'existe pas — `--color-primary-500` quand le système utilise `--brand-action-bg`. Le nom sonne juste, donc passe une revue rapide sans être détecté.

**Dérive intra-session.** Même composant, trois usages, trois espacements légèrement différents. Le modèle perd la valeur choisie deux messages plus tôt — la cohérence se dégrade à l'intérieur d'une même session.

**Amnésie inter-session.** Ce que le modèle a compris hier a disparu. Une nouvelle conversation fabrique des tokens différents pour les mêmes composants — le build de lundi et celui de mercredi se désaccordent silencieusement.

**Ruptures silencieuses.** Une v2 d'un composant est livrée avec une prop renommée. Le modèle continue d'émettre la v1, parce que rien ne lui a signalé que le système avait bougé.

## Cause racine

Le modèle n'a pas d'accès réel aux composants et tokens, et pas de mémoire d'eux — il devine à partir de la moyenne statistique de toute l'UI sur laquelle il a été entraîné. Il ne peut pas voir la config Tailwind, les APIs de composants ou le raisonnement derrière l'échelle d'espacement, à moins qu'on les lui mette explicitement devant. Tout ce qui n'est pas dit est réinventé.

## Le coût réel

Pas un crash — une taxe sous-évaluée : dette de composants (chaque élément off-system doit être reconstruit avant de pouvoir shipper), rework qui prend le pas sur les nouvelles features, burn de tokens/crédits à chaque cycle de correction (le contexte est rechargé et régénéré à chaque round), lock-in du prompt (chaque ajustement mineur redevient un aller-retour avec l'IA), érosion de la confiance (les équipes arrêtent de faire confiance au système et reviennent discrètement au travail manuel).

## Comment arrêter la dérive

1. Geler les tokens dans un fichier unique que l'agent lit et ne régénère jamais (source de vérité possédée par un humain).
2. Contraindre l'agent aux composants réels, pas à la génération libre — il doit assembler avec le Button existant, pas en inventer un nouveau.
3. Verrouiller les parties stables (layout, header, sidebar) pour qu'une régénération ne les reconstruise pas.
4. Valider l'output contre le système avant livraison — lint sur le hex brut et les éléments off-system, boucle render-screenshot-compare.

## Limite reconnue

Un fichier de règles (type DESIGN.md) est nécessaire mais pas suffisant : il fixe les tokens mais les agents dérivent encore sur l'*application* (comment composer un layout, quand une règle s'assouplit, un composant que le fichier ne mentionne jamais), et un fichier écrit une fois devient obsolète dès que le système réel change.
