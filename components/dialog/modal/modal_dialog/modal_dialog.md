# Guideline

## Intro 👈🤖

A modal dialog appears above the page to focus users on one decision, task or piece of information before they continue.

---

## Definition

A modal dialog is a temporary surface that interrupts the current page or task to focus the user's attention on a specific action, decision, or piece of information. It is displayed above a backdrop that visually separates the dialog from the underlying content and prevents interaction with it.

**Key definitions**
Dialog: A temporary interface surface that focuses the user's attention on a specific task, decision, or piece of information.
→ Modal dialog: A centered dialog displayed above a backdrop.
→ Side sheet: A dialog anchored to the side of the viewport and displayed above a backdrop.
→ Fullscreen dialog: A dialog that occupies the entire viewport and follows a page-like layout without a backdrop.

---

## Best for 👈🤔

✅ Confirming a destructive or irreversible action, with a clear description of its consequences

✅ Asking for a decision that must be made before the task can continue

✅ Requesting critical information the system needs before it can go on

✅ Reporting a blocking error that users need to acknowledge or resolve

✅ Urgent information about the user's current work that requires acknowledgement

✅ Confirming an important outcome, such as a completed payment or subscription

✅ Warning about unsaved changes before users leave a page or close a flow

✅ A short, single task that benefits from keeping the page context behind it

✅ Breaking a focused task into a few short steps, using the Previous link to go back

✅ Critical moments only: non-critical feedback belongs in a toast or an inline alert

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Backdrop | Dark overlay, blurred or not, that separates the dialog from the page and blocks interaction with it | N |
| 2 | Container | The centred surface that holds the dialog content, with square or rounded corners | N |
| 3 | Previous or Subtitle | A link back to the previous step of a flow, or supporting text above the title; not used together | Y |
| 4 | Title | Names the purpose of the dialog and gives it its accessible name; can be preceded by a decorative or status icon | N |
| 5 | Close button | Lets users dismiss the dialog without completing the primary action | Y |
| 6 | Description | Supporting text below the title that adds context or instructions | Y |
| 7 | Slot | Flexible area for custom content the standard structure does not cover | Y |
| 8 | Actions | One to three actions: primary, secondary and a tertiary link; can stay sticky at the bottom | Y |

---

## Size

**`Default`** The Default size is intended for most modal dialog use cases. It provides sufficient space for standard content, including a title, description, optional supporting content, and one or more actions.

**`Small`** The Small size is intended for simple, focused interactions with limited content. Use it when the dialog requires less space and the user can complete the task with minimal information or interaction.

The Size variant defines the overall dimensions of the dialog container and adapts the scale of its internal layout.

On mobile, the Default and Small sizes use the same container dimensions. The difference between the two sizes becomes visible from tablet and desktop breakpoints, where they follow different responsive grid configurations and therefore use different container widths and heights.

The Size variant also affects the internal scale of the dialog. The Default and Small sizes use different typography references and internal spacing values, including both horizontal and vertical spacing, to maintain a consistent visual hierarchy and proportion at each size.

---

## size_do_&_dont 👈🤔

✅ **Do:** Choose the size from the amount of content: Default for most dialogs, Small for brief text  
❌ **Don't:** Pick Small for content that needs room to be read comfortably

✅ **Do:** Use Small for short confirmations and simple, focused choices  
❌ **Don't:** Use Default for a one-line message that leaves the dialog mostly empty

✅ **Do:** Keep the same size for dialogs of the same kind across a journey  
❌ **Don't:** Change size between two steps of the same flow

✅ **Do:** Let the size set typography and spacing together  
❌ **Don't:** Override text styles or spacing to squeeze more content into a size

✅ **Do:** Move to the Default size, or to a Fullscreen dialog, when content no longer fits  
❌ **Don't:** Let content scroll horizontally inside the dialog

---

## Fixed height

**`False`** The modal height adapts to the content and uses an Auto Layout Hug behavior. The maximum height is not reached, allowing the modal to remain as compact as possible.

**`True`** The modal uses its maximum defined height. This option can be used to simulate a modal containing a large amount of content that requires vertical scrolling, or to define a fixed-height modal for multi-step flows or content with a consistent layout.

