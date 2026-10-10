### Slot
Use Slot for custom leading content that cannot be represented by Icon, Image, Avatar or Flag.  
Slot provides flexibility for specific product requirements but should be used as an exception rather than the default solution.

&nbsp;

### ⚠️ Interaction
The complete Accordion trigger already controls whether its associated content is expanded or collapsed.

Custom Slot content inside the trigger must not contain:  
• Buttons  
• Links  
• Checkboxes  
• Radio buttons  
• Toggles  
• Menus  
• Any independently focusable element

Nested interactive elements create conflicting activation and focus behaviour and may make it unclear whether an interaction expands the accordion or activates another control.  
When an independent action is required, place it inside the expanded content or use another component designed to support multiple actions.
