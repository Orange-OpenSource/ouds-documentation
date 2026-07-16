---
type: source
tags: [workflows, agent, documentation, sans-mcp, chatgpt-projects, audit, contribution]
created: 2026-06-18
updated: 2026-06-18
sources:
  - "[agent-workflows-design-system-teams](agent-workflows-design-system-teams.md)"
related:
  - "[workflows-agent-sans-mcp](../concepts/workflows-agent-sans-mcp.md)"
  - "[gerard-pamies](../entities/gerard-pamies.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[architecture-skills-rules-instructions](../concepts/architecture-skills-rules-instructions.md)"
---

## Agent Workflows for Design System Teams (Pàmies, 2026)

[gerard-pamies](../entities/gerard-pamies.md), UX Designer spécialisé en design systems, décrit comment son équipe utilise des agents IA pour six catégories de tâches — sans MCP, sans base vectorielle, sans infrastructure. L'approche repose sur un ChatGPT Project alimenté de fichiers MD structurés.

**Thèse centrale** : l'agent peut se comporter comme le membre le plus expert de l'équipe (réponses cohérentes, références aux décisions internes) simplement grâce au contexte fourni — pas grâce à une architecture technique sophistiquée. "What matters is providing clear prompts, reusable templates, and structured inputs like Markdown, ADRs, and token/component exports."

## Six workflows documentés

Les six workflows forment un spectre allant du plus analytique au plus opérationnel :

**Inventaire interne** — L'agent analyse la documentation technique du DS existant pour générer des résumés de composants, comparer des versions de DS (ancien vs actuel), et identifier des différences structurelles. Cas d'usage : onboarding, revues de composants.

**Recherche et benchmark** — À partir d'une liste de DS de référence, l'agent produit un benchmark comparatif (propriétés, comportements, patterns API). Ce travail prenait auparavant "beaucoup de temps" manuellement — maintenant utilisé avant de définir l'API table d'un nouveau composant.

**Génération de documentation** — L'agent produit des premières versions de documentation (Figma component set docs, variant documentation sous forme de matrice, pages de documentation composant). Utile pour les designers qui rédigent une documentation destinée aux développeurs. L'agent comble aussi les lacunes techniques (contraintes de plateforme, notes d'implémentation). Requiert un MD d'inventaire de composants comme input principal — voir [workflows-agent-sans-mcp](../concepts/workflows-agent-sans-mcp.md) pour le template.

**Support à la contribution** — Dans un modèle de contribution multi-équipes, les équipes peuvent demander à l'agent comment implémenter un composant dans une technologie spécifique. L'agent référence les ADRs et décisions internes pour retourner une réponse cohérente avec la gouvernance du DS — sans interrompre les membres seniors de l'équipe.

**Interrogation conversationnelle** — Poser des questions à l'agent plutôt que naviguer dans la documentation atomique. L'agent fait surface la connaissance dispersée entre fondations, tokens et composants.

**Audit de composants** — Export JSON depuis Figma via le plugin **Anova** → input pour QA et vérification de cohérence. C'est le workflow le plus technique, le plus proche d'une automation de gouvernance.

## Citations clés

"An agent can give expert-level answers to short prompts because it has project context." ([gerard-pamies](../entities/gerard-pamies.md))

"You get consistent answers similar to what you'd get from the most knowledgeable person on the team — without interrupting them." ([gerard-pamies](../entities/gerard-pamies.md))

## Évaluation

Source pratique et opérationnelle — la plus actionnable du vault pour les équipes sans infrastructure MCP. Complémentaire aux sources Wolosin/Kavcic/Gardner qui présupposent une stack technique avancée. Le positionnement "Step 1" dans le parcours vers le design system agentique est explicite : "For teams just beginning to introduce AI into design processes, this is an easy way to move from experimentation to real impact."

Données empiriques : aucune (pas de benchmark, pas de métriques). Style : pratique, concret, sans ambition théorique.
