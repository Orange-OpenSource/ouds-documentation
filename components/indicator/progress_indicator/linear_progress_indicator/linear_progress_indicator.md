# Guideline

## Intro 👈🤖

A linear progress indicator shows that a task is loading or advancing along a horizontal bar, by an exact amount or as ongoing activity.

---

## Definition

A linear indicator shows the progress of a task using a horizontal line. It can show a specific value (determinate) or just that something is in progress (indeterminate). Best used inside layouts to show progress.

---

## Best for 👈🤔

✅ Showing determinate progress inside a page, list, card, or form layout

✅ File uploads or downloads with measurable, reportable progress

✅ Multi-step flows where a horizontal bar communicates how far along the user is

✅ Indicating ongoing activity when the wait time cannot be measured

✅ Embedding at the top or bottom of a container, sheet, or banner

✅ Pairing progress with a short helper label or percentage

✅ Long determinate tasks (over 5 s) where percentage or step progress reassures users

✅ Full-width loading where vertical space is constrained but horizontal space is available

✅ Brand-forward or status-driven loading using Accent or functional status colors

✅ Reduced-motion contexts where a static determinate value is preferable to animation

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Track | The horizontal background line showing the full extent of the progress path | Y |
| 2 | Indicator | The filled segment that grows to represent completed (or ongoing) progress | N |
| 3 | Stop indicator | A marker at the end of the track showing the target endpoint | Y |
| 4 | Gap | The spacing that separates the indicator from the track | N |
| 5 | Helper text | Optional label or percentage shown with the bar | Y |
| 6 | Rounded cap | The end style applied to the indicator and track | Y |

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

## progresse_type_do_&_dont 👈🤔

✅ **Do:** Use a determinate indicator whenever the system can measure or estimate progress  
❌ **Don't:** Default to indeterminate when a real percentage or step count is available

✅ **Do:** Reserve indeterminate indicators for genuinely unknown wait times (e.g. server responses)  
❌ **Don't:** Show any indicator for instant operations under ~200 ms — it only flickers

✅ **Do:** Transition from indeterminate to determinate once progress becomes measurable  
❌ **Don't:** Switch types back and forth repeatedly, which makes the wait feel unstable

✅ **Do:** Pair long waits (over 5 s) with descriptive context about what is happening  
❌ **Don't:** Leave users guessing whether a long indeterminate process is still alive

✅ **Do:** Choose the type from expected duration and measurability, not visual preference  
❌ **Don't:** Mix determinate and indeterminate styles for the same task in one flow

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

## progress_determinate_state_only_do_&_dont 👈🤔

✅ **Do:** Use motion to reassure users that a determinate process is actively advancing  
❌ **Don't:** Animate a value that never changes — static content should not appear to load

✅ **Do:** Keep the indicator static when displaying a fixed, already-known value (e.g. 50%)  
❌ **Don't:** Force continuous motion when the result is frozen or complete

✅ **Do:** Favor the static option when the user has enabled reduced-motion preferences  
❌ **Don't:** Override OS reduced-motion settings with non-essential looping animation

✅ **Do:** Keep motion smooth and proportional to the actual change in progress  
❌ **Don't:** Use looping motion that implies activity where there is none

✅ **Do:** Limit motion control to the Determinate variant, as the component intends  
❌ **Don't:** Expect static behavior from Indeterminate, which always relies on motion

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

## status_do_&_dont 👈🤔

✅ **Do:** Use Neutral for generic loading where progress carries no semantic meaning  
❌ **Don't:** Apply a functional color (Positive, Negative…) to ordinary background loading

✅ **Do:** Reserve Negative for error recovery, rollback, or failure-related progress  
❌ **Don't:** Use Negative merely to draw attention to a routine process

✅ **Do:** Use Accent to reinforce brand on key user-initiated operations (uploads, onboarding)  
❌ **Don't:** Overuse Accent so that it loses its emphasis across the interface

✅ **Do:** Match the status color to the meaning of the operation, not its completion level  
❌ **Don't:** Change status color to represent percentage (e.g. green = almost done)

✅ **Do:** Pair functional statuses with text, since color alone is not an accessible signal  
❌ **Don't:** Rely solely on status color to convey success, warning, or error

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

## animated_for_determinate_state_only_do_&_dont 👈🤔

✅ **Do:** Enable animation when a determinate value updates over time  
❌ **Don't:** Animate a determinate indicator whose value is fixed and final

✅ **Do:** Use Start animation (0% → value) when introducing a brand-new process  
❌ **Don't:** Replay the intro animation when simply restoring a known, in-progress value

✅ **Do:** Set Start animation to false when the current value is already known on load  
❌ **Don't:** Delay perceived readiness with an intro animation users do not need

