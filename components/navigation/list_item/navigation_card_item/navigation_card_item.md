# Guideline

## Intro 👈🤖

A navigation card item is a clickable card that leads users to one page or view, giving a destination more visual weight than a list row.

---

## Definition

A navigation card item is an interactive, self-contained card that takes users to one internal or external destination. Use it when navigational content requires stronger visual grouping or prominence than a standard navigation list item.
The card may be displayed independently or within a card-based layout and may use a distinct background, outline or rounded corners. The entire card acts as a single navigation target and supports the required hover, focus and pressed states. Do not use a Navigation card item when the card must contain several destinations or independent interactive controls.

---

## Best for 👈🤔

✅ Highlighting a few key destinations that need more prominence than a list row

✅ Dashboards or home screens that group entry points to main services in cards

✅ Standalone links to a single destination placed among other page content

✅ Card collections where users compare destinations by status, value or count

✅ Destinations recognised faster with a visual cue: icon, image, avatar or flag

✅ Account or product overviews that lead to a dedicated detail page

✅ Linking to another product or service, made explicit with the External indicator

✅ Returning to a parent level or an earlier step with the Previous layout

✅ Mobile layouts where the whole card must be one easy-to-reach tap target

✅ Card layouts that load progressively, using Skeleton placeholders

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The card surface that forms one navigation target, with optional background, outline, rounded corners and divider | N |
| 2 | Leading container | Icon, image, avatar, flag or slot that helps users recognise the destination | Y |
| 3 | Text container | The label (Default, Bold or Slot) with optional overline, extra label and description | N |
| 4 | Trailing container | Secondary information such as text, badge, tag or a shared container type | Y |
| 5 | Affordance indicator | Internal or External indicator, at the end (Next) or start (Previous) of the card | N |
| 6 | Helper text | Additional context users need before navigating, below the main content | Y |
| 7 | Bottom slot | Custom non-interactive content area below the main card content | Y |

---

## Size

**`Default`** Use the Default size in most interfaces.
It provides sufficient spacing for standalone navigation cards, card collections, multiline destination labels and visual elements such as avatars, images or badges.

**`Small`** Use the Small size in compact card-based layouts where information density is important.

The Small size is best suited to:
• Short destination labels.
• Simple supporting metadata.
• Compact desktop card layouts.

⚠️ Do not mix Default and Small cards within the same card collection unless they represent clearly different categories or levels of hierarchy.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use the Default size for most navigation cards, especially with multiline labels or visuals  
❌ **Don't:** Switch to Small just to fit more cards on a screen when labels or visuals need room

✅ **Do:** Reserve Small for compact, information-dense card layouts with short labels  
❌ **Don't:** Use Small in touch-first layouts where cards become harder to tap

✅ **Do:** Keep one size across a card collection so the cards read as a set  
❌ **Don't:** Mix Default and Small cards in one collection without a clear change of category or hierarchy

✅ **Do:** Let the card grow with its content, whatever the size  
❌ **Don't:** Force a fixed card height that clips multiline content

✅ **Do:** Check the Small size with real, translated labels before adopting it  
❌ **Don't:** Assume short English labels stay short in every language

---

## Alignment

**`Center`** Center alignment is the default for items containing:
• A single-line label.
• Short supporting content.
• Leading and trailing elements with similar dimensions.

⚠️ Do not use Center alignment when it makes an icon, avatar, value or affordance indicator appear visually disconnected from the first line of the card content.

**`Top`** Use Top alignment when:
• The label wraps onto multiple lines.
• A description or extra label is displayed.
• The Bottom slot is enabled.
• Leading or trailing content must remain aligned with the beginning of the text.
• The different content areas have noticeably different heights.

⚠ Top alignment must not change the navigation behaviour or the programmatic reading order of the card.

---

## alignment_do_&_dont 👈🤔

✅ **Do:** Use Center for single-line cards whose elements have similar heights  
❌ **Don't:** Keep Center alignment when the label wraps onto several lines

✅ **Do:** Switch to Top alignment when a description, helper text or Bottom slot is shown  
❌ **Don't:** Leave leading visuals floating mid-height next to a tall block of text

✅ **Do:** Use the same alignment for all cards of a collection  
❌ **Don't:** Alternate Center and Top alignment from one card to the next

✅ **Do:** Align leading and trailing content with the first line of text in Top alignment  
❌ **Don't:** Let the affordance indicator drift away from the label it belongs to

