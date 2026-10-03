---
type: concept
tags: [gouvernance, accountability, ia, design-system, accessibilite, responsabilite, composite-failure, traçabilité]
created: 2026-07-06
updated: 2026-07-16
sources:
  - "[design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md)"
  - "[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md)"
  - "[amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md)"
related:
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[murphy-trueman](../entities/murphy-trueman.md)"
  - "[accessibilite-continue](accessibilite-continue.md)"
  - "[shadow-ia-design-system](shadow-ia-design-system.md)"
  - "[shadow-code](shadow-code.md)"
  - "[modele-accountability-trois-couches](modele-accountability-trois-couches.md)"
  - "[niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
  - "[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md)"
---

## L'accountability gap de l'IA générative

L'accountability gap désigne le vide de responsabilité qui apparaît quand une interface est générée par l'IA à partir d'un design system : personne n'a fait de choix délibéré, mais quelqu'un doit répondre quand ça se trompe. [murphy-trueman](../entities/murphy-trueman.md) formule le problème dans [design-system-ai-ready-organisation-not](../sources/design-system-ai-ready-organisation-not.md) : "Your existing accountability structures were designed for human authors with legible intent — not for outputs where nobody made a deliberate choice."

## La structure du problème

Dans un workflow humain classique, l'accountability est traçable. Quand un designer compose une interface, il y a un auteur, un intent, une conversation possible sur les décisions prises. Le processus de review critique des choix de craft : on peut interroger l'auteur sur pourquoi il a fait telle hiérarchie, pourquoi cet ordre d'information, pourquoi ce traitement des edge cases.

Quand l'interface est générée par IA, cette traçabilité disparaît. Le PM qui a prompté n'a pas fait de choix de composition — il a demandé un résultat. L'IA n'a pas d'intent, seulement des outputs. Le résultat peut passer tous les contrôles automatiques existants (tokens corrects, composants documentés, règles de nommage respectées) et rester médiocre ou défaillant sur des dimensions que les vérifications automatiques ne capturent pas.

## Le cas de l'accessibilité composite

Le cas le plus documenté de l'accountability gap est l'accessibilité ([murphy-trueman](../entities/murphy-trueman.md)) : des composants peuvent être accessibles en isolation et produire un tout inaccessible. L'accessibilité n'est pas seulement une propriété des éléments individuels — c'est une propriété des relations entre éléments, du flux cognitif, de l'ordre de navigation, du contexte d'usage. Un agent peut assembler des parties accessibles en un parcours inaccessible. "That's not a hypothetical edge case. It's the kind of failure that compounds at speed when no single person feels responsible for the composite experience."

C'est la même logique que [existence-vs-intent-violations](existence-vs-intent-violations.md) transposée à l'échelle de l'interface : les éléments *existent* correctement mais leur assemblage viole l'*intent* de l'expérience. La différence est que l'auditeur de tokens v2 peut détecter les violations d'intent sur les tokens ; aucun outil existant ne détecte systématiquement les violations d'intent sur la composition d'interface.

## Les modes de failure composite

Trueman identifie plusieurs modes qui échappent aux contrôles automatiques actuels :

Un bouton on-brand dans un flux off-brand — le composant est conforme, le contexte ne l'est pas. Un composant correct dans une hiérarchie confuse — la pièce est bonne, l'architecture de l'information est défaillante. Une interface techniquement valide avec un modèle mental fondamentalement cassé — aucune violation de règle, une mauvaise décision produit. Dans chaque cas, "AI-generated work cleared every automated check" parce que les contrôles existants ont été conçus pour valider des propriétés locales, pas des propriétés émergentes de la composition.

## Le vide d'ownership

Le gap structurel : qui est responsable de ces failures composites ? Trueman documente quatre candidats et l'absence de réponse claire dans la plupart des organisations : l'équipe design system (qui a construit les composants), la personne qui a prompté l'IA (qui a utilisé le résultat), l'ingénieur qui a implémenté (qui a déployé), le QA (qui n'a pas détecté). En l'absence de décision explicite, la responsabilité se dilue entre les quatre — ce qui signifie en pratique qu'elle n'appartient à personne.

"This will land on someone's desk. As AI-generated interfaces start shipping in production, someone will have to answer for the failures they produce. It's better to decide now whose desk that is, under what circumstances, and with what escalation path." ([murphy-trueman](../entities/murphy-trueman.md))

## Ce que ça requiert

L'accountability gap ne se résout pas techniquement — il se résout organisationnellement. Les décisions à prendre avant d'en avoir besoin : à qui appartient la responsabilité des outputs IA en production, est-ce que le seuil de review varie selon la nature du changement (contenu vs nouveau flux vs refonte de parcours), quel est le chemin d'escalade quand la responsabilité est ambiguë. Ces décisions doivent être stables avant d'être sous pression de deadline et d'enjeux stakeholders.

La connexion avec [niveaux-confiance-actions-agentiques](niveaux-confiance-actions-agentiques.md) est directe : le niveau de confiance accordé à un output agentique détermine implicitement qui en est responsable. Un output auto-mergé (niveau 1) appartient au système. Un output en draft PR (niveau 2) appartient à l'équipe qui le valide. Un output "suggest only" (niveau 3) appartient au décideur humain. Sans cette décision explicite par type d'output, le gap reste entier.

## ⚡ Tension : la vitesse comme amplificateur

Le corpus existant documente que l'IA accélère la génération d'interfaces. L'accountability gap révèle que la vitesse est aussi l'amplificateur du risque : plus la création est rapide, plus les failures composites s'accumulent vite avant que quelqu'un les détecte. La gouvernance technique (auditeurs, constraints exécutables) ne suffit pas — elle valide des propriétés locales, pas la cohérence d'ensemble. La gouvernance organisationnelle (ownership clair, seuils de review, chemins d'escalade) est la seule réponse aux failures qui émergent à l'intersection des composants plutôt que dans chaque composant pris séparément.

