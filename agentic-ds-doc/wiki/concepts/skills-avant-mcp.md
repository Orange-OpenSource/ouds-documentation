---
type: concept
tags: [skills, mcp, stratégie, ia, design-system, claude-code, itération, miro]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)"
related:
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[architecture-skills-rules-instructions](architecture-skills-rules-instructions.md)"
  - "[eddie-machado](../entities/eddie-machado.md)"
  - "[aura-miro](../entities/aura-miro.md)"
---

## Skills avant MCP

"Skills avant MCP" désigne la stratégie de développement proposée par [eddie-machado](../entities/eddie-machado.md) chez Miro : construire un nouvel outil d'abord comme Claude Code skill, l'optimiser, et le porter en outil MCP uniquement si la stabilité et le partage systémique le justifient ([miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)).

## Le raisonnement

Les outils MCP nécessitent un cycle de développement plus long, une infrastructure déployée, et un maintien dans le temps. Les Claude Code skills sont des fichiers de contexte locaux — plus rapides à écrire, triviaux à modifier, testables immédiatement. La séquence skills-first inverse la tendance naturelle des équipes à sur-ingénierer le MCP dès le départ.

## La preuve par les chiffres

[eddie-machado](../entities/eddie-machado.md) documente le cas du skill `search icons` chez Miro. Quand le MCP a atteint ses limites sur la recherche d'icônes (la doc interne est rendue en React et non crawlable par les agents), il a construit le skill directement. Puis il l'a compressé avec la commande `/simplify` de Claude Code. Résultat : **33 000 tokens → 410 tokens, soit 98 % de réduction**. "Look at this, that's 98% fewer tokens scaled across the company." Un skill à 410 tokens servi à l'ensemble des 48+ product teams de Miro représente une économie structurelle significative à chaque appel.

Le même processus a été appliqué à `search tokens`, et au `wrap-up` skill pour la création de PRs.

## La grille de décision

| Pattern | Quand l'utiliser |
|---------|-----------------|
| Claude Code skill | Workflow spécifique, besoin d'itérer vite, outil local ou semi-local, chemin le plus rapide vers la première valeur |
| Outil MCP | Capacité stable, à partager entre de nombreux agents et IDEs, justifiant un cycle de build plus long |

Le critère central : un skill peut toujours être porté en MCP plus tard. Un MCP sur-ingéniéré trop tôt bloque l'itération et fige des décisions prématurées.

## Lien avec l'architecture Skills/Rules/Instructions

Cette stratégie est cohérente avec le cadre de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) dans [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md) : les Skills sont définis comme des capacités exécutables réutilisables, distinctes des Rules (contexte passif) et des Instructions stratégiques (routeur). La nouveauté de Miro est la séquence : skill d'abord comme prototype, MCP ensuite comme industrialisation. Le point d'entrée est délibérément local et itérable.

## La commande /simplify

La commande `/simplify` de Claude Code est mentionnée explicitement comme outil de compression des skills. Elle prend un skill verbeux et en produit une version sémantiquement équivalente mais plus courte. La réduction de 33 000 à 410 tokens sur le skill `search icons` illustre l'ordre de grandeur possible. Cette étape de compression est partie intégrante de la stratégie skills-first : on écrit d'abord pour la clarté, on compresse ensuite pour l'économie.

## ⚡ Tension avec la priorisation MCP

La stratégie skills-first est pragmatique mais crée une tension avec la vision de [diana-wolosin](../entities/diana-wolosin.md) et [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) : ceux-ci traitent le MCP comme l'infrastructure de référence pour servir les métadonnées structurées à l'agent. Un skill local riche en logique n'est pas partagé automatiquement avec tous les agents de l'organisation — il reste dans l'environnement Claude Code de l'utilisateur. Pour une petite équipe qui itère, c'est un avantage. Pour une infrastructure systémique servant 48+ product teams, le skill doit finir par être porté en MCP ou distribué via un autre mécanisme. La stratégie de Miro n'est pas une alternative au MCP — c'est une antéchambre.
