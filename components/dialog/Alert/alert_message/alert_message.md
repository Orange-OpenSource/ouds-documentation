# Guideline

## Intro 👈🤖

Alert Message displays persistent system feedback, status updates, or required actions using semantic colors, icons, and optional actions.

---

## Definition

Alert Message is a functional, block-level alert used to display system feedback, status changes, or required actions. It includes a background, icon, semantic color, and may include a close button and/or action link. Unlike toast notifications, Alert Message does not disappear automatically and remains visible until dismissed or resolved. It is suitable for prominent, persistent, and actionable communication.

---

## Best for 👈🤔

✅ Communicating system-level status changes that require user awareness

✅ Displaying error messages that block user progress until resolved

✅ Confirming successful completion of important user actions

✅ Warning users about potential issues or upcoming service changes

✅ Providing contextual information within specific page sections

✅ Alerting users to required actions before they can proceed

✅ Showing persistent messages that must not auto-dismiss

✅ Delivering feedback related to form submissions or data processing

✅ Informing users about promotional content or feature announcements

✅ Communicating network connectivity or service availability status

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides visual boundary with semantic background color and optional rounded corners | N |
| 2 | Status icon | Communicates alert severity through semantic iconography (required for functional statuses) | Y |
| 3 | Label | Primary message text conveying the alert's main information | N |
| 4 | Description | Supplementary text providing additional context or guidance | Y |
| 5 | Action link | Text-only link enabling users to take immediate related action | Y |
| 6 | Close button | Dismisses the alert when user acknowledgment is sufficient | Y |
| 7 | Bullet list | Presents multiple related points or action items clearly | Y |

---

## State

**`Enabled`** The normal interactive/display state of the Alert Message component, when actual content (message text, optional icon or action) is present, and the component is fully styled and active.

**`Skeleton`** A placeholder state of the Alert Message component used when the content is not yet available (e.g., while loading). The component shows the correct visual structure but with placeholder elements (grey or shimmering blocks) instead of actual content.
Uses the "Skeleton" component, variant "Security marge=False".

---

## state_do_&_dont 👈🤔

✅ **Do:** Use the skeleton state during content loading to maintain layout stability and reduce perceived wait time.  
❌ **Don't:** Show an empty container or leave blank space while alert content loads.

✅ **Do:** Transition smoothly from skeleton to enabled state once content is available.  
❌ **Don't:** Display skeleton state indefinitely without a timeout or fallback behavior.

✅ **Do:** Match the skeleton dimensions to the expected content size to prevent layout shifts.  
❌ **Don't:** Use a generic skeleton size that causes jarring visual changes when content appears.

✅ **Do:** Reserve skeleton usage for situations where loading time is noticeable (>300ms).  
❌ **Don't:** Flash skeleton state for near-instantaneous content loads.

✅ **Do:** Ensure skeleton state is accessible with appropriate ARIA attributes indicating loading status.  
❌ **Don't:** Leave skeleton elements without accessible indicators for screen reader users.

---

## Layout

Alerts can be displayed with or without an action.
The placement of the action depends on the amount of content and the available screen space.
For action elements, we use the Link component with the "Text only" layout. This approach maintains visual consistency and aligns with our design system guidelines.

**🔗 Link style used as a button:** In this context, the link style is purely visual, it does not indicate navigation.
• Use <a> elements for navigation.
• Use <button> elements with the link visual style for in-app actions.

**⚠️ Non-navigational usage:** A link can be used to trigger an action rather than navigation (for example, opening a modal, revealing additional content, or executing a function). This pattern should only be applied when the link appearance is preferred, while ensuring the component remains accessible and its intent is clear.

**`Bottom action`** Used when the action is placed below the main message content. **Recommended for mobile** or narrow layouts, or when the text spans multiple lines. This vertical structure improves clarity and ensures the action remains visible after the message is read.

**`Trailing action`** Used when the action is positioned to the right of the message. Best suited for wider layouts or short, single-line alerts where horizontal alignment keeps content compact and balanced.

**`Without action`** Used when no user action is required. Ideal for informational alerts that simply convey status or feedback without any interaction.

---

## layout_do_&_dont 👈🤔

✅ **Do:** Use bottom action layout on mobile devices and narrow viewports to ensure readability.  
❌ **Don't:** Force trailing action layout on small screens where content becomes cramped.

✅ **Do:** Use trailing action layout for short, single-line alerts on desktop to maintain compact horizontal alignment.  
❌ **Don't:** Use trailing action layout when alert text spans multiple lines, as this creates visual imbalance.

