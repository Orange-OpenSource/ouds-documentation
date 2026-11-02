## Definition

The Card component groups related information within a single surface. The card itself is not interactive, but it can contain independently interactive elements, such as buttons and links. Its content is customizable through a slot, allowing designers to adapt the internal layout without changing the card's non-interactive behavior.

---

## Style

**`Filled`** Filled cards use a background surface to visually separate their content from the surrounding interface. By default, the card is displayed on a bg/primary background. To display the card on another supported background surface, designers should use the appropriate parent container rather than manually overriding the component's predefined visual properties. Unlike the Action card, the Card component is not interactive. Its background does not provide interaction feedback for the card itself. Any interactive elements within the slot retain their own independent interaction states.

**`Outlined`** Outlined cards define their boundaries with a border instead of a background fill. The container remains transparent, allowing the surrounding surface to show through.

**`Elevated`** Elevated cards create visual separation through a predefined shadow, giving the card a raised appearance. The background context is defined by the surrounding surface, while the card retains its own predefined elevation and visual support layers. The Card component remains non-interactive, regardless of its visual treatment.

**Inverse background**
Inverse backgrounds introduce a different color context within the interface. Text, icons, and interactive elements must adapt to the appropriate light or dark theme to maintain readability and contrast.

⚠️ Only the predefined stroke, divider, and background colors specified for this component may be used. Custom colors are not allowed.

---

## State

**`Enabled`** The card displays its content normally. Interactive elements within the slot remain independently accessible and retain their own
interaction states.

The card can be displayed on different predefined OUDS background surfaces according to its layout context. The background context must remain consistent when switching between card states. Interactive elements placed within the slot retain their own states independently of the container.

**`Disabled`** The card and its contents communicate an unavailable state. All interactive elements within the slot must also be disabled and must not respond to user interaction.

In Figma, changing the card state does not automatically update slotted content.

⚠️ Designers must manually set nested interactive components to their Disabled state and replace content color tokens, for example content/default with content/disabled, wherever applicable.

⚠️ Do not apply a global opacity reduction to the entire slot content.
Text and nested interactive components must use their corresponding Disabled states or color tokens. Images and illustrations must use the predefined OUDS disabled opacity token, which corresponds to 20% opacity in the current specification.

**`Skeleton`** The Skeleton state represents content that has not yet loaded. Replace the final content with non-interactive placeholders that reflect the card’s expected layout and visual hierarchy.

During the Skeleton state, the card must display non-interactive placeholders only. Interactive controls within the slot must not be accessible or actionable until the actual content has finished loading.

---

## Rounded corner

Although this property can be edited on individual components in Figma, the corner treatment is defined consistently at product or service level by the selected brand theme. Do not mix rounded and square treatments within the same product or service.

**`True`** Displays the card with rounded corners, creating a softer appearance in themes that support this treatment.

**`False`** Displays the card with square corners, reflecting Orange’s more structured visual language. The rounded-corner option is available for Orange and Orange Compact, but unavailable for Sosh and Wireframe.

This option is technically not available for all brand themes
Here’s the list of rounded corners availability by brand theme

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Unavailable |
| Wireframe | Unavailable |

---

## Divider

The Divider property is available only for the Filled style. It adds a subtle line along the bottom edge of the card, following the visual conventions of the Card Item component. Its color is defined by the design system and must not be modified manually.

**`True`** Displays the bottom divider. The divider adds a subtle separation along the bottom edge of a Filled card.

**`False`** The card has no divider and relies on its surface color for separation.

---

## Background

The Background Boolean property controls the visibility of the predefined color/action/support/enabled layer within the Card component. This property is available for the Filled and Elevated styles when State = Enabled.

**`True`** Displays the predefined color/action/support/enabled layer within the Card, over the underlying surface.

**`False`** Hides the internal Background layer, leaving the underlying surface visible without the additional support treatment.

**⚠️ Surface customization**
In the Filled style, designers can place the Card inside an additional Surface frame to customize its base background using supported tokens, such as surface/primary, surface/secondary, or surface/tertiary etc...

This external frame acts as the underlying surface of the Card and is independent of the component's internal Background layer.
The Background Boolean can be enabled or disabled independently of the selected Surface.

For other styles:
• Elevated: Uses its predefined surface/primary background. The Background Boolean remains available, but the external Surface customization is not supported.
• Outlined: Does not support the Background Boolean or additional Surface customization.

⚠️ The external Surface frame must use predefined OUDS surface tokens. The Card's internal Background layer must not be manually modified or replaced.

⚠️ When Rounded corner = True, the external Surface frame must use a predefined OUDS corner-radius token matching the Card's corner-radius value. This ensures consistent corner alignment between the Card and its underlying Surface.

---

## Slot spacing

The slot allows designers to customize the content and layout inside the card, including its text, imagery, and independent actions.
Internal padding and spacing can be adjusted using two types of spacing tokens.

**`Fixed space`** Uses a consistent spacing value across screen references. The spacing remains the same on mobile and desktop.

**`Scaled space`** Uses responsive spacing values that adapt to the screen reference. Spacing may differ between mobile and desktop to preserve the intended layout. Use the appropriate OUDS spacing tokens rather than arbitrary values to maintain consistency across layouts.

⚠️ The card container does not apply internal padding by default. Designers are responsible for defining the content padding and spacing within the slot using the appropriate OUDS spacing tokens.
When using nested components, their own internal spacing and corner-radius rules must be preserved.

---

## Role

The Card component is a non-interactive surface that can include multiple independent interactive elements within its slot.
Each interactive element must have its own semantic role according to the action it performs.

• Link: Navigates to another page or destination within the application or website.
• External Link: Navigates to an external destination, when applicable.
• Button: Triggers a specific action without navigation.

---

## Interaction and accessibility

• The card itself does not receive Hover, Focus or Pressed states and must not behave as a button or link.

• Interactive elements placed within the slot, such as buttons and links, remain independently accessible and retain their own interaction states.

• Each interactive element must have an appropriate semantic role and a meaningful accessible name.

• Keyboard focus must be applied to the individual interactive elements, not to the card container itself.

• When the card is Disabled, nested interactive components must also be disabled and must not respond to user interaction.
