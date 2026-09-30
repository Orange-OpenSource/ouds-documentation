**Usage without vision**

The Static card item is exposed as static content, not as a button, link or selectable control.
Use a neutral container when the card only groups related content. An article element may be used when the card represents a self-contained piece of information. Do not add role="button", role="link" or tabindex="0" to the card container.
When multiple cards form a semantic list, apply list semantics to the parent collection and its direct item wrappers rather than changing the role of the card itself.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The card’s text content and relationships are available programmatically.
The Overline, Label, Extra label, Description, Helper text, trailing information and Bottom slot must remain grouped with the same card in the DOM.
A neutral card container does not require a separate accessible name. When the card is implemented as a named article, its visible Label may be referenced as its accessible name.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Content follows a logical reading order.
The programmatic order should communicate the main subject before secondary information:

Overline, when it provides necessary context.

Label.

Extra label.

Description.

Trailing value, status, Badge or Tag.

Helper text.

Bottom slot content.
Informative leading content may be announced immediately before the Label when it adds information that is not already available in text. Do not announce a trailing value before the text that explains what the value represents.
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

Decorative visual content is ignored by assistive technologies.
Icons, images, avatars thumbnails and badges that repeat information already communicated by the visible text should use an empty text alternative or be hidden from the accessibility tree.
Avoid announcements such as “green check icon” or “profile picture” when the visible content already communicates “Active” or identifies the person.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Informative visual content has an equivalent text alternative.
Apply the requirement according to the selected container type:

Icon: provide text describing its meaning when that meaning is not otherwise visible.

Image: describe the content or purpose required to understand the card.

Avatar: use the visible Label to identify the person, profile or organisation. The avatar image itself can then be decorative.

Flag: always provide the corresponding country, territory or language name as visible text.

Badge icon: provide the represented status in text rather than exposing only the icon name.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Functional statuses are communicated through meaningful text.
Positive, Info, Warning and Negative variants must include a visible status or description. The semantic icon may be hidden from assistive technologies when it repeats that text.
Neutral and Accent variants do not automatically represent a semantic status and must not be announced as success, warning or error unless their content genuinely has that meaning.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Badge counts include the meaning of the number.
Do not expose an isolated value such as “3”. The accessible information should communicate its relationship to the card, for example “3 unread messages” or “2 connected devices”.
This relationship may be provided through visible text or an accessible name when the visual layout only displays the number.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The card container does not receive keyboard or screen-reader focus.
Only an explicitly supported interactive element, such as a dedicated Link component in the Bottom slot, is included in the focus order.
Do not place interactive content in the Leading container, Trailing container, Label slot or other custom visual slots.
WCAG 2.1 — 2.4.3 Focus Order, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Dynamic loading updates are announced according to their urgency.
Use the following behaviour:

Initial page loading: do not use a live region for every Skeleton card. Screen readers should encounter the final content when it becomes available.

User-initiated refresh: expose the relevant card or collection as busy and announce completion politely when the result would not otherwise be apparent.

Non-urgent background update: update the content without interrupting the user unless the change is important to their current task.

Urgent update: use an assertive announcement only when immediate attention is genuinely required. Prefer a dedicated Alert component or page-level alert region for this purpose.
Do not determine announcement priority from the Positive, Info, Warning or Negative colour variant alone. Do not place the entire card in a live region when this would cause every piece of content to be repeated.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage with limited vision**

Text meets the required contrast ratio in every state and theme.
Normal-size text must have a contrast ratio of at least 4.5:1. Large text must have a contrast ratio of at least 3:1.
The Disabled state still communicates meaningful static information and must remain readable. It must not be dimmed below the required contrast merely because it is named “Disabled”.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Meaningful icons, status indicators and visual boundaries have sufficient contrast.
Informative icons and graphical status indicators must have at least 3:1 contrast against adjacent colours.
An outline, divider or background boundary that is required to distinguish the card from its surroundings must also remain perceptible. Purely decorative borders are not required to communicate information.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Content remains usable when text is resized to 200%.
Labels, Extra labels, Descriptions, Helper text, trailing values, Badges and Tags must wrap without being clipped, hidden or overlapping other content.
Do not use a fixed card height. Allow the card to grow vertically when text occupies additional lines.
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The card reflows at a viewport width equivalent to 320 CSS pixels.
The component must not require horizontal scrolling to read its text at 400% browser zoom.
On narrow viewports:

