---
type: concept
tags: [design-system, machine-readable, ia, documentation, metadata, benchmark, json, ai-readiness, statistiques]
created: 2026-06-17
updated: 2026-07-06
sources:
  - "[[figma-ouds-button-specs]]"
  - "[[design-system-most-important-asset-ai-era]]"
  - "[[towards-agentic-design-system]]"
  - "[[design-system-documentation-as-structured-metadata]]"
  - "[[machine-readable-design-systems-designing-for-ai-as-a-user]]"
  - "[[designing-figma-design-system-ai-understand]]"
  - "[[50-design-token-files-one-problem]]"
  - "[[miro-ai-design-system-mcp-claude-code-skills]]"
  - "[[design-system-documentation-spec]]"
  - "[[google-design-md-spec]]"
  - "[[figma-library-invisible-ai-agents]]"
  - "[[ai-ready-design-system-olha-bondar]]"
  - "[[state-of-ai-design-systems-2026-zeroheight]]"
  - "[[making-product-docs-work-humans-ai-gerireid]]"
related:
  - "[[systeme-de-design-agentique]]"
  - "[[trois-couches-composants-agents]]"
  - "[[composants-context-aware]]"
  - "[[intent-token]]"
  - "[[knowledge-graph-design-system]]"
  - "[[protocole-arc]]"
  - "[[schema-metadata-composant]]"
  - "[[workflows-ia-metadata]]"
  - "[[readable-vs-usable-token]]"
  - "[[delegation-lens]]"
  - "[[priori-conflictuels-nommage]]"
  - "[[dtcg-annotation-schema]]"
  - "[[ia-comme-utilisateur]]"
  - "[[diana-wolosin]]"
  - "[[alpesh-karanpuria]]"
  - "[[andressa-lombardo]]"
  - "[[eddie-machado]]"
  - "[[dsds-format]]"
  - "[[pj-onori]]"
  - "[[design-md-format]]"
  - "[[grammaire-composition-composants]]"
  - "[[contraintes-fixed-preferred-exploratory]]"
  - "[[geri-reid]]"
  - "[[cinq-questions-documentation-produit]]"
updated: 2026-07-06
---

## Lisibilité machine du design system

La lisibilité machine désigne la propriété d'un design system à être compris, interrogé et utilisé par des agents IA de manière autonome, sans interprétation humaine intermédiaire. C'est la condition nécessaire au [[systeme-de-design-agentique]].

La plupart des design systems existants ne sont pas lisibles par des machines. Ils sont lisibles par des humains : les guidelines sont en prose non structurée, les règles d'usage sont implicites et portées par la culture d'équipe, les décisions de composition dépendent d'une expertise tacite. Un agent IA ne peut pas accéder à cet implicite.

## Ce que ça requiert concrètement

Pour qu'un agent puisse utiliser un design system, il faut que le système fournisse trois types d'informations structurées — détaillées dans [[trois-couches-composants-agents]] : un index des composants et de leurs relations (la couche 1), des métadonnées explicitant le comment et le pourquoi de chaque composant (la couche 2), et une logique de raisonnement pour la sélection et la composition (la couche 3).

Sans ces couches, l'agent peut savoir qu'un composant Dialog existe, mais pas qu'il faut le combiner avec Alert et deux Buttons pour une action destructive, ni que le token à utiliser est `color.bg.danger` plutôt que `color.bg.primary`. Toute la valeur est dans l'intent encodé, pas dans la liste des composants.

## Traduction, pas création

[[cristian-morales-achiardi]] affine l'argument sur l'effort avec un cadrage décisif : la documentation structurée n'est pas de la documentation supplémentaire, c'est la même documentation traduite dans un format machine ([[design-system-documentation-as-structured-metadata]]). Une règle en annotation Figma ("Don't"), un paragraphe Storybook ("Best Practices"), un commentaire de code review répété — c'est le même savoir. Le fichier de métadonnées est le quatrième format de ce savoir, optimisé pour les agents. "It's not about creating new documentation. It's about reformatting existing knowledge."

[[romina-kavcic]] confirme que l'effort est sous-estimé dans l'autre sens : Écrire 554 descriptions de composants lui a pris "une session avec l'IA" ([[design-system-most-important-asset-ai-era]]). Le vrai obstacle n'est pas le volume de travail, c'est le changement de paradigme : passer de "documenter pour les humains" à "documenter pour les machines (et les humains)". Le [[processus-generation-metadata-echelle]] détaille comment procéder en 5 étapes.

