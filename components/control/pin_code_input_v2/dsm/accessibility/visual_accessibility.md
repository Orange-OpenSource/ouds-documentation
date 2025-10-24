### Visual Accessibility

1. Ensure text and digit content have contrast ≥4.5:1 against background; labels and helper text must meet the same ratio.
2. Ensure input field borders, focus indicators, and error state borders have contrast ≥3:1 against adjacent surfaces.
3. Do not rely on color alone to convey error state; include error icon and descriptive error message text below the fields.
4. Support text resizing up to 200% without loss of content, functionality, or horizontal scrolling (reflow must pass).
5. Respect `prefers-reduced-motion` and avoid auto-advance animations or transitions that rely on motion to convey state changes.