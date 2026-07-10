# Machine-Readable Design Systems: Designing for AI as a User

**Auteur** : Diana Wolosin
**Publication** : Design Systems Collective (Medium), mars 2026
**URL** : https://www.designsystemscollective.com/machine-readable-design-systems-designing-for-ai-as-a-user-28077c9f2144
**Série** : Articles de Diana Wolosin sur les design systems machine-readable

> Note : l'article original est sur une plateforme client-rendue (Medium). Ce fichier brut est reconstitué à partir du résumé de conférence publié par Into Design Systems (Substack, juin 2026 — https://intodesignsystems.substack.com/p/ai-design-system-mcp-example) et des résultats de recherche, qui couvrent la même présentation live à l'AI Conference for Designers 2026. Le contenu reflète fidèlement les thèses de l'auteure telles qu'exposées publiquement.

---

## "AI is a new user"

La thèse centrale de Diana Wolosin : l'IA est un nouvel utilisateur du design system. Comme tout utilisateur, elle a besoin que le système soit dans un format qu'elle peut comprendre. Ce format a un nom : machine-readable.

> "Codify your design system knowledge into structured data, metadata, schemas, explicit constraints so LLM can parse it, reason about it and use it programmatically."

Arrêter d'écrire de la documentation uniquement pour les humains. L'écrire pour que les LLM puissent raisonner dessus.

---

## Le format importe plus que le modèle

Première expérience de Diana : un Google Spreadsheet converti en snippets JSON par composant. Les développeurs les copient-collent dans des outils IA pour générer des prototypes. "It almost worked, but it was not enterprise grade."

Ce que l'expérience a prouvé : "The format matters. The format we feed to LLM impacts its reasoning and its output."

---

## Comment fonctionne le MCP, étape par étape

Diana décompose le flux MCP complet :
1. L'humain envoie un prompt depuis la context window
2. Le LLM extrait les mots-clés et formule une requête
3. Le MCP reçoit la requête
4. RAG agit comme un bibliothécaire, cherchant la similarité sémantique entre la requête et les métadonnées
5. La base vectorielle retourne les résultats
6. Le serveur MCP renvoie les résultats au LLM
7. Le LLM raisonne sur les résultats et prototype les expériences

> "A model context protocol is how you give an AI on-demand access to your design system knowledge."

---

## L'implémentation chez Indeed

Documentation MDX parsée en métadonnées structurées par des parsers JavaScript, un par domaine de connaissance (accessibilité, développement, localisation, design), fusionnée en un JSON par composant, puis ingérée, chunkée et indexée dans une base vectorielle open source appelée Vectra.

77 composants. Un pipeline qui se relance automatiquement à chaque mise à jour de la doc par un maintainer — les métadonnées servies par le MCP sont toujours fraîches.

---

## Le benchmark : 8 MCP, 1 056 prompts

Stack : Cursor et Claude Sonnet 4.5. Tony Rucker (partenaire développeur) construit l'infrastructure MCP et duplique le serveur MCP 7 fois pour créer 8 configurations différentes.

5 formats testés : Markdown, plain Markdown, hybrid Markdown + JSON, JSON, TOON (Token-Oriented Object Notation).

Calcul du benchmark : 22 prompts × 3 runs × 2 (MCP input et LLM output) × 8 configurations = 1 056 prompts.

Axes d'évaluation : token efficiency et LLM accuracy.

> "We were looking for the format that gives us the sharpest, most reliable, deterministic responses at the lowest token cost."

**Résultat clair : JSON.** Précision égale ou supérieure au hybrid Markdown + JSON avec environ 80 % de tokens en moins. En coût : les 22 requêtes benchmark sur la documentation Markdown originale coûtent ~$1 500/an. JSON : $300. Même design system, même composants, 5x moins cher.

Pourquoi JSON gagne : "JSON is like a contract: explicit keys, explicit values, explicit boundaries, no ambiguity. It tells the LLM exactly what it sees and how to use it."

Nuance de la Q&A : JSON pour les métadonnées structurées des composants. Pour les règles en langage naturel et les instructions, Markdown reste l'outil correct — avec front matter plutôt que verbosité.

Règle de Diana : **JSON for MCP, Markdown for LLM.**

---

## 4 300 prototypes IA sur un MCP de design system

Lancement du MCP avec le format gagnant en août. D'août à décembre : 4 300 prototypes générés sur un outil de prototypage IA interne alimenté par le design system MCP. Product managers, researchers, content — pas seulement des développeurs. Tous utilisant des composants React du design system Indeed et le visual language d'Indeed.

Ces prototypes n'ont **pas** été générés par un MCP Figma. Ils **n'utilisaient pas** Tailwind CSS.

---

## Pourquoi un MCP parfaitement structuré produit encore des prototypes cassés

Keith Weston (lead designer) audite un échantillon des 4 300 prototypes : violations de typographie, espacement cassé, une palette de couleurs inventée que l'équipe design system n'a jamais approuvée, des emojis à la place des icônes.

Les composants étaient corrects. Les **fondations** se cassaient.

Diagnostic de Diana :
> "The MCP is on demand. It only returns fresh data about what you asked for. If the prompt says 'build me a card', it's going to give you information about the card and a button. But it's going to fully ignore the spacing, the typography, the colors, because that foundation knowledge wasn't called in the prompt."

La base vectorielle contenait tout. Le LLM n'a simplement jamais demandé les fondations. Il a comblé le vide avec ses propres hypothèses — et ces hypothèses étaient fausses.

**Distinction clé :**
- MCP = **on demand** (retourne uniquement ce qu'on demande)
- Rules = **always on** (contexte permanent, toujours présent)
- Ne jamais confondre les deux.

---

## La solution : le plugin (Rules + MCP + AGENTS.md)

L'architecture en couches combinant Rules, MCP et AGENTS.md dans ce que Diana appelle un "plugin". C'est la réponse au problème des fondations — mais les détails techniques restent dans la session complète de la conférence (payante).

---

## Takeaways de Diana

- Ne pas débattre Markdown vs JSON pour la consommation IA — lancer un mini-benchmark et laisser les chiffres trancher
- Traiter le MCP comme **on demand**, traiter les règles comme **always on** — ne jamais confondre les deux
- Mesurer les **hallucinations comme une métrique**, pas comme un feeling
- Pour les design systems machine-readable : penser **plugin**, pas juste MCP

---

## Contexte auteure

Diana Wolosin : Senior Product Designer, Architecture and Systems chez Netflix (ex-Indeed). 10 ans d'expérience à construire des systèmes à grande échelle. Actuellement focalisée sur les design systems machine-readable comme infrastructure IA, avec un accent sur les frameworks d'évaluation et la gouvernance du contexte.
