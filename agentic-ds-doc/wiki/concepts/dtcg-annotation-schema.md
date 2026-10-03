---
type: concept
tags: [tokens, dtcg, schema, annotation, description, deprecated, extensions, primer, format, ia]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[design-system-documentation-spec](../sources/design-system-documentation-spec.md)"
related:
  - "[dsds-format](dsds-format.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[intent-token](intent-token.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[2026-06-22_description-field-design-token](../questions/2026-06-22_description-field-design-token.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
---

## Le schéma d'annotation DTCG

Le DTCG (Design Token Community Group) définit un format JSON standardisé pour les tokens, incluant plusieurs champs qui sont déjà dans la spec mais quasi-universellement laissés vides : `$description` et `$deprecated`. À ces champs standards, le pattern `$extensions` permet d'ajouter une couche de métadonnées spécifique à l'organisation — sans casser la compatibilité avec les outils existants.

[romina-kavcic](../entities/romina-kavcic.md) propose dans son audit de 50 systèmes ([50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)) un template opérationnel qui combine ces trois éléments. C'est le format le plus complet documenté dans le corpus, fondé sur l'exemple de GitHub Primer — le seul des 50 systèmes à avoir une règle explicite de non-usage dans le fichier.

## L'exemple Primer

```json
muted: {
  $value: '{base.color.neutral.9}',
  $type: 'color',
  $description: 'Muted text for secondary content and less important information',
  $extensions: {
    'org.primer.llm': {
      usage: ['muted-text', 'secondary-text', 'helper-text', 'placeholder'],
      rules: 'Use for secondary text like timestamps, metadata, and helper text. Do NOT use for primary content.',
    },
  },
},
```

Le namespace `org.primer.llm` est explicitement nommé pour les LLMs — signal que l'équipe a conçu ce champ pour des consommateurs agents, pas pour le build pipeline.

## Le template complet

```json
{
  "red600": {
    "$value": "#d62b1f",
    "$type": "color",
    "$description": "System danger. Destructive action backgrounds, error text, error borders.",
    "$deprecated": false,
    "$extensions": {
      "com.yourcompany.usage": {
        "role": "danger",
        "use": ["destructive-buttons", "error-text", "error-borders"],
        "doNotUse": "Decorative elements, charts, brand moments. Use crimson500 for brand.",
        "components": ["Button[variant=danger]", "Alert[type=error]", "Input[invalid]"],
        "decision": "ADR-014"
      }
    }
  }
}
```

Ce template couvre les 7 questions qu'un agent a besoin ([readable-vs-usable-token](readable-vs-usable-token.md)) :

- **Que signifie ce token ?** → `$description`
- **Quand l'utiliser ?** → `use[]`
- **Quand ne pas l'utiliser ?** → `doNotUse`
- **Est-il déprécié ?** → `$deprecated`
- **Quel composant en dépend ?** → `components[]`
- **Quelle décision l'a créé ?** → `decision` (lien vers ADR)
- **Quelle plateforme ?** → implicite dans la structure du repo ou ajoutée comme champ supplémentaire

## Deux propriétés critiques

**Compatibilité ascendante.** `$description` et `$deprecated` sont dans la spec DTCG — pas des inventions. Le build pipeline ignore `$extensions` par définition. Adopter ce schéma ne casse rien dans l'infrastructure existante. Il n'y a pas de migration : c'est une annotation sur ce qui existe déjà.

**Coût minimal, impact maximal.** L'expérience de Kavcic montre que la différence entre "deviner" et "savoir" pour un agent est exactement un champ `$description` par token. Pas une refonte du système. Pas un changement de format. Un champ par token, dans l'ordre de priorité des tokens les plus à risque de confusion.

## Stratégie de démarrage recommandée

Ne pas annoter tout le système d'un coup. Commencer par les 10 tokens à haut risque de mauvaise lecture — ceux où la confusion entre deux tokens similaires a un impact visible :

- Couleur d'action primaire
- Couleur de danger
- État désactivé
- Focus ring
- Espacement de formulaire
- Surface de carte
- Border radius
- Élévation
- Texte body
- Background de page

Pour chacun : `$description` (rôle + contexte exclusif), `doNotUse` (anti-pattern + token alternatif), `components[]` (composants qui l'utilisent). C'est l'effort le plus petit pour la valeur la plus immédiate.

## Lien avec la question archivée

Le contenu de `$description` est formalisé dans [2026-06-22_description-field-design-token](../questions/2026-06-22_description-field-design-token.md) : prose compacte, 2-4 phrases, structure rôle / contexte exclusif / distinctions critiques / anti-pattern. Le template DTCG fournit le conteneur ; la question archivée fournit ce qu'on y met.

## DSDS comme couche complémentaire au DTCG

[pj-onori](../entities/pj-onori.md) formalise en juin 2026 la complémentarité DTCG/DSDS dans la Design System Documentation Spec ([design-system-documentation-spec](../sources/design-system-documentation-spec.md)) : "DSDS documents the *how and why* of your design system — not the token values themselves. It complements the W3C Design Tokens Format which handles the *what*." Le duo couvre ainsi l'ensemble de la connaissance d'un design system : le fichier DTCG contient les valeurs (`$value`), DSDS contient la documentation structurée de leur usage.

Dans ce cadre, le template d'annotation DTCG de Kavcic ($description + $extensions) et les entités DSDS de type `token` / `token-group` sont deux niveaux complémentaires, non redondants. Le schéma DTCG annoté enrichit le fichier de tokens au niveau de la valeur — là où les outils de build le lisent. DSDS structure la documentation à un niveau plus haut — là où les agents et les humains lisent le *pourquoi*. Un design system peut maintenir les deux en parallèle sans conflit : DTCG annoté pour les pipelines et la consommation de valeurs, DSDS pour la documentation structurée et la gouvernance agentique. Voir [dsds-format](dsds-format.md) pour l'architecture complète.
