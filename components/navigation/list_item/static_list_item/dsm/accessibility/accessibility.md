**Usage without vision**

Static list items are exposed using appropriate list semantics when they belong to a list.
Use a semantic list container and list item structure, such as <ul> and <li>, or the equivalent native platform accessibility semantics. Do not apply role="listitem" without an associated list container.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

A standalone Static list item does not need list semantics when it is not part of a collection.
Use the semantic structure that matches its actual context rather than adding a list role only to reproduce its visual appearance.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

The component remains non-interactive for assistive technologies.
Do not expose the item as a link, button, checkbox, selectable option or other control. It must not receive keyboard or screen reader focus solely because it resembles an interactive list item.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Use another list-item family when an interaction is required.
If the item navigates, opens content, changes a setting or can be selected, use the corresponding Navigation or Control list item rather than adding interactive behaviour to Static list item.
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The programmatic reading order follows the logical content order.
Recommended order: Leading content → Label → Extra label → Description → Trailing content
Visual alignment, wrapping or responsive repositioning must not create a different screen reader reading order.
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

The relationship between the label, extra label, description and trailing information is programmatically determinable.
Keep related content within the same list item and do not position visually related information elsewhere in the document structure.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Do not use heading semantics only to reproduce the visual style of the label.
Apply a heading element only when the item label is genuinely part of the page heading hierarchy. Otherwise, expose it as normal text with the appropriate typography.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Decorative leading and trailing icons are hidden from assistive technologies.
Hide an icon when it repeats information already communicated by the label, description or accompanying text. This prevents duplicate announcements such as “phone icon, Mobile plan”.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Informative icons have an equivalent text alternative.
When an icon communicates information that is not already present in visible text, provide a concise accessible equivalent. Describe the meaning, such as “Roaming included”, rather than the icon’s appearance, such as “globe icon”.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Functional status icons do not provide the only accessible indication of status.
Include the status in visible or programmatically associated text, such as “Active”, “Unavailable” or “Payment overdue”. Hide the icon from assistive technologies when the status text already communicates the same meaning.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Avatars and profile images are decorative when the person is already identified by text.
For example, when the label contains the contact’s name, an accompanying avatar should normally use an empty text alternative. Provide alternative text only when the image communicates unique information that is necessary to understand the item.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Product images and thumbnails have an accessible equivalent when they identify the listed content.
The text alternative should identify the product or content, not describe irrelevant visual details. When the label already provides the same identification, the image may be hidden from assistive technologies.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Badges and tags are included in the reading order when they communicate meaningful metadata.
Expose their visible text as part of the list item. Decorative or repeated badges should not generate duplicate screen reader output.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Trailing text includes enough context to be understood.
Values such as dates, prices, data allowances or statuses may require a programmatic prefix when their meaning is not clear from the value alone, for example “Status: Active” or “Data remaining: 2 GB”.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Separators are hidden from assistive technologies when they are purely visual.
List structure should be communicated through semantic markup rather than by announcing repeated divider elements.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Static list items do not use role="alert", role="status" or a live region by default.
Existing static content should be discovered through normal reading and navigation. Use a live region only when an external dynamic update itself needs to be announced, not simply because the information is displayed inside a list item.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

When an item’s content updates dynamically, announce only the meaningful changed information.
Do not announce the entire list repeatedly. A polite announcement may be used for non-urgent changes, such as an updated data balance. Assertive announcements are reserved for genuinely urgent information.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage with limited vision**

All text meets the minimum contrast requirement.
Labels, extra labels, descriptions, badge text, tag text and trailing values require a contrast ratio of at least 4.5:1, or 3:1 for large text.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Essential graphical information has sufficient contrast.
Informative icons, status indicators and other graphical objects needed to understand the item require a contrast ratio of at least 3:1 against adjacent colours.
Decorative graphics are not subject to this requirement, but they must not reduce the readability of nearby content.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

A separator meets non-text contrast requirements when it is necessary to distinguish adjacent items.
When spacing or another visual structure already separates items clearly, the divider may remain decorative. Do not rely on a very low-contrast separator as the only way to identify item boundaries.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Text can be resized to 200% without clipping, overlapping or losing information.
The item height must expand to accommodate the label, extra label, description and trailing content. Do not preserve a fixed height that hides text at larger settings.
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The component reflows at a viewport width equivalent to 320 CSS px without horizontal scrolling or loss of content.
Leading content, the text stack and trailing content must adapt to the available width. Information must remain available even when the item becomes significantly taller.
WCAG 2.1 — 1.4.10 Reflow, Level AA

