---
type: log
updated: 2026-07-09
---

## [2026-07-09] ingest | Building language for design systems (Achiardi, juillet 2026) (via veille web)
Thème de veille : arc protocol compose phase achiardi
Pages créées : [[building-language-design-systems]] (source), [[langage-design-system]] (concept)
Pages mises à jour : [[protocole-arc]] (+Phase 3 Compose développement conceptuel, +section disambiguation ARC, +sources juillet 2026), [[grammaire-composition-composants]] (+section vocabulaire/grammaire comme deux couches du langage), [[composant-comme-contrat]] (+section contrat formel systémique Achiardi mai 2026), [[cristian-morales-achiardi]] (+articles mai et juillet 2026, +développement Phase 3)
Note : Article fondateur du concept de [[langage-design-system]] — la Phase 3 (Compose) du [[protocole-arc]] présuppose un vocabulaire d'intent, une grammaire d'assemblage et des contrats machine-lisibles. Comble le trou conceptuel entre les articles techniques précédents (index, orchestration, gouvernance) et la composabilité agentique réelle.

---

## [2026-07-09] ingest | Design systems are contracts, not libraries (Achiardi, mai 2026) (via veille web)
Thème de veille : arc protocol compose phase achiardi
Pages créées : [[design-systems-contracts-not-libraries]] (source)
Pages mises à jour : [[composant-comme-contrat]] (+section design system comme contrat formel multi-niveaux, lien atomic design comme hiérarchie de contrats), [[cristian-morales-achiardi]] (déjà mis à jour dans l'ingest précédent)
Note : Article charnière manquant dans la série Achiardi — le maillon conceptuel entre la gouvernance technique (déjà ingérée) et le langage (juillet 2026). Pose la lecture "contrat" du design system à l'échelle du système entier, pas seulement du composant.

---

## [2026-07-09] ingest | Agent Remote Communication Protocol (ARC Protocol) — arc-protocol.org (via veille web)
Thème de veille : arc protocol compose phase achiardi
Pages créées : [[arc-protocol-agent-remote-communication]] (source), [[arc-protocol-rpc]] (entité)
Pages mises à jour : [[orchestration-multi-agents]] (+section ARC Protocol comme couche infrastructure, +disambiguation avec [[protocole-arc]] Achiardi), [[protocole-arc]] (+section disambiguation deux ARC dans le vault)
Note : Protocole RPC open-source pour communication inter-agents — distinct du [[protocole-arc]] d'Achiardi. Niche complémentaire à MCP et A2A : endpoint unique pour des centaines d'agents, chiffrement post-quantique (X25519 + Kyber-768), ARC Ledger (registre) + ARC Compass (ranking sémantique). Première entrée infrastructure réseau dans le vault.

---

## [2026-07-08] ingest | The Design System Advantage Is Memory (Romina Kavcic)

Pages créées : [[design-system-advantage-is-memory]] (source), [[memoire-design-system]] (concept), [[design-system-comme-dataset]] (concept)
Pages mises à jour : [[knowledge-graph-design-system]] (+section graphe vs pile de fichiers, QMD comme étape intermédiaire), [[mode-exploration-vs-navigation]] (+section QMD comme navigation légère), [[gouvernance-design-system-ia]] (+section coût économique du mauvais contexte : Microsoft/Claude Code, Uber, Nvidia, Gartner, METR), [[inversion-economique-code-comprehension]] (+données Kavcic sur le coût des systèmes agentiques), [[romina-kavcic]] (+article mai 2026), [[design-system-advantage-is-memory]] (fiche source complète)
Note : Reformulation tranchante de l'IA-readiness — l'avantage n'est pas le nombre d'outils MCP mais la mémoire institutionnelle rendue retrievable. Deux nouveaux concepts structurants : la distinction visible 10%/invisible 90% (décisions et historiques vs tokens et docs), et la thèse terminale "le design system est le dataset". Introduit QMD (Tobi Lütke) comme outil de test de signal sur un corpus. Crée une tension nommée avec les sources qui mesurent la maturité agentique au nombre d'outils exposés.

---

## [2026-07-07] ingest | Your design system is fragmenting into agent files (Murphy Trueman)

Pages créées : [[your-design-system-fragmenting-agent-files]] (source), [[agents-md-format]] (concept), [[dispersion-decision-design]] (concept), [[prompt-injection-design-system]] (concept)
Pages mises à jour : [[architecture-skills-rules-instructions]] (+section SKILL.md recette vs description, portabilité vs exécution inconsistante, Skills Figma bundlés), [[design-md-format]] (+section position dans la pile 3 formats, validation empirique Wolosin, calibrage optimal green-field vs codebase existant, distinction DTCG), [[gouvernance-design-system-ia]] (+section gouvernance des coutures entre formats, +section sécurité des fichiers d'instructions / prompt injection), [[lisibilite-machine-design-system]] (+section Storybook Component Manifest + Zeroheight MCP comme pattern de lisibilité depuis contenu existant), [[murphy-trueman]] (+article mai 2026), [[diana-wolosin]] (+confirmation benchmark par Trueman avec chiffres précis : 77 composants, 1056 prompts, 8 configurations)
Note : Article de synthèse par Trueman qui cartographie la pile complète des formats agent-facing (AGENTS.md / SKILL.md / DESIGN.md + Storybook manifest + MCP). Trois contributions nettes absentes du corpus : (1) AGENTS.md comme concept autonome — le format le plus ancien, le plus actionnable, et le plus ignoré comme sujet propre ; (2) la dispersion d'une décision de design unique dans cinq emplacements sans lien automatique — problème de gouvernance, pas de technologie ; (3) le prompt injection via les fichiers d'instructions — angle de sécurité absent de tous les modèles de gouvernance précédents. Confirme le benchmark Wolosin comme référence établie du domaine ("JSON for MCP, Markdown for LLM").

---

## [2026-07-07] ingest | The human layer in agentic design systems (Cristian Morales Achiardi)

Pages créées : [[human-layer-agentic-design-systems]] (source), [[designops-devops-seam]] (concept)
Pages mises à jour : [[cristian-morales-achiardi]] (+série complète 7 parties, +contexte Enara sole-designer, +accountability totale), [[concevoir-les-conditions]] (+accountability comme conséquence, +incident échelle jaune, +niveau environnement), [[accountability-gap-ia]] (+cas inverse : gap résolu par traçabilité architecturale, +distinction failure encodée vs failure composite), [[boucle-feedback-infrastructure]] (+confiance comme condition d'activation de la boucle), [[gouvernance-design-system-ia]] (+boucle humaine : limite du système agentique sur la qualité de l'encodage)
Note : Article conclusif de la série Morales Achiardi. Contribution principale : le système scale l'exactitude *et* les erreurs — la gouvernance agentique ne garantit que l'exécution de ce qui a été encodé, pas la qualité de l'encodage. Introduit la couture designops-devops comme zone de travail propre. Résout partiellement l'accountability gap (pour les décisions encodées) tout en précisant sa limite (pour les failures composites émergentes).

## [2026-07-06] ingest | 20 AI workflows that save design system teams 10+ hours a week (Romina Kavcic)

Pages créées : [[20-ai-workflows-design-system-teams]] (source), [[audit-tokens-playwright]] (concept), [[bypass-patterns-comme-user-research]] (concept), [[assistant-ia-24h]] (concept), [[context7]] (entité), [[openclaw]] (entité), [[plugma]] (entité)
Pages mises à jour : [[architecture-skills-rules-instructions]] (+Skills métier concrets : token-migration-assistant, component-audit, documentation-standards, brand-guidelines, figma-variables-generator ; +template custom Skill ; +token drift audit Skill), [[metriques-adoption-ia-design-system]] (+build-time signals : imports, drift counts, bypass signals, PR delta), [[documentation-lag]] (+migration guides, +release notes pour non-spécialistes), [[pipeline-figma-docs-automatise]] (+cron job hebdomadaire re-sync, +pipeline génération composants symétrique), [[romina-kavcic]] (+source, +résumé de l'article)
Note : Source catalogue opérationnel — valeur non pas théorique mais tactique. Trois patterns nouveaux : Playwright Planner/Generator/Healer pour audits continus, bypass patterns interprétés comme user research (renversement paradigmatique), assistant self-hosted 24/7 (OpenClaw). Enrichissement majeur de l'architecture Skills avec des exemples nommés et des templates copiables. Trois nouveaux outils référencés : Context7 (docs live), OpenClaw (assistant self-hosted), plugma (toolchain plugins Figma).

---

## [2026-07-06] ingest | Making product documentation work for humans and AI (Geri Reid)

Pages créées : [[making-product-docs-work-humans-ai-gerireid]] (source), [[cinq-questions-documentation-produit]] (concept), [[geri-reid]] (entité)
Pages mises à jour : [[documentation-lag]] (+section "de la friction à l'outcome actif" — distinction humain/LLM face à une doc médiocre, hallucination de composants), [[lisibilite-machine-design-system]] (+section lisibilité machine comme corollaire de la lisibilité humaine, dual-audience, cadre des cinq questions)
Note : Source de praticien avec un cadrage tactique distinct du corpus existant : là où le vault part de l'architecture technique pour aller vers la documentation, Reid part de la pratique quotidienne des équipes. Contribution principale : le principe dual-audience (le même effort améliore simultanément lisibilité humaine et machine) qui renverse le cadrage "surcoût" habituel de la lisibilité machine. Concept original : [[cinq-questions-documentation-produit]] — cadre de structuration accessible pour les 83 % d'équipes non encore en phase d'optimisation agentique. Saut qualitatif documenté : documentation médiocre = friction humaine vs documentation médiocre = outcome actif erroné pour les LLMs.

---

## [2026-07-06] ingest | Your design system might be AI-ready. Your organisation probably isn't. (Murphy Trueman)

Pages créées : [[design-system-ai-ready-organisation-not]] (source), [[accountability-gap-ia]] (concept), [[murphy-trueman]] (entité)
Pages mises à jour : [[gouvernance-design-system-ia]] (+section gouvernance organisationnelle — droits décisionnels, standard de qualité explicite, accountability composite, adaptation contribution ; +relation gouvernance technique/organisationnelle), [[overview.md]] (+tension readiness technique vs organisationnelle)
Note : Source qui introduit explicitement la dimension organisationnelle comme problème distinct et plus difficile que la préparation technique. Contribution centrale : l'[[accountability-gap-ia]] — le vide de responsabilité sur les failures composites (composants accessibles → parcours inaccessible, éléments on-brand → expérience off-brand) que aucune contrainte technique ne capture. Comble la lacune documentée dans [[gouvernance-design-system-ia]] ("Who's accountable for automated updates that go live ?"). Données : 55 % des product builders prennent des tâches hors périmètre (Figma research), workflow linéaire "collapsed" (Paige Costello, VP Product Figma).

## [2026-07-06] ingest | The State of AI in Design Systems 2026 — Full Report (zeroheight, N=123)

Pages créées : [[state-of-ai-design-systems-2026-zeroheight]] (source), [[shadow-ia-design-system]] (concept)
Pages mises à jour : [[metriques-adoption-ia-design-system]] (+adoption tools breakdown Claude 74%/Figma Make 56%, satisfaction par cas usage, MCP 47%), [[gouvernance-design-system-ia]] (+shadow AI comme problème de gouvernance externe, +politique IA légère), [[lisibilite-machine-design-system]] (+17% AI-readiness sectoriel), [[mcp-model-context-protocol]] (+47% adoption sectoriel, +6 cas d'usage terrain), [[documentation-lag]] (+documentation comme goulot IA), [[overview]] (+nouvelles tensions adoption/shadow AI/readiness)
Note : Premier benchmark sectoriel complet sur l'IA dans les DS (N=123, mai 2026). Rapport distinct du blog post "Design Systems Report 2026" (mars 2026). Données clés : 82% adoption, 47% MCP, 17% AI-readiness, 50% shadow AI. Introduit [[shadow-ia-design-system]] comme concept absent du corpus antérieur. Valide empiriquement à grande échelle les thèses du vault sur la lisibilité machine.

---

## [2026-07-06] ingest | Meta Just Open-Sourced Its Design System. Here's Why It Matters! (Harsha Sridhar)

Pages créées : [[meta-astryx-harsha-sridhar]] (source), [[astryx-vs-mui-atlaskit-shadcn]] (comparaison)
Pages mises à jour : [[systeme-de-design-agentique]] (+section validation de marché externe, +lien comparaison), [[grammaire-composition-composants]] (+section composants scellés vs ouverts, implication agentique)
Note : Source externe complémentaire à [[meta-astryx-design-system]] (blog officiel Meta). Apport principal : premier regard de marché comparatif dans le corpus (MUI / Atlaskit / Shadcn / Astryx) et formulation "first from a major vendor to answer with product, not a footnote" — validation externe de la thèse agentique centrale du vault. Introduit l'axe composants scellés vs ouverts comme dimension d'opérabilité agentique, en complément de la lisibilité machine au niveau métadonnées.

---

# Journal du Wiki

> Fichier append-only. Ne jamais modifier les entrées passées. Ajouter uniquement en bas.
> Format des entrées : `## [AAAA-MM-JJ] <type> | <titre>`
> Types : `ingest` | `query` | `lint` | `gap` | `init`

---

## [2026-06-17] init | Vault créé

Structure initiale générée. Domaine à définir.
Pages créées : [[index]], [[overview]], ce fichier.
Note : vault vide, prêt pour les premières ingestions.

---

## [2026-06-17] ingest | Why your design system is the most important asset in the AI era

Pages créées : [[design-system-most-important-asset-ai-era]], [[design-system-as-infrastructure]], [[systeme-de-design-agentique]], [[inversion-economique-code-comprehension]], [[lisibilite-machine-design-system]], [[trois-couches-composants-agents]], [[composants-context-aware]], [[mcp-model-context-protocol]], [[cli-vs-mcp]], [[intent-token]], [[seeds-vs-trees]], [[pipeline-intent-context-systeme]], [[knowledge-graph-design-system]], [[romina-kavcic]], [[into-design-systems-conference]], [[granola]]
Pages mises à jour : [[overview]], [[index]], [[log]]
Note : première ingestion — pose le cadre conceptuel complet du domaine (DS agentique, inversion économique, trois couches, MCP). La partie 3 de la série Kavcic (self-healing DS) est disponible dans raw/ — à ingérer.

---

## [2026-06-17] ingest | Towards an agentic design system

Pages créées : [[towards-agentic-design-system]], [[protocole-arc]], [[user-vs-maintainer-ia]], [[gouvernance-design-system-ia]], [[format-toon]], [[cristian-morales-achiardi]]
Pages mises à jour : [[lisibilite-machine-design-system]], [[trois-couches-composants-agents]], [[systeme-de-design-agentique]], [[knowledge-graph-design-system]], [[overview]], [[index]], [[log]]
Note : valide empiriquement la thèse de lisibilité machine (2x vitesse, 54 % précision, 0 faux négatif) ; introduit le protocole ARC et la distinction User/Maintainer comme critère définitoire du système agentique. Deux auteurs convergent maintenant sur les fondamentaux avec des vocabulaires différents (Kavcic : machine-readable ; Morales : AI-ready infrastructure).

---

## [2026-06-17] ingest | Design system documentation as structured metadata

Pages créées : [[design-system-documentation-as-structured-metadata]], [[schema-metadata-composant]], [[processus-generation-metadata-echelle]], [[workflows-ia-metadata]]
Pages mises à jour : [[trois-couches-composants-agents]], [[lisibilite-machine-design-system]], [[gouvernance-design-system-ia]], [[index]]
Note : zoome sur la couche 2 (métadonnées) avec un schéma à 9 sections et un argument clé — la documentation structurée est une traduction du savoir existant, pas une création. Ajoute la validation pré-génération comme mécanisme de gouvernance proactif. Clarifie que l'obstacle à la lisibilité machine est un changement de paradigme, pas un volume de travail.

---

## [2026-06-17] ingest | Mapping your design system for AI agents

Pages créées : [[mapping-design-system-for-ai-agents]], [[mode-exploration-vs-navigation]]
Pages mises à jour : [[knowledge-graph-design-system]] (+deep tracing, +import vs instance count, +quoi/où/devrait-on), [[format-toon]] (+génération automatique, +ROI), [[gouvernance-design-system-ia]] (+dette technique composée), [[index]]
Note : zoome sur la couche 1 (index) — complète la couche 2 de la source précédente. Introduit la distinction Exploration/Navigation comme cadre central et la dette technique composée comme vrai coût de la non-gouvernance. La complémentarité métadonnées/index est maintenant formalisée dans le vault (quoi / où / devrait-on).

---

## [2026-06-17] ingest | How to Automate Design System Documentation

Pages créées : [[how-to-automate-design-system-documentation]], [[documentation-lag]], [[pipeline-figma-docs-automatise]], [[mintlify]]
Pages mises à jour : [[romina-kavcic]] (+pipeline Figma→docs, mintlify), [[boucle-feedback-infrastructure]] (+variante documentation entièrement automatisée), [[mcp-model-context-protocol]] (+usage Figma MCP pour documentation), [[processus-generation-metadata-echelle]] (+variante Kavcic Figma→MDX), [[index]], [[log]]
Note : premier article pratique et opérationnel de Kavcic — descend du niveau conceptuel ("AI-ready design system") au niveau implémentation concrète (stack Figma+Claude Code+Mintlify+GitHub Actions). Introduit le [[documentation-lag]] comme problème nommé et le [[pipeline-figma-docs-automatise]] comme solution architecturale. La distinction on-demand/automatisé du pipeline fait écho à la distinction MCP on-demand/Rules always-on de Wolosin.

---

## [2026-06-17] ingest | Machine-Readable Design Systems: Designing for AI as a User

Pages créées : [[machine-readable-design-systems-designing-for-ai-as-a-user]], [[diana-wolosin]], [[ia-comme-utilisateur]], [[mcp-on-demand-vs-rules-always-on]]
Pages mises à jour : [[lisibilite-machine-design-system]] (+benchmark JSON, 1056 prompts, $300 vs $1500), [[format-toon]] (+tension avec benchmark Wolosin), [[schema-metadata-composant]] (+implémentation Indeed MDX→parsers→JSON→Vectra), [[mcp-model-context-protocol]] (+flux RAG 7 étapes, nature on-demand), [[architecture-skills-rules-instructions]] (+convergence plugin Wolosin), [[processus-generation-metadata-echelle]] (+pipeline auto-régénérant Indeed), [[index]], [[log]]
Note : premier article non-Morales Achiardi — [[diana-wolosin]] apporte la validation empirique la plus rigoureuse du corpus (benchmark 8 configs MCP) et nomme un problème structurel absent de la série Morales Achiardi : le MCP est on-demand, les fondations cassent systématiquement si elles ne sont pas portées par des Rules always-on. Résout aussi l'orphelin [[diana-wolosin]] signalé depuis l'ingest 2.

---

## [2026-06-17] ingest | Encoding governance on agentic design systems

Pages créées : [[encoding-governance-agentic-design-systems]], [[existence-vs-intent-violations]], [[concevoir-les-conditions]]
Pages mises à jour : [[gouvernance-design-system-ia]] (+orchestration vs gouvernance, +token auditor v1/v2, +contraintes exécutables), [[user-vs-maintainer-ia]] (+designer who guarantees, +défi épistémique du maintainer humain), [[intent-token]] (+violations d'intent vs violations d'existence), [[index]], [[log]]
Note : article conclusif de la série Morales Achiardi — pose la distinction linter/gouvernance (existence vs intent) et le changement de niveau d'abstraction du rôle designer (concevoir les interfaces → concevoir les conditions). Documente le cas Enara en production : token auditor v1→v2, 43→64 violations, FilterBar à 0 violation.

---

## [2026-06-17] ingest | Design Systems MCP: The Complete Guide (via veille web)

Thème de veille : agentic design systems
Pages créées : [[design-systems-mcp-complete-guide]], [[jesse-gardner]], [[laura-fehre]], [[code-source-de-verite-mcp]]
Pages mises à jour : [[mcp-on-demand-vs-rules-always-on]] (+tension Fehre "guidelines are not laws"), [[gouvernance-design-system-ia]] (+tension Fehre vs contraintes exécutables), [[mcp-model-context-protocol]] (+trois modèles d'implémentation : Indeed/NY State/Kavcic), [[romina-kavcic]] (+Tidy 66 MCP tools, +Observatory), [[index]], [[log]]
Note : source pivot — introduit deux nouvelles entités (Jesse Gardner, Laura Fehre) et un troisième modèle d'implémentation MCP (code-first JSDoc → manifest) aux côtés des approches MDX-first (Indeed) et Figma-first (Kavcic). La formule de Fehre ("guidelines are not laws, the prompt wins") crée la tension la plus productive du vault : elle délimite précisément ce que les Rules peuvent faire (orienter) vs ce que les contraintes exécutables font (bloquer).

---

## [2026-06-17] ingest | Design Systems That Document AI

Pages créées : [[design-systems-that-document-ai]], [[modele-maturite-ia-design-system]], [[quatre-regles-ia-ux]], [[deux-lectures-du-design-system-ia]]
Pages mises à jour : [[romina-kavcic]] (+article juin 2026, +modele-maturite, +quatre-regles), [[systeme-de-design-agentique]] (+deuxième lecture du terme agentique, +deux-lectures), [[gouvernance-design-system-ia]] (+Level 4 Fluent RAI rubric, +parallèle existence-vs-intent), [[index]], [[log]]
Note : article pivot qui introduit une deuxième lecture du "design system et IA" — non plus l'IA opérant le DS, mais le DS documentant les features IA pour humains. Le signal fort : convergence indépendante de 7 organisations sur 4 règles identiques. Produit la première synthèse du vault ([[deux-lectures-du-design-system-ia]]) qui formalise la distinction entre les deux lectures et prévient la confusion conceptuelle.

[GAP] noté dans [[deux-lectures-du-design-system-ia]] : aucune source dans le vault sur l'implémentation concrète des quatre règles dans un produit réel, ni sur la construction de composants de maturité Niveau 2-3.

---

## [2026-06-18] ingest | Agentic Design Systems in 2026 (Brad Frost)

Pages créées : [[agentic-design-systems-2026-bradfrost]], [[brad-frost]]
Pages mises à jour : [[systeme-de-design-agentique]] (+DS+AI vs vibe coding, +mouth coding), [[mcp-model-context-protocol]] (+Storybook MCP comme 4ème modèle d'implémentation), [[index]], [[log]]
Note : source intentionnellement mince (article-billet, contenu essentiel dans des vidéos non transcrites). Deux apports nets : la distinction DS+AI vs vibe coding — la contrainte au design system comme ce qui différencie génération IA de qualité de génération IA improvisée — et le terme "mouth coding" pour les workflows collaboratifs cross-disciplines. Brad Frost est une entité majeure du domaine (Atomic Design) jusqu'ici absente du vault.

---

## [2026-06-18] ingest | Design Systems for AI agents: The New Paradigm Shift (Vicente G.)

Pages créées : [[design-systems-for-ai-agents-paradigm-shift]], [[vicente-g]], [[architecture-contexte-agentique]]
Pages mises à jour : [[ia-comme-utilisateur]] (+knowledge API, +nouvelles responsabilités d'équipe : mauvais exemples intentionnels, recettes de patterns, standards vérifiables), [[index]], [[log]]
Note : article analytique sans données empiriques propres, mais avec une rigueur conceptuelle supérieure aux articles d'awareness. Trois apports nets : (1) "exposer le jugement, pas seulement les composants" — la formulation la plus directe du vault sur ce sujet ; (2) "L'UX vit dans les relations entre composants, pas dans les composants" — nuance qui complète la couche 3 de Kavcic ; (3) modèle de couches progressives de contexte par phase de tâche (fondations → règles composants → qualité/composition). Converge avec Wolosin et Morales Achiardi depuis un angle indépendant, sans les citer.

---

## [2026-06-18] re-ingest | Machine-Readable Design Systems: Designing for AI as a User (Wolosin)

Source déjà ingérée — re-ingestion du raw pour capturer le contenu non extrait lors de la session précédente.
Pages créées : aucune
Pages mises à jour : [[mcp-model-context-protocol]] (+Tony Rucker, +précision "not Figma MCP, not Tailwind" pour les 4300 prototypes Indeed), [[gouvernance-design-system-ia]] (+mesurer les hallucinations comme métrique d'infrastructure)
Note : deux ajouts nets. "Hallucinations as a metric, not a feeling" (Wolosin) formalise une pratique de gouvernance absente du vault — mesurer le taux d'erreurs du MCP comme un indicateur quantifiable, pas une impression. La précision "not Figma, not Tailwind" confirme que l'approche Indeed est documentation-led pure (React + DS, pas Figma-first).

---

## [2026-06-18] ingest | The Self-Healing Design System (Kavcic, Part 3)

Pages créées : [[self-healing-design-system]], [[protocole-pas-produit]]
Pages mises à jour : [[boucle-feedback-infrastructure]] (+boucle Watch/Analyze/Execute/Observe), [[seeds-vs-trees]] (+validation en production), [[romina-kavcic]] (+Part 3, architecture production, benchmark multi-modèles), [[index]], [[log]]
Note : source tronquée dans le raw (sections "what AI cannot do" et "three phases" absentes). Ce qui est disponible apporte : l'architecture MCP de production la plus complète du vault (12 outils), la boucle self-healing formalisée en 4 étapes, le premier benchmark multi-modèles spécifiquement ciblé sur le raisonnement de design system, et le principe [[protocole-pas-produit]] qui est la justification architecturale profonde du choix MCP.

---

## [2026-06-18] ingest | Automating Your Design System with AI: The Next Frontier of Efficiency

Pages créées : [[automating-design-system-ai-efficiency]], [[mehmet-celik]], [[accessibilite-continue]], [[systeme-design-proactif]]
Pages mises à jour : [[boucle-feedback-infrastructure]] (+extension systèmes proactifs), [[gouvernance-design-system-ia]] (+stat 40% NN/g, +question accountability pour updates automatisées), [[intent-token]] (+synchronisation cross-platform, +détection prédictive d'overrides), [[index]], [[log]]
Note : source d'orientation "awareness" — moins technique que le corpus Morales Achiardi/Wolosin/Gardner, mais apporte deux concepts genuinement nouveaux ([[accessibilite-continue]] comme renversement structurel du modèle réactif, [[systeme-design-proactif]] comme articulation concrète de la Phase 3 du protocole ARC), une donnée chiffrée utile (40% maintenance, NN/g 2022), et la question ouverte de responsabilité pour les décisions automatisées — lacune organisationnelle absente du corpus technique.

---

## [2026-06-18] ingest | Designing a Figma Design System That AI Can Understand (Karanpuria)

Pages créées : [[designing-figma-design-system-ai-understand]], [[alpesh-karanpuria]]
Pages mises à jour : [[lisibilite-machine-design-system]] (+structuration Figma-native : naming hiérarchique, Component Properties, Auto Layout comme signal comportemental), [[index]], [[log]]
Note : source de niveau "awareness + guide pratique", sans données empiriques. Apport net : le corpus du vault était quasi-exclusivement orienté metadata/MCP/code — Karanpuria documente la couche en amont, celle du fichier Figma lui-même. Les trois pratiques ajoutées (naming `Category/Component/Variant/State/Size`, Component Properties, Auto Layout) sont des prérequis à une bonne extraction de métadonnées, et manquaient au corpus.

---

## [2026-06-18] ingest | Stop 'Trying AI' — Start Using It: Agent Workflows for Design System Teams (Pàmies)

Pages créées : [[agent-workflows-design-system-teams]], [[gerard-pamies]], [[workflows-agent-sans-mcp]]
Pages mises à jour : [[ia-comme-utilisateur]] (+externaliseur de savoir tribal, +Gerard Pàmies angle), [[architecture-skills-rules-instructions]] (+ADRs comme Rules sans infrastructure)
Note : source pivot dans le corpus du vault — la seule à documenter explicitement une approche "no MCP required" comme stratégie délibérée plutôt que comme limitation. [[workflows-agent-sans-mcp]] formalise l'Étape 1 de la QUERY [[2026-06-17_comment-commencer-design-system-agentique]] : 6 workflows concrets opérationnels via ChatGPT Project + MD uploadés, sans base vectorielle. La tension architecturale est documentée : efficace pour des tâches ponctuelles, mais ne résolut pas le problème "always-on" identifié par Wolosin. Pàmies est la 9ème entité-personne du vault — le seul à représenter la perspective "équipe en démarrage".

---

## [2026-06-17] query | Comment commencer à faire évoluer mon design system vers l'agentique ?

Pages lues : [[seeds-vs-trees]], [[protocole-arc]], [[trois-couches-composants-agents]], [[ia-comme-utilisateur]], [[deux-lectures-du-design-system-ia]], [[mcp-on-demand-vs-rules-always-on]], [[code-source-de-verite-mcp]], [[concevoir-les-conditions]], [[schema-metadata-composant]], [[processus-generation-metadata-echelle]], [[pipeline-figma-docs-automatise]]
Archive : [[2026-06-17_comment-commencer-design-system-agentique]]
Note : synthèse stratégique en 4 étapes (0 : reformuler, 1 : workflows sans infra, 2 : trois couches dans l'ordre, 3 : choix du modèle MCP, 4 : architecture always-on) + déplacement épistémique du rôle designer. Aucun GAP identifié — la question est bien couverte par le corpus actuel.

---

## [2026-06-19] query | Is it a good idea to create one skill per DS component?

Pages lues : [[architecture-skills-rules-instructions]], [[mcp-on-demand-vs-rules-always-on]], [[trois-couches-composants-agents]], [[schema-metadata-composant]], [[lisibilite-machine-design-system]], [[knowledge-graph-design-system]], [[composants-context-aware]], [[intent-token]]
Archive : [[2026-06-19_skill-per-component]]
Note : question affinée en deux versions. Version 1 (skills comme stores de données) : erreur de catégorie nette. Version 2 (skills comme raisonneurs d'intent contextuel) : l'intuition est juste mais l'architecture redistribue différemment — l'intent et le contexte vivent dans les sections `aiHints` et `usage.antiPatterns` des métadonnées JSON (queryables via MCP), et un seul skill `/ai-ds-composer` raisonne sur l'ensemble du graphe. La clé : les tâches importantes sont toujours cross-composants, et seul un raisonneur centralisé lisant des données distribuées peut les traiter.

---

## [2026-06-17] ingest | Agent orchestration for design systems

Pages créées : [[agent-orchestration-for-design-systems]], [[architecture-skills-rules-instructions]], [[boucle-feedback-infrastructure]]
Pages mises à jour : [[trois-couches-composants-agents]] (+architecture Skills/Rules/Instructions dans couche 3), [[knowledge-graph-design-system]] (+algorithme deep tracing complet), [[gouvernance-design-system-ia]] (+efficiency rate, +dérive intentionnelle vs involontaire), [[index]]
Note : articule l'architecture d'orchestration (Skills/Rules/Instructions/CLAUDE.md comme routeur) et introduit la boucle de feedback comme mécanisme d'auto-amélioration de l'infrastructure — l'étape intermédiaire entre Phase 2 (Report) et Phase 3 (Compose) du protocole ARC. La distinction dérive intentionnelle vs involontaire est un apport diagnostique clé.

## [2026-06-22] query | Parcours de concepts pour comprendre l'AI readiness
Pages lues : [[inversion-economique-code-comprehension]], [[seeds-vs-trees]], [[lisibilite-machine-design-system]], [[readable-vs-usable-token]], [[trois-couches-composants-agents]], [[intent-token]], [[delegation-lens]], [[priori-conflictuels-nommage]], [[existence-vs-intent-violations]], [[schema-metadata-composant]], [[dtcg-annotation-schema]], [[protocole-arc]], [[modele-maturite-ia-design-system]], [[knowledge-graph-design-system]], [[concevoir-les-conditions]]
Archive : [[2026-06-22_parcours-concepts-ai-readiness]]
Note : Parcours en 15 concepts, 7 niveaux. Gap identifié : l'implémentation bout-en-bout (DTCG annoté → MCP → audit automatisé) n'est pas encore couverte de façon intégrée dans le vault.

## [2026-06-22] ingest | 50 design token files, one problem: your agents can't read the meaning
Pages créées : [[50-design-token-files-one-problem]] (source), [[readable-vs-usable-token]], [[delegation-lens]], [[priori-conflictuels-nommage]], [[dtcg-annotation-schema]]
Pages mises à jour : [[intent-token]] (+expérience crimson/red600, +état du terrain 2026), [[romina-kavcic]] (+nouvelle source), [[lisibilite-machine-design-system]] (+tension readable≠usable), [[overview]] (+tension, +carte conceptuelle)
Note : Source empiriquement la plus solide du corpus sur les tokens — audit réel de 50 fichiers sources + expérience contrôlée. Introduce la distinction readable/usable qui affine et corrige la notion de machine-readable telle que définie jusqu'ici. GitHub Primer devient le seul exemple de l'art avec règles de non-usage dans le fichier. Nouveau gap fermé : on sait maintenant que 1/50 systèmes a atteint le niveau agent-usable.

## [2026-06-22] query | Que doit contenir le champ "description" d'un design token ?
Pages lues : [[intent-token]], [[lisibilite-machine-design-system]], [[existence-vs-intent-violations]], [[schema-metadata-composant]], [[2026-06-19_audit-ai-readiness-ouds-documentation]]
Archive : [[2026-06-22_description-field-design-token]]
Note : Réponse opérationnelle — format string JSON, 2-4 phrases, structure rôle/contexte exclusif/distinctions/anti-pattern. Gap identifié : aucune source ne propose un modèle par catégorie de token (couleurs d'action, statut, élévation…). C'est le prochain chantier d'opérationnalisation de l'audit OUDS.

## [2026-06-22] ingest | Your Design System Is Not Ready for AI Agents
Pages créées : [[your-design-system-is-not-ready-for-ai-agents]] (source), [[niveaux-confiance-actions-agentiques]], [[jan-six]], [[sil-bormuller]]
Pages mises à jour : [[documentation-lag]] (+MAPE-K loop, +30-40% stat, +dérive agentique comme failure mode), [[gouvernance-design-system-ia]] (+niveaux de confiance par action, +Jan Six), [[mcp-on-demand-vs-rules-always-on]] (+Brad Frost progressive disclosure, +AGENTS.md), [[trois-couches-composants-agents]] (+Spotify Encore Foundation/Style/Behavior, +context bubbles), [[brad-frost]] (+IDS 2026, +AGENTS.md), [[romina-kavcic]] (+MAPE-K, +30-40%, +niveaux de confiance), [[diana-wolosin]] (+4300 prototypes Indeed, +citation), [[into-design-systems-conference]] (+AI DS Conf 2026, +5 speakers), [[seeds-vs-trees]] (+consensus de conférence)
Note : Source de synthèse conférence — cinq failure modes en production documentés par cinq équipes différentes (Indeed, GitHub, Spotify, Kavcic). Ajoute le cadre MAPE-K à la dérive documentaire, formalise les niveaux de confiance agentiques, introduit l'architecture Spotify "context bubbles", et confirme seeds-vs-trees comme consensus de terrain.

## [2026-06-22] ingest | Design System Documentation at Scale: Leveraging AI and Automation (Typeform)
Pages créées : [[typeform-design-system-documentation-scale-ai]] (source + raw), [[notion-cms-design-system]], [[pipeline-multi-destinations]], [[fernando-coelho]]
Pages mises à jour : [[pipeline-figma-docs-automatise]] (+variante Notion multi-destinations), [[processus-generation-metadata-echelle]] (+pipeline Typeform), [[log]]
Note : Source d'octobre 2025, antérieure au reste du corpus. Approche plus accessible que les architectures avancées du vault — Notion comme CMS pour démocratiser la contribution, un seul pipeline alimentant docs + MCP + sandbox. Tension explicite avec l'approche JSON-first de Wolosin : priorité à la contribution humaine plutôt qu'à la précision agentique. Position dans le vault : entrée accessible au protocole ARC, avant l'optimisation de format.

## [2026-06-22] ingest | Miro AI Design System: MCP + Claude Code Skills Playbook
Pages créées : [[miro-ai-design-system-mcp-claude-code-skills]] (source), [[ia-comme-nouvelle-recrue]], [[skills-avant-mcp]], [[metriques-adoption-ia-design-system]], [[andressa-lombardo]], [[eddie-machado]], [[aura-miro]]
Pages mises à jour : [[ia-comme-utilisateur]] (+tension nouvelle-recrue vs utilisateur), [[lisibilite-machine-design-system]] (+client-side rendering bloqueur), [[schema-metadata-composant]] (+3 champs icônes + do-not-use), [[readable-vs-usable-token]] (+confirmation empirique sur les icônes Miro), [[mcp-on-demand-vs-rules-always-on]] (+instruction de routage toujours-on minimal), [[sil-bormuller]] (+second article), [[into-design-systems-conference]] (+Miro session), [[overview]]
Note : Source de production unique dans son registre — récit d'une petite équipe (6 personnes) sur un an, avec résultats mesurés (–70-80 % Slack, 17 PRs/h, 33K→410 tokens). Introduit la reformulation "IA comme nouvelle recrue" distincte de "IA comme utilisateur", la stratégie skills-avant-mcp, et les métriques d'adoption par l'absence de questions.

## [2026-06-19] query | Audit AI readiness — ouds-documentation
Pages touchées : [[2026-06-19_audit-ai-readiness-ouds-documentation]], [[lisibilite-machine-design-system]], [[trois-couches-composants-agents]], [[schema-metadata-composant]], [[protocole-arc]], [[modele-maturite-ia-design-system]], [[intent-token]], [[ia-comme-utilisateur]], [[processus-generation-metadata-echelle]]
Note : Premier audit structuré du repo ouds-documentation — révèle un paradoxe : c'est le repo le plus stratégique pour l'IA (source de vérité multi-plateforme) et le moins préparé pour une consommation agentique. Niveau 0-1 sur l'axe infrastructure agentique. Recommandations : AGENTS.md, intent encoding des tokens, métadonnées composants, index relationnel.

## [2026-06-24] query | Discours pour convaincre un directeur outillage AI de co-financer OUDS AI-readable

Pages lues : [[inversion-economique-code-comprehension]], [[design-system-as-infrastructure]], [[gouvernance-design-system-ia]], [[metriques-adoption-ia-design-system]], [[lisibilite-machine-design-system]], [[generation-spec-agentique]], [[protocole-pas-produit]], [[mcp-on-demand-vs-rules-always-on]], [[jan-six]], [[diana-wolosin]]
Archive : [[2026-06-24_discours-directeur-outillage-ai]]
Note : Synthèse argumentaire en deux volets — (1) pitch co-financement structuré en 5 temps, (2) réponse à l'objection "pourquoi OUDS spécifiquement". Cadrage central : OUDS comme infrastructure de contexte pour les outils AI existants, pas comme projet design system. Argumentaire d'accélération de ROI plutôt que de rattrapage de dette.

---

## [2026-06-24] ingest | Agentic Design Systems: The Complete Guide — Into Design Systems (via veille web)

Thème de veille : agentic design system
Pages créées : [[into-design-systems-agentic-guide]] (source)
Pages mises à jour : [[jan-six]] (+quote "invisible part", +sous-agents accessibility reviewer), [[diana-wolosin]] (+formule "JSON as contract"), [[design-system-as-infrastructure]] (+section "Contexte > Probabilité", formulation "AI collapses toward average of internet")
Note : Source de synthèse conférence — la majorité des concepts est déjà couverte dans le vault. Apport net limité mais réel : trois formulations nouvelles de haute densité (Jan Six sur l'invisibilité, Wolosin sur le JSON comme contrat, "contexte > probabilité"), le détail sous-agents GitHub Primer, et les stats macro 2026 (28 modèles, $200B+, MCP 100K→8M). Document utile comme point d'entrée de référence sur l'écosystème.

---

## [2026-06-24] ingest | How Uber Built an Agentic System to Automate Design Specs in Minutes (via veille web)

Thème de veille : agentic design system
Pages créées : [[uber-uspec-agentic-design-specs]] (source), [[generation-spec-agentique]], [[ian-guisard]]
Pages mises à jour : [[pipeline-figma-docs-automatise]] (+variante uSpec : génération de spec formelle vs documentation narrative), [[accessibilite-continue]] (+cas Uber génération multi-plateforme screen reader), [[processus-generation-metadata-echelle]] (lien indirect via source)
Note : Source de terrain exemplaire — démontre à grande échelle (centaines de composants, 7 stacks) que la génération de spec peut être entièrement agentique. Le cas screen reader est le plus saillant : 3 plateformes (VoiceOver, TalkBack, ARIA) en 2 minutes vs des heures manuelles. Architecture clé : séparation entre couche déterministe (MCP Figma Console, open-source Southleft) et couche interprétative (agent skills par section de spec). Nouveau concept [[generation-spec-agentique]] créé — distinct de [[pipeline-figma-docs-automatise]] (specs formelles pour ingénieurs vs documentation narrative pour équipes). Tension ouverte : qui audite les specs générées par l'agent ?

---

## [2026-06-24] ingest | Design System Documentation Spec (DSDS) 0.12.0 — designsystemdocspec.org
Pages créées : [[design-system-documentation-spec]] (source), [[dsds-format]], [[pj-onori]]
Pages mises à jour : [[lisibilite-machine-design-system]] (+DSDS comme standard ouvert, agentDocumentBlocks, criteria), [[schema-metadata-composant]] (+source), [[dtcg-annotation-schema]] (+DSDS comme couche complémentaire DTCG, duo quoi/comment-pourquoi), [[ia-comme-utilisateur]] (+agentDocumentBlocks comme mécanisme formel de la double audience), [[systeme-de-design-agentique]] (+DSDS comme format de référence standardisé)
Note : Première spec ouverte qui formalise le design system agentique dans un format JSON validable. DSDS est à la documentation de design system ce que le DTCG est aux tokens. Nouvelles contributions au corpus : mécanisme agentDocumentBlocks formalisé dans une spec, système de criteria (automated/assisted/manual) avec fixtures pass/fail, portabilité comme principe fondateur contre le vendor lock-in de documentation.

---

## [2026-06-26] query | Workflow idéal documentation DS boostée IA, de la conception au handoff

Pages créées : [[2026-06-26_workflow-documentation-ds-conception-handoff]]
[GAP] Aucune source ne documente un workflow bout-en-bout connectant les trois phases (spec formelle + métadonnées machines + docs narratives). Les sources couvrent chaque phase séparément.

---

## [2026-06-26] ingest | Atlassian's DESIGN.md is here: what we learned testing portable design context (via veille web)

Thème de veille : DESIGN.md vs DSDS
Pages créées : [[atlassian-design-md-lessons]] (source)
Pages mises à jour : [[design-md-format]] (+section preuve empirique Atlassian, distinction reimplementing/using, customer theming), [[mcp-on-demand-vs-rules-always-on]] (+section validation empirique DESIGN.md comme cas limite du all-at-once), [[metriques-adoption-ia-design-system]] (+benchmark comparatif Atlassian)
Note : Source de terrain exceptionnelle — premier benchmark contrôlé publié DESIGN.md vs MCP sur tâche de production. Apport conceptuel principal : distinction *spec for reimplementing* (DESIGN.md) vs *guide for using* (MCP) — reformule la limite du format de façon précise et non présente dans le wiki. Découverte additionnelle : no-context est plus économique que DESIGN.md sur une codebase production (saturation de contexte). Nouveau pattern agentique identifié : customer theming for adaptive UIs.

---

## [2026-06-26] ingest | DESIGN.md — Format Specification (Google Labs) (via veille web)

Thème de veille : agentic design system
Pages créées : [[google-design-md-spec]] (source), [[design-md-format]]
Pages mises à jour : [[lisibilite-machine-design-system]] (+section DESIGN.md comme lisibilité de l'identité visuelle), [[dsds-format]] (+tension DSDS vs DESIGN.md, pont d'export dtcg), [[intent-token]] (+DESIGN.md comme encodage d'intent top-down à l'échelle projet)
Note : Source de référence primaire — spec officielle open source (Apache 2.0, 15 800 étoiles en 3 mois). Apport conceptuel central : distingue la lisibilité des valeurs (DTCG) de la lisibilité de l'intent de marque (DESIGN.md) — le *pourquoi* au niveau du projet entier, pas token par token. La CLI avec vérification WCAG AA automatique et export DTCG ouvre un pont vers l'écosystème existant. Tension ouverte avec DSDS : deux formats complémentaires mais de philosophies opposées (top-down identité vs bottom-up composants), concurrents sur l'adoption initiale.

---

## [2026-06-29] ingest | Introducing Astryx by Meta (via veille web)

Thème de veille : design system AI readiness
Pages créées : [[meta-astryx-design-system]] (source)
Pages mises à jour : [[systeme-de-design-agentique]] (+section Astryx comme premier DS ground-up AI-operable, +JSON manifest, +CLI+MCP), [[lisibilite-machine-design-system]] (source ajoutée)
Note : Source de rupture — premier DS majeur (MIT, 13k apps Meta) conçu ground-up pour les agents plutôt que retrofitté. Apport conceptuel central : "AI-operable by design" comme paradigme distinct de "machine-readable by documentation". Le JSON manifest (OpenAPI du CLI) est l'implémentation la plus concrète du principe "donner à l'agent une spec formelle de ce qu'il peut faire".

---

## [2026-06-29] ingest | Agentic design system guide (TDP / Dianne Alter) (via veille web)

Thème de veille : design system AI readiness
Pages créées : [[tdp-agentic-design-system-guide]] (source)
Pages mises à jour : [[schema-metadata-composant]] (+section 6-fichiers TDP, +anti-patterns spécifiques vs génériques), [[priori-conflictuels-nommage]] (+section nommage Figma intent vs position : emphasis/default/subtle)
Note : Guide de terrain avec implémentation concrète (6 fichiers par composant, résultat client mesuré). Apport net : anti-patterns spécifiques au produit comme distinction entre sortie "proche" et sortie "correcte". Distinction emphasis/default/subtle vs primary/secondary/tertiary applique les priors conflictuels à la couche Figma — angle non couvert par Kavcic.

---

## [2026-06-29] ingest | Design Systems Report 2026 — zeroheight (via veille web)

Thème de veille : design system AI readiness
Pages créées : [[zeroheight-design-systems-report-2026]] (source)
Pages mises à jour : [[metriques-adoption-ia-design-system]] (+section données macro sectorielles, +gap 56%/15%), [[systeme-de-design-agentique]] (+section gap adoption/satisfaction comme mesure d'AI readiness)
Note : Source macro la plus importante de la veille. Le gap 56%/15% est la première mesure sectorielle à large échelle de l'échec d'AI readiness — il valide empiriquement le corpus du vault à l'échelle de l'industrie. La chute du buy-in DS (42%→32%) introduit une tension de gouvernance non documentée jusque-là.

---

## [2026-06-29] ingest | Your Figma library is invisible to AI agents (Nurkhon)

Pages créées : [[figma-library-invisible-ai-agents]] (source)
Pages mises à jour : [[lisibilite-machine-design-system]] (+section "illegible ≠ incorrect", +23% stat, +43% semantic naming, +contrat implicite), [[ia-comme-utilisateur]] (+section "nouveau lecteur dans la pièce", +audience shift Figma MCP, +contrat implicite, +bypass pattern), [[priori-conflictuels-nommage]] (+section judgment gap : intentionnel vs accidentel), [[inversion-economique-code-comprehension]] (+section shift de compétence : craft visuel vs architecture structurelle)
Note : Source de témoignage de terrain (avril 2026) — l'auteur décrit en première personne la découverte du problème via Claude Code + Figma MCP. Apport conceptuel central : la nuance "illegible ≠ incorrect" qui manquait au corpus — un system bien construit peut être structurellement invisible. Trois contributions nettes : (1) formulation "AI agents parse, not infer" — le registre le plus précis sur le mécanisme de l'invisibilité ; (2) le contrat implicite comme racine du problème — les noms compriment une histoire inaccessible aux agents ; (3) le skill shift entre craft visuel et architecture structurelle — conséquence opérationnelle de l'inversion économique non encore formulée. Données empiriques utiles : 23% (UX Collective), 43% (Figma research), cas Spotify Encore/Cursor confirmé depuis un angle indépendant.

---

## [2026-06-29] ingest | OUDS Button — Specs Figma (Actions---Button, node 2071:11587)

Source : Figma MCP — fichier bmVSCYZgRmXwdqtpvT4flo, composant Button de [OUDS Lib] Components library, mis à jour 2026-06-26.
Pages créées : [[figma-ouds-button-specs]] (source), [[2026-06-29_figma-ouds-button-specs]] (raw)
Pages mises à jour : [[schema-metadata-composant]] (+section implémentation partielle OUDS Button, anti-pattern formulé avec alternative), [[generation-spec-agentique]] (+section frame OUDS comme output cible, contrainte de taille 2,3M chars), [[lisibilite-machine-design-system]] (+section deux niveaux de lisibilité — intent lisible, implémentation non), [[pipeline-figma-docs-automatise]] (+section limite concrète : frames de documentation oversized), [[composants-context-aware]] (+section séparation taxonomique Button vs Navigation button), [[ia-comme-utilisateur]] (+section champ Keywords OUDS comme signal d'audience explicite)
Note : Source primaire directe extraite via Figma MCP (search_design_system + get_libraries + get_screenshot). Apport principal : premier cas réel OUDS dans le corpus — illustre concrètement la thèse "lisibilité à deux vitesses" (intent machine-readable dans le champ description, specs visuelles dans un frame de 2,3M chars inaccessible sans sélection Desktop). Le champ "Key words" OUDS est l'exemple le plus direct observé d'une équipe adressant explicitement une audience IA dans sa documentation Figma. Limite documentée : get_design_context et get_variable_defs nécessitent une sélection active dans Figma Desktop — les données structurelles fines (tokens, dimensions, états) restent hors de portée du MCP sans cette sélection.

## [2026-06-30] ingest | What Is an AI-Ready Design System? (Olha Bondar)

Pages créées : [[ai-ready-design-system-olha-bondar]] (source), [[grammaire-composition-composants]], [[contraintes-fixed-preferred-exploratory]]
Pages mises à jour : [[schema-metadata-composant]] (+section contrat Bondar useWhen/doNotUseWhen/accessibility, +lien grammaire-composition-composants), [[modele-maturite-ia-design-system]] (+section troisième axe maturité Bondar niveaux 0-4, +tension mise à jour sur trois modèles orthogonaux), [[lisibilite-machine-design-system]] (+section contenu structuré comme dimension oubliée, +section validation exécutable comme boucle de feedback), [[architecture-contexte-agentique]] (+section context architecture vs context volume)
Note : Article de praticien récent (22 juin 2026) — apport incrémental mais ciblé sur deux concepts absents du wiki : la grammaire de composition (règles parent/enfant, ownership espacement, combinaisons interdites) et la tripartition fixed/preferred/exploratory pour calibrer l'autonomie des agents. Formule marquante : "If a system is clear, AI can scale the system. If a system is ambiguous, AI can scale the ambiguity." Pas de données empiriques propres, mais convergence forte avec le corpus existant sur les tokens, MCP, et contrats de composant.

---

## [2026-06-30] ingest | Key topics from Apple's WWDC 2026 (Levin & Riegner, Ivan Leider) (via veille web)

Thème de veille : Apple agentic interface WWDC 2026
Pages créées : [[wwdc-2026-apple-ai-native-os-levinriegner]] (source), [[invisibilite-produit-os-agentique]]
Pages mises à jour : [[ia-comme-utilisateur]] (+section OS comme troisième audience, trois niveaux d'audience agentique), [[protocole-pas-produit]] (+section App Intents comme implémentation Apple du principe, +tension MCP/App Intents mise à jour), [[niveaux-confiance-actions-agentiques]] (+section posture Apple "agentic with human in the loop"), [[gouvernance-design-system-ia]] (+section gouvernance par mandat plateforme / Liquid Glass forcé), [[index.md]]
Note : Source stratégique (agence produit L+R, 8 juin 2026). Apport principal : le concept d'invisibilité produit par non-exposition des App Intents — "technically installed and practically invisible" — qui prolonge et distingue l'invisibilité Figma ([[figma-library-invisible-ai-agents]]) à un niveau OS. Confirme MCP natif dans Xcode. Documente la posture Apple "agentic with human in the loop" comme choix délibéré de plateforme. Introduit la Liquid Glass migration forcée comme cas de gouvernance par mandat plateforme.

---
---

## [2026-07-03] ingest | Agentic Design System — From Chatbot to Orchestration (Kavcic, mai 2026)

Thème de veille : agentic design system
Pages créées : [[agentic-ds-from-chatbot-to-orchestration]] (source), [[composant-comme-contrat]], [[orchestration-multi-agents]]
Pages mises à jour : [[systeme-de-design-agentique]] (+section composant→contrat, +section orchestration multi-agents), [[gouvernance-design-system-ia]] (+section quatre risques de l'autonomie agentique), [[intent-token]] (+section métadonnées enrichies useFor/avoidFor/accessibility), [[romina-kavcic]] (+article mai 2026)
Note : Article charnière qui reformule le paradigme sur deux axes : (1) le composant devient contrat — pas une apparence mais un ensemble de règles, d'intent et de contraintes que l'agent peut traverser ; (2) la configuration agentique cible est une orchestration multi-agents (4 spécialistes + orchestrateur) sous principe de "governed autonomy". Contribution la plus originale au corpus existant : l'inventaire des quatre risques spécifiques à l'autonomie agentique (design debt machine-speed, fausse confiance doc générée, manipulation UX runtime, governance gaps) — un registre absent des sources antérieures.
