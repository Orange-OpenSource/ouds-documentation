---
type: concept
tags: [ia, agents, pipeline, intent, contexte, design-system]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[design-system-most-important-asset-ai-era]]"
related:
  - "[[systeme-de-design-agentique]]"
  - "[[trois-couches-composants-agents]]"
  - "[[composants-context-aware]]"
---

## Le pipeline Intent → Contexte → Sortie système

[[romina-kavcic]] formalise le flux de traitement d'un agent sur un design system en trois étapes : **Intent** (langage naturel) → **Contexte** (dimensions extraites) → **Sortie système** (guidance spécifique) ([[design-system-most-important-asset-ai-era]]).

## Les trois étapes

**Intent** : la demande en langage naturel. "J'ai besoin d'un dialog de confirmation pour supprimer un workspace." C'est le point d'entrée, non structuré, exprimant une intention fonctionnelle.

**Contexte** : l'agent extrait de cette phrase cinq dimensions : le type de composant (dialog de confirmation), la sévérité de l'action (destructive), le flux utilisateur (suppression permanente), le scope des tokens (danger vs primary), et la plateforme. Ces dimensions sont les lentilles à travers lesquelles le système est interrogé.

**Sortie système** : pas une suggestion vague, mais une guidance précise. Dialog + Alert + 2 Buttons. Mapping du token `color.bg.danger`. Règle "toujours associer à un Cancel". Lien vers le composant Dialog dans Figma. Template de composition suggéré.

## Ce que ça exige du design system

L'agent ne "devine" pas. Il lit les règles du système à travers ces couches de contexte. La sortie est aussi précise que les règles d'entrée sont complètes. Si les règles n'existent pas — si les métadonnées de composants sont absentes, si les tokens n'ont pas d'intent, si la logique de composition n'est pas formalisée — le pipeline produit des sorties génériques ou incorrectes.

C'est pourquoi [[trois-couches-composants-agents]] est le prérequis structurel de ce pipeline : sans les trois couches, les "dimensions" extraites à l'étape Contexte ne peuvent pas être résolues en guidance concrète à l'étape Sortie.