## Preuve empirique

[[cristian-morales-achiardi]] a mesuré directement l'impact de l'infrastructure machine-readable sur les performances d'un agent : 11 essais contrôlés (5 sans infrastructure, 6 avec), même modèle, même codebase, même questions ([[towards-agentic-design-system]]). Résultats : **2x plus rapide** (1:52 vs 4:26), **54 % plus précis**, **zéro faux négatif** (57/57 composants trouvés vs 43-44/57), **0,04 % de variance** vs 26,5 % sans infrastructure. Coût de l'infrastructure : ~28K tokens en protocols structurés, investissement ponctuel. La formulation de l'auteur : traiter le design system "as a data structure that AI can query, not just text it has to interpret" — c'est exactement ce que désigne la lisibilité machine.

## La structuration Figma-native comme prérequis

[[alpesh-karanpuria]] ([[designing-figma-design-system-ai-understand]]) approche la lisibilité machine depuis la couche la plus amont : le fichier Figma lui-même. Avant qu'un pipeline MCP ou un système de métadonnées puisse être construit, le fichier Figma doit être organisé de façon que l'IA puisse en extraire de la structure, pas seulement des pixels.

Trois pratiques Figma-natives qui deviennent des signaux lisibles par les agents :

**Convention de nommage hiérarchique** — `Category / Component / Variant / State / Size`. Exemple : `Button / Primary / Hover / Medium`. Cette hiérarchie prévisible permet à l'IA de détecter des familles de composants et leurs variations sans documentation supplémentaire. Le vault traite abondamment de ce que la documentation doit contenir ; Karanpuria précise la forme que le naming doit prendre dans Figma. Règle complémentaire : nommer les calques avec des labels sémantiques (`Button Container`, `Button Label`) plutôt que des noms auto-générés (`Rectangle 23`, `Frame 124`).

**Component Properties plutôt que multiples composants** — Au lieu de créer des composants distincts pour chaque variante (`Button Primary`, `Button Secondary`, `Button Large`), utiliser les Component Properties de Figma (`Variant: Primary | Secondary | Ghost`, `Size: Small | Medium | Large`, `State: Default | Hover | Disabled`). Cette structure encode la logique du composant — ses dimensions de variation — d'une façon directement lisible par l'IA, qui peut raisonner sur l'espace des propriétés plutôt que sur une liste d'artefacts disjoints.

**Auto Layout comme signal comportemental** — L'Auto Layout dans Figma définit non seulement la présentation visuelle (padding, gap, alignement) mais le comportement responsive des éléments. Pour un agent qui génère de l'UI ou convertit un design en code, ces contraintes comportementales sont essentielles : sans Auto Layout, les éléments apparaissent statiques ; avec Auto Layout, ils révèlent leur logique d'adaptation. Karanpuria formule : "Without Auto Layout, elements look static to AI. With Auto Layout, they reveal structure and behavior."

Ces trois pratiques ne remplacent pas la couche de métadonnées structurées ([[schema-metadata-composant]]) mais la précèdent logiquement : un fichier Figma bien structuré produit un contenu extractable de meilleure qualité.

## Le client-side rendering comme bloqueur concret

[[eddie-machado]] chez Miro documente un bloqueur de lisibilité machine rarement mentionné dans le corpus : le rendu client-side des sites de documentation ([[miro-ai-design-system-mcp-claude-code-skills]]). Quand la documentation interne Miro rend ses liens de librairie en React plutôt qu'en Markdown, les agents ne peuvent pas les traverser. Aura entre dans des boucles — elle scanne le codebase aléatoirement jusqu'à trouver quelque chose qui correspond, ou hallucine une réponse.

Ce n'est pas un cas isolé : "This is the failure mode for most design system docs sites today." Les sites de documentation modernes basés sur des frameworks React ou Vue rendent souvent leurs index de composants côté client, invisibles pour les crawlers d'agents. La règle opérationnelle : **rendre les index de librairies en Markdown, pas en React** — un prérequis de lisibilité machine avant même de considérer le MCP ou les métadonnées.

