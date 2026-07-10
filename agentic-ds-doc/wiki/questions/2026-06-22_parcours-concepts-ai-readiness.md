---
type: question
tags: [ai-readiness, parcours, apprentissage, design-system, ia, concepts, ordre]
created: 2026-06-22
updated: 2026-06-22
sources: []
related:
  - "[[inversion-economique-code-comprehension]]"
  - "[[lisibilite-machine-design-system]]"
  - "[[readable-vs-usable-token]]"
  - "[[trois-couches-composants-agents]]"
  - "[[intent-token]]"
  - "[[delegation-lens]]"
  - "[[priori-conflictuels-nommage]]"
  - "[[dtcg-annotation-schema]]"
  - "[[schema-metadata-composant]]"
  - "[[existence-vs-intent-violations]]"
  - "[[protocole-arc]]"
  - "[[modele-maturite-ia-design-system]]"
  - "[[seeds-vs-trees]]"
  - "[[knowledge-graph-design-system]]"
---

# Parcours de concepts pour comprendre l'AI readiness

**Question posée** : Pour expliquer les principes et les enjeux de l'"AI readiness", quels sont les concepts à étudier et dans quel ordre ?

---

## Pourquoi l'ordre compte

Les concepts de l'AI readiness ne sont pas indépendants. Chacun présuppose le précédent. Comprendre [[dtcg-annotation-schema]] sans avoir compris [[readable-vs-usable-token]] donne un template sans le problème qu'il résout. Comprendre [[protocole-arc]] sans [[trois-couches-composants-agents]] donne un cadre de maturité sans les étapes concrètes. Le parcours ci-dessous est ordonné de façon à ce que chaque concept s'appuie sur un sol déjà posé.

---

## Niveau 1 — Le pourquoi (fondements économiques et paradigmatiques)

### 1. [[inversion-economique-code-comprehension]]
Le point de départ obligatoire. En 2025, 41 % du code est généré par IA. Le coût dominant du développement ne sont plus les lignes de code — c'est la compréhension : quoi faire, pourquoi, dans quel contexte. C'est ce retournement qui rend l'AI readiness non-optionnelle. Sans ce cadre, les recommandations pratiques semblent arbitraires.

### 2. [[seeds-vs-trees]]
La posture stratégique qui découle du premier concept. Deux modes d'adoption de l'IA : planter les graines (construire les fondations, puis laisser l'automatisation pousser dessus) ou acheter les arbres (déployer des agents sans fondations, amplifier le bruit à grande échelle). La formule : "Without structure, AI amplifies noise at scale. With structure, it amplifies understanding." C'est le cadre de décision pour tout ce qui suit.

---

## Niveau 2 — Ce que "lisible" veut dire

### 3. [[lisibilite-machine-design-system]]
Définition de la propriété centrale : un design system est "machine-readable" quand un agent peut l'utiliser de manière autonome sans interprétation humaine intermédiaire. Ce concept introduit aussi la preuve empirique (2x plus rapide, 54 % plus précis, 0 faux négatif avec infrastructure vs sans) et le benchmark de format (JSON bat Markdown 5:1 en coût pour les métadonnées).

### 4. [[readable-vs-usable-token]]
Raffinement critique du concept précédent, introduit par l'audit de 50 fichiers de tokens. Machine-readable (le build pipeline compile) ≠ agent-usable (l'agent peut raisonner sur le bon token). Sur 50 systèmes publics : 1 seul a une règle de non-usage dans le fichier. C'est la distinction qui précise de quoi on parle vraiment quand on dit "AI ready" — et révèle que la quasi-totalité des design systems n'a résolu que la moitié du problème.

---

## Niveau 3 — La structure de la solution (couches et tokens)

