# 👋 Start here — Wiki LLM Design systems agentiques

> Base de connaissances persistante et cumulative sur l'intersection entre les **design systems** et l'**IA agentique**, construite et maintenue par Claude à partir de sources choisies par l'humain. Ce fichier est le point d'entrée : commence ici.

---

## Par où commencer

- **[Vue d'ensemble](wiki/overview.md)** — synthèse de l'état du domaine, thèse centrale, tensions principales. Le meilleur point d'entrée pour comprendre ce que dit le corpus aujourd'hui.
- **[Index thématique](wiki/index.md)** — carte complète du wiki : tous les concepts, entités, synthèses et comparaisons, organisés par thème.
- **[Journal du wiki](wiki/log.md)** — historique chronologique de chaque ingestion, mise à jour et query, du plus ancien au plus récent.
- **[Guide de prise en main](wiki/guide-prise-en-main.md)** — pour configurer et utiliser ce vault avec Obsidian et Claude (mode Cowork), si tu repars de zéro.

## Ce que c'est, ce que ce n'est pas

Ce vault n'est pas un système RAG ni un second cerveau classique : la synthèse est pré-compilée par Claude au fil des ingestions, pas recalculée à la demande. La division du travail est stricte : l'humain choisit les sources et pose les questions, Claude écrit le wiki, tisse les liens et signale les contradictions. Le contrat complet de cette collaboration est dans [CLAUDE.md](CLAUDE.md).

## Structure

```
vault/
├── README.md           ← ce fichier, point d'entrée
├── CLAUDE.md            ← contrat de travail de Claude (structure, conventions, opérations)
├── raw/                 ← sources brutes, immuables
├── wiki/
│   ├── overview.md       ← synthèse générale du domaine
│   ├── index.md          ← carte thématique complète
│   ├── log.md            ← journal chronologique
│   ├── guide-prise-en-main.md
│   ├── concepts/         ← idées, théories, cadres abstraits
│   ├── entities/         ← personnes, organisations, outils
│   ├── syntheses/        ← analyses transversales, tensions
│   ├── comparisons/       ← tableaux comparatifs
│   ├── questions/        ← réponses archivées à des questions spécifiques
│   └── sources/          ← une fiche par source ingérée
├── Journal/              ← bilans périodiques (opération Évolutions)
└── _meta/                ← configuration Obsidian
```

## Les quatre opérations

Détaillées dans [CLAUDE.md](CLAUDE.md) : `ingest` (ajouter une source), `query` (interroger le wiki), `lint` (auditer la santé du vault), `évolutions` (bilan d'une période — jour, semaine, mois).

## Consultation

Ce vault se lit aussi bien dans **Obsidian** (graph view, backlinks, panneau de propriétés — voir le [guide de prise en main](wiki/guide-prise-en-main.md)) que directement sur **GitHub** : tous les liens internes sont des liens markdown relatifs standards, pas des wikilinks `[[...]]`, pour rester navigables dans les deux interfaces.

---

*Méthode inspirée du gist `llm-wiki.md` d'Andrej Karpathy, adaptée pour Claude en mode Cowork.*
