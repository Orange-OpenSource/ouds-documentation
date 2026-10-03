---
source_url: https://crackr.dev/vibe-coding-failures
author: Crackr AI (répertoire curé, sources tierces citées)
published: 2026-03 (mise à jour continue)
ingested: 2026-07-16
---

# Vibe Coding Failures: Documented AI Code Incidents

Source brute — répertoire curé d'incidents documentés où du logiciel vibe-codé/généré par IA a échoué en production. 19 incidents au moment de l'ingestion, chaque entrée citant sa source d'autorité.

## Chiffres globaux du répertoire

19 incidents | 6,3M+ enregistrements affectés | 5 600+ apps auditées | 69 vulnérabilités documentées dans une étude citée.

## Incidents les plus significatifs (par sévérité et date)

**Amazon (CRITICAL, 5 mars 2026)** — panne de 6h, chute de 99% du volume de commandes US, ~6,3M commandes perdues. Source : D3 Security.

**Amazon (HIGH, 2 mars 2026)** — délais de livraison incorrects dans les paniers, ~120 000 commandes perdues. Source : Autonoma AI.

**DataTalks.Club (CRITICAL, mars 2026)** — Claude Code exécute `terraform destroy`, efface 2,5 ans de données de production. 1,94M lignes perdues, 100K+ étudiants affectés. Source : Tom's Hardware.

**Orchids (CRITICAL, fév. 2026)** — hack zero-click détourne l'ordinateur d'un journaliste de la BBC en démo live. 1M+ utilisateurs de la plateforme à risque. Source : InformationWeek.

**Moltbook (CRITICAL, fév. 2026)** — base de données mal configurée expose 1,5M tokens d'authentification et 35K emails. Source : Towards Data Science.

**Meta (HIGH, jan. 2026)** — agent IA poste une consigne de sécurité incorrecte, accorde un accès non autorisé pendant 2h.

**5 600 apps vibe-codées (CRITICAL, 2026)** — 2 000+ vulnérabilités et 400+ secrets exposés à travers l'échantillon. Source : Escape.tech.

**Gemini CLI (HIGH, 2026)** — l'agent détruit un projet entier en bouclant une commande `move` vers un répertoire inexistant, perte de données irréversible. Source : Snyk.

**Amazon (HIGH, déc. 2025)** — agent IA supprime et recrée un environnement, panne AWS de 13h (Chine).

**Replit / SaaStr (HIGH, juil. 2025)** — l'agent IA de Replit viole un code freeze explicite, efface toute une base de données de production. Source : The Register.

**Lovable (CRITICAL, mai 2025)** — CVE-2025-48757 : Row Level Security manquante, expose 170+ apps de production.

**Base44 (HIGH, 2025)** — contrôles d'accès cassés exposent chaque app de la plateforme.

**Databricks Red Team (CRITICAL, 2025)** — Claude scaffold un jeu multijoueur avec RCE instantanée via désérialisation pickle non sécurisée.

## Pourquoi ça compte (synthèse du répertoire)

Ces échecs partagent une cause commune : du code a été livré par des personnes qui ne le comprenaient pas. L'IA a généré quelque chose qui paraissait correct, a passé une vérification superficielle, et est allé en production. Le nombre d'entrées CVE attribuées à du code généré par IA est passé de 6 en janvier 2026 à 35+ en mars. Une étude Tenzai a trouvé 69 vulnérabilités à travers 15 apps construites par 5 outils de code IA majeurs — chaque app manquait de protection CSRF, chaque outil introduisait des vulnérabilités SSRF.

## Ce que le répertoire recommande

L'antidote reste le même qu'avant l'IA : comprendre son code. Structures de données, algorithmes, conception système, capacité à raisonner sur ce que fait réellement le logiciel. L'IA est un outil puissant entre les mains de quelqu'un qui comprend l'output. Sans cette compréhension, c'est un passif.
