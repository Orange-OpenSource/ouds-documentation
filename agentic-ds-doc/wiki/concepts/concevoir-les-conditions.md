---
type: concept
tags: [design-system, gouvernance, ia, designer, abstraction, conditions, épistémique, accountability, environnement]
created: 2026-06-17
updated: 2026-07-07
sources:
  - "[[encoding-governance-agentic-design-systems]]"
  - "[[human-layer-agentic-design-systems]]"
related:
  - "[[existence-vs-intent-violations]]"
  - "[[gouvernance-design-system-ia]]"
  - "[[user-vs-maintainer-ia]]"
  - "[[design-system-as-infrastructure]]"
  - "[[seeds-vs-trees]]"
  - "[[designops-devops-seam]]"
  - "[[accountability-gap-ia]]"
---

## Concevoir les conditions

"Concevoir les conditions" désigne le changement de niveau d'abstraction dans le rôle du designer quand la gouvernance est encodée dans une infrastructure agentique. La formulation de [[cristian-morales-achiardi]] : "You're not designing the interface. You're designing the conditions under which interfaces get built correctly" ([[encoding-governance-agentic-design-systems]]).

## Le glissement d'abstraction

Un designer qui livre des maquettes conçoit l'interface — il prend des décisions de composition, de couleur, d'espacement, de hiérarchie pour chaque écran. Un designer qui conçoit les conditions prend les mêmes décisions, mais les encode de sorte qu'elles s'appliquent automatiquement à tous les écrans futurs, sans intervention manuelle. Ce n'est pas un abandon des décisions design — c'est leur généralisation.

L'exemple documenté chez Enara : l'auditeur de tokens ne vérifie pas que l'auteur a bien utilisé le bon token dans un composant donné. Il vérifie que la règle "utiliser `--foreground-primary` pour le body copy" tient dans chaque composant généré par n'importe quel développeur ou agent IA, maintenant et dans le futur ([[encoding-governance-agentic-design-systems]]).

## Le défi épistémique

Le point le plus difficile n'est pas technique. C'est épistémique : articuler des règles qu'on appliquait inconsciemment. Chaque décision de design système implicite — "ici on utilise toujours l'ombre de niveau 2 pour les dropdowns", "ici `--foreground-muted` est réservé aux éléments secondaires" — doit être rendue explicite pour être encodée. Le processus de construction de l'auditeur force cette articulation. Ce n'est pas de la documentation — c'est de la connaissance qui doit être exécutable.

Cette articulation est une forme de design à part entière. Avant, les règles vivaient dans la tête du designer et se transmettaient par osmose, revues de code, et conversations. Elles étaient donc fragiles, non scalables, et dépendantes d'une présence humaine. Encodées, elles deviennent un actif durable du système.

## Du designer garant implicite au système garant explicite

Tant que le designer est la seule source de vérité sur ce qui est "correct", chaque décision dépend de sa disponibilité et de sa mémoire. À l'échelle — quand dix développeurs construisent sur le système — cette dépendance crée un goulot d'étranglement et un point de dérive. [[cristian-morales-achiardi]] décrit ce moment précis chez Enara : "I was the system. Every decision passed through me [...] The moment someone else starts building components, that knowledge stays in you while the system keeps growing. This requires interpretation. And interpretation is where drift begins."

Quand les conditions sont conçues et encodées, le designer cesse d'être le garant implicite de chaque décision pour devenir l'auteur des règles que le système applique sans lui. Voir [[user-vs-maintainer-ia]] pour la dimension IA de cette transition.

## L'objectif de gouvernance

La conséquence pratique : "The goal isn't to catch violations. It's to make violations the harder path." Un système bien conçu rend les décisions correctes plus faciles à prendre que les décisions incorrectes. L'auditeur ne fait pas la gouvernance — il vérifie que l'environnement fait son travail. FilterBar, le composant le plus récent du système Enara au moment de l'article, avait zéro violation — non parce que l'auditeur l'avait corrigé, mais parce que l'environnement était suffisamment bien structuré pour que le chemin naturel soit le chemin correct ([[encoding-governance-agentic-design-systems]]).

## L'accountability comme conséquence de concevoir les conditions

[[human-layer-agentic-design-systems]] ajoute une dimension que l'article de gouvernance laissait implicite : concevoir les conditions, c'est aussi accepter d'être la source de vérité sur ce qui est correct — et donc d'être le terminal de l'accountability quand quelque chose se trompe.

L'incident de l'échelle de jaune primitif chez Enara en est la démonstration la plus directe. Une erreur dans les valeurs primitives — une mauvaise décision de design encodée dans la fondation — s'est propagée fidèlement dans tout le système. Le token auditor a confirmé que l'implémentation était correcte. L'erreur remontait donc à la couche primitive. Et la couche primitive remontait au designer. La chaîne de traçabilité a fonctionné précisément parce que les conditions étaient bien conçues : un système sans accountability encodée n'aurait produit qu'un constat flottant d'incohérence visuelle, sans propriétaire.

[[cristian-morales-achiardi]] formule le corollaire : "Most designers hand off decisions and hope. I encode decisions and know." Encoder les décisions, c'est pouvoir savoir — savoir quand elles sont correctes, savoir quand elles sont erronées, et savoir à qui appartient la correction. C'est un gain de connaissance autant qu'un gain d'efficacité.

## L'environnement comme niveau supérieur

La partie conclusive de la série marque une progression dans la formulation : de "concevoir les conditions sous lesquelles les interfaces se construisent correctement" vers "concevoir des environnements". [[cristian-morales-achiardi]] : "I'm not just a product designer anymore. I'm designing environments. The conditions and rules that enable correct execution at a speed I physically cannot match by reviewing every screen and every PR."

Le passage à "environnement" souligne que l'objectif n'est pas un ensemble de règles statiques, mais un milieu dans lequel les bonnes décisions deviennent le chemin naturel — et dans lequel les mauvaises décisions remontent vers leur source plutôt que de se diluer dans la codebase. La gouvernance n'est pas ce qui contraint le système ; c'est ce qui lui permet de fonctionner sans surveillance constante.
