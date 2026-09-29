**Usage without vision**

The complete Navigation list item is exposed as one link to one destination.
Use native link semantics whenever possible. The Label, Description, Leading content, Trailing content and navigation indicator must not be exposed as separate interactive elements.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The visible destination label is included in the accessible name.
The accessible name must contain the visible Label so that speech-input and screen-reader users can identify and activate the same destination. Do not replace it with unrelated hidden wording.
WCAG 2.1 — 2.5.3 Label in Name, Level A

The purpose of the destination is clear from the link text and its context.
Use a specific Label that explains where the item leads. Supporting content may clarify the destination, but users should not need to infer its purpose from the icon or navigation indicator alone.
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Supporting text remains programmatically associated with the navigation item.
The Overline, Label, Extra label, Description, Helper text, Trailing information and Bottom slot content must remain within the same link structure or be programmatically associated with it.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Navigation items use appropriate list semantics when presented as a structured list.
Apply list semantics to the parent collection and item wrappers. Each Navigation list item remains a single link within that structure.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Content follows a logical reading order.
The programmatic order should communicate the destination before secondary information: Overline, Label, Extra label, Description, Trailing information, Helper text and Bottom slot content. Informative Leading content may be announced before the Label when it adds unique meaning.
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

The navigation indicator is not announced as a separate control.
The internal chevron or previous-direction indicator is decorative when the link role and destination are already available programmatically. Hide it from assistive technologies to avoid announcements such as “link, arrow, link”.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

External navigation is communicated when it is not otherwise apparent.
The External indicator must not be the only way users discover that the destination leaves the current product or service. Provide visible or programmatic wording such as “External link” when this information is relevant.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Opening a destination in a new tab or window is communicated separately from external navigation.
An External destination does not automatically mean that it opens a new tab. When a new browsing context is used and the behaviour may be unexpected, communicate it through visible supporting text or the accessible description.
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Decorative visual content is ignored by assistive technologies.
Icons, images, avatars thumbnails and badges that repeat information already available in text should use an empty text alternative or be hidden from the accessibility tree.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Informative visual content has an equivalent text alternative.
Provide a text alternative when an Icon, Image, Avatar badge thumbnail or custom Slot communicates information that is not already available in the Label, Description or status text.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Avatar identity is available as visible text.
An Avatar representing a person, profile, team, organisation or account must be accompanied by a visible Label. The image, initials or generic icon may then be treated as decorative.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Flags are accompanied by the represented country, territory or language name.
Do not expose only the visual appearance of the flag. Use visible text such as “United States” rather than an accessible name such as “stars and stripes”.
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Badge counts communicate what is being counted.
Do not expose an isolated number such as “3”. The accessible information should communicate “3 unread messages”, “2 connected devices” or another meaningful relationship with the destination.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Functional statuses are communicated through meaningful text.
Positive, Info, Warning and Negative variants require explicit text that communicates the represented state. The semantic icon can be hidden when it repeats the same information.
WCAG 2.1 — 1.1.1 Non-text Content, Level A
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

The navigation item contains no nested interactive elements.
Leading content, Trailing content, Label Slot, Description, Helper text and Bottom slot must not contain another link, button, checkbox, toggle, menu, media control or independently focusable element.
WCAG 2.1 — 2.1.1 Keyboard, Level A
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Disabled items are not exposed as active links.
A Disabled Navigation list item must not be keyboard focusable or activatable. The unavailable state and its reason should remain available as readable static information when required.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Skeleton items are not exposed as links.
Individual placeholder shapes should be ignored by assistive technologies. Do not provide an accessible destination or focus stop until the final content and destination are available.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Initial Skeleton content does not create repeated live-region announcements.
When a complete list initially loads, do not announce every placeholder or every item as it appears. Screen readers should encounter the final links through normal navigation.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

User-initiated loading completion may be announced politely.
When users explicitly refresh or load a navigation collection and completion would not otherwise be apparent, expose the parent region as busy and announce completion through a polite status message.
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Assertive announcements are not determined by visual status.
Do not use an assertive live region because an item contains a Warning or Negative Badge. Assertive announcements are reserved for genuinely urgent information requiring immediate attention and should normally use a dedicated alert pattern.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

**Usage with limited vision**

Text meets the required minimum contrast.
Normal-size text must have a contrast ratio of at least 4.5:1. Large text must have a contrast ratio of at least 3:1 against its background in Enabled, Hover, Focus, Pressed and Disabled presentations.
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Meaningful graphical elements meet non-text contrast requirements.
The navigation indicator, functional icons, status indicators and any visual boundary required to identify the item must have at least 3:1 contrast against adjacent colours.
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

