## Definition

A fullscreen dialog is a dialog that occupies the entire viewport and does not use a backdrop. Its layout follows the structure and behavior of a standard page, making it suitable for complex tasks or content that requires more space and interaction.

**Key definitions**
Dialog: A temporary interface surface that focuses the user's attention on a specific task, decision, or piece of information.
→ Modal dialog: A centered dialog displayed above a backdrop.
→ Side sheet: A dialog anchored to the side of the viewport and displayed above a backdrop.
→ Fullscreen dialog: A dialog that occupies the entire viewport and follows a page-like layout without a backdrop.

---

## Sticky action

**`False`** Actions are positioned directly after the description or content area and move with the content. The action area uses an Auto Layout Hug behavior.

**`True`** Actions remain fixed at the bottom of the modal while the content area can scroll independently. This ensures that primary actions remain continuously visible and accessible, especially when the modal contains a large amount of content.

**⚠️ Mobile layout**
This setting is automatic and changes depending on the grid. The user should not be able to interact with it.

• On mobile (grid: 2xs, xs, sm), the actions can either be stacked vertically or aligned horizontally.
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.
• On tablet and desktop, the actions are aligned horizontally (each component uses an Auto Layout Hug behavior).

---

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

---

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

**⚠️ Accessibility (action order)**
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

---

## Examples of uses

**`Negative`** The Negative status is intended for destructive or error-related situations, such as confirming a deletion or communicating a backend or system error.
Use it when the outcome may result in data loss, an irreversible action, or when an error requires the user's attention.

**`Positive`** The Positive status is intended for successful outcomes or positive confirmations, such as confirming a completed action, successful subscription, or successful transaction.
Use it to reinforce that an action has been completed successfully or that the user's request has produced a positive result.

---

## Responsive behaviour

The Fullscreen dialog occupies the entire viewport and therefore does not follow the same width and height specifications as the Modal dialog.

Unlike the Modal dialog, the Fullscreen dialog always spans the full available viewport width and height, regardless of the breakpoint or platform. It does not use fixed margins, percentage-based dimensions, or a column-based width to define its outer container.

The content within the Fullscreen dialog follows the same responsive grid and layout principles as a standard page. Content should be positioned and aligned according to the appropriate grid for each breakpoint, ensuring consistent horizontal margins, column spans, and maximum content widths across viewport sizes.

The Fullscreen dialog should therefore be treated as a full-page layout: the container occupies the entire viewport, while its content follows the standard page grid and responsive layout rules.

---

## ℹ️ Additional technical information

**Layout transformation across breakpoints**
The dialog layout may technically change between breakpoints when required by the available screen space and the interaction context.
For example, a Modal dialog may transform into a Fullscreen dialog on smaller viewports when the content or task requires more space. Similarly, a Modal dialog may transform into a Sidescreen dialog at larger breakpoints when maintaining visibility of the underlying page provides useful context.
These transformations should preserve the same task, content hierarchy, and interaction logic while adapting the presentation to the available viewport.

**Sticky action flexibility across breakpoints**
The positioning of the action area can change (sticky action=True or False) across breakpoints to adapt to the available screen space and the number of actions displayed.
This flexibility allows the action layout to adapt to the available space while preserving the same action hierarchy and interaction logic across breakpoints.

**Action button appearance flexibility**
The default action appearance is based on the action's hierarchy: the Primary action uses the Strong appearance, while the Secondary action uses the Default appearance.
However, the appearance of each action can be adapted to the context. You may select another appearance, such as Negative or Minimal, when the semantic meaning of the action requires it.
The same appearance may also be used for multiple actions when a clear primary/secondary hierarchy is not relevant. For example, two Default appearance can be used when both options should have equal visual weight and remain neutral.
The Tertiary action is always implemented as a Link and must not be replaced with a Button. Its role is to provide a lower-emphasis action that remains visually and semantically distinct from the Primary and Secondary actions.

**Title visibility**
The title must always be displayed and must not be hidden.
The title provides the dialog with a clear accessible name and allows users to immediately understand the purpose of the dialog. It is particularly important for screen reader users, who rely on the dialog's accessible name to understand the context of the content presented to them.
Even when the message is short, the title should clearly identify the purpose or subject of the dialog.

**Text max-width**
The component grid specifications are identical to those of a standard page design. The maximum text widths therefore follow the same limits as those used when designing any other page.

**Animation**
No opening animation for this component.
