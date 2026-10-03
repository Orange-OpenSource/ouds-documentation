## Definition

A toast is a temporary, non-modal status message that confirms an action or communicates a short system update without interrupting the user’s current task. It appears above the interface content and does not move keyboard focus when displayed.

Use a toast for brief, non-critical feedback that does not require an immediate decision.

---

## Alignment

**`Top`** Use Top alignment when the toast contains multiple lines of content, such as a label and a description. Aligning actions and leading container to the top keeps interactive elements visually associated with the primary message and improves readability.

**`Center`** Use Center alignment when the toast contains short or single-line content. Center alignment creates better visual balance and keeps the notification compact.

---

## State

**`Enabled`** Use the Enabled state to display a standard toast once the notification content is ready. The toast presents feedback immediately and allows users to interact with optional actions or dismiss it.

**`Loading`** Use the Loading state when an action or background process is still in progress. Replace the leading icon with a progress indicator to communicate that the operation has not yet completed. Once finished, update the toast to the enabled state with the final result.

---

## Action layout

Toast can be displayed with or without an action.
The placement of the action depends on the amount of content and the available screen space.
For action elements, we use the Link component with the “Text only” layout. This approach maintains visual consistency and aligns with our design system guidelines.

🔗 Link style used as a button: In this context, the link style is purely visual, it does not indicate navigation.
• Use <a> elements for navigation.
• Use <button> elements with the link visual style for in-app actions.

⚠️ Non-navigational usage: A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.

**`None`** Used when no user action is required. Ideal for informational alerts that simply convey status or feedback without any interaction.

**`Trailing`** Used when the action is positioned to the right of the message. Best suited for wider layouts or short, single-line alerts where horizontal alignment keeps content compact and balanced.

**`Bottom`** Recommended for mobile or narrow layouts, multiline messages, or actions with longer text labels. This vertical structure gives the action more space, improves readability, and ensures it remains visible after the message is read.

---

## Status

Toast statuses help communicate the nature of the feedback shown to the user.
They can be non-functional, when the message is contextual or decorative, or functional, when the message communicates a clear system result, status, or issue.

**Non-functional**
Non-functional toasts provide contextual information without implying a specific system state, result, or required user action.
They may use contextual or brand-related icons to support recognition, but the icon does not carry functional meaning.

**`Neutral`** Used for general information or contextual feedback without semantic meaning or urgency.
Suitable for tips, onboarding messages, dashboards, or descriptive feedback where no specific system response is required.

**Functional**
Functional toasts communicate a specific system status, result, or user feedback. Each variant conveys a clear semantic meaning, such as success, error, warning, or information. The icon should match the status to support recognition, consistency, and accessibility.

**`Negative`** Communicates an error or issue that prevents the action from being completed. Use it when the user needs to understand that something went wrong.

**`Positive`** Indicates that a task or process has been completed successfully.
Use it to confirm that the user action worked as expected.

**`Info`** Shares neutral system information or service updates that do not require immediate action. Use it when users simply need to stay informed.

**`Warning`** Draws attention to a potential issue or upcoming change that may affect the user’s experience. Use it when awareness is needed, but the action is not blocked.

---

## Close button

The close button controls whether users can dismiss the toast manually.
Its presence does not necessarily determine how long the toast remains visible. A toast may still disappear automatically after an appropriate duration, unless the message is important, actionable, or requires additional reading time.

**`False`** The toast does not include a close button and disappears automatically after a short duration. Use this behavior for short confirmations or status updates that do not require user acknowledgement or interaction. The message should be easy to understand at a glance.

**Use this option for:**
• brief confirmations
• simple status updates
• messages that require no action

**`True`** The toast includes a close button and remains visible until it is dismissed by the user. Use this behavior when the notification contains an action, important contextual information, or when users may need additional time to read it.

**Use this option when:**
• the toast contains an action
• the message contains important contextual information
• the content is multiline or requires more time to read
• the notification remains visible for an extended period
• users may want to remove the toast before it disappears automatically

**Automatic dismissal**
Use automatic dismissal for short, non-critical messages that do not require user interaction.

**Examples:**
• Changes saved
• Item added to favourites
• Connection restored

**Do not automatically dismiss a toast when:**
• it contains an action
• it communicates an important warning or error
• the content requires additional reading time
• the information is not available elsewhere

**⚠️ Note:**
Actionable toasts should remain visible long enough for users to reach and activate the action. Important messages should remain visible until dismissed or use a persistent component instead.

**Motion and timing**
Toasts may disappear automatically after a short period. The display duration should depend on the amount of content and whether the toast contains an action.

