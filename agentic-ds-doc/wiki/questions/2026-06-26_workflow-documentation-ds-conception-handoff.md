---
type: question
tags: [workflow, documentation, design-system, pipeline, handoff, ia, figma, mcp, agentique]
created: 2026-06-26
updated: 2026-06-26
sources:
  - "[generation-spec-agentique](../concepts/generation-spec-agentique.md)"
  - "[pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)"
  - "[niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md)"
  - "[mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md)"
  - "[design-md-format](../concepts/design-md-format.md)"
  - "[pipeline-multi-destinations](../concepts/pipeline-multi-destinations.md)"
  - "[metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)"
related:
  - "[systeme-de-design-agentique](../concepts/systeme-de-design-agentique.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[documentation-lag](../concepts/documentation-lag.md)"
---

## Question

Quel serait le workflow idéal pour générer et maintenir la documentation d'un DS boostée par IA, en partant de la conception du composant jusqu'au handoff vers les devs ?

## Réponse

Le workflow s'organise en quatre phases séquentielles et une boucle de maintenance permanente. Aucune phase n'est optionnelle — chacune conditionne la suivante.

### Phase 0 — Préparer la source (Figma)

Avant de penser à l'automatisation, la structuration du fichier Figma lui-même doit être pensée pour la lisibilité machine ([lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)). Trois pratiques Figma-natives deviennent des signaux exploitables par les agents : une convention de nommage hiérarchique (`Category / Component / Variant / State / Size`), l'usage des Component Properties plutôt que de composants séparés par variante (pour encoder les dimensions de variation dans la structure), et l'Auto Layout systématique (pour que les agents perçoivent le comportement responsive, pas seulement le rendu statique). Un fichier Figma mal nommé produit un contenu extractable de mauvaise qualité.

C'est aussi à cette phase que le **DESIGN.md** ([design-md-format](../concepts/design-md-format.md)) a sa place naturelle : un fichier unique décrivant l'identité visuelle du système (tokens couleur, typographie, espacement, intent de marque en prose) que les agents chargent une fois et qui garantit la cohérence visuelle dans tous les environnements où le MCP n'est pas disponible (prototypage, outils externes, customer theming).

### Phase 1 — Générer la spec formelle à destination des devs

Le modèle de référence est uSpec d'Uber ([generation-spec-agentique](../concepts/generation-spec-agentique.md)) : via le Figma Console MCP, l'agent extrait les données réelles du composant et peuple des sections de spec structurées directement dans le fichier Figma. L'architecture à deux couches est clé : couche déterministe (MCP → données exactes, sans hallucination sur les noms de tokens) + couche interprétative (skills par section de spec, chacun chargeant ses propres règles). La spec couvre l'anatomie, l'API, les annotations de tokens, les règles d'accessibilité multi-plateforme (VoiceOver, TalkBack, ARIA) — générée en minutes, directement dans Figma, sans étape manuelle de formatage.

La gouvernance de cette phase suit [niveaux-confiance-actions-agentiques](../concepts/niveaux-confiance-actions-agentiques.md) : les specs générées méritent un niveau "Draft PR" minimum (l'agent génère, un spécialiste valide), jamais auto-merge.

### Phase 2 — Construire les métadonnées machines (pour les agents consommateurs)

Les métadonnées machines sont à destination des agents IA qui utilisent le design system pour générer de l'UI — distinct des specs formelles à destination des ingénieurs. Elles s'organisent en trois couches ([trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)) : un index (qu'est-ce qui existe et dépend de quoi), des métadonnées d'intent par composant (comment et pourquoi l'utiliser, anti-patterns, contraintes de composition), et une couche de raisonnement (logique de sélection et d'assemblage). Le processus de production ([processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)) : auditer la documentation existante → créer un template → laisser un agent extraire et peupler → compléter par des scripts pour les extractions mécaniques (props TypeScript, imports, git history) → itérer.

La distribution suit l'architecture [mcp-on-demand-vs-rules-always-on](../concepts/mcp-on-demand-vs-rules-always-on.md) : les fondations (tokens, espacement, typographie) en Rules always-on, les métadonnées de composants on-demand via MCP.

### Phase 3 — Synchroniser la documentation narrative (pour les humains)

La documentation narrative (MDX, site de docs) est le troisième flux. Le pipeline de référence ([pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)) lie chaque fichier `.mdx` à son frame Figma via un commentaire `<!-- figma-frame: FILE_ID/NODE_ID -->`. Deux modes : on-demand (le designer colle un lien Figma → mise à jour + PR en 30 secondes) et automatisé (GitHub Action hebdomadaire qui détecte les changements et génère les PRs). Pour les équipes dont la source de vérité est Notion, la variante Typeform ([pipeline-multi-destinations](../concepts/pipeline-multi-destinations.md)) alimente trois destinations simultanément (docs, MCP, sandbox) depuis une interface de contribution plus accessible.

Un fichier de writing guidelines joue le rôle de Rules always-on pour la cohérence stylistique de toutes les sorties.

### Boucle permanente — Maintenir et auto-améliorer

La boucle self-healing ([boucle-feedback-infrastructure](../concepts/boucle-feedback-infrastructure.md)) tourne en continu : Watch (détection de dérive), Analyze (scoring, priorisation), Execute (génération de PRs), Observe (vérification, rebouclage). L'état cible est la Phase 3 du [protocole-arc](../concepts/protocole-arc.md) (Compose) — l'agent implémente les correctifs détectés, avec des permissions définies par type d'action. Les métriques pertinentes ([metriques-adoption-ia-design-system](../concepts/metriques-adoption-ia-design-system.md)) : baisse des questions Slack, réduction de la variance entre runs, vitesse de détection des dérives.

## Schéma synthétique

```
Figma (structuré)
    │
    ├── [Phase 0] DESIGN.md ──────────────────► Prototypage / outils externes
    │
    ├── [Phase 1] Agent + Figma MCP ──────────► Spec formelle dans Figma → devs
    │              (uSpec : anatomie, API,
    │               tokens, a11y multi-plateforme)
    │
    ├── [Phase 2] Agent + extraction ─────────► Métadonnées JSON
    │              (5 étapes Morales Achiardi)    │
    │                                            ├── Rules always-on (fondations)
    │                                            └── MCP on-demand (composants)
    │
    └── [Phase 3] Pipeline Figma→docs ─────────► Documentation MDX/Mintlify → humains
                   (ou Notion→multi-destinations)
    
         ◄─────────────────── Boucle self-healing ──────────────────►
                   Watch / Analyze / Execute / Observe
```

## Lacunes identifiées dans le wiki

Le wiki ne documente pas encore de cas concret d'équipe ayant connecté les trois phases dans un workflow unique bout-en-bout. Les sources couvrent chaque phase séparément (Uber pour la Phase 1, Indeed/Typeform pour la Phase 2-3) mais pas leur intégration. [GAP]
