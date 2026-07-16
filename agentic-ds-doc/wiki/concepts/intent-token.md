---
type: concept
tags: [tokens, design-system, intent, semantique, ia, gouvernance, violations]
created: 2026-06-17
updated: 2026-06-17
sources:
  - "[design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)"
  - "[encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)"
  - "[automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)"
  - "[50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)"
  - "[google-design-md-spec](../sources/google-design-md-spec.md)"
  - "[agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md)"
related:
  - "[lisibilite-machine-design-system](lisibilite-machine-design-system.md)"
  - "[trois-couches-composants-agents](trois-couches-composants-agents.md)"
  - "[composants-context-aware](composants-context-aware.md)"
  - "[inversion-economique-code-comprehension](inversion-economique-code-comprehension.md)"
  - "[existence-vs-intent-violations](existence-vs-intent-violations.md)"
  - "[gouvernance-design-system-ia](gouvernance-design-system-ia.md)"
  - "[readable-vs-usable-token](readable-vs-usable-token.md)"
  - "[dtcg-annotation-schema](dtcg-annotation-schema.md)"
  - "[priori-conflictuels-nommage](priori-conflictuels-nommage.md)"
  - "[delegation-lens](delegation-lens.md)"
  - "[design-md-format](design-md-format.md)"
updated: 2026-06-26
---

## Intent des tokens

L'intent d'un token désigne la signification sémantique portée par son nom, indépendamment de sa valeur brute. C'est la différence entre `color.bg.danger` et `color.bg.primary` : ils peuvent pointer vers des valeurs chromatiques différentes, mais surtout ils encodent des intentions d'usage incompatibles.

Quand un agent IA doit choisir le bon token pour un bouton dans un dialog de confirmation de suppression, il ne peut pas déduire ce choix à partir des valeurs hexadécimales seules. Il a besoin de l'intent : `color.bg.danger` signifie "action irréversible à risque", `color.bg.primary` signifie "action principale neutre". Cette information est dans le nom — mais encore faut-il que les conventions de nommage soient assez expressives pour la porter ([design-system-most-important-asset-ai-era](../sources/design-system-most-important-asset-ai-era.md)).

## Le token comme contrat sémantique

L'intent des tokens est la version tokenisée de la couche 2 des composants ([trois-couches-composants-agents](trois-couches-composants-agents.md)). De la même façon que la description d'un composant encode le quand et le pourquoi de son usage, le nom d'un token encode le contexte d'application et la signification de la valeur. Un token bien nommé est auto-documenté pour un agent.

Les conventions de nommage sémantique (par intent plutôt que par valeur) sont donc un investissement en lisibilité machine. `color.red-600` n'encode aucun intent. `color.bg.danger` encode le contexte (background), la catégorie (danger) et l'usage approprié. L'agent peut composer à partir du second ; pas du premier.

## Lien avec l'inversion économique

L'intent d'un token est exactement le type de compréhension que [inversion-economique-code-comprehension](inversion-economique-code-comprehension.md) identifie comme l'actif rare à l'ère de l'IA. La valeur `#DC2626` est libre. Savoir qu'elle doit s'appliquer sur fond de bouton destructif, et pas sur fond de bouton de navigation, est la compréhension qui coûte — et qui se capitalise dans les conventions de nommage.

## La synchronisation cross-platform comme problème de cohérence sémantique

Un problème distinct émerge dans les systèmes multi-plateformes : un token mis à jour dans Figma doit se propager de façon cohérente vers CSS, iOS et Android. Sans synchronisation, des incohérences subtiles s'accumulent — "une nuance de bleu décalée ici, une valeur d'espacement désalignée là" — qui érodent progressivement la confiance dans le système ([automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)). Cette dérive est une violation d'intent distribuée : le token a une valeur correcte à sa source mais une valeur incorrecte sur certaines plateformes cibles.

[mehmet-celik](../entities/mehmet-celik.md) documente l'évolution vers la détection prédictive : l'IA surveille les overrides récurrents et peut suggérer la création d'un nouveau token quand elle détecte que plusieurs équipes contournent systématiquement la même valeur. Cette couche dépasse la gouvernance réactive (détecter les mismatches) pour aller vers la gouvernance proactive (détecter le manque dans la taxonomie de tokens). Salesforce Lightning explore cette direction dans son Lightning Design System ([automating-design-system-ai-efficiency](../sources/automating-design-system-ai-efficiency.md)). Voir [systeme-design-proactif](systeme-design-proactif.md).

## Intent tokens et violations d'intent

La partie 6 de la série de [cristian-morales-achiardi](../entities/cristian-morales-achiardi.md) ([encoding-governance-agentic-design-systems](../sources/encoding-governance-agentic-design-systems.md)) affine la notion d'intent en introduisant deux classes de violations de tokens :

Une **violation d'existence** survient quand un token référencé dans le code (`var(--color-blue-500)`) n'existe pas dans le système. Le composant ne peut pas appliquer la valeur — le token est absent.

Une **violation d'intent** survient quand un token existe mais son usage viole la logique du système. Utiliser `--foreground-muted` pour du body copy ne crée pas d'erreur syntaxique — le token existe et sera appliqué. Mais `--foreground-muted` est conçu pour les éléments secondaires, pas pour le contenu principal. L'usage est sémantiquement incorrect : il viole l'intent encodé dans le nom même du token.

