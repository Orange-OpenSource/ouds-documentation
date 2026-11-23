---
id: fullscreen-dialog
category: Dialog
family: Modal
---

# Fullscreen dialog

A fullscreen dialog is a UI element that covers the entire viewport, interrupting the current page or task to focus the user's attention on a specific action, decision, or piece of information.

# Guideline

<img src="images/hero_image_fullscreen_dialog.png" alt="hero_image_fullscreen_dialog" width="864">

**⚠️ Web technical environment only.**  
To date, the specifications described for this component only cover the web technical environment.  
The specifications for the native iOS and Android environments will follow shortly.

## Anatomy

<img src="images/fullscreen_dialog@anatomy_img.png" alt="fullscreen_dialog@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The surface that fills the whole viewport, without backdrop, and follows the page grid | No |
| 2 | Previous or Subtitle | A link back to the previous step of a flow, or supporting text above the title; not used together | Yes |
| 3 | Title | Names the task and gives the dialog its accessible name; can be preceded by a decorative or status icon | No |
| 4 | Close button | Lets users leave the dialog without completing the primary action | Yes |
| 5 | Description | Supporting text below the title that adds context or instructions | Yes |
| 6 | Slot | Flexible area for forms and custom content laid out on the page grid | Yes |
| 7 | Actions | One to three actions: primary, secondary and a tertiary link; can stay sticky at the bottom | Yes |

## Definition

A fullscreen dialog is a UI element that covers the entire viewport, interrupting the current page or task to focus the user's attention on a specific action, decision, or piece of information.

The fullscreen dialog layout mirrors the structure and behavior of a standard page and lacks a backdrop, making it ideal for complex tasks or content needing more space and interaction.

## Sticky action

**`False`** Actions are positioned directly after the description or content area and move with the content. The action area uses an Auto Layout Hug behavior.

**`True`** Actions remain fixed at the bottom of the modal while the content area can scroll independently. This ensures that primary actions remain continuously visible and accessible, especially when the modal contains a large amount of content.

&nbsp;

### ⚠️ Mobile layout
This setting is automatic and changes depending on the grid. The user should not be able to interact with it.

• On mobile (grid: 2xs, xs, sm), the actions can either be stacked vertically or aligned horizontally.  
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
• On tablet and desktop, the actions are aligned horizontally (each component uses an Auto Layout Hug behavior).

<img src="images/fullscreen_dialog@sticky_action_img.png" alt="fullscreen_dialog@sticky_action_img" width="433">

## Other boolean options

**`Close button`** The Close button allows users to dismiss the modal without completing the primary action.

The Close button may be hidden when the modal has a clear, visible alternative way to dismiss it, such as a single Cancel action or another explicit dismissal control. It may also be omitted when the modal represents a mandatory step in a controlled flow where dismissal is intentionally unavailable.

Avoid hiding the Close button when users may reasonably expect to dismiss the dialog without committing to an action. The modal must always provide an accessible and discoverable way to exit unless the flow intentionally prevents dismissal.

**`Previous`** The Previous option displays a navigation link above the title, aligned to the leading edge of the modal. It is intended for multi-step flows where users can navigate back to a previous step without dismissing the entire modal. It is not recommended to include both a subtitle and a “previous” link.

**`Subtitle`** The Subtitle option displays supporting text above the title. Use it to provide additional context or clarify the purpose of the modal when the title alone is not sufficient. It is not recommended to include both a subtitle and a “previous” link.

**`Title icon`** The Title icon displays an icon to the right of the title. It can be used either as a decorative element or to communicate a functional status, such as success, deletion, error, warning, or information.  
Functional status icons may be static or animated using motion design when animation helps communicate a change of state or reinforces the meaning of the status.

**`Description`** The Description option displays supporting text below the title.  
It provides additional context, instructions, or information required to understand the purpose or outcome of the modal.  
The description may be omitted when the title alone provides sufficient context and the message is short and immediately understandable.

**`Slot`** The Slot provides a flexible container where you can insert custom templates, components, or other content within the modal.  
Use the Slot when the standard modal content structure does not adequately support the specific use case. Content inserted into the Slot must follow the Design System's spacing and responsive guidelines.

**`Scroll bar`** Decorative element used to indicate a vertical scroll.

**`Action`** The Action option controls whether the modal displays one or more action elements. Use it when the user needs to perform an action, make a decision, or confirm the outcome of the dialog.

Actions may be omitted when the modal is purely informative and no specific user action is required. In this case, the Close button or, when appropriate, clicking outside the modal in the backdrop area can be used to dismiss the dialog.

