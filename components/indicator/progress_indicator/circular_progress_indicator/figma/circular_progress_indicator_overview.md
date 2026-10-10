## Definition

A circular indicator shows the progress of a task using a circle. It can show a specific value (determinate) or just that something is in progress (indeterminate). Useful when you need more visual focus or when space is limited.

---

## Progress type

Select the type of progress indicator based on whether progress can be measured and how long the user is expected to wait.
• Instant (< 200ms)
Do not display any indicator.
• Short (200ms – 5s)
Use an indeterminate indicator when progress cannot be measured.
• Long (> 5s)
Use a determinate indicator when progress can be measured and communicated (with progress description).

**`Indeterminate`** Shows that a process is active without indicating exact progress. Used when the system cannot determine how long the task will take. Communicates that the system is working, even without precise data, and prevents users from thinking the interface is frozen. For long loading times (over 5 seconds), additional context must be provided. This helps inform users about the system state, reduces uncertainty, and prevents the interface from being perceived as unresponsive. User feedback and understanding of the system state (WCAG 2.2.2, 4.1.2).
• The duration is unknown or depends on external factors (e.g. waiting for server response)
• Progress cannot be reliably calculated

**Transitions** An indeterminate progress indicator may transition into a determinate state once sufficient information becomes available to calculate and communicate progress.

**`Determinate`** Shows the exact progress of a task, usually as a percentage from 0% to 100%. Provides clear and measurable feedback, helping users understand how long the task will take and reducing uncertainty. Use determinate indicators whenever possible. Avoid indeterminate when progress can be measured.
• The progress value is known (e.g. file upload, installation, data sync)
• The system can estimate completion time or percentage

---

## Progress (Determinate state only)

Controls whether the progress indicator uses motion to show activity.
Animation helps communicate that the system is actively processing.

The animated property is only available for the Determinate variant.
In the Indeterminate variant, animated = false is not supported and is therefore not exposed as a component option. Indeterminate progress indicators are specifically designed to communicate ongoing activity through motion.

**`True`** The progress indicator is static and does not move. Used to show a fixed state without suggesting ongoing activity.
• Showing a fixed value (e.g. 50%, 100%)
• Reducing motion (accessibility or low distraction)

**`False`** The progress indicator moves to show that a process is ongoing. Used to indicate active system work, especially when progress is changing or unknown (0% → 100%).
• The system is processing and needs to show activity
• It is important to reassure users that the system is not stuck

---

## Status

Progress indicators can use different statuses depending on the meaning of the process they represent. Status colors should communicate the nature of the operation, not its completion percentage.

**`Non-functional`** Non-functional statuses are used for standard progress indication without conveying any semantic feedback. They simply communicate that a process is running or progressing.

**`Neutral`** Default status used when progress has no specific semantic meaning. Suitable for generic loading, processing, synchronization, or background tasks where only the completion progress needs to be communicated.

**`Accent`** Used to highlight primary or brand-related actions. Recommended for user-initiated operations such as uploads, downloads, installations, onboarding, or other key experiences where reinforcing the brand identity is appropriate.

**`Functional`** Functional statuses communicate additional semantic meaning about the operation being performed. They should only be used when the process itself represents a meaningful system state.

⚠️ Functional statuses must not be communicated by colour alone.

When Positive, Info, Warning or Negative is used, the same meaning must be available through visible text in the parent context and through an accessible status description.

The progress indicator colour communicates the nature of the process, while the text explains the actual state.

**`Negative`** Indicates progress related to an error, recovery, cancellation, or failure. Use only when the progress itself communicates a negative operation, such as rolling back changes, removing content, or recovering from an error.

**`Positive`** Indicates successful progress or a process leading to a successful outcome. Use for confirmation, completed validations, successful synchronization, or other positive system operations.

**`Info`** Indicates informational or system-related processes. Use for background synchronization, data retrieval, initialization, or informational operations that are neither positive nor negative.

**`Warning`** Indicates progress related to an operation that requires user attention or should be monitored. Use when the process involves caution, validation, or potentially disruptive actions.

---

## Animated (for Determinate state only)

Controls whether the progress indicator uses motion to communicate progress.

The Animated property is available only for the Determinate variant. Indeterminate progress indicators always rely on animation and therefore do not expose this property.

