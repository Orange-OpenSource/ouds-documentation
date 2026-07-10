---
type: entity
tags: [personne, design-system, ia, miro, ingénierie, mcp, skills]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[[miro-ai-design-system-mcp-claude-code-skills]]"
related:
  - "[[andressa-lombardo]]"
  - "[[aura-miro]]"
  - "[[skills-avant-mcp]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[into-design-systems-conference]]"
---

## Eddie Machado

Design engineer chez Miro. Co-auteur, avec [[andressa-lombardo]], du projet [[aura-miro]]. Conférencier à l'AI Conference for Designers 2026 ([[into-design-systems-conference]]). Responsable de l'implémentation technique du MCP server, des Claude Code skills et des workflows de contribution agentique chez Miro.

## Contributions techniques documentées

**Le MCP server minimaliste.** Eddie a construit le MCP Miro avec deux outils seulement : `list components` (retourne la liste des composants) et `get component docs` (retourne la documentation d'un composant donné). Sa philosophie : "start simple, see how that works, then add more." La plupart des équipes sur-ingénièrent le MCP avant de savoir ce que designers et ingénieurs en ont réellement besoin.

**L'instruction de routage.** Plutôt que de laisser l'agent deviner quel MCP appeler parmi un stack chargé, Eddie a ajouté une instruction explicite dans le fichier Claude root de l'équipe, dirigeant Aura vers le MCP design system. Un seul ajout → chute de 70 à 80 % des questions Slack.

**La stratégie skills-first.** Face aux limites du MCP sur la recherche d'icônes et tokens (la doc interne Miro est rendue en React, les agents ne peuvent pas traverser les liens), Eddie a construit deux outils supplémentaires (`search icons`, `search tokens`) en Claude Code skills plutôt qu'en outils MCP. Raisonnement : les skills sont plus rapides à construire, plus faciles à itérer, et compressables avec `/simplify`. Il a ramené le skill de recherche d'icônes de 33 000 tokens à 410 tokens — une réduction de 98 %. "Look at this, that's 98% fewer tokens scaled across the company." Voir [[skills-avant-mcp]].

**Le wrap-up skill.** Eddie a écrit un skill qui automatise la création de PRs : lancer le linter, parcourir les checklists de qualité, d'accessibilité et de localisation, ajouter une ligne par commit, structurer le PR depuis un template. Le résultat : 17 PRs en une heure lors du premier bug-bash d'Aura. L'effet secondaire observé : "we see people more eager to contribute because there's less of a restriction now."

**L'amorce du workflow Jira.** L'équipe tag les tickets Jira "Aura ready". Aura scanne le ticket, exécute le travail, utilise le wrap-up skill et soumet le PR. C'est l'implémentation la plus concrète du rôle Maintainer dans le vault — l'agent comme contributeur autonome, pas seulement consommateur.

Sa formule sur les hallucinations : "She was not randomly wrong, she was confidently wrong" — et sa conclusion : "It wasn't Aura that was struggling. It was actually the fact that we didn't provide her enough context to get the job done."
