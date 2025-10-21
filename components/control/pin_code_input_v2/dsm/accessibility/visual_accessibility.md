### Visual Accessibility

1. Ensure digit box borders, focus indicators, and error outlines have contrast ≥3:1 against adjacent colors.
2. Error state must include both color change (e.g., red border) and a text message below the component; do not rely on color alone.
3. Helper text and error messages must have text contrast ≥4.5:1; large text (≥18pt or ≥14pt bold) requires ≥3:1.
4. Support text resizing up to 200%; boxes and text must reflow without horizontal scrolling or content loss (WCAG 2.1 Reflow).
5. Respect `prefers-reduced-motion` for focus transitions and auto-advance animations; reduce or eliminate motion when requested.