## Definition

A Static card item is a non-interactive container used to present a self-contained group of related information.
The card surface does not navigate, trigger an action or receive interactive states.
The card may be displayed independently or within a card-based layout and may use a distinct background, outline or rounded corners.

---

## Size

**`Default`** Use the Default size in most interfaces.
It provides sufficient spacing for standalone cards, card collections, multiline content and visual elements such as avatars, images or badges.

**`Small`** Use the Small size in compact layouts where information density is important.
The Small size is best suited to:
• Short labels.
• Simple metadata.
• Compact desktop interfaces.

⚠️ Do not mix Default and Small cards within the same card collection unless they represent clearly different content groups or levels of hierarchy.

---

## Alignment

**`Center`** Use Center alignment is the default alignment for items containing:
• A single-line label.
• Short supporting content.
• Leading and trailing elements with similar dimensions.

⚠️ Do not use Center alignment when it makes an icon, avatar or value appear visually disconnected from the first line of content.

**`Top`** Use Top alignment when:
• The label wraps onto multiple lines.
• A description or extra label is displayed.
• The bottom slot is enabled.
• The leading or trailing content must remain aligned with the beginning of the text.
• The different content areas have noticeably different heights.

---

## State

**`Enabled`** Enabled is the default state. All content is displayed using its standard visual tokens.  Because the card is static, the Enabled state does not introduce hover, pressed or focus behaviour.

**`Disabled`** Use Disabled when the information represented by the card is currently unavailable, inactive or no longer applicable. Since the card is non-interactive, the Disabled state communicates the availability or relevance of its content, not the availability of an action.

**`Skeleton`** Use Skeleton while the card content is loading and its final values are not yet available.

---

## Outlined

**`False`** No outline is displayed. Use when the card is already separated from the surrounding content by its background, spacing or container.

**`True`** An outline is displayed around the card. Use when the card needs clearer visual separation from a surface with a similar background.

⚠️ The outline is a visual treatment only. It must not be used as the only way to communicate selection, status or interactivity.

---

## Rounded corner

Although this rendering option is available in the properties of each Static card item in Figma, its configuration should be defined consistently across the product or service in which the component is used.
Equivalent cards within the same interface should not arbitrarily mix Rounded corner=True and Rounded corner=False.
Different corner styles may only be combined when they represent clearly documented card categories or levels of hierarchy.

**`False`** The square rendering corresponds to Orange's historical style. It conveys the brand's sense of seriousness, robustness and utility-driven. It remains the default style for our digital interface components.

**`True`** The rounded rendering offers flexibility without sacrificing the attribution to the brand. It helps anchoring the service in a reality where the visual codes of the mobile area tends to rub off on all interfaces. Use rounded corners for a softer, more approachable, friendly and tactile feel.

This option is technically not available for all brand themes
Here’s the list of rounded corners availability by brand theme

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Unavailable |
| Wireframe | Unavailable |

---

## Choosing leading and trailing content

Leading and trailing content serve different purposes within the card.
• Leading content supports recognition and identification before users read the main label.
• Trailing content provides supplementary information after the main content has been understood.
Choose each position according to the role of the content, not only according to the available space.

**Use leading content only**
Use leading content when the visual element helps users identify or understand the item before reading its text.

Leading-only layouts are recommended when:
• Visual recognition is more important than comparison.
• The item does not require a secondary value or status.
• The main label needs most of the available horizontal space.
• The interface is displayed on a narrow mobile viewport.

⚠️ Leading content must not appear to be an independent action.

**Use trailing content only**
Use trailing content when the primary label is sufficient for identification and users mainly need to scan or compare secondary information.

Trailing-only layouts are recommended when:
• Users compare values across several items.
• The list does not require visual identification.
• The secondary information is closely associated with the main label.
• Preserving a clean and compact layout is more important than adding imagery.

**Use leading and trailing content together**
Use both positions when they communicate different and complementary information.

When both positions are enabled:
• The leading element should support identification.
• The trailing element should provide secondary information.
• The main label must remain the clearest and most important element.
• Both elements must remain understandable without relying on colour alone.
• Avoid using the same container type in both positions.
• Avoid repeating the same information visually and textually.
• Do not use both positions only to create visual balance.

---

## Leading

Leading content appears before the main label and supports recognition or identification.
Use it when the visual element helps users understand the card more quickly. Do not add leading content only to decorate the card. Only one leading container should be displayed per card.

