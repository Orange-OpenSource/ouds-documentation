---
type: concept
tags: [audit, tokens, playwright, ia, automatisation, test, drift, accessibilite, design-system, continu]
created: 2026-07-06
updated: 2026-07-06
sources:
  - "[[20-ai-workflows-design-system-teams]]"
related:
  - "[[architecture-skills-rules-instructions]]"
  - "[[metriques-adoption-ia-design-system]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[boucle-feedback-infrastructure]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[bypass-patterns-comme-user-research]]"
---

## Audit continu avec Playwright et agents IA

La plupart des équipes de design system font leurs audits manuellement, juste avant une release majeure : ils identifient des problèmes, les mettent dans un backlog, et n'y reviennent pas avant la prochaine release. C'est un cycle d'accumulation de dette, pas de maintenance. Le pattern Playwright + agents IA propose une alternative : des audits qui tournent en continu, sans intervention manuelle ([[20-ai-workflows-design-system-teams]]).

## Le pattern Planner / Generator / Healer

L'intégration MCP de Playwright introduit trois agents distincts aux responsabilités séparées.

Le **Planner** explore le Storybook ou le site de documentation et crée des scénarios de test — il comprend la structure du design system et génère une stratégie de couverture. Le **Generator** écrit le code de test réel en interagissant directement avec les composants — il traduit les scénarios en assertions exécutables. Le **Healer** répare automatiquement les tests cassés quand les composants changent — il évite que les changements légitimes invalident l'ensemble de la suite de tests.

La séparation des rôles est délibérée : le Planner raisonne sur la structure, le Generator traduit en code, le Healer maintient dans le temps. Aucun des trois ne fait le travail des deux autres.

## Ce que ces agents auditent

Cinq catégories d'audit deviennent automatisables avec ce pattern.

**Token consistency audit** : scanner les composants rendus pour détecter les valeurs hardcodées. Un agent peut comparer les valeurs CSS réelles utilisées dans le DOM rendu avec les tokens attendus — une méthode plus fiable qu'un simple grep statique, car elle capture les valeurs calculées et les héritages.

**Component behavior testing** : navigation clavier, gestion du focus, comportements d'interaction. Ces tests sont typiquement écrits une fois et jamais mis à jour ; le Healer change ça.

**Accessibility checks** : rôles ARIA, ratios de contraste, labels pour les lecteurs d'écran. Playwright peut calculer les ratios réels depuis le navigateur rendu, pas des estimations à partir du code source.

**Documentation accuracy** : l'agent peut comparer ce que le composant fait réellement (states, variants, props acceptées) avec ce que la documentation décrit. Le gap entre doc et composant est l'une des sources de confusion les plus fréquentes pour les équipes consommatrices.

**Visual regression** : comparaisons de screenshots entre thèmes et viewports. Utile notamment pour détecter les régressions lors des migrations de tokens.

## Relation avec les Skills

Ce pattern est complémentaire aux [[architecture-skills-rules-instructions]] mais opère à un niveau différent. Les Skills définissent les règles de génération et de validation *dans les prompts*. Le pattern Playwright exécute les vérifications *sur le composant rendu dans un navigateur*. L'un est statique (analyse du code), l'autre est dynamique (audit du comportement).

Une [[boucle-feedback-infrastructure]] complète combine les deux : les Skills définissent les règles, Playwright vérifie leur application dans le rendu.

## Ce que ce pattern change

L'équipe core arrête de catcher des problèmes de niveau checklist dans les revues et se concentre sur les questions difficiles (patterns d'interaction, nommage, architecture), pendant que Playwright gère la liste de vérification. La maintenance des composants existants devient moins coûteuse : les régressions sont détectées immédiatement, pas lors de la release suivante.

La clé est la continuité. Un audit fait une fois avant release produit un backlog. Un audit qui tourne à chaque PR produit une maintenance.
