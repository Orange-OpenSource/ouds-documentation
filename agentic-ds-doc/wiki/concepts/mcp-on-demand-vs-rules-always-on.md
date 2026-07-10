---
type: concept
tags: [mcp, rules, design-system, ia, fondations, architecture, plugin]
created: 2026-06-17
updated: 2026-06-22
sources:
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[design-systems-mcp-complete-guide]]"
  - "[[your-design-system-is-not-ready-for-ai-agents]]"
  - "[[atlassian-design-md-lessons]]"
related:
  - "[[mcp-model-context-protocol]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[ia-comme-utilisateur]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[diana-wolosin]]"
  - "[[laura-fehre]]"
  - "[[brad-frost]]"
  - "[[eddie-machado]]"
  - "[[aura-miro]]"
  - "[[design-md-format]]"
updated: 2026-06-26
---

## MCP on-demand vs Rules always-on

La distinction MCP on-demand / Rules always-on est la contribution opérationnelle centrale de [[diana-wolosin]] ([[machine-readable-design-systems-designing-for-ai-as-a-user]]). Elle nomme une asymétrie fondamentale entre deux types d'infrastructure IA que la plupart des équipes confondent — avec des conséquences visibles en production.

## La nature on-demand du MCP

Un MCP ne retourne que ce qu'on lui demande. Quand un agent reçoit le prompt "build me a card", il formule une requête vers le MCP ; la RAG cherche la similarité sémantique entre la requête et les métadonnées ; la base vectorielle retourne les informations sur la Card, peut-être sur le Button. Elle retourne *uniquement ce qui a été demandé*. La typographie, l'espacement, les couleurs — les fondations du design system — n'ont pas été appelées dans la requête. Elles ne sont donc pas retournées. Le LLM comble le vide avec ses propres hypothèses.

C'est ce qu'a documenté [[diana-wolosin]] après l'audit de Keith Weston sur un échantillon des 4 300 prototypes générés chez Indeed : composants corrects, fondations cassées. Violations de typographie, espacement inventé, palette de couleurs inexistante dans le design system, emojis à la place des icônes. Le MCP d'Indeed contenait toutes ces informations. Mais personne ne les avait demandées.

> "The MCP is on demand. It only returns fresh data about what you asked for. If the prompt says 'build me a card', it's going to give you information about the card and a button. But it's going to fully ignore the spacing, the typography, the colors, because that foundation knowledge wasn't called in the prompt."

## Les Rules comme contexte permanent

La solution n'est pas d'améliorer le MCP — c'est de comprendre que certains types de connaissance ne peuvent pas être on-demand. Les fondations du design system (typographie, espacement, couleurs, grille, élévation) doivent être *toujours actives*, pas récupérées à la demande. Elles sont le contexte permanent dans lequel toute génération se produit.

