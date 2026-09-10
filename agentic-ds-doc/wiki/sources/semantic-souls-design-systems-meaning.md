---
type: source
tags: [design-system, agentique, ia, intent, semantique, gouvernance, drift, knowledge-graph]
created: 2026-08-17
updated: 2026-08-17
sources: []
related:
  - "[damini-patil](../entities/damini-patil.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[composant-comme-contrat](../concepts/composant-comme-contrat.md)"
  - "[knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md)"
  - "[derive-design-system-ia](../concepts/derive-design-system-ia.md)"
  - "[readable-vs-usable-token](../concepts/readable-vs-usable-token.md)"
---

## Semantic Souls: Why 2026 Design Systems Must Speak Meaning, Not Just Pixels

**Auteur** : [damini-patil](../entities/damini-patil.md)
**Publication** : Design Systems Collective (Medium)
**Date** : 2026-04-15
**URL** : https://www.designsystemscollective.com/semantic-souls-why-2026-design-systems-must-speak-meaning-not-just-pixels-f2093d9b4f65
**Fichier brut** : `raw/2026-08-17_semantic-souls-design-systems-meaning.md`

## Résumé

Damini Patil constate que la maturité technique des design systems (tokens, cohérence cross-platform, génération assistée par IA) a dépassé leur profondeur sémantique. Les interfaces générées par IA suivent les règles visuelles sans comprendre le but qu'elles servent, parce que les design systems ont historiquement été construits pour des humains qui apportaient eux-mêmes le contexte manquant. Sa proposition : une couche sémantique explicite faite de trois briques (intent tokens, contrats comportementaux, cartes de relations), complétée par une mise en œuvre pratique (champs explicatifs, bibliothèques de prompts, agents de gouvernance, tests de clarté contextuelle).

## Thèses principales

**Maturité technique sans profondeur sémantique.** L'infrastructure des design systems (tokens, multi-plateforme, génération IA) est mature, mais les interfaces produites "look on-brand but feel strangely hollow" : correctes visuellement, vides d'intention. C'est un diagnostic convergent avec celui de [romina-kavcic](../entities/romina-kavcic.md) sur les fichiers de tokens ([50-design-token-files-one-problem](50-design-token-files-one-problem.md)), mais formulé au niveau de l'interface entière plutôt qu'au niveau du fichier de tokens.

**Le gap du modèle mental partagé.** Les design systems traditionnels supposaient un designer humain qui apportait le contexte tacite. L'IA n'a pas ce modèle mental et ne peut pas interpréter *pourquoi* une décision de design existe, seulement *ce qu'elle est* visuellement.

**Trois briques de la couche sémantique.** Intent tokens (décrire le but : "destructive", "confirmatory"), contrats comportementaux (définir la réponse d'un composant selon le contexte), cartes de relations (expliquer les connexions entre patterns). Les trois briques recoupent chacune un concept déjà central dans le vault, voir Connexions identifiées.

**Mise en œuvre pratique.** Champs explicatifs ajoutés à la documentation de composants, bibliothèques de prompts appariées au design system, agents de gouvernance qui signalent la dérive sémantique, tests de clarté à travers les contextes (modes, accessibilité).

**L'avertissement.** Sans cette infrastructure, les agents IA autonomes deviennent des "dangerous amplifiers of inconsistency" : ils optimisent pour des métriques visibles (le rendu a l'air correct) en manquant les objectifs utilisateur, l'intention d'accessibilité et les considérations éthiques.

## Citations clés

"look on-brand but feel strangely hollow" ([damini-patil](../entities/damini-patil.md))

"dangerous amplifiers of inconsistency" ([damini-patil](../entities/damini-patil.md))

"Now it's time to teach them how to think." ([damini-patil](../entities/damini-patil.md))

## Connexions identifiées

Les "intent tokens" de Patil sont une reformulation indépendante, avec le même vocabulaire, de ce que [intent-token](../concepts/intent-token.md) documente déjà en détail via l'expérience crimson/red600 de Kavcic. La convergence terminologique entre deux auteurs qui ne se citent pas est un signal que la notion s'est stabilisée dans le champ, pas une nouvelle mécanique.

Les "behavioral contracts" recoupent directement [composant-comme-contrat](../concepts/composant-comme-contrat.md) : même déplacement conceptuel (un composant transporte une décision, pas seulement une apparence), vocabulaire quasi identique à celui de Kavcic ("rules, intent, constraints, accessibility requirements, and usage conditions").

Les "relationship maps" sont la formulation de Patil pour ce que le vault documente sous [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md) : une carte des relations entre composants, tokens et patterns, plutôt qu'une documentation statique à plat.

La "dérive sémantique" que les agents de gouvernance doivent signaler est un terme adjacent, mais distinct, des quatre modes de dérive déjà taxonomisés dans [derive-design-system-ia](../concepts/derive-design-system-ia.md) (fabrication de tokens, dérive intra-session, amnésie inter-session, ruptures silencieuses) : ceux-ci sont mécaniques (un token inventé, une prop renommée), la dérive sémantique de Patil est une érosion du sens (une interface correcte en surface, vide d'intention). Voir la section ajoutée dans [derive-design-system-ia](../concepts/derive-design-system-ia.md) pour la distinction complète.

Le diagnostic "look on-brand but feel strangely hollow" étend au niveau de l'interface entière la distinction readable/usable déjà établie au niveau du fichier de tokens dans [readable-vs-usable-token](../concepts/readable-vs-usable-token.md) : une interface peut être visuellement conforme (readable au sens build) sans être sémantiquement fondée (usable au sens intention).
