# Guideline

## Intro 👈🤖

A fullscreen dialog takes over the whole viewport to let users complete a complex or content-heavy task before returning to the page.

---

## Definition

A fullscreen dialog is a dialog that occupies the entire viewport and does not use a backdrop. Its layout follows the structure and behavior of a standard page, making it suitable for complex tasks or content that requires more space and interaction.

**Key definitions**
Dialog: A temporary interface surface that focuses the user's attention on a specific task, decision, or piece of information.
→ Modal dialog: A centered dialog displayed above a backdrop.
→ Side sheet: A dialog anchored to the side of the viewport and displayed above a backdrop.
→ Fullscreen dialog: A dialog that occupies the entire viewport and follows a page-like layout without a backdrop.

---

## Best for 👈🤔

✅ Complex tasks that need more space than a modal dialog can offer

✅ Forms with several fields that require keyboard input

✅ Multi-step flows, such as creating an account or setting up a service

✅ Tasks whose changes are not saved instantly and need an explicit confirmation

✅ Content-heavy screens, such as a long selection list or detailed settings

✅ Small viewports, where a modal dialog would leave too little room for its content

✅ Tasks that may open a modal dialog on top, for example to confirm discarding changes

✅ Focused work that benefits from hiding the underlying page entirely

✅ Flows that must end with a clear action, such as Send, Create or Save

✅ Tasks that stay temporary: content that deserves its own URL belongs on a page

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The surface that fills the whole viewport, without backdrop, and follows the page grid | N |
| 2 | Previous or Subtitle | A link back to the previous step of a flow, or supporting text above the title; not used together | Y |
| 3 | Title | Names the task and gives the dialog its accessible name; can be preceded by a decorative or status icon | N |
| 4 | Close button | Lets users leave the dialog without completing the primary action | Y |
| 5 | Description | Supporting text below the title that adds context or instructions | Y |
| 6 | Slot | Flexible area for forms and custom content laid out on the page grid | Y |
| 7 | Actions | One to three actions: primary, secondary and a tertiary link; can stay sticky at the bottom | Y |

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

## sticky_action_do_&_dont 👈🤔

✅ **Do:** Keep actions sticky when the content is long enough to scroll  
❌ **Don't:** Make users scroll through a long form to find the main action

✅ **Do:** Let actions follow the content when the dialog holds little content  
❌ **Don't:** Pin actions at the bottom of a dialog that never scrolls

✅ **Do:** Keep the same logical action order whether the actions are sticky or not  
❌ **Don't:** Change which action is primary when the footer becomes sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content or the focused field  
❌ **Don't:** Let the sticky footer cover content that cannot be scrolled into view

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

## other_boolean_options_do_&_dont 👈🤔

✅ **Do:** Keep the Close button so users can always leave the dialog  
❌ **Don't:** Hide the Close button and leave no visible way to exit a full-screen surface

✅ **Do:** Use Previous to go back one step of a multi-step flow without closing the dialog  
❌ **Don't:** Use Previous to close the dialog or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the dialog

✅ **Do:** Use the Slot for forms and custom content, laid out on the page grid  
❌ **Don't:** Recreate a whole application or unrelated pages inside the dialog

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

## action_number_do_&_dont 👈🤔

✅ **Do:** Use a single action when there is one clear thing to do, and limit the dialog to three actions  
❌ **Don't:** Fill the dialog with choices that compete with the task

✅ **Do:** Give the Primary action to the outcome that completes the task  
❌ **Don't:** Style two actions as Primary in the same dialog

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary on every breakpoint  
❌ **Don't:** Let the visual order on desktop change the DOM or focus order

✅ **Do:** Write a confirming label that says what happens next, such as "Send" or "Create account"  
❌ **Don't:** Use vague labels such as "Done", "OK" or "Close"

---

## Examples of uses

**`Negative`** The Negative status is intended for destructive or error-related situations, such as confirming a deletion or communicating a backend or system error.
Use it when the outcome may result in data loss, an irreversible action, or when an error requires the user's attention.

