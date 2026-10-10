### Usage without vision

The complete Navigation card item is exposed as one link to one destination.  
Use native link semantics whenever possible. On native platforms, expose the equivalent accessibility role through the platform accessibility API.  
The Label, Description, Leading content, Trailing content, Bottom slot and affordance indicator must not be exposed as separate interactive elements.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The visible destination Label is included in the accessible name.  
The accessible name must contain the visible Label so that screen-reader and speech-input users can identify and activate the same destination.  
Do not replace the visible Label with unrelated hidden wording.  
WCAG 2.1 — 2.5.3 Label in Name, Level A

The destination is clear from the Label and its context.  
Use a specific Label that explains where the card leads.  
Supporting content may clarify the destination, but users should not need to infer its purpose from the image, icon or affordance indicator alone.  
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Supporting content remains programmatically associated with the card.  
The Overline, Label, Extra label, Description, Helper text, Trailing information and Bottom slot content must remain within the same link structure or be programmatically associated with it.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

A standalone card does not require article semantics by default.  
Use the native link as the primary semantic element.  
An article or equivalent grouping container may be used around the link when the card represents self-contained content, but it must not create a second interactive role.  
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Card collections use appropriate grouping semantics.  
When several Navigation card items form a semantic list, use list semantics for the parent collection and its direct item wrappers.  
Each card remains one link within that structure.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Content follows a logical reading order.  
The programmatic order should communicate the destination before secondary information:

Label.

Extra label.

Description.

Trailing value, status, Badge or Tag.

Helper text.  
Informative Leading content may be announced before the Label when it adds information not already available in text.  
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

The affordance indicator is not announced as a separate control.  
The Internal, External or Previous indicator is part of the visual affordance of the complete link.  
Hide it from assistive technologies when the link role and destination are already available programmatically.  
Avoid repeated announcements such as “link, arrow, link”.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

External navigation is communicated when it is not otherwise apparent.  
The External indicator must not be the only way users discover that the destination leaves the current product or service.  
Provide visible or programmatic wording such as “External link” when this information is important to the user.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A  
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Opening a destination in a new tab or window is communicated separately from external navigation.  
An External destination does not automatically mean that it opens in a new browsing context.  
When a new tab or window is used and the behaviour may be unexpected, communicate it through visible supporting text or the card’s accessible description.  
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Decorative visual content is ignored by assistive technologies.  
Icons, images, Avatars thumbnails, Badges and decorative Slot content that repeat information already communicated in text should use an empty text alternative or be hidden from the accessibility tree.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Informative visual content has an equivalent text alternative.  
Provide an equivalent when an Icon, Image, Avatar badge thumbnail, Flag or custom Slot communicates information that is not already available in the Label, Description or visible status text.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Icons communicate meaning rather than their visual appearance.  
Do not announce technical names such as “orange icon”, “green check” or “right arrow”.  
Communicate the represented meaning, such as “Payment failed” or “Available”, when it is not already available in visible text.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Avatar identity is available as visible text.  
An Avatar representing a person, profile, team, organisation or account must be accompanied by a visible Label identifying the destination.  
The portrait, initials or generic icon may then be treated as decorative.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Avatar status is available independently from the visual badge.  
Availability, verification or account state must be communicated through visible text or an equivalent accessible description.  
Do not expose only a coloured dot or an unexplained Badge icon.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Flags are accompanied by the represented country, territory or language name.  
Use visible text such as “United States” rather than describing the visual appearance of the flag.  
Do not assume that a country flag always represents a language or nationality.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A

Badge counts communicate what is being counted.  
Do not expose an isolated number such as “3”.  
Communicate a meaningful relationship such as “3 unread messages” or “2 connected devices”.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Functional statuses are communicated through meaningful text.  
Positive, Info, Warning and Negative variants require explicit text communicating the represented state.  
The semantic icon may be hidden from assistive technologies when it repeats the same information.  
WCAG 2.1 — 1.1.1 Non-text Content, Level A  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Neutral and Accent variants are not announced as semantic statuses automatically.  
These variants do not inherently mean success, information, warning or error.  
Their meaning must come from the Label, Tag, Badge or Description.  
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

