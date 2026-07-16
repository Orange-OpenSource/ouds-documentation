---
type: question
tags: [pitch, financement, directeur, outillage-ai, devs, roi, argumentaire]
created: 2026-06-24
updated: 2026-06-24
sources:
  - "[inversion-economique-code-comprehension](../concepts/inversion-economique-code-comprehension.md)"
  - "[design-system-as-infrastructure](../concepts/design-system-as-infrastructure.md)"
  - "[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md)"
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[generation-spec-agentique](../concepts/generation-spec-agentique.md)"
  - "[protocole-pas-produit](../concepts/protocole-pas-produit.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[seeds-vs-trees](../concepts/seeds-vs-trees.md)"
  - "[jan-six](../entities/jan-six.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
---

## Quel discours tenir pour convaincre un directeur en charge de l'outillage AI des devs de co-financer le chantier AI-readable + usable d'OUDS ?

---

## Le problème qu'il reconnaît déjà

Un directeur en charge de l'outillage AI des devs a un mandat simple : augmenter la vélocité des équipes d'ingénierie grâce à l'IA. Il a probablement déjà déployé GitHub Copilot, Cursor ou un équivalent. Les chiffres sont réels — 39 % d'augmentation de productivité, 41 % du code produit par IA en 2025 ([inversion-economique-code-comprehension](../concepts/inversion-economique-code-comprehension.md)). C'est le terrain favorable : son budget travaille déjà.

Le problème, qu'il n'a pas encore nommé clairement, est que cette productivité arrive avec une contrepartie silencieuse. Les outils génèrent du code syntaxiquement correct et sémantiquement faux par rapport à OUDS. Un Copilot sans contexte design system produit un bouton qui fonctionne mais qui utilise `#D0021B` au lieu du token `color.action.danger`, une Card qui respecte la syntaxe React mais qui duplique un composant existant, une interface qui compile mais qui ne ressemble à rien de ce que les guidelines d'OUDS définissent. Le coût apparaît plus tard, en revue de code, en QA, en dette technique — diffus, invisible, non imputé à l'outillage IA.

La formulation la plus directe vient de [jan-six](../entities/jan-six.md) chez GitHub : *"The invisible part of your system is way bigger than your visible part. If the agent can't see it, it has to hallucinate."* OUDS n'est pas visible aux agents IA aujourd'hui. Ils hallucinent donc ses conventions à chaque génération de code.

## L'argument économique central

Le déplacement de valeur est structural. Quand le code est gratuit, ce qui devient cher c'est la compréhension — les décisions de design encodées dans OUDS : pourquoi ce token et pas un autre, quand utiliser ce composant, quels anti-patterns éviter ([inversion-economique-code-comprehension](../concepts/inversion-economique-code-comprehension.md)). Ces assets étaient importants avant. Ils sont critiques maintenant, parce que c'est précisément ce que les agents ne peuvent pas inventer sans infrastructure.

La formulation qu'on peut lui soumettre directement : *"Without infrastructure, AI collapses toward the average of the internet."* ([design-system-as-infrastructure](../concepts/design-system-as-infrastructure.md)). Ses outils Copilot, Cursor et consorts sont exceptionnels pour générer du code générique. Pour générer du code OUDS-compliant, ils ont besoin qu'OUDS soit lisible. Sans ça, chaque euro investi dans l'outillage AI produit de la médiocrité générique — pas de la cohérence de marque.

Le corollaire immédiat : rendre OUDS AI-readable multiplie le ROI de son investissement existant en outillage. Ce n'est pas un projet design system. C'est le fond sur lequel tous les outils AI de son département délivrent leur valeur.

## Les chiffres de terrain qu'il comprend

Trois cas concrets, tous mesurés :

**Miro** — une équipe de 6 personnes, un an de travail, résultat : −70 à 80 % des questions dans le canal Slack design system ([metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)). Les ingénieurs obtenaient les réponses directement dans leur IDE. Zéro changement dans leur workflow — l'agent routait vers le design system de façon transparente. C'est exactement le type d'impact que ce directeur cherche : réduire la friction de support interne pour les devs.

**Indeed** — benchmark rigoureux, 1 056 prompts, 8 configurations MCP. Résultat : 4 300 prototypes générés en 4 mois, coût MCP JSON 5 fois inférieur au Markdown ($300 vs $1 500/an) ([lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)). L'investissement dans la lisibilité machine se traduit directement en coûts d'infrastructure réduits.

**Uber** — documentation de spec de composant (anatomie, API, accessibilité multi-plateforme) en minutes au lieu de semaines. La spec screen reader couvrant VoiceOver, TalkBack et ARIA : générée en moins de 2 minutes ([generation-spec-agentique](../concepts/generation-spec-agentique.md)). Ce gain libère du temps d'ingénierie sur les problèmes à valeur ajoutée.

## Pourquoi son budget, pas seulement le nôtre

L'argument de co-financement repose sur une asymétrie : l'équipe OUDS porte le coût de la transformation de l'infrastructure (rendre les tokens usables, encoder les métadonnées de composants, construire le MCP server), mais le bénéfice est capturé principalement par les équipes produit et engineering — et donc par son périmètre.

La répartition naturelle : l'équipe OUDS finance la couche de contenu (les métadonnées, les descriptions sémantiques des tokens, les schémas de composants), qui relève de sa responsabilité. Son budget finance la couche d'outillage et d'intégration (le serveur MCP, les Rules files, l'AGENTS.md, l'intégration dans les IDE des devs), qui relève de la sienne. Les deux couches sont nécessaires et complémentaires — aucune ne fonctionne sans l'autre ([mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)).

