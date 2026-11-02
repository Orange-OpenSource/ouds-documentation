# Guideline

## Intro 👈🤖

A content card container is a surface-like UI element that groups related information within a single non-interactive surface that can include independently interactive elements.

---

## Definition

A content card container is a surface-like UI element that groups related information within a single non-interactive surface that can include independently interactive elements.

The content card container's content is customizable, allowing you to adapt the internal layout with interactive elements like buttons and links, without altering the container's behavior. Unlike the action container card, which contains a single interaction, the content card container card is designed around multiple interactions.

---

## Best for 👈🤔

✅ Grouping related information into one non-interactive surface

✅ Presenting content that needs several independent actions, such as a button and links

✅ Pairing instructions or a summary with the next steps the user can take

✅ Arranging independent blocks of content on a dashboard

✅ Separating a block of information from the surrounding page

✅ Combining text, images and nested components in a customizable layout

✅ Building account or settings overviews that hold several links

✅ Presenting offers whose details and actions stay independently accessible

✅ Keeping a defined internal layout across mobile and desktop screens

✅ Cases where the container itself must not receive Hover, Focus or Pressed states

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Background | Layer that sits over the card surface and supports the visual separation of the card. | Y |
| 2 | Divider | Predefined line along the bottom edge of a Filled card. | Y |
| 3 | Slot | Holds the customizable content of the card, including independent interactive elements. | N |
| 4 | Skeleton | Placeholder shown while the content of the card has not loaded yet. | Y |

---

## Style

**`Filled`** Filled cards use a background surface to visually separate their content from the surrounding interface. By default, the card is displayed on a bg/primary background. To display the card on another supported background surface, designers should use the appropriate parent container rather than manually overriding the component's predefined visual properties. Unlike the Action card, the Card component is not interactive. Its background does not provide interaction feedback for the card itself. Any interactive elements within the slot retain their own independent interaction states.

**`Outlined`** Outlined cards define their boundaries with a border instead of a background fill. The container remains transparent, allowing the surrounding surface to show through.

**`Elevated`** Elevated cards create visual separation through a predefined shadow, giving the card a raised appearance. The background context is defined by the surrounding surface, while the card retains its own predefined elevation and visual support layers. The Card component remains non-interactive, regardless of its visual treatment.

**Inverse background**  
Inverse backgrounds introduce a different color context within the interface. Text, icons, and interactive elements must adapt to the appropriate light or dark theme to maintain readability and contrast.

⚠️ Only the predefined stroke, divider, and background colors specified for this component may be used. Custom colors are not allowed.

---

## style_do_&_dont 👈🤔

✅ **Do:** Use one style (Filled, Outlined or Elevated) for all the cards of a group  
❌ **Don't:** Mix card styles within the same group of cards

✅ **Do:** Use a parent container to display the card on another supported background surface  
❌ **Don't:** Override the predefined visual properties of the card by hand

✅ **Do:** Keep the card non-interactive whatever its visual treatment  
❌ **Don't:** Use Elevated to suggest that the whole card can be clicked

✅ **Do:** Adapt text, icons and interactive elements to the theme of an inverse background  
❌ **Don't:** Keep colors that lose contrast on an inverse background

✅ **Do:** Use only the predefined stroke, divider and background colors  
❌ **Don't:** Apply custom colors to the card

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

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Apply one corner treatment across the whole product or service  
❌ **Don't:** Mix rounded and square cards in the same product or service

✅ **Do:** Use rounded corners only with the themes that support them: Orange and Orange Compact  
❌ **Don't:** Expect rounded corners on the Sosh and Wireframe themes

✅ **Do:** Let the brand theme decide the corner treatment  
❌ **Don't:** Change the corners of a single card to give it more emphasis

✅ **Do:** Check that images and nested elements follow the corners of the card  
❌ **Don't:** Let slot content overflow a rounded corner

✅ **Do:** Keep the same corner treatment in every state of the card  
❌ **Don't:** Switch between rounded and square when the state changes

---

## Divider

The Divider property is available only for the Filled style. It adds a subtle line along the bottom edge of the card, following the visual conventions of the Card Item component. Its color is defined by the design system and must not be modified manually.

**`True`** Displays the bottom divider. The divider adds a subtle separation along the bottom edge of a Filled card.

**`False`** The card has no divider and relies on its surface color for separation.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use the divider only on Filled cards  
❌ **Don't:** Add a divider to Outlined or Elevated cards