✅ **Do:** Keep the programmatic reading order unchanged whatever the alignment  
❌ **Don't:** Reorder content in code to follow a visual alignment choice

---

## Outlined

**`False`** No outline is displayed. Use when the card is already separated from the surrounding content by its background, spacing or container.

**`True`** An outline is displayed around the card. Use when the card needs clearer visual separation from a surface with a similar background.

⚠️ The outline is a visual treatment only. It must not be used as the only way to communicate status, availability or interactivity. The complete outlined surface remains one navigation target.

---

## outlined_do_&_dont 👈🤔

✅ **Do:** Add an outline when the card sits on a surface with a similar background and needs a clear edge  
❌ **Don't:** Add an outline to a card that is already clearly separated by its background or spacing

✅ **Do:** Use the outline consistently for equivalent cards of a collection  
❌ **Don't:** Outline some cards only, suggesting a status or selection that does not exist

✅ **Do:** Keep the whole outlined surface one navigation target  
❌ **Don't:** Make only the area inside the outline, or only the label, clickable

✅ **Do:** Communicate status, availability or selection with text or a Badge or Tag  
❌ **Don't:** Use the outline as the only cue for status, availability or interactivity

✅ **Do:** Rely on the outline alone for separation when cards sit next to each other  
❌ **Don't:** Combine an outline with a Divider on the same card

---

## Rounded corner

Although this rendering option is available in the properties of each Navigation card item in Figma, its configuration should be defined consistently across the product or service in which the component is used.
Equivalent cards within the same interface should not arbitrarily mix Rounded corner=True and Rounded corner=False.

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

## rounded_corner_do_&_dont 👈🤔

✅ **Do:** Decide rounded or square corners once for the whole product or service  
❌ **Don't:** Set rounded corners card by card, depending on the screen

✅ **Do:** Keep equivalent cards within an interface on the same corner style  
❌ **Don't:** Mix Rounded corner=True and False cards in the same collection

✅ **Do:** Check the brand theme before using rounded corners: Sosh and Wireframe do not support them  
❌ **Don't:** Design rounded cards for a brand theme where they are unavailable

✅ **Do:** Use rounded corners for a softer, friendlier feel on touch-first interfaces  
❌ **Don't:** Use corner style to signal status, category or importance

✅ **Do:** Make focus, hover and pressed treatments follow the card's corner radius  
❌ **Don't:** Draw a square focus ring around a rounded card

---

## Layout

**`Next`** Use Next when the destination moves users forward, deeper into the information hierarchy or to a related destination. The affordance indicator is positioned at the logical end of the card.

**`Previous`** Use Previous when the destination returns users to a parent destination, an earlier level or a preceding step in a navigation flow. The affordance indicator is positioned at the logical start of the card.

⚠️ Leading content is not supported in the Previous layout because the affordance indicator occupies the leading area. Only Trailing content can be added to provide secondary information.

---

## layout_do_&_dont 👈🤔

✅ **Do:** Use Next for forward, deeper or related destinations  
❌ **Don't:** Use Next for a card that actually returns to a parent level

✅ **Do:** Use Previous only to return to a parent destination, an earlier level or a preceding step  
❌ **Don't:** Use Previous as a decorative mirrored version of the card

✅ **Do:** Name the target in a Previous card, for example the parent page  
❌ **Don't:** Label a Previous card only “Back” when the parent level is not obvious

✅ **Do:** Add trailing content when a Previous card needs secondary information  
❌ **Don't:** Add leading content to a Previous card; the indicator already occupies that area

✅ **Do:** Keep the indicator at the logical start or end, including in right-to-left languages  
❌ **Don't:** Hard-code the indicator direction so it breaks in right-to-left layouts

---

## Navigation indicator type

**`Internal`** Use Internal when the card navigates to another destination within the same product, service or application.
The internal affordance indicator reinforces that activating the complete card opens another view or level.

**`External`** Use External when the card navigates outside the current product, service or application. The external affordance indicator informs users that the destination belongs to another context.

⚠️ When opening the destination in a new browser tab or window would be unexpected, communicate this through visible supporting text or the card’s accessible description.

---

## navigation_indicator_type_do_&_dont 👈🤔

✅ **Do:** Use Internal for destinations within the same product, service or app  
❌ **Don't:** Use External just to make a card stand out

✅ **Do:** Use External when the destination leaves the current product, service or app  
❌ **Don't:** Rely on the External indicator alone to tell users they are leaving

✅ **Do:** Say when a destination opens in a new tab or window, in visible text or the card's accessible description  
❌ **Don't:** Assume that External always means a new tab