**`False`** No leading content is displayed. The main content starts at the default horizontal padding.

**`True`** A leading container is displayed before the main content. Use the Leading container type property to define its content, such as an icon, image, avatar, flag, value or custom slot.

---

## Leading container type

**`Icon`** Use an icon to reinforce the meaning of the item or help users identify a familiar category, object or status.

**Size**
Controls the visual prominence of the icon.

⚠️ Use the same icon size for comparable cards within the same card collection.
Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use for standard and compact cards. This is the preferred size when the icon provides secondary visual support.

**`Large`** Use when the icon needs stronger prominence or when the card has a larger height, multiline content or additional supporting information.

**Status**
Defines the semantic colour applied to the icon.

**`Not functional`**

**`Neutral`** Use when the icon does not communicate a specific semantic status.

**`Functional`** ⚠️ Use semantic statuses only when the icon represents the same meaning as the status. Do not use a semantic colour only for decoration or visual variety.

**`Positive`** Use for successful, completed or beneficial states.

**`Info`** Use for neutral information that requires additional attention.

**`Warning`** Use for situations that may require caution or user awareness.

**`Negative`** Use for errors, failures, destructive outcomes or critical problems.

**Badge**
Controls whether an additional badge is displayed with the icon.

**`False`** Display the icon without a badge.

**`True`** Display a badge when a notification must be associated with the icon.

**`Image`** Use an image when visual identification is important, for example for a product, service, destination, article or media item.
Do not use an image when it does not add useful information.

**Size**
Controls the dimensions and visual prominence of the image.

⚠️ Use the same image size for comparable cards within the same card collection.
Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use in compact or information-dense card layouts where the image remains secondary to the text.

**`Large`** Use in standard cards where visual identification is important.

**`Xlarge`** Use when the image is a significant part of the card content, such as a product or media preview.

**Ratio**
Defines the aspect ratio of the image container.

⚠️ Do not crop meaningful content in a way that makes the image difficult to understand. Use an appropriate focal point when the source image is cropped automatically.

**`1x1`** Use for square visual content such as products, logos, album covers or profile-related imagery.

**`16x9`** Use for landscape content such as editorial images or wide media thumbnails.

**Rounded corner**
Defines whether the image is displayed with square or rounded corners. The corner style should reflect the type of content and remain consistent with the visual language used elsewhere in the product.

**`False`** Displays the image with square corners.

**`True`** Displays the image with rounded corners.

**Animated**
Defines whether the image can contain animated content. Use animation only when it provides meaningful value to the user and does not distract from the primary content or interaction.

**`False`** Displays a static image. Use when animation does not provide meaningful information or when a still representation is sufficient.

**`True`** Displays animated content, such as a GIF or WEBP file. Use when the animation provides meaningful visual information or helps communicate the nature of the content.

**⚠️ Motion & Animation accessibility rules**
The use of motion and animation in our products and components requires particular attention to the accessibility guidelines available in the dedicated section of this documentation.

**`Avatar`** Use an avatar to represent a person, profile, team, organisation or account. An avatar supports visual recognition but must always be accompanied by a visible text label identifying the represented entity.

**Size**

**`Medium`** Use in compact cards or when the avatar is secondary to the content.

**`Large`** Use in standard profile, people or account cards.

**`Xlarge`** Use when identity is a primary part of the card or when additional avatar details must remain visible.

**Type**
Defines the content displayed inside the avatar.

**`Image`** Use when a profile image, portrait or organisation logo is available. Avoid images containing small text or complex details.

**`Initials`** Use as a fallback when no suitable image is available. Initials should be generated consistently from the displayed name. Use a predictable rule, such as the first letters of the first and last names. Do not rely on initials alone to identify the person, as several users may share the same initials.

**`Icon`** Use for generic accounts, anonymous profiles, teams or entities that do not have an individual image or initials.

**Badge**
Controls whether a badge is displayed on the avatar.

**`False`** Display the avatar without additional status information.

**`True`** Display a badge when a secondary status must be associated with the avatar, such as availability, verification or account state.

⚠️ Do not use the badge as the only way to communicate an important state. The same information should be available through text or assistive technology.
When Badge is enabled, additional properties become available.

**Badge type**
Defines the visual content used in the avatar.

