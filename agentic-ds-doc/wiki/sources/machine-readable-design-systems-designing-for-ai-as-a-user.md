---
type: source
tags: [design-system, ia, machine-readable, mcp, benchmark, json, metadata, indeed]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[diana-wolosin]]"
  - "[[ia-comme-utilisateur]]"
  - "[[mcp-on-demand-vs-rules-always-on]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[format-toon]]"
  - "[[mcp-model-context-protocol]]"
  - "[[schema-metadata-composant]]"
  - "[[architecture-skills-rules-instructions]]"
  - "[[into-design-systems-conference]]"
---

## Machine-Readable Design Systems: Designing for AI as a User

**Auteure** : [[diana-wolosin]]
**Publication** : Design Systems Collective (Medium), mars 2026
**URL** : https://www.designsystemscollective.com/machine-readable-design-systems-designing-for-ai-as-a-user-28077c9f2144
**Présenté à** : [[into-design-systems-conference]] AI Conference for Designers 2026
**Fichier brut** : `raw/machine-readable-design-systems-designing-for-ai-as-a-user.md`

---

## Résumé structuré

Article et conférence de Diana Wolosin documentant un an de recherche sur les design systems machine-readable, culminant dans un benchmark rigoureux de 8 configurations MCP sur 1 056 prompts à Indeed. La thèse centrale : l'IA est un nouvel utilisateur du design system, qui requiert un format différent de celui conçu pour les humains. Résultat clé : JSON bat Markdown et TOON avec 80 % de tokens en moins et 5× moins cher. Découverte critique : même un MCP parfaitement structuré produit des violations de fondations (typographie, espacement, couleurs) parce que le MCP est on-demand — il ne retourne que ce qu'on lui demande. La solution : une architecture en couches (Rules toujours actives + MCP on-demand + AGENTS.md) que Wolosin appelle "plugin".

---

## Thèses principales

**Thèse 1 — AI is a new user.** Le design system doit être pensé pour deux audiences : les humains qui lisent et interprètent, et les IA qui requêtent et raisonnent programmatiquement. La documentation prose conçue pour les humains introduit de la variabilité quand un LLM doit en extraire des décisions. La lisibilité machine requiert une forme différente : données structurées, métadonnées, schémas, contraintes explicites.

**Thèse 2 — Le format importe plus que le modèle.** Ce qu'on donne au LLM impacte directement la qualité de son raisonnement et de ses sorties. Un spreadsheet JSON copié-collé "almost worked" chez Indeed — assez pour valider l'hypothèse, pas assez pour un usage en production. La question n'est pas quel modèle utiliser, mais quel format lui fournir.

**Thèse 3 — JSON gagne le benchmark.** 8 configurations, 1 056 prompts (22 × 3 × 2 × 8), 5 formats testés (Markdown, plain Markdown, Markdown+JSON hybride, JSON, TOON). JSON : précision équivalente ou supérieure au hybride, 80 % de tokens en moins, $300/an vs $1 500/an pour Markdown. Règle distillée : JSON pour les métadonnées structurées MCP, Markdown pour les règles et instructions en langage naturel.

**Thèse 4 — MCP on-demand vs Rules always-on.** Même parfait, le MCP ne retourne que ce qu'on lui demande. Un prompt "build me a card" retourne les infos sur la Card et le Button — et ignore complètement la typographie, l'espacement, les couleurs. Les fondations cassent non parce qu'elles sont absentes de la base vectorielle, mais parce qu'elles n'ont pas été appelées. Le MCP est on-demand. Les Rules sont always-on. Confondre les deux = violations de fondations systématiques.

**Thèse 5 — Le plugin comme architecture complète.** La réponse au problème des fondations : une architecture en couches combinant Rules (toujours actives, portent les fondations), MCP (on-demand, porte la connaissance composant), et AGENTS.md. Ce que Wolosin appelle un "plugin" — la couche qui transforme un MCP seul en infrastructure fiable.

---

## Données concrètes

Indeed : 77 composants, documentation MDX, 4 parsers JS par domaine (accessibilité, développement, localisation, design), fusion en 1 JSON par composant, Vectra (base vectorielle open source). Pipeline auto-régénérant à chaque mise à jour de doc. Benchmark : Cursor + Claude Sonnet 4.5. Lancement en production : août 2024. 4 300 prototypes en 4 mois (août–décembre). Audit Keith Weston : violations de typographie, espacement cassé, palette de couleurs inventée, emojis au lieu d'icônes.

---

## Citations clés

> "AI is a new user."

> "Codify your design system knowledge into structured data, metadata, schemas, explicit constraints so LLM can parse it, reason about it and use it programmatically."

> "The format matters. The format we feed to LLM impacts its reasoning and its output."

> "A model context protocol is how you give an AI on-demand access to your design system knowledge."

> "The MCP is on demand. It only returns fresh data about what you asked for."

> "Treat MCP as on demand, treat rules as always on, never confuse the two."

> "JSON is like a contract: explicit keys, explicit values, explicit boundaries, no ambiguity."

---

## Connexions identifiées

[[ia-comme-utilisateur]] est la thèse fondatrice. [[mcp-on-demand-vs-rules-always-on]] est la découverte opérationnelle centrale — absente des articles précédents du vault. Enrichit [[lisibilite-machine-design-system]] (benchmark empirique à grande échelle), [[format-toon]] (TOON testé mais battu par JSON), [[schema-metadata-composant]] (implémentation Indeed concrète), [[mcp-model-context-protocol]] (architecture RAG détaillée), [[architecture-skills-rules-instructions]] (plugin = Rules + MCP + AGENTS.md). Crée [[diana-wolosin]] (entity orpheline jusqu'ici).
