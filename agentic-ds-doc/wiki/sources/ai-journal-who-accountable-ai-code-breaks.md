---
type: source
tags: [accountability, shadow-code, gouvernance, ia, blame, production]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[shadow-code](../concepts/shadow-code.md)"
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[shadow-ia-design-system](../concepts/shadow-ia-design-system.md)"
---

## AI Now Writes the Code. Who's Accountable When It Breaks?

**Auteur** : Pramin Pradeep (Co-fondateur/CEO BotGauge AI), via The AI Journal
**Date** : 2026-07-05
**URL** : https://aijourn.com/ai-now-writes-the-code-whos-accountable-when-it-breaks/
**Fichier brut** : `raw/2026-07-05_ai-journal-who-accountable-ai-code-breaks.md`

## Résumé

Introduit le concept de "shadow code" : logique logicielle qui entre en production via développement assisté par IA mais n'est jamais pleinement comprise, documentée ou examinée architecturalement par les humains responsables du système. Distinct du [shadow-ia-design-system](../concepts/shadow-ia-design-system.md) déjà présent dans le vault (contournement délibéré ou non du design system par d'autres équipes) : ici, l'opacité concerne le code lui-même, même quand il est produit dans le cadre d'un usage IA légitime et approuvé. Voir [shadow-code](../concepts/shadow-code.md).

## Le mécanisme

Un développeur prompte un assistant, reçoit une fonction propre et bien structurée, la vérifie superficiellement, résout le problème immédiat, merge. Le code entre en production. Personne ne l'a conçu au sens délibéré — personne n'a tracé ses hypothèses sur le comportement système, ses interactions avec les services adjacents, ce qu'il fait sous des conditions limites jamais couvertes par le prompt. À l'échelle de centaines ou milliers de snippets mergés, les systèmes deviennent "locally understood, but globally opaque" (recherche CodeRabbit citée).

## Pourquoi les contrôles existants ratent le problème

Les outils d'analyse statique scannent pour des patterns de vulnérabilité reconnaissables — pas pour des risques comportementaux émergeant de l'interaction dynamique de composants à l'exécution. La revue par les pairs a un biais structurel : le code généré par IA paraît plausible (bien formaté, logiquement structuré), ce qui réduit le scepticisme du reviewer sous pression de temps.

## Les chiffres

40-41 % du code généré par IA dans de nombreuses équipes fin 2025. Une brèche d'entreprise sur cinq désormais causée par du code généré par IA (Aikido Security 2026). 43 % des changements de code générés par IA nécessitent du débogage en production (Lightrun, avril 2026). Sur le blâme après une brèche liée à l'IA : 53 % blâment l'équipe sécurité, 45 % le développeur, 42 % qui a mergé — aucun consensus.

## Apport net

Complète le tableau des sources sur l'accountability avec un angle distinct de [big-agile-who-owns-ai-generated-code](big-agile-who-owns-ai-generated-code.md) : là où Dacy propose un mécanisme correctif (reviewer of record), Pradeep documente le mécanisme du problème lui-même (l'opacité qui s'accumule silencieusement même sans intention de contourner quoi que ce soit). Les deux sont complémentaires — diagnostic et remède.

## Citations clés

"Locally understood, but globally opaque." (recherche CodeRabbit, citée par Pradeep)

"That ambiguity is not hypothetical. [...] No consensus. No clear ownership. Just distributed blame and unresolved accountability." (Pramin Pradeep)
