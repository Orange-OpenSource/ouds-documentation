# Guideline

## Intro 👈🤖

An action container card is a surface-like UI element that groups related information within an interactive surface and allows a user to perform a single primary action or navigate to a destination.

---

## Definition

An action container card is a surface-like UI element that groups related information within an interactive surface and allows a user to perform a single primary action or navigate to a destination.

The entire card acts as the interaction target and can behave as a button, an internal link, or an external link. Unlike the content container card, which can contain independent interactive elements, the action container card is designed around one primary interaction.

---

## Best for 👈🤔

✅ Presenting a self-contained item that leads to one destination or one action

✅ Promoting a product, offer or service when the whole surface is the target

✅ Opening a help article, tutorial or support topic from a short summary

✅ Displaying a list or grid of comparable items that each open their own detail page

✅ Starting a single task, such as a diagnostic, from a summary of what it does

✅ Linking to an external site from a visual summary of its content

✅ Offering a larger target area than a link or a button alone provides

✅ Building home pages and dashboards with several visual entry points

✅ Leading to a campaign or a landing page from a card with an image background

✅ Showing content that fits a short, scannable summary before the user goes further

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Background | Interaction support layer that sits over the card surface and carries the enabled treatment. | Y |
| 2 | Divider | Predefined line that reinforces the separation of a Filled card from its surrounding surface. | Y |
| 3 | Slot | Holds the customizable content of the card: text, imagery and other elements. | N |
| 4 | Focus | Focus indicator shown around the complete card when it receives keyboard focus. | Y |
| 5 | Focus inset | Inner line of the focus indicator that keeps it visible on any surface. | Y |
| 6 | Circular progress indicator | Shows that an action triggered by the card is being processed, in the Loading state. | Y |
| 7 | Skeleton | Placeholder shown while the content of the card is not yet available. | Y |

---

## Style

**`Filled`** Filled cards use a background surface to visually separate their content from the surrounding interface. By default, the card is displayed on a bg/primary background, with an additional action/support/enabled layer controlled by the Background Boolean property. The Background property controls only the interaction support layer, not the surrounding background surface. To display the card on a different background, designers should use a parent frame with one of the supported OUDS background or surface tokens, rather than manually overriding the card's interaction layers. This ensures that Hover, Focus and Pressed states remain consistent across different background contexts.

**`Outlined`** Outlined cards define their boundaries with a border instead of a background fill. The card remains transparent, allowing the surrounding surface to show through.

**`Elevated`** Elevated cards create visual separation through a shadow, giving the card a raised appearance. Unlike transparent cards, Elevated cards require a visible background surface to ensure that the shadow is rendered correctly. The shadow must apply to the card as a whole, not to individual elements within the slot. Designers must use the predefined OUDS elevation and background tokens. Custom shadows or opacity workarounds should not be applied.

**Inverse background**  
Inverse backgrounds introduce a different color context within the interface. Text, icons, and interactive elements must adapt to the appropriate light or dark theme to maintain readability and contrast.

**Image background**  
A background image can replace the default Filled surface.  
The image must preserve content readability across different screen sizes and cropping configurations. Interaction support layers must remain visible above the background image in all applicable states, including Hover, Focus and Pressed. The background image must not hide or override the card's interaction feedback.

⚠️ Only the predefined stroke, divider, and background colors specified for this component may be used. Custom colors are not allowed.

---

## style_do_&_dont 👈🤔

✅ **Do:** Use one style (Filled, Outlined or Elevated) for all the cards of a group  
❌ **Don't:** Mix card styles within the same group of cards

✅ **Do:** Place the card in a parent frame with a supported OUDS surface to change its background  
❌ **Don't:** Override the interaction layers of the card by hand

✅ **Do:** Use Elevated on a visible background surface, with the predefined OUDS elevation and background tokens  
❌ **Don't:** Apply a custom shadow or an opacity workaround

✅ **Do:** Keep text, icons and interactive elements readable on inverse and image backgrounds  
❌ **Don't:** Let a background image hide the Hover, Focus or Pressed feedback

✅ **Do:** Choose a background image that stays readable across screen sizes and crops  
❌ **Don't:** Use an image that only decorates the card and adds no context

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

✅ **Do:** Check that Hover, Focus and Pressed stay visible on every Surface you use  
❌ **Don't:** Add an external Surface frame to Elevated or Outlined cards

---

## Divider