The card contains no nested interactive elements.  
Leading content, Trailing content, Label Slot, Description, Helper text and Bottom slot must not contain another Link, Button, Checkbox, Radio button, Toggle, Menu, media control or independently focusable element.  
WCAG 2.1 — 2.1.1 Keyboard, Level A  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Disabled cards are not exposed as active links.  
A Disabled Navigation card item must not be keyboard focusable or activatable.  
Removing visual Hover and Focus treatments is not sufficient. The destination must also be technically unavailable.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

The Disabled state remains understandable as static content.  
When the unavailable destination and its reason are important, keep the Label and explanation available to assistive technologies as non-interactive content.  
Do not rely only on aria-disabled while leaving the link operable.  
Design guidance supporting WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Skeleton cards are not exposed as links.  
Individual placeholder shapes should be ignored by assistive technologies.  
Do not provide an accessible destination or focus stop until the final content is available.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Initial Skeleton loading does not create repeated announcements.  
When a card collection initially loads, do not announce every placeholder or every card as it appears.  
Screen readers should encounter the final links through normal reading and navigation.  
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

User-initiated loading completion may be announced politely.  
When users explicitly refresh or load a card collection and completion would not otherwise be apparent, expose the parent region as busy and announce completion through a polite status message.  
Do not move focus to the first loaded card automatically.  
WCAG 2.1 — 4.1.3 Status Messages, Level AA

Assertive announcements are based on urgency, not visual status.  
Do not use an assertive live region merely because a card contains a Warning or Negative Badge.  
Assertive announcements are reserved for genuinely urgent information requiring immediate attention and should normally use a dedicated Alert pattern.  
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

### Usage with limited vision

Text meets the required minimum contrast.  
Normal-size text must have a contrast ratio of at least 4.5:1.  
Large text must have a contrast ratio of at least 3:1.  
This applies to Enabled, Hover, Focus, Pressed and Disabled visual presentations.  
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Disabled text remains readable.  
Disabled content may use a visually reduced treatment, but meaningful information must not fall below the required text contrast.  
Do not use opacity reduction as a convenient ritual sacrifice to the design gods.  
WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA

Meaningful graphical elements meet non-text contrast requirements.  
The affordance indicator, functional icons, status indicators and any boundary required to identify the card must have at least 3:1 contrast against adjacent colours.  
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

The focus indicator remains clearly visible.  
Display one focus indicator around the complete card target.  
It must remain distinguishable from the card’s Background, Outline, Divider and Hover treatment in every supported theme.  
WCAG 2.1 — 2.4.7 Focus Visible, Level AA  
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Hover, Focus and Pressed states remain visually distinguishable.  
State treatments must remain perceptible without reducing text contrast or making the affordance indicator disappear.  
Do not use movement or a subtle colour shift as the only distinction.  
Design guidance supporting WCAG 2.1 — 1.4.3 Contrast (Minimum), Level AA  
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Content remains readable when text is resized to 200%.  
The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap without clipping, overlap or loss of information.  
The card must expand vertically instead of using a fixed height.  
WCAG 2.1 — 1.4.4 Resize Text, Level AA

The card reflows at a viewport equivalent to 320 CSS pixels.  
Users must be able to read and activate the complete card without horizontal scrolling.  
The affordance indicator must remain visible and must not overlap the destination Label.  
WCAG 2.1 — 1.4.10 Reflow, Level AA

Increased text spacing does not cause content loss.  
The card must support increased line height, paragraph spacing, letter spacing and word spacing without clipping, overlap or hidden information.  
WCAG 2.1 — 1.4.12 Text Spacing, Level AA

Long and translated content can wrap onto multiple lines.  
Do not truncate destination labels, statuses, dates, prices or other information required to understand the destination.  
Use Top alignment when the content becomes multiline.  
Design guidance supporting WCAG 2.1 — 1.4.4 Resize Text, Level AA  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Optional visual content does not reduce the text area to an unusable width.  
Leading and Trailing content must leave sufficient space for the Label and affordance indicator.  
Simplify optional decorative content on narrow layouts before hiding meaningful text.  
WCAG 2.1 — 1.4.10 Reflow, Level AA

The complete interactive target expands with multiline content.  
Hover, Focus and Pressed treatments must cover the full visible width and height of the expanded card.  
They must not remain restricted to the original single-line dimensions.  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

The card width is controlled by its parent layout without restricting readability.  
A card may span one or several grid columns, but its text area must remain wide enough to avoid extreme word-by-word wrapping.  
On wide layouts, a product-defined text maximum width may be used while the complete card remains interactive.  
Design guidance supporting WCAG 2.1 — 1.4.10 Reflow, Level AA

