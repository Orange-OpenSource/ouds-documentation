---
source_url: https://learn.thedesignsystem.guide/p/5-mcp-connections-every-design-system
author: Romina Kavcic (The Design System Guide)
published: 2025-08-22
ingested: 2026-07-16
---

# 5 MCP Connections Every Design System Team Needs Right Now

Source brute — contenu issu de thedesignsystem.guide (Substack).

## Résumé du contenu

Inventaire pratique de 6 connecteurs MCP pour équipes design system, avec niveau de complexité d'installation et exemples de prompts concrets. Outils recommandés pour le pont IA↔outils : Cursor, Claude Desktop, ou Claude Code.

### Complexité d'installation
- Figma MCP : facile
- Mintlify : facile (clé API requise)
- GitHub : facile (personal access token requis)
- GitLab : modérée (nécessite tier Premium + setup technique)
- PostHog : modérée (nécessite tracking d'événements implémenté)
- Slack : modérée (approbation admin + setup OAuth)

### Figma MCP
Connecte les fichiers de design directement aux workflows IA. Lit composants, tokens, variants depuis Figma. Exemples : générer des specs de composant ("Generate specs for our new modal component"), lister les tokens de couleur utilisés, créer des prototypes cliquables avec états hover/active/pressed.

### Mintlify
Transforme la documentation en base de connaissances vivante consultable directement depuis l'éditeur. Exemples : lookup de documentation, récupération d'exemples de code, génération de specs combinant contenu Mintlify + codebase.

### GitHub
Empêche la dérive design/code. L'agent peut ouvrir des PRs, review du code, lire des diffs, garder tokens/documentation synchronisés avec la codebase. Exemples : review de PR avec détection de tokens manquants, génération de changelog depuis l'historique de commits, comparaison Figma Variables vs tokens du repo.

### GitLab
Nécessite au minimum le tier Premium (Ultimate fonctionne aussi) — les tiers Free/Starter n'exposent pas le serveur MCP. Exemples : liste des merge requests ouvertes, ajout de commentaires sur une MR, déclenchement de pipeline CI avec rapport de statut.

### PostHog
Apporte les analytics produit directement dans le workflow IA pour valider les décisions de design system avec des données d'usage réelles. Nécessite un projet PostHog avec MCP activé et des composants trackés avec attributs analytics. Exemples : comparaison d'interaction entre ancien et nouveau bouton primaire, partage du CRO après publication de nouveaux composants, taux de complétion d'un flow avec un nouveau composant stepper.

### Slack MCP
Connecte l'historique des conversations d'équipe au workflow IA. Recherche l'historique de messages, trace les décisions de design, poste des mises à jour, monitore les discussions de composants. Exemples : retrouver une décision prise en design review, compiler le feedback sur un composant depuis un canal, alerter quand quelqu'un mentionne construire un dropdown custom, identifier les questions les plus fréquentes sur les composants.

### Limitations actuelles
Pas tous les outils n'ont de serveur MCP (pas de support natif Storybook ou Jira au moment de la publication). Certains nécessitent des tiers payants. Le setup initial demande des connaissances techniques. La performance dépend des rate limits API. Certains serveurs sont communautaires (Slack) tandis que d'autres sont officiels (GitLab, PostHog).

### Sécurité et contrôle
Avec MCP, on contrôle exactement quelles données et quels outils l'IA peut accéder — pas un accès libre, mais des ponts contrôlés et spécifiques. Le protocole est open-source et standardisé : pas de lock-in fournisseur.

### Recommandation de démarrage
Commencer petit : choisir un outil, configurer le MCP, automatiser une tâche répétitive. Commencer par Figma + Cursor/Claude.