Prefer Top alignment for multiline content.

Prefer either Leading or Trailing content when displaying both would leave insufficient text width.

Allow trailing text, Badges and Tags to wrap when their content cannot remain on one line.

Preserve the primary Label and Description before optional decorative content.
Do not use the Small size merely to force overflowing content into the available width.
WCAG 2.1 — 1.4.10 Reflow, Level AA

Text remains readable when custom text-spacing settings are applied.
The card must support increased line height, paragraph spacing, letter spacing and word spacing without clipping, overlap or loss of content.
Description and Helper text must not rely on a fixed number of lines.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

Long labels, translated content and numerical values are not unnecessarily truncated.
Allow meaningful content to wrap. Do not rely on ellipsis when truncation would conceal a status, price, date, unit, error or other information required to understand the card.
When content length creates an unbalanced layout, use Top alignment or simplify optional Leading and Trailing content rather than reducing the text size.
Design guidance supporting WCAG 2.1 — 1.4.4 Resize Text, Level AA
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The card does not require a specific screen orientation.
Its content must remain available in portrait and landscape orientations unless a particular orientation is essential to the wider product experience.
WCAG 2.1 — 1.3.4 Orientation, Level AA

High-contrast and forced-colour modes preserve meaningful information.
Status text, labels and values must remain understandable when custom colours, backgrounds, outlines and shadows are replaced by system colours.
Do not depend on a background, divider, rounded corner or outline alone to communicate grouping, state or importance. Preserve semantic grouping in the DOM.
Informative icons should use tokens or system-compatible colours rather than fixed decorative fills that disappear in forced-colour modes.
Design guidance supporting WCAG 2.1 — 1.4.1 Use of Color, Level A
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Do not embed essential text inside images thumbnails.
Product names, prices, statuses and instructions must remain real text. An image containing incidental text may be used only when that text is not required to understand the card.
WCAG 2.1 — 1.4.5 Images of Text, Level AA

**Usage without perception of colour**

Colour is not the only way a status is communicated.
Functional Positive, Info, Warning and Negative variants combine:

Explicit status text.

The corresponding semantic icon where supported.

Semantic colour.
The card must remain understandable when all semantic colours appear identical.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Functional icons remain consistent across cards.
Do not replace the predefined icon of a functional status with an unrelated icon for visual variety.
Neutral and Accent icons may be adapted to the context, but their meaning must be communicated by the visible Label, Tag or Description rather than by colour alone.
Design guidance supporting WCAG 2.1 — 1.4.1 Use of Color, Level A
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Avatar badges include a visible or programmatic status description.
Availability, verification or account state must not be represented only by a coloured dot.
Where the badge communicates important functional information, include a visible status such as “Available”, “Verified” or “Unavailable”. A programmatic description may supplement the visible text but must not leave colour-perceiving users with information that is unavailable to colour-blind users.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Badge and Tag variants remain understandable without their colour treatment.
Neutral and Accent variants require a meaningful textual label.
Functional variants require text that communicates the state, such as “Active”, “In progress”, “Almost used” or “Failed”. A bullet or icon alone is insufficient.
WCAG 2.1 — 1.4.1 Use of Color, Level A

The Disabled state is not communicated only through reduced opacity.
Include explicit content such as “Unavailable”, “Inactive”, “Archived” or “Not applicable” when users need to understand why the information appears disabled.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Outlined, Background and Divider variants do not communicate status by themselves.
These properties provide visual separation only. Do not use a red outline, coloured surface or absent divider as the only indication of an error, category, selection or disabled state.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Links remain identifiable without relying only on colour.
Use the dedicated Link component and its defined visual treatment. Underlining is reserved for hyperlinks and must not be manually applied to ordinary Description or Helper text.
WCAG 2.1 — 1.4.1 Use of Color, Level A

**Usage with limited manipulation or strength**

The Static card item itself is not interactive.
It must not activate navigation, selection or another action when clicked, tapped, focused or pressed.
Do not apply hover, pressed or focus states to the card container. Use the appropriate Navigation card or Action card component when the entire surface needs to be interactive.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Keyboard users can reach every supported interactive element.
When a dedicated Link component is placed in the Bottom slot, it must be operable with the keyboard and must not create a keyboard trap.
The card container and its non-interactive visual content must not create unnecessary tab stops.
WCAG 2.1 — 2.1.1 Keyboard, Level A
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A

