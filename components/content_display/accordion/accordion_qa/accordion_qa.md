# Guideline

## Intro 👈🤖

An accordion Q&A is a question that expands and collapses to reveal its answer, so users open only the questions that matter to them.

---

## Definition

An Accordion Q&A is an interactive question-and-answer pattern used to reveal or hide an answer within the current context. Use it to organise frequently asked questions into a compact, scannable list where users can open only the information they need. The question acts as the accordion trigger and the related answer appears directly below it when expanded.

---

## Best for 👈🤔

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

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The full-width trigger row that reveals and hides the answer, with optional background | N |
| 2 | Leading container | An icon that helps users recognise the topic of the question | Y |
| 3 | Label | The question, regular or bold, with an optional overline | N |
| 4 | Description | Supporting text below the question | Y |
| 5 | Trailing container | Short secondary information related to the question | Y |
| 6 | Expanding indicator | Chevron or plus icon that shows whether the answer is visible, at the end or the start | N |
| 7 | Expanded container | The answer: Expanded text and/or the Expand slot | Y |
| 8 | Divider | Separates adjacent questions that share the same surface | Y |

---

## Expanded

**`False`** Use the collapsed state when the answer is hidden. Only the question remains visible, allowing users to scan the available Q&A topics quickly without displaying all answers at once.

**`True`** Use the expanded state when the answer related to the question is visible. The answer appears directly below the trigger and should clearly respond to the question above it.

---

## expanded_do_&_dont 👈🤔

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

---

## Expanded text

**`False`** No standard answer text is displayed in the expanded area.
Use this option when the answer is provided through Slot (Expand) or when no standard text content is required.

**`True`** Standard answer text is displayed below the Q&A when the item is expanded.

Use it for:
• Short answers.
• Explanations.
• Instructions.
• Conditions or requirements.
• Supporting information directly related to the question.

---

## expanded_text_do_&_dont 👈🤔

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

---

## Slot (Below text)

The Below text slot adds custom supporting content directly below the main text content.
Use it when additional information needs to remain closely associated with the Label, Description or other text content rather than span the complete trigger width.
The slot follows the position and alignment of the text container. Its exact placement may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom content area is displayed directly below the main text content.

⚠️ Keep Below text content concise.
⚠️ Use Slot (bottom) when the content requires a wider area outside the text container.
⚠️ Use Slot (Expand) when the content should only become visible after expansion.

---

## slot_below_text_do_&_dont 👈🤔

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

---

## Slot (Bottom)

The Bottom slot adds custom supporting content below the complete trigger content.
Use it when information needs to remain visible independently of the Expanded state and requires more space or flexibility than the standard text properties.
The slot is positioned at the bottom of the trigger area. Its exact width and alignment may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom supporting area is displayed below the main trigger content.

⚠️ Bottom slot content remains part of the trigger and should not behave as an independent action.
⚠️ Use Slot (below text) when the information needs to remain closely aligned with the main text content.
⚠️ Use Slot (Expand) when the content should only become visible after expansion.

---

## slot_bottom_do_&_dont 👈🤔

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

---

## Slot (Expand)

The Expand slot adds custom content inside the expanded area of the Accordion.
Use it when the revealed content requires a structure that cannot be represented clearly by standard Expanded text alone.
The slot is displayed only when the Accordion is expanded. Its exact placement inside the expanded area may vary depending on the Accordion component structure.

**`False`** No additional content is displayed below the main trigger content.

**`True`** A custom content area is displayed when the Accordion is expanded.

⚠️ Use Slot (below text) or Slot (bottom) when the content needs to remain visible in both collapsed and expanded states.

---

## slot_expand_do_&_dont 👈🤔

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

---

## Alternative icon

**`False`** Use the default chevron as the Expanding indicator. This is the recommended option for standard Q&A patterns and clearly communicates that the answer can be expanded or collapsed.

**`True`** Use the alternative expand / collapse icon when the product context requires the + pattern instead of a chevron.
The icon must communicate the same expanded state consistently across all items within the same accordion.

⚠️ Do not mix chevron and + indicators within the same accordion. Different indicators may suggest different behaviours even when the interaction is identical.

---