**`Positive`** The Positive status is intended for successful outcomes or positive confirmations, such as confirming a completed action, successful subscription, or successful transaction.
Use it to reinforce that an action has been completed successfully or that the user's request has produced a positive result.

---

## examples_of_uses_do_&_dont 👈🤔

✅ **Do:** Use the Negative example, with a Negative action appearance, for destructive or irreversible actions  
❌ **Don't:** Use Negative styling for a routine, reversible choice

✅ **Do:** Use the Positive example to confirm that a long task or transaction succeeded  
❌ **Don't:** Open a full-screen Positive dialog for minor feedback a toast could give

✅ **Do:** Say what will happen and whether it can be undone before a destructive action  
❌ **Don't:** Ask "Are you sure?" without naming the consequence

✅ **Do:** Pair the status icon with a clear title and description  
❌ **Don't:** Rely on colour or the icon alone to convey the status

✅ **Do:** Give a way out of a negative dialog, such as Cancel or a recovery action  
❌ **Don't:** Leave users in an error dialog with no next step

---

## Responsive behaviour

The Fullscreen dialog occupies the entire viewport and therefore does not follow the same width and height specifications as the Modal dialog.

Unlike the Modal dialog, the Fullscreen dialog always spans the full available viewport width and height, regardless of the breakpoint or platform. It does not use fixed margins, percentage-based dimensions, or a column-based width to define its outer container.

The content within the Fullscreen dialog follows the same responsive grid and layout principles as a standard page. Content should be positioned and aligned according to the appropriate grid for each breakpoint, ensuring consistent horizontal margins, column spans, and maximum content widths across viewport sizes.

The Fullscreen dialog should therefore be treated as a full-page layout: the container occupies the entire viewport, while its content follows the standard page grid and responsive layout rules.

---

## responsive_behaviour_do_&_dont 👈🤔

✅ **Do:** Treat the dialog as a full-page layout that fills the viewport at every breakpoint  
❌ **Don't:** Add margins, a backdrop or a fixed width around the dialog

✅ **Do:** Lay the content out on the standard page grid for each breakpoint  
❌ **Don't:** Stretch text and fields across the whole width of a large screen

✅ **Do:** Keep the same maximum content and text widths as on any other page  
❌ **Don't:** Invent dialog-specific widths that differ from the rest of the product

✅ **Do:** Let long content scroll vertically inside the dialog  
❌ **Don't:** Let content scroll horizontally or overflow the viewport

✅ **Do:** Check the layout at every breakpoint, including the switch from a Modal dialog  
❌ **Don't:** Design the dialog for one screen size only

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

---

## additional_technical_information_do_&_dont 👈🤔

✅ **Do:** Always display a title that names the task  
❌ **Don't:** Hide the title, even when the content is self-explanatory

✅ **Do:** Keep the same task, content hierarchy and interaction logic when a Modal dialog becomes fullscreen  
❌ **Don't:** Change the content or the actions when the layout changes across breakpoints

✅ **Do:** Ask for confirmation in a Modal dialog before discarding unsaved changes  
❌ **Don't:** Close the dialog and lose what users entered without warning

✅ **Do:** Adapt an action's appearance, such as Negative, when its meaning requires it, and keep the Tertiary action a link  
❌ **Don't:** Turn the Tertiary action into a button

✅ **Do:** Open the dialog without animation, as specified  
❌ **Don't:** Add a slide or fade transition to the fullscreen dialog

---

# Specs

## States

🚧 Missing from source: States section in fullscreen_dialog_overview.md

---

## Layout and spacing

### Sticky action: False

