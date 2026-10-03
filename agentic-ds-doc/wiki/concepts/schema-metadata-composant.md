---
type: concept
tags: [design-system, metadata, schema, composants, ia, documentation, json, indeed]
created: 2026-06-17
updated: 2026-06-29
sources:
  - "[figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)"
  - "[design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)"
  - "[towards-agentic-design-system](../sources/towards-agentic-design-system.md)"
  - "[machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)"
  - "[miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)"
  - "[design-system-documentation-spec](../sources/design-system-documentation-spec.md)"
  - "[tdp-agentic-design-system-guide](../sources/tdp-agentic-design-system-guide.md)"
  - "[ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md)"
related:
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[workflows-ia-metadata](workflows-ia-metadata.md)"
  - "[intent-token](intent-token.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[grammaire-composition-composants](grammaire-composition-composants.md)"
updated: 2026-06-30
---

## Schéma de métadonnées de composant

Le schéma de métadonnées est la spécification formelle de ce que doit contenir un fichier `.metadata.ts` (ou `.json`, `.md`) pour rendre un composant de design system lisible et utilisable par un agent IA. [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) propose un schéma à 9 sections, avec une hiérarchie claire entre sections critiques (décisions) et sections de complétude (référence) ([design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)).

## Les 9 sections

**Sections critiques pour l'IA** — répondent aux questions que l'IA se pose le plus souvent et se trompe le plus souvent :