A single-line toast should remain visible for approximately 3 seconds.
A two-line toast should remain visible for approximately 5 seconds.
A three-line toast should remain visible for approximately 7 seconds.

The enter and exit transitions should remain short and subtle, usually 1 second.

---

## Rounded corner

Even though in Figma this rendering option is available and editable from the properties of each alert component, the configuration of this rendering option is actually transversal across the entire product/service in which the component is used.
It is therefore impossible to have one toast component set to Rounded corner=True and another set to Rounded corner=False within the same product/service.

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

## Description

Description is the optional supplementary text in an Alert Message. Use only when additional detail or guidance is needed beyond the label. It should remain short, clear and scannable, helping the user understand what happened and what they can do next.

• If you can express the message fully in the label, omit body text.
• When body text is included, limit it to one or two short sentences. This aligns with practices from major design systems: for example, the Red Hat design system recommends 1-2 sentences for the message body. Red Hat design system
• Avoid long text blocks or “long-reads” within alerts — for detailed explanations, direct users to another view or modal. The ServiceNow “Horizon” system states that an alert message shows two lines by default, and if it exceeds two lines, provide a “Show More” link. Horizon Design System
• Use plain language consistent with Orange’s tone: friendly, clear, service-oriented. Avoid jargon or complex sentences. The US Web Design System emphasises “concise, human-readable language; avoid jargon and computer code.” U.S. Web Design System (USWDS)
• Provide next-step guidance if the alert requires user action: e.g., “Try again”, “Check your settings”, “Contact support”. If no action is required, the body text can simply explain the state.

**`False`** Label alone conveys message clearly
Example: “Payment successful.”

**`True`** Label plus body text to clarify or guide — e.g., “Connection lost. Please reconnect your device to resume service.”

---

## Leading

**(for Neutral only)**
Alert messages can include an icon to enhance recognition or remain icon-free when visual simplicity is preferred.
Icons help communicate context and tone but are optional for Non-functional alerts (Neutral and Accent).

**⚠️ Note:**
Functional alerts (Negative, Positive, Info, Warning) must always include a dedicated functional icon that reflects their semantic meaning. This ensures clarity, accessibility, and consistency across all user interfaces.

**`False`** Used when the alert should appear without an icon.
Recommended for minimalist layouts or when the message content is already self-explanatory.
Works well in neutral contexts where no additional visual cue is required.

**`True`** Used when the alert includes a decorative or contextual icon to support recognition or strengthen the visual identity.
Icons can vary depending on the alert’s content — for example, informational, promotional, or illustrative.

---

## Leading container type

**(for Neutral only)**
Defines the type of content displayed before the label.

**`Icon`** Use an icon to represent an action, status, or category.

**⚠️ Note:**
For functional toasts, such as Negative, Positive, Info, or Warning, use the dedicated status icon associated with the selected semantic status.
For Neutral toasts, the icon may be contextual or decorative and is optional.

**`Image`** Use an image when richer visual identification is needed.
The image should provide useful context and remain secondary to the message content. Users must still be able to understand the toast when the image is unavailable.

---

## Image size

Defines the size of the image displayed inside the leading container.
Choose a size according to the available space, content density, and required visual emphasis. Use the same image size for similar use cases to maintain consistency across the interface.

**`Small`** Use Small when the image has low visual priority or when the available space is limited. Recommended for compact or single-line toasts.

**`Medium`** Use Medium as the default image size for most use cases. It provides a clear visual reference without competing with the text content and works well with both short and multi-line messages. Recommended for standard product or content previews.

**`Large`** Use Large when the image needs stronger visual emphasis or contains details that should remain recognisable. Recommended for messages where visual identification is important.

**⚠️ Note:**
Avoid using Large in very compact layouts or when it makes the text difficult to scan.

---

## Rounded corner Image

Defines whether the image is displayed with square or rounded corners.
The corner style should reflect the type of content and remain consistent with the visual language used elsewhere in the product.

**`False`** Displays the image with square corners.

**`True`** Displays the image with rounded corners.

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width vs full-width**
For greater flexibility, this component doesn’t have a default max-width. The max-width is applied to the text within the component.
As a result, if it is positioned across the full available width (of the screen or the container), the component’s background will stretch across the entire available surface, but the text may be limited to its max-width if the display width is larger.

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
• The text must always scale proportionally with user zoom. Text resizing must never be blocked.
• Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
• The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
• In order to preserve the minimum interactive area during user zoom out, this component have a min-width of 160px and a min-height of 48px.
• If the component doesn’t contain any interactive elements, it’s not necessary to maintain the minimum interactive area during user zooms out.
• Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
• Icons must always scale proportionally with user zoom. Icon resizing must never be blocked.
• The behaviors of the other subcomponents during user zoom are available in the corresponding documentation.

