### Usage without vision

The banner content, status and available actions are programmatically available to assistive technologies.  
The accessible reading order should follow the logical content order:  
Label → Description → Inline link → Action → Close button  
Visual variants such as Top, Center, Trailing or Bottom must not change this programmatic order.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A  
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

Functional banners that appear or update dynamically are announced without moving keyboard or screen reader focus to the banner. Use a polite announcement for routine information, positive confirmations and non-urgent warnings. Reserve assertive announcements for urgent failures that require immediate attention.  
A Negative visual status does not automatically require an assertive announcement. Announcement priority depends on urgency, not colour.  
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Non-functional Neutral and Accent banners should not use a live region by default.  
Promotional or contextual content should normally remain part of the page’s reading order. Announce it dynamically only when its appearance communicates a meaningful new change.  
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

A persistent global banner should not be announced again on every page or screen transition when its content has not changed. Repeated announcements can interrupt navigation and create unnecessary screen reader noise. Announce the banner when it first appears or when its meaning changes.  
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

The label and optional description are programmatically associated.  
In the Edge-to-edge layout, assistive technologies should read the label followed by the description. In the Center layout, the complete message is provided by the label because this variant does not support a description.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Functional icons are visually required for Negative, Positive, Info and Warning, but must not provide the only accessible indication of status.  
When the status is already expressed in text, hide the icon from assistive technologies to avoid duplicate announcements. If an icon communicates unique information, provide an accessible text alternative and repeat the same meaning in the banner content.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Optional icons used in Neutral and Accent banners should be hidden from assistive technologies when they are decorative. Do not announce icon names such as “heart”, “gift” or “warning triangle” when they do not add information beyond the text.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Every interactive element exposes an accessible name, role and state.  
The accessible name of an action or close button should include its visible label. Do not expose technical icon names such as “cross”, “chevron” or “link icon”.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A  
WCAG 2.1 — 2.5.3 Label in Name, Level A

Use the correct semantic element for the action:  
Use an <a> element when the action navigates to another destination.  
Use a <button> element when the action performs an in-page or in-app operation.  
The visual link style must not determine the semantic element.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The close icon button has a clear accessible name, such as “Dismiss banner” or “Close notification”.  
When additional context is useful, include the subject of the banner, for example “Dismiss 5G availability message”.  
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

When a focused close button removes the banner, focus moves to a logical element that remains on the page.  
Do not allow focus to return unexpectedly to the beginning of the document or disappear into the page body.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

In the Loading state, the loading status is available as text and is not communicated by animation alone.  
The loading indicator may be hidden from assistive technologies when the message already communicates the operation, for example “Activating your eSIM…”.  
When loading completes, announce the meaningful result once. Do not repeatedly announce spinner updates or decorative progress changes.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A  
WCAG 2.1 — 4.1.3 Status Messages, Level AA

If an action becomes unavailable during loading, its disabled or busy state is programmatically exposed.  
Prevent repeated activation without unexpectedly moving focus away from the action.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

&nbsp;

### Usage with limited vision

Text has a minimum contrast ratio of 4.5:1, or 3:1 for large text.  
This applies to the label, description, inline hyperlink and separate action across all statuses and themes.  
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Functional icons, the close button, focus indicators and other essential graphical controls have a minimum contrast ratio of 3:1 against adjacent colours.  
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Keyboard focus remains clearly visible against both the banner background and the surrounding page.  
Focus must remain distinguishable for all functional statuses, including high-contrast backgrounds such as Negative, Positive and Warning.  
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Text can be resized to 200% without clipping, overlapping, hiding information or removing functionality.  
Actions and the close button must remain available after text enlargement.  
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The banner reflows at a viewport width equivalent to 320 CSS px without horizontal scrolling or loss of content.  
WCAG 2.1 — 1.4.10 Reflow, Level AA

Increased line height, paragraph spacing, letter spacing and word spacing do not clip or hide the label, description, link or action.  
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