✅ **Do:** Use the same indicator type for equivalent destinations across the product  
❌ **Don't:** Change the indicator type for the same destination from one screen to another

✅ **Do:** Hide the indicator from assistive technologies once the link is correctly named  
❌ **Don't:** Let screen readers announce the arrow as a separate element

---

## Choosing leading and trailing content

Leading and trailing content serve different purposes within the navigation card.
• Leading content supports recognition and identification before users read the destination label.
• Trailing content provides supplementary information related to the destination after the main content has been understood.
The affordance indicator is separate from both areas and communicates the navigation behaviour of the complete card.
Choose each position according to the role of the content, not only according to the available space.

**Use leading content only**
Use leading content when the visual element helps users identify or understand the destination before reading its text.

Leading-only layouts are recommended when:
• Visual recognition is important.
• The destination does not require a secondary value or status.
• The main label needs most of the available horizontal space.
• The card is displayed in a narrow or compact layout.

⚠️ Leading content must not appear to be an independent action.

**Use trailing content only**
Use trailing content when the primary label is sufficient for identification and users mainly need to read or compare secondary information.

Trailing-only layouts are recommended when:
• Users compare values or statuses across a collection of cards.
• Visual identification is not required.
• The secondary information is closely associated with the destination.
• Preserving a clean card composition is more important than adding imagery.

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
• Preserve sufficient space for the Label and affordance indicator.

---

## choosing_leading_and_trailing_content_do_&_dont 👈🤔

✅ **Do:** Choose each position from the content's role: recognition leading, supplementary information trailing  
❌ **Don't:** Pick a position only because the card has space left

✅ **Do:** Use trailing content when users compare values or statuses across a card collection  
❌ **Don't:** Hide the value users compare inside the description of each card

✅ **Do:** Keep the label the clearest element when both positions are used  
❌ **Don't:** Let leading and trailing content compete with the label

✅ **Do:** Use a different container type in each position  
❌ **Don't:** Repeat the same information in the leading and trailing areas

✅ **Do:** Prefer leading-only layouts for narrow or compact cards  
❌ **Don't:** Enable both positions only to balance the card composition

---

## Leading

Leading content appears before the main label and supports recognition or identification of the card’s destination.
Use it when the visual element helps users understand the destination more quickly.
Leading content remains inside the complete card target and must not behave as an independent action.

**`False`** No leading content is displayed. The main content starts at the card’s default horizontal padding.

**`True`** A leading container is displayed before the main content. Use the Leading container type property to define its content, such as an icon, image, avatar, flag thumbnail or custom slot. The leading container remains part of the complete navigation card.

---

## leading_do_&_dont 👈🤔

✅ **Do:** Add leading content when a visual cue helps users recognise the destination faster  
❌ **Don't:** Add decorative leading content that tells users nothing

✅ **Do:** Keep leading content inside the single card target  
❌ **Don't:** Turn the leading element into an independent action, such as a separate tappable icon

✅ **Do:** Use leading content consistently for all cards of a collection  
❌ **Don't:** Show leading content on some cards only

✅ **Do:** Provide a text alternative when the leading visual adds information not in the label  
❌ **Don't:** Repeat the label in the leading visual's text alternative

✅ **Do:** Use the Next layout when a card needs leading content  
❌ **Don't:** Add leading content to a Previous card, which does not support it

---

## Leading container type

**`Icon`** Use an icon to reinforce the meaning of the destination or help users identify a familiar category, object or service.

⚠️ Do not use an action icon that suggests a separate operation inside the navigation card.

**Size**
Controls the visual prominence of the icon.

⚠️ Use the same icon size for comparable cards within the same card collection. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

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
Display a badge when a notification or secondary status must be associated with the destination represented by the icon.

**`False`** Display the icon without a badge.

**`True`** Display a badge when a notification must be associated with the icon.

**`Image`** Use an image when visual identification of the destination is important, for example for a product, service, article or media page.
Do not use an image when it does not add useful information or when it could be mistaken for a separate interactive preview.

**Size**
Controls the dimensions and visual prominence of the image.

⚠️ Use the same image size for comparable cards within the same card collection. Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use in compact or information-dense card layouts where the image remains secondary to the text.

**`Large`** Use in standard navigation cards where visual identification is important.

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
Defines whether the image can contain animated content such as a GIF or WEBP file. Use animation only when it provides meaningful value to the user and does not distract from the primary content or interaction.

