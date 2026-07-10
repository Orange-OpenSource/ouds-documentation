# LLM Wiki — Guide de démarrage

> Vault Obsidian configuré selon la méthode LLM Wiki d'Andrej Karpathy.
> Optimisé pour une utilisation avec Claude (CLAUDE.md comme schéma).

---

## Principe fondamental

Ce vault n'est **pas** un système de prise de notes classique.
C'est une **base de connaissances persistante et cumulante**, maintenue par Claude.

**Toi** : tu choisis les sources, tu poses les questions, tu lis le wiki.
**Claude** : il écrit le wiki, maintient les liens, signale les contradictions.

---

## Structure

```
vault/
├── CLAUDE.md          ← instructions pour Claude (lire en premier à chaque session)
├── raw/               ← tes sources brutes, jamais modifiées
├── wiki/
│   ├── index.md       ← point d'entrée thématique
│   ├── overview.md    ← synthèse générale du domaine
│   ├── log.md         ← journal chronologique
│   ├── concepts/
│   ├── entities/
│   ├── syntheses/
│   ├── comparisons/
│   ├── questions/
│   └── sources/
└── _meta/             ← configuration Obsidian
```

---

## Les trois opérations

### 1. `ingest` — Ajouter une source
```
ingest

[colle ici : texte d'un article, URL, notes brutes, extrait PDF...]
```
Claude lit la source, met à jour 10-15 pages wiki, enregistre dans le log.

### 2. `query` — Poser une question
```
query : Quelle est la tension entre X et Y dans la littérature ingérée ?
```
Claude répond à partir du wiki (pas des sources brutes), archive si pertinent.

### 3. `lint` — Auditer le wiki
```
lint
```
Claude identifie orphelins, contradictions, lacunes. Produit un rapport structuré.

---

## Workflow recommandé avec Claude

1. **Ouvre une nouvelle conversation Claude.**
2. **Copie-colle `CLAUDE.md`** en premier message (ou glisse le fichier).
3. Dis : `Voici le schéma de mon vault LLM Wiki. Domaine de ce vault : [ton sujet].`
4. Lance ta première ingestion.

**Conseil** : garde Obsidian ouvert à côté de Claude. Tu verras le wiki se construire en temps réel dans le graph view.

---

## Initialisation : définis ton domaine

Avant la première ingestion, précise à Claude :

```
Voici CLAUDE.md [colle le contenu].

Domaine de ce vault : [ex. "philosophie politique contemporaine", 
"design de jeux de rôle", "économie des communs"...]

Première source à ingérer : [...]
```

---

## Plugins Obsidian recommandés

- **Graph View** : visualiser les liens entre pages (essentiel)
- **Dataview** : requêtes sur le frontmatter (ex : toutes les pages `type: synthesis`)
- **Templater** : templates pour les nouvelles pages
- **Tag Wrangler** : gérer les tags au fil du temps

---

## Ce que ce vault n'est pas

- Pas un second cerveau de type Zettelkasten (c'est Claude qui écrit, pas toi)
- Pas un système RAG (la synthèse est pré-compilée, pas recalculée à la demande)
- Pas un outil de gestion de tâches

---

*Basé sur le gist `llm-wiki.md` d'Andrej Karpathy (avril 2026).*
*Adapté pour Claude et Obsidian.*