The Center layout is used only when the label and optional action fit within the defined maximum content width.  
Text and action must not touch or overflow the banner edges. When space becomes insufficient, use the Edge-to-edge layout rather than reducing text size or clipping content.  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The Edge-to-edge layout is recommended for mobile, tablet and narrow desktop screens.  
The icon, text, action and close button should align with the reference screen grid and wrap without changing their logical reading order.  
Design guidance supporting WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A  
WCAG 2.1 — 1.4.10 Reflow, Level AA

Use Top alignment when the message spans several lines.  
Aligning the icon and action with the first line keeps the beginning of the message easier to identify at high zoom and on narrow screens.  
Use Center alignment for short labels and compact desktop banners.  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Use the Bottom action layout for mobile screens, multi-line messages and long CTA labels.  
The message and action must wrap independently without overlapping or forcing the action outside the visible banner area.  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The component supports both portrait and landscape orientation unless a specific orientation is essential to the service.  
WCAG 2.1 — 1.3.4 Orientation, Level AA

Information remains visible in browser high-contrast or forced-colour modes.  
Do not rely on background colour alone to preserve the banner boundary, status or visibility of controls.  
Design guidance supporting WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA  
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

&nbsp;

### Usage without perception of colour

Colour is not used as the only way to communicate the banner status.  
Functional Negative, Positive, Info and Warning banners combine: semantic colour, a dedicated functional icon, explicit text describing the status or its effect.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Do not rely only on red, green, blue or yellow to communicate the result.  
For example, use “Internet connection restored” rather than showing only a green banner with a check icon.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Neutral and Accent banners remain understandable when their background colours cannot be distinguished.  
The text itself must communicate whether the banner contains general guidance, promotional content or a featured offer.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Links remain identifiable without relying only on colour.  
Inline hyperlinks use the dedicated underline style. Underlining must not be applied to non-interactive text.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Focus, hover, disabled and loading states are not communicated by colour alone.  
Use a visible focus indicator, explicit loading text and programmatically exposed states.  
WCAG 2.1 — 1.4.1 Use of Color, Level A  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The Loading state includes a meaningful text update.  
A rotating spinner or changing colour cannot be the only indication that an operation is in progress.  
WCAG 2.1 — 1.4.1 Use of Color, Level A  
WCAG 2.1 — 4.1.3 Status Messages, Level AA

&nbsp;

### Usage with limited manipulation or strength

The action and close button can be operated using a keyboard.  
Use standard activation keys and do not require pointer gestures, dragging, swiping or precise movement.  
WCAG 2.1 — 2.1.1 Keyboard, Level A

Keyboard focus cannot become trapped inside the banner.  
Users can move to and from the banner controls using the standard keyboard navigation mechanism.  
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A

Interactive elements follow a logical focus order that matches the reading order.  
Recommended order: Inline link → Separate action → Close button  
Visual placement such as Trailing, Bottom, Top or Center must not reorder keyboard focus.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

Every keyboard-operable element has a visible focus indicator.  
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Pointer actions complete on the up-event whenever possible, allowing users to cancel an accidental press before activation.  
WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

The full visible action and close-button area is interactive.  
Do not limit activation to a small icon path, a few letters of an underlined label or another visually hidden hit area.  
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A

Provide a target size of at least 44 × 44 CSS px for the close button and separate action where possible.  
WCAG 2.1 — 2.5.5 Target Size, Level AAA

Do not make the whole banner interactive when it also contains an independent action, inline link or close button.  
Nested or overlapping interactive areas create ambiguous pointer and keyboard behaviour.  
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The action remains stable while it is focused.  
When loading starts, do not replace the focused action with a different control without preserving focus logically. Prevent duplicate submissions and expose the busy or disabled state programmatically.  
WCAG 2.1 — 2.4.3 Focus Order, Level A  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

A dismissible banner remains visible long enough for users to locate and operate the close button or action.  
Alert banners should not disappear automatically. They should remain until the underlying state is resolved or the user explicitly dismisses them when dismissal is permitted.  
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

