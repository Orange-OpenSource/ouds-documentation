# Guideline

## Intro 👈🤖

A static list item is a read-only row that presents one piece of information in a list, with optional visuals, values and statuses.

---

## Definition

A static list item is a non-interactive horizontal row used to present a unit of information within a structured list.
It supports quick scanning and comparison between related items and may include supporting text, leading or trailing content, and status information. It does not navigate, trigger an action, or receive interactive states.

---

## Best for 👈🤔

✅ Account, contract or order summaries shown as label and value pairs

✅ Read-only details users scan and compare, such as plan features or options

✅ Lists of devices, lines or services with their current status

✅ Displaying a price, date, quantity or other value next to its label

✅ Items recognised faster with a visual cue: icon, image, avatar or flag

✅ Confirmation or review screens that recap information before a decision

✅ Showing progress or supporting metadata below an item with the Bottom slot

✅ Settings or profile information displayed without editing in place

✅ Help and information sections that list facts, conditions or included items

✅ Lists whose content loads progressively, using Skeleton placeholders

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The full-width row that holds one unit of information, with optional background and divider | N |
| 2 | Leading container | Icon, image, avatar, flag or slot that helps users recognise the item | Y |
| 3 | Text container | The label (Default, Bold or Slot) with optional overline, extra label and description | N |
| 4 | Trailing container | Secondary information such as text, badge, tag or a shared container type | Y |
| 5 | Helper text | Additional context needed to interpret the item, below the main content | Y |
| 6 | Bottom slot | Custom non-interactive content area below the main row | Y |

---

## Size

**`Default`** Use the Default size in most interfaces.
It provides sufficient spacing for standard lists, multiline content and visual elements such as avatars, images or badges.

**`Small`** Use the Small size in compact layouts where information density is important.
The Small size is best suited to:
• Short labels.
• Simple metadata.
• Compact desktop interfaces.

⚠️ Do not mix Default and Small items within the same continuous list unless they represent clearly different sections.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use the Default size for most lists, especially with multiline content or visuals  
❌ **Don't:** Switch to Small just to fit more rows when labels or visuals need room

✅ **Do:** Reserve Small for compact, information-dense layouts with short labels and simple metadata  
❌ **Don't:** Use Small for long descriptions or large avatars and images

✅ **Do:** Keep one size across a continuous list so the rows scan as a set  
❌ **Don't:** Mix Default and Small items in one list without a clear change of section

✅ **Do:** Let the tallest element (label, avatar, image) define the row height  
❌ **Don't:** Force a fixed height that clips multiline content

✅ **Do:** Check the Small size with real, translated content before adopting it  
❌ **Don't:** Assume short English labels stay short in every language

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

## alignment_do_&_dont 👈🤔

✅ **Do:** Use Center for single-line items whose elements have similar heights  
❌ **Don't:** Keep Center alignment when the label wraps onto several lines

✅ **Do:** Switch to Top alignment when a description, extra label or Bottom slot is shown  
❌ **Don't:** Leave leading visuals floating mid-height next to a tall block of text

✅ **Do:** Use the same alignment for all items of a list  
❌ **Don't:** Alternate Center and Top alignment from one item to the next

✅ **Do:** Align trailing values with the first line of text in Top alignment  
❌ **Don't:** Let a value drift away from the label it belongs to

✅ **Do:** Keep the programmatic reading order unchanged whatever the alignment  
❌ **Don't:** Reorder content in code to follow a visual alignment choice

---

## Choosing leading and trailing content

Leading and trailing content serve different purposes within the item.
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

## choosing_leading_and_trailing_content_do_&_dont 👈🤔

✅ **Do:** Choose each position from the content's role: recognition leading, supplementary information trailing  
❌ **Don't:** Pick a position only because there is space left

✅ **Do:** Use trailing content when users compare values across several items  
❌ **Don't:** Hide the value users compare inside each description

✅ **Do:** Keep the label the clearest element when both positions are used  
❌ **Don't:** Let leading and trailing content compete with the label

✅ **Do:** Use a different container type in each position  
❌ **Don't:** Repeat the same information in the leading and trailing areas