✅ **Do:** Keep animation tied to the Determinate variant, as Indeterminate handles its own motion  
❌ **Don't:** Expect an Animated toggle on Indeterminate — it is not exposed

✅ **Do:** Honor reduced-motion settings by allowing a non-animated determinate display  
❌ **Don't:** Make essential progress information depend only on motion

---

## Gap size

Controls the size of the gap between the progress indicator and the track.

**`Default`** Uses the standard gap size. Recommended for most use cases, providing balanced spacing and optimal visual clarity.

**`Small`** Reduces the gap between the progress indicator and the track. Use when a more compact appearance is preferred or to better align with specific brand styles and visual directions.

---

## gap_size_do_&_dont 👈🤔

✅ **Do:** Use Default gap for most cases to keep the value easy to read  
❌ **Don't:** Reduce the gap so far that indicator and track visually merge

✅ **Do:** Use Small gap for compact placements or to match a tighter brand style  
❌ **Don't:** Mix gap sizes inconsistently across the same screen or product area

✅ **Do:** Keep the gap consistent when several indicators appear together  
❌ **Don't:** Vary gap size decoratively without a functional reason

✅ **Do:** Verify the gap stays proportional after scaling or zoom  
❌ **Don't:** Let a small gap collapse at smaller sizes, hurting legibility

✅ **Do:** Choose gap size with the track shown, where the separation is most visible  
❌ **Don't:** Assume gap matters visually when the track is hidden

---

## Rounded corner

**`True`** Used when the visual language follows the standard rounded-corner artistic direction. It is also commonly used as an atomic element within components that do not rely on twisted corner radii.

**`False`** Used when the visual language relies on twisted corner radii. This can be applied at component level or selected as part of a brand's visual identity to ensure consistency with its design language.

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Use True to follow the standard rounded artistic direction  
❌ **Don't:** Mix rounded and twisted ends within a single coherent UI

✅ **Do:** Use False when the brand's visual identity relies on twisted corner radii  
❌ **Don't:** Override a brand-level corner decision at the component level without reason

✅ **Do:** Keep the corner style consistent with sibling components nearby  
❌ **Don't:** Switch corner style per instance, creating visual inconsistency

✅ **Do:** Let the corner setting cascade from brand or component context  
❌ **Don't:** Treat rounded corner as a decorative per-screen choice

✅ **Do:** Verify both stroke ends read cleanly at small sizes  
❌ **Don't:** Assume corner style is invisible — it affects perceived precision

---

## Track

**`True`** Use it when the indicator is shown on its own and needs a clear structure. The track helps define the full range of progress and makes the value easier to read (for determinate variant).

**`False`** Use it when the indicator is embedded inside another component (e.g. button, tag, toast). Also use it when a more minimal and lightweight appearance is needed.

---

## track_do_&_dont 👈🤔

✅ **Do:** Show the track for standalone determinate indicators to frame the full range  
❌ **Don't:** Hide the track when users need to judge how much progress remains

✅ **Do:** Hide the track when embedding the indicator in buttons, tags, or toasts  
❌ **Don't:** Keep a heavy track inside dense components where it adds visual noise

✅ **Do:** Use the track to improve readability of the current value  
❌ **Don't:** Rely on the track to convey progress — that is the indicator's job

✅ **Do:** Keep adequate contrast between track and indicator  
❌ **Don't:** Use a track color so close to the indicator that the value is unclear

✅ **Do:** Choose track visibility based on context (standalone vs embedded)  
❌ **Don't:** Apply one track setting everywhere regardless of placement

---

## Stop indicator

**`True`** Displays a stop indicator at the end of the progress track.
Use when the interface benefits from a clear visual endpoint, such as upload limits, completion goals, quotas, or multi-step workflows. The stop indicator helps users understand the expected destination of the progress value.

**`False`** Hides the stop indicator and displays only the progress value.
Use when the endpoint is already obvious from the surrounding context or when a cleaner and more minimal presentation is preferred.

---

## stop_indicator_do_&_dont 👈🤔

✅ **Do:** Show the stop indicator when a clear endpoint helps (quotas, limits, goals)  
❌ **Don't:** Display it for indeterminate progress, which has no defined endpoint

✅ **Do:** Use it to mark the target destination of a determinate value  
❌ **Don't:** Rely on it alone to convey what remains — pair it with the track

✅ **Do:** Hide it when the endpoint is already obvious from surrounding context  
❌ **Don't:** Add visual clutter in compact or embedded placements

✅ **Do:** Keep the stop indicator consistent with the track's color and contrast  
❌ **Don't:** Style it so subtly that it is indistinguishable from the track

✅ **Do:** Use it in multi-step workflows to signal the final step  
❌ **Don't:** Move or animate it independently of the actual progress value

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

## helper_text_do_&_dont 👈🤔

