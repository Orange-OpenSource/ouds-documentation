# Guideline

## Intro 👈🤖

A navigation list item is a clickable row that leads users to another page or view, with optional visuals and supporting details.

---

## Definition

A navigation list item is an interactive horizontal row that takes users to another internal or external destination when activated.
It is intended for structured lists where users need to scan and access related destinations quickly. The entire item acts as a single navigation target and supports the required hover, pressed and keyboard focus states.

---

## Best for 👈🤔

✅ Settings, account or profile menus that lead to dedicated sub-pages

✅ Drilling down through a hierarchy, from a category to its sub-categories and details

✅ Lists of related destinations that users need to scan and compare quickly

✅ Mobile menus where the whole row must be one easy-to-reach tap target

✅ Destinations recognised faster with a visual cue: icon, image, avatar or flag

✅ Showing a status, count or value for each destination before users open it

✅ Returning to a parent level or an earlier step with the Previous layout

✅ Linking to another product or service, made explicit with the External indicator

✅ Help, support or legal sections that group many links to dedicated pages

✅ Lists of destinations that load progressively, using Skeleton placeholders

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The full-width row that forms one navigation target, with optional background and divider | N |
| 2 | Leading container | Icon, image, avatar, flag or slot that helps users recognise the destination | Y |
| 3 | Text container | The label (Default, Bold or Slot) with optional overline, extra label and description | N |
| 4 | Trailing container | Secondary information such as text, badge, tag or a shared container type | Y |
| 5 | Navigation indicator | Internal or External indicator, at the end (Next) or start (Previous) of the item | N |
| 6 | Helper text | Additional context users need before navigating, below the main content | Y |
| 7 | Bottom slot | Custom non-interactive content area below the main row | Y |

---

## Size

**`Default`** Use the Default size in most interfaces.
It provides sufficient spacing for standard navigation lists, multiline destination labels and visual elements such as avatars, images or badges.

**`Small`** Use the Small size in compact navigation layouts where information density is important.

The Small size is best suited to:
• Short destination labels.
• Simple supporting metadata.
• Compact desktop navigation lists.

⚠️ Do not mix Default and Small items within the same continuous navigation list unless they represent clearly different sections or levels of hierarchy.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use the Default size for most navigation lists, especially with multiline labels or visuals  
❌ **Don't:** Switch to Small just to fit more rows when labels or visuals need room

✅ **Do:** Reserve Small for compact, information-dense layouts with short labels  
❌ **Don't:** Use Small in touch-first lists where rows become harder to tap

✅ **Do:** Keep one size across a continuous list so the rows scan as a set  
❌ **Don't:** Mix Default and Small items in one list without a clear change of section or hierarchy

✅ **Do:** Let the tallest element (label, avatar, image) define the row height  
❌ **Don't:** Force a fixed height that clips multiline content

✅ **Do:** Check the Small size with real, translated labels before adopting it  
❌ **Don't:** Assume short English labels stay short in every language

---

## Alignment

**`Center`** Center alignment is the default for items containing:
• A single-line label.
• Short supporting content.
• Leading and trailing elements with similar dimensions.

⚠️ Do not use Center alignment when it makes an icon, avatar, value or navigation indicator appear visually disconnected from the first line of content.

**`Top`** Use Top alignment when:
• The label wraps onto multiple lines.
• A description or extra label is displayed.
• The Bottom slot is enabled.
• Leading or trailing content must remain aligned with the beginning of the text.
• The different content areas have noticeably different heights.

⚠️ Top alignment must not change the navigation behaviour or the programmatic reading order of the item.

---

## alignment_do_&_dont 👈🤔

✅ **Do:** Use Center for single-line items whose elements have similar heights  
❌ **Don't:** Keep Center alignment when the label wraps onto several lines

✅ **Do:** Switch to Top alignment when a description, extra label or Bottom slot is shown  
❌ **Don't:** Leave leading visuals floating mid-height next to a tall block of text

