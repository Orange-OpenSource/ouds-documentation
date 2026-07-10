---
type: source
tags: [design-system, figma, mcp, lisibilite-machine, nommage, agents, implicit-contract, skill-shift]
created: 2026-06-29
updated: 2026-06-29
sources: []
related:
  - "[[lisibilite-machine-design-system]]"
  - "[[ia-comme-utilisateur]]"
  - "[[priori-conflictuels-nommage]]"
  - "[[inversion-economique-code-comprehension]]"
  - "[[readable-vs-usable-token]]"
  - "[[intent-token]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[user-vs-maintainer-ia]]"
---

## Your Figma library is invisible to AI agents

**URL** : https://nurxmedov.medium.com/your-figma-library-is-invisible-to-ai-agents-31ff99d0ff9c
**Auteur** : Nurkhon (Nurxmedov)
**Date** : 16 avril 2026

## Thèse principale

Un design system peut être parfaitement construit — tokens, variants, nommage sémantique, documentation — et rester structurellement invisible à un agent IA. L'invisibilité n'est pas un défaut de qualité : c'est un défaut de lisibilité. **Illegible is different from incorrect.**

## Thèses secondaires

**"AI agents parse, not infer."** Un agent lit un nom, vérifie s'il correspond à un pattern reconnu, et l'utilise ou non. `nav-item-active-v3` ne correspond à aucun pattern — l'agent génère son propre composant depuis zéro. L'auteur a vécu exactement ça : 90 secondes pour générer un écran visuellement correct, entièrement déconnecté de la librairie.

**Le problème du contrat implicite.** Les noms d'un design system compriment une histoire : les conversations, les décisions, les versions. `input-v2-final` a un sens pour ceux qui étaient dans la pièce pour v1. Un agent n'a que le fichier, le nom, et la structure — rien d'autre. La communication humaine compresse ; les agents n'ont pas le décompresseur.

**Figma MCP a changé l'audience, pas le design system.** Avant le lancement du Figma MCP (24 mars 2026), un design system avait deux lecteurs : designers et développeurs, les deux arrivant avec du contexte. Avec le MCP, un troisième lecteur est entré dans la pièce — qui ne devient pas familier, qui requête à chaque session comme si c'était la première fois, et qui n'a aucun accès à l'historique implicite.

**Le shift de compétence.** Construire une librairie de composants est un problème de *craft visuel* — variants, états, composition, hiérarchie. Rendre cette librairie machine-readable est un problème d'*architecture structurelle* — schémas de nommage, taxonomies de tokens, contrats sémantiques entre couches. Ce sont des disciplines différentes. Un designer excellent dans la première n'est pas automatiquement compétent dans la seconde.

**Le judgment gap.** Les agents ne peuvent pas distinguer les décisions de design intentionnelles des accidents historiques. Deux composants visuellement identiques dans un fichier Figma — l'un production-approved, l'autre une expérience Q3 2024 jamais supprimée — sont traités identiquement. Cette distinction est irréductiblement humaine.

## Citations clés (≤ 15 mots)

> "AI agents parse, not infer."

> "Illegible is different from incorrect."

> "The agent reads what's there and uses it."

> "Token naming is structural legibility, not a cosmetic concern."

> "The agent's confidence is the problem."

> "Consistent wrong output, with high confidence, at scale."

## Données empiriques

Semantic token naming (`color-border-error` vs `red-300`) → **43% meilleure qualité de code généré** (Figma research, 2025). Seulement **23% des design systems** sont structurés suffisamment pour un usage IA consistent (UX Collective, décembre 2025). Seulement **8%** des équipes décrivent leur système comme "very stable" (enterprise survey 2026).

## Cas documentés

**Cas Nurkhon** : librairie Figma avec mois de travail, tokens, variants, nommage sémantique. Agent connecté via MCP. Résultat : écran visuellement correct, entièrement hardcodé, aucun composant de la librairie utilisé. Noms comme `nav-item-active-v3` et `modal-overlay-blur-dark` — illisibles pour l'agent.

**Cas Rostislav Peška (janvier 2026)** : agent avec seulement un `package.json` → HTML plain, zéro composant du design system. La réutilisation n'a augmenté que lorsque les composants étaient localement inspectables — structure assez explicite pour raisonner sans inférence.

**Cas Spotify Encore** : système sophistiqué, profond, connu pour sa qualité. Les développeurs allaient sur Cursor, obtenaient du non-Encore output, le shipper. Non pas parce qu'Encore était mal construit — parce qu'il était trop complexe pour qu'un agent le parse efficacement. L'agent a contourné la librairie plutôt que de la naviguer.

## Connexions identifiées

Le "contrat implicite" est la version narrative de ce que [[priori-conflictuels-nommage]] décrit techniquement : les agents arrivent avec 10 grammaires de nommage incompatibles ; les conventions implicites d'une équipe ne sont accessibles ni via les noms ni via les priors. Deux faces du même problème d'encodage.

Le "judgment gap" (intentionnel vs accidentel) est la limite permanente qui définit la valeur humaine dans [[user-vs-maintainer-ia]] : l'agent peut être Maintainer sur les tâches déterministes ; la distinction signifié/bruit dans un fichier Figma reste dans le registre du User humain.

Le skill shift (craft visuel → architecture structurelle) est la conséquence opérationnelle de [[inversion-economique-code-comprehension]] : le coût a migré de l'écriture du code vers la structuration de la connaissance — mais la compétence de structuration n'est pas distribuée dans les équipes de la même façon que la compétence de design.