✅ **Do:** Keep helper text short, specific, and on a single line  
❌ **Don't:** Let it wrap onto multiple lines or overflow the container

✅ **Do:** Use action-oriented labels for indeterminate progress (e.g. “Connecting to server”)  
❌ **Don't:** Show a percentage or number when completion time is unknown

✅ **Do:** Show a percentage or step indicator for determinate progress  
❌ **Don't:** Leave determinate progress unlabeled when users need the value

✅ **Do:** Follow the language's convention for the space before % (40 % in French)  
❌ **Don't:** Hard-code one percent-sign spacing across every locale

✅ **Do:** Update the message to reassure users when a process runs long  
❌ **Don't:** Keep a stale label that no longer reflects the current state

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

## user_zoom_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Let the bar scale horizontally with its container  
❌ **Don't:** Let it overflow or grow beyond its parent

✅ **Do:** Keep the height fixed to design tokens  
❌ **Don't:** Scale the height freely or stretch the bar vertically

✅ **Do:** Preserve the track-to-indicator ratio and internal spacing at any width  
❌ **Don't:** Allow the indicator to distort, clip, or misalign when scaled

✅ **Do:** Keep helper text aligned and readable up to 200% zoom  
❌ **Don't:** Block text resizing or let labels overlap the bar

✅ **Do:** Respect reduced-motion settings when animated  
❌ **Don't:** Convey essential progress information through motion alone

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

## screen_reader_do_&_dont 👈🤔

✅ **Do:** Announce the purpose first, then the current stage or percentage  
❌ **Don't:** Read every incremental value (1, 2, 3…), overwhelming the listener

✅ **Do:** Group determinate progress into meaningful milestones (e.g. steps of 10)  
❌ **Don't:** Fire constant live-region updates that flood the screen reader

✅ **Do:** Provide a clear status message for indeterminate waits (“Connecting…”)  
❌ **Don't:** Leave an indeterminate process silent, implying nothing is happening

✅ **Do:** Add descriptive context at the parent level when the bar alone is ambiguous  
❌ **Don't:** Assume the indicator alone tells assistive tech what is loading

✅ **Do:** Use polite live updates so progress does not interrupt the user  
❌ **Don't:** Use assertive announcements that hijack focus on every change

---

## Rich text

Text should stay plain. No bold, italic, or other rich text styles.
In a loading context, text is short and functional. It is meant to be read quickly, not styled.
Additional formatting does not add value and can make the content harder to scan.

---

## rich_text_do_&_dont 👈🤔

✅ **Do:** Keep loading text plain and functional  
❌ **Don't:** Apply bold, italic, or other rich-text styling

✅ **Do:** Write text that can be read quickly at a glance  
❌ **Don't:** Add formatting that makes the content harder to scan

✅ **Do:** Use concise, literal wording for the process  
❌ **Don't:** Use decorative or marketing language in a loading state

✅ **Do:** Keep a consistent plain style across all progress labels  
❌ **Don't:** Mix styled and unstyled text within the same flow

✅ **Do:** Rely on the indicator, not typography, to convey progress  
❌ **Don't:** Emphasize words with color or weight to signal status

---

# Specs

## States

The linear progress indicator is non-interactive and does not expose interaction states such as hover, focus, pressed, or disabled. Its visual variations are defined by its properties (Progresse type, Status, Animated, Gap size, Rounded corner, Track, Stop indicator, Helper text).

🚧 No dedicated States section is provided in the Figma source.

---

## Layout and spacing

🚧 Content to be added

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

---

# Changelog

| Date | Number | Notes |
|------|--------|-------|
| Jun 29, 2026 | 1.1.0 | Version 2.6 of the design tokens is required for the development of this update. <ul><li>Added a new spacing token for the helper text column gap ($indicator-progress-indicator-space-column-gap). <li>Added new Helper text alignment options: Left, Center, and Right. Added Description and Progress boolean properties to control visibility. <li>Introduced Status variants, including both non-functional (Neutral, Accent) and functional (Positive, Warning, Negative, Info) statuses. Removed the Brand color boolean in favor of the new Status property. <li>Updated the Progress type and usage guidance for Deteminate and Indeterminate variants. <li>Added the Animated property for the Determinate variant to support animated progress in prototypes. <li>Added the Start animation property to control whether progress animates from 0% to the current value when the component is first displayed. <li>Added Gap size options (Default and Small) for greater visual flexibility. <li>Added the Stop indicator boolean property. It is optional and hidden by default. <li>Replaced the dedicated Rounded corner variant with a boolean property implemented as a mask, reducing the overall number of component variants.</ul> |
| May 18, 2026 | 1.0.0 | Version 2.6 of the design tokens is required for the development of this update. <ul><li>Component creation</ul> |
