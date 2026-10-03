---
type: index
tags:
  - guide
  - meta
created: 2026-07-01
updated: 2026-07-01
---

# Guide de prise en main du Wiki LLM

> Ce guide s'adresse à toi, l'humain. Il explique comment travailler avec Claude pour construire et interroger ce wiki.

---

## Ce qu'est ce wiki (et ce qu'il n'est pas)

Ce vault n'est pas un moteur de recherche. Tu n'y colles pas des articles en espérant les retrouver plus tard. C'est une **base de connaissances construite et maintenue par Claude** : chaque source que tu lui donnes est décomposée, reliée à ce qui existe déjà, et intégrée dans un réseau de pages interconnectées.

L'idée centrale : Claude écrit, toi tu lis et tu décides. Tu choisis les sources, tu poses les questions, tu valides ce qui compte. Claude fait le travail de synthèse, de liaison et de maintenance.

---

## Pré-requis

**Claude en mode Cowork**
Ce wiki fonctionne avec Claude dans son mode Cowork, accessible via l'application de bureau Claude. C'est ce mode qui permet à Claude d'accéder à un dossier sur ton ordinateur, d'y lire et d'y écrire des fichiers entre les sessions, et de maintenir une mémoire persistante du vault.

**Obsidian** — [obsidian.md](https://obsidian.md) (gratuit, Mac / Windows / Linux / iOS / Android)
Obsidian est l'interface de lecture et de navigation du wiki. C'est une application de prise de notes qui travaille directement sur des fichiers Markdown stockés localement — sans compte, sans cloud obligatoire, sans vendor lock-in. Tout ce que Claude écrit dans le vault est visible et navigable dans Obsidian : les liens markdown relatifs `[texte](chemin.md)` deviennent des connexions cliquables, le panneau Properties affiche le frontmatter de façon lisible, et la vue graphique rend visible la structure du réseau de connaissances au fil des ingestions. Ce format de lien (plutôt que le wikilink `[[...]]` propriétaire d'Obsidian) a été choisi pour que le vault reste aussi lisible et navigable sur GitHub. Obsidian ne modifie jamais les fichiers de façon opaque : ce que tu vois est ce qui est écrit sur le disque.

---

## Setup initial (une seule fois)

**0. Décompresse et renomme le template**
Décompresse `llm-wiki-template.zip` où tu veux sur ton ordinateur, puis renomme le dossier selon ton sujet — par exemple `wiki-ia-design` ou `wiki-climat`. Ce nom est libre, il n'a pas d'impact sur le fonctionnement interne.

**1. Ouvre ce vault dans Obsidian**
Fichier → Ouvrir dossier comme vault → sélectionne le dossier que tu viens de renommer.

**2. Active les Properties dans Obsidian**
Paramètres → Éditeur → Properties in document → sélectionne `Visible`. Le panneau de propriétés s'affiche alors en haut de chaque page.

**3. Définis le domaine** *(optionnel)*
Dans `CLAUDE.md`, tu peux remplacer `domaine: à définir` par ton sujet. En pratique, Claude infère le domaine dès le premier ingest à partir du contenu des sources — tu n'as pas besoin de le faire explicitement.

**4. Connecte Claude à ce dossier**
Dans Cowork, sélectionne ce dossier comme workspace. Claude lira `CLAUDE.md` automatiquement à chaque session et connaîtra ses instructions.

---

## Les quatre opérations

### INGEST — ajouter une source

Tu donnes une source à Claude (texte collé, URL, PDF). Il crée la fiche brute, rédige la fiche wiki, enrichit les pages existantes, et consigne tout dans le journal.

**Exemples de déclencheurs :**
```
ingère cet article : [colle le texte ou l'URL]
ingère ce PDF
ingère ces notes de réunion : [colle le texte]
```

**Ce que Claude produit :**
- `raw/AAAA-MM-JJ_<slug>.md` — la source brute, intacte
- `wiki/sources/<slug>.md` — résumé, thèses, citations clés
- Pages enrichies dans `wiki/concepts/` et `wiki/entities/`
- Une entrée dans `wiki/log.md`
- Un rapport dans le chat listant tout ce qui a été touché

**Règle d'or :** une source bien ingérée touche 10 à 15 pages. Si le rapport annonce moins de 5 pages, demande à Claude de creuser davantage les connexions.

---

### QUERY — interroger le wiki

Tu poses une question. Claude lit les pages pertinentes du wiki (pas les sources brutes) et répond en citant ses sources internes avec des liens markdown `[texte](chemin.md)`.

**Exemples de déclencheurs :**
```
quelle est la différence entre X et Y selon le wiki ?
fais une synthèse sur [thème]
quelles sont les tensions non résolues sur [sujet] ?
query : qu'est-ce que le wiki dit sur [concept] ?
```

**Ce que Claude produit :**
- Une réponse en prose avec liens internes
- Si la réponse dépasse 300 mots : une page archivée dans `wiki/questions/`
- Si une lacune est détectée : une note `[GAP]` dans `wiki/log.md`
- Si une comparaison est nécessaire : une page dans `wiki/comparisons/`

**Astuce :** demande des synthèses thématiques régulièrement. C'est là que le wiki prend tout son sens — Claude tisse des liens que tu n'aurais pas vus toi-même.

---

### VEILLE — chercher et ingérer du contenu web

Tu donnes un sujet. Claude cherche des articles récents sur le web, sélectionne les plus pertinents, et enchaîne les ingestions automatiquement.

**Exemples de déclencheurs :**
```
fais une veille sur [sujet]
cherche des articles récents sur [thème]
quoi de neuf sur [domaine] ?
veille : [sujet]
```

**Ce que Claude produit :**
- Une sélection d'articles pertinents et récents
- L'ingestion complète de chacun (raw + wiki + log)
- Un rapport de veille : sources trouvées, ingérées, pages créées
- La vérification des doublons via `wiki/sources/_registry.md`

**Conseil :** utilise la veille pour les sujets en mouvement rapide. Pour du contenu que tu as déjà en main (PDF, notes, articles sauvegardés), préfère l'INGEST direct.

---

### LINT — auditer le wiki

Tu lances un audit. Claude scanne le vault et te produit un rapport de santé : pages orphelines, contradictions, frontmatter manquant, sources non traitées.

**Exemples de déclencheurs :**
```
lint
audit le wiki
```

**Ce que Claude produit :**
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

**Quand lancer un lint :** après une dizaine d'ingestions, ou quand tu as l'impression que le wiki devient dense et difficile à naviguer.

---

## Structure des fichiers

```
vault/
├── CLAUDE.md          ← contrat de travail de Claude (ne pas modifier sauf le domaine)
├── raw/               ← sources brutes — ne jamais modifier
├── wiki/
│   ├── index.md       ← carte thématique, point d'entrée dans Obsidian
│   ├── overview.md    ← synthèse générale du domaine
│   ├── log.md         ← journal de tout ce qui se passe
│   ├── guide-prise-en-main.md  ← ce fichier
│   ├── concepts/      ← idées, théories, cadres abstraits
│   ├── entities/      ← personnes, outils, organisations
│   ├── syntheses/     ← analyses transversales
│   ├── comparisons/   ← face-à-face entre concepts ou approches
│   ├── questions/     ← réponses archivées aux questions importantes
│   └── sources/
│       ├── _registry.md  ← registre anti-doublon pour la veille
│       └── <slug>.md     ← une fiche par source ingérée
└── _meta/             ← configuration Obsidian (ne pas toucher)
```

---

## Le frontmatter — ce que tu dois savoir

Chaque page wiki commence par un bloc de métadonnées YAML. Obsidian l'affiche en panneau de propriétés. Claude le remplit automatiquement.

```yaml
---
type: concept          ← concept | entity | synthesis | comparison | question | source | index
tags:
  - tag1               ← format liste bloc, jamais [tag1, tag2]
  - tag2
created: 2026-07-01
updated: 2026-07-01
sources:
  - "[source-slug](../sources/source-slug.md)"  ← liens markdown relatifs entre guillemets
related:
  - "[autre-page](autre-page.md)"
---
```

**Important :** ne jamais utiliser le format inline `tags: [tag1, tag2]`. Obsidian l'affiche mal dans le panneau Properties. Claude connaît cette règle, mais si tu crées une page manuellement, respecte le format bloc.

---

## Bonnes pratiques

**Ingère par thème, pas en masse.** Trois sources bien ingérées valent mieux que dix traitées superficiellement. Laisse Claude tisser les liens entre chaque batch avant d'en ajouter d'autres.

**Lis le rapport d'ingest.** Le rapport que Claude affiche dans le chat après chaque ingestion te dit ce qui a changé. C'est ton principal outil de contrôle qualité.

**Utilise `wiki/index.md` comme point d'entrée.** C'est la carte thématique. Quand tu ne sais plus où chercher quelque chose, commence par là.

**Fais confiance aux tensions.** Les sections `## ⚡ Tension / Contradiction` que Claude ajoute sont souvent les passages les plus riches du wiki. Ce sont les endroits où le domaine n'a pas encore de réponse claire.

**Ne modifie pas les fichiers `raw/`.** Ce sont les sources brutes, immuables. Si tu veux annoter une source, fais-le dans `wiki/sources/<slug>.md`.

---

## Exemple de session type

```
# Tu ouvres Cowork avec ce vault sélectionné

> ingère cet article : [URL ou texte collé]

# Claude produit le rapport d'ingest

> fais une veille sur [même sujet]

# Claude cherche, sélectionne et ingère 3-5 articles

> quelle est la tension principale sur ce sujet selon le wiki ?

# Claude synthétise en citant les pages concernées

> lint

# Claude audite et te donne les actions prioritaires
```

---

*Ce guide est une page wiki comme les autres. Il peut être enrichi au fil du temps.*
