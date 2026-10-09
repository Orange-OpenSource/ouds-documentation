# Guideline

## Intro 👈🤖

A side sheet is a dialog that slides in from one side of the viewport to hold a secondary task or details while the page stays in view.

---

## Definition

A side sheet, (also known as a side panel, drawer or offcanvas sidebar), is a dialog that slides in from and is anchored to the right side of the viewport. It uses a backdrop to separate the dialog from the underlying content while allowing users to maintain a clear sense of the current page. It is ideal for responsive navigation, filter menu or shopping carts.

**Key definitions**
Dialog: A temporary interface surface that focuses the user's attention on a specific task, decision, or piece of information.
→ Modal dialog: A centered dialog displayed above a backdrop.
→ Side sheet: A dialog anchored to the side of the viewport and displayed above a backdrop.
→ Fullscreen dialog: A dialog that occupies the entire viewport and follows a page-like layout without a backdrop.

---

## Best for 👈🤔

✅ Secondary tasks that keep users on the page they are working on

✅ Filters and sorting options for a list or a set of results

✅ Details of an item selected in the page, such as an order or a contact

✅ Editing a small set of related fields without leaving the page

✅ Responsive navigation on small screens, anchored to the start edge

✅ A shopping cart or a summary that users open and close while browsing

✅ Supplementary information or help related to the current page

✅ Quick actions and contextual tools related to the page content

✅ Tasks where seeing part of the page behind helps users keep their bearings

✅ Short or medium tasks: decisions that must interrupt belong in a modal dialog, complex ones in a fullscreen dialog

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Backdrop | Dark overlay, blurred or not, that separates the sheet from the page and blocks interaction with it | N |
| 2 | Container | The surface anchored to the start or end edge of the viewport, over its full height | N |
| 3 | Previous or Subtitle | A link back to the previous step of a flow, or supporting text above the title; not used together | Y |
| 4 | Title | Names the purpose of the sheet and gives it its accessible name; can be preceded by a decorative or status icon | N |
| 5 | Close button | Lets users dismiss the sheet without completing the primary action | Y |
| 6 | Description | Supporting text below the title that adds context or instructions | Y |
| 7 | Slot | Flexible area for filters, forms, lists and other custom content | Y |
| 8 | Actions | One to three actions: primary, secondary and a tertiary link; can stay sticky at the bottom | Y |

---

## Size

**`Default`** The Default size is intended for side sheet use cases that require more space to present detailed information or support a more complex interaction. It is suitable for use cases such as displaying contextual details, editing a set of related fields, presenting filters with multiple options, or showing supporting information alongside the main page content.

**`Small`** The Small size is intended for lightweight, focused side sheet use cases that require limited space and minimal interaction. It is suitable for use cases such as displaying a short summary, presenting a small set of filters or options, showing contextual information, or providing quick actions related to the underlying page.

The Size variant defines the overall width of the side sheet container and adapts the scale of its internal layout.

On mobile, the Default and Small sizes use almost the same container width. The difference between the two sizes becomes more visible from tablet and desktop breakpoints, where they follow different responsive width configurations and therefore use different container widths.

The Size variant also affects the internal scale of the side sheet. The Default and Small sizes use different typography references and internal spacing values, including both horizontal and vertical spacing, to maintain a consistent visual hierarchy and proportion at each size.

---

## size_do_&_dont 👈🤔

✅ **Do:** Choose the size from the amount of content: Default for detailed content, Small for a short summary or a few options  
❌ **Don't:** Pick Small for content that needs room to be read or edited comfortably

✅ **Do:** Keep enough of the page visible behind the sheet on tablet and desktop  
❌ **Don't:** Let the sheet cover so much of the page that users lose their context

✅ **Do:** Keep the same size for sheets of the same kind across a journey  
❌ **Don't:** Change size between two steps of the same flow

✅ **Do:** Let the size set typography and spacing together  
❌ **Don't:** Override text styles or spacing to squeeze more content into a size

✅ **Do:** Move to a Fullscreen dialog when the task needs the whole viewport  
❌ **Don't:** Let content scroll horizontally inside the sheet

---

## Placement

The Placement variant defines the edge of the viewport from which the Side sheet appears. Choose the placement according to the user's task, the content being presented, and the relationship between the Side sheet and the underlying page.

**`Start`** The Side sheet is positioned on the start edge of the viewport and slides in from the left in left-to-right (LTR) layouts. Use it for content or interactions that are naturally associated with the start side of the page, such as displaying navigation options, contextual tools, or a list of related items.

