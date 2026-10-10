### Usage without vision

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

### Usage with limited vision

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

### Usage without perception of colour

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

### Usage with limited manipulation or strength

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

### Usage with limited cognition, language or learning

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

### Usage without hearing and limited hearing

Progress information does not depend on sound.  
The process, current value, status and final result remain available visually and programmatically when audio is disabled.  
Design guidance supporting non-auditory access

A completion sound does not replace the visible and accessible completion message.  
Design guidance supporting non-auditory access

If vibration or audio accompanies a Warning or Negative status, the same meaning is communicated through text.  
Design guidance supporting non-auditory access

### Minimize photosensitive seizure triggers

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