When no action is required, ensure that the available dismissal mechanism is sufficient and clearly discoverable. For dialogs containing important information or where accidental dismissal should be avoided, a Close button should be preferred over backdrop dismissal.

<img src="images/fullscreen_dialog@other_boolean_options_img.png" alt="fullscreen_dialog@other_boolean_options_img" width="433">

## Action number

**1 (single action)**  
A single action button is centered horizontally within the modal on mobile, tablet, and desktop. The action button can use either “fill” (especially on mobile devices) or “hug” behavior in Auto Layout.  
Use this configuration when there is one clear action available to the user.

**2 (primary and secondary actions)**  
Two actions are provided: a Primary action and a Secondary action.  
On mobile, the actions can either be stacked vertically or aligned horizontally. In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
On tablet and desktop, the actions are positioned horizontally and aligned to the trailing edge of the modal. Each actions are configured to “hug” behaviour in Auto Layout.  
The Primary action should represent the preferred or most important outcome, while the Secondary action provides an alternative or less prominent option.

**3 (primary, secondary, and tertiary actions)**  
Three actions are provided: a Primary action, a Secondary action, and a Tertiary action presented as a link.  
On mobile, all three actions can either be stacked vertically or aligned horizontally. In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
On tablet and desktop, the Primary and Secondary actions are positioned on the trailing edge of the modal, while the Tertiary action is positioned on the leading edge and aligned with the modal content. Each actions are configured to “hug” behaviour in Auto Layout.

**ℹ️ Note (Mobile layout=True):**  
On mobile (grid: 2xs, xs, sm), the “alignment” variant (available from 2 actions onwards) allows you to configure the actions to be positioned either vertically or horizontally.  
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
This “alignment” variant is available whether “Sticky action” is set to True or False.

**ℹ️ Note (Mobile layout=False):**  
On tablet or desktop, the “alignment” variant is not available.  
The Auto Layout setting for the action components is configured to “hug”. This setting cannot be changed.  
• If “sticky action” = True  
  • For 1 action: the element is centered in the sticky container.  
  • For 2 actions: the elements are aligned to the right of sticky container.  
  • For 3 actions: 1 element is aligned to the left and the other 2 are aligned to the right of the sticky container.  
• If “sticky action” = False, the actions are aligned horizontally to the left of the grid.

&nbsp;

### ⚠️ Accessibility (action order)
The visual order of actions must not change their semantic or interaction order.  
For screen reader and keyboard users, the implementation must preserve the following priority order:  
Primary → Secondary → Tertiary

On tablet or desktop, the visual order may be (if sticky action=True):  
Tertiary → Secondary → Primary

Or may be (sticky action=False):  
Secondary → Primary  
→ Tertiary

The DOM and accessibility tree should therefore expose the actions in priority order, even when CSS or layout positioning visually places the Tertiary action on the left. Do not rely on visual order alone to determine the reading or focus order.  
This ensures that assistive technology users encounter actions in the same logical order as users interacting with the mobile layout.

<img src="images/fullscreen_dialog@action_number_img.png" alt="fullscreen_dialog@action_number_img" width="433">

## Examples of uses

**`Negative`** The Negative status is intended for destructive or error-related situations, such as confirming a deletion or communicating a backend or system error.  
Use it when the outcome may result in data loss, an irreversible action, or when an error requires the user's attention.

**`Positive`** The Positive status is intended for successful outcomes or positive confirmations, such as confirming a completed action, successful subscription, or successful transaction.  
Use it to reinforce that an action has been completed successfully or that the user's request has produced a positive result.

<img src="images/fullscreen_dialog@examples_of_uses_img.png" alt="fullscreen_dialog@examples_of_uses_img" width="433">

## Responsive behaviour

The Fullscreen dialog occupies the entire viewport and therefore does not follow the same width and height specifications as the Modal dialog.

Unlike the Modal dialog, the Fullscreen dialog always spans the full available viewport width and height, regardless of the breakpoint or platform. It does not use fixed margins, percentage-based dimensions, or a column-based width to define its outer container.

The content within the Fullscreen dialog follows the same responsive grid and layout principles as a standard page. Content should be positioned and aligned according to the appropriate grid for each breakpoint, ensuring consistent horizontal margins, column spans, and maximum content widths across viewport sizes.

The Fullscreen dialog should therefore be treated as a full-page layout: the container occupies the entire viewport, while its content follows the standard page grid and responsive layout rules.

## Slot spacing customization