Un argument supplémentaire pour la durabilité de l'investissement : l'architecture repose sur MCP, un protocole ouvert, pas sur l'API d'un outil IA spécifique ([protocole-pas-produit](../concepts/protocole-pas-produit.md)). Si Cursor est remplacé par un meilleur outil demain, les intégrations ne bougent pas. L'investissement est durable quelle que soit l'évolution de l'écosystème IA — argument important pour quelqu'un dont le périmètre repose sur des choix d'outils potentiellement instables.

## La structure du discours en séquence

**1. Son problème d'abord.** Ses outils AI augmentent la productivité des devs mais génèrent du code hors-OUDS. Cette dérive est invisible dans les métriques de productivité mais visible en revue de code et en dette technique. Il dépense déjà pour un problème qu'il n'a pas encore nommé.

**2. La cause.** OUDS n'est pas lisible par les agents. Ce n'est pas un problème de tool — c'est un problème de contexte. Les agents hallucinent les conventions OUDS parce qu'ils ne peuvent pas y accéder structurellement.

**3. La solution et son architecture.** Deux couches interdépendantes — le contenu (métadonnées, intent encodé) que l'équipe OUDS porte, et l'outillage (MCP, intégration IDE) que son équipe porte. Chacun finance sa couche, les deux ensemble produisent l'impact.

**4. Les chiffres.** Miro −70/80 % Slack, Indeed 4 300 prototypes, Uber semaines → minutes. Contexte de marché : 84 % des devs utilisent l'IA quotidiennement, Gartner prédit 40 % des apps enterprise avec agents IA d'ici fin 2026 ([inversion-economique-code-comprehension](../concepts/inversion-economique-code-comprehension.md)).

**5. La durabilité.** L'investissement est sur protocole, pas sur un produit. Il survit à l'évolution de l'écosystème IA.

## Ce qu'il ne faut pas dire

Éviter le cadrage "design system" comme sujet principal — ce n'est pas son univers. Le cadrage juste est "infrastructure de contexte pour tes outils AI". OUDS est le nom de l'implémentation, pas l'objet du discours.

Éviter aussi de positionner ça comme un rattrapage ("on n'est pas encore prêts"). Le positionnement est : nous avons une opportunité de démultiplier le ROI des outils déjà déployés en résolvant la couche d'infrastructure qui leur manque. C'est une opportunité d'optimisation de son investissement existant, pas une dette à combler.

---

## Objection anticipée : "Pourquoi OUDS spécifiquement ?"

Il peut être tenté de demander pourquoi il est si important d'utiliser OUDS — sous-entendu : "ne peut-on pas juste laisser l'IA utiliser ce qu'elle veut ?"

### L'IA n'invente pas, elle régresse vers la moyenne

Un agent sans design system produit le code le plus *probable* selon ses données d'entraînement. Ces données sont publiques — GitHub, Stack Overflow, des millions de projets Tailwind, Material UI, Bootstrap. Le résultat est prévisible : des interfaces génériques, sans identité, qui ressemblent à n'importe quelle app SaaS. Comme [design-system-as-infrastructure](../concepts/design-system-as-infrastructure.md) le formule depuis l'IDS Conference 2026 : *"Without infrastructure, AI collapses toward the average of the internet."*

Les décisions spécifiques à l'organisation — les tokens OUDS, leurs rôles sémantiques, les anti-patterns documentés, les règles de composition entre composants — ne sont *pas* dans les données d'entraînement. Elles n'existent nulle part publiquement. Un agent qui ne peut pas les lire les hallucine. [jan-six](../entities/jan-six.md) chez GitHub : *"The invisible part of your system is way bigger than your visible part. If the agent can't see it, it has to hallucinate."*

Ce n'est pas un problème de qualité d'outil IA. GitHub Copilot et Cursor sont excellents pour du code générique. Ils n'ont aucun moyen de savoir ce qu'OUDS dit sur les boutons dans les alertes destructives — sauf si OUDS le leur dit explicitement.

### Sans OUDS, l'IA accélère la divergence

C'est l'argument qui devrait résonner spécifiquement chez un directeur outillage. Avant l'IA, les devs divergeaient lentement — un composant maison par-ci, un usage de token incorrect par-là. L'IA multiplie la vélocité de production, donc elle multiplie aussi la vélocité de divergence si aucune contrainte ne s'oppose. Dix équipes avec Cursor sans OUDS produisent dix variations légèrement différentes du même composant, chacune cohérente en interne, incohérentes entre elles.

[gouvernance-design-system-ia](../concepts/gouvernance-design-system-ia.md) documente le coût de cette dérive sans infrastructure : Nielsen Norman Group (2022) chiffre à plus de 40 % le temps des équipes design system consacré à de la maintenance corrective — régressions d'accessibilité, usages de tokens incorrects, documentation désynchronisée. Ce chiffre est déjà élevé à vélocité humaine. À vélocité IA, la même dérive s'accumule en jours plutôt qu'en mois.

OUDS n'est donc pas une contrainte sur l'IA — c'est le mécanisme qui empêche l'IA de produire activement de la dette technique à grande échelle.

### En réserve : "Pourquoi pas shadcn ou Material UI ?"

Si la question devient plus fondamentale, la réponse est que ces systèmes encodent les décisions de Vercel et de Google, pas celles de l'organisation. La valeur d'OUDS réside précisément dans ce qu'il contient d'unique : les arbitrages d'accessibilité, les compromis de densité, l'identité visuelle, les règles métier encodées dans les composants. C'est [inversion-economique-code-comprehension](../concepts/inversion-economique-code-comprehension.md) à l'état pur : ce que l'IA ne peut pas générer sans aide n'est pas le code, c'est la compréhension accumulée dans OUDS.
