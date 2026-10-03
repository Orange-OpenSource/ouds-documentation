---
type: concept
tags: [pipeline, figma, documentation, automatisation, mcp, mintlify, github-actions, sync]
created: 2026-06-17
updated: 2026-06-29
sources:
  - "[figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)"
  - "[how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)"
  - "[typeform-design-system-documentation-scale-ai](../sources/typeform-design-system-documentation-scale-ai.md)"
  - "[uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md)"
  - "[20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)"
related:
  - "[documentation-lag](documentation-lag.md)"
  - "[mcp-model-context-protocol](mcp-model-context-protocol.md)"
  - "[boucle-feedback-infrastructure](boucle-feedback-infrastructure.md)"
  - "[mcp-on-demand-vs-rules-always-on](mcp-on-demand-vs-rules-always-on.md)"
  - "[processus-generation-metadata-echelle](processus-generation-metadata-echelle.md)"
  - "[mintlify](../entities/mintlify.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[pipeline-multi-destinations](pipeline-multi-destinations.md)"
  - "[notion-cms-design-system](notion-cms-design-system.md)"
  - "[fernando-coelho](../entities/fernando-coelho.md)"
  - "[generation-spec-agentique](generation-spec-agentique.md)"
  - "[ian-guisard](../entities/ian-guisard.md)"
---

## Pipeline Figma → docs automatisé

Le pipeline Figma → docs automatisé est la réponse architecturale au [documentation-lag](documentation-lag.md) décrite par [romina-kavcic](../entities/romina-kavcic.md) ([how-to-automate-design-system-documentation](../sources/how-to-automate-design-system-documentation.md)). Il connecte trois systèmes — Figma (via API et MCP), un outil IA (Claude Code), et [mintlify](../entities/mintlify.md) (hébergement de docs) — de sorte que les mises à jour de design se propagent automatiquement à la documentation sans intervention manuelle.

## Ce qui transite dans le pipeline

Depuis Figma : les specs courantes des composants (espacement, couleurs, typographie), les noms exacts des tokens depuis Figma Variables, les variants et états interactifs, des screenshots haute résolution (PNG 2x), les timestamps de dernière modification des frames. Depuis le codebase : les fichiers de documentation existants (`.mdx`), les guidelines d'usage et patterns comportementaux, les exigences d'accessibilité, les exemples de code, les commentaires de tracking `<!-- figma-frame: ... -->`. Vers Mintlify : les screenshots mis à jour, les specs synchronisées, les composants générés selon les patterns du codebase, les PR avec diffs visuels avant/après.

## Les deux flux de synchronisation

**Flow 1 — On-demand.** Le designer copie un lien de frame Figma et le colle dans Claude Code avec une instruction ("Update button docs from this frame"). Claude lit le frame via l'API Figma, exporte le screenshot, lit les docs existantes du codebase, met à jour les fichiers `.mdx`, crée une PR avec diff visuel. Mintlify déploie automatiquement quand la PR est mergée. Temps : 30 secondes vs 30 minutes de travail manuel.

**Flow 2 — Automatisé hebdomadaire.** Une GitHub Action scanne tous les fichiers `.mdx` du dossier docs pour les commentaires `<!-- figma-frame: FILE_ID/NODE_ID -->`. Pour chaque frame trackée, elle vérifie via l'API Figma si le frame a été modifié depuis le dernier screenshot. Si oui : export d'un nouveau PNG 2x, lecture des specs, mise à jour du `.mdx`. Si des changements existent, une PR est créée. Si aucun changement : sortie silencieuse, pas de PR. Entièrement automatisé, zéro travail manuel.

## Le frame ID tracking

Le commentaire HTML `<!-- figma-frame: FILE_ID/NODE_ID -->` dans les fichiers `.mdx` est le mécanisme de liaison entre un fichier de documentation et son source Figma. Il dit à l'automatisation quel frame surveiller pour ce composant. C'est un contrat explicite qui dépasse la simple documentation — il encode la provenance et permet la synchronisation bidirectionnelle.

Ce mécanisme de tracking est une forme de métadonnée de provenance : la documentation sait d'où elle vient. Sans ce lien, l'automatisation ne peut pas savoir quoi vérifier. C'est l'équivalent documentaire de l'index de codebase ([knowledge-graph-design-system](knowledge-graph-design-system.md)) : on encode explicitement les relations entre artefacts pour que les agents puissent naviguer sans explorer.

## Les writing guidelines comme couche de cohérence

Pour des résultats consistants entre les différentes mises à jour générées par Claude Code, [romina-kavcic](../entities/romina-kavcic.md) recommande de créer un fichier Markdown de writing guidelines : ton, voix, règles de rédaction, exemples de dos/don'ts. Ce fichier joue le même rôle que les Rules dans l'architecture [architecture-skills-rules-instructions](architecture-skills-rules-instructions.md) : un contexte always-on qui garantit la cohérence stylistique de toutes les sorties, indépendamment du composant traité.

## Relation avec le pipeline de métadonnées

Ce pipeline est une variante du [processus-generation-metadata-echelle](processus-generation-metadata-echelle.md) appliqué à la documentation narrative plutôt qu'aux métadonnées structurées machines. Les deux s'appuient sur la même logique — automatiser l'extraction depuis les sources existantes plutôt que produire manuellement — mais leurs sorties sont différentes : le pipeline de métadonnées produit du JSON pour les agents IA, le pipeline Figma → docs produit du MDX pour les humains (et potentiellement les agents).