**`End`** The Side sheet is positioned on the end edge of the viewport and slides in from the right in left-to-right (LTR) layouts. Use it for contextual information and actions related to the current page or selected content, such as displaying item details, editing properties, filters, or supplementary information.

**`Top`** The Side sheet is positioned at the top edge of the viewport and slides down from the top. Use it for temporary content or interactions that benefit from a horizontal layout, such as displaying notifications, search interfaces, contextual tools, or additional controls.

WIP

**`Bottom`** The Side sheet is positioned at the bottom edge of the viewport and slides up from the bottom. Use it for short, focused interactions that are particularly suitable for touch devices, such as presenting filters, sorting options, action menus, or contextual actions.

WIP

ℹ️ Note: The Start and End placements should follow the logical direction of the interface. In right-to-left (RTL) layouts, Start corresponds to the right side of the viewport and End corresponds to the left side.

---

## placement_do_&_dont 👈🤔

✅ **Do:** Use End for details, filters, editing and supplementary information about the page  
❌ **Don't:** Open contextual details from the start edge, where users expect navigation

✅ **Do:** Use Start for navigation, tools or lists naturally tied to the start side of the page  
❌ **Don't:** Place the same kind of sheet on different edges from one page to the next

✅ **Do:** Follow the reading direction: in right-to-left layouts Start is the right edge  
❌ **Don't:** Hard-code left and right so the sheet ignores the direction of the interface

✅ **Do:** Keep the same placement across mobile, tablet and desktop  
❌ **Don't:** Move the sheet to another edge only to fit the available space

✅ **Do:** Wait for the Top and Bottom placements, still marked work in progress, before using them  
❌ **Don't:** Rebuild a top or bottom sheet from the side sheet component

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
❌ **Don't:** Make users scroll through a long list of filters to find the main action

✅ **Do:** Let actions follow the content when the sheet holds little content  
❌ **Don't:** Pin actions at the bottom of a sheet that never scrolls

✅ **Do:** Keep the same logical action order whether the actions are sticky or not  
❌ **Don't:** Reorder actions when switching between sticky and non-sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content or the focused element  
❌ **Don't:** Let the sticky footer cover content that cannot be scrolled into view

---

## Other boolean options

**`Close button`** The Close button allows users to dismiss the modal without completing the primary action.

The Close button may be hidden when the modal has a clear, visible alternative way to dismiss it, such as a single Cancel action or another explicit dismissal control. It may also be omitted when the modal represents a mandatory step in a controlled flow where dismissal is intentionally unavailable.

Avoid hiding the Close button when users may reasonably expect to dismiss the dialog without committing to an action. The modal must always provide an accessible and discoverable way to exit unless the flow intentionally prevents dismissal.

**`Previous`** The Previous option displays a navigation link above the title, aligned to the leading edge of the modal. It is intended for multi-step flows where users can navigate back to a previous step without dismissing the entire modal. It is not recommended to include both a subtitle and a “previous” link.

⚠️ Note: This setting is not available if Placement=End

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
❌ **Don't:** Hide the Close button and leave no visible way to close the sheet

✅ **Do:** Use Previous in multi-step flows to go back one step without closing the sheet, where the placement allows it  
❌ **Don't:** Use Previous to close the sheet or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the sheet

✅ **Do:** Use the Slot for filters, forms and lists, following spacing and responsive rules  
❌ **Don't:** Recreate a whole page or an application inside the sheet

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
The “alignment” variant (available from 2 actions onwards) allows you to configure the actions to be positioned either vertically or horizontally.
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.
This “alignment” variant is available whether “Sticky action” is set to True or False.

**⚠️ Accessibility (action order)**
The visual order of actions must not change their semantic or interaction order.
For screen reader and keyboard users, the implementation must preserve the following priority order:
Primary → Secondary → Tertiary

The visual order may be (if alignment=Horizontal):
Secondary → Primary
→ Tertiary

The DOM and accessibility tree should therefore expose the actions in priority order, even when CSS or layout positioning visually places the Tertiary action on the left. Do not rely on visual order alone to determine the reading or focus order.
This ensures that assistive technology users encounter actions in the same logical order as users interacting with the mobile layout.

---

## action_number_do_&_dont 👈🤔

✅ **Do:** Use a single action when there is one clear thing to do, and limit the sheet to three actions  
❌ **Don't:** Fill the sheet with choices that turn it into a complex interaction

✅ **Do:** Give the Primary action to the preferred outcome, such as "Apply filters"  
❌ **Don't:** Style two actions as Primary in the same sheet

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option such as "Reset"  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary whatever the alignment  
❌ **Don't:** Let the visual order change the DOM or focus order

