✅ **Do:** Always provide a programmatic label using `<label>`, `aria-label`, or `aria-labelledby`  
❌ **Don't:** Rely solely on placeholder text as a label substitute—it disappears when users type

✅ **Do:** Use visually hidden labels (CSS technique) when visual context makes the purpose obvious  
❌ **Don't:** Remove labels entirely from the DOM, breaking accessibility for screen reader users

✅ **Do:** Keep labels concise and descriptive: "Quantity" or "Number of guests" rather than lengthy instructions  
❌ **Don't:** Use vague labels like "Enter value" that don't clarify what the number represents

✅ **Do:** Position visible labels consistently—typically above the input or inline to its left  
❌ **Don't:** Place labels in unexpected positions that break users' scanning patterns

✅ **Do:** Include context in the label when multiple quantity inputs appear together (e.g., "Adults," "Children")  
❌ **Don't:** Use identical generic labels for multiple inputs, forcing users to infer meaning from position alone