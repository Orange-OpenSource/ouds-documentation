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