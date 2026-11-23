# Toast — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([toast.md](toast.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Confirming that an action succeeded, such as changes saved or a message sent

✅ Brief feedback on a background process, such as an upload or a sync

✅ Offering a single quick follow-up action, such as Undo, Retry or View

✅ Reporting a non-blocking error users can recover from without leaving the page

✅ Short system updates, such as connection restored or a new version available

✅ Showing that an operation is still in progress with the Loading state

✅ Warnings that need awareness but do not block the current task

✅ Short, non-critical feedback of one or two lines that users can read at a glance

✅ Confirming an item was added, moved or removed, with an image for recognition

✅ Messages whose information stays available elsewhere after the toast disappears

## Alignment — do & don't

✅ **Do:** Use Top alignment when the toast has a label and a description or wraps onto several lines  
❌ **Don't:** Center the icon and actions next to a long multiline message

✅ **Do:** Use Center alignment for short, single-line messages to keep the toast compact  
❌ **Don't:** Use Top alignment on a single-line toast, where it looks unbalanced

✅ **Do:** Keep the leading container, action and close button aligned with the first line of a multiline message  
❌ **Don't:** Let the close button drift to the vertical middle of a tall toast

✅ **Do:** Apply the same alignment to toasts with the same content structure  
❌ **Don't:** Mix alignments between similar toasts in the same product

✅ **Do:** Check the alignment again when translations or user zoom make the text wrap  
❌ **Don't:** Assume a message stays on one line in every language and text size

## Action layout — do & don't

✅ **Do:** Use None for confirmations that need no follow-up  
❌ **Don't:** Add an action only to make the toast look more useful

✅ **Do:** Use Trailing for a short action next to a single-line message on wider layouts  
❌ **Don't:** Place a long action label in the trailing position where it squeezes the message

✅ **Do:** Use Bottom on mobile, with multiline messages or with longer action labels  
❌ **Don't:** Keep a trailing action on a narrow screen when the message already wraps

✅ **Do:** Limit the toast to one short action whose label names the result, such as Undo, Retry or View order  
❌ **Don't:** Offer several actions, a vague label such as Learn more, or a decision that needs careful thought

✅ **Do:** Use a button with the link style for in-app actions and a real link for navigation  
❌ **Don't:** Use a link element to trigger an action that does not navigate

## Status — do & don't

✅ **Do:** Match the status to the real nature of the message: Positive for success, Negative for errors  
❌ **Don't:** Use Negative or Warning to draw attention to a neutral message

✅ **Do:** Use Neutral for contextual information that carries no system result  
❌ **Don't:** Use a functional status for tips or decorative messages

✅ **Do:** Keep the dedicated status icon with every functional status  
❌ **Don't:** Rely on colour alone to tell success, warning and error apart

✅ **Do:** State the result in the label so the status is clear without the icon  
❌ **Don't:** Write a vague label such as “Done” or “Error” that depends on the colour to be understood

✅ **Do:** Use a persistent component, such as an alert message, for critical errors that block the task  
❌ **Don't:** Report a blocking error only in a toast that may disappear

## Close button — do & don't

✅ **Do:** Add a close button when the toast contains an action or needs more reading time  
❌ **Don't:** Auto-dismiss a toast that contains an action before users can reach it

✅ **Do:** Let short confirmations disappear automatically without a close button  
❌ **Don't:** Keep a simple “Changes saved” message on screen until users close it

✅ **Do:** Adapt the display duration to the length of the message so users have time to read it  
❌ **Don't:** Use the same short duration for one-line and three-line messages

✅ **Do:** Keep warnings and errors visible until users dismiss them  
❌ **Don't:** Auto-dismiss an error, a warning or information that is not available anywhere else

✅ **Do:** Give the close button a descriptive accessible name, such as “Dismiss notification”  
❌ **Don't:** Leave the close button announced by the name of its icon

## Rounded corner — do & don't

✅ **Do:** Set the corner style once for the whole product or service  
❌ **Don't:** Mix square and rounded toasts within the same product

✅ **Do:** Use square corners as the default Orange style  
❌ **Don't:** Switch to rounded corners on a single screen for decoration

