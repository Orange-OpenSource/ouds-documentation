---
source_url: https://www.designsystemscollective.com/building-language-for-design-systems-1b2f260b0bdf
author: Cristian Morales Achiardi
published: juillet 2026
ingested: 2026-07-09
---

# Building language for design systems

Source brute — contenu reconstitué depuis snippets indexés (page client-rendered).

## Thèse principale

Design systems establish and maintain language through vocabulary, grammar, and enforced contracts. Choosing a framework means inheriting a language: its vocabulary (terms, prop names, token names) and its grammar (rules for how components compose, how state flows, what is idiomatic). When vocabulary and grammar are shared across design and code, the design system becomes a language both sides compose against.

## Concepts clés

**Vocabulary** : the nouns, and grammar the composition rules — the whole language. A design token is authored vocabulary at the value level: a team writes it, decides what it means, spells it one way, and points both design and code at a single source of truth. The field standardized the vocabulary's format through the W3C Design Tokens Community Group specification (DTCG tokens), which defines how tokens are named, typed, and structured.

**Grammar** : the composition rules — how components compose, how state flows, what's idiomatic and what fights the grain. When you choose a framework you inherit its language, vocabulary, and grammar.

**Contract** : the shared look-up table both design and code compose against, defining which props exist and which values each accepts. One term per meaning at both levels, named by intent. "A vocabulary you can audit is a contract."

**Machine-readable enforcement** : a designer can ask which props and values the vocabulary accepts and have the prop table generated into the design tool on demand because the contract was written in a form a machine can read and carry. Machines enforce vocabulary across surfaces consistently; humans enforce it inconsistently.

**Naming conventions as grammar** : different casing styles (camelCase, kebab-case, PascalCase) carry meaning — they tell you what kind of thing you're looking at. Naming by intent vs naming by appearance.

## Citations clés

- "When you choose a framework you inherit language, its vocabulary and its grammar: the rules for how terms are formed, how components compose, how state flows."
- "A vocabulary you can audit is a contract."
- "Machines are how you easily enforce vocabulary across surfaces."
- "One term per meaning at both levels, named by intent."

## Connexions identifiées

- [[protocole-arc]] Phase 3 Compose : le "langage" est la fondation conceptuelle de la phase compose — pour que l'IA compose correctement, la grammaire doit être déclarée et machine-lisible.
- [[grammaire-composition-composants]] : la grammaire de composition chez Bondar + le vocabulaire de tokens ici forment deux niveaux du même langage.
- [[priori-conflictuels-nommage]] : la déclaration explicite de la grammaire de nommage comme correctif aux priors contradictoires des LLMs.
- [[intent-token]] : token comme "authored vocabulary at value level" — convergence directe.
- [[dtcg-annotation-schema]] : W3C DTCG comme standard du vocabulaire.
- [[composant-comme-contrat]] : le composant comme contrat, le vocabulaire comme audit.
- [[lisibilite-machine-design-system]] : enforcement machine-readable comme couche de lisibilité.