✅ **Do:** Choose the without action layout for purely informational messages requiring no user response.  
❌ **Don't:** Include unnecessary actions on every alert just for visual consistency.

✅ **Do:** Use `<button>` elements styled as links for in-app actions that don't navigate to new pages.  
❌ **Don't:** Use `<a>` elements for actions that trigger modals or execute functions without navigation.

✅ **Do:** Position alerts contextually near the content they relate to for better user comprehension.  
❌ **Don't:** Place alerts far from the relevant content or action that triggered them.

---

## Status

**Non fonctionnel**
Non-functional alerts are informational or decorative. They provide context or highlight content without implying a specific state, system event, or user action. These alerts are not tied to UX patterns such as success, error, or warning, and may use contextual or brand-related icons to enhance recognition or storytelling.

**`Neutral`** Used as a generic informative alert without semantic meaning or colour association.
Suitable for a wide range of contexts – such as tips, general information, or descriptive labels – where no specific feedback or urgency is required.
Appropriate for help sections, dashboards, or onboarding flows.

**`Accent`** Uses brand colours to draw attention to promotional or highlighted information while remaining non-critical.
Ideal for marketing content, announcements, or feature highlights, where you want to subtly engage users without introducing functional semantics.
Ideal for promotional banners, product updates, or customer engagement moments.

**Fonctional**
Functional alerts communicate specific system statuses, results, or user feedback.
Each variant conveys a clear semantic meaning – such as success, warning, or error – and must always be paired with its dedicated functional icon to ensure clarity and accessibility.
Other icons should not be substituted, as the semantic pairing between icon, colour, and message is essential for recognition and consistency.

Use functional alerts to inform users about state changes, confirmations, or issues that are directly connected to system logic or user actions. These messages carry functional meaning and help guide user response or acknowledgment.

**`Negative`** Communicates a critical issue or error that prevents the user from proceeding until it is resolved.
These alerts remain visible until the problem is fixed or dismissed by the user.

**`Positive`** Indicates that a task or process has been completed successfully.
These alerts reassure users and confirm that no further action is needed.

**`Info`** Used to share neutral system information or service updates that do not require immediate action.
Ideal for background processes or status messages where users simply need to stay informed.

**`Warning`** Used to draw attention to potential issues or upcoming changes that might affect the user's service or experience.
Warnings encourage awareness but typically do not block actions.

---

## status_do_&_dont 👈🤔

✅ **Do:** Use the correct semantic status to match the message's intent (e.g., negative for errors, positive for success).  
❌ **Don't:** Use warning status for error messages or info status for critical failures.

✅ **Do:** Always pair functional statuses with their dedicated icons to ensure accessibility and recognition.  
❌ **Don't:** Substitute decorative or custom icons for functional status icons.

✅ **Do:** Reserve negative status for critical issues that genuinely block user progress.  
❌ **Don't:** Overuse negative alerts for minor issues, which leads to alert fatigue.

✅ **Do:** Use neutral or accent status for non-critical informational content that doesn't require urgency.  
❌ **Don't:** Apply functional status colors to promotional or marketing content.

✅ **Do:** Ensure consistent status usage across your product to build user familiarity and trust.  
❌ **Don't:** Mix status meanings inconsistently across different screens or contexts.

---

## Rounded corner

**`False`** Use square corners for a neutral, utility-driven look.

**`True`** Use rounded corners for a softer, more approachable feel. Works well in consumer-facing journeys, emotional contexts, or brand experiences where UI elements should feel more friendly and tactile.

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Use rounded corners consistently across consumer-facing interfaces to create a friendly, approachable feel.  
❌ **Don't:** Mix rounded and square corners within the same interface without clear design rationale.

✅ **Do:** Use square corners in enterprise or utility-focused interfaces where a professional tone is preferred.  
❌ **Don't:** Apply rounded corners to alerts in formal B2B contexts where they may feel out of place.

✅ **Do:** Match alert corner radius to other components in your interface for visual consistency.  
❌ **Don't:** Use drastically different corner radii between alerts and surrounding UI elements.

✅ **Do:** Consider emotional context when choosing corner style—rounded for reassurance, square for authority.  
❌ **Don't:** Ignore the psychological impact of visual styling on user perception of message severity.

✅ **Do:** Establish a design token or guideline governing corner radius usage across alert variants.  
❌ **Don't:** Allow individual designers to choose corner styles ad-hoc without system-level guidance.

---

## Close button

The close (dismiss) button controls whether a user can remove the alert message from view.
Depending on the purpose of the alert, it may either be dismissible (True) or persistent (False).
Some alerts must remain visible to ensure users are aware of important information; others can be closed to reduce visual clutter.