**`False`** Displays a static image. Use when animation does not provide meaningful information or when a still representation is sufficient.

**`True`** Displays animated content. Use when the animation provides meaningful visual information or helps communicate the nature of the content.

**⚠️ Motion & Animation accessibility rules**
The use of motion and animation in our products and components requires particular attention to the accessibility guidelines available in the dedicated section of this documentation.

**`Avatar`** Use an avatar when the destination represents a person, profile, team, organisation or account.
The avatar supports visual recognition but must always be accompanied by a visible text label identifying the destination.

**Size**

**`Medium`** Use in compact cards or when the Avatar is secondary to the content.

**`Large`** Use in standard profile, people or account cards.

**`Xlarge`** Use when identity is a primary part of the card or when additional Avatar details must remain visible.

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
The Navigation card item already acts as one complete interactive link.
Custom Slot content must not contain:
• Buttons.
• Links.
• Checkboxes.
• Radio buttons.
• Toggles.
• Menus.
• Playback controls.
• Any independently focusable element.

Nested interactive elements create conflicting activation and focus behaviour. When an independent action is required, place it outside the Navigation card item or use another component designed to support multiple actions.

---

## leading_container_type_do_&_dont 👈🤔

✅ **Do:** Match the type to the destination: icon for categories, image for products or media, avatar for people, flag for countries  
❌ **Don't:** Use images or avatars only to decorate the card

✅ **Do:** Keep one size per container type within a card collection  
❌ **Don't:** Mix icon, image or avatar sizes arbitrarily across comparable cards

✅ **Do:** Always pair avatars and flags with a visible name  
❌ **Don't:** Rely on an avatar, initials or a flag alone to identify the destination

✅ **Do:** Use semantic statuses only when they carry that meaning, backed by text  
❌ **Don't:** Use functional colours for decoration or as the only status cue

✅ **Do:** Keep Slot for content the standard types cannot express, and keep it non-interactive  
❌ **Don't:** Put buttons, links or controls inside a Slot

---

## Trailing

Trailing content appears after the main content and communicates secondary information related to the card’s destination.
It remains part of the complete navigation card and must not behave as an independent action.

**`False`** No trailing content is displayed. The main content can use the available width of the card before the affordance indicator.

**`True`** A trailing container is displayed after the main content and before the affordance indicator.
Use the Trailing container type property to define its content, such as text, a Badge, Tag, icon, image, value or custom Slot.

---

## trailing_do_&_dont 👈🤔

✅ **Do:** Use trailing content for secondary information users compare across cards  
❌ **Don't:** Put information users need to identify the destination only in the trailing area

✅ **Do:** Keep trailing content short so the label keeps most of the width  
❌ **Don't:** Let trailing content squeeze the label into excessive wrapping

✅ **Do:** Keep trailing content inside the single card target  
❌ **Don't:** Add a separate action next to the affordance indicator

✅ **Do:** Place trailing content before the affordance indicator, as designed  
❌ **Don't:** Replace the affordance indicator with trailing content

✅ **Do:** Disable the trailing container when it adds no useful information  
❌ **Don't:** Fill the trailing area just to balance the card

---

## Trailing container type

**Shared container types**
The following types reuse the properties and guidance documented under Leading container type:
• Icon
• Image
• Avatar
• Flag
• Slot

Their meaning and nested properties remain the same. Only their position within the card changes.

⚠️ All Trailing content remains part of the same navigation card and must not receive independent focus or activation.
⚠️ Do not use the same container type in both the Leading and Trailing positions within the same card. If a type is used as Leading content, choose a different Trailing type or disable the Trailing container.

**`Text`** Use Text to display a short value or secondary piece of information associated with the navigation destination.

⚠️ Keep trailing text concise. When the information requires a sentence or explanation, use the Description or Helper text property instead.
⚠️ Trailing text is not a separate link label and must not suggest a different destination.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information that should remain clearly readable without drawing more attention than the primary label.

**`Label muted`** Use Label muted for low-priority metadata that supports the card but is not essential to its immediate understanding.

**`Label strong`** Use Label strong when the trailing value requires additional visual emphasis, for example when users need to compare important values across a collection of navigation cards.

**`Label + Extra label`** Use Label + Extra label when a value requires a short qualifier, unit or supporting label.

**`Badge`** Use a Badge to communicate a compact status or notification associated with the card’s destination. A Badge should contain secondary information and must not replace the primary Label or Description.

**Type**

**`Badge`** Use Badge for a short textual status. Keep the label concise and use terminology consistently throughout the product.