✅ **Do:** Use the same alignment for all items of a list  
❌ **Don't:** Alternate Center and Top alignment from one item to the next

✅ **Do:** Align leading and trailing content with the first line of text in Top alignment  
❌ **Don't:** Let the navigation indicator drift away from the label it belongs to

✅ **Do:** Keep the programmatic reading order unchanged whatever the alignment  
❌ **Don't:** Reorder content in code to follow a visual alignment choice

---

## Layout

**`Next`** Use Next when the destination moves users forward, deeper into the information hierarchy or to a related destination. The navigation indicator is positioned at the logical end of the item.

**`Previous`** Use Previous when the destination returns users to a parent destination, an earlier level or a preceding step in a navigation flow.
The navigation indicator is positioned at the logical start of the item.

⚠️ Leading content is not supported in the Previous layout because the navigation indicator occupies the leading area. Only Trailing content can be added to provide secondary information.

---

## layout_do_&_dont 👈🤔

✅ **Do:** Use Next for forward, deeper or related destinations  
❌ **Don't:** Use Next for an item that actually returns to a parent level

✅ **Do:** Use Previous only to return to a parent destination, an earlier level or a preceding step  
❌ **Don't:** Use Previous as a decorative mirrored version of the item

✅ **Do:** Name the target in a Previous item, for example the parent page  
❌ **Don't:** Label a Previous item only “Back” when the parent level is not obvious

✅ **Do:** Add trailing content when a Previous item needs secondary information  
❌ **Don't:** Add leading content to a Previous item; the indicator already occupies that area

✅ **Do:** Keep the indicator at the logical start or end, including in right-to-left languages  
❌ **Don't:** Hard-code the indicator direction so it breaks in right-to-left layouts

---

## Navigation indicator type

**`Internal`** Use Internal when the item navigates to another destination within the same product, service or application. The internal navigation indicator reinforces that the complete item opens another view or level.

**`External`** Use External when the item navigates outside the current product, service or application. The external navigation indicator informs users that the destination belongs to another context.

⚠️ When opening the destination in a new browser tab or window would be unexpected, communicate this through visible supporting text or the link’s accessible description.

---

## navigation_indicator_type_do_&_dont 👈🤔

✅ **Do:** Use Internal for destinations within the same product, service or app  
❌ **Don't:** Use External just to make an item stand out

✅ **Do:** Use External when the destination leaves the current product, service or app  
❌ **Don't:** Rely on the External indicator alone to tell users they are leaving

✅ **Do:** Say when a destination opens in a new tab or window, in visible text or the accessible description  
❌ **Don't:** Assume that External always means a new tab

✅ **Do:** Use the same indicator type for equivalent destinations across the product  
❌ **Don't:** Change the indicator type for the same destination from one screen to another

✅ **Do:** Hide the indicator from assistive technologies once the link is correctly named  
❌ **Don't:** Let screen readers announce the chevron as a separate element

---

## Choosing leading and trailing content

Leading and trailing content serve different purposes within the navigation item.
• Leading content supports recognition and identification before users read the destination label.
• Trailing content provides supplementary information related to the destination after the main content has been understood.
The navigation indicator is separate from both areas and communicates the navigation behaviour of the complete item.
Choose each position according to the role of the content, not only according to the available space.

**Use leading content only**
Use leading content when the visual element helps users identify or understand the destination before reading its text.

Leading-only layouts are recommended when:
• Visual recognition is important.
• The destination does not require a secondary value or status.
• The main label needs most of the available horizontal space.
• The interface is displayed on a narrow mobile viewport.

⚠️ Leading content must not appear to be an independent action.

**Use trailing content only**
Use trailing content when the primary label is sufficient for identification and users mainly need to scan or compare secondary information.

Trailing-only layouts are recommended when:
• Users compare values or statuses across several destinations.
• Visual identification is not required.
• The secondary information is closely associated with the destination.
• Preserving a clean and compact layout is more important than adding imagery.

**Use leading and trailing content together**
Use both positions when they communicate different and complementary information.