✅ **Do:** Keep leading content clearly non-interactive  
❌ **Don't:** Make a leading icon or avatar look like a button users can tap

---

## Leading

Leading content appears before the main label and supports recognition or identification.
Use it when the visual element helps users understand the content more quickly. Do not add leading content only to decorate the list. Only one leading container should be displayed per item.

**`False`** No leading content is displayed. The main content starts at the default horizontal padding.

**`True`** A leading container is displayed before the main content. Use the Leading container type property to define its content, such as an icon, image, avatar, flag, value or custom slot.

---

## leading_do_&_dont 👈🤔

✅ **Do:** Add leading content when a visual cue helps users recognise the item faster  
❌ **Don't:** Add decorative leading content that tells users nothing

✅ **Do:** Display one leading container per item  
❌ **Don't:** Stack several visuals in the leading area

✅ **Do:** Use leading content consistently for all items of a list  
❌ **Don't:** Show leading content on some items only

✅ **Do:** Provide a text alternative when the leading visual adds information not in the label  
❌ **Don't:** Repeat the label in the leading visual's text alternative

✅ **Do:** Keep leading content static, like the rest of the item  
❌ **Don't:** Make the leading element an independent action inside a static row

---

## Leading container type

**`Icon`** Use an icon to reinforce the meaning of the item or help users identify a familiar category, object or status.

**Size**
Controls the visual prominence of the icon.

⚠️ Use the same icon size for equivalent items within the same list. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use for standard and compact list items. This is the preferred size when the icon provides secondary visual support.

**`Large`** Use when the icon needs stronger prominence or when the item has a larger height, multiline content or additional supporting information.

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

⚠️ Use the same image size for equivalent items within the same list. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use in compact or information-dense lists where the image remains secondary to the text.

**`Large`** Use in standard content lists where visual identification is important.

**`Xlarge`** Use when the image is a significant part of the content, such as a product or media preview.

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

**`Medium`** Use in compact lists or when the avatar is secondary to the content.

**`Large`** Use in standard people or account lists.

**`Xlarge`** Use when identity is a primary part of the item or when additional avatar details must remain visible.

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

**⚠️ Interaction**
The Static list item is non-interactive. Custom Slot content must not contain:
• Buttons
• Links
• Checkboxes
• Radio buttons
• Toggles
• Menus
• Any independently focusable element

---

## leading_container_type_do_&_dont 👈🤔

✅ **Do:** Match the type to the content: icon for categories, image for products or media, avatar for people, flag for countries  
❌ **Don't:** Use images or avatars only to add visual variety

✅ **Do:** Keep one size per container type within a list  
❌ **Don't:** Mix icon, image or avatar sizes arbitrarily in the same list

✅ **Do:** Always pair avatars and flags with a visible name  
❌ **Don't:** Rely on an avatar, initials or a flag alone to identify the item

✅ **Do:** Use semantic statuses only when they carry that meaning, backed by text  
❌ **Don't:** Use functional colours for decoration or as the only status cue

✅ **Do:** Keep Slot for content the standard types cannot express, and keep it non-interactive  
❌ **Don't:** Put buttons, links, checkboxes or toggles inside a Slot

---

## Trailing

Trailing content appears after the main content and communicates secondary information. It can be used for a value, status, category or supplementary visual element.
The trailing content should remain concise and should not contain information that is more important than the primary label.

**`False`** No trailing content is displayed. The main content can use the available width of the item.

**`True`** A trailing container is displayed after the main content. Use the Trailing container type property to define its content, such as text, a badge, tag, icon, image, value or custom slot.

---

## trailing_do_&_dont 👈🤔

✅ **Do:** Use trailing content for a value, status or category related to the label  
❌ **Don't:** Put information more important than the label in the trailing area

✅ **Do:** Keep trailing content short so the label keeps most of the width  
❌ **Don't:** Let trailing content squeeze the label into excessive wrapping

✅ **Do:** Align trailing values so users can compare them down the list  
❌ **Don't:** Mix value formats (units, date styles) from one item to the next

✅ **Do:** Disable the trailing container when it adds no useful information  
❌ **Don't:** Fill the trailing area just to balance the row

✅ **Do:** Keep trailing content read-only  
❌ **Don't:** Place a button, link or chevron in the trailing area of a static item

