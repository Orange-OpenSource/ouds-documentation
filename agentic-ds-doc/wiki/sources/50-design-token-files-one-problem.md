---
type: source
tags: [tokens, design-system, ia, agent-ready, dtcg, nommage, format, audit, empirique]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[intent-token](../concepts/intent-token.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[readable-vs-usable-token](../concepts/readable-vs-usable-token.md)"
  - "[delegation-lens](../concepts/delegation-lens.md)"
  - "[priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md)"
  - "[dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md)"
  - "[existence-vs-intent-violations](../concepts/existence-vs-intent-violations.md)"
---

## Source

**Titre** : "50 design token files, one problem: your agents can't read the meaning"
**Auteur** : [romina-kavcic](../entities/romina-kavcic.md)
**Date** : 2026-06-19
**URL** : https://learn.thedesignsystem.guide/p/50-design-token-files-one-problem

---

## Thèse principale

Un fichier de tokens peut être parfaitement valide pour un build pipeline et rester informatiquement pauvre pour un agent IA. La distinction est entre **readable** (machine-readable, compile correctement) et **usable** (agent-usable, fournit le contexte pour raisonner). La majorité des 50 systèmes audités sont dans le premier état, pas le second.

---

## Thèses secondaires

**Aucun standard commun.** Ni format (8 formats en usage actif : DTCG JSON, Style Dictionary JSON, Theo YAML, JSON brut, TypeScript, CSS custom properties, SCSS, LESS), ni emplacement, ni taille, ni convention de nommage. Un agent qui apprend une convention ne sait rien sur la suivante.

**La taille est une décision de délégation.** Chaque token que tu peux nommer et dont tu peux écrire une règle d'usage est une décision pre-made. Chaque token sans règle est une décision ouverte — que quelqu'un, humain ou agent, prendra mal à un moment. Voir [delegation-lens](../concepts/delegation-lens.md).

**Les agents arrivent avec des priors conflictuels.** Toutes les conventions de nommage documentées dans les 50 systèmes font partie des données d'entraînement. Un agent ne génère pas un nom ignorant — il génère un nom *plausible qui mélange plusieurs grammaires*, ce qui est plus difficile à détecter. Voir [priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md).

**La couche de sens est la plus jeune.** Sur 50 systèmes : ~15 ont une description écrite dans le fichier, ~10 ont un champ de dépréciation lisible par machine, **1 seul a une règle explicite de non-usage** — GitHub Primer.

---

## Données empiriques

- Taille médiane d'une échelle de spacing : ~12 tokens (Mantine : 5, Open Props : 74)
- Taille médiane de typography : ~25 tokens (Backpack : 10, Adobe Spectrum : 312)
- Couche sémantique couleur : Nord 57 → Atlassian 391
- Material Design : 18 tokens d'espacement documentés sur le site, **0 dans le code livré**
- Signification dans le fichier : descriptions ~15/50, dépréciation ~10/50, règles de non-usage 1/50

---

## L'expérience crimson vs red600

Fichier fictif de 10 couleurs, deux rouges : `crimson500` (accent brand) et `red600` (danger système). Aucune description dans le fichier.

**Sans description** (3 runs) : 2 runs placent le crimson brand sur le bouton "Delete account". Aucun des 3 runs ne produit la même réponse complète.

**Avec description DTCG** (2 runs) : réponses identiques, correctes. Le raisonnement cite la description : *"red600 is explicitly designated for destructive actions."*

Un champ `$description` par token est la différence entre deviner et savoir.

---

## L'exemple Primer (best practice)

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

C'est une **valeur + un rôle + une règle de non-usage**. Le pattern complet.

---

## Citations clés

- "A token file can be perfectly valid for a build pipeline and still be thin context for an AI agent." (≤15 mots)
- "Readable is not the same as usable." (≤15 mots)
- "Every step past what you can name and explain is a choice somebody will eventually get wrong." (≤15 mots)
- "Your token file is not only a source of truth, but a memory layer for your agents." (≤15 mots)
- "The next phase of design tokens is not only transformation. It is labeling." (≤15 mots)

---

## Connexions identifiées

- Confirme et opérationnalise [intent-token](../concepts/intent-token.md) avec un benchmark empirique (50 systèmes + expérience contrôlée)
- Confirme [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) en distinguant readable (build pipeline) vs usable (agent reasoning)
- Complète [existence-vs-intent-violations](../concepts/existence-vs-intent-violations.md) : les fichiers sans description ne permettent que la v1 (existence), jamais la v2 (intent)
- Introduit [delegation-lens](../concepts/delegation-lens.md) comme cadre pour évaluer la taille d'une échelle de tokens
- Introduit [priori-conflictuels-nommage](../concepts/priori-conflictuels-nommage.md) comme explication du comportement de génération de noms par les agents
- Introduit [dtcg-annotation-schema](../concepts/dtcg-annotation-schema.md) comme template opérationnel concret
- S'aligne avec [2026-06-19_audit-ai-readiness-ouds-documentation](../questions/2026-06-19_audit-ai-readiness-ouds-documentation.md) : OUDS est exactement dans la case "readable, pas usable"
