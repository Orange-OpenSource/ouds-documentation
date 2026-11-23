# Navigation card item — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([navigation_card_item.md](navigation_card_item.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

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

## Size — do & don't

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

## Alignment — do & don't

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

## Outlined — do & don't

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

## Rounded corner — do & don't

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

## Layout — do & don't

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

## Navigation indicator type — do & don't

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

## Choosing leading and trailing content — do & don't

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

## Leading — do & don't

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

## Leading container type — do & don't

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

## Trailing — do & don't

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

## Trailing container type — do & don't

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

## Divider — do & don't

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

## Helper text — do & don't

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

## Background — do & don't

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

## Label type — do & don't

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

## Overline — do & don't

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

## Slot (bottom) — do & don't

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

## Rich text — do & don't

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

## Multiline and responsiveness — do & don't

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

## Technical layout adjustments — do & don't

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
