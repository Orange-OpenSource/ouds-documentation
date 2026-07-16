---
type: concept
tags: [tokens, design-system, echelle, taille, delegation, decision, spacing, typography, couleur]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
related:
  - "[intent-token](intent-token.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[priori-conflictuels-nommage](priori-conflictuels-nommage.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
  - "[concevoir-les-conditions](concevoir-les-conditions.md)"
---

## Le prisme de la délégation

[romina-kavcic](../entities/romina-kavcic.md) introduit dans son audit de 50 systèmes ([50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)) un cadre de lecture pour interpréter la taille d'une échelle de tokens : **chaque token que tu peux nommer et dont tu peux écrire une règle d'usage représente une décision pre-made**. Chaque token sans règle articulée est une décision ouverte — que quelqu'un, humain ou agent, prendra mal à un moment.

Une **petite échelle** est une opinion. Elle impose des choix, réduit la surface d'erreur, et permet la cohérence presque par accident. Une **grande échelle** est une palette. Elle laisse les décisions ouvertes, maximise la flexibilité, et transfère la responsabilité du système vers le consommateur — humain ou agent.

Ni l'un ni l'autre n'est faux. Mais chaque position a des conséquences concrètes sur ce qu'un agent doit faire seul.

## Spacing : de 5 à 74 tokens

La médiane est ~12 steps, et la majorité des systèmes se situe entre 8 et 15. Deux extrêmes illustrent le prisme :

**Mantine : 5 tokens d'espacement.** Un agent qui choisit un espacement parmi 5 options sera cohérent presque par construction. La variance possible est faible. Le système a pré-décidé à la place du consommateur.

**Open Props : 74 tokens d'espacement.** Chaque gap, chaque padding, chaque margin est une décision ouverte. Face à 74 options non labelisées, un agent est un générateur de dérive. La formule de Kavcic : "Every step past what you can name and explain is a choice somebody will eventually get wrong."

La taille de l'échelle ne dit donc pas "le système est bon ou mauvais" — elle dit "voici combien de décisions le consommateur doit encore prendre". Pour un agent, le nombre de décisions ouvertes est directement proportionnel à la variance de l'output.

## Typography : presets vs atomes

La médiane est ~25 tokens. Mais la taille élevée peut signifier deux choses opposées :

**The Guardian : 100 tokens de typographie.** C'est un preset par combinaison valide de famille/grammage/style/taille, construits depuis seulement 12 tailles sous-jacentes. Le count élevé signifie que toutes les décisions sont déjà prises — il est presque impossible de composer une combinaison invalide. La taille protège.

**Adobe Spectrum : 312 tokens de typographie.** Séparation de chaque dimension (taille, grammage, hauteur de ligne, famille, script) avec des sets pour CJK et serif. La taille signifie ici que le consommateur compose encore : il choisit une taille, un grammage, une famille, et les assemble. La taille expose.

Même count, logique inverse. Le prisme révèle le sens : "la taille ne compte que quand on sait ce qu'elle délègue."

## Le cas Material Design

Le cas le plus instructif de l'audit : Material Design M3 définit 18 tokens d'espacement sur son site de documentation (`md.sys.spacing.0` à `md.sys.spacing.900`). Dans `material-web`, le code livré, le dossier de tokens contient des fichiers pour couleur, élévation, motion, shape, state, typescale — et **aucun fichier de spacing**. L'échelle existe sur papier. Dans le fichier qu'un agent charge, elle n'existe pas.

C'est l'argument de la source entière illustré dans un seul système : le sens vit dans la documentation, pas dans le fichier. Pour un agent, seul le fichier compte.

## Implications pour la gouvernance

Le prisme de la délégation est un outil de diagnostic avant de décider du niveau d'annotation nécessaire. Un système de 5 tokens d'espacement n'a pas besoin de descriptions détaillées — les choix sont si contraints que l'agent se trompe rarement. Un système de 74 tokens d'espacement non labelisés est une dette de gouvernance : chaque token sans règle explicite est un point de divergence potentielle.

La question pratique n'est pas "combien de tokens ai-je ?" mais "combien de ces tokens pourrais-je défendre à un agent avec une règle écrite ?" Le reste est surface d'erreur ouverte. Voir [concevoir-les-conditions](concevoir-les-conditions.md) pour la généralisation de ce principe.
