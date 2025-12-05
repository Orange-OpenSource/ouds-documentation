✅ **Do:** Use the disabled state only when the switch will become available based on another condition or user action.  
❌ **Don't:** Disable switches without providing context about why or how to enable them.

✅ **Do:** Ensure the focus state has a visible indicator with at least 3:1 contrast ratio against adjacent colors.  
❌ **Don't:** Remove the default focus outline without providing an equally prominent custom indicator.

✅ **Do:** Use skeleton states during initial page load to indicate where interactive content will appear.  
❌ **Don't:** Display skeleton states for more than a few seconds as users may perceive this as broken functionality.

✅ **Do:** Make the read-only state visually distinct from disabled to communicate that the value is intentionally locked.  
❌ **Don't:** Use read-only when disabled would be more appropriate—read-only implies the value is meaningful and intentional.

✅ **Do:** Provide visual feedback during the pressed state to confirm the user's action was registered.  
❌ **Don't:** Allow the pressed state to persist longer than necessary as it may confuse users about the actual toggle state.