---
type: concept
tags: [mcp, ia, protocol, agents, outils, integration, rag, on-demand, adoption, statistiques]
created: 2026-06-17
updated: 2026-07-16
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)"
  - "[how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)"
  - "[design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)"
  - "[state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md)"
  - "[storybook-mcp-ai-aware-component-libraries](../sources/storybook-mcp-ai-aware-component-libraries.md)"
  - "[figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md)"
  - "[romina-kavcic-5-mcp-connections](../sources/romina-kavcic-5-mcp-connections.md)"
related:
  - "[systeme-de-design-agentique](systeme-de-design-agentique.md)"
  - "[cli-vs-mcp](cli-vs-mcp.md)"
  - "[knowledge-graph-design-system](knowledge-graph-design-system.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[diana-wolosin](../entities/diana-wolosin.md)"
  - "[jesse-gardner](../entities/jesse-gardner.md)"
  - "[laura-fehre](../entities/laura-fehre.md)"
  - "[code-source-de-verite-mcp](code-source-de-verite-mcp.md)"
  - "[pipeline-figma-docs-automatise](pipeline-figma-docs-automatise.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[storybook](../entities/storybook.md)"
---

## Model Context Protocol (MCP)

Le Model Context Protocol est un standard qui permet aux agents IA de se connecter à des outils externes de manière structurée. [romina-kavcic](../entities/romina-kavcic.md) le décrit comme "USB for AI" : au lieu de construire une intégration personnalisée pour chaque outil, on expose les outils comme des serveurs MCP, et n'importe quel agent compatible peut les utiliser ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

L'analogie USB est précise : MCP standardise le protocole de connexion, pas le contenu de l'outil. Figma, GitHub, Storybook, Chromatic, Notion, Jira, Linear — chacun expose une tranche différente de contexte que l'agent peut interroger dans un même flux de travail.

## Adoption et momentum

L'adoption est rapide. L'écosystème MCP est passé de 100 000 à 8 millions de téléchargements en quelques mois ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)). Gartner prévoit que 40 % des applications enterprise embarqueront des agents IA d'ici fin 2026.

## Ce que MCP apporte au design system

Pour un système de design agentique, MCP permet d'orchestrer plusieurs sources de contexte en un seul flux. Exemple concret : un token change dans Figma → l'agent interroge GitHub pour identifier les composants qui l'utilisent → interroge PostHog pour identifier les pages affectées et leur trafic → décide si un PR doit être ouvert. Ce flux traverse quatre sources de données différentes (Figma, GitHub, PostHog, knowledge graph). CLI ne peut pas faire ça. MCP peut. Voir [cli-vs-mcp](cli-vs-mcp.md) pour la comparaison complète.

## MCP dans le workflow de Romina Kavcic

Les MCPs les plus utilisés dans son setup : Figma, GitHub, Storybook, Chromatic, Granola ([granola](../entities/granola.md)), Notion, Jira, Stylelint, Linear, Mintlify. Chacun représente une couche de contexte différente dans l'architecture agentique.

## MCP Figma pour la documentation automatisée

[romina-kavcic](../entities/romina-kavcic.md) documente un usage concret du MCP Figma pour l'automatisation de la documentation ([how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)). Via un Personal Access Token Figma (scope `File content`, lecture seule), Claude Code peut accéder en temps réel aux specs courantes d'un composant (espacement, couleurs, typographie), aux noms exacts des tokens depuis Figma Variables, aux variants et états interactifs, et exporter des screenshots haute résolution (PNG 2x). Ce qui nécessitait auparavant une exportation manuelle, une copie-colle de specs et une mise à jour de documentation (30 minutes) prend 30 secondes via MCP.

La formulation de Kavcic : "MCP lets Claude read [Figma files] directly. Think of it as giving Claude read-only access to your design files." C'est la même logique USB de connexion standardisée, appliquée ici non pas à l'orchestration agentique multi-outils mais à la synchronisation de documentation.

## Le flux RAG détaillé (Wolosin)

[diana-wolosin](../entities/diana-wolosin.md) décompose le flux MCP complet en 7 étapes ([machine-readable-design-systems-designing-for-ai-as-a-user](../sources/machine-readable-design-systems-designing-for-ai-as-a-user.md)) : (1) l'humain envoie un prompt depuis la context window ; (2) le LLM extrait les mots-clés et formule une requête ; (3) le MCP reçoit la requête ; (4) RAG agit comme un bibliothécaire, cherchant la similarité sémantique entre la requête et les métadonnées ; (5) la base vectorielle retourne les résultats ; (6) le serveur MCP renvoie les résultats au LLM ; (7) le LLM raisonne sur les résultats et génère.

