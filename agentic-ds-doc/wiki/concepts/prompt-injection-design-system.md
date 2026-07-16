---
type: concept
tags: [design-system, ia, sécurité, gouvernance, prompt-injection, agents-md, skill-md, mcp]
created: 2026-07-07
updated: 2026-07-07
sources:
  - "[your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)"
related:
  - "[agents-md-format](agents-md-format.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[murphy-trueman](../entities/murphy-trueman.md)"
---

## Prompt injection via la documentation du design system

Les formats de la pile agent-facing (AGENTS.md, SKILL.md, component manifests, MCP server payloads) sont des instructions exécutables pour les agents — pas des documents passifs. Ce changement de statut introduit une surface de risque que la plupart des équipes de design system n'ont pas encore intégrée à leurs modèles de gouvernance ([your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)).

## La nature du risque

Quand un agent lit AGENTS.md, il suit ces instructions. Quand il interroge un MCP server, il exécute ce que les payloads lui prescrivent. Quand il charge un Skill, il suit la procédure définie dans SKILL.md. Ces fichiers ne sont pas des guidelines que l'agent interprète librement — ils orientent et contraignent son comportement de façon directe.

"Anyone who can edit your AGENTS.md, SKILL.md, or component manifest can shape agent behaviour, and instructions delivered through MCP payloads increasingly need the same review discipline teams already apply to code and CI configuration." ([murphy-trueman](../entities/murphy-trueman.md))

"Prompt injection isn't theoretical when your design system documentation is an executable input." ([murphy-trueman](../entities/murphy-trueman.md))

## Ce que ça implique pour la gouvernance

La documentation du design system a toujours eu un impact sur les comportements — mais cet impact était médiatisé par un humain qui lisait, interprétait, et décidait d'appliquer ou non. Avec des agents qui lisent ces fichiers et les exécutent directement, la chaîne de causalité est plus courte et plus automatique.

Un contenu malveillant ou mal contrôlé dans AGENTS.md peut rediriger le comportement d'un agent sur l'ensemble des interactions avec le projet. Un payload MCP mal sécurisé peut injecter des instructions hors du contrôle de l'équipe design system. Un Skill éditable par un tiers peut modifier le workflow que l'agent suit pour implémenter des composants.

## Gouvernance applicable

Trueman ne développe pas de recommandation détaillée — il soulève le problème comme un angle ignoré. Mais la logique de gouvernance applicable est symétrique à celle du code : les fichiers d'instructions agentiques (AGENTS.md, SKILL.md, composants MCP server configs) devraient passer par les mêmes processus de review que le code de production. Cela implique : contrôle d'accès en écriture, historique de modifications auditable (git pour les fichiers de dépôt, versioning pour les configs MCP), et validation que les changements à ces fichiers ne modifient pas le comportement agent de façon non intentionnelle.

La difficulté est que ces fichiers sont souvent traités comme de la documentation plutôt que comme du code — et donc soumis à des standards de review moins stricts. Le changement de catégorie (de "doc passive" à "instruction exécutable") n'est pas encore reflété dans les pratiques de la plupart des équipes.

## Relation avec la gouvernance technique existante

La gouvernance technique documentée dans [gouvernance-design-system-ia](gouvernance-design-system-ia.md) (auditeurs de tokens, niveaux de confiance par action, contraintes exécutables) adresse les agents qui *opèrent à l'intérieur* du design system. La prompt injection adresse une menace orthogonale : la manipulation des *instructions* que ces agents reçoivent, avant même qu'ils commencent à opérer. Les deux niveaux de gouvernance sont complémentaires — l'un contrôle ce que l'agent fait, l'autre contrôle ce qu'on lui dit de faire.

## ⚡ Tension : accessibilité vs sécurité des fichiers d'instructions

La proposition de valeur des formats comme AGENTS.md est leur accessibilité : n'importe qui dans l'équipe peut lire et modifier un fichier Markdown. Cette même accessibilité est ce qui crée le risque — le fichier n'est pas protégé par les contrôles d'accès habituellement associés aux fichiers d'infrastructure. Pour des organisations où le dépôt de code est ouvert à un large nombre de contributeurs (designers, PMs, product writers), la surface d'exposition est significative. La tension n'a pas de résolution propre : c'est un arbitrage entre friction de contribution et surface de risque, à négocier selon le contexte de l'organisation.
