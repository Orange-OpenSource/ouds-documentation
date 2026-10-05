## Definition

A side sheet, (also known as a side panel, drawer or offcanvas sidebar), is a dialog that slides in from and is anchored to the right side of the viewport. It uses a backdrop to separate the dialog from the underlying content while allowing users to maintain a clear sense of the current page. It is ideal for responsive navigation, filter menu or shopping carts.

**Key definitions**
Dialog: A temporary interface surface that focuses the user's attention on a specific task, decision, or piece of information.
→ Modal dialog: A centered dialog displayed above a backdrop.
→ Side sheet: A dialog anchored to the side of the viewport and displayed above a backdrop.
→ Fullscreen dialog: A dialog that occupies the entire viewport and follows a page-like layout without a backdrop.

---

## Size

**`Default`** The Default size is intended for side sheet use cases that require more space to present detailed information or support a more complex interaction. It is suitable for use cases such as displaying contextual details, editing a set of related fields, presenting filters with multiple options, or showing supporting information alongside the main page content.

**`Small`** The Small size is intended for lightweight, focused side sheet use cases that require limited space and minimal interaction. It is suitable for use cases such as displaying a short summary, presenting a small set of filters or options, showing contextual information, or providing quick actions related to the underlying page.

The Size variant defines the overall width of the side sheet container and adapts the scale of its internal layout.

On mobile, the Default and Small sizes use almost the same container width. The difference between the two sizes becomes more visible from tablet and desktop breakpoints, where they follow different responsive width configurations and therefore use different container widths.

The Size variant also affects the internal scale of the side sheet. The Default and Small sizes use different typography references and internal spacing values, including both horizontal and vertical spacing, to maintain a consistent visual hierarchy and proportion at each size.

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

## Backdrop blurred

**`True`** The backdrop uses a black overlay with 68% opacity combined with a background blur effect. Use this option when the underlying content should be visually de-emphasized to reinforce the modal's focus and hierarchy, or when reducing background complexity helps users concentrate on the modal content.
Background blur should not be used solely for decorative purposes. It should support the visual separation between the modal and the underlying content without reducing the perceived performance or accessibility of the experience.

**`False`** The backdrop uses a black overlay with 68% opacity and no background blur. Use this option when maintaining a clear visual relationship with the underlying page is important, or when the background content provides useful context for the modal.

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