**`False`** The alert does not include a close button, and therefore remains visible until the context changes (e.g., the issue is resolved, the page is refreshed, or the user completes a related task).
Example:
• The message is critical or mandatory (e.g., service disruption, required action) and must not be ignored.
• The alert reflects a state that the user must see for the duration of a task or journey. (A network outage notification that remains until connectivity is restored.)

**`True`** The alert includes a close button, allowing the user to dismiss it when they have acknowledged the message.
Example:
• The message is informational and does not require further action from the user.
• Allowing dismissal improves UX by reducing persistent visual noise.
For example, a tip "New feature launched" that the user may choose to hide.
Not all informational alerts must have close buttons, but this offers user control when appropriate.

---

## close_button_do_&_dont 👈🤔

✅ **Do:** Make alerts dismissible when the message is informational and doesn't require action.  
❌ **Don't:** Allow users to dismiss critical error alerts that block their workflow.

✅ **Do:** Keep mandatory alerts persistent until the underlying issue is resolved or context changes.  
❌ **Don't:** Force users to repeatedly see the same dismissible alert after they've acknowledged it.

✅ **Do:** Consider what happens after dismissal—should the alert reappear on next visit or stay hidden?  
❌ **Don't:** Implement dismissal behavior inconsistently across platforms or sessions.

✅ **Do:** Ensure the close button has adequate touch target size (minimum 44×44px) for accessibility.  
❌ **Don't:** Make close buttons too small or position them where they're easily triggered accidentally.

✅ **Do:** Provide visual feedback when the close button is focused or hovered for keyboard and mouse users.  
❌ **Don't:** Hide or obscure the close button in ways that prevent users from finding it.

---

## Icon

**(for Neutral and Accent only)**
Alert messages can include an icon to enhance recognition or remain icon-free when visual simplicity is preferred.
Icons help communicate context and tone but are optional for Non-functional alerts (Neutral and Accent).

**⚠️ Note:**
Functional alerts (Negative, Positive, Info, Warning) must always include a dedicated functional icon that reflects their semantic meaning.
This ensures clarity, accessibility, and consistency across all user interfaces.

**`False`** Used when the alert should appear without an icon.
Recommended for minimalist layouts or when the message content is already self-explanatory.
Works well in neutral contexts where no additional visual cue is required.

**`True`** Used when the alert includes a decorative or contextual icon to support recognition or strengthen the visual identity.
Icons can vary depending on the alert's content – for example, informational, promotional, or illustrative.

---

## icon_do_&_dont 👈🤔

✅ **Do:** Always include semantic icons for functional alerts (negative, positive, info, warning) to ensure accessibility.  
❌ **Don't:** Remove icons from functional alerts, as users rely on visual cues to quickly identify severity.

✅ **Do:** Use icons for neutral and accent alerts only when they add meaningful context or recognition.  
❌ **Don't:** Add decorative icons that don't contribute to message comprehension.

✅ **Do:** Ensure icons have sufficient color contrast and are not the sole indicator of status (use color and text too).  
❌ **Don't:** Rely only on icon color to convey meaning, as this fails users with color blindness.

✅ **Do:** Keep icon size proportional to the alert's text size for visual balance.  
❌ **Don't:** Use oversized or undersized icons that create visual hierarchy issues.

✅ **Do:** Use consistent icon styles (filled vs. outlined) that match your design system's iconography guidelines.  
❌ **Don't:** Mix icon styles within the same alert or across similar alert types.

---

## Description

Description is the optional supplementary text in an Alert Message. Use only when additional detail or guidance is needed beyond the label. It should remain short, clear and scannable, helping the user understand what happened and what they can do next.