Padding within the content slot can be adjusted or removed according to the content and layout needs. Designers should use semantic spacing tokens when customizing these values.  
Any mandatory spacing must remain outside the slot, within the parent frame, to preserve the fullscreen layout and responsive grid rules.

## ℹ️ Additional technical information

### Layout transformation across breakpoints
The dialog layout may technically change between breakpoints when required by the available screen space and the interaction context.  
For example, a Modal dialog may transform into a Fullscreen dialog on smaller viewports when the content or task requires more space. Similarly, a Modal dialog may transform into a Sidescreen dialog at larger breakpoints when maintaining visibility of the underlying page provides useful context.  
These transformations should preserve the same task, content hierarchy, and interaction logic while adapting the presentation to the available viewport.

&nbsp;

### Sticky action behavior across breakpoints
The sticky action behavior must remain consistent across all breakpoints.  
When Sticky action=True, the action area remains sticky on mobile, tablet, and desktop. When Sticky action=False, the action area remains non-sticky across all breakpoints.  
The layout of the actions, including their alignment, orientation, and width, may adapt to the available screen space without changing the sticky behavior.

&nbsp;

### Action button appearance flexibility
The default action appearance is based on the action's hierarchy: the Primary action uses the Strong appearance, while the Secondary action uses the Default appearance.  
However, the appearance of each action can be adapted to the context. You may select another appearance, such as Negative or Minimal, when the semantic meaning of the action requires it.  
The same appearance may also be used for multiple actions when a clear primary/secondary hierarchy is not relevant. For example, two Default appearance can be used when both options should have equal visual weight and remain neutral.  
The Tertiary action is always implemented as a Link and must not be replaced with a Button. Its role is to provide a lower-emphasis action that remains visually and semantically distinct from the Primary and Secondary actions.

&nbsp;

### Title visibility
The title must always be displayed and must not be hidden.  
The title provides the dialog with a clear accessible name and allows users to immediately understand the purpose of the dialog. It is particularly important for screen reader users, who rely on the dialog's accessible name to understand the context of the content presented to them.  
Even when the message is short, the title should clearly identify the purpose or subject of the dialog.

&nbsp;

### Text max-width
The component grid specifications are identical to those of a standard page design. The maximum text widths therefore follow the same limits as those used when designing any other page.

&nbsp;

### Animation
No opening animation for this component.

# Specs

## Layout and spacing

### Sticky action: False

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_01.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_01" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_02.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_02" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_03.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_03" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_04.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_04" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_05.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_05" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_06.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_06" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_07.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_07" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_false_08.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_false_08" width="864">

### Sticky action: True

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_true_01.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_true_01" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_true_02.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_true_02" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_true_03.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_true_03" width="864">

<img src="images/fullscreen_dialog@spec_layout_spacing_sticky_action_true_04.png" alt="fullscreen_dialog@spec_layout_spacing_sticky_action_true_04" width="864">

# Accessibility

Work is in progress to deliver this content.

# Develop

## OUDS-Web example

> The current example is showing within a dedicated frame so it does not show the full screen context

[Components/Modals › Modals 5](https://web.unified-design-system.orange.com/storybook/?path=/story/components-modals--modals-5)

## Developer documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | [S-ouds-web-fullscreen-dialog](https://r.orange.fr/r/S-ouds-web-fullscreen-dialog) |
| OUDS Android | Not available yet |
| OUDS iOS | Not available yet |
| OUDS Flutter | Not available yet |

# Changelog

## Availability

Design status: **DEV**

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Fullscreen dialog component](https://r.orange.fr/r/S-ouds-design-fullscreen-dialog) | Done | 1.0.0 |
| OUDS Web (former Boosted) | [Web dev documentation](https://r.orange.fr/r/S-ouds-web-fullscreen-dialog) | Done | 1.0.0 |
| OUDS Android - Jetpack Compose | Not available yet | To do | – |
| OUDS iOS - Swift | Not available yet | To do | – |
| OUDS Flutter | Not available yet | To do | – |

## Design changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 10, 2026 | - | <ul><li>Documentation update: Sticky action behavior<ul><li>Corrected responsive behavior: previously, Sticky action could change between True and False across breakpoints.<li>Clarified that Sticky action must remain consistent on mobile, tablet, and desktop, while action alignment, orientation, and width can adapt to the available space.</ul><li>Documentation update: Slot spacing customization<ul><li>Clarified that padding within the content slot is customizable using semantic spacing tokens, while mandatory spacing must remain outside the slot to preserve the fullscreen layout.</ul></ul> | Anton Astafev |
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 28, 2026 | 1.0.0 | **Version 2.7 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