When both positions are enabled:
• The leading element should support destination recognition.
• The trailing element should provide secondary information.
• The main label must remain the clearest and most important element.
• Both elements must remain understandable without relying on colour alone.
• Neither element may behave as an independent control.
• Avoid using the same container type in both positions.
• Avoid repeating the same information visually and textually.
• Do not use both positions only to create visual balance.
• Preserve sufficient space for the label and navigation indicator.

---

## choosing_leading_and_trailing_content_do_&_dont 👈🤔

✅ **Do:** Choose each position from the content's role: recognition leading, supplementary information trailing  
❌ **Don't:** Pick a position only because there is space left

✅ **Do:** Use leading visuals for all items of a list or for none of them  
❌ **Don't:** Mix items with and without leading visuals in the same list

✅ **Do:** Keep the label the clearest element when both positions are used  
❌ **Don't:** Let leading and trailing content compete with the label

✅ **Do:** Use a different container type in each position  
❌ **Don't:** Repeat the same information in the leading and trailing areas

✅ **Do:** Prefer leading-only layouts on narrow mobile viewports  
❌ **Don't:** Enable both positions only to balance the layout

---

## Leading

Leading content appears before the main label and supports recognition or identification of the destination.
Use it when the visual element helps users understand the destination more quickly.
Leading content is included within the complete navigation target and must not behave as an independent action.

**`False`** No leading content is displayed. The main content starts at the default horizontal padding.

**`True`** A leading container is displayed before the main content.
Use the Leading container type property to define its content, such as an icon, image, avatar, flag thumbnail or custom slot.

---

## leading_do_&_dont 👈🤔

✅ **Do:** Add leading content when a visual cue helps users recognise the destination faster  
❌ **Don't:** Add decorative leading content that tells users nothing

✅ **Do:** Keep leading content inside the single navigation target  
❌ **Don't:** Turn the leading element into an independent action, such as a separate tappable icon

✅ **Do:** Use leading content consistently for all items of a list  
❌ **Don't:** Show leading content on some items only

✅ **Do:** Provide a text alternative when the leading visual adds information not in the label  
❌ **Don't:** Repeat the label in the leading visual's text alternative

✅ **Do:** Use the Next layout when an item needs leading content  
❌ **Don't:** Add leading content to a Previous item, which does not support it

---

## Leading container type

**`Icon`** Use an icon to reinforce the meaning of the destination or help users identify a familiar category, object or service.

⚠️ Do not use an action icon that suggests a separate operation inside the navigation item.

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
Display a badge when a notification or secondary status must be associated with the destination represented by the icon.

**`False`** Display the icon without a badge.

**`True`** Display a badge when a notification must be associated with the icon.

**`Image`** Use an image when visual identification of the destination is important, for example for a product, service, article or media page.
Do not use an image when it does not add useful information or when it could be mistaken for a separate interactive preview.

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

**`Avatar`** Use an avatar when the destination represents a person, profile, team, organisation or account.
The avatar supports visual recognition but must always be accompanied by a visible text label identifying the destination.

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

**`Slot`** Use Slot for custom leading content that cannot be represented by Icon, Image, Avatar or Flag. Slot provides flexibility for specific product requirements, but it should be used as an exception rather than the default solution.

⚠️ Interaction
The Navigation list item already acts as one complete interactive link.

Custom Slot content must not contain:
• Buttons.
• Links.
• Checkboxes.
• Radio buttons.
• Toggles.
• Menus.
• Playback controls.
• Any independently focusable element.

Nested interactive elements create conflicting activation and focus behaviour. When an independent action is required, place it outside the Navigation list item or use another component designed for multiple actions.

---

## leading_container_type_do_&_dont 👈🤔

✅ **Do:** Match the type to the destination: icon for categories, image for products or media, avatar for people, flag for countries  
❌ **Don't:** Use images or avatars only to add visual variety

✅ **Do:** Keep one size per container type within a list  
❌ **Don't:** Mix icon, image or avatar sizes arbitrarily in the same list

