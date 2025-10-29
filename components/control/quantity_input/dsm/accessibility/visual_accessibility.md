## Visual Accessibility

1. Ensure text contrast ≥4.5:1 for label, input text, and helper text; large text contrast ≥3:1.
2. Ensure UI components (buttons, borders, focus indicators) have contrast ≥3:1 against adjacent colors.
3. Do not rely solely on color to convey error state; include text messages, icons, or border thickness changes.
4. Support text resizing up to 200% (browser zoom) without loss of content or functionality; content must reflow properly.
5. Respect `prefers-reduced-motion` by avoiding or minimizing animations for value changes and state transitions.
6. Ensure focus indicators are clearly visible and maintain ≥3:1 contrast against the background.