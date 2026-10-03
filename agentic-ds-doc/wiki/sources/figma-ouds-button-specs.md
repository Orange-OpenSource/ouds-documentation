---
type: source
tags: [ouds, figma, button, composant, documentation, design-system, mcp, orange]
created: 2026-06-29
updated: 2026-06-29
sources: []
related:
  - "[schema-metadata-composant](../concepts/schema-metadata-composant.md)"
  - "[generation-spec-agentique](../concepts/generation-spec-agentique.md)"
  - "[lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md)"
  - "[pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md)"
  - "[composants-context-aware](../concepts/composants-context-aware.md)"
  - "[ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md)"
---

## OUDS Button — Specs Figma (Actions---Button, node 2071:11587)

**Type** : Fiche composant (bibliothèque Figma + frame de documentation)
**Source brute** : [2026-06-29_figma-ouds-button-specs](../../raw/2026-06-29_figma-ouds-button-specs.md)
**URL** : https://www.figma.com/design/bmVSCYZgRmXwdqtpvT4flo/Actions---Button?node-id=2071-11587
**Bibliothèque** : [OUDS Lib] Components library — Orange Unified Design System
**Mise à jour** : 2026-06-26

---

## Résumé

Le fichier Actions---Button est un fichier Figma dédié à la documentation du composant Button dans l'OUDS (Orange Unified Design System). Il est distinct de la bibliothèque de composants elle-même : c'est un fichier de specs, pas un fichier de composants. Le node 2071:11587 est le frame principal de documentation — une surface de 31 742 × 13 443 px contenant plusieurs colonnes de spécifications, une par variante du composant.

Le composant Button est extrait comme `component_set` dans `[OUDS Lib] Components library`, mis à jour le 2026-06-26. Sa description dans la bibliothèque Figma constitue le seul champ machine-readable accessible sans sélection dans l'app Desktop.

---

## Thèses principales

**1. La description Figma est la seule couche machine-readable sans sélection.** Le frame de documentation (2071:11587) contient l'intégralité des specs (dimensions, tokens, états, anatomie) mais est accessible uniquement en XML via get_metadata (>2,3M chars) ou via get_design_context avec sélection Desktop. La description du composant dans la bibliothèque, elle, est lisible directement par le MCP — et c'est elle qui contient les métadonnées d'usage.

**2. La description encode les trois éléments critiques pour un agent.** "When to use" (use cases), "Important" (contraintes et anti-patterns avec alternative explicite), "Key words" (tags de découvrabilité). C'est une implémentation légère du [schema-metadata-composant](../concepts/schema-metadata-composant.md) : les sections `usage` et `aiHints` sont couvertes, les sections structurelles (`props`, `variants`, `composition`) restent visuelles.

**3. L'anti-pattern est formulé avec son alternative.** "Do not use it for navigation purposes — use Navigation button instead." C'est le pattern "do-not-use + alternative" que [schema-metadata-composant](../concepts/schema-metadata-composant.md) identifie comme la forme la plus informationnellement dense pour un agent : scénario de non-usage + redirection vers le composant correct.

**4. Le champ Keywords est un signal d'audience IA.** "button, icon button, close button, action, primary action, secondary action, CTA" — cette liste n'est pas pour les designers (ils savent déjà ce qu'ils cherchent) mais pour les moteurs de recherche et les agents. Elle désambiguïse les usages proches (Button vs Icon button vs Close button) en les rendant tous accessibles depuis le même point d'entrée.

**5. Le fichier révèle une organisation multi-brand.** Sept bibliothèques Button coexistent dans l'organisation Orange (OUDS, OB, ODS Web, GP/PRO/OB, Sosh, Métier, TV). Le fichier Actions---Button documente uniquement la couche OUDS — la plus récente (mise à jour juin 2026), conçue pour couvrir les 4 plateformes (Web, Android, iOS, Flutter).

---

## Citations clés (≤ 15 mots)

— "Button should be used only to trigger actions or events." (description Figma OUDS)
— "Do not use it for navigation purposes — use Navigation button instead." (description Figma OUDS)
— "If rounded corners are used in the design system, sharp corners must be avoided." (description Figma OUDS)

---

## Connexions identifiées

Le composant Button OUDS est un cas d'école pour plusieurs concepts du vault. Sa description Figma illustre concrètement [schema-metadata-composant](../concepts/schema-metadata-composant.md) (couverture partielle des 9 sections), [lisibilite-machine-design-system](../concepts/lisibilite-machine-design-system.md) (ce qui est lisible vs ce qui reste visuel), [ia-comme-utilisateur](../concepts/ia-comme-utilisateur.md) (les keywords comme signal d'audience IA explicite), et [composants-context-aware](../concepts/composants-context-aware.md) (la règle "pas pour la navigation" comme frontière de contexte encodée au niveau de la taxonomie des composants). Le frame de documentation 2071:11587 est un exemple de la cible d'output de [generation-spec-agentique](../concepts/generation-spec-agentique.md) : ce que l'équipe OUDS produit manuellement, uSpec vise à le générer automatiquement.

Le fait que le frame soit trop grand pour le MCP sans sélection Desktop est lui-même une donnée : il illustre la limite concrète du [pipeline-figma-docs-automatise](../concepts/pipeline-figma-docs-automatise.md) tel que décrit par Kavcic — le pipeline peut tracker un frame, mais si ce frame pèse 2,3M de XML, il ne peut pas l'ingérer sans un crawl sélectif.