The focus indicator remains clearly visible.
Display one focus indicator around the complete navigation target. It must remain distinguishable from the item’s background, divider and hover treatment in every supported theme.
WCAG 2.1 — 2.4.7 Focus Visible, Level AA
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Hover, Focus and Pressed states remain visually distinguishable.
The state treatment must remain visible without reducing text contrast or making the navigation indicator disappear. Do not use subtle changes that are imperceptible at low vision or high zoom.
Design guidance supporting WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Content remains readable when text is resized to 200%.
The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap without clipping, overlap or loss of content. The item must expand vertically instead of using a fixed height.
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The component reflows at a viewport equivalent to 320 CSS pixels.
Users must be able to read and activate the complete item without horizontal scrolling. The navigation indicator must remain visible and must not overlap the destination label.
WCAG 2.1 — 1.4.10 Reflow, Level AA

Increased text spacing does not cause content loss.
The item must support increased line height, paragraph spacing, letter spacing and word spacing without clipping, overlap or hidden information.
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

Long and translated content can wrap onto multiple lines.
Do not truncate destination labels, statuses, dates, prices or information required to understand the destination. Use Top alignment when text becomes multiline.
Design guidance supporting WCAG 2.1 — 1.4.4 Resize Text, Level AA
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Optional visual content does not reduce the text area to an unusable width.
Leading and Trailing content must leave sufficient space for the Label and navigation indicator. Simplify optional visual content on narrow layouts before hiding meaningful text.
WCAG 2.1 — 1.4.10 Reflow, Level AA

The complete interactive target expands with multiline content.
Hover, Focus and Pressed treatments must cover the full visible height and width of the expanded item rather than only the first line or original fixed-height area.
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

High-contrast and forced-colour modes preserve the link and its focus state.
The Label, navigation indicator, functional statuses and focus boundary must remain perceivable when product colours, backgrounds and shadows are replaced by system colours.
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Background and Divider treatments are not required to understand the structure.
Semantic list and link relationships must remain available when backgrounds, dividers, shadows or custom outlines are not rendered.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Essential text is not embedded inside images thumbnails.
Destination names, statuses, prices and instructions must remain real text that can be resized and reflowed.
WCAG 2.1 — 1.4.5 Images of Text, Level AA

The item does not require a specific orientation.
The destination and complete navigation target must remain available in portrait and landscape orientations unless orientation is essential to the wider product.
WCAG 2.1 — 1.3.4 Orientation, Level AA

**Usage without perception of colour**

Interaction states are not communicated by colour alone.
Hover, Focus, Pressed and Disabled states must include a perceivable visual change that does not depend only on a colour difference.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Focus is not represented only by a colour change.
Use a visible outline, border or another persistent shape-based indicator around the complete navigation target.
WCAG 2.1 — 1.4.1 Use of Color, Level A
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Functional statuses combine text, semantic icon and colour.
Positive, Info, Warning and Negative variants must remain understandable when all semantic colours appear identical.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Neutral and Accent variants include meaningful text.
Do not rely on a neutral or branded colour to communicate the category, status or importance of the destination.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Avatar badges do not rely only on a coloured dot.
Availability, verification and account status require a visible label or equivalent accessible description such as “Available”, “Verified” or “Unavailable”.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Badge and Tag states remain understandable without colour.
Functional variants require explicit status text. Text + Bullet and Text + Icon layouts must not use the bullet or icon colour as the only status indicator.
WCAG 2.1 — 1.4.1 Use of Color, Level A

The Disabled state is not communicated only through reduced opacity.
Provide explicit wording when users need to understand that the destination is unavailable and why.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Internal and External destinations are not distinguished by colour alone.
Use the dedicated navigation indicator and, when necessary, supporting text or an accessible description.
WCAG 2.1 — 1.4.1 Use of Color, Level A

Background and Divider colours do not communicate status.
These properties provide visual separation only and must not be the sole indication of selection, availability, urgency or category.
WCAG 2.1 — 1.4.1 Use of Color, Level A

**Usage with limited manipulation or strength**

The complete item is operable with a keyboard.
Use native link keyboard behaviour. Users must be able to reach the item, identify its focus state and activate the destination without a pointer.
WCAG 2.1 — 2.1.1 Keyboard, Level A

The component does not create a keyboard trap.
Keyboard users must be able to move to and away from the item using standard navigation commands.
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A

The complete item creates one focus stop.
Leading content, Trailing content, Badge, Tag, navigation indicator and Bottom slot content must not create additional focus stops.
WCAG 2.1 — 2.4.3 Focus Order, Level A

Focus order follows the visual navigation order.
Navigation items must receive focus in a logical sequence that matches the structure and meaning of the list.
WCAG 2.1 — 2.4.3 Focus Order, Level A

The complete visible row is the interactive target.
Users must not be required to activate only the Label, icon or navigation indicator. Padding and supporting content remain inside the same hit area.
Design guidance supporting WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

Pointer activation occurs on release rather than pointer down.
Users must be able to move the pointer away before release to cancel activation, unless another permitted cancellation mechanism is provided.
WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

Navigation does not require complex gestures.
Do not require swiping, dragging, long-pressing, multi-pointer input or a path-based gesture to activate the item.
WCAG 2.1 — 2.5.1 Pointer Gestures, Level A

The item does not depend on device motion.
Users must not be required to tilt, shake or move the device to activate the destination.
WCAG 2.1 — 2.5.4 Motion Actuation, Level A