**`True`** The progress indicator uses animation to communicate changes in progress. Use when progress updates over time and motion helps users understand that the process is actively advancing.
• **Start animation** Controls how the progress indicator appears when it is first displayed.
  • **`True`** The progress indicator animates from 0% to the current progress value when the component enters the screen. Use when introducing a new process and providing a smooth visual transition (for example, 0% → 50%).
  • **`False`** The progress indicator immediately displays the current progress value without an introductory animation. Use when the progress value is already known or when restoring an existing process (for example, 50%).

**`False`** The progress indicator remains static and does not animate. Use when the component represents a fixed progress value rather than an actively changing process.

---

## Gap size

Controls the size of the gap between the progress indicator and the track.

**`Default`** Uses the standard gap size. Recommended for most use cases, providing balanced spacing and optimal visual clarity.

**`Small`** Reduces the gap between the progress indicator and the track. Use when a more compact appearance is preferred or to better align with specific brand styles and visual directions.

---

## Rounded corner

**`True`** Used when the visual language follows the standard rounded-corner artistic direction. It is also commonly used as an atomic element within components that do not rely on twisted corner radius.

**`False`** Used when the visual language relies on twisted corner radii. This can be applied at component level or selected as part of a brand's visual identity to ensure consistency with its design language.

---

## Track

**`True`** Use it when the indicator is shown on its own and needs a clear structure. The track helps define the full range of progress and makes the value easier to read (for determinate variant).

**`False`** Use it when the indicator is embedded inside another component (e.g. button, tag, toast). Also use it when a more minimal and lightweight appearance is needed.

---

## Helper text

Controls whether additional text is displayed with the progress indicator.
Helper text can provide context about the process or show the current progress value.
• Helper text should be short, specific.
• For indeterminate progress, use action-oriented labels with progressive verbs, such as Verifying identity or Connecting to server.
• Do not display numbers or percentages when the completion time is unknown.
• An ellipsis (…) may be added when the process is expected to complete within one or two seconds.
• For determinate progress, display the current completion status using a percentage (40% or 40% complete) or, when relevant, a step indicator (Step 3 of 5).
• If the process takes longer than expected, update the message to reassure users, for example Still verifying your identityor This may take a few minutes.
• In the French version, a non-breaking space must always be inserted between the number and the percent sign (40 %).

**Helper text**
**`True`** Displays helper text alongside the progress indicator.
**`False`** No helper text is displayed.

**Percentage (Determinate states only)**
**`True`** Shows the current value (e.g. “0%”). Used with determinate progress only.
**`False`** Text explains what is happening (e.g. “Uploading files”)

**Percentage + Description (Determinate states only)** Shows the current value (e.g. “0%”). Used with determinate progress only.
**`True`** Displays both the percentage and a short description.
**`False`** Displays the percentage only.

**Space before % (Determinate states only)** Controls whether a space is inserted between the number and the percent sign.
**`True`** Displays a space before the percent sign (e.g. 40 %)
Languages such as English, Spanish, and Italian typically do not use a space before the percent sign.
**`False`** Displays the percent sign immediately after the number (e.g. 40%) Use this property according to the typographic conventions of the language used in the interface.
Languages such as French, Russian, German, Polish, and many other European languages require a space before the percent sign.

---

## User zoom and responsiveness

The circular progress indicator must scale proportionally with user zoom and remain clear and readable in all contexts.
The component should preserve its visual structure and proportions regardless of where it is used (standalone or embedded in another component).

**Behavior**
• The loader must scale proportionally with user zoom. Resizing must never be blocked
• The shape, stroke thickness, and spacing must remain consistent at all zoom levels
• The component must remain visually balanced and recognizable at any size
• The loader must not become distorted, pixelated, or clipped

**Layout**
• The component should adapt to its container without breaking its proportions
• When embedded (e.g. button, tag, toast), it must align with surrounding elements while keeping its original ratio
• The component must not stretch to fill available space

---

## Screen Reader

Designing a progress indicator is not only about showing a progress. It is also essential to define what assistive technologies, such as screen readers, should announce to users.

Screen readers should announce the same essential information that sighted users perceive visually: what is happening, how far the process has progressed, and what remains.

**Note** Helper text is not included as part of this component. However, depending on the context in which the progress indicator is used, additional descriptive text may be required at the parent component level to provide users with meaningful context about the current process.

**`Determinate`** The system knows the exact progress value, and the loading indicator is animated. Announce the purpose of the progress indicator first (what the system is doing), followed by the current stage of completion (such as a step number or percentage), and avoid reading long sequences of individual values (for example, 1, 2, 3, 4, 5, 6) by grouping progress into clear and meaningful milestones, ideally in a limited number of steps such as 0 to 10, to reduce cognitive load and improve comprehension for screen reader users.
Recommended Screen Reader Announcement
• “Identity verification, step 1 of 2”
• “Uploading file, 50 percent complete”
• “Progress, 50 percent complete”

