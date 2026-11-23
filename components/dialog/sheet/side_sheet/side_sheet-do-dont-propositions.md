# Side sheet — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([side_sheet.md](side_sheet.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Secondary tasks that keep users on the page they are working on

✅ Filters and sorting options for a list or a set of results

✅ Details of an item selected in the page, such as an order or a contact

✅ Editing a small set of related fields without leaving the page

✅ Responsive navigation on small screens, anchored to the start edge

✅ A shopping cart or a summary that users open and close while browsing

✅ Supplementary information or help related to the current page

✅ Quick actions and contextual tools related to the page content

✅ Tasks where seeing part of the page behind helps users keep their bearings

✅ Short or medium tasks: decisions that must interrupt belong in a modal dialog, complex ones in a fullscreen dialog

## Size — do & don't

✅ **Do:** Choose the size from the amount of content: Default for detailed content, Small for a short summary or a few options  
❌ **Don't:** Pick Small for content that needs room to be read or edited comfortably

✅ **Do:** Keep enough of the page visible behind the sheet on tablet and desktop  
❌ **Don't:** Let the sheet cover so much of the page that users lose their context

✅ **Do:** Keep the same size for sheets of the same kind across a journey  
❌ **Don't:** Change size between two steps of the same flow

✅ **Do:** Let the size set typography and spacing together  
❌ **Don't:** Override text styles or spacing to squeeze more content into a size

✅ **Do:** Move to a Fullscreen dialog when the task needs the whole viewport  
❌ **Don't:** Let content scroll horizontally inside the sheet

## Placement — do & don't

✅ **Do:** Use End for details, filters, editing and supplementary information about the page  
❌ **Don't:** Open contextual details from the start edge, where users expect navigation

✅ **Do:** Use Start for navigation, tools or lists naturally tied to the start side of the page  
❌ **Don't:** Place the same kind of sheet on different edges from one page to the next

✅ **Do:** Follow the reading direction: in right-to-left layouts Start is the right edge  
❌ **Don't:** Hard-code left and right so the sheet ignores the direction of the interface

✅ **Do:** Keep the same placement across mobile, tablet and desktop  
❌ **Don't:** Move the sheet to another edge only to fit the available space

✅ **Do:** Wait for the Top and Bottom placements, still marked work in progress, before using them  
❌ **Don't:** Rebuild a top or bottom sheet from the side sheet component

## Sticky action — do & don't

✅ **Do:** Keep actions sticky when the content is long enough to scroll  
❌ **Don't:** Make users scroll through a long list of filters to find the main action

✅ **Do:** Let actions follow the content when the sheet holds little content  
❌ **Don't:** Pin actions at the bottom of a sheet that never scrolls

✅ **Do:** Keep the same logical action order whether the actions are sticky or not  
❌ **Don't:** Reorder actions when switching between sticky and non-sticky

✅ **Do:** Let the mobile layout follow the grid automatically  
❌ **Don't:** Offer users a control to switch the mobile layout

✅ **Do:** Check that sticky actions never hide the last lines of content or the focused element  
❌ **Don't:** Let the sticky footer cover content that cannot be scrolled into view

## Other boolean options — do & don't

✅ **Do:** Keep the Close button whenever users may want to leave without choosing an action  
❌ **Don't:** Hide the Close button and leave no visible way to close the sheet

✅ **Do:** Use Previous in multi-step flows to go back one step without closing the sheet, where the placement allows it  
❌ **Don't:** Use Previous to close the sheet or to leave the flow

✅ **Do:** Show either a Subtitle or a Previous link above the title  
❌ **Don't:** Display a Subtitle and a Previous link together

✅ **Do:** Use a Title icon to reinforce a status such as success, warning or deletion  
❌ **Don't:** Rely on the icon alone to convey the meaning of the sheet

✅ **Do:** Use the Slot for filters, forms and lists, following spacing and responsive rules  
❌ **Don't:** Recreate a whole page or an application inside the sheet

## Action number — do & don't

✅ **Do:** Use a single action when there is one clear thing to do, and limit the sheet to three actions  
❌ **Don't:** Fill the sheet with choices that turn it into a complex interaction

✅ **Do:** Give the Primary action to the preferred outcome, such as "Apply filters"  
❌ **Don't:** Style two actions as Primary in the same sheet

✅ **Do:** Use the Tertiary action, shown as a link, for a lower-emphasis option such as "Reset"  
❌ **Don't:** Replace the Tertiary link with a third button

✅ **Do:** Keep the focus and reading order Primary, Secondary, Tertiary whatever the alignment  
❌ **Don't:** Let the visual order change the DOM or focus order

✅ **Do:** Write action labels with active verbs that name the outcome  
❌ **Don't:** Use vague or passive labels such as "OK" or "Done"

## Backdrop blurred — do & don't

✅ **Do:** Use the blurred backdrop when a busy page beside the sheet distracts from it  
❌ **Don't:** Add blur purely as decoration

✅ **Do:** Use the plain backdrop when the page beside the sheet gives useful context  
❌ **Don't:** Blur the page when users need to refer to it while using the sheet

✅ **Do:** Keep the same backdrop setting for similar sheets in a product  
❌ **Don't:** Alternate blurred and plain backdrops at random

✅ **Do:** Keep the 68% black overlay in both settings  
❌ **Don't:** Lighten or tint the overlay to match a campaign

✅ **Do:** Check that blur does not slow the experience on low-end devices  
❌ **Don't:** Trade perceived performance for a visual effect

## Responsive behaviour — do & don't

✅ **Do:** Let the sheet width follow the column spans and maximum widths defined for each breakpoint and size  
❌ **Don't:** Set a fixed pixel width that ignores the grid

✅ **Do:** Add the grid margin on the side opposite to the anchored edge  
❌ **Don't:** Leave a gap between the sheet and the viewport edge it is anchored to

✅ **Do:** Let the sheet fill the full height of the viewport  
❌ **Don't:** Give the Default and Small sizes different heights

✅ **Do:** Let the content area scroll vertically when it exceeds the viewport height  
❌ **Don't:** Let the sheet itself scroll away from the viewport edge

✅ **Do:** Check both sizes at every breakpoint, including the transitions between them  
❌ **Don't:** Design the sheet for one screen size only

## ℹ️ Additional technical information — do & don't

✅ **Do:** Always display a title that names the purpose of the sheet  
❌ **Don't:** Hide the title, even when the content is self-explanatory

✅ **Do:** Use a static backdrop when closing by accident would lose data or progress  
❌ **Don't:** Let a click outside discard a form the user is filling in

✅ **Do:** Keep the same task, content hierarchy and interaction logic when the layout changes across breakpoints  
❌ **Don't:** Change the content or the actions when a sheet becomes fullscreen on mobile

✅ **Do:** Show one sheet at a time and keep the Tertiary action a link  
❌ **Don't:** Open a sheet from another sheet, or turn the Tertiary action into a button

✅ **Do:** Slide the sheet in from, and back to, the edge it is anchored to, and remove the animation for reduced motion  
❌ **Don't:** Animate the sheet from another direction or ignore the reduced-motion preference