High-priority functional banners are not dismissible when removing them would hide an unresolved condition.  
For example, “No internet connection” remains visible and disappears automatically only when connectivity is restored.  
Design guidance supporting cognitive and motor accessibility  
When dismissal is allowed, the close action does not require simultaneous input, complex gestures or sustained pressure.  
Design guidance supporting EN 301 549 — Usage with limited manipulation or strength

&nbsp;

### Usage with limited cognition, language or learning

The message uses short, direct and familiar language.  
Avoid technical codes, unexplained abbreviations, vague system terminology and unnecessarily complex sentences.  
Design guidance supporting cognitive accessibility

Each banner communicates one primary message.  
Do not combine unrelated service updates, promotions and errors inside the same banner.  
Design guidance supporting cognitive accessibility

Use a specific action label that describes the result of activation.  
Prefer “Manage your plan”, “Retry connection” or “View affected services” over “OK”, “Click here” or “Learn more”.  
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A  
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Keep the description to one or two short sentences.  
If detailed explanation is required, use the action or inline link to open another page, view or modal.  
Design guidance supporting cognitive accessibility

The Center layout uses a short, self-contained label.  
Because it does not support a description, do not use Center for messages that require detailed explanation, multiple steps or several links.  
Design guidance supporting cognitive accessibility

Use rich text sparingly.  
Highlight only one essential value or phrase with strong text whenever possible. Underline only interactive hyperlinks. Avoid combining several bold fragments, links and actions that compete for attention.  
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

In Edge-to-edge, rich text is used in the description.  
A separate action may also be provided. When an inline link and a separate action are both present, they should serve different purposes and should not duplicate the same destination.  
Design guidance supporting cognitive accessibility

In Center, rich text is used in the label.  
Use the dedicated Action option for the additional interaction. Do not simulate an inline link inside the Center label.  
Design guidance supporting cognitive accessibility

Errors are identified in text and include a recovery suggestion whenever one is available.  
For example: “SIM activation failed. Check your network connection and try again.”  
WCAG 2.1 — 3.3.1 Error Identification, Level A  
WCAG 2.1 — 3.3.3 Error Suggestion, Level AA

Loading messages describe the operation in progress.  
Prefer “Activating your eSIM…” over “Loading…” or a spinner without context.  
When the operation completes, replace the loading message with a clear success or failure result.  
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Important or actionable banners remain visible until the user has had enough time to understand and respond.  
Do not automatically dismiss errors, warnings, account restrictions or messages containing required actions.  
WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

Optional informational or promotional banners may include a close button.  
When dismissed, they should not immediately reappear during the same journey unless the information has materially changed.  
Design guidance supporting cognitive accessibility

Do not display several global banners at the same time unless each one is essential.  
Prioritise messages and avoid overwhelming users with competing system states.  
Design guidance supporting cognitive accessibility

Focusing or activating a banner control does not trigger an unexpected context change.  
WCAG 2.1 — 3.2.1 On Focus, Level A  
WCAG 2.1 — 3.2.2 On Input, Level A

&nbsp;

### Usage without hearing and limited hearing

The complete banner message is available visually and does not depend on sound.  
Status, failure, warning, loading and completion information must remain understandable with audio disabled.  
Design guidance supporting non-auditory access

Sound is never the only way to communicate connectivity loss, successful activation, a service interruption or another system state. Use visible text and the appropriate icon in addition to any optional sound or vibration.  
Design guidance supporting non-auditory access

If an audio notification accompanies the banner, it communicates the same result as the visible message.  
The audio must not introduce essential information that is missing from the label or description.  
Design guidance supporting non-auditory access

&nbsp;

### Minimize photosensitive seizure triggers

Entrance and exit animations remain short and non-essential.  
Avoid repeated bouncing, shaking, zooming or flashing transitions when the banner appears, updates or disappears.  
Design guidance supporting motion accessibility

Respect the platform’s reduced-motion preference.  
Replace movement with an immediate or simplified transition when reduced motion is enabled.  
Design guidance supporting reduced-motion user preferences