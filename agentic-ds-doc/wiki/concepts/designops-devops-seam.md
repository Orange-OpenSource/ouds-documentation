---
type: concept
tags: [design-system, designops, devops, gouvernance, ia, infrastructure, séam, pipeline, tokens]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
related:
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[design-system-as-infrastructure](design-system-as-infrastructure.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## La couture designops-devops

Le design system agentique opère à l'endroit précis où designops et devops partagent une surface commune sans vraiment se toucher. Ce n'est ni un outil de designops, ni un outil de devops — c'est de l'infrastructure qui travaille la couture entre les deux.

## La distinction de départ

Designops et devops ne sont pas la même chose et ne doivent pas l'être. Designops s'intéresse à l'existence des bonnes décisions design et à leur communication d'intent : est-ce que le bon token existe ? Est-ce qu'il communique sa sémantique ? Devops s'intéresse à l'intégrité de l'exécution : le build est-il propre ? Le composant se rend-il correctement ? Les deux disciplines ont des matériaux différents, des boucles de feedback différentes, des modes de failure différents. Les fusionner fait perdre la spécificité de chacune. Les traiter comme entièrement séparées fait manquer le joint.

## Ce que fait l'infrastructure agentique

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) formule la nature de ce joint dans [human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md) : "A design token governance rule and a CI pipeline linting check serve the same structural purpose: enforce decisions at the point of execution." Les deux mécanismes — la règle de gouvernance de token et le lint check CI — font la même chose structurellement. Mais l'un opère sur des décisions design, l'autre sur de la syntaxe. L'infrastructure agentique permet à la gouvernance de décision design de s'appliquer au même point d'exécution que le lint check CI, sans appartenir pour autant au registre du CI.

L'exemple concret : le token auditor v2 (voir [existence-vs-intent-violations](existence-vs-intent-violations.md)) détecte quand `--foreground-muted` est utilisé pour du body copy. Ce n'est pas une vérification d'existence (le token est là, la référence est valide) — c'est une vérification sémantique que seul quelqu'un qui connaît l'intent design peut définir. L'auditeur capte une failure designops à l'endroit où devops ne regarderait jamais — dans la relation entre les tokens, pas dans leur présence.

## Le travail dans la couture

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) conclut : "The work is in the seam." Ni la fusion des deux disciplines, ni leur séparation complète. Le travail consiste à construire l'infrastructure qui fait circuler les décisions design vers le point d'exécution technique sans les déformer — et qui remonte les violations vers la couche où elles ont été définies plutôt que de les absorber silencieusement dans la codebase.

C'est précisément ce que fait la chaîne de traçabilité documentée dans l'incident de l'échelle jaune : une décision de design incorrecte au niveau primitif se remonte depuis l'interface (observation visuelle) → implémentation (vérification par l'auditeur) → token layer (primitif incriminé) → designer (propriétaire de la décision). La couture a fonctionné : une failure designops a été tracée par l'infrastructure devops jusqu'à son origine.

## ⚡ Tension : qui possède la couture ?

La question organisationnelle reste ouverte dans le corpus. L'infrastructure agentique de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) est construite par un designer qui est aussi développeur, dans une équipe sans séparation nette designops/devops. Dans les équipes plus grandes, avec des silos explicites entre les deux disciplines, la propriété de la couture — qui la construit, qui la maintient, qui l'améliore — n'a pas de réponse évidente. La couture technique existe ; la couture organisationnelle autour de la couture technique est le problème non résolu. Voir [gouvernance-design-system-ia](gouvernance-design-system-ia.md) (section gouvernance organisationnelle).
