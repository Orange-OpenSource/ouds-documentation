# Static card item — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([static_card_item.md](static_card_item.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Summaries of an account, contract, plan or order grouped in one card

✅ Key figures, such as a data balance, price or due date, that need more prominence than a list row

✅ Dashboards or overview screens that group read-only information in cards

✅ Card collections where users compare products, plans or devices by value or status

✅ Information recognised faster with a visual cue: icon, image, avatar or flag

✅ Showing usage, progress or metadata below the main content with the Bottom slot

✅ Confirmation or review screens that recap details before a decision

✅ Status overviews of services, lines or devices, backed by a Badge or Tag

✅ A standalone card that highlights one piece of information among other page content

✅ Card layouts whose content loads progressively, using Skeleton placeholders

## Size — do & don't

✅ **Do:** Use the Default size for most cards, especially with multiline content or visuals  
❌ **Don't:** Switch to Small just to fit more cards when labels or visuals need room

✅ **Do:** Reserve Small for compact, information-dense layouts with short labels and simple metadata  
❌ **Don't:** Use Small for long descriptions or large avatars and images

✅ **Do:** Keep one size across a card collection so the cards read as a set  
❌ **Don't:** Mix Default and Small cards in one collection without a clear change of content group or hierarchy

✅ **Do:** Let the tallest element (label, avatar, image) define the card height  
❌ **Don't:** Force a fixed card height that clips multiline content

✅ **Do:** Check the Small size with real, translated content before adopting it  
❌ **Don't:** Assume short English labels stay short in every language

## Alignment — do & don't

✅ **Do:** Use Center for single-line cards whose elements have similar heights  
❌ **Don't:** Keep Center alignment when the label wraps onto several lines

✅ **Do:** Switch to Top alignment when a description, extra label or Bottom slot is shown  
❌ **Don't:** Leave leading visuals floating mid-height next to a tall block of text

✅ **Do:** Use the same alignment for equivalent cards of a collection  
❌ **Don't:** Alternate Center and Top alignment from one card to the next

✅ **Do:** Align trailing values with the first line of text in Top alignment  
❌ **Don't:** Let a value drift away from the label it belongs to

✅ **Do:** Keep the programmatic reading order unchanged whatever the alignment  
❌ **Don't:** Reorder content in code to follow a visual alignment choice

## Outlined — do & don't

✅ **Do:** Add an outline when the card sits on a surface with a similar background and needs a clear edge  
❌ **Don't:** Add an outline to a card that is already clearly separated by its background or spacing

✅ **Do:** Use the outline consistently for equivalent cards of a collection  
❌ **Don't:** Outline some cards only, suggesting a status or selection that does not exist

✅ **Do:** Communicate status or availability with text, a Badge or a Tag  
❌ **Don't:** Use the outline as the only cue for status, selection or importance

✅ **Do:** Keep the outlined card visibly static, with no hover or pressed treatment  
❌ **Don't:** Use an outline that makes a read-only card look like a button or a selectable option

✅ **Do:** Rely on the outline alone for separation when cards sit next to each other  
❌ **Don't:** Combine an outline with a Divider on the same card

## Rounded corner — do & don't

✅ **Do:** Decide rounded or square corners once for the whole product or service  
❌ **Don't:** Set rounded corners card by card, depending on the screen

✅ **Do:** Keep equivalent cards within an interface on the same corner style  
❌ **Don't:** Mix Rounded corner=True and False cards in the same collection

✅ **Do:** Check the brand theme before using rounded corners: Sosh and Wireframe do not support them  
❌ **Don't:** Design rounded cards for a brand theme where they are unavailable

✅ **Do:** Use rounded corners for a softer, friendlier feel  
❌ **Don't:** Use corner style to signal status, category or importance

✅ **Do:** Combine corner styles only for clearly documented card categories or levels of hierarchy  
❌ **Don't:** Change the corner style just to add visual variety

## Choosing leading and trailing content — do & don't

✅ **Do:** Choose each position from the content's role: recognition leading, supplementary information trailing  
❌ **Don't:** Pick a position only because there is space left

✅ **Do:** Use trailing content when users compare values across several cards  
❌ **Don't:** Hide the value users compare inside each description

✅ **Do:** Keep the label the clearest element when both positions are used  
❌ **Don't:** Let leading and trailing content compete with the label

✅ **Do:** Use a different container type in each position  
❌ **Don't:** Repeat the same information in the leading and trailing areas

✅ **Do:** Keep leading content clearly non-interactive  
❌ **Don't:** Make a leading icon or avatar look like a button users can tap

## Leading — do & don't

✅ **Do:** Add leading content when a visual cue helps users recognise the card faster  
❌ **Don't:** Add decorative leading content that tells users nothing