✅ **Do:** Use rounded corners when the product aims for a softer, more approachable feel  
❌ **Don't:** Enable rounded corners on brand themes where the option is unavailable

✅ **Do:** Keep the toast corner style consistent with other components in the product  
❌ **Don't:** Combine a rounded toast with square buttons, alerts and inputs

✅ **Do:** Check the availability of rounded corners for your brand theme first  
❌ **Don't:** Assume the Figma property can be set freely for each toast

## Description — do & don't

✅ **Do:** Add a description only when the label cannot carry the whole message  
❌ **Don't:** Repeat the label in the description with different words

✅ **Do:** Keep the description to one or two short sentences  
❌ **Don't:** Put long explanations or instructions in a toast

✅ **Do:** Use the description to say what users can do next  
❌ **Don't:** Describe a problem without giving a way forward

✅ **Do:** Use plain, friendly and service-oriented language  
❌ **Don't:** Use technical jargon, error codes or internal terms

✅ **Do:** Move detailed content to a page, a modal or a persistent message  
❌ **Don't:** Rely on a temporary toast to deliver information users need to keep

## Leading — do & don't

✅ **Do:** Use a leading icon on a Neutral toast when it helps users recognise the subject  
❌ **Don't:** Add a decorative icon that has no link with the message

✅ **Do:** Remove the leading content when the message is self-explanatory  
❌ **Don't:** Fill every Neutral toast with an icon by habit

✅ **Do:** Keep the dedicated status icon on functional toasts  
❌ **Don't:** Remove or replace the status icon of a Negative, Positive, Info or Warning toast

✅ **Do:** Choose icons from the Solaris library that match the content  
❌ **Don't:** Use an icon that suggests a status the toast does not have

✅ **Do:** Hide decorative leading content from assistive technologies  
❌ **Don't:** Convey essential information only through the leading icon

## Leading container type — do & don't

✅ **Do:** Use Icon to represent an action, a status or a category  
❌ **Don't:** Use an image where a simple icon is enough

✅ **Do:** Use Image when users recognise the content faster by seeing it, such as a product  
❌ **Don't:** Use an image that is purely decorative and distracts from the message

✅ **Do:** Keep the message understandable when the image fails to load  
❌ **Don't:** Rely on the image to carry the meaning of the toast

✅ **Do:** Use the same leading container type for the same kind of message  
❌ **Don't:** Alternate between icons and images for similar notifications

✅ **Do:** Use the dedicated status icon for functional toasts  
❌ **Don't:** Replace a functional status icon with an image

## Image size — do & don't

✅ **Do:** Use Medium as the default image size  
❌ **Don't:** Change the image size from one toast to the next without a reason

✅ **Do:** Use Small for compact or single-line toasts  
❌ **Don't:** Use Large in a single-line toast, where it makes the toast unnecessarily tall

✅ **Do:** Use Large when details of the image must stay recognisable  
❌ **Don't:** Use Small for an image users need to identify precisely

✅ **Do:** Keep the same image size for similar use cases  
❌ **Don't:** Let the image compete with the text for attention

✅ **Do:** Check that the text stays easy to scan next to the image  
❌ **Don't:** Use Large in very compact layouts where it squeezes the message

## Rounded corner Image — do & don't

✅ **Do:** Keep the image corner style consistent with images elsewhere in the product  
❌ **Don't:** Mix square and rounded images in toasts of the same product

✅ **Do:** Use square corners for images in products that follow the square Orange style  
❌ **Don't:** Round the image only to make a single toast stand out

✅ **Do:** Use rounded image corners together with a rounded visual language  
❌ **Don't:** Combine sharply square images with a fully rounded interface

✅ **Do:** Choose the corner style according to the type of content shown  
❌ **Don't:** Crop important parts of the image with the rounded corners

✅ **Do:** Decide the image corner style once and apply it to every toast  
❌ **Don't:** Leave the choice to each screen or each team

## Multiline and responsiveness — do & don't

✅ **Do:** Let the toast grow vertically when the text wraps  
❌ **Don't:** Truncate the message with an ellipsis

✅ **Do:** Keep the message to one or two lines where possible, three at most  
❌ **Don't:** Write messages so long that the toast covers the content behind it