**`Badge`** Use for simple state indicators. Do not rely on colour alone to communicate a functional status. Provide an additional text label or accessible description.

**`Badge Icon`** Use when the badge carries important or specific information. The icon must support understanding without relying on colour alone and should have an accessible description when required.

⚠️ For Neutral and Accent statuses, the icon can be adapted to the context. For functional statuses, the icon is predefined and must not be changed, ensuring consistent and accessible status communication across the design system.

**Badge status**
Defines the semantic colour of the badge.

⚠️ Colour alone must not communicate the state. Provide a visible label, description, tooltip where appropriate, or an accessible text equivalent in implementation.

**`Non functional`**

**`Neutral`** Use for non-semantic or inactive information.

**`Accent`** Use to highlight a branded or selected state that is not positive, negative or informational.

**`Functional`**

**`Positive`** Use for available, active, verified or successful states.

**`Info`** Use for additional neutral information.

**`Warning`** Use for a state requiring attention or caution.

**`Negative`** Use for unavailable, failed, blocked or notification states.

**`Flag`** Use a flag to represent a country, territory or regional context. A flag may support visual recognition, but it must not replace the corresponding country, territory or language name. Flags should be used carefully because countries, languages and nationalities do not always have a one-to-one relationship.

⚠️ Always provide the corresponding country, territory or language name as visible text.
The accessible name should describe the represented country or territory, not the visual appearance of the flag.

**`Slot`** Use Slot for custom leading content that cannot be represented by Icon, Image, Avatar or Flag.
Slot provides flexibility for specific product requirements, but it should be used as an exception rather than the default solution.

**⚠ Interaction**
The Static card item is non-interactive. Custom Slot content must not contain:
• Buttons
• Links
• Checkboxes
• Radio buttons
• Toggles
• Menus
• Any independently focusable element

---

## Trailing

Trailing content appears after the main content and communicates secondary information.
It can be used for a value, status, category or supplementary visual element.
The trailing content should remain concise and should not contain information that is more important than the primary label.

**`False`** No trailing content is displayed. The main content can use the available width of the card.

**`True`** A trailing container is displayed after the main content.
Use the Trailing container type property to define its content, such as text, a badge, tag, icon, image, value or custom slot.

---

## Trailing container type

**Shared container types**
The following types reuse the properties and guidance documented under Leading container type:
  • Icon
  • Image
  • Avatar
  • Flag
  • Slot

⚠️ Their meaning and nested properties remain the same. Only their position within the card changes.

⚠️ Do not use the same container type in both the leading and trailing positions within the same card. If a type is used as leading content, choose a different trailing type or disable the trailing container.

**`Text`** Use Text to display a short value or secondary piece of information associated with the primary label.

⚠️ Keep trailing text concise. When the information requires a sentence or explanation, use the Description or Helper text property instead.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information that should remain clearly readable without drawing more attention than the primary label.

**`Label muted`** Use Label muted for low-priority metadata that supports the item but is not essential to its immediate understanding.

**`Label strong`** Use Label strong when the trailing value requires additional visual emphasis, for example when users need to compare values across a group of cards.

**`Label + Extra label`** Use Label + Extra label when a value requires a short qualifier, unit or supporting label.

**`Badge`** Use a Badge to communicate a compact status or notification associated with the card.
A badge should contain secondary information and must not replace the primary label or description.

**Type**

**`Badge`** Use Badge for a short textual status. Keep the label concise and use terminology consistently throughout the product.

**`Badge count`** Use Badge count to display a short numerical quantity, such as unread messages, notifications or occurrences.
The count must have a clear relationship with the primary subject of the card. Users should not need to guess what is being counted.

**Status**
The Status property defines the semantic colour and meaning of the badge.

⚠️ Colour must not be the only way the meaning is communicated. Provide an equivalent accessible description.

**`Not functional`**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Use to highlight branded, selected or noteworthy information that does not correspond to another semantic status.
Do not use Accent solely to make a card more visually prominent.

**`Functional`**

**`Positive`** Use for successful, active, available or completed states.

**`Info`** Use for additional neutral information that may require attention but does not indicate success or risk.

**`Warning`** Use for states that require caution, awareness or future action.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

**Badge size**

**`XSmall`** Use for a very compact badge within small cards or dense layouts.

**`Small`** Use for a standard compact notification badge.

**`Medium`** Use when the badge requires stronger visibility or accompanies a larger card.