✅ **Do:** Always pair avatars and flags with a visible name  
❌ **Don't:** Rely on an avatar, initials or a flag alone to identify the destination

✅ **Do:** Use semantic statuses only when they carry that meaning, backed by text  
❌ **Don't:** Use functional colours for decoration or as the only status cue

✅ **Do:** Keep Slot for content the standard types cannot express, and keep it non-interactive  
❌ **Don't:** Put buttons, links or controls inside a Slot

---

## Trailing

Trailing content appears after the main content and communicates secondary information related to the destination.
Content remains part of the complete navigation target and must not behave as an independent action.

**`False`** No trailing content is displayed. The main content can use the available width of the item before the Navigation indicator.

**`True`** A trailing container is displayed after the main content and before the Navigation indicator.
Use the Trailing container type property to define its content, such as text, a badge, tag, icon, image, value or custom slot.

---

## trailing_do_&_dont 👈🤔

✅ **Do:** Use trailing content for secondary information users compare across destinations  
❌ **Don't:** Put information users need to identify the destination only in the trailing area

✅ **Do:** Keep trailing content short so the label keeps most of the width  
❌ **Don't:** Let trailing content squeeze the label into excessive wrapping

✅ **Do:** Keep trailing content inside the single navigation target  
❌ **Don't:** Add a separate action next to the navigation indicator

✅ **Do:** Place trailing content before the navigation indicator, as designed  
❌ **Don't:** Replace the navigation indicator with trailing content

✅ **Do:** Disable the trailing container when it adds no useful information  
❌ **Don't:** Fill the trailing area just to balance the row

---

## Trailing container type

**Shared container types**
The following types reuse the properties and guidance documented under Leading container type:
• Icon
• Image
• Avatar
• Flag
• Slot

Their meaning and nested properties remain the same. Only their position within the item changes.

⚠️ All trailing content remains part of the same navigation target and must not receive independent focus or activation.
⚠️ Do not use the same container type in both the leading and trailing positions within the same item. If a type is used as leading content, choose a different trailing type or disable the trailing container.

**`Text`** Use Text to display a short value or secondary piece of information associated with the navigation destination.

⚠️ Keep trailing text concise. When the information requires a sentence or explanation, use the Description or Helper text property instead.
⚠️ Trailing text is not a separate link label and must not suggest a different destination.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information that should remain clearly readable without drawing more attention than the primary label.

**`Label muted`** Use Label muted for low-priority metadata that supports the item but is not essential to its immediate understanding.

**`Label strong`** Use Label strong when the trailing value requires additional visual emphasis, for example when users need to compare important values across a navigation list.

**`Label + Extra label`** Use Label + Extra label when a value requires a short qualifier, unit or supporting label.

**`Badge`** Use a Badge to communicate a compact status or notification associated with the item. A badge should contain secondary information and must not replace the primary label or description.

**Type**

**`Badge`** Use Badge for a short textual status. Keep the label concise and use terminology consistently throughout the product.

**`Badge count`** Use Badge count to display a short numerical quantity, such as unread items, notifications or occurrences associated with the destination.

⚠️ The count must have a clear relationship with the primary item. Users should not need to guess what is being counted.
⚠️ The complete meaning should be available through visible or accessible text, for example “2 unread messages”, rather than an isolated “2”.

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

**`Enabled`** Use when the Badge communicates a current and applicable status or count associated with the destination.

**`Disabled`** Use when the status represented by the Badge is inactive, unavailable or no longer applicable.

The Badge state does not control whether the Navigation list item itself can be activated. Use the main item’s State property when the navigation destination must be disabled.

⚠️ Do not use Disabled merely to reduce the visual emphasis of the Badge.

**`Tag`** Use a Tag to communicate a category, attribute, classification or compact status associated with the navigation destination.

**Appearance**

**`Emphasized`** Use Emphasized when the tag carries information that should be easy to notice while remaining secondary to the primary label.