- Fullscreen dialog — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_01`
- Close button — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_02`
- Header — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_03`
- Subtitle container — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_04`
- Title container — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_05`
- Body — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_06`
- Text container — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_07`
- Footer — `fullscreen_dialog@spec_layout_spacing_sticky_action_false_08`

### Sticky action: True

- Body — `fullscreen_dialog@spec_layout_spacing_sticky_action_true_01`
- Sticky footer safe area — `fullscreen_dialog@spec_layout_spacing_sticky_action_true_02`
- Text container — `fullscreen_dialog@spec_layout_spacing_sticky_action_true_03`
- Footer — `fullscreen_dialog@spec_layout_spacing_sticky_action_true_04`

---

# Accessibility 👈🤖

## Accessibility intro

Fullscreen dialog components must meet WCAG 2.2 Level AA standards so that all users can perceive the dialog, understand its purpose, operate its controls and leave it using keyboard, pointer or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

A fullscreen dialog replaces the whole page with a temporary task. Users of assistive technologies must be told that a dialog has opened, must be kept inside it while it is open, and must be returned to where they were when it closes.

### Key Challenges

- Focus must move into the dialog when it opens and stay inside it until it closes
- The page underneath must be unavailable to keyboard and screen reader users, even though no backdrop shows that it is covered
- Visual action order on tablet and desktop can differ from the logical order Primary → Secondary → Tertiary
- Long forms, sticky actions and zoom must not hide the title, the actions or the focused field

### Critical Success Factors

1. Expose the dialog with `role="dialog"` and `aria-modal="true"`, named by its always-visible title through `aria-labelledby`, and make the page behind inert (WCAG 4.1.2)
2. Move focus into the dialog on opening, keep Tab and Shift+Tab cycling inside it, and return focus to the triggering element on closing (WCAG 2.4.3)
3. Always provide a keyboard-operable way to leave the dialog, including the Escape key, and confirm before discarding unsaved changes
4. Keep the DOM and focus order of actions Primary → Secondary → Tertiary whatever their visual position

---

## Design Requirements

### Structure & Labels

- [ ] **Accessible name**: The title is always displayed and is referenced by `aria-labelledby`; a short description by `aria-describedby` (omit it when the content holds lists, tables or several paragraphs)
- [ ] **Initial focus**: The most likely-used element by default, the least destructive action for irreversible choices, the title or a top element when the content is long
- [ ] **Close button**: The icon-only Close button has an accessible name such as `aria-label="Close"` ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border on every interactive element ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Text contrast**: Title, subtitle and description meet 4.5:1 against the container; the Close icon and status icons meet 3:1
- [ ] **Reflow and zoom**: At 200% zoom and 320 px width the content scrolls vertically inside the dialog and the actions remain reachable

### Content

- [ ] **Clear title**: ❌ "Details" / ✅ "Create your account" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Explicit actions**: Action labels name the outcome and stay understandable out of context
- [ ] **Status not by colour alone**: Negative and positive meanings are carried by the text; a status Title icon has a text alternative, a decorative one is hidden

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify the dialog role and title are announced on opening, the page behind is not reachable, and actions are read in the order Primary, Secondary, Tertiary

### Keyboard Testing

- [ ] Focus moves into the dialog on opening, Tab and Shift+Tab cycle inside it, Escape closes it, focus returns to the trigger
- [ ] Focus indicator visible (≥3:1 contrast) on every control and never hidden behind sticky actions

### Functional Testing

- [ ] Verify the dialog opens without animation, that form errors are announced and focus moves to the first error, and that closing with unsaved changes asks for confirmation

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **2.1.2 No Keyboard Trap** (A): Focus stays inside the open dialog but users can always leave it with the keyboard
- **2.4.3 Focus Order** (A): Focus moves into the dialog, follows the logical action order and returns to the trigger on closing
- **2.4.11 Focus Not Obscured (Minimum)** (AA): The focused element is never fully hidden by sticky actions or the dialog edges
- **4.1.2 Name, Role, Value** (A): The dialog exposes its role, modal state and an accessible name taken from the title
- **1.4.10 Reflow** (AA): Content remains usable at 320 px width without two-dimensional scrolling

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Dialogs](https://a11y-guidelines.orange.com/en/articles/dialogs/1/)
- [WAI-ARIA Authoring Practices - Dialog (Modal) Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [WCAG 2.2 Understanding - Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 28, 2026 | 1.0.0 | **Version 2.7 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
