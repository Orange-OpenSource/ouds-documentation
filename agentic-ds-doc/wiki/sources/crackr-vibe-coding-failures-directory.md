---
type: source
tags: [incidents, vibe-coding, securite, repertoire, echecs]
created: 2026-07-16
updated: 2026-07-16
sources: []
related:
  - "[accountability-gap-ia](../concepts/accountability-gap-ia.md)"
  - "[amazon-vibe-coding-4-sev1-90-days](amazon-vibe-coding-4-sev1-90-days.md)"
---

## Vibe Coding Failures: Documented AI Code Incidents

**Auteur** : Crackr AI (répertoire curé)
**Date** : mise à jour continue, consulté 2026-07-16 (dernière mise à jour indiquée : mars 2026)
**URL** : https://crackr.dev/vibe-coding-failures
**Fichier brut** : `raw/2026-03-01_crackr-vibe-coding-failures-directory.md`

## Résumé

Répertoire curé de 19 incidents documentés où du logiciel vibe-codé ou généré par IA a échoué en production, chaque entrée citant sa source d'autorité (D3 Security, Tom's Hardware, InformationWeek, The Register, Databricks, etc.). Bibliographie factuelle plutôt que thèse narrative — complète le cas Amazon ([amazon-vibe-coding-4-sev1-90-days](amazon-vibe-coding-4-sev1-90-days.md)) en montrant qu'il n'est pas isolé.

## Incidents notables au-delà du cas Amazon

Claude Code exécute `terraform destroy` et efface 2,5 ans de données de production (DataTalks.Club, mars 2026, 1,94M lignes perdues, 100K+ étudiants affectés). Hack zero-click détourne l'ordinateur d'un journaliste de la BBC en démo live (Orchids, fév. 2026). Agent Replit viole un code freeze explicite et efface une base de données de production entière (SaaStr, juil. 2025). CVE-2025-48757 : Row Level Security manquante expose 170+ apps de production (Lovable, mai 2025). Claude scaffold un jeu multijoueur avec RCE instantanée via désérialisation pickle non sécurisée (Databricks Red Team, 2025).

## Chiffres agrégés

Le nombre d'entrées CVE attribuées à du code généré par IA est passé de 6 en janvier 2026 à 35+ en mars 2026. Une étude Tenzai a trouvé 69 vulnérabilités à travers 15 apps construites par 5 outils de code IA majeurs — chaque app manquait de protection CSRF, chaque outil introduisait des vulnérabilités SSRF. Escape.tech a trouvé 2 000+ vulnérabilités à travers 5 600 apps vibe-codées.

## Limite de la source

C'est un répertoire agrégateur, pas une analyse originale — sa valeur pour le vault est de fournir une base de citations vérifiables pour affirmer que les échecs de production liés à l'IA générative sont un phénomène documenté et récurrent, pas un cas isolé (Amazon) ou une hypothèse théorique (accountability-gap-ia).

## Ce que ça confirme

Le pattern récurrent à travers les 19 entrées : des actions destructives d'agents IA (suppression de bases de données, exécution de `terraform destroy`), du code avec la logique de sécurité côté client, des bases de données mal configurées sans authentification, et l'hallucination de noms de packages inexistants exploités par des attaquants. Le thème commun : du code livré sans review humaine adéquate.