**`Muted`** Use Muted for low-priority categories or supporting metadata.

**Status**

**`Not functional`**

**`Neutral`** Use Neutral for general categories, attributes or metadata without a specific semantic meaning.

**`Accent`** se Accent for branded or noteworthy information that does not correspond to a functional status.
Do not use Accent solely to attract attention to the destination.

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

**`Disabled`** A non-active state used when the information represented by the Tag is unavailable or no longer applicable.
⚠️ The Tag state does not disable the Navigation list item. Use the main item’s Disabled state when the destination itself is unavailable.

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

✅ **Do:** Give badge counts a clear meaning, for example “2 unread messages”  
❌ **Don't:** Show an isolated number whose meaning users must guess

✅ **Do:** Use tags for categories or compact statuses, in the Small size by default  
❌ **Don't:** Make a tag or badge interactive inside the item

✅ **Do:** Use a container type different from the leading one  
❌ **Don't:** Use the same container type in both positions

✅ **Do:** Pair functional statuses with their predefined icons and explicit text  
❌ **Don't:** Signal the status of a destination with colour alone

---

## Divider

**`False`** No divider is displayed. Use this option when items are already separated by spacing, individual backgrounds or another clear grouping method.

**`True`** A divider is displayed between list items. Use it when several items share the same surface and additional visual separation improves scanning.

⚠️ The divider separates adjacent navigation items visually. It must not reduce or split the interactive area of either item.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use dividers when several items share the same surface and need extra separation  
❌ **Don't:** Add dividers when items are already separated by spacing or backgrounds

✅ **Do:** Apply dividers consistently within a list  
❌ **Don't:** Divide only some of the adjacent items of the same list

✅ **Do:** Keep the whole row interactive around the divider  
❌ **Don't:** Let the divider split or reduce the interactive area of an item

✅ **Do:** Avoid a divider that doubles the edge of the surrounding container  
❌ **Don't:** Stack a divider against a container border

✅ **Do:** Use section headings or spacing to show groups of different meaning  
❌ **Don't:** Rely on dividers alone to communicate grouping

---

## Helper text

**`False`** No helper text is displayed.

**`True`** Helper text is displayed below the primary content.
Use it for additional information required to understand the destination before navigation, such as availability, conditions or supporting context.

⚠️ Helper text remains part of the complete navigation target and must not contain a separate link or action.

---

## helper_text_do_&_dont 👈🤔

✅ **Do:** Use helper text for information users need before navigating, such as availability or conditions  
❌ **Don't:** Repeat the label or the description in the helper text

✅ **Do:** Keep helper text short and specific  
❌ **Don't:** Write long paragraphs that push the next items far down

✅ **Do:** Keep helper text part of the same navigation target  
❌ **Don't:** Put a separate link or action in the helper text

✅ **Do:** Use Top alignment when helper text is displayed  
❌ **Don't:** Keep Center alignment on an item that shows helper text

✅ **Do:** Explain why a disabled destination is unavailable when users need to know  
❌ **Don't:** Show a disabled item with no explanation when the reason matters

---

## Background

**`False`** The item uses the surrounding container surface without an individual background.
Use this option for standard continuous navigation lists.

**`True`** A background is applied to the item.
Use it when the navigation item needs stronger visual separation from its surrounding context or represents a distinct destination within a grouped layout.

---

## background_do_&_dont 👈🤔

✅ **Do:** Use no background for standard continuous navigation lists  
❌ **Don't:** Add a background to every item of a long list by default

✅ **Do:** Add a background when an item must stand apart from its context or in a grouped layout  
❌ **Don't:** Use a background to signal selection, status or urgency

✅ **Do:** Keep hover, pressed and focus treatments clearly visible on the background  
❌ **Don't:** Choose a background that hides the interaction states

✅ **Do:** Apply the background consistently to items that play the same role  
❌ **Don't:** Mix items with and without a background in the same group without a reason

✅ **Do:** Keep list and link semantics independent of the background  
❌ **Don't:** Rely on the background alone to show where an item ends

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

