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