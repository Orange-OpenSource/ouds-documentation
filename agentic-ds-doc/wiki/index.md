---
type: index
updated: 2026-07-09
---

# Index du Wiki

> Carte thématique du vault. Maintenu par Claude lors de chaque ingest.
> Navigation principale du vault dans Obsidian.

---

## Concepts

### Fondements stratégiques
- [[design-system-as-infrastructure]] — Le DS comme infrastructure non-optionnelle
- [[inversion-economique-code-comprehension]] — Le code est gratuit, la compréhension est chère
- [[seeds-vs-trees]] — Construire les fondations avant l'automatisation
- [[memoire-design-system]] — La mémoire institutionnelle (décisions, rejections, historiques) comme avantage concurrentiel réel
- [[design-system-comme-dataset]] — Le DS n'est plus le livrable ; c'est le dataset

### Architecture agentique
- [[systeme-de-design-agentique]] — Définition et propriétés d'un DS opéré par des agents
- [[lisibilite-machine-design-system]] — Rendre le DS compréhensible par une machine (benchmark JSON inclus)
- [[ia-comme-utilisateur]] — L'IA comme nouvelle audience du design system : reformuler, pas documenter plus
- [[trois-couches-composants-agents]] — Index, Métadonnées, Raisonnement (+ implémentation concrète)
- [[knowledge-graph-design-system]] — La carte relationnelle du système
- [[pipeline-intent-context-systeme]] — Le flux Intent → Contexte → Sortie
- [[protocole-arc]] — Cadre de maturité : Audit → Report → Compose
- [[user-vs-maintainer-ia]] — La frontière qui définit "agentique" (designer garant inclus)
- [[gouvernance-design-system-ia]] — Économie, automatisation et contraintes exécutables
- [[workflows-ia-metadata]] — Les 4 workflows activés par les métadonnées
- [[mode-exploration-vs-navigation]] — Sans carte, l'IA explore. Avec carte, elle navigue.
- [[architecture-skills-rules-instructions]] — Skills / Rules / Instructions + convergence avec le plugin de Wolosin
- [[boucle-feedback-infrastructure]] — Les rapports d'adoption améliorent l'infrastructure qui les produit
- [[mcp-on-demand-vs-rules-always-on]] — MCP retourne ce qu'on demande ; Rules portent toujours les fondations
- [[existence-vs-intent-violations]] — Linter vs gouvernance : existence du token vs conformité à son rôle
- [[concevoir-les-conditions]] — Designer les règles plutôt que les interfaces : abstraction et défi épistémique

### Langage et composition
- [[langage-design-system]] — Vocabulaire (tokens d'intent) + grammaire (règles d'assemblage) + contrats = fondation de la Phase 3 Compose

### Métadonnées de composants
- [[schema-metadata-composant]] — Le schéma à 9 sections pour rendre un composant queryable
- [[processus-generation-metadata-echelle]] — 5 étapes pour générer les métadonnées à grande échelle
- [[grammaire-composition-composants]] — Règles parent/enfant, ownership espacement, combinaisons interdites : comment les composants s'assemblent en interfaces
- [[contraintes-fixed-preferred-exploratory]] — Tripartition pour calibrer l'autonomie des agents : invariants non négociables, approches par défaut, zones de liberté

### Composants et tokens
- [[composants-context-aware]] — Le même composant se comporte différemment selon le contexte
- [[intent-token]] — Les tokens portent une signification sémantique, pas seulement des valeurs
- [[readable-vs-usable-token]] — Readable (pipeline compile) ≠ Usable (agent raisonne) : les 7 questions, expérience crimson/red600
- [[delegation-lens]] — La taille d'une échelle = nombre de décisions déléguées au consommateur ; chaque token sans règle est surface d'erreur
- [[priori-conflictuels-nommage]] — Les agents arrivent avec 10 grammaires contradictoires et les mélangent ; déclarer sa grammaire est le correctif
- [[dtcg-annotation-schema]] — Template DTCG : $description + $deprecated + $extensions — GitHub Primer comme référence canonique
- [[dsds-format]] — Design System Documentation Spec : format JSON ouvert pour documenter le how/why d'un DS — agentDocumentBlocks, 7 kinds d'entités, 16 document blocks, criteria vérifiables

### Implémentation MCP
- [[code-source-de-verite-mcp]] — JSDoc comme source de vérité unique pour humains et machines (approche New York State)

### Architecture de contexte et jugement
- [[architecture-contexte-agentique]] — Le DS comme architecture de couches progressives ; exposer le jugement, pas seulement les composants ; UX dans les relations entre composants
- [[invisibilite-produit-os-agentique]] — "Technically installed and practically invisible" : ce qui se passe quand les capacités d'une app ne sont pas exposées à la couche OS agentique (App Intents / Siri)

