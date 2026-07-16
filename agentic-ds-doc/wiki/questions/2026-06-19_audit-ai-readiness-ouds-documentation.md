---
type: question
tags: [audit, ia, design-system, ouds, documentation, machine-readable, readiness]
created: 2026-06-19
updated: 2026-06-19
sources: []
related:
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md)"
  - "[protocole-arc](../concepts/protocole-arc.md)"
  - "[modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md)"
  - "[workflows-ia-metadata](../concepts/workflows-ia-metadata.md)"
---

# Audit AI readiness — ouds-documentation (juin 2026)

**Repo audité** : [Orange-OpenSource/ouds-documentation](https://github.com/Orange-OpenSource/ouds-documentation)  
**Question posée** : la documentation OUDS est-elle prête pour une consommation par des agents IA ?

---

## Ce que contient le repo

La structure réelle, après inspection fichier par fichier via l'API GitHub :

```
ouds-documentation/
├── .github/
├── components/
│   ├── action/
│   │   └── button/
│   │       ├── button/         ← button.md (16 Ko) + dsm/ + figma/ + history/ + images/
│   │       ├── expand_button/
│   │       └── navigation_button/
│   ├── content_display/
│   ├── control/
│   ├── dialog/
│   ├── indicator/
│   ├── layout/
│   └── navigation/
├── tokens/
│   ├── jsonl-ai/               ← format machine (64 fichiers JSON par thème/catégorie)
│   │   ├── orange/
│   │   ├── sosh/
│   │   └── wireframe/
│   └── md/                     ← format humain (Markdown)
│       ├── orange/
│       ├── sosh/
│       └── wireframe/
├── .gitignore
└── README.md                   ← quasi vide (titre uniquement)
```

Ce repo est la source de vérité documentaire multi-plateforme de l'écosystème OUDS, distinct des implémentations (`ouds-ios`, `ouds-android`, `ouds-flutter`). Il est probablement alimenté par le *tokenator* — outil interne qui convertit les exports Figma JSON en fichiers de tokens.

Deux signaux montrent que l'équipe pense déjà à l'IA : le dossier `tokens/jsonl-ai/` est nommé explicitement pour la consommation machine, et les fichiers composants portent des marqueurs `👈🤖` (sections ciblées agents) vs `👈🤔` (sections ciblées designers). Le repo n'est pas naïf face à l'IA. Il est à mi-chemin.

---

## Évaluation par couche (framework de [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md))

### Couche 1 — Index (qu'est-ce qui existe ?)

**Verdict : partiel.**

Les 64 fichiers JSON de tokens couvrent toutes les catégories : couleurs (action, bg, border, content, overlay, surface, opacity — en variante dark et light), typographie (par plateforme et taille d'écran), espacement, taille, grille, élévation, opacité, border-radius. La structure par thème (orange, sosh, wireframe) est claire et cohérente.

Ce qui manque : une **carte relationnelle**. Quel composant utilise quels tokens ? Quelles dépendances entre composants (Dialog contient Button, Badge utilise color.status.*) ? Un agent qui arrive dans ce repo sans ce graphe doit explorer à l'aveugle. Aucun fichier `index.json` n'est visible. La couche 1 existe sous forme de liste, pas sous forme de graphe navigable.

### Couche 2 — Métadonnées d'intent (comment et pourquoi ?)

**Verdict : structure présente, contenu absent.**

C'est le paradoxe central du repo. Le schéma JSON des tokens est exactement ce qu'il faut :

```json
{"ouds.color.action.negative.enabled": {
  "type": "color",
  "value": {"core token": "core-ouds.color.functional.scarlet.300", "raw value": {"value": {"value": "#ff8081"}}},
  "description": ""
}}
```

Le champ `description` existe dans le schéma. Il est **toujours vide** sur l'intégralité des 64 fichiers inspectés. Un agent qui interroge `ouds.color.action.negative.enabled` obtient `#ff8081` et son core token, mais aucune réponse à "quand l'utiliser" ou "pourquoi pas `ouds.color.action.enabled`". L'[intent](../concepts/intent-token.md) — la raison d'être d'un token sémantique — n'est encodé nulle part.

Du côté composants, `button.md` (16 Ko) est un document dense couvrant définition, "Best for", anatomie, variantes avec do&don'ts, états, accessibilité WCAG, et changelog. Le contenu est riche. Mais il est en Markdown structuré pour la lecture humaine, non queryable programmatiquement. La [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) exige une traduction de ce savoir en format structuré — ce que [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) appelle "reformatter existing knowledge, not create new documentation."

### Couche 3 — Raisonnement (quelle logique de composition ?)

**Verdict : absent.**

Aucune règle de composition formalisée. Pas de "Dialog + Alert + Button Cancel + Button Action pour une confirmation destructive". Pas de patterns d'assemblage. Un agent qui consomme ce repo peut savoir que Button existe avec ses variantes Negative, Default, Strong — il ne peut pas inférer que la variante Negative exige une option d'annulation, ni que deux boutons Strong dans le même contexte violent les guidelines.

---

## Position sur le modèle de maturité ([modele-maturite-ia-design-system](../concepts/modele-maturite-ia-design-system.md))

Sur l'axe "infrastructure agentique" (distinct du modèle de maturité des features IA pour utilisateurs humains de Kavcic) :

| Critère | État |
|---|---|
| Fichier de contexte IA (AGENTS.md, CLAUDE.md) | ❌ Absent |
| Format machine-optimal pour les tokens (JSON) | ✅ Présent (`jsonl-ai/`) |
| Intent encoding dans les tokens | ⚠️ Structure présente, champs `description` vides |
| Docs composants avec marqueurs IA | ⚠️ Présent (`👈🤖`), non structuré pour requêtes programmatiques |
| Index relationnel composants/tokens | ❌ Absent |
| Mapping composant → tokens utilisés | ❌ Absent |
| Métadonnées JSON par composant | ❌ Absent |
| Anti-patterns formalisés | ⚠️ Dans les .md, non queryables |
| Règles de composition | ❌ Absent |
| Vocabulaire/glossaire accessible | ❌ Absent ici (existe dans `ouds-ios/AGENTS.md`) |

**Score global : niveau 1-2 sur l'axe agentique.** Le repo a fait des choix de format délibérément orientés IA, mais l'exécution s'arrête à la structure sans remplir le contenu.

---

## Le paradoxe hub

`ouds-documentation` est le repo le plus stratégique de l'écosystème OUDS pour l'IA — c'est la seule source de vérité partagée entre toutes les plateformes. Mais l'investissement AI readiness s'est fait dans `ouds-ios` (AGENTS.md de 739 lignes, copilot-instructions.md de 150 lignes), pas ici.

Résultat : chaque repo plateforme re-documente le même vocabulaire (raw/semantic/component tokens, thèmes, tokenator), les mêmes intentions de tokens, les mêmes règles de composition — avec un risque de divergence croissante. `ouds-documentation` devrait être le hub de cette connaissance partagée, encodée en format machine une fois pour toutes et consommée par les agents de tous les repos plateforme.

---

## Ce que le [protocole-arc](../concepts/protocole-arc.md) implique

**Phase 1 (Audit — l'agent consomme) :** partiellement accessible. Un agent peut lire les 64 fichiers JSON de tokens. Mais faute de descriptions, il ne peut pas raisonner sur l'intent — seulement sur les valeurs. Les benchmarks de Morales Achiardi montrent 26,5 % de variance sans infrastructure d'intent, contre 0,04 % avec.

**Phase 2 (Report — l'agent analyse) :** inaccessible. Détecter des incohérences ou de la dérive exige de savoir ce que chaque token *devrait* faire. Sans descriptions remplies, l'agent ne peut pas distinguer un usage conforme d'un abus.

**Phase 3 (Compose — l'agent maintient) :** hors de portée.

---

## Recommandations prioritaires

Ordonnées par rapport impact/effort.

**1. Remplir les champs `description` des tokens JSON — effort : faible-moyen, impact : immédiat et élevé**

C'est l'action avec le meilleur ratio du repo. La structure est prête, le pipeline est en place, le schéma est bon. Il manque uniquement le contenu. Pour chaque token, la description doit répondre à : quand utiliser ce token, ce qui le distingue des tokens adjacents, quel contexte il cible. Exemple concret :

`ouds.color.action.negative.enabled` → `"Couleur d'action pour les états interactifs d'éléments destructifs (suppression, retrait, action irréversible). À utiliser exclusivement pour les actions qui entraînent une perte de données ou une modification permanente. Distinct de color.action.enabled (actions neutres) et de color.status.negative (états d'erreur passifs)."`

Cette génération est parfaitement assistable par IA sur la base des noms de tokens, de la documentation `button.md` existante, et du contexte OUDS. Une session de travail couvre l'intégralité d'une catégorie.

**2. AGENTS.md à la racine — effort : faible, impact : immédiat**

Un fichier de contexte couvrant : vocabulaire OUDS (raw/semantic/component tokens, tokenator, thèmes), structure du repo et comment le lire, convention des marqueurs `👈🤖`/`👈🤔`, liens vers les repos plateforme. La base existe dans `ouds-ios/AGENTS.md` — extraire, généraliser, centraliser. Ce fichier est le point d'entrée pour tout agent, quel que soit le modèle ou l'outil.

**3. Mapping composant → tokens — effort : moyen, impact : élevé**

Ajouter à chaque fichier composant `.md` (ou dans un fichier JSON compagnon) la liste des tokens qu'il utilise par état et variante. Exemple pour Button : `Strong.enabled → ouds.color.action.enabled`, `Negative.enabled → ouds.color.action.negative.enabled`. Ce mapping ferme le gap entre la couche tokens et la couche composants — actuellement deux silos sans pont.

**4. Métadonnées JSON par composant — effort : moyen-élevé, impact : élevé**

Générer des fichiers `.metadata.json` co-localisés avec chaque composant, couvrant les sections critiques du [schema-metadata-composant](../concepts/schema-metadata-composant.md) : `usage` (useCases, antiPatterns avec scénario/raison/alternative), `aiHints` (selectionCriteria par variante), `variants` (options + intent), `composition` (contraintes d'imbrication). Le contenu existe dans les `.md` — il s'agit de le traduire en format queryable. Le [processus-generation-metadata-echelle](../concepts/processus-generation-metadata-echelle.md) détaille les 5 étapes de cette génération assistée.

**5. Patterns de composition — effort : élevé, impact : moyen-terme**

Un répertoire `patterns/` documentant les assemblages validés : confirmation destructive, formulaire d'erreur, notification persistante. C'est la couche 3 du framework de [trois-couches-composants-agents](../concepts/trois-couches-composants-agents.md) — la logique de raisonnement qui permet à un agent de passer d'une liste d'ingrédients à une recette.
