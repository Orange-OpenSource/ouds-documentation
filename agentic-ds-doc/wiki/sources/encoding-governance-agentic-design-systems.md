---
type: source
tags: [design-system, gouvernance, ia, tokens, auditeur, contraintes, intent]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[[existence-vs-intent-violations]]"
  - "[[concevoir-les-conditions]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[intent-token]]"
  - "[[cristian-morales-achiardi]]"
---

## Encoding governance on agentic design systems

**Auteur** : [[cristian-morales-achiardi]]
**Publication** : Design Systems Collective (Medium), 20 février 2026
**URL** : https://www.designsystemscollective.com/encoding-governance-on-agentic-design-systems-1a8c70420fec
**Série** : "Agentic Design System" de Cristian Morales Achiardi, partie 6
**Fichier brut** : `raw/Encoding governance on agentic design systems.md`

---

## Résumé structuré

Article conclusif de la série — le passage de l'orchestration à la gouvernance. L'auteur documente le déploiement en production du système Enara et l'évolution d'un token auditor de v1 (vérification d'existence) à v2 (vérification d'intent). La distinction centrale : il ne suffit pas qu'un token existe — encore faut-il qu'il soit la bonne décision dans son contexte. v1 est un linter. v2 est de la gouvernance.

L'article pose également une question de fond sur le rôle du designer : quand la connaissance design est encodée dans des contraintes exécutables plutôt que dans une personne, le designer cesse d'être le garant implicite de chaque décision et devient l'auteur des conditions sous lesquelles les décisions correctes se prennent d'elles-mêmes.

---

## Thèses principales

**Thèse 1 — Existence vs intent.** Un token peut exister et être néanmoins le mauvais choix. Utiliser `--foreground-muted` pour du body copy n'est pas une référence manquante — c'est la mauvaise position dans la hiérarchie visuelle. Une ombre `rgba` personnalisée dans un dropdown n'est pas une erreur de syntaxe — c'est le contournement d'une décision de design. v1 trouve 43 violations (existence). v2 trouve 64 violations (existence + intent). Les 21 violations supplémentaires ne sont pas une régression : l'auditeur est devenu plus intelligent.

**Thèse 2 — Gouvernance vs orchestration.** Distinction explicite : l'orchestration concerne la *capacité* (faire fonctionner l'IA dans le système). La gouvernance concerne la *confiance* (garantir que ce qui est construit est ce qui a été conçu, sans vérification manuelle). Ce sont deux problèmes différents qui requièrent deux couches différentes.

**Thèse 3 — Concevoir les conditions, pas l'interface.** La gouvernance encodée représente un changement de niveau d'abstraction pour le designer. On ne conçoit plus l'interface — on conçoit les conditions sous lesquelles les interfaces sont construites correctement. L'objectif n'est pas de détecter les violations mais de rendre les violations le chemin le plus difficile.

**Thèse 4 — Le défi épistémique.** La partie la plus difficile de la gouvernance n'est pas technique — c'est épistémique. Il faut articuler des règles qu'on appliquait inconsciemment. La construction de l'auditeur de tokens a forcé l'auteur à écrire explicitement ce que "correct" signifie, pas comme documentation mais comme connaissance exécutable.

**Thèse 5 — Du designer qui livre au designer qui garantit.** Quand le design possède l'infrastructure qui applique ses propres décisions, la question cesse d'être "comment obtenir plus de QA design ?" pour devenir "le design a déjà résolu la qualité." Changement de rôle documenté en production chez Enara.

---

## Données concrètes

Système Enara : construit sur un weekend (après 3 mois d'approche classique ratée avec Tamagui). Tokens W3C via Style Dictionary, platform-agnostic. v1 de l'auditeur : 43 violations détectées. v2 : 64 violations (21 de plus = intent violations invisibles à v1). FilterBar : 0 violation (composant le plus récent, construit après l'infrastructure établie).

---

## Citations clés

> "v1 checked existence. v2 checks intent. The difference between those two things is the difference between a linter and governance."

> "The goal isn't to catch violations. It's to make violations the harder path."

> "You're not designing the interface. You're designing the conditions under which interfaces get built correctly."

> "Orchestration is about capability. Governance is about trust."

> "From designer who delivers to designer who guarantees."

---

## Connexions identifiées

[[existence-vs-intent-violations]] est la contribution conceptuelle centrale de cet article. [[concevoir-les-conditions]] capture le changement de niveau d'abstraction du rôle designer. Enrichit directement [[gouvernance-design-system-ia]] (token auditor, executable constraints), [[user-vs-maintainer-ia]] (le designer comme garant), [[intent-token]] (intent violations distinctes des existence violations). La notion de "self-healing not autonomous" nuance [[protocole-arc]] Phase 3.
