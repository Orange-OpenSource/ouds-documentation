# Guideline

## Intro 👈🤖

An accordion card item is a self-contained card that expands and collapses to reveal related content, so users open only the sections they need.

---

## Definition

An Accordion card item is an interactive, self-contained card used to reveal or hide related content within the current context. Use it when an accordion section requires stronger visual grouping or prominence than a standard Accordion list item.
The card may be displayed independently or within a card-based accordion collection and may use a distinct Background, Outline or Rounded corners.

---

## Best for 👈🤔

✅ Organising related information into distinct cards users can scan and open one by one

✅ Shortening long pages when users are unlikely to read every section

✅ Product details, such as specifications, delivery terms or included services

✅ Offers, plans or options presented as separate blocks, each with its own details

✅ Small screens and side panels, where space is limited

✅ Sections whose labels can describe their content precisely

✅ Showing a value, status or category for each section before it is opened

✅ Content that users compare by opening several sections at once

✅ Sections recognised faster with an icon, an image, an avatar or a flag

✅ Optional or secondary content only: information all users must see stays visible on the page

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The card that holds the trigger and its expanded content, with optional outline, background and rounded corners | N |
| 2 | Leading container | Icon, image, avatar, flag or slot that helps users recognise the section | Y |
| 3 | Label | Names the section; Default, Bold or Slot, with optional overline and extra label | N |
| 4 | Description | Supporting text below the label that says what the section contains | Y |
| 5 | Trailing container | Secondary information such as text, a badge or a tag | Y |
| 6 | Expanding indicator | Chevron or plus icon that shows whether the section is open, at the end or the start | N |
| 7 | Expanded container | The revealed content: Expanded text and/or the Expand slot | Y |
| 8 | Divider | Separates the items of a group that share the same surface | Y |

---

## Size

**`Default`** Use the Default size in most interfaces.
It provides sufficient spacing for standalone accordion cards, card collections, multiline Labels and visual elements such as Icons, Avatars, Images or Badges.

**`Small`** Use the Small size in compact card-based layouts where information density is important.

The Small size is best suited to:
• Short section Labels.
• Simple supporting information.
• Compact desktop card layouts.

⚠️ Do not mix Default and Small cards within the same accordion card collection unless they represent clearly different categories or levels of hierarchy.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use the Default size in most interfaces, especially with multiline labels or visuals  
❌ **Don't:** Switch to Small only to fit more sections on screen

✅ **Do:** Use Small in compact desktop layouts with short labels and simple supporting information  
❌ **Don't:** Use Small where triggers become hard to hit on touch screens

✅ **Do:** Keep one size across a continuous accordion so the items scan as a set  
❌ **Don't:** Mix Default and Small items without a clear change of section or hierarchy

✅ **Do:** Let the tallest element define the height of the trigger  
❌ **Don't:** Force a fixed height that clips multiline content

✅ **Do:** Check the Small size with real, translated labels before adopting it  
❌ **Don't:** Assume short English labels stay short in every language

---

## Alignment

**`Center`** Center alignment is the default for card triggers containing:
• A single-line Label.
• Short supporting content.
• Leading and Trailing elements with similar dimensions.

⚠️ Do not use Center alignment when it makes an Icon, Avatar, value or Expanding indicator appear visually disconnected from the main content.

**`Top`** Use Top alignment when:
• The Label wraps onto multiple lines.
• A Description or Extra label is displayed.
• The Bottom slot is enabled.
• Leading or Trailing content must remain aligned with the beginning of the text.
• The different content areas have noticeably different heights.

⚠️ Top alignment only changes the visual alignment of the trigger content. It must not affect the expand / collapse behaviour or the layout of the Expanded content.

---

## alignment_do_&_dont 👈🤔

✅ **Do:** Use Center alignment for single-line labels with leading and trailing elements of similar height  
❌ **Don't:** Keep Center alignment when it disconnects the icon or the Expanding indicator from the label

✅ **Do:** Use Top alignment when the label wraps, or a Description, Extra label or Bottom slot is shown  
❌ **Don't:** Center the Expanding indicator against a tall block of text

✅ **Do:** Keep leading and trailing content aligned with the first line of the text in Top alignment  
❌ **Don't:** Let leading and trailing content float at different heights

✅ **Do:** Apply the same alignment to items with the same content structure  
❌ **Don't:** Mix alignments between similar items of the same accordion

✅ **Do:** Keep the expand and collapse behaviour identical whatever the alignment  
❌ **Don't:** Change the interactive area when the alignment changes

---

## Outlined

**`False`** No Outline is displayed.
Use this option when the card is already clearly separated from surrounding content by its Background, spacing or parent layout.

**`True`** An Outline is displayed around the complete accordion card. Use it when the card needs clearer visual separation from a surface with a similar Background.

---

## outlined_do_&_dont 👈🤔

✅ **Do:** Use the outline when a card must be delimited on a surface of the same colour  
❌ **Don't:** Add an outline to cards that already stand out through their background

✅ **Do:** Apply the same outline setting to every card of a group  
❌ **Don't:** Mix outlined and non-outlined cards in the same accordion

✅ **Do:** Keep the outline around the trigger and its expanded content as one card  
❌ **Don't:** Let the outline separate the trigger from its own content

✅ **Do:** Keep hover, pressed and focus treatments clearly visible on outlined cards  
❌ **Don't:** Rely on the outline to show focus

✅ **Do:** Use spacing between cards to separate them  
❌ **Don't:** Stack outlined cards edge to edge so borders double

---

## Rounded corner

Although this rendering option is available in the properties of each Accordion card item in Figma, its configuration should be defined consistently across the product or service in which the component is used.

Equivalent cards within the same interface should not arbitrarily mix Rounded corner = True and Rounded corner = False.

**`False`** The square rendering corresponds to Orange's historical visual style. It provides a structured, robust and utility-driven appearance and remains the default treatment for digital interface components where appropriate.

