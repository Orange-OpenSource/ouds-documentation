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