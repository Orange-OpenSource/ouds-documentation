---
type: source
tags: [design-system, index, codebase, ia, graphe, toon, drift, navigation]
created: 2026-06-17
updated: 2026-06-17
sources: []
related:
  - "[mode-exploration-vs-navigation](../concepts/mode-exploration-vs-navigation.md)"
  - "[knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md)"
  - "[format-toon](../concepts/format-toon.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## Mapping your design system for AI agents

**Auteur** : [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)
**Publication** : Design Systems Collective (Medium), 14 janvier 2026
**URL** : https://www.designsystemscollective.com/codebase-indexing-for-design-systems-agents-c0f6b563a39e
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 4
**Fichier brut** : `raw/Mapping your design system for AI agents.md`

---

## Résumé structuré

Article technique sur la couche 1 des [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md) : l'index de codebase. Là où la partie 3 ([design-system-documentation-as-structured-metadata](design-system-documentation-as-structured-metadata.md)) documentait le *quoi* de chaque composant (métadonnées), celle-ci documente le *où* et le *comment* les composants se relient. L'argument central : sans carte, l'IA explore (mode déterministe impossible). Avec une carte, l'IA navigue (comportement prévisible, zéro dérive).

Le problème motivant l'article est concret et documenté : Claude importait ThoughtCard mais en recréait le markup depuis zéro juste en dessous. L'import inutilisé était là. La raison : Claude savait que le composant *existait* (quoi), mais pas qu'il était *pertinent dans ce contexte* (où et comment s'intègre-t-il). La métadonnée ne suffit pas. Il faut le graphe.

---

## Thèses principales

**Thèse 1 — Exploration vs Navigation.** Sans index, l'IA est en mode Exploration : grep, find, lecture de fichiers un par un, variance de 26,5 %, faux négatifs. Avec index, elle est en mode Navigation : lecture du graphe, comportement déterministe, 0,04 % de variance. "Without a map, AI explores. With a map, AI navigates. The difference is determinism."

**Thèse 2 — L'index répond à trois questions distinctes.** Inventaire (qu'est-ce qui existe ?), graphe de relations (qui utilise qui ?), statistiques de synthèse (combien, quelle couverture ?). Les trois ensemble permettent une déduction que ni la métadonnée ni le code source seul ne permettent.

**Thèse 3 — Import ≠ usage.** Une instance d'import ne dit pas combien de fois un composant est réellement instancié. Icon est importé une fois mais instancié 126 fois. L'instance count requiert le parsing des templates, pas seulement des imports. Cette distinction est critique pour les métriques d'adoption réelles.

**Thèse 4 — Les protocols transforment l'exploration en analyse dirigée.** Les instructions de query (CLAUDE.md) sont ce qui convertit l'index de données passives en comportement déterministe : charger une fois, raisonner sur le cache, ne jamais re-lire. Sans protocols, la variance de coût en tokens pour une question de suivi variait de 0 à 36 000 tokens.

**Thèse 5 — ROI réel = dette technique évitée.** L'index coûte légèrement plus de tokens par session (~28K vs ~27K). Mais le calcul pertinent n'est pas le coût de session — c'est la dette technique composée évitée : duplications, incohérences, faux négatifs qui s'accumulent à chaque génération.

---

## Données clés

Index de 55 composants, 302 relations, ~4 000 tokens pour chargement complet. Icon.astro : 126 instances pour 1 import. Tooltip : 3 niveaux de profondeur dans la chaîne de dépendances (Tooltip → CopyButton → CodeBlock → SkillCard). TOON vs JSON : 67 vs 89 caractères pour un composant, économie qui se cumule sur 300 relations.

---

## Connexions identifiées

Complète et approfondit [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md) (graphe de relations, deep tracing, instance counting). Enrichit [format-toon](../concepts/format-toon.md) (détail d'implémentation Python). Introduit [mode-exploration-vs-navigation](../concepts/mode-exploration-vs-navigation.md) comme cadre conceptuel central. Le ROI / dette technique composée enrichit [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md). La distinction métadonnées ("quoi") / index ("où") / les deux ("devrait-on ?") clarifie la complémentarité des couches 1 et 2 de [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md).