**`True`** The rounded rendering provides a softer and more tactile card appearance while preserving the overall brand identity. Use it when rounded card surfaces are part of the visual language of the product or service.

This option is technically not available for all brand themes
Here’s the list of rounded corners availability by brand theme

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Unavailable |
| Wireframe | Unavailable |

---

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Apply the same corner setting to every card of a product or service  
❌ **Don't:** Mix square and rounded cards within the same product

✅ **Do:** Keep square corners as the default Orange style  
❌ **Don't:** Switch to rounded corners for a single screen or campaign

✅ **Do:** Use rounded corners when the whole product adopts the softer, more tactile style  
❌ **Don't:** Round the cards while buttons and inputs stay square

✅ **Do:** Check that the brand theme supports rounded corners before using them  
❌ **Don't:** Enable rounded corners on a theme where the option is unavailable

✅ **Do:** Decide the corner style once, at product level  
❌ **Don't:** Leave the choice to each designer or each screen

---

## Expanded

**`False`** Use the collapsed state when additional content is hidden.
Only the card trigger remains visible, allowing users to scan available sections without displaying all supporting information at once.

**`True`** Use the expanded state when additional content related to the trigger is visible. The card expands vertically and the revealed content appears below the trigger within the same card surface. The revealed content should directly explain, complete or provide additional information about the section identified by the Label.

⚠️ Expanded content must remain clearly associated with its trigger. Avoid revealing content that introduces an unrelated topic or appears to belong to another card.

---

## expanded_do_&_dont 👈🤔

✅ **Do:** Start with the sections collapsed so users can scan all the labels  
❌ **Don't:** Open every section by default and lose the overview

✅ **Do:** Let users open several sections at the same time  
❌ **Don't:** Close a section automatically when users open another one they may want to compare

✅ **Do:** Keep the revealed content directly related to the label above it  
❌ **Don't:** Reveal content that introduces an unrelated topic

✅ **Do:** Use an accordion for content users can skip, and show essential content directly on the page  
❌ **Don't:** Hide information all users must read inside a collapsed section

✅ **Do:** Expose the expanded state to assistive technologies on the trigger  
❌ **Don't:** Rely on the direction of the indicator alone to convey the state

---

## Expanded text

**`False`** No standard text content is displayed in the expanded area.
Use this option when the expanded content is provided only through Expanded slot, or when no additional text is required.

**`True`** Standard text content is displayed below the card trigger when the card is expanded.

Use it for:
• Short explanations.
• Additional details.
• Instructions.
• Supporting information related to the accordion topic.

⚠️ Keep Expanded text focused on the topic introduced by the trigger.
For complex structures, multiple components or interactive content, use Expanded slot instead.

---

## expanded_text_do_&_dont 👈🤔

✅ **Do:** Use Expanded text for short explanations, details or instructions about the topic  
❌ **Don't:** Paste a long article into the expanded area

✅ **Do:** Keep the text focused on the topic introduced by the trigger  
❌ **Don't:** Mix several unrelated topics in one section

✅ **Do:** Use the Expand slot for complex structures, several components or interactive content  
❌ **Don't:** Force lists, tables or forms into plain Expanded text

✅ **Do:** Split long content into short paragraphs  
❌ **Don't:** Make the expanded area scroll on its own

✅ **Do:** Write the content so it stands alone when read without the other sections  
❌ **Don't:** Refer to content hidden in another collapsed section

---

## Slot (Below text)

The Below text slot adds custom supporting content directly below the main text content.
Use it when additional information needs to remain closely associated with the Label, Description or other text content rather than span the complete trigger width.
The slot follows the position and alignment of the text container. Its exact placement may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom content area is displayed directly below the main text content.

⚠️ Keep Below text content concise.
⚠️ Use Slot (bottom) when the content requires a wider area outside the text container.
⚠️ Use Slot (Expand) when the content should only become visible after expansion.

---

## slot_below_text_do_&_dont 👈🤔

✅ **Do:** Use the Below text slot for content that must stay close to the label and description  
❌ **Don't:** Use it for content that needs the full width of the trigger

✅ **Do:** Keep Below text content concise  
❌ **Don't:** Fill the slot with content that pushes the label out of view

✅ **Do:** Use the Bottom slot when the content needs a wider area  
❌ **Don't:** Squeeze wide content into the text column

✅ **Do:** Use the Expand slot when the content should appear only after expansion  
❌ **Don't:** Show details in the trigger that belong in the expanded area

✅ **Do:** Keep the slot content part of the trigger and non-interactive  
❌ **Don't:** Place a button, link or control inside the slot

---

## Slot (Bottom)

The Bottom slot adds custom supporting content below the complete trigger content.
Use it when information needs to remain visible independently of the Expanded state and requires more space or flexibility than the standard text properties.
The slot is positioned at the bottom of the trigger area. Its exact width and alignment may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom supporting area is displayed below the main trigger content.

⚠️ Bottom slot content remains part of the trigger and should not behave as an independent action.
⚠️ Use Slot (below text) when the information needs to remain closely aligned with the main text content.
⚠️ Use Slot (Expand) when the content should only become visible after expansion.

---

## slot_bottom_do_&_dont 👈🤔

✅ **Do:** Use the Bottom slot for supporting content that stays visible whatever the Expanded state  
❌ **Don't:** Use it for content that should appear only after expansion

✅ **Do:** Use it when the content needs more width than the text container offers  
❌ **Don't:** Use it for a short note that fits below the text

✅ **Do:** Keep Bottom slot content part of the trigger  
❌ **Don't:** Make the slot content behave as an independent action

✅ **Do:** Use Top alignment when the Bottom slot is enabled  
❌ **Don't:** Keep Center alignment on a trigger made taller by the slot

