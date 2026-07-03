The circular progress indicator must scale proportionally with user zoom and remain clear and readable in all contexts.
The component should preserve its visual structure and proportions regardless of where it is used (standalone or embedded in another component).

**Behavior**
• The loader must scale proportionally with user zoom. Resizing must never be blocked
• The shape, stroke thickness, and spacing must remain consistent at all zoom levels
• The component must remain visually balanced and recognizable at any size
• The loader must not become distorted, pixelated, or clipped

**Layout**
• The component should adapt to its container without breaking its proportions
• When embedded (e.g. button, tag, toast), it must align with surrounding elements while keeping its original ratio
• The component must not stretch to fill available space

**Accessibility**
• The loader must remain visible and distinguishable at all zoom levels
• It must respect reduced motion settings when applicable
• It must not lose meaning or become ambiguous when scaled
• Progress labels must clearly communicate the ongoing process and the affected content for accessibility purposes.