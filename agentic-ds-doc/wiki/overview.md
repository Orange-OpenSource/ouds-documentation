---
type: overview
updated: 2026-07-06
---

# Vue d'ensemble

> Page de synthèse générale du domaine couvert par ce vault.
> Mise à jour par Claude à chaque ingest qui modifie l'image globale.

---

## État du domaine

Ce vault porte sur l'intersection entre les **design systems** et l'**intelligence artificielle agentique** — plus précisément, sur ce que les équipes design et dev doivent faire aujourd'hui pour que leurs systèmes de design restent cohérents et utilisables dans un monde où du code est généré automatiquement à grande échelle.

L'argument de fond est que l'IA ne rend pas les design systems obsolètes — elle les rend plus critiques. Le code devient gratuit. La compréhension (conventions de nommage, intent des tokens, règles de composition, contextes d'usage) devient l'actif rare. Et le design system est précisément le lieu où cette compréhension est encodée et transmise ([[design-system-most-important-asset-ai-era]]).

Cette thèse est maintenant validée empiriquement : avec une infrastructure machine-readable, un agent est 2x plus rapide, 54 % plus précis, zéro faux négatif, avec 0,04 % de variance contre 26,5 % sans infrastructure ([[towards-agentic-design-system]]). Le chantier qui reste ouvert est la progression du stade Consommateur vers le stade Mainteneur puis Auto-gouverné — le [[protocole-arc]].

Le domaine est en pleine accélération : 28+ modèles frontière publiés en moins de 10 mois, 41 % du code produit en 2025 généré par IA, 8 millions de téléchargements MCP. La vitesse de l'outillage devance la maturité des pratiques — c'est la tension principale.

---

## Tensions principales

**Adoption massive, résultats polarisés** : 82 % des équipes DS utilisent désormais l'IA ([[state-of-ai-design-systems-2026-zeroheight]]). La documentation est le cas d'usage gagnant (63 % satisfaits, +44 points nets). La génération de design est le cas perdant (67 % insatisfaits, -53 points nets). Cette polarisation n'est pas aléatoire — elle reflète la différence entre transformer un existant structuré (documentation) et créer depuis des contraintes implicites (design). L'écart est directement corrélé au niveau d'AI-readiness du DS sous-jacent.

**Vitesse vs fondations** : les équipes veulent déployer des agents IA immédiatement (acheter les arbres), mais sans les fondations structurelles adéquates (semences), l'IA amplifie le bruit plutôt que la compréhension. Voir [[seeds-vs-trees]].

**Documentation humaine vs lisibilité machine** : les design systems sont documentés pour les humains depuis des décennies — guidelines en prose, règles implicites, expertise tacite. Les rendre lisibles par des machines requiert un changement de paradigme, pas seulement un effort de documentation supplémentaire. Seulement 17 % des équipes estiment leur documentation "très prête pour l'IA" ([[state-of-ai-design-systems-2026-zeroheight]]). Voir [[lisibilite-machine-design-system]].

**Readable vs usable** : nouvelle tension affinée par l'audit de 50 fichiers de tokens ([[50-design-token-files-one-problem]]). Être machine-readable (le build pipeline compile) est distinct d'être agent-usable (l'agent peut raisonner sur le bon token). Sur 50 systèmes publics : ~15 ont une description dans le fichier, 1 seul a une règle de non-usage. La majorité des design systems a résolu le premier problème sans même avoir commencé le second. Voir [[readable-vs-usable-token]].

**Shadow AI** : 50 % des équipes DS signalent que l'usage IA par d'autres équipes leur crée des problèmes — UI générée qui contourne le DS, prototypes vibe-codés qui verrouillent les attentes des stakeholders, accessibilité silencieusement supprimée. La réponse dominante est la tolérance, pas la politique. La vraie solution est économique : rendre le chemin vers le DS plus court que le contournement. Voir [[shadow-ia-design-system]].

**Readiness technique vs readiness organisationnelle** : la communauté design system a produit une réponse claire à la question "comment rendre notre système lisible par les machines" (tokens DTCG, documentation d'intent, Code Connect, MCP). La question suivante — "sommes-nous prêts à ce que ça fonctionne ?" — reste largement sans réponse. Quand 55 % des product builders prennent des tâches hors de leur périmètre habituel (Figma research), le workflow linéaire "collapse" et crée une crise de gouvernance organisationnelle : qui décide si l'output IA est assez bon pour shipper, qui répond quand des composants accessibles produisent un parcours inaccessible, comment les modèles de contribution gèrent des proposants non-humains. Ces questions ne se résolvent pas avec de la meilleure architecture de tokens. Voir [[gouvernance-design-system-ia]] et [[accountability-gap-ia]].

**Architecture vs contenu** : avoir la bonne infrastructure MCP/JSON ne suffit pas si le contenu est lacunaire. Miro a démontré qu'Aura était "confidently wrong" malgré une architecture fonctionnelle — la cause était l'absence de champs "do not use" dans les métadonnées d'icônes et de tokens, pas un problème de format. La distinction [[ia-comme-nouvelle-recrue]] vs [[ia-comme-utilisateur]] formalise cette tension.

**Définitions monolithiques vs context bubbles** : les composants définis dans un seul bloc (props + variants + styles + comportements + accessibilité + guidelines) imposent une fenêtre de contexte massive aux agents. L'AI Design Systems Conference 2026 documente que Spotify Encore a résolu ce problème en décomposant les composants en trois couches architecturales indépendantes (Foundation, Style, Behavior) — des "context bubbles" que l'agent peut raisonner séparément. Voir [[trois-couches-composants-agents]].

---

## Questions ouvertes

— La Phase 3 du [[protocole-arc]] (Compose / Auto-gouverné) a son cadre conceptuel établi (juillet 2026 : [[langage-design-system]] = vocabulaire + grammaire + contrats). La prochaine question : qui a une implémentation en production qui va au-delà de la Phase 2 (audit/report) ? La [[boucle-feedback-infrastructure]] de Kavcic (Watch/Analyze/Execute) est la candidate la plus avancée.
— Comment les deux approches (Kavcic : MCP + context layers ; Morales : metadata files + TOON index) s'intègrent-elles concrètement dans un seul workflow d'équipe ?
— La partie 3 de la série Kavcic ("The Self-Healing Design System") est annoncée et disponible dans raw/ — à ingérer.

---

## Carte conceptuelle

Les concepts centraux du domaine s'articulent ainsi :

[[inversion-economique-code-comprehension]] → fonde la nécessité de [[design-system-as-infrastructure]]
[[design-system-as-infrastructure]] → requiert [[lisibilite-machine-design-system]]
[[lisibilite-machine-design-system]] → s'opérationnalise via [[trois-couches-composants-agents]]
[[trois-couches-composants-agents]] + [[knowledge-graph-design-system]] → permettent [[systeme-de-design-agentique]]
[[systeme-de-design-agentique]] → consomme [[mcp-model-context-protocol]] et [[cli-vs-mcp]]
[[composants-context-aware]] + [[intent-token]] → sont les manifestations concrètes de la lisibilité machine
[[intent-token]] → requiert [[readable-vs-usable-token]] au niveau fichier → s'implémente via [[dtcg-annotation-schema]]
[[dtcg-annotation-schema]] (quoi/valeurs) + [[dsds-format]] (comment/pourquoi) → duo de standards complémentaires pour le design system agent-usable
[[delegation-lens]] → cadre pour évaluer la taille d'une échelle de tokens et sa surface d'erreur
[[priori-conflictuels-nommage]] → explication du comportement de génération de noms d'agents sans grammaire déclarée
[[pipeline-intent-context-systeme]] → est le flux d'exécution de l'agent sur le système
[[seeds-vs-trees]] → est la posture stratégique pour l'adoption

---

*Dernière mise à jour substantielle : 2026-07-09 — ingestion série Achiardi juillet 2026 — création de [[langage-design-system]] (vocabulaire + grammaire + contrats comme fondation de la Phase 3 Compose du [[protocole-arc]]) ; ingestion ARC Protocol open-source (arc-protocol.org, protocole RPC inter-agents distinct du protocole ARC d'Achiardi — disambiguation ajoutée)*

*Mise à jour précédente : 2026-07-06 — ingestion "Your design system might be AI-ready. Your organisation probably isn't." (Murphy Trueman) — introduction de la tension readiness technique vs readiness organisationnelle ; nouveau concept [[accountability-gap-ia]] ; nouvelle section gouvernance organisationnelle dans [[gouvernance-design-system-ia]]*

*Mise à jour précédente : 2026-07-06 — ingestion "State of AI in Design Systems 2026" (zeroheight, N=123) — première mesure sectorielle de l'adoption IA dans les DS (82 %, MCP 47 %, AI-readiness 17 %) ; introduction du Shadow AI comme concept ; polarisation satisfaction documentation (+44 net) vs design generation (-53 net)*

*Mise à jour précédente : 2026-06-24 — ingestion DSDS 0.12.0 (PJ Onori) — première spec ouverte qui standardise le format machine-readable d'un design system ; formalisation de agentDocumentBlocks, système de criteria vérifiables (automated/assisted/manual), portabilité comme principe fondateur*

*Mise à jour : 2026-06-22 — ingestion Typeform/Coelho (oct. 2025) — ajout notion-cms-design-system et pipeline-multi-destinations, tension contribution vs précision agentique*

*Mise à jour : 2026-06-22 — ingestion Miro playbook (Lombardo/Machado) — nouvelle tension architecture vs contenu, concepts skills-avant-mcp, ia-comme-nouvelle-recrue, metriques-adoption, confirmation empirique do-not-use sur icônes et client-side rendering comme bloqueur*
