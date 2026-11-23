# Chat input — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([chat_input.md](chat_input.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Composing a message in a conversation

✅ Quick, iterative exchanges rather than multi-step data entry

✅ Support and customer-service conversations

✅ Messages that can run over several lines

✅ Conversations that need extra actions next to the send action

✅ The bottom of a conversation view, on mobile and on desktop

✅ Messages with a character limit that need live feedback

✅ Messaging between users or with a team inside a product

✅ Compact layouts where the label can be hidden without losing clarity

✅ Conversations that need supporting text or a helper link, such as writing guidelines

## Outlined — do & don't

✅ **Do:** Use Outlined False for a contained look in dense layouts or when the input needs more visibility  
❌ **Don't:** Place it on a surface where its fill no longer stands out

✅ **Do:** Use Outlined True when the input has to feel lightweight and unobtrusive  
❌ **Don't:** Use Outlined to signal that one input matters more than another

✅ **Do:** Keep the same style for every chat input of a product  
❌ **Don't:** Switch styles from one screen of a conversation to another

✅ **Do:** Check that Focus and Error stay visible in the style you choose  
❌ **Don't:** Rely on the border color alone to communicate an error

✅ **Do:** Choose the style according to the surface around the input  
❌ **Don't:** Combine both styles in the same view

## Rounded corner — do & don't

✅ **Do:** Apply one corner treatment to all the inputs of a product or service  
❌ **Don't:** Mix rounded and square inputs in the same product or service

✅ **Do:** Use rounded corners only with the themes that support them: Orange and Orange Compact  
❌ **Don't:** Expect rounded corners on the Sosh and Wireframe themes

✅ **Do:** Let the brand theme decide the corner treatment  
❌ **Don't:** Change the corners of one input to give it more emphasis

✅ **Do:** Keep the same corner treatment in every state of the input  
❌ **Don't:** Switch between rounded and square when the state changes

✅ **Do:** Use the same treatment as the other controls placed next to the input  
❌ **Don't:** Combine a rounded input with square controls in one row

## Input status — do & don't

✅ **Do:** Write clear, contextual placeholder text  
❌ **Don't:** Use the placeholder as the only explanation of what the input does

✅ **Do:** Replace the placeholder as soon as the user types  
❌ **Don't:** Keep the hint visible next to the entered text

✅ **Do:** Keep the placeholder short enough to fit on one line  
❌ **Don't:** Put long instructions in the placeholder

✅ **Do:** Prevent the submission of an empty message in the product logic  
❌ **Don't:** Let users send an empty message

✅ **Do:** Make entered text clearly different from placeholder text  
❌ **Don't:** Style entered text like a hint

## Error — do & don't

✅ **Do:** Show a clear error message below the input that explains the problem and how to fix it  
❌ **Don't:** Show only a red border

✅ **Do:** Combine color with the error icon and the error text  
❌ **Don't:** Rely on color alone to show the error

✅ **Do:** Keep the input editable so that users can correct their message  
❌ **Don't:** Clear what the user has typed

✅ **Do:** Replace the helper text with the error message  
❌ **Don't:** Show the helper text and the error message at the same time

✅ **Do:** Keep the helper link below the error message  
❌ **Don't:** Replace the helper link with the error message

## Other boolean options — do & don't

✅ **Do:** Use Scrolled when the text exceeds the maximum height of the input  
❌ **Don't:** Let the input grow beyond its maximum height

✅ **Do:** Keep the helper text short, ideally on a single line  
❌ **Don't:** Use helper text for long instructions

✅ **Do:** Offer a helper link when the helper text is not sufficient  
❌ **Don't:** Add several links below the input

✅ **Do:** Make sure that opening the help does not lose the message being written  
❌ **Don't:** Send the user away from a conversation with no way back

✅ **Do:** Show helper text or a helper link only when they help the conversation  
❌ **Don't:** Display them on every input by default

## Character counter — do & don't

✅ **Do:** Show the remaining characters in real time  
❌ **Don't:** Reveal the limit only after the user tries to send

✅ **Do:** Let users keep typing past the limit and show how far they have gone over  
❌ **Don't:** Block input when the limit is reached

✅ **Do:** Set the limit according to the constraints of the project  
❌ **Don't:** Copy a limit from another product without checking it

