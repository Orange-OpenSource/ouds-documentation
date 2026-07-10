---
type: question
tags: [tokens, description, format, ia, machine-readable, intent, ouds]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[[intent-token]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[existence-vs-intent-violations]]"
  - "[[schema-metadata-composant]]"
  - "[[2026-06-19_audit-ai-readiness-ouds-documentation]]"
---

# Que doit contenir le champ "description" d'un design token ?

**Question posée** : que doit contenir le champ `description` d'un design token pour un usage LLM ? Quel format ? Quel niveau de détail ?

---

## Ce que le champ doit faire

Un token sémantique porte déjà 80 % de l'information dans son nom. `ouds.color.action.negative.enabled` dit : couleur, action, valence négative, état actif. La description doit couvrir les 20 % restants que le nom seul ne peut pas encoder ([[intent-token]]) :

- le **contexte exclusif d'usage** — dans quelles situations précises ce token s'applique
- la **distinction par rapport aux tokens adjacents** — ce qui le différencie de tokens proches en valeur ou en nom
- les **anti-patterns critiques** — ce qu'il ne faut pas faire et quel token utiliser à la place

Sans ces trois éléments, la description est décorative. Un agent qui la lit doit pouvoir décider si ce token est le bon pour une situation donnée — sans voir aucune autre documentation.

---

## Format : prose compacte dans une string JSON

Le champ `description` est une string JSON. Pas de sous-objets, pas de listes, pas de Markdown. La règle de [[diana-wolosin]] — "JSON for MCP, Markdown for LLM" — distingue les deux couches d'infrastructure mais ne prescrit pas du Markdown *à l'intérieur* du JSON. À l'intérieur d'une string, la prose brute compacte est plus économe en tokens et aussi lisible par le LLM qu'une liste à puces.

Le principe de [[lisibilite-machine-design-system]] s'applique : "JSON is like a contract — explicit keys, explicit values, no ambiguity." La description est un champ du contrat, pas une documentation narrative.

---

## Niveau de détail : 2 à 4 phrases

Le benchmark d'Indeed montre que JSON est 5× moins cher que Markdown *parce qu'il est compact et explicite*. Une description de 10 lignes qui recopie la documentation humaine annule cet avantage. La cible :

- **Phrase 1** — définition du rôle dans la hiérarchie visuelle
- **Phrase 2** — contexte exclusif d'usage (avec un marqueur de restriction : "Réservé à…", "Exclusivement pour…")
- **Phrase 3** — distinctions critiques avec les tokens adjacents (les deux ou trois tokens avec lesquels la confusion est la plus probable)
- **Phrase 4** (optionnelle) — anti-pattern le plus fréquent, avec token alternatif

Au-delà de 4 phrases, le signal se noie dans le bruit.

---

## Exemple concret (OUDS)

```json
"ouds.color.action.negative.enabled": {
  "description": "Couleur d'action pour les éléments interactifs destructifs à l'état actif. Réservé aux actions irréversibles : suppression, retrait permanent, modification sans annulation possible. Distinct de color.action.enabled (actions neutres) et de color.status.negative (états d'erreur passifs non-interactifs). Ne pas utiliser pour les messages d'erreur ou les états de validation — ce sont des statuts, pas des actions."
}
```

Ce n'est pas long — c'est dense. Chaque phrase répond à une question différente qu'un agent se pose au moment de choisir un token.

---

## La structure de l'anti-pattern

Le [[schema-metadata-composant]] formalise pour les composants ce que devrait encoder une description de token : chaque anti-pattern exige trois éléments — *scénario* (quoi ne pas faire), *raison* (pourquoi c'est un problème), *alternative* (quoi faire à la place). Dans une string de description, la formule compressée est : "Ne pas utiliser pour [X] — [X] est [raison] ; utiliser [[token-correct]] à la place." Cette structure force la précision que la prose libre permet d'éviter ([[schema-metadata-composant]]).

---

## Lien avec la gouvernance des violations

La distinction [[existence-vs-intent-violations]] montre pourquoi ce champ est non-négociable pour la gouvernance agentique. Un auditeur v1 vérifie l'existence d'un token. Un auditeur v2 vérifie son intent — s'il est utilisé dans le bon contexte. Pour qu'un agent puisse détecter une violation d'intent (utiliser `--foreground-muted` pour du body copy, utiliser `color.action.negative` pour un état d'erreur passif), il doit avoir accès à la définition du rôle légitime du token. Sans `description` remplie, l'auditeur reste à v1 — il ne peut que constater l'existence, pas l'usage correct.

---

## Gap documenté dans le vault

Aucune source ingérée ne propose un modèle de description par *catégorie* de token (couleurs d'action, couleurs de statut, élévation, espacement, typographie, border-radius). L'[[intent-token]] couvre le principe. Le [[schema-metadata-composant]] couvre les composants. Mais la déclinaison pratique par catégorie OUDS reste à construire. C'est le prochain niveau d'opérationnalisation de l'audit [[2026-06-19_audit-ai-readiness-ouds-documentation]].
