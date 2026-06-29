## Definition

A linear indicator shows the progress of a task using a horizontal line. It can show a specific value (determinate) or just that something is in progress (indeterminate). Best used inside layouts to show progress.

---

## Progresse type

Select the type of progress indicator based on whether progress can be measured and how long the user is expected to wait.
• Instant (< 200ms)
Do not display any indicator.
• Short (200ms – 5s)
Use an indeterminate (loading) indicator when progress cannot be measured.
• Long (> 5s)
Use a determinate (progress) indicator when progress can be measured and communicated (with progress description).

**`Determinate`** Shows the exact progress of a task, usually as a percentage from 0% to 100%. Provides clear and measurable feedback, helping users understand how long the task will take and reducing uncertainty. Use determinate indicators whenever possible. Avoid indeterminate when progress can be measured.
• The progress value is known (e.g. file upload, installation, data sync)
• The system can estimate completion time or percentage

**`Indeterminate`** Shows that a process is active without indicating exact progress. Used when the system cannot determine how long the task will take. Communicates that the system is working, even without precise data, and prevents users from thinking the interface is frozen. For long loading times (over 5 seconds), additional context must be provided. This helps inform users about the system state, reduces uncertainty, and prevents the interface from being perceived as unresponsive. User feedback and understanding of the system state (WCAG 2.2.2, 4.1.2).
• The duration is unknown or depends on external factors (e.g. waiting for server response)
• Progress cannot be reliably calculated

**Transitions** An indeterminate progress indicator may transition into a determinate state once sufficient information becomes available to calculate and communicate progress.

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

**Non fonctionnel** Non-functional statuses are used for standard progress indication without conveying any semantic feedback. They simply communicate that a process is running or progressing.

**`Neutral`** Default status used when progress has no specific semantic meaning. Suitable for generic loading, processing, synchronization, or background tasks where only the completion progress needs to be communicated.

**`Accent`** Used to highlight primary or brand-related actions. Recommended for user-initiated operations such as uploads, downloads, installations, onboarding, or other key experiences where reinforcing the brand identity is appropriate.

**Fonctional** Functional statuses communicate additional semantic meaning about the operation being performed. They should only be used when the process itself represents a meaningful system state.

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

**`True`** Used when the visual language follows the standard rounded-corner artistic direction. It is also commonly used as an atomic element within components that do not rely on twisted corner radii.

**`False`** Used when the visual language relies on twisted corner radii. This can be applied at component level or selected as part of a brand's visual identity to ensure consistency with its design language.

---

## Track

**`True`** Use it when the indicator is shown on its own and needs a clear structure. The track helps define the full range of progress and makes the value easier to read (for determinate variant).

**`False`** Use it when the indicator is embedded inside another component (e.g. button, tag, toast). Also use it when a more minimal and lightweight appearance is needed.

---

## Stop indicator

**`True`** Displays a stop indicator at the end of the progress track.
Use when the interface benefits from a clear visual endpoint, such as upload limits, completion goals, quotas, or multi-step workflows. The stop indicator helps users understand the expected destination of the progress value.

**`False`** Hides the stop indicator and displays only the progress value.
Use when the endpoint is already obvious from the surrounding context or when a cleaner and more minimal presentation is preferred.

---

## Helper text

Controls whether additional text is displayed with the progress indicator.
Helper text can provide context about the process or show the current progress value.
• Helper text should be short, specific, and should not wrap onto multiple lines.
• For indeterminate progress, use action-oriented labels with progressive verbs, such as Verifying identity or Connecting to server.
• Do not display numbers or percentages when the completion time is unknown.
• An ellipsis (…) may be added when the process is expected to complete within one or two seconds.
• For determinate progress, display the current completion status using a percentage (40% or 40% complete) or, when relevant, a step indicator (Step 3 of 5).
• If the process takes longer than expected, update the message to reassure users, for example Still verifying your identityor This may take a few minutes.
• In the French version, a non-breaking space must always be inserted between the number and the percent sign (40 %).

**`True`** Displays helper text alongside the progress indicator.
• The process needs explanation or context
• Users need a clear progress value (determinate only)

**Percentage (Determinate states only)**
**`True`** Shows the current value (e.g. “0%”). Used with determinate progress only.
**`False`** Text explains what is happening (e.g. “Uploading files”)

**Space before % (Determinate states only)** Controls whether a space is inserted between the number and the percent sign.
**`True`** Displays a space before the percent sign (e.g. 40 %)
**`False`** Displays the percent sign immediately after the number (e.g. 40%)
Use this property according to the typographic conventions of the language used in the interface.
• Languages such as French, Russian, German, Polish, and many other European languages require a space before the percent sign.
• Languages such as English, Spanish, and Italian typically do not use a space before the percent sign.

**`False`** No helper text is displayed.
• The context is already clear from surrounding UI
• The indicator is embedded in another component
• Space is limited and layout should stay compact

---

## User zoom and responsiveness

The linear progress indicator must scale horizontally while preserving a fixed height defined by design tokens.
The component should remain clear, readable, and structurally consistent at all zoom levels and in all contexts.

**Behavior**
• The progress bar scales horizontally with its container when width is constrained
• When used in fill layouts (Auto Layout), the component must respect container bounds and must not overflow its parent
• The component must not grow beyond its container or break layout structure
• The height follows predefined tokens and must not scale freely
• The progress value must remain accurate and visually proportional at all sizes
• The component must not be distorted, stretched vertically, or clipped

**Layout**
• The component can expand to fill available width when used as a standalone element
• In constrained or embedded contexts, it must adapt to the container without exceeding it
• Vertical size is controlled by tokens (track and indicator height)
• When space is reduced, the component must scale proportionally and preserve internal spacing (e.g. between track and indicator)
• The visual ratio between track and indicator must remain consistent

**Helper text**
• The helper text must stay aligned with the progress indicator (start or center)
• Spacing between the helper text and the progress indicator must remain consistent across zoom levels.
• The text must wrap when space is limited and must not overflow the container
• The layout must expand vertically if needed to preserve readability
• Text resizing must never be blocked
• The text must not overlap, truncate, or become unreadable
• The relationship between the text and the progress indicator must remain clear

**Accessibility**
• The indicator must remain visible and distinguishable at all zoom levels
• It must support reduced motion settings when animated
• The text must remain readable at up to 200% zoom
• Contrast must meet accessibility requirements
• Progress labels must clearly communicate the ongoing process and the affected content for accessibility purposes.

---

## Screen Reader

Designing a progress indicator is not only about showing a progress bar. It is also essential to define what assistive technologies, such as screen readers, should announce to users.

Screen readers should announce the same essential information that sighted users perceive visually: what is happening, how far the process has progressed, and what remains.

**Determinate** The system knows the exact progress value, and the loading indicator is animated. Announce the purpose of the progress indicator first (what the system is doing), followed by the current stage of completion (such as a step number or percentage), and avoid reading long sequences of individual values (for example, 1, 2, 3, 4, 5, 6) by grouping progress into clear and meaningful milestones, ideally in a limited number of steps such as 0 to 10, to reduce cognitive load and improve comprehension for screen reader users.
Recommended Screen Reader Announcement
• “Identity verification, step 3 of 5”
• “Uploading file, 40 percent complete”
• “Progress, 40 percent complete”

**Indeterminate** The exact progress is unknown, and the indicator is animated continuously.
Recommended Screen Reader Announcement
• “Connecting to server, please wait”

---

## Rich text

Text should stay plain. No bold, italic, or other rich text styles.
In a loading context, text is short and functional. It is meant to be read quickly, not styled.
Additional formatting does not add value and can make the content harder to scan.
