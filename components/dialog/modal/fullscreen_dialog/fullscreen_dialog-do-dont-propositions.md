# Fullscreen dialog — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([fullscreen_dialog.md](fullscreen_dialog.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Complex tasks that need more space than a modal dialog can offer

✅ Forms with several fields that require keyboard input

✅ Multi-step flows, such as creating an account or setting up a service

✅ Tasks whose changes are not saved instantly and need an explicit confirmation

✅ Content-heavy screens, such as a long selection list or detailed settings

✅ Small viewports, where a modal dialog would leave too little room for its content

✅ Tasks that may open a modal dialog on top, for example to confirm discarding changes

✅ Focused work that benefits from hiding the underlying page entirely

✅ Flows that must end with a clear action, such as Send, Create or Save

✅ Tasks that stay temporary: content that deserves its own URL belongs on a page

## Sticky action — do & don't

✅ **Do:** Keep actions sticky when the content is long enough to scroll  
❌ **Don't:** Make users scroll through a long form to find the main action

✅ **Do:** Let actions follow the content when the dialog holds little content  
❌ **Don't:** Pin actions at the bottom of a dialog that never scrolls

✅ **Do:** Keep the same logical action order whether the actions are sticky or not  
❌ **Don't:** Change which action is primary when the footer becomes sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content or the focused field  
❌ **Don't:** Let the sticky footer cover content that cannot be scrolled into view

## Other boolean options — do & don't

✅ **Do:** Keep the Close button so users can always leave the dialog  
❌ **Don't:** Hide the Close button and leave no visible way to exit a full-screen surface

✅ **Do:** Use Previous to go back one step of a multi-step flow without closing the dialog  
❌ **Don't:** Use Previous to close the dialog or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the dialog

✅ **Do:** Use the Slot for forms and custom content, laid out on the page grid  
❌ **Don't:** Recreate a whole application or unrelated pages inside the dialog

## Action number — do & don't

✅ **Do:** Use a single action when there is one clear thing to do, and limit the dialog to three actions  
❌ **Don't:** Fill the dialog with choices that compete with the task

✅ **Do:** Give the Primary action to the outcome that completes the task  
❌ **Don't:** Style two actions as Primary in the same dialog

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary on every breakpoint  
❌ **Don't:** Let the visual order on desktop change the DOM or focus order

✅ **Do:** Write a confirming label that says what happens next, such as "Send" or "Create account"  
❌ **Don't:** Use vague labels such as "Done", "OK" or "Close"

## Examples of uses — do & don't

✅ **Do:** Use the Negative example, with a Negative action appearance, for destructive or irreversible actions  
❌ **Don't:** Use Negative styling for a routine, reversible choice

✅ **Do:** Use the Positive example to confirm that a long task or transaction succeeded  
❌ **Don't:** Open a full-screen Positive dialog for minor feedback a toast could give

✅ **Do:** Say what will happen and whether it can be undone before a destructive action  
❌ **Don't:** Ask "Are you sure?" without naming the consequence

✅ **Do:** Pair the status icon with a clear title and description  
❌ **Don't:** Rely on colour or the icon alone to convey the status

✅ **Do:** Give a way out of a negative dialog, such as Cancel or a recovery action  
❌ **Don't:** Leave users in an error dialog with no next step

## Responsive behaviour — do & don't

✅ **Do:** Treat the dialog as a full-page layout that fills the viewport at every breakpoint  
❌ **Don't:** Add margins, a backdrop or a fixed width around the dialog

✅ **Do:** Lay the content out on the standard page grid for each breakpoint  
❌ **Don't:** Stretch text and fields across the whole width of a large screen

✅ **Do:** Keep the same maximum content and text widths as on any other page  
❌ **Don't:** Invent dialog-specific widths that differ from the rest of the product

✅ **Do:** Let long content scroll vertically inside the dialog  
❌ **Don't:** Let content scroll horizontally or overflow the viewport

✅ **Do:** Check the layout at every breakpoint, including the switch from a Modal dialog  
❌ **Don't:** Design the dialog for one screen size only

## ℹ️ Additional technical information — do & don't

✅ **Do:** Always display a title that names the task  
❌ **Don't:** Hide the title, even when the content is self-explanatory

✅ **Do:** Keep the same task, content hierarchy and interaction logic when a Modal dialog becomes fullscreen  
❌ **Don't:** Change the content or the actions when the layout changes across breakpoints

✅ **Do:** Ask for confirmation in a Modal dialog before discarding unsaved changes  
❌ **Don't:** Close the dialog and lose what users entered without warning

✅ **Do:** Adapt an action's appearance, such as Negative, when its meaning requires it, and keep the Tertiary action a link  
❌ **Don't:** Turn the Tertiary action into a button

✅ **Do:** Open the dialog without animation, as specified  
❌ **Don't:** Add a slide or fade transition to the fullscreen dialog