⚠️ The Label Slot must remain non-interactive. Do not place a link, button or control inside it because the complete item already acts as one navigation link.

---

## label_type_do_&_dont 👈🤔

✅ **Do:** Use the Default label type for most items  
❌ **Don't:** Make every label bold; emphasis then loses its meaning

✅ **Do:** Use Bold when labels must be scanned quickly or item names are important  
❌ **Don't:** Mix Default and Bold labels in one list without a reason

✅ **Do:** Write specific, familiar labels that say where the item leads  
❌ **Don't:** Use vague labels such as “More”, “Click here” or “Learn more”

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
❌ **Don't:** Use the overline for the destination name

✅ **Do:** Keep overlines to a few words  
❌ **Don't:** Write sentences in the overline

✅ **Do:** Use overlines consistently for items of the same kind  
❌ **Don't:** Show overlines on random items only

✅ **Do:** Keep the overline before the label in the reading order  
❌ **Don't:** Hide information users need to identify the destination in the overline only

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

⚠️ The Description must not contain a separate inline link.

---

## description_do_&_dont 👈🤔

✅ **Do:** Add a description when users need context to understand or choose the destination  
❌ **Don't:** Repeat the label in other words

✅ **Do:** Keep descriptions brief, one or two lines where possible  
❌ **Don't:** Write long paragraphs inside list items

✅ **Do:** Use Top alignment when a description is shown  
❌ **Don't:** Keep Center alignment on items with a description

✅ **Do:** Keep the description inside the same navigation target  
❌ **Don't:** Add an inline link inside the description

✅ **Do:** Let descriptions wrap rather than truncate essential information  
❌ **Don't:** Cut descriptions that users need in order to decide

---

## Slot (bottom)

The Bottom slot adds a custom content area below the main row content.
Use it when supporting information cannot be clearly represented by the standard Description or Helper text properties.
All Bottom slot content remains part of the same navigation target.

**`False`** No additional content is displayed below the main content.

**`True`** A custom content area is displayed below the main content.

It may contain non-interactive supporting content such as:
• A progress indicator.
• A compact group of metadata.
• A visual preview.
• A status summary.
• Product-specific supporting information.

⚠️ The Bottom slot must not contain links, buttons or other independently interactive elements.

If the supporting content requires a separate destination or action, place it outside the Navigation list item or use another component architecture.

---

## slot_bottom_do_&_dont 👈🤔

✅ **Do:** Use the Bottom slot for non-interactive supporting content: progress, metadata, preview  
❌ **Don't:** Put buttons, links or controls in the Bottom slot

✅ **Do:** Use it only when Description or Helper text cannot express the content  
❌ **Don't:** Use it as the default place for supporting text

✅ **Do:** Keep Bottom slot content visually secondary to the label  
❌ **Don't:** Let the slot content dominate the item

✅ **Do:** Keep the whole item, slot included, one navigation target  
❌ **Don't:** Give slot content its own focus stop

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
• Do not place an inline Link component inside a Navigation list item. The entire item already acts as a single navigation link, and nested links create conflicting pointer, keyboard and assistive-technology behaviour.
• Essential information about the destination must remain available directly in the Label, Description or Helper text.

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

✅ **Do:** Keep the whole item as the only link  
❌ **Don't:** Place an inline Link component inside the item

---

## Multiline and responsiveness

**Multiline**
The Navigation list item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.
The item expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the item contains a Description, Helper text or Bottom slot. The navigation indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.

⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make navigation lists more difficult to scan.

**Max-width vs full-width**
The Navigation list item does not have a default maximum width. Its width is defined by its parent container or navigation layout.
The item’s interactive surface extends across its complete visible width. The clickable area must not be limited to the Label or navigation indicator. On wide layouts, the text area may use a product-defined maximum width to maintain readability. The item’s background, divider, hover, pressed and focus treatments must still cover the complete navigation target.