## alternative_icon_do_&_dont 👈🤔

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

---

## Reverse

**`False`** Use False as the standard layout.
The Expanding indicator is displayed at the logical end of the Q&A trigger, after the question and any optional Trailing content.

**`True`** Use Reverse when the Expanding indicator needs to appear at the logical start of the Q&A trigger. The indicator is positioned before the question.

⚠️ Reverse changes only the position of the Expanding indicator. It must not change the reading order, meaning or expand / collapse behaviour of the Q&A item.

---

## reverse_do_&_dont 👈🤔

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

---

## Leading

Leading displays an Icon before the Q&A. Use it when an Icon provides useful context or helps users identify the topic of the question more quickly.

**`False`** No Leading content is displayed. The main content starts at the default horizontal padding.

**`True`** A Leading Icon is displayed before the Q&A. Choose an Icon that clearly represents the topic.

⚠️ Avoid decorative Icons that do not help users understand the question.

---

## leading_do_&_dont 👈🤔

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

---

## Trailing

Trailing content displays short secondary information related to the Q&A before the Expanding indicator.
Use it sparingly when this information helps users understand the context of the question before opening the answer.

**`False`** No Trailing content is displayed. The main content can use the available width before the Expanding indicator.

**`True`** Trailing text is displayed after the question and before the Expanding indicator.

Use it for short contextual information such as:
• A value.
• A date.
• A short status.
• A compact qualifier.

⚠️ Do not place the answer itself in the Trailing area. Use Expanded text or Slot (Expand) instead.

---

## trailing_do_&_dont 👈🤔

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

---

## Trailing container type

**`Trailing Text`** Use Text to display a short value or secondary piece of information associated with the accordion section.

⚠️ Keep Trailing text concise. When the information requires a sentence or explanation, use the Description or place the information inside the expanded content instead.
⚠️ Trailing text must not look like a separate link or action.
⚠️ Keep trailing text to 1–2 words whenever possible. Longer content can reduce the space available for the primary label and cause excessive wrapping, especially when users zoom in or increase the text size.

**`Label`** Use Label for standard secondary information related to the Q&A. Use it when the trailing information is useful before expansion but does not require additional emphasis.

**`Label muted`** Use Label muted for low-priority contextual information that supports the question but is not essential before expansion. Suitable for information such as update dates, estimated durations or secondary metadata.

**`Label strong`** Use Label strong when the trailing information requires greater visual emphasis and is useful to notice before expanding the Q&A. Use it sparingly for important dates, values or statuses.

---

## trailing_container_type_do_&_dont 👈🤔

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

---

## Divider

**`False`** No Divider is displayed. Use this option when Q&A items are already clearly separated by spacing, Background or another visual treatment.

**`True`** A Divider is displayed between adjacent Q&A items. Use it when several questions share the same surface and additional visual separation improves scanning.

---

## divider_do_&_dont 👈🤔

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

---

## Background

**`False`** The Q&A item uses the surrounding container surface without an individual Background. Use this option for standard Q&A lists where spacing or Dividers already provide sufficient visual separation.

**`True`** A Background is applied to the complete Q&A item. Use it when individual questions require stronger visual grouping from the surrounding content. When expanded, the Background must visually contain both the question and its answer.

---

## background_do_&_dont 👈🤔

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

---

## Label bold

**`False`** Use the standard Label emphasis for most Q&As.

**`True`** Use Bold when stronger emphasis is required for the Q&A.

It may be appropriate when:
• Questions need stronger visual separation in a dense Q&A list.
• The Q&A is presented as a prominent content section.
• The established product pattern uses stronger question emphasis.

⚠️ Use the same Label emphasis consistently across equivalent Q&A items. Do not use Bold on an individual question only to suggest that it is more important than the others.

---

## label_bold_do_&_dont 👈🤔

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

---

## Overline

**`False`** No overline is displayed.

**`True`** A short contextual Label is displayed above the Q&A. Use an Overline when users need additional context to understand the category or scope of the question.

---

## overline_do_&_dont 👈🤔

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

---

## Description

**`False`** No supporting description is displayed.

**`True`** Supporting text is displayed below the Q&A. Use a Description when users need additional context to understand whether the question applies to their situation.
The Description should clarify the scope or conditions of the question rather than provide the answer itself.