---

## Rich text

**Strong text**
• Strong text can be used sparingly within toast to highlight key information. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**Underlined text** and **hyperlink**
• Underlined text must not be used for emphasis, as it is commonly associated with links.
• If a **hyperlink** is needed within the content, the typographic reference **Label/Medium/Underline** must be used.

---

## Horizontal responsive behaviour

The toast width adapts automatically to each screen size.
On 2xs and xs, the toast takes almost the full screen width with 8 px margins on both sides. From sm onwards, its width follows the 12-column grid: 10 columns on sm, 8 on md, 6 on lg, and 4 from xl onwards.

**Web**

| Breakpoint | Viewport width | Layout constraint |
|---|---|---|
| 2xs | 1–389 px | 8 px margin |
| xs | 390–479 px | 8 px margin |
| sm | 480–735 px | 10 of 12 grid columns |
| md | 736–1023 px | 8 of 12 grid columns |
| lg | 1024–1319 px | 6 of 12 grid columns |
| xl | 1320–1639 px | 4 of 12 grid columns |
| 2xl | 1640–1879 px | 4 of 12 grid columns |
| 3xl | 1880+ px | 4 of 12 grid columns |

---

## Placement

**Mobile reference design**
• Constraints: Left & right + Bottom
• Spacing: 8 px from both screen edges and 8 px above the bottom navigation or another persistent element.
• Use this position for feedback directly related to a recent action, especially when the action happened near the bottom of the screen.
• For the sm reference, the toast width follows the grid: it spans 10 of 12 columns, instead of using fixed 8 px side margins like 2xs and xs.

⚠️ The toast must not cover important content or controls. If a floating button, navigation bar, or sticky element is already in the same area, place the toast above it or use another position.
⚠️ On mobile reference, the toast takes almost the full screen width and does not follow the grid, unlike on other screen references.

**Tablet reference design**
Maximum width:
md 8 of 12 grid columns
lg 6 of 12 grid columns

**Top center**
• Constraints: Center + Top
• Spacing: 16 px from the top of the viewport.
Align the toast with the four central grid columns.
• Use this position as the default for narrow web layouts, tablets, forms, and pages with a centered content column.
It keeps the message visually connected to the main task without making it feel like a separate system notification.

**Bottom center**
• Constraints: Center + Bottom
• Spacing: 24 px from the bottom of the viewport.
Align the toast with the four central grid columns.
• Use this position when the message is directly related to an action performed near the bottom of the page. It is suitable for brief action feedback, such as confirming that a comment was added or an item was moved.

**Desktop/Desktop Large reference design**
Maximum width: 4 of 12 grid columns

**Top center**
• Constraints: Center + Top
• Spacing: 16 px from the top of the viewport.
Align the toast with the four central grid columns.
• Use this position for centered layouts, forms, checkout flows, or focused tasks with a clear central content area.
Use it as a  default desktop position.

**Top right**
• Constraints: Right + Top
• Spacing: 16 px from the top.
Align the toast with the four rightmost grid columns. Its right edge must align with the last grid column.
• Use this as the default desktop position for system feedback, save confirmations, uploads, and background process updates.

**Bottom center**
• Constraints: Center + Bottom
• Spacing: 32 px from the bottom of the viewport.
Align the toast with the four central grid columns.
• Use this position when the message is directly related to an action performed near the bottom of the page. It is suitable for brief action feedback, such as confirming that a comment was added or an item was moved.

**Bottom right**
• Constraints: Right + Bottom
• Spacing: 32 px from the bottom of the viewport.
• Align the toast with the four rightmost grid columns. Its right edge must follow the grid boundary and keep the responsive layout margin from the viewport edge. Use this position when the top-right area is occupied or when the product already uses a consistent bottom-right notification pattern.

⚠️ Avoid it when this area contains a chat widget, help button, floating action button, or sticky panel.

---

## Interaction and stacking

**Default behaviour**
• Display only one toast at a time.
• When several notifications are triggered, place them in a queue. The currently visible toast must complete its exit transition before the next toast enters. Entrance and exit animations must not overlap.
• This sequential behaviour reduces visual interruption, prevents content from being obscured and makes each message easier to identify.

**⚠️ Multiple visible toasts**
Displaying several toasts at the same time is not recommended. A stack can interrupt the user, obscure interface content and make important messages harder to notice.