✅ **Do:** Keep the content short enough for the list to remain scannable  
❌ **Don't:** Turn every trigger into a tall card with a heavy Bottom slot

---

## Slot (Expand)

The Expand slot adds custom content inside the expanded area of the Accordion.
Use it when the revealed content requires a structure that cannot be represented clearly by standard Expanded text alone.
The slot is displayed only when the Accordion is expanded. Its exact placement inside the expanded area may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom content area is displayed when the Accordion is expanded.

⚠️ Use Slot (below text) or Slot (bottom) when the content needs to remain visible in both collapsed and expanded states.

---

## slot_expand_do_&_dont 👈🤔

✅ **Do:** Use the Expand slot when standard Expanded text cannot carry the structure  
❌ **Don't:** Use the slot for a simple sentence that Expanded text handles

✅ **Do:** Follow the spacing and responsive rules of the design system inside the slot  
❌ **Don't:** Let slot content overflow or break the alignment with the trigger

✅ **Do:** Keep interactive content in the expanded area reachable by keyboard in a logical order  
❌ **Don't:** Leave focusable content reachable while the section is collapsed

✅ **Do:** Use the Below text or Bottom slot for content that must stay visible when collapsed  
❌ **Don't:** Hide information users need before opening in the Expand slot

✅ **Do:** Keep the slot content related to the trigger label  
❌ **Don't:** Nest another accordion inside the Expand slot

---

## Alternative icon

**`False`** Use the default chevron as the Expanding indicator.
This is the recommended option for standard accordion patterns and clearly communicates that additional content can be expanded or collapsed.

**`True`** Use the alternative expand / collapse icon when the product context requires the + pattern instead of a chevron.
The icon must communicate the same expanded state consistently across all items within the same accordion.

⚠️ Do not mix chevron and + indicators within the same accordion. Different indicators may suggest different behaviours even when the interaction is identical.

---

## alternative_icon_do_&_dont 👈🤔

✅ **Do:** Use the default chevron for standard accordion patterns  
❌ **Don't:** Switch to the plus icon without a product reason

✅ **Do:** Use the plus and minus pattern when the product context requires it  
❌ **Don't:** Mix chevron and plus indicators within the same accordion

✅ **Do:** Use the same indicator for every item of an accordion  
❌ **Don't:** Change the indicator from one item to the next

✅ **Do:** Let the indicator change with the expanded state  
❌ **Don't:** Show the same icon whether the section is open or closed

✅ **Do:** Keep the whole trigger clickable, not only the indicator  
❌ **Don't:** Limit the interactive area to the icon

---

## Reverse

**`False`** Use False as the standard layout.
The Expanding indicator is displayed at the logical end of the card trigger, after the main content and any optional Trailing content.

**`True`** Use Reverse when the Expanding indicator needs to appear at the logical start of the trigger. The indicator is positioned before the main content.

⚠️ Reverse changes only the position of the Expanding indicator. It does not change the meaning of the card, reading order or expand / collapse behaviour.

⚠️ Keep the same indicator position for equivalent items within the same accordion. Do not alternate between standard and reversed layouts only for visual variety.

---

## reverse_do_&_dont 👈🤔

✅ **Do:** Keep the Expanding indicator at the end of the trigger by default, so labels align with the page content  
❌ **Don't:** Reverse the layout only for visual variety

✅ **Do:** Use Reverse when the indicator must appear before the content, for example in a tree-like structure  
❌ **Don't:** Alternate standard and reversed items in the same accordion

✅ **Do:** Keep the same indicator position for equivalent items across the product  
❌ **Don't:** Use different positions for accordions that play the same role

✅ **Do:** Follow the reading direction: the start and the end mirror in right-to-left layouts  
❌ **Don't:** Hard-code the indicator to the left or to the right

✅ **Do:** Keep the focus and reading order identical in both layouts  
❌ **Don't:** Let the visual position change what is announced first

---

## Leading

Leading content appears before the main Label and supports recognition or identification of the accordion section. Use it when a visual element helps users understand the card topic more quickly.
Leading content remains inside the accordion trigger and must not behave as an independent action.

**`False`** No Leading content is displayed. The main content starts at the default horizontal padding.

**`True`** A Leading container is displayed before the main content. Use the Leading container type property to define its content, such as an Icon, Image, Avatar, Flag thumbnail or custom Slot.

---

## leading_do_&_dont 👈🤔

✅ **Do:** Add leading content when a visual cue helps users recognise the section faster  
❌ **Don't:** Add decorative leading content that tells users nothing

✅ **Do:** Keep leading content inside the single accordion trigger  
❌ **Don't:** Turn the leading element into an independent action

✅ **Do:** Use leading content consistently for all items of an accordion  
❌ **Don't:** Show leading content on some items only

✅ **Do:** Provide a text alternative when the leading visual adds information not in the label  
❌ **Don't:** Repeat the label in the text alternative of the leading visual

✅ **Do:** Use the Leading container type to choose an icon, image, avatar, flag or slot  
❌ **Don't:** Recreate a leading visual outside the component

---

## Leading container type

**`Icon`** Use an Icon to reinforce the meaning of the accordion section or help users identify a familiar category, object, service or status.

**Size**
Controls the visual prominence of the Icon.

⚠️ Use the same Icon size for comparable cards within the same accordion collection. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use for standard and compact cards. This is the preferred size when the Icon provides secondary visual support.

**`Large`** Use when the Icon needs stronger prominence or when the card trigger has a larger height, multiline content or additional supporting information.

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

**`Image`** Use an Image when visual identification of the accordion section is important, for example for a product, service, article, media topic or other recognisable subject.
The image should help users recognise the subject before expanding the section.

**Size**
Controls the dimensions and visual prominence of the image.

⚠️ Use the same image size for equivalent items within the same accordion. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use in compact or information-dense accordions where the image remains secondary to the text.

**`Large`** Use in standard accordion items where visual identification is important.