**`Badge count`** Use Badge count to display a short numerical quantity, such as unread items, notifications or occurrences associated with the destination.

⚠️ The count must have a clear relationship with the card’s primary subject. Users should not need to guess what is being counted.

**`Status`** The Status property defines the semantic colour and meaning of the badge.

⚠️ Colour must not be the only way the meaning is communicated. Provide an equivalent accessible description.

**`Not functional`**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Use to highlight branded, selected or noteworthy information that does not correspond to another semantic status. Do not use Accent solely to make a card more visually prominent.

**`Functional`**

**`Positive`** Use for successful, active, available or completed states.

**`Info`** Use for additional neutral information that may require attention but does not indicate success or risk.

**`Warning`** Use for states that require caution, awareness or future action.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

**Badge size**

**`XSmall`** Use for a very compact Badge within Small cards or dense card layouts.

**`Small`** Use for a standard compact notification Badge.

**`Medium`** Use when the Badge requires stronger visibility or accompanies a larger card.

**`Large`** Use only in spacious layouts where the Badge is a significant secondary element.

**Badge count size**

**`Medium`** Use Medium for standard or compact cards.

**`Large`** Use Large when the card uses larger dimensions or when a larger Badge is required to remain visually balanced with the surrounding content.

**State**

**`Enabled`** Use when the Badge communicates a current and applicable status or count associated with the destination.

**`Disabled`** Use when the status represented by the Badge is inactive, unavailable or no longer applicable.

The Badge state does not control whether the Navigation card item itself can be activated. Use the card’s main State property when the navigation destination must be disabled.

⚠️ Do not use Disabled merely to reduce the visual emphasis of the Badge.

**`Tag`** Use a Tag to communicate a category, attribute, classification or compact status associated with the card’s navigation destination.

**Appearance**

**`Emphasized`** Use Emphasized when the tag carries information that should be easy to notice while remaining secondary to the primary label.

**`Muted`** Use Muted for low-priority categories or supporting metadata.

**Status**

**`Not functional`**

**`Neutral`** Use Neutral for general categories, attributes or metadata without a specific semantic meaning.

**`Accent`** Use Accent for branded or noteworthy information that does not correspond to a functional status.
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

**`Small`** Use Small as the standard and recommended Tag size within the card. It keeps the Tag visually secondary, preserves space for the main content and works well in compact or information-dense card layouts.

**`Default`** Use Default when the card uses a larger layout or when the Tag must align with other Default-size Tags in the same interface.

**State**

**`Enabled`** The default state of the tag, used to display the main information or status.

**`Loading`** A state where the tag shows a loader together with text.

**`Disabled`** A non-active state used when the information represented by the Tag is unavailable or no longer applicable.

⚠️ The Tag state does not disable the Navigation card item. Use the card’s main Disabled state when the destination itself is unavailable.

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
❌ **Don't:** Make a tag or badge interactive inside the card

✅ **Do:** Use a container type different from the leading one  
❌ **Don't:** Use the same container type in both positions

✅ **Do:** Pair functional statuses with their predefined icons and explicit text  
❌ **Don't:** Signal the status of a destination with colour alone

---

## Divider

**`False`** No Divider is displayed.
Use this option when the card is already separated from surrounding content by spacing, a background, an outline or another clear visual boundary.

**`True`** A Divider is displayed along the bottom edge of the card.
Use it when several navigation cards are vertically grouped within the same shared surface and additional visual separation improves scanning.

Avoid using a Divider when each card already has an individual outline or clearly separated background.

---

## divider_do_&_dont 👈🤔

✅ **Do:** Use a divider only when several cards are stacked on the same shared surface  
❌ **Don't:** Add a divider to a card that already has an outline or its own background

✅ **Do:** Apply dividers consistently within a stacked group  
❌ **Don't:** Divide only some of the adjacent cards of the same group

✅ **Do:** Keep the whole card interactive around the divider  
❌ **Don't:** Let the divider split or reduce the interactive area of the card

✅ **Do:** Separate standalone cards with spacing rather than a divider  
❌ **Don't:** Add a divider under a card that stands alone

✅ **Do:** Use section headings or spacing to show groups of different meaning  
❌ **Don't:** Rely on dividers alone to communicate grouping

---

## Helper text

**`False`** No helper text is displayed.

**`True`** Helper text is displayed below the primary content.
Use it for additional information required to understand the destination before navigation, such as availability, conditions or supporting context.

