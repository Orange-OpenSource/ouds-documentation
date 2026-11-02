**`Filled`** Filled cards use a background surface to visually separate their content from the surrounding interface. By default, the card is displayed on a bg/primary background, with an additional action/support/enabled layer controlled by the Background Boolean property. The Background property controls only the interaction support layer, not the surrounding background surface. To display the card on a different background, designers should use a parent frame with one of the supported OUDS background or surface tokens, rather than manually overriding the card's interaction layers. This ensures that Hover, Focus and Pressed states remain consistent across different background contexts.

**`Outlined`** Outlined cards define their boundaries with a border instead of a background fill. The card remains transparent, allowing the surrounding surface to show through.

**`Elevated`** Elevated cards create visual separation through a shadow, giving the card a raised appearance. Unlike transparent cards, Elevated cards require a visible background surface to ensure that the shadow is rendered correctly. The shadow must apply to the card as a whole, not to individual elements within the slot. Designers must use the predefined OUDS elevation and background tokens. Custom shadows or opacity workarounds should not be applied.

&nbsp;

### Inverse background
Inverse backgrounds introduce a different color context within the interface. Text, icons, and interactive elements must adapt to the appropriate light or dark theme to maintain readability and contrast.

&nbsp;

### Image background
A background image can replace the default Filled surface.  
The image must preserve content readability across different screen sizes and cropping configurations. Interaction support layers must remain visible above the background image in all applicable states, including Hover, Focus and Pressed. The background image must not hide or override the card's interaction feedback.

⚠️ Only the predefined stroke, divider, and background colors specified for this component may be used. Custom colors are not allowed.