**`Xlarge`** Use when the image is a significant part of recognising the content, such as a product or media preview.

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
Displays animated content, such as a GIF or WEBP file. Use when the animation provides meaningful visual information or helps communicate the nature of the content.

**`False`** Displays a static image. Use when animation does not provide meaningful information or when a still representation is sufficient.

**`True`** Displays animated content. Use when the animation provides meaningful visual information or helps communicate the nature of the content.

**⚠️ Motion & Animation accessibility rules**
The use of motion and animation in our products and components requires particular attention to the accessibility guidelines available in the dedicated section of this documentation.

**`Avatar`** Use an avatar when the accordion section relates to a person, profile, team, organisation or account. An avatar supports visual recognition but must always be accompanied by a visible text label identifying the represented entity.

**Size**

**`Medium`** Use in compact accordions or when the avatar is secondary to the content.

**`Large`** Use in standard people or account sections.

**`Xlarge`** Use when identity is a primary part of the section or when additional avatar details must remain visible.

**Type**
Defines the content displayed inside the avatar.

**`Image`** Use when a profile image, portrait or organisation logo is available. Avoid images containing small text or complex details.

**`Initials`** Use as a fallback when no suitable image is available. Initials should be generated consistently from the displayed name.
Use a predictable rule, such as the first letters of the first and last names. Do not rely on initials alone to identify the person, as several users may share the same initials.

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

**`Flag`** Use a flag to represent a country, territory or regional context when this information helps users identify the accordion section.
A flag may support visual recognition, but it must not replace the corresponding country, territory or language name. Flags should be used carefully because countries, languages and nationalities do not always have a one-to-one relationship.

⚠️ Always provide the corresponding country, territory or language name as visible text. The accessible name should describe the represented country or territory, not the visual appearance of the flag.

**`Slot`** Use Slot for custom leading content that cannot be represented by Icon, Image, Avatar or Flag.
Slot provides flexibility for specific product requirements but should be used as an exception rather than the default solution.

**⚠️ Interaction**
The complete Accordion trigger already controls whether its associated content is expanded or collapsed.

Custom Slot content inside the trigger must not contain:
• Buttons
• Links
• Checkboxes
• Radio buttons
• Toggles
• Menus
• Any independently focusable element

Nested interactive elements create conflicting activation and focus behaviour and may make it unclear whether an interaction expands the accordion or activates another control.
When an independent action is required, place it inside the expanded content or use another component designed to support multiple actions.

---

## leading_container_type_do_&_dont 👈🤔

✅ **Do:** Match the type to the section: icon for categories, image for products or media, avatar for people, flag for countries  
❌ **Don't:** Use images or avatars only to add visual variety

✅ **Do:** Keep one size per container type within an accordion  
❌ **Don't:** Mix icon, image or avatar sizes arbitrarily in the same accordion

✅ **Do:** Always pair avatars and flags with a visible name  
❌ **Don't:** Rely on an avatar, initials or a flag alone to identify the section

✅ **Do:** Use semantic statuses only when they carry that meaning, backed by text  
❌ **Don't:** Use functional colours for decoration or as the only status cue

✅ **Do:** Keep Slot for content the standard types cannot express, and keep it non-interactive  
❌ **Don't:** Put buttons, links or controls inside a Slot

---

## Trailing

Trailing content appears after the main content and communicates secondary information related to the accordion section.
It may be used for a value, status, category or supplementary visual element that helps users understand the section before expanding it. Trailing content remains part of the accordion trigger and must not behave as an independent action.

**`False`** No Trailing content is displayed. The main content can use the available width before the Expanding indicator.

**`True`** A Trailing container is displayed after the main content and before the Expanding indicator. Use the Trailing container type property to define its content, such as Text, Badge, Tag, Icon, Image, Avatar, Flag or custom Slot.

⚠️ Keep sufficient visual separation between Trailing content and the Expanding indicator so that secondary information is not mistaken for the expand / collapse control.

---

## trailing_do_&_dont 👈🤔

✅ **Do:** Use trailing content for a value, status or category that helps users before they expand  
❌ **Don't:** Put information users need to identify the section only in the trailing area

✅ **Do:** Keep trailing content short so the label keeps most of the width  
❌ **Don't:** Let trailing content squeeze the label into excessive wrapping

✅ **Do:** Keep trailing content inside the single accordion trigger  
❌ **Don't:** Make trailing content behave as an independent action

✅ **Do:** Keep a clear separation between the trailing content and the Expanding indicator  
❌ **Don't:** Let trailing content be mistaken for the expand and collapse control

✅ **Do:** Disable the trailing container when it adds no useful information  
❌ **Don't:** Fill the trailing area just to balance the trigger

---

## Trailing container type

**Shared container type**
The following types reuse the properties and guidance documented under Leading container type:
Icon, Image, Avatar, Flag and Slot.

Their meaning and nested properties remain the same. Only their position within the card trigger changes.

⚠️ All Trailing content remains part of the same accordion trigger and must not suggest an independent action.
⚠️ Avoid using the same container type in both Leading and Trailing positions unless each element communicates clearly different information.

**`Trailing Text`** Use Text to display a short value or secondary piece of information associated with the accordion section.

⚠️ Keep Trailing text concise. When the information requires a sentence or explanation, use the Description or place the information inside the expanded content instead.
⚠️ Trailing text must not look like a separate link or action.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information that should remain clearly readable without drawing more attention than the primary Label.

**`Label muted`** Use Label muted for low-priority metadata that supports the card but is
not essential to understanding the accordion topic.

**`Label strong`** Use Label strong when the value requires additional visual emphasis, for example when users need to compare important values across several accordion cards.

**`Label + Extra label`** Use Label + Extra label when a value requires a short qualifier, unit or supporting label.

**`Trailing Badge`** Use a Badge to communicate a compact status or notification associated with the accordion section. A Badge contains secondary information and must not replace the primary Label or Description.

