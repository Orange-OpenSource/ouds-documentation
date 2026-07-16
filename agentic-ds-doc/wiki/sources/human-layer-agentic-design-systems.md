---
type: source
tags: [design-system, gouvernance, ia, accountability, designops, devops, humain, rôle-designer]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[concevoir-les-conditions](../concepts/concevoir-les-conditions.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[designops-devops-seam](../concepts/designops-devops-seam.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## The human layer in agentic design systems

**Auteur** : [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)
**Publication** : Design Systems Collective (Medium), 7 mars 2026
**URL** : https://www.designsystemscollective.com/the-human-layer-in-agentic-design-systems-d8f54d1bb2e5
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 7 (conclusive)
**Fichier brut** : `raw/The human layer in agentic design systems.md`

---

## Résumé structuré

Article de clôture de la série, qui déplace le regard de l'infrastructure technique vers la couche humaine qui la rend opérante. L'auteur documente un incident concret — une erreur dans l'échelle de jaune primitif, tracée depuis une interface jusqu'à lui — et en fait le point de départ d'une réflexion sur ce que la gouvernance agentique change au rôle du designer. La thèse centrale : le système peut exécuter fidèlement une décision incorrecte sans le savoir. Seul un humain qui fait confiance au système assez pour tracer les problèmes plutôt que les contourner peut fermer la boucle.

---

## Thèses principales

**Thèse 1 — Le système ne crée pas la correction, il la scale.** "The system scales whatever you give it. Including your mistakes." Si l'encodage est incorrect (une primitive jaune mal calibrée), le système exécutera l'erreur fidèlement, à l'échelle, sans jamais savoir qu'il se trompe. L'exactitude de l'exécution n'est pas la garantie de l'exactitude de la décision.

**Thèse 2 — La traçabilité comme forme d'accountability.** L'incident de l'échelle jaune produit une chaîne de traçabilité complète : développeur → système → token auditor → couche primitive → designer. Le système ne surface pas seulement une erreur — il surface *à qui appartient* l'erreur. C'est la différence entre un rapport d'anomalie et de l'accountability réelle.

**Thèse 3 — La confiance dans le système comme condition de son fonctionnement.** La développeuse aurait pu contourner le problème (changer un token, hardcoder une valeur). Elle a tracé à la place. Ce choix présuppose une confiance dans le système suffisante pour qu'il mérite d'être exploré plutôt qu'évité. "That trust is the environment working."

**Thèse 4 — La couture designops-devops.** Le design system agentique n'appartient ni complètement à designops, ni complètement à devops. Il opère au joint : "My token auditor doesn't just check that tokens exist (that's a linter). It checks whether the relationships between tokens violate the design intent (that's governance)." Catcher une failure designops à l'endroit où devops ne regarderait normalement pas.

**Thèse 5 — Concevoir des environnements, pas des interfaces.** "I'm not just a product designer anymore. I'm designing environments." Le rôle du designer est passé de la production d'interfaces à la conception des conditions sous lesquelles les interfaces se construisent correctement — extension directe de [concevoir-les-conditions](../concepts/concevoir-les-conditions.md).

---

## Données concrètes

Incident Enara : erreur dans l'échelle de jaune primitif détectée visuellement par un développeur. L'auditeur confirme l'implémentation correcte — ce qui pointe l'erreur vers la couche primitive. Correction : reconstruction de l'échelle, test Figma, export JSON, correction des tokens, push du package. Durée totale : environ 30 minutes. Sans l'infrastructure (token auditor, tracabilité de la couche primitive), la même correction aurait pris une semaine de tickets, investigations, et doigts pointés dans toutes les directions.

---

## Citations clés

> "The system scaled whatever you give it. Including your mistakes."

> "That trust is the environment working. And the environment traced the failure back to me. That's accountability."

> "My token auditor doesn't just check that tokens exist (that's a linter). It checks whether the relationships between tokens violate the design intent (that's governance)."

> "The work is in the seam." [entre designops et devops]

> "Most designers hand off decisions and hope. I encode decisions and know."

> "I'm not just a product designer anymore. I'm designing environments."

---

## Connexions identifiées

Enrichit [concevoir-les-conditions](../concepts/concevoir-les-conditions.md) avec l'angle accountability : concevoir les conditions n'est pas seulement un gain d'efficacité, c'est ce qui rend possible de savoir *dont* c'est l'erreur quand quelque chose se trompe. Enrichit [accountability-gap-ia](../concepts/accountability-gap-ia.md) avec le cas inverse : ici le gap est résolu — le système trace l'erreur jusqu'à son propriétaire. Enrichit [boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md) avec la dimension humaine de la boucle : la boucle ne fonctionne que si un humain fait confiance au système assez pour tracer plutôt que contourner. Crée [designops-devops-seam](../concepts/designops-devops-seam.md) comme nouveau concept. Met à jour [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) (série complétée à 7 parties).
