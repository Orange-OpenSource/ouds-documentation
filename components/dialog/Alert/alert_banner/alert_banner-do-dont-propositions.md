# Alert banner — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([alert_banner.md](alert_banner.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ System-wide issues, such as a lost internet connection or a service outage

✅ Confirming that a global issue is resolved, such as a restored connection

✅ Announcing scheduled maintenance or an upcoming service disruption

✅ Account-level notices, such as an approaching deadline, that apply across several screens

✅ Platform or service updates that do not require immediate action

✅ Persistent messages that must stay visible until the condition is resolved

✅ Promoting a service, an offer or a new feature across the experience

✅ General guidance, such as onboarding tips or account suggestions

✅ Global messages with a single follow-up action, such as View details

✅ The single most important global message: banners are used sparingly, one at a time

## Layout — do & don't

✅ **Do:** Use the Start layout on mobile, tablet and small desktop screens, aligned with the page grid  
❌ **Don't:** Use the Center layout on narrow screens where the content cannot stay on one line

✅ **Do:** Use the Center layout for a short message with one optional action on wide desktop screens  
❌ **Don't:** Use the Center layout for a message that needs a description or a close button

✅ **Do:** Set a maximum content width for the Center layout at each breakpoint  
❌ **Don't:** Let the text or the action touch or overflow the banner edges

✅ **Do:** Switch to the Start layout when the content becomes longer or needs more flexible actions  
❌ **Don't:** Reduce the text size or truncate the message to keep the Center layout

✅ **Do:** Keep the same layout for the same banner across the pages of a journey  
❌ **Don't:** Mix Start and Center layouts for similar messages at the same breakpoint

## Alignment — do & don't

✅ **Do:** Use Top alignment on mobile and for banners with long or multiline content  
❌ **Don't:** Centre the icon and the action next to a message that spans several lines

✅ **Do:** Use Center alignment for compact banners and short single-line messages on desktop  
❌ **Don't:** Use Top alignment on a single-line banner, where it looks unbalanced

✅ **Do:** Keep the icon and the action aligned with the first line of a multiline message  
❌ **Don't:** Let the close button drift to the vertical middle of a tall banner

✅ **Do:** Apply the same alignment to banners with the same content structure  
❌ **Don't:** Mix alignments between similar banners in the same product

✅ **Do:** Check the alignment again when translated or zoomed text wraps onto more lines  
❌ **Don't:** Assume a message that fits on one line in one language fits in every language

## Status — do & don't

✅ **Do:** Match the status to the meaning of the message: Negative, Positive, Info or Warning  
❌ **Don't:** Choose a status for its colour or to draw more attention to the banner

✅ **Do:** Use Negative for critical system issues, such as an outage or a failed connection  
❌ **Don't:** Use a Negative banner for a field error or a problem limited to one page section

✅ **Do:** Use Positive to confirm that a global issue has been resolved  
❌ **Don't:** Use a Positive banner for a minor confirmation related to a single action

✅ **Do:** Use Neutral or Accent for guidance, promotions and featured content  
❌ **Don't:** Use an Accent banner for an urgent message or a system issue

✅ **Do:** Announce urgent Negative and Warning banners as alerts and other banners as polite status messages  
❌ **Don't:** Use an assertive alert for promotional or informational banners, or show a functional banner without a real system condition

## Action layout — do & don't

✅ **Do:** Use None when the banner only informs users about the current state  
❌ **Don't:** Add an action that does not help users understand or resolve the situation

✅ **Do:** Use Trailing for short messages and short actions that stay on a single line  
❌ **Don't:** Keep a trailing action when the message or the action wraps onto several lines

✅ **Do:** Use Bottom on mobile and for multiline messages or long action labels  
❌ **Don't:** Squeeze a long action label next to the message on a narrow screen

✅ **Do:** Use an <a> element for navigation and a <button> with the link style for in-app actions  
❌ **Don't:** Let the visual link style decide which semantic element is used

✅ **Do:** Write an action label that describes the result, such as View maintenance information  
❌ **Don't:** Use a vague label such as OK, Click here or Learn more

## Close button — do & don't

✅ **Do:** Add a close button when the message can be safely removed after it has been read  
❌ **Don't:** Let users dismiss a banner that reports an active system issue

✅ **Do:** Keep high-priority banners visible until the underlying condition is resolved  
❌ **Don't:** Hide a No internet connection banner before connectivity is restored