**`Large`** Use only in spacious layouts where the badge is a significant secondary element.

**Badge count size**

**`Medium`** Use Medium for standard or compact cards.

**`Large`** Use Large when the card uses larger dimensions or when a larger badge is required to remain visually balanced with the surrounding content.

**State**

**`Enabled`** Use when the badge communicates a current and applicable status or count.

**`Disabled`** Use when the status represented by the badge is inactive, unavailable or no longer applicable.

Because the Static card item is non-interactive, Disabled does not mean that the badge cannot be clicked. It communicates the state of the represented information.
Do not use Disabled merely to reduce visual emphasis.

**`Tag`** Use a Tag to communicate a category, attribute, classification or compact status associated with the card. In a Static card item, a tag is informational.

**Appearance**

**`Emphasized`** Use Emphasized when the tag carries information that should be easy to notice while remaining secondary to the primary label.

**`Muted`** Use Muted for low-priority categories or supporting metadata.

**Status**

**`Not functional`**

**`Neutral`** Use Neutral for general categories, attributes or metadata without a specific semantic meaning.

**`Accent`** Use Accent for branded or noteworthy information that does not correspond to a functional status.

**`Functional`**

**`Positive`** Indicates a successful or confirmed status, such as completed tasks or active states. Always use the functional icon associated with success.

**`Warning`** Signals potential issues or actions that require user attention. Use with caution. Always use the functional icon associated with warning.

**`Negative`** Communicates errors, failed actions, or negative outcomes. Always use the functional icon associated with error.

**`Info`** Represents informational content, tips, or supportive context. Always use the functional icon associated with information.

**Layout**

**`Text only`** A tag that displays only text. Used for simple labels, categories, or keywords without additional visual elements.

**`Text + Bullet`** A tag with a small indicator (bullet) alongside the text. Used to show status, presence, or activity next to the label.

**`Text + Icon`** A tag that includes an icon before the text. Used to visually reinforce the meaning of the tag.

**Size**

**`Small`** Use Small as the standard and recommended tag size within the card. It keeps the tag visually secondary, preserves space for the main content and works well in compact or information-dense card layouts.

**`Default`** Use Default when the card uses a larger layout or when the tag must align with other Default-size tags in the same interface.

**State**

**`Enabled`** The default state of the tag, used to display the main information or status.

**`Loading`** A state where the tag shows a loader together with text.

**`Disabled`** A non-active state of the tag. It appears "dimmed" to indicate that it is unavailable or not relevant.

**`Skeleton`** A placeholder state shown before the actual data is loaded.

**Rounded corner**

**`False`** A tag with sharp, square corners. Squared tags provide a more formal, structured, or technical feel. They are often used in business contexts to label promotions, offers, or important notices.

**`True`** A tag with fully rounded corners, creating a pill-shaped appearance. Rounded tags offer a softer and more approachable look, suitable for most modern interfaces.

This option is available for all brand themes

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Available |
| Wireframe | Available |

---

## Divider

**`False`** No divider is displayed.
Use this option when the card is already separated from surrounding content by spacing, an individual background, an outline or another clear visual boundary.

**`True`** A divider is displayed along the bottom edge of the card.
Use it when several cards are vertically grouped on the same surface without individual outlines and subtle visual separation improves scanning.
Do not use a divider as the only boundary for a standalone card.

---

## Helper text

**`False`** No helper text is displayed.

**`True`** Helper text is displayed below the primary content.
Use helper text for additional information required to interpret the card content correctly.

---

## Background

**`False`** The card uses the surrounding container surface without an individual background.
Use this option when the card belongs to a visually grouped layout and spacing, an outline or a divider provides sufficient separation.

**`True`** A background is applied to the card.
Use it when the card needs clear visual separation from its surrounding context or represents a distinct read-only content area.

---

## Label type

**`Default`** Use Default for most cards.
It provides the standard visual hierarchy and should be the preferred option for common labels, names and titles.

**`Bold`** Use Bold when the primary label requires stronger emphasis.

Suitable for:
• Important card titles.
• Card collections where primary labels must be scanned quickly.

**`Slot`** Use Slot when the standard label cannot support the required content structure.

The Slot may be used for custom primary content such as:
• A product-specific text arrangement.
• A combination of text elements not supported by the standard properties.

---

## Overline

**`False`** No overline is displayed.