---

## fixed_height_do_&_dont 👈🤔

✅ **Do:** Let the dialog hug its content when the content is short  
❌ **Don't:** Force the maximum height on a dialog that holds two lines of text

✅ **Do:** Use a fixed height for multi-step flows so the dialog does not jump between steps  
❌ **Don't:** Let the dialog resize at every step of a flow

✅ **Do:** Keep vertical scrolling to a minimum by keeping the content concise  
❌ **Don't:** Put a long page of content into a dialog and rely on scrolling

✅ **Do:** Keep the title and the actions in place while the content scrolls vertically  
❌ **Don't:** Scroll the whole dialog, title included, out of view

✅ **Do:** Show that more content is available below when the content scrolls  
❌ **Don't:** Cut content off with no sign that it continues

---

## Sticky action

**`False`** Actions are positioned directly after the description or content area and move with the content. The action area uses an Auto Layout Hug behavior.

**`True`** Actions remain fixed at the bottom of the modal while the content area can scroll independently. This ensures that primary actions remain continuously visible and accessible, especially when the modal contains a large amount of content.

ℹ️ Note: Fixed height=True is automatically enabled when Sticky action=True.

**⚠️ Mobile layout**
This setting is automatic and changes depending on the grid. The user should not be able to interact with it.

• On mobile (grid: 2xs, xs, sm), the actions can either be stacked vertically or aligned horizontally.
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.
• On tablet and desktop, the actions are aligned horizontally (each component uses an Auto Layout Hug behavior).

---

## sticky_action_do_&_dont 👈🤔

✅ **Do:** Keep actions sticky when the content is long enough to scroll  
❌ **Don't:** Make users scroll to the end of long content to find the main action

✅ **Do:** Let actions follow the content when the dialog is short  
❌ **Don't:** Pin actions at the bottom of a dialog that never scrolls

✅ **Do:** Keep the same action order whether the actions are sticky or not  
❌ **Don't:** Reorder actions when switching between sticky and non-sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content  
❌ **Don't:** Let the action area cover content that cannot be scrolled into view

---

## Rounded corner

Even though in Figma this rendering option is available and editable from the properties of each input component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used.
It is therefore impossible to have one modal component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

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

✅ **Do:** Apply the same corner setting to every dialog in a product or service  
❌ **Don't:** Mix square and rounded dialogs within the same product

✅ **Do:** Keep square corners as the default Orange style  
❌ **Don't:** Switch to rounded corners for a single screen or campaign

✅ **Do:** Use rounded corners when the whole product adopts the softer, more tactile style  
❌ **Don't:** Round the dialog while its buttons and inputs stay square

✅ **Do:** Check that the brand theme supports rounded corners before using them  
❌ **Don't:** Enable rounded corners on Sosh or Wireframe themes

✅ **Do:** Decide the corner style once, at product level  
❌ **Don't:** Leave the choice to each designer or each screen

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

✅ **Do:** Keep the Close button whenever users may want to leave without choosing an action  
❌ **Don't:** Hide the Close button and leave no visible way to exit

✅ **Do:** Use Previous in multi-step flows to go back one step without closing the dialog  
❌ **Don't:** Use Previous to close the dialog or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the dialog

✅ **Do:** Use the Slot for content the standard structure cannot hold, following spacing and responsive rules  
❌ **Don't:** Fill the Slot with a full page of unrelated content

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
• For 1 action: the element is centered in the modal.
• For 2 actions: the elements are aligned to the right of the modal.
• For 3 actions: 1 element is aligned to the left and the other 2 are aligned to the right.

**⚠️ Accessibility (action order)**
The visual order of actions must not change their semantic or interaction order.
For screen reader and keyboard users, the implementation must preserve the following priority order:
Primary → Secondary → Tertiary

On tablet or desktop, the visual order may be:
Tertiary → Secondary → Primary

The DOM and accessibility tree should therefore expose the actions in priority order, even when CSS or layout positioning visually places the Tertiary action on the left. Do not rely on visual order alone to determine the reading or focus order.
This ensures that assistive technology users encounter actions in the same logical order as users interacting with the mobile layout.

