# Card — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([content_card_container.md](content_card_container.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Grouping related information into one non-interactive surface

✅ Presenting content that needs several independent actions, such as a button and links

✅ Pairing instructions or a summary with the next steps the user can take

✅ Arranging independent blocks of content on a dashboard

✅ Separating a block of information from the surrounding page

✅ Combining text, images and nested components in a customizable layout

✅ Building account or settings overviews that hold several links

✅ Presenting offers whose details and actions stay independently accessible

✅ Keeping a defined internal layout across mobile and desktop screens

✅ Cases where the container itself must not receive Hover, Focus or Pressed states

## Style — do & don't

✅ **Do:** Use one style (Filled, Outlined or Elevated) for all the cards of a group  
❌ **Don't:** Mix card styles within the same group of cards

✅ **Do:** Use a parent container to display the card on another supported background surface  
❌ **Don't:** Override the predefined visual properties of the card by hand

✅ **Do:** Keep the card non-interactive whatever its visual treatment  
❌ **Don't:** Use Elevated to suggest that the whole card can be clicked

✅ **Do:** Adapt text, icons and interactive elements to the theme of an inverse background  
❌ **Don't:** Keep colors that lose contrast on an inverse background

✅ **Do:** Use only the predefined stroke, divider and background colors  
❌ **Don't:** Apply custom colors to the card

## Rounded corner — do & don't

✅ **Do:** Apply one corner treatment across the whole product or service  
❌ **Don't:** Mix rounded and square cards in the same product or service

✅ **Do:** Use rounded corners only with the themes that support them: Orange and Orange Compact  
❌ **Don't:** Expect rounded corners on the Sosh and Wireframe themes

✅ **Do:** Let the brand theme decide the corner treatment  
❌ **Don't:** Change the corners of a single card to give it more emphasis

✅ **Do:** Check that images and nested elements follow the corners of the card  
❌ **Don't:** Let slot content overflow a rounded corner

✅ **Do:** Keep the same corner treatment in every state of the card  
❌ **Don't:** Switch between rounded and square when the state changes

## Background — do & don't

✅ **Do:** Use the Background property on Filled and Elevated cards in the Enabled state  
❌ **Don't:** Expect the Background property on an Outlined card

✅ **Do:** Use an external Surface frame with predefined OUDS tokens to customize the base of a Filled card  
❌ **Don't:** Modify or replace the internal Background layer by hand

✅ **Do:** Match the corner-radius token of the external Surface frame to the card when Rounded corner is True  
❌ **Don't:** Leave a square Surface frame behind a rounded card

✅ **Do:** Set the Background property independently of the selected Surface  
❌ **Don't:** Use the Background property as a replacement for the surface

✅ **Do:** Keep the base background of an Elevated card on its predefined surface  
❌ **Don't:** Add an external Surface frame to Elevated or Outlined cards

## Divider — do & don't

✅ **Do:** Use the divider only on Filled cards  
❌ **Don't:** Add a divider to Outlined or Elevated cards

✅ **Do:** Keep the predefined divider color  
❌ **Don't:** Recolor the divider by hand

✅ **Do:** Keep the divider along the bottom edge of the card  
❌ **Don't:** Add lines on the other edges of the card

✅ **Do:** Apply the same divider choice to all the cards of a group  
❌ **Don't:** Mix cards with and without a divider in one group

✅ **Do:** Rely on the surface color for separation when Divider is False  
❌ **Don't:** Draw a manual line in the slot to imitate the divider

## Slot spacing — do & don't

✅ **Do:** Define the padding and spacing of the content with OUDS spacing tokens  
❌ **Don't:** Use arbitrary spacing values in the slot

✅ **Do:** Use fixed space when the spacing must stay the same on mobile and desktop  
❌ **Don't:** Use fixed space for a layout that has to adapt to the screen

✅ **Do:** Use scaled space when the spacing must adapt to the screen reference  
❌ **Don't:** Change spacing by hand from one screen size to another

✅ **Do:** Preserve the internal spacing and corner-radius rules of nested components  
❌ **Don't:** Override the spacing of a nested component to fit the card

✅ **Do:** Test the layout with short and long content before adding more  
❌ **Don't:** Fill a card with dense, repetitive content that belongs in a list or a table

## Role — do & don't

✅ **Do:** Keep the card non-interactive and give each element in the slot its own semantic role  
❌ **Don't:** Give the card container a button or link role

✅ **Do:** Use Link for in-product destinations, External Link for outside destinations and Button for actions  
❌ **Don't:** Use a link to trigger an action without navigation

✅ **Do:** Place the actions of the card consistently, at the end of its content  
❌ **Don't:** Scatter actions through the text of the card

✅ **Do:** Give every interactive element an accessible name that makes sense on its own  
❌ **Don't:** Repeat vague labels such as "Learn more" without context

✅ **Do:** Use the action card container when the whole content leads to a single action  
❌ **Don't:** Wrap a content card container in one link