---

## Trailing container type

**Shared container types**
The following types reuse the properties and guidance documented under Leading container type:
• Icon
• Image
• Avatar
• Flag
• Slot

⚠️ Their meaning and nested properties remain the same. Only their position within the item changes.
⚠️ Do not use the same container type in both the leading and trailing positions within the same item. If a type is used as leading content, choose a different trailing type or disable the trailing container.

**`Text`** Use Text to display a short value or secondary piece of information associated with the primary label.

⚠️ Keep trailing text concise. When the information requires a sentence or explanation, use the Description or Helper text property instead.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information that should remain clearly readable without drawing more attention than the primary label.

**`Label muted`** Use Label muted for low-priority metadata that supports the item but is not essential to its immediate understanding.

**`Label strong`** Use Label strong when the trailing value requires additional visual emphasis, for example when users need to compare values across a list.

**`Label + Extra label`** Use Label + Extra label when a value requires a short qualifier, unit or supporting label.

**`Badge`** Use a Badge to communicate a compact status or notification associated with the item. A badge should contain secondary information and must not replace the primary label or description.

**Type**

**`Badge`** Use Badge for a short textual status. Keep the label concise and use terminology consistently throughout the product.

**`Badge count`** Use Badge count to display a short numerical quantity, such as unread items, notifications or occurrences.
The count must have a clear relationship with the primary item. Users should not need to guess what is being counted.

**Status**
The Status property defines the semantic colour and meaning of the badge.

⚠️ Colour must not be the only way the meaning is communicated. Provide an equivalent accessible description.

**`Not functional`**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Use to highlight branded, selected or noteworthy information that does not correspond to another semantic status. Do not use Accent solely to make an item more visually prominent.

**`Functional`**

**`Positive`** Use for successful, active, available or completed states.

**`Info`** Use for additional neutral information that may require attention but does not indicate success or risk.

**`Warning`** Use for states that require caution, awareness or future action.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

**Badge size**

**`XSmall`** Use for very compact badge with small list items or dense layouts.

**`Small`** Use for standard compact notification badge.

**`Medium`** Use when the badge requires stronger visibility or accompanies a larger item.

**`Large`** Use only in spacious layouts where the badge is a significant secondary element.

**Badge count size**

**`Medium`** Use Medium for standard or compact list items.

**`Large`** Use Large when the list item uses larger dimensions or when a larger badge is required to remain visually balanced with the surrounding content.

**State**

**`Enabled`** Use when the badge communicates a current and applicable status or count.

**`Disabled`** Use when the status represented by the badge is inactive, unavailable or no longer applicable.

Because the Static list item is non-interactive, Disabled does not mean that the badge cannot be clicked. It communicates the state of the represented information.
Do not use Disabled merely to reduce visual emphasis.

**`Tag`** Use a Tag to communicate a category, attribute, classification or compact status associated with the item. In a Static list item, a tag is informational.

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

**`Small`** Use Small as the standard and recommended tag size within the list item. It keeps the tag visually secondary, preserves space for the main content and works well in compact or information-dense lists.

**`Default`** Use Default when the list item uses a larger layout or when the tag must align with other Default-size tags in the same interface.

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

## trailing_container_type_do_&_dont 👈🤔

✅ **Do:** Keep trailing text to one or two words, such as a value or a short status  
❌ **Don't:** Write sentences in trailing text; use Description or Helper text instead

✅ **Do:** Give badge counts a clear meaning, for example “2 connected devices”  
❌ **Don't:** Show an isolated number whose meaning users must guess

✅ **Do:** Use tags for categories or compact statuses, in the Small size by default  
❌ **Don't:** Make a tag or badge interactive inside the item

✅ **Do:** Use a container type different from the leading one  
❌ **Don't:** Use the same container type in both positions

✅ **Do:** Pair functional statuses with their predefined icons and explicit text  
❌ **Don't:** Signal a status with colour alone

---

## Divider

**`False`** No divider is displayed. Use this option when items are already separated by spacing, individual backgrounds or another clear grouping method.