✅ **Do:** Use the "XXX characters maximum" text when the count cannot be added  
❌ **Don't:** Display a counter that does not update

✅ **Do:** Leave the error state as soon as the text is back within the limit  
❌ **Don't:** Keep the error displayed once the text fits

## Bottom actions — do & don't

✅ **Do:** Keep the send action identifiable and always visible  
❌ **Don't:** Hide the send action

✅ **Do:** Remove the actions that have no useful function in the conversation  
❌ **Don't:** Fill all the action places by default

✅ **Do:** Give every icon-only action an accessible name  
❌ **Don't:** Use ambiguous icons without a name

✅ **Do:** Use the slot of the bottom actions for custom content between the action groups  
❌ **Don't:** Confuse it with a content slot of the input area

✅ **Do:** Use specific, verb-based labels so that users understand the outcome  
❌ **Don't:** Use generic labels such as "OK"

## Behavior by entered line count — do & don't

✅ **Do:** Start with a compact input that grows as the user types  
❌ **Don't:** Start with a large empty field

✅ **Do:** Switch to internal scrolling once the maximum height is reached  
❌ **Don't:** Let the input push the conversation off the screen

✅ **Do:** Keep a fixed height when the page layout requires it  
❌ **Don't:** Enable expansion in a layout that cannot absorb it

✅ **Do:** Check the scroll inside a scroll on mobile  
❌ **Don't:** Assume that a nested scroll is comfortable on small screens

✅ **Do:** Rely on the planned fixed height for older web browsers  
❌ **Don't:** Depend on automatic expansion in every browser

## Label (can it be hidden?) — do & don't

✅ **Do:** Keep the function clear through placeholder text or a contextual icon when the label is hidden  
❌ **Don't:** Hide the label without replacing its meaning

✅ **Do:** Keep the label available to screen readers  
❌ **Don't:** Remove the label from the accessibility tree

✅ **Do:** Display the label when the interface includes other possible interactions  
❌ **Don't:** Hide it in a layout with several controls

✅ **Do:** Hide the label only when space is limited or the layout is compact  
❌ **Don't:** Hide it for visual preference alone

✅ **Do:** Write a short label in sentence case, without a colon  
❌ **Don't:** Use a long phrase as a label

## Truncated input area — do & don't

✅ **Do:** Respect the native truncation behavior of each environment  
❌ **Don't:** Override it with a custom behavior

✅ **Do:** Show the end of the text when the input loses focus  
❌ **Don't:** Add a visual truncation indicator (...)

✅ **Do:** Keep the entire text accessible when the input regains focus  
❌ **Don't:** Make part of the text unreachable

✅ **Do:** Offer a tooltip on hover in desktop contexts when it helps  
❌ **Don't:** Rely on a tooltip on touch screens

✅ **Do:** Test truncation with long messages  
❌ **Don't:** Assume that the visible text is enough to identify the message

## Multiline and responsiveness — do & don't

✅ **Do:** Apply a max-width of around 640px  
❌ **Don't:** Stretch the input across a very wide screen

✅ **Do:** Use the full available width on mobile or inside a specific container when the template allows it  
❌ **Don't:** Make full width the default rule

✅ **Do:** Let the text scale proportionally with user zoom  
❌ **Don't:** Block text resizing

✅ **Do:** Keep the height and width flexible so the input adapts to the zoom level  
❌ **Don't:** Fix the dimensions of the input

✅ **Do:** Preserve the minimum interactive area when the user zooms out  
❌ **Don't:** Let the input shrink below its minimum size

## Rich text — do & don't

✅ **Do:** Use the matching Strong token sparingly to highlight key information  
❌ **Don't:** Use other text styles or custom font weights

✅ **Do:** Use the dedicated helper link component when a link is required  
❌ **Don't:** Underline text manually

✅ **Do:** Reserve strong text for short, key information such as a character count  
❌ **Don't:** Set a whole sentence in strong text

✅ **Do:** Choose the Strong token that matches the selected text style  
❌ **Don't:** Mix Strong tokens from different text styles in one message

✅ **Do:** Keep supporting text simple  
❌ **Don't:** Add hyperlinks inside the helper text