Outlined and Background variants remain perceivable in supported themes.  
When an Outline or Background is required to distinguish the card from adjacent content, its visual boundary must remain identifiable against the surrounding surface.  
WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

High-contrast and forced-colour modes preserve the link and its focus state.  
The Label, affordance indicator, functional statuses and focus boundary must remain perceivable when product colours, backgrounds, outlines and shadows are replaced by system colours.  
Design guidance supporting WCAG 2.1 — 1.4.11 Non-text Contrast, Level AA

Background, Outline, Divider and rounded corners are not required to understand the structure.  
Semantic grouping and link relationships must remain available when visual surfaces, corner shapes, shadows or separators are not rendered.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Rounded and square cards expose the same information.  
Rounded corner variants change only visual presentation.  
Corner shape must not be the only way to communicate category, status, availability or importance.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Essential text is not embedded inside images thumbnails.  
Destination names, statuses, prices and instructions must remain real text that can be resized, selected and reflowed.  
WCAG 2.1 — 1.4.5 Images of Text, Level AA

Meaningful image content is preserved when cropped.  
When 1x1 or 16x9 ratios are used, select an appropriate focal point and avoid cropping information required to identify or understand the destination.  
Design guidance supporting WCAG 2.1 — 1.1.1 Non-text Content, Level A

The card does not require a specific orientation.  
The destination and complete navigation target must remain available in portrait and landscape orientations unless orientation is essential to the wider product experience.  
WCAG 2.1 — 1.3.4 Orientation, Level AA

### Usage without perception of colour

Interaction states are not communicated by colour alone.  
Hover, Focus, Pressed and Disabled states must include a perceivable visual difference that does not depend only on colour.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Focus is not represented only by a colour change.  
Use a visible outline, border or another persistent shape-based indicator around the complete card.  
WCAG 2.1 — 1.4.1 Use of Color, Level A  
WCAG 2.1 — 2.4.7 Focus Visible, Level AA

Functional statuses combine text, semantic icon and colour.  
Positive, Info, Warning and Negative variants must remain understandable when all semantic colours appear identical.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Functional status icons remain consistent.  
Use the predefined semantic icon for Positive, Info, Warning and Negative variants where supported.  
Do not replace functional icons with arbitrary alternatives for visual variety.  
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Neutral and Accent variants include meaningful text.  
Do not rely on a neutral or branded colour to communicate the category, status or importance of the destination.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Avatar badges do not rely only on a coloured dot.  
Availability, verification and account status require visible text or an equivalent accessible description such as “Available”, “Verified” or “Unavailable”.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Badge and Tag states remain understandable without colour.  
Functional variants require explicit status text.  
Text + Bullet and Text + Icon layouts must not use the bullet or icon colour as the only status indicator.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Badge counts remain understandable independently from their colour.  
The meaning must be provided through the number and its context, not through the Badge background alone.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

The Disabled state is not communicated only through reduced opacity.  
Provide explicit wording when users need to understand that the destination is unavailable and why.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Internal and External destinations are not distinguished by colour alone.  
Use the dedicated affordance indicator and, when necessary, supporting text or an accessible description.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Outlined, Background and Divider variants do not communicate status by themselves.  
These properties provide visual separation only.  
They must not be the sole indication of selection, availability, urgency or category.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Rounded corner variants do not communicate meaning by themselves.  
Do not use square and rounded corners as the only way to distinguish status, product type or destination importance.  
WCAG 2.1 — 1.4.1 Use of Color, Level A

### Usage with limited manipulation or strength

The complete card is operable with a keyboard.  
Use native link keyboard behaviour.  
Users must be able to reach the card, identify its focus state and activate the destination without a pointer.  
WCAG 2.1 — 2.1.1 Keyboard, Level A

The component does not create a keyboard trap.  
Keyboard users must be able to move to and away from the card using standard navigation commands.  
WCAG 2.1 — 2.1.2 No Keyboard Trap, Level A

The complete card creates one focus stop.  
Leading content, Trailing content, Badge, Tag, affordance indicator and Bottom slot content must not create additional focus stops.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

