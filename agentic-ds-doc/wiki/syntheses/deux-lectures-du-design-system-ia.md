---
type: synthesis
tags: [design-system, ia, synthèse, agentique, documentation, distinction, lecture]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)"
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)"
  - "[quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
---

## Deux lectures du design system IA

Le corpus du vault contient une ambiguïté productive : le terme "design system et IA" peut désigner deux objets radicalement différents. Les confondre produit des conclusions erronées. Les distinguer clairement révèle deux champs complémentaires mais non interchangeables.

## Lecture A : Le design system opéré par des agents IA

La lecture dominante dans le corpus — portée par [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md), [diana-wolosin](../entities/diana-wolosin.md), et la majorité des articles de [romina-kavcic](../entities/romina-kavcic.md) — traite de la question suivante : **comment rendre un design system compréhensible et opérable par des agents IA ?**

Dans cette lecture, l'IA est l'utilisateur (ou le mainteneur) du design system. Les humains ont créé le système ; l'IA s'en empare pour composer des interfaces, auditer la cohérence, générer des tokens, détecter des dérives. La question centrale est celle de la [lisibilité machine](../concepts/lisibilite-machine-design-system.md) : quelles structures de données, quels formats, quelles métadonnées permettent à un agent de naviguer le système avec précision et sans hallucination ?

Les concepts produits par cette lecture : [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md), [schema-metadata-composant](../concepts/schema-metadata-composant.md), [mcp-model-context-protocol](../concepts/mcp-model-context-protocol.md), [knowledge-graph-design-system](../concepts/knowledge-graph-design-system.md), [protocole-arc](../concepts/protocole-arc.md), [user-vs-maintainer-ia](../concepts/user-vs-maintainer-ia.md), [existence-vs-intent-violations](../concepts/existence-vs-intent-violations.md), [concevoir-les-conditions](../concepts/concevoir-les-conditions.md). La gouvernance ici est la gouvernance *du* système par l'IA — l'IA comme vérificateur de cohérence, auditeur de tokens, mainteneur des contrats d'architecture.

## Lecture B : Le design system qui documente les fonctionnalités IA pour les humains

L'article "Design Systems That Document AI" ([design-systems-that-document-ai](../sources/design-systems-that-document-ai.md)) introduit une lecture différente : **comment un design system documente-t-il les patterns d'interface pour les fonctionnalités IA destinées aux utilisateurs humains ?**

Dans cette lecture, l'IA est le contenu documenté, pas l'opérateur du système. Les équipes produit intègrent des fonctionnalités IA dans leurs interfaces (suggestions, génération de texte, classification, recommandations). Le design system doit fournir les composants, les tokens, les guidelines et les patterns d'interaction nécessaires pour que ces fonctionnalités soient implémentées de manière cohérente, accessible, et éthique.

Les concepts produits par cette lecture : [modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md) (comment les systèmes progressent de 0 à 5), [quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md) (les quatre règles universelles de l'interface IA/humain), le value gate (permission de ne pas utiliser l'IA). La gouvernance ici est la gouvernance *des fonctionnalités IA dans le produit* — assurer que les features IA respectent des standards éthiques, d'accessibilité, et d'expérience.

## Pourquoi la distinction est structurellement importante

Un système peut être au niveau 5 de la Lecture B (infrastructure Copilot UI Kits cross-platform comme Microsoft Fluent) tout en étant au niveau 0 de la Lecture A (aucune métadonnée machine-readable, aucun agent opérant le système). Et inversement : un système peut avoir un agent parfaitement capable d'auditer ses tokens et de composer des interfaces (Lecture A, Phase 2 du [protocole-arc](../concepts/protocole-arc.md)) sans documenter une seule règle pour les features IA intégrées dans les produits (Lecture B, Niveau 0 du [modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)).

La confusion entre les deux lectures produit des malentendus concrets. Quand [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) parle de "gouvernance IA", il parle de maintenir la cohérence architecturale du design system via un agent. Quand [romina-kavcic](../entities/romina-kavcic.md) parle de "gouvernance IA" dans l'article analysé ici, elle parle de la rubrique Responsible AI de Microsoft Fluent — un mécanisme de contrôle des features IA avant leur déploiement. Ce sont deux régimes de gouvernance, deux boucles de responsabilité, deux instruments distincts.

## La zone de convergence

Les deux lectures partagent néanmoins un terrain commun. La [règle 3 de l'interface IA](../concepts/quatre-regles-ia-ux.md) ("humain en contrôle") et la distinction [user-vs-maintainer-ia](../concepts/user-vs-maintainer-ia.md) de Morales Achiardi partagent la même philosophie : l'IA ne doit jamais retirer à l'humain le contrôle final, qu'il s'agisse d'un utilisateur face à une suggestion IA dans un produit ou d'un designer face à un agent qui propose un refactoring de tokens. La valeur éthique est la même ; le contexte technique est différent.

De même, le value gate (Lecture B) — la permission de ne pas utiliser l'IA — résonne avec la distinction entre [mode-exploration-vs-navigation](../concepts/mode-exploration-vs-navigation.md) dans la Lecture A : un design system bien conçu permet à l'agent de naviguer, mais ne l'y oblige pas si le contexte ne le justifie pas. Les deux principes accordent la primauté à la pertinence contextuelle sur l'automatisation systématique.

## Implication pour la lecture du vault

Le vault couvre les deux lectures, avec un ratio fortement asymétrique : la Lecture A (agents opérant le DS) représente 8 des 9 sources ingérées. La Lecture B (DS documentant les features IA pour humains) est introduite par un seul article, mais ouvre un champ entier non encore exploré : quels patterns d'interaction les équipes devraient-elles implémenter pour les features IA ? Comment évaluer leur maturité éthique ? Quels composants sont nécessaires ?

[GAP] : Le vault ne contient actuellement aucune source sur l'implémentation concrète des [quatre-regles-ia-ux](../concepts/quatre-regles-ia-ux.md) dans un produit réel, ni sur la construction de composants de niveau 2 ou 3 du [modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md). C'est un blanc dans le corpus.