## Le premier incident documenté : le cas Amazon (mars 2026)

Jusqu'ici, ce concept restait entièrement théorique dans le vault : Trueman décrit un scénario de défaillance composite plausible, mais aucune source ne documentait d'incident réel, nommé, chiffré. [amazon-vibe-coding-4-sev1-90-days](../sources/amazon-vibe-coding-4-sev1-90-days.md) comble ce trou, à une échelle différente de celle envisagée par Trueman : pas une interface individuelle inaccessible, mais une organisation entière où la vélocité de génération de code (mandat à 80 % d'adoption de l'assistant IA Kiro) a dépassé la capacité de vérification, produisant quatre incidents Sev-1 en 90 jours dont une panne de 6h à ~6,3M commandes perdues.

Le parallèle structurel avec la thèse de Trueman est direct : les contrôles automatiques existants (tests, analyse statique) n'ont pas détecté le problème avant production, parce qu'ils valident des propriétés locales du code, pas le comportement émergent du système à l'échelle. La différence de nature : ici il ne s'agit pas de composants individuellement corrects s'assemblant en un tout défaillant, mais de code individuellement plausible s'accumulant en un système que plus personne ne peut tracer de bout en bout — voir [shadow-code](shadow-code.md) pour ce mécanisme spécifique.

Point notable pour la lecture de ce type de source : Amazon a affirmé publiquement que les incidents n'impliquaient pas de code écrit par IA, tout en documentant en interne une "tendance d'incidents" liée aux "changements assistés par Gen-AI" — documents ensuite édités avant la réunion de discussion. Cette gestion du narratif est elle-même une donnée sur la façon dont les organisations répondent à un échec d'infrastructure IA, distincte de la question technique.

## La réponse structurelle : le modèle à trois couches

[modele-accountability-trois-couches](modele-accountability-trois-couches.md) (Lance Dacy) apporte ce que ce concept n'avait pas encore : un mécanisme correctif à coût quasi nul plutôt qu'un problème seulement nommé. Un humain nommé ("reviewer of record") par changement assisté par IA, des catégories d'exception définies par l'équipe, une politique organisationnelle écrite — trois couches, chacune nécessitant un nom humain plutôt qu'une responsabilité collective diffuse. Les contre-mesures qu'Amazon a mises en place après incident (sign-off senior, review à deux personnes, audits VP sur 335 systèmes) sont une version réactive et coûteuse de ce même modèle — la comparaison entre les deux mesure le prix de construire l'accountability avant ou après l'incident.

## Le cas inverse : quand l'accountability gap est résolu

[human-layer-agentic-design-systems](../sources/human-layer-agentic-design-systems.md) documente la situation symétrique : un design system où la traçabilité est suffisamment construite pour que le gap n'existe pas. L'incident de l'échelle de jaune primitif chez Enara produit une chaîne complète : développeur (observe une anomalie visuelle) → token auditor (confirme que l'implémentation est correcte) → couche primitive (incriminée) → designer (propriétaire de la décision). Le système a surfacé non pas seulement *qu'il y avait une erreur*, mais *à qui elle appartenait*.

[cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) nomme explicitement ce résultat : "That's accountability. And it changes everything about how I think about my role." La résolution du gap n'est pas organisationnelle dans ce cas — elle est architecturale : la traçabilité de la décision à l'exécution est encodée dans l'infrastructure, et la boucle peut donc remonter.

Cela précise la condition nécessaire pour que l'accountability soit possible : la décision doit être localisée dans le système, pas seulement entendue dans une conversation. Une décision de design qui vit dans la tête d'un designer ne peut pas être tracée automatiquement jusqu'à lui. Une décision encodée dans les tokens primitifs, avec un auditeur qui comprend les relations d'intent entre couches, peut l'être.

La leçon de synthèse est donc plus précise que "résoudre le gap organisationnellement" : la gouvernance technique bien construite peut résoudre l'accountability gap pour les décisions qui ont été encodées. Le gap organisationnellement documenté par [murphy-trueman](../entities/murphy-trueman.md) concerne les failures *composites* — celles qui émergent à l'intersection des composants, pas dans chaque décision individuelle — qui ne peuvent pas être encodées dans un token, et donc pas être tracées automatiquement.