Maintain an 8 px gap between each toast in the stack.

When a stack is necessary:
• display a maximum of three toasts
• order them according to their priority
• keep any additional notifications in the queue
• do not display repeated messages of the same type simultaneously
• ensure that the stack does not cover navigation, focused elements or important controls
• prefer a single visible toast on mobile whenever possible

A fourth notification must remain in the queue until a visible toast is dismissed or disappears.

---

## Priority queue

• A higher-priority toast is displayed before a lower-priority toast.
• When several notifications have the same priority, display them in the order in which they were triggered. This is a first in, first out queue.
• Before displaying a queued toast, verify that its information is still relevant. Do not display outdated confirmations or messages that have already been replaced by a newer system state.

**Stack behaviour**
The highest-priority toast remains closest to the placement edge.
• For top positions, the stack grows downwards.
• For bottom positions, the stack grows upwards.
• A fourth toast remains in the queue until space becomes available.

| Priority | Toast type | Auto-dismiss | Behaviour |
|---|---|---|---|
| 1 | Actionable Negative | No | Takes priority over every other toast. A visible lower-priority toast may be interrupted and returned to the queue if it is still relevant. |
| 2 | Negative | No by default | Appears before Warning, Positive, Info and Neutral notifications. Messages of the same priority follow the queue order. |
| 3 | Actionable Warning | No | Appears before non-actionable warnings and all lower-priority statuses. |
| 4 | Warning | No by default | Appears before Positive, Info and Neutral notifications. Auto-dismiss may only be used when the information is available elsewhere. |
| 5 | Actionable Positive | No | Remains visible until the user performs the action or dismisses the toast. |
| 6 | Actionable Info | No | Remains visible until the user performs the action or dismisses the toast. |
| 7 | Actionable Neutral | No | Remains visible until the user performs the action or dismisses the toast. |
| 8 | Positive | Optional | Waits behind actionable, Negative and Warning notifications. Combine repeated confirmations whenever possible. |
| 9 | Info | Optional | Waits behind higher-priority notifications. Do not interrupt an important or actionable toast. |
| 10 | Neutral | Optional | Uses the lowest queue priority. It may be discarded when the information is no longer relevant. |

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

Concrete application to the Toast:

**Pause, Stop, Hide**
A toast that appears automatically and remains visible for more than 5 seconds may fall within the scope of this criterion, depending on its behavior.
If the toast contains moving, blinking, scrolling, or automatically updating content that meets the criterion's conditions, users must be able to pause, stop, or hide it.
For automatically disappearing toasts, it is recommended to provide sufficient time for users to perceive and read the message. If the toast remains visible for more than 5 seconds and its content meets the criterion's conditions, an appropriate mechanism to pause, stop, or hide the content must be provided.

**Reduced Motion**
The animated appearance and closing of a toast are not essential to conveying the notification itself.
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.
The notification itself must remain perceivable and understandable without relying on animation.
Default: animated appearance and closing
Reduced Motion: instantaneous appearance and closing

---

## Accessibility

Toasts must remain perceivable, understandable, and operable for users of assistive technologies, keyboard users, and users who need additional time to read or interact with content.

**Usage without vision**

The toast message and its status are programmatically announced without moving keyboard or screen reader focus to the toast.
WCAG 2.1 — 4.1.3 Status Messages, Level AA
Routine confirmations and informational messages use a polite announcement. Assertive announcements are reserved for urgent errors requiring immediate attention.
WCAG 2.1 — 4.1.3 Status Messages, Level AA
Interactive elements expose their correct accessible name, role, and state.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A
The close button has a descriptive accessible name, such as “Dismiss notification”, rather than the name of its icon.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A
An action uses button semantics when it performs an action and link semantics when it navigates to another location.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A
Decorative icons and images are hidden from assistive technologies.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
Meaningful images provide equivalent information in the label, description, or accessible alternative.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
When a Loading toast changes to a completed state, the meaningful result is announced without repeatedly announcing decorative progress updates.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage with limited vision**

Text has a minimum contrast ratio of 4.5:1, or 3:1 for large text.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA
Functional icons and controls have a minimum contrast ratio of 3:1 against adjacent colours when they are required to identify a status or control.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA
Focus indicators remain clearly visible against the toast and surrounding content.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA
Text can be resized up to 200% without clipping, overlapping, or losing information or functionality.
WCAG 2.1 — 1.4.4 Resize Text, Level AA
The toast reflows at a viewport width equivalent to 320 CSS px without horizontal scrolling or loss of content.
WCAG 2.1 — 1.4.10 Reflow, Level AA
Increased line, word, letter, and paragraph spacing does not clip or hide the content.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA
Labels, descriptions, actions, and the close button remain available when content wraps onto multiple lines.
WCAG 2.1 — 1.4.10 Reflow, Level AA
The toast does not completely cover the element currently receiving keyboard focus.
WCAG 2.2 — 2.4.11 Focus Not Obscured (Minimum), Level AA