Text spacing changes do not clip or hide content.
The component must support increased line height, paragraph spacing, letter spacing and word spacing without overlapping leading or trailing content.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

Multiline text wraps naturally.
Do not truncate essential labels, descriptions, statuses, prices, dates or account information. Avoid ellipsis when the hidden content is needed to identify or understand the item.
Design guidance supporting WCAG 2.1 — 1.4.4 Resize Text, Level AA
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The item height is content-driven rather than fixed.
Variants containing several text levels, translated content or large accessibility text settings must grow vertically while preserving the intended internal spacing.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Top alignment is used when leading or trailing content accompanies multiline text.
Aligning images, icons and metadata with the beginning of the text stack makes the association clearer when the item grows vertically.
Center alignment is better suited to short, single-line or compact content.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Trailing content does not reduce the central text area below a readable width.
On narrow screens, allow the main content to wrap, shorten non-essential metadata or move supported trailing information according to the responsive specification. Do not overlap or crop the text stack.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Leading images and thumbnails preserve their intended proportions.
Do not stretch or distort meaningful images when the item becomes taller. Their size must not prevent the text from reflowing.
Design guidance supporting visual accessibility

The component supports portrait and landscape orientations.
Content must remain readable unless a specific orientation is essential to the wider product experience.
WCAG 2.1 — 1.3.4 Orientation, Level AA

Content remains understandable in high-contrast and forced-colour modes.
Text, meaningful icons, status indicators and necessary item boundaries must remain visible when custom colours or backgrounds are replaced by system colours.
Design guidance supporting WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Do not use images of text for labels or descriptions.
Provide real text so that it can resize, reflow, translate and adapt to user preferences.
WCAG 2.1 — 1.4.5 Images of Text, Level AA

**Usage without perception of colour**

Colour is not the only method used to communicate meaning.
Statuses, availability, categories and other information require explicit text, an identifiable icon or another non-colour indication.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Status dots include a textual equivalent.
A green, orange, blue or red dot alone is insufficient. Pair it with visible or accessible text such as “Active”, “Pending”, “Information” or “Unavailable”.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Badge and tag variants remain understandable without their semantic colour.
Their text must communicate the category or status even when users cannot distinguish the background or foreground colour.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Leading and trailing icons are not distinguished only by colour.
When two icons communicate different states, use different shapes and explicit text rather than relying only on a colour change.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Muted or unavailable information is not communicated only through reduced opacity.
Add explicit wording when users need to understand that content is unavailable, inactive, expired or not applicable.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Rich text does not rely on font colour alone for emphasis.
Use the approved strong style for limited emphasis. Underlining remains reserved for interactive links, which should not normally appear inside a Static list item.
Design guidance supporting WCAG 2.1 — 1.4.1 Use of Color, Level A

**Usage with limited manipulation or strength**

Static list items are not included in the keyboard tab order.
Because the component provides information only, it must not receive focus or require keyboard interaction.
WCAG 2.1 — 2.1.1 Keyboard, Level A

The item does not respond to click, tap, Enter or Space.
Do not attach an action to the row while retaining static semantics. Use an interactive list-item component when user activation is required.
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Do not display interactive affordances on a static item.
Avoid pointer cursors, pressed states, focus rings, hover-only highlights, navigation chevrons or other visual cues that imply the item can be activated.
Design guidance supporting predictable interaction

Do not place interactive controls inside Static list item.
Buttons, links, checkboxes, radio buttons, switches and menus require an interactive list-item family with the appropriate semantics, keyboard behaviour and target size.
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

An icon must not appear actionable when it is decorative or informational.
Do not give a decorative trailing icon its own hover state, pointer cursor or focus behaviour.
Design guidance supporting predictable interaction

Information must not be available only on hover.
Static list items cannot depend on tooltips or pointer hover to reveal truncated labels, descriptions or status information.
WCAG 2.1 — 1.4.13 Content on Hover or Focus, Level AA

Responsive adaptations do not create hidden controls or overlapping hit areas.
Since the component is non-interactive, responsive layouts must preserve a clear distinction from neighbouring interactive items and controls.
Design guidance supporting motor accessibility

