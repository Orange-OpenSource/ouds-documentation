---
source_url: https://getautonoma.com/blog/amazon-vibe-coding-lessons
author: Tom Piaggio (Autonoma AI)
published: 2026-03-19
ingested: 2026-07-16
---

# 4 Sev-1s in 90 Days: The Real Cost of Amazon's Vibe Coding Bet

Source brute — synthèse issue de reporting Financial Times, Fortune, The Register, et de documents internes Amazon cités par ces médias.

## Le mandat

24 novembre 2025 : mémo interne établit Kiro (assistant de code IA propriétaire d'Amazon) comme outil standardisé, cible 80 % d'usage hebdomadaire d'ici fin d'année. Janvier 2026 : 70 % des ingénieurs l'ont essayé. Amazon cite 21 000 agents IA déployés à travers Amazon Stores, 2 milliards $ d'économies revendiquées, gain de vélocité développeur de 4,5x (Dave Treadwell, SVP eCommerce Foundation). Contexte : ~30 000 suppressions de postes corporate en 90 jours (14 000 en octobre 2025, 16 000 en janvier 2026) en parallèle du mandat — la vélocité de génération augmente pendant que la capacité de review humaine diminue.

## La distinction de Matt Garman (déc. 2025, podcast WIRED Uncanny Valley)

"Vibe coding" = accepter aveuglément l'output IA. "Augmented coding" = l'IA accélère le travail mais les développeurs maintiennent un contrôle qualité. Garman qualifie de "l'une des idées les plus stupides jamais entendues" le remplacement des employés juniors par l'IA. Démo re:Invent 2025 : projet de 30 développeurs / 18 mois compressé à 6 développeurs / 76 jours avec Kiro.

## Les quatre incidents Sev-1 (déc. 2025 - mars 2026)

| Date | Incident | Durée | Impact estimé | Attribution |
|---|---|---|---|---|
| Déc. 2025 | Panne AWS Cost Explorer (Chine) | 13h | Service indisponible | Amazon : "erreur utilisateur" ; rapports citent l'IA agentique Kiro |
| 2 mars 2026 | Délais de livraison incorrects dans les paniers | inconnue | ~120 000 commandes perdues | Amazon Q identifié comme contributeur principal |
| 5 mars 2026 | Chute de 99% des commandes, Amérique du Nord | 6h | ~6,3M commandes perdues (non vérifié, source Medium largement citée) | Déploiement sans documentation ni approbation formelle |
| Début mars 2026 | Sev-1 additionnel (détails limités) | inconnue | inconnu | Documents internes : "tendance d'incidents" liée aux "changements assistés par Gen-AI" |

Documents internes Amazon avertissaient que la génération rapide de code par GenAI "exposait accidentellement des vulnérabilités" et que les mesures de sécurité actuelles étaient "complètement inadéquates". Ces références ont été supprimées des documents de réunion avant discussion (selon Fortune).

## La réunion de crise (10 mars 2026)

Dave Treadwell (le même SVP qui avait porté le déploiement de 21 000 agents) convoque une réunion obligatoire de leadership senior. Email interne : "the availability of the site and related infrastructure has not been good recently." ~1 500 ingénieurs avaient déjà signé une pétition interne demandant Claude Code à la place de Kiro. Citations d'ingénieurs (Fortune) : "People are becoming so reliant on AI that essentially they stop reviewing the code altogether."

## Les contre-mesures (cadre de sécurité temporaire de 90 jours)

Pour ~335 systèmes "Tier-1" : sign-off d'ingénieur senior obligatoire pour tout changement de production assisté par IA (ingénieurs junior/mid-level) ; review de code à deux personnes obligatoire ; audits de niveau directeur/VP sur les changements de production ; friction contrôlée ajoutée aux déploiements affectant les systèmes retail critiques.

## Tension : narratif public vs documents internes

Amazon a affirmé publiquement dans certaines déclarations qu'"aucun des incidents n'impliquait de code écrit par IA", tout en documentant en interne une "tendance d'incidents" liée aux "changements assistés par Gen-AI" — documents ensuite édités avant la réunion de discussion.

## Contexte réglementaire

EU AI Act, dispositions high-risk applicables août 2026, amendes jusqu'à 35M€ ou 7% du chiffre d'affaires mondial. Gartner projette que 40%+ des projets d'IA agentique seront annulés d'ici fin 2027 face au "governance gap".

## Données de recherche citées

CodeRabbit : code généré par IA a ~1,7x plus de problèmes que le code humain. Apiiro (analyse de dizaines de milliers de repos, entreprises Fortune 50, ~6 mois) : développeurs assistés par IA committent 3-4x plus vite ; failles de sécurité mensuelles passées de ~1000 à 10000+ en 6 mois ; failles architecturales (élévation de privilèges) +322% ; failles de design +153%. Étude ICSE 2026 (518 témoignages de praticiens) : la vibe coding accumule la dette technique ~3x plus vite que le développement traditionnel, QA "fréquemment négligée".
