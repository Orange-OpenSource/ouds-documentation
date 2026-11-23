# Navigation list item — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([navigation_list_item.md](navigation_list_item.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Size — do & don't

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

## Alignment — do & don't

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

## Layout — do & don't

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

## Navigation indicator type — do & don't

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

## Choosing leading and trailing content — do & don't

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

## Leading — do & don't

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

## Leading container type — do & don't

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

## Trailing — do & don't

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

## Trailing container type — do & don't

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

## Divider — do & don't

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

## Helper text — do & don't

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

## Background — do & don't

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

## Label type — do & don't

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

## Overline — do & don't

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

## Slot (bottom) — do & don't

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

## Rich text — do & don't

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

## Multiline and responsiveness — do & don't

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

## Technical layout adjustments — do & don't

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
