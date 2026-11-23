# Accordion Q&A — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([accordion_qa.md](accordion_qa.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Frequently asked questions on a help, support or product page

✅ Questions users scan to find the one that matches their problem

✅ Short answers that stand on their own without the other questions

✅ Reducing the length of a support page when users need only one or two answers

✅ Product pages that answer common pre-purchase questions

✅ Small screens, where a list of questions is easier to scan than long text

✅ Questions that can be written in the words users would use

✅ Answers that may contain a list, a table or a link, through the Expand slot

✅ Groups of related questions under a common heading

✅ Complementary information only: instructions users must follow stay visible on the page

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

✅ **Do:** Use trailing content only when it helps users choose a question  
❌ **Don't:** Fill the trailing area just to balance the trigger

✅ **Do:** Keep trailing content non-interactive and part of the trigger  
❌ **Don't:** Place a button or link in the trailing area

✅ **Do:** Keep the same kind of trailing content for all the questions of a list  
❌ **Don't:** Show trailing content on some questions only

✅ **Do:** Leave a clear separation before the Expanding indicator  
❌ **Don't:** Let trailing content be mistaken for the expand and collapse control

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

## Label bold — do & don't

✅ **Do:** Use the bold label when questions must be scanned quickly  
❌ **Don't:** Make some questions bold and others regular in the same list

✅ **Do:** Write each question as users would ask it, in plain language  
❌ **Don't:** Use internal jargon or a vague label such as "More information"

✅ **Do:** Keep questions short and specific  
❌ **Don't:** Write a paragraph as the question

✅ **Do:** Keep the same grammatical form for all the questions of a list  
❌ **Don't:** Mix questions, statements and keywords in the same list

✅ **Do:** Let the question carry the meaning without relying on its weight  
❌ **Don't:** Rely on bold alone to show which question matters most

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