✅ **Do:** Display one leading container per card  
❌ **Don't:** Stack several visuals in the leading area

✅ **Do:** Use leading content consistently for equivalent cards of a collection  
❌ **Don't:** Show leading content on some cards only

✅ **Do:** Provide a text alternative when the leading visual adds information not in the label  
❌ **Don't:** Repeat the label in the leading visual's text alternative

✅ **Do:** Keep leading content static, like the rest of the card  
❌ **Don't:** Make the leading element an independent action inside a static card

## Leading container type — do & don't

✅ **Do:** Match the type to the content: icon for categories, image for products or media, avatar for people, flag for countries  
❌ **Don't:** Use images or avatars only to add visual variety

✅ **Do:** Keep one size per container type for comparable cards  
❌ **Don't:** Mix icon, image or avatar sizes arbitrarily in the same card collection

✅ **Do:** Always pair avatars and flags with a visible name  
❌ **Don't:** Rely on an avatar, initials or a flag alone to identify the subject

✅ **Do:** Use semantic statuses only when they carry that meaning, backed by text  
❌ **Don't:** Use functional colours for decoration or as the only status cue

✅ **Do:** Keep Slot for content the standard types cannot express, and keep it non-interactive  
❌ **Don't:** Put buttons, links, checkboxes or toggles inside a Slot

## Trailing — do & don't

✅ **Do:** Use trailing content for a value, status or category related to the label  
❌ **Don't:** Put information more important than the label in the trailing area

✅ **Do:** Keep trailing content short so the label keeps most of the width  
❌ **Don't:** Let trailing content squeeze the label into excessive wrapping

✅ **Do:** Align trailing values so users can compare them across cards  
❌ **Don't:** Mix value formats (units, date styles) from one card to the next

✅ **Do:** Disable the trailing container when it adds no useful information  
❌ **Don't:** Fill the trailing area just to balance the card

✅ **Do:** Keep trailing content read-only  
❌ **Don't:** Place a button, link or chevron in the trailing area of a static card

## Trailing container type — do & don't

✅ **Do:** Keep trailing text to one or two words, such as a value or a short status  
❌ **Don't:** Write sentences in trailing text; use Description or Helper text instead

✅ **Do:** Give badge counts a clear meaning, for example “2 connected devices”  
❌ **Don't:** Show an isolated number whose meaning users must guess

✅ **Do:** Use tags for categories or compact statuses, in the Small size by default  
❌ **Don't:** Make a tag or badge interactive inside the card

✅ **Do:** Use a container type different from the leading one  
❌ **Don't:** Use the same container type in both positions

✅ **Do:** Pair functional statuses with their predefined icons and explicit text  
❌ **Don't:** Signal a status with colour alone

## Divider — do & don't

✅ **Do:** Use a divider only when several cards are stacked on the same shared surface  
❌ **Don't:** Add a divider to a card that already has an outline or its own background

✅ **Do:** Apply dividers consistently within a stacked group  
❌ **Don't:** Divide only some of the adjacent cards of the same group

✅ **Do:** Separate standalone cards with spacing, an outline or a background  
❌ **Don't:** Use a divider as the only boundary of a standalone card

✅ **Do:** Use section headings or spacing to show groups of different meaning  
❌ **Don't:** Rely on dividers alone to communicate grouping

✅ **Do:** Keep the divider decorative and hidden from assistive technologies  
❌ **Don't:** Use a divider to suggest that cards can be selected or opened

## Helper text — do & don't

✅ **Do:** Use helper text for information needed to interpret the card content correctly  
❌ **Don't:** Repeat the label or the description in the helper text

✅ **Do:** Keep helper text short and specific  
❌ **Don't:** Write long paragraphs that make the card hard to scan

✅ **Do:** Use Top alignment when helper text is displayed  
❌ **Don't:** Keep Center alignment on a card that shows helper text

✅ **Do:** Explain why information is unavailable when a card is disabled  
❌ **Don't:** Show a disabled card with no explanation when the reason matters

✅ **Do:** Keep helper text plain, read-only text  
❌ **Don't:** Put a link or an action in the helper text

## Background — do & don't

✅ **Do:** Add a background when the card must stand apart from its context or represents a distinct read-only content area  
❌ **Don't:** Use a background to signal selection, status or urgency

✅ **Do:** Use no background when spacing, an outline or a divider already separates the card  
❌ **Don't:** Stack a background, an outline and a divider on the same card without need

✅ **Do:** Apply the background consistently to cards that play the same role  
❌ **Don't:** Mix cards with and without a background in the same collection without a reason

✅ **Do:** Keep text and icons at the required contrast on the background  
❌ **Don't:** Choose a background that lowers the contrast of labels or statuses

✅ **Do:** Keep backgrounds calm so the static card does not look like a button  
❌ **Don't:** Use a background that makes a static card look clickable