✅ **Do:** Keep the predefined divider color  
❌ **Don't:** Recolor the divider by hand

✅ **Do:** Keep the divider along the bottom edge of the card  
❌ **Don't:** Add lines on the other edges of the card

✅ **Do:** Apply the same divider choice to all the cards of a group  
❌ **Don't:** Mix cards with and without a divider in one group

✅ **Do:** Rely on the surface color for separation when Divider is False  
❌ **Don't:** Draw a manual line in the slot to imitate the divider

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

## background_do_&_dont 👈🤔

✅ **Do:** Use the Background property on Filled and Elevated cards in the Enabled state  
❌ **Don't:** Expect the Background property on an Outlined card

✅ **Do:** Use an external Surface frame with predefined OUDS tokens to customize the base of a Filled card  
❌ **Don't:** Modify or replace the internal Background layer by hand

✅ **Do:** Match the corner-radius token of the external Surface frame to the card when Rounded corner is True  
❌ **Don't:** Leave a square Surface frame behind a rounded card

✅ **Do:** Set the Background property independently of the selected Surface  
❌ **Don't:** Use the Background property as a replacement for the surface

✅ **Do:** Keep the base background of an Elevated card on its predefined surface  
❌ **Don't:** Add an external Surface frame to Elevated or Outlined cards

---

## Slot spacing

The slot allows designers to customize the content and layout inside the card, including its text, imagery, and independent actions.  
Internal padding and spacing can be adjusted using two types of spacing tokens.

**`Fixed space`** Uses a consistent spacing value across screen references. The spacing remains the same on mobile and desktop.

**`Scaled space`** Uses responsive spacing values that adapt to the screen reference. Spacing may differ between mobile and desktop to preserve the intended layout. Use the appropriate OUDS spacing tokens rather than arbitrary values to maintain consistency across layouts.

⚠️ The card container does not apply internal padding by default. Designers are responsible for defining the content padding and spacing within the slot using the appropriate OUDS spacing tokens.  
When using nested components, their own internal spacing and corner-radius rules must be preserved.

---

## slot_spacing_do_&_dont 👈🤔

✅ **Do:** Define the padding and spacing of the content with OUDS spacing tokens  
❌ **Don't:** Use arbitrary spacing values in the slot

✅ **Do:** Use fixed space when the spacing must stay the same on mobile and desktop  
❌ **Don't:** Use fixed space for a layout that has to adapt to the screen

✅ **Do:** Use scaled space when the spacing must adapt to the screen reference  
❌ **Don't:** Change spacing by hand from one screen size to another

✅ **Do:** Preserve the internal spacing and corner-radius rules of nested components  
❌ **Don't:** Override the spacing of a nested component to fit the card

✅ **Do:** Test the layout with short and long content before adding more  
❌ **Don't:** Fill a card with dense, repetitive content that belongs in a list or a table

---

## Role

The Card component is a non-interactive surface that can include multiple independent interactive elements within its slot.  
Each interactive element must have its own semantic role according to the action it performs.

• Link: Navigates to another page or destination within the application or website.  
• External Link: Navigates to an external destination, when applicable.  
• Button: Triggers a specific action without navigation.

---

## role_do_&_dont 👈🤔

✅ **Do:** Keep the card non-interactive and give each element in the slot its own semantic role  
❌ **Don't:** Give the card container a button or link role

✅ **Do:** Use Link for in-product destinations, External Link for outside destinations and Button for actions  
❌ **Don't:** Use a link to trigger an action without navigation

✅ **Do:** Place the actions of the card consistently, at the end of its content  
❌ **Don't:** Scatter actions through the text of the card

✅ **Do:** Give every interactive element an accessible name that makes sense on its own  
❌ **Don't:** Repeat vague labels such as "Learn more" without context

✅ **Do:** Use the action card container when the whole content leads to a single action  
❌ **Don't:** Wrap a content card container in one link

---

# Specs

## States

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

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Interaction and accessibility

• The card itself does not receive Hover, Focus or Pressed states and must not behave as a button or link.

• Interactive elements placed within the slot, such as buttons and links, remain independently accessible and retain their own interaction states.

• Each interactive element must have an appropriate semantic role and a meaningful accessible name.

• Keyboard focus must be applied to the individual interactive elements, not to the card container itself.

• When the card is Disabled, nested interactive components must also be disabled and must not respond to user interaction.

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 26, 2026 | 1.0.0 | **Version 2.8 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Anton Astafev |
