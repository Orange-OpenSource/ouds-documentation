---
type: concept
tags: [ia, design-system, gouvernance, agentic, contrat, role-designer]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)"
related:
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[protocole-arc](protocole-arc.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
---

## User vs Maintainer : la frontière qui définit "agentique"

La distinction User/Maintainer est le critère analytique proposé par [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) pour définir précisément ce qui rend un design system "agentique" ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)). Elle répond à l'objection formulée par Adrián Carranco : si l'IA consomme simplement le design system comme un développeur le ferait, pourquoi parler de système agentique plutôt que d'une bibliothèque mieux indexée ?

## La distinction

Un **User** (humain ou IA) demande : "Comment j'utilise ce composant ?"
Un **Maintainer** demande : "Est-ce que ce composant devrait exister ?"

Le User lit la documentation et implémente. Le Maintainer audite la structure, identifie la dette, et fait respecter les contrats architecturaux.

## Quand l'IA franchit la ligne

L'IA franchit la frontière User → Maintainer au moment où elle ne lit plus le design system mais le *fait respecter*. Exemple précis : quand le système signale que "les classes CSS `.pill-alt` dupliquent la fonctionnalité du composant `Tag`", il ne répond pas à une question d'usage — il enforce un contrat architectural que l'auteur avait écrit mais ne suivait plus. Ce n'est plus de la consommation. C'est de la gouvernance ([towards-agentic-design-system](../sources/towards-agentic-design-system.md)).

La question de Carranco sur si l'agent devient "partie du cerveau" dès lors qu'il modifie le système reçoit une réponse précise : les fichiers `.metadata` *sont* le cerveau. Ils encodent les décisions d'architecture, les patterns d'usage, les anti-patterns. L'IA opérationnalise ce cerveau — le rend actif au lieu de passif.

## Implication pour la définition d'"agentique"

Un design system n'est pas agentique parce qu'il est mieux documenté pour l'IA. Il le devient quand l'IA peut passer du mode User au mode Maintainer — détecter les dérives par rapport aux contrats définis, les signaler, et (dans la phase 3 du [protocole-arc](protocole-arc.md)) proposer ou appliquer les correctifs. C'est à ce moment que "agentique" cesse d'être aspirationnel et devient opérationnel.

## ⚡ Tension / Contradiction

Cette distinction suppose que les "contrats architecturaux" sont explicitement encodés dans les metadata. Si les metadata ne contiennent que des descriptions d'usage et non des règles normatives ("ne pas utiliser `.pill-alt` si `Tag` existe"), l'IA ne peut pas détecter la dérive — elle peut seulement décrire l'état actuel. La frontière User/Maintainer ne se franchit que si les metadata files encodent des *normes*, pas seulement des *descriptions*.

## La même frontière pour le designer humain

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) étend la distinction User/Maintainer au rôle du designer lui-même dans la partie 6 de la série ([encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)). Avant l'infrastructure de gouvernance, le designer *est* le Maintainer — chaque décision de cohérence passe par lui, chaque revue de PR qui viole une convention nécessite son regard. Il est "la seule source de vérité sur ce qui est correct". C'est un goulot d'étranglement et un point de dérive : quand une deuxième personne commence à construire des composants, la connaissance reste dans la tête du designer pendant que le système continue de croître.

La gouvernance encodée opère le même glissement pour le designer que pour l'IA : il cesse d'être User/Maintainer à la demande (répondre aux questions, corriger les violations) pour devenir l'auteur des conditions sous lesquelles le système se maintient lui-même. La formulation de l'article : "From designer who delivers to designer who guarantees." Voir [concevoir-les-conditions](concevoir-les-conditions.md) pour la dimension épistémique de ce passage.

## Le défi épistémique du maintainer humain

Encoder des règles de gouvernance requiert d'articuler ce qu'on savait inconsciemment. Le designer-Maintainer suit des règles qu'il n'a jamais formalisées — "les dropdowns prennent l'élévation level 3", "foreground-muted est réservé aux éléments secondaires" — parce qu'elles ont été intériorisées pendant des années de pratique. Les rendre exécutables, c'est les rendre explicites pour la première fois. C'est un travail épistémique, pas seulement technique : il faut savoir *pourquoi* une règle existe pour savoir *comment* l'encoder.

Cette articulation est ce qui distingue une gouvernance superficielle (linter d'existence) d'une gouvernance profonde (détection d'intent). Voir [existence-vs-intent-violations](existence-vs-intent-violations.md) pour la matérialisation concrète de cette distinction.