**`True`** A divider is displayed between list items. Use it when several items share the same surface and additional visual separation improves scanning.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use dividers when several items share the same surface and need extra separation  
❌ **Don't:** Add dividers when items are already separated by spacing or backgrounds

✅ **Do:** Apply dividers consistently within a list  
❌ **Don't:** Divide only some of the adjacent items of the same list

✅ **Do:** Avoid a divider that doubles the edge of the surrounding container  
❌ **Don't:** Stack a divider against a container border

✅ **Do:** Use section headings or spacing to show groups of different meaning  
❌ **Don't:** Rely on dividers alone to communicate grouping

✅ **Do:** Keep the divider decorative and hidden from assistive technologies  
❌ **Don't:** Use a divider to suggest that rows can be selected or opened

---

## Helper text

**`False`** No helper text is displayed.

**`True`** Helper text is displayed below the primary content. Use helper text for additional information required to interpret the item correctly.

---

## helper_text_do_&_dont 👈🤔

✅ **Do:** Use helper text for information needed to interpret the item correctly  
❌ **Don't:** Repeat the label or the description in the helper text

✅ **Do:** Keep helper text short and specific  
❌ **Don't:** Write long paragraphs that push the next items far down

✅ **Do:** Use Top alignment when helper text is displayed  
❌ **Don't:** Keep Center alignment on an item that shows helper text

✅ **Do:** Explain why information is unavailable when an item is disabled  
❌ **Don't:** Show a disabled item with no explanation when the reason matters

✅ **Do:** Keep helper text plain, read-only text  
❌ **Don't:** Put a link or an action in the helper text

---

## Background

**`False`** The item uses the surrounding container surface without an individual background. Use this option for standard continuous lists.

**`True`** A background is applied to the item. Use it when the item needs visual separation from its surrounding context or when it belongs to a distinct read-only content area.

---

## background_do_&_dont 👈🤔

✅ **Do:** Use no background for standard continuous lists  
❌ **Don't:** Add a background to every item of a long list by default

✅ **Do:** Add a background when the item belongs to a distinct read-only content area  
❌ **Don't:** Use a background to signal selection, status or urgency

✅ **Do:** Apply the background consistently to items that play the same role  
❌ **Don't:** Mix items with and without a background in the same group without a reason

✅ **Do:** Keep text and icons at the required contrast on the background  
❌ **Don't:** Choose a background that lowers the contrast of labels or statuses

✅ **Do:** Keep backgrounds calm so the static item does not look like a button  
❌ **Don't:** Use a background that makes a static row look clickable

---

## Label type

**`Default`** Use Default for most list items. It provides the standard visual hierarchy and should be the preferred option for common labels, names and titles.

**`Bold`** Use Bold when the primary label requires stronger emphasis.

Suitable for:
• Important item names.
• Lists where labels must be scanned quickly.

**`Slot`** Use Slot when the standard label cannot support the required content structure.

The Slot may be used for custom primary content such as:
• A product-specific text arrangement.
• A combination of text elements not supported by the standard properties.

---

## label_type_do_&_dont 👈🤔

✅ **Do:** Use the Default label type for most items  
❌ **Don't:** Make every label bold; emphasis then loses its meaning

✅ **Do:** Use Bold when labels must be scanned quickly or item names are important  
❌ **Don't:** Mix Default and Bold labels in one list without a reason

✅ **Do:** Write specific, familiar labels that name the information shown  
❌ **Don't:** Use vague labels such as “Info” or “Details”

✅ **Do:** Use the label Slot only when standard properties cannot express the content  
❌ **Don't:** Put links, buttons or controls in the label Slot

✅ **Do:** Keep labels parallel in structure across the list  
❌ **Don't:** End short labels with a period when they are not sentences

---

## Overline

**`False`** No overline is displayed.

**`True`** A short contextual label is displayed above the primary label. Use an overline to communicate a short contextual qualifier.

---

## overline_do_&_dont 👈🤔

✅ **Do:** Use an overline for a short contextual qualifier, such as a category or section  
❌ **Don't:** Use the overline for the item name

✅ **Do:** Keep overlines to a few words  
❌ **Don't:** Write sentences in the overline

✅ **Do:** Use overlines consistently for items of the same kind  
❌ **Don't:** Show overlines on random items only