Focus order follows the visual and semantic order of the card collection.  
Cards must receive focus in a logical sequence matching the structure and meaning of the surrounding layout.  
Do not allow visual grid placement to create an unexpected focus order.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

The complete visible card is the interactive target.  
Users must not be required to activate only the Label, image or affordance indicator.  
Padding, Background, Outline and supporting content remain inside the same hit area.  
Design guidance supporting WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

Adjacent card targets do not overlap.  
Spacing between cards must prevent users from accidentally activating a neighbouring destination.  
Card shadows, visual overflow or media content must not extend the interactive target into another card.  
Design guidance supporting WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

Pointer activation occurs on release rather than pointer down.  
Users must be able to move the pointer away before release to cancel activation, unless another permitted cancellation mechanism is provided.  
WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

Navigation does not require complex gestures.  
Do not require swiping, dragging, long-pressing, multi-pointer input or a path-based gesture to activate the card.  
WCAG 2.1 — 2.5.1 Pointer Gestures, Level A

The card does not depend on device motion.  
Users must not be required to tilt, shake or move the device to activate the destination.  
WCAG 2.1 — 2.5.4 Motion Actuation, Level A

The interactive target should be at least 44 × 44 CSS pixels.  
This is a recommended WCAG 2.1 AAA improvement, not a Level AA requirement.

The complete card should provide the target area rather than only the visible Label or indicator.  
Recommended under WCAG 2.1 AAA — 2.5.5 Target Size

Pressed is a temporary visual state only.  
Do not use Pressed as a persistent selected or current-page state.  
Activating the card must not require users to maintain pressure or repeat an input.  
Design guidance supporting WCAG 2.1 — 2.1.1 Keyboard, Level A

Disabled cards cannot be activated accidentally.  
Remove the active destination and keyboard focus behaviour.  
A visual Disabled treatment alone is insufficient.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Skeleton content cannot be activated repeatedly.  
While the destination is unavailable, the Skeleton card must not accept pointer or keyboard activation.  
Do not leave an invisible active link beneath the placeholder.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Focus remains stable while content loads.  
Replacing a Skeleton card with final content must not unexpectedly move focus to the new link or to the beginning of the collection.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

Removing a focused card restores focus logically.  
When dynamic content removes the currently focused card, place focus on the update trigger, an adjacent destination or another logical control.  
WCAG 2.1 — 2.4.3 Focus Order, Level A

Layout changes do not create unexpected target movement during activation.  
Hover, Focus and Pressed states must not resize the card or move adjacent cards.  
Design guidance supporting WCAG 2.1 — 2.5.2 Pointer Cancellation, Level A

### Usage with limited cognition, language or learning

Each card navigates to one clearly identified destination.  
Do not combine several destinations or independent actions inside the same card.  
Use another component architecture when users need multiple links or controls.  
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Each card communicates one primary subject.  
Keep the Label, Description, status, Trailing information and Bottom slot related to the same product, person, account, service or event.  
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Destination Labels use specific and familiar wording.  
Describe where the card leads using terms users can recognise.  
Avoid vague Labels such as “Click here”, “More”, “OK” or “Learn more”.  
WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A  
WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

The primary destination is communicated before supporting details.  
Place the destination Label before secondary metadata, values, Badge counts and status information in the reading order.  
WCAG 2.1 — 1.3.2 Meaningful Sequence, Level A

Supporting content clarifies rather than replaces the destination Label.  
Use Description or Helper text for conditions, availability or additional context.  
Users should still understand the destination from the primary Label.  
Design guidance supporting WCAG 2.1 — 2.4.4 Link Purpose (In Context), Level A

Description and Helper text have distinct purposes.  
Use Description to explain the main destination.  
Use Helper text for additional conditions or information required before navigation.  
Do not repeat the same sentence in both areas.  
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Next and Previous layouts reflect the real navigation relationship.  
Use Next for deeper, forward or related navigation.  
Use Previous only when returning to a parent destination, an earlier level or a preceding step.  
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Previous is not used as a decorative reversed layout.  
The Previous indicator communicates backward navigation and occupies the logical start of the card.  
Leading content is therefore not supported in this layout.  
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Internal and External indicators are used consistently.  
Equivalent destinations must use the same indicator type throughout the product.  
Do not use External merely to make a card appear more prominent.  
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Navigation does not occur when the card only receives focus.  
Focusing, hovering over or reading the card must not automatically activate the destination or change context.  
WCAG 2.1 — 3.2.1 On Focus, Level A

