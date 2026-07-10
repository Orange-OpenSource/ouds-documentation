---
type: concept
tags: [design-system, ia, feedback, auto-amélioration, gouvernance, agentique, documentation, confiance, humain]
created: 2026-06-17
updated: 2026-07-07
sources:
  - "[[agent-orchestration-for-design-systems]]"
  - "[[how-to-automate-design-system-documentation]]"
  - "[[automating-design-system-ai-efficiency]]"
  - "[[self-healing-design-system]]"
  - "[[human-layer-agentic-design-systems]]"
related:
  - "[[protocole-arc]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[systeme-de-design-agentique]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[pipeline-figma-docs-automatise]]"
  - "[[documentation-lag]]"
  - "[[systeme-design-proactif]]"
  - "[[concevoir-les-conditions]]"
---

## La boucle de feedback infrastructure

La boucle de feedback infrastructure est le mécanisme par lequel les rapports d'adoption générés par l'agent améliorent l'infrastructure qui produit ces rapports. C'est ce qui rend un système de design agentique *actif* plutôt que passif — et ce qui, selon [[cristian-morales-achiardi]], fait passer l'agent du rôle de Consumer à celui de Maintainer ([[agent-orchestration-for-design-systems]]).

## Le mécanisme

Chaque rapport d'adoption produit non seulement des métriques sur le système de design, mais aussi des diagnostics sur la précision de la mesure elle-même. Ces diagnostics alimentent des améliorations concrètes des scripts et rules, qui produisent des rapports plus précis au cycle suivant.

Deux exemples documentés :

**Slot detection.** Le rapport de décembre 2025 révèle une inflation d'instances Icon sur `index.astro` : 31 reportés, 25 réels. L'analyse identifie la cause : quand un Icon est slotté dans un Button (`<Button><Icon /></Button>`), l'algorithme le comptait deux fois — une fois dans le template parent (correct), une fois en tracant la composition de Button (incorrect, car Button ne contient que `<slot />`). Solution : ajouter la détection des slot components à l'algorithme. Le prochain rapport : zéro inflation. Précision : 75 % → 95 %+.

**Timestamps en métadonnées.** La colonne "Modified Date" du dashboard affiche "N/A" en production. Cause : les timestamps étaient lus depuis le filesystem au runtime, indisponible en environnement serverless. Recommandation de l'agent : déplacer les timestamps dans les fichiers de métadonnées, les extraire à l'indexation, les stocker en TOON, les lire depuis le fichier généré. Résultat : source de vérité unique, mise à jour automatique, fonctionne en dev et en production.

## Ce que ça change

Sans boucle de feedback, les rapports mesurent le design system mais n'améliorent rien d'autre qu'eux-mêmes (si l'équipe agit dessus manuellement). Avec la boucle, l'infrastructure elle-même devient le sujet d'amélioration continue. Les rules deviennent plus précises. Les scripts deviennent plus exacts. Les artefacts deviennent plus riches. Chaque cycle rend le suivant plus utile.

La formulation de [[cristian-morales-achiardi]] : "The AI's analysis doesn't just measure the design system. It improves the measurement process" ([[agent-orchestration-for-design-systems]]).

## Relation avec le protocole ARC

La boucle de feedback est la mécanique interne de la transition entre Phase 2 (Report) et Phase 3 (Compose) du [[protocole-arc]]. Un système qui se contente de rapporter est en Phase 2. Un système qui utilise ces rapports pour s'améliorer automatiquement approche de la Phase 3. La boucle est le chemin entre les deux.

## ⚡ Tension / Contradiction

La boucle de feedback telle que décrite dans cet article est encore semi-manuelle : le rapport identifie un problème, l'humain lit la recommandation et implémente le correctif. La Phase 3 du [[protocole-arc]] (Compose) envisage que l'agent implémente lui-même le correctif. La boucle décrite ici est un état intermédiaire entre Phase 2 et Phase 3 — l'analyse est automatique, l'action reste humaine.

