# Action card — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([action_card_container.md](action_card_container.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ Presenting a self-contained item that leads to one destination or one action

✅ Promoting a product, offer or service when the whole surface is the target

✅ Opening a help article, tutorial or support topic from a short summary

✅ Displaying a list or grid of comparable items that each open their own detail page

✅ Starting a single task, such as a diagnostic, from a summary of what it does

✅ Linking to an external site from a visual summary of its content

✅ Offering a larger target area than a link or a button alone provides

✅ Building home pages and dashboards with several visual entry points

✅ Leading to a campaign or a landing page from a card with an image background

✅ Showing content that fits a short, scannable summary before the user goes further

## Style — do & don't

✅ **Do:** Use one style (Filled, Outlined or Elevated) for all the cards of a group  
❌ **Don't:** Mix card styles within the same group of cards

✅ **Do:** Place the card in a parent frame with a supported OUDS surface to change its background  
❌ **Don't:** Override the interaction layers of the card by hand

✅ **Do:** Use Elevated on a visible background surface, with the predefined OUDS elevation and background tokens  
❌ **Don't:** Apply a custom shadow or an opacity workaround

✅ **Do:** Keep text, icons and interactive elements readable on inverse and image backgrounds  
❌ **Don't:** Let a background image hide the Hover, Focus or Pressed feedback

✅ **Do:** Choose a background image that stays readable across screen sizes and crops  
❌ **Don't:** Use an image that only decorates the card and adds no context

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

✅ **Do:** Check that Hover, Focus and Pressed stay visible on every Surface you use  
❌ **Don't:** Add an external Surface frame to Elevated or Outlined cards

## Divider — do & don't

✅ **Do:** Use the divider only on Filled cards  
❌ **Don't:** Add a divider to Outlined or Elevated cards

✅ **Do:** Keep the predefined divider color  
❌ **Don't:** Recolor the divider to match the content

✅ **Do:** Apply the same divider choice to all the cards of a group  
❌ **Don't:** Mix cards with and without a divider in one group

✅ **Do:** Rely on the Filled surface for separation when Divider is False  
❌ **Don't:** Draw a manual line in the slot to imitate the divider

✅ **Do:** Use the divider to reinforce the separation from the surrounding surface  
❌ **Don't:** Use it to separate content inside the slot

## Role — do & don't

✅ **Do:** Define the semantic role from what activating the card does  
❌ **Don't:** Give the card a link role when it triggers an action without navigation

✅ **Do:** Use Link for destinations in the same product and External Link for destinations outside it  
❌ **Don't:** Present an external destination as an internal link

✅ **Do:** Keep the entire card as the single interaction target  
❌ **Don't:** Add buttons or links with another destination inside the slot

✅ **Do:** Give the card an accessible name that states its purpose  
❌ **Don't:** Make the accessible name repeat all the content of the slot

✅ **Do:** Use the content card container when the content needs several independent actions  
❌ **Don't:** Force several actions into an action card container
