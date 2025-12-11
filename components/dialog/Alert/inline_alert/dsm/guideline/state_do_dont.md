✅ **Do:** Use the skeleton state during asynchronous content loading to maintain layout stability and prevent content shifting  
❌ **Don't:** Show an empty container or leave blank space while alert content is being fetched

✅ **Do:** Ensure the enabled state is immediately visible when content becomes available without unnecessary animation delays  
❌ **Don't:** Add excessive entrance animations that slow down the display of important alert information

✅ **Do:** Maintain consistent dimensions between skeleton and enabled states to prevent layout jumps  
❌ **Don't:** Allow the skeleton placeholder to have different proportions than the final rendered alert

✅ **Do:** Use skeleton states only for genuinely asynchronous content that requires loading time  
❌ **Don't:** Display skeleton placeholders for static alerts that can be rendered immediately

✅ **Do:** Provide clear visual distinction between skeleton and enabled states so users understand content is loading  
❌ **Don't:** Make skeleton states so subtle that users cannot distinguish them from broken or missing content