Les Rules (équivalent du fichier de règles dans un contexte d'agent) jouent ce rôle : elles sont injectées dans chaque session, sans qu'un prompt les appelle explicitement. Elles portent les décisions qui ne devraient jamais être optionnelles.

La règle de Diana : "Treat MCP as on demand, treat rules as always on, never confuse the two."

## Le problème des fondations

Le "problème des fondations" est la conséquence directe de la confusion MCP/Rules. Un MCP seul peut servir parfaitement la connaissance composant (props, variants, anti-patterns, accessibilité) tout en laissant les fondations complètement hors contexte — parce que les fondations ne sont jamais dans le prompt utilisateur. Le LLM génère alors des interfaces visuellement cohérentes au niveau composant mais incohérentes au niveau système.

Ce problème est asymétrique : il est invisible en développement (où les développeurs savent quelles fondations appliquer) et systématique en génération IA (où le modèle n'a pas ce contexte implicite).

## L'architecture plugin comme réponse

La réponse de Wolosin : une architecture en couches qu'elle appelle "plugin" — la combinaison de Rules (always-on, portent les fondations), MCP (on-demand, porte la connaissance composant), et AGENTS.md (porte les instructions de stratégie). Cette architecture correspond à ce que [[cristian-morales-achiardi]] documente sous [[architecture-skills-rules-instructions]] : les Rules sont les fichiers de contexte passif chargés par chemin de fichier, l'AGENTS.md est le routeur stratégique.

La différence est que Wolosin articule explicitement *pourquoi* chaque couche est nécessaire : pas pour des raisons architecturales abstraites, mais parce que sans les Rules always-on, les fondations sont systématiquement absentes des sorties IA.

## L'instruction de routage comme always-on minimal (Miro)

[[eddie-machado]] chez Miro documente l'implémentation la plus légère possible de la couche always-on : une seule instruction dans le fichier Claude root de l'équipe, indiquant à Aura d'utiliser le MCP design system pour toutes les questions composants ([[miro-ai-design-system-mcp-claude-code-skills]]). Résultat : chute de 70 à 80 % des questions Slack. Les ingénieurs obtenaient leurs réponses dans leur IDE sans devoir demander manuellement.

Ce cas illustre la distinction MCP/Rules à son niveau le plus simple. Sans l'instruction de routage, l'agent doit choisir parmi un stack de MCPs chargés — friction d'invocation, risque de mauvais MCP sélectionné, comportement variable. Avec l'instruction dans le fichier root — une forme de Rule always-on — l'agent sait systématiquement où aller pour les questions design system. La Rules couche n'a pas à être sophistiquée pour produire un effet mesurable.

## La formulation Brad Frost : progressive disclosure of context

[[brad-frost]] nomme le même problème depuis l'angle de la conférence IDS 2026 et propose un cadre en trois couches qu'il appelle "progressive disclosure of context" ([[your-design-system-is-not-ready-for-ai-agents]]) :

**Toujours actif** — les fondations du design system (échelle d'espacement, tokens de couleur, typographie, border-radius) sont injectées dans chaque prompt, sans être demandées. Ce sont les décisions qui ne doivent jamais être optionnelles.

**MCP on-demand** — les composants sont interrogés quand le prompt le requiert. L'agent formule une requête pour récupérer les métadonnées de Card, Button, Dialog — et uniquement ces éléments.

**AGENTS.md comme couche d'orchestration** — un fichier unique qui déclare quelles règles sont always-on, où trouver le serveur MCP, et quels niveaux de confiance s'appliquent aux actions agentiques. C'est le routeur stratégique de l'ensemble, l'équivalent du CLAUDE.md de ce vault mais pour un design system.

Cette formulation est cohérente avec [[cristian-morales-achiardi]] ([[architecture-skills-rules-instructions]]) qui documente les Rules comme contexte passif always-on et les Skills/MCP comme capacités on-demand. La contribution de Frost est de nommer la couche AGENTS.md comme entité distincte et de la positionner comme l'interface entre les deux couches — non pas une règle de plus, mais le méta-document qui pilote la stratégie d'injection du contexte.

## ⚡ Tension : "Guidelines are not laws" (Laura Fehre)

La conférence IDS 2026 introduit une mise en garde empirique de [[laura-fehre]] qui pousse la distinction MCP/Rules encore plus loin : même les Rules always-on ne garantissent pas le résultat. "In nearly 100% of cases, the prompt will win over the guidelines." ([[design-systems-mcp-complete-guide]]). Si l'utilisateur formule un prompt qui contredit les Rules injectées, le LLM suit le prompt.

Cette observation ne contredit pas la nécessité des Rules — elle en précise la limite. Les Rules always-on réduisent les violations de fondations dans les cas normaux (quand le prompt ne les contredit pas). Mais elles ne constituent pas une contrainte exécutable au sens de [[concevoir-les-conditions]] : elles ne bloquent pas, elles orientent. La distinction est nette : une Rule qui dit "utilise le token de couleur primaire" sera contournée si le prompt dit "utilise du rouge". Un auditeur de tokens ([[existence-vs-intent-violations]]) qui bloque la génération quand `rgba()` hardcodé est détecté, non.

Fehre semble indiquer que le seul vrai contrôle est structurel : des données JSON explicites (le "contrat") résistent mieux aux déviations de prompt que des règles en prose. Ce qui rejoint la conclusion du benchmark Wolosin — JSON beats Markdown — mais étend l'argument de la précision vers la robustesse comportementale.

## Validation empirique : DESIGN.md comme cas limite du all-at-once

[[atlassian-design-md-lessons]] fournit la preuve chiffrée la plus directe de ce qu'implique l'absence du mécanisme on-demand. DESIGN.md charge l'intégralité de son contenu en début de contexte — c'est sa définition même (un fichier, une session). Le résultat : 7,21M tokens moyens pour ~30% du contexte disponible, contre 3,75M tokens pour ~80% du contexte avec un MCP. En une phrase : charger moins en une fois coûte plus cher et livre moins qu'interroger plus en plusieurs fois.

La raison est mécanique. Pour que le fichier reste dans des limites raisonnables (80 KB soit ~19 800 tokens dans le cas Atlassian, pour un contenu total disponible de 2,5 MB), il faut couper — et ce qu'on coupe en premier, c'est précisément les fondations détaillées, les guidelines de composants, les tokens de faible fréquence. Soit exactement ce que la couche Rules always-on est censée garantir. DESIGN.md tente de jouer le rôle de Rules ET de MCP dans un seul fichier, et échoue sur les deux tableaux : trop volumineux pour être gratuit comme une Rule, trop statique pour être précis comme un MCP.

Cela reformule le problème de Diana Wolosin depuis l'autre angle : elle avait montré que MCP sans Rules laisse les fondations hors contexte. Le cas Atlassian montre que DESIGN.md sans séparation on-demand/always-on sature le contexte avec les fondations au détriment de la précision composant.

## ⚡ Tension avec l'approche pure-MCP

Cette distinction pointe une lacune dans la série de [[cristian-morales-achiardi]] : les parties 1 à 6 décrivent l'infrastructure MCP et les métadonnées composant, mais n'articulent pas explicitement le problème des fondations ni la nécessité d'une couche always-on pour les tokens et fondations. La partie 5 ([[architecture-skills-rules-instructions]]) introduit les Rules comme fichiers de contexte passif, mais sans nommer le problème des fondations que cette couche résout. Wolosin nomme le problème, Morales Achiardi fournit l'architecture — les deux se complètent.