✅ **Do:** Write action labels with active verbs that name the outcome  
❌ **Don't:** Use vague or passive labels such as "OK" or "Done"

---

## Backdrop blurred

**`True`** The backdrop uses a black overlay with 68% opacity combined with a background blur effect. Use this option when the underlying content should be visually de-emphasized to reinforce the modal's focus and hierarchy, or when reducing background complexity helps users concentrate on the modal content.
Background blur should not be used solely for decorative purposes. It should support the visual separation between the modal and the underlying content without reducing the perceived performance or accessibility of the experience.

**`False`** The backdrop uses a black overlay with 68% opacity and no background blur. Use this option when maintaining a clear visual relationship with the underlying page is important, or when the background content provides useful context for the modal.

---

## backdrop_blurred_do_&_dont 👈🤔

✅ **Do:** Use the blurred backdrop when a busy page beside the sheet distracts from it  
❌ **Don't:** Add blur purely as decoration

✅ **Do:** Use the plain backdrop when the page beside the sheet gives useful context  
❌ **Don't:** Blur the page when users need to refer to it while using the sheet

✅ **Do:** Keep the same backdrop setting for similar sheets in a product  
❌ **Don't:** Alternate blurred and plain backdrops at random

✅ **Do:** Keep the 68% black overlay in both settings  
❌ **Don't:** Lighten or tint the overlay to match a campaign

✅ **Do:** Check that blur does not slow the experience on low-end devices  
❌ **Don't:** Trade perceived performance for a visual effect

---

## Responsive behaviour

**Horizontal responsive behaviour**

The Side sheet width adapts to the viewport according to the selected Size variant and the responsive grid of each platform.
The Side sheet is anchored to either the Start or End edge of the viewport, depending on its placement.

Because the Side sheet is attached to the edge of the viewport, its width is defined by a combination of the grid margin and the specified number of columns. For each breakpoint, the defined column span must therefore be combined with the corresponding grid margin. For example, at the md breakpoint (736–1023 px), the Side sheet uses 7 columns + 1 grid margin for the Default size, and 6 columns + 1 grid margin for the Small size. The grid margin is applied on the side opposite to the viewport edge where the Side sheet is anchored.

The Side sheet follows the defined column spans at smaller breakpoints and progressively reduces its relative width at larger breakpoints to preserve sufficient visibility of the underlying content. At larger breakpoints, a maximum width is applied to prevent the Side sheet from becoming disproportionately wide.

| Breakpoint | Viewport width | Default | Small |
|---|---|---|---|
| 2xs | 1–389 px | 12 columns | 11 columns |
| xs | 390–479 px | 12 columns | 11 columns |
| sm | 480–735 px | 10 columns | 9 columns |
| md | 736–1023 px | 7 columns | 6 columns |
| lg | 1024–1319 px | 5 columns (max-width:460) | 4 columns (max-width:420 \| min-width:380) |
| xl | 1320–1639 px | 4 columns (max-width:520) | 3 columns (max-width:480 \| min-width:420) |
| 2xl | 1640–1879 px | 4 columns (max-width:520) | 3 columns (max-width:480 \| min-width:420) |
| 3xl | 1880+ px | 3 columns (max-width:600) | 2 columns (max-width:520 \| min-width:440) |

**Vertical responsive behaviour**

The Side sheet occupies the full available viewport height regardless of the selected Size variant or breakpoint.
Unlike the Modal dialog, the Side sheet does not use different height specifications for its Default and Small sizes. Its height always spans the full available viewport, while the Size variant only affects its horizontal width and internal layout scale.
When the Side sheet content exceeds the available viewport height, the content area becomes vertically scrollable while the Side sheet remains fixed to the viewport edge.

---

## responsive_behaviour_do_&_dont 👈🤔

✅ **Do:** Let the sheet width follow the column spans and maximum widths defined for each breakpoint and size  
❌ **Don't:** Set a fixed pixel width that ignores the grid

✅ **Do:** Add the grid margin on the side opposite to the anchored edge  
❌ **Don't:** Leave a gap between the sheet and the viewport edge it is anchored to

✅ **Do:** Let the sheet fill the full height of the viewport  
❌ **Don't:** Give the Default and Small sizes different heights

✅ **Do:** Let the content area scroll vertically when it exceeds the viewport height  
❌ **Don't:** Let the sheet itself scroll away from the viewport edge

✅ **Do:** Check both sizes at every breakpoint, including the transitions between them  
❌ **Don't:** Design the sheet for one screen size only

---

## ℹ️ Additional technical information

