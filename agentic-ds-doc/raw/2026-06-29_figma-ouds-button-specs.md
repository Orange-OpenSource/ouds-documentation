# [RAW] OUDS Button — Specs Figma (source MCP)

> Fichier brut — ne pas modifier. Toutes les données proviennent exclusivement du Figma MCP.

**Source** : Figma MCP (`search_design_system`, `get_libraries`, `get_screenshot`)
**Fichier Figma** : Actions---Button
**URL** : https://www.figma.com/design/bmVSCYZgRmXwdqtpvT4flo/Actions---Button?node-id=2071-11587
**Node cible** : 2071:11587 (frame principale de documentation des specs)
**Bibliothèque** : [OUDS Lib] Components library
**Clé composant** : 4616cd237e834c1d101f7e2d603b1196e22168e0
**Dernière mise à jour Figma** : 2026-06-26T16:39:22Z
**Date d'extraction** : 2026-06-29

---

## 1. Description du composant (verbatim — champ description de la bibliothèque Figma)

```
🧭 When to use?
Use Button to:
Trigger an action or event
Start or submit a task (e.g. send, save, continue)
Confirm a decision or choice
Emphasize a primary or secondary action within the interface


⚠️ ImportantWhen use rounded/square corners ●■
If rounded corners are used in the design system, sharp corners must be avoided, and vice versa - this is a system-level decision that must be applied consistently across all components.
When placing a button on a colored background, use Button - On colored bg to ensure sufficient contrast and accessibility.
Button should be used only to trigger actions or events. Do not use it for navigation purposes - use Navigation button instead.


🎨 Design
Design guidelines


🛠 Development
OUDS-Web
OUDS-Android
OUDS-iOS
OUDS-Flutter


🔑 Key words
button, icon button, close button, action, primary action, secondary action, CTA
```

---

## 2. Bibliothèques liées au fichier (get_libraries)

Bibliothèques actives dans le fichier Actions / Button :

- [OUDS Lib] Orange illustrations
- [OUDS Lib] Design tokens
- [OUDS Lib] Themed icons
- [OUDS Lib] Components library
- [OUDS Lib] Wireframe icons
- Actions / Button (le fichier de documentation lui-même)
- [OUDS Lib] Sosh icons
- [OUDS Lib] Orange Solaris icons
- [OUDS Lib] Orange illustrations tokens

---

## 3. Structure visuelle du frame principal (get_screenshot — node 2071:11587)

Dimensions du frame : 31 742 × 13 443 px (original), rendu screenshot à 2 048 × 868 px.

Le frame contient plusieurs colonnes verticales de documentation, chacune dédiée à une variante du composant Button. Les colonnes visibles dans le screenshot comprennent au minimum des variantes standard et des variantes dites "fin colormap". La structure interne de chaque colonne inclut : en-tête de variante, anatomie du composant, panneaux de propriétés, grilles d'états (enabled/hover/pressed/focus/disabled/loading/skeleton) dans les différents layouts, et sections de règles d'espacement/layout.

Note technique : la frame 2071:11587 produit plus de 2,3 millions de caractères XML via get_metadata — trop large pour être traitée en un seul appel. Les détails fins (valeurs de tokens, numéros anatomiques, mesures précises) ne sont donc pas accessibles via le MCP sans sélection préalable dans l'app Figma Desktop (get_design_context requiert une couche sélectionnée).

---

## 4. Résultats de recherche dans le design system (search_design_system)

Requête : "button"
Résultat pertinent (OUDS) :

```json
{
  "name": "Button",
  "libraryName": "[OUDS Lib] Components library",
  "assetType": "component_set",
  "updatedAt": "2026-06-26T16:39:22Z",
  "componentKey": "4616cd237e834c1d101f7e2d603b1196e22168e0",
  "filePath": "design_systems/[OUDS Lib] Components library/components/Button"
}
```

Le fichier Actions---Button coexiste avec d'autres bibliothèques Button dans l'organisation Orange : Orange GP/PRO/OB, [OB Lib] Components, [ODS Lib] Orange Web UI, Sosh GP, Orange Métier, Orange TV — ce qui témoigne d'une organisation multi-brand avec un composant Button décliné par marque.
