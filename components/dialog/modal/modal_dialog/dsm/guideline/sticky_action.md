**`False`** Actions are positioned directly after the description or content area and move with the content. The action area uses an Auto Layout Hug behavior.

**`True`** Actions remain fixed at the bottom of the modal while the content area can scroll independently. This ensures that primary actions remain continuously visible and accessible, especially when the modal contains a large amount of content.

ℹ️ Note: Fixed height=True is automatically enabled when Sticky action=True.

### ⚠️ Mobile layout
This setting is automatic and changes depending on the grid. The user should not be able to interact with it.

• On mobile (grid: 2xs, xs, sm), the actions can either be stacked vertically or aligned horizontally.  
In both cases, each component can use either “fill” or “hug” behavior in Auto Layout.  
• On tablet and desktop, the actions are aligned horizontally (each component uses an Auto Layout Hug behavior).