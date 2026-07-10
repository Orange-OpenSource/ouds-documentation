---
type: source
tags: [design-system, documentation, automatisation, figma, mcp, mintlify, github-actions]
created: 2026-06-17
updated: 2026-06-17
sources:
related:
  - "[[romina-kavcic]]"
  - "[[documentation-lag]]"
  - "[[pipeline-figma-docs-automatise]]"
  - "[[mintlify]]"
  - "[[mcp-model-context-protocol]]"
  - "[[boucle-feedback-infrastructure]]"
---

## How to Automate Design System Documentation

**Auteure** : [[romina-kavcic]]
**Publication** : thedesignsystem.guide (Substack), 17 octobre 2025
**URL** : https://learn.thedesignsystem.guide/p/how-to-automate-design-system-documentation
**Sous-titre** : "From Figma to Mintlify"
**Fichier brut** : `raw/How to Automate Design System Documentation.md`

---

## Résumé structuré

Guide pratique pour éliminer le lag de documentation des design systems en connectant Figma (via API et MCP), un outil IA (Claude Code), et Mintlify (hébergement de docs). Le diagnostic : les équipes "optimisent le mauvais truc" — process plus stricts, rappels automatiques — alors que la seule vraie solution est de connecter les outils pour qu'ils se documentent eux-mêmes. L'article propose deux flux : on-demand (le designer partage un lien Figma, tout se met à jour en 30 secondes) et automatisé (GitHub Action hebdomadaire qui vérifie les frames trackées).

---

## Thèses principales

**Thèse 1 — Le problème n'est pas le process, c'est le lag structurel.** Un designer met à jour un bouton dans Figma. Le développeur l'implémente. Les docs sont mises à jour "dans une semaine ou deux, peut-être". Ce lag de 3 semaines est structurel — il vient de l'absence de connexion entre les outils, pas d'un manque de discipline. Les solutions habituelles (cadences d'update strictes, rappels automatiques, impliquer plus de personnes) optimisent le process sans toucher au problème. "The only way to kill latency is to connect your tools so they document themselves."

**Thèse 2 — MCP comme pont Figma → IA.** Figma MCP donne à Claude Code un accès en lecture directe aux fichiers de design : specs de composants (espacement, couleurs, typographie), noms exacts des tokens Figma Variables, variants et états interactifs, screenshots haute résolution (PNG 2x), timestamps de dernière modification. Plus de copier-coller de specs.

**Thèse 3 — Deux modes de sync, deux usages.** Flow 1 (on-demand) : le designer colle un lien Figma dans Claude Code → lecture du frame → export screenshot → lecture des docs existantes → mise à jour des `.mdx` → PR avec diff visuel → Mintlify déploie automatiquement. 30 secondes vs 30 minutes. Flow 2 (automatisé) : GitHub Action hebdomadaire qui scanne les fichiers `.mdx` pour les commentaires `<!-- figma-frame: FILE_ID/NODE_ID -->`, vérifie si les frames ont été modifiées depuis le dernier screenshot, exporte et met à jour si c'est le cas, crée une PR si des changements existent.

**Thèse 4 — Le frame ID tracking comme mécanisme de liaison.** Le commentaire `<!-- figma-frame: FILE_ID/NODE_ID -->` dans les fichiers `.mdx` est la cheville ouvrière de l'automatisation. Il lie un fichier de documentation à son source Figma. Sans ce lien explicite, l'automatisation ne sait pas quel frame surveiller. C'est un contrat entre la documentation et son source.

**Thèse 5 — Les writing guidelines pour la cohérence.** Pour des résultats consistants avec Claude Code, créer un fichier Markdown de writing guidelines (ton, voix, règles de rédaction, exemples de dos/don'ts). C'est l'équivalent documentaire des Rules de l'architecture Skills/Rules/Instructions.

---

## Stack documenté

Figma (API Personal Access Token + MCP Figma) + Claude Code + Mintlify (hébergement docs, auto-deploy sur push Git) + GitHub Actions (automation weekly). Secrets GitHub nécessaires : `FIGMA_PERSONAL_ACCESS_TOKEN` et `ANTHROPIC_API_KEY`.

---

## Citations clés

> "The only way to kill latency is to connect your tools so they document themselves."

> "That's optimizing the wrong thing." (à propos des process d'update manuels)

---

## Connexions identifiées

[[documentation-lag]] formalise le problème central. [[pipeline-figma-docs-automatise]] documente le flux complet. [[mintlify]] est une nouvelle entité à créer. Enrichit [[boucle-feedback-infrastructure]] (la documentation auto-mise à jour est une boucle de feedback concrète entre Figma et les docs), [[mcp-model-context-protocol]] (usage Figma MCP pour la documentation), [[processus-generation-metadata-echelle]] (variante plus automatisée du pipeline de génération). Les writing guidelines mentionnées rejoignent [[architecture-skills-rules-instructions]] (Rules comme contexte de génération).