The Divider Boolean property is available only when Style = Filled. It reinforces the card’s visual separation from its surrounding surface and follows the design system’s predefined color treatment.

**`True`** Displays the predefined divider on the Filled card.

**`False`** Hides the divider. The card relies on its Filled surface for visual separation.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use the divider only on Filled cards  
❌ **Don't:** Add a divider to Outlined or Elevated cards

✅ **Do:** Keep the predefined divider color  
❌ **Don't:** Recolor the divider to match the content

✅ **Do:** Apply the same divider choice to all the cards of a group  
❌ **Don't:** Mix cards with and without a divider in one group

✅ **Do:** Rely on the Filled surface for separation when Divider is False  
❌ **Don't:** Draw a manual line in the slot to imitate the divider

✅ **Do:** Use the divider to reinforce the separation from the surrounding surface  
❌ **Don't:** Use it to separate content inside the slot

---

## Role

The entire Action card acts as a single interactive element. Its semantic role must be defined according to the action performed when the card is activated.

**`External Link`** Navigates to a destination outside the current application or website.

**`Link`** Navigates to another page or destination within the same application or website.

**`Button`** Triggers an action without navigation.

---

## role_do_&_dont 👈🤔

✅ **Do:** Define the semantic role from what activating the card does  
❌ **Don't:** Give the card a link role when it triggers an action without navigation

✅ **Do:** Use Link for destinations in the same product and External Link for destinations outside it  
❌ **Don't:** Present an external destination as an internal link

✅ **Do:** Keep the entire card as the single interaction target  
❌ **Don't:** Add buttons or links with another destination inside the slot

✅ **Do:** Give the card an accessible name that states its purpose  
❌ **Don't:** Make the accessible name repeat all the content of the slot

✅ **Do:** Use the content card container when the content needs several independent actions  
❌ **Don't:** Force several actions into an action card container

---

# Specs

## States

**`Enabled`** The default state. The entire card is available for interaction and displays its content normally.

**`Hover`** Indicates that the pointer is positioned over the card.  
Use it to provide visual feedback that the card is interactive.

**`Focus`** Indicates that the card has received keyboard focus. The focus indicator must remain clearly visible around the complete card to support keyboard navigation and accessibility.

**`Pressed`** Provides immediate visual feedback while the user is pressing or activating the card.

⚠️ After activation, the card can follow only one interaction pattern.  
• Action or navigation: the card triggers an action or destination, behaving as a button or link.

**`Loading`** Loading indicates that an action triggered by the card is currently being processed. During this state, the card must not accept additional interactions. By default, the card content is hidden by the action/support/loading overlay, and a Progress indicator is displayed.  
In Figma, designers must set the loading overlay opacity to 100% to fully hide the underlying content.

For specific use cases, designers may customize the slot composition to preserve the existing content and display a Progress indicator over it. Loading should only be applied to the card performing an action. When multiple cards are waiting for content to load, use the Skeleton state instead.

In the Loading state, the card must provide sufficient space to display the Progress Indicator without clipping.

**`Disabled`** Indicates that the card is temporarily unavailable for interaction.

When a card is disabled, all content within the card must visually reflect the disabled state to maintain a consistent hierarchy and clearly communicate that the entire card is unavailable. Interactive or status elements such as buttons, tags, badges, links, or other components should use their corresponding Disabled state when available. Typography should use the appropriate disabled color tokens, while images and illustrations should use the defined disabled opacity.

The card and its content must not respond to user interaction while disabled.

**`Skeleton`** Represents the card while its content is not yet available.  
Use Skeleton when loading the initial content of a card or when multiple cards are loading at the same time, such as when displaying a list, grid, search results, or a page containing several cards.

Unlike the Loading state, Skeleton represents content that has not yet been loaded, rather than feedback for an action already initiated by the user.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility

## Interaction and accessibility

• The card must have a meaningful accessible name that clearly communicates its purpose without unnecessarily repeating all the content displayed within the slot.

• Hover, Focus and Pressed states must provide visual feedback across the entire card surface.

• A visual button or link may be displayed within the slot to reinforce the primary action, provided it represents the same destination or action as the card itself.

• Avoid creating additional independent focus targets for the same action. If the content requires multiple independent interactive elements, use the Card component instead.

• ⚠️ The synchronization of interaction states between the card and a nested visual action depends on platform implementation and must be validated with the relevant development team.

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 26, 2026 | 1.0.0 | **Version 2.8 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Anton Astafev |