✅ **Do:** Keep the overline before the label in the reading order  
❌ **Don't:** Hide information users need to identify the item in the overline only

✅ **Do:** Use Top alignment when the overline makes the text block taller  
❌ **Don't:** Rely on the overline's style alone to convey meaning

---

## Extra label

**`False`** No extra label is displayed.

**`True`** An additional short label is displayed with the primary label.

Use an extra label for:
• A secondary name.
• A short complementary value.
• A short piece of information directly related to the label.

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

**`True`** Supporting text is displayed below the primary label. Use a description when users need additional context to understand the item.

---

## description_do_&_dont 👈🤔

✅ **Do:** Add a description when users need context to understand the item  
❌ **Don't:** Repeat the label in other words

✅ **Do:** Keep descriptions brief, one or two lines where possible  
❌ **Don't:** Write long paragraphs inside list items

✅ **Do:** Use Top alignment when a description is shown  
❌ **Don't:** Keep Center alignment on items with a description

✅ **Do:** Keep the description plain text  
❌ **Don't:** Add an inline link inside the description

✅ **Do:** Let descriptions wrap rather than truncate essential information  
❌ **Don't:** Cut descriptions that users need to understand the item

---

## Slot (bottom)

The bottom slot adds a custom content area below the main row content. Use it when the information cannot be clearly represented by the standard Description or Helper text properties.

**`False`** No additional content is displayed below the main content.

**`True`** A custom content area is displayed below the main content.

It may contain:
• A progress indicator.
• A compact group of metadata.
• A visual preview or status summary.
• Product-specific supporting content.

---

## slot_bottom_do_&_dont 👈🤔

✅ **Do:** Use the Bottom slot for non-interactive supporting content: progress, metadata, preview  
❌ **Don't:** Put buttons, links or controls in the Bottom slot

✅ **Do:** Use it only when Description or Helper text cannot express the content  
❌ **Don't:** Use it as the default place for supporting text

✅ **Do:** Keep Bottom slot content visually secondary to the label  
❌ **Don't:** Let the slot content dominate the item

✅ **Do:** Give meaningful slot content, such as progress, a text equivalent  
❌ **Don't:** Rely on a visual-only indicator in the slot

✅ **Do:** Use Top alignment when the Bottom slot is enabled  
❌ **Don't:** Keep Center alignment on items that use the Bottom slot

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important part of the message. It must never compensate for unclear writing.

**Strong text**
• Strong text can be used sparingly in the helper text or description to highlight key information, such as a status, date, amount, or required step. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**⚠️ Underline text and Hyperlinks**
• Underlined text must not be applied manually in the Description or Helper text, as users commonly interpret underlined content as a hyperlink.

---

## rich_text_do_&_dont 👈🤔

✅ **Do:** Use one short Strong fragment to highlight key information, such as a status, date or amount  
❌ **Don't:** Emphasise several fragments in the same text

✅ **Do:** Use only the Label/Medium/Strong token for emphasis  
❌ **Don't:** Use other text styles, italics or custom font weights

✅ **Do:** Make sure the message stays clear without the emphasis  
❌ **Don't:** Use bold to compensate for unclear writing

✅ **Do:** Keep essential information in the Label, Description or Helper text  
❌ **Don't:** Underline text manually; users read it as a link

✅ **Do:** Keep the item free of links and actions  
❌ **Don't:** Add an inline link to turn a static item into a navigation entry

---

## Multiline and responsiveness

**Multiline**
The  list item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.
The item expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the item contains a Description, Helper text or Bottom slot. The navigation indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.
⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make navigation lists more difficult to scan.

**Max-width vs full-width**
The list item does not have a default maximum width. Its width is defined by its parent container or navigation layout.
The item’s interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or navigation indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability. The item’s background, divider, hover, pressed and focus treatments must still cover the complete navigation target.

The navigation indicator remains positioned at the logical edge of the item:
• At the logical end for the Next layout.
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

• ⚠️ Do not apply a text maximum width that creates a large visual gap between the Label and related Trailing content. The relationship between all parts of the item must remain clear.