Ce bloqueur affecte la couche 1 de [[trois-couches-composants-agents]] (l'index) : si l'agent ne peut pas traverser les liens d'index, il ne sait même pas ce qui existe dans le système.

## ⚡ Tension : readable ≠ usable (Kavcic, 2026)

[[romina-kavcic]] affine la notion de lisibilité machine avec une distinction que les sources précédentes ne posaient pas explicitement ([[50-design-token-files-one-problem]]). Son audit de 50 fichiers de tokens révèle deux états distincts : **machine-readable** (le build pipeline compile, les valeurs sont extraites) et **agent-usable** (l'agent peut raisonner sur quel token choisir dans quel contexte). Les design systems existants ont massivement atteint le premier état ; la quasi-totalité n'a pas atteint le second. Sur 50 systèmes : ~15 ont des descriptions dans le fichier, 1 seul a des règles de non-usage.

Cette distinction complète ce que les sources Morales Achiardi et Wolosin traitaient surtout du côté composants : la lisibilité machine au niveau des tokens est une propriété distincte, avec ses propres exigences (champs `$description`, `$deprecated`, `$extensions` dans les fichiers DTCG) et sa propre mesure empirique (expérience crimson vs red600 : 2/3 erreurs sans annotation, 0/2 avec). Voir [[readable-vs-usable-token]] pour la formalisation complète.

La définition de "lisibilité machine" dans ce wiki doit donc être précisée selon l'audience : readable-for-pipelines (compile, valeurs extraites) vs readable-for-agents (contexte, intent, règles de non-usage). Ce sont deux propriétés qui ne s'impliquent pas mutuellement.

## Benchmark de format : JSON gagne

[[diana-wolosin]] apporte la validation la plus rigoureuse publiée à ce jour sur les formats de métadonnées MCP ([[machine-readable-design-systems-designing-for-ai-as-a-user]]). Sur la base de production d'Indeed (77 composants, documentation MDX), elle a benchmarké 8 configurations MCP avec 1 056 prompts (22 prompts × 3 runs × 2 axes × 8 configs) en testant 5 formats : Markdown, plain Markdown, Markdown+JSON hybride, JSON, TOON.

Résultat : JSON gagne. Précision équivalente ou supérieure à l'hybride Markdown+JSON, avec 80 % de tokens en moins. En coût annualisé sur les 22 requêtes benchmark : Markdown ~$1 500/an, JSON ~$300/an — 5× moins cher. Raison : "JSON is like a contract: explicit keys, explicit values, explicit boundaries, no ambiguity." Il dit au LLM exactement ce qu'il voit et comment l'utiliser, sans interprétation.

Nuance importante issue de la Q&A : JSON est optimal pour les **métadonnées structurées de composants** (MCP, RAG). Pour les règles et instructions en langage naturel, Markdown reste l'outil approprié. Règle de Diana : "JSON for MCP, Markdown for LLM." Cette distinction se recoupe avec la différence entre Rules (always-on, en Markdown) et MCP (on-demand, en JSON) de l'architecture [[mcp-on-demand-vs-rules-always-on]].

## DESIGN.md : la lisibilité de l'identité visuelle (Google Labs, 2026)

Google Labs a open-sourcé en avril 2026 le format [[design-md-format]] (15 800 étoiles GitHub en moins de trois mois), qui apporte une réponse distincte au problème de lisibilité machine : plutôt que de documenter les composants un par un, décrire l'identité visuelle du projet dans un fichier unique combinant YAML (valeurs exactes des tokens) et prose Markdown (le *pourquoi* de chaque valeur). L'intention est explicitement de fournir aux agents un contexte persistant qui survit aux sessions — "a persistent, structured understanding of a design system" ([[google-design-md-spec]]).

La contribution conceptuelle de DESIGN.md à la notion de lisibilité machine est de distinguer deux niveaux de lisibilité qui restaient implicites dans le corpus : la lisibilité des valeurs (ce que DTCG et les tokens couvrent) et la lisibilité de l'intent de marque (pourquoi ce primary est "de l'encre profonde", pourquoi ce tertiary est "le seul driver d'interaction"). Ce second niveau est celui qui manque aux agents quand ils génèrent des UI génériques malgré un accès aux tokens. La CLI associée (`lint`, `diff`, `export`) fournit une infrastructure de gouvernance du fichier — vérification WCAG AA sur les paires de couleurs, détection de régressions entre versions, export vers Tailwind et W3C DTCG.

DESIGN.md ne remplace pas les approches par composants (DSDS, schémas maison) — il les précède logiquement dans le pipeline d'un agent : le fichier d'identité visuelle est lu en premier, les métadonnées de composants viennent en complément.

## Vers un standard ouvert : DSDS (Onori, 2026)

[[pj-onori]] publie en juin 2026 la Design System Documentation Spec ([[design-system-documentation-spec]]), première spécification ouverte qui formalise les exigences de lisibilité machine dans un format JSON validable. DSDS codifie ce que le corpus a décrit comme nécessaire — les trois couches, les règles d'usage structurées, la distinction humain/agent — dans une spec avec JSON Schema, versionnée et portable.

La contribution principale de DSDS à la notion de lisibilité machine est la formalisation du mécanisme `agentDocumentBlocks` : un espace séparé dans chaque entité, jamais rendu aux humains, uniquement pour les agents. Ce n'est plus une convention d'équipe à négocier — c'est un champ de la spec. La lisibilité machine devient ainsi un artefact de première classe, pas un effet de bord de la documentation humaine bien faite.

DSDS introduit également le système de `criteria` — des règles avec un mode de vérification déclaré (automated / assisted / manual) et des exemples fixtures (pass/fail) — qui va au-delà de la lisibilité passive : le design system peut vérifier que ses propres règles sont appliquées. C'est l'infrastructure de la [[boucle-feedback-infrastructure]] codifiée dans le format de documentation lui-même. Voir [[dsds-format]] pour le détail complet.

## "Illegible is different from incorrect" — la nuance manquante (Nurkhon, 2026)

La source [[figma-library-invisible-ai-agents]] apporte une reformulation qui manquait au corpus : **un design system peut être parfaitement correct et rester invisible à un agent**. L'auteur décrit en première personne avoir connecté Claude Code au Figma MCP sur une librairie construite avec soin — tokens, variants, nommage sémantique — et obtenu en 90 secondes un écran visuellement correct, entièrement hardcodé, sans aucun composant de la librairie. Les noms `nav-item-active-v3` et `modal-overlay-blur-dark` décrivent ce que les composants *ressemblent* à un humain ; ils ne disent rien à une machine sur ce pour quoi ils sont *faits*.

"AI agents parse, not infer." Cette formulation tranche ce que le reste du corpus laissait ambigu : la lisibilité machine n'est pas une question de degré dans la qualité de documentation — c'est un changement de régime. Un agent lit le nom, vérifie si un pattern correspond, utilise ou non. Il n'interroge pas l'équipe, ne lit pas l'historique des commits, ne reconstruit pas l'intention depuis le contexte. Si le nom n'encode pas la fonction, l'agent contourne.

Données d'ampleur : seulement **23 % des design systems** sont structurés suffisamment pour un usage IA consistent (UX Collective, décembre 2025). Le nommage sémantique (`color-border-error` vs `red-300`) produit **43 % de meilleure qualité de code généré** (Figma research, 2025). La Spotify Encore case est la manifestation la plus documentée de ce phénomène : système sophistiqué, développeurs qui contournent vers Cursor non pas parce qu'Encore est mal construit, mais parce qu'il est trop complexe pour qu'un agent le parse efficacement — et qu'un chemin plus direct existait.

Le contrat implicite est la racine structurelle du problème. Les noms d'un design system compriment une histoire : les conversations, les décisions, les versions. `input-v2-final` a un sens pour ceux qui étaient là pour v1. Un agent n'a que le fichier, le nom, et la structure — rien d'autre. La communication humaine compresse ; les agents n'ont pas le décompresseur.

## La lisibilité du contenu comme dimension oubliée (Bondar, 2026)

Le corpus du wiki a surtout traité la lisibilité machine comme une propriété des fondations (tokens), des composants (métadonnées, contrats, nommage) et de l'identité visuelle (DESIGN.md). [[ai-ready-design-system-olha-bondar]] ajoute une dimension que le corpus avait laissée implicite : **la guidance de contenu structurée** comme composante à part entière de la lisibilité machine.

L'observation de Bondar : les produits générés par IA échouent fréquemment sur le contenu, pas sur la mise en page. Labels vagues, terminologie incohérente, messages d'erreur sans chemin de récupération, confirmation qui ne confirme rien. Ces défauts ne sont pas corrigibles par de meilleurs tokens ou de meilleurs contrats de composant — ils requièrent que le design system expose explicitement la terminologie produit, les conventions de nommage, les patterns de formulation pour les états vides, les erreurs, les actions. La forme structurelle proposée :

```
Error message = What happened + why it may have happened + what the user can do next
```

Ce n'est pas une règle de writing style — c'est un contrat d'interaction encodé dans le système. Un agent qui a accès à ce contrat peut générer un message d'erreur cohérent ; sans lui, il improvise ("Something went wrong.").

## La validation exécutable comme boucle de feedback (Bondar, 2026)

La Layer 7 de [[ai-ready-design-system-olha-bondar]] formalise ce que la [[boucle-feedback-infrastructure]] esquissait : la validation n'est pas un audit post-hoc mais une infrastructure intégrée au workflow de génération. La boucle est : Generate → Test → Identify violation → Correct → Test again. Sans elle, "le design system devient un ensemble de règles sans signal de suivi."

Ce que les checks déterministes couvrent : absence de couleurs hardcodées quand un token existe, absence de composants dépréciés, noms accessibles requis, comportement clavier requis, propriétés de composant valides, régression visuelle sur les patterns stables, stories Storybook requises. La distinction importante : tout ce qui peut être testé *devrait* être testé — le reste peut rester dans la documentation, mais pas à la place de la validation.

Bondar cite l'outillage Storybook (MCP exposant la documentation et les manifestes aux agents, génération de stories, test failures comme feedback) comme instance de cette boucle. L'idée-clé : **le design system devient un mécanisme de feedback**, pas seulement un ensemble d'instructions. Cette dimension enrichit la définition de lisibilité machine : un système n'est pas pleinement lisible si l'agent peut lire les règles sans vérifier s'il les applique. Voir [[dsds-format]] pour la formalisation de ce principe dans les `criteria` avec modes de vérification déclarés.

## L'état de l'AI-readiness en 2026 : la donnée sectorielle

[[state-of-ai-design-systems-2026-zeroheight]] (N=123, mai 2026) fournit la première mesure sectorielle de la lisibilité machine au niveau terrain. Seulement **17 % des équipes DS** estiment leur documentation "very AI-ready" — c'est-à-dire structurée, indexée et cohérente au point d'être efficacement consommable par des agents. La distribution complète : 27 % structurée, 35 % "mostly good but inconsistent", 20 % pas organisée.

Ce chiffre est la validation empirique à grande échelle de la thèse centrale de ce wiki : la lisibilité machine n'est pas acquise par défaut, même dans des équipes ayant des design systems matures (60 % des systèmes ont 3+ ans). La maturité du DS n'implique pas sa lisibilité machine.

L'ironie structurelle que le rapport souligne : 63 % des équipes se déclarent satisfaites de l'utilisation de l'IA pour la documentation — et simultanément, 83 % ont une documentation insuffisamment structurée pour en tirer le plein bénéfice. Ces deux données ne se contredisent pas : les équipes tirent de la valeur de l'IA malgré la faible AI-readiness, mais plafonnent avant le niveau où l'IA devient réellement autonome sur les tâches de documentation.

La formulation du rapport : "Don't rush — get your design system documentation right. AI will compound good or compound bad." C'est exactement la propriété de lisibilité machine appliquée au terrain — sauf que le terrain la découvre empiriquement là où le corpus du vault la déduisait structurellement.

## Deux niveaux de lisibilité dans un même composant : le cas OUDS Button

Le Button OUDS ([[figma-ouds-button-specs]]) illustre un problème de lisibilité à deux vitesses. La description du composant dans la bibliothèque Figma est remarquablement lisible : sections structurées avec préfixes emoji comme délimiteurs sémantiques, use cases explicites, anti-pattern formulé avec son alternative, liste de mots-clés. Un agent MCP peut lire et parser cette description sans aucune sélection Desktop.

Mais les specs réelles — dimensions en pixels, valeurs de tokens, états interactifs, règles d'espacement — vivent dans un frame Figma dédié (node 2071:11587, 31 742 × 13 443 px) qui produit plus de 2,3 millions de caractères XML. Ce frame est trop grand pour être traité sans crawl sélectif. Il n'est accessible via get_design_context que si le layer est sélectionné dans l'application Figma Desktop — ce qui brise la lisibilité autonome de l'agent.

OUDS a donc résolu la moitié du problème : l'intent (pourquoi utiliser ce composant, quand ne pas l'utiliser, quels mots-clés) est machine-readable. L'implémentation (comment il est construit, quelles sont les valeurs exactes) ne l'est pas encore. C'est une illustration concrète de la distinction entre lisibilité de surface et lisibilité structurelle — et de pourquoi les deux couches exigent des solutions différentes.

## Storybook Component Manifest et Zeroheight MCP : la lisibilité machine de la documentation existante

[[murphy-trueman]] documente deux infrastructures complémentaires aux formats Markdown (AGENTS.md, SKILL.md, DESIGN.md) qui étendent la lisibilité machine au contenu de documentation déjà existant ([[your-design-system-fragmenting-agent-files]]).

Storybook 10.3 livre un addon MCP qui expose le contenu Storybook aux agents via un Storybook Component Manifest — un fichier JSON listant composants, props, stories, et documentation dans un format optimisé pour les tokens. Le manifest est généré automatiquement depuis les stories ; Chromatic le publie comme service d'hébergement avec un tier gratuit couvrant la majorité des équipes. L'agent interroge le manifest avant de générer de l'UI pour comprendre quels composants existent, leurs props, leurs variantes documentées. C'est une forme de [[schema-metadata-composant]] généré depuis la source de vérité existante (les stories) sans double saisie.

Zeroheight a son propre MCP server exposant la documentation design system hébergée dans Zeroheight aux agents. [[diana-wolosin]] chez Indeed a publié sur la construction de MCP servers customs depuis MDX, avec des parsers qui se synchronisent automatiquement à chaque mise à jour de la documentation.

Le pattern commun : prendre du contenu qui existe déjà en format humain (Storybook stories, Zeroheight pages, MDX docs) et en exposer un sous-ensemble structuré et machine-readable aux agents via MCP. La clé est "structured, machine-readable subset" — pas la totalité du contenu humain (trop verbeux, trop coûteux en tokens), mais une représentation optimisée pour le raisonnement agent. Les formats Markdown (AGENTS.md, SKILL.md, DESIGN.md) couvrent les angles que ces MCP servers n'adressent pas — gouvernance de projet, procédures de workflow, identité visuelle globale.

Cela confirme empiriquement le benchmark de [[diana-wolosin]] : JSON pour le MCP (component manifest, MCP payloads structurés), Markdown pour les instructions LLM (AGENTS.md, SKILL.md, DESIGN.md). La pile complète combine les deux selon le type d'information à transmettre.

## La lisibilité machine comme corollaire de la lisibilité humaine (Reid, 2026)

[[geri-reid]] introduit dans [[making-product-docs-work-humans-ai-gerireid]] un cadrage qui manquait au corpus : la lisibilité machine n'est pas une propriété additionnelle à ajouter à la documentation humaine existante — c'est le même effort pour deux audiences simultanées. "The same things that make documentation more accessible for people also make it more useful for AI. Clear structure. Plain language. Accessible formats."

Ce renversement est tactiquement important. Le corpus existant présente la lisibilité machine comme un surcoût : ajouter des annotations DTCG, structurer les métadonnées JSON, relier design et code via Code Connect. Ce cadrage génère de la résistance dans les équipes qui ont déjà du mal à maintenir la documentation existante. Reid propose le cadrage inverse : améliorer la documentation pour les humains *est* améliorer la documentation pour les machines. L'investissement IA devient le levier pour remettre à plat des pratiques médiocres qui existaient bien avant les agents.

Le cadre des [[cinq-questions-documentation-produit]] opérationnalise cet insight : "What exists?" (référence), "What are the rules?" (spécifications), "What needs to be done?" (tâches), "How do I do something?" (how-to guides), "What changed?" (changelogs). Chaque question structure simultanément la consultation humaine et l'interprétation machine. C'est complémentaire au corpus avancé du vault (DTCG, MCP, métadonnées JSON) qui s'adresse aux équipes en phase d'optimisation agentique — Reid s'adresse aux équipes en phase de structuration initiale, là où 83 % du secteur se trouve encore.
