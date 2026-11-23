# Accordion card item — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([accordion_card_item.md](accordion_card_item.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Size — do & don't

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

## Alignment — do & don't

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

## Outlined — do & don't

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

## Rounded corner — do & don't

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

## Expanded — do & don't

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

## Expanded text — do & don't

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

## Slot (Below text) — do & don't

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

## Slot (Bottom) — do & don't

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

## Slot (Expand) — do & don't

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

## Alternative icon — do & don't

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

## Reverse — do & don't

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

## Leading — do & don't

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

## Leading container type — do & don't

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

## Trailing — do & don't

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

## Trailing container type — do & don't

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

## Divider — do & don't

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

## Background — do & don't

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

## Label type — do & don't

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

## Overline — do & don't

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

## Rich text — do & don't

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

## Technical layout adjustments — do & don't

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

## Multiline and responsiveness — do & don't

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

## Animation — do & don't

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
