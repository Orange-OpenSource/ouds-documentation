✅ **Do:** Wait for the unified Accordion component study before implementing expand functionality  
❌ **Don't:** Create custom expand link implementations that may conflict with future Accordion patterns

✅ **Do:** Use existing disclosure patterns like Accordion or Collapsible for expand/collapse functionality  
❌ **Don't:** Attempt to recreate expand behavior using the current Link component

✅ **Do:** Document any interim expand solutions with clear migration paths to future components  
❌ **Don't:** Ship expand link variations that lack proper ARIA attributes for accessibility

✅ **Do:** Consider using Button component for toggle actions until Expand variant is supported  
❌ **Don't:** Blur the distinction between navigation links and stateful toggle controls

✅ **Do:** Provide feedback to the design system team about expand/collapse use cases  
❌ **Don't:** Assume the current limitation will prevent all disclosure pattern implementations