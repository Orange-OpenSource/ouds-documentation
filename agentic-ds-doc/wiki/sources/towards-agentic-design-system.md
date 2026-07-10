---
type: source
tags: [design-system, agentic, ia, benchmark, gouvernance, arc, metadata]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[protocole-arc]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[format-toon]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[trois-couches-composants-agents]]"
  - "[[systeme-de-design-agentique]]"
  - "[[knowledge-graph-design-system]]"
  - "[[cristian-morales-achiardi]]"
---

## Towards an agentic design system

**Auteur** : [[cristian-morales-achiardi]]
**Publication** : Design Systems Collective (Medium), 2 janvier 2026
**URL** : https://www.designsystemscollective.com/towards-an-agentic-design-system-c7e0a6469bb1
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 2
**Fichier brut** : `raw/Towards an agentic design system.md`

---

## Résumé structuré

Article qui pose la question centrale : "quand est-ce que l'IA cesse de *consommer* le design system et commence à le *gouverner* ?" Pour y répondre, l'auteur décrit une expérience contrôlée (11 essais, 5 contrôle + 6 agentiques) sur la même base de code, avec et sans infrastructure machine-readable, et documente les résultats chiffrés. Il introduit ensuite le protocole ARC (Audit → Report → Compose) comme cadre de maturation vers un système auto-gouverné.

La particularité de cet article par rapport à [[design-system-most-important-asset-ai-era]] : il est empirique là où Kavcic est conceptuelle. Il fournit des données, du code concret (.metadata.ts, TOON index, CLAUDE.md protocols), et une validation expérimentale de la thèse de lisibilité machine.

---

## Thèses principales

**Thèse 1 — L'infrastructure bat le prompting, mesures à l'appui.** Avec infrastructure machine-readable : 2x plus rapide, 54 % plus précis, zéro faux négatif, 0,04 % de variance. Sans : 26,5 % de variance, faux négatifs (composants manqués), méthodologie aléatoire.

**Thèse 2 — Il y a une frontière entre User et Maintainer.** Un user (humain ou IA) demande "comment j'utilise ce composant ?". Un maintainer demande "est-ce que ce composant devrait exister ?". L'infrastructure agentique permet à l'IA de franchir cette frontière — de consommateur à garant du contrat architectural.

**Thèse 3 — Le protocole ARC.** Trois phases de maturité : Audit (consommateur prouvé), Report (mainteneur validé), Compose (auto-gouverné, phase future). Les metadata files sont le "cerveau" — ils encodent les décisions d'architecture que l'IA opérationnalise.

**Thèse 4 — La gouvernance change d'économie.** Un audit complet de design system coûtait du temps humain qualifié, de la coordination, des enquêtes, des Google Docs. Avec infrastructure : $0,20 en tokens, à la demande, avec la même méthodologie à chaque fois.

---

## Citations clés

> "I mean treating your design system as a data structure that AI can query, not just text it has to interpret."

> "The metadata files aren't just documentation for AI to read. They're contracts the AI can enforce."

> "When AI can detect drift, report it, and propose fixes, the system becomes self-governing."

> "Governance shifts from 'expensive tax we can't afford' to 'byproduct we get for almost free.'"

---

## Données empiriques clés

11 essais (5 contrôle, 6 agentiques). Même modèle (Claude Sonnet 4.5), même questions, même codebase. Variable unique : présence ou absence d'infrastructure machine-readable.

Investissement infrastructure : ~28K tokens en protocols structurés. Gains : 2,5x de vitesse, zéro faux négatif, performance prévisible. Coût d'un rapport d'adoption complet : $0,20.

---

## Connexions identifiées

Complète et valide empiriquement [[lisibilite-machine-design-system]] et [[trois-couches-composants-agents]] (Kavcic). Introduit [[protocole-arc]] comme cadre de maturité. Affine [[systeme-de-design-agentique]] avec la distinction [[user-vs-maintainer-ia]]. Le [[format-toon]] est une contribution technique spécifique à ce contexte.

La série complète de l'auteur comprend 6 parties déjà publiées dans le vault raw/ : Building an AI-Ready design system, Towards an agentic design system, Design system documentation as structured metadata, Codebase indexing for design systems agents, Agent orchestration for agentic design systems, Encoding governance on agentic design systems.
