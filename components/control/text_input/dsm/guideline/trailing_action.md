Provides direct, quick interaction within the input field (show/hide password, clear field, open dropdown). This action must enhance efficiency without cluttering the interface.

### Do & don'ts

✅ **Do:** Use clear buttons to let users quickly empty a filled input field, especially for search inputs.  
❌ **Don't:** Show clear buttons on empty inputs—they should only appear when there's content to clear.

✅ **Do:** Provide show/hide toggles for password fields so users can verify their input before submitting.  
❌ **Don't:** Make trailing actions too small to tap easily—maintain minimum touch target sizes (48dp).

✅ **Do:** Use descriptive `aria-label` attributes for trailing action buttons (e.g., "Show password", "Clear search").  
❌ **Don't:** Stack multiple trailing actions that create visual clutter or confusion about their functions.

✅ **Do:** Ensure trailing actions are keyboard accessible and receive visible focus indicators.  
❌ **Don't:** Place critical functionality only in trailing actions—provide alternative access methods.

✅ **Do:** Design trailing actions to be clearly distinct from the input content itself.  
❌ **Don't:** Use trailing actions for primary submit functions—reserve them for field-level utilities.