**Type**

**`Badge`** Use Badge for a short textual status. Keep the label concise and use terminology consistently throughout the product.

**`Badge count`** Use Badge count to display a short numerical quantity related to the accordion section, such as unread items, notifications or occurrences.

The count must have a clear relationship with the primary Label. Users should not need to guess what is being counted.

⚠️ When the meaning of the count is not obvious from the Label, provide additional context through visible or accessible text.

**Status**
The Status property defines the semantic colour and meaning of the Badge.

⚠️ Colour must not be the only way the meaning is communicated. Provide an equivalent accessible description.

**`Not functional`**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Use to highlight branded or noteworthy information that does not correspond to a functional status. Do not use Accent only to make the accordion card more visually prominent.

**`Functional`**

**`Positive`** Use for successful, active, available or completed states.

**`Info`** Use for additional neutral information that may require attention but does not indicate success or risk.

**`Warning`** Use for states that require caution, awareness or future action.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

**Badge size**

**`XSmall`** Use for very compact Badges within Small Accordion cards or dense card layouts.

**`Small`** Use for standard compact notification badge.

**`Medium`** Use when the Badge requires stronger visibility or accompanies a larger Accordion card.

**`Large`** Use only in spacious layouts where the Badge is a significant secondary element.

⚠️ Regardless of size, the Badge should remain visually secondary to the accordion Label and Expanding indicator.

**Badge count size**

**`Medium`** Use Medium for standard or compact Accordion cards.

**`Large`** Use Large when the Accordion card uses larger dimensions or when a larger Badge count is required to remain visually balanced with the surrounding content.

**State**

**`Enabled`** Use when the Badge communicates a current and applicable status or count.

**`Disabled`** Use when the information represented by the Badge is inactive, unavailable or no longer applicable.
The Badge state is independent from the Accordion card item state. A Disabled Badge does not disable the card or prevent users from expanding it.

⚠️ Do not use Disabled merely to reduce the visual emphasis of the Badge.

**`Trailing Tag`** Use a Tag to communicate a category, attribute, classification or compact status related to the accordion section. A Tag can provide useful context before expansion and help users scan or compare several accordion cards.

⚠️ The Tag is informational within the accordion trigger. It must not appear selectable or behave as an independent action.
⚠️ A Tag must not be used to communicate the Expanded state. Use the Expanding indicator for expand and collapse behaviour.

**Appearance**

**`Emphasized`** Use Emphasized when the Tag communicates information that should be easy to notice while remaining secondary to the primary Label.

**`Muted`** Use Muted for low-priority categories or supporting metadata.

**Status**

**`Not functional`**

**`Neutral`** Use Neutral for general categories, attributes or metadata without a specific semantic meaning.

**`Accent`** Use Accent for branded or noteworthy information that does not correspond to a functional status.

**`Functional`** ⚠️ Always use the functional text associated with success.

**`Positive`** Indicates a successful or confirmed status, such as completed tasks or active states.

**`Warning`** Signals potential issues or actions that require user attention.

**`Negative`** Communicates errors, failed actions, or negative outcomes.

**`Info`** Represents informational content, tips, or supportive context.

**Layout**

**`Text only`** A Tag that displays only text. Use for simple labels, categories or
keywords without an additional visual indicator.

**`Text + Bullet`** A Tag with a small indicator alongside the text. Use when the indicator helps reinforce a status, presence or activity.

**`Text + Icon`** A Tag that includes an icon before the text. Use when the icon helps users recognise or understand the meaning of the Tag more quickly.

**Size**

**`Small`** Use Small as the standard and recommended size within the Accordion card item.
It keeps the Tag visually secondary, preserves space for the primary Label and Expanding indicator, and works well in compact or information-dense layouts.

**`Default`** Use Default when the Accordion card uses a larger layout or when the Tag must align with other Default-size Tags in the same interface.

**State**

**`Enabled`** The default state of the Tag, used to display current information or status.

**`Loading`** Use Loading when the information represented by the Tag is being updated and the loading state itself is useful to users.

**`Disabled`** The Tag state does not control the Accordion card item. A Disabled Tag does not prevent the card from being expanded.

**`Skeleton`** A placeholder state shown before the Tag content is available.

**Rounded corner**

**`False`** Displays the Tag with square corners.
Use when the product context requires a more structured visual treatment or when square Tags are used consistently elsewhere in the interface.

**`True`** Displays the Tag with fully rounded corners.
Use the rounded appearance when it matches the visual language of the product and other Tags in the same interface.

⚠️ Keep the same corner treatment for equivalent Tags within the same accordion or product context.

This option is available for all brand themes

| Brand theme | Status |
|---|---|
| Orange | Available |
| Orange Compact | Available |
| Sosh | Available |
| Wireframe | Available |

---

## trailing_container_type_do_&_dont 👈🤔

✅ **Do:** Keep trailing text to one or two words, such as a value or a short status  
❌ **Don't:** Write sentences in trailing text; use Description instead

✅ **Do:** Give badge counts a clear meaning, for example “2 unread messages”  
❌ **Don't:** Show an isolated number whose meaning users must guess

✅ **Do:** Use tags for categories or compact statuses, in the Small size by default  
❌ **Don't:** Make a tag or badge interactive inside the item

✅ **Do:** Use a container type different from the leading one  
❌ **Don't:** Use the same container type in both positions

✅ **Do:** Pair functional statuses with their predefined icons and explicit text  
❌ **Don't:** Signal the status of a section with colour alone

---

## Divider

**`False`** No Divider is displayed.
Use this option when the card is already separated from surrounding content by spacing, a Background, an Outline or another clear visual boundary.

