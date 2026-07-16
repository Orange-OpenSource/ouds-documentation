---
type: concept
tags: [tokens, ia, agent-ready, readable, usable, pipeline, contexte, description]
created: 2026-06-22
updated: 2026-06-22
sources:
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)"
related:
  - "[derive-design-system-ia](derive-design-system-ia.md)"
  - "[intent-token](intent-token.md)"
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[dtcg-annotation-schema](dtcg-annotation-schema.md)"
  - "[delegation-lens](delegation-lens.md)"
  - "[priori-conflictuels-nommage](priori-conflictuels-nommage.md)"
  - "[romina-kavcic](../entities/romina-kavcic.md)"
---

## Readable ≠ Usable

La distinction centrale introduite par [romina-kavcic](../entities/romina-kavcic.md) dans son audit de 50 fichiers de tokens ([50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)) : un fichier de tokens peut être parfaitement **machine-readable** — il compile, le build pipeline tourne, les valeurs sont extraites correctement — et rester **agent-unusable** — l'agent qui le lit ne peut pas raisonner sur quel token choisir dans quel contexte.

Ces deux états ne sont pas synonymes parce qu'ils répondent à des questions différentes. Un build pipeline pose : "quelle est la valeur de ce token ?" Un agent pose : "quel token dois-je utiliser pour ce cas d'usage ?" La réponse à la première question est dans le fichier. La réponse à la seconde, pour la majorité des 50 systèmes audités, ne l'est pas.

[derive-design-system-ia](derive-design-system-ia.md) documente la conséquence comportementale directe de cette absence : privé de la réponse à "quel token utiliser", l'agent ne s'arrête pas — il fabrique un nom de token plausible. La fabrication de tokens est donc moins un bug isolé qu'une réponse prévisible à un fichier readable-mais-pas-usable.

## Les 7 questions qu'un agent a besoin

[romina-kavcic](../entities/romina-kavcic.md) liste ce qu'un fichier de tokens doit répondre pour être agent-ready :

1. Que signifie ce token ?
2. Quand doit-il être utilisé ?
3. Quand ne doit-il **pas** être utilisé ?
4. Est-il déprécié ?
5. Quel composant ou quel état en dépend ?
6. Quelle décision l'a créé ?
7. Quelle plateforme cible-t-il ?

Sans ces réponses dans le fichier, l'agent peut lire les valeurs. Il doit deviner le reste.

## L'expérience qui le prouve

Kavcic a construit un fichier fictif de 10 couleurs avec un piège réel : deux rouges. `crimson500` est l'accent brand. `red600` est la couleur de danger système. Rien dans le fichier nu ne dit lequel est lequel.

**Fichier sans description (3 runs)** : 2 runs placent le crimson brand sur le bouton destructif "Delete account". Aucun run ne produit la même réponse complète.

**Fichier avec un champ `$description` DTCG par token (2 runs)** : réponses identiques, correctes. Le raisonnement de l'agent cite la description : *"red600 is explicitly designated for destructive actions."*

La différence entre deviner et savoir est un seul champ par token. Ce n'est pas une question de modèle, de prompt ou d'architecture — c'est une question de données disponibles dans le fichier. Voir [dtcg-annotation-schema](dtcg-annotation-schema.md) pour le template concret.

## Ce que ça révèle sur l'état du terrain

Sur 50 systèmes publics audités :

- Descriptions dans le fichier : ~15/50
- Champ de dépréciation lisible par machine : ~10/50
- Règle explicite de non-usage : **1/50** — GitHub Primer

La majorité des fichiers ressemble à :

```json
{
  "gray11": { "$value": "#646464", "$type": "color" }
}
```

Le nom *laisse entendre* un intent. Le fichier garde le silence sur le rôle, l'usage, ce qu'il faut éviter. L'agent obtient une valeur et infère le reste — avec toute la variance que l'inférence implique ([priori-conflictuels-nommage](priori-conflictuels-nommage.md)).

## Le lien avec la gouvernance des violations

La distinction readable/usable recoupe directement [existence-vs-intent-violations](existence-vs-intent-violations.md). Un fichier readable sans descriptions permet uniquement l'audit v1 (vérifier que les tokens référencés existent). Pour détecter les violations d'intent — un token utilisé dans un contexte sémantiquement incorrect — l'auditeur a besoin que le fichier dise ce que chaque token *devrait* faire. Sans la couche usable, la gouvernance reste au niveau linter, jamais au niveau sémantique.

## Confirmation empirique sur les icônes (Miro)

[eddie-machado](../entities/eddie-machado.md) chez Miro documente le même problème étendu aux icônes, avec un cas concret de production ([miro-ai-design-system-mcp-claude-code-skills](../sources/miro-ai-design-system-mcp-claude-code-skills.md)). Une icône visuellement représentant "two A's, one capital, one cursive" était nommée dans la librairie comme si elle servait les "text styles" alors qu'elle sert les "font styles" (serif, sans-serif). L'icône pour les text styles réels est nommée d'après sa forme visuelle. Résultat : Aura était "confidently wrong" — elle construisait des toolbars avec les mauvaises icônes, avec confiance.

Ce cas étend la distinction readable/usable au-delà des tokens DTCG vers les assets visuels. Une icône dans une librairie Figma est machine-readable (elle a un nom, un identifiant, une catégorie). Elle n'est pas agent-usable si son nom n'explicite pas sa fonction, si aucun champ ne dit "do not use for X, use Y instead."

La réponse de Miro : trois champs de métadonnées par icône (description visuelle, cas d'usage, catégorie) + règle de non-usage explicite. Après ajout : les mêmes prompts produisent des sorties correctes. Voir [schema-metadata-composant](schema-metadata-composant.md) pour le schéma complet.

Ce cas confirme que la distinction readable/usable n'est pas limitée aux fichiers de tokens — elle s'applique à tout asset du design system (composants, icônes, tokens) dont l'usage correct dépend d'une logique non encodée dans le nom ou la valeur brute.

## ⚡ Tension avec la notion de "machine-readable"

Le terme "machine-readable design system" tel qu'utilisé dans [lisibilite-machine-design-system](lisibilite-machine-design-system.md) désignait jusqu'à présent la propriété d'être compréhensible par un agent IA. Cette source affine : **readable-for-pipelines** et **readable-for-agents** sont deux propriétés distinctes. Un système peut être 100 % machine-readable au sens build (Style Dictionary, DTCG) et 0 % agent-usable au sens raisonnement. La notion de lisibilité machine doit donc être précisée selon l'audience : pipeline ou agent.