✅ **Do:** Give the close button a clear accessible name, such as Dismiss banner  
❌ **Don't:** Expose a technical icon name such as cross as the accessible name

✅ **Do:** Move focus to a logical element that remains on the page after dismissal  
❌ **Don't:** Let focus return to the top of the document when the banner closes

✅ **Do:** Keep a dismissed banner hidden for the rest of the journey unless its content changes  
❌ **Don't:** Show the same banner again right after the user dismissed it

## Icon — do & don't

✅ **Do:** Always show the dedicated functional icon on Negative, Positive, Info and Warning banners  
❌ **Don't:** Remove or replace the functional icon of a banner that reports a system status

✅ **Do:** Add an icon to a Neutral or Accent banner when it helps users grasp the message faster  
❌ **Don't:** Add an icon to a Neutral or Accent banner only to fill the space

✅ **Do:** Choose an icon that matches the subject of the message  
❌ **Don't:** Use a status icon on a non-functional banner, where it implies a system state

✅ **Do:** Hide decorative icons from assistive technologies  
❌ **Don't:** Let screen readers announce icon names such as heart or gift

✅ **Do:** Repeat the meaning of the icon in the text of the banner  
❌ **Don't:** Rely on the icon alone to communicate the status

## Description — do & don't

✅ **Do:** Add a description only when users need more context about the issue, its impact or the next step  
❌ **Don't:** Repeat the label in the description

✅ **Do:** Keep the description to one or two short sentences  
❌ **Don't:** Write long explanations inside the banner

✅ **Do:** Send users to another page, view or modal when a detailed explanation is needed  
❌ **Don't:** Stack several paragraphs or lists in a banner

✅ **Do:** Tell users what they can do next when the banner requires an action  
❌ **Don't:** Describe a problem without any guidance when a recovery step exists

✅ **Do:** Use plain, service-oriented language and say “we” for system faults, such as “We’ve lost the connection”  
❌ **Don't:** Blame users or use jargon, error codes or technical terms they do not know

## Placement and Interaction — do & don't

✅ **Do:** Place the banner directly below the header or main navigation, above the page content  
❌ **Don't:** Place the banner in the middle of the page or inside a single section

✅ **Do:** Keep the banner in the page flow so that it pushes the content down  
❌ **Don't:** Overlay the banner on navigation, content or interactive elements

✅ **Do:** Let the banner scroll with the page by default  
❌ **Don't:** Fix the banner over the content without a clear need

✅ **Do:** Show one banner at a time, the highest-priority one, with its content aligned with the page grid  
❌ **Don't:** Stack several banners above the page content

✅ **Do:** Use the maximum-width behaviour when the rest of the product follows a centred layout  
❌ **Don't:** Let the banner keep expanding beyond 1920 px in a product with a maximum width

## Multiline and responsiveness — do & don't

✅ **Do:** Let the banner grow in height so the text can wrap onto several lines  
❌ **Don't:** Truncate the message or fix the height of the banner

✅ **Do:** Apply the max-width to the text while the background fills the available width  
❌ **Don't:** Stretch a line of text across the full width of a large screen

✅ **Do:** Let text and icons scale proportionally with user zoom  
❌ **Don't:** Block text resizing or keep icons at a fixed size

✅ **Do:** Keep the minimum interactive area when the banner contains an action or a close button  
❌ **Don't:** Let the action or the close button shrink below the minimum area at zoom out

✅ **Do:** Check the banner at 200% zoom and at a 320 px wide viewport  
❌ **Don't:** Assume a layout that works at the default size works at every zoom level

## Rich text — do & don't

✅ **Do:** Use strong text sparingly to highlight one key piece of information, such as a date or an amount  
❌ **Don't:** Bold several fragments or the whole message

✅ **Do:** Use the Label/Medium/Strong token in the Start layout and Label/Large/Strong in the Center layout  
❌ **Don't:** Apply other text styles or custom font weights

✅ **Do:** Underline only real hyperlinks, with the dedicated underline typographic reference  
❌ **Don't:** Underline text for emphasis

✅ **Do:** Add a separate action when a more prominent or independent next step is needed  
❌ **Don't:** Give an inline link and the separate action the same destination

✅ **Do:** Write a clear message first, then decide whether rich text helps scanning  
❌ **Don't:** Use rich text to compensate for unclear writing
