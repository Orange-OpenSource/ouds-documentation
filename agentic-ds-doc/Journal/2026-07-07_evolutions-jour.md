---
type: journal
periode: jour
date: 2026-07-07
sources_ingérées: 2
pages_créées: 6
pages_mises_à_jour: 10
---

```
ÉVOLUTIONS — aujourd'hui (2026-07-07)
──────────────────────────────────────
Sources ingérées : 2
Pages créées     : 6
Pages mises à jour : 10
```

## Ce qui a été ingéré

Deux articles de [[murphy-trueman]] et [[cristian-morales-achiardi]], les deux voix les plus centrales du corpus, ont été ingérés aujourd'hui.

"Your design system is fragmenting into agent files" (Trueman) cartographie la pile complète des formats agent-facing (AGENTS.md, SKILL.md, DESIGN.md, Storybook manifest, MCP) et identifie trois angles absents du corpus : [[agents-md-format]] comme concept propre, la [[dispersion-decision-design]] d'une décision de design dans cinq emplacements sans synchronisation automatique, et la [[prompt-injection-design-system]] via les fichiers d'instructions.

"The human layer in agentic design systems" (Morales Achiardi) ferme la série de l'auteur. Contribution centrale : le système scale l'exactitude *et* les erreurs, et la gouvernance agentique ne garantit que l'exécution de ce qui a été encodé, pas la qualité de l'encodage.

## Ce qui a évolué

[[architecture-skills-rules-instructions]] s'est enrichi de la distinction recette vs description pour SKILL.md, et des nuances sur la portabilité vs l'exécution inconsistante entre agents. [[design-md-format]] a intégré sa position dans la pile des trois formats, la validation empirique de Wolosin sur le benchmark, et la distinction DTCG. [[gouvernance-design-system-ia]] a absorbé à la fois la gouvernance des coutures entre formats (Trueman) et la limite de la gouvernance agentique sur la qualité de l'encodage (Morales Achiardi) — deux angles orthogonaux qui enrichissent la même page. [[diana-wolosin]] et [[cristian-morales-achiardi]] ont reçu leurs mises à jour biographiques et bibliographiques respectives. [[accountability-gap-ia]] a intégré le cas inverse identifié par Morales Achiardi : un gap résolu par la traçabilité architecturale, ce qui raffine le concept en distinguant failures encodées et failures composites.

## Ce qui émerge

Deux tensions nouvelles ont cristallisé aujourd'hui. La première est structurelle : la multiplication des formats agent-facing ([[dispersion-decision-design]]) produit une dispersion des décisions de design sans gouvernance automatique des coutures — le problème que [[accountability-gap-ia]] identifiait au niveau organisationnel existe maintenant aussi au niveau technique, entre les formats. La seconde est sécuritaire et absente de tout le corpus antérieur : [[prompt-injection-design-system]] pointe le changement de statut des fichiers de documentation (de texte passif à instruction exécutable) comme une surface de risque que les pratiques de review habituelles ne couvrent pas.

Le concept de [[designops-devops-seam]] représente peut-être la synthèse la plus intéressante de la journée : Morales Achiardi formule que le travail est dans la couture, mais la question de qui possède organisationnellement cette couture reste le problème non résolu.

## Recommandations

Créer une page [[gouvernance-des-coutures-formats-agents]] dédiée, distincte de [[gouvernance-design-system-ia]] — la dispersion entre formats est un problème suffisamment distinct pour mériter sa propre page, avec des recommandations d'ownership et de pipeline par couche. Ingérer une source sur la sécurité des chaînes d'approvisionnement logicielles (supply chain security) pour nourrir [[prompt-injection-design-system]], qui reste pour l'instant un concept sans corpus derrière lui. Consolider [[accountability-gap-ia]] en intégrant explicitement la distinction failures encodées / failures composites dans le corps principal de la page, pas seulement dans le log. Appliquer le cadre [[dispersion-decision-design]] à OUDS spécifiquement : cartographier où vit aujourd'hui la décision "couleur primaire OUDS" dans les artefacts existants, pour rendre le problème concret et actionnable.
