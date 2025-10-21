## Visual Accessibility

1. Ensure text contrast ≥4.5:1 for digit values and helper text; large text ≥3:1.
2. Ensure digit box borders and focus indicators have contrast ≥3:1 against the background.
3. Do not rely on color alone for error state; add error icons or text indicators below the component.
4. Support text resizing up to 200% without loss of content or functionality; digit boxes must reflow gracefully.
5. Respect `prefers-reduced-motion` for any animations related to focus transitions or error state changes.