## Variante Uber : génération de spec formelle (uSpec / Guisard)

[ian-guisard](../entities/ian-guisard.md) chez Uber documente une variante architecturalement différente des pipelines précédents ([uber-uspec-agentic-design-specs](../sources/uber-uspec-agentic-design-specs.md)) : la sortie n'est pas de la documentation narrative (MDX, Mintlify) mais des **pages de spec formelles** écrites directement dans Figma — anatomie du composant, documentation API, annotation de tokens, règles d'accessibilité multi-plateforme. Voir [generation-spec-agentique](generation-spec-agentique.md) pour le détail complet.

La différence principale avec le pipeline Kavcic (Figma → docs narrative) : le pipeline de Guisard ne synchronise pas, il **génère**. Il n'existe pas de spec préalable à mettre à jour — l'agent produit la spec from scratch depuis les données réelles du composant Figma, via le Figma Console MCP. La sortie est un artefact de design à destination des ingénieurs qui implémentent, pas une documentation à destination des équipes qui consomment le système.

L'architecture est également distincte : chaque section de spec est un **agent skill** distinct portant ses propres règles de validation et schémas. Le MCP fournit les données déterministes (noms de tokens réels, variantes, variables) ; le LLM fournit l'interprétation (quel rôle ARIA sémantiquement correct pour ce composant). Les deux couches sont nécessaires et non substituables.

## Variante Notion → multi-destinations (Typeform / Coelho)

[fernando-coelho](../entities/fernando-coelho.md) chez Typeform documente une variante architecturalement différente ([typeform-design-system-documentation-scale-ai](../sources/typeform-design-system-documentation-scale-ai.md)) : la source n'est pas Figma mais Notion, et le pipeline alimente non pas une seule destination mais trois simultanément (documentation, MCP, sandbox). Voir [pipeline-multi-destinations](pipeline-multi-destinations.md) pour le détail complet.

La différence de priorité est instructive : le pipeline Figma → docs (Kavcic) prioritise la **fraîcheur** — le design Figma est la source de vérité, la documentation suit. Le pipeline Notion → multi-destinations (Coelho) prioritise la **contribution** — l'outil familier à toute l'équipe est la source de vérité, la distribution suit. Ces deux approches résolvent des points différents du problème de documentation : l'une adresse la synchronisation design → code, l'autre adresse la barrière de contribution éditoriale.

## ⚡ Tension : on-demand vs toujours actif

Le Flow 1 (on-demand) suit la logique MCP identifiée par [diana-wolosin](../entities/diana-wolosin.md) : la mise à jour ne se produit que quand on la demande. Le Flow 2 (automatisé) est l'équivalent d'une synchronisation "always-on" — mais avec un délai hebdomadaire. Ni l'un ni l'autre n'est vraiment temps-réel. La tension avec l'idéal d'une documentation always-in-sync est réelle : le Flow 2 se relance "every Monday at X am UTC", pas à chaque commit Figma. Un composant modifié le mardi ne sera mis à jour dans les docs que le lundi suivant. Pour les équipes qui font des releases fréquentes, ce délai hebdomadaire peut ne pas être suffisant.

## Cron job hebdomadaire + composant génération de components

[romina-kavcic](../entities/romina-kavcic.md) ([20-ai-workflows-design-system-teams](../sources/20-ai-workflows-design-system-teams.md)) confirme l'architecture Figma MCP → Claude Code → Mintlify avec un ajout : le **cron job optionnel hebdomadaire** pour re-synchroniser les screenshots et détecter la dérive. Ce n'est pas un remplacement du pipeline on-demand — c'est un filet de sécurité pour attraper les dérives silencieuses entre deux mises à jour manuelles.

Elle ajoute également le volet **génération de composants** comme extension naturelle du même pipeline : Figma Make + MCP connectors (Notion, GitHub) + répertoire `.ai/` dans le repo constituent un pipeline symétrique — non plus Figma → docs, mais Figma → composant code. Les deux partagent la même infrastructure MCP ; seule la destination change.

## Limite concrète : la taille des frames de documentation OUDS

Le fichier OUDS Actions---Button ([figma-ouds-button-specs](../sources/figma-ouds-button-specs.md)) illustre une limite architecturale du pipeline qui n'était pas documentée dans le corpus. Le frame de documentation principal (node 2071:11587) mesure 31 742 × 13 443 px et contient plusieurs colonnes de specs pour toutes les variantes du composant. Ce frame génère plus de 2,3 millions de caractères XML via l'API Figma — une taille qui dépasse la capacité de traitement en un seul appel MCP.

Conséquence pour le pipeline : le commentaire `<!-- figma-frame: bmVSCYZgRmXwdqtpvT4flo/2071:11587 -->` permettrait à l'automatisation hebdomadaire de détecter les modifications du frame, mais pas de le lire en intégralité. Un pipeline opérationnel sur des frames de cette taille doit implémenter un crawl sélectif : identifier les sous-frames par type (anatomie, propriétés, états) et les interroger séparément. C'est une complexité supplémentaire non couverte par les descriptions de pipeline existantes, et qui distingue les fichiers de documentation dédiés (comme OUDS Actions---Button) des frames de composants individuels plus petits.