## La boucle self-healing (Kavcic) : Watch / Analyze / Execute / Observe

[[romina-kavcic]] formalise la boucle de feedback en 4 étapes opérationnelles dans son architecture de production ([[self-healing-design-system]]) :

**Watch** — détection continue de la dérive dans les tokens, les composants et la documentation. **Analyze** — scoring de la sévérité des dérives et priorisation des correctifs. **Execute** — génération de PRs, mise à jour de la documentation, synchronisation des tokens. **Observe** — vérification des résultats et rebouclage vers Watch.

Cette formulation est plus granulaire et plus opérationnelle que la boucle de [[cristian-morales-achiardi]], qui décrit le même mécanisme au niveau conceptuel (rapport → diagnostic → correctif) mais sans décomposer la phase d'exécution. L'étape Execute de Kavcic est celle où le [[systeme-design-proactif]] s'approche le plus de son état entièrement automatisé : l'agent ne signale pas seulement la dérive, il génère le PR. L'étape Observe est la garantie de qualité qui ferme la boucle et empêche la dérive des correctifs eux-mêmes.

## Extension : le système proactif comme boucle entièrement automatisée

[[mehmet-celik]] articule la version la plus avancée de la boucle de feedback : un design system qui détecte les patterns émergents à travers plusieurs projets et suggère de nouveaux composants, prédit les risques d'accessibilité avant les tests, et recommande des ajustements de tokens d'après les overrides observés ([[automating-design-system-ai-efficiency]]). La boucle de [[cristian-morales-achiardi]] reste semi-manuelle (l'agent rapporte, l'humain implémente). Le [[systeme-design-proactif]] est la version où l'observation, la détection et la recommandation — voire l'implémentation — sont entièrement déléguées. C'est la mécanique de la Phase 3 du [[protocole-arc]] poussée jusqu'à son terme.

## La confiance comme condition d'activation de la boucle

[[human-layer-agentic-design-systems]] introduit une dimension que les formulations techniques de la boucle laissent hors cadre : la boucle ne s'active que si les humains qui y participent font confiance au système suffisamment pour tracer les problèmes plutôt que les contourner.

L'incident de l'échelle de jaune chez Enara le montre a contrario. La développeuse avait plusieurs options : changer silencieusement le token, hardcoder une valeur qui rendait bien, ou signaler. Elle a signalé. Ce choix présuppose que le système mérite d'être exploré — que s'il y a une anomalie visuelle alors que les tokens sont corrects, c'est que quelque chose dans la couche inférieure est faux, et que cette chose peut être trouvée. Sans cette confiance, la boucle est court-circuitée au premier maillon.

[[cristian-morales-achiardi]] formule ce résultat : "The developer trusted the system enough to trace the problem instead of working around it. That trust is the environment working." La confiance dans le système n'est pas une propriété psychologique de la développeuse — c'est un indicateur que l'environnement a été construit de façon suffisamment cohérente pour mériter d'être exploré. Un système incohérent, dont les annotations sont souvent fausses et les auditeurs peu fiables, produit rationnellement des comportements de contournement. La confiance est une métrique de qualité de l'infrastructure autant qu'une attitude individuelle.

## Extension : la documentation comme boucle de feedback

[[romina-kavcic]] documente une instance différente de boucle de feedback appliquée à la documentation ([[how-to-automate-design-system-documentation]]). Le [[pipeline-figma-docs-automatise]] crée une boucle entre les sources de vérité design (Figma) et la documentation consommée par les équipes : un changement dans Figma déclenche automatiquement une mise à jour de la documentation, qui à son tour maintient les équipes synchronisées avec les décisions de design. La boucle est ici entièrement automatisée (y compris la détection de changement et la génération de PR) — contrairement à la boucle de Morales Achiardi qui reste semi-manuelle au niveau de l'action. Cette variante s'applique à la documentation humaine ; la boucle de Morales Achiardi s'applique à l'infrastructure agentique. Les deux partagent la même logique : l'artefact (rapport, documentation) améliore le système qui le produit ou en dépend.