**`Indeterminate`** The exact progress is unknown, and the indicator is animated continuously.
Recommended Screen Reader Announcement
• “Connecting to server, please wait”

---

## Rich text

Text should stay plain. No bold, italic, or other rich text styles.
In a loading context, text is short and functional. It is meant to be read quickly, not styled.
Additional formatting does not add value and can make the content harder to scan.

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

Concrete application to the Progress Indicator:

**Pause, Stop, Hide**
When an animated loader starts automatically and remains active for more than 5 seconds, the criterion must be taken into account.
Two approaches can be considered:
• Use a static indicator directly (such as an hourglass icon), accompanied, where possible, by descriptive text such as “Loading…”.
• Use the animated loader for a maximum of 5 seconds, then replace it with a static indicator accompanied, where possible, by descriptive text.

**Reduced Motion**
Loader animation is generally not essential to conveying the information that loading is in progress.
When Reduced Motion is enabled, the animated loader should therefore be replaced with a static loading indicator (such as an hourglass icon, for example) and, when relevant, with a text alternative such as “Loading…”.
The loading state must remain understandable without relying on animation.

In both cases, the loading status must remain understandable and, when relevant, be exposed to assistive technologies (e.g. through a vocalized label).

---

## Accessibility

**Usage without vision**

The progress indicator exposes its purpose, type and current state programmatically.
Assistive technologies must be able to identify the component as a progress indicator and understand which process it represents.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The progress indicator has an accessible name that identifies the affected process.
Use a specific name such as “Uploading invoice”, “Activating eSIM” or “Identity verification” rather than the generic name “Progress” when the context is not already clear.
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

A determinate progress indicator exposes its minimum, maximum and current values.
The typical range is 0 to 100. When the visual value represents another measurement, expose a meaningful equivalent such as “Step 3 of 5” or “66 GB of 100 GB used”.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

An indeterminate progress indicator does not expose a fabricated current value.
Communicate that the process is in progress, but omit the current percentage when completion cannot be calculated.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Visible helper or contextual text is programmatically associated with the progress indicator.
Keep supporting text outside the semantic progressbar element and associate it as its accessible name or description.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

The component does not move keyboard or screen-reader focus when it appears or updates.
Progress information is announced without interrupting the user’s current task.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Progress updates are not announced for every visual frame or percentage change.
Announce the beginning of the process, meaningful milestones when necessary, and the final result. Avoid repeated announcements such as 41%, 42%, 43% that create screen-reader noise.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

Completion, failure or interruption is announced once as a meaningful result.
Replace the loading message with a clear status such as “Upload complete”, “Activation failed” or “Connection restored”.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Functional statuses are available through text and semantics, not only through the indicator colour.
For example, a red progress indicator must be accompanied by text explaining whether the system is cancelling, rolling back or recovering from an error.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The progress indicator is not included in the keyboard tab order.
It communicates system state but is not an interactive control. Any cancel, pause or retry action must use a separate Button component.
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

When progress applies to a specific region, the busy state is associated with that region.
Do not make the entire page unavailable to assistive technologies when only one section is updating.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

**Usage with limited vision**

The active progress indicator has a minimum contrast ratio of 3:1 against the track or adjacent background.
This is required when the graphical difference is necessary to understand the current progress value.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

The track remains distinguishable when it is necessary to understand the complete progress range.
When the track is hidden, the active indicator must still remain clearly visible against its surrounding surface.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Helper and contextual text has a minimum contrast ratio of 4.5:1, or 3:1 for large text.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Browser and operating-system zoom must not be blocked.
The component remains visible and recognisable when users increase interface or text size.
WCAG 2.1 — 1.4.4 Resize Text, Level AA

Supporting text wraps when required.
The layout must expand vertically rather than clipping, overlapping or truncating meaningful information.
WCAG 2.1 — 1.4.4 Resize Text, Level AA
WCAG 2.1 — 1.4.10 Reflow, Level AA

Increased line, word and letter spacing does not separate the helper text from its progress indicator or hide content.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

The indicator remains visible in high-contrast and forced-colour modes.
Do not depend on custom background colours alone to preserve the difference between the indicator and track.
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Stroke thickness and spacing remain visually distinguishable after scaling.
Do not allow the active indicator, track or gap to collapse into an indistinguishable shape.
Design-system accessibility requirement