The interactive target should be at least 44 × 44 CSS pixels.
This is a recommended WCAG 2.1 AAA improvement rather than a Level AA requirement. The complete row should provide the target area, not only the visible Label or indicator.
Recommended under WCAG 2.1 AAA — 2.5.5 Target Size

Pressed is a temporary visual state only.
Do not use Pressed as a persistent selected or current-page state. Activating the item must not require users to maintain pressure or perform repeated input.
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A

Disabled items cannot be activated accidentally.
Remove the active destination and keyboard focus behaviour. A visual Disabled treatment alone is insufficient.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Focus remains stable while content loads.
Replacing a Skeleton item with final content must not unexpectedly move focus to the new link or to the beginning of the list.
WCAG 2.1 — 2.4.3 Focus Order, Level A

Removing a focused item restores focus logically.
When navigation content changes and the currently focused item is removed, place focus on the update trigger, an adjacent item or another logical control.
WCAG 2.1 — 2.4.3 Focus Order, Level A

**Usage with limited cognition, language or learning**

Each item navigates to one clearly identified destination.
Do not combine several destinations or actions inside the same row. Use another component architecture when users need independent links or controls.
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Destination labels use specific and familiar wording.
Describe where the item leads using terms users can recognise. Avoid vague labels such as “Click here”, “More”, “OK” or “Learn more”.
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

The primary destination is communicated before supporting details.
Place the destination Label before secondary metadata, values, Badge counts and status information in the reading order.
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

Supporting content clarifies rather than replaces the destination label.
Use Description or Helper text for conditions, availability or additional context. Users should still understand the destination from the primary Label.
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Next and Previous layouts reflect the actual navigation relationship.
Use Next for deeper, forward or related navigation. Use Previous only when returning to a parent destination, an earlier level or a preceding step.
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Previous is not used as a decorative reversed layout.
The Previous indicator communicates backward navigation and occupies the logical start of the item. Leading content is therefore not supported in this layout.
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Internal and External indicators are used consistently.
Equivalent destinations must use the same indicator type throughout the product. Do not use External merely to attract additional attention.
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Navigation does not occur when the item only receives focus.
Focusing, hovering over or reading the item must not automatically activate the destination or change the user’s context.
WCAG 2.1 — 3.2.1 On Focus, Level A

Disabled destinations explain why they are unavailable when necessary.
Use Description or Helper text to communicate the reason and, when known, what users need to do before the destination becomes available.
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Functional Warning and Negative information includes useful wording.
Explain what the status means before users navigate. Do not rely on a warning colour or generic icon without text.
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Rich text reinforces an already clear message.
Use one short Strong fragment in Description or Helper text when emphasis is required. Use only the supported Label/Medium/Strong token.
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Underlining is not applied manually inside the item.
The complete item already acts as a link. Do not create underlined fragments that appear to be separate destinations.
Design guidance supporting WCAG 2.1 — 1.4.1 Use of Color, Level A

Inline links and separate actions are not placed inside the item.
Description, Helper text, Label Slot and Bottom slot must remain part of the same navigation target. Place an additional destination or action outside the component.
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Important destination information is not available only through emphasis.
Users must be able to understand the item when Strong styling, semantic colour or decorative imagery is unavailable.
WCAG 2.1 — 1.3.1 Info and Relationships, Level A
WCAG 2.1 — 1.4.1 Use of Color, Level A

Skeleton and Loading Tags retain meaningful context.
When loading text is displayed, identify what is loading, for example “Loading mobile plan details” or “Activating eSIM”, rather than showing only “Loading”.
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

The item behaves predictably across the product.
Equivalent items use consistent labels, navigation indicators, content positions and interaction states.
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

The component does not disappear automatically.
A Navigation list item remains available while its destination is relevant. It has no timer, dismiss action or close control.
Design guidance supporting WCAG 2.1 — 2.2.1 Timing Adjustable, Level A

Unusual words and abbreviations are avoided or explained.
Use plain language and expand unfamiliar abbreviations in the Description or Helper text when they are necessary.
Recommended under WCAG 2.1 AAA — 3.1.3 Unusual Words
Recommended under WCAG 2.1 AAA — 3.1.4 Abbreviations

**Minimize photosensitive seizure triggers**

Interaction states do not flash or rapidly alternate.
Hover, Focus, Pressed, Disabled, Badge and Tag treatments must not use flashing effects or rapid colour alternation.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Skeleton and Loading states avoid continuous flashing or pulsing.
Prefer static placeholders or subtle non-flashing movement. Loading must remain understandable when animation is removed.
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Non-essential loading animation can be paused, stopped or hidden.
Animation that starts automatically, lasts more than five seconds and appears alongside other content requires a mechanism to pause, stop or hide it.
WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A

Reduced-motion preferences are respected.
Remove shimmer, repeated movement and animated transitions when users request reduced motion. Preserve the Skeleton or Loading state through static shape and text.
Design guidance supporting WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A

Hover and Pressed feedback does not use shaking, bouncing or large movement.
Use stable visual treatments that do not move the item or surrounding content.
Design guidance supporting WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A