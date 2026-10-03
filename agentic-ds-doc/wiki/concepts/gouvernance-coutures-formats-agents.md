---
type: concept
tags: [gouvernance, design-system, ia, formats, agents-md, skill-md, design-md, ownership, securite, prompt-injection, dispersion]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)"
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
related:
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[dispersion-decision-design](dispersion-decision-design.md)"
  - "[prompt-injection-design-system](prompt-injection-design-system.md)"
  - "[agents-md-format](agents-md-format.md)"
  - "[design-md-format](design-md-format.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[murphy-trueman](../entities/murphy-trueman.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## La pile sans gouvernance

La pile agent-facing qu'une équipe maintient typiquement aujourd'hui — JSON tokens, component manifest Storybook, AGENTS.md, DESIGN.md, SKILL.md, endpoint MCP Zeroheight — n'existait pas il y a dix-huit mois. Aucun modèle de gouvernance existant n'a été conçu pour elle ([your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)).

Le problème central : une décision de design unique (la couleur primaire d'un produit, par exemple) se réplique dans chacun de ces formats, avec un mode de représentation différent dans chaque emplacement, sans lien automatique entre eux. Le mécanisme et les cinq emplacements sont documentés dans [dispersion-decision-design](dispersion-decision-design.md). La conséquence : "The seams between them are where things break, and there's no role on the org chart whose job is to keep the seams healthy." ([murphy-trueman](../entities/murphy-trueman.md))

## Ownership recommandé par couche

[murphy-trueman](../entities/murphy-trueman.md) propose une répartition explicite de la propriété par couche de la pile.

Les **tokens JSON** restent sous ownership du design system — c'est la source de vérité canonique des valeurs, et son périmètre est déjà établi dans la plupart des équipes.

**AGENTS.md** est sous ownership de l'engineering : il contient les conventions de build, de test, de lint, et les règles de modification de la codebase. C'est un fichier d'infrastructure logicielle, pas de documentation design.

**DESIGN.md** est sous ownership de quiconque détient la marque dans l'organisation. En pratique, ce rôle est souvent non défini — "often it's whoever wrote it first." C'est la couture la plus fragile : le fichier encapsule l'identité visuelle canonique, mais son maintien n'est assigné à personne.

Le **Storybook component manifest** est généré automatiquement depuis les stories — pas de mainteneur humain dédié. Sa gouvernance est celle du pipeline de génération, pas du fichier lui-même.

Les **SKILL.md** files sont sous ownership de l'équipe qui pilote le tooling agent — design tooling, platform engineering, ou DevEx selon l'organisation. C'est souvent à mi-chemin entre design et engineering, ce qui laisse la propriété dans le flou.

La répartition est plus claire que ce que la plupart des équipes ont aujourd'hui. Elle est aussi plus de travail que ce pour quoi la plupart des équipes sont dimensionnées. "That's a clearer architecture than most teams have today. It's also more work than most teams are scoped for, which is the real problem nobody is solving." ([murphy-trueman](../entities/murphy-trueman.md))

## La question de revue des modifications

Le deuxième problème de gouvernance des coutures est celui du processus de revue. Quand un des formats est modifié, qui est notifié ? Qui valide que le changement est cohérent avec les autres couches ? Sans pipeline de synchronisation automatisé et sans processus de revue inter-couches, la dérive entre représentations s'accumule silencieusement.

La bonne pratique chez les équipes les plus avancées converge sur : chaque format de la pile est versionné dans git, les modifications passent en review, et un "seam owner" — même informel — est désigné pour les cas de conflit entre couches. En l'absence de rôle org chart dédié, c'est souvent le lead design system qui assume cette responsabilité de fait.

## La sécurité comme dimension de gouvernance ignorée

Les fichiers de la pile agent-facing ne sont pas des documents passifs — ce sont des instructions exécutables. Quiconque peut éditer AGENTS.md, un SKILL.md, ou un payload MCP peut orienter directement le comportement des agents qui opèrent sur le projet. "Prompt injection isn't theoretical when your design system documentation is an executable input." ([murphy-trueman](../entities/murphy-trueman.md))

Ce constat ouvre une surface de risque absente des modèles de gouvernance existants. L'auditeur de tokens de Enara vérifie que les agents utilisent correctement les tokens — il ne vérifie pas que les instructions qui orientent ces agents n'ont pas été altérées. Pour le mécanisme et les implications complètes, voir [prompt-injection-design-system](prompt-injection-design-system.md).

La gouvernance applicable est la même que pour le code CI/CD : les fichiers d'instructions agentiques doivent passer par les mêmes processus de review que le code de production — contrôle d'accès en écriture, historique auditable, validation que les changements ne modifient pas le comportement agent de façon non intentionnelle. La difficulté est culturelle : ces fichiers ressemblent à de la documentation, et les équipes les traitent avec des standards de review moins stricts que le code.

## Lien avec la limite de l'encodage

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) apporte une nuance complémentaire dans [human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md) : même une pile bien gouvernée — ownership clair, processus de revue en place, fichiers sous contrôle de version — ne peut exécuter que ce qui a été encodé. Si les valeurs primitives elles-mêmes sont incorrectes (comme l'échelle de jaune chez Enara), l'auditeur confirme leur usage correct sans détecter l'erreur sous-jacente. La gouvernance des coutures entre formats est nécessaire mais pas suffisante : elle garantit la cohérence entre représentations d'une même décision, pas la validité de la décision elle-même.

## ⚡ Tension : portabilité des formats vs cohérence globale

La propriété qui rend chaque format utile — il est autonome et portable, utilisable sans le reste de la pile — est aussi ce qui produit la dispersion. Un format qui dépend de la source de vérité centrale pour être valide n'est pas portable. Un format portable doit encoder suffisamment d'information pour fonctionner seul, ce qui signifie dupliquer des informations qui vivent déjà ailleurs. Il n'y a pas de résolution élégante à cette tension : seulement des pipelines de synchronisation plus ou moins automatisés, et une gouvernance organisationnelle qui décide quelle représentation fait autorité en cas de conflit. Voir [dispersion-decision-design](dispersion-decision-design.md) pour le détail de cette tension.
