---
type: concept
tags: [gouvernance, design-system, ia, audit, tokens, contraintes-executables, metriques, orchestration, infrastructure]
created: 2026-07-07
updated: 2026-07-16
sources:
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)"
  - "[mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)"
  - "[agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)"
  - "[encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)"
  - "[design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)"
  - "[automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)"
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
  - "[agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md)"
  - "[machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)"
  - "[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md)"
related:
  - "[ecriture-agents-canvas-design](ecriture-agents-canvas-design.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[gouvernance-organisationnelle-ia](gouvernance-organisationnelle-ia.md)"
  - "[protocole-arc](protocole-arc.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md)"
  - "[boucle-feedback-infrastructure](boucle-feedback-infrastructure.md)"
  - "[intent-token](intent-token.md)"
  - "[workflows-ia-metadata](workflows-ia-metadata.md)"
  - "[mode-exploration-vs-navigation](mode-exploration-vs-navigation.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[jan-six](../entities/jan-six.md)"
---

## L'ancienne et la nouvelle économie de la gouvernance

Sans infrastructure machine-readable, un audit de design system requiert qu'une personne parcoure manuellement la codebase, vérifie les imports, mène des enquêtes auprès des designers et développeurs, et rédige un document de synthèse. C'est un effort suffisamment lourd pour n'être réalisé qu'une fois par trimestre — et pour accumuler de la dérive entre deux audits ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)).

Avec une infrastructure machine-readable (métadonnées, index, protocols), [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) documente un coût de **0,20 $ en tokens** pour un rapport d'adoption complet, à la demande, avec la même méthodologie reproductible à chaque exécution. La formulation condensée : "Governance shifts from 'expensive tax we can't afford' to 'byproduct we get for almost free'" ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)). Ce n'est pas une amélioration marginale — c'est un changement de catégorie. La gouvernance à la demande change le rapport à la dette technique : au lieu de laisser la dérive s'accumuler entre audits trimestriels, les équipes peuvent détecter les problèmes en continu et établir une baseline mesurable.

## L'efficiency rate comme diagnostic

L'infrastructure agentique produit une métrique clé que les outils traditionnels ne peuvent pas générer : l'efficiency rate — le ratio entre le nombre d'imports d'un composant et son nombre réel d'instances ([agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)). Mais la valeur diagnostique va au-delà du ratio. [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) documente un cas où l'agent a correctement distingué dérive et philosophie : les composants Spacer et Container peu utilisés ne reflètent pas de la dérive, mais une préférence explicite pour les utility classes. L'agent a compris *pourquoi* les atomes étaient peu utilisés, pas seulement *qu'ils l'étaient*. Cette distinction — dérive intentionnelle vs involontaire — est la vraie valeur diagnostique que seule une infrastructure avec contexte encodé peut fournir.

## Gouvernance pré-génération

Un mécanisme de gouvernance émerge avec les [workflows-ia-metadata](workflows-ia-metadata.md) : la validation pré-génération ([design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)). Avant de générer du code, l'agent vérifie les `antiPatterns` encodés dans les métadonnées. Si une composition violerait un contrat déclaré, l'agent le détecte avant de produire le code — non après. C'est une forme de gouvernance proactive qui intervient plus tôt dans le flux que la détection de dérive post-hoc.

## La dette technique composée

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) affine le calcul de ROI avec le concept de dette technique composée ([mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)). L'analyse naïve compare le coût en tokens d'une session avec index contre sans index — l'index est légèrement plus cher. Cette comparaison est trompeuse. Sans carte, un agent en [mode Exploration](mode-exploration-vs-navigation.md) accumule un "drift tax" à chaque interaction : duplication, incohérence, faux négatifs. Chaque génération ajoute une couche de dette. L'index "front-load" ce coût : une "accuracy premium" payée une fois pour garantir zéro dérive. La métrique correcte n'est pas le coût de session — c'est le coût total de possession, dérive comprise.

## Lien avec le protocole ARC

La gouvernance technique correspond aux phases 2 (Report) et 3 (Compose) du [protocole-arc](protocole-arc.md). La phase 2 automatise les rapports d'audit. La validation pré-génération est une variante de la phase 2 appliquée en temps réel. La phase 3 automatise aussi la résolution : l'agent détecte la dérive et génère le correctif sans intervention manuelle.