`usage` — Quand utiliser ce composant, patterns courants, anti-patterns. Structure : `useCases[]`, `commonPatterns[]`, `antiPatterns[]`. Chaque anti-pattern exige trois champs : `scenario` (quoi ne pas faire), `reason` (pourquoi c'est un problème), `alternative` (quoi faire à la place). Cette structure force la précision — impossible de rester vague.

`aiHints` — Critères de sélection explicites et mots-clés. `selectionCriteria` est la clé : pour chaque variante, une règle claire (`usePrimary: "Main action user should take on page/section"`). C'est la logique de décision encodée directement pour l'agent.

`variants` — Ce qui existe et l'intent de chaque option. `options[]` liste les variantes, `purpose{}` explique la raison d'être de chacune (`danger: "Destructive actions requiring attention"`).

`composition` — Ce qui va à l'intérieur, ce qui va autour. Slots, composants imbriqués, contraintes de parenté.

`behavior` — États, interactions, comportement responsive.

**Sections importantes pour la complétude** :

`props` — Définitions TypeScript complètes de l'API du composant.

`accessibility` — Rôle ARIA, support clavier, conformité WCAG, notes spécifiques.

`examples` — Extraits de code copy-paste fonctionnels (pas des screenshots).

**Métadonnées sur les métadonnées** :

`component` — Nom, catégorie (atoms/molecules/organisms), description, type (interactive/display/container/input), chemin, timestamps. C'est le **header** que les agents lisent en premier pour savoir si le composant est pertinent avant d'aller plus loin.

## La séparation Header / Body

La section `component` forme le header — lisible rapidement, format compact. Les autres sections forment le body — dense, détaillé. Cette séparation a une conséquence de performance : un agent peut scanner les headers de 57 composants en peu de tokens pour identifier les candidats, puis lire le body uniquement des 2 ou 3 qui semblent pertinents. Même logique que le HTTP : `HEAD` avant `GET`.

## Formats disponibles

Le schéma peut s'implémenter en TypeScript (`.metadata.ts`), JSON (`.metadata.json`) ou Markdown (`.metadata.md`). TypeScript est recommandé dans les projets JS/TS car les exemples sont du code réel exécutable, l'export peut être importé par des outils, et l'éditeur fournit de la coloration syntaxique. JSON est universel mais les exemples doivent être des strings. Markdown est lisible partout mais difficile à interroger programmatiquement.

## Application aux icônes : le schéma Miro (3 champs + do-not-use)

[eddie-machado](../entities/eddie-machado.md) chez Miro documente une instance du schéma appliquée non pas aux composants complexes mais aux icônes — souvent négligées dans les approches de métadonnées ([miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)). Quand Aura a généré une toolbar avec les mauvaises icônes ("confidently wrong"), la cause n'était pas le modèle mais le nommage : une icône nommée selon sa forme visuelle alors qu'elle sert une fonction différente, sans aucun champ explicitant la distinction.

La solution : trois champs obligatoires par icône.

**Visual description** — ce que l'icône montre visuellement. Exemple : "Two A's next to each other, one capital and one cursive." Sans ce champ, l'agent ne peut pas distinguer des icônes de formes similaires.

**Use case** — quand l'utiliser. Exemple : "Represents font style like serif or sans serif."

**Category** — où elle se trouve dans le système.

Et surtout, la règle de non-usage explicite dans la description : "Do not use to represent text style like bold, italic, underline." ou "Do not use for cards or flat content. Use background-surface instead."

Ce pattern — trois champs + do-not-use — s'applique identiquement aux tokens de background dans le cas Miro : "Background for toolbars, panels and dropdowns. Do not use for cards or flat content. Use background-surface instead." Après l'ajout de ces champs, les mêmes prompts produisent des sorties correctes.

La leçon de Miro étend le [schema-metadata-composant](schema-metadata-composant.md) au-delà des composants : les icônes et tokens nécessitent le même niveau d'intent encodé. Ce n'est pas une différence de principe — c'est le même principe appliqué à des assets sous-documentés par tradition.

## Le principe de précision forcée

Un bénéfice collatéral de la structuration : la forme exige la précision que la prose permet d'éviter. "Évitez les boutons primaires multiples" est acceptable en prose. En metadata, il faut écrire : scénario (`"Multiple primary buttons in same section"`), raison (`"Creates visual hierarchy confusion"`), alternative (`"Use one primary and secondary/ghost for other actions"`). Cette précision profite autant aux humains (développeurs juniors, onboarding) qu'aux agents IA ([design-system-documentation-as-structured-metadata](../sources/design-system-documentation-as-structured-metadata.md)).

## L'implémentation Indeed (Wolosin)

[diana-wolosin](../entities/diana-wolosin.md) documente une variante de ce schéma à grande échelle ([machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)). Chez Indeed, les métadonnées sont générées depuis la documentation MDX existante via des parsers JavaScript — un parser par domaine de connaissance (accessibilité, développement, localisation, design) — puis fusionnées en un JSON unique par composant. Ce JSON est ensuite ingéré, chunké et indexé dans Vectra (base vectorielle open source) pour être servi par le MCP.

La différence architecturale avec le schéma de Morales Achiardi : Indeed sépare la génération des métadonnées (parsing MDX → JSON) du service au LLM (RAG sur Vectra). Le résultat est fonctionnellement similaire — un JSON structuré par composant, queryable par l'agent — mais l'organisation des domaines (accessibilité, développement, localisation, design) comme axes de parsing est une taxonomie différente des 9 sections de Morales Achiardi. Les deux approches s'alignent sur le principe : JSON explicite et structuré plutôt que prose ambiguë.

## L'implémentation The Design Project : 6 fichiers par composant (Alter, 2026)

[tdp-agentic-design-system-guide](../sources/tdp-agentic-design-system-guide.md) documente une troisième implémentation du schéma, orientée terrain et accessible. Dianne Alter propose une structure de 6 fichiers co-localisés par composant : `.tsx` (implémentation), `.meta.json` (metadata), `.tokens.css` (tokens propres au composant), `.stories.tsx` (Storybook), `.test.tsx` (tests d'usage correct), `index.ts` (export). La distinction clé : Storybook reste la vue *humaine*, le `.meta.json` est la vue *agentique* — même composant, deux lectures.

La structure du `.meta.json` converge avec les 9 sections de Morales Achiardi sur les champs critiques : `purpose`, `variants`, `commonPatterns`, `antiPatterns`, `tokens`. La différence notable est l'accent mis sur les **anti-patterns spécifiques au produit** : les génériques ("pas deux boutons primaires côte à côte") sont utiles mais insuffisants. Ce sont les anti-patterns que seule l'équipe connaît ("jamais un bouton destructif dans l'onboarding", "jamais minimal dans un card header", "loading state après 200ms minimum") qui distinguent une sortie *correcte* d'une sortie *proche*. Ces règles ne peuvent pas être générées — elles doivent être écrites manuellement.

Résultat mesuré chez un client B2B SaaS après structuration de ~20 composants : feature work de 5 jours réduit à une après-midi. Throughput revendiqué : ~10x (témoignage non contrôlé). La formulation d'Alter rejoint la thèse Karpathy : "the hottest new programming language is English" — l'instruction la plus puissante dans un fichier metadata est ce que le composant ne doit pas faire, écrit en langage naturel.

## Le contrat complet Bondar : useWhen / doNotUseWhen / accessibility

[ai-ready-design-system-olha-bondar](../sources/ai-ready-design-system-olha-bondar.md) propose une formulation alternative et complémentaire du contrat de composant, centrée sur la logique de décision que ni les 9 sections de Morales Achiardi ni le `.meta.json` TDP ne formalisent aussi explicitement. La structure `useWhen` / `doNotUseWhen` remplace les `antiPatterns[]` par une articulation symétrique :

```json
{
  "name": "AlertDialog",
  "purpose": "Interrupt a workflow when the user must confirm or cancel a consequential action.",
  "useWhen": ["The action is destructive", "The action is difficult to reverse"],
  "doNotUseWhen": ["The message is informational", "The action is easily reversible"],
  "requiredProps": ["title", "description", "confirmLabel", "cancelLabel"],
  "states": ["default", "submitting", "error"],
  "accessibility": {
    "role": "alertdialog",
    "initialFocus": "least destructive action",
    "returnFocus": true
  },
  "status": "stable"
}
```

La valeur ajoutée : `doNotUseWhen` est symétrique à `useWhen`, forçant la documentation des deux faces du critère de sélection. Le champ `accessibility` encode les contrats comportementaux (where focus goes, is it returned) au niveau du composant, rendant le contrat auto-suffisant pour la validation. Voir [grammaire-composition-composants](grammaire-composition-composants.md) pour la couche complémentaire gérant les relations *entre* composants.

## Cas réel : la description Figma du Button OUDS comme implémentation partielle

Le Button OUDS ([figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)) offre un exemple concret de ce que le schéma produit quand il est appliqué partiellement, directement dans le champ description d'un composant Figma. La description encode les sections `usage` (quatre cas d'usage explicites) et une forme condensée de `aiHints` (les keywords + la règle anti-pattern avec alternative). Elle couvre deux des neuf sections critiques sans aucune infrastructure supplémentaire — juste le champ texte natif de Figma.

Ce qui est absent : `variants` (les variantes ne sont pas nommées dans la description — elles vivent dans le frame de documentation visuel), `composition` (l'anatomie est dans le frame, pas dans la description), `props` (aucune définition API), `accessibility` (un seul rappel sur le contraste, sans valeurs). Les sections les plus coûteuses à renseigner sont précisément celles que la description Figma ne permet pas d'encoder de façon structurée. Cela confirme la thèse de Morales Achiardi : un seul champ texte libre est insuffisant — il faut un format structuré externe (JSON, TypeScript) pour couvrir les 9 sections.

Le point remarquable est l'anti-pattern formulé avec son alternative : "Do not use it for navigation purposes — use Navigation button instead." C'est exactement la structure `{ scenario, reason, alternative }` du schéma, compressée en une phrase. Dense, précis, et actionnable pour un agent.

