---
type: concept
tags: [accountability, gouvernance, ia, ownership, raci, reviewer-of-record, organisation]
created: 2026-07-16
updated: 2026-07-16
sources:
  - "[big-agile-who-owns-ai-generated-code](../sources/big-agile-who-owns-ai-generated-code.md)"
related:
  - "[accountability-gap-ia](accountability-gap-ia.md)"
  - "[gouvernance-organisationnelle-ia](gouvernance-organisationnelle-ia.md)"
  - "[niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md)"
  - "[amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md)"
---

## Le modèle d'accountability à trois couches

Réponse structurelle au vide d'accountability documenté dans [accountability-gap-ia](accountability-gap-ia.md) : Lance Dacy ([big-agile-who-owns-ai-generated-code](../sources/big-agile-who-owns-ai-generated-code.md)) propose que l'accountability pour le code généré par IA se construise à trois couches, chacune requérant un humain nommé plutôt qu'une équipe collectivement responsable.

## Le diagnostic préalable : accountability diffusée n'est pas accountability

"AI didn't remove accountability from your engineering organization. It diffused it across so many hands that no one owns the outcome." Dans le modèle traditionnel, le code a un auteur : quand quelque chose casse, on remonte à une décision prise par quelqu'un. L'IA casse cette chaîne au premier maillon — le développeur qui a prompté n'a pas conçu la logique au sens délibéré, il l'a acceptée.

## Les trois couches

**Couche individuelle.** Pour tout travail incluant de l'output généré par IA, un humain nommé doit avoir revu le travail et être prêt à en répondre. Pratique testée en production : une ligne "Reviewer of record : [nom]" ajoutée à chaque PR assistée par IA. Ce n'est pas du gatekeeping — c'est désigner la dernière paire d'yeux humains qui a effectivement compris ce qui a été livré. Si le processus actuel ne peut pas nommer cette personne pour un changement donné, il y a un trou.

**Couche équipe.** L'équipe s'accorde sur les catégories de travail pouvant utiliser l'IA sans review renforcée, et celles qui l'exigent. Un refactoring de fonction utilitaire privée n'a pas besoin d'un audit profond ; tout ce qui touche authentification, autorisation, paiement ou PII en a besoin. Cette limite vit dans le working agreement ou la definition of done de l'équipe — elle protège les reviewers individuels de devoir auditer profondément chaque chemin de code, ce qui ralentirait tout, et protège l'organisation de laisser passer quelque chose d'important parce que personne n'était sûr que ça comptait.

**Couche organisationnelle.** Le leadership fixe la politique : catégories où l'IA est appropriée, comment la qualité est mesurée, qui possède les événements de qualité liés à l'IA au niveau leadership, comment ils sont revus trimestriellement. Sans cette couche écrite, les deux couches du dessous n'ont pas de fondation stable.

## Le test des 30 secondes

Le modèle ne vise pas une cérémonie supplémentaire mais un critère simple : pour tout artefact généré par IA qui atteint un client, on doit pouvoir tracer une chaîne d'accountability humaine en 30 secondes — pas 30 minutes, pas une réunion. Si personne n'est prêt à être nommé reviewer de record sur un travail donné, ce n'est pas un problème de qualité IA, c'est un problème de clarté.

## Les données qui motivent le modèle

Ox Security "Army of Juniors" (300+ repos analysés, oct. 2025) documente 10 patterns architecturaux et sécuritaires typiques de l'IA — "insecure by dumbness" selon leur VP Research. Le point clé : l'IA n'écrit pas un code pire ligne par ligne, elle supprime les goulots naturels (revues de code, second passage de debug) qui filtraient historiquement ce qui atteignait la production. Apiiro (Fortune 50, ~6 mois) documente le même phénomène sous un autre angle : vélocité de commit 3-4x plus rapide, mais avec des PRs plus grosses et moins fréquentes, findings de sécurité mensuels multipliés par 10, failles architecturales +322 %.

## Ce que le modèle résout et ce qu'il ne résout pas

Le modèle répond à "qui est responsable quand ça casse" par une désignation nominale à faible coût, pas par un audit préalable exhaustif. Il ne prévient pas la défaillance elle-même — il garantit qu'une personne identifiable peut être contactée immédiatement quand elle survient, et que cette personne avait un motif de comprendre ce qu'elle validait avant le merge. C'est un mécanisme d'accountability, pas un mécanisme de qualité au sens de [gouvernance-technique-ia](gouvernance-technique-ia.md) — les deux sont complémentaires, pas substituables.

## Instance de production : le reset Amazon

[amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md) documente une version dégradée de la couche organisationnelle mise en place *après* incident plutôt qu'avant : sign-off senior obligatoire, review à deux personnes, audits directeur/VP sur 335 systèmes critiques. C'est le modèle à trois couches appliqué en mode réactif et coûteux (friction ajoutée à chaque déploiement) plutôt qu'en mode préventif et léger (une ligne dans chaque PR) — la différence de coût entre construire l'accountability avant ou après l'incident est elle-même une donnée du modèle.