## Orchestration vs gouvernance

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) précise la distinction ([encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)) : "Orchestration is about capability. Governance is about trust." L'orchestration fait fonctionner les agents dans le système. La gouvernance garantit que ce qu'ils construisent correspond à ce qui a été conçu. Un système peut être parfaitement orchestré et néanmoins produire de la dérive à grande échelle si la gouvernance n'est pas encodée.

## L'auditeur de tokens : de l'existence à l'intent

Le cas Enara documente la progression d'un token auditor en production ([encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)). L'auditeur v1 scanne les CSS modules, match les `var(--*)` contre les fichiers JSON source, et flagge les références inexistantes : 43 violations détectées. Mais v1 ne détecte que les violations d'existence. L'auditeur v2 détecte les violations d'intent : utiliser `--foreground-muted` pour du body copy est sémantiquement incorrect même si le token existe. v2 trouve 64 violations — 21 de plus que v1. Ces 21 violations existaient avant, invisibles à l'infrastructure. La différence entre v1 et v2 est la différence entre un linter et de la gouvernance réelle. Voir [existence-vs-intent-violations](existence-vs-intent-violations.md).

Le résultat en production : FilterBar, le composant le plus récent au moment de l'article, présente zéro violation — non parce que l'auditeur l'a corrigé, mais parce que l'environnement est suffisamment structuré pour que le chemin naturel soit le chemin correct.

## Le Level 4 comme gouvernance formalisée dans le produit

[romina-kavcic](../entities/romina-kavcic.md) documente une instance distincte de gouvernance IA ([design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)) : la Responsible AI rubric de Microsoft Fluent 2, qui constitue le [Niveau 4 du modèle de maturité](modele-maturite-ia-design-system.md). Cette rubrique évalue les features IA avec des critères d'auto-fail — des conditions bloquantes qui empêchent le déploiement en production. Le parallèle avec l'auditeur v2 est direct : les deux mécanismes vérifient non pas si quelque chose existe, mais si ce qui existe correspond à son intent.

## Le coût de la maintenance manuelle

Nielsen Norman Group (2022) documente que les contributeurs à un design system consacrent **plus de 40 % de leur temps à la maintenance** ([automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)). Ce chiffre est cohérent avec la thèse de [inversion-economique-code-comprehension](inversion-economique-code-comprehension.md) : si la compréhension est chère et le code est gratuit, le coût de la maintenance — qui est avant tout un travail de synchronisation — capture une part disproportionnée de la capacité des équipes. L'infrastructure agentique réduit directement cette fraction.

## Mesurer les hallucinations comme une métrique d'infrastructure

[diana-wolosin](../entities/diana-wolosin.md) formule un principe rarement explicité : "Measure hallucinations as a metric, not as a feeling" ([machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)). La fréquence à laquelle le MCP retourne des informations incorrectes doit être traitée comme un indicateur quantifiable, comparable à un taux de violation de tokens. Sans mesure des hallucinations, la dérive continue invisible. La gouvernance requiert un loop de mesure explicite sur la qualité des sorties du MCP, pas seulement sur la qualité de sa structure.

## Niveaux de confiance par action agentique

L'AI Design Systems Conference 2026 introduit un cadre granulaire : définir les niveaux de confiance **par action**, pas par agent ([your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)). La taxonomie proposée : auto-merge pour les corrections à faible impact (lint, typos, labels d'accessibilité), draft PR pour les changements de valeurs (tokens, descriptions), suggest only pour les décisions architecturales (nouvelles APIs, changements breaking). Ce cadre est développé dans [niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md).

[jan-six](../entities/jan-six.md) chez GitHub Primer implémente la version la plus conservative : les agents ne peuvent créer qu'une issue, jamais merger du code. Le niveau de confiance maximal est une contrainte de permission systèmes — une contrainte exécutable au sens de [concevoir-les-conditions](concevoir-les-conditions.md), non une orientation contournable par le prompt.

## Les quatre risques de l'autonomie agentique

[romina-kavcic](../entities/romina-kavcic.md) articule dans [agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md) un inventaire de risques propres à la configuration agentique — ils apparaissent précisément quand le système *fonctionne* mais sans gouvernance adéquate.

