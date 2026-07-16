---
type: source
tags: [design-system, orchestration, ia, skills, rules, instructions, feedback, deep-tracing]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## Agent orchestration for design systems

**Auteur** : [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)
**Publication** : Design Systems Collective (Medium), 21 janvier 2026
**URL** : https://www.designsystemscollective.com/agent-orchestration-for-design-systems-da0f6a5f24fb
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 5
**Fichier brut** : `raw/Agent orchestration for design systems.md`

---

## Résumé structuré

Article sur l'orchestration — comment connecter les différentes couches de l'infrastructure agentique en un workflow cohérent. Deux contributions principales : l'architecture en trois couches d'instructions (Skills / Rules / Instructions), et la boucle de feedback où les rapports d'adoption améliorent l'infrastructure elle-même.

L'article approfondit également quatre stratégies opérationnelles : deep tracing (algorithme récursif avec détection de cycles), instance counting (avec gestion des slots), hiérarchie atomique comme diagnostic de santé système, et composition patterns comme règles de création.

---

## Thèses principales

**Thèse 1 — Trois couches d'instructions distinctes.** Les Skills sont des outils (capacités exécutables réutilisables), les Rules sont du contexte (contraintes passives spécifiques au projet), les Instructions sont la stratégie (méthodologie qui lie les deux). CLAUDE.md est le routeur qui pointe vers les règles qui référencent les skills.

**Thèse 2 — La boucle de feedback rend l'infrastructure agentique.** Les rapports d'adoption ne mesurent pas seulement le système — ils améliorent les scripts et règles qui produisent les prochains rapports. L'IA analyse sa propre analyse et la rend plus précise. C'est ce qui distingue une infrastructure "active" d'une infrastructure "passive".

**Thèse 3 — L'efficacité d'adoption comme diagnostic, pas comme métrique.** Un taux d'adoption de 63 % pour les atomes n'est pas une mauvaise nouvelle si l'agent comprend le contexte : c'est une philosophie de design (preference pour les utility classes). La valeur de l'infrastructure est de distinguer la dérive intentionnelle de la dérive involontaire.

**Thèse 4 — "Prefer editing over creating".** La règle de composition centrale : avant de créer un composant, chercher un composant similaire dans l'index, vérifier s'il peut être étendu, composer ce qui existe. Créer uniquement quand aucune alternative ne convient. Sans cette règle explicite, les agents prolifèrent les variantes.

---

## Citations clés

> "Skills are tools. Rules are context. Instructions are strategy."

> "The AI's analysis doesn't just measure the design system. It improves the measurement process."

> "The agent moves from consumer to maintainer." (à propos de la boucle de feedback)

---

## Connexions identifiées

L'architecture Skills/Rules/Instructions précise et enrichit la couche 3 de [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md) (le raisonnement). La boucle de feedback est la mécanique concrète de la transition User → Maintainer de [user-vs-maintainer-ia](../concepts/user-vs-maintainer-ia.md) et des phases 2→3 du [protocole-arc](../concepts/protocole-arc.md). L'algorithme de deep tracing détaillé enrichit [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md). L'efficiency rate comme diagnostic enrichit [gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md).
