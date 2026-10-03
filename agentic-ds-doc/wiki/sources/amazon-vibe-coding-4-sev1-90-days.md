---
type: source
tags: [incident, gouvernance, accountability, vibe-coding, production, amazon, echec]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
  - "[gouvernance-technique-ia](../concepts/gouvernance-technique-ia.md)"
  - "[modele-accountability-trois-couches](../concepts/modele-accountability-trois-couches.md)"
---

## 4 Sev-1s in 90 Days: The Real Cost of Amazon's Vibe Coding Bet

**Auteur** : Tom Piaggio (Autonoma AI)
**Date** : 2026-03-19
**URL** : https://getautonoma.com/blog/amazon-vibe-coding-lessons
**Fichier brut** : `raw/2026-03-19_amazon-vibe-coding-4-sev1-90-days.md`

## Résumé

Étude de cas la plus détaillée disponible publiquement d'un échec de déploiement IA à grande échelle. Amazon impose un mandat interne (80 % d'adoption hebdomadaire de son assistant Kiro) en parallèle de ~30 000 suppressions de postes en 90 jours : la vélocité de génération de code augmente pendant que la capacité de review humaine diminue. Quatre incidents Sev-1 suivent en 90 jours, dont une panne de 6h avec ~6,3M commandes perdues le 5 mars 2026. C'est le premier incident nommé, chiffré et documenté que le vault possède sur ce sujet — jusqu'ici, [accountability-gap-ia](../concepts/accountability-gap-ia.md) restait entièrement théorique.

## La distinction de Matt Garman

"Vibe coding" (accepter aveuglément l'output IA) vs "augmented coding" (l'IA accélère, l'humain maintient le contrôle qualité). Garman qualifie le remplacement des juniors par l'IA d'"une des idées les plus stupides jamais entendues" — la vision exécutive était nuancée. L'exécution à l'échelle l'a été moins : le mandat a comprimé le calendrier d'adoption (70 % d'essai en semaines), ce qui a transformé une partie de l'adoption en conformité plutôt qu'en adhésion réelle — et l'adoption par conformité est là où la qualité se dégrade.

## Les quatre incidents

Panne AWS Cost Explorer Chine (déc. 2025, 13h, attribuée par Amazon à une "erreur utilisateur" malgré des rapports citant l'IA agentique Kiro) ; délais de livraison incorrects (2 mars 2026, ~120 000 commandes perdues, Amazon Q identifié) ; chute de 99 % des commandes en Amérique du Nord (5 mars 2026, 6h, ~6,3M commandes perdues, déploiement sans documentation ni approbation formelle) ; un quatrième Sev-1 aux détails limités, relié par des documents internes à une "tendance d'incidents" liée aux "changements assistés par Gen-AI".

## La tension narrative

Amazon a affirmé publiquement dans certaines déclarations qu'aucun incident n'impliquait de code écrit par IA, tout en documentant en interne cette même tendance — documents ensuite édités avant la réunion de discussion. Cette contradiction est elle-même une donnée sur la gestion du narratif d'entreprise face à un échec d'infrastructure IA, distincte de la question technique elle-même.

## Les contre-mesures

Cadre de sécurité temporaire de 90 jours sur ~335 systèmes Tier-1 : sign-off senior obligatoire pour les changements assistés par IA (ingénieurs junior/mid), review à deux personnes, audits directeur/VP, friction contrôlée sur les déploiements critiques. Ce sont des rustines de vélocité (ajouter de la friction humaine), pas une architecture durable — l'auteur note que la réponse structurelle manquante est une vérification automatisée qui scale à la vitesse de génération de l'IA, pas une réinsertion de la revue humaine à chaque étape.

## Données de recherche citées

Apiiro (Fortune 50, ~6 mois) : vélocité de commit 3-4x plus rapide, mais PRs plus grosses et moins fréquentes ; findings de sécurité mensuels x10 ; failles architecturales (élévation de privilèges) +322 % ; failles de design +153 %. Étude ICSE 2026 (518 témoignages) : la vibe coding accumule la dette technique ~3x plus vite, QA "fréquemment négligée".

## Ce que ça implique pour le vault

Ce n'est pas un incident de design system au sens strict (pas de composants, tokens ou UI générée en cause directe), mais c'est l'analogue à grande échelle de ce que [accountability-gap-ia](../concepts/accountability-gap-ia.md) décrit en théorie pour les interfaces : une organisation qui a scalé la vélocité de génération plus vite que sa capacité de vérification et d'accountability, avec des conséquences réelles, chiffrées, et une réponse de gouvernance a posteriori documentée.

## Citations clés

"When you compress the timeline on velocity, you're also compressing the timeline on discovering what breaks." (Tom Piaggio)

"The durable fix is automated verification that runs at the speed of AI generation." (Tom Piaggio)