⚠️ Helper text remains part of the complete navigation card and must not contain a separate link or action.

---

## helper_text_do_&_dont 👈🤔

✅ **Do:** Use helper text for information users need before navigating, such as availability or conditions  
❌ **Don't:** Repeat the label or the description in the helper text

✅ **Do:** Keep helper text short and specific  
❌ **Don't:** Write long paragraphs that make the card hard to scan

✅ **Do:** Keep helper text part of the same navigation target  
❌ **Don't:** Put a separate link or action in the helper text

✅ **Do:** Use Top alignment when helper text is displayed  
❌ **Don't:** Keep Center alignment on a card that shows helper text

✅ **Do:** Explain why a disabled destination is unavailable when users need to know  
❌ **Don't:** Show a disabled card with no explanation when the reason matters

---

## Background

**`False`** The card uses the surrounding container surface without an individual background.
Use this option when spacing, an outline or the parent card layout already provides sufficient visual separation.

**`True`** A background is applied to the card.
Use it when the navigation card needs stronger visual separation from its surrounding context or represents a distinct destination within a card-based layout.
The entire visible background remains part of the same navigation target.

---

## background_do_&_dont 👈🤔

✅ **Do:** Add a background when the card must stand apart from its context or represents a distinct destination  
❌ **Don't:** Use a background to signal selection, status or urgency

✅ **Do:** Use no background when spacing, an outline or the parent layout already separates the card  
❌ **Don't:** Stack a background, an outline and a divider on the same card without need

✅ **Do:** Keep hover, pressed and focus treatments clearly visible on the background  
❌ **Don't:** Choose a background that hides the interaction states

✅ **Do:** Apply the background consistently to cards that play the same role  
❌ **Don't:** Mix cards with and without a background in the same collection without a reason

✅ **Do:** Keep the entire visible background part of the navigation target  
❌ **Don't:** Leave dead, non-clickable zones inside the card background

---

## Label type

**`Default`** Use Default for most navigation cards.
It provides the standard visual hierarchy and should be the preferred option for common destination labels, names and titles.

**`Bold`** Use Bold when the primary destination label requires stronger emphasis.

Suitable for:
• Important destination names.
• Card collections where primary labels must be scanned quickly.
• Prominent destinations within a clearly defined group.

**`Slot`** Use Slot when the standard label cannot support the required content structure.

The Slot may be used for custom primary content such as:
• A product-specific text arrangement.
• A combination of text elements not supported by the standard properties.

⚠️ The Label Slot must remain non-interactive. Do not place a Link, Button or control inside it because the complete card already acts as one navigation link.

---

## label_type_do_&_dont 👈🤔

✅ **Do:** Use the Default label type for most cards  
❌ **Don't:** Make every label bold; emphasis then loses its meaning

✅ **Do:** Use Bold for prominent destinations or collections that must be scanned quickly  
❌ **Don't:** Mix Default and Bold labels in one collection without a reason

✅ **Do:** Write specific, familiar labels that say where the card leads  
❌ **Don't:** Use vague labels such as “More”, “Click here” or “Learn more”

✅ **Do:** Use the label Slot only when standard properties cannot express the content  
❌ **Don't:** Put links, buttons or controls in the label Slot

✅ **Do:** Keep labels parallel in structure across the collection  
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

✅ **Do:** Use overlines consistently for cards of the same kind  
❌ **Don't:** Show overlines on random cards only

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
❌ **Don't:** Truncate it to keep the card on one line

---

## Description

**`False`** No supporting description is displayed.

**`True`** Supporting text is displayed below the primary Label.
Use a Description when users need additional context to understand where the card leads or what information they will find at the destination.

⚠️ The Description must not contain a separate inline link.

---

## description_do_&_dont 👈🤔

✅ **Do:** Add a description when users need to know where the card leads or what they will find there  
❌ **Don't:** Repeat the label in other words

✅ **Do:** Keep descriptions brief, one or two lines where possible  
❌ **Don't:** Write long paragraphs inside cards

✅ **Do:** Use Top alignment when a description is shown  
❌ **Don't:** Keep Center alignment on cards with a description

✅ **Do:** Keep the description inside the same navigation target  
❌ **Don't:** Add an inline link inside the description

✅ **Do:** Let descriptions wrap rather than truncate essential information  
❌ **Don't:** Cut descriptions that users need in order to decide

---

## Slot (bottom)

The Bottom slot adds a custom content area below the main card content.
Use it when supporting information cannot be clearly represented by the standard Description or Helper text properties.
All Bottom slot content remains part of the same navigation card.