---

## action_number_do_&_dont 👈🤔

✅ **Do:** Use a single action when there is one clear thing to do, and limit the dialog to three actions  
❌ **Don't:** Fill the dialog with choices that turn it into a complex interaction

✅ **Do:** Give the Primary action to the preferred outcome and echo the title in its label  
❌ **Don't:** Style two actions as Primary in the same dialog

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary on every breakpoint  
❌ **Don't:** Let the visual order on desktop change the DOM or focus order

✅ **Do:** Write action labels with active verbs that name the outcome, such as "Delete file"  
❌ **Don't:** Use vague or passive labels such as "OK" or "Done"

---

## Backdrop blurred

**`True`** The backdrop uses a black overlay with 68% opacity combined with a background blur effect. Use this option when the underlying content should be visually de-emphasized to reinforce the modal's focus and hierarchy, or when reducing background complexity helps users concentrate on the modal content.
Background blur should not be used solely for decorative purposes. It should support the visual separation between the modal and the underlying content without reducing the perceived performance or accessibility of the experience.

**`False`** The backdrop uses a black overlay with 68% opacity and no background blur. Use this option when maintaining a clear visual relationship with the underlying page is important, or when the background content provides useful context for the modal.

---

## backdrop_blurred_do_&_dont 👈🤔

✅ **Do:** Use the blurred backdrop when a busy page behind the dialog distracts from it  
❌ **Don't:** Add blur purely as decoration

✅ **Do:** Use the plain backdrop when the page behind gives useful context  
❌ **Don't:** Blur the page when users need to refer to what is behind the dialog

✅ **Do:** Keep the same backdrop setting for similar dialogs in a product  
❌ **Don't:** Alternate blurred and plain backdrops at random

✅ **Do:** Keep the 68% black overlay in both settings  
❌ **Don't:** Lighten or tint the overlay to match a campaign

✅ **Do:** Check that blur does not slow the experience on low-end devices  
❌ **Don't:** Trade perceived performance for a visual effect

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

✅ **Do:** Use the Positive example to confirm that an action or transaction succeeded  
❌ **Don't:** Open a Positive dialog for minor feedback a toast could give

✅ **Do:** Say what will happen and whether it can be undone before a destructive action  
❌ **Don't:** Ask "Are you sure?" without naming the consequence

✅ **Do:** Pair the status icon with a clear title and description  
❌ **Don't:** Rely on colour or the icon alone to convey the status

✅ **Do:** Give a way out of a negative dialog, such as Cancel or a recovery action  
❌ **Don't:** Leave users in an error dialog with no next step

---

## Responsive behaviour

**Horizontal responsive behaviour**

The modal width adapts to the viewport according to the selected Size variant and the responsive grid of each platform.
The modal follows the defined column spans at larger breakpoints, while smaller viewport widths use fixed horizontal margins to preserve sufficient spacing from the viewport edges.

| Breakpoint | Viewport width | Default | Small |
|---|---|---|---|
| 2xs | 1–389 px | 16 px margin | 16 px margin |
| xs | 390–479 px | 16 px margin | 16 px margin |
| sm | 480–735 px | 10 columns | 10 columns |
| md | 736–1023 px | 10 columns | 8 columns |
| lg | 1024–1319 px | 10 columns | 6 columns |
| xl | 1320–1639 px | 8 columns | 4 columns |
| 2xl | 1640–1879 px | 8 columns | 4 columns |
| 3xl | 1880+ px | 8 columns | 4 columns |

For the 2xs and xs breakpoints, the modal does not follow a column-based grid and instead maintains a 16 px margin from the viewport edges.

**Vertical responsive behaviour**

The modal height adapts to the viewport according to the selected Size variant and the responsive breakpoint.
The Default size uses a larger proportion of the available viewport, while the Small size remains more compact. When the modal content exceeds the available height, the content area becomes vertically scrollable.

| Breakpoint | Default | Small |
|---|---|---|
| 2xs | 16 px margin | 50% of viewport |
| xs | 16 px margin | 50% of viewport |
| sm | 90% of viewport | 50% of viewport |
| md | 90% of viewport | 50% of viewport |
| lg | 90% of viewport | 60% of viewport |
| xl | 90% of viewport | 60% of viewport |
| 2xl | 90% of viewport | 60% of viewport |
| 3xl | 90% of viewport | 50% of viewport |