Focus follows the visual and reading order.
A Bottom slot link is placed after the card’s primary and supporting information in the focus order.
Do not place a visually trailing link before the card Label in the DOM.
WCAG 2.1 — 2.4.3 Focus Order, Level A

Every interactive element has a visible focus indicator.
The dedicated Link component must retain its standard focus treatment in all themes, backgrounds and forced-colour modes.
The card outline must not be mistaken for the link’s focus indicator.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Interactive content is not placed in unsupported slots.
Leading and Trailing custom slots must not contain buttons, links, checkboxes, radio buttons, toggles, menus or other independently focusable elements.
The Label slot is also limited to non-interactive primary content. A supported hyperlink belongs in the Bottom slot and uses the dedicated Link component.
Design guidance supporting WCAG 2.1 — 2.4.3 Focus Order, Level A
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Pointer activation is completed on release rather than on pointer down.
A supported Bottom slot link must allow users to cancel activation by moving the pointer away before release. It must not trigger as soon as the pointer is pressed.
WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

The component does not require complex gestures.
Do not add swipe, drag, long-press, multi-pointer or motion-based behaviour to the Static card item.
WCAG 2.1 — 2.5.1 Pointer Gestures, Level A

Standalone interactive targets should provide a sufficiently large activation area.
A standalone Link component in the Bottom slot should provide or be positioned within a target area of at least 44 × 44 CSS px where possible.
This is an AAA recommendation under WCAG 2.1, not a Level AA requirement. The inline-text exception may apply when the link is presented within a sentence.
Recommended under WCAG 2.1 AAA — 2.5.5 Target Size

Focus remains stable during loading and content updates.
Replacing Enabled content with Skeleton content must not move focus to the card.
If an update removes a Bottom slot link while that link has focus, move focus to the update trigger or the next logical control. Do not return focus to the beginning of the page.
WCAG 2.1 — 2.4.3 Focus Order, Level A

**Usage with limited cognition, language or learning**

Each card communicates one primary subject.
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

Rich text is used only to reinforce an already clear message.
Inline Strong text is supported in Description and Helper text. Use the Label/Medium/Strong token and no custom font weights.
Prefer one short Strong fragment per text block. Do not bold entire descriptions or use rich text to create a hierarchy that should have been expressed through the Label, Overline or Extra label properties.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Underlining is reserved for hyperlinks.
Do not manually underline ordinary content in the Label, Description or Helper text.
When a link is required, use the dedicated Link component in the Bottom slot. Its label must describe its destination or purpose, for example “View data usage details” rather than “Click here”, “More” or “Learn more”.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Essential information is not contained only inside a link.
The Label and Description must communicate the card’s main information without requiring the user to activate the Bottom slot link.
The link provides access to additional details or a related destination rather than replacing the card’s explanation.
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

The card behaves predictably.
Focusing or reading the card must not open content, navigate, submit data or change context.
Use consistent terminology and status icons across equivalent cards.
WCAG 2.1 — 3.2.1 On Focus, Level A
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

The Static card item does not disappear automatically.
It has no dismissible behaviour, timeout or Close button. Keep it available while the represented information remains relevant.
When temporary, dismissible or automatically disappearing information is required, use a component designed for that behaviour, such as an Alert or Toast.
Design guidance supporting WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

**Minimize photosensitive seizure triggers**

The component does not use flashing, blinking or rapidly alternating status effects.
This applies to Skeleton placeholders, Loading Tags, status icons, Badges and any custom content added through the Bottom slot.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Skeleton and Loading variants avoid continuous shimmer or pulsing where possible.
Prefer a static placeholder or a subtle, non-flashing progress treatment.
When an animation continues for more than five seconds and is presented alongside other content, users must be able to pause, stop or hide it unless the animation is essential. Because a static loading alternative is available, continuous movement should not be treated as essential by default.
WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A

Loading remains understandable when motion is reduced or disabled.
Respect the user’s reduced-motion preference. A Skeleton or Loading Tag must still communicate its state through its shape, text or programmatic busy state when animation is removed.
The loader graphic should be hidden from assistive technologies when the loading text already communicates the state.
Design guidance supporting WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A