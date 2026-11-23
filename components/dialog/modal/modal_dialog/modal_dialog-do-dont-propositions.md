# Modal dialog — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([modal_dialog.md](modal_dialog.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Confirming a destructive or irreversible action, with a clear description of its consequences

✅ Asking for a decision that must be made before the task can continue

✅ Requesting critical information the system needs before it can go on

✅ Reporting a blocking error that users need to acknowledge or resolve

✅ Urgent information about the user's current work that requires acknowledgement

✅ Confirming an important outcome, such as a completed payment or subscription

✅ Warning about unsaved changes before users leave a page or close a flow

✅ A short, single task that benefits from keeping the page context behind it

✅ Breaking a focused task into a few short steps, using the Previous link to go back

✅ Critical moments only: non-critical feedback belongs in a toast or an inline alert

## Size — do & don't

✅ **Do:** Choose the size from the amount of content: Default for most dialogs, Small for brief text  
❌ **Don't:** Pick Small for content that needs room to be read comfortably

✅ **Do:** Use Small for short confirmations and simple, focused choices  
❌ **Don't:** Use Default for a one-line message that leaves the dialog mostly empty

✅ **Do:** Keep the same size for dialogs of the same kind across a journey  
❌ **Don't:** Change size between two steps of the same flow

✅ **Do:** Let the size set typography and spacing together  
❌ **Don't:** Override text styles or spacing to squeeze more content into a size

✅ **Do:** Move to the Default size, or to a Fullscreen dialog, when content no longer fits  
❌ **Don't:** Let content scroll horizontally inside the dialog

## Fixed height — do & don't

✅ **Do:** Let the dialog hug its content when the content is short  
❌ **Don't:** Force the maximum height on a dialog that holds two lines of text

✅ **Do:** Use a fixed height for multi-step flows so the dialog does not jump between steps  
❌ **Don't:** Let the dialog resize at every step of a flow

✅ **Do:** Keep vertical scrolling to a minimum by keeping the content concise  
❌ **Don't:** Put a long page of content into a dialog and rely on scrolling

✅ **Do:** Keep the title and the actions in place while the content scrolls vertically  
❌ **Don't:** Scroll the whole dialog, title included, out of view

✅ **Do:** Show that more content is available below when the content scrolls  
❌ **Don't:** Cut content off with no sign that it continues

## Sticky action — do & don't

✅ **Do:** Keep actions sticky when the content is long enough to scroll  
❌ **Don't:** Make users scroll to the end of long content to find the main action

✅ **Do:** Let actions follow the content when the dialog is short  
❌ **Don't:** Pin actions at the bottom of a dialog that never scrolls

✅ **Do:** Keep the same action order whether the actions are sticky or not  
❌ **Don't:** Reorder actions when switching between sticky and non-sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content  
❌ **Don't:** Let the action area cover content that cannot be scrolled into view

## Rounded corner — do & don't

✅ **Do:** Apply the same corner setting to every dialog in a product or service  
❌ **Don't:** Mix square and rounded dialogs within the same product

✅ **Do:** Keep square corners as the default Orange style  
❌ **Don't:** Switch to rounded corners for a single screen or campaign

✅ **Do:** Use rounded corners when the whole product adopts the softer, more tactile style  
❌ **Don't:** Round the dialog while its buttons and inputs stay square

✅ **Do:** Check that the brand theme supports rounded corners before using them  
❌ **Don't:** Enable rounded corners on Sosh or Wireframe themes

✅ **Do:** Decide the corner style once, at product level  
❌ **Don't:** Leave the choice to each designer or each screen

## Other boolean options — do & don't

✅ **Do:** Keep the Close button whenever users may want to leave without choosing an action  
❌ **Don't:** Hide the Close button and leave no visible way to exit

✅ **Do:** Use Previous in multi-step flows to go back one step without closing the dialog  
❌ **Don't:** Use Previous to close the dialog or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the dialog

✅ **Do:** Use the Slot for content the standard structure cannot hold, following spacing and responsive rules  
❌ **Don't:** Fill the Slot with a full page of unrelated content

## Action number — do & don't

✅ **Do:** Use a single action when there is one clear thing to do, and limit the dialog to three actions  
❌ **Don't:** Fill the dialog with choices that turn it into a complex interaction

✅ **Do:** Give the Primary action to the preferred outcome and echo the title in its label  
❌ **Don't:** Style two actions as Primary in the same dialog

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary on every breakpoint  
❌ **Don't:** Let the visual order on desktop change the DOM or focus order

✅ **Do:** Write action labels with active verbs that name the outcome, such as "Delete file"  
❌ **Don't:** Use vague or passive labels such as "OK" or "Done"

## Backdrop blurred — do & don't

✅ **Do:** Use the blurred backdrop when a busy page behind the dialog distracts from it  
❌ **Don't:** Add blur purely as decoration

✅ **Do:** Use the plain backdrop when the page behind gives useful context  
❌ **Don't:** Blur the page when users need to refer to what is behind the dialog

✅ **Do:** Keep the same backdrop setting for similar dialogs in a product  
❌ **Don't:** Alternate blurred and plain backdrops at random

✅ **Do:** Keep the 68% black overlay in both settings  
❌ **Don't:** Lighten or tint the overlay to match a campaign

✅ **Do:** Check that blur does not slow the experience on low-end devices  
❌ **Don't:** Trade perceived performance for a visual effect

## Examples of uses — do & don't

✅ **Do:** Use the Negative example, with a Negative action appearance, for destructive or irreversible actions  
❌ **Don't:** Use Negative styling for a routine, reversible choice

✅ **Do:** Use the Positive example to confirm that an action or transaction succeeded  
❌ **Don't:** Open a Positive dialog for minor feedback a toast could give

✅ **Do:** Say what will happen and whether it can be undone before a destructive action  
❌ **Don't:** Ask "Are you sure?" without naming the consequence

✅ **Do:** Pair the status icon with a clear title and description  
❌ **Don't:** Rely on colour or the icon alone to convey the status

✅ **Do:** Give a way out of a negative dialog, such as Cancel or a recovery action  
❌ **Don't:** Leave users in an error dialog with no next step

## Responsive behaviour — do & don't

✅ **Do:** Let the dialog width follow the column spans defined for each breakpoint and size  
❌ **Don't:** Set a fixed pixel width that ignores the grid

✅ **Do:** Keep the 16 px margin on 2xs and xs screens  
❌ **Don't:** Let the dialog touch the edges of the viewport

✅ **Do:** Let the content area scroll when it exceeds the available height  
❌ **Don't:** Let the dialog grow taller than the viewport

✅ **Do:** Check both sizes at every breakpoint, including the transitions between them  
❌ **Don't:** Design the dialog for one screen size only

✅ **Do:** Keep the dialog within the height defined for its size and breakpoint  
❌ **Don't:** Stretch a Small dialog to the height of a Default one

## ℹ️ Additional technical information — do & don't

✅ **Do:** Always display a title that names the purpose of the dialog  
❌ **Don't:** Hide the title, even when the message is short

✅ **Do:** Use a static backdrop when closing by accident would lose data or progress  
❌ **Don't:** Let a click outside discard a form the user is filling in

✅ **Do:** Keep the same task, content hierarchy and interaction logic when the layout changes across breakpoints  
❌ **Don't:** Change the content or the actions when a modal becomes fullscreen

✅ **Do:** Show one dialog at a time and keep the Tertiary action a link  
❌ **Don't:** Open a dialog from another dialog, or turn the Tertiary action into a button

✅ **Do:** Remove the opening animation when the user prefers reduced motion  
❌ **Don't:** Play the slide-down animation regardless of user preferences
