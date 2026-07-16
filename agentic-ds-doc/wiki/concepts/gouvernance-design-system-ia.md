---
type: concept
tags: [gouvernance, design-system, ia, index, infrastructure, organisation, bypass, formats]
created: 2026-06-17
updated: 2026-07-07
sources:
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)"
  - "[mapping-design-system-for-ai-agents](../sources/mapping-design-system-for-ai-agents.md)"
  - "[agent-orchestration-for-design-systems](../sources/agent-orchestration-for-design-systems.md)"
  - "[your-design-system-fragmenting-agent-files](../sources/your-design-system-fragmenting-agent-files.md)"
  - "[design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md)"
  - "[encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)"
  - "[design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)"
  - "[automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)"
  - "[your-design-system-is-not-ready-for-ai-agents](../sources/your-design-system-is-not-ready-for-ai-agents.md)"
  - "[agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md)"
  - "[state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)"
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
  - "[design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)"
related:
  - "[protocole-arc](protocole-arc.md)"
  - "[user-vs-maintainer-ia](user-vs-maintainer-ia.md)"
  - "[inversion-economique-code-comprehension](inversion-economique-code-comprehension.md)"
  - "[design-system-as-infrastructure](design-system-as-infrastructure.md)"
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[boucle-feedback-infrastructure](boucle-feedback-infrastructure.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[memoire-design-system](memoire-design-system.md)"
  - "[accountability-gap-ia](accountability-gap-ia.md)"
  - "[shadow-ia-design-system](shadow-ia-design-system.md)"
  - "[dispersion-decision-design](dispersion-decision-design.md)"
  - "[prompt-injection-design-system](prompt-injection-design-system.md)"
---

## Gouvernance du design system par l'IA

La gouvernance d'un design system désigne l'ensemble des processus qui permettent de maintenir la cohérence du système dans le temps : détecter les dérives, identifier la dette technique, faire respecter les conventions architecturales, et piloter l'adoption par les équipes.

Avec l'infrastructure agentique, l'économie de la gouvernance change radicalement. [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) le formule : "Governance shifts from 'expensive tax we can't afford' to 'byproduct we get for almost free'" ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)). Mais cette promesse repose sur quatre régimes distincts, chacun avec ses acteurs, ses mécanismes, et ses points d'échec propres.

La distinction fondamentale entre orchestration et gouvernance : "Orchestration is about capability. Governance is about trust." Un système peut être parfaitement orchestré et néanmoins produire de la dérive à grande échelle si la gouvernance n'est pas encodée ([encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)).

## Les quatre régimes

**[gouvernance-technique-ia](gouvernance-technique-ia.md)** — Les mécanismes automatisés opérant à l'intérieur du design system : auditeur de tokens v1/v2, gouvernance pré-génération, efficiency rate, niveaux de confiance par action, contraintes exécutables, mesure des hallucinations, les quatre risques de l'autonomie agentique. La couche la mieux documentée du corpus.

**[gouvernance-organisationnelle-ia](gouvernance-organisationnelle-ia.md)** — Les décisions humaines : droits décisionnels, standard de qualité explicite, accountability pour les failures composites, adaptation des modèles de contribution, politique IA légère, gouvernance par mandat plateforme. La couche la moins avancée dans la plupart des équipes.

**[gouvernance-bypass-shadow-ia](gouvernance-bypass-shadow-ia.md)** — La gouvernance des agents opérant *en dehors* du DS, sans connexion à l'infrastructure. 50 % des équipes DS signalent ce problème. La réponse n'est pas réglementaire mais économique : rendre le DS le chemin de moindre résistance pour les agents. Voir aussi [shadow-ia-design-system](shadow-ia-design-system.md) pour le détail des mécanismes.

**[gouvernance-coutures-formats-agents](gouvernance-coutures-formats-agents.md)** — L'ownership et la sécurité de la pile de formats agent-facing (AGENTS.md, SKILL.md, DESIGN.md, manifests Storybook, endpoints MCP). La page manquante jusqu'ici dans le vault. Les coutures entre ces formats sont le point de failure le plus ignoré : "There's no role on the org chart whose job is to keep the seams healthy." ([murphy-trueman](../entities/murphy-trueman.md))

## Limite commune aux quatre régimes

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) formule la limite fondamentale qui s'applique à l'ensemble : "The system can enforce what you encode. It can audit against rules you define. What it can't do is know that you encoded something wrong in the first place." ([human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md))

La gouvernance agentique n'est pas un système autonome — c'est un amplificateur de la rigueur des humains qui l'alimentent. La boucle humaine, documentée dans [gouvernance-technique-ia](gouvernance-technique-ia.md), est la condition de validité de toutes les autres couches.

## Le coût économique du mauvais contexte (Kavcic, 2026)

[romina-kavcic](../entities/romina-kavcic.md) apporte un éclairage macroéconomique sur les conséquences d'une mauvaise gouvernance de contexte ([design-system-advantage-is-memory](../sources/design-system-advantage-is-memory.md)). Les données convergent : Microsoft a annulé ses licences Claude Code dans son groupe Experiences + Devices, en partie pour des raisons financières (The Verge). Le CTO d'Uber a déclaré que son budget IA avait été "blown away already" (The Information). Bryan Catanzaro, VP Applied Deep Learning chez Nvidia, a déclaré que "pour mon équipe, le coût du compute dépasse déjà celui des employés" (Axios). Gartner prédit une baisse de 90% du coût des tokens d'ici 2030, mais note que les systèmes agentiques consomment 5 à 30 fois plus de tokens qu'un chatbot standard — la baisse unitaire ne compense pas la hausse volumétrique. METR documente que la longueur des tâches complétables par les agents à 50% de fiabilité double tous les 7 mois, ce qui signifie que chaque session nécessite plus de contexte et plus d'appels d'outils.

La conclusion pour la gouvernance du design system : un contexte partiel ou mal structuré n'est pas seulement une gêne opérationnelle. C'est une dépense structurelle récurrente — chaque re-découverte d'une décision déjà prise, chaque correction d'une recommendation incorrecte, chaque passage par un pattern rejeté se traduit en tokens brûlés à chaque session. La gouvernance du corpus de données est donc une question de gouvernance économique autant que de gouvernance technique. Voir [memoire-design-system](memoire-design-system.md) pour le détail conceptuel.