**`True`** A Divider is displayed along the bottom edge of the card.
Use it when several Accordion card items are vertically grouped within the same shared surface and additional visual separation improves scanning.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use dividers when several items share the same surface and need extra separation  
❌ **Don't:** Add dividers when items are already separated by spacing or backgrounds

✅ **Do:** Apply dividers consistently within an accordion  
❌ **Don't:** Divide only some of the adjacent items of the same accordion

✅ **Do:** Keep the whole trigger interactive around the divider  
❌ **Don't:** Let the divider split or reduce the interactive area of an item

✅ **Do:** Avoid a divider that doubles the edge of the surrounding container  
❌ **Don't:** Stack a divider against a container border

✅ **Do:** Use section headings or spacing to show groups of different meaning  
❌ **Don't:** Rely on dividers alone to communicate grouping

---

## Background

**`False`** The card uses the surrounding container surface without an individual Background. Use this option when spacing, an Outline or the parent card layout already provides sufficient visual separation.

**`True`** A Background is applied to the complete Accordion card.
Use it when the card needs stronger visual separation from its surrounding context or represents a distinct section within a card-based accordion layout.
When expanded, the same Background treatment should visually contain both the trigger and the revealed content.

⚠️ Background must not be used to communicate the Expanded state.

---

## background_do_&_dont 👈🤔

✅ **Do:** Use no background for standard continuous accordions  
❌ **Don't:** Add a background to every item of a long accordion by default

✅ **Do:** Add a background when an item must stand apart from its context or in a grouped layout  
❌ **Don't:** Use a background to signal selection, status or urgency

✅ **Do:** Keep hover, pressed and focus treatments clearly visible on the background  
❌ **Don't:** Choose a background that hides the interaction states

✅ **Do:** Apply the background consistently to items that play the same role  
❌ **Don't:** Mix items with and without a background in the same group without a reason

✅ **Do:** Keep the heading and button semantics independent of the background  
❌ **Don't:** Rely on the background alone to show where an item ends

---

## Label type

**`Default`** Use Default for most Accordion cards.
It provides the standard visual hierarchy and should be the preferred option for common section names, questions and topics.

**`Bold`** Use Bold when the primary Label requires stronger emphasis.

Suitable for:
• Important section names.
• Accordion card collections where Labels must be scanned quickly.

**`Slot`** Use Slot when the standard Label cannot support the required content structure.

The Slot may be used for custom primary content such as:
• A product-specific text arrangement.
• A combination of text elements not supported by the standard properties.

⚠️ The Label Slot remains part of the accordion trigger. Do not place an independent button, link or other interactive control inside it.

---

## label_type_do_&_dont 👈🤔

✅ **Do:** Use the Default label type for most items  
❌ **Don't:** Make every label bold; emphasis then loses its meaning

✅ **Do:** Use Bold when labels must be scanned quickly or item names are important  
❌ **Don't:** Mix Default and Bold labels in one accordion without a reason

✅ **Do:** Write specific, familiar labels that say what the section contains  
❌ **Don't:** Use vague labels such as “More”, “Click here” or “Learn more”

✅ **Do:** Use the label Slot only when standard properties cannot express the content  
❌ **Don't:** Put links, buttons or controls in the label Slot

✅ **Do:** Keep labels parallel in structure across the accordion  
❌ **Don't:** End short labels with a period when they are not sentences

---

## Overline

**`False`** No overline is displayed.

**`True`** A short contextual Label is displayed above the primary Label.
Use an Overline to provide a short qualifier that helps users understand the context of the accordion section before reading its main Label.
Keep the Overline concise and secondary to the primary Label.

---

## overline_do_&_dont 👈🤔

✅ **Do:** Use an overline for a short contextual qualifier, such as a category or section  
❌ **Don't:** Use the overline for the section name

✅ **Do:** Keep overlines to a few words  
❌ **Don't:** Write sentences in the overline

✅ **Do:** Use overlines consistently for items of the same kind  
❌ **Don't:** Show overlines on random items only

✅ **Do:** Keep the overline before the label in the reading order  
❌ **Don't:** Hide information users need to identify the section in the overline only

✅ **Do:** Use Top alignment when the overline makes the text block taller  
❌ **Don't:** Rely on the overline's style alone to convey meaning

---

## Extra label

**`False`** No extra label is displayed.

**`True`** An additional short Label is displayed with the primary Label.

Use an Extra label for:
• A secondary name.
• A short complementary value.
• A short piece of information directly related to the accordion section.

⚠️ The Extra label should provide useful context before expansion without competing with the primary Label.

---

## extra_label_do_&_dont 👈🤔

✅ **Do:** Use an extra label for a secondary name or a short complementary value  
❌ **Don't:** Use the extra label for long explanations; use Description instead

✅ **Do:** Keep the extra label directly related to the main label  
❌ **Don't:** Add unrelated metadata to the extra label

✅ **Do:** Keep it short so the label keeps priority  
❌ **Don't:** Let the extra label compete with the primary label

✅ **Do:** Show each value once, either in the extra label or in trailing text  
❌ **Don't:** Repeat the same value in the extra label and in trailing text

✅ **Do:** Let the extra label wrap when text is enlarged  
❌ **Don't:** Truncate it to keep the item on one line

---

## Description

**`False`** No supporting description is displayed.

**`True`** Supporting text is displayed below the primary Label.
Use a Description when users need additional context to understand the accordion topic or what information will be available after expansion.

⚠️ Keep the Description concise. Detailed information should normally be placed inside the Expanded content rather than duplicated in the trigger.

---

## description_do_&_dont 👈🤔

✅ **Do:** Add a description when users need context to understand or choose the section  
❌ **Don't:** Repeat the label in other words

✅ **Do:** Keep descriptions brief, one or two lines where possible  
❌ **Don't:** Write long paragraphs inside accordion items

✅ **Do:** Use Top alignment when a description is shown  
❌ **Don't:** Keep Center alignment on items with a description