Cette distinction est importante parce qu'elle montre que la gouvernance des tokens ne se réduit pas à la gestion d'un dictionnaire valide. Elle requiert que le système sache non seulement quels tokens existent, mais quel rôle chacun joue dans la hiérarchie visuelle. Un auditeur v1 peut vérifier l'existence ; un auditeur v2 doit comprendre l'intent. La différence entre les deux est la différence entre un linter et de la gouvernance réelle. Voir [existence-vs-intent-violations](existence-vs-intent-violations.md) pour la formalisation complète et les exemples concrets (cas Enara).

## Validation empirique : l'expérience crimson vs red600

[romina-kavcic](../entities/romina-kavcic.md) apporte dans son audit de 50 systèmes ([50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md)) la preuve contrôlée que l'intent dans le fichier change le comportement d'un agent. Elle construit un fichier fictif de 10 couleurs avec un piège réaliste : deux rouges, `crimson500` (accent brand) et `red600` (danger système), sans description dans le fichier.

Sans description (3 runs) : 2 runs placent le crimson brand sur le bouton destructif "Delete account". Aucun run ne produit la même réponse complète. Avec un champ `$description` DTCG sur chaque token (2 runs) : réponses identiques, correctes. Le raisonnement cite explicitement la description. La différence est un seul champ par token — pas un changement de modèle, de prompt ou d'architecture.

Ce résultat confirme que l'intent doit être encodé **dans le fichier**, pas dans la documentation humaine. L'agent ne lit pas le site de docs : il lit le fichier source qu'on lui passe. Voir [readable-vs-usable-token](readable-vs-usable-token.md) pour la distinction entre readable (pipeline) et usable (agent reasoning), et [dtcg-annotation-schema](dtcg-annotation-schema.md) pour le template concret.

## DESIGN.md comme mécanisme d'intent à l'échelle du projet

Le format [design-md-format](design-md-format.md) (Google Labs, 2026) généralise la logique de l'intent-token au niveau du projet entier. Là où DTCG encode l'intent d'un token individuel via un champ `$description` ("Boston Clay — le seul driver d'interaction"), DESIGN.md encode le système d'intent en prose : pourquoi cette palette est "Architectural Minimalism meets Journalistic Gravitas", pourquoi le tertiaire `#B8422E` ne doit servir qu'aux CTAs et à rien d'autre. L'agent qui lit ce fichier n'a pas besoin qu'on lui répète l'intent à chaque prompt — il est dans le contexte persistant ([google-design-md-spec](../sources/google-design-md-spec.md)). C'est la réponse top-down à ce que le champ `$description` DTCG résout bottom-up : deux mécanismes complémentaires d'encodage de l'intent à des niveaux différents de granularité.

## Métadonnées d'intent enrichies : useFor / avoidFor / accessibility

Le champ `$description` DTCG (documenté dans [dtcg-annotation-schema](dtcg-annotation-schema.md)) est le plancher minimal — il donne un sens au token. [romina-kavcic](../entities/romina-kavcic.md) propose dans [agentic-ds-from-chatbot-to-orchestration](../sources/agentic-ds-from-chatbot-to-orchestration.md) une structure plus riche qui dépasse la description en prose pour encoder explicitement les conditions d'usage positives, négatives et les contraintes d'accessibilité :

```json
{
  "color.action.primary": {
    "value": "#3B82F6",
    "intent": "primary action",
    "useFor": ["main action in a flow", "confirmation action", "high-priority CTA"],
    "avoidFor": ["decorative backgrounds", "low-priority actions", "destructive actions without confirmation"],
    "accessibility": {
      "minimumContrast": "4.5:1",
      "requiresTextContrastCheck": true
    }
  },
  "spacing.component.md": {
    "value": "16px",
    "intent": "standard internal component spacing",
    "useFor": ["default card padding", "form field grouping", "standard layout rhythm"],
    "responsiveRules": {
      "compact": "spacing.component.sm",
      "comfortable": "spacing.component.lg"
    }
  }
}
```

Cette structure diffère du `$description` en prose sur trois points. Les champs `useFor` et `avoidFor` sont des listes énumérables — un agent peut les traverser algorithmiquement pour vérifier si son usage courant correspond à un cas licite ou interdit, sans avoir à interpréter du langage naturel. Le champ `accessibility` encode des contraintes non-négociables séparément des règles d'usage — ce qui permet à un auditeur de les traiter comme des violations d'existence (le ratio de contraste est une propriété vérifiable) plutôt que comme des violations d'intent (qui nécessitent une interprétation). Les `responsiveRules` encodent des règles de substitution conditionnelle que le token lui-même peut transporter.

La relation avec le [dtcg-annotation-schema](dtcg-annotation-schema.md) existant est d'extension, pas de remplacement. Le `$description` DTCG reste le format interopérable standardisé. La structure useFor/avoidFor/accessibility est une convention d'extensions privées (`$extensions`) ou un format propriétaire pour les équipes qui veulent aller plus loin dans l'encodage d'intent. Le point de cohérence avec [50-design-token-files-one-problem](../sources/50-design-token-files-one-problem.md) est maintenu : l'intent doit être dans le fichier source, pas dans la documentation humaine séparée.

## L'état du terrain en 2026

Sur 50 systèmes publics audités par Kavcic : ~15/50 ont une description dans le fichier, ~10/50 ont un champ de dépréciation lisible par machine, **1/50 a une règle explicite de non-usage** — GitHub Primer avec son champ `$extensions['org.primer.llm']` contenant usage et rules. L'intent est reconnu comme nécessaire ; son encodage dans les fichiers reste l'exception.