**Usage without perception of colour**

Colour is not used as the only way to communicate the toast status.
WCAG 2.1 — 1.4.1 Use of Color, Level A
Negative, Positive, Info, and Warning statuses combine colour with a dedicated icon and explicit text.
WCAG 2.1 — 1.4.1 Use of Color, Level A
The message remains understandable when semantic colours cannot be distinguished.
WCAG 2.1 — 1.4.1 Use of Color, Level A
Do not rely only on red, green, blue, or yellow to communicate the result.
WCAG 2.1 — 1.4.1 Use of Color, Level A
An action or link remains identifiable without relying only on colour.
WCAG 2.1 — 1.4.1 Use of Color, Level A

**Usage with limited manipulation or strength**

Actions and the close button can be operated using a keyboard.
WCAG 2.1 — 2.1.1 Keyboard, Level A
Keyboard focus cannot become trapped inside the toast.
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A
Interactive elements follow a logical focus order.
WCAG 2.1 — 2.4.3 Focus Order, Level A
Every keyboard-operable element has a visible focus indicator.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA
Pointer targets are at least 24 × 24 CSS px, or meet the spacing exception.
WCAG 2.2 — 2.5.8 Target Size (Minimum), Level AA
Prefer a target size of at least 44 × 44 CSS px for touch interfaces.
WCAG 2.2 — 2.5.5 Target Size (Enhanced), Level AAA
The complete interactive area includes the visible icon or label, not only a small area inside it.
WCAG 2.2 — 2.5.8 Target Size (Minimum), Level AA
An actionable toast does not disappear before users can reach and activate its controls.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A
Automatic dismissal pauses while keyboard focus is inside the toast.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

**Usage with limited cognition, language or learning**

The message uses short, direct, and familiar language.
Design guidance supporting cognitive accessibility
Put the result first, followed by any explanation or next step.
Design guidance supporting cognitive accessibility
Use a specific action label such as Retry, Undo, or View cart. Avoid vague labels such as OK or Click here.
Design guidance supporting clear purpose and comprehension
Do not display essential instructions only in a temporary toast.
Design guidance supporting sufficient time and information persistence
Important, actionable, or complex messages remain visible until dismissed or are also available elsewhere.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A
When a toast has a time limit, users can turn it off, adjust it, or extend it unless the limit is essential.
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A
Automatically moving or updating content that lasts longer than five seconds can be paused, stopped, or hidden unless it is essential.
WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A
When a toast reports an input error, it identifies the problem in text.
WCAG 2.1 — 3.3.1 Error Identification, Level A
When a correction is known, the toast explains how the user can recover.
WCAG 2.1 — 3.3.3 Error Suggestion, Level AA
Do not show several toasts at the same time. Queue messages to prevent visual and screen reader overload.
Design guidance supporting cognitive and screen reader accessibility
Avoid repeatedly announcing minor loading or progress changes.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage without hearing and limited hearing**

The complete notification is available visually and does not depend on sound.
Design guidance supporting non-auditory access
Sound is never the only way to communicate success, failure, warning, or information.
Design guidance supporting non-auditory access
Users can understand and operate the toast with audio disabled.
Design guidance supporting non-auditory access
If automatically played audio lasts longer than three seconds, provide a way to pause or stop it, or control its volume independently.
WCAG 2.1 — 1.4.2 Audio Control, Level A

**Minimize photosensitive seizure triggers**

The toast and its animation do not flash more than three times per second or exceed the permitted flashing thresholds.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A
Avoid flashing colours or repeated high-contrast transitions.
Design guidance supporting WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A
Entrance and exit animations remain short and non-essential.
Design guidance supporting motion accessibility
Respect the platform’s reduced-motion preference.
Design guidance supporting reduced-motion user preferences
Non-essential motion triggered by interaction can be disabled.
WCAG 2.1 — 2.3.3 Animation from Interactions, Level AAA
When reduced motion is enabled, replace movement with an immediate or simplified transition.
Design guidance supporting WCAG 2.1 — 2.3.3 Animation from Interactions, Level AAA
A Loading state does not require continuous animation to communicate that the process is still running.
Design guidance supporting motion and cognitive accessibility
