---
type: concept
tags: [gouvernance, accountability, ia, design-system, accessibilite, responsabilite, composite-failure, traçabilité]
created: 2026-07-06
updated: 2026-07-07
sources:
  - "[[design-system-ai-ready-organisation-not]]"
  - "[[human-layer-agentic-design-systems]]"
related:
  - "[[gouvernance-design-system-ia]]"
  - "[[murphy-trueman]]"
  - "[[accessibilite-continue]]"
  - "[[shadow-ia-design-system]]"
  - "[[niveaux-confiance-actions-agentiques]]"
  - "[[existence-vs-intent-violations]]"
  - "[[concevoir-les-conditions]]"
  - "[[cristian-morales-achiardi]]"
---

## L'accountability gap de l'IA générative

L'accountability gap désigne le vide de responsabilité qui apparaît quand une interface est générée par l'IA à partir d'un design system : personne n'a fait de choix délibéré, mais quelqu'un doit répondre quand ça se trompe. [[murphy-trueman]] formule le problème dans [[design-system-ai-ready-organisation-not]] : "Your existing accountability structures were designed for human authors with legible intent — not for outputs where nobody made a deliberate choice."

## La structure du problème

Dans un workflow humain classique, l'accountability est traçable. Quand un designer compose une interface, il y a un auteur, un intent, une conversation possible sur les décisions prises. Le processus de review critique des choix de craft : on peut interroger l'auteur sur pourquoi il a fait telle hiérarchie, pourquoi cet ordre d'information, pourquoi ce traitement des edge cases.

Quand l'interface est générée par IA, cette traçabilité disparaît. Le PM qui a prompté n'a pas fait de choix de composition — il a demandé un résultat. L'IA n'a pas d'intent, seulement des outputs. Le résultat peut passer tous les contrôles automatiques existants (tokens corrects, composants documentés, règles de nommage respectées) et rester médiocre ou défaillant sur des dimensions que les vérifications automatiques ne capturent pas.

## Le cas de l'accessibilité composite

Le cas le plus documenté de l'accountability gap est l'accessibilité ([[murphy-trueman]]) : des composants peuvent être accessibles en isolation et produire un tout inaccessible. L'accessibilité n'est pas seulement une propriété des éléments individuels — c'est une propriété des relations entre éléments, du flux cognitif, de l'ordre de navigation, du contexte d'usage. Un agent peut assembler des parties accessibles en un parcours inaccessible. "That's not a hypothetical edge case. It's the kind of failure that compounds at speed when no single person feels responsible for the composite experience."

C'est la même logique que [[existence-vs-intent-violations]] transposée à l'échelle de l'interface : les éléments *existent* correctement mais leur assemblage viole l'*intent* de l'expérience. La différence est que l'auditeur de tokens v2 peut détecter les violations d'intent sur les tokens ; aucun outil existant ne détecte systématiquement les violations d'intent sur la composition d'interface.

## Les modes de failure composite

Trueman identifie plusieurs modes qui échappent aux contrôles automatiques actuels :

Un bouton on-brand dans un flux off-brand — le composant est conforme, le contexte ne l'est pas. Un composant correct dans une hiérarchie confuse — la pièce est bonne, l'architecture de l'information est défaillante. Une interface techniquement valide avec un modèle mental fondamentalement cassé — aucune violation de règle, une mauvaise décision produit. Dans chaque cas, "AI-generated work cleared every automated check" parce que les contrôles existants ont été conçus pour valider des propriétés locales, pas des propriétés émergentes de la composition.

## Le vide d'ownership

Le gap structurel : qui est responsable de ces failures composites ? Trueman documente quatre candidats et l'absence de réponse claire dans la plupart des organisations : l'équipe design system (qui a construit les composants), la personne qui a prompté l'IA (qui a utilisé le résultat), l'ingénieur qui a implémenté (qui a déployé), le QA (qui n'a pas détecté). En l'absence de décision explicite, la responsabilité se dilue entre les quatre — ce qui signifie en pratique qu'elle n'appartient à personne.

"This will land on someone's desk. As AI-generated interfaces start shipping in production, someone will have to answer for the failures they produce. It's better to decide now whose desk that is, under what circumstances, and with what escalation path." ([[murphy-trueman]])

## Ce que ça requiert

L'accountability gap ne se résout pas techniquement — il se résout organisationnellement. Les décisions à prendre avant d'en avoir besoin : à qui appartient la responsabilité des outputs IA en production, est-ce que le seuil de review varie selon la nature du changement (contenu vs nouveau flux vs refonte de parcours), quel est le chemin d'escalade quand la responsabilité est ambiguë. Ces décisions doivent être stables avant d'être sous pression de deadline et d'enjeux stakeholders.

La connexion avec [[niveaux-confiance-actions-agentiques]] est directe : le niveau de confiance accordé à un output agentique détermine implicitement qui en est responsable. Un output auto-mergé (niveau 1) appartient au système. Un output en draft PR (niveau 2) appartient à l'équipe qui le valide. Un output "suggest only" (niveau 3) appartient au décideur humain. Sans cette décision explicite par type d'output, le gap reste entier.

## ⚡ Tension : la vitesse comme amplificateur

Le corpus existant documente que l'IA accélère la génération d'interfaces. L'accountability gap révèle que la vitesse est aussi l'amplificateur du risque : plus la création est rapide, plus les failures composites s'accumulent vite avant que quelqu'un les détecte. La gouvernance technique (auditeurs, constraints exécutables) ne suffit pas — elle valide des propriétés locales, pas la cohérence d'ensemble. La gouvernance organisationnelle (ownership clair, seuils de review, chemins d'escalade) est la seule réponse aux failures qui émergent à l'intersection des composants plutôt que dans chaque composant pris séparément.

## Le cas inverse : quand l'accountability gap est résolu

[[human-layer-agentic-design-systems]] documente la situation symétrique : un design system où la traçabilité est suffisamment construite pour que le gap n'existe pas. L'incident de l'échelle de jaune primitif chez Enara produit une chaîne complète : développeur (observe une anomalie visuelle) → token auditor (confirme que l'implémentation est correcte) → couche primitive (incriminée) → designer (propriétaire de la décision). Le système a surfacé non pas seulement *qu'il y avait une erreur*, mais *à qui elle appartenait*.

[[cristian-morales-achiardi]] nomme explicitement ce résultat : "That's accountability. And it changes everything about how I think about my role." La résolution du gap n'est pas organisationnelle dans ce cas — elle est architecturale : la traçabilité de la décision à l'exécution est encodée dans l'infrastructure, et la boucle peut donc remonter.

Cela précise la condition nécessaire pour que l'accountability soit possible : la décision doit être localisée dans le système, pas seulement entendue dans une conversation. Une décision de design qui vit dans la tête d'un designer ne peut pas être tracée automatiquement jusqu'à lui. Une décision encodée dans les tokens primitifs, avec un auditeur qui comprend les relations d'intent entre couches, peut l'être.

La leçon de synthèse est donc plus précise que "résoudre le gap organisationnellement" : la gouvernance technique bien construite peut résoudre l'accountability gap pour les décisions qui ont été encodées. Le gap organisationnellement documenté par [[murphy-trueman]] concerne les failures *composites* — celles qui émergent à l'intersection des composants, pas dans chaque décision individuelle — qui ne peuvent pas être encodées dans un token, et donc pas être tracées automatiquement.