The navigation indicator remains positioned at the logical edge of the item:
• At the logical end for the Next layout.
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

⚠️ Do not apply a text maximum width that creates a large visual gap between the Label and related Trailing content. The relationship between all parts of the item must remain clear.

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
❌ **Don't:** Truncate information users need to understand the destination

✅ **Do:** Let the item grow vertically with its content  
❌ **Don't:** Set a fixed height on list items

✅ **Do:** Switch to Top alignment when text becomes multiline  
❌ **Don't:** Keep Center alignment with multiline labels

✅ **Do:** Remove optional decorative content first on narrow layouts  
❌ **Don't:** Hide the description or statuses to keep the item on one line

✅ **Do:** Test at 200% text size, 320 px width and with longer translations  
❌ **Don't:** Validate the layout only with short English labels on desktop

---

## Technical layout adjustments

Even though, in Figma, the component structure is unique (for easier use by designers), technically the versions differ in order to respect best practices for each environment (paradigm shift between the web “Container” vs. the native “Edge-to-Edge”):

**Web (mobile, tablet, and desktop)**
The component is contained within the browser window and has “safety margins.” It therefore cannot appear in the area corresponding to the margin grid. The component has internal padding-inline, and its display position must be between several columns (which varies depending on the number of containers used on a horizontal row).

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

✅ **Do:** Keep the interactive area covering the full visible row on every platform  
❌ **Don't:** Reduce the interactive area when switching to edge to edge

---

# Specs

## States

**`Enabled`** Enabled is the default state. The item is available for navigation.
The entire item acts as a single link target.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the item. Hover must not move content, change the item’s dimensions or reveal information required to understand the destination.

**`Focus`** Focus indicates that the entire navigation item is currently selected for keyboard interaction. Display one clear focus indicator around the complete navigation target.

**`Pressed`** Pressed is a temporary state displayed while the item is being activated. Apply the pressed treatment to the entire navigation target.

**`Disabled`** Use Disabled when the destination is temporarily unavailable or cannot currently be accessed. A Disabled navigation item must not respond to pointer or keyboard activation and must not be included in the keyboard focus order.

**`Skeleton`** Use Skeleton while the navigation item’s content or destination is loading and is not yet available. A Skeleton item is a placeholder and must not behave as a link or receive keyboard focus.

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

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 3, 2026 | 1.2.0 | <ul><li>Removal of the “Video” variant in leading and trailing positions.<li>For the nested “Image” component, addition of a new boolean variant, “Animated=True/False”, allowing the use of animated images in GIF or WEBP formats.</ul>**Bug fix**<ul><li>The “Icon”, “Image”, and “Avatar” assets in the trailing position of the “Size: Small” / “Alignment: Top alignment” variants no longer offer “Medium/Large” sizes.<li>Updated size tokens applied to “Icon” assets:<ul><li>Size “Small”: size/icon/with-label/large/size-small<li>Size “Medium”: size/icon/with-label/large/size-medium<li>Size “Large”: size/icon/with-label/large/size-xlarge</ul><li>Flag sizes have been updated for the “Small” and “Default” variants:<ul><li>Removal of the height token: list-item/size/flag/height<li>To replace it with the width tokens:<ul><li>Size “Small”: ouds/control/list-item/size/asset/small<li>Size “Medium”: ouds/control/list-item/size/asset/medium</ul></ul></ul> | Maxime Tonnerre |
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 31, 2026 | 1.1.0 | **Version 2.7 of the design tokens is required for the development of this update.**<br>The semantic tokens applied to the text within the nested elements “.Text container” and “.Text container / Top alignment” for the “Default” size variants:<ul><li>ouds/size/max-width/label-medium (used for the “Label”, “Extra label”, and “Description” text)<li>ouds/size/max-width/label-small (used for the “Overline” text)</ul>Are replaced with the following semantic token:<ul><li>ouds/size/max-width/boxed-text</ul> | Maxime Tonnerre |
| Jun 5, 2026 | 1.0.0 | **Version 2.4 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