Sa définition condensée : "A model context protocol is how you give an AI on-demand access to your design system knowledge." Le mot "on-demand" est central — c'est lui qui explique pourquoi le MCP seul est insuffisant pour les fondations. Voir [mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md) pour les implications architecturales complètes.

## Trois modèles d'implémentation

La conférence IDS 2026 documente trois architectures concrètes ([design-systems-mcp-complete-guide](../sources/design-systems-mcp-complete-guide.md)) :

**Indeed (Wolosin)** — Documentation MDX comme source primaire. Pipeline : MDX dans GitLab → parsers JavaScript par domaine (a11y, dev, localization, design) → JSON → Vectra (base vectorielle open source) → MCP. Infrastructure construite par Tony Rucker (partenaire développeur). Auto-déclenché à chaque update de documentation. 77 composants, 4 300 prototypes en 4 mois. Précision : ces prototypes n'utilisaient **pas** le MCP Figma et n'utilisaient **pas** Tailwind — composants React du DS Indeed directement. Implémentation documentation-led pure ([diana-wolosin](../entities/diana-wolosin.md)).

**New York State ([jesse-gardner](../entities/jesse-gardner.md))** — Code comme source primaire. Pipeline : web components Lit/TypeScript + JSDoc riche → custom element manifest → MCP server. Parité Figma via Code Connect. Cas documenté : PDF de 5 pages → formulaire multi-étapes fonctionnel en 13 minutes. Chiffre critique : 50–80K tokens gaspillés quand l'IA pointe sur la codebase brute sans MCP. Voir [code-source-de-verite-mcp](code-source-de-verite-mcp.md).

**The Design System Guide (Kavcic)** — Plugin Figma comme interface. Tidy : 66 MCP tools couvrant audit du naming, health score sur 6 catégories, validation de variables, composition de patterns. Couplé à Observatory, un dashboard visualisant le knowledge graph à travers Figma, GitHub, Storybook, Linear, Chromatic, Playwright et PostHog.

Ces trois modèles ne sont pas concurrents — ils reflètent des topologies d'équipe différentes : documentation-led (Indeed), engineering-led (NY State), design-led (Kavcic/Tidy).

**Storybook ([brad-frost](../entities/brad-frost.md))** — L'équipe Storybook a lancé un [Storybook MCP](https://storybook.js.org/addons/@storybook/addon-mcp) qui permet de générer de l'UI en s'appuyant sur les bibliothèques de composants du design system ([agentic-design-systems-2026-bradfrost](../sources/agentic-design-systems-2026-bradfrost.md)). Un quatrième point d'entrée dans l'écosystème, centré sur les stories comme source de vérité de la bibliothèque de composants.

## Trois usages du Figma MCP côté équipe design system (Figma, août 2025)

[figma-design-systems-ai-mcp](../sources/figma-design-systems-ai-mcp.md), publié par [figma](../entities/figma.md) elle-même, précise ce que le MCP Figma apporte spécifiquement à une équipe design system, au-delà de la lecture de specs déjà documentée par Kavcic ci-dessus : **génération de code de composant aligné** (combine le contexte MCP d'un nouveau composant avec le code des composants existants, dans le langage et framework réellement utilisés par l'équipe, pas seulement React/Tailwind par défaut), **automatisation du travail sur les tokens** (identifie où appliquer ou introduire des tokens, vérifie la conformité aux standards définis), et **audit d'alignement design/code** (compare l'usage des tokens dans le code vs le design sélectionné, signale les noms de layers à améliorer).

Chiffre structurant de cette source : 68 % des développeurs utilisent déjà l'IA pour écrire du code, mais seulement 32 % font confiance à l'output généré (Figma AI report 2025). Voir [metriques-adoption-ia-design-system](metriques-adoption-ia-design-system.md).

**Génération automatique de fichier de règles** : le MCP server peut scanner la codebase et produire un fichier de règles structuré (tokens, bibliothèques de composants, hiérarchies de style, conventions de nommage) qui sert de guide système à l'agent. C'est le mécanisme concret derrière le skill `figma-create-design-system-rules` déjà mentionné dans [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md).

## Inventaire pratique de connecteurs MCP (Kavcic, août 2025)

