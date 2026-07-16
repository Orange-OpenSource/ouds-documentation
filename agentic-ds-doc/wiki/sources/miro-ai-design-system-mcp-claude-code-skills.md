---
type: source
tags: [design-system, ia, mcp, skills, metadata, miro, onboarding, gouvernance, benchmark]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[andressa-lombardo](../entities/andressa-lombardo.md)"
  - "[eddie-machado](../entities/eddie-machado.md)"
  - "[aura-miro](../entities/aura-miro.md)"
  - "[ia-comme-nouvelle-recrue](../concepts/ia-comme-nouvelle-recrue.md)"
  - "[skills-avant-mcp](../concepts/skills-avant-mcp.md)"
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[readable-vs-usable-token](../concepts/readable-vs-usable-token.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[into-design-systems-conference](../entities/into-design-systems-conference.md)"
  - "[sil-bormuller](../entities/sil-bormuller.md)"
---

## Miro AI Design System: MCP + Claude Code Skills Playbook

Article de [sil-bormuller](../entities/sil-bormuller.md), publié le 11 mai 2026. Synthèse du talk d'[andressa-lombardo](../entities/andressa-lombardo.md) et [eddie-machado](../entities/eddie-machado.md) à l'AI Conference for Designers 2026. Documente l'année de travail de l'équipe Miro (6 personnes, 48+ product teams) pour rendre leur design system opérable par une IA baptisée [aura-miro](../entities/aura-miro.md).

## Thèses principales

**L'IA comme nouvelle recrue, pas comme outil.** [andressa-lombardo](../entities/andressa-lombardo.md) et [eddie-machado](../entities/eddie-machado.md) reformulent le problème de l'IA dans un design system : non pas comment connecter un outil, mais comment embarquer une nouvelle recrue. Ils donnent un nom à l'IA (Aura), un profil de personnalité ("extrêmement enthousiaste, très capable, et extrêmement littérale"), et construisent pour elle le même matériel d'onboarding qu'ils construiraient pour un humain. Cette reformulation change ce qu'on priorise : pas des features IA flashy, mais la documentation et les métadonnées que tout nouveau venu (humain ou machine) aurait besoin.

**Les hallucinations sont un problème de contexte, pas de modèle.** Test concret : demander à Aura de construire une toolbar avec des éléments du design system Miro. Elle l'a faite "confidently wrong" — icônes incorrectes, token déprécié. Cause racine : un icon nommé selon sa forme visuelle alors qu'il sert une fonction différente ; un token de background deprecated sans signal lisible par la machine. Solution : trois champs de métadonnées par icon (description visuelle, cas d'usage, catégorie) + règle "do not use" explicite dans la description. Résultat : les mêmes prompts produisent des sorties correctes.

**Les skills Claude Code avant les outils MCP.** [eddie-machado](../entities/eddie-machado.md) propose une stratégie concrète : construire les nouveaux outils d'abord comme Claude Code skills, puis les porter en MCP si nécessaire. Raisons : les skills sont plus rapides à construire, plus faciles à itérer, et peuvent être compressés avec `/simplify`. Il a ramené un skill de recherche d'icônes de 33 000 tokens à 410 tokens (98 % de réduction). Voir [skills-avant-mcp](../concepts/skills-avant-mcp.md).

**L'instruction de routage dans le fichier Claude.** Un seul ajout dans le fichier Claude root de l'équipe — "utilise le MCP design system pour les questions composants" — a fait chuter les questions Slack du channel design system de 70 à 80 %. Les ingénieurs obtenaient leurs réponses dans l'IDE sans pinger le canal.

**Les docs client-side rendues bloquent les agents.** Quand Aura cherchait des icônes ou tokens spécifiques, elle entrait dans des boucles. Cause : la documentation interne de Miro rend les liens de librairie en React, pas en Markdown. Les agents ne peuvent pas les traverser. Conséquence opérationnelle : rendre les index de librairies en Markdown, pas en React.

**Mesurer les questions qu'on n'a plus à répondre.** Quand le MCP fonctionne bien, il devient invisible — les calls se font en background, le call count s'efface des dashboards. La bonne métrique : volume de questions support dans le canal Slack, time-to-answer, contributions depuis l'extérieur de l'équipe core. "Any figure is better than no figure."

**La leçon de gouvernance interne.** L'équipe a été évaluée "4 sur 10 en impact" par un senior leader parce que le travail de métadonnées et documentation n'était "pas fancy". Ils ont continué. La formule d'[andressa-lombardo](../entities/andressa-lombardo.md) : "Prove the concept first. Explain it second." — non pas par naïveté mais parce que le MCP ne fonctionne que sur ce qu'Aura peut lire, et ce qu'elle peut lire est aussi bon que ce que quelqu'un a écrit.

## Citations clés

"If we didn't figure out how to make AI work within our system, somebody else was going to do it without us." ([eddie-machado](../entities/eddie-machado.md))

"She was not randomly wrong, she was confidently wrong." ([eddie-machado](../entities/eddie-machado.md) sur Aura)

"It wasn't Aura that was struggling. It was actually the fact that we didn't provide her enough context to get the job done." ([eddie-machado](../entities/eddie-machado.md))

"You don't need a perfect system. You need a system that is legible enough to teach." ([andressa-lombardo](../entities/andressa-lombardo.md))

"Prove the concept first. Explain it second." ([andressa-lombardo](../entities/andressa-lombardo.md))

## Ce que cette source apporte au vault

Source de production unique dans son registre : le vault contient beaucoup de cadres conceptuels (Morales Achiardi, Wolosin) et de benchmarks (Indeed, Spotify). Miro est différent — c'est le récit d'une équipe petite (6 personnes) qui a avancé pas à pas sur un an, raté, ajusté, et documenté les ajustements concrets. Les concepts nouveaux : [ia-comme-nouvelle-recrue](../concepts/ia-comme-nouvelle-recrue.md), [skills-avant-mcp](../concepts/skills-avant-mcp.md), [metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md). Les confirmations empiriques : le do-not-use en métadonnées fonctionne sur les icônes (étend [readable-vs-usable-token](../concepts/readable-vs-usable-token.md) au-delà des tokens), l'instruction de routage dans le fichier Claude est l'implémentation la plus légère de [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md), et le client-side rendering est un bloqueur concret documenté en production.