**Design debt à vitesse machine.** L'IA n'améliore pas les systèmes faibles — elle les amplifie. "Bad metadata creates bad output faster." La dette s'accumule en heures plutôt qu'en semaines.

**Fausse confiance dans la documentation générée.** Les agents produisent de la documentation qui *sonne* correcte même quand elle est fausse. La documentation d'un design system est de l'instruction, pas du contenu — des instructions fausses formulées avec assurance sont pires qu'une absence.

**Manipulation UX par l'adaptation runtime.** L'adaptation contextuelle est légitime. Quand elle se fonde sur la vulnérabilité comportementale inférée de l'utilisateur, elle franchit une frontière. "Agentic design systems will need ethics, permissions, audit trails, and product principles. Otherwise, adaptive UI becomes manipulation with better tooling." Ce risque requiert une gouvernance éthique, absente de la plupart des cadres documentés.

**Governance gaps structurels.** Une gouvernance agentique complète requiert : règles d'approbation, logs d'audit, mécanismes de rollback, niveaux de permission, gates de test, modèles d'ownership, chemins d'escalade. L'absence de l'un transforme "agentique" en "non contrôlé". Voir [niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md) et [concevoir-les-conditions](concevoir-les-conditions.md).

## Contraintes exécutables

Les règles doivent passer de descriptives à exécutables. Une page qui dit "utiliser `--foreground-primary` pour le body copy" est lue, oubliée, contournée. Une contrainte encodée dans l'auditeur est appliquée automatiquement à chaque composant généré, par chaque agent. Ce n'est pas une nuance technique — c'est une différence de régime. Les contraintes exécutables sont la matérialisation de [concevoir-les-conditions](concevoir-les-conditions.md) : on conçoit les conditions sous lesquelles les interfaces se construisent correctement, pas les interfaces elles-mêmes.

## La boucle humaine : condition de validité de la gouvernance technique

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) formule la limite fondamentale de cette couche dans [human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md) : "The system can enforce what you encode. It can audit against rules you define. What it can't do is know that you encoded something wrong in the first place."

L'exemple concret : l'échelle de jaune primitif incorrectement calibrée chez Enara. Le token auditor a confirmé que tous les tokens étaient correctement utilisés — l'erreur était dans les valeurs primitives elles-mêmes, une couche que l'auditeur n'audite pas parce qu'elle est la source de vérité. Ce qui a fermé la boucle, c'est un humain qui a fait confiance au système assez pour tracer le problème plutôt que le contourner. La gouvernance technique est un amplificateur de la rigueur des humains qui l'alimentent, pas un substitut à cette rigueur.

## La complétude comme métrique de sécurité (Victorino, mars 2026)

[victorino-design-governance-agent-era](../sources/victorino-design-governance-agent-era.md) déplace le regard de la gouvernance technique en amont de l'audit post-génération : quand un agent peut écrire directement dans le canvas Figma (voir [ecriture-agents-canvas-design](ecriture-agents-canvas-design.md)) et se contraint à n'utiliser que ce qui existe dans la bibliothèque de composants, la *couverture* du design system devient elle-même le mécanisme de gouvernance. Un système qui ne couvre que 60 % des patterns d'un produit laisse l'agent improviser les 40 % restants sans aucune contrainte structurelle. La couverture cesse d'être un OKR d'équipe design pour devenir une métrique de risque — un complément en amont aux auditeurs v1/v2 et aux contraintes exécutables déjà documentés dans ce concept, qui opèrent tous en aval de la génération.

## ⚡ Tension : "Le prompt gagne sur les guidelines" (Laura Fehre)

[laura-fehre](../entities/laura-fehre.md) introduit une limite empirique ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)) : "Writing more rules into a guideline file doesn't control the outcome. In nearly 100% of cases the prompt will win over the guidelines." Mais Fehre parle de guidelines en prose. Ce n'est pas le même registre que les contraintes exécutables — auditeurs de tokens, lint rules encodées en code — documentées ici. La tension est réelle mais délimitée. Une architecture de gouvernance robuste combine les Rules pour les orientations (ce que le LLM *tend* à faire), les contraintes exécutables pour les violations intolérables (ce qu'il *ne peut pas* faire), et le JSON structuré pour la précision de l'interprétation. Les trois couches sont complémentaires, pas substituables.
