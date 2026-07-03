The linear progress indicator must scale horizontally while preserving a fixed height defined by design tokens.
The component should remain clear, readable, and structurally consistent at all zoom levels and in all contexts.

**Behavior**
• The progress bar scales horizontally with its container when width is constrained
• When used in fill layouts (Auto Layout), the component must respect container bounds and must not overflow its parent
• The component must not grow beyond its container or break layout structure
• The height follows predefined tokens and must not scale freely
• The progress value must remain accurate and visually proportional at all sizes
• The component must not be distorted, stretched vertically, or clipped

**Layout**
• The component can expand to fill available width when used as a standalone element
• In constrained or embedded contexts, it must adapt to the container without exceeding it
• Vertical size is controlled by tokens (track and indicator height)
• When space is reduced, the component must scale proportionally and preserve internal spacing (e.g. between track and indicator)
• The visual ratio between track and indicator must remain consistent

**Helper text**
• The helper text must stay aligned with the progress indicator (start or center)
• Spacing between the helper text and the progress indicator must remain consistent across zoom levels.
• The text must wrap when space is limited and must not overflow the container
• The layout must expand vertically if needed to preserve readability
• Text resizing must never be blocked
• The text must not overlap, truncate, or become unreadable
• The relationship between the text and the progress indicator must remain clear

**Accessibility**
• The indicator must remain visible and distinguishable at all zoom levels
• It must support reduced motion settings when animated
• The text must remain readable at up to 200% zoom
• Contrast must meet accessibility requirements
• Progress labels must clearly communicate the ongoing process and the affected content for accessibility purposes.