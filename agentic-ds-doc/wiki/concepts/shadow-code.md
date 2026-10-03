---
type: concept
tags: [shadow-code, accountability, ia, opacite, production, gouvernance]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[ai-journal-who-accountable-ai-code-breaks](../sources/ai-journal-who-accountable-ai-code-breaks.md)"
related:
  - "[shadow-ia-design-system](shadow-ia-design-system.md)"
  - "[accountability-gap-ia](accountability-gap-ia.md)"
  - "[modele-accountability-trois-couches](modele-accountability-trois-couches.md)"
---

## Le shadow code

Le shadow code désigne la logique logicielle qui entre en production via développement assisté par IA mais qui n'est jamais pleinement comprise, documentée, ou examinée architecturalement par les humains responsables du système ([ai-journal-who-accountable-ai-code-breaks](../sources/ai-journal-who-accountable-ai-code-breaks.md)). Ce n'est pas nécessairement du code buggé — une partie fonctionne parfaitement, indéfiniment. Le problème est que son comportement sous conditions spécifiques n'a jamais été interrogé, parce que le processus qui l'a produit ne requiert pas cette interrogation de la même façon que l'ingénierie délibérée.

## ⚡ Disambiguation avec le shadow AI du design system

À ne pas confondre avec [shadow-ia-design-system](shadow-ia-design-system.md), déjà présent dans le vault : le Shadow AI y désigne l'usage d'outils IA par des équipes *en dehors* du design system, produisant une UI qui contourne le système sans que l'équipe DS le sache. Le shadow code désigne un phénomène différent : du code produit *avec* les bons outils, potentiellement en respectant le design system, mais dont personne n'a tracé les hypothèses, les interactions avec les services adjacents, ou le comportement sous conditions limites. Le premier est un problème de contournement (le code ne passe pas par le système). Le second est un problème d'opacité (le code passe par le système mais personne ne le comprend pleinement).

## Le mécanisme d'accumulation

Un développeur prompte un assistant, reçoit une fonction propre et bien structurée, la vérifie superficiellement, résout le problème immédiat, merge. Le code entre en production. À l'échelle de centaines ou milliers de snippets mergés à travers une organisation, les systèmes deviennent ce que la recherche CodeRabbit (citée par la source) nomme "locally understood, but globally opaque" : chaque pièce a l'air correcte isolément, mais aucun ingénieur ne peut tracer l'ensemble de bout en bout avec confiance.

## Pourquoi les contrôles existants ne le détectent pas

Les outils d'analyse statique scannent les artefacts de code pour des patterns de vulnérabilité reconnaissables (injection, dépendances non sécurisées, erreurs de configuration) — ils ne sont pas construits pour détecter les risques comportementaux qui émergent seulement quand des composants interagissent dynamiquement à l'exécution. La revue par les pairs a son propre biais structurel : le code généré par IA paraît souvent correct, bien formaté, immédiatement fonctionnel — cette plausibilité réduit le scepticisme du reviewer sous pression de temps, précisément le mécanisme qui permet au shadow code de s'accumuler sans déclencher d'alerte.

## Les chiffres

40-41 % du code généré par IA dans de nombreuses équipes d'ingénierie fin 2025. Une brèche d'entreprise sur cinq désormais causée par du code généré par IA (Aikido Security, 2026). 43 % des changements de code générés par IA nécessitent du débogage en production (Lightrun, avril 2026). Sur la question du blâme après une brèche liée à l'IA : 53 % blâment l'équipe sécurité, 45 % le développeur, 42 % qui a mergé le code — la dispersion elle-même est la donnée, elle signale l'absence de consensus sur l'ownership plutôt qu'un simple désaccord ponctuel.

## Lien avec l'accountability gap

Le shadow code est le mécanisme concret par lequel [accountability-gap-ia](accountability-gap-ia.md) se matérialise en production : si personne n'a tracé les hypothèses d'un bout de code, personne ne peut être tenu responsable de ses effets de bord de façon informée. Le [modele-accountability-trois-couches](modele-accountability-trois-couches.md) (reviewer of record nommé sur chaque changement) est une réponse structurelle directe à ce mécanisme — il force la traçabilité au moment du merge plutôt que de la reconstruire péniblement après incident.