### Gouvernance et automatisation avancée
- [[shadow-ia-design-system]] — Usage IA par d'autres équipes sans le DS : 50% des équipes touchées, 6 modes de bypass, réponse économique pas réglementaire
- [[accessibilite-continue]] — Accessibilité baked-in plutôt que retrofit ; vérification à chaque composant/état/token
- [[systeme-design-proactif]] — Design system qui détecte des patterns émergents et anticipe ses propres évolutions
- [[protocole-pas-produit]] — Construire sur MCP rend la couche d'orchestration IA swappable sans reconstruire les intégrations

### Approches sans infrastructure MCP
- [[workflows-agent-sans-mcp]] — ChatGPT Project + fichiers MD : 6 workflows opérationnels sans MCP, sans base vectorielle (Step 1 avant toute infrastructure)

### IA UX et documentation des features IA
- [[modele-maturite-ia-design-system]] — Trois modèles de maturité orthogonaux : Kavcic (features IA pour humains), ARC (gouvernance), Bondar (opérabilité agent, niveaux 0-4)
- [[quatre-regles-ia-ux]] — Les 4 règles convergentes (marquer, expliquer, contrôler, échouer) + value gate + 15 questions du vrai pattern

### Infrastructure et outillage
- [[mcp-model-context-protocol]] — USB pour l'IA : standard de connexion aux outils (Figma MCP inclus)
- [[cli-vs-mcp]] — CLI pour la vitesse, MCP pour l'échelle
- [[format-toon]] — Format d'index token-efficient pour codebase agents
- [[pipeline-figma-docs-automatise]] — Figma MCP → Claude Code → Mintlify : docs auto-synchronisées (+ variante uSpec : specs formelles)
- [[generation-spec-agentique]] — Génération agentique de specs formelles (anatomie, API, accessibilité) directement dans Figma via MCP (Uber/uSpec)
- [[documentation-lag]] — Le délai structurel entre update Figma et update docs, et pourquoi le process ne suffit pas

---

## Entités

### Personnes
- [[ian-guisard]] — Lead Uber Base design system ; auteur uSpec ; génération agentique de specs via Figma Console MCP
- [[brad-frost]] — Auteur Atomic Design ; DS+AI vs vibe coding ; mouth coding
- [[alpesh-karanpuria]] — Designer / Design Systems Collective ; guide Figma-natif pour la lisibilité machine ; naming hiérarchique, Component Properties, Auto Layout
- [[gerard-pamies]] — UX Designer / Bootcamp ; workflows agent sans MCP ; 6 workflows pratiques ; ChatGPT Project + MD
- [[vicente-g]] — Sr. Design Systems Designer / Medium ; "exposer le jugement, pas les composants" ; DS comme knowledge API
- [[mehmet-celik]] — Auteur UX / Medium ; vision de l'automatisation DS et des systèmes proactifs
- [[romina-kavcic]] — Designer spécialisée DS, auteure thedesignsystem.guide, créatrice Tidy + Observatory
- [[cristian-morales-achiardi]] — Designer/développeur DS, auteur série Agentic DS, giorris.dev
- [[diana-wolosin]] — Senior Product Designer Netflix (ex-Indeed), auteure benchmark MCP/format
- [[jesse-gardner]] — Director User Research, New York State ; approche code-as-source-of-truth
- [[laura-fehre]] — Designer Advocate Figma ; "Guidelines are not laws"
- [[pj-onori]] — Auteur et mainteneur de DSDS (Design System Documentation Spec)

### Organisations & événements
- [[into-design-systems-conference]] — Conférence IDS 2025 et 2026

### Outils
- [[granola]] — Notes de réunion IA avec support MCP
- [[mintlify]] — Hébergement de documentation avec auto-deploy sur push Git
- [[arc-protocol-rpc]] — Protocole RPC open-source pour communication inter-agents (endpoint unique, post-quantique, ARC Ledger + ARC Compass)

---

## Synthèses

- [[deux-lectures-du-design-system-ia]] — DS opéré par des agents vs DS qui documente les features IA pour humains : deux lectures, deux champs

---

## Comparaisons

- [[astryx-vs-mui-atlaskit-shadcn]] — MUI vs Atlaskit vs Shadcn/ui vs Astryx : composition ouverte/scellée, styling lock-in, opérabilité agentique

---

## Questions archivées

- [[2026-06-17_comment-commencer-design-system-agentique]] — Comment commencer à faire évoluer mon design system vers l'agentique ? (2026-06-17)

