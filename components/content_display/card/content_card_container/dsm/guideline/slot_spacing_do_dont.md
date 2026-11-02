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