**User zoom in/out**
The Navigation list item must remain readable, operable and complete when users zoom the interface or increase the text size.
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

## multiline_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Let labels, descriptions and helper text wrap onto several lines  
❌ **Don't:** Truncate information users need to understand the item

✅ **Do:** Let the item grow vertically with its content  
❌ **Don't:** Set a fixed height on list items

✅ **Do:** Switch to Top alignment when text becomes multiline  
❌ **Don't:** Keep Center alignment with multiline labels

✅ **Do:** Remove optional decorative content first on narrow layouts  
❌ **Don't:** Hide the description, values or statuses to keep the item on one line

✅ **Do:** Test at 200% text size, 320 px width and with longer translations  
❌ **Don't:** Validate the layout only with short English labels on desktop

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

## technical_layout_adjustments_do_&_dont 👈🤔

✅ **Do:** Contain the item within the grid columns on the web, respecting the safety margins  
❌ **Don't:** Stretch web list items into the margin area

✅ **Do:** Display the item edge to edge in native apps  
❌ **Don't:** Add web-style outer margins around native list items

✅ **Do:** Replace the internal padding-inline with the grid-margin tokens in native apps  
❌ **Don't:** Hard-code horizontal padding values per screen

✅ **Do:** Keep one component in Figma and adapt it per platform in code  
❌ **Don't:** Create separate design components for web and native

✅ **Do:** Keep text aligned with the grid on every platform  
❌ **Don't:** Let content drift from the grid when switching to edge to edge

---

# Specs

## States

**`Enabled`** Enabled is the default state. All content is displayed using its standard visual tokens. Because the item is static, the Enabled state does not introduce hover, pressed or focus behaviour.

**`Disabled`** Use Disabled when the information represented by the item is currently unavailable or inactive.
Since the row is not interactive, the Disabled state should communicate content availability rather than button availability.

**`Skeleton`** Use Skeleton while the item content is loading and its final value is not yet available.

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

Concrete application to the List item → Illustrations or animated images (leading or trailing container):

**Pause, Stop, Hide**
For an animation that starts automatically and lasts more than 5 seconds, users must be able to pause, stop, or hide the animation when it is presented alongside other content.
When the animation is short, lasting 5 seconds or less, no pause, stop, or hide control is required.

**Reduced Motion**
If Reduced Motion is enabled, any decorative or not essential animation that is not necessary to understand the content must be removed or replaced with a static representation.
If an animation conveys essential information, that same information must remain available through a non-animated alternative.

## Accessibility

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

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 3, 2026 | 1.2.0 | <ul><li>Removal of the “Video” variant in leading and trailing positions.<li>For the nested “Image” component, addition of a new boolean variant, “Animated=True/False”, allowing the use of animated images in GIF or WEBP formats.</ul>**Bug fix**<ul><li>The “Icon”, “Image”, and “Avatar” assets in the trailing position of the “Size: Small” / “Alignment: Top alignment” variants no longer offer “Medium/Large” sizes.<li>Updated size tokens applied to “Icon” assets:<ul><li>Size “Small”: size/icon/with-label/large/size-small<li>Size “Medium”: size/icon/with-label/large/size-medium<li>Size “Large”: size/icon/with-label/large/size-xlarge</ul><li>Flag sizes have been updated for the “Small” and “Default” variants:<ul><li>Removal of the height token: list-item/size/flag/height<li>To replace it with the width tokens:<ul><li>Size “Small”: ouds/control/list-item/size/asset/small<li>Size “Medium”: ouds/control/list-item/size/asset/medium</ul></ul></ul> | Maxime Tonnerre |
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 31, 2026 | 1.1.0 | **Version 2.7 of the design tokens is required for the development of this update.**<br>The semantic tokens applied to the text within the nested elements “.Text container” and “.Text container / Top alignment” for the “Default” size variants:<ul><li>ouds/size/max-width/label-medium (used for the “Label”, “Extra label”, and “Description” text)<li>ouds/size/max-width/label-small (used for the “Overline” text)</ul>Are replaced with the following semantic token:<ul><li>ouds/size/max-width/boxed-text</ul> | Maxime Tonnerre |
| Jun 5, 2026 | 1.0.0 | **Version 2.4 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