**`False`** No additional content is displayed below the main content.

**`True`** A custom content area is displayed below the main content.

It may contain non-interactive supporting content such as:
• A progress indicator.
• A compact group of metadata.
• A visual preview.
• A status summary.
• Product-specific supporting information.

⚠️ The Bottom slot must not contain links, buttons or other independently interactive elements.

If the supporting content requires a separate destination or action, place it outside the Navigation card item or use another component architecture.

---

## slot_bottom_do_&_dont 👈🤔

✅ **Do:** Use the Bottom slot for non-interactive supporting content: progress, metadata, preview  
❌ **Don't:** Put buttons, links or controls in the Bottom slot

✅ **Do:** Use it only when Description or Helper text cannot express the content  
❌ **Don't:** Use it as the default place for supporting text

✅ **Do:** Keep Bottom slot content visually secondary to the label  
❌ **Don't:** Let the slot content dominate the card

✅ **Do:** Keep the whole card, slot included, one navigation target  
❌ **Don't:** Give slot content its own focus stop

✅ **Do:** Move content that needs its own destination or action outside the card  
❌ **Don't:** Turn a navigation card into a container of several actions

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important part of the message. It must never compensate for unclear writing.

**Strong text**
• Strong text can be used sparingly in the helper text or description to highlight key information, such as a status, date, amount, or required step. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**⚠️ Underline text and Hyperlinks**
• Underlined text must not be applied manually in the Description or Helper text, as users commonly interpret underlined content as a hyperlink.
• Do not place an inline Link component inside a Navigation card item. The entire item already acts as a single navigation link, and nested links create conflicting pointer, keyboard and assistive-technology behaviour.
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

✅ **Do:** Keep the whole card as the only link  
❌ **Don't:** Place an inline Link component inside the card

---

## Multiline and responsiveness

**Multiline**
The Navigation card item supports multiline content. The number of lines is not limited.
The Label, Extra label, Description, Helper text and supported text content must wrap when there is not enough horizontal space.
The card expands vertically to display its complete content. Do not use a fixed height or truncate information that users need to understand the destination.

⚠️ Use Top alignment when the Label wraps onto multiple lines or when the card contains a Description, Helper text or Bottom slot.
The affordance indicator must remain visible and must not overlap, truncate or become visually disconnected from the destination label.

⚠️ Keep the destination Label concise. Multiline content is supported, but excessively long labels make card collections more difficult to scan.

**Max-width vs full-width**
The Navigation card item does not have a default maximum width. Its width is defined by its parent container, grid or card-based layout.
The card’s interactive surface extends across its complete visible width and height. The clickable area must not be limited to the Label or affordance indicator.
On wide layouts, the text area may use a product-defined maximum width to maintain readability. The card’s background, outline, Hover, Pressed and Focus treatments must still cover the complete navigation target.

The affordance indicator remains positioned at the logical edge of the card:
• At the logical end for the Next layout.
• At the logical start for the Previous layout.

Optional Leading and Trailing content must not reduce the text area to an unusable width.

⚠️ Do not apply a text maximum width that makes the relationship between the card’s Label, secondary content and affordance indicator unclear.

**User zoom in/out**
The Navigation card item must remain readable, operable and complete when users zoom the interface or increase the text size.

⚠️ Avoid combining too many optional elements. Trailing content with Hug contents may leave too little space for the Label and Description, causing excessive wrapping. Prioritise the text area and remove non-essential content when space is limited.

• The component must adapt without clipping, overlapping or hiding meaningful information.
• Text must resize with the user’s browser or system settings. Text resizing must not be blocked.
• The Label, Extra label, Description, Helper text, Trailing text, Badge and Tag must wrap when required.
• The card must expand vertically according to its content. Do not use a fixed height.
• The entire visible card must remain one interactive target. Zoom must not reduce the clickable area to the Label or affordance indicator.
• The affordance indicator must remain visible and must not overlap the text or move onto a separate, unrelated line.
• Leading and Trailing content must remain aligned with the related text. Use Top alignment when increased text size creates multiline content.
• Optional decorative content may be simplified on narrow layouts, but meaningful status, destination and supporting information must remain available.
• Do not truncate essential destination labels, statuses, prices, dates or values to preserve the original desktop layout.
• Focus, Hover and Pressed treatments must adapt to the expanded card dimensions and continue to cover the complete navigation target.
• In the Previous layout, the affordance indicator remains at the logical start. Leading content is not supported, including after responsive reflow.
• In the Next layout, the affordance indicator remains at the logical end. Leading content may be retained when it does not prevent the Label from reflowing correctly.
• The component must support longer translated content without changing its meaning or losing information.