---

## description_do_&_dont 👈🤔

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

---

## Rich text

Rich text should be used sparingly to improve scanning and highlight the most important information in the answer.
It must never compensate for unclear writing.

**Strong text**
• Strong text can be used sparingly in the Description or Expanded text to highlight key information, such as a status, date, amount or required step. Rich text must use the **Label/Medium/Strong** token only.
• No other text styles or custom font weights should be used.

**⚠️ Underline text and Hyperlinks**
• Underlined text must not be applied manually in the Description as users commonly interpret underlined content as a hyperlink.

---

## rich_text_do_&_dont 👈🤔

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

---

## Technical layout adjustments

Even though the component has a single structure in Figma for easier use by designers, its technical implementation may differ between Web and native environments to respect the layout conventions of each platform.
The Q&A trigger and its Expanded answer must remain visually aligned and clearly perceived as parts of the same question-and-answer item.

**Web (mobile, tablet, and desktop)**
The Q&A component is contained within the browser layout and follows the available container or grid width. Internal horizontal spacing follows the corresponding Web spacing tokens.

When expanded, the answer grows vertically below the trigger without changing the horizontal position of the Q&A item. The question and answer must remain aligned within the same content area.

**Native app (Android, iOS, Flutter)**
The Q&A component follows the screen and grid-margin conventions defined by the native product. Its horizontal spacing uses the corresponding native grid-margin tokens. When expanded, the answer grows vertically while maintaining the same relationship with its trigger.

---

## technical_layout_adjustments_do_&_dont 👈🤔

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

---

## Multiline and responsiveness

**Multiline**
Accordion Q&A supports multiline questions and answers. The number of lines is not limited. The question, Description, Trailing text and Expanded text must wrap when there is not enough horizontal space.

The Q&A item expands vertically to display its complete content. Do not use a fixed height or truncate information required to understand the question or answer.

The Expanding indicator must remain visible and must not overlap or become visually disconnected from the question.

**Max-width vs full-width**
Accordion Q&A does not have a default maximum width. Its width is defined by the parent container or Q&A layout.

The complete visible trigger remains one interactive target. The clickable area must not be limited to the question or Expanding indicator.

On wide layouts, the text area may use a product-defined maximum width to maintain comfortable reading.

The Expanded answer follows the same content alignment as its associated question.

The Expanding indicator remains positioned according to the Reverse property:
• At the logical end when Reverse is False.
• At the logical start when Reverse is True.

Optional Leading and Trailing content must not reduce the question to an unusable width.

**User zoom in/out**
Accordion Q&A does not have a default maximum width.

• Its width is defined by the parent container or Q&A layout.
• The complete visible trigger remains one interactive target. The clickable area must not be limited to the question or Expanding indicator.
• On wide layouts, the text area may use a product-defined maximum width to maintain comfortable reading.
• The Expanded answer follows the same content alignment as its associated question.
• The Expanding indicator remains positioned according to the Reverse property:
  • At the logical end when Reverse is False.
  • At the logical start when Reverse is True.
• Optional Leading and Trailing content must not reduce the question to an unusable width.

⚠️ Avoid creating excessive horizontal distance between the question and Expanding indicator. The complete trigger should remain visually understandable as one control.

---

## multiline_and_responsiveness_do_&_dont 👈🤔

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

---

## Animation

When enabled, the accordion uses a smooth expansion animation (entry and exit) rather than appearing with an immediate cut.
The accordion content expands from its collapsed state when opened, providing a clear visual transition that helps users understand the relationship between the trigger and the revealed content and establishes a stronger sense of spatial continuity.

---

## animation_do_&_dont 👈🤔

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

---

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

Concrete application to the Accordion:

**Pause, Stop, Hide**
The expansion and collapse of an accordion are triggered by the user and do not generally fall within the scope of this criterion.
However, if the expanded content contains moving, blinking, scrolling, or automatically updating content, that content must be evaluated separately.

**Reduced Motion**
The animated expansion and collapse of an accordion are not essential to its functionality or to understanding its content.
When Reduced Motion is enabled, the animated transition should therefore be removed or replaced with an instantaneous transition.
Default: animated expansion and collapse
Reduced Motion: instantaneous expansion and collapse

