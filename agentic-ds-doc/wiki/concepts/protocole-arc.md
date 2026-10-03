---
type: concept
tags: [design-system, agentic, gouvernance, arc, audit, self-healing, composition, langage]
created: 2026-06-17
updated: 2026-07-09
sources:
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[building-language-design-systems](../sources/building-language-design-systems.md)"
  - "[design-systems-contracts-not-libraries](../sources/design-systems-contracts-not-libraries.md)"
related:
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[user-vs-maintainer-ia](user-vs-maintainer-ia.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[langage-design-system](langage-design-system.md)"
  - "[composant-comme-contrat](composant-comme-contrat.md)"
  - "[grammaire-composition-composants](grammaire-composition-composants.md)"
---

## Le protocole ARC : Audit → Report → Compose

Le protocole ARC est un cadre de maturité proposé par [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) pour structurer la progression d'un design system vers l'auto-gouvernance. Il décrit trois phases successives dans la relation entre un agent IA et un design system ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)).

## Phase 1 — Audit (le Consommateur)

**Statut : prouvé.**

L'IA lit le design system avec une précision complète et zéro faux négatif. L'infrastructure convertit une exploration chaotique (grep, bash, lecture manuelle de fichiers) en requêtes déterministes sur un index structuré. Valeur : 2,5x de vitesse, précision totale, performance prévisible (0,04 % de variance contre 26,5 % sans infrastructure).

C'est la phase de l'IA comme *user* — voir [user-vs-maintainer-ia](user-vs-maintainer-ia.md). Elle consomme le design system pour répondre à des questions : "quel composant utiliser ici ?", "quelles sont les dépendances de ce composant ?".

## Phase 2 — Report (le Mainteneur)

**Statut : validé.**

L'IA analyse les patterns, identifie la dette technique, et propose des améliorations architecturales. Elle ne compte pas — elle raisonne. Exemple concret : détecter que 14 instances d'une CSS class `.pill-alt` dupliquent la fonctionnalité du composant `Tag`, identifier des composants dupliqués, signaler des écarts entre les principes architecturaux déclarés et l'usage réel.

C'est le passage de l'IA de *user* à *maintainer* ([user-vs-maintainer-ia](user-vs-maintainer-ia.md)). Quand le système dit "`.pill-alt` duplique `Tag`", il n'utilise pas le design system — il fait respecter un contrat architectural. Valeur : gouvernance automatisée, audits à $0,20 à la demande ([gouvernance-design-system-ia](gouvernance-design-system-ia.md)).

## Phase 3 — Compose (l'Auto-gouverné)

**Statut : en développement conceptuel (juillet 2026).**

L'IA détecte la dérive, génère des correctifs, et maintient le système sans intervention manuelle. Quand le rapport identifie de la dérive, l'agent ne se contente pas de la signaler — il produit aussi le correctif. C'est la "self-healing infrastructure" : voir aussi [seeds-vs-trees](seeds-vs-trees.md) (les graines ont poussé, l'arbre est autonome).

En juillet 2026, Achiardi publie le cadre conceptuel qui fonde ce que "Compose" signifie concrètement ([building-language-design-systems](../sources/building-language-design-systems.md)) : pour que l'agent compose correctement, le design system doit être un *langage déclaré* — vocabulaire d'intent, grammaire d'assemblage, contrats formels ([langage-design-system](langage-design-system.md)). Ce n'est pas suffisant que l'agent lise les composants (Phase 1) ou audite la dérive (Phase 2) : il doit *parler le langage du système*, c'est-à-dire composer en respectant les termes, les règles et les contrats sans interférence de ses priors de framework ([priori-conflictuels-nommage](priori-conflictuels-nommage.md)).

L'article de mai 2026 ([design-systems-contracts-not-libraries](../sources/design-systems-contracts-not-libraries.md)) pose le prérequis architectural : la Phase 3 suppose que le design system est un contrat formel (pas seulement une bibliothèque), et que ses règles de composition sont explicites et machine-lisibles.

## ⚠️ Disambiguation : deux "ARC" dans le vault

Le terme "ARC Protocol" désigne deux choses distinctes dans le vault :

- **[protocole-arc](protocole-arc.md)** (cette page) : le cadre de maturité d'Achiardi — Audit → Report → Compose — pour design systems agentiques.
- **[arc-protocol-rpc](../entities/arc-protocol-rpc.md)** : le projet open-source arc-protocol.org — protocole RPC stateless pour communication inter-agents, avec chiffrement post-quantique. Un protocole réseau, pas un cadre de maturité.

## Relation avec les trois couches de Kavcic

Le protocole ARC présuppose les [trois-couches-composants-agents](trois-couches-composants-agents.md) comme fondation. Phase 1 requiert au minimum la couche 1 (index). Phase 2 nécessite les couches 1 et 2 (métadonnées). Phase 3 requiert les trois couches, plus un [knowledge-graph-design-system](knowledge-graph-design-system.md) complet. La progression ARC est donc aussi une progression dans la complétude des couches.