✅ **Do:** Keep the description inside the same accordion trigger  
❌ **Don't:** Add an inline link inside the trigger description

✅ **Do:** Let descriptions wrap rather than truncate essential information  
❌ **Don't:** Cut descriptions that users need in order to decide

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important part of the information. It must never compensate for unclear writing.

**Strong text**
• Strong text can be used sparingly in the Description or Expanded text to highlight key information, such as a status, date, amount or required step. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**⚠️ Underline text and Hyperlinks**
• Underlined text must not be applied manually in the Description as users commonly interpret underlined content as a hyperlink.

---

## rich_text_do_&_dont 👈🤔

✅ **Do:** Use one short Strong fragment to highlight key information, such as a status, date or amount  
❌ **Don't:** Emphasise several fragments in the same text

✅ **Do:** Use only the Label/Medium/Strong token for emphasis  
❌ **Don't:** Use other text styles, italics or custom font weights

✅ **Do:** Make sure the message stays clear without the emphasis  
❌ **Don't:** Use bold to compensate for unclear writing

✅ **Do:** Keep essential information in the Label, Description or Expanded text  
❌ **Don't:** Underline text manually; users read it as a link

✅ **Do:** Keep the trigger as the only control  
❌ **Don't:** Place an inline Link component inside the trigger

---

## Technical layout adjustments

Even though the component structure is unique in Figma for easier use by designers, its technical implementation may differ between Web and native environments to respect the layout conventions of each platform.
The trigger and its Expanded content must nevertheless remain visually aligned and clearly perceived as parts of the same accordion section.

**Web (mobile, tablet, and desktop)**
The component is contained within the browser layout and respects its safety margins.
It therefore does not extend into the area reserved for the margin grid.
The component uses internal padding-inline, and its position follows the column structure defined by the surrounding container.
When expanded, the revealed content follows the same horizontal alignment as its associated trigger.

**Native app (Android, iOS, Flutter)**
The component may use the complete screen display area according to the native edge-to-edge layout.
Its internal padding-inline is therefore replaced by the corresponding grid-margin tokens.
The trigger and Expanded content must follow the same grid alignment so that the relationship between them remains visually clear.

---

## technical_layout_adjustments_do_&_dont 👈🤔

✅ **Do:** Contain the item within the grid columns on the web, respecting the safety margins  
❌ **Don't:** Stretch web accordion items into the margin area

✅ **Do:** Display the item edge to edge in native apps  
❌ **Don't:** Add web-style outer margins around native accordion items

✅ **Do:** Replace the internal padding-inline with the grid-margin tokens in native apps  
❌ **Don't:** Hard-code horizontal padding values per screen

✅ **Do:** Keep one component in Figma and adapt it per platform in code  
❌ **Don't:** Create separate design components for web and native

✅ **Do:** Keep the interactive area covering the full visible trigger on every platform  
❌ **Don't:** Reduce the interactive area when switching to edge to edge

---

## Multiline and responsiveness

**Multiline**
The Accordion card item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Trailing text and other supported text content must wrap when there is not enough horizontal space.
The trigger expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the accordion section.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the card contains a Description or Bottom slot. The Expanding indicator must remain visible and must not overlap, truncate or become visually disconnected from the trigger content.
⚠️ Keep the primary Label concise. Multiline content is supported, but excessively long Labels make accordion card collections more difficult to scan.

**Max-width vs full-width**
The Accordion card item does not have a default maximum width. Its width is defined by its parent container or accordion layout.
The trigger's interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or Expanding indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability.
The Background, Divider, Hover, Pressed and Focus treatments must continue to respect the complete accordion trigger.

The Expanding indicator remains positioned according to the Reverse property:
• At the logical end when Reverse is False.
• At the logical start when Reverse is True.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

⚠️ Do not apply a text maximum width that creates a large visual gap between the Label, related Trailing content and Expanding indicator. The relationship between all parts of the trigger must remain clear.

**User zoom in/out**
The Accordion card item must remain readable, operable and complete when users zoom the interface or increase the text size.

The component must adapt without clipping, overlapping or hiding meaningful information.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the main text area and simplify non-essential content when space is limited.

• Text must resize with the user's browser or system settings. Text resizing must not be blocked.
• The Label, Extra label, Description, Trailing text, Badge, Tag and Expanded text must wrap when required.
• The trigger must expand vertically according to its content. Do not use a fixed height.
• The complete visible trigger must remain one interactive target.
• The Expanding indicator must remain visible and must not overlap the text or move onto a separate unrelated line.
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.
• Optional decorative content may be simplified on narrow layouts, but meaningful statuses and supporting information must remain available.
• Do not truncate essential Labels, statuses, prices, dates or values to preserve the original desktop layout.
• Hover, Focus and Pressed treatments must adapt to the increased trigger dimensions and continue to cover the complete interactive area.
• The Expanding indicator must remain at the logical start or end according to the Reverse property after responsive reflow.
• When expanded, the revealed content must reflow independently without changing the relationship between the trigger and its content.
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the trigger on one line.

---

## multiline_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Let labels and supporting text wrap, and the trigger grow in height  
❌ **Don't:** Truncate information users need to understand the section

✅ **Do:** Use Top alignment when the label wraps or the item contains several text levels  
❌ **Don't:** Keep Center alignment on a tall, multiline trigger

✅ **Do:** Keep the whole visible width of the trigger interactive  
❌ **Don't:** Limit the clickable area to the label or the indicator

✅ **Do:** Simplify optional elements when space is limited, giving priority to the main text  
❌ **Don't:** Combine so many optional elements that the label wraps excessively

✅ **Do:** Check the item at 200% text size and at a 320 px wide viewport  
❌ **Don't:** Assume a trigger that fits at the default size fits at every zoom level

---

## Animation

