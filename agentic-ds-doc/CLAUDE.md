# CLAUDE.md — Schéma du Wiki LLM

> Ce fichier est ton contrat de travail. Lis-le intégralement avant toute opération sur ce vault.
> Il définit la structure, les conventions, et les quatre opérations que tu exécutes : **Ingest**, **Query**, **Lint**, **Évolutions**.

---

## Philosophie

Ce vault n'est pas un système RAG. Tu ne récupères pas des fragments bruts à la volée.
Tu **construis et maintiens** une base de connaissances persistante et auto-référencée.

**Règle d'or** : chaque source ingérée doit toucher 10 à 15 pages wiki. Une source isolée sans liens croisés est une ingestion bâclée.

**Division du travail** :
- L'humain : choisit les sources, pose les questions, décide ce qui compte.
- Toi : tu écris le wiki, tu maintiens les liens, tu signales les contradictions, tu archives la synthèse.
- L'humain lit. Toi tu écris.

---

## Structure du vault

```
vault/
├── CLAUDE.md          ← ce fichier (schéma + instructions)
├── raw/               ← sources brutes, immuables — jamais modifiées
│   └── AAAA-MM-JJ_<slug>.md
├── wiki/              ← wiki généré et maintenu par Claude
│   ├── index.md       ← table des matières thématique avec liens
│   ├── overview.md    ← synthèse générale du domaine (2-4 pages)
│   ├── log.md         ← journal chronologique append-only
│   ├── concepts/      ← idées, théories, cadres abstraits
│   ├── entities/      ← personnes, organisations, outils, œuvres
│   ├── syntheses/     ← analyses transversales, tensions, états de l'art
│   ├── comparisons/   ← tableaux comparatifs, face-à-face
│   ├── questions/     ← réponses à des questions spécifiques, archivées
│   └── sources/       ← une fiche par source ingérée
└── _meta/             ← fichiers de configuration Obsidian (ne pas modifier)
```

---

## Conventions de nommage

- Fichiers : `kebab-case.md` (minuscules, tirets)
- Titres de pages : `# Titre en prose naturelle`
- Dates : `AAAA-MM-JJ` en préfixe pour les fichiers `raw/` et les entrées `log.md`
- Liens internes : liens markdown standards avec chemin relatif, `[Texte affiché](chemin/relatif/vers/fichier.md)`.
  Pas de wikilinks `[[...]]` : ce format n'est pas rendu par GitHub, qui doit pouvoir afficher le vault tel quel.
  Le chemin est relatif au fichier courant (ex. depuis `wiki/concepts/x.md` vers `wiki/entities/y.md` : `[y](../entities/y.md)`).
  Obsidian affiche et suit très bien ce format (réglable dans Paramètres → Fichiers et liens → Format des liens internes,
  mais fonctionne aussi tel quel) : le graph view et les backlinks restent intacts.

---

## Frontmatter obligatoire pour toute page wiki

