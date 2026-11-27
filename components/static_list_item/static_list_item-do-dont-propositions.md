# Static list item — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([static_list_item.md](static_list_item.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Size — do & don't

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

## Alignment — do & don't

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

## Choosing leading and trailing content — do & don't

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

## Leading — do & don't

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

## Leading container type — do & don't

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

## Trailing — do & don't

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

## Trailing container type — do & don't

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

## Divider — do & don't

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

## Helper text — do & don't

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

## Background — do & don't

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

## Label type — do & don't

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

## Overline — do & don't

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

## Extra label — do & don't

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

## Description — do & don't

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

## Slot (bottom) — do & don't

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

## Rich text — do & don't

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

## Multiline and responsiveness — do & don't

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

## Technical layout adjustments — do & don't

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