When enabled, the accordion uses a smooth expansion animation (entry and exit) rather than appearing with an immediate cut.
The accordion content expands from its collapsed state when opened, providing a clear visual transition that helps users understand the relationship between the trigger and the revealed content and establishes a stronger sense of spatial continuity.

---

## animation_do_&_dont 👈🤔

✅ **Do:** Use a short, smooth expansion so users see where the content comes from  
❌ **Don't:** Reveal content with a long or elaborate animation

✅ **Do:** Animate both the opening and the closing in the same way  
❌ **Don't:** Animate the opening but cut the closing abruptly

✅ **Do:** Remove or replace the animation when users prefer reduced motion  
❌ **Don't:** Play the animation regardless of the reduced-motion preference

✅ **Do:** Keep the trigger in place while the content expands below it  
❌ **Don't:** Let the page jump so users lose the trigger they just activated

✅ **Do:** Keep the interaction available during the animation  
❌ **Don't:** Block input until the animation has finished

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

Concrete application to the Accordion:

**Pause, Stop, Hide**
The expansion and collapse of an accordion are triggered by the user and do not generally fall within the scope of this criterion.
However, if the expanded content contains moving, blinking, scrolling, or automatically updating content, that content must be evaluated separately.

**Reduced Motion**
The animated expansion and collapse of an accordion are not essential to its functionality or to understanding its content.
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.
Default: animated expansion and collapse
Reduced Motion: instantaneous expansion and collapse

Concrete application to the illustrations or animated images (leading or trailing container):

**Pause, Stop, Hide**
For an animation that starts automatically and lasts more than 5 seconds, users must be able to pause, stop, or hide the animation when it is presented alongside other content.
When the animation is short, lasting 5 seconds or less, no pause, stop, or hide control is required.

**Reduced Motion**
If Reduced Motion is enabled, any decorative or not essential animation that is not necessary to understand the content must be removed or replaced with a static representation.
If an animation conveys essential information, that same information must remain available through a non-animated alternative.

---

# Specs

## States

**`Enabled`** Enabled is the default state.
The accordion card can be expanded or collapsed. The complete trigger area acts as a single control for changing the Expanded state.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the accordion trigger. Apply the Hover treatment consistently to the trigger area. Hover must not move content, change the card dimensions or reveal information intended to appear only after expansion.

**`Focus`** Focus indicates that the accordion trigger is currently selected for keyboard interaction. Display one clear Focus treatment around the complete trigger area. When the card contains interactive elements inside its Expanded content, those elements receive their own Focus state independently from the accordion trigger.

**`Pressed`** Pressed is a temporary state displayed while the accordion trigger is being activated. Apply the Pressed treatment to the complete trigger area. Pressed must not resize the card or move surrounding content.

**`Disabled`** Use Disabled when the accordion section is temporarily unavailable or cannot currently be expanded. A Disabled trigger must not respond to activation.

**`Skeleton`** Use Skeleton while the card's trigger content is loading and the final information is not yet available. A Skeleton card acts as a placeholder and must not expand or collapse.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Accordion card item components must meet WCAG 2.2 Level AA standards so that all users can find the sections, know whether each one is open, and reach the revealed content using keyboard, pointer or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

An accordion hides content until users ask for it. Users who do not notice the control, or who cannot see the indicator change, may never find the content or may not know that it has appeared.

### Key Challenges

- The expanded or collapsed state is shown by an icon: it must also be exposed programmatically
- The whole trigger is one control: leading, trailing and slot content must not create extra, competing targets
- Collapsed content must be hidden from assistive technologies and from the focus order, not only visually
- Long labels, optional elements and zoom must not truncate the information users need to choose a section

### Critical Success Factors

1. Make each trigger a button inside a heading of the right level, with `aria-expanded` and `aria-controls` (WCAG 4.1.2)
2. Operate the trigger with Enter and Space, and keep Tab moving through triggers and visible content in page order
3. Keep collapsed content out of the accessibility tree and the tab sequence
4. Do not rely on the indicator or on colour alone to convey the state or the status of a section

---

## Design Requirements

### Structure & Labels

- [ ] **Trigger semantics**: A `button` in a heading element; the label, overline, extra label and description form its accessible name and description ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **State**: `aria-expanded` reflects the Expanded property; a Disabled item uses `aria-disabled` or the `disabled` attribute
- [ ] **Decorative visuals**: Decorative leading and trailing visuals are hidden from assistive technologies; informative ones have a text alternative

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border around the complete trigger ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Indicator contrast**: The Expanding indicator meets 3:1 against its background in every state
- [ ] **Target size**: The trigger is interactive across its full width and at least 24 × 24 CSS px

### Content

- [ ] **Descriptive labels**: ❌ "More" / ✅ "Delivery and returns" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Concise triggers**: Supporting text stays short so the announced button text remains easy to follow

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify each trigger announces its name, role and expanded or collapsed state, and that collapsed content is not read

### Keyboard Testing

- [ ] Tab reaches each trigger in order, Enter and Space toggle it, focus stays on the trigger after toggling
- [ ] Focus indicator visible (≥3:1 contrast) around the whole trigger; no focus lands inside collapsed content

### Functional Testing

- [ ] Verify the expansion animation is removed with Reduced Motion, and that nothing is truncated at 200% zoom and 320 px width

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **4.1.2 Name, Role, Value** (A): Triggers expose a name, the button role and the expanded state
- **2.1.1 Keyboard** (A): Every section can be opened and closed with the keyboard
- **1.3.1 Info and Relationships** (A): Triggers are headings, and each panel is associated with its trigger
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on the trigger
- **1.4.10 Reflow** (AA): Content wraps at 320 px without loss of information or two-dimensional scrolling

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Textual content](https://a11y-guidelines.orange.com/en/web/develop/textual-content/)
- [WAI-ARIA Authoring Practices - Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)
- [WCAG 2.2 Understanding - Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 28, 2026 | 1.0.0 | **Version 2.6 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