---

# Specs

## States

**`Enabled`** Enabled is the default state.
The Q&A can be expanded or collapsed. The complete trigger area acts as a single control for changing the Expanded state.

**`Hover`** Hover provides visual feedback when a pointer is positioned over the Q&A trigger.

**`Focus`** Focus indicates that the Q&A trigger is currently selected for keyboard interaction. Display one clear Focus treatment around the complete trigger area. When the expanded answer contains interactive elements, those elements receive their own Focus state independently from the Q&A trigger.

**`Pressed`** Pressed is a temporary state displayed while the Q&A trigger is being activated.

**`Disabled`** Use Disabled when the Q&A is temporarily unavailable or cannot currently be expanded. A Disabled trigger must not respond to activation.

**`Skeleton`** Use Skeleton while the Q&A or its required content is loading and the final information is not yet available. A Skeleton Q&A item acts as a placeholder and must not expand or collapse.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Accordion Q__NAME__A components must meet WCAG 2.2 Level AA standards so that all users can find the sections, know whether each one is open, and reach the revealed content using keyboard, pointer or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

An accordion hides content until users ask for it. Users who do not notice the control, or who cannot see the indicator change, may never find the content or may not know that it has appeared.

### Key Challenges

- The expanded or collapsed state is shown by an icon: it must also be exposed programmatically
- The whole trigger is one control: leading, trailing and slot content must not create extra, competing targets
- Collapsed content must be hidden from assistive technologies and from the focus order, not only visually
- Long labels, optional elements and zoom must not truncate the information users need to choose a section

### Critical Success Factors

1. Make each trigger a button inside a heading of the right level, with `aria-expanded` and `aria-controls` (WCAG 4.1.2)
2. Operate the trigger with Enter and Space, and keep Tab moving through triggers and visible content in page order
3. Keep collapsed content out of the accessibility tree and the tab sequence
4. Do not rely on the indicator or on colour alone to convey the state or the status of a section

---

## Design Requirements

### Structure & Labels

- [ ] **Trigger semantics**: A `button` in a heading element; the label, overline, extra label and description form its accessible name and description ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **State**: `aria-expanded` reflects the Expanded property; a Disabled item uses `aria-disabled` or the `disabled` attribute
- [ ] **Decorative visuals**: Decorative leading and trailing visuals are hidden from assistive technologies; informative ones have a text alternative

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border around the complete trigger ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Indicator contrast**: The Expanding indicator meets 3:1 against its background in every state
- [ ] **Target size**: The trigger is interactive across its full width and at least 24 × 24 CSS px

### Content

- [ ] **Descriptive labels**: ❌ "More" / ✅ "Delivery and returns" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Concise triggers**: Supporting text stays short so the announced button text remains easy to follow

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify each trigger announces its name, role and expanded or collapsed state, and that collapsed content is not read

### Keyboard Testing

- [ ] Tab reaches each trigger in order, Enter and Space toggle it, focus stays on the trigger after toggling
- [ ] Focus indicator visible (≥3:1 contrast) around the whole trigger; no focus lands inside collapsed content

### Functional Testing

- [ ] Verify the expansion animation is removed with Reduced Motion, and that nothing is truncated at 200% zoom and 320 px width

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **4.1.2 Name, Role, Value** (A): Triggers expose a name, the button role and the expanded state
- **2.1.1 Keyboard** (A): Every section can be opened and closed with the keyboard
- **1.3.1 Info and Relationships** (A): Triggers are headings, and each panel is associated with its trigger
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on the trigger
- **1.4.10 Reflow** (AA): Content wraps at 320 px without loss of information or two-dimensional scrolling

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Textual content](https://a11y-guidelines.orange.com/en/web/develop/textual-content/)
- [WAI-ARIA Authoring Practices - Accordion Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/)
- [WCAG 2.2 Understanding - Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Sep 1, 2026 | - | <ul><li>Documentation writing: Motion & Animation accessibility rules.</ul> | Maxime Tonnerre |
| Jul 28, 2026 | 1.0.0 | **Version 2.6 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Maxime Tonnerre |