---

## responsive_behaviour_do_&_dont 👈🤔

✅ **Do:** Let the dialog width follow the column spans defined for each breakpoint and size  
❌ **Don't:** Set a fixed pixel width that ignores the grid

✅ **Do:** Keep the 16 px margin on 2xs and xs screens  
❌ **Don't:** Let the dialog touch the edges of the viewport

✅ **Do:** Let the content area scroll when it exceeds the available height  
❌ **Don't:** Let the dialog grow taller than the viewport

✅ **Do:** Check both sizes at every breakpoint, including the transitions between them  
❌ **Don't:** Design the dialog for one screen size only

✅ **Do:** Keep the dialog within the height defined for its size and breakpoint  
❌ **Don't:** Stretch a Small dialog to the height of a Default one

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
There is no maximum width limit for text in this component.

**Static backdrop**
The Static backdrop parameter is optional and may be enabled or disabled depending on the use case.
When the backdrop is set to static, clicking outside the dialog does not close it. This behavior is appropriate when accidental dismissal could result in data loss, interrupt an important process, or cause the user to lose progress.
When the backdrop is not static, clicking outside the dialog may dismiss it when the interaction is considered safe to cancel.

**Animation**
When enabled, the dialog uses a slide-down entrance animation rather than appearing with an immediate cut.
The modal slides down from the top of the viewport when it opens, providing a clear visual transition that helps users understand where the dialog originated and establishes a stronger sense of spatial continuity.
Animation should respect the user's reduced-motion preferences. When reduced motion is enabled, the transition should be removed.

---

## additional_technical_information_do_&_dont 👈🤔

✅ **Do:** Always display a title that names the purpose of the dialog  
❌ **Don't:** Hide the title, even when the message is short

✅ **Do:** Use a static backdrop when closing by accident would lose data or progress  
❌ **Don't:** Let a click outside discard a form the user is filling in

✅ **Do:** Keep the same task, content hierarchy and interaction logic when the layout changes across breakpoints  
❌ **Don't:** Change the content or the actions when a modal becomes fullscreen

✅ **Do:** Show one dialog at a time and keep the Tertiary action a link  
❌ **Don't:** Open a dialog from another dialog, or turn the Tertiary action into a button

✅ **Do:** Remove the opening animation when the user prefers reduced motion  
❌ **Don't:** Play the slide-down animation regardless of user preferences

---

## Motion & Animation accessibility rules

In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”
These two main criteria address different issues:

**Pause, Stop, Hide - WCAG 2.2.2**
This concerns moving, blinking, scrolling, or automatically updating content.
The question to ask is: does the animation start automatically and meet the criterion’s conditions?
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.
The two criteria should therefore be evaluated independently.

**Reduced Motion (Animation from Interactions) - WCAG 2.3.3**
This primarily concerns motion-based animations triggered by user interaction.
The question to ask is: is the movement essential to the functionality or to the information being conveyed?
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Modal:

**Pause, Stop, Hide**
Modal animations are triggered by a user action and do not generally fall within the scope of this criterion.
However, if a modal contains moving, blinking, scrolling, or automatically updating content, that content must be evaluated separately.

**Reduced Motion**
The appearance and closing animation of a modal are not essential to its functionality or to understanding its content.
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.
Default: animated appearance and closing
Reduced Motion: instantaneous appearance and closing

---

# Specs

## States

🚧 Missing from source: States section in modal_dialog_overview.md

---

## Layout and spacing

### Size: Default

**Modal dialog**

![modal_dialog@spec_layout_spacing_size_default_01](../../images/modal_dialog@spec_layout_spacing_size_default_01.png)

**Modal dialog**

![modal_dialog@spec_layout_spacing_size_default_02](../../images/modal_dialog@spec_layout_spacing_size_default_02.png)

**Close button**

![modal_dialog@spec_layout_spacing_size_default_03](../../images/modal_dialog@spec_layout_spacing_size_default_03.png)