When interaction is added by the consuming product, the implementation must migrate to the appropriate interactive component.
Making the entire static row clickable after implementation creates a semantic mismatch that cannot be corrected through visual styling alone.
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

**Usage with limited cognition, language or learning**

Each item communicates one primary subject.
Keep the Label, Description, status, trailing information and Bottom slot content related to the same product, person, account, service or event.
Do not use one card to combine several unrelated messages merely because enough slots remain available. Humanity has already proved that available space will be filled whether or not it should be.
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

The primary information appears first.
Use a clear Label that identifies the subject or result. Place secondary metadata in the Extra label, Trailing content or Helper text.
For status-related cards, communicate the result before supporting details, for example:

“Payment failed” before the billing explanation.

“eSIM activated” before the activation details.

“5G roaming unavailable” before the destination information.
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Labels and descriptions use plain, familiar language.
Avoid internal terminology, unexplained abbreviations and overly technical status names.
Use concise sentences and state the information directly. Where complex terminology is unavoidable, provide a short explanation in the Description or Helper text.
Recommended under WCAG 2.1 AAA — 3.1.3 Unusual Words
Recommended under WCAG 2.1 AAA — 3.1.4 Abbreviations
Recommended under WCAG 2.1 AAA — 3.1.5 Reading Level

Description and Helper text serve different purposes.
Use Description to explain the primary Label. Use Helper text for additional information required to interpret the card correctly.
Do not repeat the same sentence in both properties. Avoid displaying long paragraphs in either area.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Disabled information explains its current state.
Do not rely on dimming or the property name Disabled. Use visible text that tells users whether the information is unavailable, inactive, archived or temporarily not applicable.
When useful, explain when the information may become available again.
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Negative and Warning statuses provide a useful explanation.
State what happened and, when relevant, what the user can do next.
If the card reports a form-related error, identify the error clearly and provide a correction suggestion where one is known.
Design guidance supporting WCAG 2.1 — 3.3.1 Error Identification, Level A
Design guidance supporting WCAG 2.1 — 3.3.3 Error Suggestion, Level AA

Loading information describes what is being loaded.
Do not announce only “Loading”. Use contextual wording such as “Loading mobile plan details” when an accessible loading message is required.
A Tag in the Loading state must retain meaningful text such as “Activating” or “Updating”. The loader graphic is supplementary.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

Rich text is used only to reinforce an already clear message.
Inline Strong text is supported in Description and Helper text. Use the Label/Medium/Strong token and no custom font weights.
Prefer one short Strong fragment per text block. Do not bold entire descriptions or use rich text to create a hierarchy that should have been expressed through the Label, Overline or Extra label properties.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Underlining is reserved for hyperlinks.
Do not manually underline ordinary content in the Label, Description or Helper text.
When a link is required, use the dedicated Link component in the Bottom slot. Its label must describe its destination or purpose, for example “View data usage details” rather than “Click here”, “More” or “Learn more”.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

The item behaves predictably.
Focusing or reading the card must not open content, navigate, submit data or change context.
Use consistent terminology and status icons across equivalent cards.
WCAG 2.1 — 3.2.1 On Focus, Level A
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

The Static list item does not disappear automatically.
It has no dismissible behaviour, timeout or Close button. Keep it available while the represented information remains relevant.
When temporary, dismissible or automatically disappearing information is required, use a component designed for that behaviour, such as an Alert or Toast.
Design guidance supporting WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

**Minimize photosensitive seizure triggers**

Static list items do not include animation by default.
Do not animate icons, badges, images or status indicators merely to attract attention.
Design guidance supporting motion accessibility

The component does not use flashing or rapidly alternating content.
If the wider product introduces an animated update, it must not flash more than three times per second or exceed the applicable flash thresholds.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Do not communicate a status through pulsing colour or repeated opacity changes.
Use persistent text and a stable icon instead.
WCAG 2.1 — 1.4.1 Use of Color, Level A
Design guidance supporting WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Content updates use an immediate or subtle transition.
Avoid shaking, bouncing, zooming or repeated movement when a value, badge or status changes.
Design guidance supporting motion accessibility

Respect the platform’s reduced-motion preference when transition effects are added by the consuming product.
A static presentation must remain available without animation.
Design guidance supporting reduced-motion user preferences

Loading indicators do not belong inside Static list item.
When content is still loading, use the approved skeleton or progress pattern rather than turning an informational item into an animated loading component.
Design guidance supporting motion and cognitive accessibility