✅ **Do:** Let text and icons scale with user zoom  
❌ **Don't:** Set a fixed height or width that clips the content when zoomed

✅ **Do:** Keep the minimum interactive area when the toast contains an action or a close button  
❌ **Don't:** Shrink the action or close button below the minimum interactive area

✅ **Do:** Test the toast at 200% text size and at a 320 px viewport width  
❌ **Don't:** Assume the layout holds without checking zoom and reflow

## Rich text — do & don't

✅ **Do:** Use strong text sparingly to highlight one key piece of information  
❌ **Don't:** Bold several parts of the message or the whole sentence

✅ **Do:** Use the Label/Medium/Strong token for strong text  
❌ **Don't:** Apply custom font weights or other text styles

✅ **Do:** Keep underlined text for hyperlinks only  
❌ **Don't:** Underline words for emphasis

✅ **Do:** Use the Label/Medium/Underline reference when a hyperlink is needed in the content  
❌ **Don't:** Style a hyperlink with colour alone

✅ **Do:** Prefer the action slot for the main follow-up action  
❌ **Don't:** Add several inline links to a temporary message

## Horizontal responsive behaviour — do & don't

✅ **Do:** Let the toast width follow the breakpoint rules: margins on 2xs and xs, grid columns from sm  
❌ **Don't:** Set a fixed pixel width that ignores the breakpoints

✅ **Do:** Keep 8 px margins on both sides on the smallest screens  
❌ **Don't:** Let the toast touch the edges of the screen

✅ **Do:** Reduce the number of columns as the viewport grows so the line length stays readable  
❌ **Don't:** Stretch the toast across the full width of a desktop screen

✅ **Do:** Align the toast edges with the grid columns from sm onwards  
❌ **Don't:** Position the toast off the grid on tablet and desktop

✅ **Do:** Check the toast at every breakpoint, including the transitions between them  
❌ **Don't:** Design the toast for one screen size only

## Placement — do & don't

✅ **Do:** Use one placement consistently throughout the product  
❌ **Don't:** Move toasts between corners from one screen to the next

✅ **Do:** Place the toast close to where the action happened when that helps users notice it  
❌ **Don't:** Show feedback far from the area users are looking at

✅ **Do:** Keep the specified spacing from the viewport edges and from persistent elements  
❌ **Don't:** Cover navigation bars, floating buttons or sticky elements with a toast

✅ **Do:** Place the toast above bottom navigation or other persistent elements on mobile  
❌ **Don't:** Hide the bottom navigation behind the toast

✅ **Do:** Choose another position when the area already holds a chat widget or a help button  
❌ **Don't:** Stack a toast on top of another floating element

## Interaction and stacking — do & don't

✅ **Do:** Display one toast at a time and queue the others  
❌ **Don't:** Show several toasts at once for routine feedback

✅ **Do:** Announce the toast as a status message and leave keyboard focus where it is  
❌ **Don't:** Move focus to a toast when it appears, or overlap its entrance with the exit of the previous one

✅ **Do:** Limit a necessary stack to three toasts with an 8 px gap  
❌ **Don't:** Mix auto-dismissing and persistent toasts in one stack, or let it cover the page content

✅ **Do:** Group repeated confirmations into a single message  
❌ **Don't:** Display the same message several times in a row

✅ **Do:** Prefer a single visible toast on mobile  
❌ **Don't:** Stack toasts on a small screen where they hide the content

## Priority queue — do & don't

✅ **Do:** Display higher-priority toasts first, starting with actionable and Negative ones  
❌ **Don't:** Make an error wait behind a series of routine confirmations

✅ **Do:** Show toasts of the same priority in the order they were triggered  
❌ **Don't:** Reorder same-priority messages arbitrarily

✅ **Do:** Check that a queued message is still relevant before displaying it  
❌ **Don't:** Display an outdated confirmation after the system state has changed

✅ **Do:** Keep actionable toasts visible until users act on them or dismiss them  
❌ **Don't:** Auto-dismiss an actionable toast to make room for the next one

✅ **Do:** Discard low-priority Neutral messages that are no longer useful  
❌ **Don't:** Interrupt an important or actionable toast with a lower-priority one