### 5. [[trois-couches-composants-agents]]
Le framework d'implémentation. Trois couches d'information qu'un design system doit exposer : la couche 1 (index — qu'est-ce qui existe), la couche 2 (métadonnées — comment et pourquoi l'utiliser), la couche 3 (raisonnement — quelle logique de composition). La majorité des systèmes a la couche 1, peu ont la couche 2, presque aucun la couche 3. Tout l'enjeu de l'AI readiness est de monter ces couches.

### 6. [[intent-token]]
L'application du même raisonnement à la couche tokens. Un token sémantique encode une signification indépendante de sa valeur brute : `color.bg.danger` dit plus qu'une valeur hex. Ce concept couvre également la preuve contrôlée (expérience crimson vs red600 : 2/3 erreurs sans annotation, 0/2 avec) et l'état du terrain en 2026.

### 7. [[delegation-lens]]
Outil de diagnostic pour évaluer une échelle de tokens. Chaque token que tu peux nommer et dont tu peux écrire une règle est une décision pre-made. Chaque token sans règle articulée est une décision ouverte — que quelqu'un prendra mal. Le count d'une échelle ne dit pas "le système est bon ou mauvais" — il dit combien de décisions restent ouvertes pour le consommateur (humain ou agent).

---

## Niveau 4 — Les obstacles spécifiques aux agents

### 8. [[priori-conflictuels-nommage]]
Un mécanisme contre-intuitif : les agents ne génèrent pas de noms de tokens par ignorance, mais à partir de 10 conventions contradictoires présentes dans leurs données d'entraînement. Le résultat est un nom plausible mais qui ne correspond à aucune convention maison. Le correctif coûte une ligne : déclarer sa grammaire là où l'agent la lira.

### 9. [[existence-vs-intent-violations]]
La distinction entre deux niveaux d'audit. Une violation d'existence : un token référencé dans le code n'existe pas. Une violation d'intent : le token existe mais son usage viole la logique du système (`--foreground-muted` pour du body copy). Un linter détecte les premières. La gouvernance réelle détecte les secondes — ce qui requiert que l'intent soit encodé dans le fichier. C'est la formalisation de pourquoi l'annotation n'est pas optionnelle pour la gouvernance.

---

## Niveau 5 — Les formats concrets

### 10. [[schema-metadata-composant]]
Le schéma à 9 sections pour rendre un composant queryable par un agent : `usage` (cas d'usage, anti-patterns avec scénario/raison/alternative), `aiHints` (critères de sélection), `variants` (options et intent), `composition`, `behavior`, `props`, `accessibility`, `examples`, et le `component` header. La structure qui force la précision là où la prose permet l'imprécision.

### 11. [[dtcg-annotation-schema]]
L'équivalent pour les tokens. Le template DTCG opérationnel avec `$description` (rôle + contexte exclusif), `$deprecated`, et `$extensions` (usage, doNotUse, components, decision). GitHub Primer est le seul des 50 systèmes audités à avoir implémenté ce niveau. Compatible avec les outils existants — c'est une annotation, pas une migration.

---

## Niveau 6 — La gouvernance et la maturité

### 12. [[protocole-arc]]
Le cadre de maturité en trois phases : Audit (l'agent consomme le design system avec précision), Report (l'agent analyse les patterns et détecte la dette), Compose (l'agent génère les correctifs sans intervention manuelle). Chaque phase requiert les couches correspondantes. C'est la trajectoire qui organise le travail dans le temps.

### 13. [[modele-maturite-ia-design-system]]
La taxonomie complémentaire — côté features IA pour utilisateurs humains (pas côté infrastructure agentique). 5 niveaux de 0 (aucune couche IA) à 5 (IA comme infrastructure du système). Utile pour situer un design system dans deux axes distincts : maturité de l'infrastructure agentique (ARC) et maturité de la documentation des features IA (ce modèle).

---

## Niveau 7 — L'architecture avancée (pour aller plus loin)

### 14. [[knowledge-graph-design-system]]
La couche 1 dans sa forme la plus avancée : non plus une liste de composants mais un graphe de relations navigable, auto-généré, queryable. C'est ce qui permet à un agent de raisonner sur l'ensemble du système plutôt que sur des composants isolés.

### 15. [[concevoir-les-conditions]]
La généralisation philosophique : designer les règles plutôt que les interfaces. Un design system AI-ready n'est pas un catalogue de composants — c'est un ensemble de contraintes exécutables qui rendent les mauvaises décisions impossibles ou détectables. L'AI readiness est une forme de governance-by-design.

---

## Lecture transversale recommandée

Après ce parcours linéaire, deux synthèses offrent une vue croisée :

[[deux-lectures-du-design-system-ia]] démêle deux questions souvent confondues : "Comment l'IA opère le design system ?" (infrastructure agentique) vs "Comment le design system documente les features IA pour les utilisateurs ?" (documentation UX). Les confondre produit des chantiers mal ciblés.

[[lisibilite-machine-design-system]] peut être relu en dernier comme synthèse : la distinction readable-for-pipelines vs readable-for-agents qu'on vient de parcourir y est maintenant pleinement formalisée, avec la preuve empirique et les benchmarks de format.

---

## Ce que ce parcours ne couvre pas encore

L'implémentation concrète bout-en-bout reste un gap : comment connecter les fichiers DTCG annotés à un MCP, comment générer les métadonnées de composants à grande échelle, comment automatiser l'audit de violations d'intent. Ces questions sont partiellement couvertes par [[processus-generation-metadata-echelle]] et [[workflows-ia-metadata]], mais l'intégration complète n'est pas encore archivée dans le vault.