[romina-kavcic-5-mcp-connections](../sources/romina-kavcic-5-mcp-connections.md) est l'article le plus ancien de Kavcic ingéré dans le vault — antérieur à toute sa série "Agentic Design Systems" — et le seul à structurer les connecteurs MCP par complexité d'installation plutôt que par cas d'usage narratif :

- **Figma** : facile — lecture composants/tokens/variants, génération de specs et prototypes cliquables
- **Mintlify** : facile (clé API) — documentation comme base de connaissances interrogeable depuis l'éditeur
- **GitHub** : facile (PAT) — prévention de la dérive design/code, review de PR, changelog automatique
- **GitLab** : modérée — nécessite le tier Premium/Ultimate, absent sur Free/Starter
- **PostHog** : modérée — nécessite du tracking d'événements déjà en place ; valide les décisions de design system avec des données d'usage réelles
- **Slack** : modérée — approbation admin + OAuth ; transforme l'historique de conversation en connaissance interrogeable (décisions de design review, feedback compilé, alertes sur patterns de duplication)

GitLab et Slack n'avaient jusqu'ici que des mentions ponctuelles dans le vault (pipeline Indeed pour GitLab, baisse du volume de questions dans [metriques-adoption-ia-design-system](metriques-adoption-ia-design-system.md) pour Slack) — cette source est la première à documenter leur usage MCP de façon autonome et actionnable.

## Storybook MCP en pratique (LogRocket, juillet 2026)

[storybook-mcp-ai-aware-component-libraries](../sources/storybook-mcp-ai-aware-component-libraries.md) documente ce quatrième point d'entrée avec un niveau de détail inédit dans le vault : six outils MCP en trois toolsets (docs, dev, test), backés par des component manifests générés au build. La démonstration avant/après est la preuve la plus directe du vault sur l'effet du MCP : sans lui, Claude Code écrit 263 lignes de HTML natif inventé sans un seul appel d'outil ; avec lui, l'agent fait six appels d'outils avant d'écrire la moindre ligne, puis compose 188 lignes à partir des vrais composants avec des props exactement conformes au contrat documenté.

Le toolset test (`run-story-tests`) ajoute une capacité absente des trois autres implémentations documentées (Indeed, NY State, Tidy) : la vérification et l'auto-correction. Voir [boucle-feedback-infrastructure](boucle-feedback-infrastructure.md) pour le détail de la boucle self-healing observée sur ce cas.

## Adoption MCP : première mesure sectorielle (zeroheight, mai 2026)

[state-of-ai-design-systems-2026-zeroheight](../sources/state-of-ai-design-systems-2026-zeroheight.md) publie la première donnée sectorielle sur l'adoption MCP dans les équipes DS (N=123) : **47 % font déjà tourner un serveur MCP**. 31 % planifient l'adoption. Seulement 3 % ne sont pas convaincus de la valeur.

Ce chiffre change le statut du MCP dans le discours : ce n'est plus une approche d'avant-garde documentée par quelques équipes publiées, c'est une infrastructure adoptée par près de la moitié des équipes interrogées. "78 % are using or planning to use MCP" — le débat "si" est réglé, le débat "comment" est ouvert.

Les blocages à l'adoption chez les 22 % qui ne l'utilisent pas encore ne sont pas idéologiques : 28 % sur la roadmap (timing), 22 % ne savent pas comment configurer (setup), 13 % sécurité (grandes entreprises). Ce sont des blocages opérationnels, pas des objections de principe.

Les 6 cas d'usage MCP documentés par le rapport terrain complètent les 4 implémentations de référence (Indeed, NY State, Tidy, Storybook) :
1. Design-to-code translation — agent pointe vers Figma, produit du code avec les bons tokens et composants
2. Sync bidirectionnelle design ↔ code — changements de code reflétés dans le fichier Figma sans réconciliation manuelle
3. DS comme source de vérité pour les agents dans l'IDE — docs, tokens, icônes et specs a11y exposés directement aux agents
4. Réduction du support load de l'équipe DS — questions de composants routées via MCP, moins de Slack et de tickets
5. Visual QA et détection de drift — agents comparant Figma et code livré, détection automatique de régressions
6. Stacked MCPs pour le handoff — chaîne Zeroheight + Code Connect + GitHub dans une session d'agent

La donnée grande vs. petite entreprise est instructive : adoption MCP de 53 % dans les grandes contre 40 % dans les petites (+13 pp). Les grandes ont davantage de resources pour l'infrastructure, mais aussi davantage de pression pour la gouvernance à l'échelle.
