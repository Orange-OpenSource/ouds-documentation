Toasts must remain perceivable, understandable, and operable for users of assistive technologies, keyboard users, and users who need additional time to read or interact with content.

&nbsp;

### Usage without vision

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

&nbsp;

### Usage with limited vision

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

&nbsp;

### Usage without perception of colour

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

&nbsp;

### Usage with limited manipulation or strength

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

&nbsp;

### Usage with limited cognition, language or learning

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

&nbsp;

### Usage without hearing and limited hearing

The complete notification is available visually and does not depend on sound.  
Design guidance supporting non-auditory access  
Sound is never the only way to communicate success, failure, warning, or information.  
Design guidance supporting non-auditory access  
Users can understand and operate the toast with audio disabled.  
Design guidance supporting non-auditory access  
If automatically played audio lasts longer than three seconds, provide a way to pause or stop it, or control its volume independently.  
WCAG 2.1 — 1.4.2 Audio Control, Level A

&nbsp;

### Minimize photosensitive seizure triggers

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