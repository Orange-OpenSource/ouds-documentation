---
type: source
tags: [design-system, ia, lisibilite, hygiene, enterprise, figma, paywall]
created: 2026-08-17
updated: 2026-08-17
sources: []
related:
  - "[tj-southleft](../entities/tj-southleft.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[readable-vs-usable-token](../concepts/readable-vs-usable-token.md)"
  - "[geri-reid](../entities/geri-reid.md)"
---

## Anatomy of an AI-Ready Design System

**Auteur** : [tj-southleft](../entities/tj-southleft.md)
**Publication** : Slot Machine (southleft, Substack)
**Date** : 2026-05-07
**URL** : https://southleft.substack.com/p/anatomy-of-an-ai-ready-design-system
**Fichier brut** : `raw/2026-08-17_anatomy-ai-ready-design-system-southleft.md`

⚠️ **Accès restreint** : article payant, seul l'aperçu gratuit (l'introduction) est accessible. La "hiérarchie de pratiques" annoncée en sous-titre, cœur substantiel de l'article, n'a pas pu être ingérée. Le résumé et les thèses ci-dessous portent uniquement sur ce que l'aperçu gratuit expose.

## Résumé

TJ documente un atelier mené avec une équipe design system enterprise qui n'a pas encore accès aux outils IA, retenue par les sas habituels (revue IT, procurement, sign-off sécurité). Plutôt que d'enseigner "comment utiliser l'IA", l'atelier a posé la question inverse : comment préparer un fichier Figma pour des outils IA qu'on n'a pas encore. Le constat qui en émerge : aucune des pratiques prescrites n'était spécifique à l'IA. C'était de l'hygiène de design system que personne n'avait pris la peine d'écrire, faute d'y avoir été forcé jusque-là.

## Thèses principales

**AI-ready = readable, point final.** Le sous-titre condense la thèse : "The practices that make a design system AI-ready are the same ones that make it readable, period." Pas de technique spécifique à l'IA qui manquerait aux équipes : une discipline de lisibilité générale jamais formalisée.

**Préparer à blanc, sans accès IA.** Contexte spécifique et absent du reste du corpus : des équipes enterprise qui doivent devenir "AI-ready" avant même d'avoir un accès aux outils, retardées par des sas organisationnels plutôt que par un manque de volonté technique. La préparation ne peut donc pas être validée empiriquement contre un agent réel au moment où elle est faite.

**L'IA comme révélateur, pas comme cause.** "AI happens to be the thing that's forcing it" : l'IA ne crée pas le besoin de documentation rigoureuse, elle rend visible et urgente une dette d'hygiène préexistante que rien ne forçait à traiter avant.

## Citations clés

"None of the practices we were prescribing were actually AI-specific." ([tj-southleft](../entities/tj-southleft.md))

"How do we get your Figma file ready for the AI tools you don't have yet?" ([tj-southleft](../entities/tj-southleft.md))

## Connexions identifiées

La thèse centrale converge avec celle de [geri-reid](../entities/geri-reid.md), déjà documentée dans [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) : "the same things that make documentation more accessible for people also make it more useful for AI." TJ apporte une confirmation indépendante par un canal différent (atelier de conseil auprès d'une équipe enterprise réelle, plutôt qu'un article éditorial) et un contexte inédit dans le vault : des équipes qui préparent leur système sans pouvoir tester contre un agent réel, faute d'accès. Voir la section ajoutée dans [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) pour le détail.

Ce n'est pas une tension avec la position Kavcic/Achiardi (intent tokens, champs `$description`, `useFor`/`avoidFor` documentés dans [intent-token](../concepts/intent-token.md) et [readable-vs-usable-token](../concepts/readable-vs-usable-token.md)), malgré une lecture rapide qui pourrait l'y voir. L'expérience crimson/red600 montre justement qu'une documentation "readable pour humains" au sens tacite, un collègue qu'on peut interroger, ne suffit pas à un agent. La formule de TJ, "hygiene that nobody had bothered to write down", est compatible avec cette preuve : son "AI-ready = readable" désigne une lisibilité explicite et écrite, pas la lisibilité tacite dont une équipe humaine peut se contenter. Les deux positions convergent plutôt qu'elles ne s'opposent.
