---
type: concept
tags: [gouvernance, design-system, ia, tokens, auditeur, intent, linter]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[encoding-governance-agentic-design-systems]]"
related:
  - "[[intent-token]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[concevoir-les-conditions]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[lisibilite-machine-design-system]]"
---

## Existence vs violations d'intent

La distinction existence/intent est la contribution conceptuelle centrale de la partie 6 de la série de [[cristian-morales-achiardi]] ([[encoding-governance-agentic-design-systems]]). Elle formalise la différence entre deux niveaux de vérification d'un design system par un agent IA — et donc entre un linter et de la gouvernance réelle.

## La violation d'existence

Une violation d'existence est simple : un token référencé dans le code (`var(--color-blue-500)`) n'existe pas dans le système de tokens. Le composant compile. La PR passe la review. La couleur n'apparaît jamais dans le navigateur. Personne ne l'a attrapé — ni le développeur, ni l'IA, ni la code review — parce que rien ne vérifiait l'existence au moment de la génération. C'est le problème que résout la v1 d'un token auditor : scanner les CSS modules, matcher les `var(--*)` contre les fichiers JSON source, flaguer ce qui n'existe pas. 43 violations trouvées dans le cas Enara.

## La violation d'intent

Une violation d'intent est plus subtile : le token existe, mais son usage viole la logique du système. Exemples concrets documentés :

Utiliser `--foreground-muted` pour du body copy n'est pas une référence manquante — c'est la mauvaise position dans la hiérarchie visuelle. `--foreground-muted` est conçu pour les éléments secondaires, pas pour le contenu principal. Le token est valide syntaxiquement ; son usage est sémantiquement incorrect.

Un dropdown avec une ombre `rgba` personnalisée ne casse pas la syntaxe — il contourne une décision d'élévation. Le design system a des tokens d'élévation qui encodent la hiérarchie des surfaces. Une valeur custom court-circuite cette hiérarchie même si elle est visuellement similaire.

Ces violations sont invisibles à v1. Elles ne sont détectées que si le système connaît non seulement quels tokens existent, mais *quel rôle* ils jouent dans la hiérarchie visuelle et les patterns d'usage attendus.

## La formule

"v1 checked existence. v2 checks intent. The difference between those two things is the difference between a linter and governance" ([[encoding-governance-agentic-design-systems]]). Un linter vérifie la syntaxe et l'existence. La gouvernance vérifie la sémantique et l'intent — ce qui requiert que les règles d'intent soient encodées de manière exécutable dans le système.

## Ce que ça implique pour l'infrastructure

Pour détecter les violations d'intent, l'auditeur doit avoir accès à la couche de raisonnement (couche 3 des [[trois-couches-composants-agents]]) et à l'[[intent-token]] encodé. Il ne suffit pas de lister les tokens valides — il faut documenter leur rôle dans la hiérarchie, leurs contextes d'usage légitimes, et les patterns qu'ils ne doivent pas remplacer. C'est exactement le type de connaissance que [[concevoir-les-conditions]] cherche à rendre exécutable.

## ⚡ Tension avec la lisibilité machine standard

La plupart des approches de [[lisibilite-machine-design-system]] se concentrent sur la couche 1 (index) et la couche 2 (métadonnées d'usage). La détection des violations d'intent requiert une couche supplémentaire : les règles de hiérarchie et de cohérence entre tokens. Ce n'est pas documenté dans les métadonnées individuelles de composants — c'est une connaissance systémique sur les relations entre tokens et contextes. Le fossé entre "documenter les composants" et "encoder la grammaire visuelle complète" reste ouvert dans le vault.
