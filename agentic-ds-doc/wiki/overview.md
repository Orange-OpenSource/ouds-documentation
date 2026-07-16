---
type: overview
updated: 2026-07-16
---

# Vue d'ensemble

> Page de synthèse générale du domaine couvert par ce vault.
> Mise à jour par Claude à chaque ingest qui modifie l'image globale.

---

## État du domaine

Ce vault porte sur l'intersection entre les **design systems** et l'**intelligence artificielle agentique** — plus précisément, sur ce que les équipes design et dev doivent faire aujourd'hui pour que leurs systèmes de design restent cohérents et utilisables dans un monde où du code est généré automatiquement à grande échelle.

L'argument de fond est que l'IA ne rend pas les design systems obsolètes — elle les rend plus critiques. Le code devient gratuit. La compréhension (conventions de nommage, intent des tokens, règles de composition, contextes d'usage) devient l'actif rare. Et le design system est précisément le lieu où cette compréhension est encodée et transmise ([design-system-most-important-asset-ai-era](sources/design-system-most-important-asset-ai-era.md)).

Cette thèse est maintenant validée empiriquement : avec une infrastructure machine-readable, un agent est 2x plus rapide, 54 % plus précis, zéro faux négatif, avec 0,04 % de variance contre 26,5 % sans infrastructure ([towards-agentic-design-system](sources/towards-agentic-design-system.md)). Le chantier qui reste ouvert est la progression du stade Consommateur vers le stade Mainteneur puis Auto-gouverné — le [protocole-arc](concepts/protocole-arc.md).

Le domaine est en pleine accélération : 28+ modèles frontière publiés en moins de 10 mois, 41 % du code produit en 2025 généré par IA, 8 millions de téléchargements MCP. La vitesse de l'outillage devance la maturité des pratiques — c'est la tension principale.

---

## Tensions principales

**Adoption massive, résultats polarisés** : 82 % des équipes DS utilisent désormais l'IA ([state-of-ai-design-systems-2026-zeroheight](sources/state-of-ai-design-systems-2026-zeroheight.md)). La documentation est le cas d'usage gagnant (63 % satisfaits, +44 points nets). La génération de design est le cas perdant (67 % insatisfaits, -53 points nets). Cette polarisation n'est pas aléatoire — elle reflète la différence entre transformer un existant structuré (documentation) et créer depuis des contraintes implicites (design). L'écart est directement corrélé au niveau d'AI-readiness du DS sous-jacent.

**Vitesse vs fondations** : les équipes veulent déployer des agents IA immédiatement (acheter les arbres), mais sans les fondations structurelles adéquates (semences), l'IA amplifie le bruit plutôt que la compréhension. Voir [seeds-vs-trees](concepts/seeds-vs-trees.md).

**Documentation humaine vs lisibilité machine** : les design systems sont documentés pour les humains depuis des décennies — guidelines en prose, règles implicites, expertise tacite. Les rendre lisibles par des machines requiert un changement de paradigme, pas seulement un effort de documentation supplémentaire. Seulement 17 % des équipes estiment leur documentation "très prête pour l'IA" ([state-of-ai-design-systems-2026-zeroheight](sources/state-of-ai-design-systems-2026-zeroheight.md)). Voir [lisibilite-machine-design-system](concepts/lisibilite-machine-design-system.md).

**Readable vs usable** : nouvelle tension affinée par l'audit de 50 fichiers de tokens ([50-design-token-files-one-problem](sources/50-design-token-files-one-problem.md)). Être machine-readable (le build pipeline compile) est distinct d'être agent-usable (l'agent peut raisonner sur le bon token). Sur 50 systèmes publics : ~15 ont une description dans le fichier, 1 seul a une règle de non-usage. La majorité des design systems a résolu le premier problème sans même avoir commencé le second. Voir [readable-vs-usable-token](concepts/readable-vs-usable-token.md).

**Shadow AI** : 50 % des équipes DS signalent que l'usage IA par d'autres équipes leur crée des problèmes — UI générée qui contourne le DS, prototypes vibe-codés qui verrouillent les attentes des stakeholders, accessibilité silencieusement supprimée. La réponse dominante est la tolérance, pas la politique. La vraie solution est économique : rendre le chemin vers le DS plus court que le contournement. Voir [shadow-ia-design-system](concepts/shadow-ia-design-system.md).

**Readiness technique vs readiness organisationnelle** : la communauté design system a produit une réponse claire à la question "comment rendre notre système lisible par les machines" (tokens DTCG, documentation d'intent, Code Connect, MCP). La question suivante — "sommes-nous prêts à ce que ça fonctionne ?" — reste largement sans réponse. Quand 55 % des product builders prennent des tâches hors de leur périmètre habituel (Figma research), le workflow linéaire "collapse" et crée une crise de gouvernance organisationnelle : qui décide si l'output IA est assez bon pour shipper, qui répond quand des composants accessibles produisent un parcours inaccessible, comment les modèles de contribution gèrent des proposants non-humains. Ces questions ne se résolvent pas avec de la meilleure architecture de tokens. Voir [gouvernance-design-system-ia](concepts/gouvernance-design-system-ia.md) et [accountability-gap-ia](concepts/accountability-gap-ia.md).

**Succès documentés vs échecs documentés** : jusqu'au 2026-07-16, le vault racontait presque exclusivement des succès (Indeed, New York State, GitHub Primer, Spotify Encore, Miro, uSpec/Uber, Storybook MCP) et un [accountability-gap-ia](concepts/accountability-gap-ia.md) resté entièrement théorique, sans incident réel documenté. Le cas Amazon ([amazon-vibe-coding-4-sev1-90-days](sources/amazon-vibe-coding-4-sev1-90-days.md) : quatre Sev-1 en 90 jours, ~6,3M commandes perdues) et le répertoire de 19 incidents de [crackr-vibe-coding-failures-directory](sources/crackr-vibe-coding-failures-directory.md) comblent ce déséquilibre. Le motif qui traverse ces échecs est cohérent avec la thèse déjà présente dans [seeds-vs-trees](concepts/seeds-vs-trees.md) : la vélocité de génération scale plus vite que la vérification et l'accountability, dans les organisations qui n'ont pas construit les fondations avant d'accélérer.

**Lecture vs écriture agentique** : jusqu'en mars 2026, l'intégration MCP entre agents et outils de design était structurellement une lecture — l'agent consulte le contexte Figma pour informer du code écrit ailleurs. Le Figma MCP beta introduit l'écriture directe dans le canvas : l'agent produit l'artefact final, pas une suggestion. Cela déplace la gouvernance en amont : la complétude du design system devient une métrique de sécurité, puisqu'un agent contraint à n'utiliser que ce qui existe dans la librairie improvisera tout ce qui n'y figure pas. Voir [ecriture-agents-canvas-design](concepts/ecriture-agents-canvas-design.md).

**Architecture vs contenu** : avoir la bonne infrastructure MCP/JSON ne suffit pas si le contenu est lacunaire. Miro a démontré qu'Aura était "confidently wrong" malgré une architecture fonctionnelle — la cause était l'absence de champs "do not use" dans les métadonnées d'icônes et de tokens, pas un problème de format. La distinction [ia-comme-nouvelle-recrue](concepts/ia-comme-nouvelle-recrue.md) vs [ia-comme-utilisateur](concepts/ia-comme-utilisateur.md) formalise cette tension.

**Définitions monolithiques vs context bubbles** : les composants définis dans un seul bloc (props + variants + styles + comportements + accessibilité + guidelines) imposent une fenêtre de contexte massive aux agents. L'AI Design Systems Conference 2026 documente que Spotify Encore a résolu ce problème en décomposant les composants en trois couches architecturales indépendantes (Foundation, Style, Behavior) — des "context bubbles" que l'agent peut raisonner séparément. Voir [trois-couches-composants-agents](concepts/trois-couches-composants-agents.md).

---

## Questions ouvertes

— La Phase 3 du [protocole-arc](concepts/protocole-arc.md) (Compose / Auto-gouverné) a son cadre conceptuel établi (juillet 2026 : [langage-design-system](concepts/langage-design-system.md) = vocabulaire + grammaire + contrats). La prochaine question : qui a une implémentation en production qui va au-delà de la Phase 2 (audit/report) ? La [boucle-feedback-infrastructure](concepts/boucle-feedback-infrastructure.md) de Kavcic (Watch/Analyze/Execute) est la candidate la plus avancée. Le cas Storybook MCP (juillet 2026) apporte une première preuve vérifiable, mais à l'échelle d'un seul composant, pas d'un système de production entier : la question reste ouverte au niveau systémique.
— Comment les deux approches (Kavcic : MCP + context layers ; Morales : metadata files + TOON index) s'intègrent-elles concrètement dans un seul workflow d'équipe ?
— La partie 3 de la série Kavcic ("The Self-Healing Design System") est annoncée et disponible dans raw/ — à ingérer.
— Le cas Amazon documente un échec organisationnel à grande échelle mais générique (pas spécifique aux interfaces ou aux design systems). Aucune source du vault ne documente encore un incident de production *spécifiquement* causé par une interface générée depuis un design system agentique (accessibilité composite, incohérence de marque shippée, régression UX) — la défaillance composite que Murphy Trueman décrit reste, elle, sans cas réel documenté.

---

## Carte conceptuelle

Les concepts centraux du domaine s'articulent ainsi :

[inversion-economique-code-comprehension](concepts/inversion-economique-code-comprehension.md) → fonde la nécessité de [design-system-as-infrastructure](concepts/design-system-as-infrastructure.md)
[design-system-as-infrastructure](concepts/design-system-as-infrastructure.md) → requiert [lisibilite-machine-design-system](concepts/lisibilite-machine-design-system.md)
[lisibilite-machine-design-system](concepts/lisibilite-machine-design-system.md) → s'opérationnalise via [trois-couches-composants-agents](concepts/trois-couches-composants-agents.md)
[trois-couches-composants-agents](concepts/trois-couches-composants-agents.md) + [knowledge-graph-design-system](concepts/knowledge-graph-design-system.md) → permettent [systeme-de-design-agentique](concepts/systeme-de-design-agentique.md)
[systeme-de-design-agentique](concepts/systeme-de-design-agentique.md) → consomme [mcp-model-context-protocol](concepts/mcp-model-context-protocol.md) et [cli-vs-mcp](concepts/cli-vs-mcp.md)
[composants-context-aware](concepts/composants-context-aware.md) + [intent-token](concepts/intent-token.md) → sont les manifestations concrètes de la lisibilité machine
[intent-token](concepts/intent-token.md) → requiert [readable-vs-usable-token](concepts/readable-vs-usable-token.md) au niveau fichier → s'implémente via [dtcg-annotation-schema](concepts/dtcg-annotation-schema.md)
[dtcg-annotation-schema](concepts/dtcg-annotation-schema.md) (quoi/valeurs) + [dsds-format](concepts/dsds-format.md) (comment/pourquoi) → duo de standards complémentaires pour le design system agent-usable
[delegation-lens](concepts/delegation-lens.md) → cadre pour évaluer la taille d'une échelle de tokens et sa surface d'erreur
[priori-conflictuels-nommage](concepts/priori-conflictuels-nommage.md) → explication du comportement de génération de noms d'agents sans grammaire déclarée
[pipeline-intent-context-systeme](concepts/pipeline-intent-context-systeme.md) → est le flux d'exécution de l'agent sur le système
[seeds-vs-trees](concepts/seeds-vs-trees.md) → est la posture stratégique pour l'adoption

---

*Dernière mise à jour substantielle : 2026-07-16 — veille "échecs documentés et gouvernance organisationnelle" (5 sources) : le cas Amazon (4 Sev-1 en 90 jours, [amazon-vibe-coding-4-sev1-90-days](sources/amazon-vibe-coding-4-sev1-90-days.md)) est le premier incident réel, nommé et chiffré du vault, comblant le vide théorique d'[accountability-gap-ia](concepts/accountability-gap-ia.md) ; le modèle à trois couches de Lance Dacy ([modele-accountability-trois-couches](concepts/modele-accountability-trois-couches.md)) apporte la réponse structurelle correspondante (reviewer of record) ; la taxonomie de dérive design-system de Superdesign ([derive-design-system-ia](concepts/derive-design-system-ia.md)) nomme quatre modes de défaillance design-system-spécifiques ; le concept de shadow code ([shadow-code](concepts/shadow-code.md)) distingue l'opacité du code généré du contournement déjà documenté (shadow AI) ; le répertoire Crackr confirme que le cas Amazon n'est pas isolé*

*Mise à jour précédente : 2026-07-16 — veille "agentic design system" (4 sources) : "Storybook MCP for AI-aware component libraries" (Akinyemi/LogRocket) apporte la première démonstration vérifiable de l'effet du contrat de composant et une instance entièrement automatisée de la boucle self-healing à l'échelle d'un composant ; "Design Systems Just Became AI Governance Infrastructure" (Victorino) introduit le passage du MCP Figma de la lecture à l'écriture et le nouveau concept [ecriture-agents-canvas-design](concepts/ecriture-agents-canvas-design.md) ; "Design systems and AI: Why MCP servers are the unlock" (Boyer/Figma) est la première source primaire éditeur du vault sur ce sujet et comble l'absence d'entité Figma ; "5 MCP Connections" (Kavcic) structure un inventaire de connecteurs par complexité d'installation*

*Mise à jour précédente : 2026-07-09 — ingestion série Achiardi juillet 2026 — création de [langage-design-system](concepts/langage-design-system.md) (vocabulaire + grammaire + contrats comme fondation de la Phase 3 Compose du [protocole-arc](concepts/protocole-arc.md)) ; ingestion ARC Protocol open-source (arc-protocol.org, protocole RPC inter-agents distinct du protocole ARC d'Achiardi — disambiguation ajoutée)*

*Mise à jour précédente : 2026-07-06 — ingestion "Your design system might be AI-ready. Your organisation probably isn't." (Murphy Trueman) — introduction de la tension readiness technique vs readiness organisationnelle ; nouveau concept [accountability-gap-ia](concepts/accountability-gap-ia.md) ; nouvelle section gouvernance organisationnelle dans [gouvernance-design-system-ia](concepts/gouvernance-design-system-ia.md)*

*Mise à jour précédente : 2026-07-06 — ingestion "State of AI in Design Systems 2026" (zeroheight, N=123) — première mesure sectorielle de l'adoption IA dans les DS (82 %, MCP 47 %, AI-readiness 17 %) ; introduction du Shadow AI comme concept ; polarisation satisfaction documentation (+44 net) vs design generation (-53 net)*

*Mise à jour précédente : 2026-06-24 — ingestion DSDS 0.12.0 (PJ Onori) — première spec ouverte qui standardise le format machine-readable d'un design system ; formalisation de agentDocumentBlocks, système de criteria vérifiables (automated/assisted/manual), portabilité comme principe fondateur*

*Mise à jour : 2026-06-22 — ingestion Typeform/Coelho (oct. 2025) — ajout notion-cms-design-system et pipeline-multi-destinations, tension contribution vs précision agentique*

*Mise à jour : 2026-06-22 — ingestion Miro playbook (Lombardo/Machado) — nouvelle tension architecture vs contenu, concepts skills-avant-mcp, ia-comme-nouvelle-recrue, metriques-adoption, confirmation empirique do-not-use sur icônes et client-side rendering comme bloqueur*