---

## Sources ingérées

- [[design-system-most-important-asset-ai-era]] — Kavcic, "Why your design system is the most important asset in the AI era" (2026-03-29)
- [[towards-agentic-design-system]] — Morales Achiardi, "Towards an agentic design system" (2026-01-02)
- [[design-system-documentation-as-structured-metadata]] — Morales Achiardi, "Design system documentation as structured metadata" (2026-01-09)
- [[mapping-design-system-for-ai-agents]] — Morales Achiardi, "Mapping your design system for AI agents" (2026-01-14)
- [[agent-orchestration-for-design-systems]] — Morales Achiardi, "Agent orchestration for design systems" (2026-01-21)
- [[encoding-governance-agentic-design-systems]] — Morales Achiardi, "Encoding governance on agentic design systems" (2026-02-20)
- [[machine-readable-design-systems-designing-for-ai-as-a-user]] — Wolosin, "Machine-Readable Design Systems: Designing for AI as a User" (2026-03)
- [[how-to-automate-design-system-documentation]] — Kavcic, "How to Automate Design System Documentation" (2025-10)
- [[design-systems-that-document-ai]] — Kavcic, "Design Systems That Document AI" (2026-06-01)
- [[design-systems-mcp-complete-guide]] — IDS Conference 2026 (Wolosin, Gardner, Fehre, Kavcic), "Design Systems MCP: The Complete Guide"
- [[automating-design-system-ai-efficiency]] — Mehmet Celik, "Automating Your Design System with AI: The Next Frontier of Efficiency" (2025-10-04)
- [[self-healing-design-system]] — Kavcic, "The Self-Healing Design System" — Agentic DS Part 3 (2026-04-04) ⚠️ raw tronqué
- [[design-systems-for-ai-agents-paradigm-shift]] — Vicente G., "Design Systems for AI agents: The New Paradigm Shift" (2026-05-15)
- [[agentic-design-systems-2026-bradfrost]] — Brad Frost, "Agentic Design Systems in 2026" (2025-12-16) ⚠️ contenu mince, vidéos non transcrites
- [[agent-workflows-design-system-teams]] — Gerard Pàmies, "Stop 'Trying AI' — Start Using It: Agent Workflows for Design System Teams" (2026-03-01)
- [[designing-figma-design-system-ai-understand]] — Alpesh Karanpuria, "Designing a Figma Design System That AI Can Understand" (2026-03-10)
- [[50-design-token-files-one-problem]] — Kavcic, "50 design token files, one problem: your agents can't read the meaning" (2026-06-19) — audit de 50 fichiers sources, expérience contrôlée, template DTCG
- [[design-system-documentation-spec]] — PJ Onori, "Design System Documentation Spec (DSDS) 0.12.0" (2026-06-23) — premier standard ouvert de documentation machine-readable pour design systems
- [[uber-uspec-agentic-design-specs]] — Ian Guisard (Uber), "How Uber Built an Agentic System to Automate Design Specs in Minutes" (2026-03-11) — uSpec : génération de specs via Cursor + Figma Console MCP open-source
- [[into-design-systems-agentic-guide]] — Into Design Systems, "Agentic Design Systems: The Complete Guide" (2026) — synthèse AI DS Conf 2026 : Kavcic, Wolosin, Gardner, Jan Six, Frost
- [[meta-astryx-harsha-sridhar]] — Harsha Sridhar, "Meta Just Open-Sourced Its Design System. Here's Why It Matters!" (2026-07-06) — regard de marché externe : MUI / Atlaskit / Shadcn / Astryx, composants scellés vs ouverts
- [[state-of-ai-design-systems-2026-zeroheight]] — zeroheight, "The State of AI in Design Systems 2026" (mai 2026, N=123) — premier benchmark sectoriel : adoption 82%, MCP 47%, AI-readiness 17%, shadow AI 50%
- [[design-systems-contracts-not-libraries]] — Achiardi, "Design systems are contracts, not libraries" (mai 2026) — atomic design comme hiérarchie de contrats ; distinction contrat vs bibliothèque
- [[building-language-design-systems]] — Achiardi, "Building language for design systems" (juillet 2026) — vocabulaire d'intent + grammaire d'assemblage + contrats machine-lisibles = fondation conceptuelle de la Phase 3 Compose
- [[arc-protocol-agent-remote-communication]] — ARC Protocol (arc-protocol.org, 2026) — protocole RPC stateless inter-agents, chiffrement post-quantique, endpoint unique, ARC Ledger + ARC Compass

---

## Vue d'ensemble

→ [[overview]]

## Journal

→ [[log]]