• If you can express the message fully in the label, omit body text.
• When body text is included, limit it to one or two short sentences. This aligns with practices from major design systems: for example, the Red Hat design system recommends **1-2 sentences for the message body**. [Red Hat design system](https://ux.redhat.com/elements/alert/guidelines/?utm_source=chatgpt.com)
• **Avoid long text blocks or "long-reads" within alerts** – for detailed explanations, direct users to another view or modal. The ServiceNow "Horizon" system states that an alert message shows two lines by default, and if it exceeds two lines, provide a "Show More" link. [Horizon Design System](https://horizon.servicenow.com/workspace/components/now-alert?utm_source=chatgpt.com)
• Use plain language consistent with Orange's tone: friendly, clear, service-oriented. Avoid jargon or complex sentences. The US Web Design System emphasises "concise, human-readable language; avoid jargon and computer code." [U.S. Web Design System (USWDS)](https://designsystem.digital.gov/components/alert/?utm_source=chatgpt.com)
• Provide next-step guidance if the alert requires user action: e.g., "Try again", "Check your settings", "Contact support". If no action is required, the body text can simply explain the state.

**`False`** Label alone conveys message cleary
Example: "Payment successful."

**`True`** Label plus body text to clarify or guide – e.g., "Connection lost. Please reconnect your device to resume service."

---

## description_do_&_dont 👈🤔

✅ **Do:** Keep description text to 1-2 short sentences maximum for optimal scannability.  
❌ **Don't:** Write lengthy paragraphs or "long-reads" within alert descriptions.

✅ **Do:** Omit description entirely if the label alone clearly conveys the complete message.  
❌ **Don't:** Add redundant description text that repeats what the label already states.

✅ **Do:** Provide actionable next steps when user action is required (e.g., "Check your settings").  
❌ **Don't:** Leave users without guidance when an error requires them to take corrective action.

✅ **Do:** Use plain, jargon-free language consistent with your brand's tone of voice.  
❌ **Don't:** Include technical error codes or developer-oriented messages in user-facing alerts.

✅ **Do:** Link to detailed information elsewhere if the message requires more explanation.  
❌ **Don't:** Overload the alert component with extensive details that belong on a separate page.

---

## Bullet list

Some alerts may include a bulleted list to present multiple related points or actions clearly, rather than a single sentence or paragraph.
This boolean option (True / False) controls whether the list is shown.

• Use a bullet list when you need to present multiple items that are of equal importance, not in a specific sequential order. For example: "You need to complete all of the following:" then a list. This follows the guidance from the U.S. Web Design System for bulleted lists (use unordered lists when order isn't important). [design.va.gov+1](https://design.va.gov/content-style-guide/bulleted-lists?utm_source=chatgpt.com)
• Limit the number of items: if you have more than ~5-7 items, consider splitting the content or linking to a detailed page. Long lists reduce scannability. [design.va.gov+1](https://design.va.gov/content-style-guide/bulleted-lists?utm_source=chatgpt.com)
• Introduce the list with a lead-in sentence that contextualises the items (e.g., "You can do the following:" or "Please check these items:"). Don't start the list without context. [design.va.gov](https://design.va.gov/content-style-guide/bulleted-lists?utm_source=chatgpt.com)
• Each bullet item should be short, sentence fragment or brief statement, not full paragraphs. The goal is quick scanning. [design.cms.gov+1](https://design.cms.gov/components/alert/?utm_source=chatgpt.com)
• Do not use a bullet list for only a single item; in that case, prefer a simple sentence.

**Guidelines**
• Use up to 3–5 bullet items for optimal readability.
• Each item should be concise and parallel in structure (start with the same part of speech).
• If more detail is needed, link to a page or modal instead of overloading the alert.
• Avoid combining bullet lists with multiple paragraphs – alerts should remain brief and focused.

**`False`** The alert displays a single concise message without additional listed content.
Use this state when one clear sentence (label or body text) is enough to convey the information.
Ideal for short, self-contained alerts such as confirmations or simple feedback messages.

**`True`** The alert includes a bullet list following the label (and optional body text).
Use this state when you need to highlight multiple points, such as service features, plan details, or next steps.
Each bullet should be short and written as a clear phrase or fragment – avoid long sentences or complex structures.

---

## bullet_list_do_&_dont 👈🤔

✅ **Do:** Limit bullet lists to 3-5 items for optimal readability and quick scanning.  
❌ **Don't:** Include more than 7 bullet points; link to a detailed page instead.

✅ **Do:** Introduce the list with a lead-in sentence that provides context for the items.  
❌ **Don't:** Start a bullet list without explaining what the items represent.

✅ **Do:** Keep each bullet item short—use sentence fragments or brief statements.  
❌ **Don't:** Write full paragraphs or complex sentences as bullet points.

✅ **Do:** Use parallel grammatical structure across all bullet items (start with same part of speech).  
❌ **Don't:** Mix verb forms, noun phrases, and complete sentences inconsistently.

✅ **Do:** Use bullet lists only when presenting multiple items of equal importance.  
❌ **Don't:** Use a bullet list for a single item—write it as a simple sentence instead.

---

# Specs

## States

**`Enabled`** The normal interactive/display state of the Alert Message component, when actual content (message text, optional icon or action) is present, and the component is fully styled and active.

**`Skeleton`** A placeholder state of the Alert Message component used when the content is not yet available (e.g., while loading). The component shows the correct visual structure but with placeholder elements (grey or shimmering blocks) instead of actual content.
Uses the "Skeleton" component, variant "Security marge=False".

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.0.0 | • Component creation | Anton Astafev |