**`True`** A short contextual label is displayed above the primary label. Use an overline to communicate a short contextual qualifier.

---

## Extra label

**`False`** No extra label is displayed.

**`True`** An additional short label is displayed with the primary label.

Use an extra label for:
• A secondary name.
• A short complementary value.
• A short piece of information directly related to the label.

---

## Description

**`False`** No supporting description is displayed.

**`True`** Supporting text is displayed below the primary label.
Use a description when users need additional context to understand the card content.

---

## Slot (bottom)

The bottom slot adds a custom content area below the main card content.
Use it when the information cannot be clearly represented by the standard Description or Helper text properties.

**`False`** No additional content is displayed below the main content.

**`True`** A custom content area is displayed below the main content.

It may contain:
• A progress indicator.
• A compact group of metadata.
• A visual preview or status summary.
• Product-specific supporting content.

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important part of the message. It must never compensate for unclear writing.

**Strong text**
• Strong text can be used sparingly in the helper text or description to highlight key information, such as a status, date, amount, or required step. Rich text must use the **Label/Medium/Strong** token only. No other text styles or custom font weights should be used.

**⚠️ Underline text and Hyperlinks**
• Underlined text must not be applied manually in the Description or Helper text, as users commonly interpret underlined content as a hyperlink.

---

## Multiline and responsiveness

**Multiline**
The Static card item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.
The item expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the item contains a Description, Helper text or Bottom slot. The navigation indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.
⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make navigation lists more difficult to scan.

**Max-width vs full-width**
The Static card item does not have a default maximum width. Its width is defined by its parent container or navigation layout.
The item’s interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or navigation indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability. The item’s background, divider, hover, pressed and focus treatments must still cover the complete navigation target.

The navigation indicator remains positioned at the logical edge of the item:
• At the logical end for the Next layout.
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.
⚠️ Do not apply a text maximum width that creates a large visual gap between the Label and related Trailing content. The relationship between all parts of the item must remain clear.

**User zoom in/out**
The card item must remain readable, operable and complete when users zoom the interface or increase the text size.
The component must adapt without clipping, overlapping or hiding meaningful information.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the text area and remove non-essential content when space is limited.

• Text must resize with the user’s browser or system settings. Text resizing must not be blocked.
• The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap when required.
• The item must expand vertically according to its content. Do not use a fixed height.
• The entire visible item must remain one interactive target. Zoom must not reduce the clickable area to the Label or navigation indicator.
• The navigation indicator must remain visible and must not overlap the text or move onto a separate unrelated line.
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.
• Optional decorative content may be simplified on narrow layouts, but meaningful status, destination and supporting information must remain available.
• Do not truncate essential destination labels, statuses, prices, dates or values to preserve the original desktop layout.
• Focus, hover and pressed treatments must adapt to the expanded item dimensions and continue to cover the complete navigation target.
• In the Previous layout, the navigation indicator remains at the logical start. Leading content is not supported, including after responsive reflow.
• In the Next layout, the navigation indicator remains at the logical end. Leading content may be retained when it does not prevent the Label from reflowing correctly.
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the item on one line.

---

## Technical layout adjustments

Even though, in Figma, the component structure is unique (for easier use by designers), technically the versions differ in order to respect best practices for each environment (paradigm shift between the web “Container” vs. the native “Edge-to-Edge”):

**Web (mobile, tablet, and desktop)**
The component is contained within the browser window and has “safety margins.” It therefore cannot appear in the area corresponding to the margin grid.
The component has internal padding-inline, and its display position must be between several columns (which varies depending on the number of containers used on a horizontal row).

**Native app (Android, iOS, Flutter)**
The display position of the component corresponds to the entire screen display area (edge to edge).
Its internal padding-inline is therefore replaced by the grid-margin tokens.

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

Concrete application to the List item → Illustrations or animated images (leading or trailing container):

**Pause, Stop, Hide**
For an animation that starts automatically and lasts more than 5 seconds, users must be able to pause, stop, or hide the animation when it is presented alongside other content.
When the animation is short, lasting 5 seconds or less, no pause, stop, or hide control is required.

**Reduced Motion**
If Reduced Motion is enabled, any decorative or not essential animation that is not necessary to understand the content must be removed or replaced with a static representation.
If an animation conveys essential information, that same information must remain available through a non-animated alternative.

---

## Accessibility

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