**Header**

![modal_dialog@spec_layout_spacing_size_default_04](../../images/modal_dialog@spec_layout_spacing_size_default_04.png)

**Subtitle container**

![modal_dialog@spec_layout_spacing_size_default_05](../../images/modal_dialog@spec_layout_spacing_size_default_05.png)

**Title container**

![modal_dialog@spec_layout_spacing_size_default_06](../../images/modal_dialog@spec_layout_spacing_size_default_06.png)

**Text container**

![modal_dialog@spec_layout_spacing_size_default_07](../../images/modal_dialog@spec_layout_spacing_size_default_07.png)

**Footer**

![modal_dialog@spec_layout_spacing_size_default_08](../../images/modal_dialog@spec_layout_spacing_size_default_08.png)

### Size: Small

**Modal dialog**

![modal_dialog@spec_layout_spacing_size_small_01](../../images/modal_dialog@spec_layout_spacing_size_small_01.png)

**Modal dialog**

![modal_dialog@spec_layout_spacing_size_small_02](../../images/modal_dialog@spec_layout_spacing_size_small_02.png)

**Close button**

![modal_dialog@spec_layout_spacing_size_small_03](../../images/modal_dialog@spec_layout_spacing_size_small_03.png)

**Title container**

![modal_dialog@spec_layout_spacing_size_small_04](../../images/modal_dialog@spec_layout_spacing_size_small_04.png)

**Text container**

![modal_dialog@spec_layout_spacing_size_small_05](../../images/modal_dialog@spec_layout_spacing_size_small_05.png)

**Footer**

![modal_dialog@spec_layout_spacing_size_small_06](../../images/modal_dialog@spec_layout_spacing_size_small_06.png)

### Max height: True

**Modal dialog**

![modal_dialog@spec_layout_spacing_max_height_true_01](../../images/modal_dialog@spec_layout_spacing_max_height_true_01.png)

**Modal dialog**

![modal_dialog@spec_layout_spacing_max_height_true_02](../../images/modal_dialog@spec_layout_spacing_max_height_true_02.png)

**Body**

![modal_dialog@spec_layout_spacing_max_height_true_03](../../images/modal_dialog@spec_layout_spacing_max_height_true_03.png)

**Text container**

![modal_dialog@spec_layout_spacing_max_height_true_04](../../images/modal_dialog@spec_layout_spacing_max_height_true_04.png)

**Footer**

![modal_dialog@spec_layout_spacing_max_height_true_05](../../images/modal_dialog@spec_layout_spacing_max_height_true_05.png)

---

# Accessibility 👈🤖

## Accessibility intro

Modal dialog components must meet WCAG 2.2 Level AA standards so that all users can perceive the dialog, understand its purpose, operate its controls and leave it using keyboard, pointer or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

A modal dialog interrupts the page and takes over interaction. Users of assistive technologies must be told that a dialog has opened, must be kept inside it while it is open, and must be returned to where they were when it closes.

### Key Challenges

- Focus must move into the dialog when it opens and stay inside it until it closes
- The page behind the backdrop must be unavailable to keyboard and screen reader users, not only visually dimmed
- Visual action order on tablet and desktop can differ from the logical order Primary → Secondary → Tertiary
- Long content, sticky actions and zoom must not hide the title, the actions or the focused element

### Critical Success Factors

1. Expose the dialog with `role="dialog"` and `aria-modal="true"`, named by its always-visible title through `aria-labelledby`, and make the page behind inert (WCAG 4.1.2)
2. Move focus into the dialog on opening, keep Tab and Shift+Tab cycling inside it, and return focus to the triggering element on closing (WCAG 2.4.3)
3. Always provide a keyboard-operable way to dismiss the dialog, including the Escape key, unless the flow intentionally prevents dismissal
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
- [ ] **Reflow and zoom**: At 200% zoom and 320 px width the content scrolls inside the dialog and the actions remain reachable

### Content

- [ ] **Clear title**: ❌ "Warning" / ✅ "Delete this document?" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
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

- [ ] Verify the opening and closing animation is removed when Reduced Motion is enabled, and that a static backdrop does not close the dialog on outside click

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
