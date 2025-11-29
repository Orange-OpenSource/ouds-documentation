**`False`** For a square finish.

**`True`** For a finish with rounded corner. To be favored in more emotional, immersive contexts or those tied to specific visual identities. For standard or business-oriented journeys, keep the default corners. This evolution addresses the need for flexibility in adapting the design to certain brand contexts.

### Do & don'ts

✅ **Do:** Use rounded corners consistently with other form elements in your design system to maintain visual harmony  
❌ **Don't:** Apply rounded corners to quantity inputs while using square corners on adjacent buttons or fields

✅ **Do:** Reserve rounded corners for consumer-facing or lifestyle brand interfaces where softer aesthetics align with brand identity  
❌ **Don't:** Use rounded corners in enterprise or data-heavy applications where sharp edges convey precision

✅ **Do:** Consider rounded corners for mobile interfaces where they may improve perceived touch targets  
❌ **Don't:** Assume rounded corners automatically improve usability—they are primarily a visual treatment

✅ **Do:** Document your corner radius choice in design tokens for consistent application across components  
❌ **Don't:** Mix corner radius values arbitrarily across different quantity input instances

✅ **Do:** Test rounded corner variants with your specific button placement (trailing vs. split) to ensure visual balance  
❌ **Don't:** Apply rounded corners without verifying they work well with increment/decrement button styling

---

### Input status

**`Empty`** The Empty state indicates that the quantity input is blank with no content or placeholder, a neutral starting point.

**`Empty (Placeholder)`** The Empty with Placeholder state provides a hint or guidance inside the field to suggest expected input.

**`Filled`** The Filled state shows that the user has entered valid content into the field, replacing any placeholder.

### Do & don'ts

✅ **Do:** Set a sensible default value (typically 1) to reduce user effort and prevent empty submission errors  
❌ **Don't:** Leave quantity inputs empty in e-commerce contexts where a zero value has no valid meaning

✅ **Do:** Use placeholder text to indicate expected format when the field can be empty (e.g., "Enter quantity")  
❌ **Don't:** Rely solely on placeholders for critical instructions—they disappear once users begin typing

✅ **Do:** Ensure filled state styling provides clear feedback that user input has been captured  
❌ **Don't:** Style filled and empty states identically, making it difficult to scan form completion status

✅ **Do:** Preserve entered values when users navigate away and return to the form  
❌ **Don't:** Reset quantity values unexpectedly, forcing users to re-enter their selections

✅ **Do:** Validate and display the filled state immediately when users type valid numbers  
❌ **Don't:** Delay visual confirmation of valid input, leaving users uncertain if their entry was accepted