⚠️ Do not reduce the font size, hide the Description or remove meaningful status information solely to keep the card on one line.

---

## multiline_and_responsiveness_do_&_dont 👈🤔

✅ **Do:** Let labels, descriptions and helper text wrap onto several lines  
❌ **Don't:** Truncate information users need to understand the destination

✅ **Do:** Let the card grow vertically with its content  
❌ **Don't:** Set a fixed height on navigation cards

✅ **Do:** Keep the whole card surface clickable at every width and zoom level  
❌ **Don't:** Reduce the clickable area to the label or the affordance indicator

✅ **Do:** Remove optional decorative content first on narrow layouts  
❌ **Don't:** Hide the description or statuses to keep the card on one line

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

✅ **Do:** Contain the card within the grid columns on the web, respecting the safety margins  
❌ **Don't:** Stretch web cards into the margin area

✅ **Do:** Display the card edge to edge in native apps  
❌ **Don't:** Add web-style outer margins around native cards

✅ **Do:** Replace the internal padding-inline with the grid-margin tokens in native apps  
❌ **Don't:** Hard-code horizontal padding values per screen

✅ **Do:** Keep one component in Figma and adapt it per platform in code  
❌ **Don't:** Create separate design components for web and native

✅ **Do:** Keep the interactive area covering the full visible card on every platform  
❌ **Don't:** Reduce the interactive area when switching to edge to edge

---

# Specs

## States

**`Enabled`** Enabled is the default state. The card is available for navigation.
The entire visible card acts as a single link target.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the card.
Apply the Hover treatment to the complete card surface. It must not move content, change the card’s dimensions or reveal information required to understand the destination.

**`Focus`** Focus indicates that the complete navigation card is currently selected for keyboard interaction.
Display one clear focus indicator around the complete card target.

**`Pressed`** Pressed is a temporary state displayed while the card is being activated. Apply the Pressed treatment to the complete card surface.

**`Disabled`** Use Disabled when the destination is temporarily unavailable or cannot currently be accessed. A Disabled Navigation card item must not respond to pointer or keyboard activation and must not be included in the keyboard focus order.

**`Skeleton`** Use Skeleton while the card’s content or destination is loading and is not yet available. A Skeleton card is a placeholder and must not behave as a link or receive keyboard focus.

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

**Usage with limited vision**

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

**Usage without perception of colour**

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

**Usage with limited manipulation or strength**

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

**Usage with limited cognition, language or learning**

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

**Minimize photosensitive seizure triggers**

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

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 3, 2026 | 1.2.0 | <ul><li>Removal of the “Video” variant in leading and trailing positions.<li>Removal of the “Divider flexibility” parameter when “Outlined=True”.<li>For the nested “Image” component, addition of a new boolean variant, “Animated=True/False”, allowing the use of animated images in GIF or WEBP formats.</ul>**Bug fix**<ul><li>The “Icon”, “Image”, and “Avatar” assets in the trailing position of the “Size: Small” / “Alignment: Top alignment” variants no longer offer “Medium/Large” sizes.<li>Updated size tokens applied to “Icon” assets:<ul><li>Size “Small”: size/icon/with-label/large/size-small<li>Size “Medium”: size/icon/with-label/large/size-medium<li>Size “Large”: size/icon/with-label/large/size-xlarge</ul><li>Flag sizes have been updated for the “Small” and “Default” variants:<ul><li>Removal of the height token: list-item/size/flag/height<li>To replace it with the width tokens:<ul><li>Size “Small”: ouds/control/list-item/size/asset/small<li>Size “Medium”: ouds/control/list-item/size/asset/medium</ul></ul></ul> | Maxime Tonnerre |
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 31, 2026 | 1.1.0 | **Version 2.7 of the design tokens is required for the development of this update.**<br>The semantic tokens applied to the text within the nested elements “.Text container” and “.Text container / Top alignment” for the “Default” size variants:<ul><li>ouds/size/max-width/label-medium (used for the “Label”, “Extra label”, and “Description” text)<li>ouds/size/max-width/label-small (used for the “Overline” text)</ul>Are replaced with the following semantic token:<ul><li>ouds/size/max-width/boxed-text</ul> | Maxime Tonnerre |
| Jun 5, 2026 | 1.0.0 | **Version 2.4 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
