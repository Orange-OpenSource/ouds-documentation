---
name: web-veille
description: >
  Skill de veille thématique web pour vault LLM Wiki. Déclenche quand l'utilisateur
  demande de chercher des articles récents, faire une veille, trouver de nouvelles
  sources, surveiller un sujet, ou enrichir le wiki avec des contenus frais du web.
  À utiliser systématiquement pour toute phrase du type "cherche des articles sur",
  "fais une veille sur", "quoi de neuf sur", "trouve des sources récentes sur",
  "alimente le wiki avec", "ingère des articles sur".
---
# Skill : Veille Web Thématique → Vault LLM Wiki
Ce skill conduit une recherche web sur un thème donné, produit un rapport de veille
commenté, puis ingère sélectivement les meilleurs résultats dans le vault selon les
conventions définies dans `CLAUDE.md`.
---
## Pré-requis
Avant d'exécuter ce skill, lire `CLAUDE.md` à la racine du vault pour connaître :
- La structure des dossiers `raw/` et `wiki/`
- Les conventions de frontmatter
- Le format d'entrée dans `wiki/log.md`
Si `CLAUDE.md` est absent ou illisible, interrompre et demander à l'utilisateur
de pointer sur le bon dossier vault.
---
## Paramètres d'entrée
L'utilisateur fournit (en une phrase ou en répondant aux questions de clarification) :
| Paramètre | Description | Défaut |
|---|---|---|
| `thème` | Sujet de recherche | obligatoire |
| `fraîcheur` | Période souhaitée | "récents" (3 derniers mois) |
| `langue` | Langue des résultats | français en priorité, anglais accepté |
| `nb_sources` | Nombre de sources à évaluer | 8–12 |
| `seuil_ingestion` | Pertinence minimale pour ingestion | élevée (score ≥ 4/5) |
Si le thème n'est pas précisé, demander avant de lancer la recherche.
---
## Séquence d'exécution
### Phase 1 — Recherche web (3 à 5 requêtes)
Construire des requêtes complémentaires pour couvrir le thème sous plusieurs angles.
Ne pas répéter les mêmes mots-clés. Exemples de variation :
- Requête principale sur le thème central
- Requête sur les débats ou controverses liés
- Requête sur les développements récents ou applications pratiques
- Requête en anglais si le thème est international
Pour chaque requête, utiliser l'outil `web_search` natif.
Ne pas fetch systématiquement chaque URL — réserver `web_fetch` aux articles
dont le snippet est insuffisant pour évaluer la pertinence.
### Phase 2 — Rapport de veille
Produire un rapport structuré en markdown avec ce format exact :
```markdown
# Rapport de veille : [THÈME]
Date : AAAA-MM-JJ
Requêtes effectuées : N | Sources évaluées : N | Retenues pour ingestion : N
---
## Résultats
### [Score: X/5] [TITRE DE L'ARTICLE]
**Source** : Nom du média | **Date** : date | **URL** : url
**Résumé** : 2-3 phrases sur la thèse principale et l'apport spécifique.
**Connexions wiki** : liens vers pages existantes du vault potentiellement enrichies.
**Recommandation** : Ingérer / Écarter / À surveiller
**Motif** : une phrase expliquant la décision.
---
[répéter pour chaque source]
## Synthèse de la veille
[3-5 phrases : tendances identifiées, tensions émergentes, lacunes dans le wiki]
## Prochaines veilles suggérées
[2-3 angles non couverts qui mériteraient une prochaine session]
```
**Critères de scoring (1 à 5)** :
- 5 — apport direct, thèse originale, source fiable, récent
- 4 — pertinent, bien sourcé, enrichit une page existante
- 3 — tangentiel ou trop général, utilité marginale
- 2 — hors sujet partiel, qualité douteuse
- 1 — non pertinent, bruit, source non fiable
### Phase 3 — Confirmation avant ingestion
Après avoir affiché le rapport, demander confirmation :
> "J'ai retenu N sources pour ingestion (score ≥ 4/5). Veux-tu que j'ingère
> toutes les sources recommandées, une sélection, ou aucune pour l'instant ?"
Ne jamais ingérer sans confirmation explicite de l'utilisateur.
### Phase 4 — Ingestion sélective (si confirmée)
Pour chaque source retenue, exécuter le workflow INGEST défini dans `CLAUDE.md` :
1. Créer `raw/AAAA-MM-JJ_<slug>.md` avec le contenu brut (titre, URL, résumé complet).
2. Créer `wiki/sources/<slug>.md` avec la fiche structurée.
3. Mettre à jour les pages de concepts/entités concernées.
4. Mettre à jour `wiki/overview.md` si la source modifie l'image du domaine.
5. Signaler les contradictions avec les pages existantes.
6. Enregistrer dans `wiki/log.md` :
   ```
   ## [AAAA-MM-JJ] ingest | [TITRE] (via veille web)
   Thème de veille : [thème]
   Pages touchées : [[page1]], [[page2]]...
   Note : [apport principal de cette source]
   ```
Après toutes les ingestions, afficher un bilan :
```
VEILLE TERMINÉE
───────────────
Sources évaluées    : N
Sources ingérées    : N
Pages créées        : N
Pages mises à jour  : N
Contradictions      : N
Prochaine veille suggérée : [thème / angle]
```
---
## Gestion des cas particuliers
**Article en anglais** : ingérer en traduisant le résumé en français dans la fiche
`wiki/sources/`, mais conserver le titre original et l'URL.
**Source derrière un paywall** : noter "accès restreint" dans la fiche source,
ingérer uniquement à partir du snippet public disponible, signaler la limite.
**Source déjà présente dans le vault** : ne pas recréer la fiche. Vérifier si
la nouvelle occurrence apporte des informations complémentaires et, si oui,
mettre à jour la fiche existante avec une section `## Mise à jour AAAA-MM-JJ`.
**Contradiction avec une page wiki existante** : ne pas résoudre arbitrairement.
Ajouter une section `## ⚡ Tension` dans la page concernée avec les deux positions
et leurs sources respectives. Signaler à l'utilisateur dans le bilan.
**Thème absent du vault** : si aucune page existante n'est concernée, créer une
page `wiki/concepts/<slug>.md` d'amorçage avec un frontmatter minimal et une
section "À développer", puis la lier depuis `wiki/index.md`.
---
## Commandes utilisateur reconnues
| Commande | Action |
|---|---|
| `veille : [thème]` | Lance le skill complet |
| `veille rapide : [thème]` | Rapport seul, sans ingestion |
| `ingère la veille` | Ingère après avoir vu le rapport |
| `ingère seulement [titres]` | Ingestion sélective partielle |
| `écarte tout` | Rapport conservé, aucune ingestion |
---
## Ce que ce skill ne fait pas
- Il ne résume pas des documents PDF locaux (utiliser le workflow INGEST standard).
- Il ne crée pas de pages wiki sans avoir d'abord affiché le rapport.
- Il ne modifie jamais `CLAUDE.md`.
- Il ne supprime jamais de pages existantes.
- Il ne fait pas de veille sur des sources non publiques (intranet, paywalls complets).