## Label type — do & don't

✅ **Do:** Use the Default label type for most cards  
❌ **Don't:** Make every label bold; emphasis then loses its meaning

✅ **Do:** Use Bold for important card titles or when labels must be scanned quickly  
❌ **Don't:** Mix Default and Bold labels in one collection without a reason

✅ **Do:** Write specific, familiar labels that name the subject or result  
❌ **Don't:** Use vague labels such as “Info” or “Details”

✅ **Do:** Use the label Slot only when standard properties cannot express the content  
❌ **Don't:** Put links, buttons or controls in the label Slot

✅ **Do:** Keep labels parallel in structure across the collection  
❌ **Don't:** End short labels with a period when they are not sentences

## Overline — do & don't

✅ **Do:** Use an overline for a short contextual qualifier, such as a category or section  
❌ **Don't:** Use the overline for the card title

✅ **Do:** Keep overlines to a few words  
❌ **Don't:** Write sentences in the overline

✅ **Do:** Use overlines consistently for cards of the same kind  
❌ **Don't:** Show overlines on random cards only

✅ **Do:** Keep the overline before the label in the reading order  
❌ **Don't:** Hide information users need to identify the card in the overline only

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
❌ **Don't:** Truncate it to keep the card on one line

## Description — do & don't

✅ **Do:** Add a description when users need context to understand the card content  
❌ **Don't:** Repeat the label in other words

✅ **Do:** Keep descriptions brief, one or two lines where possible  
❌ **Don't:** Write long paragraphs inside a card

✅ **Do:** Use Top alignment when a description is shown  
❌ **Don't:** Keep Center alignment on cards with a description

✅ **Do:** Keep the description plain text  
❌ **Don't:** Add an inline link inside the description

✅ **Do:** Let descriptions wrap rather than truncate essential information  
❌ **Don't:** Cut descriptions that users need to understand the card

## Slot (bottom) — do & don't

✅ **Do:** Use the Bottom slot for supporting content: progress, a group of metadata, a preview or a status summary  
❌ **Don't:** Put buttons, checkboxes, toggles or menus in the Bottom slot

✅ **Do:** Use it only when Description or Helper text cannot express the content  
❌ **Don't:** Use it as the default place for supporting text

✅ **Do:** Use the dedicated Link component when a link to more details is needed, placed after the card's information  
❌ **Don't:** Make the whole card clickable to reach those details

✅ **Do:** Give meaningful slot content, such as progress, a text equivalent  
❌ **Don't:** Rely on a visual-only indicator in the slot

✅ **Do:** Use Top alignment when the Bottom slot is enabled  
❌ **Don't:** Keep Center alignment on cards that use the Bottom slot

## Rich text — do & don't

✅ **Do:** Use one short Strong fragment to highlight key information, such as a status, date or amount  
❌ **Don't:** Emphasise several fragments in the same text

✅ **Do:** Use only the Label/Medium/Strong token for emphasis  
❌ **Don't:** Use other text styles, italics or custom font weights

✅ **Do:** Make sure the message stays clear without the emphasis  
❌ **Don't:** Use bold to compensate for unclear writing

✅ **Do:** Keep essential information in the Label, Description or Helper text  
❌ **Don't:** Underline text manually; users read it as a link

✅ **Do:** Keep the card's text free of inline links  
❌ **Don't:** Add an inline link to turn a static card into a navigation entry

## Multiline and responsiveness — do & don't

✅ **Do:** Let labels, descriptions and helper text wrap onto several lines  
❌ **Don't:** Truncate information users need to understand the card

✅ **Do:** Let the card grow vertically with its content  
❌ **Don't:** Set a fixed height on static cards

✅ **Do:** Switch to Top alignment when text becomes multiline  
❌ **Don't:** Keep Center alignment with multiline labels

✅ **Do:** Remove optional decorative content first on narrow layouts  
❌ **Don't:** Hide the description, values or statuses to keep the card on one line

✅ **Do:** Test at 200% text size, 320 px width and with longer translations  
❌ **Don't:** Validate the layout only with short English labels on desktop

## Technical layout adjustments — do & don't

✅ **Do:** Contain the card within the grid columns on the web, respecting the safety margins  
❌ **Don't:** Stretch web cards into the margin area

✅ **Do:** Display the card edge to edge in native apps  
❌ **Don't:** Add web-style outer margins around native cards

✅ **Do:** Replace the internal padding-inline with the grid-margin tokens in native apps  
❌ **Don't:** Hard-code horizontal padding values per screen

✅ **Do:** Keep one component in Figma and adapt it per platform in code  
❌ **Don't:** Create separate design components for web and native

✅ **Do:** Keep text aligned with the grid on every platform  
❌ **Don't:** Let content drift from the grid when switching to edge to edge