```yaml
---
type: concept | entity | synthesis | comparison | question | source | index
tags: [tag1, tag2]
created: AAAA-MM-JJ
updated: AAAA-MM-JJ
sources:
  - "[source-slug-1](../sources/source-slug-1.md)"
  - "[source-slug-2](../sources/source-slug-2.md)"
related:
  - "[concept-lié](concept-lie.md)"
  - "[entité-liée](../entities/entite-liee.md)"
---
```
(adapter les chemins relatifs à l'emplacement réel du fichier courant)

---

## Opération 1 : INGEST

**Déclencheur** : l'humain dit `ingest` ou `ingère` suivi d'un contenu (texte, URL, PDF, notes).

**Séquence obligatoire** :

1. Crée `raw/AAAA-MM-JJ_<slug>.md` avec le contenu brut tel quel, sans modification.
2. Crée ou mets à jour `wiki/sources/<slug>.md` : résumé structuré, thèses principales, citations clés (≤ 15 mots chacune), connexions identifiées.
3. Pour chaque concept, entité, argument significatif : crée ou mets à jour la page correspondante dans `wiki/concepts/` ou `wiki/entities/`. **Ne crée pas une nouvelle page si une page existante peut être enrichie.**
4. Mets à jour `wiki/overview.md` si la source modifie l'image globale du domaine.
5. Si la source contredit une page existante : ajoute une section `## ⚡ Tension / Contradiction` dans la page concernée, en citant les deux positions avec leurs sources.
6. Ajoute une entrée dans `wiki/log.md` :
   ```
   ## [AAAA-MM-JJ] ingest | <titre de la source>
   Pages touchées : [page1](chemin/page1.md), [page2](chemin/page2.md), [page3](chemin/page3.md)...
   Note : <une phrase sur ce que cette source apporte ou change>
   ```
7. Mets à jour `wiki/index.md` si une nouvelle catégorie thématique émerge.

**Rapport de fin d'ingest** (afficher dans le chat) :
```
INGEST COMPLET : <titre>
Pages créées    : N
Pages mises à jour : N
Contradictions  : N (lister si > 0)
Pages orphelines potentielles : lister
```

---

## Opération 2 : QUERY

**Déclencheur** : l'humain pose une question, demande une synthèse, ou dit `query`.

**Séquence** :

1. Lis les pages wiki pertinentes (pas les sources brutes).
2. Réponds en t'appuyant exclusivement sur le contenu du wiki, avec des liens `[page](chemin/page.md)`.
3. Si la réponse est substantielle (> 300 mots) et susceptible d'être utile plus tard : crée `wiki/questions/AAAA-MM-JJ_<slug>.md` et archive la réponse.
4. Si la synthèse révèle une lacune : note-la dans `wiki/log.md` sous `[GAP]`.
5. Si la réponse nécessite une comparaison : crée `wiki/comparisons/<slug>.md`.

**Format de réponse préféré pour les questions complexes** : prose continue avec liens internes, pas de listes à puces sauf pour des énumérations vraiment atomiques.

---

## Opération 3 : LINT

**Déclencheur** : l'humain dit `lint` ou `audit`.

**Séquence** :

1. Scan des pages orphelines (aucun lien entrant).
2. Détection des contradictions non résolues (deux pages affirmant des choses incompatibles).
3. Pages sans frontmatter complet.
4. Concepts mentionnés dans plusieurs pages mais sans page propre.
5. Sources dans `raw/` sans fiche dans `wiki/sources/`.
6. Pages trop courtes (< 3 phrases) ou trop longues sans structure interne.

**Rapport de lint** (format obligatoire) :
```
LINT REPORT : AAAA-MM-JJ
─────────────────────────
Pages orphelines    : N → [liste]
Contradictions      : N → [liste]
Frontmatter manquant: N → [liste]
Concepts sans page  : [liste]
Sources non traitées: N → [liste]
Recommandations     : [actions prioritaires]
```

---

## Opération 4 : ÉVOLUTIONS

**Déclencheur** : l'humain dit `évolutions`, `changelog`, `quoi de neuf`, `bilan du jour`, `bilan de la semaine`, `bilan du mois`, ou précise une période (`aujourd'hui`, `cette semaine`, `ce mois`).

**Fenêtre temporelle** :
- `aujourd'hui` ou absence de précision → jour courant (date du jour)
- `cette semaine` ou `semaine` → 7 derniers jours
- `ce mois` ou `mois` → 30 derniers jours

**Séquence** :

1. Lis `wiki/log.md` et filtre les entrées dont la date tombe dans la fenêtre temporelle demandée.
2. Pour chaque entrée du log dans la fenêtre : lis les pages wiki mentionnées dans `Pages touchées` afin d'en comprendre le contenu actuel.
3. Identifie les patterns transversaux : quels thèmes ont le plus bougé, quelles tensions sont apparues, quels concepts ont été enrichis ou créés.
4. Rédige la synthèse en prose continue, structurée en quatre parties :
   - **Ce qui a été ingéré** : sources ajoutées, avec leur apport principal en une phrase chacune.
   - **Ce qui a évolué** : pages mises à jour et nature du changement (enrichissement, contradiction, extension).
   - **Ce qui émerge** : tendances, tensions nouvelles, lacunes révélées par l'activité de la période.
   - **Recommandations** : 2 à 4 actions concrètes suggérées pour la prochaine session — ingestions à prioriser, pages à consolider, lacunes à combler, tensions à résoudre. Formuler chaque recommandation en une phrase directe et actionnelle.
5. Écris le bilan dans `Journal/AAAA-MM-JJ_evolutions-<periode>.md` (ex. `Journal/2026-07-07_evolutions-jour.md`). Affiche aussi la synthèse dans le chat.
6. Si la période ne contient aucune activité dans `log.md`, le dire explicitement sans inventer. Ne crée pas de fichier dans ce cas.

**Format de réponse** (chat + fichier) :
```
ÉVOLUTIONS — <période> (AAAA-MM-JJ → AAAA-MM-JJ)
──────────────────────────────────────────────────
Sources ingérées : N
Pages créées     : N
Pages mises à jour : N

[prose continue en quatre parties, dont Recommandations en dernière]
```

---

## Conventions stylistiques pour les pages wiki

- **Prose continue** de préférence aux listes à puces, sauf pour des éléments vraiment atomiques.
- **Pas de headers H1** dans les pages wiki (le titre est dans le frontmatter). Commence à H2.
- **Densité d'information** : chaque phrase doit apporter quelque chose. Pas de remplissage.
- **Liens systématiques** : tout nom propre, concept ou œuvre déjà présent dans le vault doit être un lien markdown `[texte](chemin/relatif.md)`.
- **Tensions visibles** : ne pas lisser les contradictions. Les rendre apparentes avec `## ⚡ Tension`.
- **Attribution** : toute affirmation non synthétique doit citer sa source entre parenthèses : `([source-slug](chemin/relatif/vers/sources/source-slug.md))`.
- **Jamais de tiret cadratin** (—). Utiliser une virgule, un point, ou reformuler la phrase.

---

## Ce que tu ne fais PAS

- Tu ne modifies jamais les fichiers dans `raw/`.
- Tu ne supprimes jamais une page wiki — tu la marques `#obsolète` et notes la raison.
- Tu n'inventes pas de faits. Si l'information est absente du wiki, tu le dis explicitement.
- Tu n'utilises pas de listes à puces pour les réponses narratives ou analytiques.
- Tu ne reformules pas les citations de sources au-delà de 15 mots.

---

## Paramètres du vault

```yaml
domaine: [à définir par l'humain à l'initialisation]
langue: français
profondeur: recherche personnelle
horizon: long terme (base de connaissance cumulante)
style_prose: continu, analytique, sans bullets
```

---

*Ce fichier est la constitution du vault. Toute modification doit être explicite et consignée dans log.md.*