**Layout transformation across breakpoints**
The dialog layout may technically change between breakpoints when required by the available screen space and the interaction context.
For example, a Modal dialog may transform into a Fullscreen dialog on smaller viewports when the content or task requires more space. Similarly, a Modal dialog may transform into a Sidescreen dialog at larger breakpoints when maintaining visibility of the underlying page provides useful context.
These transformations should preserve the same task, content hierarchy, and interaction logic while adapting the presentation to the available viewport.

**Placement across breakpoints**
Although it is technically possible, the Side sheet placement should generally remain consistent across breakpoints. A Side sheet configured with a Start placement should remain anchored to the Start edge of the viewport across mobile, tablet, and desktop, and the same applies to the End placement.
Changing the placement between breakpoints should only be considered when required by a specific responsive layout or interaction pattern. In such cases, the change should be intentional and supported by a clear UX rationale rather than being used solely to accommodate available screen space.

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
When enabled, the Side sheet uses a slide-left or slide-right entrance animation rather than appearing with an immediate cut.
The Side sheet slides in from the Start or End edge of the viewport, depending on its placement, when it opens. It slides back toward the same edge when it closes. This provides a clear visual transition that helps users understand where the dialog originates from and returns to, establishing a stronger sense of spatial continuity.
Animation should respect the user's reduced-motion preferences. When reduced motion is enabled, the transition should be removed.

---

## additional_technical_information_do_&_dont 👈🤔

✅ **Do:** Always display a title that names the purpose of the sheet  
❌ **Don't:** Hide the title, even when the content is self-explanatory

✅ **Do:** Use a static backdrop when closing by accident would lose data or progress  
❌ **Don't:** Let a click outside discard a form the user is filling in

✅ **Do:** Keep the same task, content hierarchy and interaction logic when the layout changes across breakpoints  
❌ **Don't:** Change the content or the actions when a sheet becomes fullscreen on mobile

✅ **Do:** Show one sheet at a time and keep the Tertiary action a link  
❌ **Don't:** Open a sheet from another sheet, or turn the Tertiary action into a button

✅ **Do:** Slide the sheet in from, and back to, the edge it is anchored to, and remove the animation for reduced motion  
❌ **Don't:** Animate the sheet from another direction or ignore the reduced-motion preference

---

# Specs

## States

🚧 Missing from source: States section in side_sheet_overview.md

---

## Layout and spacing

### Size: Default

- Side sheet — `side_sheet@spec_layout_spacing_size_default_01`
- Modal dialog — `side_sheet@spec_layout_spacing_size_default_02`
- Close button — `side_sheet@spec_layout_spacing_size_default_03`
- Header — `side_sheet@spec_layout_spacing_size_default_04`
- Subtitle container — `side_sheet@spec_layout_spacing_size_default_05`
- Title container — `side_sheet@spec_layout_spacing_size_default_06`
- Body — `side_sheet@spec_layout_spacing_size_default_07`
- Sticky footer safe area — `side_sheet@spec_layout_spacing_size_default_08`
- Text container — `side_sheet@spec_layout_spacing_size_default_09`
- Footer — `side_sheet@spec_layout_spacing_size_default_10`

### Size: Small

- Side sheet — `side_sheet@spec_layout_spacing_size_small_01`
- Modal dialog — `side_sheet@spec_layout_spacing_size_small_02`
- Close button — `side_sheet@spec_layout_spacing_size_small_03`
- Title container — `side_sheet@spec_layout_spacing_size_small_04`
- Text container — `side_sheet@spec_layout_spacing_size_small_05`
- Footer — `side_sheet@spec_layout_spacing_size_small_06`

### Placement: End

- Side sheet — `side_sheet@spec_layout_spacing_placement_end_01`
- Header — `side_sheet@spec_layout_spacing_placement_end_02`

### Sticky action: False

- Body — `side_sheet@spec_layout_spacing_sticky_action_false_01`
- Text container — `side_sheet@spec_layout_spacing_sticky_action_false_02`
- Footer — `side_sheet@spec_layout_spacing_sticky_action_false_03`

---

# Accessibility

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

Concrete application to the Sheet:

**Pause, Stop, Hide**
Sheet animations are triggered by a user action and do not generally fall within the scope of this criterion.
However, if a sheet contains moving, blinking, scrolling, or automatically updating content, that content must be evaluated separately.

**Reduced Motion**
The appearance and closing animation of a sheet are not essential to its functionality or to understanding its content.
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.
Default: animated appearance and closing
Reduced Motion: instantaneous appearance and closing

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 28, 2026 | 1.0.0 | **Version 2.7 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