Hover does not reveal essential destination information.  
Users must understand the card without hovering over it.  
Any optional content displayed on Hover or Focus must remain dismissible, hoverable and persistent according to the relevant requirement.  
WCAG 2.1 — 1.4.13 Content on Hover or Focus, Level AA

Disabled destinations explain why they are unavailable when necessary.  
Use Description or Helper text to communicate the reason and, when known, what users need to do before the destination becomes available.  
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Warning and Negative information includes useful wording.  
Explain what the status means before users navigate.  
Do not rely on a warning colour or generic icon without text.  
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Badge and Tag content remains secondary to the destination.  
Categories, statuses and counts must not visually compete with or replace the primary Label.  
Use short, consistent terminology.  
Design guidance supporting WCAG 2.1 — 2.4.6 Headings and Labels, Level AA

Rich text reinforces an already clear message.  
Use one short Strong fragment in Description or Helper text when emphasis is required.  
Use only the supported Label/Medium/Strong token.  
Design guidance supporting WCAG 2.1 — 1.3.1 Info and Relationships, Level A

Underlining is not applied manually inside the card.  
The complete card already acts as a link.  
Do not create underlined fragments that appear to be separate destinations.  
Design guidance supporting WCAG 2.1 — 1.4.1 Use of Color, Level A

Inline links and separate actions are not placed inside the card.  
Description, Helper text, Label Slot and Bottom slot must remain part of the same navigation target.  
Place an additional destination or action outside the Navigation card item.  
WCAG 2.1 — 4.1.2 Name, Role, Value, Level A

Essential information is not available only through emphasis.  
Users must be able to understand the card when Strong styling, semantic colour, imagery or corner shape is unavailable.  
WCAG 2.1 — 1.3.1 Info and Relationships, Level A  
WCAG 2.1 — 1.4.1 Use of Color, Level A

Loading text identifies what is loading.  
When loading text is displayed in a Tag or supporting region, use contextual wording such as “Loading mobile plan details” or “Activating eSIM” instead of only “Loading”.  
Design guidance supporting WCAG 2.1 — 4.1.3 Status Messages, Level AA

The card behaves predictably across the product.  
Equivalent cards use consistent Labels, affordance indicators, content positions, sizes and interaction states.  
WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Rounded corner configuration remains consistent within comparable collections.  
Do not mix square and rounded cards arbitrarily when this could imply a hierarchy or category that does not exist.  
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

The component does not disappear automatically.  
A Navigation card item remains available while its destination is relevant.  
It has no timer, dismiss action or Close button.  
Design guidance supporting predictable navigation behaviour

The component does not support a Close button.  
Do not add dismissible behaviour through a custom Slot.  
When temporary or dismissible information is required, use a component designed for messages rather than navigation.  
Design guidance supporting WCAG 2.1 — 3.2.4 Consistent Identification, Level AA

Unusual words and abbreviations are avoided or explained.  
Use plain language and expand unfamiliar abbreviations in the Description or Helper text when necessary.  
Recommended under WCAG 2.1 AAA — 3.1.3 Unusual Words  
Recommended under WCAG 2.1 AAA — 3.1.4 Abbreviations

### Minimize photosensitive seizure triggers

Interaction states do not flash or rapidly alternate.  
Hover, Focus, Pressed, Disabled, Badge and Tag treatments must not use flashing effects or rapid colour alternation.  
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Skeleton and Loading states avoid continuous flashing or aggressive pulsing.  
Prefer static placeholders or subtle non-flashing movement.  
Loading must remain understandable when animation is removed.  
WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A

Non-essential loading animation can be paused, stopped or hidden.  
Animation that starts automatically, lasts more than five seconds and appears alongside other content requires a mechanism to pause, stop or hide it.  
WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A

Reduced-motion preferences are respected.  
Remove shimmer, repeated movement and animated card transitions when users request reduced motion.  
Preserve the Skeleton or Loading state through static shape and meaningful text.  
Design guidance supporting WCAG 2.1 — 2.2.2 Pause, Stop, Hide, Level A

Hover and Pressed feedback does not use shaking, bouncing or large movement.  
Use stable visual treatments that do not move the card or surrounding content.  
Design guidance supporting WCAG 2.1 — 2.3.1 Three Flashes or Below Threshold, Level A