**Usage without perception of colour**

Colour is not the only way to communicate the process status.
Positive, Info, Warning and Negative variants require an explicit text equivalent in the surrounding interface.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Progress completion is not communicated only through a colour change.
Provide an explicit completion message such as “Upload complete” rather than changing the indicator from Accent to Positive without text.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Users can distinguish the current value from the remaining track without relying only on hue.
Use sufficient contrast, position and length to communicate the progress value.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Neutral and Accent remain understandable when their colours cannot be distinguished.
The component’s purpose and value must be available through text or programmatic information.
WCAG 2.1 — 1.4.1 Use of Color, Level A

**Usage with limited manipulation or strength**

The progress indicator requires no direct user interaction.
It must not respond to click, tap, Enter, Space, dragging or gestures.
Design guidance supporting predictable interaction

The component does not receive keyboard focus.
Focus remains on the control or content that started the process unless the product intentionally moves it to another meaningful destination.
WCAG 2.1 — 2.4.3 Focus Order, Level A

Actions related to the process use separate controls.
Cancel, Pause, Retry and View details must be implemented as dedicated Buttons or Links with their own accessible names and interaction states.
WCAG 2.1 — 2.1.1 Keyboard, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The visual stop indicator is not treated as a Stop button.
It communicates an endpoint only and must not receive focus or pointer interaction.
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Starting, updating or completing progress does not unexpectedly remove the user’s current focus.
Design guidance supporting WCAG 2.1 — 2.4.3 Focus Order, Level A

**Usage with limited cognition, language or learning**

Use determinate progress whenever a reliable value can be calculated.
Showing an accurate value reduces uncertainty and helps users understand how much work remains.
Design guidance supporting cognitive accessibility

Do not display a fabricated percentage or estimated value.
When progress cannot be measured reliably, use the Indeterminate type and explain what is happening.
Design guidance supporting cognitive accessibility

The progress message identifies the current process.
Prefer “Uploading your invoice” or “Verifying your identity” to generic labels such as “Loading” or “Please wait”.
Design guidance supporting cognitive accessibility

Helper text is short, specific and written in familiar language.
Communicate one process and one current state. Avoid technical codes, internal system terminology or several unrelated messages.
Design guidance supporting cognitive accessibility

Long-running processes provide additional reassurance.
When the wait becomes longer than expected, update the message, for example “Still verifying your identity. This may take a few minutes.”
When the message changes dynamically:
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Do not announce every numerical update.
Use meaningful milestones, a readable current value and a clear final result to avoid cognitive and screen-reader overload.
Design guidance supporting cognitive accessibility

Functional status colours represent the current process meaning, not a predicted outcome.
Do not use Positive merely because the process is expected to succeed. Use it when the current operation or completed result is genuinely positive.
Design guidance supporting cognitive accessibility

When an indeterminate process becomes measurable, it may transition to Determinate.
Preserve the same process label and avoid presenting the transition as a new unrelated task.
Design guidance supporting cognitive accessibility

When progress reaches completion, replace the progress state with a clear result.
Do not leave a loading indicator at 100% indefinitely.
Design guidance supporting cognitive accessibility

**Usage without hearing and limited hearing**

Progress information does not depend on sound.
The process, current value, status and final result remain available visually and programmatically when audio is disabled.
Design guidance supporting non-auditory access

A completion sound does not replace the visible and accessible completion message.
Design guidance supporting non-auditory access

If vibration or audio accompanies a Warning or Negative status, the same meaning is communicated through text.
Design guidance supporting non-auditory access

**Minimize photosensitive seizure triggers**

The indicator must not flash more than three times per second or exceed the permitted flash thresholds.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Do not use flashing, rapid opacity changes or alternating status colours to communicate progress.
Design guidance supporting WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Respect the platform’s reduced-motion preference.
Continuous rotation or movement is replaced by a static or simplified state while the accessible loading message remains unchanged.
Design guidance supporting reduced-motion user preferences

The introductory Start animation is non-essential.
When reduced motion is enabled, display the current progress value immediately rather than animating from 0%.
Design guidance supporting motion accessibility

Progress animation remains smooth and predictable.
Avoid shaking, bouncing, pulsing or abrupt direction changes that do not communicate the actual progress value.
Design guidance supporting motion accessibility

Reduced motion does not remove the loading state.
Users must still receive a visible and programmatic indication that the process is active.
Design guidance supporting motion and cognitive accessibility
